# OpenStack

{{{ docsVersionInfo.k0rdentName }}} can deploy child clusters on OpenStack virtual machines. Follow these steps to configure and deploy OpenStack clusters for your users:

1. Install {{{ docsVersionInfo.k0rdentName }}}

    Follow the instructions in [Install {{{ docsVersionInfo.k0rdentName }}}](../install-k0rdent.md) to create a management cluster with {{{ docsVersionInfo.k0rdentName }}} running.

2. OpenStack CLI (optional)

    If you plan to access OpenStack directly, go ahead and 
    [install the OpenStack CLI](https://docs.openstack.org/newton/user-guide/common/cli-install-openstack-command-line-clients.html).

3. Configure the OpenStack Application Credential

    The exported list of variables should include:

    ```shell
    OS_AUTH_URL
    OS_APPLICATION_CREDENTIAL_ID
    OS_APPLICATION_CREDENTIAL_SECRET
    OS_REGION_NAME
    OS_INTERFACE
    OS_IDENTITY_API_VERSION
    OS_AUTH_TYPE
    ```

    While it's possible to use a username and password instead of the Application Credential &mdash; adjust your YAML accordingly &mdash; an Application Credential is strongly recommended because it limits scope and improves security over a raw username/password approach.

4. Create the OpenStack Credentials Secret

    Create a Kubernetes `Secret` containing the `clouds.yaml` that defines your OpenStack environment, substituting real values
    where appropriate. Save this as `openstack-cloud-config.yaml`:

    ```yaml
    apiVersion: v1
    kind: Secret
    metadata:
      name: openstack-cloud-config
      namespace: kcm-system
      labels:
        k0rdent.mirantis.com/component: "kcm"
    stringData:
      clouds.yaml: |
        clouds:
          openstack:
            auth:
              auth_url: <OS_AUTH_URL>
              application_credential_id: <OS_APPLICATION_CREDENTIAL_ID>
              application_credential_secret: <OS_APPLICATION_CREDENTIAL_SECRET>
            region_name: <OS_REGION_NAME>
            interface: <OS_INTERFACE>
            identity_api_version: <OS_IDENTITY_API_VERSION>
            auth_type: <OS_AUTH_TYPE>
    ```

    Apply the YAML to your cluster:

    ```shell
    kubectl apply -f openstack-cloud-config.yaml
    ```

5. Create the {{{ docsVersionInfo.k0rdentName }}} Credential Object

    Next, define a `Credential` that references the `Secret` from the previous step.
    Save this as `openstack-cluster-identity-cred.yaml`:

    ```yaml
    apiVersion: k0rdent.mirantis.com/v1alpha1
    kind: Credential
    metadata:
      name: openstack-cluster-identity-cred
      namespace: kcm-system
      labels:
        k0rdent.mirantis.com/component: "kcm"  
    spec:
      description: "OpenStack credentials"
      identityRef:
        apiVersion: v1
        kind: Secret
        name: openstack-cloud-config
        namespace: kcm-system
    ```

    Apply the YAML to your cluster:

    ```shell
    kubectl apply -f openstack-cluster-identity-cred.yaml
    ```

    Note that `.spec.identityRef.name` must match the `Secret` you created in the previous step, and 
    `.spec.identityRef.namespace` must be the same as the one that includes the `Secret` (`kcm-system`).

6. Create the ConfigMap resource-template object

    Create a YAML file with the specification of the resource-template and save it as `openstack-cluster-identity-resource-template.yaml`:

    ```yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: openstack-cloud-config-resource-template
      namespace: kcm-system
      labels:
        k0rdent.mirantis.com/component: "kcm"
      annotations:
        projectsveltos.io/template: "true"
    data:
      configmap.yaml: |
        {{- $cluster := .InfrastructureProvider -}}
        {{- $identity := (getResource "InfrastructureProviderIdentity") -}}

        {{- $clouds := fromYaml (index $identity "data" "clouds.yaml" | b64dec) -}}
        {{- if not $clouds }}
          {{ fail "failed to decode clouds.yaml" }}
        {{ end -}}

        {{- $openstack := index $clouds "clouds" "openstack" -}}

        {{- if not (hasKey $openstack "auth") }}
          {{ fail "auth key not found in openstack config" }}
        {{- end }}
        {{- $auth := index $openstack "auth" -}}

        {{- $auth_url := index $auth "auth_url" -}}
        {{- $app_cred_id := index $auth "application_credential_id" -}}
        {{- $app_cred_name := index $auth "application_credential_name" -}}
        {{- $app_cred_secret := index $auth "application_credential_secret" -}}

        {{- $network_id := $cluster.status.externalNetwork.id -}}
        {{- $network_name := $cluster.status.externalNetwork.name -}}
        ---
        apiVersion: v1
        kind: Secret
        metadata:
          name: openstack-cloud-config
          namespace: kube-system
        type: Opaque
        stringData:
          cloud.conf: |
            [Global]
            auth-url="{{ $auth_url }}"

            {{- if $app_cred_id }}
            application-credential-id="{{ $app_cred_id }}"
            {{- end }}

            {{- if $app_cred_name }}
            application-credential-name="{{ $app_cred_name }}"
            {{- end }}

            {{- if $app_cred_secret }}
            application-credential-secret="{{ $app_cred_secret }}"
            {{- end }}

            {{- if and (not $app_cred_id) (not $app_cred_secret) }}
            username="{{ index $openstack "username" }}"
            password="{{ index $openstack "password" }}"
            {{- end }}
            region="{{ index $openstack "region_name" }}"

            [LoadBalancer]
            {{- if $network_id }}
            floating-network-id="{{ $network_id }}"
            {{- end }}

            [Networking]
            {{- if $network_name }}
            public-network-name="{{ $network_name }}"
            {{- end }}
    ```
    
    Object needs to be named `openstack-cluster-identity-resource-template.yaml`, `OpenStackClusterIdentity` object name + `-resource-template` string suffix.

    Apply the YAML to your cluster:

    ```shell
    kubectl apply -f openstack-cluster-identity-resource-template.yaml
    ```

7. Create Your First Child Cluster

    To test the configuration, create a YAML file with the specification of your Managed Cluster and save it as
    `my-openstack-cluster-deployment.yaml`.  Note that you can see the available templates by listing them:

    ```shell
    kubectl get clustertemplate -n kcm-system
    ```
    ```console
    NAME                            VALID
    adopted-cluster-{{{ extra.docsVersionInfo.k0rdentVersion }}}           true
    aws-eks-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsEksCluster }}}                   true
    aws-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsHostedCpCluster }}}             true
    aws-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsStandaloneCpCluster }}}         true
    azure-aks-{{{ extra.docsVersionInfo.providerVersions.dashVersions.azureAksCluster }}}                 true
    azure-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.azureHostedCpCluster }}}           true
    azure-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.azureStandaloneCpCluster }}}       true
    openstack-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.openstackStandaloneCpCluster }}}   true
    vsphere-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.vsphereHostedCpCluster }}}         true
    vsphere-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.vsphereStandaloneCpCluster }}}     true
    ```

    The `ClusterDeployment` should look something like this:

    ```yaml
    apiVersion: k0rdent.mirantis.com/v1alpha1
    kind: ClusterDeployment
    metadata:
      name: my-openstack-cluster-deployment
      namespace: kcm-system
    spec:
      template: openstack-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.openstackStandaloneCpCluster }}}
      credential: openstack-cluster-identity-cred
      config:
        clusterLabels: {}
        controlPlaneNumber: 1
        workersNumber: 1
        controlPlane:
          flavor: m1.medium
          image:
            filter:
              name: ubuntu-22.04-x86_64
        worker:
          flavor: m1.medium
          image:
            filter:
              name: ubuntu-22.04-x86_64
        externalNetwork:
          filter:
            name: "public"
        authURL: ${OS_AUTH_URL}
        identityRef:
          name: "openstack-cloud-config"
          cloudName: "openstack"
          region: ${OS_REGION_NAME}
    ```

    You can adjust `flavor`, `image name`, `region name`, and `authURL` to match your OpenStack environment. For more information about the configuration options, see the [OpenStack Template Parameters Reference](../../../reference/template/template-openstack.md).

    Apply the YAML to your management cluster:

    ```shell
    kubectl apply -f my-openstack-cluster-deployment.yaml
    ```

    This will trigger the provisioning process where {{{ docsVersionInfo.k0rdentName }}} will create a bunch of OpenStack resources such as OpenStackCluster, OpenStackMachineTemplate, OpenStackMachineDeployment, etc. You can follow the
    provisioning process:

    ```shell
    kubectl -n kcm-system get clusterdeployment.k0rdent.mirantis.com my-openstack-cluster-deployment --watch
    ```

    After the cluster is `Ready`, you can access it via the kubeconfig, just like any other Kubernetes cluster:

    ```shell
    kubectl -n kcm-system get secret my-openstack-cluster-deployment-kubeconfig -o jsonpath='{.data.value}' | base64 -d > my-openstack-cluster-deployment-kubeconfig.kubeconfig
    KUBECONFIG="my-openstack-cluster-deployment-kubeconfig.kubeconfig" kubectl get pods -A
    ```

8. Cleanup

    To clean up OpenStack resources, delete the managed cluster by deleting the `ClusterDeployment`:

    ```shell
    kubectl get clusterdeployments -A
    ```
    ```console
    NAMESPACE    NAME                          READY   STATUS
    kcm-system   my-openstack-cluster-deployment   True    ClusterDeployment is ready
    ```
    ```shell
    kubectl delete clusterdeployments my-openstack-cluster-deployment -n kcm-system
    ```
    ```console
    clusterdeployment.k0rdent.mirantis.com "my-openstack-cluster-deployment" deleted
    ```

