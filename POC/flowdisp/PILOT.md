# FlowDisP Portable Pilot

## Goal

Test this protocol inside an unrelated project and return enough evidence to evaluate both the research result and defects in FlowDisP itself.

## Choose a real bounded claim

Prefer a claim whose answer the operator does not already know.

Examples of form:

```text
PRODUCT:
"We believe capability X does not already exist in a materially equivalent antecedent."

ACADEMIC:
"We believe concept/method X is a new contribution."

METHOD:
"We believe this decision protocol has no materially equivalent antecedent."
```

Do not use “our whole product is unique”.

## Required experiment

1. `fldp.py init`
2. Complete `CASE.md` before research.
3. Preserve initial raw HTML/MD/TXT if that is what exists.
4. Launch ABR-001 with the generated prompt.
5. Do not give the ABR a desired conclusion.
6. Preserve the raw chat.
7. Review result as Discovery Owner.
8. Ask at least one follow-up if raw trace shows a material gap.
9. Use ABR-002 independently if the first result is surprising, strongly negative or fragile.
10. Close as `CONVERGED`, `CONTESTED`, `UNRESOLVED` or `INSUFFICIENT`.
11. Complete final Evidence Pack.
12. `fldp.py validate`
13. `fldp.py pack`

## Protocol observations

Record every moment where:

- ABR asks for information the template failed to supply;
- ABR misunderstands its role;
- owner cannot classify an antecedent;
- a profile searches the wrong source classes;
- evidence cannot be represented cleanly;
- owner needs a field/status not present;
- process forces unnecessary work;
- protocol makes an unsupported conclusion too easy.

These are protocol-learning outputs, not failures.

## What we will evaluate on return

- bounded-claim discipline;
- prevention of code-review drift;
- separation of existence/equivalence/fitness/disposition;
- whether raw preservation reveals caveats omitted in summaries;
- whether iterative rounds improve the boundary;
- whether independent replication changes conclusions;
- honesty of closure state;
- usefulness of Evidence Pack for downstream actors;
- missing fields/states;
- redundant steps.
