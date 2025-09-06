# QuickStart 2 - GCP target environment

In this QuickStart unit, we'll be gathering information and performing preparatory steps to enable
{{{ docsVersionInfo.k0rdentName }}} (running on your management node) to manage clusters on GCP and deploying a child cluster.

Note that if you have already done one of the other quickstarts, such as our AWS or Azure QuickStart ([QuickStart 2 - AWS target environment](./quickstart-2-aws.md)) or Azure QuickStart ([QuickStart 2 - Azure target environment](./quickstart-2-azure.md)), 
you can use the same management cluster, continuing here with steps to add the ability to manage clusters on GCP. The 
{{{ docsVersionInfo.k0rdentName }}} management cluster can accommodate multiple provider and credential setups, enabling
management of multiple infrastructures. And even if your management node is external to GCP (for example, it could be on 
an AWS EC2 virtual machine), as long as you permit outbound traffic to all IP addresses from the management node, this should 
work fine. A big benefit of {{{ docsVersionInfo.k0rdentName }}} is that it provides a single point of control and visibility
across multiple clusters on multiple clouds and infrastructures.

The GCP provider is available starting with the {{{ docsVersionInfo.k0rdentName }}} 0.2.0 release, but it's not enabled by default.
To enable the GCP provider in {{{ docsVersionInfo.k0rdentName }}}, edit the `Management` object and add `cluster-api-provider-gcp` to the list of `spec.providers`, and the GCP components will start within a few minutes.

## Install Gcloud CLI

