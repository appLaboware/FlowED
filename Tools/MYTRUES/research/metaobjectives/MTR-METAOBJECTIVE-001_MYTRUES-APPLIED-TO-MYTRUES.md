# MTR-METAOBJECTIVE-001 — MYTRUES APPLIED TO MYTRUES

**Type:** Prior Research / Metaobjective Record  
**Audience:** MyTrues team  
**Authority:** PO conceptual direction  
**Status:** RECORD ONLY — NOT A DEMAND  
**Execution authorization:** NONE  
**Implementation authorization:** NONE  
**Purpose:** Preserve a research direction that future demands may operationalize.

---

# 0. IMPORTANT GOVERNANCE NOTE

This document is **not a development demand**.

It does not authorize the team to:

- select a final architecture;
- implement a production MyTrues;
- factor a new component;
- replace prior adoption-first studies;
- promote hypotheses to scientific claims;
- treat the architecture described here as canonical.

It records a **metaobjective**:

> Use MyTrues' own central idea — accumulated experience replacing repeated uncertain reasoning — to experimentally discover how MyTrues itself should organize, retrieve, relate and use memory.

The controlling attitude is:

> **Do not choose what appears most intelligent. Materialize alternatives, observe consequences, retain the experience, and let accumulated evidence progressively reduce the unknown space.**

---

# 1. RECURRING REFERENCE EXAMPLE — THE TIC-TAC-TOE SQL EXPERIMENT

This experiment must become a recurring conceptual reference inside the MyTrues project.

For shorthand, this document calls it:

# `SQLDAVELHA`

The important point is not tic-tac-toe itself.

The important point is the computational principle demonstrated by the experiment.

## 1.1 Original idea

A deliberately "dumb" tic-tac-toe implementation can avoid repeatedly calculating strategy if it first materializes game experience.

Conceptually:

```text
possible game sequences
        ↓
observed/final outcomes
        ↓
persistent SQL records
```

At decision time, instead of asking:

```text
"What is mathematically the best move?"
```

the program can ask the database something equivalent to:

```text
"Among previously materialized continuations compatible
with the moves already played, which continuation reaches
a winning result?"
```

The program then chooses the next recorded move in such a continuation.

The important conceptual characteristics are:

```text
NO minimax required at decision time
NO heuristic strategy required
NO probabilistic intelligence required
NO natural-language model required
NO understanding of tic-tac-toe required
```

The mechanism is approximately:

```text
CURRENT STATE
    ↓
DETERMINISTIC LOOKUP
    ↓
KNOWN EXPERIENCES
    ↓
KNOWN CONSEQUENCES
    ↓
SELECT NEXT ACTION
```

Once enough of the relevant possibility space has been materialized, the system can stop "thinking again" about already known situations.

## 1.2 The principle extracted from SQLDAVELHA

The recurring MyTrues hypothesis is:

> **When the function is unknown or expensive to recompute, useful parts of its domain may be materialized experimentally and persisted as context → action → observed consequence.**

Or more compactly:

> **Exchange repeated intelligence for accumulated experience.**

This does not imply that every real-world domain is finite or enumerable like tic-tac-toe.

The experiment is a reference model, not a proof of universal applicability.

Its role is to keep one question permanently visible:

> **What can stop being inferred once enough relevant experience has been accumulated?**

---

# 2. METAOBJECTIVE

The MyTrues team should keep the following long-term experiment in sight:

> Build a small, controlled "microbrain" in which knowledge is stored as structured memory and answers are produced by a deterministic systematic mechanism rather than by knowledge contained in an LLM's training.

Then use controlled experiments to alter the organization of that memory and observe which organizations produce better answers.

The system itself becomes an experimental object.

The intended loop is:

```text
candidate cognitive organization
        ↓
load controlled memory
        ↓
ask questions with known gold answers
        ↓
deterministic answer mechanism
        ↓
measure result
        ↓
store:
configuration → observed consequence
        ↓
use accumulated results
to choose the next experiments
```

This is:

# `MYTRUES APPLIED TO MYTRUES`

---

# 3. THE FIRST CONTROLLED MACHINE

The first useful experimental machine should be intentionally small.

A provisional name is:

