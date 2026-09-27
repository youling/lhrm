# Observability Registry v0.1 — 填充内容

**Status:** CANDIDATE CONTENT（**未合并、未跑门、未设任何基准或数值尺度**）
**As of:** 2026-09-28
**Authority:** `youling/lhrm#30` `ARCHITECT_ADJUDICATION_V1` **C-P13**、**X-4**、**X-5**、**X-13**、**C-P4**、**C-P11**、ruling §C item 3；`ARCHITECT_ROUND3_DISPATCH_V1` Track **R3-D** `D5` / Track **R3-F**
**schema 的 SSOT 归属：** `docs/foundation/MEASUREMENT_SEMANTICS_V0_1.md` §3.2（兄弟轨 `D`）。**本文不改写 schema、不新增维度、不引入第二个未判定标记（只用 `TBD`）、不另立第二份 registry。**
**同分支关联文档：** `docs/foundation/UNKNOWN_APPLICABILITY_TAXONOMY_V0_1.md`（本文的 §5 / §7 大量引用其轴 1 取值）

> **这是 measurement metadata，不是 ontology 扩张。** 本文**不新增任何构念**。
> **本文不含任何已执行结果。** 未运行 Gate A/B/C，未映射任何 fixture，未定义任何 metric，未冻结任何数值尺度。

---

## 0. 本文与 `D` 的分工

`D` 已交付 §3.2 的**逐行 schema**、§3.3 的**完整性读法**、§3.4 的**「本表不能由层裁决推出」**约束、§3.5 的 **18 行骨架**。本轨交付：

1. **§3.5 骨架的逐行替换内容**：骨架 18 行 → 本文 **60 行**（`AGENT_ATTRIBUTE_*` 按 `D` open question 6 逐项拆开；`ACTION_EVENT_OBSERVABLES` 按 canonical 逐项列全；`P4` / `P5` 各拆为「本体 / 覆盖」或「规则文本 / 被遵守」两行）。
2. 每个观测维度的**读法**（§1）—— `D` 给了字段名，没给读法；读法不定，填出来的值不可复核。
3. 观测性剖面共享但**不合并**的分组（§7）。
4. 「单一构念必须是两个有向状态的函数」这条**观测性事实**（§5）。
5. `UNKNOWN_AS_OF` 登记与「什么证据能解决它」（§4）。
6. 下游阻塞登记（§6）。
7. 与 `D` 骨架的两处计数缺陷（§8，**不静默调和**）。

---

## 1. 字段读法（`D` §3.2 未定义；本文固定，作为待 Architect 确认的候选）

`D` §3.2 给了字段名与枚举，但没给**读法**。读法不定，六个维度的取值可以互相替代，表格就不可复核。本文的读法：

| 字段 | 本文采用的读法 | 明确的**反**读法（不得采用） |
|---|---|---|
| `directly_observable` | 该构念的取值可由**不依赖被试自陈**的外部通道得到（第三方编码 / 制度记录 / 仪器 / 行为痕迹） | 「模型读一遍文本就能拿到」——那是**映射**，不是观测（`VALIDATION_GATES_V0_2` §3 的 `mapping_outcome` 是另一条轴） |
| `self_report` | 存在**该主体自己**报告该构念的有效通道 | 「该主体知道自己的状态」——那是**构念假设**，不是通道存在性 |
| `partner_report` | 存在**对方**报告该构念的有效通道 | 「对方能猜到」；「`self_report` 的镜像」——**两者是不同通道**，`Satisfaction` 一行就靠这条区分（§3 G6） |
| `behavioural_anchor` | 存在一个**可观测的行为**可作为该构念的锚 | 「该构念的行为表现」≠「该构念有行为锚」；`Action/Event` 变量本身**就是**行为，故对它们恒为 `YES`（这是平凡真，不是发现） |
| `latent_inferred_only` | 该构念的取值**只能**由推断得到，**任何**通道都不直接给出它 | 「我们还没找到工具」——那是 `NOT_INSTRUMENTED`（Axis 1），**不是** `latent_inferred_only = YES` |
| `structurally_unobservable` | 存在一条**原则性**的障碍，使该构念**在原则上**不可被任何通道观测 | 「本次没观察到」；「该通道被法律禁止」——后者是 `INACCESSIBLE_CHANNEL`（Axis 1），**可换通道**的情况与本条不同（`UNKNOWN_APPLICABILITY_TAXONOMY` L-14） |
| `layer_ref` | 该构念的 `LHRM-LANDING-1` 落点类 | **不得**当作可观察性证据（`D` §3.4 逐字：层裁决「**不蕴含**」可观察性） |
| `applicable_scopes` | `HD-ST-1` 的 `dyad_class` 列表（`VALIDATION_GATES_V0_2` §6.4）+ 轴 2 的 `applicability` 引用 | 不得用 `11` §2 的 216 格填——那些是**语义**判定，`11` §1 逐字声明**零**跨 dyad-type 不变性研究 |
| `evidence_provenance` | 锚 + 强度；无则 `NOT_YET_REGISTERED` | 不得填「层裁决」作为锚（`D` §3.4） |
| `completeness` | `COMPLETE` = 6 维全为 `YES`/`NO` 且有 `evidence_provenance`；`PARTIAL` = 部分已判定；`SKELETON` = 维度已列但 `evidence_provenance = NOT_YET_REGISTERED` | `TBD` **不得**读作 `NO`（`D` §3.3 逐字） |

> **图例**：本文表中 `Y` = `YES` · `N` = `NO` · `–` = `TBD` · `n/a` = `NOT_APPLICABLE`。

---

## 2. 逐行内容

### G1 · Action/Event observables（13 行）

**依据（逐条枚举已核）**：`PARAMETER_CONVERGENCE_V0_1.md` §8 逐字列出 **13** 项（`money spent` / `messages sent` / `response latency` / `hours together` / `sex acts` / `physical touch` / `caregiving acts` / `compliments` / `conflict acts` / `repair attempts` / `gifts` / `travel to meet` / `public declarations`），并逐字规定其 canonical 位置「优先是：`Action/Event + provenance + timestamp`」。

**统一填充**（13 行共享，**不合并**）：`directly_observable = Y`（读法见 §1：发生断言有 canonical 记录形态；**不**表示本次已观测）、`latent_inferred_only = N`（§8 逐字「**不能与 latent relationship state 平级计数**」）、`behavioural_anchor = Y`、`structurally_unobservable = N`。
**全部 `TBD`**：`self_report` · `partner_report`（共 2 维 × 13 行 = **26 个 `TBD`**）。

| construct_ref | `directly_observable` | `self_report` | `partner_report` | `behavioural_anchor` | `latent_inferred_only` | `structurally_unobservable` | layer_ref | `evidence_provenance` | `completeness` |
|---|---|---|---|---|---|---|---|---|---|
| `PARAMETER §8 / money spent` | Y | – | – | Y | N | N | `ACTION_EVENT` | `P8` 逐条枚举已核；`self_report`/`partner_report` = `NOT_YET_REGISTERED` | `PARTIAL` |
| `PARAMETER §8 / messages sent` | Y | – | – | Y | N | N | `ACTION_EVENT` | 同上 **+ `R03 §3.2` 日/周行逐字「SMS 数字轨迹」**（痕迹通道候选） | `PARTIAL` |
| `PARAMETER §8 / response latency` | Y | – | – | Y | N | N | `ACTION_EVENT` | 同上 **+ `R03 §3.2`「SMS 数字轨迹」**（latency 是痕迹**派生**，非行为本身） | `PARTIAL` |
| `PARAMETER §8 / hours together` | Y | – | – | Y | N | N | `ACTION_EVENT` | `P8`（**本项在 `D` §3.5 的枚举中被漏列**，见 §8 缺陷 1） | `PARTIAL` |
| `PARAMETER §8 / sex acts` | Y | – | – | Y | N | N | `ACTION_EVENT` | `P8` **+ `R11 §L-4` 照护列逐字「受照护者对照护者的性吸引是文献记载的类别（含失智相关去抑制），且是**保护**议题；当普通 desire 坐标表示会丢风险语义」** | `PARTIAL` |
| `PARAMETER §8 / physical touch` | Y | – | – | Y | N | N | `ACTION_EVENT` | `P8` | `PARTIAL` |
| `PARAMETER §8 / caregiving acts` | Y | – | – | Y | N | N | `ACTION_EVENT` | `P8` **+ `R02 §表8` 逐字「动机 / 行为双层；**不得把 4 个 specific 当独立状态读出**」** | `PARTIAL` |
| `PARAMETER §8 / compliments` | Y | – | – | Y | N | N | `ACTION_EVENT` | `P8` | `PARTIAL` |
| `PARAMETER §8 / conflict acts` | Y | – | – | Y | N | N | `ACTION_EVENT` | `P8` **+ `R11 §3.3` 逐字「当前 basis **无法区分『互惠的敌意』与『单向的控制』**」** | `PARTIAL` |
| `PARAMETER §8 / repair attempts` | Y | – | – | Y | N | N | `ACTION_EVENT` | `P8` | `PARTIAL` |
| `PARAMETER §8 / gifts` | Y | – | – | Y | N | N | `ACTION_EVENT` | `P8` | `PARTIAL` |
| `PARAMETER §8 / travel to meet` | Y | – | – | Y | N | N | `ACTION_EVENT` | `P8` | `PARTIAL` |
| `PARAMETER §8 / public declarations` | Y | – | – | Y | N | N | `ACTION_EVENT` | `P8` **+ `CURRENT_ARCHITECTURE §6.1`（`D` 轨新增）逐字「**单纯的沉默 / 缺席不自动是 Action。**『j 没有问』『i 没有说』在缺少 `opportunity_or_expectation_ref` 时，记为**无 action 记录**…**不得**记为 `Withhold`」** ⇒ `public declarations` 与 `InformationAction = Disclose` 的边界（一条公开声明算不算一次 `Disclose`）**未登记** | `PARTIAL` |

