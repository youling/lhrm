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

## 0-R3. Round 3 修复记录（`A2` · synthesis + reasoning repair）

> 本节由 Round-3 repair child `A2` 写入。**权威依据**：`#30 comment 5854920569`（`ARCHITECT_ADJUDICATION_V1`）
> 与 `#30 comment 5854930069`（`ARCHITECT_ROUND3_DISPATCH_V1`）。
> **本节只记录本文件被改了什么、依据哪条裁决、以及哪些旧文本被取代。旧文本一律逐字保留在下方
> `SUPERSEDED_BY_ADJUDICATION_V1` 块内，不删除。**

| 项 | 值 |
| --- | --- |
| `child_id` | `A2` |
| `work_coordinate` | `youling/lhrm#30@round3-adjudication-implementation-v1` |
| `base_sha` | `8adcf0bacc45c0feb5c14e65e2a45346dd488b43` |
| `branch` | `r3/a2` |
| 落地裁决 | **X-8** · **X-12 / C-P9** · **X-14** · Gate rationale（R-A1/R-A2/R-A3/H-A1/H-A2/H-A3）· **C-1…C-4**（sibling `A1` 移交） |
| 未落地（有意） | 见 packet `deliberately_not_applied`：X-1…X-7 / X-10 / X-11 / X-13 的**文件级**改写落在 `A3` / `A4` 的白名单文件上 |
| 边界 | 未改 `docs/foundation/*`、`AGENTS.md`、`docs/validation/*`；未跑 Gate A/B/C；未 merge / push / 开 PR；未读/执行/引用 `#20`/`#21`/`#22`；未碰 Eye/Juece；无受限数据下载 |

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
| Wave 2 audits | `SUCCESS` | A01–A04 四份报告已 durable；A01/A04 触发的 load-bearing 引用修复已收口 |
| Audit 触发的引用修复 | `SUCCESS` | 2 轮窄修复，共 5 个文件；**唯一被实测推翻的审计断言已记录**（见 §5） |
| `19_SYNTHESIS_CANDIDATE.md` | `SUCCESS` | parent join 交付 |
| Research PR | 见 `AGENT_TERMINAL_RESULT` | |
| `AGENT_TERMINAL_RESULT` | 见 `AGENT_TERMINAL_RESULT` | |

## 2. Lane 状态表

状态枚举：`DISPATCHED | CLAIMED | SUCCESS | NEGATIVE_RESULT | PARTIAL | BLOCKED | FAILED`

