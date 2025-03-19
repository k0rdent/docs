# Adopting an Existing Cluster

Creating a new cluster isn't the only way to use {{{ docsVersionInfo.k0rdentName }}}. Adopting an existing Kubernetes cluster enables you to 
bring it under {{{ docsVersionInfo.k0rdentName }}}'s management. This process is useful when you already have a running cluster but want 
to centralize management and leverage {{{ docsVersionInfo.k0rdentName }}}'s capabilities, such as unified monitoring, configuration, and automation,
but you don't want to redeploy your cluster.

## Adopting a Cluster

To adopt a cluster, {{{ docsVersionInfo.k0rdentName }}} establishes communication between the management cluster (where kcm is installed) 
and the target cluster. This requires proper credentials, network connectivity, and a standardized configuration. 

Follow these steps to adopt an existing cluster:

1. Prerequisites

    Before you start, make sure you have the following:

    - A kubeconfig file for the cluster you want to adopt (this file provides access credentials and configuration details 
      for the cluster).
    - A management cluster with {{{ docsVersionInfo.k0rdentName }}} installed and running. See the [installation instructions](../installation/index.md) 
      if you need to set it up.
    - Network connectivity between the management cluster and the cluster to be adopted (for example, ensure firewall 
      rules and VPNs allow communication).

2.  Create a Credential

    Start by creating a `Credential` object that includes all required authentication details for your chosen infrastructure 
    provider. Follow the instructions in the [Credential System](../access/credentials/index.md), as well as the specific instructions 
    for your [target infrastructure](../installation/prepare-mgmt-cluster/index.md).

    > TIP:  
    > Double-check that your credentials have sufficient permissions to create resources on the target infrastructure.

3. Configure the management cluster kubeconfig

    Set the `KUBECONFIG` environment variable to the path of your management cluster's kubeconfig file so you can 
    execute commands against the management cluster.

    For example:

    ```shell
    export KUBECONFIG=/path/to/management-cluster-kubeconfig
    ```

4. Create the `ClusterDeployment` YAML Configuration

    The `ClusterDeployment` object is used to define how {{{ docsVersionInfo.k0rdentName }}} should manage the adopted cluster. Create a 
    YAML file for the `ClusterDeployment` object, as shown below:

    ```yaml
    apiVersion: k0rdent.mirantis.com/v1alpha1
    kind: ClusterDeployment
    metadata:
      name: <CLUSTER_NAME>
      namespace: <NAMESPACE>
    spec:
      template: adopted-cluster-<VERSION>
      credential: <CREDENTIAL_NAME>
      dryRun: <BOOLEAN>
      config:
        <CONFIGURATION>
    ```

    Replace placeholders such as `<CLUSTER_NAME>`, `<NAMESPACE>`, `<VERSION>`, `<CREDENTIAL_NAME>`, and `<CONFIGURATION>` with actual values. The `dryRun` flag is useful for testing the configuration without making changes to the cluster. For more details, see the [Dry Run](../../appendix/appendix-dryrun.md) section.

    You can also get a list of the available templates with:

    ```shell
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
    openstack-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.openstackStandaloneCpCluster }}}   true
    vsphere-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.vsphereHostedCpCluster }}}         true
    vsphere-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.vsphereStandaloneCpCluster }}}     true
    ```

    Putting it all together, your YAML would look something like this:

    ```yaml
    apiVersion: k0rdent.mirantis.com/v1alpha1
    kind: ClusterDeployment
    metadata:
      name: my-cluster
      namespace: kcm-system
    spec:
      template: adopted-cluster-{{{ extra.docsVersionInfo.k0rdentVersion }}}
      credential: my-cluster-credential
      dryRun: false
      config: {}
    ```

5. Apply the `ClusterDeployment` configuration

    Once your configuration file is ready, apply it to the management cluster using `kubectl`:

    ```shell
    kubectl apply -f clusterdeployment.yaml
    ```

    This step submits the `ClusterDeployment` object to {{{ docsVersionInfo.k0rdentName }}}, initiating the adoption process.

6. Check the Status of the `ClusterDeployment` Object

    To ensure the adoption process is progressing as expected, check the status of the `ClusterDeployment` object:

    ```shell
    kubectl -n <namespace> get clusterdeployment.kcm <cluster-name> -o=yaml
    ```

    The output includes the current state and any conditions (for example, errors or progress updates). Review 
    this information to confirm that the adoption is successful.

## What's Happening Behind the Scenes?

When you adopt a cluster, {{{ docsVersionInfo.k0rdentName }}} performs several actions:
1. It validates the credentials and configuration provided in the `ClusterDeployment` object.
2. It ensures network connectivity between the management cluster and the adopted cluster.
3. It registers the adopted cluster within the {{{ docsVersionInfo.k0rdentName }}} system, enabling it to be monitored and managed like 
    any k0rdent-deployed cluster.

This process doesn't change the adopted cluster's existing workloads or configurations. Instead, it enhances your 
ability to manage the cluster through {{{ docsVersionInfo.k0rdentName }}}.

## Additional Tips
- If you encounter issues, double-check that kubeconfig file you used for the adopted cluster is valid 
  and matches the cluster you're trying to adopt.
- Use the [`dryRun`](../../appendix/appendix-dryrun.md) option during the first attempt to validate the configuration without making actual changes.