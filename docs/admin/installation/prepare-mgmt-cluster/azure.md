# Azure

Standalone clusters can be deployed on Azure instances. Follow these steps to make Azure clusters available to your users:

1. Install k0rdent

    Follow the instructions in [Install k0rdent](../install-k0rdent.md) to create a management cluster with k0rdent running.

2. The Azure CLI

    The Azure CLI (`az`) is required to interact with Azure resources. You can install it on Ubuntu as follows:

    ```shell
    curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
    ```

3. Log in to Azure

    Run the `az login` command to authenticate your session with Azure:

    ```shell
    az login
    ```

    Make sure that the account you're using has at least one active subscription.

4. Register resource providers

    In order for k0rdent to deploy and manage clusters, it needs to be able to work with Azure resources such as 
    compute, network, and identity. Make sure the subscription you're using has the following resource providers registered:

    ```shell
    Microsoft.Compute
    Microsoft.Network
    Microsoft.ContainerService
    Microsoft.ManagedIdentity
    Microsoft.Authorization
    ```

    To register these providers, run the following commands in the Azure CLI:

    ```shell
    az provider register --namespace Microsoft.Compute
    az provider register --namespace Microsoft.Network
    az provider register --namespace Microsoft.ContainerService
    az provider register --namespace Microsoft.ManagedIdentity
    az provider register --namespace Microsoft.Authorization
    ```

5. Find Your Subscription ID

    Creating a child cluster requires a structure of credentials that link to user identities on the provider system without
    exposing the actual username and password to users. You can find more information on [k0rdent 
    Credentials](../../access/credentials/index.md), but for Azure, this involves creating an `AzureClusterIdentity` and a 
    Service Principal (SP) to let CAPZ (Cluster API Azure) communicate with the cloud provider. 

    On Azure, the lowest level of this hierarchy is the subscription, which ties to your billing information for Azure. Your Azure user must have at least one subscription for you to use it with k0rdent, so if you're working with a new
    account make sure to [create a new subscription with billing information](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/create-subscription) before you start.

    To get the information you need, list all your Azure subscriptions: 

    ```shell
    az account list -o table
    ```
    ```console
    Name                     SubscriptionId                        TenantId
    -----------------------  -------------------------------------  --------------------------------
    My Azure Subscription    SUBSCRIPTION_ID_SUBSCRIPTION_ID        TENANT_ID_TENANT_ID_TENANT_ID
    ```

    Make note of the `SubscriptionId` for the subscription you want to use.

6. Create a Service Principal (SP)

    The Service Principal is like a password-protected user that CAPZ will use to manage resources on Azure.
    Create the Service Principal, making sure to replace <SUBSCRIPTION_ID_SUBSCRIPTION_ID> with the `SubscriptionId` from step 1.

    ```shell
    az ad sp create-for-rbac --role contributor --scopes="/subscriptions/<SUBSCRIPTION_ID_SUBSCRIPTION_ID>"
    ```
    ```console
    {
    "appId": "SP_APP_ID_SP_APP_ID",
    "displayName": "azure-cli-2024-10-24-17-36-47",
    "password": "SP_PASSWORD_SP_PASSWORD",
    "tenant": "SP_TENANT_SP_TENANT"
    }
    ```
    Note that this information provides access to your Azure account, so make sure to treat these strings 
    like passwords. Do not share them or check them into a repository.

7. Use the password to create a `Secret` object

    The `Secret` stores the `clientSecret` (password) from the Service Principal.
    Save the `Secret` YAML in a file called `azure-cluster-identity-secret.yaml`:

    ```yaml
    apiVersion: v1
    kind: Secret
    metadata:
      name: azure-cluster-identity-secret
      namespace: kcm-system
      labels:
        k0rdent.mirantis.com/component: "kcm"
    stringData:
      clientSecret: <SP_PASSWORD_SP_PASSWORD> # Password retrieved from the Service Principal
    type: Opaque
    ```

    You can then apply the YAML to your cluster:

    ```shell
    kubectl apply -f azure-cluster-identity-secret.yaml
    ```

