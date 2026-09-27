
# 13 — LLM Skill / 自适应访谈层：语义接口研究

- **性质**：research candidate。未修改任何 canonical 文档；未提出 ontology 变更；无实现设计。
- **研究对象**：以下管线的**语义接口层**。

```text
human natural language
 -> observation / proxy extraction
 -> canonical candidate evidence
 -> adaptive question
 -> uncertainty-aware result
```

- **立场声明**：本报告对 LLM 层采取**对抗性**评估。理由不是 LLM 抽取效果差（§2.1 里 F1 0.88–0.98 是真实结果），而是 §9.6 的一条元论证：**"多个 LLM 达成一致"本身就是 LLM 层的失败模式之一，而不是它的解药**。
- **引用强度约定**：`CITED_PRIMARY`（读到原文/官方页）/ `CITED_SECONDARY`（仅经转述）/ `AGENT_RECALL`（先验，未核实）。核实日期 2026-09-27。

---

## 1. 这条管线真正的失效面在哪

LHRM 的表示优先约束（`AGENTS.md`）已经把第一阶段定为：

```text
Raw evidence -> loss-aware / uncertainty-preserving canonical representation -> relationship state trajectory
```

并且要求**逐句测试**（`AGENTS.md` 验证纪律段；`CURRENT_ARCHITECTURE.md` §10）：

```text
sentence / event -> valid LHRM mapping ?
映射失败必须记录，不先加特例参数。
```

所以 LLM Skill 层在项目里承担的是一个**非常窄但非常难**的职责：

1. 把自由文本切成句/事件单元；
2. 为每个单元定位源 span（`FIXTURE_001` 的 `source_paragraph(s)`、`FIXTURE_002` 的 `PG7256/body/pNN`、`FIXTURE_003` 的 `SC/transcript/pNN` 已经是这个约定的三个实例）；
3. 提出候选映射，或显式产出 `MAPPING_FAILURE`；
4. **不发明 construct**。

第 4 点正是张力所在：LLM 天生擅长的是给出"看起来干净"的答案，而 §10 要求的恰恰是"保留不干净"。§9 的失败分类学全部围绕这一张力展开。

---

## 2. 结构化抽取的可靠性：现有证据说了什么

### 2.1 支持性证据（真实且相当强）

| 研究 | 设置 | 关键数字 |
|---|---|---|
| Gilardi, Alizadeh & Kubli 2023, *PNAS* 120(30):e2305016120 | 4 数据集 n=6,183 推文/新闻，5 个分类任务 | zero-shot 准确率平均比 MTurk 高约 25pp；intercoder agreement 全面高于 crowd 与 trained annotator；单条 <$0.003，约 30× 便宜 |
| Gu et al. 2025, *JAMIA* 32(10):1570（SBDH-Reader） | GPT-4o 从临床笔记抽 SDoH | 独立验证集"任一 adverse 属性"F1 **0.97** / recall 0.97 / precision 0.98；6 类 macro-F1 0.94–0.98 |
| Wang et al. 2025, medRxiv `10.1101/2025.11.15.25339520` | 规则 vs 7 个 GPT 模型，SDoH | 规则 P 0.97 / R 0.62；GPT-5(5-mini) few-shot domain F1 **0.88**；RBS+GPT 集成 F1 0.89 |
| *npj Digital Medicine* 2025, `s41746-025-01645-8` | 跨机构 SDoH | instruction-tuned LLM level-1 micro-F1 **>0.9**，level-2（带取值）>0.84 |

**结论 1**：在"**封闭取值集 + 明确类别定义 + 抽取对象是明确实体/属性**"的任务上，LLM 抽取已达到可部署质量。

### 2.2 反对性证据（对本项目更相关）

**(a) schema 宽度是硬墙。** *ExtractBench*（arXiv:2602.12247）用 35 文档 / 5 schema / 2,076 页 / 12,867 个可评字段（67.9 小时专家工时）测前沿模型：性能随 schema 变宽急剧退化，在 **369 字段的财报 schema 上所有模型 0% 有效输出**；退化主要由**输出体量**预测，而非输入长度或嵌套深度。

> 对 LHRM：`Z[k, i, j, t]`（构念族 × 方向 × pair × 时间）× `Reality / Observation / Belief` 分层，本身就是一个宽 schema。**ExtractBench 的结论直接适用于本项目，而且它是一个警告而不是许可。**

**(b) 人类的 gold 天花板比想象的低。** Fu et al. 2024（LREC-COLING, pp. 7045–7056, *PedSHAC*）：1,260 份儿科临床笔记、10 类 SDoH **事件-论元**级标注，**人类标注者一致度只有 81.9 F1**；微调 LLM 事件论元 78.4 F1，GPT-4 in-context 事件触发 82.3 F1。

> 也就是说，在"事件 + 谁 + 什么 + 何时 + 何状态"这种正是 LHRM 需要的粒度上，**人类专家自己的一致度是 ~0.82**。任何把 LHRM 抽取结果与该类 gold 比 F1 的做法，都是把 0.82 当成 1.0。

**(c) LLM 的一致性是"对齐多数派先验"，不是"更准"。** Nakamura, Tan & Yean 2026（arXiv:2609.22133v1）复现 14 项同行评审政治学研究的二元文本分类，用 **10 个 LLM、3 位专家、165 名众包工**标注同一批文本（每研究抽 100 条）：

| 任务组 | expert–expert 一致度 | LLM–expert 一致度 |
|---|---|---|
| 易（9 项研究，expert ICR > 0.8） | 0.89 | 0.89–0.91（多数票 0.92） |
| 难（5 项研究，expert ICR ≤ 0.8） | **0.67** | 0.69–0.76 |

各研究专家 ICR 从 0.987（负面竞选）到 **0.533**（议会情绪化修辞）。三个关键发现：

1. 当两个专家在某文本上分歧时，留出的那位专家**也**更可能与 LLM 分歧；不同 LLM 之间也更容易分歧。→ 分歧源是**文本与规则的歧义**，不是某一类标注者的错误。
2. **澄清 codebook 同时降低专家间与（足够强的）LLM 间的分歧。**
3. crowd 工人表现出同样的集中模式，但与专家的一致度显著更低。

> **对 LHRM 的直接后果**：把"LLM 一致度高"当质量证据，等于说"LLM 和人群**平均/多数**读法一致"。这在专家自己都分裂的文本上恰恰是误导。§9.6 会把这写成一条硬规则。

**(d) 迁移与分组差异显著。** SBDH-Reader 从内部验证的 0.97 掉到 MIMIC-G 0.92 / MIMIC-A 0.89（employment 降到 0.83）。SODA（GatorTron，*J Biomed Inform* 2024, PMC11141428）端到端 strict mF1 0.8963，但**种族分组差距 >15pp**：White 组 F1 0.9038/0.9160 vs Other 组 0.7465/0.7960。

**(e) 罕见 / 训练中缺席的构念会失灵。** Nakamura et al. 引 Halterman & Keith 2026：现成 LLM 在真实政治学 codebook 上会挣扎，尤其是训练中罕见或缺席的构念；他们特意加入 *Arias (2022)* 的 `climate securitization` 作为理论难例。

> **结论 2**：证据支持"LLM 在封闭明确定义的抽取上接近或超过廉价众包标注"；**证据不支持**"LLM 能在 LHRM 需要的开放式、多坐标、方向化、带时间与 belief 分层的抽取上可靠"。LHRM 的构念候选（共同情绪调节、关系叙事 coherence、felt security、boundary vs 控制…）在中文与英文语料中都属于 §2.2(e) 的低频类别。

**(f) 一个被低估的发现：prompt 策略比模型大小更重要。** LLMStructBench（arXiv:2602.14743，995 个人工校验样本 / 22 模型 / 5 种 prompting）结论是"choosing the right prompting strategy is more important than standard attributes such as model size"；同时**结构强制解码提升 JSON 合法率但增加语义错误**。SchemaRAG（ACL 2026 Industry 78）显示大 schema 全量入 prompt 触发 lost-in-the-middle，动态裁剪 +8.8% micro-F1 / 延迟 −47%。PARSE（EMNLP 2025 Industry 184）则指出 **JSON schema 本身就是"自然语言理解契约"**，schema 含歧义或欠定义时会出现频繁 hallucination。

> **推论**：如果"schema 质量"是主要杠杆，那么 **LHRM 的 schema 质量（构念族定义 + 显式 exclusion rule）比选哪个模型重要得多**。这与 `AGENTS.md` 的"few stable constructs + composition"一致，但理由是纯工程的。

**(g) prompt 敏感性是已被直接观测到的失败模式。** Lho et al. 2025（*JAMA Network Open*, PMC12102709）在 1,064 名韩语精神科患者的 52,627 份半结构化叙述上发现：**同一位患者在 self-concept 叙述下被判为临床显著抑郁，在 gender-perception 叙述下未被判出**；另有两位两次漏检。→ 对 LHRM：**同一段叙事在不同抽取 prompt 下可以产出不同构念读出**，且这不是噪声。

---

## 3. 歧义处理：应该发生什么

### 3.1 现有立场的方向

