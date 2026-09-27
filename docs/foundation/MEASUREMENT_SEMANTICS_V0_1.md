# Measurement / Representation Semantics v0.1

**Status:** CANDIDATE CANONICAL（**schema 与规范词表已定**；逐构念内容为骨架，**未填满**）
**As of:** 2026-09-28
**Authority:** `youling/lhrm#30` `ARCHITECT_ADJUDICATION_V1`（comment `5854920569`）X-1 / X-3 / X-4 / X-5 / X-13、C-P3 / C-P4 / C-P5 / C-P11 / C-P13、ruling §C item 3；`ARCHITECT_ROUND3_DISPATCH_V1`（comment `5854930069`）Track R3-D
**SSOT 归属：** applicability 轴 = 本文 §2；observability registry = 本文 §3
**不重复他人：** 门的诊断 / 处置 / 流水线 = `docs/foundation/VALIDATION_GATES_V0_2.md`；落点词表 `LHRM-LANDING-1` = `docs/foundation/PARAMETER_CONVERGENCE_V0_1.md` §13；层裁决 = `docs/foundation/CURRENT_ARCHITECTURE.md` §3.1；动作词表 = 同上 §6.1

> **本文不含任何已执行结果。** 未运行任何 Gate、未映射任何 fixture、未实施任何 transition law、
> 未设任何普适数值阈值（`AGENTS.md` 研究纪律）。**逐构念内容由兄弟轨 `F` 交付，本文只给 schema。**

---

## 1. 这一层补的是什么

canonical 现在缺的不是构念，而是**两个「无处登记」的语义位**：

1. 「此构念在该 dyad / 语境中不具独立意义」这条**负面知识**——它既不是 `0` 也不是 `Unknown`，
   今天只能写在报告正文里（X-5 `EV3` 的残余内核）。
2. 「哪些构念原则上可被直接观察 / 只能自陈 / 只能由对方报告 / 只能被推断 / 结构性不可观察」
   这份**清单本身**（C-P13）。今天项目里不存在它，所以 belief 层的 `g = FIRSTHAND` 与
   `structurally_unobservable` **在类型上就无法落地**。

两条都是**登记位**，不是新的状态层，也不是新的构念。

---

## 2. Applicability 轴（X-5 / C-P5）

### 2.1 值域是许可式，不是封闭枚举（X-5 已定）

`CURRENT_ARCHITECTURE.md` §9 与 `AGENTS.md` representation-first invariant 第 5 条的坐标类型清单
都是**许可式**（`可以` / `may be`）。canonical **没有任何**封闭性声明。
因此「缺少一个合法值」不是逻辑矛盾，不构成需要修本体的事件。

### 2.2 规范字段形状

```text
applicability            ∈ { APPLICABLE,
                             NOT_APPLICABLE_BY_RULE,
                             APPLICABILITY_UNKNOWN }
applicability_reason     # NOT_APPLICABLE_BY_RULE 时必填、非空
applicability_provenance # 指向支配该构念的 Boundary/Constraint 落点或规则的锚
```

- `NOT_APPLICABLE_BY_RULE` 的**唯一**合法触发是：存在一条**已命名**的 boundary / agreement / 规则，
  且该规则在语境中支配此构念的取值。`applicability_provenance` **必须**指向那条规则。
  与 `AGENTS.md` 的 Unknown 纪律同源：不能以「不适用」之名**不写理由**。
- `APPLICABILITY_UNKNOWN` 是「尚未判定」，**不是**「不适用」的委婉说法，也**不是**默认值。
- 与已命名边界规则并存的**优先级**（X-5 `EV3` 的证据链）：

```text
事实层：该事实本身落在 CONSTRAINT_AGREEMENT（BoundaryRule_(A,B,domain) 等）
轴层  ：相关构念的 applicability 记 NOT_APPLICABLE_BY_RULE，provenance 指向上面那条规则
```

即：规则**已经**被表示（不是缺口）；缺的是「这**条构念**在此语境下无独立意义」这条负面知识的**登记位**。

### 2.3 四条正交性

