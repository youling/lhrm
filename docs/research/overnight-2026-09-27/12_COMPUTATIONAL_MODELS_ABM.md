# 12 计算模型 / ABM / 微模拟基准调查（Computational relationship / ABM / microsimulation benchmark）

**Status:** `RESEARCH_CANDIDATE` / `NOT_CANONICAL`
**As of:** 2026-09-27（全部可访问性判断的核实日期）
**Lane:** R12, Wave 1 of `youling/lhrm#30@overnight-opencode-exploration-swarm-v1`
**Scope:** 与 LHRM 研究对象（Human–Human dyad 的时间索引、方向化、保留 Unknown 的关系状态表示）**真正可比**的计算模型、agent-based model、社会仿真、二人动力学模型，以及可复用的开放框架。

> 本文件不主张任何 LHRM 构念、参数、权重、转移律已被验证。文中出现的所有数值、概率、参数区间均为**引用他人的模型**，不是 LHRM 的候选值。
> 证据分级：`CITED_PRIMARY`（本次实际打开原始页）/ `CITED_SECONDARY`（转述）/ `AGENT_RECALL`（先验，未核实）/ `NEGATIVE`（主动搜索后未找到）。

---

## 0. TL;DR（先读这一段）

1. **本 lane 最重要的发现是一个否证**：**在本 lane 已检索的场所内**，未找到可与 LHRM 对象直接比较的既有关系 ABM。现有工作分成三堆——**配对人口学**、**网络 tie 动力学**、**可读行为生成**——**在本次检索覆盖的样本内没有一堆的对象是"关系内部的、方向化的、保留 Unknown 的时间索引状态"**。LHRM 在这个维度上不是落后。
   > **R12 Round-3 检索范围更正（2026-09-28；依 Architect adjudication V1 `X-14` 与 §C 第 6 条 `Search failure/access restriction is not ontology evidence`）**
   >
   > **被取代的原文**：「**不存在**可与 LHRM 对象直接比较的既有关系 ABM … LHRM 在这个维度上不是落后，而是**孤立**」。
   >
   > **两处修正**：
   > 1. **「不存在」→ 检索范围命题。** 本报告的采样框架是 §2 清单（GitHub / JOSS / CRAN / JASSS / CoMSES / arXiv / Crossref / 公开项目页），**没有任何一项是领域总体抽样**。`X-14` 明确：除非抽样支持总体不存在，字段级存在性主张必须改写为**检索范围主张**。合规表述是「**在本 lane 已审计的检索场所内未找到**」，不是「不存在」。
   > 2. **「孤立」这一措辞撤回。** 「孤立」是一个**总体断言**（它断言整个领域的状态），同样超出采样框架。而且它**低配了本报告自己的正面证据**（见 §4.2 与 §10 的 Round-3 补记）。**本报告没有资格断言一个领域的状态。**
   >
   > **对照 §1 的自陈**：§1 写的是「通过 C5 的：**本 lane 未找到任何一个**」——**这才是本报告证据所能支撑的形式**。§0 的 headline 与 §1 自相矛盾，本轮以 §1 为准。
   >
   > **不主张**：这不改变 §10 的裁决方向，也不主张存在这样的 ABM。**「未找到」与「不存在」之间的距离，正是本报告不能跨越的那一段。**
2. **校准最扎实的关系 ABM 里没有"关系状态"**。Hills & Todd (2008) 的 MADAM 匹配了美国初婚年龄曲线并成功预测了 5 年后的离婚统计，但它的一对"关系"只是"共享 trait 数 + 时长"，**没有 attraction / trust / belief，方向性完全不存在**。
3. **最成熟的有向二人统计模型（SAOM/RSiena）在原理上排除 LHRM 的对象**，而且是作者自己在正文里写明的排除性判据：tie 的存在被假定为**处于发送方单边控制之下**，因此"排除大多数需要协商才能成立的关系类型"。
4. **LHRM 方向性分解真正的统计学祖宗是 Social Relations Model（actor / partner / relationship 三分量方差成分）**，但它是**横截面**的、需要 **round-robin** 设计（Case Bank 的单一 dyad 深度材料结构上不满足），且把 residual 混在"relationship"里、不区分共享事实与测量误差。**所以它能回答"我的 8 个坐标是否可分离"，不能回答"我的转移对不对"。**
5. **机制演示 ≠ 经验验证，这有三条硬证据**（§4），其中最强的一条来自该领域内部：**Lustick (2000) 白纸黑字写下了这个领域的默认交易条件——接受"发现的近乎完全的人造性"（acceptance of the nearly complete artifactuality of the findings）**。
6. **诚实的裁决**：**在 LHRM 当前第一阶段目标（表示完备性 + Case Bank 逐句映射）下，ABM 不是正确的工具，它在这里主要是一个隐喻生成器。** 它在转移律层有条件地有用，但必须先满足 §9 的七道门。
7. **框架清单纠错**：任务候选中的 `JuSpace` 实为**神经影像学工具箱**（名字冲突），`smallslm` 与 `ASON` 在 GitHub / arXiv / Crossref / DuckDuckGo 四路检索均 0 命中。详见 §2.3。

---

## 1. 判据：什么算"真正可比"

本调查用五个硬条件筛掉"名义相关"：

| # | 条件 | 为什么 |
|---|---|---|
| C1 | **状态是 dyad 的，不是 agent 的** | 若模型里只有 agent 属性 + 网络拓扑，dyad 只是边的标签，则不涉及关系状态表示 |
| C2 | **区分 i→j 与 j→i** | 对齐 `CURRENT_ARCHITECTURE.md` §4「`i->j` 和 `j->i` 是独立分量」 |
| C3 | **有时间推进语义** | 对齐 §6 / §8 的 `X_(t+1) = F(...)` 与 `τ = (history_id, local_time)` |
| C4 | **存在可指认的 calibration / validation 动作** | 用于区分「机制演示」与「经验验证」 |
| C5 | **状态可以有 Unknown / 不确定性 / 观测限制** | 对齐 §3 `Reality != Observation != Belief` 与 §9 `ProvenanceAndUncertainty` |

**通过 C1–C3 的极少。** 通过 C4 的更少。通过 C5 的：**在本 lane 已检索的场所内未找到任何一个。**

> **检索范围声明（`X-14` 要求，与上句同生共死）**：上句是一个**检索结果**，不是**领域总体**结论。本报告的采样框架是 §2 的开放框架清单与 §3 的具名模型清单；**未做**领域总体抽样、未做系统综述、未检索付费库。因此合规的引用形式是「**在本 lane 已审计的检索场所内未找到通过 C5 的模型**」。**禁止**改写为「没有模型通过 C5」或「该维度不存在」。

---

## 2. 开放框架与基础设施（本次实际核实）

### 2.1 已核实存在的框架

| 项目 | 核实指针 | 核实结果（2026-09-27） | 对 LHRM 的可复用性判断 |
|---|---|---|---|
| **Mesa** | `https://github.com/mesa/mesa`；JOSS 10(107):7668, DOI `10.21105/joss.07668` | Apache-2.0。**已从 `projectmesa` 迁到 `mesa` org**（旧 URL 自动跳转）。最新稳定 3.x（v3.5.1），Mesa 4.0 alpha0 已发布。3.5.0 引入 public event scheduling API | **首选**。若写离散事件动力学，Mesa 3.5+ 的 event scheduling API 正好对应 F5 需要的"换 scheduler 做 artefact 检测" |
| **Repast Suite** | `https://repast.github.io/`；`https://github.com/Repast/repast.simphony`；`repast4py`；`repast.hpc` | 20+ 年持续开发。Simphony 2.11.0 (2024-07-01)；**Repast for Python 1.2.1 (2025-11-11)**。RepastJ (1999) 已停止维护但保留 archive。New BSD license。架构原语：**Contexts / Projections / Queries / Watchers** | **Context/Projection 二分值得读**：Context 存可变状态、Projection 只读派生量——这正是 LHRM `WorldState` vs readout 的工程对应 |
| **MATSim** | `https://matsim.org/` | 大规模 agent-based 交通模拟，逐秒推进整天。核心是 **iterative optimization + replanning**：让 agent 重解规划以最小化对目标分布的偏离。官网明示生态内开源/商业 license 混杂 | **机制启发价值 > 直接使用价值**。其 replanning 思路是本 lane 找到的唯一绕开"hand-tuned 增量律"的路线（§8 I6） |
| **CoMSES** | `https://www.comses.net/` | 可访问的模型代码库，含版本化 release。本 lane 定位到 2 个关系/婚恋 codebase：#4458（Sutcliffe & Wang social trust，Java）、#4490（Zinn 个体与伴侣人口学微模拟，ml-DEVS/JAMES II） | **找可复现关系模型的正确入口** |
| **Concordia (Google DeepMind)** | `https://github.com/google-deepmind/concordia`；arXiv:2312.03664 | 生成式社会仿真库。**Game Master / player 分离**：GM 负责环境与结果判定（检查物理可行性），entities 只用自然语言表达意图 | **设计启发**：GM/player 分离与 LHRM §3 `Reality != Observation != Belief` 同构。**但这是设计类比，不是经验证据** |
| **Generative Agents** | arXiv:2304.03442；DOI `10.1145/3586183.3606763`；`https://github.com/joonspk-research/generative_agents` | 25 agents，memory stream + reflection + planning。**validation = ablation + believability**。论文自陈 "long-term planning and coherence remain" | 机制启发有限。**"believable" ≠ "accurate"，更不等于 "predictive of real dyads"** |
| **AgentSociety** | `https://github.com/tsinghua-fib-lab/agentsociety` | AgentSociety 2 为 LLM-native（CodeGen/ReAct/Plan-Execute/Two-Tier/Search 路由器，Ray Tasks，JSONL replay + DuckDB）；1.x 为 gRPC 城市模拟器 | 规模工具。**与 LHRM 第一阶段目标无关** |
| **JuliaDynamics/Agents.jl** | `https://github.com/JuliaDynamics/Agents.jl` | MIT。纯 Julia。同时支持离散时间与**连续时间 event-queue** ABM；官方维护开源框架对比仓库 `JuliaDynamics/ABM_Framework_Comparisons` | 其"同一模型两种时间语义"的能力**正是 F5 需要的对照实现** |
| **RSiena / SIENA** | `https://cran.r-project.org/web/packages/RSiena/`；`https://www.stats.ox.ac.uk/~snijders/siena/RSiena_Manual.pdf` | Simulation-based estimation of SAOM。有向/无向/二模/共演化；含参数检验与拟合优度 | **必读源码**（理由见 §3 F2） |
| **SOTOPIA / SOTOPIA-π** | DOI `10.18653/v1/2024.acl-long.698`（ACL 2024, pp.12912–12940）；后继 DOI `10.18653/v1/2025.acl-long.1203` | 存在性已核实。**本次未读正文**，不对其 ground-truth 设计作任何主张 | 待读 |

### 2.2 值得认真工程阅读的短名单（5 个，附理由）

1. **RSiena / SAOM** — <https://cran.r-project.org/web/packages/RSiena/>
   唯一同时具备"有向二人状态 + 似然估计 + 拟合优度检验 + 效应相对重要性"的成熟实现。**读它不是为了采用它**（见 F2 的排除判据），而是为了知道**一个已被检验过的二人动态模型需要哪些零件**——尤其是 `interpret_size` 的 relative importance 思路，可以直接启发 LHRM 的 redundancy 审计。

