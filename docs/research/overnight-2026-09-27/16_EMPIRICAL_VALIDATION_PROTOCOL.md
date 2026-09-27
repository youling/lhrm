# 16 号 — 候选经验验证协议（Candidate Dataset-to-LHRM Mapping / equation-validation protocol）

**Status:** `CANDIDATE FOR ARCHITECT REVIEW` — 非 canonical，不修改任何 canonical doc
**Date:** 2026-09-27
**Lane:** R16（Wave 1，repair pass；**join lane**）
**Parent:** `youling/lhrm#30@overnight-opencode-exploration-swarm-v1`
**对应 issue:** `youling/lhrm#29`（`Empirical Validation Lane v0.1`，2026-09-14 建，state open，0 comments）
**零数据接触:** 本报告**未打开任何数据文件**。所有变量名与字段语义来自 R04 已审计的官方文档/结构，或来自本 lane 独立抓取的一页条款正文。

> **Round-3 记账：`16` 是 `JOIN LANE`，不是一等交付 lane。**（依 dispatch 的 delivery-accounting 要求 + R-D11）
> **本报告 38 行内容（§12 的 21 行 + §13 的 17 行）是 `05` / `06` / `R17` 的转录件，
> 加上 §7.1 中来自 `06` 的 null 模型定义。⇒ 它们不得被计为"本协议交付了 38 项"。**
> **本协议真正的首要交付物是 `F-SELF19` / `F-SELF20` / `F-SELF21`**（见 §12 顶部的重新标注；
> `F-SELF20` 的答复逐字是 **"None."**）。逐项记账表见 §12 顶部。

> **三条读前须知。**
> 1. 本协议是 `#29` C / D / F 三层的**操作化草案**。它不改写 `#29` 的分层，也不主张改写。
>    **Round-3 记录（保留上文，不改）：** `#29` D 层的公式相对 `CURRENT_ARCHITECTURE` 属
>    **`EXPIRED_RELATIVE_TO_CURRENT_ARCHITECTURE`**。⚠ **记账限定：** 本轮**未打开** `#29` 的 D 层正文
>    （`NOT_OPENED`），因此**本报告不指名**哪些公式已过期；记录的是**状态**而非清单。
>    **后果（工程性的）：** 任何规格若**引用** `#29` D 层的公式作为依据，必须**先**与当前 canonical 对齐，
>    不得把 `#29` 的 D 层公式当作现行接口使用。这一条**不**改写 `#29` 的分层。
> 2. 本协议**不含**任何参数拟合、阈值选择、权重表、归一化公式。§8 的映射表是**模板**，不是已完成的规格。
> 3. §9 给出的**可执行性判定是负面为主**的。本协议今天能完整跑通的只有一条路径（判定 E2）。

---

## 0. 本报告的一句话形式

> 在任何 LHRM 关系方程被允许接触一个 holdout 观测之前，必须先把「这个方程用的是哪个数据集的哪个版本、哪些变量、这些变量在什么层与哪个方向上、它们在多大程度上只是 proxy、它们以什么单位、什么时间被观察、谁在什么时间知道什么」写成一份可被第三方逐行审计的映射规格；把六类泄漏逐条排除；把任何候选方程必须击败的 null 集合先写死；把「不确定度以 dyad 为单位、且 fold 间 SE 不被信任」写进报告规范；最后把以上全部内容连同代码 commit hash 一起封存，之后才允许看 holdout 的第一行。

---

## 1. 标记约定

每条规则带两个字段：

**`rule_class`** ∈ `Human requirement` | `existing project constraint` | `AI recommendation` | `empirical evidence` | `model hypothesis`

**`basis`** ∈ `CITED`（有 DOI / 官方 URL） | `PROJECT`（repo 内指针） | `ISSUE`（issue 编号） | `JOIN_LANE`（sibling lane） | `DESIGN_CHOICE`（**无外部支持的设计选择，因此可被推翻**）

`DESIGN_CHOICE` 不是免责声明，是本协议的**可修订性声明**：凡标此者，Architect 可直接推翻而不需要先找到反证。

---

## 2. 数据对象与版本固定（`R16-ID01` – `R16-ID12`）

| Rule | 内容 | `rule_class` | `basis` |
|---|---|---|---|
| `R16-ID01` | 绑定 `dataset_ref@version` = `dataset_ref` + `release_version` + `retrieved_on` + `codebook_version` + `weight_variable`。任一缺失 → 不得进入 freeze。 | `AI recommendation` | `DESIGN_CHOICE` |
| `R16-ID02` | `unit_of_analysis` 必须显式取自 `PERSON_WAVE / PERSON_DYAD_WAVE / DYAD_WAVE / DYAD_DAY / DYAD_EVENT / DYAD`。 | `empirical evidence` | `JOIN_LANE: R05 SD8` |
| `R16-ID03` | `dyad_id` 必须是发货的。若由分析者重建，所有 `i->j` / `j->i` 方向性主张自动降级为 `MODEL HYPOTHESIS`。 | `empirical evidence` | `JOIN_LANE: R04`（SOEP / IFLS 反例） |
| `R16-ID04` | `side`（A/B）的语义必须结构性：anchor/partner、coupleid 派生方、进入关系早/晚者、发起/回应方、id 字典序（仅当无实质方向时）。禁止按变量名 / row order / 性别角色硬编码。 | `existing project constraint` | `PROJECT` `CURRENT_ARCHITECTURE.md` §4 + `CONSTRUCT_SCOPE_DIRECTIONALITY.md` §2；白名单 `AI recommendation` / `DESIGN_CHOICE` |
| `R16-ID05` | **Side-swap 检验（强制）**：任何 `DIRECTED_EDGE` 构念的模型对 `i` / `j` 标签置换必须结构不变。置换后结论改变 → 作废并记 `F-SIDE`。 | `AI recommendation` | `DESIGN_CHOICE`；必要性由 `JOIN_LANE: R06 F3/F4` 间接支持 |
| `R16-ID06` | `wave_id` 必须同时携带 `event_time`（参考区间）、`fieldwork_window`、`wave_index`。`wave_index` 不得当作物理时间差；滞后陈述必须写"相隔 `k` 个 `wave_index`、实际 `Δ` 天/月"。 | `empirical evidence` | `JOIN_LANE: R05 I12` + `R06 F9` |
| `R16-ID07` | 回忆与历史分支必须与测量时间分离记账：至少 `recording_time` / `event_time` / `publication_time` + `knowledge_time_by_agent`。 | `existing project constraint`（叙事侧） | `PROJECT` Fixture 003 §2 / freeze rule 2 |
| `R16-ID08` | 密集窗长度随 wave 变化时，wave 不可直接比较；`diary_window_length` 须写入 `unit_of_analysis` 行。 | `empirical evidence` | `JOIN_LANE: R04 D03`（HARP 10 天 → 8 天） |
| `R16-ID09` | 单方 respondent 模块（SHARE 的 `fin_resp` / `fam_resp` / `hou_resp`）的全部变量标 `directionality_class = UNDETERMINED`，禁止进入 `DIRECTED_EDGE` 主张。 | `empirical evidence` | `JOIN_LANE: R04 D02` |
| `R16-ID10` | 抽样框不等价写进数据集头部（不只是脚注）。HARP：同性组约 70% 经登记处邮寄、异性组因该登记处限制改用城市名单约 40%。 | `empirical evidence` | `JOIN_LANE: R04 D03` |
| `R16-ID11` | **`FREEZE_RECORD` 不得包含个体级数据行。** 只允许结构与规格、聚合统计、指针三类内容。逐行审计须在合规环境内部进行，结论以聚合形式回写。 | `existing project constraint`（由条款与 `AGENTS.md:24` 派生）；工程形式 `AI recommendation` | `CITED`（S24）+ `PROJECT`（`AGENTS.md:24`） |
| `R16-ID12` | ⭐ **Round-3 新增：`person_id` 必须是可寻址的，且必须可判定"同一 person 是否出现在多个 `dyad_id` 中"。** 若出现，则该 person 的**全部** dyad 整块落在同一侧（L3 (d)）。`FREEZE_RECORD` 字段 4 必须记录 `person_id` 的确切变量名及其发货状态；若 person 层不可寻址（例如数据只发 `coupleid` 而把两侧 person 键都做了假名且不可跨 dyad 联结），则**所有 person 层独立性主张一律标 `PERSON_NONIDENTIFIABLE`**，且 `R16-UC01` 的重抽样单位必须写明是 dyad 而非 person。 | `AI recommendation` | `DESIGN_CHOICE`（本协议自拟的阻断规则）**+** `JOIN_LANE: R05 SD8` + `R05 §4 M2`（del Rosario & West 2025 Principle 1b）作为动机 |

---

## 3. Mapping status 受控词表

### 3.1 六个成员

| # | 成员 | 判定条件（全部满足） | 存在理由 | `rule_class` / `basis` |
|---|---|---|---|---|
| 1 | `DIRECT_ITEM` | (a) 原始题项/字段自身即该构念的操作化；(b) 有方向标签；(c) 有官方 codebook 条目；(d) 不含任何分析者做的算术组合。 | 唯一允许被表述为"工具在测这个构念"的级别。R03 F10 是正面先例：`PPR` 判为 `DIRECT_PROXY`（对 `PPR_(i about j)`），并被明令**不得**用来推断 `ResponsiveAction_(j->i)` —— 工具测的是知觉而非行为。 | `AI recommendation` / `DESIGN_CHOICE`（分级思路由 J03 4 级分类启发） |
| 2 | `DERIVED_COMPOSITE` | 由 ≥2 个 `DIRECT_ITEM` 经**官方文档记载的**计分规则合成的 index / factor / sum / latent score；规则必须可被第三方逐字复现。 | 合成量一旦被当作构念本体，就隐藏了它内部的题项数、不确定度与加权。必须**同时**报出组成题项清单与各自信度。R03 F9 的 RCI 是标准反例：total α=.62–.66 而 Frequency 分量 α=.56。 | `AI recommendation` / `DESIGN_CHOICE`；RCI 依据 `JOIN_LANE: R03 F9 / N8` |
| 3 | `BEHAVIORAL_PROXY` | 被观测的是**行为、决策、痕迹或机构记录**，不是自陈。必须记录观测环境与该行为的机会结构。 | `CURRENT_ARCHITECTURE.md` §6 的 `State != Action` 在数据侧的落点。R04 D04：速配的 `dec` 是**决策变量**，R04 明文警告"把它当'attraction 的观测'是模型假设，不是证据"。 | `existing project constraint`（P03 §6）+ `JOIN_LANE: R04 D04` |
| 4 | `COVARIATE_ONLY` | 可合法进入模型作为**控制、调节或时间变量**，但**不得**被计为该构念的证据。 | 承载 P02。若不单列，制度事实会被静默升格为关系状态 —— `AGENTS.md` 明令禁止。**这是对 `#29` 词表最实质的扩展请求。** | `existing project constraint` / `PROJECT` P02 |
| 5 | `NOT_MAPPED` | 无法给出**任何**可辩护的候选构念。**必须**附 `why`（无工具 / 构念在数据中不存在 / 只有 pair 级而无方向 / 抽样框不含该情境 / 构念本身未定义）。 | 把"拿不到"与"用不上"分开命名比事后解释更诚实。R03 的 instrument gap G1–G10 是高频来源。 | `AI recommendation` / `DESIGN_CHOICE`；`JOIN_LANE: R04 §3.2` + `R03 §2.3` |
| 6 | `CONFLICTED` | 存在 ≥2 个同样可辩护的候选构念，**或**该构念的实证文献本身互相矛盾。必须附 `conflict_refs`。 | 第 4、5 级都假设"正确答案存在"。R03 记录：Rempel 三维 trust 结构至今未被系统再验证（2025 年重做发现反向措辞方法因子）；ECR-R 自身的方法效应可把理论上正交的 anxiety–avoidance 相关从 .17 推到 .41（"两维度正交"是工具假象）；权力/依赖族 38 个量表各用 1–2 次、无一成为主流。 | `AI recommendation` / `DESIGN_CHOICE`；依据 `JOIN_LANE: R03 F8 / N3 / N6 / N7` |

### 3.2 第二个正交必需字段：`directionality_class`

`mapping_status` 单独不足以决定该变量能否支持方向性主张。R03 F1 记录：ECR / ECR-R / ECR-SF / RSQ / AAS / AAQ / WTC-Trait / VFI / HISD / 3VDI / Interpersonal Dependency / Personal Sense of Power / Reiss RPS / Romantic Beliefs Scale **全部测 `i` 的一般倾向或对一般他者的态度**，target slot 结构上为空。

```text
directionality_class ∈ {
  DIRECTED_EDGE, TARGET_LEVEL, AGENT_LEVEL, PAIR_LEVEL, UNDETERMINED, NON_SEPARABLE
}
```

| 值 | 依据 | `rule_class` / `basis` |
|---|---|---|
| `DIRECTED_EDGE` | R03 F2（Liking 侧几乎唯一"有 directed + 陌生人 dyad 有效性"的族）+ R04 D04（速配是"最好的方向性非对称公开样本"） | `JOIN_LANE: R03 F2` + `R04 D04` |
| `TARGET_LEVEL` | P04 §1 分解式中 target facet 独立存在 | `PROJECT` P04 §1 |
| `AGENT_LEVEL` | R03 F1（ECR 官方语言是 trait）+ F5（SDI-2 三因子中两个与"特定 j"无关） | `JOIN_LANE: R03 F1/F5` |
| `PAIR_LEVEL` | P02 + P03 §4（`PairState_(i,j)`） | `PROJECT` P02/P03 |
| `UNDETERMINED` | R04 D08（NSFH 配偶关系质量单方报告 → `Z[i→j]` 与 `Z[j→i]` 不可分离）+ R04 D02（SHARE 单方 respondent 模块） | `JOIN_LANE: R04 D08/D02` |
| `NON_SEPARABLE` | R03 F9（生理同步结构上无法分解为 i→j 与 j→i；与结局关联方向矛盾：交感 ES=+.19 / 副交感 ES=−.21 / 总体 ES=.09 且 I²=76%；2026 年 *Nature Reviews Psychology* 综述称其心理意义"仍然含糊"；Gates et al. (2015) 发现 couples' RSA 同步与自报婚姻冲突**正相关**） | `JOIN_LANE: R03 F9` |

**`DIRECTED_EDGE` 是最稀缺的资源。** R03 F1 + R04 D04 合起来意味着：在 R04 审计的 16 个数据集中，**只有 1 个**（速配）提供无外部假设的 `DIRECTED_EDGE` 双分量，而它没有第二个时间点。

### 3.3 与 `#29` 四值词表的对齐（须 Architect 裁决）

| `#29` 值 | 本协议映射 | 说明 |
|---|---|---|
| `DIRECT_PROXY` | `DIRECT_ITEM` **或** `BEHAVIORAL_PROXY` | `#29` 把"题项直指"与"行为代理"合成一级；本协议拆开，因为 P03 §6 的 `State != Action` 要求二者在数据层不可混。**拆分是 `AI recommendation`。** |
| `NOISY_PROXY` | 上述任一 + `CONFLICTED` 标记 | `#29` 的 "noisy" 描述**信度**；`CONFLICTED` 描述**构念身份争议**。二者正交 → 两个字段。 |
| `DERIVED` | `DERIVED_COMPOSITE` | 一致 |
| `UNMAPPED` | `NOT_MAPPED` | 一致 |
| （无对应） | **`COVARIATE_ONLY`** | **`#29` 缺。** 没有它，制度事实只能被塞进 `DIRECT_PROXY`，**直接违反 P02**。 |
| （无对应） | **`CONFLICTED`** | **`#29` 缺。** |

### 3.4 第三个字段与不确定性块

`evidence_channel` 直接复用 R15 的受控表 `{DIRECT, TESTIMONIAL, DOCUMENTARY, INFERRED, ILLEGAL_OBSERVATION, ABSENT}`（`JOIN_LANE: R15 §5.2`），**不新造**；理由是 L6 需要它判定同源性。

```text
uncertainty:
  estimated_uncertainty      : 官方 reported SE / reliability / design effect → 填值 + 出处，否则 UNKNOWN
  measurement_error_known    : yes | no | partial
  floor_ceiling_risk         : yes | no | unknown
  missingness_mechanism      : MCAR_assumed | MAR_assumed | MNAR_sensitivity_done | UNKNOWN
  invariance_level_tested   : configural | metric | scalar | strict | partial | alignment_only | NOT_TESTED
```

`invariance_level_tested` 不得默认为 `NOT_TESTED` 而不显式标注（R05 I8 / SD3；S21 提供 5 步法教程与该问题被系统性忽略的证据）；`floor_ceiling_risk` 依据 R05 SD14 + R03 N8；`missingness_mechanism` 依据 R05 I13。

### 3.5 ⚠ Round-3：三组枚举**不是**封闭受控表（`NOT_CLOSED_AS_WRITTEN`）

> **依 R-D10**（`D-C21` / `D-C22` / `D-C23`）。**本节是记账修正，不新增任何构念、不改任何 canonical。**
> Round-1 形态把这三组枚举呈现为封闭受控表（§17 的"6 值 `mapping_status` + 6 值 `directionality_class` + 5 字段 uncertainty 块"）。
> **它们不是。** 下表逐组写明**究竟缺什么**——不是笼统的"可以更完善"。

