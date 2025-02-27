# k0rdent Observability and FinOps (kof)

## Overview

k0rdent Observability and FinOps ([kof](https://github.com/k0rdent/kof)) provides enterprise-grade observability
and FinOps capabilities for k0rdent-managed child Kubernetes clusters.
It enables centralized metrics, logging, and cost management
through a unified [OpenTelemetry](https://opentelemetry.io/docs/)-based architecture.

* **Observability**: KOF collects **metrics** from various sources and stores them in a time series database
based on [Victoria Metrics](https://github.com/victoriaMetrics/VictoriaMetrics/), allowing for real-time and historical analysis.
It includes **log management** features to aggregate, store, and analyze logs from different 
components of the Kubernetes ecosystem. This helps in troubleshooting and understanding the behavior of applications and infrastructure.
KOF can evaluate **alerting** rules and send notifications based on these collected metrics and logs helping to identify and respond to issues before they impact users.

* **FinOps**: KOF helps with **cost management** by tracking and managing the costs associated with running applications on Kubernetes. 
It provides insights into resource utilization and helps in optimizing costs by identifying underutilized or over-provisioned resources.
With this information, you can **set budgets and forecast future costs** based on historical data and current 
usage patterns. KOF enables **chargeback and showback** mechanisms, enabling organizations to attribute costs to 
specific teams, departments, or projects, and promotes accountability and transparency in resource usage.

* **Centralized Management**: KOF provides a **unified control plane** for managing Kubernetes clusters at scale, with a 
centralized view of all clusters, making it possible to use k0rdent to manage and operate large-scale deployments.
It also offers comprehensive **lifecycle management** capabilities, including provisioning, 
configuration, and maintenance of Kubernetes clusters, ensuring clusters are consistently managed and adhere to best practices.

* **Scalability and Performance**: KOF leverages components such as VictoriaMetrics to provide **high-performance** monitoring and analytics. 
It can handle millions of metrics per second and provides low-latency query responses. It's also designed to **scale** horizontally, enabling it to manage large volumes of data and support growing environments. It can be deployed on-premises, in the cloud, or in hybrid environments.

* **Compliance and Security**: KOF helps ensure **compliance** with organizational policies and industry standards, providing
audit trails and reporting features to meet regulatory requirements. It includes **security** features to protect data and ensure 
the integrity of monitoring and FinOps processes. It supports role-based access control (RBAC) and secure communication protocols.

### Use Cases

KOF can be used by both technical and non-technical arms of a company.

* **Platform Engineering:** KOF is ideal for platform engineers who need to manage and monitor Kubernetes 
clusters at scale. It provides the tools and insights required to ensure the reliability and performance of applications.
* **DevOps Teams:** DevOps teams can use KOF to gain visibility into the deployment and operation of applications, 
helping them to identify and resolve issues quickly.
* **Finance Teams:** Finance teams can leverage KOF's FinOps capabilities to track and manage cloud spending, 
ensuring resources are used efficiently and costs are optimized.

## Architecture

### High-level

From a high-level perspective, KOF consists of three layers:

* the Collection layer, where the statistics and events are gathered,
* the Regional layer, which includes storage to keep track of those statistics and events,
* and the Management layer, where you interact through the UI.

```mermaid
flowchart TD;
    A[Management UI, promxy] 
    A --> C[Storage Region 1]
    A --> D[Storage Region 2]
    C --> E[Collect Child 1]
    C --> F[Collect Child 2]
    D ==> G[...]
```

### Mid-level

Getting a little bit more detailed, it's important to undrestand that data flows upwards,
from observed objects to centralized Grafana on the Management layer:

<!--

To update the diagram:
* Update the indented text below.
* Copy/paste it to https://codepen.io/denis-ryzhkov/pen/ByajZeJ
* Copy the resulting HTML.
* Please preserve custom `max-width: 30em;` in the end.

<b>Management Cluster</b>
  kof-mothership chart
    grafana-operator
    victoria-metrics-operator
    cluster-api-visualizer
    sveltos-dashboard
    k0rdent service templates
    promxy

  kof-operators chart
    opentelemetry-operator
    prometheus-operator-crds

Cloud 1..N
  Region 1..M

    <b>Regional Cluster</b>
      kof-storage chart
        grafana-operator
        victoria-metrics-operator
        victoria-logs-single
        external-dns

      cert-manager of grafana and vmauth
      ingress-nginx

    <b>Child Cluster 1</b>
      cert-manager of OTel-operator

      kof-operators chart
        opentelemetry-operator
          OpenTelemetryCollector
        prometheus-operator-crds

      kof-collectors chart
        opencost
        kube-state-metrics
        prometheus-node-exporter

      observed objects
-->

<div class="o">
  <b>Management Cluster</b>
  <div class="o">
    kof-mothership chart
    <div class="o">
      grafana-operator
    </div>
    <div class="o">
      victoria-metrics-operator
    </div>
    <div class="o">
      cluster-api-visualizer
    </div>
    <div class="o">
      sveltos-dashboard
    </div>
    <div class="o">
      k0rdent service templates
    </div>
    <div class="o">
      promxy
    </div>
  </div>
  <div class="o">
    kof-operators chart
    <div class="o">
      opentelemetry-operator
    </div>
    <div class="o">
      prometheus-operator-crds
    </div>
  </div>
</div>
<div class="o">
  Cloud 1..N
  <div class="o">
    Region 1..M
    <div class="o">
      <b>Regional Cluster</b>
      <div class="o">
        kof-storage chart
        <div class="o">
          grafana-operator
        </div>
        <div class="o">
          victoria-metrics-operator
        </div>
        <div class="o">
          victoria-logs-single
        </div>
        <div class="o">
          external-dns
        </div>
      </div>
      <div class="o">
        cert-manager of grafana and vmauth
      </div>
      <div class="o">
        ingress-nginx
      </div>
    </div>
    <div class="o">
      <b>Child Cluster 1</b>
      <div class="o">
        cert-manager of OTel-operator
      </div>
      <div class="o">
        kof-operators chart
        <div class="o">
          opentelemetry-operator
          <div class="o">
            OpenTelemetryCollector
          </div>
        </div>
        <div class="o">
          prometheus-operator-crds
        </div>
      </div>
      <div class="o">
        kof-collectors chart
        <div class="o">
          opencost
        </div>
        <div class="o">
          kube-state-metrics
        </div>
        <div class="o">
          prometheus-node-exporter
        </div>
      </div>
      <div class="o">
        observed objects
      </div>
    </div>
  </div>
</div>

<style>
  .o {
    margin: 0.25em 1em;
    background-color: rgba(128, 128, 128, 0.25);
    padding: 0.25em 0.5em;
    max-width: 30em;
  }
</style>

### Low-level

At a low level, you can see how logs and traces work their way around the system.

![kof-architecture](assets/kof/otel.png)

## Helm Charts

KOF is deployed as a series of Helm charts at various levels.

### kof-mothership

- Centralized [Grafana](https://grafana.com/) dashboard, managed by [grafana-operator](https://github.com/grafana/grafana-operator)
- Local [VictoriaMetrics](https://victoriametrics.com/) storage for alerting rules only, managed by [victoria-metrics-operator](https://docs.victoriametrics.com/operator/)
- [cluster-api-visualizer](https://github.com/Jont828/cluster-api-visualizer) for insight into multicluster configuration
- [Sveltos](https://projectsveltos.github.io/sveltos/) dashboard, automatic secret distribution
- [k0rdent](https://github.com/k0rdent) service templates to deploy other charts to regional clusters
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

## Installation

### Prerequisites

Before beginning KOF installation, you should have the following components in place:

* A k0rdent management cluster - You can get instructions to create one in the [quickstart guide](https://docs.k0rdent.io/v{{{ extra.docsVersionInfo.k0rdentDotVersion }}}/quickstart-1-mgmt-node-and-cluster/)
    * To test on [macOS](https://docs.k0sproject.io/stable/system-requirements/#host-operating-system) you can install using:
      `brew install kind && kind create cluster -n k0rdent`
* You will also need your infrastructure provider credentials, such as those shown in the [guide for AWS](https://docs.k0rdent.io/v{{{ extra.docsVersionInfo.k0rdentDotVersion }}}/quickstart-2-aws/)
    * Note that you should skip the "Create your ClusterDeployment" and later sections.
* Finally, you need access to create DNS records for service endpoints such as `kof.example.com`

### DNS auto-config

To avoid [manual configuration of DNS records for service endpoints](#manual-dns-config) later,
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

### Management Cluster

To install KOF on the management cluster,
look through the default values of the [kof-mothership](https://github.com/k0rdent/kof/blob/main/charts/kof-mothership/README.md)
and [kof-operators](https://github.com/k0rdent/kof/blob/main/charts/kof-operators/values.yaml) charts,
and apply this example, or use it as a reference:

1. Install `kof-operators` required by `kof-mothership`:
    ```shell
    helm install --wait --create-namespace -n kof kof-operators \
      oci://ghcr.io/k0rdent/kof/charts/kof-operators --version 0.1.1
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
    * `grafana-admin-credentials` is a secret that we will use in the [Grafana](#grafana) section.
        It is auto-created [here](https://github.com/k0rdent/kof/blob/121b61f5f6de6ddfdf3525b98f3ad4cb8ce57eaa/charts/kof-mothership/values.yaml#L64-L65).

6. Install `kof-mothership`:
    ```shell
    helm install --wait -f mothership-values.yaml -n kof kof-mothership \
      oci://ghcr.io/k0rdent/kof/charts/kof-mothership --version 0.1.1
    ```

7. Wait for all pods to show that they're `Running`:
    ```shell
    kubectl get pod -n kof
    ```

### Regional Cluster

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
    TEMPLATE=aws-standalone-cp-{{{ extra.docsVersionInfo.k0rdentVersion }}}
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
            template: kof-storage-0-1-1
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

### Child Cluster

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
    TEMPLATE=aws-standalone-cp-{{{ extra.docsVersionInfo.k0rdentVersion }}}
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
            template: kof-operators-0-1-1
          - name: kof-collectors
            namespace: kof
            template: kof-collectors-0-1-1
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

### Verification

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

### Manual DNS config

If you've opted out of [DNS auto-config](#dns-auto-config), you will need to do the following:

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

![sveltos-demo](assets/kof/sveltos-2025-02-13.gif)

## Grafana

### Access to Grafana

To make Grafana available, follow these steps:

1. Get the Grafana username and password:
    ```shell
    kubectl get secret -n kof grafana-admin-credentials -o yaml | yq '{
      "user": .data.GF_SECURITY_ADMIN_USER | @base64d,
      "pass": .data.GF_SECURITY_ADMIN_PASSWORD | @base64d
    }'
    ```

2. Start the Grafana dashboard:
    ```shell
    kubectl port-forward -n kof svc/grafana-vm-service 3000:3000
    ```

3. Login to [http://127.0.0.1:3000/dashboards](http://127.0.0.1:3000/dashboards) with the username/password printed above.
4. Open a dashboard:

![grafana-demo](assets/kof/grafana-2025-01-14.gif)

### Cluster Overview

From here you can get an overview of the cluster, including:

* Health metrics
* Resource utilization
* Performance trends
* Cost analysis

### Logging Interface

The logging interface will also be available, including:

* Real-time log streaming
* Full-text search
* Log aggregation
* Alert correlation

### Cost Management

Finally there are the cost management features, including:

* Resource cost tracking
* Usage analysis
* Budget monitoring
* Optimization recommendations

## Scaling Guidelines

The method for scaling KOF depends on the type of expansion:

### Regional Expansion

1. Deploy a [regional cluster](#regional-cluster) in the new region
2. Configure child clusters in this region to point to this regional cluster

### Adding a New Child Cluster

1. Apply templates, as in the [child cluster](#child-cluster) section
2. Verify the data flow
3. Configure any custom dashboards

## Maintenance

### Backup Requirements

Backing up KOF requires backing up the following:

* Grafana configurations
* Alert definitions
* Custom dashboards
* Retention policies

### Health Monitoring

To implement health monitoring:

1. Apply the steps in the [Verification](#verification) section
2. Apply the steps in the [Sveltos](#sveltos) section

### Uninstallation

To remove the demo clusters created in this section:

> WARNING:
> Make sure these are just your demo clusters and do not contain important data.

```shell
kubectl delete --wait --cascade=foreground -f child-cluster.yaml
kubectl delete --wait --cascade=foreground -f regional-cluster.yaml
```

To remove KOF from the management cluster:

```shell
helm uninstall --wait --cascade foreground -n kof kof-mothership
helm uninstall --wait --cascade foreground -n kof kof-operators
kubectl delete namespace kof --wait --cascade=foreground
```

## Resource Limits

See also: [System Requirements](https://github.com/k0rdent/kof/blob/main/docs/system-requirements.md).

### Resources of Management Cluster

- [promxy](https://github.com/k0rdent/kof/blob/121b61f5f6de6ddfdf3525b98f3ad4cb8ce57eaa/charts/kof-mothership/values.yaml#L120-L126):
  ```yaml
  resources:
    requests:
      cpu: 100m
      memory: 128Mi
    limits:
      cpu: 100m
      memory: 128Mi
  ```

- [promxy-deployment](https://github.com/k0rdent/kof/blob/121b61f5f6de6ddfdf3525b98f3ad4cb8ce57eaa/charts/kof-mothership/templates/promxy/promxy-deployment.yaml#L107-L113):
  ```yaml
  resources:
    requests:
      cpu: 0.02
      memory: 20Mi
    limits:
      cpu: 0.02
      memory: 20Mi
  ```

- [promxy-operator](https://github.com/k0rdent/kof/blob/121b61f5f6de6ddfdf3525b98f3ad4cb8ce57eaa/promxy-operator/config/manager/manager.yaml#L87-L93):
  ```yaml
  resources:
    limits:
      cpu: 500m
      memory: 128Mi
    requests:
      cpu: 10m
      memory: 64Mi
  ```

### Resources of a Child Cluster

- [opentelemetry](https://github.com/k0rdent/kof/blob/121b61f5f6de6ddfdf3525b98f3ad4cb8ce57eaa/charts/kof-collectors/templates/opentelemetry/instrumentation.yaml#L18-L22):
  ```yaml
  resourceRequirements:
    limits:
      memory: 128Mi
    requests:
      memory: 128Mi
  ```

## Version Compatibility

| Component       | Version  | Notes                         |
|-----------------|----------|-------------------------------|
| k0rdent         | ≥ 0.0.7  | Required for template support |
| Kubernetes      | ≥ 1.32   | Earlier versions untested     |
| OpenTelemetry   | ≥ 0.75   | Recommended minimum           |
| VictoriaMetrics | ≥ 0.40   | Required for clustering       |

Detailed:

- [kof-mothership](https://github.com/k0rdent/kof/blob/main/charts/kof-mothership/Chart.yaml)
- [kof-storage](https://github.com/k0rdent/kof/blob/main/charts/kof-storage/Chart.yaml)
- [kof-operators](https://github.com/k0rdent/kof/blob/main/charts/kof-operators/Chart.yaml)
- [kof-collectors](https://github.com/k0rdent/kof/blob/main/charts/kof-collectors/Chart.yaml)

## More

- If you've applied this guide you should have kof up and running.
- Check [k0rdent/kof/docs](https://github.com/k0rdent/kof/tree/main/docs) for advanced guides
such as [configuring alerts](https://github.com/k0rdent/kof/blob/main/docs/alerts.md).
