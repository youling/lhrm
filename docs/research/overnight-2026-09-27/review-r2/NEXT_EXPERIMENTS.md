# NEXT_EXPERIMENTS — Round 2 review swarm over `youling/lhrm#31`

> 本文件把 `HIGH_CONFIDENCE` / `CONTESTED` / `REJECTED_OR_WEAK` 中的**可行动项**按成本与授权层级重排。
> **本轮不执行其中任何一条。** 分层的目的就是让 Architect 知道**哪些今天就能做、哪些需要签字、哪些在物理上做不了**。
>
> 分层依据：`REVIEW_CONTRACT.md` §3（禁止绕过 rights / egress / 隔离）、`ADJ2` Q6（数据的实际可及性）、
> `L`（本仓库无 runner / CI / metric 实现 / schema）、`C`（逐条打开的 rights 事实）。

---

## 层 0 — 零成本、零新证据、**只需文档编辑**（不需要任何授权）

这些不是「实验」，是**协议定义 + 记账修正**。把它们列在第 0 层是因为：**在它们完成之前，任何后续结果都不可解释。**

| id | 动作 | 依据 | 落点 |
|---|---|---|---|
| **Z-1** | 补 `§2` 全族（2.1–2.6） + `§13` 类表 + `§15` 三门的后果动词 / 阈值 / `redundancy hole` 诊断值 / leave-one-out ablation 臂；同步 `AGENTS.md:62`；先合并 `§2.5` 的 10 层与 `§13` 的 10 类 | `C-P1`（`EV1` §8 + `ADJ3` Q2） | `PARAMETER_CONVERGENCE_V0_1.md` |
| **Z-2** | 把 `VALIDATION_CORPUS` 的 `future_leakage_risk` 拆两列；把「Recommended Fixture 001–003」标注为已被取代 | `C-P6`（`I-C12`/`I-C28`）——**已发生的文档级冲突** | `docs/validation/VALIDATION_CORPUS_V0_1.md` |
| **Z-3** | 撤回 `MERGE`/`REJECT` 从未签发的四处表述（`19:32/103/185`、`00_MANIFEST:128`），改用 `ADJ3` 的 `corrected_claim_text` | `R-A1`（`ADJ3` rec 2） | `19` / `00_MANIFEST` |
| **Z-4** | 把 `19:35` / `19:182` 的「A03 修正为 8/11」撤回（`A03:736` / `A03:751` 逐字否决过该数字） | `H-A4`（`ADJ3` rec 1）—— **Architect 会最先读到的两个数字之一，且是误引不是计算错误** | `19` |
| **Z-5** | `A1` + `A10` 合并为一条；catch-all 3 → **4**；指针 `§14 Step 3` → `§14:679` + `§15 Gate A step 3` | `H-A3`（`ADJ3` rec 3） | `19` |
| **Z-6** | `A1`–`A12` 替换为 `N-A1`…`N-A12`（`Lanes` 列改为 `independent_sources × methods`；`independent_sources = 0` 不得进表） | `X-8`（`ADJ3` Q6 + rec 4） | `19` §1 |
| **Z-7** | 单份、无编号冲突的 blocker register（修 `B-3` 编号冲突、成员不相交、`B-4` 双重分类） | `R-4`（`ADJ3` Q8 + `L-C18`） | `19` §8 + `00_MANIFEST` §4 |
| **Z-8** | 撤回「唯一的真正阻塞项」标签；按依赖解锁序重排；8 个 Work Order 重分类为 3 决策 + 3 派工 + 1 基础设施 + 1 书目 | `C-P9` | `19` §7 |
| **Z-9** | `B2` 的三处措辞删除 + 从主判定清单降级 + rationale 改写 + 新增 `N7_UNDIRECTED_SCORE` / `N8_LEVEL_CONDITIONAL_SLOPE` + 修 `06:489` / `06:901` | `C-P10`（三方无争议部分） | `16` / `06` |
| **Z-10** | `B2` 是否改名 = 读 `16` §7.1 与 `06` N1 原文各一行 | `C-P10`（`X-6` 的 CONDITIONAL 分支） | — |
| **Z-11** | 补 HRS CoU 条文到 `04` §5.1；补 SOEP 行（Type 1/2/3 全 None）；G2 改述为「单源扩散」并给出溯源链 | `H-C1` + `R-C4` + `R-C7` | `04` |
| **Z-12** | 撤回 SOMAR VDE「唯一已知可行的合规 LLM 路径」，拆成三句各带条件与出处 | `R-C1`（`C-C14`）—— **唯一会导致真实合规后果的错误** | `04` §6 / §10 |
| **Z-13** | manifest §7 的 M-1…M-9 共 10 块 verbatim 替换 | `EV2` §5 | `00_MANIFEST` / `A01` / `A04` |
| **Z-14** | `04` §8.9 头条改为「本次检索的结构性结果」；§8.8、§8.6 改述 | `R-0.2` / `R-0.3` / `R-0.8` | `04` |
| **Z-15** | `02`/`02b`/`03`/`05`/`06`/`07`/`08b`/`09`/`10`/`11`/`12`/`13`/`14`/`17`/`18` 的研究侧更正（完整索引见 `CANONICAL_CHANGE_PROPOSALS.md` 末节） | 各 lane | `docs/research/overnight-2026-09-27/*` |

