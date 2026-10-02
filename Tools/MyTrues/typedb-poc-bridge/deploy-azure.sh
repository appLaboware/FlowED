#!/usr/bin/env bash
set -euo pipefail

: "${BRIDGE_SHA:?BRIDGE_SHA is required}"

RG="rg-flowed-ideos-lab"
VAULT="mytrues-ingest-kv"
PREFERRED_REGIONS=(eastus2 eastus centralus westus3 brazilsouth)

echo "[1/6] Preparing TypeDB admin credential in Azure Key Vault"
MGMT_TOKEN="$(az account get-access-token --query accessToken -o tsv)"
OID="$(MGMT_TOKEN="$MGMT_TOKEN" python3 - <<'PY'
import os,json,base64
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

cleanup_attempt() {
  local vm="$1"
  local vnet="${vm}-vnet"
  local nsg="${vm}-nsg"
  local pip="${vm}-pip"
  local disk="${vm}-osdisk"
  echo "Cleaning failed attempt resources for $vm"
  az vm delete -g "$RG" -n "$vm" --yes --force-deletion true --only-show-errors >/dev/null 2>&1 || true
  for nic in $(az network nic list -g "$RG" --query "[?starts_with(name, '$vm')].name" -o tsv 2>/dev/null || true); do
    az network nic delete -g "$RG" -n "$nic" --only-show-errors >/dev/null 2>&1 || true
  done
  az disk delete -g "$RG" -n "$disk" --yes --only-show-errors >/dev/null 2>&1 || true
  az network public-ip delete -g "$RG" -n "$pip" --only-show-errors >/dev/null 2>&1 || true
  az network nsg delete -g "$RG" -n "$nsg" --only-show-errors >/dev/null 2>&1 || true
  az network vnet delete -g "$RG" -n "$vnet" --only-show-errors >/dev/null 2>&1 || true
}

echo "[2/6] Selecting and allocating isolated Azure VM"
VM="$(az vm list -g "$RG" --query "[?tags.project=='MyTrues' && tags.purpose=='typedb-poc' && tags.role=='typedb-server' && provisioningState=='Succeeded'].name | [0]" -o tsv 2>/dev/null || true)"
REGION=""
if [ -n "$VM" ]; then
  REGION="$(az vm show -g "$RG" -n "$VM" --query location -o tsv)"
  echo "Reusing healthy TypeDB VM $VM in $REGION"
else
  SUB="$(az account show --query id -o tsv)"
  SUFFIX="$(printf '%s' "$SUB" | sha256sum | cut -c1-8)"

  for candidate_region in "${PREFERRED_REGIONS[@]}"; do
    echo "Checking quota/capacity metadata in $candidate_region"
    az vm list-skus --location "$candidate_region" --resource-type virtualMachines --all -o json > /tmp/typedb-skus.json
    az vm list-usage --location "$candidate_region" -o json > /tmp/typedb-usage.json

    PICK="$(python3 - <<'PY'
import json
skus=json.load(open("/tmp/typedb-skus.json"))
usage=json.load(open("/tmp/typedb-usage.json"))
spare={}
for u in usage:
    name=(u.get("name") or {}).get("value","").lower()
    try: spare[name]=int(u.get("limit",0))-int(u.get("currentValue",0))
    except (TypeError,ValueError): pass
if spare.get("cores",999999) < 2: raise SystemExit(0)
choices=[]
for row in skus:
    name=row.get("name","")
    if not (name.startswith("Standard_B") or name.startswith("Standard_D")): continue
    if row.get("restrictions"): continue
    family=(row.get("family") or "").lower()
    if not family or spare.get(family,0) < 2: continue
    caps={c.get("name"):c.get("value") for c in row.get("capabilities",[])}
    try:
        cpus=float(caps.get("vCPUs","0")); mem=float(caps.get("MemoryGB","0"))
    except ValueError: continue
    if cpus != 2 or mem < 4 or mem > 16: continue
    rank=0 if name.startswith("Standard_B") else 1
    choices.append((rank,mem,name,family))
if choices:
    _,mem,name,family=sorted(choices)[0]
    print(f"{name}|{family}|{mem}")
