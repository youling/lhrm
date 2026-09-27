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

候选 construct 要进入 Minimal Sufficient State，至少接受以下审计。

> **执行规格（输出字段 / 阈值 / 指定执行者 / 程序）不在本文。** 六条判据的完整执行面是
> `docs/foundation/VALIDATION_GATES_V0_2.md` §5；逐 cell 判据在同文件 §6.3。本文只写**判据本体**与**后果句**。
> 门未执行前，任何判据都不得被当作已通过。

### 2.1 Semantic independence

是否具有不能被现有 construct 无损替代的独立语义？

**后果：** 该 construct **不得**新提升进 basis；成为 `DERIVE` / `MERGE` 候选。它**不自动移出**——
移出需要覆盖证据（§2.6），语义判断单独不足以缩减 basis。
**无阈值**（拒设，`VALIDATION_GATES_V0_2` §8-2）。

### 2.2 Counterexample decoupling

现实中能否稳定出现：A 高、B 低；A 低、B 高？

若无法构造或观察解耦反例，可能属于同一 latent state 的重复命名。

**后果：** 无稳定解耦实例 ⇒ `HOLD`（`HOLD_REASON = EVIDENCE_MISSING`）；
若同时显示**耦合**行为（无任何象限组合可构造）⇒ `MERGE` 候选。
**注意不对称性：反例缺失是弱证据。**
本判据的 harness 是 `GATE_CROSS_CONTEXT` 的 Table B（原 §15 Gate C 六对中只有三对属本判据，
三对属 §15 的冗余挑战）——两者此前都无后果，现已各自接上。
**无阈值**（拒设，`VALIDATION_GATES_V0_2` §8-3）。

### 2.3 Conditional incremental information

已知其它候选后，该 construct 是否仍可能为当前状态或未来转移提供额外信息？

**后果：** FAIL ⇒ `DERIVE` 候选。**FAIL 不得由「未观测到」断言**——
本判据在现有材料下的诚实状态是 `UNTESTABLE_WITH_CURRENT_DATA`，不是 `NOT_DEMONSTRATED`。
**无阈值**（拒设，`VALIDATION_GATES_V0_2` §8-4）。

### 2.4 Scope stability

在 `HD-ST-1` 抽样框下，语义是否保持稳定？分类法 SSOT = `VALIDATION_GATES_V0_2` §6.4
（Table A 逐 cell = `HD-A01`…`HD-A15`）。

**后果：** 任一 `RUN` cell 判 `UNSTABLE` ⇒ 该构念定义在该语境有缺陷 ⇒ `HOLD`（`CONTESTED`）
并升级为定义修复。**`NOT_RUN` 不满足本判据**，且**永不**计为 pass。
**阈值（结构性零 N）：** 满足 = 无 `UNSTABLE` 的 `RUN` cell **且** 无 `NOT_RUN` cell。
**不设**跨 cell 的比例阈值（会重新引入单一分母，`VALIDATION_GATES_V0_2` §8-5）。

> **SUPERSEDED（2026-09-28，被 C-P7 取代；原文逐字保留）：** 本节原内联清单为
> 「在 same-sex / opposite-sex、kin / non-kin、stranger / established relationship、
> romance / friendship / caregiving / conflict 等语境下，语义是否保持稳定？」
> 该 8 项清单与 `CONSTRUCT_SCOPE_DIRECTIONALITY` §7 第 6 项的 6 项清单、§15 Gate B 的 11 项清单
> 三者互不相同，且都不含 `sibling` / `parent–adult-child` / `ex-partner` / `professional` / `adversarial`。
> 取代依据 = `youling/lhrm#30` `ARCHITECT_ADJUDICATION_V1` C-P7（ACCEPT）+ X-10（两层记账）。

### 2.5 Layer test

候选究竟属于 §13 的 `LHRM-LANDING-1` 落点类？判据本体与**该判据曾经使用的 10 层清单**已合并到 §13；
本节不再维护第二份词表（合并前两表各 10 项、重叠 7 项、各有 3 项只在一边，
未合并前任何 layer 判定都能被两套词表分别「证成」）。

