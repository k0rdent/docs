
<!--upgrade-start-->
## Upgrade to v1.8.0

### KOF Upgrade

KOF v1.8.0 introduces a new umbrella chart that consolidates the installation of all KOF components using FluxCD for orchestration. This represents a significant structural change in how KOF is deployed.

#### Key Changes

* **New umbrella chart**: The `kof` chart now manages the installation of operators, mothership, storage, and collectors components.
* **victoria-metrics-operator**: Now installed by the umbrella chart instead of as a dependency of `kof-mothership`.
* **Single deployment command**: Replaces the previous multi-step installation process.

#### Important: Backup Required

**Before upgrading to v1.8.0, you MUST create a backup of your Victoria Metrics and Victoria Logs data.**

The structural changes may require reinstallation of storage components, which could result in data loss if backups are not available. Follow the [Data Backup](../docs/admin/kof/kof-upgrade.md#data-backup) section at the top of this page to create backups of all your regional clusters.

#### Upgrade Procedure

1. **Create backups** as described in the [Data Backup](../docs/admin/kof/kof-upgrade.md#data-backup) section for all regional clusters.

2. **Backup current Helm values** for all KOF charts:
    ```bash
    helm get values -n kof kof-operators -o yaml > kof-operators-values.bak
    helm get values -n kof kof-mothership -o yaml > kof-mothership-values.bak
    helm get values -n kof kof-regional -o yaml > kof-regional-values.bak 2>/dev/null || true
    helm get values -n kof kof-child -o yaml > kof-child-values.bak 2>/dev/null || true
    helm get values -n kof kof-storage -o yaml > kof-storage-values.bak 2>/dev/null || true
    helm get values -n kof kof-collectors -o yaml > kof-collectors-values.bak 2>/dev/null || true
    ```

3. **Create new values file** for the umbrella chart. Merge your existing values into the new structure:

    Create `kof-values.yaml` with values nested under component keys. For example, if your `kof-mothership-values.bak` contains:
    ```yaml
    kcm:
      kof:
        mcs:
          kof-aws-dns-secrets:
            matchLabels:
              k0rdent.mirantis.com/kof-aws-dns-secrets: "true"
            secrets:
              - external-dns-aws-credentials
    ```

    Transform it to:
    ```yaml
    kof-mothership:
      values:
        kcm:
          kof:
            mcs:
              kof-aws-dns-secrets:
                matchLabels:
                  k0rdent.mirantis.com/kof-aws-dns-secrets: "true"
                secrets:
                  - external-dns-aws-credentials
    ```

    > NOTE:
    > `victoria-metrics-operator` helm chart is moved out of `kof-mothership` helm chart.
    > If you have modified values for `victoria-metrics-operator` helm chart, move them under this section:

    ```yaml
    victoria-metrics-operator:
      values:
    ```

    ??? note "Alternative: bash script that creates `kof-values.yaml` automatically"
        ```bash
        touch kof-values.yaml
        for filename in kof-*-values.bak; do
          component="${filename%-values.bak}"
          yq -i ".$component.values = load(\"$filename\")" kof-values.yaml
        done

        yq -i '
          .victoria-metrics-operator.values = .kof-mothership.values.victoria-metrics-operator
          | del(.kof-mothership.values.victoria-metrics-operator)
          | del(.victoria-metrics-operator.values | select(. == null))
        ' kof-values.yaml
        ```

4. **Patch VictoriaMetrics Operator CRDs upgrade config**:

Run the following command to enable automatic CRD upgrades for `victoria-metrics-operator` during the helm upgrade:

```bash
yq -i '
  ."kof-regional".values.storage."victoria-metrics-operator".crds.upgrade.enabled = true |
  ."kof-regional".values.storage."victoria-metrics-operator".crds.upgrade.forceConflicts = true |
  ."kof-regional".values.storage."victoria-metrics-operator".crds.upgrade.podLabels."sidecar.istio.io/inject" = "false"
' kof-values.yaml
```

5. **Upgrade to the umbrella chart**:
    ```bash
    helm upgrade -i --reset-values --wait \
      --create-namespace -n kof kof \
      -f kof-values.yaml \
      {{{ docsVersionInfo.kofVersions.kofOciRegistryBase }}}/charts/kof \
      --version 1.8.0
    ```

    The umbrella chart will take ownership of existing resources and upgrade them in place.

#### Verification

6. After upgrade, follow the [KOF Verification](../docs/admin/kof/kof-verification.md) guide to ensure KOF is functioning correctly.

7. **(If needed) Restore data** from backups if any storage components were reinstalled and verification shows data loss. Follow the restore procedures in the [Data Backup](../docs/admin/kof/kof-upgrade.md#data-backup) section.

### Istio Upgrade

> NOTICE:
> This section is for users of **k0rdent-istio** only.

Use this command to upgrade Istio:

```bash
 helm upgrade -i --reset-values --wait --create-namespace -n istio-system k0rdent-istio \
    {{{ docsVersionInfo.kofVersions.kofOciRegistryBaseIstio }}}/charts/k0rdent-istio \
    --version 0.4.0 \
    --set cert-manager-service-template.enabled=false \
    --set "istiod.meshConfig.extensionProviders[0].name=otel-tracing" \
    --set "istiod.meshConfig.extensionProviders[0].opentelemetry.port=4317" \
    --set "istiod.meshConfig.extensionProviders[0].opentelemetry.service=kof-collectors-daemon-collector.kof.svc.cluster.local" \
    --set-json 'gateway.resource.spec.servers[0]={"port":{"number":15443,"name":"tls","protocol":"TLS"},"tls":{"mode":"AUTO_PASSTHROUGH"},"hosts":["{clusterName}-vmauth.kof.svc.cluster.local"]}'
```

## Upgrade to v1.7.0

Notice the big changes:

* Grafana installation and automatic configuration are now disabled in KOF by default. You can [install and enable Grafana](../docs/admin/kof/kof-grafana.md) or [use KOF without Grafana](../docs/admin/kof/kof-using.md).
* [Tracing](https://docs.k0rdent.io/next/admin/kof/kof-tracing/) now uses VictoriaTraces instead of Jaeger.
* [Multi-tenancy](https://docs.k0rdent.io/next/admin/kof/kof-multi-tenancy/) was added, enabled by `k0rdent.mirantis.com/kof-tenant-id` label.
* Starting from v1.7.0, there is no need to use the `k0rdent.mirantis.com/kof-storage-secret` label to propagate the storage secret. From this version onward, storage secrets are automatically created and propagated to the corresponding cluster. Now each cluster has its own secrets and VMUser, which improves security.
* If you used secret generation and secret propagation values, there are major changes.

    Before:

    ```yaml
    kcm:
      kof:
        clusterProfiles:
          kof-storage-secrets:
            matchLabels:
              k0rdent.mirantis.com/kof-storage-secrets: "true"
            create_secrets: true
            secrets:
              - storage-vmuser-credentials
              - jaeger-admin-credentials
              - jaeger-admin-htpasswd
            htpasswdFrom:
              jaeger-admin-htpasswd: jaeger-admin-credentials
    ```

    Now:

    ```yaml
    kcm:
      kof:
        mcs:
          # This section is not active in values by default
          # It is included here only as an example of how to create secret propagation
          kof-storage-secrets:
            matchLabels:
              k0rdent.mirantis.com/kof-storage-secrets: "true"
            secrets:
              - storage-vmuser-credentials

        # -- Generation of secrets used by kof components.
        # Generate random username/password if secret not found.
        secrets:
          kof-storage-secrets:
            # htpasswdFrom: storage-vmuser-credentials
            secrets:
              - storage-vmuser-credentials
    ```

    Update your values to match the new structure.

* The previous storage secret propagation will be automatically disabled and this secret will be used only for the management cluster. If you use these credentials for purposes beyond VMUser, you will need to add values to enable propagation for this secret.

    ```yaml
    kcm:
      kof:
        mcs:
          kof-storage-secrets:
            matchLabels:
              k0rdent.mirantis.com/kof-storage-secrets: "true"
            secrets:
              - storage-vmuser-credentials
    ```

* If you want to continue using this secret as regional storage credentials, apply the following values in `kof-regional` values:

    ```yaml
    storage:
      victoriametrics:
        vmauth:
          vmuser:
            enabled: true
            credentials:
              username_key: username
              password_key: password
              credentials_secret_name: storage-vmuser-credentials
    ```

## Upgrade to v1.6.0

Before upgrading `kof-mothership`, ensure the following steps are completed:

1. Upgrade the `kof-operators` chart using the `--take-ownership` flag:

    ```bash
    helm upgrade --take-ownership \
      --reset-values --wait -n kof kof-operators \
      {{{ docsVersionInfo.kofVersions.kofOciRegistryBase }}}/charts/kof-operators --version 1.6.0
    ```

2. Obtain the `regional-kubeconfig` file during the [KOF Verification](../docs/admin/kof/kof-verification.md) step and make sure to upgrade `kof-operators` using the `--take-ownership` flag on each KOF Regional cluster:

    ```bash
    KUBECONFIG=regional-kubeconfig helm upgrade --take-ownership \
      --reset-values --wait -n kof kof-operators \
      {{{ docsVersionInfo.kofVersions.kofOciRegistryBase }}}/charts/kof-operators --version 1.6.0
    ```

This step will not be required in future upgrades.

### Istio Upgrade

> NOTICE:
> This section is for users of **k0rdent-istio** only.

Starting from k0rdent Istio v0.2.0, the Istio charts have been merged into a single chart called `k0rdent-istio`, replacing the previously used `k0rdent-istio-base` and `k0rdent-istio` charts. In k0rdent Istio v0.2.0, namespace creation with Istio sidecar injection was removed from the Istio charts. As a result, starting from the new KOF version, the kof namespace is created by KOF with the Istio injection label applied.

> IMPORTANT:
> You must upgrade KCM to v1.6.0 before upgrading KOF.

To prevent data loss and ensure a smooth migration, follow these steps:

#### 1. Back up data from all remote clusters

If you follow all instructions, KOF should not be uninstalled during the Istio upgrade process. However, to avoid potential data loss, perform the following step:

Follow the instructions in [Back Up Data from Istio Clusters](../docs/admin/kof/kof-upgrade.md#1-back-up-data-from-istio-clusters) from the v1.5.0 upgrade guide.

#### 2. Patch MultiClusterServices

To uninstall Istio without uninstalling KOF, remove the Istio dependency from the Istio `MultiClusterService` resources using the following commands:

```bash
kubectl patch mcs kof-istio-regional-cluster \
  --type=json \
  -p='[{"op":"remove","path":"/spec/dependsOn"}]'

kubectl patch mcs kof-istio-child-cluster \
  --type=json \
  -p='[{"op":"remove","path":"/spec/dependsOn"}]'
```

#### 3. Remove annotations from the KOF namespace on all remote clusters

Remove the annotations from the KOF namespace across all remote clusters to break the link with Sveltos resources and prevent the namespace from being uninstalled during the Istio upgrade.

```bash
KUBECONFIG=remote-kubeconfig kubectl patch namespace kof \
  --type=merge \
  -p='{"metadata":{"annotations":null}}'
```

#### 4. Uninstall old Istio resources on the management cluster

Use the following commands to uninstall the old Istio charts on the **management** cluster:

```bash
helm uninstall --wait -n istio-system k0rdent-istio
helm uninstall --wait -n istio-system k0rdent-istio-base
kubectl delete namespace istio-system --wait
kubectl get crd -o name | grep --color=never 'istio.io' | xargs kubectl delete 
kubectl get mcs -o name | grep "remote-secret-propagation-" | xargs -r kubectl delete
```

#### 5. Upgrade KOF

First upgrade the KOF operator using `--take-ownership` by following the instructions at the beginning of the [Upgrade to v1.6.0 version](../docs/admin/kof/kof-upgrade.md#upgrade-to-v160) section. After that, upgrade the KOF components as usual (kof-mothership, kof-regional, kof-child, etc.).

#### 6. Deploy the new Istio chart

Instead of installing two separate charts (`k0rdent-istio-base` and `k0rdent-istio`), install the single chart:

```bash
helm upgrade -i --reset-values --wait --create-namespace -n istio-system k0rdent-istio \
  {{{ docsVersionInfo.kofVersions.kofOciRegistryBaseIstio }}}/charts/k0rdent-istio --version 0.2.0 \
  --set cert-manager-service-template.enabled=false \
  --set "istiod.meshConfig.extensionProviders[0].name=otel-tracing" \
  --set "istiod.meshConfig.extensionProviders[0].opentelemetry.port=4317" \
  --set "istiod.meshConfig.extensionProviders[0].opentelemetry.service=kof-collectors-daemon-collector.kof.svc.cluster.local"
```

#### 7. Restart KOF pods

Wait until Istio is fully installed on the management and remote clusters, then restart the KOF pods using the following command:

```bash
kubectl delete pods -n kof --all
```

To restart KOF pods on a remote cluster, use:

```bash
KUBECONFIG=remote-kubeconfig kubectl delete pods -n kof --all
```

#### 8. (Optional) Restore Data

If, for some reason, your data on regional clusters was corrupted or KOF was uninstalled during the Istio upgrade process, follow the instructions in [Restore Data](../docs/admin/kof/kof-upgrade.md#9-restore-data)

## Upgrade to v1.5.0

> NOTE:
> To use the new [KCM Regional Clusters](../docs/admin/regional-clusters/index.md) with KOF, please apply the [KCM Region With KOF](../docs/admin/kof/kof-kcm-region.md) guide on top of the steps below.

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
> To estimate how much storage you need for the backup, open the [kof-ui](../docs/admin/kof/kof-using.md#kof-ui), navigate to the `VictoriaMetrics/Logs` section, and click the `VictoriaMetrics storage` pod name on the cluster you want to back up. Find the `Data Size` metric and multiply this value by at least two (or by at least five for VictoriaLogs). This is because the metric shows data compressed using the VictoriaMetrics algorithm, while the backup will be stored in a simple gzip format, which does not compress as efficiently.

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

#### Back Up VictoriaMetrics/Logs Data

For instructions on creating backups of VictoriaMetrics and log data, refer to the [Data Backup](../docs/admin/kof/kof-upgrade.md#data-backup) section.

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
  {{{ docsVersionInfo.kofVersions.kofOciRegistryBaseIstio }}}/charts/k0rdent-istio-base --version 0.1.0
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
  {{{ docsVersionInfo.kofVersions.kofOciRegistryBaseIstio }}}/charts/k0rdent-istio --version 0.1.0
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

#### Restore VictoriaMetrics/Logs Data

Follow the restore steps in the [Data Backup](../docs/admin/kof/kof-upgrade.md#data-backup) section to import backups into VM/VL.

## Upgrade to v1.4.0

* `PromxyServerGroup` CRD was moved from the `crds/` directory to the `templates/` directory for auto-upgrade.
* Please use `--take-ownership` on upgrade of `kof-mothership` to 1.4.0:
    ```bash
    helm upgrade --take-ownership \
      --reset-values --wait -n kof kof-mothership -f mothership-values.yaml \
      {{{ docsVersionInfo.kofVersions.kofOciRegistryBase }}}/charts/kof-mothership --version 1.4.0
    ```
* This will not be required in future upgrades.

## Upgrade to v1.3.0

Before upgrading any helm chart:

* If you have customized [VMCluster or VMAlert resources](https://github.com/k0rdent/kof/blob/v1.2.1/charts/kof-mothership/values.yaml#L169)
    then update your resources accordingly to the [new values under "spec"](https://github.com/k0rdent/kof/blob/v1.3.0/charts/kof-mothership/values.yaml#L167).

* If you have customized VMCluster/VMAlert resources using the "k0rdent.mirantis.com/kof-storage-values" cluster annotation, then keep the old but put new values first to reconcile the new `ClusterDeployment` configuration on the current release, **then** run the helm charts upgrade. After regional clusters have the new `kof-storage` helm chart installed, you can remove old values from the cluster annotation.
* If you have set `storage` values of the `kof-regional` chart, update them in the same way.

* If you are not using [Istio](../docs/admin/kof/kof-install.md#istio),
    then on the step 8 of the [Management Cluster](../docs/admin/kof/kof-install.md#management-cluster) upgrade
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

---

## Upgrade to v1.1.0

* After you `helm upgrade` the `kof-mothership` chart, please run the following:
    ```bash
    kubectl apply --server-side --force-conflicts \
    -f https://github.com/grafana/grafana-operator/releases/download/v5.18.0/crds.yaml
    ```
* After you get `regional-kubeconfig` file on the [KOF Verification](../docs/admin/kof/kof-verification.md) step,
  please run the following for each regional cluster:
    ```bash
    KUBECONFIG=regional-kubeconfig kubectl apply --server-side --force-conflicts \
    -f https://github.com/grafana/grafana-operator/releases/download/v5.18.0/crds.yaml
    ```
* This is noted as required in the [grafana-operator release notes](https://github.com/grafana/grafana-operator/releases/tag/v5.18.0).
<!--upgrade-end-->