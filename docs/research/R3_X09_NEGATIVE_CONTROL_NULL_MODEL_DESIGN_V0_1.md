# X09 — Negative-control / placebo / null-model design v0.1

**Status:** RESEARCH_CANDIDATE / DESIGN INPUT / NOT RUN / NOT CANONICAL  
**As of:** 2026-09-28  
**Authority:** `youling/lhrm#30` Round-3 exploration X09  
**Base evidence:** repaired `06_TRANSITION_LAWS.md` on PR #31 head `07db1243e9e4efb9666620c279a83dcb4d208257`  
**Scope:** Define what each negative control actually tests for BMR / APES / DVA / RGM / RT. No law is validated or frozen. No empirical run is performed.

---

## 1. Architect verdict

The transition-law program currently mixes three different things under “null”:

1. **substantive rival models** — a simpler scientific explanation could be true;
2. **measurement / timing placebos** — the apparent effect may be an artifact of alignment, common method, or reporting;
3. **surrogate-data controls** — destroy a specific dependency while preserving nuisance structure.

These must not be interpreted the same way.

A useful rule:

> A negative control is informative only if it destroys the structure claimed by the law while preserving as much irrelevant structure as possible.

Therefore:
- raw random shuffling of longitudinal observations is generally too destructive;
- dyad/partner shuffles must preserve role, calendar, and sampling structure where those matter;
- time surrogates should preserve marginal distributions and, where possible, autocorrelation;
- a control “losing” does not prove causality;
- a control “winning” can directly refute a claimed incremental mechanism when the comparison is predeclared and adequately powered.

---

## 2. Global control registry

| ID | control | preserves | destroys | primary diagnostic use |
|---|---|---|---|---|
| NC-01 | `AR_ONLY / persistence` | actor/dyad temporal persistence | all proposed cross-channel mechanism | asks whether the law adds anything beyond persistence |
| NC-02 | `RANDOM_INTERCEPT / trait-only` | stable between-person/dyad heterogeneity | within-unit dynamic mechanism | detects trait-state confounding |
| NC-03 | `ACTOR_ONLY / NO_PARTNER` | actor history + actor covariates | partner-specific channel | tests whether dyadic coupling is needed |
| NC-04 | `PARTNER_SWAP` within compatible strata | each actor series, partner-series marginal/time structure | true dyad linkage | tests dyad-specific coupling vs generic population covariance |
| NC-05 | `TIME_SURROGATE` for event/input channel | marginal distribution + chosen autocorrelation structure | exact temporal alignment to outcome | tests whether claimed timing carries information |
| NC-06 | `LEAD_PLACEBO` | same variables/models | causal/temporal direction | future input predicting prior outcome flags confounding or timestamp leakage |
| NC-07 | `UNDIRECTED / POOLED DYAD SCORE` | pair-level common signal | directed source→target asymmetry | tests whether directionality is necessary |
| NC-08 | `STABLE_LEVEL` | baseline/rank-order differences | within-dyad change mechanism | tests whether level alone is sufficient |
| NC-09 | `LEVEL_PLUS_RANDOM_WALK` | level + unsystematic within-dyad drift | structured slope mechanism | DVA-specific strong rival |
| NC-10 | `NO_INTERACTION` | main effects | level-conditioned slope / moderation | tests whether interaction shape is needed |
| NC-11 | `MEMORYLESS` | current inputs | stock/path dependence | tests accumulation/hysteresis claims |
| NC-12 | `SINGLE_CHANNEL` | dominant channel | second proposed channel | tests whether multi-channel law is distinguishable |
| NC-13 | `TRAIT_MODERATED` | stable person-specific branch differences | dyadic-state branch selector | RT premise audit |
| NC-14 | `MEASUREMENT_ARTIFACT` | contemporaneous report covariance | lagged process | distinguishes reporting recalibration from state evolution |

### 2.1 Surrogate-data guard

Do **not** use unrestricted random time permutation as the default placebo. It destroys serial dependence and can make the null unrealistically easy to beat.

