# Upgrading and rolling back deployed services

## Service Version Upgrade

When you deploy a service to a cluster, you can specify a `ServiceTemplateChain` that will be used to define available upgrade path for the service. 

> INFO:
> Before you begin, make sure all templates you're going to add to `ServiceTemplateChain` exist in system namespace (normally `kcm-system`).
> Templates can be propagated to other namespaces using [Template Life Cycle Management](../../reference/template/index.md).

First, you need to create a `ServiceTemplateChain` object:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ServiceTemplateChain
metadata:
  name: ingress-nginx-chain
  namespace: kcm-system
spec:
  supportedTemplates:
    - name: ingress-nginx-4-11-3
      availableUpgrades:
      - name: ingress-nginx-4-11-5
    - name: ingress-nginx-4-11-5
```

This object defines a chain of templates that can be used to upgrade the service.

> WARNING:
> The `ServiceTemplateChain` has immutable spec. You can't change it after it's created.

After `ServiceTemplateChain` is created, you can use it in `ClusterDeployment` or `MutliClusterService` objects to define the available upgrade path for the service:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ClusterDeployment
metadata:
  name: my-cluster-deployment
  namespace: tenant42
spec:
  config:
    clusterLabels: {}
  template: aws-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsStandaloneCpCluster }}}
  credential: aws-credential
  serviceSpec:
    services:
      - template: ingress-nginx-4-11-3
        templateChain: ingress-nginx-chain
        name: ingress-nginx
        namespace: tenant42
    priority: 100
```

> WARNING:
> If no `templateChain` is specified for the service, the service cannot be upgraded because no path is availble.
> If you try to change the service template, in the logs, you'll see an error message such as:
>
> ```bash
> service ingress-nginx/ingress-nginx can't be upgraded from ingress-nginx-4-11-3 to ingress-nginx-4-11-5
> ```

After the `ClusterDeployment` or `MultiClusterService` has been reconciled, you will see available upgrade paths for the service in the status:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ClusterDeployment
metadata:
  name: my-cluster-deployment
  namespace: tenant42
spec:
  ...
status:
  servicesUpgradePaths:
    - name: ingress-nginx
      namespace: ingress-nginx
      template: ingress-nginx-4-11-3
      availableUpgrades:
        - upgradePaths:
            - ingress-nginx-4-11-5
```

The `.status.servicesUpgradePaths[]` array shows:
- `name`: Service name
- `namespace`: Service namespace
- `template`: Currently deployed ServiceTemplate
- `availableUpgrades[]`: Available upgrade options
  - `upgradePaths[]`: Array of ServiceTemplate names in the upgrade path

> NOTE:
> The upgrade paths are calculated from the ServiceTemplateChain. If multiple paths exist to reach the target template version, the shortest path is shown.

Now you can update the `ClusterDeployment` or `MultiClusterService` object to upgrade the service to the available version:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ClusterDeployment
metadata:
  name: my-cluster-deployment
  namespace: tenant42
spec:
  config:
    clusterLabels: {}
  template: aws-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsStandaloneCpCluster }}}
  credential: aws-credential
  serviceSpec:
    services:
      - template: ingress-nginx-4-11-5 # <-- upgrade to the latest version
        templateChain: ingress-nginx-chain
        name: ingress-nginx
        namespace: tenant42
    priority: 100
```

## Extending the Upgrade Path for New Releases

A `ServiceTemplateChain` only defines the upgrade paths known at the time it was created, and its spec is immutable, so you can't append a newly released `ServiceTemplate` to a chain that's already in use. Instead, create a new `ServiceTemplateChain` that starts from the currently deployed template and points to the new one, then switch the service over to that chain.

The following example walks a service through two consecutive upgrades. It uses a `MultiClusterService` that deploys `ingress-nginx` to the management cluster itself, but the same steps apply to a `ClusterDeployment` or to any set of clusters matched by a `MultiClusterService`.

Start with a chain that allows an upgrade from version 4.11.5 to 4.12.0:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ServiceTemplateChain
metadata:
  name: ingress-nginx-4-11-5-chain
  namespace: kcm-system
spec:
  supportedTemplates:
    - name: ingress-nginx-4-11-5
      availableUpgrades:
        - name: ingress-nginx-4-12-0
    - name: ingress-nginx-4-12-0
