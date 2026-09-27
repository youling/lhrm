# 11 — General Human Dyad Scope Audit

**Status:** RESEARCH_CANDIDATE / NOT CANONICAL
**As of:** 2026-09-27
**Lane:** R11 · Wave 1
**Scope:** 检验 `docs/foundation/PARAMETER_CONVERGENCE_V0_1.md` 的 candidate construct 在 9 类 Human Dyad 上的含义稳定性与域泄漏
**Authority:** 本文件不改 ontology、不改 canonical docs、不给参数/权重/公式。§3–§7 全部条目为 **proposal only**。

---

## 0. 本文件要回答的问题（以及不回答什么）

LHRM 的研究域已冻结为 Human–Human relationship system，最小对象是 `HumanDyad(i,j)`，并**明确不预设**异性、陌生起点、婚恋目标（`CURRENT_ARCHITECTURE.md` §2、§3）。但 `PARAMETER_CONVERGENCE_V0_1.md` 的 candidate list 是从 Games / Scientific / Dating Apps / Real-world 四源收敛出来的，其中 Dating Apps 与 Scientific 两源的关系科学文献绝大多数以**恋爱 dyad** 为样本。

本文件只问两个问题：

1. **有没有哪个 primitive 的含义在不同 dyad 类型上真的不同**（而不是读数不同）？
2. **候选表里哪些地方在悄悄假定"恋爱亲密 / 性可得 / 自愿同居 / 共享未来"**，因而出了那个框架就不表示它看起来表示的东西？

**明确不回答**：一般社会理论、关系社会学批判、任何"人际关系科学应如何"的方法论争论。本文件只关心**架构表达力**。

**一个先行发现（决定本文件的写法）**：关系科学领域**自己**承认它的普适性是宣称而非事实。Finkel、Simpson & Eastwick（2017）在 *Annual Review of Psychology* 的 14 原则综述里写：`The 14 principles paint a cohesive and unified picture of **romantic** relationships`，正文进一步说 `Relationship scientists investigate many types of relationships, but the primary emphasis is on close relationships… especially **well-established romantic relationships**`。而 Reis 编的 *Handbook of Relationship Science* 前言同时写下两句相反的话：领域 `generally intend that their theories and empirical findings apply across the board… to friendships and romantic relationships of varying degrees of closeness, to relationships involving teammates and neighbors and co-workers, to student–teacher, physician–patient and supervisor–subordinate dyads, and to familial relations involving cousins and siblings and children`，但 `Empirical studies of dating and marital relationships are common; studies of […] are somewhat less common`。

**所以本文件不是"外行质疑内行"，而是记录一个内行已经写下的、尚未被工程化的 gap。** 下面的 verdict 因此按 dyad 类型给出，不按学科给出。

---

## 1. 判定码与本矩阵的效力边界

| 码 | 含义 |
|---|---|
| `MEANING_PRESERVED` | 构念语义跨该 dyad 类型稳定 |
| `MEANING_SHIFTS` | 语义在**参照类**或**边界条件**上改变，不是分布/读数差异 |
| `READOUT_DIFFERS` | 语义稳定，但下游读数、后果或极性随 dyad 类型变 |
| `NOT_APPLICABLE` | 结构性不适用（不是"未知"，不是"零"） |
| `UNKNOWN` | 文献真正沉默 |

> **矩阵效力边界（必读）**：本矩阵中所有 `MEANING_PRESERVED` 都是**语义判断**，不是**心理测量判断**。本次**没有找到**任何针对这 8 维 directed battery 的跨 dyad-type 测量不变性研究。因此"跨 9 类 dyad 语义稳定"在 LHRM 内部目前是**未经检验的假设**，不能写成"已验证"，也不应被后续 lane 当作既成前提引用。

列码：`R` 恋爱伴侣 · `D` 约会陌生人（未成形）· `F` 友谊 · `S` 兄弟姐妹 · `K` 亲子（成年）· `C` 照护 dyad · `X` 前任 · `W` 专业/合作 · `A` 冲突/敌对

---

## 2. 兼容性矩阵

| construct / 架构元素 | R | D | F | S | K | C | X | W | A |
|---|---|---|---|---|---|---|---|---|---|
| `Liking` | MP | MP | MP | MP | MP | MP | MP | MP | MP |
| `RomanticAttraction` | MP | MP | RD | MS | MS | MS | MP | MS | NA |
| `SexualDesire` | MP | MP | NA | NA | NA | MS | MP | MS | NA |
| `Trust` | MP | MS | MP | MS | MS | MS | MP | MS | MS |
| `AttachmentSecurity` | MP | MP | MP | MS | MS | MP | MP | NA | NA |
| `Caregiving` | MP | NA | MP | MP | MP | MP | MP | MS | MS |
| `Dedication` | MP | MS | MS | MS | MS | MS | MS | MS | MS |
| `OutcomeDependence` | MP | NA | MS | MS | MS | MS | MP | MS | MS |
| `PPR` | MP | RD | UK | UK | UK | UK | MP | RD | MS |
| `Cohesion / We-ness` | MP | NA | MP | MS | MS | MP | MS | MS | MS |
| `ValueCongruence` | MP | UK | MP | MP | MP | UK | MP | RD | NA |
| `GoalAlignment` | MP | UK | MP | MP | MP | RD | RD | RD | MS |
| `RelationshipIdentity` | MP | UK | MP | MS | MS | MS | MS | MS | NA |
| `Boundary / ExclusivityRules` | MP | NA | MS | MS | MS | MP | MP | MS | MS |
| `Mutuality` (derived) | MP | UK | MP | RD | MP | UK | MP | RD | RD |
| `PowerImbalance` (readout) | RD | UK | RD | NA | RD | NA | RD | NA | NA |
| `Satisfaction` (derived) | MP | NA | MP | MP | MP | RD | RD | RD | NA |
| `Alignment` (rejected) | MP | UK | MP | UK | MP | UK | RD | RD | NA |
| Agent slot `baseline libido` | NA | NA | UK | UK | UK | UK | UK | UK | NA |
| Agent slot `family obligations` | MP | UK | MP | MS | MS | MP | MS | MP | NA |
| 层类型 `ConstraintsAndAgreements` | MS | MS | MS | MS | MS | MS | MS | MS | MS |
| facet 方案 `source/target/edge` | MP | MP | RD | MS | MS | MS | MS | RD | MS |
| 局部投影 `X_(S,O,t)` | MP | UK | RD | MS | MS | MS | MS | MS | MS |
| 值类（仅 `Unknown`） | MS | MS | MS | MS | MS | MS | MS | MS | MS |

---

## 3. 真正的 primitive 变化（不是 readout 差异）

### 3.1 状态空间缺第三个值类：`ScopeApplicability`

`PARAMETER_CONVERGENCE_V0_1.md` §14 允许坐标为 `estimate_or_region / uncertainty / evidence / provenance`；`CURRENT_ARCHITECTURE.md` §9 允许 `Unknown`；`AGENTS.md` 规定 `Unknown/missing data must remain explicit; never silently coerce missing information into neutral/perfect-match values`。

