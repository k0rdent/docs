# Upgrades and rollbacks

The Disaster Recovery Feature provides a way to create backups
on each `kcm` upgrade automatically.

## Automatic Management Backups

Each `ManagementBackup` with a *non-empty* `.spec.schedule` field
can enable the automatic creation of backups before
[upgrading](../upgrade/admin-upgrading-k0rdent.md) to a new version.

To enable, set the `.spec.performOnManagementUpgrade` to `true`.

For example, a `ManagementBackup` object with enabled auto-backup before the `kcm` version upgrade looks like this:

```yaml
apiVersion: k0rdent.mirantis.com/v1alpha1
kind: ManagementBackup
metadata:
  name: example-backup
spec:
  schedule: "0 */6 * * *"
  performOnManagementUpgrade: true
```

After the enablement, before each upgrade of `kcm` to a new version,
a new backup will be created.

Automatically created backups have the
following name template to make it easier to find them:
the name of the `ManagementBackup` object with enabled `performOnManagementUpgrade`
concatenates with the name of the release before the upgrade,
for example, `example-backup-kcm-{{{ extra.docsVersionInfo.k0rdentVersion }}}`.

Automatically created backups have the label `k0rdent.mirantis.com/release-backup`
with the name of the release before the upgrade as its value
to simplify querying if required.

## Rollbacks

If during the `kcm` upgrade a failure happens, a rollback operation
should be performed to restore the `kcm` to its before-the-upgrade state:

1. Follow the first 2 steps from the [restoration section](./restore.md), creating a clean `kcm`
   installation and `BackupStorageLocation`/`Secret`.

    > WARNING:
    > Please consider the [restoration caveats](./caveats.md) section before proceeding.

1. Create the `ConfigMap` object with patches to revert the `Management`
   `.spec.release`, substitute the `<version-before-upgrade>` with
   the version of `kcm` before the upgrade, and create the `Restore` object,
   propagating the `ConfigMap` to it:

    ```yaml
    ---
    apiVersion: v1
    data:
      patch-mgmt-spec-release: |
        version: v1
        resourceModifierRules:
        - conditions:
            groupResource: managements.k0rdent.mirantis.com
          patches:
          - operation: replace
            path: "/spec/release"
            value: "<version-before-upgrade>"
    kind: ConfigMap
    metadata:
      name: patch-mgmt-spec-release
      namespace: kcm-system
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
      resourceModifier: # propagate patches
        kind: ConfigMap
        name: patch-mgmt-spec-release
    ```

1. Wait until the `Restore` status is `Completed` and all `kcm` components are up and running.
1. Optionally delete the created `ConfigMap`.

