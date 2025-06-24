# Restoring From Backup

> NOTE:
> Please refer to the
> [official migration documentation](https://velero.io/docs/v1.15/migration-case/#before-migrating-your-cluster)
> to familiarize yourself with potential limitations of the Velero backup system.

In the event of disaster, you can restore from a backup by doing the following:

1. Create a clean {{{ docsVersionInfo.k0rdentName }}} installation, including `velero` and [its plugins](./customization.md#velero-installation).
   Specifically, you want to **avoid** creating a `Management` object and similar objects because they
   will be part of your restored cluster. You can remove these objects after installation, but you
   can also install {{{ docsVersionInfo.k0rdentName }}} without them in the first place:

    ```bash
    helm install kcm {{{ extra.docsVersionInfo.ociRegistry }}} \
     --version <version> \
     --create-namespace \
     --namespace kcm-system \
     --set controller.createManagement=false \
     --set controller.createAccessManagement=false \
     --set controller.createRelease=false \
     --set controller.createTemplates=false \
     --set velero.initContainers[0].name=velero-plugin-for-<provider-name> \
     --set velero.initContainers[0].image=velero/velero-plugin-for-<provider-name>:<provider-plugin-tag> \
     --set velero.initContainers[0].volumeMounts[0].mountPath=/target \
     --set velero.initContainers[0].volumeMounts[0].name=plugins
    ```

1. Create the `BackupStorageLocation`/`Secret` objects that were created during the [preparation stage](./prepare-backups.md)
   of creating a backup (preferably the same depending on a plugin).

1. Restore the `kcm` system creating the [`Restore`](https://velero.io/docs/v1.15/api-types/restore/) object.
   Note that it is important to set the `.spec.existingResourcePolicy` field value to `update`:

    ```yaml
    apiVersion: velero.io/v1
    kind: Restore
    metadata:
      name: <restore-name>
      namespace: kcm-system
    spec:
      backupName: <backup-name>
      existingResourcePolicy: update
      includedNamespaces:
      - '*'
    ```

1. Wait until the `Restore` status is `Completed` and all `kcm` components are up and running.

## If the Restore fails

At the time of this writing, there is a mis-match between what {{{ docsVersionInfo.k0rdentName }}} expects 
   and the objects `velero` provides, which may result in a `PartiallyFailed` result. A fix for this problem 
   is coming soon, but in the meantime, you will need to rename the `kcm-velero` `Deployment` to `velero`.  
   
   Follow these steps:

1. Export the YAML for the object, then delete it:

    ```shell
    kubectl -n kcm-system get deployment kcm-velero -o yaml > velero-deployment.yaml
    kubectl delete -n kcm-system deployment kcm-velero
    ```
    ```console
    deployment.apps "kcm-velero" deleted
    ```

2. Edit the `velero-deployment.yaml` file to change `metadata.name` from `kcm-velero` to `velero`:

    ```yaml
    ...
        component: velero
        helm.sh/chart: velero-9.1.2
      name: velero
      namespace: kcm-system
      resourceVersion: "1653"
    ...
    ```

3. Recreate the `Deployment` with the new name:

    ```shell
    kubectl apply -n kcm-system -f velero-deployment.yaml
    ```
    ```console
    deployment.apps/velero created
    ```
    
4. Delete the failed `Restore`:

    ```shell
    kubectl delete restore -n <your-namespace> <restore-name>
    ```

5. Recreate the `Restore` object as before. It should now complete successfully.

## Caveats

For some CAPI providers it is necessary to make changes to the `Restore`
object due to the large number of different resources and logic in each provider.
The resources described below are not excluded from a `ManagementBackup` by
default to avoid logical dependencies on one or another provider, and to create a provider-agnostic system.

> NOTE:
> The described caveats apply only to the `Restore`
> object creation step and do not affect the other steps.

### Azure (CAPZ)

The following resources should be excluded from the `Restore` object:

* `natgateways.network.azure.com`
* `resourcegroups.resources.azure.com`
* `virtualnetworks.network.azure.com`
* `virtualnetworkssubnets.network.azure.com`

Due to the [webhook conversion](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning/#webhook-conversion),
objects of these resources cannot be restored, and they will
be created in the management cluster by the `CAPZ` provider
automatically with the same `spec` as in the backup.

The resulting `Restore` object:

```yaml
apiVersion: velero.io/v1
kind: Restore
metadata:
  name: <restore-name>
  namespace: kcm-system
spec:
  backupName: <backup-name>
  existingResourcePolicy: update
  excludedResources:
  - natgateways.network.azure.com
  - resourcegroups.resources.azure.com
  - virtualnetworks.network.azure.com
  - virtualnetworkssubnets.network.azure.com
  includedNamespaces:
  - '*'
```

### vSphere (CAPV)

The following resources should be excluded from the `Restore` object:

* `mutatingwebhookconfiguration.admissionregistration.k8s.io`
* `validatingwebhookconfiguration.admissionregistration.k8s.io`

Due to the [Velero Restoration Order](https://velero.io/docs/v1.15/restore-reference/#restore-order),
some of the `CAPV` core objects cannot be restored,
and they will not be recreated automatically.
Because all of the objects have already passed both mutations
and validations, there is not much sense in validating them again.
The webhook configurations will be restored during installation
of the `CAPV` provider.

The resulting `Restore` object:

```yaml
apiVersion: velero.io/v1
kind: Restore
metadata:
  name: <restore-name>
  namespace: kcm-system
spec:
  backupName: <backup-name>
  existingResourcePolicy: update
  excludedResources:
  - mutatingwebhookconfiguration.admissionregistration.k8s.io
  - validatingwebhookconfiguration.admissionregistration.k8s.io
  includedNamespaces:
  - '*'
```
