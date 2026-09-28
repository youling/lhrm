# Round 3 Exploration v0.1 — X01 / X02 / X03

**Status:** RESEARCH_CANDIDATE / preliminary reconnaissance  
**As of:** 2026-09-28  
**Authority:** `youling/lhrm#30` Round-3 additional exploration queue (`5856122824`)  
**Base:** `main@ee393ca24f9fbf738ac0ed839e99bdc99de6fc3a`  
**Scope:** X01 OutcomeDependence measurement · X02 Liking vs RomanticAttraction discriminant validity · X03 intensive-longitudinal dyadic datasets  
**Non-claims:** no canonical mutation; no dataset downloaded; no restricted-data access; no claim below is a validation result.

---

## 1. X01 — OutcomeDependence / relationship-level dependence measurement

### 1.1 Directly relevant measurement family exists

A strong counterexample to the earlier broad wording “relationship-level dependence has no usable instrument” is:

**Attridge (1998), _Dependency and insecurity in romantic relationships: Development and validation of two companion scales_.**  
DOI: `10.1111/j.1475-6811.1998.tb00158.x`.

The published abstract reports:
- self-report scales for **perceived dependency and insecurity in a romantic relationship**;
- original development by Fei & Berscheid;
- five studies, total **N = 1,283**;
- evidence for reliability and validity;
- dyadic-level partner similarity and discrepancy analyses;
- relationships to commitment, love, closeness, and attachment.

This is a **relationship-specific dependency instrument**, not merely a situation-level interdependence task.

### 1.2 Adjacent instrument family

**Ellis, Simpson & Campbell (2002), _Trait-Specific Dependence in Romantic Relationships_.**  
DOI: `10.1111/1467-6494.05019`.

This paper develops the **Trait-Specific Dependence Inventory (TSDI)** as a multiscale dependence construct grounded partly in interdependence theory. It is relevant to the measurement landscape, but its semantic target is not automatically identical to LHRM D8 `OutcomeDependence_(i->j,t)`.

### 1.3 X01 verdict

`VERIFIED_FACT`: relationship-level / romantic-partner-specific dependence instruments do exist.

`OPEN_GAP`: it is not yet established that Attridge/Fei-Berscheid or TSDI measure the exact LHRM D8 meaning:
> “i’s important outcomes, welfare, opportunities, or life state depend on j / this relationship.”

The next narrow task is **item-level semantic mapping**, not another broad literature search:
- map each dependency item to `outcome dependence | attachment/insecurity | emotional reliance | alternatives | resources | constraints`;
- check directionality (`i -> j`);
- determine state-vs-trait sensitivity;
- test whether the scale contains outcome-dependence signal after controlling attachment insecurity / commitment.

### 1.4 Architecture implication

Any current text saying “no relationship-level dependence tool exists” should be narrowed to:

> “No validated instrument has yet been shown to match LHRM’s exact relationship-level OutcomeDependence semantics.”

D8 should remain `HOLD_FOR_MEASUREMENT`, but the blocker is now **semantic fit**, not instrument nonexistence.

---

## 2. X02 — Liking vs RomanticAttraction discriminant validity

### 2.1 Strong nearest-neighbor evidence: Rubin Love vs Liking

**Rubin (1970), _Measurement of romantic love_.**  
DOI: `10.1037/h0029841`.

The original work developed parallel Love and Liking scales and validated them in:
- questionnaire study: **158 undergraduate dating couples**;
- laboratory study: **79 undergraduate dating couples**.

The Love and Liking scales were only moderately correlated, supporting nonidentity.

A later review/meta-analytic synthesis reports Rubin’s original Love–Liking correlations around:
- **r = .60 for men**
- **r = .39 for women**

and notes that later factor-analytic work did not reduce the literature to a clean universal two-factor boundary.

### 2.2 Factor-analytic evidence is informative but not isomorphic to LHRM D1/D2

**Cramer (1992), _Nature of Romantic Love in Female Adolescents_.**  
DOI: `10.1080/00223980.1992.10543398`.

In 301 participants, factor analysis over Rubin/Lee items yielded six orthogonal factors:
`Love | Mutual Love | Respect | Similarity | Physical Attraction | Hostility`.

Rubin Liking further split into `Respect` and `Similarity`.

This supports the idea that generic liking is not a single undifferentiated romantic-attraction construct, but it still does **not** implement LHRM’s exact D1 vs D2 definitions.

### 2.3 Behavioral romantic-interest separation

