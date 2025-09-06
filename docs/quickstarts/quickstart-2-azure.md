# QuickStart 2 - Azure target environment

In this QuickStart unit, we'll be gathering information and performing preparatory steps to enable {{{ docsVersionInfo.k0rdentName }}} (running on your management node) to manage clusters on Azure, and deploying a child cluster.

As noted in the [Guide to QuickStarts](./index.md), you'll need administrative access to an Azure account to complete this step. If you haven't yet created a management node and installed {{{ docsVersionInfo.k0rdentName }}}, go back to [QuickStart 1 - Management node and cluster](./quickstart-1-mgmt-node-and-cluster.md).

Note that if you have already done one of the other quickstarts, such as our AWS QuickStart ([QuickStart 2 - AWS target environment](./quickstart-2-aws.md)), you can use the same management cluster, continuing here with steps to add the ability to manage clusters on Azure. The {{{ docsVersionInfo.k0rdentName }}} management cluster can accommodate multiple provider and credential setups, enabling management of multiple infrastructures. And even if your management node is external to Azure (for example, it could be on an AWS EC2 virtual machine), as long as you permit outbound traffic to all IP addresses from the management node, this should work fine. A big benefit of {{{ docsVersionInfo.k0rdentName }}} is that it provides a single point of control and visibility across multiple clusters on multiple clouds and infrastructures.

> NOTE:
> **Cloud Security 101:** {{{ docsVersionInfo.k0rdentName }}} requires _some_ but not _all_ permissions to manage Azure resources via the CAPZ (ClusterAPI for Azure) provider. 

A best practice for using {{{ docsVersionInfo.k0rdentName }}} with Azure (this pattern is repeated with other clouds and infrastructures) is to create a new Azure Cluster Identity and Service Principal (SP) on your account with the particular permissions {{{ docsVersionInfo.k0rdentName }}} and CAPZ require. In this section, we'll create and configure those identity abstractions, and perform other steps to make required credentials accessible to {{{ docsVersionInfo.k0rdentName }}} in the management node.

> NOTE:
> If you're working on a shared Azure account, please ensure that the Azure Cluster Identity and Service Principal are not already set up before creating new abstractions.

Creating user identity abstractions with minimal required permissions is one of several principle-of-least-privilege mechanisms used to help ensure security as organizations work with Kubernetes at progressively greater scales. For more on {{{ docsVersionInfo.k0rdentName }}} security best practices, please see the [Administrator Guide](../admin/index.md).

## Install the Azure CLI (az)

The Azure CLI (az) is required to interact with Azure resources. Install it according to instructions in [How to install the Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli). For Linux/Debian (i.e., Ubuntu Server), it's one command:

```bash
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
```

## Log in with Azure CLI

Run the az login command to authenticate your session with Azure.

```bash
az login
```

## Register resource providers

Azure Resource Manager uses resource providers to manage resources of all different kinds, and required providers must be registered with an Azure account before {{{ docsVersionInfo.k0rdentName }}} and CAPZ can work with them.

You can list resources registered with your account using Azure CLI:

```bash
az provider list --query "[?registrationState=='Registered']" --output table
```

And see a listing like this:

```console
Namespace                             RegistrationState
-----------------------------------   -----------------
Microsoft.Compute                     Registered
Microsoft.Network                     Registered
```

You can then select from the commands below (or enter all of them) to register any unregistered resources that {{{ docsVersionInfo.k0rdentName }}} and CAPZ require:

```bash
az provider register --namespace Microsoft.Compute
az provider register --namespace Microsoft.Network
az provider register --namespace Microsoft.ContainerService
az provider register --namespace Microsoft.ManagedIdentity
az provider register --namespace Microsoft.Authorization
```

## Get your Azure Subscription ID

Use the following command to list Azure subscriptions and their IDs:

```bash
az account list -o table
```

The output will look like this:

```console
Name                     SubscriptionId                    TenantId
-----------------------  -------------------------------   -----------------------------
My Azure Subscription    SUBSCRIPTION_ID_SUBSCRIPTION_ID   TENANT_ID_TENANT_ID_TENANT_ID
```

