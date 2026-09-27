# 14 论文定位 / 新颖性 / 审稿风险（R14）

```yaml
work_coordinate: youling/lhrm#30@overnight-opencode-exploration-swarm-v1
lane: R14
role: Research child
as_of: 2026-09-27
nature: RESEARCH_CANDIDATE — positioning risk assessment, NOT a claim of contribution
status: lane SUCCESS; novelty NEGATIVE_RESULT
```

## 0. 这份文件是什么，不是什么

**是：** 一份以「尽量不让自己项目过度声称」为目标的对抗性评估。把 LHRM 的每个架构主张放到既有文献面前，看哪些是复用、哪些可能新颖、哪些必须禁止说。

**不是：** 论文大纲、投稿计划、贡献声明、或任何形式的 endorsement。

**最重要的一句话：**

> LHRM 目前所有「有向关系状态构念」都能在 1970–2020 的成熟文献里找到对应的一等公民地位；LHRM 的潜在资产在**表示形式与失败判据**，而资产恰恰还**没有被形式化到能被检验的程度**。

## 1. 摘要（BLUF）

| 结论 | 强度 |
|---|---|
| LHRM 的 8 个有向构念**全部是 REUSE**，无一条可主张原创 | 高（逐条有 DOI） |
| LHRM 最有希望的贡献方向是**「以 N=1 个体的、逐句可审计的表示完备性为主指标」**，但目前**未形式化**，因此新颖性无法被审稿人识别 | 中 |
| 现实中 LLM×关系赛道已被 5+ 篇工作占据（RELATE-Sim、Love First Know Later、CogniPair、ConflictLens、Couple Agents） | 高 |
| 现有关系质量量表已能复现**二阶 quality 因子**（PRQC）与**四维**（IAS），LHRM 8 维从未与它们对照 | 高 |
| 「方向性」的文献基础比 LHRM 需要的更弱：partner effect 可能存在发表偏倚，且 partner 判断对满意度不增加信息 | 高 |
| **对 LLM 从文本抽多类关系语义，现有最强实证是 Kappa=.42（单会话文本、28 类）**；Eberhardt 2025 的 ω=.953 是**单维**构念，不可外推 | 高 |
| 投影到论文：**当前不存在诚实的 LHRM 投稿路径**；最短诚实路径 = M0–M5（5–7 个月单人） | 高 |

## 2. 明确是复用的（LHRM 不得主张原创）

### 2.1 逐项对照表

| LHRM 主张 | 既有出处 | 严重度 |
|---|---|---|
| `i->j` / `j->i` 分开建模，互惠由两方向派生 | **SRM**（Kenny & La Voie 1984；Back & Kenny 2010）：actor / partner / relationship effect 三成分分解。**APIM**（Cook & Kenny 2005, `10.1080/01650250444000405`）显式估计 actor effect 与 partner effect；Kenny (2018, `10.1111/pere.12240`) 称其为 dyadic 数据的「default method」 | 高 |
| `OutcomeDependence` 为结构变量、power 由依赖不对称派生 | **互依理论**（Kelley & Thibaut 1978）：dependence = 本关系结果 vs 最佳替代；power = 依赖不对称。Rusbult, Martz & Agnew (1998, `10.1111/j.1475-6811.1998.tb00177.x`) 已把这一族做成四构念量表 | 高 |
| `Dedication` 独立于 investment / alternatives / satisfaction / constraint | **Investment Model**：Le & Agnew (2003, `10.1111/1475-6811.00035`)，52 研究 / 11,582 人，三基共解释 commitment **61%** 方差；Tran, Judge, Kashima & Agnew (2019, `10.1111/pere.12268`)，202 样本 / 50,427 人，**54%** 方差 | 高 |
| `PPR` 属 Belief 层，responsive action 属 Action 层 | **Reis & Shaver (1988)** intimacy process model；Reis, Clark & Holmes (2004)：PPR = 理解 + 认可 + 在乎，且本身包含 motivated construal；Reis & Clark (2013)：responsiveness 比 self-disclosure 更近端 | 高 |
| `AttachmentSecurity` 为关系层状态、anxiety/avoidance 为 Agent 属性 | 这**就是** general vs relationship-specific attachment 二分：Klohnen et al. (2005)；**ECR-RS**（Fraley, Waller & Brennan 2000，21,000+ 人）；Hyland, Overall & Maddux (2015)：关系特异测量对关系内结果预测更好，一般性测量对人格预测更好 | 高 |
| 「爱 / 亲密 / 嫉妒不是 primitive，是组合态」 | **Sternberg (1986)** 三成分；Reis & Shaver (1988) 把 intimacy 定义为披露×响应的**过程结果**；Fletcher, Simpson & Thomas (2000, `10.1177/0146167200265007`) 用**二阶因子**实证确认 love/passion/commitment/intimacy/trust/satisfaction 之上存在共同高阶「relationship quality」因子 | 高 |
| 「Compatibility / 般配感 / Ideal standards match 不是 primitive」 | **Ideal Standards Model**：Fletcher et al. (1999, `10.1037/0022-3514.76.1.72`，ideal 伴侣 3 因子 + 理想关系 2 因子)；Fletcher & Simpson (2000, `10.1111/1467-8721.00070`，evaluation / explanation / regulation 三功能)；Fletcher, Simpson & Thomas (2000)（纵向 12 个月：ideal-perception consistency 预测更高 perceived quality 与**更低 dissolution rate**） | 高 |
| State / Observation / Belief 三分 | SRM 本身即把 perceiver 知觉作为独立数据源；APIM 有 actor measure 与 partner measure 两套；latent vs observed indicator 是测量模型传统的基本分层 | 高 |
| Relationship label 是 coarse readout | **Relational Models Theory**（Fiske 1992, `10.1037/0033-295X.99.4.689`）；Finkel, Simpson & Eastwick (2017, `10.1146/annurev-psych-010416-044038`) 的 14 原则之一已系统回答「relationship 是什么」 | 中 |
| Role 是 query lens 不是 world state | 与 Boyd & Heewer (2007) *Communication as a Modeling Activity* 的 modeling-activity 立场同源（**`AGENT_RECALL`，DOI 未核实**） | 中 |
| 「低冗余 / 最小充分基 / 反例解耦 / 条件增量 / 干预独立性」判据 | **通用构念效度检查清单的重写**：Cook & Messick (1979)、Messick (1989, 1995)、Trochim (1999) 的 content / discriminant / structural / external / generalizability 五检（**`AGENT_RECALL`**）。MSC 五条结构几乎一一对应，**且报告未引出处** | 高 |
| 不用预写关系状态机，改用连续/混合状态转移 | **Granic & Hollenstein (2003)** 的 attractor / perturbation / phase-transition 路线已明确反对离散关系标签；Feinberg, Xia, Fosco, Heyman & Chow (`10.1007/s11121-017-0803-3`) 已用**耦合振子模型**拟合伴侣互动轨迹 | 高 |
| 可向 ABM / microsimulation 扩展 | 已有 marriage-market ABM 且**已声称定量准确**：Hills & Todd (2008) MADAM, JASSS 11(4), `https://www.jasss.org/11/4/5.html`（声称准确预测初婚时长、初婚离婚比例、终生已婚比例，跨文化）；Billari (2005) Wedding Ring, `https://www.demographic-research.org/volumes/vol17/3/17-3.pdf`；JASSS 16(1):6 New Zealand marriage market | 高 |
| LLM 做定性编码 / 信息抽取可服务社会科学 | Zhang et al. (2024), arXiv `2401.15170`（GPT-4 κ≥.6 for 8/9 codes；GPT-3.5 mean κ=.34；CoT 使 GPT-4 平均 κ .59→.68）；QualiGPT, arXiv `2407.14925`；**Eberhardt et al. (2025), Scientific Reports, `10.1038/s41598-025-14923-y`**（LLM rating scale 已完成完整心理测量：1,131 会谈 / 155 患者，ω=.953、CFI=.968、SRMR=.022、**RMSEA=.108**） | 高 |
| E1/E2/C/M 证据分级 | GRADE / NIH levels of evidence / 领域 strong-moderate-weak 惯例 | 中 |
| 126 条 proxy 分解词典 | construct dissection 传统（Bristow, Wright & Beauchemin 1993 一脉）；operationalization 文献 | 中 |