**Frost et al. (2007), _Improving online dating with virtual dates_.**  
DOI: `10.1002/meet.1450440265`.

A speed-dating follow-up measured:
- how much participants liked the partner;
- whether they wanted no further contact, friendship/professional contact, or a date.

Liking correlated with the romantic-interest category (**r = .50**), indicating overlap but not identity.

### 2.4 X02 verdict

`VERIFIED_FACT`: liking and romance-related constructs are empirically overlapping but nonidentical in several measurement traditions.

`OPEN_GAP`: this reconnaissance did **not** find a same-sample CFA/ESEM/MTMM study that directly instantiates:
- `Liking_(i->j)` using the LHRM D1 boundary; and
- `RomanticAttraction_(i->j)` using the LHRM D2 boundary,
then tests discriminant validity between exactly those two constructs.

Therefore B-7 is **narrowed, not closed**.

### 2.5 Minimum decisive study if no existing battery is found

Use the same targets and same respondents.

Required measures:
1. D1-specific liking items that exclude romance/sexuality.
2. D2-specific romantic-partner approach/partner-selection attraction items that exclude generic warmth.
3. sexual desire measured separately to avoid D2 absorbing D3.
4. repeated targets or repeated time points if feasible.

Pre-registered tests:
- two-factor CFA vs one-factor model;
- HTMT / latent correlation with uncertainty;
- cross-loadings via ESEM;
- incremental prediction of “want a date / pursue romantic relationship” after D1;
- incremental prediction of friendship/affiliative approach after D2;
- explicit counterexample cells: high liking / low romantic attraction and low liking / high romantic attraction.

Do not decide D1/D2 by scale-name intuition.

---

## 3. X03 — Intensive-longitudinal dyadic datasets

The dataset-existence question changes materially after targeted search. Multiple serious dyadic daily/ESM datasets exist; the remaining bottleneck is **construct fit + exact dyad linkage + rights/AI-use + directionality**, not simple existence.

### 3.1 Highest-value open / near-open candidates

#### X03-D01 — Szachter et al. daily conflict / satisfaction dataset

Mendeley Data DOI: `10.17632/fkg7tz8tnc.1`

- **87 Israeli heterosexual couples**
- **three-week daily diary**
- variables include self-concept clarity, conflict intensity, relationship satisfaction
- explicit dataset licence: **CC BY 4.0**
- both members are described as couples; raw structure must still be inspected before asserting exact dyad/person keys.

**Current classification:** `HIGH_PRIORITY_FOR_SCHEMA_AUDIT`  
Not yet `CALIBRATION_READY` until file structure, missingness, side identifiers, time keys, and construct semantics are checked.

#### X03-D02 — Haruvi & Bar-Kalifa shared-reality daily diary

Paper DOI: `10.1111/pere.70070`  
Data pointer: OSF project `9q7h6`.

- **84 couples**
- **21 daily observations**
- shared TV watching, communication, shared reality
- article states the data are **openly available on OSF**.

**Current classification:** `HIGH_PRIORITY_FOR_SCHEMA_AUDIT`  
Dataset-specific licence must be checked separately; article “open data” wording alone is not treated as a blanket AI-use licence.

#### X03-D03 — world-beliefs / relationship-satisfaction daily dyads

Paper DOI: `10.1080/17439760.2024.2387352`  
OSF: `m8kru`.

- subsample of a larger sample of **236 romantic couples**
- daily measures;
- data, syntax, and materials reported as openly accessible on OSF.

**Current classification:** `CANDIDATE` pending exact both-member, diary-length, licence, and variable inspection.

### 3.2 Highly relevant but rights/access must remain separate

#### X03-D04 — HARP / Health and Relationships Project

ICPSR study: **37404**, DOI `10.3886/ICPSR37404.v4`.

- both spouses in same-sex and different-sex marriages;
- Time 1 2014–2015, Time 2 2021–2022, Time 3 2024–2025;
- at each wave: baseline + **10 consecutive daily diary days**;
- diary includes daily stress, social interactions, health behaviours; baseline includes relationship quality.

This is unusually valuable because it combines:
`both spouses × daily diary × repeated macro waves × same-/different-sex marriages`.

**Current classification:** `STRUCTURALLY_HIGH_VALUE / RIGHTS_AND_AI_USE_NOT_CLEARED_HERE`.

Do not expose or download individual-level data into an LLM path without explicit applicable terms.

#### X03-D05 — NCHAT

