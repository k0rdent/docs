# Roles Management

{{{ docsVersionInfo.k0rdentName }}} includes the [Fairwinds RBAC Manager](https://rbac-manager.docs.fairwinds.com/) as part of the management cluster.

The RBAC Manager is an operator that simplifies Kubernetes authorization. Instead of manually creating `Roles`, `ClusterRoles`, `RoleBindings`, `ClusterRoleBindings`, or `ServiceAccounts`, you declare the desired state using an `RBACDefinition` custom resource. RBAC Manager then creates and maintains the required RBAC objects.

This allows you to manage authorization declaratively using a single resource.

## How RBAC Manager Works

RBAC Manager watches for `RBACDefinition` resources and reconciles them into the corresponding Kubernetes RBAC objects, keeping the actual cluster state aligned with the declared intent.

## Example RBACDefinition

The following example defines four distinct RBAC bindings:

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

## Resulting RBAC Objects

From the example above, RBAC Manager generates:

1. A `ClusterRoleBinding` that grants Kate the `kcm-global-admin-role`, providing full administrative access across the entire {{{ docsVersionInfo.k0rdentName }}} system.
2. A `RoleBinding` that grants Michael and Alexey the `kcm-namespace-admin-role` in the `dev` namespace and the `kcm-namespace-viewer-role` in the `test` namespace.
3. A `RoleBinding` that grants Jack the `kcm-namespace-admin-role` in the `test` namespace.
4. A `ServiceAccount` named `ci-bot` in the `kcm-system` namespace.
5. `RoleBindings` that grant the `ci-bot` ServiceAccount `edit` access in the `projectsveltos` and `kcm-system` namespaces using a namespace selector rather than explicitly listing namespaces.

> NOTE:
> The names of the `ClusterRole` objects may vary depending on the Helm release name used during installation.
> The examples above use the `kcm` prefix, which is the default Helm release name for {{{ docsVersionInfo.k0rdentName }}}.

## Further Reading

* [RBACDefinition Examples](https://github.com/FairwindsOps/rbac-manager/tree/master/examples)
* [Roles Summary](roles-summary.md)
