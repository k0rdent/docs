# Scheduled Management Backups

Backups should be run on a schedule consistent with the policy requirements of the environment. For example a production environment might be set for "daily" backups, while a testing environment is set for "weekly".

## Create a Management Backup

Periodic backups are handled by a `ManagementBackup` object, which uses a [Cron](https://en.wikipedia.org/wiki/Cron) expression
for its `.spec.schedule` field.
If the `.spec.schedule` field is not set, a [backup on demand](./ondemand-backups.md#management-backup-on-demand) will be created instead.

Optionally, set the name of the `.spec.backup.storageLocation` of the `BackupStorageLocation` object.
The default location is the `BackupStorageLocation` object with `.spec.default` set to `true`.

For example, you can create a `ManagementBackup` object that backs up to the storage object
created in the [preparation step](./prepare-backups.md) every 6 hours
(ref: [Kubernetes CronJob schedule syntax, "Vixie cron" step values](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/#schedule-syntax)). Create a YAML file called `scheduled-backup.yaml`:

```yaml
apiVersion: k0rdent.mirantis.com/v1alpha1
kind: ManagementBackup
metadata:
  name: kcm
spec:
  schedule: "0 */6 * * *"
  storageLocation: aws-s3
EOF
```
Start the scheduled backup process by applying the YAML to the cluster:
```sh
kubectl apply -f scheduled-backup.yaml
```
Confirm the backup creation was successful by navigating to the appropriate storage console UI or from the command line:
```sh
kubectl get managementbackup
```
The `managementbackup` should show as `Completed`:
```console
NAME              LASTBACKUPSTATUS   NEXTBACKUP   AGE
example-backup    Completed                       8m  
```
