# 19 — SYNTHESIS_CANDIDATE

> **`SYNTHESIS_CANDIDATE` 不是 canonical architecture。**
> 本文件是 parent（Research Orchestrator）对 18 条 Wave 1 lane 报告与 4 份 Wave 2 audit 报告的 **join**。它不修改 ontology / foundation / 公式 SSOT / schema / 权重 / 阈值。
> 未经 Human / Project Architect 审阅，本文件中的任何结论**不得**被当作已确立结论、参数、公式、公式 SSOT 或验证依据。
> 本文件不含任何新的文献主张。所有事实性陈述的指针在其来源 lane 报告中；本文件只做交叉引用与冲突登记。

- **Work Order**：`youling/lhrm#30@overnight-opencode-exploration-swarm-v1`
- **Base**：`youling/lhrm@main` = `ee393ca24f9fbf738ac0ed839e99bdc99de6fc3a`（2026-09-27 live 复核，无漂移）
- **Governance at run**：`youling/ai-use@main` = `64018d80443c1889c8aaf4a6d27ffe78f3e6dd90`
- **As of**：2026-09-27
- **构成**：18 lane 报告（R00–R17）+ 4 audit 报告（A01–A04）+ manifest + child contract = 24 份 / 1,706,903 字节

---

## 0. 读法与三条自我约束

1. **本文件不是裁决。** 下面 §2 登记的每一处矛盾都需要 Human / Architect 裁决。本 attempt 不裁决。
2. **本文件不把一致性当作正确性。** 多个 lane 独立收敛到同一结论**不构成** validation（Work Order 明确禁止把文献数量或 LLM 一致度当作 validation）。收敛只说明「多条独立文献线指向同一处」，不说明该处为真。
3. **本文件不含 filler。** 凡目标未达成处，写明未达成，不补。

---

## 1. Robust agreements（多 lane 独立收敛的结论）

> 标注格式：`Lanes` = 独立收敛的 lane 数；`Type` = `empirical`（有外部实证）/ `structural`（架构内在推论）/ `methodological`（方法学推论）。
> `Type` 一律**不是**「已确立」。

### A1. 现有的验证门在当前定义下**不能产生否决** — `methodological`

- **Lanes**：R17（F1 / F9 / F11）、A03（独立判定，三项可复现检验 T1/T2/T3）。
- A03 的判定比 R17 更强也更具体：Gate A `EXECUTABLE_BUT_NON_FALSIFIABLE`；Gate B / Gate C 既不可证伪也不可执行；`PARAMETER_CONVERGENCE_V0_1.md` §2.6（**唯一能删除 construct 的准入侧判据**）结构上无法触发 ⇒ 8 项 candidate basis 单调增长，`MERGE` 与 `REJECT` **从未被签发过一次**。
- Gate A 的五个步骤全是 *recording obligation*（记录义务），没有阈值、没有任何 `若…则否决` 句；`0%` 与 `26/26 MAPPING_FAILURE` 同样被接受。
- **A03 的额外发现**：§13「禁止**第一反应**直接新增 primitive」+ §15 step 5 构成一个**无界修复环**——唯一被规定的失败动作是「诊断 → 修 schema → 重跑」。
- **A03 修正了 R17 的一个数字**：R17 称 Gate B 的 11 类反例**全部**是项目自身假设列表；A03 逐条核对后判为 **8/11**（其中 3 类是 §4「为什么保留」条目的逐字复述），并给出更窄但更强的基础。
- **A03 确认**：R17 `F1` / `F11` / `F9`(1,3,4,5) CONFIRMED；`F9`(2) 需修正（判决「Findings of Fact」前存在**三个**正交预过滤：法律相关性 / 争议中心性 / 事件密度，不是一个）。
- **A03 量化了「所有模型都能过」的具体路径**：R13 的六个 faithfulness 指标中，存在**两条平凡通过路径**（全部弃答；直接复制 fixture 的 status 列）；且 2/6 在 Fixture 003 的任何 rights 状态下**不可计算**。
- **A03 机器核验的正面结论**：对 16 条 lane 做 packet→durable 行级 diff，**0 条判据被削弱**；3 次 repair pass 只**增加**了自我削弱的表述；R17 正文 SHA256 完全一致。
- **本文件的判断**：这是本次 attempt 最重要的发现，且**不是本 attempt 可以修复的**——修复需要改 `PARAMETER_CONVERGENCE_V0_1.md` §15，属 canonical mutation，本 Work Order 明确禁止。
- **指针**：`17_RED_TEAM_FALSIFIERS.md` §3 F1/F9/F11；`A03_FALSIFIABILITY_HINDSIGHT_AUDIT.md` §0–§4。

### A2. 「有向性」在测量层被确认，但确认出的是**逐构念**的不对称度，不是统一的低不对称 — `empirical`

- **Lanes**：R01（F0-2）、R02（E4 / R4）、R03（F1 / G9）。
- 跨伴侣一致性实测跨度极大：照护者↔被照护者的关系满意度 `r = .43`；**伴侣报告的关系信任 `r = .11`（不显著）**；正向浪漫关系行为 self–other agreement `r = .18` 而 projection `r = .90`。
- R01 推论：不一致 / 不对称度是**构念自身的经验属性**，必须逐构念估计并记录，不能作为全局架构假设。
- **指针**：`02_CONSTRUCT_CONVERGENCE.md` §3.2 前置结论 F0-2；`02b_CONSTRUCT_REDUNDANCY_AUDIT.md` §3.2 边表；`03_MEASUREMENT_INSTRUMENTS.md` §2.4/§2.5。

### A3. `OutcomeDependence`（D8）**理论地位最硬、测量地位最薄**，且关系层级无可用工具 — `empirical`

