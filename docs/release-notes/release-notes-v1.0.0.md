
# k0rdent OSS v1.0.0 Release Notes

Released: May 20, 2025

k0rdent OSS is the upstream, community-driven version of the k0rdent platform, released under the Apache 2.0 license. It delivers the core functionality of k0rdent as an open, composable control plane for managing Kubernetes clusters, services, and observability across public clouds, private data centers, and edge environments.

## OSS Component Breakdown

-   **KCM (k0rdent Cluster Management)**
    Manages provisioning, upgrade, scaling, and lifecycle of Kubernetes clusters via Cluster API.
    
-   **KSM (k0rdent State Management)**
    Uses declarative, templated ServiceTemplates to manage consistent deployment of services like Istio, Flux, and cert-manager across clusters.
    
-   **KOF (k0rdent Observability & FinOps)**
    Provides metrics, logs, dashboards, and cost visibility using VictoriaMetrics and OpenCost integration.

## Major Highlights

This GA release of the full k0rdent OSS platform includes:

-   Fully stabilized v1beta1 APIs across all components
-   Production-grade multi-cluster support
-   Enterprise-ready service templating and orchestration
-   Integrated observability stack with AI/ML workload support

## New Features

### Multi-Cluster Management

-   **ServiceTemplateChains**

    Enables conditional, chained service deployments with upgrade paths  
    [*#1433 · simplifies complex service topologies*]
    
-   **Global Values Support**

    Reuse consistent variables across ClusterTemplates and ProviderTemplates  
    [*#1535 · ensures DRY, repeatable infrastructure definitions*]
    
-   **IPAM Controller Integration**

    Automates IP address management across environments  
    [*#1260 · removes manual allocation and avoids IP conflicts*]
    

### Observability Enhancements (KOF)

-   **NVIDIA GPU Monitoring**

    Native Grafana dashboards for AI/ML workloads  
    [*#257 · visibility into GPU utilization without extra config*]
    
-   **Kube API Server Metrics**

    Adopts OpenTelemetry-based monitoring of API server health  
    [*#259 · immediate insights into control plane performance*]
    
-   **VictoriaMetrics Log Cluster Migration**

    Scalable logging stack with high-retention support  
    [*#274 · improved storage efficiency and performance*]
    
-   **Cluster Annotation Support for Promxy/Datasource Config**

    Allows per-cluster HTTP config customization  
    [*#276*]

-   **Custom Resource Limits for Observability Stack**

    Fine-tune Grafana and VM components  
    [*#263 · optimize memory/CPU usage across environments*]
    
## Notable Fixes

-   Fixed invalid CR references in OpenStack/IPAM providers 
    [*#1522, #1496*]
-   Improved e2e test reliability and configuration fetching 
    [*#1517, #1463*]
-   Fixed resource tuning for VM services 
    [*#279*]
-   Corrected Istio remote secret creation 
    [*#270*]
-   Addressed Helm/YQ compatibility issue (2-arg enforcement) 
    [*#282*]

## Component & Provider Versions

| Component / Provider          | Version          |
|-------------------------------|------------------|
| Cluster API                   | v1.9.7           |
| CAPI Provider AWS             | v2.8.2           |
| CAPI Provider Azure           | v1.19.4          |
| CAPI Provider Docker          | v1.9.6           |
| CAPI Provider GCP             | v1.8.1           |
| CAPI Provider Infoblox        | v0.1.0-alpha.8   |
| CAPI Provider IPAM            | v0.18.0          |
| CAPI Provider k0smotron       | v1.5.2           |
| CAPI Provider OpenStack (ORC) | v0.12.3 / v2.1.0 |
| CAPI Provider vSphere         | v1.13.0          |
| Project Sveltos               | v0.54.0          |


## Platform Benefits in v1.0.0

- Declarative, template-driven provisioning of clusters and services  
- Observability built-in, including GPU and API metrics  
- GitOps-ready: compatible with ArgoCD, FluxCD, Velero, etc.  
- Unified Kubernetes-native APIs with long-term schema stability

## Upgrade Notes

-   Ensure all `ClusterTemplate`, `ServiceTemplate`, and `ProviderTemplate` definitions are updated to use `apiVersion: v1beta1`.
-   Custom tooling or integrations built on v1alpha1 resources must be updated.
-   We recommend creating a Velero backup of your management cluster before upgrade.
-   Use helm upgrade `--reuse-values` to preserve your existing configuration.

## Deprecations

-   All `v1alpha1` APIs are now deprecated and will be removed in a future release.
-   Support for the legacy `loki-stack` logging backend has been removed. Migrate to the `victoria-log-cluster` stack.

## Known Issues

-   Grafana dashboards may take up to 60 seconds to initialise after cluster deployment.
-   MultiClusterService priority conflicts may require manual resolution if priorities are equal.
-   In high-latency networks, IPAM reconciliation can be delayed.
-   Velero restore across cloud providers may require exclusion of specific resources (see docs).
    
## Release Metadata

| Key                   | Value                              |
| --------------------- | ---------------------------------- |
| Helm Charts           | kcm: 1.0.0, kof: 1.0.0, ksm: 1.0.0 |
| OCI Registry          | ghcr.io/k0rdent                    |
| SBOM                  | Not included in OSS                |
| OCI Signature Support | Enterprise only                    |
| Release Tags          | v1.0.0 across all components       |

## Contributors

Huge thanks to the following contributors for making this release possible:  
[@gmlexx](https://github.com/gmlexx), [@denis-ryzhkov](https://github.com/denis-ryzhkov), [@ramessesii2](https://github.com/ramessesii2), [@aglarendil](https://github.com/aglarendil), [@kylewuolle](https://github.com/kylewuolle), [@a13x5](https://github.com/a13x5), [@eromanova](https://github.com/eromanova), [@zerospiel](https://github.com/zerospiel), [@BROngineer](https://github.com/BROngineer), [@cdunkelb](https://github.com/cdunkelb)

## Resources

-   [Documentation](https://k0rdent.github.io/docs)
-   [GitHub Repositories](https://github.com/k0rdent)
-   CNCF Slack Channels: #k0rdent

## Try It Out

QuickStart guide: [https://docs.k0rdent.io/1.0.0/quickstarts/](https://docs.k0rdent.io/1.0.0/quickstarts/)