# k0rdent 1.3.1 Release Notes
**Release date:** 2025-09-03

## Components Versions

| Provider Name | Version |
|-------------------|-------------|
| Cluster API | v1.10.4 |
| Cluster API Provider AWS | v2.8.4 |
| Cluster API Provider Azure | v1.20.2 |
| Cluster API Provider Docker | v1.9.6 |
| Cluster API Provider GCP | v1.10.0 |
| Cluster API Provider Infoblox | v0.1.0-alpha.8 |
| Cluster API Provider IPAM | v1.0.2 |
| Cluster API Provider k0smotron | v1.6.2 |
| Cluster API Provider OpenStack (ORC) | v0.12.4 (v2.1.0) |
| Cluster API Provider vSphere | v1.13.1 |
| Projectsveltos | v0.57.2 |

---

## Highlights
- **k0rdent Cluster Manager (KCM):**
    - Telemetry Collection
    - Support to customize the default Helm install or upgrade timeout

- **ServiceSet API & Sveltos provider (KSM):** 
    - New abstraction for managing services with explicit dependencies and ordered upgrades. Enables smoother rollouts and future multi-provider support.

- **Observability (KOF):**  
    - New kube-state-metrics dashboards for k0rdent CRDs and alerting.  
    - "Raw metrics" tab in the UI for collectors/logs.  
    - Promxy tuned for heavy queries to avoid OOMs.

- **Platform & Dependency Updates:**  
    - k0smotron upgraded to **v1.6.2**  
    - Cluster API Azure provider upgraded to **v1.20.2**  
    - Go toolchain moved to **1.24.6**, with Helm and testing libraries updated.

- **Stability & UX:** 
    - Multiple fixes to credential propagation, service status collection, hosted cluster templates, Helm repos, and cloud provider templates (OpenStack, Azure).

---

