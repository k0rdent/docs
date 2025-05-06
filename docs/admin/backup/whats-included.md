# What's Included in the Management Backup

The backup includes all of {{{ docsVersionInfo.k0rdentName }}} `kcm` component resources, parts of the `cert-manager`
components required for other components creation, and all the required resources
of `CAPI` and the `ClusterDeployment`s currently in use in the management cluster.

By default, objects satisfying these labels will be included in the backup:

```text
cluster.x-k8s.io/cluster-name="<cluster-deployment-name>"
helm.toolkit.fluxcd.io/name="<cluster-deployment-name>"

cluster.x-k8s.io/provider="bootstrap-<provider>"
cluster.x-k8s.io/provider="control-plane-<provider>"
cluster.x-k8s.io/provider="infrastructure-<provider>"

cluster.x-k8s.io/provider="cluster-api"

controller.cert-manager.io/fao="true"

k0rdent.mirantis.com/component="kcm"
```

An example sorted set of labels, objects satisfying these labels will
be included in the backup:

```text
cluster.x-k8s.io/cluster-name="some-cluster-deployment-name"
cluster.x-k8s.io/provider="bootstrap-k0sproject-k0smotron"
cluster.x-k8s.io/provider="cluster-api"
cluster.x-k8s.io/provider="control-plane-k0sproject-k0smotron"
cluster.x-k8s.io/provider="infrastructure-aws"
controller.cert-manager.io/fao="true"
helm.toolkit.fluxcd.io/name="some-cluster-deployment-name"
k0rdent.mirantis.com/component="kcm"
```
