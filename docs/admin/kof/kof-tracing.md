# KOF Tracing

KOF uses VictoriaTraces as the backend for distributed tracing. Traces are collected via OpenTelemetry and stored in VictoriaTraces, which provides efficient long-term storage and querying capabilities.

## Accessing Traces

Apply [Using KOF - Traces](kof-using.md#traces)
or [Grafana in KOF - Traces](kof-grafana.md#traces).

## Configuration

Tracing is enabled by default in KOF. The VictoriaTraces configuration can be customized in your `kof-storage` values.

For available configuration options, refer to the VictoriaTraces values:
[VictoriaTraces Cluster Helm Chart](https://docs.victoriametrics.com/helm/victoriatraces-cluster/#parameters)
