# Upgrading to {{{ docsVersionInfo.k0rdentName}}} 0.2.0

In {{{ docsVersionInfo.k0rdentName}}} 0.2.0, the `k0smotron` management component has been renamed to
`cluster-api-provider-k0sproject-k0smotron`. To safely upgrade from `0.1.0` to `0.2.0`, follow the upgrade guide
and perform the additional manual steps outlined below:

1. Follow the [upgrading guide](index.md) and create a new `Release` object (steps 1-2).

1. Verify the new `Release` status

    Wait for the new `Release` to have `status.ready: true`:

    ```shell
    kubectl wait --for=jsonpath='{.status.ready}=true' release/kcm-0-2-0
    ```

1. Manually delete the `k0smotron` providers (replace `kcm-system` with your system namespace):

    ```shell
    kubectl -n kcm-system delete infrastructureproviders.operator.cluster.x-k8s.io k0sproject-k0smotron
    kubectl -n kcm-system delete controlplaneproviders.operator.cluster.x-k8s.io k0sproject-k0smotron
    kubectl -n kcm-system delete bootstrapproviders.operator.cluster.x-k8s.io k0sproject-k0smotron
    ```

1. Instead of the step 3 from [Upgrading guide](index.md) you need to edit
   the `Management` object. Run:

    ```shell
    kubectl edit managements.k0rdent.mirantis.com kcm
    ```

    And do the following:

    * Set `spec.release` to `kcm-0-2-0`
    * In `spec.providers` rename the `k0smotron` provider to `cluster-api-provider-k0sproject-k0smotron`:

    ```shell
    providers:
    - name: cluster-api-provider-k0sproject-k0smotron
    ```

    The full example of the new Management spec:

    ```yaml
    apiVersion: k0rdent.mirantis.com/v1alpha1
    kind: Management
    metadata:
      labels:
        k0rdent.mirantis.com/component: kcm
      name: kcm
    spec:
      core:
        capi: {}
        kcm: {}
      providers:
      - name: cluster-api-provider-k0sproject-k0smotron
      - name: projectsveltos
      - name: cluster-api-provider-aws
      - name: cluster-api-provider-azure
      - name: cluster-api-provider-docker
      - name: cluster-api-provider-gcp
      - name: cluster-api-provider-openstack
      - name: cluster-api-provider-vsphere
      release: kcm-0-2-0
    ```

1. Follow the [Upgrading guide](index.md) and verify the upgrade (step 4).
