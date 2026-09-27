# Unknown / Applicability Two-Axis Taxonomy v0.1

**Status:** CANDIDATE CONTENT（**未合并、未跑门、未实施任何 transition law**）
**As of:** 2026-09-28
**Authority:** `youling/lhrm#30` `ARCHITECT_ADJUDICATION_V1`（comment `5854920569`）**X-5**、**C-P5**、**C-P13**、**ruling §C item 3**；`ARCHITECT_ROUND3_DISPATCH_V1`（comment `5854930069`）Track **R3-F**
**接口契约的 SSOT 归属：** applicability 字段形状 = `docs/foundation/MEASUREMENT_SEMANTICS_V0_1.md` §2.2（兄弟轨 `D`，branch `architect/measurement-semantics-v0.1`）。**本文不改写该形状**，只交付其内容侧的两轴分类与转换表。
**mapping 侧的 SSOT 归属：** `docs/foundation/VALIDATION_GATES_V0_2.md` §3（兄弟轨 `C`）。**本文不重定义 mapping 词表。**
**观测性登记表：** 内容见同分支 `docs/foundation/OBSERVABILITY_REGISTRY_V0_1.md`（schema 仍以 `MEASUREMENT_SEMANTICS_V0_1.md` §3.2 为准）。

> **本文不含任何已执行结果。** 未运行 Gate A/B/C，未映射任何 fixture，未设任何数值阈值，未主张任何具体构念在任何具体 dyad 上「不适用」。

---

## 0. 本文补的是什么

`18_CROSS_LANE_CONFLICT_AUDIT.md` `CF-12b` 判定：语料里存在**至少六套**互不兼容的「无值」编码，零交叉映射，其中**最广被使用的一套**（`UNKNOWN_AS_OF*`）不按 lane 组织、因此在任何按 lane 列举的清单里都必然先被漏掉。`CF-12c` 进一步指出：把各 lane 的取值映射成 `07` tag 集的「子集」是**类型错误**，因为已知有两项在 `07` tag 集里**没有对应值**（`MAPPING_FAILURE` 是表示失败；`UNDETERMINED` 是方向性不可分）。修法必须重写为**两轴构造**。

本文就是那次重写，并把 `CF-12c` 留给 Track R3-F 的那一格（`R08b` 行标 **未映射**）补上。

`R-K6`（`UNSUPPORTED`）只否定了「`Unknown` 值域**完全**由 6 个 lane 提出」这一**强主张**；其**弱主张**——`UNKNOWN_AS_OF` 是全语料使用最广的「无值」记账标记——由 `K-C7` 支持，本文 §5.1 给出可复算计数。

---

## 1. 为什么是两条轴，以及 `MAPPING_FAILURE` 为什么在两条轴之外

### 1.1 三条正交性（逐字承接 `MEASUREMENT_SEMANTICS_V0_1.md` §2.3，本文只补语料证据）

| 正交于 | 语料中的反例（可复算） |
|---|---|
| **值域** | `applicability` 不是坐标取值。`11_GENERAL_HUMAN_DYADS_SCOPE.md` §2 矩阵 216 格中 **24 格**为 `NA`，这 24 格**不是**值，而是对该格构念在该 dyad-class 上的适用性判断。`18` `CF-12b` 第 57 行已把这条写进披露 |
| **值域中的 `Unknown`** | `08b` §2.6 的 `g = UNKNOWN`（「根据不可辨：丢失、未记录、法务材料中不可判定」）与 Axis 1 的 `NOT_ASSESSED` 是**同一族**；而 `07` §1 的 `structurally_unobservable`（不可被**该通道**观测）与 Axis 2 的 `APPLICABILITY_UNKNOWN`（尚未判定该构念在此语境是否有独立意义）**是两个不同命题**。`07` §1.2 逐字写明这一点 |
| **`uncertainty` / mapping status** | `16_EMPIRICAL_VALIDATION_PROTOCOL.md` §3.4 的 `uncertainty` 块（`estimated_uncertainty` / `measurement_error_known` / `floor_ceiling_risk` / `missingness_mechanism` / `invariance_level_tested`）与 §3.1 的 `mapping_status` 被 `16` 自己称作「第三个字段」，而 §3.2 又称 `directionality_class` 为「**第二个正交必需字段**」。三条轴在 `16` 内部就已经分开，本文只是把 `07`/`08b` 侧补齐 |

### 1.2 `MAPPING_FAILURE` 的处置：不建第三条轴

- `MAPPING_FAILURE` 的取值域、产生点（`VALIDATION_GATES_V0_2.md` §3.4 `STAGE 1`）、持久性与 8 类诊断词表，**全部由兄弟轨 `C` 拥有**。
- `18` `CF-12c` 提议的「轴 3 · mapping status」，其取值域写成 R16 的 6 值 **∪** R15 的 7 值 verdict **∪** `UNDETERMINED`。**这是一个两套不可比词表的并集**，若落地会成为与 `C` 的 `mapping_outcome` 并列的第二份 SSOT。**本文不采纳该并集**，改为：mapping 侧一律**引用** `C` 的 `mapping_outcome` + `diagnosis`，本文 §5.2 只给出 R15/R16 → `C` 的**转换**（作为待 `C` 复核的候选）。
- 「材料充分但表示装不下」与「材料不足」在类型上不同（`15` §15.6.3 规则 3 逐字）。这条区分是 `MAPPING_FAILURE` 留在两轴之外的**承重理由**。

---

## 2. 轴 1 — epistemic / measurement uncertainty

### 2.1 记录形状（**factored register，不是单一枚举**）

```text
axis1_evidence_state {
  u_addressability     ∈ { ADDRESSABLE,
                           NOT_ADDRESSABLE_BY_CHANNEL,
                           NOT_YET_REAL }
  u_absence_mechanism  ∈ { NOT_REPORTED,
                           REFUSED,
                           WITHHELD_BY_ACTOR,
                           CENSORED_BY_DESIGN,
                           SUPERSEDED_BY_NEWER_EVIDENCE,
                           NOT_INSTRUMENTED,
                           INACCESSIBLE_CHANNEL,
                           NOT_ASSESSED }
  u_visibility         ∈ { BOTH_PARTIES_VISIBLE,
                           PRIVATE_TO_PARTNER }
  u_agreement          ∈ { NO_CONFLICT,
                           CONFLICTED_BY_EVIDENCE,
                           UNDERDETERMINED_BY_CODING,
                           SOURCE_MARKED_DISPUTED }
  u_as_of              # 日期；不参与取值域；UNKNOWN_AS_OF* 的唯一合法落点
}
```

### 2.2 逐值：主张什么 / 不主张什么 / 属于哪一类

三类的定义（本文固定，`D` 的 `MEASUREMENT_SEMANTICS_V0_1.md` §3.2 未给读法）：

- **K = 知识状态**：关于**世界/该 dyad** 的一个事实状态；原则上可被一次新观察改变。
- **R = 记录状态**：关于**本项目/本 lane 的卷宗** 的一个事实状态；只能被一次新检查改变。
- **A = 测量行为属性**：关于**测量动作本身**（工具、codebook、通道、法律许可、观察者位置）的属性；改变它要改变测量设计，不只是多看一次。

| 值 | 它主张什么 | 它**不**主张什么 | 类 | 语料锚 |
|---|---|---|---|---|
| `ADDRESSABLE` | 该命题原则上可被某条通道观测 | 不主张任何通道**已经**观测过它 | K（缺省） | — |
| `NOT_ADDRESSABLE_BY_CHANNEL` | 该命题**不能被该通道**观测 | **不**主张它不可被任何通道观测；**不**主张该构念在此语境无独立意义 | A | `07` §1 `structurally_unobservable`（表第 8 行，逐字「原则上不可被**该通道**观测」） |
| `NOT_YET_REAL` | 该命题在当前时点尚未发生 | 不主张它永远不会发生；**不**主张它不可被寻址 | K（时间性） | `07` §1 `not_yet_real`；`07` §2.3.1 第 3 条逐字「`not_yet_real` 落在 K4 **之外**，需第三条正交轴」 |
| `NOT_REPORTED` | 无人报告，**且**无人以任何方式不报告 | 不主张它是 MCAR/MAR；不主张 `Unknown → prior` 成立 | K | `07` §1 `no_evidence`（MCAR/MAR 行） |
| `REFUSED` | **一次拒答动作发生过**（被问及，主体选「无意见」/拒答） | 不主张主体无意见；不主张可用先验插补（`07` §6 FM-08 逐字：正确类型是「**比先验更宽的集合**」） | A（兼 K） | `07` §1 `refused`（MNAR 行） |
| `WITHHELD_BY_ACTOR` | 一次**主动隐瞒**动作发生过，且机制内生 | 不主张隐瞒的动机；不主张它与 `REFUSED` 机制相同（`07` §1 逐字「与 `refused` 同类，但机制模型不同」） | A（兼 K） | `07` §1 `withheld_by_actor` |
| `CENSORED_BY_DESIGN` | 该单元**按构造**为空（缺失指示是取值的确定函数） | 不主张这是小样本；加大 N 无用（`07` §6 FM-01 逐字） | A | `07` §1 `censored`；`16` §5 的 `CENSORING_BY_DESIGN` |
| `SUPERSEDED_BY_NEWER_EVIDENCE` | 旧值已被更新证据取代 | 不主张原值是错的；不主张新值已确立 | R | `07` §1 `superseded`（由 `history_id` DAG 承载，`CURRENT_ARCHITECTURE.md:241-252` 的 `tau = (history_id, local_time)`） |
| `NOT_INSTRUMENTED` | 现有工具**没有测**它 | 不主张它不可测；不主张测了就会知道（见 `structurally_unobservable` 一列） | A | `07` §1 `unmeasured_by_instrument`；`16` §3.1 `NOT_MAPPED.why` 的「无工具」 |
| `INACCESSIBLE_CHANNEL` | 该通道因**法律/规范**不可用 | 不主张该状态不存在；**不**主张该构念在此语境无独立意义 | A | `15_CASEBANK_EXPANSION.md` §15.6.2 `evidence_channel` 的 `ILLEGAL_OBSERVATION`；`15` §1 候选 N04（`NG v PS` [2020] UKSC 51，婚内秘密摄录）逐字「**非法观察通道需 `evidence_channel=ILLEGAL_OBSERVATION`**」 |
| `NOT_ASSESSED` | 截至 `u_as_of`，**本项目/本 lane 未确定** | 不主张世界上没有答案；不主张它与其他机制同族 | R | `08b` §2.6 的 `g = UNKNOWN`（「丢失、未记录、法务材料中不可判定」）；`12_COMPUTATIONAL_MODELS_ABM.md` 的 `UNVERIFIED_OR_UNKNOWN`；`04` §2.1 的 `STRUCTURAL_UNKNOWN`；`16` §3.4 的 `NOT_TESTED`；`UNKNOWN_AS_OF*` |
| `BOTH_PARTIES_VISIBLE` | 双方都处在可观测范围 | 不主张双方**知道**对方可观测 | K（缺省） | — |
| `PRIVATE_TO_PARTNER` | 该事实存在但**只对 partner 可观测** | **不**主张它不存在；`07` §1 逐字「读者侧无信息 ≠ 人口先验」 | A（观察者位置） | `07` §1 `private_to_partner`（结构性单侧可观测） |
| `NO_CONFLICT` | 没有相反证据 | 不主张有支持证据（`N` 与 `T` 在真值序上不可比，`07` §2.3.1） | K（缺省） | K4 的 `N` |
| `CONFLICTED_BY_EVIDENCE` | 存在**相反证据**，值落在 K4 的 `B` | 不主张任何一方为真；不主张可映射到 `N`（`07` §6 FM-03 逐字「不成立，且不可映射到 `n`」） | K | `07` §1 `disputed`；K4 的 `B` |
| `UNDERDETERMINED_BY_CODING` | 在**当前 codebook** 下无唯一可辩护解 | **不**主张存在相反证据；**不**主张该命题本身欠定（欠定的是编码方案） | A | `13_LLM_SKILL_INTERVIEW_LAYER.md` §3.2 `AMBIGUOUS_NO_UNIQUE_ANSWER`；§10 规则 `R6` 逐字「歧义必须保留为**分支集合**。禁止在无显式裁定时选边」 |
| `SOURCE_MARKED_DISPUTED` | **来源自身**把该主张标为 `alleged` / `disputed` / 未被裁定 | 不主张证据互相冲突；不主张该主张为假 | R | `13` §3.2 `DISPUTED_BY_SOURCE`；`15` §15.6.2 `fact_status ∈ { ADJUDICATED, ADMITTED, ALLEGED, DISPUTED, UNKNOWN }` |

