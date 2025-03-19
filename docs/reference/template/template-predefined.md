## Remove Templates shipped with {{{ docsVersionInfo.k0rdentName }}}

If you need to limit the templates that exist in your {{{ docsVersionInfo.k0rdentName }}} installation, follow the instructions below:

1. Get the list of `ProviderTemplate`, `ClusterTemplate` or `ServiceTemplate` objects shipped with {{{ docsVersionInfo.k0rdentName }}}. For example,
for `ClusterTemplate` objects, run:

    ```bash
    kubectl get clustertemplates -n kcm-system -l helm.toolkit.fluxcd.io/name=kcm-templates
    ```
    ```console
    NAMESPACE    NAME                            VALID
    kcm-system   adopted-cluster-{{{ extra.docsVersionInfo.k0rdentVersion }}}           true
    kcm-system   aws-eks-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsEksCluster }}}                   true
    kcm-system   aws-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsHostedCpCluster }}}             true
    kcm-system   aws-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.awsStandaloneCpCluster }}}         true
    kcm-system   azure-aks-{{{ extra.docsVersionInfo.providerVersions.dashVersions.azureAksCluster }}}                 true
    kcm-system   azure-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.azureHostedCpCluster }}}           true
    kcm-system   azure-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.azureStandaloneCpCluster }}}       true
    kcm-system   openstack-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.openstackStandaloneCpCluster }}}   true
    kcm-system   vsphere-hosted-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.vsphereHostedCpCluster }}}         true
    kcm-system   vsphere-standalone-cp-{{{ extra.docsVersionInfo.providerVersions.dashVersions.vsphereStandaloneCpCluster }}}     true
    ```

2. Remove the template from the list using `kubectl delete`, as in:

    ```bash
    kubectl delete clustertemplate -n kcm-system <template-name>
    ```