**G1 的统一 `TBD` 解决路径**：`R03`（`03_MEASUREMENT_INSTRUMENTS.md`）的仪器表需按 **Action/Event 变量**逐项给出通道 + `R16 §3.1` 的 `mapping_status` + `R16 §3.4` 的 `missingness_mechanism` / `invariance_level_tested`。**本轨未做该逐项检索（`NOT_OPENED`）。**

### G2 · InformationAction 家族（1 行）

| construct_ref | `directly_observable` | `self_report` | `partner_report` | `behavioural_anchor` | `latent_inferred_only` | `structurally_unobservable` | layer_ref | `evidence_provenance` | `completeness` |
|---|---|---|---|---|---|---|---|---|---|
| `CURRENT_ARCHITECTURE §6.1 / InformationAction ∈ { Disclose, Withhold, Misrepresent }` | Y | – | – | Y | N | N | `ACTION_EVENT` | C-P11 逐字「`ACCEPT AS ACTION VOCABULARY, NOT NEW STATE PRIMITIVE`」+ `CURRENT_ARCHITECTURE §6.1` 逐字「**`Withhold`** —— **仅当**信息项**与**相应的机会 / 预期**同时显式**时才成立（`info_ref` 存在 **且** `opportunity_or_expectation_ref` 存在）」+ 逐字「`Withhold` 属于后者——它是一次**在机会面前的动作**，不是一条常设边界」 | `PARTIAL` |

**`TBD` 解决路径**：三个值的**识别算法**未登记 —— 什么算一次 `Disclose`？`Withhold` 的双条件需要一个 `opportunity_or_expectation_ref` 的**登记格式**，而该格式不存在（`D` 的 §6.1 记录了条件，未记录格式）。`Misrepresent` 逐字「给你了，但内容被曲解」⇒ 它需要**内容对照**通道，canonical 未指定。

### G3 · Directed relationship states（8 行，`PARAMETER §4 D1`–`D8`）

**跨全组的负面记录（search-scope，按 `X-14` 措辞）**：
> 在 `R16 §3.2` 审计的 **16** 个数据集中，**只有 1 个**（`D04` 速配）提供**无外部假设**的 `DIRECTED_EDGE` 双分量，且它**没有第二个时间点**。
> 同表逐字点名 `ECR / ECR-R / ECR-SF / RSQ / AAS / AAQ / WTC-Trait / VFI / HISD / 3VDI / Interpersonal Dependency / Personal Sense of Power / Reiss RPS / Romantic Beliefs Scale` **全部测 `i` 的一般倾向或对一般他者的态度，target slot 结构上为空**（⇒ `directionality_class = AGENT_LEVEL`）。
> **本轨不主张**这是**总体**不存在；这是一个**检索范围结论**（`X-14` 允许的措辞）。

**跨全组的正面记录**：**24 个构念/架构元素 × 9 类 dyad = 216 格**中 `R11` 重算得 `MP = 69` · `MS = 74` · `NA = 24` · `RD = 22` · `UK = 27`。`R11` §1 逐字：这些 `MEANING_PRESERVED` **全部**是**语义**判断，**本次没有找到**任何针对这 8 维 directed battery 的跨 dyad-type 测量不变性研究 ⇒ **这 216 格不得被计入 `applicable_scopes` 的可观察性判定**。

