# X04 — Construct-bearing ablation benchmark population v0.1

**Status:** RESEARCH_CANDIDATE / DESIGN + POPULATION PLAN / NOT FROZEN / NOT RUN  
**As of:** 2026-09-28  
**Authority:** `youling/lhrm#30` Round-3 exploration queue X04  
**Base branch:** `research/round3-exploration-v0.1` from `main@ee393ca24f9fbf738ac0ed839e99bdc99de6fc3a`  
**Scope:** Populate a construct-bearing benchmark that can actually test necessity of the eight directed candidates without reusing Fixture 001 outcome knowledge.  
**Non-claims:** no construct is validated; no Gate is executed; no fixture is frozen; no rights-restricted source is introduced; no canonical mutation.

---

## 1. Executive verdict

The current benchmark gap is not “we need more relationship stories”. It is:

> We need units whose **information content is deliberately capable of separating the eight directed candidates**, and we need a predeclared prediction about what should break when one candidate is withheld.

A single naturalistic corpus cannot guarantee this. The benchmark should therefore have **two layers**:

1. **Controlled decoupling layer** — repo-native synthetic vignettes written and frozen *before* mapping, with hidden expected construct-bearing labels and explicit nearest-neighbor contrasts.
2. **Naturalistic realism layer** — public-domain/stable source candidates used only to test whether the controlled distinctions survive less curated language.

The controlled layer is the actual `GATE_MINIMALITY / ARM-ABL-1` population.  
The naturalistic layer is a stress test against overfitting the synthetic wording.

Synthetic cases are **not empirical evidence that the constructs exist in populations**. They are a mechanical test of whether the proposed representation can express predeclared distinctions without collapsing them.

---

## 2. Anti-circularity protocol

The benchmark must not be tuned to a mapper’s failures.

Required order:

```text
A. freeze candidate basis and construct definitions
B. freeze vignette text + hidden expected-bearing metadata
C. freeze nearest-neighbor adversarial pairings
D. hand only vignette text to mapper/verifier
E. run full-basis mapping
F. rerun with one construct withheld
G. reveal expected-bearing metadata
H. compare failure/degradation signatures
```

Forbidden:
- rewriting a vignette after seeing a mapping result;
- adding a construct because one synthetic case was hard;
- declaring necessity merely because the generator intended a construct;
- allowing the mapper to see the hidden target labels;
- counting a synonym as a construct-bearing success if the information is actually represented elsewhere losslessly.

A withheld construct is only “necessary for this case” if the remaining schema cannot preserve the same information without:
- `MAPPING_FAILURE`,
- materially weaker / less specific representation,
- illegal layer migration,
- or semantic distortion into a nearest-neighbor construct.

---

## 3. Controlled layer — 24-case minimum population

Each directed candidate gets:
- **2 positive-bearing cases**;
- **1 adversarial/decoupling case** against the nearest plausible neighbor.

Case IDs are design IDs only. Final fixture text should be generated once, reviewed for ambiguity, then frozen by exact commit.

### D1 — Liking / Affiliative Valence

**D1-P1 — warm friendship, no romance/sex**  
A consistently seeks B’s company, enjoys B’s presence, and speaks warmly of B, while explicitly lacking romantic or sexual interest.

**D1-P2 — sibling affection without partner framing**  
A has enduring affection and positive regard toward sibling B despite frequent disagreement and no partner-like framing.

**D1-A1 — romantic fascination with low liking**  
A strongly wants B as a romantic partner but finds B irritating and does not generally enjoy B’s company.

**Nearest-neighbor attack:** D2 RomanticAttraction.

**Withheld-D1 expected signal:** the positive-valence information should not be recoverable by D2/D3 alone; a correct system should not relabel non-romantic affection as romance.

---

### D2 — Romantic Attraction

**D2-P1 — partner-specific courtship orientation**  
A wants B specifically as a romantic partner and seeks couple-forming interaction, without relying on sexual content.

**D2-P2 — enduring romantic attachment after long separation**  
A continues to desire a romantic union with B after years apart despite low current interaction frequency.

**D2-A1 — sexual desire without romantic intention**  
A wants sexual contact with B but explicitly does not want courtship, couple identity, or romantic partnership.

**Nearest-neighbor attack:** D3 SexualDesire, secondarily D1 Liking.

**Withheld-D2 expected signal:** partner-forming romantic orientation should degrade or be forced into D1/D3, which is a semantic loss.

---

### D3 — Sexual Desire

**D3-P1 — sexual approach without relationship intention**  
A has recurring sexual desire toward B but does not seek romance or long-term relationship maintenance.

**D3-P2 — sexual desire inside established partnership**  
A reports strong desire for sexual contact with long-term partner B independent of current relationship satisfaction.

**D3-A1 — romantic attraction with no sexual desire**  
A strongly wants B as a romantic partner while explicitly reporting no sexual desire toward B.

**Nearest-neighbor attack:** D2 RomanticAttraction.

**Withheld-D3 expected signal:** sexual motivation must not be silently recoded as romance, liking, or Action/Event.

---

### D4 — Trust

