# X13 — Narrow source recovery: S31 + two method claims

**Status:** RESEARCH_CANDIDATE / source recovery  
**As of:** 2026-09-28  
**Authority:** Round-3 READY lane X13  
**Base reviewed:** PR #31 @ `07db1243e9e4efb9666620c279a83dcb4d208257` + PR #36 @ `cabf0e702a8e4c6d53b2edc49d6629c74a3247cb`  
**Allowed output vocabulary:** `FOUND_EXACT | NOT_FOUND | AMBIGUOUS`

---

## 1. The two method claims misattributed to Joel 2020

### Claim A
> “The standard error across folds strongly underestimates them.”

**Verdict: `FOUND_EXACT`.**

Exact source:

Gaël Varoquaux (2017), **“Cross-validation failure: Small sample sizes lead to large error bars.”**  
*NeuroImage* 180(Pt A).  
DOI: `10.1016/j.neuroimage.2017.06.061`  
arXiv: `1706.07581`  
PMID: `28655633`.

The abstract contains the sentence essentially verbatim:
- cross-validation error bars are often underestimated;
- “The standard error across folds strongly underestimates them.”

This is **not Joel et al. 2020**.

### Claim B
> “n = 100 → approximately ±10%.”

**Verdict: `FOUND_EXACT`.**

Same Varoquaux 2017 source. The abstract states that simple experiments show error bars of approximately **±10% for 100 samples**.

### Architect-facing consequence

In PR #31 `16_EMPIRICAL_VALIDATION_PROTOCOL.md`, these two claims should not remain attached to Joel `S04`.

Correct routing:
- source = Varoquaux 2017, `10.1016/j.neuroimage.2017.06.061`;
- evidence role = **general cross-validation uncertainty / method caution**;
- scope warning = the paper is about predictive-model validation, prominently in neuroimaging; it is not dyadic-relationship-specific evidence.

Therefore:
- it can support “fold-to-fold variation is not a valid uncertainty estimator by itself” and the illustrative small-N error-bar warning;
- it **cannot** establish the dyad-level bootstrap design as scientifically validated for LHRM by itself;
- the LHRM choice to use dyad-cluster bootstrap remains a **design/methodological choice supported by broader dependence logic**, unless separately sourced.

---

## 2. R06 `S31` — “Ideal adjusts toward actual partner”

### Corpus defect

PR #36 correctly established that R06’s source table contains **no bibliographic entry for S31**. The identifier therefore cannot be recovered by pointer-following.

### Candidate 1 — strongest semantic match

Tanja M. Gerlach, Ruben C. Arslan, Thomas Schultze, Selina K. Reinhard, & Lars Penke:

**“Predictive validity and adjustment of ideal partner preferences across the transition into romantic relationships.”**  
*Journal of Personality and Social Psychology* 116(2), 313–330.  
DOI: `10.1037/pspp0000170`.  
Published online 2017; issue publication 2019.

The abstract reports:
- N = 763 singles, followed for five months;
- preferences were less stable among people who entered a relationship;
- participants **adjusted preferences downward when partners fell short of initial preferences**;
- no consistent adjustment when partners exceeded preferences.

This is a strong semantic match to R06’s prose “伴侣调整理想偏好以匹配实际伴侣”.

### Candidate 2 — later longitudinal evidence with even closer wording

Csajbók et al. (2025), **“Mechanisms creating homogamy in depressiveness in couples: A longitudinal study from Czechia.”**  
*Scientific Reports*. DOI: `10.1038/s41598-025-93065-7`.

The abstract/full open article reports that in stable relationships, participants **adjusted ideal preferences to align more closely with actual partners over time**. This wording is extremely close to the R06 paraphrase, but it concerns the specific trait domain pessimism/depressiveness.

### Candidate 3 — longer-term preference adjustment evidence

Driebe, Stern, Penke & Gerlach (2024), **“Probing the predictive validity of ideal partner preferences for future partner traits and relationship outcomes across 13 years.”**  
DOI: `10.1177/08902070231213797`.

The paper reports current ideals being more strongly associated with perceived partner traits than initial ideals, a pattern **consistent with** ideals being somewhat malleable, and explicitly discusses prior evidence of preferences adjusting toward partners.

### S31 identity verdict

**`AMBIGUOUS`.**

Reason:
- R06 provides no title/author/year/DOI;
- more than one real study supports closely related “ideal adjustment” propositions;
- Gerlach et al. 2019 is the strongest match to the generic “preferences adjust toward partner” mechanism;
- Csajbók et al. 2025 has the closest literal wording but a narrower depressiveness domain;
- Driebe et al. 2024 supplies longer-horizon compatible evidence but is not an exact identity proof.

**Do not silently assign any of these papers the old label `S31`.**

Recommended repair:
1. retire the unresolvable label `S31` as `SOURCE_IDENTITY_LOST`;
2. if the RGM Movement hypothesis is retained, cite the newly verified papers under **new source IDs** with their actual, narrow claims;
3. keep RGM / Ideal schema promotion on HOLD until the Architect decides whether those verified claims are semantically sufficient for LHRM’s proposed dynamic-Ideal state.

---

## 3. Final X13 packet

### VERIFIED_FACTS
- The fold-standard-error claim and ±10% at n=100 claim come from **Varoquaux 2017**, not Joel 2020.
- Gerlach et al. 2019 directly reports partner-directed adjustment of ideal partner preferences.
- Csajbók et al. 2025 directly reports stable partners adjusting an ideal preference closer to the actual partner in a specific trait domain.
- R06’s historical `S31` has no recoverable bibliography in the durable artifact.

### NEGATIVE_RESULTS
- `S31` cannot be uniquely reconstructed from the repository text.
- No evidence justifies continuing to treat `S31` as a valid source pointer.

### OPEN_GAPS
- Whether verified preference adjustment evidence is sufficient to model `Ideal` as a dynamic directed state rather than Belief/evaluation metadata remains an architecture question.
- Dyad-specific uncertainty estimation still needs its own methodological justification beyond Varoquaux’s general CV warning.

### ARCHITECTURE_IMPLICATIONS
- Repair PR #31 source routing immediately.
- Do not promote RGM based on recovered source candidates alone.
- Preserve `Ideal/RGM = HOLD` pending semantic adjudication.

### NON_CLAIMS
- This memo does not claim Gerlach 2019 was historically the missing S31.
- It does not claim Varoquaux’s neuroimaging simulations establish LHRM-specific uncertainty magnitudes.
- It does not validate RGM.

### SOURCE_POINTERS
- Varoquaux 2017: `10.1016/j.neuroimage.2017.06.061`
- Gerlach et al.: `10.1037/pspp0000170`
- Csajbók et al. 2025: `10.1038/s41598-025-93065-7`
- Driebe et al. 2024: `10.1177/08902070231213797`
