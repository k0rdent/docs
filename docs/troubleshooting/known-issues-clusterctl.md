# Issues with clusterctl

When using `clusterctl` to work with child cluster objects, you may run into the following error:

```bash
clusterctl describe cluster kubevirt-demo
```
```output
Error: this version of clusterctl could be used only with "v1beta2" management clusters, "v1beta1" detected
```

This error occurs because the current CAPI operator doesn't support CAPI v1.11 yet. To solve this problem, 
install a version of `clusterctl` **below** 1.11, such as [Clusterctl v1.10.5](https://github.com/kubernetes-sigs/cluster-api/releases/tag/v1.10.5).