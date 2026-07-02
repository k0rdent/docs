# KOF Tracing

KOF uses VictoriaTraces as the backend for distributed tracing. Traces are collected via OpenTelemetry and stored in VictoriaTraces, which provides efficient long-term storage and querying capabilities.

## Configuration

Tracing is enabled by default in KOF. The VictoriaTraces configuration can be customized in your `kof-storage` values.

For available configuration options, refer to the VictoriaTraces values:
[VictoriaTraces Cluster Helm Chart](https://docs.victoriametrics.com/helm/victoriatraces-cluster/#parameters)

### Auto-instrumentation

To get basic traces:

1. Apply [OpenTelemetry Zero-code](https://opentelemetry.io/docs/concepts/instrumentation/zero-code/) guide for your app's language.

    For example, a Go executable can be instrumented like this:

    ```yaml
    kind: Deployment
    spec:
      template:
        metadata:
          annotations:
            instrumentation.opentelemetry.io/inject-go: "true"
            instrumentation.opentelemetry.io/otel-go-auto-target-exe: "/path-to-executable"
    ```

    Full Python app example and more options can be found in the advanced [Traces](https://github.com/k0rdent/kof/blob/main/docs/traces.md) guide.

2. Check that the pod was restarted and got a sidecar injected.
3. [Verify the traces](#accessing-traces).

### Instrumentation with SDK

To get advanced traces:

1. Select and use [OpenTelemetry SDK](https://opentelemetry.io/docs/languages/) for your app's language.

    For example, `kof-operator` was instrumentated with SDK in [k0rdent/kof PR #1029](https://github.com/k0rdent/kof/pull/1029).

    ??? note "If you don't see any traces"

        If you don't see any traces but you see `traces export: exporter export timeout`
        in `kubectl logs -n kof deploy/kof-mothership-kof-operator`
        this means `kof-operator` finished all its tasks before `opentelemetry-operator`
        made traces receiver ready.

        You can generate a new test trace by asking `kof-operator` to reconcile something,
        for example:

        ```bash
        kubectl label configmap -n kof kof-record-rules-default test-1=reconcile-and-trace
        ```

2. [Verify the traces](#accessing-traces).

## Accessing Traces

Apply [Using KOF - Traces](kof-using.md#traces)
or [Grafana in KOF - Traces](kof-grafana.md#traces).
