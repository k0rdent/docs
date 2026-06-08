# KOF Retention and Replication

KOF stores metrics in **VictoriaMetrics**,
logs in **VictoriaLogs**,
and traces in **VictoriaTraces**.

## Recommendations

Configure the storage class, space, retention, and replication
to balance cost, durability, and compliance, for example:

* **Management cluster:** short-term retention (1–30 days)
* **Regional clusters:** long-term retention (30–365 days)
* Increase **replicationFactor** where higher availability is required; this field enables you to determine how many copies are stored, usually on different nodes.
* The **replicaCount** defines how many pods should be running.

Review the next guides to make **informed decision:**

* [Storage Class Requirements for VictoriaMetrics Cluster](kof-storing.md#storage-class-requirements-for-victoriametrics-cluster)
* [VictoriaMetrics Cluster Resizing and Scalability](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#cluster-resizing-and-scalability)
* [VictoriaMetrics Replication and Data Safety](https://docs.victoriametrics.com/victoriametrics/cluster-victoriametrics/#replication-and-data-safety)
* [VictoriaLogs Cluster Replication](https://docs.victoriametrics.com/victorialogs/cluster/#replication) and [discussion](https://github.com/VictoriaMetrics/VictoriaLogs/issues/166#issuecomment-3043600409)
* [VictoriaTraces Cluster HA](https://docs.victoriametrics.com/victoriatraces/cluster/#high-availability)

> WARNING:
> If your `StorageClass` does not have [allowVolumeExpansion: true](https://kubernetes.io/docs/concepts/storage/storage-classes/#allow-volume-expansion)
> you will not be able to increase storage size by using the values below.

## Examples of values

### Metrics

```yaml
victoriametrics:
  vmcluster:
    spec:
      retentionPeriod: "30d"
      replicationFactor: 2
      vminsert:
        replicaCount: 2
      vmselect:
        replicaCount: 2
      vmstorage:
        replicaCount: 2
        resources:
          limits:
            cpu: "8"
            memory: 8000Mi
        storage:
          volumeClaimTemplate:
            spec:
              storageClassName: <EXAMPLE_STORAGE_CLASS>
              resources:
                requests:
                  storage: "200Gi"
```

Details: [VMClusterSpec](https://docs.victoriametrics.com/operator/api/#vmclusterspec)

### Logs

```yaml
victoria-logs-cluster:
  vlinsert:
    replicaCount: 2
  vlselect:
    replicaCount: 2
  vlstorage:
    replicaCount: 2
    extraArgs:
      retentionPeriod: "30d"
    persistentVolume:
      storageClassName: <EXAMPLE_STORAGE_CLASS>
      size: "100Gi"
```

Details: [Values of victoria-logs-cluster](https://github.com/VictoriaMetrics/helm-charts/blob/master/charts/victoria-logs-cluster/values.yaml)

### Audit Logs

KOF collects Kubernetes audit logs by default and stores them in a dedicated VictoriaLogs cluster (`vlcluster_audit`),
separate from the regular logs cluster, to allow a longer retention period (default: `1y`).

To change the retention period, storage class, or volume size, adjust the following in `kof-storage` values:

```yaml
victoriametrics:
  vlcluster_audit:
    enabled: true
    spec:
      vlinsert:
        replicaCount: 2
      vlselect:
        replicaCount: 2
      vlstorage:
        replicaCount: 2
        retentionPeriod: "1y"
        storage:
          volumeClaimTemplate:
            spec:
              storageClassName: <EXAMPLE_STORAGE_CLASS>
              resources:
                requests:
                  storage: "100Gi"
```

Details: [VLClusterSpec](https://docs.victoriametrics.com/operator/api/#vlclusterspec)

To disable audit log **storage**, set `vlcluster_audit.enabled: false` in `kof-storage` values.

To disable audit log **collection**, update the `kof-collectors` values to remove the `filelog/k8s_audit`
receiver from the daemon collector pipeline:

```yaml
opentelemetry-kube-stack:
  collectors:
    daemon:
      config:
        service:
          pipelines:
            logs:
              receivers:
                - otlp
                - receiver_creator
                - filelog/syslog
                - journald
```

### Traces

```yaml
victoria-traces-cluster:
  vtinsert:
    replicaCount: 2
  vtselect:
    replicaCount: 2
  vtstorage:
    replicaCount: 2
    extraArgs:
      retentionPeriod: "30d"
    persistentVolume:
      storageClassName: <EXAMPLE_STORAGE_CLASS>
      size: "100Gi"
```

Details: [Values of victoria-traces-cluster](https://github.com/VictoriaMetrics/helm-charts/blob/master/charts/victoria-traces-cluster/values.yaml)

## Places to customize

There are multiple places where the storage can be customized using these values.

### All regional clusters at once

Add these values to the `kof-values.yaml` file
under the `kof-regional.values.storage` key
as described in the step 5 of the [Management Cluster](kof-install.md#management-cluster) section.

### Specific regional cluster

Add these values to the regional `ClusterDeployment`
as the `spec.config.clusterAnnotations."k0rdent.mirantis.com/kof-storage-values"`
described in the step 10 of the [Regional Cluster](kof-install.md#regional-cluster) section.

### Regionless setup

Add these values to the placeholders in the [Regionless](kof-storing.md#regionless) section.

### Management to Management case

Add these values to the placeholders in the [From Management to Management](kof-storing.md#from-management-to-management) section.
