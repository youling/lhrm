# 00_MANIFEST — Overnight OpenCode Research Swarm v1

> Work Order: `youling/lhrm#30@overnight-opencode-exploration-swarm-v1`
> Role: `Builder-Orchestrator / Research Orchestrator` (Fresh Builder)
> Base: `youling/lhrm@main` = `ee393ca24f9fbf738ac0ed839e99bdc99de6fc3a` (live-rechecked 2026-09-27)
> Governance live-rechecked: `youling/ai-use@main` = `64018d80443c1889c8aaf4a6d27ffe78f3e6dd90`
> Head branch: `research/opencode-overnight-2026-09-27`
> Claim: https://github.com/youling/lhrm/issues/30#issuecomment-5850793190

**本文件是本次 overnight 研究 attempt 的 lane 状态 SSOT。**
`本文件不是 canonical architecture。` 本目录下所有文件都是 `RESEARCH_CANDIDATE`，未经 Human/Architect 审阅不得当作已确立结论、参数或公式。

---

## 0. 本次 attempt 的硬边界（复述，便于 reader 单独读本文件时判定）

- `MERGE = FORBIDDEN`（本 attempt 不 merge）
- `CANONICAL_MUTATION = FORBIDDEN`（不改 ontology / foundation docs / formula SSOT / schema / weights / thresholds）
- `PRODUCTION_MUTATION = FORBIDDEN`
- `CROSS_PROJECT_MUTATION = FORBIDDEN`（不写 Eye / Juece）
- `VERIFIER_ISOLATION = PRESERVE`（不执行、不读取、不引用 `#20/#21/#22` 的 sibling 输出）
- 不触碰 Juece `#30` / PR `#31`
- 不绕过 auth / licence / robots / rights
- 不下载受限数据
- 变更面仅限 `docs/research/overnight-2026-09-27/`

## 1. 当前状态：Wave 1 已派发

| 阶段 | 状态 |
| --- | --- |
| Governance + project-local bootstrap | `SUCCESS` |
| `AGENT_CLAIMED` + readback | `SUCCESS` |
| 隔离 branch 创建并推送 | `SUCCESS` |
| CP1（Wave 1 全 lane 派发 / manifest 骨架持久化） | 见下方 lane 表，随 lane 状态滚动 |
| Wave 2 audits | `PENDING`（仅在 Wave 1 全部 durable writeback 后启动） |
| Research PR | `PENDING` |
| `AGENT_TERMINAL_RESULT` | `PENDING` |

## 2. Lane 状态表

状态枚举：`DISPATCHED | CLAIMED | SUCCESS | NEGATIVE_RESULT | PARTIAL | BLOCKED | FAILED`