| Lane | 报告路径 | 状态 | 核心证据指针 | 备注 |
| --- | --- | --- | --- | --- |
| R00 Currentness / gap map | `01_CURRENTNESS_AND_GAP_MAP.md` | `SUCCESS` | main `ee393ca2`；23 blob tree；`#2/#3/#4/#5/#6/#13/#15/#23/#29` 状态 | 24 项 gap 分类 G-01…G-24；do-not-redo 清单 |
| R01 Construct convergence deep audit | `02_CONSTRUCT_CONVERGENCE.md` | `SUCCESS` | 45 条带 DOI 指针；Sibley 2012 / Lewicki 1998 / Chivers 2010 / Tran 2019 | 13 构念 7 维 row-set；12 条 audit delta |
| R02 Semantic redundancy / double-count red audit | `02b_CONSTRUCT_REDUNDANCY_AUDIT.md` | `PARTIAL` → 修复后 `PARTIAL` | 34 条指针；Tran 2019 R²=.54；Montoya 2016/2007 | 18 条冗余边；MGS-A/B/C；R1–R11 残余；H1–H11 高危双计 |
| R03 Measurement instruments & proxy dictionary | `03_MEASUREMENT_INSTRUMENTS.md` | `SUCCESS` | 41 instrument family / 54 条目 | 达成 30+ 目标；G1–G10 instrument gap |
| R04 Quantitative dyadic / longitudinal dataset landscape | `04_DATASET_LANDSCAPE.md` | `PARTIAL` | 16 数据集；SHARE CoU §7 本地实抓；Add Health / UAS LLM 禁令实抓 | **在本 lane 已审计的 16 个数据集范围内，四条件交集为空**（Round 3 收窄自「交集为空」，见 §4-R3-1）；PARTIAL = 出口网络限制（见 §4 B-1） |
| R05 Statistical identification / estimation methods | `05_IDENTIFICATION_AND_STATISTICS.md` | `SUCCESS` | 109 指针；Hamaker 2015 / Lucas 2023 / Robitzsch 2025 | I1–I17 识别不可能；SD1–SD20 自我欺骗 |
| R06 Candidate transition-law families / falsifiability | `06_TRANSITION_LAWS.md` | `SUCCESS` | Joel 2020 PNAS；Schrodt 2014；Johnson 2022 PNAS | 5 律族 BMR/APES/DVA/RGM/RT，各带预登记证伪判据 |
| R07 Sparse input / missingness / uncertainty | `07_PARTIAL_OBSERVABILITY.md` | `SUCCESS` | Belnap K4 双序；QSR/Renz 2007；Kalai–Vempala；Pelessoni–Vicig 2022 | I1–I19 可检验不变量；**项目在 refinement/格上完全空白** |
| R08 Belief / observation / deception / nested knowledge | `08b_BELIEF_DECEPTION_KNOWLEDGE.md` | `SUCCESS` | 72 指针；W3C PROV；Kripke–Harman 修正 Kuhn 误引 | 最小 belief 层 8 槽；3 项 REJECT 过重形式化 |
| R09 Dynamic systems, path dependence, hysteresis, no-FSM | `09_DYNAMIC_SYSTEMS_AND_HYSTERESIS.md` | `SUCCESS` | 78 指针；Bühler & Orth 2022/2024/2025；Mayo 2021 meta ES=.09 | 修复后补齐 §8/§9；迟滞在二元数据上**存在性未知** |
| R10 Mutuality / asymmetry / power / dependence emergence | `10_MUTUALITY_POWER_DEPENDENCE.md` | `SUCCESS` | 59 指针；Bodenmann 2011 判别实验 N=443；Falconier 2015 N=17,856 | R2 需**改写非否决**；G1–G16 缺口 |
| R11 General Human Dyad scope audit | `11_GENERAL_HUMAN_DYADS_SCOPE.md` | `PARTIAL` → 修复后 `PARTIAL` | 60+ 指针；de Bel 2019 N=549；Bengtson 2002；Johnson 2006 | 24×10 矩阵；P-1…P-8；L-1…L-11 域泄漏；PARTIAL 见 §4 B-2 |
| R12 Computational relationship / ABM / microsimulation benchmark | `12_COMPUTATIONAL_MODELS_ABM.md` | `SUCCESS` | Windrum 2007；Galán 2009；Schindler 2013；Snijders 2010；Hills & Todd 2008 | **在本 lane 已检索场所内未找到可比先例**（Round 3 收窄自「无一个可比先例」，见 §4-R3-1）；SAOM 结构性排除；`JuSpace`/`smallslm`/`ASON` 证伪 |
| R13 LLM Skill / adaptive interview layer | `13_LLM_SKILL_INTERVIEW_LAYER.md` | `SUCCESS` | 70 指针；Gilardi 2023 vs Nakamura 2026 直接冲突；W3C PROV | 10 类幻觉失败；6 个 representation-faithfulness 指标 |
| R14 Paper positioning / novelty / reviewer-risk | `14_PAPER_POSITIONING_NOVELTY.md` | `SUCCESS` | PRQC 2000；Joel 2020；Finkel 2017；Eberhardt 2025 ω=.953 | 17 条 REUSE；F-1…F-20 禁止主张；M0–M9 里程碑；O-1…O-17 overclaim |
| R15 Case Bank expansion strategy | `15_CASEBANK_EXPANSION.md` | `PARTIAL` | 30 条指针；Find Case Law / LGSO / Mother&Baby Homes 实抓；`Zapp` 官方原文级 | 22+3+4 分四类；A01–A14 对抗件；T1–T5 DERIVED_TRANSFORM |
| R16 Empirical validation protocol join | `16_EMPIRICAL_VALIDATION_PROTOCOL.md` | `PARTIAL` | 24 条指针；Kapoor 2023 leakage 八分类；Dwork 2015 reusable holdout；SHARE CoU §7 **本地独立实抓** | 首次 dispatch 失败 → 完整重做；L1–L8 leakage；B0–B6 null；PARTIAL 见 §4 B-1 |
| R17 Independent red-team / falsifier search | `17_RED_TEAM_FALSIFIERS.md` | `SUCCESS` | 41 引用；Joel 2020；Segal & Fraley 2016；Eastwick 2011 | **独立性 CONFIRMED**；A1–A23 裁定（8 CHALLENGED / 8 CONTESTED / 3 UNCHALLENGED / 2 无反证）；F1–F11 证伪卡 |

> 报告路径前缀均为 `docs/research/overnight-2026-09-27/`。

### Wave 2 audit lane

