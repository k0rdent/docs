# k0rdent 1.6.0 Release Notes

**Release date:** December 17, 2025

## Components Versions

| Provider Name                        | Version                     |
| ------------------------------------ |-----------------------------|
| Cluster API                          | v1.11.3                     |
| Cluster API Provider AWS             | v2.10.0                     |
| Cluster API Provider Azure           | v1.21.1                     |
| Cluster API Provider Docker          | v1.11.3                     |
| Cluster API Provider GCP             | v1.10.0                     |
| Cluster API Provider Infoblox        | v0.1.0                      |
| Cluster API Provider IPAM            | v1.1.0-rc.1                 |
| Cluster API Provider k0smotron       | v1.10.1                     |
| Cluster API Provider OpenStack (ORC) | v0.13.0-mirantis.0 (v2.1.0) |
| Cluster API Provider vSphere         | v1.14.0                     |
| Projectsveltos                       | v1.1.1                      |
| k0s (control plane runtime)          | 1.32.8                      |
| cert-manager (charts)                | v1.19.1                     |

---

## Highlights

- **k0rdent Cluster Manager (KCM):**

    - **Identity and Authorization Management Support**: A unified way to manage authentication across `ClusterDeployments`.

- **k0rdent Service Manager (KSM):**

    - An ability to pause reconciliation of Sveltos deployed services.
    - An ability to upgrade services in sequential order.
    - Add service dependencies.

- **Observability (KOF):**
    - TBD

- **Platform & Dependency Updates:**
    - Cluster API upgraded to **v1.11.3**
    - Cluster API AWS provider upgraded to **v2.10.0**
    - Cluster API Docker provider upgraded to **v1.11.3**
    - Cluster API k0smotron provider upgraded to **v1.10.1**
    - Cluster API OpenStack provider forked version **v0.13.0-mirantis.0**

---

## Upgrade Notes

TBD

---

## Changelog

### New Features

