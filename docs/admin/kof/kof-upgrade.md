# Upgrading KOF

## Data Backup

Before migrating or upgrading, it's recommended to create a backup of your Victoria Logs and Victoria Metrics data. You can export the data from the regional cluster endpoints to local files using the following commands. Repeat the describe procedure for each of your regional cluster if needed.

1. Lookup the regional cluster configmap named `kof-<cluster-name>` in the `kcm-system` namespace on the management cluster.

    ```bash
    kubectl get cm kof-<cluster-name> -n kcm-system
    ```

2. Note the `read_logs_endpoint`, `read_metrics_endpoint`, and other endpoints values from the configmap.
3. Ensure that you have enough free disk space (e.g. check the total used size of volumes allocated to your regional cluster). Victoria Logs/Metrics usually compress the data. Commands to fetch the data compress data too, but it stores data in a JSON line format, so requires 5 times more space.
4. Ensure the connectivity to the regional cluster (e.g. do it on the Mothership cluster that surely has connectivity). If you are using Istio service mesh, consider to run a container in the Mothership cluster with attached properly sized volume in the kof namespace for connectivity to regional cluster endpoints.
Check the k0rdent [cluster documentation](../clusters/deploy-cluster.md) to retrieve kubernetes configuration.

### Backup Victoria Metrics

To backup all metrics data to a local file (`victoria-metrics-backup.gz`):

```bash
curl -H 'Accept-Encoding: gzip' -sSN \
  -u "<username>:<password>" \
  <read_metrics_endpoint>/api/v1/export?reduce_mem_usage=1 \
  -d 'match[]={__name__!=""}' \
  > victoria-metrics-backup.gz
```

To restore all metrics to a regional cluster from a local file run:

Without Istio servicemesh:

```bash
KUBECONFIG=kubeconfig kubectl port-forward svc/vminsert-cluster 8480:8480 -n kof # use kubeconfig of regional cluster to import data

curl -H 'Content-Encoding: gzip' -sSX POST \
  -T victoria-metrics-backup.gz \
  http://localhost:8480/insert/0/prometheus/api/v1/import
```

With Istio servicemesh:

```bash
curl -H 'Content-Encoding: gzip' -sSX POST \
  -T victoria-metrics-backup.gz \
  http://<CLUSTER_NAME>-vminsert:8480/insert/0/prometheus/api/v1/import
```

- This command fetches all metrics from the old regional cluster and saves them as a gzip-compressed file.
- You can later use this file for migration or restoration by uploading it to the new cluster.

### Backup Victoria Logs

Before querying logs increase the "search.maxQueryDuration" value for the `kof-storage-victoria-logs-cluster-vlselect` deployment which is just a 30s by default and not enough to query all logs at one request.

```bash
KUBECONFIG=kubeconfig kubectl edit deployment/kof-storage-victoria-logs-cluster-vlselect -n kof # use kubeconfig of regional cluster to import data
```

Edit and save the deployment spec to add `search.maxQueryDuration` argument (remove it after you finish the backup).

```yaml
spec:
  template:
    spec:
      containers:
      - args:
        - --search.maxQueryDuration=24h
```

To backup all logs data to a local file (`victoria-logs-backup.gz`):

```bash
curl -H 'Accept-Encoding: gzip' -sSN \
  -u "<username>:<password>" \
  <read_logs_endpoint>/select/logsql/query \
  -d 'query=*' > victoria-logs-backup.gz
```


- This command fetches all logs from the old regional cluster and saves them as a gzip-compressed file.
- You can later use this file for migration or restoration by uploading it to the new cluster.

To restore all logs to a regional cluster from a local file run:

Without Istio servicemesh:

```bash

KUBECONFIG=kubeconfig kubectl port-forward svc/kof-storage-victoria-logs-cluster-vlinsert 9481:9481 -n kof # use kubeconfig of regional cluster to import data

curl -H 'Content-Encoding: gzip' -sSX POST \
  -T victoria-logs-backup.gz \
  http://localhost:9481/insert/jsonline
```

*N.B.* the default `write_logs_endpoint` ends with `/insert/opentelemetry/v1/logs`: replace it with `/insert/jsonline`.

With Istio servicemesh:

```bash
curl -H 'Content-Encoding: gzip' -sSX POST \
  -T victoria-logs-backup.gz \
  http://<CLUSTER_NAME>-logs-insert:9481/insert/jsonline
```

