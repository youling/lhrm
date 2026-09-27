# 10 — 互惠、不对称、权力与依赖的涌现：pair-level 现象能否由两条有向状态派生

**Status:** `RESEARCH_CANDIDATE` / NOT FROZEN
**As of:** 2026-09-27（**Round-3 repair: 依 `ARCHITECT_ADJUDICATION_V1`（`X-13` 决定性）、`CANONICAL_CHANGE_PROPOSALS.md` C-P4、`REJECTED_OR_WEAK_FINDINGS.md` R-D17/R-D18/R-D19/R-D22/R-D26、`HIGH_CONFIDENCE_FINDINGS.md` H-E2/H-E4/H-E5/H-E6、`R-G8`；本轮未编辑任何 canonical doc**）
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
Belief_i(X)      i 关于 X 的信念                          [LHRM 已有层]
T_i(i->j, t)     i 相对 j 的体验性权力 / 顺从感           [本文件提出]
Omega(S)         情境 S 的客观互赖结构                     [本文件提出，本体层缺口]
Phi(i, j, t)     shared pair facts：制度事实、约定、规范、
                 分工、第三极、领域分区                   [LHRM 已有层]
```

> **记号统一（Round-3，naming hygiene only）**：本文件原用 `B_i(X)` 表示 Belief 层，`09` 用 `Belief_i(X)` 表示**同一层**。**本文件统一改为 canonical 已有写法 `Belief_i(X)`**（`docs/foundation/PARAMETER_CONVERGENCE_V0_1.md` §5 B1 已在用 `Belief_i( Dedication_(j->i) )` 形式）。**只改符号，不改任何层的判定、归属或语义**（`R-E7` / `F-C33`：`ACCEPT_AS_PROPOSAL`）。文中 `Belief_i(...)` / `Belief_i( d )` / `Belief_i(Omega(S))` / `Belief_i( R1 )` 等全部为改写后的形式。

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

> **`ACCEPT_AS_PROPOSAL`，但换主论据（R-G8 / `G-C8`）**：支撑本条的**文献引用著录不完整**（§5 `page_verified` 标 `NO`），因此**不以「IT 说互赖很重要」作为主论据**。主论据改用**结构性论证**：
>
> ```text
> canonical 已有：
>   P5  Boundary / Exclusivity Rules  -> BoundaryRule_(A,B,domain)
>   ConstraintsAndAgreements 的域已内建同意/consent
>   -> 非法性、违反社会规范，已经有轴
>
> canonical 没有：
>   约束能力（constrainedness）本身
>   -> 非自愿约束既不是 agreement，也不是 Environment，也不是 Agent。
>
> 精确缺口：违法性有轴，但约束能力本身没有坐标。
> ```
>
> 这条论证**不依赖** `Kelley & Thibaut 1978` 的权威性，只依赖**canonical 自己的两张清单之间的空隙**。`11` lane 独立给出同一诊断并把它标为「**安全价值最高**」。

**主观侧的对应发现（对本项目有直接影响）：**

`Gerpott, Balliet, Columbus, Molho & de Vries (2018, JPSP 115, 716–742)` 用 242 个条目检验发现：人们（在情境内与情境外）**只能可靠区分 6 个维度中的 5 个**——**未能区分的那一维，是「依赖的基础（依赖是来自 partner control 还是 joint control）」这一维**。得到的主观互赖模型（mutual dependence / power / conflict / future interdependence / information certainty）仍能解释 24% 的合作方差，超出 DIAMONDS 模型。

> **命名归一（Round-3，`H-E4`：「含一处术语错配」；两套六维命名必须择一）**：本节原文写作「缺 *coordination*（basis of dependence）」，即把两个**不同的名字**并置。**本文件统一采用 `basis of dependence` 作为该维的唯一名称**，理由是它是 Kelley 等 (2003) 六维清单里的正式名称，也是本文件 §3 上面那张清单用的名字。`Gerpott et al. (2018)` 在其结果描述里对同一失败维度使用了 `coordination` 这个标签。**本文件不主张哪个标签是来源的原词**（`UNKNOWN`，未在本次核实中读到来源对该标签用法的原文表述）。**因此**：正文中该维度**一律写作 `basis of dependence`**；`coordination` 作为**来源自用标签**只在本注记中出现一次，且此后不再使用。
>
> **本项缺口（6→5）本身 `VERIFIED`**（`F-C27`），来源指针与量级（242 条目、解释 24% 合作方差）**不变**。被修掉的只是**术语错配**，不是结论。

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
**判定：`HOLD_FOR_EVIDENCE`（不是 `DERIVABLE`）。** 这是本节相对原文的**降级**，依据 R-D26：朴素的 `H(D_AB, D_BA)` 会**系统性混入与本对无关的成分**（`R_k(i)`、`T_k(j)` 是一般特质，不是本对的 relationship effect），因此**残差化不是可选的优化，而是该派生式成立的前提**。在残差化后的 `H(e_AB, e_BA)` 被证明**显著优于** `H(D_AB, D_BA)` 之前，本条**不得**按「可派生」引用。

**`HOLD_FOR_EVIDENCE` 的解除条件（= 本节已给出的 falsifier，不新增）**

若在控制 `R_k(A), R_k(B), T_k(A), T_k(B)` 之后，`H(e_AB, e_BA)` 对任一 outcome 的增量预测力**不显著优于** `H(D_AB, D_BA)`，则残差化不必要，**本条被证伪**，且朴素写法可作为 readout 使用。**在该检验被执行之前，两条写法都不得被写入 canonical。**

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

即：**asymmetry 是「带声明比较器的比较关系」，不是数字。** 这与 `AGENTS.md` Representation-first invariant 4/5 完全兼容：invariant 4 禁止把所有坐标压进 `0..1` / Euclidean / 单一语义尺度，invariant 5 明确允许「interval, ordinal state, category, constraint, probability distribution, Unknown, or estimate + uncertainty + evidence」。**`distance()` 恰好预设了 invariant 4 所禁止的那件事**（一个共同的欧氏语义尺度）。

**`SUPERSEDED` —— canonical 侧需要修正的具体位置（请求，非本文件执行）**

- **原文（逐字，`docs/foundation/CONSTRUCT_SCOPE_DIRECTIONALITY.md` §2）**：

  ```text
  Asymmetry_k(A,B)
  = distance(
      Z[k,A,B],
      Z[k,B,A]
    )
  ```

  同段随后写：「原则：**reciprocity / mutuality / asymmetry 优先由两条有向边派生，不额外重复设 primitive。**」
- **取代依据**：`AGENTS.md` Representation-first invariant 4 + 5（`CURRENT_ARCHITECTURE.md` §9 原则 3–4 同向）；本节的形式合法性论证。
- **缺陷的精确范围**：**问题在 `distance()` 这个算子，不在「由两条有向边派生」这条原则。** 派生原则**保留**；`distance` 必须换成**显式声明的比较器**。当 `Z` 是区间时，可以**退化**为距离；当 `Z` 是序数、类别、概率分布或 `Unknown` 时，`distance` **未定义**——这不是实现细节。
- **本文件不修改 canonical。** 这是给 `Architect` / canonical 维护者的**修正请求**，见 §11-A2。

**falsifier：** 若某任务（如 case-bank 检索、adversarial 覆盖测试）证明一个**声明过的**序数比较器与一个连续 `distance` 在该任务上无显著差异，则可以退回标量形式。**注意**：该退回**只对被证明的那类任务**成立，不构成对一般情形的豁免（invariant 4 是默认约束，标量形式是需要举证才能取的例外）。该主张待测。

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
  (e) PerceivedDependence_(i, j, S) = Belief_i( d )     [Belief 层]
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
total power    = mutual dependence     （非零和）
```

relative power 就是「谁的依赖更高」。它可以由两条有向依赖的不对称读出。
**判定：`DERIVABLE`。**

> **X-13 落地（本节无「独立 universal Power primitive」）**：`relative power` / `PowerImbalance` 是一个**有向 / 不对称的派生读数**（directional / asymmetry derived readout），**不是**本体里的一个原语。

#### 4.6.2 非零和分量：total power —— 可派生，**但本节原文的实现公式被取代**

`Lawler (1993)` 原文（逐字引用，保留）：

> 「In Emerson's terms, **total power constitutes the level of mutual dependence or 'relational cohesion' in the relationship.** Higher total power in a relationship essentially produces an increase in the opportunity costs associated with leaving the relation.」
> 「**total power has cohesive or integrative effects on the relationship, and these effects are distinguishable from the effects of relative power or power differences.**」
> 「The geometric-mean specification leads to the following proposition: **Proposition 1: If total power in a relationship increases and the power difference decreases, then greater commitment will develop.**」

**`X-13`（Architect 裁决，`DECIDED`）对本节实现规格的更正**——这是本节的**承重修复**：

| # | 内容 |
|---|---|
| 1 | **不存在独立的 universal Power primitive。** 权力侧不新增任何本体原语 |
| 2 | **`TotalDependence` / `TotalPower` = 两个方向的 dependence / capacity 项的**对称派生聚合**（symmetric derived aggregate）。**正确形式是对称聚合**（`Lawler` 用几何平均） |
| 3 | **relational cohesion 是一个独立的关系/过程量**，是 `TP` 与 `RP` **之间的关系**，**不是** `TP` 的定义 |
| 4 | **`RelativePower` / `PowerImbalance` = 有向 / 不对称的派生读数** |
| 5 | **R2-b 四个槽位（punitive capacity / legitimacy & bases / perceived power / felt compliance）保持 `HOLD_FOR_EVIDENCE`**，本文件**不**主张加入 schema |

**本节原文被取代的实现规格（`SUPERSEDED`，原文 + 取代依据）**

- **原文（§4.6.1 代码块）**：`total power    = mutual dependence / "relational cohesion"  （非零和）`
- **原文（§4.6.2 标题）**：「非零和分量：total power —— 可派生但不能被 R2 的写法捕捉」
- **取代依据**：`CONTESTED_FINDINGS.md` X-13（`F-C23` `WRONG-SCOPE`，**技术性错配**）：本文件把 **Lawler 的 relational-cohesion 规格**当成了 **total-power 规格**。`ADJ2` rec 5 独立要求同一更正。
- **技术错配的确切内容**：Lawler 原文中 relational cohesion 与 total power 是**并列出现在同一句里的两个说法**（"the level of mutual dependence or 'relational cohesion'"），而 Prop. 1 把 `total power` 与 `power difference` 作为**两个独立自变量**分别操作。**能作为 `TP` 定义式的只有「对称聚合」；「relational cohesion」是 `TP` 与 `RP` 的关系量**（`TP` 升 + `RP` 差 降 ⇒ 承诺升，即 Prop. 1 本身就把 cohesion 写成了 `TP`/`RP` 的**联合函数**）。把 cohesion 写成 `TP` 的定义，等于把一个**结果/关系量**当成了**自变量**。
- **取代后的形式**：