Preferred order:
1. circular shift or blockwise permutation of the input/event channel within dyad when stationarity is defensible;
2. phase/surrogate methods only when their assumptions match the measured process;
3. partner swap across compatible dyads for dyad-specificity;
4. exact timestamp misalignment placebo when the scientific claim is event→next-state coupling.

Theiler et al. (1992) is the methodological anchor for the general principle: surrogate data should be generated to satisfy a specified null while preserving irrelevant structure.

---

## 3. BMR — Belief-Mediated Revision

Current status: `HOLD_FOR_EVIDENCE`; only the directional belief-update candidate survives.

### Required rivals

| test | comparison | what it tests | consequence if rival is equivalent/better |
|---|---|---|---|
| BMR-N1 | full BMR vs `AR_ONLY` | any incremental dynamic content | independent law family fails; keep readout only |
| BMR-N2 | BMR vs `ACT_NOT_BELIEF` | belief mediation vs observable response directly | “belief rather than action” claim fails |
| BMR-N3 | BMR vs `NO_PARTNER` | partner-specific coupling | partner channel not supported |
| BMR-N4 | directed BMR vs `UNDIRECTED / pooled dyad` | source→target directionality | directed semantics not empirically needed for this readout |
| BMR-N5 | true partner vs compatible `PARTNER_SWAP` | dyad-specific linkage | generic population covariance can explain apparent partner effect |
| BMR-N6 | aligned PPR vs autocorrelation-preserving time surrogate | temporal specificity | aligned timing does not add evidence |
| BMR-N7 | `LEAD_PLACEBO`: future PPR → prior ΔZ | timestamp/common-method leakage | if comparable to forward effect, causal/process language must be withdrawn |

### Interpretation rule

- N2 is the direct falsifier for the “belief-mediated” discriminator.
- N5/N6/N7 are **diagnostics**, not proof of a competing psychological mechanism.
- If BMR beats N5/N6 but not N2, the data may support dyad-specific temporal coupling while still failing the belief-mediation claim.

---

## 4. APES — Actor–Partner Exchange with Stock

Current status: `HOLD_FOR_EVIDENCE`; X01 already weakens the old “no relationship-level dependence measure located” blocker, but semantic alignment to D8 remains open.

### Required rivals

| test | comparison | target claim |
|---|---|---|
| APES-N1 | full stock model vs `MEMORYLESS` | dependence behaves like an accumulating stock |
| APES-N2 | full vs `AR_ONLY` | inputs add information beyond persistence |
| APES-N3 | full vs `NO_ALT` | alternatives channel contributes |
| APES-N4 | full vs `NO_INV` | investment/history contributes |
| APES-N5 | full vs `NO_DISSIPATION` | return-to-center / dissipation is necessary |
| APES-N6 | full vs `RANDOM_INTERCEPT / trait-only` | stock is not merely stable dyad/person heterogeneity |
| APES-N7 | explicit D8 state vs **structural derivation** from resources + alternatives + constraints + environment | D8 is primitive/stock vs derived readout |
| APES-N8 | true pair investment history vs compatible pair-history swap | path-specificity of pair investment |

### Special disposition logic

APES-N7 is architecturally load-bearing:

> If structural components preserve the same dependency information and predictive content without an independent D8 state, the correct result is evidence for `DERIVE`, not “benchmark failure”.

Do not force APES to win merely because the stock formulation is more expressive.

---

## 5. DVA — level-conditioned slope

Current status: only `LEVEL_CONDITIONAL_SLOPE` remains; “initial differences defeated incremental change” has been withdrawn.

### Required rivals

| test | comparison | target claim |
|---|---|---|
| DVA-N1 | `N8_LEVEL_CONDITIONAL_SLOPE` vs no-interaction slope model | whether slope actually depends on baseline level |
| DVA-N2 | N8 vs `B2_STABLE_LEVEL` | any within-dyad structured change beyond stable level |
| DVA-N3 | N8 vs `B8_LEVEL_PLUS_RW` | structured conditional slope vs unsystematic drift |
| DVA-N4 | N8 vs random-slopes-only | baseline level explains slope heterogeneity rather than arbitrary dyad slopes |
| DVA-N5 | N8 vs cohort/time-period model | apparent slope heterogeneity is not cohort/calendar structure |
| DVA-N6 | **pseudo-onset placebo**: replace true relationship onset `τ0` with predeclared false anchors | whether the level→slope effect depends on the scientifically meaningful onset |
| DVA-N7 | lead/reverse-time sensitivity | regression-to-mean / alignment artifact |

