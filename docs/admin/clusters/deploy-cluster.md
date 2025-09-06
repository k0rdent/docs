# Deploying a Cluster

{{{ docsVersionInfo.k0rdentName }}} is designed to simplify the process of deploying and managing Kubernetes clusters across various cloud platforms. It does this through the use of `ClusterDeployment` objects, which include all of the information {{{ docsVersionInfo.k0rdentName }}} needs to know in order to create the cluster you're looking for. This `ClusterDeployment` system relies on predefined templates and credentials. 

A cluster deployment typically involves:

1. Setting up credentials for the infrastructure provider (for example, AWS, vSphere).
2. Choosing a template that defines the desired cluster configuration (for example, number of nodes, instance types).
3. Submitting the configuration for deployment and monitoring the process.

Follow these steps to deploy a standalone Kubernetes cluster tailored to your specific needs:

1. Create the `Credential` object

    Credentials are essential for {{{ docsVersionInfo.k0rdentName }}} to communicate with the infrastructure provider (for example, AWS, Azure, vSphere). These credentials enable {{{ docsVersionInfo.k0rdentName }}} to provision resources such as virtual machines, networking components, and storage.

    `Credential` objects are generally created ahead of time and made available to users, so before you look into creating a
    new one be sure what you're looking for doesn't already exist. You can see all of the existing `Credential` objects by 
    querying the management cluster:

    ```bash
    kubectl get credentials --all-namespaces
    ```

    If the `Credential` you need doesn't yet exist, go ahead and create it.

    Start by creating a `Credential` object that includes all required authentication details for your chosen infrastructure provider. Follow the instructions in the [chapter about credential management](../access/credentials/index.md), as well as the specific instructions for your [target infrastructure](../installation/prepare-mgmt-cluster/index.md).

    > TIP: 
    > Double-check to make sure that your credentials have sufficient permissions to create resources on the target infrastructure.

2. Select a Template

    Templates in {{{ docsVersionInfo.k0rdentName }}} are predefined configurations that describe how to set up the cluster. Templates include details such as:

    * The number and type of control plane and worker nodes
    * Networking settings
    * Regional deployment preferences

    Templates act as a blueprint for creating a cluster. To see the list of available templates, use the following command:

    ```bash
    kubectl get clustertemplate -n kcm-system
    ```
    ```console
    NAME                            VALID
    adopted-cluster-{{{ extra.docsVersionInfo.providerVersions.dashVersions.adoptedCluster }}}           true
    aws-eks-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsEksCluster }}}                   true
    aws-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsHostedCpCluster }}}             true
    aws-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsStandaloneCpCluster }}}         true
    azure-aks-{{{ extra.docsVersionInfo.providerVersions.dashVersions.azureAksCluster }}}                 true
    azure-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.azureHostedCpCluster }}}           true
    azure-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.azureStandaloneCpCluster }}}       true
    docker-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.dockerHostedCpCluster }}}          true
    gcp-gke-{{{ extra.docsVersionInfo.providerVersions.dashVersions.gcpGkeCluster }}}                   true
    gcp-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.gcpHostedCpCluster }}}             true
    gcp-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.gcpStandaloneCpCluster }}}         true
    openstack-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.openstackStandaloneCpCluster }}}   true
    remote-cluster-{{{ extra.docsVersionInfo.providerVersions.dashVersions.openstackStandaloneCpCluster }}}            true
    vsphere-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.vsphereHostedCpCluster }}}         true
    vsphere-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.vsphereStandaloneCpCluster }}}     true
    ```

    You can then get information on the actual template by describing it, as in:

    ```bash
    kubectl describe clustertemplate aws-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsStandaloneCpCluster }}} -n kcm-system
    ```

3. Create a ClusterDeployment YAML Configuration

    The `ClusterDeployment` object is the main configuration file that defines your cluster's specifications. It includes:

    * The template to use
    * The credentials for the infrastructure provider
    * Optional customizations such as instance types, regions, and networking

    Create a `ClusterDeployment` configuration in a YAML file, following this structure:

    ```yaml
    apiVersion: k0rdent.mirantis.com/v1beta1
    kind: ClusterDeployment
    metadata:
      name: <cluster-name>
      namespace: <kcm-system-namespace>
    spec:
      template: <template-name>
      credential: <infrastructure-provider-credential-name>
      dryRun: <"true" or "false" (default: "false")>
      config:
        <cluster-configuration>
    ```

    You will of course want to replace the placeholders with actual values. (For more information about `dryRun` see [Understanding the Dry Run](../../appendix/appendix-dryrun.md).) For example, this is a simple AWS infrastructure provider `ClusterDeployment`:

    ```yaml
    apiVersion: k0rdent.mirantis.com/v1beta1
    kind: ClusterDeployment
    metadata:
      name: my-cluster-deployment
      namespace: kcm-system
    spec:
      template: aws-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsStandaloneCpCluster }}}
      credential: aws-credential
      dryRun: false
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
    Note that the `.spec.credential` value should match the `.metadata.name` value of a created `Credential` object.

4. Apply the Configuration

    Once the `ClusterDeployment` configuration is ready, apply it to the {{{ docsVersionInfo.k0rdentName }}} management cluster:

    ```bash
    kubectl apply -f clusterdeployment.yaml
    ```

    This step submits your deployment request to {{{ docsVersionInfo.k0rdentName }}}. If you've set `dryRun` to `true` you can observe what would happen. Otherwise, {{{ docsVersionInfo.k0rdentName }}} will go ahead and begin provisioning the necessary infrastructure.

5. Verify Deployment Status

    After submitting the configuration, verify that the `ClusterDeployment` object has been created successfully:

    ```bash
    kubectl -n <namespace> get clusterdeployment.kcm <cluster-name> -o=yaml
    ```

    The output shows the current status and any errors.

6. Monitor Provisioning

    {{{ docsVersionInfo.k0rdentName }}} will now start provisioning resources (for example, VMs and networks) and setting up the cluster. To monitor this process, run:

    ```bash
    kubectl -n <namespace> get cluster <cluster-name> -o=yaml
    ```

    > TIP:  
    > For a detailed view of the provisioning process, use the `clusterctl describe` command (note that this requires the [`clusterctl`](https://github.com/kubernetes-sigs/cluster-api/releases) CLI):

    ```bash
    clusterctl describe cluster <cluster-name> -n <namespace> --show-conditions all
    ```

7. Retrieve the Kubernetes Configuration

    When provisioning is complete, retrieve the kubeconfig file for the new cluster. This file enables you to interact with the cluster using `kubectl`:

    ```bash
    kubectl get secret -n <namespace> <cluster-name>-kubeconfig -o=jsonpath={.data.value} | base64 -d > kubeconfig
    ```
    You can then use this file to access the cluster, as in:

    ```bash
    export KUBECONFIG=kubeconfig
    kubectl get pods -A
    ```

    Store the kubeconfig file securely, as it contains authentication details for accessing the cluster.
