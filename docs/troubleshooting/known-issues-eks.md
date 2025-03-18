# EKS Machines Are not Created: ControlPlaneIsStable Preflight Check Failed

[Related issue: KCM #907](https://github.com/k0rdent/kcm/issues/907)

The deployment of the EKS cluster is stuck waiting for the machines to be provisioned. The `MachineDeployment`
resource is showing the following conditions:

```shell
Type: MachineSetReady
Status: False
Reason: PreflightCheckFailed
Message: ekaz-eks-dev-eks-md: AWSManagedControlPlane kcm-system/ekaz-eks-dev-eks-cp is provisioning ("ControlPlaneIsStable" preflight check failed)
Type: Available
Status: False
Reason: WaitingForAvailableMachines
Message: ekaz-eks-dev-eks-md: Minimum availability requires 1 replicas, current 0 available
Type: Ready
Status: False
Reason: WaitingForAvailableMachines
Message: ekaz-eks-dev-eks-md: Minimum availability requires 1 replicas, current 0 available
```

As a result, the cluster was successfully created in EKS but no nodes are available.

**Workaround**

1. Edit the `MachineDeployment` object:
```bash
kubectl --kubeconfig <management-kubeconfig> edit MachineDeployment -n <cluster-namespace> <cluster-name>-md
```

1. Add `machineset.cluster.x-k8s.io/skip-preflight-checks: "ControlPlaneIsStable"` annotation to skip the
`ControlPlaneIsStable` preflight check:
```yaml
apiVersion: cluster.x-k8s.io/v1beta1
kind: MachineDeployment
metadata:
  annotations:
    meta.helm.sh/release-name: aws-eks-dev
    meta.helm.sh/release-namespace: kcm-system
    machineset.cluster.x-k8s.io/skip-preflight-checks: "ControlPlaneIsStable" # add new annotation
  name: aws-eks-dev-md
```

1. Save and exit
