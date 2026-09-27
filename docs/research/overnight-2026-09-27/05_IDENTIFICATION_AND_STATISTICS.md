# 05 — 识别与估计：统计方法视角

> **Status:** `RESEARCH_CANDIDATE` — 未经 Human / Architect 审阅，不得当作已确立结论、参数或公式。
> **As of:** 2026-09-27
> **Work:** `youling/lhrm#30@overnight-opencode-exploration-swarm-v1`
> **Role:** Research (Wave 1, lane R05)
> **Scope:** 统计识别 / 估计方法。本文件**不**改 ontology、不改 canonical docs、不给参数值。
> **Read-only confirmation:** 本 lane 只读 `AGENTS.md`、`docs/foundation/*`、`docs/validation/*`、`docs/research/*`；未修改 `docs/` 下任何文件；无 GitHub 写操作；未读 `#20/#21/#22`。

**证据标注**：`CITED_PRIMARY`（本次实际打开源并读到支持句）/ `CITED_SECONDARY`（引文串来自已读同行评审文献）/ `AGENT_RECALL`（先验，未核实）/ `UNKNOWN_AS_OF`（时间敏感事实未核实）。核实日期 2026-09-26 / 2026-09-27。

---

## 0. 读法

LHRM 第一阶段的目标是 *"在任意时刻，对两个具体人及其关系进行结构化、方向化、时间索引、保留 Unknown 与不确定性的数学状态表示语言"*（`CURRENT_ARCHITECTURE.md` §1）。这不是"估计一个参数"，是"定义什么可以估计、什么不能"。

因此本文件的主交付**不是方法推荐，而是边界**。

建议阅读顺序：§1 识别约束 → §2 十个真实问题 → §3 覆盖矩阵 → §4 逐方法属性表 → **§5 识别不可能清单** → §6 自我欺骗模式 → §7 活跃争议 → §8 软件指针 → §9 非主张 → §10 剩余未知 → §11 引用。

---

## 1. 为什么统计识别对 LHRM 是决定性约束

LHRM 的动力学方程（`CURRENT_ARCHITECTURE.md` §6）

```text
X_(t+1) = F(X_t, Action_t, Event_t, Belief_t, Constraint_t, Environment_t)
```

与 §3 的

```text
Reality != Observation != Belief
```

合起来，方程里同时有**四类不可观测**：

| 层 | 不可观测的东西 | 任何统计方法最多能给什么 |
|---|---|---|
| **L1 latent state** | `Z[k,i,j,t]` 的真值 | 给定 instrument 的 `E[state \| report_function]`；或该报告函数本身（measurement model / IRT curve） |
| **L2 report function** | 提问方式、item wording、情境依赖、对方报告的准确性 | 只在 instrument 固定下不变。跨 `t` 比较需测量不变性（Q7） |
| **L3 dynamics form** | `F` 的函数形式（线性？饱和？局部可加？可逆？） | **不能**由数据学习。形式是理论 / 设计承诺 |
| **L4 counterfactual** | 未发生的"如果" | 观测面板**不能**给 |

**因此 LHRM 动态结论的正确书写规范是：**

```text
在指定 instrument I、采样协议 Π、F 形式假设 H 下，
与数据 D 一致的 F 之一是 F_1。
```

这不是免责套话，是识别事实。它把 `AGENTS.md` 两条规则
（*"Do not label an unvalidated formula, parameter, weight, probability, causal relation, distance metric, normalization rule, or state transition as scientifically established"*、
*"Distance/weight/score/probability are downstream readouts"*)
变成可检查的书写规范。

---

## 2. LHRM 真实要问的 10 个统计问题

| Q | 问题 | canonical 来源 | 方法学归属 |
|---|---|---|---|
| **Q1** | actor 的 `Z[k,i,j,t]` 是否预测 partner 的 `Z[k',j,i,t+1]`，**超出 partner 自身轨迹**？ | `CURRENT_ARCHITECTURE.md` §4：`Z[k,i,j,t]`，`A->B != B->A` | APIM partner effect / cross-lag 的 within-person 分解版 |
| **Q2** | 构念 k 的个体间差异是稳定 trait 还是围绕个体均值的 state？ | `AGENTS.md` 冗余原则 | trait-state-error / TSO / STARTS |
| **Q3** | 多少 person 间差异、多少 **pair 特定**差异、多少 occasion 特异差异？ | `CONSTRUCT_SCOPE_DIRECTIONALITY.md` §2 `Asymmetry_k(A,B)` | SRM relationship effect / 三层分解 |
| **Q4** | person 间差异里有多少是**测量误差**？ | `AGENTS.md` *"Unknown/missing data must remain explicit"* | measurement model / IRT / multi-indicator / within-person reliability |
| **Q5** | 转移律形状：惯性、跨构念耦合、趋势 / 曲率、regime 切换、循环 / 回返？ | §6 `F(...)`；§8 `tau=(history_id, local_time)` | DSEM / ARMA / LMM / cycles-DSEM |
| **Q6** | pair-level 的**解体 / 重构 hazard** 随什么变化？ | §8、§4 `PairState_(i,j)`；`AGENTS.md` label 是 coarse readout | PH / discrete-time hazard / competing risks / latent-initiation |
| **Q7** | `Z[k,i,j,t]` 在不同 `t` / 关系类型 / 文化 / 角色下**是否同一构念**？ | `AGENTS.md` *"High-level labels … are not assumed to be primitive variables"*；`CONSTRUCT_SCOPE_DIRECTIONALITY.md` §7 | 纵向测量不变性 / alignment / DIF |
| **Q8** | 部分观测下 `Z` 的**后验 + 不确定性 + evidence** 如何表达？MNAR 下有多稳？ | `AGENTS.md` *"never silently coerce missing information into neutral/perfect-match values"*；§9.6 | FIML / MI / selection / pattern-mixture + sensitivity |
| **Q9** | 在给定关系状态下，**Environment / Event / Action** 与下一状态的条件关联有多强？ | §6 `F(X_t, Action_t, Event_t, Belief_t, Constraint_t, Environment_t)` | time-varying covariate / treatment-confounder feedback |
| **Q10** | `MutualX` / `Asymmetry` 作为**派生量**是否在统计上零自由度？ | `CONSTRUCT_SCOPE_DIRECTIONALITY.md` §2 *"优先由两条有向边派生"* | derived-variable 检验 |

---

## 3. 方法族与覆盖矩阵

### 3.1 方法族（矩阵的行）

| ID | 方法族 | 定位 | 主要指针 |
|---|---|---|---|
| **M1** | APIM / SRM | "谁对谁的什么"的 actor / partner / relationship 三成分形式；LHRM 方向性直觉的**测量学对应物** | Kenny (2018)；Kashy & Cook (2005)；Kenny (1994) |
| **M2** | 多层 within/between 分解（long-format MLM + Mundlak/contextual + latent centering） | 在估计层面分开"person 内变化"与"person 间差异" | Hamaker & Muthén (2020)；del Rosario & West (2025) |
| **M3** | CLPM / RI-CLPM / GC-CLPM / LCM-SR / STARTS / ARTS（含 multi-indicator 测量版） | 固定 lag 结构下的双向 prospective 关联；**本文件争议最大处** | Hamaker et al. (2015)；Lucas (2023)；Lüdtke & Robitzsch (2022)；Orth et al. (2021)；Robitzsch & Lüdtke (2025) |
| **M4** | DSEM / RDSEM / 连续时间 / 三层 / 含环 / floor-effects DSEM | state-space + 动态因子 + 多层的统一；ILM 默认主力 | Asparouhov, Hamaker & Muthén (2018)；Asparouhov & Muthén (2026)；Muthén et al. (2025) |
| **M5** | State-space / Kalman / dynamic factor / HMM-LMM / LTA / regime switching | 潜 trait-state 分离与离散 regime 转移 | Cole et al. (2005)；Vermunt (2004)；Bartolucci et al. |
| **M6** | Survival / event-history / hazard / competing risks | pair-level 解体 / 重构的事件时间风险 | Felmlee et al. (1990)；Lillard et al. (1993) |
| **M7** | ILD / ESM / EMA 设计与分析要求 | 决定 Q1–Q5 的**可检出性** | Bolger & Laurenceau (2013)；Myin Germeys & Kuppens (eds.)；Sonnentag et al. |
| **M8** | 测量：IRT / bifactor / CFA / 不变性 / argument-based validity | 决定 Q4、Q7；是 Q1–Q3 的前提 | Reise & Tucker-Drob (2010)；Kane (2013)；Robitzsch (2023) |
| **M9** | 缺失：FIML / MI / selection / pattern-mixture | 决定 Q8；威胁 Q1–Q5 的可辩护性 | Carpenter & Kenward (2007/2011) |
| **M10** | 因果：g-formula / MSM / g-estimation / target trial / interference | 决定所有 Q1–Q5 能说到哪一步 | Robins & Hernán (2020)；Sobel & Korper (2010) |
| **M11** | 元科学：multiverse / specification curve / power / 不确定性传播 | 决定任何单一结论的可报告性 | Steegen et al. (2016)；Robitzsch (2022)；Peugh & Litson (2026) |

### 3.2 覆盖矩阵（methods × questions）

图例：`●` 主要落点 ｜ `○` 可用但非首选 ｜ `△` 只能作诊断 / 压缩投影 ｜ `—` 不相关。
所有 `✗` 项在 §5 有结构性理由。

| | Q1 方向溢出 | Q2 trait/state | Q3 person/dyad/occasion | Q4 测量误差占比 | Q5 转移形状 | Q6 解体 hazard | Q7 测量不变性 | Q8 缺失/Unknown | Q9 Env/Event | Q10 派生零自由度 |
|---|---|---|---|---|---|---|---|---|---|---|
| M1 APIM/SRM | ● | △ | ● | ○ | △ | △ | ○ | ○ | ● | ○ |
| M2 多层 within/between | ● | ● | ● | △ | ○ | △ | — | ○ | ● | ○ |
| M3 CLPM 家族 | ● | ● | ○ | ○ | ● | △ | ● | ○ | ● | ○ |
| M4 DSEM / RDSEM | ● | ● | ● | ● | ● | △ | ○ | ● | ● | ○ |
| M5 State-space / LMM | ○ | ● | ● | ● | ● | ○ | ○ | ● | ○ | △ |
| M6 Survival / hazard | △ | — | ○ | — | △ | ● | — | ● | ● | △ |
| M7 ILD / ESM 设计 | ● | ● | ● | ● | ● | ○ | ● | ● | ● | — |
| M8 测量 | ○ | ○ | ○ | ● | — | — | ● | ○ | — | — |
| M9 缺失 / 选择 | ○ | — | — | — | — | ● | — | ● | ○ | — |
| M10 因果 / interference | ● | ○ | ○ | — | ○ | ● | — | ● | ● | — |
| M11 元科学 | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |

---

## 4. 逐方法属性表

每个单元格记录五项：**可识别 / 所需数据结构 / 关键假设 / 失败模式与已知误用 / 不得因果主张什么**。未列出的 (方法, 问题) 组合表示该方法对该问题无增量贡献。

### M1 — APIM 与 SRM

