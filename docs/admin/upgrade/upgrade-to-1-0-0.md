# Upgrading to {{{ docsVersionInfo.k0rdentName}}} 1.0.0

The actual process of upgrading {{{ docsVersionInfo.k0rdentName}}} to 1.0.0 doesn't require any additional steps
beyond those listed in the [general upgrade instructions](index.md), but there are several changes that may
affect ancilliary artifacts.

Specifically, as part of ongoing improvements to the {{{ docsVersionInfo.k0rdentName}}} API, we have upgraded the 
`apiVersion` from `v1alpha1` to `v1beta1`. This change introduces enhancements in stability and forward compatibility, 
but may require updates to any existing automation, scripts, or integrations built against the earlier version.

