# Access Management Resource

{{{ docsVersionInfo.k0rdentName }}} provides an `AccessManagement` resource (cluster-scoped, singleton) that
enables controlled distribution of multiple object types (`ClusterTemplate`, `ServiceTemplate`, `Credential`, and
`ClusterAuthentication`) from the system namespace (default: `kcm-system`) across other namespaces in the management
cluster. This resource is created automatically during the installation of {{{ docsVersionInfo.k0rdentName }}}.

## Supported Configuration Options

The `AccessManagement` has a numver of parameters you can adjust.

* `spec.accessRules` - A list of access rules that define how specific objects should be distributed.

Each access rule supports the following fields:

* `targetNamespaces` - Determines which namespaces selected objects should be distributed to.
If omitted, objects are distributed to all namespaces.

    You may customize this field, but you may use only one of the following mutually-exclusive selectors:

    * `targetNamespaces.stringSelector` - A label query to select namespaces (type: `string`).
    * `targetNamespaces.selector` - A structured label query to select namespaces (type: `metav1.LabelSelector`)
    * `targetNamespaces.list` - The list of namespaces to select (type: `[]string`).

* `clusterTemplateChains` - The list of `ClusterTemplateChain` names whose `ClusterTemplates` will be distributed
to all namespaces specified in `targetNamespaces`.

* `serviceTemplateChains` - The list of `ServiceTemplateChain` names whose `ServiceTemplates` will be distributed
  to all namespaces specified in `targetNamespaces`.

* `credentials` - The list of `Credential` names that will be distributed to all the namespaces specified in
`targetNamespaces`.

* `clusterAuthentications` - The list of `ClusterAuthentication` names that will be distributed to all the namespaces
specified in `targetNamespaces`.

Consider this example:

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

For the example above the following objects will be distributed following these rules:

1. All `ClusterTemplates` referenced by `ClusterTemplateChain` `ct-chain1` are distributed to `namespace1` and `namespace2`.
2. All `ServiceTemplates` referenced by `ServiceTemplateChain` `st-chain1` are distributed to `namespace1` and `namespace2`.
3. The `Credential` `cred1` and all referenced `Identity` resources are distributed to `namespace1` and `namespace2`.
4. The `ClusterAuthentication` `auth1` and its referenced CA secret are distributed to `namespace3`.

See [Credential Distribution System](credentials/credentials-propagation.md#the-credential-distribution-system)
and [Template Life Cycle Management](../../reference/template/index.md#template-life-cycle-management) for more details
about distributing `Credential`, `ClusterTemplate` and `ServiceTemplate` objects.
