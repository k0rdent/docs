# Install k0rdent

This section assumes that you already have a kubernetes cluster installed. If you need to setup a cluster you can follow the [Create and prepare a Kubernetes cluster with k0s](./create-mgmt-clusters/mgmt-create-k0s-single.md) to create a test cluster, or [Create and prepare a production grade Kubernetes cluster with EKS](./create-mgmt-clusters/mgmt-create-eks-multi.md) to create something more substantial. 

The actual management cluster is a Kubernetes cluster with the k0rdent application installed. The simplest way to install k0rdent is through its Helm chart.  You can find the latest release [here](https://github.com/k0rdent/kcm/tags), and from there you can deploy the Helm chart, as in:

```shell
helm install kcm {{{ extra.docsVersionInfo.ociRegistry }}} --version {{{ extra.docsVersionInfo.k0rdentDotVersion }}} -n kcm-system --create-namespace
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

