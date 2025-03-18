# Removing beach-head services

To remove a beach-head service simply remove its entry from `.spec.serviceSpec.services`.
The example below removes `kyverno-3-2-6`, so its status also removed from `.status.services`.

```yaml
apiVersion: k0rdent.mirantis.com/v1alpha1
kind: ClusterDeployment
metadata:
  . . .
  generation: 2
  name: wali-aws-dev
  namespace: kcm-system
  . . .
spec:
  . . .
  serviceSpec:
    services:
    - name: ingress-nginx
      namespace: ingress-nginx
      template: ingress-nginx-4-11-3
    priority: 100
    . . .
status:
  . . .
  observedGeneration: 2
  services:
  - clusterName: wali-aws-dev
    clusterNamespace: kcm-system
    conditions:
    - lastTransitionTime: "2024-12-11T23:15:45Z"
      message: ""
      reason: Provisioned
      status: "True"
      type: Helm
    - lastTransitionTime: "2024-12-11T23:15:45Z"
      message: Release ingress-nginx/ingress-nginx
      reason: Managing
      status: "True"
      type: ingress-nginx.ingress-nginx/SveltosHelmReleaseReady
```
