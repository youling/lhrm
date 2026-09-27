# Validation Gates v0.2 — 四门分离的验证协议

**Status:** CANDIDATE CANONICAL（未执行；本次只构造协议，不跑任何 Gate）
**As of:** 2026-09-28
**Authority:** `youling/lhrm#30` `ARCHITECT_ADJUDICATION_V1`（comment `5854920569`）· `ARCHITECT_ROUND3_DISPATCH_V1`（comment `5854930069`）Track R3-C
**Supersedes:** `docs/foundation/PARAMETER_CONVERGENCE_V0_1.md` §15 `Gate A / Gate B / Gate C`（原文保留在该文件 §15 的 `SUPERSEDED` 块内，未删除）
**Vocabulary owner:** 落点词表 `LHRM-LANDING-1` 的 SSOT = `PARAMETER_CONVERGENCE_V0_1.md` §13（**不在本文重复**）

> 本文的职责**只有**「门怎么执行、结果怎么落到候选清单上」。落点类、诊断类、判据文字本体都在
> `PARAMETER_CONVERGENCE_V0_1.md` §2 / §13；本文不复制它们，避免出现第二份竞争 SSOT。
>
> **本文不含任何已执行结果。** 本文构建之日，`GATE_COVERAGE` 尚未运行，
> `GATE_MINIMALITY` / `GATE_CROSS_CONTEXT` / `GATE_REDUNDANCY` 的前置材料尚不存在。

---

## 1. 为什么拆成四门

`PARAMETER_CONVERGENCE_V0_1.md` §15 原文把三件事塞进一个 `Gate A / B / C`：

- Gate A 是**覆盖**要求（关系相关事实能否表示）；
- Gate B 是**清单**（跨语境测什么），不是判据；
- Gate C 只在「通过后才有资格推进」这一句里起作用，它自己既无判据也无后果。

裁决 §C item 4 明确：**Gate A 的 Court-fact 覆盖 ≠ construct 最小性**；最小性有自己的 ablation 子门与
**construct-bearing** benchmark。`H-A2` 进一步核实：§2.6 承诺「这项将在 Case Bank regression 中直接测试」，
而 Gate A 的五个步骤里**没有任何一步包含「移除某个 construct 再重测」**——缺的是**一条臂**，不是一个阈值。

| id | 门 | 唯一职责 | 明确**不**回答 | 今日可执行性 |
|---|---|---|---|---|
| `GATE_COVERAGE` | Coverage Gate | 关系相关事实**能否被表示**（不新造构念） | 构念是否必要 | **可执行**（用已冻结 fixture） |
| `GATE_MINIMALITY` | Minimality / Ablation Gate | 构念**是否必要**，还是冗余/可无损派生 | 语义是否跨语境稳定 | **不可执行**（缺 construct-bearing benchmark，见 §6.2 / X-9） |
| `GATE_CROSS_CONTEXT` | Cross-context Gate | 构念语义在**独立生成**的 benchmark 上**是否稳定** | 是否有表示能力证据 | 部分（Table A 多为 `NOT_RUN`） |
| `GATE_REDUNDANCY` | Redundancy Gate | 对每个候选签发**终局处置** `KEEP｜MERGE｜DERIVE｜REJECT｜HOLD` | 具体构念的语义定义 | 依赖前三门 |

**分离的硬规则**：`GATE_COVERAGE` 的失败**不得**直接产生 `REJECT`；`GATE_MINIMALITY` 的失败**不得**被
`GATE_CROSS_CONTEXT` 顶替；`GATE_REDUNDANCY` **不得**在任一前置门为 `NOT_RUN` 时签发 `KEEP`。

---

## 2. 终局处置枚举（5 值）

### 2.1 枚举值

```text
KEEP | MERGE | DERIVE | REJECT | HOLD
```

### 2.2 与裁决文本的 delta（**须 parent 路由**）

- 裁决 C-P1 写的是 **4 值**：`KEEP | MERGE | REJECT | HOLD`。
- dispatch R3-C 第 1 条写的是 **5 值**：`KEEP / MERGE / DERIVE / REJECT / HOLD`。

**本文实现 5 值。** 理由：`DERIVE` 是 canonical **既有**范畴，不是新发明。`PARAMETER_CONVERGENCE_V0_1.md`
§9 `R1`（`Mutuality_k = H(Z[k,A,B], Z[k,B,A])`）、§9 `R2`（`PowerImbalance = f(OutcomeDependence_(A->B), OutcomeDependence_(B->A), …)`）、
§9 `R5`（`Alignment` 拆 `ValueCongruence` / `GoalAlignment`）已经是「由其它坐标算出」的条目；
§3 的容器把 `PairState_(A,B)` 与两条有向 `DirectedRelationship_(A->B)` / `(B->A)` **分开列出**，
`CONSTRUCT_SCOPE_DIRECTIONALITY` §2 则明写 mutuality / asymmetry **优先由双向状态派生，不额外重复设 primitive**。
若只给 4 值，`R1`/`R2` 的结果只能被记成 `MERGE`，会把「同义合并」与「可计算派生」混为一谈——
而 §1 的第二个问题（`What is derived rather than primitive?`）正是靠这条区分成立的。

### 2.3 每个值的执行语义

| 值 | 触发条件（证据） | 产生者 | 记录位置 | 对候选清单做什么 | 可逆性 |
|---|---|---|---|---|---|
| `KEEP` | 同时满足 **K1**–**K4**（见下） | Project Architect，依据前三门的记录 | 本文 §7 处置台账 + `PARAMETER_CONVERGENCE` §11 basis 清单 | 留在 basis，无附加标注 | **可逆**。新证据可下调；`KEEP` 不锁定 |
| `MERGE` | `<k>` 与 `<m>` 在 **construct-bearing** 材料上**同义**：落在 `<k>` 的每个实例都能无损落在 `<m>`。须填 `MERGE_TARGET = <m>` | Project Architect | 同上 + `MERGE_TARGET` 字段 | `<k>` 移出 basis；其单位改锚到 `<m>`；**必须**留映射别名以保 provenance | **可逆**。删别名即恢复 `<k>` |
| `DERIVE` | `<k>` 的内容是其它保留坐标/记录的**函数**（如 `Mutuality_k`、`Asymmetry_k`、`PowerImbalance`），本身不是状态。须填 `DERIVATION = <函数/公式引用>` | Project Architect | 同上 + `DERIVATION` 字段 | `<k>` 移出 primitive basis，进入 readout 清单；readout 条目**必须**列出其输入 | **可逆**。出现「可无损表示且不可派生」的构造证据时可重新提升；输入保持记录 |
| `REJECT` | 最小性失败且**不可**恢复为别名或派生：withheld 后在 construct-bearing 材料上**无任何降级**，且当前 schema 无任何单位需要它（本体并不缺它） | Project Architect | 同上 + `REENTRY_CRITERION` 字段 | 移出候选 basis；**仅**作为历史证据与 re-entry criterion 保留 | **仅在满足所写 re-entry criterion 的新证据下**可逆 |
| `HOLD` | 证据缺失 / 不可访问 / 判据未定：`NOT_RUN` cell、ablation 未在 construct-bearing 材料上跑过、诊断为 `CONTESTED` | Project Architect；access/rights 类 hold 由该门的既有负责人登记（本文不定义其行为） | 同上 + `HOLD_REASON ∈ { EVIDENCE_MISSING, ACCESS_OR_RIGHTS, BENCHMARK_NOT_BUILT, CRITERION_UNDEFINED, CONTESTED }` | 留在候选清单但标 **non-promotable**；**不得**计入任何推进决策 | **可逆**，且按定义是暂态：列明的证据到位即失效 |

