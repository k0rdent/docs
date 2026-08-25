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

#### Helm-based Chart Spec ServiceTemplate

- by defining Helm chart right in the template object, referring the existing Helm repository

  ```yaml
  apiVersion: k0rdent.mirantis.com/v1beta1
  kind: ServiceTemplate
  metadata:
    name: traefik-41-3-0
    namespace: kcm-system
  spec:
    helm:
      chartSpec:
        chart: traefik
        version: 41.3.0
        interval: 10m
        sourceRef:
          kind: HelmRepository
          name: traefik-repo
  ```

  In this case the corresponding `HelmChart` object will be created by the controller.

#### Helm-based Chart Ref ServiceTemplate

- by referring the existing Helm chart

  ```yaml
  apiVersion: k0rdent.mirantis.com/v1beta1
  kind: ServiceTemplate
  metadata:
    name: traefik-41-3-0
    namespace: kcm-system
  spec:
    helm:
      chartRef:
        kind: HelmChart
        name: traefik-41-3-0
  ```

#### Helm-based Local Source ServiceTemplate

- by defining Helm chart source, which can be one of types provided by FluxCD:

  - [HelmRepository](https://fluxcd.io/flux/components/source/helmrepositories/)
  - [GitRepository](https://fluxcd.io/flux/components/source/gitrepositories/)
  - [Bucket](https://fluxcd.io/flux/components/source/buckets/)

  Source can already exist or can be created by the controller.

  ```yaml
  apiVersion: k0rdent.mirantis.com/v1beta1
  kind: ServiceTemplate
  metadata:
    name: traefik-41-3-0
    namespace: kcm-system
  spec:
    helm:
      chartSource:
        path: ./traefik
        localSourceRef:
          kind: GitRepository
          name: traefik-repository
  ```

#### Helm-based Remote Source ServiceTemplate

  ```yaml
  apiVersion: k0rdent.mirantis.com/v1beta1
  kind: ServiceTemplate
  metadata:
    name: traefik-41-3-0
    namespace: kcm-system
  spec:
    helm:
      chartSource:
        path: ./traefik
        remoteSourceSpec:
          git:
            url: https://github.com/traefik/traefik-helm-chart
            ref:
              tag: v41.3.0
            interval: 10m
  ```

### Kustomize-based ServiceTemplate

Kustomize-based `ServiceTemplate` can be created with either local or remote source:

#### Kustomize-based Local Source ServiceTemplate

- by using existing flux source object - `GitRepository`, `Bucket` or `OCIRepository` - or using existing `ConfigMap` or `Secret`

  ```yaml
  apiVersion: k0rdent.mirantis.com/v1beta1
  kind: ServiceTemplate
  metadata:
    name: traefik-41-3-0
    namespace: kcm-system
  spec:
    kustomize:
      path: ./traefik
      deploymentType: Remote
      localSourceRef:
        kind: GitRepository  # also can be Bucket, OCIRepository, ConfigMap or Secret
        name: traefik-repo
  ```

  `ConfigMap` or `Secret` in this case must embed the tar-gzipped archive containing the kustomization files. This can be done by the following command, assuming the the archive was already created:

  ```bash
  kubectl create configmap foo-bar --from-file=/path/to/kustomization/archive.tar.gz
  ```

#### Kustomize-based Remote Source ServiceTemplate

- by defining remote source right in the template object

  ```yaml
  apiVersion: k0rdent.mirantis.com/v1beta1
  kind: ServiceTemplate
  metadata:
    name: traefik-41-3-0
    namespace: kcm-system
  spec:
    kustomize:
      path: ./traefik
      deploymentType: Remote
      remoteSourceSpec:
        oci:
          url: oci://ghcr.io/traefik/helm/traefik
          ref:
            tag: 41.3.0
          interval: 10m
          layerSelector:
            mediaType: application/vnd.cncf.helm.chart.content.v1.tar+gzip
  ```

  `.spec.kustomize.remoteSourceSpec` has mutual exclusive fields `.git`, `.bucket` and `.oci` which inline `GitRepositorySpec`, `BucketSpec` and `OCIRepositorySpec` respectively.

### Raw-resources-based ServiceTemplate

Similar to kustomize-based `ServiceTemplate`, raw-resources-based `ServiceTemplate` can be created with either local or remote source. Using the remote source has no difference with
kustomize-based `ServiceTemplate`, however using local source slightly differ in case `ConfigMap` or `Secret` object is referred as a source:

- `spec.resources.localSourceRef.path` will be ignored
- referred `ConfigMap` or `Secret` must contain inlined resources' definitions instead of embedding tar-gzipped archive.
