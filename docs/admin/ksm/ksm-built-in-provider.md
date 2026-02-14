# Built-In KSM Provider

## Overview

{{{ docsVersionInfo.k0rdentName }}} comes with a built-in KSM provider which relies on [ProjectSveltos](https://projectsveltos.github.io/sveltos/main/) as a CD solution.
This provider is enabled by default by the command-line flag `--enable-sveltos-ctrl` provided to kcm-controller-manager:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: kcm-controller-manager
  namespace: kcm-system
spec:
  # other fields are omitted
  template:
    spec:
      containers:
        - name: manager
          args:
          # other flags are omitted
          - --enable-sveltos-ctrl=true
```

Enabling this flag along with enabling of the projectsveltos provider in `Management` object results into creation of the `StateManagementProvider`:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: StateManagementProvider
metadata:
  name: ksm-projectsveltos
spec:
  adapter:
    apiVersion: apps/v1
    kind: Deployment
    name: kcm-controller-manager
    namespace: kcm-system
    readinessRule: |-
      self.status.availableReplicas == self.status.replicas &&
      self.status.availableReplicas == self.status.updatedReplicas &&
      self.status.availableReplicas == self.status.readyReplicas
  provisioner:
  - apiVersion: apps/v1
    kind: Deployment
    name: addon-controller
    namespace: projectsveltos
    readinessRule: |-
      self.status.availableReplicas == self.status.replicas &&
      self.status.availableReplicas == self.status.updatedReplicas &&
      self.status.availableReplicas == self.status.readyReplicas
  provisionerCRDs:
  - group: config.projectsveltos.io
    resources:
    - profiles
    - clustersummaries
    version: v1beta1
  selector:
    matchLabels:
      ksm.k0rdent.mirantis.com/adapter: kcm-controller-manager
  suspend: false
```

Aside from `StateManagementProvider` object creation, the controller responsible for `ServiceSet` object reconciliation will be configured and added to controller-manager.

Reconciliation of the `ServiceSet` objects will result into creation or update of ProjectSveltos-specific objects such as `Profile` and `ClusterProfile` which in turn will be reconciled by ProjectSveltos addon-controller referenced as provisioner.

## Provider Configuration

> NOTE: In previous versions the following configuration was a part of `ClusterDeployment` and `MultiClusterService` `.spec.serviceSpec` field.
> For backward compatibility it is still possible to not to add `.spec.serviceSpec.provider` field to those objects. In this case the built-in
> provider will be used and the configuration defined in `.spec.serviceSpec` will be copied to `.spec.provider.config` in produced `ServiceSet` object.

`ClusterDeployment`, `MultiClusterService` and `ServiceSet` objects have field `.spec.provider.config` in their Spec. This field is an `apiextensionv1.JSON` field which allows to pass any supported configuration to the underlying provider-specific objects.
For instance built-in adapter which relies on ProjectSveltos API, supports the following configuration which will seamlessly passed from `ClusterDeployment` or `MultiClusterService` objects to ProjectSveltos `Profile` or `ClusterProfile`:

```yaml
spec:
  provider:
    config:
      # "syncMode" specifies how features are synced in a matching workload cluster.
      # - OneTime means, first time a workload cluster matches the ClusterProfile,
      # features will be deployed in such cluster. Any subsequent feature configuration
      # change won't be applied into the matching workload clusters;
      # - Continuous mode ensures that the first time a workload cluster matches a ClusterProfile,
      # the specified features are deployed. Subsequent changes to the feature configuration are also
      # automatically applied to all matching workload clusters.
      # _ SyncModeContinuousWithDriftDetection operates similarly to Continuous mode, but also monitors
      # matching managed clusters for configuration drift. If drift is detected, a reconciliation is
      # triggered to ensure the managed cluster's configuration aligns with the ClusterProfile.
      # - DryRun means no change will be propagated to any matching cluster. A report
      # instead will be generated summarizing what would happen in any matching cluster
      # because of the changes made to ClusterProfile while in DryRun mode.
      syncMode: OnTime | Continuous | ContinuousWithDriftDetection | DryRun
      # By default (when "continueOnError" is unset or set to false), Sveltos stops deployment after
      # encountering the first error.
      # If set to true, Sveltos will attempt to deploy remaining resources in the ClusterProfile even
      # if errors are detected for previous resources.
      continueOnError: bool
      # When "stopOnConflict" is set to true, Sveltos stops deployment after
      # encountering the first conflict (e.g., another ClusterProfile already deployed the resource).
      # If set to true, Sveltos will attempt to deploy remaining resources in the ClusterProfile even
      # if conflicts are detected for previous resources.
      stopOnConflict: bool
      # "reload" indicates whether Deployment/StatefulSet/DaemonSet instances deployed
      # by Sveltos and part of Profile (or ClusterProfile) need to be restarted via rolling upgrade
      # when a ConfigMap/Secret instance mounted as volume is modified.
      # When set to true, when any mounted ConfigMap/Secret is modified, Sveltos automatically
      # starts a rolling upgrade for Deployment/StatefulSet/DaemonSet instances mounting it.
      reload: bool
      # "priority" sets the priority for the services defined in this spec.
      # Higher value means higher priority and lower means lower.
      # In case of conflict with another object managing the service,
      # the one with higher priority will get to deploy its services.
      priority: int32
      # Define additional Kustomize inline "patches" applied for all resources on this profile
      # Within the Patch Spec you can use templating.
      # REF: [github.com/projectsveltos/libsveltos/api/v1beta1.Patch]
      patches: []
      # "driftExclusions" is a list of configuration drift exclusions to be applied when syncMode is
      # set to ContinuousWithDriftDetection. Each exclusion specifies JSON6902 paths to ignore
      # when evaluating drift, optionally targeting specific resources and features.
      # REF: [github.com/projectsveltos/addon-controller/api/v1beta1.DriftExclusion]
      driftExclusions: []
      # "driftIgnore" is a list of fields selectors to ignore when checking for drift.
      # REF: [github.com/projectsveltos/libsveltos/api/v1beta1.PatchSelector]
      driftIgnore: []
      # "templateResourceRefs" is a list of resources to collect from the management cluster,
      # the values from which can be used in templates.
      # REF: [github.com/projectsveltos/addon-controller/api/v1beta1.TemplateResourceRef]
      templateResourceRefs: []
      # "policyRefs" references all the ConfigMaps/Secrets/Flux Sources containing kubernetes resources
      # that need to be deployed in the matching managed clusters.
      # The values contained in those resources can be static or leverage Go templates for dynamic customization.
      # When expressed as templates, the values are filled in using information from
      # resources within the management cluster before deployment (Cluster and TemplateResourceRefs)
      # REF: [github.com/projectsveltos/addon-controller/api/v1beta1.PolicyRef]
      policyRefs: []
```