# Roles Management

{{{ docsVersionInfo.k0rdentName }}} now includes the [Fairwinds RBAC Manager](https://rbac-manager.docs.fairwinds.com/)
as part of the management cluster.

The RBAC Manager is an operator that simplifies Kubernetes authorization.
Instead of manually creating Roles, ClusterRoles, RoleBindings, ClusterRoleBindings, or ServiceAccounts, you
declare the desired state using a `RBACDefinition` custom resource. RBAC Manager then automatically creates
and maintains the required RBAC objects.

## Usage Example

```yaml
apiVersion: rbacmanager.reactiveops.io/v1beta1
kind: RBACDefinition
metadata:
  name: rbac-manager-example
rbacBindings:
  - name: cluster-admins
    subjects:
      - kind: User
        name: kate@example.com
    clusterRoleBindings:
      - clusterRole: kcm-global-admin-role
  - name: backend-developers
    subjects:
      - kind: User
        name: michael@example.com
      - kind: User
        name: alexey@example.com
    roleBindings:
      - clusterRole: kcm-namespace-admin-role
        namespace: dev
      - clusterRole: kcm-namespace-viewer-role
        namespace: test
  - name: testers
    subjects:
      - kind: User
        name: jack@example.com
    roleBindings:
      - clusterRole: kcm-namespace-admin-role
        namespace: test
  - name: ci-bot
    subjects:
      - kind: ServiceAccount
        name: ci-bot
        namespace: kcm-system
    roleBindings:
      - clusterRole: edit
        namespaceSelector:
          matchExpressions:
            - key: name
              operator: In
              values:
                - projectsveltos
                - kcm-system
```

From the example above, RBAC Manager will generate:

1. `ClusterRoleBinding` granting Kate the `kcm-global-admin-role`, providing full administrative access across
the entire {{{ docsVersionInfo.k0rdentName }}} system.
2. `RoleBinding` that gives Michael and Alexey `kcm-namespace-admin-role` with full administrative access across
the `dev` namespace and `kcm-namespace-viewer-role` with read-only access in the `test` namespace.
3. `RoleBinding` granting Jack `kcm-namespace-admin-role` in the `test` namespace.
4. A `ServiceAccount` named `ci-bot` in the `kcm-system` namespace.
5. `RoleBindings` that grant the `ci-bot` ServiceAccount `edit` access in `projectsveltos` and `kcm-system` namespaces
using namespace selector.

See [RBACDefinition Examples](https://github.com/FairwindsOps/rbac-manager/tree/master/examples) for more examples of
the `RBACDefinition` resource.

> NOTE:
> The names of the `ClusterRole` objects may have different prefixes depending on the name of the {{{ docsVersionInfo.k0rdentName }}} Helm chart.
> The `ClusterRole` object definitions below use the `kcm` prefix, which is the default name of the {{{ docsVersionInfo.k0rdentName }}} Helm chart.

See [Roles Summary](roles-summary.md) for more details about standard {{{ docsVersionInfo.k0rdentName }}} roles.
