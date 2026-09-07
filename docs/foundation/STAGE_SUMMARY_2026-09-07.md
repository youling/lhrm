# LHRM 阶段性总结 — 2026-09-07

**Status:** Current research checkpoint  
**Scope:** Human–Human relationship modeling foundation  
**Purpose:** 将当前已较稳定的架构判断、外部成熟理论指针、未决假说与后续研究方向写回 durable SSOT，供继续研究、Agent 接力与未来论文写作使用。

> 本文件不是“最终理论”。它区分：`已较稳的项目边界 / 可复用成熟理论 / LHRM 当前架构判断 / 尚待验证的研究假说`。

---

## 1. 研究域与最小对象

LHRM 的研究域当前冻结为：

> **两个具体人之间的关系。**

最小研究单元：

```text
HumanDyad(i,j)
= Person_i + Person_j + Relationship_ij
```

关键边界：

- 不预设主体与客体是异性；
- 不预设关系从陌生人开始；
- 不预设关系以恋爱、婚姻或生育为目标；
- 允许朋友、亲属、同事、前任、配偶、第三者、敌对、违法/违反社会规范等现实存在的组合进入描述模型；
- 道德性、合法性、社会赞许度与关系强度分离建模；
- 动物、神经、遗传、生物研究只作为 **mechanism evidence**，不扩展 LHRM 的研究域。

研究原则：**向下追机制，但不向下扩研究对象；向外看社会环境，但保持 Human–Human Dyad 为最小关系查询单元。**

---

## 2. 当前世界模型与局部评价视图

### 2.1 世界层

当前较稳的底层表达是：

```text
WorldState(t)
= Agents(t)
+ Relationships(t)
+ Environment(t)
```

为处理现实中的误解、欺骗、未知与新信息，还必须承认：

```text
Reality != Observation != Belief
```

即对某个 Agent 而言，评价通常发生在其 **BeliefState** 上，而不是直接读取客观世界全状态。

世界变化由：

```text
Action / Event -> State Transition
```

产生。天气、失业、怀孕等更接近 external event；告白、隐瞒、照顾、背叛等更接近 agent action。它们改变 Person、Relationship、Belief 或 Environment state，而不要求为每种剧情新增一级本体。

### 2.2 `S / O / D / E` 的当前定位

早期：

```text
S -> O -> D -> E
```

仍保留，但不再宣称它是完整世界本体；当前将其解释为 **query-local evaluation view**：

- `S` — 当前评价主体；
- `O` — 当前被评价对象；
- `D` — 两人之间的关系状态；
- `E` — 当前问题相关的外部世界/社会环境。

这使第三者、父母、孩子、朋友等可以作为其他 Agents 存在于世界图中，而在具体查询中进入 relevant context。

### 2.3 Role 不可省略

同样的两个人在不同评价任务下没有唯一“匹配度”。

```text
Role = 当前到底在问什么
```

例如：短期性关系、浪漫伴侣、配偶、共同育儿者等会激活不同维度、偏好区域和约束。

---

## 3. 当前建模纪律

### 3.1 目标不是“物理最底层”，而是最小充分状态变量

LHRM 不以“拆到神经递质/基因”为基础性的判据。真正目标是寻找一个压缩状态：

```text
Z_t = (z_1, z_2, ..., z_k)
```

使得对 LHRM 关心的关系演化而言：

```text
P(FutureRelationshipState | FullReality)
approximately
P(FutureRelationshipState | Z_t)
```

因此候选变量应优先满足：**语义稳定、可操作定义、条件非冗余、对未来关系状态有额外信息价值。**

### 3.2 五类语义对象必须分开

当前统一使用：

```text
mechanism
primitive_state
observable_proxy
-derived_outcome
role_constraint
```

例如：

- “肯为对方花钱”通常先是 observable behavior / proxy；
- resource investment 可能是 latent/primitive candidate；
- commitment 可能与 investment 相关但不能先验等同；
- 某神经递质或脑区机制属于 mechanism，不能因为更微观就自动升级成 LHRM primitive。

### 3.3 不以统计低相关作为唯一标准

真正关注 **conditional redundancy**。候选参数至少接受：