2. **Social Relations Model 的方法学** — Kenny & La Voie (1984) *Adv. Exp. Soc. Psychol.* 18:141–182, DOI `10.1016/S0065-2601(08)60144-6`；Malloy & Kenny (1986) *J. Personality* 54(1):199–225, DOI `10.1111/j.1467-6494.1986.tb00393.x`；Back & Kenny (2010) *SPPC* 4:855–870
   LHRM 方向性分解的统计学祖宗。**必读 Malloy & Kenny (1986) 的三点**：actor/partner/relationship 三分量命名、它被定义为 generalizability theory 的特例、以及**它要求 round-robin 设计**（这一条是 LHRM 未来的一个硬约束，必须知道）。

3. **Galán et al. (2009) *Errors and Artefacts in Agent-Based Modelling*, JASSS 12(1)1** — <https://www.jasss.org/12/1/1.html>
   **最短、最可操作的"防自欺"工具书**。core/accessory assumption 二分 + 具体的 artefact 检出活动清单（换 neighbourhood 拓扑、换 agent 调度顺序、换编程语言重实现、跨编译器浮点比对、跑极端情形与可解析特例）。可以直接改写成 LHRM 动力学层的 verification protocol。

4. **Schindler (2013) *About the Uncertainties in Model Design and Their Effects*, JASSS 16(4)6, DOI `10.18564/jasss.2274`** — <https://www.jasss.org/16/4/6.html>
   **equifinality probe 的方法模板**。在同一设计策略下造 8 个同样可辩护的版本，结果"magnitude 和 direction 都显著不同"，甚至出现符号相反的趋势。R01/R02/R06 若只做语义反例攻击，会漏掉这一整类失败。

5. **Conroy-Beam (2021) *Couple Simulation: A Novel Approach for Evaluating Models of Human Mate Choice*, PSPR** — <https://par.nsf.gov/biblio/10223261-couple-simulation-novel-approach-evaluating-models-human-mate-choice>
   **目前唯一一条"用真实个体轨迹做模型鉴别"的协议**。它做的事正好是 LHRM 若要谈转移律就必须做的事：把候选模型丢进一个模拟婚恋市场，看谁能**重建真实 couple**，然后用这个能力**区分不同模型**。

> 附加（低成本高回报）：**Lawson & Park (2000) JASSS 3(1)2** <https://www.jasss.org/3/1/2.html> —— 半页就能读完的"同步时间推进会制造伪动力学"的一手复现失败案例。

### 2.3 框架清单纠错（`NEGATIVE` 结果，2026-09-27 实测）

| 任务书候选 | 实测结果 |
|---|---|
| **`JuSpace`** | **不是 ABM 框架。** 可核实的 JuSpace 是 Julich 的**神经影像学工具箱**（MRI 与 PET/SPECT 递质图的跨模态空间相关），论文 Dukart et al. (2021) *JuSpace: A tool for spatial correlation analyses of magnetic resonance imaging data with nuclear imaging derived neurotransmitter maps*, *Human Brain Mapping*, DOI `10.1002/hbm.25244`；代码 `https://github.com/juryxy/JuSpace`（Matlab + SPM12）；官网 `https://www.fz-juelich.de/en/inm/inm-7/resources/tools/juspace`。**该项目已停更，后继为 NiSpace**（Lotter & Dukart, Zenodo 2024）。**名字冲突，判为不采用。** |
| **`smallslm`** | GitHub Search API `q=smallslm&in:name` → `total_count: 0`（同一 API 用 `q=repast` 返回 421，证明查询通道有效）；arXiv API `all:smallslm` → 0；Crossref → 0；DuckDuckGo → 0。**`UNVERIFIED_OR_UNKNOWN`，倾向不存在。** |
| **`ASON`** | GitHub Search API `q=ASON+agent+social+network` → 0；`q=ASON+social+network+simulation` → 0；DuckDuckGo → 0。**`UNVERIFIED_OR_UNKNOWN`。** |
| **`SoS`** | 本次未做穷尽检索。**`UNVERIFIED_OR_UNKNOWN`。** |
| **`NetLogo` / `MASON`** | 本次**未直接核实**。仅作为二手指纹存在（Mesa README 原文："Its goal is to be the Python-based alternative to NetLogo, Repast, or MASON"）。**`UNKNOWN_AS_OF`。** |
| **`Timms & Griffiths (2007)`**（疑似"模拟社会关系"论文） | 多路检索 0 命中。**`UNVERIFIED_AS_OF_2026-09-27`，不引用。** |
| **`Kuran & Miller (2000)`**（"Simulating the life of markets"） | Crossref 无命中；JASSS 3(1)1 与 3(1)2 均为其他论文；DuckDuckGo 0 命中。**`UNVERIFIED_AS_OF_2026-09-27`，不引用。** |

> 方法论注记：这四条负结果是本报告的**组成部分而非失败**。契约要求"核实链接与包名真实存在；不要发明项目"。发现上游清单里的三个名字无法核实，本身就是需要上报的发现。

---

## 3. Named 模型卡片

### 3.1 社会统计模型（非 ABM，但最接近 LHRM 的对象）

#### C-SRM · Social Relations Model
- **状态表示**：`X_ij = A_i + P_j + M_ij + E_ij`，对每个 construct 独立成立。`A` = actor effect（i 的一般倾向），`P` = partner effect（j 的一般效应），`M` = relationship effect（**特定这一对**的残差），`E` = error。原文称之为 generalizability theory 的特例。
- **转移规则**：**无。** 这是横截面方差成分模型。
- **校准来源**：真实数据（round-robin 设计的知觉/行为评分）。
- **方向性**：**天然有。** 每个 construct 分别估 `i→j` 与 `j→i` 的方差。
- **Belief / partial observation**：不建模。它是"关于 A→B 的评分"的自变量结构，不区分 reality 与 observation。
- **原作者 validation**：方差成分分解的统计显著性、self-report 的 reliability/validity 估计。
- **可复用想法**：把 LHRM 的 `Candidate Minimal Directed Basis v0.1`（8 个 construct）当作 8 个 SRM 坐标，分别做 actor / partner / relationship 分解 → 直接回答 `PARAMETER_CONVERGENCE_V0_1.md` §2.1 semantic independence 与 §2.3 conditional incremental information。
- **常见失败 / toy assumption**：**三个硬代价**：
  1. **要求 round-robin 设计**（每人须与多个 partner 互动）才能把 actor 与 relationship 分离。**LHRM 的 Court-fact Case Bank 是单一 dyad 深度材料，结构上不满足此识别条件。** 不能直接用。
  2. **把 residual 归给"relationship"**，不区分"这一对的真实共享事实"与"测量误差/个体特异噪声"。LHRM 明确要求 `ProvenanceAndUncertainty` 独立成层，SRM 做不到。
  3. 常见误用：把 `M_ij` 当成"关系质量"读数。**它不是**，它只是没被 actor/partner 解释掉的部分。

#### C-SAOM · Stochastic Actor-Oriented Model / RSiena
- **状态表示**：邻接矩阵。`x_ij ∈ {0,1}`，**严格二值**（"Weighted networks are not allowed"）；可多模、可与行为共演化；actor/dyadic covariates。**证据等级 `VERIFIED`。**
  > **Round-3 限定（重要）**：「严格二值」这一表述**在 SAOM 的主体设定内成立，但同页存在例外条款**（Round-2 复核在同页定位到例外句）。本轮**未打开该页原文**，例外句的准确内容与范围记为 `NOT_OPENED`。**因此**下方由「严格二值」推出的任何 LHRM 侧结论**均不成立**（见 Round-3 推论更正）。
- **转移规则**：把所有网络变化分解为 **ministeps**，每一步一个 actor 创建或终止一条出边。目标函数分三个函数：**evaluation**（无边时的变化）/ **creation**（新边）/ **endowment**（既有边）。三者在统计上是**多项选择**（不是二元），参数解释为 log-probability ratio。**关键限制：三者不可同时出现在同一模型中（完美共线）。证据等级 `PLAUSIBLE` —— 本轮未定位到出处。**
  > **Round-3 证据降级**：「三函数不可同时出现（完美共线）」此前以与「严格二值」相同的确定语气写出。Round-2 复核判定该条 **`PLAUSIBLE`（未找到出处）**。本轮**未打开 RSiena manual 或 Snijders et al. 2010 正文复核该句**（`NOT_OPENED`）。该限制在 §8 `I2` 里被用作「三者的更新律不可合并」的支撑 ⇒ **`I2` 相应降级**，见 §8 Round-3 补记。

- **结构效应清单**（可复用于 LHRM）：out-degree effect、**reciprocity effect**、transitive triplets / balance / transitive ties / distance-two、three-cycles、in/out-degree popularity & activity。**balance 效应的定义值得单独抄**："a preference for ties to those others who have a **similar set of outgoing ties**"，且**同时计算同向选择与同向不选择**（`x_ih = x_jh = 1` 与 `x_ih = x_jh = 0`）——这是处理"结构等价"而非"结构相似"的正确形式。
- **校准来源**：真实**网络面板数据**（≥2 wave）。
- **方向性**：**完全支持。** `i→j` 与 `j→i` 是两个独立变量。整篇入门文献的主线就是"如何估计有向网络的动力学"。
- **Belief / partial observation**：不建模（不处理 actor 对他人 tie 的错误认知）。
- **原作者 validation**：Monte Carlo 似然估计 + **参数检验** + **拟合优度检验** + **效应的相对重要性**（Indlekofer & Brandes 2013；Snijders 2004 的 entropy-based effect size）。
- **可复用想法**：creation / endowment / evaluation 三分**直接映射 LHRM §6 的 `Action/Event` 落点**——同一个行为落在哪一类，决定它更新 `X` 的方式，且三者的更新律不可合并。`Mutuality_k = H(Z[k,i,j], Z[k,j,i])` 的可计算版本可直接借用 balance + reciprocity 两个结构性效应。
- **常见失败 / toy assumption —— 以及本条为何对本 lane 最关键**：
  Snijders, van de Bunt & Steglich (2010) 原文：
  > "Ties are supposed to be, in principle, **under control of the sending actor** (although this will be subject to constraints), **which will exclude most types of relations where negotiations are required for a tie to come into existence**."

  伴侣、亲属、照护、合作都属于"tie 的存在需要双方协商"的类型。**SAOM 的成功前提（单边 tie 控制）与 LHRM 的对象前提（双方共同构成的关系）互斥。**（引语与 DOI 均 `VERIFIED`。）
  另：该文献明确批评早期纯 ABM 网络模型"lack an **explicit estimation theory**… they cannot be used for purposes of theory testing in a statistical model"。**这句话同样适用于 LHRM：没有估计理论的模拟模型不是理论检验工具。**

  > **Round-3 推论更正（撤回，2026-09-28）**
  >
  > **被取代的原文（接上句）**：「同时二值化也**直接违反** LHRM 的混合态表示。」
  >
  > **撤回依据**（`WRONG-SCOPE`，Round-2 `R-G3` / `G-C16` 复核）：该推论**遗漏了同页的例外句**，因此是**不完整引用上的推论**。`X-14` 的精神同样适用于此 —— 拿一段被截断的来源陈述去推 LHRM 侧的结论，与把检索失败写成领域不存在是同一类错误。
  >
  > **本轮未打开该页原文**，例外句内容记为 `NOT_OPENED`；**因此本轮既不主张「二值化不违反混合态表示」，也不主张它违反。** 只声明：**该推论在当前证据状态下不成立。**
  >
  > **仍然成立的部分（不依赖被撤回的推论）**：上文的**单边 tie 控制 / 需协商的关系类型被排除**这一条**独立成立**（引语逐字、DOI 已核实），它是本报告对 SAOM 的**结构性**排除判据（§11 非主张 10、`§8 I4`）。**SAOM 被排除的理由是「对象前提互斥」，不是「二值化」。**