# `MYTRUES-MICROBRAIN`

Its purpose is **not** to be the product.

Its purpose is to become an instrument for discovering the product.

Conceptually:

```text
                  REAL INPUT
                      │
                      ▼
             ┌──────────────────┐
             │ SEMANTIC REGISTRAR│
             │ LLM may assist   │
             └────────┬─────────┘
                      │
              candidate memories
              candidate relations
                      │
                      ▼
             ┌──────────────────┐
             │   MEMORY MESH    │
             │ structured state │
             └────────┬─────────┘
                      │
                      ▼
QUESTION ───► ┌──────────────────┐
              │ SYSTEMATIC AGENT │
              │ deterministic    │
              └────────┬─────────┘
                       │
                structured answer
                       │
                       ▼
              ┌──────────────────┐
              │ LANGUAGE RENDERER│
              │ LLM may assist   │
              └──────────────────┘
```

Around this machine:

```text
               EXPERIMENT ENGINE
                       │
                       ▼
        changes controlled variables
                       │
                       ▼
                 GOLD EVALUATOR
                       │
                       ▼
 configuration → observed consequence
```

---

# 4. CRITICAL BOUNDARY — WHAT THE LLM MAY DO

The LLM remains useful.

But its role must be sharply separated from epistemic authority.

## 4.1 LLM role A — understand language

Example input:

```text
"Depois de dar Ctrl- cinco vezes,
a captura trouxe só 18 partes."
```

An LLM may propose that this refers to:

```text
ACTION:
browser zoom-out / Ctrl-minus x5

CONTEXT:
chat capture

OUTCOME:
18 captured turns
```

This is semantic interpretation.

## 4.2 LLM role B — propose possible synapses

Suppose the database already contains:

```text
A17 = Ctrl-minus x5
K08 = large ChatGPT conversation
O31 = incomplete capture
E44 = previous zoom experiment
```

The LLM may propose:

```text
new experience EXECUTED A17
new experience UNDER_CONTEXT K08
new experience RESULTED_IN O31
new experience RELATED_TO E44
```

These are **candidate relations**.

The LLM may help because its training contains enormous amounts of general semantic knowledge.

For example, it may recognize that:

```text
apple
maçã
fruit
fruta
food
alimento
Granny Smith
```

belong to a dense semantic neighborhood even when the local MyTrues database has not yet explicitly connected every term.

This makes an LLM useful as a **candidate synapse discoverer**.

## 4.3 What the LLM must not do

The LLM must not automatically convert:

```text
CandidateRelation
```

into:

```text
CanonicalRelation
```

And it must not answer a factual question merely because its pretrained model "knows" the likely answer.

The desired boundary is:

```text
LLM
= interpretation + candidate association + language

MYTRUES MEMORY + SYSTEMATIC AGENT
= epistemic content of the answer
```

A useful control sentence is:

> **The LLM may propose where a memory might connect. It does not get to decide that the connection is true.**

---

# 5. WHY A "RINHA" OF LLMS MAY BE USEFUL

A future ingestion experiment may intentionally ask multiple independent LLMs to propose connections for the same new memory.

Example:

Input:

```text
"Depois de diminuir bastante a página,
consegui capturar toda a sessão."
```

Possible candidates:

```text
LLM A:
browser_zoom
capture_complete

LLM B:
CtrlMinus
viewport_size
capture_success

LLM C:
zoom_out
visible_content
successful_outcome
```

The system performs a union:

```text
browser_zoom
CtrlMinus
zoom_out
viewport_size
visible_content
capture_complete
capture_success
```

This does **not** make the union true.

It increases semantic recall.

A later mechanism can:

- find existing identities;
- compare lexical candidates;
- compare vector candidates;
- inspect graph neighborhood;
- apply context;
- inspect provenance;
- validate deterministic constraints;
- request human authority where required.

Therefore:

> **The LLM rinha is a candidate-synapse generator, not a truth engine.**

---

# 6. THE MEMORY MESH

The first controlled memory does not need the final ontology.

A minimal experimental starting point may contain objects such as:

```text
ENTITY
EXPERIENCE
CONTEXT
ACTION
OUTCOME
CLAIM
POSITION
```

and relations such as:

```text
IS_A
PART_OF

UNDER_CONTEXT
EXECUTED
RESULTED_IN

SUPPORTS
ATTACKS
DEFEATS
SUPERSEDES

DERIVED_FROM
```

Temporal fields may progressively include:

```text
event_time
known_time
considered_time
decision_time
recorded_time
valid_from
valid_until
```

This list is experimental, not canonical.

Every future mechanism discovered by prior-art research may become a variable.

---

# 7. SIMPLE CONTROLLED EXAMPLE — RELATIONAL KNOWLEDGE

Memory:

```text
GrannySmith IS_A Apple
Apple       IS_A Fruit
Fruit       IS_A Food
```

Question:

```text
Is Granny Smith food?
```

The answer mechanism does not need an LLM to know the answer.

It traverses:

```text
GrannySmith
    ↓ IS_A
Apple
    ↓ IS_A
Fruit
    ↓ IS_A
Food
```

Structured result:

```text
YES
PATH = GrannySmith → Apple → Fruit → Food
```

This tests deterministic relational inference.

---

# 8. CONTROLLED EXAMPLE — CONTEXT

Memory:

```text
Tomato IS_A Fruit
CONTEXT = botanical

Tomato IS_A Vegetable
CONTEXT = culinary
```

Question:

```text
Is tomato a fruit?
```

Desired systematic result:

```text
CONTEXT_DEPENDENT
```

Question:

```text
Botanically, is tomato a fruit?
```

Desired result:

```text
YES
```

The system must not flatten contextual knowledge into one global answer.

---

# 9. CONTROLLED EXAMPLE — CHANGING POSITION

At T1:

```text
E1:
strategy A captured 69/70 turns

P1:
strategy A = BEST_OBSERVED
```

Later:

```text
E2:
strategy B captured 70/70 turns
```

Then:

```text
P2 SUPERSEDES P1
```

Question:

```text
What is the best known strategy now?
```

Answer:

```text
P2
```

Question:

```text
What was the best known strategy before E2 became known?
```

Answer:

```text
P1
```

Question:

```text
Why did the position change?
```

Answer path:

```text
E2
 ↓
defeated/superseded prior best
 ↓
P2
```

No previous state is deleted.

---

# 10. CONTROLLED EXAMPLE — A DEFEATED IDEA RETURNS IN ANOTHER CONTEXT

Experience 1:

```text
ACTION:
Ctrl-minus x5

CONTEXT K1:
UI version A
large conversation
capture algorithm X

OUTCOME:
18/70
```

State:

```text
Ctrl-minus x5
KNOWN_DEFEATED
UNDER K1
```

Later:

```text
ACTION:
Ctrl-minus x5

CONTEXT K2:
UI version B
capture algorithm Y

OUTCOME:
70/70
```

The system must not answer:

```text
"Ctrl-minus works."
```

or:

```text
"Ctrl-minus does not work."
```

It should derive something like:

```text
CONTEXT_DEPENDENT

K1 → defeated
K2 → successful
```

This tests whether the mesh can preserve contextual defeat without false universalization.

---

# 11. SYSTEMATIC AGENT

The systematic agent is not intended to be an autonomous LLM agent.

It is closer to:

> **a deterministic query-and-reasoning machine over the registered memory.**

For a question such as:

```text
"Should we use Ctrl-minus?"
```

an LLM may transform language into a structured query:

```text
intent = evaluate_action
action  = A17
context = K...
```

The systematic agent then executes a fixed routine such as:

```text
1. resolve identity
2. retrieve matching contexts
3. retrieve relevant Experiences
4. retrieve Outcomes
5. retrieve Defeaters
6. apply temporal validity
7. find current governing Position
8. derive epistemic state
9. return evidence paths
```

Example structured answer:

```json
{
  "action": "A17",
  "state": "KNOWN_DEFEATED",
  "context_match": "HIGH",
  "experiences": 3,
  "best_observed_alternative": "A22",
  "limitations": [
    "not a universal statement"
  ]
}
```

Only after this result exists may a language model verbalize it.

---

# 12. LANGUAGE RENDERER

A language model can transform:

```text
KNOWN_DEFEATED
context_match = HIGH
better alternative = A22
```

into natural language.

