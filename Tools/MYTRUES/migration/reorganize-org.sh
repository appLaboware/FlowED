#!/usr/bin/env bash
set -euo pipefail

# Canonical MyTrues organization migration — definitive topology.
#
# Requires:
#   - gh authenticated with organization repository-admin rights
#   - git
#   - git-filter-repo
#
# This script NEVER deletes repositories.
# It preserves all eight legacy repositories under _arquived_261001.

ORG="MyTrues"
FLOWED_REPO="appLaboware/FlowED"
FLOWED_SOURCE_SHA="121c63642c4cc552c46a7cf3ff70ab57924cb2be"
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
  local visibility="$2"
  local description="$3"

  if gh api "repos/${ORG}/${name}" >/dev/null 2>&1; then
    echo "repo already exists: ${ORG}/${name}"
    return 0
  fi

  if [[ "$visibility" == "private" ]]; then
    gh repo create "${ORG}/${name}" --private --description "$description"
  else
    gh repo create "${ORG}/${name}" --public --description "$description"
  fi

  require_repo "${ORG}/${name}"
}

mirror_history() {
  local archived="$1"
  local target="$2"
  local dir="$WORKDIR/mirror-${target}"

  rm -rf "$dir"
  git clone --mirror "https://github.com/${ORG}/${archived}.git" "$dir"
  git -C "$dir" push --mirror "https://github.com/${ORG}/${target}.git"
  echo "history mirrored: ${archived} -> ${target}"
}

ensure_identity() {
  git config user.name >/dev/null 2>&1 || git config user.name "MyTrues Migration"
  git config user.email >/dev/null 2>&1 || git config user.email "migration@mytrues.invalid"
}

# ---------------------------------------------------------------------------
# 1. Preserve legacy org exactly.
# ---------------------------------------------------------------------------

for r in MyTrues MyTrues_p cli kernel paper replication site spec; do
  rename_repo "$r"
done

# ---------------------------------------------------------------------------
# 2. Create definitive topology.
# ---------------------------------------------------------------------------

create_repo_if_missing "mytrues" "public"   "Open decision-memory protocol, ports, conformance and reference implementation"

create_repo_if_missing "ccp" "public"   "Creator Cognitive Path (CCP): open conceptual model, provenance and projections"

create_repo_if_missing "edt" "private"   "Education-Driven Thinking doctoral research workspace"

create_repo_if_missing "research" "public"   "Reproducible frontier research, benchmarks, experiments and replication"

create_repo_if_missing "registry" "public"   "Open MyTrues plugin/engine/adapter registry and conformance metadata"

create_repo_if_missing "ideos" "public"   "Open DevOps intent product and reference MyTrues client"

create_repo_if_missing "site" "public"   "Public MyTrues/CCP/EDT documentation and site"

create_repo_if_missing "mytrues-enterprise" "private"   "Closed commercial extensions implementing the open MyTrues contracts"

# ---------------------------------------------------------------------------
# 3. Clone frozen FlowED source.
# ---------------------------------------------------------------------------

rm -rf "$WORKDIR/flowed"
git clone "https://github.com/${FLOWED_REPO}.git" "$WORKDIR/flowed"
git -C "$WORKDIR/flowed" checkout "$FLOWED_SOURCE_SHA"

# ---------------------------------------------------------------------------
# 4. Preserve direct historical ancestors for CCP / EDT / research / site.
# ---------------------------------------------------------------------------

mirror_history "spec${SUFFIX}" "ccp"
mirror_history "paper${SUFFIX}" "edt"
mirror_history "replication${SUFFIX}" "research"
mirror_history "site${SUFFIX}" "site"

# ---------------------------------------------------------------------------
# 5. Build canonical open MyTrues from qualified product staging only.
#    Do NOT import broad archaeology/research/thesis directories.
# ---------------------------------------------------------------------------

command -v git-filter-repo >/dev/null 2>&1 || {
  echo "git-filter-repo is required" >&2
  exit 1
}

rm -rf "$WORKDIR/mytrues-product"
git clone "https://github.com/${FLOWED_REPO}.git" "$WORKDIR/mytrues-product"
cd "$WORKDIR/mytrues-product"
git checkout -b migration-source "$FLOWED_SOURCE_SHA"

git filter-repo   --refs migration-source   --path Tools/MYTRUES/LICENSE   --path Tools/MYTRUES/README.md   --path Tools/MYTRUES/docker-compose.yml   --path Tools/MYTRUES/protocol   --path Tools/MYTRUES/conformance   --path Tools/MYTRUES/core   --path Tools/MYTRUES/memory   --path Tools/MYTRUES/reference   --path Tools/MYTRUES/integrations   --path Tools/MYTRUES/open   --path Tools/MYTRUES/seeds   --path Tools/MYTRUES/docs/ALGORITHM-BOUNDARY.md   --path Tools/MYTRUES/docs/GENERIC-PROTOCOL.md   --path Tools/MYTRUES/docs/OPEN-EXTENSION-ECOSYSTEM.md   --path-rename Tools/MYTRUES/:   --force

git branch -M main
git remote remove origin 2>/dev/null || true
git remote add origin "https://github.com/${ORG}/mytrues.git"
git push -u --force origin main

# ---------------------------------------------------------------------------
# 6. Import IDEOS subtree preserving relevant FlowED history.
# ---------------------------------------------------------------------------

rm -rf "$WORKDIR/ideos-source"
git clone "https://github.com/${FLOWED_REPO}.git" "$WORKDIR/ideos-source"
cd "$WORKDIR/ideos-source"
git checkout "$FLOWED_SOURCE_SHA"
git branch -D import-ideos 2>/dev/null || true
git subtree split --prefix=Tools/IDEOS "$FLOWED_SOURCE_SHA" -b import-ideos
git push --force "https://github.com/${ORG}/ideos.git" "import-ideos:main"

