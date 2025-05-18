# QuickStart 1 - Setup Management Cluster

Please review the [Guide to QuickStarts](index.md) for preliminaries. This QuickStart unit details setting up a single-VM environment for managing and interacting with {{{ docsVersionInfo.k0rdentName }}}, and for hosting its components on a single-node local Kubernetes management cluster. Once {{{ docsVersionInfo.k0rdentName }}} is installed on the management cluster, you can drive it by SSHing into the management node (`kubectl` is there and will be provisioned with the appropriate `kubeconfig`) or remotely by various means. For example, you can install the management cluster `kubeconfig` in Lens or another Kubernetes dashboard on your laptop, tunnel across from your own local `kubectl`, and so on.

## Install a single-node k0s cluster locally as the management cluster

[k0s Kubernetes](https://k0sproject.io) is a CNCF-certified minimal single-binary Kubernetes that installs with one command and brings along its own CLI. We're using it to quickly set up a single-node management cluster on our manager node. However, {{{ docsVersionInfo.k0rdentName }}} works on any CNCF-certified Kubernetes. If you choose to use something else, we would love to hear how you set things up to work for you.

> NOTE:
> k0s isn't supported on MacOS, but you can install a test cluster using:
> ```
> brew install kind && kind create cluster -n k0rdent
> ```
> Skip ahead to [Install kubectl](#install-kubectl).

Download and install k0s:

```shell
curl --proto '=https' --tlsv1.2 -sSf https://get.k0s.sh | sudo sh
sudo k0s install controller --enable-worker --no-taints
sudo k0s start
```

You can check to see if the cluster is working by leveraging `kubectl` (installed and configured automatically by k0s) via the k0s CLI:

```shell
sudo k0s kubectl get nodes
```

You should see something like this:

```console
NAME              STATUS   ROLES    AGE   VERSION
ip-172-31-29-61   Ready    <none>   46s   v1.31.2+k0s
```

## Install kubectl

k0s installs a compatible `kubectl` and makes it accessible via its own client. But to make your environment easier to configure, we advise installing `kubectl` the normal way on the manager node and using it to control the local k0s management cluster:

```shell
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl gnupg
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.31/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
sudo chmod 644 /etc/apt/keyrings/kubernetes-apt-keyring.gpg # allow unprivileged APT programs to read this keyring
echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.31/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
sudo chmod 644 /etc/apt/sources.list.d/kubernetes.list   # helps tools such as command-not-found to work correctly
sudo apt-get update
sudo apt-get install -y kubectl
```

## Get the local k0s cluster's kubeconfig for kubectl

On startup, k0s stores the administrator's `kubeconfig` in a local directory, making it easy to access:

```shell
sudo cp /var/lib/k0s/pki/admin.conf KUBECONFIG
sudo chmod +r KUBECONFIG
export KUBECONFIG=./KUBECONFIG
```

At this point, your newly-installed `kubectl` should be able to interoperate with the k0s management cluster with administrative privileges. Test to see that the cluster is ready (this usually takes about one minute):

```shell
kubectl get nodes
```

You should see something like this:

```console
NAME              STATUS   ROLES           AGE   VERSION
ip-172-31-29-61   Ready    control-plane   25m   v1.31.2+k0s
```

## Install Helm

The Helm Kubernetes package manager is used to install {{{ docsVersionInfo.k0rdentName }}} services. We'll install Helm as follows:

```shell
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh
```

Issuing these commands should produce something very much like the following output:

```console
Downloading https://get.helm.sh/helm-v3.16.3-linux-amd64.tar.gz
Verifying checksum... Done.
Preparing to install helm into /usr/local/bin
helm installed into /usr/local/bin/helm
```

## Install {{{ docsVersionInfo.k0rdentName }}}

Now we'll install {{{ docsVersionInfo.k0rdentName }}} itself into the k0s management cluster:

```shell
helm install kcm {{{ extra.docsVersionInfo.ociRegistry }}} --version {{{ extra.docsVersionInfo.k0rdentDotVersion }}} -n kcm-system --create-namespace
```

You'll see something like the following. Ignore the warnings, since this is an ephemeral, non-production, non-shared environment:

```console
WARNING: Kubernetes configuration file is group-readable. This is insecure. Location: ./KUBECONFIG
WARNING: Kubernetes configuration file is world-readable. This is insecure. Location: ./KUBECONFIG
Pulled: ghcr.io/k0rdent/kcm/charts/kcm:{{{ extra.docsVersionInfo.k0rdentDotVersion }}}
Digest: {{{ extra.docsVersionInfo.k0rdentDigestValue }}}
NAME: kcm
LAST DEPLOYED: {{{ extra.docsVersionInfo.k0rdentDigestDate }}}
NAMESPACE: kcm-system
STATUS: deployed
REVISION: 1
TEST SUITE: None
```

{{{ docsVersionInfo.k0rdentName }}} startup takes several minutes.

## Check that {{{ docsVersionInfo.k0rdentName }}} cluster management pods are running

One fundamental {{{ docsVersionInfo.k0rdentName }}} subsystem, k0rdent Cluster Manager (KCM), handles cluster lifecycle management on clouds and infrastructures. For example, it helps you configure and compose clusters and manages infrastructure via Cluster API (CAPI). Before continuing, check that the KCM pods are ready:

```shell
kubectl get pods -n kcm-system   # check pods in the kcm-system namespace
```

You should see something like:

```console
NAME                                                           READY   STATUS
azureserviceoperator-controller-manager-86d566cdbc-rqkt9       1/1     Running
capa-controller-manager-7cd699df45-28hth                       1/1     Running
capi-controller-manager-6bc5fc5f88-hd8pv                       1/1     Running
capv-controller-manager-bb5ff9bd5-7dsr9                        1/1     Running
capz-controller-manager-5dd988768-qjdbl                        1/1     Running
helm-controller-76f675f6b7-4d47l                               1/1     Running
kcm-cert-manager-7c8bd964b4-nhxnq                              1/1     Running
kcm-cert-manager-cainjector-56476c46f9-xvqhh                   1/1     Running
kcm-cert-manager-webhook-69d7fccf68-s46w8                      1/1     Running
kcm-cluster-api-operator-79459d8575-2s9jc                      1/1     Running
kcm-controller-manager-64869d9f9d-zktgw                        1/1     Running
k0smotron-controller-manager-bootstrap-6c5f6c7884-d2fqs        2/2     Running
k0smotron-controller-manager-control-plane-857b8bffd4-zxkx2    2/2     Running
k0smotron-controller-manager-infrastructure-7f77f55675-tv8vb   2/2     Running
source-controller-5f648d6f5d-7mhz5                             1/1     Running
```

Pods reported in states other than Running should become ready momentarily.

## Check that the projectsveltos pods are running

The other fundamental {{{ docsVersionInfo.k0rdentName }}} subsystem, k0rdent State Manager (KSM), handles services configuration and lifecycle management on clusters. This utilizes the [projectsveltos](https://github.com/projectsveltos) Kubernetes Add-On Controller and other open source projects. Before continuing, check that the KSM pods are ready:

```shell
kubectl get pods -n projectsveltos   # check pods in the projectsveltos namespace
```

You should see something like:

```console
NAME                                     READY   STATUS    RESTARTS   AGE
access-manager-cd49cffc9-c4q97           1/1     Running   0          16m
addon-controller-64c7f69796-whw25        1/1     Running   0          16m
classifier-manager-574c9d794d-j8852      1/1     Running   0          16m
conversion-webhook-5d78b6c648-p6pxd      1/1     Running   0          16m
event-manager-6df545b4d7-mbjh5           1/1     Running   0          16m
hc-manager-7b749c57d-5phkb               1/1     Running   0          16m
sc-manager-f5797c4f8-ptmvh               1/1     Running   0          16m
shard-controller-767975966-v5qqn         1/1     Running   0          16m
sveltos-agent-manager-56bbf5fb94-9lskd   1/1     Running   0          15m
```

If you have fewer pods than shown above, just wait 5 minutes or so for all the pods to reconcile and start running.

## Verify that {{{ docsVersionInfo.k0rdentName }}} itself is ready

The actual measure of whether {{{ docsVersionInfo.k0rdentName }}} is ready is the state of the `Management` object. To check, issue this command:

```shell
kubectl get Management -n kcm-system
```
```console
NAME   READY   RELEASE     AGE
kcm    True    kcm-{{{ extra.docsVersionInfo.k0rdentVersion }}}   9m
```

## Verify that KCM provider and related templates are available

{{{ docsVersionInfo.k0rdentName }}} KCM leverages CAPI to manage Kubernetes cluster assembly and host infrastructure. CAPI requires infrastructure providers for different clouds and infrastructure types. These are delivered and referenced within {{{ docsVersionInfo.k0rdentName }}} using templates, instantiated in the management cluster as objects. Before continuing, verify that the default provider template objects are installed and verified. Other templates are also stored as provider templates in this namespace (for example, the templates that determine setup of KCM itself and other parts of the {{{ docsVersionInfo.k0rdentName }}} system, such as projectsveltos, which is a component of {{{ docsVersionInfo.k0rdentName }}} Service Manager (KSM, see below)) as well as the k0smotron subsystem, which enables creation and lifecycle management of managed clusters that use Kubernetes-hosted control planes (such as control planes as pods):

```shell
kubectl get providertemplate -n kcm-system   # list providertemplate objects in the kcm-system namespace
```

You should see output similar to:

```console
NAME                                   VALID
cluster-api-{{{ extra.docsVersionInfo.providerVersions.dashVersions.clusterApi }}}                                 true
cluster-api-provider-aws-{{{ docsVersionInfo.providerVersions.dashVersions.clusterApiProviderAws }}}                    true
cluster-api-provider-azure-{{{ docsVersionInfo.providerVersions.dashVersions.clusterApiProviderAzure }}}                  true
cluster-api-provider-docker-{{{ docsVersionInfo.providerVersions.dashVersions.clusterApiProviderDocker }}}                 true
cluster-api-provider-gcp-{{{ docsVersionInfo.providerVersions.dashVersions.clusterApiProviderGcp }}}                    true
cluster-api-provider-k0sproject-k0smotron-{{{ docsVersionInfo.providerVersions.dashVersions.k0smotron }}}   true
cluster-api-provider-openstack-{{{ docsVersionInfo.providerVersions.dashVersions.clusterApiProviderOpenstack }}}              true
cluster-api-provider-vsphere-{{{ docsVersionInfo.providerVersions.dashVersions.clusterApiProviderVsphere }}}                true
k0smotron-{{{ docsVersionInfo.providerVersions.dashVersions.k0smotron }}}                                   true
kcm-{{{ docsVersionInfo.k0rdentVersion }}}                                         true
projectsveltos-{{{ docsVersionInfo.providerVersions.dashVersions.sveltosProvider }}}                             true
```

## Verify that KCM ClusterTemplate objects are available

CAPI also requires control plane and bootstrap (worker node) providers to construct and/or manage different Kubernetes cluster distros and variants. Again, these providers are delivered and referenced within {{{ docsVersionInfo.k0rdentName }}} using templates, instantiated in the management cluster as `ClusterTemplate` objects. Before continuing, verify that default `ClusterTemplate` objects are installed and valid:

```shell
kubectl get clustertemplate -n kcm-system   # list clustertemplate objects in the kcm-system namespace
```

You should see output similar to:

```console
NAME                            VALID
adopted-cluster-{{{ extra.docsVersionInfo.providerVersions.dashVersions.adoptedCluster }}}           true
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

## Next steps

Your QuickStart management node is now complete, and {{{ docsVersionInfo.k0rdentName }}} is installed and operational. Next, it's time to select [AWS](quickstart-2-aws.md), [Azure](quickstart-2-azure.md), [GCP](quickstart-2-gcp.md), or [Remote SSH Servers](quickstart-2-remote.md) as an environment for hosting managed clusters.