**K1–K4（`KEEP` 的必要条件）：**

```text
K1  GATE_COVERAGE 已在至少一份 construct-bearing 材料上通过
K2  withheld `<k>` 后至少 1 个单位发生降级（`ablation_record` 非空且 `downgrade_kind` 已填）
K3  没有任何未结清的 `redundancy hole` 诊断指向 `<k>`
K4  `<k>` 参与裁决的每个 cell 都是 RUN + STABLE；不参与的 cell 必须记录「不参与」及其理由
```

**`HOLD` 不是软化的 `KEEP`。** `HOLD` 的构念**不得**被计入任何 `Minimal Sufficient State` 推进论证。

### 2.4 单个 `MAPPING_FAILURE` 不是本体否决

裁决 C-P1 明文：**A single relation-relevant `MAPPING_FAILURE` is a failure event to diagnose, not an
automatic ontology rejection; ablation evidence accumulates toward MERGE/REJECT.**
因此：单次 `MAPPING_FAILURE` 只进 §3 的诊断台账；只有 ablation 证据**累积**才流向 `MERGE` / `DERIVE` / `REJECT`。
本文**不设**「几个 failure 就 REJECT」的计数阈值（见 §8 declined-threshold register 第 8 条）。

---

## 3. `MAPPING_FAILURE` 的可达性与持久性

`H-A3` 核实：`MAPPING_FAILURE` 在**类型上不可达**，由**三个**文本互不相同、作用于流水线三个阶段的机制造成。
三者必须**同时**修；只修一处仍然不可达。

### 3.1 机制 (1)：落点类的 4 个 catch-all

| 阶段 | 原文位置 | 操作 | 缺陷 |
|---|---|---|---|
| 分类 | `PARAMETER_CONVERGENCE` §13 的第 7/8/9/10 类 | 装不下的句子**找不到**可落类 | 失败**不被记录** |

结构性事实：`HISTORY_TIMELINE` 与 `PROVENANCE_UNCERTAINTY` 对**每一个**单位都可用（任何陈述都有时间索引与归属）。
因此「有一个类可用」永远为真，而**可用 ≠ 正确表示**。§14 原文的成功判据「只要求**语义有合法落点**」
把「可用」当成了「通过」。

**修复（本轮实施）：**

1. **归类前的相关性前置检查**成为流水线第 0 阶段（§3.3）。
2. 落点赋值带一个**新字段**：

```text
catchall_used ∈ { NO, YES }
landing_reason  # catchall_used = YES 时必填，非空
```

3. **fail-closed 默认**：`catchall_used = YES` 时，该单位的 `mapping_outcome` **默认**为 `PARTIAL_MAPPING`，
   **不是** pass。只有分诊显式结清（triage discharge）才可升级为 `DIRECT_MAPPING`，且结清必须写入理由。
4. 合并后（§4）catch-all 类由 4 个降为 3 个（`ENVIRONMENT` / `HISTORY_TIMELINE` / `PROVENANCE_UNCERTAINTY`），
   叙事评价不再是落点类而是**状态位**。**未宣称消除它们**——它们是结构性兜底，只能被约束，不能被消灭。

### 3.2 机制 (2)：诊断清单里的「merely narrative / irrelevant」出口

`§13:648` 与 `AGENTS.md:62` 是**同一条 7 项诊断清单的逐字镜像**（`H-A3` 独立来源数 = 1 primary + 1 mirror）。
原文含一个无条件的解释性出口 ⇒ 已记录的失败**必然被解释掉** ⇒ 失败**永不升级**。

**修复（本轮实施，落在 `§13`；`AGENTS.md:62` 的镜像同步以提案形式交回，见 §9 P-1）：**

1. **新增一个诊断类**，补上「冗余结果当前无处可记」的类型缺口：

```text
redundancy hole — 该 unit 可由 <k> 无损表示，故 <m> 非必要
```

2. **`merely narrative / irrelevant` 改为条件式、必须记录的出口**（词面保留不变以维持镜像匹配）：

```text
允许以 merely narrative / irrelevant 结清 MAPPING_FAILURE，
当且仅当三条同时成立：

  (a) 记录非空的 relation_relevance_reason —— 该单位为何不承载 i–j 的状态 / 互动 / 约束；
  (b) 已证明该单位「不是因为找不到类才落不进」，而是因为存在一个语义正确的类并被有意放弃
      （即：证明过 unmappability，而不只是「不重要」）；
  (c) 结清计入运行台账的 DISCHARGED_NARRATIVE 计数，与失败计数**并列报告，永不合并**。
```

任一条不成立 ⇒ 结清无效 ⇒ 该单位保留为 `MAPPING_FAILURE`，缺省归入 `ontology hole`。

> (b) 是本条的关键：**「不相关」与「不可表示」是两个不同命题**。要求理由只能排除前者。

### 3.3 机制 (3)：成功门槛被降到「有合法落点」

**修复：把门的结果字段从「是否有类」改为「是否被正确表示」。** 新增输出字段：

```text
mapping_outcome ∈ { DIRECT_MAPPING, PARTIAL_MAPPING, MULTI_MAPPING,
                    MAPPING_FAILURE, NON_RELATION_RELEVANT_EXIT }
```

前三个 token 沿用 §15 Gate A 第 4 步原文（`PARTIAL_MAPPING / MULTI_MAPPING / MAPPING_FAILURE`），未改字面。
`MULTI_MAPPING` **不是**自动失败：同一单位可以合法地有两个落点（例：「他说他爱她」= `ACTION_EVENT` 的言语行为
+ `BELIEF_STATE` 的信念报告）。规则：

- `MULTI_MAPPING` 记为 **pass，但必须指定 primary 与 secondary 落点**；
- 仅当两个候选落点把**同一个单位**指派到**不同 layer** 且未声明二者关系时，才升级为
  `MAPPING_FAILURE`（诊断类 `ontology hole`，子标记 `layer conflict`）。

### 3.4 修复后的流水线阶段