### 2.3 为什么是 factored 而不是 flat（对 `18` `CF-12c` 硬约束 3 的正面回应）

`18` `CF-12c` 硬约束 3 逐字：「朴素并入的总值数必须被当作**失败指标**……若合并后取值数 ≥ **14**，则本构造**失败**」。本构造的算术：

| 口径 | 数值 |
|---|---|
| 最大**单facet** 取值数 | **8**（`u_absence_mechanism`） |
| 全部 facet 取值数之和 | **17**（3 + 8 + 2 + 4） |
| **单一枚举的成员数** | **不存在**（本文不定义单一枚举） |
| 乘积空间的状态数 | 3 × 8 × 2 × 4 = **192**，但**不是枚举**，且大部分格无意义 |

`18` 的失败指标针对的是**朴素并入一个枚举**。本构造不并入：它保留 `07` §4.1 规则 `C4` 已有的正交性声明（逐字「一个坐标可同时是 `private_to_partner` ∧ `not_yet_real`」「tag 复合取**集合并**」），并把 `07` §9.3 里 `tag` 与 `value_class` 的分离**下沉到 facet 之间**。⇒ `07` 的 10 个 tag 在本构造下是 **10 个 facet 值的组合**，不是 10 个平级枚举成员。

**代价（明写）**：`07` §1 的「10 值 tag 表」有单 token 报告 ergonomics；faceted register 没有。本文 §2.4 给出补偿，代价不隐藏。

### 2.4 报告纪律（补偿上一节的代价；**这是 proposal，不是已落地的规则**）

一份报告在声明「某坐标没有值」时，**必须逐 facet 写出取值**，并**显式写出全部落在缺省值的 facet**。缺省值：`u_addressability = ADDRESSABLE`、`u_absence_mechanism = NOT_REPORTED`、`u_visibility = BOTH_PARTIES_VISIBLE`、`u_agreement = NO_CONFLICT`、无 `u_as_of`。

**理由**：`AGENTS.md`「Unknown/missing data must remain explicit」的**镜像要求**——若只写非缺省 facet，则「`ADDRESSABLE / NOT_REPORTED / NO_CONFLICT`」与「`ADDRESSABLE / REFUSED / NO_CONFLICT`」在报告上不可区分，等价于把 `07` §1 表**重新压成一个 `Unknown`**。`07` §1 逐字把这种压平称为「同一种违规的更隐蔽形式」。

### 2.5 本轴**不做**的四件事

1. **不引入代数**。`07` §2.1 `R6`（K4 / RCC 族双序）是 propagation 层的选型，`07` §10 非主张 6 逐字「不主张 K4 / RCC8 / IA / STPA× 中任一个是 LHRM 应选的具体代数」。本文只登记 `CONFLICTED_BY_EVIDENCE` 指向 K4 的 `B`，**不**把 K4 的序搬进 canonical。
2. **不定义 `width` / `evidence_mass` / `coverage` 的度量**。`07` §9.2 `D8` 与 §11-2 逐字：度量与阈值**未冻结**，本轨拒绝给。
3. **不把 `REFUSE` 登记为取值**。`07` §8.3 Round-3 更正：`REFUSE` 是**一等输出**（读出层的合法终态），不是轴 1 的值。它是 readout policy。
4. **不把 `SUPERSEDED_BY_NEWER_EVIDENCE` 从 `history_id` DAG 里搬出来**。`CURRENT_ARCHITECTURE.md:241-252` 已有承载；本值只是它在轴 1 上的**别名视图**。

---

## 3. 轴 2 — construct applicability

### 3.1 逐字字段（SSOT = `MEASUREMENT_SEMANTICS_V0_1.md` §2.2，本文不改写）

```text
applicability            ∈ { APPLICABLE,
                             NOT_APPLICABLE_BY_RULE,
                             APPLICABILITY_UNKNOWN }
applicability_reason     # NOT_APPLICABLE_BY_RULE 时必填、非空
applicability_provenance # 指向支配该构念的 Boundary/Constraint 落点或规则的锚
```

| 值 | 它主张什么 | 它**不**主张什么 |
|---|---|---|
| `APPLICABLE` | 该构念在此 dyad / 语境中**有**独立意义 | **不**主张我们已知其取值；**不**主张它已被测过；与 `uncertainty` 宽窄无关（`MEASUREMENT_SEMANTICS` §2.3） |
| `NOT_APPLICABLE_BY_RULE` | 存在一条**已命名**的 boundary / agreement / 规则，该规则在此语境支配此构念的取值 | **不**主张取值为 `0`；**不**主张等于 `Unknown`；**不**进入坐标值域；值域内**不**出现 `NA`（`MEASUREMENT_SEMANTICS` §2.4 五条禁止） |
| `APPLICABILITY_UNKNOWN` | 尚未判定 | **不是**「不适用」的委婉说法；**不是**默认值（`MEASUREMENT_SEMANTICS` §2.2） |

### 3.2 规则族目录（`BY_RULE` 的**唯一**合法授权来源）

`NOT_APPLICABLE_BY_RULE` 要求 `applicability_provenance` 指向一条**已登记**的规则。以下是语料里出现过的全部候选授权形式，逐族给出状态。**本表不主张任何一族的任何一次具体适用。**

| 规则族 | 授权形式 | 语料锚 | 状态 | 备注 |
|---|---|---|---|---|
| **R-1 已命名 boundary / agreement 规则** | 一条具名 `BoundaryRule_(A,B,domain)` 或等价规则在语境中支配该构念 | `PARAMETER_CONVERGENCE_V0_1.md` §6 `P5`（`KEEP as Constraint/Agreement`）；canonical 工作例 `CURRENT_ARCHITECTURE.md:190`「『订婚前不发生性行为』更接近 Agent boundary / constraint，而不是『性欲为零』」 | **机制齐备** | `11` §3.1 逐字指出该例的三个可复用环节：(i) `constraint` 是合法值类，(ii) 边界/规则类事实归 `Constraint/Agreement` 落点，(iii) 不得写成「欲望为零」 |
| **R-2 `HD-ST-1` dyad-class 的具名范围裁定** | 一条已登记的裁定把某构念排除在某 `dyad_class` 之外 | `VALIDATION_GATES_V0_2.md` §6.4 `HD-ST-1` | **规则本身尚不存在** | **今天没有任何一格**能被 R-2 授权。这直接决定 `11` §2 的 24 个 `NA` 格必须映射成 `APPLICABILITY_UNKNOWN`（见 §6 L-3） |
| **R-3 构念定义的前置条件未满足** | 构念定义内建了某条前提，该前提在此语境不成立 | `11` §6 第 2 条（`Trust` 定义为「愿意把某类脆弱性暴露给 j」，**内建披露史前提**；零披露史 dyad 上同一量表测到的是别的东西） | **`HOLD_FOR_EVIDENCE`**（`G-C11`） | 这是语料里**唯一一条以「构念无独立意义」为形式**的论证，但它被判为**定义欠定**而非适用性（见 §6 L-15） |
| **R-4 抽样框不含该情境** | 该情境未进入任何已审计的抽样框 | `16` §3.1 `NOT_MAPPED.why` 的「抽样框不含该情境」；`X-10` 两层记账 | **不是授权** | **裁决 §C item 6 逐字：「Search failure/access restriction is not ontology evidence」**。`X-14` 同理。⇒ 最多支持 `APPLICABILITY_UNKNOWN` + 记录理由，**不**支持 `NOT_APPLICABLE_BY_RULE`。**与 `18` `CF-12c` 的映射有分歧，见 §7.3** |
| **R-5 构念本身未定义** | 该变量所指构念在项目内没有定义 | `16` §3.1 `NOT_MAPPED.why` 的「构念本身未定义」 | **不属本轴** | 这是**定义缺口**，既不是适用性也不是对世界的知识不确定。见 §6 L-6 |
| **R-6 工具的 directional slot 结构为空** | 某变量只能测 `i` 的一般倾向，`target slot` 结构上为空 | `16` §3.2 `directionality_class = AGENT_LEVEL` / `TARGET_LEVEL`；`16` §3.2 逐字「R03 F1 记录：ECR / … **全部测 `i` 的一般倾向或对一般他者的态度**，target slot 结构上为空」 | **不是授权** | 这是**工具的**性质，不是构念的。⇒ 落在 `16` 的 `directionality_class` 字段，见 §6 L-6 |

### 3.3 一条必须显式记录的**非**适用性候选

`08b` §2.5 的 `k = { +, −, ?, ⊘ }` 中，`⊘` 逐字释义为「**没有这个问题**」。`08b` §2.11.3 逐字已判定：

> `⊘`（"没有这个问题"）**不**等于 `NOT_APPLICABLE_BY_RULE`。`⊘` 是**一次提问之后得到的回答**（主体说「这不是个问题」）；`NOT_APPLICABLE_BY_RULE` 是**规则元数据**（本 dyad 语境下该构念无独立语义）。两者正交。

本轨**接受并沿用**该判定，并把它记为一条**类型事实**：`⊘` 是**轴 1 之外的肯定回答**，不是「无值」。见 §6 L-12。

---

## 4. 词表清册（转换表的**源**列）

`18` `CF-12` 逐字给出 5 个 lane（A=R07 / B=R11 / C=R13 / D=R15 / E=R16），`CF-12b` 补第 6 套。以下是**本轨独立枚举**的完整清册，共 **12 套**。清册的「专用于无值？」一列是本轨新增的分类，`18` 未做此区分，而它决定了每套的转换是否**类型正确**。

