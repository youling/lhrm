# Parameter Convergence v0.1

**Status:** CANDIDATE / NOT FROZEN  
**As of:** 2026-09-10  
**Parent:** `youling/lhrm#2`  
**Inputs:** Games #3 + Scientific #4 + Dating Apps #5 + Real-world #6 + current architecture rulings  
**Purpose:** 从四源 Research 的发散候选中，第一次正式收敛一组低语义冗余、方向明确、适合动态状态表示的 candidate basis，并明确哪些东西不应进入 relationship-state primitive。

> 本文不是最终参数表。它的职责是减少候选、暴露争议、给第一轮 representation coverage regression 一个可运行的 schema。任何数值尺度、权重、距离、概率或转移函数均未冻结。

---

## 1. 收敛目标已经变化

最早的参数研究隐含目标是：找到一组变量后计算某种匹配/距离。

当前目标已改为：

> **寻找一组足够小、语义稳定、可方向化、可时间更新的状态坐标，使任意 Human Dyad 在任意时刻的关系相关事实都能被表示。**

因此 parameter convergence 优先回答：

```text
What state is this?
Where does it live?
Who is it about / directed toward?
How is it observed?
What is derived rather than primitive?
```

而暂不回答：

```text
What is its 0..1 value?
What weight does it get?
What is the final score?
```

---

## 2. 收敛判据

候选 construct 要进入 Minimal Sufficient State，至少接受以下审计：

### 2.1 Semantic independence

是否具有不能被现有 construct 无损替代的独立语义？

### 2.2 Counterexample decoupling

现实中能否稳定出现：A 高、B 低；A 低、B 高？

若无法构造或观察解耦反例，可能属于同一 latent state 的重复命名。

### 2.3 Conditional incremental information

已知其它候选后，该 construct 是否仍可能为当前状态或未来转移提供额外信息？

### 2.4 Scope stability

在 same-sex / opposite-sex、kin / non-kin、stranger / established relationship、romance / friendship / caregiving / conflict 等语境下，语义是否保持稳定？

### 2.5 Layer test

候选究竟属于：

```text
Agent attribute/state
Directed relationship state
Pair property/state
Belief/perception
Action/Event
Constraint/Agreement
Environment
Observable proxy
Derived readout
Mechanism evidence
```

如果只是行为、标签、结果或 proxy，不因常见就升级为 primitive。

### 2.6 Representation necessity

若删除该 construct，是否会存在重要现实句子/状态无法用剩余 schema 合法表示？

这项将在 Case Bank regression 中直接测试。

---

## 3. 顶层 state container 先于 primitive list

当前 Candidate State Snapshot：

```text
DyadSnapshot_(A,B,t,h)
=
{
  AgentState_A,
  AgentState_B,
  DirectedRelationship_(A->B),
  DirectedRelationship_(B->A),
  PairState_(A,B),
  BeliefState_A,
  BeliefState_B,
  RelevantEnvironment,
  ConstraintsAndAgreements,
  ProvenanceAndUncertainty
}
```

其中 `h` = history / lineage id。

这不是“九个同级心理参数”，而是容纳不同类型状态的 schema。

---

## 4. 第一组高置信 Directed Relationship candidates

以下 construct 在科学研究、游戏形式化、现实反例和本项目压力测试中均表现出较强的独立性。它们是 **第一轮 KEEP candidates**，但仍待 Case Bank / measurement validation。

### D1. Liking / Affiliative Valence

**语义：** i 对 j 的一般积极/亲近性评价与喜欢程度，不预设浪漫或性。

```text
Liking_(i->j,t)
```

为什么保留：

- 可以喜欢但无 romantic attraction；
- 可以 sexual desire 高但一般 liking 低；
- 朋友/亲属/同事均适用。

不等于：

- relationship satisfaction；
- romantic attraction；
- sexual desire。

### D2. Romantic Attraction

**语义：** i 对 j 的浪漫伴侣式特殊吸引/趋近倾向。

```text
RomanticAttraction_(i->j,t)
```

为什么保留：

- 可与 liking、sexual desire 稳定解耦；
- 适用于单向浪漫、无性浪漫、性吸引但无恋爱意愿等反例。

### D3. Sexual Desire

**语义：** i 指向 j 的性欲/性接近动机。

```text
SexualDesire_(i->j,t)
```

为什么保留：

- 方向性极强；
- desire 与 behavior、identity、orientation 必须分离；
- 可与 romantic attraction / liking 解耦。

### D4. Trust

