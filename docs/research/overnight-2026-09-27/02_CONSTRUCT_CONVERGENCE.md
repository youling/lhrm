# 02_CONSTRUCT_CONVERGENCE — 科学构念收敛深度审计

**Status:** RESEARCH / NOT FROZEN — 全部裁决为 `RESEARCH_CANDIDATE`，等待 Human / Architect 仲裁
**As of:** 2026-09-27
**Parent:** `youling/lhrm#30` overnight exploration swarm, Wave 1, lane R01
**Scope:** Human–Human Dyad 的 directed relationship-state candidate 构念
**审计对象:** `docs/foundation/PARAMETER_CONVERGENCE_V0_1.md` §11 `Candidate Minimal Directed Basis v0.1` 的 8 项 + §4 / §5 / §6 / §9 的 contested / derived / belief 项

> 本文不修改 canonical ontology，不冻结任何数值、权重、距离、概率或转移函数。
> 每一个「裁决」单元格都是研究建议，不是决定。

---

## 0. 本文与既有文档的关系

本文是**审计**（audit），不是**重建**（rebuild）。它继承并复核：

- `docs/foundation/PARAMETER_CONVERGENCE_V0_1.md` — 当前 candidate construct 清单；
- `docs/foundation/CONSTRUCT_SCOPE_DIRECTIONALITY.md` — 构念跨域作用与方向性原则；
- `docs/foundation/CURRENT_ARCHITECTURE.md` — 当前 canonical 架构快照；
- `docs/research/RESEARCH_REPORT_SCIENTIFIC_RELATIONSHIP_PRIMITIVES.md` — prior evidence（62 构念语义边界审计）。本文**复用**其结构与大部分结论，只在 §7 记录 12 处需要收紧、改层或加限定的 Delta。

---

## 1. 审计方法与证据分级

### 1.1 每构造念的 7 行 row-set

| 行 | 名称 | 审计问题 |
|---|---|---|
| 1 | 精确语义边界 | 它是什么？它**显式不是**什么？ |
| 2 | 最近邻构念 | 心理学文献里最容易与它混淆的构念是哪些（附 DOI / pointer） |
| 3 | 反例解耦 | 具体到可想象的场景：A 在 B 缺；B 在 A 缺 |
| 4 | 测量族 | 典型量表 / 范式，以及它们各自的已知缺陷 |
| 5 | 时间行为 | state vs trait、波动性、衰减、惯性 |
| 6 | 范围 / 方向性 | 内在是否 dyad-directed？是否需要 domain 索引？在六种 dyad 形态下语义是否稳定 |
| 7 | 裁决 | `KEEP` / `SPLIT` / `MERGE` / `DERIVED` / `BELIEF_ONLY` / `REJECT` / `OPEN` + 强制该裁决的证据 |

### 1.2 来源标记（与 prior report 的分级正交）

| 标记 | 含义 |
|---|---|
| `CITED_PRIMARY` | 本次审计实际打开了原文 / 原始摘要 / 原始结果段 / Crossref 完整题录 |
| `CITED_SECONDARY` | 经二手来源转述读到，未打开原始出处 |
| `AGENT_RECALL` | Agent 先验，本次未核实，**不得作为裁决依据** |
| `NO_DOI_VERIFIED` | 保留为指针，但 DOI 或题录本轮检索未命中 |

本次审计的取证方式：Crossref REST API（书目元数据核验）、OpenAlex、websearch 摘要、webfetch 全文 PDF。**本轮有 3 条既有题录在核验中被推翻、1 条候选 DOI 被证伪**（见 §6.1），因此凡无 DOI 的指针一律标 `NO_DOI_VERIFIED`。

### 1.3 心理测量层面的三个通用批评线索

1. **反向计分题会制造出本不该有的因子。** 任何用「信任题目的反向措辞」测出来的不信任维度，都可能是方法学 artifact 而不是构念事实。
2. **bifactor 模型揭示的「一般因子 + 特定因子」层级，往往比名义上的多维模型更接近数据。** 见 §6.4（Caregiving）。
3. **不同方法学传统测的可能是不同的构念。** 见 §6.3（attachment：AAI vs 自评，mean r=.09）。

报告规范参照 JARS（Appelbaum et al., 2018, `10.1037/amp0000191` [S38]）。

---

## 2. 元层结论（先于逐构念）

### 2.1 「有向性」在测量层被确认，但确认出的是构念特异的不对称度

`CONSTRUCT_SCOPE_DIRECTIONALITY.md` §2 规定「凡是『某个人对另一个人』的状态，应优先视为有向量」。本次审计确认这一原则，并**补上一条该文档没有的定量约束**：

| 关系 | 跨伴侣一致性 | 投射系数 | 来源 |
|---|---|---|---|
| 照护者报告 <-> 被照护者报告的关系满意度 | **r = .43**（中等） | — | [S15] |
| 伴侣报告的关系信任 | **r = .11**（不显著） | — | [S15] |
| 正向浪漫关系行为的 self-other agreement | avg **r = .18** | avg **r = .90** | [S36] |
| 负向浪漫关系行为 | avg **r = .19** | avg **r = .77** | [S36] |
| 互动后双方自评「对方喜欢我」 | 系统性不对称（liking gap），5 岁即出现、随年龄扩大 | — | [S45] |
| 结构性互依知觉（日常情境 ESM） | 转述为 strongly agree | — | 转引自 [S28] |

**推论（`RESEARCH_CANDIDATE`）：一致性 / 不对称度是构念自身的经验属性，必须逐构念估计并记录，不能作为全局架构假设。** 「有向」不等于「低一致」——`Trust` 在本审计中的跨伴侣一致性低至 r=.11，而照护倾向相关的 satisfaction 一致性可达 r=.43。LHRM 不应在 schema 层假定任何特定的不对称量级。

### 2.2 「有向边」必须有 person / target / 边三层分解

Social Relations Model 分解（perceiver / target / relationship effect）显示，即便对 liking 这样最简单的关系评价，**关系特异成分也是最大方差来源**（[S40], `CITED_SECONDARY`）。这与 `CONSTRUCT_SCOPE_DIRECTIONALITY.md` §1 的分解式方向一致。

**推论（`RESEARCH_CANDIDATE`）**：Liking 及其余 directed candidate 若以单一标量存入，会把 person 层与 target 层的慢成分混入边状态。建议所有 directed 构念的 `StateCoordinate` 显式携带：

```text
z[k, i, j, t] = { edge_estimate, person_prior_i, target_attr_j, uncertainty, evidence, provenance }
```

这不是要求现在就实现，而是**在 ontology 层先承认边状态不是纯边量**。

### 2.3 8 维 basis 的保留理由需要更换

`PARAMETER_CONVERGENCE_V0_1.md` 隐含的保留理由是「这 8 个构念语义上互相独立」（§15 Gate C 的 redundancy challenge 针对此点）。本次审计认为这个理由**部分不成立**：Berscheid (2010, `10.1146/annurev.psych.093008.100318` [S21]) 记载，Hendrick & Hendrick (1989) 把多套 love 量表合并做因子分析，**未能复现任一既有 love 类型学的结构**；Berscheid 只能保守地主张「至少三类 love（companionate / romantic / compassionate）需要分别纵向评估」，并直言「问人们是否爱伴侣，很可能对关系中存在的情感状态及其未来轨迹几乎不具信息量」。

**这意味着：把「爱 = A+B+C」当作防御 8 维 basis 的理由，等于默认了一个已被否证的心理类型学承诺。**

**替代理由（`RESEARCH_CANDIDATE`）**：8 维保留的正当性来自**表示需要**而非语义差异——它们是**不同观测通道**（主观评价 / 动机 / 感知 / 结构 / 意愿）、**不同时间尺度**（快变 / 慢变 / 极慢）、**不同方向性**（`i->j` 与 `j->i` 可解耦）的**独立记录槽**。这恰好是 LHRM representation-first 立场的内容，但必须**明说**，否则就是在重复一个已被否证的承诺。

### 2.4 Investment Model 的「既是派生又是独立」硬矛盾

| 来源 | 样本 | Satisfaction | Investments | Alternatives | 三者解释 Commitment 方差 |
|---|---|---|---|---|---|
| Le & Agnew (2003) [S01] | 60 samples, N=11,582 | r = .68 | r = .46 | r = - .48 | 61% |
| Tran, Judge & Kashima (2019) [S02] | 202 samples, N=50,427 | r = .65 | r = .53 | r = - .43 | — |

且 `commitment <-> stay/leave` r = .47（12 studies, N = 1,720）[S01]。

**推论（`RESEARCH_CANDIDATE`）**：`Dedication` 的独立性论证**不应**是「它是 61% 残差」（那是定义使然），而应是「它在 61% 之外仍预测 stay/leave、trust、IoS、dyadic adjustment，且与 personal dispositions 基本无关」（后者由 Rusbult, Martz & Agnew 1998, `10.1111/j.1475-6811.1998.tb00177.x` [S03] 提供）。这是可辩护的增量信息论证。

