# GCP ClusterDeployment Deletion Stuck: Resource Is in Use by Another Resource

[Related issue: KCM #1476](https://github.com/k0rdent/kcm/issues/1476)

When deleting a GCP cluster, the process can become stuck during the VPC deletion phase. The following error may
appear in the `cluster-api-provider-gcp` logs:

```shell
E0505 13:33:29.573486       1 controller.go:324] "Reconciler error" err="googleapi:
Error 400: RESOURCE_IN_USE_BY_ANOTHER_RESOURCE - The network resource 'projects/k0rdent-dev/global/networks/network-name'
is already being used by 'projects/k0rdent-dev/global/routes/kubernetes-f85faa80-9d44-4a73-a679-97aa072ecb4e'"
controller="gcpcluster" controllerGroup="infrastructure.cluster.x-k8s.io" controllerKind="GCPCluster"
GCPCluster="kcm-system/gcp-ekaz" namespace="kcm-system" name="gcp-ekaz" reconcileID="74d04828-3892-4ad5-80c9-dd9187857c6e"
```

This typically occurs when orphaned routes remain in the VPC and reference deleted compute instances.

As a result, the `ClusterDeployment` object cannot be fully deleted until these route resources are removed.

**Workaround**

Manually delete all orphaned routes using the `gcloud` CLI or the Google Cloud Console. For example, using
the `gcloud` CLI:

1. Identify the orphaned route from the `cluster-api-provider-gcp` logs (e.g.,
`kubernetes-f85faa80-9d44-4a73-a679-97aa072ecb4e`).

1. List all routes in the affected network:

    ```bash
    gcloud compute routes list --filter="network:<networkName>"
    ```

    Example output for the network `test-net`:
    ```yaml
    NAME                                             NETWORK   DEST_RANGE     NEXT_HOP                                                           PRIORITY
    default-route-r-e39cfb79ee7071c0                 test-net  10.128.0.0/20  test-net                                                           0
    default-route-r-ffb0b56ff2dc7b8a                 test-net  10.212.0.0/20  test-net                                                           0
    kubernetes-24a016be-92d0-4298-abec-772bf45ba189  test-net  10.244.4.0/24  europe-west4-a/instances/test-ksi-gcp-18apr-20-n2d-cp-2            1000
    kubernetes-3ec1f296-768b-445d-b280-23560bed3ed1  test-net  10.244.2.0/24  europe-west4-a/instances/test-ksi-gcp-18apr-20-n2d-md-rqr5q-968gx  1000
    ```

1. Delete orphaned routes where the instance in the NEXT_HOP column no longer exists:

    ```bash
    gcloud compute routes delete <routeName>
    ```

    Repeat for each orphaned route to allow the VPC to be deleted successfully.