The Subcription ID is in the second column.

## Create a Service Principal for {{{ docsVersionInfo.k0rdentName }}}

The Service Principal is like a password-protected user that CAPZ will use to manage resources on Azure. To create it, run the following command with the Azure CLI, replacing `<subscription-id>` with the ID you copied earlier.

```bash
az ad sp create-for-rbac --role contributor --scopes="/subscriptions/<subscription-id>"
```

You'll see output that resembles what's below:

```console
{
 "appId": "SP_APP_ID_SP_APP_ID",
 "displayName": "azure-cli-2024-10-24-17-36-47",
 "password": "SP_PASSWORD_SP_PASSWORD",
 "tenant": "SP_TENANT_SP_TENANT"
}
```

Capture this output and secure the values it contains. We'll need several of these in a moment.

## Create a Secret object with the Azure credentials

In this quickstart we're assuming a self-managed Azure clusters (non-AKS) so create a `Secret` object that stores the `clientSecret` (password) from the Service Principal. Create a YAML file called `azure-cluster-identity-secret.yaml`, as follows, inserting the password for the Service Principal (represented by the placeholder `SP_PASSWORD_SP_PASSWORD` above):

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: azure-cluster-identity-secret
  namespace: kcm-system
  labels:
    k0rdent.mirantis.com/component: "kcm"
stringData:
  clientSecret: SP_PASSWORD_SP_PASSWORD # Password retrieved from the Service Principal
type: Opaque
```
<!--
For managed (AKS) clusters on Azure create the `Secret` with the `AZURE_CLIENT_ID`, `AZURE_CLIENT_SECRET`, `AZURE_SUBSCRIPTION_ID` and `AZURE_TENANT_ID` keys set:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: azure-aks-credential
  namespace: kcm-system
  labels:
    k0rdent.mirantis.com/component: "kcm"
stringData:
  AZURE_CLIENT_ID: <SP_APP_ID_SP_APP_ID> # AppId retrieved from the Service Principal
  AZURE_CLIENT_SECRET: <SP_PASSWORD_SP_PASSWORD> # Password retrieved from the Service Principal
  AZURE_SUBSCRIPTION_ID: <SUBSCRIPTION_ID_SUBSCRIPTION_ID> # The ID of the Subscription
  AZURE_TENANT_ID: <TENANT_ID_TENANT_ID_TENANT_ID> # TenantID retrieved from the Service Principal
type: Opaque
```
-->

Apply the YAML to the {{{ docsVersionInfo.k0rdentName }}} management cluster using the following command:

```bash
kubectl apply -f azure-cluster-identity-secret.yaml
```

You should see output resembling this:

```console
secret/azure-cluster-identity-secret created
```

## Create the AzureClusterIdentity Object
<!--
> INFO:
> Skip this step for managed (AKS) clusters.
-->
This object defines the credentials {{{ docsVersionInfo.k0rdentName }}} and CAPZ will use to manage Azure resources. It references the `Secret` you just created above.

Create a YAML file called `azure-cluster-identity.yaml`. Make sure that `.spec.clientSecret.name` matches the `metadata.name` in the file you created above.

```yaml
apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
kind: AzureClusterIdentity
metadata:
  name: azure-cluster-identity
  namespace: kcm-system
  labels:
    clusterctl.cluster.x-k8s.io/move-hierarchy: "true"
    k0rdent.mirantis.com/component: "kcm"
spec:
  allowedNamespaces: {}
  clientID: SP_APP_ID_SP_APP_ID # The App ID retrieved from the Service Principal above in Step 2
  clientSecret:
    name: azure-cluster-identity-secret
    namespace: kcm-system
  tenantID: SP_TENANT_SP_TENANT # The Tenant ID retrieved from the Service Principal above in Step 2
  type: ServicePrincipal
```

Apply the YAML to your cluster:

```bash
kubectl apply -f azure-cluster-identity.yaml
```

You should see output resembling this:

```console
azureclusteridentity.infrastructure.cluster.x-k8s.io/azure-cluster-identity created
```

## Create the KCM Credential Object

Create a YAML with the specification of our credential and save it as `azure-cluster-identity-cred.yaml`.