1. semantic independence test；
2. counterexample decoupling test；
3. incremental-information test；
4. intervention-independence test。

两个变量即便人口统计上强相关，只要现实中可以稳定解耦且各自带来不同信息，就可能必须保留。

### 3.4 Missing 不等于 neutral / perfect

现实输入必须允许稀疏。未知信息保持 Unknown，通过先验/不确定性处理；不得为了公式完整把 Unknown 当成 0 偏离或完美匹配。

### 3.5 计算结果不必强制单值

当前明确拒绝把核心模型收缩成单一 `LoveScore` 或 `CompatibilityIndex`。

允许输出：

- 已知匹配项 / 已知不匹配项 / Unknown；
- 区间；
- 概率分布；
- 生存/风险曲线；
- 多种竞争解释；
- “当前证据不足以区分”。

原则：**Computable != Certain.**

---

## 4. LLM 应用方向（暂不冻结 UI）

LHRM 未来一个重要形态是 LLM Skill：

```text
Natural Language
-> semantic interpretation
-> proxy / observation extraction
-> map to canonical constructs
-> detect Unknown / ambiguity / contradiction
-> adaptive follow-up questions
-> LHRM inference / simulation
-> uncertainty-aware result
-> human-readable explanation
```

LLM 的定位：

```text
semantic interpreter
+ adaptive interviewer
+ result explainer
```

LHRM Core 的定位：

```text
canonical state semantics
+ inference/update rules
+ uncertainty
+ simulation/calibration
```

两者必须解耦，避免模型版本或 prompt 风格漂移改变 ontology。

一个重要未来研究方向是基于 expected information gain 的问题选择，而不是让所有用户填写固定长问卷。

---

## 5. 成熟理论 / 方法锚点（优先 REUSE / ADAPT）

以下不是 LHRM 原创。它们是当前认为足够 solid、值得长期保留查阅指针的理论或方法基座。这里只存 canonical pointer 和与 LHRM 的关系，不复制内容。

### 5.1 Social Relations Model — SRM

**用途：** 把人际评价分成 perceiver / target / relationship effect；与 LHRM 早期 `S / O / D` 直觉高度对应。  
**判定：** `REUSE / ADAPT`，不作为原创主张。  
**Pointer:** David A. Kenny, Social Relations Model overview: https://davidakenny.net/ip/srmip.htm

### 5.2 Actor–Partner Interdependence Model — APIM

**用途：** 处理 dyad 中 actor effect、partner effect 与双向相互影响，是后续真实双人纵向数据的重要成熟统计工具。  
**判定：** `REUSE`。  
**Pointer:** Cook, W. L. & Kenny, D. A. (2005). DOI: `10.1080/01650250444000405`

### 5.3 Investment Model / Interdependence tradition

**用途：** 区分 satisfaction、quality of alternatives、investment、commitment；提醒 LHRM 不要把“投入”“满意”“承诺”“持续关系”揉成一个状态。  
**判定：** `REUSE / construct benchmark`。  
**Pointers:**  
- Rusbult (1980), DOI: `10.1016/0022-1031(80)90007-4`  
- Rusbult, Martz & Agnew (1998), DOI: `10.1111/j.1475-6811.1998.tb00177.x`

### 5.4 Interpersonal Circumplex — Agency / Communion

**用途：** 大量 interpersonal behavior 可在 dominance/agency 与 affiliation/communion 两个近似正交轴上组织；是 LHRM 参数收敛时的重要“低维基准答案”。  
**判定：** `REUSE / challenge baseline`。  
**Pointers:**  
- Wiggins & Broughton (1991), DOI: `10.1002/per.2410050503`  
- Review pointer: https://onlinelibrary.wiley.com/doi/10.1002/9781118001868.ch4

### 5.5 Relational Models Theory — RMT

**用途：** 用 Communal Sharing / Authority Ranking / Equality Matching / Market Pricing 四种关系协调模式尝试统一社会关系；对 LHRM 的“少量 primitive + 组合生成复杂现实”很有启发，但不能把四模型当已证完备公理。  
**判定：** `COMPARE / ADAPT cautiously`。  
**Pointer:** Fiske (1992), DOI: `10.1037/0033-295X.99.4.689`

