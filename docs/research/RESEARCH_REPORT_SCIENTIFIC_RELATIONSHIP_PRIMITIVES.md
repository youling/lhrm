# RESEARCH_REPORT_SCIENTIFIC_RELATIONSHIP_PRIMITIVES

```yaml
work_coordinate: youling/lhrm#4@deep-scientific-relationship-primitives
dispatch: youling/lhrm#4 issuecomment 5565248580 (ARCHITECT_RESEARCH_DISPATCH_V2)
supersedes: youling/lhrm#4 issuecomment 5565095219 (prior dispatch, current scope)
parent: youling/lhrm#2
current_rulings:
  - youling/lhrm#2 issuecomment 5565170990 (scope: general relationship system, non-hetero default, decoupling test)
  - youling/lhrm#2 issuecomment 5565245810 (domain boundary: human–human dyad; mechanism|primitive_state|observable_proxy|derived_outcome|role_constraint; minimal sufficiency)
  - youling/lhrm#4 issuecomment 5565173033 (assumption_stress_test; sex/orientation/bond/identity separation; cross-species caution)
role: Research
startup_mode: Fresh Research
status: DRAFT_FOR_ARCHITECT (研究交付物；不改写 canonical ontology)
as_of: 2026-09-07
language: zh-Hans
unit_of_analysis: Human–Human Dyad (两个具体的人及其关系边)
```

本报告是 `youling/lhrm#4` 下、按 `ARCHITECT_RESEARCH_DISPATCH_V2`（comment `5565248580`）执行的深研交付。它回答的核心问题是：**在 Human–Human Dyad 上，哪些“关系状态”语义上足够独立、可操作、能解释状态转移，值得作为 LHRM 的最小充分 primitive；哪些只是观测代理、派生结果、机制证据或角色约束。** 本报告是研究产物，不冻结任何数值/权重，也不修改 canonical ontology；全部建议最终由 Project Architect 在 `#2` 统一仲裁。

---

## 0. 摘要与主结论

### 0.1 一句话结论

日常语言与多数科普把关系拆成“喜欢、爱、投入、三观合、占有、安全感、新鲜感”，它们几乎都不是单一 primitive——绝大多数是**若干个相互独立的基础状态 + 上下文/角色/阶段**的复合物；而真正的最低层关系状态，方向是“每个主体对客体的一条有向边上的少量状态”，且**不能靠更底层机制替代**（多巴胺、催产素、脑区只是机制证据，不自动成为关系状态）。

### 0.2 六维候选裁决速览

对当前 LHRM Relationship 候选维度（Attraction / Bond / Trust / Commitment / Alignment / Dependence）的逐项裁决（详见 §7）：

| 候选维度 | 裁决 | 一句话理由 |
|---|---|---|
| **Attraction** | **SPLIT**（至少拆成 `性欲/性吸引` 与 `浪漫/亲和吸引`，`liking` 另计） | 性欲、热恋式浪漫、喜欢愉悦三者方向、时程、去耦状态各不相同，混在一个“吸引”里会丢失最关键的方向性与模式差 |
| **Bond** | **SPLIT/REDEFINE**（拆为 `依恋安全(attachment-security)` 与 `情感凝聚/we-ness(cohesion)`） | “纽带”同时吞并了依恋系统、情感凝聚与投入，语义过宽；作为单一 primitive 站不住 |
| **Trust** | **KEEP**（精确定义，拆出 `distrust` 与 `predictability` 分面） | 信任是“愿在风险下依赖对方善意可靠性”的方向性信念状态，可在安全之外独立存在（同事、长期合作、非亲属） |
| **Commitment** | **KEEP/REDEFINE**（定义为 `dedication`；把 `constraint`、`investment`、`dependence` 拆出） | 承诺常被误用为“投入+无备选+满意”的总和；最小状态是“持续维持关系的主观意愿/义务感”，与投资、依赖、满意必须分离 |
| **Alignment** | **REJECT 作为 primitive / 降为 DERIVED 评价维度**（拆为 `value/goal congruence` 与 `response match`） | “三观合”大多是可计算的偏好/目标一致性（pair 属性），不是有方向、可随时间转移的独立关系状态；与 `similarity` 高度纠缠 |
| **Dependence** | **KEEP**（用互依理论定义 `outcome dependence`），并导出 `power`（不对称依赖） | 依赖是产生约束承诺与权力不对称的结构变量，不是一种“感觉”或评价；最小充分性成立 |

> 说明：以上是“能否作为最小充分 primitive 存活”的裁决。作为**面向人的总览维度**（非 minimal primitive），六个词仍可能以 DERIVED / RATING 形式保留，但必须标注其成分构成，避免当 primitive 平级使用。

### 0.3 顶层 findings

1. **“方向性”是 primitive 的第一属性。** 关系状态几乎都发生在有向边上（Alix→Bob 的信任、Bob→Alix 的性欲），而“我们俩的三观合”“我们俩很密集”是 pair 属性。把有向状态与 pair 属性混层，是多数误区来源。
2. **机制 ≠ 状态。** 激素、神经递质、脑区、进化功能都是“解释某状态为何如此 (mechanism / evidence)”，不是可被直接建模为关系变量的状态（primitives）。只有在极少数情况下（如仅在性系统里出现的生理唤起）它才提供高阶状态无法替代的独立信息（仍可建模为生理 proxy）。
3. **“爱”几乎一定是个高阶组合态**，不是 primitive。不同文化/理论的“爱”≈ 依恋安全 + 性欲/浪漫吸引 + 投入/承诺 + 情感凝聚 + 关怀的加权或典型组合；单独作为 primitive 会同时吞掉多个独立轴。
4. **六维里，真正够“primitive 级”且能独立存活的是 Trust 与 Dependence**；Attraction 与 Bond 需要拆；Commitment 需瘦身为 dedication；Alignment 应降级为 derived。
5. **alignment/similarity/compatibility 必须三角化**：`similarity`（客体属性距离，可观测）、`value-goal congruence`（价值观/目标一致性，偏潜变量）、`complementarity`（功能互补）。三者被“三观合/互补/般配”混在一起。
6. 生物-神经类术语中，应留在 **mechanism 层**的有：多巴胺奖赏、奖赏预测误差、催产素、血管加压素、杏仁核/威胁回路、镜像/同步神经过程、性二态与激素、基因亲缘识别；不应被直接提为 LHRM primitive。

---

## 1. 任务、边界与本报告地位

### 1.1 本报告做什么

- 从关系科学、社会心理学、人格、认知/决策科学、神经/行为生物学、进化理论、互依理论，以及已有计算/形式化关系模型，建立跨学科构念地图与**语义边界审计**。
- 对 ≥50 个候选构念，逐项给出来源、定义、属于哪一层（mechanism / primitive_state / observable_proxy / derived_outcome / role_constraint）、常见代理词、易混构念、是否保留/合并/降级/淘汰、证据分级、反例解耦、以及跨关系形态的稳定性（assumption_stress_test）。
- 给出 `mechanism → primitive_state → observable_proxy/derived_outcome` 三层图。
- 对当前六维候选逐项 KEEP / SPLIT / MERGE / REJECT 并说明证据。
- 提供 ≥15 组易混淆构念成对比较、≥40 条日常代理词映射、建议合并/淘汰清单、关键争议与剩余不确定性。

### 1.2 本报告不做什么（boundary）

- **不修改 canonical ontology**；不冻结数值、权重、阈值、公式、概率。
- **不扩研究对象**为一般生物/动物关系模型；动物、遗传、神经、进化研究只被作为识别人类 dyad primitive 的机制证据 (mechanism evidence)，不做直接外推。
- **不以异性恋婚恋为默认模板**：语义必须在 same-sex / opposite-sex / kin / non-kin / stranger / established relationship 之间保持稳定，或明确标注该构念仅在某种关系形态下才有意义（那属于 role/constraint 层，而非 primitive）。
- 不把相关性当同一构念，不把机制因子直接当关系状态，不把单篇研究结论升级为 canonical primitive。

### 1.3 术语口径

沿用 `#2 裁决 5565245810` 的五分类，并在此明确其判据：

| 类别 | 含义 | 判据要点 |
|---|---|---|
| `mechanism` | 解释关系状态“为何如此/如何产生”的更低层机制或证据（生物、神经、进化、认知过程） | 不给它直接赋予“关系状态值”，只用于解释与跨层验证 |
| `primitive_state` | 最小充分的关系状态变量：可作为模型状态、随事件更新、能驱动转移 | 满足 §2.3 的最小充分性判据（不可再归约、可去耦、有动力学、可估计、跨形态稳定） |
| `observable_proxy` | 可直接观测/报告/测得的指标，用来向上推断 primitive 或向下被 primitive 解释 | 测量指标（问卷题、行为、表现、生理 proxy），不等于被推断的状态 |
| `derived_outcome` | 由若干 primitive/状态计算出的高阶结果（关系质量、满意度、总体“爱”、稳定性、婚姻决策） | 是 primitive 的消费者，不作为平级输入 |
| `role_constraint` | 由角色/任务/社会契约/阶段强加的条件（婚姻义务、排他约定、亲属义务、前任关系、第三者） | 是约束与上下文，不是主体内在状态；可调节 primitive 如何组合 |

> `layer` 一栏中，我会额外沿用 `#2` 的 S / O / D / E 视图标注（该状态主要属于哪一层），但注意 `#2` 已裁定 S/O/D/E 是“查询局部视图”，不是完整世界本体；primitive 大多落在 `D`（有向 dyad 边）或 `S`（per-agent），`E` 多为约束/上下文。

---

## 2. 方法：证据、分层与最小充分性判据

### 2.1 证据分级

为避免把未经验证的公式/参数/关系表述为已确证，全报告统一使用如下证据等级，并在每个构念的 `evidence` 字段标注：

| 等级 | 含义 |
|---|---|
| `E1 established` | 构念定义与测量在多源/多研究稳定复现，有系统综述或 meta-analysis 支撑其结构或独立性 |
| `E2 plausible` | 理论成熟、有一定高质量实证，但界定、测量或跨样本一致性仍有争议 |
| `E3 speculative` | 理论上有吸引力，但直接实证稀缺或主要靠推理 |
| `C contested` | 领域内存在明确竞争假说与反证，不能当作事实陈述，必须标注双方证据 |
| `M mechanism` | 作为机制/证据层引用（生物、神经、进化），不单独成为状态 |

凡是我无法确证具体效应量的地方，只给“量级/方向 + 分级”，不编造精确相关数。

### 2.2 术语五分类（见 §1.3）

### 2.3 最小充分性判据（Minimal Sufficiency Criteria, MSC）

候选 `X` 有资格成为 `primitive_state`，需同时满足五条：

1. **语义不可归约**：不存在另一个更省的状态或现有状态组合能无失真地同时表达 `X` 与其否定（跨现实 dyad）。若 X 只是 A、B 的某个组合，则 X 是 derived。
2. **独立性（可去耦）**：对每个其他 primitive `Y`，存在真实可发生的“X 高 Y 低”与“X 低 Y 高”状态（反例解耦）。
3. **动力学**：X 会随具体事件/交互更新，并能驱动下一状态转移；若只是静态 trait 或环境属性，则归入 S/O/E 属性或约束，而非 D 层状态。
4. **可估计**：X 能被一组明确的 observable_proxy（自我报告/行为/生理标量）推断，或在无法直接观测时作为有指标集的 latent 变量被估计。
5. **跨形态稳定**：X 的语义身份在不同关系形态（same-sex / opposite-sex / kin / non-kin / stranger / established）下要么保持同一，要么明确退化为 role/constraint 变体并给出退化规则；一个只在“异性恋情侣”里才有意义的概念不自动成为 primitive。

### 2.4 反例解耦与 assumption_stress_test

对每个候选构念，按下述两个测试约束其语义边界：

- **反例解耦 (decoupling)**：构造两个现实中可能的状态——`A 高 B 低` 与 `A 低 B 高`。若构造不出，说明二者可能不是独立构念，应考虑合并或降级。
- **assumption_stress_test**（来自 `#4 5565173033`）：逐项说明该候选在 same-sex / opposite-sex / kin / non-kin / stranger / established-relationship 六种 dyad 形态下是否保持同一语义（`stable` / `stable-as-role-variant` / `meaningless-here`），以及它属于 `behavior / attraction / preference-orientation / identity / bond / role / kinship` 哪一种或哪几种不可混同的概念。

### 2.5 全候选构念裁决索引

> 下表是 §4 审计结果的索引，便于导航与跨来源去重。`层` = 五分类；`裁决` = KEEP / SPLIT / MERGE / DERIVED / OBSERVATION_ONLY / REJECT / MECHANISM。F = 纳入“最小充分核心候选”（详见 §7.3）。

#### A. 动机 / 趋向（有向，per-agent → partner）

| # | 构念（英/中） | 层 | 裁决 | F |
|---|---|---|---|---|
| A01 | Sexual desire / 性欲 | primitive_state | KEEP | ✔ |
| A02 | Romantic/Lustful attraction（热恋/浪漫吸引） | primitive_state | KEEP | ✔ |
| A03 | Liking / positive regard（喜欢/正向评价暖感） | primitive_state | KEEP | ✔ |
| A04 | Reward valuation / incentive salience（奖赏评价） | mechanism | MECHANISM |  |
| A05 | Sexual orientation / preference（性向偏好） | role_constraint/Agent attr | KEEP(约束属性) |  |
| A06 | Intimacy motivation / sociosexuality（短择取向） | derived/agent | OBSERVATION_ONLY→DERIVED |  |

#### B. 依恋 / 关怀 / 纽带

| # | 构念 | 层 | 裁决 | F |
|---|---|---|---|---|
| B01 | Attachment (security/安全依恋，per-agent→partner) | primitive_state | KEEP | ✔ |
| B02 | Felt security / secure base & safe haven（被托底感） | primitive_state | MERGE into B01 |  |
| B03 | Attachment anxiety / avoidance（焦虑/回避维） | Agent attr（系统/倾向） | OBSERVATION_ONLY |  |
| B04 | Caregiving / 关怀照护 | primitive_state | KEEP | ✔ |
| B05 | Affiliative bond / cohesion（情感凝聚/we-ness） | primitive_state | KEEP | ✔ |
| B06 | Pair-bond（配对纽带，romantic exclusivity 语境） | derived/role | DERIVED |  |
| B07 | Social proximity / touch（身体亲近/触摸） | observable_proxy | OBSERVATION_ONLY |  |
| B08 | Loneliness / relationship need（孤独/关系需求） | derived(S) | DERIVED |  |

#### C. 互依 / 认知 / 承诺

