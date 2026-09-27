# 17 — Red Team / Falsifiers（独立红队证伪报告）

- **Lane**: R17（Wave 1，独立红队）
- **Date**: 2026-09-27
- **Role**: Research — Independent adversarial review / falsifier search
- **Status**: `RESEARCH_CANDIDATE` — 不得作为 canonical 修改依据
- **Independence**: 见 §0。本报告在形成任何结论前完成，未接触任何其他 lane 产出。

> **本报告的立场。** 这不是支持性评审。本报告的目标是**击穿** LHRM 当前架构假设。
> 但一份只攻击的红队报告是不合格的：§2 明确列出**六项攻击失败**并标 `NO_EVIDENCE_FOUND_FOR_CHALLENGE` / `UNCHALLENGED`，§7 给出最强的支持论证并对其做诚实评估。
> 全部结论按证据强度分级：`CITED_PRIMARY`（本次实际打开原文/摘要并抽取原句）/ `CITED_SECONDARY`（出版商或索引记录）/ `CITED_CLASSIC`（经 Crossref 核到卷期页，未读正文）/ `FETCH_FAILED`（检索失败，**不作论据**）。

---

## 0. INDEPENDENCE_STATEMENT

本 lane 在形成任何结论之前完成，未接触任何其他 lane 的产出。

**实际打开并读取的 `youling/lhrm` 文件（完整枚举）：**

1. `AGENTS.md`
2. `README.md`
3. `docs/foundation/CURRENT_ARCHITECTURE.md`
4. `docs/foundation/PARAMETER_CONVERGENCE_V0_1.md`
5. `docs/foundation/CONSTRUCT_SCOPE_DIRECTIONALITY.md`
6. `docs/validation/VALIDATION_CORPUS_V0_1.md`
7. `docs/validation/fixtures/FIXTURE_001_L0_001_CARTY_FACT_PACKAGE.md`
8. `docs/validation/fixtures/FIXTURE_002_L1_003_MAGI_PACKAGE.md`
9. `docs/validation/fixtures/FIXTURE_003_L1_001_STORYCORPS_PACKAGE.md`
10. `docs/research/overnight-2026-09-27/00_CHILD_CONTRACT.md`

**执行过的唯一仓库操作**：一次 `Get-ChildItem -LiteralPath "D:\coding\lhrm\docs" -Recurse -File`，仅用于定位 §6 要求的三个 fixture 路径；该命令只返回文件名，未读取内容。

**明确未读取：**

- `docs/research/overnight-2026-09-27/00_MANIFEST.md` —— mission 允许读，但**主动选择完全不读**，以避免 lane table 与任何跨 lane 提示。
- `docs/research/overnight-2026-09-27/01_*` … `19_*`、`A01_*` … `A04_*` —— 全部未读取、未列目录内容、未打开、未引用。
- `docs/foundation/PROJECT_HISTORY_2026-09-10.md`、`STAGE_SUMMARY_2026-09-07.md`、`RELATIONSHIP_EVALUATION_FOUNDATION.md`、`docs/ARCHITECT_BOOTSTRAP_REPORT.md`、`docs/ARCHITECT_RECONNAISSANCE_REPORT.md`、`docs/research/RESEARCH_REPORT_*`、`docs/RESEARCH_REPORT_*` —— 全部未读取。
- LHRM issue `#20` / `#21` / `#22` —— 未读、未引用、未执行。
- Eye / Juece / Juece#30 / PR#31 —— 未触碰。
- 未对 `D:\coding\lhrm` 做任何写入。

**独立性结论：无污染。**

---

## 1. 摘要：三个会改变项目走向的发现

红队找了 12 条攻击线。结果不是「项目错了」，而是**项目的承重墙放错了位置**。按影响排序：

1. **层边界被经验文献反向排序。** LHRM 把 `PPR` 判为 Belief 层、把 `Satisfaction` 判为 Derived 层。而 intensive-longitudinal 文献（Segal & Fraley 2016）明确报告：`PPR` 是**组织变量**，它解释了为什么 Investment Model 三个「理论独立」的分量会强烈协变；领域最大规模预注册研究（Joel et al. 2020, PNAS）报告的最强 predictor 是 **perceived partner commitment**——一个信念。**LHRM 把它降级了。** 这不是构念清单错，是**相空间选错**。

2. **Case Bank 目前不是测试。** 三个独立的机制共同保证它不会失败：(a) `PARAMETER_CONVERGENCE_V0_1.md` §13 的 10 个映射类里含三个 catch-all（`Environment` / `History` / `Derived-Narrative-only`）加自由文本 provenance，`MAPPING_FAILURE` 在类型上不可达；(b) `AGENTS.md` 的诊断清单包含 "or merely narrative/irrelevant"，任何失败都有合法出口；(c) §15 Gate B 的 11 类反例**就是项目自己的假设列表**，且 12 份语料对其中 5–6 类**没有 core-dyadic 材料**。再加上 §14 明说 Step 3 **只测命名不测数值**。**Gate A/B/C 目前测的是词汇量，不是 schema。**

3. **校准数据 100% 是恋爱 dyad，且唯一严格的形式理论是三人组的。** 恋爱构念在非恋爱场景**衰减但不崩塌**（这一点我要明确承认，见 §2 N4）——本体外推性没被证伪。但可用来估 LHRM 参数的纵向数据（Joel et al. 2020 的 43 个数据集）**全部是恋爱伴侣**；同时，Cartwright & Harary (1956) 的 signed-triad balance 是关于本项目所建模对象最严格的可证伪约束，而它**不能**由任何二人投影导出，LHRM 的 Case Bank 在结构上无法测试它。

---

## 2. 攻击失败的地方（`NO_EVIDENCE_FOUND_FOR_CHALLENGE` / `UNCHALLENGED`）

红队只攻击是不合格的。以下六项**没有找到真实反证**。

### N1 「没有任何理论预测一个 couple mutual state 的稳定均衡，而真实 couple 不表现出它」——这个攻击本身是错的

我系统性找过 attachment theory、Investment Model、Interdependence Theory、Structural Balance、Relational Turbulence、Risk Regulation：**全部不提出均衡存在性命题**。最接近的 structural balance 提出的是一组允许/禁止的符号构型，不是唯一吸引子，而且它是三人组命题。

**结论：LHRM 的转移假设没有被证伪，它只是被识别为 `unidentified`。** 这两者完全不同。把不可识别说成被证伪，是红队最常见的一种造假。我不能这么做。

### N2 「8 个构念不可分离」——攻击失败

找不到任何已发表的、同时测量 LHRM 这 8 个构念的因子分析（更别说跨关系类型）。最接近的 Rusbult, Martz & Agnew (1998) 对**另外 4 个**构念得到了干净的 4 因子；Joel et al. (2020) 的 SI 分析报告 "the predictors trust, intimacy, love, and passion generally performed quite well" —— 意思是在**预测上**可区分，而非被塌缩成一个因子。

**而且 LHRM 已经预先写下了针对这篇文献的正确回应**：`CURRENT_ARCHITECTURE.md` §7「低冗余不等于低动态耦合」，并明确引用了协变现象。Gate C 要打的冗余风险是真实的，但我**没有**证据表明它会找到冗余。

### N3 「Directionality 本身错了」——攻击打偏

Social Relations Model、Actor–Partner Interdependence Model、dyadic response surface 全部假设 actor 与 partner 是两个不同的**测量**；LHRM 明确引用 SRM（`CONSTRUCT_SCOPE_DIRECTIONALITY.md` §1）。设计不天真。

我真正的命中（Joel et al. 2020）是「partner report 在方差上没有增量」——那是关于**有用性**的陈述，不是关于**本体正确性**的陈述。**两个有向状态可以在本体上彼此独立而在方差上冗余。** 我不能把方差冗余升级成本体错误。

### N4 「恋爱构念在非恋爱 dyad 崩塌」——攻击失败

这是 mission 点名的攻击，我原本预期能打成。实际结果相反：

- Le & Agnew (2003) 报告 Investment Model 在 **relational 与 nonrelational 域都成立**，只是 relational 域显著更强；
- Branje et al. (2007) 直接把它搬到**青少年同性友谊**（"You are my best friend: Commitment and stability in adolescents' same-sex friendships"）；
- Sandberg et al. (2022) 在**无性恋**样本（N=485）里整套照用。

真实图景是**衰减 + 量表需按关系类型改造**，不是**崩塌**。标 `NO_EVIDENCE_FOUND_FOR_CHALLENGE`。
（攻击的落点被**转移**了：不是本体过拟合恋爱，而是**校准数据 100% 恋爱**——见 §3 F6。）