National Couples’ Health & Time Study:
- cohabiting/married adults;
- spouses/partners sampled;
- longitudinal survey;
- time diary with experience-sampling component;
- data distributed through ICPSR.

**Current classification:** `STRUCTURALLY_HIGH_VALUE / ACCESS_AND_AI_TERMS_REQUIRE_SEPARATE_CHECK`.

### 3.3 Useful dyadic-intensive evidence, but open raw data not established in this pass

- **Totenhagen et al. (2016)**, DOI `10.1177/0265407515597562`: 157 couples; daily variability in satisfaction, commitment, closeness, conflict, ambivalence, maintenance, love.
- **Ogolsky (2009)**, DOI `10.1111/j.1475-6811.2009.01212.x`: 98 same-sex couples; 14-day Internet diary; maintenance and commitment cross-lagged.
- **Daily technology interruptions**: 173 romantic couples, 14 days; both partners; public article in PMC.
- **Chen et al. (2024)**, DOI `10.1016/j.drugalcdep.2024.112466`: 33 adult couples; 14-day daily diary; actor/partner substance-use effects on relationship satisfaction.
- **Chronic-pain couples** (70 couples; 14-day diary): helping motivation, conflict, need satisfaction, help amount/satisfaction.

These establish that the methodological regime is not rare; they do **not** establish reusable-data rights.

### 3.4 Excluded / method-only due current LHRM boundary

**Ha et al. (2024), DOI `10.1111/desc.13511`**
- 97 mixed-gender adolescent romantic couples;
- twice-weekly diary for 12 weeks;
- both partners;
- data/code on OSF.

Because the mean age is ~16 and the sample contains minors, treat this as **method evidence only**, not a default LHRM benchmark substrate under the current sensitive-content rules.

### 3.5 X03 verdict

The previous practical bottleneck should be rephrased.

**Do not say:** “intensive longitudinal dyadic relationship datasets do not exist.”

**Supported statement:**
> Serious dyadic daily/ESM datasets exist, including some openly distributed datasets. What remains unresolved is the intersection of (a) both-member identifiable dyads, (b) enough repeated occasions, (c) construct alignment to LHRM directed states, (d) lawful/AI-compatible reuse, and (e) reproducible raw-variable mapping.

The next action is **dataset schema/rights audit**, not another broad discovery sweep.

Priority audit order:
1. `10.17632/fkg7tz8tnc.1` — explicit CC BY 4.0.
2. OSF `9q7h6` — 84 couples × 21 days.
3. OSF `m8kru` — romantic-couple daily data.
4. HARP ICPSR 37404 — highest structural value, rights-first.
5. NCHAT — rights/access-first.

---

## 4. Cross-lane architecture implications

1. **D8 measurement blocker narrows.** Instrument existence is not the problem; exact semantic fit is.
2. **B-7 remains open but better specified.** There is evidence that liking and romance-related constructs are not identical, but no exact D1-vs-D2 discriminant test was found here.
3. **X03 shifts the empirical bottleneck.** Dataset discovery is no longer the dominant problem. The hard join is:
   `construct mapping × dyad directionality × repeated time × rights × uncertainty`.
4. **Do not infer validation from dataset availability.** Open files only create an executable opportunity; they do not validate a transition law.
5. **Rights stay factorized.** Open-access paper, public webpage, open dataset, dataset licence, and AI/computational-analysis permission are separate facts.

---

## 5. Source pointers

- Attridge 1998: `10.1111/j.1475-6811.1998.tb00158.x`
- Ellis et al. 2002: `10.1111/1467-6494.05019`
- Rubin 1970: `10.1037/h0029841`
- Masuda 2003: `10.1111/1468-5884.00030`
- Cramer 1992: `10.1080/00223980.1992.10543398`
- Frost et al. 2007: `10.1002/meet.1450440265`
- Szachter et al. data: `10.17632/fkg7tz8tnc.1`
- Haruvi 2026: `10.1111/pere.70070` · OSF `9q7h6`
- Daily world beliefs: `10.1080/17439760.2024.2387352` · OSF `m8kru`
- HARP: `10.3886/ICPSR37404.v4`
- Totenhagen 2016: `10.1177/0265407515597562`
- Ogolsky 2009: `10.1111/j.1475-6811.2009.01212.x`
- Chen et al. 2024: `10.1016/j.drugalcdep.2024.112466`
- Ha et al. 2024: `10.1111/desc.13511`