Follow [Install the gcloud CLI instruction](https://cloud.google.com/sdk/docs/install) to install gcloud CLI on your local machine.

## Authenticate in GCP cloud

```bash
gcloud auth login
```

By default, this command will obtain access credentials for your user account via a web-based
authorization flow.

Set the project in which you want to deploy a cluster. Run:

```bash
gcloud config set project PROJECT_ID
```

## Create a GCP Service Account

> NOTE:
> Skip this step if the Service Account already configured
Follow the [GCP Service Account creation guide](https://cloud.google.com/iam/docs/service-accounts-create#creating)
and create a new service account with `Editor` permissions.

If you have plans to deploy `GKE`, the Service Account will also need the `iam.serviceAccountTokenCreator` role.

## Generate JSON Key for the GCP Service Account

> NOTE:
> Skip this step if you're going to use an existing key
Follow the [Create a service account key guide](https://cloud.google.com/iam/docs/keys-create-delete#creating)
and create a new key with the JSON key type.

A JSON file will be automatically downloaded to your computer. You should keep it somewhere safe.

The example of the JSON file:
```bash
{
  "type": "service_account",
  "project_id": "project_id",
  "private_key_id": "akdof8v8s6n39n29251be52cabbb3984c259f1",
  "private_key": "-----BEGIN PRIVATE KEY-----\nPRIVATE_KEY\n-----END PRIVATE KEY-----\n",
  "client_email": "name@project_id.iam.gserviceaccount.com",
  "client_id": "123456778",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/user%40project_id.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
```

## Create a Secret object with the GCP (GKE) credentials

Create a `Secret` object that stores the `credentials` field under `data` section. Create a YAML file called
`gcp-cluster-identity-secret.yaml`, as follows, inserting the base64-encoded GCP credentials
(represented by the placeholder `GCP_B64ENCODED_CREDENTIALS` below) that you get on the previous step.
To get base64 encoded credentials, run:

```bash
    GCP_B64ENCODED_CREDENTIALS=$(cat <gcpJSONCredentialsFileName> | base64 -w 0)
```

```yaml
cat > gcp-cluster-identity-secret.yaml << EOF
apiVersion: v1
kind: Secret
metadata:
  name: gcp-cloud-sa
  namespace: kcm-system
  labels:
    k0rdent.mirantis.com/component: "kcm"
data:
  credentials: ${GCP_B64ENCODED_CREDENTIALS}
type: Opaque
EOF
```
Apply the YAML to your cluster:

```bash
kubectl apply -f gcp-cluster-identity-secret.yaml
```

You should see output resembling this:

```console
secret/gcp-cloud-sa created
```

## Create the KCM Credential Object

Create a YAML with the specification of our credential and save it as `gcp-credential.yaml`.

Note that `.spec.name` must match `.metadata.name` of the `Secret` object created in the previous step.

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: Credential
metadata:
  name: gcp-credential
  namespace: kcm-system
spec:
  identityRef:
    apiVersion: v1
    kind: Secret
    name: gcp-cloud-sa
    namespace: kcm-system
```

```bash
kubectl apply -f gcp-credential.yaml
```

You should see output resembling this:

```console
credential.k0rdent.mirantis.com/gcp-credential created
```

## Create the `ConfigMap` resource-template Object

Create a YAML with the specification of our resource-template and save it as
`gcp-cloud-sa-resource-template.yaml`

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: gcp-cloud-sa-resource-template
  namespace: kcm-system
  labels:
    k0rdent.mirantis.com/component: "kcm"
  annotations:
    projectsveltos.io/template: "true"
data:
  configmap.yaml: |
    {{- $secret := (getResource "InfrastructureProviderIdentity") -}}
    ---
    apiVersion: v1
    kind: Secret
    metadata:
      name: gcp-cloud-sa
      namespace: kube-system
    type: Opaque
    data:
      cloud-sa.json: {{ index $secret "data" "credentials" }}
```

Object name needs to be exactly `gcp-cloud-sa-resource-template` (credentials `Secret` object name + `-resource-template` string suffix).

Apply the YAML to your cluster:

```bash
kubectl apply -f gcp-cloud-sa-resource-template.yaml
```
```console
configmap/gcp-cloud-sa-resource-template created
```

## Find your location/region

To determine where to deploy your cluster, you may wish to begin by listing your GCP regions:

```bash
gcloud compute regions list
```

You'll see output like this:

```console
NAME                     CPUS    DISKS_GB  ADDRESSES  RESERVED_ADDRESSES  STATUS  TURNDOWN_DATE
africa-south1            0/300   0/102400  0/575      0/175               UP
asia-east1               0/3000  0/102400  0/575      0/175               UP
asia-east2               0/1500  0/102400  0/575      0/175               UP
asia-northeast1          0/1500  0/102400  0/575      0/175               UP
asia-northeast2          0/750   0/102400  0/575      0/175               UP
. . .
```

What you'll need to insert in your ClusterDeployment is the name (first column) of the region you wish to deploy to.

## (optional) Find or create your network

If you want to deploy in existing network, obtain all network names using `gcloud` CLI and choose one of available:
```bash
gcloud compute networks list --format="value(name)"
```

If you prefer to create a new network, follow this [instruction](https://cloud.google.com/vpc/docs/create-modify-vpc-networks#create-auto-network).

## Determine the instance type

Find available machine types and its parameters by running:

```bash
gcloud compute machine-types list | grep REGION
```

## Find available images

To list all available images in your GCP project, run:

```bash
gcloud compute images list --uri
```

You'll see output like this:

```console
https://www.googleapis.com/compute/v1/projects/centos-cloud/global/images/centos-stream-9-arm64-v20250311
https://www.googleapis.com/compute/v1/projects/centos-cloud/global/images/centos-stream-9-v20250311
https://www.googleapis.com/compute/v1/projects/cos-cloud/global/images/cos-105-17412-535-84
https://www.googleapis.com/compute/v1/projects/cos-cloud/global/images/cos-109-17800-436-79
https://www.googleapis.com/compute/v1/projects/cos-cloud/global/images/cos-113-18244-291-82
. . .
```

To build your own image, follow [Building images instruction](https://cluster-api-gcp.sigs.k8s.io/prerequisites#building-images).

Replace `REGION` with the region you'd like your cluster to live.

## List available cluster templates

{{{ docsVersionInfo.k0rdentName }}} is now fully configured to manage GCP. To create a cluster, begin by listing the available ClusterTemplates provided with {{{ docsVersionInfo.k0rdentName }}}:

```bash
kubectl get clustertemplate -n kcm-system
```

You'll see output resembling what's below. Grab the name of the GCP standalone cluster template in its present version (in the example below, that's `gcp-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.gcpStandaloneCpCluster }}}`):

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

Now, to deploy a cluster, create a YAML file called `my-gcp-clusterdeployment1.yaml`. We'll use this to create
a ClusterDeployment object in {{{ docsVersionInfo.k0rdentName }}}, representing the deployed cluster. The `ClusterDeployment`
identifies for {{{ docsVersionInfo.k0rdentName }}} the `ClusterTemplate` you want to use for cluster creation, the
identity credential object you want to create it under, the GCP project, region, network name, machine types and images
you want to use to host control plane and worker nodes.

> NOTE:
> If you decide to deploy cluster with `publicIP: false`, you should make sure your cluster can communicate
> with the outside world and the load balancer. To achieve this, you may create a Cloud NAT in the region you'd like
> your cluster to live in by following
> [Set up and manage network address translation with Public NAT](https://cloud.google.com/nat/docs/set-up-manage-network-address-translation#create_nat)
> instruction.

> NOTE:
> Image parameter must be the fully qualified GCP image path. Otherwise, the GCP cloud controller manager will not find
> it.

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ClusterDeployment
metadata:
  name: my-gcp-clusterdeployment1
  namespace: kcm-system
spec:
  template: gcp-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.gcpStandaloneCpCluster }}} # name of the clustertemplate
  credential: gcp-credential
  config:
    project: "GCP_PROJECT_NAME"
    region: "GCP_REGION"
    network:
      name: "GCP_NETWORK_NAME" # The name of an existing network or a new network to be created by Cluster API Provider GCP
    controlPlane:
      instanceType: "CP_MACHINE_TYPE"
      image: projects/ubuntu-os-cloud/global/images/ubuntu-2004-focal-v20250213
      publicIP: true
    worker:
      instanceType: "WORKER_MACHINE_TYPE"
      image: projects/ubuntu-os-cloud/global/images/ubuntu-2004-focal-v20250213
      publicIP: true
```
<!-- 
For GKE clusters, the `ClusterDeployment` looks like this:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ClusterDeployment
metadata:
  name: my-gke-clusterdeployment1
  namespace: kcm-system
spec:
  template: gcp-gke-{{{ extra.docsVersionInfo.providerVersions.dashVersions.gcpGkeCluster }}}
  credential: gcp-credential
  propagateCredentials: false # Should be set to `false`
  config:
    workersNumber: 3 # Should be divisible by the number of zones in `machines.nodeLocations`. If `machines.nodeLocations` is not specified, must be divisible by the number of zones in this region (default: 3)
    project: "GCP_PROJECT_NAME"
    region: "GCP_REGION"
    network:
      name: "GCP_NETWORK_NAME"
```
-->
## Apply the ClusterDeployment to deploy the cluster
Finally, we'll apply the ClusterDeployment YAML (`my-gcp-clusterdeployment1.yaml`) to instruct {{{ docsVersionInfo.k0rdentName }}} to deploy the cluster:

```bash
kubectl apply -f my-gcp-clusterdeployment1.yaml
```

Kubernetes should confirm this:

```console
clusterdeployment.k0rdent.mirantis.com/my-gcp-clusterdeployment1 created
```

There will be a delay as the cluster finishes provisioning. Follow the provisioning process with the following command:

```bash
kubectl -n kcm-system get clusterdeployment.k0rdent.mirantis.com my-gcp-clusterdeployment1 --watch
```

## Obtain the cluster's kubeconfig

Now you can retrieve the cluster's kubeconfig:

```bash
kubectl -n kcm-system get secret my-gcp-clusterdeployment1-kubeconfig -o jsonpath='{.data.value}' | base64 -d > my-gcp-clusterdeployment1-kubeconfig.kubeconfig
```

And you can use the kubeconfig to see what's running on the cluster:

```bash
KUBECONFIG="my-gcp-clusterdeployment1-kubeconfig.kubeconfig" kubectl get pods -A
```

## List child clusters

To verify the presence of the child cluster, list the available `ClusterDeployment` objects:

```bash
kubectl get ClusterDeployments -A
```
```console
NAMESPACE    NAME                          READY   STATUS
kcm-system   my-gcp-clusterdeployment1   True    ClusterDeployment is ready
```

## Tear down the child cluster

To tear down the child cluster, delete the `ClusterDeployment`:

```bash
kubectl delete ClusterDeployment my-gcp-clusterdeployment1 -n kcm-system
```
```console
clusterdeployment.k0rdent.mirantis.com "my-gcp-clusterdeployment1" deleted
```

## Next Steps

Now that you've finished the {{{ docsVersionInfo.k0rdentName }}} QuickStart, we have some suggestions for what to do next:

Check out the [Administrator Guide](../admin/index.md) ...

* For a more detailed view of {{{ docsVersionInfo.k0rdentName }}} setup for production
* For details about setting up {{{ docsVersionInfo.k0rdentName }}} to manage clusters on VMware and OpenStack
* For details about using {{{ docsVersionInfo.k0rdentName }}} with cloud Kubernetes distros: AWS EKS and Azure AKS

Or check out the [Demos Repository](https://github.com/k0rdent/demos) for fast, makefile-driven demos of {{{ docsVersionInfo.k0rdentName }}}'s key features!
