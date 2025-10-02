# Preparing for Backups

## Preparation

> NOTE:
> The following instructions are tailored for AWS. Please adapt them to your chosen platform and storage.

Before you create a manual one-off or scheduled backup, review the steps below and update your configuration accordingly:

1. Verify whether the `velero` plugins have been installed as suggested in [Velero installation](customization.md#velero-installation). If the `velero` plugins with the desired [storage option](https://velero.io/docs/v1.15/supported-providers/) are already configured, please skip the next step.

1. If no `velero` plugins have yet been installed in your k0rdent cluster, start by getting the kcm management yaml file:

    ```sh
    kubectl get management kcm -n kcm-system -o yaml > management.yaml
    ```

    then edit the `management.yaml` file so that the velero plugin details are filled in under `spec.core.kcm`:

    ```yaml
    apiVersion: k0rdent.mirantis.com/v1beta1
    kind: Management
    metadata:
      name: kcm
    spec:
      # ... 
      core:
        kcm:
          config:
            regional:
              velero:
                initContainers:
                - name: velero-plugin-for-<PROVIDER-NAME>
                  image: velero/velero-plugin-for-<PROVIDER-NAME>:<PROVIDER-PLUGIN-TAG>
                  imagePullPolicy: IfNotPresent
                  volumeMounts:
                  - mountPath: /target
                    name: plugins
      # ...
    ```

    Please review [Velero's Docker Hub image plugin repositories](https://hub.docker.com/u/velero?page=1&search=velero-plugin)
    to help identify the required `<PROVIDER-NAME>`.
    Once the required image has been identified, select from the available tags to determine the correct
    `<PROVIDER-PLUGIN-TAG>`. In the case of AWS, the provider-name would be `velero-plugin-for-aws`, we can
    select from the [available tags](https://hub.docker.com/r/velero/velero-plugin-for-aws/tags).

1. Prepare a [storage location](https://velero.io/docs/v1.15/supported-providers/), such as an Amazon S3 bucket, to store {{{ docsVersionInfo.k0rdentName }}} backups.

1. Prepare a yaml file containing a [`BackupStorageLocation`](https://velero.io/docs/v1.15/api-types/backupstoragelocation/)
   object referencing a `Secret` with credentials to access the cloud storage
   (if the multiple credentials feature is supported by the plugin). For example, you can create the `BackupStorageLocation` and the related `Secret` yaml for the Amazon S3 configuration by following these steps.

      First create a file called `credentials.txt` with your credentials, as in:

      ```console
      [default]
      aws_access_key_id = EXAMPLE_ACCESS_KEY_ID
      aws_secret_access_key = EXAMPLE_SECRET_ACCESS_KEY
      ```

      The IAM user being used in this configuration will require certain permissions for the
      appropriate Velero S3 bucket access. Review the necessary permissions [here](https://github.com/vmware-tanzu/velero-plugin-for-aws?tab=readme-ov-file#option-1-set-permissions-with-an-iam-user). Reference the JSON policy file named `velero-policy.json` and take care to replace `${BUCKET}` with the correct bucket name).

      > NOTE:
      > If you're using EKS, the "user" is actually a role. If you get an error such as...
      >
      > ```text
      > AccessDenied: User: arn:aws:sts::026090528175:assumed-role/eksctl-JohnDoeEKSK0rdentMgmtClus-NodeInstanceRole-j0olMRJHrM0A/i-0f7dad2d91447f173 is not authorized to perform: s3:ListBucket on resource: "arn:aws:s3:::nick-chase-backup-bucket" because no identity-based policy allows the s3:ListBucket action
      > ```
      >
      > ...you can extract the role from the message (in this example, it's the assumed-role) and create the policy. For example:
      >
      > ```text
      > aws iam put-role-policy
      > --role-name eksctl-JohnDoeEKSK0rdentMgmtClus-NodeInstanceRole-j0olMRJHrM0A
      > --policy-name velero
      > --policy-document file://velero-policy.json
      > ```

      Generate the necessary base64-encoded credentials using:

      ```sh
      base64 -w0 credentials.txt; echo
      ```

      Use this base64 value in the `data.cloud` field in the `creds-and-backup-storage-location.yaml` you'll create next. Also make sure to substitute the appropriate `REGION-NAME` and `BUCKET-NAME`:

      ```yaml
      ---
      apiVersion: v1
      data:
        # base64-encoded credentials for Amazon S3 in the following format:
        # [default]
        # aws_access_key_id = EXAMPLE_ACCESS_KEY_ID
        # aws_secret_access_key = EXAMPLE_SECRET_ACCESS_KEY
        cloud: <BASE64_VALUE>
      kind: Secret
      metadata:
        name: cloud-credentials
        namespace: kcm-system
      type: Opaque
      ---
      apiVersion: velero.io/v1
      kind: BackupStorageLocation
      metadata:
        name: aws-s3
        namespace: kcm-system
      spec:
        config:
          region: <REGION-NAME>
        default: true # optional, if not set, then storage location name must always be set in ManagementBackup
        objectStorage:
          bucket: <BUCKET-NAME>
        provider: aws
        backupSyncPeriod: 1m
        credential:
          name: cloud-credentials
          key: cloud
      ```

1. Create the necessary Kubernetes resources in your k0rdent cluster by applying the YAML to the management cluster:

    ```sh
    kubectl apply -f creds-and-backup-storage-location.yaml
    kubectl apply -f management.yaml
    ```

1. Confirm that the previous steps were applied correctly:

    ```sh
    kubectl get management kcm -n kcm-system -o yaml
    ```

    The management configuration yaml should have the new velero plugin details, as shown in step 2.

    Now make sure the `backupstoragelocation` shows as `Available`:

    ```sh
    kubectl get backupstoragelocation -n kcm-system
    ```

    ```console
    NAME     PHASE       LAST VALIDATED   AGE   DEFAULT
    aws-s3   Available   27s              2d    true
    ```

You can get more information on how to build these objects at the [official Velero documentation](https://velero.io/docs/v1.15/locations).