> **层 0 的统一前提**：Z-1 落地后，Fixture schema pin `@ f237784` 意味着**所有在改动前产出的 mapping 计数都不可与之后的结果比较**（`L-C9` `VERIFIED`）。
> ⇒ **先记录基线，再改 schema。** 这是 `L-C9` 给出的唯一硬顺序约束。

---

## 层 1 — 可立即执行、有明确后果、**今天就能跑**

| id | 实验 / 动作 | 依据 | 前置 | 产出 |
|---|---|---|---|---|
| **E-6** | 删掉 `NARRATIVE_ONLY` / `IRRELEVANT` 出口后**重跑 Fixture 001 的 C001–C026** | `I-C29`（`I` 判：**全项目唯一一条可执行、后果明确、今天就能跑、且能同时产出两个退守结论的 falsifier**）。`A03` U-F 已独立确认它尚未运行 | Z-5（`MAPPING_FAILURE` 可达） | 两个退守结论：哪些 unit 落到被删掉的出口；`DIRECT_MAPPING` 率的变化 |
| **E-12** | 取样复核 **`S04`（Joel et al. 2020）的转述状态** | `ADJ2` `residual_uncertainty`：「**这是本包最需要 Architect 指定的下一处取样复核**」。`06:504` 据此标「人内变化幅度随时间 = `DIRECTION_NOT_SUPPORTED`」，而 `16:560` 自陈「书目已核实；**五条实证结论为转述**」 | 无（一次 Crossref + 全文） | DVA 的最大外部限制是否需要重估 |
| **E-13** | 补抽 `S19` 的 DOI 消歧（读 `06` §9 指针表） | `EV3` Claim 2 的 `settleable_by` 明列此项为未覆盖 | 无 | `S19` 具体所指 |
| **E-14** | 修 A01 的 83 条 `NARROW_REPAIR_REQUEST` 中的两类：① 零风险且已实测的（`11:502` F-08、`03:336` 过期注解、`10:786` 题名、`10:786/804` 页码、`02b:596` 作者）；② 承重指针（`02b:286` 的 CI/β² 精度、manifest 的 Sibley 年份） | `J` top_rec 5 | 无 | 其余 ~70 条**明确标为「接受为已知残余」**，不要让它们稀释真正的 blocker |
| **E-15** | 重出 `A04` §4.2 承重表（加 `author` + `title` 两列）与 §4.3.4 的卷期核对 | `H-B5`（`J` top_rec 2/3：19 行抽样 11 行错；**「已通过」清单里有错项 = 假的免检标记**，建议全表重跑） | 无 | A04 从此在结构上能发现本语料的主导缺陷类 |

---

## 层 2 — 需要**测量学 / 统计设计**（不需架构裁决，但需 Human 授权采样）

`ADJ3` Q8 明确：**真·研究设计任务 = 2 项**，**不需架构裁决**。

