# Identity And Authorization Management

## ClusterAuthentication Resource

{{{ docsVersionInfo.k0rdentName }}} supports configuring identity and authorization management (IAM) for
child clusters through the `ClusterAuthentication` custom resource. A `ClusterAuthentication` object
defines how the Kubernetes API server authenticates incoming requests. It supports multiple JWT authenticators,
each configurable with an issuer URL, claim mappings, certificate authorities, and more.

The `ClusterAuthentication` object example:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ClusterAuthentication
metadata:
  name: dex-cluster-auth
  namespace: kcm-system
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

### Supported Fields

* `spec.authenticationConfiguration`

Contains the full `AuthenticationConfiguration` object used by the API server. For all available configuration
options, see the official Kubernetes documentation:
[Authentication configuration from a file](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#using-authentication-configuration).

* `spec.caSecret`

References a Kubernetes Secret that contains one or more CA certificates for the JWT issuer endpoint.
If the issuer uses a custom or self-signed CA, the certificate must be provided here so the API server can trust the issuer.
The CA value is injected into the `AuthenticationConfiguration` under `jwt.issuer[*].certificateAuthority`.

## Configuring Authentication for ClusterDeployments

To enable authentication for a `ClusterDeployment`, set the `spec.clusterAuth` field to the name of an existing
`ClusterAuthentication` object in the same namespace. For example:

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ClusterDeployment
metadata:
  name: cluster-name
  namespace: kcm-system
spec:
  template: openstack-hosted-cp-1-0-12
  credential: openstack-cluster-identity-cred
  clusterAuth: dex-cluster-auth
```

> NOTE:
> `ClusterAuthentication` objects can be distributed across namespaces using `AccessManagement` resource.
> See [Access Management Resource](../access/accessmanagement.md) for details.

## Integration with ClusterTemplates

When `spec.clusterAuth` is configured in the `ClusterDeployment` and the referenced `ClusterAuthentication` exists,
the {{{ docsVersionInfo.k0rdentName }}} KCM controller performs the following:

1. Generates a Secret named `<cluster-deployment-name>-auth-config` that contains the merged
`AuthenticationConfiguration` (including injected CA certificates).

2. Passes required authentication values to the HelmRelease responsible for deploying the cluster:

```yaml
    auth:
      configSecret:
        name: cluster-name-auth-config
        key: config
        hash: 3f7b8627
```

* `auth.configSecret.name` - Name of the Secret containing the authentication config.
* `auth.configSecret.key` - Key within the Secret where the configuration is stored.
* `auth.configSecret.hash` - Hash of the configuration content; used to trigger control plane updates when changed.

ClusterTemplate must consume these values to configure the API server correctly.
In particular, the control plane resources (`K0smotronControlPlane` or `K0sControlPlane`) must:

1. Mount the authentication Secret on control plane nodes/pods, and
2. Set the API server’s `--authentication-configuration` flag.

### Example: `K0smotronControlPlane` Authentication Configuration

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

> WARNING:
> If `spec.clusterAuth` is updated with a different configuration, the hash value will change.
> This triggers a rolling recreation of the control plane machines.