```text
TotalDependence_(A,B,t) = Agg_sym( Dependence(A->B,t), Dependence(B->A,t) )
                           # 对称聚合；Lawler 的实例化是几何平均
RelativePower_(A,B,t)   = Delta( Dependence(A->B,t), Dependence(B->A,t) )
                           # 有向/不对称读数（不假定可交换算子：见 §4.3）
RelationalCohesion_(A,B,t) = Rel( TotalDependence_(A,B,t), RelativePower_(A,B,t) )
                           # 独立的关系/过程量；Lawler Prop.1 是它的一条实例

三者都是 derived readout。RelationalCohesion 不是 TotalDependence 的定义，
TotalPower 也不是 PowerImbalance 的别名。
```

**注意与 `PARAMETER_CONVERGENCE` P1 的命名冲突**（§4.6.6 已登记，此处补足其精确读法）：`Lawler` 的 "relational cohesion" 与 canonical P1 的 `Cohesion / We-ness` **同名不同义**。前者 = `TP`/`RP` 的**关系**；后者 = **共同体感**。`RelationalCohesion_(A,B,t)` 属**权力侧的关系量**；P1 的 `Cohesion_(A,B)` 属**体感侧**。**两者不得互相代入，也不得互为定义。**

而这有独立经验支持，而且这个经验结果**正是对 R2 只看不平衡这一写法的否证**：

`Overall & Hammond (2026, Annual Review of Psychology 77, 393–421)`：

> 「**This interdependence means that actors' and partners' perceived power tend to be positively correlated rather than inversely related as would occur if power was always zero-sum** (Columbus et al. 2021; Farrell et al. 2015; Hanna-Walker et al. 2024; Körner & Schütz 2024; Körner et al. 2022, 2025; Langner & Keltner 2008; Overall et al. 2023). These positive associations are modest, however, because relationships can involve both actors and partners having high power (mutual control and influence over important outcomes), both having low power …, or each having different levels of power.」

并且（同一篇）：

> 「…**few interactions involve one person having very high power and the other very low power** (Columbus et al. 2021).」

即：真实亲密关系中，**双方都无权**与**双方都有权**是常见情形，而 `f(dependence asymmetry)` 对这两种情形给出的 readout 相同（都是 imbalance ≈ 0）。R2 的写法会把这两种**行为上不同的关系**判成同一个状态。

**判定：`TotalDependence = Agg_sym(Dependence(A->B), Dependence(B->A))` 可派生；R2 的表述遗漏了这一对称分量。**（`H-E2`：**三分判定本身 `VERIFIED`**，错的是实现公式。）

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

#### 4.6.6 结论：权力需要两个派生读数 + 一个关系量；R2-b 槽位保持 `HOLD_FOR_EVIDENCE`

`PARAMETER_CONVERGENCE` R2 判「power = f(dependence, alternatives, resources, constraints)，不先设独立 power 值」。**本文件的「不先设独立 power 值」这半句站得住**（`X-13`：`无独立 universal Power primitive`）；**另一半的公式被取代**（§4.6.2：`TP` 的正确形式是对称聚合，不是 relational cohesion）。

按 `X-13` 重新分档（`H-E2`：**三分判定 `VERIFIED`**，`F-C23`：**实现公式 `WRONG-SCOPE`**）：

```text
【R2-a · 采纳：派生读数，零新原语】
  A1  TotalDependence_(A,B,t) = Agg_sym( Dependence(A->B), Dependence(B->A) )
                                # 对称聚合；Lawler 的实例化是几何平均
  A2  RelativePower_(A,B,t)   = Delta( Dependence(A->B), Dependence(B->A) )
                                # 有向/不对称读数
  A3  PowerImbalance_(A,B)    = A2 的别名 / 投影（保留为 derived readout）
  A4  RelationalCohesion_(A,B,t) = Rel(A1, A2)
                                # 独立的关系/过程量；是 A1 与 A2 的关系，
                                # 不是 A1 的定义。Lawler Prop.1 是它的一条实例。
  A5  domain 索引（domain-indexed facet / context index）

【R2-b · 保持 HOLD_FOR_EVIDENCE：四个槽位，本文件不主张加入 schema】
  B1  punitive / retaliatory capacity
  B2  legitimacy & power bases（legitimate / expert / referent / informational）
  B3  perceived power
  B4  felt compliance / chilling
```

**为什么 R2-b 保持 `HOLD_FOR_EVIDENCE`（逐项，证据来自本文件自己引用的来源）**

| 槽位 | 挡住的证据 | 性质 |
|---|---|---|
| **B1 punitive capacity** | `Lawler & Bacharach (1987)` 实验确实分离了 dependence 与 punitive capability——**方向成立**；但**能分离**≠**应当成为槽位**。把它放进 schema 需要的是**它承载独立因果信息**的检验，不是「它可分离」 | 机制证据，非 slot 证据 |
| **B2 legitimacy & bases** | **本文件自己引用的 `Junkins et al.` 写明**：「There were **no established scales used repeatedly that were developed specifically with power bases in mind**」。**本文件自己的来源否定了本文件的槽位提案** | **自我否定**（`C-P4` 明确点名） |
| **B3 perceived power** | 证据存在（`N = 1,304 dyads`，系统性低估），但它是 `Belief` 层的一个读数，**不是**权力侧的新槽位；它与 A2 的关系是 `truth vs belief` 的并置，属 `X-1`/`X-4` 类的层归属问题 | 层归属问题，非本节裁决 |
| **B4 felt compliance** | **本文件 §4.6.4 自己把它定级为「理论驱动的架构主张，证据是间接的」**；`Lawler 1993` 明说条件**尚未解决**；且其关键来源 `Solomon & Samp (1998, JSPR 15, 191–209)` 被**本文件 §12.1 自己标注为「内容未读」** | **自定级为「不应被当作已确立的发现」+ 关键来源 `内容未读`**（`C-P4` 明确点名） |

**因此本文件的权力侧建议收窄为一句**：

> **R2 应当被改写，不是被否决**：把它限定为「**relative power 分量的 derived readout**」，同时在 schema 中显式加入**对称的 total-dependence 派生读数**与**一个 domain 索引**。`PowerImbalance_(A,B)` 保留为 derived readout。**`relational cohesion` 必须作为 `TP` 与 `RP` 之间的独立关系量登记，不能充当 `TP` 的定义。** R2-b 四个槽位**不加入 schema**，保持 `HOLD_FOR_EVIDENCE`。

**架构发现（需 Architect 判决，本文件不单方面实施）**：上述四条（R2-a）**不新增任何本体原语**；R2-b 涉及的四种表示需求（`P2_capacity` / `P3_perceived` / `P4_felt` / power bases）**在本文件内保持提案状态**，其裁决属于 `X-13` 已裁定范围之外的**新增槽位**问题（`X-13` 明确把它们放在 `HOLD_FOR_EVIDENCE`）。

**注意命名冲突风险：** `Lawler (1993)` 用 "relational cohesion" 指 **`TP` / 互依程度之间的关系**；`PARAMETER_CONVERGENCE` P1 用 "Cohesion / We-ness" 指**共同体感**。两者同名不同义，且**都不是对方的定义**。readback 时必须避免混用。

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

### 4.8 共同应对方（dyadic coping）—— 文献中已知的一处「两个有向状态的函数对预测关系质量不足」

> **`SUPERSEDED` 措辞（R-D18 / `F-C18`；底层 `Bodenmann` 结果本身 `VERIFIED`）**
>
> - **原文（§4.8 标题）**：「共同应对方（dyadic coping）—— 最强的「**真涌现**」证据」
> - **原文（§4.8 首句）**：「这是本文献中**唯一**一个把「两个有向状态的函数」与「联合过程」直接对撞、并且**联合过程赢了**的实验。」
> - **原文（§4.8 判定）**：「**判定：`CommonDyadicCoping_(A,B)` 是真正的 pair-level 涌现候选。**」
> - **取代后的措辞**：「**文献中已知的、唯一一处「两个有向状态的函数在预测关系质量上不足」的构念。**」
> - **取代依据**：删「唯一」与「真涌现」两个未支撑的强主张。理由：(a)「唯一」是**全集断言**，而本文件的检索**没有做**覆盖 dyadic coping 全文献的系统检索，**无分母**（`X-14`：检索覆盖不足被写成领域存在性结论）；(b)「涌现」预设了一个**本体论**结论，而 `Bodenmann` 证明的是**预测力**命题；(c) 原文的实验**没有**排除「联合过程 = `Action/Event` 层的结构化轨迹」这一替代解释（本节末段自己就写了这一点，见 §10 U6）——**因此本文件**不能**断言它「真正」是 pair-level state。**保留为「唯一一处已知的、就预测关系质量而言不足」**，与 `F-C21` 的实体边界一致。

`Bodenmann, Meuwly & Kayser (2011, European Psychologist 16, 255–266; N = 443 瑞士伴侣)`：

> 「Two main models of dyadic coping are proposed in the current literature: (1) a **comparative approach** in which each partner's individual coping is compared with the other’s individual coping with regard to congruence or discrepancy and (2) a **systemic model** where dyadic coping is conceptualized as an **interactive and reciprocal process**… **However the systemic dyadic coping measure is a stronger predictor than the discrepancy measure for relationship quality.**」

**这一条的分量在于**：**discrepancy / congruence 正是「两个有向状态的一个函数」的教科书形式。它在与联合过程竞争同一 outcome（relationship quality）时落败。** 注意命题的**范围**是**对 relationship quality 的预测力**，不是「联合过程是一个独立构念」。

量级：`Falconier, Jackson, Hilpert & Bodenmann (2015, Clinical Psychology Review 42, 28–46)`：72 个独立样本 / 57 篇报告 / **17,856 人**；

> 「the aggregated standardized zero-order correlation (r) for total dyadic coping with relationship satisfaction was **.45** (p < .000)」
> 「**Perceptions of overall dyadic coping by partner and by both partners together were stronger predictors** of relationship satisfaction than perceptions of overall dyadic coping by self.」
> 「comparisons among dyadic coping dimensions indicated that **collaborative common coping**, supportive coping, and hostile/ambivalent coping were stronger predictors than stress communication, delegated coping, protective buffering coping, and overprotection coping.」