| construct_ref | `directly_observable` | `self_report` | `partner_report` | `behavioural_anchor` | `latent_inferred_only` | `structurally_unobservable` | layer_ref | `evidence_provenance` | `completeness` |
|---|---|---|---|---|---|---|---|---|---|
| `PARAMETER §4 D1 / Liking` | – | – | – | – | – | – | `DIRECTED_RELATIONSHIP_STATE` | `P4 D1`（**反例论证，非可观察性论证**）+ 全组负面记录。**未找到** `R03 §3.1` 的方向性良好族里有 Liking 量表 | `SKELETON` |
| `PARAMETER §4 D2 / RomanticAttraction` | – | – | – | – | – | – | `DIRECTED_RELATIONSHIP_STATE` | 同上 **+ `R11 §L-4` 逐字「`RomanticAttraction` / `SexualDesire` 是唯一两个按名称锚定恋爱的候选」**（scope 事实，非可观察性） | `SKELETON` |
| `PARAMETER §4 D3 / SexualDesire` | – | **Y** | – | – | – | – | `DIRECTED_RELATIONSHIP_STATE` | **`R03 §3.1` 逐字方向性良好族含 `SDI-2 partner-related / PSSLW`（sexual desire）** + **`R03 §3.2` 日/周行逐字「Impett et al. (2008) 的 2 题 partner-specific 性欲双周题（波内 `α_wave .69–.98`）」** + `R03 §3.2` 逐次互动行逐字「**没有『信任更新』或『欲望更新』的 state 工具**」⇒ **有 partner-specific 的 state 级自陈通道，无 trust/desire 的「更新」工具** + `R03 §3.3` 逐字「SDI-2 回顾过去 1 月…月度尺度的性欲数据有明显的**记忆重构**」 | `PARTIAL` |
| `PARAMETER §4 D4 / Trust` | – | **Y** | – | – | – | – | `DIRECTED_RELATIONSHIP_STATE` | **`R03 §3.1` 逐字方向性良好族含 `Rempel TS / DTS`（trust）** + **`R03 §3.3` 逐字「`Schumm et al. (1985) 判定 DTS 测的是 benevolence 而非 trust`（S18）** ⇒ **构念身份被质疑**（`G-2` 缺口）+ `R16 §3.1` 第 6 项逐字「Rempel 三维 trust 结构至今未被系统再验证（2025 年重做发现反向措辞方法因子）」+ `R03 §3.2` 逐次互动行「**没有『信任更新』…的 state 工具**」 | `PARTIAL` |
| `PARAMETER §4 D5 / AttachmentSecurity` | – | **Y** | – | – | – | – | `DIRECTED_RELATIONSHIP_STATE` | `R03 §3.2` 跨文化行逐字「只有这两个构念族有大规模跨文化证据」（依恋 / 性欲；ECR-R 62 文化区）⇒ `ECR-R` 通道存在 + `R02 §表6` 逐字「`KEEP` + `CONTESTED`；person / edge 双层；**保留 (anxiety, avoidance) 原始二维**」+ X-4：与 `Trust` **保持分列**，`FeltSecurity` 措辞归 `D5` | `PARTIAL` |
| `PARAMETER §4 D6 / Caregiving` | – | – | – | **Y** | – | – | `DIRECTED_RELATIONSHIP_STATE` | **`R03 §3.1` 逐字方向性良好族含 `RMBM`（maintenance 行为）** + `R02 §表7` 逐字「动机 / 行为双层；**不得把 4 个 specific 当独立状态读出**」+ **`R03 §3.3` 逐字「`Stafford (2010) 判定两个广泛使用的关系维持量表有 "fundamental measurement flaws"」（S34）** ⇒ 唯一的行为锚候选被质疑（**该逐字未指名是哪两个量表** ⇒ `RMBM` 是否在内**未确定**） | `PARTIAL` |
| `PARAMETER §4 D7 / Dedication` | – | – | – | – | – | – | `DIRECTED_RELATIONSHIP_STATE` | **`R03 §3.4` 逐字「LHRM 最缺的三个（`Dedication`、`OutcomeDependence`、`Cohesion`）**恰好是零证据**」** + `R11 §L-3` 逐字「`Dedication` 内建了自愿、可持续终止、person-specific、共享未来」（4 个假设在 6 类 dyad 上失效） | `SKELETON` |
| `PARAMETER §4 D8 / OutcomeDependence` | – | – | – | – | **Y** | **Y**（**仅 `coordination` 子维度**） | `DIRECTED_RELATIONSHIP_STATE` | **`R02 §表9` 逐字「`KEEP` + `MEASUREMENT_INFEASIBLE_AT_RELATION_LEVEL`」+ `R02 §3.9(4)` 逐字「关系级**无**被广泛接受、可比、验证过的 outcome dependence 量表…`[S28]` 原文明确：已有 mutual dependence / conflict / power 的量表，但 **no instrument has been [developed to measure all sub-dimensions of interdependence]**」+ `R03 §3.4`「零证据」** —— 详见 §5 | `PARTIAL` |

**G3 的 `TBD` 解决路径**：`R03` 仪器表**逐行**给出（构念 × 通道 × 时间尺度 × 不变性层级）+ `R16 §3.1` 的 `mapping_status` + `R16 §3.2` 的 `directionality_class`。**本轨只读了 `R03 §3.1`–`§3.4` 的方向性族 / 时间尺度 / confounds / 不变性四节，未做逐行仪器映射（`NOT_OPENED`）。**

### G4 · Belief layer（3 行）

| construct_ref | `directly_observable` | `self_report` | `partner_report` | `behavioural_anchor` | `latent_inferred_only` | `structurally_unobservable` | layer_ref | `evidence_provenance` | `completeness` |
|---|---|---|---|---|---|---|---|---|---|
| `PARAMETER §5 B1 / PPR` | **N** | **Y** | – | – | – | **N** | `BELIEF_STATE` | **`R16 §3.1` 第 1 项逐字「R03 F10 是正面先例：`PPR` 判为 `DIRECT_PROXY`（对 `PPR_(i about j)`），并被明令**不得**用来推断 `ResponsiveAction_(j->i)` —— 工具测的是知觉而非行为」** + `R03 §3.1` 逐字「其中**只有 PRI 的 Study 3（161 对伴侣 APIM）把『i 的知觉』与『j 的自报行为』在同一模型里对起来**」+ `R03 §3.2` 逐次互动行逐字「**PPR 有 state 化证据，trust 没有**」+ X-1：`PPR` 留在 `BeliefState` | `PARTIAL` |
| `PARAMETER §5 B2 / PerceivedCommitment` | – | – | – | – | – | – | `BELIEF_STATE` | `R02 §表13` 逐字「`PerceivedCommitment` → `BELIEF_ONLY` → 用 `Belief_i(Dedication_(j->i))`，**不新建构念**」（原文为表格行，表内分隔符已改写为 `→`）⇒ 它是 `D7` 的信念投影，**通道继承 `D7`**（`D7` 六维全 `TBD`）。**注意：`BELIEF_ONLY` 是层裁决，按 `D` §3.4 不得据此填任何可观察性维度** | `SKELETON` |
| `PARAMETER §5 B2 / PerceivedAttraction` | – | – | – | – | – | – | `BELIEF_STATE` | `P5 B2` 只定义**形式**，未定义可观察性（`D` §3.5 已记录） | `SKELETON` |

**G4 的一条 `UNKNOWN_AS_OF 2026-09-28`（高价值）**：
> **`ResponsiveAction_(j->i)` 在本项目内没有任何已登记的观测通道。**
> 依据：`R16 §3.1` 逐字**明令禁止**用 `PPR` 的 `DIRECT_PROXY` 工具推断它（`06_TRANSITION_LAWS.md` 的 `ResponsiveAction_(j->i)` 出现在 `08b` §2.11.1 与 `R16` 的引用中）。语料里**没有**任何一条为 `ResponsiveAction` 登记的工具、`mapping_status` 或 `directionality_class`。
> **什么证据能解决**：一次 `R03` 逐行仪器检索，专查「可观察的 partner 行为」族（`R03 §3.1` 的 `RMBM` 维护行为族是**唯一**候选，且其自身被 `R03 §3.3` S34 质疑）；加上 `R16 §3.1` 的 `mapping_status` 判定。

### G5 · Pair-level / Constraint（8 行）

| construct_ref | `directly_observable` | `self_report` | `partner_report` | `behavioural_anchor` | `latent_inferred_only` | `structurally_unobservable` | layer_ref | `evidence_provenance` | `completeness` |
|---|---|---|---|---|---|---|---|---|---|
| `PARAMETER §6 P1 / Cohesion / We-ness`（作为 **pair** 量） | – | – | – | – | – | – | `CONTESTED`（pair process vs 双方 perception） | **`R02 §表11` 逐字「`Cohesion / We-ness` → `BELIEF_ONLY`」+ `R02 U4` 逐字「`Cohesion` 是否存在独立于双方知觉的 **pair latent** / 决定它是 PairState 还是两个 Belief / 独立于双方的 pair 级观测通道（**第三方编码 / 共同叙事 / we-talk 跨评分者信度**）」（表内分隔符已改写为 `/`，原文用 `\|`）** + `R03 §3.4`「零证据」+ `R11 §3.6` 逐字「敌对 dyad 的 "we" 是对比性的（we vs. them）…作为 **pair** 容器读出来是 0，**恰好在现象最强的时候读数最错**」 | `SKELETON` |
| `PARAMETER §6 P1 / PerceivedWeNess_A / _B` | – | – | – | – | – | – | `BELIEF_STATE` | `R02 §表11` 逐字「采纳 §6 P1 的 `PerceivedWeNess_A / _B`；设升级条件」+ `P6 P1` canonical 自己标 `contested scope`。**全部 6 维 `TBD`：`BELIEF_ONLY` 是层裁决，按 `D` §3.4 不得据此填 `directly_observable` 或 `structurally_unobservable`** ⇒ `R02 U4` 的「pair 级观测通道」尚未建成 | `SKELETON` |
| `PARAMETER §6 P2 / ValueCongruence` | – | – | – | – | – | – | `PAIR_STATE`（pair comparison） | `P6 P2` 给「是何种比较」**+ 构念身份本身待定**：**`02b §4.1(4)` 已把 `E11b` / `E11c` 的 `STRONG` 标签撤回**，`02b §10.1` 逐条 3 判「`INDEPENDENT` 在第三方复现 §4.1 重算之前**不得**被引为 Gate C 证据」⇒ **`G-2` 构念身份冲突缺口** | `SKELETON` |
| `PARAMETER §6 P3 / GoalAlignment` | – | – | – | – | – | – | `PAIR_STATE` | `P6 P3`（**无 observability 证据**） | `SKELETON` |
| `PARAMETER §6 P4 / RelationshipIdentity / Agreement`（**制度事实本体**） | **Y** | – | – | – | **N** | **N** | `CONSTRAINT_AGREEMENT` | `P6 P4` 逐字「`KEEP as pair/institutional agreement fact`」+ **通道**：`R15 §15.6.2` 的 `evidence_channel` 的 `DOCUMENTARY` 成员（法院 / 官方记录）+ **`CURRENT_ARCHITECTURE.md:309` 逐字 `provenance quality != fact status` 与 `:314-316` 的 `adjudicated \| admitted \| alleged \| disputed \| unknown`（`AGENTS.md` validation discipline 逐字「do not treat all statements in a judgment as equally adjudicated truth」）** + `R15 §15.6` 逐字「**为何 `fact_status` 与 `assertion_mode` 必须是两个轴**…任一份单独看都自洽，三份并列就不可比」⇒ **「有裁定」与「事实成立」必须分通道**（Axis 1 的 `SOURCE_MARKED_DISPUTED` 是其对应物） | `PARTIAL` |
| `PARAMETER §6 P4 / RelationshipIdentity`（**枚举覆盖**） | – | – | – | – | – | – | `CONSTRAINT_AGREEMENT` | **`R11 §L-5` 逐字「`Relationship Identity` 枚举同时漏类型、混种类，且与 §2 写入域自相矛盾」+「架构声明的域比它自己的 identity 枚举宽」+「一个列表混了三种事实 —— (a) 自愿关系角色、(b) **法律/制度状态**、(c) **功能安排**」** ⇒ 覆盖缺口，**不是**可观察性判定 | `SKELETON` |
| `PARAMETER §6 P5 / BoundaryRule / ExclusivityRules`（**规则文本**） | **Y** | – | – | – | **N** | **N** | `CONSTRAINT_AGREEMENT` | `P6 P5` 逐字「`KEEP as Constraint/Agreement`」+ `evidence_channel = DOCUMENTARY` + canonical 工作例 `CURRENT_ARCHITECTURE.md:190`（「『订婚前不发生性行为』更接近 Agent boundary / constraint，而不是『性欲为零』」） | `PARTIAL` |
| `PARAMETER §6 P5 / ExclusivityRules`（**规则被遵守**） | – | – | – | – | – | – | `CONSTRAINT_AGREEMENT` | **无 canonical 登记。** `AGENTS.md` 当前架构方向第 7 条只说「`State != Action`」，没有「规则 → 遵守」的可观察性登记 ⇒ **本轨新登记的一行**；6 维全 `TBD`（见 §4 的 `U-7`） | `SKELETON` |

### G6 · Derived / Readout（8 行）

| construct_ref | `directly_observable` | `self_report` | `partner_report` | `behavioural_anchor` | `latent_inferred_only` | `structurally_unobservable` | layer_ref | `evidence_provenance` | `completeness` |
|---|---|---|---|---|---|---|---|---|---|
| `PARAMETER §9 R1 / Mutuality_k(A,B) = H(Z[k,A,B], Z[k,B,A])` | n/a | n/a | n/a | n/a | n/a | n/a | `DERIVED_READOUT` | 派生量不直接观察；其可观察性**取决于两个输入** ⇒ **§5 的核心条目** | `SKELETON` |
| `CURRENT_ARCHITECTURE §4.1 / AsymmetryReadout_k` | n/a | n/a | n/a | n/a | n/a | n/a | `DERIVED_READOUT` | 形状约束见 `CURRENT_ARCHITECTURE §4.1`（取代 `CONSTRUCT_SCOPE_DIRECTIONALITY.md:84-89` 的 `Asymmetry_k = distance(...)`；`D` 轨 P-1 请求逐字注记，**本轨未改该文件**） | `SKELETON` |
| `CURRENT_ARCHITECTURE §4.2 / TotalDependence · TotalPower`（**对称**派生聚合） | n/a | n/a | n/a | n/a | n/a | n/a | `DERIVED_READOUT` | X-13 / C-P4：`TotalDependence/TotalPower` 是**对称派生聚合**；**无独立普适 Power primitive** | `SKELETON` |
| `CURRENT_ARCHITECTURE §4.2 / RelativePower · PowerImbalance`（**方向性**读出） | n/a | n/a | n/a | n/a | n/a | n/a | `DERIVED_READOUT` | X-13 / C-P4 **+ `R11 §L-1` 逐字「一个**健康的高照护 dyad**（受照护者高度依赖、方向不对称、替代方案少）与一个**胁迫 dyad**（intimate terrorism）在 `D8` 上**数值结构相同**，R2 会打成同一类，**而它们在伤害上相反**」** ⇒ 同一读出在两种 dyad 上不可作同样解释 | `SKELETON` |
| `PARAMETER §9 R3 / Satisfaction` | **N**（作为 **pair** 属性） | **Y**（作为**个体**评价状态） | – | – | **N** | **Y**（作为 **pair** 属性） | `DERIVED_READOUT` | X-1：`Satisfaction` 留在 Derived / evaluation candidate **`+ R02 §3.10(4)` 逐字「**测量是单人做的，这一点是共识**」`+ R02 §3.10(3)` 逐字「配对数据中关系行为的跨伴侣 agreement 只有 avg `r = .18–.19`，而 projection 高达 `r = .77–.90`——双方看到的不是同一个『关系质量』…这意味着 **satisfaction 作为『关系的属性』在测量上根本不成立**」** ⇒ **`directly_observable` 与 `structurally_unobservable` 的答案取决于「谁在观测」**，这正是 §1 读法表必须先固定的原因 | `PARTIAL` |
| `PARAMETER §9 R4 / RelationshipQuality · Compatibility · MatchScore` | n/a | n/a | n/a | n/a | n/a | n/a | `REJECT as primitive` | `AGENTS.md` 研究纪律逐字「High-level labels such as "漂亮""贤惠""高价值""真爱""关系质量""匹配度" are not assumed to be primitive variables」+ `P9 R4` 当前判定 `REJECT as primitive` | `SKELETON` |
| `PARAMETER §9 R5 / Alignment` | n/a | n/a | n/a | n/a | n/a | n/a | `REJECT as single primitive` | `P9 R5`（当前判定见 `17` §F1 Round-3 逐字引用的 canonical 原文「`§9 R5`「当前：`REJECT as single primitive`」」） | `SKELETON` |
| `RelationalCohesion`（X-13 引入的独立 relation/process 量） | – | – | – | – | – | – | 独立 relation/process 量 | X-13 逐字「Relational cohesion is a **separate** relation/process quantity, not the definition of total power」+ `D` §6 非主张 8：未给它下定义。**注意：它不在 `P11` 的 8 项 basis 内，也不在 `P9` 的 R1–R5 内 ⇒ canonical 落点未指定** | `SKELETON` |

### G7 · Agent-level attributes（18 行，`PARAMETER §7` 逐项拆开）

`D` §3.5 把这一组压成一行并标 `SKELETON`，并把「9–13 项 Agent attributes 是否必须由 `F` 逐项拆分」列为 open question 6。**本轨逐项拆开（`D` open question 6 的答案是「是」）。**

**逐项枚举依据**：`P7` 的代码块是 **15 行**，其中 `income / assets / liabilities`（3 项）与 `education / skills`（2 项）各在一行内合并 ⇒ **18 个具名属性**。`P7` 逐字「但这些不是自动的 **relationship-state primitives**」+ 三条不等式：`Income_A != ResourceInvestment_(A->B)` · `BaselineLibido_A != SexualDesire_(A->B)` · `GeneralizedTrust_A != Trust_(A->B)`。

**跨全组的通道记录**：`R16 §3.2` 逐字点名 14 个已审计量表（`ECR / ECR-R / ECR-SF / RSQ / AAS / AAQ / WTC-Trait / VFI / HISD / 3VDI / Interpersonal Dependency / Personal Sense of Power / Reiss RPS / Romantic Beliefs Scale`）**全部 `directionality_class = AGENT_LEVEL`** ⇒ **它们能供给 `AGENT_STATE_ATTRIBUTE`，但结构上不能供给任何 `DIRECTED_RELATIONSHIP_STATE` 分量。** 这是本组最重要的登记。

| # | `construct_ref` | `directly_observable` | `self_report` | `partner_report` | `behavioural_anchor` | `latent_inferred_only` | `structurally_unobservable` | layer_ref | `evidence_provenance` | `completeness` |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `PARAMETER §7 / age` | – | – | – | – | – | – | `AGENT_STATE_ATTRIBUTE` | `P7` 逐项枚举已核；**无 observability 证据** | `SKELETON` |
| 2 | `PARAMETER §7 / sex / gender-related attributes` | – | – | – | – | – | – | `AGENT_STATE_ATTRIBUTE` | `P7` + **`R11 §L-4` 逐字「单一未标注槽同时承担三种 dyad 相关量（角色/权力不对称结构、吸引相关信号、自我认同），在 9 类 dyad 上作用方向不一致」** ⇒ 槽位**欠定**（`G-3` 缺口的候选） | `SKELETON` |
| 3 | `PARAMETER §7 / health` | – | – | – | – | – | – | `AGENT_STATE_ATTRIBUTE` | `P7`；**无 observability 证据** | `SKELETON` |
| 4 | `PARAMETER §7 / income` | – | – | – | – | – | – | `AGENT_STATE_ATTRIBUTE` | `P7` 不等式 `Income_A != ResourceInvestment_(A->B)` + `R11 §3.3` 逐字「受照护者的 `CareNeed` 很大程度上**由照护者的行为与制度安排产生** → S 与 T 不可分离」 | `SKELETON` |
| 5 | `PARAMETER §7 / assets` | – | – | – | – | – | – | `AGENT_STATE_ATTRIBUTE` | `P7`（与 4 同行） | `SKELETON` |
| 6 | `PARAMETER §7 / liabilities` | – | – | – | – | – | – | `AGENT_STATE_ATTRIBUTE` | `P7`（与 4 同行） | `SKELETON` |
| 7 | `PARAMETER §7 / education` | – | – | – | – | – | – | `AGENT_STATE_ATTRIBUTE` | `P7`（与 8 同行） | `SKELETON` |
| 8 | `PARAMETER §7 / skills` | – | – | – | – | – | – | `AGENT_STATE_ATTRIBUTE` | `P7`（与 7 同行） | `SKELETON` |
| 9 | `PARAMETER §7 / location` | – | – | – | – | – | – | `AGENT_STATE_ATTRIBUTE` | `P7`；**无 observability 证据** | `SKELETON` |
| 10 | `PARAMETER §7 / family obligations` | – | – | – | – | – | – | `AGENT_STATE_ATTRIBUTE` **（层位有争议）** | **`层位冲突`**：`P7` 把它放在 Agent 层；**`R11 §3.2` 的合并候选 `CAND-OBLIG` 逐字「§4 `L-10`（`family obligations` 从 Agent 层移到 pair-institutional 层）」**，且该候选是 **proposal only**。X-4 / C-P5 **未**裁定层位移 | `SKELETON` |
| 11 | `PARAMETER §7 / relationship history` | – | – | – | – | – | – | `AGENT_STATE_ATTRIBUTE` | `P7` + `R11 §3.4` 逐字「**基因上完整的同胞 dyad 可以完全惰性/不存在**」（`I don't really know my brother`）⇒ 该属性的**取值**依赖 `Relationship_ij.existence`（`R11` 的 proposal，无 canonical 落点） | `SKELETON` |
| 12 | `PARAMETER §7 / life goals` | – | – | – | – | – | – | `AGENT_STATE_ATTRIBUTE` | `P7`；**无 observability 证据** | `SKELETON` |
| 13 | `PARAMETER §7 / habit patterns` | – | – | – | – | – | – | `AGENT_STATE_ATTRIBUTE` | `P7`；**无 observability 证据** | `SKELETON` |
| 14 | `PARAMETER §7 / personality traits` | – | – | – | – | – | – | `AGENT_STATE_ATTRIBUTE` | `P7`；**无 observability 证据** | `SKELETON` |
| 15 | `PARAMETER §7 / baseline libido` | – | – | – | – | – | – | `AGENT_STATE_ATTRIBUTE` | `P7` 不等式 `BaselineLibido_A != SexualDesire_(A->B)` **+ `R11 §L-4` 逐字「这是**对所有 Agent 都开槽**的属性，等于假定每个 Agent 都是潜在性关系对象。在同胞/专业/敌对数据集上 (a) **不可测**、(b) **无关**、(c) **一旦被插补就构成伤害**（`AGENTS.md` 明禁）」+ `R11 §2` 矩阵：`NA` in R / D / A，`UK` in F / S / K / C / X / W** ⇒ **本槽是「不可测 + 插补有害」两条同时成立的唯一一格** | `SKELETON` |
| 16 | `PARAMETER §7 / generalized trust` | – | – | – | – | – | – | `AGENT_STATE_ATTRIBUTE` | `P7` 不等式 `GeneralizedTrust_A != Trust_(A->B)` + `R16 §3.2`（`ECR` / `ECR-R` / `ECR-SF` = `AGENT_LEVEL`）+ `R03 §3.2` 跨文化行逐字「`ECR-R`（62 文化区）」。**`self_report` 仍 `TBD`**：`R16 §3.1` 的 `DIRECT_ITEM` / `DERIVED_COMPOSITE` / `BEHAVIORAL_PROXY` / `COVARIATE_ONLY` 四级把「自陈」与「行为 / 记录」分开，但**未逐工具标注**哪一个走哪条通道 ⇒ **不猜** | `SKELETON` |
| 17 | `PARAMETER §7 / caregiving propensity` | – | – | – | – | – | – | `AGENT_STATE_ATTRIBUTE` | `P7` + `R16 §3.2`（`VFI` / `3VDI` = `AGENT_LEVEL`）+ `R03 §3.4` 逐字把 `VFI` / `3VDI` 列入「**完全无不变性证据**」 | `SKELETON` |
| 18 | `PARAMETER §7 / attachment tendency` | – | – | – | – | – | – | `AGENT_STATE_ATTRIBUTE` | `P7` + `R16 §3.2`（`ECR` 族 = `AGENT_LEVEL`）+ `R03 §3.2` 跨文化行逐字「`ECR-R`（62 文化区）…`ECR-R-GSF` **中国样本未达 scalar**」。**`self_report` 仍 `TBD`**（同第 16 行的理由） | `SKELETON` |

