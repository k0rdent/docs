# k0rdent 1.7.0 Release Notes

**Release date:** January 29, 2026

## Components Versions

| Provider Name                        | Version                     |
|--------------------------------------|-----------------------------|
| Cluster API                          | v1.12.2                     |
| Cluster API Provider AWS             | v2.10.0                     |
| Cluster API Provider Azure           | v1.21.1                     |
| Cluster API Provider Docker          | v1.11.3                     |
| Cluster API Provider GCP             | v1.10.0                     |
| Cluster API Provider Infoblox        | v0.1.0                      |
| Cluster API Provider IPAM            | v1.1.0-rc.1                 |
| Cluster API Provider k0smotron       | v1.10.1                     |
| Cluster API Provider OpenStack (ORC) | v0.13.0-mirantis.0 (v2.1.0) |
| Cluster API Provider vSphere         | v1.15.1                     |
| Projectsveltos                       | v1.1.1                      |
| k0s (control plane runtime)          | 1.32.8                      |
| cert-manager (charts)                | v1.19.2                     |

---

## Highlights

- **k0rdent Cluster Manager (KCM):**

    - **Proxy configuration Support**: Proxy settings can now be set, which
      enables all providers to communicate through proxy
    - **CAPK provider support**: CAPK provider templates are now a part of
      k0rdent

- **Observability (KOF):**

    - **Grafana in KOF** is now disabled by default see [Using KOF without Grafana](https://docs.k0rdent.io/next/admin/kof/kof-using/)
	- **KOF Tracing** now uses VictoriaTraces instead of Jaeger
    - **KOF Multi-tenancy** is now supported with new `kof-tenant-id` label

- **Platform & Dependency Updates:**
    - Cluster API upgraded to **v1.12.2**
    - Cluster API vSphere provider upgraded to **v1.15.1**
---

## Upgrade Notes

No specific upgrade instructions for this release.

> NOTE:
> Notice that Grafana is now disabled by default in KOF

---

## Changelog

### New Features

* **feat(controller):** add global proxy settings ([#2323](https://github.com/k0rdent/kcm/pull/2323)) by @zerospiel
* **feat:** add CAPK provider template ([#2312](https://github.com/k0rdent/kcm/pull/2312)) by @eromanova
* **feat:** add e2e tests for pausing of service set reconciliation ([#2237](https://github.com/k0rdent/kcm/pull/2237)) by @kylewuolle
* **feat:** add kubevirt standalone and hosted cluster templates ([#2351](https://github.com/k0rdent/kcm/pull/2351)) by @eromanova
* **feat:** remove v1alpha1 api version ([#2338](https://github.com/k0rdent/kcm/pull/2338)) by @Kshatrix
* **feat:** support to override deployment settings in default ProviderTemplates ([#2279](https://github.com/k0rdent/kcm/pull/2279)) by @eromanova
* **feat:** Disable Grafana ([#684](https://github.com/k0rdent/kof/pull/684)) by @denis-ryzhkov
* **feat:** replace Jaeger with VictoriaTraces ([#679](https://github.com/k0rdent/kof/pull/679)) by @AndrejsPon00
* **feat:** automate VMUser credential provisioning per cluster ([#699](https://github.com/k0rdent/kof/pull/699)) by @AndrejsPon00
* **feat:** add cluster name label automatically to `ClusterDeployment` resources ([#703](https://github.com/k0rdent/kof/pull/703)) by @AndrejsPon00

### Notable Fixes

* **fix(cleanup):** delete cld objects after servicesets ([#2350](https://github.com/k0rdent/kcm/pull/2350)) by @zerospiel
* **fix(tests):** skip provider config overwrite when empty ([#2292](https://github.com/k0rdent/kcm/pull/2292)) by @eromanova
* **fix:** add configmap read permissions for user-facing roles ([#2274](https://github.com/k0rdent/kcm/pull/2274)) by @Kshatrix
* **fix:** add namespace validation for services ([#2282](https://github.com/k0rdent/kcm/pull/2282)) by @kylewuolle
* **fix:** added the upgradePaths string slice back for backward compatibility and marked it as deprecated. ([#2251](https://github.com/k0rdent/kcm/pull/2251)) by @kylewuolle
* **fix:** define default network configuration in KubeVirt templates ([#2365](https://github.com/k0rdent/kcm/pull/2365)) by @eromanova
* **fix:** mark CRDs with helm-keep annotation where possible ([#2337](https://github.com/k0rdent/kcm/pull/2337)) by @Kshatrix
* **fix:** only set the service to failed if it's not in deployed state ([#2322](https://github.com/k0rdent/kcm/pull/2322)) by @kylewuolle
* **fix:** profile spec equality check to consider defaults ([#2270](https://github.com/k0rdent/kcm/pull/2270)) by @wahabmk
* **fix:** remove self-management cluster selector labels ([#2315](https://github.com/k0rdent/kcm/pull/2315)) by @wahabmk
* **fix:** run ksm tests via test config ([#2342](https://github.com/k0rdent/kcm/pull/2342)) by @wahabmk
* **fix:** validate only diff during object updates ([#2265](https://github.com/k0rdent/kcm/pull/2265)) by @eromanova
* **fix:** add metrics-server to resolve metric errors in KOF UI in local environment ([#655](https://github.com/k0rdent/kof/pull/655)) by @AndrejsPon00
* **fix:** update kind clusters creation with squid proxy ([#694](https://github.com/k0rdent/kof/pull/694)) by @gmlexx
* **fix:** prevent SANs checking error ([#695](https://github.com/k0rdent/kof/pull/695)) by @gmlexx
* **fix:** npm security audit ([#697](https://github.com/k0rdent/kof/pull/697)) by @gmlexx
* **fix:** update default storage values to align with the default retention ([#696](https://github.com/k0rdent/kof/pull/696)) by @gmlexx
* **fix:** upgrade opentelemetry operator and collector to 0.143.0 ([#706](https://github.com/k0rdent/kof/pull/706)) by @gmlexx
* **fix:** increase default CPU limit for collectors, k0s collector affinity ([#710](https://github.com/k0rdent/kof/pull/710)) by @gmlexx
* **fix:** CPUThrottlingHigh and KubeletPodStartUpLatencyHigh rules expressions ([#711](https://github.com/k0rdent/kof/pull/711)) by @gmlexx
* **fix:** move PKI_PATH to defaultCR env ([#713](https://github.com/k0rdent/kof/pull/713)) by @gmlexx
* **fix:** MCS valuesFrom has no namespace, helm v3 warns, helm v4 fails ([#717](https://github.com/k0rdent/kof/pull/717)) by @denis-ryzhkov
* **fix:** prevent `k0s-collector` crashes caused by values merge issue ([#719](https://github.com/k0rdent/kof/pull/719)) by @AndrejsPon00

---

## References

* [Compare KCM v1.6.0…v1.7.0](https://github.com/k0rdent/kcm/compare/v1.6.0...v1.7.0)
* [Compare KOF v1.6.0...v1.7.0](https://github.com/k0rdent/kof/compare/v1.6.0...v1.7.0)