**国别 / 调节的声明必须按来源拆成两条**（Round-3 修复：`H-E6` `ACCEPT`，但原文把两件不同的事写成了一对自相矛盾的句子）

| # | 逐来源陈述 | 来源 | `page_verified` |
|---|---|---|---|
| **C1** | Falconier et al. (2015) 的 meta 分析中，dyadic coping 与关系满意度的关联**不被**性别、年龄、关系长度、教育水平、国别**调节** | `Falconier et al. 2015, Clinical Psychology Review 42, 28–46` | **`YES`**（逐字引文在本文件 §4.8 与 §12.1 S37 记录中） |
| **C2** | **另一项独立的跨国 meta 分析**发现关联**被国别显著调节**：香港的 coping 行为对满意度的效应强，加纳/肯尼亚弱（`N = 7,973`, `35 nations`） | `Hilpert et al. (2016)` | **`NO`**（`N` 与 `35 nations` 记于本文件；**具体国别对比数字本次未在原文页核实**） |

**原文（已被取代）**：「而且 effect 在性别、年龄、关系长度、教育、国别上**都不被调节**（罕见的稳健性），但**被国别显著调节**（`Hilpert et al. (2016), N = 7,973, 35 nations`；香港的 coping 行为对满意度的效应强，加纳/肯尼亚弱）。」
**取代依据**：原文在同一句里既说「被国别调节」又说「不被国别调节」，且把两个来源的结论混成一句。**C1 与 C2 不是矛盾**——它们是**两项不同研究在两个不同样本上的结论**；原文的错误是把它们并置成同一批数据的自相矛盾陈述。**拆分后两条各自为真**（C1 `VERIFIED`；C2 的具体国别对比数字标 `NO` / 未在原文页核实）。

`Lehne & Bodenmann (2019, Frontiers in Psychology 10, 571)`（评述 139 项研究）提供两条更尖锐的证据：

> 「**perceived similarity in DC between partners matters more for relationship satisfaction than the actual similarity** (Iafrate et al., 2012).」

> 「After 5 years, couples could be correctly classified in **73%** of the cases regarding whether they would separate or stay together according to their level of DC (Bodenmann & Cina, 2005).」

**结构性论证（比统计论证更强）：** common dyadic coping 的样本题项是

```text
"我们互相帮助，把问题放到新的角度看"（Bodenmann DCI common 维度）
"当我压力大时，我的伴侣倾听我、让我说出真正困扰我的事"（supportive）
```

这些是**联合行动**属性。它们既不是 i 的心理状态，也不是 j 的心理状态，而是**耦合系统的属性**。「我们一起做」这件事，只有把两个 Agent 同时作为系统来看才存在。

**判定：`HOLD_FOR_EVIDENCE` —— `CommonDyadicCoping_(A,B)` 是「两个有向状态的函数在预测 relationship quality 上不足」的一处**已知**案例，因而是**独立 pair state 的候选**；但「候选」不等于「已确立」。**

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
- **`page_verified`（Round-3 新增，R-D19）** — `YES` = 本 lane 打开过该来源的**正文页**并定位到被引文本；`QUOTE_ONLY` = 只拿到被本文件逐字引用的句子（引文本身可核，但**页码 / 段落位置未核**）；`METADATA_ONLY` = 只核了出版元数据，**未读内容**；`NO` = **本 lane 未在原文页核实**（**该行不得按已核实引用**）。

> **为什么必须加这一列（R-D19 / `F-C31`）**：本文件建立了三档证据分级并据此把若干来源标为「本次实际读到原文」。复核发现**若干条的分级或元数据与事实不符**。**问题不是这些来源不可靠，是「本文件声称自己读到了什么」这条元数据不可靠。** 修法不是重写全部引文（那需要新的检索预算），而是**让每一行自己交代可核到什么程度**，使读者可以按行降级使用。**`page_verified: NO` / `METADATA_ONLY` 的行，其「可派生?」判定一律降为 `HOLD_FOR_EVIDENCE` 供引用时自行决定。**

> **`corroboration` 列（Round-3 新增，R-D17）** — `SELF` = 该行与本文件其它行**不独立**（已合并或已重基）；`INDEPENDENT` = 可独立计为一条。**本表多次出现同一现象的同义行（原文 #4/#7、#21b/#23、#19 与 #18、#2 与 #14）**，见下方「合并记录」。