但矩阵里 `SexualDesire × {友谊, 兄弟姐妹, 亲子, 敌对}` = `NOT_APPLICABLE`。对兄弟姐妹的性欲坐标，**正确值既不是 `Unknown`（我们可能高度确信其不存在），也不是 `0`（0 是"被测到的零"，是另一个断言），而是"该构念在此 dyad 类型上结构性不适用"**。现有值类集合里没有这一格，**唯一的合法表示方式就是把不适用填成 0 或 Unknown——正是 `AGENTS.md` 禁止的动作**。

这不是"加一个构念"，是给状态空间加一个值类，因此它**不在 8 维 basis 里**，不会被 `Gate C (Redundancy challenge)` 发现。`RomanticAttraction` 在敌对 dyad、`AttachmentSecurity` 在纯合同 dyad、`Cohesion` 与 `OutcomeDependence` 在约会陌生人落到同一问题。

> **Proposal（仅提案）**：坐标值类扩为 `{applicable(estimate/interval/…), structurally_not_applicable, scope_unknown}`；`DyadSnapshot` 顶层增加 `DyadScopeProfile`，声明本次快照的有效坐标子集与每坐标 applicability。

### 3.2 缺一个 directed 构念：`Obligation / Duty Orientation`

`Dedication` 的定义是"`主动`希望维持…的`内在`关系性承诺"（affective/voluntary 向量）；`Caregiving` 的定义是"照护…的`关系性动机`"——两者都把 affection 写死。obligation 在 LHRM 中没有坐标，只能溢出到 `ConstraintsAndAgreements`（被写成"约束/协议"的层）或 Agent 层。**五条互相独立的证据线收敛到"obligation 与 affection/attachment 可分离，且在亲属与照护域承重"**：

1. **Cicirelli (1993)**，*Psychology and Aging* 8(2):144–155，doi:10.1037/0882-7974.8.2.144 — 标题即"attachment **and obligation** as daughters' motives for caregiving behavior"，两者被**分开测量**并各自解释 burden。
2. **Montgomery, Havvey & Kosloski (1997)**，`Profiles in Caregiving: The Unexpected Career` — `Obligation is as potent a motivation for caregiving as affection insofar as some children take on caregiving responsibilities to reverse or overcome longstanding problems with parents`。二者不仅可分离，还可能**反向**。
3. **`Reciprocity and Social Support in Caregivers' Relationships` (1995)**，doi:10.1177/104973239500500306 — 互惠本身有 4 种变体（reciprocity / generalized / **waived** / constructed），其中 constructed reciprocity **只**在照护对象身上出现；且 `Some caregivers provided care by obligation with no reciprocity.`
4. **Gehr et al. (2021)**，doi:10.1186/s12877-021-02425-1 — `motivation to care due to feelings of affection` vs. `due to feelings of obligation` 是三型分类的**判别维度之一**。
5. **Meyer & Allen (1991)**，doi:10.1016/1053-4822(91)90011-z — 承诺研究自身**必须**把 commitment 拆成 affective / **normative** / continuance，说明单一"承诺"坐标**必然欠定**。

同时 Dykstra 指出代际 obligation 是**法律构成**的：`Laws define the relationships of dependence and interdependence between generations and gender`；`Legal norms and social policies are not neutral. They impose dependencies that limit the autonomy of men and women, or on the contrary, support the choice to assume intergenerational obligations`。→ `impose` 与 `choice` 两种情形在 LHRM 中无法区分。

> **Proposal（仅提案）**：`Obligation_(i->j)` 作为第九个 directed candidate；`Dedication` 相应收窄为 affective dedication，并显式记录二者相关性而非合并。

### 3.3 缺一个 per-edge 结构性构念：`Constrainedness / Control-Asymmetry`

`CURRENT_ARCHITECTURE.md` §3 的顶层容器是 `ConstraintsAndAgreements`，`PARAMETER_CONVERGENCE` §6 的 P5 是 `Boundary / Exclusivity Rules` —— **二者都内建了"同意/consent"**。但 §2 已把 `违法或违反社会规范` 的关系写入域。非自愿约束（coercive control、人身控制、勒索、囚禁）既不是 agreement，也不是 `Environment`，也不是 `Agent`。`AGENTS.md` 规定"违法性是与关系状态分离的轴"——违法性有轴，但**约束能力本身没有坐标**。

- **Johnson (2006)**，doi:10.1177/1077801206293328：有害 dyad 的**定义性变量是 control context**，`the distinctions among the types are based entirely on control context, not frequency or severity of violence`。
- **Dutton, Goodman & Schmidt**：`measurement of control tactics alone does not capture the capacity to control or the function of control`。LHRM 把一切 conflict 降级为 Action/Event（§8）之后，**capacity 无处安放**。

**可证伪主张**：当前 basis **无法区分"互惠的敌意"与"单向的控制"** —— 二者都表现为双向低 Liking + 大量 conflict action。Johnson 的四型正是靠 control context 才能分开。

> **Proposal（仅提案）**：`Constraints` 与 `Agreements` 拆为两容器；`Constraint` 为 per-edge，带 `source` / `scope` / `consent_status ∈ {consensual, imposed, unknown}` / `degree`；派生 `ConstraintAsymmetry(A,B)`。

### 3.4 `PairExistence` / `TerminationStatus`：dyad 这个对象本身存在方式不同

`CURRENT_ARCHITECTURE.md` §2 冻结 `HumanDyad(i,j) = Person_i + Person_j + Relationship_ij`，`Relationship_ij` 被直接假设存在。但：

- **前任**：Tan et al. (2014)，doi:10.1177/0265407514536293 指出 `the tradition has been to measure relationship dissolution as a dichotomous end state (i.e., intact or dissolved)`，而其自身结果表明 pre-breakup commitment **中介** post-breakup closeness，结论是 `the termination of a romance does not signal the complete termination of a relationship`。→ "已终止"不是 pair 的一个状态，而是**双方不一致 + 单方持续维护 + 各自法律状态**三件事。Hardesty et al. (2015) 更把 `harassment and violence after separation` 列为区分 coercive-control 类型的关键变量。
- **兄弟姐妹**：Blake et al. (2022, n=291) 受访者自陈 `I don't really know my brother`（like a stranger），作者结论 `confirming that they are not necessarily or always life-long, significant or supportive`。→ **基因上完整的同胞 dyad 可以完全惰性/不存在。**
- **约会陌生人**：矩阵 D 列有 4 个 `NA` + 1 个 `RD` + 2 个 `UK`，根源在此 —— **成形前的 dyad 不是一个有状态坐标的 pair，而是一个"提议"**。目前只能靠 `Unknown` 兜，会把"还没发生"与"发生了但我不知道"混为一谈。

> **Proposal（仅提案）**：`Relationship_ij.existence ∈ {not_formed, proposed_unilateral, proposed_mutual_unknown, formed, formed_contested, terminated_unilateral, terminated_mutual, terminated_with_continuing_maintenance, inert_estranged}`；`RelationshipIdentity` 拆为 `{relational_role, legal_status, functional_arrangement, termination_status}` 四轴。

### 3.5 `Ambivalence` 在亲属 dyad 里是一等状态，不是"几个坐标低的组合"

