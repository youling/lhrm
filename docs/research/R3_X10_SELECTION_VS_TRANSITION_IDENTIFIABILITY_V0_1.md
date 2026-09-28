# X10 — Selection vs transition identifiability v0.1

Status: RESEARCH_CANDIDATE / NOT CANONICAL / NO LAW VALIDATED.

Architect verdict: transition validation must distinguish relationship entry/formation selection, dyadic co-participation, wave nonresponse, relationship survival/dissolution, and delayed study entry. A transition slope estimated only among still-together observed couples is a conditional active-relationship estimand, not automatically a population transition law.

Required protocol fields: target_population, relationship_age_at_entry, co_participation_status, partner-specific observation indicators, nonresponse_reason, relationship_status, dissolution_event_time/source, post-exit construct definedness, primary_transition_estimand, selection assumptions, censoring model, and sensitivity analysis.

Hard gates: do not treat dissolution as ordinary missingness; do not impute zero when a relationship-specific construct becomes undefined; do not silently universalize complete-case estimates; do not assume two-partner participation is neutral; and do not treat IPW, joint modeling, or competing risks as automatic identification without their assumptions and diagnostics.

Evidence anchors: Park, Impett & MacDonald (2021), DOI 10.1177/0146167220920167; Johnson et al. (2024), DOI 10.1177/02654075241265063; Kolamunnage-Dona et al., https://pmc.ncbi.nlm.nih.gov/articles/PMC3315284/; Matsuura & Eguchi (2005), DOI 10.1111/j.1541-0420.2005.00325.x.

Next: X11 third-party/network context stress test, then X12 causal-language/intervention semantics. X06/X07 remain independent lanes.

#20/#21/#22 remain isolated. No Eye/Juece mutation. MERGE=FORBIDDEN.