- **Lanes**：R01（§3.2.9，判 `MEASUREMENT_INFEASIBLE_AT_RELATION_LEVEL`）、R02（E10）、R03（G1）、R10（G1 / G11）、R16（L3 / R16-ID03）。
- R01：唯一被验证的 `SIS` 是**情境级**；Kelley–Thibaut 六维中 `coordination` 一维**不可被稳定知觉**；原文明确「尚无工具测量全部互依子维」。
- R03：`JFTR` 系统综述——**38 个 power/equity/balance 量表各自只被用 1–2 次，无一成为主流工具**；RBA 自己警告「Equal」置中评分无法区分「双方都同等投入」与「双方都同等退出」。
- **跨 lane 后果**：`PARAMETER_CONVERGENCE_V0_1.md` §9 R2 规定 `PowerImbalance` 由 dependence 不对称派生 ⇒ **派生链的两端都缺可靠输入**。
- **指针**：`02_CONSTRUCT_CONVERGENCE.md` §3.2.9；`03_MEASUREMENT_INSTRUMENTS.md` §2.7 + §2.3 缺口表 G1；`10_MUTUALITY_POWER_DEPENDENCE.md` §7/§8 G1–G16。

### A4. 没有一个坐标同时具备「有向边 + 特定 j + state 层 + 第二条独立观测通道」 — `empirical`

- **Lanes**：R03（G9，架构级缺口）、R16（`directionality_class` 枚举）、A02（`Unknown` 值类重复发明）。
- R03 G9 原文：在 R03 审计的全部主流工具中，**没有任何一个坐标有两套独立渠道**（要么自评信念，要么行为/生理）。
- R16 因此新增第二个正交必需字段 `directionality_class ∈ {DIRECTED_EDGE, TARGET_LEVEL, AGENT_LEVEL, PAIR_LEVEL, UNDETERMINED, NON_SEPARABLE}`，并指出 `#29` 的四值 `mapping_status` **不足以**决定一个变量能否支撑方向性主张。
- **R04 的独立佐证**：在 16 个已审计数据集中，**只有 1 个**（速配）提供无外部假设的 `DIRECTED_EDGE` 双分量，而它**没有第二个时间点**。
- **指针**：`03_MEASUREMENT_INSTRUMENTS.md` §2.3 缺口表 G9；`16_EMPIRICAL_VALIDATION_PROTOCOL.md` mapping status / directionality class 两节；`04_DATASET_LANDSCAPE.md` §3.3 G3。

### A5. 「完全公开 + 双报告 + 方向性 + 多波 + 关系状态构念」的**交集为空** — `empirical`

- **Lanes**：R04（结构性负结果）、R16（§10 可执行性）、R05（U5）。
- 「我们能用」与「我们能拿到」在 2026-09 存在一条正在变宽的裂口：`SHARE` 2026-04-30 版 CoU §7 明文禁止把个体级数据交给非自管应用，且**AI/ML 派生量受与原始数据相同的限制**；`Add Health` 明文禁止用 LLM 处理其**任何**数据（public-use 与 restricted 均禁）；`UAS`(CESR) 同禁令；`ICPSR` Redistribution Policy 同方向。
- **指针**：`04_DATASET_LANDSCAPE.md` §3.3 G1/G2；`16_EMPIRICAL_VALIDATION_PROTOCOL.md` access/rights 可执行性节。

### A6. 领域最大规模预注册研究的结论**逆向于**当前工程的优先级 — `empirical`

- **Lanes**：R06（F1 / F2）、R14（N-1）、R16（null B1/B2/B3）、R17（F2）。
- Joel et al. (2020, PNAS)：43 数据集 / 11,196 对 / 2,413 个测量。关系特异变量解释基线**至多 45%**、期末**至多 18%**；**partner 报告在 actor 报告之外几乎无增量**；**关系质量的变化方向大体无法由任何自报变量组合预测**。
- 承载在 `Z(t+1) = F(...)` 上的动态工程（`CURRENT_ARCHITECTURE.md` §12 顺序第 5、6 步）**在 population level 上被这一证据告了一记**。
- **注意这只是 population-level 的方差陈述，不是本体陈述**——R02/R17 均明确不作「partner 侧不存在」的主张。可辩护的最小主张是**存在性/表达性**，不是**增量预测性**；当前项目文档**未做**这个区分。
- **指针**：`06_TRANSITION_LAWS.md` §3 F1/F2；`17_RED_TEAM_FALSIFIERS.md` §3 F2。

### A7. 生理同步**不能**作为 pair-level 关系的代理 — `empirical`

- **Lanes**：R03（F9）、R09（S45）、R10（未主张）。
- 关系结局 meta `ES = 0.09`（`p > .10`，`I² = 76.0%`），且**方向矛盾**：交感 `+0.19` / 副交感 `−0.21`；2026 年综述直说其心理意义仍含糊；一项研究发现 couples' RSA 同步与**自报婚姻冲突正相关**；「恋人 > 朋友 > 陌生人」的预期**被否**。
- **指针**：`03_MEASUREMENT_INSTRUMENTS.md` §2.1 缺口表 G6；`09_DYNAMIC_SYSTEMS_AND_HYSTERESIS.md` §2.6。

### A8. 项目在 refinement / 单调性 / 预序 / 数学格上**完全空白** — `structural`