family science 不把"又爱又怨"当作低分合成：

- Bengtson, Giarrusso, Mabry & Silverstein (2002)，doi:10.1111/j.1741-3737.2002.00568.x — `Solidarity, Conflict, and Ambivalence`；
- de Bel, Kalmijn & van Duijn (2019)，doi:10.1177/0192513X19860181（n=549 sibling–parent–sibling triads, Netherlands Kinship Panel）— `The reverse of no conflict is not the same as a strong relationship.`；`family relationships are often simultaneously characterized by "positive" and "negative" dimensions… that are not mutually exclusive. The co-occurrence of positive and negative relational dimensions is also known as ambivalent relationships`；
- 同一篇指出 `family systems are hard to operationalize and therefore challenging to analyze. It requires dividing the system in smaller—empirically analyzable—relational units, such as dyads or triads`；
- Blake et al. (2022) 的参与者原话 `I love my sister, who is a great person in lots of ways, but I don't like her very much` —— **不是研究者构造的解耦，是当事人自己把两个状态分开报告的**。

**对 Gate C 的直接后果**：`Gate C` 里的 `Liking vs Caregiving` / `Caregiving vs Dedication` 在 kin/care dyad 上**无法仅靠"低分组合"通过**。→ Gate C 的测试集**必须按 dyad 类型分层**，否则会在恋爱样本上"通过"而在 kin 样本上失效。

**可证伪推论（建议交 R06）**：若 `Ambivalence` 只是低分合成，则 kin dyad 上"warmth 低 + conflict 高"应预测整体状态差；de Bel et al. 的 549 triad 分析给出相反方向的证据（`enhancement` 强、`loyalty conflict` 只在 contact 上有弱效应）。→ **dyad 类型看起来是交互项的函数，不是可加坐标的函数**，直接冲击 §3.8 的加法示意分解。

### 3.6 `Cohesion / We-ness` 在敌对 dyad 上读数符号会反

项目已把 P1 标为 `contested scope` 并拆成 `PerceivedWeNess_(A about pair)`，方向正确，但还差一步：**敌对 dyad 的 "we" 是对比性的**（we vs. them）。成对分量确实为 0，而**群体级 "we" 极高**。→ `P1` 作为 **pair** 容器读出来是 0，**恰好在现象最强的时候读数最错**。

同类问题见 `W`（专业）：professional dyad 的 "we" 通常是 team/org（Gehr et al. 显示 we-ness 强度本身是照护 dyad 的类型判别变量）。`S`/`K` 列：kin 的 "we" 常是 family 而非同胞对（de Bel et al. 的 loyalty conflict；Voorpostel & Blieszner 的"第二梯队"）。

> 修复不是给 P1 加语义，而是承认 **`PairState` 按定义是 pair 级容器，而敌对/合作/kin 三类 dyad 的 "we" 的自然归属是 group 级**。
> **Proposal（仅提案）**：允许 `CohesionScope ∈ {pair, subgroup, coalition}`。

### 3.7 `Role / Institution` 目前是 query lens，但对 ≥3 类 dyad 它是**状态成分**

`AGENTS.md`「Current architecture direction」第 3 条：`Keep Role explicit as a query/evaluation lens; it does not replace world state.` 本 audit 认为这条在**专业 / 亲属 / 照护**三类 dyad 上不成立 —— 约束、依赖、行动空间都是 role 决定的：

- Dykstra：代际 dependence 由**法律与政策**构成（pair/institutional fact，不是 query lens）。
- Meyer & Allen (1991)：role-based commitment 必须在三成分间拆分，否则欠定。
- Horvath & Symonds (1991) / Flückiger et al. (2018)：专业治疗 dyad 中与结果最稳健相关的 dyad 变量是 **working alliance**（共同目标 + 协作纽带 + 共情理解）—— **任务/角色**构念，不是 affective dyadic state。
- Olson, Russell & Sprenkle (1983)：家庭/婚姻系统研究主坐标是 cohesion + adaptability + communication，**不是 love 模型** → 家庭 dyad 领域实际已用 role-结构坐标替代 affective 坐标。

> 这是对**现有架构裁决的挑战**，不是变更提案。
> **Proposal（仅提案）**：保留 `Role` 作为 query lens，新增 `RoleContract_(A,B)` pair fact（角色、期限、权限、scope of practice、单方终止权），并让 `Dedication`/`OutcomeDependence` 的读法显式声明依赖它的哪一成分。

### 3.8 `source / target / edge` facet 方案在亲属 dyad 上不可识别

`CONSTRUCT_SCOPE_DIRECTIONALITY.md` §1：

```text
Construct(i -> j, t)
= population baseline
+ source_i
+ target_j
+ directed_dyad_(i->j)
+ context/history residual
```

SRM 式分解的可识别性要求两条隐含条件：**(a) target 的属性与 source 对该 dyad 的进入/选择近似独立；(b) dyad 可重新选择。** 在亲属 dyad 上两条按构造成立地失败：

- 兄弟姐妹共享父母 → `target_j` 的部分属性由 i 自己历史中的第三方产生。de Bel et al.：`both intergenerational relationships (father–child and mother–child) turn out to be important predictors for the sibling relationship`。
- Voorpostel & Blieszner (2008)：同胞支持是"第二梯队"，质量依赖核心圈层。
- Hillcoat-Nallétamby et al.：mid-life parent–adult-child 的两个 solidarity 维度 `are weakened by parental divorce and separation` —— 被父母 dyad 的状态决定。
- Montgomery et al. (1997)：`the lifelong history of parent-child relationships influences who is drawn into the role of caregiver`。
- 照护域更极端：受照护者的 `CareNeed` 很大程度上**由照护者的行为与制度安排产生** → S 与 T 不可分离。

**结论：在亲属/照护 dyad 上，上式中的 `context/history residual` 不是残差而是主项；`target_j` 不能读作 Agent 层 trait。** 这意味着 `CURRENT_ARCHITECTURE.md` §5 的 `target component: 某人一般多容易诱发他人吸引` 在 kin/care 上**没有可识别含义**。§5 允许"并非每个构念都四项齐全"，但真正的问题是 **facet 方案本身在 dyad 类型之间不不变**。

> **可证伪推论**：若 kin dyad 上 `target_j` 仍可识别为 Agent trait，则同胞对的"target 诱引力"应能预测跨家庭（不同父母、不同家庭）结果；de Bel et al. 的 549 triad 设计与 Voorpostel & Blieszner 的"第二梯队"结论都预测**不可**。
> **Proposal（仅提案）**：给 Agent-level facet 加 `dyad_type_scope` 标签；`AgentState` 不再被当作跨 dyad 类型的公共底座。

---

## 4. 域泄漏风险排序

排序依据：**(未检验的恋爱框架假设量) × (被显式写进 schema 的程度) × (误读后果的严重度，含安全)**。

### L-1（最高）· `OutcomeDependence` 内建了自愿退出 + 开放选择集 + 共享未来

项目原文（`PARAMETER_CONVERGENCE_V0_1.md` §4 D8）：

> **语义：** i 的重要结果、福利、机会或生活状态在多大程度上依赖于 j / 该关系。
> **Open question:** 某些 dependence 是否应完全由 Agent resources / **alternatives** / institutional constraints 推导。

