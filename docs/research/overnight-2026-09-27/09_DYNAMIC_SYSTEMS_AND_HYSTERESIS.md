# 09 动力学、路径依赖、迟滞，与「不用状态机」问题

**Status:** `RESEARCH_CANDIDATE` / NOT CANONICAL
**Lane:** R09（Wave 1）
**Date:** 2026-09-27
**Scope:** 关系状态演化的数学框架比较；动力学可识别性；迟滞的存在性；粗关系标签的层次定位；对项目 rule 9 的反向审计
**Authority:** 本文件不修改任何 canonical doc。所有对 `AGENTS.md` / `docs/foundation/*` 的建议均为候选提案，需 Human/Architect 审阅。

---

## 0. 阅读约定与本文件的立场

**本文件的目的是找反例，不是找支持。** 本文件被要求把「项目当前立场可能过度陈述或对 reviewer 构成风险」作为一等交付物。因此：

- 每一节都成对给出「支持项目方向」与「反对项目方向」的证据，**反对一侧不得被压缩**。
- 所有非经验性的推理都标 `AI_DERIVED_CHARACTERIZATION`（我方推论，不是实证主张）。
- 证据分级：`CITED_PRIMARY`（本 lane 实际读到一手文本/原始摘要/官方文档页）、`CITED_SECONDARY`（转述）、`CITED_PARTIAL`（只读到摘要或片段）、`AGENT_RECALL`（先验，未核实）、`FETCH_FAILED`、`UNVERIFIED_POINTER`。
- 结论强度不得超过证据强度。凡标 `CITED_SECONDARY` 或 `AGENT_RECALL` 者，只用于举例或线索，不用于判定。

**被审计的项目立场**（`youling/lhrm@AGENTS.md`「Current architecture direction」第 9 条）：

> 核心关系演化 does **not** use a pre-enumerated relationship state machine as the engine; it is modeled as state transition over continuous/mixed state.

以及 `docs/foundation/CURRENT_ARCHITECTURE.md` §6 的形式化：

```text
X_(t+1) = F(X_t, Action_t, Event_t, Belief_t, Constraint_t, Environment_t)
```

**结论提要（先给结论）**：

1. 项目当前立场在**表示层**站得住，并得到本 lane 找到的最强非线性关系证据的**间接支持**（§3.1）。
2. 项目当前立场在**措辞层**有八处会被 reviewer 合理攻击（§7）。
3. 在**动力学层**，项目当前**没有任何可识别的结构**。这不是保守估计，是逐条清点的结果（§4）。
4. 迟滞在真实二元关系数据上的存在性**目前未知**；本 lane 未找到任何演示（§5）。这是 `NEGATIVE_RESULT`。
5. **应该有离散层，而且应该不止一层**，但任何一层都不应是 `F` 的引擎。本报告给出四个具体位置（§9）。

---

## 1. 术语与记号

记号沿用 `CURRENT_ARCHITECTURE.md`：

```text
X_(A,B)(tau)             dyad (A,B) 在历史坐标 tau 上的状态
Z[k, i, j, t]            有向关系状态：构念族 k、主体 i、对象 j、时间 t
Gamma_(A,B) = { X_(A,B)(tau) }    状态轨迹
Reality / Observation / Belief    三层分离
tau = (history_id, local_time)
```

本文件新增的记号（**仅用于本文件讨论，不建议在未审阅前写入 canonical**）：

```text
u                    控制量（外生/可操纵的投入；例：外部压力、替代选项质量、投入规模）
y                    读出（例：满意度、自报关系质量）
S(t) in R^d          连续状态向量
S_1 ... S_m          有序的粗粒化分区（S_i 与 S_(i+1) 的边界即为读出阈值）
s_1 ... s_K          离散状态（label / regime / latent class）
A : s_1..s_K -> s_1..s_K    离散转移核
Phi_j : R^d -> s_j   坐标 j 的读出映射
```

「阈值」的两种不同含义，本文件严格区分：

```text
(Threshold-1)  读出阈值      Phi 在 S 的某个水平上改变分类 -> 存在于 Phi 中，存在于观测中
(Threshold-2)  动力学阈值    控制量 u 越过某值后系统跳到不同吸引域 -> 存在于 F 中
```

**本文件的主要负面结论之一是：现有关系科学中被较好估计的是 (Threshold-1)，而项目若要主张 (Threshold-2)，必须提供目前尚不存在的一类证据。**

---

## 2. 框架比较表

十个框架。列的含义：

- **表示**：隐状态空间是什么
- **关键假设**：如果它错了会发生什么
- **使什么可观测**：在这个框架下研究者能看见、而看不见的东西
- **可识别性**：给定稀疏数据，参数在原则上能否被唯一确定
- **数据要求**：现实中最少需要什么
- **典型失效模式**：文献中反复出现的错误
- **真实二元数据证据基础**：本 lane 核实到的程度

### F1 预枚举关系状态机（FSM）

| 维度 | 内容 |
|---|---|
| 表示 | 离散标签集 `{friend, partner, married, ex}` + 手写转移表 |
| 关键假设 | 关系在这些标签之间跳；标签穷尽了相关状态 |
| 使什么可观测 | 一次性可枚举的**转移矩阵**；可数事件计数 |
| 可识别性 | 状态数**先验给定**故形式上可识别，但**语义**不识别：无法检验这个划分是否正确 |
| 数据要求 | 分类观测，最好密集 |
| 典型失效模式 | 状态集由文化先验而非数据决定；边界个案无处安放；把连续量粗暴截断 |
| 真实证据基础 | **无**（本 lane 未找到把 friend/partner/married/ex 当 FSM 并做转移估计的同行评审研究） |

### F2 关系标签上的 HMM / 潜状态分析

| 维度 | 内容 |
|---|---|
| 表示 | 离散潜在 class + 发射分布 + 转移矩阵 |
| 关键假设 | class 数量有限；给定 class 后观测条件独立 |
| 使什么可观测 | 潜在 regime 的**序列**（谁在何时处于哪种状态） |
| 可识别性 | **严重受损**：`Pohle et al. (2017)` 称之为「臭名昭著的阶数选择问题」；异常值/季节性/个体异质性被额外状态吸收，AIC/BIC **系统性高估**真实状态数；「不可能存在一刀切判据」 |
| 数据要求 | 相对密集的分类或序数序列 |
| 典型失效模式 | 状态数随数据走；状态标签换位（label switching）；状态无解释 |
| 真实证据基础 | **弱**。存在成熟的离散二元方法线（`Böllenrücher et al. 2023, 2024`，L-APIM + Markov chain，A1/B1 限制下 LRT 身份检验，显式拒收缺失），但它面向**短程分类互动序列**，不面向年尺度关系状态 |

### F3 regime-switching 状态空间（连续观测 + 离散 regime）

| 维度 | 内容 |
|---|---|
| 表示 | `y_t` 连续，`s_t in {1..K}` 离散，`y_t ~ N(mu_{s_t}, Sigma_{s_t})`，`s_t` 按 Markov 转移 |
| 关键假设 | 观测分布族被正确指定；给定 regime 后观测独立同分布 |
| 使什么可观测 | 连续读数上的**局部水平** + 隐 regime 切换 |
| 可识别性 | 与 F2 同病；额外需要 `K` 与每个 regime 的 `mu/Sigma` 都可估 |
| 数据要求 | 每 regime 需足够多的观测点 |
| 典型失效模式 | `Pohle et al. (2017)` 的结论完全适用 |
| 真实证据基础 | **无**（在关系数据上未找到成功的 K>1 估计） |

### F4 连续动力系统（耦合振子 / HKB / extended HKB）

| 维度 | 内容 |
|---|---|
| 表示 | `dx_i/dt = f_i(x_i, x_j, ...)`；常见 `extended HKB`：`dphi/dt = -a*phi - b*sin(2*phi) - d*omega` |
| 关键假设 | 存在**跨尺度有效**的集体变量与耦合强度参数 |
| 使什么可观测 | 相对相位 `phi`；多稳态；临界减速；dwell/escape 交替；亚稳态 |
| 可识别性 | **估计与定义冲突**：`Kelso (2012)` 明确——「亚稳态字面上是一种平稳瞬态」，而这类度量基于平稳性假设 |
| 数据要求 | 秒—分钟级密集采样；极小 N 的受控实验 |
| 典型失效模式 | 尺度错置；把词汇直接套到不同时间尺度的对象上。`arXiv:0911.0013` 是完整标本：把 `alpha_i/beta_i`、时滞、Hopf 分岔写进方程后**只用仿真**区分「robust / fragile」关系，**无任何数据拟合** |
| 真实证据基础 | **在运动/互动协调层：强**（`Kelso` 学派；`Frontiers in Human Neuroscience 14:317` 明确列出 dyadic social coordination 证据）。**在年尺度关系状态层：无** |

### F5 Lotka–Volterra / replicator dynamics

| 维度 | 内容 |
|---|---|
| 表示 | `dx/dt = a*x - b*x*y; dy/dt = b*x*y - c*y`（或 replicator `x_dot_i = x_i(f_i - phi)`） |
| 关键假设 | 物种/策略/资源是守恒或可归一化的；互动是成对乘积 |
| 使什么可观测 | 周期振荡、极限环、平衡点、稳定性 |
| 可识别性 | 弱：参数高度相关；`a,b,c,d` 常不可分离 |
| 数据要求 | 长时程密集序列 |
| 典型失效模式 | 经典缺陷：LV 允许被猎物种在极低数量下「反弹」，现实中几乎不会发生；把「关系」当「物种」没有辩护 |
| 真实证据基础 | **无** |

### F6 潜变量增长曲线 / DSEM / RI-CLPM 类（连续，含随机系数）

| 维度 | 内容 |
|---|---|
| 表示 | `y_ti = eta_0i + eta_1i * t + eps_ti`，随机截距/斜率，协变量时变 |
| 关键假设 | 个体内过程**平稳**（至少二阶平稳） |
| 使什么可观测 | 截距、斜率、随机系数方差、within/between 分解 |
| 可识别性 | **关系科学中实际可用的那一档**，但受三重约束：(a) 稳定成分吞掉方差（满意度秩序稳定性 `r = .76`）；(b) 自回归接近 0 时测量误差与过程随机输入不可分（`Hamaker et al. 2015`）；(c) 时变因子稳定性越高，within 与 trait 越难分（`Cole et al. 2025`），载荷 .35–.45 时 power 仅 0.04–0.33 |
| 数据要求 | `>=3` 波，最好 4–7 波；N 需足够（随机效应方差在 `N<50` 时系统性正偏） |
| 典型失效模式 | **within/between 混淆**（含符号错误风险）；小样本方差正偏；缺失数据下拟合准则失效 |
| 真实证据基础 | **中—强**。这是当前关系科学里唯一有大量成功应用的一档，但产出的是**组均值层面的趋势参数**，不是结构 |

### F7 group-based trajectory modeling（连续读出 + 离散潜在类）

