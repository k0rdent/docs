# KubeVirt Infrastructure Cluster Preparation

> NOTE:
> The KubeVirt provider is available starting from {{{ docsVersionInfo.k0rdentName }}} 1.7.0. See
> [Enable KubeVirt Provider](../admin/upgrade/upgrade-to-1-7-0.md#enable-kubevirt-provider) for
> instructions on how to enable the KubeVirt provider on an existing management cluster after upgrading to 1.7.0.

{{{ docsVersionInfo.k0rdentName }}} supports using KubeVirt to create and manage clusters backed
by [KubeVirt](https://kubevirt.io/) virtual machines (VMs). For KubeVirt deployments you must prepare a dedicated
infrastructure cluster that will host the KubeVirt VMs (**the KubeVirt Infrastructure Cluster**). In most cases this
cluster is different from the management or regional cluster, which is useful when the management or regional cluster
must remain isolated from heavy VM workloads.

## Prerequisites

You can deploy the KubeVirt Infrastructure Cluster by following the instructions in the [official KubeVirt documentation](https://kubevirt.io/user-guide/).
See the *Try it out* section. Also review the official KubeVirt documentation for more details.

The KubeVirt Infrastructure Cluster must meet the following requirements:

1. **Sufficient Resources**
    The KubeVirt Infrastructure Cluster must have enough resources to host the VMs that will be created.
    Each worker node should have at least:

    * 8 vCPUs
    * 16 GiB of RAM
    * 120 GiB of disk space

    The actual requirements depend on the size and configuration of the workload clusters.

1. **Nested virtualization (if applicable)**

    If the KubeVirt Infrastructure Cluster runs on virtual machines, consider enabling nested virtualization.
    Follow the instructions described [here](https://docs.fedoraproject.org/en-US/quick-docs/using-nested-virtualization-in-kvm/index.html).

1. **Service LoadBalancer Provisioner**

    A Service LoadBalancer provider must be deployed on the KubeVirt Infrastructure Cluster to expose each workload
    cluster API server via a LoadBalancer Service.
    For example:

    * Use [MetalLB](https://metallb.universe.tf/), or
    * When running on a cloud provider, use the Cloud Controller Manager available for that provider.

    The workload cluster API server must be accessible from the management cluster or the regional cluster (when
    deploying in a region).

1. **Storage Provisioner**

    If you plan to use the Containerized Data Importer (CDI) to import VM images for KubeVirt, the KubeVirt
    Infrastructure Cluster must have a storage provisioner and a `StorageClass` that supports `ReadWriteOnce` or better.
    See [Experiment with the Containerized Data Importer](https://kubevirt.io/labs/kubernetes/lab2.html) for details.

1. **KubeVirt and CDI installed**

    Install and configure KubeVirt and Containerized Data Imported (CDI) by following the official documentation:

    * [Installation quickstarts](https://kubevirt.io/user-guide/#try-it-out)
    * [KubeVirt requirements and configuration options](https://kubevirt.io/user-guide/cluster_admin/installation/)
    * [Experiment with Containerized Data Importer (CDI)](https://kubevirt.io/labs/kubernetes/lab2.html)

1. **Create the namespace where the cluster will be deployed**

    Due to a [known issue in the KubeVirt CAPI provider](../troubleshooting/known-issues-kubevirt.md#the-kubevirtcluster-deployment-fails-on-proto-integer-overflow-error),
    the namespace where workload clusters are deployed must be created in advance.

    For example, to create the `kcm-system` namespace, run:

    ```bash
    kubectl create namespace kcm-system
    ```