```text
STAGE 0  relation-relevance pre-check      -> 命中则 NON_RELATION_RELEVANT_EXIT（条件式 + 记录）
STAGE 1  landing-class assignment          -> 无类可落则 MAPPING_FAILURE（记录，持久）
STAGE 2  diagnosis                         -> 8 类诊断词表之一（含 redundancy hole）
STAGE 3  triage / escalation               -> 结清必须过 §3.2 三条；否则保留为 MAPPING_FAILURE
STAGE 4  gate accounting                   -> 失败数与结清数**并列**报告
```

`MAPPING_FAILURE` 的持久性由此确立：**它在 STAGE 1 产生，携带单位 id、来源锚、诊断类、结清状态，
进入 §7 台账；任何后续门都不能删除它，只能结清它。**

---

## 4. 落点词表合并（`§2.5` × `§13`）

`ADJ3` rec 7 / C-P1 项 7：两表各 10 项、重叠 7 项、各有 3 项只在一边 ⇒ 任何 layer 判定都能被两套词表分别「证成」。

**本文不复制词表。** 合并后的 SSOT 落在 `PARAMETER_CONVERGENCE_V0_1.md` §13，命名 `LHRM-LANDING-1`。
此处只记录**合并的算术与处置**，供 parent 复核：

```text
§2.5 独有 3 项：Observable proxy · Derived readout · Mechanism evidence
§13  独有 3 项：History/Timeline · Provenance/Uncertainty · Derived/Narrative-only
重叠   7 项：Agent attribute/state · Directed relationship state · Pair property/state ·
              Belief/perception ≡ BeliefState · Action/Event · Constraint/Agreement · Environment
=> 13 个 legacy 字符串，合并为 10 个落点类 + 3 个跨类状态位
```

处置要点（**须与 §13 的改写一致才成立**）：

1. §2.5 独有的 3 项**不是落点类**，改判为跨类状态位 `OBSERVABLE_PROXY_STATUS` / `MECHANISM_EVIDENCE_STATUS` /
   `NARRATIVE_EVALUATION_STATUS`：一个单位是「可观察代理」或「机制证据」是**关于它的说法**，
   不回答它落在哪一层；落点仍必须另指。
2. §13 的 `Derived/Narrative-only` 一分为二：`DERIVED_READOUT` 保留为落点类；
   `narrative` 部分降为 `NARRATIVE_EVALUATION_STATUS`，**不再具有兜底吸收能力**（§3.2）。
3. 因此 catch-all 落点类由 4 个（`ENVIRONMENT` / `HISTORY_TIMELINE` / `PROVENANCE_UNCERTAINTY` /
   `Derived/Narrative-only`）降为 **3 个**。**记录：这是收敛，不是消除。**

---

## 5. 六个判据的执行规格（`§2.1`–`§2.6`）

`ADJ3` Q2 逐条确认：`§2.1`–`§2.6` **六条全部**缺 procedure / required evidence / output field /
threshold / designated executor；`:43` 是唯一程序性句子且未指定审计者、产出、失败后果；
`§2.1` / `§2.3` / `§2.4` **连后果句都没有**。下表是补齐规格。判据**本体文字**在 `§2`，此处只写执行面。

| 判据 | 后果句（FAIL 时发生什么） | 输出字段 | 阈值 | 指定执行者 |
|---|---|---|---|---|
| §2.1 Semantic independence | 该 construct **不得**新提升进 basis；成为 `DERIVE` / `MERGE` 候选。**不自动移出**（还需覆盖证据） | `semantic_independence_record` = {claim, counterexample_or_none, evidence_ref, status ∈ `INDEPENDENT` / `NOT_ESTABLISHED` / `REFUTED`} | **无（拒设）**，见 §8-2 | Project Architect 裁定；证据由 `Independent Mapping Agent` 产出 |
| §2.2 Counterexample decoupling | 无稳定解耦实例 ⇒ `HOLD`（`HOLD_REASON = EVIDENCE_MISSING`）；若同时显示**耦合**行为（无任何象限组合可构造）⇒ `MERGE` 候选。**注意不对称性：反例缺失是弱证据** | `decoupling_record`（逐 Table B cell） | **无（拒设）**，见 §8-3 | Project Architect；实例由 `Benchmark Owner` 从 `GATE_CROSS_CONTEXT` 提供 |
| §2.3 Conditional incremental information | FAIL ⇒ `DERIVE` 候选。**FAIL 不得由「未观测到」断言** | `incremental_information_record` = {conditioning_set, information_source, status ∈ `DEMONSTRATED` / `NOT_DEMONSTRATED` / `UNTESTABLE_WITH_CURRENT_DATA`} | **无（拒设）**，见 §8-4 | Project Architect（分类）+ Empirical/Measurement lane（证据）联合指定 |
| §2.4 Scope stability | 任一 `RUN` cell 判 `UNSTABLE` ⇒ 该构念定义在该语境有缺陷 ⇒ `HOLD`（`CONTESTED`）并升级为定义修复。**`NOT_RUN` 不满足 §2.4**，且**永不**计为 pass | `scope_stability_record`（逐 Table A cell）= {cell_id, instance_ref, reading, stability ∈ `STABLE` / `UNSTABLE` / `NOT_RUN`} | **结构性零 N**：满足 = 无 `UNSTABLE` 的 `RUN` cell **且** 无 `NOT_RUN` cell。这是从判据定义推出的，不是选定的 N（见 §8-5） | Project Architect |
| §2.5 Layer test | 重路由到该判据指定的层；只是行为/标签/结果/proxy 者**不因常见就升级为 primitive**。层归属**不可**由预测强度重开 | `layer_assignment` = `LHRM-LANDING-1` 中的一个值 + `layer_reason` + `evidence_ref` | **无数值阈值（不适用）**：判据是类别型的（见 §8-6） | Project Architect |
| §2.6 Representation necessity | FAIL ⇒ `MERGE` / `DERIVE` 候选（依本文 §2.4：单次 `MAPPING_FAILURE` 非否决，ablation 证据累积，**不自动 REJECT**）。**这是唯一能让 basis 缩小的判据** | `ablation_record`（逐 construct × fixture）= {construct_withheld, downgraded_unit_ids, downgrade_kind ∈ `DIRECT→PARTIAL` / `DIRECT→FAILURE`, collateral} | **结构性存在条件**：necessity ≡ 存在至少 1 个 witness；`NON_NECESSARY` ≡ 零降级。**但**该条件只有在 construct-bearing 材料上跑过才有效；否则判 `UNTESTABLE` → `HOLD`，**不得**判 `KEEP` | `Independent Mapping Agent` 执行臂；Project Architect 裁定 |

### 5.1 「重要」的操作化定义（`§2.6` 原文「**重要**现实句子/状态」未定义）

C-P1 项 1 要求定义它。**本文的定义不依赖标注者印象，而依赖 ablation 输出：**

```text
relation-relevant(u)  当且仅当 u 承载下列之一：
  (i)   任一 Agent 对另一方的状态；
  (ii)  该 pair 的有向状态或共享状态；
  (iii) 制约其互动的 constraint / agreement / environment；
  (iv)  其被某一方解释后可能成为 (i)(ii)(iii) 输入的 action / observation。

material(u | 删除 <k>)  当且仅当 relation-relevant(u) 且删除 <k> 后 u 的 mapping 发生降级
                        且该降级未被另一落点类吸收。
```

