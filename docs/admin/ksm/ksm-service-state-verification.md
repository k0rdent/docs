# Service State Verification

## Overview

When {{{ docsVersionInfo.k0rdentName }}} deploys Helm-based services, ProjectSveltos reports each release as `Deployed` as soon as its Helm SDK returns success. That success signal is issued when the release manifest has been applied, not when the resulting workload is actually healthy on the child cluster. The verifier bridges that gap: for every service ProjectSveltos reports as `Deployed`, KSM cross-checks the child cluster's actual state against a set of CEL-based health rules before allowing the service to stay `Deployed`.

Two independent features rely on the state being accurate:

- **Sequential upgrades**, which advance services through their `ServiceTemplateChain` over time. A chain step cannot advance until the current step's service is verified as `Deployed`.
- **Dependency ordering** via `dependsOn`, which gates a service's apply on other services being `Deployed`.

## The verification flow

For each Helm service reported as `Deployed` by Sveltos:

1. KSM queries the child cluster for resources labeled with the release name (via well-known Helm labels: `release`, `app`, `app.kubernetes.io/instance`, `app.kubernetes.io/name`).
2. Every matching resource is evaluated against every CEL health rule registered for its `GroupKind`. Rules layer additively — a resource is considered healthy only if every applicable rule passes.
3. KSM computes a fingerprint hash covering chart identity, values, and patches for the release, using data from Sveltos's `ClusterConfiguration` and `ClusterSummary`.
4. When Sveltos's verdict, the on-cluster verifier's verdict, and the hash all agree that the deploy has landed, KSM stamps `.status.services[i].lastDeployedHash` and `.status.services[i].version`.

When the verifier finds unhealthy resources, the service state is downgraded from `Deployed` to `Provisioning` and `ServiceHealth<Kind>` conditions are attached to that service in `.status.services[i].conditions[]` listing the specific unhealthy resources.

When the hash inputs are not yet observable (Sveltos has not finished populating its `ClusterConfiguration` section for the profile), the service state stays `Provisioning` and the `ServiceSet` is requeued so KSM can try again on a subsequent round.

The invariant this maintains: **`state == Deployed` on a service always implies a non-empty `lastDeployedHash`**. If the fingerprint cannot be confirmed for any reason, the service is not marked `Deployed`.

## Health rules — three tiers

Health rules are loaded from `ConfigMap` objects labeled `k0rdent.mirantis.com/health-rule-target`. Three tiers are applied additively — every applicable rule must pass for a resource to be considered healthy.

| Tier                 | Namespace                               | Label value                                                     | Purpose                                                                                   |
|----------------------|-----------------------------------------|-----------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| 1 (cluster-global)   | System namespace (default `kcm-system`) | `global`                                                        | Defaults shipped with {{{ docsVersionInfo.k0rdentName }}}. Applied to every `ServiceSet`. |
| 2 (namespace-global) | `ServiceSet` namespace                  | `global`                                                        | Tenant defaults. Applied to every `ServiceSet` in that namespace.                         |
| 3 (owner-targeted)   | `ServiceSet` namespace                  | Name of the owning `MultiClusterService` or `ClusterDeployment` | Workload-specific rules.                                                                  |

Rules layer additively across tiers. Any rule applicable to a resource must pass for that resource to be considered healthy.

Rules are cached and re-loaded when the source `ConfigMap`'s `ResourceVersion` changes. Adding, editing, or removing rules takes effect on subsequent verifier rounds without requiring a controller restart.

## Default rules

{{{ docsVersionInfo.k0rdentName }}} ships a default rule `ConfigMap` named `kcm-default-health-rules` in the system namespace (default `kcm-system`), labeled as tier 1 (cluster-global). It defines rules for six workload Kinds:

| GroupKind               | What the rule checks                                                                                                            |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| `apps/Deployment`       | `observedGeneration >= generation` and `readyReplicas == updatedReplicas == spec.replicas`.                                     |
| `apps/StatefulSet`      | Same as Deployment plus `currentRevision == updateRevision` (no rolling update in progress).                                    |
| `apps/DaemonSet`        | `numberReady == desiredNumberScheduled == updatedNumberScheduled`.                                                              |
| `Pod`                   | A `Ready=True` condition exists. Pods with `deletionTimestamp` set are treated as healthy (graceful shutdown is not a failure). |
| `PersistentVolumeClaim` | `.status.phase == "Bound"`.                                                                                                     |
| `PersistentVolume`      | `.status.phase == "Bound"`.                                                                                                     |

Any resource with a `deletionTimestamp` set is treated as healthy across all Kinds. User-initiated deletion is not a failure — flagging it as unhealthy would fire spurious `Provisioning` signals during rolling updates and PVC reclaims.

## Authoring custom rules

Custom rules are declared as YAML entries under the `data.rules` key of a labeled `ConfigMap`. Each rule declares its target `GroupKind`, scope, and two CEL expressions.

### Rule schema

| Field     | Required | Purpose                                                                                                                                                                  |
|-----------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `group`   | yes      | API group. Use `""` for the core group.                                                                                                                                  |
| `version` | yes      | API version. Must be one the target cluster actually serves.                                                                                                             |
| `kind`    | yes      | Kind name.                                                                                                                                                               |
| `scope`   | yes      | Either `Namespaced` or `Cluster`. Validated against the target cluster's discovery — a rule declaring the wrong scope is rejected.                                       |
| `healthy` | yes      | CEL expression returning `bool`. The resource under evaluation is bound to the CEL variable `obj`.                                                                       |
| `message` | yes      | CEL expression returning `string`. Evaluated only when `healthy` returns `false`; the resulting text appears in the `ServiceHealth<Kind>` condition on the `ServiceSet`. |

### Worked example — a Job rule