**形式**：个体 i 的 outcome 由自己的 predictor（actor effect）与 partner 的 predictor（partner effect）共同预测。Kashy & Cook (2005) 脚注 1：*"Although we use the term* influence, an actor or partner path in the model *may simply indicate a predictive relation, not necessarily a causal one*."*

**术语警告**：同文脚注 3 明确 APIM 的 actor / partner effect **不要**与 Social Relations Model 的同名术语混淆 —— SRM 中它们是 *"components in a measurement model (i.e., latent variables or factors) rather than causal variables"*。

**SRM 三成分**（Kenny 自述）：`perceiver effect` = "how the person tends to see others"；`target effect` = "how a person is seen in general by others"；`relationship effect` = "how a perceiver uniquely sees the target"。Malloy & Kenny (1986) 把 SRM 定位为 *"a component model (a special case of generalizability theory)"*。

| Q | 可识别 | 所需数据结构 | 关键假设 | 失败模式 / 误用 | 不得因果主张 |
|---|---|---|---|---|---|
| Q1 | 严格双 entry 设计下 actor / partner effect（2 波时为 person 间水平） | 2 名可区分成员，各自在 ≥2 波同时报告 X 与 Y | 双方同测量；非独立来自 dyad | partner path 被称为 influence（官方脚注禁止）；基本 APIM 2 波**饱和**（just-identified），全局 fit 无信息 | 不得说 partner effect = A 影响 B。只能说"B 的 `X_t` 与 A 的 `Y_{t+1}` 的**预测关联**" |
| Q3 | SRM 的 relationship effect（**需 round-robin**）；APIM 本身**不**分离三者 | SRM：每人须评价**多个 target**，target 与 perceiver 集合可交叉 | SRM 需"each person interacts with multiple partners" | 单一 target 时 perceiver / target / relationship **不可分离**（**I4**）；把 APIM 的 actor effect 当 SRM 的 perceiver effect | 不得把 relationship effect 说成"这段关系特有的因果成分" |
| Q4 | SRM 把 reliability 显式建模；APIM 的 `rho` 是成员间残差相关，**不是**测量误差 | SRM 需 round-robin | 误差独立于效应 | 误把 `rho` 当 reliability；把 alpha 当 validity | 不得 |
| Q7 | 需在 APIM 框架内另跑 invariance 层级序列 | 多波 multi-indicator | 同上 | 把 invariance 失败当"关系变了"（**SD3**） | 不得 |
| Q9 | partner effect 即 partner 侧 covariate 溢出 | 双方 + 环境重复测量 | covariate 无时间变化混杂 | 把 actor / partner 效应不对称解释为"谁更主动" | 不得把不对称当权力 / 主动性证据 |

**对 LHRM 的直接含义**：`CONSTRUCT_SCOPE_DIRECTIONALITY.md` §1 的分解式是 SRM 结构的字面重述。这**证明方向性分解有成熟测量学对应**，也**暴露一个硬缺口**（**I4**）：两人 dyad 只有 2 条有向边、2 个自由度，装不下 3 个成分。APIM 提供的唯一稳健成果是"两个方向的分数不被强行合并成总分"，与 `AGENTS.md` *"Relationship labels/statuses … are coarse-grained readouts, not substitutes for bottom-level state"* 方向一致。

**反共识证据**：Kenny (2018) abstract —— *"Although the APIM is the most popular method for dyadic analysis, it should be recognized there are alternatives that should also be considered."* → **不可**把 APIM 当 LHRM 方向性的"标准答案"。

### M2 — 多层 within-person / between-person 分解

Hamaker & Muthén (2020) 证明 **FE vs RE 之争与 grand-mean vs person-mean centering 之争是同一问题的两面**；比较 long-format 的 L1–L4 与 wide-format 的 W1–W4 共 8 个做法，推荐 **latent within-person centering（L3b / W3）** 而非 sample-mean centering（L3a），因为 sample mean 不是 latent mean 的无偏估计（引 Lüdtke et al. 2008），下层样本量小时尤其严重。L3b/W3 与 Mundlak contextual model L4/W4 分别估计 within-slope、between-slope 与 contextual effect（= between − within），因此可**直接检验"是否需要 FE"**。

| Q | 可识别 | 所需数据结构 | 关键假设 | 失败模式 / 误用 | 不得因果主张 |
|---|---|---|---|---|---|
| Q1 | dyadic long-format MLM：partner 的 person-mean-centered 分数作 predictor，双向同时建模 | 双方 × ≥3 波 long format；**dyad 为分析单位** | random intercept 与 time-varying predictor 的关系（endogeneity） | 遗漏协方差项忽略 dyad 数据最核心的相依性：*"Excluding the covariances overlooks some of the interdependence in the data, such as how changes in dyad members' responses are related, which is a core feature of dyadic data"*；只有方差没有协方差会低估不确定性并可能偏方向 | 不得把 FE 系数叫"within-person 因果效应" |
| Q2 | person-mean-centered 残差 = within；random intercept = between | ≥3 波 | Mundlak：RE 的 `u_i` 与 time-varying predictor 相关时会偏 | 只做 person-mean centering 而不放开 `RI ↔ predictor` 相关（= 隐含 RE 假设） | 不得 |
| Q3 | 三层：dyad ∈ pair ∈ person；可加 dyad-level random intercept | dyad 内两成员 | 正态；协方差可估 | 不收敛常因随机结构过参数化 / 协方差近零 / singularity | 不得把 dyad-level 方差解释为"关系特有的因果来源" |
| Q5 | AR / cross-lag / random slope | 足够波数 | **需要 random slope**（只放 random intercept 会强迫所有人同一变化模式） | 用 p 值挑最终随机结构 | 不得 |
| Q9 | 天然支持 time-varying covariate | 双方 + 环境重复测量 | 同上 | 用 REML 比较只改随机效应的模型；改固定效应须改用 ML | 不得 |

**操作规则**（del Rosario & West 2025 原文）：*"do not use p values to decide for the final model. Instead, use theory and model convergence to guide your decisions."*；*"models using restricted EM can be compared only if they differ in random effects; changes to the fixed effects require using maximum likelihood, which is considered more prone to bias."* 先最大化、再逐步削减随机结构；**变动固定效应时模型整体拟合可能以难以察觉的方式改变**。

### M3 — CLPM 家族

#### 3.1 争议地图（不给伪共识）

| 阵营 | 核心主张 | 指针 |
|---|---|---|
| **A. 弃 CLPM** | 若构念有 trait-like 时间不变稳定，CLPM 的 AR 路径不代表 within-person 关系，对 **(a) 是否存在因果关系、(b) 谁因果占优、(c) 影响符号** 三项**全部**可给出错误答案 | Hamaker, Kuiper & Grasman (2015), `10.1037/a0038889` |
| **B. 弃 RI-CLPM** | RI-CLPM 需**极强**混杂假设才能控制未观测 time-invariant 混杂；CLPM 加 **lag-2 效应**在"所有相关协变量已测"时更充分地控制延迟效应；且 **RI-CLPM 估计的是不同因果 estimand** —— "increasing the exposure by one unit **around the person mean**"，"typically **less relevant** … because it only captures temporary fluctuations around the individual person means and ignores the potential effects of causes that explain differences between persons" | Lüdtke & Robitzsch (2022), `10.1080/10705511.2022.2065278` |
| **C. 反驳 B** | Orth et al. (2021) 与 Asendorpf (2021) 的辩护不成立：CLPM **嵌套在** RI-CLPM 内；无 stable-trait 方差时 RI-CLPM **退化为** CLPM；两者**未给出任何 DGP** 使 CLPM 正确而 RI-CLPM 有偏；Asendorpf 的 "severely underestimated" *"provided no evidence"*。现实假设下 CLPM *"very likely to find spurious cross-lagged effects when they do not exist"* | Lucas (2023), `10.1177/25152459231158378` |
| **D. 中间路线** | 不应用 fit 选模型（RI-CLPM 嵌套更多、多 3 df，*"with increasing sample size, the RI-CLPM necessarily fits significantly better"*）；应按**理论**选择。若 parental warmth 极稳定，RI-CLPM 的 cross-lag **原理上无法**表达"温暖养育 → 自尊发展" | Orth, Clark, Donnellan & Robins (2021), `10.1037/pspp0000358` |
| **E. illusory between-person** | RI-CLPM 的 between-person 分量 *"can occur **only** due to the presence of time-varying covariate processes that are **omitted** from the analysis model"*；作者解析导出**充要条件**并系统检验，故称 **illusory**；追溯到 Bailey et al. (2023) 的模拟 | Robitzsch & Lüdtke (2025), `10.1080/10705511.2024.2379495`（CC-BY） |
| **F. 当前状态** | Hamaker 本人出《The within-between dispute in cross-lagged panel research and how to move forward》；Andersen 给出 LCM-SR 与 RI-CLPM 的等价性分析 | Hamaker (2026), `10.1037/met0000600`；Andersen (2022), `10.1037/met0000285` |

#### 3.2 可直接引用的结构事实

- **波数下限**：CLPM 2 波即可但**饱和** —— *"We found that **45% of the studies** that we examined estimated the CLPM based on only two waves of data. In these cases, the CLPM is saturated, and hence **no statements regarding model fit can be made**."* RI-CLPM **至少 3 波**（3 波时 1 df）。
- **嵌套链**：`CLPM ⊂ RI-CLPM ⊂ STARTS`；`RI-CLPM = STARTS − state`；`CLPM = STARTS − trait − state`；`ARTS = STARTS − stable trait`。Lucas, Weidmann & Yang 建议 *"the infrequently used ARTS may often be a better alternative"*，并预测 *"estimates of cross-lagged paths from the RI-CLPM will be larger than those from the ARTS"*。
- **RI-CLPM 的可疑假设**：RI 隐含"完全稳定 trait"，被讥为 *"an [un]realistic assumption, specifically that the between-person variance is perfectly stable"*，但承认 *"some portion of the systematic between-person variance will be included in the residualized factors"*。
- **CLPM 解释性**：Allison (2021) —— ARCL 的 cross-lag 估计是 *"a weighted—and typically uninterpretable—amalgam of between- and within-person associations"*。
- **2024 新进展**：Muthén, Asparouhov & Witkiewitz (2024), *Cross-lagged panel modeling with binary and ordinal outcomes*, `10.1037/met0000701`。
- **3 步建模策略**（Hamaker et al. 2015 建议）：① 至少 3 波；② 先只约束均值、协方差自由，以判断是否有 over-time 结构性变化；③ 再比较 CLPM 与 RI-CLPM 以判断是否存在 trait-like 稳定差异。

