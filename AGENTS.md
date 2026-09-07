# AGENTS.md — LHRM Project Local Rules

## Governance

- Global governance source: `youling/ai-use`.
- Before execution/recovery/takeover, load the current `youling/ai-use/AGENTS.md` L0 first, then apply this project-local file.
- Human has final sovereignty over project goals, scope, risk acceptance, naming, and major architecture direction.
- Git/GitHub is durable truth; chat/session context is working memory.

## Project identity

- Repository: `youling/lhrm`
- Display name: **Li-Hong Relationship Model / 礼宏关系模型**
- Current phase: research + architecture foundation.
- Architect role: current Project Architect is authorized by Human current direction to maintain project structure, reconcile research, migrate prior durable artifacts into this repo, and advance architecture within the frozen project goal.

## Research discipline

- Distinguish: `Human requirement | empirical evidence | model hypothesis | architecture decision | implementation detail`.
- Do not label an unvalidated formula, parameter, weight, probability, or causal relation as scientifically established.
- Prefer few stable primitives over a growing checklist of ad-hoc variables.
- Extreme real-world cases are stress tests for representation and dynamics, not permission to overfit the ontology to anecdotes.
- Unknown/missing data must remain explicit; never silently coerce missing information into neutral/perfect-match values.
- Descriptive relationship strength, legal status, morality, welfare, and social desirability are separate axes unless explicitly modeled together.
- High-level labels such as “漂亮”“贤惠”“高价值”“真爱”“关系质量” are not assumed to be primitive variables.

## Mutation discipline

- Material semantic changes should normally use an isolated branch + PR.
- Preserve provenance when importing historical research; classify imported material as `current | superseded | historical evidence` before relying on it.
- Do not erase old evidence merely because a newer model supersedes it.
- Current architecture should be expressed through concise canonical docs; avoid duplicated competing SSOTs.

## Current architecture direction

Until superseded by a reviewed durable decision:

1. Treat `S / O / D / E` as a **local evaluation view**, not necessarily the complete world ontology.
2. Keep `Role` explicit because the same people can produce different evaluations under different relationship tasks.
3. Model real-world complexity through stable primitives, dynamic state transitions, partial observation/belief, and multi-agent relationships rather than by endlessly adding special-case parameters.
4. Separate internal computation from human-facing presentation and from empirically calibrated probability prediction.
