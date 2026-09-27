# LHRM Current Architecture

**Status:** CURRENT canonical architecture snapshot  
**As of:** 2026-09-10（2026-09-28 增补 §3.1 / §4.1 / §4.2 / §6.1 / §9.1；权威 = `youling/lhrm#30` `ARCHITECT_ADJUDICATION_V1`，comment `5854920569`）  
**Project:** Li-Hong Relationship Model / 礼宏关系模型  
**Scope:** Human–Human relationship state representation  

> 本文件是当前架构入口。旧的阶段总结继续保留作历史 provenance，但发生冲突时以 Human 当前方向、GitHub 最新 durable ruling 与本文件的 current snapshot 为准。

---

## 1. 当前第一目标

LHRM 第一阶段不以“算出一个恋爱分数”“给一段关系下唯一结论”或“预测所有关系结局”为目标。

当前首要目标是：

> **建立一套能够在任意时刻，对两个具体人及其关系进行结构化、方向化、时间索引、保留 Unknown 与不确定性的数学状态表示语言。**

方法原则：

```text
Representation before scalarization.
State-space before score.
```

更严格地说：

```text
Raw evidence
-> loss-aware / uncertainty-preserving canonical representation
-> relationship state trajectory
-> optional downstream query / prediction / simulation / decision
```

任何 distance、score、probability、recommendation 都是对既有状态空间的 readout，不是 LHRM 本体。

---

## 2. 研究域与最小对象

研究域冻结为 **Human–Human relationship system**。

最小对象：

```text
HumanDyad(i,j)
= Person_i + Person_j + Relationship_ij
```

边界：

- 不预设异性、陌生起点、婚恋目标；
- 允许亲属、朋友、同事、前任、伴侣、第三者、敌对、照护、合作、违法或违反社会规范等现实存在的关系结构进入描述；
- 动物、神经、遗传、进化研究只作为 mechanism evidence，不扩展 LHRM 的研究域；
- 合法性、道德性、社会赞许度、伤害与关系状态分层描述，互不替代。

原则：

> **向下追机制，但不向下扩研究对象；向外看 context，但 Human Dyad 仍是最小关系查询单元。**

---

## 3. 世界层与局部投影

LHRM 不再把 `S / O / D / E` 当完整世界本体。

较稳定的世界表达是：

```text
WorldState(t)
= Agents(t)
+ Relationships(t)
+ Environment(t)
```

为处理欺骗、隐瞒、误解、想象、未知与信息更新，还必须分开：

```text
Reality != Observation != Belief
```

针对具体二人关系的局部查询，再做：

```text
X_(S,O,t) = Phi_(S,O)(WorldState(t))
```

`S / O / D / E` 当前解释为 query-local view：

- `S` — 当前主体；
- `O` — 当前对象；
- `D` — 当前二人关系；
- `E` — 当前问题相关的外部环境。

`Role` 不是世界状态本身，而是“当前到底在问什么”的 query lens。

### 3.1 层归属裁决（已定，2026-09-28）

依 `youling/lhrm#30` `ARCHITECT_ADJUDICATION_V1`（comment `5854920569`）X-1 / X-3 / X-4 与 ruling §C item 1–2。**这些是当前架构，不是开放问题。**

```text
PPR_(i about j,t)        layer = BeliefState（关系特定知觉），已定
Satisfaction_i(t)        layer = Derived / evaluation-state candidate，已定
Trust_(i->j,t)           与 AttachmentSecurity_(i->j,t) 暂时保持为两个独立 candidate
```

- 一个 belief 可以有**时间持续性**与**因果 / 动态重要性**，而**不因此**成为 Reality / `DirectedRelationshipState` 坐标。
- 「organizing variable」、持续性或预测强度**本身不蕴含** Reality-state 成员资格（X-2：层归属不可由预测强度重开）。
- `Satisfaction_i(t)` 的提升是**条件式且预登记**的，**绝不**由预测强度隐含推出。后果预登记见
  `PARAMETER_CONVERGENCE_V0_1.md` §9 `R3`；**本节不预判提升是否发生，也不改写 `§4 D7`。**

---

## 4. 二人关系的方向性

关系不是一个无方向总分。

当前首选表示：

```text
Relationship_ij
= DirectedState_(i->j)
+ DirectedState_(j->i)
+ PairState_(i,j)
```

凡是“某个人对另一个人”的状态，优先建成有向分量：

```text
Z[k, i, j, t]
```

其中：