| Lane | 报告路径 | 状态 | 核心证据指针 | 备注 |
| --- | --- | --- | --- | --- |
| R00 Currentness / gap map | `docs/research/overnight-2026-09-27/01_CURRENTNESS_AND_GAP_MAP.md` | `DISPATCHED` | — | |
| R01 Construct convergence deep audit | `docs/research/overnight-2026-09-27/02_CONSTRUCT_CONVERGENCE.md` | `DISPATCHED` | — | |
| R02 Semantic redundancy / double-count red audit | `docs/research/overnight-2026-09-27/02b_CONSTRUCT_REDUNDANCY_AUDIT.md` | `DISPATCHED` | — | |
| R03 Measurement instruments & proxy dictionary | `docs/research/overnight-2026-09-27/03_MEASUREMENT_INSTRUMENTS.md` | `DISPATCHED` | — | |
| R04 Quantitative dyadic / longitudinal dataset landscape | `docs/research/overnight-2026-09-27/04_DATASET_LANDSCAPE.md` | `DISPATCHED` | — | |
| R05 Statistical identification / estimation methods | `docs/research/overnight-2026-09-27/05_IDENTIFICATION_AND_STATISTICS.md` | `DISPATCHED` | — | |
| R06 Candidate transition-law families / falsifiability | `docs/research/overnight-2026-09-27/06_TRANSITION_LAWS.md` | `DISPATCHED` | — | |
| R07 Sparse input / missingness / uncertainty | `docs/research/overnight-2026-09-27/07_PARTIAL_OBSERVABILITY.md` | `DISPATCHED` | — | |
| R08 Belief / observation / deception / nested knowledge | `docs/research/overnight-2026-09-27/08b_BELIEF_DECEPTION_KNOWLEDGE.md` | `DISPATCHED` | — | |
| R09 Dynamic systems, path dependence, hysteresis, no-FSM | `docs/research/overnight-2026-09-27/09_DYNAMIC_SYSTEMS_AND_HYSTERESIS.md` | `DISPATCHED` | — | |
| R10 Mutuality / asymmetry / power / dependence emergence | `docs/research/overnight-2026-09-27/10_MUTUALITY_POWER_DEPENDENCE.md` | `DISPATCHED` | — | |
| R11 General Human Dyad scope audit | `docs/research/overnight-2026-09-27/11_GENERAL_HUMAN_DYADS_SCOPE.md` | `DISPATCHED` | — | |
| R12 Computational relationship / ABM / microsimulation benchmark | `docs/research/overnight-2026-09-27/12_COMPUTATIONAL_MODELS_ABM.md` | `DISPATCHED` | — | |
| R13 LLM Skill / adaptive interview layer | `docs/research/overnight-2026-09-27/13_LLM_SKILL_INTERVIEW_LAYER.md` | `DISPATCHED` | — | |
| R14 Paper positioning / novelty / reviewer-risk | `docs/research/overnight-2026-09-27/14_PAPER_POSITIONING_NOVELTY.md` | `DISPATCHED` | — | |
| R15 Case Bank expansion strategy | `docs/research/overnight-2026-09-27/15_CASEBANK_EXPANSION.md` | `DISPATCHED` | — | |
| R16 Empirical validation protocol join | `docs/research/overnight-2026-09-27/16_EMPIRICAL_VALIDATION_PROTOCOL.md` | `DISPATCHED` | — | |
| R17 Independent red-team / falsifier search | `docs/research/overnight-2026-09-27/17_RED_TEAM_FALSIFIERS.md` | `DISPATCHED` | — | **独立性：首稿前不得读 R01–R16 输出** |

### Wave 2 audit lane

| Lane | 报告路径 | 状态 | 备注 |
| --- | --- | --- | --- |
| A01 Evidence quality audit | `docs/research/overnight-2026-09-27/A01_EVIDENCE_QUALITY_AUDIT.md` | `PENDING` | Wave 1 durable 后启动 |
| A02 Cross-lane contradiction / duplicate audit | `docs/research/overnight-2026-09-27/18_CROSS_LANE_CONFLICT_AUDIT.md` | `PENDING` | Wave 1 durable 后启动 |
| A03 Falsifiability / hindsight-fitting audit | `docs/research/overnight-2026-09-27/A03_FALSIFIABILITY_HINDSIGHT_AUDIT.md` | `PENDING` | Wave 1 durable 后启动 |
| A04 Citation / provenance audit | `docs/research/overnight-2026-09-27/A04_CITATION_PROVENANCE_AUDIT.md` | `PENDING` | 视 source 规模决定 |

## 3. 计数汇总（随 attempt 滚动）

- Wave 1 lane 总数：18（R00–R17）
- Wave 1 child 数（实际派发）：待填
- Wave 2 audit child 数：待填
- `SUCCESS` / `NEGATIVE_RESULT` / `PARTIAL` / `BLOCKED` / `FAILED` 计数：待填
- 去重后高质量指针数：待填
- 严肃候选 quantitative dyadic dataset 数：待填
- 已 catalog 的 validated measurement instrument family 数：待填
- falsifiable transition-law family 数：待填
- Case Bank 下一批候选数：待填
- 明确 counterexample / falsifier 数：待填

## 4. 未解 blocker

见 `19_SYNTHESIS_CANDIDATE.md` 与本文件终态小节。终态以 `AGENT_TERMINAL_RESULT` comment 为准。
