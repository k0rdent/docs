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