- `k` = construct family；
- `i` = source / perceiver / actor；
- `j` = target / recipient；
- `t` = time/history coordinate。

因此：

```text
SexualDesire(A->B) != SexualDesire(B->A)
Trust(A->B) != Trust(B->A)
Dedication(A->B) != Dedication(B->A)
```

“双方都有”“互相喜欢”“不对称程度”等优先由两个方向派生，不重复设 primitive。

#### 4.1 派生 readout 的形式约束（2026-09-28）

**先修一处形式缺陷。** 此前 canonical 把不对称读出写成

```text
Asymmetry_k(A,B) = distance( Z[k,A,B], Z[k,B,A] )
```

该形式**与 representation-first invariant 4 冲突**（不强迫进入 `0..1` / 欧氏 / 同一共同尺度），
因为 `distance` 对 `interval` / `ordinal` / `category` / `distribution` / `Unknown` **未定义**。
**本形式被取代。** 取代关系登记在 `MEASUREMENT_SEMANTICS_V0_1.md` §5；
该行原文位于 `CONSTRUCT_SCOPE_DIRECTIONALITY.md`（**兄弟轨 `C` 所有，本轨不改**），
本轨**不删该行**，只在本文记取代；该文件的同步修改已路由（见 `MEASUREMENT_SEMANTICS_V0_1.md` §5）。取代形式：**不假设度量的成对读出**。

```text
AsymmetryReadout_k(A,B)
=
{
  left,        # Z[k,A,B]，原样保留（区间/序数/类别/分布/Unknown 皆可）
  right,       # Z[k,B,A]，同上
  comparison,  # 显式声明的 comparator 读数；未声明时为 NOT_AVAILABLE
  comparator_id,# 该 comparator 的注册 id；未声明时为 NOT_AVAILABLE
  evidence,
  uncertainty
}
```

`comparison` 只有在**已注册的 comparator** 存在时才允许；`comparator_id` 指向该注册项。
本轨**不设**任何 comparator、任何权重、任何距离度量和任何数值阈值。

#### 4.2 Power readouts（X-13 / C-P4，已定）

**不存在独立的普适 Power primitive。**

```text
TotalDependence_(A,B) / TotalPower_(A,B)
  = 双方 dependence / capacity 项的【对称派生聚合】

RelativePower_(A,B) / PowerImbalance_(A,B)
  = 【方向性 / 不对称派生读出】
```

- **`TotalPower` 的实现形式必须是对称聚合**（对两侧 dependence/capacity 项的聚合，例如求和型），
  **不是** relational cohesion。此前把 Lawler 的 relational-cohesion 规格当成 total-power 规格，属实现规格错误。
- **Relational cohesion 是 `TotalPower` 与 `RelativePower` 之间的一个关系 / 过程量，
  不是 `TotalPower` 的定义。**
- `RelativePower` / `PowerImbalance` 与 §4.1 的成对读出同族：同一条 asymmetric 读出，
  不得假定两侧可度量。
- **R2-b 槽位（punitive capacity、legitimacy / bases、perceived power、felt compliance）不加入**，
  状态为 `HOLD_FOR_EVIDENCE`。它们**不得**因「三分判定已被逐字核实」而被一并视为已确立。

---

## 5. Construct family across scopes

同一个日常名称不意味着只能出现在一个位置，也不意味着所有位置必须机械复制。

对构念族 `k`，允许检查：

```text
Construct.source_i
Construct.target_j
Construct.edge_(i->j)
Construct.pair_(i,j)
```

例如 attraction family 可以包含：

- source/perceiver component：某人一般多容易被吸引；
- target component：某人一般多容易诱发他人吸引；
- edge component：特定 i 对特定 j 的特殊吸引；
- pair-derived mutuality：由两个方向组合出来的互惠/不对称模式。

但并非每个构念都四项齐全。只有独立语义存在、可解耦、可操作时才保留。

详见：`docs/foundation/CONSTRUCT_SCOPE_DIRECTIONALITY.md`。

---

## 6. State / Action / Belief / Constraint 分离

核心模型不采用预写关系状态机作为关系演化发动机。

当前动力学接口是：

```text
CurrentState
+ Action/Event
+ Belief
+ Constraint
+ Environment
-> NextState
```

概念上：

```text
State != Action
State influences ActionPolicy
Action/Event updates State
```

例如：

