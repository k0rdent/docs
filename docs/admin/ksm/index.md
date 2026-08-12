# {{{ docsVersionInfo.k0rdentName }}} State Management

{{{ docsVersionInfo.k0rdentName }}} State Management (KSM) provides capabilities to manage workloads for k0rdent-managed child Kubernetes clusters.
It enables centralized management for applications and auxiliary resources deployed to child clusters. KSM leverage [ProjectSveltos](https://projectsveltos.github.io/sveltos/main/) as built-in CD solution.
Despite of built-in provider, KSM is designed with provider-agnostic capabilities. This allows users to develop their own providers with other underlying CD solution.

* **Centralized Management**: KSM allows to define which services would be installed to which clusters using declaratively defined resources in management cluster.

* **Provider Agnostic**: KSM allows you to develop custom providers to reconcile k0rdent API resources in a user-defined manner.

## Guides

Get started with the basic documentation:

- [KSM Providers](ksm-providers.md)
- [Built-In Provider](ksm-built-in-provider.md)
- [Build-Your-Own CD Provider](ksm-byo-provider.md)
- [Service State Verification](ksm-service-state-verification.md)
- [Service Templates](ksm-service-templates.md)
- [Deploy services to multiple clusters](ksm-multiclusterservice.md)
- [Deploy services to management cluster](ksm-self-management.md)