**语义：** i 在关系中愿意把某类脆弱性暴露给 j、并预期 j 不会利用/伤害该脆弱性的关系性信任状态。

```text
Trust_(i->j,t)
```

为什么保留：

- generalized trust（Agent tendency）与 target trustworthiness 不能替代特定 dyadic trust；
- 可高喜欢低信任，也可低喜欢高制度性信任。

**Open question:** `Distrust` 是否应作为独立 construct，而不是 `1 - Trust`，保留待测。

### D5. Attachment Security / Felt Security

**语义：** i 在与 j 的关系中是否预期对方可获得、可依赖，并在需要时形成相对安全的依恋感。

```text
AttachmentSecurity_(i->j,t)
```

为什么保留：

- 与喜欢/浪漫/性欲不同；
- 可出现强吸引但低 security、低浪漫但高 attachment/security 的长期关系。

**Open question:** attachment security 是否应拆成更细 facet，暂不做。

### D6. Caregiving Motivation / Care Orientation

**语义：** i 指向 j 的照护、保护、减轻对方痛苦/负担的关系性动机或持续倾向。

```text
Caregiving_(i->j,t)
```

为什么保留：

- 照护行为不等于 caregiving state；
- 可出现在亲子、伴侣、朋友、非亲缘长期照护；
- 与 romantic/sexual attraction 可独立。

**边界：** 做饭、陪诊、接送、转账是 Action/Observation；是否由 caregiving、duty、control、exchange 等动机产生，需要 Belief/attribution 处理。

### D7. Dedication

**语义：** i 主动希望维持、维护并继续该关系的内在关系性承诺/投入意愿。

```text
Dedication_(i->j,t)
```

为什么保留：

- Investment Model 明确提醒 commitment 不能与 investment、constraints、alternatives、satisfaction 混为一体；
- dedication 可与“因为孩子/财产/法律而留下”的 constraint commitment 解耦。

### D8. Outcome Dependence

**语义：** i 的重要结果、福利、机会或生活状态在多大程度上依赖于 j / 该关系。

```text
OutcomeDependence_(i->j,t)
```

为什么保留：

- 明显方向性；
- 可高 dependence 低 liking / low dedication；
- power imbalance 很可能可由两方向 dependence 不对称派生。

**Open question:** 某些 dependence 是否应完全由 Agent resources / alternatives / institutional constraints 推导，而不是独立 latent state。第一轮保留 candidate，交给 redundancy test。

---

## 5. Belief-layer high-value constructs

以下概念很重要，但第一轮不把它们机械塞入 directed relationship primitive；更适合明确放进 Belief / perception。

### B1. Perceived Partner Responsiveness — PPR

```text
PPR_(i about j,t)
```

语义：i 是否感到 j 理解、重视、回应自己的需要与核心自我。

当前判定：

```text
KEEP
layer = Belief / relationship-specific perception
```

理由：

- PPR 是关系科学里很强的 construct；
- 但它本质上包含 i 对 j 的解释，不等于 j 的客观 responsiveness；
- 同一行为可因 attribution 不同得到不同 PPR。

因此区分：

```text
ResponsiveAction_(j->i)      # observable/action
PPR_(i about j)              # belief/perception
```

### B2. Perceived Commitment / Perceived Attraction 等

原则上不复制成新的 primitive family，而使用：

```text
Belief_i( Dedication_(j->i) )
Belief_i( RomanticAttraction_(j->i) )
Belief_i( SexualDesire_(j->i) )
```

这利用已有 construct + belief index，避免“真实状态”和“我认为对方的状态”双倍命名。

---

## 6. Pair-level / shared state candidates

### P1. Cohesion / We-ness

**语义：** 二人是否形成较强的共同体/“我们”结构。

当前判定：`KEEP_CANDIDATE / contested scope`。

难点：

- we-ness 可能存在真实 pair process；
- 也可能主要通过双方各自 perception 测量；
- 双方可对“我们感”明显不一致。

因此第一轮 schema 允许：

```text
PerceivedWeNess_(A about pair)
PerceivedWeNess_(B about pair)
```

是否再需要一个 shared latent `Cohesion_(A,B)`，待 Case Bank / longitudinal data 判定。

### P2. Value Congruence

```text
ValueCongruence_(A,B,t)
```

当前判定：`KEEP as pair comparison / derived structural quantity`。

它不是“Alignment 总分”，而是两个人价值状态之间的特定比较。

### P3. Goal Alignment

```text
GoalAlignment_(A,B,t,domain)
```

当前判定：`KEEP as pair comparison / role-sensitive structural quantity`。

与 value congruence 分开，因为：

