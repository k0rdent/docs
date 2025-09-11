# Frequently Asked Questions

**Q: What is the best way to upgrade the Kubernetes version of a {{{ docsVersionInfo.k0rdentName }}} child cluster?**

A: The simplest way to change the Kubernetes version of a specific child cluster is by updating the `ClusterDeployment` object. Set the `spec.config.k0s.version` value to the desired Kubernetes version. 

If you change the Kubernetes version used in a `ClusterTemplate`, all `ClusterDeployments` based on that template will be upgraded to the new version.

You can also [create a new `ClusterTemplate`](../templatehowto/index.md) that will set the version for new clusters created based on that template.

**Q: Is it possible to control the version of the provider in the KCM Management object? For example, what if {{{ docsVersionInfo.k0rdentName }}} is using the Kubernetes Cluster API for OpenStack (CAPO) v0.12.4 but I want to use v0.12.2?**

A: You can change the Kubernetes Cluster API version by [creating a new `ProviderTemplate`](../templatehowto/index.md) that references a Helm chart with the appropriate provider components (with either the desired version hardcoded or configurable via `values.yaml`), then updating the `Management` object to reference that template. For example, you could [update the `Management` object](../appendix/appendix-extend-mgmt.md) to specify a new template for the OpenStack provider:

```yaml
spec:
  providers:
  - name: cluster-api-provider-openstack
    template: new-capo-provider-template-name
```

