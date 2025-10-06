# AWS

{{{ docsVersionInfo.k0rdentName }}} can deploy managed clusters as both EC2-based Kubernetes clusters and EKS clusters. In both cases, you'll need to create the relevant credentials, and to do that you'll need to configure an IAM user. Follow these steps to make it possible to deploy to AWS:

## Test user creation

Part of this process involves creating a user, which is sometimes forbidden by organizational policies. Fortunately once the user is created you don't need to do it again, so if you're not sure, either contact your administrator or run this test.

1. Configure AWS IAM

    Start by specifying the environment variables the AWS CLI will use:

    ```bash
    export AWS_REGION=<EXAMPLE_AWS_REGION>
    export AWS_ACCESS_KEY_ID=<EXAMPLE_ACCESS_KEY_ID>
    export AWS_SECRET_ACCESS_KEY=<EXAMPLE_SECRET_ACCESS_KEY>
    export AWS_SESSION_TOKEN=<YOUR_SESSION_TOKEN> # Optional. If you are using Multi-Factor Auth.
    ```

2. Install the AWS CLI
 
	  If you haven't already, install the `aws` CLI tool:

    ```bash
    sudo apt install unzip
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" 
    unzip awscliv2.zip 
    sudo ./aws/install
    ```

  	The tool recognizes the environment variables you created earlier, so there's no need to login.

3. Create and delete a test user

    There are ways test the permissions assigned to your user, but the only way to ensure there are no policies preventing you from creating a user is to actually do it.  Execute these commands:

    ```bash
    aws iam create-user --user-name test-delete-me
    aws iam delete-user --user-name test-delete-me
    ```

    If your account can create a user, you'll see output such as:

    ```console  { .no-copy }
    {
        "User": {
            "Path": "/",
            "UserName": "test-delete-me",
            "UserId": "EXAMPLE_USER_ID",
            "Arn": "arn:aws:iam::FAKE_ARN_123:user/test-delete-me",
            "CreateDate": "2025-10-05T17:02:36+00:00"
        }
    }
    ```

    Note that you will NOT see any indication that the user has been deleted, even though it has. You can make sure by running:

    ```bash 
    aws iam get-user --user-name test-delete-me
    ```
    ```console { .no-copy }
    An error occurred (NoSuchEntity) when calling the GetUser operation: The user with name test-delete-me cannot be found.
    ```