```

Then reference that chain from the service:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: MultiClusterService
metadata:
  name: mcs1
spec:
  serviceSpec:
    provider:
      selfManagement: true
    services:
      - name: nginx
        namespace: nginx
        template: ingress-nginx-4-11-5
        templateChain: ingress-nginx-4-11-5-chain
```

To perform the upgrade, change only the `template` field:

```yaml
    services:
      - name: nginx
        namespace: nginx
        template: ingress-nginx-4-12-0 # <-- upgrade to 4.12.0
        templateChain: ingress-nginx-4-11-5-chain
```

The upgrade rolls out without downtime: the new controller pod becomes ready before the previously running pod is terminated.

Command:

```bash
kubectl -n nginx get pod -w
```
```console { .no-copy }
NAME                                              READY   STATUS              RESTARTS   AGE
nginx-ingress-nginx-controller-69b985bfb8-6dzx7   1/1     Running             0          2m15s
nginx-ingress-nginx-admission-create-k9hpj        0/1     Pending             0          0s
nginx-ingress-nginx-admission-create-k9hpj        0/1     ContainerCreating   0          0s
nginx-ingress-nginx-admission-create-k9hpj        0/1     Completed           0          4s
nginx-ingress-nginx-controller-57b79899cd-x9572   0/1     Pending             0          0s
nginx-ingress-nginx-controller-57b79899cd-x9572   0/1     ContainerCreating   0          0s
nginx-ingress-nginx-admission-patch-c76b8         0/1     Pending             0          0s
nginx-ingress-nginx-admission-patch-c76b8         0/1     ContainerCreating   0          0s
nginx-ingress-nginx-admission-patch-c76b8         0/1     Completed           0          2s
nginx-ingress-nginx-controller-57b79899cd-x9572   0/1     Running             0          7s
nginx-ingress-nginx-controller-57b79899cd-x9572   1/1     Running             0          18s
nginx-ingress-nginx-controller-69b985bfb8-6dzx7   1/1     Terminating         0          3m4s
nginx-ingress-nginx-controller-69b985bfb8-6dzx7   0/1     Completed           0          3m15s
```

The service is now running 4.12.0, and `ingress-nginx-4-11-5-chain` offers no further upgrades. When version 4.13.0 is released, create a new chain that starts from the currently deployed 4.12.0 template:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ServiceTemplateChain
metadata:
  name: ingress-nginx-4-12-0-chain
  namespace: kcm-system
spec:
  supportedTemplates:
    - name: ingress-nginx-4-12-0
      availableUpgrades:
        - name: ingress-nginx-4-13-0
    - name: ingress-nginx-4-13-0
```

Then point the service at the new chain, leaving the `template` field unchanged:

```yaml
    services:
      - name: nginx
        namespace: nginx
        template: ingress-nginx-4-12-0
        templateChain: ingress-nginx-4-12-0-chain # <-- switch to the new chain
```

Because 4.12.0 is already deployed, switching the chain makes no changes on the cluster. It only makes the new upgrade path available, which you can confirm in `.status.servicesUpgradePaths`. From there, upgrade to 4.13.0 the same way as before, by setting `template: ingress-nginx-4-13-0`.

## Service Version Rollback

In general, the process of rolling back a service to the previous version is the same as upgrading the service in the first place. You'll need to create a separate `ServiceTemplateChain`, which defines the downgrade path:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ServiceTemplateChain
metadata:
  name: ingress-nginx-chain
  namespace: kcm-system
spec:
  supportedTemplates:
    - name: ingress-nginx-4-11-3
    - name: ingress-nginx-4-11-5
      availableUpgrades:
        - name: ingress-nginx-4-11-3
```

After the `ServiceTemplateChain` has been created, you can use it in a `ClusterDeployment` or `MutliClusterService` object to define the available rollback path for the service. Follow these steps:

1. Update the `ClusterDeployment` or `MultiClusterService` object with the rollback `ServiceTemplateChain`.
2. Wait for the `ClusterDeployment` or `MultiClusterService` to be reconciled.
3. Update the `ClusterDeployment` or `MultiClusterService` object with the previous version of the service.