| # | 构念 | 层 | 裁决 | F |
|---|---|---|---|---|
| C01 | Trust / 信任 | primitive_state | KEEP | ✔ |
| C02 | Distrust（不信任） | primitive_state | KEEP（与信任分离） |  |
| C03 | Predictability / 可预测性 | facet | OBSERVATION_ONLY（分面） |  |
| C04 | Perceived partner responsiveness (PPR) / 感知被回馈 | primitive_state | KEEP | ✔ |
| C05 | Intimacy / 亲密 | derived（由披露+回馈累积） | DERIVED |  |
| C06 | Self-disclosure / 自我披露 | observable/behavior | OBSERVATION_ONLY |  |
| C07 | Closeness / 心理接近(we-ness overlap) | derived | DERIVED |  |
| C08 | Commitment (dedication) / 承诺-投入意愿 | primitive_state | KEEP | ✔ |
| C09 | Constraint commitment / 结构性承诺 | derived/structural | DERIVED |  |
| C10 | Investment / 投入（时间资源情感） | observable_proxy | OBSERVATION_ONLY |  |
| C11 | Alternative quality / 替代质量 | observable/E (CL-alt) | OBSERVATION_ONLY |  |
| C12 | Satisfaction (outcome - CL) / 满意 | derived | DERIVED |  |
| C13 | Outcome dependence / 结果依赖 | primitive_state | KEEP | ✔ |
| C14 | Power (asymmetrical dependence) / 权力 | derived(structural) | DERIVED |  |
| C15 | Gratitude / resentment bank（情感账本） | derived/state | DERIVED (可作中间状态) |  |

#### D. 兼容性 / 配对

| # | 构念 | 层 | 裁决 | F |
|---|---|---|---|---|
| D01 | Similarity (actual/perceived) / 相似性 | pair 属性（可观测） | OBSERVATION_ONLY |  |
| D02 | Value congruence / 价值观一致 | latent(pair) | KEEP(潜) | ✔ |
| D03 | Goal alignment / 目标同向 | latent(pair/state) | KEEP(潜) | ✔ |
| D04 | Complementarity / 互补 | pair 属性/derived | DERIVED |  |
| D05 | Ideal standards match / 理想标准匹配 | derived(评价) | DERIVED |  |
| D06 | Mate value / desirability / 择偶价值 | derived(S/O) | DERIVED |  |
| D07 | Assortative matching / 类别匹配 | E/derived | DERIVED |  |
| D08 | Perceived compatibility / “般配感” | derived | DERIVED |  |

#### E. 交互 / 调节

| # | 构念 | 层 | 裁决 | F |
|---|---|---|---|---|
| E01 | Reciprocity / 互惠 | derived(事件账) | DERIVED |  |
| E02 | Cooperation / 合作 | observable/state | OBSERVATION_ONLY |  |
| E03 | Coordination / synchrony / 协调同步 | observable_proxy | OBSERVATION_ONLY |  |
| E04 | Conflict / 冲突 | observable(事件) | OBSERVATION_ONLY |  |
| E05 | Repair / reconciliation / 修复和解 | observable/event | OBSERVATION_ONLY |  |
| E06 | Forgiveness / 原谅 | state/event | KEEP(可作状态) |  |
| E07 | Responsiveness behavior / 响应行为 | observable_proxy | OBSERVATION_ONLY |  |
| E08 | Exchange fairness / equity / 公平 | derived(账) | DERIVED |  |
| E09 | Co-regulation / emotion coreg / 共调 | mechanism/derived | MECHANISM→DERIVED |  |

#### F. 威胁 / 排他 / 认知辩护

| # | 构念 | 层 | 裁决 | F |
|---|---|---|---|---|
| F01 | Jealousy / 嫉妒 | derived/state | DERIVED(可作信号) |  |
| F02 | Mate guarding / 伴侣守护 | observable/role | DERIVED→ROLE |  |
| F03 | Exclusivity agreement / 排他约定 | role_constraint | KEEP(约束状态) | ✔ |
| F04 | Infidelity / betrayal / 出轨背叛 | event/derived | OBSERVATION_ONLY |  |
| F05 | Deception detection / 欺骗识别 | mechanism/state | MECHANISM |  |
| F06 | Uncertainty / belief update / 不确定更新 | mechanism(state,认知) | MECHANISM |  |
| F07 | Expectation violation / 期望违背 | event/mechanism | MECHANISM |  |
| F08 | Positive illusions / idealization / 理想化 | derived(cognition) | DERIVED |  |

#### G. 性 / 偏好 / 亲属 / 身份

| # | 构念 | 层 | 裁决 | F |
|---|---|---|---|---|
| G01 | Sexual compatibility / 性契合 | dyad 匹配 | KEEP(潜) |  |
| G02 | Arousal (physiological) / 生理唤起 | mechanism/生理 proxy | MECHANISM |  |
| G03 | Asexuality & desire-mode variation | Agent attr | KEEP(属性) |  |
| G04 | Kinship recognition / 亲缘识别 | mechanism | MECHANISM |  |
| G05 | Incest avoidance / 近亲回避(厌恶/Westermarck) | mechanism/role | MECHANISM |  |
| G06 | Relationship identity / “我们”认同 | role/identity | KEEP(身份状态) | ✔ |
| G07 | Love typologies (现实的组合态) | derived | DERIVED |  |
| G08 | Status/prestige/安全感代偿 | derived/mechanism | DERIVED/MECHANISM |  |

> 备注：上表把若干“机制层”术语明确留档在 MECHANISM/观察层，避免被“科学感”冒充 primitive；§5 会再集中列出应留 mechanism 层的神经-生物术语。

---

## 3. 跨学科构念地图与来源

本节说明“哪些学科传统贡献了哪些构念、各自的测量或理论传统、证据强度”，作为后面逐项审计的坐标系底座。这既回答“从哪里找更基础的词”，也用来反制“越底层越好”的倾向。

### 3.1 主要学科来源与它们贡献的关键构念

| 学科/传统 | 代表性理论与经典来源 | 贡献的关键构念 | 对 primitive 的意义 |
|---|---|---|---|
| **关系/亲密科学** | Reis & Shaver 亲密过程模型（1988）；Berscheid（1983, 2010）情感互依与亲密；Eastwick & Finkel 择偶评价理论（2023） | PPR、亲密、情感互依、自我披露 | 直接产出候选 primitive（PPR）与澄清“亲密=过程结果” |
| **社会心理/互依理论** | Thibaut & Kelley（1959）；Kelley & Thibaut（1978）；Rusbult & Van Lange（2003） | 结果依赖、CL/CL-alt、权力(冲突结构)、互依 | `Dependence`、`Power` 的结构性基础，强 |
| **投资模型** | Rusbult（1980, 1983）；Le & Agnew（2003, meta） | 承诺、投入、替代质量、满意 | 承诺=满意−替代+投入的经典分解（E1） |
| **承诺研究** | Adams & Jones（1997）；Stanley & Markman（1992） | dedication vs constraint；道德承诺 | 拆出“承诺的最小状态=dedication” |
| **依恋理论** | Bowlby（1969, 1973, 1980）；Ainsworth；Hazan & Shaver（1987）；Brennan, Clark, Shaver（1998, ECR）；Mikulincer & Shaver（2007） | 安全依恋、safe haven/secure base、焦虑/回避维、关怀照护 | `Attachment`、`Caregiving` 系统；焦虑/回避是 Agent 属性 |
| **性研究** | Kinsey；Storms；Baumeister & Joiner 等；Penke & Asendorpf（2008, SOI-R）；Basson（2000, 女性欲） | 性欲、性取向、sociosexuality、唤起、性吸引 vs 浪漫吸引 | 拆“吸引”→性欲/浪漫；性取向是属性不是状态 |
| **进化行为科学** | Buss（1988, 1992）；Buss & Schmitt（1993）；Haselton & Buss（2000, 误差管理）；Thornhill & Gangestad | 择偶策略、伴侣守护、嫉妒、地位、亲本投资、配偶价值 | 多数是“功能解释/derived/role”，非最低状态；提供跨物种 select 线索 |
| **认知/决策科学** | Tversky & Kahneman；Paulhus？；Funder；Fletcher & Simpson（2000）理想标准模型；Murray（2001, 积极错觉） | 理想标准匹配、偏好构建、信念更新、积极错觉、期望违背 | 多数是认知机制/derived；“匹配评价”非状态 |
| **神经/内分泌/基因** | dopamine-ventral tegmental area；oxytocin-arginine vasopressin（prairie vole）；amygdala；reward prediction error（Schultz） | 奖赏、RPE、催产素/AVP、威胁回路、亲缘识别 | 全部是 mechanism evidence，除非能提供不可替代信息，否则不提为 primitive |
| **计算关系模型/形式化** | 互依作为博弈结构（囚徒困境/迭代）；马尔可夫/状态转移（关系阶段）；贝叶斯信念更新（信任）；动态系统模型（如 Gottman 系）；agent-based 择偶/市场模拟 | 状态变量、转移、观测/信念分离 | 提供“状态—观测—更新”的建模语法，但不直接给出语义 primitive |

### 3.2 从计算/形式化视角学到了什么

1. **状态、观测、信念三层必须分离**：模型里的 `state`（真实关系状态）、`observation`（可测/可见信号）、`belief`（每个主体对 state 的不完全信念）是三种东西。日常词的模糊大多来自把 belief 当 state、把 observation 当 state。
2. **关系是事件驱动、路径依赖、带方向的边**：事件（披露、背叛、关心、修复）改变有向边上的状态；历史路径决定当前转移（习惯、记忆、情感账本）。
3. **低层机制可解释、但可被高层状态“吸收”**：这是 `#2 5565245810` 的核心判据——“若已知候选状态后，更底层机制对状态转移几乎不再提供独立信息，则更底层项留在 mechanism/evidence 层”。例如知道“信任高低”后，具体是哪次多巴胺释放导致的，对预测后续信任转移帮助不大。
4. **互依是结构，不是感觉**：`outcome dependence`（某主体获得满意结果在多大程度上依赖这段关系及其替代）与由此派生的 `power` 不对称，是状态转移和“为什么离不开”的结构解释，不是主观评价词。

---

## 4. 候选构念语义边界审计（50+）

> 每个构念按 `#2` 统一字段输出：`canonical_name`、`layer`（五分类 + S/O/D/E 视图）、`observable_or_latent`、`common_proxies`、`overlaps_with`、`keep_separate_because`、`merge_or_derive`、`evidence`、`edge_cases`（反例解耦）、`assumption_stress_test`。
>
> 缩写约定：`PS`=primitive_state，`OB`=observable_proxy，`DV`=derived_outcome，`RC`=role_constraint，`ME`=mechanism。

### 4.A 动机 / 趋向（有向，per-agent → partner）

#### A01 — Sexual desire / 性欲（性吸引）
- **layer**: PS / D（有向，Alix→Bob 定向）
- **definition**: 对特定对象的、唤起驱动的亲近—性行为动机状态，方向性强烈，模式=性。
- **observable_or_latent**: latent（自我报告 + 生理唤起 + 行为均可代理，但任一代理都有误报）
- **common_proxies**: “想睡TA”“来电”“有性趣”“性欲旺盛→泛指”
- **overlaps_with**: romantic attraction、arousal、lust、appetitive reward
- **keep_separate_because**: 浪漫爱≠性欲（反例可构造）；mode 可独立于 valence（激动 vs 排斥）；临床证据（sexual desire 与 romantic commitment 可分离：无性情侣、性欲但零浪漫的 casual 关系、asexual 浪漫关系真实存在）。性欲有独特生理 proxy（唤起、睾酮/周期）而不必依赖浪漫爱来估计。
- **merge_or_derive**: KEEP（作 PS）
- **evidence**: E1（性欲与浪漫吸引/依恋在时程与测量上可分离；sexual orientation ≠ sexual desire ≠ sexual behavior 已是被接受的区分）；注意“性欲”尚无单一统一量表，多成分（兴趣、唤起、频率）。
- **edge_cases**: 高性欲零浪漫（约炮、婚外性但爱情为零）；低性欲高浪漫（性冷淡却深爱；无性恋浪漫伴侣）；性欲方向与关系身份错配（性欲指向第三人）。
- **assumption_stress_test**: same-sex/opposite-sex/kin/non-kin/stranger/established —— 语义在 non-kin 各类 dyad 稳定（性欲对亲属通常应≈0 或受约束）；对 kin 需显式允许“近亲但性欲被抑制”（不可假定零）。mode 为性，与 orientation 是属性分开。

#### A02 — Romantic/Lustful attraction（热恋/浪漫吸引）
- **layer**: PS / D（有向）
- **definition**: 对特定对象的、包含理想化/渴望/亲密幻想/排他愿望的高唤起的浪漫趋向动机。
- **observable_or_latent**: latent（自我报告强烈；可代理：理想化叙述、独处渴望、专注侵入性思维、热恋脑区激活——后二者为机制 proxy）
- **common_proxies**: “恋爱脑”“上头”“小鹿乱撞”“眼里只有TA”“想TA想到失眠”
- **overlaps_with**: Sexual desire、infatuation、passionate love、attachment
- **keep_separate_because**: 热恋（infatuation/passionate）时程短暂、下降快、伴随理想化与侵入性思维；而性欲不必然上升/下降同步；浪漫爱可独立于性欲存在（asexual romantic；老年浪漫）；且与稳定依恋安全可分阶段替换（Fisher 三系统模型，C contested）。
- **merge_or_derive**: KEEP（作 PS）；不并入 A01
- **evidence**: E2（热恋有独特性：强理想化、激素变化、时间曲线；但“浪漫爱到底是性欲的子集还是独立系统”存在竞争理论 → C）
- **edge_cases**: 高浪漫低性（无性生活但深恋）；高性低浪漫（FWB/纯性伴）；热恋与安全依恋同现（健康热恋）与分离（狂恋+极低安全感）。
- **assumption_stress_test**: 对 non-kin 稳定；对 kin 通常不适用（→ role/kin 约束抑制）；same-sex/opposite-sex 语义一致。也注意“浪漫吸引”可在陌生人间为一见钟情、在 established 中转为“重燃”——不是同一个值。

#### A03 — Liking / positive affective regard（喜欢/正向评价暖感）
- **layer**: PS / D（有向）
- **definition**: 对对象产生的积极评价 + 亲近温暖倾向，不含（或不含强烈）唤起/性/浪漫幻想。
- **observable_or_latent**: latent（自我报告/行为亲近）
- **common_proxies**: “对他有好感”“聊得来”“人不错”“合得来”
- **overlaps_with**: warmth、trust、affiliative motivation、romantic (低度端)
- **keep_separate_because**: 喜欢（affective positive regard）≠ 爱/浪漫/性欲/依恋；“我喜欢你但我们不想谈恋爱”是常见现实；婚姻里可“不爱不婚却互相善待”（虽是约束维持，仍区别于爱）。低唤起的正向评价与高唤起的爱可独立变化。
- **merge_or_derive**: KEEP（作 PS，注意它与 A02/E01 的边界）
- **evidence**: E1（liking 与 loving 的测量区分由来已久；Rubin 1970 喜欢—爱量表区分）；E2（dispositional warmth）
- **edge_cases**: 高喜欢低浪漫低性（密友/同事/挚友）；高浪漫高性低“喜欢”（征服欲/性吸引强但人格上不喜欢）。
- **assumption_stress_test**: 对所有形态稳定；kin 之间的喜欢（亲情喜欢）与朋友的喜欢模式同构但对象不同——保守处理为同一 valence 状态作用于不同约束。

