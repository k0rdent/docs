# Adding a `Service` to a `ClusterDeployment`

To add the service defined by this template to a cluster, you simply add it to the `ClusterDeployment` object
when you create it, as in:

```yaml
apiVersion: k0rdent.mirantis.com/v1alpha1
kind: ClusterDeployment
metadata:
  name: my-cluster-deployment
  namespace: tenant42
spec:
  config:
    clusterLabels: {}
  template: aws-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsStandaloneCpCluster }}}
  credential: aws-credential
  serviceSpec:
    services:
      - template: project-ingress-nginx-4.11.0
        name: ingress-nginx
        namespace: tenant42
    priority: 100
```
As you can see, you're simply referencing the template in the `.spec.serviceSpec.services[].template` field of the `ClusterDeployment`
to tell {{{ docsVersionInfo.k0rdentName }}} that you want this service to be part of this cluster.

If you wanted to add this service to an existing cluster, you would simply patch the definition of the `ClusterDeployment`, as in:

```yaml
kubectl patch clusterdeployment my-cluster-deployment -n tenant42 --type='merge' -p '
spec:
  serviceSpec:
    services:
      - template: project-ingress-nginx-4.11.0
        name: ingress-nginx
        namespace: tenant42
```

Let's look at a more complex case, involving deploying beach-head services on a single cluster.
