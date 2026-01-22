# QuickStart 2 - OpenStack target environment

In this QuickStart unit, we'll be gathering information and performing preparatory steps to enable {{{ docsVersionInfo.k0rdentName }}} (running on your management node) to manage clusters on OpenStack, and deploying a child cluster.

As noted in the [Guide to QuickStarts](./index.md), you'll need administrative access to an OpenStack cloud to complete this step. If you haven't yet created a management node and installed {{{ docsVersionInfo.k0rdentName }}}, go back to [QuickStart 1 - Management node and cluster](./quickstart-1-mgmt-node-and-cluster.md).

Note that if you have already done one of the other quickstarts, such as our AWS QuickStart ([QuickStart 2 - AWS target environment](./quickstart-2-aws.md)) or Azure QuickStart ([QuickStart 2 - Azure target environment](./quickstart-2-azure.md)), you can use the same management cluster, continuing here with steps to add the ability to manage clusters on OpenStack. The {{{ docsVersionInfo.k0rdentName }}} management cluster can accommodate multiple provider and credential setups, enabling management of multiple infrastructures. And even if your management node is external to OpenStack (for example, it could be on an AWS EC2 virtual machine), as long as you permit outbound traffic to all IP addresses from the management node, this should work fine. A big benefit of {{{ docsVersionInfo.k0rdentName }}} is that it provides a single point of control and visibility across multiple clusters on multiple clouds and infrastructures.

> NOTE:
> **Cloud Security 101:** {{{ docsVersionInfo.k0rdentName }}} requires _some_ but not _all_ permissions to manage OpenStack resources via the CAPO (ClusterAPI for OpenStack) provider.

A best practice for using {{{ docsVersionInfo.k0rdentName }}} with OpenStack (this pattern is repeated with other clouds and infrastructures) is to create an Application Credential with the particular permissions {{{ docsVersionInfo.k0rdentName }}} and CAPO require. While it's possible to use a username and password instead of the Application Credential, an Application Credential is strongly recommended because it limits scope and improves security over a raw username/password approach.

> NOTE:
> If you're working on a shared OpenStack account, please ensure that the Application Credential is not already set up before creating a new one.

Creating user identity abstractions with minimal required permissions is one of several principle-of-least-privilege mechanisms used to help ensure security as organizations work with Kubernetes at progressively greater scales. For more on {{{ docsVersionInfo.k0rdentName }}} security best practices, please see the [Administrator Guide](../admin/index.md).

## Install the OpenStack CLI (optional)

If you plan to access OpenStack directly, install the OpenStack CLI. For Ubuntu/Debian:

```bash
sudo apt update
sudo apt install python3-openstackclient
```

Alternatively, you can install it using pip:

```bash
pip install python-openstackclient
```

## Configure OpenStack credentials

You'll need OpenStack credentials to access your OpenStack cloud. The credentials can be provided in one of two ways:

### Option 1: Application Credential (Recommended)

Create an Application Credential in your OpenStack dashboard or via the CLI. The exported list of variables should include:

```bash
OS_AUTH_URL
OS_APPLICATION_CREDENTIAL_ID
OS_APPLICATION_CREDENTIAL_SECRET
OS_REGION_NAME
OS_INTERFACE
OS_IDENTITY_API_VERSION
OS_AUTH_TYPE
```

### Option 2: Username and Password

Alternatively, you can use username and password authentication. You'll need:

```bash
OS_AUTH_URL
OS_USERNAME
OS_PASSWORD
OS_PROJECT_NAME
OS_PROJECT_ID
OS_USER_DOMAIN_NAME
OS_PROJECT_DOMAIN_NAME
OS_REGION_NAME
OS_INTERFACE
OS_IDENTITY_API_VERSION
```

## Create an SSH key pair

Before deploying clusters, you need to create an SSH key pair in OpenStack. This key will be used to access the VMs that {{{ docsVersionInfo.k0rdentName }}} creates.

If you don't already have an SSH key, generate one:

```bash
ssh-keygen -t rsa -f ~/.ssh/openstack_key -N ""
```

Add the public key to OpenStack:

```bash
OS_CLOUD=openstack openstack keypair create --public-key ~/.ssh/openstack_key.pub my-openstack-key
```

Replace `my-openstack-key` with a name of your choice. Note this name as you'll need it in the ClusterDeployment configuration.

You can verify the key was created:

```bash
OS_CLOUD=openstack openstack keypair list
```

## Discover OpenStack resources

Before creating the ClusterDeployment, you'll need to identify several OpenStack resources. Use the OpenStack CLI to discover them:

### Find available flavors (VM sizes)

```bash
OS_CLOUD=openstack openstack flavor list
```

You'll see output like this:

```console { .no-copy }
+----+-----------+-------+------+-----------+-------+-----------+
| ID | Name      |   RAM | Disk | Ephemeral | VCPUs | Is Public |
+----+-----------+-------+------+-----------+-------+-----------+
| 1  | m1.tiny   |   512 |    1 |         0 |     1 | True      |
| 2  | m1.small  |  2048 |   20 |         0 |     1 | True      |
| 3  | m1.medium |  4096 |   40 |         0 |     2 | True      |
| 4  | m1.large  |  8192 |   80 |         0 |     4 | True      |
+----+-----------+-------+------+-----------+-------+-----------+
```

Choose a flavor with at least 2 vCPUs and 4GB RAM for both control plane and worker nodes.

### Find available images

```bash
OS_CLOUD=openstack openstack image list
```

You'll see output like this:

```console { .no-copy }
+--------------------------------------+------------------+--------+
| ID                                   | Name             | Status |
+--------------------------------------+------------------+--------+
| abc123...                            | ubuntu-22.04     | active |
| def456...                            | ubuntu-20.04     | active |
+--------------------------------------+------------------+--------+
```

Choose an Ubuntu 22.04 or 20.04 LTS image that is `active`.

### Find external network

```bash
OS_CLOUD=openstack openstack network list --external
```

You'll see output like this:

```console { .no-copy }
+--------------------------------------+--------+-------------+
| ID                                   | Name   | Subnets     |
+--------------------------------------+--------+-------------+
| xyz789...                            | public | 10.0.0.0/24 |
+--------------------------------------+--------+-------------+
```

Note the name of the external network (commonly `public`, `external`, or `ext-net`).

### Find volume types (optional)

```bash
OS_CLOUD=openstack openstack volume type list
```

You'll see output like this:

```console { .no-copy }
+--------------------------------------+-------------+
| ID                                   | Name        |
+--------------------------------------+-------------+
| abc123...                            | lvmdriver-1 |
| def456...                            | ceph        |
+--------------------------------------+-------------+
```

Note the volume type name if you want to specify it in your ClusterDeployment (usually `lvmdriver-1` or the first one listed).

## Create the OpenStack Credentials Secret

Create a Kubernetes `Secret` containing the `clouds.yaml` that defines your OpenStack environment. Save this as `openstack-cloud-config.yaml`:

