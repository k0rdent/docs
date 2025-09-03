# How to Build a {{{ docsVersionInfo.k0rdentName }}} ClusterTemplate

One of the most important benefits of {{{ docsVersionInfo.k0rdentName }}} is the ability to create your own `ClusterTemplate` objects.

## Introduction: Templates in {{{ docsVersionInfo.k0rdentName }}}

In {{{ docsVersionInfo.k0rdentName }}}, almost everything you deploy or extend is expressed through **templates**. Templates provide a standardized way to describe complex Kubernetes resources and workflows so they can be reused, versioned, and shared. Whether you are provisioning an entire cluster, adding services on top of it, or integrating a new infrastructure provider, you interact with {{{ docsVersionInfo.k0rdentName }}} through one of three template types:

- `ClusterTemplates`: `ClusterTemplates` define clusters, packaging all the infrastructure, control plane, and machine objects required to stand up a Kubernetes environment.  
- `ServiceTemplates`: `ServiceTemplates` define additional services and applications that run on clusters, such as networking, monitoring, or data platforms.  
- `ProviderTemplates`: `ProviderTemplates` define CAPI infrastructure or bootstrap providers themselves, making them available to clusters.  

Although their use cases differ, these templates share the same architectural foundations. All of them ultimately reference **Helm charts**, which bundle Kubernetes manifests into reusable, versioned packages. All of them are retrieved and managed by **FluxCD**, which acts as the continuous delivery engine inside {{{ docsVersionInfo.k0rdentName }}}. And all of them are reconciled by **Cluster API (CAPI)** providers and other controllers, which take the rendered manifests and turn them into running infrastructure and services.  

Understanding this architectural pattern is essential before diving into `ClusterTemplates` specifically, because once you know how templating works in {{{ docsVersionInfo.k0rdentName }}}, you can apply the same mental model to service and provider definitions as well.

## What Do We Mean by “Templates”?

In software, a template is a model: a pre-defined structure that can be filled in with values to create many variations of the same kind of thing. Templating systems exist everywhere in computing. A web page template defines a layout that different content can populate. A configuration template defines settings that can be applied to different environments. In Kubernetes, templating is especially useful because clusters and workloads are defined as YAML manifests — verbose, repeatable, but often tedious to write and error-prone when copied by hand.

{{{ docsVersionInfo.k0rdentName }}} uses templates to solve exactly this problem. Instead of requiring users to manually assemble dozens of Kubernetes resources, {{{ docsVersionInfo.k0rdentName }}} provides a system where the right resources are already packaged together, their parameters exposed in a consistent way, and their lifecycle managed by controllers. With templates, you can declare intent at a high level (“I want an AWS cluster with three control plane nodes and five workers”) and trust {{{ docsVersionInfo.k0rdentName }}} to render, validate, and deploy all the underlying objects correctly.

This approach has several benefits:

- **Reusability:** A template can be shared across many deployments, ensuring consistent architecture.  
- **Configuration management:** Parameters are centralized in a `values.yaml` file, which acts like a set of variables.  
- **Upgradeability:** Because templates are versioned charts, you can move between releases safely and predictably.  
- **Governance and validation:** Templates can include schemas that enforce correct usage and prevent invalid settings.  

In {{{ docsVersionInfo.k0rdentName }}}, templates are therefore not just convenience wrappers — they are the backbone of how infrastructure and services are declared, standardized, and delivered.

## The Role of Helm, Flux, and CAPI

Every template in {{{ docsVersionInfo.k0rdentName }}} is powered by a trio of technologies:

- **Helm** provides the packaging format. A Helm chart is essentially a directory containing Kubernetes manifests (in the `templates/` folder), a metadata file (`Chart.yaml`), a values file (`values.yaml`), and optionally a schema file (`values.schema.json`). Helm’s templating engine replaces placeholders in manifests with values supplied by the user.  

- **FluxCD** provides the source management and installation mechanism. Flux fetches Helm charts from Git repositories, OCI registries, or buckets, and ensures that the correct version is available to {{{ docsVersionInfo.k0rdentName }}}. Flux also runs the Helm Controller, which is responsible for rendering and installing charts into clusters.  