- Krippendorff 2018（经 Nakamura et al. 转述 p.24）：文本没有 reader-independent 的品质；其意义不是被包含在词里，而是被读者带进去。因此两位细心的编码者可以在同一段上读出不同结果——**不是因为谁犯了错，而是因为这段话确实容许不止一种解读**。
- Nakamura et al. 明确的极端表述：**"when the codebook admits multiple defensible classifications or texts do not provide sufficient information or contexts, a unique target annotation may not exist at all."**
- Zhang et al. 2025（ICML, PMLR 267:76193–76212）：人类偏好标注分歧的 taxonomy（4 大类 10 小类），**多数分歧源于任务欠定义或回答风格**；这"challenges a standard assumption in reward modeling methods that annotator disagreements can be attributed to simple noise"。
- Ivey, Gauch & Jurgens 2025（EMNLP 2025 main 144, pp. 2874–2887, *NUTMEG*）：贝叶斯模型可**同时**降噪与保留系统性分歧，下游模型显著优于传统聚合。
- arXiv:2506.19467：多数分歧由歧义、语境敏感等**系统性**原因造成，而非粗心；并主张评估 LLM 标注器应对齐**分布**而非多数标签；同时发现 RLVR 式 reasoning **降低**分歧预测能力。
- arXiv:2601.09065（综述）：persona 变量只解释很小一部分方差；LLM 判断"压缩"人类分歧并依赖不透明先验。

### 3.2 那"应该发生什么"

不是打一个 `ambiguous` 标签，而是：

```text
AMBIGUOUS_NO_UNIQUE_ANSWER   # 在当前 codebook 下无唯一解；须给分支集合
UNKNOWN_EVIDENCE             # 证据本身缺失；不给分支也不做归一
DISPUTED_BY_SOURCE           # 来源自身标记为争议（alleged / disputed / adjudicated）
```

这三个状态**互不等价**。LHRM 现有 fixture 已在事实上区分它们（`FIXTURE_001` 的 `fact_status ∈ {adjudicated, alleged, disputed, unknown}`、`C013` 与 `C025` 明确保留 unknown 与跨记录不一致），**但抽取层的 schema 里还没有对应的一等状态**。这是一个具体的、可落地的 research candidate 缺口。

### 3.3 三条反直觉的操作性结论

1. **Codebook 清晰度是最强杠杆，但"让模型自由列解读"是反模式。** CoMeDi 2025 shared task（ACL 2025.comedi-1）在 130,000+ 标注上发现：**自由选择策略产生更不多样的标注，往往向常见标签收敛**。即"请列出所有可能解读"会制造伪多样性并稀释真分歧。
2. **ICC 阈值不可当真值。** Artstein & Poesio 2008（*CL* 34(4):555–596）指出 Di Eugenio & Glass 的经典观察：个体边际 vs 池化边际两种 chance correction 可使结果**落在被广泛引用的 0.67 阈值两侧**；且现有文献对 annotator bias 的平均化处理"do not provide a mathematical justification"。`AGENTS.md` 说"不把 LLM 一致度当 validation"是对的，但"报了 κ = 0.71"同样不是 validation。
3. **可靠性与效度的 trade-off 无法消除。** 把构念操作化为机械规则（高可靠、低效度）vs 交给整体判断（高效度、低可靠）是同一根轴的两端。这直接约束 LHRM：不要试图通过"把构念写得更机械"来同时提高抽取稳定性与构念保真度。

---

## 4. 矛盾检测：与"变化"的区分

### 4.1 三条必须引用的负向结果

**(a) LLM 消解矛盾的主流策略是"发明未说出的语境"。** arXiv:2603.22735 复用 NLI 数据集构造"生成消解矛盾的解释"任务，18 个 LLM 中**绝大多数只能有限成功**；其定性分析给出的典型策略是 *"considering potentially relevant but unstated contexts"*，并给出 gpt-5.2 的实例：把"商人不卖火把和火"与"小贩卖火把"之间的矛盾，解释成"入夜后火把是照明配件而非商品"。

> **在 LHRM 语境下，这就是 belief laundering。** 典型形态：`FIXTURE_001` 中 C024（2021-05-25 对方称"已于 2020-09 接手、已于 2020 年书面解雇"）与 C016（"似乎未寄出进一步解雇信"）、C013（"是否真的被出售或只是换了管理层，法庭记录认为不清楚"）并存。**LLM 面对这三条时最自然的操作，是补一个"中间也许补发过文件"的解释把矛盾洗掉。** 而 `C025` 已明确要求"Keep contradiction/uncertainty visible for evidence-lineage testing"。

**(b) 矛盾判定必须条件于被问的问题。** Canby et al. 2025（ACL 2025 Findings 765, *QC-NLI*）：传统文档 NLI 只要假设的一部分不一致就标 contradiction；query-conditioned 形式让**同一对文档可以得到多个标签**。该基准上**没有任何方法超过 83%**。

**(c) "时变事实"的可判定性本身不稳定。** arXiv:2603.15892 对 DYNAMICQA 与 MULAN 做统一复现，发现两篇对"时变事实是否比静态事实更易被外部上下文更新"给出**相反结论**。归因于 temporality 的操作化差异：DYNAMICQA 用 Wikipedia 编辑次数近似，**未记录质量核查也未列出进入 temporal 类的具体事实版本**；MULAN 用 Wikidata 关系类型与对象计数。

> **对 LHRM 的直接后果**：任何"矛盾 vs 状态变化"的判定规则，如果**不显式声明其时间对齐假设**，就不构成可复现的判定。`FIXTURE_003` freeze rule 2 已经做出了正确区分（`recording_time != recalled_event_time != event_time`），这是 LHRM 相对文献的真实领先点。

### 4.2 结论：矛盾不是二值

```text
CONSISTENT
CONTRADICTORY_AT_SAME_TIME_SLICE      # 需给出被对齐到的时间切片
UNRESOLVED_PENDING_TIME_ALIGNMENT     # 时间轴未对齐前，不得报 contradiction
```

在 `FIXTURE_001` 这种材料里，**第三类应该是常态而不是例外**。

另有一条相关限制：*TimeBench*（ACL 2024 long 66）显示最强 LLM 与人类在时间推理上仍有 **19.4%** 差距，且**日期格式本身显著影响表现**（"YYYY, Mon DD" 57% vs 斜杠样式更低）。LHRM 的 `event_time` 解析在混合格式语料上不应被信任。

---

## 5. 自适应提问 / 信息增益：理论基础与代价

### 5.1 理论基础（扎实）

| 来源 | 机制 |
|---|---|
| Lewenberg et al. 2017, *AAAI* 31(1)（`10.1609/aaai.v31i1.10730`） | 贝叶斯主动学习的 surveying 问题；下一问依赖前答；对缺失数据比增强线性回归更稳健 |
| Zhang, Taylor, Cobb & Sekhon, *Ann. Appl. Stat.* 14(3)（`10.1214/20-AOAS1322`） | 少问 + 概率矩阵分解插补；方差最小化准则选每受访者最有信息的问题；**Facebook 选民调查的顺序效应偏倚可能很小** |
| Bassamboo, Deep, Juneja & Zeevi 2020（arXiv:2004.05442） | δ-正确框架下的下界：渐近地任一候选**最多在 2 个（能力特定）难度层级**被提问；问题结构使**内生探索**成立，无需独立 exploration 阶段 |
| ADAPQUEST（arXiv:2112.14476） | BN 自适应问卷：选 `q` 最大化 `H(S|e) − H(S|Q,e)`；当 `H(S|e) < H*` 时停止；可在线报告选择下一题 / 停止 / 评级的数值依据（可解释性） |

这套理论完全可以形式化为 LHRM 的问题选择器。**但注意：以上全部处理的是"从固定题库里选下一题"，其 latent 变量是能力/态度维度，不是"关系状态"。**

### 5.2 代价（被严重低估，且 LHRM 的版本更严重）

**(a) 负担会系统性改变被测量的值。** Jeong, Aggarwal, Robinson, Kumar, Spearot & Park（NBER WP 30439 / *J Dev Econ* 2023，`10.3386/w30439`）随机化 2–3 小时入户调查的问题顺序：

> 多 1 小时调查时间使受访者**跳答概率上升 10–64%**；多 1 小时使**食品支出金额下降 25%**。在受访者已熟悉问题的电话调查中效应量相近，提示**认知负担是 survey fatigue 的关键驱动**。

这不是噪声。这是与"问题在问卷中的位置"系统相关的测量偏差。

**(b) 测量反应性与准确性衰减是可观察的。** Reynolds, Robles & Repetti 2016（*Developmental Psychology* 52(3):442–456），56 天日记、47 母亲 / 39 父亲 / 47 儿童：逐日报告的**亲子冲突与温暖随天数轻微下降**（作者解释为 measurement reactivity）；同时**母亲与儿童对冲突的报告一致度下降**（作者解释为 fatigue 相关准确性下降）。

**(c) 少问 + 插补是一个显式的设计权衡。** Zhang et al. 明确把它表述为"短而不完整的调查"与"长、昂贵、造成负担的调查"之间的选择。

### 5.3 LHRM 特有的、比一般问卷更严重的一层

标记为 `model hypothesis`（需 Human 裁定，不由本研究确立）：

> 一般问卷测量的是"**关于**某主题的一个人类信念或事实"。LHRM 测量的是"**两个人之间的关系状态本身**"。因此自适应追问不是对"受访者记忆的扰动"，而是**对被观测系统的干预**。

三重后果：

1. **反应性升级为本体论问题**。被问"他有没有在控制你"这个问题本身，可能改变接下来可观测到的控制行为（S38 已在家庭日记场景中观察到同类效应）。关系叙事访谈是这个效应的**最高风险场景**而非最低。
2. **访谈记录是状态的共同生产者，不是窗口**。`FIXTURE_002` freeze rule 2/3 与 `FIXTURE_003` freeze rule 2/3/7 已在做这件事（`said != believed != true`；`narrator_evaluation` 不升级为客观 latent state；`happily married / shelter / never another Annie` 不量化）。本报告只是把它推到"**提问动作本身也要入 provenance**"这一步。
3. **顺序与揭示效应在此处没有证据**。Zhang et al. 报告顺序效应在选民态度题上"可能很小"，但**那不是关系题**。涉及忠诚、控制、嫉妒、依赖的问题带有强社会赞许与需求特征；该领域**无对应证据**（U-6）。

