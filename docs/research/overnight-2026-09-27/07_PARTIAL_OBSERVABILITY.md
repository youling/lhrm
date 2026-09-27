# 07 — 稀疏输入 / 缺失性 / 不确定性的深度审计

**Status:** `RESEARCH_CANDIDATE` — 未经 Human/Architect 审阅，不得当作已确立结论、参数或公式
**Lane:** R07 · Wave 1 · Work Order `youling/lhrm#30@overnight-opencode-exploration-swarm-v1`
**Scope:** 只审计「`Unknown` 应如何表示、应如何传播、应如何被读出」，不提出新的关系构念，不改动 ontology
**核实日期:** 2026-09-27（所有时效性声明均以此日为准）

> 证据等级约定：`CITED_PRIMARY`（读到原文或官方摘要全文）/ `CITED_METADATA`（只核到 DOI 元数据，未读正文）/ `CITED_SECONDARY`（转述页）/ `AGENT_RECALL`（先验，本次未核）。模型层面的推断一律标 `MODEL_HYPOTHESIS`，架构建议标 `AI_RECOMMENDATION`。**文献数量与 LLM 一致度不构成验证。**

---

## 0. 本报告的定位与两条主张的准确措辞

本 lane 被指派审计两条项目主张。核验结果：

| 指派中的主张 | 项目内实际文本 | 位置 | 判定 |
| --- | --- | --- | --- |
| `Unknown -> prior / conditional distribution` | `Unknown -> prior / uncertainty`（对照 `Unknown -> zero deviation`） | `docs/foundation/PROJECT_HISTORY_2026-09-10.md:102`、`:108` | 存在。**但作为恒等式成立，作为设计规则未经规定** |
| "missingness lowers certainty, not computability" | `Computable != Certain` | `docs/foundation/STAGE_SUMMARY_2026-09-07.md:162` | **字面形式不存在。** 项目持有的是**更弱**的区分性陈述 |

**第二个措辞的差异不是文字游戏：**

- `Computable != Certain` 只说「可计算与确定不是同一件事」。
- "missingness lowers certainty, not computability" 是一个**不变性主张**：它断言缺失作用在确定性上、**不**作用在可计算性上。

第二个更强，而**第二个部分为假**（§6）。本报告因此：

- **不**把项目判为「主张了错的东西」；
- **而是**给出：弱版本成立的理由、强版本失效的 8 个模式、以及两者之间那个恰好可写进 canonical 的中间版本（§5.4）。

### 0.1 一个必须先说的空白

对 `D:\coding\lhrm\**\*.md` 全量检索 `refine|monoton|⊑|preorder|lattice|composabl|propagat`，**唯一 1 处命中**且与数学格无关：

```
docs/RESEARCH_REPORT_DATING_APP_PARAMETER_PRIMITIVES.md:240
| B12 | 家庭背景财富 | 家庭资源 + 赡养义务 | O/E | 百合字段；承担 lattice 但不可当个人资源 |
```

**LHRM 现有 durable 资料中，没有任何关于 refinement、单调性、预序、数学格、或 `Unknown` 组合传播的形式化内容。**

本报告因此**不是**对已有设计的修补建议，而是**新增候选**。这一点必须写明，否则下游 lane 会误以为存在一个「已被违反的不变量」。

---

## 1. 缺失性的机制分类：为什么 `Unknown` 不是一个类型

在讨论表示之前，必须先说清「缺失」有多少种，因为**不同种类的缺失在数学上不是同一个问题**。

`[MODEL_HYPOTHESIS]` 下面的分类是本报告的工作分类，用于后续类型化；每种给出机制类型、数学后果、以及它是否让「`Unknown → prior`」成立。

| tag | 机制 | 机制类型 | 对该 dyad 的正确数学类型 | `Unknown → prior` 是否成立 | 证据 |
| --- | --- | --- | --- | --- | --- |
| `no_evidence` | 无人报告、也无人不报告 | MCAR/MAR | 分布（可能是多峰） | 名义上成立（= 先验） | — |
| `refused` | 被问及但主体拒答 / 选「无意见」 | **MNAR** | **比先验更宽的集合**；不做插补 | **不成立** | Krosnick et al.：拒答主因是 satisficing（疲劳、低努力、题目靠后、低教育），且给出 "don't know" 选项**降低**了实质回答数却**不改变**重测信度（`CITED_PRIMARY`，完整书目 `PARTIAL_BIB`） |
| `private_to_partner` | 存在但只对 partner 可观测 | **结构性单侧可观测** | 需按 reporter 索引；`PairState` 上不 reporter-invariant | **不成立**（读者侧无信息 ≠ 人口先验） | Swann et al. (1994)：婚内伴侣报告呈 self-verification 系统偏倚，N=176 夫妻（`CITED_PRIMARY`，摘要） |
| `withheld_by_actor` | 主动隐瞒 | **MNAR 且机制内生** | 与 `refused` 同类，但机制模型不同 | **不成立** | 同上 + Belnap 1977 动机 |
| `disputed` | 存在相反证据 | **冲突** | 需独立于 `n` 的值（K4 的 `b`） | **不成立，且不可映射到 `n`** | Belnap 1977；Mundhenk et al.（`CITED_PRIMARY` / `CITED_SECONDARY`） |
| `censored` | 结构性空单元（如只对自报使用者询问使用行为） | **MNAR，按构造** | **结构性空**；不是小样本 | **不成立**（见 FM1） | Tennenholtz 2023 的 delphic 不可约性（`CITED_PRIMARY`） |
| `structurally_unobservable` | 原则上不可被该通道观测 | **非认知** | **不进入状态**；输出 "not addressable" | **不适用** | — |
| `not_yet_real` | 尚未发生 | **时间性** | **未来未定义**；需 trace/truncated 域 | **不适用** | 需与 `F-01` 的双序区分 |
| `superseded` | 被更新证据取代 | 惰性 | 由 `history_id` DAG 承载 | — | `CURRENT_ARCHITECTURE.md:241-252` 已有 `tau = (history_id, local_time)` |
| `unmeasured_by_instrument` | 工具未测 | 测量层 | 需 measurement model，否则不可辨识 | **不成立** | Raykar et al. 2010（`CITED_PRIMARY`） |

**这张表是本报告最重要的产出之一。** 它的直接后果是：

> `Unknown` 不是一个类型，它是**至少四个不同数学对象**的共同标签。`AGENTS.md:24` 禁止了「静默压成 neutral」，但目前**没有**任何规则禁止「把 10 种 `Unknown` 压成一个 `Unknown`」——而后者是同一种违规的更隐蔽形式。

---

## 2. Unknown 表示的候选形式化菜单与代数性质

### 2.1 六个候选

| 编号 | 表示 | 载体 | 支持的运算 | 丢失什么 | 成本 | 是否过度设计 |
| --- | --- | --- | --- | --- | --- | --- |
| **R1** | 点 + 置信度 `(v, p)` | `ℝ × [0,1]` | 比较、排序、平均、欧氏距离 | **多峰性**、机制 tag、`Unknown` 的类型；把 `⊥` 与「0.5」混同 | 极低 | **不推荐。** `p = 0.5` 就是一个 neutral 值，直接违反 `AGENTS.md:24`；且它无法表达「我不知道」与「我认为是 0.5」的差别 |
| **R2** | 区间 `[a,b]` | 带 `⊥` 的 Scott 域上的闭区间 | `min`/`max`（t-norm/t-conorm）、宽度、外延原理（extension principle） | 形状（多峰）、联合分布（独立假设）、机制 | 低 | **推荐做 display 层**；不能替代 R3/R6 |
| **R3** | 分布 `π(·)` | 概率测度 | 全套概率运算、KL、credal 上下界 | **不可辨识性**（多个 `π` 同样拟合数据）、联合结构 | 中 | **推荐做 store 层。** `CURRENT_ARCHITECTURE.md:286` 已允许「estimate + uncertainty + evidence，甚至直接保存 posterior distribution」 |
| **R4** | credal 集 `K(π)` | `π` 的凸集 | lower/upper prevision、robust Bayes、m-convex 决策 | 集合内元素的相容性；**可组合性不平凡** | 中-高 | **延后。** 见 §9.2 |
| **R5** | refinement 预序 `⊑` | `Info` 上的预序 + 集族 | 不可逆更新、单调算子、**单调函数泛函** | 不给「值」，只给「更少/更多信息」；不提供 readout | 低（形式层）/ 中（要真的重写所有算子） | **推荐作为骨架。** 唯一能给出 refinement consistency 保证的结构 |
| **R6** | typed-Unknown 代数 | 小有限格（K4 双序 / RCC 族） | 完整组合表、一致性判定、refinement 变窄、temporal 序 | 数值；需先决定 base relations | 低-中 | **推荐做 Unknown 传播层。** 代数选型留给 Architect |