**后果：** 重路由到该判据指定的层；只是行为、标签、结果或 proxy 者**不因常见就升级为 primitive**。
层归属**不可**由预测强度重开。**无数值阈值**（判据是类别型的；设数值会允许「大体上是 proxy」通过为 primitive）。
**注意：** `Observable proxy` 与 `Mechanism evidence` 在合并后**不再是落点类**，改判为跨类状态位——
它们是「关于该单位是什么」的说法，不回答它落在哪一层。

> **SUPERSEDED（2026-09-28，被 C-P1 项 7 取代；原文逐字保留）：** 本节原内联 10 层清单为
> ```text
> Agent attribute/state
> Directed relationship state
> Pair property/state
> Belief/perception
> Action/Event
> Constraint/Agreement
> Environment
> Observable proxy
> Derived readout
> Mechanism evidence
> ```
> 取代依据 = `youling/lhrm#30` `ARCHITECT_ADJUDICATION_V1` C-P1「ACCEPT WITH MODIFICATION」项 7。
> 逐项合并处置见 `VALIDATION_GATES_V0_2` §4。

### 2.6 Representation necessity

若删除该 construct，是否会存在重要现实句子/状态无法用剩余 schema 合法表示？

这项将在 Case Bank regression 中直接测试。

> **该项已由缺失的臂兑现（2026-09-28）。** 原文 `:86` 承诺「将在 Case Bank regression 中直接测试」，
> 而 Gate A 的五个步骤**没有任何一步包含「移除某个 construct 再重测」**。
> 现由共享程序步骤 **`ARM-ABL-1`（leave-one-construct-out ablation arm）** 兑现，
> 定义见 `VALIDATION_GATES_V0_2` §6.0。**缺的是一条臂，不是一个阈值。**

**后果：** FAIL ⇒ `MERGE` / `DERIVE` 候选。依 C-P1，ablation 证据**累积**才流向 `MERGE` / `REJECT`，
**单次 `MAPPING_FAILURE` 不构成本体否决**。**这是唯一能让 basis 缩小的判据。**
**阈值（结构性存在条件）：** necessity ≡ 存在至少 1 个 witness 降级；
`NON_NECESSARY` ≡ 零降级。**但该条件只有在 construct-bearing 材料上跑过才有效**；
否则判 `UNTESTABLE` → `HOLD`，**不得**判 `KEEP`。
**「重要」的操作化定义见 `VALIDATION_GATES_V0_2` §5.1**（不依赖标注者印象，依赖 ablation 输出）。

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

**落点词表 `LHRM-LANDING-1`（本文是唯一 SSOT；门与判据的引用一律指向本节，不复制本表）。**

### 13.1 落点类（10 个，`destination` 必填其一）

```text
1.  AGENT_STATE_ATTRIBUTE        # AgentState / Attribute
2.  DIRECTED_RELATIONSHIP_STATE   # DirectedRelationshipState
3.  PAIR_STATE                    # PairState
4.  BELIEF_STATE                  # BeliefState（含 perception）
5.  ACTION_EVENT                  # Action/Event
6.  CONSTRAINT_AGREEMENT          # Constraint/Agreement
7.  ENVIRONMENT                   # Environment
8.  HISTORY_TIMELINE              # History/Timeline
9.  PROVENANCE_UNCERTAINTY        # Provenance/Uncertainty
10. DERIVED_READOUT               # Derived readout（不是 narrative）
```

### 13.2 跨类状态位（3 个，**不是**落点类，不吸收单位）

```text
OBSERVABLE_PROXY_STATUS      # 「这是一个可观察代理」是关于单位的说法
MECHANISM_EVIDENCE_STATUS    # 「这只是机制证据」是关于单位的说法
NARRATIVE_EVALUATION_STATUS  # 「这是叙事/评价性表达」是关于单位的说法
```

