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

| 阶段 | 状态 | 证据 |
| --- | --- | --- |
| Governance + project-local bootstrap | `SUCCESS` | `ai-use@64018d80` / `lhrm@ee393ca2` live 复核一致 |
| `AGENT_CLAIMED` + readback | `SUCCESS` | comment `5850793190`，2314 字符回读一致 |
| 隔离 branch 创建并推送 | `SUCCESS` | `research/opencode-overnight-2026-09-27` @ `ce1a774` |
| CP1（Wave 1 全 lane 派发 / manifest 骨架持久化） | `SUCCESS` | 18 个 Wave 1 child 同批并发派发；骨架 `ce1a774` |
| Wave 1 终稿 durable writeback | `SUCCESS` | commit `8ee07c2`，18 份报告 / 11328 行 / 1,221,011 字节 |
| R17 独立性 | `CONFIRMED` | R17 在任何 lane 报告写入之前完成首稿；见 `17_RED_TEAM_FALSIFIERS.md` §0 |
| Repair pass | 3 次 | R16（首次 dispatch 失败 → 完整重做）、R09（packet 缺 §8/§9 → 补写）、R02 + R11（各一次窄修复） |
| Wave 2 audits | `IN_PROGRESS` | A01–A04 于 Wave 1 全部 durable 后启动 |
| Research PR | `PENDING` | |
| `AGENT_TERMINAL_RESULT` | `PENDING` | |

## 2. Lane 状态表

状态枚举：`DISPATCHED | CLAIMED | SUCCESS | NEGATIVE_RESULT | PARTIAL | BLOCKED | FAILED`

