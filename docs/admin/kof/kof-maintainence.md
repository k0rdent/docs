# Maintaining KOF

## Backup Requirements

Backing up KOF requires backing up the following:

* Grafana configurations
* Alert definitions
* Custom dashboards
* Retention policies

## Health Monitoring

To implement health monitoring:

1. Apply the steps in the [Verification](./kof-verification.md) section
2. Apply the steps in the [Sveltos](./kof-verification.md#sveltos) section

## Uninstallation

To remove the demo clusters created in this section:

> WARNING:
> Make sure these are just your demo clusters and do not contain important data.

```bash
kubectl delete --wait --cascade=foreground -f child-cluster.yaml
kubectl delete --wait --cascade=foreground -f regional-cluster.yaml
```

To remove KOF from the management cluster:

```bash
helm uninstall --wait --cascade foreground -n istio-system kof-istio
helm uninstall --wait --cascade foreground -n kof kof-child
helm uninstall --wait --cascade foreground -n kof kof-regional
helm uninstall --wait --cascade foreground -n kof kof-collectors
helm uninstall --wait --cascade foreground -n kof kof-storage
helm uninstall --wait --cascade foreground -n kof kof-mothership
helm uninstall --wait --cascade foreground -n kof kof-operators
kubectl delete namespace kof --wait --cascade=foreground
```