- 可以价值观相近但现实目标冲突；
- 可以价值观差异大但当前共同目标高度一致。

### P4. Relationship Identity / Agreement

例如：

```text
friend
exclusive romantic partners
engaged
married
open relationship
care arrangement
```

当前判定：

```text
KEEP as pair/institutional agreement fact
NOT affective primitive
```

它可以影响约束、预期、机会结构和 action policy，但不替代底层 relationship state。

### P5. Boundary / Exclusivity Rules

```text
BoundaryRule_(A,B,domain)
```

如性排他、情感排他、财务约定、婚前性行为边界等。

当前判定：`KEEP as Constraint/Agreement`，不是 liking/trust/commitment primitive。

---

## 7. Agent-level constructs 与 attributes

LHRM 不要求把所有 person-level 信息压成少量“人格参数”才能表示关系。

Agent 层允许保留不同数据类型，例如：

```text
age
sex / gender-related attributes
health
income / assets / liabilities
education / skills
location
family obligations
relationship history
life goals
habit patterns
personality traits
baseline libido
generalized trust
caregiving propensity
attachment tendency
```

但这些不是自动的 **relationship-state primitives**。

原则：

```text
Person property
-> AgentState/Attribute
not automatically
-> DirectedRelationshipState
```

例如：

```text
Income_A != ResourceInvestment_(A->B)
BaselineLibido_A != SexualDesire_(A->B)
GeneralizedTrust_A != Trust_(A->B)
```

---

## 8. 当前明确降级为 Action / Observation / Proxy 的变量

这些现象很重要，但不能与 latent relationship state 平级计数：

```text
money spent
messages sent
response latency
hours together
sex acts
physical touch
caregiving acts
compliments
conflict acts
repair attempts
gifts
travel to meet
public declarations
```

它们的 canonical 位置优先是：

```text
Action/Event + provenance + timestamp
```

然后通过 observation / belief / transition 更新 state。

例如：

```text
MoneySpent_(A->B,t)
-> B observes / interprets motive
-> Belief_B updates
-> possible Trust/Care/Attraction/Dedication transition
```

而不是：

```text
MoneySpent = Love
```

---

## 9. 当前明确降级为 Derived / Readout 的量

### R1. Mutual attraction / reciprocal desire / trust asymmetry

由两个方向直接派生：

```text
Mutuality_k(A,B)
= H(Z[k,A,B], Z[k,B,A])
```

### R2. Power / Power imbalance

当前优先假说：

```text
PowerImbalance_(A,B)
= f(
  OutcomeDependence_(A->B),
  OutcomeDependence_(B->A),
  alternatives,
  resources,
  constraints
)
```

不先设一个独立“权力值”。

### R3. Satisfaction

当前倾向：`DERIVED / evaluation-state candidate`。

Satisfaction 是主体对当前关系结果与期望的综合评价，很有预测价值，但它可能是多个底层状态、偏好、belief 和 environment 的 readout，而不是最小关系 basis。

需后续用 longitudinal incremental information 检验：若已知底层状态后 satisfaction 仍携带稳定独立动态信息，才考虑提升。

### R4. Relationship Quality / Compatibility / Match Score

当前：`REJECT as primitive`。

允许未来作为 task-specific readout，不进入 ontology。

### R5. Alignment

当前：`REJECT as single primitive`。

拆成至少：

```text
ValueCongruence
GoalAlignment
```

以及具体 role/domain 下的 constraints。

---

## 10. 当前不应成为 universal primitive 的表面字段

四源研究共同提示高重复计数风险：

### 10.1 年龄

Age 是 Agent attribute / temporal index，不是自动的 attraction / fertility / vitality / maturity。

下游意义需通过独立变量或 belief 映射。

### 10.2 收入 / 资产 / 消费 / 肯花钱

必须至少区分：

```text
resource stock
resource flow
resource allocation action
sacrifice/opportunity cost
motive attribution
```

### 10.3 学历 / 智力 / 阶层 / 门当户对

学历是 observation/attribute，不等于 cognition、culture、class、income expectation 或 compatibility。

### 10.4 “顾家 / 孝顺 / 责任心 / 成熟 / 情绪价值”

都是 composite proxy，必须拆到具体 Agent tendency、Action、Belief、Care、Dedication、Responsiveness、Boundary/Role expectation 等。

---

## 11. Candidate Minimal Directed Basis v0.1

为了启动第一轮 representation regression，当前给出一个**故意保守的小集合**：

