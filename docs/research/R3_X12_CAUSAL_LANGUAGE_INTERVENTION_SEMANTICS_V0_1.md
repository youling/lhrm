# X12 — causal-language / intervention semantics v0.1

Status: RESEARCH_CANDIDATE / NOT CANONICAL / NO LAW VALIDATED.

Architect finding:
- A transition equation is not automatically a causal mechanism.
- Temporal prediction is not causal identification.
- A causal promotion requires a defined intervention, comparison, outcome, horizon, target population, estimand, and explicit assumptions for consistency, exchangeability, positivity, measurement, selection/censoring, and dyadic interference.
- LHRM latent states are not direct intervention knobs unless a real intervention/version is specified.
- In dyads, partner interference is a default consideration; actor, partner, and joint effects must be distinguished.
- BMR/APES/DVA/RGM/RT remain non-causal transition candidates.

Integration guidance:
Keep state-transition semantics separate from causal-identification semantics. Put the causal-language/intervention gate in empirical validation, reusing X09 negative controls and X10 selection semantics.

Evidence anchors:
- Hernán & Robins, Causal Inference: What If.
- Cole & Frangakis 2009, DOI 10.1097/EDE.0b013e31818ef366.
- Tchetgen Tchetgen & VanderWeele 2012, DOI 10.1177/0962280210386779.
- Rizi et al. 2024, DOI 10.1002/sim.10278.

Next READY: X06 and X07.
MERGE=FORBIDDEN. #20/#21/#22 remain isolated. No Eye/Juece mutation.
