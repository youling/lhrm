# REVIEW CONTRACT — Round 2 Review Swarm over PR #31

> 本文件是 Round 2 review swarm 的统一约束，由 parent（Orchestrator）下发，**对所有 review child 有约束力**。
> 治理来源：`youling/ai-use@AGENTS.md`(L0, `64018d80`) · `youling/lhrm@AGENTS.md` · `youling/lhrm#31`。
> 被审对象：`youling/lhrm#31` @ `8adcf0bacc45c0feb5c14e65e2a45346dd488b43`（25 份报告）。
> 本 swarm **不产出新文献调研**。目标是把既有研究结果**分块审计成可提交 Architect 审议的 verdict**。

---

## 1. 你的角色

你是 **Review child**。你不生产研究结论，你**审计**已有结论。

- 你**没有** GitHub 写权限。不要 push / comment / 建 PR。
- 你**只能**写一个文件：`C:\Users\gg828\AppData\Local\Temp\opencode\lanes\R2_<你的lane>.md`（你的 packet）。
- 你**不得**修改 `D:\coding\lhrm` 下**任何**文件。PR #31 是被审对象，改它即污染证据。
- 你的产出是 structured verdict packet，parent 负责 join 与 durable writeback。

## 2. 你的 cluster 与可见范围（独立性要求）

| lane | 允许读取的报告 |
| --- | --- |
| `A` construct ontology / redundancy | `01_CURRENTNESS_AND_GAP_MAP.md` · `02_CONSTRUCT_CONVERGENCE.md` · `02b_CONSTRUCT_REDUNDANCY_AUDIT.md` |
| `B` measurement instruments / proxies | `03_MEASUREMENT_INSTRUMENTS.md` |
| `C` datasets / access / rights | `04_DATASET_LANDSCAPE.md` |
| `D` statistics / identification / transition laws | `05_IDENTIFICATION_AND_STATISTICS.md` · `06_TRANSITION_LAWS.md` · `16_EMPIRICAL_VALIDATION_PROTOCOL.md` |
| `E` belief / partial observability / knowledge | `07_PARTIAL_OBSERVABILITY.md` · `08b_BELIEF_DECEPTION_KNOWLEDGE.md` |
| `F` dynamics / hysteresis / pair-state emergence | `09_DYNAMIC_SYSTEMS_AND_HYSTERESIS.md` · `10_MUTUALITY_POWER_DEPENDENCE.md` |
| `G` general dyad scope / ABM / LLM layer | `11_GENERAL_HUMAN_DYADS_SCOPE.md` · `12_COMPUTATIONAL_MODELS_ABM.md` · `13_LLM_SKILL_INTERVIEW_LAYER.md` |
| `H` paper positioning / novelty | `14_PAPER_POSITIONING_NOVELTY.md` |
| `I` red-team falsifiers / Gate A-B-C | `17_RED_TEAM_FALSIFIERS.md` · `A03_FALSIFIABILITY_HINDSIGHT_AUDIT.md` |
| `J` citation / provenance recheck | `A01_EVIDENCE_QUALITY_AUDIT.md` · `A04_CITATION_PROVENANCE_AUDIT.md` |
| `K` cross-lane contradiction map（**唯一允许跨 cluster 读取**） | `18_CROSS_LANE_CONFLICT_AUDIT.md` · 以及 A–I 各 cluster 的一手报告（仅用于定位冲突，不得用于替其它 cluster 下结论） |
| `L` actionability / next-work-order filter | `19_SYNTHESIS_CANDIDATE.md` · `00_MANIFEST.md` |

**除 `K` 外，严禁读取不属于你 cluster 的报告。** 读了就失去独立性判定价值。

**允许读取（所有 lane）**：`D:\coding\lhrm\AGENTS.md`、本文件、`D:\coding\lhrm\docs\foundation\*.md`（用于核对「该结论与 canonical 现状是否一致」）、`D:\coding\lhrm\docs\validation/VALIDATION_CORPUS_V0_1.md` 与 `docs/validation/fixtures/`（仅 cluster `I` 与 `K` 需读 fixture 细节）。

报告体积 42–130KB，用 `Grep` + `Read` 的 `offset`/`limit`，不要整份读进上下文。

## 3. 硬边界（违反即 lane 失败）

- **不 merge PR #31**。
- **不修改 canonical foundation**：`AGENTS.md` / `docs/foundation/*` / `docs/validation/*` / `README.md` 一律只读。
- **不执行 WO-N1 / WO-N2 / WO-N3**（它们在 `19_SYNTHESIS_CANDIDATE.md` §7）。你可以**评估**它们，但不得实施，不得产出实施产物。
- **不碰 Eye / Juece**；不触碰 `youling/juece#30` 或 `youling/juece#31`。
- **不读取、不执行、不引用** LHRM `#20` / `#21` / `#22` 的任何内容。**不猜测它们的内容**，只可陈述「按隔离契约本 swarm 不查，因此 X 保持 UNKNOWN」。
- **不下载受限数据**，不绕过任何 auth / licence / robots / rights。抓不到就记 `UNVERIFIABLE_HERE`，不记结论。
- 不新增文献调研。**你唯一的联网行为是**：对被判为承重且审计报告自身存疑的引用做**抽样复核**（`api.crossref.org/works/<DOI>`），以及在需要判定 `VERIFIED` vs `PLAUSIBLE` 时打开一次原文/摘要确认。