**D4-P1 — vulnerability disclosure**  
A shares information with B that could materially harm A if misused because A expects B not to exploit it.

**D4-P2 — delegated high-stakes reliance**  
A entrusts B with a consequential responsibility despite not particularly liking B, because A expects B to act reliably and non-exploitatively.

**D4-A1 — high liking, low trust**  
A greatly enjoys B and feels affection toward B but withholds sensitive information because A expects B may weaponize it.

**Nearest-neighbor attack:** D1 Liking; secondary attack against D5 AttachmentSecurity.

**Withheld-D4 expected signal:** vulnerability/non-exploitation expectation should not be representable merely as liking, attachment, or observed disclosure action.

---

### D5 — Attachment Security / Felt Security

**D5-P1 — safe-haven expectation under distress**  
When distressed, A expects B to be available and soothing and seeks B specifically for comfort.

**D5-P2 — secure-base expectation during separation/exploration**  
A undertakes a difficult independent task while confident that B remains available and supportive if needed.

**D5-A1 — competence trust without attachment security**  
A trusts B’s competence and honesty in practical matters but does not seek B for comfort and does not expect emotional availability.

**Nearest-neighbor attack:** D4 Trust.

**Withheld-D5 expected signal:** availability/safe-haven/secure-base semantics should degrade if represented only as generic trust or caregiving action.

---

### D6 — Caregiving Motivation / Care Orientation

**D6-P1 — sustained burden relief**  
A repeatedly reorganizes time and effort to reduce B’s suffering and burden, with no expectation of repayment.

**D6-P2 — protective care after relationship de-escalation**  
A no longer wants to maintain the former romantic relationship with B but still acts from a stable motive to protect B’s welfare.

**D6-A1 — dedication without caregiving motive**  
A strongly wants the relationship with B to continue but declines burdensome care and does not experience a sustained motive to protect or relieve B.

**Nearest-neighbor attack:** D7 Dedication.

**Withheld-D6 expected signal:** protective/welfare-oriented motivation should not be replaced by relationship-maintenance intention or by the caregiving Action itself.

---

### D7 — Dedication

**D7-P1 — voluntary maintenance despite exit opportunity**  
A has a low-cost opportunity to leave but chooses to preserve and invest in the relationship because A wants it to continue.

**D7-P2 — relationship repair intention**  
After conflict, A actively seeks repair because maintaining the relationship itself is an endorsed goal.

**D7-A1 — high dependence without dedication**  
A remains in the relationship because housing, finances, or legal constraints make leaving costly, while explicitly not wanting the relationship to continue.

**Nearest-neighbor attack:** D8 OutcomeDependence / Constraint.

**Withheld-D7 expected signal:** voluntary relationship-maintenance intention should not be representable merely as dependence, investment history, or external constraint.

---

### D8 — Outcome Dependence

**D8-P1 — livelihood dependence**  
A’s housing and basic financial stability materially depend on B even though A has low liking and low dedication.

**D8-P2 — access/opportunity dependence**  
A’s access to an important life opportunity is materially contingent on B or on continuation of the dyadic arrangement.

**D8-A1 — high affection/dedication with low dependence**  
A strongly likes B and wants the relationship to continue, while maintaining independent housing, income, social support, and viable alternatives.

**Nearest-neighbor attack:** D7 Dedication; structural alternative = Agent resources + Environment + Constraints.

**Withheld-D8 expected signal:** **no predetermined failure is required.** If the remaining schema losslessly represents the same dependency through resources, alternatives, constraints, and environment, that is legitimate evidence for `DERIVE`/redundancy rather than a failed benchmark.

This is deliberately asymmetric with D1–D7 because D8 already carries an explicit redundancy hypothesis in canonical candidate text.

---

## 4. Expected outcome schema

For each vignette and each withheld arm, record:

```text
{
  case_id,
  full_basis_mapping,
  withheld_construct,
  withheld_mapping,
  information_preserved: YES | PARTIAL | NO,
  mapping_failure: YES | NO,
  illegal_layer_migration: YES | NO,
  nearest_neighbor_substitution: NONE | <construct>,
  ambiguity_before_ablation: LOW | MEDIUM | HIGH,
  verifier_notes,
  disposition_evidence: KEEP | MERGE | DERIVE | REJECT | HOLD
}
```

The benchmark does **not** decide the final disposition automatically. It creates evidence for the Architect’s terminal decision.

---

## 5. Naturalistic realism layer — public-domain seed pool

These are **source candidates**, not yet fixture units. They are selected because Project Gutenberg currently marks the text editions below as **public domain in the USA** and supplies stable eBook identifiers.