> **合并说明（2026-09-28，C-P1 项 7 / `ADJ3` rec 7）。** §2.5 的 10 层与本节原 10 类
> **重叠 7 项、各有 3 项只在一边**（13 个 legacy 字符串）⇒ 未合并前任何 layer 判定都能被
> 两套词表分别「证成」。合并结果 = 13 个 legacy 字符串 → **10 个落点类 + 3 个状态位**。
> 逐项处置见 `VALIDATION_GATES_V0_2` §4。
>
> **可核后果：** catch-all 落点类由 **4 个降为 3 个**（`ENVIRONMENT` / `HISTORY_TIMELINE` /
> `PROVENANCE_UNCERTAINTY`）——`Derived/Narrative-only` 的 narrative 部分已降为状态位，
> 不再兜底。**这是收敛，不是消除。**

> **SUPERSEDED（2026-09-28；原文逐字保留）：** 本节原 10 类表为
> ```text
> 1. AgentState / Attribute
> 2. DirectedRelationshipState
> 3. PairState
> 4. BeliefState
> 5. Action/Event
> 6. Constraint/Agreement
> 7. Environment
> 8. History/Timeline
> 9. Provenance/Uncertainty
> 10. Derived/Narrative-only
> ```
> 取代依据 = `youling/lhrm#30` `ARCHITECT_ADJUDICATION_V1` C-P1。

### 13.3 落点赋值带两个必填字段

```text
catchall_used ∈ { NO, YES }   # 是否落在三个 catch-all 类之一
landing_reason               # catchall_used = YES 时必填、非空
```

**fail-closed 默认：** `catchall_used = YES` 时该单位的 `mapping_outcome` **默认**为 `PARTIAL_MAPPING`，
**不是** pass；只有分诊显式结清并写入理由才可升级。
理由：`HISTORY_TIMELINE` 与 `PROVENANCE_UNCERTAINTY` 对**每一个**单位都可用
（任何陈述都有时间索引与归属）⇒「有一个类可用」永远为真，而**可用 ≠ 正确表示**。

### 13.4 `MAPPING_FAILURE` 必须是可达且持久的

```text
MAPPING_FAILURE
```

**可达性（2026-09-28 修复，H-A3）。** 该类型此前**不可达**，由三个作用于流水线不同阶段的机制造成，
三者已同时修（完整流水线与修法见 `VALIDATION_GATES_V0_2` §3）：

```text
STAGE 0  relation-relevance pre-check   -> NON_RELATION_RELEVANT_EXIT（条件式 + 记录）
STAGE 1  landing-class assignment       -> 无类可落则 MAPPING_FAILURE（记录，持久）
STAGE 2  diagnosis                      -> 13.5 诊断清单之一（含 redundancy hole）
STAGE 3  triage / escalation            -> 结清须过 13.5 的三条；否则保留为 MAPPING_FAILURE
STAGE 4  gate accounting                -> 失败数与结清数并列报告，永不合并
```

**持久性：** `MAPPING_FAILURE` 一旦产生，携带单位 id、来源锚、诊断类、结清状态进入
`VALIDATION_GATES_V0_2` §7 台账；**任何后续门都不能删除它，只能结清它。**
**禁止第一反应直接新增 primitive。**

### 13.5 诊断清单（8 项）

```text
ontology hole
construct hole
scope hole
temporal/history hole
belief/observation hole
measurement hole
redundancy hole                    # 新增：该 unit 可由 <k> 无损表示，故 <m> 非必要
or merely narrative/irrelevant     # 条件式出口，见下
```

> **新增 `redundancy hole` 的理由（H-A1）。** 诊断词表此前是**纯加法封闭**的：6 个 hole 全是
> 「某物无法被表示」，**没有 redundancy / duplicate 一类**。Gate 若产出「`Trust` 与
> `AttachmentSecurity` 冗余」，**当前类型系统里无处可记**——这正是 redundancy 结果此前不可记录的原因。

