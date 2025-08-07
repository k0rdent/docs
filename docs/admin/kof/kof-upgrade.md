# Upgrading KOF

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
    ```shell
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
    ```shell
    kubectl apply --server-side --force-conflicts \
    -f https://github.com/grafana/grafana-operator/releases/download/v5.18.0/crds.yaml
    ```
* After you get `regional-kubeconfig` file on the [KOF Verification](./kof-verification.md) step,
  please run the following for each regional cluster:
    ```shell
    KUBECONFIG=regional-kubeconfig kubectl apply --server-side --force-conflicts \
    -f https://github.com/grafana/grafana-operator/releases/download/v5.18.0/crds.yaml
    ```
* This is noted as required in the [grafana-operator release notes](https://github.com/grafana/grafana-operator/releases/tag/v5.18.0).
