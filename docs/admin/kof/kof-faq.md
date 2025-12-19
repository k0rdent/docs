# KOF FAQ & Scenarios

## What is full‑stack observability in KOF?
OpenTelemetry collects metrics, logs, and traces; data is stored in VictoriaMetrics, VictoriaLogs, and VictoriaTraces, and visualized in Grafana.

## How do I collect telemetry from a new service?

There are two ways to collect telemetry from a new service:

* Prometheus scrape annotations: Add scrape annotations to your pods so metrics are collected automatically.
* Auto-instrumentation: Let KOF inject the OpenTelemetry language agent into your pods at runtime.

For example, let's say you were adding auto-instrumentation to a Java Spring Boot service.  You'd follow these steps:

1. Enable instrumentation in **your application's** Helm chart values:
   ```yaml
   kof:
     instrumentation:
       enabled: true
       language: java
   ```
2. The Helm flag `kof.instrumentation.enabled=true` makes sure the necessary CRDs from the OpenTelemetry Operator are present in the cluster, but you still need to configure the actual application. When you deploy, add the appropriate annotation:
   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: my-java-service
     namespace: demo
   spec:
     replicas: 1
     selector:
       matchLabels:
         app: my-java-service
     template:
       metadata:
         labels:
           app: my-java-service
         annotations:
           instrumentation.opentelemetry.io/inject-java: "true"
       spec:
         containers:
         - name: app
           image: myregistry/my-java-service:1.0.0
           ports:
           - containerPort: 8080
   ```

   With this annotation, KOF automatically injects the OpenTelemetry Java agent. The service then exports metrics, traces, and logs through the configured OpenTelemetry Collector.

3. After deploying, you should see:
   - Traces in VictoriaTraces (via Grafana datasource)
   - Metrics in VictoriaMetrics (via Grafana dashboards)  
   - Logs in VictoriaLogs

For other languages, use the appropriate annotation, as in:

- Python: `instrumentation.opentelemetry.io/inject-python: "true"`
- Node.js: `instrumentation.opentelemetry.io/inject-nodejs: "true"`

## How should I manage dashboards?
Treat dashboards as code. Edit YAML under `charts/kof-dashboards/files/dashboards/*` and deploy via Helm/CI/CD. Avoid editing in the Grafana UI, as those changes will be overwritten.

## How do I avoid commingling tenant data?
Deploy collectors/storage per tenant namespace and restrict access with RBAC. This ensures separation of data paths per tenant.

## How do I control retention policies?
Configure the `retentionPeriod` for VictoriaMetrics and VictoriaLogs. You can find more information in [KOF Retention](./kof-retention.md).