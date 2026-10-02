#!/bin/bash
set -euo pipefail
: "${TYPEDB_ADMIN_PASSWORD:?}" "${PUBLIC_HOST:?}" "${BRIDGE_SHA:?}"
export DEBIAN_FRONTEND=noninteractive

if ! command -v docker >/dev/null; then
  apt-get update -qq
  apt-get install -y -qq docker.io curl python3-venv >/dev/null
fi
systemctl enable --now docker >/dev/null
install -d -m 700 /var/lib/mytrues-typedb/data /var/lib/mytrues-typedb/poc

IMAGE='typedb/typedb:3.12.1@sha256:4224951114b044d52e2fe48108be26ae2734726041dae8d63453ecd407fe2422'
docker pull "$IMAGE" >/dev/null
if docker inspect mytrues-typedb >/dev/null 2>&1; then
  docker rm -f mytrues-typedb >/dev/null
fi
docker run -d --name mytrues-typedb --restart unless-stopped   -p 127.0.0.1:1729:1729 -p 127.0.0.1:8000:8000   -v /var/lib/mytrues-typedb/data:/var/lib/typedb/data   "$IMAGE" >/dev/null

for i in $(seq 1 90); do
  if curl -fsS --max-time 2 http://127.0.0.1:8000/ >/dev/null 2>&1; then break; fi
  if [ "$i" = 90 ]; then docker logs mytrues-typedb >&2; exit 1; fi
  sleep 1
done

base="https://raw.githubusercontent.com/appLaboware/FlowED/$BRIDGE_SHA/Tools/MyTrues/typedb-poc-bridge"
curl -fsSL "$base/00-schema.tql" -o /var/lib/mytrues-typedb/poc/00-schema.tql
curl -fsSL "$base/canonical-memory.json" -o /var/lib/mytrues-typedb/poc/canonical-memory.json
curl -fsSL "$base/seed_once.py" -o /var/lib/mytrues-typedb/poc/seed_once.py

python3 -m venv /var/lib/mytrues-typedb/venv
/var/lib/mytrues-typedb/venv/bin/pip install -q 'typedb-driver==3.13.6'
TYPEDB_ADMIN_PASSWORD="$TYPEDB_ADMIN_PASSWORD" /var/lib/mytrues-typedb/venv/bin/python /var/lib/mytrues-typedb/poc/seed_once.py

cat >/var/lib/mytrues-typedb/Caddyfile <<EOF
$PUBLIC_HOST {
  reverse_proxy 127.0.0.1:8000
}
EOF
docker pull caddy:2 >/dev/null
if docker inspect mytrues-typedb-https >/dev/null 2>&1; then
  docker rm -f mytrues-typedb-https >/dev/null
fi
docker run -d --name mytrues-typedb-https --restart unless-stopped --network host   -v /var/lib/mytrues-typedb/Caddyfile:/etc/caddy/Caddyfile:ro   -v /var/lib/mytrues-typedb/caddy-data:/data   -v /var/lib/mytrues-typedb/caddy-config:/config   caddy:2 >/dev/null

echo "DEPLOY_OK"
