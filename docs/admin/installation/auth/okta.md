# Kubernetes OIDC Authentication Setup Guide for Okta

This section explains how to configure {{{ docsVersionInfo.k0rdentName}}} to use Okta as an OIDC provider for authentication. While the examples use k0s for demonstration purposes, the concepts and procedures are fully applicable to any Kubernetes environment that meets the minimum requirements for k0rdent.

## Prerequisites

Before you begin, ensure that your environment meets the following prerequisites.

### 1. Required Software

Make sure your development machine has the following installed:

- **[Docker](https://docs.docker.com/):** Container runtime to build and run containerized applications.
- **{{{ docsVersionInfo.k0rdentName}}} Management Cluster:** Although k0s is used in this guide, you may use any [{{{ docsVersionInfo.k0rdentName}}} management cluster](../create-mgmt-clusters/index.md) (for example, [Minikube](https://minikube.sigs.k8s.io/docs/start/), [MicroK8s](https://microk8s.io/), or a cloud-based cluster) that supports deploying k0rdent.
- **[Helm](https://helm.sh/):** A package manager for Kubernetes to install and manage applications. 
- **[Coreutils](https://www.gnu.org/software/coreutils/):** Standard UNIX utilities for various file operations. 
- **[jq](https://stedolan.github.io/jq/):** A lightweight and flexible command-line JSON processor. 
- **[jwt]( https://github.com/mike-engel/jwt-cli.):** A CLI tool to decode and inspect JSON Web Tokens.

### 2. Okta Setup

Prepare your Okta environment by completing the following steps:

- **Create an Okta Developer Account:**  
  Visit the [Okta Developer Signup](https://developer.okta.com/signup/) page and create an account if you don’t already have one.
  
- **Review Okta Configuration Guides:**  
  Familiarize yourself with the Okta user interface and setup procedures using guides such as the [UI Guide](https://developer.okta.com/blog/2021/10/08/secure-access-to-aws-eks#configure-your-okta-org). Although this guide focuses on Kubernetes, these resources provide valuable context on configuring your Okta organization, applications, and OIDC settings.

- **Obtain Okta Credentials:**  
  After setting up your Okta account and application, note the following:
  - Your **Okta Domain** (for example, `https://your-okta-domain.okta.com`)
  - The **Authorization Server** URL (typically something like `https://your-okta-domain.okta.com/oauth2/default`)
  - The **Client ID** and **Client Secret** generated when you register your Kubernetes application in Okta
  - Any additional scopes or API keys as required by your integration

## Installation Steps

Follow these steps to deloy Okta.

### 1. Install Krew (Kubectl Plugin Manager)

Krew is a package manager for kubectl plugins. Installing it ensures you can manage the OIDC login plugin easily.

You can install Krew by running the following command in your terminal. This script detects your OS and architecture, downloads the latest Krew release, extracts it, and installs it:

```bash
(
  set -x; cd "$(mktemp -d)" &&
  OS="$(uname | tr '[:upper:]' '[:lower:]')" &&
  ARCH="$(uname -m | sed -e 's/x86_64/amd64/' -e 's/\(arm\)\(64\)\?.*/\1\2/' -e 's/aarch64$/arm64/')" &&
  KREW="krew-${OS}_${ARCH}" &&
  curl -fsSLO "https://github.com/kubernetes-sigs/krew/releases/latest/download/${KREW}.tar.gz" &&
  tar zxvf "${KREW}.tar.gz" &&
  ./"${KREW}" install krew
)
```
Add `krew` to your path:
```bash
export PATH="${KREW_ROOT:-$HOME/.krew}/bin:$PATH"
```

For additional details, troubleshooting tips, and instructions for Windows installations, see the official [Krew Installation Guide](https://krew.sigs.k8s.io/docs/user-guide/setup/install/).

### 2. Install the OIDC Login Plugin

The OIDC login plugin for kubectl simplifies the process of obtaining and refreshing tokens from your Okta instance.

```bash
kubectl krew update
kubectl krew install oidc-login
```

### 3. Create the Structured Authentication Configuration

This configuration file tells your Kubernetes API server how to validate JWT tokens issued by Okta. Create a file on the controller called `authentication-config.yaml` with the following content:

```yaml
apiVersion: apiserver.config.k8s.io/v1beta1
kind: AuthenticationConfiguration
jwt:
  - issuer:
      url: "<YOUR_OKTA_DOMAIN>"
      audiences:
        - <YOUR_OKTA_CLIENT_ID>
    claimMappings:
      username:
        claim: email
        prefix: ""
      groups:
        claim: groups
        prefix: ""
    claimValidationRules:
      - expression: "has(claims.email)"
        message: "email claim must be present"
      - expression: "claims.email != ''"
        message: "email claim must be non-empty"
      - expression: "has(claims.groups)"
        message: "groups claim must be present"
      - expression: "type(claims.groups) == list ? size(claims.groups) > 0 : true"
        message: "groups list must be non-empty"
      - expression: "type(claims.groups) == string ? claims.groups.size() > 0 : true"
        message: "groups string must be non-empty"        
    userValidationRules:
      - expression: "!user.username.startsWith('system:')"
        message: "username cannot use reserved system: prefix"
      - expression: "user.groups.all(group, !group.startsWith('system:'))"
        message: "groups cannot use reserved system: prefix"
```

> NOTE:
> Remember to replace placeholder values with the actual values from your Okta configuration.

### 4. Configure Your Kubernetes Cluster

Edit your k0s config (`/etc/k0s/config.yaml`) to tell the API server to load your auth config and enable the feature gate:

```yaml
spec:
  api:
    extraArgs:
      # enable the StructuredAuthenticationConfiguration feature
      - --feature-gates=StructuredAuthenticationConfiguration=true
      # point to your auth config file
      - --authentication-config=/etc/k0s/authentication-config.yaml
    extraVolumes:
      - name: auth-config
        hostPath: /etc/k0s/authentication-config.yaml
        mountPath: /etc/k0s/authentication-config.yaml
        readOnly: true
        pathType: File
```

Then:

```bash
# ensure your auth file is in place
sudo mkdir -p /etc/k0s
sudo cp authentication-config.yaml /etc/k0s/authentication-config.yaml
sudo chmod 600 /etc/k0s/authentication-config.yaml

# restart k0s so the API server picks up the new flags
sudo systemctl restart k0scontroller
```

For other Kubernetes distributions, the concept remains the same—you need to configure your API server to load the `authentication-config.yaml` file. Check your cluster’s documentation for mounting configuration files and setting extra API server arguments.

## RBAC Configuration

For {{{ docsVersionInfo.k0rdentName }}} to work properly with OIDC-authenticated users, configure RBAC policies. Below is a sample RoleBinding configuration that grants permissions to a specific group.

Create a file named `rolebinding.yaml`:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: kcm-ns-viewer
  namespace: kcm-system
subjects:
  - kind: Group
    name: kcm-ns-viewer # Must match the Okta group claim
    apiGroup: rbac.authorization.k8s.io
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: kcm-namespace-viewer-role
```

Apply this configuration using:

```bash
kubectl apply -f rolebinding.yaml
```

## Token Management

### Obtaining an Okta OIDC Token

Use the `kubectl oidc-login` plugin to retrieve a token from your Okta instance. The token is used for authenticating with your Kubernetes API server.

```bash
export K8S_TOKEN=$(kubectl oidc-login get-token \
  --oidc-issuer-url=<YOUR_OKTA_DOMAIN> \
  --oidc-client-id=<YOUR_OKTA_CLIENT_ID> \
  --listen-address=127.0.0.1:8000 \
  --skip-open-browser=true \
  --oidc-extra-scope=email \
  --force-refresh | jq -r '.status.token' \
) && echo $K8S_TOKEN | jwt decode -
```

> **Tip:** Replace the placeholder values with your actual Okta configuration details. The command pipes the token to `jwt decode` so you can inspect its contents.

### Debug Token Validation

Validate the token by performing a simple API call that includes a higher verbosity level for debugging:

```bash
kubectl --token=$K8S_TOKEN get secrets -n kcm-system -v=9
```

---

## Configuring the Kubernetes CLI

After obtaining your token, update your kubectl configuration to use these OIDC credentials.

### 1. Set User Credentials

```bash
kubectl config set-credentials user --token=$K8S_TOKEN
```

### 2. Create a New Context

In your `~/.kube/config`, add:

```yaml
users:
...
- name: okta-user
  user:
    exec:
      apiVersion: client.authentication.k8s.io/v1beta1
      command: kubectl
      args:
        - oidc-login
        - get-token
        - --oidc-issuer-url=<YOUR_OKTA_DOMAIN>
        - --oidc-client-id=<YOUR_OKTA_CLIENT_ID>
        - --oidc-client-secret=<YOUR_OKTA_CLIENT_SECRET>
        - --oidc-extra-scope=email
        - --oidc-extra-scope=groups
```

Also add a new context referencing that user, as in:

```yaml
contexts:
...
- name: okta@k0s        
  context:
    cluster: k0s
    user: okta-user
```

### 3. Verify Access

Confirm that your OIDC credentials provide the necessary access:

```bash
kubectl --context=okta@k0s auth can-i get namespaces
kubectl --context=okta@k0s auth can-i get secrets -n kcm-system
kubectl --context=okta@k0s auth can-i get pods -n kcm-system
```

### 4. Switch Contexts

Switch to the OIDC context when needed:

```bash
kubectl config use-context okta@k0s
```

To revert to your default context, use the standard context name:

```bash
kubectl config use-context Default
```

### 5. View Kubeconfig Details

Inspect your current kubeconfig to confirm the setup:

```bash
kubectl config view --context=okta@k0s 
```

### 6. [DEBUG] Inspect API Server Logs

For further troubleshooting, review the API server logs:

```bash
journalctl -u k0scontroller -f
```

By following these instructions, you will have a fully functional OIDC authentication system integrated with your Kubernetes cluster, regardless of whether you’re using k0s or another deployment environment.