# k0rdent Observability & FinOps (KOF)

Running multiple clusters means you end up wrestling with half a dozen monitoring and cost tools, all with their own configs and upgrade headaches. k0rdent Observability & FinOps (KOF) saves you from duct-taping that stack together by bundling metrics, logs, traces, and cost tracking into one setup. It's built to roll out the same way everywhere, so you don’t have to reinvent the wheel every time you spin up a new cluster.

## KOF makes sure every cluster is observable and accountable for cost

{{{ docsVersionInfo.k0rdentName }}} estates can be large. They consist of a management cluster, potentially running many child (workload) clusters, often spread across multiple datacenters, regions, and clouds. In sthese kinds of environments, you need to both observe what clusters and workloads are doing (using metrics, logs, traces) and be accountable for what they cost (using allocation and trends).

KOF gives {{{ docsVersionInfo.k0rdentName }}} platform engineering teams the ability to guarantee that observability and cost management are deployed with every cluster they create, and then keep them consistent and automatically lifecycle-managed.

## Without KOF you would be forced to integrate and maintain multiple systems

KOF is optional, but if you were to build this yourself, you would need to select, integrate, and maintain separate systems for metrics, logs, tracing, dashboards, and cost visibility. At scale, this arrangement introduces persistent difficulties:

- **Component selection and versioning.** Each subsystem has its own CRDs, operators, and configuration. Keeping them consistent across many clusters is complex. Version skew and CRD drift cause brittle rollouts and difficult upgrades.  (See [OpenTelemetry Collector on Kubernetes](https://opentelemetry.io/docs/platforms/kubernetes/collector/).)

- **Cross-cluster aggregation.** To query estate-wide, you need to build federation or remote-write topologies. These can work, but are fragile and add operational overhead. (See [Prometheus federation](https://prometheus.io/docs/prometheus/latest/federation/).)

- **Retention and placement.** You need to plan where long-term metrics and logs live (per-cluster, regional, or dedicated) and engineer routing, storage, and query paths.

- **Access, identity, and network.** SSO, RBAC, mTLS, and inter-cluster routing must be implemented and maintained consistently across the estate.

KOF standardizes these decisions so they are consistent, repeatable, and auditable in k0rdent.

## KOF delivers unified observability and cost management across the estate

By packaging observability and FinOps as a single subsystem, KOF connects operational signals and cost signals:

- **Estate-wide visibility.** Every cluster participates, and data is aggregated centrally.
- **Actionable costs.** Workload and namespace spend is visible in the same dashboards as performance indicators.
- **Standardized retention.** Documented options define where data lives and how long it is kept.
- **Lifecycle management.** KOF is delivered as charts and operators, which can be consistently deployed and upgraded across the estate.
- **Compliance and audit.** Central policy ensures retention, RBAC, and secure transport are enforced everywhere.

Performance issues and cost spikes usually come from the same workloads, so you can't separate one from the other. When observability data and cost data live in the same place, it’s easier to spot the cause and fix both at once.

## KOF consists of well-established open source components wired for multi-cluster use

- **Metrics:** [VictoriaMetrics](https://docs.victoriametrics.com/) with vmcluster and vmauth.
- **Logs:** [VictoriaLogs](https://docs.victoriametrics.com/victorialogs/).
- **Tracing:** [Jaeger](https://www.jaegertracing.io/) with [OpenTelemetry](https://opentelemetry.io/).
- **Cost:** [OpenCost](https://opencost.io/).
- **Dashboards:** Grafana managed by grafana-operator.
- **Aggregation:** [Promxy](https://github.com/jacksontj/promxy) for Prometheus-compatible fan-out.
- **Control:** kof-operators for lifecycle and configuration.

KOF is deployed through Helm charts and MultiClusterServices: `kof-operators`, `kof-mothership`, `kof-storage`, `kof-collectors`, with optional `kof-istio`, plus per-role services such as `kof-child` and `kof-regional`. (See [KOF architecture](https://docs.k0rdent.io/latest/admin/kof/kof-architecture/).)

## KOF in Action: A Day in the Life (and A Sudden Cost Spike)

It’s Monday morning. Finance notices that last week’s cloud bill is **20% higher than forecast**. The CFO wants answers before the leadership meeting tomorrow.

Without KOF, this would trigger days of Slack threads and finger-pointing. With KOF, here’s what happens instead:

### Step 1: Finance Spots the Anomaly

The **Finance team** opens the KOF FinOps dashboard in Grafana. They see that most of the increase came from the **US-East regional cluster**, specifically from workloads tagged to the “recommendation-engine” project.

*What used to be a mystery bill is now an actionable insight.*

### Step 2: DevOps Traces the Issue

The **DevOps team** takes over. They drill into the same dashboard and pull up **OpenCost metrics** for that namespace. One service shows a sharp increase in CPU and memory usage starting on Friday.

To understand why, they pivot into **Jaeger traces**. The culprit emerges: a new API endpoint is generating far more queries than expected.

*What used to take days of log-diving is discovered in minutes.*

### Step 3: Platform Engineers Validate the Fix

The **Platform engineering team** checks KOF’s **cluster overview dashboards** to confirm whether this workload is affecting other services. They see elevated resource usage but no system-wide instability.

They work with DevOps to roll out a fix via GitOps: right-sizing the deployment and setting an alert for future usage spikes.

*What used to be firefighting is now controlled, repeatable operations.*

### Step 4: Finance Closes the Loop

By the end of the day, Finance refreshes the **chargeback dashboard**. Costs for the “recommendation-engine” namespace are already trending down. The CFO gets a simple, confident answer for tomorrow’s meeting:

"We found the root cause, we fixed it, and costs are back under control."

### The Outcome

* **Finance**: Cost visibility and accountability.
* **DevOps**: Faster root cause analysis, no wasted hours in silos.
* **Platform Engineers**: A clean GitOps workflow to fix the issue.
* **Leadership**: Confidence that teams are in control of performance *and* costs.

In a single day, KOF turned a vague cost spike into a resolved issue, with every team playing their part in one unified system.

# Getting Started

KOF lets you get started with some quick wins. For example, you can easily:

* Spin up a single cluster and access Grafana dashboards in under 10 minutes.
* Attribute cloud costs to teams immediately using OpenCost metrics.
* Configure alerts for both performance and budget thresholds.
* Start retaining logs and metrics for compliance right out of the box.


## KOF architecture places collectors everywhere and lets you choose where to store and aggregate

k0rdent defines a management cluster and many child clusters. KOF follows this and adds an optional regional role for storage and aggregation. Placement options are documented and configurable:

- **Child clusters.** Always run collectors (OpenTelemetry, OpenCost) to gather metrics, logs, and traces at the source. This is the "beach-head" service that travels with every cluster.

- **Management cluster.** Runs Grafana, promxy, operators, and policy. It may also run VictoriaMetrics for its own telemetry and alert evaluation via the `kof-mothership` chart.

- **Storage and aggregation.** The main VictoriaMetrics, VictoriaLogs, and Jaeger stack can run in:
  - the management cluster (for management data, with Grafana and VM provided by `kof-mothership`),
  - a regional KOF deployment (collecting from child clusters in that region), or
  - a third-party service for selected streams (for example, logs exported to AWS CloudWatch).
  See: [Storing KOF data](https://docs.k0rdent.io/latest/admin/kof/kof-storing/).

Data flows from child clusters into the chosen storage or aggregation point. On the management cluster, promxy and Grafana provide the consolidated UI.

## KOF can be extended with your own dashboards, pipelines, and destinations

KOF is fully functional out of the box, but you can also add additional capabilities through extensions.

- **Dashboards and alerts.** Add Grafana dashboards and VMRules in Git; k0rdent `MultiClusterService` distributes them consistently.
- **Collector pipelines.** Extend OpenTelemetry collectors with custom receivers, processors, or exporters.
- **External destinations.** Route specific streams to third-party systems (recipes are included for CloudWatch and others).

All extensions are managed through the same GitOps lifecycle as the rest of the platform.

## Managing KOF as Code

We recommend keeping a dedicated Git repository for your KOF deployment, separate from the {{{ docsVersionInfo.k0rdentName }}} repo itself and separate from application workload repos.

That repository should contain the Helm chart directories such as:

```
charts/
  kof-storage/
  kof-operators/
  kof-dashboards/
```

With this setup you can:
- Track all KOF configuration changes in Git.
- Use CI/CD pipelines to run `helm upgrade --install` against your management and regional clusters.
- Manage dashboards, retention policies, and observability settings as code for consistency across environments.

Other sections in this documentation, such as [Dashboard Lifecycle](kof-using.md) and [Retention](kof-retention.md) assume you have such a repo and a CI/CD pipeline in place.


## DIY Stack vs. KOF

| Dimension                  | DIY Stack (Prometheus, Grafana, OpenCost, Jaeger, etc.)                               | **KOF**                                                                                              |
| -------------------------- | ------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| **Setup & Integration**    | Assemble 4–6 separate projects, each with its own configs, upgrades, and quirks.      | One integrated platform: metrics, logs, traces, and costs shipped together.                          |
| **Scale & Performance**    | Prometheus federation slows at millions of samples; log systems require heavy tuning. | VictoriaMetrics/Logs designed for **millions of samples/sec**, fast queries, and long-term storage.  |
| **Consistency**            | Dashboards, alerts, and retention vary per cluster; drift happens quickly.            | **GitOps-native**: dashboards, alerts, and policies stored in Git and deployed via CI/CD.            |
| **Troubleshooting**        | Metrics in one tool, logs in another, traces in a third. Correlation is manual.       | Unified Grafana dashboards: metrics, logs, and traces correlated automatically.                      |
| **Cost Management**        | OpenCost must be bolted on; engineers rarely look at it.                              | Costs embedded in Grafana dashboards engineers already use; supports chargeback/showback.            |
| **Multi-Cluster Support**  | Each cluster runs its own observability stack; federation is fragile.                 | **Single control plane** for management, regional, and child clusters.                               |
| **Compliance & Retention** | Long-term retention requires custom S3/Elasticsearch setups, costly and brittle.      | Policy-driven retention (30–365+ days) and replication built in.                                     |
| **Security & Governance**  | Role-based access is piecemeal, TLS often manual.                                     | RBAC and secure communication enforced by default.                                                   |
| **Upgrades**               | Upgrade each component independently; breakage risk is high.                          | Guided version-to-version upgrades with clear migration paths.                                       |
| **Business Impact**        | Tools work, but require constant integration effort; finance rarely gets visibility.  | Engineers debug faster, finance gets cost accountability, compliance gets retention — in one system. |


## Guides

Get started with the basic documentation:

- [Architecture](kof-architecture.md)
- [Installing KOF](kof-install.md)
- [Verifying the KOF installation](kof-verification.md)
- [Storing KOF data](kof-storing.md)
- [Using KOF](kof-using.md)
- [KOF Alerts](kof-alerts.md)
- [KOF Tracing](kof-tracing.md)
- [Retention and Replication ](kof-retention.md)
- [Resources Requirements](kof-resources.md)
- [Scaling KOF](kof-scaling.md)
- [Maintaining KOF](kof-maintainence.md)
- [Upgrading KOF](kof-upgrade.md)
- [FAQ](kof-faq.md)

Once you have KOF up and running,
check [k0rdent/kof/docs](https://github.com/k0rdent/kof/tree/v{{{ extra.docsVersionInfo.kofVersions.kofDotVersion }}}/docs)
for advanced guides.
