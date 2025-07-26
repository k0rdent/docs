# Create and prepare a production-grade Kubernetes cluster with EKS

Follow these steps to install and prepare an [Amazon EKS](https://ca-central-1.console.aws.amazon.com/eks/clusters) management cluster:

1. The basic AWS tools

     Start by installing and configuring the Amazon tools. First download and install the `aws` tool:

     ```shell
     curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
     unzip awscliv2.zip
     sudo ./aws/install
     ```
     Then configure it using environment variables:

     ```shell
     export AWS_ACCESS_KEY_ID="EXAMPLE_ACCESS_KEY_ID"
     export AWS_SECRET_ACCESS_KEY="EXAMPLE_SECRET_ACCESS_KEY"
     export AWS_SESSION_TOKEN="EXAMPLE_SESSION_TOKEN"
     aws configure
     ```
     ```console
     AWS Access Key ID [EXAMPLE_ACCESS_KEY_ID]:
     AWS Secret Access Key [EXAMPLE_SECRET_ACCESS_KEY]:
     Default region name [YOUR_AWS_REGION]:
     Default output format [json]:
     ```
     Once `aws` is installed you can install `eksctl`:

     ```shell
     curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_Linux_amd64.tar.gz" | tar xz -C /tmp
     sudo mv /tmp/eksctl /usr/local/bin
     eksctl version
     ```
     ```console
     0.211.0
     ```

1. Create the cluster

    You can use the eksctl tool to create the basic Kubernetes cluster:
    ```shell
    eksctl create cluster --name <CLUSTER_NAME> \
    --version 1.31 \
    --region <YOUR_AWS_REGION> \
    --without-nodegroup
    ```
    ```console
    2025-03-05 22:26:02 [ℹ]  eksctl version 0.211.0
    ...
    2025-03-05 22:36:14 [✔]  all EKS cluster resources for "CLUSTER_NAME" have been created
    2025-03-05 22:36:15 [ℹ]  kubectl command should work with "/home/username/.kube/config", try 'kubectl get nodes'
    2025-03-05 22:36:15 [✔]  EKS cluster "CLUSTER_NAME" in "YOUR_AWS_REGION" region is ready
    ```

1. Add controllers

    While the cluster is now created, it doesn't actually have any nodes.  Start by adding controllers:
    ```shell
    eksctl create nodegroup --cluster <CLUSTER_NAME> \
    --name <CONTROLLER_NODE_GROUP> \
    --node-type t3.medium \
    --nodes 3 \
    --nodes-min 3 \
    --nodes-max 3 \
    --node-labels "role=control-plane" 
    ```
    ```console
    2025-03-05 22:57:15 [ℹ]  will use version 1.31 for new nodegroup(s) based on control plane version
    2025-03-05 22:57:18 [ℹ]  nodegroup "nickchasek0rdentcontroller-group" will use "" [AmazonLinux2/1.31]
    2025-03-05 22:57:19 [ℹ]  1 nodegroup (nickchasek0rdentcontroller-group) was included (based on the include/exclude rules)
    2025-03-05 22:57:19 [ℹ]  will create a CloudFormation stack for each of 1 managed nodegroups in cluster "NickChasek0rdentControlCluster"
    ...
    2025-03-05 23:00:27 [ℹ]  all nodegroups have up-to-date cloudformation templates
    ```

1. Install kubectl

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

1. Get the KUBECONFIG

    You don't have to access the KUBECONFIG directly; you can use the aws tool to get access to it:

    ```shell
    aws eks update-kubeconfig --region <YOUR_AWS_REGION> --name <CLUSTER_NAME>
    ```
    ```shell
    Updated context arn:aws:eks:ca-central-1:026090528175:cluster/NickChasek0rdentControlCluster in /home/nick/.kube/config
    ```

1. Taint controllers

    To prevent workloads from being scheduled on the controllers, add the `node-role.kubernetes.io/control-plane=true:NoSchedule` taint. First list
    the started nodes:

    ```shell
    kubectl get nodes
    ```
    ```console
    NAME                                              STATUS   ROLES    AGE    VERSION
    nodename1.compute.internal   Ready    <none>   4h1m   v1.31.7-eks-5d632ec
    nodename2.compute.internal   Ready    <none>   4h1m   v1.31.7-eks-5d632ec
    nodename3.compute.internal   Ready    <none>   4h1m   v1.31.7-eks-5d632ec
    ```
    For each node, go ahead and set the taint:

    ```shell
    kubectl taint nodes nodename1.compute.internal node-role.kubernetes.io/control-plane=true:NoSchedule
    ```
    ```console
    node/nodename1.ca-central-1.compute.internal tainted
    ```
    Now verify the taints:
    ```shell
    kubectl describe nodes | grep -A 5 "Taints:"
    ```
    ```console
    Taints:             node-role.kubernetes.io/control-plane=true:NoSchedule
    Unschedulable:      false
    Lease:
    HolderIdentity:  nodename1.compute.internal
    AcquireTime:     <unset>
    RenewTime:       Fri, 25 Jul 2025 21:16:56 -0500
    --
    Taints:             node-role.kubernetes.io/control-plane=true:NoSchedule
    Unschedulable:      false
    Lease:
    HolderIdentity:  nodename2.compute.internal
    AcquireTime:     <unset>
    RenewTime:       Fri, 25 Jul 2025 21:16:56 -0500
    --
    Taints:             node-role.kubernetes.io/control-plane=true:NoSchedule
    Unschedulable:      false
    Lease:
    HolderIdentity:  nodename3.ca-central-1.compute.internal
    AcquireTime:     <unset>
    RenewTime:       Fri, 25 Jul 2025 21:16:56 -0500
    ```

1. Add worker nodes

    Adding worker nodes is simpler than controllers:

    ```shell
    eksctl create nodegroup --cluster <CLUSTER_NAME> \
    --name <WORKER_NODE_GROUP> \
    --node-type t3.medium \
    --nodes 3 \
    --nodes-min 3 \
    --nodes-max 5 \
    --node-labels "role=worker"
    ```
    ```console
    2025-03-06 03:10:48 [ℹ]  will use version 1.31 for new nodegroup(s) based on control plane version
    ...
    2025-03-06 03:13:38 [✔]  created 1 managed nodegroup(s) in cluster "CLUSTER_NAME"
    2025-03-06 03:13:39 [ℹ]  checking security group configuration for all nodegroups
    2025-03-06 03:13:39 [ℹ]  all nodegroups have up-to-date cloudformation templates
    ```
    Verify the nodes:
    ```shell
    kubectl get nodes
    ```
    ```console
    NAME                                              STATUS   ROLES    AGE     VERSION
    nodename1.compute.internal   Ready    <none>   4h14m   v1.31.7-eks-5d632ec
    nodename4.compute.internal   Ready    <none>   79s     v1.31.7-eks-5d632ec
    nodename2.compute.internal   Ready    <none>   4h14m   v1.31.7-eks-5d632ec
    nodename5.compute.internal   Ready    <none>   82s     v1.31.7-eks-5d632ec
    nodename3.compute.internal   Ready    <none>   4h14m   v1.31.7-eks-5d632ec
    nodename6.compute.internal   Ready    <none>   4h14m   v1.31.7-eks-5d632ec
    ```

1. Verify pods

    Make sure pods will run properly by deploying a test pod:
    ```shell
    kubectl run test-pod --image=nginx --restart=Never
    kubectl get pods -o wide
    ```
    ```shell
    NAME       READY   STATUS    RESTARTS   AGE   IP               NODE                                              NOMINATED NODE   READINESS GATES
    test-pod   1/1     Running   0          15s   192.168.76.104   ip-192-168-68-189.ca-central-1.compute.internal   <none>           <none>
    ```
    Clean up so you can start fresh:
    ```shell
    kubectl delete pod test-pod
    ```
    ```shell
    pod "test-pod" deleted
    ```
    ```shell
    kubectl get pods -o wide
    ```
    ```console
    No resources found in default namespace.
    ```

1. Install Helm

    Finally, the easiest way to install {{{ docsVersionInfo.k0rdentName }}} is through its Helm chart, so let's get Helm installed. You can find the [full instructions here](https://helm.sh/docs/intro/install/), or use these instructions:

    ```shell
    curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
    chmod 700 get_helm.sh
    ./get_helm.sh
    ```

    Helm will be installed into `/usr/local/bin/helm`.