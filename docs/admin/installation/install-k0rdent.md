# Install {{{ docsVersionInfo.k0rdentName }}}

This section assumes that you already have a kubernetes cluster installed. If you need to setup a cluster you can follow the [Create and prepare a Kubernetes cluster with k0s](./create-mgmt-clusters/mgmt-create-k0s-single.md) to create a test cluster, or [Create and prepare a production grade Kubernetes cluster with EKS](./create-mgmt-clusters/mgmt-create-eks-multi.md) to create something more substantial. 

The actual management cluster is a Kubernetes cluster with the {{{ docsVersionInfo.k0rdentName }}} application installed. The simplest way to install {{{ docsVersionInfo.k0rdentName }}} is through its Helm chart.  You can find the latest release [here](https://github.com/k0rdent/kcm/tags), and from there you can deploy the Helm chart, as in:

```shell
helm install kcm {{{ extra.docsVersionInfo.ociRegistry }}} --version {{{ extra.docsVersionInfo.k0rdentDotVersion }}} -n kcm-system --create-namespace
```
```console
Pulled: ghcr.io/k0rdent/kcm/charts/kcm:{{{ extra.docsVersionInfo.k0rdentDotVersion }}}
Digest: sha256:c4cd3cceecbed98512515f080e0a2878118d122532d5e5d8b7ef87bcd991639d
NAME: kcm
LAST DEPLOYED: Tue Apr  1 22:19:26 2025
NAMESPACE: kcm-system
STATUS: deployed
REVISION: 1
TEST SUITE: None
```

> NOTE:
> Make sure to specify the correct release version number.

The helm chart deploys the KCM operator and prepares the environment, and KCM then proceeds to deploy the various subcomponents, including CAPI. The entire process takes a few minutes.

