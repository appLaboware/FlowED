#!/usr/bin/env bash
set -euo pipefail

RESOURCE_GROUP="rg-flowed-ideos-lab"
APP_DISPLAY_NAME="FlowED-GitHub-Actions"
CONTRIBUTOR_ROLE_ID="b24988ac-6180-42a0-ab88-20f7382dd24c"

echo "== IDEOS Azure bootstrap: RBAC =="

SUBSCRIPTION_ID="$(az account show --query id -o tsv)"
TENANT_ID="$(az account show --query tenantId -o tsv)"

if [[ -z "$SUBSCRIPTION_ID" || -z "$TENANT_ID" ]]; then
  echo "ERROR: no active Azure subscription/tenant." >&2
  exit 1
fi

az group show --name "$RESOURCE_GROUP" --subscription "$SUBSCRIPTION_ID" >/dev/null

APP_ID="$(az ad app list   --display-name "$APP_DISPLAY_NAME"   --query "[?displayName=='$APP_DISPLAY_NAME'].appId | [0]"   -o tsv)"

if [[ -z "$APP_ID" ]]; then
  echo "ERROR: App registration '$APP_DISPLAY_NAME' was not found in the current tenant." >&2
  exit 1
fi

SP_OBJECT_ID="$(az ad sp show --id "$APP_ID" --query id -o tsv 2>/dev/null || true)"

if [[ -z "$SP_OBJECT_ID" ]]; then
  echo "Service principal not found; creating it for application $APP_DISPLAY_NAME..."
  SP_OBJECT_ID="$(az ad sp create --id "$APP_ID" --query id -o tsv)"
fi

SCOPE="/subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP"
ROLE_DEFINITION_ID="/subscriptions/$SUBSCRIPTION_ID/providers/Microsoft.Authorization/roleDefinitions/$CONTRIBUTOR_ROLE_ID"

EXISTING="$(az role assignment list   --assignee-object-id "$SP_OBJECT_ID"   --scope "$SCOPE"   --query "[?roleDefinitionId=='$ROLE_DEFINITION_ID'] | length(@)"   -o tsv)"

if [[ "$EXISTING" == "0" ]]; then
  echo "Assigning Contributor to $APP_DISPLAY_NAME at $SCOPE..."
  az role assignment create     --assignee-object-id "$SP_OBJECT_ID"     --assignee-principal-type ServicePrincipal     --role "$CONTRIBUTOR_ROLE_ID"     --scope "$SCOPE"     --output none
else
  echo "Contributor assignment already exists; no change required."
fi

echo
echo "RBAC bootstrap complete."
echo "Resource group : $RESOURCE_GROUP"
echo "Application    : $APP_DISPLAY_NAME"
echo "Scope          : $SCOPE"
echo
echo "Next GitHub values (identifiers, not passwords):"
echo "  AZURE_CLIENT_ID       = $APP_ID"
echo "  AZURE_TENANT_ID       = $TENANT_ID"
echo "  AZURE_SUBSCRIPTION_ID = $SUBSCRIPTION_ID"
