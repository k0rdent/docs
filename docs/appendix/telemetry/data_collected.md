# What’s collected (at a glance)

The KCM controller periodically scrapes each managed cluster and records:

* **Fleet/size**: number of nodes, total CPU (cores) and memory, total GPU units
  (AMD + NVIDIA).
* **Per-node profile**: OS, architecture, kernel, Kubernetes version, and
  flavor (e.g., k0s).
* **GPU details**: capacity per vendor and GPU requests aggregated from pods;
  whether NVIDIA/AMD GPU operators are installed; count of pods requesting GPUs.
* **Virtualization**: number of [KubeVirt](https://kubevirt.io/) VMIs.
* **Template and sync info**: [ClusterTemplate](../../reference/crds/index.md#clustertemplate)'s
  name, chart version, sync mode, providers used by the template.
* **User Services**: number of services defined in [ClusterDeployment](../../reference/crds/index.md#clusterdeployment)
  and [MultiClusterService](../../reference/crds/index.md#multiclusterservice) objects.
* **Identification labels**: cluster namespaced name,
  [ClusterDeployment](../../reference/crds/index.md#clusterdeployment) UID,
  and k0s cluster ID.

The exact metrics and their representation vary from the mode.

## Mode-specific nuances

* **Online mode**: each event carries a Segment *AnonymousId* equal
  to the Management UID.
  Segment client context includes: **KCM build commit/name/version**,
  **system namespace**, **runtime OS/arch**, and **timezone**.
* **Local mode**: data is written to a **daily-rotated JSON file**
  under a base directory, with a top-level
  `clusters` array containing per-cluster `counters` and `labels`.
  Metrics are represented as counters; hence, some of the `online`
  mode's metrics are flattened or omitted due to high cardinality
  such as **per-node profile**.
