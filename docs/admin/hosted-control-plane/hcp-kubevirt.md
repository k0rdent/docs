# KubeVirt Hosted Control Plane Deployment

Follow these steps to set up a k0smotron-hosted control plane on KubeVirt.

1. Prerequisites

    Before you start, make sure you have the following:

    - A management Kubernetes cluster (Kubernetes v1.28+) with [{{{ docsVersionInfo.k0rdentName }}} installed](../installation/install-k0rdent.md).
    - A KubeVirt Infrastructure Cluster deployed and configured. See [KubeVirt Infrastructure Cluster Preparation](../../appendix/kubevirt-infra.md)
      for setup instructions.
    - Network connectivity between the management cluster and the KubeVirt Infrastructure Cluster.
    - A [default storage class](https://kubernetes.io/docs/tasks/administer-cluster/change-default-storage-class/)
      configured on the management cluster to support PersistentVolumes.
    - A Service LoadBalancer solution deployed on the management cluster to provide `LoadBalancer` Services
      for the hosted control plane that will be accessed from the KubeVirt Infrastructure Cluster.

    > IMPORTANT:
    > All control plane components for your hosted cluster run in the management cluster. The management cluster
    > must have sufficient resources to handle these additional workloads.

1. Prepare the management cluster

    Follow the [Prepare Management Cluster: KubeVirt](../installation/prepare-mgmt-cluster/kubevirt.md) guide to create
    a KubeVirt `Credential` object and a resource-template `ConfigMap` in the namespace where the cluster will be deployed.

1. Create the `ClusterDeployment` manifest

    The `ClusterDeployment` manifest for KubeVirt-hosted control planes is similar to manifests for standalone control
    plane deployments.
    For a detailed list of parameters available in the {{{ docsVersionInfo.k0rdentName }}} built-in `kubevirt-hosted-cp`
    template, refer to the schema at [Parameters for KubeVirt Hosted ClusterTemplate](https://github.com/k0rdent/kcm/blob/v1.7.0/templates/cluster/kubevirt-hosted-cp/values.schema.json).

    For example:

    ```yaml
    apiVersion: k0rdent.mirantis.com/v1beta1
    kind: ClusterDeployment
    metadata:
      name: cluster-1
    spec:
      template: kubevirt-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.kubevirtHostedCpCluster }}}
      credential: kubevirt-credential
      config:
        clusterLabels: {}
        clusterAnnotations: {}
        controlPlaneNumber: 1
        workersNumber: 1
        cluster:
          controlPlaneServiceTemplate:
            spec:
              type: ClusterIP
        worker:
          dnsConfig:
            nameservers:
            - 8.8.8.8
          cpu:
            model: host-passthrough
    ```

    For other KubeVirt cluster templates, the available parameters differ. Refer to the corresponding template reference
    guides for details.
