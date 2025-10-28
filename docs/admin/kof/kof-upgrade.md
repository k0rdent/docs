# Upgrading KOF

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
        diff -u values--kof-mothership.bak mothership-values.yaml
        ```
    * Run all `helm upgrade` commands with the new `--version` and files as documented.
* Do the same for other [KOF guides](index.md#guides).
* Apply each relevant "Upgrade to" section of this page from older to newer.
    * For example, if you're upgrading from v1.1.0 to v1.3.0,
    * first apply the [Upgrade to v1.2.0](#upgrade-to-v120) section,
    * then apply the [Upgrade to v1.3.0](#upgrade-to-v130) section.

## Upgrade to v1.5.0

**Important!!!**

> NOTICE:
> This is for users of **kof-istio** only.

Starting from the **v1.5.0** release, Istio has been moved to a separate repository, which changes the installation and upgrade process. Upgrading KOF **will trigger a complete uninstallation** of all components across Istio clusters. To prevent data loss and ensure a smooth migration, you must carefully follow the steps in the given order. Again, the steps below are only required if any Istio clusters were deployed.

### 1. Back Up Data from Istio Clusters

> NOTE:
> Perform all backup steps in this section **for each Istio cluster** individually. Each cluster must have its own backup before proceeding with the upgrade.

#### Create a PersistentVolumeClaim

Create a `PersistentVolumeClaim` named `backup-pvc` on the management cluster:

```yaml
kubectl apply -f - <<EOF
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: backup-pvc
  namespace: kof
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi # Adjust according to your data size
  storageClassName: standard
EOF
```

> NOTE:
> To estimate how much storage you need for the backup, open the [kof-ui](./ui.md), navigate to the `VictoriaMetrics/Logs` section, and click the `VictoriaMetrics storage` pod name on the cluster you want to back up. Find the `Data Size` metric and multiply this value by at least two (or by at least five for VictoriaLogs). This is because the metric shows data compressed using the VictoriaMetrics algorithm, while the backup will be stored in a simple gzip format, which does not compress as efficiently.

#### Create a Backup Pod with `curl`

Deploy a temporary pod for performing backups on the management cluster:

```yaml
kubectl apply -f - <<EOF
apiVersion: apps/v1
kind: Deployment
metadata:
  name: backup-deployment
  namespace: kof
spec:
  replicas: 1
  selector:
    matchLabels:
      app: backup-deployment
  template:
    metadata:
      labels:
        app: backup-deployment
    spec:
      containers:
      - name: backup
        image: curlimages/curl:latest
        command: ["/bin/sleep", "infinity"]
        volumeMounts:
        - mountPath: /home/curl_user
          name: backup-volume
      volumes:
      - name: backup-volume
        persistentVolumeClaim:
          claimName: backup-pvc
EOF
```

#### Retrieve Cluster Endpoints

Locate the regional cluster `ConfigMap` named `kof-<cluster-name>` in the `kcm-system` namespace of the management cluster.

Record the following endpoint values:

* read_logs_endpoint
* read_metrics_endpoint

#### Connect to the Backup Pod

```bash
kubectl exec -it -n kof <BACKUP_DEPLOYMENT_POD_NAME> -- /bin/sh
```

#### Back Up VictoriaMetrics Data

```bash
curl -H 'Accept-Encoding: gzip' -sSN \
  <read_metrics_endpoint>/api/v1/export \
  -d 'match[]={__name__!=""}' \
  > victoria-metrics-backup.gz
```

#### Back Up VictoriaLogs Data

```bash
curl -H 'Accept-Encoding: gzip' -sSN \
  <read_logs_endpoint>/select/logsql/query \
  -d 'query=*' > victoria-logs-backup.gz
```

#### (Optional) Download Backups Locally

```bash
kubectl cp -n kof <BACKUP_DEPLOYMENT_POD_NAME>:victoria-metrics-backup.gz ./victoria-metrics-backup.gz
kubectl cp -n kof <BACKUP_DEPLOYMENT_POD_NAME>:victoria-logs-backup.gz ./victoria-logs-backup.gz
```

### 2. Clean Up the Old Istio Clusters

> IMPORTANT:
> Ensure that both `VictoriaMetrics` and `VictoriaLogs` backup files have been successfully created and verified before the cluster cleanup.

#### Pause Synchronization on Managed Clusters

Before starting the cleanup, execute the following command on the management cluster:

```bash
kubectl scale --replicas=0 deployment/addon-controller -n projectsveltos
```

This command temporarily pauses synchronization between the management cluster and all managed clusters. It ensures that no old configurations are applied during the cleanup process.

#### Cleanup Old KOF Components

Use the `kof-nuke.bash` script (located in the `kof/script` directory) to completely remove all old `kof` resources from the remote cluster.

Run the script for each **regional** and **child** cluster, for example:

```bash
export KUBECONFIG=regional-kubeconfig && ls $KUBECONFIG && scripts/kof-nuke.bash
```

Cleanup typically takes 1–5 minutes, depending on the cluster size and network speed.

#### Cleanup Old Istio Components

Remove old Istio components for each **regional** and **child** cluster

```bash
export KUBECONFIG=regional-kubeconfig