### Important guard

DVA-N6 must not search many fake onsets and report the most favorable one. Use a small predeclared set. If arbitrary pseudo-onsets reproduce the same “level-conditioned slope”, the interpretation should shift toward generic regression-to-mean / time-index artifact.

---

## 6. RGM — Reference Gap and Movement

Current status: `HOLD_FOR_EVIDENCE`; exact old S31 identity is lost, while source recovery found plausible but not identity-equivalent literature. Gap and Movement must remain separate.

### Required rivals

| test | comparison | target claim |
|---|---|---|
| RGM-N1 | Actual-only vs Actual+Ideal | whether Ideal adds information beyond Actual |
| RGM-N2 | fixed Ideal vs time-varying Ideal | whether Ideal is a state process rather than a stable trait |
| RGM-N3 | contemporaneous Actual→Ideal vs lagged prior Actual→future Ideal | reporting recalibration vs temporal movement |
| RGM-N4 | true partner affirmation vs partner-swapped affirmation | dyad-specific affirmation channel |
| RGM-N5 | aligned affirmation vs time-surrogate affirmation | event timing specificity |
| RGM-N6 | Gap-only vs Gap+Movement | whether two channels are empirically separable |
| RGM-N7 | self-report affirmation vs independently coded/observed affirmation | common-method dependence |

### Disposition logic

- If RGM-N1 fails: Ideal need not enter the state representation.
- If RGM-N2 fails but RGM-N1 survives: Ideal may remain a stable belief/reference parameter, not a dynamic state.
- If RGM-N3 shows only contemporaneous association: classify as `REPORTING_ARTIFACT`, not state movement.
- If RGM-N6 is equivalent: reject the two-channel claim while preserving whichever single channel survives.

---

## 7. RT — Rhythm and Threshold

Current status: `MODEL_HYPOTHESIS / UNTESTABLE_WITH_CURRENT_ORDINARY_WAVE_DATA`; core “branch selector s is dyadic-state dependent” has zero direct support.

### Required rivals

| test | comparison | target claim |
|---|---|---|
| RT-N1 | branch model vs `LINEAR_RECIPROCITY` | branch structure vs single linear response |
| RT-N2 | branch model vs `NO_FEEDBACK` | state→next-behavior feedback exists |
| RT-N3 | dyadic-state selector vs `TRAIT_MODERATED` | branch selection is dyadic-state, not person constant |
| RT-N4 | full vs `AR_ONLY` behavior sequence | partner/current-state channels add information |
| RT-N5 | true event order vs within-dyad order surrogate preserving event counts | event sequence carries signal |
| RT-N6 | true partner sequence vs compatible `PARTNER_SWAP` | branch behavior is dyad-specific |
| RT-N7 | future/next event predicting prior event | timestamp/order leakage |
| RT-N8 | state labels time-surrogated while behavior stream preserved | selector depends on aligned dyadic state |
| RT-N9 | positive/repair branch taxonomy collapsed to one response channel | two-branch separation is necessary |

### Hard guard

RT controls are meaningful only with event-level ordered data. Ordinary multi-wave questionnaire data cannot run these tests. Do not convert “not testable in this dataset” into evidence against RT.

---

## 8. What each null is allowed to conclude

| outcome | allowed conclusion | forbidden conclusion |
|---|---|---|
| full model ≈ AR_ONLY under adequate equivalence design | no demonstrated incremental law content in this dataset | “human relationships are purely autoregressive” |
| partner swap ≈ true partner | no demonstrated dyad-specific linkage | “partners have no influence” |
| time surrogate ≈ aligned time | no demonstrated timing specificity at this resolution | “the mechanism is false at all timescales” |
| lead placebo ≈ forward effect | temporal/causal interpretation unsafe | “reverse causation is proven” |
| structural derivation ≈ explicit latent/state | evidence for DERIVE/redundancy | “the construct is psychologically unreal” |
| trait-only ≈ dynamic model | dynamics not identified beyond stable heterogeneity | “states never change” |
| two-channel ≈ single-channel | channels not separable in tested design | “one named construct is invalid” |

