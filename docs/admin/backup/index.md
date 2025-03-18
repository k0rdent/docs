# Backing Up and Restoring a k0rdent Management Cluster

Any production system needs to provide Disaster Recovery features, and the heart of these capabilities is the ability to
perform backup and restore operations. In this chapter we'll look at backing up and restoring k0rdent management cluster
so that in case of an emergency, you can restore your system to its previous condition or recreate it on another cluster.

While it's possible to back up a Kubernetes cluster manually, it's better to build on the work
of others. In this case we're going to leverage the [`velero`](https://velero.io/) project for backup management
on the backend and see how it integrates with k0rdent to ensure data persistence and recovery.

## Motivation

The primary goal of this feature is to provide a reliable and efficient way to back up and restore
a k0rdent deployment in the event of a disaster that impacts the management cluster.
By using `velero` as the backup provider, we can create consistent backups across
different cloud storage options while maintaining the integrity of critical resources.

The main goal of the feature is to provide:

* **Management Backup:** The ability to backup all configuration objects created and managed by k0rdent, including
  into an offsite location.
* **Restore:** The ability to create configuration objects from a specific Management Backup in order to create a management
  cluster in the same state that existed at the time of backup without (re)provisioning of cloud resources.
* **Disaster Recovery:** The ability to restore k0rdent on another management cluster, plus ensuring that clusters are not
  recreated or lost.
* **Rollback:** The possibility to manually restore after a specific event, such as a failed k0rdent upgrade
## Velero as Provider for Management Backups

[`Velero`](https://velero.io/) is an open-source tool that simplifies backing up and restoring clusters as well as individual resources. It seamlessly integrates into the k0rdent management environment to provide robust disaster recovery capabilities.

The `velero` instance is part of the Helm chart that installs k0rdent, which means that it
can be [customized](./customization.md#velero-installation) if necessary.

k0rdent manages the schedule and is responsible for collecting data to be included in a backup.
