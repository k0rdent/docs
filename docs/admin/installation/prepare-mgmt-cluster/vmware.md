# vSphere

To enable users to deploy child clusers on vSphere, follow these steps:

1. Create a k0rdent management cluster

    Follow the instructions in [Install k0rdent](../install-k0rdent.md) to create a management cluster with k0rdent running, as well as a local install of `kubectl`.

2. Install a vSphere instance version `6.7.0` or higher.

3. Create a vSphere account with appropriate privileges

    To function properly, the user assigned to the vSphere Provider should be able
    to manipulate vSphere resources. The user should have the following 
    required privileges:

    ```shell
    Virtual machine: Full permissions are required
    Network: Assign network is sufficient
    Datastore: The user should be able to manipulate virtual machine files and metadata
    ```

    In addition to that, specific CSI driver permissions are required. See
    [the official doc](https://docs.vmware.com/en/VMware-vSphere-Container-Storage-Plug-in/2.0/vmware-vsphere-csp-getting-started/GUID-0AB6E692-AA47-4B6A-8CEA-38B754E16567.html)
    for more information on CSI-specific permissions.

4. Image template

    You can use pre-built image templates from the
    [CAPV project](https://github.com/kubernetes-sigs/cluster-api-provider-vsphere/blob/main/README.md#kubernetes-versions-with-published-ovas)
    or build your own.

    When building your own image, make sure that VMware tools and cloud-init are
    installed and properly configured.

    You can follow the [official open-vm-tools guide](https://docs.vmware.com/en/VMware-Tools/11.0.0/com.vmware.vsphere.vmwaretools.doc/GUID-C48E1F14-240D-4DD1-8D4C-25B6EBE4BB0F.html)
    on how to correctly install VMware tools.

    When setting up cloud-init, you can refer to the [official docs](https://cloudinit.readthedocs.io/en/latest/index.html)
    and specifically the [VMware datasource docs](https://cloudinit.readthedocs.io/en/latest/reference/datasources/vmware.html)
    for extended information regarding cloud-init on vSphere.

5. vSphere network

    When creating a network, make sure that it has the DHCP service.

    Also, ensure that part of your network is out of the DHCP range (for example, the network
    `172.16.0.0/24` should have a DHCP range of `172.16.0.100-172.16.0.254` only) so that LoadBalancer services will not create any IP conflicts in the
    network.

6. vSphere Credentials

    To enable k0rdent to access vSphere resources, create the appropriate credentials objects. For a full explanation of how `Credential` objects work, see the [main Credentials chapter](../../access/credentials/index.md), but for now, follow these steps:

    Create a `Secret` object with the username and password

    The `Secret` stores the username and password for your vSphere instance. Save the `Secret` YAML in a file named `vsphere-cluster-identity-secret.yaml`:

    ```yaml
    apiVersion: v1
    kind: Secret
    metadata:
      name: vsphere-cluster-identity-secret
      namespace: kcm-system
      labels:
        k0rdent.mirantis.com/component: "kcm"
    stringData:
      username: <USERNAME>
      password: <PASSWORD>
    type: Opaque
    ```

    Apply the YAML to your cluster:

    ```shell
    kubectl apply -f vsphere-cluster-identity-secret.yaml
    ```

7. Create the `VSphereClusterIdentity` Object

    The `VSphereClusterIdentity` object defines the credentials CAPV will use to manage vSphere resources.

    Save the `VSphereClusterIdentity` YAML into a file named `vsphere-cluster-identity.yaml`:

    ```yaml
    apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
    kind: VSphereClusterIdentity
    metadata:
      name: vsphere-cluster-identity
      namespace: kcm-system
      labels:
        k0rdent.mirantis.com/component: "kcm"
    spec:
      secretName: vsphere-cluster-identity-secret
      allowedNamespaces:
        selector:
          matchLabels: {}
    ```

    The `VSphereClusterIdentity` object references the `Secret` you created in the previous step, so `.spec.secretName` 
    needs to match the `.metadata.name` for the `Secret`.

    Apply the YAML to your cluster:

    ```shell
    kubectl apply -f vsphere-cluster-identity.yaml
    ```

8. Create the `Credential` Object

    Create a YAML with the specification of our credential and save it as
    `vsphere-cluster-identity-cred.yaml`

    ```yaml
    apiVersion: k0rdent.mirantis.com/v1alpha1
    kind: Credential
    metadata:
      name: vsphere-cluster-identity-cred
      namespace: kcm-system
    spec:
      identityRef:
        apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
        kind: VSphereClusterIdentity
        name: vsphere-cluster-identity
        namespace: kcm-system
    ```
    Again, `.spec.identityRef.name` must match the `.metadata.name` of the `VSphereClusterIdentity` object you just created.

    Apply the YAML to your cluster:

    ```shell
    kubectl apply -f vsphere-cluster-identity-cred.yaml
    ```

9. Create the `ConfigMap` resource-template Object

    Create a YAML with the specification of our resource-template and save it as
    `vsphere-cluster-identity-resource-template.yaml`

    ```yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: vsphere-cluster-identity-resource-template
      namespace: kcm-system
      labels:
        k0rdent.mirantis.com/component: "kcm"
      annotations:
        projectsveltos.io/template: "true"
    data:
      configmap.yaml: |
        {{- $cluster := .InfrastructureProvider -}}
        {{- $identity := (getResource "InfrastructureProviderIdentity") -}}
        {{- $secret := (getResource "InfrastructureProviderIdentitySecret") -}}
        ---
        apiVersion: v1
        kind: Secret
        metadata:
          name: vsphere-cloud-secret
          namespace: kube-system
        type: Opaque
        data:
          {{ printf "%s.username" $cluster.spec.server }}: {{ index $secret.data "username" }}
          {{ printf "%s.password" $cluster.spec.server }}: {{ index $secret.data "password" }}
        ---
        apiVersion: v1
        kind: Secret
        metadata:
          name: vcenter-config-secret
          namespace: kube-system
        type: Opaque
        stringData:
          csi-vsphere.conf: |
            [Global]
            cluster-id = "{{ $cluster.metadata.name }}"

            [VirtualCenter "{{ $cluster.spec.server }}"]
            insecure-flag = "true"
            user = "{{ index $secret.data "username" | b64dec }}"
            password = "{{ index $secret.data "password" | b64dec }}"
            port = "443"
            datacenters = ${VSPHERE_DATACENTER}
        ---
        apiVersion: v1
        kind: ConfigMap
        metadata:
          name: cloud-config
          namespace: kube-system
        data:
          vsphere.conf: |
            global:
              insecureFlag: true
              port: 443
              secretName: vsphere-cloud-secret
              secretNamespace: kube-system
            labels:
              region: k8s-region
              zone: k8s-zone
            vcenter:
              {{ $cluster.spec.server }}:
                datacenters:
                  - ${VSPHERE_DATACENTER}
                server: {{ $cluster.spec.server }}
    ```
    Object name needs to be exactly `vsphere-cluster-identity-resource-template`, `VSphereClusterIdentity` object name + `-resource-template` string suffix.

    Apply the YAML to your cluster:

    ```shell
    kubectl apply -f vsphere-cluster-identity-resource-template.yaml
    ```

10. Create your first Cluster Deployment

    Test the configuration by deploying a cluster. Create a YAML document with the specification of your Cluster Deployment and save it as `my-vsphere-clusterdeployment1.yaml`.

    You can get a list of available templates:


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

    The `ClusterDeployment` YAML file should look something like this. Make sure to replace the placeholders with your
    specific information:

    ```yaml
    apiVersion: k0rdent.mirantis.com/v1alpha1
    kind: ClusterDeployment
    metadata:
      name: my-vsphere-clusterdeployment1
      namespace: kcm-system
    spec:
      template: vsphere-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.vsphereStandaloneCpCluster }}}
      credential: vsphere-cluster-identity-cred
      config:
        clusterLabels: {}
        controlPlaneNumber: 1
        workersNumber: 1
        vsphere:
          server: <VSPHERE_SERVER>
          thumbprint: <VSPHERE_THUMBPRINT>
          datacenter: <VSPHERE_DATACENTER>
          datastore: <VSPHERE_DATASTORE>
          resourcePool: <VSPHERE_RESOURCEPOOL>
          folder: <VSPHERE_FOLDER>
          username: ${VSPHERE_USER}
          password: ${VSPHERE_PASSWORD}
        controlPlaneEndpointIP: <VSPHERE_CONTROL_PLANE_ENDPOINT>
        controlPlane:
          ssh:
            user: ubuntu
            publicKey: <VSPHERE_SSH_KEY>
          rootVolumeSize: 50
          cpus: 4
          memory: 4096
          vmTemplate: <VSPHERE_VM_TEMPLATE>
          network: <VSPHERE_NETWORK>
        worker:
          ssh:
            user: ubuntu
            publicKey: <VSPHERE_SSH_KEY>
          rootVolumeSize: 50
          cpus: 4
          memory: 4096
          vmTemplate: <VSPHERE_VM_TEMPLATE>
          network: <VSPHERE_NETWORK>
    ```

    For more information about the available configuration options, see the [vSphere Template Parameters](../../../reference/template/template-openstack.md).

    Apply the YAML to your management cluster:

    ```shell
    kubectl apply -f my-vsphere-clusterdeployment1.yaml
    ```

    There will be a delay as the cluster finishes provisioning. Follow the
    provisioning process with the following command:

    ```shell
    kubectl -n kcm-system get clusterdeployment.k0rdent.mirantis.com my-vsphere-clusterdeployment1 --watch
    ```

    After the cluster is `Ready`, you can access it via the kubeconfig, like this:

    ```shell
    kubectl -n kcm-system get secret my-vsphere-clusterdeployment1-kubeconfig -o jsonpath='{.data.value}' | base64 -d > my-vsphere-clusterdeployment1-kubeconfig.kubeconfig
    KUBECONFIG="my-vsphere-clusterdeployment1-kubeconfig.kubeconfig" kubectl get pods -A
    ```

11. Cleanup

    To delete the provisioned cluster and free consumed vSphere resources run:

    ```shell
    kubectl -n kcm-system delete cluster my-vsphere-clusterdeployment1
    ```
