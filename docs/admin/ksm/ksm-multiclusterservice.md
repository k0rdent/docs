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

> NOTE:
> If the `MultiClusterService` matches a `ClusterDeployment` in a namespace other than `kcm-system`, the MCS will expect the `ServiceTemplates` used in its `.spec.serviceSpec.services` to already be available and ready in that namespace as well as in the `kcm-system` namespace.

### Configuring Custom Values

Refer to "Configuring Custom Values" in [Deploy beach-head Services using Cluster Deployment](../../user/services/beach-head.md#deployment-of-beach-head-services) for more information on using custom values.

### Templating Custom Values
Refer to "Templating Custom Values" in [Deploy beach-head Services using Cluster Deployment](../../user/services/beach-head.md#configuring-custom-values) for more information about dynamic custom values.

### Service Dependencies
Refer to "Service Dependencies" in [Deploy beach-head Services using Cluster Deployment](../../user/services/beach-head.md#service-dependencies) for more information about service depedencies. The only difference compared to a `ClusterDeployment` is that when using service dependencies in a `MultiClusterService` object, the dependencies will be evaluated separately for each of the matching clusters.

### Services Priority and Conflict

> WARNING:
> `.spec.serviceSpec.priority` is **deprecated**. Use `.spec.serviceSpec.provider.config.priority` instead.

The priority for the services managed by a ClusterDeployment or MultiClusterService is set via `.spec.serviceSpec.provider.config.priority` (or the deprecated `.spec.serviceSpec.priority`).

Considering the example above:

1. ClusterDeployment `dev-cluster-1` manages deployment of kyverno (v3.2.6) and ingress-nginx (v4.11.0) with `priority=100` on its cluster.
2. ClusterDeployment `dev-cluster-2` manages deployment of ingress-nginx (v4.11.0) with `priority=500` on its cluster.
3. MultiClusterService `global-ingress` manages deployment of ingress-nginx (v4.11.3) with `priority=300` on both clusters.
   This scenario presents a conflict on both the clusters as the MultiClusterService is attempting to deploy v4.11.3 of ingress-nginx
   on both whereas the ClusterDeployment for each is attempting to deploy v4.11.0 of ingress-nginx.

This is where priority can be used to specify who gets the priority. Higher number means higher priority and vice versa. In this example:

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

Both `dependsOn` between services within a `ClusterDeployment`/`MultiClusterService` and sequential upgrades through a `ServiceTemplateChain` gate on the service reaching `state == Deployed`. That state reflects the verifier's confirmation that the workload is actually healthy on the child cluster, not merely that Sveltos accepted the release. Dependent services and next chain steps advance only after the current service is verified. See [Service State Verification](ksm-service-state-verification.md) for the mechanics.

### Keeping Services on Selector Mismatch

By default, when a cluster's labels no longer match a `MultiClusterService`'s `clusterSelector` (or the selector is cleared), the services previously deployed on that cluster by this MCS are removed.

Setting `.spec.keepServicesOnSelectorMismatch: true` preserves those services on clusters that fall out of the selector. This is useful for per-cluster opt-in rollouts: you can remove a cluster from the selector without tearing down its services, allowing manual control over which clusters adopt new service versions.

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: MultiClusterService
metadata:
  name: global-ingress
spec:
  clusterSelector:
    matchLabels:
      cluster-deployment/tier: dev
  keepServicesOnSelectorMismatch: true
  serviceSpec:
    services:
    - name: ingress-nginx
      namespace: ingress-nginx
      template: ingress-nginx-4-11-3
```

Defaults to `false`.

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
        - versions:
            - name: ingress-nginx-4-12-0
              version: 4.12.0
      name: ingress-nginx
      namespace: ingress-nginx
      template: ingress-nginx-4-11-3
```

## Matching Clusters Status

The `.status.matchingClusters[]` field lists all clusters currently matched by the `MultiClusterService` selector, along with their deployment state.

Each entry contains:

| Field                  | Type      | Description                                                                 |
|------------------------|-----------|-----------------------------------------------------------------------------|
| `name`                 | string    | Name of the matched ClusterDeployment                                       |
| `namespace`            | string    | Namespace of the matched ClusterDeployment                                  |
| `kind`                 | string    | Kind of the referenced object (typically `ClusterDeployment`)               |
| `apiVersion`           | string    | API version of the referenced object                                        |
| `regional`             | bool      | Whether the cluster is a regional cluster (default: `false`)                |
| `deployed`             | bool      | Whether all services have been successfully deployed on this cluster         |
| `lastTransitionTime`   | timestamp | When the `deployed` state last changed                                      |

Example:

```yaml
status:
  matchingClusters:
    - apiVersion: k0rdent.mirantis.com/v1beta1
      kind: ClusterDeployment
      name: dev-cluster-1
      namespace: kcm-system
      regional: false
      deployed: true
      lastTransitionTime: "2025-11-07T23:28:44Z"
    - apiVersion: k0rdent.mirantis.com/v1beta1
      kind: ClusterDeployment
      name: dev-cluster-2
      namespace: kcm-system
      regional: false
      deployed: false
      lastTransitionTime: "2025-11-07T23:25:10Z"
```

## Parameter List
Refer to "Parameter List" in [Deploy beach-head Services using Cluster Deployment](../../user/services/beach-head.md#deployment-of-beach-head-services) for more information.
