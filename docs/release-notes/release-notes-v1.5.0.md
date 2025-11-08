# k0rdent 1.5.0 Release Notes 

**Release date:** October 30, 2025

## Components Versions

| Provider Name                        | Version |
| ------------------------------------ | ------- |
| Cluster API                          | v1.11.2 |
| Cluster API Provider AWS             | v2.9.2  |
| Cluster API Provider Azure           | v1.21.1 |
| Cluster API Provider Docker          | v1.11.2  |
| Cluster API Provider GCP             | v1.10.0 |
| Cluster API Provider Infoblox        | v0.1.0  |
| Cluster API Provider IPAM            | v1.1.0-rc.1  |
| Cluster API Provider k0smotron       | v1.9.0  |
| Cluster API Provider OpenStack (ORC) | v0.12.5-mirantis.0 (v2.1.0) |
| Cluster API Provider vSphere         | v1.14.0 |
| Projectsveltos                       | v1.1.1 |
| k0s (control plane runtime)          | 1.32.8  |
| cert-manager (charts)                | v1.19.1 |

---

## Highlights

  * **Regions**: Regions can now be restored from backup, and can recognize existing `ClusterDeployments`.
  * **Migrate Child Clusters**: A `ClusterDeployment` can now be moved from one management cluster to another.
  * **Credentials & Identities**: Distribute cluster identities across regions.
  * **RBAC Manager**: Introduced as a first-class KCM management component.
  * **Dependency Recognition**: k0rdent now understands `MultiClusterService` dependencies, avoiding extraneous error messages.
  * **Operational changes**: You can now pause Sveltos profile reconciliation via a `ServiceSet` annotation, easing tasks like troubleshooting and disaster recovery.

---

## Upgrade Notes

  * **IMPORTANT**: Avoid upgrading to 1.5.0 if you plan to have or have existing `ClusterDeployments` using `aws-eks-1-0-*` `ClusterTemplates`. Use k0rdent 1.4.0 instead.

  * New/stricter **Region validation** may surface issues with configurations that were previously accepted. Dry-run manifests before rollout.
  * **Region restoration** flow is new; confirm backup/restore procedures for regional components.

  * CI images switched base images from `scratch` to `gcr.io/distroless/static-debian12:nonroot`

---

## Changelog

### New Features

