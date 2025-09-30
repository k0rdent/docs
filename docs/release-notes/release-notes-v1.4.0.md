# k0rdent 1.4.0 Release Notes
**Release date:** 2025-09-30

## Components Versions

| Provider Name                        | Version                     |
|--------------------------------------|-----------------------------|
| Cluster API                          | v1.10.5                     |
| Cluster API Provider AWS             | v2.9.1                      |
| Cluster API Provider Azure           | v1.21.0                     |
| Cluster API Provider Docker          | v1.9.6                      |
| Cluster API Provider GCP             | v1.10.0                     |
| Cluster API Provider Infoblox        | v0.1.0                      |
| Cluster API Provider IPAM            | v1.0.2                      |
| Cluster API Provider k0smotron       | v1.6.2                      |
| Cluster API Provider OpenStack (ORC) | v0.12.5-mirantis.0 (v2.1.0) |
| Cluster API Provider vSphere         | v1.13.1                     |
| Projectsveltos                       | v0.57.2                     |

---

## Highlights

- **k0rdent Cluster Manager (KCM):**
    - Distributed Regional Management Control Planes (technical preview)
    - Label based role aggregation to simplify OOT provider itegration

- **k0rdent Serivce Manager (KSM):**
    - Inter-service dependencies in a ClusterDeployment or MultiClusterService spec
    - Support for helm options to use with service templayes
    - Improved observability of events and metrics for IPAM

- **Observability (KOF):**
    - KOF UI monitoring for KSM objects

- **Platform & Dependency Updates:**
    - Cluster API upgraded to **v1.10.5**
    - Cluster API AWS provider upgraded to **v2.9.1**
	- Cluster API Azure provider upgraded to **v1.21.0**
	- Cluster API IPAM provider upgraded to **v1.0.2**
    - Cluster API OpenStack provider forked version **v0.12.5-mirantis.0**
---

## Upgrade Notes