`alternatives` 是 Rusbult 选择集的直接残留，而选择集是**婚配市场**产物：

| dyad | D8 的语义实际是什么 |
|---|---|
| 友谊 | Silver：友谊承诺 `grounded in open-ended commitments without explicit provision for their termination` → `alternatives` 近乎无定义 |
| 兄弟姐妹 | `Laws define the relationships of dependence and interdependence between generations and gender`；`impose` 与 `choice` 并存 → 同一 D8 高值在两个法域语义相反 |
| 亲子 | 依赖方向随生命历程**可逆**（`young adults should not be solely looked upon as dependants, but also as givers of support and care to their parents and grandparents`）；directed 表示在老年段整体反向，而构念名不变 |
| 照护 | dependence 是**被设计的**定义特征；受照护者的 dependence 部分由照护者造成 → S/T 不可分离（与 §3.8 同源） |
| 前任 | Hardesty et al. 显示 post-separation 承重变量仍在 → **neutral 读法在这里是安全隐患** |
| 专业 | dependence 由 role / org / license 定义，**不是 person-to-person**；directed 状态强制了人的读法 |
| 敌对 | dependence 可以是**被强加的**（人身控制、勒索、囚禁）。措辞读起来是关于 i 的 option set 的中性事实，**而它实际是伤害结构本身** |

**并带出一个 readout 中立性缺陷（不是 primitive 缺陷）**：`R2 PowerImbalance = f(Dependence_A→B, Dependence_B→A, alternatives, resources, constraints)`。一个**健康的高照护 dyad**（受照护者高度依赖、方向不对称、替代方案少）与一个**胁迫 dyad**（intimate terrorism）在 D8 上**数值结构相同**，R2 会打成同一类，而它们在伤害上相反。`AGENTS.md` 说 readout 是下游产物，但**被命名的 readout 会被当成发现**。

> **Proposal（仅提案）**：所有 readout 携带 `dyad_type_scope` 与 `valence_not_defined_here` 标记；`D8` 定义显式声明其 `alternatives` 项的 `reference_class`。

### L-2 · `ConstraintsAndAgreements` / `Boundary / Exclusivity Rules` 内建 consent，且示例集是纯性/婚恋

项目原文（`CURRENT_ARCHITECTURE.md` §3；`PARAMETER_CONVERGENCE` §6 P5）：

> `ConstraintsAndAgreements`
> **P5. Boundary / Exclusivity Rules** — `如性排他、情感排他、财务约定、婚前性行为边界等。`

§2 已把 `违法或违反社会规范` 的关系写入域，但容器名与示例集都假定"约束来自协议"。P5 的示例集在 8 类非恋爱 dyad 上基本全无对应物：

| dyad | 真正的边界对象 | P5 现有示例覆盖？ |
|---|---|---|
| 友谊 | 规范规则（Argyle & Henderson friendship rules）—— **规范**，不是协议 | ✗ |
| 兄弟姐妹 | 财产 / 继承 / 代父医疗决策权 | ✗ |
| 亲子 | 谁决定手术、谁持证件、监护安排 | ✗ |
| 照护 | scope of care、同意能力、离护条件 | ✗ |
| 前任 | no-contact / no-harass —— 典型是**单方**（保护令） | ✗（方向反了） |
| 专业 | role scope、保密义务、执业边界、转介终止 | ✗ |
| 敌对 | rules of engagement、最后通牒 | ✗（单方强加） |

Silver 另给出一个直接反例：友谊理想 `grounded in open-ended commitments without explicit provision for their termination` —— **协议化的终止条件恰恰是友谊理想所排除的东西**。把 friendship 的"规则"当成 `Agreements` 会引入一个 friendship 按定义不存在的成分。

### L-3 · `Dedication` 内建了自愿、可持续终止、person-specific、共享未来

项目原文：

> **D7. Dedication** — **语义：** i **主动**希望维持、维护并继续该关系的**内在**关系性承诺/投入意愿。
> **为什么保留：** Investment Model 明确提醒 commitment 不能与 investment、constraints、**alternatives**、satisfaction 混为一体。

四个假设在 6 类 dyad 上失效（详见 §3.2）。此外：

- **前任**：`Dedication` 在前任 dyad 上**不是 0 且是承重的**（Tan et al. 2014），但解释框架从"关系持续性"换成"解体后维护"。
- **敌对**：定义是"希望维持该关系"，无法表达**长期的定向敌意**。项目无对应 primitive。这不是 readout 问题。

### L-4 · `RomanticAttraction` / `SexualDesire` 是唯一两个按名称锚定恋爱的候选

- **专业 dyad 的 power asymmetry**：在治疗、师生、医患、雇佣 dyad 中，romantic/sexual state 不是可对称表示的关系坐标，而是**角色越界 / 风险**状态。按对称 directed state 表示会**正常化**它。
- **照护**：`SexualDesire` 判 `MS` —— 受照护者对照护者的性吸引是文献记载的类别（含失智相关去抑制），且是**保护**议题；当普通 desire 坐标表示会丢风险语义。
- **Agent 层 `baseline libido`**：这是**对所有 Agent 都开槽**的属性，等于假定每个 Agent 都是潜在性关系对象。在同胞/专业/敌对数据集上 (a) 不可测、(b) 无关、(c) **一旦被插补就构成伤害**（`AGENTS.md` 明禁）。与 L-1 同属"schema 存在即邀请错误插补"。
- **Agent 层 `sex / gender-related attributes`**：单一未标注槽同时承担三种 dyad 相关量（角色/权力不对称结构、吸引相关信号、自我认同），在 9 类 dyad 上作用方向不一致。

### L-5 · `Relationship Identity` 枚举同时漏类型、混种类，且与 §2 写入域自相矛盾

项目原文（`PARAMETER_CONVERGENCE` §6 P4）：

> 例如：`friend` / `exclusive romantic partners` / `engaged` / `married` / `open relationship` / `care arrangement`
> 当前判定：`KEEP as pair/institutional agreement fact`

- **与写入域矛盾**：`CURRENT_ARCHITECTURE.md` §2 明确写入 `同事、前任、第三者、敌对、照护、合作`，枚举里**没有** `sibling`、`adult child / parent`、`co-parent`、`estranged`、`therapist–patient`、`supervisor–supervisee`、`teacher–student`、`rival`、`enemy`、`litigant`。→ **架构声明的域比它自己的 identity 枚举宽。**
- **种类混装**：一个列表混了三种事实 —— (a) 自愿关系角色、(b) **法律/制度状态**、(c) **功能安排**。因为混装，`pair/institutional agreement fact` 不是一个同质层。
- **`care arrangement` 是单例，而文献说照护 dyad 本身异质**：EUROFAMCARE 得到 **seven "caregiving situations"**；Nolan/Grant/Keady 另有一套 typology；Gehr et al. 给出 3 型；互惠研究给出 4 种变体。把 `care arrangement` 当作一个 identity 是**类别错误**。

### L-6 · `Liking` 在恋爱/友谊中**部分是成员判据**而不是坐标