| 维度 | 内容 |
|---|---|
| 表示 | 读出 `y_t` 连续；潜类 `c_i in {1..K}`；类特异的形状参数 |
| 关键假设 | 类数 `K` 由 BIC 等准则**统计选出**，非先验给定 |
| 使什么可观测 | 「有几条不同形状的轨迹」；异质性 |
| 可识别性 | 中：`K` 本身可选但会随样本变动（`Nagin & Odgers 2010` 给出报告规范以缓解） |
| 数据要求 | 3–5 波以上 |
| 典型失效模式 | 把连续分布切成类；小类不稳定；外推脆弱 |
| 真实证据基础 | **强（就「满意度读数」这一单条指标而言）**：`Anderson et al. (2010)` 在 MILS 连续婚姻者 `N=706` 上发现 **5 条不同轨迹**，并明确「不是一条持续下降的曲线」；`Williamson & Lavner (2020)` 在多元新婚样本中复现「多数高满意稳定 + 小部分中高度下降」 |

### F8 图 / 关系事件动力学（relational event models, dyadic latent class）

| 维度 | 内容 |
|---|---|
| 表示 | 事件流 `(i, j, time, type)`；倾向函数含互惠性、传递性、活跃度；可加 dyad 潜类 |
| 关键假设 | 互动是**事件**而非状态；网络结构由倾向函数生成 |
| 使什么可观测 | 谁对谁做了什么、多快、是否互惠；网络级互惠/传递 |
| 可识别性 | 中：倾向函数在充分事件量下可估；`Lakdawala et al. (2026)` 的 dyad 潜类版本可捕捉二元异质性 |
| 数据要求 | 事件级日志（需仪器或被动采集） |
| 典型失效模式 | 只看得到「发生了什么」，看不到「感觉如何」；需要高分辨率事件源 |
| 真实证据基础 | **中**（`CITED_SECONDARY`；本 lane 未审计具体实证） |

### F9 离散二元序列方法（L-APIM + Markov chain）

| 维度 | 内容 |
|---|---|
| 表示 | 分类二元序列 `(s^A_t, s^B_t)`；一阶齐次转移 |
| 关键假设 | 一阶、齐次、等长、有序；`NA` 被拒收（缺失会打断转移对构造） |
| 使什么可观测 | **actor/partner 交互模式**的统计身份（A1：actor-only 限制；B1：partner-only 限制），用 LRT 检验 |
| 可识别性 | **在这条方法线内部是可识别的**（有显式约束与检验），这是它对 F2 的关键优势 |
| 数据要求 | 分类观测、等长、有序、**无缺失** |
| 典型失效模式 | 一阶齐次假设；对缺失零容忍（会减少可用样本）；状态分类本身的质量全靠人工/编码 |
| 真实证据基础 | **弱—中**：方法成熟且已实现（CRAN 包 `dyadicMarkov`），但文献应用集中于**短程互动/治疗会话**，不是年尺度关系状态。`CITED_PRIMARY`（软件文档） |

### F10 有序/序数投影层（ordered-probit 语义，作为 measurement 而非 ontology）

| 维度 | 内容 |
|---|---|
| 表示 | 潜在连续 `y*` + 阈值向量 `tau`：`P(y* < tau_k) = F(tau_k)` |
| 关键假设 | 类别**非等距**；潜在方差不跨组/跨时点相等 |
| 使什么可观测 | 正确的响应概率；不强迫等距 |
| 可识别性 | 对**阈值本身**高度敏感（这正是问题所在）；但对本体不做任何承诺 |
| 数据要求 | Likert 类序数观测 |
| 典型失效模式 | 被误当作「可以当连续用」时会产出**系统性效应反转** |
| 真实证据基础 | **已确证的失败模式**：`Liddell & Kruschke (2018)` 调查 JPSP / Psychological Science / JEP:General 中所有提及 Likert 的文章，**100% 使用度量模型**处理序数数据；度量误用导致 false alarm、漏检、**效应方向系统性颠倒**；**对多个序数项取平均不能修复**；**没有可靠的事后检出办法** |

### 2.1 表的横贯读法

- **没有任何一行的「真实二元关系数据证据基础」是「强 + 覆盖动力学结构」。** 最强的几行各自只在一个受限的层面上强：F4 在秒—分钟的运动协调层；F7 在**满意度这一条读数的轨迹形状**上。F6 是唯一在关系科学中**大量成功应用**的一档，但产出的是趋势参数而非结构。
- **离散侧的统一失效模式是「状态数被数据结构吸收」**（`Pohle et al. 2017`）。**连续侧的统一失效模式是「平稳性假设被亚稳态违反 + 参数由先验而非数据决定」**（`Kelso 2012`；`arXiv:0911.0013`）。
- **混合状态空间不解决可识别性问题，只改变参数化方式。** 允许 `category | ordinal | interval | Unknown` 共存（`CURRENT_ARCHITECTURE` §9 原则 4–5）意味着每个坐标必须声明其**测量模型类型**；一旦声明，序数坐标就必须用序数模型（`Liddell & Kruschke 2018`），否则会得到方向反转。这一步**强制把离散性放回 measurement 层，而不是消灭它**。

---

## 3. 粗关系标签：为什么应当是 readout（以及这个论证的边界）

本节同时给出两侧证据。**反方证据在 §3.3，不得跳过。**

### 3.1 支持侧：四条实质证据

**(1) 同一标签区间内包含动力学上不同的段落。**

`Bühler & Orth (2025, JPSP, doi:10.1037/pspp0000551)` 在四个全国性纵向研究（含德国 `pairfam`，四个数据集共 11,295 人，调查期 12–21 年）中，用分段多层模型 + 倾向得分匹配的事件/对照组（事件组 `n = 987–3,373`，对照组 `n = 1,351–4,717`）发现：

```text
satisfaction ~ f(time-to-separation)
  = preterminal phase（较小下降）  ->  terminal phase（陡降）

terminal phase 起点估计：分离前 0.58 – 2.30 年
```

并且 **time-to-separation 比 time-since-beginning 更能预测变化**。

含义：`married` 这个标签同时覆盖了「平稳段」「preterminal 段」「terminal 段」三个动力学上不同的状态。因此：

```text
RelationshipLabel = married   不蕴含   ~   RelationshipState
```

这是本 lane 找到的最强「标签不等于状态」证据。**但注意同时到来的限制**（见 §3.4 第 3 点）。

**(2) 标签不分离读数分布。**

`Bühler & Orth (2024, JPSP 126(5):930–945)`，`Longitudinal Study of Generations`，`n = 2,268`（16–90 岁），最多 7 波跨 20 年：dissolving 与 continuing 关系中满意度**都**在下降且分布重叠。

**(3) 标签不预测机制。**

- 生理同步：`PMC7017247` 报告「我们关于同步随关系亲密度增强（恋人 > 朋友 > 陌生人）的**第一个假设没有成立**」。
- 情绪互依：`PMC7065936` 用 pseudo-couple 零分布发现，**只有 14–38% 的伴侣**在所考察的具体度量下表现出超出 pseudo-couple 的显著线性/非线性协动；作者结论是情感互依「可能**不是**亲密恋爱关系的内在特征，而是一种高度情境依赖的特征」。
- 生理同步的 meta 分析（`Mayo, Lavidor & Gordon 2021, Physiol Behav`）：与关系结局的**相关仅 `ES = 0.09, p > .10, I² = 76.0%`**；亚组：交感 `+0.19`、副交感 **`-0.21`**、合并 `+0.16`；与表现结局 `ES = 0.26, I² = 52.7%`。

**(4) 承诺与满意度在经验上可解耦。**

`Rusbult (1980, JESP 16(2):172–186)` 实证「关系承诺可能高而满意度与吸引低」。`Tran, Judge & Kashima (2019, Personal Relationships 26(1):158–180)` 在 50,427 名参与者、202 个独立样本上给出三者的 meta 相关：满意度 `r = .65` > 投资 `r = .53` > 替代选项质量 `r = -0.43`。三者若本就是同一个状态的不同名字，不应有这种可分离的强度结构。

### 3.2 制度事实也是离散的（这一点是 pro-label 的）

`married` / `engaged` / `legal separation` / `custody` / `cohabiting` 是**法律与协议事实**。把它们「连续化」会直接损害事实保真，与 `AGENTS.md` Representation-first invariant 3（保留原始证据/来源）冲突。`Rusbult & Martz (1995)` 与 `Böllenrücher et al.` 的工作也说明「承诺」是一个需要被制度化记录的量。

**因此本报告的立场不是「离散是坏的」，而是「离散在哪一层」。** 见 §9。

### 3.3 反方侧：四条实质证据（不得压缩）

**(R1) 离散轨迹分类在真实二元数据上有解释力。**

`Anderson, Van Ryzin & Doherty (2010, J Family Psychol 24(5):587–596)` 在 `Marital Instability over the Life Course Study` 的 `N = 706` 连续婚姻者上：

> Instead of a single continuously declining trajectory of marital happiness, we found **5 distinct trajectories**.

其中约 2/3 为高且稳定；1/3 为持续低幸福、低幸福后下降、或「高幸福 -> 下降 -> 恢复」的曲线型。`Williamson & Lavner (2020)` 在多元、低收入社区新婚样本中复现「多数高满意且几乎无下降；大幅下降限于起点较差的少数」。

这条证据的实质含义：**「关系发展存在若干条不同动力学」是可实证的命题，不只是理论偏好。** 项目的 `readout` 立场无法反驳这一点——事实上 F7 的成功恰恰**依赖**状态数由 BIC 统计选出（见 §3.4 第 4 点）。

**(R2) 假装连续比承认离散更危险。**

`Liddell & Kruschke (2018, JESP 79:328–348)` 是本报告最强的方法学证据：

- 调查 JPSP / Psychological Science / JEP:General 中所有提及 Likert 的文章，**100% 使用度量模型**分析序数数据；
- 度量误用产生 **false alarm (Type I)**、**漏检 (Type II)**、以及**系统性效应反转**（把序数当度量会给出与真实顺序相反的均值排序）；
- 同样问题出现在交互作用与趋势分析中；
- **对多个序数测量取平均并不修复这些问题**；
- **不存在可靠的事后检出办法**；
- 作者建议改用 ordered-probit（或类似）模型。

机制（`Bürkner & Vuorre 2019`）：(a) 序数类别的心理距离不必等距；(b) 潜在变量的方差可跨组/跨时点不同（这在 `0..1` 投影下**完全不可见**）；(c) 序数分布有界、偏斜、离散、常多峰（`Ferr et al. 2025`）。

这条证据的含义是：**一个把所有坐标压到 `0..1` 的连续本体，若其观测是 Likert 类别，会在 read-out 阶段产出方向颠倒的结论。** 项目 `Representation-first invariant 4`（不强迫 `0..1`）在这一点上是**正确的**，但该 invariant 的**理由**在 canonical 文本中没有被这样论证过——它应该被这样论证。

**(R3) 阈值型动力学在真实二元数据上确实被估计出来了。**

`Bühler & Orth (2025)` 的终末下降是一个**预注册、四个全国样本、有对照组、有可估计转折点**的结果。这不是伪影式的「我们看到了一个拐点」，它是本 lane 找到的**唯一一个**满足方法学门槛的阈值型关系结论。

