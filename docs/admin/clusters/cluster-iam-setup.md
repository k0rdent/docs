# Identity and Authorization Management

Identity and authorization are core to operating multi-cluster environments. {{{ docsVersionInfo.k0rdentName }}} provides a consistent mechanism for managing cluster authentication through the `ClusterAuthentication` resource.

This page focuses on **authentication configuration**—how Kubernetes API servers validate user identity. Authorization is handled separately through RBAC and role bindings.

By separating authentication policy from cluster templates and automating its propagation into hosted control planes, {{{ docsVersionInfo.k0rdentName }}} removes error-prone manual steps and provides a repeatable, auditable way to enforce identity across a fleet of clusters.

## ClusterAuthentication Resource

{{{ docsVersionInfo.k0rdentName }}} supports configuring authentication for child clusters through the `ClusterAuthentication` custom resource. A `ClusterAuthentication` object defines how the Kubernetes API server authenticates incoming requests.

It supports multiple JWT authenticators, each configurable with an issuer URL, audience validation, claim mappings, certificate authorities, and validation rules. Each `ClusterAuthentication` resource can be referenced by one or more `ClusterDeployment` objects.

### Example

The following example configures a cluster to authenticate users via a Dex identity provider using JWTs:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ClusterAuthentication
metadata:
  name: dex-cluster-auth
  namespace: my-namespace
spec:
  authenticationConfiguration:
    apiVersion: apiserver.config.k8s.io/v1beta1
    kind: AuthenticationConfiguration
    jwt:
      - issuer:
          url: https://dex.example.com:5556
          audiences:
            - example-app
        claimMappings:
          username:
            claim: email
            prefix: ""
          groups:
            claim: groups
            prefix: ""
        userValidationRules:
          - expression: "!user.username.startsWith('system:')"
            message: "username cannot use reserved system: prefix"
  caSecret:
    name: dex-ca-secret
    namespace: kcm-system
    key: ca.crt
```

This configuration authenticates users based on email addresses and propagates group claims for downstream authorization decisions.

### Key Fields

* **`spec.authenticationConfiguration`**

  Contains the full `AuthenticationConfiguration` object consumed by the Kubernetes API server. For all supported options, see the official Kubernetes documentation:
  [Authentication configuration from a file](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#using-authentication-configuration).

* **`spec.caSecret`**

  References a Kubernetes `Secret` containing one or more CA certificates used to trust the JWT issuer endpoint. The referenced `Secret` must exist before the `ClusterAuthentication` resource is applied.

  The CA certificate is injected into the generated `AuthenticationConfiguration` under `jwt.issuer[*].certificateAuthority`.

## Configuring Authentication for ClusterDeployments

This links a `ClusterDeployment` to an authentication policy. To enable authentication for a cluster, set the `spec.clusterAuth` field to the name of an existing `ClusterAuthentication` object in the same namespace.

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ClusterDeployment
metadata:
  name: cluster-name
  namespace: my-namespace
spec:
  template: openstack-hosted-cp-1-0-12
  credential: openstack-cluster-identity-cred
  clusterAuth: dex-cluster-auth
```

> NOTE:
> `ClusterAuthentication` objects can be distributed across namespaces using the `AccessManagement` resource.
> See [Access Management Resource](../access/accessmanagement.md) for details.

## Integration with ClusterTemplates

When authentication is enabled, {{{ docsVersionInfo.k0rdentName }}} injects the authentication configuration into the hosted control plane and manages updates when the configuration changes.

### What k0rdent Generates

When `spec.clusterAuth` is configured and the referenced `ClusterAuthentication` exists, the KCM controller performs the following actions:

1. Generates a `Secret` named `<cluster-deployment-name>-auth-config` containing the merged `AuthenticationConfiguration`, including injected CA certificates.
2. Passes authentication values to the `HelmRelease` responsible for deploying the cluster control plane:

```yaml
    auth:
      configSecret:
        name: cluster-name-auth-config
        key: config
        hash: 3f7b8627
```

* `auth.configSecret.name` – Name of the `Secret` containing the authentication configuration.
* `auth.configSecret.key` – Key within the `Secret` where the configuration is stored.
* `auth.configSecret.hash` – Hash of the configuration content; used to trigger control plane updates when the configuration changes.

### What ClusterTemplates Must Consume

The `ClusterTemplate` must consume these values to configure the API server correctly. Built-in templates already reference this information.

If you are creating custom `ClusterTemplates`, you must explicitly reference these values. In particular, the control plane resources (`K0smotronControlPlane` or `K0sControlPlane`) must:

1. Mount the authentication `Secret` into control plane nodes or pods.
2. Set the API server `--authentication-configuration` flag to the mounted configuration file.

> WARNING:
> Updating `spec.clusterAuth` changes the configuration hash and triggers a rolling recreation of control plane machines.

### Example: `K0smotronControlPlane` Authentication Configuration

This example shows how a hosted control plane consumes the injected authentication configuration.

```yaml
spec:
  k0sConfig:
    apiVersion: k0s.k0sproject.io/v1beta1
    kind: ClusterConfig
    metadata:
      name: k0s
    spec:
      mounts:
      {{- if .Values.auth.configSecret.name }}
      - path: /var/lib/k0s/auth
        secret:
          defaultMode: 420
          items:
            - key: {{ .Values.auth.configSecret.key }}
              path: config-{{ .Values.auth.configSecret.hash }}.yaml
          secretName: {{ .Values.auth.configSecret.name }}
      {{- end }}
      ...
      api:
        extraArgs:
          {{- if .Values.auth.configSecret.name }}
          authentication-config: /var/lib/k0s/auth/config-{{ .Values.auth.configSecret.hash }}.yaml
          {{- end }}
      ...
```

### Example: `K0sControlPlane` Authentication Configuration

This example shows the equivalent configuration for a non-hosted control plane.

```yaml
spec:
  k0sConfigSpec:
    {{- if .Values.auth.configSecret.name }}
    files:
    - contentFrom:
        secretRef:
          name: {{ .Values.auth.configSecret.name }}
          key: {{ default "config" .Values.auth.configSecret.key }}
      permissions: "0644"
      path: /var/lib/k0s/auth/config-{{ .Values.auth.configSecret.hash }}.yaml
    {{- end }}
    ...
    k0s:
      apiVersion: k0s.k0sproject.io/v1beta1
      kind: ClusterConfig
      metadata:
        name: k0s
      spec:
        api:
          extraArgs:
            {{- if .Values.auth.configSecret.name }}
            authentication-config: /var/lib/k0s/auth/config-{{ .Values.auth.configSecret.hash }}.yaml
            {{- end }}
      ...
```
