# Regional Cluster Registration

> NOTE:
> Regional clusters are available starting from version 1.4.0.

To register an existing Kubernetes cluster as a regional cluster in {{{ docsVersionInfo.k0rdentName }}}, you must create
a `Region` object. There are two ways to register a regional cluster:

* By providing a kubeconfig `Secret` in the system namespace
* By referencing an existing `ClusterDeployment` to onboard it as a regional cluster

> WARNING:
> The name of the `Region` object must not exceed 21 characters.

## Region Object with a Kubeconfig Secret Reference

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: Region
metadata:
  name: region1
spec:
  kubeConfig:
    name: kubeconfig-secret-name
    key: value
  providers:
  - name: cluster-api-provider-k0sproject-k0smotron
  - name: cluster-api-provider-openstack
  - name: projectsveltos
```

## Region Object with a ClusterDeployment Reference

> NOTE:
> Regional clusters registered by referencing a `ClusterDeployment` are available starting from version 1.5.0.

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: Region
metadata:
  name: region1
spec:
  clusterDeployment:
    name: regional-cluster
    namespace: test
  providers:
  - name: cluster-api-provider-k0sproject-k0smotron
  - name: cluster-api-provider-aws
  - name: projectsveltos
```

## Configuration Parameters

Use the `spec` to configure the `Region` object. For example:

* `spec.kubeConfig`

This field contains a reference to the `Secret` containing the kubeconfig of the cluster being onboarded as a regional
cluster. This `Secret` must reside in the system namespace (default: `kcm-system`). The field must specify both the `name`
of the `Secret` and the `key` where the kubeconfig content is stored within that `Secret`.
This field is mutually exclusive with `spec.clusterDeployment`.

* `spec.clusterDeployment`

Specifies a reference to an existing ClusterDeployment object to be onboarded as a regional cluster. This field must
include both the `name` and the `namespace` of the ClusterDeployment object.
This field is mutually exclusive with `spec.kubeConfig`.

* `spec.core`

The core KCM and CAPI configuration. Allows modification of regional components (CAPI, Cluster API Operator, Velero,
Cert Manager). This field is optional; if unspecified, {{{ docsVersionInfo.k0rdentName }}} will apply the defaults.

* `spec.providers`

This field includes a list of enabled providers to deploy on the regional cluster.

You can use this field to override the configuration (`config`) or template (`template`) of the core regional components or
providers. Example:

```yaml
spec:
  core:
    kcm:
      config:
        key1: value1
    capi:
      config:
        key1: value1
  providers:
  - name: <provider-name>
    config:
      key1: value1
    template: <provider-template-name>
```

## Overriding Core Values with Regional Components: Image Overrides

You can change the images CAPI uses for various functions by specifying the `spec.core.kcm.config` field. For example:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: Region
metadata:
  name: region2
spec:
  core:
    kcm:
      config:
        cert-manager:
          cainjector:
            image:
              repository: custom-registry-url.com/jetstack/cert-manager-cainjector
          image:
            repository: custom-registry-url.com/jetstack/cert-manager-controller
          startupapicheck:
            image:
              repository: custom-registry-url.com/jetstack/cert-manager-startupapicheck
          webhook:
            image:
              repository: custom-registry-url.com/jetstack/cert-manager-webhook
        cluster-api-operator:
          image:
            manager:
              repository: custom-registry-url.com/capi-operator/cluster-api-operator
        velero:
          image:
            repository: custom-registry-url.com/velero/velero
  kubeConfig:
    name: kubeconfig-secret-name
    key: value
  providers:
  - name: cluster-api-provider-k0sproject-k0smotron
  - name: cluster-api-provider-aws
  - name: cluster-api-provider-azure
  - name: projectsveltos
```

## After the Region is Created

Once you create the `Region` object within the management cluster:

* The regional core components and enabled providers start installing on the regional cluster automatically.
* You can monitor the Region's status and readiness using `kubectl wait`. For example:

```bash
kubectl wait --for=condition=Ready=True region/<region-name>
```

Once the `Region` is ready, you can start creating `Credentials` and deploy clusters in that region. For more infromation, see:
[Creating Credential in Region](creating-credential-in-region.md).