它对项目立场的意义是**双重的**：它同时支持「不预枚举」（因为它是分段连续读出，不是离散 regime）**并**支持「阈值在关系数据中是真实可估计的」（这与「阈值主张不可信」的批评相反）。项目必须两面都承认。

**(R4) 存在成熟的离散二元动力学方法线。**

`Böllenrücher, Darwiche & Antonietti (2023, TQMP 19(3):230–243; 2024, TQMP 20(1):17–32)` 及其 CRAN 实现 `dyadicMarkov` 提供了：

```text
empirical transition counts  ->  MLE transition probabilities
A1 比较：actor-only 限制
B1 比较：partner-only 限制
识别方式：LRT（Pearson chi-squared）
假设：一阶、齐次、等长、有序
缺失：显式拒收（NA 会打断转移对构造，不自动删除或插补）
```

对一个「有分类观测的二元序列」问题，这是一条 parsimonious、可证伪、已实现、有身份检验的路线。**它不是一个稻草人。** 项目若要在文档里说「不用状态机」，最好同时说明为什么不采用这类**有身份检验的**离散二元方法。

### 3.4 支持侧论证的四个边界（诚实交代）

1. **「标签不预测机制」依赖具体的机制度量。** 同步在秒—分钟尺度上测（`Marzoratti & Evans 2022`：同步是时间窗假象敏感的），而 `married` 覆盖数十年。不匹配的时间尺度不能互相否证。
2. **情绪互依的负面结果可能部分来自测量与检验功效**（`PMC7065936` 自述样本分组较粗、协变量简化）。它是一个**强负面提示**，不是否证。
3. **`time-to-separation` 是结果变量。** `Bühler & Orth (2025)` 的终末下降在原文中被建模为 time-to-separation 的函数；作者本人强调「once the terminal phase is reached, the relationship is doomed to come to an end ... only the individuals in the separation group go through this terminal phase, not the control group」——这正是**条件于结局**。项目若引用它，必须同时引用这个限制。
4. **`Anderson et al. (2010)` 的 5 类是「满意度读数的轨迹形状」**，且类数由 BIC 选出（该文明确：需 BIC 最大且最小类占样本 `>= 6%`）。因此它证明的是**读出轨迹的异质性**，不是**本体状态的离散性**。项目可以把这条当作「readout 分类有价值」的证据，而**不能**把它当作「本体应当离散」的证据。**这是一个真正的解释权之争，而不是事实之争。**


---

## 4. 动力学可识别性：严格处理

### 4.1 问题陈述

给定稀疏、聚合、自报、年度级的二元关系观测，我们希望约束

```text
X_(t+1) = F(X_t, Action_t, Event_t, Belief_t, Constraint_t, Environment_t)
```

中 `F` 的**结构**（而不只是参数）。本节论证：在当前数据条件下，`F` 的**结构**大体不可识别；可被识别的只有 `F` 的**最外层线性化/分段线性化**（即组均值层面的趋势）。

### 4.2 三个可叠加的识别障碍

**O1 — 稳定性主导（stability dominance）**

构念的类特质、时间不变成分吞掉大部分可观测方差，于是「自回归」估计的主要是**个体均值**而非过程。

定量锚点：`Bühler & Orth (2022, JPSP 123(5):1138–1165)`，`148` 个样本、`153,396` 名参与者、关系时长 3 个月–46 年、平均年龄 19–71 岁，个体差异的**秩序稳定性平均 `r = .76`**（已校正测量误差衰减，平均时滞 2.30 年），且稳定性随年龄升高、在关系头几年较低。

含义（`AI_DERIVED_CHARACTERIZATION`）：可观测的总变化中，只有一小部分是**个体内**的。我们把绝大部分数据预算浪费在估计「谁比谁更满意」上，而不是「关系如何随时间变化」。

**O2 — 过程随机输入与测量误差不可分离**

`Hamaker, Kuiper & Grasman (2015, Psychological Methods 20(1):102–116)` 给出两条（`CITED_PRIMARY`）：

> (a) if stability of constructs is to some extent of a trait-like, time-invariant nature, the autoregressive relationships of the CLPM fail to adequately account for this. As a result, the lagged parameters that are obtained with the CLPM **do not represent the actual within-person relationships over time**, and this may lead to erroneous conclusions regarding the presence, predominance, and **sign** of causal influences.

> (b) when the autoregressive parameter is very close to zero, it becomes difficult to distinguish between variance that is due to **measurement error**, and variance that is the **stochastic input of the autoregressive process**.

第二条是致命的：低自回归正是**低信噪比**的表现，而这恰恰是关系数据最常见的情形。`Cole et al. (2025, doi:10.1177/25152459241302300)` 的模拟显示 4 波 RI-CLPM 中载荷 `.35–.45` 时检出个体内效应的 **power 仅 0.04–0.33**；且「时变个体内因子稳定性越高，就越难把它与特质成分区分开」。

**O3 — 状态数 / 参数数不可识别**

`Pohle, Langrock, van Beest & Schmidt (2017, arXiv:1701.08673)`：

> the **notorious** problem of order selection in hidden Markov models

当 HMM 未纳入真实数据中的异常值、季节性、个体异质性时，additional states may be able to capture this ignored data structure and therefore provide a better model fit than models with a lower, but (biologically) more realistic number of hidden states；**AIC and BIC tend to favor models with too many states**；**no one-size-fits-all objective and universally applicable criterion can be developed for order selection in HMMs**。

`van Havre et al. (2015, Bayesian Analysis)` 补：状态数超过数据支持时的**非可识别性**是阶数估计的**隐含**组成部分。`Schultzberg & Muthén (2018)`：随机效应方差在 `N < 50` 时系统性正偏。

### 4.3 LHRM 特有的两重加重

**O4 — 观测密度。** 本 lane 见到的最强关系纵向研究是 **3–7 波、跨 12–21 年**（`Bühler & Orth 2025` 四研究 12–21 年；`Bühler & Orth 2024` 最多 7 波跨 20 年；`Carrese-Chacra et al. 2023` 20 个月随访；`Schokkenbroek et al. 2022` 4 波 4 个月）。在这个密度下能可靠估计的是**组均值层面的线性/分段线性趋势**。停留时间分布、多吸引域、半 Markov 性都超出信息量。

**O5 — 状态维度与个体数的乘积效应。** LHRM 状态含 `2N` 个有向关系坐标 + `PairState` + `2N` 个 belief + `Environment` + `Constraint`，且 belief 层原则上还有嵌套结构。`AI_DERIVED_CHARACTERIZATION`：在每次观测波数为 `O(3–7)` 的条件下，这是一个**参数增长率远快于信息增长率**的情形。此时 `F` 的具体形式**不可能**被数据约束，只能被**先验**或**判断**约束。

**这直接推出一个必须写进 canonical 的陈述：**

> LHRM 当前阶段的 `F` 是 **architecture decision / model hypothesis**，不是 empirical estimate。任何把 `F` 的形式当作「已经选对了」的表述都是越权。

### 4.4 诚实的量化边界

**可以主张的**（有 `CITED_PRIMARY` 支撑）：

> 在 3–7 波、跨 12–21 年、满意度秩序稳定性 `r ≈ .76`、单条自报满意度读数的条件下：**组均值层面的分段非线性趋势可被估计**（`Bühler & Orth 2025`）；**dyad 层面的吸引域、停留时间分布、迟滞结构不可被估计**。

**不主张的：**

- **不主张任何具体所需波次数或功效值。** 本 lane 未找到可靠一手来源，因此拒绝给出。（有 `CITED_SECONDARY` 层面的量级：4 波 RI-CLPM 在载荷 `.35–.45` 时 power `0.04–0.33`（`Cole et al. 2025`）——但这是**给定特定 DGP** 的模拟结果，不能直接搬到 LHRM 的观测结构上。）

---

## 5. 迟滞（hysteresis）：最诚实的回答

### 5.1 什么才算证据

「关系变差又变好」「结果不好但没分开」「吵完架感情更深」**都不是**迟滞。要成为迟滞证据，至少需要：

| 代号 | 判据 | 为何必要 |
|---|---|---|
| **E1** | **双向路径覆盖**：同一控制量 `u` 在**上升段与下降段**都被扫过，且两段可比较 | 单程数据无法区分迟滞与两个不同吸引域 |
| **E2** | **分支在统计上可分离** | 否则只是异质性——而异质性正是 O1/O2 的默认解释 |
| **E3** | **扰动撤除后不回到原值/原盆地** | 区分「记忆」与「恢复」 |
| **E4** | **分支差不能被未观测异质性解释** | 排除「不同人走不同轨道」 |
| **E5** | **观测时间窗与被测过程匹配** | 同步是时间窗假象敏感的（`Marzoratti & Evans 2022`） |

E1 的经典 realized design 是**升序/降序分别呈现**的量表/刺激序列。

### 5.2 现有证据到哪一步

| 层级 | 状态 | 依据 |
|---|---|---|
| 感觉生理/运动协调的多稳态 + 临界减速 | **已展示**（受控、极小 N、秒—分钟尺度） | `Kelso 2012`；`Kelso, Scholz & Schöner 1986`；`Tognoli & Kelso 2020` |
| 通过增强 HKB 直接施加于社会互动（Human Dynamic Clamp） | **已展示**（clamp 实验） | `Tognoli & Kelso 2020`（明确列出 dyadic social coordination 证据：`Tognoli et al. 2007; Oullier et al. 2008; Tognoli 2008`） |
| 心理物理量级估计中的迟滞 | **有经典展示**（单人、升/降两段序列） | Peterman (1963), *J. Exp. Psychol.*,「On the problem of hysteresis in psychophysics」——**`CITED_PARTIAL`，作者/卷期 `AGENT_RECALL` 未核实** |
| 工程/物理中的迟滞识别 | 存在（作为「迟滞识别本身是真实估计问题」的存在性证据） | *A nonlinear state-space approach to hysteresis identification*, *J. Sound Vibib.*（`CITED_SECONDARY`）；CRAN 包 `hysteresis` |
| **二元关系数据的 dyad 级迟滞** | **本 lane 未找到任何已发表的估计 → `NEGATIVE_RESULT`** | §5.3 |
| 二元关系**组均值**的「冲击 -> 恢复」 | **有展示，方向是恢复不是记忆** | `Carrese-Chacra et al. 2023`；`Schokkenbroek et al. 2022` |
| 二元关系**跨关系**的路径效应 | **有展示；这是跨 dyad 的记忆，不是同一 dyad 内的迟滞** | `Bühler & Orth 2024` |

### 5.3 检索过程与 NEGATIVE_RESULT 的诚实交代

**已做的检索**（三组查询）：

1. `hysteresis demonstration marital OR couple OR "close relationship" empirical path dependence evidence romantic relationship lag`
2. `testing hysteresis in psychological data null distribution identification problem "hysteresis" nonlinear measurement`
3. `hidden Markov models psychology pitfalls overfitting number of states latent state inference overinterpretation critique`（用于定位 HMM 侧的识别问题，作为对照）