### 2.5 OutcomeDependence：理论地位最硬，测量最薄

详见 §6.1。这是本次审计最重要的单条发现。

---

## 3. 逐构念 row-set

> 每构造念 7 行。「裁决」全部是 `RESEARCH_CANDIDATE`。

### 3.1 `Liking`

| 维度 | 结论 |
|---|---|
| 1 语义边界 | **是**：i 对 j 的一般性、正向、低唤起的评价与亲近倾向。**显式不是** romantic 伴侣式趋近、性欲、信任（愿交出脆弱性）、自己感到被回应（PPR）、在一起很开心（satisfaction）。**不是 disposition**：prior report 混淆了 liking 与 dispositional warmth，二者层级不同 [S22 vs S33]。 |
| 2 最近邻构念 | PPR（接收方感受，`10.1111/spc3.12308` [S34]）；Trust（愿交出脆弱性 vs 只是评价）；SRM 的 liking 三分解；meta-liking（「我认为对方喜欢我」，Belief 层对应物）[S40]。 |
| 3 反例解耦 | **A 在 B 缺**：同住多年、务实可靠但「从不问我在想什么」-> liking 高、PPR 低。**B 在 A 缺**：讨好型 / 被评价焦虑者自评「我很喜欢他」而真实 liking 低（meta-liking 侧亦有系统偏差：liking gap [S45]；projection r = .77–.90 [S36] 说明自陈评价被报告者自身状态污染）。 |
| 4 测量族 | SRM round-robin 评分；IoS（**单题图示**，`10.1037/0022-3514.63.4.596` [S19]，其 single-item 性质由 [S14] 原文明确）；RCI（`10.1037/0022-3514.57.5.792` [S20]）。 |
| 5 时间行为 | state-trait 混合，必须三层拆。关系特异成分是最大方差来源 [S40]；方向性随认识时长部分收敛但**不会消失**（consensus 上升、uniqueness 略降）。 |
| 6 范围 / 方向性 | 严格 dyad-directed；跨六形态最稳定。stranger 边上低值应作 `Unknown` 或带 prior 的低区间，**不得**记为 `0`。 |
| 7 裁决 | **`KEEP`**。强制条件：必须记为 `Susceptibility_i + Likedness_j + Edge_ij + residual` 三分解，否则 `GeneralizedLiking_i` 会污染边状态。**范围纠正**：dispositional warmth 不应与 `Liking(i->j)` 混层。 |

### 3.2 `RomanticAttraction`

| 维度 | 结论 |
|---|---|
| 1 语义边界 | **是**：i 对特定 j 的伴侣式特殊趋近、专注与理想化。**显式不是**一般亲和、性欲、依恋安全、关系认同。**不是神经机制**：Fisher 三系统理论是机制 / 演化假说 [S25, S26]。 |
| 2 最近邻构念 | Liking；SexualDesire；Idealization；`courtship attraction` vs `bonding attraction`（Bode 2023, `10.3389/fpsyg.2023.1176067` [S26] 的明确拆分提议）。**重大争议**：Bode (2023) 系统性质疑 Fisher (1998, `10.1007/s12110-998-1010-5` [S25]) 的「三系统独立演化」框架。 |
| 3 反例解耦 | **A 在 B 缺**：无性恋的高强度浪漫依恋（`AGENT_RECALL`，未直接核验 asexuality 原始文献）；Fisher 自述的三系统可分别运行 [S25 转引]。**B 在 A 缺**：征服导向 / 短期纯性关系中极高性欲、极低浪漫与 liking。**A 低 B 高**：包办 / 政治婚姻中制度身份极高而 romantic attraction 近零。 |
| 4 测量族 | Passionate Love Scale（Hatfield & Sprecher 1986, `AGENT_RECALL`）；Love Attitudes Scale（`10.1037/0022-3514.50.2.392` [S22]，N=807+567）—— **这是 love 态度量表，不是状态量表**；Fisher 的 72 题量表（`UNVERIFIED`，其因子结构本轮未核验）。**方法学警告**：所有 love 类型学量表交叉因子分析都未复现各自分类结构 [S21]。 |
| 5 时间行为 | 快变、显著衰减、可被 attachment / commitment 部分取代；[S26] 指出 Fisher 后期工作与「三系统日益独立」的说法自相矛盾。 |
| 6 范围 / 方向性 | 严格 dyad-directed。**kin 边上必须允许非零**（Westermarck 只压制性表达，不必然压制 romantic attraction）。stranger 边上高度显著且高波动。 |
| 7 裁决 | **`KEEP` + 边界 `OPEN`**。强制理由：与 liking / sexual desire 的解耦在临床上真实存在。**但**不采纳 Fischer 三系统独立性作为独立性理由。**建议**：(i) Fischer 三系统降级为 `mechanism_evidence`；(ii) 显式登记 Bode (2023) 的 courtship / bonding 拆分为 `OPEN` 子问题；(iii) 若 Case Bank 出现「高择偶驱动力但零维持驱动力」的稳定反例，再启动 SPLIT。 |

### 3.3 `SexualDesire`

| 维度 | 结论 |
|---|---|
| 1 语义边界 | **是**：i 指向特定 j 的、目标特异的**主观**性欲。**显式不是**生殖器唤起测量、性行为、性身份 / 性取向、无性恋身份、浪漫吸引。**最硬边界** [S23]：subjective 与 genital 是两个不同构念，男性一致性 r = .66，女性 r = .26。 |
| 2 最近邻构念 | Sexual arousal（生理）；Erotic desire；Sexual motivation；Asexuality / desire-mode（Agent 属性）；RomanticAttraction。[S24] 进一步主张：女性性唤起的**特异性**本身即核心议题。 |
| 3 反例解耦 | **A 在 B 缺**：无性恋浪漫伴侣（desire 约 0 而 romantic 高）；[S23] 汇总的 subjective-genital desynchrony 模式。**B 在 A 缺**：对非偏好对象有 genital response 而**不**报告主观唤起。 |
| 4 测量族 | 自我报告主观唤起（连续 Likert / visual analog）；genital 测量（penile / vaginal plethysmography）；目标特异多题项欲望量表（具体工具 `AGENT_RECALL`）。 |
| 5 时间行为 | state 成分远小于 trait 成分，且受生理周期 / 激素 / 情境门控 [S23]。基线性欲（Agent）与对特定 j 的欲望（edge）必须分离——与 LHRM §7 的 `BaselineLibido_A != SexualDesire_(A->B)` 一致。 |
| 6 范围 / 方向性 | 严格 dyad-directed（目标特异性是定义的一部分）。kin 边上取值受强约束，**不得默认 0 也不得默认高**。 |
| 7 裁决 | **`KEEP`**，**附强制测量条件**：`SexualDesire` 与 `PhysiologicalArousal` 必须是两个坐标，且每个 `StateCoordinate` 必须携带 `measurement_channel`。理由：r = .66 vs .26 的一致性差异 + 两个方法学调节变量意味着「测的是哪个通道」本身就是状态描述的一部分。违反此条件会在跨性别 / 跨文化比较中系统性误读。 |

### 3.4 `Trust`

| 维度 | 结论 |
|---|---|
| 1 语义边界 | **是**：i 在具体领域上对 j「愿承担被辜负的风险」的结构性意愿 + 对 j 善意 / 能力 / 正直的认知前提。**显式不是**情绪安全感、credibility、predictability、caregiving、PPR、承诺。**必须有 domain 索引**——domain-specificity 是理论内生的（[S10] 原文：可以信任同事做研究合作项目，但不信任他代自己的课），不是可选 facet。 |
| 2 最近邻构念 | AttachmentSecurity（被托底感 vs 愿交出脆弱性）；Predictability（Rempel 三维量表成分，`10.1037/0022-3514.49.1.95` [S08]）；Credibility / dependability / faith（`NO_DOI_VERIFIED`）；Betrayal history（事件）。 |
| 3 反例解耦 | **A 高 B 低**：依恋焦虑者理智上完全信任伴侣，但情感上仍觉不被托底 [S33]。**B 高 A 低**：长期酗酒伴侣——情绪上「这就是我的家」很安全，但关键领域绝不交出。 |
| 4 测量族 | Rempel 三维 Trust Scale [S08]；Mayer et al. willingness to be vulnerable 4–10 题（alpha 在 .59–.84 间波动，作者自承偏低并援引 Kline 的辩护 [S10]）；Investment Model Scale 中作为相关变量 [S03]。**partner-reported trust 跨伴侣一致性 r = .11（ns）**[S15]——直接反驳「trust 是共享 pair 属性」。 |
| 5 时间行为 | 惯性中等偏高、衰减慢、崩塌快。信任依赖 strain test 累积 [S33]，因此**在零 / 短程边上 trust 主要是 `Unknown` 而非低值**——**「相处多年」只推出「有机会累积 strain test」，不推出 trust 高**。这是 Case Bank court-fact 映射的关键约束。 |
| 6 范围 / 方向性 | 严格 dyad-directed **且 domain-indexed**。跨形态高度稳定。 |
| 7 裁决 | **`KEEP`**（13 个候选中最稳的一个），**强制条件**：`Trust` 的 signature 必须含 `domain`（至少：财务 / 身体与健康 / 育儿 / 情感脆弱 / 决策委托）。理由：把 domain 做成可选 facet 会让单标量变成四个不兼容标量的平均。domain 索引同时解释了为什么 `OutcomeDependence` 必须另立且独立带 domain。 |