- **Lanes**：R07（§0.1 全量 grep，1 处无关命中）、A02（`Unknown` 值类被 5 个 lane 各自重新发明）。
- R07 同时指出：R07 自己诊断出「`disputed` 与 `unmeasured` 不可比」（Belnap K4 双序），而其对 sibling 输出的引用数为 **0**。R11、R13、R15、R16 各自**重新发明**了一套 Unknown 分类，无交叉映射。
- **R07 的最强结构性发现**：LHRM 的核心坐标（`Trust`、`Dedication`、`SexualDesire`）**没有 gold standard**；在叙事材料上三者皆无 ⇒ 其「后验」在形式上必须是**不可辨识的分布族**；报告点值不是精度不足，而是**指称缺失**。
- **指针**：`07_PARTIAL_OBSERVABILITY.md` §0.1 / §3 F-07；`18_CROSS_LANE_CONFLICT_AUDIT.md`。

### A9. 迟滞在二元关系数据上的存在性**未知**，且其必要前提在多数真实 dyad 中不成立 — `empirical`（负结果）

- **Lanes**：R09（§3 迟滞诚实回答）、R06（MH2 标 `MODEL_HYPOTHESIS`）。
- R09 给出 5 条可操作判据（`E1`–`E5`），并逐层清点：感觉生理/运动协调层的多稳态**已展示**（受控、极小 N、秒—分钟尺度）；Human Dynamic Clamp **已展示**；**二元关系数据的 dyad 级迟滞：本 lane 未找到任何已发表的估计**。
- 关键：迟滞所依赖的**强耦合前提**在多数真实 dyad 中并不成立（A7 的 `ES = .09`、`I² = 76%`；情绪互依只有 14–38% 的伴侣超出 pseudo-couple）。**不是「我们还没测」，而是「我们测的那个现象在多数 dyad 里不存在」。**
- **指针**：`09_DYNAMIC_SYSTEMS_AND_HYSTERESIS.md` §3（F3.2 逐层表 + F3.3 结论）。

### A10. `MAPPING_FAILURE` 当前**类型上不可达** — `methodological`

- **Lanes**：R17（F1）、A03（T1/T2/T3 独立确认）、A02（cross-check）。
- 三个独立机制：(1) §13 的 10 个映射类含 **3 个 catch-all** + 自由文本 ⇒ `MAPPING_FAILURE` 无路径可走；(2) `AGENTS.md` 诊断清单含 "or merely narrative/irrelevant" ⇒ 每个失败都有合法出口；(3) §14 明说 Step 3 **只测命名不测数值**。
- **A03 的补充（比 R17 更强）**：不是「失败难记录」，而是**准入侧判据 §2.6 结构上无法触发** ⇒ basis 单调增长，从未签发过 `MERGE` / `REJECT`。
- **R17 已写出且已可执行的最小反证实验**（A03 明确建议 parent 执行）：**删掉三个 catch-all，重跑 Fixture 001**。A03 判定这是「唯一还能给本项目一个真实负结果的实验」。
- **指针**：`17_RED_TEAM_FALSIFIERS.md` §3 F1 / §11 优先建议 ②；`A03_FALSIFIABILITY_HINDSIGHT_AUDIT.md` §0 §4.6。

### A11. 「爱 / 亲密 / 嫉妒 / 忠诚」不宜作 primitive 这一立场**不能作为本项目的发现** — `empirical`

- **Lanes**：R14（R7 / F-15）、R01（§3.2 F0-4）、R17（A11 `UNCHALLENGED`）。
- 这是 Sternberg (1986) 三成分、Reis & Shaver (1988)（intimacy = 披露 × 响应的**过程结果**）、Fletcher et al. (2000) **二阶 quality 因子**、Ideal Standards Model 共同持有的立场。
- R01 追加：Hendrick & Hendrick (1989) 合并多套 love 量表做因子分析**未复现任一既有 love 类型学的结构**；Berscheid (2010) 直言「问人们是否爱伴侣，很可能对关系中存在的情感状态及其未来轨迹几乎不具信息量」。⇒ **把「爱 = A+B+C」当作防御 8 维 basis 的理由，等于默认一个已被否证的心理类型学承诺。**
- **指针**：`14_PAPER_POSITIONING_NOVELTY.md` §3.1 R7 / §3.3 F-15；`02_CONSTRUCT_CONVERGENCE.md` §3.2 F0-4。

### A12. 项目自身的 Gate B / cross-context 清单**三处互不相同，且合计漏 5 类 dyad** — `structural`

- **Lanes**：R11（L-8）、R00（gap map）。
- `CONSTRUCT_SCOPE_DIRECTIONALITY.md` §7 第 6 项 / `PARAMETER_CONVERGENCE_V0_1.md` §2.4 / §15 Gate B 三处清单互不相同，且**都不含** `sibling`、`parent–adult-child`、`ex-partner`、`professional/cooperative`、`adversarial/harm-asymmetric`。
- **A03 的独立佐证**：Gate B 要求的 11 类反例中，**5 类在当前 12 份语料里零覆盖**（same-sex / kin / 非浪漫友谊 / caregiving / high-dependence-low-liking）。
- **后果**：**Gate B 通过不构成「跨域稳定」的证据。**
- **指针**：`11_GENERAL_HUMAN_DYADS_SCOPE.md` §2.3 L-8；`A03_FALSIFIABILITY_HINDSIGHT_AUDIT.md` Gate B 节。

---

## 2. Unresolved contradictions（需要 Human / Architect 裁决，本 attempt 不裁决）

> 完整证据链见 `18_CROSS_LANE_CONFLICT_AUDIT.md`。此处只登记**最高优先级**项。

### C-1（阻塞级）`PPR` 的层归属三方互斥

