# Scaling Guidelines

The method for scaling KOF depends on the type of expansion:

## Increase volumes size

**Don't use this method** if your storage class doesn't have [allowVolumeExpansion](https://kubernetes.io/docs/concepts/storage/storage-classes/#allow-volume-expansion).

With allowVolumeExpansion you can increase the storage size for:

??? note "vmcluster"

    ```yaml
    kof-regional: # or kof-mothership if you have it installed on mothership cluster
      values:
        victoriametrics:
          vmcluster:
            spec:
              vmstorage:
                storage:
                  volumeClaimTemplate:
                    spec:
                      resources:
                        requests:
                          storage: <new size>
    ```

??? note "victoria-logs-cluster"

    ```yaml
    victoria-logs-cluster:
      vlstorage:
        persistentVolume:
          size: <new size>
    ```

    ```yaml
    victoria-traces-cluster:
      vtstorage:
        persistentVolume:
          size: <new size>
    ```
    
For **vmcluster** you can just run helm upgrade with new values, VictoriaMetrics operator will handle volume expansion automatically.

{%
    include-markdown "../../../includes/kof-install-includes.md"
    start="<!--install-kof-start-->"
    end="<!--install-kof-end-->"
%}

For **victoria-logs-cluster and victoria-traces-cluster** you need to delete the stateful set and expand PVCs manually before running helm upgrade:

??? note "victoria-logs-cluster volumes expansion"

    0. If you have installed the kof-storage chart on the mothership cluster via kof-umbrella helm chart, suspend the flux helmrelease firstly
    ```bash
    kubectl patch helmrelease kof-storage \
    -n kof \
    --type=merge \
    -p '{"spec":{"suspend": true}}'
    ```

    1. Delete the current stateful set:
    ```bash
    # --cascade=orphan keeps the Pods and PVCs alive while removing the StatefulSet object
    kubectl delete statefulset kof-storage-victoria-logs-cluster-vlstorage \
      -n kof --cascade=orphan
    ```
    
    2. Expand the size **for each** PVC from 0 to the number of replicas
    ```bash
    kubectl patch pvc vlstorage-volume-kof-storage-victoria-logs-cluster-vlstorage-0 \
    -n kof \
    --type=merge \
    -p '{"spec":{"resources":{"requests":{"storage":"<new size>"}}}}'
    ```

    3. Verify that PVCs are expanded
    ```bash
    kubectl get pvc -n kof -w
    ```

    4. Run helm upgrade with values set to the new size

## Regional Expansion

1. Deploy a [regional cluster](./kof-install.md#regional-cluster) in the new region.
2. Configure child clusters in this region to point to this regional cluster.

## Adding a New Child Cluster

1. Apply templates, as in the [child cluster](./kof-install.md#child-cluster) section.
2. Verify the data flow.
3. Configure any custom dashboards.

## You Must Construct Additional Pylons

1. Change the `replicaCount` of components like `victoria-logs-cluster`
    as documented in the [regional cluster](./kof-install.md#regional-cluster) section.
2. Change the `replicas` number of components like `opencost`
    as documented in the [child cluster](./kof-install.md#child-cluster) section.