**结论 3**：信息增益最大化在 LHRM 中是**有理论依据但默认关闭**的优化目标。开启需 Human 显式裁定，且提问预算、提问内容、提问顺序必须作为**观测事件**进入 provenance（见 R15）。

---

## 6. 多语言 proxy 归一化

### 6.1 跨语言模型在**英语内部**就已经不一致

- Wang et al. 2024（EACL 2024 177 / arXiv:2402.02099）：mBERT 与 XLM-r 在跨语言 NLI 与复述识别上，**即使在英语与德语这种同语族之间平均下降约 17%**；斯瓦希里语等低资源语言更严重。核心结论：*"what is transferred across languages is mostly data artifacts and biases, especially for low-resource languages"*。
- *Cross-Lingual Pitfalls*（ACL 2025 404）：6,000+ 双语对 / 16 语言；**多数模型英语近 100% 而目标语言平均掉 >50%**；Claude-3.5-sonnet 在多数语言掉 >20%。
- arXiv:2603.21036：英语 90.7% vs 哈萨克语 76.9%（−13.8pp）、蒙古语 74.0%（−16.7pp）；**表面流畅但内容准确度显著更低**。
- *MuBench*（arXiv:2506.19468，61 语言）：英语与低资源语言的差距**不随模型规模一致收窄**，只在某基准上英语接近饱和时才开始缩小。
- 反例必须并列：arXiv:2506.20793 报告 Aya-expanse-32B 在**高资源语言静态基准**上的语言差距仅 5.89%，但在**功能基准 CL-IFEval 上同样语言间差距达 23.47%**。→ **"这个模型多语言好"不能从静态基准外推到功能任务。**

### 6.2 一个无告警的硬失败

arXiv:2603.21036 记录了一个对本项目极其重要的失败模式：**一个专建的多语模型在被问哈萨克语问题时输出了吉尔吉斯语**。该研究的评分规则是"语言识别错误则 Fluency = 0，无论内容质量"。

> **对 LHRM 的直接后果**：用英语 schema 处理中文关系叙事时，完全可能出现**语言层无告警、构念层已错位**的情况。这类错误不会表现为崩溃，而会表现为"看起来合理的中文 proxy 标注"。它无法被事后审计发现，除非显式做语言与语域检查（R17）。

### 6.3 心理测量侧：部分不变性才是常态

- Davidov, Muthen & Schmidt 2018（*Cross-Cultural Research*，`10.1177/0049124118789708`）：跨国 MI 的要求"very hard to meet"；**标量不变性往往不成立，部分标量不变性也很少达成**；若连**部分 metric 不变性**都没有，回归系数比较就被阻断；失败可能说明"个体对题目反应不同，因而以有意义的方式比较潜因子均值是不可能的"。
- SPANE 跨 13 国（N=12,635）不变性研究（CDC Stacks）：configural 与 **partial** scalar 支持；3 个测量具体负性情绪的题项（sad / afraid / **angry**）跨国不不变。
- 中文 I-PANAS-SF（*Health Qual Life Outcomes* 2020, `10.1186/s12955-020-01526-6`）：ESEM 中一题（"alert"）cross-loading 0.55 > primary loading 0.22，删除后 9 题模型更优；与 Karim 等在法巴大学生中的部分因子不变性发现一致，**挑战了 Thompson 的原假设，说明需要语言特定的译本**。
- 中德跨文化污名量表（PMC6554279 / *Frontiers in Psychology* `10.3389/fpsyg.2019.01249`）：SSRPH 与 IASMHS 得到部分标量不变性，但 **SSOSH 的因子结构出现文化变异**（完整标量模型 CFI 0.777 / RMSEA 0.180 / SRMR 0.148）。
- Lacko et al. 2022（*Cross-Cultural Research*，`10.1177/10693971211068971`）：目前主流的 individualism–collectivism 量表"算术均值比较法"可产生有偏结果，潜均值比较（invariant）才更少偏。
- 另一侧也非完美：Gerlitz & Schupp 的 BFI-S 3 题分量表 alpha 仅 .50–.66；**CATI 条件下两题残差方差为负导致非正定协方差矩阵**。

### 6.4 一条必须并列的反例

Bergkvist & Rossiter 2007（*J. Marketing Research* 44(2):175, `10.1509/jmkr.44.2.175`）：对"由具体、单一对象与具体属性构成"的构念，**单题与多题的预测效度无差异**。

> **所以不能一刀切。** 脆弱的是**复合、抽象、文化负载**的构念——依恋、理想化、"贤惠"、"共同未来感"、关系质量——而这恰好是 LHRM 最关心的那一批（对照 `RESEARCH_REPORT_REAL_WORLD_PROXY_DECOMPOSITION` 的 W05 / W09 / W59 / W64 / W73 / W76）。

### 6.5 结论 4

默认策略必须是**逐 construct family 记录 alignment 状态**：

```text
INVARIANCE_EVIDENCED   |  有该族在该语言对上的不变性证据
PARTIAL_ONLY           |  仅有部分不变性证据；跨语言比较只在不变题项上有意义
UNTESTED               |  无证据（当前 126 条 proxy 的默认状态）
```

并对 `UNTESTED` 的族**禁止**跨语言直接归一化。同时必须接受：**LHRM 目前的 126 条 proxy 字典没有任何一条有跨语言不变性证据**（U-1）。

---

## 7. Provenance：最小可行记录

### 7.1 标准基线：W3C PROV

PROV Working Group 于 **2013-04-30** 发布 12 份文档，其中四项为 W3C Recommendation：**PROV-DM、PROV-O、PROV-N、PROV-CONSTRAINTS**（primer: `https://www.w3.org/TR/prov-primer`）。

| 构件 | LHRM 对应 |
|---|---|
| `Entity` / `Activity` / `Agent` | 证据项 / 抽取活动 / Human 委托者 + LLM |
| `used` | 抽取活动使用了源 span |
| `wasGeneratedBy` | 证据项由该抽取活动生成 |
| `wasDerivedFrom` | 三档精度：`precise-1` / `imprecise-1` / `imprecise-n`（`prov:steps="n"`） |
| `wasAssociatedWith` | LLM 对抽取活动负责 |
| `actedOnBehalfOf` | Human 委托 LLM 的委托链 |
| `specializationOf` / `alternateOf` | `AGENTS.md` §8–10 的 history 分叉、Belief 内嵌世界、purpose-specific views |
| `revision` / `quotation` | "只存 paraphrase + 锚点、不镜像全文"（Fixture 001/002/003 全部如此） |

PROV-AGENT（arXiv:2508.02866）表明把 PROV 扩展到 agentic workflow 溯源（含 MCP 可观测性）是一条活跃的工程路径。

### 7.2 最小可行记录（research candidate，不是设计）

```text
evidence_item:
  item_id
  source_anchor            # 必填：file / block / paragraph / char-range 级
  slot_anchors{}           # 必填：逐 slot 的锚，不是一条记录一个锚
  derivation_precision     # precise-1 | imprecise-1 | imprecise-n（+ steps）
  agent_chain[]            # 谁委托了谁（Human -> LLM -> 子调用）
  epistemic_status         # OBSERVED | REPORTED | BELIEVED | NARRATED | UNKNOWN
  knowledge_time_by_agent  # knowledge-time，与 event_time 分离
  event_time / interval
  fact_status              # adjudicated | admitted | alleged | disputed | unknown
  residual_ambiguity       # 重复抽取下的分布宽度（不设阈值）
  human_verified           # bool + 谁 + 何时
```

### 7.3 三个 PROV 没覆盖、需要 LHRM 自行裁定的点

1. **slot 级而非记录级溯源**。PROV 的 `used` 绑定在 activity/entity 上；LHRM 需要"时间指代可信、动机不可信"这种**字段级可信度差异**。这不是 PROV 的缺陷，但 PROV 也不直接提供。
2. **knowledge-time vs event-time**。`FIXTURE_001` 的 `knowledge_time_by_agent` 与 `FIXTURE_003` 的三分**比 PROV 更细**——PROV 只有 activity 的 start/end。**这可能是 LHRM 的原创贡献点，但它属于扩展还是实现细节，属 Architect / Human 裁定，不由本研究决定。**
3. **诚实标注 derivation 步数**。LLM 抽取通常经过 CoT、多步，标 `precise-1` 是撒谎；应标 `imprecise-n` 并给 `steps`。

---

## 8. LLM 自信 vs 证据

### 8.1 负向证据（密集且一致）

| 研究 | 结论 |
|---|---|
| DiNCo（arXiv:2509.25532） | 言语化 confidence 常态性 overconfidence，且存在 **confidence saturation**（分数集中于少数 bin，"jumpy" 曲线，无阈值可用）；模型对**信息量低**的主张更 **suggestible**，且这一倾向在**回答错误时更严重** |
| *Wired for Overconfidence*（arXiv:2604.01457, COLM 2026） | 驱动言语化过度自信的是一个**紧凑的、对正确性不敏感的**"confidence-writing core"；answer-substitution 对照显示该电路对已提交答案的响应**基本独立于该答案是否正确** |
| *Dunning-Kruger Effect in LLMs*（arXiv:2603.09985） | ECE 从 0.122 到 0.726；最差组合 97.9% 信心 / 3.9% 准确（preprint，弱证据） |
| Sanz-Guerrero et al. 2026（ACL 2026 Findings 1570） | 事后训练 LLM 的 logit 校准差；模型对"作为 assistant 自己给出的答案"表现出过度自信 |
| *DepressLLM*（arXiv:2508.08591） | **即使模型有 PHQ-9 token 的校准概率分布**，基于自报 confidence 的性能仍随阈值升高而退化 |
| Xiong et al. 2024（NAACL 2024 long 366） | confidence elicitation 方法综述：各类方法失效模式各异 |

