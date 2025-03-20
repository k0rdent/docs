# Scheduled Management Backups

Backups should be scheduled on a regular basis, depending on how often information changes.

## Preparation

Before you create a scheduled backup, you need to perform a few preparatory steps:

1. If no `velero` plugins have been installed as suggested
   in [Velero installation](customization.md#velero-installation),
   install a plugin that [supports Object Store](https://velero.io/docs/v1.15/supported-providers/)
   by modifying the `Management` object:

    ```yaml
    apiVersion: k0rdent.mirantis.com/v1alpha1
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
      # ...
    ```

1. Prepare a cloud storage location, such as an Amazon S3 bucket, to which to save backups.

1. Create a [`BackupStorageLocation`](https://velero.io/docs/v1.15/api-types/backupstoragelocation/)
   object referencing a `Secret` with credentials to access the cloud storage
   (if the multiple credentials feature is supported by the plugin).

    For example, if you are using Amazon S3, your `BackupStorageLocation` and the related `Secret` might look like this:

    ```yaml
    ---
    apiVersion: v1
    data:
      # base64-encoded credentials for Amazon S3 in the following format:
      # [default]
      # aws_access_key_id = EXAMPLE_ACCESS_KEY_ID
      # aws_secret_access_key = EXAMPLE_SECRET_ACCESS_KEY
      cloud: WW2RlZmF1bHRdCmF3c19hY2Nlc3Nfa2V5X2lkID0gRVhBTVBMRV9BQ0NFU1NfS0VZX0lECmF3c19zZWNyZXRfYWNjZXNzX2tleSA9IEVYQU1QTEVfU0VDUkVUX0FDQ0VTU19LRVkKICA=
    kind: Secret
    metadata:
      name: cloud-credentials
      namespace: kcm-system
    type: Opaque
    ---
    apiVersion: velero.io/v1
    kind: BackupStorageLocation
    metadata:
      name: aws-s3
      namespace: kcm-system
    spec:
      config:
        region: <your-region-name>
      default: true # optional, if not set, then storage location name must always be set in ManagementBackup
      objectStorage:
        bucket: <your-bucket-name>
      provider: aws
      backupSyncPeriod: 1m
      credential:
        name: cloud-credentials
        key: cloud
    ```

You can get more information on how to build these objects at the [official Velero documentation](https://velero.io/docs/v1.15/locations).

## Create a Management Backup

Periodic backups are handled by a `ManagementBackup` object, which uses a [Cron](https://en.wikipedia.org/wiki/Cron) expression
for its `.spec.schedule` field.
If the `.spec.schedule` field is not set, a [backup on demand](./ondemand-backups.md#management-backup-on-demand) will be created instead.

Optionally, set the name of the `BackupStorageLocation` `.spec.backup.storageLocation`.
The default location is the `BackupStorageLocation` object with `.spec.default` set to `true`.

For example, you can create a `ManagementBackup` object that backs up to the storage object created in the previous step
at minute 0 past every 6th hour would look like this:

```yaml
apiVersion: k0rdent.mirantis.com/v1alpha1
kind: ManagementBackup
metadata:
  name: kcm
spec:
  schedule: "0 */6 * * *"
  storageLocation: aws-s3
```
