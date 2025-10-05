# Checking status

The `.status.services` field of the `ClusterDeployment` object shows the status for each of the beach-head services.
For example, if you were to `describe` the `ClusterDeployment` with these services, you would see conditions that show
status information, as in:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ClusterDeployment
metadata:
  . . .
  generation: 1
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
    - name: kyverno
      namespace: kyverno
      template: kyverno-3-2-6
    . . .
status:
  . . .
  observedGeneration: 1
  services:
  - clusterName: my-cluster-deployment
    clusterNamespace: kcm-system
    conditions:
    - lastTransitionTime: "2024-12-11T23:03:05Z"
      message: ""
      reason: Provisioned
      status: "True"
      type: Helm
    - lastTransitionTime: "2024-12-11T23:03:05Z"
      message: Release kyverno/kyverno
      reason: Managing
      status: "True"
      type: kyverno.kyverno/SveltosHelmReleaseReady
    - lastTransitionTime: "2024-12-11T23:03:05Z"
      message: Release ingress-nginx/ingress-nginx
      reason: Managing
      status: "True"
      type: ingress-nginx.ingress-nginx/SveltosHelmReleaseReady
```

Based on the information above both kyverno and ingress-nginx are installed in their respective namespaces on the target cluster.
You can check to see for yourself:

```bash
kubectl get pod -n kyverno
```
```console { .no-copy }
NAME                                             READY   STATUS    RESTARTS   AGE
kyverno-admission-controller-96c5d48b4-sg5ts     1/1     Running   0          2m39s
kyverno-background-controller-65f9fd5859-tm2wm   1/1     Running   0          2m39s
kyverno-cleanup-controller-848b4c579d-ljrj5      1/1     Running   0          2m39s
kyverno-reports-controller-6f59fb8cd6-s8jc8      1/1     Running   0          2m39s
```
```bash
kubectl get pod -n ingress-nginx 
```
```console { .no-copy }
NAME                                       READY   STATUS    RESTARTS   AGE
ingress-nginx-controller-cbcf8bf58-zhvph   1/1     Running   0          24m
```

Youc an get more information on how to access the child cluster in the [create a cluster deployment](../../admin/clusters/deploy-cluster.md)
chapter, and more on `ServiceTemplate` objects in the [Template Guide](../../reference/template/index.md).