But it must not create new epistemic content.

The governing rule is:

> **The LLM may transform representation, never epistemic state.**

Or:

```text
MyTrues = WHAT MAY BE CLAIMED
LLM     = HOW TO SAY IT
```

---

# 13. OPTIONAL CLAIM CHECKER

A future controlled experiment should test whether the renderer can be constrained by a deterministic post-check.

Suppose the renderer adds:

```text
"The failure was caused by DOM virtualization."
```

If the structured result did not authorize that causal claim:

```text
UNSUPPORTED CLAIM
        ↓
REJECT / REGENERATE
```

This is another experimental variable, not yet a required architecture.

---

# 14. GOLD QUESTION SET

The microbrain should operate over controlled questions whose expected answers are known independently of the tested mechanism.

Examples:

```text
Q1:
Is Granny Smith food?
GOLD = YES

Q2:
Is tomato a vegetable?
GOLD = CONTEXT_REQUIRED

Q3:
What was the governing position before E2?
GOLD = P1

Q4:
What is the governing position now?
GOLD = P2

Q5:
Has Ctrl-minus failed under K1?
GOLD = YES

Q6:
Does that prove Ctrl-minus always fails?
GOLD = NO

Q7:
Did zoom alone cause the failure?
GOLD = UNKNOWN

Q8:
Which experience supports the current position?
GOLD = E2
```

No LLM judgment should be needed to score these questions.

---

# 15. EXPERIMENT ENGINE

The experiment engine changes the cognitive organization and measures consequences.

Example only:

```text
C0001

representation = graph
context = off
temporal = off
defeaters = off
vector = off
activation = off
```

Run gold questions:

```text
score = 63/100
```

Next:

```text
C0002

same as C0001
context = on
```

Result:

```text
score = 74/100
```

Next:

```text
C0003

same as C0002
temporal = on
```

Result:

```text
score = 82/100
```

These numbers are examples only.

No expected improvement is assumed.

A mechanism may improve, worsen, have no effect, improve one class while harming another, or interact only with another mechanism.

All are useful observations.

---

# 16. CANDIDATE EXPERIMENTAL VARIABLES

The prior Discovery work has already found a broad candidate space involving mechanisms such as:

```text
graph representation
symbolic representation
vector representation
hybrid representation

episodic memory
semantic memory
case memory
working memory

lexical retrieval
vector retrieval
graph traversal
case-based retrieval
spreading activation
hybrid retrieval

context filtering
context weighting
assumption sets

temporal models
bitemporal models
cognitive-time models

append-only revision
supersession
belief revision
TMS
ATMS

argumentation
defeaters

recency
frequency
salience
inhibition
forgetting
consolidation
replay

single embedding
multi-vector representations

edge typing
edge weighting
directionality

decision rules
case-based decision
argument-based decision
utility-based methods
hybrids
```

None is promoted by this document.

They are experimental candidates.

---

# 17. FROM COGNITIVE DESIGN SPACE TO SQLDAVELHA

Once the microbrain exists, each tested configuration becomes analogous to a tic-tac-toe continuation.

Instead of:

```text
board state
→ move
→ win/loss
```

MyTrues records:

```text
dataset/context
+
cognitive configuration
+
question set
        ↓
observed performance
```

Example:

```text
Configuration C015
Dataset D01
Questions Q001..Q100

Observed:
94/100
failures = [Q12, Q31, Q77, ...]
```

Then:

```text
Configuration C016

Difference:
activation_decay =
    exponential → linear

Observed:
96/100
```

This creates a new MyTrues Experience:

```text
CONTEXT:
D01 + benchmark conditions

ACTION:
use configuration C016

OBSERVED CONSEQUENCE:
96/100
```

The next experiment can consult accumulated results.

This is the dogfooding loop:

```textMyTrues
learns from experience
about how MyTrues should be built.
```

---

# 18. DEEPER DOGFOODING GOAL

Eventually the experimental system should be able to distinguish:

```text
UNKNOWN CONFIGURATION
```

from:

```text
KNOWN_DEFEATED CONFIGURATION
```

from:

```text
BEST_OBSERVED SO FAR
```

from:

```text
CONTEXT_DEPENDENT
```