### 2.2 关键点：R5 + R6 是骨架，R3 是存储，R2 是展示，R1 不推荐、R4 延后

这不是个人偏好，而是成本账：

- **R4 的成本是可证的**，不是估计的。Liell-Cock & Staton (2025, POPL) 明确：把 credal set 用「凸分布幂集」monad 做组合**并不 compositional**，因为该 monad 非交换；他们用 graded monad 修正后得到**更紧**的界（`CITED_PRIMARY`，DOI `10.1145/3704890`）。含义：**朴素的 credal 组合会系统性地给出过松的界，且松的程度依赖一个未被声明的独立性假设。** 这本身就是 `AGENTS.md:24` 同类违规。
- **R6 的成本也是可证的**。RCC8/IA 的经验：只用 base relations 时一致性判定可算，**允许 `2^B` 全部幂集时 NP-hard**；因此必须引入 **tractable subset**（如 `ORD-Horn`）才能保持可算（`CITED_PRIMARY`，Renz 2007；Renz/Dylla/Bhattacharya 相关工作）。
  → LHRM 的推论：**不能**对全部 construct family 同时启用完整不定关系。若要用，必须先声明 tractable subset。
- **R2 的成本几乎为零且收益明确**。而且有严格依据说明它能承载什么：Pelessoni & Vicig (2022) 证明，**Jensen / Markov / Cantelli 型界**在 imprecise 知识下仍然成立（在 `22`-coherence 下即可），因为"probability inequalities do not depend on the exact evaluations, hence are especially useful when its knowledge is vague or imprecise"（`CITED_PRIMARY`，arXiv:2211.01503）。
  → **这是本报告给出的最重要的正面结果：缺失后仍可算的是「有界量」，不是「点值」。** 见 §5.3。

### 2.3 三个序，不是三个置信度

Belnap 的四值逻辑给出了一个反直觉但可形式化的结果（`CITED_PRIMARY`，Mundhenk et al.；`CITED_SECONDARY`，Belnap 1977 官方摘要）：

- 取值 `{T, F, B, N}`：`T` = 已知真，`F` = 已知假，`B` = 已知既真又假，`N` = 无信息。
- **`B` 与 `N` 是两个「彼此不相关」的中间值**（原文 "two intermediate (but unrelated) values, namely unknown (n) and known-both-true-and-false (b)"）。
- 该结构上有**两个序**：
  - **knowledge order / approximation lattice**——信息单调性。原文："the presence of **two ordering relations** on it (the **truth order** and the **knowledge order**) has given rise to the interesting notion of **bilattice**"。
  - **truth order / logical lattice `L4`**——逻辑意义上的真值位置。
- Belnap 自己的评价（S14 官方摘要转述）："**The worst thing is to be told something is false simpliciter.** You are better off (it is one of your hopes) in either being told nothing about it, or being told both that it is true and also that it is false; while of course best of all is to being told that it is true."

**对 LHRM 的直接后果（`AI_RECOMMENDATION`）：**

> 状态侧必须**至少有两个序**：
> 1. **信息序**（`⊑`）：`N < B`？**不，N 与 B 在信息序上不可比。** 唯一单调方向是 `B → T`、`B → F`（知道了才收窄），`N → 任意`。
> 2. **时序 / 可寻址序**：`not_yet_real` 与 `structurally_unobservable` **不在** K4 里，需要另一个正交维度（trace / addressability）。

因此**单条 confidence 轴在类型上就是错的**，不是不够用。FM-03（N-03）给出了一个不需要任何数据就能判定该错误为真的反例。

### 2.4 成本小结

| | 便宜 | 昂贵 |
| --- | --- | --- |
| 数学 | Scott 域 + K4 + `2^B` 全是现成的 | 需要自创的部分 = 0 |
| 实现 | `⊥` 传播规则、单调有界 readout、`evidence_mass` 标量、REFUSE 一等输出 | 完整 credal store、maximin 稳健决策、端到端不确定性传播、per-coordinate epistemic POMDP |
| 决策 | **现在做**（§9.1） | **延后**（§9.2） |

---

## 3. Refinement consistency：数学上是否可能

### 3.1 答案：可能，而且是经典结果

**定义（`MODEL_HYPOTHESIS`，但数学本身是标准的）**

令 `Info` 为证据状态集合，定义

```
s ⊑ s′   ⟺   s 可由 s′ 遗忘得到（s′ 至少确定与 s 一样多）
```

这是**预序**（自反 + 传递），一般**非**反对称（两个不同表示可能编码同一信息量）。它成为**格**需要额外条件：闭包于 ∧（信息交）与最小上界（相对可合并性，`RelMergeability`）。

**Refinement consistency 的定义：**

```
T : Info → Info   满足   s ⊑ s′  ⟹  T(s) ⊑ T(s′)
```

即：加入证据后跑一次更新，得到的状态**不会**比「少证据时跑一次更新」更不确定。

**经典充分条件：`T` 为 Scott-continuous**（单调 + 保持定向上确界），定义域为一个 dcpo。Belnap 在构造 K4 时**明确采用了这一条件**（`CITED_SECONDARY`：他 "Referring to Dana Scott, he assumes the connectives are Scott-continuous or monotonic functions"）。

### 3.2 三条独立的定理级支撑

| 来源 | 支撑什么 | 强度 |
| --- | --- | --- |
| Dynamic epistemic logic（Baltag, van Ditmarsch & Moss 2008, Handbook of the Philosophy of Science, DOI `10.1016/B978-0-444-51726-5.50015-7`） | public announcement `!φ` **就是一个 refinement 算子**（把 `S5` 模型限制到满足 `φ` 的世界子集），有完整公理化 | `CITED_PRIMARY`（官方摘要页 + 章节片段）。**未逐条核实定理原文** |
| QSR / QCN（Renz 2007, IJCAI-07, `https://www.ijcai.org/Proceedings/07/Papers/083.pdf`） | 不定信息 = `2^B`；传播 = 单调收缩迭代 `r_{x,y} ← r_{x,y} ∩ r_{x,z} ∘ r_{z,y}`，**有限网络必然终止** | `CITED_PRIMARY` |
| De Morgan 格 / bilattice（Mundhenk et al.） | K4 有双序，Scott 连续性定义 approximation lattice | `CITED_PRIMARY` |

**QCN 那个单调迭代是最便宜的落地形态**，值得逐字记下：

> "we can enforce the 3-consistency by iterating the refinement operation `r_{x,y} ← r_{x,y} ∩ r_{x,z} ∘ r_{z,y}` … For finite constraint networks this algorithm always terminates since **the refinement operation is monotone** and there are only finitely many relations."

并且注意 closure 是**不等式**而非等式（`CITED_PRIMARY`，algebraic-properties 文献）：

```
φ(t) ∩ φ(r)∘φ(s)  ⊆  φ(r)∘φ(s)
```

即 **只会变窄，不会变宽**。这正是 refinement-monotone 的精确表述。

### 3.3 会破坏它的四类动作

`[MODEL_HYPOTHESIS]` + 项目内 provenance：

