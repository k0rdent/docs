# Create and prepare a multinode Kubernetes cluster with k0s

Many features of {{{ docsVersionInfo.k0rdentName }}} require a Kubernetes cluster that uses etcd for its persistence layer. While this is the case for many implementations, the single-node k0s cluster uses SQLite instead. Fortunately, multi-node k0s uses etcd by default, so you can solve this problem by creating controller and worker nodes and linking them together. 

Follow these steps to install and prepare a multinode [k0s kubernetes](https://k0sproject.io) management cluster:

## Create the first controller

1. Download k0s:

    Run the k0s download script to download the latest stable version of k0s and make it executable from `/usr/bin/k0s`:

    ```shell
    curl --proto '=https' --tlsv1.2 -sSf https://get.k0s.sh | sudo sh
    ```

2. Create a configuration file:

    > NOTE:
    > Depending on your configuration, you may need to execute these commands as root rather than using `sudo`. If so, executing `sudo su` will be sufficient. Don't forget to exit the root user afterwards!

    ```shell
    mkdir -p /etc/k0s
    k0s config create > /etc/k0s/k0s.yaml
    ```

3. If you need to access the cluster from outside the specific node on which you're installing it, add the public hostname as the `spec.api.externalAddress` and as an instance under `spec.api.sans`, as in:

    ```yaml
    ...
    spec:
        api:
            address: 172.31.7.199
            externalAddress: myhost.example.com
            ca:
            certificatesExpireAfter: 8760h0m0s
            expiresAfter: 87600h0m0s
            k0sApiPort: 9443
            port: 6443
            sans:
            - 172.31.7.199
            - fe80::c4:e6ff:fecc:9739
            - myhost.example.com
        controllerManager: {}
        extensions:
            helm:
    ...
    ```

    You can also make other configuration changes. For more information see the [k0s documentation](https://docs.k0sproject.io/stable/configuration/).

4. Install the controller:

    ```shell
    sudo k0s install controller -c /etc/k0s/k0s.yaml
    sudo k0s start
    ```

    The k0s process acts as a "supervisor" for all of the control plane components. In moments the control plane will be up and running, but because of the k0s architecture, you won't see any nodes running, because only worker nodes show up, and we haven't created any yet. You can, however, use the k0s-installed `kubectl` to make sure the cluster is up and running by looking for existing namespaces:

    ```shell
    sudo k0s kubectl get namespaces
    ```
    ```console
    NAME              STATUS   AGE
    default           Active   5m15s
    k0s-autopilot     Active   5m11s
    kube-node-lease   Active   5m15s
    kube-public       Active   5m15s
    kube-system       Active   5m15s
    ```

## Add workers to the cluster

Once the contoller is up, you can add a worker node by creating a "join token" and using it to start k0s on a new server. Follow these instructions:

1. Create a join token:

    To join additional nodes to the cluster, you need a join token, which is a base64-encoded `KUBECONFIG`. The token embeds information that enables mutual trust between the worker and controller(s) and allows the node to join the cluster.

    To get a worker token, run the following command on newly created existing controller node:

    ```shell
    sudo k0s token create --role=worker > token-file
    ```

    The resulting output is a long token string, which we'll use in a moment to add a worker to the cluster.

    For enhanced security, set an expiration time for the token:

    ```shell
    sudo k0s token create --role=worker --expiry=100h > token-file
    ```

2. Create the new node:

    Start by instantiating the new node and downloading k0s, as before:

    ```shell
    curl --proto '=https' --tlsv1.2 -sSf https://get.k0s.sh | sudo sh
    ```

3. Copy the token file you created in step 1 to the new server.

4. Start the new worker: 

    Now you can start the new worker, feeding it the token file so that it automatically joins the existing cluster:

    > NOTE:
    > Don't forget to use the actual path to your token file.

    ```shell
    sudo k0s install worker --token-file /path/to/token/file/token-file
    sudo k0s start
    ```

5. Check the node status:

    Now you can check the status of the node by going **to the controller** and once again checking for nodes. After a minute or two, you'll see the new node in a `Ready` state:

    ```shell
    sudo k0s kubectl get nodes
    ```
    ```console
    NAME              STATUS     ROLES    AGE     VERSION
    ip-172-31-9-107   Ready      <none>   3m39s   v1.33.1+k0s
    ```

## Add controllers to the cluster

To create a join token for the new controller, follow these steps.


1. Copy the `k0s.yaml` file to the new controller server at `/etc/k0s/k0s.yaml`. Each controller in the cluster must have this `k0s.yaml` file, or some cluster nodes will use default config values, which will lead to inconsistent behavior. 

    If your configuration file includes IP addresses (node address, sans, etcd peerAddress), remember to update them accordingly for this specific controller node.

2. Run the following command on an existing controller:

    ```shell
    sudo k0s token create --role=controller --expiry=1h > controller-token-file
    ```

    Copy the `controller-token-file` file to the new controller server.

4. As before, download and install k0s in the new controller:

    ```shell
    curl --proto '=https' --tlsv1.2 -sSf https://get.k0s.sh | sudo sh
    ```

3. On the new controller, run:

    ```shell
    sudo k0s install controller --token-file /path/to/token/file -c /etc/k0s/k0s.yaml
    sudo k0s start
    ```

4. This time, check k0s status by running this command on the new controller:

    ```shell
    sudo k0s status
    ```
    ```console
    Version: v1.33.1+k0s.1
    Process ID: 1489
    Role: controller
    Workloads: false
    SingleNode: false
    ```

## Access your cluster

Use the Kubernetes 'kubectl' command-line tool that comes with k0s binary to deploy your application or check your node status:

```shell
sudo k0s kubectl get nodes
```
```console
NAME   STATUS   ROLES    AGE    VERSION
k0s    Ready    <none>   4m6s   v1.33.1+k0s
```

You can also install `kubectl` directly. You can find the [full install docs here](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/), or just follow these instructions:

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

To use `kubectl` directly or to access the cluster from another machine, copy the `KUBECONFIG`, which is located on the controllers at:

```console
/var/lib/k0s/pki/admin.conf
```

to your target machine.  Note that to access the cluster from an external machine you must replace `localhost` in the `KUBECONFIG` with the host IP address or hostname for your controller. Make sure to use the address you added to the `sans` field, and also that port `6443` is accessible.