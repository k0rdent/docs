# k0rdent 1.10.0 Release Notes

**Release date:** June 8, 2026

## Components Versions

| Provider Name                        | Version          |
|--------------------------------------|------------------|
| Cluster API                          | v1.13.2          |
| Cluster API Provider AWS             | v2.11.1          |
| Cluster API Provider Azure           | v1.24.1          |
| Cluster API Provider Docker          | v1.13.2          |
| Cluster API Provider GCP             | v1.11.2          |
| Cluster API Provider Infoblox        | v0.1.0           |
| Cluster API Provider IPAM            | v1.1.0-rc.1      |
| Cluster API Provider k0smotron       | v1.10.6          |
| Cluster API Provider Kubevirt        | v0.11.2          |
| Cluster API Provider OpenStack (ORC) | v0.14.4 (v2.1.0) |
| Cluster API Provider vSphere         | v1.16.1          |
| Projectsveltos                       | v1.9.0           |
| k0s (control plane runtime)          | v1.35.4          |
| cert-manager (charts)                | v1.20.2          |

---

## Highlights

* **Stronger Security Baselines for New Clusters**: k0rdent 1.10.0 adds audit policy support and template-level etcd encryption configuration, helping platform teams apply security and compliance controls earlier in the cluster lifecycle instead of relying on post-deployment hardening.

* **Safer Multi-Cluster Service Changes**: Improvements to `ServiceSet` and `MultiClusterService` make service rollout status easier to understand and reduce disruption when selectors change. Operators can now keep already deployed services in place while adjusting targeting logic, which lowers the risk of accidental service removal during routine changes.

* **More Reliable Cluster Template Behavior**: Fixes to default template handling, MachineDeployment versioning, OpenStack floating IP pool references, and values merging make cluster deployments more consistent across environments. These changes reduce configuration drift and help prevent avoidable deployment failures.

* **Better Scheduling and Availability Controls for k0rdent Components**: Chart updates add support for `priorityClassName` and topology spread constraints, giving operators more control over how k0rdent components run in production Kubernetes environments.

* **Smoother Upgrades and More Predictable Convergence**: Upgrade-related fixes, semver-based version comparison, dependency handling, and controller reconcile optimizations improve the reliability of day-2 operations. The result is less controller noise, fewer edge-case failures, and clearer behavior during upgrades and reconciliation.

* **Updated Platform Foundation**: This release refreshes core providers and dependencies, including Cluster API, major infrastructure providers, Projectsveltos, k0s, and cert-manager, keeping k0rdent aligned with the current Kubernetes ecosystem while incorporating upstream fixes and compatibility improvements.

## Upgrade Notes

### k0rdent Observability an Finance (KOF)

KOF v1.10.0 introduces:

