# Construct Scope & Directionality — LHRM 构念跨域作用与方向性

**Status:** Architecture note v0.1  
**As of:** 2026-09-07  
**Scope:** Human–Human Dyad  
**Purpose:** 固化“同一构念可在 Agent / Target / Directed Dyad / Pair 等不同位置出现，但其语义侧重点不同”的当前架构判断，并明确方向性、互惠/非互惠、动态耦合与低冗余之间的关系。

> 本文件冻结的是**表示原则**，不是最终参数表、权重或数值模型。

---

## 1. 核心原则：参数名回答“是什么”，索引回答“谁对谁、在哪一层、什么时候”

LHRM 不再假设“一个参数只能属于 S、O、D、E 之一”。更准确的表达是：

> **一个 construct family 可以在多个作用位置上拥有不同但相关的语义分量。**

例如 attraction 构念族可以包含：

- `source / perceiver component`：某个 Agent 一般是否容易被他人吸引；
- `target component`：某个 Agent 一般是否容易诱发他人吸引；
- `directed dyad component`：特定 i 对特定 j 的、无法由一般倾向与目标效应完全解释的特殊吸引；
- `pair-derived pattern`：由 i→j 与 j→i 两个方向组合出的互惠、非互惠、不对称等模式。

可写成近似分解：

```text
Construct(i -> j, t)
= population baseline
+ source_i
+ target_j
+ directed_dyad_(i->j)
+ context/history residual
```

该结构与 Social Relations Model 的 perceiver / target / relationship effect 思想相容；LHRM 将其推广到动态、部分可观测、跨构念的统一表示接口。

---

## 2. 方向性是关系状态的一级属性

凡是“某个人对另一个人”的状态，应优先视为有向量：

```text
Z[k, i, j, t]
```

其中：

- `k` = construct；
- `i` = source / evaluator / actor；
- `j` = target / recipient；
- `t` = time。

例如：

```text
Z[sexual_desire, A, B, t]
Z[sexual_desire, B, A, t]
```

是两个独立状态，允许：

```text
A -> B 高，B -> A 低
A -> B 低，B -> A 高
双方都高
双方都低
```

“双方都有性欲”不是第三个 primitive，而是两个有向状态的组合模式：

```text
MutualSexualDesire(A,B)
= H(
    SexualDesire(A->B),
    SexualDesire(B->A)
  )
```

类似地，不对称程度也应优先派生：

```text
Asymmetry_k(A,B)
= distance(
    Z[k,A,B],
    Z[k,B,A]
  )
```

原则：**reciprocity / mutuality / asymmetry 优先由两条有向边派生，不额外重复设 primitive。**

---

## 3. 同一 construct family 可跨多个 scope，但不能机械复制

对候选构念 `k`，收敛时应依次问：

```text
k 在 Agent/source 上是否有独立语义？
k 在 Target 上是否有独立语义？
k 在 i->j directed edge 上是否有独立语义？
k 是否存在 pair-level 共同属性或可派生模式？
k 是否只是 action / observation / belief / constraint？
```

只有在该位置存在可独立定义、可测量、可解耦的语义时才保留。

因此不采用“所有参数在 S/O/D 各复制一份”的机械模板。

### 示例 A：Attraction family

可能存在：

```text
AttractionSusceptibility_i      # source 一般易被吸引程度
TargetAttractiveness_j          # target 一般诱发吸引程度
Attraction_(i->j)               # 特定 i 对 j 的特殊吸引
MutualAttraction_(i,j)          # pair-derived
```

### 示例 B：Trust family

更可能是：

```text
GeneralizedTrust_i              # Agent 一般信任倾向
Trustworthiness_j               # Target 可被信赖特征/行为证据
Trust_(i->j)                    # i 对 j 的方向性信任状态
```

这里三者属于同一家族，但并不是同一个 psychological construct 的简单复制。

### 示例 C：Caregiving family

