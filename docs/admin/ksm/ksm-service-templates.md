# Using and Creating ServiceTemplates: Creating and Deploying Applications

Deploying an application, like deploying a cluster, involves applying a template to the management cluster. Rather than a `ClusterTemplate`, however, applications are deployed using a `ServiceTemplate`.

You can find more information on [Bringing Your Own Templates](../../reference/template/template-byo.md)
in the Template Guide, but this section gives you an idea of how to create a `ServiceTemplate`
and use it to deploy an application to a {{{ docsVersionInfo.k0rdentName }}} child cluster.

> WARNING:
> `ServiceTemplate` spec is **immutable** once created. You cannot modify the spec fields after the template is created. To make changes, you must create a new `ServiceTemplate` object with a different name.

`ServiceTemplate` supports the following types as a source:

- [`HelmChart`](https://fluxcd.io/flux/components/source/helmcharts/)
- [`GitRepository`](https://fluxcd.io/flux/components/source/gitrepositories/)
- [`Bucket`](https://fluxcd.io/flux/components/source/buckets/)
- [`OCIRepository`](https://fluxcd.io/flux/components/source/ocirepositories/)
- `Secret`
- `ConfigMap`

## Path Field Behavior

> NOTE:
> The `path` field in `.spec.helm.chartSource`, `.spec.kustomize`, and `.spec.resources` is **optional**.
>
> - If `path` is not specified, the root of the source artifact is used.
> - When using `ConfigMap` or `Secret` with `resources`, the `path` field is ignored.

### Creating Helm-based ServiceTemplate

Before creating a `ServiceTemplate`, the source of the Helm chart that represents the service can be created. The source object must have the label `k0rdent.mirantis.com/managed: "true"`. For example, this YAML describes a FluxCD source object of `kind` `HelmRepository`:

```yaml
apiVersion: source.toolkit.fluxcd.io/v1
kind: HelmRepository
metadata:
  name: custom-templates-repo
  namespace: kcm-system
  labels:
    k0rdent.mirantis.com/managed: "true"
spec:
  interval: 10m0s
  provider: generic
  type: oci
  url: oci://ghcr.io/external-templates-repo/charts
```

#### Create the `ServiceTemplate`

Helm-based `ServiceTemplate` can be created in three ways:

- by defining Helm chart right in the template object
- by referring the existing Helm chart
- by defining or referring source provided by FluxCD

> NOTE:
> `ServiceTemplate` can be defined using `.spec.helm.chartSpec` or `.spec.helm.chartRef` if only Helm chart being defined or referred is backed by `HelmRepository` or `GitRepository` object.
> To use FluxCD sources, `ServiceTemplate` must be defined using `.spec.helm.chartSource` field.

FluxCD sources supported by `ServiceTemplate` are:

- [`GitRepository`](https://fluxcd.io/flux/components/source/gitrepositories/)
- [`Bucket`](https://fluxcd.io/flux/components/source/buckets/)
- [`OCIRepository`](https://fluxcd.io/flux/components/source/ocirepositories/)

##### Examples

1. Explicitly defining Helm chart

   ```yaml
   apiVersion: k0rdent.mirantis.com/v1beta1
   kind: ServiceTemplate
   metadata:
     name: project-ingress-nginx-4.11.3
     namespace: my-target-namespace
   spec:
     helm:
       chartSpec:
         chart: ingress-nginx
         version: 4.11.3
         interval: 10m0s
         sourceRef:
           kind: HelmRepository
           name: k0rdent-catalog
   ```

   In this case, we're creating a `ServiceTemplate` called `ingress-nginx-4.11.3` in the
   `my-target-namespace` namespace.  It references version 4.11.3 of the `ingress-nginx` chart
   located in the `k0rdent-catalog` Helm repository. The `HelmChart` object will be created by the controller.

2. Referring the existing Helm chart

   ```yaml
   apiVersion: k0rdent.mirantis.com/v1beta1
   kind: ServiceTemplate
   metadata:
     name: project-ingress-nginx-4.11.3
     namespace: my-target-namespace
   spec:
     helm:
       chartRef:
         kind: HelmChart
         name: ingress-nginx-4.11.3
   ```

   In this case, we're creating a `ServiceTemplate` called `ingress-nginx-4.11.3` in the
   `my-target-namespace` namespace.  It references the existing `ingress-nginx-4.11.3` Helm chart.

3. Referring existing FluxCD source

   ```yaml
   apiVersion: k0rdent.mirantis.com/v1beta1
   kind: ServiceTemplate
   metadata:
     name: project-ingress-nginx-4.11.3
     namespace: my-target-namespace
   spec:
     helm:
       chartSource:
         localSourceRef:
           kind: GitRepository
           name: k0rdent-catalog
         # path is optional; defaults to artifact root if omitted
         path: "./charts/ingress-nginx"
   ```

   In this case, we're creating a `ServiceTemplate` called `ingress-nginx-4.11.3` in the
   `my-target-namespace` namespace.  It references the existing `GitRepository` object called
   `k0rdent-catalog` and the Helm chart located in the `charts/ingress-nginx` path.

4. Defining Helm chart source, which can be one of types provided by FluxCD:

   ```yaml
   apiVersion: k0rdent.mirantis.com/v1beta1
   kind: ServiceTemplate
   metadata:
     name: project-ingress-nginx-4.11.3
     namespace: my-target-namespace
   spec:
     helm:
       chartSource:
         remoteSourceSpec:
           bucket:
             url: s3://bucket/path/to/charts
             interval: 10m0s
           # path is optional; defaults to artifact root if omitted
           path: "./ingress-nginx"
   ```

   In this case, we're creating a `ServiceTemplate` called `ingress-nginx-4.11.3` in the
   `my-target-namespace` namespace.  It defines the source of the Helm chart located in the
   `s3://bucket/path/to/charts` bucket and path where the Helm chart is located within the bucket.

For more information on creating templates, see the [Template Guide](../../reference/template/index.md).

## ServiceTemplate Specification Fields

### Core Fields

#### `.spec.version`
Semantic version of the application backed by the template. This field helps track which application version is deployed.

Example:
```yaml
spec:
  version: "4.11.3"
```

#### `.spec.k8sConstraint`
Kubernetes version constraint in SemVer format describing compatible K8s versions for the target cluster.

Example:
```yaml
spec:
  k8sConstraint: ">=1.28.0 <1.32.0"
```

#### `.spec.helmOptions`
Global Helm options applied when installing or updating the Helm chart. These options control the behavior of Helm operations.

Available options:

- `enableClientCache` (bool): Enable Helm client cache for improved performance
- `dependencyUpdate` (bool): Update chart dependencies if missing before installation
- `wait` (bool): Wait until all resources are in ready state before marking release as successful
- `waitForJobs` (bool): If set and `wait` is enabled, will wait until all Jobs have completed
- `skipCRDs` (bool): Skip installation of CRDs during install/upgrade operations
- `atomic` (bool): If set, the installation process rolls back on failure (automatically sets `wait: true`)
- `disableHooks` (bool): Prevent hooks from running during install/upgrade/uninstall
- `disableOpenAPIValidation` (bool): Skip validation of rendered templates against Kubernetes OpenAPI Schema
- `timeout` (duration): Time to wait for any individual Kubernetes operation (e.g., "5m", "300s")
- `skipSchemaValidation` (bool): Disable JSON schema validation
- `labels` (map[string]string): Labels that would be added to release metadata
- `description` (string): Description of the Helm operation
- `installOptions` (object): Options specific to helm install. See [Install Options](#install-options) below.

> **Deprecated fields** (still accepted but prefer `installOptions.*`):
> - `createNamespace` (bool) — use `installOptions.createNamespace` instead
> - `replace` (bool) — use `installOptions.replace` instead

#### Install Options

`helmOptions.installOptions` controls helm install-specific behavior. All fields default to `false` when unset.

- `createNamespace` (bool): Create the release namespace if it doesn't exist. Defaults to `true`.
- `replace` (bool): Replace an older release with this one if it exists. Defaults to `true`.
- `disableHooks` (bool): Prevent hooks from running during install (overrides the top-level `disableHooks` for installs only). Defaults to `false`.
- `takeOwnership` (bool): Ignore helm annotations and take ownership of existing resources. Defaults to `false`.

Example:
```yaml
spec:
  helmOptions:
    wait: true
    waitForJobs: true
    timeout: 10m
    atomic: true
    labels:
      environment: production
      team: platform
    installOptions:
      createNamespace: true
```

> NOTE:
> These global options can be overridden at the service level when deploying using `.spec.serviceSpec.services[].helmOptions`.

### Validation Rules

The following validation rules apply to `ServiceTemplate`:

1. **Mutually Exclusive Source Types**: Only one of `helm`, `kustomize`, or `resources` can be specified.
2. **Required Source**: At least one of `helm`, `kustomize`, or `resources` must be specified.
3. **LocalSourceRef vs RemoteSourceSpec**: When using `helm.chartSource`, `kustomize` or `resources`, only one of `localSourceRef` or `remoteSourceSpec` can be set.
4. **Helm Chart Sources**: When using Helm, only one of `chartSpec`, `chartRef`, or `chartSource` can be specified.
5. **ConfigMap/Secret Limitations**: `ConfigMap` and `Secret` sources are **only** supported for `kustomize` and `resources` templates, not for Helm charts.
6. **Path Field**: `path` is optional for all supported source types.

### Cross-Namespace References

When using `.spec.kustomize.localSourceRef` or `.spec.resources.localSourceRef`:

- **FluxCD Sources** (GitRepository, Bucket, OCIRepository): Cross-namespace references are allowed. You can reference sources in different namespaces.
- **ConfigMap/Secret**: Cross-namespace references are **not allowed**. The namespace field will be ignored, and the source must exist in the same namespace as the ServiceTemplate.

Example of cross-namespace reference:
```yaml
spec:
  kustomize:
    localSourceRef:
      kind: GitRepository
      name: my-git-repo
      namespace: flux-system  # Different namespace is OK
    # path is optional; defaults to repository root
    path: "./base"
```

### Remote Source Object Creation

When using `.spec.helm.chartSource.remoteSourceSpec`, `.spec.kustomize.remoteSourceSpec`, or `.spec.resources.remoteSourceSpec`, the controller automatically creates corresponding FluxCD source objects (GitRepository, Bucket, or OCIRepository).

These created objects will have:
- The label `k0rdent.mirantis.com/managed: "true"`
- Controller reference pointing to the ServiceTemplate
- Automatic lifecycle management (deleted when ServiceTemplate is deleted)

You can verify created sources with:
```bash
kubectl get gitrepositories,buckets,ocirepositories -A -l k0rdent.mirantis.com/managed=true
```

## ServiceTemplate Status

The `.status` field of a ServiceTemplate contains information about the template's validity and source status.

### Status Fields

#### `.status.valid`
Boolean indicating whether the template is valid and ready to use.

#### `.status.validationError`
Contains error details if the template validation failed.

#### `.status.k8sConstraint`
Reflects the Kubernetes version constraint from the spec.

#### `.status.sourceStatus`
Provides detailed information about the source backing the template if applicable:

- `kind`: Kind of the source (e.g., GitRepository, HelmChart, Bucket)
- `name`: Name of the source object
- `namespace`: Namespace of the source object
- `artifact`: Information about the fetched artifact
  - `digest`: The digest of the file in the form of '<algorithm>:<checksum>'
  - `path`: The relative file path of the Artifact
  - `url`: URL where the artifact can be accessed
  - `revision`: Revision/version of the artifact
  - `lastUpdateTime`: The timestamp corresponding to the last update of the artifact
  - `size`: The number of bytes in the file
  - `metadata`: Holds upstream information such as OCI annotations
- `conditions`: Array of conditions from the source object
- `observedGeneration`: Latest generation observed by the source controller

#### `.status.config`
Contains all possible values. Applicable only to `ServiceTemplate` objects based on Helm charts.

#### `.status.chartRef`
Contains cross-namespace reference to Helm chart object. Applicable only to `ServiceTemplate` objects based on Helm charts.

- `apiVersion`: API version of the source object
- `kind`: Kind of the source object
- `name`: Name of the source object
- `namespace`: Namespace of the source object

Example status:
```yaml
status:
  valid: true
  k8sConstraint: ">=1.28.0"
  sourceStatus:
    kind: GitRepository
    name: my-app-source
    namespace: kcm-system
    artifact:
      url: http://source-controller/gitrepository/kcm-system/my-app-source/abc123.tar.gz
      revision: main@sha1:abc123def456
    conditions:
    - type: Ready
      status: "True"
      reason: Succeeded
    observedGeneration: 1
```

### Monitoring Template Status

You can use `kubectl get servicetemplate` to see template status:

```bash
kubectl get servicetemplate -A
```

The output includes columns:
- `VALID`: Whether the template is valid (true/false)
- `VALIDATIONERROR`: Brief error message if validation failed
- `DESCRIPTION`: Template description

### Troubleshooting Invalid Templates

If a template shows `VALID=false`:

1. Check the `validationError` in status:
   ```bash
   kubectl get servicetemplate <name> -n <namespace> -o jsonpath='{.status.validationError}'
   ```

2. Check source object status if using remote sources:
   ```bash
   kubectl get gitrepository,helmchart,bucket,ocirepository -n <namespace>
   ```

3. Verify source conditions:
   ```bash
   kubectl describe servicetemplate <name> -n <namespace>
   ```

Common validation errors:
- Source object not found or not ready
- Invalid Helm chart reference
- Network issues fetching remote sources
- Kubernetes version constraint parsing errors

### Creating Kustomization-based ServiceTemplate

#### Deployment Type

The `deploymentType` field (enum: `Local` or `Remote`, default: `Remote`) controls where resources are applied:

- **`Remote`**: The management cluster pushes resources to the target workload cluster. This is the standard mode.
- **`Local`**: The workload cluster itself pulls and applies the resources. Use this when the management cluster does not have direct API access to the workload cluster.

> NOTE:
> The `deploymentType` field is **ignored** when `resources` is used as part of a Helm chart configuration (i.e., when `.spec.resources` is combined with `.spec.helm`). It only applies to standalone `kustomize` and `resources` templates.

Define the source of the Kustomization that defines the service. If the source object is one of Flux source - `GitRepository`, `Bucket` or `OCIRepository` - it must
have the label `k0rdent.mirantis.com/managed: "true"`.

Source object can be already created. In this case `.spec.kustomization.localSourceRef` should be used:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ServiceTemplate
metadata:
  name: kustomization-app
  namespace: kcm-system
spec:
  kustomize:
    localSourceRef:
      kind: GitRepository
      name: project-x
    deploymentType: Remote
    # path is optional
    path: "./base"
```

Aside from flux sources, local `ConfigMap` or `Secret` object can be used as a source of the kustomization manifests. The `ServiceTemplate` definition will not differ
from one in above, except the `.spec.kustomize.localSourceRef.kind` which should be set to respective object type. However, to use `ConfigMap` or `Secret` as a source, they must
embed archive with kustomization. After the archive was created, this can be done by executing the following command:

```bash
kubectl create configmap kustomization-source --from-file=/path/to/kustomization.tar.gz
```

Another option is to let the controller to create the remote source object. In this case `.spec.kustomization.remoteSourceSpec` should be used:

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
    # path is optional
    path: "./overlays"
```

When `.spec.kustomize.remoteSourceSpec` is defined, the controller will create corresponding object.

### Creating Raw-Resources-based ServiceTemplate

This type of source is quite similar to the kustomization sources, with the only exception:
when using `ConfigMap` or `Secret` as a source, the field `.spec.resources.localSourceRef.path` will be ignored
and the resources' manifests to be deployed must be inlined in the source's `data`.

Example of the `ConfigMap` and corresponding `ServiceTemplate`:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: project-cm
  namespace: project-x
data:
  namespace.yaml: |
    apiVersion: v1
    kind: Namespace
    metadata:
      name: managed-ns
```

To create such `ConfigMap` the following command can be used:

```bash
kubectl --namespace project-x create configmap project-cm --from-file=/path/to/namespace.yaml
```

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ServiceTemplate
metadata:
  name: managed-ns
  namespace: project-x
spec:
  resources:
    localSourceRef:
      kind: ConfigMap
      name: project-cm
    deploymentType: Remote
```

Using the remote source for `ServiceTemplate` based on raw resources is similar to the kustomization-based template:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ServiceTemplate
metadata:
  name: kustomization-app
  namespace: kcm-system
spec:
  resources:
    remoteSourceSpec:
      git:
        url: https://github.com/org/project-x.git
        reference:
          branch: main
        interval: 10m
    deploymentType: Remote
    # path is optional
    path: "./overlays"
```

### Deploying Application with ServiceTemplate

#### Create a `ServiceTemplateChain`

To let {{{ docsVersionInfo.k0rdentName }}} know where this `ServiceTemplate` can and can't be used, create a `ServiceTemplateChain` object, as in:

 ```yaml
 apiVersion: k0rdent.mirantis.com/v1beta1
 kind: ServiceTemplateChain
 metadata:
   name: project-ingress-nginx-4.11.3
   namespace: my-target-namespace
 spec:
   supportedTemplates:
     - name: project-ingress-nginx-4.11.3
     - name: project-ingress-nginx-4.10.0
       availableUpgrades:
         - name: project-ingress-nginx-4.11.3
 ```

Here you see a template called `project-ingress-nginx-4.11.3` that is meant to be deployed in the `my-target-namespace` namespace.
The `.spec.helm.chartSpec` specifies the name of the Helm chart and where to find it, as well as the version and other
important information. The `ServiceTempateChain` shows that this template is also an upgrade path from version 4.10.0.

If you wanted to deploy this as an application, you would first go ahead and add it to the cluster in which you were
working, so if you were to save this YAML to a file called `project-ingress.yaml` you could run this command on the management cluster:

 ```bash
 kubectl apply -f project-ingress.yaml -n my-target-namespace
 ```

#### Adding a `Service` to a `ClusterDeployment`

To add the service defined by this template to a cluster, you would simply add it to the `ClusterDeployment` object
when you create it, as in:

 ```yaml
 apiVersion: k0rdent.mirantis.com/v1beta1
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
       - template: project-ingress-nginx-4.11.3
         name: ingress-nginx
         namespace: my-target-namespace
     priority: 100
 ```
As you can see, you're simply referencing the template in the `.spec.serviceSpec.services[].template` field of the `ClusterDeployment`
to tell {{{ docsVersionInfo.k0rdentName }}} that you want this service to be part of this cluster.

If you wanted to add this service to an existing cluster, you would simply patch the definition of the `ClusterDeployment`, as in:

 ```bash
 kubectl patch clusterdeployment my-cluster-deployment -n my-target-namespace --type='merge' -p '{"spec":{"serviceSpec":{"services":[{"template":"project-ingress-nginx-4.11.3","name":"ingress-nginx","namespace":"my-target-namespace"}]}}}'
 ```
For more information on creating and using `ServiceTemplate` objects, see the [User Guide](../../user/services/index.md).