| 组 | 被呈现为 | **究竟缺什么（逐条）** | 缺了会怎样 |
|---|---|---|---|
| **`mapping_status`**（§3.1 的 6 个成员） | 封闭受控表，六值互斥且穷尽 | **(1) 互斥性未声明。** `DERIVED_COMPOSITE` 与 `CONFLICTED` 在现实中**可同时为真**（一个合成分数同时存在构念身份争议）；`DIRECT_ITEM` 与 `COVARIATE_ONLY` 也可同时为真（一个题项既是某构念的直接操作化，又是制度事实的载体，例如 `relstatus` 类字段）。表未说明这是**单值**还是**可并存的多值**字段。<br>**(2) 缺一个真实存在的值：`SELF_REPORTED_EDGE`。** §3.2 的 `DIRECTED_EDGE` 只覆盖"工具**直接**测 `i→j`"（`R03 F2` + `R04 D04`）。但"**`i` 自陈**对 `j` 的有向状态"是本项目最常见的一类字段，它既不是 `AGENT_LEVEL`（不是一般倾向），也不是 `PAIR_LEVEL`，也不是 `UNDETERMINED`（`dyad_id` 与方向是**已知的**）。它现在是**无值可填**。<br>**(3) 缺 `BELIEF_ABOUT_EDGE` 与 `DIRECTED_EDGE` 的区分位置。** `PPR_{i→j}`、`Ideal_{i→j}`、`Affirm^k_{i←j}` 都是**关于边的信念**，不是边。当前只能用 `directionality_class = DIRECTED_EDGE` 填写，会让**信念与状态混进同一格**——这正是 `F-SELF20`（basis 瞄错相空间）在数据侧的落点。<br>**(4) 缺"不适用"轴。** X-5 / C-P5 已裁决适用性是与值域**正交**的元数据（`APPLICABLE \| NOT_APPLICABLE_BY_RULE \| APPLICABILITY_UNKNOWN`）。三组枚举**都没有**这一轴 ⇒ "该构念在此 dyad 中不适用"目前只能被塞进 `NOT_MAPPED` 的 `why`，与"没有工具"混为一谈。 | 分析师遇到自陈有向边时**被迫二选一**：或把它写进 `DIRECTED_EDGE`（虚增 `DIRECTED_EDGE` 的稀缺性，与 §3.2 末句冲突），或写 `NOT_MAPPED`（把"有数据"记成"没工具"）。两种都错。 |
| **`uncertainty`**（§3.4 的 5 个字段） | 封闭受控表，五字段穷尽 | **(1) 缺独立轴 `reliability_class`。** `estimated_uncertainty` 把三样不同的东西塞进一格：官方 reported **SE**（抽样不确定度）、**reliability**（构念分数的信度）、**design effect**（复杂抽样）。三者的**取值域、单位、可比性**都不同。`measurement_error_known ∈ {yes, no, partial}` 又与它们**不正交**：`partial` 既可能是"有 SE 无 reliability"，也可能是"有 reliability 无 SE"。⇒ **必须拆出独立 `reliability_class` 轴**（候选值：`REPORTED_ALPHA \| REPORTED_OMEGA \| TEST_RETEST_DONE \| NOT_REPORTED \| NOT_APPLICABLE`），并把 `estimated_uncertainty` 拆成 `se_type ∈ {ANALYTIC_SURVEY_SE, MODEL_BASED_SE, NONE_REPORTED}` + 取值 + 出处。<br>**(2) 缺"已量化 vs 未量化"的第三态。** 现在只能写 `UNKNOWN`，而 `UNKNOWN` 混合了"官方未报告"（**数据事实**）与"我们没查"（**本 lane 的无知**）。这两者的行动后果不同：前者要求换数据 / 找 codebook，后者要求去查。<br>**(3) `floor_ceiling_risk` 的取值不完备。** `yes \| no \| unknown` 缺 `not_assessable`（例如该构念是序数类别，floor/ceiling 概念不适用）。<br>**(4) 五字段不覆盖 `R16-UC05` 要求的第三件套。** `R16-UC05` 要求 `estimate + uncertainty + evidence`；本块有 uncertainty，**没有 evidence / provenance 字段**（`evidence_channel` 是**另一张表**的字段，二者未在表结构上绑定）。 | `L6`（同源性）与 `R16-UC01`（dyad 层区间）都依赖这五字段。字段混合 ⇒ 无法机械判定"信度是否已报告"，因而 `L6` 的 `CMV_CONFOUNDED` 分支**不可执行**。 |
| **`directionality_class`**（§3.2 的 6 个值） | 封闭受控表，六值互斥且穷尽 | **(1) 缺 `SELF_REPORTED_EDGE`。** 同上：`i` 对 `j` 的自陈有向状态是本项目最常见的可填情形，**当前无值**。<br>**(2) 缺 `BELIEF_ABOUT_EDGE`。** `PPR_{i→j}` / `Ideal_{i→j}` / `Affirm^k_{i←j}` 是关于边的信念，`R03 F1` 已记录主流工具测的是"一般倾向"（→ `AGENT_LEVEL`），但**没有值**给"针对特定 `j` 的、关于这条边的信念"。当前只能误填 `DIRECTED_EDGE`。<br>**(3) `UNDETERMINED` 与 `NON_SEPARABLE` 不互斥。** `UNDETERMINED`（R04 D08/D02：单方报告 ⇒ 方向不可分）描述的是**证据来源**；`NON_SEPARABLE`（R03 F9：生理同步）描述的是**构念本身**。一个"单方报告的生理同步"同时两者皆真，表未说明优先级。<br>**(4) 缺"方向被设计性固定但无实质内容"的值。** `R16-ID04` 允许 `side` 由"id 字典序"派生（"仅当无实质方向时"）。此时方向**在技术上可填、实质上是任意的**，与 `DIRECTED_EDGE` 不同、与 `UNDETERMINED` 也不同。 | `R16-ID05`（side-swap 强制检验）以 `directionality_class` 为前提。若该字段无法诚实地填 `SELF_REPORTED_EDGE` / `BELIEF_ABOUT_EDGE`，则 side-swap 检验要么被跳过（丧失其唯一目的），要么在错误的分类上执行。 |

**Round-3 的最小可执行提案（供 Architect 裁决；本 lane 不实施）：**

1. `mapping_status` 改为**可并存的多值**字段（每值带独立 `why`），或明确声明单值并给出优先级序。
2. `directionality_class` 增加 `SELF_REPORTED_EDGE` 与 `BELIEF_ABOUT_EDGE` 两个值，并声明 `UNDETERMINED` / `NON_SEPARABLE` 的优先级。
3. `uncertainty` 拆出独立的 `reliability_class` 轴与 `evidence_provenance` 绑定（与 `evidence_channel` 结构上绑定，不另起一表）。
4. 三组枚举全部**并列**一条适用性轴（X-5 / C-P5 的 `APPLICABLE | NOT_APPLICABLE_BY_RULE | APPLICABILITY_UNKNOWN`）。

**不主张：** Round-3 **不**主张上述四个值或四个轴已被接受，也**不**主张原三组枚举"错误"。
Round-3 只主张：它们**不是封闭表**，且缺口的**具体形状**已被逐条写明。

---

## 4. Leakage 规则 L1–L8

**定义。** 采用 S01 的用法：leakage 指"任何使 holdout 评估比真实泛化更乐观的信息通道"，并采用 S02 的公式化框架。

> **Round-3 记账：L1–L8 的地位。**（**本条 `R-D11` 中无对应项**——`R-D11` 讲的是 `F-SELF19/20/21`；
> 本条的依据是 dispatch Track R3-A 的 delivery-accounting 要求 + `X-6` 的"不主张已被验证"原则）
>
> **被取代的原文（逐字保留）：** *"L1–L8 是**本协议的实例化**，**不声称**复现 S01 的八分类（S01 图 1 确切标签未取得；对应关系标 `DESIGN_CHOICE`）。"*
>
> **为什么两句不能并存（这是本轮要修的核心矛盾）：** "本协议的实例化" 蕴含 L1–L8 是某个**已知分类学**的
> 完整实例；而"不声称复现 S01 的八分类" 意味着那个分类学的标签**从未取得**。
> **二者不能同时为真。** Round-3 的诚实形式是：
>
> - **L1–L8 是本协议自行构造的、**非穷尽**的 leakage 规则集。** 它们的来源是 §6 的划分逻辑
>   （dyad / time 两轴 + dyad 分组）与 §8 的映射表，加上 `R05 SD1–SD20`，**不是**任何已取得的外部分类学。
> - **与 S01 / S02 / 任何外部分类的对应关系 = `NOT_ESTABLISHED`。** S01 图 1 的确切标签未取得
>   （§14 第 5 条非主张**继续有效**）。**"八条"这个数字不是"八分类"**，它不主张任何完备性。
> - **L1–L8 ↔ S01 的八分类映射：`NOT_OPENED`。** 本轮未打开 S01 正文以核对分类；
>   因此**不存在**一条可被引用的"L1 对应 S01 的哪一类"的映射。任何声称该映射的文本都是编造。
> - **§17 原有的一句被取代：** *"8 条 leakage 规则每条带真实引用"* ⇒ 见下方引用状态说明。
>
> **引用状态（Round-3 逐条标注）：** 下表 `依据` 列是**指针 / 书目清单**，
> **不是"该规则所依赖的内容陈述已被核实"的证明**。
> **本轮未核实任何 leakage 规则的 claim-to-source 绑定 ⇒ 整体标 `NOT_OPENED`。**
> §16 的 `CITED_PRIMARY` 列表只表示**书目**（作者/年份/卷期/DOI/URL）已核实，
> **不表示**每条规则赖以成立的那句引文已被逐字比对。这一区分在本轮之前是**隐含的**，
> Round-3 把它**显式化**：书目核实 ≠ 内容核实。
> **后果：** `L1`–`L8` 目前是**设计选择（`DESIGN_CHOICE`）的合理集合**，
> 而**不是**已被文献逐条验证的规则集。`FREEZE_RECORD` 不得把它们记为 `empirical evidence`。

| id | 名称 | 定义 | 为什么是 leakage | 依据（`NOT_OPENED`：claim-to-source 未核实） |
|---|---|---|---|---|
| **L1** | 构念跨 split 泄漏 | 若构念 `k` 的任何测量出现在 calibration 侧**且** outcome 的定义/采集/派生也依赖 `k`，则该 holdout 上任何 `k` 相关结论无效。**(a)** outcome 不得由 `k` 的函数定义。**(b)** 若 `k` 只有一个工具而它同时充当 predictor 与（直接或间接）criterion → 报 `NOT_IDENTIFIABLE`，不是报一个系数。 | criterion contamination；更根本地，跨 `t` 比较同一构念前必须先有测量不变性，而不变性失败与真实变化在观测上不可区分 | `JOIN_LANE: R05 I8/SD3` + S21 + S01 |
| **L2** | 派生量含结果 | 任何 `DERIVED_COMPOSITE` 或分析者构造的派生量，若其构造步骤**读取了** outcome 所在时点或之后的数据 → leakage。**禁止**从 outcome 所在 wave 及之后回溯计算任何 predictor 的标准化参数、缺失填补参数、PCA/因子载荷或降维基底。 | S02 的定义；S01 的 civil-war 复现表明全部宣称复杂模型胜过 LR 的论文都因 leakage 无法复现，**修复后复杂模型不再有实质优势** | S02（`10.1145/2382577.2382579`）+ S01（`10.1016/j.patter.2023.100804`） |
| **L3** | dyad 级泄漏 | 若同一 `dyad_id` 的任何行（任何 wave、任何 side）同时落入两侧 → 无效。**必须** dyad 分组划分。**(a)** 随机效应结构必须在划分**之前**按 "keep it maximal" 定好（S12）。**(b)** 置换推断必须在**最大可交换区块**内进行；对二人数据该区块 = dyad（S13）。**(c)** dyad 内两成员的残差协方差必须显式建模（R05 M2 引 del Rosario & West 2025 Principle 1b）。**(d) ⭐ Round-3 新增：person 级非独立。** 若同一个 `person_id` 出现在**超过一个** `dyad_id` 中（再婚 / 多个伴侣 / 家庭面板中同时是配偶与父母 / 速度配对中一人被多次抽到），则**该 person 的全部 dyad 必须整块落在同一侧**。理由：dyad 分组只保证"一个 dyad 不跨侧"，**不**保证"一个人不跨侧"；一个人在两侧各出现一次，就把该人的稳定特质（基线、依恋风格、报告风格）带过划分——命中 `R05 SD1` 的结构条件，与 `L3` 原有的 (c) 同源，只是**层级更高**。**(e) ⭐ Round-3 新增：共享估计器泄漏。** 若用于给 holdout 打分的任何**估计量**（标准化参数、填补参数、因子载荷、降维基底、IRT 曲线、可靠性权重、codebook 派生的取值域）是从**含 holdout** 的数据上估的 → 无效。**(f) ⭐ Round-3 新增：site / cohort / 机构级泄漏。** 同一招募点、同一队列、同一机构、同一施测窗口批次若跨两侧，则场地效应与队列效应跨划分（`R16-ID10` 已记录抽样框不等价的实例）。 | 一个 dyad 的两行不是两次独立观测；**一个人也不是两次独立观测**（Round-3 (d)）；一个从 holdout 学到的估计量会把自己的答案带进 holdout（Round-3 (e)） | S12 + S13 + S05 + `JOIN_LANE: R05 SD8 / M2` |
| **L4** | 时间泄漏 | **(a) 跨波**：`Z(t)` 的任何 predictor / 标准化参数 / 模型选择 / 缺失填补 / 因子载荷只能用 `≤ t` 的信息。**(b) 递归**：outcome 在 `t+h` 时 holdout 前沿必须是 `t` 而非 `t+h-1`。**(c) 回忆**：回溯生命史变量必须携带 `recording_time`；事后追问"后来发生的事"的问项不得当作 `t` 时刻状态。**(d) 前瞻性题项**：在 `t` 施测但内容指向 `t+1` 之后的题项须显式标 `FORWARD_LOOKING`。 | 随机切分时间序列给出系统性乐观的性能估计；ILD 对时窗设计有具体要求 | S06 + S22；叙事侧先例 `PROJECT` P06（"Legal conclusions after para 23 are future leakage"）/ P07 |
| **L5** | informant / 报告者泄漏 | **(a)** 由 `i` 提供的关于 `j` 的报告，**不得**同时充当 `Z[k,i,j,t]` 与 `Z[k,j,i,t]` 的测量或共同证据。**(b)** 单方报告的关系状态题（NSFH）**不可分离**为两条有向边 → 所得"不对称"必须标 `REPORT_ASYMMETRY`，**禁止**解释为状态不对称。**(c)** 两侧分数同时入模时必须报 "partner effect" 而非 "influences"（Kashy & Cook 2005 脚注 1）。**(d)** 若 partner report 在校准集上对 actor report 无增量，必须把 `NO-PARTNER`（`B3`）作为**真实竞争模型**。 | S23 报告 **actor-reported 变量预测的方差是 partner-reported 的 2–4 倍**，且 individual differences 与 partner reports 在 actor-reported 关系变量之外**没有预测效应** → 把 partner report 当独立证据通道很可能只是在测"谁更在意监测"。R05 I3：SRM 的 accuracy 成分需要 round-robin，两人 dyad 不满足 | S23（`10.1073/pnas.1917036117`；结论 `JOIN_LANE: R17 F2` / `R06 F1`）+ S11 + `JOIN_LANE: R05` |
| **L6** | 同源题项复用 | 若 predictor 与 criterion（或其任一合成量）**共享题项、共享施测场合或共享 respondent** → 报 `CMV_CONFOUNDED`，并**必须**同时报告 (i) 一个不共享来源的对照估计，和 (ii) common-method variance 的量级估计或对其为零的敏感性分析。 | S10；R03 F11 给出直接量化：PRQC 的 trust 分量与 satisfaction .58 / commitment .38 / intimacy .47 / passion .14 / love .48 —— **只有 passion 与 trust 明显可分（.14）**；R03 F11 结论"低冗余验收门不能只在自我报告数据上做" | S10 + `JOIN_LANE: R03 F11` |
| **L7** | holdout 自适应复用泄漏 | **(a)** holdout 只能被查看**一次**。**(b)** 看到结果之后发生的分析决定必须记入 deviation log、其结果一律标 `EXPLORATORY`、**不得**用于 confirmatory 主张。**(c)** 若确需自适应，必须改用带隐私预算的可复用 holdout，或改走 `B6` 的 multiverse 路径。**(d) ⭐ Round-3 新增：四条实现条款（见 §4.1；原文只有 (a)–(c)，是**备忘录条款**而非制度条款）。** | S07：holdout 结果一旦被反馈进设计决策，其有效性即被侵蚀；出路是加差分隐私噪声或用带隐私预算的可复用 holdout。⚠ **S09 的 89% vs 4% 标 `NOT_OPENED`**（Hussey & Hughes 的来源语境本轮未打开）——**该数字不得承担论证重量**；L7 的成立**只**依赖 S07 的机制陈述 | S07 + S08 + S09 + S16 + S17 + S18 ⚠ **整体 `NOT_OPENED`**（claim-to-source 未核实，见本节顶部）|
| **L8** | 选择 / 流失泄漏 | 若 holdout 入选概率依赖 outcome 或其代理（attrition、分层抽样、幸存者条件化样本）→ 性能估计非无偏。**必须** (a) 报 attrition 表；(b) 报至少一个 MNAR 敏感性分析；(c) 对条件于事件的样本显式标 `OUTCOME_CONDITIONED_SAMPLE`。 | HARP 的 couple 层留存 T1→T3 = 268/419 ≈ 64%（≈36% 流失），T3 因留存压力把日记由 10 天减到 8 天；CLOC 的随访对象是**丧偶者 + 匹配对照**，是条件于丧偶的样本 | `JOIN_LANE: R04 D03/D09` + `R05 I13` |

### 4.1 `L7` 的实现条款（Round-3 新增；依 `F-SELF11`："防 leakage 是**制度**问题而非**备忘录**问题"）

> **为什么必须补：** 原文 (a)–(c) 全是**规则陈述**。规则不指定**谁**持有什么、**记在哪里**、
> **偏离了会怎样由谁发现**。在没有任何制度性安排的情况下，(a)–(c) 可被完全满足而 L7 仍然发生
> ——因为"查看一次"是**一个动作**，而**动作没有被登记的地方就等于没被限制**。