| 主体 | 立场 |
|---|---|
| R01 | `PPR` 判 `BELIEF_ONLY`（perception ≠ state；引 Ackerman 2021「感到被理解与实际被理解只有中等相关」） |
| R17（F3） | **主张升入 state 层**——Segal & Fraley (2016) 原文称 PPR 是 `organizing variable`，驱动投资模型各构念的协变；Joel (2020) 最强 predictor 是 **perceived** partner commitment |
| R06 §4.9 | 其 `MEASUREMENT_NULL` 判据**预设** `Z` 与 `PPR` 必须分层——**一旦 R17 落地，R06 判 B4 在类型上失效** |
| R14 §2.1 | 把「PPR 属 Belief 层」当作**已确立的 prior art** 写进 R4 复用表 |
| 当前 canonical | `PARAMETER_CONVERGENCE_V0_1.md` §5 `B1` 判 Belief layer |

**这不是构念清单的错，是相空间选错**（R17 原文）。**若采纳 R17，R06 五族按其自身非主张条款必须全部重新推导**（A02 标为 U-9「下游爆炸半径」）。

### C-2（阻塞级）`OutcomeDependence` 被四种互斥 ontology 指派

directed 心理状态（D1–D8 原判定）/ `Ω(S)` 情境结构 readout（R10）/ pair 累积存量（R06 `APES`）/ 结构化估计而非问卷估计（R01）。它是**唯一**支撑 `PowerImbalance` 派生链的候选（见 A3）。

### C-3（阻塞级）Gate A/B/C 的可证伪性

见 A1。修复需改 canonical，本 Work Order 禁止。

### C-4（阻塞级）`Unknown` 的类型学

R07 给出诊断（K4 双序、`disputed` vs `unmeasured` 不可比）与 5 类传播规则；R11 / R13 / R15 / R16 各自另立一套。**四条 lane 之间零交叉映射。** 需要一次统一的类型学裁决。

### C-5（排序死锁）U-5：Gate C 的前置条件与 Gate C 本身互锁

R11 U1 要求 invariance 序列**在 Gate C 之前**完成；R05 I11 判 cross-context test `BLOCKED_BY_DATA`（需构念×角色×情境×文化的正交交叉设计，当前数据源不满足）⇒ **Gate C 停摆**。

### C-6（尺度冲突）CR-7

R06 的 C-A 约束要求**事件内分辨率**（否则无法分离「对方行动改变了我的状态」与「同一测量窗口内共同生产」）；R09 O8 提议把 `tau` 固定在月—年级并拒绝该词汇；而 R03 的仪器台显示**月—年级尺度上根本没有 `Trust` / `Dedication` 的 state 工具**。三者不可能同时满足。

### C-7（已定案的引用冲突）`10.1177/0146167205276865`

Crossref 实时核验（2026-09-27）：= Sibley, Fischer & Liu (2005), *PSPB* 31(11):1524–1536 ⇒ **R01 正确、R03 错误**。该数字是 R01 §3.6 / R02 E16 / R10 G14 的决定性依据。**本项已由 A02 裁决并已按 R01 记录，无需再议。**

### C-8（审计互斥，已由实测裁决）A04 与 A01 的 OSF 前缀判定相反

- A04 主张 `10.31234/osf.io/…` 前缀/后缀结构非法，应改为 `10.31219/…`。
- 修复 child 实测：`10.31234/osf.io/dus42` → **302 解析**；`10.31219/osf.io/dus42` → **404**。`10.31234` 是 OSF-preprint 前缀，`10.31219` 是 OSF **project** 前缀。
- **裁决**：`10.31234` 正确，**未改**。这是本次 attempt 内**审计结论被实测推翻**的一例，记录为流程观察：**审计 child 的断言必须经独立实测复核后才能落到 durable artifact。**

---

## 3. Strongest red-team findings（R17 + A03）

R17 独立起草（首稿在任何 lane 报告写入之前完成，独立性 CONFIRMED），共裁定 23 条假设：`CHALLENGED` 8 · `CONTESTED` 8 · `UNCHALLENGED` 3 · `NO_EVIDENCE_FOUND_FOR_CHALLENGE` 2。

| # | 发现 | 破坏了什么 | 可定案的具体观察 | 独立复核 |
| --- | --- | --- | --- | --- |
| **R17-F3** | 层边界被经验文献**反向排序** | LHRM 把经验文献认定为因果最近端的两个变量（`PPR`、`Satisfaction`）都降级了 | 同一 dyad 上同时测 belief 与 state；若 belief 层的协变领先于 state 层则层位反了 | 见 C-1 |
| **R17-F1/F9/F11** | Case Bank 目前**不是测试** | 三个独立机制 | 删掉三个 catch-all 后重跑 Fixture 001，看 `MAPPING_FAILURE` 是否变得可达 | A03 独立确认（T1/T2/T3） |
| **R17-F2** | Joel 2020 的五条结论 | 动态工程（工程顺序 5/6）与增量预测主张 | 5/5 top predictor 落在 `DirectedRelationshipState` **之外** | R06 / R14 / R16 独立采用 |
| **R17-F7** | 验证工具对目标现象的一部分**原理上盲** | 文本 benchmark 可 100% 覆盖而与真正驱动现场行为的层完全无关 | Eastwick (2011)：隐式 vs 显式吸引力偏好 `r = .00`，且显式偏好只预测照片、不预测现场 speed-dating | — |
| **R17 A6** | `Gate B` 的 11 类反例就是项目自己的假设列表 | 跨域稳定性门是同义反复 | 逐条核对清单文本 | A03 修正为 8/11，方向不变 |
| **R17 A14** | `Reality ≠ Observation ≠ Belief` 的**分离**存活，但**排序**被推翻 | 层位顺序 | — | A03/R14 一致 |
| **A03 H-4** | 存在**两条平凡通过路径**（全弃答 / 复制 fixture status 列）使 R13 的六个 faithfulness 指标全部最大化 | 指标的区分力 | 构造这两条路径并验证指标是否真的最大化 | A03 独立 |
| **A03 §2.6** | 唯一能删除 construct 的准入侧判据**结构上无法触发** | basis 单调增长；`MERGE`/`REJECT` 从未签发 | 检查该判据的分支覆盖 | A03 独立 |