> **最强的一条**：*Wired for Overconfidence* 的 answer-substitution 对照说明，**"我有多确定"与"我对不对"在模型内部是近似解耦的**。因此把自报 confidence 当权重，等于把一个与正确性近似无关的量接入下游。

### 8.2 judge 层有独立的系统性偏差

- Zheng et al. 2023（NeurIPS 2023, arXiv:2306.05685）：GPT-4 judge 与人类偏好 >80% 一致（"与人类之间的一致水平相同"）；但**明确列出 position / verbosity / self-enhancement 偏差**与推理能力不足；更重要的是——**人类认为 GPT-4 的判断合理 75%，且在 34% 的情况下愿意改变自己的选择**。
- Panickssery, Bowman & He 2024（arXiv:2410.21819）与 *Play Favorites*（arXiv:2508.06709，>5,000 人类标注 + 9 judge）：**GPT-4o、Claude 3.5 Sonnet 系统性地给自己的输出打更高分**。
- arXiv:2604.23178：去偏策略系统评估显示 **style bias 的幅度显著大于** position bias（≤0.04）与 verbosity bias，且跨 Google / Anthropic / Meta 一致；verbosity bias 按模型异质（GPT-4o 中性，Claude 偏好更短）→ **不能用一个统一的去偏操作解决所有偏差**。

### 8.3 结论 5：应该信什么

```text
DO   span_support           每个 slot 有源 span（机器可判）
DO   external_corroboration 独立第三方 / 法条 / 记录（FIXTURE_001 的 adjudicated）
DO   human_verified         有人读过并确认
DO   codebook_version       映射规则本身的版本与明确 exclusion
DO   residual_ambiguity     重复抽取的分布宽度（作为"可争议性"的记录，不作为精度）

DON'T  model_reported_confidence
DON'T  llm_ensemble_agreement_as_quality
DON'T  single_llm_selfconsistency_at_temperature_0
```

最后一个反模式特别值得强调：`temperature = 0` 下"结果稳定"几乎只说明解码是确定的，**不说明判断正确**。Ziems et al. 2024 为可复现性采用 temperature 0 + 跨 prompt 扰动平均（*CL* 50(1):237–291），但那是**在有 gold 的基准上**；在没有 gold 的 LHRM 抽取层，稳定性不可被解释为可靠性。相关地，arXiv:2503.10671 报告 sampling temperature 导致的低方差会**使效应量估计有偏**。

---

## 9. 幻觉潜状态：失败分类学

以下 10 类是本报告的核心交付。每类给出：机制、文献锚、探测信号，以及**基于项目现有冻结 fixture 的 bad / 合规对照**。

> **这些对照是"研究候选示例"，不是已经执行过的 mapping 结果。** `AGENTS.md` 与三个 fixture 包都明确禁止在材料准备阶段做映射。

### 9.1 F1 — 单实例 → 稳定倾向（single instance → disposition）

- **机制**：把一次观测当作该主体的稳定属性。
- **文献**：单题信度只有对应多题同伴的 **37%–78%**（EMA 研究，PMC10248304）；一致性式单题信度随参照量表题数增加而**下降**（PMC4332286）；Argyle et al. 2023（*Political Analysis* 31(3):337–351）的 "silicon samples" 方法论就是"用条件化历史生成**稳定的**亚群体画像"，其**成功**恰恰说明模型有能力做这件事——因此**能力存在即是风险**。
- **Fixture 对照**（`FIXTURE_002`，source `PG7256/body/p028`）：

| | 内容 |
|---|---|
| Bad | `Jim = 消极 / 低投入 / 现实压力大 / 家庭负担重`（依据：22 岁、瘦、神情严肃、缺外套与手套、工资从 30 降到 20 美元） |
| 合规 | `narrator_description, 22岁, 瘦, 神情严肃, 缺外套与手套` + `habitual_wage_change: 30→20 USD/wk` + 显式 `NOT_A_DISPOSITION` 标记；把"burdened with a family"标为 `narrator_framing`（`M038` 已有口径） |

- **探测信号**：抽取项的 `epistemic_status` 不是 `OBSERVED`，但没有对应的 belief / speech holder。

### 9.2 F2 — 单行为 → 稳定状态（single behaviour → stable disposition）

- **机制**：F1 的行为版本。这正是项目自己的反例库攻击的方向：`RESEARCH_REPORT_REAL_WORLD_PROXY_DECOMPOSITION` 对"肯花钱"（W79）的四关审查结论是"降级为 `observable_proxy`"；对"陪伴"（W33/W34/W35）的结论是"拆为 responsiveness + availability + co-presence，不平级"。
- **Fixture 对照**（`FIXTURE_003`，`SC/transcript/p004`–`p011`）：

| | 内容 |
|---|---|
| Bad | `Caregiving(Danny→Annie) = 高`（依据：每日晨间便条） |
| 合规 | `ritual / observed: 每日晨间桌上留便条` + `speaker: AP`（"若晨间桌上无便条则会担心"）+ 叙述层 `narrator_evaluation: "shelter" / "color television"` 不折算 |

- **探测信号**：一个 0..1 或 ordinal 读出，其 `support_set` 只有 1 个事件。

### 9.3 F3 — 跨语言构念等同

- **机制**：把英语的构念定义直接当作中文 / 其他语言的构念定义。
- **文献**：§6 全部。特别是 en–de 内部 17% 下降（Wang et al. 2024, EACL 177）、功能基准语言差距可达 23.47%（arXiv:2506.20793）、专建多语模型输错语种（arXiv:2603.21036）。
- **对照**：

| | 内容 |
|---|---|
| Bad | 英文叙事 "he's emotionally unavailable" → `EmotionalAvailability = 低`（在中文 schema 下直接赋 latent 值） |
| 合规 | 记录为 `proxy_phrase: "emotionally unavailable"` + `construct_alignment: UNTESTED` + `source_lang` / `target_schema_lang`；在无不变性证据时禁止折算 |

- **探测信号**：`source_lang != schema_lang` 且 `construct_alignment == UNTESTED` 却给出了数值。

### 9.4 F4 — 文化刻板输入

- **机制**：用文化先验补全未说明的属性。
- **文献**：Cheng et al. 2024（ICLR 2024，4 模型 / 19 persona / 24 数据集）：Disabled 与 Religious persona 平均比 "Human" 基线**差 35%+**，某些组合差 69%；**prompt 级缓解（"别做刻板假设"）无效或不实用**。Li, Li & Qiu 2025（*JLCL* 38(2):125–138）：persona 模型对韩国人群的 MSE 0.859 vs 美国 0.808，**所有组合都差**；**模型规模 7B–176B 与对齐度无一致相关**。Lutz et al. 2025（EMNLP 2025 Findings 1261）：看似微小的 prompt 差异显著改变描绘与刻板化，**对边缘群体尤其**。Tan et al. 2026（ACL 2026 1127）：LLM 对齐的是**单一、西方中心**的价值集。arXiv:2406.12934：合成社会数据存在 **structural consistency 失败**。Weeber et al. 2026（ACL 2026 2079）：依赖单一 persona cue 的结论外部效度低。
- **对照**：

| | 内容 |
|---|---|
| Bad | 中文叙事中"丈夫管钱、妻子不工作" → `Agent.controlling / patriarchal = 高` |
| 合规 | `Environment.role_norm: 该叙事中出现的家庭分工规范` + `Agent.ResourceControl: 收入控制权（谁持有）` + `Agent.Attitude: UNKNOWN` + `construct note: 不得由规范推断态度` |

- **探测信号**：latent 坐标的 `support_set` 里出现的是**规范陈述**而非行为或自述。

### 9.5 F5 — 歧义选边（resolving ambiguity by plausibility）

- **机制**：面对真正歧义的文本，选那个"更合理 / 更连贯"的解释。
- **文献**：Nakamura et al. 明确 "unique target annotation may not exist"；判官偏差 S63–S66。
- **Fixture 对照**（`FIXTURE_001` C013 / C025）：

| | 内容 |
|---|---|
| Bad | `PairState.business_ownership_change = "sold" (2020-08-02)`，并据此把 C014 的 "contract terminated" 归入"因出售而终止" |
| 合规 | `C013: fact_status = unknown`，两个候选（真的被出售 / 只是换了管理层）**并存**；C025 的跨记录不一致**保持可见**；C014 与 C024 的终止叙述保持为 attributed claims，不覆盖 C013 / C016 |

- **探测信号**：`fact_status = unknown` 的来源单元在下游被赋了确定值。

### 9.6 F6 — 歧义选边 + 共识幻觉（**本报告最强的一条元论证**）

