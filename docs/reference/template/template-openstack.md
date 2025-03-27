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

### SSH Configuration

`sshPublicKey` is the reference name for an existing SSH key configured in OpenStack.

- **ClusterDeployment**: Specify the SSH public key using the `.spec.config.controlPlane.sshPublicKey` and `.spec.config.worker.sshPublicKey` parameters (for the standlone control plane).

### Machine Configuration

Configurations for control plane and worker nodes are specified separately under `.spec.config.controlPlane` and `.spec.config.worker`:

| Parameter                  | Example                | Description                        |
|----------------------------|------------------------|------------------------------------|
| `flavor`                   | `m1.medium`           | OpenStack flavor for the instance.|
| `image.filter.name`        | `ubuntu-22.04-x86_64` | Name of the image.                |
| `sshPublicKey`             | `ramesses-pk`         | Reference name for an existing SSH key.|
| `securityGroups.filter.name`| `default`             | Security group for the instance.  |

> NOTE:
> Make sure `.spec.credential` references the `Credential` object.
> The recommended minimum vCPU value for the control plane flavor is 2, while for the worker node flavor, it is 1. For detailed information, refer to the [machine-flavor CAPI docs](https://github.com/kubernetes-sigs/cluster-api-provider-openstack/blob/main/docs/book/src/clusteropenstack/configuration.md#machine-flavor).

### Example ClusterDeployment

```yaml
apiVersion: k0rdent.mirantis.com/v1alpha1
kind: ClusterDeployment
metadata:
  name: my-openstack-cluster-deployment
  namespace: kcm-system
spec:
  template: openstack-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.openstackStandaloneCpCluster }}}
  credential: openstack-cluster-identity-cred
  config:
    clusterLabels: {}
    clusterLabels:
      k0rdent: demo
    controlPlaneNumber: 1
    workersNumber: 1
    controlPlane:
      sshPublicKey: my-public-key
      flavor: m1.medium
      image:
        filter:
          name: ubuntu-22.04-x86_64
    worker:
      sshPublicKey: my-public-key
      flavor: m1.medium
      image:
        filter:
          name: ubuntu-22.04-x86_64
    authURL: https://my-keystone-openstack-url.com
    identityRef:
      name: openstack-cloud-config
      cloudName: openstack
      region: RegionOne
```