| 破坏 | 机制 | LHRM 内触发点 | 现有防线 |
| --- | --- | --- | --- |
| **(a) forgetting 非单调** | 丢证据反而增不确定（先平均再补插） | 早期 `SoftDistance = sqrt(Σ w_i·dev_i²)` 叠加 `Unknown → prior` 后对已知项做平均（`PROJECT_HISTORY:94-102`） | 弱，仅文字纪律 |
| **(b) 别名 / 合并不当** | 把**不可比**的信息状态映射到同一表示 | 把 `disputed` 与 `unmeasured` 合成一个 `Unknown`（§1 分类表） | **无** |
| **(c) 转移算子非确定** | 状态是点值但 `F` 随机 → 同 history 两次运行给出不同状态 | `X_(t+1) = F(X_t, Action_t, Event_t, Belief_t, Constraint_t, Environment_t)`（`CURRENT_ARCHITECTURE.md:203`）中 `F` 的随机性来源未指定 | 部分。`Gamma_(A,B) = { X_(A,B)(τ) }`（:236）把轨迹写成集合，已隐含承认 |
| **(d) 点投影回写** | `set → point` 不是单调可逆；回写后 refinement 不可恢复 | 「输出 78/100」型 readout 若被写回 `ModelState` | **仅文字禁令**（`PROJECT_HISTORY:116`） |

### 3.4 判定

> **Refinement consistency 对 LHRM 是可达的，但代价是：必须显式声明 `⊑`，必须把所有状态算子重写为 `⊑`-单态，且必须承认 QCN 式的可算性边界（需要 tractable subset）。**
>
> **它不会自动成立。** 项目现在**没有** `⊑` 这个概念（§0.1），所以目前既谈不上违反、也谈不上满足。

---

## 4. Unknown 的类型与组合传播

### 4.1 传播规则（`AI_RECOMMENDATION`，可检查）

设坐标 `k` 的状态在类型格 `T_k` 上取值，`T_k` 允许包含底元素 `⊥`。复合状态 `S = (v_1, …, v_n)`。

| 规则 | 内容 | 依据 | 可检查性 |
| --- | --- | --- | --- |
| **C1 吸收（meet）** | `v_k = ⊥` ⟹ `S` 在坐标 `k` 上为 `⊥`。**不得**输出点值 | Scott 域 | 直接 schema 约束 |
| **C2 宽度单调** | `width(composite) ≥ max_k width(component_k)` | QCN 单调收缩 | 属性测试 |
| **C3 有界函数合法、点函数不合法** | 若 `g` 是类型格上的**单调**泛函，则 `g` 在 `⊥` 状态上有良定义的**像集**；报告 `g ∈ g(K)`，**不**报告 `g = v` | Scott 连续性 | 单位测试 |
| **C4 tag 不吸收，取集合并** | 一个坐标可同时是 `private_to_partner` ∧ `not_yet_real` | §1 分类 | schema |
| **C5 逐坐标单调** | 更新坐标 `j` 不得 refinement / un-refine 坐标 `i`，除非存在**已登记**的结构依赖（`∂F_i/∂z_j ≠ 0`） | `CURRENT_ARCHITECTURE.md:209-226`（低冗余 ≠ 低动态耦合） | 属性测试 |
| **C6 REFUSE 可达** | 成本敏感读出下，动作集必须含 `REFUSE`，且当任何替代动作的条件风险超过登记阈值时 `REFUSE` 可达 | Franc et al. 2021 (JMLR)：三个 reject model **共享同一最优策略** = Bayes classifier + randomized Bayes selection function | 存在性测试 |

### 4.2 关于 C3 的具体例示（这是本报告最实用的一条）

设 `Trust(A→B)` 的可信值集合为 `[0.1, 0.6]`，`Dedication(A→B)` 未知。

| 报告 | 是否合法 | 理由 |
| --- | --- | --- |
| `Trust(A→B) = 0.35` | **合法**（作为 display 层 R2） | 区间的中点是一个**展示选择**，不是状态主张 |
| `Trust(A→B) ∈ [0.1, 0.6]` | **合法**，且是推荐的 | 状态本身就是集合 |
| `Trust(A→B) = 0.35`（`Dedication` 已写回状态） | **非法** | 违反 C3 + 破坏 refinement（d） |
| `coverage(i,j) ≥ 0.3`（`coverage` = 非 `⊥` 坐标比例） | **合法** | `coverage` 对「信息变多」单调，可给界 |
| `relationship_quality = 0.62` | **非法** | 点函数、非单调、且坐标含 `⊥` |
| `mutuality 存在 / 不存在 / Unknown` | **合法**（枚举 + `⊥`） | 派生量，类型显式 |

### 4.3 不可复合的部分：credal 宽度的乘积是错的

`[MODEL_HYPOTHESIS]`，依据 `CITED_PRIMARY`（Liell-Cock & Staton 2025）：

- 朴素做法：composite 的不确定性 = 各分量 credal 宽度的（某种）乘积。
- 该做法**系统性过松**，且松的程度依赖一个未被声明的**独立性假设**。
- 正确做法：先做 augmentation（credal 直积），并**明确声明**独立性假设；或只报告**有界量**（C3）。
- 报告纪律：**不宣称「composite 的 credal 宽度 = 分量宽度的乘积」**。

---

## 5. 可检验不变量

以下 15 条是**候选可检验不变量**。它们现在是命题，**不是**已验证的性质（§6 非主张 10）。

### 5.1 结构与传播类

| ID | 不变量 | 检查方式 | 预期反例 |
| --- | --- | --- | --- |
| **I1** | **Unknown 吸收**：`v_k = ⊥` ⟹ composite 在 `k` 上为 `⊥`；任何 readout 不得对 `k` 输出有限标量 | schema 约束 + 单元测试 | 平均/求和把 `⊥` 当 0 处理 |
| **I2** | **底元素上不做算术**：`f(⊥_T)` 不得是数；全函数必须返回 `⊥` 或显式标记值 | 属性测试：对每个 `T` 的每个算子 | `⊥ + 0 = ⊥` 被实现成 `0` |
| **I3** | **有界读出的像集报告**：任何对 `⊥` 状态成立的 readout 必须是 `g ∈ g(K)`，不得是 `g = v` | 输出 schema 检查 | 输出单值 |
| **I4** | **tag 闭包**：tag 取值是已登记的有限枚举；复合后 tag 只增不减（取集合并）；**新 tag 不得未经登记出现** | 枚举 diff（CI） | tag 数量随 case 数增长 → ontology 蠕变 |
| **I5** | **tag 不可跨角色泄漏**：`private_to_partner` 坐标不得被 S 侧的观测 refinement | 角色置换测试：交换 `S`/`O` 后 `private_to_partner` 应仍在 partner 侧 | S 侧报告把 J 侧的私域 Unknown「解决」了 |
| **I6** | **矛盾 ≠ 未知**：相反来源必须产出 `B`，且**与来源顺序无关** | 顺序置换测试：打乱来源顺序，`B` 不变 | 按顺序「后者覆盖前者」→ 变 `T` 或 `F` |
| **I7** | **聚合顺序无关**：composite 是证据**集合**的函数，不是摄入顺序的函数（lattice join 的交换律） | 打乱证据顺序重跑，比对 | 「最后一条说了算」 |
| **I8** | **重复证据幂等**：同一事实摄入两次，状态不变；同事实的第二来源应 **refine** 而非 **overwrite** | 幂等测试 | 第二来源覆盖第一来源 |
| **I9** | **逐坐标单调（C5）**：更新 `j` 不改变 `i`，除非有已登记的 `∂F_i/∂z_j ≠ 0` | 逐坐标消融测试 | 隐式耦合无处登记 |
| **I10** | **refinement 单调**：证据集 `E ⊆ E′` ⟹ 每个坐标的宽度 `width(post(E′)) ≤ width(post(E))` | 随机抽 `E ⊆ E′` 反复测 | 丢证据反而变宽（forgetting 非单调） |
| **I11** | **时间 refinement 单调**：`history_id` 的 DAG 中，refined 视图不得作为 refined 视图的 sibling 出现 | DAG 不变量检查 | 旧 lineage 被新证据改写 |
| **I12** | **readout 不回写**：`readout : State → Readout` 的像**不是**状态更新路径的输入 | 依赖图 / 静态检查 | 78/100 型结果被写回 `ModelState` |
| **I13** | **不可约性诚实**：对被标为 `structurally_unobservable` / `censored` 的坐标，「增加证据会确定它」**不得**作为默认承诺出现在任何输出里 | 字符串/模板审计 | 报告暗示「再问几个问题就能确定」 |
| **I14** | **prior 支配标记**：`evidence_mass < θ` 时禁止点 readout | 属性测试（生成合成稀疏状态） | 零观测坐标输出点值 |
| **I15** | **多峰不取均值**：坐标后验非单峰时，禁止输出点 readout | 在合成双峰后验上跑 readout | 报告双峰后验的均值（无指称） |