| Q | 可识别 | 所需数据结构 | 关键假设 | 失败模式 / 误用 | 不得因果主张 |
|---|---|---|---|---|---|
| Q1 溢出 | 仅在**同一 dyad 内**把 partner 状态作为 cross-lag predictor；若用 CLPM，该估计是 person 间与 person 内的混合 | 双方 × ≥3 波；dyadic 扩展需每人各一套 RI + 互相 cross-lag | RI：完全稳定 trait（可疑） | 2 波 CLPM 谈 fit；把 RI-CLPM cross-lag 叫"person 内溢出因果" | 不得叫 causal effect |
| Q2 trait/state | RI-CLPM 的 random intercept **形式上**就是 trait；STARTS 另加 state 分量 | ≥3 波（RI-CLPM）；≥4–5 波（STARTS/ARTS 更稳） | RI-CLPM 假设无 occasion-specific 方差 | 用 `RIx` 直接写"person i 的 trust trait" —— 可能 illusory（**SD6**） | 不得把 `RIx` 当"已证实的稳定 trait" |
| Q3 person/dyad | dyadic RI-CLPM 需两套（一人一套）；dyadic 扩展虽 *"straightforward"*，但 dyadic RI-CLPM / dyadic LCM-SR 的实证应用**极少** | 双方 × ≥3 波 × multi-indicator | 同上 | 误把单人 RI-CLPM 结论当 dyadic 结论 | 不得 |
| Q7 不变性 | multi-indicator RI-CLPM **要求先做** weak 乃至 strong factorial invariance over time | 多指标 × 多波 | 载荷跨波恒定 | 未测不变性就做 latent RI-CLPM | 不得 |
| Q8 缺失 | 常用 `missing='ML'`（FIML） | 允许 MAR | MAR | 用 FIML 掩盖 MNAR | 不得把 FIML 结果称为对 MNAR 稳健 |
| Q9 | time-varying covariate 可放入；但协变量多时模型会 *"quickly become unwieldy, leading to large statistical models that rely on many causal and statistical assumptions"*，此时应改走 propensity-score / MSM 路线 | — | 同上 | 硬塞 10+ 个 TVC 而不转 MSM 路线 | 不得把"控制了 TVC"说成"控制了混杂" |

**LHRM 结论（`AI recommendation`）**：**不应把任何单一 cross-lagged 模型当"关系动态的证据"**。若做，必须：① ≥3 波；② 先报测量不变性层级序列；③ 同时报告 CLPM / RI-CLPM / STARTS 并给差异；④ 所有 cross-lag 标为 **predictive association**；⑤ 检查 illusory between-person 的省略型 TVC 充要条件。

### M4 — Dynamic Structural Equation Modeling

Asparouhov, Hamaker & Muthén (2018) 把 DSEM 定位为四种技术的统一体：*"The goal of the DSEM framework is to parse out and model these four types of correlations and thereby give us a fuller picture of the dynamics found in ILD."* 这几乎逐字对应 LHRM 状态模型的分解需求（person 差异 / 时间邻近 / 变量间耦合 / 演化阶段）。

**RDSEM**：把 within level 拆成 structural part（同 lag 0 的结构关系）+ autoregressive residual part。Asparouhov & Muthén (2020) 证明 DSEM AR(2) 与 RDSEM AR(2) **互相重参数化且等价**（`r1 = ρ1, r2 = ρ2, v = σ, μ = α/(1−r1−r2)`），MSE 相同。→ **不要把"自回归"与"结构耦合"当成两套竞争理论**（**SD19**）。

**三层 DSEM**（Asparouhov & Muthén 2026）：subject → day → observation-in-day。**对 LHRM 的类比**：person → dyad → construct。原文说明可用 multivariate wide format 表示"第一层只有少量观测"的三层结构，且可分别建模 within-day 与 between-day 自相关。

**含环 DSEM**（Muthén, Asparouhov & Keijsers 2025）：*Dynamic Structural Equation Modeling with cycles*，与 LHRM §8 分支 / 回返最直接相关。注意 Mplus 8.4 期 roadmap 仍把 regime-switching 列为 *"We are working on regime-switching extensions"* → 该方向**活跃但未成熟**。

**floor effects DSEM**（Muthén, Asparouhov & Shiffman 2025）：与 `AGENTS.md` *"Do not force every coordinate into `0..1`"* 直接相关 —— LHRM 若硬用 0..1 latent score 建模就会有 floor/ceiling bias。

**连续时间 DSEM**（Asparouhov & Muthén 2024 v5）：处理不等间隔观测，对应 LHRM `tau = (history_id, local_time)`。

**Mplus 实现的三条明确限制**（原文）：(a) `R_l` 与 `Q_l` 在 `l = 0` 时不能为 random；(b) `Λ1;l`、`B1;l` 与 Eq.11 的参数可 random 但不能含 time-specific random effect；(c) **分类变量没有 lagged observed variable** —— 分类变量只能通过 latent `η` 或其他连续 DV/IV 建 time-series 模型。

| Q | 可识别 | 所需数据结构 | 关键假设 | 失败模式 / 误用 | 不得因果主张 |
|---|---|---|---|---|---|
| Q1 溢出 | within level 结构关系：双方互为 predictor，**含互惠** | 双方 × 多时点（Mplus DSEM 为 two-level `CLUSTER=ID`；`TYPE=CROSSCLASSIFIED; CLUSTER=ID TIME` 加 time-specific effects） | time scale 跨个体可比 | 分类变量不能有 lagged observed variable | 不得把 within-level 结构系数叫因果；lagged predictor 只给 temporal precedence |
| Q2 trait/state | between level 的均值 / 截距 = trait；within level 的 AR / innovation = state | 足够长序列 | 三条强假设：(a) person 内与 person 间均正态；(b) 无趋势或周期；(c) **MAR** | 只放 AR(1) 不放 state 分量会把测量误差吸收进 AR | 不得 |
| Q3 三层 | 三层 DSEM | 每 period 观测数少（<10）以便 multivariate wide format | 同上 | — | 不得 |
| Q4 测量误差 | DSEM 内建 measurement model：latent `η` + loadings | multi-indicator | loadings 跨期恒定 | 单指标 DSEM 无法区分 measurement error 与 state | 不得 |
| Q5 转移形状 | AR / MA / VAR / cross-lag / 随机系数 / 连续时间 / 含环 | 长序列 | **平稳性**（除非有 time-varying covariates 或用 ARIMA 差分） | 直接套 AR(1) 到非平稳序列；AR(1) 需 \|β\| < 1，multivariate 需 β = V^{-1}C 的特征值模 < 1 | 不得 |
| Q7 不变性 | latent 因子 + 载荷约束 | multi-indicator DSEM | — | 用 multi-indicator 而不测 invariance | 不得 |
| Q8 缺失 | Bayesian MCMC 把 missing data 与 random effects / model parameters 同等对待，**从 conditional posterior 抽样**；其 conditional distribution 依赖 (a) 邻居观测、(b) 当前迭代的 AR 参数、(c) 残差方差表达的不确定性。*"similar to … a Kalman smoother based on the state-space model, and it guarantees consistent estimation **as long as the missing data are missing at random**"* | 允许 MAR | MAR | **作者自己警告**："周末不测"或 ESM"夜间不测"的结构性缺失 *"may be questionable whether this amounts to missing at random"* | 不得把 MCMC 插补后的轨迹称为"观测到的事实" |

**LHRM 结论**：`X_(t+1) = F(...)` 在统计上就是 **within-level 结构方程 + between-level 协变量回归 + time-series error**。DSEM 是这条方程最完整的现成实现。**但**其结论全部相对于"平稳 + 正态 + MAR + 测量模型设定"；且 Mplus 9.1.1 的 DSEM 是 two/three-level 框架 —— **把一个 dyad 当作一个 cluster 时，`i->j` 与 `j->i` 是同一 cluster 内的两个变量**；这能表达互惠，但**不表达**"这两条边的非独立来自不同的 person 层 trait"。这是 **I4 / I14** 的技术来源。

### M5 — State-space / Kalman / HMM-LMM / latent transition

| Q | 可识别 | 所需数据结构 | 关键假设 | 失败模式 / 误用 | 不得因果主张 |
|---|---|---|---|---|---|
| Q2 trait/state | **该方法的主场**。Kalman 滤波把观测 = 平滑 latent trait + 平滑 latent state（*"Time-series models for observed and latent variables date back to Kalman (1960)"*） | 长序列 | 线性 / SDE；正态扰动 | 用 Kalman 而不建模 measurement function：会把测量误差当状态 | 不得把滤波后的 latent 轨迹当"真状态"（**I2**） |
| Q5 转移形状 | Markov / 一阶或高阶 / time-homogeneous 或非齐次 / covariate-dependent（nonhomogeneous HMM 让 transition 成为 time-varying covariates 的函数） | 离散或连续时点 | 一阶 Markov；**local independence** | local independence 在二人情境极强：同一事件同时改变双方状态时，`i->j` 与 `j->i` 的残差相关。可用 direct effects / cross-time direct effects 放松 | 不得 |
| Q3 person/dyad | multilevel LM（LMM 随机效应 / mixed LMM） | cluster 结构 | — | — | 不得 |
| Q6 解体 hazard | LMM 可作状态转移动力学，但 hazard 是 Q6 的专线 | — | — | 用 LMM 替代 hazard 会丢掉 competing risks | 不得 |
| Q8 缺失 | Kalman smoother / 状态空间原生处理缺失 | 允许 MAR | MAR | 同 M4 | 不得 |
| Q10 派生 | LTA 的 latent state 数 K 本身是**人为设定** | — | 状态数、转移矩阵约束 | 换 K 与约束就换一套"状态" | 不得把 LTA 的 K 状态当"真实关系状态种数" |

**⭐ 与 canonical 的直接冲突点**：`CURRENT_ARCHITECTURE.md` §"Current architecture direction" 第 9 条要求 *"核心关系演化**不**使用 pre-enumerated relationship state machine 作为引擎"*，§"当前非目标" 亦列出"预写关系状态机"。而 LTA / HMM **正是离散状态机**。这不是方法优劣问题，而是**目标不同**：LTA 回答"数据能被压缩成几个离散 regime"，LHRM 要的是"保留连续 / 混合状态表示 + 显式 Unknown"。

**`AI recommendation`**：若使用 LMM/LTA，**只能作为压缩投影与诊断**，必须：① 报 K 与约束的敏感性；② 证明该离散划分不冒充本体；③ 保留连续 / 混合状态的底层表示。

**量化警示**（Vermunt 2004 原文）：2 状态真值 `P(X1=1)=.80`，两向转移概率 `.10`，测量正确率 `.20` 时，若误用 stationary manifest 一阶 Markov 拟合，会得到 state 1 规模 `.68`、转移概率 `.29` 与 `.48`。三类偏差：*"the size of the smaller group is overestimated, the amount of change is overestimated, and there seems to [be] more change in the small than in the large group."* → **观测到的"关系状态突变率"可能纯粹是测量误差。**

### M6 — Survival / event-history / hazard / competing risks

| Q | 可识别 | 所需数据结构 | 关键假设 | 失败模式 / 误用 | 不得因果主张 |
|---|---|---|---|---|---|
| Q6 解体 hazard | 生存函数、risk、基线 hazard（duration dependence）、协变量效应 | 事件时间（右删失）；**两位成员各自的报告** | 比例风险（可用 Schoenfeld 残差检验） | **报告偏差**：*"marital disruptions are seriously underreported by males, making the analysis of male marital histories problematic"*；另有"分离是否随后复合"的偏差 | 不得 |
| **谁提出解体** | 用 **latent class 嵌入 competing-risks event history**：把"husband/wife 对谁提出的报告"当**可错指标**，三状态（妻子提出 / 丈夫提出 / 仍在一起） | 双方独立报告 | local independence | 用可见报告直接当事实 | 不得把"报告的发起方"当"实际发起方" |
| Q8 缺失/删失 | competing risks 处理"外部原因死亡" | — | 独立删失 | *"It is rarely (if ever) sensible to treat 'impossible' outcomes (e.g., quality of life after death) as missing data"* | 不得 |
| Q9 Env/Event | **同时 hazard**：结婚 / 离婚 × 劳动参与 / 收入；利用完整 event history 的 *"temporal ordering of events … for identification"* | 完整 event history | 联合异质性（跨过程未观测异质性相关） | 忽略 unobserved heterogeneity（frailty）会得出"关系影响劳动、同时劳动影响关系"的双向伪因果 | 不得 |
| Q9 内生性 | **simultaneous hazard processes + 跨决策的未观测异质性相关**处理自选择：*"The endogeneity of one outcome on another is controlled for by allowing the unobserved heterogeneity components to be correlated across the various decisions that are modeled."* | — | 跨过程异质性相关 | 用普通 PH 回归处理自选择的时变处理 | 不得 |