| 正交于 | 含义 |
|---|---|
| 值域 | `applicability` **不是**坐标取值，不进入值枚举 |
| 值域中的 `Unknown` | 坐标值可以是 `Unknown` 而 `applicability = APPLICABLE`；反之亦然。两者是不同命题 |
| `uncertainty` | `APPLICABLE` 与很宽的 `uncertainty` 完全可以并存。「可适用」不是「已知」 |
| mapping status | `mapping_outcome` / `MAPPING_FAILURE`（`VALIDATION_GATES_V0_2` §3）是**另一条轴**。`MAPPING_FAILURE` 既不是 applicability 的取值，**也不**构成「不适用」的证据 |

### 2.4 五条禁止（逐条）

1. **不得**写成 `0`。
2. **不得**写成 `Unknown`。
3. **不得**把 `applicability` 加入坐标值域。
4. **不得**把 applicability 值折进 `Unknown` 的值枚举（X-5 明确：这是两轴分离的**唯一**理由；
   直接合并会得到一个 14+ 值的大枚举，违反 `AGENTS.md` 的构念纪律）。
5. 值域内**不得**出现 `NA`。

### 2.5 背景：被推翻的主张、真正的残余、以及暴露面

| 项 | 状态 | 出处 |
|---|---|---|
| 「值类是穷举集 ⇒ 存在一个逻辑上无合法表示的坐标 ⇒ canonical 内部矛盾」 | **REFUTED**。值类清单是许可式；两份清单互不一致；全库检索**无**封闭性声明。canonical 已有具名槽位 `BoundaryRule_(A,B,domain)`（`PARAMETER_CONVERGENCE` §6 `P5`，`KEEP as Constraint/Agreement`），并有一个**正是针对该语义**的 worked example（`CURRENT_ARCHITECTURE` §6：「订婚前不发生性行为」更接近 Agent boundary / constraint，而不是「性欲为零」） | X-5；`EV3` Claim 1 |
| 「`NA` 判定本身成立」（例：某 sibling dyad 上 `SexualDesire` 不适用） | **`HOLD_FOR_EVIDENCE`**。最强反证未处理。**本文不主张任何具体构念在任何具体 dyad 上不适用** | X-5；`G-C11` |
| **真正的残余**：canonical 缺少登记「某构念在某 dyad-type 上不具独立语义」的**正式位置** | **PLAUSIBLE → 本轮已落为 §2.2** | `EV3` Claim 1 残留内核 |
| **暴露面** | **若 Architect 将来裁定值类清单是封闭集，本节必须重审。** 这是 `EV3` 自陈的、对自身最依赖解释力的一环 | X-5 (c) |

### 2.6 与兄弟轨 `F` 的接口契约

- 本轨**只**定义 schema 与规范词表；逐项内容与「全部既有竞争词表 → 本词表」的
  **conversion table** 由兄弟轨 `F`（Track R3-F，delivery packet `lanes/R3_F.md`）交付。
- `F` **必须**使用本文的**逐字**字段名 `applicability` / `applicability_reason` / `applicability_provenance`
  与枚举 `APPLICABLE` / `NOT_APPLICABLE_BY_RULE` / `APPLICABILITY_UNKNOWN`。
- `F` **不得**另立第二份 applicability 词表。既有竞争词表**只能**出现在 conversion table 中作为**被转换的源列**。
- 冲突时：本文是 SSOT，`F` 的行内容以本文为准并回填。

---

## 3. Observability registry（X-4 / C-P13）

### 3.1 性质

**这是 measurement metadata，不是 ontology 扩张。**

- 登记一个构念「原则上能被观察到什么程度」，**不**新增 primitive、**不**新增层、**不**改变任何层的归属。
- 它的唯一作用是成为**未来 `Unknown` / `Belief` 映射规则的前置依赖**（C-P13）。
- 一行 registry 记录**不是**一次测量结果，**不得**被当作该构念的证据。

### 3.2 逐行 schema

