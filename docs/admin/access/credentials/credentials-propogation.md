# Cloud provider credentials propagation

Some components in the cluster deployment require cloud provider credentials to be
passed for proper functioning. For example, Cloud Controller Manager (CCM)
requires provider credentials to create load balancers and provide other
functionality.

This poses a challenge for credentials delivery. Currently `cloud-init` is used
to pass all necessary credentials, but this approach has several problems:

* Credentials are stored unencrypted in the instance metadata.
* Rotation of the credentials is impossible without complete instance
  redeployment.
* Possible leaks, since credentials are copied to several `Secret` objects
  related to bootstrap data.

To solve these problems in {{{ docsVersionInfo.k0rdentName }}} we're using the Sveltos controller, which can
render the CCM template with all necessary data from the CAPI provider resources (like
`ClusterIdentity`) and can create secrets directly on the cluster deployment.

> NOTE:
> CCM template examples can be found in `*-credentials.yaml` [here](https://github.com/k0rdent/kcm/tree/main/config/dev).
> Look for the `ConfigMap` object that has the `projectsveltos.io/template: "true"`
> annotation and `*-resource-template` as the object name.

This eliminates the need to pass anything credentials-related to `cloud-init`
and makes it possible to rotate credentials automatically without the need for
instance redeployment.

Also, this automation makes it possible to separate roles and responsibilities
so that only the lead engineer has access to credentials, and other engineers can
use them without seeing values and even any access to underlying
infrastructure platform.

The process is fully automated and credentials will be propagated automatically
within the `ClusterDeployment` reconciliation process; user only needs to provide
the correct `Credential` object.

## Provider-specific notes

Since this feature depends on the provider, it's important to review any provider-specific notes and clarifications.

> NOTE: 
> More detailed research notes can be found [here](https://github.com/k0rdent/kcm/issues/293).

### AWS

Since AWS uses roles, which are assigned to instances, no additional credentials
will be created.

The AWS provider supports 3 types of `ClusterIdentity` and, which one to use depends on
your specific use case. More information regarding CAPA `ClusterIdentity`
resources can be found in the [CRD Reference](https://cluster-api-aws.sigs.k8s.io/crd/).

### Azure

Currently the Cluster API Azure (CAPZ) provider creates `azure.json` `Secret` objects in the
same namespace as the `Cluster` object. By design they should be referenced in the
`cloud-init` YAML later during bootstrap process.

In {{{ docsVersionInfo.k0rdentName }}} these `Secret` objects aren't used and will not be added to the
`cloud-init`, but engineers can access them without restrictions, which is a security issue.

### OpenStack

For OpenStack, CAPO relies on a `clouds.yaml` file.
In {{{ docsVersionInfo.k0rdentName }}}, you provide this file in a Kubernetes `Secret` that references OpenStack credentials
(ideally application credentials for enhanced security). During reconciliation, KCM
automatically generates the cloud-config required by OpenStack’s cloud-controller-manager.

For more details, refer to the [KCM OpenStack Credential Propagation doc](https://github.com/k0rdent/kcm/blob/main/docs/dev.md#openstack).


### Adopted clusters

Credentials for adopted clusters consist of a secret containing a kubeconfig file to access the existing kubernetes cluster. 
The kubeconfig file for the cluster should be contained in the value key of the secret object. The following is an example of 
a secret that contains the kubeconfig for an adopted cluster. To create this secret, first create or obtain a kubeconfig file 
for the cluster that is being adopted and then run the following command to base64 encode it:

```shell
cat kubeconfig | base64 -w 0
```

Once you have obtained a base64 encoded kubeconfig file create a secret:

```yaml
apiVersion: v1
data:
  value: <base64 encoded kubeconfig file>
kind: Secret
metadata:
  name: adopted-cluster-kubeconf
  namespace: <namespace>
type: Opaque
```
## The Credential Distribution System

{{{ docsVersionInfo.k0rdentName }}} provides a mechanism to distribute `Credential` objects across namespaces using the
`AccessManagement` object. This object defines a set of `accessRules` that determine how credentials are distributed.

Each access rule specifies:

1. The target namespaces where credentials should be delivered.
2. A list of `Credential` names to distribute to those namespaces.

<!-- TODO show an example of the AccessManagement object. -->

The KCM controller copies the specified `Credential` objects from the `system` namespace to the target
namespaces based on the `accessRules` in the `AccessManagement` spec.

> INFO:
> Access rules can also include `Cluster` and `Service` Template Chains (`ClusterTemplateChain` objects and
> `ServiceTemplateChain` objects) to distribute templates to target namespaces.
> For more details, read: [Template Life Cycle Management](../../../reference/template/index.md).

### How to Configure Credential Distribution

To configure the distribution of `Credential` objects:

1. Edit the `AccessManagement` object.
2. Populate the `.spec.accessRules` field with the list of `Credential` names and the target namespaces.

Here’s an example configuration:

<!-- TODO show complete AccessManagement object. -->

```yaml
spec:
  accessRules:
  - targetNamespaces:
      list:
        - dev
        - test
    credentials:
      - aws-demo
      - azure-demo
```

In this example, the `aws-demo` and `azure-demo` `Credential` objects will be distributed to the `dev` and `test`
namespaces.


