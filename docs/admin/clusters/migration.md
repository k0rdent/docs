# Migrate `ClusterDeployment` from one management cluster to another

This guide provides instructions for migrating a `ClusterDeployment`
resource from one {{{ docsVersionInfo.k0rdentName }}} management cluster to another.
This process uses [Velero](https://velero.io/) for backup and restore operations
between the clusters.

## Prerequisites

Before beginning the migration process, ensure you have:

1. Access to both source and target management clusters with admin permissions.
1. `kubectl` configured to access both clusters.
1. Velero properly installed and configured on both clusters (see [Preparing for Backups](../backup/prepare-backups.md)).

## Prepare your clusters

1. **Source Cluster**: Prepare your source cluster for backups by following the instructions
   in [Preparing for Backups](../backup/prepare-backups.md).
1. **Target Cluster**: Similarly, prepare your target cluster with the same Velero
   configuration using **the same backup storage location**.

## Migration Steps

### 1. Backup the ClusterDeployment from the source cluster

```sh
# Switch context to source cluster
kubectl config use-context <source-cluster-context>
# Or set the source config
export KUBECONFIG="<path-to-source-cluster-kubeconfig>"

# Create a backup
CLD="<cluster-deployment-name>"
BSL="<storage-location-name>"
TPL="$(kubectl -n <cld-namespace> get clusterdeployments "$CLD" -o go-template='{{.spec.template}}')"

{
  cat <<EOF
apiVersion: velero.io/v1
kind: Backup
metadata:
  name: cld-migration
  namespace: kcm-system
spec:
  storageLocation: $BSL
  includedNamespaces:
  - '*'
  orLabelSelectors:
  - matchLabels:
      k0rdent.mirantis.com/component: kcm
  - matchLabels:
      cluster.x-k8s.io/provider: cluster-api
  - matchLabels:
      controller.cert-manager.io/fao: "true"
  - matchLabels:
      helm.toolkit.fluxcd.io/name: $CLD
  - matchLabels:
      cluster.x-k8s.io/cluster-name: $CLD
EOF

  kubectl -n <cluster-template-namespace> get clustertemplates "$TPL" \
    -o go-template='{{range .status.providers}}{{if ne . "cluster-api"}}{{printf "  - matchLabels:\n      cluster.x-k8s.io/provider: %s\n" .}}{{end}}{{end}}'
} | kubectl create -f -


# Verify backup completion
kubectl -n kcm-system wait backups.velero.io cld-migration \
    --for=jsonpath='{.status.phase}'='Completed' \
    --timeout 10m
```

### 2. Prepare the target Management cluster

```sh
# Switch context to target cluster
kubectl config use-context <target-cluster-context>
# Or set the target config
export KUBECONFIG="<path-to-target-cluster-kubeconfig>"

# Verify Velero and BackupStorageLocation are properly configured
kubectl -n kcm-system get backupstoragelocation
```

### 3. Restore the ClusterDeployment to the target cluster

```sh
# Disable admission validating webhook
kubectl patch managements kcm --type=merge \
    --patch='{"spec":{"core":{"kcm":{"config":{"admissionWebhook":{"enabled": false}}}}}}'

# Wait the management cluster to be reconfigured
kubectl wait management kcm --for=condition=Ready=True --timeout 10m

# Verify the backups synced from the backup storage location
kubectl -n kcm-system get backups.velero.io

# Create a restore operation on the target cluster
kubectl create -f - <<EOF
apiVersion: velero.io/v1
kind: Restore
metadata:
  name: restore-cld-migration
  namespace: kcm-system
spec:
  backupName: cld-migration
  includedNamespaces:
  - '*'
  restoreStatus:
    includedResources:
    - '*'
  excludedResources:
  - mutatingwebhookconfiguration.admissionregistration.k8s.io
  - validatingwebhookconfiguration.admissionregistration.k8s.io
EOF

# Wait for the restore process successful completion
kubectl -n kcm-system wait restores.velero.io restore-cld-migration \
    --for=jsonpath='{.status.phase}'='Completed' \
    --timeout 10m

# Enable admission validating webhook back (if it was enabled initially)
kubectl patch managements kcm --type=merge \
    --patch='{"spec":{"core":{"kcm":{"config":{"admissionWebhook":{"enabled": true}}}}}}'
```

### 4. Verify the migration

```sh
# Verify the ClusterDeployment exists on the target cluster
kubectl -n <cld-namespace> get clusterdeployments <cluster-deployment-name>

# Check cluster status
kubectl -n <cld-namespace> describe clusterdeployments <cluster-deployment-name>
```

## Troubleshooting

- **Backup fails**: Ensure Velero is properly configured and has access to
    the storage location. Check Velero logs for specific errors.
- **Restore fails**: Verify that the target cluster can access the backup
    storage location and has the necessary permissions.
- **Resource conflicts**: If resources already exist in the target cluster,
    you may need to delete them first or use the
    `existingResourcePolicy: update` option in your `Restore`.

For more detailed information on using Velero for backups and restores,
refer to the [official Velero documentation](https://velero.io/docs/).