```text
DirectedRelationship_(i->j)
=
{
  Liking,
  RomanticAttraction,
  SexualDesire,
  Trust,
  AttachmentSecurity,
  Caregiving,
  Dedication,
  OutcomeDependence
}
```

这 8 项不是宣称“人类关系只有八维”，而是当前四源收敛后最值得先拿去被真实文本击穿的 relation-state basis。

其它重要内容放入：

```text
AgentState
PairState
BeliefState
Constraint/Agreement
Environment
Action/Event log
```

而不是为了“凑维度”全部塞进 directed vector。

---

## 12. 为什么第一版先不加入一些熟悉词

### “爱”

可能是 liking + romantic attraction + attachment + caregiving + dedication 等多分量压缩，不先作为 primitive。

### “亲密”

可能混合 self-disclosure、attachment、trust、sexual/physical intimacy、interaction frequency 等，不先作为 primitive。

### “嫉妒”

更可能是某种 state/event response，由 attachment、threat belief、exclusivity rule、dependence、self-evaluation 等共同生成；先不做 universal primitive。

### “控制欲”

可能是 Agent tendency + action policy + threat / dependence / boundary conflict，不先做关系 basis。

### “忠诚”

需区分 dedication、boundary agreement、actual behavior、belief；不以一个词合并。

### “化学反应”

保留为互动过程/反馈环描述，不直接作为一个不可拆总分。

---

## 13. 第一轮 representation schema

对任意一句关系相关事实，首先尝试落到：

```text
1. AgentState / Attribute
2. DirectedRelationshipState
3. PairState
4. BeliefState
5. Action/Event
6. Constraint/Agreement
7. Environment
8. History/Timeline
9. Provenance/Uncertainty
10. Derived/Narrative-only
```

若一句话不能合法落入任何一类，标：

```text
MAPPING_FAILURE
```

禁止第一反应直接新增 primitive。

先诊断：

```text
ontology hole
construct hole
scope hole
temporal/history hole
belief/observation hole
measurement hole
or merely narrative/irrelevant
```

---

## 14. Measurement 暂不冻结

v0.1 允许一个 coordinate 不是单一标量。

例如：

```text
StateCoordinate
=
{
  estimate_or_region,
  uncertainty,
  evidence,
  provenance,
  observation_time
}
```

甚至：

```text
P(Z_k | Evidence_<=t)
```

都合法。

因此第一轮 Case Bank test 只要求 **语义有合法落点**，不要求每句话产生精确数值变化。

例如：

> “A 深情地看了一眼 B”

优先表示为：

```text
Action: Gaze_(A->B)
Narrative/Observation: affective description = affectionate/deep
EvidenceFor: Liking / RomanticAttraction, uncertain
```

而不是未经校准就写：

```text
Liking += 1
```

---

## 15. 下一验证门

`Candidate Minimal Directed Basis v0.1` 不因写进本文自动升级为 validated ontology。

下一步必须执行：

### Gate A — Court-fact sentence coverage

选一份结构简单、事实链清楚的公开判决/官方 case：

1. 去掉法律条款、裁判理由、判决结果；
2. 只保留 fact narrative；
3. 独立 Agent 逐句映射；
4. 记录所有 `PARTIAL_MAPPING / MULTI_MAPPING / MAPPING_FAILURE`；
5. Architect 只分析 failure，不允许 Agent 为了通过测试现场发明变量。

### Gate B — Cross-context counterexamples

至少测试：

```text
same-sex
opposite-sex
kin
non-kin
friendship
romance
caregiving
conflict
unilateral attraction
high-dependence/low-liking
high-attraction/low-trust
```

### Gate C — Redundancy challenge

重点攻击：

```text
Liking vs RomanticAttraction
Trust vs AttachmentSecurity
Caregiving vs Dedication
AttachmentSecurity vs Cohesion/We-ness
OutcomeDependence vs structural derivation
PPR vs Trust/Care/Attachment
```

通过后，才有资格把 v0.1 candidate 推向 `Minimal Sufficient State v0.1`。

---

## 16. 当前结论

本轮四源收敛后，最有价值的不是“终于凑出八个参数”，而是形成了更严格的层次：

```text
Agent properties
+
small directional relationship-state basis
+
pair facts/comparisons
+
beliefs
+
constraints/agreements
+
actions/events
+
environment
+
history
+
uncertainty/provenance
```

复杂现实通过这些结构的组合、方向性与时间演化产生。

因此 v0.1 的工作假说是：

> **人类二人关系不需要为每个现实故事准备一个参数；先用少量有向 relation constructs + 非关系层状态共同构成可解释的动态 state space，再让真实案例负责击穿它。**