| Lane | 报告路径 | 状态 | 备注 |
| --- | --- | --- | --- |
| A01 Evidence quality audit | `A01_EVIDENCE_QUALITY_AUDIT.md` | `SUCCESS` | 353 unique DOI，95.5% Crossref 解析；**3 条 BLOCKER**（承重指针错误，修正值已核实并已应用） |
| A02 Cross-lane contradiction / duplicate audit | `18_CROSS_LANE_CONFLICT_AUDIT.md` | `SUCCESS` | 顶层发现：Wave 1 拓扑为「17 条独立单点 + 1 条 join lane」；`PPR` 层位三方互斥；12 条 `NARROW_REPAIR_REQUEST` |
| A03 Falsifiability / hindsight-fitting audit | `A03_FALSIFIABILITY_HINDSIGHT_AUDIT.md` | `SUCCESS` | Gate A `EXECUTABLE_BUT_NON_FALSIFIABLE`；Gate B/C 既不可证伪也不可执行；**Gate 在判据原文下不存在会被算作失败的结果**（Round 3 替换了原「**§2.6 结构上无法触发**」的表述——缺陷保留，支撑论证换掉，见 `19` §1 `N-A8` 与本文件 §4-R3-2）；机器核验 0 条判据被削弱 |
| A04 Citation / provenance audit | `A04_CITATION_PROVENANCE_AUDIT.md` | `SUCCESS` | 1,199 原始出现 → 642 distinct pointer → 533 distinct source；`PEER_REVIEWED_*` **350**；DOI 覆盖 340/340；6 条 MAJOR |

## 2b. Audit 触发的引用修复（已收口）

A01 与 A04 各自独立实测核出承重引用的 DOI / 期刊 / 作者归属错误。修正值均经实时验证后应用。

| 文件 | 缺陷 | 修正 | 状态 |
| --- | --- | --- | --- |
| `03_MEASUREMENT_INSTRUMENTS.md` | `10.1037/2021-17028-001` 不解析 | `10.1037/pas0000986`（Crasta et al. 2021, *Psychological Assessment* 33(4):338–355） | 已应用 |
| `14_PAPER_POSITIONING_NOVELTY.md` | `10.1609/aaai.v35i1.16792` 不解析 | `10.1609/aaai.v35i7.16792` | 已应用 |
| `10_MUTUALITY_POWER_DEPENDENCE.md` | `10.3389/fpsyg.2019.00571` 归给 Lehne & Bodenmann | 实为 **Falconier & Kuhn (2019)** | 已应用 |
| `10_MUTUALITY_POWER_DEPENDENCE.md` | `10.2307/2092623` 实为 Gouldner (1960) | `10.2307/2089716` = Emerson (1962)，与正文 byline 一致 | 已应用 |
| `08b_BELIEF_DECEPTION_KNOWLEDGE.md` | 6 处系统性作者/期刊误引（含 `Audi` → `Goldberg & Henderson`、PII 混入 DOI 槽） | **8 处**逐条修正，8/8 经 Crossref 独立复核 | 已应用 |
| `08b_BELIEF_DECEPTION_KNOWLEDGE.md` | `[S13]` `Borges, M. (2013)` | `Sharon, A., & Spectre, L. (2010)`，DOI `10.1007/s11098-008-9330-1` | 已应用 |
| `04_DATASET_LANDSCAPE.md` | `10.1007/s11238-014-9448-x` 期刊记为 *J Behav Dec Making* | 实为 ***Theory and Decision*** 77(3):389–401 | 已应用 |
| `05_IDENTIFICATION_AND_STATISTICS.md` | `10.1177/019251391012001003` 期刊记为 *JMF*、作者缺失 | *Journal of Family Issues* 12(1):22–42；Bumpass, Martin & Sweet (1991) | 已应用 |
| `02b_CONSTRUCT_REDUNDANCY_AUDIT.md` | `10.31234/osf.io/f6wbn` 404 | 追加版本后缀 → 302 解析 | 已应用 |

**被实测推翻的审计断言（重要流程观察）——本段 Round 3 已重写，原文见下方 `SUPERSEDED` 块。**

- **原文（Round 1，已被取代）**：「A04 主张 `10.31234/osf.io/…` 前缀/后缀结构非法、应改为 `10.31219/…`。修复 child 实测 `10.31234` **解析（302）**、`10.31219` **404**；`10.31234` 是 OSF-preprint 前缀，`10.31219` 是 OSF **project** 前缀。」
- **该修改未应用**——若应用会把 live DOI 变成 404。
- **规则沉淀（不变）**：审计 child 的断言必须经独立实测复核后才能落到 durable artifact。

**🔴 Round 3 更正 —— 上面引用的原文本身有两处错（`M-1` / sibling `A1` 移交项 `C1`）。**

| # | 原文断言 | 裁决 | 实测依据 |
| --- | --- | --- | --- |
| 1 | 「`10.31219` 是 OSF **project** 前缀」（隐含 `10.31234` 是 preprint 专用前缀） | **WRONG**。`10.31234` 与 `10.31219` **两个前缀都 live**，且在 Crossref prefix registry 里**注册者是同一家**：`Center for Open Science` | prefix registry 逐条查 |
| 2 | 「`10.31219` **404**」 | **REFUTED**。`10.31219/osf.io/gu8z7` → 302 → **终态 200**。真正 404 的是**没有版本后缀**的写法：`10.31234/osf.io/f6wbn`（无 `_v1`）与 `10.31219/osf.io/f6wbn`（前缀错配） | 6 个 identifier 逐条 HEAD/GET |

