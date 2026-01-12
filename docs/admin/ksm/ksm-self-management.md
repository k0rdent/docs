# Deploy beach-head services on Management Cluster itself

To deploy beach-head services on the management cluster, a MultiClusterService object can be created with `.spec.serviceSpec.provider.selfManagement=true` as shown below: 

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: MultiClusterService
metadata:
  name: mgmt-mcs
spec:
  serviceSpec:
    provider:
      name: ksm-projectsveltos
      selfManagement: true
    services:
      - template: ingress-nginx-4-11-3
        name: ingress-nginx
        namespace: ingress-nginx
```

This will create a ServiceSet which will also have `.spec.serviceSpec.provider.selfManagement=true`, which in-turn will indicate to the KSM [StateManagementProvider](ksm-providers.md) that this MCS is supposed to match the management cluster itself. 

The default StateManagementProvider is Sveltos, so there is a SveltosCluster object named mgmt in the mgmt namespace of the cluster where k0rdent has been installed. This object represents the management cluster itself. To view this object run:

```sh
kubectl -n mgmt get sveltoscluster mgmt --show-labels
```

The output should be similar to this:

```sh
NAME   READY   VERSION   LABELS
mgmt   true    v1.32.2   k0rdent.mirantis.com/management-cluster=true,projectsveltos.io/k8s-version=v1.32.2,sveltos-agent=present
```

Any number of ServiceTemplates (ingress-nginx-4-11-3 in this example) can be added to the MultiClusterService's `.spec.serviceSpec.services` field. See [Using and Creating ServiceTemplates](./ksm-service-templates.md) for how to create ServiceTemplates.

To verify that the ingress-nginx-4-11-3 beach-head service was sucessfully deployed, the status of the MultiClusterService can be queried with:

```sh
kubectl get multiclusterservice mgmt -o yaml
```

The output should be similar to the following showing that ingress-nginx has been Provisioned:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: MultiClusterService
metadata: {}
spec: {}
status:
  conditions:
    - lastTransitionTime: "2025-11-07T23:25:25Z"
      message: ""
      observedGeneration: 2
      reason: Succeeded
      status: "True"
      type: ServicesReferencesValidation
    - lastTransitionTime: "2025-11-07T23:25:25Z"
      message: ""
      observedGeneration: 2
      reason: Succeeded
      status: "True"
      type: ServicesDependencyValidation
    - lastTransitionTime: "2025-11-07T23:25:25Z"
      message: ""
      observedGeneration: 2
      reason: Succeeded
      status: "True"
      type: MultiClusterServiceDependencyValidation
    - lastTransitionTime: "2025-11-07T23:28:44Z"
      message: 1/1
      reason: Succeeded
      status: "True"
      type: ClusterInReadyState
    - lastTransitionTime: "2025-11-07T23:28:44Z"
      message: Object is ready
      reason: Succeeded
      status: "True"
      type: Ready
  observedGeneration: 2
  servicesUpgradePaths:
    - availableUpgrades:
        - upgradePaths:
            - ingress-nginx-4-11-3
      name: ingress-nginx
      namespace: ingress-nginx
      template: ingress-nginx-4-11-3
```

See [Creating multi-cluster services](./ksm-multiclusterservice.md) for more detail on deploying beach-head services using MultiClusterService.
