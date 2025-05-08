# QuickStart 2 - AWS target environment

In this QuickStart unit, we'll be gathering information and performing preparatory steps to enable {{{ docsVersionInfo.k0rdentName }}} (running on your management node) to manage clusters on Amazon Web Services (AWS), and we'll deploy our first child cluster.

As noted in the [Guide to QuickStarts](./index.md), you'll need administrative access to an AWS account to complete this step. If you haven't yet created a management node and installed {{{ docsVersionInfo.k0rdentName }}}, go back to [QuickStart 1 - Management node and cluster](./quickstart-1-mgmt-node-and-cluster.md).

Note that if you have already done our Azure QuickStart ([QuickStart 2 - Azure target environment](./quickstart-2-azure.md)) you can  use the same management cluster, continuing here with steps to add the ability to manage clusters on AWS. The {{{ docsVersionInfo.k0rdentName }}} management cluster can accommodate multiple provider and credential setups, enabling management of multiple infrastructures. And even if your management node is external to AWS (for example, it could be on an Azure virtual machine), as long as you permit outbound traffic to all IP addresses from the management node, this should work fine. A big benefit of {{{ docsVersionInfo.k0rdentName }}} is that it provides a single point of control and visibility across multiple clusters on multiple clouds and infrastructures.

> NOTE:
> **CLOUD SECURITY 101**: {{{ docsVersionInfo.k0rdentName }}} requires _some_ but not _all_ permissions
> to manage AWS via the CAPA (ClusterAPI for AWS) provider.

Because {{{ docsVersionInfo.k0rdentName }}} doesn't require all permissions, a best practice for using {{{ docsVersionInfo.k0rdentName }}} with AWS (this pattern is repeated
with other clouds and infrastructures) is to create a new user on your account with the particular permissions it and CAPA require. In this section, we'll create and configure IAM for that user, and perform other steps to make that {{{ docsVersionInfo.k0rdentName }}} user's credentials accessible to it in the management node.

> NOTE:
> If you're working on a shared AWS account, please ensure that the {{{ docsVersionInfo.k0rdentName }}} user is not already set up before creating a new one.

Creating a {{{ docsVersionInfo.k0rdentName }}} user with minimal required permissions is one of several principle-of-least-privilege mechanisms used to help ensure security as organizations work with Kubernetes at progressively greater scales. For more on {{{ docsVersionInfo.k0rdentName }}} security best practices, please see the [Administrator Guide](../admin/index.md).

## Install the AWS CLI

We'll use the AWS CLI to create and set IAM permissions for the {{{ docsVersionInfo.k0rdentName }}} user, so we'll install it on our management node:

```shell
sudo apt install unzip
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" 
unzip awscliv2.zip 
sudo ./aws/install
```

## Install clusterawsadm

