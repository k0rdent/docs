# KOF Verification

Finally, verify that KOF installed properly.

## Management Cluster Verification

For KOF v1.8.0+, the umbrella chart uses FluxCD to orchestrate component installation. Verify the management cluster first:

1. Wait for all HelmReleases to be ready:
    ```bash
    kubectl wait --for=condition=Ready helmreleases --all -n kof --timeout=10m
    kubectl get helmreleases -n kof
    ```

    All HelmReleases should show `Ready=True`. If any are not ready, check their status:
    ```bash
    kubectl describe helmrelease -n kof <helmrelease-name>
    ```

2. Verify all pods are running in the `kof` namespace:
    ```bash
    kubectl get pods -n kof
    ```

3. Wait for ServiceTemplates to be valid:
    ```bash
    kubectl wait --for=jsonpath={.status.valid}=true svctmpl -A --all
    kubectl get svctmpl -A
    ```

    All ServiceTemplates should show `VALID=true`.

## Regional and Child Cluster Verification

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

2. Create this DNS record of type `A`, pointing to that `EXTERNAL-IP`:
    ```bash
    echo vmauth.$REGIONAL_DOMAIN
    ```
    Only if Grafana is [installed and enabled](kof-grafana.md), do the same for:
    ```bash
    echo grafana.$REGIONAL_DOMAIN
    ```

## KOF UI

You can use the KOF UI to find and debug errors or misconfigurations. Check the [Access to the KOF UI](kof-using.md#kof-ui) section to learn how to access it and read about its features.