| # | 词表 | 源位置 | 粒度 | **专用于「无值」？** | 无值成员 / 总成员 |
|---|---|---|---|---|---|
| **V1** | `Unknown.tag` 10 值 | `07` §1 表 / §9.3 | **坐标** | **是**（10 / 10） | 10 / 10 |
| **V2** | `k` / `g` / `m` / `Pol` / `Rel` / `src` 的 `UNKNOWN` 与 `?` 成员 + §2.11 派生类 | `08b` §2.5–2.11 | **信念记录**（坐标的信念侧） | **部分**（`⊘` 与 `+` / `−` 是肯定值） | 1 / 4（`k`）+ 1 / 6（`g`）+ 0 / 4（`m`）+ 1 / 3（`Pol`）+ 1 / 4（`Rel`）+ 1 / 2（`src`） |
| **V3** | §1 verdict 码 5 值 + §3.1 值域扩充提案 3 值 | `11` §1 / §3.1 | **构念 × dyad-class 格**（24 × 9 = 216 格） | **部分**（`MEANING_PRESERVED` / `READOUT_DIFFERS` 是肯定判定） | 2 / 5 + 2 / 3 |
| **V4** | `AMBIGUOUS_NO_UNIQUE_ANSWER` / `UNKNOWN_EVIDENCE` / `DISPUTED_BY_SOURCE` | `13` §3.2 | **文本单元的抽取状态** | **部分**（`UNKNOWN_EVIDENCE` 是；另两项不是） | 1 / 3 |
| **V5** | `fact_status` / `temporal_basis` / `evidence_channel` / 7 值 verdict / 9 类诊断 | `15` §15.6.2 / §15.6.3 | **原子文本单元** | **否**（4 张表里只有 4 个成员是无值） | `fact_status` 1/5 · `temporal_basis` 1/5 · `evidence_channel` 1/6 · verdict 2/7 · 诊断 0/9 |
| **V6** | `mapping_status` 6 值 / `directionality_class` 6 值 / `uncertainty` 5 字段 | `16` §3.1 / §3.2 / §3.4 | **数据集变量 → 候选 LHRM 槽位** | **否** | `mapping_status` 2/6 · `directionality_class` 2/6 · `uncertainty` 1/5 |
| **V7** | `UNKNOWN_AS_OF*` | 跨 lane，非按 lane 组织 | **记账标记，跨层** | **是**（但**不总是坐标**） | 1 token 形式 / 3 种变体 |
| **V8** | canonical 事实状态 5 值 | `CURRENT_ARCHITECTURE.md:315` `adjudicated \| admitted \| alleged \| disputed \| unknown` | **法院文书内的单条主张** | **否** | 1 / 5 |
| **V9** | `structural_verdict` 5 值 / `access_rights_axis` 5 值 | `04` §2.1 / §2.2 | **数据集** | **部分** | 1 / 5 + 1 / 5 |
| **V10** | `UNVERIFIED_OR_UNKNOWN` / 对照表中的 `UNKNOWN` | `12` §2 / §5 | **外部工具 / 框架的元数据** | **是**（`UNVERIFIED_OR_UNKNOWN`） | 1 / 1 |
| **V11** | `MAPPING_FAILURE` 可达性论证（F1）与 catch-all 盘点（F4） | `17` §F1 / §F4 | **schema 级的类型论证** | **否**（不是取值） | 0 |
| **V12** | `missingness_mechanism ∈ { MCAR_assumed, MAR_assumed, MNAR_sensitivity_done, UNKNOWN }` | `16` §3.4（归因 R05 `I13`） | **一次分析的承诺** | **部分** | 1 / 4 |

**清册本身的两条发现（本轨新增）**：

1. **12 套里只有 2 套（V1 / V7）是专用于「无值」的词表。** 其余 10 套是**混合词表**——同一个枚举里既有肯定值又有「无值」成员。把混合词表整体当作「无值词表」转换，必然丢掉肯定成员的语义。`18` `CF-12` 未做此区分。
2. **V7 是唯一不按 lane 组织的词表**，这正是 `18` `CF-12b` 逐字说的「**任何按 lane 列举的清单都必然先漏掉它，因为它不是任何一个 lane 的「设计」**」。

### 4.1 V7 的可复算计数（`18` `CF-12b` 逐格重算 + 本轨对**修复后**语料的重算）

| 口径 | `UNKNOWN_AS_OF` 出现次数 | 出现文件数 |
|---|---|---|
| `18` `CF-12b` 自报（PR #31 原始语料） | **48** | **11** |
| 本轨在**修复后**语料上的重算（`04` 用 `R3-A3b` 修好版，其余修复文件按 sibling worktree 取） | **94** | **13** |

修复后语料的逐文件计数（可复算口径：逐 token、大小写敏感、`docs/research/overnight-2026-09-27/**`）：

| 文件 | `UNKNOWN_AS_OF` |
|---|---|
| `04_DATASET_LANDSCAPE.md`（`R3-A3b` 修好版） | **29** |
| `18_CROSS_LANE_CONFLICT_AUDIT.md`（`R3-A4b` 修好版） | **22** |
| `05_IDENTIFICATION_AND_STATISTICS.md` | 14 |
| `A01_EVIDENCE_QUALITY_AUDIT.md` | 11 |
| `12_COMPUTATIONAL_MODELS_ABM.md` | 5 |
| `16_EMPIRICAL_VALIDATION_PROTOCOL.md` | 4 |
| `01_CURRENTNESS_AND_GAP_MAP.md` | 2 |
| `08b_BELIEF_DECEPTION_KNOWLEDGE.md` | 2 |
| `00_CHILD_CONTRACT.md` / `07` / `10` / `13` / `A03` | 各 1 |
| 其余 12 份文件 | 0 |

**本轨的记账观察**：`R3-A3b` 对 `04` 的修复把该文件内的 `UNKNOWN_AS_OF` 从 **9 提升到 29**（+20），`R3-A4b` 对 `18` 的修复把它从 **0 提升到 22**。⇒ **修复动作本身增加了这套标记的使用量。** 这是对 `H-F33`（`UNKNOWN_AS_OF` 是全语料使用最广的一套）方向的**加强**，不是反驳；`K-C7` 的独立来源数不变。

**`X-14` 口径**：以上只能说明「在本次的 token 口径与目录范围内」。本轨**不**主张它是项目内唯一被最广泛使用的记账标记。

---

## 5. 转换表

### 5.1 逐 token 转换

列含义：**prior token → (轴, 新值) → 得到什么 / 失去什么**。「类型」四档：`INJECTIVE`（可逆，无损）· `LOSSY`（信息丢失）· `TYPE-MISMATCH`（粒度/类型不同，映射需附加条件）· `OUT-OF-SCOPE`（不属于这两轴，**不得**转换）。

#### V1 `07` 的 10 值 tag

| prior token | 轴 / 新值 | 得到 | 失去 | 类型 |
|---|---|---|---|---|
| `no_evidence` | 1 / `NOT_REPORTED` | 与 `refused` 分离 ⇒ `07` §6 FM-08 的 MNAR 禁令可被类型化执行 | 「名义上成立（= 先验）」这条**代数便利性**的记录位 | `LOSSY`（见 L-4） |
| `refused` | 1 / `REFUSED` | 拒答动作可与「无人报告」分开 ⇒ 不再被静默插补 | — | `INJECTIVE` |
| `private_to_partner` | 1 / `PRIVATE_TO_PARTNER` | 与 `NOT_REPORTED` 组合表达「只对一方可见且双方都未报」 | — | `INJECTIVE` |
| `withheld_by_actor` | 1 / `WITHHELD_BY_ACTOR` | 主动隐瞒与拒答分离 | — | `INJECTIVE` |
| `disputed`（**缺失机制**义） | 1 / `CONFLICTED_BY_EVIDENCE` | 与 canonical 同名 token 分离（见 §5.3） | — | `INJECTIVE`（**加命名空间前缀后**） |
| `censored` | 1 / `CENSORED_BY_DESIGN` | 与 `NOT_INSTRUMENTED` 分离 | — | `INJECTIVE` |
| `structurally_unobservable` | 1 / `NOT_ADDRESSABLE_BY_CHANNEL` | **通道相对性**被写进值名 ⇒ 不可被读成「不可知」 | — | `INJECTIVE` |
| `not_yet_real` | 1 / `NOT_YET_REAL` | 「落在 K4 之外」这条要求被显式承认 | `07` §1 该行把它标为「不适用」——**本轨改判：它适用，只是未发生** | `LOSSY`（见 L-9） |
| `superseded` | 1 / `SUPERSEDED_BY_NEWER_EVIDENCE` | 值名指向 `history_id` DAG | — | `INJECTIVE` |
| `unmeasured_by_instrument` | 1 / `NOT_INSTRUMENTED` | 与 `NOT_ASSESSED` 分离（**工具层 vs 记录层**） | — | `INJECTIVE` |
| `value_class`（`⊑_a` / `⊑_t` 双序） | — | — | — | `OUT-OF-SCOPE`（**不转换**：K4/RCC 代数选型是 `07` §10 非主张 6 明确不主张的；见 §2.5 第 1 条） |
| `prior_set` / `evidence_mass` | — | — | — | `OUT-OF-SCOPE`（`evidence_mass` 的**度量**未冻结，`07` §9.2 `D8`） |
| `role_lens`（原 `reporter_role`） | — | — | — | `OUT-OF-SCOPE`（`07` §1.1 已改名为 `role_lens` 以免与 canonical `Role` 混淆） |

#### V2 `08b` 的 `UNKNOWN` / `?` 成员与派生类

| prior token | 轴 / 新值 | 得到 | 失去 | 类型 |
|---|---|---|---|---|
| `k = ?`（悬置） | 1 / `ADDRESSABLE` + `NOT_ASSESSED`（`u_as_of` 必填） | 悬置**需要一次裁决**这件事被记成「未评估 + 日期」 | 「`?` 是**主体**的悬置」这层**主体归属**（`k` 是 `ι` 的立场，不是观察者的记录状态） | `LOSSY`（见 L-10） |
| `k = ⊘` | — | — | — | `OUT-OF-SCOPE`（**肯定回答**；`08b` §2.11.3 已判定；见 L-12） |
| `g = UNKNOWN` | 1 / `NOT_ASSESSED` | `g` 层的无值与 `k` 层的无值分离 | — | `INJECTIVE` |
| `g = ASSUMED` | 1 / `ADDRESSABLE` + `NOT_REPORTED`（无证据支持） | 「假定」被记成**无证据的 `NOT_REPORTED`**，而不是第四个 `g` 值 | `g` 的**依据类别**（前提 vs 推断）——但那在 `g` 自己的值域里 | `LOSSY`（轻微；见 L-11） |
| `Pol = UNKNOWN` / `Rel = UNKNOWN` / `src = UNKNOWN` | 1 / `NOT_ASSESSED` | 三个字段的无值统一 | 各字段的**字段特定**无值语义（例如 `src = UNKNOWN` 意味着「不可辨是谁说的」） | `INJECTIVE`（逐字段保留字段名；语义差异见 L-18） |
| `Divergent(p)` | — | — | — | `OUT-OF-SCOPE`（**派生关系**，两侧立场 `+` / `−` 都是肯定值；见 L-13） |
| `ASYMMETRIC(p)` | — | — | — | `OUT-OF-SCOPE`（同上） |
| `SHARED_NOTED(p)` | — | — | — | `OUT-OF-SCOPE`（同上；两侧都是 `?`，但这是**派生关系**不是**状态**） |
| `BelievesBoth(p)` / `Overclaim` / `Meta_Unrealized` / `NonDisclosure` / `Unreliable` | — | — | — | `OUT-OF-SCOPE`（全部是**派生关系**，`08b` §2.11 逐字标注「**永不存储**」） |

#### V3 `11` 的 verdict 码与值域扩充提案

| prior token | 轴 / 新值 | 得到 | 失去 | 类型 |
|---|---|---|---|---|
| `NOT_APPLICABLE`（216 格中 **24 格**） | 2 / **`APPLICABILITY_UNKNOWN`** + reason | 24 格从**无支撑的否定**变成 24 条**有理由的未知**（`applicability_reason` 必填） | `11` 的**假设内容**（「该构念在此 dyad-class 上结构性不适用」）**不再是取值**，只留在 reason 自由文本里 | `LOSSY`（见 L-3） |
| `structurally_not_applicable`（§3.1 提案值） | 2 / `NOT_APPLICABLE_BY_RULE` | 与轴 1 的 `NOT_ADDRESSABLE_BY_CHANNEL` 强制分离（`18` `CF-12c` 已指出这条） | — | `INJECTIVE` |
| `scope_unknown`（§3.1 提案值） | 2 / `APPLICABILITY_UNKNOWN` | 与轴 1 的 `NOT_INSTRUMENTED` 强制分离（dyad-type 层 vs 工具层） | — | `INJECTIVE` |
| `MEANING_PRESERVED` / `READOUT_DIFFERS` | — | — | — | `OUT-OF-SCOPE`（**肯定**判定，不是无值） |
| `MEANING_SHIFTS` | — | — | — | `OUT-OF-SCOPE`（语义改变，既非无值也非适用性） |
| `UNKNOWN`（`Trust` × S/K/C/W/A **5 格**） | **无合法目标** | — | `11` §1 逐字自陈：「**§1 码表缺一个表示『定义欠定』的码**」 | **`LOSSY`（无目标）**，见 L-15 |
| `§3.3 consent_status ∈ {consensual, imposed, unknown}` | 1（仅 `unknown` 成员）/ `NOT_ASSESSED` | 明确「**`consent_status` 是值，不是适用性元数据**」（`11` §3.3 逐字） | — | `INJECTIVE` |