### N5 「Liking 与 RomanticAttraction 不可解耦」——攻击失败

Sternberg (1987) *Liking versus romantic: A comparative evaluation of theories* 这篇论文的**存在本身**就是它们可分离的证据。找不到它们塌缩的证据。

### N6 「Reality ≠ Observation ≠ Belief 的分离是错的」——部分失败，失败的是优先序

这个区分**必要且可实现**，三个 fixture 自己证明了：Fixture 001 的 C013/C025（法庭明确无法判定业务是否真的被出售）与 C016（"appears to have been sent"）强制要求一个**法律上权威的不可知**；Fixture 002 的 K1–K4 强制要求 Jim 在 M042 之前不知道卖头发。

**失败的是优先序**：LHRM 把 Belief 当成 state 的下游，实证说 Belief 常常是**因果最近端**（§3 F3）。**区分必须活下来；排序必须改。**

---

## 3. 逐条证伪卡

---

### F1 — `MAPPING_FAILURE` 在设计上不可达

**主张。** `PARAMETER_CONVERGENCE_V0_1.md` §13 定义 10 个映射类。第 7 类 `Environment`、第 8 类 `History/Timeline`、第 9 类 `Provenance/Uncertainty`、第 10 类 `Derived/Narrative-only`，加上 `ProvenanceAndUncertainty` 容器内的自由文本，构成**三个 catch-all + 一个自由文本槽**。`AGENTS.md` 的诊断清单再补一个出口 "or merely narrative/irrelevant"。

**因此：对任何输入字符串，一个有能力的 mapper 都能找到合法落点。`MAPPING_FAILURE` 在类型上被排除。**

**引用的方法论后果。**

- Lakatos, I. (1970), *Criticism and the Growth of Knowledge*, pp. 91–196：研究纲领若能吸收一切可能反驳（protective belt 无限扩张），它就在做**退化的 problemshift**。`CITED_CLASSIC`
- Ribeiro, M. T., Wu, T., Guestrin, C., & Singh, S. (2020), *ACL*, 4902–4912, DOI `10.18653/v1/2020.acl-main.442` (CheckList)：聚合准确率无法区分模型能力；能力测试给出显著更低的分数。**即「高覆盖率」与「高能力」在方法论上被明确解耦。** `CITED_CLASSIC`

**破坏的假设。** 「Case Bank 是 schema 的验证工具」（`CURRENT_ARCHITECTURE.md` §10；`AGENTS.md` Validation discipline）。

**可以定案的具体观察。** 删除 `Derived/Narrative-only` / `IRRELEVANT` / 自由文本 provenance 三个出口后，对 Fixture 001 的 C001–C026 重跑三 Verifier。若仍无一次 `MAPPING_FAILURE`，则该出口是唯一失败通道，须永久删除。

---

### F2 — 领域内最大规模预注册协作研究的五条结论

**引用。** Joel, S., Eastwick, P. W., Allison, C. J., Arriaga, X. B., … (2020). *PNAS* 117(32), 19061–19071. DOI `10.1073/pnas.1917036117`。**86 位研究者 / 29 个实验室 / 43 个纵向数据集 / 11,196 对伴侣 / 2,413 个测量。** `CITED_PRIMARY`（读了 abstract + 正文段落，四个镜像一致）

| # | 原文 | 破坏什么 |
|---|---|---|
| 1 | "the top relationship-specific predictors of relationship quality were **perceived partner commitment, appreciation, sexual satisfaction, perceived partner satisfaction, and conflict**" | **basis 瞄错目标**（见下方映射表） |
| 2 | "**Actor-reported variables ... predicted two to four times more variance than partner-reported variables** ... individual differences and partner reports had **no predictive effects beyond actor-reported relationship-specific variables alone**" | 「两个独立有向状态」在**方差上**冗余 |
| 3 | "**relationship-quality change ... was largely unpredictable from any combination of self-report variables.**"（正文："No analyses accounted for more than **5% of the variance**"） | 工程顺序第 6 步（`Longitudinal parameter estimation`）与 `X(t+1)=F(...)` |
| 4 | "**Relatively objective relationship variables (e.g., cohabiting status, dating versus married relationship status, having children) generally mattered little**, with the exception of relationship length" | P4 `Relationship Identity/Agreement` 与 P5 `Boundary/Exclusivity Rules` 作为**质量预测因子**的一等地位 |
| 5 | "relationship-specific variables predicted up to 45% of variance at baseline, and **up to 18%** ... at the end of each study" | 上限很低 |

**结论 1 的层映射（我已完成的计数）：**

| PNAS top-5 | LHRM 里的位置 | 在 `DirectedRelationshipState` 内？ |
|---|---|---|
| perceived partner commitment | `Belief_i(Dedication_(j->i))` | ❌ **Belief 层** |
| appreciation | 对关系的评价/情感，无对应有向构念 | ❌ |
| sexual satisfaction | Derived，且 relational 非 directional | ❌ |
| perceived partner satisfaction | 二阶信念 | ❌ |
| conflict | Action/Event 频率 | ❌ |

**5 个里 5 个落在 `DirectedRelationshipState` 之外。** 我在 packet 初稿写 4/5，**复核后更正为 5/5**（appreciation 也不在 8 构念任何一项内；`SexualDesire` 是方向性欲望，不是 sexual satisfaction）。

**诚实限定（结论 4）。** 「几乎不预测关系质量」不等于「无作用」。P4/P5 可能仍对**机会集、退出成本、契约约束**有强约束力，那不是满意度回归能测到的。我不断言 P4/P5 无用，只断言**它们作为质量预测因子的一等地位没有证据支撑，而项目自己的论证方式把它当成显然的**。

**可以定案的具体观察。** 把 PNAS top-5 与 Zoppolat et al. (2023) 的 IL predictor 集合逐条标注到 LHRM 层表，统计落在 `DirectedRelationshipState` 外的比例。**已做完：5/5。**

---

### F3 — 「Belief 是 state 的下游」被实证反向排序（头号可执行建议）

**三条独立来源，同一结论：**

**(a)** Segal, N., & Fraley, R. C. (2016), *J. Social & Personal Relationships* 33(5), 581–599, DOI `10.1177/0265407515584493`。`CITED_PRIMARY`

> "Despite the theoretical distinctions among these components, studies consistently find that satisfaction, investment, and quality of alternatives tend to covary. ... Thus, one challenge is to explain why these components covary so strongly, despite their theoretical independence."

> "we propose that **perceived partner responsiveness (PPR) ... serves as an organizing variable** that drives, in part, the covariation among investment model constructs."

> "Our findings demonstrated that ... people who perceived their partner as being more responsive were **more satisfied** in their relationships, **more invested**, and perceived alternatives ... as being **lower in quality**."

**(b)** Laurenceau, J.-P., Barrett, L. F., & Pietromonaco, P. R. (1998), *JPSP* 74(5), 1238–1251, DOI `10.1037/0022-3514.74.5.1238` — intimacy 是**人际过程**；PPR 是核心 dyadic 变量。`CITED_PRIMARY`（题名出处经 Crossref 核实，摘要经 (a) 引文间接核实）

**(c)** Joel et al. (2020) — 最强 predictor 是 **perceived** partner commitment（信念，不是事实）。

**破坏的假设。** `PARAMETER_CONVERGENCE_V0_1.md` §5 B1 把 `PPR` 判为 `layer = Belief / relationship-specific perception`；§9 R3 把 `Satisfaction` 判为 `DERIVED / evaluation-state candidate`。

**为什么这比「8 个构念选错」更致命。** basis 是 8 个有向构念，但**层边界**决定了什么算「关系状态」。如果最强的组织变量住在 Belief 层、最强 readout 住在 Derived 层，那么 8 个有向坐标就是**在一个错误的相空间里**。**构造错了，不是清单错了。**

**可以定案的具体观察。** 把 `PPR_i` 从 Belief 层提升为 state 层并允许 `Belief_i(PPR_j)`；重跑 Segal & Fraley 的 IL 构念级模型，看 `PPR` 是否能吸收 satisfaction/investment/alternatives 的协变。能 → F3 成立；不能 → F3 被推翻。

---

### F4 — 复合态（conjunctive mode）无法由「每构念一个坐标」表达

**(a)** MacDonald, G., Locke, K. D., Spielmann, S. S., & Joel, S. (2013), *J. Social & Personal Relationships* 30(5), 647–661, DOI `10.1177/0265407512465221`, N=1004。`CITED_PRIMARY`

