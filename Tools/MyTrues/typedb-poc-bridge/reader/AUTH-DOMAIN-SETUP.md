# MyTrues Reader — domain + GitHub OAuth handoff

## Current Azure Reader

- Container App: `mytrues-reader`
- Generated URL: `https://mytrues-reader.ambitioushill-c7dc3aef.brazilsouth.azurecontainerapps.io/`
- Environment: `mytrues-memory-env`
- Desired public URL: `https://mytrues.io/`

## Cloudflare DNS

The apex `mytrues.io` is hosted by Cloudflare.

Create these records with **Proxy status = DNS only** while Azure issues/renews the managed certificate:

- Type: `A`
  - Name: `@`
  - Value: `20.197.204.102`

- Type: `TXT`
  - Name: `asuid`
  - Value: `0932A75FCFE80964E218D9938962D94B83467900842010A4F491B7007C6D091F`

No CAA record is currently published. If a CAA record is introduced later, it must allow DigiCert for Azure managed certificate issuance.

## GitHub OAuth App

Create the OAuth App under the GitHub account/organization that should own the login client.

Recommended values:

- Application name: `MyTrues Reader`
- Homepage URL: `https://mytrues.io/`
- Authorization callback URL: `https://mytrues.io/.auth/login/github/callback`

Optional temporary second callback:

`https://mytrues-reader.ambitioushill-c7dc3aef.brazilsouth.azurecontainerapps.io/.auth/login/github/callback`

After registering:

1. copy the Client ID;
2. generate a Client Secret;
3. add these repository secrets to `appLaboware/FlowED`:
   - `GITHUB_OAUTH_CLIENT_ID`
   - `GITHUB_OAUTH_CLIENT_SECRET`

Do not commit or paste the client secret into repository files.

## Automated completion

Workflow:

`.github/workflows/mytrues-reader-domain-auth.yml`

When DNS and the two secrets are ready, it will:

1. bind `mytrues.io` to `mytrues-reader`;
2. request/bind the Azure managed TLS certificate;
3. configure GitHub as the Azure Container Apps authentication provider;
4. redirect anonymous users to GitHub login;
5. require HTTPS;
6. enable token store;
7. verify that `https://mytrues.io/` responds with the GitHub login gate.

Callback contract follows Azure Container Apps GitHub auth:

`https://mytrues.io/.auth/login/github/callback`
