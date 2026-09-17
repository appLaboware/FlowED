# FlowDisP Seed 0.3.0 POC

**Status:** experimental seed snapshot for external pilot

This release is designed to be extracted **inside an existing `_dev/` directory**.

It creates:

```text
_dev/
├── FLOWDISP-SEED-PROMPT.md
└── discovery/flowdisp/
    ├── seed/ROLL/
    ├── seed/FD_artifacts/
    ├── replay/
    ├── cases/
    ├── evidence-packs/
    ├── templates/
    ├── tests/
    └── fldp.py
```

Core lifecycle:

```text
free exploratory chat
→ preserve ROLL + FD_artifacts
→ chronological Seed Replay in deterministic overlapping chunks
→ append-only event / decision / claim lineage
→ one Git checkpoint commit per processed chunk
→ reverse forensic audit
→ Discovery Framing
→ bounded Research Cases FDP-RC-xxx
→ ABR rounds + owner forensic audit
→ evidence freeze
→ approved Evidence Pack
```

The ROLL remains immutable historical source. Replay files and Git commits are derived, auditable materializations and must not mutate canonical project files during reconstruction.

Validation: **7/7 stdlib-only Python tests passed**, plus an extraction smoke test under a temporary `_dev/` tree using `replay-init` and `replay-status`.

Archive SHA-256:

`725b6d58c6ae9cbd7338a47587a0a32fd535e3e7f1bd2a037bd48435c0e2aaff`

The release does not claim FlowDisP itself is novel or canonical.