> "evidence for relational ambivalence was found for both anxious and avoidant attachment. **Individuals high in anxious attachment reported relatively similar and intense threat and reward perceptions**, whereas individuals high in avoidant attachment showed evidence for **similar, but not intense**, threat and reward perceptions."

> "the weighing of prospects for rejection and intimacy in romantic relationships **arguably leads to what researchers traditionally think of as ambivalence**"

**(b)** Zoppolat, G., Faure, R., Schneider, I. K., & Righetti, F. (2023), Systematic Study of Ambivalence in Romantic Relationships。4 个 intensive longitudinal 研究，N=1136。`CITED_SECONDARY`

> "we find that ambivalence is related to worse personal and relational well-being, but this association is only significant for **explicit (i.e., objective and subjective) types of ambivalence, with subjective ambivalence playing the strongest role, particularly for relationship outcomes**."

论文明确区分四种类型：**objective / subjective / explicit-implicit / implicit**。

**破坏的假设。** `Candidate Minimal Directed Basis v0.1` 是 8 个命名标量（§11）；`StateCoordinate` 是 `estimate_or_region + uncertainty + evidence + provenance + observation_time`（§14）。这个结构能表达「Liking 不确定」，但**不能**表达：

- 「我同时感到强烈靠近与强烈排斥，且我现在体验到的是这个共存本身」——这不是区间，是**模态**；
- 更要命的是 (b)：**objective 与 subjective ambivalence 是解离的，subjective 才是最强预测因子**。真正有关系后果的那个变量是**主体对自己的一个报告**，而它与关系的客观构型**不一致**。

**可以定案的具体观察。** 构造一组 `Z` 完全相同但 subjective 报告相反的 dyad 配对。若 `Z` 无法区分而两组下游行为确实不同（S6 已给方向），则状态空间必须增加**模态/析取**层，`Z[k,i,j,t]` 降级为**边缘分布**。

---

### F5 — pair-level 状态确有不可由两个方向投影还原的证据

**5a. 真实数据里的一致性项。**
Mund, M., & Johnson, M. D. (2020), *Journal of Happiness Studies* 22(2), 575–597, DOI `10.1007/s10902-020-00241-9`。German Family Panel，**2,337 对稳定伴侣，8 年，APIM + dyadic response surface analysis**。`CITED_PRIMARY`

> "we found that loneliness evinced substantial negative actor and partner effects on relationship satisfaction and its development over 8 years. Furthermore, ... women were most satisfied with their relationships when **both partners scored low on loneliness**, whereas men were most satisfied when their own loneliness was low, irrespective of their partners' loneliness. **Congruently low levels of loneliness between women and men** as well as declines in loneliness of at least one partner were additionally associated with increases in relationship satisfaction over time."

即：**一致性项在 actor 与 partner 主效应之外携带额外方差。**

**诚实限定 → `CONTESTED` 而非 `CHALLENGED`。** LHRM 的 `Asymmetry_k(A,B) = distance(Z[k,A,B], Z[k,B,A])` 可以算这个差分。但注意方向：这份证据说**差分是一阶预测因子**，而 LHRM 把它当**派生 readout**。从 readout 升为一等坐标不是小改动。

**5b. 唯一严格的形式理论是三人组的，而语料在结构上无法测。**
Cartwright, D., & Harary, F. (1956), *Psychological Review* 63(4), 277–293, DOI `10.1037/h0046049`。`CITED_CLASSIC`（Crossref 核到卷期页）

signed triad 的 balanced 构型恰好是「全正」或「恰好一正」。这是关于**三人联合有向状态**的严格可证伪约束，**不能**由任何二人投影导出。

**对 LHRM 的直接后果。** `VALIDATION_CORPUS_V0_1.md` 的 12 份材料里只有 L2-001（Sharland，3 个孩子）与 L2-002（Harriet Mill，John Taylor / JSM / 孩子）含第三方，且都是**单一个案、没有符号边枚举**。**Case Bank 在结构上无法测试它所建模对象的最严格形式理论。**

**诚实限定。** 我**没有**核实这个理论自身的经验记录（one-mode vs two-mode 之争需 Balan 1968，`FETCH_FAILED`）。**我不断言 structural balance 成立；我断言的是：它是唯一的候选，而项目没有能力检验它。**

---

### F6 — 纵向：轨迹可能不是关系在动，是人在离开

**6a. 一手存活偏误陈述（顶配人口学论文自己写的）。**
Musick, K., & Bumpass, L. L. (2006)。全文 PDF: `https://ccpr.ucla.edu/wp-content/uploads/2024/04/Re-Examining-the-Case-for-Marriage_-Variation-and-Change-in-Well-Being-and-Relationships.pdf`。`CITED_PRIMARY`

> "we focus (by necessity) on unions still intact at NSFH2, thereby excluding many short-term unions formed between waves. ... However, **selecting on the more resilient relationships should lead to a sample that is more heavily weighted over time toward greater well-being and couple relationship quality. We find the opposite is true: married and cohabiting couples report better outcomes in shorter relationships.**"

这是**由第一方作者写下的**存活偏误警告。LHRM 的 `Gamma_(A,B) = {X_(A,B)(tau)}` 把轨迹当设计前提，从未处理过这个。

**6b. 同一个论文顺手证伪了一个第三方网络命题。**
同上，原文：

> "forming a coresidential relationship **reduces** interactions with others, as partners spend time together that previously would have gone elsewhere. ... **these findings do not support, however, arguments in the literature that marriage expands social circles**, and does so to a greater extent than cohabitation."

`CURRENT_ARCHITECTURE.md` §2 写「向外看 context，但 Human Dyad 仍是最小关系查询单元」，隐含 network 是外生背景。**这个前提被证伪了：同居/婚姻会主动收缩社会世界。** network 是**内生且被关系反向塑造的**，不是可加的外部修正。

**6c. 选择效应是被实证确认过的。**
Stutzer, A., & Frey, B. S. (2006), *Journal of Socio-Economics* 35(2), 326–347。全文 `https://docs.iza.org/dp1811.pdf`。`CITED_PRIMARY`

> "**we find evidence that happier singles opt more likely for marriage** ... **most of the extra benefits in reported well-being are experienced during the first few years of marriage.**"

**6d. 但这是活的争论，我不断言任何一方。**

- Lucas, R. E., & Clark, A. (2006), *J. Happiness Studies* 7(4), 405–426: "individuals do not get a lasting boost in life satisfaction following marriage"。`CITED_SECONDARY`
- Stutzer, Fremy-Fragoni & RTS/OFS (2006, PAA) 逐条反驳: "we do not find that adaptation to marriage is quick and complete; rather, we find **an enduring effect** of marriage comparable in magnitude to the effect of cohabitation." `https://paa2006.populationassociation.org/papers/60777`。`CITED_PRIMARY`
- Gattig, A., & Minkus, L. (2021): POLS 系数约为 FE 估计的 3 倍；FEIS 与 FE 无显著差异（Hausman p = 0.92）。`CITED_SECONDARY`

**诚实的表述**：适应速度文献仍在吵。我主张的更弱但更稳的一点：**任何用观测轨迹估 F 的方法都不区分 (i) 关系变化 (ii) 谁留下 (iii) 谁进入。** 而 LHRM 的 Case Bank 是**文档**不是 **panel**，所以它**永远检测不到**这个混淆——这是设计层面的不可修复。

**6e. 「变化不可预测」是对 F 的直接打击。** 见 F2 结论 3。

---

### F7 — 验证工具对其目标现象的一部分在原理上盲

**引用。** Eastwick, P. W., Eagly, A. H., Finkel, E. J., & Johnson, S. E. (2011), *JPSP* 101(5), 993–1011, DOI `10.1037/a0024061`。`CITED_PRIMARY`（读了 abstract + 讨论段）

> "these implicit measures were **not redundant with a traditional explicit measure: The correlation between these constructs was .00 on average**, and the implicit measures revealed no reliable sex differences, unlike the explicit measure."

> "explicit and implicit measures exhibited a **double dissociation** in predictive validity. Specifically, explicit preferences predicted the extent to which attractiveness was associated with participants' romantic interest in **opposite-sex photographs but not** their romantic interest in **real-life opposite-sex speed-daters or confederates**. Implicit preferences showed the **opposite** pattern."

**推理。** LHRM 的全部验证工具是**文本逐句映射**。文本是显式报告/叙述。S2 证明显式与隐式测量**正交（r = .00）且预测力双重分离**。因此：

