# The Templating System – Common Threads

Whether you are creating templates to add services to a cluster, or to create new clusters or infrastructure providers, templates have a few things in common.

## Sources

Every template references a source, which defines the content that k0rdent will deploy. For `ClusterTemplate` and `ProviderTemplate`, that source is always a Helm chart. For a `ServiceTemplate`, the source can be a Helm chart, Kustomize, or raw resources. 

### Source types

If you don't have one already, start by creating a **source object**. These objects can be one of multiple types.

* A [HelmRepository](https://fluxcd.io/flux/components/source/helmrepositories/) is a typical Helm chart repository, such as `https://charts.bitnami.com/bitnami` or `https://prometheus-community.github.io/helm-charts`.
* A [GitRepository](https://fluxcd.io/flux/components/source/gitrepositories/) is a Git repo containing manifests, Helm charts, or kustomizations, such as `https://github.com/kubernetes-sigs/metrics-server` or `https://github.com/bitnami/charts`.*
* An [OCIRepository](https://fluxcd.io/flux/components/source/ocirepositories/) is an OCI registry that stores Helm charts or other artifacts, such as `oci://ghcr.io/k0rdent/kcm/charts` or `oci://registry-1.docker.io/bitnamicharts`.
* A [Bucket](https://fluxcd.io/flux/components/source/buckets/) is an object storage bucket containing packaged resources, such as an S3 bucket (`s3://my-configs`), a GCS bucket (`gs://my-kustomize-overlays`), or an Azure Blob container (`https://mystorage.blob.core.windows.net/my-container`).
* A `ConfigMap` is a Kubernetes-native object that can hold kustomizations or raw manifests, such as a `ConfigMap` created from `kustomization.tar.gz` or from files like `deployment.yaml` and `namespace.yaml`.
* A `Secret` is a Kubernetes-native object that can also hold kustomizations or raw manifests, such as a `Secret` created from `kustomization.tar.gz` or from files like `deployment.yaml` and `namespace.yaml`.

To deploy a kustomization, archive the folder as `.tar.gz` and create a `ConfigMap` or `Secret` from the archive:

```console { .no-copy }
kubectl create configmap foo --from-file=kustomization.tar.gz
```

To deploy raw resources, create a `ConfigMap` or `Secret` from the resource files:

```console { .no-copy }
kubectl create configmap bar --from-file=namespace.yaml --from-file=deployment.yaml
```

Supported sources:

| **Template**       | `HelmRepository` | `GitRepository` |`OCIRepository` | `Bucket` | `ConfigMap` | `Secret` |
| ------------------ | ---------------- | --------------- | ---------------| -------- | ----------- | -------- |
| `ClusterTemplate`  | X                | X               | X              |          |             |          |
| `ProviderTemplate` | X                | X               | X              |          |             |          |
| `ServiceTemplate`  | X                | X               | X              | X        | X           | X        |

### Source Placement

{{{ docsVersionInfo.k0rdentName }}} looks for resources in specific places. `ProviderTemplate` sources must be cluster-scoped and live in the **system namespace** (`kcm-system` by default). `ServiceTemplate` and `ClusterTemplate` objects, on the other hand, must exist the same namespace as the `ClusterDeployment` that will ultimately use them. This is important, because the source object must also be in the same namespace as the template.

For example, if you have a user who will create a cluster in the `project-ottowa` namespace, the template must exist there, which means the source must as well. You can set the namespace in `metadata.namespace`.

For example, you'd start with a `HelmRepository':

```yaml
apiVersion: source.toolkit.fluxcd.io/v1
kind: HelmRepository
metadata:
  name: custom-repo
  namespace: project-ottowa
  labels:
    k0rdent.mirantis.com/managed: "true"
spec:
  url: oci://ghcr.io/project-a/k0rdent/charts
  interval: 10m
  type: oci
  secretRef:
    name: nick-repo-secret
```

Then the template that references it must also be in the `project-ottowa` namespace:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ClusterTemplate
metadata:
  name: custom-standalone
  namespace: project-ottowa
spec:
  helm:
    chartSpec:
      chart: custom-standalone-cp
      version: 1.0.1
      interval: 10m
      sourceRef:
        kind: HelmRepository
        name: custom-repo
```

And finally, so will the `ClusterDeployment`:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ClusterDeployment
metadata:
  name: ottowa-clusterdeployment
  namespace: project-ottowa
spec:
  template: custom-standalone
  credential: ottowa-cred
  config:
    clusterLabels: {}
    region: ca-central-1
    controlPlane:
      instanceType: t3.small
      rootVolumeSize: 32
    worker:
      instanceType: t3.small
      rootVolumeSize: 32
```

Note that built-in templates ship in the `kcm-system` namespace. For multi-namespace distribution, see [Template Life Cycle Management](../reference/template/index.md#template-life-cycle-management).

Once you have a source, you can define the template to reference it. How you do that depends on the source type.

## Create a Template using Helm

You can configure Helm in **exactly** one of three ways:

1. Reference an existing `HelmChart` object using `.spec.helm.chartRef`.
2. Define the chart inline with `.spec.helm.chartSpec`.
3. *(ServiceTemplate only)* Reference a FluxCD source in `.spec.helm.chartSource`.

Again, these are mutally exclusive.

### Using chartRef

The most modular way to create a template is to use a predefined `HelmChart` object.  For example, you can create that object:

```yaml
apiVersion: source.toolkit.fluxcd.io/v1beta2
kind: HelmChart
metadata:
  name: custom-standalone-cp-chart
  namespace: project-ottowa
spec:
  chart: custom-standalone-cp
  version: 1.0.1
  interval: 10m
  sourceRef:
    kind: HelmRepository
    name: custom-repo
    namespace: kcm-system
```

You can then reference that `HelmChart`:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ClusterTemplate
metadata:
  name: custom-standalone
  namespace: project-ottowa
spec:
  helm:
    chartRef:
      name: custom-standalone-cp-chart
      namespace: project-ottowa
```

### Using chartSpec

Rather than creating the `HelmChart` object, you can provide the information directly in the template using `.spec.helm.chartSpec`. Configure the following parameters:

| **Field**                                                                                                                                                   | **Description**                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `sourceRef`<br/>[LocalHelmChartSourceReference](https://fluxcd.io/flux/components/source/api/v1/#source.toolkit.fluxcd.io/v1.LocalHelmChartSourceReference) | Source object reference (`HelmRepository`, `GitRepository`, or `Bucket`) in the same namespace as template. |
| `chart` string      | Name of the chart in the source.                                                                            |
| `version` string    | Chart version (semver). Defaults to **latest**.                                                             |
| `interval`<br/>[Kubernetes meta/v1.Duration](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration)                                              | Polling frequency. Defaults to **10 minutes**.                                                              |

When you define `.spec.helm.chartSpec`, the controller creates the `HelmChart` automatically.  For example:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ClusterTemplate
metadata:
  name: custom-standalone
  namespace: project-ottowa
spec:
  helm:
    chartSpec:
      chart: custom-standalone-cp
      version: 1.0.1
      interval: 10m
      sourceRef:
        kind: HelmRepository
        name: custom-repo
```

### Using Alternative Template Sources

In addition to Helm, `ServiceTemplate` supports Kustomize and raw resources. In `.spec`, you can use one of:

* `.spec.kustomize`
* `.spec.resources`

Each accepts a `SourceSpec`.

| **Field**          | **Description**                                                                                                |
| ------------------ | -------------------------------------------------------------------------------------------------------------- |
| `deploymentType`   | `Local` or `Remote`. Deploy to the management cluster (local) or managed cluster (remote). Ignored for charts. |
| `localSourceRef`   | Reference to a local source (`ConfigMap`, `Secret`, `GitRepository`, `Bucket`, `OCIRepository`).               |
| `remoteSourceSpec` | Config for a remote source (`git`, `bucket`, or `oci`). Note that these are mutually exclusive.                                 |
| `path`             | Path in the source object pointing to manifests or kustomization config. Ignored for raw resources.            |

For example, to use `.spec.kustomize` your template will look something like this:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ServiceTemplate
metadata:
  name: example-kustomization
  namespace: kcm-system
spec:
  kustomize:
    deploymentType: Remote
    remoteSourceSpec:
      git:
        url: https://github.com/example/repo
        ref:
          branch: main
    path: ./overlays/dev
```

Using `.spec.resources` looks something like this:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ServiceTemplate
metadata:
  name: example-resources
  namespace: kcm-system
spec:
  resources:
    deploymentType: Local
    localSourceRef:
      kind: ConfigMap
      name: my-configmap
    path: ./manifests
```

## Required and Exposed Providers

Each template must define its Cluster API providers. In the case of the `ProviderTemplate`, these are the providers, the template exposes. In the case of the `ClusterTemplate` and `ServiceTemplate`, these are the providers that are required in order for the template to function properly.

There are three supported provider types: `infrastructure`, `bootstrap`, and `control-plane`.

You can define providers in two ways:

1. List them in `spec.providers` from within the template.
2. Add them as annotations in `Chart.yaml`.

To list them as part of the template, you'll use the `spec.providers` field, as in:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ClusterTemplate
metadata:
  name: custom-standalone
  namespace: project-ottowa
spec:
  helm:
    chartRef:
      name: custom-standalone-cp-chart
      namespace: project-ottowa
  providers:
  - bootstrap-k0sproject-k0smotron
  - control-plane-k0sproject-k0smotron
  - infrastructure-aws
```

However, you don't need to leave this to the people creating templates. Instead, you can define them in the chart itself using annotations in `Chart.yaml`:

```yaml
apiVersion: v2
name: custom-standalone-cp
description: |
  A KCM template to deploy a k0s cluster on AWS with bootstrapped control plane nodes.
type: application
version: 1.0.1
appVersion: "v1.32.6+k0s.0"
annotations:
  cluster.x-k8s.io/provider: infrastructure-aws, control-plane-k0sproject-k0smotron, bootstrap-k0sproject-k0smotron
  cluster.x-k8s.io/bootstrap-k0sproject-k0smotron: v1beta1
  cluster.x-k8s.io/control-plane-k0sproject-k0smotron: v1beta1
  cluster.x-k8s.io/infrastructure-aws: v1beta2
```

## Compatibility Attributes

Templates can also declare compatibility with specific CAPI versions, provider contracts, or Kubernetes versions. These values can be set in the template `.spec`, or they can be set in the chart annotations, as in the section on [Required and Exposed Providers](#required-and-exposed-providers). In case of a coflict between the two, the value specified in the template `.spec` takes precedence. 

> NOTE:
> All of the compatibility attributes are optional, and validation checks only take place
> if **both** of the corresponding type attributes
> (for example, provider contract versions in both `ProviderTemplate` and `ClusterTemplate`) are set.

### ServiceTemplate and Kubernetes Version Constraints

If a workload can only run on specific versions of Kubernetes, you can define Kubernetes version constraints in `.spec.k8sConstraint`:

**Spec example:**

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ServiceTemplate
metadata:
  name: nginx-service
  namespace: project-ottowa
spec:
  k8sConstraint: "^1.30.0"
  helm:
    chartRef:
      name: nginx-chart
      namespace: project-ottowa
```

Or you can define it in the Helm chart that backs the `ServiceTemplate`:

```yaml
k0rdent.mirantis.com/k8s-version-constraint: ^1.30.0
```

### ClusterTemplate and Kubernetes version compatibility

You can also set the target Kubernetes version for `ClusterTemplate` objects:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ClusterTemplate
spec:
  k8sVersion: 1.30.0
  providers:
  - bootstrap-k0sproject-k0smotron
  - control-plane-k0sproject-k0smotron
  - infrastructure-aws
  providerContracts:
    bootstrap-k0sproject-k0smotron: v1beta1
    control-plane-k0sproject-k0smotron: v1beta1
    infrastructure-aws: v1beta2
```

You can also set it using `annotations` in the underlying chart:

```yaml
annotations:
  cluster.x-k8s.io/provider: infrastructure-aws, control-plane-k0sproject-k0smotron, bootstrap-k0sproject-k0smotron
  cluster.x-k8s.io/bootstrap-k0sproject-k0smotron: v1beta1
  cluster.x-k8s.io/control-plane-k0sproject-k0smotron: v1beta1
  cluster.x-k8s.io/infrastructure-aws: v1beta2
  k0rdent.mirantis.com/k8s-version: 1.30.0
```

### ProviderTemplate and CAPI contract versions

The `ProviderTemplate` resource has dedicated fields to set compatible [`CAPI` contract ](https://cluster-api.sigs.k8s.io/developer/providers/contracts/overview), along
with CRDs contract versions supported by the provider. These contract versions will then be set accordingly in the `.status` field.
Compatibility contract versions are key-value pairs, where the key is **the core `CAPI` contract version**,
and the value is an underscore-delimited (_) list of provider contract versions supported by the core `CAPI`.
For the core `CAPI` Template values should be empty.

You can define the supported CAPI contract versions in `.spec.capiContracts`:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ProviderTemplate
spec:
  providers:
  - infrastructure-aws
  capiContracts:
    v1alpha3: v1alpha3
    v1alpha4: v1alpha4
    v1beta1: v1beta1_v1beta2
```

You can also set them in the chart `annotations`:

```yaml
...
annotations:
  cluster.x-k8s.io/provider: infrastructure-aws
  cluster.x-k8s.io/v1alpha3: v1alpha3
  cluster.x-k8s.io/v1alpha4: v1alpha4
  cluster.x-k8s.io/v1beta1: v1beta1_v1beta2
```


### Compatibility Enforcement

The aforedescribed attributes are checked for compliance with the following rules:

* Both the exact and constraint version of the same type (for example `k8sVersion` and `k8sConstraint`) must
be set, otherwise no check is performed;
* If a `ClusterTemplate` object's provider's contract version does not satisfy contract versions
from the related `ProviderTemplate` object, updates to the `ClusterDeployment` object will be blocked;
* If a `ProviderTemplate` object's `CAPI` contract version
(for example, in a `v1beta1: v1beta1_v1beta2` key-value pair, the key `v1beta1` is the core `CAPI` contract version)
is not listed in the core `CAPI` `ProviderTemplate` object, the updates to the `Management` object will be blocked;
* If a `ClusterTemplate` object's exact kubernetes version does not satisfy the kubernetes version
constraint from the related `ServiceTemplate` object, the updates to the `ClusterDeployment` object will be blocked.