| id | 动作 | 依据 | 判据 |
|---|---|---|---|
| **E-7** | `B-7`：`Liking ↔ RomanticAttraction` 的**同样本斜交因子相关 / CFA 判别效度检验** | `ADJ3` Q8（研究设计任务） | 判别效度不成立 ⇒ canonical §4 D1/D2 的分离必须重审 |
| **E-8** | `B-8`：`OutcomeDependence` 的**关系级可测性**（工具研制） | `ADJ3` Q8。**注意其架构部分**（R10 的 `Ω(S)` 替代推导 vs R06 的 `APES` 存量）属 `C-2`，是**另一件事** | —— |
| **E-1** | **M1：定 `domain` 是否必需**（`ADJ1` Q4 判「这是本簇真正的最小实验」） | 见下 | `scalar invariance` 成立 ⇒ `02:164` 的强制条件被**证伪**（`A-C21` 终局胜出）；失败 ⇒ `02:164` 获支持（但仍需说明为何用 organizational 域的论证足够） |
| **E-2** | **M2：定 `FeltSecurity` facet 切点**（= `02b` U4，本轮不执行） | 见下 | `FeltSecurity` 在非剥削 facet 之外是否有增量 |
| **E-10** | 序数数据处理规范落地后**重算**所有已报告的均值比较 | `C-P4` / `H-D1`（Liddell & Kruschke：系统性效应反转，取平均不修复，无可靠事后检出） | —— |

### E-1 的完整规格（`ADJ1` Q4 逐字）

> 在**同一 dyad 样本**内，对一个**已有的** dyadic trust 工具，在 `02:164` 自己列出的 5 个 domain
> （财务 / 身体与健康 / 育儿 / 情感脆弱 / 决策委托）上施测，做 **measurement invariance** 阶梯检验。
> - `scalar invariance` **成立** → `domain` **不是**必需 signature 字段 → `02:164` 的强制条件被**证伪**（`A-C21` 终局胜出）。
> - `scalar invariance` **失败** → `domain` 分解有测量学必要 → `02:164` 获支持。
>
> **成本：一次施测 + 一次 invariance 阶梯。不需要新量表，不需要纵向。**
> 附带可检验 `02:161` 自承的 alpha `.59–.84` 与跨伴侣一致性 `r = .11`。

### E-2 的完整规格（`ADJ1` Q4 逐字）

> `non-exploitation-expectation` 子量表 + 对**违反应事件**的增量效度，控制 ECR partner-specific anxiety/avoidance 与 `PPR`。
> 这判的是「`FeltSecurity` 在非剥削 facet 之外是否有增量」，**不判层归属**。

> **`ADJ1` 的硬约束（必须写进派工单）**：`M1` 与 `M2` **不可互相替代**，且**都不判**
> 「`Trust` 是否该降为 `AttachmentSecurity` 的 facet」这一**层**问题
> ——那只能由 Architect 在 M1/M2 之后裁定，**或按 `C-P3` 先做无数据部分**。

---

## 层 3 — 需要**外部数据 + egress + 存储决策**（今天物理上做不到）

### 3a. rights / egress 现状（`ADJ2` Q6 判 `PLAUSIBLE`：**0 / 5 条律有可及的法律识别数据集**）

`L1` / `L2` / `L4` / `L5` 需要同一 dyad 上**双方报告 + 至少两个时点**的合法数据。`19` §5 表内：

| 数据集 | 状态 |
|---|---|
| D01 pairfam | 需 user contract（**其是否允许 LLM 处理，`19` 未记载**）；波数需在用作承重属性前确认 |
| D02 SHARE | CoU §7 **明文禁 LLM 处理个体级数据** |
| D03 | 本环境 **403** |
| D04 speed dating | **无第二时点**（21 场是**独立 session**，不是同一 dyad 重复观测） |
| D05 | 单轮 |
| D06 | 跨波 partner id **未核实** |
| D07 | 配偶关系质量**单方报告**（且仅 Wave 1 已核实） |
| D08 | 会员限定 |

⇒ **没有任何一个同时满足「双方报告 + 多波 + 合法 + 可识别」**（`L-C14` `PLAUSIBLE`，缺口 = `19` 未记载 D01 的 LLM 条款）。

**`ADJ2` Q6 的要求**：把「0 / 5 条律有可及的法律识别数据集」改述为「**实践上**不可及」，
并在 `CURRENT_ARCHITECTURE.md` §11 前置目标加两处说明。
**`ADJ2` 明确：这必须先停在 proposal，不能作为既定文本。**