> **一个基于文本的 benchmark 可以取得 100% 映射覆盖率，同时与真正驱动现场吸引行为的层完全无关。**

**因此 `representation completeness` 的成功绝不可被读作 ecological validity。** 当前文档没有收紧这个结论边界。

**可以定案的具体观察。** 取 S2 语料（照片判断 vs 现场 speed-dating）构造 LHRM fixture。若 LHRM 对两个任务给出相同映射，则盲区存在。

---

### F8 — Scope invariance：模型族已记录在案会随关系类型/人口漂移

| 来源 | 原文 | 类型 |
|---|---|---|
| Le & Agnew (2003), *PR* 10(1), 37–57, DOI `10.1111/1475-6811.00035` | "Support for the model was obtained in predicting commitment in both **relational** ... and **nonrelational** domains ..., but was **significantly stronger in relational domains**." ／ "the associations ... **vary minimally** as a function of demographic (e.g., ethnicity) or relational (e.g., duration) factors." | `CITED_PRIMARY`(abstract) |
| Brooks, Ogolsky & Monk (2019), *J. Family Issues* 39(9), 2685–2708, DOI `10.1177/0192513X18758343` | "an interdependent version of the Investment Model (APIM) **fit intraracial relationships better than interracial relationships**. ... **Investments were associated with concurrent commitment in intraracial but not interracial relationships.**" | `CITED_PRIMARY`(abstract) |
| Branje et al. (2007), *PR* 14(4), 587–603, DOI `10.1111/j.1475-6811.2007.00173.x` | 题名即 "Commitment and stability in **adolescents' same-sex friendships**" —— 同一模型被**重新奠基**到完全不同的关系类型 | `CITED_PRIMARY`(元数据) |
| Sandberg et al. (2022), *Front. Psychol.*, DOI `10.3389/fpsyg.2022.912978` | "The Investment Model is robust and wide-reaching for characterizing **different types of relationships** ... **although occasional adjustments to the measures are made (e.g., alternatives may not be measured among those in non-monogamous relationships)**." | `CITED_PRIMARY` |
| Tran, Judge & Kashima (2019), *PR* 26(1), 158–180, DOI `10.1111/pere.12268` | 50,427 participants / 202 samples，**发现多个显著 moderator** | `CITED_PRIMARY`(abstract) |
| Vandenberg & Lance (2000), *ORM* 3(1), 4–70, DOI `10.1177/109442810031002` | 跨样本比较的前提是**测量的**不变性 | `CITED_CLASSIC` |

**破坏的假设。** `PARAMETER_CONVERGENCE_V0_1.md` §2.4 **Scope stability** 作为构念准入判据。

**关键观察。** LHRM 唯一指名道姓的构念来源（Rusbult/Investment Model，§4 D7 引用）**恰恰是「跨关系类型需改测量」记录最多的一族**。这不是别人的理论坏了，是**该理论自己反复报告的边界条件**。LHRM 把一个已知需 relation-type-scoped 化的构念（`Dedication`）当作 universal basis 元素。

**诚实限定。** 我**没有**找到「这 8 个构念在 2 种以上关系类型下 invariance 失败」的**直接**实证——那需要 LHRM 自己的 instrument，而 LHRM 没有 instrument。所以这是对**判据可执行性**的 `CHALLENGED`，不是对**判据为假**的 `CHALLENGED`。

---

### F9 — 语料库在结构上无法执行 Gate B（Case Bank 可证伪性攻击）

`PARAMETER_CONVERGENCE_V0_1.md` §15 **Gate B** 要求至少测试 11 类。逐份核对 `VALIDATION_CORPUS_V0_1.md` 的 12 份材料与三个 fixture：

| Gate B 类型 | 语料现状 | 可否测试 |
|---|---|---|
| romance | L1-001 / L1-002 / L1-003 / L2-001 / L3-001 / L3-002 / L3-003 | 可（**7/12 是恋爱**） |
| unilateral attraction | L1-003、L2-003 | 可 |
| high-attraction/low-trust | L3-001 | 可 |
| conflict | L2-003、L3-001 | 部分 |
| **same-sex** | **无任何一份以同性 dyad 为 core dyad** | **不可** |
| **kin** | L1-002 / L2-001 / L2-002 中孩子均为第三方 | **不可** |
| **friendship（纯友谊）** | L1-001 / L1-002 / L1-003 全是**婚姻**；L2-002 是智力伙伴转恋爱 | **基本不可** |
| **caregiving** | L0-002 是照护机构**合同**争议（照护对象已故）；L0-003 是医患 | **不可** |
| **work colleague** | L0-001 是 claimant↔line manager（**等级**关系） | 部分 |
| **high-dependence/low-liking** | 无 | **不可** |

**四个叠加的结构问题：**

1. **语料无法执行 Gate B 要求的 11 类中的 5–6 类。**
2. **反例集 = 项目自己的假设列表。** Gate B 的 11 类全部是 LHRM 自己候选构念的组合形态。语料由项目作者预先挑选，标准就是「能体现我们已声明的候选」。**Gate B 在构造上不可能让项目意外。** 它是确认偏误装置，不是对抗测试。
3. **Fixture 独立性不对称（文档可证）。** `FIXTURE_001` 头部：「准备者：LHRM Project Architect」；`FIXTURE_002`：「**本包由 Architect 仅做材料清洗与冻结**」；`FIXTURE_003`：「准备者：LHRM Research」。三 Verifier 是盲的，但**输入与 ontology 有共同作者**，且 2/3 fixture 由 schema 作者在**知道 schema 能表达什么**的情况下做清洗决策。冻结是机械的，这不是造假，但**必须披露**，且应改为对 schema 不可见的一方清洗。
4. **最具判别力的测试被显式解除武装。** `VALIDATION_CORPUS_V0_1.md` 对 L1-003 写："future_leakage_risk: HIGH ... **do NOT test ending prediction**"。唯一能测「mapper 是否越权使用文本未授权信息」的设计被关闭。剩下的只有逐字回忆 + 信念追踪。

**5. 法院「事实认定」是相关性预过滤后的语料。** L0-001 / L0-002 / L2-001 都是判决文书。判决 "Findings of Fact" 的**定义**就是「与法律争点有实质相关且被采纳的命题」。**这是一次与表示能力正交的过滤。** 因此在这些材料上测出的映射覆盖率**必然偏高**，其偏高程度不是 ontology 质量的函数。

**可以定案的具体观察（成本极低）。** 发布 12 份材料 × Gate B 11 类的覆盖矩阵。任一必需类型覆盖为 0 → Gate B 标 `NOT_EXECUTABLE`，在**语料层**解决，不在 ontology 层解决。

---

### F10 — 项目自身词汇导入的民间理论陷阱（术语级）

**T1（内部不一致，最锐）：`Dedication` 既是 primitive，又在源理论里是函数。**
§4 D7 把 `Dedication` 列为 KEEP，并说「Investment Model 明确提醒 commitment 不能与 investment、constraints、alternatives、satisfaction 混为一体」。但 Investment Model 的**定义式**恰恰是 Dedication 由那三者决定（S15, Rusbult/Martz/Agnew 1998 是其量表来源）。LHRM 对 `Power` 做了派生处理（§9 R2，从 `OutcomeDependence` 派生），却对一个**源理论明确用方程定义**的构念保留 primitive。**同一份文件里两种处理。** 这不是哲学分歧，是记账不一致。

**T2（有实证支撑）：`AttachmentSecurity` 把一个非加性个体差异塞进了 basis。**
Joel et al. (2020) 报告：attachment anxiety 与 avoidance 是 top-5 的**个体差异**预测因子，而 "individual differences ... **did not predict relationship quality above relationship-specific predictors alone**"。因此 `AttachmentSecurity_(i->j)` 至少混合了 (a) 一个被证明**不具增量**的个体差异成分，与 (b) 一个 dyad 特异残差。而 `AGENTS.md` 明确说「Person property → AgentState/Attribute, not automatically → DirectedRelationshipState」，§7 Agent 层列表里**已经有** `attachment tendency`。**D5 与 Agent 层存在项目自己警惕的那类重复计数。**

**T3（弱）：`Trust` 单坐标。** S15 报告 Investment Model 变量与 "trust level" 是 "moderately associated" —— trust 在该语料里是**相关物**而非正交基元素。权重低。（Mayer et al. 1995 / Rempel et al. 1985 的多维分解我**未核实**，标 `AGENT_RECALL`，不承重。）

