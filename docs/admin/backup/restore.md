# Restoring From Backup

> NOTE:
> Please refer to the
> [official migration documentation](https://velero.io/docs/v1.17/migration-case/#before-migrating-your-cluster)
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
     --set regional.velero.initContainers[0].name=velero-plugin-for-<provider-name> \
     --set regional.velero.initContainers[0].image=velero/velero-plugin-for-<provider-name>:<provider-plugin-tag> \
     --set regional.velero.initContainers[0].volumeMounts[0].mountPath=/target \
     --set regional.velero.initContainers[0].volumeMounts[0].name=plugins
    ```

1. Create the `BackupStorageLocation`/`Secret` objects that were created during the [preparation stage](./prepare-backups.md)
   of creating a backup (preferably the same depending on a plugin).

1. If a k0rdent management cluster version is less than `1.2.0`, apply the workaround to avoid failure during the restoration.
   [Related known issue: Velero #9023](https://github.com/vmware-tanzu/velero/issues/9023).

    The fix is to "rename" the Velero deployment via the override:
    in the `Management` object, add to the path `spec.core.kcm.config.velero` a new key `fullnameOverride` with the value `velero`.

    Example of a patch if the path `spec.core.kcm.config.velero` does not yet exist:

    ```bash
    kubectl patch managements kcm \
      --type=json \
      -p='[{"op": "add", "path": "/spec/core/kcm/config/velero", "value": {"fullnameOverride": "velero"}}]'
    ```

    Example how it should look after the required change:

    ```yaml
    spec:
      core:
        kcm:
          config:
            velero:
              fullnameOverride: velero
    ```

    This ensures that the Velero `Deployment` name is exactly `velero`, which is a requirement due to the
    aforementioned known issue.

1. Restore the `kcm` system creating the [`Restore`](https://velero.io/docs/v1.17/api-types/restore/) object.
   Follow one of the case that is applicable to clusters' configuration in use:

    1. If there are **no** [regional clusters](../regional-clusters/index.md)
        or all regional clusters' infrastructure is healthy.

        Note that it is important to set the `.spec.existingResourcePolicy` field value to `update`.

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

    1. If one or more [regional clusters](../regional-clusters/index.md) require **reprovisioning**.

        The following listing will create a `ConfigMap` object along with
        the `Restore` object, and it allows `Velero` to set the
        pause annotation to all of `regions` objects.

        Substitute `<cluster-deployment-name>` with the corresponding
        names of `ClusterDeployment` objects used for provisioning
        of the corresponding region cluster.

        Note that it is important to set the `.spec.existingResourcePolicy` field value to `update`.

        ```yaml
        ---
        apiVersion: v1
        kind: ConfigMap
        metadata:
          name: add-region-pause-anno
          namespace: kcm-system
        data:
          add-region-pause-anno: |
            version: v1
            resourceModifierRules:
            - conditions:
                groupResource: regions.k0rdent.mirantis.com
              mergePatches:
              - patchData: |
                  {
                    "metadata": {
                      "annotations": {
                        "k0rdent.mirantis.com/region-pause": "true"
                      }
                    }
                  }
        ---
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
          labelSelector:
            matchExpressions:
              - key: cluster.x-k8s.io/cluster-name
                operator: NotIn
                values: ["<cluster-deployment-name>"]
              # Add new entries accordingly if more regional clusters require reprovisioning
              # - key: cluster.x-k8s.io/cluster-name
              #   operator: NotIn
              #   values: ["<cluster-deployment-name>"]
          resourceModifier:
            kind: ConfigMap
            name: add-region-pause-anno
        ```

1. Wait until the `Restore` status is `Completed` and all `kcm` components are up and running.

1. If there were one or more [regional clusters](../regional-clusters/index.md)
   that required reprovisioning, then:

    1. On the management cluster, wait for the `regions` object readiness:

        ```sh
        kubectl wait regions kcm --for=condition=Ready=True --timeout 30m
        ```

    1. Manually ensure that the freshly reprovisioned regional cluster
        runs and is accessable.

    1. On the **regional** cluster, repeat the second step, creating the
        `BackupStorageLocation`/`Secret` objects that were created during
        the [preparation stage](./prepare-backups.md).

    1. On the **regional** cluster, restore the cluster by creating a new
        [`Restore`](https://velero.io/docs/v1.17/api-types/restore/) object:

        Note that in this case the `.spec.existingResourcePolicy` field is **not set**.

        ```yaml
        apiVersion: velero.io/v1
        kind: Restore
        metadata:
          name: <restore-name>
          namespace: kcm-system
        spec:
          backupName: <region-name>-<backup-name>
          excludedResources:
          - mutatingwebhookconfiguration.admissionregistration.k8s.io
          - validatingwebhookconfiguration.admissionregistration.k8s.io
          includedNamespaces:
          - '*'
        ```

    1. On the **regional** cluster, wait until the `Restore`
        status is `Completed` and all `ClusterDeployment` objects are ready.

    1. On the management cluster, unpause provisioning of
        regional `ClusterDeployment` objects by removing annotation
        from the `regions` object:

        ```sh
        kubectl annotate regions <region-name> 'k0rdent.mirantis.com/region-pause-'
        ```

## Caveats

For some CAPI providers it is necessary to make changes to the `Restore`
object due to the large number of different resources and logic in each provider.
The resources described below are not excluded from a `ManagementBackup` by
default to avoid logical dependencies on one or another provider, and to create a provider-agnostic system.

> NOTE:
> The described caveats apply only to the `Restore`
> object creation step and do not affect the other steps.

> NOTE:
> The below mentioned exclusions (`excludedResources`)
> are applicable to any of the `Restore` examples on
> this page, including those tailored for [regional clusters](../regional-clusters/index.md).

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

Due to the [Velero Restoration Order](https://velero.io/docs/v1.17/restore-reference/#restore-order),
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
