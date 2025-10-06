# Install {{{ docsVersionInfo.k0rdentName }}}

This section assumes that you already have a kubernetes cluster installed. If you need to setup a cluster you can follow the [Create and prepare a Kubernetes cluster with k0s](./create-mgmt-clusters/mgmt-create-k0s-single.md) to create a test cluster, or [Create and prepare a production grade Kubernetes cluster with EKS](./create-mgmt-clusters/mgmt-create-eks-multi.md) to create something more substantial. 

The actual management cluster is a Kubernetes cluster with the {{{ docsVersionInfo.k0rdentName }}} application installed. The simplest way to install {{{ docsVersionInfo.k0rdentName }}} is through its Helm chart.  You can find the latest release [here]({{{ docsVersionInfo.k0rdentTagList }}}), and from there you can deploy the Helm chart, as in:

```bash
helm install kcm {{{ extra.docsVersionInfo.ociRegistry }}} --version {{{ extra.docsVersionInfo.k0rdentDotVersion }}} -n kcm-system --create-namespace
```
```console { .no-copy }
Pulled: ghcr.io/k0rdent/kcm/charts/kcm:{{{ extra.docsVersionInfo.k0rdentDotVersion }}}
Digest: {{{ extra.docsVersionInfo.k0rdentDigestValue }}}
NAME: kcm
LAST DEPLOYED: {{{ extra.docsVersionInfo.k0rdentDigestDate }}}
NAMESPACE: kcm-system
STATUS: deployed
REVISION: 1
TEST SUITE: None
```

> NOTE:
> Make sure to specify the correct release version number.

The helm chart deploys the KCM operator and prepares the environment, and KCM then proceeds to deploy the various subcomponents, including CAPI. The entire process takes a few minutes.

## Cleanup: Uninstall {{{ docsVersionInfo.k0rdentName }}}

And of course when you need to clean up, you can use helm as well. Follow these steps:

1. Remove any `ClusterDeployment` objects in the cluster.

2. Delete the `Management` object:

    ```bash
    kubectl delete management.k0rdent kcm
    ```

3. Remove the kcm Helm release:

    ```bash
    helm uninstall kcm -n kcm-system
    ```

4. Finally, remove the kcm-system namespace:

    ```bash
    kubectl delete ns kcm-system
    ```