#### A04 — Reward valuation / incentive salience / reward prediction error
- **layer**: ME（神经/动机机制）
- **definition**: 对象的奖赏价值编码与激励显著性；奖赏预测误差驱动更新。
- **observable_or_latent**: mechanism（可用多巴胺/RPE 代理，但为机制）
- **common_proxies**: “有瘾”“上头”“上瘾式想念”
- **overlaps_with**: A01/A02（它们消费它）；novelty
- **keep_separate_because**: 它解释“为什么”“喜欢”会如此强烈、为何会成瘾式执着，但不能替代关系状态本身（知道 RPE 不告诉你“到底是性欲还是浪漫还是依赖”）。
- **merge_or_derive**: MECHANISM（留 mechanism 层）
- **evidence**: E2（奖励处理与初热恋、成瘾类比存在；但“恋爱成瘾”是否为独立临床构念 contested）
- **edge_cases**: 背景：奖励贬值（失去兴趣）与奖赏循环升（越追越上头）。
- **assumption_stress_test**: 与关系形态无关的通用机制；不参与六形态判断。

#### A05 — Sexual orientation / preference（性向偏好）
- **layer**: RC / Agent 属性（S）
- **definition**: 个体对性吸引目标性别/性征的稳定偏好模式（自我标识/唤起模式），是属性不是状态。
- **observable_or_latent**: latent（自我报告 + 唤起模式 + 行为）但个体内部基本稳定
- **common_proxies**: “取向”“同性恋/异性恋/双性恋/泛性恋/无性恋”
- **overlaps_with**: SEXUAL DESIRE (A01)、romantic orientation、identity、kin
- **keep_separate_because**: 性行为 ≠ 性吸引 ≠ 性取向 ≠ 性认同（已确立的四分）；把“和同性睡了”直接推断为“同性恋”是错误的；取向是入口参数，不是状态变量，也不随时间转移（慢）。
- **merge_or_derive**: KEEP 作为 Agent 属性/约束（不作为 D 层状态）
- **evidence**: E1（behavior/attraction/orientation/identity 四者关系的流行病学证据）
- **edge_cases**: 泛性恋、无性恋、fluid（少数人非固定）；行为与认同错位（深柜/阶段探索）。
- **assumption_stress_test**: 必须显式存在于模型，否则默认异性恋假设复活。

#### A06 — Sociosexuality（短择取向）/ intimacy motivation
- **layer**: RC/DV（Agent 属性为主）
- **definition**: 个体对无承诺性关系的接受度（SOI/SOI-R）。
- **observable_or_latent**: latent agent 属性（问卷）
- **common_proxies**: “玩得开”“随便”“约炮”“性观念开放”
- **overlaps_with**: 性欲热度、attachment avoidance、casual sex 行为
- **keep_separate_because**: SOI 预测短择行为但不是关系状态；常与回避依恋弱相关，不能混。
- **merge_or_derive**: OBSERVATION_ONLY→DERIVED（agent 属性，可作调节变量）
- **evidence**: E1（SOI-R 结构；跨文化有效，但性别/文化均值差异 contested）
- **edge_cases**: 高 SOI 单婚/低 SOI 现象存在（态度与行为解耦）。
- **assumption_stress_test**: 与形态无关的属性；但负极对“性契约”的理解不同时会产生不同 role。

### 4.B 依恋 / 关怀 / 纽带

#### B01 — Attachment security toward partner（对伴侣的依恋安全）
- **layer**: PS / D（有向；表征对该边上的安全基底）
- **definition**: 在该对象在场/可及时，个体体验到的情绪安全（safe haven + secure base）：需要时敢接近、敢依赖、敢表达脆弱；在威胁下对象能否接住。
- **observable_or_latent**: latent（问卷/行为：分离反应、求助行为）
- **common_proxies**: “有他在我就安心”“像家一样”“底气很足”“被托底”
- **overlaps_with**: 安全依恋(trait)、B02 felt security、Trust、Cohesion(B05)、caregiving
- **keep_separate_because**: 这是“关系依赖中是否安全”的状态，与“是否信任对方可靠/善意”有重叠但可解耦：高安全低信任（安全但对方人品存疑——少见但可能：情绪安全来自习惯而非对善意的评估）vs 高信任低安全（信任能力但不觉得被托底/不安全感强）。依恋系统是独立行为系统。
- **merge_or_derive**: KEEP（作 PS；global 焦虑/回避是 agent 属性，见 B03 —— 边安全是该属性 × 特定对象互动的状态化结果）
- **evidence**: E1（依恋对亲密关系满意度的稳定预测；ECR 两维；object-specific 工作模型）
- **edge_cases**: 高安全+关系被背叛后仍低戒备（“好了伤疤忘了疼”）；低安全+长期忠诚（强迫性回避与真实低安全）。
- **assumption_stress_test**: kin/established/same-sex 都稳定；stranger 下“无依恋对象”→状态未形成（unknown），non-kin vs kin 共享该状态。

#### B02 — Felt security / safe-haven & secure-base 体验
- **layer**: PS（并入 B01）或 OB
- **definition**: 即时主观“被托底”体验。
- **observable_or_latent**: latent，主观感应即时变化
- **common_proxies**: “踏实”“安心”“不慌了”“被他稳住”
- **overlaps_with**: B01、D06（安全感代偿）、trust
- **keep_separate_because**: 它是 B01 的主观侧（状态），也可作为 B01 的代理。不单独设 primitive。
- **merge_or_derive**: MERGE into B01（作为 B01 的主观读出口）
- **evidence**: E1
- **edge_cases**: 高 B01 但此刻不安（短时威胁未解除）——即时状态 vs 稳定状态两级。
- **assumption_stress_test**: 同 B01。

#### B03 — Attachment anxiety / avoidance（依恋焦虑/回避维，global trait）
- **layer**: OB / Agent 属性（S）
- **definition**: 个体对“被抛弃/被拒绝”的卷入焦虑，与对亲密/依赖的回避倾向；一般反映早期照料经历形成的系统倾向。
- **observable_or_latent**: latent agent 属性（ECR）
- **common_proxies**: “患得患失”“不敢投入”“作”“需要确认爱”
- **overlaps_with**: B01（但它是属性，B01 是状态）、A02（热恋增强焦虑）、F08 积极错觉
- **keep_separate_because**: 作为 agent 属性（慢变量/先验）预测 B01 状态如何被更新；区分“个体倾向于如何依恋”与“当前对这个人是否安全”。合并会把个体恒定倾向与关系状态混在一起。
- **merge_or_derive**: OBSERVATION_ONLY(agent 属性)
- **evidence**: E1（ECR 两维结构稳定；影响婚姻质量）
- **edge_cases**: 高焦虑但在安全型对象身上安全（安全对象能降焦虑）；高回避但在自己选定的长期关系中趋近安全——属性 ≠ 状态。
- **assumption_stress_test**: 与形态无关的属性。

#### B04 — Caregiving / 关怀照护
- **layer**: PS / D（有向）
- **definition**: 当伴侣处于需求/脆弱时，个体提供可感知的照料行为的动机与胜任（含 no-response 与过度介入两端失败）。
- **observable_or_latent**: latent（行为可观测部分）+ 胜任度
- **common_proxies**: “会照顾人”“体贴”“他生病时他忙前忙后”“被呵护”
- **overlaps_with**: B01、PPR(C04)、investment、role 义务
- **keep_separate_because**: 关怀是独立行为系统（依恋理论第四系统）；它 ≠ trust/爱，也不等同投入（被义务/角色驱动也算关怀）。高关怀低浪漫（父母照料、护士型伴侣）、高浪漫低关怀（热恋但不会照顾），可解耦。
- **merge_or_derive**: KEEP（作 PS）——但注意勿与 PPR 混淆：PPR 是“对方是否回应我的需求”（接收方状态），关怀是发送方胜任。
- **evidence**: E2（依恋四大系统的关怀系统；Feeney & Collins 后续研究）
- **edge_cases**: 关怀边：被照顾者体验不到（好心办坏事）；过度关怀=侵入/溺爱（反正确性）。
- **assumption_stress_test**: 所有形态稳定（亲属、朋友、伴侣、caregiving 角色）。

#### B05 — Affiliative bond / cohesion / we-ness（情感凝聚/我们感）
- **layer**: PS / D（pair+有向混合：有“我觉得我们很近”的方向主观，也有“关系本身的凝聚度”pair 属性）
- **definition**: 双方作为共同单元的认同凝聚：投入归属感、共同经历形成的“我们”感、互相把对方纳入自我（inclusion of other in self）。
- **observable_or_latent**: latent（IoS 量表、we-mentions、closeness）
- **common_proxies**: “我们两个”“形成了一个整体”“灵魂伴侣”“共同体”
- **overlaps_with**: B01 依恋安全、C06 intimacy、C07 closeness、C08 commitment、kinship/团队认同
- **keep_separate_because**: 一群高安全高亲密的人若不产生“我们是共同体”的认同，仍是独立个体；we-ness 是关系的“身份对象化”层，接近“relationship identity/commitment to the relationship as an entity”，而非单纯安全或喜欢。（注：we-ness 与 commitment 相关高，模型要防共线）
- **merge_or_derive**: KEEP（作 PS，注意与 C08 去耦）
- **evidence**: E2（we-ness/communal thinking 预测关系维持；与 commitment 强关联——GRE 研究）
- **edge_cases**: 高 we-ness 低 commitment（习惯性共同生活但随时可分）；低 we-ness 高 commitment（责任/契约维持、异地各自独立）。
- **assumption_stress_test**: 所有 non-kin/kin 形态稳定（亲子也可产生“我们感”）；stranger 下未形成。

#### B06 — Pair-bond（配对纽带，romantic 语境）
- **layer**: DV / RC（在浪漫/配偶语境下，依恋+排他+共同繁殖管理义务的复合）
- **definition**: 维持成对、通常伴随排他与共同后代/资源纽带的社会结构。
- **observable_or_latent**: derived
- **common_proxies**: “结成夫妻”“认定一生”“一对儿”“拴住”
- **overlaps_with**: B01+B05+AAA(commitment)；roule 排他；文化规范
- **keep_separate_because**: 它是“依恋安全+凝聚+排他约定+繁殖/资源义务”通过 role 与制度固定下来的组合态，不是单一状态。
- **merge_or_derive**: DERIVED（顶层人类认可的总称，可作 DERIVED/RATING）
- **evidence**: E1（跨文化/跨物种的成对维持现象；但“爱情=配对纽带”被过度泛化 → C）
- **edge_cases**: 同居不婚也有 pair-bond；包办婚姻低情感高 bond-schema；开放关系把排他拆掉后 pair-bond 语义需重定义。
- **assumption_stress_test**: kin 不明；stranger 无；established 同。

#### B07 — Social proximity / touch（社会距离/身体亲近）
- **layer**: OB
- **definition**: 可观测的空间/身体亲近度与触摸频率。
- **observable_or_latent**: observable
- **common_proxies**: “感情好就黏在一起”“身体接触”
- **overlaps_with**: cohesion、comfort (依恋) 、性亲密
- **keep_separate_because**: 它是 B01/B05 的观测代理，也是调节变量；单独作为 primitive 会把“行为显示”与“状态”混淆。
- **merge_or_derive**: OBSERVATION_ONLY（代理 B01/B05；勿作双向唯一指征）
- **evidence**: E2（触摸/靠近与情绪安全的关系；touch deprivation 等）
- **edge_cases**: 远距离恋爱高 bond 低接触；宗教/文化约束低触摸但高 bond。
- **assumption_stress_test**: 跨形态只是“表现形式随角色改变”，隐含状态相同。

#### B08 — Loneliness / need for relationship（孤独/关系需求）
- **layer**: DV（agent-S 状态）
- **definition**: 客观社会联结 vs 期望联结的缺口产生的主观感。
- **observable_or_latent**: latent
- **common_proxies**: “孤独”“想找人陪”“空窗期”“寂寞”
- **overlaps_with**: attachment anxiety、satisfaction
- **keep_separate_because**: 是 S 层状态（驱动 seeking），不是 dyad 状态；建模需性与 D 层结果区分。
- **merge_or_derive**: DERIVED（agent 需求缺口）
- **evidence**: E1（孤独流行病学；Loneliness 量表）
- **edge_cases**: 亲密关系中的孤独（“婚内单身感”）—— 高关系存量但低联结，说明孤独≠无关系。
- **assumption_stress_test**: 与形态无关的 S 状态。

---

### 4.C 互依 / 认知 / 承诺

#### C01 — Trust / 信任
- **layer**: PS / D（有向，Alix→Bob）
- **definition**: 在涉及风险/脆弱性时，一方概括性地预期对方会良性、可靠地行动（善意+能力+负责），并据此愿意让自己处于可被对方辜负的位置。
- **observable_or_latent**: latent（自我报告；行为风险承担 如依赖、托付、贷款担保 可观测）
- **common_proxies**: “信得过”“靠谱”“敢放心交出去”“不担心被坑”“掏心掏肺”
- **overlaps_with**: security(B01)、faith(dependability 分面)、reliance、predictability、credibility、commitment
- **keep_separate_because**: 信任 = 期望 + 结构性依靠意愿（愿意承担被辜负的风险）；安全感偏情绪/依恋面；可靠预期可在无风险时存在（“知道他靠谱”但未必托付），托付不一定来自善意信任（被绑定的制度信任）。Trust 是独立、可去耦、可建模状态。
- **merge_or_derive**: KEEP（作 PS）
- **evidence**: E1（信任结构——诚信/善意/可预期/信仰 多面；信任与关系满意显著正相关但不等于满意）
- **edge_cases**: 高信任低安全（信任对方能力却惴惴不安——依恋焦虑者）；低信任高安全（安全但知对方不可靠——如对酒鬼共生伴侣）；业务信任 vs 亲密信任差异。
- **assumption_stress_test**: 所有形态稳定；kin/非kin/亲友/商业高度通用。注意与文化差异（人际关系信任 vs 制度信任）分离。

#### C02 — Distrust（不信任）
- **layer**: PS / D（有向）
- **definition**: 主动预期对方会背叛/伤害/失守，且这种预期区别于“缺乏信任”（低信任≠高不信任；是趋避/回避的主动预期）。
- **observable_or_latent**: latent（出卖预期、隐瞒、帐户监控行为）
- **common_proxies**: “防着他”“总觉得会背叛”“疑神疑鬼”“翻手机”
- **overlaps_with**: jealousy、betrayal history、anxiety
- **keep_separate_because**: 信任与不信任并非单一双极（实证争议，但语义上：中性未知状态 ≠ 积极不信任）。不信任驱动监控行为、检验行为，甚至自我实现，值得独立节点。
- **merge_or_derive**: KEEP（作 PS，与 trust 分离，相关性高但方向不同）
- **evidence**: E2（trust–distrust 并非单纯反相；Lewicki 双元观点 contested）
- **edge_cases**: 已背叛却仍浪漫依恋（高 bond 高 distrust——“明知道他花心却离不开”）；无背叛但对陌生人普遍不信任（agent trait，非边状态）。
- **assumption_stress_test**: 跨形态稳定。

