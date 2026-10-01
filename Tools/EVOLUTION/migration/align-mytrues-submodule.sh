#!/usr/bin/env bash
set -euo pipefail

# Replace FlowED's staged Tools/MYTRUES directory with a gitlink to the
# canonical MyTrues repository.
#
# Run from the FlowED repository root only after MyTrues/mytrues exists.
#
# Usage:
#   Tools/EVOLUTION/migration/align-mytrues-submodule.sh <40-hex-canonical-sha>

CANONICAL_URL="https://github.com/MyTrues/mytrues.git"
PATH_IN_FLOWED="Tools/MYTRUES"
SHA="${1:-}"

if ! [[ "$SHA" =~ ^[0-9a-f]{40}$ ]]; then
  echo "usage: $0 <40-hex-canonical-sha>" >&2
  exit 2
fi

git rev-parse --show-toplevel >/dev/null
ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"

if ! git ls-remote "$CANONICAL_URL" "$SHA" | grep -q "$SHA"; then
  # Some servers do not advertise arbitrary SHA through ls-remote.
  # Fetch verification below remains authoritative.
  echo "canonical SHA not advertised directly; verifying by fetch"
fi

# Keep the operation safe if already aligned.
if git config -f .gitmodules --get-regexp '^submodule\..*\.path$' 2>/dev/null |
   grep -q "[[:space:]]$PATH_IN_FLOWED$"; then
  echo "$PATH_IN_FLOWED is already a submodule"
else
  git rm -r "$PATH_IN_FLOWED"
  git submodule add "$CANONICAL_URL" "$PATH_IN_FLOWED"
fi

git -C "$PATH_IN_FLOWED" fetch origin "$SHA"
git -C "$PATH_IN_FLOWED" checkout --detach "$SHA"

ACTUAL="$(git -C "$PATH_IN_FLOWED" rev-parse HEAD)"
[ "$ACTUAL" = "$SHA" ] || {
  echo "submodule checkout mismatch: expected $SHA got $ACTUAL" >&2
  exit 1
}

git add .gitmodules "$PATH_IN_FLOWED"

echo
echo "Staged FlowED alignment:"
git diff --cached --submodule=log -- .gitmodules "$PATH_IN_FLOWED"

echo
echo "Review, then commit the gitlink update."
