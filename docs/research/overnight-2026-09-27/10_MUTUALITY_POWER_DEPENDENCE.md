# 10 — 互惠、不对称、权力与依赖的涌现：pair-level 现象能否由两条有向状态派生

**Status:** `RESEARCH_CANDIDATE` / NOT FROZEN
**As of:** 2026-09-27
**Lane:** R10（Wave 1）
**Work Order:** `youling/lhrm#30@overnight-opencode-exploration-swarm-v1`
**Input docs（只读）:** `AGENTS.md`、`docs/foundation/CURRENT_ARCHITECTURE.md`（rule 4–5）、`docs/foundation/CONSTRUCT_SCOPE_DIRECTIONALITY.md`、`docs/foundation/RELATIONSHIP_EVALUATION_FOUNDATION.md`、`docs/foundation/PARAMETER_CONVERGENCE_V0_1.md`

> 本文件**不是** canonical architecture，**不是**参数表，**不是**已确立结论。
> 本文件不修改任何 canonical doc。文中所有派生式都是**可被后续数据 falsify 的形式猜测**。
> 本文件不主张任何公式、权重、距离、阈值、概率已被科学确立。

---

## 1. 本 lane 要回答的问题

`CURRENT_ARCHITECTURE.md` rule 4 规定：

```text
Model directed relation states separately: i->j and j->i are independent;
mutuality/asymmetry are preferably derived.
```

`PARAMETER_CONVERGENCE_V0_1.md` 给出三个具体判决：

```text
R1  mutual attraction / reciprocal desire / trust asymmetry
    -> DERIVED: H(Z[k,A,B], Z[k,B,A])

R2  power / power imbalance
    -> f(OutcomeDependence(A->B), OutcomeDependence(B->A), alternatives, resources, constraints)
    -> 不先设独立 power 值

P1  cohesion / we-ness
    -> KEEP_CANDIDATE / contested scope
```

本文件逐条追问：**这些「派生」到底能不能做？做不出来的地方，就是真正需要独立 pair state 的地方。**

判别标准只有一条，且必须可 falsify：

> **一个 pair-level 现象 X 可被派生，当且仅当存在一个函数 H，使得在给定两条有向状态与已知 shared pair facts 后，H 的取值与 X 的观测值在统计上不可区分。**
> 反之，若给定这些输入后 X 仍有稳定剩余方差，则 X 是独立 pair state 的候选。

---

## 2. 记号（本文件的研究候选记号，非 canonical）

```text
D_k(i->j, t)     构念 k 在有向边 i->j 上的状态            [LHRM 已有概念]
R_k(i, t)        构念 k 的 source / perceiver 分量        [LHRM 已有概念]
T_k(j, t)        构念 k 的 target 分量                    [LHRM 已有概念]
e_k(i->j, t)     边的 dyadic 残差 = D_k(i->j) - R_k(i) - T_k(j)   [本文件提出，仅作 readout]
                 （来自 Social Relations Model 的 relationship effect）
B_i(X)           i 关于 X 的信念                          [LHRM 已有层]
T_i(i->j, t)     i 相对 j 的体验性权力 / 顺从感           [本文件提出]
Omega(S)         情境 S 的客观互赖结构                     [本文件提出，本体层缺口]
Phi(i, j, t)     shared pair facts：制度事实、约定、规范、
                 分工、第三极、领域分区                   [LHRM 已有层]
```

**重要区分（贯穿全文）：**

```text
D_k(i->j)        是 LHRM 的 primitive
e_k(i->j)        是 measurement / readout 层
Mutuality_k      是 derived readout
```

`e_k` 的残差化**不是** ontology 主张，而是测量层操作。把它与 primitive 混为一谈是本文件要避免的错误（见 §9.10）。

---

## 3. Interdependence Theory 提供的原语，以及一个被忽略的第三类东西

Kelley 与 Thibaut (1978) 用 **interdependence matrix** 表达情境：一个结果由哪些来源决定——actor control（自己的行为）、partner control（对方的行为）、joint control（共同行为）。随后 Kelley 等人 (2003) 把情境间的差异定型为**六个结构维度**：

```text
level of dependence        依赖程度
mutuality of dependence    依赖的相互性
basis of dependence        依赖的基础（partner control vs joint control）
covariation of interests   利益一致 vs 冲突
temporal structure         未来互赖
information certainty      信息确定性
```

这些是**情境**的维度，不是人的维度。`van Lange & Rusbult (2011, p. 255)` 的表述可以直接引用：

> 「Mutuality of dependence describes whether two people are equally dependent upon one another. **Nonmutual dependence entails differential power**: when Mary is more dependent, John holds greater power.」

> 「The less dependent partner tends to exert greater control over decisions and resources, whereas the more dependent partner carries the greater burden of interaction costs (sacrifice, accommodation) and is more vulnerable to possible abandonment; threats and coercion are possible.」

**这里有一个必须显式指出的结构事实：**

```text
variation of outcomes
  = actor effect  (自己的行为)
  + partner effect (对方的行为)
  + actor x partner interaction
```

这个三段分解与 Social Relations Model 的 perceiver / target / relationship effect **完全同构**（`Kelley, Holmes, Kerr, Reis, Rusbult & Van Lange, 2003`；`Kenny, 1988`）。也就是说：

> LHRM 已经有 `D_k(i→j)` 与 `D_k(j→i)`，但**没有** `actor × partner interaction` 这一层的**情境**表示。

后果是可证伪的：**两个 dyad 可以有完全相同的两条有向状态，却处在结构上相反的情境中。** 如果 A 自己能决定结果（B 完全无法影响 A），A 对 B 有强烈的 desire；同样强度的 desire，若 B 的行为完全决定 A 的结果，则 A 的依赖是单向的。两条有向状态一样，情境结构相反。

因此本文件把「情境的客观互赖结构 `Omega(S)`」列为**本体漏洞**（ontology hole），不是构念漏洞（§8 G1）。

**主观侧的对应发现（对本项目有直接影响）：**

`Gerpott, Balliet, Columbus, Molho & de Vries (2018, JPSP 115, 716–742)` 用 242 个条目检验发现：人们（在情境内与情境外）**只能可靠区分 6 个维度中的 5 个**，缺 *coordination*（basis of dependence）。得到的主观互赖模型（mutual dependence / power / conflict / future interdependence / information certainty）仍能解释 24% 的合作方差，超出 DIAMONDS 模型。

这有两条含义：

1. **支持** LHRM 保留原始方向维度而不标量化（`AGENTS.md` representation invariant #1/#4）。
2. **警告**：任何 LHRM 的 pair 派生量，如果将来要声称「人们实际能感知 X」，必须先通过这 6→5 的有损检验。原始 6 维中有 1 维在主观层面不可分，把它当作可独立感知的 pair 状态会引入一个测量幻觉。

---

## 4. 逐现象 derivability 论证

每一项给出：**派生形式（可 falsify）**、**需要的额外 shared pair fact**、**判定**。

### 4.1 互惠性吸引 / 互惠欲望（mutual attraction / mutual desire）

**朴素派生（当前 R1 的写法）及其错误**

```text
MutualAttraction_(A,B) = H(D_att(A->B), D_att(B->A))
```

这个写法本身不定义 H。若取 `min` 或 `mean`，在原始边值上会**系统性混入**两个与本对无关的成分：

```text
D_att(A->B) ≈ R_att(A) + T_att(B) + e_att(A->B)
```

其中 `R_att(A)` 是 A 一般多容易被吸引，`T_att(B)` 是 B 一般多容易诱发吸引。Social Relations Model 明确把「双方都觉得对方特别有吸引力」的**真正来源**定义为 **dyadic reciprocity = 两个 relationship effect 之间的相关**（`Kenny, 1988`），并把它与 **generalized reciprocity = perceiver effect × target effect 的相关**区分开。

Kenny & Acitelli (2001, JPSP 80, 439–448; N = 238 对约会/已婚伴侣) 提供了这条修正的实证必要性：

> bias 效应「considerably stronger, especially when the measure was linked to the relationship」；只有在与关系定义无关的变量（伴侣工作满意度、对家庭的感受）上 accuracy 才强于 bias；对 `satisfaction with sex` 而言，**「most of the accuracy was due to the assumption of similarity」**。

也就是说：一个人报告「我们互相都很有性吸引力」时，很大一部分是**投射**（假定相似），而不是对 `e_att(B→A)` 的准确知觉。

**修正后的派生（可 falsify）**

```text
Mutuality_k(A,B,t) = H( e_k(A->B,t), e_k(B->A,t) )
其中 e_k(i->j,t) = D_k(i->j,t) - R_k(i,t) - T_k(j,t)
```

**falsifier（可被后续数据推翻）：**
若在控制 `R_k(A), R_k(B), T_k(A), T_k(B)` 之后，`H(e_AB, e_BA)` 对任一 outcome 的增量预测力**不显著优于** `H(D_AB, D_BA)`，则残差化不必要，本条被证伪。

**需要的额外 shared pair fact：** 无。
**判定：`DERIVABLE`（但必须残差化）。** 这是本文件中派生最干净的一类。

### 4.2 广义互惠（generalized reciprocity）

```text
GeneralizedReciprocity_k = corr( R_k(i), T_k(j) )     # 跨 dyad
```

它是**跨 dyad** 的协方差，不是 pair-level 量。它是 SRM 的 nuisance 结构，LHRM 需要它是为了让 §4.1 的残差化可估计，而不是为了建模。

**判定：`DERIVED nuisance quantity`，不属于 LHRM ontology。**

### 4.3 不对称（asymmetry）及其测量

`CONSTRUCT_SCOPE_DIRECTIONALITY.md` §2 给出：

```text
Asymmetry_k(A,B) = distance( Z[k,A,B], Z[k,B,A] )
```

**这个表示形式有一个与 LHRM 自身 invariant 冲突的缺陷。** `AGENTS.md` representation invariant #4 规定：

> 「Do not force every coordinate into `0..1`, Euclidean space, or one common semantic scale.」
> 「A coordinate may be an interval, ordinal state, category, constraint, probability distribution, Unknown, or estimate + uncertainty + evidence.」