**G7 的 `TBD` 解决路径**：一次 `R03 §3.2`（时间尺度）× `R03 §3.4`（不变性）**逐属性**的交叉表 + `R16 §3.1` 的 `mapping_status`。**本轨未做（`NOT_OPENED`）。**

### G8 · Environment（1 行）

| construct_ref | `directly_observable` | `self_report` | `partner_report` | `behavioural_anchor` | `latent_inferred_only` | `structurally_unobservable` | layer_ref | `evidence_provenance` | `completeness` |
|---|---|---|---|---|---|---|---|---|---|
| `ENVIRONMENT_FACT` | – | – | – | – | – | – | `ENVIRONMENT` | **未登记。** `P6 P5` 的 `BoundaryRule` 可视为「被 dyad 内化了的 environment fact」，但 canonical 未把 `ENVIRONMENT` 与 `CONSTRAINT_AGREEMENT` 的关系写成可观察性命题 | `SKELETON` |

---

## 3. 完整性统计（**由脚本解析本文表格逐格重算**，非自报）

| 项 | 数值 | 复算方式 |
|---|---|---|
| 总行数 | **60** | 逐表行计数（`D` §3.5 骨架为 **18**） |
| 分组行数 | G1 = **13** · G2 = **1** · G3 = **8** · G4 = **3** · G5 = **8** · G6 = **8** · G7 = **18** · G8 = **1** | 逐行 `construct_ref` 归组 |
| `completeness = COMPLETE` | **0** | 6 维全为 `YES`/`NO` 的行数为 0 |
| `completeness = PARTIAL` | **23** | `G1 13 + G2 1 + G3 5 + G4 1 + G5 2 + G6 1` |
| `completeness = SKELETON` | **37** | `G3 3 + G4 2 + G5 6 + G6 7 + G7 18 + G8 1` |
| **填写率**（`PARTIAL` / 总行数） | **38.3%**（23 / 60） | — |
| 6 维**全 `TBD`** 的行 | **31** | 逐行 6 格皆为 `–` |
| `directly_observable` | `YES` **16** · `NO` **2** · `TBD` **36** · `NOT_APPLICABLE` **6** | 逐格 |
| `self_report` | `YES` **5** · `TBD` **49** · `NOT_APPLICABLE` **6** | 逐格 |
| `partner_report` | `TBD` **54** · `NOT_APPLICABLE` **6**（**`YES` = 0**） | 逐格 |
| `behavioural_anchor` | `YES` **15** · `TBD` **39** · `NOT_APPLICABLE` **6** | 逐格 |
| `latent_inferred_only` | `YES` **1** · `NO` **17** · `TBD` **36** · `NOT_APPLICABLE` **6** | 逐格 |
| `structurally_unobservable` | `YES` **2** · `NO` **17** · `TBD` **35** · `NOT_APPLICABLE` **6** | 逐格 |
| `applicable_scopes` 已填的行 | **0 / 60** | 理由见 §4.3 |
| `evidence_provenance = NOT_YET_REGISTERED` 的行 | **37** | = 全部 `SKELETON` 行 |
| 带 `UNKNOWN_AS_OF 2026-09-28` 的条目 | **7**（§4 的 `U-1`…`U-7`） | 逐条 |