**T4（无证据）：`OutcomeDependence`。** 找不到直接反证。标 `NO_EVIDENCE_FOUND_FOR_CHALLENGE`。项目自己已开 Open question（§4 D8），**这是诚实的**，应予肯定。

**T5（设计异味）：** `CONSTRUCT_SCOPE_DIRECTIONALITY.md` §1 写 `Construct(i->j,t) = population baseline + source_i + target_j + directed_dyad_(i->j) + residual`。把 `source_i + target_j`（跨时间常数 / trait）放进**时间索引的状态**里，等于**静默导入一个横截面特质模型**到动态状态模型。这与 `State != Action` 是同类问题的另一个版本：**跨层污染**。

**T6（正面，必须说）。** §12 拒绝把「爱」「亲密」「嫉妒」「控制欲」「忠诚」「化学反应」当 primitive，这是**真实且正确**的。攻击在这里**失败**。

---

### F11 — Step 3 在结构上无法失败

**纯内部，可从文档直接证明。**

- `CURRENT_ARCHITECTURE.md` §12：Step 3 = `Representation coverage regression`。
- `PARAMETER_CONVERGENCE_V0_1.md` §14：「因此第一轮 Case Bank test **只要求语义有合法落点**，不要求每句话产生精确数值变化。」
- §14 示范：「"A 深情地看了一眼 B" 优先表示为 `Action: Gaze_(A->B)` / `Narrative/Observation` / `EvidenceFor: Liking / RomanticAttraction, uncertain`」，而**不是** `Liking += 1`。

**推理。** Step 3 只测**命名**，不测**状态**。Measurement & Canonicalization 是 Step 4。所以 Step 3 的失败模式只有「没有词可用」。而 §4/§5/§6/§7/§8/§9/§10/§12 已提供 Agent / Directed / Pair / Belief / Constraint / Environment / History / Action / Derived 十个有名字的抽屉，加上 §12 的六个被拒词。**这是一台词汇充足、判定宽松、且失败出口被设计为「叙事性/无关」的分类器。**

**与 F1 的区别。** F1 说失败出口被堵死；F11 说**即使不堵死，Step 3 也不测 state**。两条独立。

---

## 4. 逐假设裁定表

| # | 架构假设（出处） | 裁定 | 关键证据 |
|---|---|---|---|
| A1 | 8 个有向构念相互可分离、低语义冗余（§11, §2.1–2.2） | **CONTESTED** | S3（协变但理论独立）；S1（trust/intimacy/love/passion 在预测上可区分）。无分离性失败证据 |
| A2 | `Z[k,i,j,t]` 两方向独立、mutuality/asymmetry 可派生 | **CHALLENGED** | S1（partner report 零增量）；S11（一致性项在主效应外携带方差） |
| A3 | 关系是二人局部投影，third party 是外生背景（§2, §3） | **CHALLENGED** | S7 直接证伪「marriage expands social circles」；S20（唯一严格形式理论是三人组的） |
| A4 | 转移可由 `X(t+1)=F(...)` 演算（§6） | **CHALLENGED** | S1（变化 <5% 方差）；S7/S8/S9/S10/S29（存活 + 选择 + 活的适应之争） |
| A5 | Belief 层是 state 的下游（§5 B1） | **CHALLENGED** | S3 + S4 + S1。**承重错误** |
| A6 | `MAPPING_FAILURE` 可达；Case Bank 有诊断力（§13, §15） | **CHALLENGED（推翻）** | F1 + F9 + F11 |
| A7 | 构念语义跨关系类型/人口稳定（§2.4） | **CHALLENGED**（判据可执行性） | S12 / S14 / S16 / S17 / S18 |
| A8 | 恋爱构念可外推到全部 Human–Human dyad | **CONTESTED** | N4：本体攻击失败；但 S1 的 43 数据集全为恋爱伴侣 |
| A9 | 复合/矛盾态可由每构念一坐标表达（§11, §14） | **CHALLENGED** | S5（N=1004）+ S6（N=1136，subjective 最强且与 objective 解离） |
| A10 | `State != Action`（§6, SCOPE §5） | **UNCHALLENGED** | Hui et al. (2014, Manhattan Effect) 反而**支持**此规则。攻击失败 |
| A11 | 拒绝把「爱/亲密/嫉妒/忠诚」当 primitive（§12） | **UNCHALLENGED** | 无反证。攻击失败 |
| A12 | Unknown 必须显式，不得静默补 neutral（AGENTS.md） | **UNCHALLENGED** | Fixture 001 C013/C016/C025、Fixture 002 K1–K4 强制要求且通过 |
| A13 | 文本映射可验证状态表示（隐含于 Case Bank） | **CHALLENGED** | S2：隐式 vs 显式 r = .00 + 预测力双重分离 |
| A14 | `Reality ≠ Observation ≠ Belief` 分离 | **CONTESTED**（区分存活，排序被推翻） | N6 |
| A15 | `Dedication` 作为 universal basis 元素（§4 D7） | **CONTESTED** | T1（源理论用方程定义）+ S14（investment 跨种族不预测） |
| A16 | `AttachmentSecurity_(i->j)` 作为定向坐标（§4 D5） | **CHALLENGED** | S1：anxiety/avoidance 是个体差异且在 actor 关系变量之上无增量 |
| A17 | `Trust` 单坐标（§4 D4） | **CONTESTED**（弱） | S15 |
| A18 | `OutcomeDependence` 可完全导出（§4 D8） | **NO_EVIDENCE_FOUND_FOR_CHALLENGE** | 无反证。项目自标 open question，诚实 |
| A19 | `Liking` vs `RomanticAttraction` 可解耦（Gate C 头号对象） | **NO_EVIDENCE_FOUND_FOR_CHALLENGE** | N5：Sternberg (1987) 存在本身即分离证据 |
| A20 | `PPR` 在 Belief 层（§5 B1） | **CHALLENGED** | F3。**头号可执行建议** |
| A21 | `Satisfaction` 为 Derived（§9 R3） | **CHALLENGED** | S1：satisfaction 是该领域唯一纵向验证的 DV，是外部效度锚点 |
| A22 | Fixture 输入由与 ontology 无关的一方准备 | **CHALLENGED**（流程） | Fixture 001/002 header 明示 Architect 准备 |
| A23 | 加性分解 `baseline + source_i + target_j + edge + residual`（SCOPE §1） | **CONTESTED** | T5：跨时间常数静默进入时间索引状态 |

---

## 5. 什么结果会要求架构退守（具体到放弃什么）

### R1 — 移除 catch-all 后仍无一次 `MAPPING_FAILURE`
**放弃：Case Bank 作为「representation completeness」gate 的资格。** `CURRENT_ARCHITECTURE.md` §10 与 `AGENTS.md` 中「Case Bank 首要测试 completeness」的表述必须撤回，改为「Case Bank 测试固定词汇表的覆盖率」。`§15 Gate A` 须重写为固定词汇 cloze/probe 测试 + 预注册负结果。

### R2 — 层审计确认 ≥4/5 的稳健 predictor 落在 `DirectedRelationshipState` 之外
**放弃：`Belief < DirectedRelationshipState < Derived` 的层排序本身。** 具体：`PPR` 与 `Satisfaction` 升为一等状态层；`Belief_i(X)` 与 `X` 的类型关系需重新设计（存在循环风险，见 U6）。**这是最可能发生的一条退守。**
**明确不建议**：不要因此重选 8 个构念。那会把一个层错误伪装成清单错误，并损失 §4 已做对的 semantic independence 工作。

### R3 — 任一构念在 ≥2 种关系类型下 invariance 失败
**放弃：「构念名跨关系类型携带稳定语义」这一假设。** 正确做法是把同名的构念按 relation type **拆分**（`Liking|kin` / `Liking|romance` / `Liking|work` 是不同构念）。**这是重大退守**，因为它摧毁跨域可比性，而跨域可比性很可能是项目唯一的比较性主张。

### R4 — 复合态无法用 lattice/interval 表达
**放弃：`Z[k,i,j,t]` 作为坐标（coordinate）。** 状态必须是 `(构念, 方向, 区间) 的集合 + 联合模态标记`，`Z` 降级为**边缘分布/投影**。这会连带改变 §11、§14 与 Case Bank 的 verdict 词表。

### R5 — 任何一份语料在移除 `IRRELEVANT`/`NARRATIVE_ONLY` 出口后仍产不出失败
**放弃：Case Bank 作为任何形式的 gate。** 降级为语料库 + 人工参考标注，不再承担 schema 判决功能。

