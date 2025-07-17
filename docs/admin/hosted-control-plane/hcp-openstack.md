# OpenStack Hosted Control Plane Deployment

Follow these steps to set up a k0smotron-hosted control plane on OpenStack:

1. Prerequisites

    Before proceeding, make sure you have the following:

    * A management Kubernetes cluster (Kubernetes v1.28 or later) deployed on OpenStack with [{{{ docsVersionInfo.k0rdentName }}} installed](../installation/install-k0rdent.md).
    * An OpenStack Cloud Controller Manager installed to manage Services with the `Load Balancer` type.
    * A [default storage class](https://kubernetes.io/docs/tasks/administer-cluster/change-default-storage-class/) configured on the management cluster to support Persistent Volumes.
    * An OpenStack Credential object and resource-template ConfigMap must exist in the namespace where the cluster
      will be deployed. Refer to steps 4–6 in the [OpenStack management cluster preparation guide](../installation/prepare-mgmt-cluster/openstack.md).
    * The name of the existing network and subnet where the worker nodes will be deployed.
    * The name of the existing router that will be used to deploy the worker nodes.
    * (Optional) The name of the existing security group to attach to the worker nodes.

    > IMPORTANT:  
    > All control plane components for your hosted cluster will reside in the management cluster, and the management cluster
    > must have sufficient resources to handle these additional workloads.

2. Networking

    To deploy a hosted control plane, the necessary OpenStack networking resources must already exist or be created. If you're
    using the same network, subnet and router as your management cluster, you can reuse these resources.

    If your management cluster was deployed using the Cluster API Provider OpenStack (CAPO), you can gather the required
    networking details using the following commands:

    Retrieve the network name:

    ```shell
    kubectl -n <cluster-namespace> get openstackcluster <cluster-name> -o go-template='{{.status.network.name}}'
    ```

    Retrieve the subnet name:

    ```shell
    kubectl -n <cluster-namespace> get openstackcluster <cluster-name> -o go-template='{{(index .status.network.subnets 0).name}}'
    ```

    Retrieve the router name:

    ```shell
    kubectl -n <cluster-namespace> get openstackcluster <cluster-name> -o go-template='{{.status.router.name}}'
    ```

3. Create the `ClusterDeployment` manifest

    Once you've collected all the necessary data, you can create the `ClusterDeployment` manifest. This file tells {{{ docsVersionInfo.k0rdentName }}} how to
    deploy and manage the hosted control plane. For example:

    ```yaml
    apiVersion: k0rdent.mirantis.com/v1beta1
    kind: ClusterDeployment
    metadata:
      name: openstack-hosted-cp
    spec:
      template: openstack-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.openstackHostedCpCluster }}}
      credential: openstack-credential
    config:
      workersNumber: 2
      flavor: m1.medium
      image:
        filter:
          name: ubuntu-20.04
      externalNetwork:
        filter:
          name: "public"
      identityRef:
        name: "openstack-cloud-config"
        cloudName: "openstack"
        region: ${OS_REGION_NAME}
    
      network:
        filter:
          name: ${NETWORK_NAME}
      router:
        filter:
          name: ${ROUTER_NAME}
      subnets:
      - filter:
          name: ${SUBNET_NAME}
      ports:
      - network:
          filter:
            name: ${NETWORK_NAME}
    ```

    You can adjust `flavor`, `image name`, `region name`, `network`, `subnet` and `router` configuration to match your
    OpenStack environment.
    For more information about the configuration options, see the [Template reference for openstack](../../reference/template/template-openstack.md)

    Alternatively, you can generate the `ClusterDeployment` manifest.

    To simplify the creation of a `ClusterDeployment` manifest, you can use the following template, which dynamically
    inserts the appropriate values:

    ```yaml
    apiVersion: k0rdent.mirantis.com/v1beta1
    kind: ClusterDeployment
    metadata:
      name: openstack-hosted
    spec:
      template: openstack-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.openstackHostedCpCluster }}}
      credential: openstack-credential
      config:
        workersNumber: 2
        flavor: m1.medium
        image:
          filter:
            name: ubuntu-20.04
        externalNetwork:
          filter:
            name: "public"
        identityRef:
          name: "openstack-cloud-config"
          cloudName: "openstack"
          region: "{{.spec.identityRef.region}}"
    
        network:
          filter:
            name: "{{.status.network.name}}"
        router:
          filter:
            name: "{{.status.router.name}}"
        subnets:
        - filter:
            name: "{{(index .status.network.subnets 0).name}}"
        ports:
        - network:
            filter:
              name: "{{.status.network.name}}"
    ```

    For more information on these and other available parameters, see the [Template reference for openstack](../../reference/template/template-openstack.md).

    Save this template as `clusterdeployment.yaml.tpl`, then generate your manifest using the following command:

    ```shell
    kubectl -n <cluster-namespace> get openstackcluster <cluster-name> -o go-template="$(cat clusterdeployment.yaml.tpl)" > clusterdeployment.yaml
    ```

4. Apply the template

    Nothing actually happens until you apply the `ClusterDeployment` manifest to create a new cluster deployment:

    ```shell
    kubectl apply -f clusterdeployment.yaml -n kcm-system
    ```
