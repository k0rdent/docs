# Access Management Resource

{{{ docsVersionInfo.k0rdentName }}} provides an `AccessManagement` resource (cluster-scoped, singleton) that enables
controlled distribution of objects from the system namespace (default: `kcm-system`) across other namespaces in the
management cluster. It supports the built-in {{{ docsVersionInfo.k0rdentName }}} object types (`ClusterTemplate`, `ClusterTemplateChain`,
`ServiceTemplateChain`, `Credential`, `ClusterAuthentication`, `DataSource`, `ClusterAuditPolicy` and `RBACPolicy`) as
well as any other namespaced Kind, including custom resources. This resource is created automatically during the
installation of {{{ docsVersionInfo.k0rdentName }}}.

## Supported Configuration Options

This section describes the fields available in `AccessManagement.spec` and how they control object distribution.

* `spec.accessRules` – A list of access rules that define how specific objects are distributed.

Each access rule supports the following fields:

### Namespace Selection

* `targetNamespaces` – Determines which namespaces selected objects are distributed to.
  If omitted, objects are distributed to all namespaces.

  You may specify only one of the following mutually exclusive selectors:

  * `targetNamespaces.stringSelector` – A label query to select namespaces (type: `string`).
  * `targetNamespaces.selector` – A structured label query to select namespaces (type: `metav1.LabelSelector`).
  * `targetNamespaces.list` – A list of namespaces to select (type: `[]string`).

### Distributed Objects

* `resources` – A list of resource rules. Each entry selects a set of objects of a given Kind in the system
  namespace to distribute to the namespaces selected by `targetNamespaces`.

Each resource rule supports the following fields:

* `kind` (required) – The Kind of the objects to distribute. Any namespaced Kind is accepted, whether it is a
  built-in {{{ docsVersionInfo.k0rdentName }}} Kind or a custom resource. Cluster-scoped Kinds are skipped and
  reported in the `AccessManagement` status, because only namespaced objects can be distributed.
* `apiGroup` – The API group of the Kind, for example `k0rdent.mirantis.com` or the API group of a custom resource.
  You can omit it for the built-in Kinds (`ClusterTemplate`, `ClusterTemplateChain`, `ServiceTemplateChain`,
  `Credential`, `ClusterAuthentication`, `DataSource`, `ClusterAuditPolicy` and `RBACPolicy`), in which case it defaults to
  `k0rdent.mirantis.com`.
  For any other Kind, an omitted `apiGroup` means the core (empty) API group, for example for `ConfigMap`.

You may specify only one of the following mutually exclusive object selectors. If none of them is set, all objects of
the given Kind in the system namespace are distributed.

* `names` – An explicit list of object names in the system namespace (type: `[]string`).
* `selector` – A structured label query to select objects in the system namespace (type: `metav1.LabelSelector`).
* `stringSelector` – A label query in string form to select objects in the system namespace (type: `string`).

Depending on the Kind, distribution works as follows:

* `ClusterTemplateChain` / `ServiceTemplateChain` – The chain is distributed, and so are all the `ClusterTemplate`
  or `ServiceTemplate` objects it references.
* `ClusterTemplate` – The `ClusterTemplate` is distributed without the chart source of its own: the copy references
  the `HelmChart` the source `ClusterTemplate` has been reconciled into (`spec.helm.chartRef`), the same way as copies
  distributed by a `ClusterTemplateChain`. The source `ClusterTemplate` must be valid. Until it is, the distribution
  fails and is retried, and the error is reported in the `AccessManagement` status.
* `Credential` – The `Credential` and all referenced `Identity` resources (used for authentication) are distributed.
* `ClusterAuthentication` – The `ClusterAuthentication` and its referenced CA secret are distributed.
* Any other Kind – The object is copied as is to the target namespaces.

Distributed copies are labeled with `k0rdent.mirantis.com/managed: "true"` and have an owner reference to the
`AccessManagement` object. When an object stops matching an access rule, or a target namespace is no longer selected,
the corresponding copy is removed. If the copy has other owners as well, for example a `ClusterTemplate` that a
`ClusterTemplateChain` also distributes to the same namespace, only the owner reference to the `AccessManagement`
object is removed, and the copy is kept for its other owners.

Deleting the `AccessManagement` object, for example as part of the `Management` object deletion, removes all the
copies it distributed through the Kubernetes garbage collection. Copies distributed by previous versions of
{{{ docsVersionInfo.k0rdentName }}} are adopted, and the owner reference is added to them on the next reconciliation.

> NOTE:
> A `ClusterTemplate` in the system namespace that owns a `HelmChart` cannot be deleted while other `ClusterTemplate`
> objects, such as copies distributed by an `AccessManagement` or a `ClusterTemplateChain`, reference that chart.
> Deleting the source would leave the copies, and the clusters deployed from them, referencing a chart that no longer
> exists. Stop distributing the template and wait for the copies to be removed before deleting it.

