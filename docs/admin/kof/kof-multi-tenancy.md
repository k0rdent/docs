# Multi-tenancy in KOF

## Overview

KOF supports multi-tenancy to isolate data (metrics, logs, and traces) between tenants. In the current implementation, a tenant is an organization with child clusters.

## Architecture

Multi-tenancy is enforced by **VMAuth** using **VMUser** resources. Each cluster gets a separate VMUser automatically.
When a tenant ID label is specified, the VMUser is configured with:

- **ExtraLabels**: adds `tenantId=<TENANT_ID>` to all ingested metrics, logs, and traces
- **ExtraFilters**: restricts read access to data matching the specified `tenantId`

```mermaid
flowchart TB
 subgraph s1["Regional Cluster"]
        n1["VMAuth"]
        n5["VMUsers"]
        n6["VMInsert"]
  end
    n2["Child Cluster<br>(Tenant-A / cluster-1)"] -- Store Metrics --> n1
    n3["Child Cluster<br>(Tenant-B)"] -- Store Metrics --> n1
    n4["Child Cluster<br>(Tenant-A / cluster-2)"] -- Store Metrics --> n1
    n1 -- Authenticate and load VMUser config --> n5
    n5 -- Return tenantId / extra labels --> n1
    n1 -- Forward enriched data --> n6
```

This configuration ensures full isolation between tenants, allowing each to access only their own metrics, logs, and traces.

> NOTE:
> VMUser resources on regional clusters have administrative access without ExtraFilters restrictions, enabling cross-tenant data access.

## How to Enable Multi-tenancy

Add the tenant identification label to child `ClusterDeployment` resources:

```yaml
k0rdent.mirantis.com/kof-tenant-id: <TENANT_ID>
```