#### V4 `13` §3.2

| prior token | 轴 / 新值 | 得到 | 失去 | 类型 |
|---|---|---|---|---|
| `UNKNOWN_EVIDENCE` | 1 / `NOT_ASSESSED` | — | 「证据本身缺失；不给分支也不做归一」中的**「不给分支」**这条处置规则（它是规则不是值） | `INJECTIVE`（规则随 `13` §10 `R6` 保留在原处） |
| `AMBIGUOUS_NO_UNIQUE_ANSWER` | 1 / **`UNDERDETERMINED_BY_CODING`** | 与 `CONFLICTED_BY_EVIDENCE` 分离 | **与 `18` `CF-12c` 的 `→ disputed` 映射不同**；`disputed` 侧多了一个**不存在的相反证据** | `LOSSY`（见 L-1）。**本轨与 `18` 有分歧，见 §7.2** |
| `DISPUTED_BY_SOURCE` | 1 / `SOURCE_MARKED_DISPUTED` | 与 `CONFLICTED_BY_EVIDENCE` 分离 | — | `INJECTIVE` |

#### V5 `15` §15.6.2 / §15.6.3（**混合词表**）

| prior token | 轴 / 新值 | 得到 | 失去 | 类型 |
|---|---|---|---|---|
| `fact_status = UNKNOWN` | 1 / `NOT_ASSESSED` | — | 该 5 值表的**其余 4 个肯定成员**（`ADJUDICATED` / `ADMITTED` / `ALLEGED` / `DISPUTED`）**不是无值**，把它们一起丢掉会丢掉「法院已裁定」与「我们不知道」的**权威性差别** | `LOSSY`（见 L-8） |
| `fact_status = DISPUTED` | 1 / `SOURCE_MARKED_DISPUTED` | 与 `07` 的 `disputed` / `08b` 的 `Divergent` 分离 | — | `INJECTIVE`（**加命名空间前缀后**，见 §5.3） |
| `temporal_basis = UNKNOWN` | 1 / `NOT_ASSESSED` | — | 时间基的**具体未知方向**（是 `EVENT_TIME` 未知还是 `RECORDING_TIME` 未知） | `LOSSY`（轻微；见 L-18） |
| `evidence_channel = ABSENT` | 1 / `NOT_REPORTED` | — | 「通道不存在」vs「该通道上没人报」的区分 | `LOSSY`（轻微；见 L-18） |
| `evidence_channel = ILLEGAL_OBSERVATION` | 1 / **`INACCESSIBLE_CHANNEL`** | 本轨由此**新增**一个轴 1 值（语料中原本没有对应 token） | — | `INJECTIVE`（**本轨新增映射**；见 L-14） |
| verdict `UNKNOWN`（= 材料不足） | 1 / `NOT_ASSESSED` | — | `15` 的粒度是**原子文本单元**，`NOT_ASSESSED` 的粒度是**坐标**；且 `材料不足` 包含 MNAR 拒答，直接映到 `NOT_ASSESSED` 会把 MNAR 静默重写为「无人报告」 | `LOSSY`（见 L-2） |
| verdict `MAPPING_FAILURE` + 9 类诊断 | **轴外**，引用 `C` 的 `mapping_outcome` + `diagnosis` | `MAPPING_FAILURE` 的可达性与持久性由 `C` §3.4 流水线保证 | `15` 的 9 类诊断与 `C` 的 8 类**不对齐**（见 §7.4） | `TYPE-MISMATCH`（见 L-6） |
| verdict `NARRATIVE_ONLY` / `IRRELEVANT` | **轴外**，→ `C` 的 `NON_RELATION_RELEVANT_EXIT`（**条件式**） | `C` §3.2 的三条条件使「不相关」与「不可表示」不再混同 | `15` 的无条件出口语义 | `TYPE-MISMATCH` |
| verdict `DIRECT` / `PARTIAL` / `MULTI` | **轴外**，→ `DIRECT_MAPPING` / `PARTIAL_MAPPING` / `MULTI_MAPPING` | 统一到 `C` 的 SSOT | — | `INJECTIVE` |

#### V6 `16` §3.1 / §3.2 / §3.4

| prior token | 轴 / 新值 | 得到 | 失去 | 类型 |
|---|---|---|---|---|
| `mapping_status` 的 4 个**肯定**等级（`DIRECT_ITEM` / `DERIVED_COMPOSITE` / `BEHAVIORAL_PROXY` / `COVARIATE_ONLY`） | — | — | — | `OUT-OF-SCOPE`（**不是无值**；但它们是**映射等级**，与 `C` 的 `mapping_outcome` 粒度不同，见 L-6） |
| `mapping_status = NOT_MAPPED` + `why`「无工具」 | 1 / `NOT_INSTRUMENTED` | 五项 `why` 拆到不同轴 | `why` **这个维度本身**（记录哪一项 `why`） | `LOSSY`（见 L-5） |
| `mapping_status = NOT_MAPPED` + `why`「抽样框不含该情境」 | 2 / `APPLICABILITY_UNKNOWN`（**不是** `NOT_APPLICABLE_BY_RULE`） | 裁决 §C item 6 被强制执行 | `18` `CF-12c` 未区分 `APPLICABILITY_UNKNOWN` 与 `NOT_APPLICABLE_BY_RULE` 地把该项落轴 2 | `LOSSY`（轻微；见 §7.3） |
| `mapping_status = NOT_MAPPED` + `why`「构念在数据中不存在」 | 2 / `APPLICABILITY_UNKNOWN` | — | 「不存在于**该数据**」≠「在此语境无独立意义」 | `LOSSY`（轻微） |
| `mapping_status = NOT_MAPPED` + `why`「构念本身未定义」 | **无合法目标** | — | 定义缺口无处落 | `LOSSY`（无目标，见 L-6） |
| `mapping_status = NOT_MAPPED` + `why`「只有 pair 级而无方向」 | **轴外** → `16` 的 `directionality_class = PAIR_LEVEL` | — | — | `OUT-OF-SCOPE` |
| `mapping_status = CONFLICTED` | **必须一分为二** | 拆成「≥2 个同样可辩护的候选构念」（→ mapping 侧不可消解的 `MULTI_MAPPING`）与「该构念的实证文献互相矛盾」（→ **构念身份**冲突，**不是** `CONFLICTED_BY_EVIDENCE`，后者是**该 dyad 的**证据冲突） | `CONFLICTED` 的单一标签丢失 | `LOSSY`（见 L-16） |
| `directionality_class = UNDETERMINED` / `NON_SEPARABLE` | **轴外**，保持 `16` 的独立正交字段 | `16` §3.2 的「第二个正交必需字段」得以保留 | 若按 `18` `CF-12c` 并进 mapping 轴，则**丢失**「映射成功但不支持方向性主张」这条共存态 | `LOSSY`（见 L-6） |
| `uncertainty.estimated_uncertainty = UNKNOWN` | 1 / `NOT_ASSESSED` | — | — | `INJECTIVE` |
| `uncertainty.missingness_mechanism = UNKNOWN` | 1 / `NOT_ASSESSED` | — | — | `INJECTIVE` |
| `uncertainty.invariance_level_tested = NOT_TESTED` | 1 / `NOT_ASSESSED` | — | `NOT_TESTED` 是一条**独立轴**（不变性层级），其 6 个肯定层级不是无值 | `LOSSY`（轻微） |
| `uncertainty.missingness_mechanism` 的 3 个**肯定**承诺（`MCAR_assumed` / `MAR_assumed` / `MNAR_sensitivity_done`） | — | — | — | `OUT-OF-SCOPE`（**分析侧承诺**，与 `u_absence_mechanism` 的**世界侧机制**是两个字段；见 L-19） |

#### V7 `UNKNOWN_AS_OF*`

| prior token | 轴 / 新值 | 得到 | 失去 | 类型 |
|---|---|---|---|---|
| `UNKNOWN_AS_OF<date>`（主语是**坐标**时） | 1 / `NOT_ASSESSED` + `u_as_of = <date>` | 时间性成分被保住（`18` `CF-12b` 逐字指认这是它比 `no_evidence` 多出的两个正交成分之一） | — | `INJECTIVE`（**加 `u_as_of` 字段后**） |
| `DOI_UNKNOWN_AS_OF_2026-09-27`（主语是**文献标识**时） | — | — | — | `OUT-OF-SCOPE`（`04` §1 逐字把来源同意问题与 dataset 内容不足分成两轴；`A04_CITATION_PROVENANCE_AUDIT.md` 是书目轴） |
| `UNKNOWN_AS_OF<date>`（主语是**数据集的 wave 可得性**，如 `04` 的 `Wave 2+ UNKNOWN_AS_OF`） | — | — | — | `OUT-OF-SCOPE`（V9 的 `structural_verdict` / `access_rights_axis` 两轴之一） |
| `UNKNOWN_AS_OF<date>`（主语是**外部框架/工具的存在性**，如 `12` 的 `UNKNOWN` 对照表） | 1 / `NOT_ASSESSED`（**该元数据坐标**） | — | 该 token **不区分**这四种主语；转换时必须逐条判定主语 | `TYPE-MISMATCH`（见 L-20，**本轨最大的单条信息丢失**） |

#### V8 canonical 事实状态 5 值

| prior token | 轴 / 新值 | 得到 | 失去 | 类型 |
|---|---|---|---|---|
| `unknown`（`CURRENT_ARCHITECTURE.md:315`） | 1 / `NOT_ASSESSED` | — | 4 个肯定成员的权威性语义 | `LOSSY`（同 L-8） |
| `disputed`（`CURRENT_ARCHITECTURE.md:315`） | 1 / `SOURCE_MARKED_DISPUTED` | 三处同名 token 分离 | — | `INJECTIVE`（加前缀后） |
| `adjudicated` / `admitted` / `alleged` | — | — | — | `OUT-OF-SCOPE`（肯定事实状态） |

#### V9 `04` 的两条数据集轴

| prior token | 轴 / 新值 | 得到 | 失去 | 类型 |
|---|---|---|---|---|
| `STRUCTURAL_UNKNOWN` | 1 / `NOT_ASSESSED`（主语 = 该数据集的结构属性） | — | 「哪个数据集、哪个结构属性」被压成单值 | `TYPE-MISMATCH` |
| `ACCESS_UNKNOWN` | — | — | — | `OUT-OF-SCOPE`（**权利/访问轴**，`R3-A3b` 逐字「**两轴不可互相推导**」） |
| 其余 8 个 `STRUCTURAL_*` / `ACCESS_*` | — | — | — | `OUT-OF-SCOPE`（肯定判定） |

#### V10 `12`