- **机制**：LLM 在模糊输入上**自发收敛到同一个似真解释**。多个模型一致不是因为对，而是因为共享训练分布与"选取最连贯叙述"的归纳偏置。
- **文献**：
  - arXiv:2602.13224（*A Geometric Taxonomy of Hallucination in LLMs*）：多数幻觉 benchmark 的假内容是"**被指示编造**"的，因此携带生成模式痕迹；HaluEval 的正确/幻觉回答在嵌入空间中距离 cos 0.10–0.78，而**人类 confabulation 是 0.72–0.92**、LLM confabulation 0.86–0.96；检测 AUROC **域内 0.76–0.99 但跨域 0.50（随机）**，判别方向跨域近正交（平均余弦 −0.07）。→ **自发产生的虚假内容与真实内容在可检测性上不可区分。**
  - Nakamura et al.：LLM–expert 一致度与 expert–expert 同档；LLM 对齐的是人群平均 / 多数读法。
  - S63–S66：judge 层有 self-preference、style、position、verbosity 偏差，且人类会被系统性说服（34% 改变选择）。
- **推论**：

> **"多个 LLM 达成一致"是 F5/F6 的实例，不是它的解药。LLM 一致只能作为歧义定位信号，不能作为质量证据。**

- **这直接反驳一条常见的 LHRM 内部诱惑**："让三个模型各跑一遍取交集 / 投票，这样就更可靠。" 在 §2.2(c) 的数据面前，这个做法的实际内容是"取多数派读法"，而在专家自己都分裂的文本上，多数派不等于正确。

### 9.7 F7 — 先验回洗（laundering a prior back as an observation）

- **机制**：prompt 里的类别名、先前摘要、标签，或用户自己的断言，被 LLM 展开成一串"特征"，然后被当作从文本**独立抽取**的观察。
- **文献**：arXiv:2603.22735（发明未说出的语境）；DiNCo（suggestibility——对低信息量主张更容易被说服，且**回答错误时更严重**）。
- **对照**：

| | 内容 |
|---|---|
| Bad | prompt 已含"她说自己被骗婚"，抽取层输出 `{欺骗: 高, 承诺: 低, 短期视角: 是, 信任: 低}`，全部标为 `extracted` |
| 合规 | 全部标 `prompt_derived_prior`；`extracted` 集合为空；唯一可抽取的是"她在 [时刻] 说了这句话"（`OBSERVED` 的 speech act），内容作为 `REPORTED` |

- **探测信号**：`source_anchor` 指向 prompt 本身而不是源材料；或 `support_set` 的所有项都能被一句 prompt 陈述解释。
- **这是一个 `AGENTS.md` 级别的纪律问题**：它把 `Model hypothesis` 静默升格为 `empirical evidence`，正是 `AGENTS.md` 禁止的那类混淆。

### 9.8 F8 — 结局倒灌（future / later-state leakage）

- **机制**：用后文或世界知识补全当前窗口。
- **项目现有基础**：`VALIDATION_CORPUS_V0_1.md` 逐条给出了 `future_leakage_risk`（L0-001 HIGH、L1-003 HIGH、L3-001 HIGH、L3-002 MEDIUM-HIGH、L3-003 HIGH），并对 L3-002/003 明确写 "model may assert ... without textual warrant if windowed; enforce blind forward windowing"。
- **对照**（`FIXTURE_002`）：

| | 内容 |
|---|---|
| Bad | 对 `PG7256/body/p029` 之前的单元填入"她已经知道他卖了表" |
| 合规 | `K(i)` 只含 `≤ i` 的信息；`M001`–`M033` 中 Jim 的 knowledge 不含表已被卖（`FIXTURE_002` freeze rule 4 已是正确口径） |

- **补充风险（文献侧）**：因为语料多是高知名度作品（`VALIDATION_CORPUS_V0_1.md` 自己标注 `future_leakage_risk` 多为 HIGH），LLM 的**预训练记忆**是一条与窗口无关的旁路。Gururangan et al. 2018（仅看 hypothesis 就能在 SNLI 上到 67%）是这一旁路的机制原型。

### 9.9 F9 — 说话 / 相信 / 为真 的合并

- **Fixture 对照**（`FIXTURE_001` C004）：

| | 内容 |
|---|---|
| Bad | `Carty 已被解雇 (adjudicated)` |
| 合规 | `经理于 2020-03-23 发出含该主张的短信（消息存在 = adjudicated）`；`该主张为真 = unknown`（`FIXTURE_001` §2 规则 1 与 C013 已如此） |

- **文献侧**：`FIXTURE_003` freeze rule 6 要求 `reported_speaker_ref` 用于嵌套引语（"Danny 引用 1978 的自己"）。这在文献里没有对等物，属于 LHRM 领先点。

### 9.10 F10 — 跨构念族重复计数（double counting）

| | 内容 |
|---|---|
| Bad | 一次"他每周给她买花"同时抬高 `Caregiving / Investment / Generosity / Spending` 四个坐标（这正是 W79 的四机制问题） |
| 合规 | 记为 1 个 `ActionEvent` + 4 个 **candidate readout**，并显式标注它们在语义上**非独立**（须留下 `RESEARCH_REPORT_REAL_WORLD_PROXY_DECOMPOSITION` §8 四关审查痕迹：语义独立 / 反例解耦 / 条件增量 / 干预独立） |

- **文献侧的对应机制**：Gururangan et al. 2018（premise-oblivious 分类 SNLI 67% / MultiNLI 53%）与 McCoy, Pavlick & Linzen 2019（词汇重叠 / 子序列 / 成分三种句法启发式）说明**抽取层与判定层之间存在系统性捷径**。在 LHRM 中，捷径的方向是"复合词 → 多个构念坐标"。

---

## 10. 硬规则（research candidate，非实现设计，非验证结论）

> 依据标注：`A` = 现有项目约束的延伸；`B` = 文献直接支撑；`C` = 纯研究推断（**未验证**）。
> **本节任何一条都未经过 LHRM 数据验证。**

| # | 规则 | 依据 |
|---|---|---|
| **R1** | 不得从单条证据升格为稳定倾向或状态。`support_set` size = 1 的项只能停留在 `OBSERVED`（事件 / 行为层），不得产生 Agent 级或 Dyad 级的 trait 读出 | B（单题信度 37–78%）；**例外**：具体、单一对象 + 具体属性的构念（Bergkvist & Rossiter 2007）→ 本规则是"默认禁止 + 需显式登记例外"，不是绝对禁止 |
| **R2** | `State != Action`（复用 `AGENTS.md` §6–7）。抽取层只产出 Action/Event 与 Observation；状态是下游演算结果 | A |
| **R3** | `said / believed / true` 三分不可合并；每个断言必须携带 holder；嵌套引语必须用 `reported_speaker_ref` | A（`FIXTURE_002`/`003` freeze rules 已有） |
| **R4** | `UNKNOWN` 不得被静默转成 neutral / 低 / 零 / 缺失即默认 | A（`AGENTS.md` 研究纪律段） |
| **R5** | 每条抽取项必须携带**逐 slot** 的源 span 指针；span 必须机器可验证存在。记录级锚不满足本规则 | B（W3C PROV 2013-04-30）+ C |
| **R6** | 歧义必须保留为**分支集合**。禁止在无显式裁定时选边。`AMBIGUOUS_NO_UNIQUE_ANSWER` 是一等状态，与 `UNKNOWN_EVIDENCE` 严格区分 | B（Nakamura et al.；Zhang et al. 2025；NUTMEG） |
| **R7** | 时间轴未对齐前禁止报 `contradiction`。矛盾三分类见 §4.2 | B（arXiv:2603.22735；arXiv:2603.15892；arXiv:2601.02627） |
| **R8** | 禁止跨语言构念等同。每条 proxy 必须带 `construct_alignment ∈ {INVARIANCE_EVIDENCED, PARTIAL_ONLY, UNTESTED}`；`UNTESTED` 禁止折算为跨语言可比读出 | B（§6 全部） |
| **R9** | 禁止把模型自报 confidence 写入证据记录并作为权重或证据等级 | B（DiNCo；*Wired for Overconfidence*；*DepressLLM*） |
| **R10** | 禁止把 prompt、先前摘要、标签、类别名、用户断言当作证据来源。受其影响的项必须标 `prompt_derived_prior` 且不计入 `extracted` | B（arXiv:2603.22735；DiNCo suggestibility）+ C |
| **R11** | 禁止把高层复合词（漂亮 / 贤惠 / 高价值 / 真爱 / 关系质量 / 匹配度 / 幸福）落成单一坐标 | A（`AGENTS.md`；Proxy Decomposition §3） |
| **R12** | 抽取过程中不得发明新 construct。`MAPPING_FAILURE` 必须记账并向上暴露，不得被"顺手修好" | A（`AGENTS.md` 验证纪律段） |
| **R13** | 强制 blind forward windowing：`K(t)` 只含 `≤ t` 的信息。语料的预训练记忆是窗口外的旁路，必须在评估中作为混淆变量显式声明 | A（`VALIDATION_CORPUS_V0_1.md` 的 `future_leakage_risk` 字段已建立该实践） |
| **R14** | 多项映射同一构念族读出时必须显式标注非独立，并留下四关审查痕迹 | A（Proxy Decomposition §8） |
| **R15** | 若启用自适应提问：提问预算必须有硬上限；**提问动作本身（内容、顺序、被问者、时刻）必须作为观测事件进入 provenance**；候选问题在未经 Human 复核前不得进入被访谈者 | B（Jeong et al. 2023；Reynolds et al. 2016）+ C（LHRM 特化的反应性论证，`model hypothesis`） |
| **R16** | LLM 之间的一致**不得**作为质量证据。它只能作为歧义定位信号，用于 codebook 迭代 | B（arXiv:2602.13224；Nakamura et al.；S63–S66） |
| **R17** | 以单一语言 schema 处理他语言原文时，必须做显式的语种 / 语域检查；语种错误**不产生告警**，必须主动检测 | B（arXiv:2603.21036 的"专建多语模型输错语种"案例） |