即：「重要」= **可由删除实验观测到的降级**，不是「看起来重要」。

---

## 6. 四个门的执行规格

### 6.0 共享程序步骤 `ARM-ABL-1`（leave-one-construct-out ablation arm）

`H-A2`：§2.6 的承诺未被兑现，缺的是**一条臂**。本臂是 Case Bank regression 的**共享步骤**，
被两门读取同一份记录——这样就不必造第二套回归：

```text
ARM-ABL-1  (逐 construct 执行一次，结果被两门共用)

  baseline arm : 完整 basis 映射，记录每个单位的 mapping_outcome
  withheld arm : 逐一 withheld <k>（<k> 从 §11 basis 清单移出，不新增任何构念），
                 重跑同一批单位，记录 mapping_outcome 的变化
  记录         : ablation_record（含 downgraded_unit_ids 与 downgrade_kind）
  硬规则       : withheld 期间**不得**新造构念；新造构念 = `ontology hole`，
                 该次 withheld run 作废并重跑（记录作废理由）
  不可比较性   : 变更 schema 前后产出的 mapping 计数**不可**直接比较
                 （`H-F38` 同类约束：冻结 fixture 钉在 schema 版本上）
```

- `GATE_COVERAGE` 读 **baseline arm**；
- `GATE_MINIMALITY` 读 **withheld arm**。

### 6.1 `GATE_COVERAGE` — Coverage Gate

| 项 | 内容 |
|---|---|
| 问题 | 关系相关事实**能否被表示**（不新造构念） |
| 输入 | 已冻结 fixture（Fixture 001 / 002 / 003）+ Case Bank `#13` 单位 |
| 步骤 | 0) 流水线 STAGE 0–4（§3.4） 1) `ARM-ABL-1` 的 baseline arm 2) 逐单位落点 + `catchall_used` 3) `MAPPING_FAILURE` 全部进诊断台账 4) 两种结清分别执行——catch-all 结清按 §3.1-3（需 `landing_reason`），叙事结清按 §3.2 的三条 5) 报告：五类 outcome 计数 + 两种结清计数，**并列** |
| 产出字段 | `mapping_outcome` · `landing_class` · `catchall_used` · `landing_reason` · `diagnosis` · `discharge_status` |
| **通过判据** | 该 fixture 内 `MAPPING_FAILURE` 计数 = 0 **且** 未结清的 `catchall_used = YES` 计数 = 0 |
| 阈值性质 | **结构性零 N**（由门自身的成功定义推出）。**不是**「至少 N 个 fixture」——后者按 C-P1 拒设（§8-1） |
| 失败处置 | 单个 `MAPPING_FAILURE` → 诊断，**不**产生 `REJECT`（§2.4） |
| 执行者 | `Independent Mapping Agent`（须与 basis 定义独立）产出；Project Architect 诊断 |

### 6.2 `GATE_MINIMALITY` — Minimality / Ablation Gate

| 项 | 内容 |
|---|---|
| 问题 | 构念**是否必要**，还是冗余 / 可无损派生 |
| 前置 | **必须**有 construct-bearing 材料。未有 ⇒ 全部 §11 构念判 `UNTESTABLE`，处置 `HOLD` / `BENCHMARK_NOT_BUILT` |
| 步骤 | 1) `ARM-ABL-1` 的 withheld arm 2) 对每个 `redundancy hole` 诊断确认是否**无损** 3) 交 §5 的 §2.1 / §2.2 / §2.3 记录 4) 交 §7 签发处置 |
| 产出字段 | `ablation_record` · `materiality_verdict`（§5.1）· `lossless_derivation_ref` |
| 通过判据 | 对被检验的 `<k>`：necessity ≡ 至少 1 个 witness 降级；否则 `NON_NECESSARY` → `MERGE`/`DERIVE` 候选 |
| 阈值性质 | **结构性存在条件**（≥1 witness）。「跑几份 fixture」拒设（§8-7） |
| 失败处置 | 交 Redundancy Gate；本文**不**直接删构念 |
| 执行者 | `Independent Mapping Agent` 执行臂；Project Architect 裁定 |

**X-9（本门不得越界）：** Fixture 001 是**事实 / 观察 / 信念 / 行动 / 历史 / 归属表示与 mapping-failure 语义**
的测试，**不是**八项 relationship-state construct 必要性的证据。其 core dyad 是雇主↔雇员，
26 个原子事实是排班 / 停业 / 未付薪 / CAB / 申诉等**机构性事实**。因此：

- **construct-bearing benchmark 由兄弟轨规划，本轨不构建。**
- 在该 benchmark 存在之前，本门**不得**签出任何 `KEEP`，也**不得**用 Fixture 001 代替它。

### 6.3 `GATE_CROSS_CONTEXT` — Cross-context Gate

| 项 | 内容 |
|---|---|
| 问题 | 构念语义在**独立生成**的 benchmark 上是否稳定 |
| 硬前置 | benchmark **必须独立于当前候选 basis 生成**（§6.3.1） |
| 步骤 | 1) 读 Table A / Table B 的 cell 状态 2) 对 `RUN` cell 逐实例记录 `reading` 3) 判 `STABLE` / `UNSTABLE` / `NOT_RUN` 4) 汇入 §2.4 的 `scope_stability_record` |
| 产出字段 | `cell_status`（逐 cell）· `benchmark_instance_ref` · `reading` · `stability` · `executor` |
| 通过判据 | **逐 cell**（§6.3.2 / §6.3.3），**不存在**跨 cell 的单一分母 |
| 阈值性质 | 无全局比例阈值（§8-9） |
| 执行者 | `Benchmark Owner`（独立生成）产出；Project Architect 判 `STABLE` / `UNSTABLE` |

#### 6.3.1 独立生成的硬要求

`C-P2`：Gate B 的 counterexample list 当前是**项目自身假说清单的复述**，门因此是确认装置。
独立性的可检查形式（不是口号）：

1. 生成者的输入**只有** cell 的**行为定义**（`cell_definition`），**不得**看到：
   §11 basis 清单、任何构念的语义定义、§2.5 layer 判定、§12 的六项推测性排除、
   或本项目任何既有反例清单。
2. 每个 cell 的实例集合须附**来源**与**选入理由**；选入理由必须是「该情境在此材料中自然出现」，
   **不得**是「它能击穿 LHRM」。若某 cell 的全部实例都因后者入选，**该 cell 作废重做**。
3. `Benchmark Owner` 不得是 `GATE_MINIMALITY` 的执行者（避免同一批材料同时决定 basis 的去留）。
4. 权利 / 访问受限的来源按既有 fail-closed 处理：**记为 `NOT_RUN` 并注明 rights/access 原因**，
   **不得**记为 pass，**也不得**记为「不存在该语境」。