| # | 条款 | 内容 |
|---|---|---|
| 1 | **holdout 凭证的持有者（credential holder）** | holdout 的读取凭证由**一个被指名的角色**独占持有，该角色**不得**是执行分析的人。`FREEZE_RECORD` 字段 2（`rights_and_processing_mode`）与字段 16（`deviation_log`）必须写明**该角色**。⚠ 若因 `R16-ID11`（rights）导致无法分离执行者与持有者，则必须**如实登记这一冲突**，其代价是 L7 **不可执行**（⇒ 全部 holdout 结论标 `EXPLORATORY_ONLY`）。**不得**用"我们信任分析师"替代凭证分离。 |
| 2 | **访问日志（access log）** | 每次对 holdout 行的读取必须留下**追加式（append-only）**记录：时间戳、读取者角色、读取的**范围**（行数 / wave / 字段类别）、请求理由。日志必须与 `FREEZE_RECORD` 同一不可变 artifact 家族，且**先于**读取存在（不可事后补写）。 |
| 3 | **可审计的偏离记录（auditable deviation record）** | `deviation_log`（字段 16）必须满足：(a) 追加式，不可编辑、不可删除；(b) 每条含**时间戳 + 偏离内容 + 是否影响主判据 + 签署角色**；(c) 偏离**发生**与偏离**被登记**之间的延迟本身是违规项（"看了但先做事后补记" = L7 已发生）；(d) 日志的**完整性**必须能被**第三方**核对（若受 `R16-ID11` 限制，则按 §11.2 (d) 记录"谁在什么环境核对过 + 结论 hash"）。 |
| 4 | **若确需自适应（adaptation is required）** | 唯一合规的三条出路，**必须择一并在 `FREEZE_RECORD` 登记**：<br>**(i)** 加差分隐私噪声的**可复用** holdout（S07 的机制性出路）；<br>**(ii)** 放弃 confirmatory 主张，全部结果标 `EXPLORATORY`，并把该 holdout 从 confirmatory 证据链中移除；<br>**(iii)** 换一个新的、未被查看过的 holdout（**重新采集或重新划分**），并把原 holdout 的全部查看记录**原样保留**在 artifact 中。<br>**默认是 (ii)。** 特别地：**不得**以"我们已经记在 deviation log 里了"为由继续使用自适应后的结果做 confirmatory 主张——S07 描述的侵蚀机制**不因被记录而停止**。 |
| 5 | **与 `FZ-1` 的关系** | (1)–(3) 的执行者与 §11.2 (c) 的 `FZ-1` 持有者是**同一个角色**。若两者不是同一人，则**必须**记录"分析者与凭证持有者之间的信息通道"，因为 L7 的侵蚀可以经由该通道发生。 |

**L1–L8 的联合判定规则。** 任一 `R16-LK*` 触发 → 该 (方程, holdout) 组合的结论**降级为 `EXPLORATORY`**，并在报告中点名触发的是哪一条。**不得**通过"事后修正分析"来清除一次触发（那本身就是 L7）。
**Round-3 补一条例外（针对 `L7`）：** 若 L7 的**实现条款**（§4.1 (1)–(3)）任一条不成立，
则该 (方程, holdout) 的结论**不是** `EXPLORATORY`，而是**作废**——因为无法证明看过几次。

---

## 5. Outcome 定义

| Rule | 内容 | `rule_class` / `basis` |
|---|---|---|
| `R16-OC01` | 每个 outcome 写成五元组 `{ outcome_id, source_variable_or_event, observation_window, estimand_class, censoring_status }`，`observation_window` 必须是**区间**。 | `AI recommendation` / `DESIGN_CHOICE` |
| `R16-OC02` | `estimand_class ∈ { DESCRIPTIVE, PREDICTIVE, CAUSAL }`，三者**不得混写**。R05 S21 FAQ 原文："we should distinguish between descriptive, predictive, and causal research questions"；R05 I16 指出规范性判断不属于这三类。`#29` E 层的 `Y = g(StateTrajectory, Query, Role)` 是 PREDICTIVE / readout 层。 | `empirical evidence` / `JOIN_LANE: R05 I16`；与 `#29` 一致性为 `PROJECT` P08 |
| `R16-OC03` | **关系终止不是缺失，是设计性删失。** R06 U-3 称之为"本次 lane 发现的**最重要的数据收集方式盲点**"（Round-3 依 **R-D7** 改词：原措辞为"**最重要的结构性盲点**"——被取代的原文逐字为"结构**性**盲点"，改词理由见 `06 §10 U-3` 的 Round-3 块）：离开的人停止了作答，终止事件不是可处理的缺失，任何关于"关系最重要的一次转移"的律用受访者数据都**不可证伪**。以 breakup/divorce 为 outcome 的方程必须标 `CENSORING_BY_DESIGN`，**不得**把未观测到终止读作"未终止"。 | `empirical evidence` / `JOIN_LANE: R06 U-3`（**Round-3 改词：severity 由"结构性"改为"数据收集方式的限制"**） |
| `R16-OC04` | 制度性 outcome（离婚、分居、再婚、同居起止）必须**与关系状态 outcome 分开登记**。依据 P02。同时记录 S23 的负面证据：客观关系变量（同居状态、约会 vs 已婚、有子女）作为**对质量的预测因子**几乎无用，唯一例外是关系长度 → 这不是"制度事实无价值"，而是"不要把它们当质量 predictor"。 | `existing project constraint`（P02）+ `empirical evidence`（`JOIN_LANE: R17 F2` 第 4 条） |
| `R16-OC05` | 任何 outcome 的**事件率**必须在 freeze 之前从 calibration 集估计（只需知道量级），否则不得进入 freeze。理由：R05 SD12（power 随效应类型差 1–2 个量级）+ S04（n=100 时误差带 ±10%）。 | `empirical evidence` |

---

## 6. Split 纪律：必须在 dyad 级**与** time 级**同时**切

### 6.1 为什么两个轴都不可省

```text
只切 dyad、不切 time
  → 留出 dyad 的所有 wave 都在 holdout，calibration 侧见过同一数据集的
    time 结构、施测节奏、缺失模式、季节性、施测窗口长度
  → 若 holdout 判定涉及任何跨波比较（几乎所有 LHRM 方程都涉及，因为
    CURRENT_ARCHITECTURE.md §6 的核心就是 X_(t+1)=F(...)），模型在
    calibration 上已经"知道"了后波次的分布形态
  → 严格意义上不是 leakage，但是**乐观偏差**，方向与 L4 相同

只切 time、不切 dyad
  → 同一 dyad 的 t 期在 calibration、t+k 期在 holdout
  → 这是最危险的一种：它把"这个 dyad 本身"当成了泛化测试
  → dyad 的稳定特质（基线状态水平、冲突风格、社会阶层）跨越划分
  → 命中 R05 SD1（把 person 间相关当 person 内动态）的结构条件
  → 命中 S05（层级结构数据必须用 blocked CV）
```

> ### ⚠ Round-3 撤回的推论：`⇒ 默认几何 = dyad 分组 × 时间前向`
>
> **被取代的原文（逐字保留）：** *"⇒ 默认几何 = dyad 分组 × 时间前向，二维同时施加"*
> 以及 §6.2 表中 `G1_BLOCKED_FORWARD` 的适用栏：*"**首选默认**。需 ≥3 wave（pairfam 14 / SHARE ≥8 / HARP 3 满足）"*
>
> - **判定：`UNSUPPORTED`**（`REJECTED_OR_WEAK_FINDINGS.md` **R-D8**，依据 `D-C24`）。
> - **两条独立的反对理由：**
>   1. **`G1` 逐字意义上就是本节自己称作"最危险的一种"的那一种。** 本节 `只切 time、不切 dyad`
>      段落说"它把"这个 dyad 本身"当成了泛化测试"；而 `G1` 的定义是"calibration 侧 = **该 dyad** 的全部
>      `≤ t_last-1` wave" ⇒ **被留出的那个 dyad，它自己的早期波次就在 calibration 侧**。
>      于是 calibration 侧**已经见过**每个 holdout dyad 的 time 结构、缺失模式与结局先兆。
>      `G1` 因此**不是**"dyad 永不跨侧"，它是"**在 dyad 内部**做时间前向切"。
>   2. **`G1` / `G2` / `G3` 三者中没有任何一种实现"一个 dyad 永不跨侧"。** 三者都让同一个 `dyad_id`
>      同时出现在两侧（`G3` 更明确：逐个留出 dyad，但"每个留出 dyad 内部再做时间前向切"）。
> - **后果（必须被写明，因为它是本条最重的部分）：** `G1` 作为"首选默认"**静默地把默认 estimand
>   从"**在 dyad 之间泛化**的转移律"降级为"**同一 dyad 内的时间外推**"。
>   这是一次**未被声明的 estimand 降级**：读者从"二维同时施加"会读出双轴泛化，实际得到的是单轴。
> - **正确的几何本来就在本文件里**——§6.1 代码块的 `只切 dyad、不切 time` 分支，
>   加上 §6.3 降级表的「**仅 dyad**」行（*"只能主张 **cross-dyad generalization**，且只能主张 `t` 恒定下的截面表现"*），
>   已经写出了它的**主张上限**；只是它**从未被放进 §6.2 的几何表**。
>   Round-3 把它作为 `G4` 补进去（见 §6.2），并把 `G1` 从"首选默认"降级为**带标签的降级几何**。
> - **不主张：** 本条**不**主张 `G1` 无效。`G1` 是一项可用、合法、且在某些问题上**正是所需**的几何
>   （例如"这个 dyad 的下一次互动会怎样"）。Round-3 只主张：**它不是默认，且用了它就必须贴降级标签。**

### 6.2 四种可采纳的几何

| 几何 | 定义 | 实现"dyad 永不跨侧"？ | 实际 estimand | 适用 | `rule_class` / `basis` |
|---|---|---|---|---|---|
| **`G4_DYAD_PURE_FORWARD`**（**Round-3 新增；默认**） | ① 把 `dyad_id` 划分成 calibration dyads / holdout dyads，**两侧不相交**；② 在两侧**各自**按同一个全局时间边界 `t*` 切：holdout = `wave > t*`，calibration = `wave ≤ t*`；③ holdout 评估时，对每个 holdout dyad，用**它自己**的 `≤ t*` 波次（这些波次**全部在 holdout 侧**，从未进入 calibration）作为历史，预测它 `> t*` 的波次 | **是。** 任一 `dyad_id` 的**全部**行都在同一侧 | **cross-dyad 泛化的 within-dyad 时间预测**（两轴同时真正被检验） | 数据同时满足"dyad 数足够"与"每个 holdout dyad 在 `t*` 之后仍有观测"。⚠ 代价：holdout 侧的有效 n 是 **`n_holdout_dyads`**（`05 SD8`），不是 `n_dyads × n_waves` | `AI recommendation` / `DESIGN_CHOICE`；依 R-D8 + `05 SD8` |
| `G1_BLOCKED_FORWARD` | 按 `dyad_id` 分组做 holdout 组；每组内 holdout 时刻固定为**最后一个有观测的 wave**；calibration 侧 = 该 dyad 的全部 `≤ t_last-1` wave | **否** | **within-dyad 时间外推**。⚠ **用了它必须标 `WITHIN_DYAD_TEMPORAL_EXTRAPOLATION_ONLY`，且不得主张 cross-dyad 泛化** | 需 ≥3 wave（pairfam 14 / SHARE ≥8 / HARP 3 满足）。**Round-3：由"首选默认"降级为带标签的降级几何** | `AI recommendation` / `DESIGN_CHOICE`；依据 S05 + S06 |
| `G2_ROLLING_ORIGIN` | 多个 holdout 起点，每起点各自重新分组；等价于 rolling-origin CV | **否** | **within-dyad 时间外推**（同 `G1`，须同标签） | 数据稀疏、wave ≥4 时；给出"随 horizon 变化"的曲线 | `AI recommendation` / `DESIGN_CHOICE`；依据 S06 |
| `G3_LEAVE_ONE_DYAD_OUT_FORWARD` | 逐个留出 dyad，每个留出 dyad 内部再做时间前向切 | **否**（定义上即"内部再切"） | **within-dyad 时间外推**（同 `G1`，须同标签） | dyad 数足够（须在 freeze 时用 S04 的误差带规则算过） | `AI recommendation` / `DESIGN_CHOICE`；依据 S04 + S13 |

**几何选择的记账规则（Round-3 新增）：**

1. **默认几何 = `G4_DYAD_PURE_FORWARD`。** `FREEZE_RECORD` 字段 7 必须写明所选几何 + **该几何的实际 estimand**。
2. **只能用 `G1` / `G2` / `G3` 时**，必须 (a) 在字段 7 旁附 `WITHIN_DYAD_TEMPORAL_EXTRAPOLATION_ONLY`；
   (b) 在报告正文**点名**"本文不主张 cross-dyad 泛化"；(c) 说明为什么 `G4` 不可用（通常是
   "holdout dyad 在 `t*` 之后无观测"或"holdout dyad 数不足"）。
3. **降级标签与 §6.3 的关系：** §6.3 的三行是**轴不可用**时的上限；本节的几何是**轴可用时怎么切**。
   两者必须**同时**记录：选了 `G1` 之后，若同时只有单一时间轴可用，则标签是**两条**（几何降级 + 轴降级）。
4. **明确不主张：** 本节**不**主张 `G4` 在任何现有数据集上都可行。它是**默认**，而"默认"在
   2026-09 的数据现实下很可能立刻落到第 2 条。这一点必须**如实写进 `FREEZE_RECORD`**，不得默认掉。

**明确不采纳**：随机 k-fold over（dyad × wave）行（命中 L3 + L4）；只按 wave 随机切分 wave 内记录（命中 L3）；用 time 切分但把同一 dyad 固定在两侧（命中 L3 + `R16-ID12` 的 person 级阻断，见 §4 / L3(d)）。

### 6.3 只有一轴可用时的诚实降级

| 可用轴 | 主张上限 | 降级标签 |
|---|---|---|
| 仅 dyad | 只能主张 **cross-dyad generalization**，且只能主张 `t` 恒定下的截面表现 | `NO_TEMPORAL_AXIS` |
| 仅 time | 只能主张 within-dyad 的时间外推，**不得**主张 cross-dyad 泛化 | `NO_DYAD_AXIS` |
| 两轴皆无 | 只能主张描述性分布，**不得**主张任何预测或转移 | `DESCRIPTIVE_ONLY` |

R04 有一条**必须被引用**的总约束：

> 本审计**未发现**任何「完全公开 + 双报告 + 方向性 + 多波 + 关系状态构念」的数据集。**这四个条件的交集为空。**

> **Round-3 记账（依 `X-14`：`C-C29` `CONTESTED`）。** 上述引文中的
> *"**这四个条件的交集为空**"* 后面紧跟的 *"这是本 landscape 最重要的结构性事实"* 是一步
> **未被取样框架支持的 field-wide existence claim**，**Round-3 不采纳该读法**。
> **取代后的读法（本文件此后一律使用）：**
> **"在 R04 **被结构检验的 15 个数据集**上，四条件的交集为空；
> 另有一个数据集（`D12 / Add Health`）是被**许可**条件而非结构条件排除的，
> 因此『Add Health 从未进入结构检验』是一个**已被检查的候选反例**，不是已确立的领域事实。"**
> 逐字保留 R04 自己的限定句：*"本审计**未发现**"*（这是检索范围表述，**成立**）。
> **唯一被取代的是"因此这是领域结构性事实"那一步推理。**
> ⚠ 连带：`§10 F-03` 的 "四条件交集**为空**" 同样按此读法降级为**本次检索**的结构性结果。
> ⚠ **计数区分（勿混）：** R04 审计的**数据集总数是 16**（§3.2 的"16 个已审计数据集中只有 1 个提供 `DIRECTED_EDGE` 双分量"用的是 16）；
> **被结构检验的是 15**（`D12` 未进入结构检验）。**16 ≠ 15，两个数字各有其指。**

（`JOIN_LANE: R04 §4 矛盾 9`）→ 因此在 2026-09 这个时间点，`G1/G2/G3` 中只有 `G1` 在原则上对 pairfam / SHARE / HARP 可用，而 `#29` F 层要求的**跨数据集泛化**在**本次检索的范围内**不可执行（见 §10 `F-03`）。R04 D04 是"仅 dyad 轴"的教科书案例：速配数据"只能标定 t=0 的方向性，**不能标定任何转移律、任何持续性、任何路径依赖**"。

---

## 7. Baseline / null 模型

### 7.0 `主判定规则`（Round-3 改写；依 `X-6` / `C-P10`）

> **被取代的原文（逐字保留）：**
> *"**主判定规则**：候选方程必须在**同一个 holdout、同一套划分、同一批 null** 上，**配对地**击败 `B1`（persistence）与 `B2`（selection-only）。只击败 `B0` 不算。"*

**Round-3 改写为三条：**

1. **固定条件不变**：候选方程与 null 必须在**同一个 holdout、同一套划分、同一批 null** 上比较。这一条**不变**。
2. **配对击败 `B1`（`AR_ONLY`）是通用硬规则。** 只击败 `B0` 不算。这一条**不变**。
3. **`B2_STABLE_LEVEL` 是按需选用的诊断基线，不是通用的"每个候选必须配对击败 B1+B2"硬规则。**
   逐字理由（§7 开头那段「主判定规则」在 HEAD `16:168` 的隐含推论已被否决）：**不得**主张 `B2` 在**所有报告口径**下被 `B1` 严格数学支配。
   **保留的辩护空间（`EV3` 正确指出的一点，本轮采纳）：** 若 `B1` 与 `B2` 报告的**量不同**
   （例如 `B1` 报 holdout 预测误差、`B2` 报**方差成分分解**），则"配对击败"在**报告层**仍携带信息
   ——两个量不在同一标尺上，支配关系无从谈起。**因此本协议不把 `B2` 写进通用硬规则。**
   `B2_STABLE_LEVEL` 在**相关时**（即该候选方程的报告口径包含 level / intercept 解释）被选入 `null_set`，
   选入与否必须**写进 `FREEZE_RECORD` 字段 9 并给出理由**。

### 7.1 Baseline / null 注册表

