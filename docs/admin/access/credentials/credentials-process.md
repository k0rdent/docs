# The process

In order to pass credentials to k0rdent so it can take action, the following has to happen:

1. The lead platform engineer, or whoever has access to the actual provider credentials, creates a `Secret` that includes that information. For example, for an AWS cluster, it might look like this:

    ```yaml
    apiVersion: v1
    kind: Secret
    metadata:
        name: aws-cluster-identity-secret
        namespace: kcm-system
    type: Opaque
    stringData:
        AccessKeyID: EXAMPLE_ACCESS_KEY_ID
        SecretAccessKey: EXAMPLE_SECRET_ACCESS_KEY
    ```

    Once this secret is created, it can be referenced without the user having access to the content, and thus the actual credentials.

2. A provider-specific `ClusterIdentity` gets created. The `ClusterIdentity` references the `Secret` from step one. For example, for an AWS cluster, this object might look like this:

    ```yaml
    apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
    kind: AWSClusterStaticIdentity
    metadata:
      name: aws-cluster-identity
    spec:
      secretRef: aws-cluster-identity-secret
      allowedNamespaces:
        selector:
          matchLabels: {}
    ```

    Notice that it references the `aws-cluster-identity-secret` we created earlier. It also specifies the namespaces in which this `ClusterIdentity` can be used. (In this case there are no restrictions.)

2. Now you can create a `Credential` object that references the `ClusterIdentity`, thus making the credentials available and specifying the namespaces where it can be used. Continuing our AWS example:

    ```yaml
    apiVersion: k0rdent.mirantis.com/v1alpha1
    kind: Credential
    metadata:
      name: aws-cluster-credential
      namespace: kcm-system
    spec:
      description: "Credential Example"
      identityRef:
        apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
        kind: AWSClusterStaticIdentity
        name: aws-cluster-identity
    ```
    Notice that it references the previous `ClusterIdentity` (in this case an `AWSClusterStaticIdentity`). Also notice that you can use the `.spec.description` field to add additional text about the `Credential` so users can choose if multiple `Credential` objects are available.

3. Finally, when you create a `ClusterDeployment`, you reference the `Credential` object in order to enable k0rdent to pass that information to the infrastructure provider:

    ```yaml
    apiVersion: k0rdent.mirantis.com/v1alpha1
    kind: ClusterDeployment
    metadata:
        name: my-aws-clusterdeployment
      namespace: kcm-system
    spec:
      template: aws-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsStandaloneCpCluster }}}
      credential: aws-cluster-credential
        config:
        clusterLabels: {}
        region: us-east-2
        controlPlane:
        instanceType: t3.small
        worker:
        instanceType: t3.small
    ```

    As you can see, the user doesn't have to pass anything but the name of the `Credential` in order to deploy the cluster. So all an administrator has to do is add these `Credential`objects to the system and make them available. Note also that the `Credential` has to be available in the `ClusterDeployment`s namespace. (See [Cloud provider credentials propagation](./credentials-propogation.md) for more information on how that works. )
    
4. Optionally, certain credentials MAY be propagated to the `ClusterDeployment` after it is created.

    The following diagram illustrates the process:

    ```mermaid
    flowchart TD
      Step1["<b>Step 1</b> (Lead Engineer):<br/>Create ClusterIdentity and Secret objects where ClusterIdentity references Secret"]
      Step1 --> Step2["<b>Step 2</b> (Any Engineer):<br/>Create Credential object referencing ClusterIdentity"]
      Step2 --> Step3["<b>Step 3</b> (Any Engineer):<br/>Create ClusterDeployment referencing Credential object"]
      Step3 --> Step4["<b>Step 4</b> (Any Engineer):<br/>Apply ClusterDeployment, wait for provisioning & reconciliation, then propagate credentials to nodes if necessary"]
    ```

    By design steps 1 and 2 should be executed by the lead engineer who has
    access to the credentials. Thus credentials could be used by engineers
    without a need to have access to actual credentials or underlying resources,
    like `ClusterIdentity`.