PY
)"
    [ -n "$PICK" ] || { echo "No quota-backed candidate in $candidate_region"; continue; }
    IFS='|' read -r VM_SIZE VM_FAMILY VM_MEMORY <<<"$PICK"

    region_slug="$(printf '%s' "$candidate_region" | tr -cd 'a-z0-9')"
    ATTEMPT_VM="mytrues-tdb-$region_slug"
    VNET="${ATTEMPT_VM}-vnet"
    NSG="${ATTEMPT_VM}-nsg"
    PIP="${ATTEMPT_VM}-pip"
    DISK="${ATTEMPT_VM}-osdisk"
    DNS_LABEL="mytrues-tdb-$SUFFIX-$region_slug"

    cleanup_attempt "$ATTEMPT_VM"
    echo "Attempting region=$candidate_region size=$VM_SIZE family=$VM_FAMILY memory_gb=$VM_MEMORY"

    if az vm create \
      -g "$RG" -n "$ATTEMPT_VM" --location "$candidate_region" \
      --image "Canonical:ubuntu-24_04-lts:server:latest" \
      --size "$VM_SIZE" \
      --admin-username typedbadmin \
      --generate-ssh-keys \
      --vnet-name "$VNET" --subnet default \
      --nsg "$NSG" --nsg-rule NONE \
      --public-ip-address "$PIP" --public-ip-sku Standard \
      --public-ip-address-dns-name "$DNS_LABEL" \
      --os-disk-name "$DISK" --os-disk-delete-option Delete --nic-delete-option Delete \
      --tags project=MyTrues purpose=typedb-poc role=typedb-server \
      --only-show-errors -o none; then
        VM="$ATTEMPT_VM"
        REGION="$candidate_region"
        echo "VM allocation succeeded: $VM in $REGION"
        break
    fi

    echo "Allocation failed in $candidate_region; trying next region"
    cleanup_attempt "$ATTEMPT_VM"
  done
fi

test -n "$VM" && test -n "$REGION" || { echo "Unable to allocate TypeDB POC VM in preferred regions" >&2; exit 1; }

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
TYPEDB_ADMIN_PASSWORD="$TYPEDB_ADMIN_PASSWORD" PUBLIC_HOST="$PUBLIC_HOST" BRIDGE_SHA="$BRIDGE_SHA" \
python3 - <<'PY'
import os,pathlib,shlex
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
    -X POST "https://$PUBLIC_HOST/v1/signin" -H 'content-type: application/json' \
    --data-binary "{\"username\":\"admin\",\"password\":\"$TYPEDB_ADMIN_PASSWORD\"}" || true)"
  if [ "$CODE" = "200" ]; then OK=true; break; fi
  sleep 2
done
test "$OK" = true
jq -e '.token | type == "string" and length > 20' /tmp/signin.json >/dev/null
rm -f /tmp/signin.json

echo "[6/6] Publishing non-secret connection metadata"
STUDIO_URL="$(PUBLIC_HOST="$PUBLIC_HOST" python3 - <<'PY'
import os,urllib.parse
host=os.environ["PUBLIC_HOST"]
print("https://studio.typedb.com/connect?"+urllib.parse.urlencode({
    "address":"https://"+host,"username":"admin","name":"MyTrues TypeDB POC"}))
PY
)"
echo "TYPEDB_POC_READY"
echo "vm=$VM"
echo "region=$REGION"
echo "endpoint=https://$PUBLIC_HOST"
echo "database=mytrues_memory_poc_v0"
echo "studio=$STUDIO_URL"

if [ -n "${GITHUB_STEP_SUMMARY:-}" ]; then
  {
    echo "## MyTrues TypeDB Azure POC"
    echo
    echo "- Resource group: `$RG`"
    echo "- VM: `$VM`"
    echo "- Region: `$REGION`"
    echo "- TypeDB CE: `3.12.1`"
    echo "- Database: `mytrues_memory_poc_v0`"
    echo "- Endpoint: `https://$PUBLIC_HOST`"
    echo "- Username: `admin`"
    echo "- Password: Azure Key Vault `$VAULT` / secret `typedb-poc-admin`"
    echo "- Studio: $STUDIO_URL"
    echo "- Canonical seed: **8 occurrences / 45 bindings**"
  } >> "$GITHUB_STEP_SUMMARY"
fi