| # | 现象 | 可派生? | 派生形式 / 需要的额外 `Φ` | 增量证据 | 可 falsify 的检验 | 关键引用 | `page_verified` | `corroboration` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 互惠性吸引/互惠欲望 | **`HOLD_FOR_EVIDENCE`**（原文 `Y`，本轮降级，R-D26） | `H(e_att(A→B), e_att(B→A))`，`e = D − R − T`；无额外 `Φ`。**朴素 `H(D,D)` 混入 `R_k(i)`/`T_k(j)`，故残差化是前提而非优化** | 有（bias > accuracy, N=238） | 控制 `R,T` 后 `H(e)` 是否显著优于 `H(D)` | Kenny 1988; Kenny & Acitelli 2001 | `QUOTE_ONLY`（S23/S24 有片段全文 URL；页位置未核） | `INDEPENDENT` |
| 2 | 广义互惠（`R_k(i)` × `T_k(j)` 的跨 dyad 协方差） | Y（nuisance，**不属于 ontology**） | `corr(R_k(i), T_k(j))`，跨 dyad | 有 | N/A | Kenny 1988 | `QUOTE_ONLY` | `SELF`（与 #14 同为 Agent 层互利结构项，见合并记录 M3） |
| 3 | 不对称 | **Y**（**表示必须改**：`distance` → 显式声明的比较器） | `{left, right, comparison, comparator_id, evidence, uncertainty}`；坐标系可比较性为独立假设 | 无直接检验 | 声明过的序数比较器 vs 连续 distance 在具体任务上是否有差异 | `CONSTRUCT_SCOPE` §2; `AGENTS` invariant #4 | `YES`（canonical 文本 §2 逐字） | `INDEPENDENT` |
| 4 | 依赖不平衡 `Dependence_(i,j,S)` | Y（但 D8 应降级） | `Dependence_(i,j,S)` 为 `Omega(S)` 的 readout；需 `Alternatives_(i,ref=(j))` + `Constraint_(i,j)` | 有（IT 六维为情境维度） | 给定 alternatives/constraints/value 后 `OutcomeDependence` 是否有增量 | van Lange & Rusbult 2011; Rusbult 1983 | `QUOTE_ONLY`（S1 有章节 PDF；S46 引文位置未核） | `SELF`（已并入原 #7；见合并记录 M1） |
| 5 | 情境客观互赖结构 `Omega(S)`（actor/partner/joint control；六维） | **N（本体缺口）** | 不是有向状态的函数；需 interdependence matrix 表示 | 有（IT 全套） | 两个有向状态相同但 actor/partner control 相反的 dyad，是否被 LHRM 判为同一状态 | Kelley & Thibaut 1978; Kelley et al. 2003; van Lange & Rusbult 2011 | **`NO`**（书目可核；**正文页未打开**） | `INDEPENDENT` |
| 6 | 情境互赖的**主观**知觉 | Y（6→5 有损） | `Belief_i(Omega(S))`，但需接受 `basis of dependence` 在主观层面不可分 | 有（242 条目，5/6 因子，解释 24% 合作方差） | 亲密关系长期面板中 power 维度是否仍可区分 | Gerpott et al. 2018 | `QUOTE_ONLY`（S2） | `INDEPENDENT` |
| 7 | ~~relative power（零和）~~ | **已并入 #4** | `RelativePower_(A,B,t) = Delta(Dependence(A→B), Dependence(B→A))` | 有 | — | Lawler & Bacharach 1987; Lawler 1993 | `QUOTE_ONLY`（S7/S8） | `SELF`（M1） |
| 8 | total power（非零和）**= `TotalDependence`（`X-13`）** | **Y** | **`Agg_sym(Dependence(A→B), Dependence(B→A))`（Lawler: geometric mean）**。**不是** relational cohesion | 有（双方感知权力正相关） | 双方都无权 vs 双方都有权的 dyad，是否被判为同一状态 | Lawler 1993; Overall & Hammond 2026 | `QUOTE_ONLY`（S8 有正文片段；S6 有引文） | `INDEPENDENT` |
| 8a | `RelationalCohesion_(A,B,t) = Rel(TotalDependence, RelativePower)`（`X-13` 分离项） | Y | 独立关系/过程量；Lawler Prop.1 是它的一条实例。**不是 `TP` 的定义** | 有（Prop.1 的原文陈述） | `TP` 升 + `RP` 差降 ⇒ 承诺升，是否在本样本复现 | Lawler 1993 | `QUOTE_ONLY` | `SELF`（与 #8 同源，**不得**计为两条） |
| 9 | punitive / retaliatory power | **N（`HOLD_FOR_EVIDENCE`，R2-b）** | 不可由 dependence 派生。**本轮不主张加入 schema** | 有（实验分离；partial support 仅对 punitive） | 控制 dependence 后，punitive capacity 是否仍预测 tactics | Lawler & Bacharach 1987; Lawler 1993 | `QUOTE_ONLY` | `INDEPENDENT` |
| 10 | power bases 中非互赖基底（legitimate / expert / referent / informational） | **N（`HOLD_FOR_EVIDENCE`，R2-b）** | 与 dependence 正交。**本轮不主张加入 schema**——`Junkins et al.` 自述「**no established scales used repeatedly that were developed specifically with power bases in mind**」 | 有（orthogonal manipulation, N=320） | 控制 dependence 后 legitimacy 是否预测 coalition/appeal | French & Raven 1959; DPSIM 2019; Johnson & Ford 1996; Junkins et al. 2025 | `METADATA_ONLY`（S20 有引文；S15 摘要级，卷页 `UNVERIFIED`） | `SELF`（与原 G3 / G4 重叠，见 M2） |
| 11 | 感知权力 `PerceivedPower_i` | **N（`HOLD_FOR_EVIDENCE`；层归属待裁，R2-b）** | `Belief_i(...)`；需 truth 侧与 belief 侧并置，允许带符号 gap | 有（N=1,304 dyads，Truth-and-Bias，系统性低估） | 控制真实影响力后，感知是否仍携带独立信息与动机相关偏差 | PSPB DOI `10.1177/01461672251409849`; Guinote 2017 | **`NO`**（S19 经高校代理 URL 读到正文，但**作者名单 `UNVERIFIED`**；页位置未核） | `SELF`（与原 G5 同一条） |
| 12 | 顺从 / 寒效应 `FeltCompliance_i(j,domain)` | **N（`HOLD_FOR_EVIDENCE`；R2-b）** | 不可由结构派生；`Lawler 1993` 明说抵抗 vs 顺从的条件**尚未解决** | 间接 | 控制 `PerceivedPower` 后 chilling 是否仍有增量 | Solomon & Samp 1998; Lawler 1993; Birnbaum et al. 2024; Keltner et al. 2003 | **`METADATA_ONLY`**（S14 Solomon & Samp **内容未读**；S4 Keltner 有全文 URL） | `INDEPENDENT` |
| 13 | 权力–依恋负向耦合 | N/A（有向耦合，非 pair 现象） | `∂(depend)/∂(security_i) < 0` | 间接（章节论断） | APIM cross-lag：`security_i(t−1)` 是否负向预测 `depend_i(t)` | Overall & Cross 2019 | **`NO`**（S11 标 `CITED_SECONDARY`；经导言转述） | `INDEPENDENT` |
| 14 | 互惠规范（general tendency） | N/A（Agent 层） | `generalized reciprocity norm` | — | N/A | Gerpott et al. 章节 | `NO` | `SELF`（M3） |
| 15 | 互惠（作为行为规律） | Y（但不是 state） | `f(ActionHistory_{t−1..t−n})`；需历史 | 有（affordance 无 IT 维度对应） | 互惠是否只由历史预测，而不由 t 时刻两状态预测 | Gerpott et al. 章节; Gneezy & Fessler 2012 | `QUOTE_ONLY` | `INDEPENDENT` |
| 16 | 互惠（作为期待） | Y | `ExpectationOfReciprocity_(i→j,t)`，directed，可 Unknown | 间接 | 期待是否独立于过去的行为比率 | — | `NO`（**本行无关键引用**） | `INDEPENDENT` |
| 17 | 交换结构**类型** | Y（作为类别值 `Φ`） | `ExchangeStructureType_(i,j,domain) ∈ {…}`；**需 `Φ`，非有向状态** | 有（reward vs punishment 互惠可分离） | 高 reward / 零 punishment 的 dyad 是否被单一互惠刻度压平 | Kollock 1994; Molm 1994; Gneezy & Fessler 2012 | `QUOTE_ONLY`（S45 有逐字引文）；Kollock 四分类标签 **`UNVERIFIED`** | `INDEPENDENT` |
| 18 | Common dyadic coping | **N（候选，`HOLD_FOR_EVIDENCE`）** | 联合行动属性；discrepancy（=两有向状态的函数）**在预测 relationship quality 上**落败 | **有（直接判别实验 N=443 + meta N=17,856, r=.45）** | 复现 Bodenmann et al. 2011 的双模型竞争 | Bodenmann, Meuwly & Kayser 2011; Falconier et al. 2015; Lehne & Bodenmann 2019; Hilpert et al. 2016 | `QUOTE_ONLY`（S36/S37/S38/S39 均有逐字引文；**页位置未核**） | `INDEPENDENT` |
| 19 | ~~支持性互惠支持（supportive DC）~~ | **原判定已撤回**（`F-C30`；见合并记录 M4） | 合并入 **#18** 的 `page_verified` 与分维度检验说明 | — | by-self vs by-partner 的差异（by-partner 预测更强）——**这是「测量来源」差异，不是 derivability 差异** | Falconier et al. 2015 | `QUOTE_ONLY` | `SELF`（M4） |
| 20 | 相互亲密 | Y（需第三条输入） | `Conjunction(D_int(A about B), D_int(B about A), ActionHistory_j responded)` | 有（事件日记法） | 单向 `D_int` 高的 dyad 是否被误判为 mutual | Laurenceau et al. 1998; Reis & Shaver 1988 | `QUOTE_ONLY`（S32 有片段全文 URL） | `INDEPENDENT` |
| 21 | we-ness / cohesion（整体） | **N（作为标量）→ 拆分** | Cruwys 四因子：3 个已在 LHRM，1 个新 | 有（N=375，7 量表 → 4 因子，各自独立） | 四因子是否在 LHRM 已有坐标上各自可表示 | Cruwys et al. 2022/2023 | `QUOTE_ONLY`（S27 有逐字引文） | `INDEPENDENT` |
| 21a | we-ness 的 `partner liking` 分量 | **Y** | 即 `D1 Liking_(i→j)` | 有 | 该因子是否与 `Liking` 完全共线 | Cruwys et al. | `QUOTE_ONLY` | `INDEPENDENT` |
| 21b | ~~`partner similarity` 分量~~ | **已并入 #23** | 见 #23 | — | — | Cruwys et al. | `QUOTE_ONLY` | `SELF`（M5） |
| 21c | `relationship orientation` 分量 | Y | Agent 层 relational interdependent self-construal，domain 索引 | 有 | 同上 | Cruwys et al. | `QUOTE_ONLY` | `INDEPENDENT` |
| 21d | `couple identity` 分量 | **?（弱候选）** | 需要 `CoupleIdentity_(A,B,t)`（pair 共享内容）+ 两个 directed belief | 有（N=375 中预测力最强） | 见 #22 | Cruwys et al. | `QUOTE_ONLY` | `INDEPENDENT` |
| 22 | couple identity **clarity** | **N（不是一致性的函数）** | `Belief_i(CoupleIdentity)`，**clarity 是 `direction` 变量**（`i` 关于「我们是谁」的清楚程度，与 `j` 的 clarity 独立）；需 pair 对象 + 两个 directed belief | **有（直接：超越 agreement 预测 commitment（Study 2）+ 预测 9 月内解体可能性降低（Study 4））** | 在控制「双方对身份的实际一致」后 clarity 是否仍有增量 | Emery, Gardner, Carswell & Finkel (2021), *PSPB* **47(1)**, 146–160 | `QUOTE_ONLY`（S28 有逐字引文；**期号 47(1) 本轮已修**，见 §6.2-B1） | `INDEPENDENT` |
| 23 | value congruence / goal alignment **+ `partner similarity`**（合并行） | Y | Agent 属性或状态的比较（**已吸收原 #21b `partner similarity`**；与 `P2 ValueCongruence` / `P3 GoalAlignment` 同类） | 间接（Acitelli 等的 general vs specific 理解分离） | general 与 specific understanding 分离后哪部分预测满意度 | Acitelli, Kenny & Weiner 2001; Cruwys et al. | **`NO`**（S26 标 `CITED_SECONDARY`） | `SELF`（M5：已吸收 21b） |
| 24 | satisfaction / commitment | 部分 N | `commitment = satisfaction + investment − alternatives`；alternatives 需带 pair 参照 | 有（Rusbult 纵向） | 控制 alternatives 后 commitment 是否仍有增量 | Rusbult 1983 | `QUOTE_ONLY`（S46） | `INDEPENDENT` |
| 25 | accommodation 过程 | **N** | 二元抑制反应，结果分 recovering / condemning 两条路径 | 弱（**未读原文**） | 恢复 vs 谴责不能由瞬时状态和表示 | Rusbult et al. 1991 | **`METADATA_ONLY`**（S47 自标「内容未读」） | `INDEPENDENT` |
| 26 | transactive memory 分工 | **N** | 共享外部存储中「谁存了什么」，不是任一成员状态的函数 | 弱（框架引用） | 若双方都完整记得全部内容，transactive 结构是否仍不同 | Moreland & Argote 1996; *Close Relationships* 2004 ch. | **`NO`**（S59 作者名单 `UNVERIFIED`） | `INDEPENDENT` |

**合并记录（R-D17 / `F-C30`：「表格当前形态」`REJECT`；`corroboration` 纪律）**

| id | 合并/撤回 | 理由 | 是否由本文件自身的交叉引用确认 |
|---|---|---|---|
| **M1** | 原 **#7 relative power** 并入 **#4 依赖不平衡** | `relative power` 就是 dependence 不对称的读数，**是 #4 的一个特例**，不是独立现象。原文把特例与一般情形并列为两行 | 是（§4.6.1 原文：「relative power 就是『谁的依赖更高』」） |
| **M2** | 原 **G3 权力基底** 与原 **G4 合法性与申诉策略** 并为 **#10** | 两者都主张「legitimacy 类内容与 dependence 正交、需独立表示」，**是同一条主张的两次陈述**（三重计数模式） | 是（§8 原 G3 与 G4 的「最小补丁方向」列给出同一个 `Legitimacy_(i,j,domain)`） |
| **M3** | 原 **#2 广义互惠** 与原 **#14 互惠规范（general tendency）** 标为 `SELF`，**不合并但禁止重复计数** | 两者都是 Agent 层 / 跨 dyad 的互利结构 nuisance 量，**都不属于 ontology**；但一个是统计量、一个是 trait，语义不同，故**保留两行、禁止计为两条证据** | 是（§4.2 与 §4.7(c) 各自给出「不属于 LHRM ontology / 不是 pair 状态」的判定） |
| **M4** | 原 **#19 supportive DC** 的「部分 Y」判定**撤回**，行改为 **#18 的分维度说明** | 原文的「可派生」判定**无依据**：`Falconier et al. (2015)` 给的是「**by-partner 的知觉比 by-self 的知觉预测更强**」——这是**测量来源（informant source）**的比较，与 derivability 无关。用它支持「部分 Y」是把一个测量学发现当成派生性证据 | 是（§4.8 原文自己的引文与 §5 #19 的「可 falsify 的检验」列**不匹配**：后者问的是 by-self vs by-partner，前者问的是能否派生） |
| **M5** | 原 **#21b `partner similarity`** 并入 **#23** | 两者都标注为「Agent 属性比较（与 `P2 ValueCongruence` 同类）」——**同一派生形式、同一层、同一 falsifier** | 是（#21b 与 #23 的「派生形式」列与「可 falsify 的检验」列逐字相同） |
| **M6** | 新增 **#8a `RelationalCohesion`** | `X-13` 要求 `TP` 与 relational cohesion 分离；若不显式列为一行，读者仍会把 cohesion 当 `TP` 的定义。**新增行标 `SELF`**：它与 #8 同源，**不得计为第二条独立证据** | —（`X-13` 的技术性要求） |


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