## Upgrade Notes
- **KOF**:
    - Please apply the "Reconciling MultiClusterService" [workaround](../admin/kof/kof-upgrade.md/#upgrade-to-v130).
- **Providers:**  
    - Align pinned dependencies with new versions (k0smotron 1.6.2, CAPI Azure 1.20.2).  
    - Build/test environments should use Go 1.24.6.
- **Observability:**  
    - After upgrading KOF, apply the new dashboards and validate Promxy resource settings against your workload size.
- **KSM/KCM APIs:**  
    - The new `ServiceSet` API is additive. Existing Sveltos configurations continue to work, but you should begin testing with ServiceSets for future upgrades.

---

## Changelog

### New Features

-   [a8c97a6](https://github.com/k0rdent/kof/commit/a8c97a6512ba392e5ae32103d0565a878fba59f2): feat: kube-state-metrics dashboards for k0rdent objects ([#497](https://github.com/k0rdent/kof/pull/497)) by  [@gmlexx](https://github.com/gmlexx)
-   [bdb9707](https://github.com/k0rdent/kcm/commit/bdb97078bc1d84af8448e0bd0e705eeaee14aeaa): feat: child telemetry tracker ([#1783](https://github.com/k0rdent/kcm/pull/1783)) by  [@zerospiel](https://github.com/zerospiel)
-   [1355a18](https://github.com/k0rdent/kcm/commit/1355a18ed9d19ee8115dbcb7f3d27fe2932076b5): feat: expose services.policyRef in CD and MCS spec ([#1725](https://github.com/k0rdent/kcm/pull/1725)) by  [@wahabmk](https://github.com/wahabmk)
-   [82d3e06](https://github.com/k0rdent/kcm/commit/82d3e06820e3f90213f947825e3b9751ee2a84ed): feat: introduce local telemetry collector ([#1845](https://github.com/k0rdent/kcm/pull/1845)) by  [@zerospiel](https://github.com/zerospiel)
-   [f5fe7bb](https://github.com/k0rdent/kcm/commit/f5fe7bb4810815cef2c15392166bac9beaec8260): feat: provider-agnostic KSM with built-in provider ([#1670](https://github.com/k0rdent/kcm/pull/1670)) by  [@BROngineer](https://github.com/BROngineer)
-   [b15d226](https://github.com/k0rdent/kcm/commit/b15d226022599acf611d4d98f79e03d818b0cea5): feat: telemetry local storage configuration ([#1857](https://github.com/k0rdent/kcm/pull/1857)) by  [@zerospiel](https://github.com/zerospiel)
-   [acb9120](https://github.com/k0rdent/kof/commit/acb9120556cd9d2e28c920e8aa34c6b251873922): feat: add http config for adopted regional cluster by  [@gmlexx](https://github.com/gmlexx)
-   [93d1064](https://github.com/k0rdent/kof/commit/93d1064cb3d3bf7967a723edc6a7e646b09ed922): feat: add backend for internal observability of VictoriaMetrics/Logs ([#463](https://github.com/k0rdent/kof/pull/463)) by  [@AndrejsPon00](https://github.com/AndrejsPon00)
-   [6958133](https://github.com/k0rdent/kof/commit/6958133fb7c0dd95167dc6db8dac772f509e71f4): feat: add VictoriaMetrics and VictoriaLogs observability page to KOF UI ([#480](https://github.com/k0rdent/kof/pull/480)) by  [@AndrejsPon00](https://github.com/AndrejsPon00)
-   [1fa557d](https://github.com/k0rdent/kof/commit/1fa557d4daf245361ad38a6842e056f8c09272bf): feat: allow full vm custom objects specs definition in values ([#478](https://github.com/k0rdent/kof/pull/478)) by  [@gmlexx](https://github.com/gmlexx)
-   [6978d1c](https://github.com/k0rdent/kof/commit/6978d1c058152e014ee6fc53cab5f062cea30194): feat: add tooltip for metrics description in KOF UI ([#483](https://github.com/k0rdent/kof/pull/483)) by  [@AndrejsPon00](https://github.com/AndrejsPon00)
-   [370da8f](https://github.com/k0rdent/kof/commit/370da8ff17823920789558caa84d32c0e0330569): feat: update helm charts on storage secret change ([#484](https://github.com/k0rdent/kof/pull/484)) by  [@gmlexx](https://github.com/gmlexx)
-   [838f53a](https://github.com/k0rdent/kof/commit/838f53a09b3ce3409339f3b3ad35a2ff095d43fa): feat: add raw metrics tab in KOF UI ([#487](https://github.com/k0rdent/kof/pull/487)) by  [@AndrejsPon00](https://github.com/AndrejsPon00)
-   [1131315](https://github.com/k0rdent/kof/commit/11313151a6f775e6d4220bc787d7e9d4767b0ebc): feat: add custom resources to kube-state-metrics ([#489](https://github.com/k0rdent/kof/pull/489)) by  [@gmlexx](https://github.com/gmlexx)
-   [7832d51](https://github.com/k0rdent/kof/commit/7832d516bfda998db14c9ebc3aaae6b18747761f): feat: mothership components monitoring ([#342](https://github.com/k0rdent/kof/pull/342)) by  [@aglarendil](https://github.com/aglarendil)
-   [6df9757](https://github.com/k0rdent/kof/commit/6df97570cf35a843439cb8f2ad32f20db5384e60): feat: add misconfiguration check for collector scrape in KOF UI ([#490](https://github.com/k0rdent/kof/pull/490)) by  [@AndrejsPon00](https://github.com/AndrejsPon00)

### Notable Fixes

KSM has received several critical fixes in the v1.3.1 release:

- [b809ba8](https://github.com/k0rdent/kcm/commit/b809ba8a1c84d1e6b7b70ee9c5fe35349f8612d4): fix: collecting ksm service statuses ([#1952](https://github.com/k0rdent/kcm/pull/1952)) by [@BROngineer](https://github.com/BROngineer)
- [66af56f](https://github.com/k0rdent/kcm/commit/66af56f2c902384beed953141cadae0e1b452210): fix: enable multiclusterservice requeue on status update ([#1946](https://github.com/k0rdent/kcm/pull/1946)) by [@BROngineer](https://github.com/BROngineer)
- [030ea58](https://github.com/k0rdent/kcm/commit/030ea5898cede11324eab08123797bf7bde08132): fix: handle adopted cluster in ksm ([#1948](https://github.com/k0rdent/kcm/pull/1948)) by [@BROngineer](https://github.com/BROngineer)
- [c66bbe2](https://github.com/k0rdent/kcm/commit/c66bbe22405bcf75d1f519f5686d876267b0b072): fix: multiclusterservice cleanup ([#1947](https://github.com/k0rdent/kcm/pull/1948)) by [@BROngineer](https://github.com/BROngineer)

Other fixes:

-   [9107ce6](https://github.com/k0rdent/kof/commit/9107ce6f9873f0e762a678be60423667bc6ea63c): fix: prevent duplicate metric collection ([#488](https://github.com/k0rdent/kof/pull/488)) by  [@AndrejsPon00](https://github.com/AndrejsPon00)
-   [d61ff20](https://github.com/k0rdent/kcm/commit/d61ff20093782ea5caffc471b8265a3a72059a8b): fix: Mount CA cert as a volume to flux components ([#1844](https://github.com/k0rdent/kcm/pull/1844)) by  [@eromanova](https://github.com/eromanova)
-   [e11fe9e](https://github.com/k0rdent/kcm/commit/e11fe9eccb577366341fb6b4c26bfcb5f2d71201): fix: Mount CA secret to flux before installing kcm-templates ([#1847](https://github.com/k0rdent/kcm/pull/1847)) by  [@eromanova](https://github.com/eromanova)
-   [efb50cd](https://github.com/k0rdent/kcm/commit/efb50cde93392bf627e907f49fb6fc39ee98ea27): fix: add default storage class for openstack standalone templates ([#1871](https://github.com/k0rdent/kcm/pull/1871)) by  [@bnallapeta](https://github.com/bnallapeta)
-   [6a2ae2e](https://github.com/k0rdent/kcm/commit/6a2ae2ea9cdd1802ba0a01d9a7262edaf3c29e88): fix: allow configuration of the default HelmRelease timeout ([#1830](https://github.com/k0rdent/kcm/pull/1830)) by  [@eromanova](https://github.com/eromanova)
-   [fe394a8](https://github.com/k0rdent/kcm/commit/fe394a81dc0cae6c60f1b424b9b5ccca1fe88563): fix: continue e2e tests after deployment failure ([#1840](https://github.com/k0rdent/kcm/pull/1840)) by  [@eromanova](https://github.com/eromanova)
-   [cfcd997](https://github.com/k0rdent/kcm/commit/cfcd997ed44344c769d75b232ca8161988651cdd): fix: credentials propagation ([#1886](https://github.com/k0rdent/kcm/pull/1886)) by  [@BROngineer](https://github.com/BROngineer)
-   [44c9e2e](https://github.com/k0rdent/kcm/commit/44c9e2e896a9a4204b6aa233455633501a997cb2): fix: drop subpath from the registry in hosted helm repositories ([#1890](https://github.com/k0rdent/kcm/pull/1890)) by  [@eromanova](https://github.com/eromanova)
-   [76e1c79](https://github.com/k0rdent/kcm/commit/76e1c7918bdfbe9a066e370be7fce40d6f22507b): fix: install yq before generating release.yaml ([#1894](https://github.com/k0rdent/kcm/pull/1894)) by  [@eromanova](https://github.com/eromanova)
-   [2322cbe](https://github.com/k0rdent/kcm/commit/2322cbe1b8bb1a230f7d7e0fbab9a900e3aaeba5): fix: k0s image url for azure-hosted-cp ([#1856](https://github.com/k0rdent/kcm/pull/1856)) by  [@a13x5](https://github.com/a13x5)
-   [6e49c90](https://github.com/k0rdent/kcm/commit/6e49c90d9da00f628e44ed646a53413f99948c5c): fix: multiclusterservice requeue ([#1899](https://github.com/k0rdent/kcm/pull/1899)) by  [@BROngineer](https://github.com/BROngineer)
-   [97af4ed](https://github.com/k0rdent/kcm/commit/97af4eda4f702828d3d038da47666cdb5698ea9a): fix: redundant servicetemplates fetching ([#1832](https://github.com/k0rdent/kcm/pull/1832)) by  [@zerospiel](https://github.com/zerospiel)
-   [f1930e2](https://github.com/k0rdent/kcm/commit/f1930e25b2454c666016f08e1d21040e261a32fe): fix: remote-cluster (hosted) respects useSudo ([#1880](https://github.com/k0rdent/kcm/pull/1880)) by  [@zerospiel](https://github.com/zerospiel)
-   [103b439](https://github.com/k0rdent/kcm/commit/103b439c94508b65849d97b54e0bc0ba89048e06): fix: service statuses ([#1888](https://github.com/k0rdent/kcm/pull/1888)) by  [@BROngineer](https://github.com/BROngineer)
-   [55d963e](https://github.com/k0rdent/kcm/commit/55d963e08e448918d38ee7de4e124b025c97db09): fix: services deployed & clusters matched in MCS kubectl output ([#1779](https://github.com/k0rdent/kcm/pull/1779)) by  [@wahabmk](https://github.com/wahabmk)
-   [af5feae](https://github.com/k0rdent/kcm/commit/af5feae7fa98b9b08ee36819a0026110d024ee30): fix: set kcm version in release.yaml before making the release ([#1877](https://github.com/k0rdent/kcm/pull/1877)) by  [@eromanova](https://github.com/eromanova)
-   [cfba650](https://github.com/k0rdent/kof/commit/cfba650596935aa01cbe69816b9a4e23b9856180): fix: change opencost prometheus URL to HTTP for local cluster ([#451](https://github.com/k0rdent/kof/pull/451)) by  [@AndrejsPon00](https://github.com/AndrejsPon00)
-   [7ba9801](https://github.com/k0rdent/kof/commit/7ba98015f05699d132fc45fe8842faf7b7d9a28f): fix: correct instrumentation exporter endpoint to resolve trace export error ([#452](https://github.com/k0rdent/kof/pull/452)) by  [@AndrejsPon00](https://github.com/AndrejsPon00)
-   [1dc8a60](https://github.com/k0rdent/kof/commit/1dc8a60fcd243124dcf99b2c2e39ecaf608c93be): fix: Replacing release notes with auto-generated ones, updated docs/release ([#453](https://github.com/k0rdent/kof/pull/453)) by  [@denis-ryzhkov](https://github.com/denis-ryzhkov)
-   [64b6f5b](https://github.com/k0rdent/kof/commit/64b6f5b6d609710a74b3e1fc1aac0e52836f9dcf): fix: slow KOF UI responses due to long proxy timeout ([#448](https://github.com/k0rdent/kof/pull/448)) by  [@AndrejsPon00](https://github.com/AndrejsPon00)
-   [f49b35a](https://github.com/k0rdent/kof/commit/f49b35a0ed8f9bc6cafeada88eea4a8965982260): fix: Customized  `cert-manager-startupapicheck`  image registry ([#457](https://github.com/k0rdent/kof/pull/457)) by  [@denis-ryzhkov](https://github.com/denis-ryzhkov)
-   [d15e1cb](https://github.com/k0rdent/kof/commit/d15e1cb87bd5fe15d6ceaa6b87dc9453f3a441d3): fix: promxy server group doesn't update after http client config changes ([#456](https://github.com/k0rdent/kof/pull/456)) by  [@AndrejsPon00](https://github.com/AndrejsPon00)
-   [ad3bec4](https://github.com/k0rdent/kof/commit/ad3bec489e803b95a567961068394a45409b8166): fix: increase promxy memory requests/limits to prevent OOM ([#458](https://github.com/k0rdent/kof/pull/458)) by  [@AndrejsPon00](https://github.com/AndrejsPon00)
-   [2c3d50a](https://github.com/k0rdent/kof/commit/2c3d50a4d187d399e96b795aa41d636625ccfc36): fix: move grafana operator to kof-operators helm chart ([#461](https://github.com/k0rdent/kof/pull/461)) by  [@gmlexx](https://github.com/gmlexx)
-   [ada76b5](https://github.com/k0rdent/kof/commit/ada76b525ea813b14ad43d3e419a553005d59e18): fix: Jaeger authenticated endpoint of regional cluster became available for other clusters ([#462](https://github.com/k0rdent/kof/pull/462)) by  [@denis-ryzhkov](https://github.com/denis-ryzhkov)
-   [3437957](https://github.com/k0rdent/kof/commit/34379579f14d28b9ff9c98154d0cccb38cdbbeac): fix:  `istio/gateway`  chart repo compatibility with custom registry ([#464](https://github.com/k0rdent/kof/pull/464)) by  [@denis-ryzhkov](https://github.com/denis-ryzhkov)
-   [588682e](https://github.com/k0rdent/kof/commit/588682eea642fdb29f216cd24d920ce725c65046): fix: add promxy suffix to promxy labels by  [@gmlexx](https://github.com/gmlexx)
-   [f3dbad0](https://github.com/k0rdent/kof/commit/f3dbad00413ec30f08e5a48826c634ed037e1e88): fix: add missing env variable for goreleaser ([#466](https://github.com/k0rdent/kof/pull/466)) by  [@gmlexx](https://github.com/gmlexx)
-   [6ea8e64](https://github.com/k0rdent/kof/commit/6ea8e6429eb3942f8d4891d40064057cc56101a3): fix: Added  `ServiceTemplateChain`  `cert-manager-v1-16-4-from-1-16-4`  required for upgrade to KOF 1.2.0 ([#467](https://github.com/k0rdent/kof/pull/467)) by  [@denis-ryzhkov](https://github.com/denis-ryzhkov)
-   [52b9658](https://github.com/k0rdent/kof/commit/52b9658e3669585e054e7bd58fedc4131fa21aa9): fix: override only defined properties with annotation on config update ([#468](https://github.com/k0rdent/kof/pull/468)) by  [@gmlexx](https://github.com/gmlexx)
-   [4353a1e](https://github.com/k0rdent/kof/commit/4353a1e619d922d0e7a97eda3bd5fa6626056995): fix: Custom  `kcm.serviceMonitor.selector`  ([#472](https://github.com/k0rdent/kof/pull/472)) by  [@denis-ryzhkov](https://github.com/denis-ryzhkov)
-   [2d6104b](https://github.com/k0rdent/kof/commit/2d6104b85d9bd1f53bfc0f8c6ea61d0214f4780d): fix: "Cluster Deployments Events" dashboard vs "From Management to Regional" case ([#469](https://github.com/k0rdent/kof/pull/469)) by  [@denis-ryzhkov](https://github.com/denis-ryzhkov)
-   [5f6f3dd](https://github.com/k0rdent/kof/commit/5f6f3dd9ba5d515dbee8bc57f03d5e1afcc6c36e): fix: Custom  `registryCredentialsConfig`  in  `helmCharts`  of  `kof-istio`  ([#473](https://github.com/k0rdent/kof/pull/473)) by  [@denis-ryzhkov](https://github.com/denis-ryzhkov)
-   [f9ad1e9](https://github.com/k0rdent/kof/commit/f9ad1e92ebc79c91b8292d71f24394d5528c347c): fix: use node name in node exporter dashboards ([#470](https://github.com/k0rdent/kof/pull/470)) by  [@gmlexx](https://github.com/gmlexx)
-   [75f174b](https://github.com/k0rdent/kof/commit/75f174b96451d487d7178f65503b8a65d558f321): fix: Two cases of  `chartName`  for  `cert-manager`  in  `kof-istio-network`  by  [@denis-ryzhkov](https://github.com/denis-ryzhkov)
-   [eb8d43f](https://github.com/k0rdent/kof/commit/eb8d43f009547d125795a01642c1bf98e9b5a3f5): fix: Moved  `kof-operators`  to be installed before  `kof-storage`  in  `kof-istio-regional`  to avoid "CRDs not found" by  [@denis-ryzhkov](https://github.com/denis-ryzhkov)
-   [06a137d](https://github.com/k0rdent/kof/commit/06a137d670caa2e1839380365084c4745ab403b4): fix: Updated Jaeger secret name after movingit from  `kof-storage`  to  `kof-mothership`  in  [#462](https://github.com/k0rdent/kof/pull/462)  to avoid  `invalid ownership metadata`  by  [@denis-ryzhkov](https://github.com/denis-ryzhkov)
-   [48504e1](https://github.com/k0rdent/kof/commit/48504e11967b5c02d41595786b9b9a9e26374330): fix: ContainerHighMemUsage alert has container label missing ([#477](https://github.com/k0rdent/kof/pull/477)) by  [@aglarendil](https://github.com/aglarendil)
-   [a1ce5b9](https://github.com/k0rdent/kof/commit/a1ce5b921e1d7f54848aa1412e9d70bb27cfee5e): fix: Typo in  `intervalFactor`  lead to 500 in "Istio Service Dashboard" ([#479](https://github.com/k0rdent/kof/pull/479)) by  [@denis-ryzhkov](https://github.com/denis-ryzhkov)
-   [3154164](https://github.com/k0rdent/kof/commit/31541640e46a8afd6dd471f9bf10b1fa616f42c3): fix: incorrect log level parsing for uppercase codes ([#481](https://github.com/k0rdent/kof/pull/481)) by  [@AndrejsPon00](https://github.com/AndrejsPon00)
-   [c0098ec](https://github.com/k0rdent/kof/commit/c0098ec004eced843fba3138fd0b49784c571d3e): fix: correctly parse and render total metric values and labels (not just last label) in kof UI ([#486](https://github.com/k0rdent/kof/pull/486)) by  [@AndrejsPon00](https://github.com/AndrejsPon00)
-   [b63188f](https://github.com/k0rdent/kof/commit/b63188fd0139bf572206c2972d468131147ab451): fix: prevent OOM crash in promxy on large queries ([#491](https://github.com/k0rdent/kof/pull/491)) by  [@AndrejsPon00](https://github.com/AndrejsPon00)
-   [93599c1](https://github.com/k0rdent/kof/commit/93599c1f5c842c08471d1cfb0208706426c102c1): fix: correct memory queries in Grafana dashboard panels ([#494](https://github.com/k0rdent/kof/pull/494)) by  [@AndrejsPon00](https://github.com/AndrejsPon00)

### Notable Changes

-   [13e3720](https://github.com/k0rdent/kof/commit/13e37202f3607fc4ffe0f8f9ef469e46dbf5e02a): chore: KOF 1.3.0 release ([#499](https://github.com/k0rdent/kof/pull/499)) by  [@denis-ryzhkov](https://github.com/denis-ryzhkov)
-   [b3e2247](https://github.com/k0rdent/kcm/commit/b3e2247e04329860d2c25b337408344571ad7fc3): fix(os-tpls): correct identity name in identityref ([#1901](https://github.com/k0rdent/kcm/pull/1901)) by  [@zerospiel](https://github.com/zerospiel)
-   [608b448](https://github.com/k0rdent/kcm/commit/608b448ce8e64271d2b348a7d0e866f4ecc37593): refactor: small change to reuse already defined statemanagementprovider name ([#1883](https://github.com/k0rdent/kcm/pull/1883)) by  [@wahabmk](https://github.com/wahabmk)
-   [d3cc733](https://github.com/k0rdent/kof/commit/d3cc733a67db0a8950915aabcdf66076efb5bf81): chore: setup go based on go.mod file by  [@gmlexx](https://github.com/gmlexx)
-   [fbd2d4a](https://github.com/k0rdent/kof/commit/fbd2d4aae905221da6ed6c23ff4c2eecd021b251): chore: apply coredns patch for mothership and restart once by  [@gmlexx](https://github.com/gmlexx)
-   [7867e05](https://github.com/k0rdent/kof/commit/7867e0504b01568f384b4558fa10f246ea7735da): chore: add promxy port-forward target by  [@gmlexx](https://github.com/gmlexx)
-   [c62848b](https://github.com/k0rdent/kof/commit/c62848b351bf4dd9fd5e1a597a5b08b2ab1912aa): test: check promxy metrics by  [@gmlexx](https://github.com/gmlexx)
-   [36154db](https://github.com/k0rdent/kof/commit/36154dbbd16427f4e8b6da971f1b182a35877d48): chore: add charts and docker images build ([#465](https://github.com/k0rdent/kof/pull/465)) by  [@gmlexx](https://github.com/gmlexx)
-   [29f0a2b](https://github.com/k0rdent/kof/commit/29f0a2baae65045604ccf8e8d3d42b7e94b5d532): test: wait until vmauth creates ingress in kind-adopted-regional cluster ([#471](https://github.com/k0rdent/kof/pull/471)) by  [@gmlexx](https://github.com/gmlexx)
-   [1885064](https://github.com/k0rdent/kof/commit/18850642ce73409d03966bafcccddd9168417f76): chore: KOF 1.2.1 patch release by  [@denis-ryzhkov](https://github.com/denis-ryzhkov)
-   [c106d22](https://github.com/k0rdent/kof/commit/c106d22aa9ce5648d1f3afb1ffe364675694850f): test: add unit tests for Victoria pages (KOF UI) ([#482](https://github.com/k0rdent/kof/pull/482)) by  [@AndrejsPon00](https://github.com/AndrejsPon00)
-   [1ac30b6](https://github.com/k0rdent/kof/commit/1ac30b6e801e39593f4f42dcd45ddae9116d0112): chore: KOF KOF 1.3.0-rc1 ([#496](https://github.com/k0rdent/kof/pull/496)) by  [@denis-ryzhkov](https://github.com/denis-ryzhkov)

---

## Known Issues

None

---

## Contributors
Thank you to **everyone** who contributed PRs, issues, and testing for this release, including (but certainly not limited to) [@zerospiel](https://github.com/zerospiel), [@BROngineer](https://github.com/BROngineer), [@eromanova](https://github.com/eromanova), [@denis-ryzhkov](https://github.com/denis-ryzhkov), [@a13x5](https://github.com/a13x5), [@wahabmk](https://github.com/wahabmk), and [@bnallapeta](https://github.com/bnallapeta).

## References
- [Compare KCM v1.2.0...v1.3.1](https://github.com/k0rdent/kcm/compare/v1.2.0...v1.3.0)  
- [Compare KOF v1.2.0...v1.3.1](https://github.com/k0rdent/kof/compare/v1.2.0...v1.3.0) 