外加一篇对照文献：Peterman (1963)（见 §5.2）。

**结果**：在真实二元关系数据（夫妻/恋爱/亲子/照护）上，**未找到**任何估计出迟滞环或路径依赖分支的同行评审实证研究。

**这个 negative result 的边界**（必须一起说）：

- 未检索法文/德文数据库（`pairfam` 的德语文献是可能的来源）；
- 未检索 `history` / `histories` / `path dependence` + `marriage` / `couple` 的组合；
- 未检索 `critical slowing down` 在关系数据上的应用；
- 未检索「轨迹 + 阈值效应」类综述的全文（`FETCH_FAILED`）；
- 2024–2026 年新出的协调动力学应用论文覆盖可能偏旧。

因此这是 `PARTIAL` 的 negative result，**不是穷尽性证明**。但它足以支撑一个操作性结论：

> **在可检索范围内，「迟滞是人类二人关系的可观测动力学性质」是一个 `model hypothesis`，不是有实证基础的现象陈述。**

### 5.4 为什么这件事比「还没测」更严重

三个独立理由，第三个是本报告最强的负面发现：

1. **迟滞需要强耦合。** 没有 A 影响 B、B 影响 A 的稳定回路，就没有分支。
2. **强耦合在多数真实 dyad 中不成立。** `Mayo, Lavidor & Gordon (2021)`：生理同步与关系结局 `ES = 0.09, I² = 76.0%`；`PMC7065936`：只有 14–38% 的伴侣情绪协动超过 pseudo-couple；`PMC7017247`：`lovers > friends > strangers` 预期**未成立**。
3. **因此**——不是「我们还没测迟滞」，而是**「我们测的那个过程（双向耦合）在多数 dyad 里不存在，所以迟滞的物理前提在多数 dyad 里不成立」**。

同时，**恢复（而非记忆）的证据更直接**：

- `Carrese-Chacra et al. (2023, Family Relations, doi:10.1111/fare.12885)`：封闭期第一月满意度**下降**，封闭期末**升到初始水平之上**，**20 个月随访时回到疫情早期基线水平**。
- `Schokkenbroek et al. (2022, Front. Psychol. 13:819874)`：4 波中「被调查伴侣总体上**逐渐适应得越来越好**」，问题解决困难与攻击行为下降，双方满意度同步变化。
- `Marín, Christensen & Atkins (2014, CFP 3(2):129–141)`：控制离婚后，不忠与无不忠组的满意度在治疗结束后**仍持续改善**。

**唯一接近「路径依赖记忆」的真实发现**是 `Bühler & Orth (2024)`：分开后开始新关系者在一开始比上一段更满意，**但两段内满意度都在下降**。这提示存在**跨 dyad 的起点差异**（路径效应的一个弱信号），但它是「从哪一段开始」的差异，不是「扰动后回不到哪」的差异。这两者在数学上是不同的（前者是轨道起点偏移，后者是路径依赖记忆）。

---

## 6. 扰动后的 repair：现状与「如何检测恢复」

### 6.1 现有研究实际测的是什么

几乎所有「冲击后恢复」研究测的是**组均值满意度轨迹**，不是 dyad 级状态恢复：

| 研究 | 冲击 | 观测 | 关键读数 | 方法学限制（作者自述或可见） |
|---|---|---|---|---|
| `Carrese-Chacra et al. 2023` | 疫情封闭 | 首次封闭期 + 20 个月随访 | 组均值满意度回到**疫情早期**基线 | 基线本身是疫情开始时的水平，不是疫情前 |
| `Schokkenbroek et al. 2022` | 封锁 | 4 波（2020-03 -> 2020-07），`N = 108` 对 | 问题解决困难与攻击**下降** | 截距在封锁开始而非封锁之前（作者自述） |
| `Vigl et al. 2022, PLOS ONE 17(4):e0264511` | 疫情 | 3,243 人 / 67 国，2020-04/05 | 与**回溯自评**的疫情前满意度比较 | 基线为回溯自评；作者引用他人研究称回溯满意度「一般相当准确」 |
| `Natsal-COVID (PMC12291618)` | 疫情 | 1,407 名稳定关系者，跨一年 | 关系质量差的比例上升，**但也存在从低质量向更高质量的流动** | 非概率样本 |
| `Cassinat et al. (PMC8611690)` | 疫情 | 682 家庭 / 2,046 人 | 家庭混乱上升；**评价差异使关系变化方向可正可负** | 自陈家庭进程量表 |
| `Marín et al. 2014` | 不忠 + 治疗 | RCT 子样本，19 对，5 年 | **两条路径**；不忠组离婚率 > 2 倍 | `n = 19`；**控制离婚后**满意度继续改善 |
| `Fife et al. 2023` | 不忠 | 16 对（**筛选出「经历了有意义的康复」**） | 4 阶段愈合过程模型 | 严重选择偏倚；定性设计 |
| `Heintzelman et al. 2014` | 不忠 | 继续维持关系者 | 创伤、宽恕、创伤后成长之间的关系 | 横断面/相关设计为主 |

**结论**：「恢复到基线」是**组均值意义**的。`Marín et al. (2014)` 明确显示组层面「恢复」掩盖了 dyad 层的**双路径分岔**：一部分持续改善到与无不忠对照组无法区分，另一部分明显恶化并离婚。

### 6.2 「如何检测恢复」在 LHRM 语境下尚无可操作定义

要把 repair 变成可检验命题，至少需要四件**目前不存在**的东西：

1. **Reference set**：扰动前**同一 dyad** 的状态分布或其参数，且该 dyad 在扰动前有 `>=2` 次观测。现有数据集（`Bühler & Orth 2025` 四研究；`Bühler & Orth 2024` 7 波）只在**部分**样本上满足。
2. **Restoration 判据**：至少四种互相不等价的选项——

   ```text
   (a) 数值返回基线的 X 倍置信区间内
   (b) 恢复趋势的斜率回到基线斜率
   (c) 盆地回归（basin return）
   (d) 拓扑等价（同一吸引域）
   ```

   这四种可以给出**不同答案**，且关系科学目前无共识。
3. **足够密的观测窗**：恢复是持续过程；年度数据只能看到 1–2 个恢复点。
4. **与 regression-to-the-mean 的分离**：若某 dyad 本就处于极端值，任何「回归」都可能是统计假象。由于 `r = .76`（`Bühler & Orth 2022`），极端值**持续存在**，因此必须显式建模，不能靠直觉。

**可主张的最强修复命题**（`CITED_PRIMARY`）：

> 不忠事件后的关系不是「恢复到原状」或「恶化」，而是**分岔为两条路径**：改善并维持 / 恶化并离婚（`Marín et al. 2014`）。并且这条命题由「满意度读数 + 离婚这一离散标签事件」定义。这一点直接关系到 §7 与 §9。

---

## 7. 项目「不用预枚举状态机」立场：哪里过度陈述，哪里是 reviewer 风险

本节是本 lane 的核心反向审计。以下每一项都不是「项目错了」，而是「当前措辞会被 reviewer 合理攻击」。

| # | 过度陈述 / 缺口 | Reviewer 会怎么问 | 候选修正方向（**提案，非 mutation**） |
|---|---|---|---|
| **O1** | Rule 9 用绝对否定：「核心关系演化 **does not** use a pre-enumerated relationship state machine **as the engine**」 | 「你的 `F` 是什么？未指定的 `F`（`X_(t+1) = F(X_t, Action_t, Event_t, Belief_t, Constraint_t, Environment_t)`）在工程上就是一张预写查找表的隐式版本。区别只在是否可读，不在是否预承诺。」 | 降级为**可证伪的分工主张**：「标签序列不是状态的**充分**引擎。若在任何数据集上，给定底层状态后 label 序列不提供增量预测信息，则应正式承认 label 可作为可接受的粗状态层。」 |
| **O2** | Rule 9 与 `CURRENT_ARCHITECTURE` §9 原则 4–5（`category / ordinal / probability / Unknown` 可共存于混合状态空间）之间**未声明的一致性要求** | 「你允许离散坐标存在于状态空间，同时说不用离散状态机——边界在哪？目前的 rule 9 与 §9 原则 4 读起来互相拉扯。」 | 显式写出两句：`discrete coordinate 允许存在于状态空间` 且 `discrete label 不得作为状态演化的唯一充分条件`。两句不矛盾，但必须都写出来。 |
| **O3** | `PARAMETER_CONVERGENCE_V0_1` P4 已 `KEEP` `Relationship Identity / Agreement` = `{friend, exclusive romantic partners, engaged, married, open relationship, care arrangement}` 为 pair/institutional agreement fact——**这本身就是一份手写枚举的离散层** | 「你在本体里禁离散，同时在制度事实层留了一张手写离散清单。区分合理，但 canonical 文本只给了断言，没给判据。」 | 给出**判据**（枚举正当的充要条件）：(i) 该维度有**外部制度/协议的权威定义**（可被第三方判定真伪）；(ii) 它**不生成**关系状态而是被关系状态更新；(iii) 其取值集合可被穷举且不需随理论修订而增长。 |
| **O4** | 「Core relationship evolution」这个限定词**在数学上没有定义** | 「你把哪些东西放到 core 里了？如果制度事实、边界规则、信任、依恋都不在 core，那 core 是什么？」 | 给出 `core` 的**可操作边界**：明确列出哪些坐标参与 `F`、哪些只作为 `Constraint / Agreement` 输入。否则「core」是免责词。 |
| **O5** | `CURRENT_ARCHITECTURE` §12 工程顺序第 5 步是 `State transition / dynamics`，但**没有任何一个可证伪的 transition-law family 被冻结**；`PARAMETER_CONVERGENCE` §15 的 Gate A/B/C 全是表示覆盖测试，没有一个是动力学测试 | 「把『不用状态机』当立场是偏好；只有**冻结一组能被数据否定的转移律**才是科学主张。你现在连要检验什么都没写。」 | 建议 `F` 至少以「候选族 + 每族一个可证伪预测 + 全部标 `NOT_ESTIMATED`」的形式被记录（与 R06 交接）。**即使全部未被估计，写下来也比不写强**，因为它把偏好变成了待检验命题。 |
| **O6** | 项目文本**没有任何地方**说明「readout 不得回流为 transition 输入」；`CURRENT_ARCHITECTURE` §6 写的是 `Action/Event updates State` | 「若 readout（满意度、标签）事实上回流影响 `F`，那么『它们只是 readout』的立场就自我取消了——这不需要任何新理论，只需承认系统是**闭合的**。」 | 显式声明读出层的三种可能（`open` / `semi-open` / `closed`），默认 `open`，或明确把「readout 回流」记录为一个**建模决定**，而不是让它隐式发生。 |
| **O7** | canonical 文本中目前**不出现** `attractor` / `hysteresis` / `regime` / `threshold` 这类词（这是好事），但因此项目**没有任何机制**阻止后续 report 把它们当已确立现象写入文档 | 「你们的 lane 里已经有 `arXiv:0911.0013` 那类文档了。」 | 在 `AGENTS.md` 研究纪律里补一条（与现有「不要把未验证的 state transition 标为已确立」同向）：这些动力学词汇使用时必须带 `model hypothesis` 标签。 |
| **O8** | 隐含但未声明的**时间尺度断言** | 「你的 `F` 是分钟尺度还是十年尺度？`Kelso` 那套 HKB 词汇在秒—分钟尺度有几十年的实验传统；把它套到年尺度上是尺度错置。」 | 在文档中显式写明 LHRM 的 `tau` 主要是**月—年级**，并声明因此**不采用** coordination dynamics 的词汇与参数化（除非未来引入分钟级观测通道）。 |