#### C03 — Predictability / 可预测性
- **layer**: OB（trust 的分面）
- **definition**: 能预测对方行为的确定性（基于历史，不含价值判断“好不好”）。
- **observable_or_latent**: observable（行为一致性）
- **common_proxies**: “能算到他”“他什么时候生气我摸得清”“习惯成自然”
- **overlaps_with**: trust、familiarity、habituation
- **keep_separate_because**: 可预测可不善（驯服、规律但不能信任或依赖）；应作为 trust 的低阶成分（机制/分面）而非独立 primitive。
- **merge_or_derive**: MERGE into C01（trust 的分面）
- **evidence**: E1（trust 的行为学测量里可预测性常作为成分）
- **edge_cases**: 可预测的虐待（规律性家暴却不可托付）。
- **assumption_stress_test**: 跨形态稳定。

#### C04 — Perceived partner responsiveness (PPR) / 感知被回馈
- **layer**: PS / D（有向：Alix 感知 Bob 是否理解、认可、关心）
- **definition**: 一方感知到对方“理解我、认可我、在乎我”的程度，特别是在我披露后。
- **observable_or_latent**: latent（主观感知；可由披露→被理解行为部分代理）
- **common_proxies**: “被理解”“被接住”“我的情绪他接得住”“懂我”“共情”
- **overlaps_with**: intimacy(C05)、caregiving(B04)、validation、support 感知、attunement
- **keep_separate_because**: PPR 是“接收方的主观感知”，caregiving 是“发送方行为”。二者方向相反且可大面积解耦：对方真心关心却不会表达（高关怀低PPR）；对方熟练共情但无真心（高PPR低关怀，并可能用于操纵）。PPR 是亲密与信任的动态生成器，值得独立状态。
- **merge_or_derive**: KEEP（作 PS）
- **evidence**: E1（Reis & Shaver 亲密过程模型；PPR 预测身心健康、亲密、信任；大量实验室+纵向）
- **edge_cases**: 高 PPR 低真实关怀（专业共情人/操纵者）；真实关心但方式错误导致低 PPR；文化差异（含蓄文化表达少→PPR 低但不代表关怀低）。
- **assumption_stress_test**: 跨形态稳定（亲子、朋友、伴侣）。

#### C05 — Intimacy / 亲密
- **layer**: DV（由 PPR+披露 累积的产生物）
- **definition**: 深层、相互知晓并感到被理解/被认同的联结体验（过程结果而非单一时点状态）。
- **observable_or_latent**: latent（主观+对话深度）
- **common_proxies**: “亲密无间”“无话不谈”“灵魂深处”“心贴得很近”
- **overlaps_with**: PPR(C04)、self-disclosure、closeness、cohesion(B05)
- **keep_separate_because**: 亲密≈“披露×应时而至的响应”交互的累积结果；它是 derived，不单独当 primitive。若强行 primitive，会与 PPR 和 closeness 双重共线。
- **merge_or_derive**: DERIVED（可由 C04/disclosure 推导；若保留则作为 dyad 时间积分）
- **evidence**: E1
- **edge_cases**: 高亲密低浪漫（知己、挚友）；高浪漫低亲密（只爱表面、不进入深层）。
- **assumption_stress_test**: 跨形态稳定。

#### C06 — Self-disclosure / 自我披露
- **layer**: OB（行为）
- **definition**: 向对方提供自己真实、私密、脆弱信息的沟通行为。
- **observable_or_latent**: observable（对话记录/自我报告深度与广度）
- **common_proxies**: “什么都跟他说”“藏不住话”“交底”“敞开心扉”
- **overlaps_with**: PPR、intimacy、vulnerability
- **keep_separate_because**: 披露是行为输入，被 PPR 响应后产生亲密；行为≠状态。单独作为 primitive 会把“行为发生”当作“联结形成”。
- **merge_or_derive**: OBSERVATION_ONLY（可作事件输入调 PPR/intimacy）
- **evidence**: E1
- **edge_cases**: 高披露低亲密（对方不回应/利用；持续单方面倒苦水）；低披露高亲密（多年默契无需多言）。
- **assumption_stress_test**: 跨形态稳定（陌生人初识除外——披露是建立期事件）。

#### C07 — Closeness / 心理接近（we-ness 另一侧）
- **layer**: DV / pair（IoS）
- **definition**: 对双方心理重叠程度的总体主观（“你中有我”）。
- **observable_or_latent**: latent（IoS 量表；可作 B05 的主观读数）
- **common_proxies**: “像一个人”“不分彼此”“默契”“先说后想”
- **overlaps_with**: B05 we-ness、C05 intimacy、cohesion
- **keep_separate_because**: closeness 是 B05 的经验/主观侧，它的认知底物是自我—他人重叠。可并入 B05 状态；不单独 primitive。
- **merge_or_derive**: MERGE into B05（或作为 B05 的观测指标）
- **evidence**: E2
- **edge_cases**: 高 closeness 功能差（过于融合/共生失独立）；低 closeness 但配合良好（专业队友感）。
- **assumption_stress_test**: 跨形态稳定。

#### C08 — Commitment (dedication) / 承诺（投入意愿）
- **layer**: PS / D（有向或 pair）
- **definition**: 主观地打算长期维持这段关系的意愿、依附与义务感（dedication），区别于被结构绑住的 constraint。
- **observable_or_latent**: latent（量表；行为：计划、未来叙事、为关系牺牲）
- **common_proxies**: “认定TA”“想一直走下去”“余生”“白头偕老”“结为伴侣”
- **overlaps_with**: investment、alternative quality、satisfaction、love、obligation、pair-bond
- **keep_separate_because**: 经典分解 commitment ≈ satisfaction − alternatives + investments；这三者是输入，commitment 是输出；如果 commitment=derived，则建模失去其独立波动（dedication 可在结构不利时仍高、在条件极佳时仍掉头）。dedication 与 constraint 需要分开，否则“想逃却离不开”无法表达。
- **merge_or_derive**: KEEP（作 PS，定义为 dedication）；constraint 单独见 C09
- **evidence**: E1（投资模型 meta：承诺=满意−替代+投入，结构清晰；dedication vs constraint 两分有实证但二者交互 contested）
- **edge_cases**: 高承诺低满意（责任、孩子、面子——dedication 仍在，靠义务/身份驱动）；高满意低承诺（无惧替代、不愿绑定）。承诺的“感觉”与“契约”双重来源→分别跟踪。
- **assumption_stress_test**: 跨形态稳定（朋友承诺、伴侣承诺、合作承诺同构）。

#### C09 — Constraint commitment / 结构性承诺
- **layer**: DV / RC（结构态）
- **definition**: 脱离关系的成本与约束（投入沉没、替代稀缺、社会/物质/义务绑定）产生的事实性“离不开”，表观为不会离开但不必然想留。
- **observable_or_latent**: latent（退出成本代理）
- **common_proxies**: “离不开”“将就”“凑合过”“离婚影响大”“为孩子坚持”
- **overlaps_with**: C13 dependence、investment、C08、power
- **keep_separate_because**: “想留”与“必须留/懒得走”是两回事；合并则无法表达“被绑住的关系”，这是压测的关键情形。
- **merge_or_derive**: DERIVED（由 C13 依赖 + 投资 + 退出成本 综合得；不单独 primitive）
- **evidence**: E2（constraint 承诺单独测量）
- **edge_cases**: 高 constraint 低 dedication（困在关系里）；高 dedication 零 constraint（自愿却可随时离开——异地恋人）。
- **assumption_stress_test**: 跨形态稳定；kin 不适用（无法解除关系）。

#### C10 — Investment / 投入
- **layer**: OB（时间/资源/情感/沉没）
- **definition**: 投入这段关系的资源总和（时间、金钱、共同财产、孩子、情感、社会网络）。
- **observable_or_latent**: observable（partly）
- **common_proxies**: “付出了太多”“八九年的青春”“共同房子/公司/孩子”“一直陪伴”
- **overlaps_with**: C08/C09、resource commitment、sunk cost、D06
- **keep_separate_because**: 投入是 commitment predictor/输入，也是 constraint 来源；把它当 commitment 本体会导致“投入=爱”的循环常识错误。
- **merge_or_derive**: OBSERVATION_ONLY（预测变量/成本源）
- **evidence**: E1（投资模型）
- **edge_cases**: 高投入低向往（沉没但想逃）；低投入高向往（火花强却无共同资源）。
- **assumption_stress_test**: 跨形态稳定。

#### C11 — Alternative quality / 替代质量（CL-alt）
- **layer**: OB / E（环境+感知）
- **definition**: 对“离开后可能的选择”的品质评估（包括独身、其他对象、自由）。
- **observable_or_latent**: latent（替代评估）
- **common_proxies**: “外面更好的多”“单身也自在”“骑驴找马”“备胎”“没TA不行”
- **overlaps_with**: dependence(C13)、constraint、satisfaction、market
- **keep_separate_because**: 决定依赖与权力不对称；不是关系属性而是感知替代品评估，必须独立，否则权力解释缺失。
- **merge_or_derive**: OBSERVATION_ONLY（感知替代）
- **evidence**: E1（互依理论；CL-alt）
- **edge_cases**: 高替代仍高 commitment（价值观绑定/文化禁止）；低替代却低 commitment（自由选择不绑定）。
- **assumption_stress_test**: 跨形态稳定。

#### C12 — Satisfaction (outcome − CL) / 满意
- **layer**: DV
- **definition**: 关系提供的结果减去期望基线(CL)的正负体验。
- **observable_or_latent**: latent（量表）
- **common_proxies**: “跟他在一起很开心”“日子很顺”“幸福感”
- **overlaps_with**: C08、love、quality、cohesion
- **keep_separate_because**: 满意是输出（derived），也是 commitment 的输入；会把“在一起很爽”与“想维持关系”区分（高满意低承诺存在）。
- **merge_or_derive**: DERIVED（作 DV/中间状态）
- **evidence**: E1
- **edge_cases**: 高满意仍要离（外围环境压力）；低满意却不离（沉没）。
- **assumption_stress_test**: 跨形态稳定（朋友、伴侣、同事）。

#### C13 — Outcome dependence / 结果依赖
- **layer**: PS / D（结构态，可非对称）
- **definition**: 一方从该关系获得关键结果的依赖程度（好结局多大程度离不开这段关系）——互依理论的核心结构变量。
- **observable_or_latent**: latent（结果—替代评估，可部分可观测）
- **common_proxies**: “离不开TA”“没TA不行”“TA是我的全部意义”“依附”
- **overlaps_with**: C08/C09、power、need、alternative、attachment
- **keep_separate_because**: 依赖是结构（不一定“感觉”到），权力=依赖的不对称；它生成约束承诺与权力博弈。它 ≠ security（高依附焦虑者常高依赖，但依赖本身中性）。可与 commitment 解耦（高依赖低 dedication 典型困境）。
- **merge_or_derive**: KEEP（作 PS）
- **evidence**: E1（互依理论；Kelley；Rusbult 体系）
- **edge_cases**: 高依赖到窒息仍低 commitment（“不离开是因为没能力离开”）；低依赖高 commitment（两个可独活的成人选择在一起）。
- **assumption_stress_test**: 跨形态稳定；kin 几乎强制高依赖结构（家庭绑定）。

#### C14 — Power（asymmetric dependence）/ 权力
- **layer**: DV / RC（结构态，非体验）
- **definition**: 一方对另一方的依赖不对称→前者对后者拥有的对关系结果的控制能力。
- **observable_or_latent**: latent（由依赖差导出；可观测决策权）
- **common_proxies**: “谁说了算”“谁怕失去谁”“一家之主”“低位”
- **overlaps_with**: C13、dominance(Personality)、control、autonomy
- **keep_separate_because**: 权力可从依赖不对称直接导出，不需另设 emotion。但控制/支配（个人倾向）与结构性权力应区分。
- **merge_or_derive**: DERIVED（= C13 不对称；control/dominance 另列）
- **evidence**: E1
- **edge_cases**: 高权力低支配欲（平等但有结构优势）；低权力高发怒（弱者虚张声势）。
- **assumption_stress_test**: 结构性，跨形态稳定。

#### C15 — Gratitude / resentment（情感账本）
- **layer**: DV（累积状态）
- **definition**: 累积的感激或怨气的净留存（互动特质的记忆加权）。
- **observable_or_latent**: latent（汇报+行为）
- **common_proxies**: “记仇”“翻旧账”“一直念着TA的好”“寒心”
- **overlaps_with**: forgiveness、conflict、satisfaction
- **keep_separate_because**: 作为中间状态它解释修复与爆发；但它是 derived（由事件积分）。若建模“sentiment override/情感账户”需显式状态，但不算 new primitive。
- **merge_or_derive**: DERIVED（但可作模型存储的中间状态）
- **evidence**: E2（感恩/憎怨文献）
- **edge_cases**: 感恩高却离开（恩情≠愿意继续付出）；怨气高却不离。
- **assumption_stress_test**: 跨形态稳定。

### 4.D 兼容性 / 配对

#### D01 — Similarity（actual & perceived）/ 相似性
- **layer**: OB / pair 属性（两者属性距离）
- **definition**: 双方在某些属性（人格、价值观、兴趣、背景）上的实际或感知接近度。
- **observable_or_latent**: observable（测评匹配）与 perceived（主观）并存
- **common_proxies**: “像”“聊得来”“同类”“志趣相投”“门当户对”
- **overlaps_with**: value congruence(D02)、complementarity、alignment、homophily、assortative mating
- **keep_separate_because**: 它是“属性距离”不是“关系状态”——不随时间随机更新，也不能驱动转移（它静态预测匹配/吸引）。实际相似对吸引效应 meta 偏弱，感知相似效应更强。
- **merge_or_derive**: OBSERVATION_ONLY（用于匹配/偏好层；不是 D 状态）
- **evidence**: E1（相似吸引 meta 较小但稳定；感知相似 vs 实际相似分离）
- **edge_cases**: 高相似低和谐（两个都强势/都回避）；高互补低相似（配合好）。
- **assumption_stress_test**: 跨形态稳定（属性而非状态）。

#### D02 — Value congruence / 价值观一致
- **layer**: PS(latent) / pair（D02-D03 是少数有“pair 状态”意味的构念，但更接近“量度”）
- **definition**: 双方在重要价值观（婚姻、家庭、金钱、育儿、宗教、道德、生活方式）上的对齐程度。
- **observable_or_latent**: latent（测评/协商）
- **common_proxies**: “三观合”“三观不合”“根本说不到一块”
- **overlaps_with**: D01（值域重叠）、D03、理想匹配、冲突来源
- **keep_separate_because**: 价值观一致是长期满意/冲突的核心解释（> 一般兴趣相似），其对象是“评价/规范”，与 trait-similarity 不同（两个都内向≠三观一致）。可建模为 pair 的 alignment 分量。
- **merge_or_derive**: KEEP(潜)（作为 pair 的 alignment 的一支；不独立作状态也可→或并入 D03 alignment）
- **evidence**: E1（价值观一致温和预测满意；关系依恋调节）
- **edge_cases**: 高一致仍离（外部压力/激情崩解）；低一致却高 bond（避碰/互补分工）。
- **assumption_stress_test**: 跨形态稳定。