#### C-APIM · Actor–Partner Interdependence Model
- **状态**：`UNKNOWN`。本 lane 未检索。这是与 SRM 并列的二人方法学重要分支，**很可能是本报告的真实缺口**。见 §12。

### 3.2 关系 / 婚恋类 ABM（**这里没有一个能通过 C1–C3**）

#### C-MADAM · Hills & Todd (2008), JASSS 11(4)5 — <https://www.jasss.org/11/4/5.html>
- **状态表示**：`X_pair = (matched trait count, relationship duration)`。个体状态 = trait set（`k` 个，从 `N` 个中抽）+ **satisfice level `j`**（个体级，指数松弛 `j_t = j_0 · λ^t`，`λ ~ N(μ, σ)`）。就这些。
- **转移规则**（每年离散一步）：未婚者每年随机遇到 `x` 个异性；若匹配 trait 数 ≥ 双方各自的 `j` 且双方均同意 → 成婚，`j` 锁定在当前匹配水平。已婚者若遇到匹配数**超过当前配偶**且**对方也接受**的新个体 → 离婚并再婚（"trade up"）。年底所有未婚者的 `j` 继续松弛。
- **校准来源**：**真实数据 + 5 个自由参数**。先用 US 1990 marriage-by-age 曲线拟合（"by visual inspection"），再用该参数组预测 **US 1996 离婚统计**。结果：P(初婚以离婚告终) 0.47（数据 0.50）；以离婚告终的初婚时长中位数 6 年（数据 7–8 年）；终生未婚 ~6%（数据 50 岁以上 <5%）。
- **方向性**：**完全没有。** `j` 是**个体**属性，匹配度是**对**属性。`Duration` 与 `match` 都是对称标量。**违反 LHRM §4。**
- **Belief / partial observation**：无。
- **原作者 validation**：**这是本 lane 中最接近"正确"的一次。** 校准目标与验证目标是**不同变量**（婚姻年龄曲线 → 离婚统计），且相隔 5 年。作者还主动跑了 disassortative 变体并报告"not qualitatively different"。作者自我设限也做得不错："MADAM's flexibility could allow more complicated mechanisms for divorce to be modeled… a prerequisite to these extensions is finding supporting evidence for their necessity."
- **可复用想法**：**指数松弛的期望下调**（`j_t = j_0·λ^t`，`λ` 异质且可从 panel 估）是一条**具体、有数学形式、可估计**的机制，比"扣分"更接近可辩护。对 LHRM 的候选落点：`Dedication` / `OutcomeDependence` 的期望随时间下调。注意这只是 `MODEL_HYPOTHESIS`。
- **常见失败 / toy assumption**：dyad interior 是空的。作者自己承认 divorce 规则"simple"。**更根本的失败是：它证明了"配对人口学可拟合"，却没有为"关系内部状态"提供任何证据。** 一个新的 LHRM 式模型若只用 MADAM 的骨架 + 换几个 trait，得到的仍是人口学拟合，与关系状态表示无关。

#### C-SexualPartnership · Knittel, Riolo & Snow (2011), *Adaptive Behavior*；PMC7083591
- **状态表示**：agent = `quality`（对他人的吸引力）、`aspiration`（目标质量）、`courtship duration`、`waiting threshold`、`ideal number of partners`；pair = dating 状态 + 周数 + 潜在 date 列表。离散时间，**周为一步**。允许**多重 + 并发**伴侣关系（这是它相对前代的关键改进，前代普遍假设"一次婚配终身"）。
- **转移规则**：撮合（propose → accept / 已有对象则 weighted evaluation）→ 成为 couple → 约会满 courtship duration 且双方 max 未满 → 成为性伴侣。解除：随机 break-up（按 duration 概率）、遇到质量更高的对象、或 max 达上限。
- **校准来源**：**真实全国性数据**（National Survey of Family Growth；National Longitudinal Survey of Adolescent Health；National Health and Social Life Survey）。作者称"Model behavior was tested across a wide range of parameters and compared with empirical data"。
- **产出**：终生伴侣数、近一年伴侣数、并发率、关系时长，以及**伴侣间 quality 的相关结构**。
- **方向性**：**结构性缺失。** `quality` 是个体属性；"couple" 的存在靠双方互选，一旦成立，内部只有一个 duration 计数。
- **Belief**：无。
- **validation**：产出量级与真实数据相似 + 伴侣 quality 相关结构与婚姻/约会数据相似。**但这是"量级/结构相符"，不是 dyad-level 轨迹验证。**
- **可复用想法**：并发 / 多重关系的显式建模（对应 LHRM `Environment` 层的 availability set）；agent 的"目标 vs 现实"双变量（`aspiration` vs `actual quality`）形式上是 `Belief` 层的**极简版**，但作者并未把它当作 belief 处理。
- **常见失败 / toy assumption**：`courtship duration`、`waiting threshold` 为**个体参数**而非 `(i,j)` 参数；weighted evaluation 的权重无经验估计。实现于 Repast J，代码在 OpenABM（可复现资产）。

#### C-CoupleSimulation · Conroy-Beam (2021), *PSPR* — <https://par.nsf.gov/biblio/10223261-couple-simulation-novel-approach-evaluating-models-human-mate-choice>
- **这不是一个关系状态模型，而是一个模型鉴别协议。** 因此它对本报告的价值高于前面所有模型。
- **做法**：把"择偶"建模为 exploration–exploitation 权衡，即 **multi-armed bandit** 问题。候选算法中，**reciprocity-weighted Thompson sampling** 表现最好——在有噪搜索环境中有效引导择偶搜索，并能**复现真实参与者的择偶结果**（样本 **k = 522 real-world romantic dyads**）。**couple simulation** 进一步把候选模型放进模拟婚恋市场，看谁**能重建真实 couple**，并据此**区分不同模型**；论文报告该方法 (a) 成功重建真实世界 couple，(b) 能区分择偶模型，(c) 能预测**广谱的关系质量维度**。
- **方向性**：**有，且是被当作机制用的**——"reciprocity-weighted"意味着 `X_ij` 与 `X_ji` 的差会影响 A 的选择。
- **原作者 validation**：**这是本 lane 唯一的"out-of-sample + 模型鉴别"实例**。真实 couple 样本在模型选择过程中充当 ground truth。
- **可复用想法**：**这是 LHRM 若要谈转移律时唯一一条被验证过的现成协议。** 见 §9 Gate 3。
- **常见失败 / toy assumption**：本 lane **未读正文**，因此不主张其 ground truth 的构造细节、也不主张其结果可外推到非婚恋 dyad（朋友、亲属、照护）。**`UNKNOWN`。**

#### C-TrustModel · Sutcliffe, Wang & Dunbar (2015), *ACM TOIT* 15(4):16, DOI `10.1145/2815620`；前置版本 Sutcliffe & Wang (2012) *JASSS* 15(1), DOI `10.18564/jasss.1912`（`CITED_SECONDARY`）；代码 CoMSES #4458
- **状态表示**：ego 对每个 alter 的 **trust / relationship strength 单标量**。无 dyad 状态，无方向分解之外的内容。
- **转移规则**：交互频率↑ → trust 增益（smoothing，使强关系更抗衰减）；负面交互 / 背叛 → 折减；**waning**（衰减）。四种 partner-preference 策略（favour-the-few / midway / favour-the-many / staged），并让 `per`（起始 strong-tie 策略占比）**经 mutation 演化**。工作/社交的时间比 `WS` 构成资源竞争。
- **校准来源**：**文献经验观察，而非拟合。** 原文明确写 "Frequency of interaction is equated with strength of relationships, following empirical observations [Roberts and Dunbar 2012; Rose and Serafica 1986]"。**没有与真实二人关系纵向数据比对。**
- **方向性**：弱。ego 侧有对 alter 的 trust，alter 侧有独立的 ego 结构，但并非同一 construct 的 `i→j` / `j→i` 分解。
- **Belief**：无。
- **原作者 validation**：**参数敏感性分析**（原文："The sensitivity analysis described above demonstrated the model was robust using a wide range of parameters"）+ 复现 Dunbar 社会脑假说提出的自我中心网络多层结构（少强关系、多中、更多弱）。**不是对真实二人关系的验证。**
- **可复用想法**："衰减率高于增益率则强关系无法形成"这一**阈值结构**是可复用的动力学直觉；`mutation` 演化策略偏好是一个可选的 meta 层。
- **常见失败 / toy assumption**：把"交互频率 = 关系强度"当作**前提**而非待验假设；trust 是单标量，不承载 directional / construct-specific 语义。**它是机制演示的典型样本。**

#### C-Microsim · Zinn (2015), CoMSES #4490 — <https://www.comses.net/codebases/4490/releases/1.0.0/>
- **状态表示**：**continuous-time multi-state model** 定义个体与伴侣的 life course；**agent-based** 只用于 mate matching。
- **转移规则**：ml-DEVS 形式化，macro-DEVS 驱动 partnership onset / dissolution / birth / death；micro 组件（individual、couple）处理 life-course 动力学。
- **校准来源**：**真实人口数据**（荷兰）。原文措辞谨慎："We illustrate the potential of the presented approach by projecting a **hypothesized population** based on the population of the Netherlands."
- **方向性**：成对判定用"empirical likelihood equation"估"某男某女成对概率"，再由双方 aspiration level 决策 → **有方向性，且是双向同意式**（这与 SAOM 的单边控制形成鲜明对比，值得注意）。
- **validation**：对假定人口的投影演示。**不是 dyad 级验证。**
- **可复用想法**：**"continuous-time multi-state"** 是 LHRM 转移律的一个现成实现形态候选（对照 §11「不采用预枚举状态机」——注意 multi-state 在这里是 **partner status（制度事实）** 的状态机，恰好对应 LHRM 的 `PairState` / `Relationship Identity` 层，**不是**关系状态的引擎。这个区分很重要，值得 R09 注意）。
- **常见失败 / toy assumption**：`aspiration level` 被设为**随机抽取的单一值**；"hypothesized population" 的措辞说明其人口输入本身是假定的。