- **真实缺陷（唯一可辩护的修法）**：`f6wbn` **只在 `10.31234` + `_v1` 形态下注册** ⇒ 修法是**补版本后缀**，**不是换前缀**。
- **为什么这条必须改（下游风险）**：若下游照原文去「把 `10.31234/osf.io/…` 统一改成 `10.31219/osf.io/…`」，它会把 **live 指针 `10.31219/osf.io/gu8z7` 变成 404**，且不修复任何东西。本 child 把它登记为 `REJECTED_WITH_REASON`，与 `A04` §10 P2 的同向结论一致。
- **本 child（`A2`）2026-09-27 独立复验的 6 个 identifier**（只读 HEAD/GET，**非新文献扫描**）：
  `10.31234/osf.io/f6wbn_v1` **200** · `10.31219/osf.io/gu8z7` **200** · `10.31234/osf.io/rs7eu_v1` **200** ·
  `10.31234/osf.io/dus42` **200** · `10.31234/osf.io/f6wbn`（无后缀）**404** · `10.31219/osf.io/f6wbn` **404**。
  两前缀注册者均为 `Center for Open Science`。
- **依据**：`REVIEW_SWARM_MANIFEST.md` §7 `M-1`；`REJECTED_OR_WEAK_FINDINGS.md` `R-B5`；`ADJUDICATION_V1` §D「Apply the 10 EV2 bookkeeping/citation corrections」。

**未修复且如实保留**：
- `05_…` 一处 DOI（`10.3102/10769986024002179` 实为 Vermunt et al. 1999，非所引 Hoffmann 1985）——A01 **未提供**已核实的替换指针，修复 child **拒绝猜测**，原文未动。
- ~~`08b_…` `[S15]` 年份自相矛盾（A01 表格给 2008、其 action 行给 2010）——只改作者，未改年份。~~ **【Round 3 更正：原文在「年份」与「性质」两处都错，标 `SUPERSEDED_BY_ADJUDICATION_V1`（`M-4` / 移交项 `C3`）】**
  - **实测**：`08b_BELIEF_DECEPTION_KNOWLEDGE.md:755` 的 `[S15]` 条目是
    `**[S15]** "Convincing ourselves: accuracy motives and rationalization." *Synthese* (2025). https://link.springer.com/article/10.1007/s11229-025-05259-1 — CITED_PRIMARY · med`。
  - **该条目根本没有作者字段** ⇒「只改作者」这个描述**不成立**。
  - **其年份是 `2025`**，不是原文所说的 2008 / 2010。
  - `A01_EVIDENCE_QUALITY_AUDIT.md:456` 给的也正是 `2025` + `Wehofsits, Anna` ⇒ **A01 是对的，本 manifest 的转述在年份与性质上都错。**
  - **未被修复的残余**：`08b:755` 至今**仍无作者字段**。补作者是一次书目编辑（`Wehofsits, Anna`），**不在本 Work Order 授权内**，已登记为待 Architect 处置项。
  - **依据**：`REVIEW_SWARM_MANIFEST.md` §7 `M-4`；`REJECTED_OR_WEAK_FINDINGS.md` `R-B9`（`J-C21` 成立且更错）。
- A01 `NR-08-4` 的散文把第 5 作者写成 "Tomlinson, Eastwick"，Crossref 实为 **Troister, T.** ——按 Crossref 应用，A01 该行待 Architect 更正。
- `03_…` 一处 `UNVERIFIED_DOI` 标注现已过期（新 DOI 可解析）——属验证状态标注而非书目字符串，留待 Architect 处置。
- A04 自身报告把 `10.1007/s11238-014-9448-x` 标为 "Bodenmann & Frighi 2011"，Crossref 实为 Bacon, Conte & Moffatt (2014)——A04 报告自身的作者错误，留在 audit 报告中作为审计质量记录。

## 3. 计数汇总

- Wave 1 lane 总数：**18**（R00–R17）
- Wave 1 child 数（实际派发）：**19**（含 R16 的一次失败 dispatch + 一次 repair）
- Repair pass 数：**3 lane**（R16 完整重做 / R09 补 §8–§9 / R02 与 R11 各一次窄修复）
- Wave 1 状态计数：`SUCCESS` **13** · `PARTIAL` **5**（R02 / R04 / R11 / R15 / R16）· `NEGATIVE_RESULT` 0 · `BLOCKED` 0 · `FAILED` 0（首派失败已由 repair 关闭）
- Wave 1 报告体量：**18 份 / 1,221,011 字节 / 11,328 行**
- 单 lane 自报去重指针数：R00 30+ · R01 45 · R02 34 · R03 41 family · R04 16 dataset · R05 109 · R06 33 · R07 33 · R08 72 · R09 78 · R10 59 · R11 60+ · R12 40 · R13 70 · R14 60+ · R15 30 · R16 24 · R17 41+3。**各 lane 自报数不可相加**（Round 3 复算见 §4-R3-2）
- **【Round 3 机器复算，`M-2` / `M-6` / 移交项 `C3`】** 把上面 18 个 lane 的自报数按「`+` 取下界、`41+3` 记作 `44`」相加 = **878**（`+` 全取下界则为 **875**）。相对 **533** distinct source = **1.65×**；相对 **350** `PEER_REVIEWED_*` = **2.51×**。**本 child 逐项解析本行 addend 后相加，未复制任何旧总数。**
  - **四个数是四个不同量纲，不可相互校验或替代**：`878`（lane 自报数**之和**）· `1,199`（原始出现次数）· `642`（distinct pointer）· `533`（distinct source）。