Note that for non-AKS clusters `.spec.kind` must be `AzureClusterIdentity`, and `.spec.name` must match `.metadata.name` of the `AzureClusterIdentity` object created in the previous step.

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
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
<!--
For AKS clusters, the `.spec.identityRef.kind` must be set to `Secret`, and `.spec.name` must match
`.metadata.name` of the `Secret` object.

Note: for AKS we also need to create Cluster Identity resource template ConfigMap

```yaml
---
apiVersion: k0rdent.mirantis.com/v1beta1
kind: Credential
metadata:
  name: azure-aks-credential
  namespace: kcm-system
spec:
  identityRef:
    apiVersion: v1
    kind: Secret
    name: azure-aks-credential
    namespace: kcm-system
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: azure-aks-credential-resource-template
  namespace: kcm-system
  labels:
    k0rdent.mirantis.com/component: "kcm"
  annotations:
    projectsveltos.io/template: "true"
```
-->
Apply the YAML to your cluster:

```bash
kubectl apply -f azure-cluster-identity-cred.yaml
```

You should see output resembling this:

```console
credential.k0rdent.mirantis.com/azure-cluster-identity-cred created
```

## Create the `ConfigMap` resource-template Object

Create a YAML with the specification of our resource-template (and the necessary `StorageClass`) and save it as
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
    ---
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      name: managed-csi
      annotations:
        storageclass.kubernetes.io/is-default-class: "true"
    provisioner: disk.csi.azure.com
    parameters:
      skuName: StandardSSD_LRS
    reclaimPolicy: Delete
    volumeBindingMode: WaitForFirstConsumer
    allowVolumeExpansion: true
```

Object name needs to be exactly `azure-cluster-identity-resource-template`, `AzureClusterIdentity` object name + `-resource-template` string suffix.

Apply the YAML to your cluster:

```bash
kubectl apply -f azure-cluster-identity-resource-template.yaml
```
```console
configmap/azure-cluster-identity-resource-template created
```

## Find your location/region

To determine where to deploy your cluster, you may wish to begin by listing your Azure location/regions:

```bash
az account list-locations -o table
```

You'll see output like this:

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

What you'll need to insert in your `ClusterDeployment` is the name (center column) of the region to which you wish to deploy.

## List available cluster templates

{{{ docsVersionInfo.k0rdentName }}} is now fully configured to manage Azure. To create a cluster, begin by listing the available `ClusterTemplate` objects:

```bash
kubectl get clustertemplate -n kcm-system
```

You'll see output resembling what's below. Grab the name of the Azure standalone cluster template in its present version (in the example below, that's `azure-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.azureStandaloneCpCluster }}}`):

```console
NAMESPACE    NAME                            VALID
kcm-system   adopted-cluster-{{{ extra.docsVersionInfo.providerVersions.dashVersions.adoptedCluster }}}           true
kcm-system   aws-eks-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsEksCluster }}}                   true
kcm-system   aws-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsHostedCpCluster }}}             true
kcm-system   aws-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsStandaloneCpCluster }}}         true
kcm-system   azure-aks-{{{ extra.docsVersionInfo.providerVersions.dashVersions.azureAksCluster }}}                 true
kcm-system   azure-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.azureHostedCpCluster }}}           true
kcm-system   azure-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.azureStandaloneCpCluster }}}       true
kcm-system   docker-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.dockerHostedCpCluster }}}          true
kcm-system   gcp-gke-{{{ extra.docsVersionInfo.providerVersions.dashVersions.gcpGkeCluster }}}                   true
kcm-system   gcp-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.gcpHostedCpCluster }}}             true
kcm-system   gcp-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.gcpStandaloneCpCluster }}}         true
kcm-system   openstack-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.openstackStandaloneCpCluster }}}   true
kcm-system   remote-cluster-{{{ extra.docsVersionInfo.providerVersions.dashVersions.openstackStandaloneCpCluster }}}            true
kcm-system   vsphere-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.vsphereHostedCpCluster }}}         true
kcm-system   vsphere-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.vsphereStandaloneCpCluster }}}     true
```

## Create your ClusterDeployment

Now, to deploy a cluster, create a YAML file called `my-azure-clusterdeployment1.yaml`. We'll use this to create a `ClusterDeployment` object in {{{ docsVersionInfo.k0rdentName }}}, representing the deployed cluster. The `ClusterDeployment` identifies for {{{ docsVersionInfo.k0rdentName }}} the `ClusterTemplate` you want to use for cluster creation, the identity credential object you want to create it under, plus the location/region and instance types you want to use to host control plane and worker nodes:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ClusterDeployment
metadata:
  name: my-azure-clusterdeployment1
  namespace: kcm-system
spec:
  template: azure-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.azureStandaloneCpCluster }}} # name of the clustertemplate
  credential: azure-cluster-identity-cred
  config:
    clusterLabels: {}
    location: "AZURE_LOCATION" # Select your desired Azure Location
    subscriptionID: SUBSCRIPTION_ID_SUBSCRIPTION_ID # Enter the Subscription ID used earlier
    controlPlane:
      vmSize: Standard_A4_v2
    worker:
      vmSize: Standard_A4_v2
```
<!-- 
For AKS clusters, the `ClusterDeployment` looks like this:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ClusterDeployment
metadata:
  name: my-azure-clusterdeployment1
  namespace: kcm-system