### 5.2 评测类（需要 held-out 数据，当前无法执行）

| ID | 不变量 | 检查方式 | 现状 |
| --- | --- | --- | --- |
| **I16** | **校准**：报告的置信度必须随留出集上的经验准确率单调；且校准曲线不得劣于常数先验基线 | reliability diagram + 严格 proper scoring rule 分解（Gneiting & Raftery 2007, JASA 102(477):359–378, DOI `10.1198/016214506000001437`，`CITED_METADATA`，**未读正文**） | **无 held-out Case Bank set，`UNKNOWN`** |
| **I17** | **coverage 显式**：每个 Case Bank item 必须报告非 `⊥` 坐标比例；coverage 低于登记阈值时不得作完备性主张 | 报告 schema | 未定义阈值（`UNKNOWN`） |
| **I18** | **REFUSE 可达性**：必须存在一个状态（`⊥` 覆盖率达某水平）使最优动作是 `REFUSE` | 存在性测试（依据 Franc et al. 2021 的选择函数） | 未实现 |
| **I19** | **confidence-尖锐度非任意**：报告置信度的分布尖锐度不得是自由参数；须随输入稀疏度变化 | 分布对比 | 尚无实现 |

### 5.3 哪些是「便宜且高价值」的

I1、I2、I3、I4、I6、I7、I12、I14、I15 —— 这 9 条**不需要任何新数学**，只需要 schema 约束、属性测试与输出纪律。**建议优先落这 9 条。**

I10、I11、I13 需要先有 `⊑` 的形式定义与一个已登记的依赖表。I16–I19 需要 held-out 数据。

### 5.4 一句可以直接引用的替代文本

`[AI_RECOMMENDATION]`（**不改 canonical，仅建议**）：

```text
Computable != Certain
```

建议扩为：

```text
Missingness removes point identification.
It preserves:  (a) non-trivial bounds;  (b) monotone partial functionals.
It does NOT preserve:  point readouts;  comparisons;  transition-law identification.
Unknown / Disputed / Not-addressable are legal terminal outputs, not failures.
```

支撑 `(a)` 的严格依据：Pelessoni & Vicig (2022)，arXiv:2211.01503 —— 概率不等式在 imprecise 知识下仍成立（`CITED_PRIMARY`）。
支撑后半段的依据见 §6。

---

## 6. 「缺失降低确定性但不影响可计算性」失效的具体模式

以下 8 条，每条给出**为什么该句在这一点上为假**、**证据**、**LHRM 内的具体触发场景**。

### FM-01 — 结构性空单元：不是小样本，是**永远没有样本**

`[ESTABLISHED]` 若缺失指示 `M` 是取值的确定函数（`M = 1 ⟺ X = 1`，例如「只对自报使用某 App 的人询问其使用行为」），则分层 `X = 1` 的观测**永远为空**。

- 这不是低数据，是**条件空单元**。加大 N 无用。
- Tennenholtz (2023, arXiv:2306.01157) 给出了这类不可约性的一个干净陈述：**delphic uncertainty "cannot be diminished, even in deterministic environments and infinite data"**（`CITED_PRIMARY`）。
- **`Unknown → prior` 在此仅在空洞意义上成立**：该分层的先验**就是**目标量本身，所以推断是循环的、vacuous 的。
- **LHRM 触发场景**：任何「只有在 X 已经发生时才被问到」的坐标。典型：性行为史（Kupek 1998 在**国家级性调查**中实证研究了 item nonresponse 的系统性决定因素，`CITED_METADATA`，**未读正文**）；「吵架次数」（只在吵架时才记录）；「是否已分手」（只在分手样本中采集）。

### FM-02 — 核心坐标本身 latent 且无 gold standard：点 readout 是**无指称**，不只是「不精确」

- `[ESTABLISHED]` Raykar et al. (2010, JMLR 11(43):1297–1322)：多标注者 + **无 gold standard** 时，联合估计真标签与标注者混淆矩阵存在 "chicken-and-egg problem"，真标签估计**只相对于一个测量模型**成立（`CITED_PRIMARY`，读到引言）。
- **对 LHRM**（`[MODEL_HYPOTHESIS]`，但类型上很硬）：`Trust(A→B)`、`Dedication(A→B)`、`SexualDesire(A→B)` **没有 gold standard**。可能的锚点只有：法院/官方裁定事实、强制性行为痕迹、已验证量表。**在叙事材料上三者皆无。**
- 后果：这些坐标的「后验」在形式上必须是**不可辨识的分布族**，报告点值不是精度不足，而是**指称缺失**。
- **这条目前不在任何 canonical 文档里，是本报告最重要的结构性发现。**

### FM-03 — `disputed` 与 `unmeasured` 不可比

- **反例（不需要任何数据即可判定）：**
  - Case A：两份来源对 `Trust(A→B)` 给出相反结论（法院文书 vs 私人聊天记录）→ 值 `B`。
  - Case B：无人报告过 `Trust(A→B)` → 值 `N`。
  - 任何把两者映射到同一 confidence 值的表示，都在做一次**不可比 → 可比**的压缩。该压缩**不是** refinement 映射。
- 依据：Belnap 1977（`B`/`N` 是 "two intermediate (but unrelated) values"）；Mundhenk et al.（双序、bilattice）（均 `CITED_PRIMARY`/`CITED_SECONDARY`）。
- **可作为 Case Bank 条目立即落地。**

### FM-04 — 填补会改变 estimand

- `[ESTABLISHED]` White & Carlin (2010, *Statistics in Medicine* 29:2920–2931, DOI `10.1002/sim.3944`)：当缺失独立于给定协变量的结果时，**complete-case 几乎无偏，而 multiple imputation 偏离零假设**；而在 MAR 下 complete-case 偏向零假设（`CITED_PRIMARY`，读到摘要）。
  原文：*"the choice of method should not be based on comparison of standard errors."*
- 补充：Seaman, Bartlett & White (2012, *BMC Med Res Methodol* 12:46, DOI `10.1186/1471-2288-12-46`)：MAR 下 JAV 可有偏，logistic 情形 "JAV's performance was **sometimes very poor**"（`CITED_PRIMARY`）。
- **后果**：「用先验补 Unknown」不是「加点噪声」，而是**改变估计目标**。可计算的东西取决于你静默采纳的机制假设。**这就是「影响可计算性」的直接反例。**
- **可用工具**：White & Carlin 提出 **FICO** = "the fraction of incomplete cases among the observed values of a covariate"——这是一个现成的、可直接实现为 LHRM `evidence_mass` 候选的指标（`[AI_RECOMMENDATION]`，但**本报告不推荐具体采用**，只指出它存在）。

### FM-05 — 最优动作可能是「不算」

- `[ESTABLISHED]` Franc, Prusa & Voracek (2021, JMLR 24:21-0048)：三个 reject model（cost-based / bounded-improvement / bounded-coverage）**共享同一最优策略** = Bayes classifier + **randomized Bayes selection function**（`CITED_PRIMARY`，读到摘要与 §2.4）。选择函数**不是**可选附件。
- **后果**：在成本敏感的读出下，稀疏 dyad 的正确输出常常是「状态未定，给出界」。主张「可计算性不受影响」等于否认「拒答」属于正确的输出类。
- **限制（自我约束）**：Salez et al. (NeurIPS 2021) 明确警告拒答可能成为不公平来源，且"**it should not serve as an excuse not to collect representative data**"（`CITED_PRIMARY`）。→ 「大量输出 Unknown」**不是**一个好的分数，必须同时报告 coverage 趋势（→ I17）。