#### 6.3.2 Table A — sampling-frame contexts（**抽样框**）

SSOT 分类法 = `HD-ST-1`（Human-Dyad sampling taxonomy），定义与对齐要求见 §6.4。
**Table A 不得与 Table B 合并计数。**

**逐 cell pass/fail 语义（两表共用同一套规则）：**

| cell 状态 | 含义 | 是否计入 §2.4 |
|---|---|---|
| `PASS` | 该 cell 的每个关系相关单位都有 `DIRECT_MAPPING` 或**已声明 primary/secondary 的** `MULTI_MAPPING`；`MAPPING_FAILURE` = 0；未结清 `catchall_used = YES` = 0 | 计入（`STABLE`） |
| `FAIL_UNSTABLE` | 构念在该 cell 的读法与其记录定义**矛盾** ⇒ 定义缺陷 | 计入（`UNSTABLE`）→ §2.4 `HOLD`/`CONTESTED` |
| `FAIL_UNMAPPABLE` | 至少 1 个关系相关单位 `MAPPING_FAILURE`，或该 cell 迫使 schema **新增**落点类/构念才可表示（新增**不被允许**，故记为失败） | 计入（`UNSTABLE`）→ 诊断 |
| `NOT_RUN` | 无实例可用（未采集 / access / rights / cell 判据未定义） | **不计入**（既非 `STABLE` 也非 `UNSTABLE`），但**使 §2.4 不被满足**（§5 表 §2.4 行） |

**Table A 必需 cell**（逐 cell 一行；`coverage` 一列是**本审计语料内的检索范围陈述**，不是存在性陈述——X-14）：

| cell_id | sampling-frame context | `dyad_class` | 本审计语料（12 份）中的 core-dyadic 覆盖 | 来源（该 cell 从哪来） |
|---|---|---|---|---|
| `HD-A01` | sibling | `KIN` | `ZERO_IN_AUDITED_CORPUS` | `19` A12 点名 + `CURRENT_ARCHITECTURE` §2 亲属 |
| `HD-A02` | parent–adult-child | `KIN` | `ZERO_IN_AUDITED_CORPUS` | 同上 + 照护 |
| `HD-A03` | other adult kin | `KIN` | `ZERO_IN_AUDITED_CORPUS` | `PARAM` §2.4 `kin` + §2 亲属 |
| `HD-A04` | non-romantic friendship | `FRIEND_NONROMANTIC` | `ZERO_IN_AUDITED_CORPUS` | `19` A12 + `PARAM` §2.4 `friendship` |
| `HD-A05` | romantic partnership | `ROMANTIC_PARTNER` | `PRESENT`（8 份） | `PARAM` §2.4 `romance` |
| `HD-A06` | ex-partner / post-termination | `EX_PARTNER` | `CRITERION_DEPENDENT` | `19` A12 + §2 前任 |
| `HD-A07` | professional / cooperative | `PROFESSIONAL_COOPERATIVE` | `PRESENT`（2 份） | `19` A12 + §2 同事/合作 |
| `HD-A08` | caregiving（角色方向不对称） | `CAREGIVING` | **`CRITERION_DEPENDENT_PARTIAL`**（见 §6.3.5） | `PARAM` §2.4 `caregiving` + §2 照护 |
| `HD-A09` | adversarial | `ADVERSARIAL` | `CRITERION_DEPENDENT` | `19` A12 + §2 敌对 |
| `HD-A10` | stranger start | any | `ZERO_IN_AUDITED_CORPUS` | `PARAM` §2.4 + `CONSTRUCT_SCOPE` §7 |
| `HD-A11` | established long-duration | any | `PRESENT`（2 份） | `PARAM` §2.4 + `CONSTRUCT_SCOPE` §7 |
| `HD-A12` | same-sex core dyad | any | `ZERO_IN_AUDITED_CORPUS` | `PARAM` §2.4 + `CONSTRUCT_SCOPE` §7 |
| `HD-A13` | mixed-sex core dyad | any | `PRESENT` | `PARAM` §2.4 + `CONSTRUCT_SCOPE` §7 |
| `HD-A14` | third party / multi-party present | any | `PRESENT`（3 份） | `CURRENT_ARCHITECTURE` §2 第三者 |
| `HD-A15` | structure nonconforming or illegal | any | `PRESENT`（2 份） | `CURRENT_ARCHITECTURE` §2 违法或违反社会规范 |

**`coverage` 一列的读法（三个值互不等价，不可互相折叠）：**

- `PRESENT` —— 本轨逐条复算 12 条 `core_dyad` 字段后，指出具名实例。
- `CRITERION_DEPENDENT` —— 存在**被点名**的候选实例，但该实例是否落入本 cell 取决于尚未写定的判据
  （例：`HD-A06` 的候选是 `L2-003` 叙述者↔「aged former lover」；`former lover` 是否计入 `EX_PARTNER` 取决于判据）。
  **既不是 `PRESENT`，也不是 `ZERO`。**
- `ZERO_IN_AUDITED_CORPUS` —— 在**本审计语料（12 份）内**未找到 core-dyadic 实例。
  这是**本审计语料内未找到**的**检索范围陈述**，**不是**「该语境在字段上不存在」的断言（X-14）。
- `HD-A01` / `HD-A02` / `HD-A04` / `HD-A12` 的零覆盖与 C-P7 层 2 点名的四类一致（`sibling` /
  `parent–adult-child` / `non-romantic friendship` / `same-sex`）；`HD-A03` / `HD-A10` 为本轨同一复算的附带结果。
- **在 §6.3.2 / §6.3.3 的逐 cell 判据被写定并跑过之前，不得把本列折算成任何 `n/12` 形式的覆盖率数字**（§6.3.5）。

#### 6.3.3 Table B — construct-decoupling adversarial patterns（**对抗模式**）

**与 Table A 分母不同，永不合并。** 每 cell 须有 `construct_pair`、行为定义、pass/fail 语义。

| cell_id | pattern（行为定义） | `construct_pair` | 来源 |
|---|---|---|---|
| `HD-D01` | 单向浪漫吸引：一方有、另一方无 | `RomanticAttraction`（i→j vs j→i） | `PARAM` §15 Gate B `unilateral attraction` |
| `HD-D02` | 高依赖 / 低喜欢 | `OutcomeDependence` × `Liking` | `PARAM` §15 Gate B |
| `HD-D03` | 高浪漫吸引 / 低信任 | `RomanticAttraction` × `Trust` | `PARAM` §15 Gate B（**归属已修正，见 §6.3.4**） |
| `HD-D04` | 有喜欢、无浪漫吸引 | `Liking` × `RomanticAttraction` | §4 D1 明文「可以喜欢但无 romantic attraction」 |
| `HD-D05` | 有性欲、无恋爱意愿 | `SexualDesire` × `RomanticAttraction` | §4 D2 明文「性吸引但无恋爱意愿」 |
| `HD-D06` | 强吸引 / 低依恋安全感 | `RomanticAttraction` × `AttachmentSecurity` | §4 D5 明文「强吸引但低 security」 |
| `HD-D07` | 仅因孩子 / 财产 / 法律留下 | `Dedication` × `Constraint/Agreement` | §4 D7 明文 |
| `HD-D08` | 有照护意愿、无投入承诺 | `Caregiving` × `Dedication` | §15 Gate C `Caregiving vs Dedication` |
| `HD-D09` | 高 PPR / 低 Trust | `PPR` × `Trust` | §5 B1 + §15 Gate C |
| `HD-D10` | 有共享「我们感」但无互惠有向状态 | `Cohesion/We-ness` × 双向 directed state | §6 P1 + §15 Gate C |

