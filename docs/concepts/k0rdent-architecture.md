# {{{ docsVersionInfo.k0rdentName }}} architecture

The {{{ docsVersionInfo.k0rdentName }}} architecture follows a [declarative approach](../appendix/glossary.md#declarative-approach) to cluster management using Kubernetes principles. The modular extensible architecture provides for a repeatable template-driven solution to interact with sub components such as the Cluster API (CAPI) and other Kubernetes components.

The key principles of the architecture include:

* The leveraging of Kubernetes core principles
* A highly aligned but loosely coupled architecture
* A pluggable and extensible architecture
* A template-driven approach for repeatability
* A standards-driven API
* The leveraging of unmodified upstream components (for example, the Kubernetes Cluster API)
* Support for integration with custom components downstream

> NOTE:
> This document is a ongoing work in progress, and we would welcome suggestions and questions. 

## Overview

The {{{ docsVersionInfo.k0rdentName }}} Management Cluster orchestrates the provisioning and lifecycle of multiple child clusters on multiple clouds and infrastructures, keeping you from having to directly interact with individual infrastructure providers. By abstracting the infrastructure in this way, {{{ docsVersionInfo.k0rdentName }}} promotes reusability (reducing, for example, the effort required to implement an IDP on a particular cloud), encourages standardization where practical, and lets you use the clouds and technologies you want, while also minimizing the cost of switching components such as open source subsystems, cloud substrates, and so on.

The {{{ docsVersionInfo.k0rdentName }}} architecture comprises the following high level components:

* **Cluster Management:** Tools and controllers for defining, provisioning, and managing clusters.
* **State Management:** Controllers and systems for monitoring, updating, and managing the state of child clusters and their workloads.
* **Infrastructure Providers:** Services and APIs responsible for the under-the-hood provisioning resources such as virtual machines, networking, and storage for clusters.
* **Templates:** Templates define managed child clusters or the workloads that run on them. Instantiating those templates creates the corresponding resources.

![{{{ docsVersionInfo.k0rdentName }}} Architecture - Simplified](../assets/k0rdent-highlevel-architecure-overview.svg)

## Management cluster

The management cluster is the core of the {{{ docsVersionInfo.k0rdentName }}} architecture. It hosts all of the controllers needed to make {{{ docsVersionInfo.k0rdentName }}} work. This includes:

* **k0rdent Cluster Manager (KCM) Controller:**  KCM provides a wrapper for {{{ docsVersionInfo.k0rdentName }}}’s CAPI-related capabilities. It orchestrates:
    * **Cluster API (CAPI) Controllers:** CAPI controllers are designed to work with specific infrastructure providers. For example, one CAPI controller manages the creation and lifecycle of Kubernetes clusters running on Amazon Web Services, while another manages those on Azure. It’s also possible to create custom CAPI controllers to integrate with internal systems.
    * **k0smotron Controller:** k0smotron extends CAPI with additional functionality, including control plane and worker node bootstrap providers for k0s Kubernetes and a control plane provider that supports the creation of a Hosted Control Plane, or a k0s control plane represented by pods on a host Kubernetes cluster, which can be the same cluster that hosts {{{ docsVersionInfo.k0rdentName }}}. The k0smotron project has also provided a so-called ‘RemoteMachine’ infrastructure provider for CAPI, enabling deployment and cluster operations via SSH on arbitrary remote Linux servers (including small-scale edge devices).
* **{{{ docsVersionInfo.k0rdentName }}} Service Manager (KSM) Controller:** KSM is responsible for lifecycle managing (deploy, scale, update, upgrade, teardown) services and applications on clusters, and for doing continuous state management of these services and applications. This is currently part of the KCM code base; we may split it out in the future. It orchestrates:
    * **Services Controller:** Responsible for coordinating Kubernetes services, such as combinations of services and infrastructure provisioning dependencies that add capabilities to the platform. For example, Nginx, with its dependencies, can be packaged as a service. Artifacts for services are stored locally or in an OCI repository, and are referenced as kubernetes CRD objects.
* **{{{ docsVersionInfo.k0rdentName }}} Observability & FinOps (KOF) Controller (not depicted in above diagram):** {{{ docsVersionInfo.k0rdentName }}} Observability and FinOps provides enterprise-grade observability and FinOps capabilities for k0rdent-managed Kubernetes clusters. It enables centralized metrics, logging, and cost management through a unified OpenTelemetry-based architecture.

We’ll take a closer look at these pieces under [Roles and Responsibilities](#roles-and-responsibilities).

## Cluster Deployments

A cluster deployment is also known as a child cluster, or a workload cluster. It’s a Kubernetes cluster provisioned and managed by the management cluster, and it’s where developers run their applications and workloads. These are “regular” Kubernetes clusters, and don’t host any management components. Clusters are fully isolated from the management cluster via namespaces, and also from each other, making it possible to create multi-tenant environments. 

You can tailor a child cluster to specific use cases, with customized addons such as ingress controllers, monitoring tools, and logging solutions. You can also define specific Kubernetes configurations (for example, network policies, storage classes, and security policies) so they work for you and your applications or environments.

Simply put, child clusters are where applications and workloads run.

## Templates

One of the important tenets of the platform engineering philosophy is the use of Infrastructure as Code, but {{{ docsVersionInfo.k0rdentName }}} takes that one step further through the use of templates. Templates are re-usable text definitions of components that can be used to create and manage clusters. Templates provide a declarative way for users and developers to deploy and manage complex clusters or components while massively reducing the number of parameters they need to configure. Considered generally, {{{ docsVersionInfo.k0rdentName }}} templates are:

* **Formatted using YAML:** Templates use YAML as an abstraction to represent the target state, so they’re human-readable and editable.
* **Designed to be used in multiple contexts using runtime parameterization:** Through the use of placeholders, you can customize templates at runtime without having to directly edit the template.
* **Used for both cluster creation and addon management:** Users can define a cluster using YAML, or they can define addons, such as an ingress operator or monitoring tools, to be added to those clusters.
* **Capable of limited scope:** {{{ docsVersionInfo.k0rdentName }}} lets you set restrictions over what templates can be deployed by whom. For example, as the platform manager (see [Roles and Responsibilities](#roles-and-responsibilities)), you can specify that non-admin users can only execute templates that deploy a particular set of controllers.

Major template types used in {{{ docsVersionInfo.k0rdentName }}} include:

* **Cluster Templates:** `ClusterTemplate` objects define clusters in coordination with the clouds and infrastructures on which they run. They're designed to be immutable; they get invoked by {{{ docsVersionInfo.k0rdentName }}} objects such as `ClusterDeployment` objects to create and manage individual clusters and groups of clusters.
* **Service Templates:** `ServiceTemplate` objects define services, addons, and workloads that run on clusters. They're also designed to be immutable, and get invoked by `ClusterDeployment` objects and other {{{ docsVersionInfo.k0rdentName }}} objects so that IDPs/platforms can be declared and managed as units. 

## Roles and responsibilities

{{{ docsVersionInfo.k0rdentName }}} was designed to be used by several groups of people, with hierarchical and complementary roles and responsibilities. You may have your own names for them, but we’ll refer to them as:

* **Platform Architect:** This person or team has global responsibility to the business and technical stakeholders for designing IDPs/platforms for later adaptation to particular clouds and infrastructures, workloads, performance and cost objectives, security and regulatory regimes, and operational requirements. {{{ docsVersionInfo.k0rdentName }}} enables Platform Architects to create sets of reusable `ClusterTemplate` and `ServiceTemplate` objects, closely defining IDPs/platforms in the abstract.
* **Platform Lead:** This person or team (sometimes referred to as 'CloudOps') is primarily responsible for actions corresponding to {{{ docsVersionInfo.k0rdentName }}} Cluster Manager (KCM). They adapt `ClusterTemplate` objects to the correct cloud, and they make sure that everything is working properly. They’re also responsible for limiting the Project Team’s access to the `Cluster` and `Service` templates necessary to do their jobs. For example, they might limit the templates that can be deployed to an approved set, or provide CAPI operators for only the clouds on which the company wants applications to run, helping to eliminate shadow IT. 
* **Platform Engineer:** This person or team is responsible for the day-to-day management of the environment. They use `ClusterTemplate` and `ServiceTemplate` objects provided by the Platform Lead (as authorized to do so) and may create additional `ServiceTemplate` objects to customize their own Kubernetes cluster so that it's appropriate for their application.

## Credentials

Creating and managing Kubernetes clusters requires having the proper permissions on the target infrastructure, but you certainly wouldn't want to give out your AWS account information to every single one of your developers.

To solve this problem, {{{ docsVersionInfo.k0rdentName }}} lets you create a `Credential` object that provides the access your developers need. It works like this:

1. The platform lead creates a provider-specific `ClusterIdentity` and `Secret` that include all of the information necessary to perform various actions.
2. The platform lead then creates a `Credential` object that references the `ClusterIdentity`.
3. Developers reference the `Credential` object, which gives the cluster the ability to access these credentials (little “c”) without having to expose them to developers directly.

## TL;DR - Conclusion

{{{ docsVersionInfo.k0rdentName }}} provides a comprehensive Kubernetes lifecycle management framework through its three core components:

* **KCM:** Cluster provisioning and management
* **KSM:** Application and runtime state management
* **KOF:** Observability, logging, and cost optimization

With multi-provider support, templated deployments, and strong security controls, {{{ docsVersionInfo.k0rdentName }}} is being built to enable scalable, efficient, and consistent Kubernetes operations.