当 `Z[k,A,B]` 是区间、序数、类别、概率分布或 `Unknown` 时，`distance` **未定义**。这不是实现细节，是表示形式的合法性问题。

**修正后的表示（可 falsify）**

```text
Asymmetry_k(A,B,t) = {
  left      : e_k(A->B,t),
  right     : e_k(B->A,t),
  comparison: 由观测者显式声明的比较器 delta_k
              （可为序数、偏序、逐点支配、区间包含、分布重叠度…）,
  comparator_id,
  evidence / provenance,
  uncertainty
}
```

即：**asymmetry 是「带声明比较器的比较关系」，不是数字。**

**falsifier：** 若某任务（如 case-bank 检索、adversarial 覆盖测试）证明一个**声明过的**序数比较器与一个连续 `distance` 在该任务上无显著差异，则可以退回标量形式。该主张待测。

**额外 shared pair fact：** 无；但需要「坐标系是否允许跨 dyad 比较」的独立假设（`PARAMETER_CONVERGENCE` §2.4 scope stability 承担此项）。
**判定：`DERIVABLE`，但表示形式必须改。** 这与 rule 4 并不冲突（rule 4 只要求「preferably derived」，没要求 derived 量必须是标量）。

### 4.4 依赖不平衡（dependence imbalance）

**推导失败的地方在别处。** 互赖理论中的 dependence 不是人的状态，是情境结构（§3）。因此 `OutcomeDependence_(i→j)`（`PARAMETER_CONVERGENCE` D8）面临一个范畴问题。

Investment Model 提供了同一问题的另一种拆法（Rusbult, 1983, JPSP 45, 101–117）：

```text
satisfaction_i = rewards_i - costs_i
commitment_i  = satisfaction_i + investment_i - alternatives_i
```

注意 `alternatives` 是 commitment 的一个**独立减项**，不是 satisfaction 的函数、也不是 dependence 的函数。「我有多少更好的选择」与「我多在意这段关系」是两个正交量。

**修正后的表示**

```text
删除 directed primitive OutcomeDependence_(i->j)。
代之以：
  (a) Alternatives_(i, ref=(j))     [Agent + Environment 层，带对 (j) 的显式 pair 参照]
  (b) ValueOf_(i, j)                 [LHRM 已有：Liking / RomanticAttraction / Dedication 的加权视图]
  (c) Constraint_(i, j)             [LHRM 已有：P5 Boundary/Exclusivity / 制度事实]
  (d) Dependence_(i, j, S) = 情境 S 的结构 readout  [非心理状态]
  (e) PerceivedDependence_(i, j, S) = B_i( d )       [Belief 层]
```

**falsifier：** 给定 (a)(b)(c) 后，`OutcomeDependence_(i→j)` 是否仍携带稳定增量动态信息？若否，D8 冗余，本条成立。
**判定：`NEGATIVE` for D8 as directed primitive；`DERIVABLE` as readout。**

这正是 D8 自己标注的 open question（§4 D8：「某些 dependence 是否应完全由 Agent resources / alternatives / institutional constraints 推导」）。本文件的回答是：**是，应该。而且如果它被保留，它是 perception，不是 state。**

### 4.5 替代项 / 资源 / 约束

Interdependence Theory 的三个原语各自在 LHRM 中的位置：

| 原语 | 层次 | 现状 | 需要补的东西 |
| --- | --- | --- | --- |
| `alternatives` | Agent + Environment，带对 (j) 的 pair 参照 | `PARAMETER_CONVERGENCE` §7 列了 `income/assets/liabilities` 等，但未建模「相对 (j) 的替代质量」 | 需要一个**带参照的序数或集合值**结构（不是标量） |
| `resources` | Agent 层 | §7 有 | 需要 `Environment -> Power` 的显式映射（见 §5.5） |
| `constraints` | shared pair fact / institution | §6 P5 已有位置 | OK |

**关键观察：`alternatives` 同时驱动两件不同的事**

```text
(a) 依赖程度（离开的机会成本）
(b) 正当性 / legitimacy（能否诉诸第三方或更高权威）
```

`Johnson & Ford (1996, Social Psychology Quarterly)` 在 320 名被试的实验中把 subordinate 与 superordinate 的 alternatives 与 endorsement/authorization 正交操纵，结果：

> 「threat to leave is related **directly** to self and other alternatives, while evaluations of coalition formation, appeal to a higher authority … are related **directly** to the **legitimacy** dimensions.」

**含义：dependence 结构不足以决定一个人会用什么策略。** 一个人可以高度依赖对方，同时完全不使用威胁离开这一策略。这是 power 不可由 dependence 完全派生的**第二个**独立证据（第一个是 punitive power，§4.6.3）。

**判定：`DERIVABLE / structural`，无需新 primitive；但 alternatives 需要「带 pair 参照的序数/集合」表示，且 legitimacy 需独立表示。**

### 4.6 权力

这是本文件最长的部分，因为它给出**明确的部分否证**。

#### 4.6.1 零和分量：relative power —— 可派生

`Lawler & Bacharach (1987)` 与 `Lawler (1993)` 明确区分两个概念：

```text
relative power = power difference      （零和）
total power    = mutual dependence / "relational cohesion"  （非零和）
```

relative power 就是「谁的依赖更高」。它可以由两条有向依赖的不对称读出。
**判定：`DERIVABLE`。**

#### 4.6.2 非零和分量：total power —— 可派生但不能被 R2 的写法捕捉

`Lawler (1993)` 原文：

> 「In Emerson's terms, **total power constitutes the level of mutual dependence or 'relational cohesion' in the relationship.** Higher total power in a relationship essentially produces an increase in the opportunity costs associated with leaving the relation.」
> 「**total power has cohesive or integrative effects on the relationship, and these effects are distinguishable from the effects of relative power or power differences.**」
> 「The geometric-mean specification leads to the following proposition: **Proposition 1: If total power in a relationship increases and the power difference decreases, then greater commitment will develop.**」

而这有独立经验支持，而且这个经验结果**正是对 R2 的否证**：

`Overall & Hammond (2026, Annual Review of Psychology 77, 393–421)`：

> 「**This interdependence means that actors' and partners' perceived power tend to be positively correlated rather than inversely related as would occur if power was always zero-sum** (Columbus et al. 2021; Farrell et al. 2015; Hanna-Walker et al. 2024; Körner & Schütz 2024; Körner et al. 2022, 2025; Langner & Keltner 2008; Overall et al. 2023). These positive associations are modest, however, because relationships can involve both actors and partners having high power (mutual control and influence over important outcomes), both having low power …, or each having different levels of power.」

并且（同一篇）：

> 「…**few interactions involve one person having very high power and the other very low power** (Columbus et al. 2021).」

即：真实亲密关系中，**双方都无权**与**双方都有权**是常见情形，而 `f(dependence asymmetry)` 对这两种情形给出的 readout 相同（都是 imbalance ≈ 0）。R2 的写法会把这两种**行为上不同的关系**判成同一个状态。

**判定：`total power = H(Dependence(A->B), Dependence(B->A))` 的对称聚合（Lawler 用几何平均）可派生，但 R2 的表述把它排除在外。**

#### 4.6.3 惩罚性权力：不可由 dependence 派生

`Lawler & Bacharach (1987, Social Forces 66, 446–462)` 的实验设计直接分离 dependence 与 punitive capability：

> 「The results support the theory of bilateral deterrence **with regard to punitive power, offer partial support to extension of the theory to power dependence**, and demonstrate that **the distinction between punitive and dependence forms of power is important**.」

`Lawler (1993)` 说明了为什么 Emerson 的框架做不到这一点：

> 「Emerson (1972) began with the fairly standard notion of power is the ability of an actor to levy costs on another, yet power dependence theory actually encompassed **only one form of cost — opportunity costs**. **Retaliation or punishment costs were not easily incorporated**, and this assumption made it difficult to directly connect power dependence theory to the use of hostile tactics, such as threats and punishments.」

**判定：`NOT DERIVABLE from dependence.`** 这是本文件中第一个有实验证据支持的独立构念族候选。

同时，`Lawler & Bacharach` 的 relative/total 区分对 punitive power 同样适用——**两个方向都有 punitive capacity 的 dyad 与只有一个方向的 dyad 行为不同**（bilateral deterrence：双方 punitive capability 都高时，punitive tactics 使用率**下降**，因为报复成本上升）。

#### 4.6.4 体验性权力：结构上不可派生

这是任务点名的「不可约的关系-体验成分」。五组证据：

**(a) 定义层面的批评。** `Guinote (2017, Annu Rev Psychol 68, 677–698)`：

> 「**Conceptions of power based on influence rely on observed or inferred potential behavior. However, this conflates structural aspects of tangible control with the targets' psychological reactions and desire to comply** (Fiske & Dépret, 1996).」

**(b) power 是一种体验。** `Keltner, Gruenfeld & Anderson (2003, Psychological Review 110, 265–284)`：

> 「Second, **the experience of power involves the awareness that one can act at will without interference or serious social consequences** (Weber, 1947).」
> 「…**recognizing that an individual's power should be characterized not in absolute terms but as falling on a continuum relative to the power of others.**」

**(c) 结构性不平等不决定顺从。** `Lawler (1993)`：

> 「Bilateral deterrence clarifies the role of unequal power by suggesting **why lower power parties with substantial power capability may resist efforts at intimidation and use power as much as the higher power actor**. **An effort is needed to understand further the conditions under which unequal power relationships produce such resistance rather than compliance by the lower power party.**」

（→ 原文明确说这是一个**尚未解决**的问题。不得把它当成已知结论。）

**(d) 实际影响力与感知影响力之间有系统性、动机驱动的偏差。** 感知权力偏差研究（*PSPB*, DOI `10.1177/01461672251409849`；4 个样本，N = 1,304 dyads，覆盖 friendship / same-gender couples / woman–man couples）用 Truth-and-Bias 模型对照「自己感知的权力」与「伙伴报告的实际影响」：