**LHRM 结论**：hazard 是 Q6 的**唯一合适工具**，且它对 LHRM 有额外价值 —— **解体是唯一"关系终止"有客观时间戳的构造**，因此是 LHRM 中"事实状态"最硬的锚点。但上表说明**连这个锚点都有双向报告偏差**，且"谁发起"本身需 latent class 才能处理。

### M7 — ILD / ESM / EMA 设计与分析要求

这不是分析模型，而是"其他方法能否工作"的前置条件。

1. **power 以 dyad 数计**，且 person 内效应的 power 与 person 间效应完全不同量级。
2. **within-person reliability 必须单独报告** —— Neubauer, Voelkle, Voss & Mertens (2020) 专门处理 *"estimating reliability of within-person couplings in a multilevel framework"*。person 内相关显著但 within-person reliability 极低的结果没有实质意义。
3. **compliance**：两次 meta 分析（k = 481 / k = 496）平均合规率 **76.98%**。低合规既降 power 又制造 missing。
4. **measurement reactivity**：实证发现是"回答变快、**person 内方差随时间下降**"；均值变化不一致。
5. **间隔与时间分辨率决定"惯性"的含义**（见 **I12**）。
6. **研究设计缺乏有证据支撑的指南**：*"There are very few guidelines substantiated by evidence on how to properly conduct an ESM study"*；Janssen et al. (2018) 显示多数 ESM 研究者对自己的方法学选择**没有明确理由**。

| Q | 可识别 | 所需数据结构 | 关键假设 | 失败模式 / 误用 | 不得因果主张 |
|---|---|---|---|---|---|
| Q1 | 唯一能让 `partial F_i / partial z_j != 0` 变成可估计路径的设计 | **双人同步采样**（pair-level ESM），间隔足够短 | 同时性；双方都在采样 | 单人采样再回溯问 partner（把 partner 数据降级为回忆） | 不得 |
| Q2 | 高频数据下 trait 在采样窗内几乎不变 → 高 AR 几乎必然是真实惯性而非伪迹：*"the underlying 'trait' hardly changes from moment to moment. If one were to sample IBIs … the last interval will not be wildly different from the next"* | 高频 | — | 采样间隔太长 → cross-lag 拾取 trait 相关产生伪效应 | 不得 |
| Q5 | 连续时间 ctsem 可处理不等间隔 | — | — | 用固定 lag 假设拟合不等间隔数据 | 不得 |
| Q8 | **结构化缺失就在设计里** | — | — | 结构性缺失的 MAR 性质可疑 | 不得把"没被 beep 到的时刻"当"没发生" |

### M8 — 测量模型（IRT / bifactor / CFA / 不变性 / argument-based validity）

**这是 LHRM 全部动态结论的前提，也是最容易被跳过的层。**

**bifactor 的方法学论证**（Reise & Tucker-Drob 2010）：bifactor = 每 item 载荷在 general factor 上 + 至多在一个正交 group factor 上；group factor 相当于 *"nuisance dimensions"*。三条关键论证：① *"the determination of dimensionality is a related but distinct question from either determining the extent to which scores reflect a single individual difference variable or determining the effect of multidimensionality on IRT item parameter estimates"*；② *"in many contexts, multidimensional data can yield interpretable scale scores and be appropriately fitted to unidimensional IRT models"*；③ correlated-traits / second-order 与 bifactor 是两种哲学 —— 前者问"更基本元素间有什么共同"，后者问"items 间有什么共同"，*"the target latent variable is what is in common among the items"*。

**不变性之争**：

| 阵营 | 主张 |
|---|---|
| A. 不变性是必要前提 | *"strong invariance is the minimal level required for meaningful interpretation of group mean contrasts"*（Kline）；*"only scalar invariance allows validly comparing scale mean scores across cultures"*（Boer et al.）；Putnick & Bornstein：*"measurement invariance is fast becoming de rigueur"* |
| B. 有效性本位 | *"there is a **danger of comparing apples and oranges** when using the partial invariance approach in applications with **more than two groups**"*（被释放的 item 不参与 linking，不同组可比的是不同 item 集）；*"we would argue that there is **unavoidable ambiguity** in handling situations of measurement non-invariance"*；*"We find such statements as recommendations for practitioners **highly questionable because they carry an impetus of general validity that could never be seriously justified**"*；主张 *"intentionally misspecified multiple-group factor analysis with invariant item parameters and **unweighted least squares**"* 同样可辩护 |
| C. Alignment / approximate invariance | Bayesian approximate invariance（Muthén & Asparouhov）；alignment optimization（Asparouhov & Muthén alignment 系列；Luong & Flake 2023） |

**Argument-based validity**（Kane 2013 八点）：*"it is the proposed **score interpretations and uses** that are validated and not the test or the test scores"*；*"**more-ambitious claims require more support than less-ambitious claims**"*；*"more-ambitious claims (e.g., construct interpretations) tend to be more useful than less-ambitious claims, but they are also harder to validate"*；*"the rejection of a score use does not necessarily invalidate a prior, underlying score interpretation"*；*"the validation of the score interpretation on which a score use is based does not validate the score use"*。

→ `Z[k,i,j,t]` 不是一个"分数"，而是"由 instrument 支撑的 **score interpretation**"。Kane 的链条（observed performance → score → construct interpretation → decision）要求 LHRM **逐环显式声明 warrant**。`AGENTS.md` "Do not label an unvalidated formula, parameter, weight, probability, causal relation, distance metric, normalization rule, or state transition as scientifically established" 正是这条链的最后一环。

**结构效度报告不足的量化后果**（Hussey & Hughes 2018）：N = 144,496 sessions、15 问卷 26 分量表。按只查内部一致性的 modal practice，**89% 尺度"看似有效"**；按全面评估（内部一致性 + 即时/延迟 test-retest + 因子结构 + 对年龄与性别的 invariance），**只剩 4%**。作者提出 **"validity hacking (v-hacking)"**，并发现 *"the less commonly a test is reported in the literature, the more likely it was to be failed"*。

| Q | 可识别 | 所需数据结构 | 关键假设 | 失败模式 / 误用 | 不得因果主张 |
|---|---|---|---|---|---|
| Q4 测量误差占比 | multi-indicator latent model 把 person 间方差分解为 trait component / group(nuisance) component / residual | 每构念 ≥3 指标 × 多波 | conditional independence（bifactor 下放宽到 S+1 个 latent 条件） | **单指标尺度上，person 间差异与 occasion 特异差异不可分** | 不得 |
| Q7 不变性 | 层级序列 configural → weak(metric) → strong(scalar) → residual；每级报 Δχ²，**参数落在参数空间边界时需 χ̄² / chi-bar-square 检验** | 多波 multi-indicator | — | 用 χ² 检验边界约束；把部分不变性当完全解决方案（**SD11**）；未测不变性就做 latent RI-CLPM | 不得把"invariant 失败"说成"关系变了"（**SD3**） |
| Q2 trait/state | general vs group(nuisance) factor 的分解 | 同上 | — | 误把 nuisance group factor 当真实 sub-construct | 不得 |

### M9 — 缺失数据：FIML / MI / MNAR / selection models

**Carpenter & Kenward 的三条框架性结论**：
1. *"when data are missing any attempt to draw conclusions from a statistical analysis rests on **untestable assumptions** concerning the relationship between the unobserved data and the reasons for them being missing"*；
2. *"primary analyses should rest on … the so called **missing at random** assumption. Broadly, this is the most general assumption that allows valid analyses to be made independently of the missing value mechanism"*；
3. 敏感性分析两条路线 —— **(Route 1) 修改缺失数据本身的行为**（pattern-mixture，改 `f(Y_m | Y_o, R)`）vs **(Route 2) 修改显式 MNAR 缺失机制**（selection model，改 `P(R | Y_o, Y_m)`）。

补充两条操作警告：*"Analysis of completers only may well be inefficient, and will be **biased in general under MAR and MNAR**."*；*"Likelihood based analyses (including Bayesian), and some special weighted analyses, are valid under MAR. **Other methods, like unweighted GEE are not.**"* MAR 的表达：*"the future statistical behaviour of a subject, conditional on the history, is the same whether the subject drops out or not in the future."* Molenberghs et al. (1999) 则强调 selection 与 pattern-mixture 两族的区别，并指出 *"The central roles of **identifiability and sensitivity** are emphasized throughout."*

| Q | 可识别 | 所需数据结构 | 关键假设 | 失败模式 / 误用 | 不得因果主张 |
|---|---|---|---|---|---|
| Q8 缺失/Unknown | FIML：在 MAR 下对观测数据似然做积分，无需插补 | 允许 MAR | MAR | **未加权 GEE 在 MAR 下无效**；complete-case 在 MAR/MNAR 下一般有偏 | 不得把 FIML 结果称为对 MNAR 稳健 |
| Q8 选择模型 | selection model（显式建模 R）或 pattern-mixture（显式建模偏离 MAR 的选择） | 需协变量预测 dropout | MNAR 的具体参数化是**假设，不是估计** | 直接把 MNAR 敏感性参数当估计量；报 delta 参数却不给 prior 敏感性 | 不得 |
| Q1–Q5 连带 | DSEM 的三条强假设之一就是 MAR | — | MAR | 在 ESM / 日记里结构性缺失的 MAR 性质可疑 | 不得 |
| Q6 删失 | competing risks / 独立删失 | — | — | 把"死亡后不可测"当 missing | 不得 |
| Q4 | 高缺失下 measurement model 与 missingness model 混淆 | — | MAR | 缺失 item 被当 0 分 | 不得 |

**LHRM 结论**：`AGENTS.md` *"never silently coerce missing information into neutral/perfect-match values"* 在方法上有一个精确对应物 —— **MNAR sensitivity analysis 是可识别性边界的一部分，不是附录**。任何 LHRM 的 `Z[k,i,j,t]` 后验，若其对 MNAR 偏离的敏感度未报，就等于违反了项目自己的规则。

### M10 — 因果推断边界

#### 10.1 时间变化混杂让"控制既往分数"失效

`Causal Inference: What If` Part III 的章节目录直接对应 LHRM 的动力学：Ch.19 *Time-varying treatments*；19.6 *Time-varying confounding and time-varying confounders*；Ch.20 *Treatment-confounder feedback*（小节标题即 *"Why traditional methods cannot be used"*）；Ch.21 *G-methods*；Ch.22 *Target trial emulation*；Ch.23 *Causal mediation*。

