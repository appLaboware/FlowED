#!/usr/bin/env bash
set -euo pipefail

: "${BRIDGE_SHA:?BRIDGE_SHA is required}"

RG="rg-flowed-ideos-lab"
VAULT="mytrues-ingest-kv"
VM="mytrues-typedb-poc"
REGION="brazilsouth"

echo "[1/6] Preparing TypeDB admin credential in Azure Key Vault"
MGMT_TOKEN="$(az account get-access-token --query accessToken -o tsv)"
OID="$(MGMT_TOKEN="$MGMT_TOKEN" python3 - <<'PY'
import os, json, base64
p=os.environ["MGMT_TOKEN"].split(".")[1]
print(json.loads(base64.urlsafe_b64decode(p+"="*(-len(p)%4)))["oid"])
PY
)"
unset MGMT_TOKEN
echo "::add-mask::$OID"

az keyvault set-policy -g "$RG" -n "$VAULT" --object-id "$OID" \
  --secret-permissions get set list --only-show-errors -o none
sleep 5

TYPEDB_ADMIN_PASSWORD="$(az keyvault secret show --vault-name "$VAULT" -n typedb-poc-admin --query value -o tsv 2>/dev/null || true)"
if [ -z "$TYPEDB_ADMIN_PASSWORD" ]; then
  TYPEDB_ADMIN_PASSWORD="$(openssl rand -hex 24)"
  az keyvault secret set --vault-name "$VAULT" -n typedb-poc-admin \
    --value "$TYPEDB_ADMIN_PASSWORD" --only-show-errors -o none
fi
echo "::add-mask::$TYPEDB_ADMIN_PASSWORD"

echo "[2/6] Creating or reusing isolated Azure VM"
SUB="$(az account show --query id -o tsv)"
SUFFIX="$(printf '%s' "$SUB" | sha256sum | cut -c1-10)"
DNS_LABEL="mytrues-typedb-$SUFFIX"

if ! az vm show -g "$RG" -n "$VM" -o none 2>/dev/null; then
  echo "Resolving currently available VM size in $REGION"
  CANDIDATES=(Standard_B2als_v2 Standard_B2as_v2 Standard_D2as_v5 Standard_D2s_v5 Standard_D2_v5)
  SKU_JSON="$(az vm list-skus --location "$REGION" --resource-type virtualMachines --all -o json)"
  VM_SIZE="$(SKU_JSON="$SKU_JSON" python3 - <<'PY'
import json, os
candidates=["Standard_B2als_v2","Standard_B2as_v2","Standard_D2as_v5","Standard_D2s_v5","Standard_D2_v5"]
rows=json.loads(os.environ["SKU_JSON"])
available={r.get("name") for r in rows if not r.get("restrictions")}
for c in candidates:
    if c in available:
        print(c)
        break
PY
)"
  test -n "$VM_SIZE" || { echo "No approved 2-vCPU TypeDB POC SKU is currently unrestricted in $REGION" >&2; exit 1; }
  echo "Selected Azure VM size: $VM_SIZE"
  az vm create \
    -g "$RG" -n "$VM" --location "$REGION" \
    --image "Canonical:ubuntu-24_04-lts:server:latest" \
    --size "$VM_SIZE" \
    --admin-username typedbadmin \
    --generate-ssh-keys \
    --public-ip-sku Standard \
    --public-ip-address-dns-name "$DNS_LABEL" \
    --nsg-rule NONE \
    --tags project=MyTrues purpose=typedb-poc \
    --only-show-errors -o none
fi

echo "[3/6] Ensuring only HTTP/HTTPS public ingress"
NIC_ID="$(az vm show -g "$RG" -n "$VM" --query 'networkProfile.networkInterfaces[0].id' -o tsv)"
NSG_ID="$(az network nic show --ids "$NIC_ID" --query 'networkSecurityGroup.id' -o tsv)"
NSG_NAME="${NSG_ID##*/}"

az network nsg rule create -g "$RG" --nsg-name "$NSG_NAME" -n allow-http \
  --priority 1120 --direction Inbound --access Allow --protocol Tcp \
  --source-address-prefixes Internet --source-port-ranges '*' \
  --destination-address-prefixes '*' --destination-port-ranges 80 \
  --only-show-errors -o none

