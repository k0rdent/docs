# Remote machine parameters

## ClusterDeployment Parameters

To deploy a cluster using {{{ docsVersionInfo.k0rdentName}}} on any SSH accessible Linux host, configure the following parameters:

### Cluster parameters

* `controlPlaneNumber` (number): Specifies how many control plane pods you want to deploy. For example, 3 means three control plane pods will be set up.
* `clusterLabels` (map[string]string): A dictionary of labels that can be applied to the cluster for better management and filtering. Example: `{"environment": "production"}`.
* `clusterAnnotations` (map[string]string): A dictionary for annotations, which are often used for non-identifying information. Example: `{"team": "devops"}`.
* `clusterNetwork.pods.cidrBlocks` (array of strings): The IP address range allocated for Pods in the cluster. Example: `["10.244.0.0/16"]`.
* `clusterNetwork.services.cidrBlocks` (array of strings): The IP address range allocated for Services. Example: `["10.96.0.0/12"]`.

### Machines Parameters

* `machines[].address` (string): Address is the IP address or DNS name of the remote machine. Examples: `"10.130.0.237"`, `"2001:0db8:85a3:0000:0000:8a2e:0370:7334"`, `"some-hostname"`.
* `machines[].port` (number): The SSH port of the remote machine. Default is 22. Example: `22`.
* `machines[].user` (string): The user name for SSH login. Default is root. Example: `"root"`.
* `machines[].useSudo` (boolean): Whether or not to use sudo for running commands on the remote machine. Example: `false`.
* `machines[].provisionJob.scpCommand` (string): The command to use for copying files to remote machines. Example: `"scp"`.
* `machines[].provisionJob.sshCommand` (string): The command to use for connecting to remote machines. Example: `"ssh"`.
* `machines[].provisionJob.jobSpecTemplate.metadata`: Kubernetes metadata for the provisioning job, such as labels or annotations. See: <https://docs.k0smotron.io/stable/resource-reference/#remotemachinespecprovisionjobjobspectemplatemetadata> for more information.
* `machines[].provisionJob.jobSpecTemplate.spec`: Specification for the provisioning job, detailing the job’s behavior and configuration. See: <https://docs.k0smotron.io/stable/resource-reference/#remotemachinespecprovisionjobjobspectemplatespec> for more information.
* `machines[].k0s.args` (array of strings): A list of extra arguments for configuring the k0s worker node. See: <https://docs.k0sproject.io/stable/cli/k0s_worker>.

### K0smotron Parameters

* `k0smotron.controllerPlaneFlags` (array of strings): The `controllerPlaneFlags` parameter enables you to configure additional flags for the k0s control plane and to override existing flags. The default flags are kept unless they are explicitly overriden. Flags with arguments must be specified as a single string, such as `--some-flag=argument`.
* `k0smotron.persistence.type` (string): This parameter defines the persistence type for the control plane’s state. Example: `"EmptyDir"`. See <https://docs.k0smotron.io/stable/configuration/#persistence> for more information.
* `k0smotron.service.type` (string): This parameter defines the type of service for the Kubernetes API server: `"ClusterIP"`, `"NodePort"`, or `"LoadBalancer"`.
* `k0smotron.service.apiPort` (number): This parameter defines the port for accessing the Kubernetes API server. Example: `30443`.
* `k0smotron.service.konnectivityPort` (number): This parameter indicates the port for the Konnectivity service. Example: `30132`.

### K0s Parameters

* `k0s.version` (string): Specifies the version of the k0s Kubernetes distribution. Example: `"v1.32.2+k0s.0"`.
* `k0s.arch` (string): Defines K0s Arch in its download URL. Available if [global.k0sURL](../../appendix/appendix-extend-mgmt.md#configuring-a-global-k0s-url)
   is set. Possible values: `"amd64"` (default), `"arm64"`, `"arm"`.
* `k0s.api.extraArgs`: Additional arguments to pass to the Kubernetes API server. Example: `{"--some-arg": "value"}`.
* `k0s.network`: Network settings for the k0s cluster. Example: `{"dns": "8.8.8.8"}`.
* `k0s.extensions.helm.repositories` (array of objects): Helm repositories to add during the cluster setup. Example: `[{ "name": "repo1", "url": "https://charts.repo1.com" }]`.
* `k0s.extensions.helm.charts` (array of objects): Helm charts to be installed during bootstrap. Example: `[{ "name": "chart1", "namespace": "kube-system", "chartname": "repo1/chart1" }]`.

### Example ClusterDeployment

```yaml
apiVersion: k0rdent.mirantis.com/v1beta1
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