spec:
  template: azure-aks-{{{ extra.docsVersionInfo.providerVersions.dashVersions.azureAksCluster }}}
  credential: azure-aks-credential
  propagateCredentials: false # Should be set to `false`
  config:
    clusterLabels: {}
    location: "westus" # Select your desired Azure Location (find it via `az account list-locations -o table`)
    machinePools:
      system:
        vmSize: Standard_A4_v2
      user:
        vmSize: Standard_A4_v2
```
-->

## Apply the ClusterDeployment to deploy the cluster

Finally, we'll apply the `ClusterDeployment` YAML (`my-azure-clusterdeployment1.yaml`) to instruct {{{ docsVersionInfo.k0rdentName }}} to deploy the cluster:

```bash
kubectl apply -f my-azure-clusterdeployment1.yaml
```

Kubernetes should confirm this:

```console
clusterdeployment.k0rdent.mirantis.com/my-azure-clusterdeployment1 created
```

There will be a delay as the cluster finishes provisioning. Follow the provisioning process with the following command:

```bash
kubectl -n kcm-system get clusterdeployment.k0rdent.mirantis.com my-azure-clusterdeployment1 --watch
```

## Obtain the cluster's kubeconfig

Now you can retrieve the cluster's `kubeconfig`:

```bash
kubectl -n kcm-system get secret my-azure-clusterdeployment1-kubeconfig -o jsonpath='{.data.value}' | base64 -d > my-azure-clusterdeployment1-kubeconfig.kubeconfig
```

And you can use the `kubeconfig` to see what's running on the cluster:

```bash
KUBECONFIG="my-azure-clusterdeployment1-kubeconfig.kubeconfig" kubectl get pods -A
```

## List child clusters

To verify the presence of the child cluster, list the available `ClusterDeployment` objects:

```bash
kubectl get ClusterDeployments -A
```
```console
NAMESPACE    NAME                          READY   STATUS
kcm-system   my-azure-clusterdeployment1   True    ClusterDeployment is ready
```

## Tear down the child cluster

To tear down the child cluster, delete the `ClusterDeployment`:

```bash
kubectl delete ClusterDeployment my-azure-clusterdeployment1 -n kcm-system
```
```console
clusterdeployment.k0rdent.mirantis.com "my-azure-clusterdeployment1" deleted
```

## Next Steps

Now that you've finished the {{{ docsVersionInfo.k0rdentName }}} QuickStart, we have some suggestions for what to do next:

Check out the [Administrator Guide](../admin/index.md) ...

* For a more detailed view of {{{ docsVersionInfo.k0rdentName }}} setup for production
* For details about setting up {{{ docsVersionInfo.k0rdentName }}} to manage clusters on VMware and OpenStack
* For details about using {{{ docsVersionInfo.k0rdentName }}} with cloud Kubernetes distros: AWS EKS and Azure AKS
