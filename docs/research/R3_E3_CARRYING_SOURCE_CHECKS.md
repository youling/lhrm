# R3-E3 — 承载来源逐字复核报告（carrying-source re-verification）

- **child**: `E3`
- **worktree**: `wt/e3` · **branch**: `research/carrying-source-checks-v0.1`
- **base_sha**: `ee393ca24f9fbf738ac0ed839e99bdc99de6fc3a`（`git rev-parse HEAD` 实测一致）
- **被复核的 corpus**: `research/opencode-overnight-2026-09-27@8adcf0b`（= PR #31 head，18 lane 报告 + `A01`/`A03`/`A04`）
- **authority**: `ARCHITECT_ADJUDICATION_V1`（#30 comment 5854920569）· `ARCHITECT_ROUND3_DISPATCH_V1`（#30 comment 5854930069）Track R3-E item E3
- **角色**: 复核者（verifier），**不是**修复者。本报告**未编辑任何既有文件**。
- **日期**: 2026-09-28

## 0. 方法与判定词表

- 指针一律写"我实际打开的那个 URL / API 端点"，不写"应该可以打开的地方"。
- 逐字比较时给出**我比对的精确字符串**，供第三方复算。
- 判定词（固定五类 + 一类复核不可及）：
  `SOURCE_SUPPORTS_AS_STATED` · `SOURCE_SUPPORTS_SCOPE_NARROWER` · `SOURCE_DOES_NOT_SUPPORT` ·
  `PARTLY_REFUTED` · `UNVERIFIABLE_HERE`（原文未打开）
- **未从任何引用者论文反推被引来源的内容。** 摘要层之外的正文，只有在我实际合法打开时才记为已核。
- **未绕过任何 paywall / robots / 认证。** APA PsycNet、SAGE TDM、Wiley TDM、Elsevier TDM 链接一律**未**使用。

---

## P1 — Joel et al. (2020), PNAS（`10.1073/pnas.1917036117`）

### 我实际打开的指针

| 用途 | 指针 | 结果 |
|---|---|---|
| 摘要（权威副本 A） | `https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:"10.1073/pnas.1917036117"&resultType=core&format=json` | 成功，`pmid=32719123`，`pmcid=PMC7431040` |
| 全文（PMC author manuscript） | `https://pmc.ncbi.nlm.nih.gov/articles/PMC7431040/` | 成功，340,242 B，本地抽取为纯文本 87,080 B |
| 题录核对 | `https://doi.org/10.1073/pnas.1917036117` → Crossref | 成功 |
| SI Appendix | `https://www.pnas.org/content/pnas/117/32/19061.sapp.pdf` | **403**；PMC 附件端点返回 JS interstitial ⇒ **`NOT_OPENED`** |

### P1.1 研究数 / dyad 数 / 两个百分比 — 全部命中

| corpus 字符串（逐字） | corpus 位置 | 原文逐字（我打开的 PMC 全文） | 比对结果 |
|---|---|---|---|
| `43 longitudinal couples studies` / `43 个数据集` | `17:127`、`19:74`、`00_MANIFEST:56` | "Across 43 dyadic longitudinal datasets from 29 laboratories" | ✅ **match** |
| `11,196 对` | `17:127`、`19:74`、`01:215` | "with 11,196 couples (baseline n = 22,163 participants)" | ✅ **match** |
| `关系特异变量解释基线至多 45%、期末至多 18%` | `19:74` | "relationship-specific variables predicted up to 45% of variance at baseline, and up to 18% of variance at the end of each study" | ✅ **match** |
| `29 个实验室` | `17:127` | "from 29 laboratories" | ✅ **match** |
| `86 位研究者` | `17:127`、`17:444` | "The project combines the efforts of 86 relationship researchers" | ✅ **match** |
| `2,413 个测量` | `17:127`、`19:74`、`06:504` | "2,413 (**mostly self-report**) measures collected **at baseline**" | ⚠️ **match 但限定词被丢** |

**`2,413` 的两个被丢限定（低severity，记账项）**：
1. 原文是 **"mostly self-report"**，不是"测量"（无纯度声明）；corpus 写"2,413 个**测量**"并在 `06:504` 写"2,413 **工具**"——"工具"把"mostly"抹成全称。
2. 原文是 **"collected at baseline"**。`06:504` 把这个数字挂在"人内变化幅度随时间"一行，读起来像"跨全时段 2,413 个测量"。

**`17:450` 的内部不一致（数值错，低severity）**：同一文件 `:127` 与 `:444` 写 `2,413`，`:450` 写 `2,414`。原文只有 `2,413`。第三处应改为 `2,413`。

**判定**：`SOURCE_SUPPORTS_AS_STATED`（对 43 / 11,196 / 45% / 18% / 29 / 86）；`2,413` 一项为 `SOURCE_SUPPORTS_SCOPE_NARROWER`。

### P1.2 "人内变化幅度不预测随时间变化" — **这是本轮最需要收窄的一条**

- **corpus 位置**：`06_TRANSITION_LAWS.md:504`
  > `| 人内变化幅度随时间 | **`DIRECTION_NOT_SUPPORTED`** | S04：**"relationship-quality change was largely unpredictable from any combination of self-report variables"**（43 数据集 / 2,413 工具） |`
  该行是 `DVA`（律 C）的"最重要限制证据"之一（`06:108`），并被 `19:208` 的 `L3` 行继承为"最佳可得证据逆向于本律的增量通道"。

- **原文逐字**（我打开的 PMC 全文）：
  - 摘要："Finally, relationship-quality change (i.e., increases or decreases in relationship quality over the course of a study) was largely unpredictable from any combination of self-report variables."
  - 方法（"over time" 这一 outcome 的定义）："The baseline measures collected from each partner were used to predict relationship quality at baseline (the first time point collected), at follow-up (the last time point collected), and **over time (i.e., each participant's slope calculated across all available time points)**."
  - 结果："Analyses predicting change in satisfaction were generally poor. No analyses accounted for more than 5% of the variance, and the confidence intervals for all estimates overlapped substantially. **Self-report variables may be ill-equipped to reliably predict future changes in satisfaction, at least as operationalized here (typically over a span of 1 to 2 y)** (SI Appendix)."
  - 讨论：**"any nascent signal of whether a relationship is going to become better or worse over time does not seem to be detectable in self-reported variables at baseline. Surely, change in relationship quality can be explained by baseline variables in conjunction with time-varying predictors [e.g., stressful life events, the transition to parenthood (42, 43)]. However, models that attempt to account for future change entirely from contemporaneously assessed self-report variables may not prove robust."**
  - 讨论四条约束之三："Third, **change in relationship quality was not predictable from baseline self-report measures**, so change is likely a function of external context, behavioral processes, or other factors that are themselves changing over time."

- **来源实际说的是什么**：不是"人内变化幅度**本身**不预测/不变"，而是"**基线**自报变量不能预测**谁**会变（个体间 slope 差异）"。原文的 outcome 是**每个参与者的 slope**；被否证的是**用同时测量的基线自陈**去预测它。原文**同时明确点名了一条可行路径**——"time-varying predictors"（压力性生活事件、生育transition）。

- **corpus 的转述做了三件来源没做的事**：
  1. 把"between-person prediction of within-person slope"改写成"人内变化幅度随时间"（行标签），去掉了"个体间"这一层；
  2. 删掉 "at least as operationalized here (typically over a span of 1 to 2 y)" 这一操作化限定；
  3. 删掉"基线 + 时变预测子可能可行"这一来源主动给出的反方向线索。

- **判定**：`SOURCE_SUPPORTS_SCOPE_NARROWER`。
  - **不是**方向反转（来源没有说变化可预测），但**是**范围过宽的收窄失真：来源是"基线自陈 → slope 的个体间预测 R² ≤ 5%"，corpus 写成"人内变化幅度随时间 → `DIRECTION_NOT_SUPPORTED`"，可被读成"这条律的斜率通道无证据"。

- **consequence**：
  - `06:504` 行标签必须改为"**基线自陈变量对个体间 slope 差异的预测力**"，并把 `DIRECTION_NOT_SUPPORTED` 降为"对**同时测量的基线自陈**成立；对**时变预测子** `NOT_ESTABLISHED`"。
  - `06:529` 的识别风险第 4 条"若 S04 的一般性结论成立，`Slope` 可能≈0 且不可预测"——"一般性结论"不成立，来源自己给了反例路径。该条须标注为**依赖一个被收窄的 S04**。
  - 受影响的 sibling repair：**E1**（null registry）、**E2**（law status，`DVA` 改写为 level-conditional-slope 候选）、**r3/a3c**（`06` / `16`）、**r3/a2**（`19:74` / `19:208`）、**r3/a4**（`17`）。

### P1.3 "起点差异比变化率更能区分轨迹组" — **该主张在 corpus 里不属于 Joel，属于 Lavner 2012**

- **路由修正（重要）**：dispatch 把这条列在 P1（Joel）下。**corpus 并不这样归属**。
  - `06:499`–`06:502` 把 "declines were isolated to partners who began their marriages with lower levels of satisfaction" 与 "limited evidence … incremental change model … distinguished among trajectory groups" 全部归 **S19 = Lavner et al. 2012**。
  - `16:203`（`B2`）同样归 S19："S19 在婚姻恶化模型的正面对决中 **initial-differences 击败了 incremental-change**"。
  - Joel 2020 全文中**不存在**任何 trajectory-group 划分、任何 intercept-vs-slope discrimination 比较。
- 因此该主张我在 **P2** 下核（见 P2.4）。在 Joel 2020 名下它**没有对应文本**。
- **判定（在 Joel 名下）**：`SOURCE_DOES_NOT_SUPPORT`；**判定（在 Lavner 2012 名下）**：`SOURCE_SUPPORTS_AS_STATED`（见 P2.4）。

### P1.4 scope qualifier "这只是 population-level 的方差陈述" — **是 corpus 加的，不是来源的**

- **corpus 位置**：`19_SYNTHESIS_CANDIDATE.md:76`
  > "**注意这只是 population-level 的方差陈述，不是本体陈述**——R02/R17 均明确不作「partner 侧不存在」的主张。可辩护的最小主张是**存在性/表达性**，不是**增量预测性**；当前项目文档**未做**这个区分。"

- **我实测**：字符串 `population` 在我打开的 Joel 2020 全文中出现 **0 次**（含原始 HTML，正则 `(?i)population` 命中 0）。→ 该短语**不是来源的**。

- **来源自己给的限定是另外三条，而且更强、种类不同**（讨论节逐字）：
  1. "**Our conclusions are also specific to baseline self-report predictor variables**; of the 1,149 relationship-specific variables tested in this project, **99.4% were explicit self-report rating scales** (and similar numerical response scales) rather than independent observations that directly captured participants' real-time behavior."
  2. "These results similarly **do not apply to nonself-report measures of contextual variables**, such as income and debt …, stress …, or the role of social networks …"
  3. "All of the current datasets were sampled from **Western countries** (the United States, Canada, Switzerland, New Zealand, The Netherlands, and Israel)."

- **关键差异**：来源的限定限制的是**预测子类型**（基线自陈 / 显式自陈量表 / 非实时行为）与**样本地理**；corpus 的 "population-level vs 个体" 是**分析层级**限定，是另一回事，且**更弱**（它不说"这是自陈预测子的结论"，也不说"这是西方样本的结论"）。

