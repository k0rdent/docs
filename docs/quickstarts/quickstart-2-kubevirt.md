# QuickStart 2 - KubeVirt

> NOTE:
> The KubeVirt provider is available starting from {{{ docsVersionInfo.k0rdentName }}} 1.7.0. See
> [Enable KubeVirt Provider](../admin/upgrade/upgrade-to-1-7-0.md#enable-kubevirt-provider) for
> instructions on how to enable the KubeVirt provider on an existing management cluster after upgrading to 1.7.0.

{{{ docsVersionInfo.k0rdentName }}} supports using KubeVirt to create and manage clusters backed
by [KubeVirt](https://kubevirt.io/) virtual machines (VMs). This QuickStart guides you through the process of creating
a cluster using KubeVirt VMs as the target machines.

If you haven't yet created a management node and installed k0rdent, go back to [QuickStart 1 - Management node and cluster](quickstart-1-mgmt-node-and-cluster.md).

Note that if you have already done one of the other quickstarts, such as our AWS QuickStart
([QuickStart 2 - AWS target environment](quickstart-2-aws.md)) or ([QuickStart 2 - Azure target environment](quickstart-2-azure.md)), you can use
the same management cluster, continuing here with steps to add the ability to manage KubeVirt clusters. The k0rdent
management cluster can accommodate multiple provider and credential setups, enabling management of multiple
infrastructures. A big benefit of k0rdent is that it provides a single point of control and visibility across
multiple clusters on multiple clouds and infrastructures.

## Prerequisites

You must have a KubeVirt Infrastructure Cluster already set up and running. This cluster hosts the KubeVirt VMs that
form the target cluster. Follow the instructions in [KubeVirt Infrastructure Cluster Preparation](../appendix/kubevirt-infra.md)
to prepare the KubeVirt Infrastructure Cluster.

## Create a Secret object containing the KubeVirt Infrastructure Cluster kubeconfig

Create a `Secret` object to store the KubeVirt Infrastructure Cluster kubeconfig under the key `kubeconfig`.
The secret must be created in the same namespace where the cluster is going to be deployed. Start by setting
the following environment variables.

```bash
# Setup Environment
SECRET_NAME=kubevirt-kubeconfig
CLUSTER_NAMESPACE=kcm-system
CREDENTIAL_NAME=kubevirt-cred
RESOURCE_TEMPLATE_NAME=kubevirt-kubeconfig-resource-template
CLUSTER_DEPLOYMENT_NAME=my-kubevirt-clusterdeployment1
KUBECONFIG_PATH=/path/to/kubevirt-infra-cluster.kubeconfig
KUBEVIRT_INFRA_CLUSTER_KUBECONFIG_B64=$(cat $KUBECONFIG_PATH | base64 -w 0)
```

Now create the `kubevirt-kubeconfig-secret.yaml` file:

```bash
cat > kubevirt-kubeconfig-secret.yaml << EOF
apiVersion: v1
data:
  kubeconfig: $KUBEVIRT_INFRA_CLUSTER_KUBECONFIG_B64
kind: Secret
metadata:
  name: $SECRET_NAME
  namespace: $CLUSTER_NAMESPACE
  labels:
    k0rdent.mirantis.com/component: "kcm"
type: Opaque
EOF
```

Apply the YAML to the {{{ docsVersionInfo.k0rdentName }}} management cluster:
```bash
kubectl apply -f kubevirt-kubeconfig-secret.yaml
```
```console { .no-copy }
secret/kubevirt-kubeconfig created
```

## Create the KCM Credential Object

Create a YAML file with the specification of our credential and save it as `kubevirt-cred.yaml`.

Note that `.spec.identityRef.name` must match `.metadata.name` of the `Secret` object created in the previous step.

```bash
cat > kubevirt-cred.yaml << EOF
apiVersion: k0rdent.mirantis.com/v1beta1
kind: Credential
metadata:
  name: $CREDENTIAL_NAME
  namespace: $CLUSTER_NAMESPACE
spec:
  identityRef:
    apiVersion: v1
    kind: Secret
    name: $SECRET_NAME
    namespace: $CLUSTER_NAMESPACE
EOF
```

Apply the YAML to your cluster:
```bash
kubectl apply -f kubevirt-cred.yaml
```
```console { .no-copy }
credential.k0rdent.mirantis.com/kubevirt-cred created
```

## Create the Cluster Identity resource template ConfigMap

Now create the {{{ docsVersionInfo.k0rdentName }}} `ClusterIdentity` resource template `ConfigMap`. As in prior
steps, create a YAML file called `kubevirt-kubeconfig-resource-template.yaml`:

> NOTE:
> The `ConfigMap` name, in this case, needs to be exactly `$SECRET_NAME-resource-template` (in this case
> `kubevirt-kubeconfig-resource-template`). See
> [naming the template configmap](../appendix/appendix-providers.md#naming-the-template-configmap) for details.

```bash
cat > kubevirt-kubeconfig-resource-template.yaml << EOF
apiVersion: v1
kind: ConfigMap
metadata:
  name: $RESOURCE_TEMPLATE_NAME
  namespace: $CLUSTER_NAMESPACE
  labels:
    k0rdent.mirantis.com/component: "kcm"
  annotations:
    projectsveltos.io/template: "true"
EOF
```
Note that the `ConfigMap` only contains metadata and no data fields. This is expected, as we do not need to template
any objects inside child clusters, but we can use this object in the future if the need arises.
Apply this YAML to your management cluster:

```bash
kubectl apply -f kubevirt-kubeconfig-resource-template.yaml
```

## List available cluster templates

To create a KubeVirt cluster, begin by listing the available `ClusterTemplate` objects provided with {{{ docsVersionInfo.k0rdentName}}}:

```bash
kubectl get clustertemplate -n $CLUSTER_NAMESPACE
```

You'll see output similar to the following. Make note of the name of the KubeVirt Cluster template in its current
version (in the example below, that's `kubevirt-cluster-{{{ extra.docsVersionInfo.providerVersions.dashVersions.kubevirtStandaloneCpCluster }}}`):

```console { .no-copy }
NAMESPACE    NAME                            VALID
kcm-system   adopted-cluster-{{{ extra.docsVersionInfo.providerVersions.dashVersions.adoptedCluster }}}           true
kcm-system   aws-eks-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsEksCluster }}}                   true
kcm-system   aws-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsHostedCpCluster }}}            true
kcm-system   aws-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsStandaloneCpCluster }}}        true
kcm-system   azure-aks-{{{ extra.docsVersionInfo.providerVersions.dashVersions.azureAksCluster }}}                 true
kcm-system   azure-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.azureHostedCpCluster }}}          true
kcm-system   azure-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.azureStandaloneCpCluster }}}      true
kcm-system   docker-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.dockerHostedCpCluster }}}          true
kcm-system   gcp-gke-{{{ extra.docsVersionInfo.providerVersions.dashVersions.gcpGkeCluster }}}                   true
kcm-system   gcp-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.gcpHostedCpCluster }}}            true
kcm-system   gcp-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.gcpStandaloneCpCluster }}}        true
kcm-system   kubevirt-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.kubevirtHostedCpCluster }}}        true
kcm-system   kubevirt-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.kubevirtStandaloneCpCluster }}}    true
kcm-system   openstack-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.openstackStandaloneCpCluster }}}      true
kcm-system   openstack-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.openstackStandaloneCpCluster }}}  true
kcm-system   remote-cluster-{{{ extra.docsVersionInfo.providerVersions.dashVersions.remoteCluster }}}           true
kcm-system   vsphere-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.vsphereHostedCpCluster }}}        true
kcm-system   vsphere-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.vsphereStandaloneCpCluster }}}    true
```

## Create your ClusterDeployment

To deploy a cluster, create a YAML file called `my-kubevirt-clusterdeployment1.yaml`. You will use this to create a
`ClusterDeployment` object representing the deployed cluster.

> NOTE:
> The `spec.config.cluster.controlPlaneServiceTemplate.spec.type` field should be configured correctly. If you use
> the `LoadBalancer` service type, ensure that an appropriate Service LoadBalancer solution (for example, `MetalLB`
> or a cloud provider load balancer) is installed on the KubeVirt Infrastructure Cluster.
> This field is optional. By default, control plane nodes use a Service of type `ClusterIP`, which makes the workload
> cluster accessible only within the same cluster. In most cases, you will want to expose the workload cluster API
> server outside the KubeVirt Infrastructure Cluster, so using LoadBalancer is recommended.

```bash
cat > my-kubevirt-clusterdeployment1.yaml << EOF
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ClusterDeployment
metadata:
  name: $CLUSTER_DEPLOYMENT_NAME
  namespace: $CLUSTER_NAMESPACE
spec:
  template: kubevirt-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.kubevirtStandaloneCpCluster }}} # name of the clustertemplate
  credential: $CREDENTIAL_NAME
  propagateCredentials: false
  config:
    clusterLabels: {}
    clusterAnnotations: {}
    controlPlaneNumber: 1
    workersNumber: 1
    cluster:
      controlPlaneServiceTemplate:
        spec:
          type: LoadBalancer
    controlPlane:
      dnsConfig:
        nameservers:
        - 8.8.8.8
      cpu:
        model: host-passthrough
    worker:
      dnsConfig:
        nameservers:
        - 8.8.8.8
      cpu:
        model: host-passthrough
EOF
```

> WARNING:
> The example above creates a very basic cluster with minimal resources (1 control plane node and 1 worker node).
> This configuration is suitable for testing and learning purposes only. For production deployments, you should
> customize the cluster configuration according to your requirements, including resource allocation and networking.

## Apply the ClusterDeployment to deploy the KubeVirt cluster

Apply the `ClusterDeployment` YAML (`my-kubevirt-clusterdeployment1.yaml`) to instruct {{{ docsVersionInfo.k0rdentName }}} to deploy the cluster:

```bash
kubectl apply -f my-kubevirt-clusterdeployment1.yaml
```

Kubernetes should confirm the creation:

```console { .no-copy }
clusterdeployment.k0rdent.mirantis.com/my-kubevirt-clusterdeployment1 created
```

There will be a delay as the cluster finishes provisioning. Follow the provisioning process with the following command:

```bash
kubectl -n kcm-system get clusterdeployment.k0rdent.mirantis.com my-kubevirt-clusterdeployment1 --watch
```

To verify that the cluster has been successfully provisioned, run:

```bash
kubectl -n kcm-system get clusterdeployment.k0rdent.mirantis.com my-kubevirt-clusterdeployment1 -o=jsonpath='{.status.conditions[?(@.type=="Ready")].status}'
```

If the cluster was provisioned, the output of this command will be:

```console { .no-copy }
True
```

If there is any error, check the readiness condition in more details:

```bash
kubectl -n kcm-system get clusterdeployment.k0rdent.mirantis.com my-kubevirt-clusterdeployment1 -o=jsonpath='{.status.conditions[?(@.type=="Ready")]}' | jq
```

## Obtain the cluster's kubeconfig

Now you can retrieve the cluster's kubeconfig:

```bash
kubectl -n kcm-system get secret my-kubevirt-clusterdeployment1-kubeconfig -o jsonpath='{.data.value}' | base64 -d > my-kubevirt-clusterdeployment1.kubeconfig
```

And you can use the kubeconfig to see what's running on the cluster:

```bash
KUBECONFIG="my-kubevirt-clusterdeployment1.kubeconfig" kubectl get pods -A
```

## Tear down the child cluster

To tear down the child cluster, delete the `ClusterDeployment` from the management cluster:

```bash
kubectl delete ClusterDeployment my-kubevirt-clusterdeployment1 -n kcm-system
```
```console { .no-copy }
clusterdeployment.k0rdent.mirantis.com "my-kubevirt-clusterdeployment1" deleted
```

## Troubleshooting

For troubleshooting KubeVirt cluster deployment issues, refer to the [Troubleshooting KubeVirt Clusters](../troubleshooting/known-issues-kubevirt.md) guide.

## Next Steps

Now that you've finished the QuickStart, we have some suggestions for what to do next:

Check out the [Administrator Guide](../admin/index.md) ...

* For a more detailed view of {{{ docsVersionInfo.k0rdentName }}} setup for production
* For details about setting up {{{ docsVersionInfo.k0rdentName }}} to manage clusters on VMware and OpenStack
* For details about using {{{ docsVersionInfo.k0rdentName }}} with cloud Kubernetes distros such as AWS EKS and Azure AKS