```text
construct_ref        # §-限定的 canonical id，例：PARAMETER §4 D4 / Trust
layer_ref            # LHRM-LANDING-1 落点类；若该构念有层裁决，指向 CURRENT_ARCHITECTURE §3.1
directly_observable        ∈ { YES, NO, TBD, NOT_APPLICABLE }
self_report                ∈ { YES, NO, TBD, NOT_APPLICABLE }
partner_report             ∈ { YES, NO, TBD, NOT_APPLICABLE }
behavioural_anchor         ∈ { YES, NO, TBD, NOT_APPLICABLE }
latent_inferred_only       ∈ { YES, NO, TBD, NOT_APPLICABLE }
structurally_unobservable  ∈ { YES, NO, TBD, NOT_APPLICABLE }
applicable_scopes     # HD-ST-1 的 dyad_class 列表 + 本文 §2 的 applicability 引用
evidence_provenance   # 锚 + 强度；无则 NOT_YET_REGISTERED
completeness          ∈ { COMPLETE, PARTIAL, SKELETON }
```

**词汇纪律：** 本轴**不用** `Unknown` 作为「未判定」标记，改用 `TBD`。
理由：值域的 `Unknown`、applicability 的 `APPLICABILITY_UNKNOWN` 与本轴的「未判定」
是三个不同命题；共用一个词会重演 `07` / `08b` 的**三处同名不同义**（`E-C23`）。

### 3.3 完整性标记的读法

- `COMPLETE`：6 个观测维度**全部**为 `YES` / `NO`，且有 `evidence_provenance`。
- `PARTIAL`：部分维度已判定，其余 `TBD`。
- `SKELETON`：维度已列出但 `evidence_provenance = NOT_YET_REGISTERED`。

> **`TBD` 不得被读作 `NO`。** registry 中 `TBD` 的比例**就是**本项目 measurement metadata 的真实完成度，
> 是待办规模的诚实记账，不是缺陷的隐藏。

### 3.4 关键约束：本表**不能**由层裁决推出

层裁决回答「它住在哪一层」；本表回答「它原则上**能不能**被观察、**怎么**才能被观察」。**前者不蕴含后者。**
今天 canonical 只给了前者，因此除少数由 canonical 自身文本已写明「action / observation / institutional fact」
的行外，**几乎全部为 `TBD`**。这**不是**本轨偷懒，而是本轨要记录的事实：**这份清单今天不存在**。

### 3.5 填充骨架

图例：`Y` = canonical 文本直接写明 · `N` = canonical 文本直接写明不可能 · `–` = `TBD` · `n/a` = `NOT_APPLICABLE`。
**除第 1 组外，全部标记的 `basis_for_mark` 都是「层归属」，不是「可观察性」。**