### 3b. 存储面（`L-C7` `VERIFIED`）

`lhrm` 仓库只有 `AGENTS.md`、`README.md`、`docs/`：**无 runner、无 CI、无 metric 实现、无 schema 文件、无 `data/` 目录**。
⇒ 即使 D04（唯一权利上今天可达）也被**存储决策**阻塞：数据落在哪、是否入库、许可 / 署名政策——**需 Human 决策**。

### 3c. 动作项

| id | 动作 | 依据 |
|---|---|---|
| **E-9** | D04（Fisman & Iyengar speed dating）**标定** | `L` top_rec 4。**只能标定，不能支撑任何转移律**（单一时点） |
| **E-16** | 语料采集：`sibling` / `parent–adult-child` / `non-romantic friendship` / `same-sex` 的 core-dyadic 实例 | `C-P7` 层 2（`ADJ3` Q4）。**这需要采集，不是文档编辑** |
| **E-17** | 补 WO-N6 的 LLM 条款登记：pairfam user contract 是否允许 LLM 处理（`19` **未记载**） | `L-C14` 的缺口 |
| **E-18** | 补 `HARP` baseline 成立但 **T2/T3 微数据 release 状态未确认**（U6）的登记；按 `04` §2 的「可复现获取路径」一项，HARP 的 `CALIBRATION_READY` **站不住** | `C-C28` / `C` top_rec 6 |
| **E-19** | Fixture 003 的**权利闸裁决**（`HUMAN_REVIEW_REQUIRED` + Eye 侧 `POINTER_HASH_ONLY` fail-closed + `robots.txt` `ai-train=no` + canonical 页 URL 在 2026-09-14 实测 **404**）+ 决定它是否属「3 份已冻结 fixture」 | `L-C10` `HOLD_FOR_EVIDENCE`（`001`/`002` 可跑；`003` 需 Human 权利决定 + canonical URL 重定位） |

---

## 层 4 — 需要**密集观测 regime**（律 E / 转移律的唯一可行入口）

| id | 动作 | 依据 |
|---|---|---|
| **E-11** | 把 **ESM / IL / EMA escape clause** 补进 `09` §4.4，并**点名这些 regime** | `F-C11` + `ADJ2` rec 5。`09` 的密度条件是 regime 条件化的，但全文**未点名** ESM / IL / EMA。**这一条同时是 `RT` 的唯一可行数据 regime 的入口**（律 E 需要**事件内顺序** = 密集设计） |
| **E-20** | 律 E 的核心主张（`s` 由 dyadic state 决定）标为 `MODEL_HYPOTHESIS`，**不冻结** | `ADJ2` Q1/Q5。理由：现象存在（事件内顺序 / Gable 等 / Rusbult 1991）`SUPPORTED`，但**全是 outcome 层**；核心主张 `06:810` 自陈「无来源直接检验」⇒ **零直接支持** |
| **E-21** | 判 M 用 **AND 门**、判 N 空结果**不触发** —— 已在 `06` 实现，需确认在改写后仍成立 | `ADJ2` Q1。`D-C16` 另要求把 `06 §8.7 第 5 条` 的功效护栏**提升为跨律通用**，否则判 A/D/G/K 会把**功效不足当成律被拒** |
| **E-22** | `09` §4.4-O1 补一条明确的 **ESM/IL/EMA escape clause**：在 3–7 波、12–21 年、`r≈.76`、单条自报满意度读数的条件下，组均值分段非线性趋势**可估**，dyad 层吸引域/停留时间/迟滞**不可估** | `F-C11`（`F` 判「这是 `09` 最正确的一节」，`ACCEPT`） |

---

## 层 5 — 需要**架构裁决**（Human / Project Architect；不是研究问题）