#### C-AttachmentDyads · Darling, Burns & Grubb (2016)
- **状态表示**：三种 relationship style（secure / avoidant / anxious，loosely based on attachment theory）。
- **转移规则**（README 原文）："Couples are randomly paired, with the duration of the new relationship **assigned as the mean of the durations of the two styles**."
- **校准来源**：**folk psychology**。README 自己写 "loosely based on attachment theory"，并明确说明该模型的目的是研究**抽样偏倚**（cross-sectional dyadic samples 的 truncation），不是关系动力学。
- **方向性**：**完全无。** `Duration(A,B) = mean(f(style_A), f(style_B))`——把两人折叠为一个对称标量。
- **validation**：无（draft / conference presentation）。**`LOW` 证据强度。**
- **为什么仍然列进来**：它是**教科书级的 toy assumption 样本**。`mean(f(A), f(B))` 形式上满足"低冗余"（只有一个输出），实际上把 LHRM §4 明确禁止的"由两个方向派生出一个总分"当成了机制；同时它把 attachment style（Agent 层的倾向）**直接当作关系层参数**。**它能跑通、能产故事、也没有任何人质疑——这正是 §7 失败目录第 C3/C4 条的活标本。**

### 3.3 机制演示型（含 LLM 社会仿真）

#### C-GenAgents · Park et al. (2023), UIST；arXiv:2304.03442
- 状态 = LLM 上下文（memory stream + reflections + plan）。
- 转移 = LLM 依据 retrieved memory + reflection 生成下一个 plan。
- 校准 = **无**。
- **原作者 validation = ablation + believability**（"observation, planning, and reflection… each contribute critically to the **believability** of agent behavior"）。
- **怀疑性阅读**：ablation 只能证明"去掉某组件会降低 believability"，不能证明"believability 接近真实关系"。LLM 的行为先验来自训练语料，作者**没有**检验该先验是否与真实人类二人关系一致，也没有检验"多个 LLM agent 之间的互动"是否产生任何真实关系数据中的结构。**这是最容易被误引为"经验验证"的一类结果。**
- 自陈限制："long-term planning and coherence remain"（长程一致性问题未解决）。
- **可复用想法**：memory + reflection + plan 三段式是一个**工程上成熟**的 belief-layer 组织方式（对照 LHRM §8 的 nested belief / simulated world）。
- **常见失败**：**把 agent 间互动日志当作关系数据。** LHRM 的 Case Bank 纪律（法院/官方材料=实证覆盖；虚构=表达力压力测试）正是防止这一滑坡的护栏。

#### C-Concordia · Vezhnevets et al. (2023), arXiv:2312.03664
- 状态 = entity 的自然语言 context + GM 维护的环境状态。
- 转移 = entity 表达意图 → **GM 判定结果**（"checking physical plausibility in simulated worlds"）。
- validation：**本 lane 未核实**。README 未声明经验验证。
- **可复用想法（对 LHRM 最有价值的一条）**：**GM 与 player 分离**在结构上等价于 LHRM 的 `Reality != Observation != Belief` 分层——"让 LLM 跑 Belief 层，绝不让同一个 LLM 判定 Reality 层"。**这是架构类比，不是经验证据。**
- **常见失败**：GM 判定 = 一个未被校准的 oracle。若把 GM 当成"现实"，整个模拟就没有独立的现实锚点（这正是 Windrum et al. 说的 auto-referential risk）。

#### C-ABIR · Lustick (2000), JASSS 3(1)1 — <https://www.jasss.org/3/1/1.html>
对象是集体身份（族群/民族）而非二人关系，但**它是本报告引文密度最高的一份文献**，因为它是对"ABM 社会仿真如何自欺"最坦率的一手记录：
- **方法论交易条款（原文）**："the trade-off made in the choice for agent-based modeling approaches is **acceptance of the nearly complete artifactuality of the findings** (There is no direct need for field data to gather for purposes of testing the model.) in return for the capacity to run very controlled experiments"
- **folk psychology（原文）**："the rules for choosing some among a vast number of possible algorithms, are not themselves produced by a theory about the world… the architects of the models often resort to **folk theorems based on little more than anecdotal and impressionistic frames of reference**"
- **"good tricks"（原文）**："The ready availability of contradictory folk theorems opens the door wide to the temptation to make judgments about the construction of the model based on **preliminary exploration of the virtual space created by alpha versions** of the model, or by general accumulated knowledge of the '**good tricks**'… which lead to interestingly patterned results"
- **把结论写进规则（原文，针对 Axelrod *Disseminating Culture*）**："A powerful tendency toward convergence, in other words, **is built into the model (not really emergent from complex interactions within it)** by algorithmically producing more contact with similarity, and, automatically, more similarity… These rules are far stronger, it would appear, than the theories to which reference is made would justify."
- **形式严谨 ≠ 现实性（原文）**："Because the models run on computers there is no room for ambiguity in the specification of the model's underlying rules. While this means that some **stipulative 'patches'** must be used to operationalize the theoretical hunches…"
- 作者自陈不做点预测（脚注 1，引 Fearon 1997）："I am not interested in using ABM to make point predictions… such predictions are not possible using this kind of model. Our focus instead is explaining variation in **distributions** of outcomes."

---

## 4. 机制演示 vs 经验验证（分离声明）

### 4.1 分级

| 类别 | 本 lane 样本 | 原作者的 validation 实际是什么 |
|---|---|---|
| **机制演示型** | C-GenAgents, C-Concordia, C-TrustModel, C-ABIR | ablation、believability、参数敏感性、scenario sweep、成百上千次虚拟历史 |
| **人口学拟合型** | C-MADAM, C-SexualPartnership, C-Microsim | 匹配真实人口统计曲线 / 分布量级 |
| **模型鉴别型** | C-CoupleSimulation | 要求模型重建**真实个体**并据此区分模型 |
| **随机实验型** | Centola (2010) *Science* 329(5996):1194–1197, DOI `10.1126/science.1185231`（**本次仅核实著录，未读正文，细节 `UNKNOWN`**） | 真实 RCT + 显式模型比较 |

### 4.2 硬证据与元证据（支持"整个 ABM 社会仿真文献默认是机制演示"这一判断）

> **Round-3 分级总表（2026-09-28；三条的证据状态不同，不得并列为「三条硬证据」）**
>
> | # | 内容 | **Round-3 证据状态** | 本轮是否打开原文 |
> |---|---|---|---|
> | 1 | Lustick (2000) 领域内部自认 | **`VERIFIED`**（本报告 §3.3 逐字引文） | 是（Round-1 已实读） |
> | 2a | Angus & Hassani-Mahmooei (2015) 的 TS 建模稀少的转述 | **`PLAUSIBLE`** | **否（`NOT_OPENED`）** |
> | 2b | Grazzini & Richiardi (2015) 的**依赖图**部分 | **`VERIFIED`**（Round-2 复核）；**方向与本报告所述相反（对本项目有利）** | **否（`NOT_OPENED`）** |
> | 3 | Windrum et al. (2007) 领域诊断 | **`VERIFIED`**（§7 C1/C6/C8/C9 逐字引文） | 是（Round-1 已实读） |
>
> **对 §4.2 标题的修正**：本节标题此前称「三条**硬证据**」。**只有第 1、3 条是硬证据**；第 2 条是 `PLAUSIBLE` 转述 + 一条方向相反的 `VERIFIED` 结论。

1. **来自领域内部的自认**：Lustick (2000, §2.5) 把 ABM 的方法论交易明确写成"接受发现的近乎完全的人造性"，并因此专门撰文批评 Axelrod 等人用 folk theorem 造 agent 规则。**这不是外部批评者的攻击，是一个领域内 leader 对默认状态的承认。**
2. **元证据**：Grazzini & Richiardi (2015) *JASSS* 18(4)4 报告，Angus & Hassani-Mahmooei (2015) 扫描 100+ 篇 JASSS ABM 论文，"found **very few instances** of additional (statistical) modelling of TS data"。即：ABM 输出几乎不被当作随机过程再做统计推断。
   > **Round-3 证据分级更正（2026-09-28）**：本条此前与第 1、3 条并列为「三条硬证据」，语气相同。**实际证据状态不同**：
   > - **Angus & Hassani-Mahmooei (2015) 那条 = `PLAUSIBLE`，本轮 `NOT_OPENED`。** 本报告**未核实该文原文**，只经 Grazzini & Richiardi 转述。**其「100+ 篇」与「very few instances」两个数字不得作为已核实数字引用。**
   > - **依赖图部分 = `VERIFIED`，且方向与本报告所述相反。** Round-2 复核独立判定 Grazzini & Richiardi 的依赖图部分成立，**且其方向对本项目有利**（见 §4.2 补记与 §10 Round-3 补记）。本轮**未打开该文原文复核该部分**（`NOT_OPENED`），故按复核结论记录并标注来源。
   > - **本条不得再被并列为「三条硬证据」中的等同一条。** 它现在是一条 `PLAUSIBLE` 转述 + 一条 `VERIFIED` 依赖图结论。
3. **领域诊断**：Windrum, Fagiolo & Moneta (2007) *JASSS* 10(2)8 —— "AB modellers tend to deal with **in-sample** data (i.e., their prime aim is to replicate statistical properties of past data). **Out-of-sample exercises… are less frequently carried out** by AB economists"；并指出该领域 "an excess of heterogeneity with respect to the range of competing models and a **lack of consensus on core methodological questions**"，且 "orthodox economists have not been moved" 的原因之一是 "a perceived lack of robustness in AB modelling"。

### 4.3 唯一的"正确交易条件"被写下来了

Windrum et al. 同文记录了一条被反复引用的诊断（转述自 Edmonds & Moss 2005，**本次未核实该文确切出处**）：

> "One possible reaction is to use the computer as an artificial laboratory in which basic, causal relationships can be tested… **The danger of this strategy is that one ends up building auto-referential formalisations that have no link to reality.**"

**这句话精确命中 LHRM 的最高风险点。** 一个"关系转移律"，如果本质上是人写的关于关系的常识故事，它就是自指的；它能生成任意多条"合理轨迹"，而这些轨迹与真实 dyad 无关。

---

## 5. 状态-规则-校准-方向性-验证 对照总表