`Liking` 语义干净（`不预设浪漫或性`；`朋友/亲属/同事均适用`），但 Fehr 的友谊定义包含 `the two parties like one another` → 在友谊上 "Liking 低" 首先意味着"这还不是友谊"（**类型判定**），而不是"友谊质量低"（**程度**）。同理 `exclusive romantic partners` 把"互相喜欢"当作前置条件。

这不是 `MEANING_SHIFTS`（语义没变），是 **readout 的类型敏感性**：同一个坐标值在恋爱/友谊里"低"与"零"的分界不同，在敌对 dyad 里又不同。→ 任何跨 dyad 类型的"低 Liking 意味着坏关系"的 readout 都是**错的**。

### L-7 · `PPR` 的名称泄漏（定义不泄漏）

定义是通用的（`i 是否感到 j 理解、重视、回应自己的需要与核心自我`），泄漏在词 `Partner`，以及 Laurenceau et al. (1998) 的原始三元模型与全部因果后果都在恋爱 dyad 上建立。**并且本次检索未找到任何在友谊/亲属/照护 dyad 上验证过同一模型的工作**（§6 U2）→ 该行 F/S/K/C 列是 `UNKNOWN`，不是 `MP`。把 PPR 放在 Belief 层是**正确的缓解**，但"perceived 的是 partner"会被下游默认带进所有 dyad。

### L-8（最易修）· 项目自己的 cross-context gate 有采样框架漏洞

- `CONSTRUCT_SCOPE_DIRECTIONALITY.md` §7 第 6 项：`same-sex / opposite-sex / kin / non-kin / stranger / established relationship`
- `PARAMETER_CONVERGENCE_V0_1.md` §2.4：`same-sex / opposite-sex、kin / non-kin、stranger / established relationship、romance / friendship / caregiving / conflict`
- `PARAMETER_CONVERGENCE_V0_1.md` Gate B：`same-sex / opposite-sex / kin / non-kin / friendship / romance / caregiving / conflict / unilateral attraction / high-dependence/low-liking / high-attraction/low-trust`

三处清单**互不相同**，且**都不含** `sibling`、`parent–adult-child`、`ex-partner`、`professional/cooperative`、`adversarial/harm-asymmetric`、`dating-stranger`。Gate B 的 `unilateral attraction` 也是恋爱框架词（单向的 attachment / security / care 在 kin 里同样存在且更重要）。

**后果**：本 audit 审计的 9 类 dyad 中，**有 5 类目前根本没有被项目自己的验证门指定**。→ Gate B 通过**不构成**"跨域稳定"的证据。

### L-9 · `X_(S,O,t) = Phi_(S,O)(WorldState(t))` 的二人局部投影在 ≥4 类 dyad 上不足

- 亲属：de Bel et al. 的 loyalty conflict（同胞必须在父母 dyad 与同胞 dyad 之间选边）；Voorpostel & Blieszner 的第二梯队；Hillcoat-Nallétamby et al.
- 照护：Pruchno/Burant/Peters 发现高一致 vs 低一致家庭的照护结果显著不同，low-agreement 家庭中"大多数关系不显著"；互惠的 constructed 变体**只**在受照护者身上出现 → 需要第三方（家庭、机构）作为解释变量。
- 敌对：`Cohesion` 的 "we" 在 group 级。
- 前任：post-separation 变量由制度（保护令 / 执法）驱动。

世界层是 `Agents + Relationships + Environment`，`Role` 是 query lens —— 所以这**不是 ontology hole，是 query lens 太窄**。但结果是：当前 `S/O/D/E` 静默假设了一个 **dyad-internal 过程**。

### L-10 · Agent 层 `family obligations` 是**层级错置**

代际 obligation 由**法律**构成（Dykstra），是 pair/institutional 层事实。放在 Agent 层会导致 (a) 同一家庭两个成员得到不同值、(b) 无法表示"法律上存在但本人不承认"、(c) 方向性丢失（谁对谁有义务）。

### L-11（次要）· `Satisfaction` / `GoalAlignment` 的**跨域极性不稳定**

- 照护域：双方报告一致度调节几乎所有结果；low-agreement 家庭中大多数关系不显著 → 任何建立在双方报告上的 readout 都需先声明一致性。
- 敌对/照护域：dyad 类型是**交互项**的函数（`based entirely on control context, not frequency or severity`；类型由 burden × coping × motivation 组合决定）→ `GoalAlignment = 0` 在敌对 dyad 里可以意味着"目标高度一致（共同对付第三方）"。`GoalAlignment` 语义保住了，但**它的好/坏极性跨 dyad 类型不稳定** → 绝不可当质量指标。

---

## 5. 跨域稳定性更好的构念（候选）

| 排名 | 构念 | 证据 | 建议（均为 proposal） |
|---|---|---|---|
| 1 | **`Obligation / Duty Orientation`（缺失）** | Cicirelli 1993; Montgomery et al. 1997; 互惠研究 1995; Gehr et al. 2021; Meyer & Allen 1991 | 新增为 directed construct；`Dedication` 收窄为 affective dedication |
| 2 | **`Liking`（已在 basis）** | de Bel et al. 2019（warmth 与 conflict 正交）；Blake et al. 2022（当事人自陈"爱他但不喜欢他"） | 升为跨域基座；同时为 L-6 的 readout 类型敏感性加护栏 |
| 3 | **`Caregiving`（已在 basis）** | 整个照护学派测量族都建在这里 | 定义去掉"关系性"限定；motive attribution 拆为独立 belief |
| 4 | **`Secure-base / felt security`（D5 的一侧）** | Feeney et al. 2013（partner/parent/friend 多组合）；Cicirelli 1993 | secure-base 侧面升为跨域基座；"chosen vs ascribed attachment figure"写成显式 qualifier |
| 5 | **`Constrainedness / Control-Asymmetry`（缺失）** | Johnson 2006; Dutton et al.; Hardesty et al. 2015 | 新增为 directed structural construct；**安全价值最高** |
| 6 | **`Ambivalence`（当前隐含）** | Bengtson et al. 2002; de Bel et al. 2019; Blake et al. 2022 | 升为命名状态，或强制所有 quality readout 标注"kin/care 的 modal 状态是 ambivalent" |
| 7 | **`Structural + Associational Solidarity`（`PairState` 无对应）** | Bengtson & Roberts 1991; Silverstein & Bengtson 1997; Voorpostel & Blieszner 2008; Hillcoat-Nallétamby et al. | `PairState` 在 kin/care 域的候选主轴 |
| 8 | **`Belonging / social embeddedness`（不在 basis）** | Walton & Cohen 2011, *Science*, doi:10.1126/science.1198364；Brady et al. 2020, *Science Advances*, doi:10.1126/sciadv.aay3689 —— 有**随机实验因果证据**、跨 classroom / college / 成年长期场景 | 值得进入候选池；跨域证据基础强于 LHRM 现有若干候选 |
| 9 | **`Shared-goal / collaborative-task state`（不在 basis）** | Horvath & Symonds 1991; Flückiger et al. 2018 | `GoalAlignment` 之外需要一个 **perceived、directional** 的 shared-goal 坐标；本次**未取得** alliance 单向性原文 → `UNKNOWN` |
| 10 | **`Reconciliation / forgiveness`（不在 basis）** | 本次无已核实指针 | 只登记为待查缺口（§6 U4），不作任何主张 |