- **KCM**:
	- Due to CAPA upgrade to `v2.9.1` use of the empty selector in the
	`.spec.allowedNamespaces` in the cluster identity resources (such as
	`AWSClusterStaticIdentity`) is no longer valid and may cause `Namespace is
	not permitted` error. To mitigate that change the value to the empty object
	like so: `.spec.allowedNamespaces: {}` (ref: [#2022](https://github.com/k0rdent/kcm/issues/2022)).

- **KOF**:
	- Because of `PromxyServerGroup` CRD is moved to the `templates` directory for
	more flexible updates you must use the `--take-ownership` flag while
	upgrading `kof-mothership` to `1.4.0`. For example:

	```bash
		helm upgrade --take-ownership \
		  --reset-values --wait -n kof kof-mothership -f mothership-values.yaml \
		  oci://ghcr.io/k0rdent/kof/charts/kof-mothership --version 1.4.0
	```

---

## Changelog

### New Features

* 694718e44b4b62e13ab60fe73a29ec15bdd0e90a: feat(backups): add region support (#2040) by @zerospiel
* 330248da1a1c968d3b085d39b4af56886198ff39: feat: adapt services reconciliation to regional clusters (#2011) by @eromanova
* 2700e734a157adf2ebeedee1a2f78ebfb75a1411: feat: add JSON Schema configmap for templates if available (#1972) by @Kshatrix
* e074793a89c7db66350fd16e4e6fe72f8136b516: feat: add Region CRD and controller (#1958) by @eromanova
* 39e448b1c43c34cb6f9d81cd2fff44311ef6c68d: feat: add aggregate role for kcm manager (#1976) by @Kshatrix
* 04338d8e418d5ca0ce328207886ff8cbcadfe2ea: feat: add helm options to service templates (#1969) by @kylewuolle
* fb5618f83be005bbc69ceac50506a4664b2efb70: feat: cleanup orphaned cloud resources (#1973) by @zerospiel
* f1fcc57a631900775c672d74ba57dabd8563c197: feat: copy certificate secrets to regional clusters (#2025) by @eromanova
* afbefe3544dac44d5f1ef7c0804ee3f5ddeb68f6: feat: deprecate the Provider Interface controller (#2001) by @eromanova
* ad4e94f03220b894c187b2003d072579f8b70538: feat: implementation & validation of service dependencies (#1968) by @wahabmk
* d44581c457e1783819b73ef37997a14707032b52: feat: introduce Region field for Credential (#1980) by @eromanova
* 9b1f977db98992ba2a0f35810d191bea3d4a9c15: feat: move provider rbac to corresponding provider templates (#2007) by @Kshatrix
* 0087c5583ffce792891bc65ecdc6604292ca92ee: feat: observability of events and metrics for ipam (#1882) by @kylewuolle
* 0e7d07617c5d5e6a927e7d985a19115e9b894a79: feat: rework ClusterTemplate valid status check (#2002) by @eromanova
* 44ec8fb1724824a3873175fbc25a9353dfd8c6eb: feat: several minor Region improvements (#2010) by @eromanova
* b31f72904d1723815916051aae34891bfee35cf4: feat: add cluster deployment monitoring page to KOF UI (#502) by @AndrejsPon00
* 032fd301e52b95e1b7333e83c969ffc7d5933ca2: feat: add cluster summaries monitoring page to KOF UI (#505) by @AndrejsPon00
* ffc72f46a3e822085aba001f90d4bf3939b80f9f: feat: Add multi cluster services monitoring page to KOF UI (#508) by @AndrejsPon00
* 48eb9d3f9b4c72c7a4abd64f69c4f942af416ada: feat: add state management provider monitoring to KOF UI (#509) by @AndrejsPon00
* 4a3c1429265dde9ad325f57ed87b9a6c7338ded5: feat: add service set monitoring page to KOF UI (#519) by @AndrejsPon00
* faa2c3142d3cba5afa237eaccc7b601a77932432: feat: migrate to receiver_creator for filelog/containers to support annotation-based discovery (#529) by @gmlexx
* 3803b5a36a32934c19600bbdf54cd20e57505e7e: feat: add sveltos clusters monitoring page to KOF UI (#531) by @AndrejsPon00
* 783fe3ae93d3a76fad0b421952db5502b6406ad3: feat: add k8s audit logs collector config (#539) by @AndrejsPon00
* fbf250bb8cc2c907595b7ea8969cba8d0d027d38: feat: add parser for key-value logs (#528) by @AndrejsPon00
* 665c3a834ab05c1a658d3585b6b9c5572bb0ded1: feat: add filestore for filelogreceivers to store offsets (#544) by @gmlexx
* cae148859a60526883ebfc16244e40d9243bf8cf: feat: add alerts for CAPI Objects states (#526) by @AndrejsPon00
* ad2ff7807cd5a1f8eee84b3ed831fc33f6dc9e83: feat: add adopted clusters support for Istio (#551) by @gmlexx

### Notable Fixes

* c6acb4b1b037dc9261e9ee1871a4ead51f3d0017: fix(infoblox): support arm64 (#1938) by @zerospiel
* eb8d5fbd751a01b9c059d12d835eb55e0b60376f: fix(templates): allow null location policy for GKE (#2036) by @zerospiel
* f02213401a014eb29d267561fe4f071821d20462: fix(utils): patch object's component labels (#1949) by @zerospiel
* e1d81638900170b5144955f13d28b8198dbbdc98: fix: add configmap rbac permissions for controller (#2024) by @Kshatrix
* b2c5ec6355441c2cc86ce75af04d9b3905f2fba6: fix: add regional section to the Release spec (#2027) by @eromanova
* f7130057c6e95d9ab45d482ebb8b57a196b24e65: fix: add service as an available upgrade to itself (#2051) by @wahabmk
* 059e801179d92c7a3b14dac311b82ea5592c5405: fix: drop regional section from Release (#1996) by @eromanova
* fd2c0996626d0fce533b1f80b7c7cfe8fe53ae7a: fix: drop selector from dev aws credential (#2021) by @eromanova
* a931aabd1574b0fd47bf248c2517d54b4eb29c8b: fix: enable multiclusterservice requeue on status update (#1924) by @BROngineer
* 874c56cd26f0fef7af853aaa16ced90b1bacbd8a: fix: increase default helm timeout for dev setup (#2030) by @eromanova
* 17e432b6d7a5df2443ef0fc93f53ac1465688b4b: fix: missed registry creds config (#1974) by @BROngineer
* 1255e750fac124e15607e3a35a9e5595c5f15676: fix: moved network configuration for standalone deployments into values.yaml (#1887) by @vtrenton
* 3232eeb434258e40d2cd7b807740067de48fcda9: fix: network cfg in hosted tpls; fix standalone (#1895) by @zerospiel
* b473ea6ee3d6fcd85ee513d602afd87588173c63: fix: openstackclusteridentities permissions (#2046) by @Kshatrix
* ba8ac300dd01eed2a5f555ef09b3a9012bfc7554: fix: reflect deletion status in Region conditions (#2014) by @eromanova
* 72346855ed3bd8e346453b8e8c2ff93d0b16725e: fix: set current kcm-regional version as kcm dependency (#1982) by @eromanova
* 8c209e4a024e7dbafd2bcfb8ebc36bd7b41461db: fix: several fixes and improvements for regions (#2035) by @eromanova
* 82683aa74956f83e1e529c4aa6ea0792bfbe8b59: fix: remove timestamp metrics from kube-state custom resources (#498) by @gmlexx
* fe99e29556261358e75d98754dd9de8ce840bfc0: fix: Typo `grafana-operator.enables/enabled`, dedup of this subchart, updated descriptions (#506) by @denis-ryzhkov
* 2e6c66eacdfcb7cf9e4ef75ea43f18ab2470877c: fix: Fix of warnings on helm install/upgrade of kof-collectors (#504) by @denis-ryzhkov
* 6d2e339eb04e9878067e5d3b26a6ad921866241b: fix: flatten event fields for better filtering (#510) by @gmlexx
* cc20148369b901f000b4cb40f1853f75d55d9dc6: fix: Auto-upgrade KOF CRD PromxyServerGroup (#546) by @denis-ryzhkov
* 90cd7ab5b4fe9295121c0e983f4cc5061aa0effa: fix: Security fix of vite (#548) by @denis-ryzhkov
* 9be5d400768644698109e001922d15c4e783f7dd: fix: show log line field in dashboard (#559) by @gmlexx
* 79b2f8052d14fe7c86139d8ad371cd900a8f5f69: fix: move collectors service extensions list to upper charts values (#558) by @gmlexx

## References

- [Compare KCM v1.3.1...v1.4.0](https://github.com/k0rdent/kcm/compare/v1.3.1...v1.4.0)
