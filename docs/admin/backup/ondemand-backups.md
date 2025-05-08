# Management Backup on Demand

To create a single backup of the existing {{{ docsVersionInfo.k0rdentName }}} management cluster information, you can create a `ManagementBackup` object
using a YAML document and the `kubectl` CLI. The object then creates only one instance of a backup. For example you can backup
to the location created [previously](./prepare-backups.md). Create a YAML file called `one-time-backup.yaml`:

```yaml
apiVersion: k0rdent.mirantis.com/v1alpha1
kind: ManagementBackup
metadata:
  name: example-backup
spec:
  storageLocation: aws-s3
```
Create a one time backup of your {{{ docsVersionInfo.k0rdentName }}} cluster by applying the YAML to the cluster:
```sh
kubectl apply -f one-time-backup.yaml
```
Confirm the backup was successful by navigating to the appropriate storage console UI or from the command line:
```sh
kubectl get managementbackup
```
The `managementbackup` should show as `Completed`:
```
NAME              LASTBACKUPSTATUS   NEXTBACKUP   AGE
example-backup    Completed                       8m
```
