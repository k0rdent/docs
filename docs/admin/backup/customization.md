# Customization

This section covers different topics of customization regarding backing up and restoring {{{ docsVersionInfo.k0rdentName }}}.

## Velero installation

The [Velero helm chart](https://vmware-tanzu.github.io/helm-charts/) is supplied with the
{{{ docsVersionInfo.k0rdentName }}} helm chart and is enabled by default. There are 2 ways of customizing the chart values:

1. Install using `helm` and add corresponding parameters to the `helm install` command.

    > NOTE:
    > Only a plugin that [supports Object Store](https://velero.io/docs/v1.15/supported-providers/)
    > is required during restoration; the other parameters are optional.

    For example, this command installs {{{ docsVersionInfo.k0rdentName }}} via `helm install` with a configured plugin, `BackupStorageLocation`
    and propagated credentials:

    ```bash
    helm install kcm {{{ extra.docsVersionInfo.ociRegistry }}} \
     --version <version> \
     --create-namespace \
     --namespace kcm-system \
     --set-file velero.credentials.secretContents.cloud=<full-path-to-file> \
     --set velero.credentials.useSecret=true \
     --set velero.backupsEnabled=true \
     --set velero.configuration.backupStorageLocation[0].name=<backup-storage-location-name> \
     --set velero.configuration.backupStorageLocation[0].provider=<provider-name> \
     --set velero.configuration.backupStorageLocation[0].bucket=<bucket-name> \
     --set velero.configuration.backupStorageLocation[0].config.region=<region> \
     --set velero.initContainers[0].name=velero-plugin-for-<provider-name> \
     --set velero.initContainers[0].image=velero/velero-plugin-for-<provider-name>:<provider-plugin-tag> \
     --set velero.initContainers[0].volumeMounts[0].mountPath=/target \
     --set velero.initContainers[0].volumeMounts[0].name=plugins
    ```

1. Create or modify the existing `Management` object in the `.spec.config.kcm`.

    > NOTE:
    > Only a plugin that [supports Object Store](https://velero.io/docs/v1.15/supported-providers/)
    > is required during restoration; the other parameters are optional.

    For example, this is a `Management` object with a configured plugin and enabled metrics:

    ```yaml
    apiVersion: k0rdent.mirantis.com/v1beta1
    kind: Management
    metadata:
      name: kcm
    spec:
      # ...
      core:
        kcm:
          config:
            velero:
              initContainers:
              - name: velero-plugin-for-<provider-name>
                image: velero/velero-plugin-for-<provider-name>:<provider-plugin-tag>
                imagePullPolicy: IfNotPresent
                volumeMounts:
                - mountPath: /target
                  name: plugins
              metrics:
                enabled: true
      # ...
    ```

To fully disable `velero`, set the `velero.enabled` parameter to `false`.

## Schedule Expression Format

The `ManagementBackup` `.spec.schedule` field accepts a correct
[Cron](https://en.wikipedia.org/wiki/Cron) expression,
along with the
[nonstandard predefined scheduling definitions](https://en.wikipedia.org/wiki/Cron#Nonstandard_predefined_scheduling_definitions)
and an extra definition `@every` with a number and a valid time unit
(valid time units are `ns`, `us` (or `µs`), `ms`, `s`, `m`, `h`).

The following list contains acceptable `.spec.schedule` example values:

* `0 */1 * * *` (standard Cron expression)
* `@hourly` (nonstandard predefined definition)
* `@every 1h` (extra definition)

## Putting Extra Objects in a Management Backup

If you need to back up objects other than those [backed up by default](./whats-included.md),
you can add the label `k0rdent.mirantis.com/component="kcm"` to these objects.

All objects containing the label will be automatically added to the management backup.
