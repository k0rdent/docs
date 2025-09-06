# Azure Hosted Control Plane Deployment

Follow these steps to set up a k0smotron-hosted control plane on Azure:

1. Prerequisites

    Before you start, make sure you have the following:

    - A management Kubernetes cluster (Kubernetes v1.28+) deployed on Azure with [{{{ docsVersionInfo.k0rdentName }}} installed](../installation/install-k0rdent.md).
    - A [default storage class](https://kubernetes.io/docs/tasks/administer-cluster/change-default-storage-class/) configured
      on the management cluster to support Persistent Volumes.

    > NOTE:  
    > All control plane components for managed clusters will run in the management cluster. Make sure the management cluster
      has sufficient CPU, memory, and storage to handle the additional workload.

2. Gather Pre-existing Resources

    In a hosted control plane setup, some Azure resources must exist before deployment and must be explicitly
    provided in the `ClusterDeployment` configuration. These resources can also be reused by the management cluster.

    If you deployed your Azure Kubernetes cluster using the Cluster API Provider for Azure (CAPZ), you can retrieve
    the required information using the following commands:

    Location:

    ```bash
    kubectl get azurecluster <cluster-name> -o go-template='{{.spec.location}}'
    ```

    Subscription ID:

    ```bash
    kubectl get azurecluster <cluster-name> -o go-template='{{.spec.subscriptionID}}'
    ```

    Resource Group:

    ```bash
    kubectl get azurecluster <cluster-name> -o go-template='{{.spec.resourceGroup}}'
    ```

    VNet Name:

    ```bash
    kubectl get azurecluster <cluster-name> -o go-template='{{.spec.networkSpec.vnet.name}}'
    ```

    Subnet Name:

    ```bash
    kubectl get azurecluster <cluster-name> -o go-template='{{(index .spec.networkSpec.subnets 1).name}}'
    ```

    Route Table Name:

    ```bash
    kubectl get azurecluster <cluster-name> -o go-template='{{(index .spec.networkSpec.subnets 1).routeTable.name}}'
    ```

    Security Group Name:

    ```bash
    kubectl get azurecluster <cluster-name> -o go-template='{{(index .spec.networkSpec.subnets 1).securityGroup.name}}'
    ```

3. Create the ClusterDeployment manifest

    After collecting the required data, create a `ClusterDeployment` manifest to configure the hosted control plane. It should
    look something like this:

    ```yaml
    apiVersion: k0rdent.mirantis.com/v1beta1
    kind: ClusterDeployment
    metadata:
      name: azure-hosted-cp
    spec:
      template: azure-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.azureHostedCpCluster }}}
      credential: azure-credential
      config:
        clusterLabels: {}
        location: "westus"
        subscriptionID: ceb131c7-a917-439f-8e19-cd59fe247e03
        vmSize: Standard_A4_v2
        resourceGroup: mgmt-cluster
        network:
          vnetName: mgmt-cluster-vnet
          nodeSubnetName: mgmt-cluster-node-subnet
          routeTableName: mgmt-cluster-node-routetable
          securityGroupName: mgmt-cluster-node-nsg
    ```

    Alternatively, you can generate the `ClusterDeployment` manifest.

    If the management cluster you prepared in the first step was deployed using k0rdent or the CAPI AWS provider,
    you can simplify the creation of a `ClusterDeployment` manifest, and use the following template, which
    dynamically inserts the appropriate values:

    ```yaml
    apiVersion: k0rdent.mirantis.com/v1beta1
    kind: ClusterDeployment
    metadata:
      name: azure-hosted-cp
    spec:
      template: azure-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.azureHostedCpCluster }}}
      credential: azure-credential
      config:
        clusterLabels: {}
        location: "{{.spec.location}}"
        subscriptionID: "{{.spec.subscriptionID}}"
        vmSize: Standard_A4_v2
        resourceGroup: "{{.spec.resourceGroup}}"
        network:
          vnetName: "{{.spec.networkSpec.vnet.name}}"
          nodeSubnetName: "{{(index .spec.networkSpec.subnets 1).name}}"
          routeTableName: "{{(index .spec.networkSpec.subnets 1).routeTable.name}}"
          securityGroupName: "{{(index .spec.networkSpec.subnets 1).securityGroup.name}}"
    ```

    Save this YAML as `clusterdeployment.yaml.tpl` and render the manifest with the following command:

    ```bash
    kubectl get azurecluster <management-cluster-name> -o go-template="$(cat clusterdeployment.yaml.tpl)" > clusterdeployment.yaml
    ```

4. Create the `ClusterDeployment`

    To actually create the cluster, apply the `ClusterDeployment` manifest to the management cluster, as in:

    ```bash
    kubectl apply clusterdeployment.yaml -n kcm-system
    ```

5. Manually update the `AzureCluster` object

    Due to a limitation in k0smotron, (see [k0sproject/k0smotron#668](https://github.com/k0sproject/k0smotron/issues/668)),
    after applying the `ClusterDeployment` manifest, you must manually update the status of the `AzureCluster` object.

    Use the following command to set the `AzureCluster` object status to `Ready`:

    ```bash
    kubectl patch azurecluster <cluster-name> --type=merge --subresource status --patch '{"status": {"ready": true}}'
    ```

## Important Notes on Cluster Deletion

Due to these same k0smotron limitations, you **must** take some manual steps in order to delete a cluster properly:

1. Add a Custom Finalizer to the AzureCluster Object:

    To prevent the `AzureCluster` object from being deleted too early, add a custom finalizer:

    ```bash
    kubectl patch azurecluster <cluster-name> --type=merge --patch '{"metadata": {"finalizers": ["manual"]}}'
    ```

2. Delete the ClusterDeployment:

    After adding the finalizer, delete the `ClusterDeployment` object as usual. Confirm that all `AzureMachines` objects have been deleted successfully.

3. Remove Finalizers from Orphaned AzureMachines:

    If any `AzureMachines` are left orphaned, delete their finalizers manually after confirming no VMs remain in Azure. Use this command to remove the finalizer:

    ```bash
    kubectl patch azuremachine <machine-name> --type=merge --patch '{"metadata": {"finalizers": []}}'
    ```

4. Allowing Updates to Orphaned Objects:

    If Azure admission controls prevent updates to orphaned objects, you must disable the associated `MutatingWebhookConfiguration` by deleting it:

    ```bash
    kubectl delete mutatingwebhookconfiguration <webhook-name>
    ```