---

## 8. 对项目有利的正面结论（避免只呈现对立面）

> **本节编号的推断说明**（`AI_DERIVED_CHARACTERIZATION`）：本报告 §0–§7 依次落地了本 lane 的六组 finding（框架比较表；数学与动力学可识别性；迟滞；冲击/repair；粗关系标签；no-FSM 措辞审计）。**全文没有任何位置前向引用 §8**；而本 lane 已产出、尚未在正文出现的唯一一条实质 finding 是「对项目有利的正面结论（避免只呈现对立面）」。据此推断 **§8 = 该 finding**。为避免本 lane 已产出但未落地的材料被丢弃，本节同时并入另两块未落地材料：与离散层直接相关的 `remaining_unknown`（U1–U16）与全部 20 条 `explicit_non_claims`。**若 Human/Architect 认为 §8 应另有其题（例如单独作为交接清单），本节可整体移动；§9 的论证不依赖本节编号。**

本节的存在有独立理由：§0 声明本文件的目的是找反例，但一份只列反例的报告会被合理地指控为选择性取证。**支持项目方向的那一侧必须与反对侧同等分量地出现在正文里，而不是只出现在 packet 里。**

### 8.1 四条对项目有利的正面结论

**(1) 关系科学里最好的「阈值型非线性」结果，形式是分段连续读出，不是离散 regime。**

`Bühler & Orth (2025)` 的终末下降是预注册、四个全国性纵向样本、事件/对照组匹配的可估计分段形状（terminal 段起点为分离前 0.58–2.30 年）。**它的估计对象是单条满意度读数随 time-to-separation 的函数**——按 §1 的定义，这是 `Threshold-1`（读出阈值/分段形状），不是 `Threshold-2`（存在于 `F` 中的动力学阈值）。含义：真实关系数据里最硬的那个「非线性」发现，是靠一条连续读出加一个事件时钟得到的，**没有任何预枚举的状态集**。

**(2) 离散轨迹分类的有效性，恰恰依赖「状态数由统计选出」这一操作。**

`Anderson et al. (2010)` 的 5 条轨迹不是先验枚举的：该文要求 BIC 最大、且最小类占样本 `>= 6%`。`Williamson & Lavner (2020)` 在多元、低收入社区新婚样本中复现同一形态。**因此离散层在本项目里的价值来源是「读出形状的分类」，而不是「本体是离散的」**——这与项目 readout-first 的立场**兼容**，而不是冲突。

**(3) 真实的 dyad 级分岔确实存在，但目前只能由「读数 + 离散制度事实」定义。**

`Marín, Christensen & Atkins (2014)`：不忠伴侣 5 年后分岔为「持续改善并维持」与「明显恶化并离婚」两条路径，不忠组离婚率超过对照组两倍。**定义这条分岔的变量是自报满意度读数 + 是否离婚这一离散标签事件。** 因此离散层是**必要的观测/事实坐标**，但**不足以成为引擎**（对应 §9.3.1 的 L-A 与 §9.3.4 的 L-D）。

**(4) `Liddell & Kruschke (2018)` 为 Representation-first invariant 4 提供了 canonical 文本中尚未写出的论证基础。**

该文证明：把序数当度量会产生 false alarm、漏检与**系统性效应反转**；相关心理学期刊中提及 Likert 的文章 **100%** 这么做；**对多个序数项取平均不能修复**；**不存在可靠的事后检出办法**。**项目 invariant 4（不强迫 `0..1`）因此不只是「谨慎」，而是「不这么做就会得到方向颠倒的结论」**——这条理由目前没有写进 canonical 文本，应补上（属 `AI recommendation`，对应 §7-O2）。

### 8.2 这四条支持的是「分工主张」，不是「动力学主张」

必须把「支持」拆到具体层级，否则正面结论会被过度使用。下表逐条给出**支持到哪一步**与**明确不支持什么**：

| 正面结论 | 支持项目立场到哪一步 | **不**支持什么 | 类别标记 |
|---|---|---|---|
| (1) 终末下降是分段连续读出 | 支持「不把离散标签当引擎」 | **不**支持「`F` 的连续形式是对的」；原文中 time-to-separation 是**结果变量**（§3.4 第 3 点） | `empirical evidence`（`CITED_PRIMARY`） |
| (2) 轨迹分类依赖 BIC 选状态数 | 支持「离散层的位置是 readout 分类」 | **不**支持「本体应当离散」；也**不**支持「状态数可被稳定识别」（`Pohle et al. 2017`） | `empirical evidence` + `AI_DERIVED_CHARACTERIZATION` |
| (3) 双路径由读数 + 离散事件定义 | 支持「离散层必须存在（事实坐标）」 | **不**支持任何 `regime` / 吸引域 主张；`n = 19` | `empirical evidence`（`CITED_PRIMARY`，但 `n` 极小） |
| (4) 序数当度量会方向反转 | 支持 invariant 4 的**理由** | **不**支持「离散优于连续」这一更强的本体主张 | `empirical evidence`（`CITED_PRIMARY`）+ `AI recommendation`（补写理由） |
| 项目 rule 8 / rule 9 本身 | 是 `Human requirement`（`AGENTS.md` Current architecture direction 第 8/9 条），其正当性目前**不依赖**任何动力学证据 | 不因本报告而改变；本报告只提出措辞层面的可证伪改写（§7） | `Human requirement` / `existing project constraint` |

**因此，正面一侧的真实内容只有一句**：项目当前的**表示层**立场站得住，且本 lane 找到的最强非线性关系证据**间接**支持它（§3.1）。**但没有任何一条正面证据支持「`F` 的形式已被选对」**——后者是 `architecture decision / model hypothesis`（§4.3 已定级）。

### 8.3 已知脆弱点：本 lane 自己没能解决的

这些必须与正面结论同等显著地报告，否则 §8.1 会被读成「项目已被验证」。

| # | 脆弱点 | 状态 | 若它朝不利方向解决，会改动本报告哪一条 |
|---|---|---|---|
| **V1** | `Kay & Hensler (2018)`（常被引为「大样本心理物理观测上，连续潜特质优于 5 个离散状态」）——四次查询 + 一次 `webfetch` 全部失败 | `FETCH_FAILED`；本报告**不引用**它，结论不依赖它 | 若其结论成立（稠密观测下离散状态优于连续），则 §9.3.4 的 **L-D 定位需重做**：离散层可能需要升级为可被直接参数化的状态层，而不是纯读出 |
| **V2** | mission 要求的 Christensen–Kessels「实质门槛」反驳指针 | `UNVERIFIED_POINTER`；已用三条**已核实**的门槛批评替代（`Gelman & Stern 2006`；`Gelman & Loken 2014`；`Loken & Gelman 2017`）+ `Heck, Simons & Chabris 2018` | 无。门槛批评的论证不依赖该特定指针（影响：低） |
| **V3** | 迟滞 `NEGATIVE_RESULT` 的检索覆盖 | `PARTIAL` | §5.3 已列出的五条覆盖缺口；本节不重复 |
| **V4** | `Thompson (2011)` 全文、突变模型拟合综述、`arXiv:0911.0013` 全文、关系轨迹综述 | `CITED_PARTIAL` / `FETCH_FAILED` | 涉及这几项的强主张均已在正文降级为「有引文支持的方向性判断」，不作决定性证据 |
| **V5** | 关系标签的跨文化/跨法律语义等价性（`married` / `partner` / `ex` 在不同体系下是否同一件事） | `UNKNOWN` | 直接决定 §9.3.1 的 **L-A 能否被当作跨文化固定坐标**；本报告因此只判 L-A 在**单一制度语境内**合法 |
| **V6** | belief 与 action 是否在经验上可分离 | `UNKNOWN` | 若不可分离，`State != Action` 就没有经验基础（§9.3.2 的 L-B 随之降级） |

**V1 必须被单独强调**：它是本 lane 已知的、**会直接推翻本报告一条核心建议**的单点。这不是免责声明式的提及，而是 §9.6-K8 的正式内容。

### 8.4 本报告明确不主张的（20 条）

这些是本 lane 的自我约束。**把它们集中放在正文，而不是只放在 packet 里**，是为了让 reviewer 不必信任我就知道本报告的边界在哪。

**A. 关于关系本体与动力学**

1. **不主张**人类二人关系中不存在真实的阈值 / regime / 吸引域结构。pro-discrete 证据（`Anderson et al. 2010`；`Bühler & Orth 2025`；`Marín et al. 2014`）是**实质性的**。
2. **不主张**连续表示必然优于离散表示。`Liddell & Kruschke (2018)` 表明在**测量层**，假装连续会产出**系统性效应反转**——这是比「离散不好」强得多的证据。
3. **不主张** LHRM 已经有任何**可识别的** dynamic structure。§4 论证的正是相反方向。
4. **不主张**迟滞已被证明，**也不主张**迟滞已被排除。§5 的 `NEGATIVE_RESULT` 不是穷尽性证明（§5.3 已列覆盖缺口）。
5. **不主张** attractor / metastability 已在关系时间尺度上被证明。真实证据在秒—分钟尺度的运动/互动协调层（`Kelso 2012`；`Tognoli & Kelso 2020`）。
6. **不主张**阈值在原则上不可检验。只主张在**当前测量条件**下与替代解释不可区分。
7. **不主张**任何形式的状态机是错的。只主张把**关系标签**当引擎缺少证据支持，且会与项目自身的 mixed-state 表述产生**未声明的矛盾**（§7-O2/O3）。
8. **不主张** coupled-oscillator 框架对关系无效。只主张其证据基础弱、效应量小、异质性高、耦合前提在多数 dyad 中不成立（`ES = 0.09, I² = 76.0%`；14–38%；`lovers > friends > strangers` 预期未成立）。

**B. 关于本报告自身的可信度边界**

9. **不主张**本报告中标 `AI_DERIVED_CHARACTERIZATION` 的任何陈述是实证结论。
10. **不主张**任何具体功效数字或「所需波次数」（§4.4 明确拒绝给出）。
11. **不主张** Christensen–Kessels 指针的内容（`UNVERIFIED_POINTER`）。
12. **不主张** `Kay & Hensler (2018)` 的结论（`FETCH_FAILED`）；本报告任何结论都不依赖它。
13. **不主张**文献数量或 LLM 一致度构成验证。本报告每条主张都绑定具体指针 + 证据级。
14. **不主张**本报告读了 `Thompson (2011)`、突变模型 cusp 拟合 primer、`arXiv:0911.0013` 的**全部**全文（三者分别为 `CITED_PARTIAL`、`CITED_PRIMARY`（可读段）、`CITED_PRIMARY`（片段））。涉及它们的强主张已降级为方向性判断。