- **判定**：`SOURCE_SUPPORTS_SCOPE_NARROWER`。
  - `19:76` 的**实质**（"这是方差陈述，不是本体陈述"；"最小可辩护主张是存在性/表达性"）**正确且重要**——来源确实只说增量预测力，不用来说本体。
  - 但 `19:76` 的**限定词本身**必须替换为来源自有的三条（baseline-self-report / 99.4% explicit self-report / Western samples），并加一条 X-14 合规表述。
- **consequence**：`19:76` 改写为双层限定。`19:75` 现有措辞"承载在 `Z(t+1) = F(...)` 上的动态工程**在 population level 上被这一证据告了一记**"中的 `population level` 一词同样无来源支撑，须删或改。受影响 sibling repair：**r3/a2**、**r3/a4**、**E2**。

### P1.5 Joel 的"五条结论" — 逐条落地

corpus 位置：`17_RED_TEAM_FALSIFIERS.md:131`–`17:135`（`F2` 表五行），并在 `19:74`、`14:168`、`19:180` 被复用。

| # | corpus 记的"原文" | 我打开的文本中是否存在 | 判定 |
|---|---|---|---|
| 1 | "the top relationship-specific predictors of relationship quality were **perceived partner commitment, appreciation, sexual satisfaction, perceived-partner satisfaction, and conflict**" | **存在，摘要逐字**。原文写 "**perceived-partner** commitment"（带连字符），corpus 写成 "perceived partner" | ✅ 可核（连字符差异是转录级，**唯一实质差别**） |
| 2 | "Actor-reported variables … predicted two to four times more variance than partner-reported variables … individual differences and partner reports had **no predictive effects beyond actor-reported relationship-specific variables alone**" | **两句都逐字存在于摘要** | ✅ **可核** |
| 3 | "**relationship-quality change … was largely unpredictable from any combination of self-report variables.**" + "No analyses accounted for more than **5% of the variance**" | 两句都逐字存在。但 "No analyses accounted for more than 5%" 的主语被 corpus 抹掉：原文是 "**Analyses predicting change in satisfaction** were generally poor. No analyses accounted for more than 5% of the variance"（satisfaction 专指） | ⚠️ **可核但需补主语** |
| 4 | "**Relatively objective relationship variables (e.g., cohabiting status, dating versus married relationship status, having children) generally mattered little, with the exception of relationship length**" | **逐字存在于讨论节** | ✅ **可核** |
| 5 | "relationship-specific variables predicted up to 45% of variance at baseline, and **up to 18%** … at the end of each study" | **逐字存在于摘要** | ✅ **可核** |

**可直接消除的两条非主张**：
- `16:522` / `19` 系："S23（Joel et al. 2020）正文的五条实证结论（书目已核实，**正文未读**；结论经转述）"——**五条现已全部在已打开的原文中定位**（#1/#2/#5 在摘要，#3 在结果段，#4 在讨论节）。"正文未读"这一自我限制**可以撤销**，替换为逐条定位（见上表）。这正是 `A04-C8`（`A04:22` / `A04:213`，"**一篇 primary 被当作 meta-analysis 使用**"，MAJOR）所指的记账债。
- `A04:241` 的"承重层结论：30 项承重来源中 28 项强度充分；2 项不合格（Joel 2020 转述承重…）"——第 1 项不合格理由**不再成立**；第 2 项（R04 SOEP 著录错）**不在我的 scope 内**（见 §`NOT_VERIFIED`）。

**必须新增的两条非主张**（来源有、corpus 无）：
- **#6（paraphrase-only，corpus 已有但缺限定）**：`17:71` 引 "the predictors trust, intimacy, love, and passion generally performed quite well"——逐字存在，但原文紧接的是 "**in the SI Appendix analyses that included them as predictors**"。且 `Method` 明说这四个变量在**主分析**中被**移除**（"we removed the actor and partner versions of trust, intimacy, love, and passion as predictors (59 total variables across 21 of the datasets)"）。corpus `17:71` 用它论证"在**预测上**可区分"——方向对，但**必须**补上"这是 SI-Appendix 变体，不是预登记主分析"。
- **#7（corpus 完全没有）**：来源的**四条约束**（`17` 系从未转述）——(a) partner 自陈构念不太可能在 actor 自陈之外预测 actor 的关系质量；(b) 个体差异不太可能在关系特异变量之外预测；(c) 变化**不能由基线自陈预测**，故"change is likely a function of external context, behavioral processes, or other factors that are themselves changing over time"；(d) 模型应对表现好的变量设定更大的效应量。**(c) 是对 `DVA` / `RT` / `E1` 最直接相关的一条，且它是来源自己的正向 framing，不是"失败"。**

### P1.6 两条 `CITED_PRIMARY` 引文在 Joel 2020 原文中不存在 — **HIGH severity**

corpus 位置：`16_EMPIRICAL_VALIDATION_PROTOCOL.md:216`（`R16-UC01`），标 `CITED_PRIMARY`：
> "S04 原文："**The standard error across folds strongly underestimates them**"；"**folds are far from independent**"（`CITED_PRIMARY`）；S13；S03"

**我实测**：
- 字符串 `fold`（不分大小写）在我打开的 Joel 2020 全文中出现 **0 次**；在**原始 HTML** 中也 **0 次**（`(?i)fold` 与 `(?i)folds` 均 0）。
- `resampl` / `cluster` / `couple as a unit` / `dyad as` 均 **0 次**。
- 方法层面：论文用 Random Forests（`ntree = 5,000`，`mtry` 默认 1/3），把 "% variance accounted for" 开方转 `r` 后做 random-effects meta-analysis（`k = 43` satisfaction / `k = 31` commitment）。**全文没有交叉验证 fold 这一环节**，因此"fold 之间的标准误"不是这篇论文的对象。

**判定**：`SOURCE_DOES_NOT_SUPPORT`。
**这不属于"方向反转"，但属于同等级的书信完整性事故**：一条被标 `CITED_PRIMARY` 的逐字引文在原文中不存在，且**不可能**来自该文的任何 SI-Appendix（方法层无 folds）。

**consequence**：
- `R16-UC01` 的**方法论主张本身（不确定度的单位是 dyad；不得用 fold 间标准差）不因此失效**——但它失去"primary 支撑"，必须二选一：(i) 改标 `AI recommendation` / `DESIGN_CHOICE`，或 (ii) 重新指向一篇真正说这句话的来源并实际打开它。
- **受影响 sibling repair**：**E1**（null registry 的不确定度条目）、**r3/a3c**（`16`）、**r3/a2**（`19` 若复述）、**r3/b1**（packet 侧若把 `R16-UC01` 记为 primary-backed）。

### P1.7 "n=100 → 误差带 ±10%" — 来源无此数 — **HIGH severity（同一类）**

corpus 位置三处，全部以 S04 为据：
- `16:142`（`R16-OC05`）："理由：R05 SD12（power 随效应类型差 1–2 个量级）+ **S04（n=100 时误差带 ±10%）**"
- `16:217`（`R16-UC02`）："**S04（n=100 → ±10%）**"
- `16:397`（`F-09`）："**S04 的误差带在小样本下极宽**"

**我实测**：`10%` / `n = 100` / `±` / `+/-` / `error band` / `precision` 在 Joel 2020 已打开全文中命中数均为 **0**。

**判定**：`SOURCE_DOES_NOT_SUPPORT`。

**consequence**：这三条判据的**方法论动机（必须预登记事件率量级、必须报最小可检测效应、必须做 power 分析）完全站得住**，但**失去 S04 背书**，须改标 `AI recommendation` / `DESIGN_CHOICE` 或另寻来源。三条判据本身**不必撤回**。
**受影响 sibling repair**：**E1**、**E2**、**r3/a3c**（`16`）、**r3/a2**（`19` 若复述）。

### P1.8 附带命中：R17 对 Joel 的自我纠错是准确的

`17:147` 记："packet 里曾写 4/5，**但自我更正为 5/5**"。`19:180` 的 `R17-F2` 行把 "5/5 top predictor 落在 `DirectedRelationshipState` **之外**" 列为已被 R06/R14/R16 独立采用。我已核实 top-5 名单逐字无误（见 P1.5 #1），因此**该 5/5 计数的事实基础成立**；本报告不裁决"5/5 是否构成 layer 归属论证"（X-2 已由 Architect 裁决为 `REJECT AS ARCHITECTURE CLAIM / KEEP AS DYNAMICS EVIDENCE`）。

---

## P2 — Lavner, Bradbury & Karney (2012)（`10.1037/a0029052`）与其前身

### 我实际打开的指针

| 用途 | 指针 | 结果 |
|---|---|---|
| 题录 + 摘要 | `https://api.crossref.org/works/10.1037/a0029052`（无 abstract 字段）→ `https://api.semanticscholar.org/graph/v1/paper/DOI:10.1037/a0029052` → `https://api.openalex.org/works/doi:10.1037/a0029052` | 成功（摘要由 Semantic Scholar 与 OpenAlex `abstract_inverted_index` **双源一致**重建） |
| **全文（合法 green OA 副本）** | `https://escholarship.org/content/qt33w8w29t/qt33w8w29t.pdf`（eScholarship / UC，Semantic Scholar `openAccessPdf`，`license: other-oa`） | 成功，405,363 B，12 页，本地抽取纯文本 64,376 B |
| APA PsycNet VOR | `https://doi.apa.org/doi/10.1037/a0029052` | **未使用**（付费墙，按规则不绕过） |
| PMC author manuscript | `PMC3513382` | 仅作题录交叉核对 |
| 前身 Williamson & Lavner (2020) | `https://pmc.ncbi.nlm.nih.gov/articles/PMC8153381`（`10.1177/1948550619865056`） | 摘要+正文段落，**通过搜索结果中的 PMC 全文摘录与 SAGE 摘要交叉核对**；该文 VOR `Restricted access`，**未绕过** |
| Lavner & Bradbury (2010) | `https://pmc.ncbi.nlm.nih.gov/articles/PMC2992446` | 同上，**仅摘要层** |

### P2.1 Table 5 逐字（本项此前从未在 corpus 中出现）

> **Table 5**
> Satisfaction Trajectory Parameter Estimates (N = 251 Couples)
>
> | Satisfaction group | n | % | Intercept | Linear | Quadratic |
> |---|---|---|---|---|---|
> | **Husbands (n = 251)** | | | | | |
> | Low | 33 | 13 | 86.24 | −1.31 | 0.02 |
> | Medium | 72 | 29 | 94.19 | −0.20 | |
> | High | 146 | 58 | 98.83 | | |
> | **Wives (n = 251)** | | | | | |
> | Low | 26 | 10 | 86.58 | −1.05 | |
> | Medium | 52 | 21 | 93.66 | −0.27 | |
> | High | 173 | 69 | 100.88 | | |
>
> **Note. All parameter estimates significant at p < .001.**

- **精确显著性脚注措辞**：`Note. All parameter estimates significant at p < .001.`
- **空格格的含义（由正文交叉确证，不由表格推断）**：High 组两个空格是**斜率不显著**，正文逐字："The largest group of husbands ("High Satisfaction"; 58%) had significant intercepts (intercept = 98.83) but **slopes that did not differ significantly from zero**"；妻子同构（"slopes that did not differ significantly from zero"）。
- **Low 组按配偶角色的精确值（dispatch 明确要求）**：
  - **Husbands Low (n = 33, 13%)**：intercept **86.24**、linear **−1.31**、quadratic **0.02**。正文："began with relatively low levels of initial satisfaction (intercept = 86.24) and then experienced a substantial decline in satisfaction characterized by **significant linear and quadratic terms, indicating that their declines in satisfaction flattened out over time**."
  - **Wives Low (n = 10%)**：intercept **86.58**、linear **−1.05**，**无 quadratic**。正文："The third group of wives (10%) began with low levels of satisfaction (intercept = 86.58) and then experienced **large linear declines** in satisfaction."