### R6 — 无法说出任何一条「本 schema 会预测、而领域现有 instrument 不会预测」的命题
**放弃：科学模型的自我主张。** 重构为工程/知识表示产物（受控词表 + provenance 标准 + 知识时间线规范），并明确写下「不主张科学解释力」。**这是「整个项目不值得做」论证唯一真正成立的形态**（见 §8 论点 5）。

---

## 6. 最承重的未测假设（按「若为假则项目地基动摇」排序）

1. **8 个坐标逐项可分离，且这 8 个是对的 basis。** 从未被测。§15 Gate C 是计划，不是结果。
2. **Belief 在认识论上位于 state 下游。** 现已被 Joel et al. (2020) + Segal & Fraley (2016) 反向排序。
3. **文本映射 benchmark 可以验证状态表示。** 被 Eastwick et al. (2011) 的 r = .00 部分推翻。
4. **`MAPPING_FAILURE` 可达。** 被 schema 自身的 catch-all 推翻。
5. **构念名跨关系类型携带稳定语义。** 被 Investment Model 家族反复记录的作用域漂移所 contest。
6. **有向状态是**信息性的**，不只是本体上可区分的。** 被 Joel et al. (2020) 的 partner-report null 所 challenge。
7. **Satisfaction 是 readout 而非 state。** 未测；且它是领域唯一的外部效度锚点。若降级为 Derived，LHRM 就降级了唯一的 ground truth。
8. **二人是合适的最小单元。** 未测；structural balance 是三人组的；Musick & Bumpass 证明关系会主动收缩社会世界。
9. **`F` 在混合状态空间上可估。** 未测；领域结果是 1–2 年尺度上 <5%。
10. **法律/官方文档是关系状态的合法代理。** 未测；且判决事实认定是**相关性预过滤**产物，语料被预过滤在与表示能力正交的维度上。
11. **恋爱来源构念可外推到全部 Human–Human dyad。** 未测；校准数据 100% 恋爱。

---

## 7. 什么会让我改变看法（falsify LHRM **不是** LHRM 的实验）

诚实地说，以上大部分攻击打的是**当前文档的论证方式**，不是项目的目的。以下观察若成立，**会显著削弱本报告**：

- 若有人展示一个 `Z[k,i,j,t]` 无法表示、但对行为预测力显著的二人关系状态 → F4 失效，坐标系不需要模态层。
- 若 Joel et al. (2020) 的 top-5 可以在**保持 Belief/Derived 层归属不变**的前提下被解释为 `DirectedRelationshipState` 的读出 → F3 失效，A5/A21 的退守不必要。
- 若移除 catch-all 后 Case Bank 立刻产出成批、且 Architect 诊断后**收敛到少数几个真洞** → F1/F11 失效，Case Bank 恢复为有效测试。
- 若存在一个 non-romantic、cross-cultural、dyadic、纵向数据集，其构念与 LHRM basis 对齐 → A8 从 CONTESTED 升为 UNCHALLENGED。

---

## 8. 最佳善意论证 FOR 项目，以及它是否存活

红队只攻击是不合格的。以下是我能做出的**最强的**支持论证。

### 8.1 项目的认识论姿态是这个领域里最好的，而这不是小事

它拒绝把未验证的公式称为科学；拒绝单一分数；拒绝把 Unknown 静默压成 neutral；要求保留 provenance；要求 `MAPPING_FAILURE` **在打补丁之前**被记录；要求三个独立 Verifier 消费**同一个冻结版本**；Fixture 002/003 用 K1–K4 知识边界禁止 verifier 回填结局。

**对照 §1 F2 的经验事实**：领域规模最大的一次协作研究（86 位研究者、43 个数据集、2,413 个测量）**依然报告变化不可预测**。在这样的现实里，正确的认识论姿态是**对自己能声称什么保持克制**。LHRM 的 house rules 是按这个现实校准的，而该领域绝大多数论文**一条都没做到**。这不是修辞。

### 8.2 `Representation before scalarization` 是对一个真实病理的正确回应

领域主流工具（IMS / ECR / CSAT / RSE / PPR）都是 4–16 题自陈量表，压成每构念一个数。Joel et al. (2020) 的结果是：**一个 5 变量清单，追踪预测力 ≤18%。**

一个保留 `estimate + uncertainty + evidence + provenance`、**拒绝过早标量化**的表示，是对「再加第 2,414 个测量」的一个**合法且可以说更有根据**的替代方案。**这个领域里没有人在试这件事。** 这里的新意是真实的。

### 8.3 `Belief / Observation / Reality` 分离是经验上必要的，而且 fixture 证明了它可实现

Fixture 001 的 C013/C025（法庭明确无法判定业务是否真的被出售）与 C016（"appears to have been sent"）强制要求一个**法律上权威的不可知**。Fixture 002 的 K1–K4 强制要求 Jim 在 M042 之前不知道卖头发。Fixture 003 的 `recording_time ≠ event_time ≠ knowledge_time` 三分。

**这是我见过的 fixture-based benchmark 里最仔细的信息边界装置。** 这个装置是**独立于 8 构念是否存活的可复用贡献**。即使有向 basis 被彻底拆掉，仍然留下一个已验证的 claim–evidence–knowledge-time 表示。

### 8.4 三层时间结构是文献里的真实空白

我找到的每一个关系测量都把这三层压成一层。Joel et al. (2020) 的 43 个数据集预测不了变化，**一个可信的假说**是：没人成功建模变化，是因为没人对**每个伴侣在什么时候知道什么**有显式表示。

**这是一个真实的、未被占据的利基——而且它不是 LHRM 当前文档声称占据的那个利基**（当前文档声称的是构念收敛）。**所以这个项目最强的版本，不是现在正在执行的那个版本。**

### 8.5 诚实的反向权衡

LHRM 自己的非目标清单（`CURRENT_ARCHITECTURE.md` §11）**让项目永远不可交付**。任何最终用途（匹配、筛查、洞见、治疗辅助、创作）都需要一个分数或至少一个**校准过的序**，而 §11 明确不冻结。但这**修起来很便宜**——§11 本身已经写了 "unless later validated for a specific task"。

### 8.6 诚实评估：这个论证存活吗？

**存活，但不是在当前文档所主张的形态下存活。**

- **可辩护的项目**：「一个带显式知识时间与 provenance 的 dyadic claim 证据表示语言」。它新颖、无既有主张、可检验，而且 §8.3/§8.4 给出了具体的护城河。
- **不可辩护的项目**：「人类关系的 8 维潜在状态 basis」。它是对一个 40 年过程模型的**重新推导**，测量姿态更差，且无数据。

**LHRM 目前把可信度预算花在了后者上，而它本可以低成本地花在前者上。** 具体说：它有 3 个精心冻结的 fixture、一套三层时间规范、和一套 knowledge-boundary 协议——**这些都是前者需要的，而后者不需要**。8 个构念的收敛（§4/§5/§6）恰恰是**两者都不需要**的那部分工作。

**项目因此值得做，但 parent 应该知道：最值得做的版本被当前优先级排序排在第三位。**

### 8.7 「整个项目不值得做」的最强版本，以及我对它的诚实回应

**最强论证：**
1. 项目不做任何有争议的事：不算分、不预测、不估概率、不从个案推总体（§11 + `VALIDATION_CORPUS` 第 7 行）。
2. 它的验证指标（映射覆盖率）**在构造上恒为 100%**（F1、F11）。
3. 一个能映射任何句子的 schema，**满足项目其他所有承诺的方式是把句子原样存进 `Provenance`**——而这恰恰是 §9 明确不想要的（「原始事实不因归一化而删除」= 保留原句）。**评价标准不检验定义项目的那些承诺。**
4. 唯一与真实世界接触的地方（纵向参数估计）**领域已报告失败**（F2 结论 3）。
5. 因此项目**不可能错，也不可能对**。一个不能错的理论不是理论，是格式。

**我的诚实回应：这个论证在「科学模型」这个读法下成立，在「知识表示产物」这个读法下不成立。**

- 论点 2 成立 → 但解法不是放弃项目，是**删掉三个 catch-all**（R1），成本极低。
- 论点 3 成立且尖锐 → 但它同样适用于**所有**保留原文的表示系统（数据库、case-based reasoning、legal evidence systems）。**这不是 LHRM 的特殊缺陷，而是所有表示型项目的共同代价**；区分它们的是**下游是否有用**，而 LHRM 还没走到那一步。
- 论点 4 成立 → 但领域失败的原因**不明**。可能是 LHRM 的时间分辨率不够，也可能是需要 20 年尺度。**领域失败不证明这个方向错，只证明当前尺度不够。**
- 论点 1 + 5 成立 → 这是**唯一真正致命**的。修法就是 R6：写下**一条**「本 schema 会预测、而现有 instrument 不会预测」的命题，写不出来就诚实降级为工程产物。**这个成本几乎为零，但它决定项目是什么。**

