# Extended Management Configuration

{{{ docsVersionInfo.k0rdentName }}} is deployed with the following default configuration, which may vary
depending on the release version:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: Management
metadata:
  name: kcm
spec:
  core:
    kcm: {}
  providers:
  - name: k0smotron
  - name: cluster-api-provider-aws
  - name: cluster-api-provider-azure
  - name: cluster-api-provider-openstack
  - name: cluster-api-provider-vsphere
  - name: projectsveltos
  release: kcm-0-0-7
```

As you can see, the `Management` object defines the providers that are available from within {{{ docsVersionInfo.k0rdentName }}}. Some of these are
providers directly used by the user, such as aws, azure, and so on, and others are used internally
by {{{ docsVersionInfo.k0rdentName }}}, such as Sveltos.

To see what is included in a specific release, look at the `release.yaml` file in the tagged release.
For example, here is the [v0.0.7 release.yaml](https://github.com/k0rdent/kcm/releases/download/v0.0.7/release.yaml).

{{{ docsVersionInfo.k0rdentName }}} allows you to customize its default configuration by modifying the spec of the `Management` object.
This enables you to manage the list of providers to deploy and adjust the default settings for core components.

For detailed examples and use cases, refer to [Examples and Use Cases](#examples-and-use-cases)

## Configuration Guide

There are two options to override the default management configuration of {{{ docsVersionInfo.k0rdentName }}}:

1. Update the `Management` object after the {{{ docsVersionInfo.k0rdentName }}} installation using `kubectl`:

    `kubectl --kubeconfig <path-to-management-kubeconfig> edit management`

2. Deploy {{{ docsVersionInfo.k0rdentName }}} skipping the default `Management` object creation and provide your
   own `Management` configuration:

    - Create `management.yaml` file and configure core components and providers.
      For example:

        ```yaml
        apiVersion: k0rdent.mirantis.com/v1beta1
        kind: Management
        metadata:
          name: kcm
        spec:
          core:
            kcm:
              config:
                controller:
                  templatesRepoURL: "oci://ghcr.io/my-oci-registry-name/kcm/charts"
          providers:
          - name: k0smotron
          - name: cluster-api-provider-aws
          - name: projectsveltos
          release: kcm-0-0-7
        ```

        In the example above, the `Management` object is configured with custom registry settings for the KCM controller
        and a reduced list of providers.

    - Specify `--create-management=false` controller argument and install {{{ docsVersionInfo.k0rdentName }}}:
      If installing using `helm` add the following parameter to the `helm
      install` command:

        ```bash
        --set="controller.createManagement=false"
        ```

    - Create `kcm` `Management` object after {{{ docsVersionInfo.k0rdentName }}} installation:

        ```bash
        kubectl --kubeconfig <path-to-management-kubeconfig> create -f management.yaml
        ```

You can customize the default configuration options for core components by updating the
`.spec.core.<core-component-name>.config` section in the `Management` object. For example, to override the default
settings for the KCM component, modify the `spec.core.kcm.config` section. To view the complete list of configuration
options available for kcm, refer to:
[KCM Configuration Options for {{{ docsVersionInfo.k0rdentName }}} v0.0.7](https://github.com/k0rdent/kcm/blob/v0.0.7/templates/provider/kcm/values.yaml)
(Replace v0.0.7 with the relevant release tag for other {{{ docsVersionInfo.k0rdentName }}} versions).

To customize the list of providers to deploy, update the `.spec.providers` section. You can add or remove providers
and configure custom templates for each provider. Each provider in the list must include the `name` field
and may include the `template` and `config` fields:

```yaml
- name: <provider-name>
  template: <provider-template> # optional. If omitted, the default template from the `Release` object will be used
  config: {} # optional provider configuration containing provider Helm Chart values in YAML format