| Lane | 报告路径 | 状态 | 核心证据指针 | 备注 |
| --- | --- | --- | --- | --- |
| R00 Currentness / gap map | `01_CURRENTNESS_AND_GAP_MAP.md` | `SUCCESS` | main `ee393ca2`；23 blob tree；`#2/#3/#4/#5/#6/#13/#15/#23/#29` 状态 | 24 项 gap 分类 G-01…G-24；do-not-redo 清单 |
| R01 Construct convergence deep audit | `02_CONSTRUCT_CONVERGENCE.md` | `SUCCESS` | 45 条带 DOI 指针；Sibley 2012 / Lewicki 1998 / Chivers 2010 / Tran 2019 | 13 构念 7 维 row-set；12 条 audit delta |
| R02 Semantic redundancy / double-count red audit | `02b_CONSTRUCT_REDUNDANCY_AUDIT.md` | `PARTIAL` → 修复后 `PARTIAL` | 34 条指针；Tran 2019 R²=.54；Montoya 2016/2007 | 18 条冗余边；MGS-A/B/C；R1–R11 残余；H1–H11 高危双计 |
| R03 Measurement instruments & proxy dictionary | `03_MEASUREMENT_INSTRUMENTS.md` | `SUCCESS` | 41 instrument family / 54 条目 | 达成 30+ 目标；G1–G10 instrument gap |
| R04 Quantitative dyadic / longitudinal dataset landscape | `04_DATASET_LANDSCAPE.md` | `PARTIAL` | 16 数据集；SHARE CoU §7 本地实抓；Add Health / UAS LLM 禁令实抓 | **四条件交集为空**；PARTIAL = 出口网络限制（见 §4 B-1） |
| R05 Statistical identification / estimation methods | `05_IDENTIFICATION_AND_STATISTICS.md` | `SUCCESS` | 109 指针；Hamaker 2015 / Lucas 2023 / Robitzsch 2025 | I1–I17 识别不可能；SD1–SD20 自我欺骗 |
| R06 Candidate transition-law families / falsifiability | `06_TRANSITION_LAWS.md` | `SUCCESS` | Joel 2020 PNAS；Schrodt 2014；Johnson 2022 PNAS | 5 律族 BMR/APES/DVA/RGM/RT，各带预登记证伪判据 |
| R07 Sparse input / missingness / uncertainty | `07_PARTIAL_OBSERVABILITY.md` | `SUCCESS` | Belnap K4 双序；QSR/Renz 2007；Kalai–Vempala；Pelessoni–Vicig 2022 | I1–I19 可检验不变量；**项目在 refinement/格上完全空白** |
| R08 Belief / observation / deception / nested knowledge | `08b_BELIEF_DECEPTION_KNOWLEDGE.md` | `SUCCESS` | 72 指针；W3C PROV；Kripke–Harman 修正 Kuhn 误引 | 最小 belief 层 8 槽；3 项 REJECT 过重形式化 |
| R09 Dynamic systems, path dependence, hysteresis, no-FSM | `09_DYNAMIC_SYSTEMS_AND_HYSTERESIS.md` | `SUCCESS` | 78 指针；Bühler & Orth 2022/2024/2025；Mayo 2021 meta ES=.09 | 修复后补齐 §8/§9；迟滞在二元数据上**存在性未知** |
| R10 Mutuality / asymmetry / power / dependence emergence | `10_MUTUALITY_POWER_DEPENDENCE.md` | `SUCCESS` | 59 指针；Bodenmann 2011 判别实验 N=443；Falconier 2015 N=17,856 | R2 需**改写非否决**；G1–G16 缺口 |
| R11 General Human Dyad scope audit | `11_GENERAL_HUMAN_DYADS_SCOPE.md` | `PARTIAL` → 修复后 `PARTIAL` | 60+ 指针；de Bel 2019 N=549；Bengtson 2002；Johnson 2006 | 24×10 矩阵；P-1…P-8；L-1…L-11 域泄漏；PARTIAL 见 §4 B-2 |
| R12 Computational relationship / ABM / microsimulation benchmark | `12_COMPUTATIONAL_MODELS_ABM.md` | `SUCCESS` | Windrum 2007；Galán 2009；Schindler 2013；Snijders 2010；Hills & Todd 2008 | **无一个可比先例**；SAOM 结构性排除；`JuSpace`/`smallslm`/`ASON` 证伪 |
| R13 LLM Skill / adaptive interview layer | `13_LLM_SKILL_INTERVIEW_LAYER.md` | `SUCCESS` | 70 指针；Gilardi 2023 vs Nakamura 2026 直接冲突；W3C PROV | 10 类幻觉失败；6 个 representation-faithfulness 指标 |
| R14 Paper positioning / novelty / reviewer-risk | `14_PAPER_POSITIONING_NOVELTY.md` | `SUCCESS` | PRQC 2000；Joel 2020；Finkel 2017；Eberhardt 2025 ω=.953 | 17 条 REUSE；F-1…F-20 禁止主张；M0–M9 里程碑；O-1…O-17 overclaim |
| R15 Case Bank expansion strategy | `15_CASEBANK_EXPANSION.md` | `PARTIAL` | 30 条指针；Find Case Law / LGSO / Mother&Baby Homes 实抓；`Zapp` 官方原文级 | 22+3+4 分四类；A01–A14 对抗件；T1–T5 DERIVED_TRANSFORM |
| R16 Empirical validation protocol join | `16_EMPIRICAL_VALIDATION_PROTOCOL.md` | `PARTIAL` | 24 条指针；Kapoor 2023 leakage 八分类；Dwork 2015 reusable holdout；SHARE CoU §7 **本地独立实抓** | 首次 dispatch 失败 → 完整重做；L1–L8 leakage；B0–B6 null；PARTIAL 见 §4 B-1 |
| R17 Independent red-team / falsifier search | `17_RED_TEAM_FALSIFIERS.md` | `SUCCESS` | 41 引用；Joel 2020；Segal & Fraley 2016；Eastwick 2011 | **独立性 CONFIRMED**；A1–A23 裁定（8 CHALLENGED / 8 CONTESTED / 3 UNCHALLENGED / 2 无反证）；F1–F11 证伪卡 |

> 报告路径前缀均为 `docs/research/overnight-2026-09-27/`。

### Wave 2 audit lane

| Lane | 报告路径 | 状态 | 备注 |
| --- | --- | --- | --- |
| A01 Evidence quality audit | `A01_EVIDENCE_QUALITY_AUDIT.md` | `IN_PROGRESS` | Wave 1 durable 后启动 |
| A02 Cross-lane contradiction / duplicate audit | `18_CROSS_LANE_CONFLICT_AUDIT.md` | `IN_PROGRESS` | Wave 1 durable 后启动 |
| A03 Falsifiability / hindsight-fitting audit | `A03_FALSIFIABILITY_HINDSIGHT_AUDIT.md` | `IN_PROGRESS` | Wave 1 durable 后启动 |
| A04 Citation / provenance audit | `A04_CITATION_PROVENANCE_AUDIT.md` | `IN_PROGRESS` | source 量级足够，按 Work Order 启动 |

