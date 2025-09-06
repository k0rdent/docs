# KOF Verification

Finally, verify that KOF installed properly.

## Verification steps

1. Wait until the value of `HELMCHARTS` and `POLICYREFS`
    changes from `Provisioning` to `Provisioned`:
    ```bash
    kubectl get clustersummaries -A -o wide
    ```
    If you see the `Failed/Provisioning` loop, check status and logs:
    ```bash
    kubectl get clustersummaries -A -o yaml \
      | yq '.items[].status.featureSummaries[]
      | select(.status != "Provisioned")'

    kubectl logs -n kof deploy/kof-mothership-kof-operator | less
    kubectl logs -n projectsveltos deploy/addon-controller | less
    ```

    If you are not using [Istio](kof-install.md#istio),
    please ensure you've applied [this workaround](kof-upgrade.md/#upgrade-to-v130)
    by checking that `Reconciling MultiClusterService` is logged every 10 seconds, more than 3 times:
    ```bash
    kubectl logs -n kcm-system deploy/kcm-controller-manager -f \
      | grep 'Reconciling MultiClusterService'
    ```

2. Wait for all pods in the regional and child clusters to show as `Running`
    in the namespaces `kof, kube-system, projectsveltos`:
    ```bash
    kubectl get secret -n kcm-system $REGIONAL_CLUSTER_NAME-kubeconfig \
      -o=jsonpath={.data.value} | base64 -d > regional-kubeconfig

    kubectl get secret -n kcm-system $CHILD_CLUSTER_NAME-kubeconfig \
      -o=jsonpath={.data.value} | base64 -d > child-kubeconfig

    KUBECONFIG=regional-kubeconfig kubectl get pod -A
    KUBECONFIG=child-kubeconfig kubectl get pod -A
    ```

3. Wait until the value of `READY` changes to `True`
    for all certificates in each cluster:
    ```bash
    KUBECONFIG=regional-kubeconfig kubectl get cert -A
    KUBECONFIG=child-kubeconfig kubectl get cert -A
    ```

## Manual DNS config

If you've opted out of [DNS auto-config](./kof-install.md#dns-auto-config)
and [Istio](./kof-install.md#istio), you will need to do the following:

1. Get the `EXTERNAL-IP` of `ingress-nginx`:
    ```bash
    KUBECONFIG=regional-kubeconfig kubectl get svc \
      -n kof ingress-nginx-controller
    ```
    It should look like `REDACTED.us-east-2.elb.amazonaws.com`

2. Create these DNS records of type `A`, all pointing to that `EXTERNAL-IP`:
    ```bash
    echo grafana.$REGIONAL_DOMAIN
    echo jaeger.$REGIONAL_DOMAIN
    echo vmauth.$REGIONAL_DOMAIN
    ```

## Sveltos

Use the [Sveltos dashboard](https://projectsveltos.github.io/sveltos/getting_started/install/dashboard/#platform-administrator-example)
to verify secrets have been auto-distributed to the required clusters:

1. Start by preparing the system:

    ```bash
    kubectl create sa platform-admin
    kubectl create clusterrolebinding platform-admin-access \
      --clusterrole cluster-admin --serviceaccount default:platform-admin

    kubectl create token platform-admin --duration=24h
    kubectl port-forward -n kof svc/dashboard 8081:80
    ```

2. Now open [http://127.0.0.1:8081/login](http://127.0.0.1:8081/login) and paste the token output in step 1 above.
3. Open the `ClusterAPI` tab: [http://127.0.0.1:8081/sveltos/clusters/ClusterAPI/1](http://127.0.0.1:8081/sveltos/clusters/ClusterAPI/1)
4. Check both regional and child clusters:
    * Cluster profiles should be `Provisioned`.
    * Secrets should be distributed.

![sveltos-demo](../../assets/kof/sveltos-2025-02-13.gif)