| id | 动作 | 依据 | 为什么不能靠实验解决 |
|---|---|---|---|
| **A-1** | 裁决 Gate B 的正确数字与「分母无意义」的限定 | `H-A4` | 测试集由被测对象自产 = 结构性确认偏误 |
| **A-2** | 裁决值类清单是**许可式**还是**封闭集** | `C-P5` / `X-5` (c) | `EV3`：「这是本 verdict 中**最依赖解释力**的一环」；若裁定为封闭集，`G-C5` 需重审 |
| **A-3** | 裁决 `PPR` / `Satisfaction` 的层归属 | `X-1` | **`ADJ1`：没有实验能单独定层**。能定的是「`PPR` 是否有 state 性质」（见 E-20a），仍需**额外前提**「时间在前的自陈量 = state」，而这个前提本身未被任何 lane 检验 |
| **A-4** | 裁决 `Trust` 的 facet 切点归属 | `X-4` | `ADJ1`：**M1/M2 都不判层问题** |
| **A-5** | 裁决 `Ideal` 是否成为动态 directed state | `R-D13` | 需 S31 原文 + S17 正文；`06:647` 的 `Ideal` 论证标 `CITED_SECONDARY`（转述未读原文） |
| **A-6** | 裁决 `OutcomeDependence` 的四种互斥 ontology（R10 `Ω(S)` vs R06 `APES`） | `ADJ3` Q8（`C-2`） | —— |
| **A-7** | 建立构念可观察性 / 锚点登记表 | `C-P13` / `E-C16` | `E`：**它是一条 Architect 裁决，不是研究问题** |
| **A-8** | 裁决 `Disclosure` 作为 `Action/Event` 子类型的形态 | `C-P11` | 措辞必须从「持续的不可及性」收紧为「一次披露/不披露的动作」，否则落进 `Constraint` |
| **A-9** | 裁决 Gate A 归因推理是否按算子组合实现（`⊥` 偏算子） | `C-P12` | `U4` 本身是 `UNKNOWN` ⇒ 现在不能写进 canonical |
| **A-10** | 回答 WO-N1 的被检验对象是「**事实态分离**」还是「**构念覆盖**」 | `X-9` | Fixture 001 的 core dyad 是雇主↔雇员（`L-C11` 直读）⇒ **不回答则 N1 的结果不可解释** |
| **A-11** | 接受 `ADJ3` 的 blocker 四分类 + Work Order 重分类 | `C-P9` | —— |
| **A-12** | 接受 `N-A1`…`N-A12` 替换 A1–A12 | `X-8` | —— |

### E-20a — `PPR` 层的最小可判实验（`ADJ1` Q1 逐字）

满足以下**全部**条件才会判 `H_belief` 失败（转 `H_state`）：

- 在**外部锚定的两个不同时点**（不是同一问卷施测的相邻 wave）上测量 `PPR` 与 8 个 directed 坐标；
- `PPR` 与 directed 坐标的残差相关在时间上**先于** directed 坐标变化；
- `ResponsiveAction_(j->i)` 的独立编码与 `PPR` 的分歧在预测下游行为上**互不冗余**；
- 在 **≥2 种关系类型**上同号复制。

> 即便如此，该实验只证明「`PPR` 有独立的**时间**性质」，仍需**额外前提**「时间在前的自陈量 = state」才能完成层归属
> ——这个前提本身未被任何 lane 检验。**故：没有实验能单独定层；能定的是「`PPR` 是否有 state 性质」。**

### E-20b — `Satisfaction` 的最小可判实验（`ADJ1` Q2 逐字；四个问题中**唯一有干净实验**的）

`Satisfaction_i(t)` 与 8 个 directed 坐标在**至少 3 个不同时点**、**跨 ≥2 种关系类型**上的纵向设计，
检验 R3 `:495` **自己写的**判据（条件增量信息 + 稳定性）。

- 若 `H_belief` 方向被否（satisfaction 确实携带独立动态信息）→ R3 条件成立 → 触发预登记（`C-P8`）。
- 若成立 → R3 现状维持，本条变 moot。

> **但该实验判不了 `[S05]` 的「attraction-based 分量含 satisfaction」这一事实前提** —— 那需要 DCI 的量表结构证据（`NOT_OPENED`）。

---

## 层 6 — 本轮**物理上不可能**（不得记为 ontology blocker）

`ADJ3` Q8 明确：**这些属 contract §6.2 意义上的「方法学/访问限制而非 ontology 发现」，无人可裁决。**