- **A04 实测全局去重口径（权威）**：1,199 原始指针出现 → 642 distinct pointer → **533 distinct source**；其中 `PEER_REVIEWED_PRIMARY + PEER_REVIEWED_REVIEW` = **350**。**#30 的 150+ 去重目标以 A04 口径达成（2.3×）**
- 严肃候选 quantitative dyadic dataset：**16**（R04；目标 12+，达成；其中 `CALIBRATION_READY` 3）
- 已 catalog validated measurement instrument family：**41**（R03；目标 30+，达成）
- falsifiable transition-law family：**5**（R06：BMR / APES / DVA / RGM / RT；目标 3–5，达成）
- Case Bank 下一批候选：**30**（R15：22 narrative + 3 calibration + 4 tooling + 1 分离；目标 20–30，达成）
- 明确 counterexample / falsifier：**≥ 34**（R17 A1–A23 裁定 + F1–F11 证伪卡；R11 A-01–A-14；R15 A01–A14；目标 10+，达成）

## 4. 未解项（Wave 1 结束时）

> **🔴 Round 3：§4 不再是一份独立 register。** 原 §4 与 `19_SYNTHESIS_CANDIDATE.md` §8 各有一套 `B-n` 编号，
> 两者对 `B-3` 指不同事物，且**成员几乎不相交**（只有 `B-6 ↔ C-3` 一项对应）。
> 依 `ADJUDICATION_V1` **X-12** 与 `CANONICAL_CHANGE_PROPOSALS.md` **C-P9**：
> **唯一编号空间是 `19_SYNTHESIS_CANDIDATE.md` §8 的 `R-B-*` 分类登记表。**
> 本节现在**只提供 Wave-1 结束时的状态注记，不引入任何新编号**。
> 裁决依据：`REJECTED_OR_WEAK_FINDINGS.md` `R-4`（三处 register 缺陷）、`R-L4`、`R-L6`；
> `HIGH_CONFIDENCE_FINDINGS.md` `H-F34` / `H-F39`。

| `19` §8 的 id | Wave 1 结束时本 manifest 怎么记的 | 分类（`19` §8） |
| --- | --- | --- |
| `R-B-1` | 出口网络限制，parent 无法修复（`icpsr` 403 / `hrs` / `saflii` 403 / `courts.ie` / `wenshu` / `gutenberg`） | `C` 环境/治理限制 |
| `R-B-2` | 文献层面检索未命中（Gilligan 2017 ASR、Parsons & Bales 1955 原件等） | `C` 环境/治理限制 |
| `R-B-3` | R02「全候选电池单次 ESEM/bifactor」 | `D` **负结果，不是 blocker** |
| `R-B-4` | R09 迟滞在二元数据上无任何估计 | `D` **负结果，不是 blocker** |
| `R-B-5` | `#20/#21/#22` 隔离 lane 的 durable 结果仍未知 | `C` 环境/治理限制 |
| `R-B-6` | Gate A/B/C 在当前定义下不能产生否决 | `A` 架构设计任务 |
| `R-B-7` | `Liking ↔ RomanticAttraction` 仍缺同样本斜交因子相关 / CFA 判别检验 | `B` 研究设计任务 |
| `R-B-8` | `OutcomeDependence` 关系级可测性无任何公开工具 | `B` 研究设计任务 |
| `R-B-9` | 跨 lane 全局去重（= 原 `B-3` + 原 `B-9`，同一件事被记了两次） | 见 §4-R3-2 |
| `R-B-10` | `PPR` / `Satisfaction` 层归属 | `A` 架构设计任务 |
| `R-B-11` | `OutcomeDependence` 四种互斥 ontology | `A` 架构设计任务 |
| `R-B-12` | `Unknown` 类型学 | `A` 架构设计任务 |
| `R-B-13` | Gate C 前置条件与 Gate C 互锁（排序死锁） | `A` 架构设计任务 |
| `R-B-14` | 尺度冲突（`CR-7`） | `E` 尺度冲突 |

### §4-R3-1 Round 3 收窄的「无/不存在」表述（**X-14**：search-scope，不是 field-wide absence）

裁决：`ADJUDICATION_V1` **X-14** —— 「No qualifying dataset found in this audited landscape」**允许**；
「the intersection is empty in the field」**不允许**。同一规则适用于格统计与文献/工具缺失陈述。