可区分：

```text
CaregivingPropensity_i          # Agent 一般照顾倾向
CareNeed_j                      # Target 当前照护需求
Caregiving_(i->j)               # i 对 j 的实际照护倾向/关系状态
CaregivingReciprocity_(i,j)     # pair-derived
```

“肯花钱”“陪诊”“接送”“做饭”通常先是 action / observable proxy，用于更新 caregiving、responsiveness、dedication 等状态，而不直接成为平级 primitive。

---

## 4. 低冗余不等于动态独立

LHRM 对参数的“低相关”目标应正式解释为：

> **低语义/条件冗余，而不是要求状态变量彼此不产生因果影响。**

两个构念可以在语义上独立，同时在状态转移中高度耦合。

例如：

```text
MoneySpent_(A->B)
```

是 action / observation，而不是 attraction primitive；但它可通过 Belief 更新影响：

```text
PerceivedCare_(B->A)
Trust_(B->A)
AttachmentSecurity_(B->A)
RomanticAttraction_(B->A)
Dedication_(B->A)
```

且方向取决于解释与上下文：同样的花钱行为可能被理解为 care，也可能被理解为 control / transaction / display。

因此状态动力学允许：

```text
partial F_i / partial z_j != 0
```

但仍要求 `z_i` 与 `z_j` 不是同一潜变量的重复命名。

---

## 5. 状态、行动与策略必须分开

某一关系状态存在与否会改变 Agent 的 action policy，但状态本身不等于行为。

例如：

```text
SexualDesire_(S->O) high
```

可能改变：

```text
P(Action | current state)
```

如提高接近、求偶投入、容忍、注意、风险接受等某些行为概率；但这些都不是确定性结果，也不应把文化俗语或性别刻板规则硬编码为状态转移定律。

原则：

```text
State != Action
State influences ActionPolicy
Action/Event updates State
```

---

## 6. 当前推荐的数学直觉

LHRM 可暂时把世界表达为关系图：

```text
G_t = (V, E_t)
```

针对具体 Human Dyad 做局部投影：

```text
X_(S,O,t)
= Phi_(S,O)(G_t)
```

局部状态可包含：

```text
AgentState_S
AgentState_O
DirectedState_(S->O)
DirectedState_(O->S)
PairState_(S,O)
Belief_S
Belief_O
RelevantEnvironment
```

关系向量/构念场可作为其中一部分，但当前不假定整个状态空间必然是普通欧氏空间。连续量、概率、类别、规则/约束可能共同构成混合状态空间。

因此“向量”目前主要保留以下含义：

- 有方向；
- 可分解为多个语义分量；
- 同一事件可对多个分量产生不同作用；
- 两个反向分量可构成 mutuality / asymmetry 等 pair-level 派生量；
- 可用于后续可视化与状态转移表达。

不预先承诺线性叠加、欧氏距离或物理意义上的“力”。

---

## 7. 对 Parameter Convergence 的约束

后续每个候选 parameter family 都应通过：

1. `scope test`：属于 source / target / directed edge / pair / belief / action / constraint 中哪些位置；
2. `directionality test`：i→j 与 j→i 是否可稳定解耦；
3. `mutuality derivation test`：pair mutuality 是否可由双向量派生，避免重复 primitive；
4. `semantic redundancy test`：是否与已有构念重复描述同一 latent state；
5. `dynamic coupling test`：若相互影响，明确影响路径，而不是因为相关便合并；
6. `cross-context test`：same-sex / opposite-sex / kin / non-kin / stranger / established relationship 是否保持语义稳定。

---

## 8. 当前一句话结论

> **LHRM 的 primitive 不应只是“参数名清单”，而应是带有作用位置、方向与时间索引的构念族；同名家族可跨 S/O/D 等局部作用域呈现不同侧面，互惠与不对称优先由双向状态派生，参数之间允许强动态耦合，但应避免语义重复与双重计数。**