### FM-06 — 快照 ≠ 轨迹：没有观测模型就没有动力学

- `[ESTABLISHED]` Rajaraman et al. (NeurIPS 2021, *Epistemic POMDPs*)："even in fully-observable domains, the agent's epistemic uncertainty renders the environment **implicitly partially observed** at test-time"；不显式处理它的方法"can be **arbitrarily sub-optimal** for test-time generalization in theory and in practice"（`CITED_PRIMARY`）。
- `[ESTABLISHED]` Tennenholtz et al. (NeurIPS 2021 DeepRL Workshop)：缺失协变量存在任意分布漂移时，模仿学习有 **possibility/impossibility 结果**（`CITED_PRIMARY`）。
- **对 LHRM**（`[MODEL_HYPOTHESIS]`）：`X_(t+1) = F(...)` 是一个**条件**陈述。**在稀疏事件序列上无法从一次快照区分「没变」与「变了但没被观测到」。** 这需要显式的观测模型（哪些事件会留下痕迹、哪些不会），而项目目前没有这个层。
- **诚实标注**：RL 设定到关系设定的迁移是**类比**。网络动力学里「homophily vs. contagion 需要观测过程才能区分」这一对应结论我**未核实**（Shalizi & Thomas 2011 未获取，见 §9），因此**不写入本报告**。

### FM-07 — 校准在稀疏输入下是**被定理强制的取舍**

- `[ESTABLISHED]` Kalai & Vempala (*arXiv:2311.14648*; STOC 2024, DOI `10.1145/3618260.3649777`)：对**真实性无法从训练数据判定的任意外部事实**，满足其语义校准条件的生成器**必须**以至少

  ```
  Hallucination rate  ≥  MF̂  −  Miscalibration  −  300·|Facts|/|Possible hallucinations|  −  7/√n
  ```

  的速率产生幻觉，**即使训练数据完美**。`MF̂` 是 Good–Turing **MonoFacts** 估计，即训练集中**恰好出现一次**的事实所占比例（`CITED_PRIMARY`，读到 abstract + v3 PDF 引言与 Cor 1）。

- **对 LHRM 的结构性后果**（`[MODEL_HYPOTHESIS]`，强度 `moderate`）：LHRM 的核心输出是 **per-dyad 的一次性事实**。这在结构上就是 **monofact**。因此：
  - 若 per-dyad 置信度**完全校准** ⟹ **必须有正比例的一部分是错的**；
  - 若它们**全对** ⟹ 置信度**系统性过度自信**。
  - **「稀疏输入 + 高置信」不是可修的 bug，而是必须被显式暴露的强制取舍。** 具体后果：报告置信度的**尖锐度不能是自由参数**（→ I19）。
- **限制**：该文证明的是 next-token 生成器 + monofact 事实分布。搬到 LHRM 是**类比 + 结构性论证**，不是定理的直接应用。

### FM-08 — 拒答 ≠ 无内部状态

- `[ESTABLISHED]` Krosnick, Presser & Tan（*The Impact of "No Opinion" Response Options on Data Quality*，`https://gspp.berkeley.edu/archived/files/research/pdf/Krosnick_et_al..pdf`，`CITED_PRIMARY`，**完整书目 `PARTIAL_BIB`**）：
  - 拒答主因是 **satisficing**（疲劳、题目靠后、低努力、低教育），不是真的「无意见」；Study 3 中「reported effort was **negatively** related to no-opinion reporting, suggesting that choosing a no opinion response option was more likely the result of **satisficing** than of optimizing」。
  - 给出 "don't know" 选项**减少**了事实题的实质回答数，但**未改变**重测信度（Foe et al. 1988，转引自该文）。
- **后果（对 `Unknown → prior` 的定点反例）**：对 tag = `refused`，**不得**用先验插补。正确类型是**比先验更宽的集合**，理由是应答过程本身不是 missing-at-random——先验反映的是「愿意回答的人」的分布，不是「这些人」或「那些人」的分布。

### FM-09（附加）— 方向性 invariant 的具体威胁：partial pooling 人为制造 mutuality

- `CURRENT_ARCHITECTURE.md:130-132` 要求 `SexualDesire(A→B) != SexualDesire(B→A)` 等三条。
- 若用**单一**人口超参数对 `Z[k,i,j,t]` 做向心收缩，`i→j` 与 `j→i` 共享同一收缩中心 → **非对称性被系统性地压向对称**。
- **这是本次审计发现的唯一一条「统计方法与 canonical 架构 invariant 直接冲突」的机制，项目中没有任何记载。**
- `[AI_RECOMMENDATION]` 若采用 partial pooling：对 `i→j` / `j→i` 使用**分离的超参数或分离的随机效应**（`(1,−1)` contrast 建模），并把「收缩导致的非对称衰减量」作为 readout 显式报告。

---

## 7. 稀疏 per-dyad 数据的 partial pooling 与不可辨识性

### 7.1 pooling 帮什么

`[ESTABLISHED]` 稀疏 N 下 factor loading 高度不稳定。Hirschfeld et al.（*J. Research in Personality*，`https://www.uni-muenster.de/OWMS/uploads/drafts_thielsch/pdf/Hirschfeld_et_al_2014_JRP.pdf`，`CITED_PRIMARY` 摘要；**完整作者表 / 卷页未核**）：

> "primary factor loadings are highly variable in smaller samples (n < 500) and **some primary loadings are not stable with 10,000 participants**. … **Most studies will not have adequate sample size** to yield stable loading patterns."

**这条对 LHRM 的含义比它看起来更重：加大 N **不能**修复**测量层**的稀疏。** 参数估计的方差与测量结构的稳定性是两个不同的问题。

### 7.2 pooling 不帮什么

`[ESTABLISHED]` Rajaraman et al. (2021)：即使观测完全可得，有限训练上下文也会让测试时环境变成**隐式部分可观测**；不显式处理的方法"can be **arbitrarily sub-optimal**"。

`[ESTABLISHED]` Tennenholtz (2023)：delphic uncertainty 在确定性环境 + 无限数据下**仍不下降**。

**推论**（`[MODEL_HYPOTHESIS]`）：

> **partial pooling 降低的是参数估计的方差，不是可辨识性。**
> 若某 dyad 落在一个人口先验覆盖不到的分层里，pooling 只会把错误**传播到更多 dyad**。
> 因此 partial pooling 必须 **按分层**做（relationship type × 阶段 × Environment），并且必须把「该 dyad 的 posterior 有多少由 pooling 决定」作为**一等输出**（即 `evidence_mass` / shrinkage 幅度）。

### 7.3 先验的质量在稀疏区恰好最差

