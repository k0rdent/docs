# Pausing Beach-Head Services Reconciliation

To **pause reconciliation** of a beach-head service, add the following annotation to the `ServiceSet` object associated with your `ClusterDeployment`:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ServiceSet
metadata:
  name: example
  namespace: kcm-system
  annotations:
    k0rdent.mirantis.com/service-set-paused: "true"
  generation: 2
spec:
  ...
```

Once this annotation is applied, reconciliation for the specified beach-head service will be paused until the annotation is removed.