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

    - **Reconciliation Control for Sveltos Services**: The ability to pause reconciliation for services deployed via Sveltos, allowing controlled maintenance and troubleshooting without continuous drift correction.
    -  **Sequential Service Upgrade Support**: Support for upgrading services in a defined, sequential order to reduce risk and manage inter-service dependencies during rollout.
    - **Service Dependency Management**: The ability to define explicit dependencies between services, making sure prerequisite services are deployed and upgraded in the correct order.

- **Observability (KOF):**
  
    - **Adopted Cluster Support for KCM Regions**: Support for adopting existing clusters into a KCM Region, enabling centralized management of previously unmanaged or externally created clusters.
    - **OTel Collector Misconfiguration Detection in KOF UI**: Automatic detection and surfacing of OpenTelemetry Collector misconfigurations directly in the KOF UI to speed up diagnosis and reduce observability blind spots.

- **Platform & Dependency Updates:**
    - Cluster API upgraded to **v1.11.3**
    - Cluster API AWS provider upgraded to **v2.10.0**
    - Cluster API Docker provider upgraded to **v1.11.3**
    - Cluster API k0smotron provider upgraded to **v1.10.1**
    - Cluster API OpenStack provider forked version **v0.13.0-mirantis.0**

---

## Upgrade Notes

-   Before upgrading `kof-mothership`, ensure the following steps are completed:
    1.  Upgrade the `kof-operators` chart using the `--take-ownership` flag:

        ```
        helm upgrade --take-ownership \
          --reset-values --wait -n kof kof-operators -f operators-values.yaml \
          oci://ghcr.io/k0rdent/kof/charts/kof-operators --version 1.6.0
        ```
        
    1.  Make sure to upgrade `kof-operators` using the `--take-ownership` flag on each KOF Regional cluster:
 
        ```
        KUBECONFIG=regional-kubeconfig helm upgrade --take-ownership \
          --reset-values --wait -n kof kof-operators -f operators-values.yaml \
          oci://ghcr.io/k0rdent/kof/charts/kof-operators --version 1.6.0
        ```
        
    This step will not be required in future upgrades.

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
* **feat:** add adopted cluster support for KCM Region ([#630](https://github.com/k0rdent/kof/pull/630)) by @AndrejsPon00
* **feat:** add OTel Collector misconfiguration detection to KOF UI ([#636](https://github.com/k0rdent/kof/pull/636)) by @AndrejsPon00

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
* **fix:** update KOF operator ClusterRole to prevent KOF UI errors ([#620](https://github.com/k0rdent/kof/pull/620)) by @AndrejsPon00
* **fix:** mothership upgrade failure caused by `ServiceTemplateChain` spec changes ([#625](https://github.com/k0rdent/kof/pull/625)) by @AndrejsPon00
* **fix:** prevent chart reinstallation by adding service dependencies to region/child MCS ([#623](https://github.com/k0rdent/kof/pull/623)) by @AndrejsPon00
* **fix:** split queue utilization widgets ([#629](https://github.com/k0rdent/kof/pull/629)) by @gmlexx
* **fix:** align operator service labels and ports with operator pod configuration ([#622](https://github.com/k0rdent/kof/pull/622)) by @AndrejsPon00
* **fix:** false-positive misconfiguration alert for localhost ([#631](https://github.com/k0rdent/kof/pull/631)) by @gmlexx
* **fix:** duplicated dashboard UID ([#635](https://github.com/k0rdent/kof/pull/635)) by @gmlexx
* **fix:** Grafana operator reconciliation failure caused by missing credentials ([#645](https://github.com/k0rdent/kof/pull/645)) by @gmlexx
* **fix:** incorrect vmalert image used for vmauth ([#646](https://github.com/k0rdent/kof/pull/646)) by @denis-ryzhkov
* **fix:** improve cluster cloud detection logic ([#651](https://github.com/k0rdent/kof/pull/651)) by @AndrejsPon00
* **fix:** unused `ServiceTemplateChain` blocking KOF installation ([#654](https://github.com/k0rdent/kof/pull/654)) by @AndrejsPon00
* **fix:** remove `Patch Kind Config` step from upgrade CI pipelines ([#656](https://github.com/k0rdent/kof/pull/656)) by @AndrejsPon00
* **fix:** Grafana operator reconciliation issue caused by missing credentials ([#657](https://github.com/k0rdent/kof/pull/657)) by @gmlexx
* **fix:** make global values compatible with new collectors ([#663](https://github.com/k0rdent/kof/pull/663)) by @denis-ryzhkov
* **fix:** missing version field in `ServiceTemplateChain` upgrades ([#668](https://github.com/k0rdent/kof/pull/668)) by @AndrejsPon00
* **fix:** prevent chart reinstallation in MCS by adding `wait` to Helm options ([#664](https://github.com/k0rdent/kof/pull/664)) by @AndrejsPon00
* **ci:** fix Docker pull rate-limit issues in CI ([#650](https://github.com/k0rdent/kof/pull/650)) by @AndrejsPon00
* **ci:** add workaround for CI failures caused by Grafana Operator ([#659](https://github.com/k0rdent/kof/pull/659)) by @AndrejsPon00

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
* **chore:** bump version to upcoming 1.6.0-rc0 ([#621](https://github.com/k0rdent/kof/pull/621)) by @denis-ryzhkov
* **chore:** fix metrics port binding for kind clusters ([#626](https://github.com/k0rdent/kof/pull/626)) by @gmlexx
* **chore:** update Istio-related files following Istio chart merge ([#627](https://github.com/k0rdent/kof/pull/627)) by @AndrejsPon00
* **chore:** upgrade Grafana Operator to v5.20.0 ([#634](https://github.com/k0rdent/kof/pull/634)) by @gmlexx
* **chore:** upgrade OpenCost to v1.118.0 ([#641](https://github.com/k0rdent/kof/pull/641)) by @gmlexx
* **chore:** automatically label `kof` namespace for Istio sidecar injection ([#643](https://github.com/k0rdent/kof/pull/643)) by @AndrejsPon00
* **chore:** pin image tags in kof-collectors values ([#647](https://github.com/k0rdent/kof/pull/647)) by @denis-ryzhkov
* **chore:** bump version to KOF 1.6.0-rc1 ([#667](https://github.com/k0rdent/kof/pull/667)) by @AndrejsPon00

---

## References

* [Compare KCM v1.5.0…v1.6.0](https://github.com/k0rdent/kcm/compare/v1.5.0...v1.6.0)
* [Compare KOF v1.5.0...v1.6.0-rc1](https://github.com/k0rdent/kof/compare/v1.5.0...v1.6.0-rc1)