| prior token | 轴 / 新值 | 得到 | 失去 | 类型 |
|---|---|---|---|---|
| `UNVERIFIED_OR_UNKNOWN` | 1 / `NOT_ASSESSED` | 与 `NOT_INSTRUMENTED` 分离 | 「未验证」与「未知」被合并在一枚 token 里 ⇒ **本轨一分为二**：未验证 = `NOT_ASSESSED`（R 类），未知 = `NOT_ASSESSED`（R 类）但理由不同 | `LOSSY`（轻微） |
| 对照表中的 `UNKNOWN` | 1 / `NOT_ASSESSED` | — | 对照表单元格的**被比较对象**（框架 / state representation / transition rules / …） | `TYPE-MISMATCH` |

#### V11 `17`

| prior 项 | 处置 | 类型 |
|---|---|---|
| F1「`MAPPING_FAILURE` 在设计上不可达」 | **不是取值**。它是**轴外**的类型可达性论证。其 Round-3 结论（缺陷保留、论证换掉、catch-all 由 4 降为 3）已被 `C` §3.1 逐字吸收 ⇒ **本轨不转换，只在 §1.2 引用** | `OUT-OF-SCOPE` |
| F4「catch-all 归因谱系缺 `redundancy` 一类」 | 同上，已被 `C` §3.2 的 `redundancy hole` 吸收 | `OUT-OF-SCOPE` |

#### V12 `missingness_mechanism`

| prior token | 轴 / 新值 | 得到 | 失去 | 类型 |
|---|---|---|---|---|
| `MCAR_assumed` / `MAR_assumed` / `MNAR_sensitivity_done` | — | — | — | `OUT-OF-SCOPE`（**分析侧承诺**，必须与 `u_absence_mechanism` **分列**；见 L-19） |
| `UNKNOWN` | 1 / `NOT_ASSESSED` | — | — | `INJECTIVE` |

### 5.2 mapping 侧（轴外）的转换 —— 交 `C` 复核

| 来源 | → `VALIDATION_GATES_V0_2` | 类型 | 备注 |
|---|---|---|---|
| `15` verdict `DIRECT` | `DIRECT_MAPPING` | `INJECTIVE` | 词面沿用 |
| `15` verdict `PARTIAL` | `PARTIAL_MAPPING` | `INJECTIVE` | 词面沿用 §15 Gate A 第 4 步 |
| `15` verdict `MULTI` | `MULTI_MAPPING` | `INJECTIVE` | `C` §3.3 规定它**不是**自动失败 |
| `15` verdict `MAPPING_FAILURE` | `MAPPING_FAILURE` | `INJECTIVE` | 词面沿用 |
| `15` verdict `NARRATIVE_ONLY` / `IRRELEVANT` | `NON_RELATION_RELEVANT_EXIT`（**条件式**，须过 `C` §3.2 三条） | `LOSSY` | `C` 的词面被 §3.2 (b) 收紧；`15` 的无条件出口语义不再成立 |
| `15` 9 类诊断 vs `C` 8 类 | 见 §7.4 | `TYPE-MISMATCH` | `15` 多 `DATA_INSUFFICIENT`；`C` 多 `redundancy hole` |
| `16` `mapping_status` 4 个肯定等级 | **无对应值** | `TYPE-MISMATCH` | `C` 的 `mapping_outcome` 判「是否被正确表示」，`16` 判「映射的**级别**」。二者正交，**不应合并**；见 L-7 |

### 5.3 三处同名不同义（`H-F15` / `E-C23` / `A3d` CR-1 的处置）

`07` §1.1 / `08b` §2.11.2 / `18` `CF-12c` 逐条点名。**本轨的处置是分离 + 命名空间前缀，不是改名**（改名会破坏 `07` / `08b` / `15` / canonical 之间的既有引用）。

| token | 出处 1 | 出处 2 | 出处 3 | 本轨落点 |
|---|---|---|---|---|
| `disputed` | `07` §1 tag：**缺失机制**（存在相反证据 ⇒ K4 `B`） | `08b` §2.11.2 / §4.3：**派生关系**（`Divergent` 落点，`k_ι = +`、`k_ι' = −`） | `CURRENT_ARCHITECTURE.md:315` + `15` §15.6.2：**事实状态**（`adjudicated\|admitted\|alleged\|disputed\|unknown`） | 1 / `CONFLICTED_BY_EVIDENCE`（`ns=07`）· `OUT-OF-SCOPE`（派生关系）· 1 / `SOURCE_MARKED_DISPUTED`（`ns=fact_status`） |
| `Divergent` | `08b` §2.11：**主体立场对立** | 与上两处同名不同义 | — | `OUT-OF-SCOPE`（**不是无值**；两侧立场都是肯定值） |
| `reporter_role` | `07` §1.1：**记录层字段名** | canonical `Role`：**query / evaluation lens**，不是世界状态（`CURRENT_ARCHITECTURE.md:96`；`AGENTS.md` 当前架构方向第 3 条） | — | `OUT-OF-SCOPE`；`07` §9.3 已 `SUPERSEDED_BY_REPAIR` 改名 `role_lens` |

**具体不可再表达的案例**（`08b` §2.11.2 逐字）：法院文书里被指称的「他出轨」是 `alleged`（`fact_status` 域）；夫妻双方对「他出轨」的**信念**才是 `Divergent`（`08b` 的 `k` 域）。**同一件事在两层上是两个不同轴上的不同值**，任何把它们并成一个 token 的表示都无法读出「事实未裁定但双方信念对立」这一状态。

---

## 6. 有损映射与信息丢失案例

### 6.1 计数（可复算口径：§5.1 的 67 个 5 列表格行 + V11 的 2 个 3 列表格行 = **69**）

| 类型 | 行数 |
|---|---|
| `INJECTIVE` | **23** |
| `LOSSY` | **20** |
| `TYPE-MISMATCH` | **5** |
| `OUT-OF-SCOPE` | **21** |
| **合计** | **69** |

**有损（非单射）映射 = `LOSSY` 20 条 + `TYPE-MISMATCH` 5 条 = 25 条。** 另有 **3 条**映射**没有合法目标值**（三条都归 §7.5 的 schema 缺口，不计入上表）：`NOT_MAPPED.why`「构念本身未定义」（L-6 第 3 点）· `11` 的 `Trust × S/K/C/W/A` 5 格「定义欠定」（L-15）· `16` `CONFLICTED` 的「构念身份冲突」分支（L-16）。

**`§6.2` 逐条案例数 = 20**（`L-1` … `L-20`），其中 **`LOSSY` 类 17 条**（`L-1`–`L-5` · `L-8`–`L-11` · `L-14`–`L-20`）、**`TYPE-MISMATCH` 类 1 条**（`L-7`）、**「无合法目标」类 2 条**（`L-6` · `L-15`）、**「`OUT-OF-SCOPE` 反向记录」类 3 条**（`L-12` · `L-13` · `L-17` —— 记录的是**不应**转换的项）。**`L-9` 与 `L-4` 是「本轨改判 / 有意接受丢失」，各自在标题中显式标注。**

### 6.2 逐条信息丢失案例

每条给出：映射 · 为什么有损 · **具体不能再表达的案例** · 补偿手段。

---

**L-1 `13` `AMBIGUOUS_NO_UNIQUE_ANSWER` → 轴 1 `UNDERDETERMINED_BY_CODING`（本轨与 `18` `CF-12c` 分歧）**

`18` `CF-12c` 逐行写 `R13 AMBIGUOUS_NO_UNIQUE_ANSWER → disputed（并保留"禁止在无显式裁定时选边"这条规则）`，理由是「R13 的 `support_set` 分支结构**不并入任何一轴**，它是**推理规则**不是值」。该理由只覆盖了**规则**那一半，没覆盖**值**那一半。

- **为什么有损**：把「当前 codebook 下无唯一解」映到 `CONFLICTED_BY_EVIDENCE` 会**引入一个不存在的相反证据**。`13` §3.2 逐字「这三个状态**互不等价**」；`13` §3.2 引 Nakamura et al. 逐字「when the codebook admits multiple defensible classifications or texts do not provide sufficient information or contexts, a unique target annotation may not exist at all」——**这里没有任何相反证据，只有一个欠定的编码方案**。
- **具体不能再表达的案例**：一个 LLM 把「他说他爱她」标成 `BELIEF_STATE` 或 `ACTION_EVENT` 都说得通，**因为 schema 没有规定 speech act 与 belief report 的优先关系**。此时 `CONFLICTED_BY_EVIDENCE` 是**假**的（只有一条来源、没有相反证据），而 `UNDERDETERMINED_BY_CODING` 是真的。在 `18` 的映射下，**这两种情况在轴 1 上不可区分**。
- **补偿**：分面。`13` §10 规则 `R6` 的「禁止在无显式裁定时选边」是**推理规则**，按 `18` 自己的理由保留在 `13` 原处，不进轴。

---

**L-2 `15` verdict `UNKNOWN`（「材料不足」）→ 轴 1 `NOT_ASSESSED`**

- **为什么有损**（两层）：(a) **粒度**：`15` 的 verdict 主语是**原子文本单元**；`NOT_ASSESSED` 的主语是**坐标**。(b) **机制**：`材料不足` 包含 MNAR 拒答；映到 `NOT_ASSESSED` 会把「被问过但拒答」重写成「没人被问」。
- **具体不能再表达的案例**：某证人被询问「你是否知道他在外面有人」并选择「无可奉告」。`15` 的 `UNKNOWN` 覆盖它；`NOT_ASSESSED` 不覆盖（「无可奉告」是一个**已记录的应答**）。若用 `NOT_ASSESSED`，`07` §6 FM-08 的 MNAR 禁令就落空了。
- **补偿**：转换规则要求 `NOT_ASSESSED` **必须**同时给出 `u_absence_mechanism` 的具体机制（或明确记为「机制未判定」）。**不得**只写 `NOT_ASSESSED` 就结案。

---

**L-3 `11` §2 的 24 个 `NOT_APPLICABLE` 格 → 轴 2 `APPLICABILITY_UNKNOWN`（不是 `NOT_APPLICABLE_BY_RULE`）**

- **为什么有损**：`NOT_APPLICABLE_BY_RULE` 的**唯一**合法触发是「存在一条**已命名**的 boundary / agreement / 规则」（`MEASUREMENT_SEMANTICS` §2.2）。语料里**没有任何一格**有已登记的规则族 R-2（§3.2 状态：**规则本身尚不存在**）。⇒ 24 格只能落 `APPLICABILITY_UNKNOWN` + 非空 `applicability_reason`。
- **具体不能再表达的案例**：`SexualDesire × S`（兄弟姐妹）。`11` §2 给 `NA`；`11` §3.1 (b) 自陈最强反证：「若某个 sibling dyad 确实存在被记载的性欲坐标，则 `NA` 判定本身错误」。在新表示下，读者看到的是 `APPLICABILITY_UNKNOWN`，reason 里写着「无已登记规则；R11 L-4 假设未登记；`HOLD_FOR_EVIDENCE` (`G-C11`)」。**`11` 的假设内容从「一个取值」降格为「一段理由」** —— 这就是信息丢失的**具体形态**。
- **补偿**：`applicability_reason` 是必填自由文本；要求把被降格的假设连同其最强反证**逐字**写入 reason。**不得**只写「未知」。

---

**L-4 `07` `no_evidence` → `NOT_REPORTED`**

