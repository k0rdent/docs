# {{{ docsVersionInfo.k0rdentName }}} v1.0.0 Release Notes

**NARRATIVE SECTION HIGHLIGHTING MAJOR CHANGES TO BE ADDED WHEN LISTS ARE FINALIZED.**

## Breaking Changes

TBD

## Components Versions

```
Cluster API 0.2.2
Cluster API Provider AWS 0.2.3
Cluster API Provider Azure 0.2.4
Cluster API Provider Docker 0.2.2
Cluster API Provider GCP 0.2.2
Cluster API Provider OpenStack 0.2.2
Cluster API Provider vSphere 0.2.2
Cluster API Provider k0smotron 0.2.3
Projectsveltos 0.52.2
```

## New Features

  - Add pod placement config (nodeSelector, affinity and tolerations) by [@eromanova](https://github.com/eromanova) in [PR \# (partially obscured in PDF)](https://www.google.com/search?q=https://github.com/k0rdent/kcm/pull/Unknown)
  - Enable Helm charts installation from flux sources by [@BROngineer](https://github.com/BROngineer) in [\#1350](https://github.com/k0rdent/kcm/pull/1350)
  - Allow self management of mothership cluster via Sveltos by [@wahabmk](https://github.com/wahabmk) in [\#1356](https://github.com/k0rdent/kcm/pull/1356)

## Notable Changes

  - Drop catalog core dependency by [@eromanova](https://github.com/eromanova) in [\#1284](https://www.google.com/search?q=https://github.com/k0rdent/kcm/pull/1284) (also see [\#1287](https://www.google.com/search?q=https://github.com/k0rdent/kcm/pull/1287))
  - Access Management ctrl rearrangement by [@zerospiel](https://github.com/zerospiel) in [\#1288](https://www.google.com/search?q=https://github.com/k0rdent/kcm/pull/1288)
  - TemplateChains reconciles admission checks by [@zerospiel](https://github.com/zerospiel) in [\#1291](https://www.google.com/search?q=https://github.com/k0rdent/kcm/pull/1291)
  - Handle Release delete request by [@zerospiel](https://github.com/zerospiel) in [\#1314](https://www.google.com/search?q=https://github.com/k0rdent/kcm/pull/1314)
  - Reconcile MCS and CD validations by [@zerospiel](https://github.com/zerospiel) in [\#1337](https://www.google.com/search?q=https://github.com/k0rdent/kcm/pull/1337)
  - ClusterDeployment reconciles validations by [@zerospiel](https://github.com/zerospiel) in [\#1362](https://github.com/k0rdent/kcm/pull/1362)
  - Rework CAPI conditions aggregator for Cluster Deployment by [@eromanova](https://github.com/eromanova) in [\#1366](https://github.com/k0rdent/kcm/pull/1366)
  - Management reconciles validations by [@zerospiel](https://github.com/zerospiel) in [\#1372](https://github.com/k0rdent/kcm/pull/1372)

## Notable Fixes

  - Fix linux awscli installation by [@zerospiel](https://github.com/zerospiel) in [\#1275](https://www.google.com/search?q=https://github.com/k0rdent/kcm/pull/1275)
  - Fix panic in adopted e2e testing by [@eromanova](https://github.com/eromanova) in [\#1277](https://www.google.com/search?q=https://github.com/k0rdent/kcm/pull/1277)
  - Revert k0s version to 1.32.1 for docker cluster template by [@eromanova](https://github.com/eromanova) in [\#1286](https://www.google.com/search?q=https://github.com/k0rdent/kcm/pull/1286)
  - Do not drop unused kcm templates HelmReleases by [@eromanova](https://github.com/eromanova) in [\#1281](https://www.google.com/search?q=https://github.com/k0rdent/kcm/pull/1281) (also see [\#1285](https://www.google.com/search?q=https://github.com/k0rdent/kcm/pull/1285))
  - Fix incorrect svc readiness calculation by [@zerospiel](https://github.com/zerospiel) in [\#1309](https://www.google.com/search?q=https://github.com/k0rdent/kcm/pull/1309)
  - Ensure nil registry credential config when no config is set by [@byDimasik](https://github.com/byDimasik) in [\#1363](https://github.com/k0rdent/kcm/pull/1363) (PR number from your example, description matches PDF)
  - Add missing RBAC for clustertemplatechain/status by [@eromanova](https://github.com/eromanova) in [\#1375](https://www.google.com/search?q=https://github.com/k0rdent/kcm/pull/1375)

## Upgrade notes

Follow these upgrade [instructions](admin/upgrade/index.md), with special instructions [TBD]().

## New Contributors

TBD

**Full Changelog**: [v0.3.0-release...v1.0.0-release](https://www.google.com/search?q=https://github.com/k0rdent/kcm/compare/v0.3.0-release...v1.0.0-release)