**B1. 最尖锐的一条证据：clarity 超越 agreement。** `Emery, Gardner, Carswell & Finkel (2021, PSPB 47(1), 146–160)` 引入 **couple identity clarity**（「作为伴侣二人中的一员，我相信我们知道自己作为一对是谁」），四项研究（横断 1–2、实验 3、纵向 4）：

> 「Moreover, **higher couple identity clarity, although related to actual agreement between partners on their identity as a couple, predicted commitment above and beyond agreement** (Study 2) — as well as **predicted reduced likelihood of relationship dissolution over a 9-month period** (Study 4).」

> **期号已修（Round-3，`H-E5`）**：本节原写 `PSPB 47, 146–160`，§12.1 原写 `47(2), 146–160`。**正确期号为 `47(1)`**（`Emery, Gardner, Carswell & Finkel (2021), Personality and Social Psychology Bulletin, 47(1), 146–160`）。**卷号 47、页码 146–160、年份 2021 不变**。取代依据：`H-E5`（`F-C28`，`VERIFIED`）明写「修 issue 号（47(1)）」。**本文件不主张原 `47(2)` 是事实错误**——只主张本文件自报的期号与 `H-E5` 核实的 `47(1)` 不一致，按 `47(1)` 记。

> **clarity 是 `direction` 变量（Round-3 补，`H-E5` 明写「在 §6.2-B1 补一句」）**：couple identity **clarity 不是 pair 级标量，而是有向量**——
> ```text
> CoupleIdentityClarity_(i->j, t) = Belief_i( "我们知道自己作为一对是谁" 的清楚程度 )
> ```
> `i` 对「我们」的清楚程度与 `j` 对「我们」的清楚程度**可以是两个独立值**，且**不可**被压成一个 pair 标签。理由与本文件 §4.7(c)/§4.9 一致：`AGENTS.md` Current architecture direction 4 要求有向状态独立建模；「双方都清楚」与「只有一方清楚」是不同状态，而 pair 标签会丢掉后者。**因此 §6.3 的 `Belief_i( R1 )` 必须是两个有向 belief，而不是一个 pair 内容的两个副本**——本节原文写的是「两个 directed belief states」，本条确认该写法**正确**，并把「为什么必须是两个」的根据补在这里。


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

> **`ARBITRATION ROUTE`（Round-3，移交 Architect，本文件不解决）**：上面这条线索与 `09` §9.3.1 的 L-A 合法性判据 (ii)（「被关系状态更新而非生成关系状态」）**直接冲突**：本文件 §6.2-B3 证明 pair 内容（couple-based goals / 分工）**直接改写有向状态**（dependence → power）。两侧逐字引文见 `09` 新增的 §9.10 `A3e-ARB-1`。**本文件在此只登记，不单方面收窄 `09` 的判据 (ii)，也不把 B3 降级。** 冲突的实质：`AGENTS.md` Current architecture direction 5 只要求 shared pair facts 与 directional states **分开记**，**没有**要求 pair 事实**不得**生成有向状态；`09` 的判据 (ii) 是比 rule 5 **更严**的读法。**收窄 (ii) 还是保留 (ii)，是 canonical 裁决，不是研究问题。**

**这个判决的 falsifier：** 若 couple identity clarity 在**加入 joint Action/Event 历史**（公开承诺、共同决定、共同叙述行为）后不再有增量，则 `PairRepresentation_R1` 也是派生的，整个 `KEEP` 应降级为 `DERIVED from Action/Event history`。本 lane **未找到**做这个检验的研究（见 §10 U2）。

---

## 7. 权力与依赖：readout 还是不可约成分？

任务问：power 能否是 asymmetry + alternatives + constraints 的 readout，还是 power 有不可约的关系-体验成分（例：「不得不顺从」的主观感）。

**判决：R2 的「不先设独立 power 值」这半句成立；R2 的公式这半句要改；R2-b 的四个槽位不属于本轮。** 按 `X-13`（`DECIDED`）分档：

```text
【R2-a · 采纳为派生读数，本文件主张落地】
  total power / TotalDependence_(A,B,t)
      = Agg_sym( Dependence(A->B), Dependence(B->A) )   ← 对称聚合（Lawler: 几何平均）
  relative power / RelativePower_(A,B,t)
      = Delta( Dependence(A->B), Dependence(B->A) )     ← 有向/不对称读数
  PowerImbalance_(A,B)  = 保留为 derived readout（RelativePower 的投影）
  RelationalCohesion_(A,B,t) = Rel(TotalDependence, RelativePower)
      ← 独立关系/过程量；是 TP 与 RP 的关系，不是 TP 的定义
  domain 索引：facet / context index
  三者都从 Omega(S) + alternatives + value + constraints 读出；都【不是】本体原语

【R2-b · 保持 HOLD_FOR_EVIDENCE，本文件【不】主张加入 schema】
  (1) punitive / retaliatory capacity
  (2) legitimacy / power bases（legitimate / expert / referent / informational）
  (3) perceived power        —— 另有一层归属问题（它是 Belief 层读数）
  (4) felt compliance / chilling
```

**为什么 (1)–(4) 不落地**（证据来自本文件自己引用的来源；详见 §4.6.6 的逐项表）：`Junkins et al.` 明写「There were **no established scales used repeatedly that were developed specifically with power bases in mind**」（否定了 (2)）；`Lawler 1993` 明说 resistance vs compliance 的条件**尚未解决**，且本文件自己把 (4) 定级为「不应被当作已确立的发现」，其关键来源 `Solomon & Samp (1998)` 被本文件 §12.1 自标「**内容未读**」。(1) 与 (3) 方向可辩护，但「可分离」与「应当成为槽位」是两件事，缺的是**承载独立因果信息**的检验。

所以对 Architect 的具体问题——「`PARAMETER_CONVERGENCE` R2 应当被改写还是被否决？」——的回答是：

> **R2 应当被改写，不是被否决。** 把它限定为「**relative power 分量的 derived readout**」，同时在 schema 中显式加入**对称的 total-dependence 派生读数** + **relational cohesion 作为独立关系量** + **一个 domain 索引**。`PowerImbalance_(A,B)` 保留为 derived readout。**R2-b 的四个槽位本轮不落地，保持 `HOLD_FOR_EVIDENCE`。**

**并且要明确记录**：`felt compliance` 曾是本 lane 唯一主张的「不可约关系-体验成分」，**其证据是间接的**（`Lawler 1993` 明说条件未知；没有任何研究在控制 perceived power 后检验 felt compliance 的增量）。这是 §10 U4，**不应被当作已确立的架构发现**——**本轮据此把它从「建议加入 schema」降为 `HOLD_FOR_EVIDENCE`**。

---

## 8. 文献中存在的、当前有向状态框架**根本无法表示**的现象（gap list）

按「缺口类型」排序。类型：`ontology hole` = 世界/情境表示缺失；`construct hole` = 缺构念；`projection hole` = 本体有但局部投影取不到。

