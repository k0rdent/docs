# API Reference

Packages:

- [k0rdent.mirantis.com/v1alpha1](#k0rdentmirantiscomv1alpha1)
- [k0rdent.mirantis.com/v1beta1](#k0rdentmirantiscomv1beta1)

# k0rdent.mirantis.com/v1alpha1

Resource Types:

- [AccessManagement](#accessmanagement)

- [ClusterDeployment](#clusterdeployment)

- [ClusterTemplateChain](#clustertemplatechain)

- [ClusterTemplate](#clustertemplate)

- [Credential](#credential)

- [ManagementBackup](#managementbackup)

- [Management](#management)

- [MultiClusterService](#multiclusterservice)

- [ProviderInterface](#providerinterface)

- [ProviderTemplate](#providertemplate)

- [Release](#release)

- [ServiceTemplateChain](#servicetemplatechain)

- [ServiceTemplate](#servicetemplate)




## AccessManagement
<sup><sup>[↩ Parent](#k0rdentmirantiscomv1alpha1 )</sup></sup>






AccessManagement is the Schema for the AccessManagements API

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
      <td><b>apiVersion</b></td>
      <td>string</td>
      <td>k0rdent.mirantis.com/v1alpha1</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b>kind</b></td>
      <td>string</td>
      <td>AccessManagement</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#accessmanagementspec">spec</a></b></td>
        <td>object</td>
        <td>
          AccessManagementSpec defines the desired state of AccessManagement<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#accessmanagementstatus">status</a></b></td>
        <td>object</td>
        <td>
          AccessManagementStatus defines the observed state of AccessManagement<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### AccessManagement.spec
<sup><sup>[↩ Parent](#accessmanagement)</sup></sup>



AccessManagementSpec defines the desired state of AccessManagement

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#accessmanagementspecaccessrulesindex">accessRules</a></b></td>
        <td>[]object</td>
        <td>
          AccessRules is the list of access rules. Each AccessRule enforces
objects distribution to the TargetNamespaces.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### AccessManagement.spec.accessRules[index]
<sup><sup>[↩ Parent](#accessmanagementspec)</sup></sup>



AccessRule is the definition of the AccessManagement access rule. Each AccessRule enforces
Templates and Credentials distribution to the TargetNamespaces

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>clusterTemplateChains</b></td>
        <td>[]string</td>
        <td>
          ClusterTemplateChains lists the names of ClusterTemplateChains whose ClusterTemplates
will be distributed to all namespaces specified in TargetNamespaces.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>credentials</b></td>
        <td>[]string</td>
        <td>
          Credentials is the list of Credential names that will be distributed to all the
namespaces specified in TargetNamespaces.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>serviceTemplateChains</b></td>
        <td>[]string</td>
        <td>
          ServiceTemplateChains lists the names of ServiceTemplateChains whose ServiceTemplates
will be distributed to all namespaces specified in TargetNamespaces.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#accessmanagementspecaccessrulesindextargetnamespaces">targetNamespaces</a></b></td>
        <td>object</td>
        <td>
          TargetNamespaces defines the namespaces where selected objects will be distributed.
Templates and Credentials will be distributed to all namespaces if unset.<br/>
          <br/>
            <i>Validations</i>:<li>((has(self.stringSelector) ? 1 : 0) + (has(self.selector) ? 1 : 0) + (has(self.list) ? 1 : 0)) <= 1: only one of spec.targetNamespaces.selector or spec.targetNamespaces.stringSelector or spec.targetNamespaces.list can be specified</li>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### AccessManagement.spec.accessRules[index].targetNamespaces
<sup><sup>[↩ Parent](#accessmanagementspecaccessrulesindex)</sup></sup>



TargetNamespaces defines the namespaces where selected objects will be distributed.
Templates and Credentials will be distributed to all namespaces if unset.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>list</b></td>
        <td>[]string</td>
        <td>
          List is the list of namespaces to select.
Mutually exclusive with StringSelector and Selector.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#accessmanagementspecaccessrulesindextargetnamespacesselector">selector</a></b></td>
        <td>object</td>
        <td>
          Selector is a structured label query to select namespaces.
Mutually exclusive with StringSelector and List.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>stringSelector</b></td>
        <td>string</td>
        <td>
          StringSelector is a label query to select namespaces.
Mutually exclusive with Selector and List.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### AccessManagement.spec.accessRules[index].targetNamespaces.selector
<sup><sup>[↩ Parent](#accessmanagementspecaccessrulesindextargetnamespaces)</sup></sup>



Selector is a structured label query to select namespaces.
Mutually exclusive with StringSelector and List.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#accessmanagementspecaccessrulesindextargetnamespacesselectormatchexpressionsindex">matchExpressions</a></b></td>
        <td>[]object</td>
        <td>
          matchExpressions is a list of label selector requirements. The requirements are ANDed.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>matchLabels</b></td>
        <td>map[string]string</td>
        <td>
          matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels
map is equivalent to an element of matchExpressions, whose key field is "key", the
operator is "In", and the values array contains only "value". The requirements are ANDed.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### AccessManagement.spec.accessRules[index].targetNamespaces.selector.matchExpressions[index]
<sup><sup>[↩ Parent](#accessmanagementspecaccessrulesindextargetnamespacesselector)</sup></sup>



A label selector requirement is a selector that contains values, a key, and an operator that
relates the key and values.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>key</b></td>
        <td>string</td>
        <td>
          key is the label key that the selector applies to.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>operator</b></td>
        <td>string</td>
        <td>
          operator represents a key's relationship to a set of values.
Valid operators are In, NotIn, Exists and DoesNotExist.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>values</b></td>
        <td>[]string</td>
        <td>
          values is an array of string values. If the operator is In or NotIn,
the values array must be non-empty. If the operator is Exists or DoesNotExist,
the values array must be empty. This array is replaced during a strategic
merge patch.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### AccessManagement.status
<sup><sup>[↩ Parent](#accessmanagement)</sup></sup>



AccessManagementStatus defines the observed state of AccessManagement

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#accessmanagementstatuscurrentindex">current</a></b></td>
        <td>[]object</td>
        <td>
          Current reflects the applied access rules configuration.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>error</b></td>
        <td>string</td>
        <td>
          Error is the error message occurred during the reconciliation (if any)<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>observedGeneration</b></td>
        <td>integer</td>
        <td>
          ObservedGeneration is the last observed generation.<br/>
          <br/>
            <i>Format</i>: int64<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### AccessManagement.status.current[index]
<sup><sup>[↩ Parent](#accessmanagementstatus)</sup></sup>



AccessRule is the definition of the AccessManagement access rule. Each AccessRule enforces
Templates and Credentials distribution to the TargetNamespaces

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>clusterTemplateChains</b></td>
        <td>[]string</td>
        <td>
          ClusterTemplateChains lists the names of ClusterTemplateChains whose ClusterTemplates
will be distributed to all namespaces specified in TargetNamespaces.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>credentials</b></td>
        <td>[]string</td>
        <td>
          Credentials is the list of Credential names that will be distributed to all the
namespaces specified in TargetNamespaces.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>serviceTemplateChains</b></td>
        <td>[]string</td>
        <td>
          ServiceTemplateChains lists the names of ServiceTemplateChains whose ServiceTemplates
will be distributed to all namespaces specified in TargetNamespaces.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#accessmanagementstatuscurrentindextargetnamespaces">targetNamespaces</a></b></td>
        <td>object</td>
        <td>
          TargetNamespaces defines the namespaces where selected objects will be distributed.
Templates and Credentials will be distributed to all namespaces if unset.<br/>
          <br/>
            <i>Validations</i>:<li>((has(self.stringSelector) ? 1 : 0) + (has(self.selector) ? 1 : 0) + (has(self.list) ? 1 : 0)) <= 1: only one of spec.targetNamespaces.selector or spec.targetNamespaces.stringSelector or spec.targetNamespaces.list can be specified</li>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### AccessManagement.status.current[index].targetNamespaces
<sup><sup>[↩ Parent](#accessmanagementstatuscurrentindex)</sup></sup>



TargetNamespaces defines the namespaces where selected objects will be distributed.
Templates and Credentials will be distributed to all namespaces if unset.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>list</b></td>
        <td>[]string</td>
        <td>
          List is the list of namespaces to select.
Mutually exclusive with StringSelector and Selector.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#accessmanagementstatuscurrentindextargetnamespacesselector">selector</a></b></td>
        <td>object</td>
        <td>
          Selector is a structured label query to select namespaces.
Mutually exclusive with StringSelector and List.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>stringSelector</b></td>
        <td>string</td>
        <td>
          StringSelector is a label query to select namespaces.
Mutually exclusive with Selector and List.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### AccessManagement.status.current[index].targetNamespaces.selector
<sup><sup>[↩ Parent](#accessmanagementstatuscurrentindextargetnamespaces)</sup></sup>



Selector is a structured label query to select namespaces.
Mutually exclusive with StringSelector and List.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#accessmanagementstatuscurrentindextargetnamespacesselectormatchexpressionsindex">matchExpressions</a></b></td>
        <td>[]object</td>
        <td>
          matchExpressions is a list of label selector requirements. The requirements are ANDed.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>matchLabels</b></td>
        <td>map[string]string</td>
        <td>
          matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels
map is equivalent to an element of matchExpressions, whose key field is "key", the
operator is "In", and the values array contains only "value". The requirements are ANDed.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### AccessManagement.status.current[index].targetNamespaces.selector.matchExpressions[index]
<sup><sup>[↩ Parent](#accessmanagementstatuscurrentindextargetnamespacesselector)</sup></sup>



A label selector requirement is a selector that contains values, a key, and an operator that
relates the key and values.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>key</b></td>
        <td>string</td>
        <td>
          key is the label key that the selector applies to.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>operator</b></td>
        <td>string</td>
        <td>
          operator represents a key's relationship to a set of values.
Valid operators are In, NotIn, Exists and DoesNotExist.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>values</b></td>
        <td>[]string</td>
        <td>
          values is an array of string values. If the operator is In or NotIn,
the values array must be non-empty. If the operator is Exists or DoesNotExist,
the values array must be empty. This array is replaced during a strategic
merge patch.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>

## ClusterDeployment
<sup><sup>[↩ Parent](#k0rdentmirantiscomv1alpha1 )</sup></sup>






ClusterDeployment is the Schema for the ClusterDeployments API

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
      <td><b>apiVersion</b></td>
      <td>string</td>
      <td>k0rdent.mirantis.com/v1alpha1</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b>kind</b></td>
      <td>string</td>
      <td>ClusterDeployment</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#clusterdeploymentspec">spec</a></b></td>
        <td>object</td>
        <td>
          ClusterDeploymentSpec defines the desired state of ClusterDeployment<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clusterdeploymentstatus">status</a></b></td>
        <td>object</td>
        <td>
          ClusterDeploymentStatus defines the observed state of ClusterDeployment<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.spec
<sup><sup>[↩ Parent](#clusterdeployment)</sup></sup>



ClusterDeploymentSpec defines the desired state of ClusterDeployment

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>template</b></td>
        <td>string</td>
        <td>
          Template is a reference to a Template object located in the same namespace.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>config</b></td>
        <td>JSON</td>
        <td>
          Config allows to provide parameters for template customization.
If no Config provided, the field will be populated with the default values for
the template and DryRun will be enabled.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>credential</b></td>
        <td>string</td>
        <td>
          Name reference to the related Credentials object.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>dryRun</b></td>
        <td>boolean</td>
        <td>
          DryRun specifies whether the template should be applied after validation or only validated.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>propagateCredentials</b></td>
        <td>boolean</td>
        <td>
          PropagateCredentials indicates whether credentials should be propagated
for use by CCM (Cloud Controller Manager).<br/>
          <br/>
            <i>Default</i>: true<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clusterdeploymentspecservicespec">serviceSpec</a></b></td>
        <td>object</td>
        <td>
          ServiceSpec is spec related to deployment of services.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.spec.serviceSpec
<sup><sup>[↩ Parent](#clusterdeploymentspec)</sup></sup>



ServiceSpec is spec related to deployment of services.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>continueOnError</b></td>
        <td>boolean</td>
        <td>
          ContinueOnError specifies if the services deployment should continue if an error occurs.<br/>
          <br/>
            <i>Default</i>: false<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clusterdeploymentspecservicespecdriftexclusionsindex">driftExclusions</a></b></td>
        <td>[]object</td>
        <td>
          DriftExclusions specifies specific configurations of resources to ignore for drift detection.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clusterdeploymentspecservicespecdriftignoreindex">driftIgnore</a></b></td>
        <td>[]object</td>
        <td>
          DriftIgnore specifies resources to ignore for drift detection.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>priority</b></td>
        <td>integer</td>
        <td>
          Priority sets the priority for the services defined in this spec.
Higher value means higher priority and lower means lower.
In case of conflict with another object managing the service,
the one with higher priority will get to deploy its services.<br/>
          <br/>
            <i>Format</i>: int32<br/>
            <i>Default</i>: 100<br/>
            <i>Minimum</i>: 1<br/>
            <i>Maximum</i>: 2.147483646e+09<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>reload</b></td>
        <td>boolean</td>
        <td>
          Reload instances via rolling upgrade when a ConfigMap/Secret mounted as volume is modified.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clusterdeploymentspecservicespecservicesindex">services</a></b></td>
        <td>[]object</td>
        <td>
          Services is a list of services created via ServiceTemplates
that could be installed on the target cluster.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>stopOnConflict</b></td>
        <td>boolean</td>
        <td>
          StopOnConflict specifies what to do in case of a conflict.
E.g. If another object is already managing a service.
By default the remaining services will be deployed even if conflict is detected.
If set to true, the deployment will stop after encountering the first conflict.<br/>
          <br/>
            <i>Default</i>: false<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>syncMode</b></td>
        <td>enum</td>
        <td>
          SyncMode specifies how services are synced in the target cluster.<br/>
          <br/>
            <i>Enum</i>: OneTime, Continuous, ContinuousWithDriftDetection, DryRun<br/>
            <i>Default</i>: Continuous<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clusterdeploymentspecservicespectemplateresourcerefsindex">templateResourceRefs</a></b></td>
        <td>[]object</td>
        <td>
          TemplateResourceRefs is a list of resources to collect from the management cluster,
the values from which can be used in templates.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.spec.serviceSpec.driftExclusions[index]
<sup><sup>[↩ Parent](#clusterdeploymentspecservicespec)</sup></sup>





<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>paths</b></td>
        <td>[]string</td>
        <td>
          Paths is a slice of JSON6902 paths to exclude from configuration drift evaluation.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#clusterdeploymentspecservicespecdriftexclusionsindextarget">target</a></b></td>
        <td>object</td>
        <td>
          Target points to the resources that the paths refers to.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.spec.serviceSpec.driftExclusions[index].target
<sup><sup>[↩ Parent](#clusterdeploymentspecservicespecdriftexclusionsindex)</sup></sup>



Target points to the resources that the paths refers to.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>annotationSelector</b></td>
        <td>string</td>
        <td>
          AnnotationSelector is a string that follows the label selection expression
https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#api
It matches with the resource annotations.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>group</b></td>
        <td>string</td>
        <td>
          Group is the API group to select resources from.
Together with Version and Kind it is capable of unambiguously identifying and/or selecting resources.
https://github.com/kubernetes/community/blob/master/contributors/design-proposals/api-machinery/api-group.md<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>kind</b></td>
        <td>string</td>
        <td>
          Kind of the API Group to select resources from.
Together with Group and Version it is capable of unambiguously
identifying and/or selecting resources.
https://github.com/kubernetes/community/blob/master/contributors/design-proposals/api-machinery/api-group.md<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>labelSelector</b></td>
        <td>string</td>
        <td>
          LabelSelector is a string that follows the label selection expression
https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#api
It matches with the resource labels.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name to match resources with.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace to select resources from.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>version</b></td>
        <td>string</td>
        <td>
          Version of the API Group to select resources from.
Together with Group and Kind it is capable of unambiguously identifying and/or selecting resources.
https://github.com/kubernetes/community/blob/master/contributors/design-proposals/api-machinery/api-group.md<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.spec.serviceSpec.driftIgnore[index]
<sup><sup>[↩ Parent](#clusterdeploymentspecservicespec)</sup></sup>





<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>annotationSelector</b></td>
        <td>string</td>
        <td>
          AnnotationSelector is a string that follows the label selection expression
https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#api
It matches with the resource annotations.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>group</b></td>
        <td>string</td>
        <td>
          Group is the API group to select resources from.
Together with Version and Kind it is capable of unambiguously identifying and/or selecting resources.
https://github.com/kubernetes/community/blob/master/contributors/design-proposals/api-machinery/api-group.md<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>kind</b></td>
        <td>string</td>
        <td>
          Kind of the API Group to select resources from.
Together with Group and Version it is capable of unambiguously
identifying and/or selecting resources.
https://github.com/kubernetes/community/blob/master/contributors/design-proposals/api-machinery/api-group.md<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>labelSelector</b></td>
        <td>string</td>
        <td>
          LabelSelector is a string that follows the label selection expression
https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#api
It matches with the resource labels.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name to match resources with.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace to select resources from.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>version</b></td>
        <td>string</td>
        <td>
          Version of the API Group to select resources from.
Together with Group and Kind it is capable of unambiguously identifying and/or selecting resources.
https://github.com/kubernetes/community/blob/master/contributors/design-proposals/api-machinery/api-group.md<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.spec.serviceSpec.services[index]
<sup><sup>[↩ Parent](#clusterdeploymentspecservicespec)</sup></sup>



Service represents a Service to be deployed.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name is the chart release.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>template</b></td>
        <td>string</td>
        <td>
          Template is a reference to a Template object located in the same namespace.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>disable</b></td>
        <td>boolean</td>
        <td>
          Disable can be set to disable handling of this service.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace is the namespace the release will be installed in.
It will default to Name if not provided.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>templateChain</b></td>
        <td>string</td>
        <td>
          TemplateChain defines the ServiceTemplateChain object that will be used to deploy the service
along with desired ServiceTemplate version.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>values</b></td>
        <td>string</td>
        <td>
          Values is the helm values to be passed to the chart used by the template.
The string type is used in order to allow for templating.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clusterdeploymentspecservicespecservicesindexvaluesfromindex">valuesFrom</a></b></td>
        <td>[]object</td>
        <td>
          ValuesFrom can reference a ConfigMap or Secret containing helm values.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.spec.serviceSpec.services[index].valuesFrom[index]
<sup><sup>[↩ Parent](#clusterdeploymentspecservicespecservicesindex)</sup></sup>





<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>kind</b></td>
        <td>enum</td>
        <td>
          Kind of the resource. Supported kinds are:
- ConfigMap/Secret<br/>
          <br/>
            <i>Enum</i>: ConfigMap, Secret<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referenced resource.
Name can be expressed as a template and instantiate using any cluster field.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace of the referenced resource.
For ClusterProfile namespace can be left empty. In such a case, namespace will
be implicit set to cluster's namespace.
For Profile namespace must be left empty. The Profile namespace will be used.
Namespace can be expressed as a template and instantiate using any cluster field.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>optional</b></td>
        <td>boolean</td>
        <td>
          Optional indicates that the referenced resource is not mandatory.
If set to true and the resource is not found, the error will be ignored,
and Sveltos will continue processing other ValueFroms.<br/>
          <br/>
            <i>Default</i>: false<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.spec.serviceSpec.templateResourceRefs[index]
<sup><sup>[↩ Parent](#clusterdeploymentspecservicespec)</sup></sup>





<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>identifier</b></td>
        <td>string</td>
        <td>
          Identifier is how the resource will be referred to in the
template<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#clusterdeploymentspecservicespectemplateresourcerefsindexresource">resource</a></b></td>
        <td>object</td>
        <td>
          Resource references a Kubernetes instance in the management
cluster to fetch and use during template instantiation.
For ClusterProfile namespace can be left empty. In such a case, namespace will
be implicit set to cluster's namespace.
Name and namespace can be expressed as a template and instantiate using any cluster field.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>optional</b></td>
        <td>boolean</td>
        <td>
          Optional indicates that the referenced resource is not mandatory.
If set to true and the resource is not found, the error will be ignored,
and Sveltos will continue processing other TemplateResourceRefs.<br/>
          <br/>
            <i>Default</i>: false<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.spec.serviceSpec.templateResourceRefs[index].resource
<sup><sup>[↩ Parent](#clusterdeploymentspecservicespectemplateresourcerefsindex)</sup></sup>



Resource references a Kubernetes instance in the management
cluster to fetch and use during template instantiation.
For ClusterProfile namespace can be left empty. In such a case, namespace will
be implicit set to cluster's namespace.
Name and namespace can be expressed as a template and instantiate using any cluster field.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>apiVersion</b></td>
        <td>string</td>
        <td>
          API version of the referent.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>fieldPath</b></td>
        <td>string</td>
        <td>
          If referring to a piece of an object instead of an entire object, this string
should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2].
For example, if the object reference is to a container within a pod, this would take on a value like:
"spec.containers{name}" (where "name" refers to the name of the container that triggered
the event) or if no container name is specified "spec.containers[2]" (container with
index 2 in this pod). This syntax is chosen only to have some well-defined way of
referencing a part of an object.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>kind</b></td>
        <td>string</td>
        <td>
          Kind of the referent.
More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.
More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace of the referent.
More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>resourceVersion</b></td>
        <td>string</td>
        <td>
          Specific resourceVersion to which this reference is made, if any.
More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>uid</b></td>
        <td>string</td>
        <td>
          UID of the referent.
More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.status
<sup><sup>[↩ Parent](#clusterdeployment)</sup></sup>



ClusterDeploymentStatus defines the observed state of ClusterDeployment

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>availableUpgrades</b></td>
        <td>[]string</td>
        <td>
          AvailableUpgrades is the list of ClusterTemplate names to which
this cluster can be upgraded. It can be an empty array, which means no upgrades are
available.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clusterdeploymentstatusconditionsindex">conditions</a></b></td>
        <td>[]object</td>
        <td>
          Conditions contains details for the current state of the ClusterDeployment.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>k8sVersion</b></td>
        <td>string</td>
        <td>
          Currently compatible exact Kubernetes version of the cluster. Being set only if
provided by the corresponding ClusterTemplate.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>observedGeneration</b></td>
        <td>integer</td>
        <td>
          ObservedGeneration is the last observed generation.<br/>
          <br/>
            <i>Format</i>: int64<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clusterdeploymentstatusservicesindex">services</a></b></td>
        <td>[]object</td>
        <td>
          Services contains details for the state of services.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clusterdeploymentstatusservicesupgradepathsindex">servicesUpgradePaths</a></b></td>
        <td>[]object</td>
        <td>
          ServicesUpgradePaths contains details for the state of services upgrade paths.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.status.conditions[index]
<sup><sup>[↩ Parent](#clusterdeploymentstatus)</sup></sup>



Condition contains details for one aspect of the current state of this API Resource.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>lastTransitionTime</b></td>
        <td>string</td>
        <td>
          lastTransitionTime is the last time the condition transitioned from one status to another.
This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable.<br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>message</b></td>
        <td>string</td>
        <td>
          message is a human readable message indicating details about the transition.
This may be an empty string.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>reason</b></td>
        <td>string</td>
        <td>
          reason contains a programmatic identifier indicating the reason for the condition's last transition.
Producers of specific condition types may define expected values and meanings for this field,
and whether the values are considered a guaranteed API.
The value should be a CamelCase string.
This field may not be empty.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>status</b></td>
        <td>enum</td>
        <td>
          status of the condition, one of True, False, Unknown.<br/>
          <br/>
            <i>Enum</i>: True, False, Unknown<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>type</b></td>
        <td>string</td>
        <td>
          type of condition in CamelCase or in foo.example.com/CamelCase.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>observedGeneration</b></td>
        <td>integer</td>
        <td>
          observedGeneration represents the .metadata.generation that the condition was set based upon.
For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date
with respect to the current state of the instance.<br/>
          <br/>
            <i>Format</i>: int64<br/>
            <i>Minimum</i>: 0<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.status.services[index]
<sup><sup>[↩ Parent](#clusterdeploymentstatus)</sup></sup>



ServiceStatus contains details for the state of services.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>clusterName</b></td>
        <td>string</td>
        <td>
          ClusterName is the name of the associated cluster.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>clusterNamespace</b></td>
        <td>string</td>
        <td>
          ClusterNamespace is the namespace of the associated cluster.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clusterdeploymentstatusservicesindexconditionsindex">conditions</a></b></td>
        <td>[]object</td>
        <td>
          Conditions contains details for the current state of managed services.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.status.services[index].conditions[index]
<sup><sup>[↩ Parent](#clusterdeploymentstatusservicesindex)</sup></sup>



Condition contains details for one aspect of the current state of this API Resource.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>lastTransitionTime</b></td>
        <td>string</td>
        <td>
          lastTransitionTime is the last time the condition transitioned from one status to another.
This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable.<br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>message</b></td>
        <td>string</td>
        <td>
          message is a human readable message indicating details about the transition.
This may be an empty string.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>reason</b></td>
        <td>string</td>
        <td>
          reason contains a programmatic identifier indicating the reason for the condition's last transition.
Producers of specific condition types may define expected values and meanings for this field,
and whether the values are considered a guaranteed API.
The value should be a CamelCase string.
This field may not be empty.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>status</b></td>
        <td>enum</td>
        <td>
          status of the condition, one of True, False, Unknown.<br/>
          <br/>
            <i>Enum</i>: True, False, Unknown<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>type</b></td>
        <td>string</td>
        <td>
          type of condition in CamelCase or in foo.example.com/CamelCase.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>observedGeneration</b></td>
        <td>integer</td>
        <td>
          observedGeneration represents the .metadata.generation that the condition was set based upon.
For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date
with respect to the current state of the instance.<br/>
          <br/>
            <i>Format</i>: int64<br/>
            <i>Minimum</i>: 0<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.status.servicesUpgradePaths[index]
<sup><sup>[↩ Parent](#clusterdeploymentstatus)</sup></sup>



ServiceUpgradePaths contains details for the state of service upgrade paths.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name is the name of the service.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace is the namespace of the service.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>template</b></td>
        <td>string</td>
        <td>
          Template is the name of the current service template.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#clusterdeploymentstatusservicesupgradepathsindexavailableupgradesindex">availableUpgrades</a></b></td>
        <td>[]object</td>
        <td>
          AvailableUpgrades contains details for the state of available upgrades.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.status.servicesUpgradePaths[index].availableUpgrades[index]
<sup><sup>[↩ Parent](#clusterdeploymentstatusservicesupgradepathsindex)</sup></sup>



UpgradePath contains details for the state of service upgrade paths.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>upgradePaths</b></td>
        <td>[]string</td>
        <td>
          Versions contains the list of versions that service can be upgraded to.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>

## ClusterTemplateChain
<sup><sup>[↩ Parent](#k0rdentmirantiscomv1alpha1 )</sup></sup>






ClusterTemplateChain is the Schema for the clustertemplatechains API

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
      <td><b>apiVersion</b></td>
      <td>string</td>
      <td>k0rdent.mirantis.com/v1alpha1</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b>kind</b></td>
      <td>string</td>
      <td>ClusterTemplateChain</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#clustertemplatechainspec">spec</a></b></td>
        <td>object</td>
        <td>
          TemplateChainSpec defines the desired state of *TemplateChain<br/>
          <br/>
            <i>Validations</i>:<li>self == oldSelf: Spec is immutable</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatechainstatus">status</a></b></td>
        <td>object</td>
        <td>
          TemplateChainStatus defines the observed state of *TemplateChain<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplateChain.spec
<sup><sup>[↩ Parent](#clustertemplatechain)</sup></sup>



TemplateChainSpec defines the desired state of *TemplateChain

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#clustertemplatechainspecsupportedtemplatesindex">supportedTemplates</a></b></td>
        <td>[]object</td>
        <td>
          SupportedTemplates is the list of supported Templates definitions and all available upgrade sequences for it.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplateChain.spec.supportedTemplates[index]
<sup><sup>[↩ Parent](#clustertemplatechainspec)</sup></sup>



SupportedTemplate is the supported Template definition and all available upgrade sequences for it

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name is the name of the Template.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#clustertemplatechainspecsupportedtemplatesindexavailableupgradesindex">availableUpgrades</a></b></td>
        <td>[]object</td>
        <td>
          AvailableUpgrades is the list of available upgrades for the specified Template.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplateChain.spec.supportedTemplates[index].availableUpgrades[index]
<sup><sup>[↩ Parent](#clustertemplatechainspecsupportedtemplatesindex)</sup></sup>



AvailableUpgrade is the definition of the available upgrade for the Template

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name is the name of the Template to which the upgrade is available.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ClusterTemplateChain.status
<sup><sup>[↩ Parent](#clustertemplatechain)</sup></sup>



TemplateChainStatus defines the observed state of *TemplateChain

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>valid</b></td>
        <td>boolean</td>
        <td>
          Valid indicates whether the chain is valid and can be considered when calculating available
upgrade paths.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>validationError</b></td>
        <td>string</td>
        <td>
          ValidationError provides information regarding issues encountered during templatechain validation.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>

## ClusterTemplate
<sup><sup>[↩ Parent](#k0rdentmirantiscomv1alpha1 )</sup></sup>






ClusterTemplate is the Schema for the clustertemplates API

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
      <td><b>apiVersion</b></td>
      <td>string</td>
      <td>k0rdent.mirantis.com/v1alpha1</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b>kind</b></td>
      <td>string</td>
      <td>ClusterTemplate</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespec">spec</a></b></td>
        <td>object</td>
        <td>
          ClusterTemplateSpec defines the desired state of ClusterTemplate<br/>
          <br/>
            <i>Validations</i>:<li>self == oldSelf: Spec is immutable</li><li>!has(self.helm.chartSource): .spec.helm.chartSource is not supported for ClusterTemplates</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatestatus">status</a></b></td>
        <td>object</td>
        <td>
          ClusterTemplateStatus defines the observed state of ClusterTemplate<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec
<sup><sup>[↩ Parent](#clustertemplate)</sup></sup>



ClusterTemplateSpec defines the desired state of ClusterTemplate

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#clustertemplatespechelm">helm</a></b></td>
        <td>object</td>
        <td>
          HelmSpec references a Helm chart representing the KCM template<br/>
          <br/>
            <i>Validations</i>:<li>(has(self.chartSpec) ? (!has(self.chartSource) && !has(self.chartRef)): true): chartSpec, chartSource and chartRef are mutually exclusive</li><li>(has(self.chartSource) ? (!has(self.chartSpec) && !has(self.chartRef)): true): chartSpec, chartSource and chartRef are mutually exclusive</li><li>(has(self.chartRef) ? (!has(self.chartSpec) && !has(self.chartSource)): true): chartSpec, chartSource and chartRef are mutually exclusive</li><li>has(self.chartSpec) || has(self.chartRef) || has(self.chartSource): one of chartSpec, chartRef or chartSource must be set</li>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>k8sVersion</b></td>
        <td>string</td>
        <td>
          Kubernetes exact version in the SemVer format provided by this ClusterTemplate.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>providerContracts</b></td>
        <td>map[string]string</td>
        <td>
          Holds key-value pairs with compatibility [contract versions],
where the key is the name of the provider,
and the value is the provider contract version
required to be supported by the provider.

[contract versions]: https://cluster-api.sigs.k8s.io/developer/providers/contracts<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>providers</b></td>
        <td>[]string</td>
        <td>
          Providers represent required CAPI providers.
Should be set if not present in the Helm chart metadata.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm
<sup><sup>[↩ Parent](#clustertemplatespec)</sup></sup>



HelmSpec references a Helm chart representing the KCM template

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#clustertemplatespechelmchartref">chartRef</a></b></td>
        <td>object</td>
        <td>
          ChartRef is a reference to a source controller resource containing the
Helm chart representing the template.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsource">chartSource</a></b></td>
        <td>object</td>
        <td>
          ChartSource is a source of a Helm chart representing the template.<br/>
          <br/>
            <i>Validations</i>:<li>has(self.localSourceRef) ? (self.localSourceRef.kind != 'Secret' && self.localSourceRef.kind != 'ConfigMap'): true: Secret and ConfigMap are not supported as Helm chart sources</li><li>has(self.localSourceRef) ? !has(self.remoteSourceSpec): true: LocalSource and RemoteSource are mutually exclusive.</li><li>has(self.remoteSourceSpec) ? !has(self.localSourceRef): true: LocalSource and RemoteSource are mutually exclusive.</li><li>has(self.localSourceRef) || has(self.remoteSourceSpec): One of LocalSource or RemoteSource must be specified.</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartspec">chartSpec</a></b></td>
        <td>object</td>
        <td>
          ChartSpec defines the desired state of the HelmChart to be created by the controller<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartRef
<sup><sup>[↩ Parent](#clustertemplatespechelm)</sup></sup>



ChartRef is a reference to a source controller resource containing the
Helm chart representing the template.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>kind</b></td>
        <td>enum</td>
        <td>
          Kind of the referent.<br/>
          <br/>
            <i>Enum</i>: OCIRepository, HelmChart<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>apiVersion</b></td>
        <td>string</td>
        <td>
          APIVersion of the referent.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace of the referent, defaults to the namespace of the Kubernetes
resource object that contains the reference.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource
<sup><sup>[↩ Parent](#clustertemplatespechelm)</sup></sup>



ChartSource is a source of a Helm chart representing the template.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>deploymentType</b></td>
        <td>enum</td>
        <td>
          DeploymentType is the type of the deployment. This field is ignored,
when ResourceSpec is used as part of Helm chart configuration.<br/>
          <br/>
            <i>Enum</i>: Local, Remote<br/>
            <i>Default</i>: Remote<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>path</b></td>
        <td>string</td>
        <td>
          Path to the directory containing the resource manifest.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourcelocalsourceref">localSourceRef</a></b></td>
        <td>object</td>
        <td>
          LocalSourceRef is the local source of the kustomize manifest.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespec">remoteSourceSpec</a></b></td>
        <td>object</td>
        <td>
          RemoteSourceSpec is the remote source of the kustomize manifest.<br/>
          <br/>
            <i>Validations</i>:<li>has(self.git) ? (!has(self.bucket) && !has(self.oci)) : true: Git, Bucket and OCI are mutually exclusive.</li><li>has(self.bucket) ? (!has(self.git) && !has(self.oci)) : true: Git, Bucket and OCI are mutually exclusive.</li><li>has(self.oci) ? (!has(self.git) && !has(self.bucket)) : true: Git, Bucket and OCI are mutually exclusive.</li><li>has(self.git) || has(self.bucket) || has(self.oci): One of Git, Bucket or OCI must be specified.</li>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.localSourceRef
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsource)</sup></sup>



LocalSourceRef is the local source of the kustomize manifest.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>kind</b></td>
        <td>enum</td>
        <td>
          Kind is the kind of the local source.<br/>
          <br/>
            <i>Enum</i>: ConfigMap, Secret, GitRepository, Bucket, OCIRepository<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name is the name of the local source.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace is the namespace of the local source. Cross-namespace references
are only allowed when the Kind is one of [github.com/fluxcd/source-controller/api/v1.GitRepository],
[github.com/fluxcd/source-controller/api/v1.Bucket] or [github.com/fluxcd/source-controller/api/v1beta2.OCIRepository].
If the Kind is ConfigMap or Secret, the namespace will be ignored.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsource)</sup></sup>



RemoteSourceSpec is the remote source of the kustomize manifest.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecbucket">bucket</a></b></td>
        <td>object</td>
        <td>
          Bucket is the definition of bucket source.<br/>
          <br/>
            <i>Validations</i>:<li>self.provider == 'aws' || self.provider == 'generic' || !has(self.sts): STS configuration is only supported for the 'aws' and 'generic' Bucket providers</li><li>self.provider != 'aws' || !has(self.sts) || self.sts.provider == 'aws': 'aws' is the only supported STS provider for the 'aws' Bucket provider</li><li>self.provider != 'generic' || !has(self.sts) || self.sts.provider == 'ldap': 'ldap' is the only supported STS provider for the 'generic' Bucket provider</li><li>!has(self.sts) || self.sts.provider != 'aws' || !has(self.sts.secretRef): spec.sts.secretRef is not required for the 'aws' STS provider</li><li>!has(self.sts) || self.sts.provider != 'aws' || !has(self.sts.certSecretRef): spec.sts.certSecretRef is not required for the 'aws' STS provider</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecgit">git</a></b></td>
        <td>object</td>
        <td>
          Git is the definition of git repository source.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecoci">oci</a></b></td>
        <td>object</td>
        <td>
          OCI is the definition of OCI repository source.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.bucket
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespec)</sup></sup>



Bucket is the definition of bucket source.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>bucketName</b></td>
        <td>string</td>
        <td>
          BucketName is the name of the object storage bucket.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>endpoint</b></td>
        <td>string</td>
        <td>
          Endpoint is the object storage address the BucketName is located at.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>interval</b></td>
        <td>string</td>
        <td>
          Interval at which the Bucket Endpoint is checked for updates.
This interval is approximate and may be subject to jitter to ensure
efficient use of resources.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecbucketcertsecretref">certSecretRef</a></b></td>
        <td>object</td>
        <td>
          CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
bucket. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

This field is only supported for the `generic` provider.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>ignore</b></td>
        <td>string</td>
        <td>
          Ignore overrides the set of excluded patterns in the .sourceignore format
(which is the same as .gitignore). If not provided, a default will be used,
consult the documentation for your version to find out what those are.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>insecure</b></td>
        <td>boolean</td>
        <td>
          Insecure allows connecting to a non-TLS HTTP Endpoint.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>prefix</b></td>
        <td>string</td>
        <td>
          Prefix to use for server-side filtering of files in the Bucket.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider of the object storage bucket.
Defaults to 'generic', which expects an S3 (API) compatible object
storage.<br/>
          <br/>
            <i>Enum</i>: generic, aws, gcp, azure<br/>
            <i>Default</i>: generic<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecbucketproxysecretref">proxySecretRef</a></b></td>
        <td>object</td>
        <td>
          ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the Bucket server.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>region</b></td>
        <td>string</td>
        <td>
          Region of the Endpoint where the BucketName is located in.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecbucketsecretref">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing authentication credentials
for the Bucket.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecbucketsts">sts</a></b></td>
        <td>object</td>
        <td>
          STS specifies the required configuration to use a Security Token
Service for fetching temporary credentials to authenticate in a
Bucket provider.

This field is only supported for the `aws` and `generic` providers.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>suspend</b></td>
        <td>boolean</td>
        <td>
          Suspend tells the controller to suspend the reconciliation of this
Bucket.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>timeout</b></td>
        <td>string</td>
        <td>
          Timeout for fetch operations, defaults to 60s.<br/>
          <br/>
            <i>Default</i>: 60s<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.bucket.certSecretRef
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespecbucket)</sup></sup>



CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
bucket. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

This field is only supported for the `generic` provider.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.bucket.proxySecretRef
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespecbucket)</sup></sup>



ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the Bucket server.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.bucket.secretRef
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespecbucket)</sup></sup>



SecretRef specifies the Secret containing authentication credentials
for the Bucket.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.bucket.sts
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespecbucket)</sup></sup>



STS specifies the required configuration to use a Security Token
Service for fetching temporary credentials to authenticate in a
Bucket provider.

This field is only supported for the `aws` and `generic` providers.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>endpoint</b></td>
        <td>string</td>
        <td>
          Endpoint is the HTTP/S endpoint of the Security Token Service from
where temporary credentials will be fetched.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider of the Security Token Service.<br/>
          <br/>
            <i>Enum</i>: aws, ldap<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecbucketstscertsecretref">certSecretRef</a></b></td>
        <td>object</td>
        <td>
          CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
STS endpoint. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

This field is only supported for the `ldap` provider.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecbucketstssecretref">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing authentication credentials
for the STS endpoint. This Secret must contain the fields `username`
and `password` and is supported only for the `ldap` provider.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.bucket.sts.certSecretRef
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespecbucketsts)</sup></sup>



CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
STS endpoint. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

This field is only supported for the `ldap` provider.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.bucket.sts.secretRef
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespecbucketsts)</sup></sup>



SecretRef specifies the Secret containing authentication credentials
for the STS endpoint. This Secret must contain the fields `username`
and `password` and is supported only for the `ldap` provider.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.git
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespec)</sup></sup>



Git is the definition of git repository source.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>interval</b></td>
        <td>string</td>
        <td>
          Interval at which the GitRepository URL is checked for updates.
This interval is approximate and may be subject to jitter to ensure
efficient use of resources.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>url</b></td>
        <td>string</td>
        <td>
          URL specifies the Git repository URL, it can be an HTTP/S or SSH address.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>ignore</b></td>
        <td>string</td>
        <td>
          Ignore overrides the set of excluded patterns in the .sourceignore format
(which is the same as .gitignore). If not provided, a default will be used,
consult the documentation for your version to find out what those are.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecgitincludeindex">include</a></b></td>
        <td>[]object</td>
        <td>
          Include specifies a list of GitRepository resources which Artifacts
should be included in the Artifact produced for this GitRepository.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider used for authentication, can be 'azure', 'github', 'generic'.
When not specified, defaults to 'generic'.<br/>
          <br/>
            <i>Enum</i>: generic, azure, github<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecgitproxysecretref">proxySecretRef</a></b></td>
        <td>object</td>
        <td>
          ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the Git server.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>recurseSubmodules</b></td>
        <td>boolean</td>
        <td>
          RecurseSubmodules enables the initialization of all submodules within
the GitRepository as cloned from the URL, using their default settings.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecgitref">ref</a></b></td>
        <td>object</td>
        <td>
          Reference specifies the Git reference to resolve and monitor for
changes, defaults to the 'master' branch.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecgitsecretref">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing authentication credentials for
the GitRepository.
For HTTPS repositories the Secret must contain 'username' and 'password'
fields for basic auth or 'bearerToken' field for token auth.
For SSH repositories the Secret must contain 'identity'
and 'known_hosts' fields.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>suspend</b></td>
        <td>boolean</td>
        <td>
          Suspend tells the controller to suspend the reconciliation of this
GitRepository.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>timeout</b></td>
        <td>string</td>
        <td>
          Timeout for Git operations like cloning, defaults to 60s.<br/>
          <br/>
            <i>Default</i>: 60s<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecgitverify">verify</a></b></td>
        <td>object</td>
        <td>
          Verification specifies the configuration to verify the Git commit
signature(s).<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.git.include[index]
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespecgit)</sup></sup>



GitRepositoryInclude specifies a local reference to a GitRepository which
Artifact (sub-)contents must be included, and where they should be placed.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecgitincludeindexrepository">repository</a></b></td>
        <td>object</td>
        <td>
          GitRepositoryRef specifies the GitRepository which Artifact contents
must be included.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>fromPath</b></td>
        <td>string</td>
        <td>
          FromPath specifies the path to copy contents from, defaults to the root
of the Artifact.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>toPath</b></td>
        <td>string</td>
        <td>
          ToPath specifies the path to copy contents to, defaults to the name of
the GitRepositoryRef.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.git.include[index].repository
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespecgitincludeindex)</sup></sup>



GitRepositoryRef specifies the GitRepository which Artifact contents
must be included.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.git.proxySecretRef
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespecgit)</sup></sup>



ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the Git server.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.git.ref
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespecgit)</sup></sup>



Reference specifies the Git reference to resolve and monitor for
changes, defaults to the 'master' branch.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>branch</b></td>
        <td>string</td>
        <td>
          Branch to check out, defaults to 'master' if no other field is defined.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>commit</b></td>
        <td>string</td>
        <td>
          Commit SHA to check out, takes precedence over all reference fields.

This can be combined with Branch to shallow clone the branch, in which
the commit is expected to exist.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the reference to check out; takes precedence over Branch, Tag and SemVer.

It must be a valid Git reference: https://git-scm.com/docs/git-check-ref-format#_description
Examples: "refs/heads/main", "refs/tags/v0.1.0", "refs/pull/420/head", "refs/merge-requests/1/head"<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>semver</b></td>
        <td>string</td>
        <td>
          SemVer tag expression to check out, takes precedence over Tag.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>tag</b></td>
        <td>string</td>
        <td>
          Tag to check out, takes precedence over Branch.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.git.secretRef
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespecgit)</sup></sup>



SecretRef specifies the Secret containing authentication credentials for
the GitRepository.
For HTTPS repositories the Secret must contain 'username' and 'password'
fields for basic auth or 'bearerToken' field for token auth.
For SSH repositories the Secret must contain 'identity'
and 'known_hosts' fields.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.git.verify
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespecgit)</sup></sup>



Verification specifies the configuration to verify the Git commit
signature(s).

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecgitverifysecretref">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing the public keys of trusted Git
authors.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>mode</b></td>
        <td>enum</td>
        <td>
          Mode specifies which Git object(s) should be verified.

The variants "head" and "HEAD" both imply the same thing, i.e. verify
the commit that the HEAD of the Git repository points to. The variant
"head" solely exists to ensure backwards compatibility.<br/>
          <br/>
            <i>Enum</i>: head, HEAD, Tag, TagAndHEAD<br/>
            <i>Default</i>: HEAD<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.git.verify.secretRef
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespecgitverify)</sup></sup>



SecretRef specifies the Secret containing the public keys of trusted Git
authors.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.oci
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespec)</sup></sup>



OCI is the definition of OCI repository source.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>interval</b></td>
        <td>string</td>
        <td>
          Interval at which the OCIRepository URL is checked for updates.
This interval is approximate and may be subject to jitter to ensure
efficient use of resources.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>url</b></td>
        <td>string</td>
        <td>
          URL is a reference to an OCI artifact repository hosted
on a remote container registry.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecocicertsecretref">certSecretRef</a></b></td>
        <td>object</td>
        <td>
          CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
registry. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

Note: Support for the `caFile`, `certFile` and `keyFile` keys have
been deprecated.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>ignore</b></td>
        <td>string</td>
        <td>
          Ignore overrides the set of excluded patterns in the .sourceignore format
(which is the same as .gitignore). If not provided, a default will be used,
consult the documentation for your version to find out what those are.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>insecure</b></td>
        <td>boolean</td>
        <td>
          Insecure allows connecting to a non-TLS HTTP container registry.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecocilayerselector">layerSelector</a></b></td>
        <td>object</td>
        <td>
          LayerSelector specifies which layer should be extracted from the OCI artifact.
When not specified, the first layer found in the artifact is selected.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          The provider used for authentication, can be 'aws', 'azure', 'gcp' or 'generic'.
When not specified, defaults to 'generic'.<br/>
          <br/>
            <i>Enum</i>: generic, aws, azure, gcp<br/>
            <i>Default</i>: generic<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecociproxysecretref">proxySecretRef</a></b></td>
        <td>object</td>
        <td>
          ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the container registry.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecociref">ref</a></b></td>
        <td>object</td>
        <td>
          The OCI reference to pull and monitor for changes,
defaults to the latest tag.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecocisecretref">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef contains the secret name containing the registry login
credentials to resolve image metadata.
The secret must be of type kubernetes.io/dockerconfigjson.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>serviceAccountName</b></td>
        <td>string</td>
        <td>
          ServiceAccountName is the name of the Kubernetes ServiceAccount used to authenticate
the image pull if the service account has attached pull secrets. For more information:
https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#add-imagepullsecrets-to-a-service-account<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>suspend</b></td>
        <td>boolean</td>
        <td>
          This flag tells the controller to suspend the reconciliation of this source.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>timeout</b></td>
        <td>string</td>
        <td>
          The timeout for remote OCI Repository operations like pulling, defaults to 60s.<br/>
          <br/>
            <i>Default</i>: 60s<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecociverify">verify</a></b></td>
        <td>object</td>
        <td>
          Verify contains the secret name containing the trusted public keys
used to verify the signature and specifies which provider to use to check
whether OCI image is authentic.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.oci.certSecretRef
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespecoci)</sup></sup>



CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
registry. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

Note: Support for the `caFile`, `certFile` and `keyFile` keys have
been deprecated.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.oci.layerSelector
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespecoci)</sup></sup>



LayerSelector specifies which layer should be extracted from the OCI artifact.
When not specified, the first layer found in the artifact is selected.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>mediaType</b></td>
        <td>string</td>
        <td>
          MediaType specifies the OCI media type of the layer
which should be extracted from the OCI Artifact. The
first layer matching this type is selected.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>operation</b></td>
        <td>enum</td>
        <td>
          Operation specifies how the selected layer should be processed.
By default, the layer compressed content is extracted to storage.
When the operation is set to 'copy', the layer compressed content
is persisted to storage as it is.<br/>
          <br/>
            <i>Enum</i>: extract, copy<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.oci.proxySecretRef
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespecoci)</sup></sup>



ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the container registry.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.oci.ref
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespecoci)</sup></sup>



The OCI reference to pull and monitor for changes,
defaults to the latest tag.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>digest</b></td>
        <td>string</td>
        <td>
          Digest is the image digest to pull, takes precedence over SemVer.
The value should be in the format 'sha256:<HASH>'.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>semver</b></td>
        <td>string</td>
        <td>
          SemVer is the range of tags to pull selecting the latest within
the range, takes precedence over Tag.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>semverFilter</b></td>
        <td>string</td>
        <td>
          SemverFilter is a regex pattern to filter the tags within the SemVer range.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>tag</b></td>
        <td>string</td>
        <td>
          Tag is the image tag to pull, defaults to latest.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.oci.secretRef
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespecoci)</sup></sup>



SecretRef contains the secret name containing the registry login
credentials to resolve image metadata.
The secret must be of type kubernetes.io/dockerconfigjson.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.oci.verify
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespecoci)</sup></sup>



Verify contains the secret name containing the trusted public keys
used to verify the signature and specifies which provider to use to check
whether OCI image is authentic.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider specifies the technology used to sign the OCI Artifact.<br/>
          <br/>
            <i>Enum</i>: cosign, notation<br/>
            <i>Default</i>: cosign<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecociverifymatchoidcidentityindex">matchOIDCIdentity</a></b></td>
        <td>[]object</td>
        <td>
          MatchOIDCIdentity specifies the identity matching criteria to use
while verifying an OCI artifact which was signed using Cosign keyless
signing. The artifact's identity is deemed to be verified if any of the
specified matchers match against the identity.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecociverifysecretref">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Kubernetes Secret containing the
trusted public keys.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.oci.verify.matchOIDCIdentity[index]
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespecociverify)</sup></sup>



OIDCIdentityMatch specifies options for verifying the certificate identity,
i.e. the issuer and the subject of the certificate.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>issuer</b></td>
        <td>string</td>
        <td>
          Issuer specifies the regex pattern to match against to verify
the OIDC issuer in the Fulcio certificate. The pattern must be a
valid Go regular expression.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>subject</b></td>
        <td>string</td>
        <td>
          Subject specifies the regex pattern to match against to verify
the identity subject in the Fulcio certificate. The pattern must
be a valid Go regular expression.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.oci.verify.secretRef
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespecociverify)</sup></sup>



SecretRef specifies the Kubernetes Secret containing the
trusted public keys.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSpec
<sup><sup>[↩ Parent](#clustertemplatespechelm)</sup></sup>



ChartSpec defines the desired state of the HelmChart to be created by the controller

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>chart</b></td>
        <td>string</td>
        <td>
          Chart is the name or path the Helm chart is available at in the
SourceRef.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>interval</b></td>
        <td>string</td>
        <td>
          Interval at which the HelmChart SourceRef is checked for updates.
This interval is approximate and may be subject to jitter to ensure
efficient use of resources.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartspecsourceref">sourceRef</a></b></td>
        <td>object</td>
        <td>
          SourceRef is the reference to the Source the chart is available at.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>ignoreMissingValuesFiles</b></td>
        <td>boolean</td>
        <td>
          IgnoreMissingValuesFiles controls whether to silently ignore missing values
files rather than failing.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>reconcileStrategy</b></td>
        <td>enum</td>
        <td>
          ReconcileStrategy determines what enables the creation of a new artifact.
Valid values are ('ChartVersion', 'Revision').
See the documentation of the values for an explanation on their behavior.
Defaults to ChartVersion when omitted.<br/>
          <br/>
            <i>Enum</i>: ChartVersion, Revision<br/>
            <i>Default</i>: ChartVersion<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>suspend</b></td>
        <td>boolean</td>
        <td>
          Suspend tells the controller to suspend the reconciliation of this
source.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>valuesFiles</b></td>
        <td>[]string</td>
        <td>
          ValuesFiles is an alternative list of values files to use as the chart
values (values.yaml is not included by default), expected to be a
relative path in the SourceRef.
Values files are merged in the order of this list with the last file
overriding the first. Ignored when omitted.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartspecverify">verify</a></b></td>
        <td>object</td>
        <td>
          Verify contains the secret name containing the trusted public keys
used to verify the signature and specifies which provider to use to check
whether OCI image is authentic.
This field is only supported when using HelmRepository source with spec.type 'oci'.
Chart dependencies, which are not bundled in the umbrella chart artifact, are not verified.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>version</b></td>
        <td>string</td>
        <td>
          Version is the chart version semver expression, ignored for charts from
GitRepository and Bucket sources. Defaults to latest when omitted.<br/>
          <br/>
            <i>Default</i>: *<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSpec.sourceRef
<sup><sup>[↩ Parent](#clustertemplatespechelmchartspec)</sup></sup>



SourceRef is the reference to the Source the chart is available at.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>kind</b></td>
        <td>enum</td>
        <td>
          Kind of the referent, valid values are ('HelmRepository', 'GitRepository',
'Bucket').<br/>
          <br/>
            <i>Enum</i>: HelmRepository, GitRepository, Bucket<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>apiVersion</b></td>
        <td>string</td>
        <td>
          APIVersion of the referent.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSpec.verify
<sup><sup>[↩ Parent](#clustertemplatespechelmchartspec)</sup></sup>



Verify contains the secret name containing the trusted public keys
used to verify the signature and specifies which provider to use to check
whether OCI image is authentic.
This field is only supported when using HelmRepository source with spec.type 'oci'.
Chart dependencies, which are not bundled in the umbrella chart artifact, are not verified.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider specifies the technology used to sign the OCI Artifact.<br/>
          <br/>
            <i>Enum</i>: cosign, notation<br/>
            <i>Default</i>: cosign<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartspecverifymatchoidcidentityindex">matchOIDCIdentity</a></b></td>
        <td>[]object</td>
        <td>
          MatchOIDCIdentity specifies the identity matching criteria to use
while verifying an OCI artifact which was signed using Cosign keyless
signing. The artifact's identity is deemed to be verified if any of the
specified matchers match against the identity.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartspecverifysecretref">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Kubernetes Secret containing the
trusted public keys.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSpec.verify.matchOIDCIdentity[index]
<sup><sup>[↩ Parent](#clustertemplatespechelmchartspecverify)</sup></sup>



OIDCIdentityMatch specifies options for verifying the certificate identity,
i.e. the issuer and the subject of the certificate.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>issuer</b></td>
        <td>string</td>
        <td>
          Issuer specifies the regex pattern to match against to verify
the OIDC issuer in the Fulcio certificate. The pattern must be a
valid Go regular expression.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>subject</b></td>
        <td>string</td>
        <td>
          Subject specifies the regex pattern to match against to verify
the identity subject in the Fulcio certificate. The pattern must
be a valid Go regular expression.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSpec.verify.secretRef
<sup><sup>[↩ Parent](#clustertemplatespechelmchartspecverify)</sup></sup>



SecretRef specifies the Kubernetes Secret containing the
trusted public keys.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ClusterTemplate.status
<sup><sup>[↩ Parent](#clustertemplate)</sup></sup>



ClusterTemplateStatus defines the observed state of ClusterTemplate

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>valid</b></td>
        <td>boolean</td>
        <td>
          Valid indicates whether the template passed validation or not.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#clustertemplatestatuschartref">chartRef</a></b></td>
        <td>object</td>
        <td>
          ChartRef is a reference to a source controller resource containing the
Helm chart representing the template.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>chartVersion</b></td>
        <td>string</td>
        <td>
          ChartVersion represents the version of the Helm Chart associated with this template.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>config</b></td>
        <td>JSON</td>
        <td>
          Config demonstrates available parameters for template customization,
that can be used when creating ClusterDeployment objects.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>description</b></td>
        <td>string</td>
        <td>
          Description contains information about the template.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>k8sVersion</b></td>
        <td>string</td>
        <td>
          Kubernetes exact version in the SemVer format provided by this ClusterTemplate.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>observedGeneration</b></td>
        <td>integer</td>
        <td>
          ObservedGeneration is the last observed generation.<br/>
          <br/>
            <i>Format</i>: int64<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>providerContracts</b></td>
        <td>map[string]string</td>
        <td>
          Holds key-value pairs with compatibility [contract versions],
where the key is the name of the provider,
and the value is the provider contract version
required to be supported by the provider.

[contract versions]: https://cluster-api.sigs.k8s.io/developer/providers/contracts<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>providers</b></td>
        <td>[]string</td>
        <td>
          Providers represent required CAPI providers.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>validationError</b></td>
        <td>string</td>
        <td>
          ValidationError provides information regarding issues encountered during template validation.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.status.chartRef
<sup><sup>[↩ Parent](#clustertemplatestatus)</sup></sup>



ChartRef is a reference to a source controller resource containing the
Helm chart representing the template.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>kind</b></td>
        <td>enum</td>
        <td>
          Kind of the referent.<br/>
          <br/>
            <i>Enum</i>: OCIRepository, HelmChart<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>apiVersion</b></td>
        <td>string</td>
        <td>
          APIVersion of the referent.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace of the referent, defaults to the namespace of the Kubernetes
resource object that contains the reference.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>

## Credential
<sup><sup>[↩ Parent](#k0rdentmirantiscomv1alpha1 )</sup></sup>






Credential is the Schema for the credentials API

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
      <td><b>apiVersion</b></td>
      <td>string</td>
      <td>k0rdent.mirantis.com/v1alpha1</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b>kind</b></td>
      <td>string</td>
      <td>Credential</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#credentialspec">spec</a></b></td>
        <td>object</td>
        <td>
          CredentialSpec defines the desired state of Credential<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#credentialstatus">status</a></b></td>
        <td>object</td>
        <td>
          CredentialStatus defines the observed state of Credential<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### Credential.spec
<sup><sup>[↩ Parent](#credential)</sup></sup>



CredentialSpec defines the desired state of Credential

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#credentialspecidentityref">identityRef</a></b></td>
        <td>object</td>
        <td>
          Reference to the Credential Identity<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>description</b></td>
        <td>string</td>
        <td>
          Description of the Credential object<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### Credential.spec.identityRef
<sup><sup>[↩ Parent](#credentialspec)</sup></sup>



Reference to the Credential Identity

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>apiVersion</b></td>
        <td>string</td>
        <td>
          API version of the referent.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>fieldPath</b></td>
        <td>string</td>
        <td>
          If referring to a piece of an object instead of an entire object, this string
should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2].
For example, if the object reference is to a container within a pod, this would take on a value like:
"spec.containers{name}" (where "name" refers to the name of the container that triggered
the event) or if no container name is specified "spec.containers[2]" (container with
index 2 in this pod). This syntax is chosen only to have some well-defined way of
referencing a part of an object.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>kind</b></td>
        <td>string</td>
        <td>
          Kind of the referent.
More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.
More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace of the referent.
More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>resourceVersion</b></td>
        <td>string</td>
        <td>
          Specific resourceVersion to which this reference is made, if any.
More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>uid</b></td>
        <td>string</td>
        <td>
          UID of the referent.
More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### Credential.status
<sup><sup>[↩ Parent](#credential)</sup></sup>



CredentialStatus defines the observed state of Credential

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>ready</b></td>
        <td>boolean</td>
        <td>
          Ready holds the readiness of Credentials.<br/>
          <br/>
            <i>Default</i>: false<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#credentialstatusconditionsindex">conditions</a></b></td>
        <td>[]object</td>
        <td>
          Conditions contains details for the current state of the Credential.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### Credential.status.conditions[index]
<sup><sup>[↩ Parent](#credentialstatus)</sup></sup>



Condition contains details for one aspect of the current state of this API Resource.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>lastTransitionTime</b></td>
        <td>string</td>
        <td>
          lastTransitionTime is the last time the condition transitioned from one status to another.
This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable.<br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>message</b></td>
        <td>string</td>
        <td>
          message is a human readable message indicating details about the transition.
This may be an empty string.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>reason</b></td>
        <td>string</td>
        <td>
          reason contains a programmatic identifier indicating the reason for the condition's last transition.
Producers of specific condition types may define expected values and meanings for this field,
and whether the values are considered a guaranteed API.
The value should be a CamelCase string.
This field may not be empty.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>status</b></td>
        <td>enum</td>
        <td>
          status of the condition, one of True, False, Unknown.<br/>
          <br/>
            <i>Enum</i>: True, False, Unknown<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>type</b></td>
        <td>string</td>
        <td>
          type of condition in CamelCase or in foo.example.com/CamelCase.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>observedGeneration</b></td>
        <td>integer</td>
        <td>
          observedGeneration represents the .metadata.generation that the condition was set based upon.
For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date
with respect to the current state of the instance.<br/>
          <br/>
            <i>Format</i>: int64<br/>
            <i>Minimum</i>: 0<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>

## ManagementBackup
<sup><sup>[↩ Parent](#k0rdentmirantiscomv1alpha1 )</sup></sup>






ManagementBackup is the Schema for the managementbackups API

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
      <td><b>apiVersion</b></td>
      <td>string</td>
      <td>k0rdent.mirantis.com/v1alpha1</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b>kind</b></td>
      <td>string</td>
      <td>ManagementBackup</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#managementbackupspec">spec</a></b></td>
        <td>object</td>
        <td>
          ManagementBackupSpec defines the desired state of ManagementBackup<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#managementbackupstatus">status</a></b></td>
        <td>object</td>
        <td>
          ManagementBackupStatus defines the observed state of ManagementBackup<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ManagementBackup.spec
<sup><sup>[↩ Parent](#managementbackup)</sup></sup>



ManagementBackupSpec defines the desired state of ManagementBackup

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>performOnManagementUpgrade</b></td>
        <td>boolean</td>
        <td>
          PerformOnManagementUpgrade indicates that a single [ManagementBackup]
should be created and stored in the [ManagementBackup] storage location if not default
before the [Management] release upgrade.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>schedule</b></td>
        <td>string</td>
        <td>
          Schedule is a Cron expression defining when to run the scheduled [ManagementBackup].
If not set, the object is considered to be run only once.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>storageLocation</b></td>
        <td>string</td>
        <td>
          StorageLocation is the name of a [github.com/vmware-tanzu/velero/pkg/apis/velero/v1.StorageLocation]
where the backup should be stored.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ManagementBackup.status
<sup><sup>[↩ Parent](#managementbackup)</sup></sup>



ManagementBackupStatus defines the observed state of ManagementBackup

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>error</b></td>
        <td>string</td>
        <td>
          Error stores messages in case of failed backup creation.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#managementbackupstatuslastbackup">lastBackup</a></b></td>
        <td>object</td>
        <td>
          Most recently [github.com/vmware-tanzu/velero/pkg/apis/velero/v1.Backup] that has been created.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>lastBackupName</b></td>
        <td>string</td>
        <td>
          Name of most recently created [github.com/vmware-tanzu/velero/pkg/apis/velero/v1.Backup].<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>lastBackupTime</b></td>
        <td>string</td>
        <td>
          Time of the most recently created [github.com/vmware-tanzu/velero/pkg/apis/velero/v1.Backup].<br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>nextAttempt</b></td>
        <td>string</td>
        <td>
          NextAttempt indicates the time when the next backup will be created.
Always absent for a single [ManagementBackup].<br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ManagementBackup.status.lastBackup
<sup><sup>[↩ Parent](#managementbackupstatus)</sup></sup>



Most recently [github.com/vmware-tanzu/velero/pkg/apis/velero/v1.Backup] that has been created.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>backupItemOperationsAttempted</b></td>
        <td>integer</td>
        <td>
          BackupItemOperationsAttempted is the total number of attempted
async BackupItemAction operations for this backup.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>backupItemOperationsCompleted</b></td>
        <td>integer</td>
        <td>
          BackupItemOperationsCompleted is the total number of successfully completed
async BackupItemAction operations for this backup.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>backupItemOperationsFailed</b></td>
        <td>integer</td>
        <td>
          BackupItemOperationsFailed is the total number of async
BackupItemAction operations for this backup which ended with an error.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>completionTimestamp</b></td>
        <td>string</td>
        <td>
          CompletionTimestamp records the time a backup was completed.
Completion time is recorded even on failed backups.
Completion time is recorded before uploading the backup object.
The server's time is used for CompletionTimestamps<br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>csiVolumeSnapshotsAttempted</b></td>
        <td>integer</td>
        <td>
          CSIVolumeSnapshotsAttempted is the total number of attempted
CSI VolumeSnapshots for this backup.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>csiVolumeSnapshotsCompleted</b></td>
        <td>integer</td>
        <td>
          CSIVolumeSnapshotsCompleted is the total number of successfully
completed CSI VolumeSnapshots for this backup.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>errors</b></td>
        <td>integer</td>
        <td>
          Errors is a count of all error messages that were generated during
execution of the backup.  The actual errors are in the backup's log
file in object storage.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>expiration</b></td>
        <td>string</td>
        <td>
          Expiration is when this Backup is eligible for garbage-collection.<br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>failureReason</b></td>
        <td>string</td>
        <td>
          FailureReason is an error that caused the entire backup to fail.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>formatVersion</b></td>
        <td>string</td>
        <td>
          FormatVersion is the backup format version, including major, minor, and patch version.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#managementbackupstatuslastbackuphookstatus">hookStatus</a></b></td>
        <td>object</td>
        <td>
          HookStatus contains information about the status of the hooks.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>phase</b></td>
        <td>enum</td>
        <td>
          Phase is the current state of the Backup.<br/>
          <br/>
            <i>Enum</i>: New, FailedValidation, InProgress, WaitingForPluginOperations, WaitingForPluginOperationsPartiallyFailed, Finalizing, FinalizingPartiallyFailed, Completed, PartiallyFailed, Failed, Deleting<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#managementbackupstatuslastbackupprogress">progress</a></b></td>
        <td>object</td>
        <td>
          Progress contains information about the backup's execution progress. Note
that this information is best-effort only -- if Velero fails to update it
during a backup for any reason, it may be inaccurate/stale.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>startTimestamp</b></td>
        <td>string</td>
        <td>
          StartTimestamp records the time a backup was started.
Separate from CreationTimestamp, since that value changes
on restores.
The server's time is used for StartTimestamps<br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>validationErrors</b></td>
        <td>[]string</td>
        <td>
          ValidationErrors is a slice of all validation errors (if
applicable).<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>version</b></td>
        <td>integer</td>
        <td>
          Version is the backup format major version.
Deprecated: Please see FormatVersion<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>volumeSnapshotsAttempted</b></td>
        <td>integer</td>
        <td>
          VolumeSnapshotsAttempted is the total number of attempted
volume snapshots for this backup.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>volumeSnapshotsCompleted</b></td>
        <td>integer</td>
        <td>
          VolumeSnapshotsCompleted is the total number of successfully
completed volume snapshots for this backup.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>warnings</b></td>
        <td>integer</td>
        <td>
          Warnings is a count of all warning messages that were generated during
execution of the backup. The actual warnings are in the backup's log
file in object storage.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ManagementBackup.status.lastBackup.hookStatus
<sup><sup>[↩ Parent](#managementbackupstatuslastbackup)</sup></sup>



HookStatus contains information about the status of the hooks.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>hooksAttempted</b></td>
        <td>integer</td>
        <td>
          HooksAttempted is the total number of attempted hooks
Specifically, HooksAttempted represents the number of hooks that failed to execute
and the number of hooks that executed successfully.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>hooksFailed</b></td>
        <td>integer</td>
        <td>
          HooksFailed is the total number of hooks which ended with an error<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ManagementBackup.status.lastBackup.progress
<sup><sup>[↩ Parent](#managementbackupstatuslastbackup)</sup></sup>



Progress contains information about the backup's execution progress. Note
that this information is best-effort only -- if Velero fails to update it
during a backup for any reason, it may be inaccurate/stale.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>itemsBackedUp</b></td>
        <td>integer</td>
        <td>
          ItemsBackedUp is the number of items that have actually been written to the
backup tarball so far.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>totalItems</b></td>
        <td>integer</td>
        <td>
          TotalItems is the total number of items to be backed up. This number may change
throughout the execution of the backup due to plugins that return additional related
items to back up, the velero.io/exclude-from-backup label, and various other
filters that happen as items are processed.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>

## Management
<sup><sup>[↩ Parent](#k0rdentmirantiscomv1alpha1 )</sup></sup>






Management is the Schema for the managements API

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
      <td><b>apiVersion</b></td>
      <td>string</td>
      <td>k0rdent.mirantis.com/v1alpha1</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b>kind</b></td>
      <td>string</td>
      <td>Management</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#managementspec">spec</a></b></td>
        <td>object</td>
        <td>
          ManagementSpec defines the desired state of Management<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#managementstatus">status</a></b></td>
        <td>object</td>
        <td>
          ManagementStatus defines the observed state of Management<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### Management.spec
<sup><sup>[↩ Parent](#management)</sup></sup>



ManagementSpec defines the desired state of Management

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>release</b></td>
        <td>string</td>
        <td>
          Release references the Release object.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#managementspeccore">core</a></b></td>
        <td>object</td>
        <td>
          Core holds the core Management components that are mandatory.
If not specified, will be populated with the default values.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#managementspecprovidersindex">providers</a></b></td>
        <td>[]object</td>
        <td>
          Providers is the list of supported CAPI providers.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### Management.spec.core
<sup><sup>[↩ Parent](#managementspec)</sup></sup>



Core holds the core Management components that are mandatory.
If not specified, will be populated with the default values.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#managementspeccorecapi">capi</a></b></td>
        <td>object</td>
        <td>
          CAPI represents the core Cluster API component and references the Cluster API template.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#managementspeccorekcm">kcm</a></b></td>
        <td>object</td>
        <td>
          KCM represents the core KCM component and references the KCM template.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### Management.spec.core.capi
<sup><sup>[↩ Parent](#managementspeccore)</sup></sup>



CAPI represents the core Cluster API component and references the Cluster API template.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>config</b></td>
        <td>JSON</td>
        <td>
          Config allows to provide parameters for management component customization.
If no Config provided, the field will be populated with the default
values for the template.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>template</b></td>
        <td>string</td>
        <td>
          Template is the name of the Template associated with this component.
If not specified, will be taken from the Release object.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### Management.spec.core.kcm
<sup><sup>[↩ Parent](#managementspeccore)</sup></sup>



KCM represents the core KCM component and references the KCM template.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>config</b></td>
        <td>JSON</td>
        <td>
          Config allows to provide parameters for management component customization.
If no Config provided, the field will be populated with the default
values for the template.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>template</b></td>
        <td>string</td>
        <td>
          Template is the name of the Template associated with this component.
If not specified, will be taken from the Release object.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### Management.spec.providers[index]
<sup><sup>[↩ Parent](#managementspec)</sup></sup>





<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the provider.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>config</b></td>
        <td>JSON</td>
        <td>
          Config allows to provide parameters for management component customization.
If no Config provided, the field will be populated with the default
values for the template.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>template</b></td>
        <td>string</td>
        <td>
          Template is the name of the Template associated with this component.
If not specified, will be taken from the Release object.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### Management.status
<sup><sup>[↩ Parent](#management)</sup></sup>



ManagementStatus defines the observed state of Management

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>availableProviders</b></td>
        <td>[]string</td>
        <td>
          AvailableProviders holds all available CAPI providers.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>backupName</b></td>
        <td>string</td>
        <td>
          BackupName is a name of the management cluster scheduled backup.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>capiContracts</b></td>
        <td>map[string]map[string]string</td>
        <td>
          For each CAPI provider name holds its compatibility [contract versions]
in a key-value pairs, where the key is the core CAPI contract version,
and the value is an underscore-delimited (_) list of provider contract versions
supported by the core CAPI.

[contract versions]: https://cluster-api.sigs.k8s.io/developer/providers/contracts<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#managementstatuscomponentskey">components</a></b></td>
        <td>map[string]object</td>
        <td>
          Components indicates the status of installed KCM components and CAPI providers.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#managementstatusconditionsindex">conditions</a></b></td>
        <td>[]object</td>
        <td>
          Conditions represents the observations of a Management's current state.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>observedGeneration</b></td>
        <td>integer</td>
        <td>
          ObservedGeneration is the last observed generation.<br/>
          <br/>
            <i>Format</i>: int64<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>release</b></td>
        <td>string</td>
        <td>
          Release indicates the current Release object.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### Management.status.components[key]
<sup><sup>[↩ Parent](#managementstatus)</sup></sup>



ComponentStatus is the status of Management component installation

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>error</b></td>
        <td>string</td>
        <td>
          Error stores as error message in case of failed installation<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>exposedProviders</b></td>
        <td>[]string</td>
        <td>
          ExposedProviders is a list of CAPI providers this component exposes<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>success</b></td>
        <td>boolean</td>
        <td>
          Success represents if a component installation was successful<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>template</b></td>
        <td>string</td>
        <td>
          Template is the name of the Template associated with this component.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### Management.status.conditions[index]
<sup><sup>[↩ Parent](#managementstatus)</sup></sup>



Condition contains details for one aspect of the current state of this API Resource.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>lastTransitionTime</b></td>
        <td>string</td>
        <td>
          lastTransitionTime is the last time the condition transitioned from one status to another.
This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable.<br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>message</b></td>
        <td>string</td>
        <td>
          message is a human readable message indicating details about the transition.
This may be an empty string.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>reason</b></td>
        <td>string</td>
        <td>
          reason contains a programmatic identifier indicating the reason for the condition's last transition.
Producers of specific condition types may define expected values and meanings for this field,
and whether the values are considered a guaranteed API.
The value should be a CamelCase string.
This field may not be empty.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>status</b></td>
        <td>enum</td>
        <td>
          status of the condition, one of True, False, Unknown.<br/>
          <br/>
            <i>Enum</i>: True, False, Unknown<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>type</b></td>
        <td>string</td>
        <td>
          type of condition in CamelCase or in foo.example.com/CamelCase.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>observedGeneration</b></td>
        <td>integer</td>
        <td>
          observedGeneration represents the .metadata.generation that the condition was set based upon.
For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date
with respect to the current state of the instance.<br/>
          <br/>
            <i>Format</i>: int64<br/>
            <i>Minimum</i>: 0<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>

## MultiClusterService
<sup><sup>[↩ Parent](#k0rdentmirantiscomv1alpha1 )</sup></sup>






MultiClusterService is the Schema for the multiclusterservices API

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
      <td><b>apiVersion</b></td>
      <td>string</td>
      <td>k0rdent.mirantis.com/v1alpha1</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b>kind</b></td>
      <td>string</td>
      <td>MultiClusterService</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#multiclusterservicespec">spec</a></b></td>
        <td>object</td>
        <td>
          MultiClusterServiceSpec defines the desired state of MultiClusterService<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#multiclusterservicestatus">status</a></b></td>
        <td>object</td>
        <td>
          MultiClusterServiceStatus defines the observed state of MultiClusterService.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.spec
<sup><sup>[↩ Parent](#multiclusterservice)</sup></sup>



MultiClusterServiceSpec defines the desired state of MultiClusterService

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#multiclusterservicespecclusterselector">clusterSelector</a></b></td>
        <td>object</td>
        <td>
          ClusterSelector identifies target clusters to manage services on.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#multiclusterservicespecservicespec">serviceSpec</a></b></td>
        <td>object</td>
        <td>
          ServiceSpec is spec related to deployment of services.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.spec.clusterSelector
<sup><sup>[↩ Parent](#multiclusterservicespec)</sup></sup>



ClusterSelector identifies target clusters to manage services on.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#multiclusterservicespecclusterselectormatchexpressionsindex">matchExpressions</a></b></td>
        <td>[]object</td>
        <td>
          matchExpressions is a list of label selector requirements. The requirements are ANDed.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>matchLabels</b></td>
        <td>map[string]string</td>
        <td>
          matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels
map is equivalent to an element of matchExpressions, whose key field is "key", the
operator is "In", and the values array contains only "value". The requirements are ANDed.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.spec.clusterSelector.matchExpressions[index]
<sup><sup>[↩ Parent](#multiclusterservicespecclusterselector)</sup></sup>



A label selector requirement is a selector that contains values, a key, and an operator that
relates the key and values.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>key</b></td>
        <td>string</td>
        <td>
          key is the label key that the selector applies to.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>operator</b></td>
        <td>string</td>
        <td>
          operator represents a key's relationship to a set of values.
Valid operators are In, NotIn, Exists and DoesNotExist.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>values</b></td>
        <td>[]string</td>
        <td>
          values is an array of string values. If the operator is In or NotIn,
the values array must be non-empty. If the operator is Exists or DoesNotExist,
the values array must be empty. This array is replaced during a strategic
merge patch.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.spec.serviceSpec
<sup><sup>[↩ Parent](#multiclusterservicespec)</sup></sup>



ServiceSpec is spec related to deployment of services.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>continueOnError</b></td>
        <td>boolean</td>
        <td>
          ContinueOnError specifies if the services deployment should continue if an error occurs.<br/>
          <br/>
            <i>Default</i>: false<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#multiclusterservicespecservicespecdriftexclusionsindex">driftExclusions</a></b></td>
        <td>[]object</td>
        <td>
          DriftExclusions specifies specific configurations of resources to ignore for drift detection.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#multiclusterservicespecservicespecdriftignoreindex">driftIgnore</a></b></td>
        <td>[]object</td>
        <td>
          DriftIgnore specifies resources to ignore for drift detection.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>priority</b></td>
        <td>integer</td>
        <td>
          Priority sets the priority for the services defined in this spec.
Higher value means higher priority and lower means lower.
In case of conflict with another object managing the service,
the one with higher priority will get to deploy its services.<br/>
          <br/>
            <i>Format</i>: int32<br/>
            <i>Default</i>: 100<br/>
            <i>Minimum</i>: 1<br/>
            <i>Maximum</i>: 2.147483646e+09<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>reload</b></td>
        <td>boolean</td>
        <td>
          Reload instances via rolling upgrade when a ConfigMap/Secret mounted as volume is modified.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#multiclusterservicespecservicespecservicesindex">services</a></b></td>
        <td>[]object</td>
        <td>
          Services is a list of services created via ServiceTemplates
that could be installed on the target cluster.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>stopOnConflict</b></td>
        <td>boolean</td>
        <td>
          StopOnConflict specifies what to do in case of a conflict.
E.g. If another object is already managing a service.
By default the remaining services will be deployed even if conflict is detected.
If set to true, the deployment will stop after encountering the first conflict.<br/>
          <br/>
            <i>Default</i>: false<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>syncMode</b></td>
        <td>enum</td>
        <td>
          SyncMode specifies how services are synced in the target cluster.<br/>
          <br/>
            <i>Enum</i>: OneTime, Continuous, ContinuousWithDriftDetection, DryRun<br/>
            <i>Default</i>: Continuous<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#multiclusterservicespecservicespectemplateresourcerefsindex">templateResourceRefs</a></b></td>
        <td>[]object</td>
        <td>
          TemplateResourceRefs is a list of resources to collect from the management cluster,
the values from which can be used in templates.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.spec.serviceSpec.driftExclusions[index]
<sup><sup>[↩ Parent](#multiclusterservicespecservicespec)</sup></sup>





<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>paths</b></td>
        <td>[]string</td>
        <td>
          Paths is a slice of JSON6902 paths to exclude from configuration drift evaluation.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#multiclusterservicespecservicespecdriftexclusionsindextarget">target</a></b></td>
        <td>object</td>
        <td>
          Target points to the resources that the paths refers to.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.spec.serviceSpec.driftExclusions[index].target
<sup><sup>[↩ Parent](#multiclusterservicespecservicespecdriftexclusionsindex)</sup></sup>



Target points to the resources that the paths refers to.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>annotationSelector</b></td>
        <td>string</td>
        <td>
          AnnotationSelector is a string that follows the label selection expression
https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#api
It matches with the resource annotations.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>group</b></td>
        <td>string</td>
        <td>
          Group is the API group to select resources from.
Together with Version and Kind it is capable of unambiguously identifying and/or selecting resources.
https://github.com/kubernetes/community/blob/master/contributors/design-proposals/api-machinery/api-group.md<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>kind</b></td>
        <td>string</td>
        <td>
          Kind of the API Group to select resources from.
Together with Group and Version it is capable of unambiguously
identifying and/or selecting resources.
https://github.com/kubernetes/community/blob/master/contributors/design-proposals/api-machinery/api-group.md<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>labelSelector</b></td>
        <td>string</td>
        <td>
          LabelSelector is a string that follows the label selection expression
https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#api
It matches with the resource labels.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name to match resources with.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace to select resources from.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>version</b></td>
        <td>string</td>
        <td>
          Version of the API Group to select resources from.
Together with Group and Kind it is capable of unambiguously identifying and/or selecting resources.
https://github.com/kubernetes/community/blob/master/contributors/design-proposals/api-machinery/api-group.md<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.spec.serviceSpec.driftIgnore[index]
<sup><sup>[↩ Parent](#multiclusterservicespecservicespec)</sup></sup>





<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>annotationSelector</b></td>
        <td>string</td>
        <td>
          AnnotationSelector is a string that follows the label selection expression
https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#api
It matches with the resource annotations.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>group</b></td>
        <td>string</td>
        <td>
          Group is the API group to select resources from.
Together with Version and Kind it is capable of unambiguously identifying and/or selecting resources.
https://github.com/kubernetes/community/blob/master/contributors/design-proposals/api-machinery/api-group.md<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>kind</b></td>
        <td>string</td>
        <td>
          Kind of the API Group to select resources from.
Together with Group and Version it is capable of unambiguously
identifying and/or selecting resources.
https://github.com/kubernetes/community/blob/master/contributors/design-proposals/api-machinery/api-group.md<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>labelSelector</b></td>
        <td>string</td>
        <td>
          LabelSelector is a string that follows the label selection expression
https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#api
It matches with the resource labels.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name to match resources with.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace to select resources from.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>version</b></td>
        <td>string</td>
        <td>
          Version of the API Group to select resources from.
Together with Group and Kind it is capable of unambiguously identifying and/or selecting resources.
https://github.com/kubernetes/community/blob/master/contributors/design-proposals/api-machinery/api-group.md<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.spec.serviceSpec.services[index]
<sup><sup>[↩ Parent](#multiclusterservicespecservicespec)</sup></sup>



Service represents a Service to be deployed.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name is the chart release.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>template</b></td>
        <td>string</td>
        <td>
          Template is a reference to a Template object located in the same namespace.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>disable</b></td>
        <td>boolean</td>
        <td>
          Disable can be set to disable handling of this service.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace is the namespace the release will be installed in.
It will default to Name if not provided.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>templateChain</b></td>
        <td>string</td>
        <td>
          TemplateChain defines the ServiceTemplateChain object that will be used to deploy the service
along with desired ServiceTemplate version.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>values</b></td>
        <td>string</td>
        <td>
          Values is the helm values to be passed to the chart used by the template.
The string type is used in order to allow for templating.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#multiclusterservicespecservicespecservicesindexvaluesfromindex">valuesFrom</a></b></td>
        <td>[]object</td>
        <td>
          ValuesFrom can reference a ConfigMap or Secret containing helm values.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.spec.serviceSpec.services[index].valuesFrom[index]
<sup><sup>[↩ Parent](#multiclusterservicespecservicespecservicesindex)</sup></sup>





<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>kind</b></td>
        <td>enum</td>
        <td>
          Kind of the resource. Supported kinds are:
- ConfigMap/Secret<br/>
          <br/>
            <i>Enum</i>: ConfigMap, Secret<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referenced resource.
Name can be expressed as a template and instantiate using any cluster field.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace of the referenced resource.
For ClusterProfile namespace can be left empty. In such a case, namespace will
be implicit set to cluster's namespace.
For Profile namespace must be left empty. The Profile namespace will be used.
Namespace can be expressed as a template and instantiate using any cluster field.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>optional</b></td>
        <td>boolean</td>
        <td>
          Optional indicates that the referenced resource is not mandatory.
If set to true and the resource is not found, the error will be ignored,
and Sveltos will continue processing other ValueFroms.<br/>
          <br/>
            <i>Default</i>: false<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.spec.serviceSpec.templateResourceRefs[index]
<sup><sup>[↩ Parent](#multiclusterservicespecservicespec)</sup></sup>





<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>identifier</b></td>
        <td>string</td>
        <td>
          Identifier is how the resource will be referred to in the
template<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#multiclusterservicespecservicespectemplateresourcerefsindexresource">resource</a></b></td>
        <td>object</td>
        <td>
          Resource references a Kubernetes instance in the management
cluster to fetch and use during template instantiation.
For ClusterProfile namespace can be left empty. In such a case, namespace will
be implicit set to cluster's namespace.
Name and namespace can be expressed as a template and instantiate using any cluster field.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>optional</b></td>
        <td>boolean</td>
        <td>
          Optional indicates that the referenced resource is not mandatory.
If set to true and the resource is not found, the error will be ignored,
and Sveltos will continue processing other TemplateResourceRefs.<br/>
          <br/>
            <i>Default</i>: false<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.spec.serviceSpec.templateResourceRefs[index].resource
<sup><sup>[↩ Parent](#multiclusterservicespecservicespectemplateresourcerefsindex)</sup></sup>



Resource references a Kubernetes instance in the management
cluster to fetch and use during template instantiation.
For ClusterProfile namespace can be left empty. In such a case, namespace will
be implicit set to cluster's namespace.
Name and namespace can be expressed as a template and instantiate using any cluster field.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>apiVersion</b></td>
        <td>string</td>
        <td>
          API version of the referent.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>fieldPath</b></td>
        <td>string</td>
        <td>
          If referring to a piece of an object instead of an entire object, this string
should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2].
For example, if the object reference is to a container within a pod, this would take on a value like:
"spec.containers{name}" (where "name" refers to the name of the container that triggered
the event) or if no container name is specified "spec.containers[2]" (container with
index 2 in this pod). This syntax is chosen only to have some well-defined way of
referencing a part of an object.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>kind</b></td>
        <td>string</td>
        <td>
          Kind of the referent.
More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.
More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace of the referent.
More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>resourceVersion</b></td>
        <td>string</td>
        <td>
          Specific resourceVersion to which this reference is made, if any.
More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>uid</b></td>
        <td>string</td>
        <td>
          UID of the referent.
More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.status
<sup><sup>[↩ Parent](#multiclusterservice)</sup></sup>



MultiClusterServiceStatus defines the observed state of MultiClusterService.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#multiclusterservicestatusconditionsindex">conditions</a></b></td>
        <td>[]object</td>
        <td>
          Conditions contains details for the current state of the MultiClusterService.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>observedGeneration</b></td>
        <td>integer</td>
        <td>
          ObservedGeneration is the last observed generation.<br/>
          <br/>
            <i>Format</i>: int64<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#multiclusterservicestatusservicesindex">services</a></b></td>
        <td>[]object</td>
        <td>
          Services contains details for the state of services.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#multiclusterservicestatusservicesupgradepathsindex">servicesUpgradePaths</a></b></td>
        <td>[]object</td>
        <td>
          ServicesUpgradePaths contains details for the state of services upgrade paths.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.status.conditions[index]
<sup><sup>[↩ Parent](#multiclusterservicestatus)</sup></sup>



Condition contains details for one aspect of the current state of this API Resource.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>lastTransitionTime</b></td>
        <td>string</td>
        <td>
          lastTransitionTime is the last time the condition transitioned from one status to another.
This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable.<br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>message</b></td>
        <td>string</td>
        <td>
          message is a human readable message indicating details about the transition.
This may be an empty string.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>reason</b></td>
        <td>string</td>
        <td>
          reason contains a programmatic identifier indicating the reason for the condition's last transition.
Producers of specific condition types may define expected values and meanings for this field,
and whether the values are considered a guaranteed API.
The value should be a CamelCase string.
This field may not be empty.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>status</b></td>
        <td>enum</td>
        <td>
          status of the condition, one of True, False, Unknown.<br/>
          <br/>
            <i>Enum</i>: True, False, Unknown<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>type</b></td>
        <td>string</td>
        <td>
          type of condition in CamelCase or in foo.example.com/CamelCase.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>observedGeneration</b></td>
        <td>integer</td>
        <td>
          observedGeneration represents the .metadata.generation that the condition was set based upon.
For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date
with respect to the current state of the instance.<br/>
          <br/>
            <i>Format</i>: int64<br/>
            <i>Minimum</i>: 0<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.status.services[index]
<sup><sup>[↩ Parent](#multiclusterservicestatus)</sup></sup>



ServiceStatus contains details for the state of services.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>clusterName</b></td>
        <td>string</td>
        <td>
          ClusterName is the name of the associated cluster.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>clusterNamespace</b></td>
        <td>string</td>
        <td>
          ClusterNamespace is the namespace of the associated cluster.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#multiclusterservicestatusservicesindexconditionsindex">conditions</a></b></td>
        <td>[]object</td>
        <td>
          Conditions contains details for the current state of managed services.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.status.services[index].conditions[index]
<sup><sup>[↩ Parent](#multiclusterservicestatusservicesindex)</sup></sup>



Condition contains details for one aspect of the current state of this API Resource.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>lastTransitionTime</b></td>
        <td>string</td>
        <td>
          lastTransitionTime is the last time the condition transitioned from one status to another.
This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable.<br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>message</b></td>
        <td>string</td>
        <td>
          message is a human readable message indicating details about the transition.
This may be an empty string.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>reason</b></td>
        <td>string</td>
        <td>
          reason contains a programmatic identifier indicating the reason for the condition's last transition.
Producers of specific condition types may define expected values and meanings for this field,
and whether the values are considered a guaranteed API.
The value should be a CamelCase string.
This field may not be empty.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>status</b></td>
        <td>enum</td>
        <td>
          status of the condition, one of True, False, Unknown.<br/>
          <br/>
            <i>Enum</i>: True, False, Unknown<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>type</b></td>
        <td>string</td>
        <td>
          type of condition in CamelCase or in foo.example.com/CamelCase.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>observedGeneration</b></td>
        <td>integer</td>
        <td>
          observedGeneration represents the .metadata.generation that the condition was set based upon.
For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date
with respect to the current state of the instance.<br/>
          <br/>
            <i>Format</i>: int64<br/>
            <i>Minimum</i>: 0<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.status.servicesUpgradePaths[index]
<sup><sup>[↩ Parent](#multiclusterservicestatus)</sup></sup>



ServiceUpgradePaths contains details for the state of service upgrade paths.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name is the name of the service.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace is the namespace of the service.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>template</b></td>
        <td>string</td>
        <td>
          Template is the name of the current service template.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#multiclusterservicestatusservicesupgradepathsindexavailableupgradesindex">availableUpgrades</a></b></td>
        <td>[]object</td>
        <td>
          AvailableUpgrades contains details for the state of available upgrades.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.status.servicesUpgradePaths[index].availableUpgrades[index]
<sup><sup>[↩ Parent](#multiclusterservicestatusservicesupgradepathsindex)</sup></sup>



UpgradePath contains details for the state of service upgrade paths.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>upgradePaths</b></td>
        <td>[]string</td>
        <td>
          Versions contains the list of versions that service can be upgraded to.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>

## ProviderInterface
<sup><sup>[↩ Parent](#k0rdentmirantiscomv1alpha1 )</sup></sup>






ProviderInterface is the Schema for the ProviderInterface API

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
      <td><b>apiVersion</b></td>
      <td>string</td>
      <td>k0rdent.mirantis.com/v1alpha1</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b>kind</b></td>
      <td>string</td>
      <td>ProviderInterface</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#providerinterfacespec">spec</a></b></td>
        <td>object</td>
        <td>
          ProviderInterfaceSpec defines the desired state of ProviderInterface<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providerinterfacestatus">status</a></b></td>
        <td>object</td>
        <td>
          ProviderInterfaceStatus defines the observed state of ProviderInterface<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderInterface.spec
<sup><sup>[↩ Parent](#providerinterface)</sup></sup>



ProviderInterfaceSpec defines the desired state of ProviderInterface

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#providerinterfacespecclustergvksindex">clusterGVKs</a></b></td>
        <td>[]object</td>
        <td>
          ClusterGVKs defines the Group-Version-Kind resources this provider can manage<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>clusterIdentityKinds</b></td>
        <td>[]string</td>
        <td>
          ClusterIdentityKinds defines the Kind of identity objects supported by this provider<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>description</b></td>
        <td>string</td>
        <td>
          Description provides a human-readable explanation of what this provider does<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderInterface.spec.clusterGVKs[index]
<sup><sup>[↩ Parent](#providerinterfacespec)</sup></sup>



GroupVersionKind unambiguously identifies a kind. It doesn't anonymously include GroupVersion
to avoid automatic coercion. It doesn't use a GroupVersion to avoid custom marshalling
Note: mirror of https://github.com/kubernetes/apimachinery/blob/v0.32.3/pkg/runtime/schema/group_version.go#L140-L146

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>group</b></td>
        <td>string</td>
        <td>
          <br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>kind</b></td>
        <td>string</td>
        <td>
          <br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>version</b></td>
        <td>string</td>
        <td>
          <br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ProviderInterface.status
<sup><sup>[↩ Parent](#providerinterface)</sup></sup>



ProviderInterfaceStatus defines the observed state of ProviderInterface

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>exposedProviders</b></td>
        <td>string</td>
        <td>
          ExposedProviders contains the list of exposed provider<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>

## ProviderTemplate
<sup><sup>[↩ Parent](#k0rdentmirantiscomv1alpha1 )</sup></sup>






ProviderTemplate is the Schema for the providertemplates API

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
      <td><b>apiVersion</b></td>
      <td>string</td>
      <td>k0rdent.mirantis.com/v1alpha1</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b>kind</b></td>
      <td>string</td>
      <td>ProviderTemplate</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#providertemplatespec">spec</a></b></td>
        <td>object</td>
        <td>
          ProviderTemplateSpec defines the desired state of ProviderTemplate<br/>
          <br/>
            <i>Validations</i>:<li>self == oldSelf: Spec is immutable</li><li>!has(self.helm.chartSource): .spec.helm.chartSource is not supported for ProviderTemplates</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatestatus">status</a></b></td>
        <td>object</td>
        <td>
          ProviderTemplateStatus defines the observed state of ProviderTemplate<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec
<sup><sup>[↩ Parent](#providertemplate)</sup></sup>



ProviderTemplateSpec defines the desired state of ProviderTemplate

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>capiContracts</b></td>
        <td>map[string]string</td>
        <td>
          Holds key-value pairs with compatibility [contract versions],
where the key is the core CAPI contract version,
and the value is an underscore-delimited (_) list of provider contract versions
supported by the core CAPI.

[contract versions]: https://cluster-api.sigs.k8s.io/developer/providers/contracts<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelm">helm</a></b></td>
        <td>object</td>
        <td>
          HelmSpec references a Helm chart representing the KCM template<br/>
          <br/>
            <i>Validations</i>:<li>(has(self.chartSpec) ? (!has(self.chartSource) && !has(self.chartRef)): true): chartSpec, chartSource and chartRef are mutually exclusive</li><li>(has(self.chartSource) ? (!has(self.chartSpec) && !has(self.chartRef)): true): chartSpec, chartSource and chartRef are mutually exclusive</li><li>(has(self.chartRef) ? (!has(self.chartSpec) && !has(self.chartSource)): true): chartSpec, chartSource and chartRef are mutually exclusive</li><li>has(self.chartSpec) || has(self.chartRef) || has(self.chartSource): one of chartSpec, chartRef or chartSource must be set</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>providers</b></td>
        <td>[]string</td>
        <td>
          Providers represent exposed CAPI providers.
Should be set if not present in the Helm chart metadata.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm
<sup><sup>[↩ Parent](#providertemplatespec)</sup></sup>



HelmSpec references a Helm chart representing the KCM template

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#providertemplatespechelmchartref">chartRef</a></b></td>
        <td>object</td>
        <td>
          ChartRef is a reference to a source controller resource containing the
Helm chart representing the template.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsource">chartSource</a></b></td>
        <td>object</td>
        <td>
          ChartSource is a source of a Helm chart representing the template.<br/>
          <br/>
            <i>Validations</i>:<li>has(self.localSourceRef) ? (self.localSourceRef.kind != 'Secret' && self.localSourceRef.kind != 'ConfigMap'): true: Secret and ConfigMap are not supported as Helm chart sources</li><li>has(self.localSourceRef) ? !has(self.remoteSourceSpec): true: LocalSource and RemoteSource are mutually exclusive.</li><li>has(self.remoteSourceSpec) ? !has(self.localSourceRef): true: LocalSource and RemoteSource are mutually exclusive.</li><li>has(self.localSourceRef) || has(self.remoteSourceSpec): One of LocalSource or RemoteSource must be specified.</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartspec">chartSpec</a></b></td>
        <td>object</td>
        <td>
          ChartSpec defines the desired state of the HelmChart to be created by the controller<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartRef
<sup><sup>[↩ Parent](#providertemplatespechelm)</sup></sup>



ChartRef is a reference to a source controller resource containing the
Helm chart representing the template.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>kind</b></td>
        <td>enum</td>
        <td>
          Kind of the referent.<br/>
          <br/>
            <i>Enum</i>: OCIRepository, HelmChart<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>apiVersion</b></td>
        <td>string</td>
        <td>
          APIVersion of the referent.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace of the referent, defaults to the namespace of the Kubernetes
resource object that contains the reference.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource
<sup><sup>[↩ Parent](#providertemplatespechelm)</sup></sup>



ChartSource is a source of a Helm chart representing the template.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>deploymentType</b></td>
        <td>enum</td>
        <td>
          DeploymentType is the type of the deployment. This field is ignored,
when ResourceSpec is used as part of Helm chart configuration.<br/>
          <br/>
            <i>Enum</i>: Local, Remote<br/>
            <i>Default</i>: Remote<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>path</b></td>
        <td>string</td>
        <td>
          Path to the directory containing the resource manifest.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourcelocalsourceref">localSourceRef</a></b></td>
        <td>object</td>
        <td>
          LocalSourceRef is the local source of the kustomize manifest.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespec">remoteSourceSpec</a></b></td>
        <td>object</td>
        <td>
          RemoteSourceSpec is the remote source of the kustomize manifest.<br/>
          <br/>
            <i>Validations</i>:<li>has(self.git) ? (!has(self.bucket) && !has(self.oci)) : true: Git, Bucket and OCI are mutually exclusive.</li><li>has(self.bucket) ? (!has(self.git) && !has(self.oci)) : true: Git, Bucket and OCI are mutually exclusive.</li><li>has(self.oci) ? (!has(self.git) && !has(self.bucket)) : true: Git, Bucket and OCI are mutually exclusive.</li><li>has(self.git) || has(self.bucket) || has(self.oci): One of Git, Bucket or OCI must be specified.</li>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.localSourceRef
<sup><sup>[↩ Parent](#providertemplatespechelmchartsource)</sup></sup>



LocalSourceRef is the local source of the kustomize manifest.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>kind</b></td>
        <td>enum</td>
        <td>
          Kind is the kind of the local source.<br/>
          <br/>
            <i>Enum</i>: ConfigMap, Secret, GitRepository, Bucket, OCIRepository<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name is the name of the local source.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace is the namespace of the local source. Cross-namespace references
are only allowed when the Kind is one of [github.com/fluxcd/source-controller/api/v1.GitRepository],
[github.com/fluxcd/source-controller/api/v1.Bucket] or [github.com/fluxcd/source-controller/api/v1beta2.OCIRepository].
If the Kind is ConfigMap or Secret, the namespace will be ignored.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec
<sup><sup>[↩ Parent](#providertemplatespechelmchartsource)</sup></sup>



RemoteSourceSpec is the remote source of the kustomize manifest.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecbucket">bucket</a></b></td>
        <td>object</td>
        <td>
          Bucket is the definition of bucket source.<br/>
          <br/>
            <i>Validations</i>:<li>self.provider == 'aws' || self.provider == 'generic' || !has(self.sts): STS configuration is only supported for the 'aws' and 'generic' Bucket providers</li><li>self.provider != 'aws' || !has(self.sts) || self.sts.provider == 'aws': 'aws' is the only supported STS provider for the 'aws' Bucket provider</li><li>self.provider != 'generic' || !has(self.sts) || self.sts.provider == 'ldap': 'ldap' is the only supported STS provider for the 'generic' Bucket provider</li><li>!has(self.sts) || self.sts.provider != 'aws' || !has(self.sts.secretRef): spec.sts.secretRef is not required for the 'aws' STS provider</li><li>!has(self.sts) || self.sts.provider != 'aws' || !has(self.sts.certSecretRef): spec.sts.certSecretRef is not required for the 'aws' STS provider</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecgit">git</a></b></td>
        <td>object</td>
        <td>
          Git is the definition of git repository source.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecoci">oci</a></b></td>
        <td>object</td>
        <td>
          OCI is the definition of OCI repository source.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.bucket
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespec)</sup></sup>



Bucket is the definition of bucket source.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>bucketName</b></td>
        <td>string</td>
        <td>
          BucketName is the name of the object storage bucket.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>endpoint</b></td>
        <td>string</td>
        <td>
          Endpoint is the object storage address the BucketName is located at.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>interval</b></td>
        <td>string</td>
        <td>
          Interval at which the Bucket Endpoint is checked for updates.
This interval is approximate and may be subject to jitter to ensure
efficient use of resources.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecbucketcertsecretref">certSecretRef</a></b></td>
        <td>object</td>
        <td>
          CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
bucket. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

This field is only supported for the `generic` provider.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>ignore</b></td>
        <td>string</td>
        <td>
          Ignore overrides the set of excluded patterns in the .sourceignore format
(which is the same as .gitignore). If not provided, a default will be used,
consult the documentation for your version to find out what those are.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>insecure</b></td>
        <td>boolean</td>
        <td>
          Insecure allows connecting to a non-TLS HTTP Endpoint.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>prefix</b></td>
        <td>string</td>
        <td>
          Prefix to use for server-side filtering of files in the Bucket.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider of the object storage bucket.
Defaults to 'generic', which expects an S3 (API) compatible object
storage.<br/>
          <br/>
            <i>Enum</i>: generic, aws, gcp, azure<br/>
            <i>Default</i>: generic<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecbucketproxysecretref">proxySecretRef</a></b></td>
        <td>object</td>
        <td>
          ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the Bucket server.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>region</b></td>
        <td>string</td>
        <td>
          Region of the Endpoint where the BucketName is located in.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecbucketsecretref">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing authentication credentials
for the Bucket.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecbucketsts">sts</a></b></td>
        <td>object</td>
        <td>
          STS specifies the required configuration to use a Security Token
Service for fetching temporary credentials to authenticate in a
Bucket provider.

This field is only supported for the `aws` and `generic` providers.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>suspend</b></td>
        <td>boolean</td>
        <td>
          Suspend tells the controller to suspend the reconciliation of this
Bucket.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>timeout</b></td>
        <td>string</td>
        <td>
          Timeout for fetch operations, defaults to 60s.<br/>
          <br/>
            <i>Default</i>: 60s<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.bucket.certSecretRef
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespecbucket)</sup></sup>



CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
bucket. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

This field is only supported for the `generic` provider.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.bucket.proxySecretRef
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespecbucket)</sup></sup>



ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the Bucket server.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.bucket.secretRef
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespecbucket)</sup></sup>



SecretRef specifies the Secret containing authentication credentials
for the Bucket.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.bucket.sts
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespecbucket)</sup></sup>



STS specifies the required configuration to use a Security Token
Service for fetching temporary credentials to authenticate in a
Bucket provider.

This field is only supported for the `aws` and `generic` providers.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>endpoint</b></td>
        <td>string</td>
        <td>
          Endpoint is the HTTP/S endpoint of the Security Token Service from
where temporary credentials will be fetched.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider of the Security Token Service.<br/>
          <br/>
            <i>Enum</i>: aws, ldap<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecbucketstscertsecretref">certSecretRef</a></b></td>
        <td>object</td>
        <td>
          CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
STS endpoint. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

This field is only supported for the `ldap` provider.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecbucketstssecretref">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing authentication credentials
for the STS endpoint. This Secret must contain the fields `username`
and `password` and is supported only for the `ldap` provider.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.bucket.sts.certSecretRef
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespecbucketsts)</sup></sup>



CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
STS endpoint. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

This field is only supported for the `ldap` provider.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.bucket.sts.secretRef
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespecbucketsts)</sup></sup>



SecretRef specifies the Secret containing authentication credentials
for the STS endpoint. This Secret must contain the fields `username`
and `password` and is supported only for the `ldap` provider.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.git
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespec)</sup></sup>



Git is the definition of git repository source.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>interval</b></td>
        <td>string</td>
        <td>
          Interval at which the GitRepository URL is checked for updates.
This interval is approximate and may be subject to jitter to ensure
efficient use of resources.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>url</b></td>
        <td>string</td>
        <td>
          URL specifies the Git repository URL, it can be an HTTP/S or SSH address.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>ignore</b></td>
        <td>string</td>
        <td>
          Ignore overrides the set of excluded patterns in the .sourceignore format
(which is the same as .gitignore). If not provided, a default will be used,
consult the documentation for your version to find out what those are.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecgitincludeindex">include</a></b></td>
        <td>[]object</td>
        <td>
          Include specifies a list of GitRepository resources which Artifacts
should be included in the Artifact produced for this GitRepository.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider used for authentication, can be 'azure', 'github', 'generic'.
When not specified, defaults to 'generic'.<br/>
          <br/>
            <i>Enum</i>: generic, azure, github<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecgitproxysecretref">proxySecretRef</a></b></td>
        <td>object</td>
        <td>
          ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the Git server.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>recurseSubmodules</b></td>
        <td>boolean</td>
        <td>
          RecurseSubmodules enables the initialization of all submodules within
the GitRepository as cloned from the URL, using their default settings.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecgitref">ref</a></b></td>
        <td>object</td>
        <td>
          Reference specifies the Git reference to resolve and monitor for
changes, defaults to the 'master' branch.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecgitsecretref">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing authentication credentials for
the GitRepository.
For HTTPS repositories the Secret must contain 'username' and 'password'
fields for basic auth or 'bearerToken' field for token auth.
For SSH repositories the Secret must contain 'identity'
and 'known_hosts' fields.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>suspend</b></td>
        <td>boolean</td>
        <td>
          Suspend tells the controller to suspend the reconciliation of this
GitRepository.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>timeout</b></td>
        <td>string</td>
        <td>
          Timeout for Git operations like cloning, defaults to 60s.<br/>
          <br/>
            <i>Default</i>: 60s<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecgitverify">verify</a></b></td>
        <td>object</td>
        <td>
          Verification specifies the configuration to verify the Git commit
signature(s).<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.git.include[index]
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespecgit)</sup></sup>



GitRepositoryInclude specifies a local reference to a GitRepository which
Artifact (sub-)contents must be included, and where they should be placed.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecgitincludeindexrepository">repository</a></b></td>
        <td>object</td>
        <td>
          GitRepositoryRef specifies the GitRepository which Artifact contents
must be included.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>fromPath</b></td>
        <td>string</td>
        <td>
          FromPath specifies the path to copy contents from, defaults to the root
of the Artifact.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>toPath</b></td>
        <td>string</td>
        <td>
          ToPath specifies the path to copy contents to, defaults to the name of
the GitRepositoryRef.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.git.include[index].repository
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespecgitincludeindex)</sup></sup>



GitRepositoryRef specifies the GitRepository which Artifact contents
must be included.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.git.proxySecretRef
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespecgit)</sup></sup>



ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the Git server.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.git.ref
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespecgit)</sup></sup>



Reference specifies the Git reference to resolve and monitor for
changes, defaults to the 'master' branch.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>branch</b></td>
        <td>string</td>
        <td>
          Branch to check out, defaults to 'master' if no other field is defined.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>commit</b></td>
        <td>string</td>
        <td>
          Commit SHA to check out, takes precedence over all reference fields.

This can be combined with Branch to shallow clone the branch, in which
the commit is expected to exist.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the reference to check out; takes precedence over Branch, Tag and SemVer.

It must be a valid Git reference: https://git-scm.com/docs/git-check-ref-format#_description
Examples: "refs/heads/main", "refs/tags/v0.1.0", "refs/pull/420/head", "refs/merge-requests/1/head"<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>semver</b></td>
        <td>string</td>
        <td>
          SemVer tag expression to check out, takes precedence over Tag.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>tag</b></td>
        <td>string</td>
        <td>
          Tag to check out, takes precedence over Branch.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.git.secretRef
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespecgit)</sup></sup>



SecretRef specifies the Secret containing authentication credentials for
the GitRepository.
For HTTPS repositories the Secret must contain 'username' and 'password'
fields for basic auth or 'bearerToken' field for token auth.
For SSH repositories the Secret must contain 'identity'
and 'known_hosts' fields.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.git.verify
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespecgit)</sup></sup>



Verification specifies the configuration to verify the Git commit
signature(s).

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecgitverifysecretref">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing the public keys of trusted Git
authors.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>mode</b></td>
        <td>enum</td>
        <td>
          Mode specifies which Git object(s) should be verified.

The variants "head" and "HEAD" both imply the same thing, i.e. verify
the commit that the HEAD of the Git repository points to. The variant
"head" solely exists to ensure backwards compatibility.<br/>
          <br/>
            <i>Enum</i>: head, HEAD, Tag, TagAndHEAD<br/>
            <i>Default</i>: HEAD<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.git.verify.secretRef
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespecgitverify)</sup></sup>



SecretRef specifies the Secret containing the public keys of trusted Git
authors.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.oci
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespec)</sup></sup>



OCI is the definition of OCI repository source.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>interval</b></td>
        <td>string</td>
        <td>
          Interval at which the OCIRepository URL is checked for updates.
This interval is approximate and may be subject to jitter to ensure
efficient use of resources.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>url</b></td>
        <td>string</td>
        <td>
          URL is a reference to an OCI artifact repository hosted
on a remote container registry.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecocicertsecretref">certSecretRef</a></b></td>
        <td>object</td>
        <td>
          CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
registry. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

Note: Support for the `caFile`, `certFile` and `keyFile` keys have
been deprecated.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>ignore</b></td>
        <td>string</td>
        <td>
          Ignore overrides the set of excluded patterns in the .sourceignore format
(which is the same as .gitignore). If not provided, a default will be used,
consult the documentation for your version to find out what those are.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>insecure</b></td>
        <td>boolean</td>
        <td>
          Insecure allows connecting to a non-TLS HTTP container registry.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecocilayerselector">layerSelector</a></b></td>
        <td>object</td>
        <td>
          LayerSelector specifies which layer should be extracted from the OCI artifact.
When not specified, the first layer found in the artifact is selected.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          The provider used for authentication, can be 'aws', 'azure', 'gcp' or 'generic'.
When not specified, defaults to 'generic'.<br/>
          <br/>
            <i>Enum</i>: generic, aws, azure, gcp<br/>
            <i>Default</i>: generic<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecociproxysecretref">proxySecretRef</a></b></td>
        <td>object</td>
        <td>
          ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the container registry.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecociref">ref</a></b></td>
        <td>object</td>
        <td>
          The OCI reference to pull and monitor for changes,
defaults to the latest tag.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecocisecretref">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef contains the secret name containing the registry login
credentials to resolve image metadata.
The secret must be of type kubernetes.io/dockerconfigjson.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>serviceAccountName</b></td>
        <td>string</td>
        <td>
          ServiceAccountName is the name of the Kubernetes ServiceAccount used to authenticate
the image pull if the service account has attached pull secrets. For more information:
https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#add-imagepullsecrets-to-a-service-account<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>suspend</b></td>
        <td>boolean</td>
        <td>
          This flag tells the controller to suspend the reconciliation of this source.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>timeout</b></td>
        <td>string</td>
        <td>
          The timeout for remote OCI Repository operations like pulling, defaults to 60s.<br/>
          <br/>
            <i>Default</i>: 60s<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecociverify">verify</a></b></td>
        <td>object</td>
        <td>
          Verify contains the secret name containing the trusted public keys
used to verify the signature and specifies which provider to use to check
whether OCI image is authentic.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.oci.certSecretRef
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespecoci)</sup></sup>



CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
registry. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

Note: Support for the `caFile`, `certFile` and `keyFile` keys have
been deprecated.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.oci.layerSelector
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespecoci)</sup></sup>



LayerSelector specifies which layer should be extracted from the OCI artifact.
When not specified, the first layer found in the artifact is selected.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>mediaType</b></td>
        <td>string</td>
        <td>
          MediaType specifies the OCI media type of the layer
which should be extracted from the OCI Artifact. The
first layer matching this type is selected.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>operation</b></td>
        <td>enum</td>
        <td>
          Operation specifies how the selected layer should be processed.
By default, the layer compressed content is extracted to storage.
When the operation is set to 'copy', the layer compressed content
is persisted to storage as it is.<br/>
          <br/>
            <i>Enum</i>: extract, copy<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.oci.proxySecretRef
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespecoci)</sup></sup>



ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the container registry.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.oci.ref
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespecoci)</sup></sup>



The OCI reference to pull and monitor for changes,
defaults to the latest tag.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>digest</b></td>
        <td>string</td>
        <td>
          Digest is the image digest to pull, takes precedence over SemVer.
The value should be in the format 'sha256:<HASH>'.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>semver</b></td>
        <td>string</td>
        <td>
          SemVer is the range of tags to pull selecting the latest within
the range, takes precedence over Tag.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>semverFilter</b></td>
        <td>string</td>
        <td>
          SemverFilter is a regex pattern to filter the tags within the SemVer range.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>tag</b></td>
        <td>string</td>
        <td>
          Tag is the image tag to pull, defaults to latest.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.oci.secretRef
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespecoci)</sup></sup>



SecretRef contains the secret name containing the registry login
credentials to resolve image metadata.
The secret must be of type kubernetes.io/dockerconfigjson.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.oci.verify
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespecoci)</sup></sup>



Verify contains the secret name containing the trusted public keys
used to verify the signature and specifies which provider to use to check
whether OCI image is authentic.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider specifies the technology used to sign the OCI Artifact.<br/>
          <br/>
            <i>Enum</i>: cosign, notation<br/>
            <i>Default</i>: cosign<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecociverifymatchoidcidentityindex">matchOIDCIdentity</a></b></td>
        <td>[]object</td>
        <td>
          MatchOIDCIdentity specifies the identity matching criteria to use
while verifying an OCI artifact which was signed using Cosign keyless
signing. The artifact's identity is deemed to be verified if any of the
specified matchers match against the identity.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecociverifysecretref">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Kubernetes Secret containing the
trusted public keys.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.oci.verify.matchOIDCIdentity[index]
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespecociverify)</sup></sup>



OIDCIdentityMatch specifies options for verifying the certificate identity,
i.e. the issuer and the subject of the certificate.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>issuer</b></td>
        <td>string</td>
        <td>
          Issuer specifies the regex pattern to match against to verify
the OIDC issuer in the Fulcio certificate. The pattern must be a
valid Go regular expression.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>subject</b></td>
        <td>string</td>
        <td>
          Subject specifies the regex pattern to match against to verify
the identity subject in the Fulcio certificate. The pattern must
be a valid Go regular expression.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.oci.verify.secretRef
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespecociverify)</sup></sup>



SecretRef specifies the Kubernetes Secret containing the
trusted public keys.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSpec
<sup><sup>[↩ Parent](#providertemplatespechelm)</sup></sup>



ChartSpec defines the desired state of the HelmChart to be created by the controller

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>chart</b></td>
        <td>string</td>
        <td>
          Chart is the name or path the Helm chart is available at in the
SourceRef.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>interval</b></td>
        <td>string</td>
        <td>
          Interval at which the HelmChart SourceRef is checked for updates.
This interval is approximate and may be subject to jitter to ensure
efficient use of resources.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartspecsourceref">sourceRef</a></b></td>
        <td>object</td>
        <td>
          SourceRef is the reference to the Source the chart is available at.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>ignoreMissingValuesFiles</b></td>
        <td>boolean</td>
        <td>
          IgnoreMissingValuesFiles controls whether to silently ignore missing values
files rather than failing.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>reconcileStrategy</b></td>
        <td>enum</td>
        <td>
          ReconcileStrategy determines what enables the creation of a new artifact.
Valid values are ('ChartVersion', 'Revision').
See the documentation of the values for an explanation on their behavior.
Defaults to ChartVersion when omitted.<br/>
          <br/>
            <i>Enum</i>: ChartVersion, Revision<br/>
            <i>Default</i>: ChartVersion<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>suspend</b></td>
        <td>boolean</td>
        <td>
          Suspend tells the controller to suspend the reconciliation of this
source.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>valuesFiles</b></td>
        <td>[]string</td>
        <td>
          ValuesFiles is an alternative list of values files to use as the chart
values (values.yaml is not included by default), expected to be a
relative path in the SourceRef.
Values files are merged in the order of this list with the last file
overriding the first. Ignored when omitted.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartspecverify">verify</a></b></td>
        <td>object</td>
        <td>
          Verify contains the secret name containing the trusted public keys
used to verify the signature and specifies which provider to use to check
whether OCI image is authentic.
This field is only supported when using HelmRepository source with spec.type 'oci'.
Chart dependencies, which are not bundled in the umbrella chart artifact, are not verified.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>version</b></td>
        <td>string</td>
        <td>
          Version is the chart version semver expression, ignored for charts from
GitRepository and Bucket sources. Defaults to latest when omitted.<br/>
          <br/>
            <i>Default</i>: *<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSpec.sourceRef
<sup><sup>[↩ Parent](#providertemplatespechelmchartspec)</sup></sup>



SourceRef is the reference to the Source the chart is available at.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>kind</b></td>
        <td>enum</td>
        <td>
          Kind of the referent, valid values are ('HelmRepository', 'GitRepository',
'Bucket').<br/>
          <br/>
            <i>Enum</i>: HelmRepository, GitRepository, Bucket<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>apiVersion</b></td>
        <td>string</td>
        <td>
          APIVersion of the referent.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSpec.verify
<sup><sup>[↩ Parent](#providertemplatespechelmchartspec)</sup></sup>



Verify contains the secret name containing the trusted public keys
used to verify the signature and specifies which provider to use to check
whether OCI image is authentic.
This field is only supported when using HelmRepository source with spec.type 'oci'.
Chart dependencies, which are not bundled in the umbrella chart artifact, are not verified.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider specifies the technology used to sign the OCI Artifact.<br/>
          <br/>
            <i>Enum</i>: cosign, notation<br/>
            <i>Default</i>: cosign<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartspecverifymatchoidcidentityindex">matchOIDCIdentity</a></b></td>
        <td>[]object</td>
        <td>
          MatchOIDCIdentity specifies the identity matching criteria to use
while verifying an OCI artifact which was signed using Cosign keyless
signing. The artifact's identity is deemed to be verified if any of the
specified matchers match against the identity.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartspecverifysecretref">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Kubernetes Secret containing the
trusted public keys.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSpec.verify.matchOIDCIdentity[index]
<sup><sup>[↩ Parent](#providertemplatespechelmchartspecverify)</sup></sup>



OIDCIdentityMatch specifies options for verifying the certificate identity,
i.e. the issuer and the subject of the certificate.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>issuer</b></td>
        <td>string</td>
        <td>
          Issuer specifies the regex pattern to match against to verify
the OIDC issuer in the Fulcio certificate. The pattern must be a
valid Go regular expression.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>subject</b></td>
        <td>string</td>
        <td>
          Subject specifies the regex pattern to match against to verify
the identity subject in the Fulcio certificate. The pattern must
be a valid Go regular expression.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSpec.verify.secretRef
<sup><sup>[↩ Parent](#providertemplatespechelmchartspecverify)</sup></sup>



SecretRef specifies the Kubernetes Secret containing the
trusted public keys.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ProviderTemplate.status
<sup><sup>[↩ Parent](#providertemplate)</sup></sup>



ProviderTemplateStatus defines the observed state of ProviderTemplate

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>valid</b></td>
        <td>boolean</td>
        <td>
          Valid indicates whether the template passed validation or not.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>capiContracts</b></td>
        <td>map[string]string</td>
        <td>
          Holds key-value pairs with compatibility [contract versions],
where the key is the core CAPI contract version,
and the value is an underscore-delimited (_) list of provider contract versions
supported by the core CAPI.

[contract versions]: https://cluster-api.sigs.k8s.io/developer/providers/contracts<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatestatuschartref">chartRef</a></b></td>
        <td>object</td>
        <td>
          ChartRef is a reference to a source controller resource containing the
Helm chart representing the template.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>chartVersion</b></td>
        <td>string</td>
        <td>
          ChartVersion represents the version of the Helm Chart associated with this template.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>config</b></td>
        <td>JSON</td>
        <td>
          Config demonstrates available parameters for template customization,
that can be used when creating ClusterDeployment objects.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>description</b></td>
        <td>string</td>
        <td>
          Description contains information about the template.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>observedGeneration</b></td>
        <td>integer</td>
        <td>
          ObservedGeneration is the last observed generation.<br/>
          <br/>
            <i>Format</i>: int64<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>providers</b></td>
        <td>[]string</td>
        <td>
          Providers represent exposed CAPI providers.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>validationError</b></td>
        <td>string</td>
        <td>
          ValidationError provides information regarding issues encountered during template validation.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.status.chartRef
<sup><sup>[↩ Parent](#providertemplatestatus)</sup></sup>



ChartRef is a reference to a source controller resource containing the
Helm chart representing the template.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>kind</b></td>
        <td>enum</td>
        <td>
          Kind of the referent.<br/>
          <br/>
            <i>Enum</i>: OCIRepository, HelmChart<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>apiVersion</b></td>
        <td>string</td>
        <td>
          APIVersion of the referent.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace of the referent, defaults to the namespace of the Kubernetes
resource object that contains the reference.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>

## Release
<sup><sup>[↩ Parent](#k0rdentmirantiscomv1alpha1 )</sup></sup>






Release is the Schema for the releases API

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
      <td><b>apiVersion</b></td>
      <td>string</td>
      <td>k0rdent.mirantis.com/v1alpha1</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b>kind</b></td>
      <td>string</td>
      <td>Release</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#releasespec">spec</a></b></td>
        <td>object</td>
        <td>
          ReleaseSpec defines the desired state of Release<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#releasestatus">status</a></b></td>
        <td>object</td>
        <td>
          ReleaseStatus defines the observed state of Release<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### Release.spec
<sup><sup>[↩ Parent](#release)</sup></sup>



ReleaseSpec defines the desired state of Release

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#releasespeccapi">capi</a></b></td>
        <td>object</td>
        <td>
          CAPI references the Cluster API template.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#releasespeckcm">kcm</a></b></td>
        <td>object</td>
        <td>
          KCM references the KCM template.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>version</b></td>
        <td>string</td>
        <td>
          Version of the KCM Release in the semver format.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#releasespecprovidersindex">providers</a></b></td>
        <td>[]object</td>
        <td>
          Providers contains a list of Providers associated with the Release.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### Release.spec.capi
<sup><sup>[↩ Parent](#releasespec)</sup></sup>



CAPI references the Cluster API template.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>template</b></td>
        <td>string</td>
        <td>
          Template references the Template associated with the provider.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### Release.spec.kcm
<sup><sup>[↩ Parent](#releasespec)</sup></sup>



KCM references the KCM template.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>template</b></td>
        <td>string</td>
        <td>
          Template references the Template associated with the provider.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### Release.spec.providers[index]
<sup><sup>[↩ Parent](#releasespec)</sup></sup>





<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the provider.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>template</b></td>
        <td>string</td>
        <td>
          Template references the Template associated with the provider.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### Release.status
<sup><sup>[↩ Parent](#release)</sup></sup>



ReleaseStatus defines the observed state of Release

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#releasestatusconditionsindex">conditions</a></b></td>
        <td>[]object</td>
        <td>
          Conditions contains details for the current state of the Release<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>observedGeneration</b></td>
        <td>integer</td>
        <td>
          ObservedGeneration is the last observed generation.<br/>
          <br/>
            <i>Format</i>: int64<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>ready</b></td>
        <td>boolean</td>
        <td>
          Ready indicates whether KCM is ready to be upgraded to this Release.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### Release.status.conditions[index]
<sup><sup>[↩ Parent](#releasestatus)</sup></sup>



Condition contains details for one aspect of the current state of this API Resource.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>lastTransitionTime</b></td>
        <td>string</td>
        <td>
          lastTransitionTime is the last time the condition transitioned from one status to another.
This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable.<br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>message</b></td>
        <td>string</td>
        <td>
          message is a human readable message indicating details about the transition.
This may be an empty string.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>reason</b></td>
        <td>string</td>
        <td>
          reason contains a programmatic identifier indicating the reason for the condition's last transition.
Producers of specific condition types may define expected values and meanings for this field,
and whether the values are considered a guaranteed API.
The value should be a CamelCase string.
This field may not be empty.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>status</b></td>
        <td>enum</td>
        <td>
          status of the condition, one of True, False, Unknown.<br/>
          <br/>
            <i>Enum</i>: True, False, Unknown<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>type</b></td>
        <td>string</td>
        <td>
          type of condition in CamelCase or in foo.example.com/CamelCase.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>observedGeneration</b></td>
        <td>integer</td>
        <td>
          observedGeneration represents the .metadata.generation that the condition was set based upon.
For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date
with respect to the current state of the instance.<br/>
          <br/>
            <i>Format</i>: int64<br/>
            <i>Minimum</i>: 0<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>

## ServiceTemplateChain
<sup><sup>[↩ Parent](#k0rdentmirantiscomv1alpha1 )</sup></sup>






ServiceTemplateChain is the Schema for the servicetemplatechains API

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
      <td><b>apiVersion</b></td>
      <td>string</td>
      <td>k0rdent.mirantis.com/v1alpha1</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b>kind</b></td>
      <td>string</td>
      <td>ServiceTemplateChain</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#servicetemplatechainspec">spec</a></b></td>
        <td>object</td>
        <td>
          TemplateChainSpec defines the desired state of *TemplateChain<br/>
          <br/>
            <i>Validations</i>:<li>self == oldSelf: Spec is immutable</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatechainstatus">status</a></b></td>
        <td>object</td>
        <td>
          TemplateChainStatus defines the observed state of *TemplateChain<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplateChain.spec
<sup><sup>[↩ Parent](#servicetemplatechain)</sup></sup>



TemplateChainSpec defines the desired state of *TemplateChain

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#servicetemplatechainspecsupportedtemplatesindex">supportedTemplates</a></b></td>
        <td>[]object</td>
        <td>
          SupportedTemplates is the list of supported Templates definitions and all available upgrade sequences for it.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplateChain.spec.supportedTemplates[index]
<sup><sup>[↩ Parent](#servicetemplatechainspec)</sup></sup>



SupportedTemplate is the supported Template definition and all available upgrade sequences for it

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name is the name of the Template.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#servicetemplatechainspecsupportedtemplatesindexavailableupgradesindex">availableUpgrades</a></b></td>
        <td>[]object</td>
        <td>
          AvailableUpgrades is the list of available upgrades for the specified Template.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplateChain.spec.supportedTemplates[index].availableUpgrades[index]
<sup><sup>[↩ Parent](#servicetemplatechainspecsupportedtemplatesindex)</sup></sup>



AvailableUpgrade is the definition of the available upgrade for the Template

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name is the name of the Template to which the upgrade is available.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplateChain.status
<sup><sup>[↩ Parent](#servicetemplatechain)</sup></sup>



TemplateChainStatus defines the observed state of *TemplateChain

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>valid</b></td>
        <td>boolean</td>
        <td>
          Valid indicates whether the chain is valid and can be considered when calculating available
upgrade paths.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>validationError</b></td>
        <td>string</td>
        <td>
          ValidationError provides information regarding issues encountered during templatechain validation.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>

## ServiceTemplate
<sup><sup>[↩ Parent](#k0rdentmirantiscomv1alpha1 )</sup></sup>






ServiceTemplate is the Schema for the servicetemplates API

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
      <td><b>apiVersion</b></td>
      <td>string</td>
      <td>k0rdent.mirantis.com/v1alpha1</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b>kind</b></td>
      <td>string</td>
      <td>ServiceTemplate</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespec">spec</a></b></td>
        <td>object</td>
        <td>
          ServiceTemplateSpec defines the desired state of ServiceTemplate<br/>
          <br/>
            <i>Validations</i>:<li>self == oldSelf: Spec is immutable</li><li>has(self.helm) ? (!has(self.kustomize) && !has(self.resources)): true: Helm, Kustomize and Resources are mutually exclusive.</li><li>has(self.kustomize) ? (!has(self.helm) && !has(self.resources)): true: Helm, Kustomize and Resources are mutually exclusive.</li><li>has(self.resources) ? (!has(self.kustomize) && !has(self.helm)): true: Helm, Kustomize and Resources are mutually exclusive.</li><li>has(self.helm) || has(self.kustomize) || has(self.resources): One of Helm, Kustomize, or Resources must be specified.</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatestatus">status</a></b></td>
        <td>object</td>
        <td>
          ServiceTemplateStatus defines the observed state of ServiceTemplate<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec
<sup><sup>[↩ Parent](#servicetemplate)</sup></sup>



ServiceTemplateSpec defines the desired state of ServiceTemplate

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#servicetemplatespechelm">helm</a></b></td>
        <td>object</td>
        <td>
          Helm contains the Helm chart information for the template.<br/>
          <br/>
            <i>Validations</i>:<li>(has(self.chartSpec) ? (!has(self.chartSource) && !has(self.chartRef)): true): chartSpec, chartSource and chartRef are mutually exclusive</li><li>(has(self.chartSource) ? (!has(self.chartSpec) && !has(self.chartRef)): true): chartSpec, chartSource and chartRef are mutually exclusive</li><li>(has(self.chartRef) ? (!has(self.chartSpec) && !has(self.chartSource)): true): chartSpec, chartSource and chartRef are mutually exclusive</li><li>has(self.chartSpec) || has(self.chartRef) || has(self.chartSource): one of chartSpec, chartRef or chartSource must be set</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>k8sConstraint</b></td>
        <td>string</td>
        <td>
          Constraint describing compatible K8S versions of the cluster set in the SemVer format.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomize">kustomize</a></b></td>
        <td>object</td>
        <td>
          Kustomize contains the Kustomize configuration for the template.<br/>
          <br/>
            <i>Validations</i>:<li>has(self.localSourceRef) ? !has(self.remoteSourceSpec): true: LocalSource and RemoteSource are mutually exclusive.</li><li>has(self.remoteSourceSpec) ? !has(self.localSourceRef): true: LocalSource and RemoteSource are mutually exclusive.</li><li>has(self.localSourceRef) || has(self.remoteSourceSpec): One of LocalSource or RemoteSource must be specified.</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresources">resources</a></b></td>
        <td>object</td>
        <td>
          Resources contains the resource configuration for the template.<br/>
          <br/>
            <i>Validations</i>:<li>has(self.localSourceRef) ? !has(self.remoteSourceSpec): true: LocalSource and RemoteSource are mutually exclusive.</li><li>has(self.remoteSourceSpec) ? !has(self.localSourceRef): true: LocalSource and RemoteSource are mutually exclusive.</li><li>has(self.localSourceRef) || has(self.remoteSourceSpec): One of LocalSource or RemoteSource must be specified.</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>version</b></td>
        <td>string</td>
        <td>
          Version is the semantic version of the application backed by template.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm
<sup><sup>[↩ Parent](#servicetemplatespec)</sup></sup>



Helm contains the Helm chart information for the template.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#servicetemplatespechelmchartref">chartRef</a></b></td>
        <td>object</td>
        <td>
          ChartRef is a reference to a source controller resource containing the
Helm chart representing the template.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsource">chartSource</a></b></td>
        <td>object</td>
        <td>
          ChartSource is a source of a Helm chart representing the template.<br/>
          <br/>
            <i>Validations</i>:<li>has(self.localSourceRef) ? (self.localSourceRef.kind != 'Secret' && self.localSourceRef.kind != 'ConfigMap'): true: Secret and ConfigMap are not supported as Helm chart sources</li><li>has(self.localSourceRef) ? !has(self.remoteSourceSpec): true: LocalSource and RemoteSource are mutually exclusive.</li><li>has(self.remoteSourceSpec) ? !has(self.localSourceRef): true: LocalSource and RemoteSource are mutually exclusive.</li><li>has(self.localSourceRef) || has(self.remoteSourceSpec): One of LocalSource or RemoteSource must be specified.</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartspec">chartSpec</a></b></td>
        <td>object</td>
        <td>
          ChartSpec defines the desired state of the HelmChart to be created by the controller<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartRef
<sup><sup>[↩ Parent](#servicetemplatespechelm)</sup></sup>



ChartRef is a reference to a source controller resource containing the
Helm chart representing the template.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>kind</b></td>
        <td>enum</td>
        <td>
          Kind of the referent.<br/>
          <br/>
            <i>Enum</i>: OCIRepository, HelmChart<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>apiVersion</b></td>
        <td>string</td>
        <td>
          APIVersion of the referent.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace of the referent, defaults to the namespace of the Kubernetes
resource object that contains the reference.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource
<sup><sup>[↩ Parent](#servicetemplatespechelm)</sup></sup>



ChartSource is a source of a Helm chart representing the template.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>deploymentType</b></td>
        <td>enum</td>
        <td>
          DeploymentType is the type of the deployment. This field is ignored,
when ResourceSpec is used as part of Helm chart configuration.<br/>
          <br/>
            <i>Enum</i>: Local, Remote<br/>
            <i>Default</i>: Remote<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>path</b></td>
        <td>string</td>
        <td>
          Path to the directory containing the resource manifest.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourcelocalsourceref">localSourceRef</a></b></td>
        <td>object</td>
        <td>
          LocalSourceRef is the local source of the kustomize manifest.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespec">remoteSourceSpec</a></b></td>
        <td>object</td>
        <td>
          RemoteSourceSpec is the remote source of the kustomize manifest.<br/>
          <br/>
            <i>Validations</i>:<li>has(self.git) ? (!has(self.bucket) && !has(self.oci)) : true: Git, Bucket and OCI are mutually exclusive.</li><li>has(self.bucket) ? (!has(self.git) && !has(self.oci)) : true: Git, Bucket and OCI are mutually exclusive.</li><li>has(self.oci) ? (!has(self.git) && !has(self.bucket)) : true: Git, Bucket and OCI are mutually exclusive.</li><li>has(self.git) || has(self.bucket) || has(self.oci): One of Git, Bucket or OCI must be specified.</li>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.localSourceRef
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsource)</sup></sup>



LocalSourceRef is the local source of the kustomize manifest.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>kind</b></td>
        <td>enum</td>
        <td>
          Kind is the kind of the local source.<br/>
          <br/>
            <i>Enum</i>: ConfigMap, Secret, GitRepository, Bucket, OCIRepository<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name is the name of the local source.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace is the namespace of the local source. Cross-namespace references
are only allowed when the Kind is one of [github.com/fluxcd/source-controller/api/v1.GitRepository],
[github.com/fluxcd/source-controller/api/v1.Bucket] or [github.com/fluxcd/source-controller/api/v1beta2.OCIRepository].
If the Kind is ConfigMap or Secret, the namespace will be ignored.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsource)</sup></sup>



RemoteSourceSpec is the remote source of the kustomize manifest.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecbucket">bucket</a></b></td>
        <td>object</td>
        <td>
          Bucket is the definition of bucket source.<br/>
          <br/>
            <i>Validations</i>:<li>self.provider == 'aws' || self.provider == 'generic' || !has(self.sts): STS configuration is only supported for the 'aws' and 'generic' Bucket providers</li><li>self.provider != 'aws' || !has(self.sts) || self.sts.provider == 'aws': 'aws' is the only supported STS provider for the 'aws' Bucket provider</li><li>self.provider != 'generic' || !has(self.sts) || self.sts.provider == 'ldap': 'ldap' is the only supported STS provider for the 'generic' Bucket provider</li><li>!has(self.sts) || self.sts.provider != 'aws' || !has(self.sts.secretRef): spec.sts.secretRef is not required for the 'aws' STS provider</li><li>!has(self.sts) || self.sts.provider != 'aws' || !has(self.sts.certSecretRef): spec.sts.certSecretRef is not required for the 'aws' STS provider</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecgit">git</a></b></td>
        <td>object</td>
        <td>
          Git is the definition of git repository source.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecoci">oci</a></b></td>
        <td>object</td>
        <td>
          OCI is the definition of OCI repository source.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.bucket
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespec)</sup></sup>



Bucket is the definition of bucket source.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>bucketName</b></td>
        <td>string</td>
        <td>
          BucketName is the name of the object storage bucket.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>endpoint</b></td>
        <td>string</td>
        <td>
          Endpoint is the object storage address the BucketName is located at.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>interval</b></td>
        <td>string</td>
        <td>
          Interval at which the Bucket Endpoint is checked for updates.
This interval is approximate and may be subject to jitter to ensure
efficient use of resources.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecbucketcertsecretref">certSecretRef</a></b></td>
        <td>object</td>
        <td>
          CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
bucket. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

This field is only supported for the `generic` provider.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>ignore</b></td>
        <td>string</td>
        <td>
          Ignore overrides the set of excluded patterns in the .sourceignore format
(which is the same as .gitignore). If not provided, a default will be used,
consult the documentation for your version to find out what those are.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>insecure</b></td>
        <td>boolean</td>
        <td>
          Insecure allows connecting to a non-TLS HTTP Endpoint.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>prefix</b></td>
        <td>string</td>
        <td>
          Prefix to use for server-side filtering of files in the Bucket.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider of the object storage bucket.
Defaults to 'generic', which expects an S3 (API) compatible object
storage.<br/>
          <br/>
            <i>Enum</i>: generic, aws, gcp, azure<br/>
            <i>Default</i>: generic<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecbucketproxysecretref">proxySecretRef</a></b></td>
        <td>object</td>
        <td>
          ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the Bucket server.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>region</b></td>
        <td>string</td>
        <td>
          Region of the Endpoint where the BucketName is located in.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecbucketsecretref">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing authentication credentials
for the Bucket.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecbucketsts">sts</a></b></td>
        <td>object</td>
        <td>
          STS specifies the required configuration to use a Security Token
Service for fetching temporary credentials to authenticate in a
Bucket provider.

This field is only supported for the `aws` and `generic` providers.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>suspend</b></td>
        <td>boolean</td>
        <td>
          Suspend tells the controller to suspend the reconciliation of this
Bucket.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>timeout</b></td>
        <td>string</td>
        <td>
          Timeout for fetch operations, defaults to 60s.<br/>
          <br/>
            <i>Default</i>: 60s<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.bucket.certSecretRef
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespecbucket)</sup></sup>



CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
bucket. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

This field is only supported for the `generic` provider.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.bucket.proxySecretRef
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespecbucket)</sup></sup>



ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the Bucket server.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.bucket.secretRef
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespecbucket)</sup></sup>



SecretRef specifies the Secret containing authentication credentials
for the Bucket.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.bucket.sts
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespecbucket)</sup></sup>



STS specifies the required configuration to use a Security Token
Service for fetching temporary credentials to authenticate in a
Bucket provider.

This field is only supported for the `aws` and `generic` providers.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>endpoint</b></td>
        <td>string</td>
        <td>
          Endpoint is the HTTP/S endpoint of the Security Token Service from
where temporary credentials will be fetched.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider of the Security Token Service.<br/>
          <br/>
            <i>Enum</i>: aws, ldap<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecbucketstscertsecretref">certSecretRef</a></b></td>
        <td>object</td>
        <td>
          CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
STS endpoint. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

This field is only supported for the `ldap` provider.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecbucketstssecretref">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing authentication credentials
for the STS endpoint. This Secret must contain the fields `username`
and `password` and is supported only for the `ldap` provider.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.bucket.sts.certSecretRef
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespecbucketsts)</sup></sup>



CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
STS endpoint. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

This field is only supported for the `ldap` provider.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.bucket.sts.secretRef
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespecbucketsts)</sup></sup>



SecretRef specifies the Secret containing authentication credentials
for the STS endpoint. This Secret must contain the fields `username`
and `password` and is supported only for the `ldap` provider.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.git
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespec)</sup></sup>



Git is the definition of git repository source.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>interval</b></td>
        <td>string</td>
        <td>
          Interval at which the GitRepository URL is checked for updates.
This interval is approximate and may be subject to jitter to ensure
efficient use of resources.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>url</b></td>
        <td>string</td>
        <td>
          URL specifies the Git repository URL, it can be an HTTP/S or SSH address.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>ignore</b></td>
        <td>string</td>
        <td>
          Ignore overrides the set of excluded patterns in the .sourceignore format
(which is the same as .gitignore). If not provided, a default will be used,
consult the documentation for your version to find out what those are.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecgitincludeindex">include</a></b></td>
        <td>[]object</td>
        <td>
          Include specifies a list of GitRepository resources which Artifacts
should be included in the Artifact produced for this GitRepository.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider used for authentication, can be 'azure', 'github', 'generic'.
When not specified, defaults to 'generic'.<br/>
          <br/>
            <i>Enum</i>: generic, azure, github<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecgitproxysecretref">proxySecretRef</a></b></td>
        <td>object</td>
        <td>
          ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the Git server.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>recurseSubmodules</b></td>
        <td>boolean</td>
        <td>
          RecurseSubmodules enables the initialization of all submodules within
the GitRepository as cloned from the URL, using their default settings.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecgitref">ref</a></b></td>
        <td>object</td>
        <td>
          Reference specifies the Git reference to resolve and monitor for
changes, defaults to the 'master' branch.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecgitsecretref">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing authentication credentials for
the GitRepository.
For HTTPS repositories the Secret must contain 'username' and 'password'
fields for basic auth or 'bearerToken' field for token auth.
For SSH repositories the Secret must contain 'identity'
and 'known_hosts' fields.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>suspend</b></td>
        <td>boolean</td>
        <td>
          Suspend tells the controller to suspend the reconciliation of this
GitRepository.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>timeout</b></td>
        <td>string</td>
        <td>
          Timeout for Git operations like cloning, defaults to 60s.<br/>
          <br/>
            <i>Default</i>: 60s<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecgitverify">verify</a></b></td>
        <td>object</td>
        <td>
          Verification specifies the configuration to verify the Git commit
signature(s).<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.git.include[index]
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespecgit)</sup></sup>



GitRepositoryInclude specifies a local reference to a GitRepository which
Artifact (sub-)contents must be included, and where they should be placed.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecgitincludeindexrepository">repository</a></b></td>
        <td>object</td>
        <td>
          GitRepositoryRef specifies the GitRepository which Artifact contents
must be included.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>fromPath</b></td>
        <td>string</td>
        <td>
          FromPath specifies the path to copy contents from, defaults to the root
of the Artifact.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>toPath</b></td>
        <td>string</td>
        <td>
          ToPath specifies the path to copy contents to, defaults to the name of
the GitRepositoryRef.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.git.include[index].repository
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespecgitincludeindex)</sup></sup>



GitRepositoryRef specifies the GitRepository which Artifact contents
must be included.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.git.proxySecretRef
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespecgit)</sup></sup>



ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the Git server.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.git.ref
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespecgit)</sup></sup>



Reference specifies the Git reference to resolve and monitor for
changes, defaults to the 'master' branch.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>branch</b></td>
        <td>string</td>
        <td>
          Branch to check out, defaults to 'master' if no other field is defined.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>commit</b></td>
        <td>string</td>
        <td>
          Commit SHA to check out, takes precedence over all reference fields.

This can be combined with Branch to shallow clone the branch, in which
the commit is expected to exist.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the reference to check out; takes precedence over Branch, Tag and SemVer.

It must be a valid Git reference: https://git-scm.com/docs/git-check-ref-format#_description
Examples: "refs/heads/main", "refs/tags/v0.1.0", "refs/pull/420/head", "refs/merge-requests/1/head"<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>semver</b></td>
        <td>string</td>
        <td>
          SemVer tag expression to check out, takes precedence over Tag.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>tag</b></td>
        <td>string</td>
        <td>
          Tag to check out, takes precedence over Branch.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.git.secretRef
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespecgit)</sup></sup>



SecretRef specifies the Secret containing authentication credentials for
the GitRepository.
For HTTPS repositories the Secret must contain 'username' and 'password'
fields for basic auth or 'bearerToken' field for token auth.
For SSH repositories the Secret must contain 'identity'
and 'known_hosts' fields.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.git.verify
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespecgit)</sup></sup>



Verification specifies the configuration to verify the Git commit
signature(s).

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecgitverifysecretref">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing the public keys of trusted Git
authors.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>mode</b></td>
        <td>enum</td>
        <td>
          Mode specifies which Git object(s) should be verified.

The variants "head" and "HEAD" both imply the same thing, i.e. verify
the commit that the HEAD of the Git repository points to. The variant
"head" solely exists to ensure backwards compatibility.<br/>
          <br/>
            <i>Enum</i>: head, HEAD, Tag, TagAndHEAD<br/>
            <i>Default</i>: HEAD<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.git.verify.secretRef
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespecgitverify)</sup></sup>



SecretRef specifies the Secret containing the public keys of trusted Git
authors.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.oci
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespec)</sup></sup>



OCI is the definition of OCI repository source.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>interval</b></td>
        <td>string</td>
        <td>
          Interval at which the OCIRepository URL is checked for updates.
This interval is approximate and may be subject to jitter to ensure
efficient use of resources.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>url</b></td>
        <td>string</td>
        <td>
          URL is a reference to an OCI artifact repository hosted
on a remote container registry.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecocicertsecretref">certSecretRef</a></b></td>
        <td>object</td>
        <td>
          CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
registry. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

Note: Support for the `caFile`, `certFile` and `keyFile` keys have
been deprecated.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>ignore</b></td>
        <td>string</td>
        <td>
          Ignore overrides the set of excluded patterns in the .sourceignore format
(which is the same as .gitignore). If not provided, a default will be used,
consult the documentation for your version to find out what those are.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>insecure</b></td>
        <td>boolean</td>
        <td>
          Insecure allows connecting to a non-TLS HTTP container registry.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecocilayerselector">layerSelector</a></b></td>
        <td>object</td>
        <td>
          LayerSelector specifies which layer should be extracted from the OCI artifact.
When not specified, the first layer found in the artifact is selected.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          The provider used for authentication, can be 'aws', 'azure', 'gcp' or 'generic'.
When not specified, defaults to 'generic'.<br/>
          <br/>
            <i>Enum</i>: generic, aws, azure, gcp<br/>
            <i>Default</i>: generic<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecociproxysecretref">proxySecretRef</a></b></td>
        <td>object</td>
        <td>
          ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the container registry.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecociref">ref</a></b></td>
        <td>object</td>
        <td>
          The OCI reference to pull and monitor for changes,
defaults to the latest tag.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecocisecretref">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef contains the secret name containing the registry login
credentials to resolve image metadata.
The secret must be of type kubernetes.io/dockerconfigjson.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>serviceAccountName</b></td>
        <td>string</td>
        <td>
          ServiceAccountName is the name of the Kubernetes ServiceAccount used to authenticate
the image pull if the service account has attached pull secrets. For more information:
https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#add-imagepullsecrets-to-a-service-account<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>suspend</b></td>
        <td>boolean</td>
        <td>
          This flag tells the controller to suspend the reconciliation of this source.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>timeout</b></td>
        <td>string</td>
        <td>
          The timeout for remote OCI Repository operations like pulling, defaults to 60s.<br/>
          <br/>
            <i>Default</i>: 60s<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecociverify">verify</a></b></td>
        <td>object</td>
        <td>
          Verify contains the secret name containing the trusted public keys
used to verify the signature and specifies which provider to use to check
whether OCI image is authentic.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.oci.certSecretRef
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespecoci)</sup></sup>



CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
registry. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

Note: Support for the `caFile`, `certFile` and `keyFile` keys have
been deprecated.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.oci.layerSelector
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespecoci)</sup></sup>



LayerSelector specifies which layer should be extracted from the OCI artifact.
When not specified, the first layer found in the artifact is selected.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>mediaType</b></td>
        <td>string</td>
        <td>
          MediaType specifies the OCI media type of the layer
which should be extracted from the OCI Artifact. The
first layer matching this type is selected.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>operation</b></td>
        <td>enum</td>
        <td>
          Operation specifies how the selected layer should be processed.
By default, the layer compressed content is extracted to storage.
When the operation is set to 'copy', the layer compressed content
is persisted to storage as it is.<br/>
          <br/>
            <i>Enum</i>: extract, copy<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.oci.proxySecretRef
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespecoci)</sup></sup>



ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the container registry.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.oci.ref
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespecoci)</sup></sup>



The OCI reference to pull and monitor for changes,
defaults to the latest tag.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>digest</b></td>
        <td>string</td>
        <td>
          Digest is the image digest to pull, takes precedence over SemVer.
The value should be in the format 'sha256:<HASH>'.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>semver</b></td>
        <td>string</td>
        <td>
          SemVer is the range of tags to pull selecting the latest within
the range, takes precedence over Tag.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>semverFilter</b></td>
        <td>string</td>
        <td>
          SemverFilter is a regex pattern to filter the tags within the SemVer range.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>tag</b></td>
        <td>string</td>
        <td>
          Tag is the image tag to pull, defaults to latest.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.oci.secretRef
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespecoci)</sup></sup>



SecretRef contains the secret name containing the registry login
credentials to resolve image metadata.
The secret must be of type kubernetes.io/dockerconfigjson.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.oci.verify
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespecoci)</sup></sup>



Verify contains the secret name containing the trusted public keys
used to verify the signature and specifies which provider to use to check
whether OCI image is authentic.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider specifies the technology used to sign the OCI Artifact.<br/>
          <br/>
            <i>Enum</i>: cosign, notation<br/>
            <i>Default</i>: cosign<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecociverifymatchoidcidentityindex">matchOIDCIdentity</a></b></td>
        <td>[]object</td>
        <td>
          MatchOIDCIdentity specifies the identity matching criteria to use
while verifying an OCI artifact which was signed using Cosign keyless
signing. The artifact's identity is deemed to be verified if any of the
specified matchers match against the identity.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecociverifysecretref">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Kubernetes Secret containing the
trusted public keys.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.oci.verify.matchOIDCIdentity[index]
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespecociverify)</sup></sup>



OIDCIdentityMatch specifies options for verifying the certificate identity,
i.e. the issuer and the subject of the certificate.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>issuer</b></td>
        <td>string</td>
        <td>
          Issuer specifies the regex pattern to match against to verify
the OIDC issuer in the Fulcio certificate. The pattern must be a
valid Go regular expression.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>subject</b></td>
        <td>string</td>
        <td>
          Subject specifies the regex pattern to match against to verify
the identity subject in the Fulcio certificate. The pattern must
be a valid Go regular expression.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.oci.verify.secretRef
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespecociverify)</sup></sup>



SecretRef specifies the Kubernetes Secret containing the
trusted public keys.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSpec
<sup><sup>[↩ Parent](#servicetemplatespechelm)</sup></sup>



ChartSpec defines the desired state of the HelmChart to be created by the controller

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>chart</b></td>
        <td>string</td>
        <td>
          Chart is the name or path the Helm chart is available at in the
SourceRef.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>interval</b></td>
        <td>string</td>
        <td>
          Interval at which the HelmChart SourceRef is checked for updates.
This interval is approximate and may be subject to jitter to ensure
efficient use of resources.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartspecsourceref">sourceRef</a></b></td>
        <td>object</td>
        <td>
          SourceRef is the reference to the Source the chart is available at.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>ignoreMissingValuesFiles</b></td>
        <td>boolean</td>
        <td>
          IgnoreMissingValuesFiles controls whether to silently ignore missing values
files rather than failing.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>reconcileStrategy</b></td>
        <td>enum</td>
        <td>
          ReconcileStrategy determines what enables the creation of a new artifact.
Valid values are ('ChartVersion', 'Revision').
See the documentation of the values for an explanation on their behavior.
Defaults to ChartVersion when omitted.<br/>
          <br/>
            <i>Enum</i>: ChartVersion, Revision<br/>
            <i>Default</i>: ChartVersion<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>suspend</b></td>
        <td>boolean</td>
        <td>
          Suspend tells the controller to suspend the reconciliation of this
source.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>valuesFiles</b></td>
        <td>[]string</td>
        <td>
          ValuesFiles is an alternative list of values files to use as the chart
values (values.yaml is not included by default), expected to be a
relative path in the SourceRef.
Values files are merged in the order of this list with the last file
overriding the first. Ignored when omitted.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartspecverify">verify</a></b></td>
        <td>object</td>
        <td>
          Verify contains the secret name containing the trusted public keys
used to verify the signature and specifies which provider to use to check
whether OCI image is authentic.
This field is only supported when using HelmRepository source with spec.type 'oci'.
Chart dependencies, which are not bundled in the umbrella chart artifact, are not verified.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>version</b></td>
        <td>string</td>
        <td>
          Version is the chart version semver expression, ignored for charts from
GitRepository and Bucket sources. Defaults to latest when omitted.<br/>
          <br/>
            <i>Default</i>: *<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSpec.sourceRef
<sup><sup>[↩ Parent](#servicetemplatespechelmchartspec)</sup></sup>



SourceRef is the reference to the Source the chart is available at.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>kind</b></td>
        <td>enum</td>
        <td>
          Kind of the referent, valid values are ('HelmRepository', 'GitRepository',
'Bucket').<br/>
          <br/>
            <i>Enum</i>: HelmRepository, GitRepository, Bucket<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>apiVersion</b></td>
        <td>string</td>
        <td>
          APIVersion of the referent.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSpec.verify
<sup><sup>[↩ Parent](#servicetemplatespechelmchartspec)</sup></sup>



Verify contains the secret name containing the trusted public keys
used to verify the signature and specifies which provider to use to check
whether OCI image is authentic.
This field is only supported when using HelmRepository source with spec.type 'oci'.
Chart dependencies, which are not bundled in the umbrella chart artifact, are not verified.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider specifies the technology used to sign the OCI Artifact.<br/>
          <br/>
            <i>Enum</i>: cosign, notation<br/>
            <i>Default</i>: cosign<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartspecverifymatchoidcidentityindex">matchOIDCIdentity</a></b></td>
        <td>[]object</td>
        <td>
          MatchOIDCIdentity specifies the identity matching criteria to use
while verifying an OCI artifact which was signed using Cosign keyless
signing. The artifact's identity is deemed to be verified if any of the
specified matchers match against the identity.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartspecverifysecretref">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Kubernetes Secret containing the
trusted public keys.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSpec.verify.matchOIDCIdentity[index]
<sup><sup>[↩ Parent](#servicetemplatespechelmchartspecverify)</sup></sup>



OIDCIdentityMatch specifies options for verifying the certificate identity,
i.e. the issuer and the subject of the certificate.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>issuer</b></td>
        <td>string</td>
        <td>
          Issuer specifies the regex pattern to match against to verify
the OIDC issuer in the Fulcio certificate. The pattern must be a
valid Go regular expression.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>subject</b></td>
        <td>string</td>
        <td>
          Subject specifies the regex pattern to match against to verify
the identity subject in the Fulcio certificate. The pattern must
be a valid Go regular expression.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSpec.verify.secretRef
<sup><sup>[↩ Parent](#servicetemplatespechelmchartspecverify)</sup></sup>



SecretRef specifies the Kubernetes Secret containing the
trusted public keys.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize
<sup><sup>[↩ Parent](#servicetemplatespec)</sup></sup>



Kustomize contains the Kustomize configuration for the template.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>deploymentType</b></td>
        <td>enum</td>
        <td>
          DeploymentType is the type of the deployment. This field is ignored,
when ResourceSpec is used as part of Helm chart configuration.<br/>
          <br/>
            <i>Enum</i>: Local, Remote<br/>
            <i>Default</i>: Remote<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>path</b></td>
        <td>string</td>
        <td>
          Path to the directory containing the resource manifest.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizelocalsourceref">localSourceRef</a></b></td>
        <td>object</td>
        <td>
          LocalSourceRef is the local source of the kustomize manifest.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespec">remoteSourceSpec</a></b></td>
        <td>object</td>
        <td>
          RemoteSourceSpec is the remote source of the kustomize manifest.<br/>
          <br/>
            <i>Validations</i>:<li>has(self.git) ? (!has(self.bucket) && !has(self.oci)) : true: Git, Bucket and OCI are mutually exclusive.</li><li>has(self.bucket) ? (!has(self.git) && !has(self.oci)) : true: Git, Bucket and OCI are mutually exclusive.</li><li>has(self.oci) ? (!has(self.git) && !has(self.bucket)) : true: Git, Bucket and OCI are mutually exclusive.</li><li>has(self.git) || has(self.bucket) || has(self.oci): One of Git, Bucket or OCI must be specified.</li>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.localSourceRef
<sup><sup>[↩ Parent](#servicetemplatespeckustomize)</sup></sup>



LocalSourceRef is the local source of the kustomize manifest.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>kind</b></td>
        <td>enum</td>
        <td>
          Kind is the kind of the local source.<br/>
          <br/>
            <i>Enum</i>: ConfigMap, Secret, GitRepository, Bucket, OCIRepository<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name is the name of the local source.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace is the namespace of the local source. Cross-namespace references
are only allowed when the Kind is one of [github.com/fluxcd/source-controller/api/v1.GitRepository],
[github.com/fluxcd/source-controller/api/v1.Bucket] or [github.com/fluxcd/source-controller/api/v1beta2.OCIRepository].
If the Kind is ConfigMap or Secret, the namespace will be ignored.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec
<sup><sup>[↩ Parent](#servicetemplatespeckustomize)</sup></sup>



RemoteSourceSpec is the remote source of the kustomize manifest.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecbucket">bucket</a></b></td>
        <td>object</td>
        <td>
          Bucket is the definition of bucket source.<br/>
          <br/>
            <i>Validations</i>:<li>self.provider == 'aws' || self.provider == 'generic' || !has(self.sts): STS configuration is only supported for the 'aws' and 'generic' Bucket providers</li><li>self.provider != 'aws' || !has(self.sts) || self.sts.provider == 'aws': 'aws' is the only supported STS provider for the 'aws' Bucket provider</li><li>self.provider != 'generic' || !has(self.sts) || self.sts.provider == 'ldap': 'ldap' is the only supported STS provider for the 'generic' Bucket provider</li><li>!has(self.sts) || self.sts.provider != 'aws' || !has(self.sts.secretRef): spec.sts.secretRef is not required for the 'aws' STS provider</li><li>!has(self.sts) || self.sts.provider != 'aws' || !has(self.sts.certSecretRef): spec.sts.certSecretRef is not required for the 'aws' STS provider</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecgit">git</a></b></td>
        <td>object</td>
        <td>
          Git is the definition of git repository source.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecoci">oci</a></b></td>
        <td>object</td>
        <td>
          OCI is the definition of OCI repository source.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.bucket
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespec)</sup></sup>



Bucket is the definition of bucket source.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>bucketName</b></td>
        <td>string</td>
        <td>
          BucketName is the name of the object storage bucket.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>endpoint</b></td>
        <td>string</td>
        <td>
          Endpoint is the object storage address the BucketName is located at.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>interval</b></td>
        <td>string</td>
        <td>
          Interval at which the Bucket Endpoint is checked for updates.
This interval is approximate and may be subject to jitter to ensure
efficient use of resources.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecbucketcertsecretref">certSecretRef</a></b></td>
        <td>object</td>
        <td>
          CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
bucket. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

This field is only supported for the `generic` provider.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>ignore</b></td>
        <td>string</td>
        <td>
          Ignore overrides the set of excluded patterns in the .sourceignore format
(which is the same as .gitignore). If not provided, a default will be used,
consult the documentation for your version to find out what those are.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>insecure</b></td>
        <td>boolean</td>
        <td>
          Insecure allows connecting to a non-TLS HTTP Endpoint.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>prefix</b></td>
        <td>string</td>
        <td>
          Prefix to use for server-side filtering of files in the Bucket.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider of the object storage bucket.
Defaults to 'generic', which expects an S3 (API) compatible object
storage.<br/>
          <br/>
            <i>Enum</i>: generic, aws, gcp, azure<br/>
            <i>Default</i>: generic<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecbucketproxysecretref">proxySecretRef</a></b></td>
        <td>object</td>
        <td>
          ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the Bucket server.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>region</b></td>
        <td>string</td>
        <td>
          Region of the Endpoint where the BucketName is located in.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecbucketsecretref">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing authentication credentials
for the Bucket.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecbucketsts">sts</a></b></td>
        <td>object</td>
        <td>
          STS specifies the required configuration to use a Security Token
Service for fetching temporary credentials to authenticate in a
Bucket provider.

This field is only supported for the `aws` and `generic` providers.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>suspend</b></td>
        <td>boolean</td>
        <td>
          Suspend tells the controller to suspend the reconciliation of this
Bucket.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>timeout</b></td>
        <td>string</td>
        <td>
          Timeout for fetch operations, defaults to 60s.<br/>
          <br/>
            <i>Default</i>: 60s<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.bucket.certSecretRef
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespecbucket)</sup></sup>



CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
bucket. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

This field is only supported for the `generic` provider.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.bucket.proxySecretRef
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespecbucket)</sup></sup>



ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the Bucket server.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.bucket.secretRef
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespecbucket)</sup></sup>



SecretRef specifies the Secret containing authentication credentials
for the Bucket.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.bucket.sts
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespecbucket)</sup></sup>



STS specifies the required configuration to use a Security Token
Service for fetching temporary credentials to authenticate in a
Bucket provider.

This field is only supported for the `aws` and `generic` providers.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>endpoint</b></td>
        <td>string</td>
        <td>
          Endpoint is the HTTP/S endpoint of the Security Token Service from
where temporary credentials will be fetched.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider of the Security Token Service.<br/>
          <br/>
            <i>Enum</i>: aws, ldap<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecbucketstscertsecretref">certSecretRef</a></b></td>
        <td>object</td>
        <td>
          CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
STS endpoint. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

This field is only supported for the `ldap` provider.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecbucketstssecretref">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing authentication credentials
for the STS endpoint. This Secret must contain the fields `username`
and `password` and is supported only for the `ldap` provider.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.bucket.sts.certSecretRef
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespecbucketsts)</sup></sup>



CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
STS endpoint. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

This field is only supported for the `ldap` provider.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.bucket.sts.secretRef
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespecbucketsts)</sup></sup>



SecretRef specifies the Secret containing authentication credentials
for the STS endpoint. This Secret must contain the fields `username`
and `password` and is supported only for the `ldap` provider.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.git
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespec)</sup></sup>



Git is the definition of git repository source.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>interval</b></td>
        <td>string</td>
        <td>
          Interval at which the GitRepository URL is checked for updates.
This interval is approximate and may be subject to jitter to ensure
efficient use of resources.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>url</b></td>
        <td>string</td>
        <td>
          URL specifies the Git repository URL, it can be an HTTP/S or SSH address.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>ignore</b></td>
        <td>string</td>
        <td>
          Ignore overrides the set of excluded patterns in the .sourceignore format
(which is the same as .gitignore). If not provided, a default will be used,
consult the documentation for your version to find out what those are.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecgitincludeindex">include</a></b></td>
        <td>[]object</td>
        <td>
          Include specifies a list of GitRepository resources which Artifacts
should be included in the Artifact produced for this GitRepository.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider used for authentication, can be 'azure', 'github', 'generic'.
When not specified, defaults to 'generic'.<br/>
          <br/>
            <i>Enum</i>: generic, azure, github<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecgitproxysecretref">proxySecretRef</a></b></td>
        <td>object</td>
        <td>
          ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the Git server.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>recurseSubmodules</b></td>
        <td>boolean</td>
        <td>
          RecurseSubmodules enables the initialization of all submodules within
the GitRepository as cloned from the URL, using their default settings.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecgitref">ref</a></b></td>
        <td>object</td>
        <td>
          Reference specifies the Git reference to resolve and monitor for
changes, defaults to the 'master' branch.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecgitsecretref">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing authentication credentials for
the GitRepository.
For HTTPS repositories the Secret must contain 'username' and 'password'
fields for basic auth or 'bearerToken' field for token auth.
For SSH repositories the Secret must contain 'identity'
and 'known_hosts' fields.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>suspend</b></td>
        <td>boolean</td>
        <td>
          Suspend tells the controller to suspend the reconciliation of this
GitRepository.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>timeout</b></td>
        <td>string</td>
        <td>
          Timeout for Git operations like cloning, defaults to 60s.<br/>
          <br/>
            <i>Default</i>: 60s<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecgitverify">verify</a></b></td>
        <td>object</td>
        <td>
          Verification specifies the configuration to verify the Git commit
signature(s).<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.git.include[index]
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespecgit)</sup></sup>



GitRepositoryInclude specifies a local reference to a GitRepository which
Artifact (sub-)contents must be included, and where they should be placed.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecgitincludeindexrepository">repository</a></b></td>
        <td>object</td>
        <td>
          GitRepositoryRef specifies the GitRepository which Artifact contents
must be included.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>fromPath</b></td>
        <td>string</td>
        <td>
          FromPath specifies the path to copy contents from, defaults to the root
of the Artifact.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>toPath</b></td>
        <td>string</td>
        <td>
          ToPath specifies the path to copy contents to, defaults to the name of
the GitRepositoryRef.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.git.include[index].repository
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespecgitincludeindex)</sup></sup>



GitRepositoryRef specifies the GitRepository which Artifact contents
must be included.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.git.proxySecretRef
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespecgit)</sup></sup>



ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the Git server.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.git.ref
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespecgit)</sup></sup>



Reference specifies the Git reference to resolve and monitor for
changes, defaults to the 'master' branch.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>branch</b></td>
        <td>string</td>
        <td>
          Branch to check out, defaults to 'master' if no other field is defined.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>commit</b></td>
        <td>string</td>
        <td>
          Commit SHA to check out, takes precedence over all reference fields.

This can be combined with Branch to shallow clone the branch, in which
the commit is expected to exist.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the reference to check out; takes precedence over Branch, Tag and SemVer.

It must be a valid Git reference: https://git-scm.com/docs/git-check-ref-format#_description
Examples: "refs/heads/main", "refs/tags/v0.1.0", "refs/pull/420/head", "refs/merge-requests/1/head"<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>semver</b></td>
        <td>string</td>
        <td>
          SemVer tag expression to check out, takes precedence over Tag.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>tag</b></td>
        <td>string</td>
        <td>
          Tag to check out, takes precedence over Branch.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.git.secretRef
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespecgit)</sup></sup>



SecretRef specifies the Secret containing authentication credentials for
the GitRepository.
For HTTPS repositories the Secret must contain 'username' and 'password'
fields for basic auth or 'bearerToken' field for token auth.
For SSH repositories the Secret must contain 'identity'
and 'known_hosts' fields.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.git.verify
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespecgit)</sup></sup>



Verification specifies the configuration to verify the Git commit
signature(s).

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecgitverifysecretref">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing the public keys of trusted Git
authors.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>mode</b></td>
        <td>enum</td>
        <td>
          Mode specifies which Git object(s) should be verified.

The variants "head" and "HEAD" both imply the same thing, i.e. verify
the commit that the HEAD of the Git repository points to. The variant
"head" solely exists to ensure backwards compatibility.<br/>
          <br/>
            <i>Enum</i>: head, HEAD, Tag, TagAndHEAD<br/>
            <i>Default</i>: HEAD<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.git.verify.secretRef
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespecgitverify)</sup></sup>



SecretRef specifies the Secret containing the public keys of trusted Git
authors.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.oci
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespec)</sup></sup>



OCI is the definition of OCI repository source.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>interval</b></td>
        <td>string</td>
        <td>
          Interval at which the OCIRepository URL is checked for updates.
This interval is approximate and may be subject to jitter to ensure
efficient use of resources.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>url</b></td>
        <td>string</td>
        <td>
          URL is a reference to an OCI artifact repository hosted
on a remote container registry.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecocicertsecretref">certSecretRef</a></b></td>
        <td>object</td>
        <td>
          CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
registry. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

Note: Support for the `caFile`, `certFile` and `keyFile` keys have
been deprecated.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>ignore</b></td>
        <td>string</td>
        <td>
          Ignore overrides the set of excluded patterns in the .sourceignore format
(which is the same as .gitignore). If not provided, a default will be used,
consult the documentation for your version to find out what those are.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>insecure</b></td>
        <td>boolean</td>
        <td>
          Insecure allows connecting to a non-TLS HTTP container registry.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecocilayerselector">layerSelector</a></b></td>
        <td>object</td>
        <td>
          LayerSelector specifies which layer should be extracted from the OCI artifact.
When not specified, the first layer found in the artifact is selected.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          The provider used for authentication, can be 'aws', 'azure', 'gcp' or 'generic'.
When not specified, defaults to 'generic'.<br/>
          <br/>
            <i>Enum</i>: generic, aws, azure, gcp<br/>
            <i>Default</i>: generic<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecociproxysecretref">proxySecretRef</a></b></td>
        <td>object</td>
        <td>
          ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the container registry.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecociref">ref</a></b></td>
        <td>object</td>
        <td>
          The OCI reference to pull and monitor for changes,
defaults to the latest tag.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecocisecretref">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef contains the secret name containing the registry login
credentials to resolve image metadata.
The secret must be of type kubernetes.io/dockerconfigjson.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>serviceAccountName</b></td>
        <td>string</td>
        <td>
          ServiceAccountName is the name of the Kubernetes ServiceAccount used to authenticate
the image pull if the service account has attached pull secrets. For more information:
https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#add-imagepullsecrets-to-a-service-account<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>suspend</b></td>
        <td>boolean</td>
        <td>
          This flag tells the controller to suspend the reconciliation of this source.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>timeout</b></td>
        <td>string</td>
        <td>
          The timeout for remote OCI Repository operations like pulling, defaults to 60s.<br/>
          <br/>
            <i>Default</i>: 60s<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecociverify">verify</a></b></td>
        <td>object</td>
        <td>
          Verify contains the secret name containing the trusted public keys
used to verify the signature and specifies which provider to use to check
whether OCI image is authentic.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.oci.certSecretRef
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespecoci)</sup></sup>



CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
registry. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

Note: Support for the `caFile`, `certFile` and `keyFile` keys have
been deprecated.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.oci.layerSelector
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespecoci)</sup></sup>



LayerSelector specifies which layer should be extracted from the OCI artifact.
When not specified, the first layer found in the artifact is selected.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>mediaType</b></td>
        <td>string</td>
        <td>
          MediaType specifies the OCI media type of the layer
which should be extracted from the OCI Artifact. The
first layer matching this type is selected.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>operation</b></td>
        <td>enum</td>
        <td>
          Operation specifies how the selected layer should be processed.
By default, the layer compressed content is extracted to storage.
When the operation is set to 'copy', the layer compressed content
is persisted to storage as it is.<br/>
          <br/>
            <i>Enum</i>: extract, copy<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.oci.proxySecretRef
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespecoci)</sup></sup>



ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the container registry.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.oci.ref
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespecoci)</sup></sup>



The OCI reference to pull and monitor for changes,
defaults to the latest tag.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>digest</b></td>
        <td>string</td>
        <td>
          Digest is the image digest to pull, takes precedence over SemVer.
The value should be in the format 'sha256:<HASH>'.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>semver</b></td>
        <td>string</td>
        <td>
          SemVer is the range of tags to pull selecting the latest within
the range, takes precedence over Tag.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>semverFilter</b></td>
        <td>string</td>
        <td>
          SemverFilter is a regex pattern to filter the tags within the SemVer range.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>tag</b></td>
        <td>string</td>
        <td>
          Tag is the image tag to pull, defaults to latest.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.oci.secretRef
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespecoci)</sup></sup>



SecretRef contains the secret name containing the registry login
credentials to resolve image metadata.
The secret must be of type kubernetes.io/dockerconfigjson.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.oci.verify
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespecoci)</sup></sup>



Verify contains the secret name containing the trusted public keys
used to verify the signature and specifies which provider to use to check
whether OCI image is authentic.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider specifies the technology used to sign the OCI Artifact.<br/>
          <br/>
            <i>Enum</i>: cosign, notation<br/>
            <i>Default</i>: cosign<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecociverifymatchoidcidentityindex">matchOIDCIdentity</a></b></td>
        <td>[]object</td>
        <td>
          MatchOIDCIdentity specifies the identity matching criteria to use
while verifying an OCI artifact which was signed using Cosign keyless
signing. The artifact's identity is deemed to be verified if any of the
specified matchers match against the identity.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecociverifysecretref">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Kubernetes Secret containing the
trusted public keys.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.oci.verify.matchOIDCIdentity[index]
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespecociverify)</sup></sup>



OIDCIdentityMatch specifies options for verifying the certificate identity,
i.e. the issuer and the subject of the certificate.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>issuer</b></td>
        <td>string</td>
        <td>
          Issuer specifies the regex pattern to match against to verify
the OIDC issuer in the Fulcio certificate. The pattern must be a
valid Go regular expression.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>subject</b></td>
        <td>string</td>
        <td>
          Subject specifies the regex pattern to match against to verify
the identity subject in the Fulcio certificate. The pattern must
be a valid Go regular expression.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.oci.verify.secretRef
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespecociverify)</sup></sup>



SecretRef specifies the Kubernetes Secret containing the
trusted public keys.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources
<sup><sup>[↩ Parent](#servicetemplatespec)</sup></sup>



Resources contains the resource configuration for the template.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>deploymentType</b></td>
        <td>enum</td>
        <td>
          DeploymentType is the type of the deployment. This field is ignored,
when ResourceSpec is used as part of Helm chart configuration.<br/>
          <br/>
            <i>Enum</i>: Local, Remote<br/>
            <i>Default</i>: Remote<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>path</b></td>
        <td>string</td>
        <td>
          Path to the directory containing the resource manifest.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourceslocalsourceref">localSourceRef</a></b></td>
        <td>object</td>
        <td>
          LocalSourceRef is the local source of the kustomize manifest.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespec">remoteSourceSpec</a></b></td>
        <td>object</td>
        <td>
          RemoteSourceSpec is the remote source of the kustomize manifest.<br/>
          <br/>
            <i>Validations</i>:<li>has(self.git) ? (!has(self.bucket) && !has(self.oci)) : true: Git, Bucket and OCI are mutually exclusive.</li><li>has(self.bucket) ? (!has(self.git) && !has(self.oci)) : true: Git, Bucket and OCI are mutually exclusive.</li><li>has(self.oci) ? (!has(self.git) && !has(self.bucket)) : true: Git, Bucket and OCI are mutually exclusive.</li><li>has(self.git) || has(self.bucket) || has(self.oci): One of Git, Bucket or OCI must be specified.</li>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.localSourceRef
<sup><sup>[↩ Parent](#servicetemplatespecresources)</sup></sup>



LocalSourceRef is the local source of the kustomize manifest.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>kind</b></td>
        <td>enum</td>
        <td>
          Kind is the kind of the local source.<br/>
          <br/>
            <i>Enum</i>: ConfigMap, Secret, GitRepository, Bucket, OCIRepository<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name is the name of the local source.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace is the namespace of the local source. Cross-namespace references
are only allowed when the Kind is one of [github.com/fluxcd/source-controller/api/v1.GitRepository],
[github.com/fluxcd/source-controller/api/v1.Bucket] or [github.com/fluxcd/source-controller/api/v1beta2.OCIRepository].
If the Kind is ConfigMap or Secret, the namespace will be ignored.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec
<sup><sup>[↩ Parent](#servicetemplatespecresources)</sup></sup>



RemoteSourceSpec is the remote source of the kustomize manifest.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecbucket">bucket</a></b></td>
        <td>object</td>
        <td>
          Bucket is the definition of bucket source.<br/>
          <br/>
            <i>Validations</i>:<li>self.provider == 'aws' || self.provider == 'generic' || !has(self.sts): STS configuration is only supported for the 'aws' and 'generic' Bucket providers</li><li>self.provider != 'aws' || !has(self.sts) || self.sts.provider == 'aws': 'aws' is the only supported STS provider for the 'aws' Bucket provider</li><li>self.provider != 'generic' || !has(self.sts) || self.sts.provider == 'ldap': 'ldap' is the only supported STS provider for the 'generic' Bucket provider</li><li>!has(self.sts) || self.sts.provider != 'aws' || !has(self.sts.secretRef): spec.sts.secretRef is not required for the 'aws' STS provider</li><li>!has(self.sts) || self.sts.provider != 'aws' || !has(self.sts.certSecretRef): spec.sts.certSecretRef is not required for the 'aws' STS provider</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecgit">git</a></b></td>
        <td>object</td>
        <td>
          Git is the definition of git repository source.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecoci">oci</a></b></td>
        <td>object</td>
        <td>
          OCI is the definition of OCI repository source.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.bucket
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespec)</sup></sup>



Bucket is the definition of bucket source.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>bucketName</b></td>
        <td>string</td>
        <td>
          BucketName is the name of the object storage bucket.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>endpoint</b></td>
        <td>string</td>
        <td>
          Endpoint is the object storage address the BucketName is located at.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>interval</b></td>
        <td>string</td>
        <td>
          Interval at which the Bucket Endpoint is checked for updates.
This interval is approximate and may be subject to jitter to ensure
efficient use of resources.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecbucketcertsecretref">certSecretRef</a></b></td>
        <td>object</td>
        <td>
          CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
bucket. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

This field is only supported for the `generic` provider.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>ignore</b></td>
        <td>string</td>
        <td>
          Ignore overrides the set of excluded patterns in the .sourceignore format
(which is the same as .gitignore). If not provided, a default will be used,
consult the documentation for your version to find out what those are.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>insecure</b></td>
        <td>boolean</td>
        <td>
          Insecure allows connecting to a non-TLS HTTP Endpoint.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>prefix</b></td>
        <td>string</td>
        <td>
          Prefix to use for server-side filtering of files in the Bucket.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider of the object storage bucket.
Defaults to 'generic', which expects an S3 (API) compatible object
storage.<br/>
          <br/>
            <i>Enum</i>: generic, aws, gcp, azure<br/>
            <i>Default</i>: generic<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecbucketproxysecretref">proxySecretRef</a></b></td>
        <td>object</td>
        <td>
          ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the Bucket server.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>region</b></td>
        <td>string</td>
        <td>
          Region of the Endpoint where the BucketName is located in.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecbucketsecretref">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing authentication credentials
for the Bucket.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecbucketsts">sts</a></b></td>
        <td>object</td>
        <td>
          STS specifies the required configuration to use a Security Token
Service for fetching temporary credentials to authenticate in a
Bucket provider.

This field is only supported for the `aws` and `generic` providers.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>suspend</b></td>
        <td>boolean</td>
        <td>
          Suspend tells the controller to suspend the reconciliation of this
Bucket.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>timeout</b></td>
        <td>string</td>
        <td>
          Timeout for fetch operations, defaults to 60s.<br/>
          <br/>
            <i>Default</i>: 60s<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.bucket.certSecretRef
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespecbucket)</sup></sup>



CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
bucket. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

This field is only supported for the `generic` provider.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.bucket.proxySecretRef
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespecbucket)</sup></sup>



ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the Bucket server.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.bucket.secretRef
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespecbucket)</sup></sup>



SecretRef specifies the Secret containing authentication credentials
for the Bucket.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.bucket.sts
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespecbucket)</sup></sup>



STS specifies the required configuration to use a Security Token
Service for fetching temporary credentials to authenticate in a
Bucket provider.

This field is only supported for the `aws` and `generic` providers.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>endpoint</b></td>
        <td>string</td>
        <td>
          Endpoint is the HTTP/S endpoint of the Security Token Service from
where temporary credentials will be fetched.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider of the Security Token Service.<br/>
          <br/>
            <i>Enum</i>: aws, ldap<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecbucketstscertsecretref">certSecretRef</a></b></td>
        <td>object</td>
        <td>
          CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
STS endpoint. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

This field is only supported for the `ldap` provider.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecbucketstssecretref">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing authentication credentials
for the STS endpoint. This Secret must contain the fields `username`
and `password` and is supported only for the `ldap` provider.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.bucket.sts.certSecretRef
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespecbucketsts)</sup></sup>



CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
STS endpoint. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

This field is only supported for the `ldap` provider.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.bucket.sts.secretRef
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespecbucketsts)</sup></sup>



SecretRef specifies the Secret containing authentication credentials
for the STS endpoint. This Secret must contain the fields `username`
and `password` and is supported only for the `ldap` provider.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.git
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespec)</sup></sup>



Git is the definition of git repository source.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>interval</b></td>
        <td>string</td>
        <td>
          Interval at which the GitRepository URL is checked for updates.
This interval is approximate and may be subject to jitter to ensure
efficient use of resources.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>url</b></td>
        <td>string</td>
        <td>
          URL specifies the Git repository URL, it can be an HTTP/S or SSH address.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>ignore</b></td>
        <td>string</td>
        <td>
          Ignore overrides the set of excluded patterns in the .sourceignore format
(which is the same as .gitignore). If not provided, a default will be used,
consult the documentation for your version to find out what those are.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecgitincludeindex">include</a></b></td>
        <td>[]object</td>
        <td>
          Include specifies a list of GitRepository resources which Artifacts
should be included in the Artifact produced for this GitRepository.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider used for authentication, can be 'azure', 'github', 'generic'.
When not specified, defaults to 'generic'.<br/>
          <br/>
            <i>Enum</i>: generic, azure, github<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecgitproxysecretref">proxySecretRef</a></b></td>
        <td>object</td>
        <td>
          ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the Git server.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>recurseSubmodules</b></td>
        <td>boolean</td>
        <td>
          RecurseSubmodules enables the initialization of all submodules within
the GitRepository as cloned from the URL, using their default settings.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecgitref">ref</a></b></td>
        <td>object</td>
        <td>
          Reference specifies the Git reference to resolve and monitor for
changes, defaults to the 'master' branch.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecgitsecretref">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing authentication credentials for
the GitRepository.
For HTTPS repositories the Secret must contain 'username' and 'password'
fields for basic auth or 'bearerToken' field for token auth.
For SSH repositories the Secret must contain 'identity'
and 'known_hosts' fields.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>suspend</b></td>
        <td>boolean</td>
        <td>
          Suspend tells the controller to suspend the reconciliation of this
GitRepository.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>timeout</b></td>
        <td>string</td>
        <td>
          Timeout for Git operations like cloning, defaults to 60s.<br/>
          <br/>
            <i>Default</i>: 60s<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecgitverify">verify</a></b></td>
        <td>object</td>
        <td>
          Verification specifies the configuration to verify the Git commit
signature(s).<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.git.include[index]
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespecgit)</sup></sup>



GitRepositoryInclude specifies a local reference to a GitRepository which
Artifact (sub-)contents must be included, and where they should be placed.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecgitincludeindexrepository">repository</a></b></td>
        <td>object</td>
        <td>
          GitRepositoryRef specifies the GitRepository which Artifact contents
must be included.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>fromPath</b></td>
        <td>string</td>
        <td>
          FromPath specifies the path to copy contents from, defaults to the root
of the Artifact.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>toPath</b></td>
        <td>string</td>
        <td>
          ToPath specifies the path to copy contents to, defaults to the name of
the GitRepositoryRef.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.git.include[index].repository
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespecgitincludeindex)</sup></sup>



GitRepositoryRef specifies the GitRepository which Artifact contents
must be included.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.git.proxySecretRef
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespecgit)</sup></sup>



ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the Git server.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.git.ref
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespecgit)</sup></sup>



Reference specifies the Git reference to resolve and monitor for
changes, defaults to the 'master' branch.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>branch</b></td>
        <td>string</td>
        <td>
          Branch to check out, defaults to 'master' if no other field is defined.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>commit</b></td>
        <td>string</td>
        <td>
          Commit SHA to check out, takes precedence over all reference fields.

This can be combined with Branch to shallow clone the branch, in which
the commit is expected to exist.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the reference to check out; takes precedence over Branch, Tag and SemVer.

It must be a valid Git reference: https://git-scm.com/docs/git-check-ref-format#_description
Examples: "refs/heads/main", "refs/tags/v0.1.0", "refs/pull/420/head", "refs/merge-requests/1/head"<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>semver</b></td>
        <td>string</td>
        <td>
          SemVer tag expression to check out, takes precedence over Tag.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>tag</b></td>
        <td>string</td>
        <td>
          Tag to check out, takes precedence over Branch.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.git.secretRef
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespecgit)</sup></sup>



SecretRef specifies the Secret containing authentication credentials for
the GitRepository.
For HTTPS repositories the Secret must contain 'username' and 'password'
fields for basic auth or 'bearerToken' field for token auth.
For SSH repositories the Secret must contain 'identity'
and 'known_hosts' fields.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.git.verify
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespecgit)</sup></sup>



Verification specifies the configuration to verify the Git commit
signature(s).

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecgitverifysecretref">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing the public keys of trusted Git
authors.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>mode</b></td>
        <td>enum</td>
        <td>
          Mode specifies which Git object(s) should be verified.

The variants "head" and "HEAD" both imply the same thing, i.e. verify
the commit that the HEAD of the Git repository points to. The variant
"head" solely exists to ensure backwards compatibility.<br/>
          <br/>
            <i>Enum</i>: head, HEAD, Tag, TagAndHEAD<br/>
            <i>Default</i>: HEAD<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.git.verify.secretRef
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespecgitverify)</sup></sup>



SecretRef specifies the Secret containing the public keys of trusted Git
authors.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.oci
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespec)</sup></sup>



OCI is the definition of OCI repository source.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>interval</b></td>
        <td>string</td>
        <td>
          Interval at which the OCIRepository URL is checked for updates.
This interval is approximate and may be subject to jitter to ensure
efficient use of resources.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>url</b></td>
        <td>string</td>
        <td>
          URL is a reference to an OCI artifact repository hosted
on a remote container registry.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecocicertsecretref">certSecretRef</a></b></td>
        <td>object</td>
        <td>
          CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
registry. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

Note: Support for the `caFile`, `certFile` and `keyFile` keys have
been deprecated.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>ignore</b></td>
        <td>string</td>
        <td>
          Ignore overrides the set of excluded patterns in the .sourceignore format
(which is the same as .gitignore). If not provided, a default will be used,
consult the documentation for your version to find out what those are.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>insecure</b></td>
        <td>boolean</td>
        <td>
          Insecure allows connecting to a non-TLS HTTP container registry.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecocilayerselector">layerSelector</a></b></td>
        <td>object</td>
        <td>
          LayerSelector specifies which layer should be extracted from the OCI artifact.
When not specified, the first layer found in the artifact is selected.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          The provider used for authentication, can be 'aws', 'azure', 'gcp' or 'generic'.
When not specified, defaults to 'generic'.<br/>
          <br/>
            <i>Enum</i>: generic, aws, azure, gcp<br/>
            <i>Default</i>: generic<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecociproxysecretref">proxySecretRef</a></b></td>
        <td>object</td>
        <td>
          ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the container registry.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecociref">ref</a></b></td>
        <td>object</td>
        <td>
          The OCI reference to pull and monitor for changes,
defaults to the latest tag.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecocisecretref">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef contains the secret name containing the registry login
credentials to resolve image metadata.
The secret must be of type kubernetes.io/dockerconfigjson.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>serviceAccountName</b></td>
        <td>string</td>
        <td>
          ServiceAccountName is the name of the Kubernetes ServiceAccount used to authenticate
the image pull if the service account has attached pull secrets. For more information:
https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#add-imagepullsecrets-to-a-service-account<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>suspend</b></td>
        <td>boolean</td>
        <td>
          This flag tells the controller to suspend the reconciliation of this source.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>timeout</b></td>
        <td>string</td>
        <td>
          The timeout for remote OCI Repository operations like pulling, defaults to 60s.<br/>
          <br/>
            <i>Default</i>: 60s<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecociverify">verify</a></b></td>
        <td>object</td>
        <td>
          Verify contains the secret name containing the trusted public keys
used to verify the signature and specifies which provider to use to check
whether OCI image is authentic.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.oci.certSecretRef
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespecoci)</sup></sup>



CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
registry. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

Note: Support for the `caFile`, `certFile` and `keyFile` keys have
been deprecated.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.oci.layerSelector
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespecoci)</sup></sup>



LayerSelector specifies which layer should be extracted from the OCI artifact.
When not specified, the first layer found in the artifact is selected.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>mediaType</b></td>
        <td>string</td>
        <td>
          MediaType specifies the OCI media type of the layer
which should be extracted from the OCI Artifact. The
first layer matching this type is selected.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>operation</b></td>
        <td>enum</td>
        <td>
          Operation specifies how the selected layer should be processed.
By default, the layer compressed content is extracted to storage.
When the operation is set to 'copy', the layer compressed content
is persisted to storage as it is.<br/>
          <br/>
            <i>Enum</i>: extract, copy<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.oci.proxySecretRef
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespecoci)</sup></sup>



ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the container registry.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.oci.ref
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespecoci)</sup></sup>



The OCI reference to pull and monitor for changes,
defaults to the latest tag.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>digest</b></td>
        <td>string</td>
        <td>
          Digest is the image digest to pull, takes precedence over SemVer.
The value should be in the format 'sha256:<HASH>'.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>semver</b></td>
        <td>string</td>
        <td>
          SemVer is the range of tags to pull selecting the latest within
the range, takes precedence over Tag.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>semverFilter</b></td>
        <td>string</td>
        <td>
          SemverFilter is a regex pattern to filter the tags within the SemVer range.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>tag</b></td>
        <td>string</td>
        <td>
          Tag is the image tag to pull, defaults to latest.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.oci.secretRef
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespecoci)</sup></sup>



SecretRef contains the secret name containing the registry login
credentials to resolve image metadata.
The secret must be of type kubernetes.io/dockerconfigjson.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.oci.verify
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespecoci)</sup></sup>



Verify contains the secret name containing the trusted public keys
used to verify the signature and specifies which provider to use to check
whether OCI image is authentic.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider specifies the technology used to sign the OCI Artifact.<br/>
          <br/>
            <i>Enum</i>: cosign, notation<br/>
            <i>Default</i>: cosign<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecociverifymatchoidcidentityindex">matchOIDCIdentity</a></b></td>
        <td>[]object</td>
        <td>
          MatchOIDCIdentity specifies the identity matching criteria to use
while verifying an OCI artifact which was signed using Cosign keyless
signing. The artifact's identity is deemed to be verified if any of the
specified matchers match against the identity.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecociverifysecretref">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Kubernetes Secret containing the
trusted public keys.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.oci.verify.matchOIDCIdentity[index]
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespecociverify)</sup></sup>



OIDCIdentityMatch specifies options for verifying the certificate identity,
i.e. the issuer and the subject of the certificate.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>issuer</b></td>
        <td>string</td>
        <td>
          Issuer specifies the regex pattern to match against to verify
the OIDC issuer in the Fulcio certificate. The pattern must be a
valid Go regular expression.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>subject</b></td>
        <td>string</td>
        <td>
          Subject specifies the regex pattern to match against to verify
the identity subject in the Fulcio certificate. The pattern must
be a valid Go regular expression.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.oci.verify.secretRef
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespecociverify)</sup></sup>



SecretRef specifies the Kubernetes Secret containing the
trusted public keys.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.status
<sup><sup>[↩ Parent](#servicetemplate)</sup></sup>



ServiceTemplateStatus defines the observed state of ServiceTemplate

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>valid</b></td>
        <td>boolean</td>
        <td>
          Valid indicates whether the template passed validation or not.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#servicetemplatestatuschartref">chartRef</a></b></td>
        <td>object</td>
        <td>
          ChartRef is a reference to a source controller resource containing the
Helm chart representing the template.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>chartVersion</b></td>
        <td>string</td>
        <td>
          ChartVersion represents the version of the Helm Chart associated with this template.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>config</b></td>
        <td>JSON</td>
        <td>
          Config demonstrates available parameters for template customization,
that can be used when creating ClusterDeployment objects.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>description</b></td>
        <td>string</td>
        <td>
          Description contains information about the template.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>k8sConstraint</b></td>
        <td>string</td>
        <td>
          Constraint describing compatible K8S versions of the cluster set in the SemVer format.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>observedGeneration</b></td>
        <td>integer</td>
        <td>
          ObservedGeneration is the last observed generation.<br/>
          <br/>
            <i>Format</i>: int64<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatestatussourcestatus">sourceStatus</a></b></td>
        <td>object</td>
        <td>
          SourceStatus reflects the status of the source.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>validationError</b></td>
        <td>string</td>
        <td>
          ValidationError provides information regarding issues encountered during template validation.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.status.chartRef
<sup><sup>[↩ Parent](#servicetemplatestatus)</sup></sup>



ChartRef is a reference to a source controller resource containing the
Helm chart representing the template.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>kind</b></td>
        <td>enum</td>
        <td>
          Kind of the referent.<br/>
          <br/>
            <i>Enum</i>: OCIRepository, HelmChart<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>apiVersion</b></td>
        <td>string</td>
        <td>
          APIVersion of the referent.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace of the referent, defaults to the namespace of the Kubernetes
resource object that contains the reference.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.status.sourceStatus
<sup><sup>[↩ Parent](#servicetemplatestatus)</sup></sup>



SourceStatus reflects the status of the source.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>kind</b></td>
        <td>string</td>
        <td>
          Kind is the kind of the remote source.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name is the name of the remote source.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace is the namespace of the remote source.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#servicetemplatestatussourcestatusartifact">artifact</a></b></td>
        <td>object</td>
        <td>
          Artifact is the artifact that was generated from the template source.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatestatussourcestatusconditionsindex">conditions</a></b></td>
        <td>[]object</td>
        <td>
          Conditions reflects the conditions of the remote source object.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>observedGeneration</b></td>
        <td>integer</td>
        <td>
          ObservedGeneration is the latest source generation observed by the controller.<br/>
          <br/>
            <i>Format</i>: int64<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.status.sourceStatus.artifact
<sup><sup>[↩ Parent](#servicetemplatestatussourcestatus)</sup></sup>



Artifact is the artifact that was generated from the template source.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>lastUpdateTime</b></td>
        <td>string</td>
        <td>
          LastUpdateTime is the timestamp corresponding to the last update of the
Artifact.<br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>path</b></td>
        <td>string</td>
        <td>
          Path is the relative file path of the Artifact. It can be used to locate
the file in the root of the Artifact storage on the local file system of
the controller managing the Source.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>revision</b></td>
        <td>string</td>
        <td>
          Revision is a human-readable identifier traceable in the origin source
system. It can be a Git commit SHA, Git tag, a Helm chart version, etc.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>url</b></td>
        <td>string</td>
        <td>
          URL is the HTTP address of the Artifact as exposed by the controller
managing the Source. It can be used to retrieve the Artifact for
consumption, e.g. by another controller applying the Artifact contents.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>digest</b></td>
        <td>string</td>
        <td>
          Digest is the digest of the file in the form of '<algorithm>:<checksum>'.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>metadata</b></td>
        <td>map[string]string</td>
        <td>
          Metadata holds upstream information such as OCI annotations.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>size</b></td>
        <td>integer</td>
        <td>
          Size is the number of bytes in the file.<br/>
          <br/>
            <i>Format</i>: int64<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.status.sourceStatus.conditions[index]
<sup><sup>[↩ Parent](#servicetemplatestatussourcestatus)</sup></sup>



Condition contains details for one aspect of the current state of this API Resource.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>lastTransitionTime</b></td>
        <td>string</td>
        <td>
          lastTransitionTime is the last time the condition transitioned from one status to another.
This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable.<br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>message</b></td>
        <td>string</td>
        <td>
          message is a human readable message indicating details about the transition.
This may be an empty string.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>reason</b></td>
        <td>string</td>
        <td>
          reason contains a programmatic identifier indicating the reason for the condition's last transition.
Producers of specific condition types may define expected values and meanings for this field,
and whether the values are considered a guaranteed API.
The value should be a CamelCase string.
This field may not be empty.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>status</b></td>
        <td>enum</td>
        <td>
          status of the condition, one of True, False, Unknown.<br/>
          <br/>
            <i>Enum</i>: True, False, Unknown<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>type</b></td>
        <td>string</td>
        <td>
          type of condition in CamelCase or in foo.example.com/CamelCase.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>observedGeneration</b></td>
        <td>integer</td>
        <td>
          observedGeneration represents the .metadata.generation that the condition was set based upon.
For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date
with respect to the current state of the instance.<br/>
          <br/>
            <i>Format</i>: int64<br/>
            <i>Minimum</i>: 0<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>

# k0rdent.mirantis.com/v1beta1

Resource Types:

- [AccessManagement](#accessmanagement)

- [ClusterDeployment](#clusterdeployment)

- [ClusterIPAMClaim](#clusteripamclaim)

- [ClusterIPAM](#clusteripam)

- [ClusterTemplateChain](#clustertemplatechain)

- [ClusterTemplate](#clustertemplate)

- [Credential](#credential)

- [ManagementBackup](#managementbackup)

- [Management](#management)

- [MultiClusterService](#multiclusterservice)

- [ProviderInterface](#providerinterface)

- [ProviderTemplate](#providertemplate)

- [Release](#release)

- [ServiceTemplateChain](#servicetemplatechain)

- [ServiceTemplate](#servicetemplate)




## AccessManagement
<sup><sup>[↩ Parent](#k0rdentmirantiscomv1beta1 )</sup></sup>






AccessManagement is the Schema for the AccessManagements API

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
      <td><b>apiVersion</b></td>
      <td>string</td>
      <td>k0rdent.mirantis.com/v1beta1</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b>kind</b></td>
      <td>string</td>
      <td>AccessManagement</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#accessmanagementspec-1">spec</a></b></td>
        <td>object</td>
        <td>
          AccessManagementSpec defines the desired state of AccessManagement<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#accessmanagementstatus-1">status</a></b></td>
        <td>object</td>
        <td>
          AccessManagementStatus defines the observed state of AccessManagement<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### AccessManagement.spec
<sup><sup>[↩ Parent](#accessmanagement-1)</sup></sup>



AccessManagementSpec defines the desired state of AccessManagement

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#accessmanagementspecaccessrulesindex-1">accessRules</a></b></td>
        <td>[]object</td>
        <td>
          AccessRules is the list of access rules. Each AccessRule enforces
objects distribution to the TargetNamespaces.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### AccessManagement.spec.accessRules[index]
<sup><sup>[↩ Parent](#accessmanagementspec-1)</sup></sup>



AccessRule is the definition of the AccessManagement access rule. Each AccessRule enforces
Templates and Credentials distribution to the TargetNamespaces

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>clusterTemplateChains</b></td>
        <td>[]string</td>
        <td>
          ClusterTemplateChains lists the names of ClusterTemplateChains whose ClusterTemplates
will be distributed to all namespaces specified in TargetNamespaces.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>credentials</b></td>
        <td>[]string</td>
        <td>
          Credentials is the list of Credential names that will be distributed to all the
namespaces specified in TargetNamespaces.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>serviceTemplateChains</b></td>
        <td>[]string</td>
        <td>
          ServiceTemplateChains lists the names of ServiceTemplateChains whose ServiceTemplates
will be distributed to all namespaces specified in TargetNamespaces.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#accessmanagementspecaccessrulesindextargetnamespaces-1">targetNamespaces</a></b></td>
        <td>object</td>
        <td>
          TargetNamespaces defines the namespaces where selected objects will be distributed.
Templates and Credentials will be distributed to all namespaces if unset.<br/>
          <br/>
            <i>Validations</i>:<li>((has(self.stringSelector) ? 1 : 0) + (has(self.selector) ? 1 : 0) + (has(self.list) ? 1 : 0)) <= 1: only one of spec.targetNamespaces.selector or spec.targetNamespaces.stringSelector or spec.targetNamespaces.list can be specified</li>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### AccessManagement.spec.accessRules[index].targetNamespaces
<sup><sup>[↩ Parent](#accessmanagementspecaccessrulesindex-1)</sup></sup>



TargetNamespaces defines the namespaces where selected objects will be distributed.
Templates and Credentials will be distributed to all namespaces if unset.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>list</b></td>
        <td>[]string</td>
        <td>
          List is the list of namespaces to select.
Mutually exclusive with StringSelector and Selector.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#accessmanagementspecaccessrulesindextargetnamespacesselector-1">selector</a></b></td>
        <td>object</td>
        <td>
          Selector is a structured label query to select namespaces.
Mutually exclusive with StringSelector and List.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>stringSelector</b></td>
        <td>string</td>
        <td>
          StringSelector is a label query to select namespaces.
Mutually exclusive with Selector and List.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### AccessManagement.spec.accessRules[index].targetNamespaces.selector
<sup><sup>[↩ Parent](#accessmanagementspecaccessrulesindextargetnamespaces-1)</sup></sup>



Selector is a structured label query to select namespaces.
Mutually exclusive with StringSelector and List.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#accessmanagementspecaccessrulesindextargetnamespacesselectormatchexpressionsindex-1">matchExpressions</a></b></td>
        <td>[]object</td>
        <td>
          matchExpressions is a list of label selector requirements. The requirements are ANDed.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>matchLabels</b></td>
        <td>map[string]string</td>
        <td>
          matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels
map is equivalent to an element of matchExpressions, whose key field is "key", the
operator is "In", and the values array contains only "value". The requirements are ANDed.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### AccessManagement.spec.accessRules[index].targetNamespaces.selector.matchExpressions[index]
<sup><sup>[↩ Parent](#accessmanagementspecaccessrulesindextargetnamespacesselector-1)</sup></sup>



A label selector requirement is a selector that contains values, a key, and an operator that
relates the key and values.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>key</b></td>
        <td>string</td>
        <td>
          key is the label key that the selector applies to.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>operator</b></td>
        <td>string</td>
        <td>
          operator represents a key's relationship to a set of values.
Valid operators are In, NotIn, Exists and DoesNotExist.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>values</b></td>
        <td>[]string</td>
        <td>
          values is an array of string values. If the operator is In or NotIn,
the values array must be non-empty. If the operator is Exists or DoesNotExist,
the values array must be empty. This array is replaced during a strategic
merge patch.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### AccessManagement.status
<sup><sup>[↩ Parent](#accessmanagement-1)</sup></sup>



AccessManagementStatus defines the observed state of AccessManagement

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#accessmanagementstatuscurrentindex-1">current</a></b></td>
        <td>[]object</td>
        <td>
          Current reflects the applied access rules configuration.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>error</b></td>
        <td>string</td>
        <td>
          Error is the error message occurred during the reconciliation (if any)<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>observedGeneration</b></td>
        <td>integer</td>
        <td>
          ObservedGeneration is the last observed generation.<br/>
          <br/>
            <i>Format</i>: int64<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### AccessManagement.status.current[index]
<sup><sup>[↩ Parent](#accessmanagementstatus-1)</sup></sup>



AccessRule is the definition of the AccessManagement access rule. Each AccessRule enforces
Templates and Credentials distribution to the TargetNamespaces

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>clusterTemplateChains</b></td>
        <td>[]string</td>
        <td>
          ClusterTemplateChains lists the names of ClusterTemplateChains whose ClusterTemplates
will be distributed to all namespaces specified in TargetNamespaces.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>credentials</b></td>
        <td>[]string</td>
        <td>
          Credentials is the list of Credential names that will be distributed to all the
namespaces specified in TargetNamespaces.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>serviceTemplateChains</b></td>
        <td>[]string</td>
        <td>
          ServiceTemplateChains lists the names of ServiceTemplateChains whose ServiceTemplates
will be distributed to all namespaces specified in TargetNamespaces.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#accessmanagementstatuscurrentindextargetnamespaces-1">targetNamespaces</a></b></td>
        <td>object</td>
        <td>
          TargetNamespaces defines the namespaces where selected objects will be distributed.
Templates and Credentials will be distributed to all namespaces if unset.<br/>
          <br/>
            <i>Validations</i>:<li>((has(self.stringSelector) ? 1 : 0) + (has(self.selector) ? 1 : 0) + (has(self.list) ? 1 : 0)) <= 1: only one of spec.targetNamespaces.selector or spec.targetNamespaces.stringSelector or spec.targetNamespaces.list can be specified</li>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### AccessManagement.status.current[index].targetNamespaces
<sup><sup>[↩ Parent](#accessmanagementstatuscurrentindex-1)</sup></sup>



TargetNamespaces defines the namespaces where selected objects will be distributed.
Templates and Credentials will be distributed to all namespaces if unset.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>list</b></td>
        <td>[]string</td>
        <td>
          List is the list of namespaces to select.
Mutually exclusive with StringSelector and Selector.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#accessmanagementstatuscurrentindextargetnamespacesselector-1">selector</a></b></td>
        <td>object</td>
        <td>
          Selector is a structured label query to select namespaces.
Mutually exclusive with StringSelector and List.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>stringSelector</b></td>
        <td>string</td>
        <td>
          StringSelector is a label query to select namespaces.
Mutually exclusive with Selector and List.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### AccessManagement.status.current[index].targetNamespaces.selector
<sup><sup>[↩ Parent](#accessmanagementstatuscurrentindextargetnamespaces-1)</sup></sup>



Selector is a structured label query to select namespaces.
Mutually exclusive with StringSelector and List.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#accessmanagementstatuscurrentindextargetnamespacesselectormatchexpressionsindex-1">matchExpressions</a></b></td>
        <td>[]object</td>
        <td>
          matchExpressions is a list of label selector requirements. The requirements are ANDed.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>matchLabels</b></td>
        <td>map[string]string</td>
        <td>
          matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels
map is equivalent to an element of matchExpressions, whose key field is "key", the
operator is "In", and the values array contains only "value". The requirements are ANDed.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### AccessManagement.status.current[index].targetNamespaces.selector.matchExpressions[index]
<sup><sup>[↩ Parent](#accessmanagementstatuscurrentindextargetnamespacesselector-1)</sup></sup>



A label selector requirement is a selector that contains values, a key, and an operator that
relates the key and values.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>key</b></td>
        <td>string</td>
        <td>
          key is the label key that the selector applies to.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>operator</b></td>
        <td>string</td>
        <td>
          operator represents a key's relationship to a set of values.
Valid operators are In, NotIn, Exists and DoesNotExist.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>values</b></td>
        <td>[]string</td>
        <td>
          values is an array of string values. If the operator is In or NotIn,
the values array must be non-empty. If the operator is Exists or DoesNotExist,
the values array must be empty. This array is replaced during a strategic
merge patch.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>

## ClusterDeployment
<sup><sup>[↩ Parent](#k0rdentmirantiscomv1beta1 )</sup></sup>






ClusterDeployment is the Schema for the ClusterDeployments API

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
      <td><b>apiVersion</b></td>
      <td>string</td>
      <td>k0rdent.mirantis.com/v1beta1</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b>kind</b></td>
      <td>string</td>
      <td>ClusterDeployment</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#clusterdeploymentspec-1">spec</a></b></td>
        <td>object</td>
        <td>
          ClusterDeploymentSpec defines the desired state of ClusterDeployment<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clusterdeploymentstatus-1">status</a></b></td>
        <td>object</td>
        <td>
          ClusterDeploymentStatus defines the observed state of ClusterDeployment<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.spec
<sup><sup>[↩ Parent](#clusterdeployment-1)</sup></sup>



ClusterDeploymentSpec defines the desired state of ClusterDeployment

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>template</b></td>
        <td>string</td>
        <td>
          Template is a reference to a Template object located in the same namespace.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>config</b></td>
        <td>JSON</td>
        <td>
          Config allows to provide parameters for template customization.
If no Config provided, the field will be populated with the default values for
the template and DryRun will be enabled.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>credential</b></td>
        <td>string</td>
        <td>
          Name reference to the related Credentials object.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>dryRun</b></td>
        <td>boolean</td>
        <td>
          DryRun specifies whether the template should be applied after validation or only validated.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clusterdeploymentspecipamclaim">ipamClaim</a></b></td>
        <td>object</td>
        <td>
          IPAMClaim defines IP Address Management (IPAM) requirements for the cluster.
It can either reference an existing IPAM claim or specify an inline claim.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>propagateCredentials</b></td>
        <td>boolean</td>
        <td>
          PropagateCredentials indicates whether credentials should be propagated
for use by CCM (Cloud Controller Manager).<br/>
          <br/>
            <i>Default</i>: true<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clusterdeploymentspecservicespec-1">serviceSpec</a></b></td>
        <td>object</td>
        <td>
          ServiceSpec is spec related to deployment of services.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.spec.ipamClaim
<sup><sup>[↩ Parent](#clusterdeploymentspec-1)</sup></sup>



IPAMClaim defines IP Address Management (IPAM) requirements for the cluster.
It can either reference an existing IPAM claim or specify an inline claim.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>ref</b></td>
        <td>string</td>
        <td>
          ClusterIPAMClaimRef is the name of an existing ClusterIPAMClaim resource to use.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clusterdeploymentspecipamclaimspec">spec</a></b></td>
        <td>object</td>
        <td>
          ClusterIPAMClaimSpec defines the inline IPAM claim specification if no reference is provided.
This allows for dynamic IP address allocation during cluster provisioning.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.spec.ipamClaim.spec
<sup><sup>[↩ Parent](#clusterdeploymentspecipamclaim)</sup></sup>



ClusterIPAMClaimSpec defines the inline IPAM claim specification if no reference is provided.
This allows for dynamic IP address allocation during cluster provisioning.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider is the name of the provider that this claim will be consumed by<br/>
          <br/>
            <i>Enum</i>: in-cluster, ipam-infoblox<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>cluster</b></td>
        <td>string</td>
        <td>
          Cluster is the reference to the [ClusterDeployment] that this claim is for<br/>
          <br/>
            <i>Validations</i>:<li>oldSelf == '' || self == oldSelf: Cluster reference is immutable once set</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>clusterIPAMRef</b></td>
        <td>string</td>
        <td>
          ClusterIPAMRef is the reference to the [ClusterIPAM] resource that this claim is for<br/>
          <br/>
            <i>Validations</i>:<li>oldSelf == '' || self == oldSelf: ClusterIPAM reference is immutable once set</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clusterdeploymentspecipamclaimspecclusternetwork">clusterNetwork</a></b></td>
        <td>object</td>
        <td>
          ClusterNetwork defines the allocation for requisitioning ip addresses for use by the k8s cluster itself<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clusterdeploymentspecipamclaimspecexternalnetwork">externalNetwork</a></b></td>
        <td>object</td>
        <td>
          ExternalNetwork defines the allocation for requisitioning ip addresses for use by services such as load balancers<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clusterdeploymentspecipamclaimspecnodenetwork">nodeNetwork</a></b></td>
        <td>object</td>
        <td>
          NodeNetwork defines the allocation requisitioning ip addresses for cluster nodes<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.spec.ipamClaim.spec.clusterNetwork
<sup><sup>[↩ Parent](#clusterdeploymentspecipamclaimspec)</sup></sup>



ClusterNetwork defines the allocation for requisitioning ip addresses for use by the k8s cluster itself

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>cidr</b></td>
        <td>string</td>
        <td>
          CIDR notation of the allocated address space<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>ipAddresses</b></td>
        <td>[]string</td>
        <td>
          IPAddresses to be allocated<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.spec.ipamClaim.spec.externalNetwork
<sup><sup>[↩ Parent](#clusterdeploymentspecipamclaimspec)</sup></sup>



ExternalNetwork defines the allocation for requisitioning ip addresses for use by services such as load balancers

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>cidr</b></td>
        <td>string</td>
        <td>
          CIDR notation of the allocated address space<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>ipAddresses</b></td>
        <td>[]string</td>
        <td>
          IPAddresses to be allocated<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.spec.ipamClaim.spec.nodeNetwork
<sup><sup>[↩ Parent](#clusterdeploymentspecipamclaimspec)</sup></sup>



NodeNetwork defines the allocation requisitioning ip addresses for cluster nodes

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>cidr</b></td>
        <td>string</td>
        <td>
          CIDR notation of the allocated address space<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>ipAddresses</b></td>
        <td>[]string</td>
        <td>
          IPAddresses to be allocated<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.spec.serviceSpec
<sup><sup>[↩ Parent](#clusterdeploymentspec-1)</sup></sup>



ServiceSpec is spec related to deployment of services.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>continueOnError</b></td>
        <td>boolean</td>
        <td>
          ContinueOnError specifies if the services deployment should continue if an error occurs.<br/>
          <br/>
            <i>Default</i>: false<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clusterdeploymentspecservicespecdriftexclusionsindex-1">driftExclusions</a></b></td>
        <td>[]object</td>
        <td>
          DriftExclusions specifies specific configurations of resources to ignore for drift detection.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clusterdeploymentspecservicespecdriftignoreindex-1">driftIgnore</a></b></td>
        <td>[]object</td>
        <td>
          DriftIgnore specifies resources to ignore for drift detection.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>priority</b></td>
        <td>integer</td>
        <td>
          Priority sets the priority for the services defined in this spec.
Higher value means higher priority and lower means lower.
In case of conflict with another object managing the service,
the one with higher priority will get to deploy its services.<br/>
          <br/>
            <i>Format</i>: int32<br/>
            <i>Default</i>: 100<br/>
            <i>Minimum</i>: 1<br/>
            <i>Maximum</i>: 2.147483646e+09<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>reload</b></td>
        <td>boolean</td>
        <td>
          Reload instances via rolling upgrade when a ConfigMap/Secret mounted as volume is modified.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clusterdeploymentspecservicespecservicesindex-1">services</a></b></td>
        <td>[]object</td>
        <td>
          Services is a list of services created via ServiceTemplates
that could be installed on the target cluster.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>stopOnConflict</b></td>
        <td>boolean</td>
        <td>
          StopOnConflict specifies what to do in case of a conflict.
E.g. If another object is already managing a service.
By default the remaining services will be deployed even if conflict is detected.
If set to true, the deployment will stop after encountering the first conflict.<br/>
          <br/>
            <i>Default</i>: false<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>syncMode</b></td>
        <td>enum</td>
        <td>
          SyncMode specifies how services are synced in the target cluster.<br/>
          <br/>
            <i>Enum</i>: OneTime, Continuous, ContinuousWithDriftDetection, DryRun<br/>
            <i>Default</i>: Continuous<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clusterdeploymentspecservicespectemplateresourcerefsindex-1">templateResourceRefs</a></b></td>
        <td>[]object</td>
        <td>
          TemplateResourceRefs is a list of resources to collect from the management cluster,
the values from which can be used in templates.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.spec.serviceSpec.driftExclusions[index]
<sup><sup>[↩ Parent](#clusterdeploymentspecservicespec-1)</sup></sup>





<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>paths</b></td>
        <td>[]string</td>
        <td>
          Paths is a slice of JSON6902 paths to exclude from configuration drift evaluation.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#clusterdeploymentspecservicespecdriftexclusionsindextarget-1">target</a></b></td>
        <td>object</td>
        <td>
          Target points to the resources that the paths refers to.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.spec.serviceSpec.driftExclusions[index].target
<sup><sup>[↩ Parent](#clusterdeploymentspecservicespecdriftexclusionsindex-1)</sup></sup>



Target points to the resources that the paths refers to.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>annotationSelector</b></td>
        <td>string</td>
        <td>
          AnnotationSelector is a string that follows the label selection expression
https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#api
It matches with the resource annotations.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>group</b></td>
        <td>string</td>
        <td>
          Group is the API group to select resources from.
Together with Version and Kind it is capable of unambiguously identifying and/or selecting resources.
https://github.com/kubernetes/community/blob/master/contributors/design-proposals/api-machinery/api-group.md<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>kind</b></td>
        <td>string</td>
        <td>
          Kind of the API Group to select resources from.
Together with Group and Version it is capable of unambiguously
identifying and/or selecting resources.
https://github.com/kubernetes/community/blob/master/contributors/design-proposals/api-machinery/api-group.md<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>labelSelector</b></td>
        <td>string</td>
        <td>
          LabelSelector is a string that follows the label selection expression
https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#api
It matches with the resource labels.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name to match resources with.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace to select resources from.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>version</b></td>
        <td>string</td>
        <td>
          Version of the API Group to select resources from.
Together with Group and Kind it is capable of unambiguously identifying and/or selecting resources.
https://github.com/kubernetes/community/blob/master/contributors/design-proposals/api-machinery/api-group.md<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.spec.serviceSpec.driftIgnore[index]
<sup><sup>[↩ Parent](#clusterdeploymentspecservicespec-1)</sup></sup>





<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>annotationSelector</b></td>
        <td>string</td>
        <td>
          AnnotationSelector is a string that follows the label selection expression
https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#api
It matches with the resource annotations.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>group</b></td>
        <td>string</td>
        <td>
          Group is the API group to select resources from.
Together with Version and Kind it is capable of unambiguously identifying and/or selecting resources.
https://github.com/kubernetes/community/blob/master/contributors/design-proposals/api-machinery/api-group.md<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>kind</b></td>
        <td>string</td>
        <td>
          Kind of the API Group to select resources from.
Together with Group and Version it is capable of unambiguously
identifying and/or selecting resources.
https://github.com/kubernetes/community/blob/master/contributors/design-proposals/api-machinery/api-group.md<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>labelSelector</b></td>
        <td>string</td>
        <td>
          LabelSelector is a string that follows the label selection expression
https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#api
It matches with the resource labels.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name to match resources with.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace to select resources from.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>version</b></td>
        <td>string</td>
        <td>
          Version of the API Group to select resources from.
Together with Group and Kind it is capable of unambiguously identifying and/or selecting resources.
https://github.com/kubernetes/community/blob/master/contributors/design-proposals/api-machinery/api-group.md<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.spec.serviceSpec.services[index]
<sup><sup>[↩ Parent](#clusterdeploymentspecservicespec-1)</sup></sup>



Service represents a Service to be deployed.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name is the chart release.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>template</b></td>
        <td>string</td>
        <td>
          Template is a reference to a Template object located in the same namespace.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>disable</b></td>
        <td>boolean</td>
        <td>
          Disable can be set to disable handling of this service.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace is the namespace the release will be installed in.
It will default to Name if not provided.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>templateChain</b></td>
        <td>string</td>
        <td>
          TemplateChain defines the ServiceTemplateChain object that will be used to deploy the service
along with desired ServiceTemplate version.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>values</b></td>
        <td>string</td>
        <td>
          Values is the helm values to be passed to the chart used by the template.
The string type is used in order to allow for templating.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clusterdeploymentspecservicespecservicesindexvaluesfromindex-1">valuesFrom</a></b></td>
        <td>[]object</td>
        <td>
          ValuesFrom can reference a ConfigMap or Secret containing helm values.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.spec.serviceSpec.services[index].valuesFrom[index]
<sup><sup>[↩ Parent](#clusterdeploymentspecservicespecservicesindex-1)</sup></sup>





<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>kind</b></td>
        <td>enum</td>
        <td>
          Kind of the resource. Supported kinds are:
- ConfigMap/Secret<br/>
          <br/>
            <i>Enum</i>: ConfigMap, Secret<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referenced resource.
Name can be expressed as a template and instantiate using any cluster field.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace of the referenced resource.
For ClusterProfile namespace can be left empty. In such a case, namespace will
be implicit set to cluster's namespace.
For Profile namespace must be left empty. The Profile namespace will be used.
Namespace can be expressed as a template and instantiate using any cluster field.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>optional</b></td>
        <td>boolean</td>
        <td>
          Optional indicates that the referenced resource is not mandatory.
If set to true and the resource is not found, the error will be ignored,
and Sveltos will continue processing other ValueFroms.<br/>
          <br/>
            <i>Default</i>: false<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.spec.serviceSpec.templateResourceRefs[index]
<sup><sup>[↩ Parent](#clusterdeploymentspecservicespec-1)</sup></sup>





<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>identifier</b></td>
        <td>string</td>
        <td>
          Identifier is how the resource will be referred to in the
template<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#clusterdeploymentspecservicespectemplateresourcerefsindexresource-1">resource</a></b></td>
        <td>object</td>
        <td>
          Resource references a Kubernetes instance in the management
cluster to fetch and use during template instantiation.
For ClusterProfile namespace can be left empty. In such a case, namespace will
be implicit set to cluster's namespace.
Name and namespace can be expressed as a template and instantiate using any cluster field.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>optional</b></td>
        <td>boolean</td>
        <td>
          Optional indicates that the referenced resource is not mandatory.
If set to true and the resource is not found, the error will be ignored,
and Sveltos will continue processing other TemplateResourceRefs.<br/>
          <br/>
            <i>Default</i>: false<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.spec.serviceSpec.templateResourceRefs[index].resource
<sup><sup>[↩ Parent](#clusterdeploymentspecservicespectemplateresourcerefsindex-1)</sup></sup>



Resource references a Kubernetes instance in the management
cluster to fetch and use during template instantiation.
For ClusterProfile namespace can be left empty. In such a case, namespace will
be implicit set to cluster's namespace.
Name and namespace can be expressed as a template and instantiate using any cluster field.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>apiVersion</b></td>
        <td>string</td>
        <td>
          API version of the referent.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>fieldPath</b></td>
        <td>string</td>
        <td>
          If referring to a piece of an object instead of an entire object, this string
should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2].
For example, if the object reference is to a container within a pod, this would take on a value like:
"spec.containers{name}" (where "name" refers to the name of the container that triggered
the event) or if no container name is specified "spec.containers[2]" (container with
index 2 in this pod). This syntax is chosen only to have some well-defined way of
referencing a part of an object.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>kind</b></td>
        <td>string</td>
        <td>
          Kind of the referent.
More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.
More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace of the referent.
More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>resourceVersion</b></td>
        <td>string</td>
        <td>
          Specific resourceVersion to which this reference is made, if any.
More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>uid</b></td>
        <td>string</td>
        <td>
          UID of the referent.
More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.status
<sup><sup>[↩ Parent](#clusterdeployment-1)</sup></sup>



ClusterDeploymentStatus defines the observed state of ClusterDeployment

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>availableUpgrades</b></td>
        <td>[]string</td>
        <td>
          AvailableUpgrades is the list of ClusterTemplate names to which
this cluster can be upgraded. It can be an empty array, which means no upgrades are
available.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clusterdeploymentstatusconditionsindex-1">conditions</a></b></td>
        <td>[]object</td>
        <td>
          Conditions contains details for the current state of the ClusterDeployment.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>k8sVersion</b></td>
        <td>string</td>
        <td>
          Currently compatible exact Kubernetes version of the cluster. Being set only if
provided by the corresponding ClusterTemplate.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>observedGeneration</b></td>
        <td>integer</td>
        <td>
          ObservedGeneration is the last observed generation.<br/>
          <br/>
            <i>Format</i>: int64<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clusterdeploymentstatusservicesindex-1">services</a></b></td>
        <td>[]object</td>
        <td>
          Services contains details for the state of services.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clusterdeploymentstatusservicesupgradepathsindex-1">servicesUpgradePaths</a></b></td>
        <td>[]object</td>
        <td>
          ServicesUpgradePaths contains details for the state of services upgrade paths.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.status.conditions[index]
<sup><sup>[↩ Parent](#clusterdeploymentstatus-1)</sup></sup>



Condition contains details for one aspect of the current state of this API Resource.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>lastTransitionTime</b></td>
        <td>string</td>
        <td>
          lastTransitionTime is the last time the condition transitioned from one status to another.
This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable.<br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>message</b></td>
        <td>string</td>
        <td>
          message is a human readable message indicating details about the transition.
This may be an empty string.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>reason</b></td>
        <td>string</td>
        <td>
          reason contains a programmatic identifier indicating the reason for the condition's last transition.
Producers of specific condition types may define expected values and meanings for this field,
and whether the values are considered a guaranteed API.
The value should be a CamelCase string.
This field may not be empty.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>status</b></td>
        <td>enum</td>
        <td>
          status of the condition, one of True, False, Unknown.<br/>
          <br/>
            <i>Enum</i>: True, False, Unknown<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>type</b></td>
        <td>string</td>
        <td>
          type of condition in CamelCase or in foo.example.com/CamelCase.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>observedGeneration</b></td>
        <td>integer</td>
        <td>
          observedGeneration represents the .metadata.generation that the condition was set based upon.
For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date
with respect to the current state of the instance.<br/>
          <br/>
            <i>Format</i>: int64<br/>
            <i>Minimum</i>: 0<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.status.services[index]
<sup><sup>[↩ Parent](#clusterdeploymentstatus-1)</sup></sup>



ServiceStatus contains details for the state of services.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>clusterName</b></td>
        <td>string</td>
        <td>
          ClusterName is the name of the associated cluster.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>clusterNamespace</b></td>
        <td>string</td>
        <td>
          ClusterNamespace is the namespace of the associated cluster.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clusterdeploymentstatusservicesindexconditionsindex-1">conditions</a></b></td>
        <td>[]object</td>
        <td>
          Conditions contains details for the current state of managed services.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.status.services[index].conditions[index]
<sup><sup>[↩ Parent](#clusterdeploymentstatusservicesindex-1)</sup></sup>



Condition contains details for one aspect of the current state of this API Resource.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>lastTransitionTime</b></td>
        <td>string</td>
        <td>
          lastTransitionTime is the last time the condition transitioned from one status to another.
This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable.<br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>message</b></td>
        <td>string</td>
        <td>
          message is a human readable message indicating details about the transition.
This may be an empty string.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>reason</b></td>
        <td>string</td>
        <td>
          reason contains a programmatic identifier indicating the reason for the condition's last transition.
Producers of specific condition types may define expected values and meanings for this field,
and whether the values are considered a guaranteed API.
The value should be a CamelCase string.
This field may not be empty.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>status</b></td>
        <td>enum</td>
        <td>
          status of the condition, one of True, False, Unknown.<br/>
          <br/>
            <i>Enum</i>: True, False, Unknown<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>type</b></td>
        <td>string</td>
        <td>
          type of condition in CamelCase or in foo.example.com/CamelCase.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>observedGeneration</b></td>
        <td>integer</td>
        <td>
          observedGeneration represents the .metadata.generation that the condition was set based upon.
For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date
with respect to the current state of the instance.<br/>
          <br/>
            <i>Format</i>: int64<br/>
            <i>Minimum</i>: 0<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.status.servicesUpgradePaths[index]
<sup><sup>[↩ Parent](#clusterdeploymentstatus-1)</sup></sup>



ServiceUpgradePaths contains details for the state of service upgrade paths.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name is the name of the service.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace is the namespace of the service.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>template</b></td>
        <td>string</td>
        <td>
          Template is the name of the current service template.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#clusterdeploymentstatusservicesupgradepathsindexavailableupgradesindex-1">availableUpgrades</a></b></td>
        <td>[]object</td>
        <td>
          AvailableUpgrades contains details for the state of available upgrades.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.status.servicesUpgradePaths[index].availableUpgrades[index]
<sup><sup>[↩ Parent](#clusterdeploymentstatusservicesupgradepathsindex-1)</sup></sup>



UpgradePath contains details for the state of service upgrade paths.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>upgradePaths</b></td>
        <td>[]string</td>
        <td>
          Versions contains the list of versions that service can be upgraded to.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>

## ClusterIPAMClaim
<sup><sup>[↩ Parent](#k0rdentmirantiscomv1beta1 )</sup></sup>






ClusterIPAMClaim is the Schema for the clusteripamclaims API

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
      <td><b>apiVersion</b></td>
      <td>string</td>
      <td>k0rdent.mirantis.com/v1beta1</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b>kind</b></td>
      <td>string</td>
      <td>ClusterIPAMClaim</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#clusteripamclaimspec">spec</a></b></td>
        <td>object</td>
        <td>
          ClusterIPAMClaimSpec defines the desired state of ClusterIPAMClaim<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clusteripamclaimstatus">status</a></b></td>
        <td>object</td>
        <td>
          ClusterIPAMClaimStatus defines the observed state of ClusterIPAMClaim<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterIPAMClaim.spec
<sup><sup>[↩ Parent](#clusteripamclaim)</sup></sup>



ClusterIPAMClaimSpec defines the desired state of ClusterIPAMClaim

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider is the name of the provider that this claim will be consumed by<br/>
          <br/>
            <i>Enum</i>: in-cluster, ipam-infoblox<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>cluster</b></td>
        <td>string</td>
        <td>
          Cluster is the reference to the [ClusterDeployment] that this claim is for<br/>
          <br/>
            <i>Validations</i>:<li>oldSelf == '' || self == oldSelf: Cluster reference is immutable once set</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>clusterIPAMRef</b></td>
        <td>string</td>
        <td>
          ClusterIPAMRef is the reference to the [ClusterIPAM] resource that this claim is for<br/>
          <br/>
            <i>Validations</i>:<li>oldSelf == '' || self == oldSelf: ClusterIPAM reference is immutable once set</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clusteripamclaimspecclusternetwork">clusterNetwork</a></b></td>
        <td>object</td>
        <td>
          ClusterNetwork defines the allocation for requisitioning ip addresses for use by the k8s cluster itself<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clusteripamclaimspecexternalnetwork">externalNetwork</a></b></td>
        <td>object</td>
        <td>
          ExternalNetwork defines the allocation for requisitioning ip addresses for use by services such as load balancers<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clusteripamclaimspecnodenetwork">nodeNetwork</a></b></td>
        <td>object</td>
        <td>
          NodeNetwork defines the allocation requisitioning ip addresses for cluster nodes<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterIPAMClaim.spec.clusterNetwork
<sup><sup>[↩ Parent](#clusteripamclaimspec)</sup></sup>



ClusterNetwork defines the allocation for requisitioning ip addresses for use by the k8s cluster itself

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>cidr</b></td>
        <td>string</td>
        <td>
          CIDR notation of the allocated address space<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>ipAddresses</b></td>
        <td>[]string</td>
        <td>
          IPAddresses to be allocated<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterIPAMClaim.spec.externalNetwork
<sup><sup>[↩ Parent](#clusteripamclaimspec)</sup></sup>



ExternalNetwork defines the allocation for requisitioning ip addresses for use by services such as load balancers

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>cidr</b></td>
        <td>string</td>
        <td>
          CIDR notation of the allocated address space<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>ipAddresses</b></td>
        <td>[]string</td>
        <td>
          IPAddresses to be allocated<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterIPAMClaim.spec.nodeNetwork
<sup><sup>[↩ Parent](#clusteripamclaimspec)</sup></sup>



NodeNetwork defines the allocation requisitioning ip addresses for cluster nodes

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>cidr</b></td>
        <td>string</td>
        <td>
          CIDR notation of the allocated address space<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>ipAddresses</b></td>
        <td>[]string</td>
        <td>
          IPAddresses to be allocated<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterIPAMClaim.status
<sup><sup>[↩ Parent](#clusteripamclaim)</sup></sup>



ClusterIPAMClaimStatus defines the observed state of ClusterIPAMClaim

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>bound</b></td>
        <td>boolean</td>
        <td>
          Bound is a flag to indicate that the claim is bound because all ip addresses are allocated<br/>
          <br/>
            <i>Default</i>: false<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#clusteripamclaimstatusconditionsindex">conditions</a></b></td>
        <td>[]object</td>
        <td>
          Conditions contains details for the current state of the [ClusterIPAMClaim]<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterIPAMClaim.status.conditions[index]
<sup><sup>[↩ Parent](#clusteripamclaimstatus)</sup></sup>



Condition contains details for one aspect of the current state of this API Resource.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>lastTransitionTime</b></td>
        <td>string</td>
        <td>
          lastTransitionTime is the last time the condition transitioned from one status to another.
This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable.<br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>message</b></td>
        <td>string</td>
        <td>
          message is a human readable message indicating details about the transition.
This may be an empty string.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>reason</b></td>
        <td>string</td>
        <td>
          reason contains a programmatic identifier indicating the reason for the condition's last transition.
Producers of specific condition types may define expected values and meanings for this field,
and whether the values are considered a guaranteed API.
The value should be a CamelCase string.
This field may not be empty.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>status</b></td>
        <td>enum</td>
        <td>
          status of the condition, one of True, False, Unknown.<br/>
          <br/>
            <i>Enum</i>: True, False, Unknown<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>type</b></td>
        <td>string</td>
        <td>
          type of condition in CamelCase or in foo.example.com/CamelCase.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>observedGeneration</b></td>
        <td>integer</td>
        <td>
          observedGeneration represents the .metadata.generation that the condition was set based upon.
For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date
with respect to the current state of the instance.<br/>
          <br/>
            <i>Format</i>: int64<br/>
            <i>Minimum</i>: 0<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>

## ClusterIPAM
<sup><sup>[↩ Parent](#k0rdentmirantiscomv1beta1 )</sup></sup>






ClusterIPAM is the Schema for the clusteripams API

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
      <td><b>apiVersion</b></td>
      <td>string</td>
      <td>k0rdent.mirantis.com/v1beta1</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b>kind</b></td>
      <td>string</td>
      <td>ClusterIPAM</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#clusteripamspec">spec</a></b></td>
        <td>object</td>
        <td>
          ClusterIPAMSpec defines the desired state of ClusterIPAM<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clusteripamstatus">status</a></b></td>
        <td>object</td>
        <td>
          ClusterIPAMStatus defines the observed state of ClusterIPAM<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterIPAM.spec
<sup><sup>[↩ Parent](#clusteripam)</sup></sup>



ClusterIPAMSpec defines the desired state of ClusterIPAM

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>clusterIPAMClaimRef</b></td>
        <td>string</td>
        <td>
          ClusterIPAMClaimRef is a reference to the [ClusterIPAMClaim] that this [ClusterIPAM] is bound to.<br/>
          <br/>
            <i>Validations</i>:<li>oldSelf == '' || self == oldSelf: Claim reference is immutable once set</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          The provider that this claim will be consumed by<br/>
          <br/>
            <i>Enum</i>: in-cluster, ipam-infoblox<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterIPAM.status
<sup><sup>[↩ Parent](#clusteripam)</sup></sup>



ClusterIPAMStatus defines the observed state of ClusterIPAM

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>phase</b></td>
        <td>enum</td>
        <td>
          Phase is the current phase of the ClusterIPAM.<br/>
          <br/>
            <i>Enum</i>: Pending, Bound<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clusteripamstatusproviderdataindex">providerData</a></b></td>
        <td>[]object</td>
        <td>
          ProviderData is the provider specific data produced for the ClusterIPAM.
This field is represented as a list, because it will store multiple entries
for different networks - nodes, cluster (pods, services), external - for
the same provider.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterIPAM.status.providerData[index]
<sup><sup>[↩ Parent](#clusteripamstatus)</sup></sup>





<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>config</b></td>
        <td>JSON</td>
        <td>
          Data is the IPAM provider specific data<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the IPAM provider data<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>ready</b></td>
        <td>boolean</td>
        <td>
          Ready indicates that the IPAM provider data is ready<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>

## ClusterTemplateChain
<sup><sup>[↩ Parent](#k0rdentmirantiscomv1beta1 )</sup></sup>






ClusterTemplateChain is the Schema for the clustertemplatechains API

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
      <td><b>apiVersion</b></td>
      <td>string</td>
      <td>k0rdent.mirantis.com/v1beta1</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b>kind</b></td>
      <td>string</td>
      <td>ClusterTemplateChain</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#clustertemplatechainspec-1">spec</a></b></td>
        <td>object</td>
        <td>
          TemplateChainSpec defines the desired state of *TemplateChain<br/>
          <br/>
            <i>Validations</i>:<li>self == oldSelf: Spec is immutable</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatechainstatus-1">status</a></b></td>
        <td>object</td>
        <td>
          TemplateChainStatus defines the observed state of *TemplateChain<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplateChain.spec
<sup><sup>[↩ Parent](#clustertemplatechain-1)</sup></sup>



TemplateChainSpec defines the desired state of *TemplateChain

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#clustertemplatechainspecsupportedtemplatesindex-1">supportedTemplates</a></b></td>
        <td>[]object</td>
        <td>
          SupportedTemplates is the list of supported Templates definitions and all available upgrade sequences for it.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplateChain.spec.supportedTemplates[index]
<sup><sup>[↩ Parent](#clustertemplatechainspec-1)</sup></sup>



SupportedTemplate is the supported Template definition and all available upgrade sequences for it

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name is the name of the Template.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#clustertemplatechainspecsupportedtemplatesindexavailableupgradesindex-1">availableUpgrades</a></b></td>
        <td>[]object</td>
        <td>
          AvailableUpgrades is the list of available upgrades for the specified Template.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplateChain.spec.supportedTemplates[index].availableUpgrades[index]
<sup><sup>[↩ Parent](#clustertemplatechainspecsupportedtemplatesindex-1)</sup></sup>



AvailableUpgrade is the definition of the available upgrade for the Template

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name is the name of the Template to which the upgrade is available.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ClusterTemplateChain.status
<sup><sup>[↩ Parent](#clustertemplatechain-1)</sup></sup>



TemplateChainStatus defines the observed state of *TemplateChain

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>valid</b></td>
        <td>boolean</td>
        <td>
          Valid indicates whether the chain is valid and can be considered when calculating available
upgrade paths.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>validationError</b></td>
        <td>string</td>
        <td>
          ValidationError provides information regarding issues encountered during templatechain validation.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>

## ClusterTemplate
<sup><sup>[↩ Parent](#k0rdentmirantiscomv1beta1 )</sup></sup>






ClusterTemplate is the Schema for the clustertemplates API

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
      <td><b>apiVersion</b></td>
      <td>string</td>
      <td>k0rdent.mirantis.com/v1beta1</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b>kind</b></td>
      <td>string</td>
      <td>ClusterTemplate</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespec-1">spec</a></b></td>
        <td>object</td>
        <td>
          ClusterTemplateSpec defines the desired state of ClusterTemplate<br/>
          <br/>
            <i>Validations</i>:<li>self == oldSelf: Spec is immutable</li><li>!has(self.helm.chartSource): .spec.helm.chartSource is not supported for ClusterTemplates</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatestatus-1">status</a></b></td>
        <td>object</td>
        <td>
          ClusterTemplateStatus defines the observed state of ClusterTemplate<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec
<sup><sup>[↩ Parent](#clustertemplate-1)</sup></sup>



ClusterTemplateSpec defines the desired state of ClusterTemplate

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#clustertemplatespechelm-1">helm</a></b></td>
        <td>object</td>
        <td>
          HelmSpec references a Helm chart representing the KCM template<br/>
          <br/>
            <i>Validations</i>:<li>(has(self.chartSpec) ? (!has(self.chartSource) && !has(self.chartRef)): true): chartSpec, chartSource and chartRef are mutually exclusive</li><li>(has(self.chartSource) ? (!has(self.chartSpec) && !has(self.chartRef)): true): chartSpec, chartSource and chartRef are mutually exclusive</li><li>(has(self.chartRef) ? (!has(self.chartSpec) && !has(self.chartSource)): true): chartSpec, chartSource and chartRef are mutually exclusive</li><li>has(self.chartSpec) || has(self.chartRef) || has(self.chartSource): one of chartSpec, chartRef or chartSource must be set</li>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>k8sVersion</b></td>
        <td>string</td>
        <td>
          Kubernetes exact version in the SemVer format provided by this ClusterTemplate.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>providerContracts</b></td>
        <td>map[string]string</td>
        <td>
          Holds key-value pairs with compatibility [contract versions],
where the key is the name of the provider,
and the value is the provider contract version
required to be supported by the provider.

[contract versions]: https://cluster-api.sigs.k8s.io/developer/providers/contracts<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>providers</b></td>
        <td>[]string</td>
        <td>
          Providers represent required CAPI providers.
Should be set if not present in the Helm chart metadata.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm
<sup><sup>[↩ Parent](#clustertemplatespec-1)</sup></sup>



HelmSpec references a Helm chart representing the KCM template

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#clustertemplatespechelmchartref-1">chartRef</a></b></td>
        <td>object</td>
        <td>
          ChartRef is a reference to a source controller resource containing the
Helm chart representing the template.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsource-1">chartSource</a></b></td>
        <td>object</td>
        <td>
          ChartSource is a source of a Helm chart representing the template.<br/>
          <br/>
            <i>Validations</i>:<li>has(self.localSourceRef) ? (self.localSourceRef.kind != 'Secret' && self.localSourceRef.kind != 'ConfigMap'): true: Secret and ConfigMap are not supported as Helm chart sources</li><li>has(self.localSourceRef) ? !has(self.remoteSourceSpec): true: LocalSource and RemoteSource are mutually exclusive.</li><li>has(self.remoteSourceSpec) ? !has(self.localSourceRef): true: LocalSource and RemoteSource are mutually exclusive.</li><li>has(self.localSourceRef) || has(self.remoteSourceSpec): One of LocalSource or RemoteSource must be specified.</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartspec-1">chartSpec</a></b></td>
        <td>object</td>
        <td>
          ChartSpec defines the desired state of the HelmChart to be created by the controller<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartRef
<sup><sup>[↩ Parent](#clustertemplatespechelm-1)</sup></sup>



ChartRef is a reference to a source controller resource containing the
Helm chart representing the template.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>kind</b></td>
        <td>enum</td>
        <td>
          Kind of the referent.<br/>
          <br/>
            <i>Enum</i>: OCIRepository, HelmChart<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>apiVersion</b></td>
        <td>string</td>
        <td>
          APIVersion of the referent.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace of the referent, defaults to the namespace of the Kubernetes
resource object that contains the reference.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource
<sup><sup>[↩ Parent](#clustertemplatespechelm-1)</sup></sup>



ChartSource is a source of a Helm chart representing the template.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>deploymentType</b></td>
        <td>enum</td>
        <td>
          DeploymentType is the type of the deployment. This field is ignored,
when ResourceSpec is used as part of Helm chart configuration.<br/>
          <br/>
            <i>Enum</i>: Local, Remote<br/>
            <i>Default</i>: Remote<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>path</b></td>
        <td>string</td>
        <td>
          Path to the directory containing the resource manifest.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourcelocalsourceref-1">localSourceRef</a></b></td>
        <td>object</td>
        <td>
          LocalSourceRef is the local source of the kustomize manifest.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespec-1">remoteSourceSpec</a></b></td>
        <td>object</td>
        <td>
          RemoteSourceSpec is the remote source of the kustomize manifest.<br/>
          <br/>
            <i>Validations</i>:<li>has(self.git) ? (!has(self.bucket) && !has(self.oci)) : true: Git, Bucket and OCI are mutually exclusive.</li><li>has(self.bucket) ? (!has(self.git) && !has(self.oci)) : true: Git, Bucket and OCI are mutually exclusive.</li><li>has(self.oci) ? (!has(self.git) && !has(self.bucket)) : true: Git, Bucket and OCI are mutually exclusive.</li><li>has(self.git) || has(self.bucket) || has(self.oci): One of Git, Bucket or OCI must be specified.</li>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.localSourceRef
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsource-1)</sup></sup>



LocalSourceRef is the local source of the kustomize manifest.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>kind</b></td>
        <td>enum</td>
        <td>
          Kind is the kind of the local source.<br/>
          <br/>
            <i>Enum</i>: ConfigMap, Secret, GitRepository, Bucket, OCIRepository<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name is the name of the local source.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace is the namespace of the local source. Cross-namespace references
are only allowed when the Kind is one of [github.com/fluxcd/source-controller/api/v1.GitRepository],
[github.com/fluxcd/source-controller/api/v1.Bucket] or [github.com/fluxcd/source-controller/api/v1beta2.OCIRepository].
If the Kind is ConfigMap or Secret, the namespace will be ignored.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsource-1)</sup></sup>



RemoteSourceSpec is the remote source of the kustomize manifest.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecbucket-1">bucket</a></b></td>
        <td>object</td>
        <td>
          Bucket is the definition of bucket source.<br/>
          <br/>
            <i>Validations</i>:<li>self.provider == 'aws' || self.provider == 'generic' || !has(self.sts): STS configuration is only supported for the 'aws' and 'generic' Bucket providers</li><li>self.provider != 'aws' || !has(self.sts) || self.sts.provider == 'aws': 'aws' is the only supported STS provider for the 'aws' Bucket provider</li><li>self.provider != 'generic' || !has(self.sts) || self.sts.provider == 'ldap': 'ldap' is the only supported STS provider for the 'generic' Bucket provider</li><li>!has(self.sts) || self.sts.provider != 'aws' || !has(self.sts.secretRef): spec.sts.secretRef is not required for the 'aws' STS provider</li><li>!has(self.sts) || self.sts.provider != 'aws' || !has(self.sts.certSecretRef): spec.sts.certSecretRef is not required for the 'aws' STS provider</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecgit-1">git</a></b></td>
        <td>object</td>
        <td>
          Git is the definition of git repository source.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecoci-1">oci</a></b></td>
        <td>object</td>
        <td>
          OCI is the definition of OCI repository source.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.bucket
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespec-1)</sup></sup>



Bucket is the definition of bucket source.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>bucketName</b></td>
        <td>string</td>
        <td>
          BucketName is the name of the object storage bucket.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>endpoint</b></td>
        <td>string</td>
        <td>
          Endpoint is the object storage address the BucketName is located at.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>interval</b></td>
        <td>string</td>
        <td>
          Interval at which the Bucket Endpoint is checked for updates.
This interval is approximate and may be subject to jitter to ensure
efficient use of resources.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecbucketcertsecretref-1">certSecretRef</a></b></td>
        <td>object</td>
        <td>
          CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
bucket. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

This field is only supported for the `generic` provider.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>ignore</b></td>
        <td>string</td>
        <td>
          Ignore overrides the set of excluded patterns in the .sourceignore format
(which is the same as .gitignore). If not provided, a default will be used,
consult the documentation for your version to find out what those are.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>insecure</b></td>
        <td>boolean</td>
        <td>
          Insecure allows connecting to a non-TLS HTTP Endpoint.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>prefix</b></td>
        <td>string</td>
        <td>
          Prefix to use for server-side filtering of files in the Bucket.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider of the object storage bucket.
Defaults to 'generic', which expects an S3 (API) compatible object
storage.<br/>
          <br/>
            <i>Enum</i>: generic, aws, gcp, azure<br/>
            <i>Default</i>: generic<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecbucketproxysecretref-1">proxySecretRef</a></b></td>
        <td>object</td>
        <td>
          ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the Bucket server.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>region</b></td>
        <td>string</td>
        <td>
          Region of the Endpoint where the BucketName is located in.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecbucketsecretref-1">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing authentication credentials
for the Bucket.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecbucketsts-1">sts</a></b></td>
        <td>object</td>
        <td>
          STS specifies the required configuration to use a Security Token
Service for fetching temporary credentials to authenticate in a
Bucket provider.

This field is only supported for the `aws` and `generic` providers.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>suspend</b></td>
        <td>boolean</td>
        <td>
          Suspend tells the controller to suspend the reconciliation of this
Bucket.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>timeout</b></td>
        <td>string</td>
        <td>
          Timeout for fetch operations, defaults to 60s.<br/>
          <br/>
            <i>Default</i>: 60s<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.bucket.certSecretRef
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespecbucket-1)</sup></sup>



CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
bucket. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

This field is only supported for the `generic` provider.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.bucket.proxySecretRef
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespecbucket-1)</sup></sup>



ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the Bucket server.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.bucket.secretRef
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespecbucket-1)</sup></sup>



SecretRef specifies the Secret containing authentication credentials
for the Bucket.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.bucket.sts
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespecbucket-1)</sup></sup>



STS specifies the required configuration to use a Security Token
Service for fetching temporary credentials to authenticate in a
Bucket provider.

This field is only supported for the `aws` and `generic` providers.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>endpoint</b></td>
        <td>string</td>
        <td>
          Endpoint is the HTTP/S endpoint of the Security Token Service from
where temporary credentials will be fetched.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider of the Security Token Service.<br/>
          <br/>
            <i>Enum</i>: aws, ldap<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecbucketstscertsecretref-1">certSecretRef</a></b></td>
        <td>object</td>
        <td>
          CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
STS endpoint. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

This field is only supported for the `ldap` provider.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecbucketstssecretref-1">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing authentication credentials
for the STS endpoint. This Secret must contain the fields `username`
and `password` and is supported only for the `ldap` provider.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.bucket.sts.certSecretRef
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespecbucketsts-1)</sup></sup>



CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
STS endpoint. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

This field is only supported for the `ldap` provider.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.bucket.sts.secretRef
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespecbucketsts-1)</sup></sup>



SecretRef specifies the Secret containing authentication credentials
for the STS endpoint. This Secret must contain the fields `username`
and `password` and is supported only for the `ldap` provider.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.git
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespec-1)</sup></sup>



Git is the definition of git repository source.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>interval</b></td>
        <td>string</td>
        <td>
          Interval at which the GitRepository URL is checked for updates.
This interval is approximate and may be subject to jitter to ensure
efficient use of resources.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>url</b></td>
        <td>string</td>
        <td>
          URL specifies the Git repository URL, it can be an HTTP/S or SSH address.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>ignore</b></td>
        <td>string</td>
        <td>
          Ignore overrides the set of excluded patterns in the .sourceignore format
(which is the same as .gitignore). If not provided, a default will be used,
consult the documentation for your version to find out what those are.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecgitincludeindex-1">include</a></b></td>
        <td>[]object</td>
        <td>
          Include specifies a list of GitRepository resources which Artifacts
should be included in the Artifact produced for this GitRepository.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider used for authentication, can be 'azure', 'github', 'generic'.
When not specified, defaults to 'generic'.<br/>
          <br/>
            <i>Enum</i>: generic, azure, github<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecgitproxysecretref-1">proxySecretRef</a></b></td>
        <td>object</td>
        <td>
          ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the Git server.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>recurseSubmodules</b></td>
        <td>boolean</td>
        <td>
          RecurseSubmodules enables the initialization of all submodules within
the GitRepository as cloned from the URL, using their default settings.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecgitref-1">ref</a></b></td>
        <td>object</td>
        <td>
          Reference specifies the Git reference to resolve and monitor for
changes, defaults to the 'master' branch.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecgitsecretref-1">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing authentication credentials for
the GitRepository.
For HTTPS repositories the Secret must contain 'username' and 'password'
fields for basic auth or 'bearerToken' field for token auth.
For SSH repositories the Secret must contain 'identity'
and 'known_hosts' fields.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>suspend</b></td>
        <td>boolean</td>
        <td>
          Suspend tells the controller to suspend the reconciliation of this
GitRepository.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>timeout</b></td>
        <td>string</td>
        <td>
          Timeout for Git operations like cloning, defaults to 60s.<br/>
          <br/>
            <i>Default</i>: 60s<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecgitverify-1">verify</a></b></td>
        <td>object</td>
        <td>
          Verification specifies the configuration to verify the Git commit
signature(s).<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.git.include[index]
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespecgit-1)</sup></sup>



GitRepositoryInclude specifies a local reference to a GitRepository which
Artifact (sub-)contents must be included, and where they should be placed.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecgitincludeindexrepository-1">repository</a></b></td>
        <td>object</td>
        <td>
          GitRepositoryRef specifies the GitRepository which Artifact contents
must be included.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>fromPath</b></td>
        <td>string</td>
        <td>
          FromPath specifies the path to copy contents from, defaults to the root
of the Artifact.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>toPath</b></td>
        <td>string</td>
        <td>
          ToPath specifies the path to copy contents to, defaults to the name of
the GitRepositoryRef.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.git.include[index].repository
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespecgitincludeindex-1)</sup></sup>



GitRepositoryRef specifies the GitRepository which Artifact contents
must be included.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.git.proxySecretRef
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespecgit-1)</sup></sup>



ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the Git server.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.git.ref
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespecgit-1)</sup></sup>



Reference specifies the Git reference to resolve and monitor for
changes, defaults to the 'master' branch.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>branch</b></td>
        <td>string</td>
        <td>
          Branch to check out, defaults to 'master' if no other field is defined.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>commit</b></td>
        <td>string</td>
        <td>
          Commit SHA to check out, takes precedence over all reference fields.

This can be combined with Branch to shallow clone the branch, in which
the commit is expected to exist.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the reference to check out; takes precedence over Branch, Tag and SemVer.

It must be a valid Git reference: https://git-scm.com/docs/git-check-ref-format#_description
Examples: "refs/heads/main", "refs/tags/v0.1.0", "refs/pull/420/head", "refs/merge-requests/1/head"<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>semver</b></td>
        <td>string</td>
        <td>
          SemVer tag expression to check out, takes precedence over Tag.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>tag</b></td>
        <td>string</td>
        <td>
          Tag to check out, takes precedence over Branch.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.git.secretRef
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespecgit-1)</sup></sup>



SecretRef specifies the Secret containing authentication credentials for
the GitRepository.
For HTTPS repositories the Secret must contain 'username' and 'password'
fields for basic auth or 'bearerToken' field for token auth.
For SSH repositories the Secret must contain 'identity'
and 'known_hosts' fields.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.git.verify
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespecgit-1)</sup></sup>



Verification specifies the configuration to verify the Git commit
signature(s).

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecgitverifysecretref-1">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing the public keys of trusted Git
authors.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>mode</b></td>
        <td>enum</td>
        <td>
          Mode specifies which Git object(s) should be verified.

The variants "head" and "HEAD" both imply the same thing, i.e. verify
the commit that the HEAD of the Git repository points to. The variant
"head" solely exists to ensure backwards compatibility.<br/>
          <br/>
            <i>Enum</i>: head, HEAD, Tag, TagAndHEAD<br/>
            <i>Default</i>: HEAD<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.git.verify.secretRef
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespecgitverify-1)</sup></sup>



SecretRef specifies the Secret containing the public keys of trusted Git
authors.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.oci
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespec-1)</sup></sup>



OCI is the definition of OCI repository source.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>interval</b></td>
        <td>string</td>
        <td>
          Interval at which the OCIRepository URL is checked for updates.
This interval is approximate and may be subject to jitter to ensure
efficient use of resources.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>url</b></td>
        <td>string</td>
        <td>
          URL is a reference to an OCI artifact repository hosted
on a remote container registry.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecocicertsecretref-1">certSecretRef</a></b></td>
        <td>object</td>
        <td>
          CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
registry. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

Note: Support for the `caFile`, `certFile` and `keyFile` keys have
been deprecated.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>ignore</b></td>
        <td>string</td>
        <td>
          Ignore overrides the set of excluded patterns in the .sourceignore format
(which is the same as .gitignore). If not provided, a default will be used,
consult the documentation for your version to find out what those are.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>insecure</b></td>
        <td>boolean</td>
        <td>
          Insecure allows connecting to a non-TLS HTTP container registry.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecocilayerselector-1">layerSelector</a></b></td>
        <td>object</td>
        <td>
          LayerSelector specifies which layer should be extracted from the OCI artifact.
When not specified, the first layer found in the artifact is selected.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          The provider used for authentication, can be 'aws', 'azure', 'gcp' or 'generic'.
When not specified, defaults to 'generic'.<br/>
          <br/>
            <i>Enum</i>: generic, aws, azure, gcp<br/>
            <i>Default</i>: generic<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecociproxysecretref-1">proxySecretRef</a></b></td>
        <td>object</td>
        <td>
          ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the container registry.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecociref-1">ref</a></b></td>
        <td>object</td>
        <td>
          The OCI reference to pull and monitor for changes,
defaults to the latest tag.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecocisecretref-1">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef contains the secret name containing the registry login
credentials to resolve image metadata.
The secret must be of type kubernetes.io/dockerconfigjson.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>serviceAccountName</b></td>
        <td>string</td>
        <td>
          ServiceAccountName is the name of the Kubernetes ServiceAccount used to authenticate
the image pull if the service account has attached pull secrets. For more information:
https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#add-imagepullsecrets-to-a-service-account<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>suspend</b></td>
        <td>boolean</td>
        <td>
          This flag tells the controller to suspend the reconciliation of this source.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>timeout</b></td>
        <td>string</td>
        <td>
          The timeout for remote OCI Repository operations like pulling, defaults to 60s.<br/>
          <br/>
            <i>Default</i>: 60s<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecociverify-1">verify</a></b></td>
        <td>object</td>
        <td>
          Verify contains the secret name containing the trusted public keys
used to verify the signature and specifies which provider to use to check
whether OCI image is authentic.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.oci.certSecretRef
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespecoci-1)</sup></sup>



CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
registry. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

Note: Support for the `caFile`, `certFile` and `keyFile` keys have
been deprecated.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.oci.layerSelector
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespecoci-1)</sup></sup>



LayerSelector specifies which layer should be extracted from the OCI artifact.
When not specified, the first layer found in the artifact is selected.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>mediaType</b></td>
        <td>string</td>
        <td>
          MediaType specifies the OCI media type of the layer
which should be extracted from the OCI Artifact. The
first layer matching this type is selected.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>operation</b></td>
        <td>enum</td>
        <td>
          Operation specifies how the selected layer should be processed.
By default, the layer compressed content is extracted to storage.
When the operation is set to 'copy', the layer compressed content
is persisted to storage as it is.<br/>
          <br/>
            <i>Enum</i>: extract, copy<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.oci.proxySecretRef
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespecoci-1)</sup></sup>



ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the container registry.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.oci.ref
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespecoci-1)</sup></sup>



The OCI reference to pull and monitor for changes,
defaults to the latest tag.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>digest</b></td>
        <td>string</td>
        <td>
          Digest is the image digest to pull, takes precedence over SemVer.
The value should be in the format 'sha256:<HASH>'.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>semver</b></td>
        <td>string</td>
        <td>
          SemVer is the range of tags to pull selecting the latest within
the range, takes precedence over Tag.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>semverFilter</b></td>
        <td>string</td>
        <td>
          SemverFilter is a regex pattern to filter the tags within the SemVer range.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>tag</b></td>
        <td>string</td>
        <td>
          Tag is the image tag to pull, defaults to latest.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.oci.secretRef
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespecoci-1)</sup></sup>



SecretRef contains the secret name containing the registry login
credentials to resolve image metadata.
The secret must be of type kubernetes.io/dockerconfigjson.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.oci.verify
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespecoci-1)</sup></sup>



Verify contains the secret name containing the trusted public keys
used to verify the signature and specifies which provider to use to check
whether OCI image is authentic.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider specifies the technology used to sign the OCI Artifact.<br/>
          <br/>
            <i>Enum</i>: cosign, notation<br/>
            <i>Default</i>: cosign<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecociverifymatchoidcidentityindex-1">matchOIDCIdentity</a></b></td>
        <td>[]object</td>
        <td>
          MatchOIDCIdentity specifies the identity matching criteria to use
while verifying an OCI artifact which was signed using Cosign keyless
signing. The artifact's identity is deemed to be verified if any of the
specified matchers match against the identity.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartsourceremotesourcespecociverifysecretref-1">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Kubernetes Secret containing the
trusted public keys.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.oci.verify.matchOIDCIdentity[index]
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespecociverify-1)</sup></sup>



OIDCIdentityMatch specifies options for verifying the certificate identity,
i.e. the issuer and the subject of the certificate.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>issuer</b></td>
        <td>string</td>
        <td>
          Issuer specifies the regex pattern to match against to verify
the OIDC issuer in the Fulcio certificate. The pattern must be a
valid Go regular expression.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>subject</b></td>
        <td>string</td>
        <td>
          Subject specifies the regex pattern to match against to verify
the identity subject in the Fulcio certificate. The pattern must
be a valid Go regular expression.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.oci.verify.secretRef
<sup><sup>[↩ Parent](#clustertemplatespechelmchartsourceremotesourcespecociverify-1)</sup></sup>



SecretRef specifies the Kubernetes Secret containing the
trusted public keys.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSpec
<sup><sup>[↩ Parent](#clustertemplatespechelm-1)</sup></sup>



ChartSpec defines the desired state of the HelmChart to be created by the controller

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>chart</b></td>
        <td>string</td>
        <td>
          Chart is the name or path the Helm chart is available at in the
SourceRef.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>interval</b></td>
        <td>string</td>
        <td>
          Interval at which the HelmChart SourceRef is checked for updates.
This interval is approximate and may be subject to jitter to ensure
efficient use of resources.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartspecsourceref-1">sourceRef</a></b></td>
        <td>object</td>
        <td>
          SourceRef is the reference to the Source the chart is available at.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>ignoreMissingValuesFiles</b></td>
        <td>boolean</td>
        <td>
          IgnoreMissingValuesFiles controls whether to silently ignore missing values
files rather than failing.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>reconcileStrategy</b></td>
        <td>enum</td>
        <td>
          ReconcileStrategy determines what enables the creation of a new artifact.
Valid values are ('ChartVersion', 'Revision').
See the documentation of the values for an explanation on their behavior.
Defaults to ChartVersion when omitted.<br/>
          <br/>
            <i>Enum</i>: ChartVersion, Revision<br/>
            <i>Default</i>: ChartVersion<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>suspend</b></td>
        <td>boolean</td>
        <td>
          Suspend tells the controller to suspend the reconciliation of this
source.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>valuesFiles</b></td>
        <td>[]string</td>
        <td>
          ValuesFiles is an alternative list of values files to use as the chart
values (values.yaml is not included by default), expected to be a
relative path in the SourceRef.
Values files are merged in the order of this list with the last file
overriding the first. Ignored when omitted.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartspecverify-1">verify</a></b></td>
        <td>object</td>
        <td>
          Verify contains the secret name containing the trusted public keys
used to verify the signature and specifies which provider to use to check
whether OCI image is authentic.
This field is only supported when using HelmRepository source with spec.type 'oci'.
Chart dependencies, which are not bundled in the umbrella chart artifact, are not verified.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>version</b></td>
        <td>string</td>
        <td>
          Version is the chart version semver expression, ignored for charts from
GitRepository and Bucket sources. Defaults to latest when omitted.<br/>
          <br/>
            <i>Default</i>: *<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSpec.sourceRef
<sup><sup>[↩ Parent](#clustertemplatespechelmchartspec-1)</sup></sup>



SourceRef is the reference to the Source the chart is available at.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>kind</b></td>
        <td>enum</td>
        <td>
          Kind of the referent, valid values are ('HelmRepository', 'GitRepository',
'Bucket').<br/>
          <br/>
            <i>Enum</i>: HelmRepository, GitRepository, Bucket<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>apiVersion</b></td>
        <td>string</td>
        <td>
          APIVersion of the referent.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSpec.verify
<sup><sup>[↩ Parent](#clustertemplatespechelmchartspec-1)</sup></sup>



Verify contains the secret name containing the trusted public keys
used to verify the signature and specifies which provider to use to check
whether OCI image is authentic.
This field is only supported when using HelmRepository source with spec.type 'oci'.
Chart dependencies, which are not bundled in the umbrella chart artifact, are not verified.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider specifies the technology used to sign the OCI Artifact.<br/>
          <br/>
            <i>Enum</i>: cosign, notation<br/>
            <i>Default</i>: cosign<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartspecverifymatchoidcidentityindex-1">matchOIDCIdentity</a></b></td>
        <td>[]object</td>
        <td>
          MatchOIDCIdentity specifies the identity matching criteria to use
while verifying an OCI artifact which was signed using Cosign keyless
signing. The artifact's identity is deemed to be verified if any of the
specified matchers match against the identity.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#clustertemplatespechelmchartspecverifysecretref-1">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Kubernetes Secret containing the
trusted public keys.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSpec.verify.matchOIDCIdentity[index]
<sup><sup>[↩ Parent](#clustertemplatespechelmchartspecverify-1)</sup></sup>



OIDCIdentityMatch specifies options for verifying the certificate identity,
i.e. the issuer and the subject of the certificate.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>issuer</b></td>
        <td>string</td>
        <td>
          Issuer specifies the regex pattern to match against to verify
the OIDC issuer in the Fulcio certificate. The pattern must be a
valid Go regular expression.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>subject</b></td>
        <td>string</td>
        <td>
          Subject specifies the regex pattern to match against to verify
the identity subject in the Fulcio certificate. The pattern must
be a valid Go regular expression.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSpec.verify.secretRef
<sup><sup>[↩ Parent](#clustertemplatespechelmchartspecverify-1)</sup></sup>



SecretRef specifies the Kubernetes Secret containing the
trusted public keys.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ClusterTemplate.status
<sup><sup>[↩ Parent](#clustertemplate-1)</sup></sup>



ClusterTemplateStatus defines the observed state of ClusterTemplate

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>valid</b></td>
        <td>boolean</td>
        <td>
          Valid indicates whether the template passed validation or not.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#clustertemplatestatuschartref-1">chartRef</a></b></td>
        <td>object</td>
        <td>
          ChartRef is a reference to a source controller resource containing the
Helm chart representing the template.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>chartVersion</b></td>
        <td>string</td>
        <td>
          ChartVersion represents the version of the Helm Chart associated with this template.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>config</b></td>
        <td>JSON</td>
        <td>
          Config demonstrates available parameters for template customization,
that can be used when creating ClusterDeployment objects.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>description</b></td>
        <td>string</td>
        <td>
          Description contains information about the template.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>k8sVersion</b></td>
        <td>string</td>
        <td>
          Kubernetes exact version in the SemVer format provided by this ClusterTemplate.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>observedGeneration</b></td>
        <td>integer</td>
        <td>
          ObservedGeneration is the last observed generation.<br/>
          <br/>
            <i>Format</i>: int64<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>providerContracts</b></td>
        <td>map[string]string</td>
        <td>
          Holds key-value pairs with compatibility [contract versions],
where the key is the name of the provider,
and the value is the provider contract version
required to be supported by the provider.

[contract versions]: https://cluster-api.sigs.k8s.io/developer/providers/contracts<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>providers</b></td>
        <td>[]string</td>
        <td>
          Providers represent required CAPI providers.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>validationError</b></td>
        <td>string</td>
        <td>
          ValidationError provides information regarding issues encountered during template validation.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.status.chartRef
<sup><sup>[↩ Parent](#clustertemplatestatus-1)</sup></sup>



ChartRef is a reference to a source controller resource containing the
Helm chart representing the template.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>kind</b></td>
        <td>enum</td>
        <td>
          Kind of the referent.<br/>
          <br/>
            <i>Enum</i>: OCIRepository, HelmChart<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>apiVersion</b></td>
        <td>string</td>
        <td>
          APIVersion of the referent.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace of the referent, defaults to the namespace of the Kubernetes
resource object that contains the reference.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>

## Credential
<sup><sup>[↩ Parent](#k0rdentmirantiscomv1beta1 )</sup></sup>






Credential is the Schema for the credentials API

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
      <td><b>apiVersion</b></td>
      <td>string</td>
      <td>k0rdent.mirantis.com/v1beta1</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b>kind</b></td>
      <td>string</td>
      <td>Credential</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#credentialspec-1">spec</a></b></td>
        <td>object</td>
        <td>
          CredentialSpec defines the desired state of Credential<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#credentialstatus-1">status</a></b></td>
        <td>object</td>
        <td>
          CredentialStatus defines the observed state of Credential<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### Credential.spec
<sup><sup>[↩ Parent](#credential-1)</sup></sup>



CredentialSpec defines the desired state of Credential

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#credentialspecidentityref-1">identityRef</a></b></td>
        <td>object</td>
        <td>
          Reference to the Credential Identity<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>description</b></td>
        <td>string</td>
        <td>
          Description of the Credential object<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### Credential.spec.identityRef
<sup><sup>[↩ Parent](#credentialspec-1)</sup></sup>



Reference to the Credential Identity

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>apiVersion</b></td>
        <td>string</td>
        <td>
          API version of the referent.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>fieldPath</b></td>
        <td>string</td>
        <td>
          If referring to a piece of an object instead of an entire object, this string
should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2].
For example, if the object reference is to a container within a pod, this would take on a value like:
"spec.containers{name}" (where "name" refers to the name of the container that triggered
the event) or if no container name is specified "spec.containers[2]" (container with
index 2 in this pod). This syntax is chosen only to have some well-defined way of
referencing a part of an object.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>kind</b></td>
        <td>string</td>
        <td>
          Kind of the referent.
More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.
More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace of the referent.
More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>resourceVersion</b></td>
        <td>string</td>
        <td>
          Specific resourceVersion to which this reference is made, if any.
More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>uid</b></td>
        <td>string</td>
        <td>
          UID of the referent.
More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### Credential.status
<sup><sup>[↩ Parent](#credential-1)</sup></sup>



CredentialStatus defines the observed state of Credential

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>ready</b></td>
        <td>boolean</td>
        <td>
          Ready holds the readiness of Credentials.<br/>
          <br/>
            <i>Default</i>: false<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#credentialstatusconditionsindex-1">conditions</a></b></td>
        <td>[]object</td>
        <td>
          Conditions contains details for the current state of the Credential.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### Credential.status.conditions[index]
<sup><sup>[↩ Parent](#credentialstatus-1)</sup></sup>



Condition contains details for one aspect of the current state of this API Resource.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>lastTransitionTime</b></td>
        <td>string</td>
        <td>
          lastTransitionTime is the last time the condition transitioned from one status to another.
This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable.<br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>message</b></td>
        <td>string</td>
        <td>
          message is a human readable message indicating details about the transition.
This may be an empty string.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>reason</b></td>
        <td>string</td>
        <td>
          reason contains a programmatic identifier indicating the reason for the condition's last transition.
Producers of specific condition types may define expected values and meanings for this field,
and whether the values are considered a guaranteed API.
The value should be a CamelCase string.
This field may not be empty.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>status</b></td>
        <td>enum</td>
        <td>
          status of the condition, one of True, False, Unknown.<br/>
          <br/>
            <i>Enum</i>: True, False, Unknown<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>type</b></td>
        <td>string</td>
        <td>
          type of condition in CamelCase or in foo.example.com/CamelCase.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>observedGeneration</b></td>
        <td>integer</td>
        <td>
          observedGeneration represents the .metadata.generation that the condition was set based upon.
For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date
with respect to the current state of the instance.<br/>
          <br/>
            <i>Format</i>: int64<br/>
            <i>Minimum</i>: 0<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>

## ManagementBackup
<sup><sup>[↩ Parent](#k0rdentmirantiscomv1beta1 )</sup></sup>






ManagementBackup is the Schema for the managementbackups API

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
      <td><b>apiVersion</b></td>
      <td>string</td>
      <td>k0rdent.mirantis.com/v1beta1</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b>kind</b></td>
      <td>string</td>
      <td>ManagementBackup</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#managementbackupspec-1">spec</a></b></td>
        <td>object</td>
        <td>
          ManagementBackupSpec defines the desired state of ManagementBackup<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#managementbackupstatus-1">status</a></b></td>
        <td>object</td>
        <td>
          ManagementBackupStatus defines the observed state of ManagementBackup<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ManagementBackup.spec
<sup><sup>[↩ Parent](#managementbackup-1)</sup></sup>



ManagementBackupSpec defines the desired state of ManagementBackup

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>performOnManagementUpgrade</b></td>
        <td>boolean</td>
        <td>
          PerformOnManagementUpgrade indicates that a single [ManagementBackup]
should be created and stored in the [ManagementBackup] storage location if not default
before the [Management] release upgrade.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>schedule</b></td>
        <td>string</td>
        <td>
          Schedule is a Cron expression defining when to run the scheduled [ManagementBackup].
If not set, the object is considered to be run only once.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>storageLocation</b></td>
        <td>string</td>
        <td>
          StorageLocation is the name of a [github.com/vmware-tanzu/velero/pkg/apis/velero/v1.StorageLocation]
where the backup should be stored.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ManagementBackup.status
<sup><sup>[↩ Parent](#managementbackup-1)</sup></sup>



ManagementBackupStatus defines the observed state of ManagementBackup

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>error</b></td>
        <td>string</td>
        <td>
          Error stores messages in case of failed backup creation.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#managementbackupstatuslastbackup-1">lastBackup</a></b></td>
        <td>object</td>
        <td>
          Most recently [github.com/vmware-tanzu/velero/pkg/apis/velero/v1.Backup] that has been created.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>lastBackupName</b></td>
        <td>string</td>
        <td>
          Name of most recently created [github.com/vmware-tanzu/velero/pkg/apis/velero/v1.Backup].<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>lastBackupTime</b></td>
        <td>string</td>
        <td>
          Time of the most recently created [github.com/vmware-tanzu/velero/pkg/apis/velero/v1.Backup].<br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>nextAttempt</b></td>
        <td>string</td>
        <td>
          NextAttempt indicates the time when the next backup will be created.
Always absent for a single [ManagementBackup].<br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ManagementBackup.status.lastBackup
<sup><sup>[↩ Parent](#managementbackupstatus-1)</sup></sup>



Most recently [github.com/vmware-tanzu/velero/pkg/apis/velero/v1.Backup] that has been created.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>backupItemOperationsAttempted</b></td>
        <td>integer</td>
        <td>
          BackupItemOperationsAttempted is the total number of attempted
async BackupItemAction operations for this backup.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>backupItemOperationsCompleted</b></td>
        <td>integer</td>
        <td>
          BackupItemOperationsCompleted is the total number of successfully completed
async BackupItemAction operations for this backup.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>backupItemOperationsFailed</b></td>
        <td>integer</td>
        <td>
          BackupItemOperationsFailed is the total number of async
BackupItemAction operations for this backup which ended with an error.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>completionTimestamp</b></td>
        <td>string</td>
        <td>
          CompletionTimestamp records the time a backup was completed.
Completion time is recorded even on failed backups.
Completion time is recorded before uploading the backup object.
The server's time is used for CompletionTimestamps<br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>csiVolumeSnapshotsAttempted</b></td>
        <td>integer</td>
        <td>
          CSIVolumeSnapshotsAttempted is the total number of attempted
CSI VolumeSnapshots for this backup.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>csiVolumeSnapshotsCompleted</b></td>
        <td>integer</td>
        <td>
          CSIVolumeSnapshotsCompleted is the total number of successfully
completed CSI VolumeSnapshots for this backup.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>errors</b></td>
        <td>integer</td>
        <td>
          Errors is a count of all error messages that were generated during
execution of the backup.  The actual errors are in the backup's log
file in object storage.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>expiration</b></td>
        <td>string</td>
        <td>
          Expiration is when this Backup is eligible for garbage-collection.<br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>failureReason</b></td>
        <td>string</td>
        <td>
          FailureReason is an error that caused the entire backup to fail.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>formatVersion</b></td>
        <td>string</td>
        <td>
          FormatVersion is the backup format version, including major, minor, and patch version.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#managementbackupstatuslastbackuphookstatus-1">hookStatus</a></b></td>
        <td>object</td>
        <td>
          HookStatus contains information about the status of the hooks.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>phase</b></td>
        <td>enum</td>
        <td>
          Phase is the current state of the Backup.<br/>
          <br/>
            <i>Enum</i>: New, FailedValidation, InProgress, WaitingForPluginOperations, WaitingForPluginOperationsPartiallyFailed, Finalizing, FinalizingPartiallyFailed, Completed, PartiallyFailed, Failed, Deleting<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#managementbackupstatuslastbackupprogress-1">progress</a></b></td>
        <td>object</td>
        <td>
          Progress contains information about the backup's execution progress. Note
that this information is best-effort only -- if Velero fails to update it
during a backup for any reason, it may be inaccurate/stale.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>startTimestamp</b></td>
        <td>string</td>
        <td>
          StartTimestamp records the time a backup was started.
Separate from CreationTimestamp, since that value changes
on restores.
The server's time is used for StartTimestamps<br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>validationErrors</b></td>
        <td>[]string</td>
        <td>
          ValidationErrors is a slice of all validation errors (if
applicable).<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>version</b></td>
        <td>integer</td>
        <td>
          Version is the backup format major version.
Deprecated: Please see FormatVersion<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>volumeSnapshotsAttempted</b></td>
        <td>integer</td>
        <td>
          VolumeSnapshotsAttempted is the total number of attempted
volume snapshots for this backup.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>volumeSnapshotsCompleted</b></td>
        <td>integer</td>
        <td>
          VolumeSnapshotsCompleted is the total number of successfully
completed volume snapshots for this backup.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>warnings</b></td>
        <td>integer</td>
        <td>
          Warnings is a count of all warning messages that were generated during
execution of the backup. The actual warnings are in the backup's log
file in object storage.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ManagementBackup.status.lastBackup.hookStatus
<sup><sup>[↩ Parent](#managementbackupstatuslastbackup-1)</sup></sup>



HookStatus contains information about the status of the hooks.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>hooksAttempted</b></td>
        <td>integer</td>
        <td>
          HooksAttempted is the total number of attempted hooks
Specifically, HooksAttempted represents the number of hooks that failed to execute
and the number of hooks that executed successfully.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>hooksFailed</b></td>
        <td>integer</td>
        <td>
          HooksFailed is the total number of hooks which ended with an error<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ManagementBackup.status.lastBackup.progress
<sup><sup>[↩ Parent](#managementbackupstatuslastbackup-1)</sup></sup>



Progress contains information about the backup's execution progress. Note
that this information is best-effort only -- if Velero fails to update it
during a backup for any reason, it may be inaccurate/stale.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>itemsBackedUp</b></td>
        <td>integer</td>
        <td>
          ItemsBackedUp is the number of items that have actually been written to the
backup tarball so far.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>totalItems</b></td>
        <td>integer</td>
        <td>
          TotalItems is the total number of items to be backed up. This number may change
throughout the execution of the backup due to plugins that return additional related
items to back up, the velero.io/exclude-from-backup label, and various other
filters that happen as items are processed.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>

## Management
<sup><sup>[↩ Parent](#k0rdentmirantiscomv1beta1 )</sup></sup>






Management is the Schema for the managements API

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
      <td><b>apiVersion</b></td>
      <td>string</td>
      <td>k0rdent.mirantis.com/v1beta1</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b>kind</b></td>
      <td>string</td>
      <td>Management</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#managementspec-1">spec</a></b></td>
        <td>object</td>
        <td>
          ManagementSpec defines the desired state of Management<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#managementstatus-1">status</a></b></td>
        <td>object</td>
        <td>
          ManagementStatus defines the observed state of Management<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### Management.spec
<sup><sup>[↩ Parent](#management-1)</sup></sup>



ManagementSpec defines the desired state of Management

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>release</b></td>
        <td>string</td>
        <td>
          Release references the Release object.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#managementspeccore-1">core</a></b></td>
        <td>object</td>
        <td>
          Core holds the core Management components that are mandatory.
If not specified, will be populated with the default values.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#managementspecprovidersindex-1">providers</a></b></td>
        <td>[]object</td>
        <td>
          Providers is the list of supported CAPI providers.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### Management.spec.core
<sup><sup>[↩ Parent](#managementspec-1)</sup></sup>



Core holds the core Management components that are mandatory.
If not specified, will be populated with the default values.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#managementspeccorecapi-1">capi</a></b></td>
        <td>object</td>
        <td>
          CAPI represents the core Cluster API component and references the Cluster API template.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#managementspeccorekcm-1">kcm</a></b></td>
        <td>object</td>
        <td>
          KCM represents the core KCM component and references the KCM template.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### Management.spec.core.capi
<sup><sup>[↩ Parent](#managementspeccore-1)</sup></sup>



CAPI represents the core Cluster API component and references the Cluster API template.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>config</b></td>
        <td>JSON</td>
        <td>
          Config allows to provide parameters for management component customization.
If no Config provided, the field will be populated with the default
values for the template.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>template</b></td>
        <td>string</td>
        <td>
          Template is the name of the Template associated with this component.
If not specified, will be taken from the Release object.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### Management.spec.core.kcm
<sup><sup>[↩ Parent](#managementspeccore-1)</sup></sup>



KCM represents the core KCM component and references the KCM template.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>config</b></td>
        <td>JSON</td>
        <td>
          Config allows to provide parameters for management component customization.
If no Config provided, the field will be populated with the default
values for the template.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>template</b></td>
        <td>string</td>
        <td>
          Template is the name of the Template associated with this component.
If not specified, will be taken from the Release object.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### Management.spec.providers[index]
<sup><sup>[↩ Parent](#managementspec-1)</sup></sup>





<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the provider.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>config</b></td>
        <td>JSON</td>
        <td>
          Config allows to provide parameters for management component customization.
If no Config provided, the field will be populated with the default
values for the template.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>template</b></td>
        <td>string</td>
        <td>
          Template is the name of the Template associated with this component.
If not specified, will be taken from the Release object.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### Management.status
<sup><sup>[↩ Parent](#management-1)</sup></sup>



ManagementStatus defines the observed state of Management

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>availableProviders</b></td>
        <td>[]string</td>
        <td>
          AvailableProviders holds all available CAPI providers.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>backupName</b></td>
        <td>string</td>
        <td>
          BackupName is a name of the management cluster scheduled backup.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>capiContracts</b></td>
        <td>map[string]map[string]string</td>
        <td>
          For each CAPI provider name holds its compatibility [contract versions]
in a key-value pairs, where the key is the core CAPI contract version,
and the value is an underscore-delimited (_) list of provider contract versions
supported by the core CAPI.

[contract versions]: https://cluster-api.sigs.k8s.io/developer/providers/contracts<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#managementstatuscomponentskey-1">components</a></b></td>
        <td>map[string]object</td>
        <td>
          Components indicates the status of installed KCM components and CAPI providers.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#managementstatusconditionsindex-1">conditions</a></b></td>
        <td>[]object</td>
        <td>
          Conditions represents the observations of a Management's current state.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>observedGeneration</b></td>
        <td>integer</td>
        <td>
          ObservedGeneration is the last observed generation.<br/>
          <br/>
            <i>Format</i>: int64<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>release</b></td>
        <td>string</td>
        <td>
          Release indicates the current Release object.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### Management.status.components[key]
<sup><sup>[↩ Parent](#managementstatus-1)</sup></sup>



ComponentStatus is the status of Management component installation

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>error</b></td>
        <td>string</td>
        <td>
          Error stores as error message in case of failed installation<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>exposedProviders</b></td>
        <td>[]string</td>
        <td>
          ExposedProviders is a list of CAPI providers this component exposes<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>success</b></td>
        <td>boolean</td>
        <td>
          Success represents if a component installation was successful<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>template</b></td>
        <td>string</td>
        <td>
          Template is the name of the Template associated with this component.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### Management.status.conditions[index]
<sup><sup>[↩ Parent](#managementstatus-1)</sup></sup>



Condition contains details for one aspect of the current state of this API Resource.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>lastTransitionTime</b></td>
        <td>string</td>
        <td>
          lastTransitionTime is the last time the condition transitioned from one status to another.
This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable.<br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>message</b></td>
        <td>string</td>
        <td>
          message is a human readable message indicating details about the transition.
This may be an empty string.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>reason</b></td>
        <td>string</td>
        <td>
          reason contains a programmatic identifier indicating the reason for the condition's last transition.
Producers of specific condition types may define expected values and meanings for this field,
and whether the values are considered a guaranteed API.
The value should be a CamelCase string.
This field may not be empty.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>status</b></td>
        <td>enum</td>
        <td>
          status of the condition, one of True, False, Unknown.<br/>
          <br/>
            <i>Enum</i>: True, False, Unknown<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>type</b></td>
        <td>string</td>
        <td>
          type of condition in CamelCase or in foo.example.com/CamelCase.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>observedGeneration</b></td>
        <td>integer</td>
        <td>
          observedGeneration represents the .metadata.generation that the condition was set based upon.
For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date
with respect to the current state of the instance.<br/>
          <br/>
            <i>Format</i>: int64<br/>
            <i>Minimum</i>: 0<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>

## MultiClusterService
<sup><sup>[↩ Parent](#k0rdentmirantiscomv1beta1 )</sup></sup>






MultiClusterService is the Schema for the multiclusterservices API

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
      <td><b>apiVersion</b></td>
      <td>string</td>
      <td>k0rdent.mirantis.com/v1beta1</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b>kind</b></td>
      <td>string</td>
      <td>MultiClusterService</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#multiclusterservicespec-1">spec</a></b></td>
        <td>object</td>
        <td>
          MultiClusterServiceSpec defines the desired state of MultiClusterService<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#multiclusterservicestatus-1">status</a></b></td>
        <td>object</td>
        <td>
          MultiClusterServiceStatus defines the observed state of MultiClusterService.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.spec
<sup><sup>[↩ Parent](#multiclusterservice-1)</sup></sup>



MultiClusterServiceSpec defines the desired state of MultiClusterService

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#multiclusterservicespecclusterselector-1">clusterSelector</a></b></td>
        <td>object</td>
        <td>
          ClusterSelector identifies target clusters to manage services on.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#multiclusterservicespecservicespec-1">serviceSpec</a></b></td>
        <td>object</td>
        <td>
          ServiceSpec is spec related to deployment of services.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.spec.clusterSelector
<sup><sup>[↩ Parent](#multiclusterservicespec-1)</sup></sup>



ClusterSelector identifies target clusters to manage services on.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#multiclusterservicespecclusterselectormatchexpressionsindex-1">matchExpressions</a></b></td>
        <td>[]object</td>
        <td>
          matchExpressions is a list of label selector requirements. The requirements are ANDed.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>matchLabels</b></td>
        <td>map[string]string</td>
        <td>
          matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels
map is equivalent to an element of matchExpressions, whose key field is "key", the
operator is "In", and the values array contains only "value". The requirements are ANDed.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.spec.clusterSelector.matchExpressions[index]
<sup><sup>[↩ Parent](#multiclusterservicespecclusterselector-1)</sup></sup>



A label selector requirement is a selector that contains values, a key, and an operator that
relates the key and values.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>key</b></td>
        <td>string</td>
        <td>
          key is the label key that the selector applies to.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>operator</b></td>
        <td>string</td>
        <td>
          operator represents a key's relationship to a set of values.
Valid operators are In, NotIn, Exists and DoesNotExist.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>values</b></td>
        <td>[]string</td>
        <td>
          values is an array of string values. If the operator is In or NotIn,
the values array must be non-empty. If the operator is Exists or DoesNotExist,
the values array must be empty. This array is replaced during a strategic
merge patch.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.spec.serviceSpec
<sup><sup>[↩ Parent](#multiclusterservicespec-1)</sup></sup>



ServiceSpec is spec related to deployment of services.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>continueOnError</b></td>
        <td>boolean</td>
        <td>
          ContinueOnError specifies if the services deployment should continue if an error occurs.<br/>
          <br/>
            <i>Default</i>: false<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#multiclusterservicespecservicespecdriftexclusionsindex-1">driftExclusions</a></b></td>
        <td>[]object</td>
        <td>
          DriftExclusions specifies specific configurations of resources to ignore for drift detection.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#multiclusterservicespecservicespecdriftignoreindex-1">driftIgnore</a></b></td>
        <td>[]object</td>
        <td>
          DriftIgnore specifies resources to ignore for drift detection.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>priority</b></td>
        <td>integer</td>
        <td>
          Priority sets the priority for the services defined in this spec.
Higher value means higher priority and lower means lower.
In case of conflict with another object managing the service,
the one with higher priority will get to deploy its services.<br/>
          <br/>
            <i>Format</i>: int32<br/>
            <i>Default</i>: 100<br/>
            <i>Minimum</i>: 1<br/>
            <i>Maximum</i>: 2.147483646e+09<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>reload</b></td>
        <td>boolean</td>
        <td>
          Reload instances via rolling upgrade when a ConfigMap/Secret mounted as volume is modified.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#multiclusterservicespecservicespecservicesindex-1">services</a></b></td>
        <td>[]object</td>
        <td>
          Services is a list of services created via ServiceTemplates
that could be installed on the target cluster.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>stopOnConflict</b></td>
        <td>boolean</td>
        <td>
          StopOnConflict specifies what to do in case of a conflict.
E.g. If another object is already managing a service.
By default the remaining services will be deployed even if conflict is detected.
If set to true, the deployment will stop after encountering the first conflict.<br/>
          <br/>
            <i>Default</i>: false<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>syncMode</b></td>
        <td>enum</td>
        <td>
          SyncMode specifies how services are synced in the target cluster.<br/>
          <br/>
            <i>Enum</i>: OneTime, Continuous, ContinuousWithDriftDetection, DryRun<br/>
            <i>Default</i>: Continuous<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#multiclusterservicespecservicespectemplateresourcerefsindex-1">templateResourceRefs</a></b></td>
        <td>[]object</td>
        <td>
          TemplateResourceRefs is a list of resources to collect from the management cluster,
the values from which can be used in templates.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.spec.serviceSpec.driftExclusions[index]
<sup><sup>[↩ Parent](#multiclusterservicespecservicespec-1)</sup></sup>





<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>paths</b></td>
        <td>[]string</td>
        <td>
          Paths is a slice of JSON6902 paths to exclude from configuration drift evaluation.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#multiclusterservicespecservicespecdriftexclusionsindextarget-1">target</a></b></td>
        <td>object</td>
        <td>
          Target points to the resources that the paths refers to.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.spec.serviceSpec.driftExclusions[index].target
<sup><sup>[↩ Parent](#multiclusterservicespecservicespecdriftexclusionsindex-1)</sup></sup>



Target points to the resources that the paths refers to.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>annotationSelector</b></td>
        <td>string</td>
        <td>
          AnnotationSelector is a string that follows the label selection expression
https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#api
It matches with the resource annotations.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>group</b></td>
        <td>string</td>
        <td>
          Group is the API group to select resources from.
Together with Version and Kind it is capable of unambiguously identifying and/or selecting resources.
https://github.com/kubernetes/community/blob/master/contributors/design-proposals/api-machinery/api-group.md<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>kind</b></td>
        <td>string</td>
        <td>
          Kind of the API Group to select resources from.
Together with Group and Version it is capable of unambiguously
identifying and/or selecting resources.
https://github.com/kubernetes/community/blob/master/contributors/design-proposals/api-machinery/api-group.md<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>labelSelector</b></td>
        <td>string</td>
        <td>
          LabelSelector is a string that follows the label selection expression
https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#api
It matches with the resource labels.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name to match resources with.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace to select resources from.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>version</b></td>
        <td>string</td>
        <td>
          Version of the API Group to select resources from.
Together with Group and Kind it is capable of unambiguously identifying and/or selecting resources.
https://github.com/kubernetes/community/blob/master/contributors/design-proposals/api-machinery/api-group.md<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.spec.serviceSpec.driftIgnore[index]
<sup><sup>[↩ Parent](#multiclusterservicespecservicespec-1)</sup></sup>





<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>annotationSelector</b></td>
        <td>string</td>
        <td>
          AnnotationSelector is a string that follows the label selection expression
https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#api
It matches with the resource annotations.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>group</b></td>
        <td>string</td>
        <td>
          Group is the API group to select resources from.
Together with Version and Kind it is capable of unambiguously identifying and/or selecting resources.
https://github.com/kubernetes/community/blob/master/contributors/design-proposals/api-machinery/api-group.md<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>kind</b></td>
        <td>string</td>
        <td>
          Kind of the API Group to select resources from.
Together with Group and Version it is capable of unambiguously
identifying and/or selecting resources.
https://github.com/kubernetes/community/blob/master/contributors/design-proposals/api-machinery/api-group.md<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>labelSelector</b></td>
        <td>string</td>
        <td>
          LabelSelector is a string that follows the label selection expression
https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#api
It matches with the resource labels.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name to match resources with.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace to select resources from.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>version</b></td>
        <td>string</td>
        <td>
          Version of the API Group to select resources from.
Together with Group and Kind it is capable of unambiguously identifying and/or selecting resources.
https://github.com/kubernetes/community/blob/master/contributors/design-proposals/api-machinery/api-group.md<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.spec.serviceSpec.services[index]
<sup><sup>[↩ Parent](#multiclusterservicespecservicespec-1)</sup></sup>



Service represents a Service to be deployed.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name is the chart release.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>template</b></td>
        <td>string</td>
        <td>
          Template is a reference to a Template object located in the same namespace.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>disable</b></td>
        <td>boolean</td>
        <td>
          Disable can be set to disable handling of this service.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace is the namespace the release will be installed in.
It will default to Name if not provided.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>templateChain</b></td>
        <td>string</td>
        <td>
          TemplateChain defines the ServiceTemplateChain object that will be used to deploy the service
along with desired ServiceTemplate version.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>values</b></td>
        <td>string</td>
        <td>
          Values is the helm values to be passed to the chart used by the template.
The string type is used in order to allow for templating.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#multiclusterservicespecservicespecservicesindexvaluesfromindex-1">valuesFrom</a></b></td>
        <td>[]object</td>
        <td>
          ValuesFrom can reference a ConfigMap or Secret containing helm values.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.spec.serviceSpec.services[index].valuesFrom[index]
<sup><sup>[↩ Parent](#multiclusterservicespecservicespecservicesindex-1)</sup></sup>





<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>kind</b></td>
        <td>enum</td>
        <td>
          Kind of the resource. Supported kinds are:
- ConfigMap/Secret<br/>
          <br/>
            <i>Enum</i>: ConfigMap, Secret<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referenced resource.
Name can be expressed as a template and instantiate using any cluster field.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace of the referenced resource.
For ClusterProfile namespace can be left empty. In such a case, namespace will
be implicit set to cluster's namespace.
For Profile namespace must be left empty. The Profile namespace will be used.
Namespace can be expressed as a template and instantiate using any cluster field.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>optional</b></td>
        <td>boolean</td>
        <td>
          Optional indicates that the referenced resource is not mandatory.
If set to true and the resource is not found, the error will be ignored,
and Sveltos will continue processing other ValueFroms.<br/>
          <br/>
            <i>Default</i>: false<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.spec.serviceSpec.templateResourceRefs[index]
<sup><sup>[↩ Parent](#multiclusterservicespecservicespec-1)</sup></sup>





<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>identifier</b></td>
        <td>string</td>
        <td>
          Identifier is how the resource will be referred to in the
template<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#multiclusterservicespecservicespectemplateresourcerefsindexresource-1">resource</a></b></td>
        <td>object</td>
        <td>
          Resource references a Kubernetes instance in the management
cluster to fetch and use during template instantiation.
For ClusterProfile namespace can be left empty. In such a case, namespace will
be implicit set to cluster's namespace.
Name and namespace can be expressed as a template and instantiate using any cluster field.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>optional</b></td>
        <td>boolean</td>
        <td>
          Optional indicates that the referenced resource is not mandatory.
If set to true and the resource is not found, the error will be ignored,
and Sveltos will continue processing other TemplateResourceRefs.<br/>
          <br/>
            <i>Default</i>: false<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.spec.serviceSpec.templateResourceRefs[index].resource
<sup><sup>[↩ Parent](#multiclusterservicespecservicespectemplateresourcerefsindex-1)</sup></sup>



Resource references a Kubernetes instance in the management
cluster to fetch and use during template instantiation.
For ClusterProfile namespace can be left empty. In such a case, namespace will
be implicit set to cluster's namespace.
Name and namespace can be expressed as a template and instantiate using any cluster field.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>apiVersion</b></td>
        <td>string</td>
        <td>
          API version of the referent.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>fieldPath</b></td>
        <td>string</td>
        <td>
          If referring to a piece of an object instead of an entire object, this string
should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2].
For example, if the object reference is to a container within a pod, this would take on a value like:
"spec.containers{name}" (where "name" refers to the name of the container that triggered
the event) or if no container name is specified "spec.containers[2]" (container with
index 2 in this pod). This syntax is chosen only to have some well-defined way of
referencing a part of an object.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>kind</b></td>
        <td>string</td>
        <td>
          Kind of the referent.
More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.
More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace of the referent.
More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>resourceVersion</b></td>
        <td>string</td>
        <td>
          Specific resourceVersion to which this reference is made, if any.
More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>uid</b></td>
        <td>string</td>
        <td>
          UID of the referent.
More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.status
<sup><sup>[↩ Parent](#multiclusterservice-1)</sup></sup>



MultiClusterServiceStatus defines the observed state of MultiClusterService.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#multiclusterservicestatusconditionsindex-1">conditions</a></b></td>
        <td>[]object</td>
        <td>
          Conditions contains details for the current state of the MultiClusterService.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>observedGeneration</b></td>
        <td>integer</td>
        <td>
          ObservedGeneration is the last observed generation.<br/>
          <br/>
            <i>Format</i>: int64<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#multiclusterservicestatusservicesindex-1">services</a></b></td>
        <td>[]object</td>
        <td>
          Services contains details for the state of services.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#multiclusterservicestatusservicesupgradepathsindex-1">servicesUpgradePaths</a></b></td>
        <td>[]object</td>
        <td>
          ServicesUpgradePaths contains details for the state of services upgrade paths.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.status.conditions[index]
<sup><sup>[↩ Parent](#multiclusterservicestatus-1)</sup></sup>



Condition contains details for one aspect of the current state of this API Resource.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>lastTransitionTime</b></td>
        <td>string</td>
        <td>
          lastTransitionTime is the last time the condition transitioned from one status to another.
This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable.<br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>message</b></td>
        <td>string</td>
        <td>
          message is a human readable message indicating details about the transition.
This may be an empty string.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>reason</b></td>
        <td>string</td>
        <td>
          reason contains a programmatic identifier indicating the reason for the condition's last transition.
Producers of specific condition types may define expected values and meanings for this field,
and whether the values are considered a guaranteed API.
The value should be a CamelCase string.
This field may not be empty.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>status</b></td>
        <td>enum</td>
        <td>
          status of the condition, one of True, False, Unknown.<br/>
          <br/>
            <i>Enum</i>: True, False, Unknown<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>type</b></td>
        <td>string</td>
        <td>
          type of condition in CamelCase or in foo.example.com/CamelCase.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>observedGeneration</b></td>
        <td>integer</td>
        <td>
          observedGeneration represents the .metadata.generation that the condition was set based upon.
For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date
with respect to the current state of the instance.<br/>
          <br/>
            <i>Format</i>: int64<br/>
            <i>Minimum</i>: 0<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.status.services[index]
<sup><sup>[↩ Parent](#multiclusterservicestatus-1)</sup></sup>



ServiceStatus contains details for the state of services.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>clusterName</b></td>
        <td>string</td>
        <td>
          ClusterName is the name of the associated cluster.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>clusterNamespace</b></td>
        <td>string</td>
        <td>
          ClusterNamespace is the namespace of the associated cluster.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#multiclusterservicestatusservicesindexconditionsindex-1">conditions</a></b></td>
        <td>[]object</td>
        <td>
          Conditions contains details for the current state of managed services.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.status.services[index].conditions[index]
<sup><sup>[↩ Parent](#multiclusterservicestatusservicesindex-1)</sup></sup>



Condition contains details for one aspect of the current state of this API Resource.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>lastTransitionTime</b></td>
        <td>string</td>
        <td>
          lastTransitionTime is the last time the condition transitioned from one status to another.
This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable.<br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>message</b></td>
        <td>string</td>
        <td>
          message is a human readable message indicating details about the transition.
This may be an empty string.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>reason</b></td>
        <td>string</td>
        <td>
          reason contains a programmatic identifier indicating the reason for the condition's last transition.
Producers of specific condition types may define expected values and meanings for this field,
and whether the values are considered a guaranteed API.
The value should be a CamelCase string.
This field may not be empty.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>status</b></td>
        <td>enum</td>
        <td>
          status of the condition, one of True, False, Unknown.<br/>
          <br/>
            <i>Enum</i>: True, False, Unknown<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>type</b></td>
        <td>string</td>
        <td>
          type of condition in CamelCase or in foo.example.com/CamelCase.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>observedGeneration</b></td>
        <td>integer</td>
        <td>
          observedGeneration represents the .metadata.generation that the condition was set based upon.
For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date
with respect to the current state of the instance.<br/>
          <br/>
            <i>Format</i>: int64<br/>
            <i>Minimum</i>: 0<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.status.servicesUpgradePaths[index]
<sup><sup>[↩ Parent](#multiclusterservicestatus-1)</sup></sup>



ServiceUpgradePaths contains details for the state of service upgrade paths.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name is the name of the service.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace is the namespace of the service.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>template</b></td>
        <td>string</td>
        <td>
          Template is the name of the current service template.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#multiclusterservicestatusservicesupgradepathsindexavailableupgradesindex-1">availableUpgrades</a></b></td>
        <td>[]object</td>
        <td>
          AvailableUpgrades contains details for the state of available upgrades.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.status.servicesUpgradePaths[index].availableUpgrades[index]
<sup><sup>[↩ Parent](#multiclusterservicestatusservicesupgradepathsindex-1)</sup></sup>



UpgradePath contains details for the state of service upgrade paths.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>upgradePaths</b></td>
        <td>[]string</td>
        <td>
          Versions contains the list of versions that service can be upgraded to.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>

## ProviderInterface
<sup><sup>[↩ Parent](#k0rdentmirantiscomv1beta1 )</sup></sup>






ProviderInterface is the Schema for the ProviderInterface API

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
      <td><b>apiVersion</b></td>
      <td>string</td>
      <td>k0rdent.mirantis.com/v1beta1</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b>kind</b></td>
      <td>string</td>
      <td>ProviderInterface</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#providerinterfacespec-1">spec</a></b></td>
        <td>object</td>
        <td>
          ProviderInterfaceSpec defines the desired state of ProviderInterface<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providerinterfacestatus-1">status</a></b></td>
        <td>object</td>
        <td>
          ProviderInterfaceStatus defines the observed state of ProviderInterface<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderInterface.spec
<sup><sup>[↩ Parent](#providerinterface-1)</sup></sup>



ProviderInterfaceSpec defines the desired state of ProviderInterface

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#providerinterfacespecclustergvksindex-1">clusterGVKs</a></b></td>
        <td>[]object</td>
        <td>
          ClusterGVKs defines the Group-Version-Kind resources this provider can manage<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>clusterIdentityKinds</b></td>
        <td>[]string</td>
        <td>
          ClusterIdentityKinds defines the Kind of identity objects supported by this provider<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>description</b></td>
        <td>string</td>
        <td>
          Description provides a human-readable explanation of what this provider does<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderInterface.spec.clusterGVKs[index]
<sup><sup>[↩ Parent](#providerinterfacespec-1)</sup></sup>



GroupVersionKind unambiguously identifies a kind. It doesn't anonymously include GroupVersion
to avoid automatic coercion. It doesn't use a GroupVersion to avoid custom marshalling
Note: mirror of https://github.com/kubernetes/apimachinery/blob/v0.32.3/pkg/runtime/schema/group_version.go#L140-L146

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>group</b></td>
        <td>string</td>
        <td>
          <br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>kind</b></td>
        <td>string</td>
        <td>
          <br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>version</b></td>
        <td>string</td>
        <td>
          <br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ProviderInterface.status
<sup><sup>[↩ Parent](#providerinterface-1)</sup></sup>



ProviderInterfaceStatus defines the observed state of ProviderInterface

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>exposedProviders</b></td>
        <td>string</td>
        <td>
          ExposedProviders contains the list of exposed provider<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>

## ProviderTemplate
<sup><sup>[↩ Parent](#k0rdentmirantiscomv1beta1 )</sup></sup>






ProviderTemplate is the Schema for the providertemplates API

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
      <td><b>apiVersion</b></td>
      <td>string</td>
      <td>k0rdent.mirantis.com/v1beta1</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b>kind</b></td>
      <td>string</td>
      <td>ProviderTemplate</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#providertemplatespec-1">spec</a></b></td>
        <td>object</td>
        <td>
          ProviderTemplateSpec defines the desired state of ProviderTemplate<br/>
          <br/>
            <i>Validations</i>:<li>self == oldSelf: Spec is immutable</li><li>!has(self.helm.chartSource): .spec.helm.chartSource is not supported for ProviderTemplates</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatestatus-1">status</a></b></td>
        <td>object</td>
        <td>
          ProviderTemplateStatus defines the observed state of ProviderTemplate<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec
<sup><sup>[↩ Parent](#providertemplate-1)</sup></sup>



ProviderTemplateSpec defines the desired state of ProviderTemplate

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>capiContracts</b></td>
        <td>map[string]string</td>
        <td>
          Holds key-value pairs with compatibility [contract versions],
where the key is the core CAPI contract version,
and the value is an underscore-delimited (_) list of provider contract versions
supported by the core CAPI.

[contract versions]: https://cluster-api.sigs.k8s.io/developer/providers/contracts<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelm-1">helm</a></b></td>
        <td>object</td>
        <td>
          HelmSpec references a Helm chart representing the KCM template<br/>
          <br/>
            <i>Validations</i>:<li>(has(self.chartSpec) ? (!has(self.chartSource) && !has(self.chartRef)): true): chartSpec, chartSource and chartRef are mutually exclusive</li><li>(has(self.chartSource) ? (!has(self.chartSpec) && !has(self.chartRef)): true): chartSpec, chartSource and chartRef are mutually exclusive</li><li>(has(self.chartRef) ? (!has(self.chartSpec) && !has(self.chartSource)): true): chartSpec, chartSource and chartRef are mutually exclusive</li><li>has(self.chartSpec) || has(self.chartRef) || has(self.chartSource): one of chartSpec, chartRef or chartSource must be set</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>providers</b></td>
        <td>[]string</td>
        <td>
          Providers represent exposed CAPI providers.
Should be set if not present in the Helm chart metadata.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm
<sup><sup>[↩ Parent](#providertemplatespec-1)</sup></sup>



HelmSpec references a Helm chart representing the KCM template

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#providertemplatespechelmchartref-1">chartRef</a></b></td>
        <td>object</td>
        <td>
          ChartRef is a reference to a source controller resource containing the
Helm chart representing the template.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsource-1">chartSource</a></b></td>
        <td>object</td>
        <td>
          ChartSource is a source of a Helm chart representing the template.<br/>
          <br/>
            <i>Validations</i>:<li>has(self.localSourceRef) ? (self.localSourceRef.kind != 'Secret' && self.localSourceRef.kind != 'ConfigMap'): true: Secret and ConfigMap are not supported as Helm chart sources</li><li>has(self.localSourceRef) ? !has(self.remoteSourceSpec): true: LocalSource and RemoteSource are mutually exclusive.</li><li>has(self.remoteSourceSpec) ? !has(self.localSourceRef): true: LocalSource and RemoteSource are mutually exclusive.</li><li>has(self.localSourceRef) || has(self.remoteSourceSpec): One of LocalSource or RemoteSource must be specified.</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartspec-1">chartSpec</a></b></td>
        <td>object</td>
        <td>
          ChartSpec defines the desired state of the HelmChart to be created by the controller<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartRef
<sup><sup>[↩ Parent](#providertemplatespechelm-1)</sup></sup>



ChartRef is a reference to a source controller resource containing the
Helm chart representing the template.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>kind</b></td>
        <td>enum</td>
        <td>
          Kind of the referent.<br/>
          <br/>
            <i>Enum</i>: OCIRepository, HelmChart<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>apiVersion</b></td>
        <td>string</td>
        <td>
          APIVersion of the referent.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace of the referent, defaults to the namespace of the Kubernetes
resource object that contains the reference.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource
<sup><sup>[↩ Parent](#providertemplatespechelm-1)</sup></sup>



ChartSource is a source of a Helm chart representing the template.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>deploymentType</b></td>
        <td>enum</td>
        <td>
          DeploymentType is the type of the deployment. This field is ignored,
when ResourceSpec is used as part of Helm chart configuration.<br/>
          <br/>
            <i>Enum</i>: Local, Remote<br/>
            <i>Default</i>: Remote<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>path</b></td>
        <td>string</td>
        <td>
          Path to the directory containing the resource manifest.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourcelocalsourceref-1">localSourceRef</a></b></td>
        <td>object</td>
        <td>
          LocalSourceRef is the local source of the kustomize manifest.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespec-1">remoteSourceSpec</a></b></td>
        <td>object</td>
        <td>
          RemoteSourceSpec is the remote source of the kustomize manifest.<br/>
          <br/>
            <i>Validations</i>:<li>has(self.git) ? (!has(self.bucket) && !has(self.oci)) : true: Git, Bucket and OCI are mutually exclusive.</li><li>has(self.bucket) ? (!has(self.git) && !has(self.oci)) : true: Git, Bucket and OCI are mutually exclusive.</li><li>has(self.oci) ? (!has(self.git) && !has(self.bucket)) : true: Git, Bucket and OCI are mutually exclusive.</li><li>has(self.git) || has(self.bucket) || has(self.oci): One of Git, Bucket or OCI must be specified.</li>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.localSourceRef
<sup><sup>[↩ Parent](#providertemplatespechelmchartsource-1)</sup></sup>



LocalSourceRef is the local source of the kustomize manifest.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>kind</b></td>
        <td>enum</td>
        <td>
          Kind is the kind of the local source.<br/>
          <br/>
            <i>Enum</i>: ConfigMap, Secret, GitRepository, Bucket, OCIRepository<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name is the name of the local source.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace is the namespace of the local source. Cross-namespace references
are only allowed when the Kind is one of [github.com/fluxcd/source-controller/api/v1.GitRepository],
[github.com/fluxcd/source-controller/api/v1.Bucket] or [github.com/fluxcd/source-controller/api/v1beta2.OCIRepository].
If the Kind is ConfigMap or Secret, the namespace will be ignored.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec
<sup><sup>[↩ Parent](#providertemplatespechelmchartsource-1)</sup></sup>



RemoteSourceSpec is the remote source of the kustomize manifest.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecbucket-1">bucket</a></b></td>
        <td>object</td>
        <td>
          Bucket is the definition of bucket source.<br/>
          <br/>
            <i>Validations</i>:<li>self.provider == 'aws' || self.provider == 'generic' || !has(self.sts): STS configuration is only supported for the 'aws' and 'generic' Bucket providers</li><li>self.provider != 'aws' || !has(self.sts) || self.sts.provider == 'aws': 'aws' is the only supported STS provider for the 'aws' Bucket provider</li><li>self.provider != 'generic' || !has(self.sts) || self.sts.provider == 'ldap': 'ldap' is the only supported STS provider for the 'generic' Bucket provider</li><li>!has(self.sts) || self.sts.provider != 'aws' || !has(self.sts.secretRef): spec.sts.secretRef is not required for the 'aws' STS provider</li><li>!has(self.sts) || self.sts.provider != 'aws' || !has(self.sts.certSecretRef): spec.sts.certSecretRef is not required for the 'aws' STS provider</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecgit-1">git</a></b></td>
        <td>object</td>
        <td>
          Git is the definition of git repository source.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecoci-1">oci</a></b></td>
        <td>object</td>
        <td>
          OCI is the definition of OCI repository source.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.bucket
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespec-1)</sup></sup>



Bucket is the definition of bucket source.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>bucketName</b></td>
        <td>string</td>
        <td>
          BucketName is the name of the object storage bucket.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>endpoint</b></td>
        <td>string</td>
        <td>
          Endpoint is the object storage address the BucketName is located at.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>interval</b></td>
        <td>string</td>
        <td>
          Interval at which the Bucket Endpoint is checked for updates.
This interval is approximate and may be subject to jitter to ensure
efficient use of resources.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecbucketcertsecretref-1">certSecretRef</a></b></td>
        <td>object</td>
        <td>
          CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
bucket. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

This field is only supported for the `generic` provider.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>ignore</b></td>
        <td>string</td>
        <td>
          Ignore overrides the set of excluded patterns in the .sourceignore format
(which is the same as .gitignore). If not provided, a default will be used,
consult the documentation for your version to find out what those are.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>insecure</b></td>
        <td>boolean</td>
        <td>
          Insecure allows connecting to a non-TLS HTTP Endpoint.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>prefix</b></td>
        <td>string</td>
        <td>
          Prefix to use for server-side filtering of files in the Bucket.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider of the object storage bucket.
Defaults to 'generic', which expects an S3 (API) compatible object
storage.<br/>
          <br/>
            <i>Enum</i>: generic, aws, gcp, azure<br/>
            <i>Default</i>: generic<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecbucketproxysecretref-1">proxySecretRef</a></b></td>
        <td>object</td>
        <td>
          ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the Bucket server.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>region</b></td>
        <td>string</td>
        <td>
          Region of the Endpoint where the BucketName is located in.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecbucketsecretref-1">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing authentication credentials
for the Bucket.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecbucketsts-1">sts</a></b></td>
        <td>object</td>
        <td>
          STS specifies the required configuration to use a Security Token
Service for fetching temporary credentials to authenticate in a
Bucket provider.

This field is only supported for the `aws` and `generic` providers.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>suspend</b></td>
        <td>boolean</td>
        <td>
          Suspend tells the controller to suspend the reconciliation of this
Bucket.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>timeout</b></td>
        <td>string</td>
        <td>
          Timeout for fetch operations, defaults to 60s.<br/>
          <br/>
            <i>Default</i>: 60s<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.bucket.certSecretRef
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespecbucket-1)</sup></sup>



CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
bucket. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

This field is only supported for the `generic` provider.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.bucket.proxySecretRef
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespecbucket-1)</sup></sup>



ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the Bucket server.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.bucket.secretRef
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespecbucket-1)</sup></sup>



SecretRef specifies the Secret containing authentication credentials
for the Bucket.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.bucket.sts
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespecbucket-1)</sup></sup>



STS specifies the required configuration to use a Security Token
Service for fetching temporary credentials to authenticate in a
Bucket provider.

This field is only supported for the `aws` and `generic` providers.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>endpoint</b></td>
        <td>string</td>
        <td>
          Endpoint is the HTTP/S endpoint of the Security Token Service from
where temporary credentials will be fetched.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider of the Security Token Service.<br/>
          <br/>
            <i>Enum</i>: aws, ldap<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecbucketstscertsecretref-1">certSecretRef</a></b></td>
        <td>object</td>
        <td>
          CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
STS endpoint. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

This field is only supported for the `ldap` provider.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecbucketstssecretref-1">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing authentication credentials
for the STS endpoint. This Secret must contain the fields `username`
and `password` and is supported only for the `ldap` provider.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.bucket.sts.certSecretRef
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespecbucketsts-1)</sup></sup>



CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
STS endpoint. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

This field is only supported for the `ldap` provider.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.bucket.sts.secretRef
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespecbucketsts-1)</sup></sup>



SecretRef specifies the Secret containing authentication credentials
for the STS endpoint. This Secret must contain the fields `username`
and `password` and is supported only for the `ldap` provider.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.git
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespec-1)</sup></sup>



Git is the definition of git repository source.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>interval</b></td>
        <td>string</td>
        <td>
          Interval at which the GitRepository URL is checked for updates.
This interval is approximate and may be subject to jitter to ensure
efficient use of resources.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>url</b></td>
        <td>string</td>
        <td>
          URL specifies the Git repository URL, it can be an HTTP/S or SSH address.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>ignore</b></td>
        <td>string</td>
        <td>
          Ignore overrides the set of excluded patterns in the .sourceignore format
(which is the same as .gitignore). If not provided, a default will be used,
consult the documentation for your version to find out what those are.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecgitincludeindex-1">include</a></b></td>
        <td>[]object</td>
        <td>
          Include specifies a list of GitRepository resources which Artifacts
should be included in the Artifact produced for this GitRepository.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider used for authentication, can be 'azure', 'github', 'generic'.
When not specified, defaults to 'generic'.<br/>
          <br/>
            <i>Enum</i>: generic, azure, github<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecgitproxysecretref-1">proxySecretRef</a></b></td>
        <td>object</td>
        <td>
          ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the Git server.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>recurseSubmodules</b></td>
        <td>boolean</td>
        <td>
          RecurseSubmodules enables the initialization of all submodules within
the GitRepository as cloned from the URL, using their default settings.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecgitref-1">ref</a></b></td>
        <td>object</td>
        <td>
          Reference specifies the Git reference to resolve and monitor for
changes, defaults to the 'master' branch.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecgitsecretref-1">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing authentication credentials for
the GitRepository.
For HTTPS repositories the Secret must contain 'username' and 'password'
fields for basic auth or 'bearerToken' field for token auth.
For SSH repositories the Secret must contain 'identity'
and 'known_hosts' fields.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>suspend</b></td>
        <td>boolean</td>
        <td>
          Suspend tells the controller to suspend the reconciliation of this
GitRepository.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>timeout</b></td>
        <td>string</td>
        <td>
          Timeout for Git operations like cloning, defaults to 60s.<br/>
          <br/>
            <i>Default</i>: 60s<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecgitverify-1">verify</a></b></td>
        <td>object</td>
        <td>
          Verification specifies the configuration to verify the Git commit
signature(s).<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.git.include[index]
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespecgit-1)</sup></sup>



GitRepositoryInclude specifies a local reference to a GitRepository which
Artifact (sub-)contents must be included, and where they should be placed.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecgitincludeindexrepository-1">repository</a></b></td>
        <td>object</td>
        <td>
          GitRepositoryRef specifies the GitRepository which Artifact contents
must be included.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>fromPath</b></td>
        <td>string</td>
        <td>
          FromPath specifies the path to copy contents from, defaults to the root
of the Artifact.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>toPath</b></td>
        <td>string</td>
        <td>
          ToPath specifies the path to copy contents to, defaults to the name of
the GitRepositoryRef.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.git.include[index].repository
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespecgitincludeindex-1)</sup></sup>



GitRepositoryRef specifies the GitRepository which Artifact contents
must be included.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.git.proxySecretRef
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespecgit-1)</sup></sup>



ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the Git server.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.git.ref
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespecgit-1)</sup></sup>



Reference specifies the Git reference to resolve and monitor for
changes, defaults to the 'master' branch.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>branch</b></td>
        <td>string</td>
        <td>
          Branch to check out, defaults to 'master' if no other field is defined.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>commit</b></td>
        <td>string</td>
        <td>
          Commit SHA to check out, takes precedence over all reference fields.

This can be combined with Branch to shallow clone the branch, in which
the commit is expected to exist.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the reference to check out; takes precedence over Branch, Tag and SemVer.

It must be a valid Git reference: https://git-scm.com/docs/git-check-ref-format#_description
Examples: "refs/heads/main", "refs/tags/v0.1.0", "refs/pull/420/head", "refs/merge-requests/1/head"<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>semver</b></td>
        <td>string</td>
        <td>
          SemVer tag expression to check out, takes precedence over Tag.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>tag</b></td>
        <td>string</td>
        <td>
          Tag to check out, takes precedence over Branch.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.git.secretRef
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespecgit-1)</sup></sup>



SecretRef specifies the Secret containing authentication credentials for
the GitRepository.
For HTTPS repositories the Secret must contain 'username' and 'password'
fields for basic auth or 'bearerToken' field for token auth.
For SSH repositories the Secret must contain 'identity'
and 'known_hosts' fields.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.git.verify
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespecgit-1)</sup></sup>



Verification specifies the configuration to verify the Git commit
signature(s).

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecgitverifysecretref-1">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing the public keys of trusted Git
authors.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>mode</b></td>
        <td>enum</td>
        <td>
          Mode specifies which Git object(s) should be verified.

The variants "head" and "HEAD" both imply the same thing, i.e. verify
the commit that the HEAD of the Git repository points to. The variant
"head" solely exists to ensure backwards compatibility.<br/>
          <br/>
            <i>Enum</i>: head, HEAD, Tag, TagAndHEAD<br/>
            <i>Default</i>: HEAD<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.git.verify.secretRef
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespecgitverify-1)</sup></sup>



SecretRef specifies the Secret containing the public keys of trusted Git
authors.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.oci
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespec-1)</sup></sup>



OCI is the definition of OCI repository source.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>interval</b></td>
        <td>string</td>
        <td>
          Interval at which the OCIRepository URL is checked for updates.
This interval is approximate and may be subject to jitter to ensure
efficient use of resources.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>url</b></td>
        <td>string</td>
        <td>
          URL is a reference to an OCI artifact repository hosted
on a remote container registry.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecocicertsecretref-1">certSecretRef</a></b></td>
        <td>object</td>
        <td>
          CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
registry. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

Note: Support for the `caFile`, `certFile` and `keyFile` keys have
been deprecated.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>ignore</b></td>
        <td>string</td>
        <td>
          Ignore overrides the set of excluded patterns in the .sourceignore format
(which is the same as .gitignore). If not provided, a default will be used,
consult the documentation for your version to find out what those are.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>insecure</b></td>
        <td>boolean</td>
        <td>
          Insecure allows connecting to a non-TLS HTTP container registry.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecocilayerselector-1">layerSelector</a></b></td>
        <td>object</td>
        <td>
          LayerSelector specifies which layer should be extracted from the OCI artifact.
When not specified, the first layer found in the artifact is selected.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          The provider used for authentication, can be 'aws', 'azure', 'gcp' or 'generic'.
When not specified, defaults to 'generic'.<br/>
          <br/>
            <i>Enum</i>: generic, aws, azure, gcp<br/>
            <i>Default</i>: generic<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecociproxysecretref-1">proxySecretRef</a></b></td>
        <td>object</td>
        <td>
          ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the container registry.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecociref-1">ref</a></b></td>
        <td>object</td>
        <td>
          The OCI reference to pull and monitor for changes,
defaults to the latest tag.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecocisecretref-1">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef contains the secret name containing the registry login
credentials to resolve image metadata.
The secret must be of type kubernetes.io/dockerconfigjson.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>serviceAccountName</b></td>
        <td>string</td>
        <td>
          ServiceAccountName is the name of the Kubernetes ServiceAccount used to authenticate
the image pull if the service account has attached pull secrets. For more information:
https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#add-imagepullsecrets-to-a-service-account<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>suspend</b></td>
        <td>boolean</td>
        <td>
          This flag tells the controller to suspend the reconciliation of this source.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>timeout</b></td>
        <td>string</td>
        <td>
          The timeout for remote OCI Repository operations like pulling, defaults to 60s.<br/>
          <br/>
            <i>Default</i>: 60s<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecociverify-1">verify</a></b></td>
        <td>object</td>
        <td>
          Verify contains the secret name containing the trusted public keys
used to verify the signature and specifies which provider to use to check
whether OCI image is authentic.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.oci.certSecretRef
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespecoci-1)</sup></sup>



CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
registry. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

Note: Support for the `caFile`, `certFile` and `keyFile` keys have
been deprecated.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.oci.layerSelector
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespecoci-1)</sup></sup>



LayerSelector specifies which layer should be extracted from the OCI artifact.
When not specified, the first layer found in the artifact is selected.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>mediaType</b></td>
        <td>string</td>
        <td>
          MediaType specifies the OCI media type of the layer
which should be extracted from the OCI Artifact. The
first layer matching this type is selected.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>operation</b></td>
        <td>enum</td>
        <td>
          Operation specifies how the selected layer should be processed.
By default, the layer compressed content is extracted to storage.
When the operation is set to 'copy', the layer compressed content
is persisted to storage as it is.<br/>
          <br/>
            <i>Enum</i>: extract, copy<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.oci.proxySecretRef
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespecoci-1)</sup></sup>



ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the container registry.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.oci.ref
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespecoci-1)</sup></sup>



The OCI reference to pull and monitor for changes,
defaults to the latest tag.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>digest</b></td>
        <td>string</td>
        <td>
          Digest is the image digest to pull, takes precedence over SemVer.
The value should be in the format 'sha256:<HASH>'.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>semver</b></td>
        <td>string</td>
        <td>
          SemVer is the range of tags to pull selecting the latest within
the range, takes precedence over Tag.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>semverFilter</b></td>
        <td>string</td>
        <td>
          SemverFilter is a regex pattern to filter the tags within the SemVer range.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>tag</b></td>
        <td>string</td>
        <td>
          Tag is the image tag to pull, defaults to latest.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.oci.secretRef
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespecoci-1)</sup></sup>



SecretRef contains the secret name containing the registry login
credentials to resolve image metadata.
The secret must be of type kubernetes.io/dockerconfigjson.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.oci.verify
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespecoci-1)</sup></sup>



Verify contains the secret name containing the trusted public keys
used to verify the signature and specifies which provider to use to check
whether OCI image is authentic.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider specifies the technology used to sign the OCI Artifact.<br/>
          <br/>
            <i>Enum</i>: cosign, notation<br/>
            <i>Default</i>: cosign<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecociverifymatchoidcidentityindex-1">matchOIDCIdentity</a></b></td>
        <td>[]object</td>
        <td>
          MatchOIDCIdentity specifies the identity matching criteria to use
while verifying an OCI artifact which was signed using Cosign keyless
signing. The artifact's identity is deemed to be verified if any of the
specified matchers match against the identity.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartsourceremotesourcespecociverifysecretref-1">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Kubernetes Secret containing the
trusted public keys.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.oci.verify.matchOIDCIdentity[index]
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespecociverify-1)</sup></sup>



OIDCIdentityMatch specifies options for verifying the certificate identity,
i.e. the issuer and the subject of the certificate.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>issuer</b></td>
        <td>string</td>
        <td>
          Issuer specifies the regex pattern to match against to verify
the OIDC issuer in the Fulcio certificate. The pattern must be a
valid Go regular expression.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>subject</b></td>
        <td>string</td>
        <td>
          Subject specifies the regex pattern to match against to verify
the identity subject in the Fulcio certificate. The pattern must
be a valid Go regular expression.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.oci.verify.secretRef
<sup><sup>[↩ Parent](#providertemplatespechelmchartsourceremotesourcespecociverify-1)</sup></sup>



SecretRef specifies the Kubernetes Secret containing the
trusted public keys.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSpec
<sup><sup>[↩ Parent](#providertemplatespechelm-1)</sup></sup>



ChartSpec defines the desired state of the HelmChart to be created by the controller

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>chart</b></td>
        <td>string</td>
        <td>
          Chart is the name or path the Helm chart is available at in the
SourceRef.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>interval</b></td>
        <td>string</td>
        <td>
          Interval at which the HelmChart SourceRef is checked for updates.
This interval is approximate and may be subject to jitter to ensure
efficient use of resources.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartspecsourceref-1">sourceRef</a></b></td>
        <td>object</td>
        <td>
          SourceRef is the reference to the Source the chart is available at.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>ignoreMissingValuesFiles</b></td>
        <td>boolean</td>
        <td>
          IgnoreMissingValuesFiles controls whether to silently ignore missing values
files rather than failing.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>reconcileStrategy</b></td>
        <td>enum</td>
        <td>
          ReconcileStrategy determines what enables the creation of a new artifact.
Valid values are ('ChartVersion', 'Revision').
See the documentation of the values for an explanation on their behavior.
Defaults to ChartVersion when omitted.<br/>
          <br/>
            <i>Enum</i>: ChartVersion, Revision<br/>
            <i>Default</i>: ChartVersion<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>suspend</b></td>
        <td>boolean</td>
        <td>
          Suspend tells the controller to suspend the reconciliation of this
source.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>valuesFiles</b></td>
        <td>[]string</td>
        <td>
          ValuesFiles is an alternative list of values files to use as the chart
values (values.yaml is not included by default), expected to be a
relative path in the SourceRef.
Values files are merged in the order of this list with the last file
overriding the first. Ignored when omitted.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartspecverify-1">verify</a></b></td>
        <td>object</td>
        <td>
          Verify contains the secret name containing the trusted public keys
used to verify the signature and specifies which provider to use to check
whether OCI image is authentic.
This field is only supported when using HelmRepository source with spec.type 'oci'.
Chart dependencies, which are not bundled in the umbrella chart artifact, are not verified.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>version</b></td>
        <td>string</td>
        <td>
          Version is the chart version semver expression, ignored for charts from
GitRepository and Bucket sources. Defaults to latest when omitted.<br/>
          <br/>
            <i>Default</i>: *<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSpec.sourceRef
<sup><sup>[↩ Parent](#providertemplatespechelmchartspec-1)</sup></sup>



SourceRef is the reference to the Source the chart is available at.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>kind</b></td>
        <td>enum</td>
        <td>
          Kind of the referent, valid values are ('HelmRepository', 'GitRepository',
'Bucket').<br/>
          <br/>
            <i>Enum</i>: HelmRepository, GitRepository, Bucket<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>apiVersion</b></td>
        <td>string</td>
        <td>
          APIVersion of the referent.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSpec.verify
<sup><sup>[↩ Parent](#providertemplatespechelmchartspec-1)</sup></sup>



Verify contains the secret name containing the trusted public keys
used to verify the signature and specifies which provider to use to check
whether OCI image is authentic.
This field is only supported when using HelmRepository source with spec.type 'oci'.
Chart dependencies, which are not bundled in the umbrella chart artifact, are not verified.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider specifies the technology used to sign the OCI Artifact.<br/>
          <br/>
            <i>Enum</i>: cosign, notation<br/>
            <i>Default</i>: cosign<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartspecverifymatchoidcidentityindex-1">matchOIDCIdentity</a></b></td>
        <td>[]object</td>
        <td>
          MatchOIDCIdentity specifies the identity matching criteria to use
while verifying an OCI artifact which was signed using Cosign keyless
signing. The artifact's identity is deemed to be verified if any of the
specified matchers match against the identity.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatespechelmchartspecverifysecretref-1">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Kubernetes Secret containing the
trusted public keys.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSpec.verify.matchOIDCIdentity[index]
<sup><sup>[↩ Parent](#providertemplatespechelmchartspecverify-1)</sup></sup>



OIDCIdentityMatch specifies options for verifying the certificate identity,
i.e. the issuer and the subject of the certificate.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>issuer</b></td>
        <td>string</td>
        <td>
          Issuer specifies the regex pattern to match against to verify
the OIDC issuer in the Fulcio certificate. The pattern must be a
valid Go regular expression.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>subject</b></td>
        <td>string</td>
        <td>
          Subject specifies the regex pattern to match against to verify
the identity subject in the Fulcio certificate. The pattern must
be a valid Go regular expression.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSpec.verify.secretRef
<sup><sup>[↩ Parent](#providertemplatespechelmchartspecverify-1)</sup></sup>



SecretRef specifies the Kubernetes Secret containing the
trusted public keys.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ProviderTemplate.status
<sup><sup>[↩ Parent](#providertemplate-1)</sup></sup>



ProviderTemplateStatus defines the observed state of ProviderTemplate

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>valid</b></td>
        <td>boolean</td>
        <td>
          Valid indicates whether the template passed validation or not.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>capiContracts</b></td>
        <td>map[string]string</td>
        <td>
          Holds key-value pairs with compatibility [contract versions],
where the key is the core CAPI contract version,
and the value is an underscore-delimited (_) list of provider contract versions
supported by the core CAPI.

[contract versions]: https://cluster-api.sigs.k8s.io/developer/providers/contracts<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#providertemplatestatuschartref-1">chartRef</a></b></td>
        <td>object</td>
        <td>
          ChartRef is a reference to a source controller resource containing the
Helm chart representing the template.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>chartVersion</b></td>
        <td>string</td>
        <td>
          ChartVersion represents the version of the Helm Chart associated with this template.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>config</b></td>
        <td>JSON</td>
        <td>
          Config demonstrates available parameters for template customization,
that can be used when creating ClusterDeployment objects.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>description</b></td>
        <td>string</td>
        <td>
          Description contains information about the template.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>observedGeneration</b></td>
        <td>integer</td>
        <td>
          ObservedGeneration is the last observed generation.<br/>
          <br/>
            <i>Format</i>: int64<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>providers</b></td>
        <td>[]string</td>
        <td>
          Providers represent exposed CAPI providers.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>validationError</b></td>
        <td>string</td>
        <td>
          ValidationError provides information regarding issues encountered during template validation.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.status.chartRef
<sup><sup>[↩ Parent](#providertemplatestatus-1)</sup></sup>



ChartRef is a reference to a source controller resource containing the
Helm chart representing the template.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>kind</b></td>
        <td>enum</td>
        <td>
          Kind of the referent.<br/>
          <br/>
            <i>Enum</i>: OCIRepository, HelmChart<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>apiVersion</b></td>
        <td>string</td>
        <td>
          APIVersion of the referent.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace of the referent, defaults to the namespace of the Kubernetes
resource object that contains the reference.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>

## Release
<sup><sup>[↩ Parent](#k0rdentmirantiscomv1beta1 )</sup></sup>






Release is the Schema for the releases API

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
      <td><b>apiVersion</b></td>
      <td>string</td>
      <td>k0rdent.mirantis.com/v1beta1</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b>kind</b></td>
      <td>string</td>
      <td>Release</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#releasespec-1">spec</a></b></td>
        <td>object</td>
        <td>
          ReleaseSpec defines the desired state of Release<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#releasestatus-1">status</a></b></td>
        <td>object</td>
        <td>
          ReleaseStatus defines the observed state of Release<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### Release.spec
<sup><sup>[↩ Parent](#release-1)</sup></sup>



ReleaseSpec defines the desired state of Release

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#releasespeccapi-1">capi</a></b></td>
        <td>object</td>
        <td>
          CAPI references the Cluster API template.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#releasespeckcm-1">kcm</a></b></td>
        <td>object</td>
        <td>
          KCM references the KCM template.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>version</b></td>
        <td>string</td>
        <td>
          Version of the KCM Release in the semver format.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#releasespecprovidersindex-1">providers</a></b></td>
        <td>[]object</td>
        <td>
          Providers contains a list of Providers associated with the Release.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### Release.spec.capi
<sup><sup>[↩ Parent](#releasespec-1)</sup></sup>



CAPI references the Cluster API template.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>template</b></td>
        <td>string</td>
        <td>
          Template references the Template associated with the provider.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### Release.spec.kcm
<sup><sup>[↩ Parent](#releasespec-1)</sup></sup>



KCM references the KCM template.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>template</b></td>
        <td>string</td>
        <td>
          Template references the Template associated with the provider.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### Release.spec.providers[index]
<sup><sup>[↩ Parent](#releasespec-1)</sup></sup>





<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the provider.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>template</b></td>
        <td>string</td>
        <td>
          Template references the Template associated with the provider.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### Release.status
<sup><sup>[↩ Parent](#release-1)</sup></sup>



ReleaseStatus defines the observed state of Release

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#releasestatusconditionsindex-1">conditions</a></b></td>
        <td>[]object</td>
        <td>
          Conditions contains details for the current state of the Release<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>observedGeneration</b></td>
        <td>integer</td>
        <td>
          ObservedGeneration is the last observed generation.<br/>
          <br/>
            <i>Format</i>: int64<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>ready</b></td>
        <td>boolean</td>
        <td>
          Ready indicates whether KCM is ready to be upgraded to this Release.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### Release.status.conditions[index]
<sup><sup>[↩ Parent](#releasestatus-1)</sup></sup>



Condition contains details for one aspect of the current state of this API Resource.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>lastTransitionTime</b></td>
        <td>string</td>
        <td>
          lastTransitionTime is the last time the condition transitioned from one status to another.
This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable.<br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>message</b></td>
        <td>string</td>
        <td>
          message is a human readable message indicating details about the transition.
This may be an empty string.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>reason</b></td>
        <td>string</td>
        <td>
          reason contains a programmatic identifier indicating the reason for the condition's last transition.
Producers of specific condition types may define expected values and meanings for this field,
and whether the values are considered a guaranteed API.
The value should be a CamelCase string.
This field may not be empty.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>status</b></td>
        <td>enum</td>
        <td>
          status of the condition, one of True, False, Unknown.<br/>
          <br/>
            <i>Enum</i>: True, False, Unknown<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>type</b></td>
        <td>string</td>
        <td>
          type of condition in CamelCase or in foo.example.com/CamelCase.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>observedGeneration</b></td>
        <td>integer</td>
        <td>
          observedGeneration represents the .metadata.generation that the condition was set based upon.
For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date
with respect to the current state of the instance.<br/>
          <br/>
            <i>Format</i>: int64<br/>
            <i>Minimum</i>: 0<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>

## ServiceTemplateChain
<sup><sup>[↩ Parent](#k0rdentmirantiscomv1beta1 )</sup></sup>






ServiceTemplateChain is the Schema for the servicetemplatechains API

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
      <td><b>apiVersion</b></td>
      <td>string</td>
      <td>k0rdent.mirantis.com/v1beta1</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b>kind</b></td>
      <td>string</td>
      <td>ServiceTemplateChain</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#servicetemplatechainspec-1">spec</a></b></td>
        <td>object</td>
        <td>
          TemplateChainSpec defines the desired state of *TemplateChain<br/>
          <br/>
            <i>Validations</i>:<li>self == oldSelf: Spec is immutable</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatechainstatus-1">status</a></b></td>
        <td>object</td>
        <td>
          TemplateChainStatus defines the observed state of *TemplateChain<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplateChain.spec
<sup><sup>[↩ Parent](#servicetemplatechain-1)</sup></sup>



TemplateChainSpec defines the desired state of *TemplateChain

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#servicetemplatechainspecsupportedtemplatesindex-1">supportedTemplates</a></b></td>
        <td>[]object</td>
        <td>
          SupportedTemplates is the list of supported Templates definitions and all available upgrade sequences for it.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplateChain.spec.supportedTemplates[index]
<sup><sup>[↩ Parent](#servicetemplatechainspec-1)</sup></sup>



SupportedTemplate is the supported Template definition and all available upgrade sequences for it

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name is the name of the Template.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#servicetemplatechainspecsupportedtemplatesindexavailableupgradesindex-1">availableUpgrades</a></b></td>
        <td>[]object</td>
        <td>
          AvailableUpgrades is the list of available upgrades for the specified Template.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplateChain.spec.supportedTemplates[index].availableUpgrades[index]
<sup><sup>[↩ Parent](#servicetemplatechainspecsupportedtemplatesindex-1)</sup></sup>



AvailableUpgrade is the definition of the available upgrade for the Template

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name is the name of the Template to which the upgrade is available.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplateChain.status
<sup><sup>[↩ Parent](#servicetemplatechain-1)</sup></sup>



TemplateChainStatus defines the observed state of *TemplateChain

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>valid</b></td>
        <td>boolean</td>
        <td>
          Valid indicates whether the chain is valid and can be considered when calculating available
upgrade paths.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>validationError</b></td>
        <td>string</td>
        <td>
          ValidationError provides information regarding issues encountered during templatechain validation.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>

## ServiceTemplate
<sup><sup>[↩ Parent](#k0rdentmirantiscomv1beta1 )</sup></sup>






ServiceTemplate is the Schema for the servicetemplates API

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
      <td><b>apiVersion</b></td>
      <td>string</td>
      <td>k0rdent.mirantis.com/v1beta1</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b>kind</b></td>
      <td>string</td>
      <td>ServiceTemplate</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespec-1">spec</a></b></td>
        <td>object</td>
        <td>
          ServiceTemplateSpec defines the desired state of ServiceTemplate<br/>
          <br/>
            <i>Validations</i>:<li>self == oldSelf: Spec is immutable</li><li>has(self.helm) ? (!has(self.kustomize) && !has(self.resources)): true: Helm, Kustomize and Resources are mutually exclusive.</li><li>has(self.kustomize) ? (!has(self.helm) && !has(self.resources)): true: Helm, Kustomize and Resources are mutually exclusive.</li><li>has(self.resources) ? (!has(self.kustomize) && !has(self.helm)): true: Helm, Kustomize and Resources are mutually exclusive.</li><li>has(self.helm) || has(self.kustomize) || has(self.resources): One of Helm, Kustomize, or Resources must be specified.</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatestatus-1">status</a></b></td>
        <td>object</td>
        <td>
          ServiceTemplateStatus defines the observed state of ServiceTemplate<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec
<sup><sup>[↩ Parent](#servicetemplate-1)</sup></sup>



ServiceTemplateSpec defines the desired state of ServiceTemplate

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#servicetemplatespechelm-1">helm</a></b></td>
        <td>object</td>
        <td>
          Helm contains the Helm chart information for the template.<br/>
          <br/>
            <i>Validations</i>:<li>(has(self.chartSpec) ? (!has(self.chartSource) && !has(self.chartRef)): true): chartSpec, chartSource and chartRef are mutually exclusive</li><li>(has(self.chartSource) ? (!has(self.chartSpec) && !has(self.chartRef)): true): chartSpec, chartSource and chartRef are mutually exclusive</li><li>(has(self.chartRef) ? (!has(self.chartSpec) && !has(self.chartSource)): true): chartSpec, chartSource and chartRef are mutually exclusive</li><li>has(self.chartSpec) || has(self.chartRef) || has(self.chartSource): one of chartSpec, chartRef or chartSource must be set</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>k8sConstraint</b></td>
        <td>string</td>
        <td>
          Constraint describing compatible K8S versions of the cluster set in the SemVer format.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomize-1">kustomize</a></b></td>
        <td>object</td>
        <td>
          Kustomize contains the Kustomize configuration for the template.<br/>
          <br/>
            <i>Validations</i>:<li>has(self.localSourceRef) ? !has(self.remoteSourceSpec): true: LocalSource and RemoteSource are mutually exclusive.</li><li>has(self.remoteSourceSpec) ? !has(self.localSourceRef): true: LocalSource and RemoteSource are mutually exclusive.</li><li>has(self.localSourceRef) || has(self.remoteSourceSpec): One of LocalSource or RemoteSource must be specified.</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresources-1">resources</a></b></td>
        <td>object</td>
        <td>
          Resources contains the resource configuration for the template.<br/>
          <br/>
            <i>Validations</i>:<li>has(self.localSourceRef) ? !has(self.remoteSourceSpec): true: LocalSource and RemoteSource are mutually exclusive.</li><li>has(self.remoteSourceSpec) ? !has(self.localSourceRef): true: LocalSource and RemoteSource are mutually exclusive.</li><li>has(self.localSourceRef) || has(self.remoteSourceSpec): One of LocalSource or RemoteSource must be specified.</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>version</b></td>
        <td>string</td>
        <td>
          Version is the semantic version of the application backed by template.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm
<sup><sup>[↩ Parent](#servicetemplatespec-1)</sup></sup>



Helm contains the Helm chart information for the template.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#servicetemplatespechelmchartref-1">chartRef</a></b></td>
        <td>object</td>
        <td>
          ChartRef is a reference to a source controller resource containing the
Helm chart representing the template.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsource-1">chartSource</a></b></td>
        <td>object</td>
        <td>
          ChartSource is a source of a Helm chart representing the template.<br/>
          <br/>
            <i>Validations</i>:<li>has(self.localSourceRef) ? (self.localSourceRef.kind != 'Secret' && self.localSourceRef.kind != 'ConfigMap'): true: Secret and ConfigMap are not supported as Helm chart sources</li><li>has(self.localSourceRef) ? !has(self.remoteSourceSpec): true: LocalSource and RemoteSource are mutually exclusive.</li><li>has(self.remoteSourceSpec) ? !has(self.localSourceRef): true: LocalSource and RemoteSource are mutually exclusive.</li><li>has(self.localSourceRef) || has(self.remoteSourceSpec): One of LocalSource or RemoteSource must be specified.</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartspec-1">chartSpec</a></b></td>
        <td>object</td>
        <td>
          ChartSpec defines the desired state of the HelmChart to be created by the controller<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartRef
<sup><sup>[↩ Parent](#servicetemplatespechelm-1)</sup></sup>



ChartRef is a reference to a source controller resource containing the
Helm chart representing the template.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>kind</b></td>
        <td>enum</td>
        <td>
          Kind of the referent.<br/>
          <br/>
            <i>Enum</i>: OCIRepository, HelmChart<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>apiVersion</b></td>
        <td>string</td>
        <td>
          APIVersion of the referent.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace of the referent, defaults to the namespace of the Kubernetes
resource object that contains the reference.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource
<sup><sup>[↩ Parent](#servicetemplatespechelm-1)</sup></sup>



ChartSource is a source of a Helm chart representing the template.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>deploymentType</b></td>
        <td>enum</td>
        <td>
          DeploymentType is the type of the deployment. This field is ignored,
when ResourceSpec is used as part of Helm chart configuration.<br/>
          <br/>
            <i>Enum</i>: Local, Remote<br/>
            <i>Default</i>: Remote<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>path</b></td>
        <td>string</td>
        <td>
          Path to the directory containing the resource manifest.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourcelocalsourceref-1">localSourceRef</a></b></td>
        <td>object</td>
        <td>
          LocalSourceRef is the local source of the kustomize manifest.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespec-1">remoteSourceSpec</a></b></td>
        <td>object</td>
        <td>
          RemoteSourceSpec is the remote source of the kustomize manifest.<br/>
          <br/>
            <i>Validations</i>:<li>has(self.git) ? (!has(self.bucket) && !has(self.oci)) : true: Git, Bucket and OCI are mutually exclusive.</li><li>has(self.bucket) ? (!has(self.git) && !has(self.oci)) : true: Git, Bucket and OCI are mutually exclusive.</li><li>has(self.oci) ? (!has(self.git) && !has(self.bucket)) : true: Git, Bucket and OCI are mutually exclusive.</li><li>has(self.git) || has(self.bucket) || has(self.oci): One of Git, Bucket or OCI must be specified.</li>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.localSourceRef
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsource-1)</sup></sup>



LocalSourceRef is the local source of the kustomize manifest.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>kind</b></td>
        <td>enum</td>
        <td>
          Kind is the kind of the local source.<br/>
          <br/>
            <i>Enum</i>: ConfigMap, Secret, GitRepository, Bucket, OCIRepository<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name is the name of the local source.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace is the namespace of the local source. Cross-namespace references
are only allowed when the Kind is one of [github.com/fluxcd/source-controller/api/v1.GitRepository],
[github.com/fluxcd/source-controller/api/v1.Bucket] or [github.com/fluxcd/source-controller/api/v1beta2.OCIRepository].
If the Kind is ConfigMap or Secret, the namespace will be ignored.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsource-1)</sup></sup>



RemoteSourceSpec is the remote source of the kustomize manifest.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecbucket-1">bucket</a></b></td>
        <td>object</td>
        <td>
          Bucket is the definition of bucket source.<br/>
          <br/>
            <i>Validations</i>:<li>self.provider == 'aws' || self.provider == 'generic' || !has(self.sts): STS configuration is only supported for the 'aws' and 'generic' Bucket providers</li><li>self.provider != 'aws' || !has(self.sts) || self.sts.provider == 'aws': 'aws' is the only supported STS provider for the 'aws' Bucket provider</li><li>self.provider != 'generic' || !has(self.sts) || self.sts.provider == 'ldap': 'ldap' is the only supported STS provider for the 'generic' Bucket provider</li><li>!has(self.sts) || self.sts.provider != 'aws' || !has(self.sts.secretRef): spec.sts.secretRef is not required for the 'aws' STS provider</li><li>!has(self.sts) || self.sts.provider != 'aws' || !has(self.sts.certSecretRef): spec.sts.certSecretRef is not required for the 'aws' STS provider</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecgit-1">git</a></b></td>
        <td>object</td>
        <td>
          Git is the definition of git repository source.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecoci-1">oci</a></b></td>
        <td>object</td>
        <td>
          OCI is the definition of OCI repository source.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.bucket
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespec-1)</sup></sup>



Bucket is the definition of bucket source.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>bucketName</b></td>
        <td>string</td>
        <td>
          BucketName is the name of the object storage bucket.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>endpoint</b></td>
        <td>string</td>
        <td>
          Endpoint is the object storage address the BucketName is located at.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>interval</b></td>
        <td>string</td>
        <td>
          Interval at which the Bucket Endpoint is checked for updates.
This interval is approximate and may be subject to jitter to ensure
efficient use of resources.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecbucketcertsecretref-1">certSecretRef</a></b></td>
        <td>object</td>
        <td>
          CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
bucket. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

This field is only supported for the `generic` provider.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>ignore</b></td>
        <td>string</td>
        <td>
          Ignore overrides the set of excluded patterns in the .sourceignore format
(which is the same as .gitignore). If not provided, a default will be used,
consult the documentation for your version to find out what those are.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>insecure</b></td>
        <td>boolean</td>
        <td>
          Insecure allows connecting to a non-TLS HTTP Endpoint.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>prefix</b></td>
        <td>string</td>
        <td>
          Prefix to use for server-side filtering of files in the Bucket.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider of the object storage bucket.
Defaults to 'generic', which expects an S3 (API) compatible object
storage.<br/>
          <br/>
            <i>Enum</i>: generic, aws, gcp, azure<br/>
            <i>Default</i>: generic<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecbucketproxysecretref-1">proxySecretRef</a></b></td>
        <td>object</td>
        <td>
          ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the Bucket server.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>region</b></td>
        <td>string</td>
        <td>
          Region of the Endpoint where the BucketName is located in.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecbucketsecretref-1">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing authentication credentials
for the Bucket.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecbucketsts-1">sts</a></b></td>
        <td>object</td>
        <td>
          STS specifies the required configuration to use a Security Token
Service for fetching temporary credentials to authenticate in a
Bucket provider.

This field is only supported for the `aws` and `generic` providers.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>suspend</b></td>
        <td>boolean</td>
        <td>
          Suspend tells the controller to suspend the reconciliation of this
Bucket.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>timeout</b></td>
        <td>string</td>
        <td>
          Timeout for fetch operations, defaults to 60s.<br/>
          <br/>
            <i>Default</i>: 60s<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.bucket.certSecretRef
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespecbucket-1)</sup></sup>



CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
bucket. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

This field is only supported for the `generic` provider.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.bucket.proxySecretRef
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespecbucket-1)</sup></sup>



ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the Bucket server.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.bucket.secretRef
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespecbucket-1)</sup></sup>



SecretRef specifies the Secret containing authentication credentials
for the Bucket.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.bucket.sts
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespecbucket-1)</sup></sup>



STS specifies the required configuration to use a Security Token
Service for fetching temporary credentials to authenticate in a
Bucket provider.

This field is only supported for the `aws` and `generic` providers.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>endpoint</b></td>
        <td>string</td>
        <td>
          Endpoint is the HTTP/S endpoint of the Security Token Service from
where temporary credentials will be fetched.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider of the Security Token Service.<br/>
          <br/>
            <i>Enum</i>: aws, ldap<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecbucketstscertsecretref-1">certSecretRef</a></b></td>
        <td>object</td>
        <td>
          CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
STS endpoint. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

This field is only supported for the `ldap` provider.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecbucketstssecretref-1">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing authentication credentials
for the STS endpoint. This Secret must contain the fields `username`
and `password` and is supported only for the `ldap` provider.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.bucket.sts.certSecretRef
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespecbucketsts-1)</sup></sup>



CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
STS endpoint. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

This field is only supported for the `ldap` provider.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.bucket.sts.secretRef
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespecbucketsts-1)</sup></sup>



SecretRef specifies the Secret containing authentication credentials
for the STS endpoint. This Secret must contain the fields `username`
and `password` and is supported only for the `ldap` provider.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.git
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespec-1)</sup></sup>



Git is the definition of git repository source.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>interval</b></td>
        <td>string</td>
        <td>
          Interval at which the GitRepository URL is checked for updates.
This interval is approximate and may be subject to jitter to ensure
efficient use of resources.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>url</b></td>
        <td>string</td>
        <td>
          URL specifies the Git repository URL, it can be an HTTP/S or SSH address.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>ignore</b></td>
        <td>string</td>
        <td>
          Ignore overrides the set of excluded patterns in the .sourceignore format
(which is the same as .gitignore). If not provided, a default will be used,
consult the documentation for your version to find out what those are.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecgitincludeindex-1">include</a></b></td>
        <td>[]object</td>
        <td>
          Include specifies a list of GitRepository resources which Artifacts
should be included in the Artifact produced for this GitRepository.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider used for authentication, can be 'azure', 'github', 'generic'.
When not specified, defaults to 'generic'.<br/>
          <br/>
            <i>Enum</i>: generic, azure, github<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecgitproxysecretref-1">proxySecretRef</a></b></td>
        <td>object</td>
        <td>
          ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the Git server.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>recurseSubmodules</b></td>
        <td>boolean</td>
        <td>
          RecurseSubmodules enables the initialization of all submodules within
the GitRepository as cloned from the URL, using their default settings.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecgitref-1">ref</a></b></td>
        <td>object</td>
        <td>
          Reference specifies the Git reference to resolve and monitor for
changes, defaults to the 'master' branch.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecgitsecretref-1">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing authentication credentials for
the GitRepository.
For HTTPS repositories the Secret must contain 'username' and 'password'
fields for basic auth or 'bearerToken' field for token auth.
For SSH repositories the Secret must contain 'identity'
and 'known_hosts' fields.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>suspend</b></td>
        <td>boolean</td>
        <td>
          Suspend tells the controller to suspend the reconciliation of this
GitRepository.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>timeout</b></td>
        <td>string</td>
        <td>
          Timeout for Git operations like cloning, defaults to 60s.<br/>
          <br/>
            <i>Default</i>: 60s<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecgitverify-1">verify</a></b></td>
        <td>object</td>
        <td>
          Verification specifies the configuration to verify the Git commit
signature(s).<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.git.include[index]
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespecgit-1)</sup></sup>



GitRepositoryInclude specifies a local reference to a GitRepository which
Artifact (sub-)contents must be included, and where they should be placed.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecgitincludeindexrepository-1">repository</a></b></td>
        <td>object</td>
        <td>
          GitRepositoryRef specifies the GitRepository which Artifact contents
must be included.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>fromPath</b></td>
        <td>string</td>
        <td>
          FromPath specifies the path to copy contents from, defaults to the root
of the Artifact.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>toPath</b></td>
        <td>string</td>
        <td>
          ToPath specifies the path to copy contents to, defaults to the name of
the GitRepositoryRef.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.git.include[index].repository
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespecgitincludeindex-1)</sup></sup>



GitRepositoryRef specifies the GitRepository which Artifact contents
must be included.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.git.proxySecretRef
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespecgit-1)</sup></sup>



ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the Git server.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.git.ref
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespecgit-1)</sup></sup>



Reference specifies the Git reference to resolve and monitor for
changes, defaults to the 'master' branch.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>branch</b></td>
        <td>string</td>
        <td>
          Branch to check out, defaults to 'master' if no other field is defined.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>commit</b></td>
        <td>string</td>
        <td>
          Commit SHA to check out, takes precedence over all reference fields.

This can be combined with Branch to shallow clone the branch, in which
the commit is expected to exist.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the reference to check out; takes precedence over Branch, Tag and SemVer.

It must be a valid Git reference: https://git-scm.com/docs/git-check-ref-format#_description
Examples: "refs/heads/main", "refs/tags/v0.1.0", "refs/pull/420/head", "refs/merge-requests/1/head"<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>semver</b></td>
        <td>string</td>
        <td>
          SemVer tag expression to check out, takes precedence over Tag.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>tag</b></td>
        <td>string</td>
        <td>
          Tag to check out, takes precedence over Branch.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.git.secretRef
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespecgit-1)</sup></sup>



SecretRef specifies the Secret containing authentication credentials for
the GitRepository.
For HTTPS repositories the Secret must contain 'username' and 'password'
fields for basic auth or 'bearerToken' field for token auth.
For SSH repositories the Secret must contain 'identity'
and 'known_hosts' fields.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.git.verify
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespecgit-1)</sup></sup>



Verification specifies the configuration to verify the Git commit
signature(s).

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecgitverifysecretref-1">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing the public keys of trusted Git
authors.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>mode</b></td>
        <td>enum</td>
        <td>
          Mode specifies which Git object(s) should be verified.

The variants "head" and "HEAD" both imply the same thing, i.e. verify
the commit that the HEAD of the Git repository points to. The variant
"head" solely exists to ensure backwards compatibility.<br/>
          <br/>
            <i>Enum</i>: head, HEAD, Tag, TagAndHEAD<br/>
            <i>Default</i>: HEAD<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.git.verify.secretRef
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespecgitverify-1)</sup></sup>



SecretRef specifies the Secret containing the public keys of trusted Git
authors.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.oci
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespec-1)</sup></sup>



OCI is the definition of OCI repository source.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>interval</b></td>
        <td>string</td>
        <td>
          Interval at which the OCIRepository URL is checked for updates.
This interval is approximate and may be subject to jitter to ensure
efficient use of resources.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>url</b></td>
        <td>string</td>
        <td>
          URL is a reference to an OCI artifact repository hosted
on a remote container registry.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecocicertsecretref-1">certSecretRef</a></b></td>
        <td>object</td>
        <td>
          CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
registry. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

Note: Support for the `caFile`, `certFile` and `keyFile` keys have
been deprecated.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>ignore</b></td>
        <td>string</td>
        <td>
          Ignore overrides the set of excluded patterns in the .sourceignore format
(which is the same as .gitignore). If not provided, a default will be used,
consult the documentation for your version to find out what those are.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>insecure</b></td>
        <td>boolean</td>
        <td>
          Insecure allows connecting to a non-TLS HTTP container registry.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecocilayerselector-1">layerSelector</a></b></td>
        <td>object</td>
        <td>
          LayerSelector specifies which layer should be extracted from the OCI artifact.
When not specified, the first layer found in the artifact is selected.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          The provider used for authentication, can be 'aws', 'azure', 'gcp' or 'generic'.
When not specified, defaults to 'generic'.<br/>
          <br/>
            <i>Enum</i>: generic, aws, azure, gcp<br/>
            <i>Default</i>: generic<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecociproxysecretref-1">proxySecretRef</a></b></td>
        <td>object</td>
        <td>
          ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the container registry.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecociref-1">ref</a></b></td>
        <td>object</td>
        <td>
          The OCI reference to pull and monitor for changes,
defaults to the latest tag.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecocisecretref-1">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef contains the secret name containing the registry login
credentials to resolve image metadata.
The secret must be of type kubernetes.io/dockerconfigjson.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>serviceAccountName</b></td>
        <td>string</td>
        <td>
          ServiceAccountName is the name of the Kubernetes ServiceAccount used to authenticate
the image pull if the service account has attached pull secrets. For more information:
https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#add-imagepullsecrets-to-a-service-account<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>suspend</b></td>
        <td>boolean</td>
        <td>
          This flag tells the controller to suspend the reconciliation of this source.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>timeout</b></td>
        <td>string</td>
        <td>
          The timeout for remote OCI Repository operations like pulling, defaults to 60s.<br/>
          <br/>
            <i>Default</i>: 60s<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecociverify-1">verify</a></b></td>
        <td>object</td>
        <td>
          Verify contains the secret name containing the trusted public keys
used to verify the signature and specifies which provider to use to check
whether OCI image is authentic.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.oci.certSecretRef
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespecoci-1)</sup></sup>



CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
registry. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

Note: Support for the `caFile`, `certFile` and `keyFile` keys have
been deprecated.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.oci.layerSelector
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespecoci-1)</sup></sup>



LayerSelector specifies which layer should be extracted from the OCI artifact.
When not specified, the first layer found in the artifact is selected.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>mediaType</b></td>
        <td>string</td>
        <td>
          MediaType specifies the OCI media type of the layer
which should be extracted from the OCI Artifact. The
first layer matching this type is selected.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>operation</b></td>
        <td>enum</td>
        <td>
          Operation specifies how the selected layer should be processed.
By default, the layer compressed content is extracted to storage.
When the operation is set to 'copy', the layer compressed content
is persisted to storage as it is.<br/>
          <br/>
            <i>Enum</i>: extract, copy<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.oci.proxySecretRef
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespecoci-1)</sup></sup>



ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the container registry.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.oci.ref
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespecoci-1)</sup></sup>



The OCI reference to pull and monitor for changes,
defaults to the latest tag.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>digest</b></td>
        <td>string</td>
        <td>
          Digest is the image digest to pull, takes precedence over SemVer.
The value should be in the format 'sha256:<HASH>'.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>semver</b></td>
        <td>string</td>
        <td>
          SemVer is the range of tags to pull selecting the latest within
the range, takes precedence over Tag.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>semverFilter</b></td>
        <td>string</td>
        <td>
          SemverFilter is a regex pattern to filter the tags within the SemVer range.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>tag</b></td>
        <td>string</td>
        <td>
          Tag is the image tag to pull, defaults to latest.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.oci.secretRef
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespecoci-1)</sup></sup>



SecretRef contains the secret name containing the registry login
credentials to resolve image metadata.
The secret must be of type kubernetes.io/dockerconfigjson.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.oci.verify
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespecoci-1)</sup></sup>



Verify contains the secret name containing the trusted public keys
used to verify the signature and specifies which provider to use to check
whether OCI image is authentic.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider specifies the technology used to sign the OCI Artifact.<br/>
          <br/>
            <i>Enum</i>: cosign, notation<br/>
            <i>Default</i>: cosign<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecociverifymatchoidcidentityindex-1">matchOIDCIdentity</a></b></td>
        <td>[]object</td>
        <td>
          MatchOIDCIdentity specifies the identity matching criteria to use
while verifying an OCI artifact which was signed using Cosign keyless
signing. The artifact's identity is deemed to be verified if any of the
specified matchers match against the identity.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartsourceremotesourcespecociverifysecretref-1">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Kubernetes Secret containing the
trusted public keys.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.oci.verify.matchOIDCIdentity[index]
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespecociverify-1)</sup></sup>



OIDCIdentityMatch specifies options for verifying the certificate identity,
i.e. the issuer and the subject of the certificate.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>issuer</b></td>
        <td>string</td>
        <td>
          Issuer specifies the regex pattern to match against to verify
the OIDC issuer in the Fulcio certificate. The pattern must be a
valid Go regular expression.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>subject</b></td>
        <td>string</td>
        <td>
          Subject specifies the regex pattern to match against to verify
the identity subject in the Fulcio certificate. The pattern must
be a valid Go regular expression.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.oci.verify.secretRef
<sup><sup>[↩ Parent](#servicetemplatespechelmchartsourceremotesourcespecociverify-1)</sup></sup>



SecretRef specifies the Kubernetes Secret containing the
trusted public keys.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSpec
<sup><sup>[↩ Parent](#servicetemplatespechelm-1)</sup></sup>



ChartSpec defines the desired state of the HelmChart to be created by the controller

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>chart</b></td>
        <td>string</td>
        <td>
          Chart is the name or path the Helm chart is available at in the
SourceRef.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>interval</b></td>
        <td>string</td>
        <td>
          Interval at which the HelmChart SourceRef is checked for updates.
This interval is approximate and may be subject to jitter to ensure
efficient use of resources.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartspecsourceref-1">sourceRef</a></b></td>
        <td>object</td>
        <td>
          SourceRef is the reference to the Source the chart is available at.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>ignoreMissingValuesFiles</b></td>
        <td>boolean</td>
        <td>
          IgnoreMissingValuesFiles controls whether to silently ignore missing values
files rather than failing.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>reconcileStrategy</b></td>
        <td>enum</td>
        <td>
          ReconcileStrategy determines what enables the creation of a new artifact.
Valid values are ('ChartVersion', 'Revision').
See the documentation of the values for an explanation on their behavior.
Defaults to ChartVersion when omitted.<br/>
          <br/>
            <i>Enum</i>: ChartVersion, Revision<br/>
            <i>Default</i>: ChartVersion<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>suspend</b></td>
        <td>boolean</td>
        <td>
          Suspend tells the controller to suspend the reconciliation of this
source.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>valuesFiles</b></td>
        <td>[]string</td>
        <td>
          ValuesFiles is an alternative list of values files to use as the chart
values (values.yaml is not included by default), expected to be a
relative path in the SourceRef.
Values files are merged in the order of this list with the last file
overriding the first. Ignored when omitted.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartspecverify-1">verify</a></b></td>
        <td>object</td>
        <td>
          Verify contains the secret name containing the trusted public keys
used to verify the signature and specifies which provider to use to check
whether OCI image is authentic.
This field is only supported when using HelmRepository source with spec.type 'oci'.
Chart dependencies, which are not bundled in the umbrella chart artifact, are not verified.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>version</b></td>
        <td>string</td>
        <td>
          Version is the chart version semver expression, ignored for charts from
GitRepository and Bucket sources. Defaults to latest when omitted.<br/>
          <br/>
            <i>Default</i>: *<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSpec.sourceRef
<sup><sup>[↩ Parent](#servicetemplatespechelmchartspec-1)</sup></sup>



SourceRef is the reference to the Source the chart is available at.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>kind</b></td>
        <td>enum</td>
        <td>
          Kind of the referent, valid values are ('HelmRepository', 'GitRepository',
'Bucket').<br/>
          <br/>
            <i>Enum</i>: HelmRepository, GitRepository, Bucket<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>apiVersion</b></td>
        <td>string</td>
        <td>
          APIVersion of the referent.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSpec.verify
<sup><sup>[↩ Parent](#servicetemplatespechelmchartspec-1)</sup></sup>



Verify contains the secret name containing the trusted public keys
used to verify the signature and specifies which provider to use to check
whether OCI image is authentic.
This field is only supported when using HelmRepository source with spec.type 'oci'.
Chart dependencies, which are not bundled in the umbrella chart artifact, are not verified.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider specifies the technology used to sign the OCI Artifact.<br/>
          <br/>
            <i>Enum</i>: cosign, notation<br/>
            <i>Default</i>: cosign<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartspecverifymatchoidcidentityindex-1">matchOIDCIdentity</a></b></td>
        <td>[]object</td>
        <td>
          MatchOIDCIdentity specifies the identity matching criteria to use
while verifying an OCI artifact which was signed using Cosign keyless
signing. The artifact's identity is deemed to be verified if any of the
specified matchers match against the identity.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespechelmchartspecverifysecretref-1">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Kubernetes Secret containing the
trusted public keys.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSpec.verify.matchOIDCIdentity[index]
<sup><sup>[↩ Parent](#servicetemplatespechelmchartspecverify-1)</sup></sup>



OIDCIdentityMatch specifies options for verifying the certificate identity,
i.e. the issuer and the subject of the certificate.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>issuer</b></td>
        <td>string</td>
        <td>
          Issuer specifies the regex pattern to match against to verify
the OIDC issuer in the Fulcio certificate. The pattern must be a
valid Go regular expression.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>subject</b></td>
        <td>string</td>
        <td>
          Subject specifies the regex pattern to match against to verify
the identity subject in the Fulcio certificate. The pattern must
be a valid Go regular expression.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSpec.verify.secretRef
<sup><sup>[↩ Parent](#servicetemplatespechelmchartspecverify-1)</sup></sup>



SecretRef specifies the Kubernetes Secret containing the
trusted public keys.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize
<sup><sup>[↩ Parent](#servicetemplatespec-1)</sup></sup>



Kustomize contains the Kustomize configuration for the template.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>deploymentType</b></td>
        <td>enum</td>
        <td>
          DeploymentType is the type of the deployment. This field is ignored,
when ResourceSpec is used as part of Helm chart configuration.<br/>
          <br/>
            <i>Enum</i>: Local, Remote<br/>
            <i>Default</i>: Remote<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>path</b></td>
        <td>string</td>
        <td>
          Path to the directory containing the resource manifest.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizelocalsourceref-1">localSourceRef</a></b></td>
        <td>object</td>
        <td>
          LocalSourceRef is the local source of the kustomize manifest.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespec-1">remoteSourceSpec</a></b></td>
        <td>object</td>
        <td>
          RemoteSourceSpec is the remote source of the kustomize manifest.<br/>
          <br/>
            <i>Validations</i>:<li>has(self.git) ? (!has(self.bucket) && !has(self.oci)) : true: Git, Bucket and OCI are mutually exclusive.</li><li>has(self.bucket) ? (!has(self.git) && !has(self.oci)) : true: Git, Bucket and OCI are mutually exclusive.</li><li>has(self.oci) ? (!has(self.git) && !has(self.bucket)) : true: Git, Bucket and OCI are mutually exclusive.</li><li>has(self.git) || has(self.bucket) || has(self.oci): One of Git, Bucket or OCI must be specified.</li>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.localSourceRef
<sup><sup>[↩ Parent](#servicetemplatespeckustomize-1)</sup></sup>



LocalSourceRef is the local source of the kustomize manifest.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>kind</b></td>
        <td>enum</td>
        <td>
          Kind is the kind of the local source.<br/>
          <br/>
            <i>Enum</i>: ConfigMap, Secret, GitRepository, Bucket, OCIRepository<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name is the name of the local source.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace is the namespace of the local source. Cross-namespace references
are only allowed when the Kind is one of [github.com/fluxcd/source-controller/api/v1.GitRepository],
[github.com/fluxcd/source-controller/api/v1.Bucket] or [github.com/fluxcd/source-controller/api/v1beta2.OCIRepository].
If the Kind is ConfigMap or Secret, the namespace will be ignored.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec
<sup><sup>[↩ Parent](#servicetemplatespeckustomize-1)</sup></sup>



RemoteSourceSpec is the remote source of the kustomize manifest.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecbucket-1">bucket</a></b></td>
        <td>object</td>
        <td>
          Bucket is the definition of bucket source.<br/>
          <br/>
            <i>Validations</i>:<li>self.provider == 'aws' || self.provider == 'generic' || !has(self.sts): STS configuration is only supported for the 'aws' and 'generic' Bucket providers</li><li>self.provider != 'aws' || !has(self.sts) || self.sts.provider == 'aws': 'aws' is the only supported STS provider for the 'aws' Bucket provider</li><li>self.provider != 'generic' || !has(self.sts) || self.sts.provider == 'ldap': 'ldap' is the only supported STS provider for the 'generic' Bucket provider</li><li>!has(self.sts) || self.sts.provider != 'aws' || !has(self.sts.secretRef): spec.sts.secretRef is not required for the 'aws' STS provider</li><li>!has(self.sts) || self.sts.provider != 'aws' || !has(self.sts.certSecretRef): spec.sts.certSecretRef is not required for the 'aws' STS provider</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecgit-1">git</a></b></td>
        <td>object</td>
        <td>
          Git is the definition of git repository source.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecoci-1">oci</a></b></td>
        <td>object</td>
        <td>
          OCI is the definition of OCI repository source.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.bucket
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespec-1)</sup></sup>



Bucket is the definition of bucket source.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>bucketName</b></td>
        <td>string</td>
        <td>
          BucketName is the name of the object storage bucket.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>endpoint</b></td>
        <td>string</td>
        <td>
          Endpoint is the object storage address the BucketName is located at.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>interval</b></td>
        <td>string</td>
        <td>
          Interval at which the Bucket Endpoint is checked for updates.
This interval is approximate and may be subject to jitter to ensure
efficient use of resources.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecbucketcertsecretref-1">certSecretRef</a></b></td>
        <td>object</td>
        <td>
          CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
bucket. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

This field is only supported for the `generic` provider.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>ignore</b></td>
        <td>string</td>
        <td>
          Ignore overrides the set of excluded patterns in the .sourceignore format
(which is the same as .gitignore). If not provided, a default will be used,
consult the documentation for your version to find out what those are.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>insecure</b></td>
        <td>boolean</td>
        <td>
          Insecure allows connecting to a non-TLS HTTP Endpoint.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>prefix</b></td>
        <td>string</td>
        <td>
          Prefix to use for server-side filtering of files in the Bucket.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider of the object storage bucket.
Defaults to 'generic', which expects an S3 (API) compatible object
storage.<br/>
          <br/>
            <i>Enum</i>: generic, aws, gcp, azure<br/>
            <i>Default</i>: generic<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecbucketproxysecretref-1">proxySecretRef</a></b></td>
        <td>object</td>
        <td>
          ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the Bucket server.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>region</b></td>
        <td>string</td>
        <td>
          Region of the Endpoint where the BucketName is located in.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecbucketsecretref-1">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing authentication credentials
for the Bucket.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecbucketsts-1">sts</a></b></td>
        <td>object</td>
        <td>
          STS specifies the required configuration to use a Security Token
Service for fetching temporary credentials to authenticate in a
Bucket provider.

This field is only supported for the `aws` and `generic` providers.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>suspend</b></td>
        <td>boolean</td>
        <td>
          Suspend tells the controller to suspend the reconciliation of this
Bucket.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>timeout</b></td>
        <td>string</td>
        <td>
          Timeout for fetch operations, defaults to 60s.<br/>
          <br/>
            <i>Default</i>: 60s<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.bucket.certSecretRef
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespecbucket-1)</sup></sup>



CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
bucket. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

This field is only supported for the `generic` provider.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.bucket.proxySecretRef
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespecbucket-1)</sup></sup>



ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the Bucket server.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.bucket.secretRef
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespecbucket-1)</sup></sup>



SecretRef specifies the Secret containing authentication credentials
for the Bucket.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.bucket.sts
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespecbucket-1)</sup></sup>



STS specifies the required configuration to use a Security Token
Service for fetching temporary credentials to authenticate in a
Bucket provider.

This field is only supported for the `aws` and `generic` providers.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>endpoint</b></td>
        <td>string</td>
        <td>
          Endpoint is the HTTP/S endpoint of the Security Token Service from
where temporary credentials will be fetched.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider of the Security Token Service.<br/>
          <br/>
            <i>Enum</i>: aws, ldap<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecbucketstscertsecretref-1">certSecretRef</a></b></td>
        <td>object</td>
        <td>
          CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
STS endpoint. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

This field is only supported for the `ldap` provider.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecbucketstssecretref-1">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing authentication credentials
for the STS endpoint. This Secret must contain the fields `username`
and `password` and is supported only for the `ldap` provider.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.bucket.sts.certSecretRef
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespecbucketsts-1)</sup></sup>



CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
STS endpoint. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

This field is only supported for the `ldap` provider.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.bucket.sts.secretRef
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespecbucketsts-1)</sup></sup>



SecretRef specifies the Secret containing authentication credentials
for the STS endpoint. This Secret must contain the fields `username`
and `password` and is supported only for the `ldap` provider.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.git
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespec-1)</sup></sup>



Git is the definition of git repository source.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>interval</b></td>
        <td>string</td>
        <td>
          Interval at which the GitRepository URL is checked for updates.
This interval is approximate and may be subject to jitter to ensure
efficient use of resources.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>url</b></td>
        <td>string</td>
        <td>
          URL specifies the Git repository URL, it can be an HTTP/S or SSH address.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>ignore</b></td>
        <td>string</td>
        <td>
          Ignore overrides the set of excluded patterns in the .sourceignore format
(which is the same as .gitignore). If not provided, a default will be used,
consult the documentation for your version to find out what those are.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecgitincludeindex-1">include</a></b></td>
        <td>[]object</td>
        <td>
          Include specifies a list of GitRepository resources which Artifacts
should be included in the Artifact produced for this GitRepository.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider used for authentication, can be 'azure', 'github', 'generic'.
When not specified, defaults to 'generic'.<br/>
          <br/>
            <i>Enum</i>: generic, azure, github<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecgitproxysecretref-1">proxySecretRef</a></b></td>
        <td>object</td>
        <td>
          ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the Git server.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>recurseSubmodules</b></td>
        <td>boolean</td>
        <td>
          RecurseSubmodules enables the initialization of all submodules within
the GitRepository as cloned from the URL, using their default settings.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecgitref-1">ref</a></b></td>
        <td>object</td>
        <td>
          Reference specifies the Git reference to resolve and monitor for
changes, defaults to the 'master' branch.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecgitsecretref-1">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing authentication credentials for
the GitRepository.
For HTTPS repositories the Secret must contain 'username' and 'password'
fields for basic auth or 'bearerToken' field for token auth.
For SSH repositories the Secret must contain 'identity'
and 'known_hosts' fields.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>suspend</b></td>
        <td>boolean</td>
        <td>
          Suspend tells the controller to suspend the reconciliation of this
GitRepository.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>timeout</b></td>
        <td>string</td>
        <td>
          Timeout for Git operations like cloning, defaults to 60s.<br/>
          <br/>
            <i>Default</i>: 60s<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecgitverify-1">verify</a></b></td>
        <td>object</td>
        <td>
          Verification specifies the configuration to verify the Git commit
signature(s).<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.git.include[index]
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespecgit-1)</sup></sup>



GitRepositoryInclude specifies a local reference to a GitRepository which
Artifact (sub-)contents must be included, and where they should be placed.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecgitincludeindexrepository-1">repository</a></b></td>
        <td>object</td>
        <td>
          GitRepositoryRef specifies the GitRepository which Artifact contents
must be included.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>fromPath</b></td>
        <td>string</td>
        <td>
          FromPath specifies the path to copy contents from, defaults to the root
of the Artifact.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>toPath</b></td>
        <td>string</td>
        <td>
          ToPath specifies the path to copy contents to, defaults to the name of
the GitRepositoryRef.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.git.include[index].repository
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespecgitincludeindex-1)</sup></sup>



GitRepositoryRef specifies the GitRepository which Artifact contents
must be included.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.git.proxySecretRef
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespecgit-1)</sup></sup>



ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the Git server.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.git.ref
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespecgit-1)</sup></sup>



Reference specifies the Git reference to resolve and monitor for
changes, defaults to the 'master' branch.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>branch</b></td>
        <td>string</td>
        <td>
          Branch to check out, defaults to 'master' if no other field is defined.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>commit</b></td>
        <td>string</td>
        <td>
          Commit SHA to check out, takes precedence over all reference fields.

This can be combined with Branch to shallow clone the branch, in which
the commit is expected to exist.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the reference to check out; takes precedence over Branch, Tag and SemVer.

It must be a valid Git reference: https://git-scm.com/docs/git-check-ref-format#_description
Examples: "refs/heads/main", "refs/tags/v0.1.0", "refs/pull/420/head", "refs/merge-requests/1/head"<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>semver</b></td>
        <td>string</td>
        <td>
          SemVer tag expression to check out, takes precedence over Tag.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>tag</b></td>
        <td>string</td>
        <td>
          Tag to check out, takes precedence over Branch.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.git.secretRef
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespecgit-1)</sup></sup>



SecretRef specifies the Secret containing authentication credentials for
the GitRepository.
For HTTPS repositories the Secret must contain 'username' and 'password'
fields for basic auth or 'bearerToken' field for token auth.
For SSH repositories the Secret must contain 'identity'
and 'known_hosts' fields.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.git.verify
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespecgit-1)</sup></sup>



Verification specifies the configuration to verify the Git commit
signature(s).

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecgitverifysecretref-1">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing the public keys of trusted Git
authors.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>mode</b></td>
        <td>enum</td>
        <td>
          Mode specifies which Git object(s) should be verified.

The variants "head" and "HEAD" both imply the same thing, i.e. verify
the commit that the HEAD of the Git repository points to. The variant
"head" solely exists to ensure backwards compatibility.<br/>
          <br/>
            <i>Enum</i>: head, HEAD, Tag, TagAndHEAD<br/>
            <i>Default</i>: HEAD<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.git.verify.secretRef
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespecgitverify-1)</sup></sup>



SecretRef specifies the Secret containing the public keys of trusted Git
authors.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.oci
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespec-1)</sup></sup>



OCI is the definition of OCI repository source.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>interval</b></td>
        <td>string</td>
        <td>
          Interval at which the OCIRepository URL is checked for updates.
This interval is approximate and may be subject to jitter to ensure
efficient use of resources.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>url</b></td>
        <td>string</td>
        <td>
          URL is a reference to an OCI artifact repository hosted
on a remote container registry.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecocicertsecretref-1">certSecretRef</a></b></td>
        <td>object</td>
        <td>
          CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
registry. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

Note: Support for the `caFile`, `certFile` and `keyFile` keys have
been deprecated.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>ignore</b></td>
        <td>string</td>
        <td>
          Ignore overrides the set of excluded patterns in the .sourceignore format
(which is the same as .gitignore). If not provided, a default will be used,
consult the documentation for your version to find out what those are.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>insecure</b></td>
        <td>boolean</td>
        <td>
          Insecure allows connecting to a non-TLS HTTP container registry.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecocilayerselector-1">layerSelector</a></b></td>
        <td>object</td>
        <td>
          LayerSelector specifies which layer should be extracted from the OCI artifact.
When not specified, the first layer found in the artifact is selected.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          The provider used for authentication, can be 'aws', 'azure', 'gcp' or 'generic'.
When not specified, defaults to 'generic'.<br/>
          <br/>
            <i>Enum</i>: generic, aws, azure, gcp<br/>
            <i>Default</i>: generic<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecociproxysecretref-1">proxySecretRef</a></b></td>
        <td>object</td>
        <td>
          ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the container registry.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecociref-1">ref</a></b></td>
        <td>object</td>
        <td>
          The OCI reference to pull and monitor for changes,
defaults to the latest tag.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecocisecretref-1">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef contains the secret name containing the registry login
credentials to resolve image metadata.
The secret must be of type kubernetes.io/dockerconfigjson.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>serviceAccountName</b></td>
        <td>string</td>
        <td>
          ServiceAccountName is the name of the Kubernetes ServiceAccount used to authenticate
the image pull if the service account has attached pull secrets. For more information:
https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#add-imagepullsecrets-to-a-service-account<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>suspend</b></td>
        <td>boolean</td>
        <td>
          This flag tells the controller to suspend the reconciliation of this source.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>timeout</b></td>
        <td>string</td>
        <td>
          The timeout for remote OCI Repository operations like pulling, defaults to 60s.<br/>
          <br/>
            <i>Default</i>: 60s<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecociverify-1">verify</a></b></td>
        <td>object</td>
        <td>
          Verify contains the secret name containing the trusted public keys
used to verify the signature and specifies which provider to use to check
whether OCI image is authentic.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.oci.certSecretRef
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespecoci-1)</sup></sup>



CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
registry. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

Note: Support for the `caFile`, `certFile` and `keyFile` keys have
been deprecated.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.oci.layerSelector
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespecoci-1)</sup></sup>



LayerSelector specifies which layer should be extracted from the OCI artifact.
When not specified, the first layer found in the artifact is selected.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>mediaType</b></td>
        <td>string</td>
        <td>
          MediaType specifies the OCI media type of the layer
which should be extracted from the OCI Artifact. The
first layer matching this type is selected.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>operation</b></td>
        <td>enum</td>
        <td>
          Operation specifies how the selected layer should be processed.
By default, the layer compressed content is extracted to storage.
When the operation is set to 'copy', the layer compressed content
is persisted to storage as it is.<br/>
          <br/>
            <i>Enum</i>: extract, copy<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.oci.proxySecretRef
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespecoci-1)</sup></sup>



ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the container registry.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.oci.ref
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespecoci-1)</sup></sup>



The OCI reference to pull and monitor for changes,
defaults to the latest tag.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>digest</b></td>
        <td>string</td>
        <td>
          Digest is the image digest to pull, takes precedence over SemVer.
The value should be in the format 'sha256:<HASH>'.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>semver</b></td>
        <td>string</td>
        <td>
          SemVer is the range of tags to pull selecting the latest within
the range, takes precedence over Tag.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>semverFilter</b></td>
        <td>string</td>
        <td>
          SemverFilter is a regex pattern to filter the tags within the SemVer range.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>tag</b></td>
        <td>string</td>
        <td>
          Tag is the image tag to pull, defaults to latest.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.oci.secretRef
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespecoci-1)</sup></sup>



SecretRef contains the secret name containing the registry login
credentials to resolve image metadata.
The secret must be of type kubernetes.io/dockerconfigjson.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.oci.verify
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespecoci-1)</sup></sup>



Verify contains the secret name containing the trusted public keys
used to verify the signature and specifies which provider to use to check
whether OCI image is authentic.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider specifies the technology used to sign the OCI Artifact.<br/>
          <br/>
            <i>Enum</i>: cosign, notation<br/>
            <i>Default</i>: cosign<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecociverifymatchoidcidentityindex-1">matchOIDCIdentity</a></b></td>
        <td>[]object</td>
        <td>
          MatchOIDCIdentity specifies the identity matching criteria to use
while verifying an OCI artifact which was signed using Cosign keyless
signing. The artifact's identity is deemed to be verified if any of the
specified matchers match against the identity.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespeckustomizeremotesourcespecociverifysecretref-1">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Kubernetes Secret containing the
trusted public keys.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.oci.verify.matchOIDCIdentity[index]
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespecociverify-1)</sup></sup>



OIDCIdentityMatch specifies options for verifying the certificate identity,
i.e. the issuer and the subject of the certificate.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>issuer</b></td>
        <td>string</td>
        <td>
          Issuer specifies the regex pattern to match against to verify
the OIDC issuer in the Fulcio certificate. The pattern must be a
valid Go regular expression.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>subject</b></td>
        <td>string</td>
        <td>
          Subject specifies the regex pattern to match against to verify
the identity subject in the Fulcio certificate. The pattern must
be a valid Go regular expression.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.oci.verify.secretRef
<sup><sup>[↩ Parent](#servicetemplatespeckustomizeremotesourcespecociverify-1)</sup></sup>



SecretRef specifies the Kubernetes Secret containing the
trusted public keys.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources
<sup><sup>[↩ Parent](#servicetemplatespec-1)</sup></sup>



Resources contains the resource configuration for the template.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>deploymentType</b></td>
        <td>enum</td>
        <td>
          DeploymentType is the type of the deployment. This field is ignored,
when ResourceSpec is used as part of Helm chart configuration.<br/>
          <br/>
            <i>Enum</i>: Local, Remote<br/>
            <i>Default</i>: Remote<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>path</b></td>
        <td>string</td>
        <td>
          Path to the directory containing the resource manifest.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourceslocalsourceref-1">localSourceRef</a></b></td>
        <td>object</td>
        <td>
          LocalSourceRef is the local source of the kustomize manifest.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespec-1">remoteSourceSpec</a></b></td>
        <td>object</td>
        <td>
          RemoteSourceSpec is the remote source of the kustomize manifest.<br/>
          <br/>
            <i>Validations</i>:<li>has(self.git) ? (!has(self.bucket) && !has(self.oci)) : true: Git, Bucket and OCI are mutually exclusive.</li><li>has(self.bucket) ? (!has(self.git) && !has(self.oci)) : true: Git, Bucket and OCI are mutually exclusive.</li><li>has(self.oci) ? (!has(self.git) && !has(self.bucket)) : true: Git, Bucket and OCI are mutually exclusive.</li><li>has(self.git) || has(self.bucket) || has(self.oci): One of Git, Bucket or OCI must be specified.</li>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.localSourceRef
<sup><sup>[↩ Parent](#servicetemplatespecresources-1)</sup></sup>



LocalSourceRef is the local source of the kustomize manifest.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>kind</b></td>
        <td>enum</td>
        <td>
          Kind is the kind of the local source.<br/>
          <br/>
            <i>Enum</i>: ConfigMap, Secret, GitRepository, Bucket, OCIRepository<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name is the name of the local source.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace is the namespace of the local source. Cross-namespace references
are only allowed when the Kind is one of [github.com/fluxcd/source-controller/api/v1.GitRepository],
[github.com/fluxcd/source-controller/api/v1.Bucket] or [github.com/fluxcd/source-controller/api/v1beta2.OCIRepository].
If the Kind is ConfigMap or Secret, the namespace will be ignored.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec
<sup><sup>[↩ Parent](#servicetemplatespecresources-1)</sup></sup>



RemoteSourceSpec is the remote source of the kustomize manifest.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecbucket-1">bucket</a></b></td>
        <td>object</td>
        <td>
          Bucket is the definition of bucket source.<br/>
          <br/>
            <i>Validations</i>:<li>self.provider == 'aws' || self.provider == 'generic' || !has(self.sts): STS configuration is only supported for the 'aws' and 'generic' Bucket providers</li><li>self.provider != 'aws' || !has(self.sts) || self.sts.provider == 'aws': 'aws' is the only supported STS provider for the 'aws' Bucket provider</li><li>self.provider != 'generic' || !has(self.sts) || self.sts.provider == 'ldap': 'ldap' is the only supported STS provider for the 'generic' Bucket provider</li><li>!has(self.sts) || self.sts.provider != 'aws' || !has(self.sts.secretRef): spec.sts.secretRef is not required for the 'aws' STS provider</li><li>!has(self.sts) || self.sts.provider != 'aws' || !has(self.sts.certSecretRef): spec.sts.certSecretRef is not required for the 'aws' STS provider</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecgit-1">git</a></b></td>
        <td>object</td>
        <td>
          Git is the definition of git repository source.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecoci-1">oci</a></b></td>
        <td>object</td>
        <td>
          OCI is the definition of OCI repository source.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.bucket
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespec-1)</sup></sup>



Bucket is the definition of bucket source.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>bucketName</b></td>
        <td>string</td>
        <td>
          BucketName is the name of the object storage bucket.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>endpoint</b></td>
        <td>string</td>
        <td>
          Endpoint is the object storage address the BucketName is located at.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>interval</b></td>
        <td>string</td>
        <td>
          Interval at which the Bucket Endpoint is checked for updates.
This interval is approximate and may be subject to jitter to ensure
efficient use of resources.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecbucketcertsecretref-1">certSecretRef</a></b></td>
        <td>object</td>
        <td>
          CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
bucket. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

This field is only supported for the `generic` provider.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>ignore</b></td>
        <td>string</td>
        <td>
          Ignore overrides the set of excluded patterns in the .sourceignore format
(which is the same as .gitignore). If not provided, a default will be used,
consult the documentation for your version to find out what those are.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>insecure</b></td>
        <td>boolean</td>
        <td>
          Insecure allows connecting to a non-TLS HTTP Endpoint.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>prefix</b></td>
        <td>string</td>
        <td>
          Prefix to use for server-side filtering of files in the Bucket.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider of the object storage bucket.
Defaults to 'generic', which expects an S3 (API) compatible object
storage.<br/>
          <br/>
            <i>Enum</i>: generic, aws, gcp, azure<br/>
            <i>Default</i>: generic<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecbucketproxysecretref-1">proxySecretRef</a></b></td>
        <td>object</td>
        <td>
          ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the Bucket server.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>region</b></td>
        <td>string</td>
        <td>
          Region of the Endpoint where the BucketName is located in.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecbucketsecretref-1">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing authentication credentials
for the Bucket.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecbucketsts-1">sts</a></b></td>
        <td>object</td>
        <td>
          STS specifies the required configuration to use a Security Token
Service for fetching temporary credentials to authenticate in a
Bucket provider.

This field is only supported for the `aws` and `generic` providers.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>suspend</b></td>
        <td>boolean</td>
        <td>
          Suspend tells the controller to suspend the reconciliation of this
Bucket.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>timeout</b></td>
        <td>string</td>
        <td>
          Timeout for fetch operations, defaults to 60s.<br/>
          <br/>
            <i>Default</i>: 60s<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.bucket.certSecretRef
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespecbucket-1)</sup></sup>



CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
bucket. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

This field is only supported for the `generic` provider.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.bucket.proxySecretRef
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespecbucket-1)</sup></sup>



ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the Bucket server.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.bucket.secretRef
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespecbucket-1)</sup></sup>



SecretRef specifies the Secret containing authentication credentials
for the Bucket.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.bucket.sts
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespecbucket-1)</sup></sup>



STS specifies the required configuration to use a Security Token
Service for fetching temporary credentials to authenticate in a
Bucket provider.

This field is only supported for the `aws` and `generic` providers.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>endpoint</b></td>
        <td>string</td>
        <td>
          Endpoint is the HTTP/S endpoint of the Security Token Service from
where temporary credentials will be fetched.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider of the Security Token Service.<br/>
          <br/>
            <i>Enum</i>: aws, ldap<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecbucketstscertsecretref-1">certSecretRef</a></b></td>
        <td>object</td>
        <td>
          CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
STS endpoint. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

This field is only supported for the `ldap` provider.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecbucketstssecretref-1">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing authentication credentials
for the STS endpoint. This Secret must contain the fields `username`
and `password` and is supported only for the `ldap` provider.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.bucket.sts.certSecretRef
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespecbucketsts-1)</sup></sup>



CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
STS endpoint. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

This field is only supported for the `ldap` provider.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.bucket.sts.secretRef
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespecbucketsts-1)</sup></sup>



SecretRef specifies the Secret containing authentication credentials
for the STS endpoint. This Secret must contain the fields `username`
and `password` and is supported only for the `ldap` provider.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.git
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespec-1)</sup></sup>



Git is the definition of git repository source.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>interval</b></td>
        <td>string</td>
        <td>
          Interval at which the GitRepository URL is checked for updates.
This interval is approximate and may be subject to jitter to ensure
efficient use of resources.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>url</b></td>
        <td>string</td>
        <td>
          URL specifies the Git repository URL, it can be an HTTP/S or SSH address.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>ignore</b></td>
        <td>string</td>
        <td>
          Ignore overrides the set of excluded patterns in the .sourceignore format
(which is the same as .gitignore). If not provided, a default will be used,
consult the documentation for your version to find out what those are.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecgitincludeindex-1">include</a></b></td>
        <td>[]object</td>
        <td>
          Include specifies a list of GitRepository resources which Artifacts
should be included in the Artifact produced for this GitRepository.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider used for authentication, can be 'azure', 'github', 'generic'.
When not specified, defaults to 'generic'.<br/>
          <br/>
            <i>Enum</i>: generic, azure, github<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecgitproxysecretref-1">proxySecretRef</a></b></td>
        <td>object</td>
        <td>
          ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the Git server.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>recurseSubmodules</b></td>
        <td>boolean</td>
        <td>
          RecurseSubmodules enables the initialization of all submodules within
the GitRepository as cloned from the URL, using their default settings.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecgitref-1">ref</a></b></td>
        <td>object</td>
        <td>
          Reference specifies the Git reference to resolve and monitor for
changes, defaults to the 'master' branch.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecgitsecretref-1">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing authentication credentials for
the GitRepository.
For HTTPS repositories the Secret must contain 'username' and 'password'
fields for basic auth or 'bearerToken' field for token auth.
For SSH repositories the Secret must contain 'identity'
and 'known_hosts' fields.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>suspend</b></td>
        <td>boolean</td>
        <td>
          Suspend tells the controller to suspend the reconciliation of this
GitRepository.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>timeout</b></td>
        <td>string</td>
        <td>
          Timeout for Git operations like cloning, defaults to 60s.<br/>
          <br/>
            <i>Default</i>: 60s<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecgitverify-1">verify</a></b></td>
        <td>object</td>
        <td>
          Verification specifies the configuration to verify the Git commit
signature(s).<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.git.include[index]
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespecgit-1)</sup></sup>



GitRepositoryInclude specifies a local reference to a GitRepository which
Artifact (sub-)contents must be included, and where they should be placed.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecgitincludeindexrepository-1">repository</a></b></td>
        <td>object</td>
        <td>
          GitRepositoryRef specifies the GitRepository which Artifact contents
must be included.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>fromPath</b></td>
        <td>string</td>
        <td>
          FromPath specifies the path to copy contents from, defaults to the root
of the Artifact.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>toPath</b></td>
        <td>string</td>
        <td>
          ToPath specifies the path to copy contents to, defaults to the name of
the GitRepositoryRef.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.git.include[index].repository
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespecgitincludeindex-1)</sup></sup>



GitRepositoryRef specifies the GitRepository which Artifact contents
must be included.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.git.proxySecretRef
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespecgit-1)</sup></sup>



ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the Git server.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.git.ref
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespecgit-1)</sup></sup>



Reference specifies the Git reference to resolve and monitor for
changes, defaults to the 'master' branch.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>branch</b></td>
        <td>string</td>
        <td>
          Branch to check out, defaults to 'master' if no other field is defined.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>commit</b></td>
        <td>string</td>
        <td>
          Commit SHA to check out, takes precedence over all reference fields.

This can be combined with Branch to shallow clone the branch, in which
the commit is expected to exist.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the reference to check out; takes precedence over Branch, Tag and SemVer.

It must be a valid Git reference: https://git-scm.com/docs/git-check-ref-format#_description
Examples: "refs/heads/main", "refs/tags/v0.1.0", "refs/pull/420/head", "refs/merge-requests/1/head"<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>semver</b></td>
        <td>string</td>
        <td>
          SemVer tag expression to check out, takes precedence over Tag.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>tag</b></td>
        <td>string</td>
        <td>
          Tag to check out, takes precedence over Branch.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.git.secretRef
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespecgit-1)</sup></sup>



SecretRef specifies the Secret containing authentication credentials for
the GitRepository.
For HTTPS repositories the Secret must contain 'username' and 'password'
fields for basic auth or 'bearerToken' field for token auth.
For SSH repositories the Secret must contain 'identity'
and 'known_hosts' fields.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.git.verify
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespecgit-1)</sup></sup>



Verification specifies the configuration to verify the Git commit
signature(s).

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecgitverifysecretref-1">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing the public keys of trusted Git
authors.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>mode</b></td>
        <td>enum</td>
        <td>
          Mode specifies which Git object(s) should be verified.

The variants "head" and "HEAD" both imply the same thing, i.e. verify
the commit that the HEAD of the Git repository points to. The variant
"head" solely exists to ensure backwards compatibility.<br/>
          <br/>
            <i>Enum</i>: head, HEAD, Tag, TagAndHEAD<br/>
            <i>Default</i>: HEAD<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.git.verify.secretRef
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespecgitverify-1)</sup></sup>



SecretRef specifies the Secret containing the public keys of trusted Git
authors.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.oci
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespec-1)</sup></sup>



OCI is the definition of OCI repository source.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>interval</b></td>
        <td>string</td>
        <td>
          Interval at which the OCIRepository URL is checked for updates.
This interval is approximate and may be subject to jitter to ensure
efficient use of resources.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>url</b></td>
        <td>string</td>
        <td>
          URL is a reference to an OCI artifact repository hosted
on a remote container registry.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecocicertsecretref-1">certSecretRef</a></b></td>
        <td>object</td>
        <td>
          CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
registry. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

Note: Support for the `caFile`, `certFile` and `keyFile` keys have
been deprecated.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>ignore</b></td>
        <td>string</td>
        <td>
          Ignore overrides the set of excluded patterns in the .sourceignore format
(which is the same as .gitignore). If not provided, a default will be used,
consult the documentation for your version to find out what those are.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>insecure</b></td>
        <td>boolean</td>
        <td>
          Insecure allows connecting to a non-TLS HTTP container registry.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecocilayerselector-1">layerSelector</a></b></td>
        <td>object</td>
        <td>
          LayerSelector specifies which layer should be extracted from the OCI artifact.
When not specified, the first layer found in the artifact is selected.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          The provider used for authentication, can be 'aws', 'azure', 'gcp' or 'generic'.
When not specified, defaults to 'generic'.<br/>
          <br/>
            <i>Enum</i>: generic, aws, azure, gcp<br/>
            <i>Default</i>: generic<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecociproxysecretref-1">proxySecretRef</a></b></td>
        <td>object</td>
        <td>
          ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the container registry.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecociref-1">ref</a></b></td>
        <td>object</td>
        <td>
          The OCI reference to pull and monitor for changes,
defaults to the latest tag.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecocisecretref-1">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef contains the secret name containing the registry login
credentials to resolve image metadata.
The secret must be of type kubernetes.io/dockerconfigjson.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>serviceAccountName</b></td>
        <td>string</td>
        <td>
          ServiceAccountName is the name of the Kubernetes ServiceAccount used to authenticate
the image pull if the service account has attached pull secrets. For more information:
https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#add-imagepullsecrets-to-a-service-account<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>suspend</b></td>
        <td>boolean</td>
        <td>
          This flag tells the controller to suspend the reconciliation of this source.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>timeout</b></td>
        <td>string</td>
        <td>
          The timeout for remote OCI Repository operations like pulling, defaults to 60s.<br/>
          <br/>
            <i>Default</i>: 60s<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecociverify-1">verify</a></b></td>
        <td>object</td>
        <td>
          Verify contains the secret name containing the trusted public keys
used to verify the signature and specifies which provider to use to check
whether OCI image is authentic.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.oci.certSecretRef
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespecoci-1)</sup></sup>



CertSecretRef can be given the name of a Secret containing
either or both of

- a PEM-encoded client certificate (`tls.crt`) and private
key (`tls.key`);
- a PEM-encoded CA certificate (`ca.crt`)

and whichever are supplied, will be used for connecting to the
registry. The client cert and key are useful if you are
authenticating with a certificate; the CA cert is useful if
you are using a self-signed server certificate. The Secret must
be of type `Opaque` or `kubernetes.io/tls`.

Note: Support for the `caFile`, `certFile` and `keyFile` keys have
been deprecated.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.oci.layerSelector
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespecoci-1)</sup></sup>



LayerSelector specifies which layer should be extracted from the OCI artifact.
When not specified, the first layer found in the artifact is selected.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>mediaType</b></td>
        <td>string</td>
        <td>
          MediaType specifies the OCI media type of the layer
which should be extracted from the OCI Artifact. The
first layer matching this type is selected.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>operation</b></td>
        <td>enum</td>
        <td>
          Operation specifies how the selected layer should be processed.
By default, the layer compressed content is extracted to storage.
When the operation is set to 'copy', the layer compressed content
is persisted to storage as it is.<br/>
          <br/>
            <i>Enum</i>: extract, copy<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.oci.proxySecretRef
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespecoci-1)</sup></sup>



ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the container registry.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.oci.ref
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespecoci-1)</sup></sup>



The OCI reference to pull and monitor for changes,
defaults to the latest tag.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>digest</b></td>
        <td>string</td>
        <td>
          Digest is the image digest to pull, takes precedence over SemVer.
The value should be in the format 'sha256:<HASH>'.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>semver</b></td>
        <td>string</td>
        <td>
          SemVer is the range of tags to pull selecting the latest within
the range, takes precedence over Tag.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>semverFilter</b></td>
        <td>string</td>
        <td>
          SemverFilter is a regex pattern to filter the tags within the SemVer range.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>tag</b></td>
        <td>string</td>
        <td>
          Tag is the image tag to pull, defaults to latest.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.oci.secretRef
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespecoci-1)</sup></sup>



SecretRef contains the secret name containing the registry login
credentials to resolve image metadata.
The secret must be of type kubernetes.io/dockerconfigjson.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.oci.verify
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespecoci-1)</sup></sup>



Verify contains the secret name containing the trusted public keys
used to verify the signature and specifies which provider to use to check
whether OCI image is authentic.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>provider</b></td>
        <td>enum</td>
        <td>
          Provider specifies the technology used to sign the OCI Artifact.<br/>
          <br/>
            <i>Enum</i>: cosign, notation<br/>
            <i>Default</i>: cosign<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecociverifymatchoidcidentityindex-1">matchOIDCIdentity</a></b></td>
        <td>[]object</td>
        <td>
          MatchOIDCIdentity specifies the identity matching criteria to use
while verifying an OCI artifact which was signed using Cosign keyless
signing. The artifact's identity is deemed to be verified if any of the
specified matchers match against the identity.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatespecresourcesremotesourcespecociverifysecretref-1">secretRef</a></b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Kubernetes Secret containing the
trusted public keys.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.oci.verify.matchOIDCIdentity[index]
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespecociverify-1)</sup></sup>



OIDCIdentityMatch specifies options for verifying the certificate identity,
i.e. the issuer and the subject of the certificate.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>issuer</b></td>
        <td>string</td>
        <td>
          Issuer specifies the regex pattern to match against to verify
the OIDC issuer in the Fulcio certificate. The pattern must be a
valid Go regular expression.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>subject</b></td>
        <td>string</td>
        <td>
          Subject specifies the regex pattern to match against to verify
the identity subject in the Fulcio certificate. The pattern must
be a valid Go regular expression.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.oci.verify.secretRef
<sup><sup>[↩ Parent](#servicetemplatespecresourcesremotesourcespecociverify-1)</sup></sup>



SecretRef specifies the Kubernetes Secret containing the
trusted public keys.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplate.status
<sup><sup>[↩ Parent](#servicetemplate-1)</sup></sup>



ServiceTemplateStatus defines the observed state of ServiceTemplate

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>valid</b></td>
        <td>boolean</td>
        <td>
          Valid indicates whether the template passed validation or not.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#servicetemplatestatuschartref-1">chartRef</a></b></td>
        <td>object</td>
        <td>
          ChartRef is a reference to a source controller resource containing the
Helm chart representing the template.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>chartVersion</b></td>
        <td>string</td>
        <td>
          ChartVersion represents the version of the Helm Chart associated with this template.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>config</b></td>
        <td>JSON</td>
        <td>
          Config demonstrates available parameters for template customization,
that can be used when creating ClusterDeployment objects.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>description</b></td>
        <td>string</td>
        <td>
          Description contains information about the template.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>k8sConstraint</b></td>
        <td>string</td>
        <td>
          Constraint describing compatible K8S versions of the cluster set in the SemVer format.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>observedGeneration</b></td>
        <td>integer</td>
        <td>
          ObservedGeneration is the last observed generation.<br/>
          <br/>
            <i>Format</i>: int64<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatestatussourcestatus-1">sourceStatus</a></b></td>
        <td>object</td>
        <td>
          SourceStatus reflects the status of the source.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>validationError</b></td>
        <td>string</td>
        <td>
          ValidationError provides information regarding issues encountered during template validation.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.status.chartRef
<sup><sup>[↩ Parent](#servicetemplatestatus-1)</sup></sup>



ChartRef is a reference to a source controller resource containing the
Helm chart representing the template.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>kind</b></td>
        <td>enum</td>
        <td>
          Kind of the referent.<br/>
          <br/>
            <i>Enum</i>: OCIRepository, HelmChart<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name of the referent.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>apiVersion</b></td>
        <td>string</td>
        <td>
          APIVersion of the referent.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace of the referent, defaults to the namespace of the Kubernetes
resource object that contains the reference.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.status.sourceStatus
<sup><sup>[↩ Parent](#servicetemplatestatus-1)</sup></sup>



SourceStatus reflects the status of the source.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>kind</b></td>
        <td>string</td>
        <td>
          Kind is the kind of the remote source.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name is the name of the remote source.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace is the namespace of the remote source.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b><a href="#servicetemplatestatussourcestatusartifact-1">artifact</a></b></td>
        <td>object</td>
        <td>
          Artifact is the artifact that was generated from the template source.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b><a href="#servicetemplatestatussourcestatusconditionsindex-1">conditions</a></b></td>
        <td>[]object</td>
        <td>
          Conditions reflects the conditions of the remote source object.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>observedGeneration</b></td>
        <td>integer</td>
        <td>
          ObservedGeneration is the latest source generation observed by the controller.<br/>
          <br/>
            <i>Format</i>: int64<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.status.sourceStatus.artifact
<sup><sup>[↩ Parent](#servicetemplatestatussourcestatus-1)</sup></sup>



Artifact is the artifact that was generated from the template source.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>lastUpdateTime</b></td>
        <td>string</td>
        <td>
          LastUpdateTime is the timestamp corresponding to the last update of the
Artifact.<br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>path</b></td>
        <td>string</td>
        <td>
          Path is the relative file path of the Artifact. It can be used to locate
the file in the root of the Artifact storage on the local file system of
the controller managing the Source.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>revision</b></td>
        <td>string</td>
        <td>
          Revision is a human-readable identifier traceable in the origin source
system. It can be a Git commit SHA, Git tag, a Helm chart version, etc.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>url</b></td>
        <td>string</td>
        <td>
          URL is the HTTP address of the Artifact as exposed by the controller
managing the Source. It can be used to retrieve the Artifact for
consumption, e.g. by another controller applying the Artifact contents.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>digest</b></td>
        <td>string</td>
        <td>
          Digest is the digest of the file in the form of '<algorithm>:<checksum>'.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>metadata</b></td>
        <td>map[string]string</td>
        <td>
          Metadata holds upstream information such as OCI annotations.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>size</b></td>
        <td>integer</td>
        <td>
          Size is the number of bytes in the file.<br/>
          <br/>
            <i>Format</i>: int64<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.status.sourceStatus.conditions[index]
<sup><sup>[↩ Parent](#servicetemplatestatussourcestatus-1)</sup></sup>



Condition contains details for one aspect of the current state of this API Resource.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>lastTransitionTime</b></td>
        <td>string</td>
        <td>
          lastTransitionTime is the last time the condition transitioned from one status to another.
This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable.<br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>message</b></td>
        <td>string</td>
        <td>
          message is a human readable message indicating details about the transition.
This may be an empty string.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>reason</b></td>
        <td>string</td>
        <td>
          reason contains a programmatic identifier indicating the reason for the condition's last transition.
Producers of specific condition types may define expected values and meanings for this field,
and whether the values are considered a guaranteed API.
The value should be a CamelCase string.
This field may not be empty.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>status</b></td>
        <td>enum</td>
        <td>
          status of the condition, one of True, False, Unknown.<br/>
          <br/>
            <i>Enum</i>: True, False, Unknown<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>type</b></td>
        <td>string</td>
        <td>
          type of condition in CamelCase or in foo.example.com/CamelCase.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>observedGeneration</b></td>
        <td>integer</td>
        <td>
          observedGeneration represents the .metadata.generation that the condition was set based upon.
For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date
with respect to the current state of the instance.<br/>
          <br/>
            <i>Format</i>: int64<br/>
            <i>Minimum</i>: 0<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>
