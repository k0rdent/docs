# vSphere Hosted Control Plane Deployment

Follow these steps to set up a k0smotron-hosted control plane on vSphere. 

1. Prerequisites

    Before you start, make sure you have the following:

    - A management Kubernetes cluster (Kubernetes v1.28+) deployed on vSphere with [k0rdent installed](../installation/install-k0rdent.md).

    All control plane components for managed clusters will reside in the management cluster, so make sure the management 
    cluster has sufficient resources (CPU, memory, and storage) to handle these workloads.

2. Create the `ClusterDeployment` Manifest

    The `ClusterDeployment` manifest for vSphere-hosted control planes is similar to standalone control plane deployments. 
    For a detailed list of parameters, refer to our discussion of [Template parameters for vSphere](../../reference/template/template-vsphere.md).

    > IMPORTANT: 
    > The vSphere provider requires you to specify the control plane endpoint IP before deploying the cluster. This IP 
    > address must match the one assigned to the k0smotron load balancer (LB) service.  
    > Use an annotation supported by your load balancer provider to assign the control plane endpoint IP to the k0smotron 
    > service. For example, the manifest below includes a `kube-vip` annotation.

    `ClusterDeployment` objects for vSphere-based clusters include a `.spec.config.vsphere` object that contains vSphere-specific
    parameters. For example:

    ```yaml
    apiVersion: k0rdent.mirantis.com/v1alpha1
    kind: ClusterDeployment
    metadata:
      name: cluster-1
    spec:
      template: vsphere-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.vsphereHostedCpCluster }}}
      credential: vsphere-credential
      config:
        clusterLabels: {}
        vsphere:
          server: vcenter.example.com
          thumbprint: "00:00:00"
          datacenter: "DC"
          datastore: "/DC/datastore/DC"
          resourcePool: "/DC/host/vCluster/Resources/ResPool"
          folder: "/DC/vm/example"
        controlPlaneEndpointIP: "172.16.0.10"
        ssh:
          user: ubuntu
          publicKey: |
            ssh-rsa AAA...
        rootVolumeSize: 50
        cpus: 2
        memory: 4096
        vmTemplate: "/DC/vm/template"
        network: "/DC/network/Net"
        k0smotron:
          service:
            annotations:
              kube-vip.io/loadbalancerIPs: "172.16.0.10"
    ```

For more information on these parameters, see the [Template reference for vsphere](../../reference/template/template-vsphere.md). 