- **为什么有损**：`07` §1 该行在「`Unknown → prior` 是否成立」列写了「**名义上成立（= 先验）**」。这是**代数便利性**的记录位。`NOT_REPORTED` 这个名字只断言「无人报告，也无人不报告」，**不**断言先验可用。
- **具体不能再表达的案例**：`07` §2.2 Round-3 强制的限定语逐字：「它**直接**覆盖 `no_evidence`（名义上 `= prior` 的那一支），但它**不直接**覆盖 `refused` / `refused-to-answer`」。⇒ `NOT_REPORTED` 与 `REFUSED` 的分离**保住了**这条限定的可执行性；但「这一支名义上等于先验」这条**正向**信息在新表示里没有位置。
- **补偿**：不补偿。**这是有意的**：该断言是一个**设计选择**而非世界事实（`07` §7.3 逐字「『Unknown → prior』在稀疏区的收益与代价都集中在这里——不是一个可以靠调参解决的问题，而是**设计选择**」）。把它记成值等于把设计选择固化成语义。**记录为丢失，接受。**

---

**L-5 `16` `NOT_MAPPED.why`「无工具」→ `NOT_INSTRUMENTED`**

- **为什么有损**：`why` **这个维度本身**（记录是哪一项 `why`）被压成单值。`18` `CF-12c` 自己逐字指出五项 `why` 跨三条轴：「`NOT_MAPPED.why` 本身是跨轴的，不能整体归一轴」。
- **具体不能再表达的案例**：同一个数据集变量 `NOT_MAPPED`，一次是因为「无工具」，另一次是因为「只有 pair 级而无方向」。转换后两者在轴 1 上不可区分（只有一次 `NOT_INSTRUMENTED`），而下游处置完全不同（前者可由新工具解决，后者要改 facet 设计）。
- **补偿**：**保留 `NOT_MAPPED` 及其 `why` 字段本身**（它在 mapping 轴上，`C` 所有）。轴 1 只是它的**投影**，不得替代它。

---

**L-6 `16` 的 `UNDETERMINED` / `NON_SEPARABLE` / `CONFLICTED` / `NOT_MAPPED.why`「构念本身未定义」—— 四项无 Axis 1/2 目标**

`18` `CF-12c` 逐字记录前两项「在 R07 的 tag 集合里**也无对应**」，并把 `UNDETERMINED` 放进「轴 3」。

- **本轨的处置**：**不把它们塞进轴 3**（§1.2）。理由逐条：
  1. `directionality_class` 是 `16` §3.2 逐字命名的「**第二个正交必需字段**」，与 `mapping_status` 正交。**具体不能再表达的案例**：`ECR` 是一个已验证工具（`mapping_status = DIRECT_ITEM` 就 generalized attachment 而言成立），但 `directionality_class = AGENT_LEVEL`（`16` §3.2 逐字「target slot 结构上为空」）。在合并轴下，**这两条信息会互相覆盖**：LHRM 要么把 ECR 当成有向状态的证据（有害 —— `16` §3.1 已明令 `PPR` 工具「不得用来推断 `ResponsiveAction_(j->i)`」），要么把 ECR 整体丢弃（丢掉一个可用的 general-trait readout）。**`mapping_status` 与 `directionality_class` 的共存态是真实存在的。**
  2. `CONFLICTED` 一分为二（见 L-16）。
  3. `NOT_MAPPED.why`「构念本身未定义」是**定义缺口**，不是对世界的知识不确定，也不是适用性。**具体案例**：某问卷变量被标注为「relationship quality」——它不是「未测」，也不是「不适用」，而是**所指未定**。Axis 1 与 Axis 2 都没有这个面。⇒ **登记为 schema 缺口，见 §7.5。**
  4. `15` 的 9 类诊断与 `C` 的 8 类不对齐（见 §7.4），其中 `DATA_INSUFFICIENT` 的归属未定义（`18` `CF-14` 后果 3 逐字点名）。

---

**L-7 `16` `directionality_class` 与 `mapping_status` 的粒度差（`TYPE-MISMATCH`）**

`16` §3.1 的主语是**数据集变量 → 候选 LHRM 槽位**；`15` verdict 与 `C` `mapping_outcome` 的主语是**文本单元 / 落点单位**。二者是**不同层级**的操作。`16` §3.3 自己逐字给出与 `#29` 四值词表的对齐表，说明这层映射已被做过一次；与 `C` 的对齐**尚未做**。⇒ 本轨**不做**这个对齐（不属本轨职权），**路由**给 `C`。

---

**L-8 `fact_status` / canonical 事实状态 5 值表 → 只取 `UNKNOWN` 一员（丢失 4 个肯定成员的权威性）**

- **具体不能再表达的案例**：同一份法院文书里，A 案由法院**裁定**（`adjudicated`），B 案只是**被指称**（`alleged`），C 案我们**不知道**（`unknown`）。若把 `fact_status` 整表当「无值词表」处理，转换后三者中只有 C 进入轴 1，A 与 B 之间的差别**在轴 1 上不存在**。`15` §15.6 逐字要求 `fact_status` 与 `assertion_mode` 分成两轴，理由正是「任一份单独看都自洽，三份并列就不可比」。
- **补偿**：`fact_status` 整表**留在原处**（它是 provenance / 证据地位轴，`15` 与 canonical 共同拥有）。轴 1 只是它在「无值」那一格上的投影。

---

**L-9 `07` `not_yet_real` 被 `07` 自己标为「不适用」→ 本轨改判为 `NOT_YET_REAL`**

- `07` §1 该行在「对该 dyad 的正确数学类型」列写「未来未定义」，在「`Unknown → prior` 是否成立」列写「**不适用**」。本轨改判：`NOT_YET_REAL` **适用**，只是尚未发生。
- **为什么有损**：若沿用 `07` 的「不适用」措辞，「尚未发生」会被读成构念不适用；这正是 X-5 禁止的那类混淆。**本轨的改判是纠正，不是丢失。** 但它确实**改变了 `07` 原文的一处分类**，需登记（见 §9 `supersessions` 的交接说明）。
- **具体案例**：`11` §3.4 逐字「成形前的 dyad 不是一个有状态坐标的 pair，而是一个『**提议**』……目前只能靠 `Unknown` 兜，会把『还没发生』与『发生了但我不知道』混为一谈」。⇒ `NOT_YET_REAL` 使这条区分可类型化；代价是 `07` §1 那一格的原文分类被改判。

---

**L-10 `08b` `k = ?` 的主体归属丢失**

- **为什么有损**：`k = ?` 是**主体 `ι` 的悬置**（他还没决定）；`NOT_ASSESSED` 是**观察者/项目卷宗的未评估**。两者方向相反：一个在世界里，一个在卷宗里。
- **具体不能再表达的案例**：`08b` §2.5 逐字「亲密关系材料中『我不敢问』是一个 `?`，而『我们不谈这个』是一个**双方共谋维持的 `?`**（§4.4）」。`?` 的**主体性**是 `08b` §3.9（dogmatism paradox）整节论证的落点：`Harman` 的 defeat solution 与 `Kripke` 的两个残留 worries 结构上正是关于主体在 `?` 状态下遇到证据会转 `+` 或 `−`。把 `?` 映成 `NOT_ASSESSED` 会把**主体的认知状态**变成**项目的记账状态**。
- **补偿（重要）**：**`k` / `m` 是 Belief 层的**立场坐标**（`08b` §2.5 / §2.8），它们的 `?` **不转换**。轴 1 只承接 `08b` 中 `g` / `Pol` / `Rel` / `src` 的 `UNKNOWN` 成员。§5.1 的 V2 第一行应按此读：**`k = ?` 不是一个候选映射**，本轨把它列在那里只是为了记录「**它曾被误当作候选**」这一事实。

---

**L-11 `08b` `g = ASSUMED` → `ADDRESSABLE` + `NOT_REPORTED`（无证据）**

- **为什么有损**：`g` 的六值各对应一条独立处理规则（`08b` §2.6 逐字）。`ASSUMED` 的规则是「前提，无证据支持」；`NOT_REPORTED` 的规则是「无人报告也无人不报告」。后者**蕴含**「没有人报告，也没有人明确不报」；前者**不蕴含**前者 —— `ASSUMED` 常常是**明知无报告而仍然假设**。
- **具体案例**：`08b` §2.6 逐字「若没有 `ASSUMED`，『我假设他知情』会被静默塞进 `FIRSTHAND`」。映射后 `ASSUMED` 与 `NOT_REPORTED` 在轴 1 上同形 ⇒ **「我假设他知情」与「没人报告过他知情」变成同一条记录**。
- **补偿**：`g` 字段**留在原处**（它是 Belief 层的**根据类别**轴）。`ASSUMED` 的语义由 `g = ASSUMED` 承载，**不**由轴 1 承载。

---

**L-12 `08b` `k = ⊘` —— 不是无值，不得转换**

- **具体案例**：`08b` §4.4 的**共谋维持的 `?`** 与真正的 `⊘`（「我们不谈这个，而且我认为这不是个问题」）在 `08b` 的设计里是**两个不同值**；把 `⊘` 当无值会抹掉「主体明确否认这个问题存在」这一肯定断言。
- `08b` §2.11.3 已自行判定，本轨沿用（§3.3）。

---

**L-13 `08b` `Divergent` / `ASYMMETRIC` / `SHARED_NOTED` / `BelievesBoth` / `Overclaim` / `Meta_Unrealized` / `NonDisclosure` / `Unreliable` —— 全部 `OUT-OF-SCOPE`**

`18` `CF-12c` 的 `R08b Divergent / ASYMMETRIC / g ∈ {…, UNKNOWN}` 整行标 **未映射** 并把决定权交给本轨。

- **本轨的答案**：这些是 `08b` §2.11 逐字标注「**永不存储**」的**派生关系**，它们的定义全部是**对两个（或三个）已存储值的判定**。`Divergent(p)` = `k_ι(p) = +` 且 `k_ι'(p) = −`；两侧都是**肯定值**。⇒ **它们不属任何一条「无值」轴，转换是范畴错误。**
- **具体案例**：`BelievesBoth(p)` 要求 `k_ι(p) = k_ι'(p) = +`。若它被放进轴 1，读者会以为「双方都相信」是一种**证据状态**。它不是；它是一个关于**两个信念记录**的派生判定。
- **唯一需要转换的是 `g = UNKNOWN`**（`08b` §2.6），已单列。`08b` 的 8 个派生类**全部不转换**。

---

**L-14 `15` `evidence_channel = ILLEGAL_OBSERVATION` —— 本轨新增一个轴 1 值（`INCLUSIVE` 方向）**

这是**唯一一条从「无 prior token」到「新值」**的映射，也是本轨对语料的净贡献。
- **来源**：`15` §15.6.2 的 `evidence_channel ∈ { DIRECT, TESTIMONIAL, DOCUMENTARY, INFERRED, ILLEGAL_OBSERVATION, ABSENT }`；`15` §1 候选 N04（`NG v PS` [2020] UKSC 51，「配偶；婚内秘密摄录」）逐字「**非法观察通道需 `evidence_channel=ILLEGAL_OBSERVATION`**」。**注意 `15` 同一行的后半句是另一条独立纪律**（「法庭对构念的规范评价不得当 latent state」），它对应 `AGENTS.md` validation discipline 的「do not treat all statements in a judgment as equally adjudicated truth」，落点是 `SOURCE_MARKED_DISPUTED` / `fact_status`，**不是**本值。
- **为什么需要一个独立值**：该情形既不是「没测」（`NOT_INSTRUMENTED`），也不是「不可被该通道观测」（`NOT_ADDRESSABLE_BY_CHANNEL` —— 后者暗示存在**别的**合法通道），而是「**这条通道（秘密摄录）在法律上不可用**」。⇒ 换通道解决不了。
- **具体案例**：一段关系材料**只**能通过婚内秘密摄录获得。`NOT_ADDRESSABLE_BY_CHANNEL` 会诱导「换一条通道」；`INACCESSIBLE_CHANNEL` 明写「这条通道不行」。这直接影响下游的可修复性判断——前者可重规划测，后者只能改设计或放弃该材料。

