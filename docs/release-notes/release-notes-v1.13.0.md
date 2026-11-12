# k0rdent 1.13.0 Release Notes

**Release date:** November 12, 2026

## Components Versions

| Provider Name                        | Version          |
|--------------------------------------|------------------|
| Cluster API                          | v1.14.3          |
| Cluster API Provider AWS             | v2.13.0          |
| Cluster API Provider Azure           | v1.26.0          |
| Cluster API Provider Docker          | v1.14.3          |
| Cluster API Provider GCP             | v1.13.1          |
| Cluster API Provider Infoblox        | v0.2.2           |
| Cluster API Provider IPAM            | v1.1.0           |
| Cluster API Provider k0smotron       | v2.3.1           |
| Cluster API Provider Kubevirt        | v0.11.2          |
| Cluster API Provider OpenStack (ORC) | v0.14.7 (v2.1.0) |
| Cluster API Provider vSphere         | v1.16.1          |
| Projectsveltos                       | v1.16.0          |
| k0s (control plane runtime)          | v1.36.3          |
| cert-manager (charts)                | v1.21.3          |
| CAPI Operator                        | v0.30.0          |

---

## Highlights

* **Cluster API In-Place Updates**: Worker machines of k0s-based clusters can now be updated in place when only the
k0s version changes, instead of being replaced. The feature is enabled with the `controller.enableInPlaceUpdates`
KCM setting, which configures the Cluster API core provider and the k0smotron provider for the `Management` object
and every `Region`. See [Configuring Cluster API In-Place Updates](../appendix/appendix-extend-mgmt.md#configuring-cluster-api-in-place-updates).

* **In-Place Version Updates with the Delete-First Strategy**: The new `controller.enableInPlaceVersionWithDeleteFirst`
KCM setting enables the experimental k0smotron `InPlaceVersionWithDeleteFirst` feature gate. k0s version-only changes
of a `K0sControlPlane` are applied in place, while other changes replace the control plane machines with the
`RecreateDeleteFirst` strategy. See
[Combining in-place version updates with the delete-first strategy](../appendix/appendix-extend-mgmt.md#combining-in-place-version-updates-with-the-delete-first-strategy).

* **Patches from ConfigMaps and Secrets**: Services can now reference ConfigMaps or Secrets with Kustomize inline
patches through the new `patchesFrom` field. The patches are applied to the rendered manifests of the service and
support Go templates. See [ServiceTemplate Parameters](../user/services/servicetemplate-parameters.md).

* **ClusterTemplate Distribution with AccessManagement**: `ClusterTemplate` is now a built-in `AccessManagement` Kind,
so individual templates can be distributed to other namespaces without a `ClusterTemplateChain`. Distributed objects
now have an owner reference to the `AccessManagement` object, so they are garbage-collected when it is deleted. See
[AccessManagement](../admin/access/accessmanagement.md).

* **Reliable Service Upgrade Ordering**: `dependsOn` now orders upgrades as well as the initial rollout. A service is
not upgraded until the services it depends on, directly, transitively or in another `MultiClusterService`, have been
upgraded to their desired versions. Deleting a `MultiClusterService` whose services form a `dependsOn` chain no
longer gets stuck, because Projectsveltos v1.16.0 uninstalls the services in the reverse of the installation order.

* **Remote Cluster Control Plane Address**: The `remote-cluster` template exposes the new `k0smotron.externalAddress`
and `k0s.api.sans` parameters, so a control plane exposed through NAT or a floating IP can be advertised on a
routable address that works for joining workers and in the generated kubeconfig. See
[Remote machine parameters](../reference/template/template-remote.md).

* **Platform Updates**: Cluster API v1.14.3, k0smotron v2.3.1, Projectsveltos v1.16.0, CAPI Operator v0.30.0,
cert-manager v1.21.3 and Flux v2.19.1.

## Upgrade Notes

### Stricter API Validation

The {{{ docsVersionInfo.k0rdentName }}} API types are now checked with the Kubernetes API Linter, and the
CustomResourceDefinitions have stricter OpenAPI validation. Among other changes:

* `spec` is required for `ClusterAuthentication`, `ClusterIPAM`, `ClusterIPAMClaim`, `ClusterTemplate`,
  `Management`, `ProviderTemplate`, `Release`, `ServiceSet`, `ServiceTemplate` and `StateManagementProvider` objects.
* Many optional string fields must be non-empty when set, and many lists have minimum and maximum lengths. For example,
  the `names` and `targetNamespaces.list` lists of the `AccessManagement` access rules must not be empty when set, and
  each name in them is limited to 512 characters.

Objects that are already stored are not revalidated, but creating or updating objects with empty strings or empty
lists in such fields is rejected. Review your manifests and remove empty values for fields you do not set.

### ClusterDeployment Provisioning Timeout Removed

A `ClusterDeployment` no longer switches its `Ready` condition from `Progressing` to `Failed` after its Cluster API
cluster has not been ready for 30 minutes. It now stays `Progressing` and shows the message of the not-ready Cluster
API condition for as long as provisioning takes. If you relied on the `Failed` reason to detect stuck provisioning,
use your own timeout instead.

### Helm Options of Services

The `helmOptions.atomic: true` option is no longer enforced for the Projectsveltos profiles created for services. The
workaround is not needed since Projectsveltos v1.14.0 fixed unintended service reinstallation after a failed upgrade.
Set `atomic: true` explicitly in `helmOptions` if you rely on the rollback on failure.

### Installation Retries of KCM Components

The installation of KCM components through Flux `HelmRelease` objects is now retried indefinitely instead of failing
after three attempts, and the automatic remediation of the last failed attempt is removed. Investigate and fix
installation failures of the components manually.

### Deleting System ClusterTemplates

A `ClusterTemplate` in the system namespace can no longer be deleted while copies distributed by a
`ClusterTemplateChain` or an `AccessManagement` object still reference its `HelmChart`. Stop distributing the template
first.

---

## Changelog

### New Features

* **feat**: enable k0smotron InPlaceVersionWithDeleteFirst feature gate ([#3171](https://github.com/k0rdent/kcm/pull/3171)) by @Kshatrix
* **feat**: distribute ClusterTemplate as a built-in AccessManagement kind ([#3148](https://github.com/k0rdent/kcm/pull/3148)) by @Kshatrix
* **feat**: add patchesFrom field to allow using configmaps as a source of patches ([#3104](https://github.com/k0rdent/kcm/pull/3104)) by @kylewuolle
* **feat**: remote-cluster: expose control plane externalAddress and API SANs ([#3093](https://github.com/k0rdent/kcm/pull/3093)) by @valentynkhalin
* **feat**: enable inplace workers update ([#3087](https://github.com/k0rdent/kcm/pull/3087)) by @zerospiel
* **feat**: introduce KAL ([#3014](https://github.com/k0rdent/kcm/pull/3014)) by @zerospiel

---

### Notable Fixes

* **fix(webhook)**: forbid removing a system ClusterTemplate with distributed copies ([#3149](https://github.com/k0rdent/kcm/pull/3149)) by @Kshatrix
* **fix(ksm)**: resolve cross-MCS dependsOn desired versions in the ServiceSet namespace ([#3141](https://github.com/k0rdent/kcm/pull/3141)) by @wahabmk
* **fix**: remove finalizer from SveltosCluster manually ([#3121](https://github.com/k0rdent/kcm/pull/3121)) by @wahabmk
* **fix**: drop hardcoded CAPI provisioning timeout for ClusterDeployment ([#3133](https://github.com/k0rdent/kcm/pull/3133)) by @eromanova
* **fix**: wait for control plane initialization before syncing RBACPolicy ([#3112](https://github.com/k0rdent/kcm/pull/3112)) by @eromanova
* **fix(ksm)**: deploy sveltos 1.16.0 so a dependsOn chain can be deleted ([#3109](https://github.com/k0rdent/kcm/pull/3109)) by @josef-hak
* **fix(ksm)**: gate cross-MCS dependsOn on versions, not just Deployed ([#3085](https://github.com/k0rdent/kcm/pull/3085)) by @josef-hak
* **fix(telemetry)**: hardcode leader-elect-id to enable FIPS ([#3100](https://github.com/k0rdent/kcm/pull/3100)) by @zerospiel
* **fix(ksm)**: an unchanged service must not unlock what depends on it ([#3081](https://github.com/k0rdent/kcm/pull/3081)) by @josef-hak
* **fix(helm)**: remove remediation; infinite retries ([#3091](https://github.com/k0rdent/kcm/pull/3091)) by @zerospiel
* **fix(ksm)**: keep polling a ServiceSet whose version stamp is still owed ([#3088](https://github.com/k0rdent/kcm/pull/3088)) by @josef-hak
* **fix(am)**: add ownerReference to distributed objects ([#3084](https://github.com/k0rdent/kcm/pull/3084)) by @eromanova
* **fix**: do not enforce atomic helm option ([#3080](https://github.com/k0rdent/kcm/pull/3080)) by @BROngineer

---

### Platform & Dependency Updates

* **chore(deps)**: bump cel.dev/cel-go from 0.32.0 to 0.33.0 ([#3174](https://github.com/k0rdent/kcm/pull/3174)) by @dependabot
* **chore(bump)**: k0smotron to v2.3.1 ([#3170](https://github.com/k0rdent/kcm/pull/3170)) by @Kshatrix
* **chore(bump)**: flux to v2.19.1 ([#3163](https://github.com/k0rdent/kcm/pull/3163)) by @Kshatrix
* **chore(deps)**: bump github.com/fluxcd/pkg/runtime from 0.120.0 to 0.122.0 ([#3154](https://github.com/k0rdent/kcm/pull/3154)) by @dependabot
* **chore(bump)**: capi operator to v0.30.0 ([#3161](https://github.com/k0rdent/kcm/pull/3161)) by @Kshatrix
* **chore(deps)**: bump github.com/fluxcd/pkg/apis/meta from 1.36.0 to 1.38.0 ([#3157](https://github.com/k0rdent/kcm/pull/3157)) by @dependabot
* **chore(bump)**: cert-manager to v1.21.3 ([#3159](https://github.com/k0rdent/kcm/pull/3159)) by @Kshatrix
* **chore(deps)**: bump github.com/cert-manager/cert-manager ([#3155](https://github.com/k0rdent/kcm/pull/3155)) by @dependabot
* **chore(deps)**: bump sigs.k8s.io/cluster-api-operator from 0.29.0 to 0.30.0 ([#3151](https://github.com/k0rdent/kcm/pull/3151)) by @dependabot
* **chore(deps)**: bump go from 1.27.1 to 1.27.3; golangci-lint from 2.13.2 to 2.15.0 ([#3147](https://github.com/k0rdent/kcm/pull/3147)) by @zerospiel
* **chore(deps)**: bump k0smotron provider from 2.2.0 to 2.3.0 ([#3143](https://github.com/k0rdent/kcm/pull/3143)) by @zerospiel
* **chore(deps)**: bump helm.sh/helm/v3 from 3.22.0 to 3.22.1 ([#3138](https://github.com/k0rdent/kcm/pull/3138)) by @dependabot
* **chore(deps)**: bump github.com/fluxcd/pkg/runtime from 0.116.0 to 0.120.0 ([#3139](https://github.com/k0rdent/kcm/pull/3139)) by @dependabot
* **chore(bump)**: capi to v1.14.3 ([#3131](https://github.com/k0rdent/kcm/pull/3131)) by @Kshatrix
* **chore(deps)**: bump kubevirt.io/api from 1.9.0 to 1.9.1 ([#3128](https://github.com/k0rdent/kcm/pull/3128)) by @dependabot
* **chore(deps)**: bump github.com/onsi/ginkgo/v2 from 2.33.0 to 2.33.1 ([#3127](https://github.com/k0rdent/kcm/pull/3127)) by @dependabot
* **chore(deps)**: bump github.com/fluxcd/pkg/runtime from 0.115.0 to 0.116.0 ([#3126](https://github.com/k0rdent/kcm/pull/3126)) by @dependabot
* **chore(deps)**: bump github.com/prometheus/client_golang ([#3122](https://github.com/k0rdent/kcm/pull/3122)) by @dependabot
* **chore(deps)**: bump golang.org/x/net from 0.59.0 to 0.61.0 ([#3124](https://github.com/k0rdent/kcm/pull/3124)) by @dependabot
* **chore(deps)**: bump sigs.k8s.io/cluster-api from 1.14.2 to 1.14.3 ([#3118](https://github.com/k0rdent/kcm/pull/3118)) by @dependabot
* **chore(deps)**: bump sigs.k8s.io/cluster-api/api from 1.14.2 to 1.14.3 ([#3117](https://github.com/k0rdent/kcm/pull/3117)) by @dependabot
* **chore(deps)**: bump golang.org/x/sync from 0.23.0 to 0.24.0 ([#3116](https://github.com/k0rdent/kcm/pull/3116)) by @dependabot
* **chore(deps)**: bump github.com/fluxcd/helm-controller/api ([#3111](https://github.com/k0rdent/kcm/pull/3111)) by @dependabot
* **chore(deps)**: bump github.com/fluxcd/pkg/runtime from 0.114.0 to 0.115.0 ([#3108](https://github.com/k0rdent/kcm/pull/3108)) by @dependabot
* **chore(deps)**: bump github.com/segmentio/analytics-go/v3 ([#3102](https://github.com/k0rdent/kcm/pull/3102)) by @dependabot
* **chore(deps)**: bump github.com/onsi/gomega from 1.43.1 to 1.44.0 ([#3098](https://github.com/k0rdent/kcm/pull/3098)) by @dependabot
* **chore(deps)**: bump k8s.io/kubectl from 0.37.0 to 0.37.1 ([#3097](https://github.com/k0rdent/kcm/pull/3097)) by @dependabot
* **chore(deps)**: bump k0smotron provider from 2.1.1 to 2.2.0 ([#3096](https://github.com/k0rdent/kcm/pull/3096)) by @zerospiel
* **chore(deps)**: bump github.com/vmware-tanzu/velero from 1.18.3 to 1.18.4 ([#3094](https://github.com/k0rdent/kcm/pull/3094)) by @dependabot
* **chore(deps)**: bump k8s.io/apiserver from 0.37.0 to 0.37.1 ([#3092](https://github.com/k0rdent/kcm/pull/3092)) by @dependabot
* **chore(go)**: 1.27.1; bump deps ([#3086](https://github.com/k0rdent/kcm/pull/3086)) by @zerospiel
* **chore(deps)**: bump github.com/onsi/gomega from 1.43.0 to 1.43.1 ([#3082](https://github.com/k0rdent/kcm/pull/3082)) by @dependabot
* **chore(deps)**: bump github.com/onsi/ginkgo/v2 from 2.32.2 to 2.33.0 ([#3079](https://github.com/k0rdent/kcm/pull/3079)) by @dependabot

---

### Other Changes (CI, Tests, Refactors)

* **chore(deps)**: bump docker/login-action ([#3156](https://github.com/k0rdent/kcm/pull/3156)) by @dependabot
* **chore(deps)**: bump goreleaser/goreleaser-action ([#3129](https://github.com/k0rdent/kcm/pull/3129)) by @dependabot
* **chore(deps)**: bump actions/upload-artifact ([#3125](https://github.com/k0rdent/kcm/pull/3125)) by @dependabot
* **chore(deps)**: bump azure/setup-kubectl ([#3119](https://github.com/k0rdent/kcm/pull/3119)) by @dependabot
* **chore(deps)**: bump mikefarah/yq ([#3103](https://github.com/k0rdent/kcm/pull/3103)) by @dependabot
* **ci**: skip GitHub release and changelog for -dev tags ([#3099](https://github.com/k0rdent/kcm/pull/3099)) by @eromanova
* **test(e2e)**: drop the specs k0rdent/ksm-tests now covers ([#3095](https://github.com/k0rdent/kcm/pull/3095)) by @josef-hak
* **ci**: run the KSM scenarios on pull requests ([#3090](https://github.com/k0rdent/kcm/pull/3090)) by @josef-hak
* **chore(deps)**: bump docker/setup-buildx-action ([#3078](https://github.com/k0rdent/kcm/pull/3078)) by @dependabot

---

## References

* [Compare KCM v1.12.0...v1.13.0](https://github.com/k0rdent/kcm/compare/v1.12.0...v1.13.0)