Dependent resources (secrets, VMUser object) will be updated or created automatically. See [storage credentials](https://github.com/k0rdent/kof/blob/main/docs/storage-creds.md) for details.

## Usage Examples

The next examples show how to test multi-tenancy using
local management cluster with [Grafana in KOF](kof-grafana.md)
integrated with local [Dex SSO](kof-grafana.md#single-sign-on)
exposed as `dex.example.com:32000` and configured to use Google OIDC provider.

Other dashboarding tools, [OIDC providers](https://dexidp.io/docs/connectors/oidc/),
and remote management cluster can be used instead.
Please adapt these reference examples to your own case.

## Single Sign-On

KOF uses [Dex SSO](kof-grafana.md#single-sign-on) to identify the tenant of the user:

```mermaid
sequenceDiagram
  actor User
  User ->> Grafana: Open
  Grafana ->> Dex: Sign in with Dex
  Dex ->> Google: Log in with Google
  Google ->> User: Are you user@example.com?
  User -->> Google: Yes
  Google -->> Dex: token with<br>hd:example.com
  Dex -->> Grafana: token with<br>tenant:example.com
```

## Access Control

Once the tenant is identified, KOF ACL service enforces the filtering of the data:

```mermaid
flowchart TB
  User((User)) --"Show metrics,<br>logs, alerts"--> Grafana
  Grafana --"Get the data<br>using token with<br>tenant:example.com"--> ACL[KOF ACL]
  ACL --"Get the data<br>having label<br>tenant:example.com"--> Proxies[Promxy, vlogxy]
  Proxies --> Cluster1 -.-> Proxies
  Proxies --> Cluster2[...] -.-> Proxies
  Proxies --> ClusterN -.-> Proxies
  Proxies -."aggregated data<br>from all clusters<br>filtered by the label".-> ACL
  ACL -."this data<br>post-filtered<br>by deep labels".-> Grafana
  Grafana -."dashboards<br>of this tenant".-> User
```

## Sign In Options

KOF provides multiple options to sign in to [Grafana](kof-grafana.md) for different levels of access.

### Full Access

Username and password from [grafana-admin-credentials](kof-grafana.md#install-and-enable-grafana)
grant full access to all tenants and features.

### SSO Admin

"Sign in with Dex" followed by "Log in with Email" grants access to all tenants and limited features.

To enable this option and Dex in general with [Usage Examples](#usage-examples) assumptions:

1. ??? note "Get admin email and password hash:"

        ```bash
        ADMIN_EMAIL=$(git config user.email)
        ADMIN_PASSWORD_HASH=$(htpasswd -BnC 10 admin | cut -d: -f2)
        ```

2. ??? note "Create the patch:"

        ```bash
        cat <<EOF
        kof-mothership:
          values:
            kcm:
              kof:
                acl:
                  enabled: true
                  developmentMode: true  # For local test only: self-signed Dex TLS
                  replicaCount: 1
                  extraArgs:
                    issuer: https://dex.example.com:32000
                    admin-email: "$ADMIN_EMAIL"
            dex:
              enabled: true
              config:
                issuer: https://dex.example.com:32000
                enablePasswordDB: true
                staticPasswords:
                  - email: "$ADMIN_EMAIL"
                    hash: "$ADMIN_PASSWORD_HASH"
                    username: "admin"
                    userID: "1"
                oauth2:
                  passwordConnector: local
                staticClients:
                  - id: grafana-id
                    redirectURIs:
                      - "http://localhost:3000/login/generic_oauth"
                    name: Grafana
                    secret: grafana-secret
                connectors: []
        EOF
        ```

3. Add this patch to the existing `kof-values.yaml` file
    and then apply `kof-values.yaml` to the [Management Cluster](kof-install.md/#management-cluster):

{%
    include-markdown "../../../includes/kof-install-includes.md"
    start="<!--install-kof-start-->"
    end="<!--install-kof-end-->"
%}

4. ??? note "Expose Dex at local management cluster as `https://dex.example.com:32000`"

        ```bash
        grep -qxF "127.0.0.1 dex.example.com" /etc/hosts \
          || echo "127.0.0.1 dex.example.com" | sudo tee -a /etc/hosts

        node_internal_ip=$(kubectl get node k0rdent-control-plane \
          -o jsonpath='{.status.addresses[?(@.type=="InternalIP")].address}'
        )

        kubectl get ns kof || kubectl create ns kof
        git clone git@github.com:k0rdent/kof.git
        cd ./kof
        bash scripts/generate-dex-secret.bash
        bash scripts/patch-coredns.bash kubectl dex.example.com $node_internal_ip

        kubectl rollout restart deploy/coredns -n kube-system
        kubectl rollout status deploy/coredns -n kube-system --timeout=1m

        kubectl rollout restart deploy/kof-mothership-dex -n kof
        kubectl rollout status deploy/kof-mothership-dex -n kof --timeout=1m

        kubectl port-forward svc/kof-mothership-dex 32000:5554 -n kof
        ```

5. Apply the [Install and enable Grafana](kof-grafana.md#install-and-enable-grafana).

6. ??? note "Integrate Grafana with Dex:"

        ```bash
        cat >grafana-dex.yaml <<EOF
        spec:
          config:
            auth.generic_oauth:
              enabled: "true"
              name: Dex
              scopes: "openid email profile groups offline_access"
              auth_url: https://dex.example.com:32000/auth
              token_url: https://dex.example.com:32000/token
              api_url: https://dex.example.com:32000/userinfo
              client_id: grafana-id
              client_secret: grafana-secret
              tls_skip_verify_insecure: "true"
        EOF

        kubectl patch -n kof grafana grafana-vm --type merge \
          --patch-file=grafana-dex.yaml
        ```

### SSO User

"Sign in with Dex" followed by "Log in with Google" grants access to a single tenant and limited features.

To enable this option:

1. ??? note "Create Google OIDC credentials for `https://dex.example.com:32000`:"

        * Open the [Google Cloud Console](https://console.cloud.google.com/).
        * Create a project, e.g. `dex`
        * Configure OAuth screen:
            * Audience: Internal (initially, while you're testing it)
        * Create OAuth client:
            * App type: Web app
            * Authorized JavaScript origins: `https://dex.example.com:32000`
            * Authorized redirect URIs: `https://dex.example.com:32000/callback`
            * Create, download JSON with creds, copy `client_id` and `client_secret`.

2. Apply the [SSO Admin](#sso-admin) steps
    with the next part added to `kof-values.yaml`,
    replacing `<GOOGLE_CLIENT_ID>` and `<GOOGLE_CLIENT_SECRET>`:

    ??? note "Google OIDC connectors:"

        ```yaml
        kof-mothership:
          values:
            dex:
              config:
                connectors:
                  - type: oidc
                    id: google
                    name: Google
                    config:
                      issuer: https://accounts.google.com
                      clientID: "<GOOGLE_CLIENT_ID>"
                      clientSecret: "<GOOGLE_CLIENT_SECRET>"
                      redirectURI: https://dex.example.com:32000/callback
                      insecureEnableGroups: true
                      claimModifications:
                        newGroupFromClaims:
                          - prefix: tenant
                            delimiter: ":"
                            clearDelimiter: false
                            claims:
                              - hd
                      scopes:
                        - openid
                        - email
                        - profile
        ```

KOF ACL uses either `tenant` claim or `tenant:...` group in the `groups` claim.

??? note "Details"
    * If your OIDC provider creates ID token with `tenant` claim,
        KOF ACL uses it to identify the tenant.
    * Google ID token doesn't have `tenant` claim,
        but it has the [`hd` claim](https://developers.google.com/identity/openid-connect/openid-connect#id_token-hd)
        (Hosted Domain associated with the Google Workspace or Cloud organization of the user)
        with a value like `example.com`.
    * Dex supports [claimMapping](https://dexidp.io/docs/connectors/oidc/#configuration)
        of a non-standard claim like `hd` to a standard one,
        but the `tenant` is not one of the [standard claims](https://openid.net/specs/openid-connect-core-1_0.html#Claims).
    * So the [claimModifications](https://dexidp.io/docs/connectors/oidc/#configuration)
        in the Dex configuration above add a new group like `tenant:example.com` to the `groups` claim.
    * KOF ACL finds the `tenant:...` group in the `groups` claim to identify the tenant.

??? note "If you see the `Missing saved oauth state` error:"

    Just retry "Sign in with Dex" followed by "Log in with Google", it should work.