### 2.2 关系质量测量 / 既有复合评分系统清单（对新颖性最关键）

| 系统 | 结构 | 出处 |
|---|---|---|
| **PRQC** | 6 一阶成分（satisfaction / commitment / intimacy / trust / passion / love）→ **一个二阶 overall perceived relationship quality 因子**；二阶模型 CFI=.92 vs「指标直接负载到单因子」CFI=.61 | Fletcher, Simpson & Thomas (2000), `10.1177/0146167200265007` |
| PRQC 整体指数 | 六成分均值，**α=.96**；各成分 α=.86–.96，相互 r=.36–.87 | Sakaluk et al. (2015) 复本 |
| **IAS** | 关系质量四维原型：**intimacy / agreement / independence / sexuality**；德、加两样本复本；intimacy 贡献最大、sexuality 最小 | Neubauer, Voss & Asendorpf (2015), `10.1111/1475-6811.00017` |
| **M-QoRS** | **bi-factor**：general factor「Quality of relationship」+ 4 域（Quality of communication / Conflict management / Feeling connected / Overall happiness）；N=745，ωH=.89 | McTaggart et al.（City Research Online 全文） |
| **RQ** | 26 题：commitment + mutual enjoyment +「right person」；英国社会学 practices approach | PMC6187488 |
| DAS / commitment | Dyadic Adjustment Scale（Spanier 1976）；Lund (1985) investment & commitment scales | 见 Fletcher et al. 2000 参考文献表 |
| Sternberg | 三角理论 intimacy / passion / commitment；并被 PRQC 的二阶结构支持 | Sternberg (1986) |
| Ideal Standards | 理想伴侣 3 因子 + 理想关系 2 因子 | Fletcher et al. (1999) |
| ECR / ECR-RS | anxiety + avoidance 两维；ECR-RS 加**关系特异性**索引 | Brennan, Clark & Shaver (1998)；Fraley, Waller & Brennan (2000) |
| 依恋分类 | secure / preoccupied / dismissing / fearful（Bartholomew 四类） | Roisman (2009), `10.1111/j.1467-8721.2009.01621.x` |
| Acitelli & Antonioni | 关系科学的维度化方案（页数/题名待核） | **`AGENT_RECALL` / `UNVERIFIED_DOI` — 最高优先 prior-art** |

**结论：不存在「无先例」的关系质量复合评分系统。** LHRM 唯一可能的差异化是：**拒绝输出分数**，并把「表示是否完备」而不是「分数是否准」当作问题。**这必须被写成明确的设计选择与代价，而不能被写成「更优」。**

### 2.3 现实中的 LLM×关系竞争工作（已占据的位置）

| 工作 | 定位 | 关键数字 |
|---|---|---|
| **RELATE-Sim**（arXiv `2510.00414`，投稿 CHI 2026；Yue, Xu, Gupta, Ha, Sharabi & Zhou） | Turning Point Theory + 双 LLM agent + Scene Master；每 scene 标注 **8 个可解释关系状态**；可审计 commitment 估计 | N=101：64.4% vs 基线 48.5%（exact binomial p=.005）；N=71 两年追踪，组间分离度 3× |
| **Love First, Know Later**（arXiv `2512.11844`） | LLM 同时充当 agent 与 environment；compatibility 形式化为 reward modeling / inverse RL；给出「LLM policy 逼近人类行为 ⇒ 匹配收敛到最优稳定匹配」的**定理** | speed dating + 离婚预测（170 对、54 题 Likert），基线为 survey 特征 logistic regression |
| **CogniPair / GNWT-Agents**（arXiv `2506.03543`） | 551 个 GNWT agent 的 speed dating 数字孪生 | 吸引相关 0.72；参与者评价行为准确度 5.6/7.0、选择一致率 74% |
| **ConflictLens**（arXiv `2505.11715`，UIST 2025） | 从上传的私密对话**估计 13 题冲突问卷得分**并四分类冲突风格；11 类负面沟通行为标注 | 自陈仅 3 位领域专家评估；**未确认是否反映真实沟通** |
| **Couple Agents**（arXiv `2601.10970`，Wang, Chen, Bao, Jin, Swartz, Wu, Kraut & Zhu, 2026） | sense–plan–act + **显式六阶段 interaction-stage controller** | 21 名美国持照治疗师：更准确识别状态转移、评价更真实 |
| Rehearsal（CHI 2024） | LLM 生成对话脚本做冲突解决练习 | 经 ConflictLens 转述 |

**对 LHRM 的直接含义：**

1. 「LLM agent + 理论锚定 + 可解释关系状态 + 两年纵向预测」的叙事位**已被占**。
2. RELATE-Sim 与 Love First Know Later 都**报告了预测结果**。LHRM **明确拒绝**预测。这是诚实差异，必须主动写出，且必须承认它同时意味着 LHRM **没有**这些工作的结果强度。
3. 唯一叙事空位：**representation-first、refuse-to-score、abstain-first、no pre-enumerated FSM、per-dyad 而非 per-population**。空位真实存在，但目前**没有被形式化到能被识别**。

### 2.4 知识表示侧的对照（ACL 审稿人一定会问）

| ATOMIC / SOCIAL IQA 已有 | LHRM 声称 | 差别在哪 |
|---|---|---|
| `xIntent / xNeed / xReact / xWant / oWant / xEffect / oEffect / xAttr / oAttr`（9 维 if-then，PersonX/PersonY/PersonZ 分离，300K 事件 / 877K 推论，Sap et al. 2019） | `Action/Event + Belief` 分离；`DirectedState_(i->j)` vs `DirectedState_(j->i)` | ATOMIC 的 **xWant（PersonX 想要）vs oWant（PersonY 想要）** 与 LHRM 的两个方向状态在**结构上高度同构**。差别只剩：ATOMIC 是**群体常识先验**（`if-then` 关系），LHRM 声称是**个体特异、带不确定性、有 provenance 的状态**。**必须写成差别，否则会被说成「你重做了 ATOMIC 的 xWant/oWant」** |
| COMET / 动态 commonsense KG（`arXiv:1911.03876`）：按需生成上下文相关 KG，不依赖静态图 link | 保留 raw evidence/provenance；不强迫 normalization | 目标相近但目的不同（NLU 推理 vs 关系状态表示） |
| ATOMIC 2020（`10.1609/aaai.v35i7.16792`）| 「不把 literature 数量当 validation」 | **值得注意的反证**：ATOMIC 2020 报告 **GPT-3 few-shot 比用 ATOMIC 训练的 BART 模型低约 12 个百分点**（参数少 430×）——「模型自带知识比专门标注的知识库更好」是错的。这**支持** LHRM 的 schema-first 立场 |
| SOCIAL IQA 最佳 baseline 64.5%（BERT-large），人类接近 90%（Sap et al. 2019） | 期待 LLM 稳定做逐句多维状态映射 | 社会情境的机器推理与人类仍有 **~25 个百分点**缺口。LHRM 任务难度不低于 SOCIAL IQA |

### 2.5 LLM 从文本抽多类关系语义的实证上限（对 LHRM 最直接的相关性反证）

| 工作 | 任务 | 指标 |
|---|---|---|
| **Eberhardt et al. (2025)**, `10.1038/s41598-025-14923-y` | 从治疗会谈转录抽**单维**「患者参与度」，120 题取前 8 题 | ω=.953、CFI=.968、SRMR=.022、**RMSEA=.108**；效标 r=.41/.39/−.30 |
| **Lalk et al. (2025)**, `10.3389/fpsyt.2025.1504306` | 从治疗会谈转录抽**28 类情绪** | **F1macro=.45、Accuracy=.41、Kappa=.42**；对症状严重度 r=.50、对 alliance r=.20 |
| Zhang et al. (2024), arXiv `2401.15170` | 9 个社科质性码 | GPT-4 κ：3/9 ≥.79、8/9 ≥.6；GPT-3.5 mean κ=.34 |
| *Decoding Complexity*, arXiv `2403.06607` | 3 档复杂度编码任务 | 任务越难，人–模型一致性下降越快，且快于人–人 |