| 模型 | State representation | Transition rules | Calibration source（真实数据?） | Dyadic directionality | Belief / partial obs. | 原作者 validation | 证据强度 |
|---|---|---|---|---|---|---|---|
| **SRM** | actor + partner + relationship + error（三分量方差成分） | **无**（横截面） | ✅ 真实 round-robin 数据 | ✅ 每个 construct 独立估 i→j / j→i | ❌ | 方差成分显著性、self-report reliability/validity | HIGH |
| **SAOM / RSiena** | 二值有向邻接矩阵 | ministep：outgoing tie 的 creation / endowment / evaluation；三函数不可同时 | ✅ 真实网络面板（≥2 wave） | ✅✅ 完整支持 | ❌ | Monte Carlo 似然 + 参数检验 + 拟合优度 + 效应相对重要性 | HIGH |
| **APIM** | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | **未检索** |
| **MADAM** | matched trait count + duration + 个体 satisfice level | 年步：匹配 + 期望指数松弛 + "trade up" 离婚 | ✅ 真实 US 婚姻/离婚统计 | ❌ **完全没有** | ❌ | 校准婚姻曲线 → **预测** 5 年后离婚统计（本 lane 最佳） | HIGH |
| **Sexual partnership (Knittel et al.)** | 个体 quality / aspiration / courtship / threshold / max + pair dating 状态与周数 | 周步撮合 / 升级 / 三类解除 | ✅ 真实美国全国调查 | ❌ | ⚠️ aspiration vs actual 形式相近但**未作 belief 处理** | 宽参数扫描 + 与全国数据比对 | MEDIUM-HIGH |
| **Couple simulation (Conroy-Beam)** | bandit 式择偶策略 + reciprocity 权重 | Thompson sampling（探索/利用） | ✅ **k = 522 真实 dyads** | ✅ reciprocity-weighted | ⚠️ 搜索噪声即部分可观测性 | **模型能重建真实 couple + 区分模型 + 预测多维关系质量** | MEDIUM-HIGH（未读正文） |
| **Social trust model (Sutcliffe et al.)** | ego→alter trust 单标量 | 频率增益 + waning + smoothing + 策略 mutation | ❌ **假设**（引文献观察，非拟合） | ⚠️ 弱 | ❌ | 参数敏感性 | HIGH |
| **Microsim (Zinn)** | continuous-time multi-state life course + ABM 择偶 | ml-DEVS；双方 aspiration 同意式撮合 | ✅ 荷兰人口（但称 "hypothesized population"） | ✅ 双向同意 | ❌ | 人口投影演示 | HIGH |
| **Attachment dyads (Darling et al.)** | 三种 style | **duration = mean(两人 style duration)** | ❌ folk psychology | ❌ **对称标量** | ❌ | 无 | **LOW** |
| **Generative Agents** | LLM memory stream + reflection + plan | LLM 生成下一 plan | ❌ | ❌ | ⚠️ per-agent 记忆（非关系 belief） | ablation + believability | HIGH |
| **Concordia** | 自然语言 context + GM 环境 | 意图 → GM 判定 | ❌ | ❌ | ⚠️ GM/player 分离（结构类似 belief 隔离） | `UNKNOWN` | HIGH（存在性） |
| **ABIR (Lustick)** | 身份 repertoire + 激活身份 | 邻域身份权重 + 阈值切换 + entrepreneur 特权 | ❌ | ❌ | ❌ | 敏感性与多种子重复 | HIGH |
| **Centola (2010)** | 网络 + 健康行为 | 阈值/动态网络扩散 | ✅ 真实 RCT | ⚠️ 定向 tie | ❌ | 真实 RCT 比对 | MEDIUM-HIGH（著录级） |

---

## 6. 数值伪影：固定步长会伪造"关系动力学"

Lawson & Park (2000) *JASSS* 3(1)2 记录了一次**可复现性失败**并定位了根因。作者最初的工作动机就是"our **inability to reproduce** the results Epstein and Axtell obtained"；在"considerable experimentation"之后他们写道："we were **never able to reproduce** the results in Figure III-4"，并给出诊断：

> "we conjecture that the oscillatory behavior… is a **simulation artifact** caused primarily by **synchronous time evolution**"

改用 next-event 异步推进后，振荡消失，且对随机种子不再敏感（作者在 50×50 与 100×100 两种规模上各做了 100 个种子的检查）。

**对 LHRM 的直接后果**：`X_(t+1) = F(X_t, Action_t, Event_t, Belief_t, Constraint_t, Environment_t)` 这个接口**没有指定推进语义**。若用固定步长同步实现，观察到的 hysteresis / decay / tipping / 路径依赖 **都可能是 `F` 的更新顺序与同步锁步的产物，而不是关系性质**。

**更值得警惕的一点**：Gilbert (2007, p.38) —— "…no matter how carefully you have designed and built your simulation, **it will contain bugs**"；Axelrod (1997b) —— "confirming that the model was correctly programmed was **substantially more work than programming the model in the first place**"。Galán et al. (2009) 进一步指出 Axtell & Epstein (1994, p.31) 的观察：**宏观结构对个体扰动的"鲁棒性"本身就会掩盖 bug**（"exacerbates the problem of detecting 'bugs'"）。

> **推论（`MODEL_HYPOTHESIS`，但我认为应写进 future work 的 guardrail）**：在 LHRM 里，一个**跨条件稳定复现**的关系轨迹应当被视为**需要解释的异常**，而不是质量保证。它可能意味着 `F` 对所有参数都太平坦（`F` 写得太弱），也可能意味着某条 accessory assumption 在全局支配（`F` 写得太"巧"）。两者都不合格。

---

## 7. Common-failure catalogue（计算关系模型如何自欺）

> 编号 C1–C15 供跨 lane 引用。每条给出**可判定的症状**与**对应的检出动作**（不是道德训诫）。

| # | 失败模式 | 一手证据 | 可判定症状 | 检出动作 |
|---|---|---|---|---|
| **C1** | **Hand-tuned 参数被表述为"发现"** | Windrum et al. 2007：模型维度可多到"**it can generate any result**… explanative potential **little better than a random walk**" | 参数取值的依据是"这样能复现 X"，而 X 本身是被挑中的 | 写明每个参数的**来源等级**（真实数据 / 文献 / 假设），并把"假设"直接标在文档上 |
| **C2** | **在模拟数据上做验证** | Lustick 2000 §2.5：ABM 的交易条件是"acceptance of the **nearly complete artifactuality of the findings**… **There is no direct need for field data**" | 验证目标是模型自己产生的第二条 trace | 验证目标必须来自模型外部；无法做到就**明确声明这是机制演示** |
| **C3** | **agent 行为规则出自民间心理 / "常识"** | Lustick 2000 §2.7 逐字点名："**folk theorems based on little more than anecdotal and impressionistic frames of reference**" | 规则理由是"人都这样" | 每条规则必须能指到一个**被检验过的构念或已发表的机制**；指不到就标 `MODEL_HYPOTHESIS` |
| **C4** | **把结论写进规则，再用规则"发现"结论** | Lustick 2000 §2.9 评 Axelrod *Disseminating Culture*："convergence… **is built into the model (not really emergent from complex interactions within it)**" | 机制描述与结果之间没有独立的因果链条 | 用 Galán et al. 的 artefact 活动：把该规则换成**同样可辩护的另一种**再跑一次 |
| **C5** | **靠 "good tricks" 与 alpha 版试错调模型** | Lustick 2000 §2.7："**preliminary exploration of the virtual space created by alpha versions**… the '**good tricks**'… which lead to interestingly patterned results" | 改模型的理由是"这样曲线好看" | 记录全部被否决的设计及否决理由（Schindler 式多版本并存），不允许静默丢弃 |
| **C6** | **没有 out-of-sample test** | Windrum et al. 2007 §3.4："Out-of-sample exercises… are **less frequently carried out** by AB economists" | 校准与验证用同一批统计量 | 见 §9 的 out-of-sample 门 |
| **C7** | **不做敏感性分析 / 只做参数敏感性不做设计敏感性** | Windrum et al. 2007 §1.6（领域缺标准做法）；Schindler 2013（**设计层面**的替代实现导致结论方向相反） | 只有"参数扰动 ±10% 结果类似"这一句 | 参数敏感性 **+** 设计敏感性（至少 2–3 个同样可辩护的替代设计） |
| **C8** | **equifinality 未被审视** | Windrum et al. 2007 §4.24："there are, in principle, **a great many combinations of alternative parameter settings that can produce an identical output trace**"；§5.2 同上引 Brock 1999 "unconditional objects" | 只有一个参数点/一个设计版本能给出结论 | 报告"结论在多少个同样可辩护的设置下保持"（Schindler protocol） |
| **C9** | **复现 ≠ 解释** | Windrum et al. 2007 §5.2（转引 Brock 1999）："**replication does not necessary imply explanation**"；并指出 Nelson-Winter (1982) 的高聚合输出"can also be replicated by conventional neoclassical growth models" | 用"复现了几个 stylised fact"支撑因果解释 | 明确区分「输出一致」与「机制一致」；要求第二种机制也能复现同一输出时**主动报告** |
| **C10** | **toy assumption：accessory assumption 支配了结果** | Galán et al. 2009 定义 artefact = "**significant phenomena caused by accessory assumptions that are (mistakenly) deemed non-significant**"；其检出活动：换 neighbourhood 函数、换 grid 拓扑、换 agent 决策调度顺序、换语言/平台重实现、跨编译器浮点比对、跑极端情形 | 更新顺序、步长、PRNG、`Unknown` 填充策略决定结论 | 对 LHRM：`Unknown` 策略、coordinate 更新顺序、belief↔reality 采样独立性，全部列为待检 accessory assumption |
| **C11** | **时间推进语义制造伪动力学** | Lawson & Park 2000：同步推进的"大振荡"是 **simulation artifact**；异步版消失 | 轨迹形态依赖步长或更新顺序 | 同一模型用两种时间语义（固定步长 vs next-event / 连续时间）各跑一遍，结论必须一致 |
| **C12** | **非遍历 / 非平稳未检验就解读单次轨迹** | Grazzini 2012（*JASSS* 15(2)7, DOI `10.18564/jasss.1929`）："Knowing whether a model is **ergodic and stationary** is essential… in order to understand its behavior and the real system it is intended to represent" | 用单次 run 的轨迹讲故事 | 在宣称 `Γ_(A,B)` 可解释之前，先做平稳性/遍历性检验 |
| **C13** | **把形式严谨误当作现实对应** | Lustick 2000 §2.1：代码无歧义 "While this means that some **stipulative 'patches'** must be used to operationalize the theoretical hunches" | 用"我的规则写得很精确"为现实对应辩护 | 逐条列出 patch 及其现实对应物；无对应的即 accessory assumption |
| **C14** | **把 LLM agent 互动日志当作关系数据** | （`MODEL_HYPOTHESIS`，但风险结构清楚） | 从 agent 间对话中抽取"关系状态"并声称发现规律 | LHRM 已有护栏：Case Bank 实证覆盖只用法院/官方材料；虚构材料只做表达力压力测试 |
| **C15** | **"auto-referential formalisation"：转移律本身就是关系故事** | Windrum et al. 2007 §4.3（转引 Edmonds & Moss 2005） | `F` 的每一项都能追溯到"关系是这样的"这句常识 | 问：有没有任何一条 `F` 的项，其存在理由不是"我以为关系是这样"？ |

---

## 8. 可复用的实现 / 数学想法（全部标为 `MODEL_HYPOTHESIS`）