`[ESTABLISHED]` Gu & Koenker (2015, *International Statistical Review*，`http://www.econ.uiuc.edu/~roger/research/ebayes/isrProbRob.pdf`，`CITED_PRIMARY`）：Robbins (1951) 的 compound decision 设定下，`n = 20` 时方法矩估计在 `p → 1/2` 附近有 "modest disadvantage"；换 beta prior 收缩后 "deliver better performance than the MoM procedure **while sacrificing some of their advantage when p is near 0 or 1**"。

`[ESTABLISHED]` 另经转述（Berger 1985, *Statistical Decision Theory*，转引自 *Robustifying Empirical Bayes*，`PARTIAL_BIB`）：

> "A natural objection to many empirical Bayes procedures is that they place **unjustified reliance on an initial prior**. While such procedures may still perform well with respect to ensemble risk, they may also **fail spectacularly for some subpopulations or individuals**."
>
> Berger (1985): "it is very difficult to determine such δ\*; furthermore, this 'optimal' δ\* is **usually extremely messy and difficult to work with**."

**这条的含义**：稀疏区的先验既无数据约束、又在数学上难处理。**「Unknown → prior」在稀疏区的收益与代价都集中在这里**——不是一个可以靠调参解决的问题，而是**设计选择**。

---

## 8. 稳健读出与稳健决策

### 8.1 现在就能用的：有界量

`[ESTABLISHED]` Pelessoni & Vicig (2022)：Markov / Cantelli / Jensen 型界在 imprecise 知识下仍成立（`22`-coherence 即可），因为这些不等式**不依赖精确评估**。

**因此，以下 readout 在 `⊥` 状态上合法且有严格依据：**

```text
coverage(i,j)                  = fraction of coordinates with value ≠ ⊥
width_k                        = upper_k − lower_k
P(X ≥ c) ≥ 1 − μ/c             若只有 [μ, ·] 与上界信息
count_k(tag) ≥ / ≤             某 tag 的坐标数
lower / upper of any monotone g
```

### 8.2 延后的：credal 决策

`[ESTABLISHED]` 成本依据：

- credal set 作为**存储层**会引入**可组合性**问题，且朴素组合**系统性地过松**（Liell-Cock & Staton 2025, POPL, DOI `10.1145/3704890`）。
- credal network 是 Bayesian network 的**严格推广**（Antonucci, de Campos & Zaffalon 2014, in Augustin et al. (eds.), *An Introduction to Imprecise Probabilities*, Wiley, ISBN `0470973811`；`CITED_PRIMARY`，读到章节 PDF）——推广意味着**更贵**，且该章自己列出 "some important challenges and open problems"。

**结论**：credal 决策（maximin / m-convex / 后悔）作为**默认**读出是过度设计。它应在**一个明确场景**下才启用——见 §9.2。

### 8.3 拒答的合法性与限度

见 FM-05 与 N-06。`REFUSE` 是一等输出（I6 / I18），但 Salez et al. 的警告必须同时写进报告规范。

---

## 9. 建议

### 9.1 最小可行处理（现在做）

按「成本 / 收益」排序。全部不需要 LHRM 自创数学。

| # | 动作 | 成本 | 收益 | 对应不变量 |
| --- | --- | --- | --- | --- |
| **1** | 引入 `⊥` 作为每个坐标类型的底元素，**禁止对 `⊥` 做算术**（返回 `⊥` 或显式标记，不返回数） | 极低 | 消除 `AGENTS.md:24` 的最隐蔽违规形式 | I1, I2 |
| **2** | 引入 `evidence_mass` 标量（先验主导程度）作为**一等输出**；`evidence_mass < θ` 时禁止点 readout。度量与阈值留给 Architect | 低 | 让「`Unknown → prior`」的后果**可见** | I14, I17 |
| **3** | 引入 §1 的 **tag 分类**（10 值），tag 复合取**集合并**。**不**引入代数语义（只做类型排除） | 低 | 让 8 个失效模式可被区分 | I4, I5 |
| **4** | 采用 C1–C6 六条传播规则作为**实现约束** | 低 | 让 composite 的类型有定义 | I1, I3, I6, I7, I9 |
| **5** | 引入 **refinement 单调性**作为 readout 层的必要条件：**`readout` 的像不是状态更新路径的输入**（readout 不回写） | 极低 | 把 `PROJECT_HISTORY:116` 的文字禁令变成可检查条件 | I10, I11, I12 |
| **6** | 多峰后验**禁止取均值** readout | 低 | 消除「无指称点值」 | I15 |
| **7** | 引入 `REFUSE` / `Not-addressable` 作为**一等终态输出**，与 `Unknown` 区分 | 低 | 让「不算」成为合法答案 | I18 |
| **8** | 报告 coverage 数字（每个 Case Bank item） | 极低 | 防止「大量 Unknown」被当成质量 | I17 |
| **9** | 声明 `⊑`（信息序）为一个显式概念，并登记逐坐标依赖表 | 中 | 为 I10/I11 提供前提 | I9, I10, I11 |
| **10** | 若采用 partial pooling：分离 `i→j` / `j→i` 的超参数或随机效应 | 低 | 保护方向性 invariant | I9（结构层） |
| **11** | 优先落 9 条**可立即检查**的不变量（I1–I4, I6, I7, I12, I14, I15） | 低 | 无需 held-out 数据 | — |
| **12** | 把 §5.4 的替代文本提交 Architect 审阅（**本报告不改 canonical**） | 极低 | 修正一条过强表述 | — |

### 9.2 应该延后

| # | 项目 | 为什么延后 | 触发升级的条件 |
| --- | --- | --- | --- |
| **D1** | credal set 作为默认存储层 | 组合不平凡（Liell-Cock & Staton 2025）；朴素组合系统性过松 | 出现一类 tag，其**先验**已知是多峰且机制不可辨识（典型：FM-01 的结构性空单元） |
| **D2** | maximin / m-convex / 后悔稳健决策 | 需要先有成本函数；没有决策场景就无对象 | 出现明确的成本敏感 readout 场景 |
| **D3** | 端到端不确定性传播（transition 层的 epistemic 状态） | 属于 R06 / R09 lane 的 territory；本 lane 不越界 | R06 交付 transition law 家族后 |
| **D4** | 完整 QSR 代数（RCC8/IA/STPA×/RCC9） | 需先决定 base relations；且全幂集 NP-hard，必须先定 tractable subset | 需要对 construct family 做**关系型**（而非数值型）推理时 |
| **D5** | per-coordinate epistemic POMDP 建模 | Rajaraman et al. 的框架是 RL 专用；迁移到关系状态未验证 | LHRM 引入可学习的 action policy 后 |
| **D6** | 与 K4 竞争的代数选型（`B` 是否需要细分为 `B_priv` / `B_public`） | 无明确需求 | 出现「私域矛盾 vs 公共矛盾」需要区分的 Case |
| **D7** | 校准指标（Brier / 严格 proper scoring rule）落地 | 需要 held-out Case Bank set，当前不存在 | Case Bank 达到可留出规模后 |

### 9.3 一个具体的 canonical 形状（候选，非提议修改）

```text
CoordinateValue(k, i, j, t) =
    Known { value, kind, provenance, reporter_role, history_id }
  | Unknown {
        tag ∈ { no_evidence, refused, private_to_partner, withheld_by_actor,
                disputed, censored, structurally_unobservable,
                not_yet_real, superseded, unmeasured_by_instrument },
        prior_set,          # tag 蕴含机制多重性时是集合，否则是单分布
        evidence_mass,      # 先验主导程度；一等输出
        value_class,        # 无信息 / 真且假 / 未来未定义 / 不可寻址 —— 互不同类
        provenance
    }
```

与现有架构的对应关系：

- `value_class` 承载 F-01 的双序；它与 `tag` **正交**（一个坐标可以同时是 `private_to_partner` 与 `not_yet_real`）。
- `reporter_role` 承载 FM-08 的方向性要求：`PairState_(i,j)` **必须**按 reporter 索引，或**显式声明**为 reporter-invariant——而 Swann et al. (1994) 的证据表明它**不是** reporter-invariant。
- `history_id` 复用 `CURRENT_ARCHITECTURE.md:241` 已有的 `tau = (history_id, local_time)`。
- **这个形状不新增任何人类关系构念**，只新增**证据侧的类型**。这是它符合 `AGENTS.md`「few stable constructs」纪律的原因。

### 9.4 状态建议

见 §11。

---

## 10. 明确非主张（Explicit non-claims）

1. **不主张** LHRM 现有 canonical 文档有任何错误。§0.1 的 grep 结果只说明**形式化内容缺失**，不是**内容错误**。缺失 ≠ 缺陷。
2. **不主张** 项目实际持有的 `Computable != Certain` 为假。它成立。§6 的反例针对的是 mission 的**强版本**。
3. **不主张** 任何 LHRM 坐标的先验、任何缺失机制在关系数据中的**具体分布**、任何 attrition 率。S19 / S20 只支撑「该问题存在且被领域当作问题处理」。
4. **不主张** Kalai–Vempala 定理**直接**适用于 LHRM（见 FM-07 的限制说明）。
5. **不主张** credal set / imprecise probability 是 LHRM 的「正确答案」。§9.2 明确列为延后项。
6. **不主张** K4 / RCC8 / IA / STPA× 中任一个是 LHRM 应选的具体代数。§9.3 给的是**形状**。
7. **不主张** 任何具体数值：阈值 `θ`、credal 集合大小、可接受 coverage 下限、refinement 收敛判据。
8. **不主张** Belnap 关于「被告知为假最糟」的话是 LHRM 的决策规则建议。那是对**信息论意义上被告知为假**的评价。
9. **不主张** 拒答 / `REFUSE` 应成为 LHRM 的默认输出。Salez et al. 明确警告了其公平性代价。
10. **不主张** 本报告的任何一个不变量已被验证。它们是**可检验的候选**，目前无实现可检验。
11. **不主张** 网络动力学里「homophily vs. contagion 需要观测过程才能区分」这一对应结论（Shalizi & Thomas 2011 **未获取**，见 §11）。
12. **不主张** 我读过任何 LHRM issue `#20`/`#21`/`#22`、Eye、Juece、PR31 的内容。**未读取、未执行、未引用。**

---

## 11. 剩余未知与本次未做到的事

1. **LHRM 自己的 prior 来源未定义。** `Unknown -> prior` 在 `PROJECT_HISTORY:102` 被提出，但 `docs/foundation/*` 中没有任何一处说明 prior 是什么、按什么分层、如何做 prior-sensitivity。`UNKNOWN_AS_OF_2026-09-27`。
2. **`evidence_mass` 的度量与阈值未冻结。** FICO（White & Carlin 2010）、posterior/prior KL、variance ratio、shrinkage 幅度都是候选。**本报告不推荐具体采用任何一个。**
3. **哪些坐标在结构上不可观测，从未被枚举。** 需要 Architect 逐构念族判定。这是**人类/架构决定**，不是研究问题。
4. **LHRM 稀疏输入下的实际 calibration 未知。** 无 held-out Case Bank set，未报告过 reliability diagram。`UNKNOWN`。
5. **只核到元数据的来源**（未读正文，因此本报告只使用其标题/存在性可支撑的定性表述）：Miller & Wright (1995, JMF 57(4):921, DOI `10.2307/353412`)；Kupek (1998, Arch Sex Behav 27(6):581–594, DOI `10.1023/A:1018721100903`)；Gneiting & Raftery (2007, JASA 102(477):359–378)；Bergemann & Morris (2016, AER 106(5):586–591, DOI `10.1257/aer.p20161046`)。
6. **检索失败导致的缺口**（`websearch` 多次返回 HTTP 429 / 限流）：
   - couples / relationship longitudinal attrition 的**定量**文献（Lavner & Karney 2010 类型的 RDD 选择论证、Couple Study 的 attrition 描述）**未核实**。
   - **STPA× 的 13 元代数未核实**（第一次查询被 429 打断且未重试成功）。因此本报告**只使用 RCC8 / IA / RCC9 这一族已核实的 QSTR 结论**，不引用 STPA× 的具体性质。
   - **Dynamic epistemic logic 第 5.1 节的定理原文未逐条核实**。本报告只说「public announcement 是一个 refinement 算子且有完整公理化」这一层，不引用具体公式。
   - **Shalizi & Thomas (2011) 未获取**，故 §6 FM-06 不使用 homophily/contagion 对应。
7. **K4 是否足以表达 LHRM 需要的全部 `Unknown` 种类未验证。** K4 只有一个 `n`，而 §1 的分类至少需要 epistemic / temporal / structural / conflict 四个正交维度。**可能需要 K4 的扩张。选型未做。**
8. **C1–C6 对全部 construct family 是否封闭，未检验。**
9. **`F` 是否已被要求为随机/确定，未定义。** `CURRENT_ARCHITECTURE.md:203` 写作 `F(...)` 未指明。§3.3(c) 因此只能是风险提示，不能是缺陷认定。

---

## 12. 参考文献

> 标注约定：`[PRIMARY]` 读到原文或官方摘要全文；`[ABSTRACT]` 读到官方摘要；`[METADATA]` 只核到 DOI 元数据；`[SECONDARY]` 转述页；`[PARTIAL_BIB]` 正文读到但书目不完整；`[UNVERIFIED]` 本次未核。

1. `[ABSTRACT]` Kalai, A. T., & Vempala, S. S. (2023; v3 2024-03). *Calibrated Language Models Must Hallucinate.* arXiv:2311.14648. STOC 2024. DOI `10.1145/3618260.3649777`. — FM-07；quote: "Hallucination rate ≥ MF̂ − Miscalibration − 300|Facts|/|Possible hallucinations| − 7/√n"。
2. `[PRIMARY]` Raykar, V. C., Yu, S., Zhao, L. H., Valadez, G. H., Florin, C., Bogoni, L., & Moy, L. (2010). *Learning From Crowds.* Journal of Machine Learning Research, 11(43), 1297–1322. `https://jmlr.org/papers/v11/raykar10a.html` — FM-02。
3. `[ABSTRACT]` Swann, W. B. Jr., De La Ronde, C., & Hixon, J. G. (1994). *Authenticity and positivity strivings in marriage and courtship.* JPSP, 66(5), 857–869. DOI `10.1037/0022-3514.66.5.857`. PMID 8014831. — FM-08 / §9.3。
4. `[PARTIAL_BIB]` Krosnick, J. A., Presser, S., & Tan, P. *The Impact of "No Opinion" Response Options on Data Quality: Distinguishing satisficing from optimizing in the survey interview.* `https://gspp.berkeley.edu/archived/files/research/pdf/Krosnick_et_al..pdf`（完整出版信息未核） — FM-08。
5. `[PRIMARY]` Franc, V., Prusa, D., & Voracek, V. (2021). *Optimal Strategies for Reject Option Classifiers.* JMLR, 24, 21-0048. `https://jmlr.org/papers/volume24/21-0048/21-0048.pdf` — FM-05, C6, I18。
6. `[PRIMARY]` Rajaraman, D., Han, T., Yang, P., Ramchandran, K., Van Dyke, D., Peng, X., & Levine, S. (2021). *Why Generalization in RL is Difficult: Epistemic POMDPs and Implicit Partial Observability.* NeurIPS 2021. — FM-06, §7.2。
7. `[PRIMARY]` Tennenholtz, G. (2023). *Delphic Offline Reinforcement Learning under Nonidentifiable Hidden Confounding.* arXiv:2306.01157. — FM-01, N-04。
8. `[ABSTRACT]` Tennenholtz, G., Hallak, A., Dalal, G., Mannor, S., Chechik, G., & Shalit, U. (2021). *Covariate Shift of Latent Confounders in Imitation and Reinforcement Learning.* NeurIPS 2021 Workshops (DeepRL). — FM-06。
9. `[ABSTRACT]` Baltag, A., van Ditmarsch, H. P., & Moss, L. S. (2008). *Epistemic Logic and Information Update.* Handbook of the Philosophy of Science, 8, 361–455. DOI `10.1016/B978-0-444-51726-5.50015-7`. — §3.2。
10. `[PRIMARY]` Liell-Cock, J., & Staton, S. (2025). *Compositional Imprecise Probability: A Solution from Graded Monads and Markov Categories.* Proc. ACM Program. Lang. 9 (POPL), Article 54. DOI `10.1145/3704890`. — §2.2, §4.3, D1。
11. `[SECONDARY]` Augustin, T., Coolen, F. P. A., de Cooman, G., & Troffaes, M. C. M. (Eds.) (2014). *An Introduction to Imprecise Probabilities.* Wiley. ISBN `0470973811`.
12. `[PRIMARY]` Antonucci, A., de Campos, C. P., & Zaffalon, M. (2014). *Probabilistic graphical models.* Ch. in [11]. `https://people.idsia.ch/~zaffalon/papers/2014itip-pgm.pdf` — §8.2。
13. `[PRIMARY]` Pelessoni, R., & Vicig, P. (2022). *Jensen's and Cantelli's Inequalities with Imprecise Previsions.* arXiv:2211.01503. — §2.2, §5.3, §8.1。
14. `[SECONDARY]` Belnap, N. D. (1977). *A useful four-valued logic.* In J. M. Dunn & G. Epstein (Eds.), *Modern Uses of Multiple-Valued Logic.* D. Reidel. — §2.3, FM-03, FM-08。
15. `[PRIMARY]` Mundhenk, J., Rautmann, S., & Schnoor, A. (n.d.). *Belnap's Four-Valued Logic and De Morgan Lattices.* `https://users.fmi.uni-jena.de/~mundhenk/Webseite/FDE/BelnapIGPL.pdf` — §2.3, FM-03。quote: "the presence of two ordering relations on it (the truth order and the knowledge order) has given rise to the interesting notion of bilattice"。
16. `[UNVERIFIED]` Belnap, N. D. (1976). *On a partial truth functional.* Inquiry 19(4), 490–499. DOI `10.2307/2265159`. — 背景提及，未用于任何主张。
17. `[PRIMARY]` White, I. R., & Carlin, J. B. (2010). *Bias and efficiency of multiple imputation compared with complete-case analysis for missing covariate values.* Statistics in Medicine, 29, 2920–2931. DOI `10.1002/sim.3944`. — FM-04。
18. `[PRIMARY]` Seaman, S. R., Bartlett, J. W., & White, I. R. (2012). *Multiple imputation of missing covariates with non-linear effects and interactions.* BMC Medical Research Methodology, 12, 46. DOI `10.1186/1471-2288-12-46`. — FM-04。
19. `[METADATA]` Miller, R. B., & Wright, D. W. (1995). *Detecting and Correcting Attrition Bias in Longitudinal Family Research.* Journal of Marriage and the Family, 57(4), 921. DOI `10.2307/353412`. — §1 分类表（`refused` / attrition 行）。
20. `[METADATA]` Kupek, E. (1998). *Determinants of Item Nonresponse in a Large National Sex Survey.* Archives of Sexual Behavior, 27(6), 581–594. DOI `10.1023/A:1018721100903`. — FM-01。
21. `[METADATA]` Gneiting, T., & Raftery, A. E. (2007). *Strictly Proper Scoring Rules, Prediction, and Estimation.* JASA, 102(477), 359–378. DOI `10.1198/016214506000001437`. — I16。
22. `[SECONDARY]` Walley, P. (1991). *Statistical Reasoning with Imprecise Probabilities.* Chapman & Hall. ISBN `978-0-412-28660-5`. — 术语出处。quote（转述）："precision is often mistaken for accuracy, whereas an imprecise representation may be more accurate than a spuriously precise representation"。
23. `[PRIMARY]` Renz, J. (2007). *Qualitative Spatial and Temporal Reasoning.* IJCAI-07, 519–526. `https://www.ijcai.org/Proceedings/07/Papers/083.pdf` — §3.2。
24. `[PRIMARY]` Dylla, M., Botea, D., & Renz, J. (2013). *Algebraic Properties of Qualitative Spatio-Temporal Calculi.* arXiv:1305.7345. + Bhattacharya, M., & Renz, J. (2023). *Decomposition and tractability in qualitative spatial and temporal reasoning.* EPFL LIA. — §2.2, §3.2。
25. `[PRIMARY]` Hirschfeld, …, Thielsch, M. T., et al. (2014). *Selecting items for Big Five questionnaires: At what sample size do factor loadings stabilize?* J. Research in Personality.（完整作者表 / 卷页未核） — §7.1。
26. `[PARTIAL_BIB]` *Robustifying Empirical Bayes.* arXiv preprint. `https://arxiv.org/html/2603.00704v2`（arXiv id 与日期异常，需复核；正文已读，含对 Berger 1985 的引文） — §7.3。
27. `[PRIMARY]` Gu, J., & Koenker, R. (2015). *On a Problem of Robbins.* International Statistical Review. `http://www.econ.uiuc.edu/~roger/research/ebayes/isrProbRob.pdf` — §7.3。
28. `[PRIMARY]` Salicz, T., et al. (2021). *Towards optimally abstaining from prediction with OOD test examples.* NeurIPS 2021. `https://proceedings.neurips.cc/paper_files/paper/2021/file/6a26c75d6a576c94654bfc4dda548c72-Paper.pdf` — FM-05, N-06。
29. `[METADATA]` Bergemann, D., & Morris, S. (2016). *Information Design, Bayesian Persuasion, and Bayes Correlated Equilibrium.* AER, 106(5), 586–591. DOI `10.1257/aer.p20161046`. — §2.2 延伸阅读（仅定性）。

### 12.1 项目内 provenance（本 lane 只读，未修改任何文件）

```text
AGENTS.md:24                       缺失不得静默压成 neutral / 完美匹配
AGENTS.md:26-27                    高层标签不作 primitive；低冗余 ≠ 零相关/动态独立
AGENTS.md:37                       坐标可为 interval / ordinal / category / constraint /
                                    probability distribution / Unknown /
                                    estimate+uncertainty+evidence
AGENTS.md:26, 35-38                representation-first invariant
docs/foundation/CURRENT_ARCHITECTURE.md:18          第一目标含「保留 Unknown 与不确定性」
docs/foundation/CURRENT_ARCHITECTURE.md:104-134     方向性 invariant（三条 != 断言）
docs/foundation/CURRENT_ARCHITECTURE.md:203         X_(t+1) = F(...)（F 的随机性未指明）
docs/foundation/CURRENT_ARCHITECTURE.md:236         Gamma_(A,B) = { X_(A,B)(tau) }（集合形式）
docs/foundation/CURRENT_ARCHITECTURE.md:241         tau = (history_id, local_time)
docs/foundation/CURRENT_ARCHITECTURE.md:284         混合状态空间中类型可共存（**无组合规则**）
docs/foundation/CURRENT_ARCHITECTURE.md:315         adjudicated|admitted|alleged|disputed|unknown
docs/foundation/STAGE_SUMMARY_2026-09-07.md:145-147  稀疏输入须允许；不得为公式完整而压平
docs/foundation/STAGE_SUMMARY_2026-09-07.md:162      Computable != Certain
docs/foundation/PROJECT_HISTORY_2026-09-10.md:74     Unknown 不能当成 0 或完美匹配
docs/foundation/PROJECT_HISTORY_2026-09-10.md:94-108 SoftDistance / hard vs soft / Unknown -> prior
docs/foundation/PROJECT_HISTORY_2026-09-10.md:115-116 稀疏输入须 graceful degradation；不得伪造 78/100
```

---

## 13. 建议状态与后续

**建议状态：`SUCCESS`（含 1 条 `NEGATIVE_RESULT` 子项）。**

理由：

- 5 项交付物全部完成，且每条主张都有可核指针或明确标 `MODEL_HYPOTHESIS`。
- 发现了 3 条项目内**没有记载**的结构性问题：
  1. **`Unknown` 缺少类型学**（`disputed` 与 `unmeasured` 不可比）——含一个**不需要数据即可判定**的 Case Bank 反例；
  2. **核心坐标 latent 且无 gold standard** ⟹ 点 readout 无指称（FM-02）；
  3. **partial pooling 与方向性 invariant 冲突**（FM-09）。
- 给出 19 条可检验不变量，其中 9 条**现在就能检查**。
- `NEGATIVE_RESULT` 子项：mission 的第二条主张**字面形式在项目内不存在**；项目实际持有的弱版本成立。因此 **§1.2 的 claim-attribution correction 必须进入 A02**。

**建议的后续工作（不属于本 lane）：**

1. **A02** 处理 §1.2 的 claim-attribution correction。
2. **R05** 处理 §9.1 #9（`⊑` 的形式定义 + 逐坐标依赖登记），与 R06 的 transition law 对接。
3. **R13** 处理 §9.1 #7（`REFUSE` 作为一等输出）在 LLM Skill 层的行为。
4. **R15** 把 FM-03 的 Case Bank 反例（「`disputed` vs `unmeasured` 不可比」）作为 representation test 条目收录。
5. **R16** 在 Case Bank 达到可留出规模后，执行 I16（校准）。
