# Caveats / Limitations

The credentials stored in backups can and will get stale,
so a proper rotation should be considered beforehand.

Only plugins that [support Object Store](https://velero.io/docs/v1.15/supported-providers/)
can be used to store backups into an object storage.

All `velero` caveats and limitations are transitively implied in {{{ docsVersionInfo.k0rdentName }}}. In particular, that
means no backup encryption is provided until it is implemented by a `velero` plugin that supports
encryption and cloud storage backups.

## Velero Backups / Restores deletion

### Delete Restores

To delete a `velero` `Restore` from the management cluster
**and** from cloud storage, delete `restores.velero.io` object(s),
such as with the following command:

```bash
kubectl delete restores.velero.io -n kcm-system <restore-name>
```

> WARNING:
> Deletion of a `Restore` object deletes it from both
> the management cluster and from cloud storage.

### Delete Backups

To remove a `velero` `Backup` from the management cluster,
delete `backups.velero.io` object(s), such as with the following command:

```bash
kubectl delete backups.velero.io -n kcm-system <velero-backup-name>
```

> HINT:
> The command above only removes objects from
> the cluster; the data continues to persist
> on the cloud storage.
>
> The deleted object will be recreated in the
> cluster if its `BackupStorageLocation` `.spec.backupSyncPeriod`
> is set and does not equal `0`.

To delete a `velero` `Backup` from the management cluster
**and** from cloud storage, create the following `DeleteBackupRequest` object:

```yaml
apiVersion: velero.io/v1
kind: DeleteBackupRequest
metadata:
  name: delete-backup-completely
  namespace: kcm-system
spec:
  backupName: <velero-backup>
```

> WARNING:
> Deletion of a `Backup` object via the `DeleteBackupRequest`
> deletes it from both
> the management cluster and from the cloud storage.

Optionally, delete the created `DeleteBackupRequest` object
from the cluster after `Backup` has been deleted.

For reference, follow the [official documentation](https://velero.io/docs/v1.15/backup-reference/#deleting-backups).