---

**L-15 `11` §1 码表缺「定义欠定」这一码（`Trust` × S/K/C/W/A **5 格**）—— 无合法目标**

- `11` Round-3 补记逐字：5 格由 `MS` 降为 `UK`，真实状态是「**构念定义未被确定，而非语义跨类型改变**」，并逐字承认「**`UNKNOWN` 也不是完美标签：§1 码表缺一个表示『定义欠定』的码**」；同时登记为 Architect 待决项。
- **为什么无目标**：定义欠定**不是**对世界的知识不确定（再多的 dyad 证据也不解决它），**也不是**适用性（它不是「这个构念在此无意义」，而是「这个构念的**定义**在两种前提之间摇摆）。
- **具体不能再表达的案例**：`Trust` 定义为「愿意把某类脆弱性暴露给 j」，**内建披露史前提**。在零披露史 dyad（初识的专业 dyad）上，同一量表测到的是别的东西。⇒ 这 5 格既不是 `NA` 也不是 `UK`。
- **登记为 schema 缺口**（§7.5）。本轨**不新增**轴 1 或轴 2 的取值（`MEASUREMENT_SEMANTICS` §2.4 禁止 4 / `D` 的接口契约禁止新增维度），**只**把它写成一条 open question + 一条缺口记录。

---

**L-16 `16` `mapping_status = CONFLICTED` 一分为二（丢失单一标签）**

- `16` §3.1 第 6 项逐字：「存在 ≥2 个同样可辩护的候选构念，**或**该构念的实证文献本身互相矛盾。必须附 `conflict_refs`」。
- **为什么有损**：一个枚举值被拆成两个不同轴上的状态。**具体案例**：某变量映射到 ≥2 个同样可辩护的候选构念 —— 这是**映射侧**不可消解的多重性（`C` 的 `MULTI_MAPPING` 但不可指定 primary）；另一变量是 ECR-R 的方法效应把「焦虑–回避正交」这一理论主张本身变成待定（`16` §3.1 逐字「ECR-R 自身的方法效应可把理论上正交的 anxiety–avoidance 相关从 .17 推到 .41（"两维度正交"是工具假象）」）—— 这是**构念身份**冲突，与该 dyad 的证据无关。
- 二者在轴 1 上**都不是** `CONFLICTED_BY_EVIDENCE`（那一条断言的是**该 dyad** 有相反证据）。⇒ 构念身份冲突**无轴**。登记为缺口（§7.5）。

---

**L-17 `07` `value_class` 的双序不转换（丢失全部代数内容）**

- **具体不能再表达的案例**：`07` §6 FM-03 逐字给出反例 —— Case A（两份来源给出相反结论）值 `B`；Case B（无人报告）值 `N`；「任何把两者映射到同一 confidence 值的表示，都在做一次**不可比 → 可比**的压缩」。
- 本轨用 `CONFLICTED_BY_EVIDENCE` vs `NOT_REPORTED` **两个不同的 facet 值**保留了这条区分的**可类型性**，但**没有**保留 K4 的两个序（`⊑_a` / `⊑_t`）、`value_class` 的三分类（`⊑_a` 位置 / `⊑_t` 位置 / 未来未定义 / 不可寻址），或任何运算规则。
- **为什么接受**：`07` §10 非主张 6 逐字「不主张 K4 / RCC8 / IA / STPA× 中任一个是 LHRM 应选的具体代数」；`07` §9.2 `D4` 判完整 QSR 代数**延后**，且必须先声明 tractable subset。⇒ 代数选型不是本轨的交付物。

---

**L-18 `08b` `Pol` / `Rel` / `src` / `temporal_basis` / `evidence_channel = ABSENT` 的字段特定无值语义被压成 `NOT_ASSESSED`**

- **具体案例**：`src = UNKNOWN`（「不可辨是谁说的」）与 `Pol = UNKNOWN`（「未登记证据策略」）在轴 1 上同形。前者的修复动作是**追 provenance**，后者是**做一次策略判定**。
- **补偿**：字段名**必须随值一起保留**（§2.4 的逐 facet 报告纪律 + 字段名）。轴 1 的值**永远**与承载它的字段名一起出现。

---

**L-19 V12 `missingness_mechanism` 的 3 个肯定承诺被 `OUT-OF-SCOPE`（丢失「世界侧 vs 分析侧」的分离）**

- `16` §3.4 的 `missingness_mechanism ∈ { MCAR_assumed, MAR_assumed, MNAR_sensitivity_done, UNKNOWN }` 记录的是**分析者做了什么承诺**；`07` §1 的 tag 记录的是**缺失的生成机制**。
- **具体不能再表达的案例**：两个数据集的真实缺失机制**都是** MAR，但一份做了 `MNAR_sensitivity_done`、另一份没有。两者的 `missingness_mechanism` 取值不同（`MAR_assumed` vs `MNAR_sensitivity_done`），而 `u_absence_mechanism` **相同**。若把两者并到同一 facet，**分析质量的信息全部丢失**。
- **结论**：**这是两个字段，不是一个。** `07` §4.1 规则 `C4` 逐字「tag 取集合并」为这一分离留了位置。**本轨不合并。**

---

**L-20 `UNKNOWN_AS_OF*` 的主语不区分（四种主语共用一枚 token）—— 本轨最大的单条信息丢失**

- **具体不能再表达的案例**（全部来自 `UNKNOWN_AS_OF*` 实际出现的行）：
  1. `04` 的「Wave 2+ `UNKNOWN_AS_OF`」→ 主语是**数据集的一波是否可下载**（V9 / 访问轴）。
  2. `05` 把它用在**关键引用行**（`18` `CF-12b` 逐字「`10:689` 把它用在**关键引用列**，不是用在值类上」）→ 主语是**一条书目记录**。
  3. `A01_EVIDENCE_QUALITY_AUDIT.md`（11 次）→ 主语是**证据质量判定**。
  4. `16` §3.4 / `18` → 主语是**一个坐标的估计**。
- **为什么有损**：一枚 token 承载四种主语。若把全部 94 次都转成轴 1 的 `NOT_ASSESSED`，就会**凭空制造 94 条坐标级不确定记录**，其中约四分之三的主语不是坐标。⇒ 转换规则必须是**逐条判定主语**，不能批量替换。
- **补偿**：`u_as_of` 字段是 `UNKNOWN_AS_OF*` 在轴 1 上的**唯一合法落点**；主语不是坐标的行**不转换**。**这是条件式转换，不是枚举替换。**

---

## 7. 与兄弟轨 `D` / `C` 的一致性与冲突（**不静默调和**）

### 7.1 一致

1. 逐字使用 `applicability` / `applicability_reason` / `applicability_provenance` 与 `APPLICABLE` / `NOT_APPLICABLE_BY_RULE` / `APPLICABILITY_UNKNOWN`（`MEASUREMENT_SEMANTICS` §2.2）。
2. 未新增 applicability 取值；未把 `applicability` 加入任何坐标值域；值域内未出现 `NA`。
3. observability 轴只用 `TBD` 作未判定标记（本文不产出 observability 行；见 `OBSERVABILITY_REGISTRY_V0_1.md`）。
4. `MAPPING_FAILURE` 未进入任何一条轴。
5. 未主张任何具体构念在任何具体 dyad 上不适用（`G-C11` 判 `HOLD_FOR_EVIDENCE`）。

### 7.2 冲突 1：与 `18` `CF-12c` 的 `AMBIGUOUS_NO_UNIQUE_ANSWER → disputed`

- `18` `CF-12c` 逐行：`R13 AMBIGUOUS_NO_UNIQUE_ANSWER → disputed（并保留"禁止在无显式裁定时选边"这条规则）`。
- **本轨的处置**：`→ UNDERDETERMINED_BY_CODING`（新值，见 L-1）。理由：`13` §3.2 逐字「这三个状态**互不等价**」，且 `13` §3.2 引的 Nakamura 原文描述的是「codebook admits multiple defensible classifications」——**没有相反证据**。
- **影响面**：`13` §3.2 的三值抽取状态 + `13` §10 规则 `R6` 的分支集合要求。
- **请 parent 裁决**（不是我能定的）：`18` 是研究侧 audit 产物，本轨是 taxonomy 轨。**若 Architect 接受 `18` 的映射，L-1 的具体案例（speech act vs belief report 的 codebook 欠定）将不可表达。**

### 7.3 冲突 2：与 `18` `CF-12c` 对 `NOT_MAPPED.why`「抽样框不含该情境」的落值

- `18` `CF-12c` 逐字：「`抽样框不含该情境`」落轴 2（`X-10` 的 layer 2）。它未指明落轴 2 的哪个值。
- **本轨的处置**：→ `APPLICABILITY_UNKNOWN` + reason，**不是** `NOT_APPLICABLE_BY_RULE`。依据：**ruling §C item 6 逐字「Search failure/access restriction is not ontology evidence」**；`X-14` 同理（检索范围结论不得升级为总体否定）。
- **若按 `NOT_APPLICABLE_BY_RULE`**，则 `applicability_provenance` 必须指向一条**已命名的规则** —— 而「我们的抽样框里没有」**不是**一条 boundary / agreement / 规则，它是一条**关于本项目**的事实。⇒ 该落法会让 `NOT_APPLICABLE_BY_RULE` 的唯一合法触发条件失效。

### 7.4 冲突 3：`15` 的 9 类诊断与 `C` 的 8 类诊断不对齐（**`C` 轨**）

| | `15` §15.6.3 规则 2（9 类） | `C` `VALIDATION_GATES_V0_2` §3.2（8 类） |
|---|---|---|
| 有 | `ONTOLOGY_HOLE` / `CONSTRUCT_HOLE` / `SCOPE_HOLE` / `TEMPORAL_HOLE` / `BELIEF_OBSERVATION_HOLE` / `TRANSITION_HOLE` / `MEASUREMENT_HOLE` / `NARRATIVE_ONLY` / **`DATA_INSUFFICIENT`** | `ontology hole` / `construct hole` / `scope hole` / `temporal/history hole` / `belief/observation hole` / `measurement hole` / `transition hole`（按 `AGENTS.md` 镜像的 7 项） + **`redundancy hole`**；`merely narrative / irrelevant` 改为**条件式出口** |

- 差异：`15` 有 `DATA_INSUFFICIENT`、**无** `redundancy hole`、且 `NARRATIVE_ONLY` 是**无条件**类；`C` **无** `DATA_INSUFFICIENT`、**有** `redundancy hole`、且叙事出口是条件式。
- `18` `CF-14` 后果 3 逐字已点名：「`DATA_INSUFFICIENT` 对应哪个 tag 未定义」。
- **本轨无法解决**（不在本轨白名单，且 `C` 拥有 mapping 侧）。**路由给 `C`**：`DATA_INSUFFICIENT` 应落在哪一轴，或被显式废弃。本轨的读法是它**跨轴**（可能是轴 1 的 `NOT_ASSESSED`，也可能是轴 3 的一个理由），因此**不能**被当成一个 mapping diagnosis 类。

### 7.5 冲突 4：schema 缺口（本轨**未**新增取值，只登记）

两处**两条轴都没有面**的状态。本轨**不**擅自新增（`MEASUREMENT_SEMANTICS` §2.4 禁止 4；`D` 接口契约第 3/4 条禁止新增维度与第二个 registry）：