## 3. 计数汇总

- Wave 1 lane 总数：**18**（R00–R17）
- Wave 1 child 数（实际派发）：**19**（含 R16 的一次失败 dispatch + 一次 repair）
- Repair pass 数：**3 lane**（R16 完整重做 / R09 补 §8–§9 / R02 与 R11 各一次窄修复）
- Wave 1 状态计数：`SUCCESS` **13** · `PARTIAL` **5**（R02 / R04 / R11 / R15 / R16）· `NEGATIVE_RESULT` 0 · `BLOCKED` 0 · `FAILED` 0（首派失败已由 repair 关闭）
- Wave 1 报告体量：**18 份 / 1,221,011 字节 / 11,328 行**
- 单 lane 自报去重指针数：R00 30+ · R01 45 · R02 34 · R03 41 family · R04 16 dataset · R05 109 · R06 33 · R07 33 · R08 72 · R09 78 · R10 59 · R11 60+ · R12 40 · R13 70 · R14 60+ · R15 30 · R16 24 · R17 41+3。**全 swarm 未做跨 lane 全局去重**（见 §4 B-3）
- 严肃候选 quantitative dyadic dataset：**16**（R04；目标 12+，达成；其中 `CALIBRATION_READY` 3）
- 已 catalog validated measurement instrument family：**41**（R03；目标 30+，达成）
- falsifiable transition-law family：**5**（R06：BMR / APES / DVA / RGM / RT；目标 3–5，达成）
- Case Bank 下一批候选：**30**（R15：22 narrative + 3 calibration + 4 tooling + 1 分离；目标 20–30，达成）
- 明确 counterexample / falsifier：**≥ 34**（R17 A1–A23 裁定 + F1–F11 证伪卡；R11 A-01–A-14；R15 A01–A14；目标 10+，达成）

## 4. 未解 blocker（Wave 1 结束时）

- **B-1｜网络出口限制，parent 无法修复**：R04 / R15 / R16 的 `PARTIAL` 主因是本环境出口对 `icpsr.umich.edu`(403)、`hrs.isr.umich.edu`(403/timeout)、`saflii.org`(403)、`courts.ie`、`wenshu.court.gov.cn`、`gutenberg.org`(timeout)、`gpair.wustl.edu` 等站点不可达。Work Order 要求「不得下载受限数据、不得绕过 access」，因此**不得**以任何方式规避。影响：三份 `CALIBRATION_READY` 数据集的**构念内容**（而非结构）未核实；R15 的 7 条来源仍为 `UNVERIFIED_CANDIDATE`。
- **B-2｜文献层面的未命中，非网络问题**：R11 若干 `UNVERIFIED_AGENT_RECALL` 条目（如 Gilligan 2017 ASR、Parsons & Bales 1955 原件）经 Crossref 检索未命中。R02 的「全候选电池单次 ESEM/bifactor 分析」在文献中可能本就不存在（`NEGATIVE`，非未找到）。
- **B-3｜跨 lane 全局去重未做**：各 lane 各自报数，同一来源可能被 2–3 个 lane 独立引用。全局去重与质量分级由 A04 执行。**在 A04 完成前，上表「单 lane 自报指针数」不可相加，也不可对外声称为 150+ 独立来源。**
- **B-4｜R09 迟滞在二元数据上无任何估计**：这是负结果，不是缺口。R09 明确记录迟滞所依赖的强耦合前提在多数真实 dyad 中不成立。
- **B-5｜`#20/#21/#22` 隔离 lane 的 durable 结果仍未知**：R13 记录的 U-5（fixture 上人工 verifier 的真实 ICR）因此无法回答。按隔离契约，本 attempt 不查。

> 终态 blocker 列表以 `19_SYNTHESIS_CANDIDATE.md` 与 `AGENT_TERMINAL_RESULT` comment 为准。
