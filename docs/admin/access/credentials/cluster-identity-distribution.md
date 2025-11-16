# Cluster Identity Distribution

To deploy clusters correctly, the `ClusterIdentity` object (for example, `AWSClusterStaticIdentity`) and all of its
referenced resources (such as `Secrets`) must exist in the same cluster where the CAPI objects are created.
This configuration is different for each provider.

Starting from v1.5.0 the Cluster Identity Distribution system was introduced. This applies to the regional `Credential`
objects (with `spec.region`) and for the `Credential` distributed by the {{{ docsVersionInfo.k0rdentName }}}
AccessManagement system (Credentials with `k0rdent.mirantis.com/managed: "true"` label)
(see [The Credential Distribution System](credentials-propagation.md#the-credential-distribution-system)).

> WARNING:
> To ensure proper Cluster Identity distribution, make sure the following requirements are met:
> 
> 1. The ProviderInterface object is correctly configured. For details, see 
> [ProviderInterface Configuration](#providerinterface-configuration).
> 
> 2. When distributing `ClusterIdentity` objects to regional clusters, the provider that defines the corresponding
> `ClusterIdentity` CRDs must be enabled on the management and on the regional cluster. For example, to distribute
> an `AWSClusterStaticIdentity` to a regional cluster, the AWS provider must be enabled on both the
> management and regional clusters.

## Cluster Identity Distribution Process

When you create a `Credential` object, Cluster Identity distribution begins. The example below walks through
the process step-by-step:

1. User creates the following `Credential` and identity objects for the Azure provider in `region1` region:

    > NOTE:
    > The Secret name needs to follow a pattern, see [credential secret](../../../appendix/appendix-providers.md#credential-secret) for more detail. 

    ```yaml
    apiVersion: k0rdent.mirantis.com/v1beta1
    kind: Credential
    metadata:
      name: azure-cluster-credential
      namespace: test
    spec:
      region: region1
      description: "Azure Credential Example"
      identityRef:
        apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
        kind: AzureClusterIdentity
        name: azure-cluster-identity
        namespace: test
    ---
    apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
    kind: AzureClusterIdentity
    metadata:
      name: azure-cluster-identity
      namespace: test
    spec:
      allowedNamespaces: {}
      clientID: "${AZURE_CLIENT_ID}"
      clientSecret:
        name: azure-cluster-identity-secret
        namespace: test
      tenantID: "${AZURE_TENANT_ID}"
      type: ServicePrincipal
    ---
    apiVersion: v1
    kind: Secret
    metadata:
      name: azure-cluster-identity-secret
      namespace: test
      labels:
        k0rdent.mirantis.com/component: "kcm"
    stringData:
      clientSecret: "${AZURE_CLIENT_SECRET}"
    type: Opaque
    ```
   
2. The KCM controller retrieves all the `ProviderInterfaces` from the regional cluster registered with `region1` Region
and looks for the `AzureClusterIdentity` object definition under `spec.clusterIdentities` of each `ProviderInterface`
object. If nothing found, the cluster identity distribution will not work.

3. The KCM controller copies the `test/azure-cluster-identity-secret` `Secret` and `test/azure-cluster-identity`
`AzureClusterIdentity` objects from the management to the regional cluster.

## ProviderInterface Configuration

A `Credential` in k0rdent could reference more than one `ClusterIdentity` type and each of those identities might have
its own transitive references.
It’s important to have a mechanism to reliably identify all referenced resources to e.g. distribute them across
namespaces and multiple regions.

The `ProviderInterface` object which is a part of the `ProviderTemplate` should define a set of identity kinds, each
with its own reference-resolution instructions. Providers included with {{{ docsVersionInfo.k0rdentName }}} already
have a preconfigured ProviderInterface as part of the `ProviderTemplate`. If you are using a custom or Bring-Your-Own
provider, you must properly configure the ProviderInterface `spec.clusterIdentities` field to enable Cluster
Identity distribution.

The example of the `ProviderInterface` object for the Azure provider:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ProviderInterface
metadata:
  name: cluster-api-provider-azure
  annotations:
    helm.sh/resource-policy: keep
spec:
  clusterGVKs:
    - group: infrastructure.cluster.x-k8s.io
      version: v1beta1
      kind: AzureCluster
    - group: infrastructure.cluster.x-k8s.io
      version: v1alpha1
      kind: AzureASOManagedCluster
  clusterIdentities:
    - group: infrastructure.cluster.x-k8s.io
      version: v1beta1
      kind: AzureClusterIdentity
      references:
        - group: ""
          version: v1
          kind: Secret
          nameFieldPath: spec.clientSecret.name
          namespaceFieldPath: spec.clientSecret.namespace
    - group: ""
      version: v1
      kind: Secret
  description: "Azure infrastructure provider for Cluster API"
```

The `spec.clusterIdentities` section defines the cluster identity objects supported by this provider. Each item
of the `clusterIdentities` array defines how to locate and resolve a referenced object associated with
a ClusterIdentity.

At the moment of writing, the Azure provider supports two kinds of Cluster Identities: `AzureClusterIdentity` and
`Secret`. `Secret` identities do not have any transitive references while the `AzureClusterIdentity` references
a `Secret` with the name defined under `spec.clientSecret.name` and the namespace defined under
`spec.clientSecret.namespace`.

> WARNING:
> Cluster Identity distribution will not work if the ProviderInterface for a particular provider does not exist or
> does not have `spec.clusterIdentities` field defined. The KCM controller will not fail, but it will not create any cluster
> identity resources automatically. You will have to create it manually.


