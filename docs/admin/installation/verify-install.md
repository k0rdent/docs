# Confirming the deployment

> NOTE:
> After running the helm install command, please wait 5 to 10 minutes for the deployment to stabilize.

To understand whether installation is complete, start by making sure all pods are ready in the `kcm-system` namespace. There should be 20 pod entries:

```shell
kubectl get pods -n kcm-system
```

```console
NAME                                                           READY   STATUS    RESTARTS   AGE
azureserviceoperator-controller-manager-6b4dd86894-4dpfc       1/1     Running   0          7m15s
capa-controller-manager-64bbcb9f8-ltj6z                        1/1     Running   0          6m58s
capd-controller-manager-7586b6577c-6w4wq                       1/1     Running   0          7m11s
capg-controller-manager-774958b9b9-hvxvv                       1/1     Running   0          6m54s
capi-controller-manager-5b67d4fc7-dhk7p                        1/1     Running   0          8m49s
capo-controller-manager-6f98bb68cd-vsc24                       1/1     Running   0          6m33s
capv-controller-manager-69f7fc65d8-jx8s4                       1/1     Running   0          6m40s
capz-controller-manager-5b87fdf745-mzm7x                       1/1     Running   0          7m15s
helm-controller-746d7db585-x64ld                               1/1     Running   0          11m
k0smotron-controller-manager-bootstrap-67dd88d848-wfrhm        2/2     Running   0          8m32s
k0smotron-controller-manager-control-plane-657f5578d4-7vb8t    2/2     Running   0          8m24s
k0smotron-controller-manager-infrastructure-5867d575f9-t28hp   2/2     Running   0          6m46s
kcm-cert-manager-6979c67bc4-b6s4w                              1/1     Running   0          11m
kcm-cert-manager-cainjector-5b97c84fdb-kdsw5                   1/1     Running   0          11m
kcm-cert-manager-webhook-755796f599-q6727                      1/1     Running   0          11m
kcm-cluster-api-operator-65c8f75569-rfsp2                      1/1     Running   0          9m30s
kcm-controller-manager-68b56bff85-6fmsp                        1/1     Running   0          9m30s
kcm-velero-67bf545995-x6784                                    1/1     Running   0          11m
source-controller-74b597b995-kkqqw                             1/1     Running   0          11m
```

```shell
kubectl get pods -n kcm-system --no-headers | wc -l
```

```console
20
```

State management is handled by Project Sveltos, so you'll want to make sure that all 10 pods are running/completed in the `projectsveltos` namespace:

```shell
kubectl get pods -n projectsveltos
```

```console
NAME                                      READY   STATUS    RESTARTS   AGE
access-manager-6696df779-pnxjx            1/1     Running   0          10m
addon-controller-6cb6c5f6df-zmfch         1/1     Running   0          10m
classifier-manager-5b47b66fc9-5mtwl       1/1     Running   0          10m
event-manager-564d6644b4-wr9cq            1/1     Running   0          10m
hc-manager-7c56c59d9c-w5gds               1/1     Running   0          10m
sc-manager-6798cd9d4d-r7z9j               1/1     Running   0          10m
shard-controller-797965bb58-65lmp         1/1     Running   0          10m
sveltos-agent-manager-5445f6f57c-wxw2s    1/1     Running   0          10m
techsupport-controller-5b666d6884-jfqnp   1/1     Running   0          10m
```

```shell
kubectl get pods -n projectsveltos --no-headers | wc -l
```

```console
10
```

If any of these pods are missing, simply give {{{ docsVersionInfo.k0rdentName }}} more time. If there's a problem, you'll see pods crashing and restarting, and you can see what's happening by describing the pod, as in:

```shell
kubectl describe pod classifieclassifier-manager-5b47b66fc9-5mtwl -n projectsveltos
```

As long as you're not seeing pod restarts, you just need to wait a few minutes.

## Verify that {{{ docsVersionInfo.k0rdentName }}} itself is ready