- “肯花钱”首先是 action / observable，不自动等于 attraction、care 或 dedication；
- “订婚前不发生性行为”更接近 Agent boundary / constraint，而不是“性欲为零”；
- 已婚/订婚/同居等可以是制度事实、协议或 pair state，但不能反过来替代底层关系状态；
- Relationship label 是更高层的 coarse-graining，而不是底层 primitive。

#### 6.1 `InformationAction` family（2026-09-28，C-P11）

**这是 Action/Event 的动作词表，不是新的 state primitive。**

```text
InformationAction_(i->j, t, info_ref, action_ref)
  action ∈ { Disclose, Withhold, Misrepresent }
```

- **`Disclose`** —— i 就某个具名信息项向 j 发生了一次披露动作。
- **`Withhold`** —— **仅当**信息项**与**相应的机会 / 预期**同时显式**时才成立
  （`info_ref` 存在 **且** `opportunity_or_expectation_ref` 存在）。缺任一项 ⇒ **不是 `Withhold`**。
- **`Misrepresent`** —— i 就该信息项对 j 作出一次不实陈述。

**为什么「不披露」不是信息缺口。** 非披露**不是**一个 information gap，而是**关于一个 `Behavior` 的断言**；
它需要第三个输入「`i` 确实有东西没披露」，而该输入只能来自 action / event 记录，**不能**是 belief 层的字段。
把 `NonDisclosure` 写成 belief 层的一个 latent 字段，等于把「他没说」当作关于他内心的事实。

**单纯的沉默 / 缺席不自动是 Action。** 「j 没有问」「i 没有说」在缺少
`opportunity_or_expectation_ref` 时，记为**无 action 记录**（可留 `HISTORY` / `PROVENANCE` 记录），
**不得**记为 `Withhold`，**也不得**记为 `NonDisclosure = true`。

**为什么落在 Action/Event 而不是 Constraint。** canonical 已有先例并给出判据：
「订婚前不发生性行为」更接近 Agent boundary / constraint，而不是「性欲为零」。
即：**「不做某事」若由一条具名边界 / 约定支配，它归 `Constraint/Agreement`；
若由一次具体情境下的取舍或机会支配，它归 `Action/Event`。**
`Withhold` 属于后者——它是一次**在机会面前的动作**，不是一条常设边界。

**本条不引入新构念、不引入 belief 层字段、不引入 `disclosure` 坐标。**

核心不走：

```text
state label + event -> lookup next state
```

而走实时演算：

```text
X_(t+1) = F(X_t, Action_t, Event_t, Belief_t, Constraint_t, Environment_t)
```

---

## 7. 低冗余不等于低动态耦合

LHRM 寻找的不是统计上互不相关的变量，而是 **低语义/条件冗余的状态基**。

两个 construct 可以语义独立，同时在转移中强耦合：

```text
partial F_i / partial z_j != 0
```

例如花钱行为可能经由 motive attribution / perceived care / responsiveness 等路径改变 attraction 或 trust，但这不意味着 spending 与 attraction 是同一个 primitive。

参数收敛关注：

- semantic independence；
- counterexample decoupling；
- incremental information；
- conditional redundancy；
- intervention independence。

---

## 8. 时间、轨迹与历史分支

LHRM 的核心产物优先是动态状态轨迹：

```text
Gamma_(A,B)
= { X_(A,B)(tau) }
```

`tau` 不必永远是单一线性标量，可扩展为：

```text
tau = (history_id, local_time)
```

从而表示带 lineage 的历史版本图 / DAG。

在复杂叙事中：

- 现实历史可 fork；
- 平行历史可并存；
- 某条新历史可以被选为 active/main lineage；
- 旧历史不需要“合并回真相”，保留 provenance 即可。

梦境、幻想、计划、回忆重构、反事实等不必污染真实 WorldState，可以作为某个 Agent 的 Belief / simulated world 内的 nested model：

```text
SimWorld_(Agent,m)
= fork(BeliefState_A, mode)
```

其结果再通过 belief / emotion / action-policy 更新影响现实。

因此不需要专门增加“穿越参数”“梦境参数”；复杂性由 history / belief / environment 的组合表达。

---

## 9. Measurement / Canonicalization 的原则

当前尚未冻结统一尺度、权重或归一化公式。

先保留：

```text
RawObservation
-> CanonicalRepresentation
-> ModelState
```

原则：

