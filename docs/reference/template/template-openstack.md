# OpenStack Machine parameters

## ClusterDeployment Parameters

To deploy an OpenStack cluster, the following are the primary parameters in the `ClusterDeployment` resource:

| Parameter                         | Example                               | Description                                                 |
|-----------------------------------|---------------------------------------|-------------------------------------------------------------|
| `.spec.credential`                | `openstack-cluster-identity-cred`     | Reference to the `Credential` object.                       |
| `.spec.template`                  | `openstack-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.openstackStandaloneCpCluster }}}` | Reference to the `ClusterTemplate`. |
| `.spec.config.authURL`            | `https://keystone.yourorg.net/`       | Keystone authentication endpoint for OpenStack.             |
| `.spec.config.controlPlaneNumber` | `3`                                   | Number of control plane nodes.                              |
| `.spec.config.workersNumber`      | `2`                                   | Number of worker nodes.                                     |
| `.spec.config.clusterLabels`      | `k0rdent: demo`                       | Labels to apply to the cluster. Used by MultiClusterService.|
| `.spec.config.ccmRegional`         | `true`                                | Enables the OpenStack CCM OS_CCM_REGIONAL envvar feature and allows OpenStack CCM to define the region in nodes |

### SSH Configuration

To access deployed machines over ssh requires two things:

- `sshKeyName` - the reference name for an existing SSH key configured in OpenStack.
- `bastion` - bastion host being enabled and its flavor and image specified.

#### SSH keys

Specify the SSH public key using the `.spec.config.controlPlane.sshKeyName` and `.spec.config.worker.sshKeyName` parameters (for the standalone control plane)
or `spec.config.sshKeyName` parameter (for the hosted control plane).

#### Bastion

Specify `.spec.config.bastion.enabled` to enable it as well as provide `sshKeyName`, `flavor` and `image` in `.spec.config.bastion.spec`, similarly to workers and control plane.

