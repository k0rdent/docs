# Management Backup on Demand

To create a single backup of the existing {{{ docsVersionInfo.k0rdentName }}} management cluster information, you can create a `ManagementBackup` object
using a YAML document and the `kubectl` CLI. The object then creates only one instance of a backup. For example you can backup
to the location created [previously](./prepare-backups.md).

> NOTE:
> For the [regional cluster](../regional-clusters/index.md) case,
> make sure to setup the same location on the regional cluster.

Create a one time backup of your {{{ docsVersionInfo.k0rdentName }}} cluster by creating the following object:

```sh
kubectl create -f - <<EOF
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ManagementBackup
metadata:
  name: example-backup
spec:
  storageLocation: aws-s3
EOF
```

Confirm the backup was successful by navigating to the appropriate storage console UI or from the command line:

```sh
kubectl get mgmtbackup
```

The `managementbackup` should show as `Completed`:

```console
NAME              LASTBACKUPSTATUS   NEXTBACKUP   AGE
example-backup    Completed                       8m
```