**C. 关于建议与改动**

15. **不主张**本报告对 `AGENTS.md` rule 9 或 `CURRENT_ARCHITECTURE` §6 的任何修改已经发生。本文件是 `RESEARCH_CANDIDATE`；写入需 Human/Architect 审阅。
16. **不主张** `Bühler & Orth (2025)` 的终末下降是因果机制。它在原论文中被建模为 time-to-separation 的函数，而 time-to-separation 本身是**结果变量**（§3.4 第 3 点已主动降级）。
17. **不主张** §9 的四层划分是唯一正确划分。它是 `AI recommendation`，其正当性论证依赖 §3.4 承认的四个边界。
18. **不主张** §2 框架表中任何一行的「典型失效模式」是该框架的**唯一**失效模式；表格只列本 lane 找到的、被一手指针支持的失效模式。
19. **不主张** LHRM 应当采纳或不采纳任何一个具体替代框架。§9 的建议是关于**层次位置**的建议，不是关于**框架选择**的建议。
20. **不主张**本报告的结论适用于 LHRM 研究域之外（动物、神经、遗传仅作 mechanism evidence，沿用 `CURRENT_ARCHITECTURE` §2 既有约束）。

---

## 9. 离散层：应该有，而且应该不止一层——但任何一层都不能是 `F` 的引擎（`AI recommendation`）

本节是 §0 第 5 条与 §3.2 结尾所承诺的交付：**离散层的 4 个具体位置**。**本节不引入任何新来源**；全部指针来自本 lane 已核实的 78 条指针，引用沿用 §2–§7 已使用的标签。

> **类别**：`AI recommendation`。**不是** `Human requirement`，**不是** `empirical evidence`，**不是** canonical 变更。任何一条被采纳都需 Human/Architect 审阅（§8.4-C-15）。
>
> **记号提示**：本节用 `L-A`/`L-B`/`L-C`/`L-D` 标记四个层，用 `K1`–`K9` 标记可证伪/撤退判据（`K` = kill criterion），**刻意避开 `F1`–`F10`**，因为那组编号已被 §2 的框架表占用。

### 9.1 两侧等重的开场

**本报告保留的立场**（`AI_DERIVED_CHARACTERIZATION`，与 §4.4 同级）：

> 在**年度、自报、聚合观测**这一尺度上，「连续/混合状态 + 无预枚举引擎」是一个**可辩护但未经验证**的位置。它有本 lane 找到的最强非线性关系证据的**间接支持**（§3.1-(1)：`married` 覆盖三个动力学上不同的段落；§8.1-(1)），但**没有任何已发表的估计验证过它的动力学形式**。因此它现在只能标 `model hypothesis` + `architecture decision`，不能标 `empirical evidence`。

**与它等重的相反证据**（§3.3 已完整给出，此处不压缩）：

- 离散轨迹分类在真实二元数据上有解释力，且其有效性**依赖**状态数由 BIC 统计选出（`Anderson et al. (2010)`；`Williamson & Lavner (2020)`）——这既是**对项目的支持**（因为它证明离散层的价值在读出分类），也是**对「本体离散」的反驳**。
- 制度事实必须精确离散记录，把它们连续化会直接损害事实保真（`AGENTS.md` Representation-first invariant 3）。
- **假装连续比承认离散更危险**：序数当度量会产生方向颠倒的结论，而取平均不能修复、无可靠事后检出办法（`Liddell & Kruschke 2018`）。
- 存在成熟的、**有身份检验的**离散二元动力学方法线（L-APIM + Markov chain，A1/B1 限制下的 LRT 身份检验，显式拒收缺失；CRAN `dyadicMarkov`；`Böllenrücher et al. 2023, 2024`）——**它不是稻草人**。项目若要在文档里说「不用状态机」，最好同时说明为什么不采用这类方法。

**两侧不冲突，因为它们针对不同的对象**：相反证据几乎全部针对「**观测与制度事实的离散性**」；本节的建议针对「**把离散标签当作关系本体的状态空间并用它驱动转移**」。**本节的全部合法性建立在这个区分上；若这个区分被推翻，本节作废。**

### 9.2 强制性的事实条件

在进入四个位置之前，先把**强制性的**事实条件摆出来（全部已在正文给出，此处只做压缩引用，不重复论证）：

```text
FACT-1  没有任何一个框架在真实二元关系数据上有可接受的、可复现的动力学参数估计证据。
        锚点：ES = 0.09, I² = 76.0%（同步与关系结局）；14–38%（情绪互依超出 pseudo-couple）；
              阶数不可识别（AIC/BIC 系统性高估状态数）；r = .76（满意度秩序稳定性）；
              无拟合的连续关系模型（参数全部来自设定而非数据）。（§2.1；§2-F4；§2-F5）

FACT-2  唯一一个有真实数据支撑的「非线性阈值」发现（Bühler & Orth 2025 终末下降）
        是分段非线性连续读出，不是状态机：它的估计对象是单条满意度读数随
        time-to-separation 的函数。（§3.1-(1)；§8.1-(1)）

FACT-3  唯一一个 dyad 级「分岔」发现（Marín et al. 2014，19 对，n 极小）
        是由「满意度读数 + 离婚这一离散标签事件」定义的。（§6.2；§8.1-(3)）

FACT-4  迟滞在真实二元关系数据上的存在性目前未知（NEGATIVE_RESULT）；
        且它所必需的双向强耦合前提在多数真实 dyad 中不成立。（§5.3；§5.4）
```

**FACT-1 与 FACT-4 合起来强制一个结论**（`AI_DERIVED_CHARACTERIZATION`）：**任何离散层的位置，若要求它承担 `F` 的引擎角色，就必须先通过一个目前没有任何框架通过的证据门槛。** 因此本节的四个位置全部是「非引擎」位置。

**这不是因为离散不好，而是因为引擎角色所需的那一类证据现在不存在。** 若它将来出现，本节的判断必须重做——这一条已写成 §9.6-K8 与 K9。

### 9.3 四个候选位置：逐项判定

四张表的维度与 §2 的框架比较表保持一致（`维度 | 内容` 两列），但按本节的问题重排为八个必须回答的维度：**表示 / 转移规则 / 校准来源 / 二元方向性 / belief 与部分可观测 / 验证方法 / 复用价值 / 典型失效模式**。

#### 9.3.1 L-A 制度 / 协议事实层

| 维度 | 内容 |
|---|---|
| 表示 | 婚姻状态、订婚、同居、财产/监护安排、排他协议、居住安排、法定分居。`PARAMETER_CONVERGENCE_V0_1` P4 已 `KEEP` 的 `Relationship Identity / Agreement` = `{friend, exclusive romantic partners, engaged, married, open relationship, care arrangement}` 即属此层（`existing project constraint`） |
| 转移规则 | **无内生转移规则。** 取值由外部制度事件（登记、诉讼、签署、协议变更）改变；关系状态**更新**它，而不是它生成关系状态。这就是它满足 §7-O3 判据 (ii) 的方式 |
| 校准来源 | 外部制度/协议的**权威定义**：可被第三方（法院、登记机关、律师、对方当事人）判定真伪。这是 §7-O3 判据 (i)，也是本层唯一不可替代的合法性来源 |
| 二元方向性 | 本质是 **pair fact**（`AGENTS.md` rule 5：共享 pair 事实与有向状态分开记），因此**不区分 `i->j` / `j->i`**。但必须同时记录 `(jurisdiction, effective date)`：同一对 dyad 在不同法域或不同时点可取不同值（`AI_DERIVED_CHARACTERIZATION`） |
| belief 与部分可观测 | 对第三方**信噪比最高**：可被文书独立核实。但它对「当事人以为是什么」**完全不适用**——`married` 的法律事实不蕴含任何 belief 内容（§3.1-(4)：承诺与满意度可解耦，`Rusbult 1980`；`Tran, Judge & Kashima 2019` 给出三者的可分离 meta 相关强度） |
| 验证方法 | (a) 事实状态核对（文书/记录）——`AGENTS.md` Validation discipline 已要求 provenance quality 与 fact status 分开；(b) §7-O3 三判据逐条检查；(c) 在 Case Bank 中记为 **fact-status 测试**而非表示覆盖测试 |
| 复用价值 | 高：作为 `Constraint` / `Environment` 输入改变 `F` 的**可行域**；作为查询过滤条件；作为 §6.2 中「离婚」这一离散事件坐标。**它是四层中唯一跨本体稳定的一层**（不随关系理论修订而变） |
| 典型失效模式 | (a) 把制度事实当状态生成器（`legal separation` 一发生就断言状态跳变）；(b) 法域/时代漂移；(c) `ex` 由减法推出而非协议事实——这会把它偷偷变成 L-D 的投影（U16，§9.6-K3）；(d) 用 L-A 的枚举清单去定义 L-D 的取值 |

**判定（L-A）：合法，建议采纳为显式层。** 合法性完全落在 §7-O3 的三条判据上：(i) 外部权威定义；(ii) 被关系状态更新而非生成关系状态；(iii) 取值集合可穷举且不需随理论修订而增长。**引擎角色：明确不是。** 违反任一判据的值必须降级为 `Unknown` 或移出本层。

#### 9.3.2 L-B 观测者知识层（belief）

| 维度 | 内容 |
|---|---|
| 表示 | `Belief_i(A–B 是什么) ∈ {friend, partner, married, ex, unknown, contested}`——**关于认知主体的 epistemic 状态，不是关于关系本体的状态**。这是它合法的**唯一**理由（`existing project constraint`：`AGENTS.md` rule 2 把 `Belief` 与 `Agent | Relationship | Environment` 分列） |
| 转移规则 | 被 `Observation` / `Event` / `Action` 更新，被 `ActionPolicy` 读取。**不进入关系状态的转移方程**，除非显式建模 belief-dependent coupling——那是一个单独的 `model hypothesis`，当前 `NOT_ESTIMATED`（§7-O5） |
| 校准来源 | 主体自陈 + 交叉询问 + 与 L-A 的**一致性检查**（belief 与文书不一致 = `contested`；这不是错误，是数据） |
| 二元方向性 | **必须方向化**：`Belief_i` 与 `Belief_j` 是两个独立对象（`AGENTS.md` rule 4）。二者的分歧本身是本层最有价值的输出之一，且**不可**被压缩成一个 pair 级标签 |
| belief 与部分可观测 | 本层**就是** belief 层，因此它携带「A 以为是什么」而非「是什么」。**任何把 L-B 读作 L-A 的实现都是范畴错误**——这正是本层存在的理由 |
| 验证方法 | (a) belief accuracy：与 L-A/文书对照；(b) **增量预测检验**：给定 `X_t` 后加入 L-B 是否提高预测；(c) belief 与 action 是否经验可分离（U8 / §8.3-V6）——**目前 `UNKNOWN`**；若不可分离，`State != Action` 就没有经验基础 |
| 复用价值 | 高：deception / 知识状态研究（不越界，交 R08）；`contested` 状态是关系干预的直接抓手 |
| 典型失效模式 | (a) 把 belief 当事实——**最严重的一种，因为它在数据上不可见**：文书正确而 belief 错误时，只有本层能发现；(b) 阶数不可识别原样适用（`Pohle et al. 2017`：AIC/BIC 系统性高估状态数、不存在普适判据）；(c) label switching；(d) 把 `contested` 塌缩成多数方，从而删掉唯一的冲突信息 |

