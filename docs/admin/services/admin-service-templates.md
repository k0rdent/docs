# Using and Creating ServiceTemplates: Creating and Deploying Applications

Deploying an application, like deploying a cluster, involves applying a template to the management cluster. Rather than a `ClusterTemplate`, however, applications are deployed using a `ServiceTemplate`.

You can find more information on [Bringing Your Own Templates](../../reference/template/template-byo.md)
in the Template Guide, but this section gives you an idea of how to create a `ServiceTemplate`
and use it to deploy an application to a {{{ docsVersionInfo.k0rdentName }}} child cluster.

The basic sequence looks like this:

  1. Define the source of the Helm chart that defines the service. The source object must have the label `k0rdent.mirantis.com/managed: "true"`. For example, this YAML describes a custom `Source` object of `kind` `HelmRepository`:

    ```yaml
    apiVersion: source.toolkit.fluxcd.io/v1
    kind: HelmRepository
    metadata:
      name: custom-templates-repo
      namespace: kcm-system
      labels:
        k0rdent.mirantis.com/managed: "true"
    spec:
      insecure: true
      interval: 10m0s
      provider: generic
      type: oci
      url: oci://ghcr.io/external-templates-repo/charts
    ```

  2. Create the `ServiceTemplate`

    A template can either define a Helm chart directly using the template's `spec.helm.chartSpec` field or reference its location using the `spec.helm.chartRef` field.

    For example:

    ```yaml
    apiVersion: k0rdent.mirantis.com/v1alpha1
    kind: ServiceTemplate
    metadata:
      name: project-ingress-nginx-4.11.3
      namespace: my-target-namespace
    spec:
      helm:
        chartSpec:
          chart: ingress-nginx
          version: 4.11.3
          interval: 10m0s
          sourceRef:
            kind: HelmRepository
            name: k0rdent-catalog
    ```

    In this case, we're creating a `ServiceTemplate` called `ingress-nginx-4.11.3` in the
    `my-target-namespace` namespace.  It references version 4.11.3 of the `ingress-nginx` chart
    located in the `k0rdent-catalog` Helm repository.

    For more information on creating templates, see the [Template Guide](../../reference/template/index.md).

  3. Create a `ServiceTemplateChain`

    To let {{{ docsVersionInfo.k0rdentName }}} know where this `ServiceTemplate` can and can't be used, create a `ServiceTemplateChain` object, as in:

    ```yaml
    apiVersion: k0rdent.mirantis.com/v1alpha1
    kind: ServiceTemplateChain
    metadata:
      name: project-ingress-nginx-4.11.3
      namespace: my-target-namespace
    spec:
      supportedTemplates:
        - name: project-ingress-nginx-4.11.3
        - name: project-ingress-nginx-4.10.0
          availableUpgrades:
            - name: project-ingress-nginx-4.11.3
    ```

    Here you see a template called `project-ingress-nginx-4.11.3` that is meant to be deployed in the `my-target-namespace` namespace.
    The `.spec.helm.chartSpec` specifies the name of the Helm chart and where to find it, as well as the version and other 
    important information. The `ServiceTempateChain` shows that this template is also an upgrade path from version 4.10.0.

    If you wanted to deploy this as an application, you would first go ahead and add it to the cluster in which you were
    working, so if you were to save this YAML to a file called `project-ingress.yaml` you could run this command on the management cluster:

    ```shell
    kubectl apply -f project-ingress.yaml -n my-target-namespace
    ```

  4. Adding a `Service` to a `ClusterDeployment`

    To add the service defined by this template to a cluster, you would simply add it to the `ClusterDeployment` object
    when you create it, as in:

    ```yaml
    apiVersion: k0rdent.mirantis.com/v1alpha1
    kind: ClusterDeployment
    metadata:
      name: my-cluster-deployment
      namespace: tenant42
    spec:
      config:
        clusterLabels: {}
      template: aws-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsStandaloneCpCluster }}}
      credential: aws-credential
      serviceSpec:
        services:
          - template: project-ingress-nginx-4.11.3
            name: ingress-nginx
            namespace: my-target-namespace
        priority: 100
    ```
    As you can see, you're simply referencing the template in the `.spec.serviceSpec.services[].template` field of the `ClusterDeployment`
    to tell {{{ docsVersionInfo.k0rdentName }}} that you want this service to be part of this cluster.

    If you wanted to add this service to an existing cluster, you would simply patch the definition of the `ClusterDeployment`, as in:

    ```shell
    kubectl patch clusterdeployment my-cluster-deployment -n my-target-namespace --type='merge' -p '{"spec":{"services":[{"template":"project-ingress-nginx-4.11.3","name":"ingress-nginx","namespace":"my-target-namespace"}]}}'
    ```
    For more information on creating and using `ServiceTemplate` objects, see the [User Guide](../../user/services/index.md).