| id | 事项 | 状态 |
|---|---|---|
| **N-1** | `B-1` 网络出口不可达（icpsr 403 / saflii 403 / gutenberg timeout） | **环境限制。不是项目缺陷。** contract §3 禁止绕过 |
| **N-2** | `B-2` Gilligan / Kleemans / Rodriguez (2017) ASR 确认不可得 | **环境限制**（且是一个**文献负结果**）。无解 |
| **N-3** | `B-5` `#20` / `#21` / `#22` 隔离 lane 结果未知 | **治理限制。** 须隔离解除后才可查；**本 swarm 不猜、不引、不推断其内容** |
| **N-4** | `B-3` R02 的 ESEM / bifactor 真实文献负结果 | **负结果（不是 blocker）。须移出 blocker register** |
| **N-5** | `B-4` 迟滞在二元关系数据上无任何估计 | **负结果（不是 blocker）。** `19` 自己在 A9 已正确处理为负结果，**§8 B-4 给了两种分类** |
| **N-6** | 「intensive longitudinal 关系日记数据」不存在 | **本轮不得检索。** 若未来要查，须作为**独立的系统检索**立项，不作为报告正文的注记 |

---

## 被降级为 `NEGATIVE_RESULT` 的项（**记录，不是 blocker，也不是缺陷**）

| id | 内容 | 依据 |
|---|---|---|
| **NR-1** | 「missingness lowers certainty, not computability」在仓库内**字面不存在**；项目实际持有的是更弱的 `Computable != Certain` | `R-E3`（`E-C1` 判「这是本 lane 最有价值的一条，应作为 `NEGATIVE_RESULT` 进入 join」） |
| **NR-2** | 迟滞在夫妻/恋爱/亲子/照护数据上的存在性 = **`UNKNOWN` / `model hypothesis`**（不是领域否定） | `R-F2`（`F-C1`）。`F` 自陈「在已检索场所内未找到 ≠ 不存在」 |
| **NR-3** | L3（`DVA`）与 L5（`RT`）的**自预注册 kill criterion 未被触发** | `X-11`（`ADJ2` 推翻 `L-C15`）。**分类错误的纠正**：它们仍是 `RESEARCH_CANDIDATE` |
| **NR-4** | `JuSpace` / `smallslm` / `ASON` 三个候选 ABM 名字不存在 | `H-E7`（`G-C19`）—— **正面产出**：这是「不存在的候选工具」清单的样板 |
| **NR-5** | `Unknown` 值类被**至少六套**（不是五套）词表各自重发明 | `R-K6`（`K-C7`）+ `N-A7`（4 条 lane 独立重发明，`independent_sources = 5`） |

---

## 派工前必须知道的四个顺序约束

1. **Z-1 先于 E-6。** `MAPPING_FAILURE` 类型上不可达时，E-6 的任何计数都不可解释。
2. **基线先于 schema。** Fixture schema pin 在 `f237784`；Z-1 落地后，改动前产出的 mapping 计数**不可与之后比较**（`L-C9`）。
3. **层 3 全部在层 0/1 之后。** `L` 的重排（N1a→N3→N5a→N5b→N2→N4→D04→N7→N8）里，
   **只有 D04 标定与 N7 需要数据**；其余全是文档 / 裁决。
4. **A-10 先于任何 WO-N1 执行。** Fixture 001 的 core dyad 是雇主↔雇员 ⇒ 不回答「事实态分离 vs 构念覆盖」，
   N1 交不出可解释的产出（`X-9`）。

---

## 明确**不做**的事（`REVIEW_CONTRACT.md` §3）

- **不实施** `WO-N1` / `WO-N2` / `WO-N3`（本轮只评估）。
- **不 merge PR #31**，不修改其任何文件。
- **不读取、不执行、不引用** `youling/lhrm#20` / `#21` / `#22` 的任何内容；**不猜测**其内容。
- **不触碰** Eye / Juece；不查询 `youling/juece#30` / `#31`。
- **不下载受限数据**，不绕过任何 auth / licence / robots / rights。抓不到就记 `UNVERIFIABLE_HERE`。
- **不新增文献调研。** 本轮唯一的联网行为是对被判为承重且审计报告自身存疑的引用做抽样复核
  （`A` 18 次、`B`/`D`/`F`/`H`/`J`/`K` 各自的 Crossref 抽样、`EV1`/`EV2`/`EV3` 的一手全文与摘要核查）。
- **不执行 Gate A/B/C 的任何一次完整运行。** ⇒ 因此本 review **无法确认「门实际上会产出什么」**。