### 3.5 `Distrust`（争议项）

| 维度 | 结论 |
|---|---|
| 1 语义边界 | **是（若独立）**：i 对 j「确信对方会伤害 / 背叛」的主动预期，驱动监控、检验、回避。**显式不是** `1 - Trust`——[S09] 原文：low trust 是「没有希望」，high distrust 是「有理由的恐惧」，两者 do not converge—they are characterized as conceptually distinct conditions。 |
| 2 最近邻构念 | Trust；Attachment anxiety（Agent 属性）；Jealousy；Betrayal history（事件）；Monitoring behavior（observable）。 |
| 3 反例解耦 | **A 高 B 低**：对财务极度不信任、对情感高度信任的同一关系。**A 低 B 低**：零信息新关系——既不信任也不怀疑。**方法学警告**：许多 distrust 操作化是信任题的反向计分，而反向计分在因子分析中天然分离出第二因子（[S09] 论证中即引用了 Wrightsman 哲学量表两因子的例子）-> 部分「trust / distrust 二维」证据可能是 artifact。 |
| 4 测量族 | Lewicki-McAllister-Bies 双维评分；McKnight et al. (2001) 单篇章节（`CITED_SECONDARY`，元数据未独立核验）；亲密关系研究多用就地编写的负向措辞题目。**不存在一个被广泛接受、跨实验室可比的 close-relationship distrust scale**——这是本构念最大的硬伤。 |
| 5 时间行为 | 若独立应为慢变量、崩塌慢、恢复极慢。**该时间剖面无直接经验支持（`UNVERIFIED`）。** |
| 6 范围 / 方向性 | 严格 dyad-directed + domain-indexed（同 Trust）。 |
| 7 裁决 | **`OPEN`（强烈倾向 `DERIVED`）**。这是本文对 prior report 的**最主要分歧**。理由：(a) 同刊同档正面对撞已持续 30+ 年 [S09 vs S10]；(b) Schoorman et al. (2007) 的对应论断（`CITED_SECONDARY`）；(c) **决定性实验尚未见成规模执行**——用非反向措辞的独立题目在同一 dyad 上同时测 trust 与 distrust、检查是否真能同 domain 内同时高。**建议**：先按 domain 索引的 Trust 建模，在观测不确定区（低信度、近中性）允许显式 `ambivalent` 标记；只有当纵向数据能稳定复现「同 domain 内 trust 高而 distrust 也高」时，才立独立坐标。 |

### 3.6 `AttachmentSecurity`

| 维度 | 结论 |
|---|---|
| 1 语义边界 | **是**：i 在与 j 的具体关系中「预期对方可获得 / 可依赖、需要时敢暴露脆弱」的**边安全基底**。**显式不是**依恋风格（person-level 个体差异）、Trust、AAS 的 dependency、love。**注意**：`security = 1 - anxiety - avoidance` 这个压缩本身是待检验的建模决定，不是文献事实（见 §6.3）。 |
| 2 最近邻构念 | ECR-R anxiety / avoidance（person-level）[S12]；AAI states of mind [S11]；Collins & Read dependency [S13]，其定义**复合了 reliance 与 trustworthiness**（「strong reliance on ones partner in conjunction with expectations that the partner is trustworthy」，[S17] 原文），故与 `Trust` 不是可解耦的；Responsiveness / PPR [S33]。 |
| 3 反例解耦 | **A 高 B 低** / **B 高 A 低**：见 §3.4。**A 高 B 低（Security 高、Caregiving 低）**：被虐待但仍以家为安全底地的受控者。**额外反例**：在 AAS 口径下，「依赖高」与「信任低」在概念上不可同时表达，因为 dependency 定义已含 trustworthiness 预期。 |
| 4 测量族 | ECR / ECR-R [S12]；RSQ（`AGENT_RECALL`）；Adult Attachment Scale [S13]；ASRS（Brassard et al. 2009，`NO_DOI_VERIFIED`）；AAI [S11]。**关键数字** [S12]：ECR-R 3 周 latent 稳定 85% shared variance；HLM 显示 ECR-R 解释**与浪漫伴侣互动**的 diary attachment 情绪人际差异的 **30–40%**，但只解释**与家人朋友**互动的 **5–15%**。 |
| 5 时间行为 | person 层极稳（3 周 85%），但 edge 层必须能变——机制是 earned security（[S33] 记载该命题 yet to be fully tested）。要求 person 与 edge 分离。 |
| 6 范围 / 方向性 | 严格 dyad-directed（[S12] 是支持它最强的定量证据）。但边状态的可估计性因方法学争议而存疑 [S11, S44]。 |
| 7 裁决 | **`KEEP`，但标 `CONTESTED / LOW_CONSENSUS`，并要求 person / edge 双层且保留原始二维。** 支持侧 = [S12]；反对侧必须同时记录 = [S11]（AAI vs 自评 mean r = .09，N = 961）、[S44]（not profitably conceptualized as a single, monolithic construct）、[S39]（the categories do not seem to be "real" except as regions in a two-dimensional space）。**结论**：不应把 `AttachmentSecurity(i->j)` 建模成连续、低不确定性的单标量；应是 person 层 prior（anxiety, avoidance）+ 边层残差构成的**高不确定坐标**。 |

### 3.7 `Caregiving`

| 维度 | 结论 |
|---|---|
| 1 语义边界 | **是**：i 指向 j 的、在对方需要 / 脆弱时提供照护的**关系性动机与倾向 + 敏感度 / 临近 / 胜任**。**显式不是**照护行为（Action / Observation）；被照护者的感受（PPR 侧）；Dedication；Obligation（照护的一种**动机**）；Trust。**现有表述「Caregiving Motivation / Care Orientation」准确，但未点明它同时含「倾向」与「胜任」两层**（[S14] 的 responsive caregiving 复合里就含 sensitivity 与 capable caregiver）。 |
| 2 最近邻构念 | PPR（接收侧，方向相反；[S32] 的 paradox of received support——received support 可能**提高**应激反应，而 perceived partner responsiveness 才是有益路径；相关短文 [S31]）；Altruistic motivation（[S15] 的 7 维之一）；Communal orientation；Attachment（[S17]：照护者自身 attachment model 在控制伴侣 attachment 与照护后仍强预测关系功能）。 |
| 3 反例解耦 | **A 在 B 缺**：到处帮忙但帮不到点子上；跨文化情形（[S33] 引 Kim et al. 2008：亚洲人更倾向行为性而非言语性支持 -> PPR 低但照护高）。**B 在 A 缺**：专业共情者 / 高功能共情但无关怀，或以共情操控。**额外必需反例** [S15]：7 维里同时存在 feels obligated、self-benefit、needy (incapable) partner、relationship purposes——**「照护行为」与「照护动机」之间也必须解耦**。 |
| 4 测量族 | Caregiving Questionnaire（Kunce & Shaver 1994，4 维）[S18]；Feeney & Collins 的 Motivations for Caregiving / Not Caregiving（各 40 题 -> 各 7 维）[S15]；responsive / compulsive / controlling 三复合 [S14]。**最重要的心理测量警示** [S18]：N=912 智利受试者，bifactor-CFA（2 general + 4 specific）**优于**原始 4 维正交结构，且跨 sex 与 sexual orientation 测量等值。 |
| 5 时间行为 | 倾向 / 胜任层慢、行为层快（分钟尺度可测）。跨伴侣一致性中等（satisfaction 侧 r = .43）[S15]。 |
| 6 范围 / 方向性 | 严格 dyad-directed。跨形态语义稳定但角色变异大（亲子、伴侣、朋友、非亲缘长期照护、护患）。`CareNeed_j` 是 target 侧的另一个语义位置，不可与 `Caregiving_(i->j)` 混（`CONSTRUCT_SCOPE_DIRECTIONALITY.md` §3 示例 C 已正确指出）。 |
| 7 裁决 | **`KEEP`**，但强制拆出「动机」与「行为」两个记录层。理由：[S15] 证明「照护动机」至少是 7 选 1 的向量；[S18] 证明「照护」整体适合 general + specific 的层级而非 4 个并列子量表。**表示建议**：单一有向坐标可接受（general 因子即「总照护倾向」），但**不得**在诊断时把 4 个 specific 当 4 个独立状态读出；行为留在 `Action/Event` 层，动机缺失时写 `motive_attribution: Unknown`，不填坑。 |

### 3.8 `Dedication`（及 commitment / investment / constraint 的区分）