#### D03 — Goal alignment / 目标同向
- **layer**: PS(latent) / pair（含未来计划重叠）
- **definition**: 双方对未来的共同目标方向、手段与优先级的一致程度（包含 buy-in、协作）。
- **observable_or_latent**: latent（规划评估）
- **common_proxies**: “奔着同一个方向”“想一起过的未来不一样”“目标不同”
- **overlaps_with**: D02、complementarity、coordination
- **keep_separate_because**: 目标一致性涉及“未来合作可行性”，与静态价值观相似不同（价值观一致但目标冲突——都要事业但不同城市；目标同向但价值观有差——一起赚钱但方法不同）。关系到 co-planning 与资源分配冲突。
- **merge_or_derive**: KEEP(潜)（alignment 的主力）
- **evidence**: E2
- **edge_cases**: 高目标一致低日常同频（大事却没法小处合）；目标看似同向却为一个手段冲突。
- **assumption_stress_test**: 跨形态稳定（朋友一起创业、伴侣成家、亲子规划）。

#### D04 — Complementarity / 互补
- **layer**: DV / pair（功能匹配）
- **definition**: 双方技能/资源/性格在任务上的互补带来的功能适配。
- **observable_or_latent**: observable（技能评估）
- **common_proxies**: “互补”“搭”“一攻一受”“刚柔相济”“黄金搭档”
- **overlaps_with**: D02、匹配、skill synergy
- **keep_separate_because**: 互补是“功能场景下的适配”，并非整体关系状态；高低受影响于任务类型。
- **merge_or_derive**: DERIVED（功能适配，按 role/任务评估）
- **evidence**: E2（适配/互补研究结论较弱且混杂——警示别当作强 primitive）
- **edge_cases**: 同类互补因任务而不同（都擅长赚钱但不会生活）。
- **assumption_stress_test**: 跨形态稳定（同事/伴侣/亲子）。

#### D05 — Ideal standards match / 理想标准匹配
- **layer**: DV（评价层）
- **definition**: 对象与自身理想伴侣标准的匹配程度（评价人对理想画像匹配的评估）。
- **observable_or_latent**: latent（理想标准问卷）
- **common_proxies**: “不是我的菜”“达不到标准”“够不上理想”
- **overlaps_with**: mate value、preference、satisfaction、attraction
- **keep_separate_because**: 是“偏好×客体属性”匹配器，属于评价/过滤层（S×O），不是 dyad 动态状态。
- **merge_or_derive**: DERIVED
- **evidence**: E2（理想标准与满意相关；评估人会更新标准）
- **edge_cases**: 高匹配仍不选（市场/情绪原因）；低匹配却在爱（获得后理想化重组）。
- **assumption_stress_test**: 评价层，非关系状态。

#### D06 — Mate value / desirability / 择偶价值
- **layer**: DV / S,O 属性（评价）
- **definition**: 个体在关系市场中的总体可欲性（外表、资源、地位、健康、性格的加权市场值）。
- **observable_or_latent**: latent（市场/自评/他评 rater）
- **common_proxies**: “高富帅”“白富美”“加分项”“减分项”“条件”
- **overlaps_with**: status、resource、market position、preference
- **keep_separate_because**: 是高阶市场评价（E/DV），不是状态；它影响吸引阈值与替代质量，但本身不提供“关系当前状态”信息。
- **merge_or_derive**: DERIVED
- **evidence**: E2（mate value 构念有争议，测量多元→C）
- **edge_cases**: 高价值却关系久困（选择不受市场支配）；低价值却高回报关系。
- **assumption_stress_test**: 评价层，非状态。

#### D07 — Assortative mating / 类别匹配
- **layer**: DV / E（市场结果）
- **definition**: 现实配对在属性上的正相关程度（教育、阶级、宗教、年龄、外表）。
- **observable_or_latent**: DERIVED（宏观统计）
- **common_proxies**: “一般配”“圈子不同”“高攀”
- **overlaps_with**: D01、market、role
- **keep_separate_because**: 是宏观现象统计，不是个体/关系状态。
- **merge_or_derive**: DERIVED
- **evidence**: E1（在教育和年龄上分类配强）
- **edge_cases**: 异质配对也存在（跨阶级能结婚，只是概率低）→不设硬规则。
- **assumption_stress_test**: 统计层。

#### D08 — Perceived compatibility / “般配感”
- **layer**: DV（评价）
- **definition**: 对“我们是否合适”的整体主观碾压感（通常是 D01-D04 的加权估计）。
- **observable_or_latent**: latent（量表）
- **common_proxies**: “般配”“不合适”“磨合不了”“命中注定”
- **overlaps_with**: D05、D02/D03、satisfaction、commitment
- **keep_separate_because**: 是全局评价，重复计数风险高；作为 DV 可保留给 UI，不作为 primitive。
- **merge_or_derive**: DERIVED
- **evidence**: E2
- **edge_cases**: 前期般配感高后期崩（动态）；环境压力下的“被般配”（包办）。
- **assumption_stress_test**: 评价层。

### 4.E 交互 / 调节

#### E01 — Reciprocity / 互惠
- **layer**: DV（事件账）
- **definition**: 给予与回报的即时/延迟对称结构（行为模式）。
- **observable_or_latent**: observable（给予-回报序列）
- **common_proxies**: “礼尚往来”“有来有往”“单方面付出”“人心换人心”
- **overlaps_with**: exchange、fairness、gratitude、cooperation
- **keep_separate_because**: 是交换结构（互依的一部分），描述事件流属性；不单独作为关系状态，但影响 trust/commitment。
- **merge_or_derive**: DERIVED（事件统计）
- **evidence**: E1（互惠规范跨文化）
- **edge_cases**: 慷慨却不互惠（单相思付出）；激烈互惠却是毁灭性对耗（互相报复式对等）。
- **assumption_stress_test**: 跨形态稳定（家庭互助、合作、恋人）

#### E02 — Cooperation / 协作
- **layer**: OB（行为）
- **definition**: 在共同任务中协调努力以产生联合结果的行为。
- **observable_or_latent**: observable
- **common_proxies**: “互相帮忙”“合作愉快”“我们并肩作战”
- **overlaps_with**: coordination、reciprocity、alignment
- **keep_separate_because**: 协作是行为表现，可被 commitment/goal alignment 解释；单独 primitive 会把“做了什么”当状态。
- **merge_or_derive**: OBSERVATION_ONLY
- **evidence**: E1
- **edge_cases**: 叛徒式协作（表面协作实际背叛）；拒绝协作但关系好（家务分工分离）。
- **assumption_stress_test**: 跨形态稳定。

#### E03 — Coordination / synchrony（行为协调/同步）
- **layer**: OB / prospective（有时序性）
- **definition**: 双方行为/情绪/生理节奏的时间耦合与协调效率。
- **observable_or_latent**: observable（对话打断、行走同步、生理耦合）
- **common_proxies**: “默契”“搭得上节奏”“同频”
- **overlaps_with**: rapport、attunement、C04 PPR、turn-taking
- **keep_separate_because**: 是近距离互动的代理/机制信号（含自动同步），可预测好感；不是关系状态本身（陌生人也能暂时同步）。
- **merge_or_derive**: OBSERVATION_ONLY
- **evidence**: E2（同步研究稳健但因果性 contested）
- **edge_cases**: 高同步却敌对（互相较劲的舞蹈/嘴架）；低同步却亲密（内向搭档慢慢来）。
- **assumption_stress_test**: 跨形态稳定。

#### E04 — Conflict / 冲突
- **layer**: OB（事件/状态段）
- **definition**: 目标/期望冲突刺激下双方（或单方）的对抗互动事件或持续性对抗状态。
- **observable_or_latent**: observable（事件记录、量表）
- **common_proxies**: “吵架”“冷战”“闹矛盾”“翻脸”
- **overlaps_with**: repair、satisfaction、power struggle
- **keep_separate_because**: 冲突是事件（会触发状态转移），需与长期rumination/怨恨区分；冲突频次≠强度≠有害性（建设性冲突有增益）。
- **merge_or_derive**: OBSERVATION_ONLY（事件）
- **evidence**: E1
- **edge_cases**: 零冲突却崩解（回避问题型）；高冲突却稳定（热络吵架的稳定伴侣）。
- **assumption_stress_test**: 跨形态稳定。

#### E05 — Repair / reconciliation / 修复和解
- **layer**: OB（事件/技能）
- **definition**: 冲突后的弥补、道歉、再联结行为与成功度。
- **observable_or_latent**: observable（行为+主观修复感）
- **common_proxies**: “先低头”“主动求和”“破镜重圆”“冷战结束”
- **overlaps_with**: forgiveness、C15 sentiment、conflict
- **keep_separate_because**: 修复是事件技能，效果体现在恩怨账与信任；可独立测量其频次/成功度。
- **merge_or_derive**: OBSERVATION_ONLY（事件；维护状态可为 DV）
- **evidence**: E2（Gottman repair 概念；修复增益多数研究为间接证据）
- **edge_cases**: 修复成功但仍有再犯（高修复低稳定）；没有冲突却无修复需求（良好型）。
- **assumption_stress_test**: 跨形态稳定。

#### E06 — Forgiveness / 原谅
- **layer**: PS（事件态）/ pair
- **definition**: 在遭受伤害后，对“回到正常交换与亲近”的心理/关系状态（决定不再追责/记仇）。
- **observable_or_latent**: latent（量表+行为）
- **common_proxies**: “原谅”“算了”“翻篇”“放下”
- **overlaps_with**: repair、revenge、trust 恢复、bitterness
- **keep_separate_because**: 原谅是受伤害后对“是否保留关系”的决定性状态，可独立于客观伤害与信任水平。
- **merge_or_derive**: DERIVED（由伤害+修复+信任综合得，也可作 model 状态）
- **evidence**: E2（原谅与关系维持相关）
- **edge_cases**: 原谅却不修复（表面原谅暗伤）；不原谅却留关系（惩罚式维持）。
- **assumption_stress_test**: 跨形态稳定。

#### E07 — Responsiveness behavior / 响应行为
- **layer**: OB
- **definition**: 发送方真正理解/在乎/协助的言行（C04 的客观侧）。
- **observable_or_latent**: observable（编码）
- **common_proxies**: “关键时刻在”“来接我”“帮我出主意”
- **overlaps_with**: C04、caregiving、support
- **keep_separate_because**: 发送行为≠接收感知；两者都需要（C04 是主观，E07 是客观）。
- **merge_or_derive**: OBSERVATION_ONLY
- **evidence**: E1（支持效应的感知模型：感知支持 > 实际支持，几乎全部预测）
- **edge_cases**: 客观支持多但低感知（方式不匹配）；无实际帮助但高感知（象征性在场）。
- **assumption_stress_test**: 跨形态稳定。

#### E08 — Exchange fairness / equity / 公平
- **layer**: DV / E（交换账）
- **definition**: 贡献—所得在两方的公平结构（过度受益/受益不足）。
- **observable_or_latent**: latent（感知公平）
- **common_proxies**: “不公平”“我付出多”“吃亏”“凭什么”
- **overlaps_with**: reciprocity、gratitude、resentment、power
- **keep_separate_because**: 公平感知驱动怨恼与承诺，但它是互依结果（投入/回报），非基础状态。
- **merge_or_derive**: DERIVED
- **evidence**: E2（亲密关系中的公平效应不如泛社会显著——争议）
- **edge_cases**: 客观上公平但感知不公平；愿意承受不公平（补偿性依恋）。
- **assumption_stress_test**: 跨形态稳定。

#### E09 — Co-regulation / 情绪共调
- **layer**: ME→DV
- **definition**: 双方情绪/生理相互调节（缓冲或放大）的动态过程。
- **observable_or_latent**: observed；机制性
- **common_proxies**: “他的情绪带动我”“紧张会传染”
- **overlaps_with**: synchrony、caregiving、PPR
- **keep_separate_because**: 是过程机制；关系模型的产物可见于 PPR/安全/冲突，但共调本身不独立作为 primitive。
- **merge_or_derive**: MECHANISM→DERIVED
- **evidence**: E2（核心调节研究）
- **edge_cases**: 重视它作为 buffering/exhaustion 的路径而非单独变量。
- **assumption_stress_test**: 机制层。

---

### 4.F 威胁 / 排他 / 认知辩护

#### F01 — Jealousy / 嫉妒
- **layer**: DV（由威胁触发）→可作 PS
- **definition**: 因感知到对方情感/性/忠诚可能被第三方(或替代)夺走而产生的情绪-行为反应（疑问、监测、防卫）。
- **observable_or_latent**: latent（事件诱发；嫉妒倾向属性 vs 关系突发事件）
- **common_proxies**: “吃醋”“查岗”“疑心重”“看他/她跟别人说话就难受”
- **overlaps_with**: envy、mate guarding、distrust、anxiety、territoriality
- **keep_separate_because**: 嫉妒是“对威胁信号的响应状态”，与敌意嫉妒(envy)不同，也与防御性不信任不同；可作为模型状态，但要注意它常由 attachment anxiety 与信任/排他规则共同驱动——构造应放在“威胁事件→情绪状态”层。
- **merge_or_derive**: DERIVED（可作触发信号；若作 primitive 则与 C02 distrust 高度共线→建议 DERIVED）
- **evidence**: E1（嫉妒与性别差异/进化解释：Buss 提出差异，Harris contested）；存在文化差异
- **edge_cases**: 嫉妒型伴侣对稳定忠贞对象的无据嫉妒；开放关系中的“边界嫉妒”（吃醋规则不一）。
- **assumption_stress_test**: 跨形态稳定但内容不同（情感出轨 vs 性出轨嫉妒权重依文化/性别）。

#### F02 — Mate guarding / 伴侣守护
- **layer**: RC/DV（进化语境）
- **definition**: 防止伴侣被竞争者染指的行为（时间占用、遥控、贬损、守人）。
- **observable_or_latent**: observable（行为）
- **common_proxies**: “管得紧”“看得很紧”“走到哪都带着”
- **overlaps_with**: jealousy、control、ownership、exclusivity
- **keep_separate_because**: 是进化行为策略；作为单一 primitive 会把“行为策略”与“关系状态”混同；在现今语境多为 role/文化行为。
- **merge_or_derive**: DERIVED→ROLE（行为/约束）
- **evidence**: E2（进化解释有证据但现代社会变异性大→C）
- **edge_cases**: 高守卫零威胁（害怕失去而过度管控）；零守卫高威胁（疏忽放任）。
- **assumption_stress_test**: 跨形态稳定（伴侣独占语境）。

#### F03 — Exclusivity agreement / 排他约定
- **layer**: RC（契约/规则状态）
- **definition**: 双方对边界（性/情感/时间/信息）的约定状态：排他、开放式或其具体形态。
- **observable_or_latent**: latent（约定+遵守）
- **common_proxies**: “一对一的”“开放关系”“边界”“不出轨”“忠诚契约”
- **overlaps_with**: pair-bond、relationship identity、commitment、jealousy
- **keep_separate_because**: 排他不是自然状态而是规则状态（“谁和谁可以”），是可协商、multiform 的约束，必须与信任/爱分离置档。不同违约的意义。
- **merge_or_derive**: KEEP（作 RC 状态）
- **evidence**: E2（关系协议/边界文献较少）
- **edge_cases**: 排他约定但无爱（形式婚姻）；开放关系但爱深。EX 复合后边界改写。
- **assumption_stress_test**: 跨形态稳定（经验观察：开放关系在浪漫 dyad 中存在，须建模）。