> NOTE:
> The `Secret` name, in this case, needs to be exactly `openstack-cloud-config`. See [credential secret](../appendix/appendix-providers.md#credential-secret) for details.

### Using Application Credential (Recommended)

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: openstack-cloud-config
  namespace: kcm-system
  labels:
    k0rdent.mirantis.com/component: "kcm"
type: Opaque
stringData:
  clouds.yaml: |
    clouds:
      openstack:
        auth:
          auth_url: <OS_AUTH_URL>
          application_credential_id: <OS_APPLICATION_CREDENTIAL_ID>
          application_credential_secret: <OS_APPLICATION_CREDENTIAL_SECRET>
        region_name: <OS_REGION_NAME>
        interface: <OS_INTERFACE>
        identity_api_version: <OS_IDENTITY_API_VERSION>
        auth_type: <OS_AUTH_TYPE>
```

### Using Username and Password

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: openstack-cloud-config
  namespace: kcm-system
  labels:
    k0rdent.mirantis.com/component: "kcm"
type: Opaque
stringData:
  clouds.yaml: |
    clouds:
      openstack:
        auth:
          auth_url: <OS_AUTH_URL>
          username: <OS_USERNAME>
          password: <OS_PASSWORD>
          project_name: <OS_PROJECT_NAME>
          project_id: <OS_PROJECT_ID>
          user_domain_name: <OS_USER_DOMAIN_NAME>
          project_domain_name: <OS_PROJECT_DOMAIN_NAME>
        region_name: <OS_REGION_NAME>
        interface: <OS_INTERFACE>
        identity_api_version: <OS_IDENTITY_API_VERSION>
```

Replace the placeholder values with your actual OpenStack credentials.

Apply the YAML to your cluster:

```bash
kubectl apply -f openstack-cloud-config.yaml
```

You should see output resembling this:

```console { .no-copy }
secret/openstack-cloud-config created
```

## Create the {{{ docsVersionInfo.k0rdentName }}} Credential Object

Next, define a `Credential` that references the `Secret` from the previous step. Save this as `openstack-cluster-identity-cred.yaml`:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: Credential
metadata:
  name: openstack-cluster-identity-cred
  namespace: kcm-system
  labels:
    k0rdent.mirantis.com/component: "kcm"
spec:
  description: "OpenStack credentials"
  identityRef:
    apiVersion: v1
    kind: Secret
    name: openstack-cloud-config
    namespace: kcm-system
```

Note that `.spec.identityRef.name` must match the `Secret` you created in the previous step, and `.spec.identityRef.namespace` must be the same as the one that includes the `Secret` (`kcm-system`).

Apply the YAML to your cluster:

```bash
kubectl apply -f openstack-cluster-identity-cred.yaml
```

You should see output resembling this:

```console { .no-copy }
credential.k0rdent.mirantis.com/openstack-cluster-identity-cred created
```

## Create the ConfigMap resource-template object

Create a YAML file with the specification of the resource-template and save it as `openstack-cloud-config-resource-template.yaml`:

> NOTE:
> The `ConfigMap` name, in this case, needs to be exactly `openstack-cloud-config-resource-template`. See [naming the template configmap](../appendix/appendix-providers.md#naming-the-template-configmap) for details.

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: openstack-cloud-config-resource-template
  namespace: kcm-system
  labels:
    k0rdent.mirantis.com/component: "kcm"
  annotations:
    projectsveltos.io/template: "true"
data:
  configmap.yaml: |
    {{- $cluster := .InfrastructureProvider -}}
    {{- $identity := (getResource "InfrastructureProviderIdentity") -}}
    {{- $clouds := fromYaml (index $identity "data" "clouds.yaml" | b64dec) -}}
    {{- if not $clouds }}
      {{ fail "failed to decode clouds.yaml" }}
    {{ end -}}
    {{- $openstack := index $clouds "clouds" "openstack" -}}
    {{- if not (hasKey $openstack "auth") }}
      {{ fail "auth key not found in openstack config" }}
    {{- end }}
    {{- $auth := index $openstack "auth" -}}
    {{- $auth_url := index $auth "auth_url" -}}
    {{- $app_cred_id := index $auth "application_credential_id" -}}
    {{- $app_cred_name := index $auth "application_credential_name" -}}
    {{- $app_cred_secret := index $auth "application_credential_secret" -}}
    {{- $network_id := $cluster.status.externalNetwork.id -}}
    {{- $network_name := $cluster.status.externalNetwork.name -}}
    ---
    apiVersion: v1
    kind: Secret
    metadata:
      name: openstack-cloud-config
      namespace: kube-system
    type: Opaque
    stringData:
      cloud.conf: |
        [Global]
        auth-url="{{ $auth_url }}"
        {{- if $app_cred_id }}
        application-credential-id="{{ $app_cred_id }}"
        {{- end }}
        {{- if $app_cred_name }}
        application-credential-name="{{ $app_cred_name }}"
        {{- end }}
        {{- if $app_cred_secret }}
        application-credential-secret="{{ $app_cred_secret }}"
        {{- end }}
        {{- if and (not $app_cred_id) (not $app_cred_secret) }}
        username="{{ index $openstack "username" }}"
        password="{{ index $openstack "password" }}"
        {{- end }}
        region="{{ index $openstack "region_name" }}"
        [LoadBalancer]
        {{- if $network_id }}
        floating-network-id="{{ $network_id }}"
        {{- end }}
        [Networking]
        {{- if $network_name }}
        public-network-name="{{ $network_name }}"
        {{- end }}
```

Apply the YAML to your cluster:

```bash
kubectl apply -f openstack-cloud-config-resource-template.yaml
```

You should see output resembling this:

```console { .no-copy }
configmap/openstack-cloud-config-resource-template created
```

## List available cluster templates

{{{ docsVersionInfo.k0rdentName }}} is now fully configured to manage OpenStack. To create a cluster, begin by listing the available `ClusterTemplate` objects provided with {{{ docsVersionInfo.k0rdentName }}}:

```bash
kubectl get clustertemplate -n kcm-system
```

You'll see output resembling what's below. Grab the name of the OpenStack standalone cluster template in its present version (in the example below, that's `openstack-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.openstackStandaloneCpCluster }}}`):

```console { .no-copy }
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

Now, to deploy a cluster, create a YAML file called `my-openstack-clusterdeployment1.yaml`. We'll use this to create a `ClusterDeployment` object in {{{ docsVersionInfo.k0rdentName }}}, representing the deployed cluster. The `ClusterDeployment` identifies for {{{ docsVersionInfo.k0rdentName }}} the `ClusterTemplate` you want to use for cluster creation, the identity credential object you want to create it under, plus the region, flavors, images, and SSH key you want to use to host control plane and worker nodes:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ClusterDeployment
metadata:
  name: my-openstack-clusterdeployment1
  namespace: kcm-system
spec:
  template: openstack-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.openstackStandaloneCpCluster }}}
  credential: openstack-cluster-identity-cred
  config:
    clusterLabels: {}
    region: "RegionOne" # Your OpenStack region name
    controlPlane:
      flavor: m1.medium # OpenStack flavor for control plane nodes
      image:
        filter:
          name: ubuntu-22.04 # OpenStack image name or filter
      sshKeyName: my-openstack-key # Name of SSH key in OpenStack
      rootVolume:
        sizeGiB: 30
        volumeType: lvmdriver-1 # Optional: OpenStack volume type
    worker:
      flavor: m1.medium # OpenStack flavor for worker nodes
      image:
        filter:
          name: ubuntu-22.04 # OpenStack image name or filter
      sshKeyName: my-openstack-key # Name of SSH key in OpenStack
      rootVolume:
        sizeGiB: 30
        volumeType: lvmdriver-1 # Optional: OpenStack volume type
    externalNetwork:
      filter:
        name: "public" # Name of external/public network in OpenStack
    identityRef:
      name: "openstack-cloud-config"
      cloudName: "openstack"
      region: "RegionOne"
```

> NOTE:
> When deploying clusters with `openstack-standalone-cp` template version `1-0-12` or newer, the `identityRef.name` parameter is ignored and can be omitted. For older template versions, this parameter is required and must match the name of the `Secret` containing the `clouds.yaml` configuration.

Replace the placeholder values with your actual OpenStack resources:
- `region`: Your OpenStack region (commonly `RegionOne`)
- `flavor`: The flavor name you discovered earlier (e.g., `m1.medium`)
- `image.filter.name`: The image name you discovered earlier (e.g., `ubuntu-22.04`)
- `sshKeyName`: The name of the SSH key you created in OpenStack
- `externalNetwork.filter.name`: The name of your external network (commonly `public`)
- `volumeType`: Optional, the volume type you discovered earlier (e.g., `lvmdriver-1`)

You can adjust `flavor`, `image name`, `region name`, and other parameters to match your OpenStack environment. For more information about the configuration options, see the [OpenStack Template Parameters Reference](../reference/template/template-openstack.md).

## Apply the ClusterDeployment to deploy the cluster

Finally, we'll apply the `ClusterDeployment` YAML (`my-openstack-clusterdeployment1.yaml`) to instruct {{{ docsVersionInfo.k0rdentName }}} to deploy the cluster:

```bash
kubectl apply -f my-openstack-clusterdeployment1.yaml
```

Kubernetes should confirm this:

```console { .no-copy }
clusterdeployment.k0rdent.mirantis.com/my-openstack-clusterdeployment1 created
```

There will be a delay as the cluster finishes provisioning. You can watch the provisioning process with the following command:

```bash
kubectl -n kcm-system get clusterdeployment.k0rdent.mirantis.com my-openstack-clusterdeployment1 --watch
```

In a short while, you'll see output such as:

```console { .no-copy }
NAME                        READY   STATUS
my-openstack-clusterdeployment1   True    ClusterDeployment is ready
```

## Obtain the cluster's kubeconfig

Now you can retrieve the cluster's `kubeconfig`:

```bash
kubectl -n kcm-system get secret my-openstack-clusterdeployment1-kubeconfig -o jsonpath='{.data.value}' | base64 -d > my-openstack-clusterdeployment1.kubeconfig
```

And you can use the `kubeconfig` to see what's running on the cluster:

```bash
KUBECONFIG="my-openstack-clusterdeployment1.kubeconfig" kubectl get pods -A
```

## List child clusters

To verify the presence of the child cluster, list the available `ClusterDeployment` objects:

```bash
kubectl get ClusterDeployments -A
```

You'll see output something like this:

```console { .no-copy }
NAMESPACE    NAME                          READY   STATUS
kcm-system   my-openstack-clusterdeployment1   True    ClusterDeployment is ready
```

## Tear down the child cluster

To tear down the child cluster, delete the `ClusterDeployment`:

```bash
kubectl delete ClusterDeployment my-openstack-clusterdeployment1 -n kcm-system
```

You'll see confirmation like this:

```console { .no-copy }
clusterdeployment.k0rdent.mirantis.com "my-openstack-clusterdeployment1" deleted
```

## Next Steps

Now that you've finished the {{{ docsVersionInfo.k0rdentName }}} QuickStart, we have some suggestions for what to do next:

Check out the [Administrator Guide](../admin/index.md) ...

* For a more detailed view of {{{ docsVersionInfo.k0rdentName }}} setup for production
* For details about setting up {{{ docsVersionInfo.k0rdentName }}} to manage clusters on VMware and OpenStack
* For details about using {{{ docsVersionInfo.k0rdentName }}} with cloud Kubernetes distros: AWS EKS and Azure AKS

<!--
Or check out the [Demos Repository](https://github.com/k0rdent/demos) for fast, makefile-driven demos of {{{ docsVersionInfo.k0rdentName }}}'s key features.
-->