LHRM 的 `F(X_t, Action_t, Event_t, Belief_t, Constraint_t, Environment_t)` **字面上就是 time-varying treatments**：`Action_t` 影响 `X_{t+1}`，同时 `X_t` / `Environment_t` 又影响 `Action_{t+1}` → treatment-confounder feedback。

两条精确定论（原文）：
> *"**The value of the g-formula depends on what, if anything, has been included in Λ.** … if we do not collect data on Λ_1 because we believe, **incorrectly**, that our study is represented by a causal diagram … **after removing the arrow from Λ_1 to A_1** … the g-formula that **fails to include Λ_1 no longer has a causal interpretation**."*
> *"**even when the g-formula does have a causal interpretation, each of its components may lack a causal interpretation.**"*

Lüdtke & Robitzsch 与 Mulder et al. 把这套搬进 CLPM 文献并给出 SEM 路线 vs marginal structural model 路线的比较。RI-CLPM FAQ 建议协变量多时 *"consider alternative modeling approaches … such as those based on **propensity scores**"*。

#### 10.2 二人 dyad 在结构上违反 no-interference

*Toward causal inference with interference* 第一段：
> *"A fundamental assumption usually made in the potential outcomes approach to causal inference is that of **no interference** between individuals (or units); that is, the potential outcomes of one individual are assumed to be unaffected by the treatment assignment of other individuals. **However, in many settings, this assumption obviously does not hold.**"*

其记号 `Y_ij(z_i)` 明确允许 *"the potential outcome for individual j **may depend on another individual's treatment assignment** in group i"* —— **这正是 LHRM 的 `i->j` / `j->i`**。该文区分 partial interference、stratified interference、direct / indirect / total / overall causal effects（*"the total causal effect is shown to equal the sum of direct and indirect causal effects"*）、exposure mapping、neighborhood interference；后续工作进一步给出 misspecified exposure mapping 的偏差分析与 degree of interference 框架。BK Handbook Ch.16 给出 LHRM 直接可用的警告：*"In practice, however, the interference structure is typically **assumed to be given, unique, and correctly specified**."*，且网络 *"edges can be censored, the structure can change over time, and contamination between clusters may exist"*。

| Q | 可识别 | 所需数据结构 | 关键假设 | 失败模式 / 误用 | 不得因果主张 |
|---|---|---|---|---|---|
| Q1 | 在 **no-interference 不可满足** 的 dyad 中，direct / spillover / total / overall effect **必须分别定义并分别假设** | 明确的 exposure map（如"自己的状态"与"邻居的处理"是两个不同 exposure） | partial / stratified / neighborhood interference + 交换性 | 用"一个人的潜在结果"记号描述二人关系 | **不得**使用任何隐含 no-interference 的因果表述 |
| Q5 / Q9 | 关系里的"行为 → 状态 → 行为"是**动态 treatment**；需 g-methods 而非简单回归 | 需曝光出 treatment strategy 的变异 | sequential exchangeability + positivity | 用"控制了 t−1 分数"当作充分控制 | 不得 |
| Q6 | 解体 hazard 的因果版需 **target trial emulation** | 明确的 index time、eligibility、strategy、outcome、follow-up、censor plan | exchangeability / positivity | 把 PH 的 hazard ratio 当"如果……会怎样" | 不得 |
| Q3 | dyad-level 方差在 interference 框架下是"暴露 mapping"的一部分，不是独立来源 | — | — | 把 pair-level 分解当"结构性权力 / 主动性证据" | 不得 |

**LHRM 结论（`AI recommendation`）**：`CONSTRUCT_SCOPE_DIRECTIONALITY.md` §4 说"低冗余不等于动态独立"、允许 `partial F_i / partial z_j != 0`，在统计上意味着 **LHRM 的状态转移天然是带干扰（interference-aware）的动力学系统**。这不否定架构，但要求：任何"X 导致 Y"的写法必须显式写出 exposure map。

### M11 — 元科学：multiverse / specification curve / power / 不确定性传播

Robitzsch (2022) 的 PISA 2018 specification curve 分析给出对 LHRM 直接可用的量化警示：
> *"In our multiverse analysis, it turned out that **model uncertainty had almost the same impact on variability in the country means as sampling errors** due to the sampling of students. **Model uncertainty had an even larger impact than standard errors for country standard deviations.**"*
> *"each of the five specification factors in the multiverse analysis had **at least a moderate effect** on either country means or standard deviations or both."*
> *"It is emphasized that **model fit should not play a role in selecting a scaling strategy** for LSA applications."*

Orth et al. 也直接引用 false-positive psychology 说 CLPM 文献存在 *"selective reporting (i.e., choosing the best model after seeing the results from several competing models)"*。

**LHRM 结论**：由于 LHRM 明确"候选参数集尚未冻结"（`CURRENT_ARCHITECTURE.md` §"当前工程顺序" 第 1 步即 Parameter Convergence），**multiverse / specification curve 正是把"未冻结"变成可报告结果的标准工具**，而不是"还没做完"。模型不确定性 ≈ 抽样误差这一发现，正是对"先选一套模型再报告"的直接反驳。

---

## 5. 识别不可能清单（**一等交付物**）

> 这一节不是脚注。它是 LHRM 应在 canonical 层面承认的硬边界。**换方法不能越过这一节。**

| ID | 结构上不可能回答的问题 | 为什么换方法也解决不了 | 对 LHRM 的具体后果 |
|---|---|---|---|
| **I1** | 单一段 case（Case Bank 材料）能否拟合关系状态转移律 `F`？ | `F` 的函数形式不可由数据学习（结构因果模型不可由数据识别，只能由理论 + 设计限制）。单一轨迹对 `F` 的约束是**无穷薄的曲线**。 | Case Bank 继续只做 representation completeness / closure / regression 测试（与 `CURRENT_ARCHITECTURE.md` §10 一致）。**不得**从 case 拟合转移律。 |
| **I2** | 对方真实状态 `Z[k,j,i,t]` 的真值 | 观测是 `report_function(state, context)`。数据只给 `P(state \| report)`；即使完美模型，posterior 也不会坍缩到点。 | 任何 `Z` 都必须**始终**表示为 estimate + uncertainty + evidence（§9.6）。**不得**把 posterior mean 写成"真实状态"。 |
| **I3** | partner 报告的准确性 | SRM 的 accuracy 成分需要多个 target 与多个 perceiver（round-robin）。两人 dyad 不满足。 | **不得**把 partner report 的差异解释为"一方更了解对方"。 |
| **I4** | ⭐ 两人 dyad 里分离 `source_i` / `target_j` / `directed_dyad_(i->j)` | 自由度：2 条有向边 = 2 个自由度；SRM 三成分 + 多个 target 需要更多。 | `CONSTRUCT_SCOPE_DIRECTIONALITY.md` §1 的分解式在**纯 dyad 设计下不可识别**。三者可作**架构占位符**存在，但**不得**写成"估计值"。要估计它们必须重新采集 round-robin / 交叉设计数据。 |
| **I5** | 关系的"因果优先级"（谁是原因） | 需要 exchangeability + 无 time-varying 混杂 + 顺序可交换性。二人关系中"共同环境 + 共同第三方 + 归因反馈 + 双向行为反馈"同时破坏它们；且 no-interference 本身不成立。 | **不得**给"A 导致了 B 的关系破裂"这类单向归因。 |
| **I6** | 互惠 / 不对称作为 primitive 的额外信息 | 若 `Z[k,i,j]` 与 `Z[k,j,i]` 可稳定解耦，则 `MutualX` / `Asymmetry` 是**确定性派生量**，零自由度。 | 这**支持** §2 的"优先派生"决定。同时：**不得**反过来用"互惠低"去推断哪个方向分量错（推导不可逆）。 |
| **I7** | "这对关系现在处于哪个离散状态"作为**主要估计目标** | LTA/LMM 的状态数 K 与转移矩阵约束是人为设定；换 K 与约束就换一套"状态"。 | 与"不用 pre-enumerated state machine 作引擎"一致：LTA 只能作**压缩投影 + 诊断**，且须报 K / 约束敏感性。 |
| **I8** | ⭐ "变化了多少"与"变了什么"（测量工具变了） | 观测协方差模式在两种生成机制（DIF vs 真变）下**相同**。除非有 invariant 锚定 item 或外部锚。 | 任何动态结论前必须先做 invariance 层级序列。否则结论**未定义**。 |
| **I9** | `Constraint`（如"订婚前不发生性行为"）的 effect | Constraint 本身是"未发生的事件"，无反事实对照就无 estimand。 | `AGENTS.md` 已把 constraint 与 state 分开。**不得**把 constraint 的存在写成"性欲为零"（§6 明举此例）。统计上是 **structural zero / undefined**，不是 `0`。 |
| **I10** | "为什么这段关系如此"的机制归因 | 不可约化的等价模型：不同 DAG / `F` 形式可给相同拟合；g-formula 的各组成部分**可能都没有**因果解释。 | **不得**把最好拟合的 `F` 当机制。`F` 的形式是理论承诺，不是估计结果。 |
| **I11** | "这是关系的性质 / 这个人的性质 / 这段历史的性质 / 这个文化标签的性质" | 需要构念 × 角色 × 情境 × 文化的**正交交叉设计**。LHRM 当前数据源不满足。 | `CONSTRUCT_SCOPE_DIRECTIONALITY.md` §7 的 cross-context test 目前**不可执行**。应标 `BLOCKED_BY_DATA`。 |
| **I12** | ⭐ 状态转移的**速率** | 同一 `psi(t)` 序列在不同 lag / 时间分辨率下给出不同 AR 系数与不同"惯性"结论；若 `tau` 是 history branch 或回忆时间而非真实连续时间，"lag"**不是物理时差**。 | 所有速率陈述必须**相对于采样协议**表述。`X_(t+1) = F(...)` 中的 `+1` 不是一个自然量。 |
| **I13** | "完整轨迹"的陈述（当存在任何缺失时） | 任何"完整轨迹"都是 MAR 下的模型外推；FIML 也不例外。 | 缺失不是中性。必须报 MNAR 敏感性。 |
| **I14** | ⭐ dyad 内两条有向边的**非独立来源分解**（person 层 trait vs dyad 层特殊） | 同一 dyad 内至少有 person 层与 dyad 层两个来源；Mplus DSEM 是 two/three-level，dyad 当 cluster 时两条边在同一 level，**无法**同时分离两者。要分离需 SRM 式多 target 设计（I4），或至少 3 波 + STARTS + 显式排除遗漏型 TVC。 | **这是 LHRM 最难的一个识别缺口**，直接限制 §1 分解式中"多少是 `source_i` / `target_j` / `directed_dyad`"的可回答性。 |
| **I15** | 从单个案例估计现实概率 | `AGENTS.md` 与 `CURRENT_ARCHITECTURE.md` §10/§11 已明示。 | 方法学上：n = 1 的 hazard / transition 无 estimand。 |
| **I16** | 观测数据能否给出"关系应当如何"的规范性判断 | 描述性 / 预测性 / 因果性三类问题的 estimand 互不相同（*"we should distinguish between descriptive, predictive, and causal research questions"*）。规范性判断不在其中任何一类。 | 任何 LHRM 输出的"建议"必须标为 downstream readout，不得反向进入 ontology。 |
| **I17** | "trait 还是 state"这个二分本身 | TSE 会 improper solution；LST-AR 只适用于自相关随时间增加的构念；TSO 仍有 occasion factor stability 太大 / 太小的问题。Cole et al. 明确这是 *"empirical or conceptual problems"*，不是已解决的对立。 | **不得**把 Q2 当成有唯一答案的分类问题。应作为**模型依赖的分解比例**报告，并报模型敏感性。 |