| construct_ref | 观测性 | layer_ref | evidence_provenance |
|---|---|---|---|
| `ACTION_EVENT_OBSERVABLES`（§8 列举的 12 类：money spent / messages / latency / touch / caregiving acts / compliments / conflict / repair / gifts / travel / public declarations） | `Y` 直接观察 | `ACTION_EVENT` | `PARAMETER §8` 逐条写明「canonical 位置优先是 Action/Event + provenance + timestamp」。**只覆盖 `directly_observable`；其余 5 维 `–`** |
| `InformationAction`（`Disclose` / `Withhold` / `Misrepresent`） | `Y` 直接观察（一次动作 = 一条 event 记录） | `ACTION_EVENT` | `CURRENT_ARCHITECTURE §6.1`。**不是新 state primitive** |
| `Liking` · `RomanticAttraction` · `SexualDesire` · `Trust` · `AttachmentSecurity` · `Caregiving` · `Dedication` · `OutcomeDependence`（`PARAMETER §4` `D1`–`D8`） | 全 `–` | `DIRECTED_RELATIONSHIP_STATE` | **无 observability 证据。** `PARAMETER §4` 逐条给的是「为什么保留」的**反例**论证，不是可观察性论证 |
| `PPR`（`PARAMETER §5 B1`） | 全 `–` | `BELIEF_STATE` | **层裁决 ≠ 自陈登记。** canonical 说它是关系特定知觉，但「是否可作 first-hand 报告」正是本文 §3.6 要解决而今天**未解决**的那一条 |
| `PerceivedCommitment` / `PerceivedAttraction` / `PerceivedSexualDesire`（`Belief_i(...)` 形式） | 全 `–` | `BELIEF_STATE` | `PARAMETER §5 B2` 只定义**形式**，未定义可观察性 |
| `Cohesion/We-ness` · `PerceivedWeNess`（`PARAMETER §6 P1`） | 全 `–` | `CONTESTED`（pair process vs 双方 perception） | canonical 自己标 `contested scope`。**`structurally_unobservable` 此刻无法判** |
| `ValueCongruence` · `GoalAlignment`（`PARAMETER §6 P2` / `P3`） | 全 `–` | `PAIR_STATE`（pair comparison） | canonical 给的是「是何种比较」，不是可观察性 |
| `RelationshipIdentity/Agreement`（`PARAMETER §6 P4`） | 全 `–` | `CONSTRAINT_AGREEMENT`（institutional fact） | **`institutional fact` ≠ `directly_observable`。** 需登记才能分辨，已标 `TBD` |
| `BoundaryRule` / `ExclusivityRules`（`PARAMETER §6 P5`） | 全 `–` | `CONSTRAINT_AGREEMENT` | `KEEP as Constraint/Agreement`；可观察性未登记 |
| `Satisfaction`（`PARAMETER §9 R3`） | 全 `–` | `DERIVED_READOUT`（evaluation-state candidate） | **层已定、applicability 未定、可观察性未定。** 三者是不同命题 |
| `Mutuality_k` · `AsymmetryReadout_k`（派生） | `n/a` | `DERIVED_READOUT` | 派生量不直接观察；其可观察性**取决于输入**。形状约束见 `CURRENT_ARCHITECTURE §4.1` |
| `TotalDependence` / `TotalPower`（对称派生聚合） · `RelativePower` / `PowerImbalance`（方向性读出） | `n/a` | `DERIVED_READOUT` | 同上。X-13 / C-P4 已定：无独立普适 Power primitive |
| `RelationalCohesion` | 全 `–` | 独立 relation/process 量 | X-13：它与 total / relative power 的**关系**独立存在，不是 total power 的定义 |
| `RelationshipQuality` / `Compatibility` / `MatchScore`（`PARAMETER §9 R4`） | `n/a` | `REJECT as primitive` | 未来只可能作 task-specific readout |
| `AGENT_ATTRIBUTE_*`（`PARAMETER §7` 的 13 项：age / sex-gender attributes / health / income / assets / liabilities / education / skills / location / family obligations / relationship history / life goals / habit patterns / personality traits / baseline libido / generalized trust / caregiving propensity / attachment tendency） | 全 `–` | `AGENT_STATE_ATTRIBUTE` | **`SKELETON`。** 须由 `F` 逐项拆开；本轨把这一组压成一行**只是**骨架，不是「这些项可观察性相同」的判断 |
| `ENVIRONMENT_FACT` | 全 `–` | `ENVIRONMENT` | 未登记 |

**`applicable_scopes` 一列今天整体留空。** 它需要 `HD-ST-1`（`VALIDATION_GATES_V0_2` §6.4）与本文 §2
同时到位才能填；**填它需要先有观测性判定**，否则只是把 `TBD` 搬个地方。

**两处必须随表带走的 scope 缺陷记录（X-4）：** `domain` 被要求作强制 signature 的缺陷
**不限于 `Trust`**；对 `OutcomeDependence`（`PARAMETER §4 D8`）的同一条要求**复用了同一条
organizational-trust 单一来源**。两者的处置相同：`domain` = **可选 facet / context index，
非必需 signature**，待 measurement invariance（`FACET_RECOMMENDED_NOT_REQUIRED`，C-P3 部分接受）。

### 3.6 为什么它在关键路径上