If you are unable to create a user, contact your administrator to request the user creation. (You should also show them this page to make sure you won't run into other issues.)

## Configure the system for AWS child clusters

Now go ahead and prepare the cluster.

1. Install {{{ docsVersionInfo.k0rdentName }}}

    Follow the instructions in [Install {{{ docsVersionInfo.k0rdentName }}}](../install-k0rdent.md) to create a management cluster with {{{ docsVersionInfo.k0rdentName }}} running.

2. Install `clusterawsadm`

    {{{ docsVersionInfo.k0rdentName }}} uses the Cluster API (CAPI) to marshal clouds and infrastructures. For AWS, this means using the components from the Cluster API Provider AWS (CAPA) project. `clusterawsadm`, a CLI tool created by CAPA project, helps with AWS-specific tasks such as creating IAM roles and policies, as well as credential configuration. To install clusterawsadm on Ubuntu on x86 hardware, execute these commands:

    ```bash
    curl -LO https://github.com/kubernetes-sigs/cluster-api-provider-aws/releases/download/v2.7.1/clusterawsadm-linux-amd64
    sudo install -o root -g root -m 0755 clusterawsadm-linux-amd64 /usr/local/bin/clusterawsadm
    ```

3. Configure AWS IAM

    Next you'll need to create the IAM policies and service account {{{ docsVersionInfo.k0rdentName }}} will use to take action within the AWS infrastructure. (Note that you only need to do this once.)

    The first step is to create the IAM CloudFormation stack based on your admin user. Start by specifying the environment variables `clusterawsadm` will use as AWS credentials:

    ```bash
    export AWS_REGION=<EXAMPLE_AWS_REGION>
    export AWS_ACCESS_KEY_ID=<EXAMPLE_ACCESS_KEY_ID>
    export AWS_SECRET_ACCESS_KEY=<EXAMPLE_SECRET_ACCESS_KEY>
    export AWS_SESSION_TOKEN=<YOUR_SESSION_TOKEN> # Optional. If you are using Multi-Factor Auth.
    ```

4. Create the IAM CloudFormation stack

  	Now use `clusterawsadm` to create the IAM CloudFormation stack:

    ```bash
	  clusterawsadm bootstrap iam create-cloudformation-stack
	  ```
	
5. Install the AWS CLI
 
	  With the stack in place you can create the AWS IAM user. You can do this in the UI, but it's also possible to do it from the command line using the `aws` CLI tool.  Start by installing it, if you haven't already:

    ```bash
    sudo apt install unzip
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" 
    unzip awscliv2.zip 
    sudo ./aws/install
    ```

  	The tool recognizes the environment variables you created earlier, so there's no need to login.

6. Check for available IPs

    Because {{{ docsVersionInfo.k0rdentName }}} has 3 availablilty zone NAT gateways, each cluster needs 3 public IPs. Unfortunately, the default
    `EC2-VPC Elastic IPs` quota per region is 5, so while you likely won't have issues with a first cluster, if you try to deplay a 
    second to the same region, you are likely to run into issues.  

    You can determine how many elastic IPs are available from the command line:

    ```bash
    LIMIT=$(aws ec2 describe-account-attributes --attribute-names vpc-max-elastic-ips --query 'AccountAttributes[0].AttributeValues[0].AttributeValue' --output text)
    USED=$(aws ec2 describe-addresses --query 'Addresses[*].PublicIp' --output text | wc -w)
    AVAILABLE=$((LIMIT - USED))
    echo "Available Public IPs: $AVAILABLE"
    ```
    ```console { .no-copy }
    Available Public IPs: 5
    ```

    If you have less than 3 available public IPs, you can request an increase in your quota:

    ```bash
    aws service-quotas request-service-quota-increase \
        --service-code ec2 \
        --quota-code L-0263D0A3 \
        --desired-value 20
    ```

    You can check on the status of your request:

    ```bash
    aws service-quotas list-requested-service-quota-change-history \
        --service-code ec2
    ```
    ```console { .no-copy }
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

6. Create the IAM user. 

	  The actual `user-name` parameter is arbitrary; you can specify it as anything you like:

    ```bash
    aws iam create-user --user-name k0rdentUser
    ```
    ```console { .no-copy }
    {
      "User": {
        "Path": "/",
        "UserName": "k0rdentUser",
        "UserId": "EXAMPLE_USER_ID",
        "Arn": "arn:aws:iam::FAKE_ARN_123:user/k0rdentUser",
        "CreateDate": "2025-01-18T08:15:27+00:00"
      }
    }
    ```

7. Assign the relevant policies
 
    You'll need to assign the following policies to the user you just created:

    ```bash
    control-plane.cluster-api-provider-aws.sigs.k8s.io
    controllers.cluster-api-provider-aws.sigs.k8s.io
    nodes.cluster-api-provider-aws.sigs.k8s.io
    controllers-eks.cluster-api-provider-aws.sigs.k8s.io
    ```
    To do that, you'll need the ARNs for each policy.  You can get them with the `list-policies` command, as in:

    ```bash
    aws iam list-policies --scope Local
    ```
    ```console { .no-copy }
    {
      "Policies": [
        {
          "PolicyName": "controllers-eks.cluster-api-provider-aws.sigs.k8s.io",
          "PolicyId": "ANPA22CF4NNF3VUDTMH3N",
          "Arn": "arn:aws:iam::FAKE_ARN_123:policy/controllers-eks.cluster-api-provider-aws.sigs.k8s.io",
          "Path": "/",
          "DefaultVersionId": "v1",
          "AttachmentCount": 2,
          "PermissionsBoundaryUsageCount": 0,
          "IsAttachable": true,
          "CreateDate": "2025-01-01T18:47:43+00:00",
          "UpdateDate": "2025-01-01T18:47:43+00:00"
        },
        {
          "PolicyName": "nodes.cluster-api-provider-aws.sigs.k8s.io",
          "PolicyId": "ANPA22CF4NNF5TAKL44PU",
          "Arn": "arn:aws:iam::FAKE_ARN_123:policy/nodes.cluster-api-provider-aws.sigs.k8s.io",
          "Path": "/",
          "DefaultVersionId": "v1",
          "AttachmentCount": 3,
          "PermissionsBoundaryUsageCount": 0,
          "IsAttachable": true,
          "CreateDate": "2025-01-01T18:47:44+00:00",
          "UpdateDate": "2025-01-01T18:47:44+00:00"
        },
        {
          "PolicyName": "controllers.cluster-api-provider-aws.sigs.k8s.io",
          "PolicyId": "ANPA22CF4NNFVO6OHIQOE",
          "Arn": "arn:aws:iam::FAKE_ARN_123:policy/controllers.cluster-api-provider-aws.sigs.k8s.io",
          "Path": "/",
          "DefaultVersionId": "v1",
          "AttachmentCount": 3,
          "PermissionsBoundaryUsageCount": 0,
          "IsAttachable": true,
          "CreateDate": "2025-01-01T18:47:43+00:00",
          "UpdateDate": "2025-01-01T18:47:43+00:00"
        },
        {
          "PolicyName": "control-plane.cluster-api-provider-aws.sigs.k8s.io",
          "PolicyId": "ANPA22CF4NNFY4FJ3DA2E",
          "Arn": "arn:aws:iam::FAKE_ARN_123:policy/control-plane.cluster-api-provider-aws.sigs.k8s.io",
          "Path": "/",
          "DefaultVersionId": "v1",
          "AttachmentCount": 2,
          "PermissionsBoundaryUsageCount": 0,
          "IsAttachable": true,
          "CreateDate": "2025-01-01T18:47:43+00:00",
          "UpdateDate": "2025-01-01T18:47:43+00:00"
        }
      ]
    }
    ```

    Now you can add the policies using the `attach-user-policy` command and the ARNs you retrieved in the previous step:

    ```bash
    aws iam attach-user-policy --user-name k0rdentUser --policy-arn arn:aws:iam::FAKE_ARN_123:policy/controllers.cluster-api-provider-aws.sigs.k8s.io
    aws iam attach-user-policy --user-name k0rdentUser --policy-arn arn:aws:iam::FAKE_ARN_123:policy/control-plane.cluster-api-provider-aws.sigs.k8s.io
    aws iam attach-user-policy --user-name k0rdentUser --policy-arn arn:aws:iam::FAKE_ARN_123:policy/nodes.cluster-api-provider-aws.sigs.k8s.io
    aws iam attach-user-policy --user-name k0rdentUser --policy-arn arn:aws:iam::FAKE_ARN_123:policy/controllers-eks.cluster-api-provider-aws.sigs.k8s.io
    ```
	
8. Create an access key and secret

    To access AWS as this new user, you'll need to create an access key:

    ```bash
    aws iam create-access-key --user-name k0rdentUser 
    ```
    ```console { .no-copy }
    {
      "AccessKey": {
        "UserName": "k0rdentUser",
        "AccessKeyId": "EXAMPLE_ACCESS_KEY_ID",
        "Status": "Active",
        "SecretAccessKey": "EXAMPLE_SECRET_ACCESS_KEY",
        "CreateDate": "2025-01-18T08:33:35+00:00"
      }
    }
    ```

9. Create the IAM Credentials `Secret` on the {{{ docsVersionInfo.k0rdentName }}} Management Cluster

    Create a YAML file called `aws-cluster-identity-secret.yaml` and add the following text, including the `AccessKeyId` and `SecretAccessKey` you created in the previous step:

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
      AccessKeyID: EXAMPLE_ACCESS_KEY_ID
      SecretAccessKey: EXAMPLE_SECRET_ACCESS_KEY
    ```

    Apply the YAML to your cluster, making sure to add it to the namespace where the CAPA provider is running (currently `kcm-system`) so the controller can read it:

    ```bash
    kubectl apply -f aws-cluster-identity-secret.yaml -n kcm-system
    ```

10. Create the `AWSClusterStaticIdentity`

    Create the `AWSClusterStaticIdentity` object in a file named `aws-cluster-identity.yaml`:

    ```yaml
    apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
    kind: AWSClusterStaticIdentity
    metadata:
      name: aws-cluster-identity
      labels:
        k0rdent.mirantis.com/component: "kcm"
    spec:
      secretRef: aws-cluster-identity-secret
      allowedNamespaces: {}
    ```

    Notice that the `secretRef` references the `Secret` you created in the previous step.

    Apply the YAML to your cluster, again adding it to the `kcm-system` namespace.

    ```bash
    kubectl apply -f aws-cluster-identity.yaml  -n kcm-system
    ```

11. Create the Cluster Identity resource template `ConfigMap`

    Now we create Cluster Identity resource template `ConfigMap`. As in prior steps, create a YAML file called `aws-cluster-identity-resource-template.yaml`:

    ```yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: aws-cluster-identity-resource-template
      labels:
        k0rdent.mirantis.com/component: "kcm"
      annotations:
        projectsveltos.io/template: "true"
    ```

    Note that `ConfigMap` is empty, this is expected, we don't need to template any object inside child cluster(s), but we can use that object in the future if need arises.

    Apply the YAML to your cluster, again keeping it in the `kcm-system` namespace:

    ```bash
    kubectl apply -f aws-cluster-identity-resource-template.yaml -n kcm-system
    ```

12. Create the `Credential`

    Finally, create the KCM `Credential` object, making sure to reference the `AWSClusterStaticIdentity` you just created:

    ```yaml
    apiVersion: k0rdent.mirantis.com/v1beta1
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
    Apply the YAML to your cluster, again keeping it in the `kcm-system` namespace:

    ```bash
    kubectl apply -f aws-cluster-identity-cred.yaml -n kcm-system
    ```


13. Deploy a cluster

    Make sure everything is configured properly by creating a `ClusterDeployment`. Start with a YAML file specifying the `ClusterDeployment`, as in:

    ```yaml
    apiVersion: k0rdent.mirantis.com/v1beta1
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
    > NOTE:
    > - You're giving it an arbitrary name in `.metadata.name` (`my-aws-clusterdeployment1`)
    > - You're referencing the credential you created in the previous step, `aws-cluster-identity-cred`. This enables you to set up a system where users can take advantage of having access to the credentials to the AWS account without actually having those credentials in hand.
    > - You need to choose a template to use for the cluster, in this case `aws-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsStandaloneCpCluster }}}`. You can get a list of available templates using:

    ```bash
    kubectl get clustertemplate -n kcm-system
    ```
    ```console { .no-copy }
    NAME                            VALID
    adopted-cluster-{{{ extra.docsVersionInfo.k0rdentVersion }}}           true
    aws-eks-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsEksCluster }}}                   true
    aws-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsHostedCpCluster }}}             true
    aws-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsStandaloneCpCluster }}}         true
    azure-aks-{{{ extra.docsVersionInfo.providerVersions.dashVersions.azureAksCluster }}}                 true
    azure-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.azureHostedCpCluster }}}           true
    azure-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.azureStandaloneCpCluster }}}       true
    openstack-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.openstackStandaloneCpCluster }}}   true
    vsphere-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.vsphereHostedCpCluster }}}         true
    vsphere-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.vsphereStandaloneCpCluster }}}     true
    ```
    Apply the YAML to your management cluster:
    ```bash
    kubectl apply -f my-aws-clusterdeployment1.yaml
    ```
    ```console { .no-copy }
    clusterdeployment.k0rdent.mirantis.com/my-aws-clusterdeployment1 created
    ```
    As before, there will be a delay as the cluster finishes provisioning. Follow the provisioning process with:
    ```bash
    kubectl -n kcm-system get clusterdeployment.k0rdent.mirantis.com my-aws-clusterdeployment1 --watch
    ```
    ```console { .no-copy }
    NAME                        READY   STATUS
    my-aws-clusterdeployment1   True    ClusterDeployment is ready
    ```
    When the cluster is `Ready`, you can access it via the kubeconfig, as in:
    ```bash
    kubectl -n kcm-system get secret my-aws-clusterdeployment1-kubeconfig -o jsonpath='{.data.value}' | base64 -d > my-aws-clusterdeployment1-kubeconfig.kubeconfig
    KUBECONFIG="my-aws-clusterdeployment1-kubeconfig.kubeconfig" kubectl get pods -A
    ```

14. Cleanup

    When you've established that it's working properly, you can delete the managed cluster and its AWS objects:

    ```bash
    kubectl delete clusterdeployments my-aws-clusterdeployment1 
    ```

