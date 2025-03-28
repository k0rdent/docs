# Architecture

## High-level

From a high-level perspective, KOF consists of three layers:

* the Collection layer, where the statistics and events are gathered,
* the Regional layer, which includes storage to keep track of those statistics and events,
* and the Management layer, where you interact through the UI.

```mermaid
flowchart TD;
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
  kof-mothership chart
    grafana-operator
    victoria-metrics-operator
    cluster-api-visualizer
    sveltos-dashboard
    kof-operator
    {{{ docsVersionInfo.k0rdentName }}} service templates
    promxy

  kof-operators chart
    opentelemetry-operator
    prometheus-operator-crds

  kof-regional chart
    MultiClusterService

  kof-child chart
    MultiClusterService

Cloud 1..N
  Region 1..M

    <b>Regional Cluster</b>
      kof-storage chart
        grafana-operator
        victoria-metrics-operator
        victoria-logs-single
        jaeger-operator
        external-dns

      cert-manager of grafana and vmauth
      ingress-nginx

    <b>Child Cluster 1</b>
      cert-manager of OTel-operator

      kof-operators chart
        opentelemetry-operator
          OpenTelemetryCollector
        prometheus-operator-crds

      kof-collectors chart
        opencost
        kube-state-metrics
        prometheus-node-exporter

      observed objects
-->

<div class="o">
  <b>Management Cluster</b>
  <div class="o">
    kof-mothership chart
    <div class="o">
      grafana-operator
    </div>
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
      kof-operator
    </div>
    <div class="o">
      {{{ docsVersionInfo.k0rdentName }}} service templates
    </div>
    <div class="o">
      promxy
    </div>
  </div>
  <div class="o">
    kof-operators chart
    <div class="o">
      opentelemetry-operator
    </div>
    <div class="o">
      prometheus-operator-crds
    </div>
  </div>
  <div class="o">
    kof-regional chart
    <div class="o">
      MultiClusterService
    </div>
  </div>
  <div class="o">
    kof-child chart
    <div class="o">
      MultiClusterService
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
        kof-storage chart
        <div class="o">
          grafana-operator
        </div>
        <div class="o">
          victoria-metrics-operator
        </div>
        <div class="o">
          victoria-logs-single
        </div>
        <div class="o">
          jaeger-operator
        </div>
        <div class="o">
          external-dns
        </div>
      </div>
      <div class="o">
        cert-manager of grafana and vmauth
      </div>
      <div class="o">
        ingress-nginx
      </div>
    </div>
    <div class="o">
      <b>Child Cluster 1</b>
      <div class="o">
        cert-manager of OTel-operator
      </div>
      <div class="o">
        kof-operators chart
        <div class="o">
          opentelemetry-operator
          <div class="o">
            OpenTelemetryCollector
          </div>
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
          kube-state-metrics
        </div>
        <div class="o">
          prometheus-node-exporter
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

## Low-level

At a low level, you can see how logs and traces work their way around the system.

![kof-architecture](../../assets/kof/otel.png)

## Helm Charts

KOF is deployed as a series of Helm charts at various levels.

### kof-mothership

- Centralized [Grafana](https://grafana.com/) dashboard, managed by [grafana-operator](https://github.com/grafana/grafana-operator)
- Local [VictoriaMetrics](https://victoriametrics.com/) storage for alerting rules only, managed by [victoria-metrics-operator](https://docs.victoriametrics.com/operator/)
- [cluster-api-visualizer](https://github.com/Jont828/cluster-api-visualizer) for insight into multicluster configuration
- [Sveltos](https://projectsveltos.github.io/sveltos/) dashboard, automatic secret distribution
- [kof-operator](https://github.com/k0rdent/kof/tree/main/kof-operator/internal/controller) (don't confuse it with the `kof-operators` chart) for auto-configuration
- [{{{ docsVersionInfo.k0rdentName }}}](https://github.com/k0rdent) service templates used by `kof-regional` and `kof-child` charts
- [Promxy](https://github.com/jacksontj/promxy) for aggregating Prometheus metrics from regional clusters

### kof-regional

- [MultiClusterService](https://github.com/k0rdent/kof/blob/d0baccd068f08f0f1d95ae0a26173176d106d284/charts/kof-regional/templates/regional-multi-cluster-service.yaml)
  which configures and installs `kof-storage` and other charts to regional clusters

### kof-child

- [MultiClusterService](https://github.com/k0rdent/kof/blob/d0baccd068f08f0f1d95ae0a26173176d106d284/charts/kof-child/templates/child-multi-cluster-service.yaml)
  which configures and installs `kof-collectors` and other charts to child clusters

### kof-storage

- Regional [Grafana](https://grafana.com/) dashboard, managed by [grafana-operator](https://github.com/grafana/grafana-operator)
- Regional [VictoriaMetrics](https://victoriametrics.com/) storage with main data, managed by [victoria-metrics-operator](https://docs.victoriametrics.com/operator/)
    - [vmauth](https://docs.victoriametrics.com/vmauth/) entrypoint proxy for VictoriaMetrics components
    - [vmcluster](https://docs.victoriametrics.com/operator/resources/vmcluster/) for high-available fault-tolerant version of VictoriaMetrics database
    - [victoria-logs-single](https://github.com/VictoriaMetrics/helm-charts/tree/master/charts/victoria-logs-single) for high-performance, cost-effective, scalable logs storage
- Regional [Jaeger](https://www.jaegertracing.io/) tracing platform, managed by [jaeger-operator](https://github.com/jaegertracing/jaeger-operator)
- [external-dns](https://github.com/kubernetes-sigs/external-dns) to communicate with other clusters

### kof-istio

- Optional [Istio](https://github.com/k0rdent/kof/blob/main/docs/istio.md) support for secure connectivity between clusters

### kof-operators

- [prometheus-operator-crds](https://github.com/prometheus-community/helm-charts/tree/main/charts/prometheus-operator-crds) required to create OpenTelemetry collectors, also required to monitor [`kof-mothership`](#management-cluster) itself
- [OpenTelemetry](https://opentelemetry.io/) [collectors](https://opentelemetry.io/docs/collector/) below, managed by [opentelemetry-operator](https://opentelemetry.io/docs/kubernetes/operator/)

### kof-collectors

- [prometheus-node-exporter](https://prometheus.io/docs/guides/node-exporter/) for hardware and OS metrics
- [kube-state-metrics](https://github.com/kubernetes/kube-state-metrics) for metrics about the state of Kubernetes objects
- [OpenCost](https://www.opencost.io/) "shines a light into the black box of Kubernetes spend"
