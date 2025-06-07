# Creating the management cluster

The type of cluster you create for as a {{{ docsVersionInfo.k0rdentName }}} management cluster is going to depend on how you're going to use it. For example, a simple [single-node k0s install](./mgmt-create-k0s-single.md) is sufficient for testing and evaluation, but you will want a multi-node, etcd-backed cluster such as one created using [k0sctl](https://docs.k0sproject.io/stable/k0sctl-install/) or [EKS](./mgmt-create-eks-multi.md) for production.

> NOTE:
> For best results use Kubernetes version 1.32. or above.

In a production environment, you will always want to ensure that your management cluster is backed up. There are a few caveats and things you need to take into account when backing up {{{ docsVersionInfo.k0rdentName }}}. More info can be found in the guide at [use Velero as a backup provider](../../backup/index.md).

- [Create a single node k0s cluster](./mgmt-create-k0s-single.md)
- [Create a multi-node k0s cluster](./mgmt-create-k0s-multi.md)
- [Create a multinode EKS cluster](./mgmt-create-eks-multi.md)
  