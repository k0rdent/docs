# API Reference

Packages:

- [k0rdent.mirantis.com/v1beta1](#k0rdentmirantiscomv1beta1)

# k0rdent.mirantis.com/v1beta1

Resource Types:

- [AccessManagement](#accessmanagement)

- [ClusterAuthentication](#clusterauthentication)

- [ClusterDataSource](#clusterdatasource)

- [ClusterDeployment](#clusterdeployment)

- [ClusterIPAMClaim](#clusteripamclaim)

- [ClusterIPAM](#clusteripam)

- [ClusterTemplateChain](#clustertemplatechain)

- [ClusterTemplate](#clustertemplate)

- [Credential](#credential)

- [DataSource](#datasource)

- [ManagementBackup](#managementbackup)

- [Management](#management)

- [MultiClusterService](#multiclusterservice)

- [ProviderTemplate](#providertemplate)

- [Region](#region)

- [Release](#release)

- [ServiceSet](#serviceset)

- [ServiceTemplateChain](#servicetemplatechain)

- [ServiceTemplate](#servicetemplate)

- [StateManagementProvider](#statemanagementprovider)




## AccessManagement






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
        <td><b>spec</b></td>
        <td>object</td>
        <td>
          AccessManagementSpec defines the desired state of AccessManagement<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>status</b></td>
        <td>object</td>
        <td>
          AccessManagementStatus defines the observed state of AccessManagement<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### AccessManagement.spec



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
        <td><b>accessRules</b></td>
        <td>[]object</td>
        <td>
          AccessRules is the list of access rules. Each AccessRule enforces
objects distribution to the TargetNamespaces.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### AccessManagement.spec.accessRules[index]



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
        <td><b>clusterAuthentications</b></td>
        <td>[]string</td>
        <td>
          ClusterAuthentications is the list of [ClusterAuthentication] names that will be distributed to all the
namespaces specified in TargetNamespaces.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>clusterTemplateChains</b></td>
        <td>[]string</td>
        <td>
          ClusterTemplateChains is the list of [ClusterTemplateChain] names whose ClusterTemplates
will be distributed to all namespaces specified in TargetNamespaces.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>credentials</b></td>
        <td>[]string</td>
        <td>
          Credentials is the list of [Credential] names that will be distributed to all the
namespaces specified in TargetNamespaces.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>dataSources</b></td>
        <td>[]string</td>
        <td>
          DataSources is the list of [DataSource] names that will be distributed to all the
namespaces specified in TargetNamespaces.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>serviceTemplateChains</b></td>
        <td>[]string</td>
        <td>
          ServiceTemplateChains is the list of [ServiceTemplateChain] names whose ServiceTemplates
will be distributed to all namespaces specified in TargetNamespaces.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>targetNamespaces</b></td>
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
        <td><b>selector</b></td>
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
        <td><b>matchExpressions</b></td>
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
        <td><b>current</b></td>
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
        <td><b>clusterAuthentications</b></td>
        <td>[]string</td>
        <td>
          ClusterAuthentications is the list of [ClusterAuthentication] names that will be distributed to all the
namespaces specified in TargetNamespaces.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>clusterTemplateChains</b></td>
        <td>[]string</td>
        <td>
          ClusterTemplateChains is the list of [ClusterTemplateChain] names whose ClusterTemplates
will be distributed to all namespaces specified in TargetNamespaces.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>credentials</b></td>
        <td>[]string</td>
        <td>
          Credentials is the list of [Credential] names that will be distributed to all the
namespaces specified in TargetNamespaces.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>dataSources</b></td>
        <td>[]string</td>
        <td>
          DataSources is the list of [DataSource] names that will be distributed to all the
namespaces specified in TargetNamespaces.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>serviceTemplateChains</b></td>
        <td>[]string</td>
        <td>
          ServiceTemplateChains is the list of [ServiceTemplateChain] names whose ServiceTemplates
will be distributed to all namespaces specified in TargetNamespaces.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>targetNamespaces</b></td>
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
        <td><b>selector</b></td>
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
        <td><b>matchExpressions</b></td>
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

## ClusterAuthentication






ClusterAuthentication is the Schema for the cluster authentication configuration API

<table>
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
      <td>ClusterAuthentication</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b>spec</b></td>
        <td>object</td>
        <td>
          ClusterAuthenticationSpec defines the desired state of ClusterAuthentication<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterAuthentication.spec



ClusterAuthenticationSpec defines the desired state of ClusterAuthentication

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>authenticationConfiguration</b></td>
        <td>object</td>
        <td>
          AuthenticationConfiguration contains the full content of an [AuthenticationConfiguration] object,
which defines how the API server should perform request authentication.

For more details, see: https://kubernetes.io/docs/reference/access-authn-authz/authentication/#using-authentication-configuration<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>caSecret</b></td>
        <td>object</td>
        <td>
          CASecret is the reference to the secret containing the CA certificates used to validate the connection
to the issuers endpoints.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterAuthentication.spec.authenticationConfiguration



AuthenticationConfiguration contains the full content of an [AuthenticationConfiguration] object,
which defines how the API server should perform request authentication.

For more details, see: https://kubernetes.io/docs/reference/access-authn-authz/authentication/#using-authentication-configuration

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>jwt</b></td>
        <td>[]object</td>
        <td>
          jwt is a list of authenticator to authenticate Kubernetes users using
JWT compliant tokens. The authenticator will attempt to parse a raw ID token,
verify it's been signed by the configured issuer. The public key to verify the
signature is discovered from the issuer's public endpoint using OIDC discovery.
For an incoming token, each JWT authenticator will be attempted in
the order in which it is specified in this list.  Note however that
other authenticators may run before or after the JWT authenticators.
The specific position of JWT authenticators in relation to other
authenticators is neither defined nor stable across releases.  Since
each JWT authenticator must have a unique issuer URL, at most one
JWT authenticator will attempt to cryptographically validate the token.

The minimum valid JWT payload must contain the following claims:
{
		"iss": "https://issuer.example.com",
		"aud": ["audience"],
		"exp": 1234567890,
		"<username claim>": "username"
}<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>anonymous</b></td>
        <td>object</td>
        <td>
          If present --anonymous-auth must not be set<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>apiVersion</b></td>
        <td>string</td>
        <td>
          APIVersion defines the versioned schema of this representation of an object.
Servers should convert recognized schemas to the latest internal value, and
may reject unrecognized values.
More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>kind</b></td>
        <td>string</td>
        <td>
          Kind is a string value representing the REST resource this object represents.
Servers may infer this from the endpoint the client submits requests to.
Cannot be updated.
In CamelCase.
More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterAuthentication.spec.authenticationConfiguration.jwt[index]



JWTAuthenticator provides the configuration for a single JWT authenticator.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>claimMappings</b></td>
        <td>object</td>
        <td>
          claimMappings points claims of a token to be treated as user attributes.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>issuer</b></td>
        <td>object</td>
        <td>
          issuer contains the basic OIDC provider connection options.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>claimValidationRules</b></td>
        <td>[]object</td>
        <td>
          claimValidationRules are rules that are applied to validate token claims to authenticate users.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>userValidationRules</b></td>
        <td>[]object</td>
        <td>
          userValidationRules are rules that are applied to final user before completing authentication.
These allow invariants to be applied to incoming identities such as preventing the
use of the system: prefix that is commonly used by Kubernetes components.
The validation rules are logically ANDed together and must all return true for the validation to pass.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterAuthentication.spec.authenticationConfiguration.jwt[index].claimMappings



claimMappings points claims of a token to be treated as user attributes.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>username</b></td>
        <td>object</td>
        <td>
          username represents an option for the username attribute.
The claim's value must be a singular string.
Same as the --oidc-username-claim and --oidc-username-prefix flags.
If username.expression is set, the expression must produce a string value.
If username.expression uses 'claims.email', then 'claims.email_verified' must be used in
username.expression or extra[*].valueExpression or claimValidationRules[*].expression.
An example claim validation rule expression that matches the validation automatically
applied when username.claim is set to 'email' is 'claims.?email_verified.orValue(true) == true'. By explicitly comparing
the value to true, we let type-checking see the result will be a boolean, and to make sure a non-boolean email_verified
claim will be caught at runtime.

In the flag based approach, the --oidc-username-claim and --oidc-username-prefix are optional. If --oidc-username-claim is not set,
the default value is "sub". For the authentication config, there is no defaulting for claim or prefix. The claim and prefix must be set explicitly.
For claim, if --oidc-username-claim was not set with legacy flag approach, configure username.claim="sub" in the authentication config.
For prefix:
    (1) --oidc-username-prefix="-", no prefix was added to the username. For the same behavior using authentication config,
        set username.prefix=""
    (2) --oidc-username-prefix="" and  --oidc-username-claim != "email", prefix was "<value of --oidc-issuer-url>#". For the same
        behavior using authentication config, set username.prefix="<value of issuer.url>#"
    (3) --oidc-username-prefix="<value>". For the same behavior using authentication config, set username.prefix="<value>"<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>extra</b></td>
        <td>[]object</td>
        <td>
          extra represents an option for the extra attribute.
expression must produce a string or string array value.
If the value is empty, the extra mapping will not be present.

hard-coded extra key/value
- key: "foo"
  valueExpression: "'bar'"
This will result in an extra attribute - foo: ["bar"]

hard-coded key, value copying claim value
- key: "foo"
  valueExpression: "claims.some_claim"
This will result in an extra attribute - foo: [value of some_claim]

hard-coded key, value derived from claim value
- key: "admin"
  valueExpression: '(has(claims.is_admin) && claims.is_admin) ? "true":""'
This will result in:
 - if is_admin claim is present and true, extra attribute - admin: ["true"]
 - if is_admin claim is present and false or is_admin claim is not present, no extra attribute will be added<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>groups</b></td>
        <td>object</td>
        <td>
          groups represents an option for the groups attribute.
The claim's value must be a string or string array claim.
If groups.claim is set, the prefix must be specified (and can be the empty string).
If groups.expression is set, the expression must produce a string or string array value.
 "", [], and null values are treated as the group mapping not being present.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>uid</b></td>
        <td>object</td>
        <td>
          uid represents an option for the uid attribute.
Claim must be a singular string claim.
If uid.expression is set, the expression must produce a string value.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterAuthentication.spec.authenticationConfiguration.jwt[index].claimMappings.username



username represents an option for the username attribute.
The claim's value must be a singular string.
Same as the --oidc-username-claim and --oidc-username-prefix flags.
If username.expression is set, the expression must produce a string value.
If username.expression uses 'claims.email', then 'claims.email_verified' must be used in
username.expression or extra[*].valueExpression or claimValidationRules[*].expression.
An example claim validation rule expression that matches the validation automatically
applied when username.claim is set to 'email' is 'claims.?email_verified.orValue(true) == true'. By explicitly comparing
the value to true, we let type-checking see the result will be a boolean, and to make sure a non-boolean email_verified
claim will be caught at runtime.

In the flag based approach, the --oidc-username-claim and --oidc-username-prefix are optional. If --oidc-username-claim is not set,
the default value is "sub". For the authentication config, there is no defaulting for claim or prefix. The claim and prefix must be set explicitly.
For claim, if --oidc-username-claim was not set with legacy flag approach, configure username.claim="sub" in the authentication config.
For prefix:
    (1) --oidc-username-prefix="-", no prefix was added to the username. For the same behavior using authentication config,
        set username.prefix=""
    (2) --oidc-username-prefix="" and  --oidc-username-claim != "email", prefix was "<value of --oidc-issuer-url>#". For the same
        behavior using authentication config, set username.prefix="<value of issuer.url>#"
    (3) --oidc-username-prefix="<value>". For the same behavior using authentication config, set username.prefix="<value>"

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>claim</b></td>
        <td>string</td>
        <td>
          claim is the JWT claim to use.
Mutually exclusive with expression.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>expression</b></td>
        <td>string</td>
        <td>
          expression represents the expression which will be evaluated by CEL.

CEL expressions have access to the contents of the token claims, organized into CEL variable:
- 'claims' is a map of claim names to claim values.
  For example, a variable named 'sub' can be accessed as 'claims.sub'.
  Nested claims can be accessed using dot notation, e.g. 'claims.foo.bar'.

Documentation on CEL: https://kubernetes.io/docs/reference/using-api/cel/

Mutually exclusive with claim and prefix.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>prefix</b></td>
        <td>string</td>
        <td>
          prefix is prepended to claim's value to prevent clashes with existing names.
prefix needs to be set if claim is set and can be the empty string.
Mutually exclusive with expression.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterAuthentication.spec.authenticationConfiguration.jwt[index].claimMappings.extra[index]



ExtraMapping provides the configuration for a single extra mapping.

<table>
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
          key is a string to use as the extra attribute key.
key must be a domain-prefix path (e.g. example.org/foo). All characters before the first "/" must be a valid
subdomain as defined by RFC 1123. All characters trailing the first "/" must
be valid HTTP Path characters as defined by RFC 3986.
key must be lowercase.
Required to be unique.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>valueExpression</b></td>
        <td>string</td>
        <td>
          valueExpression is a CEL expression to extract extra attribute value.
valueExpression must produce a string or string array value.
"", [], and null values are treated as the extra mapping not being present.
Empty string values contained within a string array are filtered out.

CEL expressions have access to the contents of the token claims, organized into CEL variable:
- 'claims' is a map of claim names to claim values.
  For example, a variable named 'sub' can be accessed as 'claims.sub'.
  Nested claims can be accessed using dot notation, e.g. 'claims.foo.bar'.

Documentation on CEL: https://kubernetes.io/docs/reference/using-api/cel/<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ClusterAuthentication.spec.authenticationConfiguration.jwt[index].claimMappings.groups



groups represents an option for the groups attribute.
The claim's value must be a string or string array claim.
If groups.claim is set, the prefix must be specified (and can be the empty string).
If groups.expression is set, the expression must produce a string or string array value.
 "", [], and null values are treated as the group mapping not being present.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>claim</b></td>
        <td>string</td>
        <td>
          claim is the JWT claim to use.
Mutually exclusive with expression.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>expression</b></td>
        <td>string</td>
        <td>
          expression represents the expression which will be evaluated by CEL.

CEL expressions have access to the contents of the token claims, organized into CEL variable:
- 'claims' is a map of claim names to claim values.
  For example, a variable named 'sub' can be accessed as 'claims.sub'.
  Nested claims can be accessed using dot notation, e.g. 'claims.foo.bar'.

Documentation on CEL: https://kubernetes.io/docs/reference/using-api/cel/

Mutually exclusive with claim and prefix.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>prefix</b></td>
        <td>string</td>
        <td>
          prefix is prepended to claim's value to prevent clashes with existing names.
prefix needs to be set if claim is set and can be the empty string.
Mutually exclusive with expression.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterAuthentication.spec.authenticationConfiguration.jwt[index].claimMappings.uid



uid represents an option for the uid attribute.
Claim must be a singular string claim.
If uid.expression is set, the expression must produce a string value.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>claim</b></td>
        <td>string</td>
        <td>
          claim is the JWT claim to use.
Either claim or expression must be set.
Mutually exclusive with expression.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>expression</b></td>
        <td>string</td>
        <td>
          expression represents the expression which will be evaluated by CEL.

CEL expressions have access to the contents of the token claims, organized into CEL variable:
- 'claims' is a map of claim names to claim values.
  For example, a variable named 'sub' can be accessed as 'claims.sub'.
  Nested claims can be accessed using dot notation, e.g. 'claims.foo.bar'.

Documentation on CEL: https://kubernetes.io/docs/reference/using-api/cel/

Mutually exclusive with claim.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterAuthentication.spec.authenticationConfiguration.jwt[index].issuer



issuer contains the basic OIDC provider connection options.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>audiences</b></td>
        <td>[]string</td>
        <td>
          audiences is the set of acceptable audiences the JWT must be issued to.
At least one of the entries must match the "aud" claim in presented JWTs.
Same value as the --oidc-client-id flag (though this field supports an array).
Required to be non-empty.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>url</b></td>
        <td>string</td>
        <td>
          url points to the issuer URL in a format https://url or https://url/path.
This must match the "iss" claim in the presented JWT, and the issuer returned from discovery.
Same value as the --oidc-issuer-url flag.
Discovery information is fetched from "{url}/.well-known/openid-configuration" unless overridden by discoveryURL.
Required to be unique across all JWT authenticators.
Note that egress selection configuration is not used for this network connection.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>audienceMatchPolicy</b></td>
        <td>string</td>
        <td>
          audienceMatchPolicy defines how the "audiences" field is used to match the "aud" claim in the presented JWT.
Allowed values are:
1. "MatchAny" when multiple audiences are specified and
2. empty (or unset) or "MatchAny" when a single audience is specified.

- MatchAny: the "aud" claim in the presented JWT must match at least one of the entries in the "audiences" field.
For example, if "audiences" is ["foo", "bar"], the "aud" claim in the presented JWT must contain either "foo" or "bar" (and may contain both).

- "": The match policy can be empty (or unset) when a single audience is specified in the "audiences" field. The "aud" claim in the presented JWT must contain the single audience (and may contain others).

For more nuanced audience validation, use claimValidationRules.
  example: claimValidationRule[].expression: 'sets.equivalent(claims.aud, ["bar", "foo", "baz"])' to require an exact match.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>certificateAuthority</b></td>
        <td>string</td>
        <td>
          certificateAuthority contains PEM-encoded certificate authority certificates
used to validate the connection when fetching discovery information.
If unset, the system verifier is used.
Same value as the content of the file referenced by the --oidc-ca-file flag.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>discoveryURL</b></td>
        <td>string</td>
        <td>
          discoveryURL, if specified, overrides the URL used to fetch discovery
information instead of using "{url}/.well-known/openid-configuration".
The exact value specified is used, so "/.well-known/openid-configuration"
must be included in discoveryURL if needed.

The "issuer" field in the fetched discovery information must match the "issuer.url" field
in the AuthenticationConfiguration and will be used to validate the "iss" claim in the presented JWT.
This is for scenarios where the well-known and jwks endpoints are hosted at a different
location than the issuer (such as locally in the cluster).

Example:
A discovery url that is exposed using kubernetes service 'oidc' in namespace 'oidc-namespace'
and discovery information is available at '/.well-known/openid-configuration'.
discoveryURL: "https://oidc.oidc-namespace/.well-known/openid-configuration"
certificateAuthority is used to verify the TLS connection and the hostname on the leaf certificate
must be set to 'oidc.oidc-namespace'.

curl https://oidc.oidc-namespace/.well-known/openid-configuration (.discoveryURL field)
{
    issuer: "https://oidc.example.com" (.url field)
}

discoveryURL must be different from url.
Required to be unique across all JWT authenticators.
Note that egress selection configuration is not used for this network connection.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>egressSelectorType</b></td>
        <td>string</td>
        <td>
          egressSelectorType is an indicator of which egress selection should be used for sending all traffic related
to this issuer (discovery, JWKS, distributed claims, etc).  If unspecified, no custom dialer is used.
When specified, the valid choices are "controlplane" and "cluster".  These correspond to the associated
values in the --egress-selector-config-file.

- controlplane: for traffic intended to go to the control plane.

- cluster: for traffic intended to go to the system being managed by Kubernetes.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterAuthentication.spec.authenticationConfiguration.jwt[index].claimValidationRules[index]



ClaimValidationRule provides the configuration for a single claim validation rule.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>claim</b></td>
        <td>string</td>
        <td>
          claim is the name of a required claim.
Same as --oidc-required-claim flag.
Only string claim keys are supported.
Mutually exclusive with expression and message.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>expression</b></td>
        <td>string</td>
        <td>
          expression represents the expression which will be evaluated by CEL.
Must produce a boolean.

CEL expressions have access to the contents of the token claims, organized into CEL variable:
- 'claims' is a map of claim names to claim values.
  For example, a variable named 'sub' can be accessed as 'claims.sub'.
  Nested claims can be accessed using dot notation, e.g. 'claims.foo.bar'.
Must return true for the validation to pass.

Documentation on CEL: https://kubernetes.io/docs/reference/using-api/cel/

Mutually exclusive with claim and requiredValue.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>message</b></td>
        <td>string</td>
        <td>
          message customizes the returned error message when expression returns false.
message is a literal string.
Mutually exclusive with claim and requiredValue.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>requiredValue</b></td>
        <td>string</td>
        <td>
          requiredValue is the value of a required claim.
Same as --oidc-required-claim flag.
Only string claim values are supported.
If claim is set and requiredValue is not set, the claim must be present with a value set to the empty string.
Mutually exclusive with expression and message.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterAuthentication.spec.authenticationConfiguration.jwt[index].userValidationRules[index]



UserValidationRule provides the configuration for a single user info validation rule.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>expression</b></td>
        <td>string</td>
        <td>
          expression represents the expression which will be evaluated by CEL.
Must return true for the validation to pass.

CEL expressions have access to the contents of UserInfo, organized into CEL variable:
- 'user' - authentication.k8s.io/v1, Kind=UserInfo object
   Refer to https://github.com/kubernetes/api/blob/release-1.28/authentication/v1/types.go#L105-L122 for the definition.
   API documentation: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#userinfo-v1-authentication-k8s-io

Documentation on CEL: https://kubernetes.io/docs/reference/using-api/cel/<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>message</b></td>
        <td>string</td>
        <td>
          message customizes the returned error message when rule returns false.
message is a literal string.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterAuthentication.spec.authenticationConfiguration.anonymous



If present --anonymous-auth must not be set

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>enabled</b></td>
        <td>boolean</td>
        <td>
          <br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>conditions</b></td>
        <td>[]object</td>
        <td>
          If set, anonymous auth is only allowed if the request meets one of the
conditions.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterAuthentication.spec.authenticationConfiguration.anonymous.conditions[index]



AnonymousAuthCondition describes the condition under which anonymous auth
should be enabled.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>path</b></td>
        <td>string</td>
        <td>
          Path for which anonymous auth is enabled.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ClusterAuthentication.spec.caSecret



CASecret is the reference to the secret containing the CA certificates used to validate the connection
to the issuers endpoints.

<table>
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
          Key is the name of the key for the given Secret reference where the value is stored.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          name is unique within a namespace to reference a secret resource.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          namespace defines the space within which the secret name must be unique.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>

## ClusterDataSource






ClusterDataSource is the Schema for the clusterdatasources API

<table>
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
      <td>ClusterDataSource</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b>spec</b></td>
        <td>object</td>
        <td>
          ClusterDataSourceSpec defines the desired state of ClusterDataSource<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>status</b></td>
        <td>object</td>
        <td>
          ClusterDataSourceStatus defines the observed state of ClusterDataSource<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDataSource.spec



ClusterDataSourceSpec defines the desired state of ClusterDataSource

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>dataSource</b></td>
        <td>string</td>
        <td>
          DataSource references the [DataSource] object (in the same namespace) that provides database connection
information and credentials.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>schema</b></td>
        <td>string</td>
        <td>
          Schema is the name of the database for the Cluster. This value is immutable.
The value defaults to the namespace and name of the [ClusterDeployment] with some short random suffix.<br/>
          <br/>
            <i>Validations</i>:<li>self == oldSelf: changing the schema is not supported</li>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ClusterDataSource.status



ClusterDataSourceStatus defines the observed state of ClusterDataSource

<table>
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
          Ready indicates whether the object is fully initialized and operational.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>caSecret</b></td>
        <td>string</td>
        <td>
          CASecret is the name of the Secret containing the CA certificate used to establish a TLS-secured
connection to the datastore, if applicable.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>error</b></td>
        <td>string</td>
        <td>
          Error contains a description of any errors that occurred, if applicable. It is omitted if no errors are present.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>kineDataSourceSecret</b></td>
        <td>string</td>
        <td>
          KineDataSourceSecret is the name of the Secret containing credentials for the Kine datastore connection.
Created and managed by the controller.<br/>
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

## ClusterDeployment






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
        <td><b>spec</b></td>
        <td>object</td>
        <td>
          ClusterDeploymentSpec defines the desired state of ClusterDeployment<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>status</b></td>
        <td>object</td>
        <td>
          ClusterDeploymentStatus defines the observed state of ClusterDeployment<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.spec



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
        <td><b>cleanupOnDeletion</b></td>
        <td>boolean</td>
        <td>
          CleanupOnDeletion specifies whether potentially orphaned Services and PVCs
should be removed during the object deletion.
This is a best-effort cleanup, if there is no possibility to acquire
a managed cluster's kubeconfig, the cleanup will NOT happen.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>clusterAuth</b></td>
        <td>string</td>
        <td>
          Name reference to the related [ClusterAuthentication] object.<br/>
        </td>
        <td>false</td>
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
          Name reference to the related [Credential] object located in the same namespace.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>dataSource</b></td>
        <td>string</td>
        <td>
          DataSource is the name reference to the related [DataSource] object located in the same namespace.<br/>
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
        <td><b>ipamClaim</b></td>
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
        <td><b>serviceSpec</b></td>
        <td>object</td>
        <td>
          ServiceSpec is spec related to deployment of services.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.spec.ipamClaim



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
        <td><b>spec</b></td>
        <td>object</td>
        <td>
          ClusterIPAMClaimSpec defines the inline IPAM claim specification if no reference is provided.
This allows for dynamic IP address allocation during cluster provisioning.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.spec.ipamClaim.spec



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
        <td><b>clusterNetwork</b></td>
        <td>object</td>
        <td>
          ClusterNetwork defines the allocation for requisitioning ip addresses for use by the k8s cluster itself<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>externalNetwork</b></td>
        <td>object</td>
        <td>
          ExternalNetwork defines the allocation for requisitioning ip addresses for use by services such as load balancers<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>nodeNetwork</b></td>
        <td>object</td>
        <td>
          NodeNetwork defines the allocation requisitioning ip addresses for cluster nodes<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.spec.ipamClaim.spec.clusterNetwork



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
        <td><b>gateway</b></td>
        <td>string</td>
        <td>
          Gateway to be used for the address space<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>ipAddresses</b></td>
        <td>[]string</td>
        <td>
          IPAddresses to be allocated<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>prefix</b></td>
        <td>integer</td>
        <td>
          Prefix is the network prefix to use.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.spec.ipamClaim.spec.externalNetwork



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
        <td><b>gateway</b></td>
        <td>string</td>
        <td>
          Gateway to be used for the address space<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>ipAddresses</b></td>
        <td>[]string</td>
        <td>
          IPAddresses to be allocated<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>prefix</b></td>
        <td>integer</td>
        <td>
          Prefix is the network prefix to use.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.spec.ipamClaim.spec.nodeNetwork



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
        <td><b>gateway</b></td>
        <td>string</td>
        <td>
          Gateway to be used for the address space<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>ipAddresses</b></td>
        <td>[]string</td>
        <td>
          IPAddresses to be allocated<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>prefix</b></td>
        <td>integer</td>
        <td>
          Prefix is the network prefix to use.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.spec.serviceSpec



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
          ContinueOnError specifies if the services deployment should continue if an error occurs.

Deprecated: use .provider.config field to define provider-specific configuration.<br/>
          <br/>
            <i>Default</i>: false<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>driftExclusions</b></td>
        <td>[]object</td>
        <td>
          DriftExclusions specifies specific configurations of resources to ignore for drift detection.

Deprecated: use .provider.config field to define provider-specific configuration.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>driftIgnore</b></td>
        <td>[]object</td>
        <td>
          DriftIgnore specifies resources to ignore for drift detection.

Deprecated: use .provider.config field to define provider-specific configuration.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>policyRefs</b></td>
        <td>[]object</td>
        <td>
          PolicyRefs references all the ConfigMaps/Secrets/Flux Sources containing kubernetes resources
that need to be deployed in the target clusters.
The values contained in those resources can be static or leverage Go templates for dynamic customization.
When expressed as templates, the values are filled in using information from
resources within the management cluster before deployment (Cluster and TemplateResourceRefs)

Deprecated: use .provider.config field to define provider-specific configuration.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>priority</b></td>
        <td>integer</td>
        <td>
          Priority sets the priority for the services defined in this spec.
Higher value means higher priority and lower means lower.
In case of conflict with another object managing the service,
the one with higher priority will get to deploy its services.

Deprecated: use .provider.config field to define provider-specific configuration.<br/>
          <br/>
            <i>Format</i>: int32<br/>
            <i>Default</i>: 100<br/>
            <i>Minimum</i>: 1<br/>
            <i>Maximum</i>: 2.147483646e+09<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>object</td>
        <td>
          Provider is the definition of the provider to use to deploy services.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>reload</b></td>
        <td>boolean</td>
        <td>
          Reload instances via rolling upgrade when a ConfigMap/Secret mounted as volume is modified.

Deprecated: use .provider.config field to define provider-specific configuration.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>services</b></td>
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
If set to true, the deployment will stop after encountering the first conflict.

Deprecated: use .provider.config field to define provider-specific configuration.<br/>
          <br/>
            <i>Default</i>: false<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>syncMode</b></td>
        <td>enum</td>
        <td>
          SyncMode specifies how services are synced in the target cluster.

Deprecated: use .provider.config field to define provider-specific configuration.<br/>
          <br/>
            <i>Enum</i>: OneTime, Continuous, ContinuousWithDriftDetection, DryRun<br/>
            <i>Default</i>: Continuous<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>templateResourceRefs</b></td>
        <td>[]object</td>
        <td>
          TemplateResourceRefs is a list of resources to collect from the management cluster,
the values from which can be used in templates.

Deprecated: use .provider.config field to define provider-specific configuration.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.spec.serviceSpec.driftExclusions[index]





<table>
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
        <td><b>target</b></td>
        <td>object</td>
        <td>
          Target points to the resources that the paths refers to.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.spec.serviceSpec.driftExclusions[index].target



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





<table>
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


### ClusterDeployment.spec.serviceSpec.policyRefs[index]





<table>
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
- ConfigMap/Secret
- flux GitRepository;OCIRepository;Bucket<br/>
          <br/>
            <i>Enum</i>: GitRepository, OCIRepository, Bucket, ConfigMap, Secret<br/>
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
        <td><b>deploymentType</b></td>
        <td>enum</td>
        <td>
          DeploymentType indicates whether resources need to be deployed
into the management cluster (local) or the managed cluster (remote)<br/>
          <br/>
            <i>Enum</i>: Local, Remote<br/>
            <i>Default</i>: Remote<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace of the referenced resource.
For ClusterProfile namespace can be left empty. In such a case, namespace will
be implicit set to cluster's namespace.
For Profile namespace must be left empty. Profile namespace will be used.
Namespace can be expressed as a template and instantiate using any cluster field.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>optional</b></td>
        <td>boolean</td>
        <td>
          Optional indicates that the referenced resource is not mandatory.
If set to true and the resource is not found, the error will be ignored,
and Sveltos will continue processing other PolicyRefs.<br/>
          <br/>
            <i>Default</i>: false<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>path</b></td>
        <td>string</td>
        <td>
          Path to the directory containing the YAML files.
Defaults to 'None', which translates to the root path of the SourceRef.
Used only for GitRepository;OCIRepository;Bucket<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.spec.serviceSpec.provider



Provider is the definition of the provider to use to deploy services.

<table>
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
          Config is the provider-specific configuration applied to the produced objects.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name is the name of the [StateManagementProvider] object.<br/>
          <br/>
            <i>Validations</i>:<li>oldSelf == '' || self == oldSelf: Provider name is immutable once set</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>selfManagement</b></td>
        <td>boolean</td>
        <td>
          SelfManagement flag defines whether resources must be deployed to the management cluster itself.
This field is ignored if set for ClusterDeployment.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.spec.serviceSpec.services[index]



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
        <td><b>dependsOn</b></td>
        <td>[]object</td>
        <td>
          DependsOn specifies a list of other services that this service depends on.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>disable</b></td>
        <td>boolean</td>
        <td>
          Disable can be set to disable handling of this service.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>helmOptions</b></td>
        <td>object</td>
        <td>
          HelmOptions are the options to be passed to the provider for helm installation or updates<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace is the namespace the release will be installed in.
It will default to "default" if not provided.<br/>
          <br/>
            <i>Default</i>: default<br/>
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
        <td><b>valuesFrom</b></td>
        <td>[]object</td>
        <td>
          ValuesFrom can reference a ConfigMap or Secret containing helm values.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>version</b></td>
        <td>string</td>
        <td>
          Version is the version of the service template.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.spec.serviceSpec.services[index].dependsOn[index]



ServiceDependsOn identifies a service by its release name and namespace.

<table>
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
          Name is the release name on target cluster.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace is the release namespace on target cluster.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.spec.serviceSpec.services[index].helmOptions



HelmOptions are the options to be passed to the provider for helm installation or updates

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>atomic</b></td>
        <td>boolean</td>
        <td>
          if set, the installation process deletes the installation/upgrades on failure.
The --wait flag will be set automatically if --atomic is used<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>createNamespace</b></td>
        <td>boolean</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>dependencyUpdate</b></td>
        <td>boolean</td>
        <td>
          update dependencies if they are missing before installing the chart<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>description</b></td>
        <td>string</td>
        <td>
          Description is the description of an helm operation<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>disableHooks</b></td>
        <td>boolean</td>
        <td>
          prevent hooks from running during install/upgrade/uninstall<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>disableOpenAPIValidation</b></td>
        <td>boolean</td>
        <td>
          if set, the installation process will not validate rendered templates against the Kubernetes OpenAPI Schema<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>enableClientCache</b></td>
        <td>boolean</td>
        <td>
          EnableClientCache is a flag to enable Helm client cache. If it is not specified, it will be set to false.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>labels</b></td>
        <td>map[string]string</td>
        <td>
          Labels that would be added to release metadata.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>replace</b></td>
        <td>boolean</td>
        <td>
          Replaces if set indicates to replace an older release with this one<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>skipCRDs</b></td>
        <td>boolean</td>
        <td>
          SkipCRDs controls whether CRDs should be installed during install/upgrade operation.
By default, CRDs are installed if not already present.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>skipSchemaValidation</b></td>
        <td>boolean</td>
        <td>
          SkipSchemaValidation determines if JSON schema validation is disabled.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>timeout</b></td>
        <td>string</td>
        <td>
          time to wait for any individual Kubernetes operation (like Jobs for hooks) (default 5m0s)<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>wait</b></td>
        <td>boolean</td>
        <td>
          if set, will wait until all Pods, PVCs, Services, and minimum number of Pods of a Deployment, StatefulSet, or ReplicaSet
are in a ready state before marking the release as successful. It will wait for as long as --timeout<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>waitForJobs</b></td>
        <td>boolean</td>
        <td>
          if set and --wait enabled, will wait until all Jobs have been completed before marking the release as successful.
It will wait for as long as --timeout<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.spec.serviceSpec.services[index].valuesFrom[index]



ValuesFrom is the source of the values to pass to the ServiceTemplate. The source
can be a ConfigMap or a Secret located in the same namespace as the ServiceSet.

<table>
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
          Kind is the kind of the source.<br/>
          <br/>
            <i>Enum</i>: ConfigMap, Secret<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name is the name of the source.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ClusterDeployment.spec.serviceSpec.templateResourceRefs[index]





<table>
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
        <td><b>resource</b></td>
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
        <td><b>conditions</b></td>
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
        <td><b>region</b></td>
        <td>string</td>
        <td>
          Region shows the region the [ClusterDeployment] targets.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>services</b></td>
        <td>[]object</td>
        <td>
          Services contains details for the state of services.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>servicesUpgradePaths</b></td>
        <td>[]object</td>
        <td>
          ServicesUpgradePaths contains details for the state of services upgrade paths.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.status.conditions[index]



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



ServiceState is the state of a Service

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>lastStateTransitionTime</b></td>
        <td>string</td>
        <td>
          LastStateTransitionTime is the time the State was last transitioned<br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name is the name of the Service<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace is the namespace of the Service<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>state</b></td>
        <td>enum</td>
        <td>
          State is the state of the Service<br/>
          <br/>
            <i>Enum</i>: Deployed, Provisioning, Failed, Pending, Deleting<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>template</b></td>
        <td>string</td>
        <td>
          Template is the name of the ServiceTemplate used to deploy the Service<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>type</b></td>
        <td>enum</td>
        <td>
          Type is the type of the deployment method for the Service<br/>
          <br/>
            <i>Enum</i>: Helm, Kustomize, Resource<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>conditions</b></td>
        <td>[]object</td>
        <td>
          Conditions is a list of conditions for the Service<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>failureMessage</b></td>
        <td>string</td>
        <td>
          FailureMessage is the reason why the Service failed to deploy<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>version</b></td>
        <td>string</td>
        <td>
          Version is the version of the Service<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.status.services[index].conditions[index]



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
        <td><b>availableUpgrades</b></td>
        <td>[]object</td>
        <td>
          AvailableUpgrades contains details for the state of available upgrades.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.status.servicesUpgradePaths[index].availableUpgrades[index]



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
          Deprecated: use Versions to define versions that service can be upgraded to.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>versions</b></td>
        <td>[]object</td>
        <td>
          Versions contains the list of versions that service can be upgraded to.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterDeployment.status.servicesUpgradePaths[index].availableUpgrades[index].versions[index]



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
      </tr><tr>
        <td><b>version</b></td>
        <td>string</td>
        <td>
          Version is the version of the Template to which the upgrade is available.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>

## ClusterIPAMClaim






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
        <td><b>spec</b></td>
        <td>object</td>
        <td>
          ClusterIPAMClaimSpec defines the desired state of ClusterIPAMClaim<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>status</b></td>
        <td>object</td>
        <td>
          ClusterIPAMClaimStatus defines the observed state of ClusterIPAMClaim<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterIPAMClaim.spec



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
        <td><b>clusterNetwork</b></td>
        <td>object</td>
        <td>
          ClusterNetwork defines the allocation for requisitioning ip addresses for use by the k8s cluster itself<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>externalNetwork</b></td>
        <td>object</td>
        <td>
          ExternalNetwork defines the allocation for requisitioning ip addresses for use by services such as load balancers<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>nodeNetwork</b></td>
        <td>object</td>
        <td>
          NodeNetwork defines the allocation requisitioning ip addresses for cluster nodes<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterIPAMClaim.spec.clusterNetwork



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
        <td><b>gateway</b></td>
        <td>string</td>
        <td>
          Gateway to be used for the address space<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>ipAddresses</b></td>
        <td>[]string</td>
        <td>
          IPAddresses to be allocated<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>prefix</b></td>
        <td>integer</td>
        <td>
          Prefix is the network prefix to use.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterIPAMClaim.spec.externalNetwork



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
        <td><b>gateway</b></td>
        <td>string</td>
        <td>
          Gateway to be used for the address space<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>ipAddresses</b></td>
        <td>[]string</td>
        <td>
          IPAddresses to be allocated<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>prefix</b></td>
        <td>integer</td>
        <td>
          Prefix is the network prefix to use.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterIPAMClaim.spec.nodeNetwork



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
        <td><b>gateway</b></td>
        <td>string</td>
        <td>
          Gateway to be used for the address space<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>ipAddresses</b></td>
        <td>[]string</td>
        <td>
          IPAddresses to be allocated<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>prefix</b></td>
        <td>integer</td>
        <td>
          Prefix is the network prefix to use.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterIPAMClaim.status



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
        <td><b>conditions</b></td>
        <td>[]object</td>
        <td>
          Conditions contains details for the current state of the [ClusterIPAMClaim]<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterIPAMClaim.status.conditions[index]



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
        <td><b>spec</b></td>
        <td>object</td>
        <td>
          ClusterIPAMSpec defines the desired state of ClusterIPAM<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>status</b></td>
        <td>object</td>
        <td>
          ClusterIPAMStatus defines the observed state of ClusterIPAM<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterIPAM.spec



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
        <td><b>providerData</b></td>
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





<table>
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
        <td><b>spec</b></td>
        <td>object</td>
        <td>
          TemplateChainSpec defines the desired state of *TemplateChain<br/>
          <br/>
            <i>Validations</i>:<li>self == oldSelf: Spec is immutable</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>status</b></td>
        <td>object</td>
        <td>
          TemplateChainStatus defines the observed state of *TemplateChain<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplateChain.spec



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
        <td><b>supportedTemplates</b></td>
        <td>[]object</td>
        <td>
          SupportedTemplates is the list of supported Templates definitions and all available upgrade sequences for it.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplateChain.spec.supportedTemplates[index]



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
        <td><b>availableUpgrades</b></td>
        <td>[]object</td>
        <td>
          AvailableUpgrades is the list of available upgrades for the specified Template.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplateChain.spec.supportedTemplates[index].availableUpgrades[index]



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
      </tr><tr>
        <td><b>version</b></td>
        <td>string</td>
        <td>
          Version is the version of the Template to which the upgrade is available.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ClusterTemplateChain.status



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
        <td><b>spec</b></td>
        <td>object</td>
        <td>
          ClusterTemplateSpec defines the desired state of ClusterTemplate<br/>
          <br/>
            <i>Validations</i>:<li>self == oldSelf: Spec is immutable</li><li>!has(self.helm.chartSource): .spec.helm.chartSource is not supported for ClusterTemplates</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>status</b></td>
        <td>object</td>
        <td>
          ClusterTemplateStatus defines the observed state of ClusterTemplate<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec



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
        <td><b>helm</b></td>
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
        <td><b>chartRef</b></td>
        <td>object</td>
        <td>
          ChartRef is a reference to a source controller resource containing the
Helm chart representing the template.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>chartSource</b></td>
        <td>object</td>
        <td>
          ChartSource is a source of a Helm chart representing the template.<br/>
          <br/>
            <i>Validations</i>:<li>has(self.localSourceRef) ? (self.localSourceRef.kind != 'Secret' && self.localSourceRef.kind != 'ConfigMap'): true: Secret and ConfigMap are not supported as Helm chart sources</li><li>has(self.localSourceRef) ? !has(self.remoteSourceSpec): true: LocalSource and RemoteSource are mutually exclusive.</li><li>has(self.remoteSourceSpec) ? !has(self.localSourceRef): true: LocalSource and RemoteSource are mutually exclusive.</li><li>has(self.localSourceRef) || has(self.remoteSourceSpec): One of LocalSource or RemoteSource must be specified.</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>chartSpec</b></td>
        <td>object</td>
        <td>
          ChartSpec defines the desired state of the HelmChart to be created by the controller<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartRef



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
            <i>Enum</i>: OCIRepository, HelmChart, ExternalArtifact<br/>
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
        <td><b>localSourceRef</b></td>
        <td>object</td>
        <td>
          LocalSourceRef is the local source of the kustomize manifest.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>remoteSourceSpec</b></td>
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
[github.com/fluxcd/source-controller/api/v1.Bucket] or [github.com/fluxcd/source-controller/api/v1.OCIRepository].
If the Kind is ConfigMap or Secret, the namespace will be ignored.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec



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
        <td><b>bucket</b></td>
        <td>object</td>
        <td>
          Bucket is the definition of bucket source.<br/>
          <br/>
            <i>Validations</i>:<li>self.provider == 'aws' || self.provider == 'generic' || !has(self.sts): STS configuration is only supported for the 'aws' and 'generic' Bucket providers</li><li>self.provider != 'aws' || !has(self.sts) || self.sts.provider == 'aws': 'aws' is the only supported STS provider for the 'aws' Bucket provider</li><li>self.provider != 'generic' || !has(self.sts) || self.sts.provider == 'ldap': 'ldap' is the only supported STS provider for the 'generic' Bucket provider</li><li>!has(self.sts) || self.sts.provider != 'aws' || !has(self.sts.secretRef): spec.sts.secretRef is not required for the 'aws' STS provider</li><li>!has(self.sts) || self.sts.provider != 'aws' || !has(self.sts.certSecretRef): spec.sts.certSecretRef is not required for the 'aws' STS provider</li><li>self.provider != 'generic' || !has(self.serviceAccountName): ServiceAccountName is not supported for the 'generic' Bucket provider</li><li>!has(self.secretRef) || !has(self.serviceAccountName): cannot set both .spec.secretRef and .spec.serviceAccountName</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>git</b></td>
        <td>object</td>
        <td>
          Git is the definition of git repository source.<br/>
          <br/>
            <i>Validations</i>:<li>!has(self.serviceAccountName) || (has(self.provider) && self.provider == 'azure'): serviceAccountName can only be set when provider is 'azure'</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>oci</b></td>
        <td>object</td>
        <td>
          OCI is the definition of OCI repository source.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.bucket



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
        <td><b>certSecretRef</b></td>
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
        <td><b>proxySecretRef</b></td>
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
        <td><b>secretRef</b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing authentication credentials
for the Bucket.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>serviceAccountName</b></td>
        <td>string</td>
        <td>
          ServiceAccountName is the name of the Kubernetes ServiceAccount used to authenticate
the bucket. This field is only supported for the 'gcp' and 'aws' providers.
For more information about workload identity:
https://fluxcd.io/flux/components/source/buckets/#workload-identity<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>sts</b></td>
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
        <td><b>certSecretRef</b></td>
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
        <td><b>secretRef</b></td>
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
        <td><b>include</b></td>
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
        <td><b>proxySecretRef</b></td>
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
        <td><b>ref</b></td>
        <td>object</td>
        <td>
          Reference specifies the Git reference to resolve and monitor for
changes, defaults to the 'master' branch.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>secretRef</b></td>
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
        <td><b>serviceAccountName</b></td>
        <td>string</td>
        <td>
          ServiceAccountName is the name of the Kubernetes ServiceAccount used to
authenticate to the GitRepository. This field is only supported for 'azure' provider.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>sparseCheckout</b></td>
        <td>[]string</td>
        <td>
          SparseCheckout specifies a list of directories to checkout when cloning
the repository. If specified, only these directories are included in the
Artifact produced for this GitRepository.<br/>
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
        <td><b>verify</b></td>
        <td>object</td>
        <td>
          Verification specifies the configuration to verify the Git commit
signature(s).<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.git.include[index]



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
        <td><b>repository</b></td>
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
        <td><b>secretRef</b></td>
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
        <td><b>certSecretRef</b></td>
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
be of type `Opaque` or `kubernetes.io/tls`.<br/>
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
        <td><b>layerSelector</b></td>
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
        <td><b>proxySecretRef</b></td>
        <td>object</td>
        <td>
          ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the container registry.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>ref</b></td>
        <td>object</td>
        <td>
          The OCI reference to pull and monitor for changes,
defaults to the latest tag.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>secretRef</b></td>
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
        <td><b>verify</b></td>
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

<table>
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
        <td><b>matchOIDCIdentity</b></td>
        <td>[]object</td>
        <td>
          MatchOIDCIdentity specifies the identity matching criteria to use
while verifying an OCI artifact which was signed using Cosign keyless
signing. The artifact's identity is deemed to be verified if any of the
specified matchers match against the identity.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>secretRef</b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Kubernetes Secret containing the
trusted public keys.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSource.remoteSourceSpec.oci.verify.matchOIDCIdentity[index]



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
        <td><b>sourceRef</b></td>
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
        <td><b>verify</b></td>
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
        <td><b>matchOIDCIdentity</b></td>
        <td>[]object</td>
        <td>
          MatchOIDCIdentity specifies the identity matching criteria to use
while verifying an OCI artifact which was signed using Cosign keyless
signing. The artifact's identity is deemed to be verified if any of the
specified matchers match against the identity.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>secretRef</b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Kubernetes Secret containing the
trusted public keys.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ClusterTemplate.spec.helm.chartSpec.verify.matchOIDCIdentity[index]



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
        <td><b>chartRef</b></td>
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
        <td><b>schemaConfigMapName</b></td>
        <td>string</td>
        <td>
          SchemaConfigMapName specifies the name of the ConfigMap that contains the JSON Schema definition for Helm Chart validation.<br/>
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
            <i>Enum</i>: OCIRepository, HelmChart, ExternalArtifact<br/>
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
        <td><b>spec</b></td>
        <td>object</td>
        <td>
          CredentialSpec defines the desired state of Credential<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>status</b></td>
        <td>object</td>
        <td>
          CredentialStatus defines the observed state of Credential<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### Credential.spec



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
        <td><b>identityRef</b></td>
        <td>object</td>
        <td>
          Reference to the Credential Identity<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>description</b></td>
        <td>string</td>
        <td>
          Description of the [Credential] object<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>region</b></td>
        <td>string</td>
        <td>
          Region specifies the region where [ClusterDeployment] resources using
this [Credential] will be deployed<br/>
          <br/>
            <i>Validations</i>:<li>self == oldSelf: Region is immutable</li>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### Credential.spec.identityRef



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
          Ready holds the readiness of [Credential].<br/>
          <br/>
            <i>Default</i>: false<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>conditions</b></td>
        <td>[]object</td>
        <td>
          Conditions contains details for the current state of the [Credential].<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### Credential.status.conditions[index]



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

## DataSource






DataSource is the Schema for the datasources API

<table>
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
      <td>DataSource</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b>spec</b></td>
        <td>object</td>
        <td>
          DataSourceSpec defines the desired state of DataSource<br/>
          <br/>
            <i>Validations</i>:<li>self == oldSelf: changing the spec is not supported, create a new object</li>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### DataSource.spec



DataSourceSpec defines the desired state of DataSource

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>auth</b></td>
        <td>object</td>
        <td>
          Auth specifies the authentication configuration for accessing the data source.
This field contains credentials required to establish
a secure connection to the external data source.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>endpoints</b></td>
        <td>[]string</td>
        <td>
          Endpoints contains one or more host/port pairs that clients should use to connect to the data source.

Only IP:port or FQDN:port, no schema and/or parameters are required.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>type</b></td>
        <td>enum</td>
        <td>
          Type specifies the database type to connect to the data source.<br/>
          <br/>
            <i>Enum</i>: postgresql<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>certificateAuthority</b></td>
        <td>object</td>
        <td>
          CertificateAuthority optionally specifies the reference to a Secret containing
the certificate authority (CA) certificate used to verify the data source's
server certificate during TLS handshake.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### DataSource.spec.auth



Auth specifies the authentication configuration for accessing the data source.
This field contains credentials required to establish
a secure connection to the external data source.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>password</b></td>
        <td>object</td>
        <td>
          Password is a reference to a secret key containing the password credential
used for data source authentication.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>username</b></td>
        <td>object</td>
        <td>
          Username is a reference to a secret key containing the username credential
used for data source authentication.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### DataSource.spec.auth.password



Password is a reference to a secret key containing the password credential
used for data source authentication.

<table>
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
          Key is the name of the key for the given Secret reference where the value is stored.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          name is unique within a namespace to reference a secret resource.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          namespace defines the space within which the secret name must be unique.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### DataSource.spec.auth.username



Username is a reference to a secret key containing the username credential
used for data source authentication.

<table>
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
          Key is the name of the key for the given Secret reference where the value is stored.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          name is unique within a namespace to reference a secret resource.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          namespace defines the space within which the secret name must be unique.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### DataSource.spec.certificateAuthority



CertificateAuthority optionally specifies the reference to a Secret containing
the certificate authority (CA) certificate used to verify the data source's
server certificate during TLS handshake.

<table>
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
          Key is the name of the key for the given Secret reference where the value is stored.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          name is unique within a namespace to reference a secret resource.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          namespace defines the space within which the secret name must be unique.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>

## ManagementBackup






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
        <td><b>spec</b></td>
        <td>object</td>
        <td>
          ManagementBackupSpec defines the desired state of [ManagementBackup].<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>status</b></td>
        <td>object</td>
        <td>
          ManagementBackupStatus defines the observed state of [ManagementBackup].<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ManagementBackup.spec



ManagementBackupSpec defines the desired state of [ManagementBackup].

<table>
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



ManagementBackupStatus defines the observed state of [ManagementBackup].

<table>
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
        <td><b>lastBackup</b></td>
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
      </tr><tr>
        <td><b>region</b></td>
        <td>string</td>
        <td>
          Region reflects the name of a region for which
the [github.com/vmware-tanzu/velero/pkg/apis/velero/v1.Backup] has been created.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>regions</b></td>
        <td>[]object</td>
        <td>
          RegionsLastBackups denotes the status of the last backups in the corresponding regions.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ManagementBackup.status.lastBackup



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
        <td><b>hookStatus</b></td>
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
        <td><b>progress</b></td>
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


### ManagementBackup.status.regions[index]



ManagementBackupSingleStatus defines the observed state of a single entry of [ManagementBackupStatus].

<table>
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
        <td><b>lastBackup</b></td>
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
      </tr><tr>
        <td><b>region</b></td>
        <td>string</td>
        <td>
          Region reflects the name of a region for which
the [github.com/vmware-tanzu/velero/pkg/apis/velero/v1.Backup] has been created.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ManagementBackup.status.regions[index].lastBackup



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
        <td><b>hookStatus</b></td>
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
        <td><b>progress</b></td>
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


### ManagementBackup.status.regions[index].lastBackup.hookStatus



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


### ManagementBackup.status.regions[index].lastBackup.progress



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
        <td><b>spec</b></td>
        <td>object</td>
        <td>
          ManagementSpec defines the desired state of Management<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>status</b></td>
        <td>object</td>
        <td>
          ManagementStatus defines the observed state of Management<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### Management.spec



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
        <td><b>core</b></td>
        <td>object</td>
        <td>
          Core holds the core components that are mandatory.
If not specified, will be populated with the default values.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>providers</b></td>
        <td>[]object</td>
        <td>
          Providers is the list of enabled CAPI providers.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### Management.spec.core



Core holds the core components that are mandatory.
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
        <td><b>capi</b></td>
        <td>object</td>
        <td>
          CAPI represents the core Cluster API component and references the Cluster API template.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>kcm</b></td>
        <td>object</td>
        <td>
          KCM represents the core KCM component and references the KCM template.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### Management.spec.core.capi



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





<table>
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
        <td><b>components</b></td>
        <td>map[string]object</td>
        <td>
          Components indicates the status of installed KCM components and CAPI providers.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>conditions</b></td>
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
        <td><b>spec</b></td>
        <td>object</td>
        <td>
          MultiClusterServiceSpec defines the desired state of MultiClusterService<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>status</b></td>
        <td>object</td>
        <td>
          MultiClusterServiceStatus defines the observed state of MultiClusterService.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.spec



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
        <td><b>clusterSelector</b></td>
        <td>object</td>
        <td>
          ClusterSelector identifies target clusters to manage services on.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>dependsOn</b></td>
        <td>[]string</td>
        <td>
          DependsOn is a list of other MultiClusterServices this one depends on.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>serviceSpec</b></td>
        <td>object</td>
        <td>
          ServiceSpec is spec related to deployment of services.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.spec.clusterSelector



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
        <td><b>matchExpressions</b></td>
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
          ContinueOnError specifies if the services deployment should continue if an error occurs.

Deprecated: use .provider.config field to define provider-specific configuration.<br/>
          <br/>
            <i>Default</i>: false<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>driftExclusions</b></td>
        <td>[]object</td>
        <td>
          DriftExclusions specifies specific configurations of resources to ignore for drift detection.

Deprecated: use .provider.config field to define provider-specific configuration.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>driftIgnore</b></td>
        <td>[]object</td>
        <td>
          DriftIgnore specifies resources to ignore for drift detection.

Deprecated: use .provider.config field to define provider-specific configuration.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>policyRefs</b></td>
        <td>[]object</td>
        <td>
          PolicyRefs references all the ConfigMaps/Secrets/Flux Sources containing kubernetes resources
that need to be deployed in the target clusters.
The values contained in those resources can be static or leverage Go templates for dynamic customization.
When expressed as templates, the values are filled in using information from
resources within the management cluster before deployment (Cluster and TemplateResourceRefs)

Deprecated: use .provider.config field to define provider-specific configuration.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>priority</b></td>
        <td>integer</td>
        <td>
          Priority sets the priority for the services defined in this spec.
Higher value means higher priority and lower means lower.
In case of conflict with another object managing the service,
the one with higher priority will get to deploy its services.

Deprecated: use .provider.config field to define provider-specific configuration.<br/>
          <br/>
            <i>Format</i>: int32<br/>
            <i>Default</i>: 100<br/>
            <i>Minimum</i>: 1<br/>
            <i>Maximum</i>: 2.147483646e+09<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>object</td>
        <td>
          Provider is the definition of the provider to use to deploy services.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>reload</b></td>
        <td>boolean</td>
        <td>
          Reload instances via rolling upgrade when a ConfigMap/Secret mounted as volume is modified.

Deprecated: use .provider.config field to define provider-specific configuration.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>services</b></td>
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
If set to true, the deployment will stop after encountering the first conflict.

Deprecated: use .provider.config field to define provider-specific configuration.<br/>
          <br/>
            <i>Default</i>: false<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>syncMode</b></td>
        <td>enum</td>
        <td>
          SyncMode specifies how services are synced in the target cluster.

Deprecated: use .provider.config field to define provider-specific configuration.<br/>
          <br/>
            <i>Enum</i>: OneTime, Continuous, ContinuousWithDriftDetection, DryRun<br/>
            <i>Default</i>: Continuous<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>templateResourceRefs</b></td>
        <td>[]object</td>
        <td>
          TemplateResourceRefs is a list of resources to collect from the management cluster,
the values from which can be used in templates.

Deprecated: use .provider.config field to define provider-specific configuration.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.spec.serviceSpec.driftExclusions[index]





<table>
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
        <td><b>target</b></td>
        <td>object</td>
        <td>
          Target points to the resources that the paths refers to.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.spec.serviceSpec.driftExclusions[index].target



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





<table>
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


### MultiClusterService.spec.serviceSpec.policyRefs[index]





<table>
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
- ConfigMap/Secret
- flux GitRepository;OCIRepository;Bucket<br/>
          <br/>
            <i>Enum</i>: GitRepository, OCIRepository, Bucket, ConfigMap, Secret<br/>
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
        <td><b>deploymentType</b></td>
        <td>enum</td>
        <td>
          DeploymentType indicates whether resources need to be deployed
into the management cluster (local) or the managed cluster (remote)<br/>
          <br/>
            <i>Enum</i>: Local, Remote<br/>
            <i>Default</i>: Remote<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace of the referenced resource.
For ClusterProfile namespace can be left empty. In such a case, namespace will
be implicit set to cluster's namespace.
For Profile namespace must be left empty. Profile namespace will be used.
Namespace can be expressed as a template and instantiate using any cluster field.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>optional</b></td>
        <td>boolean</td>
        <td>
          Optional indicates that the referenced resource is not mandatory.
If set to true and the resource is not found, the error will be ignored,
and Sveltos will continue processing other PolicyRefs.<br/>
          <br/>
            <i>Default</i>: false<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>path</b></td>
        <td>string</td>
        <td>
          Path to the directory containing the YAML files.
Defaults to 'None', which translates to the root path of the SourceRef.
Used only for GitRepository;OCIRepository;Bucket<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.spec.serviceSpec.provider



Provider is the definition of the provider to use to deploy services.

<table>
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
          Config is the provider-specific configuration applied to the produced objects.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name is the name of the [StateManagementProvider] object.<br/>
          <br/>
            <i>Validations</i>:<li>oldSelf == '' || self == oldSelf: Provider name is immutable once set</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>selfManagement</b></td>
        <td>boolean</td>
        <td>
          SelfManagement flag defines whether resources must be deployed to the management cluster itself.
This field is ignored if set for ClusterDeployment.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.spec.serviceSpec.services[index]



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
        <td><b>dependsOn</b></td>
        <td>[]object</td>
        <td>
          DependsOn specifies a list of other services that this service depends on.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>disable</b></td>
        <td>boolean</td>
        <td>
          Disable can be set to disable handling of this service.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>helmOptions</b></td>
        <td>object</td>
        <td>
          HelmOptions are the options to be passed to the provider for helm installation or updates<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace is the namespace the release will be installed in.
It will default to "default" if not provided.<br/>
          <br/>
            <i>Default</i>: default<br/>
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
        <td><b>valuesFrom</b></td>
        <td>[]object</td>
        <td>
          ValuesFrom can reference a ConfigMap or Secret containing helm values.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>version</b></td>
        <td>string</td>
        <td>
          Version is the version of the service template.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.spec.serviceSpec.services[index].dependsOn[index]



ServiceDependsOn identifies a service by its release name and namespace.

<table>
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
          Name is the release name on target cluster.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace is the release namespace on target cluster.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.spec.serviceSpec.services[index].helmOptions



HelmOptions are the options to be passed to the provider for helm installation or updates

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>atomic</b></td>
        <td>boolean</td>
        <td>
          if set, the installation process deletes the installation/upgrades on failure.
The --wait flag will be set automatically if --atomic is used<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>createNamespace</b></td>
        <td>boolean</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>dependencyUpdate</b></td>
        <td>boolean</td>
        <td>
          update dependencies if they are missing before installing the chart<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>description</b></td>
        <td>string</td>
        <td>
          Description is the description of an helm operation<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>disableHooks</b></td>
        <td>boolean</td>
        <td>
          prevent hooks from running during install/upgrade/uninstall<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>disableOpenAPIValidation</b></td>
        <td>boolean</td>
        <td>
          if set, the installation process will not validate rendered templates against the Kubernetes OpenAPI Schema<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>enableClientCache</b></td>
        <td>boolean</td>
        <td>
          EnableClientCache is a flag to enable Helm client cache. If it is not specified, it will be set to false.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>labels</b></td>
        <td>map[string]string</td>
        <td>
          Labels that would be added to release metadata.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>replace</b></td>
        <td>boolean</td>
        <td>
          Replaces if set indicates to replace an older release with this one<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>skipCRDs</b></td>
        <td>boolean</td>
        <td>
          SkipCRDs controls whether CRDs should be installed during install/upgrade operation.
By default, CRDs are installed if not already present.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>skipSchemaValidation</b></td>
        <td>boolean</td>
        <td>
          SkipSchemaValidation determines if JSON schema validation is disabled.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>timeout</b></td>
        <td>string</td>
        <td>
          time to wait for any individual Kubernetes operation (like Jobs for hooks) (default 5m0s)<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>wait</b></td>
        <td>boolean</td>
        <td>
          if set, will wait until all Pods, PVCs, Services, and minimum number of Pods of a Deployment, StatefulSet, or ReplicaSet
are in a ready state before marking the release as successful. It will wait for as long as --timeout<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>waitForJobs</b></td>
        <td>boolean</td>
        <td>
          if set and --wait enabled, will wait until all Jobs have been completed before marking the release as successful.
It will wait for as long as --timeout<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.spec.serviceSpec.services[index].valuesFrom[index]



ValuesFrom is the source of the values to pass to the ServiceTemplate. The source
can be a ConfigMap or a Secret located in the same namespace as the ServiceSet.

<table>
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
          Kind is the kind of the source.<br/>
          <br/>
            <i>Enum</i>: ConfigMap, Secret<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name is the name of the source.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### MultiClusterService.spec.serviceSpec.templateResourceRefs[index]





<table>
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
        <td><b>resource</b></td>
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
        <td><b>conditions</b></td>
        <td>[]object</td>
        <td>
          Conditions contains details for the current state of the MultiClusterService.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>matchingClusters</b></td>
        <td>[]object</td>
        <td>
          MatchingClusters contains a list of clusters matching MultiClusterService selector<br/>
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
        <td><b>services</b></td>
        <td>[]object</td>
        <td>
          Services contains details for the state of services.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>servicesUpgradePaths</b></td>
        <td>[]object</td>
        <td>
          ServicesUpgradePaths contains details for the state of services upgrade paths.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.status.conditions[index]



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


### MultiClusterService.status.matchingClusters[index]





<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>deployed</b></td>
        <td>boolean</td>
        <td>
          Deployed indicates whether all services were successfully deployed.<br/>
          <br/>
            <i>Default</i>: false<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>regional</b></td>
        <td>boolean</td>
        <td>
          Regional indicates whether given cluster is regional.<br/>
          <br/>
            <i>Default</i>: false<br/>
        </td>
        <td>true</td>
      </tr><tr>
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
        <td><b>lastTransitionTime</b></td>
        <td>string</td>
        <td>
          LastTransitionTime reflects when Deployed state was changed last time.<br/>
          <br/>
            <i>Format</i>: date-time<br/>
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


### MultiClusterService.status.services[index]



ServiceState is the state of a Service

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>lastStateTransitionTime</b></td>
        <td>string</td>
        <td>
          LastStateTransitionTime is the time the State was last transitioned<br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name is the name of the Service<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace is the namespace of the Service<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>state</b></td>
        <td>enum</td>
        <td>
          State is the state of the Service<br/>
          <br/>
            <i>Enum</i>: Deployed, Provisioning, Failed, Pending, Deleting<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>template</b></td>
        <td>string</td>
        <td>
          Template is the name of the ServiceTemplate used to deploy the Service<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>type</b></td>
        <td>enum</td>
        <td>
          Type is the type of the deployment method for the Service<br/>
          <br/>
            <i>Enum</i>: Helm, Kustomize, Resource<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>conditions</b></td>
        <td>[]object</td>
        <td>
          Conditions is a list of conditions for the Service<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>failureMessage</b></td>
        <td>string</td>
        <td>
          FailureMessage is the reason why the Service failed to deploy<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>version</b></td>
        <td>string</td>
        <td>
          Version is the version of the Service<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.status.services[index].conditions[index]



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
        <td><b>availableUpgrades</b></td>
        <td>[]object</td>
        <td>
          AvailableUpgrades contains details for the state of available upgrades.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.status.servicesUpgradePaths[index].availableUpgrades[index]



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
          Deprecated: use Versions to define versions that service can be upgraded to.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>versions</b></td>
        <td>[]object</td>
        <td>
          Versions contains the list of versions that service can be upgraded to.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### MultiClusterService.status.servicesUpgradePaths[index].availableUpgrades[index].versions[index]



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
      </tr><tr>
        <td><b>version</b></td>
        <td>string</td>
        <td>
          Version is the version of the Template to which the upgrade is available.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>

## ProviderTemplate






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
        <td><b>spec</b></td>
        <td>object</td>
        <td>
          ProviderTemplateSpec defines the desired state of ProviderTemplate<br/>
          <br/>
            <i>Validations</i>:<li>self == oldSelf: Spec is immutable</li><li>!has(self.helm.chartSource): .spec.helm.chartSource is not supported for ProviderTemplates</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>status</b></td>
        <td>object</td>
        <td>
          ProviderTemplateStatus defines the observed state of ProviderTemplate<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec



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
        <td><b>helm</b></td>
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
        <td><b>chartRef</b></td>
        <td>object</td>
        <td>
          ChartRef is a reference to a source controller resource containing the
Helm chart representing the template.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>chartSource</b></td>
        <td>object</td>
        <td>
          ChartSource is a source of a Helm chart representing the template.<br/>
          <br/>
            <i>Validations</i>:<li>has(self.localSourceRef) ? (self.localSourceRef.kind != 'Secret' && self.localSourceRef.kind != 'ConfigMap'): true: Secret and ConfigMap are not supported as Helm chart sources</li><li>has(self.localSourceRef) ? !has(self.remoteSourceSpec): true: LocalSource and RemoteSource are mutually exclusive.</li><li>has(self.remoteSourceSpec) ? !has(self.localSourceRef): true: LocalSource and RemoteSource are mutually exclusive.</li><li>has(self.localSourceRef) || has(self.remoteSourceSpec): One of LocalSource or RemoteSource must be specified.</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>chartSpec</b></td>
        <td>object</td>
        <td>
          ChartSpec defines the desired state of the HelmChart to be created by the controller<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartRef



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
            <i>Enum</i>: OCIRepository, HelmChart, ExternalArtifact<br/>
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
        <td><b>localSourceRef</b></td>
        <td>object</td>
        <td>
          LocalSourceRef is the local source of the kustomize manifest.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>remoteSourceSpec</b></td>
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
[github.com/fluxcd/source-controller/api/v1.Bucket] or [github.com/fluxcd/source-controller/api/v1.OCIRepository].
If the Kind is ConfigMap or Secret, the namespace will be ignored.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec



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
        <td><b>bucket</b></td>
        <td>object</td>
        <td>
          Bucket is the definition of bucket source.<br/>
          <br/>
            <i>Validations</i>:<li>self.provider == 'aws' || self.provider == 'generic' || !has(self.sts): STS configuration is only supported for the 'aws' and 'generic' Bucket providers</li><li>self.provider != 'aws' || !has(self.sts) || self.sts.provider == 'aws': 'aws' is the only supported STS provider for the 'aws' Bucket provider</li><li>self.provider != 'generic' || !has(self.sts) || self.sts.provider == 'ldap': 'ldap' is the only supported STS provider for the 'generic' Bucket provider</li><li>!has(self.sts) || self.sts.provider != 'aws' || !has(self.sts.secretRef): spec.sts.secretRef is not required for the 'aws' STS provider</li><li>!has(self.sts) || self.sts.provider != 'aws' || !has(self.sts.certSecretRef): spec.sts.certSecretRef is not required for the 'aws' STS provider</li><li>self.provider != 'generic' || !has(self.serviceAccountName): ServiceAccountName is not supported for the 'generic' Bucket provider</li><li>!has(self.secretRef) || !has(self.serviceAccountName): cannot set both .spec.secretRef and .spec.serviceAccountName</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>git</b></td>
        <td>object</td>
        <td>
          Git is the definition of git repository source.<br/>
          <br/>
            <i>Validations</i>:<li>!has(self.serviceAccountName) || (has(self.provider) && self.provider == 'azure'): serviceAccountName can only be set when provider is 'azure'</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>oci</b></td>
        <td>object</td>
        <td>
          OCI is the definition of OCI repository source.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.bucket



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
        <td><b>certSecretRef</b></td>
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
        <td><b>proxySecretRef</b></td>
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
        <td><b>secretRef</b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing authentication credentials
for the Bucket.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>serviceAccountName</b></td>
        <td>string</td>
        <td>
          ServiceAccountName is the name of the Kubernetes ServiceAccount used to authenticate
the bucket. This field is only supported for the 'gcp' and 'aws' providers.
For more information about workload identity:
https://fluxcd.io/flux/components/source/buckets/#workload-identity<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>sts</b></td>
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
        <td><b>certSecretRef</b></td>
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
        <td><b>secretRef</b></td>
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
        <td><b>include</b></td>
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
        <td><b>proxySecretRef</b></td>
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
        <td><b>ref</b></td>
        <td>object</td>
        <td>
          Reference specifies the Git reference to resolve and monitor for
changes, defaults to the 'master' branch.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>secretRef</b></td>
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
        <td><b>serviceAccountName</b></td>
        <td>string</td>
        <td>
          ServiceAccountName is the name of the Kubernetes ServiceAccount used to
authenticate to the GitRepository. This field is only supported for 'azure' provider.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>sparseCheckout</b></td>
        <td>[]string</td>
        <td>
          SparseCheckout specifies a list of directories to checkout when cloning
the repository. If specified, only these directories are included in the
Artifact produced for this GitRepository.<br/>
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
        <td><b>verify</b></td>
        <td>object</td>
        <td>
          Verification specifies the configuration to verify the Git commit
signature(s).<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.git.include[index]



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
        <td><b>repository</b></td>
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
        <td><b>secretRef</b></td>
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
        <td><b>certSecretRef</b></td>
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
be of type `Opaque` or `kubernetes.io/tls`.<br/>
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
        <td><b>layerSelector</b></td>
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
        <td><b>proxySecretRef</b></td>
        <td>object</td>
        <td>
          ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the container registry.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>ref</b></td>
        <td>object</td>
        <td>
          The OCI reference to pull and monitor for changes,
defaults to the latest tag.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>secretRef</b></td>
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
        <td><b>verify</b></td>
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

<table>
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
        <td><b>matchOIDCIdentity</b></td>
        <td>[]object</td>
        <td>
          MatchOIDCIdentity specifies the identity matching criteria to use
while verifying an OCI artifact which was signed using Cosign keyless
signing. The artifact's identity is deemed to be verified if any of the
specified matchers match against the identity.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>secretRef</b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Kubernetes Secret containing the
trusted public keys.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSource.remoteSourceSpec.oci.verify.matchOIDCIdentity[index]



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
        <td><b>sourceRef</b></td>
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
        <td><b>verify</b></td>
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
        <td><b>matchOIDCIdentity</b></td>
        <td>[]object</td>
        <td>
          MatchOIDCIdentity specifies the identity matching criteria to use
while verifying an OCI artifact which was signed using Cosign keyless
signing. The artifact's identity is deemed to be verified if any of the
specified matchers match against the identity.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>secretRef</b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Kubernetes Secret containing the
trusted public keys.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ProviderTemplate.spec.helm.chartSpec.verify.matchOIDCIdentity[index]



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
        <td><b>chartRef</b></td>
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
        <td><b>schemaConfigMapName</b></td>
        <td>string</td>
        <td>
          SchemaConfigMapName specifies the name of the ConfigMap that contains the JSON Schema definition for Helm Chart validation.<br/>
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
            <i>Enum</i>: OCIRepository, HelmChart, ExternalArtifact<br/>
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

## Region






Region is the Schema for the regions API

<table>
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
      <td>Region</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b>spec</b></td>
        <td>object</td>
        <td>
          RegionSpec defines the desired state of Region<br/>
          <br/>
            <i>Validations</i>:<li>has(self.kubeConfig) != has(self.clusterDeployment): exactly one of kubeConfig or clusterDeployment must be set</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>status</b></td>
        <td>object</td>
        <td>
          RegionStatus defines the observed state of Region<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### Region.spec



RegionSpec defines the desired state of Region

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>clusterDeployment</b></td>
        <td>object</td>
        <td>
          ClusterDeployment is the reference to the existing ClusterDeployment object
to be onboarded as a regional cluster.<br/>
          <br/>
            <i>Validations</i>:<li>self == oldSelf: clusterDeployment is immutable</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>core</b></td>
        <td>object</td>
        <td>
          Core holds the core components that are mandatory.
If not specified, will be populated with the default values.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>kubeConfig</b></td>
        <td>object</td>
        <td>
          KubeConfig references the Secret containing the kubeconfig
of the cluster being onboarded as a regional cluster.
The Secret must reside in the system namespace.<br/>
          <br/>
            <i>Validations</i>:<li>self == oldSelf: kubeConfig is immutable</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>providers</b></td>
        <td>[]object</td>
        <td>
          Providers is the list of enabled CAPI providers.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### Region.spec.clusterDeployment



ClusterDeployment is the reference to the existing ClusterDeployment object
to be onboarded as a regional cluster.

<table>
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
          <br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          <br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### Region.spec.core



Core holds the core components that are mandatory.
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
        <td><b>capi</b></td>
        <td>object</td>
        <td>
          CAPI represents the core Cluster API component and references the Cluster API template.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>kcm</b></td>
        <td>object</td>
        <td>
          KCM represents the core KCM component and references the KCM template.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### Region.spec.core.capi



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


### Region.spec.core.kcm



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


### Region.spec.kubeConfig



KubeConfig references the Secret containing the kubeconfig
of the cluster being onboarded as a regional cluster.
The Secret must reside in the system namespace.

<table>
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
          Name of the Secret.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>key</b></td>
        <td>string</td>
        <td>
          Key in the Secret, when not specified an implementation-specific default key is used.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### Region.spec.providers[index]





<table>
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


### Region.status



RegionStatus defines the observed state of Region

<table>
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
        <td><b>components</b></td>
        <td>map[string]object</td>
        <td>
          Components indicates the status of installed KCM components and CAPI providers.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>conditions</b></td>
        <td>[]object</td>
        <td>
          Conditions represents the observations of a Region's current state.<br/>
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


### Region.status.components[key]



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


### Region.status.conditions[index]



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

## Release






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
        <td><b>spec</b></td>
        <td>object</td>
        <td>
          ReleaseSpec defines the desired state of Release<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>status</b></td>
        <td>object</td>
        <td>
          ReleaseStatus defines the observed state of Release<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### Release.spec



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
        <td><b>capi</b></td>
        <td>object</td>
        <td>
          CAPI references the Cluster API template.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>kcm</b></td>
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
        <td><b>providers</b></td>
        <td>[]object</td>
        <td>
          Providers contains a list of Providers associated with the Release.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>regional</b></td>
        <td>object</td>
        <td>
          Regional references the KCM regional template.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### Release.spec.capi



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





<table>
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


### Release.spec.regional



Regional references the KCM regional template.

<table>
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


### Release.status



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
        <td><b>conditions</b></td>
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

## ServiceSet






ServiceSet is the Schema for the servicesets API

<table>
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
      <td>ServiceSet</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b>spec</b></td>
        <td>object</td>
        <td>
          ServiceSetSpec defines the desired state of ServiceSet<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>status</b></td>
        <td>object</td>
        <td>
          ServiceSetStatus defines the observed state of ServiceSet<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceSet.spec



ServiceSetSpec defines the desired state of ServiceSet

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>cluster</b></td>
        <td>string</td>
        <td>
          Cluster is the name of the ClusterDeployment<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>object</td>
        <td>
          Provider is the definition of the provider to use to deploy services defined in the ServiceSet.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>multiClusterService</b></td>
        <td>string</td>
        <td>
          MultiClusterService is the name of the MultiClusterService<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>services</b></td>
        <td>[]object</td>
        <td>
          Services is the list of services to deploy.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceSet.spec.provider



Provider is the definition of the provider to use to deploy services defined in the ServiceSet.

<table>
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
          Config is the provider-specific configuration applied to the produced objects.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name is the name of the [StateManagementProvider] object.<br/>
          <br/>
            <i>Validations</i>:<li>oldSelf == '' || self == oldSelf: Provider name is immutable once set</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>selfManagement</b></td>
        <td>boolean</td>
        <td>
          SelfManagement flag defines whether resources must be deployed to the management cluster itself.
This field is ignored if set for ClusterDeployment.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceSet.spec.services[index]





<table>
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
          Name is the name of the service. If the ServiceTemplate is backed by Helm chart,
then the name is the name of the Helm release.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace is the namespace where the service is deployed. If the ServiceTemplate
is backed by Helm chart, then the namespace is the namespace where the Helm release is deployed.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>template</b></td>
        <td>string</td>
        <td>
          Template is the name of the ServiceTemplate to use to deploy the service.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>helmOptions</b></td>
        <td>object</td>
        <td>
          HelmOptions are the options to be passed to the provider for helm installation or updates<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>values</b></td>
        <td>string</td>
        <td>
          Values is the values to pass to the ServiceTemplate.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>valuesFrom</b></td>
        <td>[]object</td>
        <td>
          ValuesFrom is the list of sources of the values to pass to the ServiceTemplate.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>version</b></td>
        <td>string</td>
        <td>
          Version is the version of the service.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceSet.spec.services[index].helmOptions



HelmOptions are the options to be passed to the provider for helm installation or updates

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>atomic</b></td>
        <td>boolean</td>
        <td>
          if set, the installation process deletes the installation/upgrades on failure.
The --wait flag will be set automatically if --atomic is used<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>createNamespace</b></td>
        <td>boolean</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>dependencyUpdate</b></td>
        <td>boolean</td>
        <td>
          update dependencies if they are missing before installing the chart<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>description</b></td>
        <td>string</td>
        <td>
          Description is the description of an helm operation<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>disableHooks</b></td>
        <td>boolean</td>
        <td>
          prevent hooks from running during install/upgrade/uninstall<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>disableOpenAPIValidation</b></td>
        <td>boolean</td>
        <td>
          if set, the installation process will not validate rendered templates against the Kubernetes OpenAPI Schema<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>enableClientCache</b></td>
        <td>boolean</td>
        <td>
          EnableClientCache is a flag to enable Helm client cache. If it is not specified, it will be set to false.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>labels</b></td>
        <td>map[string]string</td>
        <td>
          Labels that would be added to release metadata.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>replace</b></td>
        <td>boolean</td>
        <td>
          Replaces if set indicates to replace an older release with this one<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>skipCRDs</b></td>
        <td>boolean</td>
        <td>
          SkipCRDs controls whether CRDs should be installed during install/upgrade operation.
By default, CRDs are installed if not already present.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>skipSchemaValidation</b></td>
        <td>boolean</td>
        <td>
          SkipSchemaValidation determines if JSON schema validation is disabled.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>timeout</b></td>
        <td>string</td>
        <td>
          time to wait for any individual Kubernetes operation (like Jobs for hooks) (default 5m0s)<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>wait</b></td>
        <td>boolean</td>
        <td>
          if set, will wait until all Pods, PVCs, Services, and minimum number of Pods of a Deployment, StatefulSet, or ReplicaSet
are in a ready state before marking the release as successful. It will wait for as long as --timeout<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>waitForJobs</b></td>
        <td>boolean</td>
        <td>
          if set and --wait enabled, will wait until all Jobs have been completed before marking the release as successful.
It will wait for as long as --timeout<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceSet.spec.services[index].valuesFrom[index]



ValuesFrom is the source of the values to pass to the ServiceTemplate. The source
can be a ConfigMap or a Secret located in the same namespace as the ServiceSet.

<table>
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
          Kind is the kind of the source.<br/>
          <br/>
            <i>Enum</i>: ConfigMap, Secret<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name is the name of the source.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceSet.status



ServiceSetStatus defines the observed state of ServiceSet

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>deployed</b></td>
        <td>boolean</td>
        <td>
          Deployed is true if the ServiceSet has been deployed<br/>
          <br/>
            <i>Default</i>: false<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>cluster</b></td>
        <td>object</td>
        <td>
          Cluster contains [k8s.io/api/core/v1.ObjectReference] to the cluster object.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>conditions</b></td>
        <td>[]object</td>
        <td>
          Conditions is a list of conditions for the ServiceSet<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>provider</b></td>
        <td>object</td>
        <td>
          Provider is the state of the provider<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>services</b></td>
        <td>[]object</td>
        <td>
          Services is a list of Service states in the ServiceSet<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceSet.status.cluster



Cluster contains [k8s.io/api/core/v1.ObjectReference] to the cluster object.

<table>
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


### ServiceSet.status.conditions[index]



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


### ServiceSet.status.provider



Provider is the state of the provider

<table>
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
          Ready is true if the provider is ready<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>suspended</b></td>
        <td>boolean</td>
        <td>
          Suspended is true if the provider is suspended<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceSet.status.services[index]



ServiceState is the state of a Service

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>lastStateTransitionTime</b></td>
        <td>string</td>
        <td>
          LastStateTransitionTime is the time the State was last transitioned<br/>
          <br/>
            <i>Format</i>: date-time<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name is the name of the Service<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace is the namespace of the Service<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>state</b></td>
        <td>enum</td>
        <td>
          State is the state of the Service<br/>
          <br/>
            <i>Enum</i>: Deployed, Provisioning, Failed, Pending, Deleting<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>template</b></td>
        <td>string</td>
        <td>
          Template is the name of the ServiceTemplate used to deploy the Service<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>type</b></td>
        <td>enum</td>
        <td>
          Type is the type of the deployment method for the Service<br/>
          <br/>
            <i>Enum</i>: Helm, Kustomize, Resource<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>conditions</b></td>
        <td>[]object</td>
        <td>
          Conditions is a list of conditions for the Service<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>failureMessage</b></td>
        <td>string</td>
        <td>
          FailureMessage is the reason why the Service failed to deploy<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>version</b></td>
        <td>string</td>
        <td>
          Version is the version of the Service<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceSet.status.services[index].conditions[index]



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
        <td><b>spec</b></td>
        <td>object</td>
        <td>
          TemplateChainSpec defines the desired state of *TemplateChain<br/>
          <br/>
            <i>Validations</i>:<li>self == oldSelf: Spec is immutable</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>status</b></td>
        <td>object</td>
        <td>
          TemplateChainStatus defines the observed state of *TemplateChain<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplateChain.spec



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
        <td><b>supportedTemplates</b></td>
        <td>[]object</td>
        <td>
          SupportedTemplates is the list of supported Templates definitions and all available upgrade sequences for it.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplateChain.spec.supportedTemplates[index]



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
        <td><b>availableUpgrades</b></td>
        <td>[]object</td>
        <td>
          AvailableUpgrades is the list of available upgrades for the specified Template.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplateChain.spec.supportedTemplates[index].availableUpgrades[index]



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
      </tr><tr>
        <td><b>version</b></td>
        <td>string</td>
        <td>
          Version is the version of the Template to which the upgrade is available.<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### ServiceTemplateChain.status



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
        <td><b>spec</b></td>
        <td>object</td>
        <td>
          ServiceTemplateSpec defines the desired state of ServiceTemplate<br/>
          <br/>
            <i>Validations</i>:<li>self == oldSelf: Spec is immutable</li><li>has(self.helm) ? (!has(self.kustomize) && !has(self.resources)): true: Helm, Kustomize and Resources are mutually exclusive.</li><li>has(self.kustomize) ? (!has(self.helm) && !has(self.resources)): true: Helm, Kustomize and Resources are mutually exclusive.</li><li>has(self.resources) ? (!has(self.kustomize) && !has(self.helm)): true: Helm, Kustomize and Resources are mutually exclusive.</li><li>has(self.helm) || has(self.kustomize) || has(self.resources): One of Helm, Kustomize, or Resources must be specified.</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>status</b></td>
        <td>object</td>
        <td>
          ServiceTemplateStatus defines the observed state of ServiceTemplate<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec



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
        <td><b>helm</b></td>
        <td>object</td>
        <td>
          Helm contains the Helm chart information for the template.<br/>
          <br/>
            <i>Validations</i>:<li>(has(self.chartSpec) ? (!has(self.chartSource) && !has(self.chartRef)): true): chartSpec, chartSource and chartRef are mutually exclusive</li><li>(has(self.chartSource) ? (!has(self.chartSpec) && !has(self.chartRef)): true): chartSpec, chartSource and chartRef are mutually exclusive</li><li>(has(self.chartRef) ? (!has(self.chartSpec) && !has(self.chartSource)): true): chartSpec, chartSource and chartRef are mutually exclusive</li><li>has(self.chartSpec) || has(self.chartRef) || has(self.chartSource): one of chartSpec, chartRef or chartSource must be set</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>helmOptions</b></td>
        <td>object</td>
        <td>
          HelmOptions are the global options to use when installing or updating the helm chart.<br/>
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
        <td><b>kustomize</b></td>
        <td>object</td>
        <td>
          Kustomize contains the Kustomize configuration for the template.<br/>
          <br/>
            <i>Validations</i>:<li>has(self.localSourceRef) ? !has(self.remoteSourceSpec): true: LocalSource and RemoteSource are mutually exclusive.</li><li>has(self.remoteSourceSpec) ? !has(self.localSourceRef): true: LocalSource and RemoteSource are mutually exclusive.</li><li>has(self.localSourceRef) || has(self.remoteSourceSpec): One of LocalSource or RemoteSource must be specified.</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>resources</b></td>
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
        <td><b>chartRef</b></td>
        <td>object</td>
        <td>
          ChartRef is a reference to a source controller resource containing the
Helm chart representing the template.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>chartSource</b></td>
        <td>object</td>
        <td>
          ChartSource is a source of a Helm chart representing the template.<br/>
          <br/>
            <i>Validations</i>:<li>has(self.localSourceRef) ? (self.localSourceRef.kind != 'Secret' && self.localSourceRef.kind != 'ConfigMap'): true: Secret and ConfigMap are not supported as Helm chart sources</li><li>has(self.localSourceRef) ? !has(self.remoteSourceSpec): true: LocalSource and RemoteSource are mutually exclusive.</li><li>has(self.remoteSourceSpec) ? !has(self.localSourceRef): true: LocalSource and RemoteSource are mutually exclusive.</li><li>has(self.localSourceRef) || has(self.remoteSourceSpec): One of LocalSource or RemoteSource must be specified.</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>chartSpec</b></td>
        <td>object</td>
        <td>
          ChartSpec defines the desired state of the HelmChart to be created by the controller<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartRef



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
            <i>Enum</i>: OCIRepository, HelmChart, ExternalArtifact<br/>
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
        <td><b>localSourceRef</b></td>
        <td>object</td>
        <td>
          LocalSourceRef is the local source of the kustomize manifest.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>remoteSourceSpec</b></td>
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
[github.com/fluxcd/source-controller/api/v1.Bucket] or [github.com/fluxcd/source-controller/api/v1.OCIRepository].
If the Kind is ConfigMap or Secret, the namespace will be ignored.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec



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
        <td><b>bucket</b></td>
        <td>object</td>
        <td>
          Bucket is the definition of bucket source.<br/>
          <br/>
            <i>Validations</i>:<li>self.provider == 'aws' || self.provider == 'generic' || !has(self.sts): STS configuration is only supported for the 'aws' and 'generic' Bucket providers</li><li>self.provider != 'aws' || !has(self.sts) || self.sts.provider == 'aws': 'aws' is the only supported STS provider for the 'aws' Bucket provider</li><li>self.provider != 'generic' || !has(self.sts) || self.sts.provider == 'ldap': 'ldap' is the only supported STS provider for the 'generic' Bucket provider</li><li>!has(self.sts) || self.sts.provider != 'aws' || !has(self.sts.secretRef): spec.sts.secretRef is not required for the 'aws' STS provider</li><li>!has(self.sts) || self.sts.provider != 'aws' || !has(self.sts.certSecretRef): spec.sts.certSecretRef is not required for the 'aws' STS provider</li><li>self.provider != 'generic' || !has(self.serviceAccountName): ServiceAccountName is not supported for the 'generic' Bucket provider</li><li>!has(self.secretRef) || !has(self.serviceAccountName): cannot set both .spec.secretRef and .spec.serviceAccountName</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>git</b></td>
        <td>object</td>
        <td>
          Git is the definition of git repository source.<br/>
          <br/>
            <i>Validations</i>:<li>!has(self.serviceAccountName) || (has(self.provider) && self.provider == 'azure'): serviceAccountName can only be set when provider is 'azure'</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>oci</b></td>
        <td>object</td>
        <td>
          OCI is the definition of OCI repository source.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.bucket



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
        <td><b>certSecretRef</b></td>
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
        <td><b>proxySecretRef</b></td>
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
        <td><b>secretRef</b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing authentication credentials
for the Bucket.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>serviceAccountName</b></td>
        <td>string</td>
        <td>
          ServiceAccountName is the name of the Kubernetes ServiceAccount used to authenticate
the bucket. This field is only supported for the 'gcp' and 'aws' providers.
For more information about workload identity:
https://fluxcd.io/flux/components/source/buckets/#workload-identity<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>sts</b></td>
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
        <td><b>certSecretRef</b></td>
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
        <td><b>secretRef</b></td>
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
        <td><b>include</b></td>
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
        <td><b>proxySecretRef</b></td>
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
        <td><b>ref</b></td>
        <td>object</td>
        <td>
          Reference specifies the Git reference to resolve and monitor for
changes, defaults to the 'master' branch.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>secretRef</b></td>
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
        <td><b>serviceAccountName</b></td>
        <td>string</td>
        <td>
          ServiceAccountName is the name of the Kubernetes ServiceAccount used to
authenticate to the GitRepository. This field is only supported for 'azure' provider.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>sparseCheckout</b></td>
        <td>[]string</td>
        <td>
          SparseCheckout specifies a list of directories to checkout when cloning
the repository. If specified, only these directories are included in the
Artifact produced for this GitRepository.<br/>
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
        <td><b>verify</b></td>
        <td>object</td>
        <td>
          Verification specifies the configuration to verify the Git commit
signature(s).<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.git.include[index]



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
        <td><b>repository</b></td>
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
        <td><b>secretRef</b></td>
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
        <td><b>certSecretRef</b></td>
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
be of type `Opaque` or `kubernetes.io/tls`.<br/>
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
        <td><b>layerSelector</b></td>
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
        <td><b>proxySecretRef</b></td>
        <td>object</td>
        <td>
          ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the container registry.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>ref</b></td>
        <td>object</td>
        <td>
          The OCI reference to pull and monitor for changes,
defaults to the latest tag.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>secretRef</b></td>
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
        <td><b>verify</b></td>
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

<table>
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
        <td><b>matchOIDCIdentity</b></td>
        <td>[]object</td>
        <td>
          MatchOIDCIdentity specifies the identity matching criteria to use
while verifying an OCI artifact which was signed using Cosign keyless
signing. The artifact's identity is deemed to be verified if any of the
specified matchers match against the identity.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>secretRef</b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Kubernetes Secret containing the
trusted public keys.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSource.remoteSourceSpec.oci.verify.matchOIDCIdentity[index]



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
        <td><b>sourceRef</b></td>
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
        <td><b>verify</b></td>
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
        <td><b>matchOIDCIdentity</b></td>
        <td>[]object</td>
        <td>
          MatchOIDCIdentity specifies the identity matching criteria to use
while verifying an OCI artifact which was signed using Cosign keyless
signing. The artifact's identity is deemed to be verified if any of the
specified matchers match against the identity.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>secretRef</b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Kubernetes Secret containing the
trusted public keys.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.helm.chartSpec.verify.matchOIDCIdentity[index]



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


### ServiceTemplate.spec.helmOptions



HelmOptions are the global options to use when installing or updating the helm chart.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>atomic</b></td>
        <td>boolean</td>
        <td>
          if set, the installation process deletes the installation/upgrades on failure.
The --wait flag will be set automatically if --atomic is used<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>createNamespace</b></td>
        <td>boolean</td>
        <td>
          <br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>dependencyUpdate</b></td>
        <td>boolean</td>
        <td>
          update dependencies if they are missing before installing the chart<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>description</b></td>
        <td>string</td>
        <td>
          Description is the description of an helm operation<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>disableHooks</b></td>
        <td>boolean</td>
        <td>
          prevent hooks from running during install/upgrade/uninstall<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>disableOpenAPIValidation</b></td>
        <td>boolean</td>
        <td>
          if set, the installation process will not validate rendered templates against the Kubernetes OpenAPI Schema<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>enableClientCache</b></td>
        <td>boolean</td>
        <td>
          EnableClientCache is a flag to enable Helm client cache. If it is not specified, it will be set to false.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>labels</b></td>
        <td>map[string]string</td>
        <td>
          Labels that would be added to release metadata.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>replace</b></td>
        <td>boolean</td>
        <td>
          Replaces if set indicates to replace an older release with this one<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>skipCRDs</b></td>
        <td>boolean</td>
        <td>
          SkipCRDs controls whether CRDs should be installed during install/upgrade operation.
By default, CRDs are installed if not already present.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>skipSchemaValidation</b></td>
        <td>boolean</td>
        <td>
          SkipSchemaValidation determines if JSON schema validation is disabled.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>timeout</b></td>
        <td>string</td>
        <td>
          time to wait for any individual Kubernetes operation (like Jobs for hooks) (default 5m0s)<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>wait</b></td>
        <td>boolean</td>
        <td>
          if set, will wait until all Pods, PVCs, Services, and minimum number of Pods of a Deployment, StatefulSet, or ReplicaSet
are in a ready state before marking the release as successful. It will wait for as long as --timeout<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>waitForJobs</b></td>
        <td>boolean</td>
        <td>
          if set and --wait enabled, will wait until all Jobs have been completed before marking the release as successful.
It will wait for as long as --timeout<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize



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
        <td><b>localSourceRef</b></td>
        <td>object</td>
        <td>
          LocalSourceRef is the local source of the kustomize manifest.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>remoteSourceSpec</b></td>
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
[github.com/fluxcd/source-controller/api/v1.Bucket] or [github.com/fluxcd/source-controller/api/v1.OCIRepository].
If the Kind is ConfigMap or Secret, the namespace will be ignored.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec



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
        <td><b>bucket</b></td>
        <td>object</td>
        <td>
          Bucket is the definition of bucket source.<br/>
          <br/>
            <i>Validations</i>:<li>self.provider == 'aws' || self.provider == 'generic' || !has(self.sts): STS configuration is only supported for the 'aws' and 'generic' Bucket providers</li><li>self.provider != 'aws' || !has(self.sts) || self.sts.provider == 'aws': 'aws' is the only supported STS provider for the 'aws' Bucket provider</li><li>self.provider != 'generic' || !has(self.sts) || self.sts.provider == 'ldap': 'ldap' is the only supported STS provider for the 'generic' Bucket provider</li><li>!has(self.sts) || self.sts.provider != 'aws' || !has(self.sts.secretRef): spec.sts.secretRef is not required for the 'aws' STS provider</li><li>!has(self.sts) || self.sts.provider != 'aws' || !has(self.sts.certSecretRef): spec.sts.certSecretRef is not required for the 'aws' STS provider</li><li>self.provider != 'generic' || !has(self.serviceAccountName): ServiceAccountName is not supported for the 'generic' Bucket provider</li><li>!has(self.secretRef) || !has(self.serviceAccountName): cannot set both .spec.secretRef and .spec.serviceAccountName</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>git</b></td>
        <td>object</td>
        <td>
          Git is the definition of git repository source.<br/>
          <br/>
            <i>Validations</i>:<li>!has(self.serviceAccountName) || (has(self.provider) && self.provider == 'azure'): serviceAccountName can only be set when provider is 'azure'</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>oci</b></td>
        <td>object</td>
        <td>
          OCI is the definition of OCI repository source.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.bucket



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
        <td><b>certSecretRef</b></td>
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
        <td><b>proxySecretRef</b></td>
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
        <td><b>secretRef</b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing authentication credentials
for the Bucket.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>serviceAccountName</b></td>
        <td>string</td>
        <td>
          ServiceAccountName is the name of the Kubernetes ServiceAccount used to authenticate
the bucket. This field is only supported for the 'gcp' and 'aws' providers.
For more information about workload identity:
https://fluxcd.io/flux/components/source/buckets/#workload-identity<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>sts</b></td>
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
        <td><b>certSecretRef</b></td>
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
        <td><b>secretRef</b></td>
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
        <td><b>include</b></td>
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
        <td><b>proxySecretRef</b></td>
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
        <td><b>ref</b></td>
        <td>object</td>
        <td>
          Reference specifies the Git reference to resolve and monitor for
changes, defaults to the 'master' branch.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>secretRef</b></td>
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
        <td><b>serviceAccountName</b></td>
        <td>string</td>
        <td>
          ServiceAccountName is the name of the Kubernetes ServiceAccount used to
authenticate to the GitRepository. This field is only supported for 'azure' provider.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>sparseCheckout</b></td>
        <td>[]string</td>
        <td>
          SparseCheckout specifies a list of directories to checkout when cloning
the repository. If specified, only these directories are included in the
Artifact produced for this GitRepository.<br/>
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
        <td><b>verify</b></td>
        <td>object</td>
        <td>
          Verification specifies the configuration to verify the Git commit
signature(s).<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.git.include[index]



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
        <td><b>repository</b></td>
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
        <td><b>secretRef</b></td>
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
        <td><b>certSecretRef</b></td>
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
be of type `Opaque` or `kubernetes.io/tls`.<br/>
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
        <td><b>layerSelector</b></td>
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
        <td><b>proxySecretRef</b></td>
        <td>object</td>
        <td>
          ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the container registry.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>ref</b></td>
        <td>object</td>
        <td>
          The OCI reference to pull and monitor for changes,
defaults to the latest tag.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>secretRef</b></td>
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
        <td><b>verify</b></td>
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

<table>
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
        <td><b>matchOIDCIdentity</b></td>
        <td>[]object</td>
        <td>
          MatchOIDCIdentity specifies the identity matching criteria to use
while verifying an OCI artifact which was signed using Cosign keyless
signing. The artifact's identity is deemed to be verified if any of the
specified matchers match against the identity.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>secretRef</b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Kubernetes Secret containing the
trusted public keys.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.kustomize.remoteSourceSpec.oci.verify.matchOIDCIdentity[index]



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
        <td><b>localSourceRef</b></td>
        <td>object</td>
        <td>
          LocalSourceRef is the local source of the kustomize manifest.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>remoteSourceSpec</b></td>
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
[github.com/fluxcd/source-controller/api/v1.Bucket] or [github.com/fluxcd/source-controller/api/v1.OCIRepository].
If the Kind is ConfigMap or Secret, the namespace will be ignored.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec



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
        <td><b>bucket</b></td>
        <td>object</td>
        <td>
          Bucket is the definition of bucket source.<br/>
          <br/>
            <i>Validations</i>:<li>self.provider == 'aws' || self.provider == 'generic' || !has(self.sts): STS configuration is only supported for the 'aws' and 'generic' Bucket providers</li><li>self.provider != 'aws' || !has(self.sts) || self.sts.provider == 'aws': 'aws' is the only supported STS provider for the 'aws' Bucket provider</li><li>self.provider != 'generic' || !has(self.sts) || self.sts.provider == 'ldap': 'ldap' is the only supported STS provider for the 'generic' Bucket provider</li><li>!has(self.sts) || self.sts.provider != 'aws' || !has(self.sts.secretRef): spec.sts.secretRef is not required for the 'aws' STS provider</li><li>!has(self.sts) || self.sts.provider != 'aws' || !has(self.sts.certSecretRef): spec.sts.certSecretRef is not required for the 'aws' STS provider</li><li>self.provider != 'generic' || !has(self.serviceAccountName): ServiceAccountName is not supported for the 'generic' Bucket provider</li><li>!has(self.secretRef) || !has(self.serviceAccountName): cannot set both .spec.secretRef and .spec.serviceAccountName</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>git</b></td>
        <td>object</td>
        <td>
          Git is the definition of git repository source.<br/>
          <br/>
            <i>Validations</i>:<li>!has(self.serviceAccountName) || (has(self.provider) && self.provider == 'azure'): serviceAccountName can only be set when provider is 'azure'</li>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>oci</b></td>
        <td>object</td>
        <td>
          OCI is the definition of OCI repository source.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.bucket



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
        <td><b>certSecretRef</b></td>
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
        <td><b>proxySecretRef</b></td>
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
        <td><b>secretRef</b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Secret containing authentication credentials
for the Bucket.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>serviceAccountName</b></td>
        <td>string</td>
        <td>
          ServiceAccountName is the name of the Kubernetes ServiceAccount used to authenticate
the bucket. This field is only supported for the 'gcp' and 'aws' providers.
For more information about workload identity:
https://fluxcd.io/flux/components/source/buckets/#workload-identity<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>sts</b></td>
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
        <td><b>certSecretRef</b></td>
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
        <td><b>secretRef</b></td>
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
        <td><b>include</b></td>
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
        <td><b>proxySecretRef</b></td>
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
        <td><b>ref</b></td>
        <td>object</td>
        <td>
          Reference specifies the Git reference to resolve and monitor for
changes, defaults to the 'master' branch.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>secretRef</b></td>
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
        <td><b>serviceAccountName</b></td>
        <td>string</td>
        <td>
          ServiceAccountName is the name of the Kubernetes ServiceAccount used to
authenticate to the GitRepository. This field is only supported for 'azure' provider.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>sparseCheckout</b></td>
        <td>[]string</td>
        <td>
          SparseCheckout specifies a list of directories to checkout when cloning
the repository. If specified, only these directories are included in the
Artifact produced for this GitRepository.<br/>
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
        <td><b>verify</b></td>
        <td>object</td>
        <td>
          Verification specifies the configuration to verify the Git commit
signature(s).<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.git.include[index]



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
        <td><b>repository</b></td>
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
        <td><b>secretRef</b></td>
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
        <td><b>certSecretRef</b></td>
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
be of type `Opaque` or `kubernetes.io/tls`.<br/>
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
        <td><b>layerSelector</b></td>
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
        <td><b>proxySecretRef</b></td>
        <td>object</td>
        <td>
          ProxySecretRef specifies the Secret containing the proxy configuration
to use while communicating with the container registry.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>ref</b></td>
        <td>object</td>
        <td>
          The OCI reference to pull and monitor for changes,
defaults to the latest tag.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>secretRef</b></td>
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
        <td><b>verify</b></td>
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

<table>
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
        <td><b>matchOIDCIdentity</b></td>
        <td>[]object</td>
        <td>
          MatchOIDCIdentity specifies the identity matching criteria to use
while verifying an OCI artifact which was signed using Cosign keyless
signing. The artifact's identity is deemed to be verified if any of the
specified matchers match against the identity.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>secretRef</b></td>
        <td>object</td>
        <td>
          SecretRef specifies the Kubernetes Secret containing the
trusted public keys.<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### ServiceTemplate.spec.resources.remoteSourceSpec.oci.verify.matchOIDCIdentity[index]



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
        <td><b>chartRef</b></td>
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
        <td><b>schemaConfigMapName</b></td>
        <td>string</td>
        <td>
          SchemaConfigMapName specifies the name of the ConfigMap that contains the JSON Schema definition for Helm Chart validation.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>sourceStatus</b></td>
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
            <i>Enum</i>: OCIRepository, HelmChart, ExternalArtifact<br/>
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
        <td><b>artifact</b></td>
        <td>object</td>
        <td>
          Artifact is the artifact that was generated from the template source.<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>conditions</b></td>
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
        <td><b>digest</b></td>
        <td>string</td>
        <td>
          Digest is the digest of the file in the form of '<algorithm>:<checksum>'.<br/>
        </td>
        <td>true</td>
      </tr><tr>
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

## StateManagementProvider






StateManagementProvider is the Schema for the statemanagementproviders API

<table>
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
      <td>StateManagementProvider</td>
      <td>true</td>
      </tr>
      <tr>
      <td><b><a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.27/#objectmeta-v1-meta">metadata</a></b></td>
      <td>object</td>
      <td>Refer to the Kubernetes API documentation for the fields of the `metadata` field.</td>
      <td>true</td>
      </tr><tr>
        <td><b>spec</b></td>
        <td>object</td>
        <td>
          StateManagementProviderSpec defines the desired state of StateManagementProvider<br/>
        </td>
        <td>false</td>
      </tr><tr>
        <td><b>status</b></td>
        <td>object</td>
        <td>
          StateManagementProviderStatus defines the observed state of StateManagementProvider<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### StateManagementProvider.spec



StateManagementProviderSpec defines the desired state of StateManagementProvider

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>adapter</b></td>
        <td>object</td>
        <td>
          Adapter is an operator with translates the k0rdent API objects into provider-specific API objects.
It is represented as a reference to operator object<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>provisioner</b></td>
        <td>[]object</td>
        <td>
          Provisioner is a set of resources required for the provider to operate. These resources
reconcile provider-specific API objects. It is represented as a list of references to
provider's objects<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>provisionerCRDs</b></td>
        <td>[]object</td>
        <td>
          ProvisionerCRDs is a set of references to provider-specific CustomResourceDefinition objects,
which are required for the provider to operate.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>selector</b></td>
        <td>object</td>
        <td>
          Selector is label selector to be used to filter the [ServiceSet] objects to be reconciled.<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>suspend</b></td>
        <td>boolean</td>
        <td>
          Suspend suspends the StateManagementProvider. Suspending a StateManagementProvider
will prevent the adapter from reconciling any resources.<br/>
          <br/>
            <i>Default</i>: false<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### StateManagementProvider.spec.adapter



Adapter is an operator with translates the k0rdent API objects into provider-specific API objects.
It is represented as a reference to operator object

<table>
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
          APIVersion is the API version of the resource<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>kind</b></td>
        <td>string</td>
        <td>
          Kind is the kind of the resource<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name is the name of the resource<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace is the namespace of the resource<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>readinessRule</b></td>
        <td>string</td>
        <td>
          ReadinessRule is a CEL expression that evaluates to true when the resource is ready<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### StateManagementProvider.spec.provisioner[index]



ResourceReference is a cross-namespace reference to a resource

<table>
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
          APIVersion is the API version of the resource<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>kind</b></td>
        <td>string</td>
        <td>
          Kind is the kind of the resource<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>name</b></td>
        <td>string</td>
        <td>
          Name is the name of the resource<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>namespace</b></td>
        <td>string</td>
        <td>
          Namespace is the namespace of the resource<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>readinessRule</b></td>
        <td>string</td>
        <td>
          ReadinessRule is a CEL expression that evaluates to true when the resource is ready<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### StateManagementProvider.spec.provisionerCRDs[index]



ProvisionerCRD is a GVRs for a custom resource reconciled by provisioners

<table>
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
          Group is the API group of the resources<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>resources</b></td>
        <td>[]string</td>
        <td>
          Resources is the list of resources under given APIVersion<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>version</b></td>
        <td>string</td>
        <td>
          Version is the API version of the resources<br/>
        </td>
        <td>true</td>
      </tr></tbody>
</table>


### StateManagementProvider.spec.selector



Selector is label selector to be used to filter the [ServiceSet] objects to be reconciled.

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Description</th>
            <th>Required</th>
        </tr>
    </thead>
    <tbody><tr>
        <td><b>matchExpressions</b></td>
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


### StateManagementProvider.spec.selector.matchExpressions[index]



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


### StateManagementProvider.status



StateManagementProviderStatus defines the observed state of StateManagementProvider

<table>
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
          Ready is true if the state management provider is valid<br/>
        </td>
        <td>true</td>
      </tr><tr>
        <td><b>conditions</b></td>
        <td>[]object</td>
        <td>
          Conditions is a list of conditions for the state management provider<br/>
        </td>
        <td>false</td>
      </tr></tbody>
</table>


### StateManagementProvider.status.conditions[index]



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
