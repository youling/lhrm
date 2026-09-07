# ARCHITECT_RECONNAISSANCE_REPORT

```yaml
as_of: 2026-09-07
scope: LHRM foundational architecture for relationship evaluation and simulation
external_current_state: |
  Contemporary relationship science treats mate evaluation as a process that changes from initial attraction through established relationships, and emphasizes both normative desirability and person-specific heterogeneity. Mate Evaluation Theory further separates perceiver, target, and relationship variance and argues that repeated interaction expands target-specific information. These findings are compatible with LHRM's decision to avoid a single static person-score and to preserve dyad-specific state, partial observation, and dynamic updating.
reuse_candidates: |
  REUSE relationship-science distinctions around perceiver/target/relationship variance, attraction vs satisfaction, and longitudinal relationship development.
  REUSE standard probabilistic, survival/hazard, Bayesian updating, microsimulation, and agent-based modeling patterns where appropriate rather than inventing bespoke mathematics for common problems.
architecture_delta: |
  The prior S/O/D/E draft is useful as a local evaluation coordinate, but current project discussion has exposed a broader world-model requirement: multiple agents, multiple relationship edges, external environment, belief/observation differences, events/actions, and state transition. S/O/D/E should therefore be retained as a query-local projection rather than asserted as the complete world ontology.
decisions: |
  ADAPT prior S/O/D/E foundation into the new dedicated LHRM repository with provenance preserved.
  BUILD only the project-specific unifying ontology, evaluation interface, and simulation architecture that cannot be reused directly from established methods.
  DEFER numerical weights, calibrated probabilities, and causal claims until empirical data and validation exist.
do_not_build / deprecated_paths: |
  Do not build a monolithic LoveScore or CompatibilityIndex as the core model.
  Do not equate missing data with perfect/neutral matching.
  Do not treat game mechanics or dating-app scores as empirical relationship truth; use them as modeling/UI benchmarks only.
  Do not overfit ontology to extreme anecdotes; extreme cases are adversarial representation tests.
open_questions: |
  Minimal world-state ontology; minimal relationship-state dimensions; observation/belief representation; role/task semantics; stage representation; event/state-transition semantics; calibration datasets; human-readable result presentation.
targeted_research_needed: |
  Relationship-state decomposition, longitudinal outcome datasets, Chinese marriage/divorce/population statistics, dating-app matching mechanics, relationship-game state/visualization benchmark.
first_architecture_direction: |
  Establish LHRM as the dedicated durable SSOT; migrate the historical foundation from youling/an; keep architecture documents sparse and versioned; continue by stress-testing and reducing primitives before numerical implementation.
```

## External evidence used for current-state alignment

1. Eastwick, P. W., & Joel, S. (2025), **How Do People Feel About Mates?**, *Annual Review of Psychology* 76:385–412. The review spans initial attraction through long-term relationship settings, distinguishes normative desirability from heterogeneity, and discusses how evaluations change across the relationship arc.  
   https://doi.org/10.1146/annurev-psych-012224-025712

2. Eastwick, P. W., Finkel, E. J., & Joel, S. (2023), **Mate Evaluation Theory**, *Psychological Review* 130(1):211–241. MET decomposes mate evaluations into target, perceiver, and relationship variance and argues that repeated interaction increasingly supplies target-specific information.  
   https://pubmed.ncbi.nlm.nih.gov/35389716/

## Architecture classification

- Prior `S/O/D/E` foundation: **ADAPT**, not discard.
- `Role` as explicit query condition: **KEEP**.
- Missing/unknown information as first-class state: **KEEP**.
- Dynamic relationship evolution and path dependence: **BUILD/ADAPT using standard stochastic/state-transition methods**.
- Multi-agent social graph: **BUILD/ADAPT using established graph/agent-based modeling patterns**.
- Numerical compatibility score as project core: **REJECT**.
- Human-facing count/probability/curve visualizations: **DEFER implementation; keep as presentation layer**.

## Readiness

```yaml
architect_readiness: ARCHITECT_READY
reason: bootstrap durable, target repo reconciled, current external frame checked, migration direction classified
next_classification: CONTINUE_WITHIN_AUTHORITY
```