---

## 11. 最低风险设计：LLM 允许做什么 / 不允许做什么

### 11.1 允许（作为 **candidate generator**，不是 decision maker）

| 允许 | 为什么这是低风险 | 验证方式 |
|---|---|---|
| 在给定窗口内切分句/事件单元、标注说话人、识别**显式**时间锚 | 可被源文本完全或大部分校验 | `SPAN_SUPPORT_RATE` |
| 为每个单元**定位**源 span | 存在性可机器判定 | 同上 |
| 输出**候选类型标记**（允许多重）与显式 `NO_MAPPING_CANDIDATE` 选项 | 只是枚举，不做裁决 | `UNKNOWN_PRESERVATION_RATE` |
| 忠实 paraphrase 与引语复制 | 与 `FIXTURE_*` 现有口径一致 | span 覆盖检查 |
| **发现**冲突候选并列出涉及的 span 对 | 发现 ≠ 裁决；输出可以是"这两个单元若在同一时间切片上不可同真" | `FUTURE_LEAK_RATE` + 时间切片标注完整性 |
| 生成澄清问题的**候选**，附"该问题可能泄露什么 / 可能引发什么反应性 / 属于哪个 construct 家族"元数据 | 仍需 Human 复核（R15） | 人工复核日志 |
| 输出 `residual_ambiguity`（重复抽取的分布宽度） | 它是歧义度量，不是精度度量 | 分布可复现 |

### 11.2 不允许

| 禁止 | 触发的失败类 |
|---|---|
| 赋 latent 数值 / 区间 / 类别（含"大致""偏""中等""较强"这类软化措辞） | F1 F2 F4 F10 |
| 从单条证据升格为稳定倾向或状态 | F1 |
| 消解歧义或矛盾以使输出"干净" | F5 F6 |
| 跨语言构念等同 | F3 |
| 引入源文本中不存在的实体 / 时间 / 因果 / 动机 | F4 F7 F8 |
| 对 dyad 状态做总结、评分、排序、建议 | F10 + `AGENTS.md` §11 非目标 |
| 未经 Human 复核直接向被访谈者提问 | R15 |
| 用自报 confidence 或 LLM 间一致度调节下游权重 | R9 R16 |
| 在抽取过程中发明新 construct | R12 |

### 11.3 一句话总结

> **让 LLM 做"穷举 + 定位 + 标歧义"，不让 LLM 做"消歧 + 折叠 + 赋值"。**
> 前者的错误是可枚举、可机器检出、可回滚的；后者的错误是**不可见**的，因为它们恰好长得像一份干净的答案。

---

## 12. 每一阶段的证据基础，以及哪里基本是空的

| 阶段 | 证据强度 | 具体依据 | 缺口 |
|---|---|---|---|
| 句/事件切分 | **弱** | 事件抽取有成熟基准（S16 PedSHAC 事件-论元 F1 78–82） | **无针对叙事 / 口述史 / 文学文本的切分 benchmark**；无中文的 |
| schema-bound 结构化抽取（封闭取值） | **强** | F1 0.88–0.98（S14/S15/S18） | 域外：临床 / EHR，非关系叙事 |
| schema-bound 结构化抽取（宽 schema / 开放构念） | **弱–中** | ExtractBench 369 字段 0%（S09）；Halterman & Keith（S13） | **无针对 LHRM 式方向化多坐标抽取的 benchmark** |
| `Observation / Belief / Environment` 分层 | **基本为空** | 项目 fixture 有构造 | **0 条外部文献**。这是 LHRM 独有结构 |
| 说话/相信/真值三分 | **弱** | `FIXTURE_002/003` freeze rules | 无针对叙事主张分层的评测 |
| 歧义保留 | **中（方法论层）/ 空（实现层）** | Nakamura；Zhang 2025；NUTMEG；CoMeDi | 无"何时该保留为分支、何时该收敛"的判定规程 |
| 矛盾检测（同一切片内） | **中** | QC-NLI ≤83%（S29）；C³D（S26） | gold 部分由 LLM 生成（S26），存在循环风险 |
| **变化 vs 不一致的区分** | **基本为空** | 只有 S30 的 benchmark 间**结论反转**这一警示 | **无可复现判定规程**。§4.2 的三分类是本研究提出，**无文献背书** |
| 时间解析 | **弱–中** | TimeBench 19.4% gap（S31）；格式敏感 | 混合格式中文日期语料无研究 |
| 信息增益选问 | **强（理论）** | S33–S36 | latent 变量是"能力 / 态度"维度，**不是关系状态** |
| **提问的反应性代价** | **一般问卷：强；关系状态：空** | S37（10–64% / −25%）；S38（日记反应性） | **U-3：0 条研究测量"追问关系状态"对关系状态的改变量** |
| 跨语言 proxy 归一化 | **中（人类量表）/ 弱（LLM 抽取）** | S57–S61 | **U-1：LHRM 126 条 proxy 零条有不变性证据**；且无"LLM 抽取 + 人类因子结构"结合的先例 |
| Provenance 记录 | **强（标准）** | W3C PROV 2013-04-30 | slot 级 + knowledge-time 的具体形态需 Architect 裁定 |
| LLM confidence 的可用性 | **强（负向）** | S44–S48 | — |
| 反幻觉（自发 confabulation） | **强（负向）** | arXiv:2602.13224 | 现有 benchmark 不测这一类（自指问题） |
| **抽取质量的度量本身** | **基本为空** | Nakamura 的 ambiguity-aware bounds 是最接近的 | 见 §13 |

**统计**：本报告 70 条指针中，**直接**支撑"LLM 做人类关系语义抽取"的：**0 条**。全部为邻近领域外推。这必须被明确承认，而不是用"文献很多"掩盖。

---

## 13. 度量问题：没有 ground truth 怎么测

### 13.1 先承认这是根本困难

LHRM 的第一产物是 **latent dyad state**。它没有 ground truth，也**不应该**有。因此"抽取准确率"在 LHRM 语境下**没有定义**。

| 直觉目标 | 致命缺陷 |
|---|---|
| 与人工 gold 比 F1 / κ | gold 本身一致度只有 81.9 F1（S16 事件-论元级）；专家 ICR 可低至 0.533（S02）；"多对少"是聚合伪影（Artstein & Poesio 2008） |
| 与 LLM 的一致度 | **循环论证**；且已证明是失败模式的实例（§9.6） |
| 与真实关系状态的一致度 | **不可观测**（无 ground truth），且在伦理上不可获取 |

### 13.2 可行的替代：把目标从 *accuracy* 换成 **representation faithfulness**

在冻结 fixture 上，下列量**完全可机器判定**（因为 fixture 本身是冻结的、有明确 `fact_status` 与 `source_anchor`）：

| 指标 | 定义 | 目标 | 为什么可判定 |
|---|---|---|---|
| `SPAN_SUPPORT_RATE` | 每个抽取 slot 是否有源 span，且 span 真实包含该断言 | 1.0 | 源文本固定 |
| `ENTITY_INSERTION_RATE` | 抽取结果中的实体 / 日期 / 数值是否全部出现在源窗口 | 0 | 源窗口固定 |
| `UNKNOWN_PRESERVATION_RATE` | fixture 明标 `unknown / disputed / alleged / 谨慎措辞` 时，抽取层是否保留 | 1.0 | fixture 的 `fact_status` 是冻结事实 |
| `FUTURE_LEAK_RATE` | 是否引用了窗口外文本 | 0 | 窗口冻结（`FIXTURE_003` freeze rule 5） |
| `HOLDER_LEAK_RATE` | 断言是否被安到了错误的 holder / 错误的时间切片 | 0 | `knowledge_time_by_agent` 冻结 |
| `DISTINCTION_LEAK_RATE` | 高层评价（`narrator_evaluation` / `figurative_expression`）是否被升级为客观 latent state | 0 | `FIXTURE_002/003` 的 `fact_or_narrative_status` 冻结 |

这六个指标有一个共同性质：**它们测的不是"抽得准不准"，而是"有没有凭空引入 / 有没有把未知压实 / 有没有把叙述当事实"**。而这三件事恰恰是本报告找到的全部主要失效面。

### 13.3 统计量（明确不设阈值）

| 统计量 | 用途 | 明确不是 |
|---|---|---|
| `CROSS_RUN_DISPERSION` | 同一单元在重复抽取下的输出分布宽度。**只用于歧义定位与 codebook 迭代**（Nakamura et al. 的用法） | **不是精度。** 它测的是"该 item 在当前 codebook 下有多可争议" |
| `HUMAN_LLM_LEAVE_ONE_OUT` | 把 LLM 当作第四/五位"标注者"，与多位 Human 用**留一法**比较（参照 Nakamura et al. 的 hold-out expert 设计） | 不是"LLM vs 人类"的胜负；它只回答"分歧是否集中在同一批 item" |
| `MAPPING_FAILURE_PROFILE` | `PARTIAL / MULTI / UNKNOWN / MAPPING_FAILURE` 的**分布**（不是率） | 不是失败率 KPI。它是**表示完备性的诊断 profile**，与 `AGENTS.md` 的 Case Bank 纪律一致 |
| `DIVERGENCE_CONCENTRATION` | LLM 间分歧是否像人类间分歧一样**集中**在同一批 item（S02 H2 的直接检验） | 不是质量分。若分歧**不**集中，说明分歧是随机噪声而非语义歧义，那是**坏消息** |