| 缺口 | 状态 | 出处 |
|---|---|---|
| **G-1 构念定义欠定**（definition underdetermined） | 轴 1、轴 2 均无面。`11` §1 逐字自陈码表缺此码 | `11` Round-3 补记；`11` §6 第 2 条 |
| **G-2 构念身份冲突**（construct-identity conflict） | 轴 1 的 `CONFLICTED_BY_EVIDENCE` 断言的是**该 dyad** 的证据冲突；构念身份冲突是**跨 dyad 的文献层**冲突 | `16` §3.1 第 6 项后半句 |
| **G-3 构念未定义**（construct undefined） | 轴 1 说「没查清」，轴 2 说「在此无意义」；都不是「所指未定」 | `16` §3.1 `NOT_MAPPED.why` 第 5 项 |

**三者是同一个形状**：**不是「没查到」，也不是「不适用」，而是「问题本身还没被正确提出」。** 是否需要第四条轴（**构念定义状态轴**）是 Architect 的决定，见 §10 open question 2。

### 7.6 冲突 5：`MEASUREMENT_SEMANTICS` §3.6 把 refinement 依赖表等同于本 registry

- `MEASUREMENT_SEMANTICS_V0_1.md` §3.6 逐字：「refinement 程序（研究侧 `07` 的 `⊑` 程序的依赖表，`I9`）| 依赖表**本身即本 registry**」。
- `07` §5.3「第二批（E2，3 条 + 1 条）——只卡在同一件事上」逐字把 `I9` 的**共同前置**列为**三项分列**：「① §3.1 的 `⊑` 形式定义 + 逐坐标依赖表；② **C-P13** 可观察性 / 锚点登记表（`I13` 需要知道哪些坐标是 `structurally_unobservable` / `censored`）；③ `Role` 命名与层级的澄清（§1.1）」——可观察性登记表只是**第 ② 项**。
- `07` §5.1 `I9` 行的判据逐字是「除非有已登记的 `∂F_i/∂z_j ≠ 0`」；`07` §3.4 落地层 ③ 要求登记的是「**逐坐标依赖表的登记格式**」；`CURRENT_ARCHITECTURE.md` §7（本轨 `D` 兄弟轨未改的原文）已把这条依赖写成 canonical 表达式 `partial F_i / partial z_j != 0`。
- **本轨的判断**：依赖表登记的是 **canonical §7 那一族 `∂F_i/∂z_j`（转移层的结构依赖）**；observability registry 登记的是**「构念原则上能否被观察」**。二者是**不同制品**，且 canonical 已把依赖表达式的落点放在 `§7` 而非 `MEASUREMENT_SEMANTICS §3`。把依赖表等同于 registry 会使 `I9` 在**没有任何 `∂F` 登记**的情况下被误判为已就绪。
- **路由**：请 parent 或 `C` 决定表述。**本轨不改 `D` 的文件。**

### 7.7 与 `D` 的两处骨架缺陷（见 `OBSERVABILITY_REGISTRY_V0_1.md` §8）

`MEASUREMENT_SEMANTICS_V0_1.md` §3.5 的 `ACTION_EVENT_OBSERVABLES` 行写「§8 列举的 **12** 类」并列出 11 个名字；`AGENT_ATTRIBUTE_*` 行写「§7 的 **13** 项」并列出 18 个名字。逐字复核 `PARAMETER_CONVERGENCE_V0_1.md` §8（**13** 项，含 `hours together`）与 §7（**15** 行 / **18** 个具名属性）。⇒ **两处计数错误。** 本轨在 `OBSERVABILITY_REGISTRY_V0_1.md` 中按 canonical 逐项展开（13 行 / 18 行），并**保留** `D` 的原文表述作为待更正项。

---

## 8. 路由说明（给 parent）

| 本轨产物 | 建议合并进 | 方式 |
|---|---|---|
| 本文 §2（轴 1 记录形状 + 逐值表） | `docs/foundation/MEASUREMENT_SEMANTICS_V0_1.md` **新增 §2A** | 逐字搬入；`D` 的 §2.2 不动（那是 applicability） |
| 本文 §3（轴 2 + 规则族目录） | 同上 **新增 §2B** | 同上；`D` 的 §2.4 五条禁止不动 |
| 本文 §4–§6（词表清册 / 转换表 / 信息丢失案例） | 同上 **新增附录 A / B / C**，或独立成 `docs/foundation/UNKNOWN_VOCAB_CONVERSION_V0_1.md` | 二选一由 parent 定；**必须保留为可引用文档**，因为 `supersessions` 标记生成要用 |
| `OBSERVABILITY_REGISTRY_V0_1.md` 全文 | `MEASUREMENT_SEMANTICS_V0_1.md` **§3.5 骨架替换为内容** | `D` 的 §3.2 schema / §3.3 读法 / §3.4 约束**不动** |

**合并顺序建议**：`C` 的 `VALIDATION_GATES_V0_2` → `D` 的 `MEASUREMENT_SEMANTICS_V0_1` → 本轨的两份文档。理由：本轨 §1.2 / §5.2 / §7.4 全部引用 `C` 的 `mapping_outcome` 与 `diagnosis`；先定 `C` 才能给本轨的 mapping 侧转换下最终判定。

---

## 9. `supersessions`（本轨**未删除任何 canonical 文本**；以下是需 parent 生成 `SUPERSEDED_BY_REPAIR` 的清单）

**本轨删除的 canonical 文本：0 行。** 本轨是纯新增。

| # | 原文（位置） | 状态 | 取代者 | 依据 |
|---|---|---|---|---|
| 1 | 「10（`07`）+ 4（`08b` 的 `⊘` / `UNKNOWN` / `Divergent` / `ASYMMETRIC` 侧翼）+ canonical 的 5（`CURRENT_ARCHITECTURE.md:315`）去重后仍是一个 **14+ 值枚举**」作为**修法** | **修法被取代** | 两轴 factored register（本文 §2.1） | X-5 / C-P5 / `18` `CF-12c` |
| 2 | `18` `CF-12c` 的「轴 3 · mapping status = R16 6 值 **∪** R15 7 值 **∪** `UNDETERMINED`」 | **本轨不采纳**（未取代，**已弃用提案**） | 引用 `C` 的 `mapping_outcome` + `diagnosis`（§1.2） | `C` §3 拥有 mapping 侧；并集会造成第二份 SSOT |
| 3 | `18` `CF-12c` 的「R13 `AMBIGUOUS_NO_UNIQUE_ANSWER` → `disputed`」 | **本轨改判** | `→ UNDERDETERMINED_BY_CODING` | `13` §3.2 逐字「这三个状态**互不等价**」；L-1 |
| 4 | `07` §1 表 `not_yet_real` 行的「不适用」标注 | **本轨改判** | `→ NOT_YET_REAL`（适用，未发生） | `07` §2.3.1 第 3 条；L-9 |
| 5 | `11` §3.1 的值域扩充提案 `{applicable(estimate/interval/…), structurally_not_applicable, scope_unknown}`（**值域内**） | **REJECT**（作为**值域扩充**） | 轴 2 的 `applicability` 正交元数据 | X-5：`MEASUREMENT_SEMANTICS` §2.4 禁止 3 |
| 6 | `11` §3.1 的「**不能停在 proposal、必须 durable**」框架 | **WITHDRAWN** | 无（`11` 自身 Round-3 已撤回） | X-5 |
| 7 | `08b` §2.5 的 `reporter_role` 命名 | 已由 `07` §9.3 改名 `role_lens` | — | `07` §1.1（`E-C23`） |

---

## 10. `open_questions_for_architect`

1. **是否接受 §7.2 的改判**（`AMBIGUOUS_NO_UNIQUE_ANSWER` → `UNDERDETERMINED_BY_CODING`，而非 `18` 的 `→ disputed`）？不接受则 L-1 的具体案例不可表达。
2. **§7.5 的三个 schema 缺口（G-1 定义欠定 / G-2 构念身份冲突 / G-3 构念未定义）是否需要第四条轴？** 三者都不是「没查到」也不是「不适用」。本轨**未擅自新增**任何取值。
3. **`NOT_APPLICABLE_BY_RULE` 的规则族 R-2（`HD-ST-1` dyad-class 范围裁定）由谁签发？** 规则族本身**尚不存在**（§3.2）。没有它，`11` 的 24 格永久停在 `APPLICABILITY_UNKNOWN`。签发者是 Architect 决定（`NEXT_EXPERIMENTS` `A-7` 判「它是一条 Architect 裁决，不是研究问题」）。
4. **`C` 的 8 类诊断与 `15` 的 9 类如何对齐**（§7.4）？`DATA_INSUFFICIENT` 落在哪一轴，还是被显式废弃？
5. **§7.6 的依赖表表述**：「refinement 依赖表 = observability registry」（`D`）还是「两者是不同制品」（`07` §5.0 E2）？
6. **§2.4 的逐 facet 报告纪律是否采纳为硬要求？** 不采纳则 `07` §1 的 10 值压平风险（`07` §1 逐字「同一种违规的更隐蔽形式」）回归。
7. **是否需要命名空间前缀方案？** §5.3 分离了 `disputed` 的三处同名，但**没有**给出前缀语法。`18` `CF-12c` 逐字要求「**须带命名空间前缀**」却未给方案。候选：`ns=07` / `ns=08b` / `ns=fact_status`（本文 §5.3 用法），但这是 Architect 的命名决定。

---

## 11. `explicit_non_claims`

1. **未运行任何 Gate，未映射任何 fixture。** 本文无任何 mapping 结果、cell 状态或覆盖数字。
2. **未主张任何具体构念在任何具体 dyad 上「不适用」。** `G-C11` 判 `HOLD_FOR_EVIDENCE`；§3.2 的规则族目录是**授权机制**的登记，不是任何一次具体适用。
3. **未把 `11` 的 24 个 `NA` 格当作已成立的否定结论。** 它们映射成 `APPLICABILITY_UNKNOWN`（L-3）。
4. **未选定 K4 / RCC8 / IA / STPA× 中任何一个代数**，未把 `07` 的 `value_class` 双序搬进 canonical（§2.5 第 1 条、L-17）。
5. **未定义 `evidence_mass` / `width` / `coverage` 的度量或任何阈值。** `07` §9.2 `D8` / §11-2：本轨拒绝给。
6. **未把 `REFUSE` 登记为取值。** 它是 readout 层的一等输出（§2.5 第 3 条）。
7. **未把 `08b` 的 `k = ?` 或 `⊘` 转换为轴 1 的值。** `?` 是主体立场（L-10），`⊘` 是肯定回答（L-12）。
8. **未把 `08b` 的 8 个派生关系（`Divergent` 等）当作无值词表。** 它们是永不存储的派生判定（L-13）。
9. **未把 `15` 的 `fact_status` / `temporal_basis` / `evidence_channel` / verdict 4 张表整体当作「无值词表」。** 只有 4 个成员是无值（L-8）。
10. **未把 `04` 的 `access_rights_axis` 并入任何一条轴。** `R3-A3b` 逐字「两轴不可互相推导」。
11. **未把 `16` 的 `mapping_status` 与 `C` 的 `mapping_outcome` 合并**，也**未**把 `directionality_class` 并进 mapping 轴（L-6）。
12. **未把 `UNKNOWN_AS_OF*` 批量替换为轴 1 取值。** 转换是逐条判定主语的条件式转换（L-20）。
13. **未新增 applicability 取值、未新增轴 1 之外的新维度、未另立第二份 registry、未引入第二个未判定标记。**
14. **未把 PR #31 / #32 的 swarm 主张当作已验证科学。** 实现的是 adjudication V1 的裁决；§5.1 的 `18` 侧映射（`CF-12c`）是**待复核的研究产物**，与本轨不一致处已在 §7 显式列出。
15. **未合并、未 push、未开 PR、未改任何 GitHub review state。** 交付形式 = branch + commit + packet。
16. **未读取 / 未执行 / 未引用 `#20` / `#21` / `#22`；未运行 Eye/Juece；未下载受限数据；未做文献扫描。**