#### F04 — Infidelity / betrayal / 出轨背叛
- **layer**: OB（事件/违约）>DV
- **definition**: 违反关系约定（通常排他）的性与/或情感行为。
- **observable_or_latent**: observable（事件）+ 影响衍生
- **common_proxies**: “出轨”“劈腿”“精神出轨”“肉体出轨”“背叛”
- **overlaps_with**: exclusivity violation、lies、betrayal、distrust
- **keep_separate_because**: 是事件（违约输入），不是关系状态；其影响落到 trust/distrust 与恩怨账。
- **merge_or_derive**: OBSERVATION_ONLY（事件；+防守预期）
- **evidence**: E1（出轨后信任崩、修复难，多数研究描述 背叛后）
- **edge_cases**: 一次性肉体出轨与长期隐瞒精神出轨结构差异大；开放式关系中“越界”即使小也构成背叛（约定中心论）。
- **assumption_stress_test**: 关键在“边界”依约定而定。

#### F05 — Deception detection / 欺骗识别
- **layer**: ME
- **definition**: 识别对方隐瞒/虚假的能力；人际“诚实注意”的警觉度。
- **observable_or_latent**: mechanism（检测准确率很低是有名事实）
- **common_proxies**: “直觉觉得在骗”“看出破绽”“隐瞒”
- **overlaps_with**: distrust、belief updating、truth-default
- **keep_separate_because**: 人类欺骗检测准确率≈chance（真相默认理论）；应作为机制/信念层，不是状态。
- **merge_or_derive**: MECHANISM
- **evidence**: E1（诚实默认/检测底层）
- **edge_cases**: 高警觉无作弊（焦虑监控）；低警觉有大量隐瞒（盲信）。
- **assumption_stress_test**: 认知机制层。

#### F06 — Uncertainty / belief update / 期望与信念更新
- **layer**: ME（认知状态→可建模为 agent 信念）
- **definition**: 对“对方如何/关系如何”的不确定性及其贝叶斯式更新。
- **observable_or_latent**: latent（agent 信念）
- **common_proxies**: “不知道TA怎么想”“看不透”“摸不准”
- **overlaps_with**: PPR、goal/expectation、confidence
- **keep_separate_because**: 属于信念层（agent 的 belief），不是关系的 world state；模型会用 prior+update 表达不确定性，不新增 primitive。
- **merge_or_derive**: MECHANISM（信念表示）
- **evidence**: E2（关系中的信念更新模型较少）
- **edge_cases**: 高不确定高投入（“投资不确定的感情”）；确定性却崩（过度自信忽略信号）。
- **assumption_stress_test**: 认知层。

#### F07 — Expectation violation / 期望违背
- **layer**: ME（事件）
- **definition**: 实际结果显著偏离期待（正向/负向）触发的认知—情感更新。
- **observable_or_latent**: mechanism（对照 CL/标准）
- **common_proxies**: “没想TA会这样”“完全起反应”“惊喜/惊吓”
- **overlaps_with**: satisfaction、norm、surprise、RPE
- **keep_separate_because**: 是更新机制（无论正负），罕见作为关系状态；惊喜(positive)与失望(negative)都属违背但方向相反——不适合单独 primitive。
- **merge_or_derive**: MECHANISM
- **evidence**: E2
- **edge_cases**: 正违背递增满意度曲线（成长型婚姻）；负违背崩解信任。
- **assumption_stress_test**: 认知机制层。

#### F08 — Positive illusions / idealization / 理想化
- **layer**: DV（认知偏差）
- **definition**: 对关系/伴侣的过度放大的积极评价（与理想标准、错觉组合）。
- **observable_or_latent**: latent
- **common_proxies**: “滤镜”“情人眼里出西施”“看不到缺点”
- **overlaps_with**: love(initial)、mate value 误判、satisfaction
- **keep_separate_because**: 是认知加工风格（会影响状态），不是状态；热恋的高估是 temporary，与稳定依恋不同。
- **merge_or_derive**: DERIVED
- **evidence**: E2（积极错觉对满意有益但有边界——自欺成本）
- **edge_cases**: 强滤镜维持满意但现实脱节；无滤镜仍满意（现实派）。
- **assumption_stress_test**: 认知层。

### 4.G 性 / 偏好 / 亲属 / 身份

#### G01 — Sexual compatibility / 性契合
- **layer**: pair 匹配（DV/潜）
- **definition**: 双方性欲阶段、偏好、频率、方式的匹配程度。
- **observable_or_latent**: latent（性频率/满意/偏好匹配）
- **common_proxies**: “床上合得来”“性欲望不匹配”“没性趣”
- **overlaps_with**: A01、satisfaction、arousal
- **keep_separate_because**: 性满意 ≠ 一般关系满意的一半来源；性需求不匹配是显著分手/外遇因素。作为 dyad 匹配（D01 在性维的分量），可保留为潜变量。
- **merge_or_derive**: KEEP(潜)
- **evidence**: E1（性满意与关系满意高相关但不等价）
- **edge_cases**: 高性契合零爱情（炮友）；深爱却性不合（无性夫妻）。
- **assumption_stress_test**: 跨形态稳定（sexual 语境；asexual 时退化为无）。

#### G02 — Arousal / 唤起（生理）
- **layer**: ME（生理 proxy）
- **definition**: 自主/生理唤起水平（性唤起、心跳、掌心汗），是低层机制/代理。
- **observable_or_latent**: 生理可测（心理物理）
- **common_proxies**: “上脸”“呼吸急促”“身体有反应”
- **overlaps_with**: desire、anxiety (唤起共享)、excitement
- **keep_separate_because**: 唤起是跨情绪共享的低层生理维度，不宜当关系状态；可用作性欲/应激的观测代理。
- **merge_or_derive**: MECHANISM（生理 proxy）
- **evidence**: E1（唤起指纹说：跨情绪非特异）
- **edge_cases**: 高唤起误读为爱（吊桥效应）；焦虑高唤起被误读为欲望。
- **assumption_stress_test**: 机制层。

#### G03 — Asexuality / desire-mode variation（无性恋与欲模式差异）
- **layer**: Agent 属性（S）
- **definition**: 性吸引缺位或对性本身无需求；以及性欲在“主动/被动/情境性”上的模式差异。
- **observable_or_latent**: latent 属性
- **common_proxies**: “无性恋”“性冷淡”“不想要”“欲望低”“对性没兴趣”
- **overlaps_with**: A01、romantic orientation、文化与医疗
- **keep_separate_because**: 无性恋是性吸引的独立维度缺位，不等于功能障碍/回避；浪漫吸引仍可强。建模需允许“性欲=0 但浪漫高”。
- **merge_or_derive**: KEEP（Agent 属性）
- **evidence**: E2（asexuality 临床与身份研究）
- **edge_cases**: 无性恋者在浪漫亲密中的“性矛盾”（为爱而为 vs 无欲）。注意区分 desire vs 行为适应 vs 无性认同。
- **assumption_stress_test**: 跨形态稳定（性维只在按约定情况下参与）。

#### G04 — Kinship recognition / 亲缘识别
- **layer**: ME
- **definition**: 对亲缘程度的识别与对应关系反应（生理线索、表型匹配、环境线索）。
- **observable_or_latent**: mechanism（proxy：出生/环境/表型/气味）
- **common_proxies**: “血缘”“一家人”“像谁”“从小一起长大”
- **overlaps_with**: attachment、incest avoidance、social identity
- **keep_separate_because**: 用作解释为何亲近/回避亲缘；机制层解释不替代 dyad 状态。
- **merge_or_derive**: MECHANISM
- **evidence**: E2（亲缘识别：基于 co-residence 比基因更重要——Westermarck）；C（社会亲缘 vs 生物亲缘争论）
- **edge_cases**: 收养手足性吸引回避（共同抚养→伪亲缘抑制，支持 Westermarck）；亲缘却性吸引（极少，耦合环境异常）。
- **assumption_stress_test**: 机制层（kin 特殊化处理）。

#### G05 — Incest avoidance / 近亲回避
- **layer**: ME/RC
- **definition**: 对近亲性行为的心理回避与厌恶（Westermarck 假说）及伦理/法律约束。
- **observable_or_latent**: mechanism + role
- **common_proxies**: “恶心”“乱伦”“下不去手”
- **overlaps_with**: kinship、sexual orientation、moral
- **keep_separate_because**: 是对“性欲方向是否允许表达”的抑制回路；应作为约束/机制，而非状态。
- **merge_or_derive**: MECHANISM（+RC）
- **evidence**: E2（Westermarck 有支持有挑战；跨文化 incest taboo 存在但实施不一）
- **edge_cases**: 环境错疑虑（被误认为近亲而回避）；基因亲缘却无回避。
- **assumption_stress_test**: 机制/约束层。

#### G06 — Relationship identity / “我们”的认同
- **layer**: RC/identity（soft）
- **definition**: 个人对自己“是谁”（是否已婚/恋人/比朋友更亲）的自居身份，及对关系标签的认同。
- **observable_or_latent**: latent（self-identify + 行为标签）
- **common_proxies**: “我是他对象”“我们正式了”“公开”“官宣”
- **overlaps_with**: B05 we-ness、commitment、social role、pair-bond
- **keep_separate_because**: 身份（我在关系中是谁）与状态（我现在感觉如何）是两个层；身份改变（官宣、称谓）影响关系脚本但不必然改状态值。
- **merge_or_derive**: KEEP（身份状态）
- **evidence**: E2（关系认同与积极性）
- **edge_cases**: 身份是“前男友”但残余状态极高（复合纠结）；公开身份但状态冷却。
- **assumption_stress_test**: 跨形态稳定（伴侣身份、朋友身份等是 RC）。

#### G07 — Love 相关整体（浪漫/友伴/亲情 爱的类型）
- **layer**: DV（组合态）
- **definition**: “爱”在科学分类中是多种状态的组合——Sternberg 三成分（亲密/激情/承诺）、Berscheid 激情—友伴之爱、Shakespeare 语义都不指单一构念；现实中常见组合：
  - 热恋（浪漫爱）：A02 + (A01 或 G01) + 理想化
  - 友伴爱（companionate）：C05/B05 + C08 + B01（亲密+承诺+依恋，低激情）
  - 亲情之爱：B01 + B04 + C08(B05 取向) 不包含 A01/A02
- **observable_or_latent**: latent（组合诊断）
- **common_proxies**: “我爱你”“爱过”“亲情式的爱”“变成亲情了”“谁说爱就不吵”
- **overlaps_with**: 几乎与所有 情绪束缚
- **keep_separate_because**: 它不独立；因此永远不能当 primitive，但可作为 human-facing 的 RATING/DERIVED（组合看出成分）。
- **merge_or_derive**: DERIVED（组合性结论）
- **evidence**: E1（三成分/激情—友伴持续使用；“爱是动词”非单一状态）
- **edge_cases**: 激情爱保高而承诺低（抛弃性）；亲情式爱中无激情但稳定高。作 UI 结果，不作输入。
- **assumption_stress_test**: 组合性；重定义随语境（对亲友/伴侣都适用——对象不同成分不同）。

#### G08 — Status / prestige / 地位声望（及资源示好）
- **layer**: DV（评价）
- **definition**: 社会地位/声望/资源显示在择偶与关系权力中的作用。
- **observable_or_latent**: observable（S/O 属性）
- **common_proxies**: “有地位”“有面子”“大佬”“条件好”“门第”
- **overlaps_with**: mate value、D06、resource、power
- **keep_separate_because**: 地位是个人属性（S/O），通过 mate value 与资源进入关系；不是关系 state。
- **merge_or_derive**: OBSERVATION_ONLY（属性）
- **evidence**: E1（地位与择偶偏好存在相关，但因果方向 contested）
- **edge_cases**: 权威高而情感低（烂脾气但威名在外）；地位反向（高价值却低相处）。
- **assumption_stress_test**: 市场/属性层。

> 至此完成 **6A+8B+15C+8D+9E+8F+8G = 62 个候选构念**的语义边界审计，满足 “50+ 候选构念审计”。

---

---

## 5. mechanism → state → observation 三层图

### 5.1 总图

```text
┌──────────────────────────────────────────────────────────────────────────┐
│  OBSERVATION 层（可测量 / 可报告 / 可编码）                              │
│    自我报告题项、行为频次（接触/投入/冲突/修复）、身体亲近、生理 proxy、 │
│    SNS 互动、礼物金钱、共同生活事件记录                                  │
│    → 供 estimation 反推 state；不可直接当 state                          │
└──────────────────────────────┬───────────────────────────────────────────┘
                               │ 估计/推断 (inverse model)
┌──────────────────────────────▼───────────────────────────────────────────┐
│  PRIMITIVE_STATE 层（最小充分关系状态，有向 dyad 边或 pair 量）          │
│  有向 (per-agent → partner)：                                            │
│    A01 Sexual desire ─────── A02 Romantic attraction ─── A03 Liking       │
│    B01 Attachment security    C04 PPR(感知被回馈)       C01 Trust         │
│    C08 Commitment(dedication) B04 Caregiving                               │
│   pair 侧：B05 Cohesion/we-ness · D02/D03 Value&Goal congruence(A)=align  │
│   结构侧：C13 Outcome dependence（不对称→权力 DV）                         │
│   规则侧：F03 Exclusivity agreement (RC)、G06 Relationship identity (RC)  │
└──────────────────────────────▲───────────────────────────────────────────┘
                               │ 生成/解释 (forward model)
┌──────────────────────────────┴───────────────────────────────────────────┐
│  MECHANISM 层（解释为什么如此；不直接建模为关系状态）                    │
│    奖赏/多巴胺/RPE · 催产素/AVP · 杏仁核威胁 · 性激素周期                │
│    依恋行为系统 · 关怀系统 · 求偶/守护/亲本投资 策略                     │
│    认知机制（信念更新、期望违背、诚实默认、理想化）                      │
│    亲缘识别 / Westermarck 抑制                                            │
└───────────────────────────────────────────────────────────────────────────┘
```

### 5.2 判定规则（哪些进 primitive）

按 `#2 5565245810` 的最小充分性：给定某个 primitive 状态后，若更底层机制对该状态的转移几乎不提供额外信息，则底层机制留在 ME 层。只有同时满足 MSC 五条（§2.3）的才进 primitive。例如：**“他给我多巴胺”不是 primitive；可建模的是 A01/A02/C01 等状态的可观测估计。**

### 5.3 D/O/A 三视图与所对应的 primitive 候选