| # | 想法 | 出处 | 落点（假设，不是结论） | 风险 |
|---|---|---|---|---|
| I1 | 指数松弛的期望下调 `j_t = j_0·λ^t`，`λ ~ N(μ,σ)` 个体异质 | Hills & Todd 2008 | `Dedication` / `OutcomeDependence` 的期望随时间下调 | 需 longitudinal panel 估 `μ,σ`；无数据即退化为 hand-tuned |
| I2 | **creation / endowment / evaluation** 三分 | RSiena manual | LHRM §6：`Action/Event` 落在哪一类决定它如何更新 `X`。**三者的更新律不可合并**（SAOM 已证明共线） | 分类本身是模型假设，不是观察事实 || I3 | **reciprocity effect** 与 **balance effect**（同时计同向选与同向不选） | RSiena manual | `Mutuality_k = H(Z[k,i,j], Z[k,j,i])` 的可计算版本；处理不对称 | 仅适用于"结构等价"，不覆盖 dyad 内部语义 |
| I4 | **"tie 在单边控制之下"作为适用性判据** | Snijders et al. 2010 | 反向用作 LHRM 的**适用性测试**：本质需要双方协商的关系，不能只用单边 edge 语义建模 → 支持 LHRM 保留独立 `PairState` 层 | 这是一条**排除性**证据，不是支持性证据 |
| I5 | core / accessory assumption 二分 + artefact 检出活动集 | Galán et al. 2009 | LHRM 动力学层的 verification protocol 骨架 | 活动本身有成本，需要先决定哪些 accessory assumption 值得测 |
| I6 | **iterative replanning / 对目标分布最小化成本** | MATSim | **替代 hand-tuned 增量律**的唯一现成路线：让 `X_(t+1)` 由"在约束下重解一个与观测目标对齐的优化"产生 | MATSim 的目标分布来自移动调查；LHRM 缺对应目标分布 → 目前不可用 |
| I7 | Wald–Wolfowitz 非参数平稳性/遍历性检验 | Grazzini 2012 | 解读 `Γ_(A,B)` 之前的必要前置检验 | 对 LHRM 的小样本 dyad，检验功效可能不足 |
| I8 | GM / player 分离 | Concordia | 让 LLM 只跑 Belief 层；`Reality` 层由非 LLM 组件持有 | 纯架构类比，无经验支持 |
| I9 | 拆分 evaluation 与 creation/endowment | RSiena（引 Cheadle et al. 2013：split 可产生 insight，但会降低统计功效） | "保持"和"新建"在关系状态更新中可能确实不同 | 功效代价在小样本上不可接受 |

> **R12 Round-3 `I2` 降级（2026-09-28）**：`I2` 的落点写「**三者的更新律不可合并（SAOM 已证明共线）**」。「SAOM 已证明共线」这一支撑本轮降为 **`PLAUSIBLE`（未定位到出处）**（见 §3.1 `C-SAOM` 的 Round-3 限定）。因此 `I2` 的落点改为：
> - **不再主张**「三者的更新律不可合并」已被证明。
> - **仍主张**（`PLAUSIBLE`）：creation / endowment / evaluation 的三分**可以**映射到 LHRM §6 的 `Action/Event` 落点，**且这个映射本身是模型假设**。
> - **新增一个更强的、本文件不依赖 SAOM 的理由**：即便三者可共线于一个模型，**LHRM 也不需要这个共线性**——LHRM 的 `Action/Event` 落点是**语义**分类（这一动作更新哪个坐标），不是**统计**参数化。**把 SAOM 的统计限制搬成 LHRM 的语义限制是一次范畴错误。**
> - `I2` 仍为 `MODEL_HYPOTHESIS`。
| I10 | SRM 三分量分解 | Malloy & Kenny 1986 | 对 `Candidate Minimal Directed Basis v0.1` 的 8 个 construct 做 actor/partner/relationship 分解，回答 §2.1/§2.3 | **要求 round-robin 设计；Case Bank 单一 dyad 材料不满足**（见 §3.1 C-SRM） |

---

## 9. 一个 LHRM 对象的 ABM 要可信，需要什么

**门槛（全部满足才算"可信"，缺一项都必须自我降级为"机制演示"）：**

### Gate 1 — Calibration target（校准目标）
必须是**dyad 级、纵向、有方向性标注**的数据。人口统计量（初婚年龄、离婚率）**不合格**——见 F1（MADAM 正是只能做这个）。
**可接受候选类型（待 R04 确认是否存在）**：couples' diary / experience sampling / 双方分别报告的 directed 状态时间序列。
**当前状态：LHRM 无此数据。** 在此之前，任何 LHRM 转移律都只能是 assumed。

### Gate 2 — Validation target（验证目标）
必须是**与校准目标不同的变量**。反例与正例：
- ✅ Hills & Todd：校准婚姻年龄曲线 → 验证离婚统计（相隔 5 年）。
- ❌ 校准"满意度"→ 验证"满意度"。

### Gate 3 — Out-of-sample test（样本外测试）
**推荐协议：Conroy-Beam (2021) 的 couple simulation。**
> 把候选转移律放进模拟婚恋市场/关系场，看它能否**重建一个 held-out 真实 couple 的轨迹**；再用这个能力**区分不同的候选转移律**。

这个协议同时解决了三件事：(a) out-of-sample，(b) 模型间的相对比较（而非"我这个模型能跑出故事"），(c) 给出"哪个模型更接近真实"的**可判据**。
**注意**：LHRM 的对象是**一般 Human Dyad**，不是婚恋。因此 Conroy-Beam 协议需要**改造**：用非婚恋 dyad（朋友、亲属、照护、冲突）重做一遍。这本身是一个可立项的研究任务。

### Gate 4 — Equifinality probe（等终局性探测）
**推荐协议：Schindler (2013)。**
1. 选定一个**已被使用过、有真实数据**的设计策略；
2. 系统列出该策略**允许的其它同样可辩护的设计**（至少 2–3 个部件各 2 个备选）；
3. 全部实现，跑出结论矩阵；
4. **只报告在所有版本下都成立的结论**；把方向相反的结论显式列出。

**对 LHRM 的具体建议**：`PARAMETER_CONVERGENCE_V0_1.md` §15 Gate C 当前是**语义反例**攻击。建议增补**形式攻击**：为同一份 Court fact 构造 2–3 个同样"通过"语义门的转移律，检查它们是否给出**方向相反**的读数。若是，则 Gate C 的通过**不足以**支持该 construct 进入 Minimal Sufficient State。

### Gate 5 — Verification / artefact protocol
照抄 Galán et al. (2009) 的活动清单，改写为 LHRM 版：
- 同一模型用**两种时间语义**（固定步长 vs next-event / 连续时间）各跑一遍（Lawson & Park 的教训）；
- 改变 **coordinate 更新顺序**；
- 改变 **`Unknown` 填充策略**（不更新 / 衰减 / 区间化 / posterior）——这是 LHRM 特有的 accessory assumption 候选；
- 改变 **belief 与 reality 的采样独立性假设**；
- 用第二种实现（不同语言 / 平台）重实现，比对；
- 跑极端情形（单 agent、零 interaction、完全 Unknown）。

### Gate 6 — Ergodicity / stationarity 前置检验
在宣称 `Γ_(A,B)` 可解释之前，先做平稳性/遍历性检验（Grazzini 2012）。**非遍历 ⇒ 单次轨迹叙事无意义。**

### Gate 7 — 方向性必须被**证明存在**，而不是被建模假定
LHRM §4 要求 `i→j` 与 `j->i` 独立。因此任何 LHRM 模型必须能演示：**存在真实案例，其中两个方向给出实质不同的读数，且该差异不是模型假设的产物。**
反例警报：C-AttachmentDyads 用 `mean(f(A), f(B))`——形式上"一个输出"，实际上是**把方向性折叠掉了**。这在 LHRM 里是**硬失败**，不是简化。

---

## 10. 诚实裁决：ABM 是 LHRM 问题的正确工具吗？

### 10.1 对**第一阶段目标**（表示完备性 + Case Bank 逐句映射）：**不是。**

`CURRENT_ARCHITECTURE.md` §1 / §12 把第一阶段目标定为：
> 建立一套结构化、方向化、时间索引、保留 Unknown 与不确定性的**数学状态表示语言**；`Representation before scalarization. State-space before score.`

这是一个**表示 / 语义**问题，不是一个**动力学**问题。理由：

1. **ABM 对表示完备性零贡献。** Case Bank 测的是"这句话能否合法落到某个层"（§13 的 10 类落点 + `MAPPING_FAILURE` 记录）。ABM 不会让某个 sentence 多一个合法落点，也不会少一个。
2. **ABM 在此阶段主动增加风险面**：equifinality（C7/C8）、accessory assumption 支配（C10）、同步伪影（C11）、非遍历未检验（C12）、自指形式化（C15）。在一个还没有转移律的阶段引入模拟，等于**先建好了一整套可以骗自己的设施**。
3. **本 lane 未找到任何已发表的、用真实二人关系纵向数据校准的关系状态转移模型**（§12）。**没有 data 就没有 ABM 的正当性，只有 metaphor。**

### 10.2 对**转移律 / 动力学层**（第 5 步以后）：**有条件地是，但必须先过 §9 的七道门。**

若满足 Gate 1–7 全部通过，则 ABM 在 LHRM 中的正当角色是：
- **机制探针**（在已校准的转移律上做 counterfactual 与扰动实验）——但注意 Windrum et al. 引 Cowan & Foray (2002) 的警告："using (evolutionary) AB models to address **counterfactual-like questions may be misleading**"，因为系统随机、非遍历、且结构演化。
- **模型鉴别器**（Conroy-Beam 协议）——这才是 ABM 在 LHRM 中**最站得住脚**的角色。
- **表示的压力测试**：用模拟轨迹去撞 schema，看是否出现 `MAPPING_FAILURE` 级的不可表示状态。这**可能是 ABM 对 LHRM 唯一真正独特的价值**——它能生成 Case Bank 里还没有但可能出现的结构。

### 10.3 一句话裁决

> **对 LHRM 声明的问题，ABM 目前主要是一个隐喻生成器。**
> 它在"把一段关于关系的散文变成可运行的代码"这一步很有生产力；但那一步恰恰是 Windrum et al. 说的 "auto-referential formalisation"，也是 Lustick 说的 "nearly complete artifactuality"。
> **它什么时候不再是隐喻生成器：当你手里有一个 Gate 1 级的 dyad 级纵向校准数据集，并且愿意让 Conroy-Beam 协议在 held-out 真实 couple 上否掉你的模型的时候。**
> 在那之前，正确的用法是：**把它当作发现 ontology hole 的机器，而不是发现机制的机器。**

> **R12 Round-3 定位诚实性补记（2026-09-28）—— 结论方向不变，但停止低配自己的正面证据**
>
> **不撤回本裁决的方向。** 「当前第一阶段目标下 ABM 主要产出隐喻」这个判断**继续成立**，它由第 1、3 条 `VERIFIED` 证据支撑。
>
> **但本报告此前把它写得比自己的证据更负面，三处需修正**：
>
> 1. **「ABM 不是正确工具」这一措辞本身要收窄，尽管限定词已经就位。** 复核确认：§10.1 标题、§0 第 6 条、§11 非主张 3 **三处都带了「第一阶段目标」这个限定词**（本报告的限定纪律是好的，此处不撤销）。**问题出在主语**：这些句子把判断挂在「ABM 是什么」上（「不是**正确**的工具」），而不是挂在「ABM 对**哪个目标**产出什么」上。**限定词管不住主语。** 合规的改法是把主语也换成目标化表述。
> 2. **依赖图部分对本项目有利，本报告此前把它算在否定面。** §4.2 第 2 条的依赖图结论（`VERIFIED`，方向与本报告所述**相反**）应当被计入**正面**证据，而不是被当作又一条"ABM 有问题"。**方向更正**：它说明的是「ABM 输出缺少被当作随机过程再做统计推断的习惯」——这对**依赖 ABM 输出做二次推断**的项目是风险，但对**不复用 ABM 输出、只借其工程纪律**的项目**几乎无损失**。LHRM 属于后者。
> 3. **C1/C2/C6 三条失败模式对本项目有利，本报告把它们写成了负债。** `C1`（hand-tuned 参数被表述为发现）、`C2`（在模拟数据上做验证）、`C6`（没有 out-of-sample test）**全部是 LHRM 尚未犯的错误**（`§11` 非主张 5：本报告明确写「LHRM 当前还没有写任何转移律」）。**一份还没建转移律的项目，引用一份关于「别在模拟数据上做验证」的目录，是在给自己上保险，不是在给自己记过。** 这三条**保留在 §7 目录中**（作为 Gate 5 的直接输入），但**在证据盘点中应计为对本项目有利的方向性确认**。
>
> **修正后的定位（以此为准）**：
> - **A. 阶段限定**：ABM 对**表示完备性 / Case Bank 逐句映射**这一第一阶段目标**不产出价值**，且**主动增加**伪影面（`C7`/`C8`/`C10`/`C11`/`C12`/`C15`）。**这条成立。**
> - **B. 纪律可借**：ABM 文献对本项目最有价值的产出**不是模型，是失败目录**（`C1`–`C15`）与 artefact 检出协议（Galán et al. 2009）。**这三项 C1/C2/C6 与依赖图结论都指向同一件事：这个领域自己已经把「怎么骗自己」写清楚了，LHRM 可以直接抄这份清单。**
> - **C. 转移律层有条件可用**（§10.2 不变），且 Conroy-Beam 协议仍是 LHRM 若要谈转移律时**唯一有先例的现成协议**。
> - **不主张**：ABM 对 LHRM 是「正确工具」，也不主张它「不是正确工具」——**在第一阶段它不相关，在转移律层它有条件可用。** 这两句话必须一起说。

