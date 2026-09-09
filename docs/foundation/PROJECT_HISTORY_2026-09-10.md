# LHRM Project History — 从起点到 2026-09-10

**Status:** historical/provenance checkpoint  
**As of:** 2026-09-10  
**Purpose:** 记录项目从早期择偶/关系评价问题，到当前 representation-first Human–Human relationship state model 的关键转向、保留项、否决项与研究证据链。

> 本文件用于 provenance 与未来论文写作，不与 `CURRENT_ARCHITECTURE.md` 竞争 current authority。架构现状以 `docs/foundation/CURRENT_ARCHITECTURE.md` 为准。

---

## 0. 项目从什么问题开始

LHRM 最早不是从“建立一门完整的人际关系理论”开始，而是从一个很具体的问题出发：

> **一个人为什么会被另一个人吸引？为什么“想和她在一起”与“适合长期生活”不是同一个判断？**

早期讨论围绕：

- 初始视觉/性吸引；
- 互动后的 chemistry；
- 恋爱与配偶角色的不同评价标准；
- 人的需求会随阶段变化；
- 同一对象在不同 role 下不存在唯一匹配度。

由此形成早期关键区分：

```text
“I want to be with you” gate
!=
“I can live with you long term” gate
```

以及动态直觉：

```text
Like(t)
= F(self(t), other(t), relationship(t), environment(t))
```

这奠定了“关系不是静态对象属性”的起点。

---

## 1. 第一代架构：S / O / D / E

项目最早形成的四层局部结构：

```text
S — Subject / 主体
O — Object / 客体
D — Dyad / 二人系统
E — Environment / 环境
```

研究/评价按：

```text
S -> O -> D -> E
```

逐层展开。

Human 随后明确修正过顺序语义：S 第一、O 第二、D 第三、E 第四，是 **information/evaluation unfolding order**，因为关系未必进入真正二人互动，更未必进入长期现实约束层。

同时引入：

- `t`：状态时间；
- `Role`：评价任务/视角。

这阶段形成了几个至今仍保留的纪律：

- demographics 是输入，不是结论；
- 同一 S/O 在不同 Role 下没有唯一匹配度；
- Unknown 不能当成 0 或完美匹配；
- 不把“漂亮”“贤惠”“真爱”“高价值”当唯一 primitive；
- coarse input 可以作为 noisy evidence，后续再细化。

---

## 2. 早期计算尝试：偏好区域、距离、稀疏输入

为了让模型在少量信息下也可计算，早期尝试过：

```text
Subject + Object + Role
-> active dimensions
-> preferred regions
-> hard constraints
-> soft distance
```

典型形式：

```text
SoftDistance
= sqrt(sum_i w_i * deviation_i^2)
```

同时强调：

```text
Unknown -> prior / uncertainty
```

而不是：

```text
Unknown -> zero deviation
```

这阶段的重要收获不是欧氏距离本身，而是：

1. preferred region 比“越大越好”更符合现实；
2. hard constraint 与 soft preference 必须区分；
3. 稀疏输入必须 graceful degradation；
4. 输出不能伪造 78/100 之类精度。

后来项目逐渐发现：distance / weight / normalization 自身会引入大量任意性，因此它们从“地基”降级成未来可选 readout。

---

## 3. 吸引与 chemistry 的拆分

围绕 physical preference 与 chemistry 的研究推动模型从粗标签向 latent construct 拆分。

物理吸引不再只写“漂亮”，而尝试区分：

```text
aesthetic value
sexual salience
signal inference
learned/idiosyncratic association
```

同时明确：

```text
审美愉悦 != 性吸引 != 接近欲望 != 伴侣价值判断
```

Chemistry 被理解成互动中的正反馈耦合：

```text
signal
-> responsive/high-value response
-> feeling understood/rewarded
-> engagement increases
-> richer signal
-> reciprocal engagement
```

并区分：

```text
social chemistry
romantic chemistry
sexual chemistry
```

由此形成一个重要判断：

```text
S + O does not determine D
```

静态人物资料无法完整推导二人互动层。

---

## 4. 极端故事压力测试：S/O/D/E 不够做世界本体