| # | 现象 | 缺口类型 | 为什么当前框架表示不了 | 最小补丁方向 | 关键引用 |
| --- | --- | --- | --- | --- | --- |
| G1 | **情境的客观互赖结构** `Omega(S)`：actor control / partner control / joint control；六维结构 | **ontology hole** | LHRM 只把世界投影到两个具体人，没有「情境的 outcome-contingency 结构」这一实体。两个有向状态相同、情境结构相反的 dyad 会被判为同一状态。**canonical 的精确缺口是：非法性有轴（P5 / `ConstraintsAndAgreements` 已内建同意/consent），但约束能力本身没有坐标** | 在 `RelevantEnvironment` / `PairState` 之上增加一个 `SituationStructure` 对象；可借用 IT 的 matrix 表示为转移表。**`ACCEPT_AS_PROPOSAL`，换主论据为 canonical 内部空隙论证（见 §3 修订块）** | Kelley & Thibaut 1978; van Lange & Rusbult 2011（**`page_verified: NO`**） |
| G2 | **惩罚性/报复性能力** | construct hole（**`HOLD_FOR_EVIDENCE` / R2-b，本轮不主张加入 schema**） | 不是 dependence 的函数（实验分离） | 独立 construct family，directed。**「可分离」≠「应当成为槽位」** | Lawler & Bacharach 1987; Lawler 1993 |
| G3+G4 | **权力基底与合法性**（legitimate / expert / referent / informational）+ **合法性与申诉策略**（**已合并，原为 G3 / G4 两行**） | construct hole（**`HOLD_FOR_EVIDENCE` / R2-b**） | 这四种基底与互赖无直接关系；DPSIM 承认它们是核心基底，但 `Junkins et al.` 自述「**no established scales used repeatedly that were developed specifically with power bases in mind**」；dependence 结构亦不决定策略选择（`Johnson & Ford 1996` 的正交操纵） | 至少 legitimate / expert 基底需要表示；可用 Agent 属性 + domain 参照。**但本文件【不】主张本轮加入 schema** | French & Raven 1959; DPSIM 2019; Junkins et al. 2025; Johnson & Ford 1996 |
| G5 | **实际影响力与感知影响力的带符号差距** | 混合（**`HOLD_FOR_EVIDENCE` / R2-b**；另涉层归属） | 需要 truth 侧与 belief 侧同时存在并可比较 | 在 dyadic representation 中为同一定义保留 `actual` 与 `perceived` 两个坐标。**与 §5 #11 是同一条，标 `SELF`，不得计两次** | PSPB DOI `10.1177/01461672251409849`（**作者名单 `UNVERIFIED`**）; Guinote 2017 |
| G6 | **共同（total）权力 / 非零和权力** | **已在 §4.6.2 / §7 落地（R2-a）；不再是 gap** | R2 只看不平衡，把「双方都无权」和「双方都有权」压平 | **已给出**：`TotalDependence_(A,B,t) = Agg_sym(Dependence(A→B), Dependence(B→A))` + `RelationalCohesion = Rel(TP, RP)`。**X-13 已裁决** | Overall & Hammond 2026; Lawler 1993 |
| G7 | **交换结构类型** | `Φ` 的类别值缺失 | 「单方面承诺」与「对等承诺」在行为上不同，不能用一个刻度 | 类别值 `ExchangeStructureType_(i,j,domain)` | Kollock 1994; Gneezy & Fessler 2012 |
| G8 | **联合/耦合过程**（common dyadic coping 等） | construct hole（**候选，`HOLD_FOR_EVIDENCE`**） | 联合行动属性不是任一人的状态；comparison 版本**在预测 relationship quality 上**落败（`N = 443`） | `PairState` 下新增一个 **joint process** 分支（结构化轨迹或状态均可，见 U6） | Bodenmann et al. 2011; Falconier et al. 2015 |
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
2. **不主张「power 不可由 dependence 派生」适用于全部 power。** 分量区分见 §7；`X-13` 已把「不先设独立 power 值」这半句定为成立。
3. **不主张把 Gneezy & Fessler (2012) 的群际冲突实验结论直接外推到亲密关系。** 只用它支持「互惠的 reward 与 punishment 分支可分离」这一较弱命题。
4. **不主张 PSPB 感知权力偏差研究（DOI `10.1177/01461672251409849`）证明了实际权力与感知权力之间有因果关系。** 只主张存在系统性、动机驱动的偏差。**该文作者名单本次未在稳定公开出处核实（`UNVERIFIED`）。**
5. **不主张 `CoupleIdentity` 一定是独立 pair state。** 只主张存在不能由「双方一致」与「两条有向状态」解释的残余；「joint Action/Event 历史的函数」这一替代解释未被排除。
6. **不主张 SRM 残差化是 ontology 主张。** `D_k` 是 primitive，`e_k` 是 readout。**但本文件主张残差化是 `Mutuality_k` 该派生式成立的**前提**（判定 `HOLD_FOR_EVIDENCE`）——「不主张它是 ontology 主张」与「主张它是必要步骤」不矛盾。**
7. **不主张 6→5 的互赖维度塌缩适用于亲密关系长期情境。** `Gerpott et al. (2018)` 的样本是情境描述任务。**本文件不主张 `coordination` 与 `basis of dependence` 中哪个是来源原词（`UNKNOWN`）**；本文件统一用 `basis of dependence` 作为该维的唯一名称（§3 命名归一块）。
8. **不主张 Lawler 的 "relational cohesion" 等于 LHRM 的 `Cohesion`。** 前者是 `TP` 与 `RP` 之间的**关系量**；后者 = 共同体感。**同名不同义，且互不为定义，必须在 readback 时避免。** **同样不主张 relational cohesion 等于 `TotalDependence`**（`X-13` 的技术性更正，见 §4.6.2）。
9. **不主张本文件对 `Huston, Caughlin, Houts, Smith & George (2001)`（JPSP 80, 237–252; DOI `10.1037/0022-3514.80.2.237`）有任何实证发现的使用。** 该文本次只核实了出版元数据，**未读内容**。它在本文件中仅作为「cohesion 已被多维操作化」的存在性指针。
10. **不主张本文件对 rule 4 的任何修改。** §4.3 关于「asymmetry 应是带声明比较器的比较关系」是对**表示形式**的细化主张，Architect 可独立否决。**本文件未修改 `docs/foundation/CONSTRUCT_SCOPE_DIRECTIONALITY.md`；那是一份修正请求。**
11. **不主张文献数量或 LLM 一致度构成验证。** 每个「derivable」都配 falsifier；没有 falsifier 的已进入 gap list。
12. **不主张我读过 LHRM issue #20 / #21 / #22。** 没有读取、执行或引用。
13. **不主张本文件完成了 `OutcomeDependence`（D8）的实测裁决。** 见 §10 U1。
14. **不主张 `PairState` 必须包含 joint process。** `Bodenmann et al. (2011)` 证明的是「两条有向状态的函数**在预测 relationship quality 上**不够」，**没有**证明「必须有独立 pair state」。**同样不主张它是文献中「唯一」一处不足**（无分母；`X-14`）。
15. **不主张本文件评估了 `PARAMETER_CONVERGENCE_V0_1.md` v0.1 的 8 项 directed basis 的完备性。** 本 lane 只测 pair-level 派生问题。
16. **不主张 §5 表中 `page_verified: NO` / `METADATA_ONLY` 的行已核实。** 这些行的「可派生?」判定**不得**按已核实结果引用（`R-D19`）。
17. **不主张 `09` 的 §7-O3 判据 (ii) 已被本文件推翻。** §6.2-B3 与该判据的冲突已登记为 Architect 裁决项（`A3e-ARB-1`），本文件**不单方面裁决**。
18. **不主张 R2-b 的四个槽位已被否决。** 它们是 `HOLD_FOR_EVIDENCE`——**既未被采纳，也未被否决**；本文件不主张它们为假，只主张现有证据不足以把它们写进 schema。

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
| A1 | 在 `mutuality / asymmetry` 的派生规范中**加入 SRM 残差化前置步骤**（`e = D − R − T`），并标注 `e` 属 measurement 层。**注意**：`Mutuality_k` 当前的判定是 `HOLD_FOR_EVIDENCE`（R-D26），**残差化是前提而非优化**；A1 是「把前提写进规范」，不是「宣告已可派生」 | §4.1；Kenny 1988; Kenny & Acitelli 2001 | 高 |
| A2 | 把 `Asymmetry_k` 的表示从 `distance()` 改为「带声明比较器的比较关系」——**这是对 `docs/foundation/CONSTRUCT_SCOPE_DIRECTIONALITY.md` §2 的 canonical 修正请求，不是本文件自行生效**（§4.3 已给出待替换文本） | §4.3；`AGENTS` invariant #4/#5 | 中 |
| A3 | 把 D8 `OutcomeDependence` 降级：标为 `Omega(S)` 的 readout，或 `Belief_i` 层的知觉；不再作为 directed psychological state | §4.4；Rusbult 1983 | 高 |
| A4 | 改写 R2（`X-13` **已裁决**）：限定为 relative power 分量的 derived readout；**加入对称的 `TotalDependence = Agg_sym(Dependence(A→B), Dependence(B→A))` 派生读数**；**加入 `RelationalCohesion = Rel(TP, RP)` 作为独立关系量**（**不是 `TP` 的定义**）；加入一个 domain 索引。**R2-b 的四个槽位（punitive capacity / legitimacy&bases / perceived power / felt compliance）本轮【不】加入 schema，保持 `HOLD_FOR_EVIDENCE`** | §4.6.2、§4.6.6、§7；`X-13`; `C-P4`; Lawler & Bacharach 1987; Overall & Hammond 2026 | 高 |
| A5 | 在 ontology 中补 `SituationStructure`（`Omega`），与 `Environment` / `PairState` 并列。**主论据用 canonical 内部空隙**（非法性有轴、约束能力无坐标），不依赖 IT 权威性 | §3；`R-G8` | 高 |
| A6 | 明确否决 `Cohesion_(A,B)` 标量；把 P1 改名为 `PairRepresentation` 族（couple identity / shared project / division of labor / shared external memory）+ 两个 directed belief + 有向入边 | §6.3；Cruwys et al. 2022/2023; Emery et al. 2021 | 高 |
| A7 | 拆分 `Reciprocity`：拒绝标量；建 `ExchangeStructureType_(i,j,domain)` 类别值 + 两个 directed 期待 | §4.7 | 中 |
| A8 | 在 `PairState` 概念下留出 **joint process** 分支（不急于定义坐标）；把 `CommonDyadicCoping` 作为第一个候选 case | §4.8；Bodenmann et al. 2011 | 中（U6 未决） |
| A9 | 补一条 `AttachmentSecurity_(i→j) → Dependence_(i→j)` 的有向负向耦合边 | §4.10；Overall & Cross 2019 | 中 |
| A10 | 记录命名冲突：`Lawler` 的 "relational cohesion" ≠ LHRM 的 `Cohesion`；**且 ≠ `TotalDependence`**（`X-13`） | §4.6.2、§4.6.6 | 低（readback 时处理） |
| **A11** | **把 §5 表的 `page_verified` 与 `corroboration` 两列一起带进任何下游汇总**——`page_verified: NO` / `METADATA_ONLY` 的行不得按已核实结果引用；`corroboration: SELF` 的行不得重复计数 | §5；R-D17; R-D19 | 高（纯记账，零新证据） |
| **A12** | **把 `Mutuality_k` 的判定从 `DERIVABLE` 改为 `HOLD_FOR_EVIDENCE` 后的连带影响**：`PARAMETER_CONVERGENCE` R1 当前写 `Mutuality_k(A,B) = H(Z[k,A,B], Z[k,B,A])`（**未含残差化**）。**R1 的现写法与 A1 冲突**——若 A1 落地，R1 的公式需同步标注「须残差化后才成立」 | §4.1；R-D26; `PARAMETER_CONVERGENCE` §9 R1 | 高 |

**建议的 status 判定：**

```text
R10 lane status                       : SUCCESS（部分结论本轮降级/收回，见下）
其中 R2（power 完整表述）子结论       : PARTLY_NEGATIVE + X-13 已裁决
    三分判定（relative/total/punitive）: VERIFIED（H-E2）——【保留】
    TP 的实现规格（曾误用 cohesion）  : CORRECTED（X-13 / F-C23）
    R2-b 四个槽位                    : HOLD_FOR_EVIDENCE（X-13 裁决）——【不加入 schema】
    relational cohesion              : 独立关系量 Rel(TP, RP)，非 TP 的定义
Mutuality_k（SRM 残差化）             : HOLD_FOR_EVIDENCE（本轮由 DERIVABLE 降级，R-D26）
Asymmetry_k 的表示形式               : DERIVABLE，但 distance 必须换成显式声明的比较器
    CoupleIdentity 独立 pair state    : PARTIAL
    joint process 的本体地位          : UNKNOWN（交 R06/R09）
所有「derivable」判断                 : 形式论证 + 文献支持，未经量化；全部配 falsifier
§5 表的证据可核性                     : 逐行 page_verified；NO / METADATA_ONLY 行不得按已核实引用
§5 表的独立性                         : 6 处合并/撤回（M1–M6）；SELF 行不得重复计数
```

**本轮对自身结论的收回清单（parent join 需据此生成 `SUPERSEDED_BY_REPAIR`）**