az network nsg rule create -g "$RG" --nsg-name "$NSG_NAME" -n allow-https \
  --priority 1121 --direction Inbound --access Allow --protocol Tcp \
  --source-address-prefixes Internet --source-port-ranges '*' \
  --destination-address-prefixes '*' --destination-port-ranges 443 \
  --only-show-errors -o none

PUBLIC_HOST="$(az vm show -d -g "$RG" -n "$VM" --query fqdns -o tsv)"
test -n "$PUBLIC_HOST"

echo "[4/6] Installing TypeDB CE 3.12.1 and seeding canonical memory"
BASE="https://raw.githubusercontent.com/appLaboware/FlowED/$BRIDGE_SHA/Tools/MyTrues/typedb-poc-bridge"
curl -fsSL "$BASE/on-vm.sh" -o /tmp/on-vm.sh

python3 - <<'PY'
import os, pathlib, shlex
keys=("TYPEDB_ADMIN_PASSWORD","PUBLIC_HOST","BRIDGE_SHA")
wrapper="#!/bin/bash\n"+''.join("export "+k+"="+shlex.quote(os.environ[k])+"\n" for k in keys)
wrapper+=pathlib.Path("/tmp/on-vm.sh").read_text()
pathlib.Path("/tmp/typedb-on-vm.sh").write_text(wrapper)
PY

az vm run-command invoke -g "$RG" -n "$VM" \
  --command-id RunShellScript --scripts @/tmp/typedb-on-vm.sh \
  --output json > /tmp/typedb-deploy.json

python3 - <<'PY'
import json
r=json.load(open("/tmp/typedb-deploy.json"))
msg="\n".join(x.get("message","") for x in r.get("value",[]))
if "READY database=mytrues_memory_poc_v0 occurrences=8 bindings=45" not in msg:
    raise SystemExit("Canonical TypeDB seed validation missing:\n"+msg[-1800:])
if "DEPLOY_OK" not in msg:
    raise SystemExit("Guest deploy completion marker missing:\n"+msg[-1800:])
print("Guest validation: 8 occurrences / 45 bindings")
PY

echo "[5/6] Verifying HTTPS and TypeDB authentication"
OK=false
for i in $(seq 1 90); do
  CODE="$(curl -sS --connect-timeout 5 --max-time 10 -o /tmp/signin.json -w '%{http_code}' \
    -X POST "https://$PUBLIC_HOST/v1/signin" \
    -H 'content-type: application/json' \
    --data-binary "{\"username\":\"admin\",\"password\":\"$TYPEDB_ADMIN_PASSWORD\"}" || true)"
  if [ "$CODE" = "200" ]; then
    OK=true
    break
  fi
  sleep 2
done
test "$OK" = true
jq -e '.token | type == "string" and length > 20' /tmp/signin.json >/dev/null
rm -f /tmp/signin.json

echo "[6/6] Publishing non-secret connection metadata"
STUDIO_URL="$(PUBLIC_HOST="$PUBLIC_HOST" python3 - <<'PY'
import os, urllib.parse
host=os.environ["PUBLIC_HOST"]
print("https://studio.typedb.com/connect?"+urllib.parse.urlencode({
    "address":"https://"+host,
    "username":"admin",
    "name":"MyTrues TypeDB POC",
}))
PY
)"

echo "TYPEDB_POC_READY"
echo "endpoint=https://$PUBLIC_HOST"
echo "database=mytrues_memory_poc_v0"
echo "studio=$STUDIO_URL"

if [ -n "${GITHUB_STEP_SUMMARY:-}" ]; then
  {
    echo "## MyTrues TypeDB Azure POC"
    echo
    echo "- TypeDB CE: `3.12.1`"
    echo "- Database: `mytrues_memory_poc_v0`"
    echo "- Endpoint: `https://$PUBLIC_HOST`"
    echo "- Username: `admin`"
    echo "- Password: Azure Key Vault `$VAULT` / secret `typedb-poc-admin`"
    echo "- Studio: $STUDIO_URL"
    echo "- Canonical seed: **8 occurrences / 45 bindings**"
  } >> "$GITHUB_STEP_SUMMARY"
fi