**R17 攻击失败、明确站在项目一方的 3 条**（R17 自己记录，红队不说假话）：
- A10 `State ≠ Action`：Hui et al. (2014) Manhattan Effect 反而**支持**它。
- A11 拒绝「爱/亲密/嫉妒/忠诚」为 primitive：攻击不动。
- A12 Unknown 显式化：三个 fixture 构成真实压力测试并通过。

**R17 未能找到反证、如实登记为 `NO_EVIDENCE_FOUND_FOR_CHALLENGE` 的 2 条**：`OutcomeDependence`（项目自标 open question，诚实）；`Liking` vs `RomanticAttraction`（R17 判断 Sternberg (1987) 的存在本身即分离证据）。

**R17 对本项目最有价值的一句判断（parent 保留为待议观点，非结论）**：
> 最可辩护的项目是「带显式知识时间与 provenance 的 dyadic claim 证据表示语言」；最不可辩护的是「人类关系的 8 维潜在状态 basis」——后者是对一个 40 年过程模型的重新推导，测量姿态更差，且无数据。**LHRM 目前把可信度预算花在了后者上，而它本可以低成本地花在前者上。**

---

## 4. Candidate empirical laws worth later freezing（3–5 条，**候选**，非已冻结）

> 全部为 `RESEARCH_CANDIDATE`。**无参数、无权重、无阈值、无拟合。**
> 每条都带预登记的证伪判据。冻结需 Human 授权的**独立** Work Order；本 Work Order 明确禁止拟合与冻结。

| id | 律 | 一句话 | 关键支持 | 必须击败的 null | 证伪判据（预登记） |
| --- | --- | --- | --- | --- | --- |
| **L1** | `BMR` Belief-Mediated Responsiveness | `i` 的有向状态**只**经由 `i` 对 `j` 行为的**解释**移动；归属在门控符号与门控强度两处起作用 | Laurenceau 1998/2005（PPR 为部分中介，96 对 × 42 天双报告） | `AR_ONLY` / `NO_PARTNER` / `ACT-NOT-BELIEF` / `NO-ATTRIB` / `MEAN-REV-ONLY` | `NO-ATTRIB`（去掉归属门控）与完整版拟合相同 ⇒ 核心主张被削弱 |
| **L2** | `APES` Actor–Partner Exchange with Stock | 满意度–替代品–投入驱动一个**积累的** dependence 存量；dedication 是其下游读出 | Le & Agnew 2003（52 研究，≈2/3 方差）；Rusbult & Martz 1995（受虐关系中 commitment 仍高） | `B1` persistence / `B2` selection-only | 完整版**未能击败** `AR_ONLY` ⇒ 该律退化为自回归，拒绝其作为独立律族 |
| **L3** | `DVA` Deterioration vs Actualization | 评价读出的下降由两个**可分离**机制产生：起点选择 + 个体内实际化 | Johnson 2022（LCM-SR，双方非零自回归 + 交叉滞后，**无性别差异**）；Lavner 2012（**初始差异胜出**，对增量模型「limited evidence」） | `B2` selection-only（稳定 per-dyad 截距） | **注意**：最佳可得证据**逆向**于本律的增量通道。冻结前必须先解释这一冲突 |
| **L4** | `RGM` Reference Gap and Movement | 同一对方行为可经**两条通道**缩小 gap：改变 Actual，或移动 Ideal | Drigotas 1999（Michelangelo 现象，4 研究）；Pusch 2023（response surface，Actual/Desired 双侧有害） | `B1` / `B5` label-only | 两条通道无法在同设计中分离（各自解释 <50% 共享方差）⇒ 拆成两条单通道律 |
| **L5** | `RT` Rhythm and Threshold（双分支） | 事件级互动有**两条分支**：放大（`Λ⁺`）与抑制/修复（`Λ⁻`）；分支由 dyadic state 决定 | Schrodt 2014（74 研究 / 14,255；两个方向的 r 近乎相同：.380 vs .392）；Gable 2004（capitalization 的**独立正向**支持）；Rusbult 1991（accommodation） | `B1` / `B3` no-partner | 性别不对称的耦合被检出（**当前最佳证据反对**）⇒ 律族须重写 |

**为什么只列 5 条而不是更多**：R06 交付 5 族；R16 已为每族给出对应的 leakage 规则（L1–L8）与 null（B0–B6）；R05 已给出每族对应 Q1–Q10 中哪几个**在当前数据下不可识别**。**再加律族不会增加信息，只会增加不可检验面。**

**R06 明确列为「当前不可证伪」的律族**（点名比隐藏更有价值）：依赖 `U-1`–`U-8`，其中 `U-3`（关系终止的删失偏差）被 R16 升格为**最严重的结构性盲点**——离开的人停止作答，因此**任何关于「关系最重要的一次转移」的律在受访者数据上都不可证伪**。

---

## 5. 最佳 dataset 候选（8 条，全部来自 R04 的 16 份审计）

> **零数据接触。** 全部判断基于官方文档与元数据。「能用」与「能拿到」分列。

