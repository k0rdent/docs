# Remote machine parameters

## ClusterDeployment Parameters

To deploy a cluster using k0rdent on any SSH accessible Linux host, the following parameters can be configured:

### Cluster parameters

* `controlPlaneNumber` (number): Specifies how many control plane pods you want to deploy. For example, 3 means three control plane pods will be set up.
* `clusterLabels` (map[string]string): A dictionary of labels that can be applied to the cluster for better management and filtering. Example: `{"environment": "production"}`.
* `clusterAnnotations` (map[string]string): A dictionary for annotations, which are often used for non-identifying information. Example: `{"team": "devops"}`.
* `clusterNetwork.pods.cidrBlocks` (array of strings): The IP address range allocated for Pods in the cluster. Example: `["10.244.0.0/16"]`.
* `clusterNetwork.services.cidrBlocks` (array of strings): The IP address range allocated for Services. Example: `["10.96.0.0/12"]`.

### Machines Parameters
* `machines[].address` (string): The IP address of the remote machine. Example: `"10.130.0.237"`.
* `machines[].port` (number): The SSH port of the remote machine. Default is 22. Example: `22`.
* `machines[].user` (string): The user name for SSH login. Default is root. Example: `"root"`.
* `machines[].useSudo` (boolean): Whether or not to use sudo for running commands on the remote machine. Example: `false`.
* `machines[].provisionJob.scpCommand` (string): The command to use for copying files to remote machines. Example: `"scp"`.
* `machines[].provisionJob.sshCommand` (string): The command to use for connecting to remote machines. Example: `"ssh"`.
* `machines[].provisionJob.jobSpecTemplate.metadata`: Kubernetes metadata for the provisioning job, e.g., labels or annotations. See: https://docs.k0smotron.io/stable/resource-reference/#remotemachinespecprovisionjobjobspectemplatemetadata.
* `machines[].provisionJob.jobSpecTemplate.spec`: Specification for the provisioning job, detailing the job’s behavior and configuration. See: https://docs.k0smotron.io/stable/resource-reference/#remotemachinespecprovisionjobjobspectemplatespec.
* `machines[].k0s.args` (array of strings): A list of extra arguments for configuring the k0s worker node. Example: `["--extra-arg"]`.

### K0smotron Parameters

* `k0smotron.controllerPlaneFlags` (array of strings): ControllerPlaneFlags allows to configure additional flags for k0s control plane and to override existing ones. The default flags are kept unless they are overriden explicitly. Flags with arguments must be specified as a single string, e.g. `--some-flag=argument`.
* `k0smotron.persistence.type` (string): Defines the persistence type for the control plane’s state. Example: `"EmptyDir"`. See https://docs.k0smotron.io/stable/configuration/#persistence.
* `k0smotron.service.type` (string): Defines the type of service for the Kubernetes API server: `"ClusterIP"`, `"NodePort"`, or `"LoadBalancer"`.
* `k0smotron.service.apiPort` (number): The port for accessing the Kubernetes API server. Example: `30443`.
* `k0smotron.service.konnectivityPort` (number): The port for the Konnectivity service. Example: `30132`.

### K0s Parameters
* `k0s.version` (string): Specifies the version of the k0s Kubernetes distribution. Example: `"v1.32.2+k0s.0"`.
* `k0s.api.extraArgs`: Additional arguments to pass to the Kubernetes API server. Example: `{"--some-arg": "value"}`.
* `k0s.network`: Network settings for the k0s cluster. Example: `{"dns": "8.8.8.8"}`. 
* `k0s.extensions.helm.repositories` (array of objects): Helm repositories to add during the cluster setup. Example: `[{ "name": "repo1", "url": "https://charts.repo1.com" }]`.
* `k0s.extensions.helm.charts` (array of objects): Helm charts to be installed during bootstrap. Example: `[{ "name": "chart1", "namespace": "kube-system", "chartname": "repo1/chart1" }]`.


### Example ClusterDeployment

```yaml
apiVersion: k0rdent.mirantis.com/v1alpha1
kind: ClusterDeployment
metadata:
  name: my-remote-cluster-deployment
  namespace: kcm-system
spec:
  template: remote-cluster-{{{ extra.docsVersionInfo.providerVersions.dashVersions.remoteCluster }}}
  credential: remote-cred
  propagateCredentials: false
  config:
    controlPlaneNumber: 1
    clusterLabels:
      k0rdent: demo
    clusterAnnotations:
      k0rdent: demo
    k0smotron:
      service:
        type: LoadBalancer
    machines:
      - address: 10.130.0.237
        user: root
        port: 22
        k0s:
          args:
            - --debug
      - address: 10.130.0.174
        user: root
        port: 22
    k0s:
      version: v1.31.5+k0s.0
      extension:
        helm:
          repositories:
            - name: custom-repo
              url: https://custom-repo-url
          charts:
            - name: custom-chart
              namespace: kube-system
              chartname: custom-repo/custom-chart
              version: "0.0.8"
              values: |
                customKey: customValue
```
