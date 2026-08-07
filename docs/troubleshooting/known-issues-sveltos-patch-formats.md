# Sveltos-Managed Services Fail with PatchTransformer Errors

When an authenticated image registry and custom Projectsveltos patches are configured together, Sveltos-managed
services might fail with an error similar to the following:

```text
trouble configuring builtin PatchTransformer with config: `
patch: |-
  patch: |-
    - op: add
      path: /spec/template/spec/imagePullSecrets
`: unable to parse SM or JSON patch
```

This issue occurs when one of the following Projectsveltos patch ConfigMaps contains both legacy bare patches and
structured Sveltos `Patch` documents:

- `sveltos-agent-config`
- `drift-detection-config`

For example, custom values in the `Management` object might add a legacy strategic merge patch:

```yaml
data:
  scheduling-patch: |-
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: sveltos-agent-manager
```

At the same time, setting `controller.imagePullSecret` causes KCM to add a structured patch:

```yaml
data:
  image-patch: |-
    patch: |-
      - op: add
        path: /spec/template/spec/imagePullSecrets
        value:
        - name: registry-pull-secret
```

Projectsveltos first attempts to parse all entries in a ConfigMap as structured patches. If any entry is a legacy bare
patch, it falls back to interpreting all entries as legacy patches. The structured `image-patch` is then passed to
kustomize without removing its inner `patch` field, resulting in the duplicate `patch: |-` shown in the error.

## Verify the Issue

Inspect both ConfigMaps:

```bash
kubectl -n projectsveltos get configmap \
  sveltos-agent-config drift-detection-config -o yaml
```

The issue is present if the same ConfigMap contains a bare patch that starts with `apiVersion`, `{`, or `- op`, and a
structured patch that starts with `patch:`.

## Workaround

Use the structured Sveltos patch format for every custom entry in both ConfigMaps. The following minimal
`Management` fragment configures structured scheduling patches that can coexist with the KCM-generated image pull
secret patch:

```yaml
spec:
  providers:
  - name: projectsveltos
    config:
      projectsveltos:
        classifierManager:
          agentPatchConfigMap:
            data:
              scheduling-patch: |-
                patch: |-
                  apiVersion: apps/v1
                  kind: Deployment
                  metadata:
                    name: sveltos-agent-manager
                  spec:
                    template:
                      spec:
                        nodeSelector:
                          kubernetes.io/os: linux
                target:
                  group: apps
                  version: v1
                  kind: Deployment
                  name: sveltos-agent-manager
        addonController:
          driftDetectionManagerPatchConfigMap:
            data:
              scheduling-patch: |-
                patch: |-
                  apiVersion: apps/v1
                  kind: Deployment
                  metadata:
                    name: drift-detection-manager
                  spec:
                    template:
                      spec:
                        nodeSelector:
                          kubernetes.io/os: linux
                target:
                  group: apps
                  version: v1
                  kind: Deployment
                  name: drift-detection-manager
```

Apply the updated `Management` object, then verify that every entry in both ConfigMaps begins with `patch:`. Existing
custom patch bodies, including tolerations and probes, can remain unchanged inside the inner `patch: |-` block.
