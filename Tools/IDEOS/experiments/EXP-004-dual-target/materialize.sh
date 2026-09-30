#!/usr/bin/env bash
set -euo pipefail

ACTION="${1:-}"
TARGET="${2:-}"

BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck disable=SC1091
source "$BASE_DIR/application.env"

RESOURCE_GROUP="${RESOURCE_GROUP:-rg-flowed-ideos-lab}"
LOCATION="${LOCATION:-brazilsouth}"

usage() {
  echo "Usage: $0 <deploy|verify|destroy|endpoint> <docker|azure>"
  exit 2
}

[[ -n "$ACTION" && -n "$TARGET" ]] || usage

case "$TARGET" in
  docker|azure) ;;
  *) usage ;;
esac

HTML="<html><head><title>${PAGE_TITLE}</title></head><body><h1>${PAGE_TITLE}</h1><p>${PAGE_MESSAGE}</p><p>app=${APP_ID}</p></body></html>"
HTML_B64="$(printf '%s' "$HTML" | base64 | tr -d '\n')"
START_COMMAND="printf '%s' '$HTML_B64' | base64 -d > /usr/share/nginx/html/index.html && exec nginx -g 'daemon off;'"

docker_name() {
  echo "ideos-${APP_ID}"
}

azure_name() {
  # Stable per GitHub run when available; otherwise stable for interactive use.
  if [[ -n "${GITHUB_RUN_ID:-}" ]]; then
    echo "ideos-${APP_ID}-${GITHUB_RUN_ID}"
  else
    echo "ideos-${APP_ID}"
  fi
}

azure_dns_label() {
  local suffix
  if [[ -n "${GITHUB_RUN_ID:-}" ]]; then
    suffix="${GITHUB_RUN_ID}"
  else
    suffix="$(az account show --query id -o tsv | tr -d '-' | cut -c1-10)"
  fi
  echo "ideos-${APP_ID}-${suffix}" | tr '[:upper:]' '[:lower:]'
}

deploy_docker() {
  local name
  name="$(docker_name)"

  docker rm -f "$name" >/dev/null 2>&1 || true

  docker run -d     --name "$name"     -p "${PUBLIC_PORT}:${CONTAINER_PORT}"     "$IMAGE"     /bin/sh -c "$START_COMMAND" >/dev/null

  echo "docker://$name"
  echo "http://127.0.0.1:$PUBLIC_PORT"
}

verify_docker() {
  curl --fail --silent --show-error --retry 20 --retry-delay 1     "http://127.0.0.1:$PUBLIC_PORT"
  echo
}

destroy_docker() {
  docker rm -f "$(docker_name)" >/dev/null 2>&1 || true
  echo "Docker materialization removed."
}

endpoint_docker() {
  echo "http://127.0.0.1:$PUBLIC_PORT"
}

deploy_azure() {
  command -v az >/dev/null 2>&1 || {
    echo "Azure CLI is required." >&2
    exit 1
  }

  local name dns
  name="$(azure_name)"
  dns="$(azure_dns_label)"

  az group show --name "$RESOURCE_GROUP" >/dev/null

  az container delete     --resource-group "$RESOURCE_GROUP"     --name "$name"     --yes >/dev/null 2>&1 || true

  az container create     --resource-group "$RESOURCE_GROUP"     --name "$name"     --location "$LOCATION"     --image "$IMAGE"     --os-type Linux     --cpu 1     --memory 1     --ports "$CONTAINER_PORT"     --ip-address Public     --dns-name-label "$dns"     --restart-policy Always     --command-line "/bin/sh -c \"$START_COMMAND\""     --output none

  local fqdn
  fqdn="$(az container show     --resource-group "$RESOURCE_GROUP"     --name "$name"     --query ipAddress.fqdn     -o tsv)"

  echo "azure://$RESOURCE_GROUP/$name"
  echo "http://$fqdn"
}

verify_azure() {
  local name fqdn
  name="$(azure_name)"
  fqdn="$(az container show     --resource-group "$RESOURCE_GROUP"     --name "$name"     --query ipAddress.fqdn     -o tsv)"

  test -n "$fqdn"

  for attempt in $(seq 1 30); do
    if curl --fail --silent --show-error --max-time 10 "http://$fqdn"; then
      echo
      return 0
    fi
    echo "Waiting for Azure endpoint ($attempt/30)..." >&2
    sleep 10
  done

  az container logs     --resource-group "$RESOURCE_GROUP"     --name "$name" || true
  return 1
}

destroy_azure() {
  local name
  name="$(azure_name)"

  az container delete     --resource-group "$RESOURCE_GROUP"     --name "$name"     --yes >/dev/null 2>&1 || true

  echo "Azure materialization removed."
}

endpoint_azure() {
  local name
  name="$(azure_name)"

  az container show     --resource-group "$RESOURCE_GROUP"     --name "$name"     --query '"http://" + ipAddress.fqdn'     -o tsv
}

case "$ACTION:$TARGET" in
  deploy:docker) deploy_docker ;;
  verify:docker) verify_docker ;;
  destroy:docker) destroy_docker ;;
  endpoint:docker) endpoint_docker ;;
  deploy:azure) deploy_azure ;;
  verify:azure) verify_azure ;;
  destroy:azure) destroy_azure ;;
  endpoint:azure) endpoint_azure ;;
  *) usage ;;
esac