### 10.4 给 LHRM 的具体建议（`AI_RECOMMENDATION`，非 `Human_requirement`）

1. **不要**在 `docs/foundation/` 里引入 ABM 依赖。任何 ABM 依赖应留在 `docs/research/` 与未来的实验分支。
2. **现在值得做的 ABM 相关工作只有三件**，都不需要 ABM 框架：
   - 把 `Candidate Minimal Directed Basis v0.1` 的 8 个 construct 映射到 SRM 的 actor/partner/relationship 三分量（I10）——**但必须先解决 round-robin 识别问题**，否则做不了；
   - 把 Galán et al. 的 artefact 活动清单改写成 LHRM 的 verification protocol 文档（Gate 5）；
   - 把 Conroy-Beam 协议改写成"一般 Human Dyad 版"的实验设计（Gate 3）。
3. **把 C11/C12/C13/C15 写进 future work 的 guardrail**，因为它们对 R06（transition laws）和 R09（hysteresis）两条 lane 是直接的输入风险。
4. **不要**把 LLM agent（Concordia / GenAgents / AgentSociety）接入 LHRM 第一阶段。若未来要做，只允许它跑 Belief 层（I8）。

---

## 11. 明确不主张（Explicit non-claims）

1. 不主张 Mesa / Repast / MATSim / Concordia / AgentSociety / Agents.jl 中任何一个在**关系建模**上比 LHRM 强或弱。本报告对它们的评价**只关于工程成熟度与可复用性**。
2. 不主张 Hills & Todd / Knittel et al. / Zinn 的模型是"错的"。它们在**自己声明的目标**上可用，并已避免本文批评的许多事。批评只针对**不能挪用到 LHRM 的对象**。
3. 不主张 ABM 在任何意义上"不能"用于 LHRM。只主张：**当前第一阶段目标下它不产生价值**；且**在缺少 calibration data 时它主动增加**伪影与 equifinality 风险面。
4. 不主张 LHRM 的 8 个 candidate construct 已被 ABM 文献支持或证伪。
5. 不主张本文任何失败模式在 LHRM 中**已经**发生。全部是**风险**。LHRM 当前还没有写任何转移律。
6. 不主张文献数量、模型数量或 LLM 一致度构成任何支持。
7. **不主张** `JuSpace` / `smallslm` / `ASON` / `SoS` 已被证明"不存在"——只主张**本次在指定渠道内未能核实**（`NEGATIVE`，非 `DISPROVEN`）。负检索的价值有上限。
8. **不引用** `Timms & Griffiths (2007)` 与 `Kuran & Miller (2000)`——本次未能核实存在或著录。
9. 不主张 Generative Agents / Concordia / SOTOPIA 已被或未被验证；问题不是"错"，而是其 validation 目标（believability / 任务表现）与 LHRM 目标（表示完备性）**不同构**。
10. 不主张 LHRM 应当采用 SAOM 的数学（F2 给出结构性排除判据）。
11. 不主张 MATSim 式 replanning 是 LHRM 转移律的正确形式。`MODEL_HYPOTHESIS`。
12. **本 lane 未覆盖二人方法学的 `APIM` 分支**（Barry 等）。这是本报告**已知的最大缺口**。
13. 不修改、不评价 LHRM 任何 canonical 文档的内容正确性。本报告只与其对齐。

---

## 12. 剩余未知

| 项 | 状态 | 备注 |
|---|---|---|
| **是否存在用真实纵向二人关系数据校准的关系状态转移模型** | **本 lane 最重要未知** | **在本次检索场所内未找到；本报告无资格判定「不存在」或「极少」。** **必须由 R04（dataset landscape）与 R16（validation protocol）交叉确认。若 R04 找到此类模型，本报告 §10 裁决需修正。** |
| `APIM`（Barry 等）分支 | 未检索 | 本报告最大缺口 |
| `Timms & Griffiths (2007)` | `UNVERIFIED_AS_OF_2026-09-27` | 4 路检索 0 命中。**这是检索结果，不是「不存在」** |
| `Kuran & Miller (2000)` | `UNVERIFIED_AS_OF_2026-09-27` | Crossref / JASSS / DDG 均 0 命中。同上 |
| `Guizzetti (2011) Is the modelbuilder schizophrenic?` | `AGENT_RECALL` | 未核实 |
| `ten Brooke et al. (2016)` 敏感性分析选择 | `AGENT_RECALL` | 未核实 |
| `SOTOPIA` 的 ground-truth 设计 | `UNKNOWN` | 仅核实存在性 |
| `Centola (2010) Science` 的模型比较细节 | `UNKNOWN` | 仅核实题名/DOI/卷页 |
| `Grimm et al. (2005) Science` pattern-oriented 具体做法 | `UNKNOWN` | 仅确认著录 |
| `Edmonds & Moss (2005)` / `Brock (1999)` 确切出处 | `UNKNOWN` | 仅经 Windrum et al. 转述 |
| NetLogo / MASON / SoS 当前维护状态 | `UNKNOWN_AS_OF` | 仅二手指纹 |
| `Angus & Hassani-Mahmooei (2015)` 的完整著录 | `UNKNOWN` | 仅经 Grazzini & Richiardi 转述；**其"100+ 篇 JASSS ABM 中只有极少做 TS 统计建模"是本报告最有力的元证据之一，建议单独核实原文** |

---

## 13. 建议 status

**`SUCCESS`**（带一条 `PARTIAL` 级 caveat：本 lane 未检索 `APIM` 分支，且"是否存在真实二人关系校准模型"这一关键问题未获肯定答案）。

**给 parent 的行动建议：**
1. **把 §10.3 的一句话裁决**作为 synthesis 的一个独立小节保留。它是本 lane 最难被后续 lane 推翻的结论。
2. **交叉检查项**：R04 必须回答"有没有真实纵向二人关系 directed 状态数据"。若没有，§9 的 Gate 1 就应当被写进 LHRM 的 roadmap 作为**数据获取任务**，而不是建模任务。
3. **风险提示给 R06 / R09**：C11（同步伪影）与 C12（遍历性）在"无数据也能做"的领域里，恰恰是产出**看起来很像科学发现**的机制。请在设计 transition-law family 时就把 Gate 5/6 作为必答项。
4. **待补 lane**：建议追加一个短 lane 专门做 `APIM` + 二人动态回归（cross-lagged / dynamic panel / latent transition for dyads）+ `Kenny & Kashy (2015)` 多人层。这是本 lane 唯一明确的检索缺口。
5. **待补核实**：`Angus & Hassani-Mahmooei (2015)` 的原文与完整著录（C7 之外的 C1/C2/C6 都依赖这条元证据）。

---

## 附录 A：引用列表

**方法论 / 失败目录**
- Windrum, P., Fagiolo, G., & Moneta, A. (2007). Empirical Validation of Agent-Based Models: Alternatives and Prospects. *JASSS* 10(2)8. <https://www.jasss.org/10/2/8.html>
- Galán, J. M., Izquierdo, L. R., Izquierdo, S. S., Santos, J. I., del Olmo, R., López-Paredes, A., & Edmonds, B. (2009). Errors and Artefacts in Agent-Based Modelling. *JASSS* 12(1)1. <https://www.jasss.org/12/1/1.html>
- Schindler, J. (2013). About the Uncertainties in Model Design and Their Effects: An Illustration with a Land-Use Model. *JASSS* 16(4)6. DOI `10.18564/jasss.2274`. <https://www.jasss.org/16/4/6.html>
- Grazzini, J. (2012). Analysis of the Emergent Properties: Stationarity and Ergodicity. *JASSS* 15(2)7. DOI `10.18564/jasss.1929`
- Grazzini, J., & Richiardi, M. (2015). The Complexities of Agent-Based Modeling Output Analysis. *JASSS* 18(4)4. <https://www.jasss.org/18/4/4.html>
- Lustick, I. S. (2000). Agent-based modelling of collective identity: testing constructivist theory. *JASSS* 3(1)1. <https://www.jasss.org/3/1/1.html>
- Lawson, B. G., & Park, S. (2000). Asynchronous Time Evolution in an Artificial Society Model. *JASSS* 3(1)2. <https://www.jasss.org/3/1/2.html>
- Grimm, V., Revilla, E., Berger, U., Jeltsch, F., Mooij, W. M., Railsback, S. F., et al. (2005). Pattern-oriented modeling of agent-based complex systems: Lessons from ecology. *Science* 310(5750):987–991. DOI `10.1126/science.1116681`（`CITED_SECONDARY`）
- Centola, D. (2010). The Spread of Behavior in an Online Social Network Experiment. *Science* 329(5996):1194–1197. DOI `10.1126/science.1185231`
- **Edmonds, C., & Moss, S. (2005).** — **转述于 Windrum et al. 2007 §4.3；确切著录 `UNKNOWN`** — **Round-3 姓名更正**：本条目原作 **`Edwards, C., & Moss, S.`**，姓氏**误作 `Edwards`**。**更正为 `Edmonds`**，理由是本报告正文三处（§4.3、§7 `C15`、§12）**一致使用 `Edmonds & Moss 2005`**，且 Round-2 复核以 `Edmonds` 为正字。**本文件此前在正文与附录之间存在姓氏不一致，本轮统一为 `Edmonds`。** 姓名更正**不等于该文已被定位**：确切出处仍标 `UNKNOWN`（本轮 `NOT_OPENED`，未核实原文）
- Brock, W. A. (1999). — **转述于 Windrum et al. 2007 §5.2；确切著录 `UNKNOWN`**

