#!/usr/bin/env bash
set -euo pipefail

REPO="appLaboware/FlowED"
ENV_FILE="$HOME/.config/infabric/env/cloudflare.env"

if [ ! -f "$ENV_FILE" ]; then
  echo "ERRO: $ENV_FILE não encontrado." >&2
  exit 1
fi

# shellcheck disable=SC1090
source "$ENV_FILE"

TOKEN="${CLOUDFLARE_API_TOKEN:-${CF_DNS_EDIT:-}}"
if [ -z "$TOKEN" ]; then
  echo "ERRO: CLOUDFLARE_API_TOKEN/CF_DNS_EDIT ausente em $ENV_FILE." >&2
  exit 1
fi

command -v curl >/dev/null || { echo "ERRO: curl ausente" >&2; exit 1; }
command -v jq >/dev/null || { echo "ERRO: jq ausente" >&2; exit 1; }
command -v gh >/dev/null || { echo "ERRO: gh CLI ausente" >&2; exit 1; }

verify="$(curl -fsS https://api.cloudflare.com/client/v4/user/tokens/verify   -H "Authorization: Bearer $TOKEN"   -H 'Content-Type: application/json')"

jq -e '.success == true and .result.status == "active"' <<<"$verify" >/dev/null || {
  echo "ERRO: token Cloudflare não está ativo." >&2
  exit 1
}

zone="$(curl -fsS 'https://api.cloudflare.com/client/v4/zones?name=mytrues.io&status=active'   -H "Authorization: Bearer $TOKEN"   -H 'Content-Type: application/json')"

jq -e '.success == true and (.result | length) > 0' <<<"$zone" >/dev/null || {
  echo "ERRO: token não consegue ler a zona mytrues.io." >&2
  exit 1
}

printf '%s' "$TOKEN" | gh secret set CF_DNS_EDIT --repo "$REPO"

# O mesmo token deve ter Zone:Read + DNS:Edit; o workflow usa CF_DNS_EDIT para ambos.
gh workflow run mytrues-cloudflare-dns-apply.yml --repo "$REPO" --ref tools/ideos-lab

echo "OK: token validado e CF_DNS_EDIT atualizado em $REPO."
echo "A automação DNS foi disparada; o bind do Azure verifica a zona a cada 5 minutos."
