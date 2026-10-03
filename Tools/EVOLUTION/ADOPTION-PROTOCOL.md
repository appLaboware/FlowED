# ADOPTION-PROTOCOL

Status: canonical adoption rule for external and internal upstreams.

## Purpose

Adopt an existing tool/protocol without turning a consumer into a fork, mirror
or second source of truth.

## Required record

Every adoption MUST record:

1. upstream identity and canonical repository;
2. license;
3. immutable version/commit SHA used by the consumer;
4. capability being adopted;
5. consumer-side port/boundary;
6. adapter location, when an adapter is necessary;
7. conformance/integration evidence for that exact pin;
8. update and rollback procedure.

## Source-of-truth rule

The upstream repository is the only original for upstream behavior.

A consumer MUST NOT copy the upstream implementation merely for convenience.
Documentation excerpts, protocol schemas intentionally distributed for
interoperability, generated clients, or fixtures are allowed only when their
role is explicit and licensing permits it.

## Pin rule

Production/reproducible integration uses an immutable commit SHA or immutable
release digest.

A floating branch such as `main` is discovery input, not an accepted pin.

## Port rule

The consumer depends on a capability port owned by the consumer, not on upstream
storage internals or implementation details.

An adapter translates the consumer port into the upstream public contract.

## Update rule

Updating an adopted tool is an explicit operation:

`discover upstream change -> select candidate SHA -> run compatibility/conformance -> record evidence -> update pin`

The consumer is free to remain on the previous accepted SHA.

## Fork rule

A local fork is not an adoption update.

A fork requires the wider evolution protocol gate: reproducible limitation,
configuration/extensions exhausted, upstream contribution considered,
maintenance cost accepted, and compatibility tests.

## First canonical case

`Tools/EVOLUTION/ADOPTIONS/001-IDEOS-MYTRUES.md`

records IDEOS consuming MyTrues through `DecisionMemory`.