| # | 原文（逐字） | 收窄后 | 依据 |
| --- | --- | --- | --- |
| X-14-1 | R04 行「**四条件交集为空**」（§2 lane 表） | **在本 lane 已审计的 16 个数据集范围内，四条件交集为空** | `R-0.2` / `C-C29` `CONTESTED` |
| X-14-2 | R12 行「**无一个可比先例**」（§2 lane 表） | **在本 lane 已检索场所内未找到可比先例** | `R-0.1` / `G-C17` `WRONG-SCOPE` |
| X-14-3 | B-2 内的「R02 的『全候选电池单次 ESEM/bifactor 分析』在文献中**可能本就不存在**（`NEGATIVE`，非未找到）」 | **本 lane 的检索未发现**；**存在性否定需独立系统检索** | `R-0.4` / `A-C29` `WRONG-SCOPE` |

> **R04 的结构性结果**在 `19` §5 一并收窄（`R-0.2` / `C-C29`）——「这是**本次检索**的结构性结果」，
> 且 **Add Health 从未进入结构检验**（`C-C20` / `C-C26`：`ACCESS_BLOCKED` 是**许可**轴，不是结构轴）。

### §4-R3-2 Round 3 更正：跨 lane 全局去重的记账（`M-2` / `M-6` / 移交项 `C3`）

> **原文（Round 1，已被取代 —— 逐字保留）**：
> 「**B-9（跨 lane 全局去重）｜已完成，但不得对外声称 lane 自报数之和**：A04 实测 1,199 原始指针出现 →
> 642 distinct pointer → **533 distinct source**，其中 `PEER_REVIEWED_PRIMARY + REVIEW` = **350**。
> 各 lane 自报数相加 ≈1,201，**高估 2.3–3.4×**。两个独立机制：跨 lane 重复（单个来源被最多 7 个 lane 引 13 次）
> + 书写形态重复（340 个 DOI 有 740 次出现）。」
>
> **取代它的表述**：各 lane 自报数相加 = **878**（不是 ≈1,201）。相对 **533** distinct source 高估 **1.65×**、
> 相对 **350** 高估 **2.51×**（不是「2.3–3.4×」）。`1,199` 是**原始出现次数**，与「lane 内去重后计数」**不是同一量纲**。
> **去重链 `1,199 → 642 → 533` 与 `350` 本身未被本轮触及，仍然成立。**
> **依据**：`REVIEW_SWARM_MANIFEST.md` §7 `M-2`；`REJECTED_OR_WEAK_FINDINGS.md` `R-B4`；
> `HIGH_CONFIDENCE_FINDINGS.md` `H-B3`（`533` 与 `1,201` 是两笔账）。**本 child 逐项重算，未复制旧总数。**

**同时修掉的三处 register 缺陷**（`R-4`）：

1. **`B-3` 编号冲突** —— 本 manifest §4 曾同时用 `B-3`（= 跨 lane 全局去重，指向 `§4 B-9`）与 `B-9`（= 同一件事）指同一项。
   ⇒ 现改为单一 `R-B-9`。
2. **成员不相交** —— 本 manifest §4 的 `B-1…B-9` 与 `19` §8 的 `B-1…B-8` **只有 `B-6 ↔ C-3` 一项对应**；
   `C-1`/`C-2`/`C-4`/`C-5`/`C-6` 在 §8 无编号。⇒ 这**不是「编号错乱」，是「分母不同」**。
   现两份文件共用 `19` §8 的一个编号空间。
3. **`B-4` 双重分类** —— §1 `A9` 当作重要负结果，§8 当作 blocker。
   ⇒ 现归入 `D` 类，**从 blocker 列表移出**。

**Gate 一条（`R-B-6`）的论证已在 Round 3 换掉，缺陷保留**：

