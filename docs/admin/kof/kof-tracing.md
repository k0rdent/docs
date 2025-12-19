# KOF Tracing

KOF uses VictoriaTraces as the backend for distributed tracing. Traces are collected via OpenTelemetry and stored in VictoriaTraces, which provides efficient long-term storage and querying capabilities.

## Accessing Traces

You can view and analyze traces through Grafana Explore:

1. Open Grafana in your browser
2. Navigate to **Explore** (compass icon in the left sidebar)
3. Select the **Jaeger** type datasource from the dropdown at the top
4. Use the query builder to search for traces by service name, operation, tags, or trace ID

## Configuration

Tracing is enabled by default in KOF. The VictoriaTraces configuration can be customized in your `kof-storage` values.

For available configuration options, refer to the VictoriaTraces values:
[VictoriaTraces Cluster Helm Chart](https://docs.victoriametrics.com/helm/victoriatraces-cluster/#parameters)