| id | 数据集 | 能识别 | **不能**识别 | 分类 | 2026-09-27 access |
| --- | --- | --- | --- | --- | --- |
| **D01** | **pairfam**（德国，ZA5678，14 wave） | anchor↔partner 双报告方向性分量；`relstat`/`marstat`/`homosex` 提供的**关系类型与制度状态分离**；关系生命史 | 非共居 partner 的独立测量；跨文化（仅德国）；两套 instrument 跨波模块不全覆盖 | `CALIBRATION_READY` | 免费 + 签署 user contract |
| **D02** | **SHARE**（欧盟 27+ 国，≥8 完整 wave） | `mergeidp*w` + `coupleid*w` 完整双报告 dyad；SHARELIFE 回溯生命史 | 50 岁以下 partner；非同住 / 从未受访 partner；部分模块单方 respondent ⇒ 该模块 `directionality_class = UNDETERMINED` | `CALIBRATION_READY` | 免费 + User Statement；**CoU §7 禁止非自管应用，AI 派生量同受限** |
| **D03** | **HARP**（美国，ICPSR 37404，3 时点 + 各 8–10 天日记） | 双配偶**分开作答**；稀疏面板内嵌 intensive longitudinal；关系质量 + 日常压力 + 互动 + 健康行为同时双报告 | 离婚/分居后的**新关系**；非已婚/未婚关系；T1→T3 couple 层流失 ≈36%；**同性与异性抽样框不同**（同性经州 Vital Records 邮寄约 70%，异性因该登记处限制改用城市名单约 40%） | `CALIBRATION_READY` | ICPSR 公版（本环境 403，构造性不可达） |
| **D04** | **Fisman & Iyengar speed dating** | 同一 dyad 上 `dec`（i 想再见）+ `match`（互惠）⇒ **方向性不对称最干净的公开标定集** | **任何**时间演化；outcome 只有「想不想再见」；`wave` = 场次非重复观测；异性恋单性；无官方 missingness 文档 | `MEASUREMENT_ONLY` | **完全公开**（GitHub / OpenML / OSF，2026-09-27 HEAD 200） |
| **D05** | **DHS Couples (CR)** | 双方自述配对后链接；官方直接以 couple 为分析单位并计算配偶年龄差；约 90 国 ⇒ 跨文化最强 | 任何纵向（每国单轮）；非 co-resident 配对；**部分轮次因 Men's Questionnaire 未记录配偶 line number 而根本生成不了 couples 文件** | `MEASUREMENT_ONLY` | 免费 + 授权申请 |
| **D06** | **IFLS**（印尼，5 wave） | household head + spouse 均受访；`BA` 非同住亲属 + `TF` 亲属转移 ⇒ 非浪漫 dyad 与照护流动 | **跨波 partner id 未核实** ⇒ 方向性依赖重建假设 | `MEASUREMENT_ONLY` | 免费 + RAND 注册；"Please do not distribute" |
| **D07** | **NSFH**（美国，3 wave，多成员访谈） | 亲子、跨代、同住非婚 dyad；极完整的关系/同居/离婚/再婚/继亲生命史 | **配偶间关系质量是单方报告** ⇒ **不能**识别 `i→j` vs `j→i`；无同性婚姻 | `MEASUREMENT_ONLY` | ICPSR 公版，无需会员机构 |
| **D08** | **CLOC**（美国，4 wave，丧偶） | `Couples Only` 数据集（Part 5）**同时含妻（V）与夫（S）在全部 4 wave 的数据**，423 对 | **只有丧偶者 + 匹配对照被随访** ⇒ 存活-与丧偶-条件化选择；非一般婚姻样本 | `MEASUREMENT_ONLY` | ICPSR 会员机构限定 |

**明确排除（权利或抽样框）**：Add Health、UAS、American Family Cohort、Oregon Youth Study Couples Study（`ACCESS_BLOCKED`）；SOEP（`NOT_DYADIC_ENOUGH`，构造后「we do not find any same-gender couples」）。

**R04 的结构性发现（比任何单个数据集的优劣都重要）**：**这四个条件的交集为空。** 因此 `#29` F 层要求的**跨数据集泛化在结构上不可执行**。

**R15 的 Case Bank 侧**（与定量数据集**不重叠**）：`15_CASEBANK_EXPANSION.md` 交付 22 条 narrative + 3 条 calibration + 4 条 tooling + 1 条分离，Wave A 的 3 份（N02 `H v H` [2022] UKPC 3、N16 *The Mill on the Floss* Book 3–7、N06 `Dougherty v Dougherty` [2015] EWCA Civ 805）**已实测可立即开工且不依赖任何待确认项**。

---

## 6. Measurement gaps

### 6.1 架构级缺口（无工具，不是「工具不够好」）

| id | 缺口 | 出处 |
| --- | --- | --- |
| **G1** | `OutcomeDependence_(i→j)` —— 关系级**无可引用 validated 工具**；power 族 38 个量表各用 1–2 次 | R03 |
| **G2** | `Trust_(i→j)` 的**更新事件** —— 全部 level 型、回顾性自评、无时间戳 | R03 |
| **G3** | `Dedication` 与 constraint commitment 的分离 —— IMS 在**定义层**就合并了 investment + alternatives + satisfaction | R03 |
| **G6** | `Cohesion_(A,B)` 作为 shared latent —— 只有 i-perception；**没有任何工具能裁决「谁更 cohesive」** | R03 |
| **G9** | **无任何坐标具备两条独立观测通道** | R03 |
| **G10** | 依恋的 **state 层** instrument —— 主流工具是 trait | R03 |

### 6.2 方向性能力缺口

