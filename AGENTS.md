# AGENTS.md — LHRM Project Local Rules

## Governance

- Global governance source: `youling/ai-use`.
- Before execution/recovery/takeover, load the current `youling/ai-use/AGENTS.md` L0 first, then apply this project-local file.
- Human has final sovereignty over project goals, scope, risk acceptance, naming, and major architecture direction.
- Git/GitHub is durable truth; chat/session context is working memory.

## Project identity

- Repository: `youling/lhrm`
- Display name: **Li-Hong Relationship Model / 礼宏关系模型**
- Current phase: **Parameter Convergence + representation-first state architecture**.
- Current canonical architecture pointer: `docs/foundation/CURRENT_ARCHITECTURE.md`.
- Architect role: current Project Architect is authorized by Human current direction to maintain project structure, reconcile research, migrate prior durable artifacts into this repo, and continue architecture/research convergence within the frozen project goal.

## Research discipline

- Distinguish: `Human requirement | empirical evidence | model hypothesis | architecture decision | implementation detail`.
- Do not label an unvalidated formula, parameter, weight, probability, causal relation, distance metric, normalization rule, or state transition as scientifically established.
- Prefer few stable constructs + composition + time evolution over a growing checklist of ad-hoc variables.
- Extreme real-world cases are stress tests for representation and dynamics, not permission to overfit the ontology to anecdotes.
- Unknown/missing data must remain explicit; never silently coerce missing information into neutral/perfect-match values.
- Descriptive relationship state, legal status, morality, welfare, and social desirability are separate axes unless explicitly modeled together.
- High-level labels such as “漂亮”“贤惠”“高价值”“真爱”“关系质量”“匹配度” are not assumed to be primitive variables.
- Low redundancy means low semantic/conditional redundancy, not zero statistical correlation or dynamic independence.

## Representation-first invariant

Until superseded by a reviewed durable Human/Architect decision:

1. **Representation before scalarization; state-space before score.**
2. The first-stage product is a time/history-indexed Human-Dyad state representation, not a mandatory single score/prediction.
3. Preserve raw evidence/provenance; normalization is only a computational projection.
4. Do not force every coordinate into `0..1`, Euclidean space, or one common semantic scale.
5. A coordinate may be an interval, ordinal state, category, constraint, probability distribution, Unknown, or estimate + uncertainty + evidence.
6. Distance/weight/score/probability are downstream readouts unless later validated for a specific task.

## Current architecture direction

Until superseded by a reviewed durable decision:

1. Treat `S / O / D / E` as a **local evaluation view**, not the complete world ontology.
2. World representation separates `Agent | Relationship | Environment | Belief`, with `Action/Event + Transition` for change.
3. Keep `Role` explicit as a query/evaluation lens; it does not replace world state.
4. Model directed relation states separately: `i->j` and `j->i` are independent; mutuality/asymmetry are preferably derived.
5. Model shared pair facts separately from directional states.
6. Allow one construct family to have source/target/edge/pair facets only where those facets have independent semantics; do not mechanically copy every construct across S/O/D.
7. Keep `State != Action`; state may change action policy, and actions/events may update states.
8. Relationship labels/statuses (friend, partner, engaged, married, ex, etc.) are pair/institutional facts or coarse-grained readouts, not substitutes for bottom-level state.
9. Core relationship evolution does **not** use a pre-enumerated relationship state machine as the engine; it is modeled as state transition over continuous/mixed state.
10. Time/history may branch. Dream/fantasy/plan/counterfactual worlds should normally live as nested Belief/simulated histories rather than contaminate real WorldState.
11. Candidate relation-state parameters remain candidates until representation coverage and redundancy tests pass; current list lives in `docs/foundation/PARAMETER_CONVERGENCE_V0_1.md`.

## Validation discipline

- Long-term Case Bank lives in GitHub issue `#13`.
- Case Bank primarily tests `representation completeness | closure | regression | adversarial coverage`, not population probability.
- For court/official materials, provenance quality and fact status are separate; do not treat all statements in a judgment as equally adjudicated truth.
- First representation test should map source text sentence/event by sentence/event without inventing new constructs mid-test.
- Record unmappable material as `MAPPING_FAILURE`; Architect diagnoses whether the failure is ontology, construct, scope, temporal/history, belief/observation, measurement, or merely narrative/irrelevant.
- Fiction may be used as expressivity stress test; fictional world rules belong in Environment/History unless they truly require a new Human relationship construct.

## Mutation discipline

- Material semantic changes should normally use an isolated branch + PR.
- Preserve provenance when importing historical research; classify imported material as `current | superseded | historical evidence` before relying on it.
- Do not erase old evidence merely because a newer model supersedes it.
- Current architecture should be expressed through concise canonical docs; avoid duplicated competing SSOTs.