**读法：Eberhardt 的 ω=.953 是**单维**构念 + 结构化转录文本的组合。LHRM 要抽的是 **8 维 × 2 方向 = 16 坐标**，且语料是自由叙事。现有最强的多类抽取证据是 **Kappa=.42**。**论文若引用 Eberhardt 的 ω=.953 来暗示「LLM 可以可靠地做关系状态测量」，是把单维结论外推到多维，属于 F-6 类违规。**

## 3. 可能新颖的整合（每条含反证方向）

> **警告：这是定位失败最常见的模式。** 每条都同时给出「为什么可能已经存在」。**全部是候选，无一条已被证明。**

### NC-1 以 N=1 个体、逐句可审计的「表示完备性」为主指标的关系状态表示语言

- **可能新在哪：** 现有 SRM/APIM 需要**多人次抽样 dyad + 量表**；现有动态系统方法需要**微编码互动时间序列**；叙事心理学是**解释性、非形式化**的；LLM 定性文献是**给文本贴码**，不是**沿时间重建状态轨迹**。unit of analysis（单个具体 dyad 的轨迹）、失败判据（映射失败而非预测误差）、证据制度（Case Bank 而非样本）三者同时不同。
- **可能已存在在哪：** (a) 本质是「带领域本体的事件抽取 + 角色关系抽取」；(b) **临床个案概念化**（Persons & Tompson 2018 CASE framework：逐案例假设生成、结局监测、概念化修订）是最贴近的成熟近邻，**LHRM 与它的差别目前没有被写出来**；(c)「Unknown 作一等公民」= SQuAD 2.0 unanswerable 传统 + 形态学 paradigm coverage + IE error rate 分析；(d)「模型是建模活动」= Boyd & Heewer (2007)；(e)「先测量后因果」= Lin (2025a) dual-validity。
- **置信度：MEDIUM**（窄化到「针对特定 dyad 叙述材料的逐句表示完备性基准 + 公开可复现语料」可能成立）；按 `CURRENT_ARCHITECTURE.md:18` 现有表述 **LOW**。

### NC-2 逐维度双向有向状态 + 互惠 / 权力由派生

- **不可主张为原创。** APIM 就是双向分解；互依理论里 power 本来就是 dependence asymmetry 的函数；依赖不对称本身已是可直接测量的量表构念。
- **置信度（作为新颖主张）：LOW。** 会被一击击穿。

### NC-3 `Agency｜Relationship｜Environment｜Belief` + `Reality≠Observation≠Belief` + 嵌套反事实世界 + history lineage DAG

- **可能新在哪：** 把「per-agent 信念」「嵌套模拟世界」「历史分叉 DAG」收进同一套符号、且允许坐标为 interval / ordinal / category / distribution / Unknown，在**单个形式系统**里少见。
- **可能已存在在哪：** SRM 已把 perceiver 知觉独立成数据源；BDI / 动态认识论逻辑（van Benthem & Liu）/ POMDP 早有嵌套信念与部分可观测；关系中的贝叶斯信念更新很老；反事实/历史分叉在 plan 语义与社会科学 counterfactual reasoning 里是标准操作。
- **置信度：MEDIUM-LOW。** 记号法可能新；「现实/观察/信念不同」这个洞见不新。

### NC-4 把「映射失败率 + 弃答率」作为第一指标

- **可能新在哪：** 关系科学里几乎无人以拒答为主指标。
- **可能已存在在哪：** SQuAD 2.0 unanswerable、形态学 paradigm coverage、IE error rate 都是同一模式。
- **致命反驳：** coverage 可被堆构念刷高。**没有 coverage–construct-count trade-off 曲线，「最小充分基」就只是断言。**
- **置信度：MEDIUM**（最可辩护的一条），**但必须先补 trade-off 曲线与「弃答成本」定义**。

### NC-5 显式拒绝预枚举关系状态机

- **可能新在哪：** 这是**可检查的设计承诺**，与当前 LLM×关系工作形成对照：RELATE-Sim 用 turning-point 分类驱动场景；**Couple Agents 用显式六阶段 controller**；人口学/生命历程研究里 HMM 关系状态模型常见。
- **可能已存在在哪：** Granic & Hollenstein (2003) 已在关系科学中做过同款 move；interval + precision 语义的坐标在 AI 中是标准的——最接近的先例是 **Gelfond 的 *numbers***（{domain, precision, open/closed} 与 partial information 数值），与 LHRM 的 `estimate_or_region + uncertainty + evidence` 几乎同构。
- **置信度：MEDIUM。** 是**设计立场**不是科学发现。审稿人会问「连续/混合状态相对一个**认真指定**的有限模型买到了什么」——目前答案是「没证明」。

### NC-6 126 条 proxy 分解词典

- **可能新在哪：** 这种颗粒度、带「重复计数对象」与「最小解耦反例」列的公开词典，尚未见到。
- **可能已存在在哪：** construct dissection 传统；已有至少四套互不一致的维度方案（Sternberg 三 / Fletcher 理想 3+2 / PRQC 6+二阶 / Neubauer 四 / Acitelli 三十【未核实】）。
- **置信度：MEDIUM-LOW 作为科学新颖；MEDIUM-HIGH 作为工程/知识 artifact。**

### NC-7 把 LLM 当「自适应访谈器材」（expected information gain 选题、双人双向、维护非对称有向状态）

- **可能新在哪：** 我检索到的 LLM×关系工作里，LLM 角色分别是编码器（Zhang 2024 / QualiGPT）、量表评分器（Eberhardt 2025）、教练/训练器（Rehearsal 2024 / ConflictLens 2025 / Couple Agents 2026）、模拟器（RELATE-Sim / Love First Know Later / CogniPair）。**「LLM = 双人 dyadic 临床式评估器材 + 必须维护两个方向不一致的状态」这一格是空的。**
- **可能已存在在哪：** (a) 计算机化自适应测验已有 50 年历史，选题数学（IRT/BILT 信息函数）现成；(b) 会话式/动态评估 agent 已存在；(c) 继承 Lin (2025a) 全部批评；(d) **最致命先例反证**：`arXiv:2511.10457` 显示前代模型 state tracking 在若干步后即崩；(e) Lalk et al. 2025 显示 LLM 从文本抽**多类**语义 kappa 仅 .42。
- **置信度：MEDIUM**（网格中最空的一格），但门槛实验未做。

## 4. 禁止主张清单（forbidden claims）

> 以下不是「谨慎建议」，而是**若出现在论文/摘要/宣传材料里就构成学术不端或事实错误**的表述。