**Table B 逐 cell pass/fail 语义（与 Table A 的差别必须保留）：**

| cell 状态 | Table B 的含义 |
|---|---|
| `PASS` | 该 cell 的实例**能在不合并两个构念、不新增构念的前提下**被表示，且四象限组合中该 cell 命名的那一象**被观测到** |
| `FAIL_DECOUPLED` | 该象限**未出现且不可构造** ⇒ 指向 §2.2 失败 ⇒ `MERGE` 候选（**弱证据**，§5 表 §2.2 行） |
| `FAIL_COLLAPSING` | 表示该实例**必须**把一个构念塌进另一个才能完成 ⇒ `redundancy hole` 诊断 ⇒ 交 Redundancy Gate（**不在本门签处置**） |
| `NOT_RUN` | 同 Table A |

#### 6.3.4 对原文枚举的四处更正 + 逐条去向

1. **一个 cell 的归属曾把构念映射到一个被 canonical 显式区分开的构念上。**
   `HD-D03`（`high-attraction/low-trust`）曾被归属到 §4 D4「可高**喜欢**低信任」。但 §4 D1 明写
   「可以喜欢但无 romantic attraction」，D2 明写可与 liking 解耦 ⇒ **`Liking` 不得顶替 `Romantic Attraction`**。
   本表的归属改为 `RomanticAttraction` × `Trust`。
2. **移除一个类目错误。** `harm-asymmetric` 是**不对称轴**，不是 dyad **型**。它从 dyad 型清单中删除；
   「角色方向不对称」只作为 `HD-A08` 的**修饰语**保留（照护 dyad 确有方向不对称的真实结构）。
   任何对称性**轴**（attraction / dependence / asymmetry / care）都不得作为 Table A 的一行。
3. **两个真 cell 曾在一张派生覆盖表里漏记。** `opposite-sex` 与 `non-kin` 在 canonical §15 Gate B 中存在，
   但在 PR #31 `17` 的 Gate B 覆盖表中被漏记。本表把它们**具名为两个独立 cell**
   （`HD-A13` = `mixed-sex core dyad`；`HD-A03` = `other adult kin`）。
   **同时记录**：那张覆盖表另含一个**非 Gate B cell** `work colleague`——它是 `HD-A07`
   （`professional / cooperative`）的一个角色实例，**不是**独立的抽样框，也不是解耦模式 ⇒ 不作为一行。
4. **原 11 项 cell 的逐条去向（可核）**：

```text
原 §15 Gate B 11 项
  same-sex                        -> HD-A12
  opposite-sex                    -> HD-A13          （派生覆盖表曾漏记）
  kin                             -> HD-A01 / HD-A02 / HD-A03
  non-kin                         -> HD-A03          （派生覆盖表曾漏记）
  friendship                      -> HD-A04
  romance                         -> HD-A05
  caregiving                      -> HD-A08
  conflict                        -> HD-A09（作为 adversarial 的一种；判据待写定）
  unilateral attraction           -> HD-D01
  high-dependence/low-liking     -> HD-D02
  high-attraction/low-trust      -> HD-D03（归属已修正，见上）
派生覆盖表多出的 work colleague   -> 不作为一行（是 HD-A07 的角色实例）
另加：harm-asymmetric             -> 移除（是不对称轴，不是 dyad 型）
本表新增（不在原 11 项内）：
  HD-D04 / HD-D05 / HD-D06 / HD-D07  来自 §4 D1 / D2 / D5 / D7 各自的「为什么保留」明文
  HD-D08 / HD-D09 / HD-D10          来自原 §15 Gate C 的三对构念解耦挑战
  HD-A14 / HD-A15                   来自 CURRENT_ARCHITECTURE §2 的 第三者 / 违法或违反社会规范
```

**新增行的理由（避免无据扩张）：** 原 11 项是**项目自身假说清单的复述**（`H-A4` 判 10/11 自产），
本身不是判据集；Table B 的 6 个新增解耦 cell 逐条来自 canonical **自己已写下的**「为什么保留」段落，
不是新造的假说。`HD-A14` / `HD-A15` 逐字来自 `CURRENT_ARCHITECTURE` §2 的域枚举。

#### 6.3.5 分母不存在的诚实记账

`H-A4` rec 4 与 `C-P2` 的强制限定，逐条保留：

1. **不存在有意义的单一分母。** 原 §15 Gate B 把 8 项抽样框与 3 项解耦模式混在一张清单里；
   本表拆成两表后，**仍不得**把两表相除或相加得到「覆盖率」。
2. **cell 判据未定义 ⇒ 任何覆盖计数不可锁定。** 在 §6.3.2 / §6.3.3 的逐 cell 判据被写定并跑过之前，
   不得发布任何 `n/12` 形式的覆盖率数字。
3. **`HD-A08`（caregiving）的覆盖是 criterion-dependent partial，不是 0。** 本审计语料中可见的近似实例：
   `L0-003`（23 年医患纵向）与 `L3-001`（care-control 家庭内控制）。`H-A4` 记录：把它记为 0 的那个说法
   **部分成因是权利 / 访问门，不是策展失败**。因此该 cell 记 `CRITERION_DEPENDENT_PARTIAL`，
   **不得**记 `ZERO_IN_AUDITED_CORPUS`。
4. **同族的 `NOT_RUN` 记录必须携带 `HOLD_REASON`**（`ACCESS_OR_RIGHTS` / `EVIDENCE_MISSING`），
   使「没采到」与「采不到」可区分。rights fail-closed 继续有效（裁决 §C item 7）。

### 6.4 `HD-ST-1` — 唯一的 Human-Dyad sampling taxonomy

`C-P7`：把三张互不相同的 cross-context 清单对齐到**一个**分类法，同时把**经验语料覆盖**留作**独立**的 benchmark matrix。

- 分类法**只声明抽样框**（测哪些 Human Dyad 语境），维度为
  `dyad_class` · `gender_composition` · `stage`；**不**声称任何语境可被表示。
- `gender_composition` 取值为 `SAME_SEX` / `MIXED_SEX` / `UNDECLARED`。
  **「不适用」的语义归属 applicability 轴**（C-P5，兄弟轨 D 拥有），
  本文**不**复制该轴的定义，以免出现第二份 SSOT。