```text
Layer S（Agent 属性/慢变量）：A05 orientation、B03 anxiety/avoidance、SOI、age/health/resources（D06）
Layer D（Dyad，有向为主）：A01/A02/A03、B01/B04、C01/C04/C08、C13（结构）、B05、F03/G06（RC）
Layer E（Context/环境约束）：替代质量 C11、社会/法律/文化规范、资源环境、制度
```

### 5.4 “primitive / latent construct / observable proxy / derived outcome” 四类判定总表

| 判定 | 判据 | 落入的构念 |
|---|---|---|
| **primitive** | MSC 五条全过 | A01, A02, A03, B01, B04, B05, C01, C02, C04, C08, C13；结构侧 F03/G06（RC 类别，不叫恋爱状态） |
| **latent construct（潜变量，不直接可测，但有指标）** | 可被代理推断、但本身是状态 | 上表里多数 PS；另 D02/D03 对齐、G01 性契合 属于 pair 潜 |
| **observable proxy（代理/指标）** | 直接可测、用于反推上面 | C03 predictability、C06 disclosure、C10 investment、E03 synchrony、E07 responsiveness 行为、B07 touch、G02 生理唤起 |
| **derived outcome（派生结果）** | 由状态/指标组合计算 | C05 intimacy、C07 closeness、C09 constraint、C12 satisfaction、C14 power、E08 fairness、C15 恩怨账、G07 love、D08 般配感、D04 互补、F01 嫉妒 |

> 注：同一词在不同语境可能出现在多个格子（如 intimacy 既作状态又作 DV）；本表给出 LHRM 推荐用法。

---

## 6. 易混淆构念成对比较（15+）

> 每对比的核心问题：**它们是否同一构念？若不是，区分它们的现实反例是什么？**

### 6.1 commitment vs investment
- 反例解耦：**高投入低承诺**（维持多年共同财产却因无爱而想离）× **高承诺低投入**（初见即网络异地、资历浅却生死相许）。
- 结论：investment 是 commitment 的输入/成本（贡献 commitment），不是 commitment 本身。把“投入了很多”当“一定很爱/一定承诺”是常见直觉错误（沉没成本谬误的风险更强）。

### 6.2 trust vs security
- 反例：**高信任低安全**（他值得信赖，但我仍不踏实——依恋焦虑/低安全感患者）× **低信任高安全**（相信现有和平度日，却不认为对方关键时刻可靠）。
- 结论：trust = 期望+愿意承担被辜负的风险；security = 情绪安全/可依赖感。可重叠但不同轴。security 更靠近 B01；trust 更靠近决策/信念。

### 6.3 bond vs attachment
- 反例：**强 bond 低 attachment**（为共同体/利益/习惯绑定却无依恋感）× **强 attachment 低 bond**（极强依恋依赖却谈不上“我们是一体”的共同体感）。
- 结论：bond 语义被滥用（含凝聚、承诺、制度、身份）。本报告建议 bond 拆为 B01(B01 attachment-security) 与 B05(cohesion/we-ness)；attachment 指依恋系统。

### 6.4 alignment vs similarity
- 反例：**高分同质低 alignment**（都高攻击性所以互相消耗）× **低分相似高 alignment**（性格互补但目标一致）。
- 结论：similarity = 属性距离；alignment = 目标/价值观/方向一致性。相似可预测消遣/初始吸引，alignment 预测长期 co-planning 与幸福。二者是多向关系，不是同一构念。

### 6.5 attraction vs liking vs love vs sexual desire（四联）
- 反例：
  - **liking 高、sex desire 0、romantic 0**（密友纯喜欢）
  - **sex desire 高、liking 低、romantic 低**（纯性吸引、反感其人格）
  - **romantic 高、sex 0**（无性恋恋爱）
  - **love（DV）＝各状态组合**，非独立。
- 结论：必须分三股（性欲、浪漫吸引、喜欢），love 是熔炉态（DV）。

### 6.6 intimacy vs closeness vs self-disclosure vs responsiveness（亲密族）
- 反例：**披露多但亲密低**（单向倾吐不被回应，只感觉受伤）；**亲密深却不靠披露**（共同经历酿出的心印）；**closeness 高但 intimacy 低**（互利同盟却无深交）。
- 结论：self-disclosure=行为（OB）；responsiveness=感知/行为（C04/E07）；intimacy=结果态（DV）=f(披露×响应, 时间)；closeness=心理重叠的 DV/IoS。四个词别用同一 primitive。

### 6.7 dependence vs commitment vs constraint
- 反例：**高依赖低 dedication**（离不开却不想留）× **低依赖高 dedication**（可复利的人选择留下）× **高 constraint 高 dependence**（被困）× 高 dedication 低 constraint（自愿无绑）。
- 结论：dependence=C13 结构；constraint=C09 结果态（=trade-off/成本）；dedication=C08 意愿。三者独立演化，合并会让“被困关系”无表达。

### 6.8 trust vs faith vs predictability vs credibility
- 拆解：predictability（C03 可预期，无价值判断）< credibility（能力/一致评价）< dependability（善意承诺可依赖）< faith（超越现有证据的信任）——信任假设型末端 e.g. 短期无信息即托付。
- 结论：作为 primitive 保留 trust（C01 总体）。其余为 facet 或 proxy。

### 6.9 power vs dominance vs control vs autonomy
- 反例：**高 power 低 dominance**（结构上房主但从不胁迫）× **低 power 高 dominance**（弱势方拍桌威胁）；control 是行为，dominance 是偏好（个人倾向），power 是结构。
- 结论：power=C14（derived）；dominance/control 属 S 属性（人格/行为倾向）；autonomy 是 S/O 层面的个人自由度（见 §6.12）。

### 6.10 jealousy vs envy vs mate guarding
- jealousy=关系对象关系威胁；envy=渴望他人所有（不舒服的另一种）；mate guarding=行为策略（F02）。envy 不该混进关系 primitive；mate guarding 是行为/策略层。

### 6.11 conflict vs repair vs forgiveness vs gratitude/resentment
- conflict=事件（E04），repair=事件技能（E05），forgiveness=伤害后决定（E06），C15 恩怨账=进程累积（DV）。若只留一个会导致“冲突→怨恨、可修复、可原谅”的动态无法表达。

### 6.12 autonomy vs dependence（这不是反义词的简单两端）
- 反例：**高 autonomy 高 dependence**（个人自由度高却高度依赖对方的结果）：独立能力强但把幸福锚定在对方身上；**低 autonomy 低 dependence**（都没自由、也都无所谓对方在不在）：功能性共栖但无情感依赖。
- 结论：autonomy（自主自由，S/E 属性）与 dependence（结果依赖，C13）不同轴。合并会让“自由恋却缠人”难以建模。

### 6.13 exclusivity vs infidelity vs jealousy vs pair-bond
- exclusivity=规则（F03）；infidelity=违约事件（F04）；jealousy=对威胁的情绪（F01）；pair-bond=组合制度（B06 DV）。四个各在不同层。

### 6.14 love（G07） vs commitment（C08） vs satisfaction（C12）
- 反例：爱高但 commitment 低（相爱却分手——禁忌爱）；承诺高但 satisfaction 低（责任维持，程式化之爱）；满意高但爱低（相处舒服无热情）。
- 结论：爱≠承诺≠满意。爱是成分组合 DV，commitment 是维持意愿，satisfaction 是收益评估。

### 6.15 value congruence vs ideal standards match vs compatibility（D02/D05/D08）
- value congruence=双方价值观一致（pair 属性）；ideal standards match=个体理想标准（评价者内部）；perceived compatibility=全局“般配感”DV。三者在“三观合/合适”语义里被混用；应分离：理想标准匹配是 S×O 评价器，价值一致是 pair 属性，般配感是 DV。

### 6.16 attraction（D） vs status/economic value（E/O）
- 反例：高地位高资源但零吸引（有钱没性张力）× 高吸引却低地位（穷但有魅力）。
- 结论：吸引（A 系）是关系状态，地位/资源是 S/O 初始属性，可通过 mate value(D06) 影响初始评估与匹配，但不可相互替代。不得把“条件好”当“有吸引力”。

### 6.17 sexual desire vs arousal vs orientation（A01/G02/A05）
- desire=状态（想要目标）；arousal=生理机制；orientation=稳定偏好（属性）。三者测量与含义不同（女人 desire-arousal 解耦尤其显著；asexual）——分开放。

### 6.18 closeness vs we-ness vs cohesion vs inclusivity（B05 家族）
- closeness（C07）=主观心理重叠；we-ness（B05）=共同体认同；cohesion=群体的凝聚（社会心理更常用）；inclusion of other in self（IoS）=认知测量。建议 B05 统一建模，C07 作为其 proxy。

### 6.19 PPR vs support vs caregiving（接收 vs 发送）
- PPR（C04）=接收方感知“被理解被认可被在乎”；support/caregiving（B04/E07）=发送方行为与胜任。反例：到处帮忙却帮不到点子上（高支持低 PPR）。方向、声音、评估者不同。

### 6.20 trust vs cooperation vs reciprocity（不同层）
- trust=状态（C01）；cooperation=行为（E02）；reciprocity=交换结构（E01 DV）。高信任也可能不合作（策略性）；合作可出于规则而非信任。三者不能画等号。

> 至此提供 **20 组**易混淆构念成对比较，满足“≥15 组”。

---

---

## 7. 当前 Relationship 候选六维的逐项裁决

> 判据：MSC（§2.3）+ 反例解耦（§2.4）+ 跨形态稳定性 + 与其它五维的冗余度审查。

### 7.1 Attraction → **SPLIT**

**裁决**：拆为 `A01 sexual desire` 与 `A02 romantic attraction`（`A03 liking` 另计）。

**证据**：性欲、热恋与喜欢在时程、功能、测量上均可分离（E1/E2）；“零性欲但深恋”“零浪漫但纯性”“纯喜欢但在恋爱外”三状态真实存在；浪漫热恋随时间衰减而性欲不一定同向（E2）。吸引一个词吞掉三种不同方向的趋向，导致无法表达“到底哪种吸引”。

**MSC 审查**：性欲（A01）：不可归约、可去耦（与浪漫、喜欢、依恋解耦）、有动力学（频次、唤起、欲望随互动变化）、可估计（自报+唤起）、跨形态稳定。故 A01 胜出。浪漫吸引（A02）同理。liking（A03）作为低唤起正向亲和，也与前两者可解耦。

**若强留“Attraction”**：只能作为 DERIVED/RATING（面向 UI 的“对TA有无感觉”总评），且必须标注其成分及缺失模式。

### 7.2 Bond → **SPLIT/REDEFINE**（拆为 B01 依恋安全 + B05 情感凝聚/we-ness）

**裁决**：不保留单一 Bond primitive。

**证据**：依恋安全（B01）与共同体凝聚（B05）可解耦：①高 B01 低 B05（安全亲密却无“我们是一家”认同——可长期相守但身份各自独立）；②低 B01 高 B05（强烈共同体认同却无明显依恋安全，如责任感/利益共同体）。二者驱动因素不同（依恋系统 vs 关系认同与共享身份）。

**MSC**：B01 满足全部五条（安全状态有动力学：分离/威胁事件升降；可被投入代理；跨形态稳定）。B05 作为 pair 量更接近“慢结构+认同”，也有动力学但更缓慢——仍列为 PS（低时间尺度）。

### 7.3 Trust → **KEEP**（精确定义）

**裁决**：保留 C01（+拆出 C02 distrust、C03 predictability）。

**证据**：信任是跨形态都存在的方向性状态（商业伙伴、亲友、伴侣同构）；与安全、亲密、承诺均可解耦（§6.2 等反例）。MSC 全部满足。**前提**是把它从“安全感”“善良评价”“满意度”中拆干净。

### 7.4 Commitment → **KEEP/REDEFINE**（定义为 dedication）

**裁决**：保留 C08（dedication），把 investment（C10）、alternative（C11）、satisfaction（C12）、constraint（C09）、dependence（C13）全部拆出。

**证据**：投资模型 meta 支持“commitment ≈ satisfaction − alternatives + investments”是成分关系（E1），因此 commitment 若是 derived 会重复计数 input；保留“dedication”作为独立意愿状态（E1 结构清晰）。承诺的“感觉/契约”双源性也支持 dedication 与 constraint 分开（E2）。

**MSC**：dedication 满足（意愿受事件影响可更新、可去耦——§6.7 反例全可构造、可被 proxy 估计、跨形态稳定）。

### 7.5 Alignment → **REJECT 作为 primitive**（降为 DERIVED/评价维度）

**裁决**：不保留 alignment 作为单一 primitive；拆为 D02 value congruence + D03 goal alignment，二者可建模为 pair 的慢潜 / 匹配量；"alignment" 保留为 DERIVED 面向用户的评价词。

**证据**：alignment/similarity/compatibility 三词在“三观合、般配”语义中混用，统计学上和日常直觉上都高度纠缠（E2）。它**不是有向边上的最小状态**，而是对两个 Agent 属性（价值观、目标向量）的“一致性度量”外加感知（D08）。它更像匹配层的 pair-quantity，而非随时间以细粒度更新的关系状态；MSC 第 3、5 条（动力学、独立性）不能满足或至少被 D01/D02/D03 分享。

**反例**：属性相似≠目标同向；目标同向≠功能互补；三者需分列，否则“三观不合但同心合力”“性格像却互相消耗”无法表达。（拆分后 D02/D03 可作 KEEP/latent；D01 是 OB。）

### 7.6 Dependence → **KEEP**（结构定义）

**裁决**：保留 C13（outcome dependence），并派生 C14 power（不对称）。

**证据**：互依理论是关系动态的结构支柱（E1）；结果依赖不可归约、可去耦（§6.7-6.12）、有动力学（投入/替代变化时改变）、可估计（结果评估+替代）、跨形态稳定；它与 security、trust、commitment 均非同一轴。它是“为什么离不开”最必要的结构变量。

### 7.7 汇总表

| 候选 | 裁决 | 保留形态 | 需拆出的东西 |
|---|---|---|---|
| Attraction | SPLIT | A01(性欲) + A02(浪漫) [A03 liking 另列] | 不要把吸引当单一值 |
| Bond | SPLIT/REDEFINE | B01(安全依恋) + B05(凝聚/we-ness) | 避免 bond 吞掉 commitment/身份 |
| Trust | KEEP | C01 trust（+C02 distrust） | predictability 作 facet/obs |
| Commitment | KEEP/REDEFINE | C08 dedication | 拆 investment/alt/satisfaction/constraint/dependence |
| Alignment | REJECT→DERIVED | D02+D03（pair 潜） | 拆 similarity/compatibility/ideals |
| Dependence | KEEP | C13 outcome dependence | 派生 power(C14) |

### 7.8 研究性建议：可能的“最小充分核心”候选集（供 Architect 仲裁）

依据 MSC，我建议把以下作为**最小充分关系状态字典**候选（仍属 research proposal，不是冻结规范）：

