#!/usr/bin/env bash
set -euo pipefail

NET=ideos-exp005
IM=ideos-exp005-im
PROXY=ideos-exp005-docker-api
AUTH_DIR="$(mktemp -d)"
trap 'docker rm -f "$IM" "$PROXY" >/dev/null 2>&1 || true; docker network rm "$NET" >/dev/null 2>&1 || true; rm -rf "$AUTH_DIR"' EXIT

docker network create "$NET" >/dev/null 2>&1 || true

docker run -d --name "$PROXY"   --network "$NET"   -v /var/run/docker.sock:/var/run/docker.sock   alpine/socat   TCP-LISTEN:2375,fork,reuseaddr UNIX-CONNECT:/var/run/docker.sock >/dev/null

docker run -d --name "$IM"   --network "$NET"   grycap/im:latest >/dev/null

cat > "$AUTH_DIR/auth.dat" <<'EOF'
id = im; type = InfrastructureManager; username = ideos; password = ideos
id = docker; type = Docker; host = http://ideos-exp005-docker-api:2375
EOF

for i in $(seq 1 30); do
  if docker run --rm --network "$NET"       -v "$AUTH_DIR:/work"       ghcr.io/grycap/im-client:latest       -r http://ideos-exp005-im:8800       -a /work/auth.dat list >/tmp/im-list.txt 2>&1; then
    break
  fi
  sleep 2
done

cat /tmp/im-list.txt

docker run --rm --network "$NET"   -v "$AUTH_DIR:/work"   -v "$PWD/Tools/IDEOS/experiments/EXP-005-infrastructure-manager:/exp:ro"   ghcr.io/grycap/im-client:latest   -r http://ideos-exp005-im:8800   -a /work/auth.dat   create /exp/docker-baseline.radl | tee /tmp/im-create.txt

echo "=== containers created through IM ==="
docker ps -a --format '{{.ID}} {{.Image}} {{.Names}} {{.Status}}'

if ! docker ps -a --format '{{.Image}}' | grep -q '^ubuntu:22.04$'; then
  echo "No Ubuntu container was materialized by IM." >&2
  docker logs "$IM" || true
  exit 1
fi

echo "EXP-005 phase B local Docker materialization: PASS"
