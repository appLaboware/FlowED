#!/usr/bin/env bash
set -euo pipefail

# IDEOS / FlowED Azure bootstrap
#
# Goal:
#   From an authenticated Azure CLI session, converge the Azure side of the
#   GitHub Actions OIDC trust to the desired state without using the portal.
#
# Safe to run repeatedly: every step is existence-checked before mutation.

RESOURCE_GROUP="${RESOURCE_GROUP:-rg-flowed-ideos-lab}"
LOCATION="${LOCATION:-brazilsouth}"

APP_DISPLAY_NAME="${APP_DISPLAY_NAME:-FlowED-GitHub-Actions}"
FEDERATED_CREDENTIAL_NAME="${FEDERATED_CREDENTIAL_NAME:-github-flowed-tools-ideos-lab}"

GITHUB_ORG="${GITHUB_ORG:-appLaboware}"
GITHUB_REPO="${GITHUB_REPO:-FlowED}"
GITHUB_BRANCH="${GITHUB_BRANCH:-tools/ideos-lab}"
GITHUB_REPOSITORY="${GITHUB_ORG}/${GITHUB_REPO}"

CONTRIBUTOR_ROLE_ID="b24988ac-6180-42a0-ab88-20f7382dd24c"
OIDC_ISSUER="https://token.actions.githubusercontent.com"
OIDC_AUDIENCE="api://AzureADTokenExchange"
OIDC_SUBJECT="repo:${GITHUB_REPOSITORY}:ref:refs/heads/${GITHUB_BRANCH}"

say() {
  printf '\n== %s ==\n' "$1"
}

fail() {
  echo "ERROR: $*" >&2
  exit 1
}

command -v az >/dev/null 2>&1 || fail "Azure CLI (az) is required."

say "Azure session"

SUBSCRIPTION_ID="$(az account show --query id -o tsv 2>/dev/null || true)"
TENANT_ID="$(az account show --query tenantId -o tsv 2>/dev/null || true)"
SUBSCRIPTION_NAME="$(az account show --query name -o tsv 2>/dev/null || true)"

[[ -n "$SUBSCRIPTION_ID" ]] || fail "No active Azure subscription. Run 'az login' or use Azure Cloud Shell."
[[ -n "$TENANT_ID" ]] || fail "No tenant was resolved from the active Azure account."

echo "Subscription : $SUBSCRIPTION_NAME"
echo "Subscription ID: $SUBSCRIPTION_ID"
echo "Tenant ID      : $TENANT_ID"

say "Resource group"

if az group show --name "$RESOURCE_GROUP" --subscription "$SUBSCRIPTION_ID" >/dev/null 2>&1; then
  echo "Exists: $RESOURCE_GROUP"
else
  echo "Creating $RESOURCE_GROUP in $LOCATION..."
  az group create     --name "$RESOURCE_GROUP"     --location "$LOCATION"     --subscription "$SUBSCRIPTION_ID"     --output none
fi

say "Microsoft Entra application"

APP_ID="$(
  az ad app list     --display-name "$APP_DISPLAY_NAME"     --query "[?displayName=='$APP_DISPLAY_NAME'].appId | [0]"     -o tsv
)"

if [[ -z "$APP_ID" ]]; then
  echo "Creating app registration: $APP_DISPLAY_NAME"
  APP_ID="$(
    az ad app create       --display-name "$APP_DISPLAY_NAME"       --sign-in-audience AzureADMyOrg       --query appId       -o tsv
  )"
else
  echo "Exists: $APP_DISPLAY_NAME ($APP_ID)"
fi

say "Service principal"

SP_OBJECT_ID="$(az ad sp show --id "$APP_ID" --query id -o tsv 2>/dev/null || true)"

if [[ -z "$SP_OBJECT_ID" ]]; then
  echo "Creating service principal..."
  SP_OBJECT_ID="$(az ad sp create --id "$APP_ID" --query id -o tsv)"