helm uninstall --wait -n istio-system kof-istio-gateway
helm uninstall --wait -n istio-system kof-istio
helm uninstall --wait -n istio-system cert-manager
kubectl delete namespace istio-system --wait
kubectl get crd -o name | grep --color=never 'istio.io' | xargs kubectl delete
```

Once the cleanup of all regional and child clusters is complete,
run `unset KUBECONFIG` to use the **management** cluster in the next steps.

### 3. Remove the Old Istio Chart

Remove the old Istio release and related resources from the management cluster:

```bash
helm un -n istio-system kof-istio
kubectl delete namespace istio-system --wait
kubectl get crd -o name | grep --color=never 'istio.io' | xargs kubectl delete
```

### 4. Deploy New Istio Release

Install the new Istio release to the management cluster.

#### Install the `k0rdent-istio-base` Chart

```bash
helm upgrade -i --wait \
  --create-namespace -n istio-system k0rdent-istio-base \
  --set cert-manager-service-template.enabled=false \
  --set injectionNamespaces="{kof}" \
  oci://ghcr.io/k0rdent/istio/charts/k0rdent-istio-base --version 0.1.0
```

**Notes:**

* `cert-manager-service-template.enabled=false` disables the deployment of the cert-manager service template. It should already be deployed as part of KOF.
* `injectionNamespaces="{kof}"` ensures Istio sidecars are injected only into the `kof` namespace. To inject sidecars into additional namespaces, list them comma-separated: `{kof,<YOUR_NAMESPACE>}`.

#### Install the `k0rdent-istio` Chart

```bash
helm upgrade -i --wait -n istio-system k0rdent-istio \
  --set cert-manager-service-template.enabled=false \
  --set "istiod.meshConfig.extensionProviders[0].name=otel-tracing" \
  --set "istiod.meshConfig.extensionProviders[0].opentelemetry.port=4317" \
  --set "istiod.meshConfig.extensionProviders[0].opentelemetry.service=kof-collectors-daemon-collector.kof.svc.cluster.local" \
  oci://ghcr.io/k0rdent/istio/charts/k0rdent-istio --version 0.1.0
```

### 5. Upgrade the KOF Version

Upgrade KOF to the target version following standard upgrade procedures.

### 6. Restart the KOF Pods

You must restart the KOF pods on the management cluster to update the `istio-proxy` sidecar. Without restarting, you may encounter connection errors or Istio pod crashes.

```bash
kubectl delete pod --all -n kof
```

**Notes:**

* If you have additional namespaces with Istio sidecar injection, make sure to restart pods in those namespaces as well.
* Restarting ensures all pods run with the updated Istio configuration and sidecar versions.

### 7. Resume Sveltos Synchronization

Resume synchronization between the management cluster and all managed (regional and child) clusters.

Run the following command on the management cluster:

```bash
kubectl scale --replicas=1 deployment/addon-controller -n projectsveltos
```

### 8. Add New Labels to ClusterDeployment

To enable Istio on your clusters, you need to add two new labels to the corresponding ClusterDeployment resources.

* `k0rdent.mirantis.com/istio-role: member` - Apply this label to СlustersDeployment where Istio should be installed.
* `k0rdent.mirantis.com/istio-gateway: "true"` - Apply this label only to regional clusters to install Istio gateway.

### 9. Restore Data

Use the backup created in step 2 to restore VictoriaMetrics and VictoriaLogs data.

#### Connect to the Backup Pod

```bash
kubectl exec -it -n kof <BACKUP_DEPLOYMENT_POD_NAME> -- /bin/sh
```

#### Restore VictoriaMetrics Data

```bash
curl -H 'Content-Encoding: gzip' -sSX POST \
  -T victoria-metrics-backup.gz \
  http://<CLUSTER_NAME>-vminsert:8480/insert/0/prometheus/api/v1/import
