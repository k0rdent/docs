# Confirming the deployment

> NOTE:
> After running the helm install command, please wait 5 to 10 minutes for the deployment to stabilize.

To understand whether installation is complete, start by making sure all pods are ready in the `kcm-system` namespace. There should be 27 pod entries:

```bash
kubectl get pods -n kcm-system
```

```console { .no-copy }
NAME                                                           READY   STATUS    RESTARTS   AGE
azureserviceoperator-controller-manager-557c4bc8dc-hs26b       1/1     Running   0          20h
azureserviceoperator-controller-manager-557c4bc8dc-wwxzr       1/1     Running   0          20h
capa-controller-manager-58554ddc78-htjst                       1/1     Running   0          20h
capd-controller-manager-659885cb55-2ns4b                       1/1     Running   0          20h
capg-controller-manager-7bc675f69b-x7wrz                       1/1     Running   0          20h
capi-controller-manager-78bdccfb94-kcddw                       1/1     Running   0          20h
capi-ipam-in-cluster-controller-manager-56c7bd877c-62bvk       1/1     Running   0          20h
capi-ipam-infoblox-controller-manager-548877ddb5-58pzg         1/1     Running   0          20h
capk-controller-manager-56d4bd4ccd-6z57q                       1/1     Running   0          20h
capo-controller-manager-7f77d84c58-fvv2n                       1/1     Running   0          20h
capv-controller-manager-64664f5cf4-9xsrp                       1/1     Running   0          20h
capz-controller-manager-669dffc9c7-7jssw                       1/1     Running   0          20h
helm-controller-5466948d9f-vsr7v                               1/1     Running   0          20h
k0smotron-controller-manager-bootstrap-5686664764-4ssh4        1/1     Running   0          20h
k0smotron-controller-manager-control-plane-6456dfd98-rq6xw     1/1     Running   0          20h
k0smotron-controller-manager-infrastructure-8479cbc858-2mv9x   1/1     Running   0          20h
kcm-cert-manager-76c7bcbcff-twckq                              1/1     Running   0          20h
kcm-cert-manager-cainjector-66c48469bb-dz99n                   1/1     Running   0          20h
kcm-cert-manager-webhook-f6587877f-vxpdw                       1/1     Running   0          20h
kcm-cluster-api-operator-684db579d6-m6gpq                      1/1     Running   0          20h
kcm-controller-manager-fbc544dcb-k474v                         1/1     Running   0          20h
kcm-rbac-manager-7579db64d9-fltlw                              1/1     Running   0          20h
kcm-regional-telemetry-777886fdd-vmqtc                         1/1     Running   0          20h
kcm-reloader-fc9cbb8cf-bgq8b                                   1/1     Running   0          20h
orc-controller-manager-6fb5b76975-4pg7g                        1/1     Running   0          20h
source-controller-597784bdbb-8mb9g                             1/1     Running   0          20h
velero-5c95c499cf-jblr2                                        1/1     Running   0          20h
```

```bash
kubectl get pods -n kcm-system --no-headers | wc -l
```

```console { .no-copy }
27
```

State management is handled by Project Sveltos, so you'll want to make sure that all 11 pods are running/completed in the `projectsveltos` namespace:

```bash
kubectl get pods -n projectsveltos
```

```console { .no-copy }
NAME                                       READY   STATUS    RESTARTS   AGE
access-manager-c7fcff5-h86f9               1/1     Running   0          20h
addon-controller-69b4bc995-bn7nl           1/1     Running   0          20h
classifier-manager-6b4bf7ccd7-g74n6        1/1     Running   0          20h
drift-detection-manager-64cbb969d6-lqh5x   1/1     Running   0          20h
event-manager-88dd9795b-dmrwq              1/1     Running   0          20h
hc-manager-5d69454f9c-2pmdr                1/1     Running   0          20h
mcp-server-575979f9dd-pjgmx                1/1     Running   0          20h
sc-manager-8b59fb5c4-v9bl8                 1/1     Running   0          20h
shard-controller-f4cf55db6-78pjn           1/1     Running   0          20h
sveltos-agent-manager-75c9b8dc45-5mvdp     1/1     Running   0          20h
techsupport-controller-6589c84864-vfzhl    1/1     Running   0          20h
```

```bash
kubectl get pods -n projectsveltos --no-headers | wc -l
```

```console { .no-copy }
11
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
cluster-api-provider-aws-{{{ docsVersionInfo.providerVersions.dashVersions.clusterApiProviderAws }}}                   true
cluster-api-provider-azure-{{{ docsVersionInfo.providerVersions.dashVersions.clusterApiProviderAzure }}}                 true
cluster-api-provider-docker-{{{ docsVersionInfo.providerVersions.dashVersions.clusterApiProviderDocker }}}                true
cluster-api-provider-gcp-{{{ docsVersionInfo.providerVersions.dashVersions.clusterApiProviderGcp }}}                   true
cluster-api-provider-infoblox-{{{ docsVersionInfo.providerVersions.dashVersions.clusterApiProviderInfoblox }}}               true
cluster-api-provider-ipam-{{{ docsVersionInfo.providerVersions.dashVersions.clusterApiProviderIpam }}}                   true
cluster-api-provider-k0sproject-k0smotron-{{{ docsVersionInfo.providerVersions.dashVersions.k0smotron }}}  true
cluster-api-provider-openstack-{{{ docsVersionInfo.providerVersions.dashVersions.clusterApiProviderOpenstack }}}             true
cluster-api-provider-vsphere-{{{ docsVersionInfo.providerVersions.dashVersions.clusterApiProviderVsphere }}}               true
kcm-{{{ docsVersionInfo.k0rdentVersion }}}                                         true
kcm-regional-{{{ docsVersionInfo.providerVersions.dashVersions.regional }}}                                true
projectsveltos-{{{ docsVersionInfo.providerVersions.dashVersions.sveltosProvider }}}                              true
```

Make sure that all templates are not just installed, but valid. Again, this may take a few minutes.

You'll also want to make sure the `ClusterTemplate` objects are installed and valid:

```bash
kubectl get clustertemplate -n kcm-system
```
```console { .no-copy }
NAME                             VALID
adopted-cluster-{{{ docsVersionInfo.providerVersions.dashVersions.adoptedCluster }}}            true
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
