# Deploy services using MultiClusterService

The `MultiClusterService` object is used to deploy services on multiple matching clusters.

## Creation

You can create the `MultiClusterService` object with the following YAML:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: MultiClusterService
metadata:
  name: <name>
spec:
  clusterSelector:
    matchLabels:
      <key1>: <value1>
      <key2>: <value2>
  serviceSpec:
    services:
    - template: <servicetemplate-1-name>
      name: <release-name>
      namespace: <release-namespace>
    priority: 100
```

## Matching Multiple Clusters

Consider the following example where two clusters have been deployed using `ClusterDeployment` objects:

Command:

```bash
kubectl get clusterdeployments.k0rdent.mirantis.com -n kcm-system --show-labels
```
```console { .no-copy }
NAME             READY   STATUS                      LABELS
dev-cluster-1   True    ClusterDeployment is ready  cluster-deployment/tier=dev
dev-cluster-2   True    ClusterDeployment is ready  cluster-deployment/tier=dev
```

The `dev-cluster-1` `ClusterDeployment` services are specified as:
```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ClusterDeployment
metadata:
  name: dev-cluster-1
  namespace: kcm-system
  labels:
     cluster-deployment/tier: dev
spec:
  . . .
  serviceSpec:
    services:
    - name: kyverno
      namespace: kyverno
      template: kyverno-3-2-6
    - name: ingress-nginx
      namespace: ingress-nginx
      template: ingress-nginx-4-11-0
    priority: 100
  . . .
```

The `dev-cluster-2` `ClusterDeployment` beach-head services are specified as:
```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ClusterDeployment
metadata:
  name: dev-cluster-2
  namespace: kcm-system
  labels:
     cluster-deployment/tier: dev
spec:
  . . .
  serviceSpec:
    services:
    - name: ingress-nginx
      namespace: ingress-nginx
      template: ingress-nginx-4-11-0
    priority: 500
  . . .
```

> NOTE:
> See [Deploy beach-head Services using Cluster Deployment](../../user/services/beach-head.md#deployment-of-beach-head-services) for how to use beach-head services with ClusterDeployment.

Now create the following `global-ingress` `MultiClusterService` object:
```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: MultiClusterService
metadata:
  name: global-ingress
spec:
  clusterSelector:
    matchLabels:
      cluster-deployment/tier: dev
  serviceSpec:
    services:
    - name: ingress-nginx
      namespace: ingress-nginx
      template: ingress-nginx-4-11-3
    priority: 300