**反向结论（值得写进定位章节）**：`RomanticAttraction` / `SexualDesire` 的**测量基础**几乎全部在恋爱/约会 dyad 上生成（Laurenceau et al. 1998；Bruch & Newman 2018）；`Dedication` 的理论骨架来自一个**婚配选择集**模型；P4 枚举、P5 示例集、Agent 层 `baseline libido` 三处是纯婚恋/性框架。→ **越是"关系科学核心"的构念，恋爱框架依赖越深。** 这与"通用关系模型"的目标方向相反。

---

## 6. 采样框架后果

> **如果一个构念只在部分 dyad 上存在，那么数据集不重新指定（re-specify）就不能跨 dyad 类型比较。**

这不是"注意一下"，是一条会**静默出错**的推论。

1. **共享坐标 schema + 构念的条件存在性 = 同一个向量在不同 dyad 类型上语义不同。** 任何把恋爱样本与同胞样本拼在一起的 pooled 分析比较的是**不可比的量**，偏误方向由**过采样哪种 dyad 类型**决定。矩阵中 `RomanticAttraction` 有 2 个 `NA`+3 个 `MS`、`SexualDesire` 有 4 个 `NA`、`OutcomeDependence` 有 1 个 `NA`+5 个 `MS`、facet 方案有 5 个 `MS` —— pooled 估计在这些行上**没有定义**。

2. **同一份 instrument 在不同 dyad 类型上测的不是同一个构念。**
   - **`Dedication` 的 Investment Model 三件套**（satisfaction / investment / **alternatives**）不能直接搬到友谊/亲属/专业：`alternatives` 在友谊上近乎无定义（Silver），在亲属上为空（ascriptive），在专业上被 role contract 替代（Meyer & Allen）。
   - **`Trust` 定义的"愿意把某类脆弱性暴露给 j"** 内建了**披露史**前提。`I don't really know my brother`（基因同胞、30+ 年共存、零披露史）说明在 estrangement / 同胞 / 纯合同 dyad 上**同一量表会测到别的东西**。这一格判为"定义欠定"，不是"数据缺失"。
   - **Rempel 式 dyadic trust 三维（competence / benevolence / integrity）**是**关系内他人属性归因**；在专业 dyad 上被测的是 role-holder 的 competence / reliability，标的人不是同一个人。
   → 这不是"噪声大一点"，是 **construct validity 失败**。

3. **`Gate A`（Case Bank）与 `Gate B` 同样不能跨 dyad 类型 pooled。** 需要 per-dyad-type 的 coverage baseline，且 Gate B 清单要先补齐 L-8 列出的 5 类。

4. **对本项目最有利的推论**：这一节为 representation-first invariant 提供了**独立于哲学立场的经验理由**。`AGENTS.md` 的 `Representation before scalarization; state-space before score` 通常被当作原则性偏好；本 audit 给出的理由是**经验性的**：只要构念的条件存在性存在，跨 dyad 类型的标量距离与分数就**不是**同一个量的函数，因此 §11 列为非目标的 `Relationship Quality / Compatibility / Match Score` 的"跨类型"读法在数学上无意义。这与 §11 一致，且比 §11 更强。

5. **可执行的重指定清单（proposal）**：跨 dyad 类型数据集必须显式携带
   (a) `DyadTypeLabel`（且承认**多标签**：可以是 `sibling + caregiving + estranged`）、
   (b) `DyadScopeProfile`（有效坐标子集 + 每坐标 applicability）、
   (c) 每个比较型坐标（`ValueCongruence` / `GoalAlignment` / Investment Model 的 `alternatives`）的 **reference class 定义**、
   (d) 允许的 readout 集合（readout 不得跨 `dyad_type_scope` 复用）。
   缺 (a) 或 (b) 的数据集**不能**用于跨类型比较，也不应被用来"验证"通用 basis。

6. **一个反直觉的观察**：`Kelley et al. (1983)` 的 close-relationship 定义是 `strong, frequent, and diverse interdependence that lasts over a considerable period of time`。用它作**入样规则**，会把 (a) 敌对 dyad（长期相互依赖、频繁、diverse，只是方向为负）**纳入**，把 (b) **高强度但低互赖**的 dating dyad **排除**。→ LHRM 若需要一个 membership test，不能用 "close"，必须用 `PairExistence` + 依赖强度 + 时长三轴，且**符号不能进这个 test**。

---

## 7. 项目内部矛盾清单（供 Architect 直接处理）

| ID | 矛盾 |
|---|---|
| X-1 | `CURRENT_ARCHITECTURE.md` §2 写入域（含敌对 / 前任 / 同事 / 违法）⊃ §6 P4 的 identity 枚举 |
| X-2 | "不预设异性、陌生起点、婚恋目标" vs. P5 示例集全是性/婚恋、Agent 层 `baseline libido`、Gate B 的 `unilateral attraction` |
| X-3 | `AGENTS.md` "never silently coerce missing information into neutral values" vs. `Unknown` 是唯一非数值值类 → 结构性不适用**必然**被 coerce 成 0 |
| X-4 | §2 "允许…违法或违反社会规范…关系结构" vs. 约束层被类型化为 `ConstraintsAndAgreements` |
| X-5 | `AGENTS.md` "Role is a query lens; it does not replace world state" vs. Dykstra / Horvath / Meyer & Allen / Olson 显示 role/contract 在 ≥3 类 dyad 上是**状态**成分 |
| X-6 | `CONSTRUCT_SCOPE_DIRECTIONALITY.md` §1 的加法示意分解 vs. §6 "不预先承诺线性叠加"；本 audit 给出可证伪推论说 dyad 类型本身是交互项的函数 |
| X-7 | 三处 cross-context / Gate B 清单互不相同，且漏 5 类 dyad |
| X-8 | `Cohesion` 是 pair 级容器，但敌对 / 合作 / kin 三类 dyad 的 "we" 归属是 group 级 |

---

## 8. 本文件的证据与未知

**负结果（对项目不利，必须记录）**

- **未检索到**任何在友谊 / 亲属 / 照护 dyad 上验证过 perceived partner responsiveness 三元模型的工作。→ `PPR` 行 F/S/K/C 列判 `UNKNOWN`，**不**判 `MEANING_PRESERVED`。这直接反驳"Reis 模型天然跨域"这一常见假设。
- **未检索到**针对本 basis（或任何 8 维 directed dyad-state battery）的跨 dyad-type 测量不变性研究。→ 矩阵中所有 `MP` 仅为语义判断。**这是本文件最重要的单一空白。**
- **未取得**"敌对 human dyad 在 dyad（而非 group）层面可持续多年"的一手同行评议指针。→ "长期定向敌意是可持续状态"在本文中作为**架构论证**（basis 无对应 primitive）呈现，实证状态 `UNKNOWN`；本文件只支持"per-edge control 是定义性变量"这一条。

**本 lane 的自我更正**（记录以免下游引用错误指针）