> **原文（Round 1，已被取代 —— 逐字保留）**：
> 「**B-6（来自 A03，阻塞级）｜Gate A/B/C 在当前定义下不能产生否决**：A03 三项可复现检验判定 Gate A
> `EXECUTABLE_BUT_NON_FALSIFIABLE`、Gate B/C 既不可证伪也不可执行；`PARAMETER_CONVERGENCE_V0_1.md` §2.6
> （**唯一能删除 construct 的准入侧判据**）结构上无法触发 ⇒ 8 项 candidate basis 单调增长，`MERGE` 与 `REJECT`
> **从未被签发过一次**。**修复需改 canonical，本 Work Order 明确禁止。**」
>
> **取代它的表述（缺陷保留，两条支撑论证删除）**：
> - **保留的缺陷**：当前 Gate A/B/C 在判据原文下**不存在会被算作失败的结果**；`MAPPING_FAILURE` **类型上不可达**。
> - **删除的支撑 (a)**：「`§2.6` 是**唯一**能删除 construct 的准入侧判据」—— **假**。
>   六条准入判据中**只有一条用删除框架（`§2.6`）**、**两条用降级框架（`§2.2` / `§2.5`）**、
>   **三条连后果句都没有（`§2.1` / `§2.3` / `§2.4`）**；且**六条全部**无 procedure / required evidence /
>   output field / threshold / designated executor。**（本 child 逐行读 `PARAMETER_CONVERGENCE_V0_1.md:45–:86` 复核。）**
> - **删除的支撑 (b)**：「`MERGE` 与 `REJECT` **从未被签发过一次**」—— **项目层为假**。
>   `PARAMETER_CONVERGENCE_V0_1.md:499` / `:505`（`§9 R4` / `R5`）各含一个 `REJECT`；本次 attempt 全域另有
>   **≥8 处** `REJECT` 承载行（`08b` 12 行 / `A03` 7 行 / `10` 3 行 / `01` 3 行 / `02b` 2 行 等）。
>   **正确表述**：**8 项 basis 从未被一个「能失败的门」删减过一条**；项目确实签发过 `REJECT`，
>   但那些**全部是 drafting 时的散文判断，没有一条是由 §2 判据或 §15 门跑出来的**（**无执行记录**）。
> - **严重性已降级**（`R-A3` / `EV1`）：从「昂贵 canonical patch + 重跑 Fixture」降为
>   **约 5–8 句文档编辑 + 1 个 ablation 步骤定义 + 1 个诊断枚举值**。**不需要新文献、不需要新数据、不需要新模型。**
> - **依据**：`REJECTED_OR_WEAK_FINDINGS.md` `R-A1` / `R-A2` / `R-A3`；`HIGH_CONFIDENCE_FINDINGS.md`
>   `H-A1` / `H-A2` / `H-A3`；`CANONICAL_CHANGE_PROPOSALS.md` **C-P1**；`ADJUDICATION_V1` §D。
>   **完整的新论证见 `19_SYNTHESIS_CANDIDATE.md` §1 `N-A8`。**

> **终态未解项以 `19_SYNTHESIS_CANDIDATE.md` §8 的 `R-B-*` 分类登记表为准**
> （`AGENT_TERMINAL_RESULT` comment 为同源的 terminal snapshot）。
> **`MERGE` 与 `REJECT` 从未被签发过一次**是本 manifest 内的**唯一失效指针**（原「终态 blocker 列表以 `19` §8 与
> `AGENT_TERMINAL_RESULT` comment 为准」指向两份成员不相交的 register）——现两份文件指向**同一份**登记表。

---

## 5-R3. `SUPERSEDED_BY_ADJUDICATION_V1` 索引（`00_MANIFEST.md` 侧）

> 格式：`旧文本（逐字） → 取代它的表述 → 依据`。
> **全部旧文本已就地保留在上文对应位置的引用块 / 划删除线中，不删除。**
> 本索引是 parent 生成 `SUPERSEDED_BY_REPAIR` 标记所需的机器可 grep 清单。