---

## 9. Pre-registration packet for any future empirical run

For every law test, freeze before looking at outcomes:

```text
law_id
claim_under_test
dataset_exact_version
rights_snapshot
unit_of_analysis
time_resolution
target_population
primary_model
negative_control_ids[]
surrogate_generation_rule
role/calendar/context strata preserved
outcome_metric
equivalence_margin_or_MDE
missingness handling
power / precision criterion
multiple-testing rule
failure consequence
underpowered consequence
diagnostic-only controls
```

A negative control without a predeclared consequence is only a descriptive sensitivity check.

---

## 10. VERIFIED_FACTS

- PR #31 currently contains five unfrozen law families: BMR / APES / DVA / RGM / RT.
- The repaired document already names many reduced models but does not yet provide one normalized cross-law negative-control registry.
- DVA’s surviving claim is level-conditioned slope, not “incremental change defeated”.
- RT requires event-level order and cannot be tested by ordinary coarse multi-wave data.
- X04 establishes that lossless representation after withholding a construct can support DERIVE/redundancy.
- X05 establishes that channel/target/observability must be separated before using behavioral proxies as state measurements.

## 11. NEGATIVE_RESULTS

- Unrestricted random time shuffling is not an acceptable universal placebo because it destroys nuisance temporal structure.
- A partner/dyad shuffle by itself does not distinguish belief mediation from action mediation.
- “null not significant” is not evidence for equivalence.
- No single control can establish causality for any of the five law families.
- RT cannot be falsified with current ordinary-wave data merely by failing to estimate event-order terms.

## 12. OPEN_GAPS

- Exact equivalence margins / MDEs remain dataset-specific and must be frozen per run.
- X10 must handle selection, attrition, breakup, and survivorship before transition estimates are interpreted.
- Some datasets may not permit valid partner swap because calendar/context/role matching is inadequate.
- X07 invariance can change whether a null comparison is interpretable across groups.
- D8 semantic alignment from X01 must be resolved before APES-N7 becomes a construct-level verdict.

## 13. ARCHITECTURE_IMPLICATIONS

- Add a normalized `negative_control_registry` to the future empirical protocol, not to ontology.
- Keep diagnostic controls separate from law falsifiers.
- Treat `DERIVE` as a valid terminal consequence when an explicit state adds no information over structural components.
- Require temporal/dyadic surrogates to declare which nuisance structure they preserve.
- Never interpret failure to estimate as falsification.

## 14. NON_CLAIMS

- No law is validated, rejected, or frozen by this design memo.
- No effect size, threshold, equivalence margin, or parameter is proposed as universal.
- Surrogate-data success is not causal identification.
- RI-CLPM/APIM or any other estimator is not mandated as the single implementation.

## 15. SOURCE POINTERS

Project-local primary target:
- `docs/research/overnight-2026-09-27/06_TRANSITION_LAWS.md` @ PR #31 head `07db1243e9e4efb9666620c279a83dcb4d208257`.

Methodological anchors:
- Theiler J, Eubank S, Longtin A, Galdrikian B, Farmer JD. (1992). *Testing for nonlinearity in time series: the method of surrogate data*. Physica D 58:77–94. DOI: `10.1016/0167-2789(92)90102-S`.
- Hamaker EL, Kuiper RM, Grasman RPPP. (2015). *A critique of the cross-lagged panel model*. Psychological Methods 20:102–116. DOI: `10.1037/a0038889`.
- Loeys T, Cook W, De Smet O, Wietzker A, Buysse A. (2014). *The actor–partner interdependence model for categorical dyadic data: a user-friendly guide to GEE*. Personal Relationships 21:225–241. DOI: `10.1111/pere.12028`.
