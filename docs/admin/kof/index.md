# {{{ docsVersionInfo.k0rdentName }}} Observability and FinOps

{{{ docsVersionInfo.k0rdentName }}} Observability and FinOps ([kof](https://github.com/k0rdent/kof)) provides enterprise-grade observability
and FinOps capabilities for k0rdent-managed child Kubernetes clusters.
It enables centralized metrics, logging, and cost management
through a unified [OpenTelemetry](https://opentelemetry.io/docs/)-based architecture.

* **Observability**: KOF collects **metrics** from various sources and stores them in a time series database
based on [Victoria Metrics](https://github.com/victoriaMetrics/VictoriaMetrics/), allowing for real-time and historical analysis.
It includes **log management** features to aggregate, store, and analyze logs from different 
components of the Kubernetes ecosystem. This helps in troubleshooting and understanding the behavior of applications and infrastructure.
KOF can evaluate **alerting** rules and send notifications based on these collected metrics and logs helping to identify and respond to issues before they impact users.

* **FinOps**: KOF helps with **cost management** by tracking and managing the costs associated with running applications on Kubernetes. 
It provides insights into resource utilization and helps in optimizing costs by identifying underutilized or over-provisioned resources.

* **Centralized Management**: KOF provides a **unified control plane** for managing Kubernetes clusters at scale, with a 
centralized view of all clusters, making it possible to use {{{ docsVersionInfo.k0rdentName }}} to manage and operate large-scale deployments.
It also offers comprehensive **lifecycle management** capabilities, including provisioning, 
configuration, and maintenance of Kubernetes clusters, ensuring clusters are consistently managed and adhere to best practices.

* **Scalability and Performance**: KOF leverages components such as VictoriaMetrics to provide **high-performance** monitoring and analytics. 
It can handle millions of metrics per second and provides low-latency query responses. It's also designed to **scale** horizontally, enabling it to manage large volumes of data and support growing environments. It can be deployed on-premises, in the cloud, or in hybrid environments.

* **Compliance and Security**: KOF helps ensure **compliance** with organizational policies and industry standards, providing
audit trails and reporting features to meet regulatory requirements. It includes **security** features to protect data and ensure 
the integrity of monitoring and FinOps processes. It supports role-based access control (RBAC) and secure communication protocols.

## Use Cases

KOF can be used by both technical and non-technical arms of a company.

* **Platform Engineering:** KOF is ideal for platform engineers who need to manage and monitor Kubernetes 
clusters at scale. It provides the tools and insights required to ensure the reliability and performance of applications.
* **DevOps Teams:** DevOps teams can use KOF to gain visibility into the deployment and operation of applications, 
helping them to identify and resolve issues quickly.
* **Finance Teams:** Finance teams can leverage KOF's FinOps capabilities to track and manage cloud spending, 
ensuring resources are used efficiently and costs are optimized.

## Guides

Get started with the basic documentation:

- [Architecture](kof-architecture.md)
- [Installing KOF](kof-install.md)
- [Verifying the KOF installation](kof-verification.md)
- [Storing KOF data](kof-storing.md)
- [Using KOF](kof-using.md)
- [KOF Alerts](kof-alerts.md)
- [Scaling KOF](kof-scaling.md)
- [Maintaining KOF](kof-maintainence.md)

Once you have KOF up and running,
check [k0rdent/kof/docs](https://github.com/k0rdent/kof/tree/v{{{ extra.docsVersionInfo.kofVersions.kofDotVersion }}}/docs)
for advanced guides.
