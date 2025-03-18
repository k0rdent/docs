# Deployment of beach-head services

Beach-head services can be installed on a cluster deployment (that is, a target cluster) using the `ClusterDeployment` object, just as with a single service. Consider the following example of a `ClusterDeployment` object for AWS Infrastructure Provider with beach-head services.

```yaml
apiVersion: k0rdent.mirantis.com/v1alpha1
kind: ClusterDeployment
metadata:
  name: my-cluster-deployment
  namespace: kcm-system
spec:
  config:
    clusterLabels: {}
    clusterIdentity:
      name: aws-cluster-identity
      namespace: kcm-system
    controlPlane:
      amiID: ami-0eb9fdcf0d07bd5ef
      instanceProfile: control-plane.cluster-api-provider-aws.sigs.k8s.io
      instanceType: t3.small
      controlPlaneNumber: 1
      publicIP: true
      region: ca-central-1
    worker:
      amiID: ami-0eb9fdcf0d07bd5ef
      instanceProfile: nodes.cluster-api-provider-aws.sigs.k8s.io
      instanceType: t3.small
    workersNumber: 1
  credential: aws-cluster-identity-cred
  serviceSpec:
    services:
      - template: kyverno-3-2-6
        name: kyverno
        namespace: kyverno
      - template: ingress-nginx-4-11-3
        name: ingress-nginx
        namespace: ingress-nginx
    priority: 100
  template: aws-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsStandaloneCpCluster }}}
```

In the example above, the fields under `serviceSpec` are relevant to the deployment of beach-head services.

> NOTE:
> Refer to the [Template Guide](../../reference/template/template-intro.md) for more detail about these fields.

This example `ClusterDeployment` object deploys kyverno and ingress-nginx, as referred to by their
service templates respectively, on the target cluster.  As before, the `ServiceTemplate` includes information on the service. For example, here is the `ServiceTemplate` for kyverno:

```yaml
apiVersion: k0rdent.mirantis.com/v1alpha1
kind: ServiceTemplate
metadata:
  name: kyverno-3-2-6
  annotations:
    helm.sh/resource-policy: keep
spec:
  helm:
    chartSpec:
      chart: kyverno
      version: 3.2.6
      interval: 10m0s
      sourceRef:
        kind: HelmRepository
        name: k0rdent-catalog
```

The `k0rdent-catalog` helm repository hosts the actual kyverno chart version 3.2.6.
For more details see the [Bring your own Templates](../../reference/template/template-byo.md) guide.

## Configuring Custom Values

Helm values can be passed to each beach-head service with the `.spec.serviceSpec.services[].values` field in the `ClusterDeployment` or `MultiClusterService` object. For example:

```yaml
apiVersion: k0rdent.mirantis.com/v1alpha1
kind: ClusterDeployment
metadata:
  name: my-clusterdeployment
  namespace: kcm-system
spec:
  . . .
  serviceSpec:
    services:
    - template: ingress-nginx-4-11-3
      name: ingress-nginx
      namespace: ingress-nginx
      values: |
        ingress-nginx:
          controller:
            replicaCount: 3
    - name: kyverno
      namespace: kyverno
      template: kyverno-3-2-6
      values: |
        kyverno:
          admissionController:
            replicas: 3
    - name: motel-regional
      namespace: motel
      template: motel-regional-0-1-1
      values: |
        victoriametrics:
          vmauth:
            ingress:
              host: vmauth.kcm0.example.net
            credentials:
              username: motel
              password: motel
        grafana:
          ingress:
            host: grafana.kcm0.example.net
   . . .
```
> NOTE: 
> The values for ingress-nginx and kyverno start with the "ingress-nginx:" and "kyverno:" keys respectively because
> the helm charts used by the ingress-nginx-4-11-3 and kyverno-3-2-6 `ServiceTemplate` objects use the official upstream
> helm charts for ingress-nginx and kyverno as dependencies.

## Templating Custom Values

Using the Sveltos templating feature, we can also write templates that can be useful for automatically fetching pre-existing information within the cluster. For example:

```yaml
apiVersion: k0rdent.mirantis.com/v1alpha1
kind: ClusterDeployment
metadata:
  name: my-clusterdeployment
  namespace: kcm-system
spec:
  . . .
  serviceSpec:
    services:
    - template: motel-{{{ extra.docsVersionInfo.k0rdentVersion }}}
      name: motel
      namespace: motel
    - template: myappz-0-3-0
      name: myappz
      namespace: myappz
      values: |
        controlPlaneEndpointHost: {{ .Cluster.spec.controlPlaneEndpoint.host }}
        controlPlaneEndpointPort: "{{ .Cluster.spec.controlPlaneEndpoint.port }}"
    priority: 100
    . . .        
```

In this case, the host and port information will be fetched from the spec of the CAPI cluster that hosts this `ClusterDeployment`.