Example `ClusterDeployment with enabled bastion can be found [below](#example-clusterdeployment).

### Machine Configuration

Configurations for control plane and worker nodes are specified separately under `.spec.config.controlPlane` and `.spec.config.worker`
for standalone control plane or under `spec.config` for hosted control plane.

| Parameter                      | Example               | Description                             |
|--------------------------------|-----------------------|-----------------------------------------|
| `flavor`                       | `m1.medium`           | OpenStack flavor for the instance.      |
| `image.filter.name`            | `ubuntu-22.04-x86_64` | Name of the image.                      |
| `sshKeyName`                   | `ramesses-pk`         | Reference name for an existing SSH key. |
| `securityGroups[].filter.name` | `default`             | Security group for the instance.        |

> NOTE:
> Make sure `.spec.credential` references the `Credential` object.
> The recommended minimum vCPU value for the control plane flavor is 2, while for the worker node flavor, it is 1. For detailed information, refer to the [machine-flavor CAPI docs](https://github.com/kubernetes-sigs/cluster-api-provider-openstack/blob/main/docs/book/src/clusteropenstack/configuration.md#machine-flavor).

### External Network Configuration

If your OpenStack cloud contains more than one network marked as external it is necessary to provide which one clusterapi should use when creating a cluster. You do this by providing `.spec.config.externlNetwork.filter.name` value with the name of your external network.

### Load Balancer Configuration

If your user doesn't have access to or your cloud doesn't utilize octavia load balancer it is possible to disable usage of it by specifying
`.spec.config.apiServerLoadBalancer.enabled` as `false` (for standalone control plane only).

> WARNING: Disabling loadbalancer blocks usage of `LoadBalancer` type services in cluster until one is manually installed.

### Configuring some of k0s parameters

- `k0s.arch` (string): Defines K0s Arch in its download URL. Available if [global.k0sURL](../../appendix/appendix-extend-mgmt.md#configuring-a-global-k0s-url)
   is set. Possible values: `"amd64"` (default), `"arm64"`, `"arm"`.
- `k0s.cpArgs` (array of strings): A list of extra arguments to be passed to k0s controller. For standalone control plane only.
   See: <https://docs.k0sproject.io/stable/cli/k0s_controller>.
- `k0s.workerArgs` (array of strings): A list of extra arguments for configuring the k0s worker node. See: <https://docs.k0sproject.io/stable/cli/k0s_worker>.

### Hosted ClusterDeployment parameters

#### Network configuration

The following parameters under `spec.config` are specific to the hosted cluster deployment:

* `network.filter` (object): Specifies a query to select an OpenStack network. The value of [NetworkFilter](https://cluster-api-openstack.sigs.k8s.io/api/v1beta1/api#infrastructure.cluster.x-k8s.io/v1beta1.NetworkFilter) type. Required.

    Example:

    ```yaml
      network:
        filter:
          name: my-network-name
    ```

* `subnets[].filter` (array): Specifies a query to select an OpenStack subnet. The value of [SubnetFilter](https://cluster-api-openstack.sigs.k8s.io/api/v1beta1/api#infrastructure.cluster.x-k8s.io/v1beta1.SubnetFilter) type. Required.

    Example:

    ```yaml
      subnets:
      - filter:
          name: my-subnet-name
    ```

* `router.filter` (object): Specifies a query to select an OpenStack router. The value of [RouterFilter](https://cluster-api-openstack.sigs.k8s.io/api/v1beta1/api#infrastructure.cluster.x-k8s.io/v1beta1.RouterFilter) type. Required.

    Example:

    ```yaml
      router:
        filter:
          name: my-router-name
    ```

* `ports[].network.filter` (object): Specifies a query to select an OpenStack network. The value of [NetworkFilter](https://cluster-api-openstack.sigs.k8s.io/api/v1beta1/api#infrastructure.cluster.x-k8s.io/v1beta1.NetworkFilter) type. Required.

    Example:

    ```yaml
      ports:
      - network:
          filter:
            name: my-network-name
    ```

* `managedSecurityGroups` (object): Defines the desired state of security groups and rules for the cluster. When not
  defined, security groups will not be created. The value of [ManagedSecurityGroups](https://cluster-api-openstack.sigs.k8s.io/api/v1beta1/api#infrastructure.cluster.x-k8s.io/v1beta1.ManagedSecurityGroups) type.

    Example:
    ```yaml
      managedSecurityGroups:
        allowAllInClusterTraffic: false
    ```

#### K0smotron Parameters

Available for the hosted cluster template only.

* `k0smotron.service.type` (string): An ingress method for a service. One of: `ClusterIP`, `NodePort`, `LoadBalancer`. Defaults to: `LoadBalancer`.
* `k0smotron.service.apiPort` (number): The Kubernetes API port. If empty, K0smotron will pick it automatically.
* `k0smotron.service.konnectivityPort` (number): The Konnectivity port. If empty, K0smotron will pick it automatically.
* `k0smotron.controllerPlaneFlags` (array of strings): The `controllerPlaneFlags` parameter enables you to configure additional flags for the k0s control plane
  and to override existing flags. The default flags are kept unless they are explicitly overriden. Flags with arguments must be specified as a single
  string, such as `--some-flag=argument`.

### Example ClusterDeployment

The standalone `ClusterDeployment` may look like this:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ClusterDeployment
metadata:
  name: my-openstack-cluster-deployment
  namespace: kcm-system
spec:
  template: openstack-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.openstackStandaloneCpCluster }}}
  credential: openstack-cluster-identity-cred
  config:
    clusterLabels:
      k0rdent: demo
    controlPlaneNumber: 1
    workersNumber: 1
    bastion:
      enabled: true
      spec:
        sshKeyName: my-public-key
        flavor: m1.small
        image:
          filter:
            name: ubuntu-22.04-x86_64
    controlPlane:
      sshKeyName: bastion-public-key
      flavor: m1.medium
      image:
        filter:
          name: ubuntu-22.04-x86_64
    worker:
      sshKeyName: bastion-public-key
      flavor: m1.medium
      image:
        filter:
          name: ubuntu-22.04-x86_64
    externalNetwork:
      filter:
        name: "public"
    authURL: https://my-keystone-openstack-url.com
    identityRef:
      name: openstack-cloud-config
      cloudName: openstack
      region: RegionOne
```

The hosted `ClusterDeployment` may look like this:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ClusterDeployment
metadata:
  name: my-openstack-hosted-deployment
  namespace: kcm-system
spec:
  template: openstack-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.openstackHostedCpCluster }}}
  credential: openstack-cluster-identity-cred
  config:
    clusterLabels:
      k0rdent: demo
    workersNumber: 3
    bastion:
      enabled: true
      spec:
        sshKeyName: my-ssh-key
        flavor: m1.medium
        image:
          filter:
            name: ubuntu-22.04-x86_64
    sshKeyName: my-ssh-key
    flavor: m1.medium
    image:
      filter:
        name: ubuntu-22.04-x86_64
    externalNetwork:
      filter:
        name: "public"
    identityRef:
      name: "openstack-cloud-config"
      cloudName: "openstack"
      region: RegionOne

    managedSecurityGroups:
      allowAllInClusterTraffic: false
    network:
      filter:
        name: my-network-name
    router:
      filter:
        name: my-router-name
    subnets:
    - filter:
        name: my-subnet-name
    ports:
    - network:
        filter:
          name: my-network-name
    securityGroups:
    - filter:
        name: my-security-group-name
```
