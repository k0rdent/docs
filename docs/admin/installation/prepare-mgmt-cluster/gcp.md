# GCP

*Available starting in {{{ docsVersionInfo.k0rdentName }}} 0.2.0 and later*

Standalone clusters can be deployed on GCP instances. Follow these steps to make GCP clusters available to your users:

1. Install {{{ docsVersionInfo.k0rdentName }}}

    Follow the instructions in [Install {{{ docsVersionInfo.k0rdentName }}}](../install-k0rdent.md) to create a management cluster with {{{ docsVersionInfo.k0rdentName }}} running.

2. The gcloud CLI

    The gcloud CLI (`gcloud`) is required to interact with GCP resources. You can install it by following 
    the [Install the gcloud CLI instructions](https://cloud.google.com/sdk/docs/install).

3. Log in to GCP

    Authenticate your session with GCP:

    ```bash
    gcloud auth login
    ```

4. Enable the required API for your Google Cloud project (if it wasn't previously enabled)

    The proper API to enable depends on how you plan to deploy {{{ docsVersionInfo.k0rdentName }}}:

    * Standalone/hosted GCP clusters: Enable the `Compute Engine API`.
    * GKE clusters: Enable the `Compute Engine API` and the `Kubernetes Engine API`.
    
    To enable `Compute Engine API` using the Google Cloud Console (UI):

    1. Go to the Google Cloud Console.
    2. Select your project. 
    3. In the top navigation bar, click on the project selector (drop-down menu). 
    4. Choose the project where you want to enable the `Compute Engine API`. 
    5. Navigate to the `API Library` (click on the Navigation Menu in the upper-left corner and select `APIs & Services` → `Library`). 
    6. Search for Compute Engine API (in the API Library, type `Compute Engine API` in the search bar and press Enter).
    7. Enable the API. Click on `Compute Engine API` from the search results. Click the `Enable` button.

5. Create a GCP Service Account

    > NOTE:
    > Skip this step if the Service Account already configured

    Follow the [GCP Service Account creation guide](https://cloud.google.com/iam/docs/service-accounts-create#creating)
    and create a new service account with `Editor` permissions.
    If you have plans to deploy `GKE`, the Service Account will also need the `iam.serviceAccountTokenCreator` role.

6. Generate a JSON Key for the GCP Service Account

    > NOTE:
    > Skip this step if you're going to use an existing key

    Follow the [Create a service account key guide](https://cloud.google.com/iam/docs/keys-create-delete#creating)
    and create a new key with the JSON key type.

    A JSON file will automatically download to your computer. Keep it somewhere safe.

    The example of the JSON file:

    ```bash
    {
      "type": "service_account",
      "project_id": "GCP_PROJECT_ID",
      "private_key_id": "GCP_PRIVATE_KEY_ID",
      "private_key": "-----BEGIN PRIVATE KEY-----\nGCP_PRIVATE_KEY\n-----END PRIVATE KEY-----\n",
      "client_email": "name@project_id.iam.gserviceaccount.com",
      "client_id": "GCP_CLIENT_ID",
      "auth_uri": "https://accounts.google.com/o/oauth2/auth",
      "token_uri": "https://oauth2.googleapis.com/token",
      "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
      "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/user%40project_id.iam.gserviceaccount.com",
      "universe_domain": "googleapis.com"
    }
    ```

7. Create a `Secret` object

    Create a `Secret` object that stores the credentials under `data` section. Create a YAML file called
    `gcp-cluster-identity-secret.yaml`, as follows, inserting the base64-encoded GCP credentials
    (represented by the placeholder `GCP_B64ENCODED_CREDENTIALS` below) that you get on the previous step.
    To get base64 encoded credentials, run:

    ```bash
    cat <gcpJSONCredentialsFileName> | base64 -w 0
    ```

    ```yaml
    apiVersion: v1
    kind: Secret
    metadata:
      name: gcp-cloud-sa
      namespace: kcm-system
      labels:
        k0rdent.mirantis.com/component: "kcm"
    data:
      # the secret key should always equal `credentials`
      credentials: GCP_B64ENCODED_CREDENTIALS
    type: Opaque
    ```

     You can then apply the YAML to your cluster:

     ```bash
     kubectl apply -f gcp-cluster-identity-secret.yaml
     ```

8. Create the {{{ docsVersionInfo.k0rdentName }}} `Credential` Object

    Create a YAML document with the specification of the `Credential` and save it as `gcp-cluster-identity-cred.yaml`.

    Note that `.spec.name` must match `.metadata.name` of the `Secret` object created in the previous step.

    ```yaml
    apiVersion: k0rdent.mirantis.com/v1beta1
    kind: Credential
    metadata:
      name: gcp-credential
      namespace: kcm-system
    spec:
      identityRef:
        apiVersion: v1
        kind: Secret
        name: gcp-cloud-sa
        namespace: kcm-system
    ```

    ```bash
    kubectl apply -f gcp-cluster-identity-cred.yaml
    ```

    You should see output of:

    ```console { .no-copy }
    credential.k0rdent.mirantis.com/gcp-cluster-identity-cred created
    ```

9. Create the `ConfigMap` resource-template Object

    Create a YAML with the specification of our resource-template and save it as
    `gcp-cloud-sa-resource-template.yaml`

    ```yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: gcp-cloud-sa-resource-template
      namespace: kcm-system
      labels:
        k0rdent.mirantis.com/component: "kcm"
      annotations:
        projectsveltos.io/template: "true"
    data:
      configmap.yaml: |
        {{- $secret := (getResource "InfrastructureProviderIdentity") -}}
        ---
        apiVersion: v1
        kind: Secret
        metadata:
          name: gcp-cloud-sa
          namespace: kube-system
        type: Opaque
        data:
          cloud-sa.json: {{ index $secret "data" "credentials" }}
    ```

    Object name needs to be exactly `gcp-cloud-sa-resource-template` (credentials `Secret` object name + `-resource-template` string suffix).

    Apply the YAML to your cluster:

    ```bash
    kubectl apply -f gcp-cloud-sa-resource-template.yaml
    ```
    ```console { .no-copy }
    configmap/gcp-cloud-sa-resource-template created
    ```

Now you're ready to deploy the cluster.

9. Create a `ClusterDeployment`

    To test the configuration, deploy a child cluster by following these steps:
    First get a list of available regions:

    ```bash
    gcloud compute regions list
    ```
    
    You'll see output like this:

    ```console { .no-copy }
    NAME                     CPUS    DISKS_GB  ADDRESSES  RESERVED_ADDRESSES  STATUS  TURNDOWN_DATE
    africa-south1            0/300   0/102400  0/575      0/175               UP
    asia-east1               0/3000  0/102400  0/575      0/175               UP
    asia-east2               0/1500  0/102400  0/575      0/175               UP
    asia-northeast1          0/1500  0/102400  0/575      0/175               UP
    asia-northeast2          0/750   0/102400  0/575      0/175               UP
    ...
    ```

    Make note of the region you want to use, such as `us-east4`.

     To create the actual child cluster, create a `ClusterDeployment` that references the appropriate template
     as well as the region, credentials, and cluster configuration.

     You can see the available templates by listing them:

     ```bash
     kubectl get clustertemplate -n kcm-system
     ```
     ```console { .no-copy }
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
     gcp-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.gcpStandaloneCpCluster }}}     true
     gcp-gke-{{{ extra.docsVersionInfo.providerVersions.dashVersions.gcpGkeCluster }}}     true
     ```

     Create the YAML for the `ClusterDeployment` and save it as my-gcp-clusterdeployment1.yaml:

     ```yaml
     apiVersion: k0rdent.mirantis.com/v1beta1
     kind: ClusterDeployment
     metadata:
       name: my-gcp-clusterdeployment1
       namespace: kcm-system
     spec:
       template: gcp-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.gcpStandaloneCpCluster }}}
       credential: gcp-credential
       config:
         project: PROJECT_NAME # Your project name
         region: "GCP_REGION" # Select your desired GCP region (find it via `gcloud compute regions list`)
         network:
           name: default # Select your desired network name (select new network name to create or find it via `gcloud compute networks list --format="value(name)"`)
         controlPlane:
           instanceType: n1-standard-2 # Select your desired instance type (find it via `gcloud compute machine-types list | grep REGION`)
           image: projects/ubuntu-os-cloud/global/images/ubuntu-2004-focal-v20250213 # Select image (find it via `gcloud compute images list --uri`)
           publicIP: true
         worker:
           instanceType: n1-standard-2 
           image: projects/ubuntu-os-cloud/global/images/ubuntu-2004-focal-v20250213
           publicIP: true
     ```

     Apply the YAML to your management cluster:

     ```bash
     kubectl apply -f my-gcp-clusterdeployment1.yaml
     ```
     ```console { .no-copy }
     clusterdeployment.k0rdent.mirantis.com/my-gcp-clusterdeployment1 created
     ```

     Note that although the `ClusterDeployment` object has been created, there will be a delay as actual GCP instances
     are provisioned and added to the cluster. You can follow the provisioning process:

     ```bash
     kubectl -n kcm-system get clusterdeployment.k0rdent.mirantis.com my-gcp-clusterdeployment1 --watch
     ```

     After the cluster is `Ready`, you can access it via the kubeconfig:

     ```bash
     kubectl -n kcm-system get secret my-gcp-clusterdeployment1-kubeconfig -o jsonpath='{.data.value}' | base64 -d > my-gcp-clusterdeployment1-kubeconfig.kubeconfig
     KUBECONFIG="my-gcp-clusterdeployment1-kubeconfig.kubeconfig" kubectl get pods -A
     ```

12. Cleanup

    To clean up GCP resources, delete the child cluster by deleting the `ClusterDeployment`:

    ```bash
    kubectl get clusterdeployments -A
    ```
    ```console { .no-copy }
    NAMESPACE    NAME                          READY   STATUS
    kcm-system   my-gcp-clusterdeployment1   True    ClusterDeployment is ready
    ```
    ```bash
    kubectl delete clusterdeployments my-gcp-clusterdeployment1 -n kcm-system
    ```
    ```console { .no-copy }
    clusterdeployment.k0rdent.mirantis.com "my-gcp-clusterdeployment1" deleted
    ```