```

#### Restore VictoriaLogs Data

```bash
curl -H 'Content-Encoding: gzip' -sSX POST \
  -T victoria-logs-backup.gz \
  http://<CLUSTER_NAME>-logs-insert:9481/insert/jsonline
```

## Upgrade to v1.4.0

* `PromxyServerGroup` CRD was moved from the `crds/` directory to the `templates/` directory for auto-upgrade.
* Please use `--take-ownership` on upgrade of `kof-mothership` to 1.4.0:
    ```bash
    helm upgrade --take-ownership \
      --reset-values --wait -n kof kof-mothership -f mothership-values.yaml \
      oci://ghcr.io/k0rdent/kof/charts/kof-mothership --version 1.4.0
    ```
* This will not be required in future upgrades.

## Upgrade to v1.3.0

Before upgrading any helm chart:
* If you have customized [VMCluster or VMAlert resources](https://github.com/k0rdent/kof/blob/v1.2.1/charts/kof-mothership/values.yaml#L169)
    then update your resources accordingly to the [new values under "spec"](https://github.com/k0rdent/kof/blob/v1.3.0/charts/kof-mothership/values.yaml#L167).

* If you have customized VMCluster/VMAlert resources using the "k0rdent.mirantis.com/kof-storage-values" cluster annotation, then keep the old but put new values first to reconcile the new `ClusterDeployment` configuration on the current release, **then** run the helm charts upgrade. After regional clusters have the new `kof-storage` helm chart installed, you can remove old values from the cluster annotation.
* If you have set `storage` values of the `kof-regional` chart, update them in the same way.

* If you are not using [Istio](kof-install.md#istio),
    then on the step 8 of the [Management Cluster](kof-install.md#management-cluster) upgrade
    please apply this temporary workaround for the [Reconciling MultiClusterService](https://github.com/k0rdent/kcm/issues/1914) issue:
    ```bash
    kubectl rollout restart -n kcm-system deploy/kcm-controller-manager
    ```

## Upgrade to v1.2.0

* As part of the KOF 1.2.0 overhaul of metrics collection and representation, we switched from the [victoria-metrics-k8s-stack](https://github.com/VictoriaMetrics/helm-charts/tree/master/charts/victoria-metrics-k8s-stack) metrics and dashboards to [opentelemetry-kube-stack](https://github.com/open-telemetry/opentelemetry-helm-charts/tree/main/charts/opentelemetry-kube-stack) metrics and [kube-prometheus-stack](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack) dashboards.
* Some of the previously collected metrics have slightly different labels.
* If consistency of timeseries labeling is important, users are advised to conduct relabeling of the corresponding timeseries in the metric storage by running a retroactive relabeling procedure of their preference.
* A possible reference solution here would be to use [Rules backfilling via vmalert](https://victoriametrics.com/blog/rules-replay/).
* The labels that would require renaming are these:
    * Replace `job="integrations/kubernetes/kubelet"` with `job="kubelet", metrics_path="/metrics"`.
    * Replace `job="integrations/kubernetes/cadvisor"` with `job="kubelet", metrics_path="/metrics/cadvisor"`.
    * Replace `job="prometheus-node-exporter"` with `job="node-exporter"`.

Also:

* To upgrade from `cert-manager-1-16-4` to `cert-manager-v1-16-4`
    please apply this patch to management cluster:
    ```bash
    kubectl apply -f - <<EOF
    apiVersion: k0rdent.mirantis.com/v1beta1
    kind: ServiceTemplateChain
    metadata:
      name: patch-cert-manager-v1-16-4-from-1-16-4
      namespace: kcm-system
      annotations:
        helm.sh/resource-policy: keep
    spec:
      supportedTemplates:
        - name: cert-manager-v1-16-4
        - name: cert-manager-1-16-4
          availableUpgrades:
            - name: cert-manager-v1-16-4
    EOF
    ```

## Upgrade to v1.1.0

* After you `helm upgrade` the `kof-mothership` chart, please run the following:
    ```bash
    kubectl apply --server-side --force-conflicts \
    -f https://github.com/grafana/grafana-operator/releases/download/v5.18.0/crds.yaml
    ```
* After you get `regional-kubeconfig` file on the [KOF Verification](./kof-verification.md) step,
  please run the following for each regional cluster:
    ```bash
    KUBECONFIG=regional-kubeconfig kubectl apply --server-side --force-conflicts \
    -f https://github.com/grafana/grafana-operator/releases/download/v5.18.0/crds.yaml
    ```
* This is noted as required in the [grafana-operator release notes](https://github.com/grafana/grafana-operator/releases/tag/v5.18.0).