**结论：项目存活，条件是 R6 被执行，且 R1–R2 被优先处理。** 若 R6 不做，则「不值得做」这个论证就赢了。

---

## 9. 未找到真实反证的地方（parent 应知道攻击在哪里哑火）

1. **「不存在被理论预测但真实 couple 不表现的稳定均衡」** —— 见 §2 N1。**这个攻击本身是错的**：没有理论提出这种均衡命题，LHRM 的转移假设只是 `unidentified`。
2. **「8 个构念不可分离」** —— 见 §2 N2。无证据；反而 LHRM 已预先写下针对协变文献的正确回应。
3. **「恋爱构念在非恋爱场景崩塌」** —— 见 §2 N4。证据显示**衰减而非崩塌**。
4. **「Liking 与 RomanticAttraction 不可解耦」** —— 见 §2 N5。Sternberg (1987) 存在本身即分离性证据。
5. **「Directionality 本身错了」** —— 见 §2 N3。partner-report null 是**方差**陈述，不是**本体**陈述。
6. **「State != Action 规则有问题」** —— 攻击失败。Hui et al. (2014) 的 Manhattan Effect 反而**支持**它。
7. **「拒绝把「爱/亲密/嫉妒/忠诚」当 primitive 是错的」** —— 攻击失败。
8. **「Unknown 显式化规则是过度工程」** —— 攻击失败。三个 fixture 是它的真实压力测试，且通过了。
9. **「`OutcomeDependence` 是错的」** —— 无反证。项目自标 open question 并交给 redundancy test，**这是诚实的做法**。
10. **「structural balance 自己的经验地位有问题」** —— **我 FETCH_FAILED 了**（需 Balan 1968，`10.1177/…` 与 Crossref 检索均未命中）。因此我只用它证明「项目测不了唯一候选」，**不用它证明平衡成立**。
11. **「跨文化 attachment 不变性失败」** —— **未完成。** 只拿到 Keller (2021) / Mesman (2021) 的出版商 TOC（`Attachment: The Fundamental Questions` ch. 28 / ch. 30），未能读到内容。这条攻击**没有结论**。
12. **「标注分歧是构念问题的信号」** —— **FETCH_FAILED**（Poesio 2012, JAIR 48, DOI `10.1613/jair.3600` 不解析；jair.org 404）。因此「`MAPPING_FAILURE` ≈ 标注分歧」这一条**未建立**；F1/F11 改由 schema 自身的 catch-all 与 §14「只测命名」承担，**结论未受影响**。
13. **「Weiss & Murchison (2005) 的认知/情感双类矛盾」** —— **FETCH_FAILED**（Crossref / Semantic Scholar / Exa / DuckDuckGo 四路未命中）。F4 改由 MacDonald et al. (2013) + Zoppolat et al. (2023) 承担，**结论未受影响**。
14. **文献内部矛盾，我如实并列：** Le & Agnew (2003) 同时说「moderators vary minimally」与「significantly stronger in relational domains」。跨关系类型稳定性在文献里**不是共识而是争议区**。LHRM §2.4 把它当硬判据，**超出了文献共识**。
15. **适应速度是活争议：** Lucas & Clark (2006) vs Stutzer & Fremy-Fragoni (2006) vs Gattig & Minkus (2021)。我**不断言任何一方**，只主张「观测轨迹混合了关系变化 / 谁留下 / 谁进入，任何 F 估计都不区分」。

---

## 10. 一个文档级冲突（顺带发现）

`CONSTRUCT_SCOPE_DIRECTIONALITY.md` §2 直接写：

```text
Asymmetry_k(A,B) = distance( Z[k,A,B], Z[k,B,A] )
```

而 `CURRENT_ARCHITECTURE.md` §11 明确**不冻结统一欧氏距离**、且 §9 原则 4 允许 `category / ordinal / continuous / constraint / probability / Unknown` **共存于混合状态空间**。

**同一个项目里两处直接冲突。** 在一个 interval / ordinal / category / Unknown 共存的空间里，`distance` **未被定义**。这是文档里的一个真实空洞，不是修辞问题。

---

## 11. 给 parent 的优先处理建议

按「修起来便宜 / 收益大」排序，**不是**按科学重要性排序：

1. **提升 `PPR` 与 `Satisfaction` 到一等状态层**（A5 / A20 / A21 / F3）。**唯一一处**找到「项目自己的层边界被经验文献直接反向排序」的地方。改动小、收益最大。
2. **删除 `MAPPING_FAILURE` 路径上的三个 catch-all 出口**（F1），或至少要求每次 `NARRATIVE_ONLY` / `IRRELEVANT` 判定附带「若不允许此出口，此句会落在哪里」的强制记录。
3. **发布 12 份语料 × Gate B 11 类的覆盖矩阵**（F9），并把 Gate B 从「schema 测试」重新定位为「语料缺口清单」。
4. **把 §2.4 Scope stability 从 KEEP 判据降级为「需 instrument 才能执行」的待办**，直到项目有至少一个多题项 instrument 并通过 Vandenberg & Lance 意义上的 invariance 检验。
5. **写下 R6 那一条命题。** 写不出来就诚实降级为知识表示产物。

**不建议现在做的事：** 不要因为 F2 就去重选 8 个构念。F2 的真实结论是**层排序错了**，不是**构念清单错了**。重选清单会把一个层错误伪装成清单错误，并损失 §4 已经做对的 semantic independence 工作。

---

## 12. 引用清单

> 所有卷期页均经 Crossref API 核验（2026-09-27）。标注 `FETCH_FAILED` 的条目**不作为论据**。

**CITED_PRIMARY**

1. Joel, S., Eastwick, P. W., Allison, C. J., Arriaga, X. B., Baker, Z. G., Bar-Kalifa, E., … & Wolf, S. (2020). Machine learning uncovers the most robust self-report predictors of relationship quality across 43 longitudinal couples studies. *PNAS* 117(32), 19061–19071. DOI `10.1073/pnas.1917036117` — https://www.pnas.org/doi/10.1073/pnas.1917036117
2. Eastwick, P. W., Eagly, A. H., Finkel, E. J., & Johnson, S. E. (2011). Implicit and explicit preferences for physical attractiveness in a romantic partner: A double dissociation in predictive validity. *JPSP* 101(5), 993–1011. DOI `10.1037/a0024061`
3. Segal, N., & Fraley, R. C. (2016). Broadening the investment model: An intensive longitudinal study on attachment and perceived partner responsiveness in commitment dynamics. *J. Social & Personal Relationships* 33(5), 581–599. DOI `10.1177/0265407515584493`（online 2015-05-22）
4. MacDonald, G., Locke, K. D., Spielmann, S. S., & Joel, S. (2013). Insecure attachment predicts ambivalent social threat and reward perceptions in romantic relationships. *J. Social & Personal Relationships* 30(5), 647–661. DOI `10.1177/0265407512465221`
5. Mund, M., & Johnson, M. D. (2020). Lonely Me, Lonely You: Loneliness and the Longitudinal Course of Relationship Satisfaction. *Journal of Happiness Studies* 22(2), 575–597. DOI `10.1007/s10902-020-00241-9`
6. Musick, K., & Bumpass, L. L. (2006). Cohabitation, Marriage, and Trajectories in Well-Being and Relationships. 全文 PDF: https://ccpr.ucla.edu/wp-content/uploads/2024/04/Re-Examining-the-Case-for-Marriage_-Variation-and-Change-in-Well-Being-and-Relationships.pdf
7. Stutzer, A., & Frey, B. S. (2006). Does marriage make people happy, or do happy people get married? *Journal of Socio-Economics* 35(2), 326–347. 全文: https://docs.iza.org/dp1811.pdf
8. Stutzer, A., Fremy-Fragoni, V., & RTS/OFS (2006). Does marriage make people happy or do happy people get married?（对 Lucas & Clark 的公开反驳）https://paa2006.populationassociation.org/papers/60777
9. Laurenceau, J.-P., Barrett, L. F., & Pietromonaco, P. R. (1998). Intimacy as an interpersonal process. *JPSP* 74(5), 1238–1251. DOI `10.1037/0022-3514.74.5.1238`
10. Le, B., & Agnew, C. R. (2003). Commitment and its theorized determinants: A meta-analysis of the Investment Model. *Personal Relationships* 10(1), 37–57. DOI `10.1111/1475-6811.00035`
11. Tran, P. D., Judge, M., & Kashima, Y. (2019). Commitment in relationships: An updated meta-analysis of the Investment Model. *Personal Relationships* 26(1), 158–180. DOI `10.1111/pere.12268`
12. Brooks, J. E., Ogolsky, B. G., & Monk, J. K. (2019). Commitment in Interracial Relationships: Dyadic and Longitudinal Tests of the Investment Model. *Journal of Family Issues* 39(9), 2685–2708. DOI `10.1177/0192513X18758343`
13. Rusbult, C. E., Martz, J. M., & Agnew, C. R. (1998). The Investment Model Scale. *Personal Relationships* 5(4), 357–387. DOI `10.1111/j.1475-6811.1998.tb00177.x`
14. Branje, S. J. T., Frijns, T., Finkenauer, C., Engels, R., & Meeus, W. (2007). You are my best friend: Commitment and stability in adolescents' same-sex friendships. *Personal Relationships* 14(4), 587–603. DOI `10.1111/j.1475-6811.2007.00173.x`
15. Sandberg, et al. (2022). A test of the investment model among asexual individuals: The moderating role of attachment orientation. *Frontiers in Psychology*. DOI `10.3389/fpsyg.2022.912978`
16. Zoppolat, G., Faure, R., Schneider, I. K., & Righetti, F. (2023). Systematic Study of Ambivalence in Romantic Relationships — `CITED_SECONDARY`