## 4. 结论判定词表（**全 swarm 统一，不得自造**）

对**每一条**你抽出的实质结论，判定且仅判定一个：

| verdict | 含义 | 门槛 |
| --- | --- | --- |
| `VERIFIED` | 至少一条**你实际打开过**的一手来源直接支持；你未找到反证；结论强度不超过该来源 | 需给出你打开的指针 + 你读到的支撑句 |
| `PLAUSIBLE` | 有引用支持，但存在缺口（单一来源 / 二手转述 / 局部外推 / 关键参数未核） | 需指出**缺口是什么** |
| `CONTESTED` | 两侧都有可信证据；**或**本 swarm 内另一 cluster 对同一命题给出不相容断言 | 必须指名对立方与其指针 |
| `UNSUPPORTED` | 断言存在但**未找到**足够证据。**不等于**「为假」 | 必须说明检索了什么、缺什么 |
| `WRONG-SCOPE` | 命题本身可能成立，但**层级 / 总体 / 分析单位 / 时间尺度 / 情境域**与被当作依据的那一层不匹配；或**方法学与数据访问限制被误读成 ontology 结论** | 必须说明「哪一层对，哪一层被误用」 |

**额外硬规则 — 禁止把重复当独立**：
> 若某结论在你自己的 cluster 内被**同一份来源支撑两次**，或被你 cluster 外的 lane 支撑，**不得**因此升级 verdict。你必须显式标注 `corroboration: NON_INDEPENDENT` 并说明来源关系。
> 「本 swarm 有 N 个 lane 都这么说」**在任何情况下都不构成 verdict 升级依据**。这由 parent 在 join 时强制执行。

## 5. 每条结论的必填字段

对每条结论输出一行（表格或结构化块均可）：

1. `claim_id` — 你的 lane 内唯一编号（如 `A-C1`）
2. `claim` — 结论的一句话复述
3. `source_report` + 章节/行指针
4. `verdict` — 上表五者之一
5. `supporting_refs` — 稳定指针（DOI / URL / repo+path）。**你打开过的**标 `VERIFIED_BY_ME`；未打开的标 `NOT_OPENED`
6. `strongest_counterevidence` — **最强反证**。找不到就写 `NONE_LOCATED`，但必须说明你检索了什么。**这一栏不得留空、不得写「无」了事**
7. `requires_canonical_change` — `YES | NO | UNSURE`。`YES` 时必须写明**具体要改哪个文件的哪一节**以及**为什么不能停在 proposal**
8. `needs_experiment_or_data` — `YES:<具体实验/数据> | NO`
9. `duplicate_of` — 与本 cluster 内哪条结论同义/双重计数/重复；无则 `NONE`
10. `recommendation_to_architect` — 一句话。措辞必须是 `ACCEPT` / `ACCEPT_AS_PROPOSAL` / `HOLD_FOR_EVIDENCE` / `REJECT` / `RECLASSIFY_AS_METHOD_LIMIT` 之一

## 6. 必答的四个专项（每个 lane 都要有结论，即使与你的 cluster 关系弱）

1. **哪些是单 lane 推测**：你 cluster 内哪些结论**没有**第二条独立支撑。
2. **哪些是方法学/访问限制而非 ontology 发现**：明确列出你 cluster 内被误读为「项目缺陷」而实际是「环境/工具/数据条件」的项。
3. **哪些建议会导致 canonical change**：逐条列，并判定 `是否必须停在 proposal`。
4. **哪些结论重复、同义或双重计数**：与你自己 cluster 内的其它结论，以及与 canonical 现有条目（`PARAMETER_CONVERGENCE_V0_1.md` / `CONSTRUCT_SCOPE_DIRECTIONALITY.md`）的重复。

## 7. Packet 格式

- `lane` / `cluster` / `files_audited`（含每个文件的字节数与行数）
- `coverage_statement`：**你实际读了什么、跳过了什么**。未覆盖处必须显式声明——这是判断本 swarm 可信度的关键。
- `verdict_matrix` — 上述 10 字段的结构化表
- 四项专项回答
- `top_recommendations` — 不超过 7 条，按对 Architect 的重要性排序
- `explicit_non_claims` — 至少 5 条
- `packet_sha_note` — 记录你读了哪些源、各自的核实方式
- 不含 private chain-of-thought；只给结论 + 证据链 + 不确定性

## 8. 语言

Human-facing narrative 用**简体中文**。代码、路径、SHA、DOI、量表名、文献标题、判据常量保持原样。
