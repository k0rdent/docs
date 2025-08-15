# AWS template parameters

## AWS AMI

For AWS, by default {{{ docsVersionInfo.k0rdentName }}} looks up the AMI ID automatically, using the latest Amazon Linux 2 image.

You can override lookup parameters to search your desired image automatically or you can
use a specific AMI ID directly.
If both the AMI ID and lookup parameters are defined, the AMI ID will have higher precedence.

### Image lookup

To configure automatic AMI lookup, {{{ docsVersionInfo.k0rdentName }}} uses three parameters:

* `.imageLookup.format` - Used directly as a value for the `name` filter
(see the [describe-images filters](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-images.html#describe-images)).
This field supports substitutions for `{{.BaseOS}}` and `{{.K8sVersion}}` with the base OS
and kubernetes version, respectively.

* `.imageLookup.org` - The AWS org ID that will be used as value for the `owner-id`
filter.

* `.imageLookup.baseOS` - The string to be used as a value for the `{{.BaseOS}}` substitution in
the `.imageLookup.format` string.

### AMI ID

The AMI ID can be directly used in the `.amiID` parameter.

#### CAPA prebuilt AMIs

Use `clusterawsadm` to get available AMIs to create a `ClusterDeployment`:

```bash
clusterawsadm ami list
```

For details, see [Pre-built Kubernetes AMIs](https://cluster-api-aws.sigs.k8s.io/topics/images/built-amis.html).

## SSH access to cluster nodes

To access nodes using SSH you'll need to do two things:

* Add an SSH key added in the region where you want to deploy the cluster
* Enable Bastion host is enabled

### SSH keys

Only one SSH key is supported and it should be added in AWS prior to creating
the `ClusterDeployment` object. The name of the key should then be placed under the `.spec.config.sshKeyName`.

The same SSH key will be used for all machines and a bastion host, or jump box. The bastion host is used as a single entry point that provides access to the rest of the cluster, enabling you to more tightly control access.

To enable the bastion, set the `.spec.config.bastion.enabled` option in the
`ClusterDeployment` object to `true`.

You can get a full list of the bastion configuration options in the [CAPA docs](https://cluster-api-aws.sigs.k8s.io/crd/#infrastructure.cluster.x-k8s.io/v1beta2.Bastion).

The resulting `ClusterDeployment` might look something like this:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ClusterDeployment
metadata:
  name: cluster-1
spec:
  template: aws-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsStandaloneCpCluster }}}
  credential: aws-cred
  config:
    clusterLabels: {}
    sshKeyName: foobar
    bastion:
      enabled: true
...
```

## Configuring some of k0s, k0smotron parameters

* `k0s.arch` (string): Defines K0s Arch in its download URL. Available if [global.k0sURL](../../appendix/appendix-extend-mgmt.md#configuring-a-global-k0s-url)
   is set. Possible values: `"amd64"` (default), `"arm64"`, `"arm"`.
* `k0s.cpArgs` <sup>only standalone</sup> (array of strings): A list of extra arguments to be passed to k0s controller.
   See: <https://docs.k0sproject.io/stable/cli/k0s_controller>.
* `k0s.workerArgs` (array of strings): A list of extra arguments for configuring the k0s worker node. See: <https://docs.k0sproject.io/stable/cli/k0s_worker>.
* `k0smotron.controllerPlaneFlags` <sup>only hosted</sup> (array of strings): The `controllerPlaneFlags` parameter enables you to configure additional flags for the k0s control plane
   and to override existing flags. The default flags are kept unless they are explicitly overriden. Flags with arguments must be specified as a single
   string, such as `--some-flag=argument`.

## EKS templates

> WARNING:
> When deploying an EKS cluster please note that
> [additional steps](../../troubleshooting/admin-troubleshooting-aws-vpcs.md) may be needed for proper VPC removal.

> WARNING:
> You may encounter an issue where EKS machines are not created due to the `ControlPlaneIsStable` preflight check
> failure during EKS cluster deployment. Please follow this
> [instruction](../../troubleshooting/known-issues-eks.md#eks-machines-are-not-created-controlplaneisstable-preflight-check-failed)
> to apply the workaround.

EKS templates use parameters similar to AWS and the resulting EKS
`ClusterDeployment` looks something like this:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ClusterDeployment
metadata:
  name: cluster-1
spec:
  template: aws-eks-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsEksCluster }}}
  credential: aws-cred
  config:
    clusterLabels: {}
    sshKeyName: foobar
    region: ${AWS_REGION}
    workersNumber: 1
...
```

## Non-root volumes

To configure options for non-root storage volumes, set the corresponding
fields in the `ClusterDeployment` responsible for these settings, which depend on the template in use:

| Template | Section(s) |
| --- | --- |
| `aws-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsStandaloneCpCluster }}}` | `.spec.controlPlane.nonRootVolumes`,`.spec.worker.nonRootVolumes` |
| `aws-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsHostedCpCluster }}}` | `.spec.nonRootVolumes` |
| `aws-eks-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsEksCluster }}}` | `.spec.worker.nonRootVolumes` |

The `nonRootVolumes` field is **a list** of [Volumes](https://cluster-api-aws.sigs.k8s.io/crd/#infrastructure.cluster.x-k8s.io/v1beta2.Volume).

## Setting the `managementClusterName` parameter for Hosted Control Plane clusters

The `managementClusterName` parameter is **required** for hosted control plane clusters.
It should match the `<cluster-id>` from the `kubernetes.io/cluster/<cluster-id> = owned` tag on existing AWS network
resources:

### Management Cluster Deployed on EKS

* If deployed using k0rdent (`aws-eks` template), the EKS cluster name defaults to:
  `<namespace>_<clusterdeploymentname>-cp`, or to the value of `eksClusterName` if explicitly set.

* If deployed separately (using `eksctl` or manually via the AWS console), the `<cluster-id>` is typically the
**EKS cluster name**.

### Management Cluster is EC2-Based (Self-Managed)

* If deployed using k0rdent (`aws-standalone-cp` template), use the **name of the ClusterDeployment** object.

* If created with Cluster API Provider AWS, use the value of `spec.clusterName` from the Cluster object.