**`merely narrative / irrelevant` 是条件式出口，不再是无条件逃生门（词面保留不变以维持镜像匹配）：**

```text
允许以 merely narrative / irrelevant 结清 MAPPING_FAILURE，当且仅当三条同时成立：

  (a) 记录非空的 relation_relevance_reason —— 该单位为何不承载 i–j 的状态 / 互动 / 约束；
  (b) 已证明该单位「不是因为找不到类才落不进」，而是因为存在一个语义正确的类并被有意放弃
      （即：证明过 unmappability，而不只是「不重要」）；
  (c) 结清计入运行台账的 DISCHARGED_NARRATIVE 计数，与失败计数并列报告，永不合并。
```

任一条不成立 ⇒ 结清无效 ⇒ 保留为 `MAPPING_FAILURE`，缺省归入 `ontology hole`。

> **(b) 是本条的关键：「不相关」与「不可表示」是两个不同命题。** 要求一个理由只能排除前者；
> 要求 `unmappability` 才排除后者。因此**要求「该单位不关系相关」不等于**要求「该单位不可映射」。

> **镜像义务（未在本轨执行）。** 本节 8 项清单原先被 `AGENTS.md` 第 62 行**逐字镜像**。
> 该镜像**必须**同步加入 `redundancy hole` 与条件式出口，否则本节的 delete 臂在类型上仍不可达。
> 本轨**不编辑** `AGENTS.md`（兄弟轨 D 所有）：逐字替换提案见 `VALIDATION_GATES_V0_2` §9 P-1。

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

> **本句的成功判据已被收紧（2026-09-28，H-A3 机制 (3)）。**
> 「**有一个合法落点**」不是门的通过条件，因为三个 catch-all 类（§13.3）对**每一个**单位都可用
> ⇒ 该判据永远为真，失败因此**很少发生**。
> 现行判据是 §13.3 的 `catchall_used`：**`MAPPING_FAILURE` 计数 = 0，且未结清的
> `catchall_used = YES` 计数 = 0**（结构性零 N，由门自身的成功定义推出，不是选定的数字）。
> 「不要求精确数值变化」这一半**不变**——representation-first invariant 不受本次修复影响。
> 见 `VALIDATION_GATES_V0_2` §3.1 与 §6.1。

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

> **本节已被 `docs/foundation/VALIDATION_GATES_V0_2.md` 取代（2026-09-28）。**
> 取代依据 = `youling/lhrm#30` `ARCHITECT_ADJUDICATION_V1` 的 C-P1（ACCEPT WITH MODIFICATION）与
> C-P2（ACCEPT）。**原文完整保留在本节末尾的 `SUPERSEDED` 块内，一行未删。**
> 取代原因：原 Gate A/B/C 把覆盖、最小性、跨语境、冗余处置混在一起；Gate B 无判据；
> Gate C 无后果；`MAPPING_FAILURE` 类型上不可达。裁决 §C item 4 明确
> **Gate A 的 Court-fact 覆盖 ≠ construct 最小性**。

### 15.1 现行四门（SSOT = `VALIDATION_GATES_V0_2`）

| 门 | 唯一职责 | 今日可执行性 |
|---|---|---|
| `GATE_COVERAGE` | 关系相关事实**能否被表示**（不新造构念） | **可执行**（用已冻结 fixture） |
| `GATE_MINIMALITY` | 构念**是否必要**，还是冗余 / 可无损派生 | **不可执行**（缺 construct-bearing benchmark，见 X-9） |
| `GATE_CROSS_CONTEXT` | 语义在**独立生成**的 benchmark 上**是否稳定** | 部分（Table A 多为 `NOT_RUN`） |
| `GATE_REDUNDANCY` | 签发终局处置 `KEEP｜MERGE｜DERIVE｜REJECT｜HOLD` | 依赖前三门 |

**共享程序步骤：** `ARM-ABL-1`（leave-one-construct-out ablation arm）——兑现 §2.6 的承诺；
`GATE_COVERAGE` 读其 baseline arm，`GATE_MINIMALITY` 读其 withheld arm。

