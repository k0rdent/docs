# KCM Region With KOF

## KCM/KOF Regional Cluster

### KCM Region Installation

To install KOF on a KCM Regional Cluster, you first need to set up all required components. Please follow this documentation to create a [KCM Region Cluster](../../admin/regional-clusters/creating-credential-in-region.md).

When setting up a KCM Regional cluster to work with KOF, make sure the correct labels are applied for resource propagation:

* `k0rdent.mirantis.com/kcm-region-cluster: "true"` - Enables propagation of templates and required resources to the regional cluster.
* `k0rdent.mirantis.com/kof-aws-dns-secrets: "true"` - Propagates AWS DNS secrets to the regional cluster.
* `k0rdent.mirantis.com/kof-storage-secrets: "true"` - Propagates storage secrets to the regional cluster.

To prevent conflicts with an existing CertManager installation, disable CertManager in the KCM Region configuration. KOF will deploy its own CertManager instance automatically. Add the following configuration to the Region spec:

```yaml
spec:
  core:
    kcm:
      config:
        cert-manager:
          enabled: false
```

> NOTE:
> When creating a ClusterDeployment for a KCM Region, use a name shorter than 15 characters. Longer names may cause deployment errors.

> NOTE:
> These labels are required when using KOF. To propagate resources to KCM child clusters, all necessary resources must first exist in the KCM Regional cluster. These labels will be deprecated in the future once KCM automatically propagates all required resources, as currently handled by the MultiClusterService.

### KOF Region Installation

A KCM Regional cluster can also act as a KOF Regional cluster if it has enough capacity to deploy KOF Regional cluster workloads.
To enable this, add the following label to the KCM Regional ClusterDeployment:

```yaml
k0rdent.mirantis.com/kof-cluster-role: regional
```

> NOTE:
> KCM Regional and KOF Regional should be the same cluster. Don't install KOF Regional to an isolated KCM Child not seen from the Management cluster.

> NOTE:
> A KCM Regional cluster cannot be extended with a KOF child role, but you can deploy a separate KOF child cluster within the same KCM Region if needed.

Make sure to apply all the main [KOF Regional Cluster](kof-install.md#regional-cluster) steps for this `ClusterDeployment`.
### Istio Installation

If you want to use Istio in the KCM Regional cluster, add the following labels to the KCM Regional ClusterDeployment:

```yaml
k0rdent.mirantis.com/istio-mesh: <REGION_NAME>
k0rdent.mirantis.com/istio-gateway: "true"
k0rdent.mirantis.com/istio-role: member
```

> NOTE:
> The `k0rdent.mirantis.com/istio-mesh` label allows propagating `remote secrets` only to clusters that have this label. If this label is not set, remote secrets will be propagated across all regions.

> NOTE:
> To enable connectivity between a child cluster and the regional cluster, set the `k0rdent.mirantis.com/istio-mesh` label with the same `<REGION_NAME>` value on both clusters.

## Deploying Child Clusters in a KCM Region

By now you have created the Region, Credential, and ClusterDeployment resources.
The KCM/KOF Regional cluster is up and running.

To deploy child clusters within a KCM Region, use the standard cluster templates but reference the regional credentials in the `ClusterDeployment` specification.

Example:

```bash
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ClusterDeployment
metadata:
  name: <CHILD_CLUSTER_NAME>
  namespace: kcm-system
  labels:
    k0rdent.mirantis.com/kof-cluster-role: child
spec:
  template: aws-standalone-cp-1-0-16
  credential: <REGION_CREDENTIALS>
...
```

Make sure to apply all the main [KOF Child Cluster](kof-install.md#child-cluster) steps for this `ClusterDeployment`.
> NOTE:
> Within a KCM Region, all KOF clusters (both kof-regional and kof-child) operate in isolation from any KOF clusters that are not part of the same Region.
