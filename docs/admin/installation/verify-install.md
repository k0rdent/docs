# Confirming the deployment

> NOTE:
> After running the helm install command, please wait 5 to 10 minutes for the deployment to stabilize.

To understand whether installation is complete, start by making sure all pods are ready in the `kcm-system` namespace. There should be 21 pod entries:

```bash
kubectl get pods -n kcm-system
```

```console { .no-copy }
NAME                                                           READY   STATUS    RESTARTS   AGE
azureserviceoperator-controller-manager-58bb68bc75-22p2m       1/1     Running   0          18m
capa-controller-manager-d84cc5796-2bqx2                        1/1     Running   0          18m
capd-controller-manager-74b8c9f576-mvvfg                       1/1     Running   0          18m
capg-controller-manager-7f8bc6699f-f9vbh                       1/1     Running   0          18m
capi-controller-manager-7666b86bcc-qzdqc                       1/1     Running   0          19m
capi-ipam-in-cluster-controller-manager-68d4694bb4-dclj2       1/1     Running   0          19m
capi-ipam-infoblox-controller-manager-5c76bc45b-cwh6g          1/1     Running   0          19m
capo-controller-manager-b5b5c65bd-cxksm                        1/1     Running   0          18m
capv-controller-manager-67674cc985-2qdmn                       1/1     Running   0          18m
capz-controller-manager-b7dbff77-q569b                         1/1     Running   0          18m
helm-controller-5b6bbd6968-4w6ln                               1/1     Running   0          23m
k0smotron-controller-manager-bootstrap-5cd9cb9b75-vdff4        1/1     Running   0          19m
k0smotron-controller-manager-control-plane-7776f8f694-zf75g    1/1     Running   0          19m
k0smotron-controller-manager-infrastructure-5cdbc6b6d5-5c825   1/1     Running   0          18m
kcm-cert-manager-657f64dbcb-f2r98                              1/1     Running   0          23m
kcm-cert-manager-cainjector-7bc4bddd94-29qxh                   1/1     Running   0          23m
kcm-cert-manager-webhook-598b5c4d9c-77fb4                      1/1     Running   0          23m
kcm-cluster-api-operator-7d86849496-szdw2                      1/1     Running   0          20m
kcm-controller-manager-6d79df9759-d66fz                        1/1     Running   0          20m
kcm-rbac-manager-757798cd54-d4pjw                              1/1     Running   0          23m
kcm-regional-telemetry-66f675fdf5-44f44                        1/1     Running   0          23m
source-controller-5d7986cdd-9gblh                              1/1     Running   0          23m
velero-67dc7b7dff-5mvcs                                        1/1     Running   0          23m
```

```bash
kubectl get pods -n kcm-system --no-headers | wc -l
```

```console { .no-copy }
23
```

State management is handled by Project Sveltos, so you'll want to make sure that all 10 pods are running/completed in the `projectsveltos` namespace:

```bash
kubectl get pods -n projectsveltos
```

```console { .no-copy }
NAME                                      READY   STATUS    RESTARTS   AGE
access-manager-74b7c98d8b-npj6t           1/1     Running   0          20m
addon-controller-6ddb848fdf-5vpnc         1/1     Running   0          20m
classifier-manager-57d5779966-ft9vs       1/1     Running   0          20m
event-manager-5569df975f-4cgrf            1/1     Running   0          20m
hc-manager-66c559fff6-l6xnx               1/1     Running   0          20m
mcp-server-55459fdccf-sg4lj               1/1     Running   0          20m
sc-manager-56ccc48477-lvz66               1/1     Running   0          20m
shard-controller-6b65cd4f8f-kmpps         1/1     Running   0          20m
sveltos-agent-manager-97d78f4bb-hqjm6     1/1     Running   0          19m
techsupport-controller-797459769b-wwg6h   1/1     Running   0          20m
```

```bash
kubectl get pods -n projectsveltos --no-headers | wc -l
```

```console { .no-copy }
10
```