else
  echo "Exists: service principal $SP_OBJECT_ID"
fi

say "GitHub OIDC federation"

FIC_EXISTS="$(
  az ad app federated-credential list     --id "$APP_ID"     --query "[?name=='$FEDERATED_CREDENTIAL_NAME'] | length(@)"     -o tsv 2>/dev/null || echo "0"
)"

if [[ "$FIC_EXISTS" == "0" ]]; then
  echo "Creating federated credential for $GITHUB_REPOSITORY @ $GITHUB_BRANCH..."

  FIC_FILE="$(mktemp)"
  trap 'rm -f "$FIC_FILE"' EXIT

  cat >"$FIC_FILE" <<JSON
{
  "name": "$FEDERATED_CREDENTIAL_NAME",
  "issuer": "$OIDC_ISSUER",
  "subject": "$OIDC_SUBJECT",
  "description": "GitHub Actions OIDC for $GITHUB_REPOSITORY branch $GITHUB_BRANCH",
  "audiences": [
    "$OIDC_AUDIENCE"
  ]
}
JSON

  az ad app federated-credential create     --id "$APP_ID"     --parameters "$FIC_FILE"     --output none

  rm -f "$FIC_FILE"
  trap - EXIT
else
  echo "Exists: $FEDERATED_CREDENTIAL_NAME"
fi

say "Resource-group RBAC"

SCOPE="/subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP"
ROLE_DEFINITION_ID="/subscriptions/$SUBSCRIPTION_ID/providers/Microsoft.Authorization/roleDefinitions/$CONTRIBUTOR_ROLE_ID"

EXISTING_ROLE_COUNT="$(
  az role assignment list     --assignee-object-id "$SP_OBJECT_ID"     --scope "$SCOPE"     --query "[?roleDefinitionId=='$ROLE_DEFINITION_ID'] | length(@)"     -o tsv
)"

if [[ "$EXISTING_ROLE_COUNT" == "0" ]]; then
  echo "Assigning Contributor at resource-group scope..."
  az role assignment create     --assignee-object-id "$SP_OBJECT_ID"     --assignee-principal-type ServicePrincipal     --role "$CONTRIBUTOR_ROLE_ID"     --scope "$SCOPE"     --output none
else
  echo "Exists: Contributor assignment at $SCOPE"
fi

say "Verification"

az group show   --name "$RESOURCE_GROUP"   --subscription "$SUBSCRIPTION_ID"   --query "{name:name, location:location, id:id}"   --output table

az role assignment list   --assignee-object-id "$SP_OBJECT_ID"   --scope "$SCOPE"   --query "[].{role:roleDefinitionName, scope:scope}"   --output table

echo
echo "Azure bootstrap is complete."
echo
echo "GitHub Actions identifiers:"
echo "AZURE_CLIENT_ID=$APP_ID"
echo "AZURE_TENANT_ID=$TENANT_ID"
echo "AZURE_SUBSCRIPTION_ID=$SUBSCRIPTION_ID"
echo
echo "No Azure client secret was created."
echo "GitHub Actions will obtain ephemeral Azure access tokens through OIDC."

if command -v gh >/dev/null 2>&1 && gh auth status >/dev/null 2>&1; then
  echo
  echo "GitHub CLI is authenticated. To configure repository secrets automatically, run:"
  echo "  gh secret set AZURE_CLIENT_ID --repo $GITHUB_REPOSITORY --body \"$APP_ID\""
  echo "  gh secret set AZURE_TENANT_ID --repo $GITHUB_REPOSITORY --body \"$TENANT_ID\""
  echo "  gh secret set AZURE_SUBSCRIPTION_ID --repo $GITHUB_REPOSITORY --body \"$SUBSCRIPTION_ID\""
else
  echo
  echo "Optional: authenticate GitHub CLI ('gh auth login') and use the three commands above"
  echo "to eliminate the remaining GitHub portal steps."
fi