**判定（L-B）：合法，且 HMM / latent transition / GBTM 在这里是恰当工具，不是稻草人。** 这是它与 §2-F2 的关键差别：F2 的病是「离散状态**就是**关系本体」，本层没有这个病。**引擎角色：明确不是。** 边界条件：belief 潜类的类数选择、标签语义、以及 belief 与 coupling 的关系都 `NOT_ESTABLISHED`（§9.6-K4 给出检验与撤退条件）。

#### 9.3.3 L-C 测量模型层

| 维度 | 内容 |
|---|---|
| 表示 | 当观测是 Likert/序数类别时的 `ordered-probit` / cumulative-link / HMM emission：`P(y* < tau_k) = F(tau_k)`（§2-F10） |
| 转移规则 | `RawObservation -> CanonicalRepresentation` 的模型。**它作用于观测，不作用于关系状态。** 它甚至可以**反对**本体的连续假设 |
| 校准来源 | 序数方法学本身（`Liddell & Kruschke 2018`；`Bürkner & Vuorre 2019`；`Gambarotta et al. 2024`；`Ferr et al. 2025`）+ 具体量表的实际分布形状（U4：`UNKNOWN`，归 R03） |
| 二元方向性 | 逐坐标、逐方向地声明：`A` 对 `B` 的读数与 `B` 对 `A` 的读数**各自**声明其测量模型类型。**不允许先合并再声明**——合并会把方向信息与序数信息一起丢掉 |
| belief 与部分可观测 | 本层处理的是**测量误差与类别几何**，不是 belief。但与 L-B 的界线必须写清：`contested` 是 epistemic 状态（要建模），而「两人对同一题选了不同档」可能只是**测量噪声 + 真实差异**的混合——这一点在 Gate C 必须显式处理，不得默认归给任一侧 |
| 验证方法 | **无法事后验证**——这是本层最危险也最重要的一条：`Liddell & Kruschke 2018` 明确「不存在可靠的事后检出办法」。因此验证必须**前置**：每个序数坐标在进入 Gate A/B/C 之前先声明模型类型（`AGENTS.md` rule 11 的精神）。**这是本节唯一一条「必须先做」的层** |
| 复用价值 | 极高且**立即生效**：它是唯一一个「不做就已知会出错」的层。`0..1` 投影 + 度量模型 = 可能的方向颠倒（§3.3-R2） |
| 典型失效模式 | (a) 多个序数项取平均「修复」——**已被证伪不能修复**；(b) 强制等距；(c) 用连续指标代替类别；(d) 把测量模型的选择当成可由数据事后挑选的自由参数——那正是 `Gelman & Loken 2014` 的 forking paths |

**判定（L-C）：合法，建议采纳为强制前置声明。** 这是四层中**唯一一条「不做就已知会出错」**的层，因此它的正当性**不依赖**任何关于关系本体的理论主张——这一点使它成为本节建议中最稳的一条。**引擎角色：明确不是。** 条件：U4 未答前，L-C 的强制性范围 `UNKNOWN`（哪些主流量表受序数误用影响，取决于其实际分布形状，而非其自报量表类型）。

#### 9.3.4 L-D readout 层（现有但未显式化）

| 维度 | 内容 |
|---|---|
| 表示 | `friend / partner / married / ex` 等，作为从 `X_t` + L-A 事实 + L-B belief **导出**的粗粒化读数（§1 的 `Phi_j`） |
| 转移规则 | **派生量**，由 `Phi` 从连续/混合状态计算。必须标 `READOUT`；**必须显式声明不回流**为 `F` 的输入（除非采纳 §7-O6 的 `closed` 设定，且那是一个显式的建模决定，不是隐式默认） |
| 校准来源 | 制度事实（L-A）+ 主观读数轨迹（`Anderson et al. (2010)` 的 5 轨迹；`Williamson & Lavner (2020)`）+ 承诺/满意度解耦的经验结构（`Rusbult 1980`；`Tran, Judge & Kashima 2019`） |
| 二元方向性 | 读出必须声明它是 pair 级（`married`）还是有向级（`i 认为 j 是 partner，但 j 不这么认为`）。**把有向不一致压成 pair 标签会丢掉本项目最有价值的坐标之一**（`AGENTS.md` rule 4/5） |
| belief 与部分可观测 | 读出是**面向人**的产物，其定义必须写明它回答的是「事实问题」「A 的信念问题」还是「统计形状问题」——这三者给出**不同答案**，混用是本层最常见的错误 |
| 验证方法 | **增量预测检验**（§7-O1 的降级主张，§9.6-K1）：在任何数据集上，若给定底层状态后 label 序列**不提供**增量预测信息，则应正式承认 label 可作为**可接受的粗状态层**。**这是本节唯一一条能真正把项目立场推翻的检验** |
| 复用价值 | 高（人机接口、Case Bank 叙述、跨文档一致性），但**动力学复用价值 = 0**（按定义） |
| 典型失效模式 | (a) readout 回流（§7-O6）；(b) 把 readout 当本体（§3.4 第 4 点：这**是一个真正的解释权之争，而不是事实之争**）；(c) 用 L-A 的枚举清单去定义 L-D 的取值——这会让 L-D 退化为 L-A 的投影，丢掉全部读出信息；(d) 忘记 `belief` 分歧，使 L-D 看起来比 L-B 更「确定」 |

**判定（L-D）：合法，建议采纳并显式标注 `READOUT`**，同时补上 §7-O6 的不回流声明。**引擎角色：明确不是——但这是四层中唯一有可能在将来被升级为「可接受粗状态层」的一层**，条件见 §9.6-K1。

### 9.4 明确不推荐的三条（附理由）

❌ **把 `friend / partner / married / ex` 直接做成 `F` 的状态空间。** 三条并列理由：(a) 阶数不可识别（`Pohle et al. 2017`：AIC/BIC 系统性高估状态数、「不可能存在一刀切判据」；`van Havre et al. 2015`：额外状态的稳态分布可被压到任意小但仍非零）；(b) `Anderson et al. (2010)` 的 5 类有效性**依赖 BIC 统计**选择状态数，属读出分类而非本体离散；(c) 若离散化基于序数读出，会引入方向反转风险（`Liddell & Kruschke 2018`）。

❌ **用 HKB / extended HKB 直接参数化年尺度关系状态。** 三条并列理由：(a) 估计与亚稳态定义冲突（`Kelso 2012`：「这类度量基于平稳性假设，而协调动力学中的亚稳态字面上是一种平稳瞬态」）；(b) 耦合前提弱（同步与关系结局 `ES = 0.09, I² = 76.0%`；只有 14–38% 的伴侣情绪协动超出 pseudo-couple；`lovers > friends > strangers` 预期**未成立**）；(c) `arXiv:0911.0013` 是完整反面标本——把个体参数、时滞、Hopf 分岔写进方程后**只用仿真**区分 robust / fragile，**无任何数据拟合**。**这正是 LHRM 必须在 canonical 文本中显式禁止的做法。**

❌ **在任何未冻结 `F` 族之前使用 `attractor` / `hysteresis` / `regime` 措辞**（§7-O5/O7）。并且：**当前任何「实质阈值」主张在统计上都与「测量噪声 + 个体异质性 + 时间趋势」的替代解释不可区分**（`AI_DERIVED_CHARACTERIZATION`）。支撑这一点的四条已核实门槛批评：门槛移动本身无实质意义（`Gelman & Stern 2006`：「从一个 5.1% 显著性水平移动到 4.9% 就跨过门槛」）；`data-dependent analysis` / forking paths 使「我们找到了自然门槛」必须穷举自由度（`Gelman & Loken 2014`）；**测量误差不总是压低效应量**——因此「阈值处效应消失」几乎无法被确立（`Loken & Gelman 2017`）；构念的分布形状决定「高于/低于门槛」有没有内容（`Heck, Simons & Chabris 2018`）。

要解除这条限制，必须拿到三样东西中的至少样：**(a)** 更密的观测；**(b)** 客观/行为读数；**(c)** 明确的外生控制量扫描设计。

**并且必须把三条历史警告一起带上**（本节对「LHRM 引用阈值/相变/吸引子词汇」最直接的历史警告）：

- 突变理论在行为科学中的应用已被系统批评：`Sussmann & Zahler 1978`——「所谓灾变只是把『现实中存在不连续』这件事重述一遍；并没有真正用到深刻的数学结果……更好的、更简单的数学工具存在」。
- 其心理学检验法在方法学史上是一次**干净的失败**：Guastello 多项式法在**完全随机数据**上 `R²` 也可达 0.50，因而无法区分 cusp 与线性（`Alexander et al. 1992`）；Guastello 自己的反驳是随机数据 `R² = 0.55`、把 bifurcation/asymmetry factor 当已知可得近乎完美模型（`Guastello 1992`）——**两种做法都不能从该数据中识别 cusp 结构**。
- 突变模型拟合困难，需用 MSEM / regime-switching 绕过（突变模型作为横断面/纵向混合 SEM 的论文自述「突变理论流行度起伏，也招致相当份额的批评」）。

**调和（`Golubitsky 2010`）：数学本体（奇异性）本身有效，被误解和被夸大的是应用。** 因此 LHRM 可以合法地谈微分方程，但**不得**把「我们用了微分方程」当成经验支持。

### 9.5 §4 / §7 的障碍如何约束这四层

> **编号提示**：本报告有两套 `O` 编号——**§4.2/§4.3 的 O1–O5** 是动力学可识别性障碍（3 个可叠加障碍 + 2 个 LHRM 特有加重），**§7 的 O1–O8** 是 no-FSM 措辞审计项。**两套编号互不引用。本节显式区分，不做统一重编号**（重编号会改动既有正文，且会破坏已发布的前向引用）。