- **组间检验**（逐字）：丈夫 `F(2, 247) = 85.58, p < .001`，各组两两 `ps < .001`；离婚率 `χ²(2, N = 251) = 10.49, p < .01`，从 High 组 12% / Medium 13% 到 **Low 组 33%**。妻子 `F(2, 248) = 73.83, p < .001`；`χ²(2, N = 251) = 22.78, p < .001`，High 11% / Medium 12% / **Low 46%**。

**bookkeeping 事实**：corpus（`8adcf0b`）**全文没有任何 "Table 5" 字样**（`Select-String 'Table 5|表 5|表5'` 命中 0）。dispatch 提到的 "S19/Lavner exact Table 5" 来自 **`r3/a2` 已落地的修复文本**（`r3/a2:19_SYNTHESIS_CANDIDATE.md:350`、`:384`），不是修复前语料。这一点记录为路由事实，不是缺陷。

**判定**：`SOURCE_SUPPORTS_AS_STATED`（表值、脚注、正文交叉一致）。

### P2.2 "limited evidence" 逐字，**以及它到底限定什么** — **CONFIRM dispatch 的猜测**

- **corpus 位置**：`06:502`
  > `| **段内实际化模型**能解释不同满意度组 | **`DIRECTION_NOT_SUPPORTED`（明确反证）** | S19 原文："**we found limited evidence** to support an incremental change model in which differences in patterns of change in these predictor variables distinguished among trajectory groups" |`

- **原文逐字**（我打开的全文，讨论节）：
  > "**Limited evidence was found to support an incremental change model in which differences in patterns of change in these predictor variables distinguished among trajectory groups.** Husbands with different satisfaction trajectories could be distinguished on the basis of their relationship problems and relationship attributions over time, although the magnitude of these effects was small. Differences between husbands' outcome groups were also found for acute stress and for self-esteem, but not in expected directions (e.g., stress uniformly decreased, and more so in the less satisfied groups). **For wives, changes in risk over time did not significantly distinguish partners with different satisfaction trajectories**, and the general patterns of some changes were inconsistent with the observed trajectories…"

- **转录差异（低severity）**：原文是 "**Limited evidence was found to support…**"；corpus 写成 "**we found limited evidence to support…**"——`we found` 不在原文。

- **它到底限定什么 —— CONFIRM（这是 dispatch 的核心问题）**：
  被比较的是**五个预测子变量**（relationship problems、verbal aggression、negative attributions、acute stress、self-esteem）的 **initial scores vs 4-year changes**；**判据（criterion）是 satisfaction trajectory group**。来源**从未**主张 outcome 的 slope 是平的、也**从未**主张"增量变化通道在 outcome 侧被击败"。
  - 丈夫侧甚至有**部分小效应支持**："For the husbands, changes in four of the five variables … were moderated by trajectory group … Effect size r estimates ranged from .12 to .26 (median = .18), indicating that these effects were **small in magnitude**."
  - 妻子侧是**零支持**："trajectory group membership did not significantly moderate the pattern of change over time for any of the risk variables … these findings indicate that wives' groups tended to change over time at **similar rates**, regardless of their satisfaction trajectories."
  - 摘要同向："**Across all predictor variables, initial values afforded stronger discrimination of outcome groups than did rates of change in these variables.**"

- **判定**：`SOURCE_SUPPORTS_SCOPE_NARROWER`。
  - `06:502` 的**引用本身正确**（语义准确，仅 `we found` 为非原文）。
  - 但 `06:502` 把它标成对"**段内实际化模型**"的 `DIRECTION_NOT_SUPPORTED`（明确反证），是把一个**关于预测子变量的判别力比较**读成了**对 outcome 斜率通道的否证**。**这一步没有来源支撑。**

### P2.3 Lavner 2012 **不**击败 flat / no-slope null — **对 E1 null registry 是决定性的**

- **corpus 的表述**：
  - `06:488`–`06:489`："`**`SELECTION-ONLY`（只起点，无 slope）**`：`E(τ) = Level(τ₀) + 随机游走 + 误差`。**这是本律最强、最危险的对手。** S19 正是它赢了。"
  - `16:203`（`B2`，事后被 X-6 改名为 `B2_STABLE_LEVEL`）："**本协议认为最重要的一条 null，因为它已经击败过一个候选。** R06 F6：S19 在婚姻恶化模型的正面对决中 **initial-differences 击败了 incremental-change** … R06 N1 记为"对律 C 的已核实证伪""
  - `19:208`（`L3`）："Lavner 2012（**初始差异胜出**，对增量模型「limited evidence」）"

- **来源实际报告的（我打开的全文逐字）**：
  1. **样本平均轨迹有显著负斜率**："High intercepts and **negative linear slopes** did characterize the average satisfaction trajectories for husbands and for wives"；"the wives' common trajectory showed a **significant linear decline** over the first 4 years"。
  2. **Table 5：6 个 trajectory×spouse 格中 4 格有显著 linear slope**（Husbands-Low −1.31、Husbands-Medium −0.20、Wives-Low −1.05、Wives-Medium −0.27），Husbands-Low 另有显著 quadratic 0.02。
  3. **作者对整体图景的收尾句**："Overall, although the average marital trajectory was one of declining satisfaction, the majority of spouses actually exhibited stable satisfaction over the newlywed years. **Changes in satisfaction were isolated among the subset of spouses who started with lower levels of satisfaction, with the greatest declines occurring among those spouses who started with the lowest satisfaction.**"
  4. **讨论节的"落败方"不是斜率**："these different marital trajectories appear to be due **more to stable initial differences in a variety of domains**, ranging from verbal aggression to acute stress, **than to changes in those domains over time**."（比较对象再次是**预测子变量的变化**，不是 outcome 的 slope。）
  5. **反过来的支持句**："our longitudinal analyses **lend specificity to the change processes that matter**"。

- **判定**：`SOURCE_DOES_NOT_SUPPORT`（对"S19 击败了 flat/no-slope null / `SELECTION-ONLY` 赢了"这一表述）。
  **同时** `SOURCE_SUPPORTS_SCOPE_NARROWER`（对 `06:499`–`06:501` 的三条：下降集中在起点低者、最严重限于起点最低子集、`Level→Slope` 交互存在性——这三条**成立**，且第三条正是来源自己的 "greatest declines occurring among those spouses who started with the lowest satisfaction"）。

- **这是本轮对下游影响最大的一条。** 来源给出的恰恰是 `LEVEL_CONDITIONAL_SLOPE`（起点条件化的斜率），而 **adjudication V1 的 X-11 已经裁决 `DVA`：keep only as level-conditional-slope candidate, not "incremental change defeated"** —— 来源与裁决**同向**；是 corpus 的语料措辞与裁决相反。

- **consequence**：
  - `06:488`–`06:490` 必须撤下"S19 正是它赢了"与"最危险的对手"；改为"S19 支持 `Level→Slope` 交互存在，并**同时**报告 4/6 格显著非零斜率 ⇒ `SELECTION-ONLY` 作为**诊断基线**成立，作为**已被击败的候选**不成立"。
  - `16:203` 的 "**它已经击败过一个候选**" 与 "R06 N1 记为'对律 C 的已核实证伪'" 必须撤回；"**本协议认为最重要的一条 null**" 按 X-6 / C-P10 的"remove 'most important/already falsified' wording"一并处理。
  - `19:208` 的 "**最佳可得证据逆向于本律的增量通道**" 必须删（`r3/a2` 已在该行加了删除说明，方向正确，但删除的**理由**应换成上面这条来源依据，而不是"那写的是一条注记"）。
  - **受影响 sibling repair**：**E1**（`B2_STABLE_LEVEL` 的 rationale 段）、**E2**（`DVA` 状态列与判 G 的措辞）、**r3/a3c**（`06` / `16`）、**r3/a2**（`19:208` / `19:379` 的 `PENDING_EVIDENCE_CHECK` 清单）、**r3/a4**（`17`）、**r3/a4b**（`18` / `A03`，其 `H-7` 把"判 G 的形式来自 initial-differences 胜出的结果"当**正确**做法，实际形式依据来自一个被误读的来源）。
  - **给 E1 的一条正面输入**：`N8_LEVEL_CONDITIONAL_SLOPE` 的形式依据（`Slope_k = α + β · Level(τ₀)`）在 Table 5 里**有直接实证对应**（Low 组 intercept 86.24/86.58 且斜率最大；High 组 intercept 98.83/100.88 且斜率不显著）。`r3/a3c` 已声明"`N8` 的存在与必要性不依赖该复核结果"——这一点**成立**；但现在它**顺带**获得了来源支撑。

### P2.4 "起点值比变化率更能区分结果组" — 逐字命中

- **corpus 位置**：`06:502`（"limited evidence" 那行）；`16:203`（"initial-differences 击败了 incremental-change"）。
- **原文逐字（摘要）**："**Across all predictor variables, initial values afforded stronger discrimination of outcome groups than did rates of change in these variables.**"
- **原文逐字（结果节）**："**Initial differences in risk by trajectory group.** Consistent with the initial differences model, there were **significant differences in intercepts by trajectory group for every risk factor** (ps < .01; see Table 6). Effect size r estimates ranged from **.20 to .59 for husbands (median = .27)** and **.26 to .45 for wives (median = .33)**, suggesting these differences were moderate to large in size (Cohen, 1988)."
- **判定**：作为**比较陈述**，`SOURCE_SUPPORTS_AS_STATED`。
  作为**"击败 incremental-change"** 的推论，`SOURCE_SUPPORTS_SCOPE_NARROWER`（它击败的是"用**预测子的变化**来区分组"这一**策略**，不是"段内实际化模型"这个 outcome 通道）。
- 附带：`06:499`–`06:500` 的引文 "declines were isolated to partners who began their marriages with lower levels of satisfaction, **with the most severe declines limited to a subset of spouses who began with the lowest initial levels of satisfaction**" **逐字命中**（我打开的全文，"Consistent with predictions and prior work (Kamp Dush et al., 2008; Lavner & Bradbury, 2010), declines were isolated to partners who began their marriages with lower levels of satisfaction, with the most severe declines limited to a subset of spouses who began with the lowest initial levels of satisfaction."）。corpus 在 `:500` 只引了前半句、把后半句当"同上"——**可补全**。

### P2.5 两篇 Lavner 论文的身份关系 / 前身 / 是否**都**拒绝 flat null

- **corpus 中的三个 Lavner 条目**（注意 **S 编号是 lane-local**，`S31`/`S36` 在不同 lane 指向完全不同的论文，见 P3）：
  1. **Lavner, Bradbury & Karney (2012)**，`06:1035` 记为 `S19`，`Journal of Family Psychology, 26(4), 606–616`，`10.1037/a0029052`。**题录我已用 Crossref + OpenAlex 双源核实：逐字一致**（作者序、卷、期、起止页、DOI）。
  2. **Lavner & Bradbury (2010)**，"Patterns of Change in Marital Satisfaction Over the Newlywed Years"，*Journal of Marriage and Family*。**corpus 记为 `07:522` 的 "Lavner & Karney 2010"——作者名单错误**（2010 那篇是 Lavner & Bradbury；2012 那篇才是 Bradbury & Karney 在列）。这是**指代错误**，会让读者以为 R07 引用的是另一篇。
  3. **Williamson & Lavner (2020)**，`10.1177/1948550619865056`，SPPS 11(5), 597–604，`09:169` / `09:270` / `09:528` / `09:618` / `09:705`。

