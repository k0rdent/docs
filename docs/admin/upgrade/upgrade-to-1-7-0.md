# Upgrade to v1.7.0

## Enable KubeVirt Provider

Starting from the v1.7.0 release, KubeVirt is now supported as a provider in {{{ docsVersionInfo.k0rdentName}}}.
This allows users to manage KubeVirt virtual machines alongside Kubernetes clusters. The KubeVirt provider
will be automatically enabled only on new installations of {{{ docsVersionInfo.k0rdentName}}}.
For existing installations, users need to manually enable the KubeVirt provider by following the instructions:

1. Follow the main upgrade instructions [here](./index.md) and wait for the successful upgrade to v1.7.0.

1. Patch the Management object and enable the `cluster-api-provider-kubevirt` provider by running:

    ```bash
    kubectl patch managements kcm \
      --type=json \
      -p='[{"op": "add", "path": "/spec/providers/-", "value": {"name": "cluster-api-provider-kubevirt"}}]'
    ```

1. Wait for the Management object to be ready:

```bash
kubectl wait --for=jsonpath='{.status.components.cluster-api-provider-kubevirt.success}=true' managements.k0rdent.mirantis.com/kcm
```
