# Installing {{{ docsVersionInfo.k0rdentName }}} Observability and FinOps

KOF can be installed using Helm charts.

## Helm Charts

KOF is deployed as a series of Helm charts at various levels.

### kof-mothership

- Centralized [Grafana](https://grafana.com/) dashboard, managed by [grafana-operator](https://github.com/grafana/grafana-operator)
- Local [VictoriaMetrics](https://victoriametrics.com/) storage for alerting rules only, managed by [victoria-metrics-operator](https://docs.victoriametrics.com/operator/)
- [cluster-api-visualizer](https://github.com/Jont828/cluster-api-visualizer) for insight into multicluster configuration
- [Sveltos](https://projectsveltos.github.io/sveltos/) dashboard, automatic secret distribution
- [{{{ docsVersionInfo.k0rdentName }}}](https://github.com/k0rdent) service templates to deploy other charts to regional clusters
- [Promxy](https://github.com/jacksontj/promxy) for aggregating Prometheus metrics from regional clusters

### kof-storage

- Regional [Grafana](https://grafana.com/) dashboard, managed by [grafana-operator](https://github.com/grafana/grafana-operator)
- Regional [VictoriaMetrics](https://victoriametrics.com/) storage with main data, managed by [victoria-metrics-operator](https://docs.victoriametrics.com/operator/)
    - [vmauth](https://docs.victoriametrics.com/vmauth/) entrypoint proxy for VictoriaMetrics components
    - [vmcluster](https://docs.victoriametrics.com/operator/resources/vmcluster/) for high-available fault-tolerant version of VictoriaMetrics database
    - [victoria-logs-single](https://github.com/VictoriaMetrics/helm-charts/tree/master/charts/victoria-logs-single) for high-performance, cost-effective, scalable logs storage
- [external-dns](https://github.com/kubernetes-sigs/external-dns) to communicate with other clusters

### kof-operators

- [prometheus-operator-crds](https://github.com/prometheus-community/helm-charts/tree/main/charts/prometheus-operator-crds) required to create OpenTelemetry collectors, also required to monitor [`kof-mothership`](#management-cluster) itself
- [OpenTelemetry](https://opentelemetry.io/) [collectors](https://opentelemetry.io/docs/collector/) below, managed by [opentelemetry-operator](https://opentelemetry.io/docs/kubernetes/operator/)

### kof-collectors

- [prometheus-node-exporter](https://prometheus.io/docs/guides/node-exporter/) for hardware and OS metrics
- [kube-state-metrics](https://github.com/kubernetes/kube-state-metrics) for metrics about the state of Kubernetes objects
- [OpenCost](https://www.opencost.io/) "shines a light into the black box of Kubernetes spend"

## Prerequisites

Before beginning KOF installation, you should have the following components in place:

* A {{{ docsVersionInfo.k0rdentName }}} management cluster - You can get instructions to create one in the [quickstart guide](https://docs.k0rdent.io/v{{{ extra.docsVersionInfo.k0rdentDotVersion }}}/quickstart-1-mgmt-node-and-cluster/)
    * To test on [macOS](https://docs.k0sproject.io/stable/system-requirements/#host-operating-system) you can install using:
      `brew install kind && kind create cluster -n {{{ docsVersionInfo.k0rdentName }}}`
* You will also need your infrastructure provider credentials, such as those shown in the [guide for AWS](https://docs.k0rdent.io/v{{{ extra.docsVersionInfo.k0rdentDotVersion }}}/quickstart-2-aws/)
    * Note that you should skip the "Create your ClusterDeployment" and later sections.
* Finally, you need access to create DNS records for service endpoints such as `kof.example.com`

### DNS auto-config

To avoid manual configuration of DNS records for service endpoints later,
you can automate the process now using [external-dns](https://kubernetes-sigs.github.io/external-dns/latest/).

For example, for AWS you should use the [Node IAM Role](https://github.com/kubernetes-sigs/external-dns/blob/master/docs/tutorials/aws.md#node-iam-role)
or [IRSA](https://github.com/kubernetes-sigs/external-dns/blob/master/docs/tutorials/aws.md#iam-roles-for-service-accounts) methods in production.

For now, however, just for the sake of this demo based on the `aws-standalone` template,
you can use the most straightforward (though less secure) [static credentials](https://github.com/kubernetes-sigs/external-dns/blob/master/docs/tutorials/aws.md#static-credentials) method:

1. Create an `external-dns` IAM user with [this policy](https://github.com/kubernetes-sigs/external-dns/blob/master/docs/tutorials/aws.md#iam-policy).
2. Create an access key and `external-dns-aws-credentials` file, as in:
    ```
    [default]
    aws_access_key_id = <EXAMPLE_ACCESS_KEY_ID>
    aws_secret_access_key = <EXAMPLE_SECRET_ACCESS_KEY>
    ```
3. Create the `external-dns-aws-credentials` secret in the `kof` namespace:
    ```shell
    kubectl create namespace kof
    kubectl create secret generic \
      -n kof external-dns-aws-credentials \
      --from-file external-dns-aws-credentials
    ```

## Management Cluster

To install KOF on the management cluster,
look through the default values of the [kof-mothership](https://github.com/k0rdent/kof/blob/main/charts/kof-mothership/README.md)
and [kof-operators](https://github.com/k0rdent/kof/blob/main/charts/kof-operators/values.yaml) charts,
and apply this example, or use it as a reference:

1. Install `kof-operators` required by `kof-mothership`:
    ```shell
    helm install --wait --create-namespace -n kof kof-operators \
      oci://ghcr.io/k0rdent/kof/charts/kof-operators --version {{{ extra.docsVersionInfo.kofVersions.kofDotVersion }}}
    ```

2. Create the `mothership-values.yaml` file:
    ```yaml
    kcm:
      installTemplates: true
    ```
    This enables installation of `ServiceTemplates` such as `cert-manager` and `kof-storage`,
    to make it possible to reference them from the Regional and Child `ClusterDeployments`.

3. If you want to use a [default storage class](https://kubernetes.io/docs/concepts/storage/storage-classes/#default-storageclass),
    but `kubectl get sc` shows no `(default)`, create it.
    Otherwise you can use a non-default storage class in the `mothership-values.yaml` file:
    ```yaml
    global:
      storageClass: <EXAMPLE_STORAGE_CLASS>
    ```

4. If you've applied the [DNS auto-config](#dns-auto-config) section,
    add to the `kcm:` object in the `mothership-values.yaml` file:
    ```yaml
      kof:
        clusterProfiles:
          kof-aws-dns-secrets:
            matchLabels:
              k0rdent.mirantis.com/kof-aws-dns-secrets: "true"
            secrets:
              - external-dns-aws-credentials
    ```
    This enables Sveltos to auto-distribute DNS secret to regional clusters.

5. Two secrets are auto-created by default:
    * `storage-vmuser-credentials` is a secret used by VictoriaMetrics.
        You don't need to use it directly.
        It is auto-distributed to other clusters by the Sveltos `ClusterProfile` [here](https://github.com/k0rdent/kof/blob/121b61f5f6de6ddfdf3525b98f3ad4cb8ce57eaa/charts/kof-mothership/values.yaml#L25-L31).
    * `grafana-admin-credentials` is a secret that we will use in the [Grafana](./kof-using.md#access-to-grafana) section.
        It is auto-created [here](https://github.com/k0rdent/kof/blob/121b61f5f6de6ddfdf3525b98f3ad4cb8ce57eaa/charts/kof-mothership/values.yaml#L64-L65).

6. Install `kof-mothership`:
    ```shell
    helm install --wait -f mothership-values.yaml -n kof kof-mothership \
      oci://ghcr.io/k0rdent/kof/charts/kof-mothership --version {{{ extra.docsVersionInfo.kofVersions.kofDotVersion }}}
    ```

7. Wait for all pods to show that they're `Running`:
    ```shell
    kubectl get pod -n kof
    ```

## Regional Cluster

To install KOF on the regional cluster,
look through the default values of the [kof-storage](https://github.com/k0rdent/kof/blob/main/charts/kof-storage/values.yaml) chart,
and apply this example for AWS, or use it as a reference:

1. Set your KOF variables using your own values:
    ```shell
    REGIONAL_CLUSTER_NAME=cloud1-region1
    REGIONAL_DOMAIN=$REGIONAL_CLUSTER_NAME.kof.example.com
    ADMIN_EMAIL=$(git config user.email)
    echo "$REGIONAL_CLUSTER_NAME, $REGIONAL_DOMAIN, $ADMIN_EMAIL"
    ```

2. Use the up-to-date `ClusterTemplate`, as in:
    ```shell
    kubectl get clustertemplate -n kcm-system | grep aws
    TEMPLATE=aws-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsStandaloneCpCluster }}}
    ```

3. Compose the following objects:
    * `ClusterDeployment` - regional cluster
    * `PromxyServerGroup` - for metrics
    * `GrafanaDatasource` - for logs

    ```shell
    cat >regional-cluster.yaml <<EOF
    apiVersion: k0rdent.mirantis.com/v1alpha1
    kind: ClusterDeployment
    metadata:
      name: $REGIONAL_CLUSTER_NAME
      namespace: kcm-system
      labels:
        kof: storage
    spec:
      template: $TEMPLATE
      credential: aws-cluster-identity-cred
      config:
        clusterIdentity:
          name: aws-cluster-identity
          namespace: kcm-system
        controlPlane:
          instanceType: t3.large
        controlPlaneNumber: 1
        publicIP: false
        region: us-east-2
        worker:
          instanceType: t3.medium
        workersNumber: 3
        clusterLabels:
          k0rdent.mirantis.com/kof-storage-secrets: "true"
          k0rdent.mirantis.com/kof-aws-dns-secrets: "true"
      serviceSpec:
        priority: 100
        services:
          - name: ingress-nginx
            namespace: ingress-nginx
            template: ingress-nginx-4-11-3
          - name: cert-manager
            namespace: cert-manager
            template: cert-manager-1-16-2
            values: |
              cert-manager:
                crds:
                  enabled: true
          - name: kof-storage
            namespace: kof
            template: kof-storage-{{{ extra.docsVersionInfo.kofVersions.kofStorageVersion }}}
            values: |
              external-dns:
                enabled: true
              victoriametrics:
                vmauth:
                  ingress:
                    host: vmauth.$REGIONAL_DOMAIN
                security:
                  username_key: username
                  password_key: password
                  credentials_secret_name: storage-vmuser-credentials
              grafana:
                ingress:
                  host: grafana.$REGIONAL_DOMAIN
                security:
                  credentials_secret_name: grafana-admin-credentials
              cert-manager:
                email: $ADMIN_EMAIL
    ---
    apiVersion: kof.k0rdent.mirantis.com/v1alpha1
    kind: PromxyServerGroup
    metadata:
      labels:
        app.kubernetes.io/name: promxy-operator
        k0rdent.mirantis.com/promxy-secret-name: kof-mothership-promxy-config
      name: $REGIONAL_CLUSTER_NAME-metrics
      namespace: kof
    spec:
      cluster_name: $REGIONAL_CLUSTER_NAME
      targets:
        - "vmauth.$REGIONAL_DOMAIN:443"
      path_prefix: /vm/select/0/prometheus/
      scheme: https
      http_client:
        dial_timeout: "5s"
        tls_config:
          insecure_skip_verify: true
        basic_auth:
          credentials_secret_name: storage-vmuser-credentials
          username_key: username
          password_key: password
    ---
    apiVersion: grafana.integreatly.org/v1beta1
    kind: GrafanaDatasource
    metadata:
      labels:
        app.kubernetes.io/managed-by: Helm
      name: $REGIONAL_CLUSTER_NAME-logs
      namespace: kof
    spec:
      valuesFrom:
        - targetPath: "basicAuthUser"
          valueFrom:
            secretKeyRef:
              key: username
              name: storage-vmuser-credentials
        - targetPath: "secureJsonData.basicAuthPassword"
          valueFrom:
            secretKeyRef:
              key: password
              name: storage-vmuser-credentials
      datasource:
        name: $REGIONAL_CLUSTER_NAME
        url: https://vmauth.$REGIONAL_DOMAIN/vls
        access: proxy
        isDefault: false
        type: "victoriametrics-logs-datasource"
        basicAuth: true
        basicAuthUser: \${username}
        secureJsonData:
          basicAuthPassword: \${password}
      instanceSelector:
        matchLabels:
          dashboards: grafana
      resyncPeriod: 5m
    EOF
    ```

4. The `ClusterTemplate` above provides the [default storage class](https://kubernetes.io/docs/concepts/storage/storage-classes/#default-storageclass)
    `ebs-csi-default-sc`. If you want to use a non-default storage class,
    add it to the `regional-cluster.yaml` file
    in the `ClusterDeployment.spec.serviceSpec.services[name=kof-storage].values`:
    ```yaml
    global:
      storageClass: <EXAMPLE_STORAGE_CLASS>
    victoria-logs-single:
      server:
        storage:
          storageClassName: <EXAMPLE_STORAGE_CLASS>
    ```

5. Verify and apply the Regional `ClusterDeployment`:
    ```shell
    cat regional-cluster.yaml

    kubectl apply -f regional-cluster.yaml
    ```

6. Watch how the cluster is deployed to AWS until all values of `READY` are `True`:
    ```shell
    clusterctl describe cluster -n kcm-system $REGIONAL_CLUSTER_NAME \
      --show-conditions all
    ```

## Child Cluster

To install KOF on the actual cluster to be monitored,
look through the default values of the [kof-operators](https://github.com/k0rdent/kof/blob/main/charts/kof-operators/values.yaml)
and [kof-collectors](https://github.com/k0rdent/kof/blob/main/charts/kof-collectors/values.yaml) charts,
and apply this example for AWS, or use it as a reference:

1. Set your own value below, verifing [the variables](#regional-cluster):
    ```shell
    CHILD_CLUSTER_NAME=$REGIONAL_CLUSTER_NAME-child1
    echo "$CHILD_CLUSTER_NAME, $REGIONAL_DOMAIN"
    ```

2. Use the up-to-date `ClusterTemplate`, as in:
    ```shell
    kubectl get clustertemplate -n kcm-system | grep aws
    TEMPLATE=aws-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsStandaloneCpCluster }}}
    ```

3. Compose the `ClusterDeployment`:

    ```shell
    cat >child-cluster.yaml <<EOF
    apiVersion: k0rdent.mirantis.com/v1alpha1
    kind: ClusterDeployment
    metadata:
      name: $CHILD_CLUSTER_NAME
      namespace: kcm-system
      labels:
        kof: collector
    spec:
      template: $TEMPLATE
      credential: aws-cluster-identity-cred
      config:
        clusterIdentity:
          name: aws-cluster-identity
          namespace: kcm-system
        controlPlane:
          instanceType: t3.large
        controlPlaneNumber: 1
        publicIP: false
        region: us-east-2
        worker:
          instanceType: t3.small
        workersNumber: 3
        clusterLabels:
          k0rdent.mirantis.com/kof-storage-secrets: "true"
      serviceSpec:
        priority: 100
        services:
          - name: cert-manager
            namespace: kof
            template: cert-manager-1-16-2
            values: |
              cert-manager:
                crds:
                  enabled: true
          - name: kof-operators
            namespace: kof
            template: kof-operators-{{{ extra.docsVersionInfo.kofVersions.kofOperatorsVersion }}}
          - name: kof-collectors
            namespace: kof
            template: kof-collectors-{{{ extra.docsVersionInfo.kofVersions.kofCollectorsVersion }}}
            values: |
              global:
                clusterName: $CHILD_CLUSTER_NAME
              opencost:
                enabled: true
                opencost:
                  prometheus:
                    username_key: username
                    password_key: password
                    existingSecretName: storage-vmuser-credentials
                    external:
                      url: https://vmauth.$REGIONAL_DOMAIN/vm/select/0/prometheus
                  exporter:
                    defaultClusterId: $CHILD_CLUSTER_NAME
              kof:
                logs:
                  username_key: username
                  password_key: password
                  credentials_secret_name: storage-vmuser-credentials
                  endpoint: https://vmauth.$REGIONAL_DOMAIN/vls/insert/opentelemetry/v1/logs
                metrics:
                  username_key: username
                  password_key: password
                  credentials_secret_name: storage-vmuser-credentials
                  endpoint: https://vmauth.$REGIONAL_DOMAIN/vm/insert/0/prometheus/api/v1/write
    EOF
    ```

4. Verify and apply the `ClusterDeployment`:
    ```shell
    cat child-cluster.yaml

    kubectl apply -f child-cluster.yaml
    ```

5. Watch while the cluster is deployed to AWS until all values of `READY` are `True`:
    ```shell
    clusterctl describe cluster -n kcm-system $CHILD_CLUSTER_NAME \
      --show-conditions all
    ```