- **谁是谁的前身 —— 确认**：**Lavner & Bradbury (2010) 是 2012 那篇的前身**，且是同一 8-wave / 4-year newlywed 设计的**前半段**：2010 报 **5 条**轨迹（摘要逐字："Using eight self-reports of satisfaction collected over 4 years from 464 newlywed spouses, we identified five trajectory groups, including patterns defined by high intercepts and no declines in satisfaction, moderate intercepts and minimal declines, and low intercepts and substantial declines"；"relationship dissatisfaction appeared to be isolated within two groups … **Characterized by low initial satisfaction scores, rapid linear declines in satisfaction, or both**, those groups comprised about 19% of the sample"）。2012 在**同族设计**上（8 waves / 4 years / 251 newlywed marriages）用 **3 条**轨迹重做，并加上"initial vs change"判别分析。**2012 自己引用 2010 作为前作**（"Replicating previous findings (Lavner & Bradbury, 2010)"；"Lavner and Bradbury (2010) similarly showed that wives tended to have higher satisfaction group assignments than husbands"）。**身份关系确认。**

- **是否两者（乃至三篇）都拒绝 flat / no-slope null —— 明确：都不拒绝。**
  - **Lavner et al. 2012**：见 P2.3（4/6 格显著非零斜率 + 明确的 negative linear slopes 结论句）。
  - **Lavner & Bradbury 2010**：摘要逐字就有 "**low intercepts and substantial declines**"、"**rapid linear declines in satisfaction**"；"dissolution rates were higher, ranging from **40% to 60% over 10 years**"。
  - **Williamson & Lavner 2020**：逐字"Results indicated that, on average, relationship satisfaction **significantly declined over time (husbands: linear slope = −.030, p < .001, wives: linear slope = −.036, p < .001)**"；且"the low satisfaction group had the lowest initial level of satisfaction and **the greatest decline in satisfaction**"；讨论更写"spouses were robustly distinguished by their intercepts (**which were subsequently related to their slopes**)"。
  - **Williamson & Lavner 2020 还额外报告了一条 `Level→Slope` 证据**，与 `06:501` 的 `SUPPORTED（存在性）` 同向。

- **判定**：`SOURCE_DOES_NOT_SUPPORT`（对"两篇都拒绝 flat/no-slope null"这一被 null-registry 改写所依赖的前提）。

- **consequence**：`B2_STABLE_LEVEL` / `N8_LEVEL_CONDITIONAL_SLOPE` 的 rationale **不得**写成"S19（及其前身）击败了 flat null"。可写的最强版本是："三篇 Lavner 系研究一致报告**起点条件化的斜率**（起点最低者降幅最大），且**都同时报告了非零的显著负斜率**；因此 flat/no-slope 不是被击败的候选，而是**被数据支持的方向**；`B2_STABLE_LEVEL` 只能作**诊断基线**，且必须与 `N8_LEVEL_CONDITIONAL_SLOPE` 成对出现。"
- **受影响 sibling repair**：**E1**、**E2**、**r3/a3c**、**r3/a3e**（`09` 的 5-vs-3 轨迹叙述）、**r3/a3d**（`07:522` 的作者名单）、**r3/a2**（`19:208`）。

### P2.6 "head-to-head defeated" 是否公平描述 — 不公平，且是**反向**高危项

- corpus 的实质措辞不是英文 "head-to-head defeated"，但语义等同：`06:489` "S19 正是它赢了"、`16:203` "initial-differences 击败了 incremental-change"、`19:208` "初始差异胜出"。
- **来源说的是一次**预测子判别策略的比较**（initial scores vs 4-year changes，5 个预测子，判据是 satisfaction trajectory group），**不是**两个 **outcome 模型**（`Level`-only vs `Level+Slope`）的对决。来源从未把这两个 outcome 模型摆在一起比较；它反而**报告了两个模型都要估的非零斜率**。
- **判定**：`SOURCE_DOES_NOT_SUPPORT`。
- **注意方向**：这里**不是**"corpus 把来源说反了"，而是"corpus 把来源的**比较对象换了**，然后宣布对方输了"。失败被归给了一个来源从未测试的对手。这是**高危记账项**，因为它同时喂养了 `B2` 的"已击败一个候选"、`DVA` 的"已核实证伪"、以及 `19:208` 的"最佳可得证据逆向"三处结论。
- **受影响 sibling repair**：同 P2.3 / P2.5 全部。

---

## P3 — `Ideal` / 律族来源（schema 层唯一冲突项）

### 我实际打开的指针

| 用途 | 指针 | 结果 |
|---|---|---|
| S17 = Pusch, Neyer & Hagemeyer | `https://api.crossref.org/works/10.1177/01461672221113981`（**含 abstract**）· `https://api.semanticscholar.org/graph/v1/paper/DOI:10.1177/01461672221113981` | 成功（双源一致） |
| S17 OA 判定 | `https://api.unpaywall.org/v2/10.1177/01461672221113981` | `oa_status: green`，但 `best_oa_location.url_for_pdf = null`（evidence `deprecated`）→ **VOR 正文 `NOT_OPENED`**（SAGE TDM 链接为 license-gated，**未绕过**） |
| S16 = Drigotas et al. (1999) | — | **未打开**（见 §`NOT_VERIFIED`） |
| **S31（R06 的 `Ideal` 源）** | — | **无指针可开**，见 P3.1 |

### P3.1 决定性发现：R06 的 `S31` **在全 corpus 中没有任何书目信息**

`Ideal` 升为动态 directed state 的建议（`06:995`–`06:997`，即 §12 **裁决请求 2**，corpus 自称"本 lane 发现的**唯一会改动 schema 层**的冲突"）的依据是 **S31 + S17**。

- **`S31` 在 R06 的编号来源表（`06:1017`–`06:1046`）中不存在条目 31。** R06 的 `S31` 只在 `06:647` / `:649` / `:659` / `:895` / `:897` / `:996` 被当作证据引用，并在 `06:1048` 被归入 "`CITED_SECONDARY`（转述，未读原文）：S20, S27, S29, S30, S31" —— 也就是说，**它从未获得过任何作者、年份、标题、DOI 或刊物**。
- **而 `S31` 在其他 lane 里是完全不同的论文**（S 编号是 lane-local，这一点 corpus 从未声明）：
  - `08b:771` — R08b 的 `S31` = Delavande, Kočar & Zafar (2025), "Information Spillovers Within Couples…"
  - `10:795` — R10 的 `S31` = We-ness Questionnaire (2021) 的土耳其语验证
  - `13:532` — R13 的 `S31` = TimeBench
  - `16:207` — R16 的 `S31` = 一句 "model uncertainty had almost the same impact as sampling errors"
- **判定**：`UNVERIFIABLE_HERE` —— 但**不是**"我打不开"，而是**"corpus 没有给出任何可打开的东西"**。这是一个**可判定为缺陷**的结论：RGM 的 schema 层建议目前挂在一个**无指针**的承载源上。

- **consequence**：
  - 按 **X-11**（"`RGM`: hold pending Ideal-source verification"）与 `r3/a3c` 已落地的 `HOLD_FOR_EVIDENCE`（`r3/a3c:06:245`、`:945`、`:1460`），**`Ideal` 不得进入 `PARAMETER_CONVERGENCE`** —— 维持该 HOLD。
  - **必须补的东西不是"再读一遍原文"，而是 S31 的书目身份**。在 S31 被指认之前，`Ideal` 漂移现象**没有证据基础**，`RGM` 的 `Movement` 通道**没有经验支点**（`r3/a3c:945` 已正确记录了这一点）。
  - `18_CROSS_LANE_CONFLICT_AUDIT.md:428`（N-17，`GENUINELY_DISTINCT`）**必须降级**为 `UNRESOLVED / S31_UNIDENTIFIED`：该行现在把 R01 与 R06 的冲突判为"真正不同"，但冲突一方的**唯一 schema 级依据不可识别**。
  - **受影响 sibling repair**：**E2**（`RGM` 状态列）、**r3/a3c**（`06` §7 / §12）、**r3/a2**（`19:351`）、**r3/a4b**（`18` N-17）。

### P3.2 S17（可识别的那一半）— 一条逐字命中，一条过宽，一条打不开

- **corpus 位置**：`06:642` / `06:643` / `06:644`；题录 `06:1033`。
- **题录核对（Crossref，逐字）**：
  > Pusch, S., Neyer, F. J., & Hagemeyer, B. "Closeness Discrepancies in Couple Relationships: A Dyadic Response Surface Analysis." *Personality and Social Psychology Bulletin* **49**(12), **1709–1722**. `10.1177/01461672221113981`. online 2022-08-11 / print 2023-12.
  - **corpus 错**：页码 `06:1033` 写 **1709–1724**，实为 **1709–1722**。（低severity 指针项；`A01` 的"verified citation repairs"未抓到。）
  - N（corpus 未记）：**N = 1,177 individuals from 748 couples**。
- **`06:642` 第一句 — 判定 `SOURCE_SUPPORTS_SCOPE_NARROWER`**：
  - corpus：「discrepancies between actual and desired closeness are **detrimental to relationship satisfaction and well-being**」
  - 摘要逐字："The analyses found evidence for **linear, but not broad**, closeness discrepancy effects: **SRQ was lower for individuals reporting more negative closeness discrepancies** and, independent of this actor effect, for individuals with partners who reported more negative closeness discrepancies."
  - 差异有三处：(a) 摘要有 **"linear, but not broad"** 这一关键限定，corpus 删了；(b) 原文说的是 **"SRQ was lower"**（一个方向的、负向差异的效应），不是" detrimental … and well-being"；(c) 原文的效应对象是**subjective relationship quality**，corpus 扩成"satisfaction **and well-being**"。
- **`06:642` 第二句 — 判定 `SOURCE_SUPPORTS_AS_STATED`**：
  - 摘要逐字："These results suggest that **low levels of closeness paired with a strong desire for closeness can impair both partners' relational well-being**." ✅ 完全命中。
- **`06:644`（"too close" 非对称）— 判定 `UNVERIFIABLE_HERE`**：
  - corpus：「Feeling too close … may … propel individuals to distance themselves from their partners … likely inducing dissatisfaction on the partner's side」，标 **SUPPORTED（存在性）**。
  - **这句话不在摘要中**；且摘要显示作者自己的效应**只对 negative（想更亲密）差异成立**，positive/too-close 一侧未被本摘要支持——corpus 却把它标成 `SUPPORTED（存在性）`。
  - 该句极可能出自**引言中对既有工作的转述**（参考文献里紧邻有 Mashek, LeB, Israel & Aron 2011 "Wanting less closeness…"、`10.1080/01973533.2011.614164`，与 Gamarel & Golub 2018），即**二手转述**。SAGE VOR 正文 `NOT_OPENED`（green 副本无 PDF，TDM license-gated）。
  - **能定案的东西**：a lawful green copy（S. `10.1027/1016-9040`? no）→ 实际可用途径是 `eScholarship`/`FORZA`（Jena）之外的机构库记录；能一次性定案的是**该句所在段落 + 它是否被标为 prior work**。
