# What roles do
{{{ docsVersionInfo.k0rdentName }}} leverages the Kubernetes RBAC system and provides a set of standard `ClusterRole` objects with
associated permissions. These standard `ClusterRole` objects are created as part of the {{{ docsVersionInfo.k0rdentName }}} helm chart.
{{{ docsVersionInfo.k0rdentName }}} roles are based on labels and aggregated permissions, meaning they automatically collect
rules from other `ClusterRole` objects with specific labels.

The following table outlines the roles available in {{{ docsVersionInfo.k0rdentName }}}, along with their respective read/write or read-only
permissions:

| Roles                            | Global Admin | Global Viewer | Namespace Admin | Namespace Editor | Namespace Viewer |
|----------------------------------|--------------|---------------|-----------------|------------------|------------------|
| **Scope**                        | **Global**   | **Global**    | **Namespace**   | **Namespace**    | **Namespace**    |
| {{{ docsVersionInfo.k0rdentName }}} management               | r/w          | r/o           | -               | -                | -                |
| Namespaces management            | r/w          | r/o           | -               | -                | -                |
| Provider Templates               | r/w          | r/o           | -               | -                | -                |
| Global Template Management       | r/w          | r/o           | -               | -                | -                |
| Multi Cluster Service Management | r/w          | r/o           | -               | -                | -                |
| Template Chain Management        | r/w          | r/o           | r/w             | r/o              | r/o              |
| Cluster and Service Templates    | r/w          | r/o           | r/w             | r/o              | r/o              |
| Credentials                      | r/w          | r/o           | r/w             | r/o              | r/o              |
| Flux Helm objects                | r/w          | r/o           | r/w             | r/o              | r/o              |
| Cluster Deployments              | r/w          | r/o           | r/w             | r/w              | r/o              |
