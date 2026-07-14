# KCM-Managed Resources

This document catalogs all Kubernetes resources created and managed by KCM controllers.

All managed resources are labeled with:
```
k0rdent.mirantis.com/managed: "true"
```

> WARNING:
> 1. Ensure that these object names are not used by other resources in the same namespace to avoid conflicts.
> 2. These document describes the resources created by KCM controllers only. It does not include resources created by
> other controllers (e.g., Cluster API).

---

## ClusterDeployment Related Resources

Created by the **ClusterDeployment controller** during cluster lifecycle management.

| Kind            | Name                                            | Namespace                 | Target Cluster      | Condition                                                                                               |
|-----------------|-------------------------------------------------|---------------------------|---------------------|---------------------------------------------------------------------------------------------------------|
| `HelmRelease`   | `<cdName>`                                      | Same as ClusterDeployment | Management          | Always                                                                                                  |
| `Secret`        | `<cdName>-auth-config`                          | Same as ClusterDeployment | Management/Regional | [Cluster Authentication](../admin/clusters/cluster-iam-setup.md) is configured                          |
| `ConfigMap`     | `<cdName>-audit-policy`                         | Same as ClusterDeployment | Management/Regional | [Cluster Audit Policy](../admin/clusters/cluster-audit-policy.md) is configured                         |
| `Secret` (copy) | Same as kubeconfig secret reference from Region | Same as ClusterDeployment | Management          | ClusterDeployment is [deployed in a Region](../admin/regional-clusters/deploying-clusters-in-region.md) |

---

## Management Related Resources

Created by the **Management controller** to deploy platform components.

| Kind          | Name                                                    | Namespace             | Target Cluster | Condition                                                                                                                                                  |
|---------------|---------------------------------------------------------|-----------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `HelmRelease` | `<componentName>` (e.g., `kcm`, `capi`, provider names) | System (`kcm-system`) | Management     | Always per component in `.spec.core` / `.spec.providers`                                                                                                   |
| `Secret`      | `cld-registry-credentials`                              | System (`kcm-system`) | Management     | [Global registry with authentication credentials](appendix-extend-mgmt#configuring-a-custom-oci-registry-for-kcm-components) configured                    |
| `Secret`      | `<componentName>-variables`                             | System (`kcm-system`) | Management     | Per provider component when [global registry with authentication](appendix-extend-mgmt#configuring-a-custom-oci-registry-for-kcm-components) is configured |

---

## Template Related Resources

Created by the **Template controllers** (ClusterTemplate, ProviderTemplate, ServiceTemplate) to fetch and validate Helm charts.

| Kind             | Name                             | Namespace        | Target Cluster  | Condition                                                                                                                                                             |
|------------------|----------------------------------|------------------|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `HelmRepository` | `kcm-templates`                  | Same as Template | Management      | Always (default repository)                                                                                                                                           |
| `Secret` (copy)  | Same as source credential secret | Same as Template | Management      | Default HelmRepository has [authentication credentials (`registryCredsSecret`) configured](appendix-extend-mgmt#configuring-a-custom-oci-registry-for-kcm-components) |
| `Secret` (copy)  | Same as source credential secret | Same as Template | Management      | Default HelmRepository has [custom certificate (`registryCertSecret`) configured](appendix-extend-mgmt#configuring-a-custom-oci-registry-for-kcm-components)          |
| `HelmChart`      | `<templateName>`                 | Same as Template | Management      | Always                                                                                                                                                                |
| `ConfigMap`      | `schema-{ct\|pt}-<templateName>` | Same as Template | Management      | Chart contains `values.schema.json`                                                                                                                                   |

> NOTE:
> **Prefix key:** `ct` = ClusterTemplate, `pt` = ProviderTemplate

---

## Credential Related Resources

Created by the **Credential controller** to distribute cloud provider identities.

| Kind                                                                   | Name                           | Namespace            | Target Cluster      | Condition                                                                                                                                                               |
|------------------------------------------------------------------------|--------------------------------|----------------------|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Provider-specific `ClusterIdentity` (e.g., `AWSClusterStaticIdentity`) | Same as source ClusterIdentity | Credential namespace | Management/Regional | Credentials [distributed](../admin/access/credentials/cluster-identity-distribution.md) via `AccessManagement` or to regional clusters; released on Credential deletion |

---

## Region Related Resources

Created by the **Region controller** to manage connectivity and distribute objects that need to reside on regional clusters.

| Kind            | Name                                                    | Namespace             | Target Cluster  | Condition                                                                                                                                                     |
|-----------------|---------------------------------------------------------|-----------------------|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Secret` (copy) | `<cdNamespace>.<cdName>-kubeconfig`                     | System (`kcm-system`) | Management      | ClusterDeployment is [referenced](../admin/regional-clusters/regional-cluster-registration#region-object-with-a-clusterdeployment-reference) in a Region spec |
| `Secret` (copy) | Same as registry cert secret name (configured via flag) | System (`kcm-system`) | Regional        | [Registry certificate (`registryCertSecret`)](appendix-extend-mgmt#configuring-a-custom-oci-registry-for-kcm-components) is configured                        |
| `Secret` (copy) | Same as source proxy secret                             | System (`kcm-system`) | Regional        | [Proxy](proxy.md) is configured                                                                                                                               |

---

## Quick Reference by Resource Kind

| Resource Kind                       | Names Created by KCM                                                                                                                                                                       |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `HelmRelease`                       | `<cdName>`, `<componentName>`                                                                                                                                                              |
| `Secret`                            | `<cdName>-auth-config`, `cld-registry-credentials`, `<componentName>-variables`, regional kubeconfigs, registry certificate, registry credential, proxy config, HelmRepository auth config |
| `ConfigMap`                         | `<cdName>-audit-policy`, `schema-{ct\|pt}-<templateName>`                                                                                                                                  |
| `HelmRepository`                    | `kcm-templates`                                                                                                                                                                            |
| `HelmChart`                         | `<templateName>`                                                                                                                                                                           |
| Provider-specific `ClusterIdentity` | Same as source (provider-specific)                                                                                                                                                         |

> NOTE:
> - `cdName` = ClusterDeployment name
> - `<componentName>` = The name of the component (e.g., `kcm`, `capi`, provider names)
> - `<templateName>` = The name of the Cluster, Provider, or Service Template
> - `ct` = ClusterTemplate, `pt` = ProviderTemplate