| source | stable pointer | current rights signal | likely use in realism stress test |
|---|---|---|---|
| Jane Austen, *Pride and Prejudice* | Project Gutenberg eBook **1342** | Public domain in USA | liking vs romantic attraction; trust changes; courtship vs social constraint |
| Jane Austen, *Emma* | eBook **158** | Public domain in USA | friendship/liking vs romantic inference; mistaken beliefs about attraction |
| Jane Austen, *Persuasion* | eBook **105** | Public domain in USA | enduring romantic attraction, dedication, separation/history |
| O. Henry, *The Gift of the Magi* | eBook **7256** | Public domain in USA | caregiving/sacrifice/dedication; already familiar project material but useful only as a realism seed |
| Edith Wharton, *The Age of Innocence* | eBook **541** | Public domain in USA | romance vs duty/constraint; triangular social context |
| Louisa May Alcott, *Little Women* | eBook **514** | Public domain in USA | sibling liking/care; family obligations; non-romantic dyads |
| George Eliot, *Silas Marner* | eBook **550** | Public domain in USA | trust/betrayal, caregiving, attachment-like security, parent-child pair dynamics |

Current Project Gutenberg records explicitly mark these editions as public domain in the USA.  
Jurisdiction remains a real gate: Project Gutenberg itself notes that users outside the United States must check applicable local law.

**Important:** this seed pool does not imply that every D1–D8 construct is cleanly observable in every work. In particular:
- D3 SexualDesire is often indirect/euphemistic in older fiction;
- D8 OutcomeDependence may be representable structurally rather than as a latent state;
- fictional narrator claims are not empirical observations of real humans.

Naturalistic units must therefore be selected **after** the controlled layer is frozen, and selection criteria must be structural (dyad/context/rights/stability), not “find a passage that makes our favorite construct look necessary”.

---

## 6. Natural-source anti-leakage rule

A naturalistic unit is admissible only if the selector records, before mapping:

```text
source_id
exact edition / eBook id
chapter / stable local anchor
dyad
time/history context
rights snapshot
reason for inclusion independent of expected construct
```

Do **not** record an expected construct label in the mapper-visible packet.

A separate hidden key may record the selection hypothesis, but the result is allowed to refute it.

---

## 7. Relationship to PR #37

PR #37 already supplies:
- the ablation-arm concept;
- benchmark-gap source planning;
- rights/stability cautions;
- the distinction between corpus coverage and construct minimality.

X04 adds the missing **construct-bearing population plan**.

Therefore:
- do not create a second Gate SSOT here;
- do not copy `VALIDATION_GATES_V0_2.md`;
- do not treat PR #37 source counts as construct evidence;
- use X04 only to populate the minimality arm once the canonical Gate package is integrated and accepted.

---

## 8. Stop conditions before turning X04 into a fixture

Do not freeze or run the benchmark until all are true:

1. the eight candidate definitions being tested are pinned to an exact reviewed version;
2. #33/#34/#35 semantics are reconciled in the future integration head;
3. synthetic vignette text and hidden key are committed before any mapping run;
4. a fresh verifier confirms each synthetic case is not trivially label-leaking;
5. natural-source units have exact edition/anchor + current rights record;
6. mapper does not receive hidden expected-bearing labels;
7. #20/#21/#22 isolation remains untouched;
8. no rights-restricted source is smuggled in through a “publicly viewable” assumption.

---

## 9. Final X04 packet

### VERIFIED_FACTS
- Current canonical candidate basis contains eight directed constructs D1–D8.
- PR #37’s benchmark design identifies the need for construct-bearing ablation but does not itself provide a full per-construct 2-positive + 1-decoupling population.
- Project Gutenberg currently identifies the listed editions as public domain in the USA and provides stable eBook identifiers.

### NEGATIVE_RESULTS
- Fixture 001 cannot establish eight-construct necessity merely by being a successful representation fixture.
- A naturalistic corpus alone cannot guarantee balanced nearest-neighbor decoupling coverage.
- Synthetic success cannot validate prevalence, measurement validity, or causal importance of a construct.

### OPEN_GAPS
- exact frozen synthetic wording;
- independent ambiguity review;
- naturalistic unit selection and local anchors;
- whether D8 survives ablation or is losslessly derivable;
- whether any other D1–D7 construct also proves redundant under a lossless alternative representation.

### ARCHITECTURE_IMPLICATIONS
- Use controlled decoupling as the primary minimality arm.
- Use public-domain naturalistic material only as a realism stress test.
- Freeze expected failure signatures before mapping.
- Treat “withheld construct produces no information loss” as possible redundancy evidence, not as benchmark failure.

### NON_CLAIMS
- No construct is validated or frozen by this memo.
- No Gate was run.
- No fictional vignette is empirical evidence about population psychology.
- Public-domain status is edition/jurisdiction-specific and not a blanket rights claim for all copies.

### SOURCE POINTERS
- Project Gutenberg 1342, *Pride and Prejudice*: https://www.gutenberg.org/ebooks/1342
- Project Gutenberg 158, *Emma*: https://www.gutenberg.org/ebooks/158
- Project Gutenberg 105, *Persuasion*: https://www.gutenberg.org/ebooks/105
- Project Gutenberg 7256, *The Gift of the Magi*: https://www.gutenberg.org/ebooks/7256
- Project Gutenberg 541, *The Age of Innocence*: https://www.gutenberg.org/ebooks/541
- Project Gutenberg 514, *Little Women*: https://www.gutenberg.org/ebooks/514
- Project Gutenberg 550, *Silas Marner*: https://www.gutenberg.org/ebooks/550