The actual measure of whether {{{ docsVersionInfo.k0rdentName }}} is ready is the state of the `Management` object. To check, issue this command:

```shell
kubectl get Management -n kcm-system
```

```console
NAME   READY   RELEASE     AGE
kcm    True    kcm-{{{ extra.docsVersionInfo.k0rdentVersion }}}   9m
```

## Verify the templates

Next verify whether the KCM templates have been successfully installed and reconciled. Start with the `ProviderTemplate` objects:

```shell
kubectl get providertemplate -n kcm-system
```

```console
NAME                                   VALID
cluster-api-{{{ extra.docsVersionInfo.providerVersions.dashVersions.clusterApi }}}                                 true
cluster-api-provider-aws-{{{ docsVersionInfo.providerVersions.dashVersions.clusterApiProviderAws }}}                    true
cluster-api-provider-azure-{{{ docsVersionInfo.providerVersions.dashVersions.clusterApiProviderAzure }}}                  true
cluster-api-provider-docker-{{{ docsVersionInfo.providerVersions.dashVersions.clusterApiProviderDocker }}}                 true
cluster-api-provider-gcp-{{{ docsVersionInfo.providerVersions.dashVersions.clusterApiProviderGcp }}}                    true
cluster-api-provider-k0sproject-k0smotron-{{{ docsVersionInfo.providerVersions.dashVersions.k0smotron }}}   true
cluster-api-provider-openstack-{{{ docsVersionInfo.providerVersions.dashVersions.clusterApiProviderOpenstack }}}              true
cluster-api-provider-vsphere-{{{ docsVersionInfo.providerVersions.dashVersions.clusterApiProviderVsphere }}}                true
k0smotron-{{{ docsVersionInfo.providerVersions.dashVersions.k0smotron }}}                                   true
kcm-{{{ docsVersionInfo.k0rdentVersion }}}                                         true
projectsveltos-{{{ docsVersionInfo.providerVersions.dashVersions.sveltosProvider }}}                             true
```

Make sure that all templates are not just installed, but valid. Again, this may take a few minutes.

You'll also want to make sure the `ClusterTemplate` objects are installed and valid:

```shell
kubectl get clustertemplate -n kcm-system
```

```console
NAME                            VALID
adopted-cluster-{{{ extra.docsVersionInfo.k0rdentVersion }}}           true
aws-eks-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsEksCluster }}}                   true
aws-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsHostedCpCluster }}}             true
aws-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsStandaloneCpCluster }}}         true
azure-aks-{{{ extra.docsVersionInfo.providerVersions.dashVersions.azureAksCluster }}}                 true
azure-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.azureHostedCpCluster }}}           true
azure-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.azureStandaloneCpCluster }}}       true
docker-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.azureHostedCpCluster }}}           true
gcp-gke-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsEksCluster }}}                   true
gcp-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsHostedCpCluster }}}             true
gcp-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsStandaloneCpCluster }}}         true
openstack-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.openstackStandaloneCpCluster }}}   true
remote-cluster-{{{ extra.docsVersionInfo.providerVersions.dashVersions.openstackStandaloneCpCluster }}}   true
vsphere-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.vsphereHostedCpCluster }}}         true
vsphere-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.vsphereStandaloneCpCluster }}}     true
```

If this is a new `v0.2.0` cluster, you will see:

```shell
No resources found in kcm-system namespace.
```

You can then install the `ServiceTemplates` objects as follows:

```shell
helm upgrade --install catalog-core oci://ghcr.io/k0rdent/catalog/charts/catalog-core --version 1.0.0 -n kcm-system
```

Finally, make sure the `ServiceTemplate` objects are installed and valid:

```shell
kubectl get servicetemplate -n kcm-system
```

```console
NAME                      VALID
cert-manager-1-16-2       true
dex-0-19-1                true
external-secrets-0-11-0   true
ingress-nginx-4-11-0      true
ingress-nginx-4-11-3      true
kyverno-3-2-6             true
velero-8-1-0              true
```