**推进资格：** 通过后才可推向 `Minimal Sufficient State v0.1`，但「通过」现在有确切含义：
`KEEP` 需满足 K1–K4（`VALIDATION_GATES_V0_2` §2.3）。
**今日诚实记账：** 在 construct-bearing benchmark 存在之前，§11 的任何构念都**无法**被签 `KEEP`；
可达的最高处置是 `HOLD / BENCHMARK_NOT_BUILT`。**这不是失败结果，是前置条件的记账。**

### 15.2 SUPERSEDED（2026-09-28）— Gate A / B / C 原文

以下为**历史文本**，保留作 provenance，**不再是规范**。任何执行必须读
`docs/foundation/VALIDATION_GATES_V0_2.md`。

```text
### Gate A — Court-fact sentence coverage

选一份结构简单、事实链清楚的公开判决/官方 case：

1. 去掉法律条款、裁判理由、判决结果；
2. 只保留 fact narrative；
3. 独立 Agent 逐句映射；
4. 记录所有 PARTIAL_MAPPING / MULTI_MAPPING / MAPPING_FAILURE；
5. Architect 只分析 failure，不允许 Agent 为了通过测试现场发明变量。

### Gate B — Cross-context counterexamples

至少测试：

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

### Gate C — Redundancy challenge

重点攻击：

Liking vs RomanticAttraction
Trust vs AttachmentSecurity
Caregiving vs Dedication
AttachmentSecurity vs Cohesion/We-ness
OutcomeDependence vs structural derivation
PPR vs Trust/Care/Attachment

通过后，才有资格把 v0.1 candidate 推向 Minimal Sufficient State v0.1。
```

**取代关系逐条：**

| 原文 | 取代者 | 依据 |
|---|---|---|
| Gate A 五步 | `GATE_COVERAGE` + `ARM-ABL-1` baseline arm | C-P1；H-A2（缺的是臂，不是阈值） |
| Gate B 11 项**单表** | Table A `HD-A01…HD-A15`（抽样框）+ Table B `HD-D01…HD-D10`（解耦模式）——**两表，无单一分母** | C-P2；H-A4 |
| Gate C 六对 | `GATE_MINIMALITY`（判冗余）+ `GATE_REDUNDANCY`（签处置） | C-P1 |
| 「通过后，才有资格……」 | 5 值终局处置 + K1–K4 | C-P1（4 值扩展为 5 值的 delta 见 `VALIDATION_GATES_V0_2` §2.2） |

**Gate B 枚举的四处更正（原文之外，逐条给出依据）：**

1. **归属错误：** `high-attraction/low-trust` 曾被归属到 §4 D4「可高**喜欢**低信任」，
   而 D1 明写「可以喜欢但无 romantic attraction」、D2 明写可与 liking 解耦
   ⇒ `Liking` 不得顶替 `Romantic Attraction`。修正为 `RomanticAttraction` × `Trust`（`HD-D03`）。
2. **类目错误：** `harm-asymmetric` 是**不对称轴**，不是 dyad **型**，从 dyad 型清单中删除。
   「角色方向不对称」只作为 `HD-A08`（caregiving）的修饰语保留。
3. **两个真 cell 曾在一张派生覆盖表里漏记**（`opposite-sex`、`non-kin`）。缺陷发生在 PR #31 `17` 的覆盖表，
   **不在 canonical §15 本身**——§15 两条都在；本节真正的缺陷是**无逐 cell 判据**。
   本表把它们具名为 `HD-A13` / `HD-A03`。
4. **一个非 Gate B cell 曾被计入**（`work colleague`，同一张派生覆盖表）：它是 `HD-A07` 的角色实例，
   不是独立的抽样框，也不是解耦模式 ⇒ 不作为一行。

原 11 项的逐条去向 + 本表新增行的理由见 `VALIDATION_GATES_V0_2` §6.3.4。

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