| # | 禁止主张 | 禁止理由 | 要成立需要 |
|---|---|---|---|
| F-1 | 「本模型揭示/发现了关系状态的方向性」 | 方向性 = SRM actor/partner/relationship effect + APIM 双向效应，已存在 40 年 | 不可能以「发现」措辞成立 |
| F-2 | 「首次区分了 responsiveness 的感知侧与行为侧」 | Reis, Clark & Holmes 2004 已如此定义 PPR 并强调 motivated construal | 不可能成立 |
| F-3 | 「最小充分基经受了统计/心理测量学验证」 | 零数据。`PARAMETER_CONVERGENCE_V0_1.md` §15 Gate A/B/C **未执行**；`VALIDATION_CORPUS_V0_1.md` 明确「None of the 12 includes any mapping result」 | M2–M6 |
| F-4 | 「比现有关系质量工具（PRQC / DAS / RQ / M-QoRS）更准确或更少冗余」 | 从未 head-to-head。LHRM 8 维**不是**已发现的因子结构（PRQC 二阶 / IAS 四维 / Sternberg 三成分 / ideal 3+2） | M6 因子等价性研究。**最危险的一条** |
| F-5 | 「预测关系结局（持续/破裂/满意度/离婚）」 | Joel et al. 2020：actor 自陈解释约 45% 当期满意度，**partner 不增加信息**，**无变量能预测变化方向**。RELATE-Sim 的 64.4% 已是现有 LLM×关系工作上限量级 | N≥数百纵向 dyad + 预注册 + 与 Joel 2020 口径可比。**1–3 年** |
| F-6 | 「LLM 判定与人类编码一致，故模型被验证」 | Lin (2025a/b)：LLM 输出同时充当测量指标与实验结果是**序列塌缩**；多因子结构会塌成「verbal fluency 单一维度」；Eberhardt 2025 即使 ω=.953 仍需独立效标相关；Lalk 2025 多类抽取仅 κ=.42；Zhang 2024 反对对 interview 级小数据自动编码 | 人类独立编码基线 + IRR + 预注册 + 跨模型族复现 + 外部效标相关。**LLM–LLM 一致度永远不算** |
| F-7 | 「跨文化有效 / 文化普适 / 可迁移到中文」 | 依恋量表跨文化结构本身是活跃争议（Masopustová 2025 承认 dimensional 证据在英语样本占主导）；dyadic measurement invariance Registered Report 已发现若干常用量表在 dyad 上「concerning levels」noninvariance。LHRM **零 invariance 检验** | 中英双语语料 + 跨文化样本 + invariance / DIF 检验 |
| F-8 | 「state of the art / 首次 / 首创」 | 任何 first / SOTA 措辞都可被 RELATE-Sim、Love First Know Later、CogniPair、ConflictLens、Couple Agents、ATOMIC 2020、Zhang 2024 逐一反驳。Finkel et al. 2017 已宣称完成跨理论整合 | 禁止 first / novel / unprecedented / SOTA，除非逐条给出「相对哪一具体工作的哪一具体差别」 |
| F-9 | 「从 Case Bank 个案推断现实概率 / base rate / 人口结论」 | 项目 `AGENTS.md` 与 `CURRENT_ARCHITECTURE.md` §10 已禁止；12 份材料来源等级极不均衡，3 份是极知名公版作品（leakage HIGH–VERY HIGH） | 概率抽样设计。**永远不可能**从本 Case Bank 得到 |
| F-10 | 「状态坐标具有因果效力 / 干预独立」 | §2.5 把「intervention independence」列为判据但无干预设计。Joel/Eastwick/Khera 2025 把因果混淆控制列为关系科学未解决问题；Sakaluk 2025 指出 dyadic 同时控制双方时极易高估效应与 I 类错误 | 因果推断设计。**声称因果会同时踩「没做」与「dyadic 因果本身易偏」两个坑** |
| F-11 | 「比 SRM/APIM 提供更合适的 dyadic 建模方式」 | SRM/APIM 是 dyadic 默认方法（Kenny 2018）。需同语料并列比较覆盖率与误设率——**从未做过** | M5 四路对照 |
| F-12 | 「simulation / 仿真」已在描述当前能力 | 无 transition operator、无参数标定、无仿真结果、无实现。`F(...)` 是**未定义签名** | 可运行实现 + 转移算子的可证伪测试 |
| F-13 | 「覆盖率/完备性高，所以模型好」 | coverage 可被构念膨胀刷高；**弃答率与覆盖率必须一起报告** | M4 trade-off 曲线 |
| F-14 | 「8 个有向坐标已是最小充分基」 | 「充分性」是关于目标语料的陈述。当前 12 份语料、零人工基线、零 ablation | M4 逐构造删除实验 |
| F-15 | 「关系质量 / 匹配度 / 真爱不是 primitive」被表述为本模型的发现 | 这是 Sternberg、Fletcher PRQC 二阶、Reis & Shaver 亲密过程模型、Ideal Standards Model 共同持有的立场 | 只能写「与这些理论一致」 |
| F-16 | 任何暗示 LLM 判断「准确」或「可靠」的表述 | `Decoding Complexity` 复杂度↑则人–模型一致性下降更快；QualiGPT 更新版 IRR **反而降低**；Brook 显示 LLM 生成码 specificity 更低；Lalk 2025 κ=.42 | 只有 F-6 那套证据组合 |
| F-17 | 「power / 互惠由方向性状态自动涌现」被写成结论 | 只写了 `PowerImbalance = f(...)` 签名式**假说**（§9 R2 自标「优先假说」）。且依赖不对称在既有文献里已是可测量的一等构念 | 形式条件 + 实证导出验证 |
| F-18 | 「信念/观测三分使本模型能刻画欺骗」 | 谎言识别基线准确率接近随机是学界共识。优势空间极小，易被解读为「模型在编」 | 与人类/既有工具对比（且需说明基线本身很弱） |
| F-19 | 「本模型可作为心理测量工具 / 量表」 | Eberhardt 2025 已展示完整心理测量流程。LHRM 走**结构化表示**而非**评分**，不能借用量表的效度话语 | 先把表示做成可评分量表（这会是新工作） |
| F-20 | 任何 authorship / submission / acceptance / venue 表述 | 本 lane 无此类权威；项目**没有**投稿物 | 不适用 |

## 5. 最可能的审稿攻击面（按 venue 类型）

### A. 关系科学 / 心理学期刊（JPSP、PSPB、Personal Relationships、Psychological Review、JCR、Family Relations）

- **A1「这是又一个无数据的框架论文」— 致命，当前不能应答。** 且 Finkel, Simpson & Eastwick 2017 使这个批评更锋利：关系科学**自己已经**完成跨理论整合、产出 14 条核心原则，并自我批评「the principles afford few of the sorts of conflicting predictions that can be especially helpful in fostering novel theory development」。LHRM 处境更差。
- **A2「你的 8 个有向坐标能复现已知因子结构吗？」— 致命，但可被纯文档分析回应。** 若 8 维不能承载已验证量表题项，它就只是**另一套平行分类学**。**修法不需要被试**：把既有量表题项作为 mapping target 做形式化覆盖分析（M6）。**这是最有杀伤力也最可修的批评。**
- **A3「方向性的经验基础可能比你想的弱」— 强，当前不能应答。** Joel et al. 2020：partner 判断对当期满意度不增加信息；Bloomberg/Joel/Eastwick：partner effects 的 p-curve 不符合 → 选择性报告与发表偏倚。LHRM 把「双向有向坐标」当架构基石，恰落在文献中最不可靠的那一半上。
- **A4「你把 attachment 的 general vs relationship-specific 之争当成已解决」— 中强，不能应答。** ECR-RS：关系特异测量对**关系内**结果预测更好，一般性测量对**人格**预测更好；「differentiation … is not related to psychological outcomes independently of mean levels of security」。LHRM 把 B01/B03 分层写成判定结果，这在文献里是**未决问题**。
- **A5「你的 MSC 判据没有出处」— 中，不能应答。** 与通用构念效度五检同构，报告未引出处。
- **A6「跨文化主张」— 中，不能应答。**
- **A7「Case Bank 语料有严重选择偏倚与泄漏」— 中强，部分能。** 项目已诚实标注；但 Gift of the Magi / Yellow Wallpaper / Aspern Papers / Looking Backward / Orpheus 等极知名公版作品使泄漏控制几乎无解。

### B. 方法学 / 测量期刊（Psychological Methods、Assessment、JCP、SEM、JCM）

