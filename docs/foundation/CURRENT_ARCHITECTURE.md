# LHRM Current Architecture

**Status:** CURRENT canonical architecture snapshot  
**As of:** 2026-09-10  
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