- R03 F1：ECR / ECR-R / RSQ / AAS / AAQ / VFI / HISD / 3VDI / Interpersonal Dependency / Personal Sense of Power / Reiss RPS / Romantic Beliefs Scale **全部测 `i` 的一般倾向或对一般他者的态度**。「ECR-R 是 directed measure」是**改写指令的决策，不是工具属性**，且改写后 IRT 标定是否仍有效未审。
- R03 F3 的一条实测发现直接冲击 Gate C：**DTS 的 Female 对 partner 的 love `r = .23` 显著，Male 的 `r = −.06` (n.s.)**；作者解释为「信任在依赖度低的一方更关键」⇒ **`Trust_(i→j)` 的值本身依赖 `i` 的 dependence**。这是 Trust 与 OutcomeDependence 在**测量层**纠缠的首个实测证据。
- R02 E4：Trust 与 AttachmentSecurity 不是「两个独立 primitive」，而是**一个共享 felt-security/benevolence 内核 + 两个非零残余**（trust 的定义本身含 emotional security；benevolence referent 直接含 responsiveness/caring），但 attachment–trust 实测仅 `r = −.23 / −.31`。
- R10 F1：mutuality 必须在 **SRM 残差**上计算，不是原始边聚合；asymmetry 应当是**带显式声明比较器的比较关系**而非标量（否则与 `AGENTS.md` invariant 4 直接冲突——区间/序数/类别/Unknown 空间上 `distance` 未定义）。

### 6.3 不变性缺口

- R11：24 × 10 矩阵共 **216 个判定格，其中 69 个 `MEANING_PRESERVED`，支撑它的 invariance 研究数 = 0**。这 69 格**不可计数、不可聚合、不可视为独立**；若 `U1` 失败，相关格必须**重做**而非重新标度。
- R03 N6：ECR 两维度「正交」是**工具假象**——CMB 方法因子可把理论正交的 anxiety–avoidance 相关从 `.17` 推到 `.41`。
- R16：`invariance_level_tested` 不得默认为 `NOT_TESTED` 而不显式标注；`#29` 分层与 R16 协议一致，但两者都**未**执行。

### 6.4 语言与文化覆盖缺口

- R13：LHRM 现有 126 条 proxy **无一条有跨语言不变性证据**。跨语言模型可能在**无告警**的情况下把 proxy 归到错误构念上（实测：专建多语模型在被问哈萨克语时**输出吉尔吉斯语**）。
- R02（repair 后）：中文覆盖从 0 增至 5 条来源，其中 3 条带可核实数字，但**没有一条能承载裁决**；中文的 Liking↔RomanticAttraction、trust↔attachment-security、dedication↔satisfaction 三处估计**均未找到**。
- R11：3 处 `cross-cultural` / cross-jurisdiction 域泄漏无 invariance 支撑。

---

## 7. Recommended next Work Orders

> 全部为 `AI recommendation`。排序依据：**修起来便宜 / 收益大**。**均不属本 Work Order 授权范围**，需 Human 授权后另行派发。

### 优先级 1 — 让验证门能够失败（**这是唯一的真正阻塞项**）

**WO-N1｜Gate A 可证伪性修复 + 首次真实否决尝试**
- 内容：删掉 §13 的 3 个 catch-all 映射类与自由文本出口；把 §2.6 改写成**可触发**的准入侧判据（含至少一条 `MERGE` 与一条 `REJECT` 的判定规则）；重跑 Fixture 001。
- 依据：R17-F1 / A03（`§2.6` 结构上无法触发；两条平凡通过路径）。
- 变更面：`docs/foundation/PARAMETER_CONVERGENCE_V0_1.md` ⇒ **canonical mutation，本 Work Order 明确禁止**。需 Human 显式授权。
- **这是 A03 判定「唯一还能给本项目一个真实负结果的实验」。**
- **建议同时补上**：`UNKNOWN`（材料不足）vs `MAPPING_FAILURE`（材料充分但表示装不下）的分离记账——R07 的 C1 吸收规则已给出可检查形式。

### 优先级 2 — 层位裁决（阻塞后续一切推导）

**WO-N2｜`PPR` / `Satisfaction` 层归属裁决 + 连带重新推导**
- 内容：Human / Architect 裁决 C-1；若采纳 R17，须同时授权 R06 五族的**重新推导**（不是重新拟合）。
- 依据：R17-F3；R06 §4.9；R14 R4；A02 U-9。
- 变更面：`PARAMETER_CONVERGENCE_V0_1.md` §5/§9 ⇒ canonical mutation。

**WO-N3｜`Unknown` 类型学统一**
- 内容：以 R07 的 K4 双序 + 10 类 tag + C1–C6 传播规则为基线，吸收 R11 / R13 / R15 / R16 各自的分类，产出**单一受控词表**。
- 依据：A8；A02（4 lane 零交叉映射）。
- 变更面：`AGENTS.md` + `CURRENT_ARCHITECTURE.md` §9 ⇒ canonical mutation。

### 优先级 3 — 采样与语料（可与优先级 1 并行，且不需要 canonical 变更）

**WO-N4｜Case Bank Wave A 冻结**
- 内容：冻结 R15 的 3 份（`H v H` [2022] UKPC 3 / *The Mill on the Floss* Book 3–7 / `Dougherty v Dougherty` [2015] EWCA Civ 805），并落实 `#13` comment 2 的 `t0` / `INPUT|HOLDOUT` 分离。
- 依据：R15 Wave A；R15 明确「这 3 份不依赖任何待确认项」。
- 变更面：`docs/validation/fixtures/` ⇒ **不是** foundation doc，但仍是 canonical 面。需 Human 确认。
- 附：R15 同时提出 `DERIVED_TRANSFORM`（T1–T5）作为新 fixture 类——**这是 Human 决定**，本 attempt 不主张。

**WO-N5｜Gate B 覆盖矩阵发布 + 清单对齐**
- 内容：发布「12 份语料 × Gate B 11 类反例」覆盖矩阵；把三处互不相同的 cross-context 清单合并为一份，并补入 R11 指出的 5 类缺失 dyad。
- 依据：R11 L-8；A03 Gate B（5 类零覆盖）。
- 变更面：新增研究文档 + 可能的 foundation 清单 ⇒ 前者可做，后者需授权。

### 优先级 4 — 测量（需要网络出口，不是需要设计）