| 维度 | 结论 |
|---|---|
| 1 语义边界 | **是**：i 主动希望维持、维护、继续该关系的**内在意愿**（long-term orientation、priority、sacrifice willingness、couple identity、**attraction-based 的 devotion / love / satisfaction**——后者是 [S05] 的第一个维度，必须注意）。**显式不是** Investment、Alternatives、Satisfaction、Constraint commitment、Bonding / Agreement（制度约束）、Behavior。**[S05] 的三分必须被显式采用**：attraction-based（含 satisfaction）/ moral-normative（个人责任感 + 婚姻作为社会宗教制度的重要性信念）/ constraining（终止的社会、财务、情感成本）。 |
| 2 最近邻构念 | Satisfaction（最强预测因子）；Investment；Quality of alternatives；Constraint commitment（6 个子量表 [S06]）；Commitment Inventory 的 dedication 子量表 [S06]；Dimensions of Commitment Inventory [S05]。 |
| 3 反例解耦 | **A 高 B 低**：初识即网络异地、毫无共同资产却「想一辈子」。**B 高 A 低**：多年共同财产 / 孩子后「想走」。**A 高 B 低（Dedication 高、Constraint 低）**：自愿但可随时离开的关系。**B 高 A 低**：困在关系里。**关键**：Satisfaction 高而 Dedication 低真实且高频——若 Satisfaction 降为 DERIVED，就必须解释 Dedication 如何**先于** satisfaction 变化。 |
| 4 测量族 | Investment Model Scale（4 因子）[S03]；Commitment Inventory / Revised Commitment Inventory（dedication + 6 constraint；320 对未婚伴侣 dyadic CFA 拟合良好）[S06]；Dimensions of Commitment Inventory（6 studies, N=1,787）[S05]。 |
| 5 时间行为 | 惯性中等；受沉没成本单向抬升（constraint 的作用）。`commitment <-> 后续 stay/leave` r = .47 [S01]。 |
| 6 范围 / 方向性 | 严格 dyad-directed。跨形态同构（[S02] 报告性别 / 族裔 / 性取向 / 时长的影响很小，但承认部分条件下会改变关联强度）。在「无法解除」的关系（法定亲子）中 constraint 极高而 dedication 极低——LHRM 必须能表达。 |
| 7 裁决 | **`KEEP`（定义为 `Dedication`）**。**但附一条 prior report 与 `PARAMETER_CONVERGENCE_V0_1.md` 都未处理的要求**：attraction-based 维度**包含 satisfaction**。这意味着若 §9 R3 把 Satisfaction 定为 DERIVED，则 Dedication 的一个组成落在 DERIVED 层 -> **同一语义被两个层级同时占用**。**必须由 Architect 裁决的内部不一致**（见 §7 Delta #3）。 |

### 3.9 `OutcomeDependence`

| 维度 | 结论 |
|---|---|
| 1 语义边界 | **是**：i 的重要结果 / 福利 / 机会 / 生活状态在多大程度上取决于 j **以及这段关系的存续**。**显式不是** Attachment dependency（复合 reliance + trustworthiness [S17]）、Constraint commitment（退出成本，是 dependence 的后果 / 成分）、Power（派生）、Need / Loneliness（person 层）、Emotional reliance（临床构念）。**必须 domain-indexed**（同 Trust）。 |
| 2 最近邻构念 | Interdependence Theory [S30]；Situational Interdependence Scale（[S28] 的 mutual dependence / power / conflict / future interdependence / information certainty 五维）；Erber & Fiske (1984)（`10.1037/0022-3514.47.4.709` [S29]）；Attachment dependency [S13]；Power。 |
| 3 反例解耦 | **A 高 B 低**：经济完全依附但关系痛苦。**B 高 A 低**：两个经济独立的人选择在一起。**A 高 B 低（Dependence 高、Dedication 低）**：「没能力离开」。**额外反例** [S28]：人们**无法可靠知觉**互依理论中的 coordination 一维（题项交叉载荷、含反向题也正相关）——这是「我以为我很依赖」与「我确实很依赖」之间的**结构性知觉鸿沟**，不是噪声。 |
| 4 测量族 | **关系级无被广泛接受、可比、验证过的 outcome dependence 量表。** 存在的是：(a) **情境级** SIS [S28]（30 题 5 维，跨实验室游戏情境验证：Dictator game vs Prisoner's Dilemma 的知觉区分正确；但**不是关系级**）；(b) Investment Model 的 satisfaction + alternatives（**是代理，不是 dependence 本身**；[S01] / [S02] / [S03] 均只测那四个）；(c) 早期实验室操纵范式 [S29]。**[S28] 原文明确**：已有 mutual dependence / conflict / power 的量表，但 no instrument has been [developed to measure all sub-dimensions of interdependence]——同时该研究发现 coordination 维不可可靠知觉。 |
| 5 时间行为 | 结构上慢、变化上可慢可快（法律 / 移民 / 健康 / 育儿结构 vs 失业 / 生病 / 被捕 / 被家暴）。**`CITED_SECONDARY`**：转述 [S28] 引述的日常情境 ESM 证据称浪漫伴侣在互依知觉上 strongly agree，作者据此认为这些知觉 rooted in an interpersonal reality（**Columbus et al. 2019 原文献本轮未直接核验**）。若成立，这是全部 13 个候选中**唯一一条**把「这是共享现实结构而非个人建构」说清楚的证据。 |
| 6 范围 / 方向性 | 严格 dyad-directed + **domain-indexed + 近似不可逆**。power = dependence 的不对称，但 **power != dependence**。 |
| 7 裁决 | **`KEEP`，但必须标 `MEASUREMENT_INFEASIBLE_AT_RELATION_LEVEL`**。这是本文最重要的判定。理论地位最硬（是 Rusbult 体系的理论地基），结构方向性最清晰，且是**唯一有可能支撑 `Power` 派生的候选**（若降级，§9 R2 的 `PowerImbalance = f(...)` 就失去全部输入）。但测量现状是：关系级无验证量表；情境级量表存在且其中一维不可知觉；两次 meta 都不测它。**建议的处理不是「删」**：(i) 保留为候选，但明确当前只能**结构化估计**（Agent 资源 / 替代 / 制度约束 + 事件证据）而非问卷估计；(ii) 引入 `domain` 索引；(iii) 显式登记 coordination 不可知觉为该坐标的**已知系统误差源**；(iv) 在 Case Bank 中把「我对你的依赖」与「我以为我依赖你」分列为两种 provenance，不得互替。 |

### 3.10 `Satisfaction`（争议项）

| 维度 | 结论 |
|---|---|
| 1 语义边界 | **是**：i 对当前关系结果与**自己的比较基线**之差的主观评价（outcome - CL）[S30]。**显式不是** Dedication、Love、关系质量总分、ValueCongruence、person 层生活满意度。**定义上它就是一个差值**——这是归 DERIVED 的最强理由。 |
| 2 最近邻构念 | Comparison level [S30]；Commitment（r = .65–.68）；Perceived partner responsiveness（低 PPR 伴随低 satisfaction [S33]）；Relationship quality；Life satisfaction。**批评簇（弱证据）**：relationship satisfaction 被批评 too individualistic、inappropriately unidimensional, insensitive to variation in the upper range of relationship quality、非西方文化中的相关性被质疑（**`CITED_SECONDARY` 转引；被引的 Galovan et al. 2021 与 Sanri et al. 2021 原文本轮未核验，不得作为强证据**）。 |
| 3 反例解耦 | **A 高 B 低**：高满意低承诺。**B 高 A 低**：低满意仍不离。**A 低 B 低**：退出前夜。**关键方法学反例** [S36]：配对数据中关系行为的跨伴侣 agreement 只有 avg r = .18–.19，而 projection 高达 r = .77–.90——双方看到的不是同一个「关系质量」，而是各自把自己的行为投射给对方。这意味着 satisfaction 作为「关系的属性」在测量上根本不成立。 |
| 4 测量族 | Couples Satisfaction Index（Funk & Rogge 2007, 32 题，`NO_DOI_VERIFIED`）；Marital Satisfaction Questionnaire（Lavner, Karney & Bradbury, `NO_DOI_VERIFIED`）；各短版。**测量是单人做的，这一点是共识。** |
| 5 时间行为 | state-trait 混合：对近期事件反应快，但比较基线 CL 极慢（甚至终身）。[S01] / [S02] 的横断面相关无法区分这两层。 |
| 6 范围 / 方向性 | **不是 pair 属性，是 person-directed 的评价**（`Satisfaction_i(about D_ij)`）。[S36] 与 [S15] 都指向这一点。 |
| 7 裁决 | **`DERIVED`（维持 §9 R3 判定），但附时序保留**。支持 DERIVED：(a) 定义上是差值；(b) 测量上是 person 层且投射污染严重；(c) 它是 Dedication 的**输入**而非独立状态。**保留意见（必须写进正文）**：investment model 的路径图把 satisfaction 放在 commitment **上游**。若把 satisfaction 完全降为 readout，就无法表达「满意度先跌、commitment 后跌」这一时间顺序，而这在现实里常见且可观察——LHRM 的轨迹导向需要一个能先行下降的量。**建议**：把 `Satisfaction` 建模为 `DerivedEvaluation`（带显式 `comparison_baseline` 与 `observation_time`），**不禁止**它被下游转移引用，但**禁止**它进入 `DirectedRelationshipState` 的 primitive 集合。 |