Human 枚举了长生命周期、高冲突、高不确定性的关系故事：从线上相识、吸引、性关系、快速承诺、家庭干预、同居磨合、结婚、生育、照护、婚外情、离婚、复合/残余依恋等一路展开。

压力测试暴露：

- 第三者、父母、孩子、同事都需要成为独立 Agent；
- deception / concealment / misunderstanding 不能只靠 D 表示；
- 当前状态不足以表达路径依赖；
- relationship labels 不等于底层关系状态；
- 同一事件对不同人可能产生完全不同更新。

因此发生第一次重大架构升级：

```text
WorldState(t)
= Agents + Relationships + Environment
```

并引入：

```text
TrueState != ObservedState != BelievedState
```

以及：

```text
Action/Event -> Transition
```

从这一步开始，`S / O / D / E` 被重新定位为 **local evaluation projection**，不再声称是世界完整 ontology。

---

## 5. 研究域扩展，但不扩成所有生物

随后对同性行为、动物研究、神经/遗传机制等材料的讨论推动 Human 明确范围：

```text
Domain = Human–Human Relationship
Atomic Unit = Two Human Agents + Their Relationship
Animal Research = Mechanism Evidence
```

关键裁决：

> **向下追机制，但不向下扩研究对象。**

因此项目可以使用神经、认知、进化、生物机制帮助识别更好的 construct，但不把 LHRM 变成动物关系模型，也不因为某个变量更微观就自动升级为 primitive。

---

## 6. “参数低相关”被修正为“低语义/条件冗余”

Human 提出一个关键反例：

> “肯花钱”和 attraction 可以是不同参数，但花钱本身又会改变 attraction；那参数是否还算独立？

由此澄清：

```text
basis independence
!=
dynamic independence
```

LHRM 追求的是：

```text
low semantic / conditional redundancy
```

而不是：

```text
zero statistical correlation
```

状态变量可以强烈耦合：

```text
partial F_i / partial z_j != 0
```

但只要现实中可稳定解耦、语义不同、对状态/未来提供独立信息，就不应因为相关而合并。

同时形成：

```text
State + Action + Transition
```

的基本动力学框架。

---

## 7. 关系方向性：A->B 与 B->A 是两条不同状态

随后 Human 明确认同：

> **关系也是有方向的。**

性欲是最直观例子：

```text
SexualDesire(A->B)
SexualDesire(B->A)
```

可以分别高/低。

因此当前关系结构逐渐收敛为：

```text
Relationship_ij
= DirectedState_(i->j)
+ DirectedState_(j->i)
+ PairState_(i,j)
```

由此 mutuality / asymmetry 不再重复设 primitive：

```text
Mutuality_k(A,B)
= H(Z[k,A,B], Z[k,B,A])
```

这一步把“有向图”与“关系向量”真正接起来。

---

## 8. Construct family across scopes：同一个参数名可以一体多面

Human 又提出进一步修正：同一个“吸引”可以在 S、O、D 中表现为不同侧面：

- S：一般容易被别人吸引；
- O：一般容易诱发别人吸引；
- D：特定 A 对特定 B 的特殊吸引。

这与 Social Relations Model 的 perceiver / target / relationship effect 有明显对应。

因此 LHRM 不再追求“一份扁平参数表”，而开始使用 indexed construct family：

```text
Construct.source_i
Construct.target_j
Construct.edge_(i->j)
Construct.pair_(i,j)
```

但不机械要求每个 construct 在每个 scope 都复制。只有独立语义成立才保留。

该结论已固化到：

`docs/foundation/CONSTRUCT_SCOPE_DIRECTIONALITY.md`

---

## 9. 四路独立 Research：从“发明参数”转为“跨源收敛”

Parent research program：`#2`。

四条独立研究 lane：

```text
#3 Games / simulation systems
#4 Scientific relationship constructs
#5 Dating apps / product fields
#6 Real-world proxies / statistics / adversarial cases
```

对应研究报告均已进入 main。

### #3 Games 的主要启发

游戏提供的是 formalization / update / UI 经验，而不是人类真理：

- attraction 不能等于关系长期状态；
- short-term / long-term relation 可分离；
- satisfaction 可以是方向性的；
- discrete labels、continuous states、thresholds、decay、path dependence 可分层；
- 不应建立一个万能“好感度”。