* [Regionless](../admin/kof/kof-storing.md#regionless) setup option.
  There are no regional clusters in this case.
  Child clusters send metrics/logs/traces to the management cluster for storage.
* Simplified [From Management to Management](../admin/kof/kof-storing.md#from-management-to-management) (M2M)
  and  [From Management to Regional](../admin/kof/kof-storing.md#from-management-to-regional) (M2R) options.
  Note that `kof-storage`/`kof-collectors` are removed from `kof` umbrella chart in favor of dynamic M2M option.
* [Audit logs](../admin/kof/kof-retention.md/#audit-logs).
* S3-compatible cold storage exporter.
* File storage to persist export data.
* Aggregation and multi-tenancy for traces.
* Vlogxy is replaced with VLCluster multi-level selection.
* Example of opentelemetry SDK usage in kof-operator.

---

## Changelog


Here’s the structured conversion with proper categorization (and deduping where needed):

---

### New Features

* **feat**: audit policy support ([#2723](https://github.com/k0rdent/kcm/pull/2723)) by @eromanova
* **feat**: add `<deployed>/<total>` services printcolumn to ServiceSet ([#2760](https://github.com/k0rdent/kcm/pull/2760)) by @wahabmk
* **feat**: allow to keep deployed services when changing MultiClusterService selector ([#2715](https://github.com/k0rdent/kcm/pull/2715)) by @BROngineer
* **feat(template):** allow to disable ingress deployment ([#2719](https://github.com/k0rdent/kcm/pull/2719)) by @uwej711
* **feat(templates):** add etcd encryption config ([#2704](https://github.com/k0rdent/kcm/pull/2704)) by @zerospiel
* **feat**: support topology spread constraints in kcm chart ([#2691](https://github.com/k0rdent/kcm/pull/2691)) by @Danil-Grigorev

---

### Notable Fixes

* **fix:** proper aso version for capz ([#2787](https://github.com/k0rdent/kcm/pull/2787)) by @a13x5
* **fix:** sequential upgrades pick dead-end branches ([#2693](https://github.com/k0rdent/kcm/pull/2693)) by @kylewuolle
* **fix:** make ServicesInReady condition true when 0 services ([#2764](https://github.com/k0rdent/kcm/pull/2764)) by @wahabmk
* **fix:** update helmController image to v1.5.5 ([#2775](https://github.com/k0rdent/kcm/pull/2775)) by @eromanova
* **fix(charts):** pin vsphere-cpi Helm chart to 1.35.1 ([#2758](https://github.com/k0rdent/kcm/pull/2758)) by @Oleksandr Shepotinnik
* **fix:** change Deployed comment to indicate if all services were deployed ([#2754](https://github.com/k0rdent/kcm/pull/2754)) by @wahabmk
* **fix:** ensure kcm helm chart is updated while dev-upgrade ([#2748](https://github.com/k0rdent/kcm/pull/2748)) by @eromanova
* **fix:** support priorityClassName in kcm chart ([#2746](https://github.com/k0rdent/kcm/pull/2746)) by @vikramhh
* **fix(templates):** add missing MachineDeployment version ([#2742](https://github.com/k0rdent/kcm/pull/2742)) by @kristiangronas
* **fix(templates):** add openstack floatingippoolref ([#2741](https://github.com/k0rdent/kcm/pull/2741)) by @bnallapeta
* **fix:** respect dependsOn on upgrades ([#2714](https://github.com/k0rdent/kcm/pull/2714)) by @BROngineer
* **fix(templates):** update CAPI resources ([#2732](https://github.com/k0rdent/kcm/pull/2732)) by @zerospiel
* **fix(templates):** proper merge user and defaults vals ([#2722](https://github.com/k0rdent/kcm/pull/2722)) by @zerospiel
* **fix:** number of total and deployed services ([#2717](https://github.com/k0rdent/kcm/pull/2717)) by @BROngineer
* **fix(am):** filter namespace watch reconciles ([#2695](https://github.com/k0rdent/kcm/pull/2695)) by @zerospiel
* **fix:** too many files open error in kind cluster while testing ([#2689](https://github.com/k0rdent/kcm/pull/2689)) by @wahabmk
* **fix:** mcs status not persisting for delete ([#2690](https://github.com/k0rdent/kcm/pull/2690)) by @wahabmk
* **fix:** change version compare to use semver ([#2662](https://github.com/k0rdent/kcm/pull/2662)) by @kylewuolle

---

### Platform & Dependency Updates

* **chore:** update default k0s version to v1.35.4 ([#2782](https://github.com/k0rdent/kcm/pull/2782)) by @eromanova
* **chore(deps):** bump sigs.k8s.io/cluster-api-ipam-provider-in-cluster ([#2778](https://github.com/k0rdent/kcm/pull/2778)) by @dependabot
* **chore(deps):** bump github.com/fluxcd/pkg/runtime from 0.106.0 to 0.107.0 ([#2779](https://github.com/k0rdent/kcm/pull/2779)) by @dependabot
* **chore(bump):** azure provider to v1.24.1 ([#2771](https://github.com/k0rdent/kcm/pull/2771)) by @Kshatrix
* **chore(deps):** bump golang.org/x/crypto from 0.51.0 to 0.52.0 ([#2768](https://github.com/k0rdent/kcm/pull/2768)) by @dependabot
* **chore(deps):** bump docker/login-action from 4.1.0 to 4.2.0 ([#2766](https://github.com/k0rdent/kcm/pull/2766)) by @dependabot
* **chore(deps):** bump github.com/fluxcd/pkg/apis/meta from 1.27.0 to 1.28.0 ([#2767](https://github.com/k0rdent/kcm/pull/2767)) by @dependabot
* **chore(deps):** bump golang.org/x/net from 0.54.0 to 0.55.0 ([#2769](https://github.com/k0rdent/kcm/pull/2769)) by @dependabot
* **chore(deps):** bump github.com/containerd/containerd ([#2762](https://github.com/k0rdent/kcm/pull/2762)) by @dependabot
* **chore(deps):** bump github.com/fluxcd/source-controller/api ([#2755](https://github.com/k0rdent/kcm/pull/2755)) by @dependabot
* **chore(deps):** bump github.com/telekom/cluster-api-ipam-provider-infoblox ([#2756](https://github.com/k0rdent/kcm/pull/2756)) by @dependabot
* **chore(deps):** bump github.com/fluxcd/helm-controller/api ([#2757](https://github.com/k0rdent/kcm/pull/2757)) by @dependabot
* **chore(deps):** bump github.com/vmware-tanzu/velero from 1.18.0 to 1.18.1 ([#2753](https://github.com/k0rdent/kcm/pull/2753)) by @dependabot
* **chore(deps):** bump github.com/onsi/gomega from 1.40.0 to 1.41.0 ([#2750](https://github.com/k0rdent/kcm/pull/2750)) by @dependabot
* **chore(deps):** bump github.com/onsi/ginkgo/v2 from 2.28.3 to 2.29.0 ([#2752](https://github.com/k0rdent/kcm/pull/2752)) by @dependabot
* **chore(templates):** bump chart versions and align values overrides ([#2700](https://github.com/k0rdent/kcm/pull/2700)) by @oshep
* **chore(deps):** bump github.com/telekom/cluster-api-ipam-provider-infoblox ([#2745](https://github.com/k0rdent/kcm/pull/2745)) by @dependabot
* **chore(deps):** bumps CAPI (1.13.2) and CAPI Operator (0.27.0) ([#2743](https://github.com/k0rdent/kcm/pull/2743)) by @dependabot
* **chore(deps):** bump helm.sh/helm/v3 from 3.20.2 to 3.21.0 ([#2739](https://github.com/k0rdent/kcm/pull/2739)) by @dependabot
* **chore(deps):** bump k8s.io/apiserver from 0.36.0 to 0.36.1 ([#2735](https://github.com/k0rdent/kcm/pull/2735)) by @dependabot
* **chore(deps):** bump k8s.io/kubectl from 0.36.0 to 0.36.1 ([#2733](https://github.com/k0rdent/kcm/pull/2733)) by @dependabot
* **chore(bump):** vsphere provider to v1.16.1 ([#2730](https://github.com/k0rdent/kcm/pull/2730)) by @Kshatrix
* **chore(bump):** gcp provider to v1.11.2 ([#2729](https://github.com/k0rdent/kcm/pull/2729)) by @Kshatrix
* **chore(bump):** capi to v1.31.1 ([#2728](https://github.com/k0rdent/kcm/pull/2728)) by @Kshatrix
* **chore(deps):** bump sigs.k8s.io/cluster-api-operator from 0.26.0 to 0.27.0 ([#2727](https://github.com/k0rdent/kcm/pull/2727)) by @dependabot
* **chore(deps):** bump github.com/fluxcd/source-controller/api ([#2725](https://github.com/k0rdent/kcm/pull/2725)) by @dependabot
* **chore(deps):** bump github.com/google/cel-go from 0.28.0 to 0.28.1 ([#2726](https://github.com/k0rdent/kcm/pull/2726)) by @dependabot
* **chore(deps):** bump github.com/fluxcd/pkg/runtime from 0.105.0 to 0.106.0 ([#2706](https://github.com/k0rdent/kcm/pull/2706)) by @dependabot
* **chore:** Bump sveltos to 1.9.0 ([#2718](https://github.com/k0rdent/kcm/pull/2718)) by @wahabmk
* **chore(deps):** bump golang.org/x/net from 0.53.0 to 0.54.0 ([#2720](https://github.com/k0rdent/kcm/pull/2720)) by @dependabot
* **chore(deps):** bump golang.org/x/crypto from 0.50.0 to 0.51.0 ([#2721](https://github.com/k0rdent/kcm/pull/2721)) by @dependabot
* **chore(deps):** bump golang.org/x/text from 0.36.0 to 0.37.0 ([#2708](https://github.com/k0rdent/kcm/pull/2708)) by @dependabot
* **chore(deps):** bump github.com/fluxcd/pkg/apis/meta from 1.26.0 to 1.27.0 ([#2707](https://github.com/k0rdent/kcm/pull/2707)) by @dependabot
* **chore(deps):** bump github.com/Masterminds/semver/v3 from 3.4.0 to 3.5.0 ([#2688](https://github.com/k0rdent/kcm/pull/2688)) by @dependabot
* **chore(deps):** bump sigs.k8s.io/cluster-api-ipam-provider-in-cluster ([#2680](https://github.com/k0rdent/kcm/pull/2680)) by @dependabot
* **chore(deps):** bump github.com/onsi/ginkgo/v2 from 2.28.2 to 2.28.3 ([#2685](https://github.com/k0rdent/kcm/pull/2685)) by @dependabot
* **chore(deps):** bump sigs.k8s.io/cluster-api from 1.13.0 to 1.13.1 ([#2679](https://github.com/k0rdent/kcm/pull/2679)) by @dependabot
* **chore(deps):** bump github.com/fluxcd/pkg/runtime from 0.104.0 to 0.105.0 ([#2674](https://github.com/k0rdent/kcm/pull/2674)) by @dependabot
* **chore(deps):** bump github.com/onsi/ginkgo/v2 from 2.28.1 to 2.28.2 ([#2675](https://github.com/k0rdent/kcm/pull/2675)) by @dependabot
* **chore(deps):** bump CAPI Provider from 1.12.5 to 1.13.0 ([#2659](https://github.com/k0rdent/kcm/pull/2659)) by @dependabot
* **chore(deps):** bump github.com/Azure/go-ntlmssp ([#2667](https://github.com/k0rdent/kcm/pull/2667)) by @dependabot
* **chore(deps):** bump github.com/fluxcd/source-controller/api ([#2654](https://github.com/k0rdent/kcm/pull/2654)) by @dependabot
* **chore(deps):** bump github.com/fluxcd/pkg/runtime from 0.103.0 to 0.104.0 ([#2656](https://github.com/k0rdent/kcm/pull/2656)) by @dependabot
* **chore(deps):** bump github.com/fluxcd/helm-controller/api ([#2655](https://github.com/k0rdent/kcm/pull/2655)) by @dependabot

---

### Other Changes (CI, Tests, Refactors)

* **chore:** make default AWS AMI filter architecture-agnostic([#2786](https://github.com/k0rdent/kcm/pull/2786)) by @eromanova
* **chore:** migrate to upstream openstack provider ([#2781](https://github.com/k0rdent/kcm/pull/2781)) by @eromanova
* **chore(templates):** disable Windows DaemonSet for azuredisk-csi-driver ([#2765](https://github.com/k0rdent/kcm/pull/2765)) by @oshep
* **test:** add more coverage for ksm ([#2724](https://github.com/k0rdent/kcm/pull/2724)) by @kylewuolle
* **refactor:** optimizations to CD reconcile process ([#2703](https://github.com/k0rdent/kcm/pull/2703)) by @wahabmk
* **refactor:** optimizations to the MCS reconcile process ([#2702](https://github.com/k0rdent/kcm/pull/2702)) by @wahabmk
* **refactor:** normalize requeue/error controller paths ([#2699](https://github.com/k0rdent/kcm/pull/2699)) by @zerospiel
* **chore(template):** add openstack tls verify example ([#2696](https://github.com/k0rdent/kcm/pull/2696)) by @bnallapeta
* **chore:** re-generate divergent versions ([#2673](https://github.com/k0rdent/kcm/pull/2673)) by @zerospiel
* **ci(staging):** fix incorrect base commit to avoid failures if discrepancy ([#2670](https://github.com/k0rdent/kcm/pull/2670))
* **test:** improve ClusterDeployment integration tests ([#2618](https://github.com/k0rdent/kcm/pull/2618)) by @eromanova

---

## References

* [Compare KCM v1.9.0...v1.10.0](https://github.com/k0rdent/kcm/compare/v1.9.0...v1.10.0)
* [Compare KOF v1.9.0...v1.10.0](https://github.com/k0rdent/kof/compare/v1.9.0...v1.10.0)
