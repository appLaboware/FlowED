# FlowED alignment after MyTrues split

Status: **STAGED — execute only after `MyTrues/mytrues` exists**.

## Goal

After the canonical repository is created, FlowED must stop carrying a second
editable copy of MyTrues.

`Tools/MYTRUES` becomes a **Git submodule** pointing to:

`https://github.com/MyTrues/mytrues.git`

This gives FlowED a repository-aligned link while keeping the canonical source
of truth in `MyTrues/mytrues`.

## Why submodule

A submodule preserves the required properties:

- the canonical repository remains independent;
- FlowED records an immutable MyTrues commit SHA;
- updating MyTrues inside FlowED is explicit;
- no implementation code is copied;
- FlowED can reproduce exactly which MyTrues revision it was aligned to.

A symlink to a URL would not provide Git version alignment and is therefore not
the chosen mechanism.

## Transition

After the canonical repository has been created and its accepted initial SHA is
known:

1. verify that every file currently required from `Tools/MYTRUES` exists in
   `MyTrues/mytrues`;
2. remove the tracked FlowED directory;
3. add `MyTrues/mytrues` as submodule at exactly `Tools/MYTRUES`;
4. checkout the accepted canonical SHA inside the submodule;
5. commit both `.gitmodules` and the gitlink entry;
6. verify a clean clone using:

   `git clone --recurse-submodules ...`

7. future alignment updates use an explicit reviewed SHA change.

## Update rule

Do not configure FlowED to follow `main` automatically.

The normal update is:

`candidate MyTrues SHA -> compatibility/conformance -> update submodule SHA -> commit`

This follows the same adoption principle used by IDEOS.

## IDEOS note

The new `MyTrues/ideos` repository is also canonical after the split. Whether
`Tools/IDEOS` becomes a submodule should be handled as a separate explicit
FlowED alignment decision; this migration only stages the requested
`Tools/MYTRUES` replacement.
