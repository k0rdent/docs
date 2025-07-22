# Understanding ServiceTemplates

`ServiceTemplate` objects are a representation of the source where {{{ docsVersionInfo.k0rdentName }}} can find a resource or set of resources to
be deployed as a complete application.

`ServiceTemplate` supports the following types as a source:

- [`HelmChart`](https://fluxcd.io/flux/components/source/helmcharts/)
- [`GitRepository`](https://fluxcd.io/flux/components/source/gitrepositories/)
- [`Bucket`](https://fluxcd.io/flux/components/source/buckets/)
- [`OCIRepository`](https://fluxcd.io/flux/components/source/ocirepositories/)
- `Secret`
- `ConfigMap`

### Helm-based ServiceTemplate

> NOTE:
> `ServiceTemplate` can be defined using `.spec.helm.chartSpec` or `.spec.helm.chartRef` if only Helm chart being defined or referred is backed by `HelmRepository` or `GitRepository` object.

Helm-based `ServiceTemplate` can be created in three ways:

- by defining Helm chart right in the template object

  ```yaml
  apiVersion: k0rdent.mirantis.com/v1beta1
  kind: ServiceTemplate
  metadata:
    name: foo
    namespace: bar
  spec:
    helm:
      chartSpec:
        chart: ingress-nginx
        version: 4.11.0
        interval: 10m
        sourceRef:
          kind: HelmRepository
          name: foo-repository
  ```

  In this case the corresponding `HelmChart` object will be created by the controller.

- by referring the existing Helm chart

  ```yaml
  apiVersion: k0rdent.mirantis.com/v1beta1
  kind: ServiceTemplate
  metadata:
    name: foo
    namespace: bar
  spec:
    helm:
      chartRef:
        kind: HelmChart
        name: foo-chart
  ```

- by defining Helm chart source, which can be one of types provided by FluxCD:

  - [HelmRepository](https://fluxcd.io/flux/components/source/helmrepositories/)
  - [GitRepository](https://fluxcd.io/flux/components/source/gitrepositories/)
  - [Bucket](https://fluxcd.io/flux/components/source/buckets/)

  Source can already exist or can be created by the controller.

  ```yaml
  apiVersion: k0rdent.mirantis.com/v1beta1
  kind: ServiceTemplate
  metadata:
    name: foo
    namespace: bar
  spec:
    helm:
      chartSource:
        localSourceRef:
          kind: GitRepository
          name: foo-repository
        path: "./charts"
  ```

  ```yaml
  apiVersion: k0rdent.mirantis.com/v1beta1
  kind: ServiceTemplate
  metadata:
    name: foo
    namespace: bar
  spec:
    helm:
      chartSource:
        remoteSourceRef:
          git:
            url: https://github.com/bar/foo.git
            reference:
              branch: main
            interval: 10m
          path: "./charts"
  ```

### Kustomize-based ServiceTemplate

Kustomize-based `ServiceTemplate` can be created with either local or remote source:

- by using existing flux source object - `GitRepository`, `Bucket` or `OCIRepository` - or using existing `ConfigMap` or `Secret`

  ```yaml
  apiVersion: k0rdent.mirantis.com/v1beta1
  kind: ServiceTemplate
  metadata:
    name: foo
    namespace: bar
  spec:
    kustomize:
      localSourceRef:
        kind: Bucket  # also can be GitRepository, OCIRepository, ConfigMap or Secret
        name: foo-bar
      deploymentType: Remote
      path: "./base"
  ```

  `ConfigMap` or `Secret` in this case must embed the tar-gzipped archive containing the kustomization files. This can be done by the following command, assuming the the archive was already created:

  ```shell
  kubectl create configmap foo-bar --from-file=/path/to/kustomization/archive.tar.gz
  ```

- by defining remote source right in the template object

  ```yaml
  apiVersion: k0rdent.mirantis.com/v1beta1
  kind: ServiceTemplate
  metadata:
    name: kustomization-app
    namespace: kcm-system
  spec:
    kustomize:
      remoteSourceSpec:
        oci:
          url: oci://ghcr.io/org/project-x
          reference:
            tag: latest
          interval: 10m
      deploymentType: Remote
      path: "./overlays"
  ```

  `.spec.kustomize.remoteSourceSpec` has mutual exclusive fields `.git`, `.bucket` and `.oci` which inline `GitRepositorySpec`, `BucketSpec` and `OCIRepositorySpec` respectively.

### Raw-resources-based ServiceTemplate

Similar to kustomize-based `ServiceTemplate`, raw-resources-based `ServiceTemplate` can be created with either local or remote source. Using the remote source has no difference with
kustomize-based `ServiceTemplate`, however using local source slightly differ in case `ConfigMap` or `Secret` object is referred as a source:

- `spec.resources.localSourceRef.path` will be ignored
- referred `ConfigMap` or `Secret` must contain inlined resources' definitions instead of embedding tar-gzipped archive.