- 治疗联盟综述作者是 **Ardito & Rabellino (2011)**，不是 Zalecki & Hall。
- coercive-control operationalization 论文是 **Hardesty, Crossman, Haselschwerdt, Raffaelli, Ogolsky & Johnson (2015)**，不是 Anderson。
- Horvath & Symonds (1991) 在 **Journal of Counseling Psychology 38(2):139–149**。
- Finkel, Hui, Carswell & Larson 的 suffocation 目标论文是 **Psychological Inquiry 2014, 25(1):1–41**。
- de Bel 等人的 triad 论文在 **Journal of Family Issues 40(18)**，作者 de Bel, Kalmijn, van Duijn (2019)。
- Meyer & Allen (1991) 在 **Human Resource Management Review 1(1):61–89**。
- Flückiger et al. (2018) 的 alliance meta-analysis 在 **Psychotherapy 55(4):316–340**。

**能定案后续未知项的研究设计**

| ID | 未知项 | 能定案的研究 |
|---|---|---|
| U1 | 8 维 battery 跨 romance / friendship / kin / professional 是否**测量等价** | 4 组多组 CFA/invariance 序列（configural → metric → scalar），每组 ≥300 dyad，两方向分别估计。**应在 Gate C 之前先做。** |
| U2 | PPR / perceived other responsiveness 是否在 F/S/K/C 上与 self-disclosure 构成同一因果模型 | 4 组配对日记或频次感知测量，检验三段链系数是否跨组等值 |
| U3 | 成形前 dyad 能否表示为 `PairExistence = proposed_*`，且与成形后取值同尺度连续 | 纵向网络约会数据 + 配对日记；需一个**允许 `mutuality` 为 Unknown 而非 False** 的潜变量模型（当前 basis 不允许） |
| U4 | 敌对 dyad 的长期性可否由"定向敌意持续状态"刻画 | 单例纵向 ≥3 年 + 敌意定向状态的自我报告与第三方行为双通道，对照组为已终止敌意 |
| U5 | `Trust` 在零披露史 dyad 上"高信任"是否可能存在 | 同一 dyad 内操纵披露量（low/high）的实验，测 relational trust；同时测 character-based / ascribed trust 作为替代读法 |
| U6 | kin/care dyad 中 obligatory vs affectionate 照护的权重与结果弹性 | Cicirelli (1993) 式分离测量基础上的结构方程：双路径 → caregiving behavior → burden/reward，外加第三/第四方调节 |
| U7 | `Cohesion` 的 "we" 在敌对/合作 dyad 中的归属层级 | 三组（romantic pair / professional team / adversarial coalition）配对测量 IOS + subgroup identity + pair cohesion |
| U8 | `Dedication` 三分后是否在**恋爱**样本上也可分离 | 3 组（romance/kin/professional）invariance 序列 + 判别效度；若恋爱样本上三因子不可分，则拆分是**域依赖**的 |
| U9 | `PowerImbalance` 在加入 constraint-asymmetry 后能否把健康照护 dyad 与胁迫 dyad 分开 | 照护 dyad（healthy vs conflicted）+ IPV 类型样本，用 `Dependence_asym` 与 `Constraint_asym` 两个独立轴分类 |
| U10 | 同性 / 跨性别 dyad 在 D1–D8 上是否有任何差异 | 把 U1 的 invariance 序列按性别组合分层（项目 Gate B 已列 `same-sex` 但从未执行） |
| U11 | 项目 Gate B 扩到 5 类新 dyad 后，8 维中会先被击穿哪几个 | 逐类跑 Gate B（sentence-level mapping），记录 `MAPPING_FAILURE`；预期首先暴露 D2/D3（scope）、P4/P5（容器）、A3/A4（层与 facet） |
| U12 | `Satisfaction` / `GoalAlignment` 的极性是否可跨 dyad 类型共享一个符号约定 | 5 类 dyad 上同时测 state 坐标与 subjective valence，检验符号约定是否随 dyad 类型翻转 |

---

## 9. 引用列表

