# Guide to QuickStarts

The following QuickStart chapters provide a recipe for quickly installing and trying {{{ docsVersionInfo.k0rdentName }}}. Setting up {{{ docsVersionInfo.k0rdentName }}} for production is detailed in the [Administrator Guide](../admin/index.md).

## What the QuickStart covers

The goal of the QuickStart is:

* To get a working environment set up for managing {{{ docsVersionInfo.k0rdentName }}}.
* To get a Kubernetes cluster and other tools set up for hosting {{{ docsVersionInfo.k0rdentName }}} itself.
* To select a cloud environment (AWS or Azure) and configure {{{ docsVersionInfo.k0rdentName }}} to lifecycle manage clusters on this substrate.
* To use {{{ docsVersionInfo.k0rdentName }}} to deploy a managed cluster.
* (Optional stretch goal) It's also possible to set up the {{{ docsVersionInfo.k0rdentName }}} management cluster to simultaneously lifecycle manage clusters on _both_ cloud environments.

## Where the QuickStart leads

The QuickStart shows and briefly explains the hows, whys, and wherefores of manually setting up {{{ docsVersionInfo.k0rdentName }}} for use. Once built and validated, the QuickStart setup can be leveraged to begin [an expanding sequence of demos](https://github.com/k0rdent/demos) that let you explore {{{ docsVersionInfo.k0rdentName }}}'s many features. The demos presently use makefiles to speed and simplify setup and operations. We strongly recommend exploring this fast-evolving resource.

## QuickStart Prerequisites

QuickStart prerequisites are simple &mdash; you'll need:

* A desktop or virtual machine running a [supported version of linux](#supported-operating-systems). You'll use this machine to install a basic Kubernetes working environment, and to host a single-node k0s Kubernetes management cluster to host {{{ docsVersionInfo.k0rdentName }}} components. For simplest setup, configure this machine as follows:
  * A minimum of 8GB RAM, 4 vCPUs, 100GB SSD (for example, AWS `t2.xlarge` or equivalent)
  * Set up for SSH access using keys (standard for cloud VMs)
  * Set up for passwordless sudo (that is, edit `/etc/sudoers` to configure your user to issue `sudo` commands without a password challenge)
  * Inbound traffic: SSH (port 22) and ping from your laptop's IP address
  * Outbound traffic: All to any IP address
  * Apply all recent updates and upgrade local applications (`sudo apt update`/`sudo apt upgrade`)
  * (Optional) snapshot the machine in its virgin state
* Administrative-level access to an AWS or Azure cloud account, depending on which cloud environment you prefer. {{{ docsVersionInfo.k0rdentName }}} will leverage this cloud to provide infrastructure for hosting child clusters.

### Supported Operating Systems

Any linux based os that supports deploying [k0s](https://k0sproject.io/) will work, though you may need to adjust the suggested commands.


| OS | Package Manager | Link|
|----|-----------------|-----|
|Ubuntu Server| `apt` | [22.04.5 LTS, Jammy Jellyfish](https://releases.ubuntu.com/jammy/) |

> NOTE: 
> Other recent versions of 'enterprise' Linux should work with the
> following instructions as well, though you will need to adapt for
> different package managers and perhaps use slightly-different
> provider-recommended methods for installing required dependencies
> (for example, Helm). Once you've installed {{{ docsVersionInfo.k0rdentName }}} in the management cluster
> and have kubectl, Helm, and other resources connected, you'll mostly
> be dealing with Kubernetes, and everything should work the same way on
> any host OS.

## Limitations

This QuickStart guides you in quickly creating a minimal {{{ docsVersionInfo.k0rdentName }}} working environment. Setting up {{{ docsVersionInfo.k0rdentName }}} for production is detailed in the [Administrator Guide](../admin/index.md).

The current QuickStart focuses on AWS and Azure cloud environments, and guides in creating 'standalone' clusters. In {{{ docsVersionInfo.k0rdentName }}} parlance, that means 'CNCF-certified Kubernetes clusters with control planes and workers hosted on cloud virtual machines.' The 'CNCF-certified Kubernetes cluster' (in this case) is the [k0s Kubernetes distro](https://k0sproject.io).

{{{ docsVersionInfo.k0rdentName }}} can do so much more today. Let's take a look at what's possible.

## Coming soon

QuickStarts for other Kubernetes distros, clouds, and environments will appear in the near future (short-term roadmap below):

* **AWS EKS hosted** &mdash; Amazon Elastic Kubernetes Service managed clusters 
* **Azure AKS hosted** &mdash; Azure Kubernetes Service
* **vSphere standalone** &mdash; k0s Kubernetes on vSphere virtual machines
* **OpenStack standalone** &mdash; k0s Kubernetes on OpenStack virtual machines

Plus (intermediate-term roadmap) tutorials for using {{{ docsVersionInfo.k0rdentName }}} to create and manage hybrid, edge, and distributed platforms with Kubernetes-hosted control planes and workers on local or remote substrates will be available soon.

**Demo/Tutorials:** We will also be converting the demos gradually into tutorials that explain how to use {{{ docsVersionInfo.k0rdentName }}} for:

* Adding services to individual managed clusters, enabling management of complete platforms/IDPs
* Adding services to multiple managed clusters, enabling at-scale implementation and lifecycle management of standardized environments
* (As a Platform Architect) Authorizing cluster and service templates for use by others, and constraining their use within guardrails (enabling self-service)
* (As an authorized user) Leveraging shared cluster and service templates to lifecycle manage platforms (performing self-service)
* ... and more

Next you'll want to learn how to:

- [Set up the Management Node and Cluster](quickstart-1-mgmt-node-and-cluster.md)
- [Configure and Deploy to AWS](quickstart-2-aws.md)
- [Configure and Deploy to Azure](quickstart-2-azure.md)
- [Configure and Deploy on any SSH-accessible Linux hosts](quickstart-2-remote.md)
- [Configure and Deploy to GCP](quickstart-2-gcp.md)
