# Backing Up and Restoring a {{{ docsVersionInfo.k0rdentName }}} Management Cluster

Any production system needs to provide Disaster Recovery features, and the heart of these capabilities is the ability to
perform backup and restore operations. In this chapter we'll look at backing up and restoring {{{ docsVersionInfo.k0rdentName }}} management cluster
so that in case of an emergency, you can restore your system to its previous condition or recreate it on another cluster.

While it's possible to back up a Kubernetes cluster manually, it's better to build on the work
of others. In this case we're going to leverage the [`velero`](https://velero.io/) project for backup management
on the backend and see how it integrates with {{{ docsVersionInfo.k0rdentName }}} to ensure data persistence and recovery.

## Motivation

The primary goal of this feature is to provide a reliable and efficient way to back up and restore
a {{{ docsVersionInfo.k0rdentName }}} deployment in the event of a disaster that impacts the management cluster.
By using `velero` as the backup provider, we can create consistent backups across
different cloud storage options while maintaining the integrity of critical resources.

The main goal of the feature is to provide:

* **Management Backup:** The ability to backup all configuration objects created and managed by {{{ docsVersionInfo.k0rdentName }}}, including
  into an offsite location.
* **Restore:** The ability to create configuration objects from a specific Management Backup in order to create a management
  cluster in the same state that existed at the time of backup without (re)provisioning of cloud resources.
* **Disaster Recovery:** The ability to restore {{{ docsVersionInfo.k0rdentName }}} on another management cluster, plus ensuring that clusters are not
  recreated or lost.
* **Rollback:** The possibility to manually restore after a specific event, such as a failed {{{ docsVersionInfo.k0rdentName }}} upgrade
## Velero as Provider for Management Backups

[`Velero`](https://velero.io/) is an open-source tool that simplifies backing up and restoring clusters as well as individual resources. It seamlessly integrates into the {{{ docsVersionInfo.k0rdentName }}} management environment to provide robust disaster recovery capabilities.

The `velero` instance is part of the Helm chart that installs {{{ docsVersionInfo.k0rdentName }}}, which means that it
can be [customized](./customization.md#velero-installation) if necessary.

{{{ docsVersionInfo.k0rdentName }}} manages the schedule and is responsible for collecting data to be included in a backup.

- [Scheduled Management Backups](scheduled-backups.md)
- [Management Backup on Demand](ondemand-backups.md)
- [What's Included in a Backup](whats-included.md)
- [Restoring From Backup](restore.md)
- [Upgrades and Rollbacks](upgrades-rollbacks.md)
- [Caveats](caveats.md)
- [Customization](customization.md)
