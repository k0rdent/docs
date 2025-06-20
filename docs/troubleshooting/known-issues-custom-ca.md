# Helm Extensions Cannot Be Pulled from Private Registry on Hosted ClusterDeployments

[Related issue: KCM #1612](https://github.com/k0rdent/kcm/issues/1612)

When deploying Hosted ClusterDeployments on a management cluster configured with a custom container registry, and
the registry uses a certificate signed by an unknown certificate authority, Helm extensions (e.g., CCM or CSI
drivers) may fail to install.

You may encounter an error similar to the following in the logs of the hosted cluster controller pods:

```shell
can''t locate chart `oci://172.19.125.101:5001/charts/vsphere-csi-driver-0.0.3`:
failed to do request: Head "https://172.19.125.101:5001/v2/charts/vsphere-csi-driver/manifests/0.0.3":
tls: failed to verify certificate: x509: certificate signed by unknown authority
```

As a result, the Helm extension fails to install.

The controller cannot verify the registry’s TLS certificate because the required custom CA certificate is not
trusted by the k0s environment.

Support for supplying custom CA certificates for Helm extensions from OCI registries is being added in
[Allow providing CA certificate for helm extensions that use OCI registries](https://github.com/k0sproject/k0s/issues/5877).
When using a k0s version that includes this fix, the workaround is no longer required.

**Workaround**

You can work around this issue by manually mounting the registry CA certificate into the hosted cluster controller’s
StatefulSet. The secret with the registry CA should already be present in your system namespace (as you configured
`registryCertSecret` parameter):

1. Patch the StatefulSet for the hosted cluster controller:
* Add a volume from the Secret
* Mount it inside the container at a known location (e.g., `/etc/ssl/certs/registry-ca.pem`)

```bash
kubectl patch statefulset kmc-<CLUSTER_DEPLOYMENT_NAME> \
  -n <CLUSTER_DEPLOYMENT_NAMESPACE> \
  --type='json' \
  -p='[
    {
      "op": "add",
      "path": "/spec/template/spec/volumes/-",
      "value": {
        "name": "registry-ca",
        "secret": {
          "secretName": "<REGISTRY_SECRET_NAME>",
          "items": [
            {
              "key": "ca.crt",
              "path": "registry-ca.pem"
            }
          ]
        }
      }
    },
    {
      "op": "add",
      "path": "/spec/template/spec/containers/0/volumeMounts/-",
      "value": {
        "name": "registry-ca",
        "mountPath": "/etc/ssl/certs/registry-ca.pem",
        "subPath": "registry-ca.pem",
        "readOnly": true
      }
    }
  ]'
```
