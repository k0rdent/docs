
# IP Address Management (IPAM)

`{{{ docsVersionInfo.k0rdentName }}}` provides a flexible IP Address Management (IPAM) system that enables deterministic allocation of IP addresses throughout the cluster lifecycle.
> ⚠️ At the moment **only node network supported**
With IPAM enabled, IP addresses can be assigned to both worker and control plane nodes.

Administrators can define address ranges using either CIDR blocks or explicit IP lists, enabling:

- Predictable, conflict-free assignments
- Seamless integration with existing network topologies
- Fine-grained control in multi-tenant or segmented environments

---

# Deploying a Cluster with IPAM

Follow these steps to configure IPAM for your cluster deployment.

## 1. Prerequisites

Ensure the following before configuring IPAM:

- A valid, unused IP space is available (CIDR or static IP list).
- The reserved space must accommodate:
  - One IP per control plane node
  - One IP per worker node

## 2. Define IPAM configuration

### Option 1: Use mutual references in `ClusterDeployment` and `ClusterIPAMClaim`

#### Define a `ClusterIPAMClaim`

The `ClusterIPAMClaim` resource reserves the required IP address space for the cluster. Node network segment can be defined using either a `cidr` or a static list of `ipAddresses`.

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ClusterIPAMClaim
metadata:
  name: <claim-name>
  namespace: <namespace>
spec:
  provider: <provider-name>
  nodeNetwork:
    cidr: <cidr>
    # ipAddresses:
    # - <ip-1>
    # - <ip-2>
  cluster: <cluster-name>
```

> ⚠️ The `cluster` field in `ClusterIPAMClaim` is immutable once set.
> 
> 💡 The `cluster` field links the claim to a specific `ClusterDeployment`, ensuring IPs are reserved before provisioning begins.

#### Apply the `ClusterIPAMClaim`

To create the claim:

```bash
kubectl apply -f <cluster-ipam-claim-file>.yaml
```

To verify the claim:

```bash
kubectl get clusteripamclaim <claim-name> -n <namespace>
```

### Example Output
``` yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ClusterIPAMClaim
metadata:
  name: <claim-name>
  namespace: <namespace>
spec:
  cluster: <cluster-name>
  clusterIPAMRef: <claim-name>
  nodeNetwork:
    cidr: <cidr>
    # ipAddresses:
    # - <ip-1>
    # - <ip-2>
  provider: <provider-name>
status:
  bound: true
```

- ```.spec.clusterIPAMRef```: Indicates that the child ClusterIPAM object was successfully created, if this field is set.

- ```.status.bound```: If true, it means the child ClusterIPAM was successfully reconciled and the defined addresses were allocated.

#### Define a `ClusterDeployment`

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ClusterDeployment
metadata:
  name: <cluster-name>
  namespace: <namespace>
spec:
  template: <template-name>
  credential: <provider-credential-name>
  dryRun: <"true" | "false">  # Optional; defaults to "false"
  config:
    <cluster-configuration>
  ipamClaim:
    ref: <claim-name>
```

### Option 2: Use inline IPAM configuration in `ClusterDeployment`

IPAM configuration can be defined inline within the `ClusterDeployment` resource:

#### Define a `ClusterDeployment`

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ClusterDeployment
metadata:
  name: <cluster-name>
  namespace: <namespace>
spec:
  template: <template-name>
  credential: <provider-credential-name>
  dryRun: <"true" | "false">  # Optional; defaults to "false"
  config:
    <cluster-configuration>
  ipamClaim:
    spec:
      provider: <provider-name>
      nodeNetwork:
        cidr: <cidr>
        # ipAddresses:
        # - <ip-1>
        # - <ip-2>
```

#### Apply the `ClusterDeployment`:

```bash
kubectl apply -f <cluster-deployment-file>.yaml
```

## 4. Verify IPAM
The specified IPAM settings will be used to allocate IP addresses during provisioning. Keep in mind, that cluster provisioning will not proceed until IPAM resources ready and addresses allocated.

To inspect the resulting `ClusterIPAM` resource:

```bash
kubectl get -n <namespace> ClusterIPAM <claim-name>
```

### Example Output

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
kind: ClusterIPAM
metadata:
  name: <cluster-ipam-name>
  namespace: <namespace>
spec:
  provider: <provider-name>
  clusterIPAMClaimRefs: <cluster-ipam-claim-name>
status:
  phase: Bound
  providerData:
    <provider data>
```

---