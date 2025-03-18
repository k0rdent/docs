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
    k0rdent service templates
    promxy

  kof-operators chart
    opentelemetry-operator
    prometheus-operator-crds

Cloud 1..N
  Region 1..M

    <b>Regional Cluster</b>
      kof-storage chart
        grafana-operator
        victoria-metrics-operator
        victoria-logs-single
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
      k0rdent service templates
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
