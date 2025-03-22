# OpenID Connect (OIDC)

OpenID Connect (OIDC) is an identity layer built on top of the OAuth 2.0 authorization framework. It streamlines the authentication process by enabling applications to verify a user's identity and retrieve essential profile information in a standardized and secure manner. {{{ docsVersionInfo.k0rdentName}}} integrates with multiple OIDC providers.

## Core Concepts and Components

OIDC enables {{{ docsVersionInfo.k0rdentName}}} to provide a standardized way to handle authentication. 

- **Authentication vs. Authorization:**  
 It's easy to conflate authetication and authorization, but while they are related, they are not the same. Authentication establishes the identity of an individual or application, while authorization defines what that identity has permission to do.  While OAuth 2.0 is focused on authorization, granting applications access to resources, OIDC specifically addresses the authentication piece of the puzzle. It enables applications to confirm that a user is who they claim to be before allowing access.

- **ID Tokens and JWTs:**  
  At the heart of OIDC is the ID token, a JSON Web Token (JWT) that carries critical information (claims) about the user, such as a unique identifier, name, email, and the token’s expiration. These tokens are digitally signed (often with RS256), which means they can be validated by any service that has access to the public key, eliminating the need for constant re-validation of credentials.

- **Discovery and Dynamic Configuration:**  
  OIDC features a discovery mechanism via the `/.well-known/openid-configuration` endpoint. This endpoint automatically provides metadata about the identity provider, including available authentication endpoints, supported scopes, and the necessary public keys for token verification. This simplifies setup and integration, reducing the need for manual configuration.

- **Scopes and Claims:**  
  The protocol defines standard scopes—such as `openid`, `profile`, and `email`—that specify what user data the client wishes to access. In response, the ID token will include corresponding claims, delivering verified user information in a secure and structured format. Custom scopes and claims can also be configured to meet specific application needs.

- **Flexible Authentication Flows:**  
  OIDC supports multiple flows tailored to different application types:
  - **Authorization Code Flow:** Ideal for server-side applications, where the client exchanges an authorization code for tokens in a secure manner.
  - **Implicit Flow:** Suited for single-page or mobile applications, delivering tokens directly through the browser or app interface.
  - **Hybrid Flow:** Combines elements of both the authorization code and implicit flows, balancing security and performance.

## OIDC in the Context of Kubernetes

Integrating OIDC with Kubernetes enables the cluster to delegate authentication to an external identity provider. Here’s how it works:

- **Delegated Authentication:**  
  The Kubernetes API server is configured with OIDC parameters (like `--oidc-issuer-url` and `--oidc-client-id`). (In the context of {{{ docsVersionInfo.k0rdentName}}} these are configured with templates.) When a user makes a request (for example, via `kubectl`), the API server validates the accompanying OIDC token by checking its signature, issuer, and expiration date. This offloads the responsibility of authentication to a trusted external provider.

- **User Identity and RBAC:**  
  Upon successful token validation, Kubernetes extracts user details (such as username or group memberships) from the token’s claims. These details are then used to enforce Role-Based Access Control (RBAC) policies, ensuring  users have the proper permissions to access resources within the cluster.

- **Simplified and Centralized User Management:**  
  By integrating with a centralized OIDC provider, Kubernetes can manage user identities and access rights more efficiently across multiple clusters. This not only enhances security but also streamlines administrative tasks.

## OIDC in {{{ docsVersionInfo.k0rdentName}}}

{{{ docsVersionInfo.k0rdentName}}} supports multiple OIDC providers to accommodate various organizational needs. These options are:

- [Okta](okta.md)
- [Entra-ID](entra-id.md)
