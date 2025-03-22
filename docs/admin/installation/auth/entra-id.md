# Microsoft Entra ID

This section explains how to configure {{{ docsVersionInfo.k0rdentName }}} to use Microsoft Entra ID as an OIDC provider for authentication. While the examples use KinD (Kubernetes in Docker) for demonstration purposes, the concepts and procedures are fully applicable to any {{{ docsVersionInfo.k0rdentName }}} management cluster (for example, [Minikube](https://minikube.sigs.k8s.io/docs/start/), [MicroK8s](https://microk8s.io/), or a cloud-based cluster) that meets the minimum requirements for k0rdent.

## Prerequisites

Before you begin, ensure that your environment meets the following prerequisites.

### 1. Required Software

Make sure your development machine has the following installed:

- **[Docker](https://docs.docker.com/):** Container runtime to build and run containerized applications.
- **{{{ docsVersionInfo.k0rdentName }}} Management Cluster:** Although KinD is used in this guide, you may use any {{{ docsVersionInfo.k0rdentName }}} management cluster that supports deploying k0rdent.
- **[Helm](https://helm.sh/):** A package manager for Kubernetes to install and manage applications.
- **[Coreutils](https://www.gnu.org/software/coreutils/):** Standard UNIX utilities for various file operations.
- **[jq](https://stedolan.github.io/jq/):** A lightweight and flexible command-line JSON processor.
- **[jwt](https://github.com/mike-engel/jwt-cli):** A CLI tool to decode and inspect JSON Web Tokens.

### 2. Microsoft Entra ID Setup

Prepare your Microsoft Entra ID environment by completing the following steps:

- **Register an OIDC-Enabled Application:**  
  In the Microsoft Entra ID (formerly Azure AD) portal, register an application with OIDC enabled. Ensure that you configure the appropriate redirect URIs (for example, `http://localhost:8000`).

- **Assign Users to an Entra ID Group:**  
  Ensure that the users who will authenticate are assigned to an Entra ID group that you will use for Kubernetes RBAC.

- **Configure Claims:**  
  Verify that the OIDC application returns the necessary claims—**preferred_username** (or **email**/**upn** if preferred), **groups**, and **profile**.  
  > **Note:** Some Entra ID configurations might not return the `email` claim. In such cases, the `preferred_username` claim is used as the username.

- **Obtain Entra ID Credentials:**  
  After registering your application, note the following:
  - Your **Tenant ID**.
  - The **Authorization Server** URL (for example, `https://login.microsoftonline.com/<tenant-id>/v2.0`).
  - The **Client ID** and, if applicable, the **Client Secret** generated for your Kubernetes application.

---

## Installation Steps

Follow these steps to deploy Microsoft Entra ID as your OIDC provider.

### 1. Install Krew (Kubectl Plugin Manager)

Krew is a package manager for kubectl plugins. Installing it ensures you can manage the OIDC login plugin easily.

You can install Krew by running the following command in your terminal. This script detects your OS and architecture, downloads the latest Krew release, extracts it, and installs it:

```bash
(
  set -x; cd "$(mktemp -d)" &&
  OS="$(uname | tr '[:upper:]' '[:lower:]')" &&
  ARCH="$(uname -m | sed -e 's/x86_64/amd64/' -e 's/arm.*$/arm/')" &&
  KREW="krew-${OS}_${ARCH}" &&
  curl -fsSLO "https://github.com/kubernetes-sigs/krew/releases/latest/download/${KREW}.tar.gz" &&
  tar zxvf "${KREW}.tar.gz" &&
  ./"${KREW}" install krew
)
```

For additional details, troubleshooting tips, and instructions for Windows installations, see the official [Krew Installation Guide](https://krew.sigs.k8s.io/docs/user-guide/setup/install/).

### 2. Install the OIDC Login Plugin

The OIDC login plugin for kubectl simplifies the process of obtaining and refreshing tokens from your Entra ID instance.

```bash
kubectl krew update
kubectl krew install oidc-login
```

### 3. Create the Structured Authentication Configuration

This configuration file tells your Kubernetes API server how to validate JWT tokens issued by Entra ID. Create a file named `authentication-config.yaml` with the following content:

```yaml
apiVersion: apiserver.config.k8s.io/v1beta1
kind: AuthenticationConfiguration
jwt:
  - issuer:
      url: "https://login.microsoftonline.com/<tenant-id>/v2.0"
      audiences:
        - "<client-id>"
    claimMappings:
      username:
        claim: preferred_username  # Use 'email' or 'upn' if preferred and available
        prefix: ""
      groups:
        claim: groups
        prefix: ""
    claimValidationRules:
      - expression: "has(claims.preferred_username)"
        message: "preferred_username claim must be present"
      - expression: "claims.preferred_username != ''"
        message: "preferred_username claim must be non-empty"
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

> **Note:** Replace `<tenant-id>` and `<client-id>` with the actual values from your Microsoft Entra ID application registration. Adjust the claim mappings if your token uses different claim names (for example, `email` or `upn`).

### 4. Configure Your Kubernetes Cluster

Below is an example KinD cluster configuration that mounts the authentication configuration file. Adapt these instructions if you are using another Kubernetes system.

#### Create the KinD Cluster Configuration

Create a file named `kind-config.yaml`:

```yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
featureGates:
  "StructuredAuthenticationConfiguration": true
nodes:
  - role: control-plane
    kubeadmConfigPatches:
      - |
        kind: ClusterConfiguration
        apiServer:
          extraArgs:
            authentication-config: /etc/kubernetes/authentication-config.yaml
          extraVolumes:
            - name: authentication-config
              hostPath: /etc/kubernetes/authentication-config.yaml
              mountPath: /etc/kubernetes/authentication-config.yaml
              readOnly: true
              pathType: File
    extraMounts:
      - hostPath: ./authentication-config.yaml
        containerPath: /etc/kubernetes/authentication-config.yaml
        readOnly: true
```

For other Kubernetes distributions, the concept remains the same—you need to configure your API server to load the `authentication-config.yaml` file. Consult your cluster’s documentation for mounting configuration files and setting extra API server arguments.

### 5. Cluster Management with KinD (Example)

If you are using KinD, execute the following commands. Otherwise, adjust these steps to match your Kubernetes provider’s procedures.

#### Create the KinD Cluster

```bash
kind create cluster --verbosity 99 --config kind-config.yaml --retain
```

#### Retrieve API Server Pod Information

To inspect the API server configuration, use:

```bash
kubectl describe pod -n kube-system kube-apiserver-$(kubectl get nodes -o jsonpath='{.items[0].metadata.name}')
```

#### Debugging the Control Plane

For troubleshooting, you can view logs and container status:

```bash
docker exec kind-control-plane ls /var/log/containers/
docker exec kind-control-plane crictl ps
```

---

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
    name: "<group-id-from-token>"
    apiGroup: rbac.authorization.k8s.io
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: kcm-namespace-viewer-role
```

> **Note:** Replace `<group-id-from-token>` with the group identifier returned in the Entra ID token that should have access to the `kcm-system` namespace.

Apply this configuration using:

```bash
kubectl apply -f rolebinding.yaml
```

---

## Token Management

### Obtaining a Microsoft Entra ID OIDC Token

Use the `kubectl oidc-login` plugin to retrieve a token from your Entra ID instance. The token is used for authenticating with your Kubernetes API server.

```bash
export K8S_TOKEN=$(kubectl oidc-login get-token \
  --oidc-issuer-url=https://login.microsoftonline.com/<tenant-id>/v2.0 \
  --oidc-client-id=<client-id> \
  --oidc-client-secret=<client-secret> \
  --oidc-redirect-url-hostname=localhost \
  --listen-address=localhost:8000 \
  --skip-open-browser=true \
  --oidc-extra-scope="email profile openid" \
  --force-refresh | jq -r '.status.token' \
) && echo $K8S_TOKEN | jwt decode -
```

> **Tip:** Replace `<tenant-id>`, `<client-id>`, and `<client-secret>` with the actual values from your Entra ID application registration. The `--oidc-redirect-url-hostname` should match the redirect URI configured in Entra ID.

### Debug Token Validation

Validate the token by performing a simple API call that includes a higher verbosity level for debugging:

```bash
kubectl --token=$K8S_TOKEN get secrets -n kcm-system -v=9
```

---

## Configuring Kubernetes CLI

After obtaining your token, update your kubectl configuration to use these OIDC credentials.

### 1. Set User Credentials

```bash
kubectl config set-credentials user --token=$K8S_TOKEN
```

### 2. Create a New Context

Set up a context that references your cluster and the new user credentials. For KinD, you might use:

```bash
kubectl config set-context user --cluster="kind-$(kind get clusters | head -1)" --user=user --namespace=kcm-system
```

For other Kubernetes clusters, replace the cluster name appropriately.

### 3. Verify Access

Confirm that your OIDC credentials provide the necessary access:

```bash
kubectl --context=user auth can-i get namespaces
kubectl --context=user auth can-i get secrets -n kcm-system
kubectl --context=user auth can-i get pods -n kcm-system
```

### 4. Switch Contexts

Switch to the OIDC context when needed:

```bash
kubectl config use-context user
```

To revert to your default context, use the standard context name (for example, the KinD default):

```bash
kubectl config use-context "kind-$(kind get clusters | head -1)"
```

### 5. View Kubeconfig Details

Inspect your current kubeconfig to confirm the setup:

```bash
kubectl config view --context=user
```

### 6. [DEBUG] Inspect API Server Logs

For further troubleshooting, review the API server logs:

```bash
kubectl --context="kind-$(kind get clusters | head -1)" logs -n kube-system kube-apiserver-kind-control-plane | grep authentication.go
```
