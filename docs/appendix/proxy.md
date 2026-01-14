# Proxy Configuration Support

## Overview

k0rdent enables configuring HTTP/HTTPS proxy settings for all default
CAPI providers deployed by the `kcm`, using a **single Kubernetes Secret**.
The proxy configuration is propagated automatically from the `kcm` chart
to all underlying provider charts and to the `kcm-regional` chart
(see [Components segregation](../admin/regional-clusters/components-segregation.md)),
with fine-grained opt-in controls per chart.

The `kcm-regional` chart proxy configuration affects only the
[telemetry](./telemetry/index.md) collection.

The `kcm` controller itself **does not proxy any requests**, as all its
interactions are limited to the Kubernetes API and local cluster resources.

## High-Level Flow

1. The user creates a Kubernetes `Secret` in a system namespace containing
   proxy configuration.
1. The user installs `kcm` in the same namespace and references the
   `Secret` via `.Values.proxy.secretName`.
1. The deployed controller:
    1. Detects the proxy `Secret` via an environment variable.
    1. Propagates the proxy configuration to all underlying CAPI provider
       charts and to `kcm-regional`.
1. Each downstream chart decides whether to apply the proxy configuration based
   on its own enablement flags.

## User Workflow

1. Create a Proxy `Secret`.

    The user creates a `Secret` containing one or more of the following keys:

    * `HTTP_PROXY`
    * `HTTPS_PROXY`
    * `NO_PROXY`

    Example:

    ```yaml
    apiVersion: v1
    kind: Secret
    metadata:
      name: proxy-settings
      namespace: <system-namespace>
    type: Opaque
    stringData:
      HTTP_PROXY: http://proxy.example.com:8080
      HTTPS_PROXY: http://proxy.example.com:8443
      NO_PROXY: localhost,127.0.0.1,10.96.0.1
    ```

    All keys are optional; only the provided ones will be consumed.

1. Install `kcm` with the proxy `Secret` name given.

    ```bash
    helm install kcm {{{ extra.docsVersionInfo.ociRegistry }}} \
      --version <version> \
      --namespace <system-namespace> \
      --set proxy.secretName=proxy-settings
    ```

    This sets the `PROXY_SECRET` environment variable in the `Deployment`
    with the `kcm` controller.

## Controller Behavior

### Proxy Detection

If the `PROXY_SECRET` environment variable is present, the `kcm` controller
interprets this as an instruction to propagate proxy configuration to
downstream charts.

### Values Propagation

`kcm` injects the following values into:

* All default CAPI provider charts (including CAPI core)
* The `kcm-regional` chart

```yaml
global:
  proxy:
    secretName: <given-secret-name>
```

### Secret Propagation

The `Secret` object automatically propagates to all
of the existing [regional](../admin/regional-clusters/index.md) clusters.

> WARNING:
> When doing initial installation one limitation is applied to the
> `cluster-api-provider-openstack` ORC controller, which is installed in the
> `orc-system` namespace.
>
> To mitigate this you must either create the `orc-system` namespace and duplicate
> the `Secret` there manually or disable the provider in the `Management`
> object.

## CAPI Provider Charts

See: [Extended Management Configuration](./appendix-extend-mgmt.md#configuration-guide).

### Enablement Flag

Each CAPI provider chart exposes a local toggle:

```yaml
proxy:
  enabled: true
```

* Type: `boolean`
* Default: `true`

This allows selectively disabling proxy configuration for individual providers.

An example of the `Management` object disabling the proxy for the
`cluster-api-provider-aws`:

```yaml
spec:
  providers:
  - name: cluster-api-provider-aws
    config:
      proxy:
        enabled: false
```

### Environment Variable Injection

If the conditions below are met:

1. `.Values.global.proxy.secretName` is set
1. `.Values.proxy.enabled` is `true`

The provider's `Deployment` object is modified via either the
`InfrastructureProvider`, `BootstrapProvider`, `ControlPlaneProvider`,
or `CoreProvider` object to include standard proxy environment variables
sourced from the `Secret`:

```yaml
env:
  - name: HTTP_PROXY
    valueFrom:
      secretKeyRef:
        name: <secret-name>
        key: HTTP_PROXY
        optional: true
  - name: http_proxy
    valueFrom:
      secretKeyRef:
        name: <secret-name>
        key: HTTP_PROXY
        optional: true
  - name: HTTPS_PROXY
    valueFrom:
      secretKeyRef:
        name: <secret-name>
        key: HTTPS_PROXY
        optional: true
  - name: https_proxy
    valueFrom:
      secretKeyRef:
        name: <secret-name>
        key: HTTPS_PROXY
        optional: true
  - name: NO_PROXY
    valueFrom:
      secretKeyRef:
        name: <secret-name>
        key: NO_PROXY
        optional: true
  - name: no_proxy
    valueFrom:
      secretKeyRef:
        name: <secret-name>
        key: NO_PROXY
        optional: true
```

This ensures compatibility with applications that are case-sensitive when
reading proxy environment variables.

## `kcm-regional` Chart

See: [Extended Management Configuration](./appendix-extend-mgmt.md#configuring-telemetry).

### Enablement Flags

Proxy configuration for `kcm-regional` is controlled independently and is
scoped to telemetry functionality:

```yaml
telemetry:
  controller:
    proxy:
      enabled: true
```

An example of the `Management` object disabling the proxy for the
`kcm-regional` chart:

```yaml
spec:
  core:
    kcm:
      regional:
        telemetry:
          controller:
            proxy:
              enabled: false
```

### Behavior Differences

Unlike CAPI providers, `kcm-regional`:

* Does not proxy Kubernetes API requests
* Uses the proxy only for outbound telemetry delivery

If the conditions below are met:

1. Telemetry collection is enabled (See: [Telemetry Modes](./telemetry/modes.md))
1. Telemetry mode is set to `online`
1. `.Values.telemetry.controller.proxy.enabled` is `true`

Then the `Deployment` includes:

```yaml
env:
  - name: PROXY_SECRET
    value: "<secret-name>"
```

The application logic consumes this variable internally to configure the
telemetry client.

## Important Notes & Limitations

### No Proxying in the `kcm` Controller

The `kcm` controller does not proxy any requests because:

* All interactions are limited to the Kubernetes API
* All interactions are cluster-local

As a result, the proxy configuration is only propagated, not consumed, by the
`kcm` controller.

### TLS and Custom Certificates

TLS customization is **not supported** for proxy connections.

Specifically: there is no mechanism in the CAPI Operator API to mount
additional volumes.

As a result the following cannot be configured for HTTPS proxies:

  * Custom CA bundles
  * Client certificates
  * Mutual TLS (mTLS)

### `NO_PROXY` Configuration Is Critical

Because CAPI providers communicate extensively with the Kubernetes API server,
it is **strongly recommended** to include the following in the `NO_PROXY`
value:

* Kubernetes API server IPs and hostnames
* Cluster-internal CIDRs

Failing to do so may cause controller failures due to Kubernetes API requests
being incorrectly routed through the proxy.

### Openstack ORC Controller Requires Intervention

When doing initial installation one limitation is applied to the
`cluster-api-provider-openstack` ORC controller, which is installed in the
`orc-system` namespace.

To mitigate this you must either create the `orc-system` namespace and duplicate
the `Secret` there manually or disable the provider in the `Management`
object.
