# AWS Hosted Control Plane Deployment

Follow these steps to set up a k0smotron-hosted control plane on AWS: 

1. Prerequisites

    Before proceeding, make sure you have the following:

    * A management Kubernetes cluster (Kubernetes v1.28 or later) deployed on AWS with [{{{ docsVersionInfo.k0rdentName }}} installed](../installation/install-k0rdent.md).
    * A [default storage class](https://kubernetes.io/docs/tasks/administer-cluster/change-default-storage-class/) configured on the management cluster to support Persistent Volumes.
    * The VPC ID where the worker nodes will be deployed.
    * The Subnet ID and Availability Zone (AZ) for the worker nodes.
    * The AMI ID for the worker nodes (Amazon Machine Image ID for the desired OS and Kubernetes version).

    > IMPORTANT:  
    > All control plane components for your hosted cluster will reside in the management cluster, and the management cluster 
    > must have sufficient resources to handle these additional workloads.

2. Networking

    To deploy a hosted control plane, the necessary AWS networking resources must already exist or be created. If you're 
    using the same VPC and subnets as your management cluster, you can reuse these resources.

    If your management cluster was deployed using the Cluster API Provider AWS (CAPA), you can gather the required 
    networking details using the following commands:

    Retrieve the VPC ID:
    ```shell
    kubectl get awscluster <cluster-name> -o go-template='{{.spec.network.vpc.id}}'
    ```

    Retrieve Subnet ID:
    ```shell
    kubectl get awscluster <cluster-name> -o go-template='{{(index .spec.network.subnets 0).resourceID}}'
    ```

    Retrieve Availability Zone:
    ```shell
    kubectl get awscluster <cluster-name> -o go-template='{{(index .spec.network.subnets 0).availabilityZone}}'
    ```

    Retrieve Security Group:
    ```shell
    kubectl get awscluster <cluster-name> -o go-template='{{.status.networkStatus.securityGroups.node.id}}'
    ```

    Retrieve AMI ID:
    ```shell
    kubectl get awsmachinetemplate <cluster-name>-worker-mt -o go-template='{{.spec.template.spec.ami.id}}'
    ```

    > TIP:  
    > If you want to use different VPCs or regions for your management and hosted clusters, you’ll need to configure additional networking, such as [VPC peering](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/vpc-peering.html), to allow communication between them.


3. Create the ClusterDeployment manifest

    Once you've collected all the necessary data, you can create the `ClusterDeployment` manifest. This file tells {{{ docsVersionInfo.k0rdentName }}} how to 
    deploy and manage the hosted control plane. For example:

    ```yaml
    apiVersion: k0rdent.mirantis.com/v1alpha1
    kind: ClusterDeployment
    metadata:
      name: aws-hosted-cp
    spec:
      template: aws-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsHostedCpCluster }}}
      credential: aws-credential
      config:
        clusterLabels: {}
        vpcID: vpc-0a000000000000000
        region: us-west-1
        publicIP: true
        subnets:
          - id: subnet-0aaaaaaaaaaaaaaaa
            availabilityZone: us-west-1b
            isPublic: true
            natGatewayID: xxxxxx
            routeTableId: xxxxxx
          - id: subnet-1aaaaaaaaaaaaaaaa
            availabilityZone: us-west-1b
            isPublic: false
            routeTableId: xxxxxx
        instanceType: t3.medium
        securityGroupIDs:
          - sg-0e000000000000000
    ```

    > NOTE:  
    > The example above uses the `us-west-1` region, but you should use the region of your VPC.

4. Generate the `ClusterDeployment` Manifest

    To simplify the creation of a `ClusterDeployment` manifest, you can use the following template, which dynamically 
    inserts the appropriate values:
    ```yaml
    apiVersion: k0rdent.mirantis.com/v1alpha1
    kind: ClusterDeployment
    metadata:
      name: aws-hosted
    spec:
      template: aws-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsHostedCpCluster }}}
      credential: aws-credential
      config:
        clusterLabels: {}
        vpcID: "{{.spec.network.vpc.id}}"
        region: "{{.spec.region}}"
        subnets:
        {{- range $subnet := .spec.network.subnets }}
          - id: "{{ $subnet.resourceID }}"
            availabilityZone: "{{ $subnet.availabilityZone }}"
            isPublic: {{ $subnet.isPublic }}
            {{- if $subnet.isPublic }}
            natGatewayId: "{{ $subnet.natGatewayId }}"
            {{- end }}
            routeTableId: "{{ $subnet.routeTableId }}"
        {{- end }}
        instanceType: t3.medium
        securityGroupIDs:
          - "{{.status.networkStatus.securityGroups.node.id}}"
    ```

    Save this template as `clusterdeployment.yaml.tpl`, then generate your manifest using the following command:

    ```shell
    kubectl get awscluster <cluster-name> -o go-template="$(cat clusterdeployment.yaml.tpl)" > clusterdeployment.yaml
    ```

5. Apply the `ClusterTemplate`

    Nothing actually happens until you apply the `ClusterDeployment` manifest to create a new cluster deployment:

    ```shell
    kubectl apply -f clusterdeployment.yaml -n kcm-system
    ```

## Deployment Tips

Here are some additional tips to help with deployment:

1. Controller and Template Availability:

    Make sure the KCM controller image and templates are available in a public or accessible repository.

2. Install Charts and Templates:

    If you're using a custom repository, run the following commands with the appropriate `kubeconfig`:

    ```shell
    KUBECONFIG=kubeconfig IMG="ghcr.io/k0rdent/kcm/controller-ci:v0.0.1-179-ga5bdf29" REGISTRY_REPO="oci://ghcr.io/k0rdent/kcm/charts-ci" make dev-apply
    KUBECONFIG=kubeconfig make dev-templates
    ```

3. Mark the Infrastructure as Ready:

    To scale up the `MachineDeployment`, manually mark the infrastructure as ready:
    ```shell
    kubectl patch AWSCluster <hosted-cluster-name> --type=merge --subresource status --patch '{"status": {"ready": true}}' -n kcm-system
    ```
    For more details on why this is necessary, [click here](https://docs.k0smotron.io/stable/capi-aws/#:~:text=As%20we%20are%20using%20self%2Dmanaged%20infrastructure%20we%20need%20to%20manually%20mark%20the%20infrastructure%20ready.%20This%20can%20be%20accomplished%20using%20the%20following%20command).
