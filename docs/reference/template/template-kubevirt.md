# KubeVirt cluster template parameters

## ClusterDeployment parameters

To create a cluster deployment, you must provide a set of parameters to the ClusterDeployment object.
The full list of parameters is defined in the corresponding Helm chart for the Cluster Template you use. For
built‑in KubeVirt Cluster Templates, refer to the
[Cluster Templates](https://github.com/k0rdent/kcm/tree/v{{{ extra.docsVersionInfo.k0rdentDotVersion }}}/templates/cluster)
section of the `k0rdent/kcm` repository.

The KubeVirt API is documented in the [KubeVirt API Reference](https://kubevirt.io/api-reference/).

### Data Volumes

If you want to use a `DataVolume` that references the source data you plan to import into your KubeVirt cluster
deployment, configure the `dataVolumes` section of the ClusterDeployment spec for `controlPlane` and/or `worker`
nodes. For example:

```yaml
spec:
  config:
    controlPlane:
      dataVolumes:
      - name: dv0
        accessModes: ReadWriteOnce
        storage: 7Gi
        storageClassName: csi-cinder-sc-delete
        source:
          http:
            url: https://cloud-images.ubuntu.com/jammy/current/jammy-server-cloudimg-amd64.img
    worker:
      dataVolumes:
        - name: dv1
          accessModes: ReadWriteOnce
          storage: 7Gi
          storageClassName: csi-cinder-sc-delete
          source:
            http:
              url: https://cloud-images.ubuntu.com/jammy/current/jammy-server-cloudimg-amd64.img
```

Supported parameters for each DataVolume are:

* `name` (string): Name of the DataVolume.
* `accessModes` (array): Desired access modes for the volume. Valid values are `ReadOnlyMany`, `ReadWriteMany`,
`ReadWriteOnce`, `ReadWriteOncePod`. More information: [Access Modes](https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1).
* `storage` (string): Requested storage size for the corresponding PVC (example: `10Gi`).
* `volumeMode` (string): Type of volume required by the claim: `Block`, `Filesystem` or `FromStorageProfile`.
* `storageClassName` (string): Name of the StorageClass required by the claim. More information: [Storage Class](https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1)).
* `source` (object): The source of the DataVolume. See [supported volumes sources](https://kubevirt.io/user-guide/storage/disks_and_volumes/#volumes)
for more details.

For more information, see [DataVolumes](https://kubevirt.io/user-guide/storage/disks_and_volumes/#datavolume)
in the official KubeVirt documentation.

### Networking configuration

For the KubeVirt cluster to function properly, networking must be properly configured.
k0rdent supports configuring the network of a KubeVirt ClusterDeployment through the `devices` and `networks` sections
for the `controlPlane` and `worker` nodes. For example, to configure networking for the control plane VMs:

```yaml
spec:
  config:
    controlPlane:
      devices:
        interfaces:
        - name: default
          bridge: {}
      networks:
      - name: default
        pod: {}
```

By default, the `bridge` network interface type is used for both control plane and worker nodes.
For more information about KubeVirt networking, see the official KubeVirt documentation:
[Interfaces and Networks](https://kubevirt.io/user-guide/network/interfaces_and_networks/).