> 「We found **robust evidence that people underestimated their power**. Moreover, higher self-protection motives (e.g., attachment anxiety) and specific power motives (e.g., desire for power) predicted greater underestimation bias whereas higher pro-relationship motives (commitment) predicted lower underestimation bias.」

并且：

> 「Despite extensive evidence for the important implications of low perceived power, little is known about people's perceptions of power accurately reflect how much they can influence their relationship partners. Indeed, the behavioral inhibition, aggression, and poor well-being that arises from low power may arise because people **actually lack influence** in their relationship **and/or because they inaccurately perceive they lack influence**.」

**(e) 顺从的行为后果。** `Birnbaum, Kanat-Maymon, Zholtack, Avidan & Reis (2024, PMC11782303)`：

> 「power imbalances may generate dynamics in which high-power partners are less responsive to their partners' needs, while **low-power partners tend to comply** with partners, **inhibiting their own needs** (Knudson-Martin, 2013; Mahoney & Knudson-Martin, 2009).」

配合 `Solomon & Samp (1998, JSPR 15, 191–209)` 的 chilling effect：因预期负面后果而不表达不满。

**判定：`NOT DERIVABLE from structure.` 但这是一个**理论驱动的架构主张，证据是间接的**（见 §10 U4）。**

#### 4.6.5 权力必须 domain-indexed，而 domain 分区是 shared pair fact

`Simpson, Farrell & Rothman (2019)`（DPSIM 扩展章）：

> 「Within-dyad variables can also include **relationship-specific rules or norms that partners develop and follow, such as which partner is responsible for making decisions in a given domain** (e.g., paying the bills, deciding where to go on vacation).」

> 「Relationship power is typically conceptualized as a general, global feature of the relationship in which one partner is thought to have more or less power than the other. **However, power can also be situated within a given domain** (e.g., finances, parenting)… Johnny may have more power in the relationship overall, but **Tara may get her way in "her" decision [domain]**.」

> 「Individuals who get their way on a specific issue **may begin to perceive they have relatively more power in that domain than their partner does**, which could lead individuals to take charge of future decisions in that domain.」

最后一句是关键：**power 的变化先发生在 perception 里，再发生在行为里。** 这把它归入 `B_i`。

`Junkins, Derringer, Ogolsky, Hardesty & Weisberg (2025/2026, JFTR 18, 170–191)` 的系统评述确认测量现实：

> 「General relationship power (κ = 76) and the next category, power balance, were attempts to measure the **unspoken and subjective question, "who has more power,"** that is not easily addressed by tangible items.」
> 「There were **no established scales used repeatedly that were developed specifically with power bases in mind**.」
> 「…the measures were focused on White, younger, and heterosexual men and women in shorter-length relationships.」

#### 4.6.6 结论：一个权力 readout 不够

`PARAMETER_CONVERGENCE` R2 判「power = f(dependence, alternatives, resources, constraints)，不先设独立 power 值」。本文件判：

```text
R2 完整表述  -> NEGATIVE（作为对 power 的完整说明是错的）
R2 作为 relative power 分量的 readout -> 正确

R2 遗漏至少五件东西：
  (1) punitive / retaliatory capacity                       [不可由 dependence 派生]
  (2) power bases 中的非互赖基底
      legitimate / expert / referent / informational        [French & Raven 1959；DPSIM 承认六种]
  (3) 体验性 / 感知维度                                    [不可由结构派生]
  (4) 共同（非零和）分量                                     [需要对称聚合，不能只看不平衡]
  (5) domain 索引                                            [domain 分区 = shared pair fact]
```

**架构发现（需 Architect 判决）：** 权力至少需要四个表示，而不是一个 readout：

```text
P1_structural  = 结构侧：从 alternatives / value / constraints / Omega(S) 读出
P2_capacity    = 能力侧：PunitiveCapacity_(i->j)，独立 construct family，不可由 P1 派生
P3_perceived   = 知觉侧：PerceivedPower_i(j, domain) = B_i(...)   [Belief layer, directed by perceiver]
P4_felt        = 体验侧：FeltCompliance_i(j, domain)，directed experiential state
                 （并允许 P3 与真实影响力之间存在带符号、带动机的 gap）
```

`PowerImbalance_(A,B)` 仍然是有效的 **derived readout**，但它只是 `P3/P4` 的一个投影，且**不完整**。

**注意命名冲突风险：** `Lawler (1993)` 用 "relational cohesion" 指 **total power / 互依程度**；`PARAMETER_CONVERGENCE` P1 用 "Cohesion / We-ness" 指**共同体感**。两者同名不同义。readback 时必须避免混用。

### 4.7 互惠（reciprocity）

「互惠」在文献里至少指三件不同的事。混在一个词里是本 lane 遇到的主要概念隐藏。

**(a) 时序成分。** 互惠在定义上是**对先前行为的反应**。`Gerpott et al.` 明确指出，互惠 affordance 之所以在 IT 六个维度中**没有直接概念对应**，正是因为它需要顺序/重复互动：

> 「the reciprocity affordance is arguably the only affordance that has **no direct conceptual link to any dimension of interdependence** as specified in Interdependence Theory.」

**推论：`Reciprocity` 不能由 t 时刻的两个心理状态派生；它必须是历史（Action/Event log）的函数。**

```text
Derived:  reciprocity_(i->j) = f( History_{t-1..t-n}( Action_j, Return_i ) )
```

**判定：这是行为/历史层的规律，不应作为新的关系状态 primitive。** 但它有一个**规范面**，那个是 directed 状态：

```text
ExpectationOfReciprocity_(i->j, t)   [i 期待 j 会回报的历史比率 / i 感知到的 j 的互惠意愿]
```

这两个是 directed、可从历史 + belief 派生、可表示为 Unknown。

**(b) 类型成分（互惠不是刻度）。** `Kollock (1994, AJS 100, 313–345)` 证明交换结构是不确定性与承诺的**类型**结果，不是好感程度的连续结果；`Molm (1994)` 证明依赖与风险改变交换**结构**本身。（Kollock 的四分类标签——reciprocity / lump-sum exchange / unilateral commitment-to-perform / equilateral commitment——本次未在原始出处核实，故只使用其较弱的「存在不同交换结构且机制不同」这一论断。）

`Gneezy & Fessler (2012, Proc R Soc B 279, 219–223)` 提供了强证据，说明「回报」与「惩罚」是**可分离**的两个互惠分支，且**可以同时被提升**：

> 「during wartime, people are more willing to pay costs to **punish non-cooperative** group members and **reward cooperative** group members. **Rather than simply increasing within-group solidarity**, violent intergroup conflict thus elicits behaviours that … enhance cooperation within the group.」

**这直接否证「互惠 = 一个刻度」的表示。** 一对伴侣可以 reward-reciprocity 高而 punishment-reciprocity 为零，反之亦然。

**推论：** 交换结构类型应当是**类别值的 shared pair fact**，不是潜在标量：

```text
ExchangeStructureType_(i,j, domain) ∈ { negotiated_agreement,
                                       lump_sum_exchange,
                                       unilateral_commitment,
                                       reciprocity,
                                       mixed / Unknown }
```

**这不违反 representation invariant #4——类别值是合法坐标。** 它甚至是一个具体的架构示范。

**(c) 规范强度。** 互惠规范本身是 Agent 的 general tendency（`Gerpott et al.` 把它归给 forgivingness / positive reciprocity 等 trait），**不是 pair 状态**。LHRM 已有 `generalized trust` 之类的 Agent 层入口。

**判定：`MutualReciprocity` 作为标量 primitive -> REJECT；拆为 (i) 历史规律 (ii) 两个 directed 期待状态 (iii) 一个类别值 shared pair fact。**

### 4.8 共同应对方（dyadic coping）—— 最强的「真涌现」证据

这是本文献中**唯一**一个把「两个有向状态的函数」与「联合过程」直接对撞、并且**联合过程赢了**的实验。

`Bodenmann, Meuwly & Kayser (2011, European Psychologist 16, 255–266; N = 443 瑞士伴侣)`：

> 「Two main models of dyadic coping are proposed in the current literature: (1) a **comparative approach** in which each partner's individual coping is compared with the other’s individual coping with regard to congruence or discrepancy and (2) a **systemic model** where dyadic coping is conceptualized as an **interactive and reciprocal process**… **However the systemic dyadic coping measure is a stronger predictor than the discrepancy measure for relationship quality.**」

这一条的分量在于：**discrepancy / congruence 正是「两个有向状态的一个函数」的教科书形式。它在与联合过程竞争同一 outcome 时落败。**

量级：`Falconier, Jackson, Hilpert & Bodenmann (2015, Clinical Psychology Review 42, 28–46)`：72 个独立样本 / 57 篇报告 / **17,856 人**；

> 「the aggregated standardized zero-order correlation (r) for total dyadic coping with relationship satisfaction was **.45** (p < .000)」
> 「**Perceptions of overall dyadic coping by partner and by both partners together were stronger predictors** of relationship satisfaction than perceptions of overall dyadic coping by self.」
> 「comparisons among dyadic coping dimensions indicated that **collaborative common coping**, supportive coping, and hostile/ambivalent coping were stronger predictors than stress communication, delegated coping, protective buffering coping, and overprotection coping.」

而且 effect 在性别、年龄、关系长度、教育、国别上**都不被调节**（罕见的稳健性），但**被国别显著调节**（`Hilpert et al. (2016), N = 7,973, 35 nations`；香港的 coping 行为对满意度的效应强，加纳/肯尼亚弱）。

`Lehne & Bodenmann (2019, Frontiers in Psychology 10, 571)`（评述 139 项研究）提供两条更尖锐的证据：

> 「**perceived similarity in DC between partners matters more for relationship satisfaction than the actual similarity** (Iafrate et al., 2012).」

> 「After 5 years, couples could be correctly classified in **73%** of the cases regarding whether they would separate or stay together according to their level of DC (Bodenmann & Cina, 2005).」

**结构性论证（比统计论证更强）：** common dyadic coping 的样本题项是

```text
"我们互相帮助，把问题放到新的角度看"（Bodenmann DCI common 维度）
"当我压力大时，我的伴侣倾听我、让我说出真正困扰我的事"（supportive）
```