**CITED_CLASSIC**（经 Crossref 核到卷期页，未读正文）

17. Vandenberg, R. J., & Lance, C. E. (2000). A review and synthesis of the measurement invariance literature. *Organizational Research Methods* 3(1), 4–70. DOI `10.1177/109442810031002`
18. Ribeiro, M. T., Wu, T., Guestrin, C., & Singh, S. (2020). Beyond Accuracy: Behavioral Testing of NLP Models with CheckList. *ACL 2020*, 4902–4912. DOI `10.18653/v1/2020.acl-main.442`
19. Cartwright, D., & Harary, F. (1956). Structural balance: a generalization of Heider's theory. *Psychological Review* 63(4), 277–293. DOI `10.1037/h0046049`
20. Lakatos, I. (1970). Falsification and the methodology of scientific research programmes. In I. Lakatos & A. Musgrave (Eds.), *Criticism and the Growth of Knowledge*, pp. 91–196. Cambridge University Press.
21. Popper, K. R. (1959). *The Logic of Scientific Discovery*. Hutchinson.

**指针级（未读内容，不承重）**

22. Lucas, R. E., & Clark, A. (2006). Do People Really Adapt to Marriage? *J. Happiness Studies* 7(4), 405–426 — `CITED_SECONDARY`
23. Gattig, A., & Minkus, L. (2021). Does Marriage Increase Couples' Life Satisfaction? — `CITED_SECONDARY`
24. Hui, C. M., Finkel, E. J., Fitzsimons, G. M., Kumashiro, M., & Hofmann, W. (2014). The Manhattan effect. *JPSP* 106(4), 546–570 — 指针来自 https://iarr.org/img/syllabi/Agnew_GR-PSY_2016_Close-Relationships.pdf
25. Fraley, R. C., Gillath, O., & Deboeck, P. R. (2021). Do life events lead to enduring changes in adult attachment styles? *JPSP* 120(6), 1567–1606 — https://labs.psychology.illinois.edu/~rcfraley/pubs.html
26. Sun, T., Fraley, R. C., & Drasgow, F. (2021). Matches made with information: Fitting measurement models to adult attachment data. *Assessment* 28(7), 1828–1847 — 同上
27. Fraley, R. C., & Dugan, K. A. (2021). The consistency of attachment security across time and relationships. In Thompson, Simpson & Berlin (Eds.), *Attachment: The Fundamental Questions*, pp. 147–153. Guilford. — **结论内容未核实，不作为论据**
28. Raby, K. L., Fraley, R. C., & Roisman, G. I. (2021). Categorical or dimensional measures of attachment? 同上书, pp. 70–77. — **未读，不作为论据**
29. Keller, H. (2021). Attachment Theory: Fact or Fancy? / Mesman, J. (2021). Attachment Theory's Universality Claims: Asking Different Questions. 同上书, ch. 28 / ch. 30. — **仅 TOC，攻击未完成**

**FETCH_FAILED（不作为论据，如实登记）**

30. Weiss, M., & Murchison, E. (2005). When and why are romantic relationships ambivalent? *ASR* 70(2), 287–306. — Crossref / Semantic Scholar / Exa / DuckDuckGo 四路未命中
31. Poesio, M. (2012). A survey of ambiguity and consensus in natural language processing. *JAIR* 48, 1–154. DOI `10.1613/jair.3600` 不解析；jair.org 404
32. Balan, P. (1968). Structural balance among signed graphs: the two-mode theory. *Psychological Bulletin* 68(6), 406–420. — Crossref 未命中

**Project-internal pointers**（本报告的直接依据）

33. `AGENTS.md`（Representation-first invariant；Current architecture direction；Validation discipline；Mutation discipline）
34. `docs/foundation/CURRENT_ARCHITECTURE.md`（§2 最小对象与边界；§3 世界层与局部投影；§4 二人关系的方向性；§6 State/Action/Belief/Constraint 分离；§7 低冗余≠低动态耦合；§8 时间与历史分支；§9 Measurement 原则；§10 Case Bank；§11 非目标；§12 工程顺序）
35. `docs/foundation/PARAMETER_CONVERGENCE_V0_1.md`（§2 收敛判据；§4 D1–D8；§5 B1–B2；§6 P1–P5；§7 Agent 层；§8 降级为 Action/Observation/Proxy；§9 R1–R5；§10 表面字段；§11 Candidate Minimal Directed Basis v0.1；§12 暂不加入的熟悉词；§13 第一轮 representation schema 与 MAPPING_FAILURE；§14 Measurement 暂不冻结；§15 Gate A/B/C）
36. `docs/foundation/CONSTRUCT_SCOPE_DIRECTIONALITY.md`（§1 加性分解；§2 方向性为一等属性与 `Asymmetry_k = distance(...)`；§3 跨 scope 不机械复制；§4 低冗余≠动态独立；§6 关系图与局部投影；§7 六项测试）
37. `docs/validation/VALIDATION_CORPUS_V0_1.md`（12 份材料的 L0–L3 分级；跨层覆盖表；Fixture 001–003 推荐；L1-003 leakage 禁令；「No generative-AI-invented stories / No three-rewrites-of-one-story」；敏感内容规则）
38. `docs/validation/fixtures/FIXTURE_001_L0_001_CARTY_FACT_PACKAGE.md`（C001–C026；K0–K4 知识边界；C013/C016/C025 不可知与 `appears`；准备者标注）
39. `docs/validation/fixtures/FIXTURE_002_L1_003_MAGI_PACKAGE.md`（M001–M061；K1–K4 知识边界；`said != believed != true`；准备者标注；leakage 禁令）
40. `docs/validation/fixtures/FIXTURE_003_L1_001_STORYCORPS_PACKAGE.md`（S001–S042；K0_editorial/K1/K2/K3；`recording_time != recalled_event_time != event_time`；rights 状态 `HUMAN_REVIEW_REQUIRED` / `POINTER_HASH_ONLY`；verdict 词表）
41. `README.md`（当前阶段、当前 basis、建模边界、验证路线、治理）

---

## 13. `status_recommendation`

**SUCCESS**

12 项攻击面全部有裁定；6 项取得可引用、可定案的证伪或强挑战（F1、F2、F3、F4、F7、F9）；3 项 CONTESTED（F5、F6、A15/A16/A17/A23）；6 项明确 `NO_EVIDENCE_FOUND_FOR_CHALLENGE` 或 `UNCHALLENGED`（N1–N6、A10–A12、A18、A19）；5 项 `FETCH_FAILED` 如实登记且**无一被用作承重论据**。

**独立性：CONFIRMED。** 见 §0。

**给 parent 的一句话结论**：
> 项目的**目的**存活；项目**当前执行的重心**（8 构念 basis 收敛）不是最值得做的部分，而**最可能出错的那一层**是 Belief/Derived 的层排序。Case Bank 目前不是测试——这是一个可低成本修复的设计问题，不是否定项目的理由。
