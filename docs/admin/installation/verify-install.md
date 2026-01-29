# Confirming the deployment

> NOTE:
> After running the helm install command, please wait 5 to 10 minutes for the deployment to stabilize.

To understand whether installation is complete, start by making sure all pods are ready in the `kcm-system` namespace. There should be 21 pod entries:

```bash
kubectl get pods -n kcm-system
```

```console { .no-copy }
NAME                                                           READY   STATUS    RESTARTS   AGE
azureserviceoperator-controller-manager-58bb68bc75-9ml6f       1/1     Running   0          8h
capa-controller-manager-d84cc5796-86wf7                        1/1     Running   0          8h
capd-controller-manager-74b8c9f576-m8dxk                       1/1     Running   0          8h
capg-controller-manager-7f8bc6699f-lb988                       1/1     Running   0          8h
capi-controller-manager-79db96b978-68wtf                       1/1     Running   0          8h
capi-ipam-in-cluster-controller-manager-68d4694bb4-kmrp5       1/1     Running   0          8h
capi-ipam-infoblox-controller-manager-5c76bc45b-brrtv          1/1     Running   0          8h
capk-controller-manager-d95b4487b-ldcrr                        1/1     Running   0          8h
capo-controller-manager-b5b5c65bd-h59wx                        1/1     Running   0          8h
capv-controller-manager-5c47d75597-lkgrh                       1/1     Running   0          8h
capz-controller-manager-b7dbff77-fbc2r                         1/1     Running   0          8h
helm-controller-76bd49f44b-fbnhj                               1/1     Running   0          8h
k0smotron-controller-manager-bootstrap-5cd9cb9b75-2q2kj        1/1     Running   0          8h
k0smotron-controller-manager-control-plane-7776f8f694-78knr    1/1     Running   0          8h
k0smotron-controller-manager-infrastructure-5cdbc6b6d5-s4ppb   1/1     Running   0          8h
kcm-cert-manager-67f468cb5d-rr4fq                              1/1     Running   0          8h
kcm-cert-manager-cainjector-5b669dfcc-cjb54                    1/1     Running   0          8h
kcm-cert-manager-webhook-575596f6b6-qf8s9                      1/1     Running   0          8h
kcm-cluster-api-operator-7d86849496-g74v2                      1/1     Running   0          8h
kcm-controller-manager-86d748b49c-znmb8                        1/1     Running   0          8h
kcm-rbac-manager-bdf9b4b8-9shrs                                1/1     Running   0          8h
kcm-regional-telemetry-8499966b87-54hf6                        1/1     Running   0          8h
source-controller-694fb4cd65-4jskk                             1/1     Running   0          8h
velero-699d774b66-xqwqv                                        1/1     Running   0          8h
```

```bash
kubectl get pods -n kcm-system --no-headers | wc -l
```

```console { .no-copy }
24
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
cluster-api-provider-aws-{{{ docsVersionInfo.providerVersions.dashVersions.clusterApiProviderAws }}}                   true
cluster-api-provider-azure-{{{ docsVersionInfo.providerVersions.dashVersions.clusterApiProviderAzure }}}                 true
cluster-api-provider-docker-{{{ docsVersionInfo.providerVersions.dashVersions.clusterApiProviderDocker }}}                 true
cluster-api-provider-gcp-{{{ docsVersionInfo.providerVersions.dashVersions.clusterApiProviderGcp }}}                    true
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