| id | Null | 定义 | 为什么被列入（**不再声称它"击败过"任何东西**） | 依据 |
|---|---|---|---|---|
| `B0` | `MARGINAL_RATE` / grand mean | 只用 outcome 的边际分布（或聚类后 dyad 均值）预测 | 下限地板 | `DESIGN_CHOICE` |
| `B1` | `AR_ONLY` / persistence | 只用 `Y(t)`（或该 dyad 的历史均值）预测 `Y(t+h)`；不含任何 partner 侧或环境侧信息 | R06 判 C：若 `AR-ONLY` 与完整模型无实质差异，该律**退化为自回归 → 拒绝**该律作为独立律族，只保留为 readout。R06 F2 记录了可复用的设计模板（LCM-SR on both partners） | `JOIN_LANE: R06 §4.8 判 C / F2`；`R05 SD7` |
| **`B2_STABLE_LEVEL`** | **`STABLE_PER_DYAD_INTERCEPT`（random-intercept-only；稳定 per-dyad 截距，无 wave-to-wave 增量）** | 每 dyad 一个随机截距（估计自 calibration），**只有**该截距，**不含任何时间变化的增量项**。**本 null 不再叫 `SELECTION_ONLY`。** | **Round-3 全部改写（依 `X-6` / `C-P10`）：** (a) **改名**：`B2` → `B2_STABLE_LEVEL`；**停止**使用 `SELECTION_ONLY` 这一名称（该名称在 `16` 与 `06 §6.3` 指向**两个不同的模型**，是 PR 内最危险的一处同名异义）。(b) **删掉三处措辞**：*"本协议认为最重要的一条 null"*、*"因为它已经击败过一个候选"*、R06 N1 的 *"对律 C 的已核实证伪"*。(c) **角色降级**为**按需选用的诊断基线**（见 §7.0 第 3 条），**不是**通用配对硬规则。(d) **不得**主张 `B2` 在所有报告口径下被 `B1` 严格支配（见 §7.0）。 | `DESIGN_CHOICE`（定义）+ `JOIN_LANE: R06 §6.3 第 1 条`（模型同构） |
| **`B8_LEVEL_PLUS_RW`** | **`LEVEL_PLUS_RANDOM_WALK`（`Level + 随机游走 + 误差`）** | `E(τ) = Level(τ₀) + 随机游走 + 误差`。**与 `B2_STABLE_LEVEL` 是两个不同的 null**：随机游走给出**随机变化的增量**，随机截距不给出。 | **Round-3 新增为独立命名 null（依 `X-6`：*"Keep R06's Level+RW competitor as a distinct null"*）。** 混淆这两个是 §7.0 改名动作要消除的**同一个**错误。**它是 `B2_STABLE_LEVEL` 的必要对照**：若候选方程的增量项相对随机游走没有增量，则"增量"这一说法本身未被识别。 | `JOIN_LANE: R06 §6.3 第 1 条` 原文 |
| `B3` | `NO_PARTNER` | 移除全部 partner 侧信息，保留 actor 侧与时间结构 | R06 显式非主张 5："**不主张 partner 效应存在。S04 是'在现有效度下 partner 效应可能近似为零'的证据。`NO-PARTNER` 竞争模型在全文中被当作真实对手。**" S23 提供经验合理性 | `empirical evidence` / `JOIN_LANE: R06 非主张 5` + S23 ⚠ `PENDING_EVIDENCE_CHECK (R3-E3)`（S04 = Joel et al. 2020，正在复核；本行**不依赖**其结论，`B3` 作为真实对手的理由是 R06 的非主张，与 S04 的内容无关） |
| `B4` | `MEASUREMENT_NULL`（lag-0 联合模型） | 把同构念的 `t` 与 `t+1` 在**同一模型内联合**估计 | R06 §4.9：若符号对、效应在联合建模 lag-0 时消失，说明 `Z` 与 `PPR` 是**同一测量**而非两层；**修正方向是合并，而非各留一个 primitive**。这是一个"击败即推翻模型结构"的 null | `JOIN_LANE: R06 §4.9` |
| `B5` | `LABEL_BASELINE` | 只用 coarse 关系标签（`marital status` / `cohabit` / `duration` / `has children`）预测 | 直接检验 LHRM 核心主张：双有向坐标是否比制度事实**多**提供了什么 | `existing project constraint`（P02 的推论）+ `AI recommendation`；动机 `JOIN_LANE: R17 F2` |
| `B6` | `MODEL_UNCERTAINTY_FLOOR` | 整族合理规格全跑一遍，报告**分布**而非点估计 | R05 SD18 引 S31 原文："model uncertainty had almost the same impact as sampling errors"；S130 给出 multiverse 方法 | `JOIN_LANE: R05 SD18` |
| `B7` | `FIT_BASELINE`（仅 `DESCRIPTIVE`） | 与最简饱和模型比较 | R05 SD7（2 波 CLPM 饱和 → 无 fit 信息，Hamaker et al. 2015 摘要逐字：*"We found that **45% of the studies** that we examined estimated the CLPM based on only two waves of data"* —— 该数字说的是"**所估计的 CLPM 只基于两波**"，**不是**关于拟合质量的判断）；R05 SD17（RI-CLPM 多 3 df → **不得用 fit 选模型**） | `JOIN_LANE: R05 SD7/SD17` |
| **`N7_UNDIRECTED_SCORE`** | **`UNDIRECTED_SCORE`（把 `Z[k,i→j]` 与 `Z[k,j→i]` 坍缩为单一无向分数）** | 对每个构念 `k`，把两个方向的坐标合并成**一个**无向量（例如 `min` / `mean` / 预登记的组合），然后只用它预测 outcome。 | **Round-3 新增（依 `X-6` 明确接受）。这是唯一直接检验本项目中心表示主张的 null**：它问的是"**LHRM 最贵的那件事——把 `i→j` 与 `j→i` 分开建模——是否比不分开更值钱**"。独立支撑（`JOIN_LANE`）：`19:62`「在 16 个已审计数据集中，**只有 1 个**（速配）提供无外部假设的 `DIRECTED_EDGE` 双分量，而它**没有第二个时间点**」。**若本项目最强的表示主张只有一个单波数据集可支撑，则该主张必须先通过 `N7` 的对照。** **不得**把 `N7` 读成"方向性已被证伪"——它是一个**对照**，不是判决。 | `AI recommendation` / `DESIGN_CHOICE`；动机 `JOIN_LANE: R17 F2` + `19:62`（经 `X-6` 采纳） |
| **`N8_LEVEL_CONDITIONAL_SLOPE`** | **`LEVEL_CONDITIONAL_SLOPE`（`Level → Slope` 交互模型）** | 在 `Level` 之外显式估计一个由 `Level` 调节的 slope：`Slope_k = α + β · Level(τ₀)`。 | **Round-3 新增（依 `X-6` 明确接受）。这是唯一能真正测 DVA 交互的模型；若 null 集里没有它，DVA 的判 G（`06 §6.8`）没有参照物** —— 判 G 要求比较"`Level` 独解释的人内方差"与"`Level + Slope` 合计所解释者"，而 `N8` 是**唯一一个把"slope 依赖起点"写成可估模型的**候选。`N8` 同时是 §7.0 中"候选必须真正击败"的那个对照的**唯一**实例化。⚠ **`N8` 的形式依据落在 Lavner（`06` 的 S19）上，而 S19 的精确措辞与 Table 5 正在被复核** ⇒ `PENDING_EVIDENCE_CHECK (R3-E3)`。**本行的存在与必要性不依赖该复核结果**（`N8` 测的是 DVA 的判据形态，不是 S19 的结论）。 | `AI recommendation` / `DESIGN_CHOICE`；依 `X-6` + `06 §6.8 判 G` |

**`B2_STABLE_LEVEL` 的 rationale（Round-3 逐字改写，依 `X-6` / `C-P10` 第 3 条）。**

> **被取代的原文（逐字保留）：** *"**本协议认为最重要的一条 null，因为它已经击败过一个候选。** R06 F6：S19 在婚姻恶化模型的正面对决中 **initial-differences 击败了 incremental-change**，衰退集中在**起点低**的人身上、且最严重的一群是起点最低的子集，对 incremental-change 模型只有 'limited evidence'。R06 N1 记为'对律 C 的已核实证伪'"*
>
> **取代文本：** R06 F6 实际报告的发现是——**在所测的预测变量中，起点值对轨迹组的区分力强于这些变量的变化率**。
> **必须同时记录的三条限定：**
> 1. **该发现讲的是 `predictor` 变量，不是 outcome 的人内斜率。**
> 2. 原文说的是 *"limited evidence"*，**不是** explicit refutation；丈夫侧的读法是 *"consistent with the incremental change model"*。
>    因此**既不得**写成"initial differences 击败了 incremental change"，**也不得**写成"incremental change 已被反驳"。
> 3. **存活下来的结论是 level-conditional slope**（`N8_LEVEL_CONDITIONAL_SLOPE`），不是"null 赢了"。
>
> ⚠ 上述三条限定所依据的来源是 Lavner（`06` 的 S19）。**S19 的精确措辞与 Table 5 正在被复核**
> ⇒ 本段标 `PENDING_EVIDENCE_CHECK (R3-E3)`。**本行不主张 S19 的任何结论成立或不成立**；
> 它只把"该结论**不能**被写成什么"记录下来。

**§7 开头原「配对击败 B1 与 B2」主判定规则（HEAD `16:168`）的处置：** 见 §7.0。**该条被删除**，不保留为规则；
其**唯一未被否定的残留**是 §7.0 第 1、2 条（固定条件 + 配对击败 `B1`）。

**跨模型比较的报告要求**：候选与每个 null 的比较必须 (a) 报**效应差**及其 dyad-level 区间；(b) 报 holdout 上两者的**绝对误差**（不只报相对提升）；(c) 遵守 §7.2 的不确定度规范。**禁止只报 p 值**（R05 SD9：明确禁止 "do not use p values to decide for the final model"）。

### 7.2 不确定度报告要求


| Rule | 内容 | 依据 |
|---|---|---|
| `R16-UC01` | **不确定度的单位是 dyad。** 所有区间必须来自 dyad 分层重抽样（cluster bootstrap / dyad-block permutation），**不得**来自 fold 间标准差。 | S04 原文："The standard error across folds strongly underestimates them"；"folds are far from independent"（`CITED_PRIMARY`）；S13；S03 |
| `R16-UC02` | 必须同时给出 `n_dyads`、`n_dyad_waves`、`n_measurement_occasions`、attrition 表（按 wave / side / 关系类型）与**估计的最小可检测效应**。 | S04（n=100 → ±10%）；`JOIN_LANE: R05 SD12` |
| `R16-UC03` | 概率型 readout 必须用 **strictly proper scoring rule** 报校准（log score / Brier），不得只报 accuracy 或 AUC。 | S19（Gneiting & Raftery 2007） |
| `R16-UC04` | **禁止**用误差条重叠做视觉判断；必须写数值区间 + "区间是否包含 null" + 当前样本量下的可检出性。 | S20（Cumming & Finch 2005，"Inference by Eye"） |
| `R16-UC05` | 任何 `Z` 的读出必须携带 **estimate + uncertainty + evidence/provenance**；**不得**把 posterior mean 写成"真实状态"。 | `existing project constraint` P03 §9.6；`empirical evidence` R05 I2 |
| `R16-UC06` | `INVARIANCE_REPORT` 必填：报告实际达到的不变性层级。**`NOT_TESTED` 必须出现在报告正文而不是附录。** | R05 I8 / SD3；S21 |
| `R16-UC07` | MNAR 敏感性分析必须与主分析**并列**报告，不得放脚注。 | `JOIN_LANE: R05 I13` |
| `R16-UC08` | **禁止把 `R²` / fit / effect size 当作"模型是对的"的证据。** 任何 `F` 的表述必须限定为"在指定 instrument、采样协议与 `F` 形式假设下，与数据一致的 `F` 之一"。 | `JOIN_LANE: R05 SD7 / F1` |

---

## 8. Worked example mapping skeleton

> **零数据接触声明。** 下表**没有任何一行来自被打开的数据文件**。所有变量名与字段语义来自 R04 已审计的官方文档与 codebook 结构（R04 报告 D01–D04、D08、D09），或来自本 lane 独立抓取的 SHARE CoU 正文。凡 R04 未给出确切变量名处，本表**显式标 `UNVERIFIED_AS_OF` 并拒绝编造**。

### 8.1 表头模板（每行必填）

```text
row_id
dataset_ref@version
unit_of_analysis
raw_variable            # 发货名；复合量须写出构成题项
side_binding            # anchor / partner / 无方向 / pair
directionality_class    # §3.2 受控表
mapping_status          # §3.1 六值受控表
measurement_type        # single_item | multi_item_index | latent_factor | behavior_decision
                         # | administrative_record | physiological | derived_transform
candidate_lhrm_slot     # DirectedRelationshipState[K, i->j, t] / PairState / Belief_i(.)
                         # / AgentState / ActionEvent / Environment / COVARIATE
basis_note              # 指向官方 codebook 章节 / 官方 FAQ 原句 / 文献
conflict_refs           # 当 status = CONFLICTED
uncertainty{...}        # §3.4 五字段
leakage_flags           # L1..L8 中命中的编号 + 一句话
outcome_link            # 该变量是否被任何 outcome 的定义读取（→ L2）
rights_note             # 依 SHARE CoU §7 的可处理性
verified_on / verified_by
```

### 8.2 五行示例（真实变量；来源 R04 审计）

#### R1 — pairfam：`reldur` vs `preldur`（同一 pair 事实的两位 informant）

| 字段 | 值 |
|---|---|
| `dataset_ref@version` | `pairfam / ZA5678 / Release 14.2`（14 wave；J04 记 2026-09-27；**本 lane 独立核实失败**：HTTP 500 → 版本串标 `JOIN_LANE`） |
| `unit_of_analysis` | `DYAD_WAVE` |
| `raw_variable` | `reldur`（anchor 自报关系时长）与 `preldur`（partner 自报关系时长）—— R04 D01 明确 partner 侧变量统一 `p` 前缀（`psex_gen, page, preldur, pmarstat, pincoecd`） |
| `side_binding` | `reldur` → anchor；`preldur` → partner |
| `directionality_class` | `PAIR_LEVEL` |
| `mapping_status` | **`CONFLICTED`** |
| `measurement_type` | `single_item`（双方各一题） |
| `candidate_lhrm_slot` | `PairState_(i,j)` 的时间坐标 / `COVARIATE` |
| `basis_note` | R04 D01 记录 `relstat / marstat / cohabdur / mardur / reldur / meetdur / homosex` 存在；`p` 前缀为 partner 侧 |
| `conflict_refs` | 两个候选读法：(a) 它是 **pair 的共同事实**，两方报告应合并；(b) 它是**两个 informant 对同一 pair 事实的报告**，差异是 informant accuracy。R04 D01 自身记录 pairfam 侧关系状态构念清单**未核实**（U15）→ 无法裁决 |
| `uncertainty` | `estimated_uncertainty = UNKNOWN`；`measurement_error_known = no`；`invariance_level_tested = NOT_TESTED`；`floor_ceiling_risk = yes`（自报时长的四舍五入 + 记忆偏差） |
| `leakage_flags` | **L5**（同一 pair 事实经两位 informant 取得，若同时入模则 partner 侧携带 actor 侧的部分信息）；**L1(b)**（若时长被用作任一 outcome 的组成部分） |
| `outcome_link` | 若进入 `B5`（`LABEL_BASELINE`）则被 outcome 读取 → L2 检查点 |
| `rights_note` | pairfam §3（经 `J04 D01` 转述，本 lane 未独立核实）："Zulässig sind nur zusammenfassende Darstellungen der Daten … Die Darstellung oder Publikation von Einzeldatensätzen oder Einzelfällen, auch wenn es keinen direkten Personenbezug gibt, ist nicht erlaubt." → 映射表**可以**做（内部工作），**派生个体记录不可**进 Case Bank |
| `verified_on / verified_by` | 2026-09-27 / `JOIN_LANE: R04 D01`（本 lane 独立核实 = **失败**） |

#### R2 — speed dating：`dec` / `match`（唯一无外部假设的 `DIRECTED_EDGE`）

| 字段 | 值 |
|---|---|
| `dataset_ref@version` | Fisman & Iyengar speed dating（2002–2004，21 场 session）；镜像 `https://github.com/datasets/speed-dating`、`https://www.openml.org/d/40536`、`https://osf.io/8k7rf/`（J04 D04 记 2026-09-27 HEAD 200） |
| `unit_of_analysis` | `DYAD_EVENT`（一次 4 分钟接触 = 一行） |
| `raw_variable` | `dec`（是否想再见对方）与 `match`（互惠标记）；另有 6 项属性评分（Attractiveness / Sincerity / Intelligence / Fun / Ambition / Shared Interests） |
| `side_binding` | `dec` 与 6 项评分均有方向绑定：同一 `(i,j)` 上既有 i 对 j 的量，也有 j 对 i 的量 |
| `directionality_class` | **`DIRECTED_EDGE`** |
| `mapping_status` | `dec` 与 6 项评分 → **`BEHAVIORAL_PROXY`**；`match` → **`DERIVED_COMPOSITE`** |
| `measurement_type` | `behavior_decision`；`single_item × 6`；`derived_transform` |
| `candidate_lhrm_slot` | `dec` → `ActionEvent`（决策行为）或 `BEHAVIORAL_PROXY` of `Liking_(i->j)`；`match` → `MutualLiking_(i,j)`（pair-derived，**不得**单设 primitive） |
| `basis_note` | R04 D04 原文：每段结束时该参加者被问"是否想再见该对象 (dec) + 在 6 个属性上评分"；"`match` = 双方都想再见的互惠标记" |
| `conflict_refs` | `dec` 的读法冲突：**(a)** 它是 `Liking` 的观测（越过界）；**(b)** 它是**决策**，R04 明文警告"把它当'attraction 的观测'是模型假设，不是证据" → 采纳 (b) |
| `uncertainty` | `estimated_uncertainty = UNKNOWN`（R04："未找到官方 sampling/attrition 文档 → missingness 文档视为**弱**"）；`measurement_error_known = no`；`invariance_level_tested = NOT_APPLICABLE`（单一时点） |
| `leakage_flags` | **L1(b) 强触发**（`dec` 同时是 predictor 与 criterion → `NOT_IDENTIFIABLE`）；**L3**（21 场 session 内同一个人与多位参加者配对，**该人的行跨越多个 dyad** → 必须按 `wave`(session) 分组）；**L4**（无第二时间点，转移律不可识别） |
| `outcome_link` | 若 `match` 被当作 outcome，则 `dec` 是 outcome 的确定函数 → **L2 必然触发** |
| `rights_note` | **完全公开，无注册**（R04 D04）。本 landscape 中唯一的零门槛数据 → 也是本协议中唯一**今天就能完整执行**的映射练习 |
| `verified_on / verified_by` | 2026-09-27 / `JOIN_LANE: R04 D04`；`dec` / `match` / `wave` 由 J04 命名并经本 lane 采信；**6 项评分的实际变量名 `UNVERIFIED_AS_OF`（未下载数据，拒绝推测）** |