```

## Examples and Use Cases

### Configuring a Custom OCI Registry for KCM components

You can override the default registry settings in {{{ docsVersionInfo.k0rdentName }}} by specifying the `templatesRepoURL`, `insecureRegistry`,
and `registryCredsSecret` parameters under `spec.core.kcm.config.controller`.

- `templatesRepoURL`: Specifies the registry URL for downloading Helm charts representing templates.
Use the `oci://` prefix for OCI registries. Default: `oci://ghcr.io/k0rdent/kcm/charts`.
- `globalRegistry`: Specifies the global registry. This value will be propagated to all `ClusterDeployment` objects
configuration as `global.registry` (for example, it is used for pulling cluster Helm extensions, such as the Cloud
Controller Manager and to download required images, such as `etcd` or `kube-proxy`).
- `insecureRegistry`: Allows connecting to an HTTP registry. Default: `false`.
- `registryCredsSecret`: Specifies the name of a Kubernetes `Secret` containing authentication credentials for the
registry (optional). This `Secret` should exist in the system namespace (default: `kcm-system`).
- `imagePullSecret`: Specifies the name of image pull secret which will be used
  to pull images and components for all providers defined in the
  `Management`. This `Secret` should exist in the system namespace (default:
  `kcm-system`).

Additionally, if your templates repository (`templatesRepoURL`) and/or registry (`globalRegistry`) is private and
uses a certificate signed by an unknown authority, you can make them "trusted" within the K0rdent system by configuring
the `registryCertSecret` parameter. This parameter should reference the name of a `Secret` in the system
(default: `kcm-system`) namespace that contains the root CA certificate(s) (`ca.crt`) used to verify the server
certificates of the registry and/or templates repository. If the `templatesRepoURL` and `globalRegistry` refer to
different endpoints, and each uses a different certificate authority, you can include both certificates concatenated
in the same `ca.crt` key of the `Secret`, like this:

```text
-----BEGIN CERTIFICATE-----
<templatesRepo CA cert>
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
<registry CA cert>
-----END CERTIFICATE-----
```

> NOTE:
> This is used for server certificate verification only - mutual TLS (mTLS) is not supported yet.

> NOTE:
> If you’re using a private registry signed by an unknown certificate authority, refer to
> [Private Secure Registry Usage](private-secure-registry.md) for the required prerequisites.

Example Configuration:

```yaml
spec:
  core:
    kcm:
      config:
        controller:
          templatesRepoURL: "oci://ghcr.io/my-private-oci-registry-name/kcm/charts"
          globalRegistry: ghcr.io/my-private-oci-registry-name
          insecureRegistry: false
          registryCredsSecret: my-private-oci-registry-creds
          registryCertSecret: registry-cert
```

