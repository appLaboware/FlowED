#!/usr/bin/env sh
set -eu

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
IDEOS_ROOT="$(CDPATH= cd -- "$SCRIPT_DIR/../.." && pwd)"
LOCK_FILE="${IDEOS_MYTRUES_LOCK:-$IDEOS_ROOT/upstreams/mytrues.lock.json}"
BASE_URL="${MYTRUES_BASE_URL:-}"

fail() {
  echo "DecisionMemory/MyTrues adapter: $*" >&2
  exit 2
}

[ -f "$LOCK_FILE" ] || fail "canonical upstream lock missing: $LOCK_FILE"
[ -n "$BASE_URL" ] || fail "MYTRUES_BASE_URL is required"

python3 - "$LOCK_FILE" <<'PY'
import json, re, sys
p = sys.argv[1]
with open(p, encoding="utf-8") as f:
    lock = json.load(f)
sha = lock.get("upstream", {}).get("commit_sha", "")
repo = lock.get("upstream", {}).get("repository", "")
if repo != "https://github.com/MyTrues/mytrues":
    raise SystemExit("invalid canonical MyTrues repository in lock")
if not re.fullmatch(r"[0-9a-f]{40}", sha):
    raise SystemExit("MyTrues lock must contain a real 40-hex commit SHA")
PY

cmd="${1:-}"
case "$cmd" in
  request)
    [ "$#" -eq 2 ] || fail "usage: adapter.sh request <decision-request.json>"
    curl --fail-with-body --silent --show-error       -H 'Content-Type: application/json'       --data-binary "@$2"       "${BASE_URL%/}/v1/decisions/resolve.failure"
    ;;
  poll)
    [ "$#" -eq 2 ] || fail "usage: adapter.sh poll <decisionRequestId>"
    curl --fail-with-body --silent --show-error       "${BASE_URL%/}/v1/decision-requests/$2"
    ;;
  *)
    fail "supported commands: request | poll"
    ;;
esac