1. 原始事实不因归一化而删除；
2. 可计算范围不等于共同语义尺度；
3. 不强迫所有变量进入 `0..1`；
4. category、ordinal、continuous、constraint、probability、Unknown 可以共存于混合状态空间；
5. 自然语言 proxy 可通过 fuzzy membership、ordinal model、posterior distribution 等方式提供 evidence，但不必强制 defuzzify 成精确单值；
6. 一个 latent coordinate 可以表示成 estimate + uncertainty + evidence/provenance，甚至直接保存 posterior distribution。

Fuzzy / normalization / distance 等技术可以作为 measurement/readout 工具，但不拥有定义 LHRM 本体的优先权。

### 9.1 两条已登记的 measurement / representation 语义（2026-09-28）

> **本节只引用，不复制。** schema 与规范词表的 SSOT 在
> `docs/foundation/MEASUREMENT_SEMANTICS_V0_1.md`；门的诊断 / 处置 / 流水线 SSOT 在
> `docs/foundation/VALIDATION_GATES_V0_2.md`。本文不重复它们，避免第二份竞争 SSOT。

**(a) 值域是许可式（permissive），不是封闭枚举**（X-5）。

- 第 4 条原则的清单是**许可式**（`可以` / `may be`）；canonical **没有任何**封闭性声明。
- 「此构念在该 dyad / 语境中不具独立意义」**既不是 `0`，也不是 `Unknown`**。
  它登记在**与值域正交**的 applicability 轴上：`applicability ∈
  { APPLICABLE, NOT_APPLICABLE_BY_RULE, APPLICABILITY_UNKNOWN }`，
  配 `applicability_reason` / `applicability_provenance`。
- 该轴**不得**折进 `Unknown` 的值枚举、**不得**加进坐标值域、值域内**不得**出现 `NA`。
- schema 与全部字段语义：`MEASUREMENT_SEMANTICS_V0_1.md` §2。
- `AGENTS.md` representation-first invariant 第 5 条的坐标类型清单**同样是许可式**；
  是否在该处加一句显式许可式声明，**不由本轨改**（`AGENTS.md` 镜像义务只覆盖 diagnosis 清单那一条），已路由 parent。

**(b) Observability registry 是未满足的前置条件，不是已完成项**（X-4 / C-P13）。

- 项目**至今没有**一份「哪些构念原则上可被直接观察 / 只能自陈 / 只能由对方报告 / 只能推断 / 结构性不可观察」的清单。
- 因此 belief 层对 `g = FIRSTHAND` 与 `structurally_unobservable` 的赋值**今天无法落地**；
  它同时阻塞：Unknown 类型学落地、refinement 程序的依赖表、belief 层本身，以及研究侧已局部提出的单构念登记。
- schema 与已填充骨架（含诚实完整性标记）见 `MEASUREMENT_SEMANTICS_V0_1.md` §3。
- 逐构念内容由兄弟轨 `F` 交付（Track R3-F）。**本节是依赖登记，不是结论。**

---

## 10. Case Bank 与表示完备性验证

长期 benchmark lane：`#13`。

Case Bank 不用于估计 population base rate，而用于：

```text
completeness
closure
representation coverage
regression
adversarial stress test
```

第一优先来源是事实链丰富、可复核的法院/官方材料；但来源等级与事实状态分开：

```text
provenance quality != fact status
```

法院文书中的事实需区分：

```text
adjudicated | admitted | alleged | disputed | unknown
```

验证协议的核心不是“让模型解释整个故事”，而是逐句测试：

```text
sentence / event
-> valid LHRM mapping ?
```

映射失败必须记录，不先加特例参数。

法院/纪实材料主要做 empirical coverage test；小说、志怪、科幻玄幻可做 expressivity stress test。虚构世界规则优先进入 Environment / History，而不污染 Human relationship primitives。

---

## 11. 当前非目标

当前明确不冻结：

- 单一 LoveScore / CompatibilityIndex；
- 统一欧氏距离；
- 统一权重表；
- 所有维度统一 `0..1`；
- 预写关系状态机；
- 任意产品的闭源“匹配分”；
- 从单个案例估计现实概率；
- 把高层 proxy 直接当 primitive；
- 把神经/基因机制因“更底层”自动升级为 relationship state。

---

## 12. 当前工程顺序

```text
1. Parameter Convergence
2. Candidate Minimal Sufficient State
3. Representation coverage regression
4. Measurement & Canonicalization
5. State transition / dynamics
6. Longitudinal parameter estimation & validation
7. Optional prediction / readout / simulation / decision layers
```

当前正在从第 1 步进入第 2 步。

候选收敛见：`docs/foundation/PARAMETER_CONVERGENCE_V0_1.md`。