这些是**联合行动**属性。它们既不是 i 的心理状态，也不是 j 的心理状态，而是**耦合系统的属性**。「我们一起做」这件事，只有把两个 Agent 同时作为系统来看才存在。

**判定：`CommonDyadicCoping_(A,B)` 是真正的 pair-level 涌现候选。**

**但有一个必须标注的本体论不确定性（见 §10 U6）：** `Bodenmann et al. (2011)` 证明的是「**只靠两条有向状态的函数不够**」，它没有证明「**必须**有一个独立的 pair state 变量」。在 LHRM 的框架里，联合过程也可能是 `Action/Event` 层的一种**结构化轨迹**（例如 dyad 层面的循环：stress → communicate → respond → joint coping → outcome），而不必是一个状态坐标。这是一个 `R06` / `R09` 的裁决点。

### 4.9 亲密（intimacy）的相互性

`Laurenceau, Barrett & Pietromonaco (1998, JPSP 74, 1238–1251)` 用事件日记法（1–2 周，每次互动后立即报告）检验了 Reis & Shaver (1988) 的 interpersonal process model：

> 「**the findings strongly supported the conceptualization of intimacy as a combination of self-disclosure and partner disclosure at the level of individual interactions with partner responsiveness as a partial mediator in this process.**」
> 「**Reis and Shaver regard the speaker's interpretation of the listener's communication as more important for the development of intimacy than a speaker's disclosure or the listener's actual response.** Although a partner may make a genuine attempt to be responsive to a disclosure, **the speaker may not perceive the partner's behavior as responsive.**」

**这给出两个对 LHRM 直接相关的事实：**

1. **「相互的亲密」不是两个 Intimacy 状态的任何对称聚合。** 因为该模型的不对称恰恰在**方向内部**：`D_int(i about j, 情境 t)` 依赖 j 在 t 的响应被 i **如何知觉**。`min(D_int_i, D_int_j)` 允许 A 感到被回应、B 感到没被回应——这是**最常见的真实情形之一**，而它恰好不是「相互亲密」。

2. **这个不匹配的方向性是关键的。** 「被回应」这个体验具有**不对称结构**：j 的回应由 j 的动机/需求/目标决定（S9 引用了 Reis & Patrick 1996 的这一段）。因此「是否相互」是关于这个方向的一个**条件陈述**：

```text
MutualIntimacy_(A,B,t)
  ≈  Conjunction( D_int(A about B) >= threshold,
                  D_int(B about A) >= threshold,
                  ActionHistory_j responded to A 的表露 )
```

这仍然是一个**关于两个有向状态的函数**——只是它需要第三条输入（互动历史），因为单向的 `D_int` 不足以确定条件是否满足。

**判定：`DERIVABLE`，但输入必须包含 `ActionHistory`（或从 belief 层读取），不能只有两个状态。** 这一条是对「pair 现象需要三个输入而非两个」的干净例证。

### 4.10 依赖的体验性调节（attachment → power 的有向耦合）

`Overall & Cross (2019, Power in Close Relationships, pp. 28–54; DOI 10.1017/9781108131490.003)`，经该书导言转述：

> 「those individuals with attachment-based **avoidant** tendencies are associated with **minimizing one's dependence** on a partner, but also with **attempts to sustain control and power** in a relationship. In contrast, those individuals with **anxiety** tendencies **seek to maximize their dependence** on a partner, with a corresponding **loss of power** within the relationship.」

**这条的重要性：它把 LHRM 的两个已有 primitive（`D5 AttachmentSecurity` 与 dependence）连成一条有向的负向耦合边。** `CONSTRUCT_SCOPE_DIRECTIONALITY.md` §4 明确允许状态之间有强动态耦合（`partial F_i / partial z_j != 0`），所以这**不违反**现有架构，但它是一条**具体的、有经验支持的**耦合路径，当前 `PARAMETER_CONVERGENCE` 没有写。

**判定：不是 pair 现象（它是 i 的两个构造之间的有向耦合）。本文件记录它是因为它给 §4.6.4 的 `P4_felt` 提供了一条独立的因果入口。**

---

## 5. Test table

列含义：
- **可派生？** — `Y` = 形式论证成立且已有文献支持；`N` = 已证不可派生；`?` = 未定。
- **派生形式 / 需要的额外 `Φ`** — 见 §4。
- **增量证据** — `有` = 文献中有直接检验；`无` = 本 lane 未找到直接检验（**不等于不存在**）；`间接`。
- **可 falsify 的检验** — 具体到可执行。

| # | 现象 | 可派生? | 派生形式 / 需要的额外 `Φ` | 增量证据 | 可 falsify 的检验 | 关键引用 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 互惠性吸引/互惠欲望 | **Y** | `H(e_att(A→B), e_att(B→A))`，`e = D − R − T`；无额外 `Φ` | 有（bias > accuracy, N=238） | 控制 `R,T` 后 `H(e)` 是否显著优于 `H(D)` | Kenny 1988; Kenny & Acitelli 2001 |
| 2 | 广义互惠 | Y（nuisance） | `corr(R_k(i), T_k(j))`，跨 dyad；不属于 ontology | 有 | N/A | Kenny 1988 |
| 3 | 不对称 | **Y**（表示须改） | 带**显式声明比较器**的比较关系，非 `distance`；坐标系可比较性为独立假设 | 无直接检验 | 声明过的序数比较器 vs 连续 distance 在具体任务上是否有差异 | `CONSTRUCT_SCOPE` §2; `AGENTS` invariant #4 |
| 4 | 依赖不平衡 | Y（但 D8 应降级） | `Dependence_(i,j,S)` 为 `Omega(S)` 的 readout；需 `Alternatives_(i,ref=(j))` + `Constraint_(i,j)` | 有（IT 六维为情境维度） | 给定 alternatives/constraints/value 后 `OutcomeDependence` 是否有增量 | van Lange & Rusbult 2011; Rusbult 1983 |
| 5 | 情境客观互赖结构 `Omega(S)`（actor/partner/joint control；六维） | **N（本体缺口）** | 不是有向状态的函数；需 interdependence matrix 表示 | 有（IT 全套） | 两个有向状态相同但 actor/partner control 相反的 dyad，是否被 LHRM 判为同一状态 | Kelley & Thibaut 1978; Kelley et al. 2003; van Lange & Rusbult 2011 |
| 6 | 情境互赖的**主观**知觉 | Y（6→5 有损） | `B_i(Omega(S))`，但需接受 coordination 不可分 | 有（242 条目，5/6 因子） | 亲密关系长期面板中 power 维度是否仍可区分 | Gerpott et al. 2018 |
| 7 | relative power（零和） | **Y** | `f(Dependence(i→j) − Dependence(j→i))` | 有 | 已知 dependence 不对称时，relative power 是否有增量 | Lawler & Bacharach 1987; Lawler 1993 |
| 8 | total power（非零和） | **Y** | 对称聚合（如 geometric mean），Lawler Prop.1；**R2 的写法遗漏此项** | 有（双方感知权力正相关） | 双方都无权 vs 双方都有权的 dyad，是否被判为同一状态 | Lawler 1993; Overall & Hammond 2026 |
| 9 | punitive / retaliatory power | **N** | 不可由 dependence 派生 | 有（实验分离；partial support 仅对 punitive） | 控制 dependence 后，punitive capacity 是否仍预测 tactics | Lawler & Bacharach 1987; Lawler 1993 |
| 10 | power bases 中非互赖基底（legitimate / expert / referent / informational） | **N（gap）** | 与 dependence 正交；需 `Legitimacy_(i,j,domain)` | 有（orthogonal manipulation, N=320） | 控制 dependence 后 legitimacy 是否预测 coalition/appeal | French & Raven 1959; DPSIM 2019; Johnson & Ford 1996 |
| 11 | 感知权力 `PerceivedPower_i` | **N（不可由结构派生）** | `B_i(...)`；需 truth 侧与 belief 侧并置，允许带符号 gap | 有（N=1,304 dyads，Truth-and-Bias，系统性低估） | 控制真实影响力后，感知是否仍携带独立信息与动机相关偏差 | PSPB DOI `10.1177/01461672251409849`; Guinote 2017 |
| 12 | 顺从 / 寒效应 `FeltCompliance_i(j,domain)` | **N（证据间接）** | 不可由结构派生；`Lawler 1993` 明说抵抗 vs 顺从的条件**尚未解决** | 间接 | 控制 `PerceivedPower` 后 chilling 是否仍有增量 | Solomon & Samp 1998; Lawler 1993; Birnbaum et al. 2024; Keltner et al. 2003 |
| 13 | 权力–依恋负向耦合 | N/A（有向耦合，非 pair 现象） | `∂(depend)/∂(security_i) < 0` | 间接（章节论断） | APIM cross-lag：`security_i(t−1)` 是否负向预测 `depend_i(t)` | Overall & Cross 2019 |
| 14 | 互惠规范（general tendency） | N/A（Agent 层） | `generalized reciprocity norm` | — | N/A | Gerpott et al. 章节 |
| 15 | 互惠（作为行为规律） | Y（但不是 state） | `f(ActionHistory_{t−1..t−n})`；需历史 | 有（affordance 无 IT 维度对应） | 互惠是否只由历史预测，而不由 t 时刻两状态预测 | Gerpott et al. 章节; Gneezy & Fessler 2012 |
| 16 | 互惠（作为期待） | Y | `ExpectationOfReciprocity_(i→j,t)`，directed，可 Unknown | 间接 | 期待是否独立于过去的行为比率 | — |
| 17 | 交换结构**类型** | Y（作为类别值 `Φ`） | `ExchangeStructureType_(i,j,domain) ∈ {…}`；**需 `Φ`，非有向状态** | 有（reward vs punishment 互惠可分离） | 高 reward / 零 punishment 的 dyad 是否被单一互惠刻度压平 | Kollock 1994; Molm 1994; Gneezy & Fessler 2012 |
| 18 | Common dyadic coping | **N** | 联合行动属性；discrepancy（=两有向状态的函数）在同 outcome 竞争中落败 | **有（直接判别实验 + meta, N=17,856, r=.45）** | 复现 Bodenmann et al. 2011 的双模型竞争 | Bodenmann, Meuwly & Kayser 2011; Falconier et al. 2015; Lehne & Bodenmann 2019; Hilpert et al. 2016 |
| 19 | 支持性互惠支持（supportive DC） | 部分 Y | `Supportive_(j→i)` 已是 directed；perception 已在 Belief | 有 | by-self vs by-partner 的差异（by-partner 预测更强） | Falconier et al. 2015 |
| 20 | 相互亲密 | Y（需第三条输入） | `Conjunction(D_int(A about B), D_int(B about A), ActionHistory_j responded)` | 有（事件日记法） | 单向 `D_int` 高的 dyad 是否被误判为 mutual | Laurenceau et al. 1998; Reis & Shaver 1988 |
| 21 | we-ness / cohesion（整体） | **N（作为标量）→ 拆分** | Cruwys 四因子：3 个已在 LHRM，1 个新 | 有（N=375，7 量表 → 4 因子，各自独立） | 四因子是否在 LHRM 已有坐标上各自可表示 | Cruwys et al. 2022/2023 |
| 21a | we-ness 的 `partner liking` 分量 | **Y** | 即 `D1 Liking_(i→j)` | 有 | 该因子是否与 `Liking` 完全共线 | Cruwys et al. |
| 21b | `partner similarity` 分量 | Y | Agent 属性比较（与 `P2 ValueCongruence` 同类） | 有 | 同上 | Cruwys et al. |
| 21c | `relationship orientation` 分量 | Y | Agent 层 relational interdependent self-construal，domain 索引 | 有 | 同上 | Cruwys et al. |
| 21d | `couple identity` 分量 | **?（弱候选）** | 需要 `CoupleIdentity_(A,B,t)`（pair 共享内容）+ 两个 directed belief | 有（N=375 中预测力最强） | 见 #22 | Cruwys et al. |
| 22 | couple identity clarity | **N（不是一致性的函数）** | `Belief_i(CoupleIdentity)`；需 pair 对象 + 两个 belief | **有（直接：超越 agreement 预测 commitment + 9 月解体）** | 在控制「双方对身份的实际一致」后 clarity 是否仍有增量 | Emery et al. 2021 |
| 23 | value congruence / goal alignment | Y | Agent 属性或状态的比较（同 #21b） | 间接（Acitelli 等的 general vs specific 理解分离） | general 与 specific understanding 分离后哪部分预测满意度 | Acitelli, Kenny & Weiner 2001 |
| 24 | satisfaction / commitment | 部分 N | `commitment = satisfaction + investment − alternatives`；alternatives 需带 pair 参照 | 有（Rusbult 纵向） | 控制 alternatives 后 commitment 是否仍有增量 | Rusbult 1983 |
| 25 | accommodation 过程 | **N** | 二元抑制反应，结果分 recovering / condemning 两条路径 | 弱（未读原文） | 恢复 vs 谴责不能由瞬时状态和表示 | Rusbult et al. 1991 |
| 26 | transactive memory 分工 | **N** | 共享外部存储中「谁存了什么」，不是任一成员状态的函数 | 弱（框架引用） | 若双方都完整记得全部内容，transactive 结构是否仍不同 | Moreland & Argote 1996; *Close Relationships* 2004 ch. |