---

## 6. 统计自我欺骗模式

| ID | 模式 | 机理 | LHRM 里的具体表现 |
|---|---|---|---|
| **SD1** | 把 person 间相关当 person 内动态 | CLPM 的 AR 路径吸收 trait 稳定，导致存在性 / 优先级 / 符号三项都可能错 | 用两人两波的相关报告"A 的话语预示 B 的状态" |
| **SD2** | 把一次性 cross-sectional 差异当 transition | 两波差异 ≠ 变化；可能只是不同 instrument / 不同 occasion | 从两份材料读出"关系在 T1→T2 变冷了" |
| **SD3** | 把 measurement invariance 失败当真实变化（**或反向**） | 两者协方差模式相同（I8） | 把"量表在离婚后失效"读成"离婚导致自我报告改变" |
| **SD4** | 把 actor / partner path 叫 influence | 官方脚注即禁止 | "partner effect 表明 A 影响了 B" |
| **SD5** | 把 within-person 效应当总体相关 | RI-CLPM 的 estimand 转移：*"around the person mean"*，*"typically less relevant"* | 用 RI-CLPM 论证"高 trust 的人更少焦虑"——那其实是 between-person 命题 |
| **SD6** | ⭐ 把 random intercept 当"真 trait" | illusory between-person component：可能**只**来自省略的 time-varying covariate | "`RIx` 的方差 0.42 → trust 是稳定 trait" |
| **SD7** | 把 effect size / R² / fit 当因果证据 | 2 波 CLPM 饱和 → 无 fit 信息；且 45% 文献这样做 | "模型拟合良好 → 我们的关系状态模型是对的" |
| **SD8** | 把 dyad 内 N 加大当精度提高 | 分析单位是 **dyad** | 把 200 人 × 2 方向的 400 个数当 n = 400 |
| **SD9** | 从 p 值挑最终随机结构 | 明确禁止：*"do not use p values to decide for the final model"* | 用"收敛良好"或"p 显著"决定保留哪些 pair-level 方差 |
| **SD10** | researcher degrees of freedom / **v-hacking** | 结构效度报告不全 → 89% vs 4% 的差距 | 换 indicator、换 invariance 处理、换 centering、换约束直到 cross-lag 显著 |
| **SD11** | 把 partial invariance 当解决方案 | n > 2 组时 *"comparing apples and oranges"*（被释放的 item 不参与 linking） | 三个文化情境各用不同 item 集做均值比较 |
| **SD12** | 把"不显著"当"不存在" | power 随效应类型差 1–2 个量级；部分理论问题是 between-person 而 RI-CLPM 原理上无法表达 | partner effect 常被指为 power 不足 |
| **SD13** | 把 hazard ratio 当"确定解体" | competing risks + 双向报告偏差 + latent initiation | "HR = 2.1 → 这段关系会解体" |
| **SD14** | ⭐ 把 floor/ceiling 当小事 | 硬 0..1 latent score 会产生 floor/ceiling bias | 把 LHRM 的 0..1 投影直接当 latent variable 建模 |
| **SD15** | 把不收敛 / 非 admissible 解当估计 | 不收敛常因随机结构过参数化、协方差近零（singularity）、样本量小、迭代上限 | 强行"修好"后报告参数 |
| **SD16** | 把 Granger / 时序优先当因果 | lagged predictor 只给 temporal precedence | "A 在 t 的状态在 t+1 预测 B → A 影响 B" |
| **SD17** | ⭐ 用 fit 选模型 | RI-CLPM 嵌套 CLPM 多 3 df → *"with increasing sample size, the RI-CLPM necessarily fits significantly better"* | "RI-CLPM 拟合更好 → 用 RI-CLPM" |
| **SD18** | ⭐ 把 model specification 选择当无所谓 | *"model uncertainty had almost the same impact as sampling errors"* | LHRM 参数集未冻结时只报一套模型的结果 |
| **SD19** | 把 AR 与 residual-AR 当两套理论 | 二者已被证明**互相重参数化且等价** | "我们用 DSEM 而不是 RDSEM，所以我们测的是不同东西" |
| **SD20** | 把 LTA 的 K 状态当客观类别数 | K 与转移矩阵约束是人为设定 | "这段关系属于 4 类中的第 3 类" |

---

## 7. 活跃争议（呈现争议，不给伪共识）

| 议题 | 争议双方 | 现状 | LHRM 立场 |
|---|---|---|---|
| CLPM vs RI-CLPM vs STARTS vs ARTS | Hamaker et al. (2015) / Lucas (2023) / Hamaker (2026) **vs** Lüdtke & Robitzsch (2022) / Orth et al. (2021) | **未解决** | **不定论**。并行报告 + 明确 estimand 差异 + 不用 fit 选模型 |
| random intercept 是否为真 trait | 常规解释 **vs** Robitzsch & Lüdtke (2025) | CC-BY 同行评审、充要条件明确、**未被广泛反驳** | 必须先排除省略型 TVC 条件 |
| 测量不变性是必要前提吗 | Putnick & Bornstein (2016) / Kline / Boer et al. **vs** Robitzsch (2023) / Muthén & Asparouhov | **活跃**；alignment 提供第三条路 | **不给伪共识**。报层级序列 + 处理方式 + 对结论的影响 |
| trait vs state 的二分 | Cole et al. 的 TSE / LST-AR / TSO **vs** 认知测量传统 | 已知经验 / 概念问题，未解决 | 报**模型依赖的分解比例** + 敏感性 |
| LTA/LMM 的 K 与约束 | 方法学上是人为设定 **vs** 实务上广泛使用 | 已知问题 | 只作投影 + 报敏感性 |
| CLPM with binary/ordinal | Muthén et al. (2024) 刚出 | 新 | 关注；与 LHRM 混合状态空间直接相关 |
| DSEM 的"环"与"边界" | Muthén et al. (2025) 两篇 | 新；regime-switching 仍是 roadmap 项 | 与 §8 分支 / 回返相关，但**尚无实证基线** |
| AR vs RDSEM | Asparouhov & Muthén (2020) 证明等价 | **已解决** | 不得当作两个竞争理论（SD19） |
| DAG / `F` 形式是否可由数据学到 | 不可 | **已解决** | 不得声称"数据揭示了机制"（I10） |
| 2-wave CLPM 能否谈 fit | 不能；且 45% 文献这样做 | **已解决** | 不得（SD7） |
| no-interference 在二人关系是否可能 | 不可能 | **已解决**（这是 LHRM 的定义性约束） | 任何因果写法必须显式给 exposure map（I5） |

---

## 8. 软件 / 生态指针

（核实日期 2026-09-26 / 2026-09-27）

| 用途 | 工具 | 指针 | 核实状态 |
|---|---|---|---|
| **DSEM / RI-CLPM / 混合 LTA / IRT / 不变性 / Survival / 多层 / Bayesian SEM** | **Mplus 9.1.1**（9.1 于 2026-05 发布，9.1.1 为勘误） | `https://www.statmodel.com/`；专题页含 `DSEM – MultiLevel Time Series Analysis`、`RI-CLPM`、`RI-LTA`、`IRT`、`Measurement Invariance and Alignment`、`Survival Analysis`、`Bayesian SEM`、`Multilevel Modeling`、`Mixture Modeling – LCA/LPA/LTA` | 已核实（首页 fetch） |
| DSEM 论文作者版全文 | Asparouhov, Hamaker & Muthén | `https://statmodel.com/download/DSEM.pdf` | 已核实 |
| 多指标 RI-CLPM 语法 | Nguyen, T. | `https://www.statmodel.com/download/RI-CLPM.pdf` | 已核实 |
| RI-CLPM 官方代码补充站（Mplus + lavaan + FAQ） | Mulder & Hamaker | `https://jeroendmulder.github.io/RI-CLPM/`（`/mplus`、`/lavaan`、`/faq.html`） | 已核实（FAQ 全文） |
| CLPM 建模策略 web talk | Muthén & Asparouhov | `https://statmodel.com/download/WebTalk4.pdf` | 已核实 |
| ILM 模型比较 / RDSEM | Asparouhov & Muthén | `https://statmodel.com/download/RDSEM.pdf` | 已核实 |
| **连续时间 SDE / DSEM（R）** | `ctsem` **v3.11.1**（published 2026-07-13；Driver, Voelkle, Oud）；SDE / 差分方程 + ML/EM 或 Stan HMC | `https://CRAN.R-project.org/package=ctsem`；repo `https://github.com/cdriveraus/ctsem` | 已核实（CRAN 页 fetch） |
| **多维 IRT / bifactor / two-tier（Q4, Q7）** | `mirt` **v1.47**（published 2026-08-20；Chalmers）；含 confirmatory bifactor / two-tier、mixture IRT、unfolding models | `https://CRAN.R-project.org/package=mirt` | 已核实（CRAN 页 fetch） |
| SEM / FIML / RI-CLPM（R） | `lavaan` | `https://lavaan.ugent.be/`（**本次 fetch 失败 → `UNKNOWN_AS_OF`**）；教程 PDF 已读 | URL 未核实 |
| MI（Q8） | `mice`、`blimp` | 本次未 fetch | `UNKNOWN_AS_OF` |
| 向量自回归 / 动态因子（R） | `mlVAR`（Epskamp, Deserno & Bringmann, 2017）、`OpenMx`（Boker et al. 2011）、`Stan` | 出现在 DSEM 综述引用串 | `CITED_SECONDARY` |
| APIM 交互工具 | Kenny (2015) | `https://davidakenny.shinyapps.io/APIM_MM/` | `CITED_SECONDARY` |
| APIM 教学 | SSRI, Penn State | `https://quantdev.ssri.psu.edu/sites/qdev/files/APIM_tutorial_2020.html` | 已核实（全文） |
| ILM / ESM 教材与数据 | Bolger & Laurenceau (2013) companion site | `http://www.intensivelongitudinal.com/index.html` | 已核实 |
| ESM 设计手册 | Myin Germeys & Kuppens (eds.) | `https://ppw.kuleuven.be/okp/esmhandbook.php` | 已核实 |
| 纵向不变性 + CLPM 的 lavaan 5 步教程 | Metapsychology（开放获取 PDF） | 全文已读 | 已核实 |
| JARS 量表合集 | — | `https://www.jars.network/` **实测为 Namecheap 停放页** | **`BLOCKED_POINTER` — 不得引用为可用仓库** |
| Simulation-based power | Peugh & Litson, *Monte Carlo Power Analyses Using Mplus and R* (Guilford, 2026) | Mplus 官网书目 | `CITED_SECONDARY` |

---

## 9. 明确的非主张（explicit non-claims）

本文件**不主张**以下任何一项：

