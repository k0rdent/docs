# Management Backup on Demand

To create a single backup of the existing {{{ docsVersionInfo.k0rdentName }}} management cluster information, you can create a `ManagementBackup` object
using a YAML document and the `kubectl` CLI. The object then creates only one instance of a backup. For example you can backup
to the location created earlier:

```yaml
apiVersion: k0rdent.mirantis.com/v1alpha1
kind: ManagementBackup
metadata:
  name: example-backup
spec:
  storageLocation: aws-s3
```
