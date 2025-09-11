# Upgrading KOF

## Upgrade to any version

* Open the latest version of the [Installing KOF](kof-install.md) guide.
* Make sure you see the expected new version in the top navigation bar.
* Go to the directory with YAML files created the last time you've applied the guide.
* Create their backup copies:
    ```shell
    for file in *.yaml; do cp $file $file.bak; done
    ```
* If you don't have such files, you may get them like this:
    ```shell
    helm get values -n kof kof-mothership -o yaml > mothership-values.yaml.bak
    ```
* Ideally, [create a backup](../backup/index.md) of everything including VictoriaMetrics/Logs data volumes.
* Apply the guide step by step, but:
    * Skip unchanged credentials like `external-dns-aws-credentials`.
    * Verify how YAML files have changed with `diff -u $file.bak $file` before using them.
    * Run all `helm upgrade` commands with the new `--version` and files as documented.
* Do the same for other [KOF guides](index.md#guides).
* Apply each relevant "Upgrade to" section of this page from older to newer.
    * For example, if you're upgrading from v1.1.0 to v1.3.0,
    * first apply the [Upgrade to v1.2.0](#upgrade-to-v120) section,
    * then apply the [Upgrade to v1.3.0](#upgrade-to-v130) section.

## Upgrade to v1.3.0

* If you are not using [Istio](kof-install.md#istio),
    then on the step 8 of the [Management Cluster](kof-install.md#management-cluster) upgrade
    please apply this temporary workaround for the [Reconciling MultiClusterService](https://github.com/k0rdent/kcm/issues/1914) issue:
    ```shell
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
