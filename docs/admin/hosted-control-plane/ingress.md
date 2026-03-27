# Ingress Support for Hosted Control Planes

> NOTE:
>
> **Supported k0s Versions:** `v1.34.1+k0s.0` and later.

{{{ docsVersionInfo.k0rdentName }}} enables deployment of hosted control plane clusters with the API server and konnectivity
exposed via an ingress controller. This allows cluster access through hostnames instead of direct service endpoints,
reducing the number of required load balancers.

k0smotron automatically creates an `Ingress` resource that routes traffic to the control plane service. Each worker
node runs a local HAProxy sidecar, which proxies pod traffic to the ingress controller. The kubelet connects
directly to the ingress controller for control plane communication, while pods use the HAProxy sidecar.

## Prerequisites

1. An ingress controller deployed on a cluster where hosted control plane components run. The ingress controller must
   support SSL passthrough such as HAProxy, NGINX, or Traefik.

    > NOTE: When deploying a cluster, make sure to use the correct SSL passthrough annotation for your ingress controller implementation. For example, HAProxy Ingress (community) requires `haproxy-ingress.github.io/ssl-passthrough: "true"`.

1. A `ClusterTemplate` referenced by the `ClusterDeployment`, which uses a Helm chart configured to set the
   `K0smotronControlPlane` `spec.ingress` field appropriately. 
1. DNS must be properly configured in both the cluster hosting control plane components and the child cluster.
   API server and konnectivity hostnames should resolve to the ingress controller's external IP address. Alternatively,
   use a DNS service like sslip.io or nip.io (e.g., `api.<cluster-name>.<ingress-ip>.nip.io` and
   `konnectivity.<cluster-name>.<ingress-ip>.nip.io`) that automatically resolves the hostnames to the IP address
   embedded in the hostname.