* **feat:** add (Cluster)DataSource processing ([#2151](https://github.com/k0rdent/kcm/pull/2151)) by @zerospiel
* **feat:** add DataSource and ClusterDataSource types ([#2147](https://github.com/k0rdent/kcm/pull/2147)) by @zerospiel
* **feat:** add e2e tests for pausing of service set reconciliation ([#2237](https://github.com/k0rdent/kcm/pull/2237)) by @kylewuolle
* **feat:** cluster authentication configuration ([#2108](https://github.com/k0rdent/kcm/pull/2108)) by @eromanova
* **feat:** enhance KSM types representation ([#2159](https://github.com/k0rdent/kcm/pull/2159)) by @BROngineer
* **feat:** enhance multiclusterservice status with matching clusters ([#2169](https://github.com/k0rdent/kcm/pull/2169)) by @BROngineer
* **feat:** implement sequential upgrade ([#2062](https://github.com/k0rdent/kcm/pull/2062)) by @kylewuolle
* **feat:** keep deployed resources ([#2220](https://github.com/k0rdent/kcm/pull/2220)) by @BROngineer

### Notable Fixes

* **fix(cld):** pass correct kubeconfig reference during cleanup ([#2221](https://github.com/k0rdent/kcm/pull/2221)) by @zerospiel
* **fix(cld):** wait for CDS to be deleted ([#2194](https://github.com/k0rdent/kcm/pull/2194)) by @zerospiel
* **fix(cleanup):** collect owners and delete ([#2233](https://github.com/k0rdent/kcm/pull/2233)) by @zerospiel
* **fix(cleanup):** wait for PVs cleanup ([#2241](https://github.com/k0rdent/kcm/pull/2241)) by @zerospiel
* **fix(e2e):** move testing config validation to Makefile ([#2253](https://github.com/k0rdent/kcm/pull/2253)) by @eromanova
* **fix(openstack):** relax managedSecurityGroups schema and align hosted and standalone charts ([#2185](https://github.com/k0rdent/kcm/pull/2185)) by @bnallapeta
* **fix(regions):** propagate kubconfig if cld ref ([#2158](https://github.com/k0rdent/kcm/pull/2158)) by @zerospiel
* **fix(telemetry):** incorrect addressing ([#2161](https://github.com/k0rdent/kcm/pull/2161)) by @zerospiel
* **fix(templates):** migrate ASO objects to v1beta1 ([#2201](https://github.com/k0rdent/kcm/pull/2201)) by @zerospiel
* **fix(templates):** pass OS security groups ([#2209](https://github.com/k0rdent/kcm/pull/2209)) by @zerospiel
* **fix(templates):** substitute exact images with registry ([#2204](https://github.com/k0rdent/kcm/pull/2204)) by @zerospiel
* **fix(webhook):** validate templates on chains creation ([#2215](https://github.com/k0rdent/kcm/pull/2215)) by @zerospiel
* **fix:** CD summary for service deployment state ([#2225](https://github.com/k0rdent/kcm/pull/2225)) by @wahabmk
* **fix:** Improve run-time for mcs mothership e2e tests ([#2222](https://github.com/k0rdent/kcm/pull/2222)) by @wahabmk
* **fix:** ServiceSet update bug if status isn't Deployed ([#2142](https://github.com/k0rdent/kcm/pull/2142)) by @wahabmk
* **fix:** added the upgradePaths string slice back for backward compatibility and marked it as deprecated. ([#2251](https://github.com/k0rdent/kcm/pull/2251)) by @kylewuolle
* **fix:** converting serviceSpec to provider config ([#2236](https://github.com/k0rdent/kcm/pull/2236)) by @BROngineer
* **fix:** create serviceset if no services defined ([#2157](https://github.com/k0rdent/kcm/pull/2157)) by @BROngineer
* **fix:** dataSource values propagation ([#2219](https://github.com/k0rdent/kcm/pull/2219)) by @eromanova
* **fix:** do not update mgmt release immediately ([#2203](https://github.com/k0rdent/kcm/pull/2203)) by @zerospiel
* **fix:** helm options merging fails ([#2208](https://github.com/k0rdent/kcm/pull/2208)) by @kylewuolle
* **fix:** move auth config file out of /etc/k0s directory ([#2214](https://github.com/k0rdent/kcm/pull/2214)) by @eromanova
* **fix:** multicluster service value updates not reflected in service deployment ([#2258](https://github.com/k0rdent/kcm/pull/2258)) by @kylewuolle
* **fix:** poll cluster summaries ([#2163](https://github.com/k0rdent/kcm/pull/2163)) by @BROngineer
* **fix:** remove apiserver availability check for cleanup ([#2229](https://github.com/k0rdent/kcm/pull/2229)) by @Kshatrix
* **fix:** serviceset creation if no services defined in cld ([#2174](https://github.com/k0rdent/kcm/pull/2174)) by @BROngineer
* **fix:** support empty ClusterDataSource status ([#2192](https://github.com/k0rdent/kcm/pull/2192)) by @eromanova
* **fix:** trigger the deletion of ClusterDataSource ([#2200](https://github.com/k0rdent/kcm/pull/2200)) by @eromanova

### Dependency / Tooling Bumps (partial)

* **chore(deps):** bump cluster-api-provider-aws from 2.9.2 to 2.10.0 ([#2216](https://github.com/k0rdent/kcm/pull/2216) by @zerospiel
* **chore(bump):** k0smotron to v1.10.1 ([#2211](https://github.com/k0rdent/kcm/pull/2211)) by @Kshatrix
* **chore(deps):** bump github.com/fluxcd/helm-controller/api ([#2206](https://github.com/k0rdent/kcm/pull/2206))
* **chore(deps):** bump kubevirt.io/api from 1.6.3 to 1.7.0 ([#2207](https://github.com/k0rdent/kcm/pull/2207))
* **chore(deps):** bump sigs.k8s.io/cluster-api-operator from 0.24.0 to 0.24.1 ([#2197](https://github.com/k0rdent/kcm/pull/2197))
* **chore(deps):** bump k0smotron@v1.10.0 ([#2198](https://github.com/k0rdent/kcm/pull/2198)) by @zerospiel
* **chore(deps):** bump actions/checkout from 5 to 6 ([#2195](https://github.com/k0rdent/kcm/pull/2195))
* **chore(deps):** bump github.com/fluxcd/pkg/runtime from 0.89.0 to 0.91.0 ([#2191](https://github.com/k0rdent/kcm/pull/2191))
* **chore(deps):** bump github.com/fluxcd/source-controller/api ([#2189](https://github.com/k0rdent/kcm/pull/2189))
* **chore(deps):** bump golang.org/x/crypto ([#2193](https://github.com/k0rdent/kcm/pull/2193))
* **chore(deps):** bump github.com/fluxcd/helm-controller/api ([#2190](https://github.com/k0rdent/kcm/pull/2190))
* **chore(deps):** bump github.com/fluxcd/pkg/apis/meta from 1.22.0 to 1.23.0 ([#2186](https://github.com/k0rdent/kcm/pull/2186))
* **chore(deps):** bump k8s.io/apiserver from 0.34.1 to 0.34.2 ([#2178](https://github.com/k0rdent/kcm/pull/2178))
* **chore(deps):** bump k8s.io/kubectl from 0.34.1 to 0.34.2 ([#2176](https://github.com/k0rdent/kcm/pull/2176))
* **chore(deps):** bump golang.org/x/crypto from 0.43.0 to 0.44.0 ([#2175](https://github.com/k0rdent/kcm/pull/2175))
* **chore(deps):** bump helm.sh/helm/v3 from 3.19.1 to 3.19.2 ([#2177](https://github.com/k0rdent/kcm/pull/2177))
* **chore(deps):** bump helm.sh/helm/v3 from 3.19.0 to 3.19.1 ([#2171](https://github.com/k0rdent/kcm/pull/2171))
* **chore(deps):** bump golang.org/x/text from 0.30.0 to 0.31.0 ([#2172](https://github.com/k0rdent/kcm/pull/2172))
* **chore(deps):** bump kubevirt.io/api from 1.6.2 to 1.6.3 ([#2173](https://github.com/k0rdent/kcm/pull/2173))
* **chore(deps):** bump golang.org/x/sync from 0.17.0 to 0.18.0 ([#2165](https://github.com/k0rdent/kcm/pull/2165))
* **chore(deps):** bump github.com/vmware-tanzu/velero from 1.17.0 to 1.17.1 ([#2162](https://github.com/k0rdent/kcm/pull/2162))
* **chore(deps):** bump github.com/containerd/containerd ([#2153](https://github.com/k0rdent/kcm/pull/2153))
* **chore(bump):** update openstack provider version to v0.13.0 ([#2154](https://github.com/k0rdent/kcm/pull/2154)) by @Kshatrix
* **chore(bump):** update capi version to v1.11.3 ([#2150](https://github.com/k0rdent/kcm/pull/2150)) by @Kshatrix
* **chore(deps):** bump sigs.k8s.io/cluster-api from 1.11.2 to 1.11.3 ([#2148](https://github.com/k0rdent/kcm/pull/2148))

---

## References

* [Compare KCM v1.5.0…v1.6.0](https://github.com/k0rdent/kcm/compare/v1.5.0...v1.6.0)