- **`06:643`**（S17 支撑 "`Actual` 与 `Desired` 之外的两条通道"）引 Frost & Forrester 2013 / Frost et al. 2017 / Mashek & Sherman 2004 —— **本轮未打开**（见 §`NOT_VERIFIED`），不裁决。
- **consequence**：`06:642` 补"linear, but not broad" + 把 "detrimental … and well-being" 收成 "SRQ lower for **negative** closeness discrepancy"；`06:644` 的 `SUPPORTED` 降为 `CITED_SECONDARY / 待正文核实`，或改为只引摘要可支持的一半。`06:1033` 页码改 1709–1722。
  **受影响 sibling repair**：**E2**、**r3/a3c**、**r3/a2**、**r3/a1**（页码属 citation 修正）。

---

## P4 — kill criterion 所依赖的来源

### P4.1 被撤回的支撑 + "把否定性文献存在性答案当成支持"（`alliance 单向构念`）

- **corpus 位置**：`11_GENERAL_HUMAN_DYADS_SCOPE.md:294`–`11:316`（`L-7` 修复轮补记）、`:369`–`:370`、`:442`、`:546`、`:554`；矩阵行 `11:313`。
- **指针（corpus 自己给的）**：`https://www.frontiersin.org/articles/10.3389/fpsyg.2011.00270/full`；Ardito, A., & Rabellino, U. (2011). *Frontiers in Psychology*, 2:70. `10.3389/fpsyg.2011.00270`。
- **我实际打开**：上引 Frontiers URL（重定向到 `.../journals/psychology/articles/10.3389/fpsyg.2011.00270/full`），943,050 B，本地纯文本。

| corpus 逐字（`11:298`–`11:301` / `:305`） | 我打开的原文 | 判定 |
|---|---|---|
| WAI：`There are three versions of the WAI according to the rater's perspective`；raters `Therapists / clients / clinical observers` | "There are three versions of the WAI according to the rater's perspective." | ✅ 逐字命中（raters 列表在同一段的表格里，同页可查） |
| TARS：`There are three versions of the TARS according to the rater's perspective`；`42 items (21 pertaining to the patient and 21 pertaining to the therapist)` | "There are three versions of the TARS according to the rater's perspective" + "**All of the three versions of the TARS consist of 42 items (21 pertaining to the patient and 21 pertaining to the therapist).**" | ✅ 逐字命中 |
| ARM：`28 items rated on parallel forms by patients and therapists`；`Therapists / clients` | "The ARM has five scales comprising **28 items rated on parallel forms by patients and therapists** using a seven-point scale." | ✅ 逐字命中 |
| 结论段：`must necessarily consider the differences between that perceived by the patient and that perceived by the therapist` | "…therapeutic alliance ruptures, which **must necessarily consider the differences between that perceived by the patient and that perceived by the therapist**." | ✅ 逐字命中 |
| CALTRAS：`41 items, 20 of which refer to the therapist, and 21 to the patient` | "The CALTRAS consists of **41 items, 20 of which refer to the therapist, and 21 to the patient**." | ✅ 逐字命中 |
| Bordin 三分：`the bond` + `the agreement on goals` + `the agreement on tasks` | "the three aspects of the alliance theorized by Bordin's (1979): **the bond, the agreement on goals, and the agreement on tasks**" | ✅ 逐字命中 |

- **判定**：corpus 对 Ardito & Rabellino 的六条引文 `SOURCE_SUPPORTS_AS_STATED` —— **本轮最干净的一条。**

- **"撤回"这件事本身的核实**：corpus 记 `:303` "'alliance 是单向构念'被原文直接反驳（`REFUTED`），该支撑**撤回**"；`:369` "被撤回的说明：`本次未取得 alliance 单向性原文`"。**确认这正是 dispatch 描述的那个逻辑错误**：第一轮把"**没找到**说 alliance 是单向的原文"当成"它不是单向的"的支持，然后这条支持被原文推翻。
- **但要写清楚后果**：`11:554` 自己也记了"**`B1×W` 原先的一条支撑被原文撤回**（`UNVERIFIED` → `REFUTED`）。verdict 之所以不变，是因为**换**了一条理由，不是因为原理由被证实。" ⇒ **换上去的那条理由（referent 是测量面 facet，不是构念属性）现在经我核实站得住**。

- **consequence（替换用 data-condition 判据该怎么写）**：
  - **可安全依赖的**（我已逐字核实）：**同一构念标签在不同工具里的 rater/referent 结构不同** —— WAI/TARS 各有 3 个 rater 版本；TARS 42 题在**同一份量表内**就分裂为 21 指向 patient / 21 指向 therapist；CALTRAS 41 题同样内部分裂 20/21；ARM 28 题有 patients/therapists 的 **parallel forms**；作者本人要求联盟破裂分析 "must necessarily consider the differences between that perceived by the patient and that perceived by the therapist"。
  - **因此替换判据的正确形式是 data/measurement-condition 型**，不是 literature-existence 型。可写成：**"凡 readout 被跨 dyad 类型复用，其 `i`/`j`/`(i,j)` referent 必须由**该 dyad 类型上所用的 instrument 的 rater 结构**显式确定；无 instrument-rater 声明的 readout 不得跨类型共用。"** 这与 **C-P5**（applicability 轴）、**X-4**（`domain` 为 facet 而非必需签名）、**C-P13**（observability registry）同向，且不依赖任何检索失败的否定。
  - **必须同时保留 corpus 已有的诚实限定**（`11:316`）："以上**不是**'已取得 `W` 列跨域等价性证据'… 本节**不主张** `PPR` 在专业 dyad 上的构念等价性已被建立。" 我**确认**这条限定是必要的：Ardito & Rabellino 是**治疗联盟单一领域**综述。
- **受影响 sibling repair**：**E2**（无直接依赖）、**r3/a3f**（`11`）、**C-P5 / C-P13 的 measurement-semantics 分支（`architect/measurement-semantics-v0.1`）** —— 后者应把"instrument rater 结构 → referent"作为 registry 的一个必填字段。

### P4.2 "notorious" 的 stance-selection 主张 — 逐字命中 + 一处过强

- **corpus 位置**：`09_DYNAMIC_SYSTEMS_AND_HYSTERESIS.md:354`–`09:358`（`O3`），标 `CITED_PRIMARY`；并被 `09:759`（`K4`）用作"**撤退**"触发条件、并锚定 `09:705` / `09:716` 的替代论证。
- **指针**：`Pohle, J., Langrock, R., van Beest, F., & Schmidt, N. M. (2017). arXiv:1701.08673`。我实际打开 `https://export.arxiv.org/abs/1701.08673`（v2, submitted 30 Jan 2017, last revised 14 Apr 2017）。
- **摘要逐字**：
  > "We discuss the **notorious problem of order selection in hidden Markov models**, i.e. of selecting an adequate number of states, highlighting typical pitfalls and practical challenges arising when analyzing real data. Extensive simulations are used to demonstrate the reasons that render order selection particularly challenging in practice despite the conceptual simplicity of the task. In particular, we demonstrate why well-established formal procedures for model selection, such as those based on standard information criteria, **tend to favor models with numbers of states that are undesirably large in situations where states shall be meaningful entities**. We also offer a **pragmatic step-by-step approach** together with comprehensive advice for how practitioners can implement order selection. Our proposed strategy is illustrated with a real-data case study on muskox movement."

- **判定**：
  - "notorious problem of order selection in hidden Markov models" → `SOURCE_SUPPORTS_AS_STATED`（**逐字命中**）。
  - "AIC 和 BIC 倾向于偏好状态数过多的模型" → `SOURCE_SUPPORTS_AS_STATED`（原文是 "tend to favor models with numbers of states that are undesirably **large**"，"desirably" 一词保留了条件从句 "in situations where states shall be meaningful entities"；corpus `09:358` 的中文表述"系统性地高估状态数"**丢掉了这个条件从句**，建议补回）。
  - "**不存在可普适、客观的单一标准**"（corpus `09:358` 写作 "**no one-size-fits-all objective and universally applicable criterion can be developed for order selection in HMMs**"）→ `UNVERIFIABLE_HERE`（正文未打开），且**摘要方向上略相反**：作者"offer a pragmatic step-by-step approach"。若这句在正文，须按正文原样转述；若正文也没有，该绝对命题应删除。
- **consequence**：`09:356` 与 `09:358` 前半可标 `CITED_PRIMARY`。`09:358` 的绝对命题降级为待核 / 或删除。`09:759`（`K4`）若依赖那句绝对命题，其"撤退"触发条件须改写为可核版本（"标准信息准则在状态须具实体意义时系统偏好过多状态"）。**受影响 sibling repair**：**r3/a3e**（`09`）、**E2**（若 `RT` 的 stance 论证引用它）、**r3/a2**（`19` 若复述）。

### P4.3 大样本研究与另一 lane 的 "construct hole" — **两者不冲突，是 cross-lane audit 的范畴错误**

- **corpus 侧 A（`SUPPORTED`）**：`06:803`
  > `| demand–withdraw **模式**在恋人/伴侣互动中存在/普遍 | **SUPPORTED** | S09：配偶要求 r = .360，撤回 r = .423，顺从 r = .418，**开放**系统统计 r = .239，**生气** r = .249；**74 研究 / N = 14,255** |`
  以及 `19:210`（`L5` = `RT`）：「Schrodt 2014：**74 研究 / 14,255**；**性别对称**（wife-demand r = .380 vs husband-demand r = .392）」
- **corpus 侧 B（`construct hole`）**：`10:689`（`G16`）
  > `| G16 | **conflict pattern 存在**（如 demand–withdraw） | construct hole（本体/测量有缺） | … | **本 lane 未找到强引用** → `UNKNOWN_AS_OF` | Bodenmann et al. 2011; Falconier et al. 2015 |`
- **指针**：`https://api.crossref.org/works/10.1080/03637751.2013.813632`（无 abstract）+ `https://api.openalex.org/works/doi:10.1080/03637751.2013.813632`（`abstract_inverted_index` 完整重建）+ `https://api.semanticscholar.org/.../10.1080/03637751.2013.813632`（`abstract: null`，publisher elided；`oa_status: closed`）⇒ **VOR 正文 `NOT_OPENED`**，无合法 OA 副本。
- **摘要逐字（OpenAlex 重建，标点已复原）**：
  > "This meta-analysis reviews the findings of **74 studies (N = 14,255)** examining associations between demand/withdraw pattern interaction and individual, relational, and communicative outcomes. When both individual behaviors—demanding and withdrawing—are considered **collectively**, cumulative evidence indicates a moderate, meaningful relationship between the demand/withdraw pattern and **overall relational outcomes (r = .360)**. **Similar effect sizes were observed for wife demand/husband withdraw (r = .380) and husband demand/wife withdraw (r = .392)**, although the size of the demand/withdraw patterns in studies that included **distressed/clinical participants (r = .413)** was greater in magnitude than that obtained in **nondistressed studies (r = .345)**. On average, higher correlations with **relational outcomes (r = .423)**, **communicative outcomes (r = .418)**, **demographic variables (r = .239)**, and **well-being (r = .249)** were also observed."

- **`19:210`（`L5`）判定**：`SOURCE_SUPPORTS_AS_STATED` —— `74 研究` ✅、`14,255` ✅、`r = .380` vs `r = .392` ✅、"**性别对称**"这一措辞公平（原文自己写 "Similar effect sizes were observed for…"）。

