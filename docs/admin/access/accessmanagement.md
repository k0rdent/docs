# Access Management Resource

{{{ docsVersionInfo.k0rdentName }}} provides an `AccessManagement` resource (cluster-scoped, singleton) that enables controlled distribution of multiple object types (`ClusterTemplate`, `ServiceTemplate`, `Credential`, and `ClusterAuthentication`) from the system namespace (default: `kcm-system`) across other namespaces in the management cluster. This resource is created automatically during the installation of {{{ docsVersionInfo.k0rdentName }}}.

## Supported Configuration Options

This section describes the fields available in `AccessManagement.spec` and how they control object distribution.

The `AccessManagement` resource has a number of parameters you can adjust.

* `spec.accessRules` – A list of access rules that define how specific objects are distributed.

Each access rule supports the following fields:

### Namespace Selection

* `targetNamespaces` – Determines which namespaces selected objects are distributed to.
  If omitted, objects are distributed to all namespaces.

  You may specify only one of the following mutually exclusive selectors:

  * `targetNamespaces.stringSelector` – A label query to select namespaces (type: `string`).
  * `targetNamespaces.selector` – A structured label query to select namespaces (type: `metav1.LabelSelector`).
  * `targetNamespaces.list` – A list of namespaces to select (type: `[]string`).

### Distributed Object Types

* `clusterTemplateChains` – The list of `ClusterTemplateChain` names whose `ClusterTemplates` are distributed to the selected namespaces.

* `serviceTemplateChains` – The list of `ServiceTemplateChain` names whose `ServiceTemplates` are distributed to the selected namespaces.

* `credentials` – The list of `Credential` names that are distributed to the selected namespaces.

* `clusterAuthentications` – The list of `ClusterAuthentication` names that are distributed to the selected namespaces.

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
    clusterTemplateChains:
    - ct-chain1
    serviceTemplateChains:
    - st-chain1
    credentials:
    - cred1
  - targetNamespaces:
      list:
      - namespace3
    clusterAuthentications:
    - auth1
```

Based on the configuration above, the following objects are distributed:

1. All `ClusterTemplates` referenced by the `ClusterTemplateChain` `ct-chain1` are distributed to `namespace1` and `namespace2`.
2. All `ServiceTemplates` referenced by the `ServiceTemplateChain` `st-chain1` are distributed to `namespace1` and `namespace2`.
3. The `Credential` `cred1` and all referenced `Identity` resources (used for authentication) are distributed to `namespace1` and `namespace2`.
4. The `ClusterAuthentication` `auth1` and its referenced CA secret are distributed to `namespace3`.

For more details, see:

* [Credential Distribution System](credentials/credentials-propagation.md#the-credential-distribution-system)
* [Template Life Cycle Management](../../reference/template/index.md#template-life-cycle-management)