| # | 本文件旧文本（逐字） | 取代它的表述 | 依据 |
|---|---|---|---|
| `M-S1` | 「`10.31219` 是 OSF **project** 前缀」 | 两个前缀**都 live**，注册者同为 `Center for Open Science` | `M-1` / `R-B5`；本 child 复验 6 个 identifier |
| `M-S2` | 「修复 child 实测 …… `10.31219` **404**」 | `10.31219/osf.io/gu8z7` → 302 → **终态 200**；真 404 的是**无版本后缀**的 `10.31234/osf.io/f6wbn` 与前缀错配的 `10.31219/osf.io/f6wbn` | 同上 |
| `M-S3` | 「**该修改未应用**——若应用会把两个 live DOI 变成 404」（作为对 A04 主张的裁决） | 结论方向保留，**理由换掉**：`f6wbn` 只在 `10.31234` + `_v1` 注册 ⇒ 修法是**补版本后缀**，不是换前缀 | `M-1` |
| `M-S4` | `08b` 行「7 处逐条修正，7/7 经 Crossref 独立复核」 | **8 处逐条修正，8/8**（`git show 8adcf0b -- 08b` 的 `[S2][S12][S13][S34][S37][S51][S60][S70]`） | `M-3` / `R-B8`（`J-C20`） |
| `M-S5` | 「`08b_…` `[S15]` 年份自相矛盾（A01 表格给 2008、其 action 行给 2010）——只改作者，未改年份。」 | `08b:755` 的 `[S15]` **根本没有作者字段**；其年份是 **2025**；`A01:456` 给的正是 `2025` + `Wehofsits, Anna` ⇒ **A01 是对的，本 manifest 的转述在年份与性质上都错** | `M-4` / `R-B9`（`J-C21`） |
| `M-S6` | R04 行「**四条件交集为空**」 | **在本 lane 已审计的 16 个数据集范围内**，四条件交集为空 | `X-14` / `R-0.2` / `C-C29` |
| `M-S7` | R12 行「**无一个可比先例**」 | **在本 lane 已检索场所内未找到**可比先例 | `X-14` / `R-0.1` / `G-C17` |
| `M-S8` | B-2 内「R02 的『全候选电池单次 ESEM/bifactor 分析』在文献中**可能本就不存在**（`NEGATIVE`，非未找到）」 | **本 lane 的检索未发现**；存在性否定需独立系统检索 | `X-14` / `R-0.4` / `A-C29` |
| `M-S9` | B-9「各 lane 自报数相加 ≈**1,201**，**高估 2.3–3.4×**」 | 相加 = **878**；相对 533 高估 **1.65×**、相对 350 高估 **2.51×**。`1,199` 是原始出现次数，**不同量纲** | `M-2` / `M-6` / `R-B4` / `H-B3`；本 child 逐项重算 |
| `M-S10` | B-3「**跨 lane 全局去重已由 A04 完成**：见 §4 B-9」 | 与 B-9 **同一件事两个编号** ⇒ 合并为单一 `R-B-9` | `R-4` 第 1 点 / `H-F34` |
| `M-S11` | B-6「`PARAMETER_CONVERGENCE_V0_1.md` §2.6（**唯一能删除 construct 的准入侧判据**）结构上无法触发 ⇒ …… `MERGE` 与 `REJECT` **从未被签发过一次**」 | 缺陷保留；**两条支撑删除**：六条判据里 1 删 / 2 降 / 3 无后果、全部无 procedure/evidence/output/threshold/executor；项目层 `REJECT` 存在（`PARAMETER:499` / `:505` + 全域 ≥8 处），但**无执行记录** | `R-A1` / `R-A2` / `R-A3` / `H-A1` / `H-A2` / `C-P1` |
| `M-S12` | 「终态 blocker 列表以 `19_SYNTHESIS_CANDIDATE.md` §8 与 `AGENT_TERMINAL_RESULT` comment 为准」 | 唯一编号空间是 `19` §8 的 `R-B-*` 分类登记表；本文件 §4 只提供状态注记、**不引入新编号** | `X-12` / `C-P9` / `R-4` 第 2 点 / `H-F39` |
| `M-S13` | §2 Wave 2 表 A03 行「**§2.6 结构上无法触发**」 | **Gate 在判据原文下不存在会被算作失败的结果**（缺陷保留，支撑换掉） | `R-A1` / `R-A2` |

### 5-R3.1 明确**未改**的（`C4` 移交项 · 不得连带删除）

| 位置 | 文本 | 为什么必须留着 |
|---|---|---|
| `00_MANIFEST.md` §3「**`#30` 的 150+ 去重目标以 A04 口径达成（2.3×）**」 | `350/150` = Work-Order 达成倍数 | **这是一个不同的、合法的比率**，只是与 §4 B-9 那个错误的「2.3–3.4× 高估倍数」**同名**。**修 B-9 不得删掉本行。**（`EV2` §5.11 明确提醒；sibling `A1` 移交项 `C4`） |

### 5-R3.2 本 child 的复算台账

| # | 复算对象 | 方法 | 结果 |
|---|---|---|---|
| `V1` | lane 自报数之和 | 解析 §3 单-lane 行的 18 个 addend 后脚本相加；`+` 取下界、`41+3` 记 44 | **878**（`+` 全取下界 = **875**）· 18/18 解析成功 |
| `V2` | 两个倍率 | `878/533`、`878/350` | **1.6473 → 1.65×** · **2.5086 → 2.51×** |
| `V3` | `08b` 修复数 | `git show 8adcf0b -- 08b` 的 `+` 行上的 `[S*]` 标记 | **8** 个：`[S2][S12][S13][S34][S37][S51][S60][S70]` |
| `V4` | `[S15]` 性质与年份 | 读 `08b:755` + `A01:456` | **无作者字段**；年份 **2025**；A01 给 `Wehofsits, Anna` |
| `V5` | OSF 两前缀 | 6 个 identifier 只读 HEAD/GET + prefix registry | `f6wbn_v1` 200 · `gu8z7` 200 · `rs7eu_v1` 200 · `dus42` 200 · `f6wbn`（无后缀）404 · `f6wbn`@`10.31219` 404；两前缀 registrant 均 `Center for Open Science` |
| `V6` | `02b` 对 `R04`/`R06` 的引用 | 全文正则计数 | `R04`=**0** `R06`=**0** `04_DATASET_LANDSCAPE`=**0** `06_TRANSITION_LAWS`=**0** `pairfam`=**0** `APES`=**0** `DVA`=**0** `BMR`=**0** `RGM`=**0** |
| `V7` | `02b` 的 `H2 CRITICAL` 位置 | 定位 | `02b_CONSTRUCT_REDUNDANCY_AUDIT.md:439` |

**全部脚本在 `C:\Users\gg828\AppData\Local\Temp\opencode\a2\`，不在 repo 内。**
