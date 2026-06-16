# Updating a Single Standalone Cluster

{{{ docsVersionInfo.k0rdentName }}} `ClusterTemplate` objects are immutable, so the only way to change a `ClusterDeployment` is to change the template
that forms its basis. 

To update the `ClusterDeployment`, modify the `.spec.template` field to use the name of the new `ClusterTemplate`. 
This enables you to apply changes to the cluster configuration. These changes will then be applied to the actual 
cluster. For example, if the cluster currently uses `t2.large` instances, that will be specified in its current template. 
To change the cluster to use `t2.xlarge` instances, you would simply apply a template that references that new size; 
{{{ docsVersionInfo.k0rdentName }}} will then realize the cluster is out of sync and will attempt to remedy the situation by updating the cluster.

Follow these steps to update the `ClusterDeployment`:

1. Patch the `ClusterDeployment` with the new template

    Run the following command, replacing the placeholders with the appropriate values:

    ```bash
    kubectl patch clusterdeployment.kcm <cluster-name> -n <namespace> --patch '{"spec":{"template":"<new-template-name>"}}' --type=merge
    ```

2. Check the status of the `ClusterDeployment`

    After applying the patch, verify the status of the `ClusterDeployment` object:

    ```bash
    kubectl get clusterdeployment.kcm <cluster-name> -n <namespace>
    ```

3. Inspect the detailed status

    For more details, use the `-o=yaml` option to check the `.status.conditions` field:

    ```bash
    kubectl get clusterdeployment.kcm <cluster-name> -n <namespace> -o=yaml
    ```

Note that not all updates are possible; `ClusterTemplateChain` objects limit what templates can be applied.  Consider,
for example, this `ClusterTemplateChain`:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ClusterTemplateChain
metadata:
  name: aws-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsStandaloneCpCluster }}}
  namespace: kcm-system
spec:
  supportedTemplates:
    - name: aws-standalone-cp-0-0-2
      availableUpgrades:
        - name: aws-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsStandaloneCpCluster }}}
    - name: aws-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsStandaloneCpCluster }}}
```

As you can see from the `.spec`, the `aws-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsStandaloneCpCluster }}}` template can be applied to a cluster that also uses
the `aws-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsStandaloneCpCluster }}}` template, or it can be used as an upgrade from a cluster that uses `aws-standalone-cp-0.0.2`.
You wouldn't be able to use this template to update a cluster that uses any other `ClusterTemplate`.

Similarly, the `AccessManagement` object must have properly configured `spec.accessRules` with a list of allowed 
`ClusterTemplateChain` object names and their namespaces. For more information, see [Template Life Cycle Management](../../reference/template/index.md#template-life-cycle-management).

> NOTE:  
> Support for displaying all available Cluster Templates for updates in the `ClusterDeployment` status is planned.

      <!-- TODO
      ## Scaling a Cluster 
      ## Upgrading a Single Standalone Cluster 
      -->

# Control Plane Machines Rollout

Certain cluster configuration changes trigger an automatic rollout of control plane machines. For example, updating the
[ClusterAuditPolicy](cluster-audit-policy.md) or [ClusterAuthentication](cluster-iam-setup.md) reference in the
`ClusterDeployment` spec initiates a control plane rollout.

There is a known issue that can affect clusters initially deployed with a single control plane node. During
the rollout, `etcd` may become unavailable if the cluster temporarily loses quorum. This can occur when
the departing control plane node is removed before quorum is safely maintained, preventing the cluster from scaling
below the quorum threshold (for example, from two control plane nodes to one).

To avoid issues, {{{ docsVersionInfo.k0rdentName }}} recommends:

1. Scaling the control plane to at least three nodes before applying any configuration changes that triggers a rollout.
Once the rollout has completed successfully, you can scale the control plane back down if desired.
1. Don't attempt to make configuration changes that would trigger another rollout until the current one has completed.
You can check the status of the rollout by inspecting the `ClusterDeployment` conditions.

This issue is expected to be resolved in future k0s releases.