`E-C16` 判它是**唯一**的 head-of-list 阻塞项：`07 §11-3` 与 `08b §9-1` **从相反方向独立发现同一缺口**。
项目内不存在该清单 ⇒ 下列各项**今天全部无法落地**：

| 被阻塞项 | 阻塞机制 |
|---|---|
| `Unknown` 类型学的落地 | 需要先知道哪些构念**只能**被推断，才能区分「没测到」与「测不了」 |
| refinement 程序（研究侧 `07` 的 `⊑` 程序的依赖表，`I9`） | 依赖表本身即本 registry |
| belief 层整体 | `g = FIRSTHAND` 与 `structurally_unobservable` 两个赋值**无处可查** |
| 研究侧已局部提出的单构念登记（`coordination` 不可知觉） | 缺一个可写入的登记表 |

### 3.7 与兄弟轨 `F` 的接口契约

- 本轨**只**定义 §3.2 的 schema、§3.3 的读法与 §3.5 的骨架行集合。
- `F` 交付：**填充后的逐行内容** + **全部既有竞争词表 → 本 schema 的 conversion table**
  （既有平行编码见 `E-C23`：`07` 与 `08b` 各自发明平行编码，且存在**三处同名不同义**）。
- `F` **不得**新增维度、**不得**引入第二个未判定标记（只用 `TBD`）、**不得**另立第二份 registry。
- `F` 的每一行必须带 `evidence_provenance`；无来源的行只能是 `SKELETON` 且 `TBD`。

---

## 4. Supplied 决策的落地位置（不含被取代文本的复制）

| 裁决 | 落地位置 | 形态 |
|---|---|---|
| X-1 `PPR` = BeliefState | `CURRENT_ARCHITECTURE §3.1`；`PARAMETER §5 B1` | 已定，非开放问题 |
| X-1 `Satisfaction` = Derived candidate | `CURRENT_ARCHITECTURE §3.1` | 同上 |
| X-3 后果预登记 + 撤回「canonical 内部不一致」 | `PARAMETER §9 R3` | **只登记后果，不预判结论** |
| X-4 `Trust` / `AttachmentSecurity` 保持分列 | `CURRENT_ARCHITECTURE §3.1`；`PARAMETER §4 D4` / `D5` | 无第二处 `FeltSecurity` 槽位 |
| X-4 / C-P3 `domain` = 可选 facet | `PARAMETER §4 D4`；本文 §3.5 | `FACET_RECOMMENDED_NOT_REQUIRED` |
| X-5 值域许可式 | 本文 §2.1 / §2.5 | 与 `CURRENT_ARCHITECTURE §9.1(a)` 引用一致 |
| C-P5 applicability 轴 | 本文 §2.2 | 逐字字段名 + 三值枚举 |
| C-P11 `InformationAction` | `CURRENT_ARCHITECTURE §6.1` | 动作词表，非新 state primitive |
| C-P4 / X-13 power readouts | `CURRENT_ARCHITECTURE §4.2` | 对称聚合 + 方向性读出；R2-b `HOLD` |
| 不对称读出的形式修正 | `CURRENT_ARCHITECTURE §4.1` | 取代 `distance(...)`（见 §5） |
| C-P13 observability registry | 本文 §3 | schema + 骨架 + 阻塞登记 |

---

## 5. 取代关系与跨轨路由

