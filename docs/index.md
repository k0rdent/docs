# Welcome to the {{{ docsVersionInfo.k0rdentName }}} docs

## Introduction

{{{ docsVersionInfo.k0rdentName }}} has been developed to provide a way to manage distributed infrastructure
at massive scale leveraging kubernetes.

The project is based on the premise that:

* Kubernetes and its ecosystem are mature and inherently stable.
* Large scale adoption of Kubernetes means that {{{ docsVersionInfo.k0rdentName }}} can run anywhere.
* Community standards and open source projects ensure support and reduce adoption risk.

The goal of the {{{ docsVersionInfo.k0rdentName }}} project is to provide platform engineers with the means
to deliver a distributed container management environment (DCME) and enable them to
compose unique internal developer platforms (IDP) to support a diverse range
of complex modern application workloads.

Another way to think of {{{ docsVersionInfo.k0rdentName }}} is as a "super control plane" designed to ensure the
consistent provisioning and lifecycle management of kubernetes clusters and the
services that make them useful.

In short:
Kubernetes clusters at scale, managed centrally, template driven, based on open
community driven standards, enabling Golden Paths ... {{{ docsVersionInfo.k0rdentName }}} aspires to do all of that.

Whether you want to manage Kubernetes clusters on-premises, in the cloud,
or a combination of both, {{{ docsVersionInfo.k0rdentName }}} provides a consistent way to do it. With
full life-cycle management, including provisioning, configuration, and
maintenance, {{{ docsVersionInfo.k0rdentName }}} is designed to be a repeatable and secure way to
manage your Kubernetes clusters in a central location.

## Structure and History

The project has a number of components, including:

* **k0rdent**: the overall project

    * **k0rdent Cluster Manager (KCM)**

        Deployment and life-cycle management of Kubernetes clusters, including
        configuration, updates, and other CRUD operations.

    * **k0rdent State Manager (KSM)**

        Installation and life-cycle management of deployed services.

          * This is currently rolled into kcm, but may be split out in the future
          * ksm leverages [Project Sveltos](https://github.com/projectsveltos/sveltos)
            for an increasing amount of functionality

    * **k0rdent Observability and FinOps (KOF)**

        Cluster and beach-head services monitoring, events and log management.

There are a few historical names that may show up in the code and in older docs, including:

* **Project 2A**: the original codename of k0rdent, 2A references the hexadecimal 0x2A, 
  or 42, which encompasses our hopes for the project.
* **HMC or hmc**: the original repository name for k0rdent and KCM
  development
* **motel**: the original repository and codename for KOF

## Quick Start

See the [{{{ docsVersionInfo.k0rdentName }}} Quick Start Guide](quickstarts/index.md) to get started with a small deployment.

## Supported Providers

{{{ docsVersionInfo.k0rdentName }}} leverages the Cluster API provider ecosystem; the following
providers have had `ProviderTemplates` created and validated, and more are
in the works. 

* [AWS](admin/installation/prepare-mgmt-cluster/aws.md)
* [Azure](admin/installation/prepare-mgmt-cluster/azure.md)
* [vSphere](admin/installation/prepare-mgmt-cluster/vmware.md)
* [OpenStack](admin/installation/prepare-mgmt-cluster/openstack.md)
* [GCP](admin/installation/prepare-mgmt-cluster/gcp.md)

{{{ docsVersionInfo.k0rdentName }}} also includes a way to add custom providers, so it's possible to integrate it with other hyperscalers, 
or even into an existing local infrastructure.

## Development Documentation

Documentation related to the development process and developer-specific notes is
located in the [main k0rdent repository](https://github.com/k0rdent/kcm/blob/main/docs/dev.md).

## Where to go from here

This documentation covers all aspects of administering, using, and contributing to {{{ docsVersionInfo.k0rdentName }}}, including:

- [{{{ docsVersionInfo.k0rdentName }}} concepts](concepts/index.md)
- [QuickStarts](quickstarts/index.md)
- [Administrator Guide](admin/index.md)
- [User Guide](user/index.md)
- [{{{ docsVersionInfo.k0rdentName }}} Templates Reference](reference/template/index.md)
- [Troubleshooting](troubleshooting/index.md)
- [Glossary](appendix/glossary.md)
- [Appendix](appendix/index.md)
- [Contributor's Guide](contrib/index.md)
