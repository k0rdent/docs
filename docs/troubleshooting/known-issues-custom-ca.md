# Helm Extensions Cannot Be Pulled from Private Registry on Hosted ClusterDeployments

[Related issue: KCM #1612](https://github.com/k0rdent/kcm/issues/1612)

> NOTE:
> The issue is resolved in k0s versions `v1.32.6+k0s.0`, `v1.33.2+k0s.0`.

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

# KCM Installation Fails with Custom Registry Using Redirects: TLS Certificate Mismatch

> NOTE:
> This issue is automatically handled starting from K0rdent v1.3.0.

When installing KCM with a custom registry that uses a custom CA and supports redirects, installation may fail due to
a known Flux bug: [certSecretRef does not handle redirects](https://github.com/fluxcd/flux2/issues/5477).

The error typically looks like:

```bash
x509: certificate is valid for a, not b
```

**Workaround**

Until K0rdent v1.3.0 (or if you cannot upgrade), you can apply the following steps manually:

1. Mount the Registry CA Certificate into Flux Source Controller

Ensure the secret with your registry CA is present in the system namespace (`kcm-system` by default), as configured
by the `registryCertSecret` parameter. Then patch the `source-controller` Deployment:

```bash
kubectl patch deployment source-controller \
  -n kcm-system \
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

2. Remove `certSecretRef` from the HelmRepository

Patch the `kcm-templates` HelmRepository to remove the `certSecretRef` field:

```bash
kubectl patch helmrepository kcm-templates \
  -n kcm-system \
  --type=json \
  -p='[{"op": "remove", "path": "/spec/certSecretRef"}]'
```
