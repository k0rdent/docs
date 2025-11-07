# KOF Verification

Finally, verify that KOF installed properly.

## Verification steps

1. Get kubeconfigs of the regional and child clusters:
    ```bash
    kubectl get secret -n kcm-system $REGIONAL_CLUSTER_NAME-kubeconfig \
      -o=jsonpath={.data.value} | base64 -d > regional-kubeconfig

    kubectl get secret -n kcm-system $CHILD_CLUSTER_NAME-kubeconfig \
      -o=jsonpath={.data.value} | base64 -d > child-kubeconfig
    ```

    If the child cluster is created in [KCM Region](../regional-clusters/index.md), run:
    ```
    KUBECONFIG=regional-kubeconfig kubectl get secret \
      -n kcm-system $CHILD_CLUSTER_NAME-kubeconfig \
      -o=jsonpath={.data.value} | base64 -d > child-kubeconfig
    ```

2. Wait until the value of `HELMCHARTS` and `POLICYREFS`
    changes from `Provisioning` to `Provisioned`:
    ```bash
    kubectl get clustersummaries -A -o wide

    KUBECONFIG=regional-kubeconfig kubectl get clustersummaries -A -o wide
    ```

    If you see the `Failed/Provisioning` loop, check status and logs:
    ```bash
    kubectl get clustersummaries -A -o yaml \
      | yq '.items[].status.featureSummaries[]
      | select(.status != "Provisioned")'

    kubectl logs -n kof deploy/kof-mothership-kof-operator | less
    kubectl logs -n projectsveltos deploy/addon-controller | less
    ```

3. Wait for all pods in the regional and child clusters to show as `Running`
    in the namespaces `kof, kube-system, projectsveltos`:
    ```bash
    KUBECONFIG=regional-kubeconfig kubectl get pod -A
    KUBECONFIG=child-kubeconfig kubectl get pod -A
    ```

4. Wait until the value of `READY` changes to `True`
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

## KOF UI

You can use the KOF UI to find and debug errors or misconfigurations. Check the [Access to the KOF UI](kof-using.md#access-to-the-kof-ui) section to learn how to access it and read about its features.
