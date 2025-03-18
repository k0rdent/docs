# Understanding ServiceTemplates

`ServiceTemplate` objects are meant to let k0rdent know where to find a Helm chart with instructions for installing
an application. In many cases, these charts will be in a private repository.  For example, consider this template for
installing Nginx Ingress:

```yaml
apiVersion: k0rdent.mirantis.com/v1alpha1
kind: ServiceTemplate
metadata:
  name: project-ingress-nginx-4.11.0
  namespace: tenant42
spec:
  helm:
    chartSpec:
      chart: demo-ingress-nginx
      version: 4.11.0
      interval: 10m0s
      sourceRef:
        kind: HelmRepository
        name: k0rdent-demos
---
apiVersion: k0rdent.mirantis.com/v1alpha1
kind: ServiceTemplateChain
metadata:
  name: project-ingress-nginx-4.11.0
  namespace: tenant42
spec:
  supportedTemplates:
    - name: project-ingress-nginx-4.11.0
    - name: project-ingress-nginx-4.10.0
      availableUpgrades:
        - name: project-ingress-nginx-4.11.0
```

Here you see a template called `project-ingress-nginx-4.11.0` that is meant to be deployed in the `tenant42` namespace.
The `.spec.helm.chartSpec` specifies the name of the Helm chart and where to find it, as well as the version and other 
important information. The `ServiceTemplateChain` shows that this template is also an upgrade path from version 4.10.0.

If you wanted to deploy this as an application, you would first go ahead and add the template to the cluster in which you were working, so if you were to save this YAML to a file called `project-ingress.yaml` you could run this command on the management cluster:

```shell
kubectl apply -f project-ingress.yaml -n tenant42
```