- **Cluster API (CAPI)** provides the reconciliation logic. Once the chart is rendered into Kubernetes manifests, CAPI controllers reconcile the resources and create real infrastructure. For example, the CAPI AWS provider reconciles `AWSCluster` and `AWSMachine` objects into EC2 instances, while the k0smotron controller reconciles `K0sControlPlane` objects into running control plane nodes.  

These three components work together so that a single `ClusterTemplate` reference can ultimately produce a fully functioning Kubernetes cluster.

## Anatomy of a ClusterTemplate

A `ClusterTemplate` in {{{ docsVersionInfo.k0rdentName }}} is a Kubernetes custom resource that points to a Helm chart. The chart itself contains all the CAPI objects required to define a cluster. A typical chart structure might look like this:

```
├── Chart.yaml
├── templates
│   ├── awscluster.yaml
│   ├── awsmachinetemplate-controlplane.yaml
│   ├── awsmachinetemplate-worker.yaml
│   ├── cluster.yaml
│   ├── k0scontrolplane.yaml
│   ├── k0sworkerconfigtemplate.yaml
│   └── machinedeployment.yaml
├── values.schema.json
└── values.yaml
```

- `Chart.yaml` contains metadata: chart name, version, and description.  
- `values.yaml` contains the default configuration parameters, such as cluster size, networking, and AMI IDs.  
- `values.schema.json` can restrict or validate the parameters that users supply.  
- The `templates/` directory contains Kubernetes manifests for CAPI objects, such as `Cluster`, `AWSCluster`, machine templates, and control plane definitions.  

By changing the values in `values.yaml`, you can produce many different clusters without modifying the underlying templates.

## Default values.yaml Example

The following snippet shows the default `values.yaml` for the AWS standalone control plane `ClusterTemplate`. This file is the main entry point for customization.

```yaml
controlPlaneNumber: 3
workersNumber: 2

clusterNetwork:
  pods:
    cidrBlocks:
      - "10.244.0.0/16"
  services:
    cidrBlocks:
      - "10.96.0.0/12"

clusterLabels: {}
clusterAnnotations: {}

region: ""
sshKeyName: ""
publicIP: false
bastion:
  enabled: false
  disableIngressRules: false
  allowedCIDRBlocks: []
  instanceType: t2.micro
  ami: ""
clusterIdentity:
  name: ""
  kind: "AWSClusterStaticIdentity"

controlPlane:
  amiID: ""
  iamInstanceProfile: control-plane.cluster-api-provider-aws.sigs.k8s.io
  instanceType: ""
  rootVolumeSize: 8
  imageLookup:
    format: "amzn2-ami-hvm*-gp2"
    org: "137112412989"
    baseOS: ""
  uncompressedUserData: false
  nonRootVolumes: []

worker:
  amiID: ""
  iamInstanceProfile: control-plane.cluster-api-provider-aws.sigs.k8s.io
  instanceType: ""
  rootVolumeSize: 8
  imageLookup:
    format: "amzn2-ami-hvm*-gp2"
    org: "137112412989"
    baseOS: ""
  uncompressedUserData: false
  nonRootVolumes: []

k0s:
  version: v1.32.6+k0s.0
  arch: amd64
  cpArgs: []
  workerArgs: []
  api:
    extraArgs: {}
  files: []
```

## Building a ClusterTemplate: Step by Step

Follow these steps to create a custom `ClusterTemplate`.

### 1. Obtain or create a Helm chart