**已发表的 named 关系 / 二人 ABM 与 microsimulation**
- Hills, T., & Todd, P. M. (2008). Population Heterogeneity and Individual Differences in an Assortative Agent-Based Marriage and Divorce Model (MADAM) Using Search with Relaxing Expectations. *JASSS* 11(4)5. <https://www.jasss.org/11/4/5.html>
- Knittel, K. K., Riolo, R. L., & Snow, C. R. (2011). Development and evaluation of an agent-based model of sexual partnership. *Adaptive Behavior*. <https://pmc.ncbi.nlm.nih.gov/articles/PMC7083591/>
- Conroy-Beam, D. (2021). Couple Simulation: A Novel Approach for Evaluating Models of Human Mate Choice. *Personality and Social Psychology Review*. <https://par.nsf.gov/biblio/10223261-couple-simulation-novel-approach-evaluating-models-human-mate-choice>
- Sutcliffe, A. G., Wang, D., & Dunbar, R. I. M. (2015). Modelling the role of trust in social relationships. *ACM TOIT* 15(4):16. DOI `10.1145/2815620`
- Sutcliffe, A. G., & Wang, D. (2012). Computational Modelling of Trust and Social Relationships. *JASSS* 15(1). DOI `10.18564/jasss.1912`（`CITED_SECONDARY`）
- Wang, D., & Sutcliffe, A. G. (2014). Social trust model (v1.0.0). CoMSES codebase 4458. <https://www.comses.net/codebases/4458/releases/1.0.0/>
- Zinn, S. (2015). Demographic microsimulation for individuals and couples (v1.0.0). CoMSES codebase 4490. <https://www.comses.net/codebases/4490/releases/1.0.0/>
- Darling, N., & Burns, I. R. D. Computational models for understanding sampling issues in studies of dyadic relationships. GitHub `NancyDarling/sampling-models`（`CITED_SECONDARY`；`LOW`）
- Darling, N., Burns, I. R. D., & Grubb, C. (2016-03). A Dynamic Systems Simulation of the Patterning of Attachment Dyads. Conference presentation（`CITED_SECONDARY`；`LOW`）

**统计学二人 / 关系模型**
- Kenny, D. A., & La Voie, L. (1984). The Social Relations Model. *Advances in Experimental Social Psychology* 18:141–182. DOI `10.1016/S0065-2601(08)60144-6`
- Malloy, T. E., & Kenny, D. A. (1986). The Social Relations Model: An integrative method for personality research. *Journal of Personality* 54(1):199–225. DOI `10.1111/j.1467-6494.1986.tb00393.x`
- Back, M. D., & Kenny, D. A. (2010). The Social Relations Model: How to understand dyadic processes. *Social and Personality Psychology Compass* 4:855–870
- Snijders, T. A. B., van de Bunt, G. G., & Steglich, C. E. G. (2010). Introduction to stochastic actor-based models for network dynamics. *Social Networks* 32(1):44–60. DOI `10.1016/j.socnet.2009.02.004`
- Snijders, T. A. B. (2017). Stochastic Actor-Oriented Models for Network Dynamics. *Annual Review of Statistics and Its Application* 4:343–363. DOI `10.1146/annurev-statistics-060116-054035`（`CITED_SECONDARY`）
- RSiena CRAN: <https://cran.r-project.org/web/packages/RSiena/>；SIENA manual: <https://www.stats.ox.ac.uk/~snijders/siena/RSiena_Manual.pdf>
- Kenny, D. A., & Kashy, D. A. (2015). Dyadic Data Analysis Using Multilevel Modeling. In *Handbook of Multilevel Models*, ch.17. DOI `10.4324/9780203848852.ch17`（`CITED_SECONDARY`）

**框架与基础设施**
- Mesa: <https://github.com/mesa/mesa>；ter Hoeven et al. (2025) *JOSS* 10(107):7668. DOI `10.21105/joss.07668`
- Repast Suite: <https://repast.github.io/>；<https://github.com/Repast/repast.simphony>；<https://github.com/Repast/repast4py>；<https://github.com/Repast/repast.hpc>
- MATSim: <https://matsim.org/>；<https://matsim.org/docs/>
- CoMSES: <https://www.comses.net/>
- Concordia: <https://github.com/google-deepmind/concordia>；Vezhnevets et al. (2023) arXiv:2312.03664
- Generative Agents: arXiv:2304.03442；DOI `10.1145/3586183.3606763`；<https://github.com/joonspk-research/generative_agents>
- AgentSociety: <https://github.com/tsinghua-fib-lab/agentsociety>
- JuliaDynamics/Agents.jl: <https://github.com/JuliaDynamics/Agents.jl>
- SOTOPIA-π: ACL 2024, pp.12912–12940. DOI `10.18653/v1/2024.acl-long.698`；SOTOPIA-: ACL 2025, pp.24669–24697. DOI `10.18653/v1/2025.acl-long.1203`

**否证 / 名字冲突**
- Dukart, J., … Lotter, L., et al. (2021). JuSpace: A tool for spatial correlation analyses of magnetic resonance imaging data with nuclear imaging derived neurotransmitter maps. *Human Brain Mapping*. DOI `10.1002/hbm.25244`；代码 <https://github.com/juryxy/JuSpace>；官网 <https://www.fz-juelich.de/en/inm/inm-7/resources/tools/juspace>
- `smallslm`：GitHub Search API `q=smallslm&in:name` → 0（2026-09-27）；arXiv / Crossref / DuckDuckGo 均 0
- `ASON`：GitHub Search API 两种查询均 0（2026-09-27）；DuckDuckGo 0

---

## 14. Round-3 修复轮记录（2026-09-28；child `A3f`）

**权威**：Architect `ARCHITECT_ADJUDICATION_V1`（`#30` comment `5854920569`）· dispatch `5854930069`。
**范围**：本文件**只做研究与定位的修复**，**不含任何 canonical 编辑**。

### 14.1 逐 hunk 裁决映射

| # | 位置 | 变更 | 依据 |
|---|---|---|---|
| 1 | §0 第 1 条（headline） | **「不存在」→ 检索范围命题；撤回「孤立」** | `X-14` + §C 第 6 条 `Search failure/access restriction is not ontology evidence` |
| 2 | §1 末句 + 新增检索范围声明 | 「本 lane 未找到」补上采样框架边界 | `X-14` |
| 3 | §3.1 `C-SAOM` 状态表示 | 保留「严格二值」并标 `VERIFIED`；**加注同页存在例外条款** | `R-G3` / `G-C16` |
| 4 | §3.1 `C-SAOM` 转移规则 | 「三函数不可共线」降级为 **`PLAUSIBLE`（未定位到出处）** | `R-G3` / `G-C16` |
| 5 | §3.1 `C-SAOM` 收尾 | **撤回「二值化直接违反 LHRM 混合态表示」**；保留「对象前提互斥」为唯一排除判据 | `R-G3` / `G-C16` `WRONG-SCOPE` |
| 6 | §4.2 标题 + 新增分级总表 | 「三条硬证据」→ 分级；`2a` `PLAUSIBLE`/`NOT_OPENED`、`2b` `VERIFIED` 且方向相反 | `R-G12` / `G-C27` |
| 7 | §8 `I2` | 「SAOM 已证明共线」降级；补一个不依赖 SAOM 的理由 | 随 #4 连带 |
| 8 | §10.3 | **定位诚实性升级**：主语目标化；依赖图与 `C1`/`C2`/`C6` 方向更正为**对本项目有利** | `R-G4` / `G-C18` `HOLD_FOR_EVIDENCE` |
| 9 | §12 第 1 行 + 两行工具名 | 「倾向不存在 / 极少」→ 检索范围表述 | `X-14` |
| 10 | 附录 A | **`Edwards` → `Edmonds`**（与正文三处统一） | `R-G13` / `G-C24(b)` |
| 11 | §2.3 / §11 非主张 7 | **未改动**（见 14.3） | — |

### 14.2 本轮独立核实（只核实**实际改动**的 claim）

| 主张 | 结果 |
|---|---|
| `Edmonds` vs `Edwards` 哪一个是本文件正文所用 | **正文三处（§4.3、§7 `C15`、§12）全部为 `Edmonds`**；附录为 `Edwards`。**内部不一致成立**，已统一为 `Edmonds`。**本轮未核实该文确切出处**（`NOT_OPENED`），故仍标 `UNKNOWN` |
| `JuSpace` / `smallslm` / `ASON` 三个名字的否证 | **未重跑**。`X-14` 提醒「检索失败 ≠ 不存在」，但 Round-2 判定为 `VERIFIED`，且本报告已用 `NEGATIVE` 而非 `DISPROVEN` 分级、§11 非主张 7 已写明「只主张本次在指定渠道内未能核实」。**分级与限定均已到位，保留原文** |
| `Angus & Hassani-Mahmooei (2015)` | **`NOT_OPENED`**（按裁决要求不追）。标 `PLAUSIBLE` |
| Grazzini & Richiardi (2015) 依赖图部分 | **`NOT_OPENED`**。按 Round-2 复核记录为 `VERIFIED` + 方向相反，并标注来源 |
| SAOM 同页例外句 | **`NOT_OPENED`**。只记录「存在例外条款」这一事实，不复述其内容 |

### 14.3 本轮**未**做的事（`deliberately_not_applied`）

1. **未重跑 `JuSpace` / `smallslm` / `ASON` 的四路检索。** 它们的 `NEGATIVE` 分级与「非 `DISPROVEN`」限定已合规；重跑会把一个已裁决的 `VERIFIED` 项变成新的检索活动，无收益。
2. **未打开 `RSiena manual` / `Snijders et al. 2010` 正文。** 撤回一条推论不需要新来源。
3. **未打开 `Angus & Hassani-Mahmooei (2015)`、`Grazzini & Richiardi (2015)` 原文。** 按裁决要求分级标注即可。
4. **未改 §7 `C1`–`C15` 失败目录的任何一条。** 方向性更正只改**证据盘点与 §10 定位**，不改目录本体。
5. **未改 §9 Gate 1–7。** 不在本轮裁决范围。
6. **未动 `CF-xx` 与 `UNKNOWN_AS_OF` 的全局计数。** 这两项的账本属于 `18`（见 14.4）。本文件内的 `UNKNOWN_AS_OF` 出现次数**本轮刻意未重算**。

### 14.4 路由（交回 parent / 其它 child）

| 项 | 路由对象 | 内容 |
|---|---|---|
| `CF-xx` 代码空间 | **parent → `18` 的 owner** | 本轮全目录检索确认 `CF-[0-9]` **只出现在 `18_CROSS_LANE_CONFLICT_AUDIT.md`**（47 处），**不**出现在本文件。代码空间归属 `18`，本 child 未动 |
| `UNKNOWN_AS_OF` 全局计数 | **parent → `18` 的 owner** | 该码在 11 个文件出现（含本文件 2 处）。**跨文件计数与账本属于 `18`**，本 child 只在文件内保持自洽，不出全局数 |
| §4.2 依赖图结论的原文定位 | **parent（可选后续 lane）** | 若要把 §4.2 第 2 条从「复核判定」升为「本报告自核实」，需打开 `Grazzini & Richiardi (2015) *JASSS* 18(4)4` 与 `Angus & Hassani-Mahmooei (2015)` 原文。**本轮按裁决不做** |
| SAOM 三函数共线的出处 | **parent（可选后续 lane）** | 同上，`C-SAOM` 转移规则的 `PLAUSIBLE` 需原文才能升 `VERIFIED` |