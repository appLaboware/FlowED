#!/usr/bin/env bash
set -euo pipefail

# Canonical MyTrues org migration.
# Requires:
#   - gh authenticated with admin rights to the MyTrues organization
#   - git
#   - git-filter-repo (only for the legacy CCP history merge)
#
# This script is intentionally explicit and idempotency-aware. It never deletes repos.

ORG="MyTrues"
FLOWED_REPO="appLaboware/FlowED"
FLOWED_SOURCE_SHA="ef07118f8f4b3cee5f9c2bcd110d1ab9e50753f7"
LEGACY_CCP_REPO="InitProj-260119/MyTrues"
LEGACY_CCP_SHA="dc891f1d354b85c6f11666d62cb1e59dde839b2e"
SUFFIX="_arquived_261001"

WORKDIR="${WORKDIR:-$(pwd)/.mytrues-org-migration}"
mkdir -p "$WORKDIR"

require_repo() {
  gh api "repos/$1" >/dev/null
}

rename_repo() {
  local old="$1"
  local new="${old}${SUFFIX}"

  if gh api "repos/${ORG}/${new}" >/dev/null 2>&1; then
    echo "rename already satisfied: ${ORG}/${new}"
    return 0
  fi

  require_repo "${ORG}/${old}"
  gh api -X PATCH "repos/${ORG}/${old}" -f "name=${new}" >/dev/null
  require_repo "${ORG}/${new}"
  echo "renamed: ${ORG}/${old} -> ${ORG}/${new}"
}

create_repo_if_missing() {
  local name="$1"
  local description="$2"
  if gh api "repos/${ORG}/${name}" >/dev/null 2>&1; then
    echo "repo already exists: ${ORG}/${name}"
    return 0
  fi
  gh repo create "${ORG}/${name}" --public --description "$description"
  require_repo "${ORG}/${name}"
}

for r in MyTrues MyTrues_p cli kernel paper replication site spec; do
  rename_repo "$r"
done

create_repo_if_missing "mytrues" "Open domain-generic decision protocol and reference implementation"
create_repo_if_missing "ideos" "Open DevOps intent CLI composed from adopted tools"

rm -rf "$WORKDIR/flowed"
git clone "https://github.com/${FLOWED_REPO}.git" "$WORKDIR/flowed"
cd "$WORKDIR/flowed"
git checkout "$FLOWED_SOURCE_SHA"

git branch -D import-mytrues 2>/dev/null || true
git branch -D import-ideos 2>/dev/null || true

git subtree split --prefix=Tools/MYTRUES "$FLOWED_SOURCE_SHA" -b import-mytrues
git subtree split --prefix=Tools/IDEOS "$FLOWED_SOURCE_SHA" -b import-ideos

# Migration evidence belongs to FlowED, not to the new canonical MyTrues product.
git checkout import-mytrues
git rm -r ORG-INVENTORY.md MIGRATION-MANIFEST.md migration
git commit -m "chore(migration): keep FlowED migration evidence outside canonical MyTrues"
git checkout "$FLOWED_SOURCE_SHA"

git push --force-with-lease="refs/heads/main:"   "https://github.com/${ORG}/mytrues.git" "import-mytrues:main" || git push "https://github.com/${ORG}/mytrues.git" "import-mytrues:main"

git push --force-with-lease="refs/heads/main:"   "https://github.com/${ORG}/ideos.git" "import-ideos:main" || git push "https://github.com/${ORG}/ideos.git" "import-ideos:main"

# Preserve the earlier CCP/EDT lineage as documentary history.
command -v git-filter-repo >/dev/null 2>&1 || {
  echo "git-filter-repo is required to preserve legacy CCP history" >&2
  exit 1
}

rm -rf "$WORKDIR/legacy-ccp"
git clone "https://github.com/${LEGACY_CCP_REPO}.git" "$WORKDIR/legacy-ccp"
cd "$WORKDIR/legacy-ccp"
git checkout "$LEGACY_CCP_SHA"
git filter-repo   --path docs/pt-br   --path CORE/mytrues-evolution   --path LICENSE   --to-subdirectory-filter docs/legacy-ccp-history   --force

LEGACY_HEAD="$(git rev-parse HEAD)"

rm -rf "$WORKDIR/mytrues-canonical"
git clone "https://github.com/${ORG}/mytrues.git" "$WORKDIR/mytrues-canonical"
cd "$WORKDIR/mytrues-canonical"
git remote add legacy "$WORKDIR/legacy-ccp"
git fetch legacy
git merge --allow-unrelated-histories --no-ff "$LEGACY_HEAD"   -m "docs(ccp): preserve historical EDT/CCP lineage"
git push origin main

MYTRUES_SHA="$(git rev-parse HEAD)"
IDEOS_SHA="$(git -C "$WORKDIR/flowed" rev-parse import-ideos)"

# Verify MIT license is present in both canonical roots.
test -f "$WORKDIR/mytrues-canonical/LICENSE"
git clone --depth 1 "https://github.com/${ORG}/ideos.git" "$WORKDIR/ideos-canonical"
test -f "$WORKDIR/ideos-canonical/LICENSE"

cat > "$WORKDIR/migration-evidence.json" <<JSON
{
  "organization": "$ORG",
  "flowed_source_sha": "$FLOWED_SOURCE_SHA",
  "legacy_ccp_source_sha": "$LEGACY_CCP_SHA",
  "mytrues_url": "https://github.com/$ORG/mytrues",
  "mytrues_initial_sha": "$MYTRUES_SHA",
  "ideos_url": "https://github.com/$ORG/ideos",
  "ideos_initial_subtree_sha": "$IDEOS_SHA",
  "archive_suffix": "$SUFFIX"
}
JSON

cat "$WORKDIR/migration-evidence.json"

echo
echo "NEXT:"
echo "1. run adapter compatibility against canonical MyTrues SHA $MYTRUES_SHA"
echo "2. write that SHA + run URL into MyTrues/ideos upstream lock"
echo "3. verify all eight archived repository URLs"