---

## 6. 重点分析：we-ness / cohesion 案例的双向论证

这是任务指定的 key test case。它值得单列，因为**两种立场都有真实证据**。

### 6.1 立场 A：共享身份是涌现的，可以由已有构件组合出来

**A1. 文献里的 we-ness 本身是个大杂烩。** `Cruwys, South, Kim, Halford, Murray & Fladerer (2022/2023, Family Process 62, 795–817; N = 375)` 把文献中最常用的 7 个 we-ness 量表做 EFA，得到 4 个因子：

```text
F1  couple identity         （54% 的 item 负荷；把 couple 感知为集体/团队）
F2  partner liking          （interpersonal attraction 的一部分）
F3  relationship orientation （relational interdependent self-construal 的一部分）
F4  partner similarity      （3 个 item，来自两个量表）
```

关键在两个细节：

> 「the diverse ways in which we-ness have been measured in the literature are, indeed, capturing **several distinct concepts**. However, **these concepts did not map directly onto the seven distinct scales from which these measures were drawn.**」

> 「**each of the four factors was independently associated** with relationship quality… Couple identity and then partner liking were the strongest predictors in each regression model, while relationship orientation and partner similarity were much weaker predictors.」

**A1 的后果非常具体：** F2/F3/F4 在 LHRM 里**已经有位置**（分别是 `D1 Liking`、Agent 层 self-construal、Agent 属性比较，与 `P2 ValueCongruence` 同类）。也就是说，把 `Cohesion_(A,B)` 设成一个独立标量，会把三个**已经存在**的坐标再打包一次，直接违反 `AGENTS.md`「Prefer few stable constructs + composition over a growing checklist」和 `PARAMETER_CONVERGENCE` §15 Gate C 的 redundancy challenge。

**A2. 「我们」的度量本身就是两个 perception。** we-ness 的测量工具（IOS，Aron et al. 1992；URCS）都是**个体报告的图示或量表**，测的是「我怎么看我们」，不是「我们是什么」。`Cruwys et al.` 也把 IOS 与 in-group 重叠变体分别施测（r = .70，但非同一构念）。`PARAMETER_CONVERGENCE` P1 现有的
`PerceivedWeNess_(A about pair)` / `PerceivedWeNess_(B about pair)` 因此是**正确**的形式。

**A3. 「we」被明确描述为「第三方元素」。** 若 `we` 只是两个状态的函数，它就不是「we」。多个作者把它写成**第三个对象**：

> 「the creation of a couple considers its two members, **plus a third element, the concept of the couple itself**, which will define them exclusively because of their union (Rashidi et al., 2022; 转引自 EIPAR 量表开发论文)」

> 「As a relationship develops, partners are likely to identify new couple-based goals … leading them to **merge** many of their personal goals with those held by their partner (Aron et al., 1992)」（DPSIM 2019）

**立场 A 的最强版本：** we-ness 不需要独立 pair state，只需要 (i) 两条 directed perception，(ii) 三条已在的坐标（Liking / orientation / similarity），(iii) 也许一小块 pair 内容。

### 6.2 立场 B：共享身份不是涌现的，它有独立方差，只是反过来影响有向状态

**B1. 最尖锐的一条证据：clarity 超越 agreement。** `Emery, Gardner, Carswell & Finkel (2020/2021, PSPB 47, 146–160)` 引入 **couple identity clarity**（「作为伴侣二人中的一员，我相信我们知道自己作为一对是谁」），四项研究（横断 1–2、实验 3、纵向 4）：

> 「Moreover, **higher couple identity clarity, although related to actual agreement between partners on their identity as a couple, predicted commitment above and beyond agreement** (Study 2) — as well as **predicted reduced likelihood of relationship dissolution over a 9-month period** (Study 4).」

**这个设计排除了一个最明显的替代解释。** 如果「we」只是两个 directed 状态的函数，那么当双方都正确地反映了那个函数时，「双方一致」应当平凡地预测「双方都清楚」。事实是：**clarity 有超出 agreement 的独立预测力**。而且是纵向、9 个月、对真实结果（解体）。

**B2. 一个共享表征对象需要「外部」内容，这是自指的。** 共享心智模型 / transactive memory 的整个框架建立在「共享的外部存储里，谁存了什么」上（`Moreland & Argote, 1996`；`Close Relationships, 2004, pp. 339–353`）。这个分工不是任一成员状态的函数——它是**一个存储加两个指针**的结构。完全被双方各自记得的内容，transactive 结构就退化了。类似地，couple identity 的内容里有「我们为什么要在一起」这类**共享的叙事**，它不是任何一个人的心理状态。

**B3. 反馈方向：pair-level → directed，不是 directed → pair。** `Simpson, Farrell & Rothman (2019)` 的 DPSIM 反馈环写得非常具体：

> 「As a relationship develops and grows, partners are likely to identify new couple-based goals (e.g., buying a house, starting a family), **leading them to merge many of their personal goals with those held by their partner** (Aron et al., 1992). **Over time, this transformation should render the more powerful partner in the relationship somewhat less powerful** because what is good for Johnny is now also good for Tara as **he becomes more dependent on her.**」

**这是 pair-level 内容直接改写有向状态（dependence → power）的因果路径。** 一个纯 readout 在因果上是单向的（directed → readout），不可能产生这种箭头。

**B4. 独立测量的四因子各自有贡献这一点也支持 B。** `Cruwys et al.` 强调 `couple identity` 与 `partner liking` 各自独立预测关系质量，**且不能互相替代**。如果 we-ness 只是已有坐标的派生聚合，四个因子的独立贡献是自动的、无信息的；关键在于 `couple identity` **不能**由 `partner liking` 预测。

### 6.3 判决

**两者都对，但它们不冲突——因为它们回答的是不同的问题。**

- 「we-ness 这个**名字**所覆盖的东西是否需要一个新的标量 pair state？」→ **不需要。** 立场 A 完全成立，而且有 N=375 的直接因子证据。把 `Cohesion_(A,B)` 当标量 primitive 应被否决。
- 「是否存在一个**不能**由两条有向状态 + shared facts 解释的 pair-level 内容？」→ **是。** 立场 B 有 `Emery et al. (2021)` 的直接证据（clarity 超越 agreement，纵向预测解体）。

因此本文件的判决：

```text
REJECT   Cohesion_(A,B) as a scalar primitive
REJECT   "we-ness" as a construct name in the ontology
KEEP     PairRepresentation_(A,B,t)  -- 一个小的、显式的 pair 内容族，而非单一刻度
           members (first cut, all CANDIDATE):
             R1  couple identity / shared narrative ("who we are, why")
             R2  shared future / couple project (DPSIM 的 couple-based goals)
             R3  division of labor / relational norms ("who decides what")  [= §4.6.5 的 domain 分区]
             R4  shared external memory (transactive 分工)
KEEP     Belief_i( R1 ) / Belief_i( R2 )  -- 两个 directed belief states
KEEP     coupling  R1/R2 -> D_k(i->j)  -- 有向因果入边（B3）
```