### 3.11 `Cohesion / We-ness`（争议项）

| 维度 | 结论 |
|---|---|
| 1 语义边界 | **是**：二人被体验 / 表述为一个共同体（「我们」、共享身份、相互纳入自我、couple identity）。**显式不是**接触频率（observable）、AttachmentSecurity、Intimacy（过程结果）、Dedication（维持意愿）、Satisfaction、Relationship identity / label（制度事实）。**关键问题**：是否存在独立于双方各自知觉的 pair latent？ |
| 2 最近邻构念 | IoS [S19]（**单题图示**）；RCI [S20]（**已内含 interdependence** -> 会与 `OutcomeDependence` 争语义）；`we-talk` 语言编码（`NO_DOI_VERIFIED`）；`Group cohesiveness`（主要是实验室小组文献，**与二人 dyad 不同层级**）。 |
| 3 反例解耦 | **A 高 B 低（We-ness 高、Dedication 低）**：习惯性共同生活但随时可分。**B 高 A 低**：责任 / 契约维持的异地、各自独立。**双方 we-ness 严重不一致**：一方视关系为「唯一的家」，另一方视其为「需要维护的责任」（`PARAMETER_CONVERGENCE_V0_1.md` §6 P1 已提出）。**方法学反例**：IoS / RCI 都是单人自陈，双方都自陈高时，模型无法区分「真共同体」与「两人各自的正向投射」（[S36] 的 projection r = .77–.90）。 |
| 4 测量族 | IoS（单题）[S19]；RCI [S20]；We-ness 语言编码；Investment Model Scale 把 IoS 当与 commitment 中度相关的指标 [S03]。**没有任何被广泛接受的 pair-level cohesion 量表——因为无法在不看两人的情况下测 pair latent。** |
| 5 时间行为 | 慢。形成期快、稳定后极慢衰减。IoS 与 IM commitment 中度相关，但 IM 四成分与 personal dispositions 基本无关 [S03]。 |
| 6 范围 / 方向性 | **本次审计中唯一存在层级归属争议的候选**。§6 P1 已正确标为 contested scope 并只允许 `PerceivedWeNess_A / _B` 两种表示。 |
| 7 裁决 | **`BELIEF_ONLY`（当前阶段）**——采纳 §6 P1 的保守表示，**不**承认独立于双方知觉的 `Cohesion_(A,B)` primitive。强制理由：(a) 所有可用工具都是单人自陈，最具代表性的 IoS 甚至是**单题**；(b) 投射量级（r = .77–.90）与 agreement 量级（r = .18–.19）不成比例，无法从「双方都高」推断「pair latent 高」；(c) RCI 已内含 interdependence。**升级条件**：出现独立的 pair-level 观测通道（第三方编码 / 共同叙事），且纵向数据显示 `Cohesion_pair` 在已知 `PerceivedWeNess_A, _B` 之上仍有稳定增量信息。 |

### 3.12 `PPR` / `Perceived Commitment` as `Belief`

| 维度 | 结论 |
|---|---|
| 1 语义边界 | **是**（PPR）：i 感到 j 理解、认可、在乎自己的需要与核心自我（understood / validated / cared for）[S33]。**显式不是** j 的实际回应行为（`ResponsiveAction_(j->i)`，Action 层）；Trust；Caregiving（发送侧）；Intimacy（过程累积结果）。**是**（`Belief_i(Dedication_(j->i))` 等）：i 关于 j 的有向状态的一阶信念——**不是新构念，是同一构念 + belief index**。 |
| 2 最近邻构念 | Perceived partner responsiveness [S33, S34]；Perceived social support（批评簇见 S41）；Responsiveness behavior（Action 层）；Feeling understood / validation；Comfort / intimacy（prior report C05, DERIVED）。**争议**：[S34] 摘要开篇即写 people's perceptions of being understood are only modestly related to actually being understood by others——这**直接支持**把 PPR 放在 Belief 层而不是 state 层。 |
| 3 反例解耦 | **A 高 B 低（PPR 高、实际 responsiveness 低）**：熟练共情但无真诚（可被用于操控）；[S33] 引述 projections of responsiveness。**B 高 A 低（实际 responsiveness 高、PPR 低）**：亚洲文化中行为性支持多于言语性支持 [S33 引 Kim et al. 2008]。**`Belief_i(Dedication_(j->i))` 的反例**：j 的 dedication 客观下降但 i 完全未察觉 -> belief 高、state 低；反向亦然。 |
| 4 测量族 | PPR / PPRS（Reis et al.；[S33] 章节综述，**具体量表题录本轮未核验**）；Perceived partner responsiveness scale（PsycTESTS 记录存在，**DOI 未核验**）；Perceived Support 测量群。**关键经验警告** [S15]：partner-reported trust 跨伴侣一致性 r = .11（ns）——**PPR 的双人一致性可能同样很低，但本审计未找到直接测量 PPR 一致性的元分析，标 UNVERIFIED。** |
| 5 时间行为 | 双成分：belief 层在分钟–日尺度上可极快波动（[S33] 章节引用的研究使用日记法检验 daily fluctuations in PPR）；state 层（若假设存在）慢。**这是把 PPR 放 Belief 层的又一理由。** |
| 6 范围 / 方向性 | PPR 是 `BeliefState_i` 关于 `j` 的内容，**不需要新的有向 primitive**。`Belief_i(Dedication_(j->i))` 复用既有构念——**这是 LHRM 现有的、也是本审计明确支持的设计**（`PARAMETER_CONVERGENCE_V0_1.md` §5 B2）。 |
| 7 裁决 | **`BELIEF_ONLY`（PPR 与 Perceived Commitment 均是）**。强制理由：[S34] + [S33] 共同说明 PPR 是**对状态的解释**，不是状态本身；而 [S33] 同时把 PPR 定位为 trust 与 commitment 的**上游生成器**（mutual cyclical growth），这进一步说明它应当是**一个独立的 belief 变量**，而不是任何有向状态的重复命名。**附加**：PPR 不应被降为「某个别的构念的 proxy」——prior report §4.C04 判 `KEEP（作 PS）`，本审计认为那是把 belief 误标为 primitive 的典型错误。 |

---

## 4. 裁决速览表

| # | 构念 | 裁决（`RESEARCH_CANDIDATE`） | 关键附加条件 | 决定性证据 |
|---|---|---|---|---|
| 1 | `Liking` | `KEEP` | 必须三分解（person / target / edge） | [S40] relationship variance 最大 |
| 2 | `RomanticAttraction` | `KEEP` + 边界 `OPEN` | Fisher 三系统降级为 mechanism_evidence；登记 Bode (2023) 拆分提议 | [S21] [S26] |
| 3 | `SexualDesire` | `KEEP` | 强制 `measurement_channel` 字段；与 PhysiologicalArousal 分坐标 | [S23] 男 .66 / 女 .26 |
| 4 | `Trust` | `KEEP` | 强制 `domain` 索引；零/短程边为 `Unknown` 而非低值 | [S10] domain-specificity |
| 5 | `Distrust` | **`OPEN`**（强烈倾向 `DERIVED`） | 先做 domain 索引 Trust + `ambivalent` 标记 | [S09] vs [S10]；反向计分 artifact |
| 6 | `AttachmentSecurity` | `KEEP` + `CONTESTED` | person / edge 双层；**保留 (anxiety, avoidance) 原始二维** | [S12] 30–40% vs 5–15%；[S11] r=.09；[S39] [S44] |
| 7 | `Caregiving` | `KEEP` | 动机 / 行为双层；不得把 4 个 specific 当独立状态读出 | [S15] 7 维动机；[S18] bifactor |
| 8 | `Dedication` | `KEEP` | 必须声明是否含 satisfaction 成分（否则与 §9 R3 冲突） | [S05] 三来源；[S01] [S02] 两次 meta |
| 9 | `OutcomeDependence` | `KEEP` + **`MEASUREMENT_INFEASIBLE_AT_RELATION_LEVEL`** | domain 索引；登记 coordination 不可知觉为系统误差源；两种 provenance 不得互替 | [S28] 关系级无工具 |
| 10 | `Satisfaction` | `DERIVED`（`DerivedEvaluation`） | 保留时序能力（可被下游转移引用）；不进 primitive 集合 | [S30] 差值定义；[S36] projection .77–.90 |
| 11 | `Cohesion / We-ness` | **`BELIEF_ONLY`** | 采纳 §6 P1 的 `PerceivedWeNess_A / _B`；设升级条件 | [S19] IoS 单题；[S36]；[S20] RCI 含 interdependence |
| 12 | `PPR` | **`BELIEF_ONLY`** | 禁止作为任何有向状态的 proxy | [S34] 感知 vs 实际只中度相关 |
| 13 | `Perceived Commitment` | **`BELIEF_ONLY`** | 用 `Belief_i(Dedication_(j->i))`，不新建构念 | `PARAMETER_CONVERGENCE_V0_1.md` §5 B2 |