| # | 原表述 | 新判定 | 依据 |
|---|---|---|---|
| 1 | `§4.1` 「判定：`DERIVABLE`（但必须残差化）」 | **`HOLD_FOR_EVIDENCE`** | R-D26 |
| 2 | `§4.6.1` 「`total power = mutual dependence / "relational cohesion"`」 | **`TotalDependence = Agg_sym(...)`；cohesion 是 `Rel(TP, RP)`** | `X-13`; `F-C23` |
| 3 | `§4.8` 标题「最强的「真涌现」证据」+ 首句「**唯一**」+ 判定「真正的 pair-level 涌现候选」 | 「文献中已知的、唯一一处『两个有向状态的函数在**预测关系质量上**不足』」；判定 `HOLD_FOR_EVIDENCE` | R-D18 / `F-C18` |
| 4 | `§4.8`「effect 在……国别上**都不被调节**……但**被国别显著调节**」 | 拆成 **C1（Falconier 2015，不被国别调节）/ C2（Hilpert 2016，被国别调节）** | `H-E6`; 内部自相矛盾 |
| 5 | `§3`「缺 *coordination*（basis of dependence）」 | 统一为 `basis of dependence`；`coordination` 只作来源自用标签注记一次 | `H-E4`（术语错配） |
| 6 | `§6.2-B1` `PSPB 47, 146–160`（§12.1 `47(2)`） | **`47(1)`**，另补「clarity 是 direction 变量」 | `H-E5` |
| 7 | `§4.6.6` / `§7` / `§11-A4`「显式登记 punitive capacity、legitimacy/bases、perceived power、felt compliance **四个槽位**」 | **`HOLD_FOR_EVIDENCE`，本轮不加入 schema** | `X-13`; `C-P4` |
| 8 | `§5` 表 #7 / #21b（独立行）、#19（「部分 Y」） | #7 并入 #4；#21b 并入 #23；#19 判定**撤回** | R-D17 / `F-C30` |
| 9 | `§2` 记号 `B_i(X)` | **`Belief_i(X)`** | `R-E7` / `F-C33`（naming hygiene） |

---

## 12. 引用列表

> 分三类：`CITED_PRIMARY`（本次实际读到原文/原始摘要/出版元数据）、`CITED_SECONDARY`（经他人文献转述）、`AGENT_RECALL / UNVERIFIED`（本次未核实）。
> 全部核实日期：**2026-09-27**。
> 编号与 packet `§2` 的 S 编号一致，便于回查。
>
> **`page_verified` 列（Round-3 新增，R-D19 / `F-C31`）**：原三分级把「读到原文/原始摘要/出版元数据」**混在一级**，因此一条只核了出版元数据的条目与一条打开过正文页的条目在同一级。复核发现**若干条的分级或元数据与事实不符**。**修法是加一列，不重写引文。** 含义：
> - `YES` = 打开过正文页并定位到被引文本；
> - `QUOTE_ONLY` = 拿到被本文件逐字引用的句子，**页码/段落位置未核**；
> - `METADATA_ONLY` = 只核出版元数据，**未读内容**；
> - `NO` = **本 lane 未在原文页核实**。
>
> **本表下方的每条都已补 `page_verified`**（`S28` 已在上方条目内标注）。**`NO` / `METADATA_ONLY` 的条目不得按「已核实原文」引用**——这是 R-D19 的处置，不是一条新的科学判断。

### 12.1 CITED_PRIMARY

- Agnew, N. R., & Harman, A. M. (Eds.). (2019). *Power in Close Relationships*. Cambridge University Press. 章节导言 excerpt: https://assets.cambridge.org/97811071/92614/excerpt/9781107192614_excerpt.pdf — **S10** -- page_verified: YES
- Aron, A., Aron, E. N., & Smollan, D. (1992). Inclusion of Other in the Self Scale and the structure of interpersonal closeness. *JPSP*, 63(4), 596–612. https://doi.org/10.1037/0022-3514.63.4.596 — **S29** -- page_verified: NO
- Birnbaum, G. E., Kanat-Maymon, Y., Zholtack, K., Avidan, R., & Reis, H. T. (2024). The power to flirt: Power within romantic relationships and extradyadic sexual interest. PMC11782303. — **S18** -- page_verified: QUOTE_ONLY
- Bolger, N., & Shrout, P. E. (2005). Accounting for statistical dependency in longitudinal data on dyads. In *Longitudinal Dyadic Data*. http://www.columbia.edu/~nb2229/docs/Bolger%20and%20Shrout-Accounting%20for%20Statistical%20Dependency%20May%202005.pdf — **S52** -- page_verified: NO
- Bodenmann, G., Meuwly, N., & Kayser, K. (2011). Two conceptualizations of dyadic coping and their potential for predicting relationship quality and individual well-being. *European Psychologist*, 16(4), 255–266. https://doi.org/10.1027/1016-9040/a000068 — **S36** — `page_verified: QUOTE_ONLY`
- Cruwys, T., South, E. I., Kim, W., Halford, J. A., Murray, J. A., & Fladerer, M. P. (2022). Measuring "we-ness" in couple relationships: A social identity approach. *Family Process*, 62(3), 795–817. https://doi.org/10.1111/famp.12811 — **S27** -- page_verified: QUOTE_ONLY
- Emery, L. F., Gardner, W. L., Carswell, K. L., & Finkel, E. J. (2021). Who are "we"? Couple identity clarity and romantic relationship commitment. *Personality and Social Psychology Bulletin*, **47(1)**, 146–160. https://doi.org/10.1177/0146167220921717 — **S28 — `page_verified: QUOTE_ONLY`；期号 `47(1)` 为 Round-3 依 `H-E5` 修正（原 `47(2)`）；clarity 为 direction 变量，见 §6.2-B1**
- Falconier, M. K., Jackson, J. B., Hilpert, P., & Bodenmann, G. (2015). Dyadic coping and relationship satisfaction: A meta-analysis. *Clinical Psychology Review*, 42, 28–46. https://doi.org/10.1016/j.cpr.2015.07.002 — **S37** — `page_verified: QUOTE_ONLY`
- Gerpott, F. H., Balliet, D., Columbus, S., Molho, C., & de Vries, R. E. (2018). How do people think about interdependence? A multidimensional model of subjective outcome interdependence. *JPSP*, 115(6), 716–742. https://doi.org/10.1037/pspp0000166 — **S2** — `page_verified: QUOTE_ONLY`
- Gerpott, F. H., et al. Interdependence, the person and the situation. 章节全文 PDF: https://amsterdamcooperationlab.com/wp-content/uploads/2020/11/CH0017_Gerpott_v6_R2_clean.pdf — **S3** -- page_verified: QUOTE_ONLY
- Gneezy, A., & Fessler, D. M. T. (2012). Conflict, sticks and carrots: war increases prosocial punishments and rewards. *Proceedings of the Royal Society B*, 279(1727), 219–223. https://doi.org/10.1098/rspb.2011.0805 — **S45** — `page_verified: QUOTE_ONLY`
- Guinote, A. (2017). How power affects people: Activating, wanting, and goal seeking. *Annual Review of Psychology*, 68, 677–698. https://doi.org/10.1146/annurev-psych-010416-044153 — **S5** -- page_verified: QUOTE_ONLY
- Hilpert, P., Randall, A. K., Sorokowski, P., Atkins, D. C., Sorokowska, A., & Ahmadi, K. (2016). The associations of dyadic coping and relationship satisfaction: A cross-national meta-analytic approach. *Frontiers in Psychology* / PMC4976670. — **S39** — `page_verified: NO`（`N = 7,973` / `35 nations` 记于 §4.8 表 C2；**具体国别对比数字未在原文页核实**）
- Huston, T. L., Caughlin, J. P., Houts, R. M., Smith, S. E., & George, L. J. (2001). The connubial crucible: Newlywed years as predictors of marital delight, distress, and divorce. *JPSP*, 80(2), 237–252. https://doi.org/10.1037/0022-3514.80.2.237 — **S57 — 仅出版元数据；内容未读** -- page_verified: METADATA_ONLY
- Johnson, C., & Ford, R. S. (1996). Dependence power, legitimacy, and tactical choice. *Social Psychology Quarterly*, 59(2). — **S15 — 摘要级；卷页 UNVERIFIED** — `page_verified: NO`
- Junkins, E. J., Derringer, J., Ogolsky, B. G., Hardesty, J. L., & Weisberg, Y. (2025/2026). Measures of relationship power dynamics in romantic relationships. *Journal of Family Theory & Review*, 18, 170–191. https://doi.org/10.1111/jftr.70019 — **S20** -- page_verified: QUOTE_ONLY
- Keltner, D. A., Gruenfeld, D. H., & Anderson, C. P. (2003). Power, approach, and inhibition. *Psychological Review*, 110(2), 265–284. https://doi.org/10.1037/0033-295X.110.2.265 ; 全文 https://greatergood.berkeley.edu/dacherkeltner/docs/keltner.power.psychreview.2003.pdf — **S4** -- page_verified: QUOTE_ONLY
- Kenny, D. A. (1988). Interpersonal perception: A social relations analysis. *Journal of Social and Personal Relationships*, 5(2), 247–261. https://doi.org/10.1177/026540758800500207 ; 作者自述页 https://davidakenny.net/ip/srmip.htm — **S24** -- page_verified: QUOTE_ONLY
- Kenny, D. A., & Acitelli, L. K. (2001). Accuracy and bias in the perception of the partner in a close relationship. *JPSP*, 80(3), 439–448. 片段全文 https://cmapspublic.ihmc.us/rid=1K8Z03TTP-15BMW7T-1H1V/Biases_Assumptions_Accuracy.pdf — **S23** -- page_verified: QUOTE_ONLY
- Kenny, D. A., & Kashy, D. A. (2014). The design and analysis of data from dyads and groups. In *Handbook of Research Methods in Social and Personality Psychology*, pp. 589–607. https://doi.org/10.1017/CBO9780511996481.027 — **S50** -- page_verified: NO
- Laurenceau, J.-P., Barrett, L. F., & Pietromonaco, P. R. (1998). Intimacy as an interpersonal process: The importance of self-disclosure, partner disclosure, and perceived partner responsiveness in interpersonal exchanges. *JPSP*, 74(5), 1238–1251. https://doi.org/10.1037/0022-3514.74.5.1238 ; PDF https://www.affective-science.org/wp-content/uploads/2024/04/LaurenFBPl1998.pdf — **S32** -- page_verified: QUOTE_ONLY
- Lawler, E. J. (1993). From revolutionary coalitions to bilateral deterrence: A nonzero-sum approach to social power（书章；venue UNVERIFIED）。正文片段: https://ecommons.cornell.edu/server/api/core/bitstreams/cb8acb6b-d8df-4509-8e74-130f6ebed363/content — **S8** — `page_verified: QUOTE_ONLY`
- Lawler, E. J., & Bacharach, S. B. (1987). Comparison of dependence and punitive forms of power. *Social Forces*, 66(2), 446–462. https://doi.org/10.2307/2578749 — **S7** — `page_verified: QUOTE_ONLY`
- Falconier, M. K., & Kuhn, R. (2019). Dyadic coping in couples: A conceptual integration and a research agenda. *Frontiers in Psychology*, 10, 571. https://doi.org/10.3389/fpsyg.2019.00571 — **S38** -- page_verified: QUOTE_ONLY
- Overall, N. C., & Hammond, M. D. (2026). Power and ideology in close relationships. *Annual Review of Psychology*, 77, 393–421. https://doi.org/10.1146/annurev-psych-012325-032022 — **S6** — `page_verified: QUOTE_ONLY`
- Reis, H. T., & Shaver, P. (1988). Interpersonal process model of intimacy. 章节 PDF: https://sk.sagepub.com/ency/edvol/download/humanrelationships/chpt/interpersonal-process-model-intimacy.pdf — **S34** -- page_verified: NO
- Rusbult, C. E. (1983). A longitudinal test of the investment model: The development (and deterioration) of satisfaction and commitment in heterosexual involvements. *JPSP*, 45(1), 101–117. https://doi.org/10.1037/0022-3514.45.1.101 — **S46** -- page_verified: QUOTE_ONLY
- Simpson, J. A., Farrell, A. K., & Rothman, A. J. (2019). The dyadic power-social influence model: Extensions and future directions. https://socialinteractionlab.psych.umn.edu/sites/socialinteractionlab.psych.umn.edu/files/files/media/simpson_farrell_rothman_power_chapter_2019.pdf — **S9** -- page_verified: QUOTE_ONLY
- Solomon, D. H., & Samp, J. A. (1998). Power and problem appraisal: Perceptual foundations of the chilling effect in dating relationships. *JSPR*, 15(2), 191–209. https://doi.org/10.1177/0265407598152004 — **S14 — 出版元数据；内容未读** -- page_verified: METADATA_ONLY
- Stress, dyadic coping, and relationship satisfaction: A longitudinal study disentangling timely stable from yearly fluctuations. (2020). *PLOS ONE*. — **S40** -- page_verified: NO
- van Lange, P. A. M., & Rusbult, C. E. (2011). Interdependence theory. In *Handbook of Theories of Social Psychology*, ch.39. https://www.paulvanlange.com/s/vanlangerusbultchap2011-590f.pdf — **S1** -- page_verified: QUOTE_ONLY
- Bias in perceptions of power in close relationships: The role of self-protection, pro-relationship, and power motives. *Personality and Social Psychology Bulletin*. https://doi.org/10.1177/01461672251409849 — **S19 — 作者名单 UNVERIFIED；本次经高校代理 URL 读到正文** -- page_verified: NO
- We-ness Questionnaire: Development and Validation. (2021). **仅摘要级**（IngentaConnect 页面，Taylor & Francis 旗下；N = 434）。**完整出版元数据（期刊名 / 卷期 / 页码 / DOI）本次未核实**。土耳其样本验证见 DerGipark, *Bartın University Journal of Faculty of Education* (2024)。cognitive / emotional / behavioral 三 facet — **S31** -- page_verified: NO