#### R3 — HARP：baseline 关系质量 + 8–10 天日记（day 粒度 `t`）

| 字段 | 值 |
|---|---|
| `dataset_ref@version` | HARP（ICPSR 37404）。**版本状态矛盾**：落地页 "Version Date: Jan 4, 2022" 且标题仍为 "2014-2015"；`/summary` 与 `/datadocumentation` 索引显示 "2014-2025" 含 T2/T3 → `UNKNOWN_AS_OF`。**本 lane 独立核实失败**：ICPSR HTTP 403 |
| `unit_of_analysis` | `DYAD_WAVE`（稀疏面板 3 点）**嵌套** `DYAD_DAY`（每点 8–10 天日记）→ 须写两个单位 |
| `raw_variable` | 每时间点 baseline questionnaire 的 relationship-quality 测量 + daily diary 的当日测量。**确切发货变量名 `UNVERIFIED_AS_OF`**（R04 只核实了设计：spouses were asked to complete the surveys separately；日记入组门槛 10 天中完成 ≥6 天；每点 10 天日记；T3 降为 8 天）。**本 lane 拒绝编造变量名。** |
| `side_binding` | 双配偶**分开作答** → 有真实 side 绑定 |
| `directionality_class` | `DIRECTED_EDGE`（设计层） |
| `mapping_status` | **`DIRECT_ITEM`**（设计层）／多题合成则 `DERIVED_COMPOSITE`。**最终判定阻塞于 codebook 未核实**（F-01） |
| `measurement_type` | `single_item` 或 `multi_item_index`（`UNVERIFIED_AS_OF`） |
| `candidate_lhrm_slot` | `DirectedRelationshipState[RELATIONSHIP_QUALITY, i->j, t]` 与 `[·, j->i, t]`；日记层给 `t` 的**日粒度** |
| `basis_note` | R04 D03 入组条件：合法已婚 + **已同居至少 3 年**，T1 时 35–65 岁，马萨诸塞州 |
| `conflict_refs` | 入组条件使该样本**无法覆盖** LHRM 研究域中的陌生起点、非婚、第三方。R04 明确这与 `AGENTS.md` 当前架构方向第 2 条冲突 → HARP 只能作**局部**校准源 |
| `uncertainty` | `estimated_uncertainty = UNKNOWN`（有官方留存数字 T1 419 → T3 268 couples ≈ 36% couple 层流失，但那**不是**抽样误差 SE）；`missingness_mechanism = UNKNOWN`（MNAR 敏感性**尚未做**）；`invariance_level_tested = NOT_TESTED`；`floor_ceiling_risk = unknown` |
| `leakage_flags` | **L8**（36% 流失 + T3 日记窗 10→8 天 + 幸存/丧偶条件化）；**L4**（日记内部顺序：若用当日较早条目预测当日较晚条目，须显式声明时间间隔，不能称"日间转移"） |
| `outcome_link` | 若 outcome 含"离婚/分居" → `R16-OC03`（T2/T3 只续访原配偶身份 → 离婚/分居后的**新关系**不可观测 → `CENSORING_BY_DESIGN` + `NOT_MAPPED`） |
| `rights_note` | ICPSR 公版申请 + ICPSR LLM 政策适用（`JOIN_LANE: R04 D03/D12`；本 lane 独立核实失败） |
| `verified_on / verified_by` | 2026-09-27 / `JOIN_LANE: R04 D03`；版本 `UNKNOWN_AS_OF` |

#### R4 — NSFH：单方报告的配偶关系质量（`UNDETERMINED` 方向性的标准反例）

| 字段 | 值 |
|---|---|
| `dataset_ref@version` | NSFH Wave 1–3（1987-88 / 1992-94 / 2001-02 或 2001-03 —— 两个官方来源年份不一致，**并列保留、不选边**） |
| `unit_of_analysis` | `PERSON_WAVE` + `PERSON_DYAD_WAVE` |
| `raw_variable` | 主受访者被问的 household members 之间的关系质量题（R04 D08 引 Wave 1 原文："Respondents were also asked about the relationship of household members to each other and the quality of their relationships with their parents, children, and in-laws"）。**确切变量名 `UNVERIFIED_AS_OF`** |
| `side_binding` | **无配偶间 side 绑定** —— 由**一个人**报告 |
| `directionality_class` | **`UNDETERMINED`**（由 `R16-ID09` 与 L5b 强制） |
| `mapping_status` | 题本身是 `DIRECT_ITEM`；但**任何 `i->j` / `j->i` 用途必须标 `REPORT_ASYMMETRY`，禁止解释为状态不对称** |
| `measurement_type` | `single_item` 或 `multi_item_index`（`UNVERIFIED_AS_OF`） |
| `candidate_lhrm_slot` | 仅可用于该 dyad 的**报告层**；**不得**填入 `DirectedRelationshipState` |
| `basis_note` | R04 D08 判断原文：**配偶关系质量是单方报告** → "`Z[i→j]` 与 `Z[j→i]` 在 NSFH 中不可分离"；但**亲子/跨代方向是真实可测的**（子女 + 随机一名家长 + 关系质量题）→ 这是 NSFH 真正的方向性资产 |
| `conflict_refs` | 无构念冲突；**有分析权限冲突**：用它做方向性分析会违反 L5b |
| `uncertainty` | `invariance_level_tested = NOT_TESTED`；`measurement_error_known = partial`（有 PI codebook + DDI XML，但未核实到量表级文档） |
| `leakage_flags` | **L5a / L5b 强触发** |
| `outcome_link` | 若同时作为 predictor 与 outcome → **L1(b) + L2** |
| `rights_note` | ICPSR 公版（非成员可申请）；三波地码版为 restricted（`JOIN_LANE: R04 D08`；本 lane 独立核实失败） |
| `verified_on / verified_by` | 2026-09-27 / `JOIN_LANE: R04 D08` |

#### R5 — pairfam：`pmarstat` / `relstat` / `homosex`（制度事实 → `COVARIATE_ONLY`）

| 字段 | 值 |
|---|---|
| `dataset_ref@version` | `pairfam / ZA5678 / Release 14.2`（同 R1 来源；本 lane 独立核实失败） |
| `unit_of_analysis` | `PERSON_WAVE`（anchor 问卷）/ `PERSON_WAVE`（partner 问卷，**不同 instrument**） |
| `raw_variable` | `pmarstat`（partner 自报婚姻状态）、`preldur`、`relstat`、`homosex` / `ALKhomosex_new` |
| `side_binding` | partner 侧（`p` 前缀） |
| `directionality_class` | `PAIR_LEVEL`（制度事实，不分解为两条有向边） |
| `mapping_status` | **`COVARIATE_ONLY`** |
| `measurement_type` | `single_item`（分类） |
| `candidate_lhrm_slot` | `PairState_(i,j)` 的制度/协议层，或 `COVARIATE` |
| `basis_note` | R04 D01：`relstat / marstat / cohabdur / mardur / reldur / meetdur / homosex` 存在；`homosex` 提供**同性伴侣 dyad** 的存在性（德国样本） |
| `conflict_refs` | 无 |
| `uncertainty` | `invariance_level_tested = NOT_TESTED`；`floor_ceiling_risk = no`（分类变量） |
| `leakage_flags` | **L5**（anchor 与 partner 用**不同 instrument** 报告同一制度事实 —— 既是泄漏风险也是测量机会：它给出一个**制度事实层的双报告**对照，与 R4（NSFH 单方报告）形成方法学对照） |
| `outcome_link` | 若进入 `B5`（`LABEL_BASELINE`）→ 该 null 的定义就包含它，**这不是泄漏**（`B5` 的目的正是如此），但必须标注 |
| `rights_note` | 同 R1：pairfam §3 禁止发布个体记录（`JOIN_LANE`） |
| `verified_on / verified_by` | 2026-09-27 / `JOIN_LANE: R04 D01` |

### 8.3 未纳入示例但已被 R04 命名、且对方向性协议最关键的两个数据集（留给 Wave 2）

- **CLOC Part 5 "Couples Only"（ICPSR 3370）**：R04 D09 记 "contains data collected from both the husband and the wife of 423 couples (n = 846) and includes all available data from all four waves … Each record contains data for the wife (the 'V' variables) and data for the husband (the 'S' variables)"。这是 R04 找到的**最早、最干净的双人同 record 四波设计**（1987–1993），且 `V` / `S` 是**真实的 dataset-level 命名**。它应成为检验 `R16-ID05`（side-swap 检验）的首选载体 —— wife/husband 是**不对称命名**，side-swap 检验在此有真实可失败的余地。限制：随访对象是丧偶者 + 匹配对照 → 触发 L8。
- **DHS Couples (CR) file**：R04 D05 记 MR19 直接用 "the person's own age" 与 "the person's report (estimate) of their partner's age" 做跨人感知误差分析，覆盖 113 surveys for men / 67 surveys for women。这是**可核实的方法学先例**：DHS 官方就把"我报你的年龄"与"你自报年龄"当两个不同测量对象 → L5 的官方级先例。限制：**逐轮/逐国需查**（R04 记录的官方 user forum 失败案例）。

---

## 9. 显式调和 R04 的 access/rights 结论：本协议的可执行性判定

### 9.1 四条事实

1. **唯一三个 `CALIBRATION_READY` 数据集（pairfam / SHARE / HARP）全部在注册或 DUA 之后。**（`JOIN_LANE: R04 §3.1 / §3.5`）
2. **SHARE CoU §7（2026-04-30 版）明文禁止非 fully-self-administered 的应用**，并规定 **"Any derivative datasets, models, or analytical outputs generated through AI or machine learning processes remain subject to the same usage restrictions as the original data."**（本 lane **独立逐字核实**）同页另有：access 按个人授予，团队内每个人都必须各自注册下载。
3. **pairfam §3 只允许汇总呈现**，即使无直接标识也**不得发布个体级记录**；§4 禁商业用途；§5 原则上不得向项目/机构外第三方转发。（`JOIN_LANE: R04 D01`；本 lane 独立核实失败）
4. **Add Health 与 UAS（ICPSR 系）已被明文禁止用 LLM/AI 管理、处理或分析其任何数据**；ICPSR 的 `Redistribution Policy` 把"把数据交给会留存或用于训练的 LLM"定为 redistribution 并禁止。UAS 原文："the use of LLMs constitutes a violation of all existing Data Use Agreements."（`JOIN_LANE: R04 §3.3 G2`；本 lane 独立核实失败）

### 9.2 四条可执行性判定

| # | 判定（含依据） |
|---|---|
| E1 | **本协议不能被实现为"LLM 参与的公开流水线"。** SHARE CoU §7 的后两句（"非 fully self-administered 的应用严格禁止" + "派生数据集/模型/分析产出受同样限制"）合起来意味着：即使个体级数据从不离开合规环境，**任何经 LLM 生成的映射表、派生量或分析产出也不得自由再分发**。而本协议的核心交付物（`FREEZE_RECORD` 的 16 字段、`mapping_table_ref` 的 commit hash、`B6` 的 multiverse 分布）**天然是会被 review、会进 Git、会被引用**的产物 → 这就是 `R16-ID11` 存在的理由。 |
| E2 | **唯一今天可完整执行的路径是"零门槛数据 + 结构性产出"。** 速配数据**完全公开、无注册**。它不能标定任何转移律（无第二时间点，须标 `NO_TEMPORAL_AXIS`），但它**可以**完整执行 §2 的 ID 纪律、§3 的六值词表、§4 的 L1–L8 检查、§6 的降级路径、§10 的 `FREEZE_RECORD` 全流程。**这应当是本协议的第一个 dry run。** |
| E3 | **"内部方法学验证"与"公开验证语料"是两个不重叠的世界，协议必须分开写。** R04 §4 矛盾 8：`VALIDATION_CORPUS_V0_1.md` 现有 12 个材料的来源**全部不在**本 lane 审计的任何 access 条款管辖范围内 → 本协议**不要求** Case Bank 与量化数据集共享权利路径；但**量化验证结果不得回流进 Case Bank**。 |
| E4 | **三个 `CALIBRATION_READY` 全部需要自托管才可能合规。** R04 定位到唯一已知可行的合规路径是 ICPSR SOMAR VDE / MiCDA Enclave 内自托管模型。本协议对此**不表态**（合规判定属法务，R04 已明确其 non-claim 11），只登记一条工程后果：若走 enclave，则 `code_commit` 必须能在一个**离线可复现**的镜像中复现，否则 `FREEZE_RECORD` 的可审计性在物理上就断了。 |

**`R16-ID11` 的代价必须被明说**：它使**外部第三方无法独立复核 `FREEZE_RECORD` 的映射行**。这是 rights 与可复现性之间的一次真实取舍，本协议**不**把它包装成已解决。替代方案（enclave 内提交可复现脚本、由 enclave 运营方在内部复核）是 R04 已定位的路径，但本 lane 无法核实其可行性（`UNKNOWN_AS_OF`）。

---

## 10. 协议在哪里**不足**（→ `PARTIAL` 的根据）

| # | 不足 | 原因 | 严重度 |
|---|---|---|---|
| **F-01** | **映射表今天填不出来。** §8 的 5 行里有 3 行的**变量级 codebook 未核实**。R04 自己把这条列为 U15（pairfam / SHARE / HARP 的问卷中实际有哪些「关系状态」构念 = **未核实**），并警告"这直接决定它们到底能不能标定 LHRM 的关系状态参数"。 | `JOIN_LANE: R04 U15` | **阻断级。** §8 因此是**模板**，不是规格 |
| **F-02** | **本 lane 无法独立复核 pairfam 与 ICPSR 的条款**（500 / 未解析 PDF / 403）。§9 中除 SHARE 外的所有 rights 表述强度均为 `CITED_SECONDARY`。 | 本 lane 实测 | 高 |
| **F-03** | **外部验证（`#29` F 层）当前不可执行。** → ⚠ **Round-3（依 `X-14`）：** 不是"四条件交集**为空**"，而是**在 R04 被结构检验的 15 个数据集**上四条件交集为空（审计总数 16，`D12` 未进入结构检验）；`D12 / Add Health` 是被**许可**条件排除的**已检候选反例**（`C-C19` / `C-C20`）。**本文件此后不主张该交集在领域中为空。** | `JOIN_LANE: R04 §4 矛盾 9` | **阻断级**（`NOT_STATED_AS_FIELD_WIDE_ABSENCE`） |
| **F-04** | **终止事件不可作 outcome。** 关系终止是 censoring by design。 | `JOIN_LANE: R06 U-3` | **数据收集方式的限制**（Round-3 改词，依 **R-D7**：`D-C35`）。**被取代的原文：severity = `结构性`。** 改词理由：终止事件不是"关系这个对象在原理上不可观测终止"，而是"**以自陈面板这种数据收集方式**采集不到终止"。行政 / 法律 / 事件记录可以观测它。同一改词适用于 `06 §10 U-3`（见该文件 §10 的 Round-3 交叉注记） |
| **F-05** | **律 A（`BMR`）的判别内容当前不可检验。** 需要对方行为的独立观察 + 双方各自信念的独立报告。 | `JOIN_LANE: R06 U-1` | **数据收集方式的限制**（Round-3 改词，依 **R-D7**）。⚠ **Round-3 记账（依 `X-14` / `X-11`）：** 原文"现有绝大多数 dyadic 面板只有自陈"是一个**未被取样框架支持的 field-wide absence claim**。Round-3 降级为检索范围表述：**"在 `06` 本次检索到的来源中，未发现同时满足'对方行为的独立观察 + 双方各自信念的独立报告'的 dyadic 面板"**。`06` 的 `BMR` 状态因此是 `HOLD_FOR_EVIDENCE`，**不是**"结构上不可证伪"。⚠ `S04`（Joel et al. 2020）正在被复核 ⇒ 该行的 S04 依赖部分标 `PENDING_EVIDENCE_CHECK (R3-E3)`；**本行的阻塞理由不依赖 S04** |
| **F-06** | **无任何构念有两个独立通道。** R03 G9 标为**架构级 gap** → L6 **无法被经验地满足**。 | `JOIN_LANE: R03 G9` | 阻断级（对 Reality/Observation/Belief 分离的验证） |
| **F-07** | **方向性分解不可识别。** P04 §1 的分解式在纯两人 dyad 下**不可识别**（2 条有向边 = 2 个自由度）。R05 I4：三者可作**架构占位符**，但**不得**写成"估计值"；R05 I14 称这是"**LHRM 最难的一个识别缺口**"。 | `JOIN_LANE: R05 I4/I14` + `PROJECT` P04 §1 | 阻断级 |
| **F-08** | **表示完备性无法用作前置健全性检查。** R17 F1 证明 `MAPPING_FAILURE` **构造上不可达** → Case Bank 的 representation completeness 恒等于 100%，**不携带任何关于 schema 质量的信息**。→ **不能用"Case Bank 映射通过"支持"量化映射规格正确"。** | `JOIN_LANE: R17 F1` | 高 |
| **F-09** | **power 分析做不出来。** 事件率未知 + dyad 数小（HARP T3 仅 268 couples）+ S04 的误差带在小样本下极宽。 | `JOIN_LANE: R05 SD12` + S04 | 中–高 |
| **F-10** | **`L8` 的 MNAR 敏感性在 outcome 侧无方法指引**（"关系解体"无可用 missingness indicator）。 | 本 lane 推理 | 中 |
| **F-11** | **无 item 级使用登记表** → `F-SELF21`（跨行同源复用）无法被审计。 | 本 lane 推理 | 中 |
| **F-12** | **`R16-ID05`（side-swap 检验）无参照量表**（S12 在二人 dyad 随机效应结构上的具体推荐规格未取得）。 | `UNKNOWN_AS_OF` | 低–中 |
| **F-13** | ⭐ **（Round-3 新增）默认几何在现有数据上不可实现，且这一点此前未被登记。** `G4_DYAD_PURE_FORWARD`（§6.2，Round-3 补入的默认）要求每个 holdout dyad 在全局边界 `t*` 之后仍有观测。HARP T3 仅 268 couples 且日记窗已从 10 天缩到 8 天。 | `AI recommendation` / `DESIGN_CHOICE`（`16` 本文件推理）+ `JOIN_LANE: R04 D03/D09` | **高**（依 R-D8 的直接后果）。**必须写进 `FREEZE_RECORD`**：默认几何不可用时不得默认掉，须落到 §6.2 记账规则第 2 条（`WITHIN_DYAD_TEMPORAL_EXTRAPOLATION_ONLY` + 理由） |
| **F-14** | ⭐ **（Round-3 新增）`FZ-1` 的持有者与可审计性在现行条文下未定义。** 见 §11.2 顶部 (a)–(f)。 | `NOT_ENFORCEABLE_AS_WRITTEN`（依 **R-D9**） | **高**。**后果**：在 `FZ-1` 规格落地前，本协议**不得**声称"已防 holdout 自适应复用泄漏"（`F-SELF11` / L7） |

