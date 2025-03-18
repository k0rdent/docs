# Resource Limits

See also: [System Requirements](https://github.com/k0rdent/kof/blob/main/docs/system-requirements.md).

## Resources of Management Cluster

- [promxy](https://github.com/k0rdent/kof/blob/121b61f5f6de6ddfdf3525b98f3ad4cb8ce57eaa/charts/kof-mothership/values.yaml#L120-L126):
  ```yaml
  resources:
    requests:
      cpu: 100m
      memory: 128Mi
    limits:
      cpu: 100m
      memory: 128Mi
  ```

- [promxy-deployment](https://github.com/k0rdent/kof/blob/121b61f5f6de6ddfdf3525b98f3ad4cb8ce57eaa/charts/kof-mothership/templates/promxy/promxy-deployment.yaml#L107-L113):
  ```yaml
  resources:
    requests:
      cpu: 0.02
      memory: 20Mi
    limits:
      cpu: 0.02
      memory: 20Mi
  ```

- [promxy-operator](https://github.com/k0rdent/kof/blob/121b61f5f6de6ddfdf3525b98f3ad4cb8ce57eaa/promxy-operator/config/manager/manager.yaml#L87-L93):
  ```yaml
  resources:
    limits:
      cpu: 500m
      memory: 128Mi
    requests:
      cpu: 10m
      memory: 64Mi
  ```

## Resources of a Child Cluster

- [opentelemetry](https://github.com/k0rdent/kof/blob/121b61f5f6de6ddfdf3525b98f3ad4cb8ce57eaa/charts/kof-collectors/templates/opentelemetry/instrumentation.yaml#L18-L22):
  ```yaml
  resourceRequirements:
    limits:
      memory: 128Mi
    requests:
      memory: 128Mi
  ```