- **`06:803` 判定：`PARTLY_REFUTED` — 四个 r 值被挂到了错误的 outcome 类别上（记账事故，中severity）**：
  | corpus `06:803` 的标签 | 原文里这个数**实际**是什么 | 值 |
  |---|---|---|
  | 配偶要求 `r = .360` | overall relational outcomes（D/W 模式**整体**） | .360 ✅ |
  | **撤回** `r = .423` | **relational outcomes**（各类关系结果） | .423 ❌ 标签错 |
  | **顺从** `r = .418` | **communicative outcomes**（沟通结果） | .418 ❌ 标签错 |
  | **开放系统统计** `r = .239` | **demographic variables**（人口学变量） | .239 ❌ 标签错 |
  | **生气** `r = .249` | **well-being**（幸福感） | .249 ❌ 标签错 |
  - 摘要**没有任何**按 D/W 行为类别（demand / withdraw / compliance / openness / anger）分解的 r。
  - **`06:808` 的引文**（"although researchers have generally examined DM/W as a predictor of relational dissatisfaction, it is certainly plausible that dissatisfied partners are motivated to communicate desires for change that lead to DM/W behaviors"）→ `UNVERIFIABLE_HERE`（不在摘要；正文未打开）。无 OA 副本、publisher elided。

- **"construct hole" 与 `SUPPORTED` 是否冲突 —— 不冲突，是范畴错误**：
  - Schrodt 2014 支持的是**关系层关联**（D/W 模式 ↔ 关系结果，`r = .360`，74 研究的累积证据）。`06:803` 的 `SUPPORTED` 成立。
  - R10 `G16` 的 `construct hole` 问的是**另一个问题**：LHRM 该不该有一个**离散的"conflict pattern"构念 / `PairState` 槽位**。`10:478` 自己写得很清楚："`Bodenmann et al. (2011)` 只证实了'共同应对状态是后续状态的一个构成部分'，**没有**证实'共同'（两个视角之间）本身构成一种状态……`PairState` 通道**没有结构性位置**。"
  - 所以 `18_CROSS_LANE_CONFLICT_AUDIT.md` 若把它们记成冲突，那是把"**现象有经验支持**"与"**本体该不该有槽位**"混成了一件事。
- **"本 lane 未找到强引用" 的定性**：按 **X-14**，这是**检索范围陈述**，不是领域级不存在。R10 的写法若已是 `UNKNOWN_AS_OF`，则合规；`18` 若据此判 `UNKNOWN_AS_OF` → "无强引用"则需收窄为检索范围表述。
- **consequence**：`06:803` 的四个标签必须改成四个 outcome 类别（relational / communicative / demographic / well-being），并注明 `.360` 是**模式整体**。`19:210` 保持不变。`18` 的相关行从"冲突"降为"范畴不同（经验关联 vs 本体槽位）"。
  **受影响 sibling repair**：**E2**（`RT` 的 `SUPPORTED` 行）、**r3/a3c**（`06`）、**r3/a2**（`19:210`）、**r3/a3e**（`09` / `10`）、**r3/a4b**（`18`）。

---

## P5 — 争议数值归属

### P5.1 review-article 的两个争议数值 — **CONFIRMED 不在 deposited abstract**

- **corpus 位置**：`02b_CONSTRUCT_REDUNDANCY_AUDIT.md:286`（并被 `00_MANIFEST.md:52` 复述为 R02 头号证据指针；`18:85` 复述 `R2 = .54`）
  > 「三者联合解释 commitment 方差 `R2 = .54 (95% CI [.53,.55])`；单项最强为 satisfaction（`β² = .47`），其次 investment（`.32`），再次 alternatives（`−.19`）」

- **指针**：`https://api.crossref.org/works/10.1111/pere.12268` —— **含 deposited abstract**（这是本条能定案的原因）。
- **摘要逐字**：
  > "This meta-analysis included **50,427 participants from 202 independent samples** (collected between 1980 and early 2016) that had examined the intercorrelations between satisfaction, investment size, quality of alternatives, and commitment. Across all studies, **satisfaction had the largest aggregate association with commitment (r = 0.65)**, followed by **investments (r = 0.53)** and **quality of alternatives (r = −0.43)**."

- **判定**：
  - `N=50,427` / `k=202` / `r = .65 / .53 / −.43` → `SOURCE_SUPPORTS_AS_STATED`。
  - **`R² = .54 (95% CI [.53,.55])`** → `SOURCE_DOES_NOT_SUPPORT`（摘要**无 R²、无 CI**）。
  - **`β² = .47 / .32 / −.19`** → `SOURCE_DOES_NOT_SUPPORT`（摘要**无 β²**；且 `β²` 记法未在任何已打开文本中定义）。
  - ⇒ **CONFIRM `A01` 的 F-15**（`A01:247`、`A01:213`、`A01:723` NR-02-6）。**这不是"转述"，是摘要层不存在的数值。**
- **附带指针错误（新发现，MINOR）**：Crossref 与 A01 的 DOI 解析**都只列 3 位作者**（Tran, Peter; Judge, Madeline; Kashima, Yoshihisa）。corpus `14:327` 写 "Tran, P., Judge, M., Kashima, Y., **& Agnew, C. R.** (2019)" —— **多出一位作者 Agnew**。corpus `17:563` 的 3 作者版本是对的。`14:327` 应改。卷期页 `26(1), 158–180` ✅。
- **另一处 A01 指错行号（MINOR）**：`A01:247` 说复述在 `00_MANIFEST.md:50`；实际 R02 行在 `00_MANIFEST.md:52`。
- **consequence**：`02b:286` 的 `R² CI` 与 `β²` 按 `A01` 的 NR-02-6 处理（降 `CITED_SECONDARY` + 标"未在摘要层核对"），或补页码/表号后重新核。`18:85` 的 `R2 = .54` 作为**跨 lane 冲突依据**须同样降级。`14:327` 作者名单修正。
  **受影响 sibling repair**：**r3/a1**（A01/A04 的 citation 修正 —— 并须**不要**把 A01 F-18 的"改成 Relationship Satisfaction"应用到 Bodenmann 2011，见 P5.3）、**r3/a3a**（`02` / `02b`）、**r3/a3f**（`14`）、**r3/a4b**（`18`）、**r3/a2**（`00_MANIFEST`）。

### P5.2 "人们可靠区分 6 个维度中的 5 个" + coordination 缺口

- **corpus 位置**：`10_MUTUALITY_POWER_DEPENDENCE.md:112`（主陈述）、`10:531`（`G6` 承重行）、`18` 未单列。
  > 「`Gerpott, Balliet, Columbus, Molho & de Vries (2018, JPSP 115, 716–742)` 用 **242 个条目**检验发现：人们（在情境内与情境外）**只能可靠区分 6 个维度中的 5 个**，缺 *coordination*（basis of dependence）。得到的主观互赖模型（mutual dependence / power / conflict / future interdependence / information certainty）仍能解释 **24%** 的合作方差，超出 DIAMONDS 模型。」

- **指针**：`https://api.crossref.org/works?query.bibliographic=Selecting+an+interdependence+network+model+for+power+and+dependence+Gerpott+2018` → 定位到正确记录；`https://api.openalex.org/works/doi:10.1037/pspp0000166`（`abstract_inverted_index` 完整重建；**Crossref 未存 abstract**）。**VOR 正文 `NOT_OPENED`**（`oa_status: green` 但 `best_oa_location.url_for_pdf = null`；VU 库落地页 `research.vu.nl/en/publications/e72c64c4-c6ea-4407-a6df-0b2a3814ed51` 无 PDF）。
- **题录（Crossref 逐字）**：Gerpott, F. H., Balliet, D., Columbus, S., Molho, C., & de Vries, R. E. "**How do people think about interdependence? A multidimensional model of subjective outcome interdependence.**" *Journal of Personality and Social Psychology* **115(4)**, 716–742. `10.1037/pspp0000166`. 另有配套 `10.1037/t69611-000` "Situational Interdependence Scale"（PsycTESTS Dataset）。
  - **corpus 缺 issue (4) 与 DOI**。低severity，但这是 `G6` 的唯一承载指针。
- **摘要逐字（重建）**：
  > "Interdependence is a fundamental characteristic of social interactions. Theory states that **6 dimensions** describe differences between social situations. Here, we examine if these are how people think about their interdependence with others in a given situation. We find that (in situ and ex situ) people can reliably differentiate situations according to **5, but not 6, interdependence dimensions: (a) mutual dependence, (b) power, (c) conflict, (d) future interdependence, and (e) information certainty.** This model offers a unique framework … compared to another recent situation construal (**DIAMONDS**) model. … **explains substantial variation in cooperative behavior**, experience of emotions (i.e., happiness, sadness, anger, disgust), **24% of variance in cooperation, above and beyond the DIAMONDS model.** Throughout these studies, we develop and validate a multidimensional measure of outcome interdependence … the **Situational Interdependence Scale (SIS)**."

- **判定**：
  - "**5, but not 6, interdependence dimensions**" + 五个维度名 + "**24% of variance in cooperation, above and beyond the DIAMONDS model**" → `SOURCE_SUPPORTS_AS_STATED`（**逐字命中**，含 "in situ and ex situ" 这一 corpus 写对了的条件）。
  - "缺 *coordination*（basis of dependence）" → `UNVERIFIABLE_HERE`：**摘要未点名失败的第 6 维**。
  - "**242 个条目**" → `SOURCE_DOES_NOT_SUPPORT`（单位错 + 摘要无此数）：摘要**没有给任何 N**。"242 个条目"把人数/案例数写成了量表条目数；一个 5 维（理论 6 维）多维量表不可能有 242 题。该数在摘要层无法核实，**不能**按 `242 items` 引用。
- **consequence**：
  - `10:112` 删掉"242 个条目"，改为"（摘要层未给 N；**待正文核实**）"，或去 VU 落地页取正文确认 242 的真实单位。
  - `10:112` 的"缺 *coordination*"降为 `UNVERIFIABLE_HERE` + 待正文；**但**"5 而非 6"这个有损检验**本身已核实成立**，因此 `10:114`–`10:117` 的两条含义（支持保留有向维度 / 任何"人能感知 X"的声称须先过 6→5 有损检验）**可以保留**，只需把"缺哪一维"这一细节标为待核。
  - `10:531`（`G6`）的 `Gerpott et al. 2018` 补 issue + DOI `10.1037/pspp0000166`。
  - **受影响 sibling repair**：**r3/a3e**（`09` / `10`）、**C-P13 / D5（observability registry，`architect/measurement-semantics-v0.1`）** —— 6→5 有损检验是 registry 里"structurally unobservable / 不可独立感知"的一等判据，值得被引用为**已核实的先例**。

### P5.3 "systemic measure predicts better than discrepancy" + 样本量 — **逐字命中**

- **corpus 位置**：`10:443`（§4.8 标题「**共同应对的证据如何击败 discrepancy**」）、`10:447`、`10:449`、`18:419`（N-08）。
- **指针**：`https://api.crossref.org/works/10.1027/1016-9040/a000068` —— **含 deposited abstract**。
- **题录（Crossref 逐字）**：Bodenmann, G., Meuwly, N., & Kayser, K. "**Two Conceptualizations of Dyadic Coping and Their Potential for Predicting Relationship Quality and Individual Well-Being**" [subtitle "**A Comparison**"]. *European Psychologist* **16(4)**, 255–266. `10.1027/1016-9040/a000068`.
- **摘要逐字**：
  > "Two main models of dyadic coping are proposed in the current literature: (1) a **comparative approach** in which each partner's individual coping is compared with the other's individual coping with regard to congruence or discrepancy and (2) a **systemic model** where dyadic coping is conceptualized as an **interactive and reciprocal process**. … The study is conducted with **443 Swiss couples**. Results reveal that both dyadic coping measures are related to relationship quality and psychological well-being. **However the systemic dyadic coping measure is a stronger predictor than the discrepancy measure for relationship quality.** Both measures show weaker associations with well-being."

