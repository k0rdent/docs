# Create and prepare a Kubernetes cluster with k0s

Follow these steps to install and prepare a [k0s kubernetes](https://k0sproject.io) management cluster:

1. Deploy a Kubernetes cluster

    The first step is to create the actual cluster itself. Again, the actual distribution used for the management cluster isn't important, as long as it's a CNCF-compliant distribution. That means you can use an existing EKS cluster, or whatever is your normal corporate standard. 

    To make things simple this guide uses [k0s](https://github.com/k0sproject/k0s/), a small, convenient, and fully-functional distribution. For more granular instructions, including those for creating a cluster accessible from a different server, see the [k0s multi-node instructions](mgmt-create-k0s-multi.md):

    ```shell
    curl --proto '=https' --tlsv1.2 -sSf https://get.k0s.sh | sudo sh
    sudo k0s install controller --enable-worker --no-taints
    sudo k0s start
    ```

    k0s includes its own preconfigured version of `kubectl` so make sure the cluster is running:

    ```shell
    sudo k0s kubectl get nodes
    ```

    After 2-3 minutes you should see a single `control-plane` node with a status of `Ready`, as in:

    ```shell
    NAME              STATUS   ROLES            AGE   VERSION
    ip-172-31-29-61   Ready    control-plane    46s   v1.31.2+k0s
    ```

2. Install kubectl

    Everything you do in {{{ docsVersionInfo.k0rdentName }}} is done by creating and manipulating Kubernetes objects, so you'll need to have `kubectl` installed. You can find the [full install docs here](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/), or just follow these instructions:

    ```shell
    sudo apt-get update
    sudo apt-get install -y apt-transport-https ca-certificates curl gnupg
    curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.31/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
    sudo chmod 644 /etc/apt/keyrings/kubernetes-apt-keyring.gpg # allow unprivileged APT programs to read this keyring
    echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.31/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
    sudo chmod 644 /etc/apt/sources.list.d/kubernetes.list   # helps tools such as command-not-found to work correctly
    sudo apt-get update
    sudo apt-get install -y kubectl
    ```

3. Get the kubeconfig

    In order to access the management cluster you will, of course, need the kubeconfig. Again, if you're using another Kubernetes distribution follow those instructions to get the kubeconfig, but for k0s, the process involves simply copying the existing file and adding it to an environment variable so `kubectl` knows where to find it.

    ```shell
    sudo cp /var/lib/k0s/pki/admin.conf KUBECONFIG
    sudo chmod +r KUBECONFIG
    export KUBECONFIG=./KUBECONFIG
    ```

    Now you should be able to use the non-k0s `kubectl` to see the status of the cluster:

    ```shell
    kubectl get nodes
    ```

    Again, you should see the single k0s node, but by this time it should have had its role assigned, as in:

    ```console
    NAME              STATUS   ROLES           AGE   VERSION
    ip-172-31-29-61   Ready    control-plane   25m   v1.31.2+k0s
    ```

    Now the cluster is ready for installation, which we'll do using Helm.

4. Install Helm

    The easiest way to install {{{ docsVersionInfo.k0rdentName }}} is through its Helm chart, so let's get Helm installed. You can find the [full instructions here](https://helm.sh/docs/intro/install/), or use these instructions:

    ```shell
    curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
    chmod 700 get_helm.sh
    ./get_helm.sh
    ```

    Helm will be installed into `/usr/local/bin/helm`.

## Access your cluster from another machine

To use a tool like Lens or to access the cluster from another machine, copy the `KUBECONFIG`, which is located at:

```console
/var/lib/k0s/pki/admin.conf
```

to your target machine.  Note that to access the cluster from an external machine you must replace `localhost` in the `KUBECONFIG` with the host IP address or hostname for your controller. Make sure to use the address you added to the `sans` field, and also that port `6443` is accessible.