### 12.2 CITED_SECONDARY

- Acitelli, L. K., Kenny, D. A., & Weiner, D. (2001). The importance of similarity and understanding of partners' marital ideals to relationship satisfaction. *Personal Relationships*, 8(2), 167–185. https://doi.org/10.1111/j.1475-6811.2001.tb00034.x — **S26** -- page_verified: NO
- Anderson, C. P., & Berzaghi, E. (2012). Sense of Power Scale. — **S22** -- page_verified: NO
- Bacharach, S. B., & Lawler, E. J. (1976). The perception of power. *Social Forces*, 55(1), 123–134. https://doi.org/10.1093/sf/55.1.123 — 支撑：dependence power 概念的来源之一 -- page_verified: NO
- Bodenmann, G. (2008). *Dyadisches Coping Inventar (DCI). Test Manual*. Huber. — **S41** -- page_verified: METADATA_ONLY
- Collins, N. L., & Miller, L. C. (1994). Self-disclosure and liking: A meta-analytic review. *Psychological Bulletin*, 116(3), 457–475. https://doi.org/10.1037/0033-2909.116.3.457 — **S33** -- page_verified: NO
- Emerson, R. M. (1962). Power-dependence relations. *American Sociological Review*, 27(3), 31–41. https://doi.org/10.2307/2089716 — **S49** -- page_verified: NO
- Falbo, T. L., & Peplau, L. A. (1980). Power strategies in intimate relationships. *JPSP*, 38(4), 618–628. https://doi.org/10.1037/0022-3514.38.4.618 — **S16** -- page_verified: NO
- French, J. R. P., & Raven, B. (1959). The bases of social power. In D. Cartwright (Ed.), *Studies in Social Power*, pp. 150–167. — **S17** -- page_verified: NO
- Gonzalez, R., & Griffin, D. (2002). Modeling the personality of dyads and groups. *JPSP*, 83(5), 1109–1126. — **S54** -- page_verified: NO
- Iafrate, R., et al. (2012). Perceived vs. actual dyadic coping similarity.（经 S38 转述） — 支撑内容：**未直接核实** -- page_verified: NO
- Kelley, H. H., & Thibaut, J. W. (1978). *Interpersonal Relations: A Theory of Interdependence*. Wiley. ISBN 9780471034735 / 0471034738; OCLC 3627845 — **S55** -- page_verified: METADATA_ONLY
- Kelley, H. H., Holmes, J. G., Kerr, N. L., Reis, H. T., Rusbult, C. E., & Van Lange, P. A. M. (2003). *An Atlas of Interpersonal Situations*. Cambridge University Press. — **S56** -- page_verified: METADATA_ONLY
- Kenny, D. A., & Albright, T. (1987). Accuracy in interpersonal perception: A social relations analysis. *Psychological Bulletin*, 102(3), 390–402. https://doi.org/10.1037/0033-2909.102.3.390 — **S25** -- page_verified: NO
- Kenny, D. A., & Cook, W. L. (2006). *Dyadic Data Analysis*. Guilford. — **S53** -- page_verified: METADATA_ONLY
- Kollock, P. (1994). The emergence of exchange structures: An experimental study of uncertainty, commitment, and trust. *American Journal of Sociology*, 100(2), 313–345. https://doi.org/10.1086/230539 — **S42** -- page_verified: NO
- Krueger, K. L., & Forest, M. L. (2022). Putting responsiveness in context: How a partner's responsiveness baseline shapes perceived responsiveness. *Personal Relationships*, 29(4), 857–874. https://doi.org/10.1111/pere.12447 — **S35** -- page_verified: NO
- Molm, L. D. (1994). Dependence and risk: Transforming the structure of social exchange. *American Journal of Sociology*. — **S44** -- page_verified: NO
- Moreland, R. L., & Argote, L. (1996). Socially shared cognition at work: Transactive memory and group performance. In *What's Social about Social Cognition? Research on Socially Shared Cognition in Small Groups*, pp. 57–84. https://doi.org/10.4135/9781483327648.n3 — **S58** -- page_verified: NO
- Overall, N. C., & Cross, E. J. (2019). Attachment insecurity and the regulation of power and dependence in intimate relationships. In *Power in Close Relationships*, pp. 28–54. https://doi.org/10.1017/9781108131490.003 — **S11** -- page_verified: NO
- Rusbult, C. E., Verette, J. A., Whitney, G. A., Slovik, L. F., & Lipkus, I. M. (1991). Accommodation processes in close relationships: Theory and preliminary empirical evidence. *JPSP*, 60(1), 53–78. https://doi.org/10.1037/0022-3514.60.1.53 — **S47 — 内容未读** -- page_verified: METADATA_ONLY
- Simpson, J. A., Farrell, A. K., Oriña, E. A., & Rothman, A. J. (2015). The dyadic power-social influence model（原始论文；venue UNVERIFIED，p. 409 引文经 S20 转述）。— **S21** -- page_verified: NO
- Transactive memory in close relationships. (2004). In *Close Relationships*, pp. 339–353. https://doi.org/10.4324/9780203311851-29 — **S59 — 作者名单 UNVERIFIED** -- page_verified: NO
- VanderDrift, L. E., Ioerger, M., & Arriaga, X. B. (2019). Interdependence theory and power in close relationships（ch.3, in *Power in Close Relationships*）。— **S12** -- page_verified: NO
- Worley, T. R., & Samp, J. A. (2016). Complaint expression in close relationships: A dependence power perspective（书章）。— **S13** -- page_verified: NO
- Dibble, J. J., et al. (2012). Unidimensional Relationship Closeness scale. — **S30** -- page_verified: NO

### 12.3 AGENT_RECALL / UNVERIFIED

- Homans, J. D. (1960). *Social Behaviour as Exchange*. — **S48 — 不承载本报告任何独立主张** -- page_verified: NO
- Kashy, D. A., & Kenny, D. A. (2000). *American Political Science Review*, 94(4), 765–774. — **S51 — 卷页本次未直接核实** -- page_verified: NO
- Kollock 的 Exchange Structure Scales 四分类标签（reciprocity / lump-sum exchange / unilateral commitment-to-perform / equilateral commitment）。— **S43 — 四标签本次未在原始出处核实；本报告只使用其较弱论断** -- page_verified: NO
- We-ness Questionnaire (2021) 的完整出版元数据（期刊名 / 卷期 / 页码 / DOI）。— **S31 — 仅摘要级；出版元数据未完全核实** -- page_verified: NO
- PSPB 感知权力偏差论文的作者名单。— **S19 — UNVERIFIED** -- page_verified: NO
- 泰后、随访/诉讼材料中常见的 power-bases 操作化（income / education / employment 等 proxy）细节。— 经 S20 转述，未直接核实 -- page_verified: NO

---

## 13. 一句话总结

> **LHRM 的 rule 4（mutuality/asymmetry 优先派生）在形式上成立，但需要三个修正：mutuality 必须在 SRM 残差上计算（且其当前判定是 `HOLD_FOR_EVIDENCE`，不是「已可派生」）；asymmetry 应当是带声明比较器的比较关系而不是标量；权力侧必须把 `TotalDependence`（对称聚合）与 `RelationalCohesion`（`TP` 与 `RP` 的关系）**分开记**，后者不得充当前者的定义。真正不能派生的不是「pair」本身，而是三样东西——惩罚性能力、共同（非零和）权力、以及共享身份/共同项目的表征内容；其中共同应对方（dyadic coping）是**文献中已知的一处「两个有向状态的函数在预测关系质量上不足」的构念**。权力的「不得不顺从」体验有间接但真实的支持，却仍缺少直接检验，因此保持 `HOLD_FOR_EVIDENCE`。**