{{{ docsVersionInfo.k0rdentName }}} uses Cluster API (CAPI) to marshal clouds and infrastructures. For AWS, this means using the components from the Cluster API Provider AWS (CAPA) project. This QuickStart leverages [`clusterawsadm`](https://cluster-api-aws.sigs.k8s.io/), a CLI tool created by the CAPA project that helps with AWS-specific tasks like IAM role, policy, and credential configuration.

To install `clusterawsadm` on Ubuntu on x86 hardware:

```shell
curl -LO https://github.com/kubernetes-sigs/cluster-api-provider-aws/releases/download/v2.7.1/clusterawsadm-linux-amd64
sudo install -o root -g root -m 0755 clusterawsadm-linux-amd64 /usr/local/bin/clusterawsadm
```

## Export your administrative credentials

You should have these already, preserved somewhere safe. If not, you can visit the AWS webUI (Access Management > Users) and generate new credentials (Access Key ID, Secret Access Key, and Session Token (if using multi-factor authentication)).

Export the credentials to the management node environment:

```shell
export AWS_REGION=EXAMPLE_AWS_REGION
export AWS_ACCESS_KEY_ID=EXAMPLE_ACCESS_KEY_ID
export AWS_SECRET_ACCESS_KEY=EXAMPLE_SECRET_ACCESS_KEY
export AWS_SESSION_TOKEN=EXAMPLE_SESSION_TOKEN # Optional. If you are using Multi-Factor or Single Sign On Auth.
```

These credentials will be used both by the AWS CLI (to create your {{{ docsVersionInfo.k0rdentName }}} user) and by `clusterawsadm` (to create a CloudFormation template used by CAPA within {{{ docsVersionInfo.k0rdentName }}}).

## Check for available IPs

Because {{{ docsVersionInfo.k0rdentName }}} has 3 availablilty zone NAT gateways, each cluster needs 3 public IPs. Unfortunately, the default
`EC2-VPC Elastic IPs` quota per region is 5, so while you likely won't have issues with a first cluster, if you try to deplay a 
second to the same region, you are likely to run into issues.  

You can determine how many elastic IPs are available from the command line:

```shell
LIMIT=$(aws ec2 describe-account-attributes --attribute-names vpc-max-elastic-ips --query 'AccountAttributes[0].AttributeValues[0].AttributeValue' --output text)
USED=$(aws ec2 describe-addresses --query 'Addresses[*].PublicIp' --output text | wc -w)
AVAILABLE=$((LIMIT - USED))
echo "Available Public IPs: $AVAILABLE"
```
```console
Available Public IPs: 5
```

If you have less than 3 available public IPs, you can request an increase in your quota:

```shell
aws service-quotas request-service-quota-increase \
    --service-code ec2 \
    --quota-code L-0263D0A3 \
    --desired-value 20
```

You can check on the status of your request:

```shell
aws service-quotas list-requested-service-quota-change-history \
    --service-code ec2
```
```console
{
    "RequestedQuotas": [
        {
            "Id": "EXAMPLE_ACCESS_KEY_ID",
            "ServiceCode": "ec2",
            "ServiceName": "Amazon Elastic Compute Cloud (Amazon EC2)",
            "QuotaCode": "L-0263D0A3",
            "QuotaName": "EC2-VPC Elastic IPs",
            "DesiredValue": 20.0,
            "Status": "PENDING",
            "Created": "2025-02-09T02:27:01.573000-05:00",
            "LastUpdated": "2025-02-09T02:27:01.956000-05:00",
            "Requester": "{\"accountId\":\"EXAMPLE_ACCESS_KEY_ID\",\"callerArn\":\"arn:aws:iam::EXAMPLE_ACCESS_KEY_ID:user/nchase\"}",
            "QuotaArn": "arn:aws:servicequotas:EXAMPLE_AWS_REGION:EXAMPLE_ACCESS_KEY_ID:ec2/L-0263D0A3",
            "GlobalQuota": false,
            "Unit": "None",
            "QuotaRequestedAtLevel": "ACCOUNT"
        }
    ]
}
```

## Create the {{{ docsVersionInfo.k0rdentName }}} AWS user

Now we can use the AWS CLI to create a new {{{ docsVersionInfo.k0rdentName }}} user:

```shell
 aws iam create-user --user-name k0rdentQuickstart
```
```console
{
    "User": {
        "Path": "/",
        "UserName": "k0rdentQuickstart",
        "UserId": "EXAMPLE_USER_ID",
        "Arn": "arn:aws:iam::FAKE_ARN_123:user/k0rdentQuickstart",
        "CreateDate": "2025-01-18T08:15:27+00:00"
    }
}
```

## Configure AWS IAM for {{{ docsVersionInfo.k0rdentName }}}

Before {{{ docsVersionInfo.k0rdentName }}} CAPI can manage resources on AWS, you need to use `clusterawsadm` to create a bootstrap CloudFormation stack with additional IAM policies and a service account. You do this under the administrative account credentials you earlier exported to the management node environment:

```shell
clusterawsadm bootstrap iam create-cloudformation-stack
```

## Attach IAM policies to the {{{ docsVersionInfo.k0rdentName }}} user

Next, we'll attach appropriate policies to the {{{ docsVersionInfo.k0rdentName }}} user. These are:

* `control-plane.cluster-api-provider-aws.sigs.k8s.io`
* `controllers.cluster-api-provider-aws.sigs.k8s.io`
* `nodes.cluster-api-provider-aws.sigs.k8s.io`
* `controllers-eks.cluster-api-provider-aws.sigs.k8s.io`

We use the AWS CLI to attach them. To do this, you will need to extract the Amazon Resource Name (ARN) for the newly-created user:

```shell
AWS_ARN_ID=$(aws iam get-user --user-name k0rdentQuickstart --query 'User.Arn' --output text | sed -E 's/.*::([0-9]+):.*/\1/')
echo $AWS_ARN_ID
```

 Assemble and execute the following commands to implement the required policies:

```shell
aws iam attach-user-policy --user-name k0rdentQuickstart --policy-arn arn:aws:iam::$AWS_ARN_ID:policy/controllers.cluster-api-provider-aws.sigs.k8s.io
aws iam attach-user-policy --user-name k0rdentQuickstart --policy-arn arn:aws:iam::$AWS_ARN_ID:policy/control-plane.cluster-api-provider-aws.sigs.k8s.io
aws iam attach-user-policy --user-name k0rdentQuickstart --policy-arn arn:aws:iam::$AWS_ARN_ID:policy/nodes.cluster-api-provider-aws.sigs.k8s.io
aws iam attach-user-policy --user-name k0rdentQuickstart --policy-arn arn:aws:iam::$AWS_ARN_ID:policy/controllers-eks.cluster-api-provider-aws.sigs.k8s.io
```

We can check to see that policies were attached to the new user:

```shell
aws iam list-attached-user-policies --user-name k0rdentQuickstart

```
And you'll see output that looks like this (this is non-valid example text):

```console
{
    "AttachedPolicies": [
        {
            "PolicyName": "controllers-eks.cluster-api-provider-aws.sigs.k8s.io",
            "PolicyArn": "arn:aws:iam::AWS_ARN_ID:policy/controllers-eks.cluster-api-provider-aws.sigs.k8s.io"
        },
        {
            "PolicyName": "controllers.cluster-api-provider-aws.sigs.k8s.io",
            "PolicyArn": "arn:aws:iam::AWS_ARN_ID:policy/controllers.cluster-api-provider-aws.sigs.k8s.io"
        },
        {
            "PolicyName": "control-plane.cluster-api-provider-aws.sigs.k8s.io",
            "PolicyArn": "arn:aws:iam::AWS_ARN_ID:policy/control-plane.cluster-api-provider-aws.sigs.k8s.io"
        },
        {
            "PolicyName": "nodes.cluster-api-provider-aws.sigs.k8s.io",
            "PolicyArn": "arn:aws:iam::AWS_ARN_ID:policy/nodes.cluster-api-provider-aws.sigs.k8s.io"
        }
    ]
}
```

## Create AWS credentials for the {{{ docsVersionInfo.k0rdentName }}} user

In the AWS IAM Console, you can now create the Access Key ID and Secret Access Key for the {{{ docsVersionInfo.k0rdentName }}} user and download them. You can also do this via the AWS CLI:

```shell
aws iam create-access-key --user-name k0rdentQuickstart
```

You should see something like this. It's important to save these credentials securely somewhere other than the management node, since the management node may end up being ephemeral. Again, this is non-valid example text:

```console
{
    "AccessKey": {
        "UserName": "k0rdentQuickstart",
        "AccessKeyId": "EXAMPLE_ACCESS_KEY_ID",
        "Status": "Active",
        "SecretAccessKey": "EXAMPLE_SECRET_ACCESS_KEY",
        "CreateDate": "2025-01-18T08:33:35+00:00"
    }
}
```

<!--
> WARNING:
> You may encounter an issue where EKS machines are not created due to the `ControlPlaneIsStable` preflight check
> failure during EKS cluster deployment. Please follow the
> [instruction](known-issues-eks.md#eks-machines-are-not-created-controlplaneisstable-preflight-check-failed)
> to apply the workaround.
-->

## Create IAM credentials secret on the management cluster

Next, we create a `Secret` containing credentials for the {{{ docsVersionInfo.k0rdentName }}} user and apply this to the management cluster running {{{ docsVersionInfo.k0rdentName }}}, in the `kcm-system` namespace. Important: if you use another namespace, {{{ docsVersionInfo.k0rdentName }}} will be unable to read the credentials. To do this, create the following YAML in a file called `aws-cluster-identity-secret.yaml`:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: aws-cluster-identity-secret
  namespace: kcm-system
  labels:
    k0rdent.mirantis.com/component: "kcm"
type: Opaque
stringData:
  AccessKeyID: "EXAMPLE_ACCESS_KEY_ID"
  SecretAccessKey: "EXAMPLE_SECRET_ACCESS_KEY"
```

Remember: the Access Key ID and Secret Access Key are the ones you generated for the {{{ docsVersionInfo.k0rdentName }}} user, `k0rdentQuickStart`.

Apply this YAML to the management cluster as follows:

```shell
kubectl apply -f aws-cluster-identity-secret.yaml -n kcm-system
```

## Create the AWSClusterStaticIdentity object

Next, we need to create an `AWSClusterStaticIdentity` object that uses the secret.

To do this, create a YAML file named `aws-cluster-identity.yaml` as follows:

```yaml
apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
kind: AWSClusterStaticIdentity
metadata:
  name: aws-cluster-identity
  labels:
    k0rdent.mirantis.com/component: "kcm"
spec:
  secretRef: aws-cluster-identity-secret
  allowedNamespaces:
    selector:
      matchLabels: {}
```

Note that the `spec.secretRef` is the same as the `metadata.name` of the secret we just created.

Create the object as follows:

```shell
kubectl apply -f aws-cluster-identity.yaml  -n kcm-system
```

## Create the {{{ docsVersionInfo.k0rdentName }}} Cluster Manager credential object

Now we create the {{{ docsVersionInfo.k0rdentName }}} Cluster Manager credential object. As in prior steps, create a YAML file called `aws-cluster-identity-cred.yaml`:

```yaml
apiVersion: k0rdent.mirantis.com/v1alpha1
kind: Credential
metadata:
  name: aws-cluster-identity-cred
  namespace: kcm-system
spec:
  description: "Credential Example"
  identityRef:
    apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
    kind: AWSClusterStaticIdentity
    name: aws-cluster-identity
```

Note that `.spec.identityRef.kind` must be `AWSClusterStaticIdentity` and `.spec.identityRef.name` must match the `.metadata.name` of the `AWSClusterStaticIdentity` object.

Now apply this YAML to your management cluster:

```shell
kubectl apply -f aws-cluster-identity-cred.yaml -n kcm-system
```

## Create the {{{ docsVersionInfo.k0rdentName }}} Cluster Identity resource template ConfigMap

Now we create the {{{ docsVersionInfo.k0rdentName }}} Cluster Identity resource template `ConfigMap`. As in prior steps, create a YAML file called `aws-cluster-identity-resource-template.yaml`:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: aws-cluster-identity-resource-template
  namespace: kcm-system
  labels:
    k0rdent.mirantis.com/component: "kcm"
  annotations:
    projectsveltos.io/template: "true"
```

Note that `ConfigMap` is empty. This is expected, we don't need to template any object inside child cluster(s), but we can use that object in the future if need arises.

Now apply this YAML to your management cluster:

```shell
kubectl apply -f aws-cluster-identity-resource-template.yaml -n kcm-system
```

## List available cluster templates

{{{ docsVersionInfo.k0rdentName }}} is now fully configured to manage AWS. To create a cluster, begin by listing the available `ClusterTemplate` objects provided with {{{ docsVersionInfo.k0rdentName }}}:

```shell
kubectl get clustertemplate -n kcm-system
```

You'll see output resembling what's below. Grab the name of the AWS standalone cluster template in its present version (in the below example, that's `aws-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsStandaloneCpCluster }}}`):

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
kcm-system   vsphere-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.vsphereHostedCpCluster }}}         true
kcm-system   vsphere-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.vsphereStandaloneCpCluster }}}     true
```

## Create your ClusterDeployment

Now, to deploy a cluster, create a YAML file called `my-aws-clusterdeployment1.yaml`. We'll use this to create a `ClusterDeployment` object in {{{ docsVersionInfo.k0rdentName }}}, representing the deployed cluster. The `ClusterDeployment` identifies for {{{ docsVersionInfo.k0rdentName }}} the `ClusterTemplate` you want to use for cluster creation, the identity credential object you want to create it under (that of your {{{ docsVersionInfo.k0rdentName }}} user), plus the region and instance types you want to use to host control plane and worker nodes:

```yaml
apiVersion: k0rdent.mirantis.com/v1alpha1
kind: ClusterDeployment
metadata:
  name: my-aws-clusterdeployment1
  namespace: kcm-system