Bruch, H. E., & Newman, M. E. J. (2018). Aspirational pursuit of mates in online dating markets. *Science Advances*, 4(7), eaap9815. doi:10.1126/sciadv.aap9815
Blake, L., Bland, M., & Rouncefield-Swales, J. (2022). Estrangement between siblings in adulthood: A qualitative exploration. *Journal of Family Issues*, 44(7), 1859–1879. doi:10.1177/0192513X211064876
Cicirelli, V. G. (1993). Attachment and obligation as daughters' motives for caregiving behavior and subsequent effect on subjective burden. *Psychology and Aging*, 8(2), 144–155. doi:10.1037/0882-7974.8.2.144
de Bel, D. F., Kalmijn, M., & van Duijn, J. J. (2019). Balance in family triads: How intergenerational relationships affect the adult sibling relationship. *Journal of Family Issues*, 40(18), 2707–2727. doi:10.1177/0192513X19860181
Dutton, M. A., Goodman, L. A., & Schmidt, R. J. *Development and Validation of a Coercive Control Measure for Intimate Partner Violence.* (研究总报告，开放 PDF: `niwaplibrary.wcl.american.edu/`)
Dykstra, P. A. Intergenerational family relationships in ageing societies. (开放获取综述章节)
Feeney, J., Collins, N. L., Van Vleet, T., & Tomlinson, T. M. (2013). Motivations for providing a secure base. *Attachment & Human Development*, 15(3), 261–280. doi:10.1080/14616734.2013.782654
Fehr, B. (1996). *Friendship Processes.* SAGE.
Finkel, E. J., Hui, C. M., Carswell, K. L., & Larson, G. M. (2014). The suffocation of marriage: Climbing Mount Maslow without enough oxygen. *Psychological Inquiry*, 25(1), 1–41. doi:10.1080/1047840X.2014.863723
Finkel, E. J., Simpson, J. A., & Eastwick, P. W. (2017). The psychology of close relationships: Fourteen core principles. *Annual Review of Psychology*, 68, 383–411. doi:10.1146/annurev-psych-010416-044038
Flückiger, C., Del Re, A. C., Wampold, B. E., & Horvath, A. O. (2018). The alliance in adult psychotherapy: A meta-analytic synthesis. *Psychotherapy*, 55(4), 316–340. doi:10.1037/pst0000172
Gehr, T. J., Freiberger, E., Sieber, C. C., & Engel, S. A. (2021). A typology of caregiving spouses of geriatric patients without dementia: caring, worried, desperate. *BMC Geriatrics*. doi:10.1186/s12877-021-02425-1
Hardesty, R. R., Crossman, A. M., Haselschwerdt, R. M., Raffaelli, C., Ogolsky, J. D., & Johnson, M. P. (2015). Toward a standard approach to operationalizing coercive control and classifying violence types. *Journal of Marriage and Family*, 77(3), 833–843. doi:10.1111/jomf.12201
Hazan, C., & Shaver, P. (1987). Romantic love conceptualized as an attachment process. *Journal of Personality and Social Psychology*, 52(3), 511–524. doi:10.1037/0022-3514.52.3.511
Hillcoat-Nallétamby, S., Dharmalingam, A., & Baxendine, S. Living together or communicating at a distance: Structural and associational solidarity between mid-life parent and adult child in New Zealand. (作者/年份未核)
Horvath, A. O., & Symonds, D. (1991). Relation between working alliance and outcome in psychotherapy: A meta-analysis. *Journal of Counseling Psychology*, 38(2), 139–149. doi:10.1037/0022-0167.38.2.139
Johnson, M. P. (2006). Conflict and control: Gender symmetry and asymmetry in domestic violence. *Violence Against Women*, 12(11), 1003–1018. doi:10.1177/1077801206293328
Kellas, C. M., Bean, R. A., Cunningham, M. R., & Cheng, K. Y. (2008). The ex-files: Trajectories, turning points, and adjustment in the development of post-dissolutional relationships. *Journal of Social and Personal Relationships*, 25(1), 23–50. doi:10.1177/0265407507086804
Laurenceau, J.-P., Barrett, L. F., & Pietromonaco, P. R. (1998). Intimacy as an interpersonal process. *Journal of Personality and Social Psychology*, 74(5), 1238–1251. doi:10.1037/0022-3514.74.5.1238
Meyer, J. W., & Allen, N. R. (1991). A three-component conceptualization of organizational commitment. *Human Resource Management Review*, 1(1), 61–89. doi:10.1016/1053-4822(91)90011-z
Montgomery, A. W., Havvey, J. E., & Kosloski, R. L. (1997). Profiles in caregiving: The unexpected career. In R. D. Miller & S. M. Gillies (Eds.), *Making Hard Decisions*. Oxford University Press. (本次经非出版方镜像读到文本，需合法渠道复核)
Nolan, M., Keady, J., & Grant, G. (1996). Developing a typology of family care. *Journal of Advanced Nursing*, 23, 950–961.
Olson, D. H., Russell, D. R., & Sprenkle, D. H. (1983). Circumplex model of marital and family systems: VI. Theoretical update. *Family Process*, 22(1), 69–83. doi:10.1111/j.1545-5300.1983.00069.x
Pietromonaco, P. R., & Perry-Jenkins, E. (2014). Marriage in whose America? What the suffocation model misses. *Psychological Inquiry*, 25(1), 108–113. doi:10.1080/1047840x.2014.876909
Pruchno, R. A., Burant, C. J., & Peters, N. D. (1997). Typologies of caregiving families: Family congruence and individual well-being. *Family Relations*. (DOI 未核)
"Reciprocity and Social Support in Caregivers' Relationships: Variations and Consequences" (1995). *Home Health Care Services in Aging*. doi:10.1177/104973239500500306 (作者名未取得)
Reis, H. T. (Ed.). *Handbook of Relationship Science*. (章节前言 "Close relationships", publisher preview)
Rodriguez, L. M., Øverup, C. S., Wickham, R. E., Knee, C. R., & Amspoker, A. B. (2016). Communication with former romantic partners and current relationship outcomes among college students. *Personal Relationships*, 23(3), 409–424. doi:10.1111/pere.12133
Silver, A. Friendship and trust as moral ideals: An historical approach. (开放 PDF: `voidnetwork.gr`)
Tan, K., Agnew, C. R., VanderDrift, L. E., & Harvey, S. M. (2014). Committed to us: Predicting relationship closeness following nonmarital romantic relationship breakup. *Journal of Social and Personal Relationships*, 32(4), 456–471. doi:10.1177/0265407514536293
Voorpostel, M., & Blieszner, R. (2008). Intergenerational solidarity and support between adult siblings. *Journal of Marriage and Family*, 70(1), 157–167. doi:10.1111/j.1741-3737.2007.00468.x
Walton, K. E., & Cohen, G. L. (2011). A brief social-belonging intervention improves academic and health outcomes of minority students. *Science*, 331(6023), 1447–1451. doi:10.1126/science.1198364
Whiteman, S. D., McHale, S. M., & Soli, A. R. (2011). 兄弟姐妹关系理论综述. PMC3127251
Bengtson, V. L., Giarrusso, R., Mabry, J. E., & Silverstein, M. (2002). Solidarity, conflict, and ambivalence: Complementary or competing perspectives on intergenerational relationships? *Journal of Marriage and Family*, 64(3), 568–576. doi:10.1111/j.1741-3737.2002.00568.x
Bengtson, V. L., & Roberts, J. A. P. (1991). Intergenerational solidarity in aging families: An example of formal theory construction. *Journal of Marriage and the Family*, 53(4), 856–870. doi:10.2307/352993
Silverstein, M., & Bengtson, V. L. (1997). Intergenerational solidarity and the structure of adult child–parent relationships in American families. *American Journal of Sociology*, 103(2), 429–460. doi:10.1086/231213
Leib, E. J. Friendship and the law. *Fordham Law Review*. (开放 PDF: `ir.lawnet.fordham.edu`)
Geyer, S., et al. (1999). A typology of caregiving situations and service use in family carers of older people in six European countries: The EUROFAMCARE study. *GeroPsych*, 24(1). doi:10.1024/1662-9647.a000031
Aron, A., Melinat, E., Aron, E. N., Vallone, R. D., & Bator, R. J. (1997). The experimental generation of interpersonal closeness. *Personality and Social Psychology Bulletin*, 23(4), 363–377. doi:10.1177/0146167297234003
Park, J., Sanchez, K., & Bryndilsen, K. (2011). Maladaptive responses to relationship dissolution: The role of relationship contingent self-worth. *Journal of Adolescent Research*. (开放 PDF: `ubwp.buffalo.edu`)
Argyle, M., & Henderson, M. (1984). *The Anatomy of Friendship.* Routledge.（经二次转引使用）
Ardito, A., & Rabellino, U. (2011). Therapeutic alliance and outcome of psychotherapy. *Frontiers in Psychology*, 2:70. doi:10.3389/fpsyg.2011.00270
Brady, G., Cohen, G., Jarvis, J., & Walton, K. (2020). A brief social-belonging intervention in college improves adult outcomes for Black Americans. *Science Advances*, 6(18). doi:10.1126/sciadv.aay3689

---

## 10. 非主张与剩余未知（汇总）

- 不主张 8 维 basis 在恋爱域之外是错的；最可能结论是**大部分语义可保**，主要缺陷在 basis 之外的容器。
- 不主张任何 `MEANING_PRESERVED` 已被验证；所有 `MP` 是**语义判断**，不是**心理测量判断**。
- 不主张 `SexualDesire` 在亲属 dyad 上"为 0"；主张的是当前 schema 无法把它与 `Unknown` 区分。
- 不主张 PPR 跨域无效；主张的是**未找到**支持其跨域的证据。
- 不主张 therapeutic alliance 是单向知觉构念（未取得原文）；只主张它是一个任务/协作型、结果关联最稳健的专业 dyad 变量。
- 不主张"长期敌意是可持续状态"有实证支持；只主张当前 basis 无对应 primitive。
- 不主张 IPV 类型学可直接迁移到一般 Human Dyad；只把它用作"承重变量可以是 per-edge 约束能力"这一结构事实的反例。
- 不主张任何矩阵格是最终判定；每条 `MP`/`MS` 都对应 §6 的一个可定案研究。
- 不主张对 canonical 文档做任何变更。