> NOTE:
> Prior to K0rdent v0.3.0, the `templatesRepoURL` parameter was named `defaultRegistryURL`.
> (See: [K0rdent v0.3.0 Release Notes](https://github.com/k0rdent/kcm/releases/tag/v0.3.0)).

Example of a `Secret` with Registry Credentials:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: my-private-oci-registry-creds
  namespace: kcm-system
stringData:
  username: "my-user-123"
  password: "my-password-123"
```

Example of a `Secret` with Registry Certificate:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: registry-cert
  namespace: kcm-system
stringData:
  ca.crt: |
    -----BEGIN CERTIFICATE-----
    MIIDfjCCAmagAwIBAgIUV/Ykpp7jzkOdfsZs0wwNZOS9X04wDQYJKoZIhvcNAQEL
    ...
    2eVUGBCoHgFcUrkjcZlxvjjdaV5L/Y6mEt6u9mIhsb1M8w==
    -----END CERTIFICATE-----
```

The KCM controller will create the default [HelmRepository](https://fluxcd.io/flux/components/source/helmrepositories/)
using the provided configuration and fetch KCM components from this repository. For the example above,
the following `HelmRepository` will be created:

```yaml
apiVersion: source.toolkit.fluxcd.io/v1
kind: HelmRepository
metadata:
  labels:
    k0rdent.mirantis.com/managed: "true"
  name: my-private-oci-registry-name
  namespace: kcm-system
spec:
  insecure: false
  interval: 10m0s
  provider: generic
  type: oci
  url: oci://ghcr.io/my-private-oci-registry-name/kcm/charts
  secretRef:
    name: my-private-oci-registry-creds
  certSecretRef:
    name: registry-cert
```

### Configuring a global K0s URL

You can override the default URL from which to download the k0s binary in {{{ docsVersionInfo.k0rdentName }}} by
specifying the `globalK0sURL`, and optionally `k0sURLCertSecret` (if the k0s download URL is private and uses a
certificate signed by an unknown authority), under `spec.core.kcm.config.controller`. This is optional and is only
needed when the environment does not have access to the default upstream k0s binaries endpoint. This is required for
airgapped environments.

- `globalK0sURL`: Specifies the prefix of the k0s URL from which to download the k0s binary. This value will be
propagated to all `ClusterDeployment` objects configuration as `global.k0sURL`.
- `k0sURLCertSecret`: The name of the secret in the system (default: `kcm-system`) namespace containing the root CA
certificate (`ca.crt`) for the k0s download URL.

> NOTE:
> This is used for server certificate verification only - mutual TLS (mTLS) is not supported yet.

> NOTE:
> If you’re using a private registry signed by an unknown certificate authority, refer to
> [Private Secure Registry Usage](private-secure-registry.md) for the required prerequisites.

Example Configuration:

```yaml
spec:
  core:
    kcm:
      config:
        controller:
          globalK0sURL: https://172.19.123.4:8443
          k0sURLCertSecret: k0s-url-cert
```

Example of a `Secret` with K0s URL Certificate:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: k0s-url-cert
  namespace: kcm-system
stringData:
  ca.crt: |
    -----BEGIN CERTIFICATE-----
    MIIDfjCCAmagAwIBAgIUV/Ykpp7jzkOdfsZs0wwNZOS9X04wDQYJKoZIhvcNAQEL
    ...
    2eVUGBCoHgFcUrkjcZlxvjjdaV5L/Y6mEt6u9mIhsb1M8w==
    -----END CERTIFICATE-----
```

### Configuring a Custom Image for KCM controllers

You can override the default image for the KCM controllers by specifying the `repository`, `tag` and `pullPolicy`
parameters under `spec.core.kcm.config.image`:

Example Configuration:

```yaml
spec:
  core:
    kcm:
      config:
        image:
          repository: ghcr.io/my-custom-repo/kcm/controller
          tag: v0.0.7
          pullPolicy: IfNotPresent
```

### Configuring manager settings for CAPI providers

Starting from `v0.3.0`, {{{ docsVersionInfo.k0rdentName }}} supports configuring manager settings for CAPI providers. You can override
these settings by defining the `spec.providers[*].config.manager` section. The values under the `manager` section should
follow the format defined by the [CAPI Operator](https://pkg.go.dev/sigs.k8s.io/cluster-api-operator/api/v1alpha2#ManagerSpec).

> WARNING: Prior to `v1.2.0` {{{ docsVersionInfo.k0rdentName }}}, this is not supported for the `k0sproject-k0smotron` provider due to a bug in the CAPI Operator:
> [CAPI operator incorrectly finds the manager container if the number of containers is >1](https://github.com/kubernetes-sigs/cluster-api-operator/issues/787).
>
> Starting `v1.2.0` {{{ docsVersionInfo.k0rdentName }}} shipped with a CAPI Operator version with [the issue addressed](https://github.com/kubernetes-sigs/cluster-api-operator/pull/796).

For example, to override feature gates for the Cluster API Provider AWS, configure the following:

```yaml
spec:
  providers:
  - name: cluster-api-provider-aws
    config:
      manager:
        featureGates:
          MachinePool: true
          EKSEnableIAM: true
          EKSAllowAddRoles: true
```

### Configuring Cluster API In-Place Updates

> WARNING:
> This feature is experimental in both Cluster API and k0smotron.

<!-- TODO: put a proper version the feature is available starting with -->
KCM can enable the Cluster API
[in-place updates](https://github.com/kubernetes-sigs/cluster-api/blob/main/docs/proposals/20240807-in-place-updates.md)
mechanism. When it is enabled, a change of the k0s version (for example, after switching a `ClusterDeployment` to a
`ClusterTemplate` with a newer k0s version) is applied to the existing machines by
[k0s autopilot](https://docs.k0sproject.io/stable/autopilot/) instead of replacing them.

This applies to k0s-based clusters managed by k0smotron:

- Worker machines owned by a `MachineDeployment` are updated in place. Without this feature, a k0s version change
  replaces worker machines.
- Control plane machines of a `K0sControlPlane` with the `InPlace` update strategy (the default) are already updated in
  place by k0smotron itself. With this feature enabled, k0smotron hands the update over to Cluster API instead.

Only the k0s version is updated in place. Other changes, such as a new machine template or bootstrap configuration,
still replace the machines. For details, see the k0smotron documentation on updating
[control plane](https://docs.k0smotron.io/stable/update/update-capi-cluster/) and
[worker](https://docs.k0smotron.io/stable/update/update-capi-cluster-workers/) nodes.

The feature is *disabled* by default. To enable it, set the `enableInPlaceUpdates` KCM controller setting in the
`Management` object:

```yaml
spec:
  core:
    kcm:
      config:
        controller:
          enableInPlaceUpdates: true
```

Or, on the initial installation, add the following parameter to the `helm install` command:

```bash
--set="controller.enableInPlaceUpdates=true"
```

KCM passes the setting to the providers of the `Management` object and of every `Region` object, which results in
the following:

- The `cluster-api` core provider gets the `InPlaceUpdates` and `RuntimeSDK` feature gates enabled.
- The `cluster-api-provider-k0sproject-k0smotron` provider gets the `InPlaceUpdates` feature gate of the control plane
  provider enabled, and deploys the k0smotron in-place version update extension: the `k0smotron-extension-webhook`
  `Deployment` in the system namespace and the `inplace-version-update-extensionconfig` `ExtensionConfig` that registers
  it within Cluster API.

Other providers ignore the setting.

#### Overriding the setting per provider

The `inPlaceUpdates.enabled` value in the provider configuration takes precedence over the KCM controller setting.
Feature gates explicitly set under `manager.featureGates` of the `cluster-api` provider and
`controlPlane.manager.featureGates` of the `cluster-api-provider-k0sproject-k0smotron` provider take precedence over
both. The extension is deployed whenever the resulting `InPlaceUpdates` feature gate of the k0smotron control plane
provider is enabled.

For example, to enable in-place updates only for the providers of a specific `Region` while keeping the KCM controller
setting disabled, configure both providers in the `Region` object:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: Region
metadata:
  name: region1
spec:
  core:
    capi:
      config:
        inPlaceUpdates:
          enabled: true
  providers:
  - name: cluster-api-provider-k0sproject-k0smotron
    config:
      inPlaceUpdates:
        enabled: true
```

The same configuration applies to the `Management` object. Conversely, set `inPlaceUpdates.enabled: false` to disable
the feature for a provider while the KCM controller setting is enabled.

#### Configuring the extension webhook server

You can configure the extension webhook server under `inPlaceUpdates.extension` in the
`cluster-api-provider-k0sproject-k0smotron` provider configuration:

```yaml
spec:
  providers:
  - name: cluster-api-provider-k0sproject-k0smotron
    config:
      inPlaceUpdates:
        extension:
          image:
            repository: "" # defaults to <globalRegistry>/capi/k0smotron if globalRegistry is set, otherwise to quay.io/k0sproject/k0smotron
            tag: "" # defaults to the k0smotron version of the provider
            pullPolicy: IfNotPresent
          replicas: 1
          resources: {}
          nodeSelector: {}
          tolerations: []
          affinity: {}
```

The extension webhook server uses the same image as the k0smotron providers, so no additional image needs to be
mirrored to a private registry.

#### Limitations

- In-place updates must be enabled for both the `cluster-api` and the `cluster-api-provider-k0sproject-k0smotron`
  providers. The installation or upgrade of the k0smotron provider fails if `spec.manager.featureGates` of the Cluster API
  `CoreProvider` object lacks either of the `InPlaceUpdates` or `RuntimeSDK` feature gates. Feature gates enabled by other
  means, such as provider `patches` or additional manager arguments, are not recognized and fail the check as well, so
  enable them with `inPlaceUpdates.enabled` or `manager.featureGates` instead.
- The `InPlaceUpdates` feature gate of the `cluster-api` provider requires the `RuntimeSDK` feature gate, since the
  Cluster API core provider fails to start otherwise. Setting `manager.featureGates.InPlaceUpdates: true` without
  `manager.featureGates.RuntimeSDK: true` fails the installation or upgrade of the `cluster-api` provider.
- Disabling the feature removes the extension webhook server. Disable it only when no cluster uses the `InPlace` update
  strategy and no cluster is being updated.

### Configuring the Sveltos Stuck Tokens Controller

If a management cluster has some maintenance activity or hardware issue causing it to go down for more than ~30 minutes,
the token for the management `sveltoscluster` object expires. This leads to continuous errors and
failure to reconcile the management `sveltoscluster` object. [Related issue: KCM #995](https://github.com/k0rdent/kcm/issues/995).

A dedicated controller that automatically detects and renews stuck tokens is shipped with
{{{ docsVersionInfo.k0rdentName }}} starting `v1.1.0` and is *disabled* by default.

To enable the controller, set:

```yaml
spec:
  core:
    kcm:
      config:
        controller:
          enableSveltosExpiredCtrl: true
```

### Configuring Default Timeout for Helm Install and Upgrade Operations

In some environments, Helm chart installations or upgrades may take longer than the default timeout of 5 minutes.
This hardcoded limit could cause operations to fail unexpectedly if they exceeded the timeout.

Starting from K0rdent v1.3.0, KCM allows you to configure the default Helm timeout using the `defaultHelmTimeout`
controller setting:

```yaml
spec:
  core:
    kcm:
      config:
        controller:
          defaultHelmTimeout: 20m
```

This value accepts standard duration format (e.g., 20m, 1h).

### Configuring Telemetry

To configure [Telemetry](./telemetry/index.md) options via the
[Management](../reference/crds/index.md#management) object,
set values under the `telemetry` block. For example, you can disable collection by setting `mode` to `disabled`:

```yaml
spec:
  core:
    kcm:
      regional:
        telemetry:
          mode: disabled
```

Follow the [telemetry configuration page](./telemetry/configuration.md)
for all of the possible values.

### Configuring ImagePullSecrets

Starting with k0rdent v1.6.0, a new flag (`controller.imagePullSecret`) has been introduced
to pass registry authentication parameters to providers on the management
cluster. To use it, you must create an image pull secret in a `dockerconfigjson`
format following the [standard
procedure](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/).

> NOTE:
> If the `Management` object also defines custom Projectsveltos agent or drift detection patches, use the structured
> patch format consistently. Mixing legacy bare patches with KCM-generated image pull secret patches can cause
> [Sveltos PatchTransformer errors](../troubleshooting/known-issues-sveltos-patch-formats.md).

After the secret has been created, you can reference it by name in the helm chart
values on:

- Initial installation values

    ```yaml
    controller:
      imagePullSecret: registry-pull-secret
    ```

- Management object configuration

    ```yaml
    spec:
      core:
        kcm:
          config:
            controller:
              imagePullSecret: registry-pull-secret
    ```

On initial installation, if registry authentication is required, you must still
pass `imagePullSecrets` values to all subchart values as follows:

```yaml
global:
  imagePullSecrets:
    - name: registry-pull-secret

controller:
  imagePullSecret: registry-pull-secret

flux2:
  imagePullSecrets:
    - name: registry-pull-secret

regional:
  cluster-api-operator:
    imagePullSecrets:
    - name: registry-pull-secret

  velero:
    image:
      imagePullSecrets:
      - registry-pull-secret

rbac-manager:
  image:
    imagePullSecrets:
    - registry-pull-secret
```

### Configuring Custom User-Provided Patches for Providers

You can provide custom CAPI Operator `spec.patches` entries per provider by
setting `spec.providers[].config.patches` in the `Management` object.

This is useful when you need provider-specific adjustments that are not covered
by default settings, for example adding custom pod annotations, labels, or
other Deployment-level patch customizations.

Custom patches are merged with built-in provider patches.

Example:

```yaml
spec:
  providers:
  - name: cluster-api-provider-aws
    config:
      patches:
      - patch: |
          - op: add
            path: /spec/template/metadata/annotations/example.com~1custom-patch
            value: "enabled"
        target:
          group: apps
          version: v1
          kind: Deployment
          namespace: kcm-system
```

Example for `k0smotron` provider (patches are defined per corresponding
sub-provider):

```yaml
spec:
  providers:
  - name: k0smotron
    config:
      infrastructure:
        patches:
        - patch: |
            - op: add
              path: /spec/template/metadata/annotations/example.com~1infra-patch
              value: "enabled"
          target:
            group: apps
            version: v1
            kind: Deployment
            namespace: kcm-system
      bootstrap:
        patches:
        - patch: |
            - op: add
              path: /spec/template/metadata/annotations/example.com~1bootstrap-patch
              value: "enabled"
          target:
            group: apps
            version: v1
            kind: Deployment
            namespace: kcm-system
      controlPlane:
        patches:
        - patch: |
            - op: add
              path: /spec/template/metadata/annotations/example.com~1control-plane-patch
              value: "enabled"
          target:
            group: apps
            version: v1
            kind: Deployment
            namespace: kcm-system
```

### Configuring Automatic Provider Reload Annotations

When enabled, k0rdent adds `reloader.stakater.com/auto` annotations to provider
Deployments (through provider `patches`), so changes in referenced Secrets or
ConfigMaps can trigger automatic pod reloads.

This is useful in environments where credentials, certificates, or proxy-related
configuration are rotated and you want provider controllers to pick up changes
without manual rollout restarts.

> NOTE:
> This mechanism relies on the [Stakater Reloader](https://github.com/stakater/reloader)
> controller being installed in
> the management cluster.

To enable it in the `Management` object:

```yaml
spec:
  core:
    kcm:
      config:
        enableProvidersReload: true
```

### Configuring Cert Manager

Some environments require additional Cert Manager configuration. You can customize cert-manager by setting
`spec.core.kcm.config.cert-manager` in either a `Management` or `Region` resource.

For example, to enable support for the Gateway API, you can configure
`spec.core.kcm.config.cert-manager.config.enableGatewayAPI: true`.

> NOTE: See the Cert Manager documentation for the Gateway API in
> the [Annotated Gateway resource guide](https://cert-manager.io/docs/usage/gateway/) (before enabling this feature,
> ensure that all prerequisites are met, including installing the Gateway API CRDs).

For the full list of available Cert Manager
configuration options, refer to the [cert-manager's ArtifactHub page](https://artifacthub.io/packages/helm/cert-manager/cert-manager).

```yaml
spec:
  core:
    kcm:
      config:
        cert-manager:
          config:
            enableGatewayAPI: true
```