```

This MultiClusterService will match any `ClusterDeployment` with the label `cluster-deployment/tier: dev` and deploy chart
version 4.11.3 of ingress-nginx service on it.

### Configuring Custom Values

Refer to "Configuring Custom Values" in [Deploy beach-head Services using Cluster Deployment](../../user/services/beach-head.md#deployment-of-beach-head-services) for more information on using custom values.

### Templating Custom Values
Refer to "Templating Custom Values" in [Deploy beach-head Services using Cluster Deployment](../../user/services/beach-head.md#configuring-custom-values) for more information about dynamic custom values.

### Service Dependencies
Refer to "Service Dependencies" in [Deploy beach-head Services using Cluster Deployment](../../user/services/beach-head.md#service-dependencies) for more information about service depedencies. The only difference compared to a `ClusterDeployment` is that when using service dependencies in a `MultiClusterService` object, the dependencies will be evaluated separately for each of the matching clusters.

### Services Priority and Conflict

The `.spec.serviceSpec.priority` field specifies the priority for the services managed by a ClusterDeployment or MultiClusterService object.

Considering the example above:

1. ClusterDeployment `dev-cluster-1` manages deployment of kyverno (v3.2.6) and ingress-nginx (v4.11.0) with `priority=100` on its cluster.
2. ClusterDeployment `dev-cluster-2` manages deployment of ingress-nginx (v4.11.0) with `priority=500` on its cluster.
3. MultiClusterService `global-ingress` manages deployment of ingress-nginx (v4.11.3) with `priority=300` on both clusters.
   This scenario presents a conflict on both the clusters as the MultiClusterService is attempting to deploy v4.11.3 of ingress-nginx
   on both whereas the ClusterDeployment for each is attempting to deploy v4.11.0 of ingress-nginx.

This is where `.spec.serviceSpec.priority` can be used to specify who gets the priority. Higher number means higer priority and vice versa. In this example:

1. MultiClusterService "global-ingress" will take precedence over ClusterDeployment "dev-cluster-1" and ingress-nginx (v4.11.3) defined in MultiClusterService object will be deployed on the cluster.
2. ClusterDeployment "dev-cluster-2" will take precedence over MultiClusterService "global-ingress" and ingress-nginx (v4.11.0) defined in ClusterDeployment object will be deployed on the cluster.

> NOTE:
> If `priority` values are equal, the first one to reach the cluster wins and deploys its beach-head services.

### MCS Dependencies
Dependencies among MultiClusterServices can be defined using the `.spec.dependsOn[]` field in the `MultiClusterService` object. If `mcs2` depends on `mcs1`, then services defined by `mcs2` will not be deployed on a matching cluster until all services defined by `mcs1` have been successfully deployed on that cluster. For Example:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: MultiClusterService
metadata:
  name: mcs1
spec:
  clusterSelector:
    matchLabels:
      owner: dev-team
  serviceSpec:
    services:
      - template: cert-manager-1-18-2
        name: cert-manager
        namespace: cert-manager
        values: |
          cert-manager:
            crds:
              enabled: true
---
apiVersion: k0rdent.mirantis.com/v1beta1
kind: MultiClusterService
metadata:
  name: mcs2
spec:
  clusterSelector:
    matchLabels:
      owner: dev-team
  dependsOn:
    - mcs1
  serviceSpec:
    services:
      - template: ingress-nginx-4-13-0
        name: ingress-nginx
        namespace: ingress-nginx
        values: |
          ingress-nginx:
            controller:
              replicaCount: 3
      - template: postgres-operator-1-14-0
        name: postgres-operator
        namespace: postgres-operator
        dependsOn:
          - name: ingress-nginx
            namespace: ingress-nginx
```

In this example, for all matching clusters, `ingress-nginx` and `postgres-operators` defined by `mcs2` will not be deployed until `cert-manager` defined by `mcs1` has been successfully deployed.

## Checking Status

The status for the `MultiClusterService` object shows the overall status of the `MultiClusterService` object
along with upgrade paths available for services defined in `.spec.serviceSpec.services[]`. Status of the deployments
can be observed in the matching `ClusterDeployment` objects `.status`:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: MultiClusterService
metadata:
  . . .
  name: global-ingress
  resourceVersion: "38146"
  . . .
spec:
  clusterSelector:
    matchLabels:
      app.kubernetes.io/managed-by: Helm
  serviceSpec:
    services:
    - name: ingress-nginx
      namespace: ingress-nginx
      template: ingress-nginx-4-11-3
    . . .
  . . .
status:
  conditions:
    - lastTransitionTime: "2025-11-07T23:25:25Z"
      message: ""
      observedGeneration: 2
      reason: Succeeded
      status: "True"
      type: ServicesReferencesValidation
    - lastTransitionTime: "2025-11-07T23:25:25Z"
      message: ""
      observedGeneration: 2
      reason: Succeeded
      status: "True"
      type: ServicesDependencyValidation
    - lastTransitionTime: "2025-11-07T23:25:25Z"
      message: ""
      observedGeneration: 2
      reason: Succeeded
      status: "True"
      type: MultiClusterServiceDependencyValidation
    - lastTransitionTime: "2025-11-07T23:28:44Z"
      message: 1/1
      reason: Succeeded
      status: "True"
      type: ClusterInReadyState
    - lastTransitionTime: "2025-11-07T23:28:44Z"
      message: Object is ready
      reason: Succeeded
      status: "True"
      type: Ready
  observedGeneration: 2
  servicesUpgradePaths:
    - availableUpgrades:
        - upgradePaths:
            - ingress-nginx-4-11-3
      name: ingress-nginx
      namespace: ingress-nginx
      template: ingress-nginx-4-11-3
```

## Parameter List
Refer to "Parameter List" in [Deploy beach-head Services using Cluster Deployment](../../user/services/beach-head.md#deployment-of-beach-head-services) for more information.