### 13.4 三个必须接受的结论

1. **`MAPPING_FAILURE` 的分布 profile 才是 LHRM 该看的量**，不是任何单一准确率。这与 `AGENTS.md` 验证纪律段（测 completeness / closure / regression / adversarial coverage，**不测 population probability**）一致，不是新发明。
2. **`CROSS_RUN_DISPERSION` 不能被当成精度**，无论它多好看。
3. **任何单一数字（例如"抽取准确率 91%"）都应被视为误导性产物**：它的参照系要么是人（不可靠，S02/S16），要么是模型（循环，§9.6）。如果它出现，几乎肯定是有人把 `MAPPING_FAILURE` 记成了别的名字。

### 13.5 建议的最小可执行评估（research candidate）

```text
对每个冻结 fixture：
  1. 冻结 window（blind forward），声明窗口外旁路风险
  2. 三次独立抽取（不同采样），记录 13.2 的六个率 + 13.3 的两个分布
  3. 至少两位 Human 独立执行同一协议（消费同一 merged exact version）
  4. 计算 HUMAN_LLM_LEAVE_ONE_OUT 与 DIVERGENCE_CONCENTRATION
  5. 记录 MAPPING_FAILURE_PROFILE
  6. 对 UNKNOWN_PRESERVATION_RATE < 1.0 的每一处，生成一个 codebook 修订候选
     —— 依据 Nakamura et al. H3：澄清 codebook 是唯一被反复验证有效的杠杆
  7. **不产生任何"准确率"数字**
```

---

## 14. 明确不主张（explicit non-claims）

1. **不主张** LLM 抽取"不可靠"。§2.1 的 F1 0.88–0.98 是真实结果。本报告只主张它**不能外推**到 LHRM 的任务形态。
2. **不主张** 人类标注是 gold standard。Nakamura et al. 与 PedSHAC（81.9 F1）都直接反驳。
3. **不主张** 本报告的 70 条指针里"文献多"等于"证据强"。其中直接支撑本项目任务的为 **0 条**。
4. **不主张** LLM 一致度代表正确性。§9.6 是本报告最强的单条主张。
5. **不主张** §10 的 17 条硬规则经过验证。它们是 research candidate，其中 R1 / R15 / R17 明确标为 `C`（纯研究推断）。
6. **不主张** §13 的度量方案是充分的。它是**在现有条件下唯一诚实可做**的度量，不是好的度量。
7. **不主张** 信息增益在 LHRM 不可用。只主张其**代价目前无文献支撑**（U-3），因此默认关闭。
8. **不主张** 本报告需要修改任何 canonical 文档。`knowledge_time_by_agent` 是否升格为 LHRM 对 PROV 的扩展，是 **Architect / Human 的裁定**，不是研究结论。
9. **不主张** 西方量表（BFI / EPQ 等）的中文版可直接用作 LHRM proxy 的校准目标。§6.3 恰恰说明相反。
10. **不主张** `#20` / `#21` / `#22` 的 verifier 结果已被读取。因此 **U-5（fixture 上人工 verifier 的真实 ICR）是 open**。
11. **不主张** §12 表中标注为"强"的那些格，其证据可以跨域迁移到关系叙事。它们全部标明了原始域。

---

## 15. 剩余未知

| # | 未知 | 为什么重要 | 本次已尝试 |
|---|---|---|---|
| U-1 | LHRM 126 条 proxy 的**跨语言测量不变性** | §6.5 的默认分支直接决定能否跨语言归一化 | 检索 cross-lingual MI / 跨文化心理测量文献；**未找到任何 proxy-level 不变性研究** |
| U-2 | "叙事中 状态变化 vs 事实不一致" 的可复现判定规程 | §4.2 三分类目前**没有可实现的算法** | 检索 NLI / document inconsistency / temporal fact conflict 文献；全部无此切分；S30 甚至显示 benchmark 间结论反转 |
| U-3 | 追问关系状态对关系状态的**反应性量级** | 决定 R15 / 自适应层是否伦理可接受 | 只找到一般问卷负担（S37）与日记反应性（S38）；**0 条研究测量关系状态的自反应性** |
| U-4 | LHRM 目标语料（中文关系叙事 + 英文学术/文学）的**歧义密度分布** | 决定 codebook 迭代优先级与最小评估样本量 | 无 |
| U-5 | `FIXTURE_001/002/003` 上人工 verifier 之间的**真实 ICR** | 现有 fixture 报告的是材料结构，**未报告任何 ICR**；PedSHAC 表明事件-论元级人工一致度可能仅 ~0.82 F1 | contract 禁止读取 `#20/#21/#22`，**不知道 verifier 结果是否已存在** |
| U-6 | AI 辅助关系访谈中的 **social desirability / demand characteristics** 量级 | 关系访谈必然涉及忠诚 / 控制 / 嫉妒等社会赞许敏感项 | 未检索到直接文献；S40 只覆盖 survey fatigue |
| U-7 | Nakamura et al. 2026（arXiv:2609.22133v1）的**同行评审状态** | 该文是本报告最重的单一支柱 | 未核实。标 `CITED_PRIMARY_FULLTEXT`（已读全文大部分）+ `PEER_REVIEW_STATUS = UNKNOWN_AS_OF` |
| U-8 | 中文关系叙事上**专门训练过**的抽取模型 vs 通用前沿模型 | S15 显示通用 GPT-5 在临床域已达 domain F1 0.88；关系域未知 | 无 |
| U-9 | LHRM 的 `Observation / Belief / Environment` 分层在 LLM 抽取下的**错误率** | 项目独有结构 | **0 条外部文献** |
| U-10 | prompt 层的**先验回洗**（F7）能否被机器检测 | 它污染 prompt 层而非文本层，不在现有 benchmark 覆盖内 | DiNCo 的 suggestibility 是最接近的技术，可能可用；**未验证** |
| U-11 | "style bias 是最大 judge 偏差"（arXiv:2604.23178）是否也适用于**抽取**层 | 若成立，抽取层输出的措辞华丽程度会污染下游 | 邻近推断，未验证 |

---

## 16. 引用清单

### 结构化抽取 / LLM-as-annotator
- Gilardi, F., Alizadeh, M., & Kubli, M. (2023). ChatGPT outperforms crowd workers for text-annotation tasks. *PNAS* 120(30):e2305016120. DOI `10.1073/pnas.2305016120` · PMC10372638 · arXiv:2303.15056
- Nakamura, K., Tan, J. L., & Yean, G. (2026). Observational Equivalence of LLM and Human Annotation. arXiv:2609.22133v1（同行评审状态未知）
- Huo et al. (2024). Comparing LLM and human annotations of conversational safety. *EMNLP 2024*, main 511
- Zhang, M. J., et al. (2025). Diverging Preferences: When do Annotators Disagree and do Models Know? *ICML 2025*, PMLR 267:76193–76212
- Ivey, J., Gauch, S., & Jurgens, D. (2025). NUTMEG: Separating Signal From Noise in Annotator Disagreement. *EMNLP 2025*, main 144, pp. 2874–2887. DOI `10.18653/v1/2025.emnlp-main.144` · arXiv:2507.18890
- Can Large Language Models Capture Human Annotator Disagreements? arXiv:2506.19467
- Beyond Consensus: Perspectivist Modeling and Evaluation of Annotator Disagreement in NLP. arXiv:2601.09065
- Tenckhoff, S., Koddenbrock, M., & Rodner, E. (2026). LLMStructBench. arXiv:2602.14743
- ExtractBench: A Benchmark and Evaluation Methodology for Complex Structured Extraction. arXiv:2602.12247
- Shrimal, A., et al. (2025). PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction. *EMNLP 2025 Industry Track*, 184, pp. 2749–2763
- Ho, S. Y. B., et al. (2026). SchemaRAG: Dynamic Large Schema Reduction for LLM-driven Structured Information Extraction. *ACL 2026 Industry Track*, 78, pp. 1114–1127
- Ziems, C., et al. (2024). Can Large Language Models Transform Computational Social Science? *Computational Linguistics* 50(1):237–291. DOI `10.1162/coli_a_00502`
- Gu, Z., et al. (2025). SBDH-Reader: an LLM-powered method for extracting social and behavioral determinants of health from clinical notes. *JAMIA* 32(10):1570. PMC11875322
- Wang, B., et al. (2025). Extracting social determinants of health from electronic health records: development and comparison of rule-based and large language models-based methods. medRxiv `10.1101/2025.11.15.25339520`
- Fu, Y., Ramachandran, G. K., Dobbins, N. J., Park, N., & Leu, M. (2024). Extracting Social Determinants of Health from Pediatric Patient Notes Using Large Language Models: Novel Corpus and Methods. *LREC-COLING 2024*, pp. 7045–7056
- Yu, J., et al. (2024). Identifying Social Determinants of Health from Clinical Narratives. *J Biomed Inform*. PMC11141428
- Social determinants of health extraction from clinical notes across institutions using large language models. *npj Digital Medicine* (2025). `s41746-025-01645-8`
- Lho, S. K., et al. (2025). LLMs and Text Embeddings to Detect Depression and Suicide in Patient Narratives. *JAMA Network Open*. PMC12102709
- DepressLLM: Interpretable domain-adapted language model for depression detection from real-world narratives. arXiv:2508.08591

