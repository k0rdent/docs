# Upgrading {{{ docsVersionInfo.k0rdentName }}}

IMPORTANT: When upgrading to K0rdent `0.2.0` follow this [instruction](upgrade-to-0-2-0.md) and perform
additional manual steps.

Upgrading {{{ docsVersionInfo.k0rdentName }}} involves making upgrades to the `Management` object. To do that, you must have the `Global Admin` role. (For detailed information about {{{ docsVersionInfo.k0rdentName }}} RBAC roles and permissions, refer to the [RBAC documentation](../access/rbac/index.md).) Follow these steps to upgrade {{{ docsVersionInfo.k0rdentName }}}:

1. Create a new `Release` object

    Start by creating a `Release` object in the management cluster that points to the desired version. You can see
    available versions at [https://github.com/k0rdent/kcm/releases](https://github.com/k0rdent/kcm/releases).  The actual
    `Release` object includes information on the templates and resources that are available, as well as the version of the
    Kubernetes Cluster API.  For example, the v{{{ extra.docsVersionInfo.k0rdentDotVersion }}} `Release` object looks like this:

    ```yaml
    apiVersion: k0rdent.mirantis.com/v1alpha1
    kind: Release
    metadata:
      name: kcm-{{{ extra.docsVersionInfo.k0rdentVersion }}}
      annotations:
        helm.sh/resource-policy: keep
    spec:
      version: {{{ extra.docsVersionInfo.k0rdentDotVersion }}}
      kcm:
        template: kcm-{{{ extra.docsVersionInfo.k0rdentVersion }}}
      capi:
        template: cluster-api-{{{ extra.docsVersionInfo.k0rdentVersion }}}
      providers:
        - name: k0smotron
          template: k0smotron-{{{ extra.docsVersionInfo.k0rdentVersion }}}
        - name: cluster-api-provider-azure
          template: cluster-api-provider-azure-{{{ extra.docsVersionInfo.k0rdentVersion }}}
        - name: cluster-api-provider-vsphere
          template: cluster-api-provider-vsphere-{{{ extra.docsVersionInfo.k0rdentVersion }}}
        - name: cluster-api-provider-aws
          template: cluster-api-provider-aws-{{{ extra.docsVersionInfo.k0rdentVersion }}}
        - name: cluster-api-provider-openstack
          template: cluster-api-provider-openstack-{{{ extra.docsVersionInfo.k0rdentVersion }}}
        - name: projectsveltos
          template: projectsveltos-0-45-0
    ```

    Thankfully, you don't have to build these YAML files yourself. Once you've chosen a release, you can go ahead and create the release object by referencing the YAML file online, as in:

    ```shell
    VERSION=v{{{ extra.docsVersionInfo.k0rdentDotVersion }}}
    kubectl create -f https://github.com/k0rdent/kcm/releases/download/${VERSION}/release.yaml
    ```

2. List Available `Releases`

    Once you've created the new `Release` you need to update the `Management` object to use it. Start by viewing all available `Release`s:

    ```shell
    kubectl get releases
    ```

    ```console
    NAME        AGE
    kcm-0-0-6   71m
    kcm-0-0-7   65m
    kcm-{{{ extra.docsVersionInfo.k0rdentVersion }}}   12m
    ```

3. Patch the `Management` object with the new `Release`

    Update the `spec.release` field in the `Management` object to point to the new release. Replace `<release-name>` with the name of your desired release:

    ```shell
    RELEASE_NAME=kcm-{{{ extra.docsVersionInfo.k0rdentVersion }}}
    kubectl patch managements.k0rdent.mirantis.com kcm --patch "{\"spec\":{\"release\":\"${RELEASE_NAME}\"}}" --type=merge
    ```

4. Verify the Upgrade

    Although the change will be made immediately, it will take some time for {{{ docsVersionInfo.k0rdentName }}} to update the components it should be
    using. Monitor the readiness of the `Management` object to ensure the upgrade was successful. For example:

    ```shell
    kubectl get managements.k0rdent.mirantis.com kcm
    NAME   READY   RELEASE     AGE
    kcm    True    kcm-{{{ extra.docsVersionInfo.k0rdentVersion }}}   4m34s
    ```