---

## 11. 预登记式 freeze point

### 11.1 `FZ-0` / `FZ-1`：定义

> 在**任何 holdout 行被读取之前**（不是"在看到 holdout 结果之前"），下列 16 字段必须被写入一份不可变的 `FREEZE_RECORD`，并由 Architect 做 durable writeback。`FREEZE_RECORD` 一旦生成，holdout 才解锁。

**时点必须早于"看结果"，且早于"看 holdout 的边际分布"。** R05 SD10（researcher DoF / v-hacking）不是只在看结果后才发生的；看边际分布同样会泄漏信息。S07 表明"结果反馈进设计"是 holdout 失效的机制，而边际分布反馈是同一机制的一个温和版本。

> **Round-3 拆分 `FZ-0` / `FZ-1`（依 R-D9）。** 上面的原始条文只定义了一个冻结点。
> Round-3 拆成两个，并声明**现行条文不足**：
> - **`FZ-0`（本条原文，保留）：** 字段全表 + immutable artifact 生成。⚠ 但 `FZ-0` **本身不充分**——
>   它允许字段 12 为 `TBD_AT_FZ1`，于是**存在一条合规路径让主 estimand 在看数据之后才定**。
>   ⇒ `FZ-0` 与 §11.2 的字段表合起来的状态是 **`NOT_ENFORCEABLE_AS_WRITTEN`**。
> - **`FZ-1`（Round-3 新增，单一不可逆点）：** `FZ-0` 之后、**任何 holdout 行被读取之前**。
>   `FZ-1` 的存在条件、持有者、可审计性与越界后果见 §11.2 顶部的 (a)–(f) 表。
>   **`FZ-1` 之后 holdout 解锁；`FZ-1` 不可撤销、不可延后。**

### 11.2 `FREEZE_RECORD` 必填 16 字段

> ### ⚠ Round-3：freeze 条款判 `NOT_ENFORCEABLE_AS_WRITTEN`（依 **R-D9**，`ADJ2` Q4 / `D-C25` 同向）
>
> **漏洞的精确形状：** 字段 12 允许写 `TBD_AT_FZ1`，而 holdout 在 `FZ-0` 之后**立即**解锁。
> 于是存在一条**完全合规的路径**：
> `FZ-0` 时把 `estimator_family` 写成 `TBD_AT_FZ1` → holdout 解锁 → 看 holdout →
> 在 `FZ-1` 补上 `estimator_family` → 由于 `primary_estimand`（字段 10）的**报告口径**是由
> `estimator_family` 决定的，"主 estimand"实际上可以在**看过数据之后**才定。
> **这正是 L7 存在的目的所要禁止的那件事**（"看结果之后发生的分析决定"），
> 而现行条文在**形式上合规**。⇒ **现行 freeze 条款不可执行。**
>
> **合谋条款（必须一并记入）：** `06 §12` 的 *"明确不建议的动作：不要在 R16 之前冻结任何转移律的函数形式"*
> 与本漏洞方向相同——它把字段 12 的 `TBD` 合法化到跨过 holdout 解锁点。
> **Round-3 的处置：** `06 §12` 已加交叉注记（见该文件 §12）——**"不冻结函数形式"** 与
> **"冻结 estimand"** 是两件事，前者可以晚，后者不能。**本协议要求的是后者。**
>
> **实际需要什么（Round-3 规格，替代上述 `TBD_AT_FZ1` 许可）：**
>
> | # | 要求 | 内容 |
> |---|---|---|
> | **(a) 单一不可逆冻结点** | 引入 **`FZ-1`（单一不可逆冻结点）**：`FZ-0` 之后、**任何 holdout 行被读取之前**。`FZ-1` 之后 holdout 解锁。**`FZ-1` 不可撤销、不可延后。** |
> | **(b) `TBD` 的许可被逐字段收紧** | `TBD` **只**允许出现在能证明**在 holdout 解锁前不可能影响所报告量**的字段。字段 **7（`split_geometry`）、10（`primary_estimand`）、11（`secondary_estimands`）、12（`estimator_family`）** 在 `FZ-1` 时**必须**全部为非 `TBD`：这四个字段共同决定"报告什么量、用什么报"，其中任何一个留 `TBD` 都构成 §11.1 的漏洞。 |
> | **(c) 冻结点的持有者（holder）** | 必须**指名一个角色**（不是自然人）：durable writeback 属 **Project Architect**（本 lane 无此权限，见 §11.4）。**`FZ-1` 的持有者与分析者的身份必须可区分** —— 若同一人既签 `FZ-1` 又读 holdout，S07 描述的自适应反馈通道**结构性打开**。 |
> | **(d) 可审计性** | `FZ-1` 必须产生一个**不可变 artifact**：字段全表 + 时间戳 + `code_commit` + **签署角色的记录**。该 artifact 必须可被第三方读取并逐字段核对。若因 `R16-ID11`（rights）不能公开，则必须**同时**记录"谁在什么环境内核对过、核对结论的 hash"，并把这一取舍写进 `FREEZE_RECORD`（不得只留不可读）。 |
> | **(e) 与 `06 §12` 的冲突处理** | 二选一，**必须显式登记**：(i) `FZ-1` 排在转移律形式裁决**之后**（于是本协议在裁决前不可执行）；或 (ii) `estimand`（字段 10）**独立于** `estimator_family` 冻结，且冻结时写明"族的形式可在不改变 estimand 的前提下后续调整"。**默认 (ii)**，因为 (i) 会让整条 lane 阻塞在一个尚未裁决的 schema 问题上。 |
> | **(f) 越界的自动后果** | 若 `FZ-1` 后发现字段 7/10/11/12 中任一为 `TBD`，**该 (方程, holdout) 的全部结论自动作废**（不是降级为 `EXPLORATORY`，是**作废**）—— 因为无法证明主判据是在看数据前定的。 |

| # | 字段 | 说明 |
|---|---|---|
| 1 | `dataset_ref@version` | `release_version` / `retrieved_on` / `codebook_version` / `weight_variable`（`R16-ID01`） |
| 2 | `rights_and_processing_mode` | 依 SHARE CoU §7，必须记录"处理是否 fully self-administered"、"是否有第三方可验证地不存储/不处理"、"是否仅本地科研目的训练"。**若无法为真 → 该数据集不得进入任何 LLM 参与的流水线** |
| 3 | `mapping_table_ref` | §8 表格的 commit hash。含每行的 `mapping_status` / `directionality_class` / `evidence_channel` / uncertainty 块 |
| 4 | `key_variable_set` | `dyad_id` / `side` / `wave_id` 的确切变量名及其发货状态（shipped vs reconstructed，`R16-ID03`） |
| 5 | `side_label_semantics` | A/B 标签的语义（`R16-ID04`）+ side-swap 检验设计（`R16-ID05`） |
| 6 | `outcome_definitions` | §5 五元组全体 |
| 7 | `split_geometry` | `G4_DYAD_PURE_FORWARD`（默认）/ `G1_BLOCKED_FORWARD` / `G2_ROLLING_ORIGIN` / `G3_LEAVE_ONE_DYAD_OUT_FORWARD` 之一 + 参数（horizon `h`、**全局时间边界 `t*`**、每个 holdout 的 wave 列表、每组 dyad 数）+ **该几何的实际 estimand 文字**。⚠ **若不是 `G4`，必须附 `WITHIN_DYAD_TEMPORAL_EXTRAPOLATION_ONLY` 并说明 `G4` 为何不可用**（§6.2 记账规则第 2 条） |
| 8 | `split_assignment` | **完整 assignment 列表 + 其 hash**（不是 seed）——任何人可独立复现划分而不重跑 RNG |
| 9 | `null_set` | §7.1 的 **11 个** null：`B0` / `B1` / **`B2_STABLE_LEVEL`** / `B3` / `B4` / `B5` / `B6` / `B7` / **`B8_LEVEL_PLUS_RW`** / **`N7_UNDIRECTED_SCORE`** / **`N8_LEVEL_CONDITIONAL_SLOPE`**（`B2_STABLE_LEVEL` 与 `B8_LEVEL_PLUS_RW` 是两个**不同的** level-only null），含每个 null 的实现要点 + **`B2_STABLE_LEVEL` 是否被选入及其理由**（§7.0 第 3 条） |
| 10 | `primary_estimand` | 一个，及其 `estimand_class`。⚠ **`FZ-1` 时必须为非 `TBD`**（§11.2 (b)） |
| 11 | `secondary_estimands` | 全部（多重性处理方式也要登记：不做校正则明写不做校正）。⚠ **`FZ-1` 时必须为非 `TBD`** |
| 12 | `estimator_family` | 方法族 + 随机效应结构的**完整**规格（S12 "keep it maximal"），含 covariance 结构。⚠ **Round-3 收紧：** 原文为 *"若 R06 的律族形式尚未被 Architect 裁决，写 `TBD_AT_FZ1`"* —— **该许可被撤回**（见 §11.2 漏洞说明）。`FZ-1` 时本字段必须为具体族名；族的形式若尚未裁决，走 §11.2 (e)(ii) 的"estimand 独立冻结"路径，而不是留 `TBD`。 |
| 13 | `stopping_rule` | 明确"看几次 holdout"。默认 **1 次** |
| 14 | `min_detectable_effect` | 由 `R16-OC05` 的事件率 + `R16-UC02` 的 dyad 数推出；若算不出，必须写"本设计在当前样本量下无法检出任何小于 X 的效应"——**不得**用"不显著"当结论 |
| 15 | `code_commit` | 分析代码的 commit SHA（含划分生成、缺失处理、估计、评分） |
| 16 | `deviation_log` | 初始为空；freeze 后每次偏离追加一条（时间、原因、是否影响主判据）。**任何一条记录了"看了 holdout 之后改了 X" → 该结果自动为 `EXPLORATORY`** |

### 11.3 freeze 之后的偏离政策

```text
未记录的偏离      → 该 (方程, holdout) 结论作废
已记录的偏离      → 结论降级为 EXPLORATORY，并在报告正文点名
用偏离结果做主张  → 违反 S07 精神；等同 L7 触发
"只改一个选项再看一次" → L7 触发，无例外
```

若确需多次查看（例如要报 `B6` 的 multiverse），**唯一合规路径**是 S07 给的两条：加差分隐私噪声，或改用带隐私预算的可复用 holdout。**对个体级问卷数据，差分隐私会破坏 §3 / §8 要求的逐行可复核性**（`NOT_MAPPED` 之所以有意义，正因为它可被第三方独立检查）→ 因此本协议推荐：**冻结后不看 holdout，改用"预登记的 multiverse 一次性全部报告"**（S18 registered reports 模式；S130 的分析单位）。

### 11.4 签名

`FREEZE_RECORD` 的 durable writeback 属 Architect 权限。**本 lane 无此权限，也未尝试。** 本协议也不主张"由分析者自己签"是充分的 —— 那正是 S07 描述的自适应反馈通道。

---

## 12. 本协议自身设计的失败分类（false-positive 模式）

> ### ⚠ Round-3：本节 21 行里 **18 行是转录件**，不是本协议新产出的检查项（依 **R-D11** + dispatch 的 delivery-accounting 要求）
>
> **逐字保留的原始小标题：** *"## 12. 本协议自身设计的失败分类（false-positive 模式）"* ·
> *"每条 = 本协议可能**产生假阳性**（宣称"已验证"而实际未验证）的方式。交叉 R05 SD1–SD20 与 R17 F1。"*
>
> **计数（Round-3 机械复算，可复现）：** 本节共 **21** 行（`F-SELF01` … `F-SELF21`）。
> ⚠ **dispatch 的文字说"§12 的 20 行"，实际是 21 行。** 差异记录在 packet，**正文按实际计数**。
>
> **它们是什么：** `F-SELF01`–`F-SELF18` 逐条对应 `05 §6` 的 `SD` 项与 `R17 F1` / `PROJECT` P03
> （**不全是 `SD1–SD20`**：`F-SELF01` = R17 F1、`F-SELF02` = P03 §6、`F-SELF15` 含 P03 §9）；
> 加上 `F-SELF19`–`F-SELF21` 三条**本 lane 特有**的观察。
> **它们不是什么：** 那 18 条**不是**本协议独立产出的检查项，**不得**被计入"本协议交付了 21 条失败模式"。
> 本协议在 §12 的**独立**贡献只有两处：把 `SD` / `R17 F1` / `P03` 项映射到本协议的具体防线（"本协议的防线"列），
> 以及 `F-SELF19` / `F-SELF20` / `F-SELF21` 三条。
>
> **同样地（delivery accounting 的完整版）：**
>
> | 节 | 行数 | 是否一等交付物 | 理由 |
> |---|---:|---|---|
> | §2 `R16-ID01`–`R16-ID12` | 12 | **是** | 本 lane 自己的设计决定 |
> | §3 三组枚举 | — | **是** | 本 lane 自己的词表 + §3.5 的缺口诊断 |
> | §4 `L1`–`L8` + §4.1 | 8 + 5 | **是** | 本 lane 自己的规则集（但 claim-to-source `NOT_OPENED`） |
> | §5 `R16-OC01`–`OC05` | 5 | **是** | 本 lane 自己的设计决定 |
> | §6 四种几何 | 4 | **是** | 本 lane 自己的设计决定 |
> | §7 null 注册表 | **11** | **是** | 本 lane 自己的注册表（`B0`–`B8` = 9 个 `B*` + `N7` + `N8`；`N7` / `N8` 是本轮新增） |
> | §7.2 `R16-UC01`–`UC08` | 8 | **是**（部分转录自 `05 SD`） | 字段设计是本 lane 的 |
> | **§12 `F-SELF01`–`F-SELF21`** | **21** | **否（转录件）** | 转录 `05 §6` / `R17 F1` |
> | **§13 `I1`–`I17`** | **17** | **否（转录件）** | 转录 `05 §5`（Round-1 形态） |
> | **§7.1 的 null 名称中来自 `06` 的部分** | — | **否（转录件）** | `B2_STABLE_LEVEL` / `B8_LEVEL_PLUS_RW` / `N8` 的**模型**来自 `06 §6.3`；本 lane 的贡献是**改名与角色降级** |
>
> **⇒ 本报告被归类为 `JOIN LANE`。** 它的独立贡献集中在 §2 / §3 / §4 / §5 / §6 / §7 / §7.2 / §11 / §4.1；
> §12 与 §13 是把 sibling lane 的结论接进本协议的**接口**，不是本协议的产物。
>
> ### ⭐ 重新标注：**本协议真正的首要交付物是 `F-SELF19` / `F-SELF20` / `F-SELF21`**
> （依 **R-D11**，判定为 **`VERIFIED` 为遗漏**，`D-C30`）
>
> §17 的 Round-1 交付清单把"21 条失败模式"当作普通一项。本节把它提到**首位**，理由是：
> `F-SELF20` 那一行是**三份报告里最诚实的一句话**：
>
> > **无。（`F-SELF20` 的"本协议的防线"列，逐字）**
> > *"**无防线，本协议最严重的设计级风险。** 如果 schema 的层归属本身错了，本协议的全部 machinery 会忠实地验证一个错误的对象。"*
>
> **逐字保留的原文（`F-SELF20` 行）：** 防线列 = **"无。"**（英文写法为 `None.` ——
> ⚠ **`None.` 不是本表原文**，是同一格的英文写法；引用时必须以 **"无。"** 为准）。
> 逐字保留其请求与答复：*"**无防线，本协议最严重的设计级风险。** 如果 schema 的层归属本身错了，本协议的全部 machinery 会忠实地验证一个错误的对象。"* + 防线列 **"无。"**
> **本协议的全部 machinery（`FREEZE_RECORD`、L1–L8、null 注册表、`UNKNOWN_AS_OF` 纪律）都能被忠实地
> 用在一个层归属错误的 schema 上，并且会给出漂亮的合规通过。**
> **本协议对此**无防线**，且不打算假装有。**
>
> **这三条为什么是首要交付物：** `F-SELF01`–`F-SELF18` 是"我们会不小心夸大"，可被流程缓解；
> `F-SELF19`–`F-SELF21` 是"**我们会认真地做对一件没有用的事**"。
> 交付一份协议而不交付它的**失效方向**，等于交付了一份隐藏前提的协议。
> **本 lane 的立场：这一节优先于 §8 的 worked example 与 §11 的 `FREEZE_RECORD` 规格。**

> 每条 = 本协议可能**产生假阳性**（宣称"已验证"而实际未验证）的方式。交叉 R05 SD1–SD20 与 R17 F1。