### #4 Science 的主要收敛

高权重候选：

- sexual desire；
- romantic attraction；
- liking；
- attachment security；
- caregiving；
- perceived partner responsiveness；
- trust；
- dedication；
- outcome dependence；
- cohesion / we-ness；
- value congruence；
- goal alignment。

同时：

- commitment 不应把 investment / constraint / satisfaction 混成一个量；
- alignment 更像多个 pair-level 构念的派生压缩；
- power 很可能是 dependence asymmetry 的派生。

### #5 Dating apps 的主要启发

约会产品主要暴露的是 Observation / declared preference / revealed behavior，而不是底层 relationship primitive。

高风险重复计数组：

- age / young appearance / fertility；
- income / assets / spending；
- education / cognition / class；
- companionship / time / availability / responsiveness；
- religion identity / strictness / conservative values。

产品 match score 不可当现实真值。

### #6 Real-world 的主要启发

现实语言大量是 composite proxy：

- “顾家”；
- “有责任心”；
- “肯花钱”；
- “门当户对”；
- “高质量关系”。

它们需要拆到 Agent / Relationship / Belief / Action / Constraint 等更底层结构。

极端案例没有稳定击穿当前顶层 ontology：

```text
Agent + Relationship + Environment + Belief
with Action/Event + Transition
```

因此下一步不再继续广泛收集更多日常词，而进入 Parameter Convergence。

---

## 10. LLM Skill：语言理解与核心模型分离

项目同时形成一个实际应用方向：

```text
Natural language
-> LLM semantic parsing / adaptive interview
-> canonical LHRM representation
-> model core
-> uncertainty-aware result
-> LLM explanation
```

LLM 负责：

- natural-language proxy 解析；
- 自适应追问；
- ambiguity / contradiction / Unknown 检测；
- 结果解释。

LHRM core 负责：

- 状态语义；
- measurement contract；
- transition / simulation；
- uncertainty。

目标是避免 ontology 随 LLM 版本或 prompt 风格漂移。

---

## 11. Case Bank：把案例从“灵感”升级为 regression suite

Human 提出建立真实案例库，尤其优先法院判决/官方材料。

长期 lane：`#13`。

用途被明确限制为：

```text
representation completeness
closure
adversarial coverage
regression
```

而不是 population probability estimation。

法院文书的优势是争议事实会被迫进入正式记录，能覆盖传记、书信、出版物常主动过滤的内容。

同时必须区分：

```text
source quality
!=
fact status
```

即同一份判决内仍需标：

```text
adjudicated | admitted | alleged | disputed | unknown
```

后续验证思路：遮掉法律条款与判决结果，只取事实经过，让独立 Agent 逐句映射到当前 LHRM schema；无法表达的句子单独进入 `MAPPING_FAILURE` 队列。

难度可以逐步升级：

```text
court facts
-> short narrative
-> medium story
-> biography / long-form profile
-> romance novel
-> weird fiction
-> science fiction / fantasy
```

真实材料主要测 empirical coverage，虚构材料主要测 expressivity。

---

## 12. Representation-first 转向：不再急着算一个结果

2026-09-10 形成当前阶段最重要的优先级调整。

Human 明确指出：

> 与其在缺乏可靠权重时强行算出一个 `0..1` 结果，不如先建立一个稳定的动态关系坐标系，使一段百万字故事都能被表示成从开始到结束的关系状态轨迹。

因此当前架构原则正式转为：

```text
Representation before scalarization.
State-space before score.
```

第一阶段的成功标准不再要求：

- 唯一综合分；
- 唯一欧氏距离；
- 唯一权重；
- 所有量归一到 0..1；
- 唯一结局预测。

而要求：

> **每个与二人关系相关的重要事实，都能在模型里找到合法、语义明确、保留不确定性的数学落点。**

一个时刻可抽成 snapshot，一整段关系则形成 trajectory / dynamic tensor。

这让模型即使暂时不预测，也具有独立价值：

- 社会科学编码；
- 长文本关系抽取；
- 游戏角色/关系模拟；
- 历史/法律案例结构化；
- ABM 初始状态与事件轨迹；
- 后续 prediction/readout 的公共底座。