The default rule set does not cover `batch/v1/Job`, so a chart that deploys a Job would not have its state verified out of the box. This example rule reports a Job as healthy when it has succeeded at least once:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: job-health-rules
  namespace: kcm-system
  labels:
    k0rdent.mirantis.com/health-rule-target: global
data:
  rules: |
    - group: batch
      version: v1
      kind: Job
      scope: Namespaced
      healthy: |
        has(obj.status.succeeded) && int(obj.status.succeeded) > 0
      message: |
        !has(obj.status.succeeded) || int(obj.status.succeeded) == 0
          ? "job has not completed successfully yet"
          : ""
```

To scope the same rule to a specific `MultiClusterService` named `data-jobs`, replace the label value:

```yaml
metadata:
  labels:
    k0rdent.mirantis.com/health-rule-target: data-jobs
```

and place the `ConfigMap` in the same namespace as the `ServiceSet` the `MultiClusterService` owns.

### CEL notes

- The variable `obj` holds the resource under evaluation. Access fields as `obj.spec.replicas`, `obj.status.conditions[0].type`, etc.
- Use `has(...)` before accessing optional fields — CEL raises an error on missing paths otherwise.
- `int(...)` coercion is often required because Kubernetes JSON numbers deserialize as different Go types depending on context.
- The `ext.Strings` extension is available (methods like `.join(",")` on string lists).
- Both `healthy` and `message` share the same `obj` binding. `message` is evaluated only on the unhealthy path.

### Validation of custom rules

Rules that fail to parse or compile are surfaced on the `ServiceSet`'s `ServiceSetHealthRules` condition. When all rules load and compile, the condition is `True` with reason `AllRulesValid`. When some fail, the condition is `False` and the message enumerates the offending sources (up to a bounded number to keep the message readable).

Scope mismatches (a rule declaring `Cluster` for a Kind that is actually `Namespaced` on the target cluster, or vice versa) are surfaced as a synthetic unhealthy verdict with reason `HealthRuleScopeMismatch` on the affected service. The verifier does not run the mismatched rule.

Versions declared by rules but not served by the target cluster are logged at debug level, aggregated into one line per verifier round.

### RBAC for custom rule Kinds

{{{ docsVersionInfo.k0rdentName }}}'s shipped `ClusterRole` grants read on the six default Kinds only (Deployment, StatefulSet, DaemonSet, Pod, PersistentVolumeClaim, PersistentVolume). Rules targeting additional Kinds — Jobs, CRDs, custom resources — require the operator to grant read on those Kinds to the KCM controller `ServiceAccount`. Without the extra permission, the verifier hits `Forbidden` on `List` and logs the error.

This applies only to the self-management scheme, where the controller reads workload resources on the management cluster itself. In flat and regional schemes, the workload cluster is reached via its CAPI kubeconfig, which typically carries cluster-admin equivalent access.

## Deployment schemes — where each client reads

{{{ docsVersionInfo.k0rdentName }}} supports three deployment schemes. The verifier needs three logical clients — for the management cluster (rules), for the regional cluster (Sveltos artifacts), and for the child cluster (workload). Each scheme collapses some of them onto the same client:

| Scheme          | Health rules from | Sveltos artifacts from | Workload resources from                                      |
|-----------------|-------------------|------------------------|--------------------------------------------------------------|
| Self-management | Management        | Management             | Management                                                   |
| Flat            | Management        | Management             | Child (via `<Spec.Cluster>-kubeconfig` secret on management) |
| Regional        | Management        | Regional               | Child (via `<Spec.Cluster>-kubeconfig` secret on regional)   |

For adopted clusters registered via `SveltosCluster`, the workload kubeconfig is discovered from the `SveltosCluster.Spec.KubeconfigName` field.

## What surfaces on the `ServiceSet`

The verifier writes to two levels of `ServiceSet.status`:

**Per-service** (`.status.services[i]`):

- `state` — reflects the verifier's decision after cross-checking Sveltos with the child cluster.
- `lastDeployedHash` — the fingerprint at which this service was most recently confirmed `Deployed`. Never populated on a service that has not been verified.
- `version` — the spec-side version at the moment the deploy was verified. Advances together with `lastDeployedHash`.
- `conditions[]` — `ServiceHealth<Kind>` entries, one per Kind with unhealthy resources. Message lists the specific refs (capped at three per Kind; the rest are summarized as "…and N more").

**Per-`ServiceSet`** (`.status.conditions[]`):

- `ServiceSetHealthRules` — `True` when all rule `ConfigMap`s loaded and compiled successfully; `False` with the offending sources in the message otherwise.

### Example mid-upgrade status

A ServiceSet whose `podinfo` release has just been upgraded from 6.5.0 to 6.6.0, currently mid-rollout:

```yaml
status:
  conditions:
    - type: ServiceSetHealthRules
      status: "True"
      reason: AllRulesValid
      message: All health rules loaded successfully
    - type: ServicesInReadyState
      status: "False"
      reason: Succeeded
      message: 0/1
  services:
    - name: podinfo
      namespace: podinfo
      template: podinfo-6-6-0
      type: Helm
      state: Provisioning
      lastDeployedHash: 3f2c8b1a...
      version: 6.5.0
      conditions:
        - type: ServiceHealthDeployment
          status: "False"
          reason: DeploymentUnhealthy
          message: "1 Deployment unhealthy: podinfo/podinfo (0/1 replicas ready, 1 updated, rule kcm-system/kcm-default-health-rules#0)"
```

Once the 6.6.0 Deployment reaches `1/1 ready`, the verifier promotes the service back to `Deployed`, clears the `ServiceHealth*` condition, and stamps `lastDeployedHash` and `version` to the 6.6.0 fingerprint.
