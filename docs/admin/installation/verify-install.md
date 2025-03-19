# Confirming the deployment

> NOTE:
> After running the helm install command, please wait 5 to 10 minutes for the deployment to stabilize.

To understand whether installation is complete, start by making sure all pods are ready in the `kcm-system` namespace. There should be 17 pod entries:

```shell
kubectl get pods -n kcm-system
```
```console
NAME                                                          READY   STATUS    RESTARTS   AGE
azureserviceoperator-controller-manager-6b4dd86894-2m2wh      1/1     Running   0          57s
capa-controller-manager-64bbcb9f8-kx6wr                       1/1     Running   0          2m3s
capi-controller-manager-66f8998ff5-2m5m2                      1/1     Running   0          2m32s
capo-controller-manager-588f45c7cf-lmkgz                      1/1     Running   0          50s
capv-controller-manager-69f7fc65d8-wbqh8                      1/1     Running   0          46s
capz-controller-manager-544845f786-q8rzn                      1/1     Running   0          57s
helm-controller-7644c4d5c4-t6sjm                              1/1     Running   0          5m1s
k0smotron-controller-manager-bootstrap-9fc48d76f-hppzs        2/2     Running   0          2m9s
k0smotron-controller-manager-control-plane-7df9bc7bf-74vcs    2/2     Running   0          2m4s
k0smotron-controller-manager-infrastructure-f7f94dd76-ppzq4   2/2     Running   0          116s
kcm-cert-manager-895954d88-jplf6                              1/1     Running   0          5m1s
kcm-cert-manager-cainjector-685ffdf549-qlj8m                  1/1     Running   0          5m1s
kcm-cert-manager-webhook-59ddc6b56-8hfml                      1/1     Running   0          5m1s
kcm-cluster-api-operator-8487958779-l9lvf                     1/1     Running   0          3m12s
kcm-controller-manager-7998cdb69-x7kd9                        1/1     Running   0          3m12s
kcm-velero-b68fd5957-fwg2l                                    1/1     Running   0          5m1s
source-controller-6cd7676f7f-7kpjn                            1/1     Running   0          5m1s
```

```shell
kubectl get pods -n kcm-system --no-headers | wc -l
```
```console
17
```

State management is handled by Project Sveltos, so you'll want to make sure that all 9 pods are running/completed in the `projectsveltos` namespace:

```shell
kubectl get pods -n projectsveltos
```

```console
NAME                                     READY   STATUS      RESTARTS   AGE
access-manager-56696cc7f-5txlb           1/1     Running     0          4m1s
addon-controller-7c98776c79-dn9jm        1/1     Running     0          4m1s
classifier-manager-7b85f96469-666jx      1/1     Running     0          4m1s
event-manager-67f6db7f44-hsnnj           1/1     Running     0          4m1s
hc-manager-6d579d675f-fgvk2              1/1     Running     0          4m1s
register-mgmt-cluster-job-rfkdh          0/1     Completed   0          4m1s
sc-manager-55c99d494b-c8wrl              1/1     Running     0          4m1s
shard-controller-5ff9cd796d-tlg79        1/1     Running     0          4m1s
sveltos-agent-manager-7467959f4f-lsnd5   1/1     Running     0          3m34s
```
```shell
kubectl get pods -n projectsveltos --no-headers | wc -l
```
```console
9
```


If any of these pods are missing, simply give {{{ docsVersionInfo.k0rdentName }}} more time. If there's a problem, you'll see pods crashing and restarting, and you can see what's happening by describing the pod, as in:

```shell
kubectl describe pod classifier-manager-7b85f96469-666jx -n projectsveltos
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

Next verify whether the KCM templates have been successfully installed and reconciled.  Start with the `ProviderTemplate` objects:

```shell
kubectl get providertemplate -n kcm-system
```

```console
NAME                                   VALID
cluster-api-{{{ extra.docsVersionInfo.k0rdentVersion }}}                      true
cluster-api-provider-aws-{{{ extra.docsVersionInfo.k0rdentVersion }}}         true
cluster-api-provider-azure-{{{ extra.docsVersionInfo.k0rdentVersion }}}       true
cluster-api-provider-openstack-{{{ extra.docsVersionInfo.k0rdentVersion }}}   true
cluster-api-provider-vsphere-{{{ extra.docsVersionInfo.k0rdentVersion }}}     true
k0smotron-{{{ extra.docsVersionInfo.k0rdentVersion }}}                        true
kcm-{{{ extra.docsVersionInfo.k0rdentVersion }}}                              true
projectsveltos-0-45-0                  true
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
openstack-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.openstackStandaloneCpCluster }}}   true
vsphere-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.vsphereHostedCpCluster }}}         true
vsphere-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.vsphereStandaloneCpCluster }}}     true
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