- **对齐义务（四处必须同指 `HD-ST-1`）：**
  1. 本文 Table A（`HD-A01`…`HD-A15`）
  2. `docs/foundation/PARAMETER_CONVERGENCE_V0_1.md` §2.4
  3. `docs/foundation/CONSTRUCT_SCOPE_DIRECTIONALITY.md` §7 第 6 项
  4. `docs/foundation/CURRENT_ARCHITECTURE.md` §2 的研究域枚举 —— **该文件不属本轨白名单**，
     以提案交回（§9 P-2）。
- **经验覆盖是独立矩阵**：本审计语料对每个 `dyad_class` 的 core-dyadic 覆盖，
  记在 §6.3.2 `coverage` 一列，**不是**分类法的属性。

**X-10 双层记账（domain ≠ evidence）：**

```text
层 1（零成本，已在本轨完成）  文档对齐：四处清单同指 HD-ST-1
层 2（有成本，不在本轨）      经验语料覆盖：sibling / parent–adult-child /
                             non-romantic friendship / same-sex 在本审计语料内
                             零 core-dyadic 实例 —— 这需要采集，不是文档编辑
```

**域声明不是表示证据。** 本表 `coverage` 一列的 `ZERO_IN_AUDITED_CORPUS` 是**本审计语料内未找到**
的检索范围陈述，**不是**「该语境在字段上不存在」的断言（X-14）。

---

## 7. 处置台账（记录位置）

所有门的产出与处置落在**同一张台账**，避免多份竞争记录：

| 字段 | 内容 |
|---|---|
| `run_id` · `date` | 运行标识 |
| `gate` | `GATE_COVERAGE` / `GATE_MINIMALITY` / `GATE_CROSS_CONTEXT` / `GATE_REDUNDANCY` |
| `fixture_or_benchmark_ref` | 冻结 fixture 版本或独立 benchmark 标识 |
| `cell_id` | Table A / Table B 的 cell（跨语境门必填） |
| `construct` | 被判定的 §11 构念 |
| `mapping_outcome` / `diagnosis` / `discharge_status` | §3 的记录 |
| `disposition` | `KEEP｜MERGE｜DERIVE｜REJECT｜HOLD` |
| `disposition_fields` | `MERGE_TARGET` / `DERIVATION` / `HOLD_REASON` / `REENTRY_CRITERION`（按 §2.3） |
| `executor` | 指定执行者 |
| `evidence_ref` | 指向 Case Bank `#13` 或冻结 fixture 的锚 |

**当前台账内容：无。** 本文件构建之时尚未运行任何门。
**明确记录：按 §2.3 的 K1–K4，在 construct-bearing benchmark 存在之前，§11 的任何构念都**无法**被签 `KEEP`；
今日可达的最高处置是 `HOLD / BENCHMARK_NOT_BUILT`。**这不是失败结果，是前置条件的诚实记账。**

---

## 8. 拒设阈值登记（Decined-threshold register）

裁决 C-P1：**Do not invent arbitrary N-fixture numeric thresholds yet.** dispatch R3-C 第 4 条同义。
下表逐条登记**拒绝设定阈值**的位置与理由，并给出**什么证据能产生一个阈值**。

| # | 位置 | 拒设的阈值 | 为什么拒设 | 什么证据会产生一个阈值 |
|---|---|---|---|---|
| 1 | `GATE_COVERAGE` 通过判据 | 「至少 N 个 fixture」 | C-P1 明令；且 N 与表示能力无推导关系 | 一个**已论证**的 fixture 集合与目标构念的对应关系（哪些 dyad_class 必须被覆盖），加上每 class 的实例数下限 |
| 2 | §2.1 Semantic independence | 语义独立性的数值下限 | 独立性是**对当前 basis 的语义判断**；任何数字会随 basis 变化而改变含义 | `construct-bearing` 材料上的固定 witness 集 + 预注册的「可接受附带变化」计数 |
| 3 | §2.2 Counterexample decoupling | 每 cell 的反例数下限 | 这是**benchmark 阈值**不是**门阈值**；目前**不存在**任何 construct-bearing 外部语料 | 一次独立采集，产出预注册的每 Table B cell 最少实例数 |
| 4 | §2.3 Conditional incremental information | 最小方差 / 解释增量 | 无冻结模型、无测量方案；任何数字都是**未验证阈值**，违反 `AGENTS.md` 研究纪律 | 一个被裁定的测量方案 + 明确的报告指标 + 该指标的可靠性下限 |
| 5 | §2.4 Scope stability | 需要通过的 cell **比例** | 逐 cell 判据已给；比例会重新引入 C-P2 禁止的单一分母。**结构性零 N 已给**（无 `UNSTABLE` 且无 `NOT_RUN`） | 若将来决定允许部分 `NOT_RUN`，需要一个有论证的最小覆盖集；本轮**不**设 |
| 6 | §2.5 Layer test | — | **不适用**：判据是类别型的。设数值会允许「大体上是 proxy」通过为 primitive | 不需要 |
| 7 | §2.6 Representation necessity | 跑几份 fixture 才算跑过 | 同 #1 | 同 #1 |
| 8 | `GATE_REDUNDANCY` 处置 | 累积多少 ablation 证据才可 `MERGE` / `REJECT` | C-P1 说 ablation 证据**累积**；给数字即等于发明任意普适阈值 | 一次预注册的效力分析（需要 construct-bearing 材料才有意义） |
| 9 | `GATE_CROSS_CONTEXT` | 跨 cell 的通过比例 | C-P2 明令两表不合并、不设单一分母 | 不设 |
| 10 | `VALIDATION_CORPUS_V0_1` 的 `HIGH / MEDIUM-HIGH / LOW` 泄漏标注 | 把它升格为门阈值 | 那是 2026-09-11 采集期的**策展启发式**，不是门判据 | 不设；保留为历史采集标注 |

**已给出的阈值共三处，全部标为「结构性」**（由门/判据的成功定义直接推出，不是选定的数字，
且都**不是** N-fixture 型阈值）：

1. `GATE_COVERAGE` 的「`MAPPING_FAILURE` = 0 且未结清 catch-all = 0」（§6.1）；
2. §2.4 的「无 `UNSTABLE` 的 `RUN` cell 且无 `NOT_RUN` cell」（§5 表）；
3. §2.6 / K2 的「necessity ≡ 至少 1 个 witness 降级」（§5 表 / §2.3）。

**除此之外，本轨没有在任何门或判据上写入数字。**

---

## 9. `proposals_addressed_to_other_files`

本轨**不编辑** `AGENTS.md` 与 `docs/foundation/CURRENT_ARCHITECTURE.md`（兄弟轨 D 所有）。
以下为逐字提案，请 parent 路由。

### P-1 → `AGENTS.md`（Validation discipline，第 62 行）