If any of these pods are missing, simply give {{{ docsVersionInfo.k0rdentName }}} more time. If there's a problem, you'll see pods crashing and restarting, and you can see what's happening by describing the pod, as in:

```bash
kubectl describe pod classifieclassifier-manager-5b47b66fc9-5mtwl -n projectsveltos
```

As long as you're not seeing pod restarts, you just need to wait a few minutes.

## Verify the templates

Next verify whether the KCM templates have been successfully installed and reconciled. Start with the `ProviderTemplate` objects:

```bash
kubectl get providertemplate -n kcm-system
```
```console { .no-copy }
NAME                                   VALID
cluster-api-{{{ extra.docsVersionInfo.providerVersions.dashVersions.clusterApi }}}                                 true
cluster-api-provider-aws-{{{ docsVersionInfo.providerVersions.dashVersions.clusterApiProviderAws }}}                    true
cluster-api-provider-azure-{{{ docsVersionInfo.providerVersions.dashVersions.clusterApiProviderAzure }}}                 true
cluster-api-provider-docker-{{{ docsVersionInfo.providerVersions.dashVersions.clusterApiProviderDocker }}}                 true
cluster-api-provider-gcp-{{{ docsVersionInfo.providerVersions.dashVersions.clusterApiProviderGcp }}}                    true
cluster-api-provider-infoblox-{{{ docsVersionInfo.providerVersions.dashVersions.clusterApiProviderInfoblox }}}               true
cluster-api-provider-ipam-{{{ docsVersionInfo.providerVersions.dashVersions.clusterApiProviderIpam }}}                   true
cluster-api-provider-k0sproject-k0smotron-{{{ docsVersionInfo.providerVersions.dashVersions.k0smotron }}}  true
cluster-api-provider-openstack-{{{ docsVersionInfo.providerVersions.dashVersions.clusterApiProviderOpenstack }}}             true
cluster-api-provider-vsphere-{{{ docsVersionInfo.providerVersions.dashVersions.clusterApiProviderVsphere }}}                true
kcm-{{{ docsVersionInfo.k0rdentVersion }}}                                     true
kcm-regional-{{{ docsVersionInfo.providerVersions.dashVersions.regional }}}                            true
projectsveltos-{{{ docsVersionInfo.providerVersions.dashVersions.sveltosProvider }}}                              true
```

Make sure that all templates are not just installed, but valid. Again, this may take a few minutes.

You'll also want to make sure the `ClusterTemplate` objects are installed and valid:

```bash
kubectl get clustertemplate -n kcm-system
```
```console { .no-copy }
NAME                             VALID
adopted-cluster-{{{ docsVersionInfo.providerVersions.dashVersions.clusterApi }}}            true
aws-eks-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsEksCluster }}}                    true
aws-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsHostedCpCluster }}}             true
aws-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsStandaloneCpCluster }}}         true
azure-aks-{{{ extra.docsVersionInfo.providerVersions.dashVersions.azureAksCluster }}}                  true
azure-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.azureHostedCpCluster }}}           true
azure-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.azureStandaloneCpCluster }}}       true
docker-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.azureHostedCpCluster }}}          true
gcp-gke-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsEksCluster }}}                    true
gcp-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsHostedCpCluster }}}             true
gcp-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsStandaloneCpCluster }}}         true
openstack-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.openstackStandaloneCpCluster }}}       true
openstack-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.openstackStandaloneCpCluster }}}   true
remote-cluster-{{{ extra.docsVersionInfo.providerVersions.dashVersions.remoteCluster }}}            true
vsphere-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.vsphereHostedCpCluster }}}         true
vsphere-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.vsphereStandaloneCpCluster }}}     true
```

## Verify {{{ docsVersionInfo.k0rdentName }}} status

The final test of whether {{{ docsVersionInfo.k0rdentName }}} installation is installed is making sure the
status of the `Management` object itself is `True`:

```bash
kubectl get management -n kcm-system
```
```console { .no-copy }
NAME   READY   RELEASE         AGE
kcm    True    kcm-{{{ docsVersionInfo.k0rdentVersion}}}   18m
```
