# X14 — Factorized Human-Dyad sampling taxonomy red team

**Status:** RESEARCH_CANDIDATE / architecture red-team input  
**As of:** 2026-09-28  
**Authority:** Round-3 READY lane X14  
**Target reviewed:** PR #33 @ `83ff2e3436260f70e381b1aff7e6060d65142753`  
**Related evidence:** PR #37 @ `391c8b9e7476febf45c2794a3d872e139dbf5aa6`

---

## 1. Red-team question

Can the proposed Human-Dyad sampling taxonomy represent overlapping real cases without:
- forcing one person-pair into a single mutually exclusive mega-enum;
- double-counting one source as independent coverage of many “cells”;
- confusing demographic composition, relationship role, temporal stage, and context;
- making a benchmark impossible to reason about?

The current PR #33 already names three dimensions:
`dyad_class · gender_composition · stage`,
but Table A still flattens examples from all three dimensions plus context into peer rows.

**Verdict:** the flat Table-A cell list fails this red team. The underlying idea survives if the taxonomy is factored.

---

## 2. Required factorization

Recommended record:

```text
HumanDyadSampleContext =
{
  relation_classes: set<RelationClass>,
  gender_composition,
  relationship_stage,
  context_flags: set<ContextFlag>,
  role_asymmetry,
  source_ref,
  unit_ref,
  provenance
}
```

### 2.1 `relation_classes` must be multi-valued

Do not force a pair to have exactly one relationship class.

Minimum current vocabulary may include:
- `KIN_SIBLING`
- `KIN_PARENT_ADULT_CHILD`
- `KIN_OTHER_ADULT`
- `FRIEND_NONROMANTIC`
- `ROMANTIC_PARTNER`
- `EX_PARTNER`
- `PROFESSIONAL_COOPERATIVE`
- `CAREGIVING`
- `ADVERSARIAL`

A dyad may carry multiple simultaneous classes.

### 2.2 `gender_composition` is orthogonal

```text
SAME_SEX | MIXED_SEX | UNDECLARED
```

This is never a relation class.

### 2.3 `relationship_stage` is orthogonal

A minimum usable stage axis is:

```text
STRANGER_OR_PRE_RELATION
FORMING
ESTABLISHED
TRANSITIONING_OR_UNSTABLE
POST_TERMINATION
UNDECLARED
```

Do not treat “stranger start”, “established long-duration”, or “ex” as mutually interchangeable categories.  
`EX_PARTNER` may remain a relation-history class for querying, while `POST_TERMINATION` records temporal stage.

### 2.4 `context_flags` are multi-valued

Examples:
- `THIRD_PARTY_PRESENT`
- `CO_PARENTING`
- `SHARED_HOUSEHOLD`
- `LEGAL_OR_INSTITUTIONAL_CONSTRAINT`
- `RESOURCE_DEPENDENCE`
- `CARE_NEED_PRESENT`
- `CONFLICT_ACTIVE`
- `GEOGRAPHIC_DISTANCE`
- `BEREAVEMENT`
- `MIGRATION`
- `ILLEGAL_OR_NONCONFORMING_STRUCTURE`

These are not dyad classes.

---

## 3. Stress cases

### Case A — sibling + caregiving

Example shape:
- adult siblings;
- one sibling becomes primary caregiver after illness/disability;
- both remain kin;
- role asymmetry can become strong;
- shared resources/institutional obligations may appear.

Correct encoding:

```text
relation_classes = { KIN_SIBLING, CAREGIVING }
gender_composition = SAME_SEX | MIXED_SEX | UNDECLARED
stage = ESTABLISHED
context_flags = { CARE_NEED_PRESENT, maybe RESOURCE_DEPENDENCE }
role_asymmetry = DIRECTIONAL
```

**Flat-enum failure:** forcing the dyad into either “sibling” or “caregiving” loses a real dimension and makes coverage accounting misleading.

### Case B — romantic + professional/cooperative

Examples include cofounders, colleagues, artistic collaborators, or business partners who are also romantic partners.

```text
relation_classes = { ROMANTIC_PARTNER, PROFESSIONAL_COOPERATIVE }
stage = ESTABLISHED
context_flags = { maybe SHARED_HOUSEHOLD, LEGAL_OR_INSTITUTIONAL_CONSTRAINT }
```

**Flat-enum failure:** “romantic” and “professional” are not mutually exclusive; treating them as separate cells can falsely count one source twice as independent cross-context evidence.

### Case C — ex-partner + co-parenting

```text
relation_classes = { EX_PARTNER }
stage = POST_TERMINATION
context_flags = { CO_PARENTING, LEGAL_OR_INSTITUTIONAL_CONSTRAINT }
```

The relationship is no longer current-romantic, but the dyad remains active through shared obligations and repeated interaction.

**Flat-enum failure:** if “ex-partner” is only a stage, the continuing co-parenting role disappears; if it is only a dyad class, termination timing disappears.

### Case D — same-sex + friendship / romance

PR #37 already supplies an empirical warning: one sibling source contains both same-sex and mixed-sex sibling dyads; another friendship study contains both same- and mixed-gender friendship dyads.