| id | 失败模式 | 机理 | 关联 | 本协议的防线 | 防线够不够 |
|---|---|---|---|---|---|
| `F-SELF01` | **映射表通过 = 构念被测量。** | 分析师把"能把 `reldur` 填进 `PairState`"当成"`PairState` 被测量了"。 | R17 F1（完备性指标恒为 100%，不携带信息） | `mapping_status` + `directionality_class` + `uncertainty` 三字段强制并列 | **不够。** R17 的证明是构造级的；本协议只是要求把不确定性显式化，**并没有使 `mapping_status` 成为一个可失败的检验** |
| `F-SELF02` | **`BEHAVIORAL_PROXY` 被静默升格为状态。** | `dec` / ADL 协助次数 / 礼物记录被写成 "「Liking」上升"。 | `PROJECT` P03 §6 | 第 3 类必须记观测环境与机会结构 | 部分。`AGENTS.md` 已禁止，但协议无法阻止实现省略该字段 |
| `F-SELF03` | **把 person 间相关当 person 内动态。** | 只切 time 不切 dyad 时，dyad 的稳定基线跨越划分。 | **SD1**；R05 I17 | `G4_DYAD_PURE_FORWARD`（§6.2，Round-3 新增的默认几何，dyad 永不跨侧）+ `R16-ID12`（person 级阻断）+ `B2_STABLE_LEVEL`（**按需选用**的诊断基线，§7.0 第 3 条）| 强（Round-3 后更强：几何从"声称双轴"改为"真正双轴"） |
| `F-SELF04` | **把一次性截面差异当 transition。** | "关系在 T1→T2 变冷了"。 | **SD2** | `NO_TEMPORAL_AXIS` / `DESCRIPTIVE_ONLY` 降级标签 | 中。降级标签可能被实现忽略 |
| `F-SELF05` | **把不变性失败当真实变化（或反向）。** | 两者观测协方差模式相同。 | **SD3** + I8 | `R16-UC06` | 中–强。S21 表明现实中这类检验被系统性忽略；协议无法强制执行 |
| `F-SELF06` | **把 partner path 叫 influence。** | 官方脚注即禁止。 | **SD4** | `R16-LK5c` + `estimand_class` 强制 | 强 |
| `F-SELF07` | **把 within-person 效应当总体相关。** | RI-CLPM 的 estimand 是 "around the person mean" 提升一个单位。 | **SD5** | `R16-ID02` | 中。estimand 的口述转换仍可能出错 |
| `F-SELF08` | **把 random intercept 当"真 trait"。** | illusory between-person component：可能**只**来自省略的 time-varying covariate（`05 SD6` 的 Round-3 补处置：`RIx` 的方差**不得**直接写进 "stable trait"，未排除该充要条件前只能记为"某分解记账下的残差项"）。 | **SD6** | `R16-ID01` 禁止省略 TVC 而不声明；`B6` 报告规格分布 | **弱。** 本协议**没有**给出检查该省略型 TVC 条件的具体程序（U14）—— 真实缺口。**Round-3 确认这条防线仍为"弱"，不因本轮改动而加强** |
| `F-SELF09` | **把 effect size / R² / fit 当因果证据。** | 2 波 CLPM 饱和 → 无 fit 信息；45% 文献这样做。 | **SD7** + **SD17** | `R16-UC08` + `B7` | 强 |
| `F-SELF10` | **把 dyad 内 N 加大当精度提高。** | 分析单位是 dyad。 | **SD8** | `R16-ID02` + `R16-UC01/UC02` | 强 |
| `F-SELF11` | **反复看 holdout。** | researcher DoF / v-hacking。 | **SD10** | `R16-LK7` + `stopping_rule` + `deviation_log` | **中。** S07 表明这是**制度**问题而非**备忘录**问题 |
| `F-SELF12` | **把 partial invariance 当解决方案。** | `n > 2` 组时 "comparing apples and oranges"。 | **SD11** | `R16-UC06` 要求报**实际达到的层级** | 中 |
| `F-SELF13` | **把"不显著"当"不存在"。** | power 随效应类型差 1–2 个量级。 | **SD12** | `R16-UC02` 要求报 `min_detectable_effect` | **弱。** 见 F-09 |
| `F-SELF14` | **把 hazard ratio 当"确定解体"。** | competing risks + 双向报告偏差 + latent initiation。 | **SD13** | `R16-OC03` | 强——但**前提是**有人读这一条 |
| `F-SELF15` | **把 floor/ceiling 当小事。** | 硬 `0..1` latent score 产生 floor/ceiling bias。 | **SD14** + P03 §9 | `R16-OC01` + `floor_ceiling_risk` | 中 |
| `F-SELF16` | **不收敛 / 非 admissible 解被"修好"后报告参数。** | 过参数化、协方差近零、样本量小、迭代上限。 | **SD15** | `B6` + `R16-UC08` | 中–强 |
| `F-SELF17` | **把 Granger / 时序优先当因果。** | lagged predictor 只给 temporal precedence。 | **SD16** | `R16-OC02` + `R16-LK4` | 强 |
| `F-SELF18` | **规格选择当无所谓。** | "model uncertainty had almost the same impact as sampling errors"。 | **SD18** | `B6` multiverse | 强 |
| `F-SELF19` | **用"能表示"冒充"能预测"。** | 领域内最大规模预注册协作研究（43 数据集 / 11,196 对伴侣）报告 relationship-quality change **"largely unpredictable from any combination of self-report variables"**，任何分析解释的方差**未超过 5%**。 | S23 结论（`JOIN_LANE: R17 F2` 第 3 条）+ R06 F1/N2 | 本协议**不能**防这个 —— 它只能保证我们不会**夸大**预测主张 | **本协议最可能失败的方向，而它失败的方式是"诚实的失败"** |
| `F-SELF20` | **basis 瞄错了相空间。** | S23 的 top-5 predictor 有 **4/5 落在 `DirectedRelationshipState` 之外**（perceived partner commitment = `Belief_i(Dedication_(j->i))`；appreciation = 对关系的评价/情感；sexual satisfaction = Derived 且关系性非方向性；perceived partner satisfaction = 二阶信念；conflict = Action/Event 频率）。R17 F3 更进一步：最强组织变量 `PPR` 在当前 schema 里住在 Belief 层，而派生 readout 住在 Derived 层。 | `JOIN_LANE: R17 F2 / F3` | **无。** | **无防线，本协议最严重的设计级风险。** 如果 schema 的层归属本身错了，本协议的全部 machinery 会忠实地验证一个错误的对象。R17 F3 的措辞是"**构造错了，不是清单错了**" |
| `F-SELF21` | **跨行同源复用未被检出。** | 同一批题项同时进 calibration 与 holdout（不同 dyad），L1 在**行级**看不出来。⚠ **Round-3 补一条同族漏洞：** 同一 `person_id` 出现在两侧（不同 dyad）同样在行级看不出来——由 `R16-ID12` + `L3(d)` 覆盖。 | L1 / L6 / L3(d) / `R16-ID12` | `G4_DYAD_PURE_FORWARD` + `R16-ID12`（person 级阻断）| **中。** 需要 codebook 层的 item 使用登记表（F-11）；本协议未设计该登记表 |

**注意 `F-SELF19` / `F-SELF20` / `F-SELF21` 的性质。** 前 18 条是"我们会不小心夸大"，后三条是"我们会认真地做对一件没有用的事"。协议能可靠地防前者的一部分，对后者只能**显式命名**。

---

## 13. 本协议**仍然不能**建立的事项（交叉 R05 I1–I17）

> ### ⚠ Round-3：本节 17 行是 `05 §5` 的**转录件，不是本协议的交付物**（delivery accounting；依 **R-D2** 对 `05 §5` 的改写）
>
> **逐字保留的原始小标题：** *"## 13. 本协议**仍然不能**建立的事项（交叉 R05 I1–I17）"*
> **计数（机械复算）：** 17 行（`I1` … `I17`），与 `05 §5` 的 17 条一一对应。
> **本节的独立贡献只有一列：** 最后一列"本协议能做的最大让步"。
> ⇒ §12 与 §13 一起构成 `JOIN LANE` 的记账依据：**17 + 21 = 38 行转录件**，
> **不得**计入"本协议交付了 38 项"。
>
> **Round-3 的下游对齐（重要）：** `05 §5` 已被 Round-3 改写为**四类分级**
> （`I-STRUCTURAL` 8 / `I-DESIGN` 3 / `I-LIT-OPEN` 1 / `I-CONVENTION` 5，见 `05 §5.0`）。
> **本节下表仍是 Round-1 的单类型形态**（"为什么换方法也不行"），因为本 lane 只做转录、不重做 `05` 的判断。
> **必须在读本节时一并读的限定（来自 `05` 的 Round-3 改写，逐条）：**
> - `I4` / `I11` / `I14` 是 **`I-DESIGN`（数据设计限制）**，不是永久非目标 ⇒ 本节第 4/11/14 行
>   的"为什么换方法也不行"应读作"为什么**在当前设计下**换方法也不行"。
> - `I9` / `I12` / `I16` 是 **`I-CONVENTION`（estimand scope / 报告口径）**，不是识别限制。
> - `I6` / `I7` 是 **`I-CONVENTION`（投影 / 冗余约定）**。
> - `I8` 的 Round-3 改写：未测不变性时**强均值比较未定义**；aliasing 仍可能。
> - `I1` / `I17` 的 Round-3 限定：`n = 1` 的"不可识别"≠"换方法也做不到"；trait 与 state 不可直接比较。
> - `I2` 的 Round-3 限定：分布层量在已知测量模型下**可识别**。
> **本节不复制 `05` 的分级表（避免两份 SSOT）；上列限定即本节的读法补丁。**

| I-id | 不能建立 | 为什么换方法也不行 | 本协议能做的最大让步 |
|---|---|---|---|
| **I1** | 单一段 case / 单条轨迹拟合转移律 `F` | `F` 的函数形式不可由数据学习；单一轨迹对 `F` 的约束是无穷薄的曲线 | 协议只对**面板**数据谈 `F`；`n_dyad = 1` 一律标 `SINGLE_TRAJECTORY` 且不产生任何参数陈述 |
| **I2** | 对方真实状态 `Z[k,j,i,t]` 的真值 | 观测是 `report_function(state, context)`；即使完美模型 posterior 也不坍缩 | `R16-UC05` 强制 estimate+uncertainty+evidence；**不主张**任何 `Z` 的点值 |
| **I3** | partner 报告的准确性 | SRM 的 accuracy 成分需要 round-robin；两人 dyad 不满足 | `R16-LK5a/b` 强制标 `REPORT_ASYMMETRY`；**不主张**"一方更了解对方" |
| **I4** | 纯 dyad 中分离 `source_i` / `target_j` / `directed_dyad_(i->j)` | 2 条有向边 = 2 个自由度 | 三者可作为**架构占位符**存在于 `directionality_class` 取值里，但**不得**作为估计量被报告（F-07） |
| **I5** | 关系的因果优先级 | 需 exchangeability + 无 time-varying 混杂 + 顺序可交换；二人关系中共同环境 + 共同第三方 + 归因反馈 + 双向行为反馈同时破坏它们；**no-interference 本身不成立** | `R16-OC02` 禁止在观测问卷数据上主张 `CAUSAL` estimand；若声称，必须给 exposure mapping（S14；S15） |
| **I6** | 互惠/不对称作为 primitive 的额外信息 | 若两方向可解耦，`MutualX` / `Asymmetry` 是确定性派生量，零自由度 | 协议支持 P03 §4 的"优先派生"决定（速配 `match` 即典型）；**禁止**反向用"互惠低"推断哪个方向分量错 |
| **I7** | "现在处于哪个离散状态"作为主要估计目标 | LTA/LMM 的状态数 K 与转移约束是人为设定 | 若做状态化投影，必须报 K 与约束敏感性，并标 `COMPRESSED_PROJECTION_ONLY`（P03 架构方向第 9 条） |
| **I8** | "变化了多少"与"变了什么" | DIF 与真变的观测协方差模式相同 | `R16-UC06` + `R16-LK1`；⚠ **Round-3 限定**：未测不变性时**强均值比较**（scalar / strict 层的跨组、跨 `t` 均值差）标 `UNDEFINED`；**不得**把它扩大为"任何动态结论都未定义"，也**不得**因此认为 aliasing 已被排除 |
| **I9** | `Constraint` 的 effect | constraint 是"未发生的事件"，无反事实对照无 estimand | 协议**不提供** constraint 效应的 estimand；`NOT_MAPPED` 是唯一诚实的行状态 |
| **I10** | "为什么这段关系如此"的机制归因 | 不同 DAG / `F` 形式可给相同拟合 | `R16-UC08`：任何 `F` 表述必须写成"在指定 instrument、采样协议与 `F` 形式假设下，与数据一致的 `F` 之一" |
| **I11** | 构念 / 角色 / 情境 / 文化的正交交叉 | 需要正交交叉设计；LHRM 当前数据源不满足 | `cross_context_test` 标 `BLOCKED_BY_DATA`（P04 §7 第 6 条） |
| **I12** | 状态转移的**速率** | 同一序列在不同 lag / 分辨率下给出不同 AR 系数；若 `tau` 是 history branch 或回忆时间，"lag"不是物理时差 | `R16-ID06`：所有滞后陈述必须携带真实时间间隔 |
| **I13** | "完整轨迹"的陈述 | 任何"完整轨迹"都是 MAR 下的外推；FIML 也不例外 | `R16-UC07` 强制 MNAR 敏感性并列报告 |
| **I14** | dyad 内两条有向边的非独立来源分解（person 层 trait vs dyad 层特殊） | 同一 dyad 内至少有 person 层与 dyad 层两个来源；Mplus DSEM 是 two/three-level，dyad 当 cluster 时两条边在同一 level，**无法**同时分离 | **LHRM 最难的一个识别缺口。** 协议只能要求显式声明随机结构，**不能**解决 |
| **I15** | 从单个案例估计现实概率 | `n = 1` 无 hazard / transition estimand | `R16-ID02` + P03 §11（明列的非目标） |
| **I16** | 观测数据给出规范性判断 | 描述/预测/因果三类 estimand 互不相同；规范性不在其中 | `R16-OC02` 三值封闭表；规范性输出只能标 `DOWNSTREAM_READOUT`（P03 §1） |
| **I17** | "trait 还是 state"这个二分本身 | TSE 会 improper solution；LST-AR 适用面窄；TSO 仍有 occasion factor stability 问题 | 协议只允许作为**模型依赖的分解比例**报告 + 报模型敏感性（`B6`） |

---

## 14. 显式非主张（Explicit non-claims）

1. **不主张**本协议已通过 Architect 或 Human 审阅。它是 `CANDIDATE`。
2. **不主张**本协议已被任何数据集执行过。**本报告零数据接触。** §8 的表格是模板。
3. **不主张** §3.1 的六值词表已被接受。它是对 `#29` 四值词表的**扩展请求**。
4. **不主张** §3.2 的 `directionality_class` 已在项目中被采纳。它是本报告的新字段。
5. **不主张** L1–L8 复现了 S01 的八分类（S01 图 1 确切标签未取得）。**Round-3 加强**：L1–L8 **也不**声称是
   任何已取得分类学的完整实例；它们是本协议**自行构造的非穷尽**规则集，与外部分类的对应关系 `NOT_ESTABLISHED`；
   L1–L8 ↔ S01 八分类的映射本身标 `NOT_OPENED`。
6. **不主张** pairfam / SHARE / HARP 能标定 LHRM 的关系状态参数（R04：把「结构合适」升格为「参数可标定」是越界；U15 未核实）。
7. **不主张** speed dating 的 `dec` / `match` 等同于 LHRM 的 attraction / trust / dedication（R04 明文：那是模型假设，不是证据）。
8. **不主张** 任何合规判定。§9 是**文本层面的事实记录 + 工程后果推导**；具体项目的合规判定需法务。
9. **不主张** 三个 `CALIBRATION_READY` 数据集的使用条款未来不变（SHARE CoU §12 写有 21 天生效的变更机制）。
10. **不主张** 本协议能替代 `#29` 的 Gate。Gate 四条由 Architect 与 parent 判定。
11. **不主张** §13 的 17 条中任何一条被本协议解决。它们被逐条登记为**硬边界**。**Round-3 加强**：§12 的 21 条与 §13 的 17 条都是**转录件**，不得计为本协议的交付项（见 §12 顶部的记账表）。
12. **不主张** 本协议对 `F-SELF20`（schema 层归属可能本身错误）有任何防线。R17 F3 的判断被原样登记。**Round-3：这一条被提升为本协议的首要交付物**（§12 顶部），因为它是三份报告里最诚实的一句话。
13. **不主张** 读过 LHRM issue #20 / #21 / #22 的任何内容。
14. **不主张** R03 / R04 / R05 / R06 / R07 / R15 / R17 的结论被本报告独立复核（读的是 packet 文本）。
15. **不主张** S23（Joel et al. 2020）正文的五条实证结论（书目已核实，正文未读；结论经转述）。该来源在 `R16-LK5` 与 `B3` 中 load-bearing。**Round-3：标 `PENDING_EVIDENCE_CHECK (R3-E3)`** —— 该来源正在被 sibling child 复核；本报告**既不主张也不否认**其五条结论。
16. **不主张** 本协议覆盖完整的 dataset landscape 或完整的 leakage 分类学。
17. **不主张** 文献数量或 LLM 一致度构成验证。
18. **（Round-3）不主张** `B2_STABLE_LEVEL` 曾击败过任何候选，也不主张它被 `B1` 在所有报告口径下严格支配。§7.0 记录了两条限定。
19. **（Round-3）不主张** `G1_BLOCKED_FORWARD` 无效。它是合法几何，Round-3 只把它从"首选默认"降级为带标签的降级几何。
20. **（Round-3）不主张** `G4_DYAD_PURE_FORWARD` 在任何现有数据集上可行。它是**默认**；"默认不可用"必须落到 §6.2 记账规则第 2 条，不得默认掉。
21. **（Round-3）不主张** 本协议已防住 holdout 自适应复用泄漏。`FZ-1` 的持有者与可审计性在原文中未定义（`F-14` / `NOT_ENFORCEABLE_AS_WRITTEN`）；L7 的实现条款（§4.1）是**本轮新增的提案**，尚未被裁决。
22. **（Round-3）不主张** §3 的三组枚举是封闭受控表。它们不是；缺口逐条写在 §3.5。
23. **（Round-3）不主张** §11.2 的 `TBD_AT_FZ1` 许可仍有效。它已被撤回（`NOT_ENFORCEABLE_AS_WRITTEN`）。
24. **（Round-3）不主张** §4 的 leakage 规则的 claim-to-source 绑定已被核实。整体 `NOT_OPENED`；§16 的 `CITED_PRIMARY` 只表示**书目**核实。

