# Installing k0rdent

The process of installing k0rdent is straightforward, and involves the following steps:

1. Create a Kubernetes cluster to act as the management cluster
2. Install k0rdent into the management cluster
3. Add the necessary credentials and templates to work with the providers in your infrastructure.

## Create and prepare the Management Kubernetes cluster

The first step is to create the Kubernetes cluster. You should have the following installed:

* Kubernetes
* Helm
* kubectl

### CNCF-certified Kubernetes

k0rdent is designed to run on any CNCF-certified Kubernetes. This gives you great freedom in setting up k0rdent for convenient, secure, and reliable operations.

* Proof-of-concept scale k0rdent implementations can run on a beefy Linux desktop or laptop, using a single-node-capable CNCF Kubernetes distribution like [k0s](https://k0sproject.io), running natively as bare processes, or inside a container with [KinD](https://kind.sigs.k8s.io/).
* More capacious implementations can run on multi-node Kubernetes clusters on bare metal or in clouds.
* Production users can leverage cloud provider Kubernetes variants like Amazon EKS or Azure AKS to quickly create highly-reliable and scalable k0rdent management clusters.
  
### Mixed-use management clusters

k0rdent management clusters can also be mixed-use. For example, a cloud Kubernetes k0rdent management cluster can also be used as a 'mothership' environment for [k0smotron](https://k0smotron.io) hosted control planes managed by k0rdent, integrated with workers bootstrapped (also by k0rdent) on adjacent cloud VMs or on remote VMs, bare metal servers, or edge nodes.

### Where k0rdent management clusters can live

k0rdent management clusters can live anywhere. Unlike prior generations of Kubernetes cluster managers, there's no technical need to co-locate a k0rdent manager with child clusters on a single infrastructure. k0rdent provides a single point of control and visibility across any cloud, any infrastructure, anywhere, on-premise or off. Deciding where to put a management cluster (or multiple clusters) is best done by assessing the requirements of your use case. Considered in the abstract, a k0rdent management cluster should be:

* Resilient and available
* Accessible and secure
* Easy to network
* Scalable (particularly for mixed-use implementations)
* Easy to operate with minimum overhead
* Monitored and observable
* Equipped for backup and disaster recovery

### Minimum requirements for single-node k0rdent management clusters for testing

There isn't a strict minimum system requirement for k0rdent, but the following are recommended for a single node:

* A minimum of 8 GB RAM
* 4 CPU
* 100GB SSD

This configuration is only sufficient for the base case.  If you will run k0rdent Observability and FinOps (KOF) you will need significantly more resources and in particular, much more storage.

### Recommended requirements for single-node k0rdent management clusters for production

We do not recommend running k0rdent in production on a single node.  If you are running in production you will want a scale-out architecture.  These documents do not yet cover this case, but the general Kubernetes administration principles apply.

> IMPORTANT:
> Detailed instructions for deploying k0rdent management clusters into a multi-node configuration and scaling them as needed are COMING SOON!

## Install k0rdent

This section assumes that you already have a kubernetes cluster installed. If you need to setup a cluster you can follow the [Create and prepare a Kubernetes cluster with k0s](#create-and-prepare-a-kubernetes-cluster-with-k0s) guide. 

> NOTE:
> While it is technically possible to run k0rdent on an existing cluster, using a fresh cluster is recommended to avoid conflicts with pre-installed components.

The actual management cluster is a Kubernetes cluster with the k0rdent application installed. The simplest way to install k0rdent is through its Helm chart.  You can find the latest release [here](https://github.com/k0rdent/kcm/tags), and from there you can deploy the Helm chart, as in:

```shell
helm install kcm oci://ghcr.io/k0rdent/kcm/charts/kcm --version {{{ extra.docsVersionInfo.k0rdentDotVersion }}} -n kcm-system --create-namespace
```
```console
Pulled: ghcr.io/k0rdent/kcm/charts/kcm:{{{ extra.docsVersionInfo.k0rdentDotVersion }}}
Digest: sha256:1f75e8e55c44d10381d7b539454c63b751f9a2ec6c663e2ab118d34c5a21087f
NAME: kcm
LAST DEPLOYED: Mon Dec  9 00:32:14 2024
NAMESPACE: kcm-system
STATUS: deployed
REVISION: 1
TEST SUITE: None
```

> NOTE:
> Make sure to specify the correct release version number.

The helm chart deploys the KCM operator and prepares the environment, and KCM then proceeds to deploy the various subcomponents, including CAPI. The entire process takes a few minutes.

## Confirming the deployment

> NOTE:
> After running the helm install command, please wait 5 to 10 minutes for the deployment to stabilize.

To understand whether installation is complete, start by making sure all pods are ready in the `kcm-system` namespace. There should be 17 pod entries:

```shell
kubectl get pods -n kcm-system
```
```console
NAME                                                          READY   STATUS    RESTARTS   AGE
azureserviceoperator-controller-manager-6b4dd86894-2m2wh      1/1     Running   0          57s
capa-controller-manager-64bbcb9f8-kx6wr                       1/1     Running   0          2m3s
capi-controller-manager-66f8998ff5-2m5m2                      1/1     Running   0          2m32s
capo-controller-manager-588f45c7cf-lmkgz                      1/1     Running   0          50s
capv-controller-manager-69f7fc65d8-wbqh8                      1/1     Running   0          46s
capz-controller-manager-544845f786-q8rzn                      1/1     Running   0          57s
helm-controller-7644c4d5c4-t6sjm                              1/1     Running   0          5m1s
k0smotron-controller-manager-bootstrap-9fc48d76f-hppzs        2/2     Running   0          2m9s
k0smotron-controller-manager-control-plane-7df9bc7bf-74vcs    2/2     Running   0          2m4s
k0smotron-controller-manager-infrastructure-f7f94dd76-ppzq4   2/2     Running   0          116s
kcm-cert-manager-895954d88-jplf6                              1/1     Running   0          5m1s
kcm-cert-manager-cainjector-685ffdf549-qlj8m                  1/1     Running   0          5m1s
kcm-cert-manager-webhook-59ddc6b56-8hfml                      1/1     Running   0          5m1s
kcm-cluster-api-operator-8487958779-l9lvf                     1/1     Running   0          3m12s
kcm-controller-manager-7998cdb69-x7kd9                        1/1     Running   0          3m12s
kcm-velero-b68fd5957-fwg2l                                    1/1     Running   0          5m1s
source-controller-6cd7676f7f-7kpjn                            1/1     Running   0          5m1s
```

```shell
kubectl get pods -n kcm-system --no-headers | wc -l
```
```console
17
```

State management is handled by Project Sveltos, so you'll want to make sure that all 9 pods are running/completed in the `projectsveltos` namespace:

```shell
kubectl get pods -n projectsveltos
```

```console
NAME                                     READY   STATUS      RESTARTS   AGE
access-manager-56696cc7f-5txlb           1/1     Running     0          4m1s
addon-controller-7c98776c79-dn9jm        1/1     Running     0          4m1s
classifier-manager-7b85f96469-666jx      1/1     Running     0          4m1s
event-manager-67f6db7f44-hsnnj           1/1     Running     0          4m1s
hc-manager-6d579d675f-fgvk2              1/1     Running     0          4m1s
register-mgmt-cluster-job-rfkdh          0/1     Completed   0          4m1s
sc-manager-55c99d494b-c8wrl              1/1     Running     0          4m1s
shard-controller-5ff9cd796d-tlg79        1/1     Running     0          4m1s
sveltos-agent-manager-7467959f4f-lsnd5   1/1     Running     0          3m34s
```
```shell
kubectl get pods -n projectsveltos --no-headers | wc -l
```
```console
9
```


If any of these pods are missing, simply give k0rdent more time. If there's a problem, you'll see pods crashing and restarting, and you can see what's happening by describing the pod, as in:

```shell
kubectl describe pod classifier-manager-7b85f96469-666jx -n projectsveltos
```

As long as you're not seeing pod restarts, you just need to wait a few minutes.

## Verify that k0rdent itself is ready

The actual measure of whether k0rdent is ready is the state of the `Management` object. To check, issue this command:

```shell
kubectl get Management -n kcm-system
```
```console
NAME   READY   RELEASE     AGE
kcm    True    kcm-{{{ extra.docsVersionInfo.k0rdentVersion }}}   9m
```

## Verify the templates

Next verify whether the KCM templates have been successfully installed and reconciled.  Start with the `ProviderTemplate` objects:

```shell
kubectl get providertemplate -n kcm-system
```

```console
NAME                                   VALID
cluster-api-{{{ extra.docsVersionInfo.k0rdentVersion }}}                      true
cluster-api-provider-aws-{{{ extra.docsVersionInfo.k0rdentVersion }}}         true
cluster-api-provider-azure-{{{ extra.docsVersionInfo.k0rdentVersion }}}       true
cluster-api-provider-openstack-{{{ extra.docsVersionInfo.k0rdentVersion }}}   true
cluster-api-provider-vsphere-{{{ extra.docsVersionInfo.k0rdentVersion }}}     true
k0smotron-{{{ extra.docsVersionInfo.k0rdentVersion }}}                        true
kcm-{{{ extra.docsVersionInfo.k0rdentVersion }}}                              true
projectsveltos-0-45-0                  true
```

Make sure that all templates are not just installed, but valid. Again, this may take a few minutes.

You'll also want to make sure the `ClusterTemplate` objects are installed and valid:

```shell
kubectl get clustertemplate -n kcm-system
```

```console
NAME                            VALID
adopted-cluster-{{{ extra.docsVersionInfo.k0rdentVersion }}}           true
aws-eks-{{{ extra.docsVersionInfo.k0rdentVersion }}}                   true
aws-hosted-cp-{{{ extra.docsVersionInfo.k0rdentVersion }}}             true
aws-standalone-cp-{{{ extra.docsVersionInfo.k0rdentVersion }}}         true
azure-aks-{{{ extra.docsVersionInfo.k0rdentVersion }}}                 true
azure-hosted-cp-{{{ extra.docsVersionInfo.k0rdentVersion }}}           true
azure-standalone-cp-{{{ extra.docsVersionInfo.k0rdentVersion }}}       true
openstack-standalone-cp-{{{ extra.docsVersionInfo.k0rdentVersion }}}   true
vsphere-hosted-cp-{{{ extra.docsVersionInfo.k0rdentVersion }}}         true
vsphere-standalone-cp-{{{ extra.docsVersionInfo.k0rdentVersion }}}     true
```

Finally, make sure the `ServiceTemplate` objects are installed and valid:

```shell
kubectl get servicetemplate -n kcm-system
```

```console
NAME                      VALID
cert-manager-1-16-2       true
dex-0-19-1                true
external-secrets-0-11-0   true
ingress-nginx-4-11-0      true
ingress-nginx-4-11-3      true
kyverno-3-2-6             true
velero-8-1-0              true
```

## Backing up a k0rdent management cluster

In a production environment, you will always want to ensure that your management cluster is backed up. There are a few caveats and things you need to take into account when backing up k0rdent. More info can be found in the guide at [use Velero as a backup provider](admin-backup.md).


## Create and prepare a Kubernetes cluster with k0s

Follow these steps to install and prepare a [k0s kubernetes](https://k0sproject.io) management cluster:

1. Deploy a Kubernetes cluster

    The first step is to create the actual cluster itself. Again, the actual distribution used for the management cluster isn't important, as long as it's a CNCF-compliant distribution. That means you can use an existing EKS cluster, or whatever is your normal corporate standard. To make things simple this guide uses [k0s](https://github.com/k0sproject/k0s/), a small, convenient, and fully-functional distribution:

    ```shell
    curl --proto '=https' --tlsv1.2 -sSf https://get.k0s.sh | sudo sh
    sudo k0s install controller --single
    sudo k0s start
    ```

    k0s includes its own preconfigured version of `kubectl` so make sure the cluster is running:

    ```shell
    sudo k0s kubectl get nodes
    ```

    After 2-3 minutes you should see a single `control-plane` node with a status of `Ready`, as in:

    ```shell
    NAME              STATUS   ROLES            AGE   VERSION
    ip-172-31-29-61   Ready    control-plane    46s   v1.31.2+k0s
    ```

2. Install kubectl

    Everything you do in k0rdent is done by creating and manipulating Kubernetes objects, so you'll need to have `kubectl` installed. You can find the [full install docs here](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/), or just follow these instructions:

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

3. Get the kubeconfig

    In order to access the management cluster you will, of course, need the kubeconfig. Again, if you're using another Kubernetes distribution follow those instructions to get the kubeconfig, but for k0s, the process involves simply copying the existing file and adding it to an environment variable so `kubectl` knows where to find it.

    ```shell
    sudo cp /var/lib/k0s/pki/admin.conf KUBECONFIG
    sudo chmod +r KUBECONFIG
    export KUBECONFIG=./KUBECONFIG
    ```

    Now you should be able to use the non-k0s `kubectl` to see the status of the cluster:

    ```shell
    kubectl get nodes
    ```

    Again, you should see the single k0s node, but by this time it should have had its role assigned, as in:

    ```console
    NAME              STATUS   ROLES           AGE   VERSION
    ip-172-31-29-61   Ready    control-plane   25m   v1.31.2+k0s
    ```

    Now the cluster is ready for installation, which we'll do using Helm.

4. Install Helm

    The easiest way to install k0rdent is through its Helm chart, so let's get Helm installed. You can find the [full instructions here](https://helm.sh/docs/intro/install/), or use these instructions:

    ```shell
    curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
    chmod 700 get_helm.sh
    ./get_helm.sh
    ```

    Helm will be installed into `/usr/local/bin/helm`