---

## 5. 文献自身被争议之处 / 心理测量再分析的威胁

> 本节是本文的核心产出之一：记录**文献在哪些地方自己不确定**，而不是只记录结论。

### 5.1 依恋的两种方法学文化几乎不重合

- [S11]（Roisman et al. 2007, *JPSP*）：AAI security 与自评 attachment 维度 mean **r = .09**（trivial-to-small），N = 961。
- [S44]（Fraley & Roisman 综述）：Attachment security in adulthood is **not profitably conceptualized as a single, monolithic construct**；两类工具虽「represents the underlying structure of adult attachment similarly」，但「measures of attachment vary in a number of important ways that are not yet well understood」，且**不同方法测到的形式实证重叠弱，却与不同的结果变量相关**。
- [S39]（Fraley 测量页）：依恋四分类在不同测量下类别占比差异很大，the categories do not seem to be "real" except as regions in a two-dimensional space。
- [S12]（Sibley et al. 2005）则是**反向**证据：ECR-R 3 周 latent 稳定 85% 共享方差，且相对家人朋友高度对象特异（30–40% vs 5–15%）。
- **净结论**：支持「对象特异的边状态」（[S12]），但说明**依恋测量的构念边界本身处于争议中**。`AttachmentSecurity` 必须是全 basis 中**不确定度最高**的坐标。

### 5.2 「单一 security 标量」是建模决定，不是文献事实

ECR-R 的规范口径是**两个**维度：anxiety 与 avoidance（[S12]；Fraley 的 measures 页把 avoidance 的两个成分命名为 Discomfort with Closeness 与 Discomfort Depending on Others）。「安全」在这个二维空间里是**第四象限的一个区域**，不是一个连续标量。§5.1 的三条反对证据合起来说明：LHRM 若以单标量使用它，其值完全依赖于对 (anxiety, avoidance) 的投影选择，而这个投影选择在文献中没有共识。**若要用它，必须显式声明投影规则并保留原始二维。**

### 5.3 爱 / 浪漫的类型学在因子层面反复失败

- [S21]（Berscheid 2010）记载 Hendrick & Hendrick (1989) 合并多套 love 量表做因子分析，**未复现任一既有分类结构**。
- [S22]（Hendrick & Hendrick 1986）的 LAS 得到 6 个干净因子，但那是 **love 态度风格**（attitudes），不是关系状态——两者被日常语言与 prior report §4.G07 混在一起。
- 后果：LHRM 若以「爱是复合物」为由保留 8 维有向基，等于**默认了一个已被否证的心理类型学承诺**（见 §2.3）。

### 5.4 Fischer 三系统理论的正面对撞

- [S25]（Fisher 1998）是三系统理论的原始出处。
- [S26]（Bode 2023, *Frontiers in Psychology*）系统性质疑其「三系统独立演化」框架，主张 `courtship attraction` / `bonding attraction` 二分，并称 sexual desire 与两个 attraction 系统协作紧密到「应被当作单一现象（romantic love）」；Bode 同时指出 Fisher 后期工作与「三系统日益独立」的说法自相矛盾。
- **对 LHRM 的直接后果**：`RomanticAttraction` 与 `SexualDesire` 的分离**不是无争议的**。本审计仍建议 KEEP 两者（临床上真实存在解耦），但必须把 [S26] 登记为强反对意见，并承认「分离的理由」目前部分是**临床描述性的**而非机制性的。

### 5.5 trust / distrust 的单极 vs 双极之争（30+ 年未决）

- [S09]（Lewicki, McAllister & Bies 1998, *AMR*）明确主张 trust 与 distrust 是可分别变化、可共存的二维。
- [S10]（Schoorman, Mayer & Davis 2007, *AMR*）走相反方向，主张 trust 单维、domain-specific。
- **方法学隐忧（`MODEL_HYPOTHESIS`）**：distrust 的很多操作化是信任题目的反向计分，而反向计分题在因子分析中天然分离出第二个因子。这意味着部分「trust / distrust 二维」证据可能是**方法学 artifact 而非构念事实**。

### 5.6 测量通道的性别差异会污染 SexualDesire

[S23]：132 项研究（1969–2007），2,505 名女性 / 1,918 名男性，**男性自我报告–生殖器反应一致性 r = .66，女性 r = .26**；调节变量为 stimulus variability 与自我报告的评估时机。如果 LHRM 在 `SexualDesire` 坐标上不携带 `measurement_channel`，任何跨性别 / 跨文化的比较都在比较「通道差异」而不是「状态差异」。**这是一个可以用 0 额外数据避免的设计错误。**

### 5.7 Caregiving 的 bifactor 重分析

[S18]：N=912 智利受试者，bifactor（2 general + 4 specific）优于 Kunce & Shaver 的 4 维正交结构。把 `Caregiving` 当 4 个并列状态会重复计数 general 因子。LHRM 用单一有向坐标作为表示是可以的（general 因子就是「总照护倾向」），但**不得**在诊断 / 解释时把 4 个 specific 当作 4 个独立状态读出。

### 5.8 Caregiving 的跨伴侣一致性远低于 assumed

[S15] 报告 caregiver 报告与 recipient 报告在 satisfaction 上只有 r = .43（中等），在 relationship trust 上只有 r = .11（ns）。**`Caregiving` 不能被建模为一个「双方共享的关系属性」。** 它是一个 person-directed 坐标，且接收侧的实际体验有相当大的一部分不来自照护者。

### 5.9 PPR 的知觉-实际鸿沟（Belief 层化的直接证据）

[S34]：people's perceptions of being understood are only modestly related to actually being understood by others。
[S33]：PPR reflects both actual partner behavior and motivated reinterpretations。
两者共同说明 PPR 是 belief，不是 state。

### 5.10 Satisfaction 的测量批评簇（**弱证据，必须标注**）

relationship satisfaction 被批评 too individualistic、inappropriately unidimensional, insensitive to variation in the upper range of relationship quality、非西方文化中的相关性被质疑。这段批评是通过 Ayub et al. (2022) 的**转述**读到的，**被引的 Galovan et al. (2021) 与 Sanri et al. (2021) 原文本审计未核验**。本审计**不使用**该批评做任何裁决，只记录其存在与出处弱点。

### 5.11 本审计自身的方法学失败（自我记录）

- 3 条题录在 Crossref / OpenAlex / websearch 三路检索中**均未命中**：Campbell & Fiske (1959)、Hendrick, Fontaine & Swann (1978)、Overall, Simpson & Struthers (2017) 的 Commitment Inventory 修订版（实际命中的是 Owen et al. 2010）。
- 1 条 DOI 候选被**明确证伪**：`10.1037/h0040084` 并非 Campbell & Fiske，而是 Poole (1957)。
- 2 条 prior report 的记忆性错误被 Crossref 推翻：Rempel et al. 1985 的卷期（本应为 49(1):95–112，而非 48(1):22–35）、Aron et al. 1992 的 DOI 末位（`.596`，而非 `.589`）。
- **后果**：prior report §11「文献细节请在外部库核对」的免责是必要的；**任何不含 DOI 或未标注 `NO_DOI_VERIFIED` 的构念裁决都不应被当作可引用依据。**

---

## 6. 对 prior report 的 audit delta（复核而非重做）

| # | prior report 判定 | 本审计判定 | 变化 | 依据 |
|---|---|---|---|---|
| 1 | C02 `Distrust` = `KEEP（与信任分离）`，E2 | **`OPEN`（强烈倾向 DERIVED）** | **降级** | [S09] vs [S10]；反向计分方法学隐忧 |
| 2 | C04 `PPR` = `KEEP（作 PS）` | **`BELIEF_ONLY`** | **改层** | [S34] + [S33] |
| 3 | §9.2 `Satisfaction = DERIVED` + §7.4 `Commitment = dedication（含 satisfaction 成分）` | 两者并存 -> **内部不一致**，需二选一 | **发现冲突** | [S05] |
| 4 | B01 `Attachment security` = `KEEP`，E1 | **`KEEP` + `CONTESTED`**，要求 person / edge 双层且保留原始二维 | **加限定** | [S11] [S44] [S39]；支持侧 [S12] |
| 5 | C13 `Outcome dependence` = `KEEP`，E1 | **`KEEP` + `MEASUREMENT_INFEASIBLE_AT_RELATION_LEVEL`** | **加限定** | [S28]；[S01] [S02] [S03] 均未测 dependence |
| 6 | A02 `Romantic/Lustful attraction` = KEEP，标 C contested | **`KEEP` + 边界 `OPEN`**，Fisher 三系统降级为 mechanism_evidence | **降级机制地位** | [S26] |
| 7 | B05 `Cohesion/we-ness` = `KEEP（作 PS）` | **`BELIEF_ONLY`（当前阶段）** | **改层** | [S19] + [S14]；[S36]；[S20] |
| 8 | A01 `Sexual desire` = KEEP | **`KEEP` + 强制 `measurement_channel`** | **加条件** | [S23] |
| 9 | B04 `Caregiving` = KEEP，E2 | **`KEEP`**（+ 动机 / 行为双层） | **维持 + 细化** | [S15] [S18] |
| 10 | C01 `Trust` = KEEP | **`KEEP` + 强制 `domain` 索引** | **加条件** | [S10] |
| 11 | 全文无 DOI，§11 声明「文献细节请在外部库核对」 | 建议改为：**无 DOI 或未核验 DOI 的指针不得作为裁决依据** | **流程修订** | §5.11 |
| 12 | 用 `E1/E2/E3/C/M` 分级，无机制记录「是否读到原文」 | 建议叠加 `CITED_PRIMARY / CITED_SECONDARY / AGENT_RECALL / NO_DOI_VERIFIED` 正交标记 | **流程修订** | §1.2 |