**WO-N6｜数据集出口核实 + 构念内容核实**
- 内容：在**可访问 ICPSR / `pairfam.de` / Gutenberg / `wenshu.court.gov.cn` / `courts.ie` 的网络环境**下，核实三份 `CALIBRATION_READY` 数据集实际**问了哪些关系状态构念**（R04 `U15`，这是 A4/A5 能否推进的唯一钥匙），并重跑 R15 §3 全部核实。
- 依据：R04 `U15` / blocker B-1；R15 `U6`。
- **不得**以任何方式绕过 access / rights（Work Order 明确禁止）。

### 优先级 5 — 投影层（低成本、条件新颖性最高）

**WO-N7｜以 `CITED_PRIMARY` 复核既有 fixture 的 LHRM 映射**
- 内容：把 3 份已冻结 fixture 跑一遍 LHRM 映射，作为**可执行的首次 falsification 尝试**；R17 R3 写出的「唯一命题」（写不出就诚实降级为知识表示产物）是其候选。
- 依据：R17 §11 优先建议 ⑤；R14 NC-1；R13 的 6 个 representation-faithfulness 指标。
- **前提**：WO-N1 必须先完成，否则跑出来的是又一次不可否决的覆盖。
- **注意 R13 的度量立场**：「抽取准确率」在本项目**无定义**（无 ground truth）。可用的替代是 6 个 `representation faithfulness` 指标，且必须**同时报告 `CROSS_RUN_DISPERSION` 不得被当作精度**。

### 优先级 6 — 定位（若考虑对外表述）

**WO-N8｜prior-art 定位补验**
- 内容：核实 R14 自标的最高优先未验 prior art（`Acitelli & Antonioni (2006)` 关系科学的维度化方案；`Boyd & Heewer (2007)`），因为二者直接威胁「最小充分有向基」与「representation over prediction」的新颖性。
- 依据：R14 `N-13` / U1–U2。R14 与 A04 均记录检索未命中。
- **在此之前不得对新颖性做任何表述。**

---

## 8. 未解 blocker（终态）

| id | blocker | 可否由本 attempt 修复 |
| --- | --- | --- |
| **B-1** | 网络出口不可达（`icpsr`403 / `hrs` / `saflii`403 / `courts.ie` / `wenshu` / `gutenberg`）⇒ 三份 `CALIBRATION_READY` 的**构念内容**未核实；R15 的 7 条来源仍 `UNVERIFIED_CANDIDATE` | **否**。Work Order 禁止绕过 access / rights |
| **B-2** | R11 的 Gilligan/Kleemans/Rodriguez (2017) ASR 记录经 10 路检索**确认不可得** | **否**。已记为永久缺口 |
| **B-3** | R02 的「全候选电池单次 ESEM/bifactor」是**真实文献负结果** | 不适用（负结果，非缺口） |
| **B-4** | 迟滞在二元关系数据上无任何估计 | 不适用（负结果） |
| **B-5** | `#20/#21/#22` 隔离 lane 的 durable 结果仍未知 | **否**。按隔离契约本 attempt 不查 |
| **B-6** | Gate A/B/C 在当前定义下**不能产生否决** | **否**。需改 canonical，本 Work Order 禁止 |
| **B-7** | `Liking ↔ RomanticAttraction` 仍缺**同样本斜交因子相关 / CFA 判别检验**（R02 repair 后仍如此） | 需专门设计研究 |
| **B-8** | `OutcomeDependence` 关系级可测性无任何公开工具 | 需专门设计研究 |

**本次 attempt 自身的方法学缺口（诚实记录）**：
- 跨 lane **全局去重**已由 A04 完成（1,199 原始出现 → 642 distinct pointer → 533 distinct source，其中 `PEER_REVIEWED_*` **350**）。**各 lane 自报数相加 ≈1,201 不成立，高估 2.3–3.4×。** 因此**不得**对外声称「1,201 个独立来源」。
- A04 与 A01 各自的 DOI 抽样**不重合**，两次审计的合并覆盖率未单独计算。
- 报告体量的**最小可解释性**：`02b` 的多数结论依赖 `R04`/`R06` 的 sibling 输出，而 R04 与 R06 之间**从未互相读取** ⇒ 存在一条未被任何单点研究覆盖的依赖链（A02 已标记为 CR-7 尺度冲突）。

---

## 9. 本文件明确不主张

1. **不主张** 本文件或本目录下任何文件是 canonical architecture、参数表、公式 SSOT、schema 或验证依据。
2. **不主张** §1 的任何 `A*` 收敛条目为「已确立」。它们记录的是**多条独立文献线指向同一处**，不是该处为真。
3. **不主张** §4 的 5 条律为真。`L3` 的最佳可得证据**逆向**于其增量通道，这一点必须在冻结前解决。
4. **不主张** §5 的数据集**已被获取、已下载、已打开或已跑过映射**。全部为 suitability 描述，零数据接触。
5. **不主张** §6 的任何缺口可由「多找几个量表」关闭。G1/G2/G3/G6/G9 是**架构级**缺口。
6. **不主张** 本 attempt 的文献数量、child 数量或一致性构成任何形式的 validation。
7. **不主张** 本 attempt 对 §2 的任何矛盾作出了裁决。**全部留给 Human / Architect。**
8. **不主张** `AGENT_RECALL` / `UNVERIFIED` / `POINTER_ONLY` 级来源可承载任何裁决。
9. **不主张** 本 attempt 读取、执行或引用了 LHRM `#20` / `#21` / `#22` 的任何内容；未写 Eye / Juece；未做 merge。
10. **不主张** R17 的项目取舍判断（§3 末段）是结论。它是**一个独立红队的保留意见**，采纳与否属 Human。