Most users start from an existing template. Mirantis maintains a set of baseline `ClusterTemplates` in the [k0rdent GitHub repository](https://github.com/k0rdent/kcm/tree/main/templates/cluster). You can download these as tarballs from an OCI registry or clone them directly from GitHub. Alternatively, you can create your own chart with `helm create`.

### 2. Inspect the chart

Unpack the chart and look through the `templates/` directory. Each file maps to a CAPI object. Look at how values are referenced, usually with syntax like `.Values.controlPlaneNumber`. This tells you which parameters you can customize in `values.yaml`.

### 3. Modify configuration

Edit `values.yaml` to set the cluster size, networking ranges, AMIs, or k0s configuration. If you are creating a custom template, update `Chart.yaml` with your own name and version to distinguish it from the default. You may also extend `values.schema.json` to validate new parameters.

For example, to adjust Calico settings you might add:

```yaml
k0s:
  version: v1.32.6+k0s.0
  cpArgs:
    - "--enable-worker"
    - "--enable-calico"
  workerArgs:
    - "--labels=network=calico"
```

### 4. Package and upload

Once modified, package the chart:

```bash
helm package ./my-custom-template
```

Then push it to your OCI registry:

```bash
helm push my-custom-template-0.1.0.tgz oci://registry.example.com/templates
```

## Connecting the Chart to {{{ docsVersionInfo.k0rdentName }}}

{{{ docsVersionInfo.k0rdentName }}} does not fetch charts directly. Instead, it relies on FluxCD Source objects. You must define a `HelmRepository`, `GitRepository`, or `Bucket` that points to your chart location, and you must label it so that {{{ docsVersionInfo.k0rdentName }}} will recognize it.

For example:

```yaml
apiVersion: source.toolkit.fluxcd.io/v1
kind: HelmRepository
metadata:
  name: custom-repo
  namespace: kcm-system
  labels:
    k0rdent.mirantis.com/managed: "true"
spec:
  url: oci://registry.example.com/templates
  type: oci
  interval: 10m
  secretRef:
    name: my-repo-secret
```

## Creating the ClusterTemplate Resource

With the source in place, you can now define a `ClusterTemplate` CR that references your Helm chart:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ClusterTemplate
metadata:
  name: custom-aws-standalone
spec:
  helm:
    chartSpec:
      chart: my-custom-template
      version: 0.1.0
      interval: 10m
      sourceRef:
        kind: HelmRepository
        name: custom-repo
```

At this point, the {{{ docsVersionInfo.k0rdentName }}} controller validates the chart, reads the default values, and checks any annotations in `Chart.yaml` that declare required providers. For example, an AWS template might require `infrastructure-aws`, `control-plane-k0sproject-k0smotron`, and `bootstrap-k0sproject-k0smotron`. The template will only be marked "ready" if those providers are present.

## Deploying with a ClusterTemplate

Creating a `ClusterTemplate` does not deploy a cluster. Actual clusters are instantiated through **ClusterDeployment** objects, which reference `ClusterTemplates` and may override their default values. For example:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ClusterDeployment
metadata:
  name: my-cluster
  namespace: kcm-system
spec:
  template: custom-aws-standalone
  credential: aws-cluster-identity-cred
  config:
    clusterLabels: {}
    region: us-west-2
    controlPlane:
      instanceType: t3.small
      rootVolumeSize: 32
    worker:
      instanceType: t3.small
      rootVolumeSize: 32
```

When this object is applied, Flux installs the chart, CAPI providers reconcile their objects, and controllers like k0smotron configure k0s. Eventually, the `ClusterDeployment` is marked ready.

## Customizing Templates

Customization is usually as simple as editing `values.yaml`. The key is to understand which variables are exposed. You can determine this by inspecting the `templates/` directory and seeing where `.Values` are used. For example, if a manifest contains:

```yaml
metadata:
  name: {{ .Values.clusterName }}
```

Then you know that adding `clusterName: "my-new-cluster"` to your values file will set the name.

Because Helm supports hierarchies and conditionals, values files can become quite expressive. Over time, organizations often create their own libraries of values files tailored for different environments — dev, staging, production — while reusing the same underlying templates.

## Troubleshooting and Validation

The most common issues when building `ClusterTemplates` involve:

- **Missing providers:** If the template references providers not installed in your management cluster, it will fail validation.  
- **Schema violations:** If you supply a value of the wrong type, Helm will reject it if a schema is defined.  
- **Flux sync errors:** If Flux cannot reach your repository or chart, the template will not resolve.  

Debugging usually involves checking Flux logs (`kubectl logs -n flux-system deployment/helm-controller`), verifying that sources are labeled correctly, and ensuring that provider CRDs are installed.

## Next Steps

Building a `ClusterTemplate` is often the first step toward customizing {{{ docsVersionInfo.k0rdentName }}} for your environment. Once you understand how charts, values, and templates work together, you can extend the same model to **ServiceTemplates** for application add-ons and **ProviderTemplates** for new infrastructure backends.  

By embracing templating as the core abstraction, {{{ docsVersionInfo.k0rdentName }}} gives you a powerful system: clusters, services, and providers all managed through the same consistent pattern, with strong validation, automation, and reuse built in.
