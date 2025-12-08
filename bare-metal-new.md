
## Overview of Bare Metal Support

### What the Bare Metal Provider Does

### Key Components (CAPM3, Ironic, IPA, Templates)

### When to Use Bare Metal vs Cloud Providers

## Prerequisites and Environment Requirements

### Hardware Requirements

### Network Requirements

### Required Tools and Installed Components

### Supported BMC Protocols (IPMI, Redfish)

## Prepare the Management Cluster

### Install OOT CAPM3 Provider

### Validate ProviderTemplate and ClusterTemplate

### Configure the Management Object

### Verify Management Cluster Readiness

### Optional: DHCP Server Tuning

### Optional: Use MetalLB on the Management Cluster

## Enroll Bare Metal Hosts

### Create BMC Credential Secrets

### Create BareMetalHost Objects

### Understanding Provisioning States

### Optional: Root Device Hints

### Optional: RAID Configuration Limits

## Deploy a Bare Metal Cluster

### Create Cluster Credential Objects

### Create Configuration Resource Templates

### Build and Apply ClusterDeployment

### Monitor Host Provisioning

### Retrieve and Use the Kubeconfig

### Cleanup and Reuse Bare Metal Hosts

### Optional: Install MetalLB on Child Clusters

## Optional and Advanced Configuration

### OS and Software Update Workflow (Deprovision/Reprovision)

### Custom Cloud-Init UserData for Partitioning

### Block Device and Filesystem Management

### RAID Configuration Constraints

### Using Configuration Management Tools (Ansible, etc.)

## Air-Gapped Deployment

### Prepare and Verify Airgap Bundles

### Upload Charts and Images to Offline Registry

### Configure CAPM3 Provider for Airgapped Environments

### Deploy Bare Metal Clusters in Airgap Mode

### Airgap-Specific Behavior and Restrictions

## Multi-Architecture Provisioning

### Requirements and Limitations

### Preparing Target OS Images for amd64/arm64

### Labeling BareMetalHosts for Architecture Selection

### Deploying Mixed-Architecture Worker Pools

### Unsupported Topologies

## Troubleshooting and Common Failure Modes

### Host Enrollment Problems

### Provisioning Stuck or Failed

### Common Network Misconfigurations

### BMC Protocol Issues (IPMI/Redfish)

### Image, Cloud-Init, or RAID Errors

### Airgap Deployment Failures