8. Create the `AzureClusterIdentity` objects

    The `AzureClusterIdentity` object defines the credentials CAPZ uses to manage Azure resources. 
    It references the `Secret` you just created, so make sure that `.spec.clientSecret.name` matches 
    the name of that `Secret`.

    Save the following YAML into a file named `azure-cluster-identity.yaml`:

    ```yaml
    apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
    kind: AzureClusterIdentity
    metadata:
      labels:
        clusterctl.cluster.x-k8s.io/move-hierarchy: "true"
        k0rdent.mirantis.com/component: "kcm"
      name: azure-cluster-identity
      namespace: kcm-system
    spec:
      allowedNamespaces: {}
      clientID: <SP_APP_ID_SP_APP_ID> # The App ID retrieved from the Service Principal above in Step 2
      clientSecret:
        name: azure-cluster-identity-secret
        namespace: kcm-system
      tenantID: <SP_TENANT_SP_TENANT> # The Tenant ID retrieved from the Service Principal above in Step 2
      type: ServicePrincipal
    ```

    Apply the YAML to your cluster:

    ```shell
    kubectl apply -f azure-cluster-identity.yaml
    ```
    ```console
    azureclusteridentity.infrastructure.cluster.x-k8s.io/azure-cluster-identity created
    ```

9. Create the k0rdent `Credential` Object

    Create the YAML for the specification of the `Credential` and save it as `azure-cluster-identity-cred.yaml`.

    ```YAML
    apiVersion: k0rdent.mirantis.com/v1alpha1
    kind: Credential
    metadata:
      name: azure-cluster-identity-cred
      namespace: kcm-system
    spec:
      identityRef:
        apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
        kind: AzureClusterIdentity
        name: azure-cluster-identity
        namespace: kcm-system
    ```

    You're referencing the `AzureClusterIdentity` object you just created, so make sure that `.spec.name` matches 
    `.metadata.name` of that object. Also, note that while the overall object's `kind` is `Credential`, the 
    `.spec.identityRef.kind` must be `AzureClusterIdentity` to match that object.

    Apply the YAML to your cluster:

    ```shell
    kubectl apply -f azure-cluster-identity-cred.yaml
    ```
    ```console
    credential.k0rdent.mirantis.com/azure-cluster-identity-cred created
    ```

10. Create the `ConfigMap` resource-template Object

    Create a YAML with the specification of our resource-template and save it as
    `azure-cluster-identity-resource-template.yaml`

    ```yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: azure-cluster-identity-resource-template
      namespace: kcm-system
      labels:
        k0rdent.mirantis.com/component: "kcm"
      annotations:
        projectsveltos.io/template: "true"
    data:
      configmap.yaml: |
        {{- $cluster := .InfrastructureProvider -}}
        {{- $identity := (getResource "InfrastructureProviderIdentity") -}}
        {{- $secret := (getResource "InfrastructureProviderIdentitySecret") -}}
        {{- $subnetName := "" -}}
        {{- $securityGroupName := "" -}}
        {{- $routeTableName := "" -}}
        {{- range $cluster.spec.networkSpec.subnets -}}
          {{- if eq .role "node" -}}
            {{- $subnetName = .name -}}
            {{- $securityGroupName = .securityGroup.name -}}
            {{- $routeTableName = .routeTable.name -}}
            {{- break -}}
          {{- end -}}
        {{- end -}}
        {{- $cloudConfig := dict
          "aadClientId" $identity.spec.clientID
          "aadClientSecret" (index $secret.data "clientSecret" | b64dec)
          "cloud" $cluster.spec.azureEnvironment
          "loadBalancerName" ""
          "loadBalancerSku" "Standard"
          "location" $cluster.spec.location
          "maximumLoadBalancerRuleCount" 250
          "resourceGroup" $cluster.spec.resourceGroup
          "routeTableName" $routeTableName
          "securityGroupName" $securityGroupName
          "securityGroupResourceGroup" $cluster.spec.networkSpec.vnet.resourceGroup
          "subnetName" $subnetName
          "subscriptionId" $cluster.spec.subscriptionID
          "tenantId" $identity.spec.tenantID
          "useInstanceMetadata" true
          "useManagedIdentityExtension" false
          "vmType" "vmss"
          "vnetName" $cluster.spec.networkSpec.vnet.name
          "vnetResourceGroup" $cluster.spec.networkSpec.vnet.resourceGroup
        -}}
        ---
        apiVersion: v1
        kind: Secret
        metadata:
          name: azure-cloud-provider
          namespace: kube-system
        type: Opaque
        data:
          cloud-config: {{ $cloudConfig | toJson | b64enc }}
    ```
    Object name needs to be exactly `azure-cluster-identity-resource-template.yaml`, `AzureClusterIdentity` object name + `-resource-template` string suffix.

    Apply the YAML to your cluster:

    ```shell
    kubectl apply -f azure-cluster-identity-resource-template.yaml
    ```
    ```console
    configmap/azure-cluster-identity-resource-template created
    ```

