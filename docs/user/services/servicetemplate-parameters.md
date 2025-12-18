# Parameter List

Here is an idea of the parameters involved.

## ServiceSpec Parameters

> WARNING:
> The following fields are **deprecated** and should be configured in `.spec.serviceSpec.provider.config` instead:
> - `.spec.serviceSpec.syncMode`
> - `.spec.serviceSpec.driftIgnore`
> - `.spec.serviceSpec.driftExclusions`
> - `.spec.serviceSpec.priority`
> - `.spec.serviceSpec.stopOnConflict`
> - `.spec.serviceSpec.reload`
> - `.spec.serviceSpec.continueOnError`
> - `.spec.serviceSpec.templateResourceRefs`
> - `.spec.serviceSpec.policyRefs`

### Current Recommended Parameters

| Parameter                                      | Example                                                     | Description                                                                                     |
|------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| `.spec.serviceSpec.provider.name`              | `kcm-projectsveltos`                                        | Name of the StateManagementProvider to use for service deployment                               |
| `.spec.serviceSpec.provider.config`            | See [Provider Configuration](#provider-configuration) below | Provider-specific configuration                                                                 |
| `.spec.serviceSpec.provider.selfManagement`    | `true`                                                      | Deploy services to the management cluster itself (for MultiClusterService only)                 |
| `.spec.serviceSpec.services[].template`        | `kyverno-3-2-6`                                             | Name of the `ServiceTemplate` object located in the same namespace                              |
| `.spec.serviceSpec.services[].templateChain`   | `kyverno-chain`                                             | Name of the `ServiceTemplateChain` for upgrade/rollback paths (optional)                        |
| `.spec.serviceSpec.services[].name`            | `my-kyverno-release`                                        | Release name for the beach-head service                                                         |
| `.spec.serviceSpec.services[].namespace`       | `my-kyverno-namespace`                                      | Release namespace for the beach-head service (default: `.spec.services[].name`)                 |
| `.spec.serviceSpec.services[].values`          | `replicas: 3`                                               | Helm values to be used with the template while deploying the beach-head services                |
| `.spec.serviceSpec.services[].valuesFrom[]`    | See [ValuesFrom Structure](#valuesfrom-structure) below     | Array of references to ConfigMaps or Secrets containing helm values                             |
| `.spec.serviceSpec.services[].helmOptions`     | See [HelmOptions Structure](#helmoptions-structure) below   | Per-service Helm options that override template-level helmOptions                               |
| `.spec.serviceSpec.services[].dependsOn[]`     | See [Service Dependencies](#service-dependencies) below     | Array of service dependencies (service won't deploy until dependencies are ready)               |
| `.spec.serviceSpec.services[].disable`         | `false`                                                     | Boolean flag to disable handling of this service - service won't be deployed (default: `false`) |

### ValuesFrom Structure

The `valuesFrom` field allows referencing ConfigMaps or Secrets that contain Helm values:

```yaml
valuesFrom:
  - kind: ConfigMap  # or Secret
    name: my-config
```

**Fields:**
- `kind` (required): Either `ConfigMap` or `Secret`
- `name` (required): Name of the ConfigMap or Secret

**Merge Behavior:**
- Multiple `valuesFrom` entries are merged in order
- Values from `.spec.serviceSpec.services[].values` are merged last (highest priority)

**Example:**
```yaml
services:
  - template: ingress-nginx-4-11-3
    name: ingress-nginx
    namespace: ingress-nginx
    valuesFrom:
      - kind: ConfigMap
        name: base-config
      - kind: Secret
        name: sensitive-config
    values: |
      # These values override anything from valuesFrom
      controller:
        replicaCount: 3
```

### HelmOptions Structure

Per-service Helm options that override template-level `helmOptions`. See [ServiceTemplate Helm Options](../../admin/ksm/ksm-service-templates.md#spechelmoptions) for the complete list of available options.

**Example:**
```yaml
services:
  - template: cert-manager-1-18-2
    name: cert-manager
    namespace: cert-manager
    helmOptions:
      wait: true
      waitForJobs: true
      timeout: 15m
      createNamespace: true
```

### Service Dependencies

The `dependsOn` field defines dependencies between services. A service will not be deployed until all its dependencies are successfully deployed.

```yaml
dependsOn:
  - name: cert-manager
    namespace: cert-manager
```

**Fields:**
- `name` (required): Name of the dependent service
- `namespace` (required): Namespace of the dependent service

**Behavior:**
- Dependencies are evaluated per cluster (for MultiClusterService, each matching cluster is evaluated independently)
- If a service already exists from another source (e.g., different MultiClusterService), it will be processed depending on defined priority
- Circular dependencies are not allowed and will cause validation errors

**Example:**
```yaml
services:
  - template: cert-manager-1-18-2
    name: cert-manager
    namespace: cert-manager
  - template: ingress-nginx-4-13-0
    name: nginx
    namespace: nginx
    dependsOn:
      - name: cert-manager
        namespace: cert-manager
  - template: my-app-1-0-0
    name: my-app
    namespace: my-app
    dependsOn:
      - name: nginx
        namespace: nginx
      - name: cert-manager
        namespace: cert-manager
```

### Provider Configuration

The `.spec.serviceSpec.provider.config` field accepts provider-specific configuration as JSON. For the built-in `kcm-projectsveltos` provider, the following options are available:

| Field                    | Type    | Default                        | Description                                                                                |
|--------------------------|---------|--------------------------------|--------------------------------------------------------------------------------------------|
| `syncMode`               | string  | `Continuous`                   | How services are synced: `OneTime`, `Continuous`, `ContinuousWithDriftDetection`, `DryRun` |
| `priority`               | int32   | `100`                          | Priority for conflict resolution (higher number = higher priority)                         |
| `stopOnConflict`         | bool    | `false`                        | Stop deployment if a conflict is encountered                                               |
| `continueOnError`        | bool    | `false`                        | Continue deploying other services if one fails                                             |
| `reload`                 | bool    | `false`                        | Restart deployments when mounted ConfigMap/Secret changes                                  |
| `driftIgnore`            | array   | `[]`                           | Resources to ignore for drift detection (Sveltos PatchSelector format)                     |
| `driftExclusions`        | array   | `[]`                           | Specific field paths to ignore for drift (JSON6902 format)                                 |
| `templateResourceRefs`   | array   | `[]`                           | Resources to collect from management cluster for templating                                |
| `policyRefs`             | array   | `[]`                           | ConfigMaps/Secrets/Flux Sources with Kubernetes resources                                  |
| `patches`                | array   | `[]`                           | Kustomize inline patches to apply to all resources                                         |

**Example:**
```yaml
serviceSpec:
  provider:
    name: kcm-projectsveltos
    config:
      syncMode: ContinuousWithDriftDetection
      priority: 200
      stopOnConflict: false
      continueOnError: true
      reload: true
      driftIgnore:
        - group: apps
          kind: Deployment
          name: my-app
      patches:
        - target:
            kind: Deployment
          patch: |-
            - op: add
              path: /metadata/labels/environment
              value: production
  services:
    - template: my-app-1-0-0
      name: my-app
```

## Deprecated Parameters (Legacy)

The following parameters are still supported but deprecated. Use `.spec.serviceSpec.provider.config` instead:

| Parameter                                 | Replacement                                              | Description                                                                    |
|-------------------------------------------|----------------------------------------------------------|--------------------------------------------------------------------------------|
| `.spec.serviceSpec.syncMode`              | `.spec.serviceSpec.provider.config.syncMode`             | Specifies how services are synced in the target cluster (default:`Continuous`) |
| `.spec.serviceSpec.driftIgnore`           | `.spec.serviceSpec.provider.config.driftIgnore`          | Specifies resources to ignore for drift detection                              |
| `.spec.serviceSpec.driftExclusions`       | `.spec.serviceSpec.provider.config.driftExclusions`      | Specifies specific configurations of resources to ignore for drift detection   |
| `.spec.serviceSpec.priority`              | `.spec.serviceSpec.provider.config.priority`             | Sets the priority for services defined in this spec (default: `100`)           |
| `.spec.serviceSpec.stopOnConflict`        | `.spec.serviceSpec.provider.config.stopOnConflict`       | Stops deployment upon first conflict (default: `false`)                        |
| `.spec.serviceSpec.reload`                | `.spec.serviceSpec.provider.config.reload`               | Auto-restart on ConfigMap/Secret changes (default: `false`)                    |
| `.spec.serviceSpec.continueOnError`       | `.spec.serviceSpec.provider.config.continueOnError`      | Continue deployment on errors (default: `false`)                               |
| `.spec.serviceSpec.templateResourceRefs`  | `.spec.serviceSpec.provider.config.templateResourceRefs` | Resources to collect for templating                                            |
| `.spec.serviceSpec.policyRefs`            | `.spec.serviceSpec.provider.config.policyRefs`           | ConfigMaps/Secrets/Flux Sources with resources                                 |