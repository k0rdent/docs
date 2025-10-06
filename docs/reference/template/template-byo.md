# Bring Your Own Templates

In addition to the templates that ship with {{{ docsVersionInfo.k0rdentName }}}, it's possible to make your own. These might represent different types of clusters, or they may represent additional services to add to a cluster. Follow these steps:

## Create a Source Object

> INFO:
> Skip this step if you're using an existing source.

`ClusterTemplate` and `ProviderTemplate` are based on a Helm chart. `ServiceTemplate`, apart from Helm chart, can be also based on kustomization or raw resources.
Regardless of the type of the resources to be deployed using template, the corresponding source object should be created.

The source can be one of the following types:

| **Template**       | `HelmRepository` | `Bucket` | `OCIRepository` | `ConfigMap` | `Secret` |
|--------------------|------------------|----------|-----------------|-------------|----------|
| `ClusterTemplate`  | V                | X        | X               | X           | X        |
| `ProviderTemplate` | V                | X        | X               | X           | X        |
| `ServiceTemplate`  | V                | V        | V               | V           | V        |

- [HelmRepository](https://fluxcd.io/flux/components/source/helmrepositories/)
- [GitRepository](https://fluxcd.io/flux/components/source/gitrepositories/)
- [Bucket](https://fluxcd.io/flux/components/source/buckets/)

> INFO:
> `ConfigMap` and `Secret` can only be used as a source of kustomization or raw resources for `ServiceTemplate`.
> To deploy kustomization using `ConfigMap` or `Secret` the kustomization folder must be archived in *.tar.gz and
> then `ConfigMap` or `Secret` must be created from resulting archive:
>
> ```console { .no-copy }
> kubectl create configmap foo --from-file=kustomization.tar.gz
> ```
>
> To deploy raw resources using `ConfigMap` or `Secret` source object must be created from raw resource files:
>
> ```console { .no-copy }
> kubectl create configmap bar --from-file=namespace.yaml --from-file=deployment.yaml
> ```

Note that it's important to pay attention to where the source resides. Cluster-scoped `ProviderTemplate` objects must reside in the **system** namespace (`kcm-system` by default) but other template sources must reside in the same namespace as the templates that will come from them.

For example, this YAML describes a custom `Source` object of `kind` `HelmRepository`:

> NOTE:
> The custom `HelmRepository` must have the label
> `k0rdent.mirantis.com/managed: "true"`.

```yaml
apiVersion: source.toolkit.fluxcd.io/v1
kind: HelmRepository
metadata:
  name: k0rdent-catalog
  namespace: kcm-system
  labels:
    k0rdent.mirantis.com/managed: "true"
spec:
  insecure: true
  interval: 10m0s
  provider: generic
  type: oci
  url: oci://ghcr.io/k0rdent/kcm/charts
```

## Create the Template

Once you have the source, you can create the actual template. This template can be one of three types:

* `ClusterTemplate`
* `ServiceTemplate`
* `ProviderTemplate`

For `ClusterTemplate` and `ServiceTemplate` objects, configure the namespace where this template should reside
(`metadata.namespace`).

For defining the Helm chart, you have three choices. You can either:

1. Specify the actual Helm chart definition in the `.spec.helm.chartSpec` field of the
   [HelmChartSpec](https://fluxcd.io/flux/components/source/api/v1/#source.toolkit.fluxcd.io/v1.HelmChartSpec) kind,
2. Reference an existing `HelmChart` object in `.spec.helm.chartRef`

> NOTE:
> Next option is supported for `ServiceTemplate` objects only

3. Reference FluxCD source of the Helm chart in `.spec.helm.chartSource`

> NOTE:
> `spec.helm.chartSpec`, `spec.helm.chartRef`, `spec.helm.chartSource` are mutually exclusive.

To automatically create the `HelmChart` for the `Template`, configure the following custom helm chart parameters
under `spec.helm.chartSpec`:

| **Field**                                                                                                                                                   | **Description**                                                                                                                     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| `sourceRef`<br/>[LocalHelmChartSourceReference](https://fluxcd.io/flux/components/source/api/v1/#source.toolkit.fluxcd.io/v1.LocalHelmChartSourceReference) | Reference to the source object (for example, `HelmRepository`, `GitRepository`, or `Bucket`) in the same namespace as the Template. |
| `chart`<br/>string                                                                                                                                          | The name of the Helm chart available in the source.                                                                                 |
| `version`<br/>string                                                                                                                                        | Version is the chart version semver expression. Defaults to **latest** when omitted.                                                |
| `interval`<br/>[Kubernetes meta/v1.Duration](https://pkg.go.dev/k8s.io/apimachinery/pkg/apis/meta/v1#Duration)                                              | The frequency at which the `sourceRef` is checked for updates. Defaults to **10 minutes**.                                          |

For the complete list of the `HelmChart` parameters, see:
[HelmChartSpec](https://fluxcd.io/flux/components/source/api/v1/#source.toolkit.fluxcd.io/v1.HelmChartSpec).

The controller automatically creates the `HelmChart` object based on the chartSpec defined in
`.spec.helm.chartSpec`.

> NOTE:
> `ClusterTemplate` and `ServiceTemplate` objects should reside in the same namespace as the `ClusterDeployment`
> referencing them. The `ClusterDeployment` can't reference the Template from another namespace (the creation request will
> be declined by the admission webhook). All `ClusterTemplate` and `ServiceTemplate` objects shipped with KCM reside in the
> system namespace (defaults to `kcm-system`). To get the instructions on how to distribute Templates along multiple
> namespaces, read [Template Life Cycle Management](index.md#template-life-cycle-management).

### Alternative Template Sources

Aside from Helm charts, `ServiceTemplate` also supports alternative resource definitions using either Kustomize or raw resources.

You can use one of the following fields in `.spec` (they are mutually exclusive):

- `.spec.kustomize`
- `.spec.resources`
- `.spec.helm.chartSource`

Each of these fields accepts a `SourceSpec`, which defines the origin of the template content. Only one can be used at a time.

A `SourceSpec` includes:

| **Field**          | **Description**                                                                                                                                                                      |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `deploymentType`   | Must be either `Local` or `Remote`. Defines whether resources will be deployed to management (local) or to managed (remote) cluster. Ignored if defined in `.spec.helm.chartSource`. |
| `localSourceRef`   | Reference to a local source (e.g., `ConfigMap`, `Secret`, `GitRepository`, `Bucket`, `OCIRepository`). `ConfigMap` and `Secret` are not supported in `.spec.helm.chartSource`.       |
| `remoteSourceSpec` | Configuration for a remote source. Includes support for `Git`, `Bucket`, or `OCI` repositories.                                                                                      |
| `path`             | Path within the source object pointing to the manifests or kustomize config. Ignored when deploying raw resources using `ConfigMap` or `Secret`                                      |

> NOTE:
> Fields `.spec.*.remoteSourceSpec.git`, `.spec.*.remoteSource.Spec.bucket` and `.spec.*.remoteSourceSpec.oci` are mutually exclusive.

Example using `.spec.kustomize`:

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

Example using `.spec.resources`:

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

All of the above follow the same mutual exclusivity and version constraint rules as Helm.

## Required and exposed providers definition

The `*Template` object must specify the list of Cluster API providers that are either **required** (for
`ClusterTemplates` and `ServiceTemplates`) or **exposed** (for `ProviderTemplates`). These providers include
`infrastructure`, `bootstrap`, and `control-plane`. This can be achieved in two ways:

1. By listing the providers explicitly in the `spec.providers` field.
2. Alternatively, by including specific annotations in the `Chart.yaml` of the referenced Helm chart. The annotations should list the providers as a `comma-separated` value.

For example:

In a `Template` spec:

```yaml
spec:
  providers:
  - bootstrap-k0sproject-k0smotron
  - control-plane-k0sproject-k0smotron
  - infrastructure-aws
```

In a `Chart.yaml`:

```bash
annotations:
    cluster.x-k8s.io/provider: infrastructure-aws, control-plane-k0sproject-k0smotron, bootstrap-k0sproject-k0smotron
```

## Compatibility attributes

Each of the `*Template` resources has compatibility versions attributes to constraint the core `CAPI`, `CAPI` provider or Kubernetes versions.
CAPI-related version constraints must be set in the [`CAPI` contract format](https://cluster-api.sigs.k8s.io/developer/providers/contracts/overview).
Kubernetes version constraints must be set in the Semantic Version format.
Each attribute can be set either via the corresponding `.spec` fields or via the annotations.
Values set via the `.spec` have precedence over the values set via the annotations.

> NOTE:
> All of the compatibility attributes are optional, and validation checks only take place
> if **both** of the corresponding type attributes
> (e.g. provider contract versions in both `ProviderTemplate` and `ClusterTemplate`) are set.

1. The `ProviderTemplate` resource has dedicated fields to set compatible `CAPI` contract versions along
with CRDs contract versions supported by the provider.
Given contract versions will then be set accordingly in the `.status` field.
Compatibility contract versions are key-value pairs, where the key is **the core `CAPI` contract version**,
and the value is an underscore-delimited (_) list of provider contract versions supported by the core `CAPI`.
For the core `CAPI` Template values should be empty.

    Example with the `.spec`:

    ```yaml
    apiVersion: k0rdent.mirantis.com/v1beta1
    kind: ProviderTemplate
    # ...
    spec:
      providers:
      - infrastructure-aws
      capiContracts:
        # commented is the example exclusively for the core CAPI Template
        # v1alpha3: ""
        # v1alpha4: ""
        # v1beta1: ""
        v1alpha3: v1alpha3
        v1alpha4: v1alpha4
        v1beta1: v1beta1_v1beta2
    ```

    Example with the `annotations` in the `Chart.yaml` with the same logic
    as in the `.spec`:

    ```yaml
    annotations:
      cluster.x-k8s.io/provider: infrastructure-aws
      cluster.x-k8s.io/v1alpha3: v1alpha3
      cluster.x-k8s.io/v1alpha4: v1alpha4
      cluster.x-k8s.io/v1beta1: v1beta1_v1beta2
    ```

1. The `ClusterTemplate` resource has dedicated fields to set an exact compatible Kubernetes version
in the Semantic Version format and required contract versions per each provider to match against
the related `ProviderTemplate` objects.
Given compatibility attributes will be then set accordingly in the `.status` field.
Compatibility contract versions are key-value pairs, where the key is **the name of the provider**,
and the value is the provider contract version required to be supported by the provider.

    Example with the `.spec`:

    ```yaml
    apiVersion: k0rdent.mirantis.com/v1beta1
    kind: ClusterTemplate
    # ...
    spec:
      k8sVersion: 1.30.0 # only exact semantic version is applicable
      providers:
      - bootstrap-k0sproject-k0smotron
      - control-plane-k0sproject-k0smotron
      - infrastructure-aws
      providerContracts:
        bootstrap-k0sproject-k0smotron: v1beta1 # only a single contract version is applicable
        control-plane-k0sproject-k0smotron: v1beta1
        infrastructure-aws: v1beta2
    ```

    Example with the `.annotations` in the `Chart.yaml`:

    ```yaml
    annotations:
      cluster.x-k8s.io/provider: infrastructure-aws, control-plane-k0sproject-k0smotron, bootstrap-k0sproject-k0smotron
      cluster.x-k8s.io/bootstrap-k0sproject-k0smotron: v1beta1
      cluster.x-k8s.io/control-plane-k0sproject-k0smotron: v1beta1
      cluster.x-k8s.io/infrastructure-aws: v1beta2
      k0rdent.mirantis.com/k8s-version: 1.30.0
    ```

1. The `ServiceTemplate` resource has dedicated fields to set an compatibility constrained
Kubernetes version to match against the related `ClusterTemplate` objects.
Given compatibility values will be then set accordingly in the `.status` field.

    Example with the `.spec`:

    ```yaml
    apiVersion: k0rdent.mirantis.com/v1beta1
    kind: ServiceTemplate
    # ...
    spec:
      k8sConstraint: "^1.30.0" # only semantic version constraints are applicable
    ```

    Example with the `annotations` in the `Chart.yaml`:

    ```yaml
    k0rdent.mirantis.com/k8s-version-constraint: ^1.30.0
    ```

### Compatibility attributes enforcement

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