**Notes:**
- Replace `<username>:<password>`, `<read_metrics_endpoint>`, `<read_logs_endpoint>`, etc with your actual credentials and endpoints (lookup the `storage-vmuser-credentials` secret in the `kof` namespace for basic authentication credentials if you are not using Istio servicemesh)
- For chunked or filtered backups, refer to the [official documentation](https://docs.victoriametrics.com/victorialogs/querying/#querying-logs) for available query options.
- Ensure you have sufficient disk space for the backup files.

## Data migration to a new regional cluster

This section describes the process for migrating data to a new KOF regional cluster, including both the cluster migration steps and the detailed procedure for migrating Victoria Logs and Metrics data.

### Migration Overview

1. **Deploy a new kof-regional cluster.**
2. **Add `k0rdent.mirantis.com/kof-regional-cluster-name` label** to a child ClusterDeployment to point all collectors to the new regional cluster.
3. **Ensure metrics and logs are available** for the child cluster, confirming the new regional cluster is operational.
4. **Change all other child clusters** from the old regional cluster to the new one.
5. **Start the data migration.**
6. **Ensure that the data is migrated and explorable**
7. **Delete old kof-regional cluster**
8. **Remove the label from child ClusterDeployments.**

### Victoria Logs and Metrics Data Migration

Follow these steps to migrate Victoria Logs and Metrics data from the old regional cluster to the new one:

1. **Lookup the old regional cluster configmap** named `kof-<cluster-name>` in the `kcm-system` namespace on the management cluster.
2. **Note the `read_logs_endpoint` and `read_metrics_endpoint` values** from the configmap.
3. **Authentication and Service Mesh:**
    - If **not using Istio servicemesh**:
        - Lookup the `storage-vmuser-credentials` secret in the `kof` namespace for basic authentication credentials.
    - If **using Istio servicemesh**:
        - Copy the `istio-remote-secret-<cluster-name>` secret from the old regional cluster to the new regional cluster to enable Istio endpoints discovery.
4. **Prepare a migration environment** on the new regional cluster:
    ```bash
    KUBECONFIG=regional-kubeconfig kubectl run -it --rm \
      --image=alpine:latest -n kof migration -- sh

    apk update
    apk add curl pv
    ```
5. **Migrate metrics data** by running the following command (replace placeholders as needed):
    ```bash
    curl -H 'Accept-Encoding: gzip' -sSN \
      -u "<username>:<password>" \
      <read_metrics_endpoint>/api/v1/export?reduce_mem_usage=1 \
      -d 'match[]={__name__!=""}' \
      | pv | curl -H 'Content-Encoding: gzip' -sSX POST -T - \
      http://vminsert-cluster.kof:8480/insert/0/prometheus/api/v1/import
    ```

    Check [VictoriaMetrics API](https://docs.victoriametrics.com/victoriametrics/url-examples/#apiv1export) for more details.

    The query fetches all metrics from the old regional cluster endpoint. If you need to split migration by chunks, please refer the documentation for `match[]` filter available options (by metric name, time range, etc)

    Reset vmselect cache after the migration:
    ```bash
    curl -I http://vmselect-cluster.kof:8481/internal/resetRollupResultCache
    ```

6. **Migrate logs data** by running the following command (replace placeholders as needed):
    ```bash
    curl -H 'Accept-Encoding: gzip' -sSN \
      -u "<username>:<password>" \
      <read_logs_endpoint>/select/logsql/query \
      -d 'query=*' \
      | pv | curl -H 'Content-Encoding: gzip' -sSX POST -T - \
      http://kof-storage-victoria-logs-cluster-vlinsert.kof:9481/insert/jsonline
    ```

    Check [VictoriaLogs FAQ](https://docs.victoriametrics.com/victorialogs/faq/#how-to-export-logs-from-victorialogs) for more details.

    The query fetches all logs from the old regional cluster endpoint. If you need to split migration by chunks, please refer the documentation for `logsql` query filter available options (by stream name, time range, etc)

To migrate data with transformation please consider one of the following options:

* Backup data to a file with a JSON line format, change each json, restore the file to a new cluster
* Use the [Python script](https://github.com/k0rdent/kof/tree/main/scripts/victoria-migration) with your custom transformation function

**Explanation of curl parameters:**

- `-H 'Accept-Encoding: gzip'`: Requests gzip-compressed response to reduce bandwidth.
- `-sS`: Silent mode. Hides progress, shows error messages.
- `-N`: Disables output buffering, streaming data as it arrives.
- `-u "<username>:<password>"`: Specifies basic authentication credentials (not needed for Istio)
- `-d 'match[]={__name__!=""}'`: Sends POST data to filter all metrics.
- `| pv`: Pipes output through `pv` to monitor progress.
- Second `curl`:
  - `-H 'Content-Encoding: gzip'`: Informs the server that the data is gzip-compressed.
  - `-X POST`: Uses HTTP POST method.
  - `-T -`: Reads data from stdin (the pipe) and uploads it.

**Notes:** Ensure you have the correct credentials and endpoints for your environment. Adjust the commands as necessary for your authentication method and network setup.

## Upgrade to any version

* Create a backup of each KOF chart values in each cluster, for example:
    ```bash
    # Management cluster uses default KUBECONFIG=""
    for cluster in "" regional-kubeconfig child-kubeconfig; do
      for namespace in kof istio-system; do
        for chart in $(KUBECONFIG=$cluster helm list -qn $namespace); do
          KUBECONFIG=$cluster helm get values -n $namespace $chart -o yaml \
            > values-$cluster-$chart.bak
        done
      done
    done
    ls values-*.bak
    ```
* Ideally, [create a backup](../backup/index.md) of everything including VictoriaMetrics/Logs data volumes.
* Open the latest version of the [Installing KOF](kof-install.md) guide.
* Make sure you see the expected new version in the top navigation bar.
* Apply the guide step by step, but:
    * Skip unchanged credentials like `external-dns-aws-credentials`.
    * Before applying new YAML files, verify what has changed, for example:
        ```bash
        diff -u values-kof.bak kof-values.yaml
        ```
    * Run all `helm upgrade` commands with the new `--version` and files as documented.
* Do the same for other [KOF guides](index.md#guides).
* Apply each relevant "Upgrade to" section of this page from older to newer.

{%
    include-markdown "../../../includes/kof-upgrade-includes.md"
    start="<!--upgrade-start-->"
    end="<!--upgrade-end-->"
%}