Now you're ready to deploy the cluster.

11. Create a `ClusterDeployment`

    To test the configuration, deploy a child cluster by following these steps:

    First get a list of available locations/regions:

    ```shell
    az account list-locations -o table
    ```
    ```console
    DisplayName               Name                 RegionalDisplayName
    ------------------------  -------------------  -------------------------------------
    East US                   eastus               (US) East US
    South Central US          southcentralus       (US) South Central US
    West US 2                 westus2              (US) West US 2
    West US 3                 westus3              (US) West US 3
    Australia East            australiaeast        (Asia Pacific) Australia East
    . . .
    ```

    Make note of the location you want to use, such as `eastus`.

    To create the actual child cluster, create a `ClusterDeployment` that references the appropriate template
    as well as the location, credentials, and `subscriptionId`.

    You can see the available templates by listing them:

    ```shell
    kubectl get clustertemplate -n kcm-system
    ```
    ```console
    NAME                            VALID
    adopted-cluster-{{{ extra.docsVersionInfo.k0rdentVersion }}}           true
    aws-eks-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsEksCluster }}}                   true
    aws-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsHostedCpCluster }}}             true
    aws-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsStandaloneCpCluster }}}         true
    azure-aks-{{{ extra.docsVersionInfo.providerVersions.dashVersions.azureAksCluster }}}                 true
    azure-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.azureHostedCpCluster }}}           true
    azure-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.azureStandaloneCpCluster }}}       true
    openstack-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.openstackStandaloneCpCluster }}}   true
    vsphere-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.vsphereHostedCpCluster }}}         true
    vsphere-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.vsphereStandaloneCpCluster }}}     true
    ```

    Create the yaml:

    ```yaml
    apiVersion: k0rdent.mirantis.com/v1alpha1
    kind: ClusterDeployment
    metadata:
      name: my-azure-clusterdeployment1
      namespace: kcm-system
    spec:
      template: azure-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.azureStandaloneCpCluster }}}
      credential: azure-cluster-identity-cred
      config:
        location: "westus" # Select your desired Azure Location (find it via `az account list-locations -o table`)
        subscriptionID: <SUBSCRIPTION_ID_SUBSCRIPTION_ID> # Enter the Subscription ID used earlier
        controlPlane:
          vmSize: Standard_A4_v2
        worker:
          vmSize: Standard_A4_v2
    ```

    Apply the YAML to your management cluster:

    ```shell
    kubectl apply -f my-azure-clusterdeployment1.yaml
    ```
    ```console
    clusterdeployment.k0rdent.mirantis.com/my-azure-clusterdeployment1 created
    ```

    Note that although the `ClusterDeployment` object has been created, there will be a delay as actual Azure instances
    are provisioned and added to the cluster. You can follow the provisioning process:

    ```shell
    kubectl -n kcm-system get clusterdeployment.k0rdent.mirantis.com my-azure-clusterdeployment1 --watch
    ```

    If the provisioning process continues for a more than a few minutes, check to make sure k0rdent isn't trying to
    exceed your quotas. If you are near the top of your quotas, requesting an increase can "unstick" the provisioning process.

    After the cluster is `Ready`, you can access it via the kubeconfig:

    ```shell
    kubectl -n kcm-system get secret my-azure-clusterdeployment1-kubeconfig -o jsonpath='{.data.value}' | base64 -d > my-azure-clusterdeployment1-kubeconfig.kubeconfig
    KUBECONFIG="my-azure-clusterdeployment1-kubeconfig.kubeconfig" kubectl get pods -A
    ```

12. Cleanup

    To clean up Azure resources, delete the child cluster by deleting the `ClusterDeployment`:

    ```shell
    kubectl get clusterdeployments -A
    ```
    ```console
    NAMESPACE    NAME                          READY   STATUS
    kcm-system   my-azure-clusterdeployment1   True    ClusterDeployment is ready
    ```
    ```shell
    kubectl delete clusterdeployments my-azure-clusterdeployment1 -n kcm-system
    ```
    ```console
    clusterdeployment.k0rdent.mirantis.com "my-azure-clusterdeployment1" deleted
    ```
