# k0rdent 1.11.0 Release Notes

**Release date:** July 28, 2026

## Components Versions

| Provider Name                        | Version          |
|--------------------------------------|------------------|
| Cluster API                          | v1.13.4          |
| Cluster API Provider AWS             | v2.12.1          |
| Cluster API Provider Azure           | v1.26.0          |
| Cluster API Provider Docker          | v1.13.4          |
| Cluster API Provider GCP             | v1.12.0          |
| Cluster API Provider Infoblox        | v0.2.2           |
| Cluster API Provider IPAM            | v1.1.0           |
| Cluster API Provider k0smotron       | v2.0.4           |
| Cluster API Provider Kubevirt        | v0.11.2          |
| Cluster API Provider OpenStack (ORC) | v0.14.6 (v2.1.0) |
| Cluster API Provider vSphere         | v1.16.1          |
| Projectsveltos                       | v1.12.0          |
| k0s (control plane runtime)          | v1.36.3          |
| cert-manager (charts)                | v1.21.0          |
| CAPI Operator                        | v0.28.0          |

---

## Highlights

* **Migration to k0smotron v2**: k0rdent 1.11.0 migrates to k0smotron v2.0.4 that contains the new v1beta2 API version
and fully aligned with Cluster API v1beta2. For more details about the migration, see [k0smotron migration to v1beta2 APIs](https://docs.k0smotron.io/stable/update/migrate-v1beta2-api/).

* **Improved Cluster Template Flexibility**: New template enhancements allow zero-worker standalone control plane
deployments, expose etcd storage configuration for hosted control planes making cluster provisioning more versatile.

* **Better Service Lifecycle and Status Reporting**: ServiceSet status now surfaces error messages from ClusterSummary
failures, and fixes to service key collision handling and dependency filtering improve multi-cluster service management
reliability.

* **Audit Policy Distribution**: Building on v1.10.0's audit policy support, this release adds the ability
to distribute `ClusterAuditPolicies` across managed clusters, along with 

* **Improved Auth and Audit-related Secrets and ConfigMaps Cleanup**: k0rdent now properly removes authentication and
audit-related Secrets and ConfigMaps when they are no longer referenced.

* **Periodic CAPI Status Polling**: A new periodic status poller for ClusterDeployments ensures that CAPI resource
status is kept up-to-date improving convergence reliability.

* **Enhanced Resilience and Cleanup**: Transient error retries in watchers, proper orphaned resource cleanup
for provider configs and registry secrets, and safeguards against accidental `dataSource` changes
on ClusterDeployments make operations more robust.

## Upgrade Notes

### k0smotron v2 Migration

This release upgrades k0smotron from the v1beta1 to the v1beta2 API. The default cluster templates have been updated
to use the new API and field naming conventions. If you maintain custom templates that reference k0smotron resources,
review and update them for compatibility.

For migration instructions, see the [k0smotron migration to v1beta2 APIs](https://docs.k0smotron.io/stable/update/migrate-v1beta2-api/).

### Removal of `clusterGVKs` from ProviderInterface

The unused `clusterGVKs` field has been removed from the ProviderInterface API [`feat!: drop unused PI clusterGVKs field`](https://github.com/k0rdent/kcm/pull/2912).

If you have custom ProviderInterface resources that still include this field, remove it before applying them to
a cluster running this release.

---

## Changelog

### New Features

* **feat**: support to distribute ClusterAuditPolicies ([#2890](https://github.com/k0rdent/kcm/pull/2890)) by @eromanova
* **feat**: remote-cluster: expose prestart configuration ([#2898](https://github.com/k0rdent/kcm/pull/2898)) by @asizov
* **feat**: add a flag to remove k0rdent CRDs on management removal ([#2539](https://github.com/k0rdent/kcm/pull/2539)) by @kylewuolle
* **feat!**: drop unused PI clusterGVKs field ([#2912](https://github.com/k0rdent/kcm/pull/2912)) by @mmorgen
* **feat(cld)**: periodic CAPI status poller ([#2816](https://github.com/k0rdent/kcm/pull/2816)) by @mmorgen
* **feat(controller)**: retry transient errs in watchers ([#2789](https://github.com/k0rdent/kcm/pull/2789)) by @mmorgen
* **feat(templates)**: allow 0 workers in standalone-cp charts ([#2785](https://github.com/k0rdent/kcm/pull/2785)) by @mmorgen
* **feat(templates)**: expose storage.etcd.autoDeletePVCs in hosted-cp templates ([#2834](https://github.com/k0rdent/kcm/pull/2834)) by @XDDDaniel

---

### Notable Fixes

* **fix**: properly handle k0smotron service annotations for vsphere hosted ([#2954](https://github.com/k0rdent/kcm/pull/2954)) by @eromanova
* **fix(sveltos)**: insufficient RBAC on upgrade ([#2955](https://github.com/k0rdent/kcm/pull/2955)) by @mmorgen
* **fix**: gcp and kubevirt rendering issues ([#2948](https://github.com/k0rdent/kcm/pull/2948)) by @eromanova
* **fix**: mgmt serviceset should be deleted on mismatch (selfManagement=false) ([#2920](https://github.com/k0rdent/kcm/pull/2920)) by @wahabmk
* **fix**: do not add owner ref to profile when operating on regional clusters ([#2905](https://github.com/k0rdent/kcm/pull/2905)) by @kylewuolle
* **fix**: gke clustertemplate rendering issues ([#2931](https://github.com/k0rdent/kcm/pull/2931)) by @apavlov
* **fix**: addon rendering for EKS ClusterTemplate ([#2933](https://github.com/k0rdent/kcm/pull/2933)) by @apavlov
* **fix**: incorrect serviceAccount field usage in GCPMachineTemplate ([#2929](https://github.com/k0rdent/kcm/pull/2929)) by @apavlov
* **fix(cld)**: missing rbac on delete path ([#2922](https://github.com/k0rdent/kcm/pull/2922)) by @mmorgen
* **fix**: drop dead drift-detection ensure workaround ([#2913](https://github.com/k0rdent/kcm/pull/2913)) by @mmorgen
* **fix(templates)**: trust registry CA regardless of OS ([#2897](https://github.com/k0rdent/kcm/pull/2897)) by @mmorgen
* **fix**: surface errors to ServiceSet status ([#2889](https://github.com/k0rdent/kcm/pull/2889)) by @wahabmk
* **fix**: rename remaining fields after k0smotron v2beta2 migration ([#2887](https://github.com/k0rdent/kcm/pull/2887)) by @eromanova
* **fix**: svc key collisions in FilteredDependencies func ([#2842](https://github.com/k0rdent/kcm/pull/2842)) by @wahabmk
* **fix**: delete auth and audit related secrets and configmaps on ref removal ([#2853](https://github.com/k0rdent/kcm/pull/2853)) by @eromanova
* **fix**: delete orphaned provider config and cld registry secrets ([#2855](https://github.com/k0rdent/kcm/pull/2855)) by @eromanova
* **fix**: disallow enabling or removing ClusterDeployment spec.dataSource ([#2857](https://github.com/k0rdent/kcm/pull/2857)) by @eromanova
* **fix**: omit etcd section when kine is used ([#2852](https://github.com/k0rdent/kcm/pull/2852)) by @apavlov
* **fix**: svc status in ServiceSet to consider new FailureMessage field in ClusterSummary ([#2604](https://github.com/k0rdent/kcm/pull/2604)) by @wahabmk

---

### Platform & Dependency Updates

* **chore**: update k0s to v1.36.3+k0s.0 ([#2964](https://github.com/k0rdent/kcm/pull/2964)) by @eromanova
* **chore(deps)**: bump CAP-A/Z/G ([#2952](https://github.com/k0rdent/kcm/pull/2952)) by @Kshatrix
* **chore**: bump k0smotron to v2.0.4 ([#2950](https://github.com/k0rdent/kcm/pull/2950)) by @eromanova
* **chore(deps)**: bump CAPI-operator from 0.27.0 to 0.28.0 ([#2937](https://github.com/k0rdent/kcm/pull/2937)) by @dependabot
* **chore(deps)**: bump sigs.k8s.io/cluster-api-operator from 0.27.0 to 0.28.0 ([#2935](https://github.com/k0rdent/kcm/pull/2935)) by @dependabot
* **chore(bump)**: flux chart to 2.19.0 ([#2927](https://github.com/k0rdent/kcm/pull/2927)) by @apavlov
* **chore(deps)**: bump sigs.k8s.io/cluster-api from 1.13.3 to 1.13.4 ([#2923](https://github.com/k0rdent/kcm/pull/2923)) by @dependabot
* **chore(deps)**: bump go modules and charts ([#2917](https://github.com/k0rdent/kcm/pull/2917)) by @mmorgen
* **chore(deps)**: bump github.com/fluxcd/source-controller/api ([#2918](https://github.com/k0rdent/kcm/pull/2918)) by @dependabot
* **chore(deps)**: bump helm.sh/helm/v3 from 3.21.2 to 3.21.3 ([#2914](https://github.com/k0rdent/kcm/pull/2914)) by @dependabot
* **chore(deps)**: bump github.com/cert-manager/cert-manager ([#2907](https://github.com/k0rdent/kcm/pull/2907)) by @dependabot
* **chore(deps)**: bump golang.org/x/net from 0.56.0 to 0.57.0 ([#2909](https://github.com/k0rdent/kcm/pull/2909)) by @dependabot
* **chore(deps)**: bump github.com/google/cel-go from 0.29.1 to 0.29.2 ([#2903](https://github.com/k0rdent/kcm/pull/2903)) by @dependabot
* **chore(deps)**: bump golang.org/x/text from 0.39.0 to 0.40.0 ([#2904](https://github.com/k0rdent/kcm/pull/2904)) by @dependabot
* **chore(deps)**: bump github.com/fluxcd/source-controller/api ([#2899](https://github.com/k0rdent/kcm/pull/2899)) by @dependabot
* **chore(deps)**: bump github.com/fluxcd/helm-controller/api ([#2900](https://github.com/k0rdent/kcm/pull/2900)) by @dependabot
* **chore(deps)**: bump k0smotron from 2.0.2 to 2.0.3 ([#2895](https://github.com/k0rdent/kcm/pull/2895)) by @dependabot
* **chore(deps)**: bump golang.org/x/text from 0.38.0 to 0.39.0 ([#2893](https://github.com/k0rdent/kcm/pull/2893)) by @dependabot
* **chore(deps)**: bump github.com/google/cel-go from 0.28.1 to 0.29.1 ([#2880](https://github.com/k0rdent/kcm/pull/2880)) by @dependabot
* **chore(deps)**: bump github.com/fluxcd/source-controller/api from 1.8.5 to 1.9.1 ([#2876](https://github.com/k0rdent/kcm/pull/2876)) by @dependabot
* **chore(deps)**: bump github.com/fluxcd/helm-controller/api ([#2872](https://github.com/k0rdent/kcm/pull/2872)) by @dependabot
* **chore(bump)**: openstack-provider to v0.14.6 ([#2864](https://github.com/k0rdent/kcm/pull/2864)) by @Kshatrix
* **chore(bump)**: azure-provider to v1.25.1 ([#2861](https://github.com/k0rdent/kcm/pull/2861)) by @Kshatrix
* **chore**: migrate to k0smotron v2.0.2 ([#2807](https://github.com/k0rdent/kcm/pull/2807)) by @eromanova
* **chore(deps)**: bump github.com/vmware-tanzu/velero from 1.18.1 to 1.18.2 ([#2859](https://github.com/k0rdent/kcm/pull/2859)) by @dependabot
* **chore**: update k0s version to v1.36.1+k0s.0 ([#2843](https://github.com/k0rdent/kcm/pull/2843)) by @eromanova
* **chore(deps)**: bump github.com/cert-manager/cert-manager ([#2856](https://github.com/k0rdent/kcm/pull/2856)) by @dependabot
* **chore(deps)**: bump github.com/onsi/gomega from 1.42.0 to 1.42.1 ([#2854](https://github.com/k0rdent/kcm/pull/2854)) by @dependabot
* **chore(bump)**: capi to v1.13.3 ([#2850](https://github.com/k0rdent/kcm/pull/2850)) by @Kshatrix
* **chore(deps)**: bump sigs.k8s.io/cluster-api from 1.13.2 to 1.13.3 ([#2848](https://github.com/k0rdent/kcm/pull/2848)) by @dependabot
* **chore(deps)**: bump github.com/containerd/containerd ([#2847](https://github.com/k0rdent/kcm/pull/2847)) by @dependabot
* **chore(deps)**: bump github.com/onsi/ginkgo/v2 from 2.31.0 to 2.32.0 ([#2845](https://github.com/k0rdent/kcm/pull/2845)) by @dependabot
* **chore(deps)**: bump helm.sh/helm/v3 from 3.21.1 to 3.21.2 ([#2846](https://github.com/k0rdent/kcm/pull/2846)) by @dependabot
* **chore(deps)**: bump github.com/fluxcd/helm-controller/api ([#2832](https://github.com/k0rdent/kcm/pull/2832)) by @dependabot
* **chore**: bump k0smotron to v1.10.8 ([#2829](https://github.com/k0rdent/kcm/pull/2829)) by @eromanova
* **chore(deps)**: bump kubevirt.io/api from 1.8.3 to 1.8.4 ([#2826](https://github.com/k0rdent/kcm/pull/2826)) by @dependabot
* **chore(deps)**: bump github.com/onsi/ginkgo/v2 from 2.30.0 to 2.31.0 ([#2825](https://github.com/k0rdent/kcm/pull/2825)) by @dependabot
* **chore(deps)**: bump k8s.io/kubectl from 0.36.1 to 0.36.2 ([#2822](https://github.com/k0rdent/kcm/pull/2822)) by @dependabot
* **chore(deps)**: bump k8s.io/apiserver from 0.36.1 to 0.36.2 ([#2823](https://github.com/k0rdent/kcm/pull/2823)) by @dependabot
* **chore(deps)**: bump github.com/onsi/gomega from 1.41.0 to 1.42.0 ([#2821](https://github.com/k0rdent/kcm/pull/2821)) by @dependabot
* **chore(deps)**: bump github.com/fluxcd/pkg/runtime from 0.108.0 to 0.110.0 ([#2817](https://github.com/k0rdent/kcm/pull/2817)) by @dependabot
* **chore(deps)**: bump helm.sh/helm/v3 from 3.21.0 to 3.21.1 ([#2818](https://github.com/k0rdent/kcm/pull/2818)) by @dependabot
* **chore(deps)**: bump github.com/fluxcd/pkg/apis/meta from 1.29.0 to 1.30.0 ([#2819](https://github.com/k0rdent/kcm/pull/2819)) by @dependabot
* **chore(deps)**: bump github.com/onsi/ginkgo/v2 from 2.29.0 to 2.30.0 ([#2814](https://github.com/k0rdent/kcm/pull/2814)) by @dependabot
* **chore(deps)**: bump golang.org/x/net from 0.55.0 to 0.56.0 ([#2811](https://github.com/k0rdent/kcm/pull/2811)) by @dependabot
* **chore(deps)**: bump golang.org/x/crypto from 0.52.0 to 0.53.0 ([#2805](https://github.com/k0rdent/kcm/pull/2805)) by @dependabot
* **chore(deps)**: bump github.com/fluxcd/pkg/runtime from 0.107.0 to 0.108.0 ([#2798](https://github.com/k0rdent/kcm/pull/2798)) by @dependabot
* **chore(deps)**: bump kubevirt.io/api from 1.8.2 to 1.8.3 ([#2791](https://github.com/k0rdent/kcm/pull/2791)) by @dependabot
* **chore(deps)**: bump github.com/prometheus/client_golang ([#2940](https://github.com/k0rdent/kcm/pull/2940)) by @dependabot
* **chore(deps)**: bump github.com/fluxcd/pkg/runtime from 0.110.0 to 0.111.0 ([#2867](https://github.com/k0rdent/kcm/pull/2867)) by @dependabot
* **chore(deps)**: bump github.com/fluxcd/pkg/apis/meta from 1.30.0 to 1.31.0 ([#2868](https://github.com/k0rdent/kcm/pull/2868)) by @dependabot
* **chore**: mgmt cleanup omitzero; deps bumps ([#2925](https://github.com/k0rdent/kcm/pull/2925)) by @mmorgen

---

### Other Changes (CI, Tests, Refactors)

* **refactor**: retire legacy paths ([#2944](https://github.com/k0rdent/kcm/pull/2944)) by @mmorgen
* **ci**: update release branch naming pattern ([#2951](https://github.com/k0rdent/kcm/pull/2951)) by @eromanova
* **ci(e2e)**: drop unused caching due to pr_target ([#2938](https://github.com/k0rdent/kcm/pull/2938)) by @mmorgen
* **refactor**: drop PI lookup on CD delete path ([#2901](https://github.com/k0rdent/kcm/pull/2901)) by @mmorgen
* **ci**: overhaul e2e matrix, staging, vsphere nuke ([#2875](https://github.com/k0rdent/kcm/pull/2875)) by @mmorgen
* **test**: adapt validation functions to handle k0smotron v1beta2 ([#2871](https://github.com/k0rdent/kcm/pull/2871)) by @eromanova
* **ci**: restructure pipelines, harden secrets boundary ([#2815](https://github.com/k0rdent/kcm/pull/2815)) by @mmorgen
* **test(e2e)**: fail fast on stuck cluster deletion ([#2794](https://github.com/k0rdent/kcm/pull/2794)) by @mmorgen

---

## References

* [Compare KCM v1.10.0...v1.11.0](https://github.com/k0rdent/kcm/compare/v1.10.0...v1.11.0)
