# Roles summary

> NOTE:
> The names of the `ClusterRole` objects may have different prefixes depending on the name of the {{{ docsVersionInfo.k0rdentName }}} Helm chart.
> The `ClusterRole` object definitions below use the `kcm` prefix, which is the default name of the {{{ docsVersionInfo.k0rdentName }}} Helm chart.

## Global Admin

The `Global Admin` role provides full administrative access across all the {{{ docsVersionInfo.k0rdentName }}} system.

**Name**: `kcm-global-admin-role`

**Aggregation Rule**: Includes all `ClusterRoles` with the labels:

* `k0rdent.mirantis.com/aggregate-to-global-admin: true`
* `k0rdent.mirantis.com/aggregate-to-namespace-admin: true`
* `k0rdent.mirantis.com/aggregate-to-namespace-editor: true`

**Permissions**:

1. Full access to the {{{ docsVersionInfo.k0rdentName }}} API
2. Full access to Flux Helm repositories and Helm charts
3. Full access to Cluster API identities
4. Full access to namespaces and secrets

**Use case**

A user with the `Global Admin` role is authorized to perform the following actions:

1. Manage the {{{ docsVersionInfo.k0rdentName }}} configuration
2. Manage namespaces in the management cluster
3. Manage `ProviderTemplate` objects: add new templates or remove unneeded ones
4. Manage `ClusterTemplate` and `ServiceTemplate` objects in any namespace, including adding and removing templates
5. Manage Flux `HelmRepository` and `HelmChart` objects in any namespace
6. Manage access rules for `ClusterTemplate` and `ServiceTemplate` objects, including distributing templates across namespaces using
   `TemplateChain` objects
7. Manage upgrade sequences for `ClusterTemplate` and `ServiceTemplate` objects
8. Manage and deploy Services across multiple clusters in any namespace by modifying `MultiClusterService` resources
9. Manage `ClusterDeployment` objects in any namespace
10. Manage `Credential` and `Secret` objects in any namespace
11. Upgrade {{{ docsVersionInfo.k0rdentName }}}
12. Uninstall {{{ docsVersionInfo.k0rdentName }}}


## Global Viewer

The `Global Viewer` role grants read-only access across the {{{ docsVersionInfo.k0rdentName }}} system. It does not permit any modifications,
including the creation of clusters.

**Name**: `kcm-global-viewer-role`

**Aggregation Rule**: Includes all `ClusterRole` objects with the labels:

* `k0rdent.mirantis.com/aggregate-to-global-viewer: true`
* `k0rdent.mirantis.com/aggregate-to-namespace-viewer: true`

**Permissions**:

1. Read access to {{{ docsVersionInfo.k0rdentName }}} API
2. Read access to Flux Helm repositories and Helm charts
3. Read access to Cluster API identities
4. Read access to namespaces and secrets

**Use case**

A user with the `Global Viewer` role is authorized to perform the following actions:

1. View the {{{ docsVersionInfo.k0rdentName }}} configuration
2. List namespaces available in the management cluster
3. List and get the detailed information about available `ProviderTemplate` objects
4. List available `ClusterTemplate` and `ServiceTemplate` objects in any namespace
5. List and view detailed information about Flux `HelmRepository` and `HelmChart` objects in any namespace
6. View access rules for `ClusterTemplate` and `ServiceTemplate` objects, including `TemplateChain` objects in any namespace
7. View full details about the created `MultiClusterService` objects
8. List and view detailed information about `ClusterDeployment` objects in any namespace
9. List and view detailed information about created `Credential` and `Secret` objects in any namespace

## Namespace Admin

The `Namespace Admin` role provides full administrative access within a namespace.

**Name**: `kcm-namespace-admin-role`

**Aggregation Rule**: Includes all `ClusterRole` objects with the labels:

* `k0rdent.mirantis.com/aggregate-to-namespace-admin: true`
* `k0rdent.mirantis.com/aggregate-to-namespace-editor: true`

**Permissions**:

1. Full access to `ClusterDeployment`, `Credential`, `ClusterTemplate` and `ServiceTemplate` objects in the namespace
2. Full access to `TemplateChain` objects in the namespace
3. Full access to Flux `HelmRepository` and `HelmChart` objects in the namespace

**Use case**

A user with the `Namespace Admin` role is authorized to perform the following actions within the namespace:

1. Create and manage all `ClusterDeployment` objects in the namespace
2. Create and manage `ClusterTemplate` and `ServiceTemplate` objects in the namespace
3. Manage the distribution and upgrade sequences of Templates within the namespace
4. Create and manage Flux `HelmRepository` and `HelmChart` objects in the namespace
5. Manage `Credential` objects created by any user in the namespace


## Namespace Editor

The `Namespace Editor` role allows users to create and modify `ClusterDeployment` objects within namespace using predefined
`Credential` and `Template` objects.

**Name**: `kcm-namespace-editor-role`

**Aggregation Rule**: Includes all `ClusterRole` objects with the labels:

* `k0rdent.mirantis.com/aggregate-to-namespace-editor: true`

**Permissions**:

1. Full access to `ClusterDeployment` objects in the allowed namespace
2. Read access to `Credential`, `ClusterTemplate` and `ServiceTemplate`, and `TemplateChain` objects in the namespace
3. Read access to Flux `HelmRepository` and `HelmChart` objects in the namespace

**Use case**

A user with the `Namespace Editor` role has the following permissions in the namespace:

1. Can create and manage `ClusterDeployment` objects in the namespace using existing `Credential` and `Template` objects
2. Can list and view detailed information about the `Credential` objects available in the namespace
3. Can list and view detailed information about the available `ClusterTemplate` and `ServiceTemplate` objects and the `Template`  upgrade sequences
4. Can list and view detailed information about the Flux `HelmRepository` and `HelmChart` objects


## Namespace Viewer

The `Namespace Viewer` role grants read-only access to resources within a namespace.

**Name**: `kcm-namespace-viewer-role`

**Aggregation Rule**: Includes all `ClusterRole` objects with the labels:

* `k0rdent.mirantis.com/aggregate-to-namespace-viewer: true`

**Permissions**:

1. Read access to `ClusterDeployment` objects in the namespace
2. Read access to `Credential`, `ClusterTemplate`, `ServiceTemplate`, and `TemplateChain` objects in the namespace
3. Read access to Flux `HelmRepository` and `HelmChart` objects in the namespace

**Use case**

A user with the `Namespace Viewer` role has the following permissions in the namespace:

1. Can list and view detailed information about all the `ClusterDeployment` objects in the allowed namespace
2. Can list and view detailed information about `Credential` objects available in the specific namespace
3. Can list and view detailed information about available `ClusterTemplate` and `ServiceTemplate` objects, and `Template`
   upgrade sequences
4. Can list and view detailed information about Flux `HelmRepository` and `HelmChart` objects