---

## 15. 剩余未知（Remaining unknown）

见 packet `[FIELD 5]` 的 U1–U16。要点：阻断级的是 U1（关系状态构念清单未核实）与 U3（ICPSR 全站 403）；其余为中低。

---

## 16. 引用列表

> **Round-3 记账：书目核实 ≠ 内容核实。** 下表的 `CITED_PRIMARY` 只表示**书目**
> （作者 / 年份 / 卷期 / DOI / URL）在本 lane 被核实过。
> **它不表示** §4 的 leakage 规则、§7 的 null 依据、§6 的几何依据所依赖的**具体内容陈述**已被逐字比对。
> **本轮（L1–L8 的 claim-to-source 绑定）标 `NOT_OPENED`**（见 §4 顶部）。

**`CITED_PRIMARY`（书目本报告实际核实，2026-09-27）**

1. Kapoor, S., & Narayanan, A. (2023). *Leakage and the reproducibility crisis in machine-learning-based science*. Patterns, 4(9), 100804. `10.1016/j.patter.2023.100804`
2. Kaufman, S., Rosset, S., Perlich, C., & Stitelman, O. (2012). *Leakage in data mining*. ACM TKDD, 6(4), 1–21. `10.1145/2382577.2382579`
3. Bates, S., Hastie, T., & Tibshirani, R. (2024). *Cross-Validation: What Does It Estimate and How Well Does It Do It?* JASA, 119(546), 1434–1445. `10.1080/01621459.2023.2197686`
4. Varoquaux, G. (2018). *Cross-validation failure: Small sample sizes lead to large error bars*. NeuroImage, 180(Pt A), 68–77. `10.1016/j.neuroimage.2017.06.061`
5. Roberts, D. R., Bahn, V., Ciuti, S., et al. (2017). *Cross-validation strategies for data with temporal, spatial, hierarchical, or phylogenetic structure*. Ecography, 40(8), 913–929. `10.1111/ecog.02881`
6. Cerqueira, V., Torgo, L., Mozeta, I., et al. (2020). *Evaluating time series forecasting models: an empirical study on performance estimation methods*. Machine Learning, 109(11), 1997–2028. `10.1007/s10994-020-05910-7`
7. Dwork, C., Feldman, V., Hardt, M., Pitassi, T., Reingold, O., & Roth, A. (2015). *The reusable holdout: Preserving validity in adaptive data analysis*. Science, 349(6248), 636–638. `10.1126/science.aaa9375`
8. Simmons, J. P., Nelson, L. D., & Simonsohn, U. (2011). *False-Positive Psychology*. Psychological Science, 22(11), 1359–1366. `10.1177/0956797611417632`
9. Hussey, I., & Hughes, S. (2020). *Hidden Invalidity Among 15 Commonly Used Measures in Social and Personality Psychology*. AMPPS, 3(2), 166–184. `10.1177/2515245919882903`（**Round-3：书目核实；`L7` 引用的 89% / 4% 数字标 `NOT_OPENED`，不得承担论证重量**）
10. Podsakoff, P. M., MacKenzie, S. B., Lee, J.-Y., & Podsakoff, N. P. (2003). *Common method biases in behavioral research*. Journal of Applied Psychology, 88(5), 879–903. `10.1037/0021-9010.88.5.879`
11. Iacobucci, D., Neelamegham, S., & Hopkins, N. (1999). *Measurement quality issues in dyadic models of relationships*. Social Networks, 21(3), 211–237. `10.1016/S0378-8733(99)00010-6`
12. Barr, D. J., Levy, R., Scheepers, C., & Tily, H. J. M. (2013). *Random effects structure for confirmatory hypothesis testing: Keep it maximal*. Journal of Memory and Language, 68(3), 255–278. `10.1016/j.jml.2012.11.001`
13. Winkler, A. M., Ridgway, G. R., Webster, M. A., Smith, S. M., & Nichols, T. E. (2014). *Permutation inference for the general linear model*. NeuroImage, 92, 381–397. `10.1016/j.neuroimage.2014.01.060`
14. Ogburn, J. W., & VanderWeele, T. J. (2014). *Causal Diagrams for Interference*. Statistical Science, 29(4), 559–578. `10.1214/14-STS501`
15. Aronow, S., & Samii, C. (2017). *Estimating average causal effects under general interference*. Annals of Applied Statistics, 11(4), 805–824. `10.1214/16-AOAS1005`
16. Nosek, B. A., Ebersole, C. R., DeHaven, A. C., & Mellor, D. T. (2018). *The preregistration revolution*. PNAS, 115(11), 2600–2606. `10.1073/pnas.1708274114`
17. Munafò, M. R., Nosek, B. A., Bishop, D. V. M., et al. (2017). *A manifesto for reproducible science*. Nature Human Behaviour, 1, 0021. `10.1038/s41562-016-0021`
18. Wagenmakers, A.-L., et al. (2017). *Promoting reproducibility with registered reports*. Nature Human Behaviour, 1, 0020. `10.1038/s41562-016-0034`
19. Gneiting, T., & Raftery, A. E. (2007). *Strictly Proper Scoring Rules, Prediction, and Estimation*. JASA, 102(477), 359–378. `10.1198/016214506000001437`
20. Cumming, G., & Finch, S. (2005). *Inference by Eye*. American Psychologist, 60(2), 170–180. `10.1037/0003-066X.60.2.170`
21. Maassen, E., D'Urso, E. D., van Assen, M. A. L. M., Nuijten, M. B., De Roover, K., & Wicherts, I. M. (2025). *The dire disregard of measurement invariance testing in psychological science*. Psychological Methods, 30(5), 966–979. `10.1037/met0000624`
22. Laurenceau, J.-P., DiGiovanni, A. M., & Bolger, N. (2026). *Intensive Longitudinal Methods: Toward a Psychological Science of Daily Life*. Annual Review of Psychology, 77, 513–541. `10.1146/annurev-psych-040325-025418`
23. Joel, S., Eastwick, P. W., Allison, C. J., Arriaga, X. B., et al. (2020). PNAS, 117(32), 19061–19071. `10.1073/pnas.1917036117`（**书目已核实；五条实证结论为转述**）
24. SHARE — *Conditions of Use*, last updated 2026-04-30. `https://share-eric.eu/data/data-access/conditions-of-use`（**逐字抓取 §7 全文**）

**`JOIN_LANE`（相对本报告为 `CITED_SECONDARY`）**

25. R03 packet — `R03_packet.md`（instrument family、G1–G10 gap、F1–F12、SD 侧证据）
26. R04 packet — `R04_packet.md`（16 dataset、pairfam / SHARE / HARP detail card、LLM/AI 条款、四条件交集为空）
27. R05 packet — `R05_packet.md`（I1–I17、SD1–SD20、S01–S133、M1–M11、Q1–Q10）
28. R06 packet — `R06_packet.md`（F1–F9、BMR/APES/DVA/RGM/RT、判 A/B/C、U-1…U-8）
29. R07 packet — `R07_packet.md`（稀疏输入不变量、`Computable != Certain`）
30. R15 packet — `R15_packet.md`（fixture metadata 模板、`t0_anchor` / `holdout_policy`、`evidence_channel`）
31. R17 packet — `R17_packet.md`（F1 `MAPPING_FAILURE` 构造上不可达、F2 Joel et al. 五条结论、F3 belief 层实证反向排序）

**`PROJECT` / `ISSUE`**

32. `AGENTS.md`（尤其 `AGENTS.md:24`、`:25`、`:26`、§Validation discipline）
33. `docs/foundation/CURRENT_ARCHITECTURE.md`（§1 / §4 / §6 / §9 / §10 / §11）
34. `docs/foundation/CONSTRUCT_SCOPE_DIRECTIONALITY.md`（§1 / §2 / §7）
35. `docs/validation/VALIDATION_CORPUS_V0_1.md`（12 条材料、`future_leakage_risk`）
36. `docs/validation/fixtures/FIXTURE_001_L0_001_CARTY_FACT_PACKAGE.md`（§2.5 / §2.7 / §4）
37. `docs/validation/fixtures/FIXTURE_003_L1_001_STORYCORPS_PACKAGE.md`（§2 / §3 rules 2,5）
38. `youling/lhrm#29`（`Empirical Validation Lane v0.1`，2026-09-14，state open）

---

## 17. 建议状态

**`PARTIAL`**（`CANDIDATE PROTOCOL`）· **`JOIN LANE`**

- **本 lane 的独立交付（Round-3 重列；Round-1 清单把转录件与独立产物混列，已拆开）：**

  | 类别 | 内容 | Round-1 清单里的对应措辞（逐字保留） |
  |---|---|---|
  | **首要交付物** | **`F-SELF19` / `F-SELF20` / `F-SELF21`** —— 尤其 `F-SELF20`（"如果 schema 的层归属本身错了，本协议的全部 machinery 会忠实地验证一个错误的对象" / 防线列逐字 **"无。"**；`None.` 是英文写法，非原文） | *"21 条失败模式"* —— **Round-3 把这一项提到首位并重新归类**（见 §12 顶部） |
  | 独立设计 | 12 条 ID 规则（`R16-ID01`–`R16-ID12`，含 Round-3 新增 `R16-ID12`） | *"11 条 ID 规则"* |
  | 独立设计 | 6 值 `mapping_status` + 6 值 `directionality_class` + `evidence_channel`（复用 R15）+ 5 字段 uncertainty 块 **+ §3.5 的 `NOT_CLOSED_AS_WRITTEN` 缺口诊断** | *"6 值 … 5 字段 uncertainty 块"* |
  | 独立设计 | 8 条 leakage 规则 + §4.1 的 5 条 `L7` 实现条款 + `L3(d)(e)(f)` 三条 Round-3 补漏 | *"8 条 leakage 规则每条带真实引用"* —— **该措辞被取代**（见下） |
  | 独立设计 | 5 条 outcome 规则 | *"5 条 outcome 规则"* |
  | 独立设计 | **4 种** split 几何（Round-3 补入 `G4_DYAD_PURE_FORWARD` 为默认）+ 3 个降级标签 | *"3 种 split 几何"* —— **计数被取代** |
  | 独立设计 | **11 个 null**（`B0`–`B8` = 9 个 `B*`，+ `N7` + `N8`；含改名 `B2_STABLE_LEVEL` 与新增 `B8_LEVEL_PLUS_RW` / `N7` / `N8`） | *"8 个 null"* —— **计数被取代** |
  | 独立设计 | 8 条不确定度要求 | *"8 条不确定度要求"* |
  | 独立设计 | 16 字段 `FREEZE_RECORD` + 偏离政策 + **Round-3 的 `FZ-1` 规格 (a)–(f)** | *"16 字段 `FREEZE_RECORD` + 偏离政策"* |
  | 独立设计 | 5 行真实变量 worked example（含 2 个明确的 `UNVERIFIED_AS_OF` 而非编造） | 同 |
  | 独立设计 | **14 项**不足（Round-3 新增 `F-13` / `F-14`） | *"12 项不足"* —— **计数被取代** |
  | 独立设计 | R04 access/rights 的 4 条可执行性判定 | 同 |
  | **转录件（不计）** | §12 的 21 条 `F-SELF`（其中 18 条转自 `05 §6` / `R17 F1`）+ §13 的 17 条 `I`（转自 `05 §5`） | *"21 条失败模式；17 条不可建立事项"* —— **Round-3 判定为转录件** |

- **三处被取代的措辞（逐条）：**
  1. ~~*"8 条 leakage 规则每条带真实引用"*~~ → **取代**：L1–L8 的 `依据` 列是**指针 / 书目清单**；
     **claim-to-source 绑定本轮未核实 ⇒ 整体 `NOT_OPENED`**；且 L1–L8 **不**声称是任何外部分类学的
     完整实例（与 S01 八分类的对应关系 `NOT_ESTABLISHED`）。见 §4 顶部。
  2. ~~*"3 种 split 几何"*~~ → **取代**：4 种；默认几何为 Round-3 新增的 `G4_DYAD_PURE_FORWARD`；
     `G1_BLOCKED_FORWARD` 由"首选默认"降级为带 `WITHIN_DYAD_TEMPORAL_EXTRAPOLATION_ONLY` 标签的降级几何。见 §6.1 / §6.2。
  3. ~~*"8 个 null"*~~ → **取代**：**11 个**（`B0`–`B8` = 9 个 `B*`，+ `N7` + `N8`；计数可复算）。见 §7.1。

- **故非 `SUCCESS` 的理由**（四条；第 4、5 条为 Round-3 新增）：
  1. **U1 / F-01** — 三个 `CALIBRATION_READY` 数据集的关系状态构念清单未核实，§8 的映射表因此是模板而非规格。协议的核心交付物之一**今天填不出来**。
  2. **F-03** — `#29` F 层的跨数据集外部验证在结构上不可执行（四条件交集为空）。⚠ Round-3 记账（`X-14`）：这是**本次检索**的结构性结果，**不是**"该交集在领域中为空"。
  3. **F-06 / F-07** — R03 G9 使 L6 不可满足；R05 I4/I14 使 P04 §1 的方向性分解不可识别。协议**不能**验证 LHRM 最核心的表示选择。
  4. **F-08 / `F-SELF20`** — R17 F1 与 R17 F3 表明：现有 Case Bank 不能作本协议的前置健全性检查，且 schema 的层归属本身可能错误。本协议对后者**无防线**。
  5. **（Round-3 新增）F-13 / F-14** — 默认几何 `G4_DYAD_PURE_FORWARD` 在现有数据现实下很可能不可用（须落到降级几何并贴标签）；`FZ-1` 的持有者与可审计性在原文中未定义（`NOT_ENFORCEABLE_AS_WRITTEN`）。⇒ **本协议目前不得声称"已防 holdout 自适应复用泄漏"。**
- **不是 `NEGATIVE_RESULT`**：本 lane 不是在检验一个假设，而是在设计协议；上述不足是**设计被数据现实约束**的记录，不是某个主张被证伪。
- **不是 `BLOCKED`**：唯一今天可完整执行的路径（速配数据 + 结构性产出，判定 E2）未被任何 access gate 阻断。
- **不是 `NOT_OPENED`（整份）**：只有 §4 的 claim-to-source 绑定、§3.5 引用的 review-r2 判定码、以及 §13 提到的 `#29` D 层正文是 `NOT_OPENED`；本协议自身的**设计决定**不依赖任何未打开的来源。

**给 Architect 的具体裁决请求（按优先级）：**

1. **裁决 §3.1 的六值词表是否可以取代 `#29` 的四值。** 具体是：接受 `COVARIATE_ONLY` 与 `CONFLICTED` 两个新成员（否则违反 `AGENTS.md` 关系 label 规则），以及把 `#29` 的 `DIRECT_PROXY` 拆为 `DIRECT_ITEM` / `BEHAVIORAL_PROXY`。**Round-3 追加（同批裁决，见 §3.5）：** `mapping_status` 是否为可并存多值；`directionality_class` 是否加 `SELF_REPORTED_EDGE` / `BELIEF_ABOUT_EDGE`；`uncertainty` 是否拆出独立 `reliability_class`；三组枚举是否并列适用性轴（X-5 / C-P5）。
2. **裁决是否接受新增字段 `directionality_class`。** 本报告主张这是必需的，因为 R03 F1 表明主流工具在结构上不是 directed-edge measure，而 `mapping_status` 单独无法表达这一点。
3. **裁决 `R16-ID11`（`FREEZE_RECORD` 不得含个体级数据行）。** 它是 SHARE CoU §7 + `AGENTS.md:24` 的直接后果，但代价是外部第三方无法独立复核映射行。若不接受，需要一条经法务确认的替代披露路径。
4. **认领 U1（关系状态构念清单）。** 这是把本报告从 `PARTIAL` 推向可执行的第一块多米诺骨牌；没有它，§8 永远是模板。
5. **裁决是否把速配数据定为 `G-NO-TEMPORAL_AXIS` dry run。** 依据 §9 判定 E2，这是唯一零门槛、今天可跑通的路径。
6. ~~**记录 §11.2 第 12 字段 `estimator_family` 与 R06 §12 的依赖关系。** … 要么等 R06 的裁决，要么接受 `TBD_AT_FZ1` 占位。~~ → **Round-3：该请求已被本轮裁决取代（`NOT_ENFORCEABLE_AS_WRITTEN`）。** `TBD_AT_FZ1` 许可**已撤回**；新请求是：**裁决 §11.2 (e) 的二选一 —— (i) `FZ-1` 排在转移律形式裁决之后，还是 (ii) `estimand` 独立于 `estimator_family` 冻结。** 本 lane 默认 (ii)，理由见 §11.2 (e)。
7. **（Round-3 新增）裁决 `FZ-1` 的持有者角色。** §11.2 (c) 要求该角色与分析者可区分。**这是制度裁决，不是研究问题。**
8. **（Round-3 新增）裁决 `N7` / `N8` 的 id 前缀。** 本轮按 `X-6` 的字面采用 `N7_` / `N8_`，与既有的 `B*` 家族不同族。见 packet 的 `open_questions_for_architect`。

**明确不建议的动作：** 不要在 U1 解决之前把本报告的映射表当作规格使用；不要把 `FREEZE_RECORD` 的存在当作"已防 leakage"——`F-SELF11` 与 `F-14` 表明防 leakage 是制度问题而非备忘录问题，且在 `FZ-1` 规格落地前该防线**尚不存在**。
