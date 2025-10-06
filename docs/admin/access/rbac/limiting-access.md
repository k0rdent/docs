# Limiting Access

While you could certainly run {{{ docsVersionInfo.k0rdentName }}} with all of your people
having access to everything and putting all of their `ClusterDeployment` objects, and so on
in the `kcm-system` namespace, you've probably already realized that this is not a good idea.
It's a bit like having everyone use `root` to do all of their daily business.  It's asking for
trouble.

Fortunately, {{{ docsVersionInfo.k0rdentName }}} makes it possible to avoid this situation. 
In general, there are two situations of concern:

* Limiting access to system credentials
* Limiting access to the `kcm-system` namespace

Both are straightforward, and the principles apply to any restrictions you may wish to apply.

## Limiting credential access

In order for {{{ docsVersionInfo.k0rdentName }}} to manage infrastructure, you must provide it
with access keys, passwords, and so on. In order to avoid making these credentials (little "c")
available to all your developers, you can store them as `Secret` objects in the management cluster.

However, you still need to hide those `Secret` objects from the developer to keep those credentials
safe.  Fortunately, the developer never needs to use a `Secret` directly; it's embedded in a `Credential`,
along with the cluster identity. So to keep credentials safe, you need to limit the developer's access
to `kcm-system` namespace objects to just `Credential` objects.

The `kcm-credentials-viewer-role` `ClusterRole` provides read-only access to `Credential` objects, 
and nothing else:

```bash
kubectl describe clusterrole kcm-credentials-viewer-role
```
```console { .no-copy }
Name:         kcm-credentials-viewer-role
Labels:       app.kubernetes.io/managed-by=Helm
              helm.toolkit.fluxcd.io/name=kcm
              helm.toolkit.fluxcd.io/namespace=kcm-system
              k0rdent.mirantis.com/aggregate-to-namespace-editor=true
              k0rdent.mirantis.com/aggregate-to-namespace-viewer=true
Annotations:  meta.helm.sh/release-name: kcm
              meta.helm.sh/release-namespace: kcm-system
PolicyRule:
  Resources                         Non-Resource URLs  Resource Names  Verbs
  ---------                         -----------------  --------------  -----
  credentials.k0rdent.mirantis.com  []                 []              [get list watch]
```

So to assign these limited privileges to a developer, create the 
following `RoleBinding`, which defines what they can do in the referenced namespace
(in this case, `kcm-system`).

```bash
kubectl apply -f - <<EOF
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: credential-viewer
  namespace: kcm-system
subjects:
  - kind: User
    name: user
    apiGroup: rbac.authorization.k8s.io
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: kcm-credentials-viewer-role
EOF
```

You can use the same principle to control where developers can actually put their
applications and `ClusterDeployment` objects.


## Keep users out of the `kcm-system` namespace

The `kcm-system` namespace should be reserved for core components that come with {{{ docsVersionInfo.k0rdentName }}}
That means users should not create resources (such as `Secret`, `ClusterDeployment`, or `ServiceTemplate` objects) 
in this namespace.

Instead, create a namespace for your user(s):

```bash
kubectl create namespace user-cluster-ns
```

You can then give them the ability to create clusters in that namespace using the `kcm-namespace-editor-role`
`ClusterRole`:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: user-cluster-ns-editor
  namespace: user-cluster-ns
subjects:
  - kind: User
    name: user
    apiGroup: rbac.authorization.k8s.io
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: kcm-namespace-editor-role
```

This `ClusterRole` enables the user to create clusters but limits their ability to add 
new `ServiceTemplate` objects:

```bash
kubectl describe clusterrole kcm-namespace-editor-role -n kcm-system
```
```console { .no-copy }
Name:         kcm-namespace-editor-role
Labels:       app.kubernetes.io/managed-by=Helm
              helm.toolkit.fluxcd.io/name=kcm
              helm.toolkit.fluxcd.io/namespace=kcm-system
Annotations:  meta.helm.sh/release-name: kcm
              meta.helm.sh/release-namespace: kcm-system
PolicyRule:
  Resources                                      Non-Resource URLs  Resource Names  Verbs
  ---------                                      -----------------  --------------  -----
  clusterdeployments.k0rdent.mirantis.com        []                 []              [create delete get list patch update watch]
  clusteripamclaims.k0rdent.mirantis.com/status  []                 []              [create delete get list patch update watch]
  clusteripamclaims.k0rdent.mirantis.com         []                 []              [create delete get list patch update watch]
  secrets                                        []                 []              [get list watch]
  helmcharts.helm.toolkit.fluxcd.io              []                 []              [get list watch]
  helmrepositories.helm.toolkit.fluxcd.io        []                 []              [get list watch]
  clustertemplatechains.k0rdent.mirantis.com     []                 []              [get list watch]
  clustertemplates.k0rdent.mirantis.com          []                 []              [get list watch]
  credentials.k0rdent.mirantis.com               []                 []              [get list watch]
  servicetemplatechains.k0rdent.mirantis.com     []                 []              [get list watch]
  servicetemplates.k0rdent.mirantis.com          []                 []              [get list watch]
```

Creating `ServiceTemplate` objects enables new workloads on created clusters, so this
is something that you will want to keep track of, either enabling creation on a case-by-case
basis or keeping that as something to be handled by admins in the `kcm-system` namespace.

For more information on the `ClusterRoles` available in {{{ docsVersionInfo.k0rdentName }}}
see the [roles summary](roles-summary.md).