- **判定**：
  - "systemic measure predicts better than discrepancy" → `SOURCE_SUPPORTS_AS_STATED`（**逐字命中**，且 corpus 补的限定 "**for relationship quality**"（不是 well-being）是**正确且必要**的 —— 原文明确 "Both measures show **weaker** associations with well-being"）。
  - **N = 443 couples** → `SOURCE_SUPPORTS_AS_STATED`（原文是 "**443 Swiss couples**"，即 **443 对**，不是 443 名受试者）。corpus `10:447` / `00_MANIFEST:60` 写 "N = 443"／"N=443"——**单位应写"对"**。（A01:220 把它写成 "N=443（受试者对）"亦含混。）
  - `10:449` 的引文摘录**准确**，且它的省略号正好落在本文逐字验证过的那一句开头。
  - **Falconier et al. (2015) 侧**（`r = .45`、`17,856`、`72 samples`、by-partner/both > by-self，corpus `10:453`–`10:457`）→ `UNVERIFIABLE_HERE`：`https://api.crossref.org/works/10.1016/j.cpr.2015.07.002` **未存 abstract**；Elsevier TDM 链接为 license-gated，**未绕过**。`A01:220` 已把它记为 `NOT_VERIFIED_BY_A01`。题录 `Clinical Psychology Review 42, 28–46` ✅（Crossref `page: 28-46`）。
- **必须纠正 A01 的一处"citation repair"（MINOR，但会引入新错误）**：`A01:250`（F-18 第三子项）断言 Bodenmann 2011 原题是 "…predicting **Relationship Satisfaction**"。**这是错的。** Crossref 存的题名是 "…Predicting **Relationship Quality** and Individual Well-Being"，corpus `10:767` 的写法**是对的**；corpus 唯一可加的是被漏掉的副题 "**A Comparison**"。
  ⇒ **`r3/a1` 若已把该题名改成 "Relationship Satisfaction"，必须回退。**
- **consequence**：`10:443` 的 §标题「如何击败 discrepancy」**过强** —— 来源报告的是**两个模型对 relationship quality 的预测力比较**，不是"击败"；且 `10:478` 自己已诚实记下"没有证实'共同'本身构成一种状态"。建议改题为「两种 dyadic coping 构念的预测力比较，及它**不**能证明什么」。`10:447` 补 "443 对" 与副题。Falconier 三项数值维持 `NOT_VERIFIED`。
  **受影响 sibling repair**：**r3/a3e**（`10`）、**r3/a1**（**回退 A01 F-18 第三子项**）、**r3/a4b**（`18` N-08）。

### P5.4 两个争议的相关系数（女 r = .26 vs r = .25）— **可判定：.26**

- **corpus 位置 A（`r = .26`）**：`02_CONSTRUCT_CONVERGENCE.md:146`、`:152`、`:270`、`:320`；`03_MEASUREMENT_INSTRUMENTS.md:65`；`18:343`、`:344`、`:544`。
  > 「自陈 vs 生殖器唤起的一致性 meta（Chivers, Seto, Lalumière, Laan & Grimbos 2010, *Arch Sex Behav* 39:5-56, `10.1007/s10508-009-9556-9`）… **男 r = .66，女 r = .26**」；`02:320` 另记「**132 项研究** 1969–2007；**2,505 女 / 1,918 男**」
- **corpus 位置 B（`r = .25`）**：`02b_CONSTRUCT_REDUNDANCY_AUDIT.md:421`、`:461`（**并把该数挂在两个来源上**：`Chivers et al. 2010` + `Meston & Stanton 2018`）；`18:345`。
- **指针**：`https://api.semanticscholar.org/graph/v1/paper/DOI:10.1007/s10508-009-9556-9` —— **含完整摘要**（Europe PMC 亦有 `PMC2811244`）。**VOR 正文未打开**（`openAccessPdf` 标 `HYBRID / CCBYNC` 但那是 Springer 的 VOR，本次未下载；摘要层已足以定案该数字）。
- **摘要逐字**：
  > "We identified **132 peer- or academically-reviewed laboratory studies published between 1969 and 2007** reporting a correlation between self-reported and genital measures of sexual arousal, with total sample sizes of **2,505 women and 1,918 men**. There was a **statistically significant gender difference in the agreement** between self-reported and genital measures, with **men (r = .66) showing a greater degree of agreement than women (r = .26)**. **Two methodological moderators** of the gender difference in subjective-genital agreement were identified: **stimulus variability and timing of the assessment of self-reported sexual arousal.**"

- **判定（可判定部分）**：
  - Chivers et al. 2010 的女性值 = **`.26`**，男性 = **`.66`** ⇒ **corpus A 正确，corpus B 的 `.25` 在"归给 Chivers 2010"这一条上被证伪**。
  - `132 项研究` ✅、`1969–2007` ✅、`2,505 女 / 1,918 男` ✅ —— corpus A 的这三项全部命中。
  - `02:320` 的"两条关键解释性假设 = stimulus variability + 报告时点" ✅ 命中（"stimulus variability and timing of the assessment of self-reported sexual arousal"）。**这两个 moderator 恰好就是 `02` 用来给 `SexualDesire` 加 `measurement_channel` 字段的论证** —— 该论证现在有了逐字依据。
  - **`Meston & Stanton 2018` 这一条腿 → `UNVERIFIABLE_HERE`**（未打开）。按 dispatch 要求"**不要**选一个我核不出来的赢家"：我只判 `.25` **不能**归给 Chivers；不判 Meston & Stanton 支持什么。
  - `02b:421` 的另一条（"与'完全不同 vs 完全无互补'双面"）与 `02b:461` 的 DSM-5 引文 → 未核，不裁决。
- **附带发现（LOW severity，记账项）**：`03:65` 另记「**20 项研究** r=.66 / .44」——摘要只给了**合并**值 `.66`，未给分层的 20 项 / `.44`。该子项 → `UNVERIFIABLE_HERE`，须在引用前补齐。
- **consequence**：`02b:421` 与 `02b:461` 的 `女 r = .25` 改为 `r = .26` 并**只挂 Chivers et al. 2010**；若仍要保留 Meston & Stanton，须先实际打开它并给出**它自己**的数字。`18:345`（R02 立场）随之更新为"`.26`（Chivers 2010 摘要层）"。
  **受影响 sibling repair**：**r3/a3a**（`02` / `02b`）、**r3/a3b**（`03`）、**r3/a4b**（`18`）。

---

## 汇总表

| # | 优先项 | 语料主张（逐字，位置） | 打开的指针 | 判定 | 严重度 |
|---|---|---|---|---|---|
| P1.1 | Joel 研究数/dyad/百分比 | `43 个数据集`、`11,196 对`、`至多 45%`、`至多 18%`（`17:127`,`19:74`） | PMC7431040 全文 + Europe PMC 摘要 | `SOURCE_SUPPORTS_AS_STATED` | — |
| P1.1b | `2,413` | `2,413 个测量` / `2,413 工具`（`17:127`,`19:74`,`06:504`） | 同上（原文 "mostly self-report … at baseline"） | `SOURCE_SUPPORTS_SCOPE_NARROWER` | LOW |
| P1.1c | `2,414` | `2,414`（`17:450`） | 同上（原文 `2,413`） | `SOURCE_DOES_NOT_SUPPORT` | LOW |
| P1.2 | "人内变化幅度随时间" | `DIRECTION_NOT_SUPPORTED`（`06:504`） | 同上 | `SOURCE_SUPPORTS_SCOPE_NARROWER` | **HIGH**（范围过宽 + 删掉来源的反方向线索） |
| P1.3 | "起点差异胜出"归 Joel | `06:499`–`502` 归 S19 而非 S04 | 同上 | 在 Joel 名下 `SOURCE_DOES_NOT_SUPPORT`；在 Lavner 名下见 P2.4 | MED（路由） |
| P1.4 | scope qualifier | `19:76` "这只是 population-level 的方差陈述" | 同上（`population` 命中 **0**） | `SOURCE_SUPPORTS_SCOPE_NARROWER` | MED |
| P1.5 | 五条结论 | `17:131`–`17:135` | 同上 | #1/#2/#4/#5 逐字命中；#3 需补主语；#6 需补 SI-Appendix 限定；#7（来源四条约束）corpus 完全没有 | MED（消除 + 新增） |
| P1.6 | fold 引文 | `16:216` `CITED_PRIMARY`，"standard error across folds…" | 同上（`fold` 命中 **0**，原始 HTML 亦 0；方法无 CV fold） | `SOURCE_DOES_NOT_SUPPORT` | **HIGH** |
| P1.7 | `n=100 → ±10%` | `16:142`,`16:217`,`16:397` | 同上（`10%`/`n = 100`/`±` 命中 **0**） | `SOURCE_DOES_NOT_SUPPORT` | **HIGH** |
| P2.1 | Table 5 数值 + 脚注 | corpus **无** Table 5；`r3/a2:350` 引用了它 | eScholarship 全文（合法 green OA） | `SOURCE_SUPPORTS_AS_STATED` | — |
| P2.2 | "limited evidence" 限定对象 | `06:502` 判为"段内实际化模型"被反证 | 同上 | `SOURCE_SUPPORTS_SCOPE_NARROWER`（引用准确，归属错） | **HIGH** |
| P2.3 | S19 击败 flat/no-slope null | `06:489` "S19 正是它赢了"；`16:203` "已击败过一个候选"；`19:208` | 同上（4/6 格显著非零斜率 + "negative linear slopes did characterize…"） | `SOURCE_DOES_NOT_SUPPORT` | **HIGH（决定性）** |
| P2.4 | 起点值 > 变化率的判别力 | `06:502`；`16:203` | 同上（摘要 + 结果节逐字） | 比较陈述 `SOURCE_SUPPORTS_AS_STATED`；"击败"推论 `SOURCE_SUPPORTS_SCOPE_NARROWER` | MED |
| P2.5 | 两篇 Lavner 的身份 / 是否都拒 flat null | `07:522` "Lavner & Karney 2010"；`09:*` | PMC2992446 / PMC8153381 摘要 + 2012 全文 | 身份 `SOURCE_SUPPORTS_AS_STATED`（但作者名单错）；"都拒 flat null" `SOURCE_DOES_NOT_SUPPORT` | **HIGH** |
| P2.6 | "head-to-head defeated" | `06:489` / `16:203` / `19:208` | 同上 | `SOURCE_DOES_NOT_SUPPORT` | **HIGH** |
| P3.1 | R06 `S31`（`Ideal` schema 层依据） | `06:647` 等 + `06:995` 裁决请求 2 | **无指针存在**（R06 来源表无 31；且 S 编号 lane-local） | `UNVERIFIABLE_HERE`（可判定为**缺陷**） | **BLOCKER** |
| P3.2 | S17 "detrimental…well-being" | `06:642` | Crossref `10.1177/01461672221113981` 摘要 | `SOURCE_SUPPORTS_SCOPE_NARROWER`（丢 "linear, but not broad"） | MED |
| P3.2b | S17 "both partners' relational well-being" | `06:642` | 同上 | `SOURCE_SUPPORTS_AS_STATED` | — |
| P3.2c | S17 "too close" 非对称 | `06:644` `SUPPORTED（存在性）` | 同上（**不在摘要**；VOR `NOT_OPENED`） | `UNVERIFIABLE_HERE` | MED |
| P3.2d | S17 页码 | `1709–1724`（`06:1033`） | Crossref（`1709–1722`） | `SOURCE_DOES_NOT_SUPPORT` | LOW |
| P4.1 | Ardito & Rabellino 六条引文 | `11:298`–`11:305` | Frontiers 全文（open access） | `SOURCE_SUPPORTS_AS_STATED` | — |
| P4.1b | "否定性存在性答案当支持" | `11:369` | 同上 | **CONFIRMED**（且替换理由现经逐字核实） | MED（可关闭） |
| P4.2 | "notorious" + AIC/BIC 偏好过多状态 | `09:356`,`09:358` | arXiv:1701.08673v2 摘要 | `SOURCE_SUPPORTS_AS_STATED` | — |
| P4.2b | "no one-size-fits-all 判据可被建立" | `09:358` | 同上（不在摘要；摘要反而 offer pragmatic approach） | `UNVERIFIABLE_HERE` | MED |
| P4.3 | Schrodt 74/14,255 + 性别对称 | `19:210` | OpenAlex 摘要重建 | `SOURCE_SUPPORTS_AS_STATED` | — |
| P4.3b | Schrodt 四个 r 的标签 | `06:803` | 同上 | `PARTLY_REFUTED`（.423/.418/.239/.249 挂在错误的 outcome 类别上） | MED |
| P4.3c | Schrodt 因果引文 | `06:808` | 同上（不在摘要；无 OA） | `UNVERIFIABLE_HERE` | LOW |
| P4.3d | Schrodt vs R10 `G16` construct hole | `06:803` vs `10:689` | 同上 | 两者**不冲突**（范畴不同） | MED（cross-lane 修正） |
| P5.1 | `R² = .54 (95% CI [.53,.55])`、`β²` | `02b:286` | Crossref `10.1111/pere.12268` 摘要 | `SOURCE_DOES_NOT_SUPPORT`（**CONFIRM A01 F-15**） | MED |
| P5.1b | Tran 作者含 Agnew | `14:327` | Crossref（3 作者） | `SOURCE_DOES_NOT_SUPPORT` | LOW |
| P5.2 | "5 of 6" + 24% | `10:112` | OpenAlex `10.1037/pspp0000166` 摘要重建 | `SOURCE_SUPPORTS_AS_STATED` | — |
| P5.2b | "缺 coordination" | `10:112` | 同上（摘要未点名第 6 维；VOR `NOT_OPENED`） | `UNVERIFIABLE_HERE` | MED |
| P5.2c | "242 个条目" | `10:112` | 同上（摘要无 N；单位错） | `SOURCE_DOES_NOT_SUPPORT` | MED |
| P5.3 | systemic > discrepancy + N | `10:443`,`10:447`,`10:449` | Crossref `10.1027/1016-9040/a000068` 摘要 | `SOURCE_SUPPORTS_AS_STATED`（N=443 **对**） | — |
| P5.3b | §4.8 标题"击败 discrepancy" | `10:443` | 同上 | `SOURCE_DOES_NOT_SUPPORT`（过强） | LOW |
| P5.3c | Bodenmann 题名含 "Satisfaction" | `A01:250` F-18 | Crossref（是 "Relationship **Quality**"） | `SOURCE_DOES_NOT_SUPPORT`（**A01 错，corpus 对**） | LOW（但会引入新错） |
| P5.4 | 女 `r = .26` vs `r = .25` | `02:146/152/270/320`,`03:65` vs `02b:421/461` | Semantic Scholar `10.1007/s10508-009-9556-9` 摘要 | `.26` = `SOURCE_SUPPORTS_AS_STATED`（`.25` 归 Chivers 被证伪）；Meston & Stanton 那条腿 `UNVERIFIABLE_HERE` | MED |

