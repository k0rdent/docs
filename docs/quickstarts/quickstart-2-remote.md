# QuickStart 2 - Deploying a child cluster on existing infrastructure

In this QuickStart unit, we will gather essential information and perform the preparatory steps needed to enable k0rdent (running on your management node) to deploy a k0s child cluster on existing infrastructure. The remote servers will serve as worker nodes in the cluster, while the control plane components will reside within the management cluster and be managed by k0smotron.

The remote machines that will be part of the cluster must meet the following prerequisites:
1.	Linux-based operating system on the remote hosts.
2.	SSH access enabled for the root user.
3.	Internet access for the remote hosts.
4.	The remote hosts should meet the [k0s system requirements](https://docs.k0sproject.io/stable/system-requirements/).
5.	Ensure connectivity between the management cluster and the remote hosts networks.

If you haven't yet created a management node and installed k0rdent, go back to [QuickStart 1 - Management node and cluster](quickstart-1-mgmt-node-and-cluster.md).

Note that if you have already done our AWS QuickStart ([QuickStart 2 - AWS target environment](quickstart-2-aws.md)) or ([QuickStart 2 - Azure target environment](quickstart-2-azure.md)) you can use the same management cluster, continuing here with steps to add the ability to manage remote clusters. The k0rdent management cluster can accommodate multiple provider and credential setups, enabling management of multiple infrastructures. A big benefit of k0rdent is that it provides a single point of control and visibility across multiple clusters on multiple clouds and infrastructures.

## Create a Secret object containing private SSH key to access remote machines

Create a `Secret` object to securely store the private SSH key, under the key `value`, for accessing all remote machines that will be part of the cluster. Save this configuration in a YAML file named `remote-ssh-key-secret.yaml`. Ensure you replace the placeholder `PRIVATE_SSH_KEY_B64` with your base64-encoded private SSH key:

```yaml
apiVersion: v1
data:
  value: PRIVATE_SSH_KEY_B64 # Base64-encoded private SSH key
kind: Secret
metadata:
  name: remote-ssh-key
  namespace: kcm-system
  labels:
    k0rdent.mirantis.com/component: "kcm"
type: Opaque
```

Apply the YAML to the k0rdent management cluster using the following command:

```shell
kubectl apply -f remote-ssh-key-secret.yaml
```

## Create the KCM Credential Object

Create a YAML with the specification of our credential and save it as `remote-cred.yaml`.

Note that `.spec.name` must match `.metadata.name` of the `Secret` object created in the previous step.

```yaml
apiVersion: k0rdent.mirantis.com/v1alpha1
kind: Credential
metadata:
  name: remote-cred
  namespace: kcm-system
spec:
  identityRef:
    apiVersion: v1
    kind: Secret
    name: remote-ssh-key
    namespace: kcm-system
```

Apply the YAML to your cluster:

```shell
kubectl apply -f remote-cred.yaml
```

You should see output resembling this:

```console
credential.k0rdent.mirantis.com/remote-cred created
```

## Create the {{{ docsVersionInfo.k0rdentName }}} Cluster Identity resource template ConfigMap

Now we create the {{{ docsVersionInfo.k0rdentName }}} Cluster Identity resource template `ConfigMap`. As in prior steps, create a YAML file called `remote-ssh-key-resource-template.yaml`:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: remote-ssh-key-resource-template
  namespace: kcm-system
  labels:
    k0rdent.mirantis.com/component: "kcm"
  annotations:
    projectsveltos.io/template: "true"
```

Note that `ConfigMap` is empty, this is expected, we don't need to template any object inside child cluster(s), but we can use that object in the future if need arises.

Now apply this YAML to your management cluster:

```shell
kubectl apply -f remote-ssh-key-resource-template.yaml -n kcm-system
```

## List available cluster templates

To create a remote cluster, begin by listing the available ClusterTemplates provided with k0rdent:

```shell
kubectl get clustertemplate -n kcm-system
```

You'll see output resembling what's below. Grab the name of the Remote Cluster template in its present version (in the example below, that's `remote-cluster-{{{ extra.docsVersionInfo.providerVersions.dashVersions.azureStandaloneCpCluster }}}`):

```console
NAMESPACE    NAME                            VALID
kcm-system   adopted-cluster-{{{ extra.docsVersionInfo.k0rdentVersion }}}           true
kcm-system   aws-eks-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsEksCluster }}}                   true
kcm-system   aws-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsHostedCpCluster }}}             true
kcm-system   aws-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsStandaloneCpCluster }}}         true
kcm-system   azure-aks-{{{ extra.docsVersionInfo.providerVersions.dashVersions.azureAksCluster }}}                 true
kcm-system   azure-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.azureHostedCpCluster }}}           true
kcm-system   azure-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.azureStandaloneCpCluster }}}       true
kcm-system   openstack-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.openstackStandaloneCpCluster }}}   true
kcm-system   remote-cluster-{{{ extra.docsVersionInfo.providerVersions.dashVersions.remoteCluster }}}     true
kcm-system   vsphere-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.vsphereHostedCpCluster }}}         true
kcm-system   vsphere-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.vsphereStandaloneCpCluster }}}     true
```

## Create your ClusterDeployment

Now, to deploy a cluster, create a YAML file called `my-remote-clusterdeployment1.yaml`. We'll use this to create a ClusterDeployment object in k0rdent, representing the deployed cluster. The `ClusterDeployment` identifies for k0rdent the `ClusterTemplate` you want to use for cluster creation, the identity credential object you want to create it under, plus the machines' IP addresses (represented by the placeholder `MACHINE_0_ADDRESS` and `MACHINE_1_ADDRESS` below), SSH port of the remote machines and the user to use when connecting to remote machines (root):

> NOTE:
> The user must have root permissions. 
> The service type should be correctly configured. If using the `LoadBalancer` service type, ensure the appropriate cloud provider is installed on the management cluster.
> For other service types (such as `ClusterIP` or `NodePort`), verify that the management cluster network is accessible from the host machines to allow virtual machines to connect to the API server.

```yaml
apiVersion: k0rdent.mirantis.com/v1alpha1
kind: ClusterDeployment
metadata:
  name: my-remote-clusterdeployment1
  namespace: kcm-system
