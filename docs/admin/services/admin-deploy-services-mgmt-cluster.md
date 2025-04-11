# Deploy beach-head services on Management Cluster itself

On the management cluster where k0rdent has been installed, there is a `SveltosCluster` called "mgmt" available in the "mgmt" namespace as seen below. We can use this resource to manage beach-head services on the management cluster itself.

```sh
➜  ~ kubectl -n mgmt get sveltoscluster mgmt --show-labels
NAME   READY   VERSION   LABELS
mgmt   true    v1.32.2   k0rdent.mirantis.com/management-cluster=true,projectsveltos.io/k8s-version=v1.32.2,sveltos-agent=present
```

To do so, we can create a `MultiClusterService` object that matches the "mgmt" `SveltosCluster` using the `k0rdent.mirantis.com/management-cluster=true` and `sveltos-agent=present` labels.

```yaml
apiVersion: k0rdent.mirantis.com/v1alpha1
kind: MultiClusterService
metadata:
  name: myapp-mcs
spec:
  clusterSelector:
    matchLabels:
      k0rdent.mirantis.com/management-cluster: "true"
      sveltos-agent: present
  serviceSpec:
    services:
      - template: myapp-0-1-0
        name: myapp
        namespace: myapp
```

Using the "myapp-mcs" `MultiClusterService` above, the "myapp" beach-head service can be deployed on the management cluster itself:

```sh
➜  ~ kubectl get pod -A
NAMESPACE            NAME                                                           READY   STATUS    RESTARTS   AGE
kcm-system           azureserviceoperator-controller-manager-6b4dd86894-t4nxm       1/1     Running   0          13m
kcm-system           capa-controller-manager-64bbcb9f8-pbf5w                        1/1     Running   0          12m
kcm-system           capd-controller-manager-7586b6577c-d5zpq                       1/1     Running   0          13m
kcm-system           capg-controller-manager-774958b9b9-l45bd                       1/1     Running   0          12m
kcm-system           capi-controller-manager-5b67d4fc7-jjvm5                        1/1     Running   0          14m
kcm-system           capo-controller-manager-6f98bb68cd-dwtzr                       1/1     Running   0          12m
kcm-system           capv-controller-manager-69f7fc65d8-wvpb6                       1/1     Running   0          12m
kcm-system           capz-controller-manager-5b87fdf745-nxlkk                       1/1     Running   0          13m
kcm-system           helm-controller-746d7db585-f585w                               1/1     Running   0          16m
kcm-system           k0smotron-controller-manager-bootstrap-67dd88d848-r2d8h        2/2     Running   0          13m
kcm-system           k0smotron-controller-manager-control-plane-657f5578d4-ggjfq    2/2     Running   0          13m
kcm-system           k0smotron-controller-manager-infrastructure-5867d575f9-vvttc   2/2     Running   0          12m
kcm-system           kcm-cert-manager-6979c67bc4-6gplg                              1/1     Running   0          16m
kcm-system           kcm-cert-manager-cainjector-5b97c84fdb-5k9tc                   1/1     Running   0          16m
kcm-system           kcm-cert-manager-webhook-755796f599-fcnfv                      1/1     Running   0          16m
kcm-system           kcm-cluster-api-operator-65c8f75569-4rnsf                      1/1     Running   0          15m
kcm-system           kcm-controller-manager-785c5964d-6l8sl                         1/1     Running   0          15m
kcm-system           kcm-velero-67bf545995-4d8ns                                    1/1     Running   0          16m
kcm-system           source-controller-74b597b995-wkfj2                             1/1     Running   0          16m
kube-system          coredns-668d6bf9bc-46hqk                                       1/1     Running   0          17m
kube-system          coredns-668d6bf9bc-m4bk8                                       1/1     Running   0          17m
kube-system          etcd-kcm-dev-control-plane                                     1/1     Running   0          17m
kube-system          kindnet-fwh7t                                                  1/1     Running   0          17m
kube-system          kube-apiserver-kcm-dev-control-plane                           1/1     Running   0          17m
kube-system          kube-controller-manager-kcm-dev-control-plane                  1/1     Running   0          17m
kube-system          kube-proxy-bk6tx                                               1/1     Running   0          17m
kube-system          kube-scheduler-kcm-dev-control-plane                           1/1     Running   0          17m
local-path-storage   local-path-provisioner-7dc846544d-qjkwh                        1/1     Running   0          17m
myapp                myapp-85b8d7f879-rcdp9                                         1/1     Running   0          6m52s
orc-system           orc-controller-manager-5f6dbcc58-l8mxn                         1/1     Running   0          13m
projectsveltos       access-manager-6696df779-rdn92                                 1/1     Running   0          13m
projectsveltos       addon-controller-7bb87bc597-9c6c9                              1/1     Running   0          13m
projectsveltos       classifier-manager-5b47b66fc9-bzkt2                            1/1     Running   0          13m
projectsveltos       event-manager-564d6644b4-vdtjz                                 1/1     Running   0          13m
projectsveltos       hc-manager-7c56c59d9c-c7lqb                                    1/1     Running   0          13m
projectsveltos       sc-manager-6798cd9d4d-9q6b6                                    1/1     Running   0          13m
projectsveltos       shard-controller-797965bb58-rp6jl                              1/1     Running   0          13m
projectsveltos       sveltos-agent-manager-5445f6f57c-56mjz                         1/1     Running   0          12m
projectsveltos       techsupport-controller-5b666d6884-dhd6s                        1/1     Running   0          13m
```
