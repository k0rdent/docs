# Parameter List

Here is an idea of the parameters involved.

| Parameter                                 | Example                | Description                                                                                   |
|-------------------------------------------|------------------------|-----------------------------------------------------------------------------------------------|
| `.spec.serviceSpec.syncMode`              | `Continuous`           | Specifies how beach-head services are synced i the target cluster (default:`Continuous`)      |
| `.spec.serviceSpec.DriftIgnore`           |                        | specifies resources to ignore for drift detection                                             |
| `.spec.serviceSpec.DriftExclusions`       |                        | specifies specific configurations of resources to ignore for drift detection                  |
| `.spec.serviceSpec.priority`              | `100`                  | Sets the priority for the beach-head services defined in this spec (default: `100`)           |
| `.spec.serviceSpec.stopOnConflict`        | `false`                | Stops deployment of beach-head services upon first encounter of a conflict (default: `false`) |
| `.spec.serviceSpec.services[].template`   | `kyverno-3-2-6`        | Name of the `ServiceTemplate` object located in the same namespace                            |
| `.spec.serviceSpec.services[].name`       | `my-kyverno-release`   | Release name for the beach-head service                                                       |
| `.spec.serviceSpec.services[].namespace`  | `my-kyverno-namespace` | Release namespace for the beach-head service (default: `.spec.services[].name`)               |
| `.spec.serviceSpec.services[].values`     | `replicas: 3`          | Helm values to be used with the template while deployed the beach-head services               |
| `.spec.serviceSpec.services[].valuesFrom` | ``                     | Can reference a ConfigMap or Secret containing helm values                                    |
| `.spec.serviceSpec.services[].disable`    | `false`                | Disable handling of this beach-head service (default: `false`)                                |