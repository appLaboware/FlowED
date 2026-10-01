#!/usr/bin/env bash
set -euo pipefail

docker rm -f ideos-exp005-im >/dev/null 2>&1 || true

docker pull grycap/im:latest
docker pull ghcr.io/grycap/im-client:latest

docker run -d   --name ideos-exp005-im   -p 8800:8800   -p 8899:8899   grycap/im:latest >/dev/null

cleanup() {
  docker logs ideos-exp005-im || true
  docker rm -f ideos-exp005-im >/dev/null 2>&1 || true
}
trap cleanup EXIT

echo "Waiting for the official IM container..."

ready=0
for i in $(seq 1 30); do
  if docker ps --filter name=ideos-exp005-im --filter status=running --format '{{.Names}}' | grep -qx ideos-exp005-im; then
    if (echo >/dev/tcp/127.0.0.1/8800) >/dev/null 2>&1 ||        (echo >/dev/tcp/127.0.0.1/8899) >/dev/null 2>&1; then
      ready=1
      break
    fi
  fi
  sleep 2
done

if [[ "$ready" != "1" ]]; then
  echo "IM container did not expose its service ports." >&2
  exit 1
fi

echo "IM service container is running."

docker run --rm ghcr.io/grycap/im-client:latest --help >/tmp/im-client-help.txt 2>&1 || true

if ! grep -qi "im_client\|Usage" /tmp/im-client-help.txt; then
  cat /tmp/im-client-help.txt
  echo "Official IM client did not expose the expected CLI." >&2
  exit 1
fi

echo "Official IM client is executable."
echo
echo "EXP-005 phase A: PASS"