**未发现需推翻 prior report 的项**：C08 commitment 的 `KEEP/REDEFINE` 方向正确（但需换独立性论证理由，见 §2.4）；C14 power 作为 dependence 不对称的派生、B02 felt security 并入 B01、B07/C07 降为 proxy、Alignment 拆为 value / goal congruence 三项均站得住。

---

## 7. 明确不主张什么（explicit non-claims）

1. **不主张修改 canonical ontology。** 每一个「裁决」都是 `RESEARCH_CANDIDATE`，等待 Human / Architect 仲裁。本文不构成对 `PARAMETER_CONVERGENCE_V0_1.md` 的任何改写。
2. **不主张任何数值、权重、距离、概率、阈值、转移函数、范式。** 报告中的 r、方差比例、类别占比全部是**文献报道值**，不构成 LHRM 的任何参数建议。
3. **不主张任何构念在 LHRM 中已经 validated。** `KEEP` 只意味着「通过本审计施加的条件」，不等于「已通过 representation coverage regression / redundancy test / 纵向验证」（那仍是 `PARAMETER_CONVERGENCE_V0_1.md` §15 Gate A–C 的任务）。
4. **不主张 literature count 或 LLM agreement 构成验证。** 本文记录了 3 条检索失败、1 条 DOI 证伪、2 处记忆性错误被推翻，正是为了说明文献条数本身不是证据。
5. **不主张把任何 AI / 研究建议升格为 Human requirement。**
6. **不主张 Fischer 三系统理论成立或不成立。** 本文只说明该理论处于公开争议中（[S25] vs [S26]），并把 LHRM 对它的依赖降级为 `mechanism_evidence`。
7. **不主张 evolutionary / neuroendocrine 机制可作为关系状态的定义。** 与 AGENTS.md 的「机制 != 状态」一致。
8. **不主张任何动物、跨物种证据外推到 Human–Human dyad。** 与 `CURRENT_ARCHITECTURE.md` §2 一致。
9. **不主张 Galovan et al. (2021) 或 Sanri et al. (2021) 的具体结论**（§5.10）；只以二级转述形式出现，未用于任何裁决。
10. **不主张 Campbell & Fiske (1959) 与 Hendrick, Fontaine & Swann (1978) 的任何内容**（§5.11）；题录未核实，只作为待补指针。
11. **不主张 Satisfaction 应当被删除。** 建议的是分层（`DerivedEvaluation`）而非删除。
12. **不主张 `Distrust` 应当被删除。** 建议的是 `OPEN` + 决定性实验，而非删除。
13. **不主张 8 维 basis 是「人类关系只有八维」。** 与 `PARAMETER_CONVERGENCE_V0_1.md` §11 一致；本文只是指出保留 8 维的**论证**需要更换（见 §2.3）。
14. **不主张「缺少双向高相关数据」就是「没有 pair latent」。**
15. **不主张本审计的 `OPEN` 判定是终局。** 每一处 `OPEN` 都附了具体的判定实验（见 §9）。

---

## 8. 剩余未知（remaining unknowns）

| # | 未知 | 为什么重要 | 需要什么才能定 |
|---|---|---|---|
| U1 | `AttachmentSecurity` 的**边层增量**是否超出 person 层（anxiety, avoidance） | 若不超出，8 维中的 1 维实际冗余 | 对象特异的纵向设计 + APIM 或随机截距模型 |
| U2 | `Satisfaction -> Dedication` 的**时间顺序**是否真的存在 | 若存在，Satisfaction 不能纯降为 readout | 交叉滞后或日级 / 周级 longitudinal，控制先前底层状态 |
| U3 | `Distrust` 是否在**同一 domain 内**可与 `Trust` 同时高 | 决定 Distrust 是独立坐标还是派生量 | 非反向措辞的独立题目在同一 dyad 上同时测两维 |
| U4 | `Cohesion` 是否存在独立于双方知觉的 **pair latent** | 决定它是 PairState 还是两个 Belief | 独立于双方的 pair 级观测通道（第三方编码 / 共同叙事 / we-talk 跨评分者信度） |
| U5 | `OutcomeDependence` 的**关系级**可测性 | 决定 `Power` 能否被派生 | 关系级 dependence 量表 + 跨实验室信度；`coordination` 维能否被稳定知觉 |
| U6 | `RomanticAttraction` 是否需拆 `courtship / bonding` | 决定 [S26] 的批评是否被实证支持 | 不预设分类的因子分析 + 跨文化复制 |
| U7 | Liking / Trust / PPR / Dedication / Satisfaction 在**同一 dyad 上同时测**时的联合结构 | 决定 8 维 basis 是否在统计上可区分 | 一个把 5 个构念放进同一多方法矩阵的研究 |
| U8 | `Caregiving` 的 general 因子与 `PPR` / `AttachmentSecurity` 的相关强度 | 决定照护是否可由受方感知完全预测 | APIM / mediation on dyads，跨 sexual orientation 复制 |
| U9 | `Liking` 的 `Unknown` 与 `低值` 的区分在 court-fact 文本中是否可判 | 直接影响 Case Bank 第一轮表示测试 | Case Bank Gate A 的实际映射结果 |
| U10 | 所有「跨形态稳定性」判断在 **same-sex / kin** 语境下是否真的一致 | `PARAMETER_CONVERGENCE_V0_1.md` §2.4 明确要求 | 每个构念各一次 same-sex 与 kin 的专门样本研究；本审计未覆盖 |
| U11 | 中文语境下这 13 个构念的**测量等价性** | LHRM 主要案例语料可能是中文 | 中文版 ECR-R / IoS / CQ 的测量不变性研究（本审计未找到） |
| U12 | `SexualDesire` 的「目标特异」在非西方 / 非二元性别样本中是否同样成立 | 决定该坐标能否跨文化使用 | [S23] [S24] 的调节变量在跨文化样本中的复制 |

---

## 9. 给 Human / Architect 的可执行建议（全部为 `RESEARCH_CANDIDATE`）

按「不需新数据即可执行」与「需新数据」分层：

### 9.1 不需新数据即可执行（表示层的纯表示决定）

| 建议 | 依据 | 影响 |
|---|---|---|
| `Trust` 与 `OutcomeDependence` 的 signature 加 `domain` 索引 | [S10] [S30] | 避免「四个不兼容标量取平均」 |
| `SexualDesire` 与 `PhysiologicalArousal` 分为两个坐标，且带 `measurement_channel` | [S23] | 避免跨性别 / 跨文化比较误读 |
| 所有 directed 构念的三分解（person / target / edge）进入 `StateCoordinate` 结构 | [S40] [CONSTRUCT_SCOPE_DIRECTIONALITY §1] | 防止 Agent 属性污染边状态 |
| `AttachmentSecurity` 保留 (anxiety, avoidance) 原始二维，单标量只作显式投影 | §5.2 | 避免在无共识的压缩上建立推理 |
| `Satisfaction` 移入 `DerivedEvaluation`（带 `comparison_baseline`），不进 primitive 集合 | [S30] [S36] | 解决 R3 与 Dedication 定义的重叠 |
| `Cohesion` 只保留 `PerceivedWeNess_A / _B`，不建 pair 坐标 | [S19] [S36] [S20] | 采纳 §6 P1 |
| `PPR` 移入 Belief 层，与 `ResponsiveAction_(j->i)` 分离 | [S33] [S34] | 修正 prior report 的层次错置 |
| `Caregiving` 行为留 Action 层，动机缺失写 `Unknown` | [S15] [S18] | 符合 AGENTS.md Validation discipline |

### 9.2 需新数据（优先级排序）

1. **U5** — 关系级 `OutcomeDependence` 量表。若无，`Power` 派生链必须改为 judgment-based 且显式标注。
2. **U7** — 5 构念同一多方法矩阵。这是 8 维 basis 的存亡检验。
3. **U1** — `AttachmentSecurity` 边层增量。8 维或 7 维的分水岭。
4. **U3** — `Distrust` 同 domain 双高。`Distrust` 的去留取决于此。
5. **U2** — satisfaction / dedication 时序。`Satisfaction` 分层方案的稳定性。
6. **U4** — pair-level cohesion 观测通道。
7. **U10 / U11 / U12** — 跨形态稳定性、中文测量等价性、跨文化目标特异性。

