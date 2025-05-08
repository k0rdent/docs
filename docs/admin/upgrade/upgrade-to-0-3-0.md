# Upgrading to {{{ docsVersionInfo.k0rdentName}}} 0.3.0

Several changes in 0.3.0 can require manual intervention while upgrading.

## `defaultRegistryURL` parameter rename

In {{{ docsVersionInfo.k0rdentName}}} 0.3.0, the KCM controller parameter
`defaultRegistryURL` was renamed to `templatesRepoURL`.

If you used a custom value for the `defaultRegistryURL` parameter, upon upgrade you'll need to
add `templatesRepoURL` with the same value to the
`spec.core.kcm.config.controller` of the `Management` object. After you've upgraded to
v0.3.0, you can remove the `defaultRegistryURL` parameter altogether.

## Possible projectsveltos upgrade issue

When updating the `projectsveltos` component, you may run into a problem where the
upgrade is stuck, with an error referencing an immutable field when patching the
`register-mgmt-cluster-job` `Job` object.

For example:

```
Helm upgrade failed for release projectsveltos/projectsveltos with chart projectsveltos@0.52.2: cannot patch "register-mgmt-cluster-job" with kind Job: Job.batch "register-mgmt-cluster-job" is invalid: spec.template: Invalid value
```

To mitigate this error, follow these steps:

1. Delete any jobs in the `projectsveltos` namespace:
   ```bash
   kubectl -n projectsveltos delete jobs --all
   ```
1. Fix the `projectsveltos` helm release by executing the following command:
	```bash
	TOKEN="$(date +%s)" kubectl -n kcm-system annotate hr projectsveltos "reconcile.fluxcd.io/requestedAt=$TOKEN" "reconcile.fluxcd.io/forceAt=$TOKEN"
	```
