# Creating a Credential in a Region

Once a `Region` is deployed and ready, you can proceed with `Credential` configuration.

Credentials are required for {{{ docsVersionInfo.k0rdentName }}} to communicate with the infrastructure provider
(such as AWS, Azure, vSphere, and so on). They enable provisioning of resources such as virtual machines, networking components,
and storage.

The `Credential` `spec` has been extended with a `region` field, which specifies the name of the `Region` object in which the `Credential`
applies. This is the only place where the region is configured. When `spec.region` is set, any `ClusterDeployment`
referencing this Credential will be deployed to the corresponding regional cluster.

> NOTE:
> Each `Credential` maps 1:1 to a Region. If `spec.region` is empty, the `Credential` is tied to the management cluster
> and deployment will proceed as though there are no regional clusters.

## Creating Cluster Identity objects

> WARNING:
> Starting from {{{ docsVersionInfo.k0rdentName }}} v1.5.0 the ClusterIdentity resources for regional Credential
> are synced with the regional cluster. Which means, when the regional Credential object references some
> ClusterIdentity as `identityRef` (for example `AWSClusterStaticIdentity`) this identity object and all referenced
> objects (for example, `Secrets`) will be copied from the management to the regional cluster. To get more information
> follow [Regional Credential Distribution](../access/credentials/credentials-propagation.md#regional-credential-distribution).
>
> Before {{{ docsVersionInfo.k0rdentName }}} v1.5.0 you should manually create `ClusterIdentity` resources
> for regional Credential in the **regional** cluster, and **not the management cluster**.
>
> This does not apply to the resource template `ConfigMap` which should be manually created in the **regional**
> cluster.

Depending on the provider, you need to create `ClusterIdentity` resources to allow provider components to interact
with the cloud.

### Example: AWS

1. Create the `Secret` with your AWS cloud credential

    Create a YAML file called `aws-cluster-identity-secret.yaml` and add the following text, replacing the
`EXAMPLE_ACCESS_KEY_ID` and `EXAMPLE_SECRET_ACCESS_KEY` with corresponding cloud values:

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

    ```bash
    kubectl apply -f aws-cluster-identity-secret.yaml -n kcm-system --kubeconfig <path-to-management-cluster-kubeconfig>
    ```

2. Create the `AWSClusterStaticIdentity`

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

   Apply the YAML to your management cluster:

   ```bash
   kubectl apply -f aws-cluster-identity.yaml --kubeconfig <path-to-management-cluster-kubeconfig>
   ```

3. Create the `ClusterIdentity` resource template `ConfigMap` in the regional cluster

> WARNING:
> Create `ClusterIdentity` resource template `ConfigMap` in the **regional** cluster, and
> **not the management cluster**.

   Now we create `ClusterIdentity` resource template `ConfigMap`. As in prior steps, create a YAML file called `aws-cluster-identity-resource-template.yaml`:

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

   Note that `ConfigMap` is empty. This is expected as we don't need to template any objects inside child cluster(s) for now, but we can use that object in the future if need arises.

   Apply the YAML to your regional cluster:

   ```bash
   kubectl apply -f aws-cluster-identity-resource-template.yaml -n kcm-system --kubeconfig <path-to-regional-cluster-kubeconfig>
   ```

## Creating the Credential

> WARNING:
> The `Credential` should be created in the **management cluster** and **not the regional cluster**

After configuring the `ClusterIdentity` objects in the regional cluster, create the `Credential` in the management cluster, referencing that
`ClusterIdentity`.

For AWS, the `Credential` should be created in the same namespace as the previously created `ClusterIdentity` objects.
The `spec.region` should be configured and refer the name of the `Region` object that points to the cluster where the
`ClusterIdentity` resources have been created:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: Credential
metadata:
  name: aws-cluster-identity-cred
  namespace: kcm-system
spec:
  region: region1
  description: Credential for child clusters of region1
  identityRef:
    apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
    kind: AWSClusterStaticIdentity
    name: aws-cluster-identity
```

Apply the YAML to your management cluster:

```bash
kubectl apply -f aws-cluster-identity-cred.yaml -n kcm-system
```

## Verifying Credential Status

After creation, the `Credential` is validated and its status will reflect readiness. To ensure the `Credential` is
ready, run:

```bash
kubectl get credential -n kcm-system aws-cluster-identity-cred
```

and check the `READY` column.

For the detailed information about Credential readiness, run:

```bash
kubectl get credential -n kcm-system aws-cluster-identity-cred -o=yaml
```

Example of an error status:

```yaml
status:
  conditions:
  - lastTransitionTime: "2025-09-26T10:15:17Z"
    type: CredentialReady
    status: "False"
    reason: Failed
    message: "Failed to get ClusterIdentity object of Kind=AWSClusterStaticIdentity
      /aws-cluster-identity: unable to retrieve the complete list of server APIs:
      infrastructure.cluster.x-k8s.io/v1beta2: no matches for infrastructure.cluster.x-k8s.io/v1beta2,
      Resource="
   ready: false
```

This usually indicates that either the provider is not enabled in the specified `Region`, or provider deployment failed.
Double-check the `Region` spec for the required provider's presence and status for any issues.

Example of a ready status:

```yaml
status:
  conditions:
  - lastTransitionTime: "2025-09-26T11:15:57Z"
    message: Credential is ready
    observedGeneration: 1
    reason: Succeeded
    status: "True"
    type: CredentialReady
  ready: true
```

To get more details about Credential usage, follow the instructions in the [Credential System](../access/credentials/index.md).
For other providers, see the specific credential setup instructions for your
[target infrastructure](../installation/prepare-mgmt-cluster/index.md).

Once the `Credential` is ready, you can proceed with [Deploying Clusters in Region](deploying-clusters-in-region.md).