| 障碍 | 来源 | 对 L-A | 对 L-B | 对 L-C | 对 L-D |
|---|---|---|---|---|---|
| **O1 稳定性主导**（`r = .76`） | §4.2 | 弱：制度事实几乎不随时间在个体内波动 | 中：belief 的类特质成分同样吞掉方差 | 弱 | 强：读出的任何「变化」都须先排除个体均值漂移 |
| **O2 过程噪声 vs 测量误差不可分** | §4.2 | 弱 | 中 | **决定性**：本层就是这条障碍的解药 | 强 |
| **O3 状态数 / 参数数不可识别** | §4.2 | 弱：枚举由外部给定，不需估计 | **决定性**：HMM 阶数问题原样适用 | 中：阈值向量 `tau` 高度敏感 | 强 |
| **O4 观测密度（3–7 波 / 12–21 年）** | §4.3 | 弱 | 强：belief 的更新频率受观测窗限制 | 中 | 强：读出轨迹的形状只能估到组均值层面 |
| **O5 状态维度 × 个体数乘积** | §4.3 | 弱 | 强 | 弱 | 强 |
| **一致性要求未声明**（rule 9 ↔ 混合状态空间） | §7-O2 | — | — | **直接要求 L-C 逐坐标声明模型类型** | 同一要求也适用于 L-D 的取值来源声明 |
| **无可证伪转移律被冻结** | §7-O5 | — | 中：L-B 有 LRT 式身份检验可借 | — | — |
| **readout 回流未声明** | §7-O6 | 中 | 中 | — | **决定性：L-D 必须声明不回流** |
| **时间尺度未声明** | §7-O8 | 弱：制度事实跨尺度稳定 | 中 | 弱 | 中 |

**读法**：**决定性**的三格（L-C 的 O2、L-B 的 O3、L-D 的 O6）就是本节三个「必须显式声明」的技术要求；其余各格只影响优先级，不影响合法性。**没有一个格子支持把任何一层提升为引擎。**

### 9.6 可证伪条件与撤退条件

**这是本节真正的交付物。** 每一条都写成「若 X 则 Y」，使它可以被 reviewer 直接攻击，而不是被当作偏好接受。**当前九条全部处于未执行状态**；`NOT_ESTIMATED` 与 `UNKNOWN` 保持原状，不因本节而升级。

| 代号 | 检验 | 若成立 | 若不成立 | 当前状态 |
|---|---|---|---|---|
| **K1 · 增量预测检验** | 在满足 §4-O4 观测密度的数据上，给定 `X_t`（或给定 L-A + L-B）后，label 序列是否提供**增量**预测信息 | 若**不**提供 → 应正式承认 label 可作为**可接受的粗状态层**，L-D 升级，§3 的 readout 立场需在限定条件下重述 | 若提供 → 项目的「标签只是 readout」立场被削弱，须解释增量信息来自哪一坐标 | `NOT_ESTIMATED`（需 R16 的验证协议） |
| **K2 · 测量层强制性** | 关系科学主流量表的实际分布形状是否非等距 / 有天花板地板 / 多峰（U4） | 若是 → L-C 从「可选」升为「**必须**」，且**所有**把序数坐标当度量的既有结果必须重算 | 若否（近等距、近正态）→ L-C 仍建议保留，但不再是「不做就一定出错」 | `UNKNOWN`（归 R03） |
| **K3 · L-A 三判据检查** | §7-O3 (i)(ii)(iii) 逐条是否满足，特别是 `ex` 是协议事实还是 `married/partner` 的减法（U16） | 任一不满足 → 该值必须降级为 `Unknown` 或移出 L-A | 全部满足 → 保留在 L-A | `UNKNOWN`（归 R11 + R15） |
| **K4 · HMM 阶数稳健性** | 在 `Nagin & Odgers 2010` 的报告规范 + 敏感性分析下，belief 潜类数是否稳定 | 稳定 → HMM / GBTM 可作为 L-B 的默认工具 | 随样本变动（`Pohle et al. 2017`：不存在普适判据）→ **撤退**：L-B 退回有序/区间式 belief 表达，不使用离散潜类 | `NOT_ESTIMATED` |
| **K5 · 迟滞五判据** | §5.1 的 E1–E5 是否被**同时**满足 | 全部满足 → 才允许把 `hysteresis` 写入 canonical，且必须带 `empirical evidence` 标签 | 任一不满足 → 必须停在 `model hypothesis`。**当前连 E1（双向路径覆盖）在关系数据上都不存在** | `NEGATIVE_RESULT` + `UNKNOWN`（覆盖缺口见 §5.3） |
| **K6 · 阈值可分离性** | 在 (a) 更密观测 + (b) 客观/行为读数 + (c) 外生控制量扫描设计下，「实质阈值」是否可与测量噪声 + 个体异质 + 时间趋势分离 | 可分离 → 可主张 `Threshold-2` | 不可分离 → 任何阈值措辞必须标 `NOT_ESTABLISHED` | `NOT_ESTIMATED`。注意 `Bühler & Orth 2025` 的 terminal 起点是**持续时间区间估计**（0.58–2.30 年），**不是**水平跳变阈值，因此它与 Gelman–Stern 的批评**不冲突** |
| **K7 · 耦合前提检验** | 在关系数据上，双向耦合是否达到能产生分支的强度 | 达到 → 迟滞研究有物理前提，可设计 E1 的双向扫描 | 未达到 → 迟滞在多数 dyad 中**不是「还没测」，而是「前提不成立」**（§5.4 第 3 点） | 现有证据指向「未达到」（`ES = 0.09, I² = 76.0%`；14–38%；`lovers > friends > strangers` 未成立） |
| **K8 · 外部反驳条件** | `Kay & Hensler (2018)` 的结论（§8.3-V1） | 若核实为「稠密观测下离散状态优于连续 latent trait」→ **L-D 的定位需重做**，离散层可能必须升级为可被直接参数化的状态层 | 若不成立 → 本节不动 | `FETCH_FAILED` / `UNKNOWN`——**这是本节已知的最大单点脆弱性** |
| **K9 · 双稳态存在性** | 是否存在任何在真实 dyad 数据上估计出双吸引域 / 停留时间分布的同行评审研究（U1） | 存在 → §9.2-FACT-1 需修订，四层的「非引擎」论证需重做 | 不存在 → 维持本节结论 | `UNKNOWN`（归 R17 red-team + Wave 2） |

**整节的撤退条件**（必须写出来，否则本节就只是 quadruple confirmation）：

> 若 **K1** 与 **K8** 同时朝不利方向解决——即 label 序列在给定底层状态后**确实**提供增量预测信息，**且**稠密观测下离散状态被证明优于连续 latent trait——那么本节关于 **L-D** 的定位是错的：L-D 必须从 `READOUT` 升格为**可参数化的状态层**，而 §3.4 第 4 点的「解释权之争」将变成事实之争并以反方胜出。**本报告没有能力预判这一条，只能把它标出来。**

**次级撤退条件**：若 **K9** 为真（真实 dyad 数据上存在已发表的双稳态/吸引域估计），则 §9.2-FACT-1 作废，四层的「非引擎」定位需整体重做——**注意方向**：这会使「非引擎」变得**更难**成立，而不是更容易。

**K4 的撤退是唯一一个「不改变项目立场、只改变工具」的撤退**，因此它成本最低，建议优先执行。

### 9.7 本节建议与项目当前立场的关系（分类标注）

按 `AGENTS.md` Research discipline 的要求逐条标注。**本节没有任何一条是 `Human requirement`。**

| 陈述 | 类别 | 依据 |
|---|---|---|
| 离散层应存在，且应不止一层 | `AI recommendation` | 本节；其正当性论证依赖 §3.4 承认的四个边界 |
| 离散层**不得**作为 `F` 的引擎（**当前阶段**） | `AI recommendation`（论证）+ `existing project constraint`（约束） | 约束部分来自 `AGENTS.md` rule 8/9；论证部分来自 §9.2-FACT-1/FACT-4 |
| 制度事实必须以离散、可第三方判定的形式保留 | `existing project constraint` | `AGENTS.md` Representation-first invariant 3（保留原始证据/来源） |
| belief 必须与关系事实分开建模；有向 belief 独立 | `existing project constraint` | `AGENTS.md` rule 2 / rule 4 / rule 5 |
| 每个序数坐标必须声明其测量模型类型 | `AI recommendation`（其**理由**已是 `empirical evidence`：`Liddell & Kruschke 2018`） | §9.3.3；对应 §7-O2 |
| readout 不得回流为 transition 输入（默认 `open`） | `AI recommendation` | §7-O6 |
| 粗关系标签应留在 readout 层 | `AI recommendation`（**解释权之争**，非事实之争） | §3.1 vs §3.3；§3.4 第 4 点 |
| LHRM 的 `tau` 是月—年级，因而不采用 coordination dynamics 词汇 | `model hypothesis`（待 Architect 决策，U15） | §7-O8 |
| 迟滞 / 吸引域 / regime 在关系数据上存在 | `UNKNOWN`（是 `model hypothesis`，**不是** `empirical evidence`） | §5.3；§5.4；K5 |
| 「实质阈值」已在关系数据中被确立 | **否**（`NOT_ESTABLISHED`） | §9.4；K6 |
| 本节任何一层已被写入 canonical | **否** | 本文件是 `RESEARCH_CANDIDATE`；§8.4-C-15 |

### 9.8 交接

| 交给谁 | 本节的什么 | 为什么是它 |
|---|---|---|
| **R05**（identification） | K1、K4 | 这两条是本节唯一的判决性统计检验 |
| **R03**（measurement instruments） | K2、U4 | L-C 是否为「必须」完全取决于此 |
| **R11**（general human dyads） | K3、U9、U16 | L-A 的跨文化/跨法域语义等价性；`ex` 的操作方式 |
| **R16**（empirical validation protocol） | K1、K6 的实现；§6.2 的四种 restoration 判据 | 本节全部 `NOT_ESTIMATED` 项都需要一个验证协议才能变成可执行 |
| **R17**（red-team） | K5、K9、U1/U2/U14 | 本节最可能被推翻的两条是 K5 与 K9 |
| **R08**（belief/deception/knowledge） | L-B；U8 | L-B 的经验基础是「belief 与 action 是否可分离」 |
| **R00**（currentness）+ Wave 2 | U12（2024–2026 是否已有年尺度关系状态动力学成功估计） | 直接决定 K9 |
| **Architect** | U15（`tau` 尺度）；K3 的判据是否写入 canonical | 决策项，非研究项 |
| **本项目 Gate C** | U5 | 见下 |

**最后一件必须单独说的（`AI_DERIVED_CHARACTERIZATION`）**：**波动幅度**——「用增长曲线法从重复满意度评分提取 4 个预测因子（初始水平、线性趋势、**波动度**、平均水平）；波动幅度越大者关系越可能结束，即使控制平均水平后仍成立」，且波动者报告更低的 commitment（归 R01 / R02 + Gate C）——在本项目 schema 里**没有落点**。它既不是 L-A（不是制度事实），也不是 L-B（不是 belief），也不是 L-D（不是从状态导出的粗标签——它是一个**方差**量）。**这是本 lane 在离散层问题之外发现的一个可能的 `representation hole`**，与 `AGENTS.md` Validation discipline 中「record unmappable material as `MAPPING_FAILURE`」的处理方式一致：它应被记录，而不是被就近塞进四层中的任何一层。

**本节的收尾陈述**（与 §4.4 同级，可直接引用）：

> 离散层应当存在，而且应不止一层；但在**年度、自报、聚合观测**这一尺度上，**没有任何一层现在有资格充当 `F` 的引擎**，因为那类证据（可复现的动力学参数估计、可分离的阈值、双向路径覆盖）目前**全部不存在**。把这件事写下来，比让它隐式存在更安全。