> WARNING:
> When deploying a hosted control plane cluster with ingress enabled and using `--cloud-provider=external` in kubelet
> args, the CCM must be configured with the correct API host and port to use the ingress API hostname directly for
> in-cluster config, instead of the default Kubernetes Service address. See the
> [troubleshooting section](#clusterdeployment-stuck-waiting-for-worker-nodes-to-become-ready-when-ingress-is-enabled)
> below for details.

## ClusterTemplate and Helm Chart Configuration

In {{{ docsVersionInfo.k0rdentName }}}, ingress support is enabled in the default `openstack-hosted-cp` `ClusterTemplate`. 
When using this `ClusterTemplate`, you can enable ingress for your OpenStack hosted control plane
cluster by setting the following parameters in the `ClusterDeployment`:

```yaml
spec:
  config:
    k0smotron:
      service:
        type: ClusterIP
    ingress:
      enabled: true
      className: "haproxy"
      apiHost: api.test-cluster.example.com
      konnectivityHost: konnectivity.test-cluster.example.com
      port: 443
```

> NOTE:
> By default, the `openstack-hosted-cp` `ClusterTemplate` is configured to pass the `haproxy.org/ssl-passthrough: "true"`
> annotation to the `K0smotronControlPlane``spec.ingress.annotations` field. If you're using a different ingress
> controller, make sure to set the correct SSL passthrough annotation.

When using a custom `ClusterTemplate`, ensure that the `K0smotronControlPlane` `spec.ingress` field is properly configured
in the Helm chart. The `K0smotronControlPlane` `spec.ingress` field includes:

* `apiHost`: Hostname for the Kubernetes API (for example, `kube-api.example.com`). Required when ingress is enabled.
* `konnectivityHost`: Hostname for the konnectivity server (for example, `konnectivity.example.com`). Required when ingress is enabled.
* `annotations`: Additional annotations for the ingress controller service. Must include the SSL passthrough annotation.
* `className`: The ingress class name used by the ingress controller (for example, `haproxy`).
* `deploy`: Whether to deploy an ingress resource for the cluster or let the user do it manually. Defaults to `true`.
* `port`: Port used by the ingress controller. Defaults to `443`.

The Helm chart must be adapted to consume `ingress` values to properly configure the `K0smotronControlPlane` object. See the examples below.

### Example: K0smotronControlPlane `spec.ingress` Configuration

```yaml
apiVersion: controlplane.cluster.x-k8s.io/v1beta1
kind: K0smotronControlPlane
metadata:
  name: {{ include "k0smotroncontrolplane.name" . }}
spec:
  {{- if and .Values.ingress.enabled .Values.ingress.apiHost .Values.ingress.konnectivityHost }}
  ingress:
    deploy: true
    className: {{ .Values.ingress.className }}
    {{- with .Values.ingress.annotations }}
    annotations:
      {{- toYaml . | nindent 6 }}
    {{- end }}
    port: {{ .Values.ingress.port }}
    apiHost: {{ .Values.ingress.apiHost }}
    konnectivityHost: {{ .Values.ingress.konnectivityHost }}
  {{- end }}
  ...
```

### Example: ClusterTemplate `ingress` Configuration in values.yaml

```yaml
ingress:
  enabled: false
  className: "haproxy"
  apiHost: ""
  konnectivityHost: ""
  port: 443
  annotations: {}
```

> NOTE:
> The parameter names in `values.yaml` are not significant, but the values must be correctly mapped to the corresponding
> fields in the `K0smotronControlPlane` `spec.ingress`.

## Example: Hosted ClusterDeployment Configuration with Ingress Enabled

This example assumes the referenced `ClusterTemplate` is configured to set the `K0smotronControlPlane`
`spec.ingress` field based on values provided in the `ClusterDeployment` `spec.config.ingress` field. Ensure your `ClusterTemplate` is configured accordingly.

When using an ingress controller with SSL passthrough enabled via annotation, make sure to set the correct SSL passthrough annotation for your controller in the `spec.config.ingress.annotations` field.

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ClusterDeployment
metadata:
  name: test-cluster
  namespace: kcm-system
spec:
  template: custom-hosted-cp-1-0-22
  credential: test-credential
  config:
    ingress:
      enabled: true
      className: "haproxy"
      apiHost: api.test-cluster.172.96.1.2.nip.io
      konnectivityHost: konnectivity.test-cluster.172.96.1.2.nip.io
      port: 443
      annotations:
        haproxy-ingress.github.io/ssl-passthrough: "true"
```

## Troubleshooting

### ClusterDeployment Stuck Waiting for Worker Nodes to Become Ready When Ingress Is Enabled

When deploying a hosted control plane cluster with ingress enabled and using the external cloud provider in kubelet
args, the `ClusterDeployment` may get stuck waiting for the worker nodes to become ready.

The ingress architecture uses a local HAProxy sidecar on each worker to proxy pod-to-API traffic. However, with
`--cloud-provider=external`, a deadlock can occur: the HAProxy sidecar cannot be configured until the CCM reports
worker node addresses, but the CCM cannot reach the API server because the HAProxy is not yet set up.

#### Workaround

Override the in-cluster config used by the CCM by explicitly setting `KUBERNETES_SERVICE_HOST` and `KUBERNETES_SERVICE_PORT`
in the CCM pod spec, pointing directly to the ingress hostname:

```
env:
- name: KUBERNETES_SERVICE_HOST
  value: "api.test-cluster.example.com"
- name: KUBERNETES_SERVICE_PORT
  value: "443"
```

This can be done either by modifying the CCM deployment directly after the API server becomes reachable or,
if the CCM configuration is managed by the helm chart, by setting these env vars in the CCM helm chart values.

> NOTE:
> When using the default `openstack-hosted-cp` `ClusterTemplate`, the workaround is already implemented in the CCM helm
> chart, and the env vars will be automatically set when ingress is enabled in the ClusterDeployment.

See details:

* [Cloud Controller Manager fails to start with `--cloud-provider=external` when using Ingress support](https://docs.k0smotron.io/head/troubleshooting/#cloud-controller-manager-fails-to-start-with-cloud-providerexternal-when-using-ingress-support)
* [GitHub issue](https://github.com/k0sproject/k0smotron/issues/1396)