> NOTE:
> The KCM controller manages the RBAC permissions needed to distribute the referenced Kinds automatically. It
> maintains a dedicated `ClusterRole` that grants access only to the Kinds currently referenced in
> `spec.accessRules`.

> NOTE:
> Changes to source objects of the referenced Kinds are picked up periodically, so it may take up to a couple of
> minutes for them to be propagated to the target namespaces.

### Example

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: AccessManagement
metadata:
  labels:
    k0rdent.mirantis.com/component: kcm
  name: kcm
spec:
  accessRules:
  - targetNamespaces:
      list:
      - namespace1
      - namespace2
    resources:
    - kind: ClusterTemplateChain
      names:
      - ct-chain1
    - kind: ServiceTemplateChain
      names:
      - st-chain1
    - kind: Credential
      names:
      - cred1
  - targetNamespaces:
      list:
      - namespace3
    resources:
    - kind: ClusterAuthentication
      names:
      - auth1
    - kind: ClusterAuditPolicy
      names:
      - audit-policy1
    - kind: ClusterTemplate
      names:
      - aws-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsStandaloneCpCluster }}}
  - targetNamespaces:
      stringSelector: "team=dev"
    resources:
    - apiGroup: k0rdent.mirantis.com
      kind: DataSource
      selector:
        matchLabels:
          env: dev
    - kind: ConfigMap
      stringSelector: "shared=true"
```

Based on the configuration above, the following objects are distributed:

1. All `ClusterTemplates` referenced by the `ClusterTemplateChain` `ct-chain1` are distributed to `namespace1` and `namespace2`.
2. All `ServiceTemplates` referenced by the `ServiceTemplateChain` `st-chain1` are distributed to `namespace1` and `namespace2`.
3. The `Credential` `cred1` and all referenced `Identity` resources (used for authentication) are distributed to `namespace1` and `namespace2`.
4. The `ClusterAuthentication` `auth1` and its referenced CA secret are distributed to `namespace3`.
5. The `ClusterAuditPolicy` `audit-policy1` is distributed to `namespace3`.
6. The `ClusterTemplate` `aws-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsStandaloneCpCluster }}}` is distributed to `namespace3`.
7. All `DataSource` objects labeled with `env: dev` are distributed to all namespaces labeled with `team=dev`.
8. All `ConfigMap` objects labeled with `shared=true` are distributed to all namespaces labeled with `team=dev`.

## Status

The `AccessManagement` status reports the result of the last reconciliation:

* `status.current` – The applied access rules configuration.
* `status.error` – The aggregate error that occurred during the reconciliation, if any.
* `status.resources` – The outcome for each distinct Kind referenced in `spec.accessRules`. Each entry contains
  `apiGroup`, `kind` and, if the Kind failed to be processed, an `error` message (for example, when the referenced
  object is not found or the Kind is cluster-scoped).

To check the status, run:

```bash
kubectl get accessmanagement kcm -o jsonpath='{.status}'
```

## Backward Compatibility

Before {{{ docsVersionInfo.k0rdentName }}} v1.12.0, each distributable object type had its own dedicated field in the
access rule. These fields are deprecated in favor of `resources`, but are still supported for backward compatibility,
so existing `AccessManagement` configurations keep working without any changes:

| Deprecated field         | Equivalent `resources` entry                        |
|--------------------------|-----------------------------------------------------|
| `clusterTemplateChains`  | `kind: ClusterTemplateChain` with `names`           |
| `serviceTemplateChains`  | `kind: ServiceTemplateChain` with `names`           |
| `credentials`            | `kind: Credential` with `names`                     |
| `clusterAuthentications` | `kind: ClusterAuthentication` with `names`          |
| `dataSources`            | `kind: DataSource` with `names`                     |
| `clusterAuditPolicies`   | `kind: ClusterAuditPolicy` with `names`             |

For example, the following access rule in the previous format:

```yaml
spec:
  accessRules:
  - targetNamespaces:
      list:
      - namespace1
    clusterTemplateChains:
    - ct-chain1
    credentials:
    - cred1
```

is equivalent to:

```yaml
spec:
  accessRules:
  - targetNamespaces:
      list:
      - namespace1
    resources:
    - apiGroup: k0rdent.mirantis.com
      kind: ClusterTemplateChain
      names:
      - ct-chain1
    - apiGroup: k0rdent.mirantis.com
      kind: Credential
      names:
      - cred1
```

When you create or update an `AccessManagement` object that uses the deprecated fields, the admission webhook
automatically converts them into equivalent `resources` entries and clears the deprecated fields. If the webhook is
disabled, the controller still honors the deprecated fields of any access rule that has no `resources` set.

> WARNING:
> The deprecated fields will be removed in a future API version. Use `resources` for new configurations and
> avoid mixing the deprecated fields with `resources` in the same access rule.

For more details, see:

* [Credential Distribution System](credentials/credentials-propagation.md#the-credential-distribution-system)
* [Template Life Cycle Management](../../reference/template/index.md#template-life-cycle-management)