1. **不主张**任何 transition law、权重、距离、probability、normalization rule 是"已确立"或"已验证"的。全部为 `model hypothesis`。
2. **不主张** LHRM 的候选参数集（`PARAMETER_CONVERGENCE_V0_1.md`）已可被任何方法估计。本文件只给出"哪个问题需要哪种数据"，不给参数先验结构。
3. **不主张** RI-CLPM（或任何 cross-lagged 模型）优于 CLPM。争议未解决。
4. **不主张** random intercept 一定是真 trait。
5. **不主张** measurement invariance 是 group/time 比较的必要且充分前提。
6. **不主张** "trait 还是 state"有唯一答案。
7. **不主张** 关系解体 hazard 的任何报告偏差已被解决。
8. **不主张** 从 Case Bank 材料可估计任何 population 量或转移律。
9. **不主张** `Construct.source_i` / `Construct.target_j` 在纯 dyad 数据下可估计。
10. **不主张** LTA/LMM 的离散状态个数是关系状态的真实个数。
11. **不主张** 文献数量或 LLM 一致度构成任何验证。本文件的指针只用于定位方法与争议，不用于支持"某方法对 LHRM 适用"。
12. **不主张** 本文件的矩阵是完备的方法清单。它是面向 LHRM 已声明问题的**方法映射**。
13. **不主张** 修改任何 canonical doc。本文件为 `RESEARCH_CANDIDATE`。
14. **不主张** R03 / R04 等 sibling lane 的结论。本 lane 未读 sibling lane 输出。
15. **不主张** dyad 数据已足够回答 Q1–Q3。这取决于剩余未知 U5 / U10。

---

## 10. 剩余未知（remaining unknowns）

| # | 未知 | 影响 | 建议 |
|---|---|---|---|
| U1 | Besser, Perla & Hamaker (2022) step-by-step RI-CLPM 指南的 DOI 未核实 | 引用完整性 | 换检索源，或交 Wave 2 引用核查 lane |
| U2 | Lucas, Weidmann & Yang 的期刊版身份未核实（只查到 PsyArXiv 预印本） | §3.2 嵌套链的来源 | 同上 |
| U3 | Atkins & Frey (2004) *Ready for the Millennium?* 未取得稳定指针 | 本文件未使用该引用 | — |
| U4 | JARS 正确入口未知（`jars.network` 已停放） | 测量工具 catalog（R03） | Architect 决定是否继续找，或改用其他官方量表站 |
| U5 | ⭐ LHRM 实际可获得的**波数分布** | **决定 Q1–Q5 是否可行**。若多数数据只有 1–2 波 → Q1 / Q2 / Q3 基本不可估计（2 波 CLPM 饱和且无法分离 within-person） | 与 R04 对齐后重估；可能需要把 LHRM 动态部分明确标为"需专门采集设计" |
| U6 | 中文 / 东亚语境的 relationship state 测量工具 | Q7 跨文化部分 | 与 R03 对齐 |
| U7 | `Sonnenstag et al.` 综述的确切年份 | 引用 | 标 `UNKNOWN_AS_OF` |
| U8 | dyadic DSEM / dyadic 连续时间 SDE 的现成实现 | **直接决定 I14 能否被绕开** | 需单独核实 `ctsem` 是否有 dyadic / 多 agent 扩展 |
| U9 | ESM 类设计中"dyad 同步采样"的合规率与 reactivity 实证 | M7 的设计可行性 | R04 / R16 |
| U10 | ⭐ 关系研究里 rival-directed / 多 target（round-robin）数据集是否存在 | **直接决定 I4 能否被绕开** | R04 专项确认 |
| U11 | 二人 dyad 的 third-party / network 结构测量方案 | interference 结构假设 | R08 / R10 |
| U12 | *Toward causal inference with interference* 的作者与正式书目（只核实到全文 PMC2600548） | 引用 | 引用时按 PMC ID 指向，或 Wave 2 补全 |

---

## 11. 引用清单

### 方向性二人 / APIM / SRM
- Kenny, D. A. (2018). Reflections on the actor–partner interdependence model. *Personal Relationships, 25*(2), 160–170. `10.1111/pere.12240`
- Kenny, D. A., & Cook, W. (1999). Partner effects in relationship research. *Personal Relationships, 6*(4), 433–448. `10.1111/j.1475-6811.1999.tb00202.x`
- Kenny, D. A. (1994). *Interpersonal Perception: A Social Relations Analysis*. Guilford.；Kenny & La Voie (1984), *AESP, 18*, 141–182.；Malloy & Kenny (1986), *J. Personality, 54*, 199–225, `10.1111/j.1467-6494.1986.tb00393.x`
- Kashy, D. A., & Cook, W. L. (2005). The Actor–Partner Interdependence Model. *Development and Psychopathology*. `10.1080/01650250444000405`
- Campbell, L., & Stanton, R. (2015). Actor–Partner Interdependence Model. *Encyclopedia of Clinical Psychology*. `https://www.sarahcestanton.com/s/2015_Campbell-Stanton_Encycl-of-Clin-Psychol_APIM.pdf`
- *Introduction to APIM tutorial*, SSRI, Penn State. `https://quantdev.ssri.psu.edu/sites/qdev/files/APIM_tutorial_2020.html`

### within / between 分解与 CLPM 家族
- Hamaker, E. L., Kuiper, R. M., & Grasman, R. P. P. P. (2015). A critique of the cross-lagged panel model. *Psychological Methods, 20*(1), 102–116. `10.1037/a0038889`
- Hamaker, E. L. (2026). The within-between dispute in cross-lagged panel research and how to move forward. *Psychological Methods, 31*(1), 56–76. `10.1037/met0000600`
- Lucas, R. E. (2023). Why the cross-lagged panel model is almost never the right choice. *AMPPS, 6*(1). `10.1177/25152459231158378`
- Orth, U., Clark, D. A., Donnellan, M. B., & Robins, R. W. (2021). Testing prospective effects in longitudinal research: Comparing seven competing cross-lagged models. *JPSP, 120*(4), 1013–1034. `10.1037/pspp0000358`
- Lüdtke, O., & Robitzsch, A. (2022). A comparison of different approaches for estimating cross-lagged effects from a causal inference perspective. *SEM, 29*(6), 888–907. `10.1080/10705511.2022.2065278`
- Robitzsch, A., & Lüdtke, O. (2025). A note on the occurrence of the illusory between-person component in the random intercept cross-lagged panel model. *SEM, 32*(1), 36–45. `10.1080/10705511.2024.2379495`（preprint `10.31234/osf.io/dus42`）
- Andersen, H. K. (2022). Equivalent approaches to dealing with unobserved heterogeneity in cross-lagged panel models? *Psychological Methods, 27*(5), 730–751. `10.1037/met0000285`
- Bailey, D. H., Oh, Y., Farkas, G., Morgan, P. L., & Hillemeier, M. M. (2020). Reciprocal effects of reading and mathematics? Beyond the cross-lagged panel model. *Developmental Psychology, 56*(5), 912–921. `10.1037/dev0000902`
- Lucas, R. E., Weidmann, R., & Yang, H. Typical Patterns of Stability in Longitudinal Data: Implications for Model Choice. *PsyArXiv*. `10.31234/osf.io/rs7eu_v1`（期刊版 `UNKNOWN_AS_OF`）
- Usami, S. (2021). On the differences between general CLPM and RI-CLPM. *SEM, 28*(3), 331–344. `10.1080/10705511.2020.1821690`
- Mulder, J. D., & Hamaker, E. L. (2021). Three extensions of the RI-CLPM. *SEM, 28*(4), 638–648. `10.1080/10705511.2020.1784738`
- Mulder, J. D., & Hamaker, E. L. The RI-CLPM & Extensions — FAQ. `https://jeroendmulder.github.io/RI-CLPM/faq.html`
- Hamaker, E. L., & Muthén, B. (2020). The fixed versus random effects debate and how it relates to centering in multilevel modeling. *Psychological Methods, 25*(3), 365–379. `10.1037/met0000239`
- Schuurman, N. K., Ferrer, E., de Boer-Sonnenschein, M., & Hamaker, E. L. (2016). How to compare cross-lagged associations in a multilevel autoregressive model. *Psychological Methods, 21*(2), 206–221. `10.1037/met0000062`
- del Rosario, K. S., & West, T. V. (2025). A practical guide to specifying random effects in longitudinal dyadic multilevel modeling. *PSPI*. `10.1177/25152459251351286`
- Allison, P. D. (2021). On the practical interpretability of cross-lagged panel models. *Child Development*. `10.1111/cdev.12660`
- Neubauer, A. B., Voelkle, M. C., Voss, A., & Mertens, U. K. (2020). Estimating reliability of within-person couplings in a multilevel framework. *J. Personality Assessment, 102*(1), 10–21. `10.1080/00223891.2018.1521418`
- Muthén, B., Asparouhov, T., & Witkiewitz, K. (2024). Cross-lagged panel modeling with binary and ordinal outcomes. *Psychological Methods*. `10.1037/met0000701`（`CITED_SECONDARY`）
- Curran, P. J., Howard, A. L., Bainter, A. H., Lane, T. G., & McGinley, T. A. (2014). Latent curve model with structured residuals. *JCCP*.（`CITED_SECONDARY`，DOI `UNKNOWN_AS_OF`）
- Oud, J. H. (2002). Continuous time modeling of the cross-lagged panel design. *Kwantitatieve Methoden, 69*, 1–26.（`CITED_SECONDARY`）
- Schimmack, U. (2020). Why most cross-lagged models are false. `https://replicationindex.com/2020/08/22/cross-lagged/`（非同行评审；`CITED_SECONDARY`）
- Besser, J. G., Perla, G. M., & Hamaker, E. L. (2022). How to construct a multilevel cross-lagged panel model. *SEM*.（`AGENT_RECALL`，**DOI 未核实**）