- **B1「报告了覆盖率却没报弃答率，也无任何信度证据」— 致命，不能。**
- **B2「LLM rating / coding 的心理测量必须做」— 强，不能。** 且不能靠「我们是结构化表示不是评分」完全挡掉。
- **B3「混合类型坐标（interval / ordinal / category / distribution / Unknown）如何比较、如何定义距离、partial ordering 怎么处理？」— 强，不能。** LHRM 拒绝统一欧氏距离与 `0..1`，但**没有**替代比较理论。`AGENTS.md` 的「不强迫所有坐标进入 0..1、欧氏空间或共同语义尺度」在数学上需要一套 handle / partial-order 代数才有意义。
- **B4「不可识别性：一般关系满足 `Y=α_i+β_j`，两个方向的斜率可与任意配对互换」— 强，不能。** 需 state-space 多重测量的识别假设与可检验锚定。注意 LHRM 的「Case Bank 不做总体推断」只回避了 pop-level 识别，**没回避 state-level 坐标锚定问题**。
- **B5「Kenny 2018 / Sakaluk 2025 说 APIM 是默认、dyadic SEM 才是被低估的选项；你为什么不比较？」— 中强，不能。**

### C. HCI / CSCW（CHI、CSCW、UIST、TOCHI）— **现实上最可投的一类**

- **C1「这只是 demo」— 强，不能。**
- **C2「赛道已有 ConflictLens（UIST 2025）、Rehearsal（CHI 2024）、Couple Agents（2026）；你的增量在哪？」— 强，不能。** 但这恰恰是 LHRM **唯一**可能讲清差异的地方（它们是 stage/FSM 驱动的模拟器或教练；LHRM 是 representation-first、无预枚举状态机、拒答优先）。
- **C3「LLM 读私密关系对话的伦理风险？双方知情同意？」— 强，部分能。** `VALIDATION_CORPUS` 已做敏感内容筛选（无未成年人、无性暴力），是加分项；但无真实用户数据设计，也无数据治理方案。
- **C4「MAPPING_FAILURE 是可解释的设计，还是把难题外包给 abstention？」— 强，不能。**
- **C5「叙事材料（判决书/文学）vs 真实关系（用户自述）的外部效度」— 强，不能。** LHRM 语料几乎全是**第三方叙述**；真实关系是**第一人称、自愿、隐私敏感**语料，语用结构完全不同。

### D. 计算社会科学 / 数字社会学（Sociological Methods & Research、Social Media + Society、JASSS、EPJ Data Science）

- **D1「需要真实 dyad 数据与基线（APIM / SRM / dyadic SEM）对照」— 强，不能。**
- **D2「ABM 已有 2005 年起的 marriage-market 模型，甚至声称定量复现婚龄与离婚统计；你的模型多了什么？」— 中强，不能。** 但可**主动进攻**：论证「单 dyad 表示」与「群体统计 ABM」是**不同研究问题**。
- **D3「LLM 分析的透明度与可复现性（prompt 敏感性、模型版本漂移）」— 强，部分能。** `VALIDATION_CORPUS` 有 2026-09-11 的 live-fetch 核实日志（好习惯）；但对 LLM 本身**无**版本固定/复现协议。

### E. 知识表示 / 语义网 / 计算语言学（ACL、LREC、EMNLP、*Semantics*、JWS）

- **E1「你的 schema 有形式语义吗？是一条语法、一套本体、一个 EBNF，还是散文？」— 致命，不能。** 当前是散文 + 表格 + markdown 代码块。
- **E2「有公开基准与基线系统吗？」— 致命，不能。**
- **E3「ATOMIC 的 `xWant` vs `oWant`（PersonX/PersonY 分离）与你的两个方向状态结构上高度同构，差别在哪？」— 强，不能。**
- **E4「SOCIAL IQA 上人类 90%、模型 64.5% —— 你的 LLM 映射凭什么可信？」— 强，不能。**

### F. ML 会议（NeurIPS / ICLR / ACL-ML）

**直接判定：dead end。** 无学习组件、无 benchmark、无理论保证、无规模。**不要投，不要以此为目标改写定位。**

### G. 数字人文 / 叙事研究

- **G1「用 LLM 做叙事分析却没有人类 close reading 作为方法论锚定，也没有 inter-annotator 协商」— 强。**
- **G2「已知名文本（Aspern Papers、Yellow Wallpaper、Orpheus）被模型记忆污染」— 强。**

### H. 最恶毒但最可能的一条（元审稿攻击）

> **「这是一份用 12 份已知来源的文本、一位非受训编码者作为验证者、零人工基线、零统计量做出的完备性报告。因此所有 'coverage' 结果都是关于该 LLM 记住了多少文本的函数，而不是关于该表示的函数。」**

项目当前**完全无法**回应。要回应，**必须**有：human baseline（≥2 名独立编码者 + IRR + 仲裁）、模型版本固定、held-out split，以及把语料换成**低泄漏**材料（法律/机构文件优先，文学只作 expressivity stress test，且必须明确不测泄漏敏感能力）。

## 6. 诚实投稿所需的实证里程碑

> 单人全职估计；括号内为双人并行乐观估计。**均为本 lane 判断，不是任何 Human 承诺。**

| 阶段 | 内容 | 产出判据 | 估计 | 阻塞后续？ |
|---|---|---|---|---|
| **M0 形式化** | 定义带类型的坐标代数（interval / ordinal / category / constraint / distribution / Unknown 各自的半序/偏序/区间代数）；给 `Mapping` 一个可判定的判定过程；写清 partial order 完备性条件与不可比较时的处理 | 可机读 schema 规范 + 参考实现（输出 `{coordinate, type, uncertainty, evidence, provenance}` 或 `MAPPING_FAILURE` **并给出失败理由**） | **4–8 周** | **是** |
| **M1 Case Bank 扩容** | 12 → ≥60 份（法院/官方 25、小说与纪实 15、神话/科幻 10、日常对话/短信 10）+ ≥20 条 adversarial case；每份附 `access_status / licence / leakage_risk / fact-unit 预估` | 公开语料清单 + 抓取清洗日志 + 许可说明 | **6–10 周**（抓取与清洗可并行） | 是 |
| **M2 人类编码基线**（当前完全缺失，最被低估） | ≥2 名独立人类编码者 + 1 名仲裁；全语料逐句标注；计算 IRR（per-code κ / Gwet AC1）与一致性讨论；记录分歧的**本体层**诊断（ontology / construct / scope / temporal / belief / measurement hole） | 人类基准标注 + 逐 code IRR 表 + 仲裁记录 | **4–6 周 + 被试时间** | **是** |
| **M3 LLM 映射基准** | ≥3 个模型族（≥2 个架构）× ≥2 个时间点（防止把 2026-09 的模型能力当永久属性）；报告 per-coordinate 覆盖率、**弃答率**、错误分类、与 M2 对照；显式测 **state-tracking 衰减**（`arXiv:2511.10457`） | 可复现脚本 + 完整结果表 + 错误分类法 | **3–4 周** | 是 |
| **M4 消融与「最小充分性」检验** | 逐个删除 construct k → 记录 `MAPPING_FAILURE` 上升；逐个加入 → 记录弃答率下降。**目标是 coverage–construct-count trade-off 曲线** | 消融矩阵 + trade-off 曲线 + 「最小」主张的正式陈述 | **3–4 周** | 是（否则 F-14 不可解除） |
| **M5 四路表示对照** | 同一语料四种表示并行编码：(a) SRM/APIM 式双向量表读数；(b) ATOMIC 式 if-then 事件三元组（含 xWant/oWant 分离）；(c) RMT / Interpersonal Circumplex；(d) 纯叙事摘要基线。比较覆盖率、弃答率、错误类型 | 对照矩阵 + 诚实报告（**允许结论是「我们并没有更好」**） | **4–6 周** | 是（否则 F-11 / NC-1 无法辩护） |
| **M6 覆盖已知因子结构** | 把 PRQC 6+二阶 / IAS 4 / Sternberg 3 / ECR 2 / Fletcher ideal 3+2 的**题项**作为 mapping target，跑 M0 判定过程 | 构念等价性报告 | **3–4 周** | 若要谈测量则阻塞 |
| **M7 测量学** | reliability 六项（照 `arXiv:2406.17675`）+ factor structure + measurement invariance | 心理测量报告 | **2–4 个月**（需 N≥数百） | 否（除非投 B 组） |
| **M8 纵向 dyad 样本** | 预注册、≥200–500 对、≥3 时间点、双方独立测量、含 APIM 必需的两方同量表 | 纵向数据集 + 论文 | **1–3 年** | 否（F-5 永远不能解除） |
| **M9 跨文化 / 跨语言** | 中英双语语料 + invariance 检验 | 跨文化附录 | **3–6 个月** | 否（F-7 永远不能解除） |