* **feat:** upgrade cluster-api@v1.11.2 ([#2032](https://github.com/k0rdent/kcm/pull/2032)) by @zerospiel
* **feat(restore):** support regions restoration ([#2073](https://github.com/k0rdent/kcm/pull/2073)) by @zerospiel
* **feat:** adapt existing validation for Regions ([#2065](https://github.com/k0rdent/kcm/pull/2065)) by @eromanova
* **feat:** region validation ([#2063](https://github.com/k0rdent/kcm/pull/2063)) by @eromanova
* **feat:** credential cluster identity distribution ([#2075](https://github.com/k0rdent/kcm/pull/2075)) by @eromanova
* **feat:** support `ClusterDeployment` reference in Region spec ([#2096](https://github.com/k0rdent/kcm/pull/2096)) by @eromanova
* **feat:** add RBAC manager as the KCM management component ([#2109](https://github.com/k0rdent/kcm/pull/2109)) by @eromanova
* **feat:** pause reconciliation of sveltos profiles via ServiceSet annotation (no PR listed) by @kylewuolle
* **feat:** implement MultiClusterService dependencies ([#2009](https://github.com/k0rdent/kcm/pull/2009)) by @wahabmk
* **feat:** regional telemetry collection ([#2113](https://github.com/k0rdent/kcm/pull/2113)) by @zerospiel

### Notable Fixes

* **fix:** cert-manager-dependent regional components disabling ([#2061](https://github.com/k0rdent/kcm/pull/2061)) by @eromanova
* **fix:** update Credential status when Region is not ready ([#2066](https://github.com/k0rdent/kcm/pull/2066)) by @eromanova
* **chore:** remove multiclusterservice validation webhook ([#2071](https://github.com/k0rdent/kcm/pull/2071)) by @BROngineer
* **fix:** self-management panics & incorrect profile type ([#2074](https://github.com/k0rdent/kcm/pull/2074)) by @wahabmk
* **fix(providerinterface):** Azure ClusterIdentities ([#2088](https://github.com/k0rdent/kcm/pull/2088)) by @zerospiel
* **fix(templates):** AWS-CSI image paths; Azure required parameters ([#2111](https://github.com/k0rdent/kcm/pull/2111)) by @a13x5
* **fix:** drop kcm-regional version annotation from Release ([#2117](https://github.com/k0rdent/kcm/pull/2117)) by @eromanova

### Dependency / Tooling Bumps (partial)

* **chore:** cert-manager@v1.19.1 ([#2090](https://github.com/k0rdent/kcm/pull/2090)) by @zerospiel
* **chore:** k0smotron provider v1.9.0 ([#2115](https://github.com/k0rdent/kcm/pull/2115)) by @zerospiel
* **chore:** k0s 1.32.8 ([#2116](https://github.com/k0rdent/kcm/pull/2116)) by @zerospiel
* **chore:** CAPA v2.9.2 ([#2123](https://github.com/k0rdent/kcm/pull/2123)) by @Kshatrix
* **chore:** CAPZ v1.21.1 ([#2121](https://github.com/k0rdent/kcm/pull/2121)) by @Kshatrix
* **chore:** bump `peter-evans/find-comment` 3.1.0→4.0.0 ([#2059](https://github.com/k0rdent/kcm/pull/2059))
* **chore:** Velero chart bump ([#2058](https://github.com/k0rdent/kcm/pull/2058)) by @zerospiel
* **chore:** Ginkgo v2.26.0→v2.27.1 ([#2114](https://github.com/k0rdent/kcm/pull/2114))
* **chore:** Ginkgo v2.27.1→v2.27.2 ([#2140](https://github.com/k0rdent/kcm/pull/2140))
* **chore:** fluxcd/helm-controller API bump ([#2139](https://github.com/k0rdent/kcm/pull/2139))
* **chore:** fluxcd/source-controller API bump ([#2141](https://github.com/k0rdent/kcm/pull/2141))
* **chore:** `x/crypto` 0.42.0→0.43.0 ([#2080](https://github.com/k0rdent/kcm/pull/2080))
* **chore:** `kubevirt.io/api` 1.6.0→1.6.2 ([#2079](https://github.com/k0rdent/kcm/pull/2079))
* **chore:** `kubevirt.io/containerized-data-importer-api` bump ([#2078](https://github.com/k0rdent/kcm/pull/2078))
* **ci:** distroless to embed CA certs ([#2106](https://github.com/k0rdent/kcm/pull/2106)) by @zerospiel
* **chore:** Dockerfile uses `buildplatform` for builder ([#2110](https://github.com/k0rdent/kcm/pull/2110)) by @a13x5
* **ci(docker):** produce **latest telemetry** image tag ([#2135](https://github.com/k0rdent/kcm/pull/2135)) by @zerospiel
* **ci(post):** add dev segment ([#2102](https://github.com/k0rdent/kcm/pull/2102)) by @zerospiel
* **perf(dev):** add troubleshoot-profiles to config ([#2031](https://github.com/k0rdent/kcm/pull/2031)) by @briantd
* **chore:** default E2E config to AWS if empty ([#2134](https://github.com/k0rdent/kcm/pull/2134)) by @BROngineer
* **chore(telemetry):** enable on CI ([#2055](https://github.com/k0rdent/kcm/pull/2055)) by @zerospiel

---

## References

* [Compare KCM v1.4.0…main](https://github.com/k0rdent/kcm/compare/v1.4.0...main)