`R3` 值得单独指出：它**同时**是 we-ness 的内容、也是 power 的 domain 分区（§4.6.5）。这提示 pair 内容层与权力层共享一个对象——这是一条本 lane 之前没有看到的架构线索，建议 Architect 考虑。

**这个判决的 falsifier：** 若 couple identity clarity 在**加入 joint Action/Event 历史**（公开承诺、共同决定、共同叙述行为）后不再有增量，则 `PairRepresentation_R1` 也是派生的，整个 `KEEP` 应降级为 `DERIVED from Action/Event history`。本 lane **未找到**做这个检验的研究（见 §10 U2）。

---

## 7. 权力与依赖：readout 还是不可约成分？

任务问：power 能否是 asymmetry + alternatives + constraints 的 readout，还是 power 有不可约的关系-体验成分（例：「不得不顺从」的主观感）。

**判决：两者都有，但它们落在不同层，R2 把它们混成了一个。**

```text
可以 readout 的部分：
  relative power  = Dependence 不对称
  total power     = Dependence 的对称聚合（Lawler Prop.1）
  这两个都从 Omega(S) + alternatives + value + constraints 读出

不可 readout 的部分（各有独立证据）：
  (1) PunitiveCapacity_(i->j)   -- 实验证明与 dependence 分离
  (2) Legitimacy / power bases  -- 正交操纵证明与 dependence 分离
  (3) PerceivedPower_i          -- 系统性、动机驱动的偏差
  (4) FeltCompliance_i(j, d)    -- 结构不平等不决定顺从 vs 抵抗
  (5) 共同（非零和）分量         -- 双方感知权力正相关
  (6) domain 索引                -- 规范/分工是 shared pair fact
```

所以对 Architect 的具体问题——「`PARAMETER_CONVERGENCE` R2 应当被改写还是被否决？」——的回答是：

> **R2 应当被改写，不是被否决。** 把它限定为「**relative power 分量的 derived readout**」，同时在 schema 中显式加入 punitive capacity、legitimacy/bases、perceived power、felt compliance 四个槽位，以及一个 domain 索引。`PowerImbalance_(A,B)` 保留为 derived readout。

**并且要明确记录：`felt compliance` 是本 lane 唯一主张的「不可约关系-体验成分」，但它的证据是间接的**（`Lawler 1993` 明说条件未知；没有任何研究在控制 perceived power 后检验 felt compliance 的增量）。这是 §10 U4，不应被当作已确立的架构发现。

---

## 8. 文献中存在的、当前有向状态框架**根本无法表示**的现象（gap list）

按「缺口类型」排序。类型：`ontology hole` = 世界/情境表示缺失；`construct hole` = 缺构念；`projection hole` = 本体有但局部投影取不到。

| # | 现象 | 缺口类型 | 为什么当前框架表示不了 | 最小补丁方向 | 关键引用 |
| --- | --- | --- | --- | --- | --- |
| G1 | **情境的客观互赖结构** `Omega(S)`：actor control / partner control / joint control；六维结构 | **ontology hole** | LHRM 只把世界投影到两个具体人，没有「情境的 outcome-contingency 结构」这一实体。两个有向状态相同、情境结构相反的 dyad 会被判为同一状态 | 在 `RelevantEnvironment` / `PairState` 之上增加一个 `SituationStructure` 对象；可借用 IT 的 matrix 表示为转移表 | Kelley & Thibaut 1978; van Lange & Rusbult 2011 |
| G2 | **惩罚性/报复性能力** | construct hole | 不是 dependence 的函数（实验分离） | 独立 construct family，directed | Lawler & Bacharach 1987; Lawler 1993 |
| G3 | **权力基底**：legitimate / expert / referent / informational | construct hole | 这四种与互赖无直接关系；DPSIM 承认它们是核心基底，但**没有反复使用的成熟量表** | 至少 legitimate / expert 基底需要表示；可用 Agent 属性 + domain 参照 | French & Raven 1959; DPSIM 2019; Junkins et al. 2025 |
| G4 | **合法性与申诉策略** | construct hole | dependence 结构不决定策略选择 | `Legitimacy_(i,j,domain)` | Johnson & Ford 1996 |
| G5 | **实际影响力与感知影响力的带符号差距** | 混合 | 需要 truth 侧与 belief 侧同时存在并可比较 | 在 dyadic representation 中为同一定义保留 `actual` 与 `perceived` 两个坐标 | PSPB DOI `10.1177/01461672251409849`; Guinote 2017 |
| G6 | **共同（total）权力 / 非零和权力** | construct hole（当前公式遗漏） | R2 只看不平衡，把「双方都无权」和「双方都有权」压平 | 显式的对称聚合 readout | Overall & Hammond 2026; Lawler 1993 |
| G7 | **交换结构类型** | `Φ` 的类别值缺失 | 「单方面承诺」与「对等承诺」在行为上不同，不能用一个刻度 | 类别值 `ExchangeStructureType_(i,j,domain)` | Kollock 1994; Gneezy & Fessler 2012 |
| G8 | **联合/耦合过程**（common dyadic coping 等） | construct hole | 联合行动属性不是任一人的状态；comparison 版本在同 outcome 竞争落败 | `PairState` 下新增一个 **joint process** 分支（结构化轨迹或状态均可，见 U6） | Bodenmann et al. 2011; Falconier et al. 2015 |
| G9 | **couple-level 目标 / 共同项目** | construct hole | 一对伴侣有「一起要买房子」这样的目标集，它不是任一人的个人目标 | `PairRepresentation_R2`（§6.3）；并给 directed 入边 | DPSIM 2019 |
| G10 | **分工与领域规范**（「谁管钱、谁管育儿」） | `Φ` 缺失 | 它同时是权力 domain 分区、也是 we-ness 内容、也是约束来源 | `Φ` 中显式加入 domain 分区 | DPSIM 2019; `RELATIONSHIP_EVALUATION_FOUNDATION` §1.4 |
| G11 | **第三方极**：孩子作为共同项目、情敌、in-law、竞争者 | ontology hole（`PairState` 定义过窄） | `PairState_(A,B)` 的定义只容纳二人；实际 dyad 几乎总有第三方极点 | `PairState` 允许显式第三个 referent | Birnbaum et al. 2024（extradyadic） |
| G12 | **第三方视角下的 pair 身份**（被社区看作一对） | `Φ` 缺失 | we-ness 文献明确提到社会见证 | `Φ` 中允许外部观察者维度 | Cruwys et al. 2022/2023 讨论项（Sayre et al. 2006 转引） |
| G13 | **三角/多边现象**（关系内的权力影响婚外动机） | **projection hole** | `X_(S,O,t) = Phi_(S,O)(WorldState(t))` 是二人投影；世界图能表示但投影取不到 | 局部投影需要允许第三个 agent 进入 | Birnbaum et al. 2024 |
| G14 | **依恋 → 依赖/权力的负向耦合** | coupling 边缺失 | `D5 AttachmentSecurity` 与 dependence 之间有一条有证据的有向负边，schema 未写 | 显式写一条 directed coupling 边（不违反 `CONSTRUCT_SCOPE` §4） | Overall & Cross 2019 |
| G15 | **accommodation / 克制过程及其恢复/谴责分叉** | construct hole（过程） | 一次性抑制反应 + 二分后果，不可由瞬时状态和表示 | 作为 `Action/Event` 的结构化轨迹 | Rusbult et al. 1991 |
| G16 | **conflict pattern 类型**（如 demand–withdraw） | construct hole（过程类型） | 这是 dyad 级反馈回路的**类型**，不是两人状态之和 | 回路类型作为 `Φ` 或 pair process 的类别 | —（本 lane 未找到强引用，标 `UNKNOWN_AS_OF`） |

---

## 9. 明确不主张什么

1. **不主张本文件任何派生式、公式、权重、距离、阈值、概率已被科学确立。** 所有形式都是待 falsify 的猜测。
2. **不主张「power 不可由 dependence 派生」适用于全部 power。** 分量区分见 §7。
3. **不主张把 Gneezy & Fessler (2012) 的群际冲突实验结论直接外推到亲密关系。** 只用它支持「互惠的 reward 与 punishment 分支可分离」这一较弱命题。
4. **不主张 PSPB 感知权力偏差研究（DOI `10.1177/01461672251409849`）证明了实际权力与感知权力之间有因果关系。** 只主张存在系统性、动机驱动的偏差。**该文作者名单本次未在稳定公开出处核实（`UNVERIFIED`）。**
5. **不主张 `CoupleIdentity` 一定是独立 pair state。** 只主张存在不能由「双方一致」与「两条有向状态」解释的残余；「joint Action/Event 历史的函数」这一替代解释未被排除。
6. **不主张 SRM 残差化是 ontology 主张。** `D_k` 是 primitive，`e_k` 是 readout。
7. **不主张 6→5 的互赖维度塌缩适用于亲密关系长期情境。** `Gerpott et al. (2018)` 的样本是情境描述任务。
8. **不主张 Lawler 的 "relational cohesion" 等于 LHRM 的 `Cohesion`。** 前者 = total power / 互依程度；后者 = 共同体感。**同名不同义，必须在 readback 时避免。**
9. **不主张本文件对 `Huston, Caughlin, Houts, Smith & George (2001)`（JPSP 80, 237–252; DOI `10.1037/0022-3514.80.2.237`）有任何实证发现的使用。** 该文本次只核实了出版元数据，**未读内容**。它在本文件中仅作为「cohesion 已被多维操作化」的存在性指针。
10. **不主张本文件对 rule 4 的任何修改。** §4.3 关于「asymmetry 应是带声明比较器的比较关系」是对**表示形式**的细化主张，Architect 可独立否决。
11. **不主张文献数量或 LLM 一致度构成验证。** 每个「derivable」都配 falsifier；没有 falsifier 的已进入 gap list。
12. **不主张我读过 LHRM issue #20 / #21 / #22。** 没有读取、执行或引用。
13. **不主张本文件完成了 `OutcomeDependence`（D8）的实测裁决。** 见 §10 U1。
14. **不主张 `PairState` 必须包含 joint process。** `Bodenmann et al. (2011)` 只证明了「两条有向状态的函数不够」，没有证明「必须有独立 pair state」。
15. **不主张本文件评估了 `PARAMETER_CONVERGENCE_V0_1.md` v0.1 的 8 项 directed basis 的完备性。** 本 lane 只测 pair-level 派生问题。