**诚实的端到端时间：M0–M5 ≈ 5–7 个月单人全职（2–3 个月双人并行）。这是可以把 representation 论文写诚实的最短路径下界。没有 M0–M5，任何投稿都是 overclaim。**

## 7. 项目自身文档的 overclaim 位置（研究反馈，不做任何编辑）

> 引文逐字取自本次实际读取的文件。**未修改任何文件。**

| # | 文件:行 | 项目原话 | 问题 |
|---|---|---|---|
| O-1 | `README.md:5` | 「LHRM 是一个用于研究、表达与**仿真**人类二人关系的开放研究项目。」 | 「仿真」被当作**当前能力**陈述。现状：无 transition operator、无参数标定、无仿真结果、无实现。建议改为「表示与（未来的）仿真」，或在「当前阶段」显式列出 `simulation = NOT IMPLEMENTED` |
| O-2 | `CURRENT_ARCHITECTURE.md:18` | 「建立一套能够在任意时刻……进行结构化、方向化、时间索引、保留 Unknown 与不确定性的**数学**状态表示语言。」 | 「**数学**」暗示已形式化。当前是散文 + markdown 代码块：无类型系统、无公理、无 partial order 代数、无映射判定过程 |
| O-3 | `CURRENT_ARCHITECTURE.md:203` | 「X_(t+1) = F(X_t, Action_t, Event_t, Belief_t, Constraint_t, Environment_t)」 | (a) **括号不匹配**（`X_(t+1)` 缺右括号）——会被审稿人当作粗心证据；(b) 读起来像**已定义的转移律**，实际只是 schema 签名；(c) 紧接 204 行「而走**实时演算**」进一步强化「已实现」的错觉 |
| O-4 | `CURRENT_ARCHITECTURE.md:232-236` | 「LHRM 的核心产物优先是动态状态轨迹：Gamma_(A,B) = { X_(A,B)(tau) }」 | 「核心产物」被写成**已存在**的对象。当前只有 `tau` 的**记法**设想与一句 lineage DAG 文字描述，无数据结构、无存储、无生成过程 |
| O-5 | `PARAMETER_CONVERGENCE_V0_1.md:119` | 「以下 construct 在科学研究、游戏形式化、现实反例和**本项目压力测试中均表现出较强的独立性**。」 | **循环论证。** 独立性按 §15 Gate C 才要检验，而 Gate C 明确 `PENDING`；`MAPPING_FAILURE` 尚未跑过任何一份语料。应改为「按 §2 判据的**初步判断**」 |
| O-6 | `PARAMETER_CONVERGENCE_V0_1.md:45-86` | §2 的 6 条收敛判据 | 判据是**问题形式**（「是否仍可能为额外信息？」），不是**可操作判据**（无阈值、无统计量、无判定程序）。因此 §11 的 8 维 basis 选择过程不可复核 |
| O-7 | `RESEARCH_REPORT_SCIENTIFIC_RELATIONSHIP_PRIMITIVES.md:109-115` | 「候选 `X` 有资格成为 `primitive_state`，需**同时满足五条**」（MSC） | 与通用构念效度检查清单（Cook & Messick 1979 / Messick 1989,1995 / Trochim 1999 五检）结构几乎一一对应，**报告未引任何出处**。审稿人会问「your criteria are Cook & Messick's with new labels; where is the increment?」 |
| O-8 | 同上 `:28` | 「**真正的最低层关系状态，方向是「每个主体对客体的一条有向边上的少量状态」，且不能靠更底层机制替代**」 | 把 SRM/APIM 的既有结构表述成**发现**。必须改为 REUSE 语态 |
| O-9 | 同上 `:50` | 「六维里，**真正够「primitive 级」且能独立存活的是 Trust 与 Dependence**」 | 关于关系科学构念结构的**实质经验主张**，无任何数据；且与已发表维度方案不一致。M6 未做前必须降级为 hypothesis |
| O-10 | 同上 `:1440` | 「采用简标明（author, year）形式；**文献细节请在外部库核对**」 | 全部引用未经 DOI 级核实。本次抽查即发现一处上游引用错误：Fletcher & Simpson (2000) CDPS 把 Fletcher et al. (1999) JPSP 页码写成 **54–71**，Crossref 确认正确为 **72–89**（`10.1037/0022-3514.76.1.72`）。**LHRM 自己的 `STAGE_SUMMARY_2026-09-07.md` §5.6 写 72–89，是对的**——但「请外部库核对」使每条都成为 A04 lane 的攻击面 |
| O-11 | `RELATIONSHIP_EVALUATION_FOUNDATION.md:13` | 「先固定一套**足够精妙、优雅**、直接且可扩展的底层坐标系。」 | 「精妙/优雅」是不可证伪的价值判断，出现在项目定位句里 |
| O-12 | `RELATIONSHIP_EVALUATION_FOUNDATION.md:22` | 「**动态但不漂移**：……**基础结构本身尽量不变**。」 | **历史事实与该句冲突**：S/O/D/E 已从「完整世界本体」降级为「query-local view」；`Candidate Minimal Directed Basis` 已经历缩减 |
| O-13 | `RELATIONSHIP_EVALUATION_FOUNDATION.md:150` | 「同样的 `S + O + D`，在**不同 `E` 下可能形成完全不同的长期关系结果**。」 | 关于 Environment 层因果强度的**实质主张**，无证据。Joel et al. 2020 已证明人口学/客观状态变量几乎无预测力——既是 `E` 层的直接反例 |
| O-14 | `STAGE_SUMMARY_2026-09-07.md:317` | 「未来若形成论文，优先把贡献写成：问题定义 → 已有理论碎片 → **统一架构** → 构念收敛方法 → **LLM 交互式测量** → **实证/仿真验证**」 | 这是**论文提纲**，但把「LLM 交互式测量」与「实证/仿真验证」写得像已有内容。**LHRM 交互式测量层不存在**（§4 只是「一个重要未来研究方向」）。照此提纲写论文，摘要会自动产生 F-3/F-6/F-12 违规 |
| O-15 | `STAGE_SUMMARY_2026-09-07.md:327` | 「LHRM 专注于统一状态语义、观测/信念接口、动态更新与**可验证的集成架构**。」 | 暗示已可验证。当前 M0–M5 全部未做，**零验证**。这是 README 层的 overclaim，会被截图传播 |
| O-16 | `AGENTS.md:21` vs `README.md:5` | `AGENTS.md` 要求「不得把未经验证的公式……表述为已验证预测模型」；`README.md` 写「仿真」 | **项目内部自相矛盾**：最严格的规则与最宽松的对外描述并存。README 是最可能被外部读到的文件，规则应反向约束 README 措辞 |
| O-17 | `PARAMETER_CONVERGENCE_V0_1.md:497-501` | 「### R4. Relationship Quality / Compatibility / Match Score — 当前：`REJECT as primitive`」 | 措辞正确。**但要警惕**：论文里若写成「we improve on existing quality indices」就瞬间触发 F-4。**措辞陷阱，不是文档错误** |

**总评：** 项目在**研究纪律层面**（`AGENTS.md`、§15 验证门、VALIDATION_CORPUS 的诚实标注、STAGE_SUMMARY §6 的「只是 novelty hypotheses」）明显高于一般开源项目。overclaim 集中在**三处**：**(a) `README.md` 的「仿真」**；**(b) `CURRENT_ARCHITECTURE.md` 的「数学语言 / 实时演算 / 核心产物」**；**(c) `STAGE_SUMMARY` §8 的论文提纲把规划当内容**。三处都是**措辞层**问题而非**架构层**问题——修掉它们不需要改任何设计决策。