**现状**：该行是 `PARAMETER_CONVERGENCE` §13 诊断清单的**逐字镜像**。§13 增加了 `redundancy hole`
与条件式叙事出口后，**只改一侧会造成 canonical 内部冲突**（`I-C12` 已证明本项目发生过一次同类文档级冲突）。

**提案替换文本**（诊断清单 8 项 + 条件式出口）：

```text
- Record unmappable material as `MAPPING_FAILURE`; Architect diagnoses whether the failure is
  ontology hole, construct hole, scope hole, temporal/history hole, belief/observation hole,
  measurement hole, redundancy hole (a unit losslessly representable by <k>, so <m> is unnecessary),
  or — only as a conditional and logged discharge — merely narrative/irrelevant, which requires
  a recorded relation-relevance reason **and** a demonstrated unmappability, and is counted apart
  from failures, never merged into them.
```

### P-2 → `CURRENT_ARCHITECTURE.md` §2（研究域与最小对象）

**提案**：在 §2 的域枚举之后追加一句指向分类法与双层记账，不改动枚举本身：

```text
The canonical sampling-frame taxonomy for cross-context validation is `HD-ST-1`
(`docs/foundation/VALIDATION_GATES_V0_2.md` §6.4). Domain declaration is **not** representation
evidence: empirical corpus coverage is tracked in a separate benchmark matrix, and
`sibling` / `parent–adult-child` / `non-romantic friendship` / `same-sex` have zero core-dyadic
instances in the audited corpus (a search-scope statement about that corpus, not a field-wide
absence claim).
```

### P-3 → `PARAMETER_CONVERGENCE_V0_1.md` §9（`R1` / `R2` / `R5`）与 §2.3 / §2.6 交叉引用

§9 与 §11 不在本轨白名单（本轨只拥有 §2.1–§2.6、§13、§14、§15；§9 与兄弟轨 D 的 §9 R3 相邻）。
**提案**：在 §9 `R1` / `R2` / `R5` 与 §11 basis 清单附近各补一句交叉引用：

```text
`DERIVE` / `MERGE`（终局处置，见 VALIDATION_GATES_V0_2 §2.3）是本文 §9 R1 / R2 / R5 的执行面落点；
两者必须使用同一「同义（MERGE）」与「可计算派生（DERIVE）」的区分，不得互相改写。
§11 的任何条目被移出或降级，必须经 GATE_REDUNDANCY 签发处置，不得直接删改本文。
```

### P-4 → `PARAMETER_CONVERGENCE_V0_1.md` §4 D7 / §5 B1 / §9 R3

这三节由兄弟轨 D 所有（§4 D4/D5、§5 B1、§9 R3）。**本轨不编辑。** 相关待路由项：

- `DERIVE` 处置的存在意味着 §9 `R1`（`Mutuality_k`）类条目**现在有执行语义**（原 §15 无处置动词）。
- X-3 后果预登记若落地，`Dedication` 的 basis 地位需重新审议时，**必须**经 `GATE_REDUNDANCY` 签发
  处置，不得直接删改 §11。
- X-4（`Trust` / `AttachmentSecurity` 分列、`domain` 为可选 facet）**不产生** Gate 处置：
  它是架构裁决，不是 ablation 结果。门**不得**用它做 MERGE 依据。

---

## 10. Supersession ledger（本轨自身的取代关系）

| 原文 | 位置 | 被什么取代 | 依据 |
|---|---|---|---|
| `Gate A — Court-fact sentence coverage` 五步 | `PARAMETER_CONVERGENCE` §15 | `GATE_COVERAGE` + `ARM-ABL-1` baseline arm | C-P1；H-A2（承诺未兑现、缺的是臂） |
| `Gate B — Cross-context counterexamples` 11 项单表 | 同上 | Table A `HD-A01…HD-A15` + Table B `HD-D01…HD-D10`（两表、无单一分母） | C-P2；H-A4 |
| `Gate C — Redundancy challenge` 六对 | 同上 | `GATE_MINIMALITY`（判冗余）+ `GATE_REDUNDANCY`（签处置） | C-P1 |
| 「通过后，才有资格把 v0.1 candidate 推向 `Minimal Sufficient State v0.1`」 | 同上 | §2.3 的 5 值终局处置 + K1–K4 | C-P1（4 值扩展为 5 值的 delta 见 §2.2） |
| §2.4 的 8 项 cross-context 内联清单 | `PARAMETER_CONVERGENCE` §2.4 | `HD-ST-1` 引用 | C-P7 |
| §7 第 6 项的 6 项 cross-context 内联清单 | `CONSTRUCT_SCOPE_DIRECTIONALITY` | `HD-ST-1` 引用 | C-P7 |
| §13 的 10 类落点表 | `PARAMETER_CONVERGENCE` §13 | `LHRM-LANDING-1`（10 落点类 + 3 状态位） | C-P1 项 7 / `ADJ3` rec 7 |
| §2.5 的 10 层内联清单 | `PARAMETER_CONVERGENCE` §2.5 | 同上（同指 `LHRM-LANDING-1`） | 同上 |
| §14「第一轮 Case Bank test 只要求**语义有合法落点**」 | `PARAMETER_CONVERGENCE` §14 | §3.1 的 `catchall_used` + fail-closed 默认 | H-A3 机制 (3) |

**历史文本一律保留**：被取代的 §15 Gate A/B/C 原文保留在 `PARAMETER_CONVERGENCE` §15 的 `SUPERSEDED` 块内；
被取代的 §13 落点表与 §2.5 清单保留在该两节内的 `SUPERSEDED` 注释中；本文不删除任何一行旧证据。

---

## 11. `explicit_non_claims`

1. **未运行任何 Gate。** 本文不含任何 mapping 结果、任何计数、任何 cell 状态。
2. **未验证任何构念的必要性。** Fixture 001/002/003 未被用作八项 basis 的证据（X-9）。
3. **未构建 construct-bearing benchmark。** 该 benchmark 由兄弟轨规划，本文只规定它必须满足什么。
4. **未引入任何新构念、值类、transition law、权重、距离或分数。** 本文只写门怎么跑。
5. **未设任何普适数值阈值。** 全文只有三处「结构性」条件，且都不是 N-fixture 型（§8 末）。
6. **未声称消除了 catch-all 类。** 由 4 降为 3，且仍以 fail-closed 方式受约束（§3.1）。
7. **未声称 `MAPPING_FAILURE` 已「可达」到有实证产出。** 只声称**类型上可达**（§3）。
8. **未裁定任何构念的层归属、applicability、observability。** 那些属兄弟轨 D 的文件。
9. **未合并、未 push、未开 PR。** 交付形式 = branch + commit + packet。
10. **未读取 / 未执行 / 未引用 `#20` / `#21` / `#22`。**
11. **未对 Fixture 003 的权利边界作任何新的判断。** 只引用 canonical 已记录的
    `rights_policy=HUMAN_REVIEW_REQUIRED` / pointer-only fail-closed 状态，不定义、不修改其行为。