---

## `NOT_VERIFIED_AND_OUT_OF_SCOPE`（明确记录我**故意**没有核的，及原因）

**A. 因"不是 carrying source"而按 scope rule 排除**（不满足 (a)(b)(c) 任一条）：

1. **Joel et al. 2020 的 SI Appendix**（`pnas.1917036117.sapp.pdf`）—— PNAS 403，PMC 附件端点为 JS interstitial ⇒ `NOT_OPENED`。会定案的东西：P1.6 / P1.7 两条是否存在于 SI（我判断极不可能，因方法层无 folds）。
2. **Pusch et al. 2022 的 VOR 正文**（SAGE）—— green 副本无 PDF，TDM license-gated ⇒ `NOT_OPENED`。会定案 P3.2c（"too close" 那句在正文还是引言的 prior work 转述）。
3. **Gerpott et al. 2018 的 VOR 正文** —— green 副本无 PDF ⇒ `NOT_OPENED`。会定案 P5.2b（第 6 维究竟是不是 `coordination`）与 P5.2c（242 的单位）。
4. **Falconier et al. 2015 的摘要/正文** —— Crossref 未存 abstract，Elsevier TDM license-gated ⇒ `NOT_OPENED`。会定案 P5.3 的 `r = .45` / `17,856` / `72 samples` / by-partner>by-self。
5. **Schrodt et al. 2014 的 VOR 正文** —— `oa_status: closed`，无合法 OA ⇒ `NOT_OPENED`。会定案 P4.3c 的因果引文。
6. **Bodenmann & Arabin? 不在 scope** — 未打开。
7. **`S16` = Drigotas, Rusbult, Wieselquist & Whitton (1999)**（`06:1032`，`10.1037/0022-3514.77.2.293`）—— `06:646` 的 "4 项研究中 perceived partner **behavioral** affirmation…" 只在 `RGM` 的 `SUPPORTED` 行里（属 P3 家族），但**不是** `Ideal` schema 层建议的依据（那是 S31 + S17），且不由任何 kill criterion 独占 ⇒ **本轮未打开**。会定案：那句是否逐字、以及 "4 项研究" 的出处。
8. **`06:643` 的 Frost & Forrester 2013 / Frost et al. 2017 / Mashek & Sherman 2004** —— `RGM` 的支撑行，但**不是** schema 层建议的依据，且不独占任何 kill criterion ⇒ 未打开。
9. **`09` 的 `Anderson et al. (2010)`（MILS，N=706，5 条轨迹）** —— `19:208` 未把它挂到 `L5`；它支撑的是 `09` 内部的 discrete-belief-class 论证（`09:169`/`:528`/`:618`/`:705`），**不由任何 kill criterion 独占** ⇒ 未打开。（若 Architect 认为 `19` 的 "5 条轨迹" 链条构成对 `DVA` 的承载，须另开一个 P4 复核。）
10. **`Meston & Stanton (2018)`** —— 见 P5.4，只判了 Chivers 那条腿。
11. **`02:320` / `03:65` 的「20 项研究 r=.66 / .44」** —— Chivers 摘要只给合并值 `.66`；分层值 `UNVERIFIABLE_HERE`。
12. **Joel 2020 的「R17 N2」那条 SI-Appendix 变体的完整限定** —— 我核实了该句逐字存在及其 "in the SI Appendix analyses" 限定，但**未打开 SI** 去核 trust/intimacy/love/passion 在主分析中被移除的完整后果。
13. **A01/A04 的其余 40+ 条 correction** —— 不在 E3 scope（那些是 bookkeeping/citation 事项，不是"承载来源"）。**我唯一反向指出的是 P5.3c（A01 F-18 第三子项本身有错）。**
14. **`#20` / `#21` / `#22`** —— 按 dispatch 隔离，未读取、未执行、未引用。
15. **任何 Gate A/B/C 复跑、任何 transition law 实施、任何 restricted-data 下载、任何 Eye/Juece 变更** —— 全部未做。

**B. 我**没有**做的、且我认为本应有人做的**（不是"我核不了"，是"没人核"）：

16. **R06 `S31` 的书目身份** —— corpus 侧根本不存在，任何人都无法核实；这是需要**产出**而非**复核**的工作。
17. **S 编号的 lane-local 性** —— corpus 从未声明 `S19`/`S31`/`S36` 是 lane-local。这不是本次某个来源的缺陷，而是**贯穿全语料的编号制度缺陷**；我只在 P3.1 记录了它对我核查造成的具体后果，没有把它扩成一次全语料审计（那会违反"不要扩成另一次文献群"）。

---

## `open_questions_for_architect`

1. **`DVA` 的 null registry 依赖一个来源所不支持的前提。** P2.3 / P2.5：Lavner 系三篇研究**都报告了显著的负斜率**；S19 支持的是"起点条件化的斜率"，不是"斜率通道被击败"。**请裁决**：`B2_STABLE_LEVEL` 的 rationale 是否整体改写为"诊断基线，且必须与 `N8_LEVEL_CONDITIONAL_SLOPE` 成对"？这会同时改 `E1`、`E2`、`06`、`16`、`19`。
2. **`Ideal` 的 schema 层建议目前挂在一个无指针的 `S31` 上。** P3.1。**请裁决**：(a) 是否要求 R06 补出 `S31` 的书目身份后再解 `RGM` 的 HOLD；(b) 在此之前 `18:428`（N-17 `GENUINELY_DISTINCT`）是否降级为 `UNRESOLVED / S31_UNIDENTIFIED`。
3. **两条 `CITED_PRIMARY` 逐字引文在 Joel 2020 中不存在**（P1.6 的 folds、P1.7 的 ±10%）。**请裁决**：`R16-UC01` / `R16-UC02` / `R16-OC05` 的证据等级是统一降为 `AI recommendation` / `DESIGN_CHOICE`，还是允许 sibling 去重新寻找并实际打开来源？后者会超出"不扩成文献群"的边界，需要你显式授权。
4. **`A01` 的 F-18 第三子项本身是错的**（P5.3c：Bodenmann 2011 题名是 "Relationship **Quality**"，不是 "Relationship Satisfaction"）。**请裁决**：是否要我在你的记账里把这条记为"审计结论被实测推翻"的第二例（第一例是 `19:164`–`19:168` 记的 OSF 前缀那一例），并由 `r3/a1` 回退？
5. **`P4.2b` 的绝对命题**（"HMM 阶数不存在普适客观判据"）在 Pohle et al. 2017 摘要里**不存在**，而摘要反而 offer 了 pragmatic approach。**请裁决**：`09:759`（`K4`）的"撤退"触发条件是否必须改写？我倾向必须改写，否则一个 `K4` 撤退条件挂在一个未经核实的绝对命题上。
6. **Joel 2020 的"来源自有四条约束"（P1.5 #7）目前完全没有进入语料。** 其中第 3 条（"change is likely a function of external context, behavioral processes, or other factors that are themselves changing over time"）是来源**主动给出的、指向 `DVA`/`RT` 设计的正向线索**，且与 `E2` 的 hold 决策直接相关。**请裁决**：是否授权一个 follow-up child 把来源自有 framing（而非语料的失败 framing）写进 `06` / `19`？
7. **范围问题（我可能过度收缩了）**：dispatch 的 P1 把"initial-level differences discriminate trajectory groups better than rates of change"列在 Joel 名下。corpus 实际把它归给 S19（Lavner）。**请确认**我的路由判断（该主张属 P2，不属 P1）符合你的意图；若你认为语料另有一处把它归给 Joel，我需要知道位置。

---

*本报告只做复核。`docs/research/overnight-2026-09-27/` 下的既有文件**未被本 child 编辑**。所有依赖本报告结论的修复，由 `E1` / `E2` / `r3/a1` / `r3/a2` / `r3/a3a` / `r3/a3b` / `r3/a3c` / `r3/a3d` / `r3/a3e` / `r3/a3f` / `r3/a4` / `r3/a4b` 各自在自己拥有的文件上执行。*