## 8. 明确非主张（本 lane 不主张什么）

1. 不主张任何 authorship、submission、acceptance、venue 相关事实。LHRM **没有**投稿物。
2. 不主张 LHRM 优于或劣于任何现有工具、量表、框架。
3. 不主张任何映射覆盖率数字。**零**份语料已被映射。
4. 不主张 LHRM 的 8 维是「最小充分」或「低冗余」。这是**待检验假说**（M4）。
5. 不主张 LHRM 有任何因果效力、内效度、测量不变性、跨文化效度。
6. 不主张 LLM 与 LHRM 的一致度构成任何形式的验证。
7. 不主张 Case Bank 可支持任何总体、概率、base rate 或文化普适结论。
8. 不主张 LHRM 发现了方向性、responsiveness、互依、依恋、理想标准或关系质量维度。**全部为 REUSE。**
9. 不主张本次检索完备（`websearch` 多次 429 / transport error；`export.arxiv.org` API 超时；商业产品线未覆盖）。
10. 不主张 §3（NC-1..NC-7）中任何项已被证明新颖。**全部是候选**，每条都给了反证方向与置信度。
11. 不对 commercial relationship-assessment 产品的能力做任何评价。
12. **不把 literature 数量或 LLM 一致度当作 validation。**

## 9. 剩余未知

1. **Acitelli & Antonioni (2006) 30 维方案的确切题名/卷期/DOI 与内容** —— 决定「最小充分基」新颖性判断的最大单一变量。
2. **Boyd & Heewer (2007) 是否确为 LHRM 立场的来源** —— 决定「representation over prediction」是否可作原创主张。
3. **LHRM 的 8 个有向坐标能否承载已验证关系量表的题项**（M6）—— 论文可行性的核心未测项。
4. **`PowerImbalance = f(两方向 OutcomeDependence, alternatives, resources, constraints)` 是否真能稳定导出**。
5. **`Cohesion_(A,B)` 是否需要 shared latent**（§6 P1 明确未定）。
6. **`Distrust` 是否独立于 `1 − Trust`**（Lewicki 双元 vs 单极之争仍未定）。
7. **不可识别性风险**：`D6/D7/D8` 是否满足 state-space 多重测量的识别条件。本 lane 未做文献穷尽检索。
8. **中文语料下的映射可行性**（本次全部语料证据为英文）。**未测。**
9. **LLM×关系表示工作的检索不完整**。可能存在未被检出的直接竞争者。
10. **relationship science 对「框架/本体/表示语言」类贡献的实际发表位置**。**未知。**

## 10. 参考文献（本 lane 核实，2026-09-27）

### 二人 / dyadic 方法学
- Cook, W. L., & Kenny, D. A. (2005). The Actor–Partner Interdependence Model. *Int. J. Behavioral Development, 29*(2), 101–109. DOI `10.1080/01650250444000405`
- Kenny, D. A. (2018). Reflections on the actor–partner interdependence model. *Personal Relationships*. DOI `10.1111/pere.12240`
- Garcia, R. L., Kenny, D. A., & Ledermann, T. (2015). Moderation in the actor–partner interdependence model. *Personal Relationships*. DOI `10.1111/pere.12060`
- Sakaluk, J. K., Joel, S., Quinn-Nilas, C., Camanto, O. J., Pevie, N. W., Tu, E., & Jorgensen-Wells, M. A. (2025). A Renewal of Dyadic Structural Equation Modeling With Latent Variables. *Social and Personality Psychology Compass*. DOI `10.1111/spc3.70045`
- Back, M. D., & Kenny, D. A. (2010). The Social Relations Model: How to Understand Dyadic Processes. `CITED_SECONDARY`

### 互依 / 投资模型
- Rusbult, C. E. (1980). Commitment and satisfaction in romantic associations. *JESP, 16*(2), 172–186. DOI `10.1016/0022-1031(80)90007-4`
- Rusbult, C. E., Martz, J. M., & Agnew, C. R. (1998). The Investment Model Scale. *Personal Relationships, 5*(4), 357–387. DOI `10.1111/j.1475-6811.1998.tb00177.x`
- Le, B., & Agnew, C. R. (2003). Commitment and its theorized determinants. *Personal Relationships, 10*(1), 37–57. DOI `10.1111/1475-6811.00035`
- Tran, P., Judge, M., Kashima, Y., & Agnew, C. R. (2019). Commitment in relationships: An updated meta-analysis of the Investment Model. *Personal Relationships*. DOI `10.1111/pere.12268`
- Rusbult, C. E., & Van Lange, P. A. M. (2003). Interdependence, interaction, and relationships. *Annual Review of Psychology, 54*, 351–375. DOI `10.1146/annurev.psych.54.101601.145059`

### 依恋
- Roisman, G. I. (2009). Adult Attachment: Toward a Rapprochement of Methodological Cultures. *Current Directions in Psychological Science*. DOI `10.1111/j.1467-8721.2009.01621.x`
- Hyland, S. M., Overall, N. C., & Maddux, G. M. (2015). Are adult attachment styles categorical or dimensional? `https://pubmed.ncbi.nlm.nih.gov/25559192/`
- Raby, K. L., et al. (2020). Categorical or Dimensional Measures of Attachment? `https://earlyexperiences.psych.utah.edu/pubs/Raby-categorical-or-dimensional-in%20press.pdf`
- Ravitz, P., et al. (2015). Adult attachment measures: A 25-year review. `https://learn.lakesidetraining.org/wp-content/uploads/2024/08/Adult-Attachment-Measures.pdf`
- Fraley, R. C. (2019). Attachment in Adulthood. *Annual Review of Psychology*. DOI `10.1146/annurev-psych-010418-102813`
- Masopustová, K., et al. (2025). Can different adult attachment profiles be distinguished… *Journal of Individual Differences*. DOI `10.1007/s12144-025-08223-x`
- Fraley, R. C., Waller, N. G., & Brennan, K. A. (2000). The Experiences in Close Relationships—Relationship Structures Questionnaire. `CITED_SECONDARY`

### Responsiveness / Michelangelo
- Reis, H. T., Clark, M. S., & Holmes, J. G. (2004). Perceived Partner Responsiveness as an Organizing Construct. `https://www.sas.rochester.edu/psy/people/faculty/reis_harry/assets/pdf/ReisClarkHolmes_2004.pdf`
- Reis, H. T., & Shaver, P. (1988). Intimacy as an interpersonal process. `CITED_SECONDARY`
- Reis, H. T., & Clark, M. S. (2013). Responsiveness. *Annual Review of Psychology*. `https://anthonyongphd.wordpress.com/wp-content/uploads/2018/01/reis-clark-2013.pdf`
- Drigotas, S. M., Rusbult, C. E., Wieselquist, J., & Whitton, S. W. (1999). Close partner as sculptor of the ideal self. *JPSP*. `https://faculty.wcas.northwestern.edu/eli-finkel/documents/69_DrigotasRusbultWieselquistWhitton1999_JournalOfPersonalityAndSocialPsychology.pdf`
- Rusbult, C. E., Finkel, E. J., & Kumashiro, M. (2009). The Michelangelo Phenomenon. *Current Directions in Psychological Science, 18*(4), 143–158. DOI `10.1111/j.1467-8721.2009.01657.x`
- Visserman, M., et al. (2022). Lightening the Load. `https://labsites.rochester.edu/lelab/wp-content/uploads/2022/12/Visserman-et-al.-2022-Perceived-partner-responsiveness-fosters-more-positive-appraisals-of-relational-sacrifices.pdf`