---

## 10. 剩余未知

见 packet `§6 remaining_unknown`（U1–U9）。本文件不重复；只强调最关键的两条：

- **U6（本文件最重要的未决本体问题）** `dyadic coping` 类 joint process 是否必须进入 ontology，还是可作为 `Action/Event` 的结构化轨迹表达。
- **U4** `felt compliance / chilling` 在控制 `PerceivedPower` 后是否携带独立增量。当前无直接检验。

**推荐的执行性检验**（`R05` / `R16` 可直接采用）：见 packet `§5` 的 M1 / M2 / M3 三步规格，以及 `Bodenmann, Meuwly & Kayser (2011)` 作为唯一已存在的直接判别模板。

---

## 11. 建议的状态与下游动作

**建议 lane 状态：`SUCCESS`**

**建议 Architect 处理的候选动作（每条都标为 CANDIDATE，非决定）：**

| # | 动作 | 依据 | 建议优先级 |
| --- | --- | --- | --- |
| A1 | 在 `mutuality / asymmetry` 的派生规范中**加入 SRM 残差化前置步骤**（`e = D − R − T`），并标注 `e` 属 measurement 层 | §4.1；Kenny 1988; Kenny & Acitelli 2001 | 高 |
| A2 | 把 `Asymmetry_k` 的表示从 `distance()` 改为「带声明比较器的比较关系」 | §4.3；`AGENTS` invariant #4 | 中 |
| A3 | 把 D8 `OutcomeDependence` 降级：标为 `Omega(S)` 的 readout，或 `B_i` 层的知觉；不再作为 directed psychological state | §4.4；Rusbult 1983 | 高 |
| A4 | 改写 R2：限定为 relative power 分量的 derived readout；同时显式登记 punitive capacity、legitimacy/bases、perceived power、felt compliance 四个槽位 + domain 索引 | §7；Lawler & Bacharach 1987; Johnson & Ford 1996; Overall & Hammond 2026 | 高 |
| A5 | 在 ontology 中补 `SituationStructure`（`Omega`），与 `Environment` / `PairState` 并列 | §3；Kelley & Thibaut 1978 | 高 |
| A6 | 明确否决 `Cohesion_(A,B)` 标量；把 P1 改名为 `PairRepresentation` 族（couple identity / shared project / division of labor / shared external memory）+ 两个 directed belief + 有向入边 | §6.3；Cruwys et al. 2022/2023; Emery et al. 2021 | 高 |
| A7 | 拆分 `Reciprocity`：拒绝标量；建 `ExchangeStructureType_(i,j,domain)` 类别值 + 两个 directed 期待 | §4.7 | 中 |
| A8 | 在 `PairState` 概念下留出 **joint process** 分支（不急于定义坐标）；把 `CommonDyadicCoping` 作为第一个候选 case | §4.8；Bodenmann et al. 2011 | 中（U6 未决） |
| A9 | 补一条 `AttachmentSecurity_(i→j) → Dependence_(i→j)` 的有向负向耦合边 | §4.10；Overall & Cross 2019 | 中 |
| A10 | 记录命名冲突：`Lawler` 的 "relational cohesion" ≠ LHRM 的 `Cohesion` | §4.6.6 | 低（readback 时处理） |

**建议的 status 判定：**

```text
R10 lane status                       : SUCCESS
其中 R2（power 完整表述）子结论       : NEGATIVE（部分正确）
    CoupleIdentity 独立 pair state    : PARTIAL
    joint process 的本体地位          : UNKNOWN（交 R06/R09）
所有「derivable」判断                 : 形式论证 + 文献支持，未经量化；全部配 falsifier
```

---

## 12. 引用列表

> 分三类：`CITED_PRIMARY`（本次实际读到原文/原始摘要/出版元数据）、`CITED_SECONDARY`（经他人文献转述）、`AGENT_RECALL / UNVERIFIED`（本次未核实）。
> 全部核实日期：**2026-09-27**。
> 编号与 packet `§2` 的 S 编号一致，便于回查。

### 12.1 CITED_PRIMARY

- Agnew, N. R., & Harman, A. M. (Eds.). (2019). *Power in Close Relationships*. Cambridge University Press. 章节导言 excerpt: https://assets.cambridge.org/97811071/92614/excerpt/9781107192614_excerpt.pdf — **S10**
- Aron, A., Aron, E. N., & Smollan, D. (1992). Inclusion of Other in the Self Scale and the structure of interpersonal closeness. *JPSP*, 63(4), 596–612. https://doi.org/10.1037/0022-3514.63.4.596 — **S29**
- Birnbaum, G. E., Kanat-Maymon, Y., Zholtack, K., Avidan, R., & Reis, H. T. (2024). The power to flirt: Power within romantic relationships and extradyadic sexual interest. PMC11782303. — **S18**
- Bolger, N., & Shrout, P. E. (2005). Accounting for statistical dependency in longitudinal data on dyads. In *Longitudinal Dyadic Data*. http://www.columbia.edu/~nb2229/docs/Bolger%20and%20Shrout-Accounting%20for%20Statistical%20Dependency%20May%202005.pdf — **S52**
- Bodenmann, G., Meuwly, N., & Kayser, K. (2011). Two conceptualizations of dyadic coping and their potential for predicting relationship quality and individual well-being. *European Psychologist*, 16(4), 255–266. https://doi.org/10.1027/1016-9040/a000068 — **S36**
- Cruwys, T., South, E. I., Kim, W., Halford, J. A., Murray, J. A., & Fladerer, M. P. (2022). Measuring "we-ness" in couple relationships: A social identity approach. *Family Process*, 62(3), 795–817. https://doi.org/10.1111/famp.12811 — **S27**
- Emery, L. F., Gardner, W. L., Carswell, K. L., & Finkel, E. J. (2020). Who are "we"? Couple identity clarity and romantic relationship commitment. *Personality and Social Psychology Bulletin*, 47(2), 146–160. https://doi.org/10.1177/0146167220921717 — **S28**
- Falconier, M. K., Jackson, J. B., Hilpert, P., & Bodenmann, G. (2015). Dyadic coping and relationship satisfaction: A meta-analysis. *Clinical Psychology Review*, 42, 28–46. https://doi.org/10.1016/j.cpr.2015.07.002 — **S37**
- Gerpott, F. H., Balliet, D., Columbus, S., Molho, C., & de Vries, R. E. (2018). How do people think about interdependence? A multidimensional model of subjective outcome interdependence. *JPSP*, 115(6), 716–742. https://doi.org/10.1037/pspp0000166 — **S2**
- Gerpott, F. H., et al. Interdependence, the person and the situation. 章节全文 PDF: https://amsterdamcooperationlab.com/wp-content/uploads/2020/11/CH0017_Gerpott_v6_R2_clean.pdf — **S3**
- Gneezy, A., & Fessler, D. M. T. (2012). Conflict, sticks and carrots: war increases prosocial punishments and rewards. *Proceedings of the Royal Society B*, 279(1727), 219–223. https://doi.org/10.1098/rspb.2011.0805 — **S45**
- Guinote, A. (2017). How power affects people: Activating, wanting, and goal seeking. *Annual Review of Psychology*, 68, 677–698. https://doi.org/10.1146/annurev-psych-010416-044153 — **S5**
- Hilpert, P., Randall, A. K., Sorokowski, P., Atkins, D. C., Sorokowska, A., & Ahmadi, K. (2016). The associations of dyadic coping and relationship satisfaction: A cross-national meta-analytic approach. *Frontiers in Psychology* / PMC4976670. — **S39**
- Huston, T. L., Caughlin, J. P., Houts, R. M., Smith, S. E., & George, L. J. (2001). The connubial crucible: Newlywed years as predictors of marital delight, distress, and divorce. *JPSP*, 80(2), 237–252. https://doi.org/10.1037/0022-3514.80.2.237 — **S57 — 仅出版元数据；内容未读**
- Johnson, C., & Ford, R. S. (1996). Dependence power, legitimacy, and tactical choice. *Social Psychology Quarterly*, 59(2). — **S15 — 摘要级；卷页 UNVERIFIED**
- Junkins, E. J., Derringer, J., Ogolsky, B. G., Hardesty, J. L., & Weisberg, Y. (2025/2026). Measures of relationship power dynamics in romantic relationships. *Journal of Family Theory & Review*, 18, 170–191. https://doi.org/10.1111/jftr.70019 — **S20**
- Keltner, D. A., Gruenfeld, D. H., & Anderson, C. P. (2003). Power, approach, and inhibition. *Psychological Review*, 110(2), 265–284. https://doi.org/10.1037/0033-295X.110.2.265 ; 全文 https://greatergood.berkeley.edu/dacherkeltner/docs/keltner.power.psychreview.2003.pdf — **S4**
- Kenny, D. A. (1988). Interpersonal perception: A social relations analysis. *Journal of Social and Personal Relationships*, 5(2), 247–261. https://doi.org/10.1177/026540758800500207 ; 作者自述页 https://davidakenny.net/ip/srmip.htm — **S24**
- Kenny, D. A., & Acitelli, L. K. (2001). Accuracy and bias in the perception of the partner in a close relationship. *JPSP*, 80(3), 439–448. 片段全文 https://cmapspublic.ihmc.us/rid=1K8Z03TTP-15BMW7T-1H1V/Biases_Assumptions_Accuracy.pdf — **S23**
- Kenny, D. A., & Kashy, D. A. (2014). The design and analysis of data from dyads and groups. In *Handbook of Research Methods in Social and Personality Psychology*, pp. 589–607. https://doi.org/10.1017/CBO9780511996481.027 — **S50**
- Laurenceau, J.-P., Barrett, L. F., & Pietromonaco, P. R. (1998). Intimacy as an interpersonal process: The importance of self-disclosure, partner disclosure, and perceived partner responsiveness in interpersonal exchanges. *JPSP*, 74(5), 1238–1251. https://doi.org/10.1037/0022-3514.74.5.1238 ; PDF https://www.affective-science.org/wp-content/uploads/2024/04/LaurenFBPl1998.pdf — **S32**
- Lawler, E. J. (1993). From revolutionary coalitions to bilateral deterrence: A nonzero-sum approach to social power（书章；venue UNVERIFIED）。正文片段: https://ecommons.cornell.edu/server/api/core/bitstreams/cb8acb6b-d8df-4509-8e74-130f6ebed363/content — **S8**
- Lawler, E. J., & Bacharach, S. B. (1987). Comparison of dependence and punitive forms of power. *Social Forces*, 66(2), 446–462. https://doi.org/10.2307/2578749 — **S7**
- Falconier, M. K., & Kuhn, R. (2019). Dyadic coping in couples: A conceptual integration and a research agenda. *Frontiers in Psychology*, 10, 571. https://doi.org/10.3389/fpsyg.2019.00571 — **S38**
- Overall, N. C., & Hammond, M. D. (2026). Power and ideology in close relationships. *Annual Review of Psychology*, 77, 393–421. https://doi.org/10.1146/annurev-psych-012325-032022 — **S6**
- Reis, H. T., & Shaver, P. (1988). Interpersonal process model of intimacy. 章节 PDF: https://sk.sagepub.com/ency/edvol/download/humanrelationships/chpt/interpersonal-process-model-intimacy.pdf — **S34**
- Rusbult, C. E. (1983). A longitudinal test of the investment model: The development (and deterioration) of satisfaction and commitment in heterosexual involvements. *JPSP*, 45(1), 101–117. https://doi.org/10.1037/0022-3514.45.1.101 — **S46**
- Simpson, J. A., Farrell, A. K., & Rothman, A. J. (2019). The dyadic power-social influence model: Extensions and future directions. https://socialinteractionlab.psych.umn.edu/sites/socialinteractionlab.psych.umn.edu/files/files/media/simpson_farrell_rothman_power_chapter_2019.pdf — **S9**
- Solomon, D. H., & Samp, J. A. (1998). Power and problem appraisal: Perceptual foundations of the chilling effect in dating relationships. *JSPR*, 15(2), 191–209. https://doi.org/10.1177/0265407598152004 — **S14 — 出版元数据；内容未读**
- Stress, dyadic coping, and relationship satisfaction: A longitudinal study disentangling timely stable from yearly fluctuations. (2020). *PLOS ONE*. — **S40**
- van Lange, P. A. M., & Rusbult, C. E. (2011). Interdependence theory. In *Handbook of Theories of Social Psychology*, ch.39. https://www.paulvanlange.com/s/vanlangerusbultchap2011-590f.pdf — **S1**
- Bias in perceptions of power in close relationships: The role of self-protection, pro-relationship, and power motives. *Personality and Social Psychology Bulletin*. https://doi.org/10.1177/01461672251409849 — **S19 — 作者名单 UNVERIFIED；本次经高校代理 URL 读到正文**
- We-ness Questionnaire: Development and Validation. (2021). **仅摘要级**（IngentaConnect 页面，Taylor & Francis 旗下；N = 434）。**完整出版元数据（期刊名 / 卷期 / 页码 / DOI）本次未核实**。土耳其样本验证见 DerGipark, *Bartın University Journal of Faculty of Education* (2024)。cognitive / emotional / behavioral 三 facet — **S31**

