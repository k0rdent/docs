# Architecture

## High-level

From a high-level perspective, KOF consists of three layers:

* the Collection layer, where the statistics and events are gathered,
* the Regional layer, which includes storage to keep track of those statistics and events,
* and the Management layer, where you interact through the UI.

```mermaid
flowchart TD
    A[Management UI, promxy] 
    A --> C[Storage Region 1]
    A --> D[Storage Region 2]
    C --> E[Collect Child 1]
    C --> F[Collect Child 2]
    D ==> G[...]
```

## Mid-level

Getting a little bit more detailed, it's important to undrestand that data flows upwards,
from observed objects to centralized Grafana on the Management layer:

<!--

To update the diagram:
* Update the indented text below.
* Copy/paste it to https://codepen.io/denis-ryzhkov/pen/ByajZeJ
* Copy the resulting HTML.
* Please preserve custom `max-width: 30em;` in the end.

<b>Management Cluster</b>
  kof-operators chart
    grafana-operator
    opentelemetry-operator
    prometheus-operator-crds

  kof-mothership chart
    victoria-metrics-operator
    cluster-api-visualizer
    sveltos-dashboard
    dex
    {{{ docsVersionInfo.k0rdentName }}} service templates
    kof-dashboards
    kof-operator
    promxy

  kof-collectors chart
    opencost
    opentelemetry-kube-stack

  Either kof-istio
    Certificates
    ClusterProfiles
  Or kof-regional and kof-child
    MultiClusterServices

Cloud 1..N
  Region 1..M

    <b>Regional Cluster</b>
      kof-operators chart
        grafana-operator
        opentelemetry-operator
        prometheus-operator-crds

      kof-storage chart
        victoria-metrics-operator
        victoria-logs-cluster
        external-dns
        jaeger-operator
        dex
        kof-dashboards

      kof-collectors chart
        opencost
        opentelemetry-kube-stack

      cert-manager
      ingress-nginx
      istio/gateway

      kof-istio chart
        cert-manager-istio-csr
        istio/base
        istiod

    <b>Child Cluster 1</b>
      cert-manager
      Optional kof-istio

      kof-operators chart
        Disabled grafana-operator
        opentelemetry-operator
        prometheus-operator-crds

      kof-collectors chart
        opencost
        opentelemetry-kube-stack

      observed objects
-->

<div class="o">
  <b>Management Cluster</b>
  <div class="o">
    kof-operators chart
    <div class="o">
      grafana-operator
    </div>
    <div class="o">
      opentelemetry-operator
    </div>
    <div class="o">
      prometheus-operator-crds
    </div>
  </div>
  <div class="o">
    kof-mothership chart
    <div class="o">
      victoria-metrics-operator
    </div>
    <div class="o">
      cluster-api-visualizer
    </div>
    <div class="o">
      sveltos-dashboard
    </div>
    <div class="o">
      dex
    </div>
    <div class="o">
      {{{ docsVersionInfo.k0rdentName }}} service templates
    </div>
    <div class="o">
      kof-dashboards
    </div>
    <div class="o">
      kof-operator
    </div>
    <div class="o">
      promxy
    </div>
  </div>
  <div class="o">
    kof-collectors chart
    <div class="o">
      opencost
    </div>
    <div class="o">
      opentelemetry-kube-stack
    </div>
  </div>
  <div class="o">
    Either kof-istio
    <div class="o">
      Certificates
    </div>
    <div class="o">
      ClusterProfiles
    </div>
  </div>
  <div class="o">
    Or kof-regional and kof-child
    <div class="o">
      MultiClusterServices
    </div>
  </div>
</div>
<div class="o">
  Cloud 1..N
  <div class="o">
    Region 1..M
    <div class="o">
      <b>Regional Cluster</b>
      <div class="o">
        kof-operators chart
        <div class="o">
          grafana-operator
        </div>
        <div class="o">
          opentelemetry-operator
        </div>
        <div class="o">
          prometheus-operator-crds
        </div>
      </div>
      <div class="o">
        kof-storage chart
        <div class="o">
          victoria-metrics-operator
        </div>
        <div class="o">
          victoria-logs-cluster
        </div>
        <div class="o">
          external-dns
        </div>
        <div class="o">
          jaeger-operator
        </div>
        <div class="o">
          dex
        </div>
        <div class="o">
          kof-dashboards
        </div>
      </div>
      <div class="o">
        kof-collectors chart
        <div class="o">
          opencost
        </div>
        <div class="o">
          opentelemetry-kube-stack
        </div>
      </div>
      <div class="o">
        cert-manager
      </div>
      <div class="o">
        ingress-nginx
      </div>
      <div class="o">
        istio/gateway
      </div>
      <div class="o">
        kof-istio chart
        <div class="o">
          cert-manager-istio-csr
        </div>
        <div class="o">
          istio/base
        </div>
        <div class="o">
          istiod
        </div>
      </div>
    </div>
    <div class="o">
      <b>Child Cluster 1</b>
      <div class="o">
        cert-manager
      </div>
      <div class="o">
        Optional kof-istio
      </div>
      <div class="o">
        kof-operators chart
        <div class="o">
          Disabled grafana-operator
        </div>
        <div class="o">
          opentelemetry-operator
        </div>
        <div class="o">
          prometheus-operator-crds
        </div>
      </div>
      <div class="o">
        kof-collectors chart
        <div class="o">
          opencost
        </div>
        <div class="o">
          opentelemetry-kube-stack
        </div>
      </div>
      <div class="o">
        observed objects
      </div>
    </div>
  </div>
