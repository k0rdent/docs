# GCP template parameters

## Common ClusterDeployment parameters

* `controlPlaneNumber` (number): The number of the control plane nodes (or pods for the hosted cluster). Not available for the GKE cluster template.
* `workersNumber` (number): The number of the worker nodes. For GKE clusters this parameter should be divisible by the number of zones in machines.nodeLocations. If nodeLocations is not specified, must be divisible by the number of zones in this region (default: 3)
* `clusterNetwork.apiServerPort` (number): The port the API Server should bind to. Not available for the GKE cluster template.
* `clusterNetwork.pods.cidrBlocks` (array): A list of CIDR blocks from which Pod networks are allocated.
* `clusterNetwork.services.cidrBlocks` (array): A list of CIDR blocks from which service VIPs are allocated.
* `clusterLabels` (object): Labels to apply to the Cluster object.
* `clusterAnnotations` (object): Annotations to apply to the Cluster object.

## GCP Cluster parameters

The following parameters are available for standalone and hosted cluster templates:

* `project` (string): The name of the project to deploy the cluster to.
* `region` (string): The GCP Region the cluster lives in.
* `network.name` (string): The name of an existing GCP network or a new network to be created by Cluster API Provider GCP.
* `network.mtu` (number): Maximum Transmission Unit in bytes.
* `additionalLabels` (object): Additional set of labels to add to all the GCP resources.

### GCP Machines parameters

The following parameters are available for `controlPlane` (for standalone cluster template) and `worker`
(for standalone and hosted cluster templates) machines (for example, `controlPlane.instanceType`):

* `instanceType` (string): The type of instance to create.
* `subnet` (string): A reference to the subnetwork to use for this instance.
* `providerID` (string): The unique identifier as specified by the cloud provider.
* `imageFamily` (string): The full reference to a valid image family to be used for this machine.
* `image` (string): The full reference to a valid image to be used for this machine. Takes precedence over imageFamily.
* `additionalLabels` (object): Additional set of labels to add to an instance.
* `publicIP` (boolean): Specifies whether the instance should get a public IP.
* `additionalNetworkTags` (array): A list of network tags that should be applied to the instance.
* `rootDeviceSize` (number): The size of the root volume in GB.
* `rootDeviceType` (string): The type of the root volume. One of: `pd-standard`,`pd-ssd`,`pd-balanced`,`hyperdisk-balanced`.
* `serviceAccount.email` (string): Email address of the service account.
* `serviceAccount.scopes` (array): The list of scopes to be made available for this service account.
* `ipForwarding` (string): Allows this instance to send and receive packets with non-matching destination or source IPs. One of: `Enabled`,`Disabled`.


### K0s Parameters

* `k0s.version` (string): K0s version.
* `k0s.api.extraArgs` (object): Map of key-values (strings) for any extra arguments to pass down to the Kubernetes API server process.

### K0smotron Parameters

Available for the hosted cluster template only.

* `k0smotron.service.type` (string): An ingress method for a service. One of: `ClusterIP`, `NodePort`, `LoadBalancer`. Defaults to: `LoadBalancer`.
* `k0smotron.service.apiPort` (number): The Kubernetes API port. If empty, K0smotron will pick it automatically.
* `k0smotron.service.konnectivityPort` (number): The Konnectivity port. If empty, K0smotron will pick it automatically.

### Extensions parameters

* `extensions.chartRepository` (string): Custom Helm repository.
* `extensions.imageRepository` (string): Custom images’ repository.

## GKE template parameters

### GKE Cluster Parameters

* `gkeClusterName` (string): The name of the GKE cluster. If unspecified, a default name is created based on the namespace and managed control plane name.
* `project` (string): The name of the GCP project where the cluster is deployed.
* `enableAutopilot` (boolean): Indicates whether to enable Autopilot for this GKE cluster.
* `releaseChannel` (string): The release channel of the GKE cluster.
* `controlPlaneVersion` (string): The control plane version of the GKE cluster. If unspecified, the default version supported by GKE is used.
* `masterAuthorizedNetworksConfig` (object): Configuration options for the master authorized networks feature. If unspecified, the feature is disabled.
* `region` (string): The GCP region where the cluster is deployed.
* `location` (string): The location where the GKE cluster is created. If unspecified, the cluster is regional; otherwise, specifying a location creates a zonal cluster.
* `network.name` (string): The GCP network name.
* `network.mtu` (number): Maximum Transmission Unit (MTU) in bytes.

