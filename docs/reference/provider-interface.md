# ProviderInterface

`ProviderInterface` is a cluster-scoped CRD that defines the contract between {{{ docsVersionInfo.k0rdentName }}} and an infrastructure provider. It tells the system which Kubernetes resource kinds a provider manages and how to locate credential identity objects for that provider.

Each infrastructure provider Helm chart ships with a pre-configured `ProviderInterface` object. Custom or bring-your-own providers must supply their own.

**Short name:** `pi`  
**Scope:** Cluster

## Spec Fields

### `.spec.description`

Human-readable explanation of what this provider does.

```yaml
spec:
  description: "AWS infrastructure provider for Cluster API"
```

### `.spec.clusterGVKs`

> WARNING:
> Removed in {{{ docsVersionInfo.k0rdentName }}} `v1.11.0`.

List of Group-Version-Kind (GVK) tuples identifying the cluster resource kinds this provider manages. Used by {{{ docsVersionInfo.k0rdentName }}} to locate infrastructure cluster objects for a given `ClusterDeployment`.

```yaml
spec:
  clusterGVKs:
    - group: infrastructure.cluster.x-k8s.io
      version: v1beta2
      kind: AWSCluster
    - group: infrastructure.cluster.x-k8s.io
      version: v1beta2
      kind: AWSManagedCluster
```

**Fields per entry:**

- `group` (string): API group
- `version` (string): API version
- `kind` (string): Resource kind

### `.spec.clusterIdentities`

List of `ClusterIdentity` types supported by this provider, along with instructions for resolving their transitive references (e.g., Secrets referenced by the identity object). Used by the Cluster Identity distribution mechanism to propagate credentials across namespaces and regions.

```yaml
spec:
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
```

**`ClusterIdentity` fields:**

- `group` (string): API group of the identity object
- `version` (string): API version of the identity object
- `kind` (string): Kind of the identity object
- `references[]`: List of objects transitively referenced by this identity (see below)

**`ClusterIdentityReference` fields:**

- `group` (string): API group of the referenced object
- `version` (string): API version of the referenced object
- `kind` (string): Kind of the referenced object
- `nameFieldPath` (string, required): Dot-separated field path in the identity object where the referenced object's name can be found. Cannot start with `.`. Example: `spec.clientSecret.name`
- `namespaceFieldPath` (string): Dot-separated field path in the identity object where the referenced object's namespace can be found. Cannot start with `.`. Defaults to the system namespace. Example: `spec.clientSecret.namespace`

### `.spec.clusterIdentityKinds`

> **Deprecated**: Use `.spec.clusterIdentities` instead.

Legacy list of identity kind strings. Does not support reference resolution.

```yaml
spec:
  clusterIdentityKinds:
    - AzureClusterIdentity
```

## Full Example

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ProviderInterface
metadata:
  name: cluster-api-provider-azure
  annotations:
    helm.sh/resource-policy: keep
spec:
  description: "Azure infrastructure provider for Cluster API"
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
```

## Viewing ProviderInterfaces

```bash
# List all ProviderInterfaces
kubectl get providerinterfaces

# Or using the short name
kubectl get pi

# Describe a specific one
kubectl describe pi cluster-api-provider-aws
```

## Related Documentation

- [Cluster Identity Distribution](../admin/access/credentials/cluster-identity-distribution.md) — how `ProviderInterface` enables credential propagation across namespaces and regions
- [Credentials Propagation](../admin/access/credentials/credentials-propagation.md) — broader credentials management overview
- [Bring Your Own Templates](template/template-byo.md) — creating custom provider templates that include a `ProviderInterface`
