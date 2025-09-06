# GCP Hosted Control Plane Deployment

Follow these steps to set up a k0smotron-hosted control plane on Google Cloud:

1. Prerequisites

    Before you start, make sure you have the following:

    - A management Kubernetes cluster (Kubernetes v1.28+) deployed on GCP with [{{{ docsVersionInfo.k0rdentName }}} installed](../installation/install-k0rdent.md).
    - A GCP Cloud Controller Manager installed to manage Services with the `Load Balancer` type.
    - A [default storage class](https://kubernetes.io/docs/tasks/administer-cluster/change-default-storage-class/) configured
      on the management cluster to support Persistent Volumes.

    > NOTE:  
    > All control plane components for managed clusters will run in the management cluster. Make sure the management cluster has sufficient CPU, memory, and storage to handle the additional workload.

2. Create the `ClusterDeployment` manifest

    The `ClusterDeployment` manifest for a GCP-hosted control plane is similar to those for standalone control plane deployments.
    For a detailed list of parameters, refer to the [Template Reference Guide](../../reference/template/template-gcp.md), but here is an example:

    ```yaml
    apiVersion: k0rdent.mirantis.com/v1beta1
    kind: ClusterDeployment
    metadata:
      name: gcp-hosted-cp
    spec:
      template: gcp-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.gcpHostedCpCluster }}}
      credential: gcp-credential
      config:
        project: "PROJECT_NAME"
        region: "us-east4"
        network:
          name: default # Select your desired network name (select new network name to create or find it via `gcloud compute networks list --format="value(name)"`)
        worker:
          instanceType: n1-standard-2 # Select your desired instance type (find it via `gcloud compute machine-types list | grep REGION`)
          image: projects/ubuntu-os-cloud/global/images/ubuntu-2004-focal-v20250213 # Select image (find it via `gcloud compute images list --uri`)
    ```

    Apply the `ClusterDeployment` manifest to the management cluster, as in:

    ```bash
    kubectl apply -f clusterdeployment.yaml -n kcm-system
    ```
