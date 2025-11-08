# Resource Requirements

## System Overview

Let's assume the `kof` regional storage cluster consists of three nodes configured for fault tolerance.
All nodes must have identical hardware configurations to ensure consistent performance.

## Hardware Requirements

Each node in the cluster must meet the following hardware specifications:

**Minimal requirements:**
For development and testing purposes.

| Component   | Requirement |
| ----------- | ----------- |
| **CPU**     | 2 Cores     |
| **RAM**     | 4 GB        |
| **Storage** | 25 GB       |

**Recommended Requirements:**
For production usage.

| Component   | Requirement |
| ----------- | ----------- |
| **CPU**     | 3 Cores     |
| **RAM**     | 5 GB        |
| **Storage** | 30 GB       |

### Storage Requirements

Storage capacity may need to be expanded depending on the volume of logs and metrics collected. The estimates below provide guidance for the Victoria components:

#### Victoria Logs Storage

For Victoria Logs storage, every **1 million logs** is estimated to require approximately **25 MB** of storage in the `emptyDir` volume of the `victoria-logs-cluster-vlstorage` pod.

#### Victoria Metrics Storage

For Victoria Metrics storage, every **100 million metrics** is estimated to require roughly **50 MB** of storage in the `vmstorage-db` PVC.

**Note**: These estimates are approximate and may vary based on workload and environmental factors. To ensure stability, consider provisioning an additional storage margin.

#### Persistent Volume Claims (PVC) Details

By default, the following PVCs are deployed across the nodes:

* **vmstorage-db**: 10Gi per node
Each node is provisioned with its own `vmstorage-db` PVC for storing Victoria Metrics data.
* **vmselect-cachedir**: 2Gi per node
Each node has a dedicated `vmselect-cachedir` PVC for caching in VMSelect.
* **grafana-vm-pvc**: 1Gi
Used for regional components such as Grafana.

## Recommendations for Cluster Scaling

To ensure optimal performance of your cluster under high load, it is recommended to:

* **Resource Monitoring**: Regularly track key metrics such as CPU usage, memory consumption, disk I/O, and data ingestion rates to promptly identify the need for scaling.

* **Review Documentation and Benchmarks**: Consult the official documentation and performance test results to determine the optimal resources for your workload.

Detailed recommendations on resource planning and scaling are available in the official VictoriaMetrics documentation:

* [Understanding your setup size](https://docs.victoriametrics.com/guides/understand-your-setup-size/)

* [Cluster resizing and scalability](https://docs.victoriametrics.com/cluster-victoriametrics/#cluster-resizing-and-scalability)

* [Benchmarks](https://docs.victoriametrics.com/articles/#benchmarks)

## Resources of Opentemetry Collectors

- [collectors](https://github.com/k0rdent/kof/blob/9577d59796fa27fa51c1b755b11648376aae4d74/charts/kof-collectors/values.yaml#L42)

Check the `resources` section for each collector. The required resources depend on the configuration and the amount of data collected and processed via configured pipelines.

1. The `cluster` collector receives the k8s events, so its resources depend on the k8s cluster size and number of events.
2. The `target-allocator` collector watches monitoring custom resources like Prometheus `ServiceMonitors`, so its resources depend on the scale of workloads across the cluster.
3. The `daemon` collector runs on each node and mostly reads pod logs, so its resources depend on the number of pods and the total amount of logs on each node.
4. The `controller-k0s` collector has hardcoded scrape configs for k0s control plane nodes; the amount of resources depends on the control plane logging and metrics configuration.


## Resources of Management Cluster

- [promxy](https://github.com/k0rdent/kof/blob/9577d59796fa27fa51c1b755b11648376aae4d74/charts/kof-mothership/values.yaml#L451-L462):

Memory consumption depends on the number of metric data points returned by the query. This amount of memory is enough to fetch ~500K datapoints.

  ```yaml
  resources:
    requests:
      cpu: 100m
      memory: 512Mi
    limits:
      cpu: 100m
      memory: 512Mi
  ```

- [kof-operator](https://github.com/k0rdent/kof/blob/9577d59796fa27fa51c1b755b11648376aae4d74/charts/kof-mothership/values.yaml#L102-L111):

Resource utilization depends on the number of KOF clusters; this is a good starting point.

  ```yaml
  resources:
    limits:
      cpu: 100m
      memory: 128Mi
    requests:
      cpu: 100m
      memory: 128Mi
  ```

## Resources of a Child Cluster

- [opentelemetry](https://github.com/k0rdent/kof/blob/9577d59796fa27fa51c1b755b11648376aae4d74/charts/kof-collectors/values.yaml#L14-L18):

Resource utilization depends on the workload runtime and the image pulled for autoinstrumentation. The recommendation is to observe and adjust accordingly. Default values are:

  ```yaml
  resourceRequirements:
    limits:
      memory: 512Mi
    requests:
      memory: 512Mi
  ```

## Why VictoriaMetrics instead of Prometheus?

KOF uses VictoriaMetrics as the metrics backend, rather than Prometheus alone, for several reasons.

- Scalability: VictoriaMetrics supports horizontal clustering for large multi-cluster environments.
- Compression: VictoriaMetrics stores high-cardinality metrics efficiently.
- Federation: VictoriaMetrics integrates cleanly with Promxy for cross-cluster queries.

We still use Prometheus at the collection layer, but long-term storage and query efficiency are handled by VictoriaMetrics.
