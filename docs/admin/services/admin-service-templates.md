# Using and Creating ServiceTemplates: Creating and Deploying Applications

Deploying an application, like deploying a cluster, involves applying a template to the management cluster. Rather than a `ClusterTemplate`, however, applications are deployed using a `ServiceTemplate`.

You can find more information on [Bringing Your Own Templates](../../reference/template/template-byo.md)
in the Template Guide, but this section gives you an idea of how to create a `ServiceTemplate`
and use it to deploy an application to a {{{ docsVersionInfo.k0rdentName }}} child cluster.

`ServiceTemplate` supports the following types as a source:

- [`HelmChart`](https://fluxcd.io/flux/components/source/helmcharts/)
- [`GitRepository`](https://fluxcd.io/flux/components/source/gitrepositories/)
- [`Bucket`](https://fluxcd.io/flux/components/source/buckets/)
- [`OCIRepository`](https://fluxcd.io/flux/components/source/ocirepositories/)
- `Secret`
- `ConfigMap`

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
  insecure: true
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
           path: "./ingress-nginx"
   ```

   In this case, we're creating a `ServiceTemplate` called `ingress-nginx-4.11.3` in the
   `my-target-namespace` namespace.  It defines the source of the Helm chart located in the
   `s3://bucket/path/to/charts` bucket and path where the Helm chart is located within the bucket.

For more information on creating templates, see the [Template Guide](../../reference/template/index.md).

### Creating Kustomization-based ServiceTemplate

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
    path: "./base"
```

Aside from flux sources, local `ConfigMap` or `Secret` object can be used as a source of the kustomization manifests. The `ServiceTemplate` definition will not differ
from one in above, except the `.spec.kustomize.localSourceRef.kind` which should be set to respective object type. However, to use `ConfigMap` or `Secret` as a source, they must
embed archive with kustomization. After the archive was created, this can be done by executing the following command:

```shell
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

```shell
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
    path: ""  # will be ignored
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

 ```shell
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

 ```shell
 kubectl patch clusterdeployment my-cluster-deployment -n my-target-namespace --type='merge' -p '{"spec":{"serviceSpec":{"services":[{"template":"project-ingress-nginx-4.11.3","name":"ingress-nginx","namespace":"my-target-namespace"}]}}}'
 ```
For more information on creating and using `ServiceTemplate` objects, see the [User Guide](../../user/services/index.md).
