# Deploying a Hosted Control Plane

Under normal circumstances, {{{ docsVersionInfo.k0rdentName }}} deploys a child cluster as a complete, self-contained unit.
That is, the controllers and workers are all part of the `ClusterDeployment`. There are serious advantages to deploying
a cluster this way, not the least of which is the fact that the cluster is essentially independent of the Management cluster,
in that if the Management cluster becomes inaccessible for any reason the child cluster can continue on as though nothing
has happened. This is known as a "standalone" deployment.

On the other hand, for many Kubernetes clusters, the controllers are either too busy -- that is, they are constantly
being scaled up and down -- or they're not busy enough -- that is, they're taking up server resources that aren't being
fully used.

For either of these cases, a better choice may be a "hosted control plane". 

A hosted control plane is a Kubernetes setup in which the control plane components (such as the API server, 
etcd, and controllers) run as pods inside the management cluster instead of separate controller nodes. This 
architecture centralizes control plane management and improves scalability by sharing resources in the management cluster.
Need more controllers? Spin up another pod. Need fewer controllers? Remove some pods.

It's important to remember that if a child cluster's control plane goes down, workloads will continue on
indefinitely, but you won't be able to manage the cluster. So be sure to [back up your management cluster](../backup/index.md) after
deploying important child clusters!

Hosted control planes are managed by [k0smotron](https://k0smotron.io/), which makes it possible for Kubernetes
controller nodes and worker nodes to reside not only in different clusters, but even in different clouds.

Instructions for setting up a hosted control plane vary slighting depending on the provider.

- [AWS](hcp-aws.md)
- [Azure](hcp-azure.md)
- [OpenStack](hcp-openstack.md)
- [VMware](hcp-vmware.md)
- [GCP](hcp-gcp.md)