### GKE Managed Machines Parameters

* `machines.nodePoolName` (string): The name of the GKE node pool. If unspecified, a default name is created based on the namespace and managed machine pool name.
* `machines.machineType` (string): The name of a Google Compute Engine machine type. Defaults to `e2-medium`.
* `machines.diskSizeGB` (number): The size of the disk attached to each node (in GB). The smallest allowed disk size is 10GB. If unspecified, the default disk size is 100GB.
* `machines.localSsdCount` (number,null): The number of local SSD disks attached to the node.
* `machines.scaling.enableAutoscaling` (boolean): Indicates if autoscaling is enabled for this node pool. Defaults to true.
* `machines.scaling.minCount` (number,null): The minimum number of nodes in the node pool.
* `machines.scaling.maxCount` (number,null): The maximum number of nodes in the node pool.
* `machines.scaling.locationPolicy` (string): Location policy used when scaling up a node pool.
* `machines.nodeLocations` (array): The list of zones where the node pool’s nodes are located.
* `machines.imageType` (string): The image type used for this node pool.
* `machines.instanceType` (string): The Compute Engine machine type.
* `machines.diskType` (string): The type of disk attached to each node.
* `machines.maxPodsPerNode` (number,null): The maximum number of pods allowed per node.
* `machines.kubernetesLabels` (object): Labels applied to the nodes of the node pool.
* `machines.kubernetesTaints` (array): Taints applied to the nodes of the node pool.
* `machines.additionalLabels` (object): Additional labels added to GCP resources managed by the provider.
* `machines.management.autoUpgrade` (boolean): Specifies if node auto-upgrade is enabled. Defaul
* `machines.management.autoRepair` (boolean): Specifies if node auto-repair is enabled.


The resulting GCP standalone `ClusterDeployment` might look something like this:

```yaml
apiVersion: k0rdent.mirantis.com/v1alpha1
kind: ClusterDeployment
metadata:
  name: cluster-1
spec:
  template: gcp-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.gcpStandaloneCpCluster }}}
  credential: gcp-cred
  config:
    clusterLabels:
      foo: bar
    project: dev
    region: us-east4
    network:
      name: default
    controlPlane:
      instanceType: n1-standard-2
      image: projects/ubuntu-os-cloud/global/images/ubuntu-2004-focal-v20250213
      publicIP: true
      rootDeviceSize: 100
      ipForwarding: Enabled
    controlPlaneNumber: 1
    worker:
      instanceType: n1-standard-2
      image: projects/ubuntu-os-cloud/global/images/ubuntu-2004-focal-v20250213
      publicIP: true
      rootDeviceSize: 50
      ipForwarding: Enabled
    workersNumber: 1
...
```

The resulting GCP hosted `ClusterDeployment` might look something like this:

```yaml
apiVersion: k0rdent.mirantis.com/v1alpha1
kind: ClusterDeployment
metadata:
  name: cluster-1
spec:
  template: gcp-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.gcpHostedCpCluster }}}
  credential: gcp-cred
  config:
    clusterAnnotations:
      foo: bar
    project: dev
    region: us-east4
    network:
      name: default
    controlPlaneNumber: 3
    worker:
      instanceType: n1-standard-2
      image: projects/ubuntu-os-cloud/global/images/ubuntu-2004-focal-v20250213
      publicIP: true
      rootDeviceSize: 50
      ipForwarding: Enabled
    workersNumber: 2
...
```

The resulting GCP GKE `ClusterDeployment` might look something like this:

```yaml
apiVersion: k0rdent.mirantis.com/v1alpha1
kind: ClusterDeployment
metadata:
  name: cluster-1
spec:
  template: gcp-gke-{{{ extra.docsVersionInfo.providerVersions.dashVersions.gcpGkeCluster }}}
  credential: gcp-cred
  propagateCredentials: false
  config:
    clusterLabels:
      env: dev
    gkeClusterName: "dev-cluster-1"
    workersNumber: 3 # Should be divisible by the number of zones in `machines.nodeLocations`. If `machines.nodeLocations` is not specified, must be divisible by the number of zones in this region (default: 3)
    project: dev
    region: us-east4
    network:
      name: default
    machines:
      diskSizeGB: 120
      scaling:
        enableAutoscaling: true
        minCount: 5
        maxCount: 25
      maxPodsPerNode: 250
...
```