</div>

<style>
  .o {
    margin: 0.25em 1em;
    background-color: rgba(128, 128, 128, 0.25);
    padding: 0.25em 0.5em;
    max-width: 30em;
  }
</style>

## Helm Charts

KOF is deployed as a series of Helm charts at various levels.

### kof-operators

- [Grafana](https://grafana.com/) dashboards platform, managed by [grafana-operator](https://github.com/grafana/grafana-operator)
- [OpenTelemetry](https://opentelemetry.io/) [collectors](https://opentelemetry.io/docs/collector/) below, managed by [opentelemetry-operator](https://opentelemetry.io/docs/kubernetes/operator/)
- [prometheus-operator-crds](https://github.com/prometheus-community/helm-charts/tree/main/charts/prometheus-operator-crds) required to create OpenTelemetry collectors, also required to monitor [`kof-mothership`](#kof-mothership) itself

### kof-mothership

- Local [VictoriaMetrics](https://victoriametrics.com/) storage for alerting rules only, managed by [victoria-metrics-operator](https://docs.victoriametrics.com/operator/)
- [cluster-api-visualizer](https://github.com/Jont828/cluster-api-visualizer) for insight into multicluster configuration
- [Sveltos](https://projectsveltos.github.io/sveltos/) dashboard, automatic secret distribution
- [Dex](https://dexidp.io/) SSO [chart](https://github.com/dexidp/helm-charts/tree/master/charts/dex)
- [{{{ docsVersionInfo.k0rdentName }}}](https://github.com/k0rdent) service templates used by `kof-regional` and `kof-child` charts
- [kof-dashboards](https://github.com/k0rdent/kof/tree/v{{{ extra.docsVersionInfo.kofVersions.kofDotVersion }}}/charts/kof-dashboards) for Grafana
- [kof-operator](https://github.com/k0rdent/kof/tree/v{{{ extra.docsVersionInfo.kofVersions.kofDotVersion }}}/kof-operator/internal/controller) (don't confuse it with the `kof-operators` chart) for auto-configuration
- [Promxy](https://github.com/jacksontj/promxy) for aggregating Prometheus metrics from regional clusters

### kof-regional

- [MultiClusterService](https://github.com/k0rdent/kof/blob/v{{{ extra.docsVersionInfo.kofVersions.kofDotVersion }}}/charts/kof-regional/templates/regional-multi-cluster-service.yaml)
  which configures and installs `kof-storage` and other charts to regional clusters

### kof-child

- [MultiClusterService](https://github.com/k0rdent/kof/blob/v{{{ extra.docsVersionInfo.kofVersions.kofDotVersion }}}/charts/kof-child/templates/child-multi-cluster-service.yaml)
  which configures and installs `kof-collectors` and other charts to child clusters

### kof-istio

- Optional [Istio](https://istio.io/) support for secure connectivity between clusters without external DNS

### kof-storage

- Regional [VictoriaMetrics](https://victoriametrics.com/) storage with main data, managed by [victoria-metrics-operator](https://docs.victoriametrics.com/operator/)
  - [vmauth](https://docs.victoriametrics.com/vmauth/) entrypoint proxy for VictoriaMetrics components
  - [vmcluster](https://docs.victoriametrics.com/operator/resources/vmcluster/) for high-available fault-tolerant version of VictoriaMetrics database
  - [victoria-logs-cluster](https://github.com/VictoriaMetrics/helm-charts/tree/master/charts/victoria-logs-cluster) for high-performance, cost-effective, scalable logs storage
- [external-dns](https://github.com/kubernetes-sigs/external-dns) to communicate with other clusters
- [Jaeger](https://www.jaegertracing.io/) tracing platform, managed by [jaeger-operator](https://github.com/jaegertracing/jaeger-operator)
- [Dex](https://dexidp.io/) SSO [chart](https://github.com/dexidp/helm-charts/tree/master/charts/dex)
- [kof-dashboards](https://github.com/k0rdent/kof/tree/v{{{ extra.docsVersionInfo.kofVersions.kofDotVersion }}}/charts/kof-dashboards) for Grafana

### kof-collectors

- [opentelemetry-kube-stack](https://github.com/open-telemetry/opentelemetry-helm-charts/tree/main/charts/opentelemetry-kube-stack) for hardware, OS, and Kubernetes metrics
- [OpenCost](https://www.opencost.io/) "shines a light into the black box of Kubernetes spend"
