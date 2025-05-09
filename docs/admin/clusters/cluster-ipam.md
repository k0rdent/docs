# IP Address Management (IPAM)

{{{ docsVersionInfo.k0rdentName }}} provides a flexible IP Address Management (IPAM) system that enables deterministic allocation of IP addresses throughout the cluster lifecycle.

With IPAM enabled, IP addresses can be assigned to critical components such as:

- Control plane nodes
- Worker nodes
- Cluster-internal networks (e.g., pod/service networks)
- External-facing resources (e.g., load balancers, ingress)

Administrators can define address ranges using either CIDR blocks or explicit IP lists, allowing for:

- Predictable, conflict-free assignments
- Seamless integration with existing network topologies
- Fine-grained control in multi-tenant or segmented environments

---

# Deploying a Cluster with IPAM

Follow these steps to configure IPAM in your cluster deployment.

## 1. Prerequisites

Ensure the following before configuring IPAM:

- A valid, unused IP space is available (CIDR or static IP list).
- The reserved space must accommodate:
  - One IP per control plane node
  - One IP per worker node

## 2. Define a `ClusterIPAMClaim`

Use the `ClusterIPAMClaim` resource to reserve IP address space required for the cluster. Each network segment—node, cluster, and external—can be defined using either a `cidr` or a static list of `ipaddresses`.

```yaml
apiVersion: k0rdent.mirantis.com/v1alpha1
kind: ClusterIPAMClaim
metadata:
  name: <claim-name>
  namespace: <namespace>
spec:
  provider: <provider-name>
  nodeNetwork:
    cidr: <cidr>
    # ipaddresses:
    # - <ip-1>
    # - <ip-2>
  clusterNetwork:
    cidr: <cidr>
  externalNetwork:
    cidr: <cidr>
  clusterDeploymentRef: <cluster-name>
```

> 💡 The `clusterDeploymentRef` field links this claim to a specific `ClusterDeployment`, ensuring IPs are reserved before the cluster is provisioned.

### Apply the `ClusterIPAMClaim`

To submit the claim, run:

```bash
kubectl apply -f <cluster-ipam-claim-file>.yaml
```

You can confirm the claim was created with:

```bash
kubectl get clusteripamclaim <claim-name> -n <namespace>
```

## 3. (Alternative) Inline IPAM in `ClusterDeployment`

Alternatively, define IPAM directly in the `ClusterDeployment` resource:

```yaml
apiVersion: k0rdent.mirantis.com/v1alpha1
kind: ClusterDeployment
metadata:
  name: <cluster-name>
  namespace: <kcm-system-namespace>
spec:
  template: <template-name>
  credential: <provider-credential-name>
  dryRun: <"true" | "false">  # Optional; defaults to "false"
  config:
    <cluster-configuration>
  ipam:
    provider: <provider-name>
    nodeNetwork:
      cidr: <cidr>
      # ipaddresses:
      # - <ip-1>
      # - <ip-2>
    clusterNetwork:
      cidr: <cidr>
    externalNetwork:
      cidr: <cidr>
```

## 4. Deploy the Cluster

To deploy the cluster with IPAM configured:

```bash
kubectl apply -f <cluster-deployment-file>.yaml
```

The specified IPAM settings will be used to allocate IP addresses during provisioning.

---