### 理想标准 / 择偶评价
- Fletcher, G. J. O., Simpson, J. A., Thomas, G., & Giles, L. (1999). Ideals in intimate relationships. *JPSP, 76*(1), 72–89. DOI `10.1037/0022-3514.76.1.72`
- Fletcher, G. J. O., & Simpson, J. A. (2000). Ideal Standards in Close Relationships. *CDPS, 9*(3), 102–105. DOI `10.1111/1467-8721.00070`
- Fletcher, G. J. O., Simpson, J. A., & Thomas, G. (2000). The role of ideals in early relationship development. *JPSP*. `https://pubmed.ncbi.nlm.nih.gov/11138762/`
- Eastwick, P. W., Finkel, E. J., & Joel, S. (2023). Mate evaluation theory. *Psychological Review, 130*(1), 211–241. DOI `10.1037/rev0000360`
- Eastwick, P. W., Joel, S., Carswell, K. L., Molden, D. C., Finkel, E. J., & Blozis, S. A. (2022). Predicting romantic interest during early relationship development. *European Journal of Personality*. DOI `10.1177/08902070221085877`
- Joel, S., Eastwick, P. W., & Finkel, E. J. (2017). Is romantic desire predictable? `https://doi.org/10.31219/osf.io/gu8z7`

### 关系质量测量
- Fletcher, G. J. O., Simpson, J. A., & Thomas, G. (2000). The measurement of perceived relationship quality components. *PSPB, 25*(4), 429–441. DOI `10.1177/0146167200265007`
- Neubauer, A. B., Voss, A., & Asendorpf, J. B. (2015). Dimensions of Relationship Quality. *Personal Relationships*. DOI `10.1111/1475-6811.00017`
- McTaggart, D., et al. Multidimensional Quality of Relationship Scale (M-QoRS). `https://openaccess.city.ac.uk/id/eprint/35352/3/Development%20of%20MQoRS.pdf`
- Measuring Relationship Quality in an International Study. `https://pmc.ncbi.nlm.nih.gov/articles/PMC6187488/`
- Joel, S., Eastwick, P. W., Allison, C. J., Arriaga, X. B., et al. (2020). Machine learning uncovers the most robust self-report predictors of relationship quality across 43 longitudinal couples studies. *PNAS, 117*(32). DOI `10.1073/pnas.1917036117`
- Joel, S., Eastwick, P. W., & Khera, D. S. (2025). A Credibility Revolution for Relationship Science. *Social and Personality Psychology Compass*. DOI `10.1111/spc3.70042`
- Bloomberg, J. J., Joel, S., & Eastwick, P. W. Partner Effects May Be Weaker Than We Thought. **`UNVERIFIED_DOI`**

### 动态系统
- Feinberg, M. E., Xia, M., Fosco, G. M., Heyman, R. E., & Chow, S.-M. Dynamical Systems Modeling of Couple Interaction. *Prevention Science*. DOI `10.1007/s11121-017-0803-3`
- Granic, I., & Hollenstein, T. (2003). Annual Review of Psychology. `CITED_SECONDARY`
- de Haan, G. J. P., Thompson, E. E., & Vogeley, S. (2014). An enactive and dynamical systems theory account of dyadic relationships. *Frontiers in Psychology, 5*, 452. DOI `10.3389/fpsyg.2014.00452`
- The Paradox of Stability and Change in Relationships. *JSP, 17*(3), 300. DOI `10.1177/0265407500173006`

### ABM / microsimulation
- Billari, F. C. (2005). The "Wedding-Ring". *Demographic Research, 17*(3). `https://www.demographic-research.org/volumes/vol17/3/17-3.pdf`
- Hills, T., & Todd, P. M. (2008). MADAM. *JASSS, 11*(4). `https://www.jasss.org/11/4/5.html`
- Modelling "Marriage Markets" (New Zealand). *JASSS, 16*(1), 6. `https://www.jasss.org/16/1/6.html`
- Mudimu, E. (2015). Agent-based model for social and sexual partnerships formation. DOI `10.1177/1059712314547709`

### LLM × 定性编码 / 测量 / 心理模拟
- Zhang, et al. (2024). Scalable Qualitative Coding with LLMs. arXiv `2401.15170`；OSF `https://osf.io/k4fg9`
- Deilamsalehi, H., et al. (2024). QualiGPT. arXiv `2407.14925`
- Decoding Complexity: Exploring Human-AI Concordance in Qualitative Coding. arXiv `2403.06607`
- An Examination of the Use of LLMs to Aid Analysis of Textual Data. DOI `10.1177/16094069241231168`
- Eberhardt, S. T., Vehlen, A., Schaffrath, J., Schwartz, B., Baur, T., Schiller, D., Hallmen, T., André, E., & Lutz, W. (2025). Development and validation of large language model rating scales. *Scientific Reports*. DOI `10.1038/s41598-025-14923-y`
- Lalk, C., Targan, K., Steinbrenner, T., Schaffrath, J., Eberhardt, S., Schwartz, B., Vehlen, A., & Lutz, W. (2025). Employing large language models for emotion detection in psychotherapy transcripts. *Frontiers in Psychiatry*. DOI `10.3389/fpsyt.2025.1504306`
- Large Language Models in Qualitative Research. arXiv `2410.07362`
- Exploring State Tracking Capabilities of Large Language Models. arXiv `2511.10457`
- Psychometric Benchmark for LLMs. arXiv `2406.17675`
- Lin, Z. (2025). Large Language Models as Psychological Simulators: A Methodological Guide. *AMMPS*. DOI `10.1177/25152459251410153`
- Lin, Z. (2025). arXiv `2506.16697`；arXiv `2507.04491`

### LLM × 关系（直接竞争）
- Yue, M., Xu, Z., Gupta, V., Ha, T., Sharabi, L., & Zhou, B. RELATE-Sim. arXiv `2510.00414`
- Love First, Know Later: Persona-Based Romantic Compatibility Through LLM Text World Engines. arXiv `2512.11844`
- CogniPair: GNWT-Agents. arXiv `2506.03543`
- ConflictLens. arXiv `2505.11715`（UIST 2025）
- Wang, C., Chen, A., Bao, C., Jin, S., Swartz, H., Wu, T., Kraut, R. E., & Zhu, H. (2026). Simulating Couple Conflict. arXiv `2601.10970`
- Shaikh, O., Chai, V. E., Gelfand, M., Yang, D., & Bernstein, M. S. (2024). Rehearsal. *CHI 2024*. `CITED_SECONDARY`

### 社会常识 / 事件图
- Sap, M., et al. (2019). ATOMIC. *AAAI*. `https://maartensap.com/pdfs/sap2019atomic.pdf`
- Sap, M., et al. (2019). SOCIAL IQA. `https://maartensap.com/pdfs/sap2019socialIQa.pdf`
- Hwang, J. D., et al. (2021). (Comet-) Atomic 2020. *AAAI*. DOI `10.1609/aaai.v35i7.16792`
- COMET-based dynamic commonsense QA. arXiv `1911.03876`

### 跨理论整合
- Finkel, E. J., Simpson, J. A., & Eastwick, P. W. (2017). The Psychology of Close Relationships: Fourteen Core Principles. *Annual Review of Psychology, 68*, 383–411. DOI `10.1146/annurev-psych-010416-044038`
- Fiske, S. T. (1992). Relational Models Theory. *Psychological Review, 99*(4), 689. DOI `10.1037/0033-295X.99.4.689`
- Wiggins, G., & Broughton, R. (1991). Interpersonal Circumplex. DOI `10.1002/per.2410050503`

### 未核实（高优先 prior-art，必须由 A04 补验）
- Acitelli, A. L., & Antonioni, R. (2006). Twenty dimensions of marriage. *JPSP, 90*(6). **`AGENT_RECALL` / `UNVERIFIED_DOI`**
- Boyd, J. G., & Heewer, S. C. (2007). Communication as a Modeling Activity. *Communication Theory, 17*(1), 4–25. **`AGENT_RECALL`**
- Cook, T. E., & Messick, T. E. (1979) / Messick, N. (1989, 1995) / Trochim, W. M. K. (1999). Construct validity checks. **`AGENT_RECALL`**
- Sternberg, R. J. (1986) triangular theory; Spanier, J. A. (1976) DAS; Lund, M. (1985) investment & commitment scales. **`AGENT_RECALL`**
