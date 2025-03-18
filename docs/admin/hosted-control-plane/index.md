# Deploying a Hosted Control Plane

A hosted control plane is a Kubernetes setup in which the control plane components (such as the API server, 
etcd, and controllers) run inside the management cluster instead of separate controller nodes. This 
architecture centralizes control plane management and improves scalability by sharing resources in the management cluster.
Hosted control planes are managed by [k0smotron](https://k0smotron.io/).

Instructions for setting up a hosted control plane vary slighting depending on the provider.