| # | 原文（位置） | 状态 | 取代者 / 路由 |
|---|---|---|---|
| 1 | `Asymmetry_k(A,B) = distance( Z[k,A,B], Z[k,B,A] )`（`CONSTRUCT_SCOPE_DIRECTIONALITY.md:84-89`） | **本形式被取代**，但**本轨不改该文件**（兄弟轨 `C` 所有） | 取代形式 = `CURRENT_ARCHITECTURE §4.1` 的 `AsymmetryReadout_k`。理由：`distance` 对 `interval` / `ordinal` / `category` / `distribution` / `Unknown` 未定义，与 representation-first invariant 4 冲突。**路由给 parent：`C` 轨或 parent 需在该处加 `SUPERSEDED_BY_REPAIR` 注记**（本轨遵守 `AGENTS.md`「不因新模型取代就抹掉旧证据」，原文一行未删） |
| 2 | `PARAMETER §4 D4` 的 `domain` 强制 signature（由研究侧提出） | **REJECT** | X-4 / C-P3：改为 `FACET_RECOMMENDED_NOT_REQUIRED` |
| 3 | 研究侧 `02b` 提出的「`Trust` 下新增具名 `FeltSecurity` facet 槽位」 | **REJECT** | X-4 / C-P3 部分接受：`D5` 的 `Attachment Security / Felt Security` **已拥有该措辞**，重复登记会加重正在审查的歧义。**该文件在研究侧（Track R3-A），由 parent 路由更正** |
| 4 | `domain` 强制要求同样施加于 `OutcomeDependence`（`PARAMETER §4 D8`） | 同 #2 | **§4 D8 不在本轨白名单**（本轨只拥有 §4 `D4` / `D5`）。**路由 parent**：建议在 `D8` 追加与 `D4` 同一句 `FACET_RECOMMENDED_NOT_REQUIRED`，理由是它**复用了同一条单一来源** |
| 5 | 「`§4 D7` 与 `§9 R3` 之间存在 canonical 内部矛盾」这一**框架** | **WITHDRAWN** | X-3：`NO LOGICAL CONTRADICTION`。canonical 侧在 `PARAMETER §9 R3` 记录；研究侧表述的更正属 Track R3-A，**路由 parent** |
| 6 | `AGENTS.md` representation-first invariant 第 5 条是否补显式「许可式」声明 | **未做** | 本轨对 `AGENTS.md` 的授权**只覆盖** diagnosis 清单那一行（兄弟轨 `C` 的镜像义务）。**路由 parent** |

---

## 6. `explicit_non_claims`

1. **未运行任何 Gate，未映射任何 fixture。** 本文无任何 mapping 结果、计数或 cell 状态。
2. **未主张任何具体构念在任何具体 dyad 上「不适用」。** §2 是一条**登记机制**；
   `G-C11` 判 `HOLD_FOR_EVIDENCE`，本文**不**继承该主张。
3. **未把 applicability 值加进任何坐标值域**，未新增 `NA`，未产生第二个 `Unknown` 标记。
4. **未新增任何构念、层、primitive、transition law、comparator、权重、距离度量或数值阈值。**
5. **未裁定 `Trust` 与 `AttachmentSecurity` 的合并或拆分。** 两者**保持分列**；
   更细的 facet 切分（如 vulnerability / non-exploitation expectation）**仍是 candidate**，
   且必须使用**更窄的语义标签**——不得复用已被 `D5` 占用的 `FeltSecurity` 措辞。
6. **未确认任何构念的可观察性。** §3.5 除 `ACTION_EVENT_OBSERVABLES` 与 `InformationAction`
   两行（依据 canonical 自己写明的 action/observation 落点）外**全为 `TBD`**。
7. **未把 `layer_ref` 当作 observability 证据。** §3.4 明写二者不可互推。
8. **未给 relational cohesion 下定义，也未把它接回 total power。** 只记录 X-13 的裁定：
   它是独立的 relation/process 量。
9. **未接受 R2-b 的任何槽位。** punitive capacity / legitimacy / perceived power / felt compliance
   保持 `HOLD_FOR_EVIDENCE`；H-E2 的「逐字核实」**不**等于这四个槽位已被确立。
10. **未把 `Withhold` 的成立条件放宽。** 缺 `info_ref` 或缺 `opportunity_or_expectation_ref`
    一律**不是** `Withhold`；沉默不自动是 Action。
11. **未把 PR #31 / #32 的 swarm 主张当作已验证科学。** 实现的是 adjudication V1 的裁决；
    凡 swarm 主张与裁决冲突处一律以裁决为准。
12. **未合并、未 push、未开 PR、未改任何 review state。** 交付形式 = branch + commit + packet。
13. **未读取 / 未执行 / 未引用 `#20` / `#21` / `#22`；未运行 Eye/Juece；未下载受限数据；未做文献扫描。**