spec:
  template: aws-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsStandaloneCpCluster }}}
  credential: aws-cluster-identity-cred
  config:
    clusterLabels: {}
    region: us-east-2
    controlPlane:
      instanceType: t3.small
      rootVolumeSize: 32
    worker:
      instanceType: t3.small
      rootVolumeSize: 32
```

## Apply the `ClusterDeployment` to deploy the cluster

Finally, we'll apply the `ClusterDeployment` YAML (`my-aws-clusterdeployment1.yaml`) to instruct {{{ docsVersionInfo.k0rdentName }}} to deploy the cluster:

```shell
kubectl apply -f my-aws-clusterdeployment1.yaml
```

Kubernetes should confirm this:

```console
clusterdeployment.k0rdent.mirantis.com/my-aws-clusterdeployment1 created
```

There will be a delay as the cluster finishes provisioning. You can watch the provisioning process with the following command:

```shell
kubectl -n kcm-system get clusterdeployment.k0rdent.mirantis.com my-aws-clusterdeployment1 --watch
```

In a short while, you'll see output such as:

```console
NAME                        READY   STATUS
my-aws-clusterdeployment1   True    ClusterDeployment is ready
```

## Obtain the cluster's kubeconfig

Now you can retrieve the cluster's `kubeconfig`:

```shell
kubectl -n kcm-system get secret my-aws-clusterdeployment1-kubeconfig -o jsonpath='{.data.value}' | base64 -d > my-aws-clusterdeployment1.kubeconfig
```

And you can use the `kubeconfig` to see what's running on the cluster:

```shell
KUBECONFIG="my-aws-clusterdeployment1.kubeconfig" kubectl get pods -A
```

## List child clusters

To verify the presence of the child cluster, list the available `ClusterDeployment` objects:

```shell
kubectl get ClusterDeployments -A
```

You'll see output something like this:

```console
NAMESPACE    NAME                        READY   STATUS
kcm-system   my-aws-clusterdeployment1   True    ClusterDeployment is ready
```

## Tear down the child cluster

To tear down the child cluster, delete the `ClusterDeployment`:

```shell
kubectl delete ClusterDeployment my-aws-clusterdeployment1 -n kcm-system
```

You'll see confirmation like this:

```console
clusterdeployment.k0rdent.mirantis.com "my-aws-clusterdeployment1" deleted
```

## Next Steps

Now that you've finished the {{{ docsVersionInfo.k0rdentName }}} QuickStart, we have some suggestions for what to do next:

Check out the [Administrator Guide](../admin/index.md) ...

* For a more detailed view of {{{ docsVersionInfo.k0rdentName }}} setup for production
* For details about setting up {{{ docsVersionInfo.k0rdentName }}} to manage clusters on VMware and OpenStack
* For details about using {{{ docsVersionInfo.k0rdentName }}} with cloud Kubernetes distros: AWS EKS and Azure AKS

<!--
Or check out the [Demos Repository](https://github.com/k0rdent/demos) for fast, makefile-driven demos of {{{ docsVersionInfo.k0rdentName }}}'s key features.
-->