### 12.2 CITED_SECONDARY

- Acitelli, L. K., Kenny, D. A., & Weiner, D. (2001). The importance of similarity and understanding of partners' marital ideals to relationship satisfaction. *Personal Relationships*, 8(2), 167–185. https://doi.org/10.1111/j.1475-6811.2001.tb00034.x — **S26**
- Anderson, C. P., & Berzaghi, E. (2012). Sense of Power Scale. — **S22**
- Bacharach, S. B., & Lawler, E. J. (1976). The perception of power. *Social Forces*, 55(1), 123–134. https://doi.org/10.1093/sf/55.1.123 — 支撑：dependence power 概念的来源之一
- Bodenmann, G. (2008). *Dyadisches Coping Inventar (DCI). Test Manual*. Huber. — **S41**
- Collins, N. L., & Miller, L. C. (1994). Self-disclosure and liking: A meta-analytic review. *Psychological Bulletin*, 116(3), 457–475. https://doi.org/10.1037/0033-2909.116.3.457 — **S33**
- Emerson, R. M. (1962). Power-dependence relations. *American Sociological Review*, 27(3), 31–41. https://doi.org/10.2307/2089716 — **S49**
- Falbo, T. L., & Peplau, L. A. (1980). Power strategies in intimate relationships. *JPSP*, 38(4), 618–628. https://doi.org/10.1037/0022-3514.38.4.618 — **S16**
- French, J. R. P., & Raven, B. (1959). The bases of social power. In D. Cartwright (Ed.), *Studies in Social Power*, pp. 150–167. — **S17**
- Gonzalez, R., & Griffin, D. (2002). Modeling the personality of dyads and groups. *JPSP*, 83(5), 1109–1126. — **S54**
- Iafrate, R., et al. (2012). Perceived vs. actual dyadic coping similarity.（经 S38 转述） — 支撑内容：**未直接核实**
- Kelley, H. H., & Thibaut, J. W. (1978). *Interpersonal Relations: A Theory of Interdependence*. Wiley. ISBN 9780471034735 / 0471034738; OCLC 3627845 — **S55**
- Kelley, H. H., Holmes, J. G., Kerr, N. L., Reis, H. T., Rusbult, C. E., & Van Lange, P. A. M. (2003). *An Atlas of Interpersonal Situations*. Cambridge University Press. — **S56**
- Kenny, D. A., & Albright, T. (1987). Accuracy in interpersonal perception: A social relations analysis. *Psychological Bulletin*, 102(3), 390–402. https://doi.org/10.1037/0033-2909.102.3.390 — **S25**
- Kenny, D. A., & Cook, W. L. (2006). *Dyadic Data Analysis*. Guilford. — **S53**
- Kollock, P. (1994). The emergence of exchange structures: An experimental study of uncertainty, commitment, and trust. *American Journal of Sociology*, 100(2), 313–345. https://doi.org/10.1086/230539 — **S42**
- Krueger, K. L., & Forest, M. L. (2022). Putting responsiveness in context: How a partner's responsiveness baseline shapes perceived responsiveness. *Personal Relationships*, 29(4), 857–874. https://doi.org/10.1111/pere.12447 — **S35**
- Molm, L. D. (1994). Dependence and risk: Transforming the structure of social exchange. *American Journal of Sociology*. — **S44**
- Moreland, R. L., & Argote, L. (1996). Socially shared cognition at work: Transactive memory and group performance. In *What's Social about Social Cognition? Research on Socially Shared Cognition in Small Groups*, pp. 57–84. https://doi.org/10.4135/9781483327648.n3 — **S58**
- Overall, N. C., & Cross, E. J. (2019). Attachment insecurity and the regulation of power and dependence in intimate relationships. In *Power in Close Relationships*, pp. 28–54. https://doi.org/10.1017/9781108131490.003 — **S11**
- Rusbult, C. E., Verette, J. A., Whitney, G. A., Slovik, L. F., & Lipkus, I. M. (1991). Accommodation processes in close relationships: Theory and preliminary empirical evidence. *JPSP*, 60(1), 53–78. https://doi.org/10.1037/0022-3514.60.1.53 — **S47 — 内容未读**
- Simpson, J. A., Farrell, A. K., Oriña, E. A., & Rothman, A. J. (2015). The dyadic power-social influence model（原始论文；venue UNVERIFIED，p. 409 引文经 S20 转述）。— **S21**
- Transactive memory in close relationships. (2004). In *Close Relationships*, pp. 339–353. https://doi.org/10.4324/9780203311851-29 — **S59 — 作者名单 UNVERIFIED**
- VanderDrift, L. E., Ioerger, M., & Arriaga, X. B. (2019). Interdependence theory and power in close relationships（ch.3, in *Power in Close Relationships*）。— **S12**
- Worley, T. R., & Samp, J. A. (2016). Complaint expression in close relationships: A dependence power perspective（书章）。— **S13**
- Dibble, J. J., et al. (2012). Unidimensional Relationship Closeness scale. — **S30**

### 12.3 AGENT_RECALL / UNVERIFIED

- Homans, J. D. (1960). *Social Behaviour as Exchange*. — **S48 — 不承载本报告任何独立主张**
- Kashy, D. A., & Kenny, D. A. (2000). *American Political Science Review*, 94(4), 765–774. — **S51 — 卷页本次未直接核实**
- Kollock 的 Exchange Structure Scales 四分类标签（reciprocity / lump-sum exchange / unilateral commitment-to-perform / equilateral commitment）。— **S43 — 四标签本次未在原始出处核实；本报告只使用其较弱论断**
- We-ness Questionnaire (2021) 的完整出版元数据（期刊名 / 卷期 / 页码 / DOI）。— **S31 — 仅摘要级；出版元数据未完全核实**
- PSPB 感知权力偏差论文的作者名单。— **S19 — UNVERIFIED**
- 泰后、随访/诉讼材料中常见的 power-bases 操作化（income / education / employment 等 proxy）细节。— 经 S20 转述，未直接核实

---

## 13. 一句话总结

> **LHRM 的 rule 4（mutuality/asymmetry 优先派生）在形式上成立，但需要两个修正：mutuality 必须在 SRM 残差上计算，asymmetry 应当是带声明比较器的比较关系而不是标量。真正不能派生的不是「pair」本身，而是三样东西——惩罚性能力、共同（非零和）权力、以及共享身份/共同项目的表征内容；其中共同应对方（dyadic coping）是文献中唯一被实验证明「两个有向状态的函数不足」的构念。权力的「不得不顺从」体验有间接但真实的支持，却仍缺少直接检验。**