and use this history to avoid repeating defeated experiments unless there is:

```text
MATERIAL NEW EVIDENCE
```

At that point, the research process itself begins to exhibit the MyTrues principle.

---

# 19. WHAT MUST REMAIN DETERMINISTIC

The controlled experiment should progressively maximize deterministic surfaces.

Candidates include:

```text
schema validation
identity resolution rules
graph traversal
temporal filtering
context filtering
supersession
defeater application
constraint checking
gold scoring
configuration generation
experiment logging
provenance
answer structure
claim support validation
```

The goal is not "remove every LLM."

The goal is:

> **use probabilistic intelligence where approximation is useful, and deterministic machinery where epistemic repeatability is required.**

---

# 20. WHAT MAY REMAIN PROBABILISTIC

Candidate LLM roles include:

```text
natural-language understanding
entity/relation candidate discovery
semantic normalization proposals
candidate analogy
candidate context extraction
candidate synapse generation
human-oriented explanation
```

These should preferably emit proposals with provenance, not silently mutate epistemic authority.

---

# 21. META-RESEARCH QUESTION

The deepest experimental question is not:

```text
"Can a deterministic system answer every question?"
```

It is:

> **How far can systematic deterministic use of accumulated structured experience replace repeated probabilistic cognition before new intelligence is actually necessary?**

A second question follows:

> **Which organization of memory most efficiently enables that substitution?**

And a third:

> **Which parts of the remaining unknown space benefit from LLM intelligence, and which parts become deterministic once enough experience is materialized?**

---

# 22. SUCCESS WOULD NOT MEAN "WE BUILT A BRAIN"

This work must avoid biological overclaiming.

Even if the system becomes highly effective, the correct statement is not:

```text
"We reproduced human cognition."
```

The defensible statement would be closer to:

```text
"We experimentally identified memory organizations
and deterministic retrieval/revision mechanisms
that improve performance on defined classes
of longitudinal, relational and contextual knowledge tasks."
```

Any stronger scientific claim requires independent evidence.

---

# 23. NEAR-TERM RESEARCH TARGET

A future authorized demand may instantiate:

# `MYTRUES-MICROBRAIN-V0`

A deliberately minimal candidate:

```text
Python
SQLite
controlled schema
controlled fixture
50–100 gold questions
deterministic systematic agent
deterministic evaluator
experiment runner
no LLM knowledge inside answer engine
```

Then experimental layers may be added progressively:

```text
V0
 ↓
+ context
 ↓
+ temporal semantics
 ↓
+ defeaters
 ↓
+ richer graph relations
 ↓
+ case-based memory
 ↓
+ vector candidate retrieval
 ↓
+ spreading activation
 ↓
+ TMS / ATMS
 ↓
+ other mechanisms discovered by research
 ↓
+ combinations
```

This sequence is illustrative only.

The experiment may deliberately vary ordering and combinations.

---

# 24. FINAL METAOBJECTIVE

The team should preserve the following as the intended long-range research loop:

```text
DISCOVERY
find what humanity has already imagined/tested
        ↓
DESIGN SPACE
turn mechanisms into variables and constraints
        ↓
MICROBRAIN
build the smallest controlled experimental memory
        ↓
SQLDAVELHA ENGINE
systematically vary configurations
        ↓
GOLD EVALUATION
measure deterministic answers
        ↓
EXPERIENCE
configuration → observed consequence
        ↓
MYTRUES
retain what happened
        ↓
NEXT EXPERIMENT
avoid defeated paths / explore unknown frontier
        ↓
repeat
```

The core recurring example remains:

# `SQLDAVELHA`

because it captures the principle in its simplest form:

> **Do not repeatedly solve what experience has already made queryable.**

And the dogfooding version is:

> **Do not repeatedly guess how MyTrues should work when MyTrues can experimentally accumulate evidence about how MyTrues works.**

---

# 25. STATUS

```text
METAOBJECTIVE = RECORDED
DEMAND = NONE
IMPLEMENTATION = NOT AUTHORIZED
ARCHITECTURE = NOT SELECTED
SCIENTIFIC CLAIM = NOT PROMOTED
NEXT ACTION = WAIT FOR FUTURE PO DEMAND
```