### 5.6 Ideal Standards Model

**用途：** 伴侣/关系理想不是单一“喜欢”，而可组织为若干理想维度和现实偏离；适合对照 LHRM 的 role-conditioned preferred region / deviation 思路。  
**判定：** `REUSE / ADAPT`。  
**Pointer:** Fletcher, Simpson, Thomas & Giles (1999), DOI: `10.1037/0022-3514.76.1.72`

### 5.7 Mate Evaluation Theory — MET

**用途：** 研究从初始吸引到持续关系中的 mate evaluation、person-specific information 与评价变化；是 LHRM 从静态对象属性转向互动/关系信息的重要 benchmark。  
**判定：** `REUSE / ADAPT`。  
**Pointer:** Eastwick, Finkel & Joel (2023), DOI: `10.1037/rev0000360`

### 5.8 Fourteen Core Principles of Close Relationships

**用途：** 关系科学自身做过一次跨理论整合，涵盖 relationship 是什么、如何运作、个体带入什么、context 如何作用；与 LHRM 当前“跨理论去冗余、统一接口”的目标高度相关。  
**判定：** `FOUNDATIONAL REVIEW / architecture benchmark`。  
**Pointer:** Finkel, Simpson & Eastwick (2017), DOI: `10.1146/annurev-psych-010416-044038`

---

## 6. 当前可能需要 BUILD 的部分

以下只是 **novelty hypotheses**，尚不能声称学术原创成立：

1. 一个跨关系类型的统一 Human–Human Dyad state ontology；
2. 将 everyday proxy language 编译到 canonical relationship constructs 的可验证语义层；
3. 将 Role、Belief、Unknown、partial observation 统一纳入关系评价接口；
4. 把成熟关系科学、dyadic statistics、动态系统、survival/probabilistic modeling 和 LLM adaptive interview 接到统一架构；
5. 用同一模型既支持具体二人交互式分析，又可向 microsimulation / agent-based social simulation 扩展。

是否构成真正贡献，必须等后续文献综述、形式化定义、实证验证和与现有框架直接比较以后判断。

---

## 7. 当前 Research Work Graph

Parent: `youling/lhrm#2`

并行研究：

- `#3` 游戏/人生模拟中的关系状态与可视化反向工程；
- `#4` 关系科学/认知神经/生物与计算项目中的基础构念；
- `#5` 婚恋/约会 App 中偏好、约束与代理变量反向工程；
- `#6` 社会现实/统计/极端案例中的 proxy decomposition 与压力测试。

当前策略：**先允许发散到足够深，再由 Project Architect 收敛。**

收敛顺序：

```text
cross-source merge
-> semantic de-duplication
-> proxy / primitive / mechanism classification
-> redundancy & double-counting audit
-> adversarial coverage audit
-> candidate minimal sufficient state set
```

---

## 8. 为未来论文保留的研究 provenance

从现在开始，重要阶段性 artifact 应尽量保留以下信息：

- Human 原始研究问题与范围变化；
- 关键 architecture decision 及其前一版方案；
- 外部理论/方法来源及 `REUSE / ADAPT / BUILD / REJECT` 判定；
- 被否决的构念、公式和原因；
- extreme/adversarial cases；
- Research Agent findings 与 Architect 最终裁剪之间的差异；
- 后续形式化定义、数据集、参数估计、验证与失败结果。

未来若形成论文，优先把贡献写成：

> **问题定义 -> 已有理论碎片 -> 统一架构 -> 构念收敛方法 -> LLM 交互式测量 -> 实证/仿真验证**

而不是从“提出一个万能爱情公式”开始。

---

## 9. 当前 checkpoint 结论

当前最稳的方向不是继续发明更多术语，而是：

> **寻找一组跨性别、跨亲缘、跨关系类型、跨阶段仍具有稳定语义的最小充分 Human–Human relationship state variables；成熟理论和数学工具尽量复用，LHRM 专注于统一状态语义、观测/信念接口、动态更新与可验证的集成架构。**

本 checkpoint 之后，继续等待 #3–#6 深入研究结果，再做第一次正式 parameter convergence。