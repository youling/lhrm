# X05 — Observability evidence audit v0.1

Status: RESEARCH_CANDIDATE / PARTIAL EVIDENCE AUDIT / NOT CANONICAL
As of: 2026-09-28
Authority: youling/lhrm#30 Round-3 exploration X05
Scope: D1–D8 + PPR measurement-channel audit. No Gate run; no canonical mutation.

## Architect finding

The observability registry must separate **measurement channel** from **epistemic target**.

A first-person report may target the actor's own relationship state. A partner report ordinarily represents an informant belief about that state unless the target is an externally observable fact. Observer coding normally targets displayed behavior. Behavioral evidence can be a proxy without being the state itself.

Recommended metadata shape:

```text
construct_ref
epistemic_target
channel = self_report | partner_report | observer_code | behavioral_log | institutional_record | derived
directness = DIRECT | PROXY | INFERRED
assessment_status = UNASSESSED | ASSESSED
temporal_resolution
evidence_provenance
```

Hard rules:
1. UNASSESSED != NO.
2. ontology/layer membership != observability evidence.
3. behavioral anchor != construct identity.

## First-pass matrix

| construct | externally direct as internal state | self-report | other-person / observer channel | behavior | temporal note |
|---|---|---|---|---|---|
| D1 Liking | NO | YES | informant/inferred | PROXY | change possible |
| D2 RomanticAttraction | NO | YES | observer inference imperfect | PROXY | interaction-sensitive |
| D3 SexualDesire | NO | YES | informant/inferred | PROXY | high-frequency variation documented |
| D4 Trust | NO | YES | informant/inferred | PROXY | longitudinally mutable |
| D5 AttachmentSecurity | NO | YES | informant/inferred | PROXY | relationship-specific |
| D6 Caregiving motivation/orientation | NO | YES | care behavior can be reported/coded | PROXY | context-sensitive |
| D7 Dedication | NO | YES | informant/inferred | PROXY | longitudinally mutable |
| D8 OutcomeDependence | NO as one integrated state | YES | structural components may be recorded | PROXY / DERIVABLE COMPONENTS | daily variation documented |
| PPR | NO by definition (perception) | YES | partner/observer responsiveness is a different target | PROXY | interaction-sensitive |

No row is COMPLETE. This is a repair input, not a registry import.

## Evidence anchors

### D1
Rubin's Liking tradition is participant-report measurement distinct from romantic love.
- https://doi.org/10.1111/j.1475-6811.2009.01209.x
- https://doi.org/10.1177/014616727600200225

### D2
Speed-dating work uses a three-item actor-report attraction measure. Third-party video observers are not consistently reliable, so external behavior cannot be treated as lossless direct observation.
- https://pmc.ncbi.nlm.nih.gov/articles/PMC5006939/
- https://doi.org/10.1007/s12144-022-02927-0
- https://doi.org/10.1111/j.1467-9280.2008.02248.x

### D3
Dyadic sexual desire is repeatedly measured by participant report at daily/EMA resolution; multiple datasets show real temporal variation.
- https://doi.org/10.1080/00224499.2024.2393378
- https://doi.org/10.1080/00224499.2023.2170965
- https://pubmed.ncbi.nlm.nih.gov/30756211/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC6192626/

### D4
Partner-specific trust is measured by self-report (predictability/dependability/faith). Observable reliance is behavioral evidence, not the trust state itself.
- Rempel, Holmes & Zanna (1985), Journal of Personality and Social Psychology 49:95–112
- https://us.psytoolkit.org/survey-library/trust.html

### D5 / PPR
Partner-specific attachment and perceived partner responsiveness are participant-reported; partner's own responsiveness and observer-coded responsiveness are separate targets.
- https://doi.org/10.3390/ijerph17197178
- https://research.polyu.edu.hk/en/publications/perceiving-change-in-responsiveness-from-the-relationship-partner/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC8801651/

### D6
The Caregiving Questionnaire is a participant-report instrument with multiple caregiving dimensions. Observed care acts remain behavior/proxy and do not uniquely reveal motive.
- https://pmc.ncbi.nlm.nih.gov/articles/PMC6908499/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC7764100/

### D7
The Revised Commitment Inventory separates dedication from constraint commitment in dyadic data.
- https://pmc.ncbi.nlm.nih.gov/articles/PMC3348588/

### D8
Romantic-couple studies measure dependence by actor report (including preference for current partner over alternatives), while daily work shows dependence varies over time.
- https://pmc.ncbi.nlm.nih.gov/articles/PMC4248306/
- https://doi.org/10.1177/02654075241235335

## InformationAction correction

Action/Event classification alone cannot justify direct observability of every semantic action.

- Disclose can be directly recorded when the communication channel/content is observed.
- Withhold requires more than silence: the relevant information, an applicable disclosure opportunity/expectation, and evidence of non-disclosure.
- Misrepresentation requires an observed statement plus comparison against the relevant fact/belief/evidence standard.

Therefore the future integration should not infer `directly_observable=YES` from Action/Event membership.

## Architecture implications

- Keep D1–D8 internal directed states distinct from their behavioral evidence.
- Add channel-target semantics and explicit assessment status.
- Make temporal resolution first-class measurement metadata.
- Preserve PPR as BeliefState; observed responsiveness is not PPR.
- Treat D8 specially: objective resource/constraint components can be observable even when the integrated dependence quantity is report-based or derived.

## Open gaps

Self/partner agreement and short-interval reliability remain incomplete for several constructs; measurement invariance belongs to X07; pair/agent/constraint observability rows are outside this first-pass scope.

## Non-claims

No construct is validated or frozen. A questionnaire does not prove primitiveness. Self-report is a measurement channel, not objective truth. Observer coding is not privileged access to an internal state.
