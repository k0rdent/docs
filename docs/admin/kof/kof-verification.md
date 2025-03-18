# KOF Verification

Finally, verify that KOF installed properly.

```shell
kubectl get clustersummaries -A -o wide
```
Wait until the value of `HELMCHARTS` changes from `Provisioning` to `Provisioned`.

```shell
kubectl get secret -n kcm-system $REGIONAL_CLUSTER_NAME-kubeconfig \
  -o=jsonpath={.data.value} | base64 -d > regional-kubeconfig

kubectl get secret -n kcm-system $CHILD_CLUSTER_NAME-kubeconfig \
  -o=jsonpath={.data.value} | base64 -d > child-kubeconfig

KUBECONFIG=regional-kubeconfig kubectl get pod -A
  # Namespaces: cert-manager, ingress-nginx, kof, kube-system, projectsveltos

KUBECONFIG=child-kubeconfig kubectl get pod -A
  # Namespaces: kof, kube-system, projectsveltos
```
Wait for all pods to show as `Running`.

## Manual DNS config

If you've opted out of [DNS auto-config](./kof-install.md#dns-auto-config), you will need to do the following:

1. Get the `EXTERNAL-IP` of `ingress-nginx`:
    ```shell
    KUBECONFIG=regional-kubeconfig kubectl get svc \
      -n ingress-nginx ingress-nginx-controller
    ```
    It should look like `REDACTED.us-east-2.elb.amazonaws.com`

2. Create these DNS records of type `A`, both pointing to that `EXTERNAL-IP`:
    ```shell
    echo vmauth.$REGIONAL_DOMAIN
    echo grafana.$REGIONAL_DOMAIN
    ```

## Sveltos

Use the [Sveltos dashboard](https://projectsveltos.github.io/sveltos/getting_started/install/dashboard/#platform-administrator-example)
to verify secrets have been auto-distributed to the required clusters:

1. Start by preparing the system:

    ```shell
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