---

## 13. Fuzzy / normalization / metric 的新定位

Human 对 fuzzy decision / fuzzy mathematics 的观察推动另一个边界澄清：

可借鉴：

- membership / vague concept representation；
- linguistic-to-numeric/interval mapping；
- uncertainty-aware representation；
- ordinal / fuzzy evidence。

不默认接受：

- 任意 membership function 当真值；
- 人工权重叠加后伪装成精确科学；
- 强制 defuzzification；
- 强制所有东西进入 0..1；
- 用单一 weighted Euclidean distance 代替关系状态本身。

Measurement 层当前原则：

```text
RawObservation
-> CanonicalRepresentation
-> ModelState
```

原始输入保留，归一化只是 computational projection。

---

## 14. 时间不再局限于一条线：history branch 与 nested world

Human 进一步指出：时间旅行、梦境、反事实并不会真正击穿当前架构。

如果世界历史发生分叉：

```text
fork(history, t0) -> history'
```

新历史可成为 active/main lineage，旧历史只保留 provenance；不要求强制 merge 冲突事实。

梦境、幻想、计划、反事实则可视为 Belief 内部的 nested simulated world：

```text
SimWorld_(A,m)
= fork(Belief_A, mode=dream|plan|counterfactual|fantasy)
```

其内部也可运行同一 Human–Human state language，但不会自动写回真实 WorldState。

这验证了一个更强的架构思想：

> **复杂叙事应尽量由已有 primitive + scope + history + composition 生成，而不是为每类故事发明专用参数。**

---

## 15. 到 2026-09-10，哪些东西已被否决或降级

当前明确不再把以下内容当 LHRM 地基：

- 单一 compatibility score；
- “爱情浓度”总分；
- 所有关系都走离散状态机；
- 把关系标签当底层状态；
- 把 spending / messages / sex acts 直接当 latent relationship primitive；
- 把 attraction / liking / sexual desire 混成一个量；
- 把 commitment / investment / satisfaction / dependence 混成一个量；
- 仅靠 raw correlation 做 parameter merge；
- 所有维度强制归一到同一 0..1；
- 为极端故事增设 ad-hoc special parameter；
- 把高层自然语言 proxy 当 ontology。

这些并非永远不能作为 UI/readout/derived variable，而是不能反过来定义底层状态空间。

---

## 16. 当前形成的最短架构链

截至当前，最简洁的项目路线可以压缩成：

```text
Human social world
-> local dyad projection
-> indexed construct families
-> two directed relationship states + pair state
-> time/history-indexed snapshots
-> trajectory / dynamic tensor
-> optional measurement / transition / prediction / simulation / decision readouts
```

或者：

```text
Graph
-> Local Projection
-> Directed State Representation
-> Trajectory
-> Optional Readout
```

---

## 17. 当前 durable work graph

核心 parent：`#2`。

已完成首轮 Research evidence：

- `#3` Games；
- `#4` Scientific constructs；
- `#5` Dating apps；
- `#6` Real-world proxies。

长期 benchmark：

- `#13` Case Bank / completeness regression。

当前 next stage：

```text
Parameter Convergence
-> Candidate Minimal Sufficient State v0.1
-> first representation coverage fixture
-> Measurement & Canonicalization v0.1
```

本轮开始推进：`docs/foundation/PARAMETER_CONVERGENCE_V0_1.md`。

---

## 18. 对未来论文最重要的 provenance

若 LHRM 后续形成论文，应该保留并明确：

- Human 原始问题如何改变研究范围；
- 哪些 construct 来自现有关系科学；
- 哪些架构只是对已有理论的集成；
- 哪些 candidate 被合并、拆分或否决；
- 极端案例如何暴露 ontology hole；
- representation-first 为什么取代 premature scalarization；
- 失败的公式、权重与 normalization 尝试；
- Case Bank 的 MAPPING_FAILURE；
- 后续真实纵向数据能否验证 transition / prediction。

优先把潜在贡献表述为：

> **统一的人类二人关系状态表示框架、观测/信念/不确定性接口、方向性与动态轨迹语义，以及可重复的 representation-completeness 验证方法。**

而不是“发明了一个万能爱情公式”。