### DSEM / state-space / regime switching
- Asparouhov, T., Hamaker, E. L., & Muthén, B. (2018). Dynamic structural equation models. *SEM, 25*(3), 359–388. `10.1080/10705511.2017.1406803`
- Asparouhov, T., Hamaker, E. L., & Muthén, B. (2017). Dynamic latent class analysis. *SEM, 24*(2), 257–269. `10.1080/10705511.2016.1253479`
- Asparouhov, T., & Muthén, B. (2026). Three-level dynamic structural equation modeling. *SEM, 33*(2), 281–309. `10.1080/10705511.2025.2608122`
- Asparouhov, T., & Muthén, B. (2020). Comparison of models for the analysis of intensive longitudinal data. *SEM, 27*(2), 275–297. `10.1080/10705511.2019.1626733`
- Asparouhov, T., & Muthén, B. (2024). Continuous time dynamic structural equation models. *Mplus Web Note*, Version 5, 2024-10-18.（`CITED_SECONDARY`）
- Muthén, B., Asparouhov, T., & Keijsers, L. (2025). Dynamic structural equation modeling with cycles. *SEM, 32*(2), 264–286. `10.1080/10705511.2024.2406510`（`CITED_SECONDARY`）
- Muthén, B., Asparouhov, T., & Shiffman, S. (2025). Dynamic structural equation modeling with floor effects. *Psychological Methods*. `10.1037/met0000720`（`CITED_SECONDARY`）
- Hamaker, E. L., Asparouhov, T., Brose, A., Schmiedek, F., & Muthén, B. (2018). At the frontiers of modeling intensive longitudinal data. *MBR, 53*(6), 820–841. `10.1080/00273171.2018.1446819`
- McNeish, D., & Hamaker, E. L. (2020). A primer on two-level dynamic structural equation models for intensive longitudinal data in Mplus. *Psychological Methods, 25*(5), 610–635. `10.1037/met0000250`
- Cole, D. A., Martin, N. C., Steiger, J. H., & King, V. (2005). Empirical and conceptual problems with longitudinal trait-state models. *Psychological Methods, 10*(1), 3–20. `10.1037/1082-989X.10.1.3`
- Kenny, D. A., & Zautra, A. (1995). *JCCP, 63*(1), 52–59.；Kenny & Zautra (2001). APA eBook, 243–263.（`CITED_SECONDARY`）
- Vermunt, J. K. (2004). Latent Markov model. `https://www.jeroenvermunt.nl/ermss2004e.pdf`
- Bartolucci, F., Pandolfi, R., & Vermunt, J. K. Latent Markov models: a review. `https://ar5iv.labs.arxiv.org/html/1003.2804`（DOI `UNKNOWN_AS_OF`）
- Janc, M. (1999). A hidden Markov model of customer relationship dynamics. Columbia University. `http://www.columbia.edu/~on2110/Papers/HMM_of_Customer_Relationship_Dynamics.pdf`
- Hoffmann, L., Lehrke, M., & Todt, E. (1985). *J. Educational Statistics*. `10.3102/10769986024002179`（DOI `UNKNOWN_AS_OF`）
- Nguyen, T. How to run a multiple indicator RI-CLPM with Mplus. `https://www.statmodel.com/download/RI-CLPM.pdf`
- Muthén, B., & Asparouhov, T. Cross-Lagged Panel Modeling of Panel Data (Web Talk 4). `https://statmodel.com/download/WebTalk4.pdf`

### ILD / ESM
- Bolger, N., & Laurenceau, J.-P. (2013). *Intensive Longitudinal Methods*. Guilford. `http://www.intensivelongitudinal.com/index.html`
- Myin Germeys, I., & Kuppens, P. (eds.). *The Open Handbook of Experience Sampling Methodology*. `https://ppw.kuleuven.be/okp/esmhandbook.php`
- Sonnentag, S., Neumer, A., Partsch, F., & Völker, J. Intensive longitudinal methods in Work and Organizational Psychology. *Z. Organ Psychol.* `10.1026/0932-4089/a000478`（年份 `UNKNOWN_AS_OF`）

### 测量
- Reise, S. P., & Tucker-Drob, E. M. (2010). Bifactor models and rotations. *Psychological Methods*. PMC2981404
- Gibbons, R. D., Choi, H., & Hedeker, D. 等. Generalized full-information item bifactor analysis. PMC3150629
- Robitzsch, D. (2023). Why full, partial, or approximate measurement invariance needs to take a validity-based perspective. *SEM*. `10.1080/10705511.2023.2191292`
- Putnick, D. L., & Bornstein, M. H. (2016). Measurement invariance conventions and reporting. *Developmental Review, 41*, 71–90. `10.1016/j.dr.2016.06.004`（`CITED_SECONDARY`）
- Kane, M. T. (2013). Validating the interpretations and uses of test scores. *JEM, 50*(1), 1–73. `10.1111/jedm.12000`
- Flake, J. K., Pek, J. X., & Hehman, E. (2017). Construct validation in social and personality research. *SPPS, 8*(4), 370–378. `10.1177/1948550617693063`（`CITED_SECONDARY`）
- Hussey, I., & Hughes, S. (2018). Hidden invalidity among fifteen commonly used measures in social and personality psychology. *AMPPS*.（DOI `UNKNOWN_AS_OF`）
- Luong, R., & Flake, J. K. (2023). Measurement invariance testing using CFA and alignment optimization. *AMPPS*.（DOI `UNKNOWN_AS_OF`）
- Fried, E. I., et al. (2016). Measuring depression over time… or not? *Psychological Assessment, 28*, 1354–1367. `10.1037/pas0000275`（`CITED_SECONDARY`）
- AERA/APA/NCME (2014). *Standards for Educational and Psychological Testing*.

### 缺失数据
- Carpenter, J. R., & Kenward, M. G. (2007/2011). *Missing data in clinical trials: a practical guide*. LSHTM. `https://researchonline.lshtm.ac.uk/id/eprint/4018500/1/rm04_jh17_mk.pdf`
- Kenward, M. G. (2012). *Introduction to missing data: Part 2*. LSHTM. `https://web-archive.lshtm.ac.uk/csm.lshtm.ac.uk/wp-content/uploads/sites/6/2016/04/Mike-Kenward-22-11-2012.pdf`
- Carpenter, J. R., Kenward, M. G., & White, I. R. (2007). Sensitivity analysis after multiple imputation under missing at random: a weighting approach. *Statistics in Medicine*.（DOI `UNKNOWN_AS_OF`）
- Molenberghs, G., et al. (1999). Parametric models for incomplete continuous and categorical longitudinal data. *Statistical Methods in Medical Research*. `10.1177/096228029900800105`

### Survival / event-history
- Felmlee, D., Sprecher, S., & Bassin, E. (1990). The dissolution of intimate relationships: a hazard model. *Social Forces, 68*(4).（DOI `UNKNOWN_AS_OF`）
- Lillard, L. A., Brien, M., & Waite, L. (1993). Pre-marital cohabitation and subsequent marital dissolution: is it self-selection? *RAND DRU-489*. `https://www.rand.org/pubs/drafts/DRU489.html`
- Lillard, L. A., & Panis, C. W. (2003). PSID 婚姻 / 劳动史同时 hazard. `https://mrdrc.dev.isr.umich.edu/wp-content/uploads/2024/04/cp00_lillard.pdf`
- Menken, J. A., et al. (1981). Proportional hazards life table models. *Demography, 18*, 181–200.（`CITED_SECONDARY`）
- *She Left, He Left: How Employment and Satisfaction Affect Women's and Men's Decisions to Leave Marriages*. `https://statisticalhorizons.com/wp-content/uploads/2022/01/She-let-he-left.pdf`（作者与发表信息 `UNKNOWN_AS_OF`）
- *The Impact of Family Background and Early Marital Factors on Marital Disruption*. *JMF*. `10.1177/019251391012001003`（作者 `UNKNOWN_AS_OF`）
- Tuma, T. B., Hannan, M. T., & Groeneveld, L. P. (1979). *AJS, 84*(4), 820–854. `10.1086/226863`（`CITED_SECONDARY`）

### 因果推断 / interference
- Robins, J. M., & Hernán, M. A. *Causal Inference: What If*. Chapman & Hall/CRC. `https://content.sph.harvard.edu/wwwhsph/sites/1268/2024/04/hernanrobins_WhatIf_26apr24.pdf`
- *Toward causal inference with interference*. PMC2600548（作者串 `AGENT_RECALL`；常引为 Sobel & Korper, *Statistical Science* 2010, 27(1)）
- Aronow, S., & Samii, C. — exposure mapping / misspecification. BK Handbook Ch.16. `https://cyrussamii.com/wp-content/uploads/2025/11/BK-EEP-Chp16.pdf`
- *A General Framework for Causal Inference Under Interference* (degree of interference). *JMLR* (2025). `http://jmlr.org/papers/volume26/24-0119/24-0119.pdf`
- Mulder, J. D., Luijken, K., Penning de Vries, B. B. L., & Hamaker, E. L. (2024). Causal effects of time-varying exposures. *SEM, 31*(4), 575–591. `10.1080/10705511.2024.2316586`
- Mulder, J. D., Usami, S., & Hamaker, E. L. (2025). Joint effects in cross-lagged panel research using structural nested mean models. *SEM, 32*(2), 339–355. `10.1080/10705511.2024.2355579`
- Mulder, J. D., & Hamaker, E. L. (2024). Comparing SEM and propensity-score approaches for adjusting for multiple time-varying covariates.（`CITED_SECONDARY`）
- VanderWeele, T. J., Mathur, M. A., & Chen, Y. H. (2020).（`CITED_SECONDARY`）
- Imbens, G. W., & Rubin, D. B. (2015). *Causal Inference for Statistics, Social, and Biomedical Sciences*.；Pearl, J., Glymour, M., & Jewell, N. (2016). *Causal Inference in Statistics*.（`CITED_SECONDARY`）

### 元科学
- Steegen, S., Tuerlinckx, F., Gelman, A., & Vanpaemel, W. (2016). Increasing transparency through a multiverse analysis. *Perspectives on Psychological Science, 11*(6), 702–712. `10.1177/1745691616658637`（`CITED_SECONDARY`）
- Robitzsch, A. (2022). Exploring the multiverse of analytical decisions in scaling educational LSA data. *Eur. J. Investig. Health Psychol. Educ., 12*(7), 731–753. `10.3390/ejihpe12070054`
- Simmons, J. P., Nelson, L. D., & Simonsohn, U. (2011). False-positive psychology.（`CITED_SECONDARY`）
- Peugh, J. L., & Litson, K. (2026). *Monte Carlo Power Analyses Using Mplus and R*. Guilford.

### 软件
- Mplus 9.1.1. `https://www.statmodel.com/`（核实 2026-09-26）
- RI-CLPM & Extensions code supplement. `https://jeroendmulder.github.io/RI-CLPM/`
- R `ctsem` v3.11.1 (2026-07-13). `https://CRAN.R-project.org/package=ctsem`
- R `mirt` v1.47 (2026-08-20). `https://CRAN.R-project.org/package=mirt`
- Bolger & Laurenceau companion site. `http://www.intensivelongitudinal.com/index.html`
- Open Handbook of ESM. `https://ppw.kuleuven.be/okp/esmhandbook.php`
- SSRI APIM tutorial. `https://quantdev.ssri.psu.edu/sites/qdev/files/APIM_tutorial_2020.html`
- `https://www.jars.network/` — **`BLOCKED_POINTER`（实测为停放域，不得引用为可用仓库）**

---

## 12. 给 Architect 的三条可执行建议（`AI recommendation`，非 Human requirement）

1. **把 §5 识别不可能清单（尤其 I4 / I8 / I12 / I14）纳入 canonical 文档的显式非目标。** 这四条不是"暂时做不到"，是"换方法也做不到"。当前 `CURRENT_ARCHITECTURE.md` 的非目标列表覆盖了"单一 LoveScore / 统一欧氏距离 / 统一权重表 / 预写关系状态机 / 从单个案例估计现实概率"，但**没有**覆盖"person / dyad / occasion 三层来源分解的可识别性上限"与"trait-state 二分本身的无解性"。
2. **Wave 2 应加一个 cross-lane 检查：R03（instrument catalog）与本文件的 Q7 结论是否一致。** 若 R03 catalog 的任何 instrument 缺 invariance 证据，则该 instrument 不能进入任何动态陈述。
3. **本文件与 R04 对齐后重估 Q1–Q5 可行性（U5）。** 若数据以 1–2 波为主，LHRM 的动态部分应明确标为"需专门采集设计"，并把 ILD / ESM（R7? / M7）列为独立的采集 lane 而非分析 lane。