spec:
  template: remote-cluster-{{{ extra.docsVersionInfo.providerVersions.dashVersions.remoteCluster }}} # name of the clustertemplate
  credential: remote-cred
  propagateCredentials: false
  config:
    k0smotron:
      service:
        type: LoadBalancer
    machines:
    - address: MACHINE_0_ADDRESS
      user: root # The user must have root permissions 
      port: 22
    - address: MACHINE_1_ADDRESS
      user: root # The user must have root permissions 
      port: 22
```

## Apply the ClusterDeployment to deploy the cluster

Finally, we'll apply the ClusterDeployment YAML (`my-remote-clusterdeployment1.yaml`) to instruct k0rdent to deploy the cluster:

```shell
kubectl apply -f my-remote-clusterdeployment1.yaml
```

Kubernetes should confirm this:

```console
clusterdeployment.k0rdent.mirantis.com/my-remote-clusterdeployment1 created
```

There will be a delay as the cluster finishes provisioning. Follow the provisioning process with the following command:

```shell
kubectl -n kcm-system get clusters.cluster.x-k8s.io my-remote-clusterdeployment1 --watch
```

To verify that the remote machines were successfuly provisioned, run:

```shell
kubectl -n kcm-system get remotemachines.infrastructure.cluster.x-k8s.io -l helm.toolkit.fluxcd.io/name=my-remote-clusterdeployment1 -o=jsonpath={.items[*].status}
```

If the machines were provisioned, the output of this command will be similar to:

```console
{"ready":true}{"ready":true}
```

If there is any error, the output will contain an error message.

## Obtain the cluster's kubeconfig

Now you can retrieve the cluster's kubeconfig:

```shell
kubectl -n kcm-system get secret my-remote-clusterdeployment1-kubeconfig -o jsonpath='{.data.value}' | base64 -d > my-remote-clusterdeployment1-kubeconfig.kubeconfig
```

And you can use the kubeconfig to see what's running on the cluster:

```shell
KUBECONFIG="my-remote-clusterdeployment1-kubeconfig.kubeconfig" kubectl get pods -A
```

## List child clusters

To verify the presence of the child cluster, list the available `ClusterDeployment` objects:

```shell
kubectl get ClusterDeployments -A
```
```console
NAMESPACE    NAME                          READY   STATUS
kcm-system   my-remote-clusterdeployment1   True    ClusterDeployment is ready
```

## Tear down the child cluster

To tear down the child cluster, delete the `ClusterDeployment`:

```shell
kubectl delete ClusterDeployment my-remote-clusterdeployment1 -n kcm-system
```
```console
clusterdeployment.k0rdent.mirantis.com "my-remote-clusterdeployment1" deleted
```

## Next Steps

Now that you've finished the k0rdent QuickStart, we have some suggestions for what to do next:

Check out the [Administrator Guide](admin-before.md) ...

* For a more detailed view of k0rdent setup for production
* For details about setting up k0rdent to manage clusters on VMware and OpenStack
* For details about using k0rdent with cloud Kubernetes distros: AWS EKS and Azure AKS

Or check out the [Demos Repository](https://github.com/k0rdent/demos) for fast, makefile-driven demos of k0rdent's key features!