Correct bookkeeping is **per dyad/unit**, not per article:

```text
relation_classes = { FRIEND_NONROMANTIC } OR { ROMANTIC_PARTNER }
gender_composition = SAME_SEX
stage = ESTABLISHED
```

**Flat-enum failure:** “same-sex core dyad” as a peer row to “friendship” or “romance” causes cross-axis double counting.

### Case E — romantic + third party

Affair/triangle or poly-context examples:

```text
core_query_dyad = (A,B)
relation_classes = { ROMANTIC_PARTNER }
context_flags = { THIRD_PARTY_PRESENT }
linked_context_entities = { C }
```

The project may retain HumanDyad as the query unit while referencing a third person in Environment/History/linked context.

**Flat-enum failure:** “third party present” is not a dyad type.

### Case F — adversarial + kin / ex / professional

Conflict can occur inside nearly every relation class.

```text
relation_classes = { KIN_SIBLING, ADVERSARIAL }
# or { EX_PARTNER, ADVERSARIAL }
# or { PROFESSIONAL_COOPERATIVE, ADVERSARIAL }
context_flags = { CONFLICT_ACTIVE }
```

Whether `ADVERSARIAL` should itself remain a relation class or be reduced to a context/process axis is still open. The red team only establishes that it cannot be assumed mutually exclusive with the other classes.

---

## 4. Coverage accounting rule

A benchmark must not compute “15/15 contexts passed” by treating all axis values as independent peer cells.

Instead maintain separate coverage matrices.

### Matrix A — relation-class coverage
Counts independent benchmark units for each relation class.

### Matrix B — composition coverage
Same-sex / mixed-sex / undeclared, with source dependence recorded.

### Matrix C — temporal-stage coverage
Pre/formation/established/transition/post-termination.

### Matrix D — context-flag stress coverage
Third-party, co-parenting, care need, institutional constraints, etc.

A single source/unit may populate multiple matrices, but must carry the same `source_ref` so independence accounting can see that those observations are **not independent evidence**.

---

## 5. Gate semantics implication

For `GATE_CROSS_CONTEXT`, the test should not require the Cartesian product of all axes.

That would explode combinatorially and create an impossible pass condition.

Recommended rule:
1. every **required marginal axis value** must have at least one lawful independent benchmark instance;
2. predefined **high-risk interactions** must be tested explicitly;
3. untested interactions remain `NOT_RUN`, but do not imply that every Cartesian combination is mandatory.

Initial high-risk interactions:
- `KIN_SIBLING × CAREGIVING`;
- `ROMANTIC_PARTNER × PROFESSIONAL_COOPERATIVE`;
- `EX_PARTNER × CO_PARENTING`;
- `SAME_SEX × FRIEND_NONROMANTIC`;
- `SAME_SEX × ROMANTIC_PARTNER`;
- `ROMANTIC_PARTNER × THIRD_PARTY_PRESENT`;
- any relation class × `ADVERSARIAL/CONFLICT_ACTIVE`.

This preserves falsifiability without demanding an unbounded benchmark.

---

## 6. Required repair to PR #33

The current `HD-A01…HD-A15` flat peer list should be replaced by:
- a factor vocabulary table;
- independent per-axis coverage tables;
- an interaction-stress table;
- source-dependence/provenance fields.

Specific remapping:
- sibling / parent-adult-child / other kin / friendship / romance / professional / caregiving -> `relation_classes`;
- same-sex / mixed-sex -> `gender_composition`;
- stranger start / established long duration / post-termination -> `relationship_stage`;
- third-party / illegal or nonconforming / conflict-like context -> `context_flags` or explicit orthogonal context axes;
- `harm-asymmetric` remains outside sampling class and belongs to directionality/asymmetry metadata.

---

## 7. Final X14 packet

### VERIFIED_FACTS
- PR #33 currently declares a multi-dimensional taxonomy but Table A still flattens values from different dimensions into one peer-cell list.
- PR #37 already demonstrates sources whose individual dyads differ on gender composition within the same relationship class.
- Real Human Dyads can simultaneously occupy multiple relationship roles.

### NEGATIVE_RESULTS
- A single mutually exclusive `dyad_class` enum is insufficient.
- A Cartesian-product requirement across every possible axis is also unsuitable.

### OPEN_GAPS
- Whether `ADVERSARIAL` is best modeled as a relation class, process state, or context flag.
- The minimum required high-risk interaction set should remain versioned and empirically driven.

### ARCHITECTURE_IMPLICATIONS
- Repair `HD-ST-1` before integration.
- Make relation class multi-valued.
- Separate composition, stage, and context.
- Preserve source dependence when one material covers several axes.

### NON_CLAIMS
- This red team does not expand LHRM beyond the HumanDyad query unit.
- It does not claim every possible role combination needs a benchmark.
- It does not establish population prevalence.

### SOURCE_POINTERS
- PR #33 exact head `83ff2e3436260f70e381b1aff7e6060d65142753`
- PR #37 exact head `391c8b9e7476febf45c2794a3d872e139dbf5aa6`