```text
有向（Alix→Bob 与 Bob→Alix 各一套，可非对称）：
  性欲 Desire             A01
  浪漫/热恋取向 Rrom      A02
  喜欢/正向暖感 Liking    A03
  依恋安全 Security       B01
  关怀 Caregiving         B04
  感知被回馈 PPR          C04
  信任 Trust              C01（+Distrust C02）
  承诺意愿 Dedication     C08

pair / 结构 / 约束：
  情感凝聚 Cohesion / we-ness       B05
  价值观&目标一致 Value/Goal align   D02/D03（合称 Alignment，慢）
  结果依赖 Outcome Dependence       C13
  排他/边界约定 Exclusivity Rule    F03（RC）
  关系身份 Relationship Identity    G06（RC）
```

其余 40+ 构念按 §2.2 映射到：observable_proxy（C03/C06/C10/C11/E03…）、derived（C05/C07/C12/C14/E01/E06/G07…）、mechanism（A04/G02/F05/G04/G05…）、Agent 属性（A05/B03/G03/…）。这组“核心 + 代理 + 派生 + 机制 + 约束”五层映射，就是供 `#2` 跨 Research 去重与最小生成时使用的推荐素材。

> **重要**：这一“最小核心”是研究判断，仅作为 Architect 融合时的候选；最终 canonical 集合与数值由 `#2` 仲裁，本报告不越权定稿。

---

## 8. 日常代理词 → 构念映射（40+）

> 说明：一个代理词可映射到多个候选（按上下文），此处给主映射与备选。

### 8.1 吸引 / 性 / 浪漫

| 日常词 | 主映射 | 备注/备选 |
|---|---|---|
| 来电 / 有感觉 | A01/A02 | 需要判断模式（性/浪漫），常混合 |
| 心动 / 小鹿乱撞 | A02 | 热恋唤起 |
| 想睡TA / 有性趣 | A01 | |
| 恋爱脑 / 上头 | A02 | +F08 理想化 |
| 眼里只有TA | A02 | |
| 想TA想到失眠 | A02 | |
| 性冷淡 / 没性趣 | A01(−)/G03 | 属低性欲或 asexual 身份 |
| 床上合得来 | G01 | 性契合 |
| 炮友 / 只约不处 | A01, 无 A02 | high sex, low romantic |
| 无性恋 / 对性没兴趣 | G03 | desire-mode |
| 高富帅 / 白富美 / 条件好 | D06 | 与 A01 无关的市场价值 |
| 有魅力 / 很社交 | D06/A03 | 广义吸引的代理 |

### 8.2 依恋 / 安全 / 关怀

| 日常词 | 主映射 | 备注/备选 |
|---|---|---|
| 有他在就安心 / 像家一样 | B01/B02 | 依恋安全 |
| 被托底 / 睡前都踏实 | B01 | |
| 患得患失 / 作 / 要确认爱 | B03(焦虑) | agent 属性 |
| 不敢投入 / 疏离 | B03(回避) | |
| 有安全感 / 安全感足 | B01 + C01 | 常混淆 trust/security |
| 他会照顾人 / 体贴 | B04/C04 | 行为侧 |
| 被呵护 / 被宠 | B04/C04 | 感知侧 |
| 孤单但有人陪（婚内寂寞） | B08(孤独) | 不因“在一起”而消解 |

### 8.3 信任 / 承诺 / 投入

| 日常词 | 主映射 | 备注/备选 |
|---|---|---|
| 信得过 / 靠谱 | C01 | trust |
| 敢放心交出去 / 掏心掏肺 | C01 | trust(behavior) |
| 防着他 / 疑神疑鬼 | C02 | distrust |
| 认定TA / 想走下去 | C08 | dedication |
| 余生都是你 / 白首 | C08 + B05 | |
| 将就 / 凑合过 | C09/C13 | constraint/dependence |
| 离不开 / 没TA不行 | C13 | |
| 骑驴找马 / 备胎 | C11 | alternative/CL-alt |
| 付出了太多 / 已绑死 | C10/C09 | investment→constraint |
| 为孩子坚持 / 离婚影响大 | C09 | structural |
| 感激 / 记仇 / 寒心 / 翻旧账 | C15 | 恩怨账 |

### 8.4 相容 / 匹配 / 三观

| 日常词 | 主映射 | 备注/备选 |
|---|---|---|
| 三观合 | D02 + D03 | 勿与 D01 混淆 |
| 三观不合 | D02(−) | |
| 聊得来 | A03 + C04 | liking+PPR |
| 同类 / 像 | D01 | similarity(obs) |
| 互补 / 一攻一受 | D04 | complementarity(DV) |
| 默契 / 同频 | E03 + B05 | synchrony/cohesion |
| 般配 / 门当户对 | D08+D07 | 评价/D-V |
| 不是我的菜 / 够不上标准 | D05 | ideals match |
| 灵魂伴侣 | B05 + C05 + C08 | 组合处 |

### 8.5 威胁 / 边界 / 背叛

| 日常词 | 主映射 | 备注/备选 |
|---|---|---|
| 吃醋 / 查岗 | F01 + C02 | jealousy+distrust |
| 管得紧 / 看得紧 | F02 | mate guarding |
| 一对一的 / 开放关系 | F03 | exclusivity rule |
| 出轨 / 劈腿 / 精神出轨 | F04 | infidelity(breach) |
| 背叛 / 骗我 | F04→C02− | betrayal→distrust drop |
| 第一次吵架 冷战 | E04 | conflict event |
| 主动求和 / 破镜重圆 | E05 + E06 | repair/forgive |
| 原谅不了 / 咽不下这口气 | E06(−) | unforgiveness |
| 好马不吃回头草 vs 复合 | C13/C08/C01 综合 | |

### 8.6 情绪 / 评价 / 综合

| 日常词 | 主映射 | 备注/备选 |
|---|---|---|
| 跟他在一起很开心 | C12 | satisfaction |
| 很幸福 / 日子顺 | C12 + B01 | |
| 生气就下头 | A02− + C03 | |
| 他让我很安心很有底气 | C01+B01 | |
| 缘分 / 命中注定 | D08 | perceived compatibility |
| 真爱 / 真爱无敌 | G07 | love DV（成分组合） |
| 亲情式的爱（变亲情） | G07(: compose) | companionate |
| 我们（我们俩） | B05 | we-ness |
| 我是他对象 / 我们正式了 | G06 | relationship identity |
| 前 / 现任 / 前任 | G06 + role | identity/stage class |
| 对他来说我只是个好消息 | C04(−) | PPR 低 |

> 合计 ≥52 条代理词映射，满足 “40+ 日常代理词映射”。

---

## 9. 建议合并 / 淘汰 / 降级清单

### 9.1 建议合并（避免重复计数）

| 建议 | 理由 |
|---|---|
| B02 felt security → MERGE into B01 | 仅为 B01 的主观读出口 |
| B06 pair-bond → MERGE into BV(B01+B05+C08+F03 组合态) | 组合词，不作独立 primitive |
| B07 touch / C07 closeness → MERGE into B05（作 proxy） | 行为/认知代理 |
| C03 predictability / C07 closeness → 作为 C01/B05 的分面, 不单设 | 见 §6.8 |
| D04 complementarity → MERGE into functional-fit(DV) 或 D02/D03 | 弱、任务依赖 |
| E01 reciprocity/E08 fairness → 并入“互依/交换账”（DV） | 事件统计 |
| F01 jealousy → 由 威胁事件+C02+B03 触发态 表达 | 避免与 distrust/anxiety 共线 |
| A04 reward/RPE、G02 arousal、E09 coregulation → 统归 MECHANISM | 机制层 |

### 9.2 建议淘汰 / 降级为 OBSERVATION_ONLY 或 DERIVED

| 构念 | 处置 | 理由 |
|---|---|---|
| Attraction（总词） | SPLIT | 见 §7.1 |
| Bond（总词） | SPLIT | 见 §7.2 |
| Alignment（总词） | DERIVED（评价） | 见 §7.5 |
| D05 ideals match | DERIVED | 评价器 |
| D06 mate value | DERIVED | 市场评价 |
| D07 assortative mating | DERIVED | 宏观统计 |
| D08 perceived compatibility | DERIVED | 全局评价，重复计数高 |
| C12 satisfaction | DERIVED | 收益输出 |
| C14 power | DERIVED | = 依赖不对称 |
| C05 intimacy | DERIVED | = f(PPR×disclosure, t) |
| G07 love 及各“爱”类型 | DERIVED | 组合态 |

### 9.3 建议保留为 Agent 属性 / 约束（非 dyad primitive）

A05 orientation、B03 anxiety/avoidance、G03 asexuality/desire-mode、SOI、C11 alternatives（感知替代）、F03 exclusivity、G06 relationship identity、亲属/kin 关系类型、E 资源/地位（D06 源属性）。

### 9.4 明确机制层（不进入 primitive）术语

多巴胺 / 奖赏 / RPE、催产素 / 血管加压素、杏仁核 / 威胁回路、性激素与周期、亲源识别 / Westermarck、镜像/同步神经过程、co-regulation、deception detection、belief update、expectation violation、positive illusions（指向认知机制），以及所有“xxx脑区激活”类表述。

---

## 10. 关键争议、竞争理论与剩余不确定性

### 10.1 仍无法用单一结构消解的竞争假说

1. **热恋到底是不是独立系统**：Fisher 三系统（lust/attraction/attachment）vs 将 romantic passion 视为 attachment × desire 的复合（Berscheid/Beach 诸家）。→ 我在 A01/A02 选择分离式建模，但注明 C contested。
2. **信任与不信任是否同一双极**：Lewicki 双元论 vs 单极观。→ C02 暂列独立节点，Architect 可按模型需要极化。
3. **相似是否真的重要**：实际相似吸引效应小、感知相似效应大（meta）。这意味着“matching/准确性”更多是认知人际层，未必作为 primitive 动力学核心。→ 降 D01 为 OB。
4. **承诺两分（dedication/constraint）的理论与测量之争**：约束承诺是 subtype 还是独立构念仍有争议。→ 我建议 dedication 独立、constraint 作 derived。
5. **性吸引与浪漫吸引在临床上/神经上是否可分离**：强证据支持“行为上”可分离（asexual/非婚），但神经编码可能共享 reward mechanism。→ 状态层分离，机制层共享（可接受）。
6. **同性恋进化解释的竞争性假说**（平衡选择、kin selection、圣父假说、性选择、中性/社会构建等）：许多假说并存且无统一结论。→ 本报告因此刻意“不将进化功能作为关系的 canonical primitive 依据”，仅作 hypothesis/evidence（符合 amendment）。
7. **神经影像/激素的“因果”错觉**：处刑式激活转载、催产素“爱情荷尔蒙”标签在科普常被放大；医学证据反复后归因稳弱。→ 本报告将全部神经-生物词放入 mechanism 层并附警示。
8. **“爱”是否应存在模型**：争论“爱”是否“真实构念”“动词”是否有独立状态。→ 我用组合态（DV）处理，避免把它当 primitive。

### 10.2 方法论上的剩余不确定性

- 本报告基于领域内公认经典与部分 meta 的结构性归纳；**不做权重/校准/因果估计**，具体效应量与参数由后续 Empirical/校准工作承担（超出 Research scope）。
- 跨文化普适性：X 六形态压力测试仅从“语义能否保持”维度验证；**文化差异**（如对性、亲情、排他、地位的不同规范）应以 `role_constraint`/`E` 层变体表达，而非每个文化一套 primitive。
- 对“亲缘/亲属”与“陌生/既有”的压测：本报告通过 `assumption_stress_test` 标记出 `meaningless-here` 与 `role-variant`，但**认定某个构念在 kin/stranger 下“无意义”也是一种语义决策**，需 Architect 复核，尤其要避免“无意义”被误用为“不存在”从而漏掉压测覆盖。
- 计算关系模型现状：可见的成熟“关系状态形式化”多于游戏/市场/统计层；语义 primitive 多来自社会科学而非 ABM。若后续要 ABM 化，需要把 C13/治理/背叛等动力学落到事件级转移，这超出本报告，作为 downstream 建议提出。

### 10.3 Remaining uncertainty 摘要

1. 每个 primitive 的“时间粒度”与“更新方程”未定（研究不设公式/权重）。
2. C02（distrust）与 C01（trust）的关系待实证数据定夺（平台化后验）。
3. D02/D03（alignment）的“量度”定义未定（pair 属性还是慢状态）。
4. assumption_stress_test 在“kin / stranger”两类边上到底应标记成熟态还是 unknown，待 #2 仲裁。
5. 所有 “E1/E2” 的强度来自既有文献方向性，非直接引具体相关系数（避免造假）；具体校准值留给后续。

---

## 11. 引用与来源（精选，按主题）

> 采用简标明（author, year）形式；文献细节请在外部库核对。所有被标 `C`（contested）或 `hypothesis` 的命题都只作为竞争假说，不作为 canonical 事实。

**依恋**：Bowlby（1969–1980 Attachment and Loss 三卷）；Ainsworth 陌生情境；Hazan & Shaver（1987, JPSP）；Brennan, Clark & Shaver（1998, ECR）；Mikulincer & Shaver（2007, *Attachment in Adulthood*）。

**亲密/PPR**：Reis & Shaver（1988, 亲密过程模型）；Reis, Clark & Holmes（2004, PPR 综述）；Laurenceau, Barrett & Pietromonaco（1998, 披露×响应）。

**互依/承诺/投入**：Thibaut & Kelley（1959）；Kelley & Thibaut（1978）；Rusbult（1980, 1983）；Rusbult & Van Lange（2003, AnnuRev）；Le & Agnew（2003, 投资模型 meta）；Adams & Jones（1997）；Stanley & Markman（1992）。

**信任**：Rempel, Holmes & Zanna（1985, JPSP）；Simpson（2007）；Lewicki et al.（1998, trust-distrust）。

**择偶/进化**：Buss & Schmitt（1993）；Buss（1988）；Haselton & Buss（2000, 误差管理）；Thornhill & Gangestad；Westermarck（近亲回避）。

**性/取向**：Penke & Asendorpf（2008, SOI-R）；Basson（2000, 女性性反应模型）；Kinsey 等；Storms（浪漫/性吸引）；deinition of asexuality 文献（Brotto 等）。

**爱/组合态**：Sternberg（1986, 1997）；Berscheid（2010, 激情/友伴爱）；Lee（颜色论）；Rubin（1970, 喜欢—爱量表）。

**认知/匹配**：Byrne（相似吸引）；Montoya, Horton & Kirchner（2008, 相似吸引 meta）；Luo & Klohnen（2005, 类选婚配与婚姻质量）；Fletcher & Simpson（2000, 理想标准模型）；Murray, Holmes & Griffin（1996, 积极错觉）。

**计算/形式化启发**：互依理论博弈化（Kelley 体系）；动态系统/状态转移关系模型（Gottman 系）；贝叶斯信念更新（信任与期望）以及 agent-based 择偶/市场模拟的传统（作建模语法参考）。

> 证据分级与争议标注见 §2.1 与 §10；任何未确认的机制关系（脑区/激素/基因→关系状态）一律标注 hypothesis/mechanism，不作为 primitive 依据。

---

*本报告由 Research 角色按 `youling/lhrm#4` comment `5565248580`（ARCHITECT_RESEARCH_DISPATCH_V2）生成，供 `youling/lhrm#2` 架构仲裁使用。不修改 canonical ontology。*