**5 个 `self_report = YES` 是哪 5 行**：`SexualDesire`（`R03 §3.2` 的「2 题 partner-specific 性欲双周题」）· `Trust`（`R03 §3.3` 的「`DTS 8 题中 5 题反向」+「Gate C 的三对挑战**在自陈通道上**都缺乏分离性证据」）· `AttachmentSecurity`（`R03 §3.4` 的 `ECR` / `ECR-R`）· `PPR`（`R16 §3.1` 的 `DIRECT_PROXY` + `R03 §3.1` 的 `PRI / PPRS`）· `Satisfaction`（`R02 §3.10(4)`「测量是单人做的，这一点是共识」）。

**2 个 `structurally_unobservable = YES` 是哪 2 行**：`OutcomeDependence`（**仅 `coordination` 子维度**，依据 `R02 §3.9(3)`）· `Satisfaction`（**作为 pair 属性**，依据 `R02 §3.10(3)` 的 `r=.18–.19` vs projection `.77–.90`）。
**2 个 `directly_observable = NO`**：`PPR`（依据 `R16 §3.1`「工具测的是知觉而非行为」）· `Satisfaction`（作为 pair 属性，同上依据）。
**1 个 `latent_inferred_only = YES`**：`OutcomeDependence`（依据 `R02 §表9` 的 `MEASUREMENT_INFEASIBLE_AT_RELATION_LEVEL` + 关系级无验证量表）。
**0 个 `partner_report = YES`**：**本项目今天没有任何构念登记了「对方报告」通道。** 这是 `08b` §2.6 的 `g = REPORTED` 在类型上无处落地的**直接证据**（见 §6 B-1）。

**`D` 骨架 18 行的对照**：11 行全 `TBD` · 3 行带 canonical 直接写明的 `Y`（`ACTION_EVENT_OBSERVABLES` / `InformationAction` / `PPR`）· 4 行 `NOT_APPLICABLE`。
**本轨 60 行的对照**：31 行全 `TBD` · 23 行 `PARTIAL` · 6 行 `NOT_APPLICABLE`（全在 G6）。

**读法（必须连同数字一起读）**：`D` 的 18 → 本轨 60 是**行数增加**（`AGENT_ATTRIBUTE_*` 拆 18 行、`P4`/`P5` 各拆 2 行、`G6` 展开 8 行），**不是完成度增加**。`TBD` 的绝对数从 11 升到 31，其中 **18** 行来自 Agent 属性拆分（16 行全 `TBD`）、**2** 行来自 `P4`/`P5` 的「规则文本 / 被遵守」拆分、**1** 行来自 G6 的 `RelationalCohesion`。**本轨相对 `D` 的净增是 20 个有据判定**（3 → 23），**其中 18 个来自 G1/G2 的 `ACTION_EVENT` 族**（`D` 只给了 1 行），**真正的构念级净增是 5 个**（`SexualDesire` / `Trust` / `AttachmentSecurity` 的 `self_report`，`PPR` 的 `directly_observable = NO` + `structurally_unobservable = N`，`OutcomeDependence` 的 `latent_inferred_only` + `structurally_unobservable`，`Satisfaction` 的 4 个维度）。

**本轨自我更正的记录**：起草过程中我曾把 3 个值填成有据判定，随后按 `D` §3.4（「层裁决**不蕴含**可观察性」）撤回为 `TBD`：`PerceivedCommitment.directly_observable`（依据是 `BELIEF_ONLY`）、`PerceivedWeNess.directly_observable` 与 `.structurally_unobservable`（依据是 `BELIEF_ONLY`）、`ExclusivityRules(遵守).behavioural_anchor`（无 canonical 登记）。另把 `generalized trust` / `attachment tendency` 的 `self_report` 从 `Y` 降为 `TBD`（`R16 §3.1` 的四级**未逐工具标注**自陈 vs 行为通道 ⇒ **不猜**）。**这 5 处撤回是本轨的纪律记录，不是缺陷。**

---

## 4. `UNKNOWN_AS_OF 2026-09-28` 登记（**不猜测**；逐条给出「什么证据能解决」）

`UNKNOWN_AS_OF` 是语料中使用最广的记账标记（`UNKNOWN_APPLICABILITY_TAXONOMY` §4.1：**修复后语料 94 次 / 13 文件**）。本节**沿用**该标记，而不是引入第二个「未判定」词。

| # | 条目 | 当前状态 | **什么证据能解决它** | 解决者 |
|---|---|---|---|---|
| **U-1** | `ResponsiveAction_(j->i)` 的可观察性 | **无任何已登记通道**（`R16 §3.1` 逐字**禁止**用 `PPR` 工具推断它） | 一次 `R03` 逐行仪器检索，专查「可观察的 partner 行为」族；候选 `R03 §3.1` 的 `RMBM` 维护行为族（**其自身被 `R03 §3.3` S34 质疑**） | Track R3-E / 新证据轨 |
| **U-2** | `Caregiving` 的唯一行为锚候选 `RMBM` 是否落在 `R03 §3.3` S34 点名的「两个广泛使用的关系维持量表」之内 | `UNKNOWN_AS_OF 2026-09-28` | 打开 `Stafford (2010)`（S34）正文，核对其点名的是哪两个量表 | Track R3-E `E3` carrying-source check |
| **U-3** | `Dedication` · `OutcomeDependence` · `Cohesion` 的**任何**不变性证据 | **零证据**（`R03 §3.4` 逐字） | 一次覆盖这 3 个构念族的多组 CFA 不变性序列（`R11 U1`：configural → metric → scalar，每组 ≥300 dyad，两方向分别估计） | Track R3-G / R3-E |
| **U-4** | `Satisfaction` 是否存在独立于双方知觉的 **pair 属性** | `structurally_unobservable = YES`（作为 pair 属性），依据 `R02 §3.10(3)` `r=.18–.19` vs projection `.77–.90` | 与 `R02 U4`（`Cohesion`）同型的设计：独立于双方的 pair 级观测通道（第三方编码 / 共同叙事 / 跨评分者信度） | 研究轨；**注意：这可能不是可由研究解决的问题**（`NEXT_EXPERIMENTS` `A-7` 判「它是一条 Architect 裁决」） |
| **U-5** | 全部 18 个 `AGENT_ATTRIBUTE_*` 的通道与不变性 | 未做逐属性交叉表（`NOT_OPENED`） | `R03 §3.2`（时间尺度）× `R03 §3.4`（不变性）**逐属性**交叉 + `R16 §3.1` 的 `mapping_status` | 研究轨 |
| **U-6** | `applicable_scopes` 全列 | **0 / 60 行已填** | 先有观测性判定（`D` §3.5 的理由：填它需要先有观测性判定，否则只是把 `TBD` 搬个地方），再由 `HD-ST-1`（`VALIDATION_GATES_V0_2` §6.4）逐类对齐 | 本轨的后继 |
| **U-7** | `P5 ExclusivityRules`（**规则被遵守**） | 无 canonical 登记 | 需要一条新的 `AGENTS.md` 当前架构方向条目或一条 `PARAMETER §6` 补充，把「规则」与「遵守」分成两个落点 | **Architect**（不是研究问题） |

### 4.3 为什么 `applicable_scopes` 全部留空（沿用 `D` 的理由并加一条）

`D` §3.5 逐字：「它需要 `HD-ST-1`（`VALIDATION_GATES_V0_2` §6.4）与本文 §2 同时到位才能填；**填它需要先有观测性判定**，否则只是把 `TBD` 搬个地方。」

**本轨追加一条语料证据**：`R11` §2 的 **216 格**（24 元素 × 9 dyad-class，重算 `MP 69 / MS 74 / NA 24 / RD 22 / UK 27`）看起来正是「构念 × scope」表，但 `R11` §1 逐字声明：这些 `MEANING_PRESERVED` **全部**是**语义**判断，**本次没有找到任何**针对这 8 维 directed battery 的跨 dyad-type 测量不变性研究；且逐字「这 69 格**不可被计数、不可被聚合、不可当作相互独立的证据**」。

⇒ **语义稳定性 ≠ 可观察性。** 用 `R11` 的格码填 `applicable_scopes` 会把一个**自陈的未检验假设**（69 次重述）伪装成观测性判定。**故全部留空。**

### 4.4 唯一一条 registry → taxonomy 的交叉引用（`baseline libido`）

`R11` §2 矩阵的 `baseline libido` 行：`NA` in `R` / `D` / `A`，`UK` in `F` / `S` / `K` / `C` / `X` / `W`（合计 **3** 个 `NA` + **6** 个 `UK`）。
按 `UNKNOWN_APPLICABILITY_TAXONOMY` **L-3**，这 3 个 `NA` 格**必须**映射成 `APPLICABILITY_UNKNOWN` + 非空 `applicability_reason`（理由：规则族 R-2 尚不存在，无已登记规则可指向 `applicability_provenance`），**不是** `NOT_APPLICABLE_BY_RULE`。

**同时**（这是本轨最重要的一条轴间纪律）：`R11 §L-4` 逐字「**一旦被插补就构成伤害**」⇒ 该槽在 Axis 1 上**永远不得**落 `NOT_REPORTED` 而不带显式的 `applicability` 记录。`AGENTS.md`「Unknown/missing data must remain explicit; never silently coerce missing information into neutral/perfect-match values」在这里的具体含义是：**「插补」与「不适用」必须可区分，而当前没有第 3 个位置记录「这里有一个不适用问题尚未判定」。**

---

## 5. 「单一构念必须是两个有向状态的函数」—— 一条必须显式记录的观测性事实

> **登记**：`Mutuality_k(A,B) = H(Z[k,A,B], Z[k,B,A])`（`P9 R1`）与 `AsymmetryReadout_k`（`CURRENT_ARCHITECTURE §4.1`）**不是单个有向状态的 readout，而是两个有向状态的函数**。`TotalDependence` / `TotalPower`（对称）与 `RelativePower` / `PowerImbalance`（方向性）是同一形状在 power 族上的两个实例（X-13 / C-P4）。

**为什么这是观测性事实，不只是形状约定**：

1. **它使可观察性成为合取条件。** 派生量的可观察性 = `可观察(Z[k,A,B]) ∧ 可观察(Z[k,B,A])`。⇒ 在 `R16 §3.2` 审计的 16 个数据集中只有 **1** 个提供无外部假设的 `DIRECTED_EDGE` 双分量（D04 速配，且**无第二时间点**）的条件下，**每一个两向派生量的可观察性都被结构性限死在「两个方向同时可得」这一格上**。
2. **它与 `16` 的 `directionality_class` 直接耦合。** `directionality_class = AGENT_LEVEL`（14 个已审计量表全部如此）的变量**在结构上**不能进入 `Z[k,A,B]` 或 `Z[k,B,A]`；`= NON_SEPARABLE` 的变量（`R16 §3.2` 逐字：生理同步结构上无法分解为 `i→j` 与 `j→i`，且与结局关联方向矛盾：交感 `ES=+.19` / 副交感 `ES=−.21` / 总体 `ES=.09` 且 `I²=76%`）**永远**不能进入任何两向派生量。⇒ **一整个已审计的测量族对派生 readout 的贡献恒为「不可用」。**
3. **它使 `structurally_unobservable` 的答案依赖输入，故这 8 行全 `NOT_APPLICABLE` 是正确的读法**（`D` §3.5 已如此填）—— 但**必须**附上本节的合取条件，否则 `n/a` 会被读成「派生量不需要观测性登记」。

**本轨不做的事**：不定义 `H`、不设 comparator / 权重 / 距离度量 / 任何数值阈值（`CURRENT_ARCHITECTURE` §11 当前非目标；`AGENTS.md` representation-first invariant 1/2/4/6）。`CURRENT_ARCHITECTURE §4.1` 的 `AsymmetryReadout_k` 已要求 comparator **已注册**；**本轨不注册任何 comparator** ⇒ 该字段今天恒为 `NOT_AVAILABLE`。

---

## 6. 下游阻塞登记（`C-P13` / `E-C16` / `NEXT_EXPERIMENTS` `A-7`）

`D` §3.6 已列 4 条。本轨逐条更新**今天的状态**：

| # | 被阻塞项 | 阻塞机制 | **本轨之后的状态（2026-09-28）** |
|---|---|---|---|
| **B-1** | belief 层的 `g = FIRSTHAND` / `REPORTED` / … 赋值 | `structurally_unobservable` 无处可查 | **部分解锁（1 / 3 条 belief 行）**：`PPR` 的 `self_report = YES` 已凭 `R16 §3.1` 的 `DIRECT_PROXY` 落地 ⇒ `PPR` 可取 `g = FIRSTHAND`。**`PerceivedCommitment` / `PerceivedAttraction` 仍未解锁**（继承 `D7` / `D2` 的全 `TBD`）⇒ **belief 层整体仍未落地** |
| **B-2** | `Unknown` 类型学的落地 | 需先知道哪些构念**只能**被推断 | **部分解锁**：`OutcomeDependence` 已有 `latent_inferred_only = YES` + `structurally_unobservable = YES`（`coordination`）；`Satisfaction` 已有 `structurally_unobservable = YES`（作为 pair 属性）⇒ 轴 1 的 `NOT_ADDRESSABLE_BY_CHANNEL` 现在**有 2 个可用锚点**。**但 31 / 60 行仍 6 维全 `TBD`，且 `partner_report` 一列 `YES` = 0** |
| **B-3** | refinement 程序（`07` 的 `⊑` 程序）的依赖表 | `D` §3.6 称「依赖表本身即本 registry」 | **未解锁，且本轨的判断是「本 registry ≠ 依赖表」** —— 见 `UNKNOWN_APPLICABILITY_TAXONOMY` §7.6。`07` §5.3「第二批」逐字把 `I9` 的**共同前置**列为**三项分列**（① `⊑` 形式定义 + 逐坐标依赖表；② **C-P13** 可观察性 / 锚点登记表；③ `Role` 命名与层级澄清），可观察性登记表只是**第 ② 项**；`07` §5.1 `I9` 的判据是「已登记的 `∂F_i/∂z_j ≠ 0`」，而该表达式的 canonical 落点已在 `CURRENT_ARCHITECTURE.md` §7（`partial F_i / partial z_j != 0`）⇒ 那是**转移层的结构依赖**，不是可观察性。**本轨不把 registry 当作依赖表** |
| **B-4** | 研究侧已局部提出的单构念登记（`coordination` 不可知觉） | 缺一个可写入的登记表 | **已落地**：见 §5 与 G3 的 `D8` 行 + §2 的 `R02 §3.9(3)` 引文。这是**本轨唯一一条从研究侧「无处登记」变成「已登记」的条目** |

**B-3 的具体交付形态建议（供 parent 路由）**：依赖表应是一张**新表**，每行 = `∂F_i/∂z_j ≠ 0` 的一个已登记依赖，含**依据**与**消融臂**（`C-P1` 的 leave-one-construct-out）。本 registry 是它的**输入之一**（哪些坐标根本没有可观察值 ⇒ 依赖不可检验），不是它本身。

---

## 7. 观测性剖面共享但**不合并**的分组（`AGENTS.md`「Prefer few stable constructs」纪律的边界）

`AGENTS.md` 逐字：「Prefer few stable constructs + composition + time evolution over a growing checklist of ad-hoc variables.」本轨遵守该纪律的方式是**不合并行**，而不是删行。以下四组的行**故意保持分离**，理由逐条给出：

| 组 | 共享剖面 | 成员 | **为什么不能合并** |
|---|---|---|---|
| **P-α** | `self_report = YES`，其余 5 维**不共享** | `SexualDesire` · `Trust` · `AttachmentSecurity` · `PPR` · `Satisfaction`（**5** 行） | 这 5 行**只有 `self_report` 一维相同**，其余维度各不相同：除 `Satisfaction` 外 4 行 6 维中只有 1 维被判定；`Satisfaction` 另有 4 个有据判定。**自陈通道的强度也不同**：`SexualDesire` 有 state 级（双周题 `α_wave .69–.98`）；`Trust` **无** state 级工具（`R03 §3.2` 逐字「没有『信任更新』…的 state 工具」）**且其工具的构念身份被 `S18` 质疑**；`ECR-R` 有 62 文化区证据但**中国样本未达 scalar**；`PPR` 的工具被 `R16 §3.1` **明令禁止**用于推断其指代。⇒ 一个 `Y` 掩盖了这四档差异 |
| **P-β** | `directly_observable = Y` / `self_report = TBD` / `partner_report = TBD` / `behavioural_anchor = Y` / `latent_inferred_only = N` / `structurally_unobservable = N` | G1 的 **13** 行 + G2 的 1 行（**14** 行） | 它们的 **`applicable_scopes` 与证据严重度不同**：`sex acts` 带 `R11 §L-4` 的保护议题；`caregiving acts` 带 `R02 §表7` 的「不得当独立状态读出」；`conflict acts` 带 `R11 §3.3` 的「互惠的敌意 vs 单向的控制」不可区分；`messages sent` / `response latency` 有 `R03 §3.2` 的数字轨迹通道候选；`public declarations` 与 `InformationAction` 的边界未登记。⇒ 一个 `Y` 掩盖了 14 份不同的下游约束 |
| **P-γ** | 6 维全 `TBD` | **31** 行 | `AGENT_ATTRIBUTE_*` 的 **16** 行在此组内（`D` 把它们压成 1 行）。**压成一行等于断言「这 16 个属性的可观察性相同」** —— 而 `D` §3.5 自己逐字说「本轨把这一组压成一行**只是**骨架，不是『这些项可观察性相同』的判断」。⇒ **本轨的拆分是对 `D` 自陈欠账的清偿，不是 ontology 扩张** |
| **P-δ** | 至少 4 维全 `NOT_APPLICABLE` | G6 的 **6** 行（`Mutuality_k` · `AsymmetryReadout_k` · `TotalDependence/TotalPower` · `RelativePower/PowerImbalance` · `R4` · `R5`；G6 的另 2 行 `Satisfaction` = `PARTIAL`、`RelationalCohesion` = 全 `TBD`，**不属本组**） | X-13 逐字区分**对称**（`TotalDependence` / `TotalPower`）与**方向性**（`RelativePower` / `PowerImbalance`）；`R11 §L-1` 逐字指出**同一组依赖数值在健康照护 dyad 与胁迫 dyad 上伤害相反** ⇒ 对称读出与方向读出的**可解释性不同**。另 `R4` / `R5` 的 `n/a` 理由与派生量**不同**（是 `REJECT as primitive`，不是「派生量不直接观察」）。⇒ 一个 `n/a` 会掩盖 3 类不同的理由 |

---

## 8. 与 `D` §3.5 骨架的两处计数缺陷（**不静默调和**）

| # | `D` §3.5 的原文 | 逐字复核 canonical 后的实际值 | 本轨处置 |
|---|---|---|---|
| **1** | 「`ACTION_EVENT_OBSERVABLES`（§8 列举的 **12** 类：money spent / messages / latency / touch / caregiving acts / compliments / conflict / repair / gifts / travel / public declarations）」——括号内实列 **11** 个名字 | `PARAMETER_CONVERGENCE_V0_1.md` §8 的代码块是 **13** 行（逐项：`money spent` / `messages sent` / `response latency` / **`hours together`** / **`sex acts`** / `physical touch` / `caregiving acts` / `compliments` / `conflict acts` / `repair attempts` / `gifts` / `travel to meet` / `public declarations`）。⇒ `D` 声明「12 类」但只列 **11** 个名字，且相对 canonical **漏列 `hours together` 与 `sex acts` 两项**；另有 3 项被简写（`messages` / `latency` / `travel`，canonical 分别为 `messages sent` / `response latency` / `travel to meet`） | 本轨 G1 按 canonical 列 **13** 行。**请 parent 路由给 `D`**（`D` 的 §3.5 是 SSOT 侧，本轨无权改） |
| **2** | 「`AGENT_ATTRIBUTE_*`（`PARAMETER §7` 的 **13** 项：age / sex-gender attributes / health / income / assets / liabilities / education / skills / location / family obligations / relationship history / life goals / habit patterns / personality traits / baseline libido / generalized trust / caregiving propensity / attachment tendency）」 | `PARAMETER_CONVERGENCE_V0_1.md` §7 的代码块是 **15 行**，其中 `income / assets / liabilities`（3 项）与 `education / skills`（2 项）各在一行内合并 ⇒ **18 个具名属性**。`D` 写「13 项」但列出 **18** 个名字 ⇒ **自相矛盾** | 本轨 G7 按 canonical 列 **18** 行。**请 parent 路由给 `D`** |

**这两处都不影响 `D` 的任何裁决**，只是骨架的枚举计数。**本轨未改 `D` 的文件。**

---

## 9. 路由说明（给 parent）

| 本轨产物 | 建议合并进 | 方式 |
|---|---|---|
| 本文 §1（字段读法） | `MEASUREMENT_SEMANTICS_V0_1.md` **§3.3 之后新增读法小节** | 逐字搬入。**这是 schema 的补充而非变更**，请 `D` 确认是否接受 |
| 本文 §2（60 行内容） | 同上 **§3.5 骨架 → 内容** | 替换。`D` 的 §3.2 schema / §3.4 约束**不动** |
| 本文 §3（统计） | 同上 §3.5 末尾 | 追加 |
| 本文 §4（`UNKNOWN_AS_OF` 登记） | 同上 §3.6 之后 | 追加；可与 `NEXT_EXPERIMENTS` 的 `A-7` 交叉引用 |
| 本文 §5（两向函数事实） | 同上 §3.5 之后 | 追加 |
| 本文 §6（阻塞登记） | 同上 §3.6 | 逐条替换 / 更新 |
| 本文 §7（不合并分组） | 同上 §3.5 之后 | 追加 |
| 本文 §8（两处计数缺陷） | **不改 `D` 的文件**；作为 `conflicts_and_routes` 交回 parent | 见本文 §8 表 |

**合并顺序建议**：先 `C`（`VALIDATION_GATES_V0_2`，因为 `applicable_scopes` 依赖 `HD-ST-1`）→ 再 `D`（`MEASUREMENT_SEMANTICS_V0_1`）→ 再本轨两份文档。

---

## 10. `open_questions_for_architect`

1. **§1 的字段读法是否接受？** 六个维度在 `D` §3.2 只有字段名与枚举，没有读法。本文的读法（尤其 `directly_observable` = 「不依赖自陈的外部通道」）决定了 §3 的每一个取值。**不接受则本文的 19 个有据判定需重算。**
2. **是否需要为「构念身份冲突」（`G-2`）与「构念定义欠定」（`G-1`）开一个面？** 见 `UNKNOWN_APPLICABILITY_TAXONOMY` §7.5。三者形状相同：**不是「没查到」，也不是「不适用」，而是「问题本身还没被正确提出」。**
3. **`D` open question 6（Agent attributes 是否必须逐项拆分）的答案本轨已给「是」。** 请 parent 确认。
4. **`D` open question 7（`applicable_scopes` 是否必须与 `HD-ST-1` 一一对应）**：本轨的答案是「**当前不填**」，理由见 §4.3（`R11` 的 216 格是语义判定、零不变性研究）。若 Architect 要求先按 `HD-ST-1` 建行，**schema 需加一个「域 × 可观察性」二维形状** —— **这是 schema 变更，不由本轨擅自做**。
5. **`D` open question 8（`I9` 依赖表的形状是否就是本 registry）**：本轨的判断是**不是**（§6 B-3 + `UNKNOWN_APPLICABILITY_TAXONOMY` §7.6）。请 parent 或 `C` 决定表述。
6. **U-7（`ExclusivityRules` 的「规则被遵守」）需要一条新的 canonical 落点吗？** 这是本轨新登记的一行，现有 canonical 无对应。

---

## 11. `explicit_non_claims`

1. **未新增任何构念、层、primitive、transition law、comparator、权重、距离度量或数值尺度。** 本表是 measurement metadata。
2. **未运行任何 Gate，未映射任何 fixture。** 本文无任何 mapping 结果、cell 状态或覆盖数字。
3. **未定义任何 metric。** `evidence_mass` / `width` / `coverage` 的度量**未冻结**（`07` §9.2 `D8` / §11-2）。
4. **未把 `layer_ref` 当作可观察性证据。** 沿用 `D` §3.4。G3 的 8 行里，**没有任何一行的维度由层裁决判定**。
5. **未用 `R11` §2 的 216 格填 `applicable_scopes`。** 它们是语义判定，且 `R11` §1 逐字声明零不变性研究（§4.3）。
6. **未把 `R16 §3.2` 的「16 个数据集中只有 1 个提供 `DIRECTED_EDGE` 双分量」读作领域总体结论。** 这是 `X-14` 允许的**检索范围结论**。
7. **未把 `Satisfaction` 的 `structurally_unobservable = YES` 读作「该 dyad 不可研究」。** 它断言的是「**作为 pair 属性**不可观察」；作为**个体**评价状态它 `self_report = Y`。
8. **未主张 `ResponsiveAction_(j->i)` 不可观察。** 只记录「**无任何已登记通道**」，并指出 `PPR` 工具被**明令禁止**用于推断它（U-1）。
9. **未把 `R03 §3.3` 的 S34 质疑指定给 `RMBM`。** 该逐字未指名是哪两个量表（U-2）。
10. **未合并任何共享观测剖面的行。** 31 行 6 维全 `TBD`、6 行 `NOT_APPLICABLE` **是欠账与派生性的诚实记账**，不是可折叠的冗余（§7）。
11. **未把 `D` 的两处计数缺陷静默改正。** 已在 §8 逐条列出并路由（`12` vs `13`；`13` 项 vs 18 个具名属性）。
12. **未把 PR #31 / #32 的 swarm 主张当作已验证科学。** 本文引用的 `R02` / `R03` / `R11` / `R16` 均为**研究候选**；凡与 adjudication V1 冲突处一律以裁决为准（X-1 / X-4 / X-5 / X-13 / C-P4 / C-P11 / C-P13）。
13. **未合并、未 push、未开 PR、未改任何 GitHub review state。** 交付形式 = branch + commit + packet。
14. **未读取 / 未执行 / 未引用 `#20` / `#21` / `#22`；未运行 Eye/Juece；未下载受限数据；未做文献扫描。**