### 歧义 / 一致性
- Artstein, R., & Poesio, M. (2008). Inter-Coder Agreement for Computational Linguistics. *Computational Linguistics* 34(4):555–596. DOI `10.1162/coli.07-034-R2`
- Krippendorff, K. (2018). *Content Analysis: An Introduction to Its Methodology*（经 Nakamura et al. 转述 p.24）
- Adcock, R., & Collier, D. (2001).（测量模型，经 Nakamura et al. 转述）
- Proceedings of Context and Meaning: Navigating Disagreements in NLP Annotation (CoMeDi 2025). ACL 2025.comedi-1

### 矛盾 / 时间
- Li, et al. (2024). C³D: Understanding Self-Contradictions in Documents with Large Language Models. *NAACL 2024*, long 362
- Improved Evidence Extraction and Metrics for Document Inconsistency Detection with LLMs. arXiv:2601.02627（引 Graesser & McMahen 1993；Otero & Kintsch 1992）
- Explanation Generation for Contradiction Reconciliation with LLMs. arXiv:2603.22735
- Canby, M. E., et al. (2025). Benchmarking Query-Conditioned Natural Language Inference. *ACL 2025 Findings*, 765, pp. 14808–14835
- Temporal Fact Conflicts in LLMs: Reproducibility Insights from Unifying DYNAMICQA and MULAN. arXiv:2603.15892
- TimeBench: A Comprehensive Evaluation of Temporal Reasoning Capabilities of Large Language Models. *ACL 2024*, long 66
- The Personality Trap: How LLMs Embed Bias When Generating Human-Like Personas. arXiv:2602.03334

### 主动学习 / 负担
- Lewenberg, Y., Bachrach, Y., Paquet, U., & Rosenschein, J. (2017). Knowing What to Ask: A Bayesian Active Learning Approach to the Surveying Problem. *AAAI* 31(1). DOI `10.1609/aaai.v31i1.10730`
- Zhang, X., Taylor, C., Cobb, A., & Sekhon, J. (2020/21). Active matrix factorization for surveys. *Annals of Applied Statistics* 14(3). DOI `10.1214/20-AOAS1322`
- Bassamboo, A., Deep, V., Juneja, S., & Zeevi, A. (2020). Discriminative Learning via Adaptive Questioning. arXiv:2004.05442
- Antonucci, et al. (2021). ADAPQUEST: A Software for Web-Based Adaptive Questionnaires based on Bayesian Networks DAX. arXiv:2112.14476
- Jeong, D., Aggarwal, S., Robinson, J., Kumar, N., Spearot, A., & Park, D. S. (2022/2023). Exhaustive or Exhausting? Evidence on Respondent Fatigue in Long Surveys. NBER WP 30439 / *Journal of Development Economics*. DOI `10.3386/w30439`
- Reynolds, B. M., Robles, T. F., & Repetti, R. L. (2016). Measurement Reactivity and Fatigue Effects in Daily Diary Research with Families. *Developmental Psychology* 52(3):442–456
- Yan, T., et al. (2022). Response Burden – Review and Conceptual Framework. *Field Work and Social Research*. DOI `10.2478/jos-2022-0041`
- US Census Bureau (2021). Research Report Series (Survey Methodology #2021-04)
- Multi-lingual Functional Evaluation for Large Language Models. arXiv:2506.20793

### 幻觉 / 校准 / 文化 / 判官 / 标注 artifact
- Huang, L., et al. (2024). A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions. *ACM Computing Surveys*. DOI `10.1145/3703155`
- A Geometric Taxonomy of Hallucination in LLMs. arXiv:2602.13224
- Stengel-Eskin, V. W., & Wang, C. (2025). Calibrating Verbalized Confidence with Self-Generated Distractors (DiNCo). arXiv:2509.25532
- Wired for Overconfidence: A Mechanistic Perspective on Inflated Verbalized Confidence in LLMs. arXiv:2604.01457 (COLM 2026)
- The Dunning-Kruger Effect in Large Language Models: An Empirical Study of Confidence Calibration. arXiv:2603.09985（preprint，弱证据）
- Sanz-Guerrero, M., et al. (2026). Large Language Models Are Overconfident in Their Own Responses. *ACL 2026 Findings*, 1570
- Xiong, M., et al. (2024). A Survey of Confidence Estimation and Calibration in Large Language Models. *NAACL 2024*, long 366
- Cheng, M., et al. (2024). Implicit Reasoning Biases in Persona-Assigned LLMs. *ICLR 2024*
- Li, D., et al. (2025). Political Bias in LLMs: Unaligned Moral Values in Agent-centric Simulations. *Journal of Language Technology and Computational Linguistics* 38(2):125–138. DOI `10.21248/jlcl.38.2025.289`
- Lutz, J., et al. (2025). The Prompt Makes the Person(a): A Systematic Evaluation of Persona Prompting Strategies. *EMNLP 2025 Findings*, 1261
- Weeber, F., et al. (2026). One Persona, Many Cues, Different Results. *ACL 2026*, long 2079
- Tan, B. C., et al. (2026). Can Persona-Prompted LLMs Emulate Subgroup Values? *ACL 2026*, long 1127
- Argyle, L. P., et al. (2023). Out of One, Many: Using Language Models to Simulate Human Samples. *Political Analysis* 31(3):337–351. arXiv:2209.06899
- Li, D., Li, L., & Qiu, H. S. ChatGPT is not A Man but Das Man. arXiv:2406.12934
- Identifying Non-Replicable Social Science Studies with Language Models. arXiv:2503.10671
- Zheng, L., et al. (2023). Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. *NeurIPS 2023*. arXiv:2306.05685
- Panickssery, Y., Bowman, S. R., & He, H. (2024). Self-Preference Bias in LLM-as-a-Judge. arXiv:2410.21819
- Play Favorites: A Statistical Method to Measure Self-Bias in LLM-as-a-Judge. arXiv:2508.06709
- Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines. arXiv:2604.23178
- Gururangan, S., et al. (2018). Annotation Artifacts in Natural Language Inference Data. *NAACL 2018*, main 202. arXiv:1803.02324
- McCoy, R. T., Pavlick, E., & Linzen, T. (2019). Right for the Wrong Reasons: Diagnosing Syntactic Heuristics in Natural Language Inference. *ACL 2019*, 66, pp. 3428–3448

### 多语言 / 测量
- MuBench: Assessment of Multilingual Capabilities of Large Language Models Across 61 Languages. arXiv:2506.19468
- Left Behind: Cross-Lingual Transfer as a Bridge for Low-Resource Languages in Large Language Models. arXiv:2603.21036
- Wang, W., et al. (2024). Analyzing the Evaluation of Cross-Lingual Knowledge Transfer in Multilingual Language Models. *EACL 2024*, 177. arXiv:2402.02099
- Cross-Lingual Pitfalls: Automatic Probing Cross-Lingual Weakness of Multilingual Large Language Models. *ACL 2025*, 404
- Davidov, E., Muthén, B., & Schmidt, P. (2018). Measurement Invariance in Cross-National Studies. *Cross-Cultural Research*. DOI `10.1177/0049124118789708`
- Putnick, D. L., & Bornstein, M. H. (2016). Testing the Equivalence of Factor Covariance and Mean Structures: The Issue of Partial Measurement Invariance. *Psychological Bulletin* 105(3):456–466
- Measurement Invariance of the Scale of Positive and Negative Experience Across 13 Countries. CDC Stacks
- Chinese version of the International Positive and Negative Affect Schedule short form. *Health and Quality of Life Outcomes* (2020). DOI `10.1186/s12955-020-01526-6`
- Cross-Cultural Measurement Invariance of Scales Assessing Stigma and Attitude to Seeking Professional Psychological Help. PMC6554279 / *Frontiers in Psychology* `10.3389/fpsyg.2019.01249`
- Lacko, D., et al. (2022). The Necessity of Testing Measurement Invariance in Cross-Cultural Research. *Cross-Cultural Research*. DOI `10.1177/10693971211068971`
- Rammstedt, B., et al. (2013). A Short Scale for Assessing the Big Five Dimensions of Personality: 10 Item Big Five Inventory. *MDA* 7(2). DOI `10.12758/mda.2013.013`
- Gerlitz, & Schupp. Short assessment of the Big Five. PMC3098347
- Meta-Analytic Guidelines for Evaluating Single-Item Reliabilities of Personality Instruments. PMC4332286
- Examining the Concurrent and Predictive Validity of Single Items in Ecological Momentary Assessments. PMC10248304
- Bergkvist, L., & Rossiter, J. R. (2007). The Predictive Validity of Multiple-Item versus Single-Item Measures of the Same Constructs. *J. Marketing Research* 44(2):175. DOI `10.1509/jmkr.44.2.175`

### Provenance
- W3C Provenance Working Group (2013-04-30). PROV-DM / PROV-O / PROV-N / PROV-CONSTRAINTS（W3C Recommendations）；*PROV Model Primer*. `https://www.w3.org/TR/prov-primer`
- PROV-AGENT: Unified Provenance for Tracking AI Agent Interactions in Agentic Workflows. arXiv:2508.02866

### 项目内文档（本报告只读，未修改）
- `AGENTS.md`
- `docs/foundation/CURRENT_ARCHITECTURE.md`（as of 2026-09-10）
- `docs/validation/VALIDATION_CORPUS_V0_1.md`
- `docs/validation/fixtures/FIXTURE_001_L0_001_CARTY_FACT_PACKAGE.md`
- `docs/validation/fixtures/FIXTURE_002_L1_003_MAGI_PACKAGE.md`
- `docs/validation/fixtures/FIXTURE_003_L1_001_STORYCORPS_PACKAGE.md`
- `docs/research/RESEARCH_REPORT_REAL_WORLD_PROXY_DECOMPOSITION.md`