---

## 10. 引用清单（精选，按构念分组；DOI 已核验者标 ✓）

**承诺 / 投入 / 满意**
- Le, B., & Agnew, C. R. (2003). *Personal Relationships*, 10(1), 37–57. `10.1111/1475-6811.00035` ✓
- Tran, P., Judge, M., & Kashima, Y. (2019). *Personal Relationships*, 26, 158–180. `10.1111/pere.12268` ✓
- Rusbult, C. E., Martz, J. N., & Agnew, C. R. (1998). *Personal Relationships*, 5, 357–387. `10.1111/j.1475-6811.1998.tb00177.x` ✓
- Rusbult, C. E., & Van Lange, P. A. M. (2003). *Annual Review of Psychology*, 54, 351–375. `10.1146/annurev.psych.54.101601.145059` ✓
- Adams, J. M., & Jones, W. H. (1997). *JPSP*, 72(5), 1177–1196. `10.1037/0022-3514.72.5.1177` ✓
- Owen, J., Rhoades, R. K., Stanley, S. M., & Markman, H. J. (2010). *Journal of Family Issues*, 32(6), 820–841. `10.1177/0192513x10385788` ✓
- Agnew, P. A. M., Van Lange, P. A. M., Rusbult, C. E., & Langston, C. A. (1998). *JPSP*, 74(4), 939–954. `10.1037/0022-3514.74.4.939` ✓（摘要正文未读）
- Drigotas, S. M., Rusbult, C. E., Wieselquist, J., & Whitton, S. W. (1999). *JPSP*, 77(2), 293–323. `10.1037/0022-3514.77.2.293` ✓

**信任 / 不信任**
- Rempel, J. K., Holmes, J. G., & Zanna, M. P. (1985). *JPSP*, 49(1), 95–112. `10.1037/0022-3514.49.1.95` ✓（摘要正文未读）
- Lewicki, R. J., McAllister, D. J., & Bies, R. J. (1998). *Academy of Management Review*, 23(3), 438–458. `10.5465/amr.1998.926620` ✓
- Schoorman, F. D., Mayer, R. C., & Davis, J. H. (2007). *Academy of Management Review*, 32(2), 343–356. `10.5465/AMR.2007.24348410` ✓

**依恋 / 照护**
- Roisman, G. I., Holland, A. S., Fortuna, K., Fraley, R. C., Clausell, E., & Clarke, A. M. (2007). *JPSP*, 92(4), 678–697. `10.1037/0022-3514.92.4.678` ✓
- Sibley, C. G., Fischer, R. D., & Liu, J. H. (2005). *PSPB*, 31(11), 1524–1536. `10.1177/0146167205276865` ✓
- Collins, N. L., & Read, R. R. (1990). Adult Attachment Scale. `10.1037/t01997-000` ✓
- Feeney, B. C., & Collins, N. L. (2001). *JPSP*, 80(6), 972–994. `10.1037/0022-3514.80.6.972` ✓
- Feeney, B. C., & Collins, N. L. (2003). *PSPB*, 29(7), 950–968. `10.1177/0146167203252807` ✓
- Collins, N. L., & Feeney, B. C. (2000). *JPSP*, 78(6), 1053–1073. `10.1037/0022-3514.78.6.1053` ✓（摘要正文未读）
- Carnelley, K. B., Pietromonaco, P. R., & Jaffe, K. (1996). *Personal Relationships*, 3(3), 257–278. `10.1111/j.1475-6811.1996.tb00116.x` ✓
- Guzmán-González, M., Calderón, D. F., Murray, S. B., Henríquez, G. (2020). *IJERPH*, 17(24), 9306. `10.3390/ijerph17249306` ✓
- Fraley, R. C. (n.d.). *Measures*. https://labs.psychology.illinois.edu/~rcfraley/measures/measures.html ✓
- Roisman, G. I., & Fraley, R. C. (2019). Adult attachment: Toward a rapprochement of methodological cultures. `10.1111/j.1467-8721.2009.01621.x` ✓

**互依 / 依赖 / 权力**
- Kelley, H. H., & Thibaut, J. W. (1978). *Interpersonal Relations: A Theory of Interdependence*. Wiley. （无 DOI；经同期书评确认存在）
- Gerpott, T. H., Balliet, D., Columbus, J., Molho, M., & de Vries, R. E. (2018). *JPSP*, 115(5), 716–742. `10.1037/pspp0000166` ✓
- Erber, R., & Fiske, S. T. (1984). *JPSP*, 47(4), 709–726. `10.1037/0022-3514.47.4.709` ✓（摘要正文未读）

**吸引 / 欲望 / love 类型学**
- Fisher, H. E. (1998). *Human Nature*, 9(1), 23–52. `10.1007/s12110-998-1010-5` ✓
- Bode, A. (2023). *Frontiers in Psychology*, 14. `10.3389/fpsyg.2023.1176067` ✓
- Chivers, M. L., Seto, M. C., Lalumière, M. L., Laan, E., & Grimbos, T. (2010). *Archives of Sexual Behavior*, 39(1), 5–56. `10.1007/s10508-009-9556-9` ✓
- Chivers, M. L. (2017). *Archives of Sexual Behavior*, 46(4), 1213–1221. `10.1007/s10508-017-1015-4` ✓
- Berscheid, E. (2010). *Annual Review of Psychology*, 61, 1–25. `10.1146/annurev.psych.093008.100318` ✓
- Hendrick, C., & Hendrick, S. (1986). *JPSP*, 50(2), 392–402. `10.1037/0022-3514.50.2.392` ✓

**接近 / 凝聚 / 回应**
- Aron, A., Aron, E. N., & Smollan, D. (1992). *JPSP*, 63(4), 596–612. `10.1037/0022-3514.63.4.596` ✓
- Berscheid, E., Snyder, M., & Omoto, A. M. (1989). *JPSP*, 57(5), 792–807. `10.1037/0022-3514.57.5.792` ✓（摘要正文未读）
- Reis, H. T., & Clark, M. S. (2013). Responsiveness. In *Oxford Handbook of Close Relationships*. ✓
- Ackerman, S. J. (2021). *Social and Personality Psychology Compass*. `10.1111/spc3.12308` ✓
- Maisel, N. C., & Gable, S. L. (2009). *Psychological Science*, 20(8), 928–932. `10.1111/j.1467-9280.2009.02388.x` ✓
- Bolger, N., & Amarel, D. (2007). *JPSP*, 92(3), 458–475. `10.1037/0022-3514.92.3.458` ✓
- Neff, L. A., & Karney, B. R. (2005). *JPSP*, 88(3), 480–497. `10.1037/0022-3514.88.3.480` ✓
- Overall, J. A., Fletcher, G. J. O., & Simpson, J. A. (2010). *PSPB*, 36(11), 1496–1513. `10.1177/0146167210383045` ✓

**满意 / 配对一致性 / 方法学**
- Zimmer-Gembeck, M. J., & Ducat, W. (2010). *Journal of Adolescence*, 33(6), 879–890. `10.1016/j.adolescence.2010.07.008` ✓
- Appelbaum, M., Cooper, H., Kline, R. B., Mayo-Wilson, E., Nezu, A. M., & Rao, S. M. (2018). *American Psychologist*, 73(1), 3–25. `10.1037/amp0000191` ✓
- The Development of the Liking Gap. *Psychological Science*. `10.1177/0956797620980754` ✓（题录部分核实）

**未核实指针（`NO_DOI_VERIFIED` / `AGENT_RECALL`）**
- Campbell, D. T., & Fiske, N. (1959). *JASP*, 55(2), 77–98.（三路检索未命中；候选 DOI `10.1037/h0040084` 已证伪）
- Hendrick, C., Fontaine, R., & Swann, W. B. (1978). *JPSP*, 36(12), 1438–1444.（三路检索未命中）
- Overall, J. A., Simpson, J. A., & Struthers, J. J. (2017). Revised Commitment Inventory 修订版.（未命中；命中的是 Owen et al. 2010）
- Nestler, S., & Bruns, J. (2025). Meta-liking 准确性的纵向研究.
- Funk & Rogge (2007) Couples Satisfaction Index；Lavner, Karney & Bradbury Marital Satisfaction Questionnaire.
- Galovan et al. (2021)；Sanri et al. (2021)（仅经 Ayub et al. 2022 转述读到批评语）

> 证据分级（`CITED_PRIMARY` / `CITED_SECONDARY` / `AGENT_RECALL`）见 parent packet `R01_packet.md` §2 的 sources 表，该表应随本文一并 durable writeback。

---

*本文由 Research child lane R01 按 `youling/lhrm#30` overnight swarm Work Order 与 `00_CHILD_CONTRACT.md` 生成。不修改 canonical ontology；全部裁决为 `RESEARCH_CANDIDATE`，最终由 Human / Project Architect 仲裁。*
