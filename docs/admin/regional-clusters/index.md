# Regional Clusters

> NOTE:
> Regional clusters are available starting from version 1.4.0.

> WARNING:
> There are some limitations in deploying regional clusters:
>
> * Automated credential distribution is supported starting from version 1.5.0 (see
> [The Credential Distribution System](../access/credentials/credentials-propagation.md#the-credential-distribution-system)).
> Before that, you must manually create the corresponding `ClusterIdentity` objects (e.g., `Secrets`, `AWSClusterIdentity`)
> on each regional cluster.
> * The kubeconfig `Secret` must exist in the system namespace (default: `kcm-system`) when registering a new region.

{{{ docsVersionInfo.k0rdentName }}} can manage thousands of clusters, potentially over multiple clouds and infrastructure domains. 
It's possible to do all of this within a single {{{ docsVersionInfo.k0rdentName }}} management cluster. In that case, the management
cluster works to manage child clusters across multiple clouds and infrastructures, and serves as the operator's 'single pane of glass'.
It collects metrics, provides visibility, and so on. Moreover, {{{ docsVersionInfo.k0rdentName }}} is designed so that a single 
manager does not become a single point of failure. The management cluster can be backed up quite simply (see [Backups](../backup/index.md) 
and restored to its prior state quickly without disrupting operations across the IT estate.

However, {{{ docsVersionInfo.k0rdentName }}} can also work in a distributed arrangement, where each infrastructure domain (for example, a 
cloud provider, a region within a cloud provider, and so on) is partly controlled by a Regional Cluster. A {{{ docsVersionInfo.k0rdentName }}} 
Regional Cluster is not a full-featured k0rdent manager, but a drone cluster containing:

- **CAPI components** pertinent to the infrastructure the Regional Cluster is managing. Infrastructure operations (often time-consuming) are distributed by the manager to the Regional Cluster for execution.
- **KOF components** including regional metrics and logs aggregation
- **Backup components** such as Velero
- and so on

When using regional clusters, the management cluster remains the single pane of glass, responsible
for managing `ClusterDeployments`, `Credentials`, `Templates`, and other {{{ docsVersionInfo.k0rdentName }}} resources.
It then deploys the actual CAPI objects that implement those k0rdent resources on the regional cluster, a plain (non-k0rdent) 
Kubernetes cluster where provider-related infrastructure (such as CAPI
providers) and the objects that implement it (such as `Cluster`, and `Machine` objects) are deployed. 

Regional clusters provide several benefits:

* Cluster resources can be distributed across multiple, purpose-specific clusters.
* Improved fault isolation, because the management cluster only needs to deal with {{{ docsVersionInfo.k0rdentName }}} objects.
* Geographic placement of resources.

For more details, see:

- [Understanding Regional Components Segregation](components-segregation.md)
- [Register Regional Cluster](regional-cluster-registration.md)
- [Creating Credential in Region](creating-credential-in-region.md)
- [Deploying Clusters in Region](deploying-clusters-in-region.md)