# ---------------------------------------------------------------------------
# 7. Add current conceptual/research material to historical successor repos.
# ---------------------------------------------------------------------------

sync_file() {
  local repo="$1"
  local src="$2"
  local dst="$3"
  local checkout="$WORKDIR/work-${repo}"

  if [[ ! -d "$checkout/.git" ]]; then
    rm -rf "$checkout"
    git clone "https://github.com/${ORG}/${repo}.git" "$checkout"
  fi

  mkdir -p "$checkout/$(dirname "$dst")"
  cp "$WORKDIR/flowed/$src" "$checkout/$dst"
}

# CCP
sync_file "ccp" "Tools/MYTRUES/docs/CCP-RECORD.md" "docs/CCP-RECORD.md"
sync_file "ccp" "Tools/MYTRUES/docs/EDT-CCP-MYTRUES-BOUNDARY.md" "docs/EDT-CCP-MYTRUES-BOUNDARY.md"
sync_file "ccp" "Tools/MYTRUES/docs/archaeology/EDT-001-TREE-ASSESSMENT.md" "research/EDT-001-TREE-ASSESSMENT.md"

# EDT
sync_file "edt" "Tools/MYTRUES/docs/EDT-CCP-MYTRUES-BOUNDARY.md" "research/EDT-CCP-MYTRUES-BOUNDARY.md"
sync_file "edt" "Tools/MYTRUES/docs/archaeology/EDT-HISTORICAL-SOURCES-001.md" "historical/EDT-HISTORICAL-SOURCES-001.md"
sync_file "edt" "Tools/MYTRUES/docs/archaeology/EDT-001-TREE-ASSESSMENT.md" "historical/EDT-001-TREE-ASSESSMENT.md"

# Research
rm -rf "$WORKDIR/work-research"
git clone "https://github.com/${ORG}/research.git" "$WORKDIR/work-research"
mkdir -p "$WORKDIR/work-research/current"
cp -R "$WORKDIR/flowed/Tools/MYTRUES/research/." "$WORKDIR/work-research/current/"

for repo in ccp edt research; do
  d="$WORKDIR/work-${repo}"
  (
    cd "$d"
    ensure_identity
    git add -A
    if ! git diff --cached --quiet; then
      git commit -m "docs(migration): import qualified FlowED material @ ${FLOWED_SOURCE_SHA}"
      git push origin main
    fi
  )
done

# ---------------------------------------------------------------------------
# 8. Seed registry and enterprise boundary repositories.
# ---------------------------------------------------------------------------

seed_repo() {
  local repo="$1"
  local body="$2"
  local d="$WORKDIR/work-${repo}"

  rm -rf "$d"
  git clone "https://github.com/${ORG}/${repo}.git" "$d"
  cd "$d"
  ensure_identity

  if [[ ! -f README.md ]]; then
    printf "%s\n" "$body" > README.md
    git add README.md
    git commit -m "chore: initialize canonical repository boundary"
    git push origin main
  fi
}

seed_repo "registry" "# MyTrues Registry

Open registry for MyTrues-compatible engines, adapters and plugins.

Publication does not imply conformance, security review, benchmarking or scientific reproduction."

seed_repo "mytrues-enterprise" "# MyTrues Enterprise

Private commercial extensions implementing the OPEN MyTrues protocol and ports.

This repository MUST NOT redefine the public wire protocol, port contracts, CCP or EDT."

# ---------------------------------------------------------------------------
# 9. Evidence and optional final legacy archive lock.
# ---------------------------------------------------------------------------

MYTRUES_SHA="$(gh api "repos/${ORG}/mytrues/commits/main" --jq '.sha')"
CCP_SHA="$(gh api "repos/${ORG}/ccp/commits/main" --jq '.sha')"
EDT_SHA="$(gh api "repos/${ORG}/edt/commits/main" --jq '.sha')"
RESEARCH_SHA="$(gh api "repos/${ORG}/research/commits/main" --jq '.sha')"
IDEOS_SHA="$(gh api "repos/${ORG}/ideos/commits/main" --jq '.sha')"

for r in MyTrues MyTrues_p cli kernel paper replication site spec; do
  gh api -X PATCH "repos/${ORG}/${r}${SUFFIX}" -F archived=true >/dev/null
done

cat > "$WORKDIR/migration-evidence.json" <<JSON
{
  "organization": "$ORG",
  "flowed_source_sha": "$FLOWED_SOURCE_SHA",
  "archive_suffix": "$SUFFIX",
  "canonical": {
    "mytrues": {"visibility":"public","sha":"$MYTRUES_SHA"},
    "ccp": {"visibility":"public","sha":"$CCP_SHA"},
    "edt": {"visibility":"private","sha":"$EDT_SHA"},
    "research": {"visibility":"public","sha":"$RESEARCH_SHA"},
    "registry": {"visibility":"public"},
    "ideos": {"visibility":"public","sha":"$IDEOS_SHA"},
    "site": {"visibility":"public"},
    "mytrues-enterprise": {"visibility":"private"}
  }
}
JSON

cat "$WORKDIR/migration-evidence.json"

echo
echo "NEXT:"
echo "1. run MyTrues conformance in canonical mytrues"
echo "2. run IDEOS -> MyTrues adapter compatibility and pin canonical SHA"
echo "3. verify CCP/EDT/research history and licenses"
echo "4. populate registry manifest/conformance schemas"
echo "5. publish no scientific novelty claim until frontier suite gates are run"
