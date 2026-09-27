# 18 — 跨 Lane 矛盾 / 重复审计（Cross-Lane Conflict Audit）

**Status:** `RESEARCH_CANDIDATE` / NOT CANONICAL
**As of:** 2026-09-27
**Lane:** A02（Wave 2，join lane）
**Work Order:** `youling/lhrm#30@overnight-opencode-exploration-swarm-v1`
**Input docs（只读）:** `AGENTS.md`、`docs/foundation/CURRENT_ARCHITECTURE.md`、`docs/foundation/CONSTRUCT_SCOPE_DIRECTIONALITY.md`、`docs/foundation/PARAMETER_CONVERGENCE_V0_1.md`、本目录 Wave 1 全部 18 份报告（`01_` – `17_`）

> 本文件**不是** canonical architecture，**不是**参数表，**不是**已确立结论。
> 本文件**不修改**任何 canonical doc，也**不修改**任何 Wave 1 报告；所有 `NARROW_REPAIR_REQUEST` 都是给 parent / Architect 的**文本级建议**。
> 本文件**不主张**任何冲突裁决改变了 ontology、层归属、参数、权重或公式。
> 本文件**没有**读取 LHRM issue `#20` / `#21` / `#22`；**没有**触碰 Eye / Juece / Juece `#30` / PR `#31`。

---

## 0. TL;DR

1. **Wave 1 的实际拓扑是「17 条独立单点研究 + 1 条 join lane（R16）」，不是一次协作。** R16 报告含 60 行 sibling-lane 引用，R03 有 10 行，R06 有 4 行，R08b 有 3 行；**R01 / R02 / R04 / R07 / R12 / R13 / R14 / R15 各 0 行**。R17 与 R05 都明文声明未读 sibling 产出。**因此本报告发现的绝大多数「跨 lane 分歧」不是意见冲突，而是从未被放在同一张桌子上比较过。**
2. **全 swarm 在「什么不能做」上高度一致，在「什么该做」上分裂。** 10 条强收敛**全部是否定性 / 限制性主张**。真残余分歧集中在 9 处，全部在**「该保留什么 / 该归哪层」**。
3. **最高优先级的三条冲突**：(a) `PPR` 的层位有**三种互斥处置**（R01 `BELIEF_ONLY` / R17 升入 state 层 / R06 的判据预设二者必须分层），而 R14 把这场争议当作不存在；(b) `OutcomeDependence`（D8）被**四种互斥 ontology** 指派，而它是**唯一**支撑 `PowerImbalance` 派生链的候选；(c) `Unknown` 值类被**五个 lane 各自重新发明**（R07 / R11 / R13 / R15 / R16），零交叉映射，而 R07 自己已经诊断出这个问题。
4. **三条任何单 lane 都不可能发现的跨 lane 后果**：(a) **排序死锁** —— R11 U1 要求 invariance 序列在 Gate C 之前完成，R05 I11 判定 cross-context test `BLOCKED_BY_DATA`（U-5）；(b) **下游爆炸半径** —— R17 R2 若被采纳（层归属改变），R06 五族按其自身 §11 非主张 3 必须**全部重新推导**（U-9）；(c) **律 E 尺度冲突** —— R06 C-A 要求事件内分辨率，R09 O8 提议把项目 `tau` 固定在月—年级并拒绝该词汇（U-3 / CR-7）。
5. **R03 的 instrument + R04 的 dataset + R06 的 law + R16 的 protocol 不能整体执行。** 11 条具名不可满足要求。**唯一值得做的实证**是：在 pairfam / SHARE 上用 `G1_BLOCKED_FORWARD` 问一个纯预测问题——「`PPR`（Belief 层读出）是否比 `Trust`（directed 读出）更能预测 `satisfaction` 读出？」它的结果直接裁定冲突 (a) 与 (b)。
6. **R01 与 R02 重复执行了 Gate C，且在 4 / 6 个攻击面上给出了不同答案**；**R01 与 R07 也重复了「层 / 值类裁决」，且 R07 的诊断从未被消费**（§3）。
7. **本报告明确记录了 4 处 `COMPATIBLE`**（Gate B 可执行性、终止 / 存活偏误、ABM 先例、`r = .11` 的解读），以履行「不制造矛盾」的义务。

---

## 1. 方法与判定码

### 1.1 本 lane 只裁决「相容性」，不裁决「真伪」

本报告的每一条 A/B 两侧引文都是**对 durable 报告正文的逐行引用**。因此：

- 「该 claim 存在」是 `CITED_PRIMARY`（本地实读）；
- 「该 claim 为真」**不由本报告裁决**——那是 A01（证据质量）与 A04（引用 / provenance）的职责；
- 本报告只裁决：**这两条 claim 是否能同时为真**。

### 1.2 不兼容性质（`incompatibility_kind`）

| 码 | 含义 |
|---|---|
| `定义冲突` | 同一构念在两个 lane 拿到不兼容的定义 / 语义边界 |
| `经验冲突` | 两个 lane 关于同一文献或同一数据集断言不兼容的经验事实 |
| `范围冲突` | 两个 lane 的主张都成立，但被放在不重叠的 scope 里而无人调和；或对同一现象的**缺口类型**分类不同 |
| `层冲突` | 同一个量被分配到不同的 schema 层（`Agent / Directed / Pair / Belief / Constraint / Action / Derived`） |
| `要求冲突` | 两个 lane 的数据 / 协议 / 验证要求不能同时满足 |
| `记账冲突` | 推理一致，只是数字 / 标签 / 指针未同步 |

### 1.3 构念碰撞判定枚举

`SAME_CONSTRUCT_DIFFERENT_NAME | GENUINELY_DISTINCT | OVERLAPPING_NEEDS_SCOPE_RULE | UNRESOLVED`

### 1.4 本 lane 做的独立核验

Crossref REST API，2026-09-27 实时查询。1 次 DOI 身份核验（CR-1，命中）+ 2 次辅助查询（其中 1 次为负结果，NR-1）。

---

## 2. 冲突登记（Conflict Register）

### CF-00｜先行统计：swarm 内部引用的实际拓扑

| 观测 | 数值 | 出处 |
|---|---|---|
| 含 sibling-lane 引用的行数 | R16 = **60**；R03 = 10；R06 = 4；R08b = 3；R00 / R05 / R09 / R10 / R11 / R17 各 1–2；**R01 = R02 = R04 = R07 = R12 = R13 = R14 = R15 = 0** | 全 18 份报告逐行扫描 |
| R17 主动不读任何 sibling 产出 | 明文枚举 | `17_RED_TEAM_FALSIFIERS.md:15-43` |
| R05 明文声明不读 sibling 结论 | 「不主张 R03 / R04 等 sibling lane 的结论。本 lane 未读 sibling lane 输出。」 | `05_IDENTIFICATION_AND_STATISTICS.md:466` |

**读法**：Wave 1 的实际结构是**独立单点研究 + 一条事后 join lane**。因此下文每一条冲突的**修法**大多是「加一句限定语 / 改一个枚举 / 加一条指针」，而不是「重做研究」。

---

### CF-01｜`Dedication` 的层位：四条互斥主张

| 项 | 内容 |
|---|---|
| **Lane A（R01）** | §3.8 裁决：**`KEEP`（定义为 `Dedication`）**，强制条件是「必须声明是否含 satisfaction 成分（否则与 §9 R3 冲突）」。`02_CONSTRUCT_CONVERGENCE.md:212`，速览表 `:275` |
| **Lane B（R02）** | §5.2：**「LHRM 当前的分类很可能反了」**——按未解释方差排序，`Dedication` 是被三个 LHRM「或有或无的构念线性解释了 54% 的那个量」，而 `Satisfaction` 的未解释方差才是未知项；建议标 `CONTESTED_PRIMITIVE`，并要求任何「dedication 有独立波动」的辩护必须在**控制 satisfaction + investment + alternatives 之后**提出。`02b_CONSTRUCT_REDUNDANCY_AUDIT.md:288-301`（H2 判 `CRITICAL`：`:376`） |
| **Lane C（R06）** | 律 B `APES` §5.1：`Ded(tau+Delta-tau) = Psi(D^d, Inv, Alt, Std, GapB)`——`Dedication` 是**一个累积 dependence 存量的下游读出**。并要求 R02 优先裁决「判 E 若成立应**删除** `Dedication` 这个候选 primitive」。`06_TRANSITION_LAWS.md:285-296`、`:998-1000` |
| **Lane D（R17）** | F10 T1：`Dedication` **既是 primitive，又在源理论里是函数**（Investment Model 的定义式由 satisfaction + investment − alternatives 给出），而 LHRM 对 `Power` 做了派生处理——「**同一份文件里两种处理**」。A15 裁定 `CONTESTED`。`17_RED_TEAM_FALSIFIERS.md:327`、`:374` |
| **`incompatibility_kind`** | **层冲突 + 经验冲突** |
| **R01 自己的记录** | §6 audit delta #3 已把这条记为「prior report **内部不一致**，需二选一」并上交 Architect（`02_CONSTRUCT_CONVERGENCE.md:355`）。**R01 不是没看到冲突，是看到了并把它升级了。** |
| **判定** | **`UNRESOLVED`**，但 3:1 偏向「标 `CONTESTED_PRIMITIVE`」。R01 §2.4（`02_CONSTRUCT_CONVERGENCE.md:106`）其实已自行给出该辩护的**形式**，只是未据此改裁决。 |

**为什么不是重复劳动**：B / C / D 三条**不共享同一证据**——R02 用 meta 相关（Tran, Judge & Kashima 2019, `doi:10.1111/pere.12268`, 202 samples / N = 50,427, `R2 = .54`）；R06 用形式化存量；R17 用源理论定义式。**三条独立收敛到同一方向，R01 是唯一孤立方。**

---

### CF-02｜`Satisfaction`：派生还是一等状态 —— 主要是**术语**冲突

| 项 | 内容 |
|---|---|
| **Lane A（R01）** | §3.10：`DERIVED`（维持 §9 R3），但**附时序保留**——investment model 路径图把 satisfaction 放在 commitment **上游**，完全降为 readout 就无法表达「满意度先跌、commitment 后跌」；建议建模为 `DerivedEvaluation`（带显式 `comparison_baseline` 与 `observation_time`），**可被下游转移引用**，但**禁止**进入 primitive 集合。`02_CONSTRUCT_CONVERGENCE.md:236`、`:421` |
| **Lane B（R17）** | §3 F3 + A21：`Satisfaction` 为 Derived = **`CHALLENGED`**，理由是「它是该领域唯一纵向验证的 DV，是外部效度锚点。若降级为 Derived，LHRM 就降级了唯一的 ground truth」。`17_RED_TEAM_FALSIFIERS.md:380`、`:417` |
| **Lane C（R06）** | 律 C `DVA` 主体层登记为 `Derived readout + History`；§11 非主张 3 明文：「各律**假定** 现有层归属（… R3 Satisfaction 属 derived …）。若 Gate C 冗余审计合并其中任一项，对应律族**必须重新推导**，不能只重新拟合」。`06_TRANSITION_LAWS.md:108`、`:965-968` |
| **Lane D（R09）** | §8.1(1)：「真实关系数据里最硬的『非线性』发现，是靠**一条连续读出**加一个事件时钟得到的」——正面支持把 satisfaction 一类读数留在 readout 侧。`09_DYNAMIC_SYSTEMS_AND_HYSTERESIS.md:524` |
| **`incompatibility_kind`** | **层冲突，但实质是术语冲突** |
| **R16 的独立确认** | §12 `F-SELF20`：「R17 F3 更进一步：最强组织变量 `PPR` 在当前 schema 里住在 Belief 层，而派生 readout 住在 Derived 层。防线：**无**。本协议最严重的设计级风险。如果 schema 的层归属本身错了，本协议的全部 machinery 会**忠实地验证一个错误的对象**。」`16_EMPIRICAL_VALIDATION_PROTOCOL.md:475` |
| **判定** | **`OVERLAPPING_NEEDS_SCOPE_RULE`** |

**关键澄清（避免制造矛盾）**：R01 反对的不是「Satisfaction 进入 dynamics」，而是「Satisfaction 成为 primitive **坐标**」；R17 的 R2 退守条件（`17_RED_TEAM_FALSIFIERS.md:391-393`）也只要求「`PPR` 与 `Satisfaction` 升为一等**状态层**」。**两者在争同一个词的两义：「一等状态」vs「primitive 坐标」。** R01 的 `DerivedEvaluation` 已经是一个可用的区分，只是没人给它命名。

---

### CF-03｜`PPR` 的层位：三种互斥处置（优先级最高）

| 项 | 内容 |
|---|---|
| **Lane A（R01）** | §3.12 裁决：**`BELIEF_ONLY`**，强制理由 `[S34] + [S33]`（people's perceptions of being understood are only modestly related to actually being understood；PPR reflects both actual partner behavior and motivated reinterpretations）；并加禁令「**PPR 不应被降为某个别的构念的 proxy**」。`02_CONSTRUCT_CONVERGENCE.md:260`、`:279` |
| **Lane B（R17）** | §3 F3：**`CHALLENGED`**，判为「**头号可执行建议**」——「可定案的具体观察：把 `PPR_i` 从 Belief 层**提升为 state 层**并允许 `Belief_i(PPR_j)`」。A20 裁定 `CHALLENGED`。`17_RED_TEAM_FALSIFIERS.md:155-175`、`:379` |
| **Lane C（R06）** | §4.9：若「符号对、效应在联合建模 lag-0 时消失」，则「说明 `Z` 与 `PPR` 是**同一测量**，不是两层」，「**修正方向：合并，而非各留一个 primitive**」。`06_TRANSITION_LAWS.md:269-271` |
| **Lane D（R14）** | §2.1 把「`PPR` 属 Belief 层，responsive action 属 Action 层」直接列为 **REUSE（高严重度）**，即视为已有先例、不再是待议问题。`14_PAPER_POSITIONING_NOVELTY.md:43` |
| **`incompatibility_kind`** | **层冲突，三方互斥** |
| **R01 自身未调和的一点** | §3.12 引 `[S33]` 把 PPR 定位为 trust 与 commitment 的**上游生成器**（mutual cyclical growth），并在 `02_CONSTRUCT_CONVERGENCE.md:258` 用「belief 层在分钟–日尺度上可极快波动」作为留在 Belief 层的理由。**这两点支持 R17 的因果近端性判断。** → R01 同时持有「PPR 是上游生成器」和「PPR 是下游 belief」两种读法，其 §3.12 未调和 |
| **R14 的问题** | R14 是唯一一份把**未裁决**的层归属写成 prior art 的报告，而 R17 R2 明说这是「最可能发生的一条退守」 |
| **判定** | **`UNRESOLVED`。** 三方各执一词；R14 的处理方式最需要修 |

---

### CF-04｜`Cohesion / We-ness`：同一 canonical 槽位 P1 的两种互斥解

| 项 | 内容 |
|---|---|
| **Lane A（R01）** | §3.11 裁决：**`BELIEF_ONLY`（当前阶段）**——采纳 §6 P1 的保守表示，**不**承认独立于双方知觉的 `Cohesion_(A,B)` primitive；升级条件是「出现独立的 pair-level 观测通道，且纵向数据显示 `Cohesion_pair` 在已知 `PerceivedWeNess_A, _B` 之上仍有稳定增量信息」。`02_CONSTRUCT_CONVERGENCE.md:248`、`:278`、`:422` |
| **Lane B（R10）** | §6.3 判决：`REJECT Cohesion_(A,B) as a scalar primitive` + `REJECT "we-ness" as a construct name in the ontology` + **`KEEP PairRepresentation_(A,B,t)`**（成员：R1 couple identity / shared narrative、R2 shared future / couple project、R3 division of labor / relational norms、R4 shared external memory）+ 两个 directed belief + 一条 `pair -> directed` 因果入边。`10_MUTUALITY_POWER_DEPENDENCE.md:618-631` |
| **Lane C（R11）** | §3.6：P1 方向对，但还差一步——敌对 / 合作 / kin 三类 dyad 的 "we" 的自然归属是 **group 级**；提案 `CohesionScope ∈ {pair, subgroup, coalition}`。`11_GENERAL_HUMAN_DYADS_SCOPE.md:135-142` |
| **Lane D（R02）** | E12（`AttachmentSecurity` vs `Cohesion`）判 **`UNKNOWN`**——五个 lens 全部未取得证据。`02b_CONSTRUCT_REDUNDANCY_AUDIT.md:241` |
| **`incompatibility_kind`** | **范围冲突（真残余分歧）** |
| **关键澄清** | 三条**共享**一条结论：「we-ness 不能是一个标量 pair primitive」。分歧只在**是否允许一个非标量的 pair 级内容对象**。R10 的核心证据是 **clarity 不等于 agreement**（Emery et al. 2021, `doi:10.1177/0146167220921717`：couple identity **clarity** 超出 **agreement** 预测 commitment，并预测 9 个月解体；另 Cruwys et al. 2022/2023, `doi:10.1111/famp.12811`, N = 375：7 个量表析为 4 因子，couple identity 与 partner liking 不能互相预测）；R01 的核心论证是 **agreement 低则无法推断 pair latent**（IoS 单题；projection `r = .77–.90` vs agreement `r = .18–.19`；RCI 已内含 interdependence）。**这两条证据测的不是同一个东西，不能靠「谁引用更多」解决。** |
| **判定** | **`UNRESOLVED`。** 有可执行的 tie-breaker，且 R10 已给出：**若 couple identity clarity 在加入 joint `Action/Event` 历史后不再有增量，则 `PairRepresentation_R1` 也是派生的**（`10_MUTUALITY_POWER_DEPENDENCE.md:635`）。该检验**未被任何 lane 执行** |

---

### CF-05｜`Trust` vs `AttachmentSecurity`：保留 vs 降级

| 项 | 内容 |
|---|---|
| **Lane A（R01）** | §3.4 / §3.6：两者**都 `KEEP`**（`Trust` = 13 个候选中最稳的一个，强制加 `domain` 索引；`AttachmentSecurity` `KEEP` + `CONTESTED / LOW_CONSENSUS`，要求 person / edge 双层且**保留 (anxiety, avoidance) 原始二维**）。`02_CONSTRUCT_CONVERGENCE.md:164`、`:188`、`:271`、`:273` |
| **Lane B（R02）** | E4：`STRONG`（重叠）/ `MOD`（残余），H1 判 **`CRITICAL`**：「**定义层内嵌**。trust 定义含 emotional security；benevolence referent 含 responsiveness / caring。**危险机制：朴素 CFA 允许斜交时『看起来没问题』，而条目层冗余是 100% 的**」。MGS-C 裁决「`Trust` **降为其部分 facet**」，同时承认「若把 trust 全降为 `AttachmentSecurity` 的 facet，会丢掉『预期不被剥削 / 守约 / 可预测 / 能力』这一整片语义。**本 lane 无法决定这一刀切在哪 -> U4**」。`02b_CONSTRUCT_REDUNDANCY_AUDIT.md:230`、`:255-271`、`:375`、`:440`、`:468` |
| **`incompatibility_kind`** | **定义冲突** |
| **关键澄清** | R02 自己在 `02b_CONSTRUCT_REDUNDANCY_AUDIT.md:271` 写「不要把这两项当两个干净的独立 coordinate。至少承认 `Trust` 内含一个 `FeltSecurity` facet」。**R01 §3.6 的 person / edge 双层要求与 R02 的 facet 拆分方向一致。** 冲突的只是**协调子的地位**：R01 让两者平级（各带强制条件），R02 让 `Trust` 从属于 `AttachmentSecurity`。 |
| **R03 的独立数据** | PRQC 同施测内亚量表相关：trust 与 satisfaction `.58` / intimacy `.47` / love `.48` / commitment `.38`，**仅 passion `.14`**（Fletcher, Simpson & Thomas 2000, `10.1177/0146167200265007`）；R03 结论「Gate C 的三对挑战在自陈通道上都**缺乏分离性证据**」。`03_MEASUREMENT_INSTRUMENTS.md:215`、`:272` |
| **判定** | **`OVERLAPPING_NEEDS_SCOPE_RULE`** |

**需要的不是一条裁决，是一张 facet 分配表**：4 个 McKnight & Chervany referent（`benevolence / integrity / competence / predictability`，`doi:10.1007/3-540-45547-7_3`）× R01 的 role facets × R02 的 `FeltSecurity`。R02 自己的 U4（`02b_CONSTRUCT_REDUNDANCY_AUDIT.md:496`）与 R01 自己的 §5.1（`02_CONSTRUCT_CONVERGENCE.md:290-294`）都指向这条规则。

---

### CF-06｜`Distrust`：R01 与 R02 / R03 给出互斥结论，且共用同一证据族

| 项 | 内容 |
|---|---|
| **Lane A（R01）** | §3.5 裁决：**`OPEN`（强烈倾向 `DERIVED`）**——「这是本文对 prior report 的**最主要分歧**」；理由：(a) 同刊同档正面对撞已持续 30+ 年（Lewicki, McAllister & Bies 1998, `10.5465/amr.1998.926620` vs Schoorman, Mayer & Davis 2007, `10.5465/AMR.2007.24348410`）；(b) **反向计分方法学 artifact**——「distrust 的很多操作化是信任题目的反向计分，而反向计分题在因子分析中天然分离出第二个因子」；(c) **决定性实验尚未见成规模执行**。`02_CONSTRUCT_CONVERGENCE.md:176`、`:272` |
| **Lane B（R02）** | C9 / E13 / R9 residual：**否证 `1 − Trust`**——「trust 与 distrust 是**分离且同时运作**的构念」；R9 列为「不可消去残余」。`02b_CONSTRUCT_REDUNDANCY_AUDIT.md:242`、`:365`、`:401` |
| **Lane C（R03）** | §4.1：**建议把 `Distrust` 从 open question 升级为独立候选**，理由从「待测」改为「**78% 共存的直接证据 + trust / distrust 分别测量的工具化路径**」（Hsu 2019：279 名被试中 78% 曾对同一人同时经历 trust 与 distrust；Wildman et al. 2025 高阶两因子模型）。`03_MEASUREMENT_INSTRUMENTS.md:76`、`:250` |
| **`incompatibility_kind`** | **经验冲突（同一文献族，不同结论）** |
| **一个具体的解释（不是矛盾）** | R03 的 `78%` 来自 **workplace / 抽象定义**情境（`03_MEASUREMENT_INSTRUMENTS.md:75-76` 自陈「目标场景是 workplace，不是 close relationship」）。**R01 的 artifact 论证恰恰预测在关系场景的条目池上会失效。** 因此 R01 与 R03 更可能是**范围不同**而非矛盾——但**没有任何 lane 把这一点写出来**，而 R03 的建议动作（「升级为独立候选」）**不带范围限定**。 |
| **判定** | **`OVERLAPPING_NEEDS_SCOPE_RULE`**：R03 的证据须先被限定到 workplace 域，才可能与 R01 的 artifact 论证在同一域内比较。R01 的 `OPEN` + 决定性实验规格（U3，`02_CONSTRUCT_CONVERGENCE.md:396`）是三者中唯一给出可执行 tie-breaker 的位置。 |

---

### CF-07｜`OutcomeDependence`（D8）：四种互斥本体论

| 项 | 内容 |
|---|---|
| **Lane A（R01）** | §3.9：**`KEEP` + `MEASUREMENT_INFEASIBLE_AT_RELATION_LEVEL`**，但「**建议的处理不是『删』**」——保留为候选，当前只能**结构化估计**而非问卷估计；加 `domain` 索引；登记 coordination 不可知觉为系统误差源。`02_CONSTRUCT_CONVERGENCE.md:224`、`:276` |
| **Lane B（R02）** | E10：`CONTESTED`（**偏向不可仅派生**）——`I` lens 判 `✗反向`，`F` lens 判 `✓失败`。`02b_CONSTRUCT_REDUNDANCY_AUDIT.md:237` |
| **Lane C（R10）** | §4.4：**`NEGATIVE` for D8 as directed primitive**——「**删除 directed primitive `OutcomeDependence_(i->j)`**，代之以 (a) `Alternatives_(i, ref=(j))` (b) `ValueOf_(i, j)` (c) `Constraint_(i, j)` (d) `Dependence_(i,j,S)` = 情境 `S` 的**结构 readout** [非心理状态] (e) `PerceivedDependence_(i,j,S) = B_i(d)`」。动作项 A3 标**高优先级**。`10_MUTUALITY_POWER_DEPENDENCE.md:219-234`、`:734` |
| **Lane D（R03）** | §4.1：**降级为 `NOT_IDENTIFIABLE`**——「两端（dependence 工具、power 工具）皆空」。`03_MEASUREMENT_INSTRUMENTS.md:254` |
| **Lane E（R17）** | A18：`OutcomeDependence` 可完全导出 = **`NO_EVIDENCE_FOUND_FOR_CHALLENGE`**，并肯定「项目自己已开 Open question（§4 D8），**这是诚实的**」。`17_RED_TEAM_FALSIFIERS.md:377` |
| **Lane F（R06）** | 律 B `APES`：`D^d` 是一个**累积存量**，`Dedication` 是它的下游读出（见 CF-01）。`06_TRANSITION_LAWS.md:291-296` |
| **`incompatibility_kind`** | **层冲突 + 范围冲突** |
| **连锁后果** | D8 是**唯一**能支撑 `PowerImbalance` 派生链的候选（R01 §3.9 明写「若降级，§9 R2 的 `PowerImbalance = f(...)` 就失去全部输入」）。R10 的删除方案把 D8 的**全部输入**换成 `Alternatives / ValueOf / Constraint / Omega(S)`，而 R10 §6.3 同时把 `CoupleIdentity` 从 D8 里拿出来单列（`PairRepresentation_R2` = shared future / couple-based goals）。→ **R10 的方案一旦采纳，R06 `APES` 的存量 `D^d` 与 R10 的 `Omega(S)` readout 争夺同一个 slot。** |
| **R11 独立支持** | L-1：`D8` 的 `alternatives` 项内建了**自愿退出 + 开放选择集 + 共享未来**；在友谊上「近乎无定义」、在亲属上为空、在专业上被 role contract 替代。`11_GENERAL_HUMAN_DYADS_SCOPE.md:195-205` |
| **判定** | **`UNRESOLVED` + `SAME_CONSTRUCT_DIFFERENT_NAME`** |

**读法**：「dependence」这一个词被指派了**四种互不兼容的本体地位**：(i) 有向心理状态（R01 立场）；(ii) 情境结构 `Omega(S)` 的 readout（R10）；(iii) pair 层累积存量（R06 `APES`）；(iv) 由 Agent 资源 / alternatives / 制度约束**结构化估计**（R01 §9.1 的建议本身就是 iv，但其裁决是 i）。**这不是五条 lane 各说各话**——R01 / R02 / R03 / R17 **四条共享「关系级无验证量表」这一前提**，只有 R10 主张**删**。

---

### CF-08｜`PowerLevel` / `PunitiveCapacity` / `Constrainedness`：一个家族被四个 lane 各切一刀，层位互斥

| 项 | 内容 |
|---|---|
| **Lane A（R02）** | 把 `PWL = PowerLevel_(i->j)` 放在 **`DirectedState_(i->j)` 子图内**（`02b_CONSTRUCT_REDUNDANCY_AUDIT.md:74`），§3.3 节点表同（`:203`），依据 C2（`:394`：`70–75% 的日常互动涉及相对平等的权力`；actor 与 partner 的知觉权力倾向**正相关**；引 Overall & Hammond 2026, `doi:10.1146/annurev-psych-012325-032022`）。**但同一份报告的 MGS-C 又把它列进「derived / readout」组**（`:458-459`） |
| **Lane B（R10）** | §4.6.6 + §7：把同一现象拆成**四个表示**——`P1_structural`（从 `Omega / alternatives / value / constraints` 读出）、`P2_capacity = PunitiveCapacity_(i->j)`（**独立 construct family，不可由 P1 派生**；依据 Lawler & Bacharach 1987, `10.2307/2578749` 的实验分离 + Lawler 1993）、`P3_perceived = PerceivedPower_i(j, domain) = B_i(...)`（**Belief layer, directed by perceiver**）、`P4_felt = FeltCompliance_i(j, domain)`。`10_MUTUALITY_POWER_DEPENDENCE.md:366-395`、`:652-657` |
| **Lane C（R11）** | §3.3：提案把 `Constraints` 与 `Agreements` 拆为两容器，`Constraint` 为 **per-edge，带 `source` / `scope` / `consent_status ∈ {consensual, imposed, unknown}` / `degree`**；派生 `ConstraintAsymmetry(A,B)`。证据 Johnson 2006, `10.1177/1077801206293328`（有害 dyad 的**定义性变量是 control context**，`the distinctions among the types are based entirely on control context, not frequency or severity of violence`）+ Dutton, Goodman & Schmidt。`11_GENERAL_HUMAN_DYADS_SCOPE.md:101-110` |
| **Lane D（R10）** | §4.5 + G4：另需 `Legitimacy_(i,j,domain)`，依据 Johnson & Ford 1996 的**正交操纵**（subordinate / superordinate 的 alternatives 与 endorsement / authorization 正交操纵，N = 320）。`10_MUTUALITY_POWER_DEPENDENCE.md:246-259`、`:677` |
| **`incompatibility_kind`** | **层冲突（同源证据，不同层位）** |
| **为什么这是最干净的一条层冲突** | R02 与 R10 引**同一篇** Overall & Hammond 2026，得出**同一个经验结论**（per-person power 不等于 dyadic asymmetry；actor / partner 知觉权力正相关；70–75% 互动平等），然后把它放到**两个不同的层**：R02 放 `DirectedState`，R10 放 `Belief`。**这不是「谁对」，而是「同一个量在两张 schema 表里被分配到不同抽屉」。** |
| **R02 自身的次级不一致** | mermaid（`:74`）与节点表（`:203`）归 `DirectedState`，MGS-C（`:458-459`）归 `derived / readout`。**同一 lane 内部未对齐**，因此这一格当前是「内部矛盾」，不是稳定 lane 立场 |
| **判定** | (i) `PerceivedPower_i`（R10）vs `PowerLevel_(i->j)`（R02）= **`SAME_CONSTRUCT_DIFFERENT_NAME` + 层冲突**；(ii) `PunitiveCapacity` vs `Constrainedness / Control-Asymmetry` = **`OVERLAPPING_NEEDS_SCOPE_RULE`**（R11 覆盖面严格包含 R10 的：人身控制 / 勒索 / 囚禁都能写成 `Constraint` with `consent_status = imposed`）；(iii) `Legitimacy` = **`GENUINELY_DISTINCT`**；(iv) `FeltCompliance` = **`GENUINELY_DISTINCT`**（R10 自陈证据间接，`Lawler 1993` 明说抵抗 vs 顺从的条件**尚未解决**） |

---

### CF-09｜`SituationStructure`（`Omega`）：R10 判 ontology hole，R11 判「不是 ontology hole」

| 项 | 内容 |
|---|---|
| **Lane A（R10）** | §3 + G1：把「情境的客观互赖结构 `Omega(S)`」列为**本体漏洞（ontology hole），不是构念漏洞**；可证伪后果是「两个有向状态相同、情境结构相反的 dyad 会被判为同一状态」；动作项 A5「在 ontology 中补 `SituationStructure`（`Omega`），与 `Environment` / `PairState` **并列**」标**高优先级**。`10_MUTUALITY_POWER_DEPENDENCE.md:93-108`、`:674`、`:736` |
| **Lane B（R11）** | L-9：`X_(S,O,t) = Phi_(S,O)(WorldState(t))` 的二人局部投影在 ≥4 类 dyad 上不足，但「世界层是 `Agents + Relationships + Environment`，`Role` 是 query lens —— 所以这**不是 ontology hole，是 query lens 太窄**」。`11_GENERAL_HUMAN_DYADS_SCOPE.md:282-289` |
| **`incompatibility_kind`** | **范围冲突（对缺口类型的分类冲突）** |
| **共享的结论** | 两者**都同意**当前二人局部投影装不下这些现象（kin 的忠诚冲突、care 的机构中介、敌对 dyad 的 group 级 "we"、前任的制度驱动）。分歧只在**修在哪一层** |
| **为什么重要** | 若 R11 对，则 R10 的 A5 会把一个**查询层**需求写成本体层实体，`AGENTS.md`「Role 显式为 query lens，不替代 world state」的方向会被侵蚀。若 R10 对，则 R11 的修法会漏掉 `Omega` 的 actor / partner / joint control 结构 |
| **第三份材料** | R12 C-SAOM 从**方法学侧**给出同向压力但落在别处：SAOM 假定 tie 的存在**处于发送方单边控制之下**，原文点名这会「exclude most types of relations where negotiations are required for a tie to come into existence」（Snijders, van de Bunt & Steglich 2010）。`12_COMPUTATIONAL_MODELS_ABM.md:120-123` |
| **判定** | **`UNRESOLVED`，但这是纯架构裁决，不需要新证据。** R10 的判别（「两个有向状态相同但 actor / partner control 相反的 dyad，是否被 LHRM 判为同一状态」，`10_MUTUALITY_POWER_DEPENDENCE.md:530`）在**当前 schema 下已经可执行**，答案是「会」 |

---

### CF-10｜SRM 三分解（`source_i` / `target_j` / `edge`）：六条 lane 的位置，其中两条互斥

| 项 | 内容 |
|---|---|
| **Lane A（R01，主张采纳）** | §2.2：「建议所有 directed 构念的 `StateCoordinate` 显式携带 `z[k,i,j,t] = { edge_estimate, person_prior_i, target_attr_j, uncertainty, evidence, provenance }`」；列为「不需新数据即可执行」的首项建议。`02_CONSTRUCT_CONVERGENCE.md:81-87`、`:419` |
| **Lane B（R10，主张采纳但依赖它）** | §4.1：`Mutuality_k(A,B,t) = H(e_k(A->B,t), e_k(B->A,t))`，其中 `e_k = D_k − R_k(i) − T_k(j)`；动作项 A1 标**高优先级**。`10_MUTUALITY_POWER_DEPENDENCE.md:147-158`、`:732` |
| **Lane C（R05，判定不可识别）** | I4（⭐）：「**两人 dyad 里分离 `source_i` / `target_j` / `directed_dyad_(i->j)`** —— 自由度：2 条有向边 = 2 个自由度」。结论：「`CONSTRUCT_SCOPE_DIRECTIONALITY.md` §1 的分解式在**纯 dyad 设计下不可识别**。三者可作**架构占位符**存在，但**不得**写成『估计值』。要估计它们必须重新采集 round-robin / 交叉设计数据。」`05_IDENTIFICATION_AND_STATISTICS.md:360` |
| **Lane C-2（R05）** | I14：「**LHRM 最难的一个识别缺口**」；「Mplus DSEM 是 two / three-level，dyad 当 cluster 时两条边在同一 level，**无法**同时分离两者」。`05_IDENTIFICATION_AND_STATISTICS.md:370` |
| **Lane D（R17，第三种立场）** | F10 T5 / A23：加法分解把 `source_i + target_j`（跨时间常数 / trait）放进**时间索引的状态**里，「等于**静默导入一个横截面特质模型**到动态状态模型」；裁定 `CONTESTED`。`17_RED_TEAM_FALSIFIERS.md:336`、`:382` |
| **Lane E（R11，域特异不可识别）** | §3.8：SRM 式分解的可识别性要求两条隐含条件（target 属性与 source 的进入 / 选择近似独立；dyad 可重新选择），**在亲属 dyad 上按构造成立地失败**；「`context/history residual` 不是残差而是主项；`target_j` 不能读作 Agent 层 trait」。`11_GENERAL_HUMAN_DYADS_SCOPE.md:156-180` |
| **Lane F（R12，round-robin 是硬约束）** | C-SRM：「**要求 round-robin 设计**…**LHRM 的 Court-fact Case Bank 是单一 dyad 深度材料，结构上不满足此识别条件。不能直接用。**」`12_COMPUTATIONAL_MODELS_ABM.md:106` |
| **Lane G（R16，协议侧已接受不可识别）** | `F-07`（阻断级）：「方向性分解不可识别…三者可作**架构占位符**，但**不得**写成『估计值』」；§13 I4 再次确认。`16_EMPIRICAL_VALIDATION_PROTOCOL.md:395`、`:489` |
| **`incompatibility_kind`** | **层冲突 / 要求冲突** |
| **可执行后果（本报告的新发现）** | R10 §4.1 的 falsifier 是「控制 `R_k(A), R_k(B), T_k(A), T_k(B)` 之后，`H(e_AB, e_BA)` 对任一 outcome 的增量预测力不显著优于 `H(D_AB, D_BA)`」。**这个 falsifier 在 R04 审计的任何数据集上都不可执行**——R12 明说 round-robin 不存在，R04 的 16 个数据集中没有任何一个是 round-robin 设计。→ **R10 优先级最高的派生修正（动作 A1）的验证程序被 R05 I4 + R12 §3.1 + R04 §3 三方共同封死。** |
| **判定** | **`OVERLAPPING_NEEDS_SCOPE_RULE`（可低成本修）**。R05 I4 已经给了出口（「可作架构占位符」），R16 `F-07` 也已采纳；**缺的是 R01 §9.1 与 R10 A1 侧的限定语** |

---

### CF-11｜时间 / 尺度假设：R09 提议的 `tau`、R03 的仪器台、R06 律 E 的要求三者互不相交

| 项 | 内容 |
|---|---|
| **Lane A（R09）** | §7 O8 候选修正方向：「在文档中显式写明 LHRM 的 `tau` 主要是**月—年级**，并声明因此**不采用** coordination dynamics 的词汇与参数化（**除非未来引入分钟级观测通道**）」。`09_DYNAMIC_SYSTEMS_AND_HYSTERESIS.md:510` |
| **Lane B（R06）** | §2 约束 C-A「**分辨率即识别参数**」：「年级面板**在结构上**无法分离『对方行动改变了我的状态』与『我们在同一测量窗口内共同生产一个状态』。任何律族若要主张 partner effect，其测量间隔必须细到能产生 lag-0 与 lag-1 的可区分性。」`06_TRANSITION_LAWS.md:74-81`；律 E §8.6：「**分辨率由约束 C-A 强制**（需能区分 lag-0 与 lag-1）」+「事件触发式记录，含**事件内顺序**。这是律 E 的**硬性**要求」。`06_TRANSITION_LAWS.md:830-833` |
| **Lane C（R03）** | §3.2 时间尺度表：state 层工具只存在于「逐次互动 / 日 / 周」；「**月**：除性欲外几乎无月度工具」；「**回溯年度：无**」；并明写「**没有『信任更新』或『欲望更新』的 state 工具。PPR 有 state 化证据，trust 没有**」。`03_MEASUREMENT_INSTRUMENTS.md:201-208` |
| **Lane D（R09）** | §6.2 第 3 点（把 repair 变成可检验命题所需四件东西之一）：「**足够密的观测窗**：恢复是持续过程；**年度数据只能看到 1–2 个恢复点**。」`09_DYNAMIC_SYSTEMS_AND_HYSTERESIS.md:488` |
| **Lane E（R05）** | I12（⭐）：「状态转移的**速率** —— 同一 `psi(t)` 序列在不同 lag / 时间分辨率下给出不同 AR 系数与不同『惯性』结论」；「所有速率陈述必须**相对于采样协议**表述。`X_(t+1) = F(...)` 中的 `+1` **不是一个自然量**」。`05_IDENTIFICATION_AND_STATISTICS.md:368` |
| **Lane F（R16）** | `R16-ID06`（把 I12 变成强制字段）：`wave_id` 必须携带 `event_time` / `fieldwork_window` / `wave_index`；「**`wave_index` 不得当作物理时间差**」；滞后陈述必须写「相隔 `k` 个 `wave_index`、实际 `Δ` 天 / 月」。`16_EMPIRICAL_VALIDATION_PROTOCOL.md:44` |
| **第四份材料（R12）** | §2.2 Lawson & Park (2000), *JASSS* 3(1)2：「**同步时间推进会制造伪动力学**」；并指出 JuliaDynamics/Agents.jl 的「同一模型两种时间语义」能力**正是 F5 需要的对照实现**。`12_COMPUTATIONAL_MODELS_ABM.md:54`、`:75` |
| **`incompatibility_kind`** | **范围冲突，且有直接可执行后果** |
| **三点具体后果** | (1) R09 提议把项目 `tau` 固定在月—年级并据此**拒绝** coordination dynamics 词汇；R06 律 E 的**硬性**数据要求恰好就是 coordination dynamics 的事件内尺度。**二者不能同时被采纳为「当前项目立场」。**<br>(2) R03 的仪器台显示：**月—年级尺度上 `Trust` / `Dedication` / `AttachmentSecurity` / `Caregiving` 没有任何 validated state 工具**（唯一的年度层级工具是回溯式，不是 state）→ **R09 提议的 canonical `tau` 在测量层没有对应工具。**<br>(3) 反过来，R03 说 state 工具只在逐次互动 / 日尺度，而 R09 §5.4 已论证该尺度的**强耦合前提在多数真实 dyad 中不成立**（`ES = .09, I2 = 76.0%`；只有 14–38% 的伴侣情绪协动超过 pseudo-couple；`lovers > friends > strangers` 预期**未成立**）。 |
| **注意（不构成冲突）** | R05 I12 与 R16 ID06 **不构成冲突**——它们是**揭示**上述冲突的那条约束（R16 直接把 I12 落成字段），应记为 convergence |
| **判定** | **真实残余分歧（架构决定，非证据问题）**，影响面 = R06 的 `RT` 律族 + R09 的 L-A–L-D 离散层。**R06 §12 的 5 条裁决请求与 R09 §8.3 的 20 条 non-claim 都没有记录这条冲突。** |

---

### CF-12｜`Unknown` / 「无值」值类：五个 lane 五套互不兼容的类型系统，零交叉映射

| 项 | 内容 |
|---|---|
| **Lane A（R07）** | §9.3 给出具体形状：`Unknown { tag ∈ { no_evidence, refused, private_to_partner, withheld_by_actor, disputed, censored, structurally_unobservable, not_yet_real, superseded, unmeasured_by_instrument }, prior_set, evidence_mass, value_class, provenance }`；并声明 `value_class` 承载双序（F-01）、与 `tag` **正交**（一个坐标可以同时是 `private_to_partner` 与 `not_yet_real`）。`07_PARTIAL_OBSERVABILITY.md:470-486` |
| **Lane B（R11）** | §3.1：值类扩为 `{applicable(estimate/interval/...), structurally_not_applicable, scope_unknown}`，并要求 `DyadSnapshot` 顶层增加 `DyadScopeProfile`。论据：「对兄弟姐妹的性欲坐标，正确值既不是 `Unknown`（我们可能高度确信其不存在），也不是 `0`（`0` 是『被测到的零』，是另一个断言）… 现有值类集合里没有这一格，**唯一的合法表示方式就是把不适用填成 0 或 Unknown——正是 `AGENTS.md` 禁止的动作**」。`11_GENERAL_HUMAN_DYADS_SCOPE.md:79-85` |
| **Lane C（R13）** | §10 规则 R6：「歧义必须保留为**分支集合**。禁止在无显式裁定时选边。`AMBIGUOUS_NO_UNIQUE_ANSWER` 是一等状态，与 `UNKNOWN_EVIDENCE` 严格区分」。`13_LLM_SKILL_INTERVIEW_LAYER.md:470` |
| **Lane D（R15）** | §15.6.3 规则 3：「`UNKNOWN` 与 `MAPPING_FAILURE` 必须分清：`UNKNOWN` = 材料不足；`MAPPING_FAILURE` = 材料充分但表示装不下」；§15.6.2 另有 `fact_status ∈ {ADJUDICATED, ADMITTED, ALLEGED, DISPUTED, UNKNOWN}` 与 `temporal_basis ∈ {..., UNKNOWN}`；对抗件 A02「同时为真、被相信、且为假」失败判据是「单一真值字段二选一即失败；**须三轴并存**」。`15_CASEBANK_EXPANSION.md:180`、`:198-201`、`:229` |
| **Lane E（R16）** | §3.1 第 5 值 `NOT_MAPPED`（「必须附 `why`：无工具 / 构念在数据中不存在 / 只有 pair 级而无方向 / 抽样框不含该情境 / 构念本身未定义」）+ §3.2 `directionality_class` 的 `UNDETERMINED`。`16_EMPIRICAL_VALIDATION_PROTOCOL.md:63`、`:82` |
| **`incompatibility_kind`** | **`SAME_CONSTRUCT_DIFFERENT_NAME`** |
| **命名空间的重叠与错位** | • R11 `structurally_not_applicable` 约等于 R07 `structurally_unobservable`；R11 `scope_unknown` 约等于 R07 `unmeasured_by_instrument`（**但 R11 只加了一个值，R07 把「工具没测」与「结构性不可观测」分成两个 tag**）。<br>• R13 `AMBIGUOUS_NO_UNIQUE_ANSWER` 约等于 R07 的 K4 值 `B`（known-both-true-and-false）约等于 R15 的 `DISPUTED`——**三处不同名，同一语义**。<br>• R15 `UNKNOWN`（材料不足）约等于 R16 `NOT_MAPPED.why = 无工具` 约等于 R07 `no_evidence`。<br>• R15 `MAPPING_FAILURE` 在 R07 的 tag 集合里**没有对应值**（它是表示失败，不是证据状态）。<br>• R16 `UNDETERMINED`（方向性不可分）约等于 R16 自己的 `NON_SEPARABLE`，在 R07 的 tag 集合里也无对应。 |
| **为什么最要紧** | R07 §6 FM-03 明确写：「**`disputed` 与 `unmeasured` 不可比**… 任何把两者映射到同一 confidence 值的表示，都在做一次**不可比 -> 可比**的压缩」——**R07 诊断出了这个问题，而 R11 / R13 / R15 / R16 各自独立地重新发明了一个部分解，没有一个引用 R07**（R07 的 sibling-lane 引用数 = 0）。R06 §1 U-4 已指出下游后果：「若 Gate A 的覆盖推理依赖算子组合，必须先证其组合性与闭包性，否则 `MAPPING_FAILURE` 的归因会出错。此项 `UNKNOWN`」。`06_TRANSITION_LAWS.md:66-68` |
| **唯一的成功复用** | R15 是唯一把 `evidence_channel` 做成受控表并与 `fact_status` / `assertion_mode` 分成三轴的 lane，且 R16 §3.4 **显式复用**了它（「**不新造**」）。这是全 swarm 唯一一次跨 lane 词表复用成功，应作为范例。`16_EMPIRICAL_VALIDATION_PROTOCOL.md:100` |
| **判定** | **`SAME_CONSTRUCT_DIFFERENT_NAME`；SSOT 应为 R07 §9.3。** R07 的 tag 集合是唯一**超集**且带**正交性声明**的提案；其余四家都是它的子集或正交切面。修法是纯枚举工作。 |

---

### CF-13｜测量不变性状态字段：三套互不兼容的值集

| 项 | 内容 |
|---|---|
| **Lane A（R16）** | §3.4：`invariance_level_tested ∈ { configural, metric, scalar, strict, partial, alignment_only, NOT_TESTED }`；且「**不得默认为 `NOT_TESTED` 而不显式标注**」，并由 `R16-UC06` 要求「`NOT_TESTED` 必须出现在报告正文而不是附录」。`16_EMPIRICAL_VALIDATION_PROTOCOL.md:108`、`:221` |
| **Lane B（R13）** | §6.5：`construct_alignment ∈ { INVARIANCE_EVIDENCED, PARTIAL_ONLY, UNTESTED }`；并规定「对 `UNTESTED` 的族**禁止**跨语言直接归一化」。`13_LLM_SKILL_INTERVIEW_LAYER.md:231-239`、`:472` |
| **Lane C（R03）** | §3.4 用一张三列散文表（`多国·大样本·跨性别·跨性取向` / `多文化区` / `跨性别·关系状态` / `跨性取向` / `完全无不变性证据`）记录，并给出关键结论：「关系科学里『跨文化不变』的证据**高度集中在两个构念族**（依恋、性欲），而 LHRM 最缺的三个（`Dedication`、`OutcomeDependence`、`Cohesion`）**恰好是零证据**」。`03_MEASUREMENT_INSTRUMENTS.md:224-236` |
| **`incompatibility_kind`** | **`SAME_CONSTRUCT_DIFFERENT_NAME`** |
| **关键区分** | R13 的 `PARTIAL_ONLY` 与 R16 的 `partial` **不是同一个东西**：R13 的 `PARTIAL` 是「存在部分不变性证据」这一**存在性**判断；R16 的 `partial` 是 CFA 的**特定层级**。R03 的三列表是**覆盖矩阵**（分组变量 × 构念族），不是字段值。 |
| **连锁严重度** | 不变性状态是 **R11 U1/U10、R05 I8、R16 L1 / R16-UC06、R03 F-11** 的共同前置。一个没有统一值集的前置字段，会让这五条规则各自发明记法。R11 U1 更进一步把它设成 **Gate C 的前置条件**（「4 组多组 CFA / invariance 序列（configural -> metric -> scalar），每组 >=300 dyad，两方向分别估计。**应在 Gate C 之前先做**」，`11_GENERAL_HUMAN_DYADS_SCOPE.md:387`），而 R05 I11 判定同一切片 `BLOCKED_BY_DATA`（`05_IDENTIFICATION_AND_STATISTICS.md:367`）。**这是一个排序死锁，见 §5.3 U-5。** |
| **判定** | **`SAME_CONSTRUCT_DIFFERENT_NAME`；SSOT 应为 R16 的 7 值层级**（最严格、且已被 `R16-UC06` 强制进报告正文）；R13 的三值降级为**派生标签**；R03 的三列改名为**覆盖矩阵**而非字段。 |

---

### CF-14｜Case Bank / 验证的 verdict 词表：两套并存，只有一套被红队审计

| 项 | 内容 |
|---|---|
| **Lane A（R15）** | §15.6.3 规则 1：「**单一 verdict 词表**：`DIRECT / PARTIAL / MULTI / NARRATIVE_ONLY / IRRELEVANT / UNKNOWN / MAPPING_FAILURE`」（7 值），粒度 = **原子文本单元 -> 映射裁决**。`15_CASEBANK_EXPANSION.md:198` |
| **Lane B（R16）** | §3.1 `mapping_status ∈ { DIRECT_ITEM, DERIVED_COMPOSITE, BEHAVIORAL_PROXY, COVARIATE_ONLY, NOT_MAPPED, CONFLICTED }`（6 值），粒度 = **数据集变量 -> candidate LHRM slot**。`16_EMPIRICAL_VALIDATION_PROTOCOL.md:57-64` |
| **Lane C（R17）** | F1：`MAPPING_FAILURE` **在设计上不可达**——§13 的 10 个映射类含三个 catch-all + 自由文本 provenance；「对任何输入字符串，一个有能力的 mapper 都能找到合法落点」。可定案观察：「删除 `Derived / Narrative-only` / `IRRELEVANT` / 自由文本 provenance 三个出口后，对 Fixture 001 的 C001–C026 重跑三 Verifier」。`17_RED_TEAM_FALSIFIERS.md:108-121` |
| **`incompatibility_kind`** | **`OVERLAPPING_NEEDS_SCOPE_RULE` + 一条真实的覆盖缺口** |
| **三点具体后果** | (1) R17 F1 / F11 的攻击**只针对 R15 的 7 值表**（`NARRATIVE_ONLY` / `IRRELEVANT` 正是它点名的两个出口）；**R16 扩展的 6 值表从未被任何 lane 做过可达性分析**。<br>(2) R16 §12 `F-SELF01` 已把 R17 F1 吸收进自己的失败清单（`16_EMPIRICAL_VALIDATION_PROTOCOL.md:456`），但 R16 自己在同表的「防线够不够」列写「**不够。R17 的证明是构造级的；本协议只是要求把不确定性显式化，并没有使 `mapping_status` 成为一个可失败的检验**」。<br>(3) R15 规则 2 要求的 `MAPPING_FAILURE` 九类归因（`ONTOLOGY_HOLE / CONSTRUCT_HOLE / SCOPE_HOLE / TEMPORAL_HOLE / BELIEF_OBSERVATION_HOLE / TRANSITION_HOLE / MEASUREMENT_HOLE / NARRATIVE_ONLY / DATA_INSUFFICIENT`）与 R07 的 Unknown tag 集**没有交叉映射**——`DATA_INSUFFICIENT` 对应哪个 tag 未定义。 |
| **判定** | **`OVERLAPPING_NEEDS_SCOPE_RULE`**（粒度不同，**不必合并**）+ **`SAME_CONSTRUCT_DIFFERENT_NAME`**（归因词表 vs tag 词表） |

---

### CF-15｜Gate B 的可执行性 —— **`COMPATIBLE`**

| 项 | 内容 |
|---|---|
| **R17** | F9 逐份核对 12 份材料与三个 fixture：same-sex「**无任何一份以同性 dyad 为 core dyad**」；kin / friendship / caregiving「不可」；high-dependence / low-liking「无」。四个叠加问题：语料无法执行 11 类中的 5–6 类；**反例集 = 项目自己的假设列表**（确认偏误装置）；fixture 输入与 ontology 有共同作者（2/3 由 schema 作者在「知道 schema 能表达什么」的情况下做清洗决策）；L1-003 的 `future_leakage_risk: HIGH ... do NOT test ending prediction` 显式解除了最具判别力的测试。`17_RED_TEAM_FALSIFIERS.md:294-320` |
| **R11** | L-8：§7 / §2.4 / Gate B **三处清单互不相同，且都不含** `sibling`、`parent–adult-child`、`ex-partner`、`professional/cooperative`、`adversarial/harm-asymmetric`、`dating-stranger`；「本 audit 审计的 9 类 dyad 中，**有 5 类目前根本没有被项目自己的验证门指定** -> Gate B 通过**不构成**『跨域稳定』的证据」。`11_GENERAL_HUMAN_DYADS_SCOPE.md:272-280` |
| **R15（唯一实际补救）** | §15.2 提供 22 条 narrative 指针，明确含 `same-sex`（`15_CASEBANK_EXPANSION.md:81`）、N13 `Pepys 日记` 作为 `ordinary / longitudinal / deception / same-sex` 压力件（`:66`）、对抗件 A12「非浪漫但极强强度的 dyad」（N16 兄妹）、A13（亲属术语在非西方体系的歧义）。`15_CASEBANK_EXPANSION.md:239-240` |
| **判定** | **`COMPATIBLE`**。R17 与 R11 独立地、用**不同方法**得出同一结论，且 R15 已在提供补救。需记录：**R15 的补救尚未被 R17 / R11 消费**（R15 的 sibling 引用数 = 0；R17 在任何 lane 报告写入之前完成首稿，`17_RED_TEAM_FALSIFIERS.md:36-37`）。执行顺序要求：R15 的覆盖矩阵应先于 Gate B 的任何结论产生。 |

---

### CF-16｜终止事件 / 存活偏误 —— **`COMPATIBLE`**

| 项 | 内容 |
|---|---|
| **R06** | U-3：「律族把 `exit` 当作最大的转移，但**自陈面板在结构上无法观测它**：离开的人停止了作答。终止事件是**设计性删失（censoring by design）**，不是可处理的缺失。」标为「本次 lane 发现的**最重要的结构性盲点**」。`06_TRANSITION_LAWS.md:924-929` |
| **R16** | `R16-OC03`：「**关系终止不是缺失，是设计性删失。**… 以 breakup / divorce 为 outcome 的方程必须标 `CENSORING_BY_DESIGN`，**不得**把未观测到终止读作『未终止』」；`F-04`（结构性）。`16_EMPIRICAL_VALIDATION_PROTOCOL.md:140`、`:392` |
| **R17** | F6 6a 引 Musick & Bumpass (2006) 一手存活偏误陈述：「**selecting on the more resilient relationships should lead to a sample… We find the opposite is true**」；更弱的稳结论：「任何用观测轨迹估 F 的方法都不区分 (i) 关系变化 (ii) 谁留下 (iii) 谁进入。而 LHRM 的 Case Bank 是**文档**不是 panel，所以它**永远检测不到**这个混淆——这是设计层面的不可修复」。`17_RED_TEAM_FALSIFIERS.md:226-251` |
| **R16（L8）** | 要求 attrition 表 + 至少一个 MNAR 敏感性 + 对条件于事件的样本标 `OUTCOME_CONDITIONED_SAMPLE`；举例 CLOC 的随访对象是**丧偶者 + 匹配对照**（条件于丧偶）。`16_EMPIRICAL_VALIDATION_PROTOCOL.md:128` |
| **判定** | **`COMPATIBLE`**。全 swarm 最干净的 convergence 之一。唯一需补的边界是 R17 的「Case Bank 永远检测不到」与 R16 L8 的「必须报 attrition」之间的**适用域划分**（文档语料无 attrition 表可报）——R16 未明写这条边界。 |

---

### CF-17｜Joel et al. 2020 top-5 的层归属计数：R16 沿用了 R17 已自我更正的数字

| 项 | 内容 |
|---|---|
| **Lane A（R17）** | F2：「**5 个里 5 个落在 `DirectedRelationshipState` 之外。** 我在 packet 初稿写 4/5，**复核后更正为 5/5**（appreciation 也不在 8 构念任何一项内；`SexualDesire` 是方向性欲望，不是 sexual satisfaction）。」`17_RED_TEAM_FALSIFIERS.md:147` |
| **Lane B（R16）** | §12 `F-SELF20`：「S23 的 top-5 predictor 有 **4/5 落在 `DirectedRelationshipState` 之外**」。`16_EMPIRICAL_VALIDATION_PROTOCOL.md:475` |
| **`incompatibility_kind`** | **记账冲突（不是经验冲突）** |
| **为什么仍要报告** | R16 同一格里**逐条列举了 5 项**且 5 项都标注为「在 `DirectedRelationshipState` 之外」，但**数字写 4/5**。→ R16 的**推理已是 5/5，只是数字未随 R17 的更正传播**。而这个数字是 R16 **最严重设计级风险**（`F-SELF20` 的「防线」列 = 「**无**」）的唯一量化依据 |
| **判定** | **可修复的记账不一致。** **不**应被写成经验冲突 |

---

### CF-18｜DOI `10.1177/0146167205276865` 的文献身份：R01 与 R03 互相矛盾（本 lane 已实时核验）

| 项 | 内容 |
|---|---|
| **Lane A（R01）** | §3.6 row 4 与 §5.1 引用「S12 = Sibley, Fischer & Liu (2005)」的 `85% shared variance` / `30–40%` vs `5–15%`；§10 引用清单：「Sibley, C. G., Fischer, R. D., & Liu, J. H. (2005). *PSPB*, 31(11), 1524–1536. `10.1177/0146167205276865` [已核]」。`02_CONSTRUCT_CONVERGENCE.md:185`、`:293`、`:457` |
| **Lane B（R03）** | §2.5 row A4「**ECR-R 心理测量与行为效标**」引用 `10.1177/0146167205276865` 并承载**同一组数字**（3 周 85% / 30–40% / 5–15%）；但 §7 引用清单把该 DOI 归给「Fraley, R. C., Waller, N. G., & Shaver, P. R. (2000). Reliability and validity of the Revised Experiences in Close Relationships (ECR-R) … *Assessment*. `10.1177/0146167205276865`」。`03_MEASUREMENT_INSTRUMENTS.md:87`、`:327` |
| **本 lane 的独立核验** | **Crossref REST** `GET https://api.crossref.org/works/10.1177/0146167205276865`，2026-09-27 实时查询，返回：<br>**TITLE** = Reliability and Validity of the Revised Experiences in Close Relationships (ECR-R) Self-Report Measure of Adult Romantic Attachment<br>**CONTAINER-TITLE** = *Personality and Social Psychology Bulletin*<br>**VOLUME / ISSUE / PAGE** = 31 / 11 / 1524–1536<br>**ISSUED** = 2005<br>**AUTHOR** = Sibley Chris G.; Fischer Ronald; Liu James H.<br>→ **R01 的归属正确，R03 的归属错误。** 旁证：同日的 `query.bibliographic=Fraley+Waller+Shaver+2000 ECR-R` 查询把该 DOI 返回给 PSPB 2005 那条 |
| **`incompatibility_kind`** | **引用冲突（文献身份）** |
| **为什么载荷很重** | 那组 `85%` / `30–40%` vs `5–15%` 数字是 **R01 §3.6 判定 `AttachmentSecurity` 必须是 person / edge 双层高不确定坐标**、**R02 E16 / R10 G14** 的决定性依据；R03 自身 row A4 也把它当作「trait 工具少有的行为效标」的证据。**结论数字是对的，出处标签错了一处。** |
| **附带发现（非冲突）** | R03 §7 引用清单**第 5 条重复出现两次**（`03_MEASUREMENT_INSTRUMENTS.md:325-326` 完全相同）；R03 §1.1 规则 4 把 Fraley 拼错（F-a-l-e-y）。两项均为 bookkeeping |
| **判定** | **已定案的引用冲突。** 「*Assessment* 2000 ECR-R 论文的正确 DOI」作为 open item 移交 A04 |

---

### CF-19｜同一统计量的数值差：主观–生殖一致性 `r = .26` vs `.25`（低严重度）

| 项 | 内容 |
|---|---|
| **R01** | §5.6：「**男性自我报告–生殖器反应一致性 r = .66，女性 r = .26**」引 Chivers, Seto, Lalumière, Laan & Grimbos (2010), `10.1007/s10508-009-9556-9`。`02_CONSTRUCT_CONVERGENCE.md:320` |
| **R03** | §2.3 row S8：「**男 r=.66，女 r=.26**；同条件子样本 r=.66 / .44」。`03_MEASUREMENT_INSTRUMENTS.md:65` |
| **R02** | §6 R2 与 C6：「主观-生殖一致性女性 **r = .25**」引「Chivers et al. 2010；Meston & Stanton 2018」。`02b_CONSTRUCT_REDUNDANCY_AUDIT.md:358`、`:398` |
| **`incompatibility_kind`** | **经验冲突（数值），低严重度** |
| **判定** | **`UNRESOLVED`（低）**，移交 A01 / A04 做数值对齐。**不**应被写成「R02 算错了」——三处差异可能全部正确，指向不同子估计（R03 记录了「同条件子样本 r=.66 / .44」，表明该 meta 有多个条件切片）。**本 lane 不选边。** |

---

### CF-20｜`ABM 是否已有可比先例` —— **`COMPATIBLE`**

| 项 | 内容 |
|---|---|
| **R12** | §0.1-2：「**本 lane 最重要的发现是一个否证**：不存在可与 LHRM 对象直接比较的既有关系 ABM… **校准最扎实的关系 ABM 里没有『关系状态』**。Hills & Todd (2008) 的 MADAM 匹配了美国初婚年龄曲线并成功预测了 5 年后的离婚统计，但它的一对『关系』只是『共享 trait 数 + 时长』，**没有 attraction / trust / belief，方向性完全不存在**。」并逐条确认 MADAM 的定量准确性（P(初婚以离婚告终) 0.47 vs 数据 0.50；以离婚告终的初婚时长中位数 6 年 vs 数据 7–8 年；终生未婚 ~6% vs 数据 50 岁以上 <5%）。`12_COMPUTATIONAL_MODELS_ABM.md:15-16`、`:131-139` |
| **R14** | §2.1：「可向 ABM / microsimulation 扩展：已有 marriage-market ABM 且**已声称定量准确**：Hills & Todd (2008) MADAM, *JASSS* 11(4) `https://www.jasss.org/11/4/5.html`（声称准确预测初婚时长、初婚离婚比例、终生已婚比例，跨文化）；Billari (2005) Wedding Ring」。`14_PAPER_POSITIONING_NOVELTY.md:52` |
| **`incompatibility_kind`** | **无冲突** |
| **为什么 compatible** | 两者**共享同一批事实**（同一篇 MADAM、同样承认其定量准确性）。差别只在**「可比」的判据**：R12 用五条硬条件 C1–C5（状态是 dyad 的 / 区分 i->j 与 j->i / 有时间推进语义 / 有可指认的 calibration / 状态可有 Unknown），R14 用**新颖性**判据。R12 §0.6 还给出与 R14 完全一致的结论：「**在 LHRM 当前第一阶段目标（表示完备性 + Case Bank 逐句映射）下，ABM 不是正确的工具**」 |
| **判定** | **`COMPATIBLE`**。明确记为 compatible，以免下游误以为 R12 与 R14 打架 |

---

### CF-21｜`Trust` 跨伴侣一致性 `r = .11` 的解读分歧 —— **`COMPATIBLE`**

| 项 | 内容 |
|---|---|
| **R01** | §3.4 row 4：「**partner-reported trust 跨伴侣一致性 r = .11（ns）** —— **直接反驳『trust 是共享 pair 属性』**」；§5.8 用同一数字得出「`Caregiving` **不能被建模为一个『双方共享的关系属性』**」。`02_CONSTRUCT_CONVERGENCE.md:161`、`:328` |
| **R02** | §6 R8：「trust 的非安全感残余：attachment–trust 仅 `r = −.23 / −.31`」——引 Campbell et al. (2022), `https://pmc.ncbi.nlm.nih.gov/articles/PMC8895702/`，用途是**支持** Trust 与 AttachmentSecurity **部分冗余而非同一**。`02b_CONSTRUCT_REDUNDANCY_AUDIT.md:360` |
| **`incompatibility_kind`** | **无冲突** |
| **为什么 compatible** | R01 用 `r = .11` 论证「trust 不是 pair 属性」（**跨伴侣一致性**）；R02 用 `r = −.23 / −.31` 论证「trust 不被 attachment 覆盖」（**跨构念相关**）。两者测的是**不同的两个量** |
| **判定** | **`COMPATIBLE`**。记录在案以防 A01 / A03 误报为矛盾 |

---

## 3. 重复劳动（Duplicate Work）

### 3.1 R01 与 R02 重复执行 Gate C，且在 4 / 6 个攻击面上给出不同答案

`PARAMETER_CONVERGENCE_V0_1.md` §15 Gate C 点名六对；R01 与 R02 **各自独立地**跑完了它（两条 lane 的 sibling 引用数都是 0）。

| Gate C 攻击面 | R01 裁决 | R02 裁决 | 是否分歧 |
|---|---|---|---|
| `Liking` vs `RomanticAttraction` | `KEEP` + 边界 `OPEN`（`02_CONSTRUCT_CONVERGENCE.md:140`、`:269`） | E1 `CONTESTED`（`02b_CONSTRUCT_REDUNDANCY_AUDIT.md:227`） | **表述分歧，非实质**（R01 也认为边界不稳） |
| `Trust` vs `AttachmentSecurity` | **两者都 `KEEP`**（`:164`、`:188`） | E4 `STRONG` 重叠 + MGS-C「`Trust` 降为其部分 facet」（`:230`、`:440`） | ✅ **分歧：平级 vs 从属** |
| `Caregiving` vs `Dedication` | 两者 `KEEP`，动机 / 行为双层（`:200`、`:274`） | E7b `CONTESTED`；H3 潜伏（`:234`、`:377`） | 否 |
| `AttachmentSecurity` vs `Cohesion / We-ness` | `BELIEF_ONLY`（`:248`） | E12 **`UNKNOWN`**（`:241`） | **互补**：R02 提供了 R01 缺失的「无证据」登记 |
| `OutcomeDependence` vs structural derivation | `KEEP` + `MEASUREMENT_INFEASIBLE_AT_RELATION_LEVEL`（`:224`） | E10 `CONTESTED`（`:237`） | **方向一致，强度不同** |
| `PPR` vs `Trust / Care / Attachment` | `BELIEF_ONLY`（`:260`） | E5 `SUPPORTED_REDUNDANCY` **@ measurement**；E6 `INDEPENDENT`；E14 `INDEPENDENT`（`:231-232`、`:243`） | ✅ **关键分歧** |

**问题**：Gate C 是 canonical 文件里点名的 gate，两条独立 lane 对它的 4 / 6 个面给出不同答案，而**没有任何 lane 读过对方**。更严重的是 R02 的 E5 判「`Trust` / `PPR` = `SUPPORTED_REDUNDANCY` @ measurement」——这与 R01 §3.12「`BELIEF_ONLY`，禁止作 proxy」**方向相反**（一个说别把它当状态，一个说它与状态在测量上重叠）。**这两条合起来的净效果是：`PPR` 相对 `Trust` 的位置在 schema 里既不是「独立层」也不是「冗余」，而是无定义。**

### 3.2 R01 与 R07 重复「层 / 值类裁决」，且 R07 的诊断从未被消费

R07 的整个 lane 使命是 `Unknown` 的形式化；R01 却在 §3.5 / §3.10 / §3.11 / §3.12 独立做了四个**层归属**裁决（`Distrust -> OPEN`、`Satisfaction -> DERIVED`、`Cohesion -> BELIEF_ONLY`、`PPR -> BELIEF_ONLY`）。两条 lane 各自的 sibling 引用数为 0。R07 的 FM-03 诊断（`disputed` 与 `unmeasured` 不可比）与 R01 的四个裁决**没有任何交叉引用**。

### 3.3 全 swarm 唯一一次成功的跨 lane 复用（应作为范例）

R16 §3.4 **显式复用** R15 的 `evidence_channel` 受控表（`DIRECT / TESTIMONIAL / DOCUMENTARY / INFERRED / ILLEGAL_OBSERVATION / ABSENT`），并写明理由是「不新造」（`16_EMPIRICAL_VALIDATION_PROTOCOL.md:100`）。**这是 18 份报告里唯一一次有记录的跨 lane 词表复用，且它成功地把 R15 的 fixture 设计接进了 R16 的数据协议。**

### 3.4 重复劳动的根因

Wave 1 的 dispatch 让 18 个 child **并发**执行，各自带一份 `00_CHILD_CONTRACT.md`，但**没有任何 join / 合并步骤被安排在 Wave 1 内**。R16 的 mission 名义上是「Empirical validation protocol **join**」，实际是唯一一条 join lane，且它 join 的是 **R03 / R04 / R05 / R06 的结论**，不是 R01 / R02 / R07 / R10 / R11 / R15 的。→ **构念层与值类层的分歧被结构性地漏掉了。**

---

## 4. Duplicate / Collision Analysis（全部被提议的新构念）

判定枚举：`SAME_CONSTRUCT_DIFFERENT_NAME | GENUINELY_DISTINCT | OVERLAPPING_NEEDS_SCOPE_RULE | UNRESOLVED`

| # | 构念 | 提出者 | 最近邻居 | 判别式 | **verdict** |
|---|---|---|---|---|---|
| N-01 | `Obligation_(i->j)` | R11 §3.2（`11_GENERAL_HUMAN_DYADS_SCOPE.md:87-99`） | R01 §3.8 `Dedication`（`02_CONSTRUCT_CONVERGENCE.md:212`） | R01 的 `Dedication` 定义**已包含 moral-normative 来源**（引 [S05] 三来源）。R11 的 `Obligation` 由 5 条独立证据线支撑（Cicirelli 1993 `10.1037/0882-7974.8.2.144` / Montgomery, Havvey & Kosloski 1997 / 互惠研究 1995 `10.1177/104973239500500306` / Gehr et al. 2021 `10.1186/s12877-021-02425-1` / Meyer & Allen 1991 `10.1016/1053-4822(91)90011-z`），全部集中在**照护与亲属域**。重叠区 = R01 的 moral-normative facet；R11 覆盖域更宽（法定亲子中 `Dedication` 极低而 `Obligation` 极高） | **`OVERLAPPING_NEEDS_SCOPE_RULE`**：`Obligation` 按**规范来源**索引（法律 / 道德 / 机构 / ascriptive），`Dedication` 按**情感向量**索引；交集 = 「个人责任感」，必须二选一归属，否则触发 R02 H2 型双计 |
| N-02 | `Constrainedness / Control-Asymmetry` | R11 §3.3（`:101-110`） | R10 `PunitiveCapacity_(i->j)`（`10_MUTUALITY_POWER_DEPENDENCE.md:299-311`）；R02 `PowerLevel_(i->j)`（`02b_CONSTRUCT_REDUNDANCY_AUDIT.md:203`） | (a) R11 `Constraint` 覆盖面**严格包含** R10 的 punitive power，且多出 `consent_status` 与 `degree`；(b) R10 的 punitive 严格指**施加成本 / 报复**，且是唯一有**实验分离**证据的；(c) R02 的 `PowerLevel` 依据的是**知觉层面** | (a) vs (b) = **`OVERLAPPING_NEEDS_SCOPE_RULE`**（以 R11 为容器、punitive 为其中一个 `basis`）；(a)/(b) vs (c) = **`GENUINELY_DISTINCT`**（能力 vs 体验，不可互相推导） |
| N-03 | `PowerLevel_(i->j)` | R02（`:74` / `:203`，依据 C2 `:394`） | R10 `P3_perceived`（`10_MUTUALITY_POWER_DEPENDENCE.md:388`） | 同一篇来源（Overall & Hammond 2026）、同一经验结论。差别仅在**层位**。**R02 自身在 MGS-C（`:458-459`）又把它改归 `derived/readout`** | **`SAME_CONSTRUCT_DIFFERENT_NAME` + 层冲突（`DirectedState` vs `Belief`）**。全表最容易修的一格 |
| N-04 | `Legitimacy_(i,j,domain)` | R10 §4.5 + G4（`10_MUTUALITY_POWER_DEPENDENCE.md:246-259` / `:677`） | R11 `RoleContract_(A,B)`（`11_GENERAL_HUMAN_DYADS_SCOPE.md:154`） | Johnson & Ford 1996 **正交操纵**后的分离证据，与 dependence 正交。R11 的 `RoleContract` 记的是「角色、期限、权限、scope of practice、单方终止权」——制度事实，与「能否诉诸第三方 / 更高权威」不同 | **`GENUINELY_DISTINCT`** |
| N-05 | `FeltCompliance_i(j, domain)` | R10 §4.6.4（`10_MUTUALITY_POWER_DEPENDENCE.md:313-346`） | R11 `Constrainedness` | R10 自陈「理论驱动的架构主张，**证据是间接的**」，并把「没有任何研究在控制 perceived power 后检验 felt compliance 的增量」列为 U4。R11 的 U9 提出**同一检验**（`11_GENERAL_HUMAN_DYADS_SCOPE.md:395`）——**两条 lane 指向同一未执行检验** | **`GENUINELY_DISTINCT`（但 `UNVERIFIED`）** |
| N-06 | `CoupleIdentity` / `PairRepresentation` | R10 §6.3（`10_MUTUALITY_POWER_DEPENDENCE.md:618-635`） | R01 `Cohesion/We-ness`（`02_CONSTRUCT_CONVERGENCE.md:248`）；R11 `CohesionScope`（`11_GENERAL_HUMAN_DYADS_SCOPE.md:135-142`） | 见 CF-04 | **`UNRESOLVED`**。tie-breaker = R10 自带 falsifier，**未被任何 lane 执行** |
| N-07 | `SituationStructure`（`Omega`） | R10 §3 + G1（`10_MUTUALITY_POWER_DEPENDENCE.md:108` / `:674`） | R11 L-9（`11_GENERAL_HUMAN_DYADS_SCOPE.md:282-289`） | 见 CF-09 | **`UNRESOLVED`**（纯架构裁决；R10 的判别测试在当前 schema 下已可执行） |
| N-08 | `CommonDyadicCoping_(A,B)` | R10 §4.8（`10_MUTUALITY_POWER_DEPENDENCE.md:443-478`） | 无 | 唯一有**直接判别实验**支持的 pair-level 涌现候选（Bodenmann, Meuwly & Kayser 2011, `10.1027/1016-9040/a000068`, N = 443；meta `Falconier et al. 2015`, 72 samples / 17,856 人, r = .45）。R10 明确说这**只证明「两条有向状态的函数不够」，不证明「必须有独立 pair state」** | **`GENUINELY_DISTINCT`**（**过程** vs 内容，与 `Omega` / `PairRepresentation` 都不同） |
| N-09 | `ExchangeStructureType_(i,j,domain)` | R10 §4.7（`10_MUTUALITY_POWER_DEPENDENCE.md:427-435`） | R06 `RT` 的 `Λ+ / Λ-`（`06_TRANSITION_LAWS.md:741-749`） | R10 的论点是「reward 互惠与 punishment 互惠**可分离且可同时提升**」（Gneezy & Fessler 2012 `10.1098/rspb.2011.0805`）。R06 律 E 也主张「存在一条独立的正向（趋近）分支」+「存在一条独立的抑制 / 修复分支」——**但 R06 把两者作为行为层的两条通道，R10 把它们作为交换结构的类别值** | **`OVERLAPPING_NEEDS_SCOPE_RULE`**：R06 是**行为频率**，R10 是**结构类别** |
| N-10 | `Alternatives_(i, ref=(j))` | R10 §4.4 / §4.5（`10_MUTUALITY_POWER_DEPENDENCE.md:224` / `:246`） | R02 `QualityOfAlternatives`（`02b_CONSTRUCT_REDUNDANCY_AUDIT.md:211`）；R03 D1 / O8（`03_MEASUREMENT_INSTRUMENTS.md:115` / `:132`）；R11 L-1（`11_GENERAL_HUMAN_DYADS_SCOPE.md:195-205`） | 四条 lane 指向同一 Rusbult 分量。R10 加**唯一的新东西** = 「带 pair 参照的序数 / 集合值，不是标量」。**R11 独立地提出同一条要求**（`11_GENERAL_HUMAN_DYADS_SCOPE.md:342`：「每个比较型坐标（`ValueCongruence` / `GoalAlignment` / Investment Model 的 `alternatives`）的 **reference class 定义**」） | **`SAME_CONSTRUCT_DIFFERENT_NAME`**，且**这是全表最健康的一处重复**：R10 与 R11 独立收敛到同一条修法。无冲突，只有登记 |
| N-11 | `RoleContract_(A,B)` | R11 §3.7（`11_GENERAL_HUMAN_DYADS_SCOPE.md:144-154`） | `AGENTS.md` 架构方向第 3 条 | R11 明写「这是对**现有架构裁决的挑战**，不是变更提案」——在 >=3 类 dyad（专业 / 亲属 / 照护）上 role / contract 是**状态成分**。这是全 swarm 唯一一处直接挑战 `AGENTS.md` 正文的提议 | **`UNRESOLVED`，但须升级到 Human 层级。** 本报告不主张 R11 对，也不主张 Architect 条目错 |
| N-12 | `Ambivalence` | R11 §3.5（`11_GENERAL_HUMAN_DYADS_SCOPE.md:122-133`） | R17 §3 F4（`17_RED_TEAM_FALSIFIERS.md:179-198`） | **两条 lane 独立发现同一构念，证据互补**：R11 用 family science（Bengtson et al. 2002 `10.1111/j.1741-3737.2002.00568.x`；de Bel, Kalmijn & van Duijn 2019 n = 549 `10.1177/0192513X19860181`；Blake et al. 2022 `10.1177/0192513X211064876` 参与者原话）；R17 用 relationship science（MacDonald et al. 2013 N = 1004 `10.1177/0265407512465221`；Zoppolat et al. 2023 N = 1136）。**R17 提供了 R11 没有的关键区分**：`objective` 与 `subjective` ambivalence 解离，**subjective 最强且与 objective 不一致** | **`OVERLAPPING_NEEDS_SCOPE_RULE`，且应合并为一个提案**。R17 的 R4 退守条件（`17_RED_TEAM_FALSIFIERS.md:398-399`）比 R11 的命名状态更强 |
| N-13 | `ScopeApplicability`（值类）/ `DyadScopeProfile` | R11 §3.1（`11_GENERAL_HUMAN_DYADS_SCOPE.md:77-85`） | R07 / R13 / R15 / R16 的「无值」词表 | 见 CF-12。R07 的 tag 集合是唯一**超集**且带**正交性声明** | **`SAME_CONSTRUCT_DIFFERENT_NAME`；SSOT = R07 §9.3** |
| N-14 | `Belief_i(perceived value similarity)` | R02 §3.3（`02b_CONSTRUCT_REDUNDANCY_AUDIT.md:206`），依据 C5（`:397`） | R11 §6.2 | R02 的 Montoya et al. 2008 `10.1177/0265407508096700`（既有关系 actual `r = .08` vs perceived `r = .32`）与 R11 §6.2 的推论**方向一致**；R02 H5 已把这条登记为高危双计点（`:379`） | **`OVERLAPPING_NEEDS_SCOPE_RULE`**（R02 自己已提出该规则）。**R02 与 R11 独立收敛 -> 记为 convergence** |
| N-15 | R07 全部提案（`evidence_mass` / `reporter_role` / `value_class` / `REFUSE` / `(1,-1)` contrast 建模） | R07 §9.3（`07_PARTIAL_OBSERVABILITY.md:470-489`）、FM-09（`:359-364`） | 无 | 全部是**证据侧类型**，不新增人类关系构念（R07 §9.3 自陈）。FM-09 是全 swarm 唯一一条「统计方法与 canonical invariant 直接冲突」的机制：单一人口超参数对 `Z[k,i,j,t]` 做向心收缩会**把非对称性系统性压向对称** | **`GENUINELY_DISTINCT`（全部）**。但 FM-09 需在 Architect 层面被消费——R01 §2.2 与 R10 §4.1 的残差化方案都依赖 `i->j` / `j->i` 可分离，而收缩会先腐蚀它 |
| N-16 | R08 全部 8 槽 + `Pol` + `Rel` + `Claim` + `Disclosure` 事件 | R08 §4.1–§4.5（`08b_BELIEF_DECEPTION_KNOWLEDGE.md:357-461`） | R10 `PairRepresentation_R1`；R15 A10 | `Claim_ι⊛`（以二人名义的联合承诺，R08 §4.3 称其为「**唯一**的 pair-level 原语」，`:426-429`）与 R10 的 `PairRepresentation_R1`（**持久**的共享叙事内容）在**时间语义**上不同：前者是一次 **act 的记录**，后者是 **content 的持久对象** | **`OVERLAPPING_NEEDS_SCOPE_RULE`**。R08 §2.11 已把 `Disclosure` 判为 Action/Event（`:207-210`），但**没有**把 `Claim_ι⊛` 判为 Action/Event |
| N-17 | R06 `Ideal` 升为动态 directed state（律 D `RGM`） | R06 §12 裁决请求 2（`06_TRANSITION_LAWS.md:995-997`） | R01 `P2 ValueCongruence` / `P3 GoalAlignment` | R06 自陈这是「本 lane 提出的**唯一会改变 schema 层级**的建议」。`Ideal` 是 **per-agent 参照标准**（Belief / Agent 层），P2/P3 是 **pair comparison**（Pair 层），**不碰撞**。R06 自带的 `R_i` 记号已承载它（`:38`） | **`GENUINELY_DISTINCT`**。但 R06 自评「概率最高的结局：`Ideal` 漂移 = 回溯伪影 -> 移出 state」（`:901`）——提案者自己认为它大概率会被否决 |
| N-18 | R06 `D^d` dependence 存量（律 B `APES`） | R06 §5.1（`06_TRANSITION_LAWS.md:291-296`） | R01 / R02 / R03 / R17 的 `OutcomeDependence`；R10 的 `Dependence_(i,j,S)` | 见 CF-07。全表唯一一处**四个 ontology 争夺同一 slot** | **`UNRESOLVED` + `SAME_CONSTRUCT_DIFFERENT_NAME`** |
| N-19 | R02 的 `MGS-A` / `MGS-B` / `MGS-C`（3 / 2 / 4 节点） | R02 §9（`02b_CONSTRUCT_REDUNDANCY_AUDIT.md:410-468`） | R11 `Obligation`（-> 9 节点）；`PARAMETER_CONVERGENCE_V0_1.md` §11（8 节点） | 三个 MGS 是 R02 自标的**显式临时假说**（`:408`），R02 不主张任一为真。全 swarm 的 basis 规模**跨度 2 -> 4 -> 8 -> 9+**，且**没有任何 lane 提出裁决程序** | **`UNRESOLVED`（by design）**。须记录一条**程序性缺口**：R01 §2.3 主张 8 维的正当性来自**表示需要**（`02_CONSTRUCT_CONVERGENCE.md:95`），R02 的 MGS-C 主张 4 维足够，R11 主张 9 维不够——三条 lane 对「什么算正当理由」本身没有共同定义 |
| N-20 | R13 的 `support_set` / `residual_ambiguity` / `prompt_derived_prior` / 提问预算硬上限 | R13 §10 R1 / R6 / R10 / R15（`13_LLM_SKILL_INTERVIEW_LAYER.md:465`、`:470`、`:474`、`:479`） | R15 `evidence_weight_note`；R16 `evidence_channel` | `support_set` 的 size = 1 禁止升格为 trait / 状态（规则 R1）**是别的 lane 都没有的约束**，与 R15 的权重（质量）和 R16 的通道**正交** | **`GENUINELY_DISTINCT`**（`support_set` = 证据**条数**）；R15 与 R16 的通道 / 权重字段之间 `OVERLAPPING_NEEDS_SCOPE_RULE` |
| N-21 | R15 的 `SIT::` 语义情境锚点集（12–20 条） | R15 §15.6.3 规则 7（`15_CASEBANK_EXPANSION.md:204`） | R11 的 9 类 dyad 矩阵（`11_GENERAL_HUMAN_DYADS_SCOPE.md:40`、`:46-71`）；R17 F9 的 Gate B 11 类覆盖矩阵 | 三者是**同一件事的三种命名**：`SIT::` 锚点 约等于 R11 的 dyad 类型列 约等于 R17 的 Gate B 11 类。R15 自陈「这是 `#13` 成功标准 4 的**唯一可执行落地方式**」。R15 已给出 9 条 `SIT::` 示例，与 R11 的 L-3 / L-5 / L-9 / L-10 高度对应 | **`OVERLAPPING_NEEDS_SCOPE_RULE`，三者应合并为一份覆盖矩阵** |
| N-22 | R12 Gate 1–7（ABM 七道门） | R12 §9（`12_COMPUTATIONAL_MODELS_ABM.md:325-368`） | R16 `FZ-0`（`16_EMPIRICAL_VALIDATION_PROTOCOL.md:404-431`）；R14 M0–M9 | R12 的 Gate 1–7 是 **ABM-specific** 的采纳前置（calibration target / validation target / out-of-sample / equifinality / verification / ergodicity / regime） | **`GENUINELY_DISTINCT`**。但 R12 Gate 4（equifinality probe，引 Schindler 2013, `10.18564/jasss.2274`：「同一设计策略下 8 个同样可辩护的版本，magnitude 和 direction 都显著不同」，`12_COMPUTATIONAL_MODELS_ABM.md:69-70`）应被 R16 的 `B6 MODEL_UNCERTAINTY_FLOOR` 消费——R16 已引用 R05 SD18 引用同一现象（`:207`），但**未引用 R12 的方法模板** |

---

## 5. 可组合性检查（Composability Check）

### 5.1 一句话结论

**不能整体执行。** 可以执行的部分是「用 R03 的 instrument 当**外部效标**、用 R04 的三个结构合格数据集、在 R16 的冻结协议下、检验 R16 的 null 集合（`B1` / `B2` / `B5`）能否被击败」；**不能**执行的是任何一条 R06 律族的判别部分、任何跨数据集泛化主张、以及任何依赖 `MAPPING_FAILURE` 的诊断。

### 5.2 逐条要求是否可同时满足

| 要求 | 来源 | 状态 | 依据 |
|---|---|---|---|
| 每个 directed 坐标需 **self-report belief 通道 + 独立 behavioral / physiological 通道** | R03 §4.2 Q1 / G9：「**没有任何已验证坐标同时拥有自陈信念通道与行为 / 生理独立通道**」；R16 `F-06`（阻断级） | ❌ **不可满足** | `03_MEASUREMENT_INSTRUMENTS.md:262`；`16_EMPIRICAL_VALIDATION_PROTOCOL.md:394` |
| 律 A（`BMR`）的判别部分需要「对方行为的独立观察 + 双方各自信念的独立报告」 | R06 §10 U-1；R16 `F-05`（结构性） | ❌ **不可满足**（R06 自认） | `06_TRANSITION_LAWS.md:911-916`；`16_EMPIRICAL_VALIDATION_PROTOCOL.md:393` |
| 律 E（`RT`）需要 event-contingent 记录 + **事件内顺序** + lag-0 / lag-1 可分辨 | R06 §8.6（硬性）+ C-A | ❌ **不可满足** | `06_TRANSITION_LAWS.md:830-833`、`:74-81` |
| 律 B（`APES`）需要 **>=4 wave** | R06 §9 最小可测设计 | ⚠️ **勉强**：pairfam 14 / SHARE >=8 满足；HARP 只有 3 -> HARP 不可用于律 B | `06_TRANSITION_LAWS.md:900`；`04_DATASET_LANDSCAPE.md:57` |
| 律 C（`DVA`）需要**真实起点波次** | R06 §9 | ⚠️ 三个数据集都没有「关系起点」波次（HARP 的 T1 已是合法婚姻 + 同居 >=3 年） | `06_TRANSITION_LAWS.md:900`；`04_DATASET_LANDSCAPE.md:57` |
| `directionality_class = DIRECTED_EDGE` 的双分量 | R16 §3.2 结论：「在 R04 审计的 16 个数据集中，**只有 1 个**（速配）提供无外部假设的 `DIRECTED_EDGE` 双分量，而它**没有第二个时间点**」 | ❌ **不可满足** | `16_EMPIRICAL_VALIDATION_PROTOCOL.md:85` |
| 跨数据集泛化（`#29` F 层） | R04 §8 矛盾 9：「**这四个条件的交集为空**」；R16 `F-03`（阻断级） | ❌ **不可满足** | `04_DATASET_LANDSCAPE.md:864`；`16_EMPIRICAL_VALIDATION_PROTOCOL.md:391` |
| split 几何 `G1_BLOCKED_FORWARD`（需 >=3 wave） | R16 §6.2 / §6.3 | ✅ **可满足**（pairfam 14 / SHARE >=8 / HARP 3） | `16_EMPIRICAL_VALIDATION_PROTOCOL.md:173`、`:191` |
| `invariance_level_tested` 必填且 `NOT_TESTED` 须进正文 | R16 §3.4 + `R16-UC06` | ⚠️ **可满足但结果几乎必然是 `NOT_TESTED`**：R03 §3.4 列出「完全无不变性证据」的族包含 RCI / DTS / IMS / VFI / RMBM / IOS / RPI / RBA / 3VDI / PRI / PPRS；R04 U15（三个数据集的**构念内容**未核实） | `03_MEASUREMENT_INSTRUMENTS.md:234`；`04_DATASET_LANDSCAPE.md:888`；`16_EMPIRICAL_VALIDATION_PROTOCOL.md:221` |
| 关系终止作为 outcome | R06 U-3 / R16 `R16-OC03` / R16 `F-04` | ❌ **不可满足**（censoring by design） | `06_TRANSITION_LAWS.md:924-929`；`16_EMPIRICAL_VALIDATION_PROTOCOL.md:140`、`:392` |
| `mapping_status` 变量级 codebook | R16 `F-01`（阻断级）：「§8 的 5 行里有 3 行的**变量级 codebook 未核实**… **§8 因此是模板，不是规格**」 | ❌ **不可满足**（今日） | `16_EMPIRICAL_VALIDATION_PROTOCOL.md:389`；`04_DATASET_LANDSCAPE.md:888` |
| `side-swap` 检验（`R16-ID05`） | R16 `F-12`：「**无参照量表**」 | ⚠️ **可满足但无参照规格** | `16_EMPIRICAL_VALIDATION_PROTOCOL.md:400` |
| LLM 参与的验证流水线 | R04 §5.1：Add Health（全部禁止）/ UAS（全部禁止）/ SHARE（禁止非完全自管应用 + 禁止 AI 训练）/ HRS（NIH Certificate of Confidentiality，**即使法院命令或传票也不得披露**）/ pairfam（§3 只允许汇总呈现） | ❌ **对全部三个 `CALIBRATION_READY` 数据集不可满足**。唯一已知合规路径 = ICPSR SOMAR VDE / MiCDA Enclave 内的自托管模型 | `04_DATASET_LANDSCAPE.md:771-784`、`:818`；`16_EMPIRICAL_VALIDATION_PROTOCOL.md:417` |
| Case Bank 官方材料路线 | R04 §5.2 结论 2 | ✅ **与 R16 不冲突**（R16 走问卷侧、R15 走公开叙事侧；R04 §5.2 结论 3 明说这「为 LHRM 提供了一个结构性回旋空间」） | `04_DATASET_LANDSCAPE.md:794-801` |
| `MAPPING_FAILURE` 可达并具诊断力 | R17 F1 + F11；R16 `F-08`；R15 的 7 值表仍含 `NARRATIVE_ONLY` / `IRRELEVANT` | ❌ **不可满足** | `17_RED_TEAM_FALSIFIERS.md:108-121`、`:342-352`；`16_EMPIRICAL_VALIDATION_PROTOCOL.md:396`；`15_CASEBANK_EXPANSION.md:198` |

### 5.3 具名的不可同时满足的要求（Unsatisfiable Requirements Register）

| id | 不可满足的要求 | 冲突双方 | 判断 |
|---|---|---|---|
| **U-1** | 「R03 要求的双通道测量」 与 「R04 找到的可用数据集」 | R03 G9 / R16 `F-06` vs R04 全部 16 个数据集 | **结构性不可满足。** R16 自己标为**阻断级**并明说「协议**不能**解决，只能**显式命名**」 |
| **U-2** | 「R06 律 A 的判别内容」 与 「R16 的协议」 | R06 U-1 vs R16 `F-05` | **不可满足，R06 与 R16 已共同记录。** 本报告只补一条：**R06 §12 的 5 条裁决请求中没有一条是「U-1 使律 A 不可证伪该怎么办」** |
| **U-3** | 「R06 律 E 的 event-internal ordering + lag-0 / lag-1」 与 「R09 提议的 `tau` = 月—年级」 与 「R16 `G1_BLOCKED_FORWARD` 的 wave 级切分」 | R06 C-A / §8.6 vs R09 O8 vs R16 §6 | **不可同时满足。** R09 §6.2 自称「年度数据只能看到 1–2 个恢复点」；R16 §6.2 的唯一可采纳几何是 wave 级 dyad 分组前向切——两者都无法提供事件内顺序 |
| **U-4** | 「R05 I4 / I14 要求的方向性分解」 与 「R01 §9.1 / R10 A1 要求的 `R` / `T` 残差化写入 schema 与派生规范」 | R05 I4 / I14 vs R01 / R10 | **不可同时满足为「估计值」；可同时满足为「架构占位符」**（R05 I4 已给了这个出口）。**缺的是 R01 / R10 侧的限定语** |
| **U-5** | 「R11 U1 要求 Gate C 之前先做 4 组 x >=300 dyad 的 invariance 序列」 与 「R05 I11 判定 cross-context test `BLOCKED_BY_DATA`」 | R11 U1 vs R05 I11 | **排序死锁。** 若 R05 对，则 **Gate C 在当前数据条件下不可执行**；R11 的排序要求会使整个 Gate C 停摆。**这个死锁未被任何 lane 记录** |
| **U-6** | 「R04 §5.2 的 Case Bank 官方材料路线」 与 「R16 `FREEZE_RECORD` 字段 2」 与 「R15 fixture header 的 rights 字段」 | R04 vs R16 vs R15 | **可同时满足**（走不同制度通道），但 **R15 的 fixture header 没有 `llm_use_condition` 字段**（R04 §5.2 建议 1 明确要求加）-> 三个 lane 对**同一个 artifact** 给了三套 rights 字段集，无交叉映射 |
| **U-7** | 「R16 的 6 值 `mapping_status`」 与 「R15 的 7 值 verdict」 与 「R17 F1 对后者的可达性证明」 | R16 vs R15 vs R17 | **可并存**（粒度不同），但 **R17 的攻击只落在 R15 那套上，R16 那套从未被做可达性分析**；且 R15 的九类归因与 R07 的 tag 集无交叉映射 |
| **U-8** | 「R16 的 7 值 `invariance_level_tested`」 与 「R13 的 3 值 `construct_alignment`」 | R16 vs R13 | **不可在同一字段上同时满足**（值集不同、粒度不同）。R16 侧更严且已被 `R16-UC06` 强制进正文 |
| **U-9** | 「R06 §11 非主张 3：各律假定现有层归属」 与 「R17 F3 / R2：层归属本身要改」 | R06 vs R17 | **逻辑上不可同时满足。** R06 明说「若 Gate C 冗余审计合并其中任一项，对应律族**必须重新推导**，不能只重新拟合」；R17 R2 是**最可能发生**的退守。-> **一旦采纳 R17 R2，R06 五族全部需重新推导。这是一条未被任何 lane 记录的下游爆炸半径** |
| **U-10** | 「R16 `L5(d)`：`NO-PARTNER` 必须作为真实竞争模型」 与 「R06 五律全部主张 partner 侧输入」 | R16 vs R06 | ✅ **可满足**（这正是 R16 的设计意图）。记为 **convergence** |
| **U-11** | 「R17 F7：文本 benchmark 与生态效度正交」 与 「R15 §15.6 全部 Case Bank 路径都是文本」 | R17 vs R15 | **不可同时主张。** R15 §15.6.3 规则 8 的泄漏探针**只测 future leakage，不测隐式 / 显式正交性**。这是 CF-14 之外的第二个 coverage 缺口 |

### 5.4 因此**可以**执行的那一小块

| 可执行项 | 条件 | 用哪条 lane 的资产 |
|---|---|---|
| 在 pairfam / SHARE 上用 `G1_BLOCKED_FORWARD` 几何问一个**纯描述 / 预测**问题：「`PPR`（Belief 层读出）是否比 `Trust`（directed 读出）更能预测 `satisfaction` 读出？」 | (a) `mapping_status` 全行填 `DIRECT_ITEM` 或 `DERIVED_COMPOSITE`，无 `BEHAVIORAL_PROXY`；(b) `invariance_level_tested` 如实填（很可能 `NOT_TESTED`，则结论标 `UNDEFINED`，`R16-UC06`）；(c) null 集合 = `B0 / B1 / B2 / B3 / B5 / B6`；(d) `rights_and_processing_mode` 须为真，否则改走 SOMAR VDE | R03、R04、R16、R05、R01 |
| **这条是唯一值得做的实证，其结果直接裁定 CF-02 与 CF-03** | — | — |
| 用 R15 的 `SIT::` 锚点集发布「12 份现有材料 x Gate B 11 类 x R11 9 类 dyad」的覆盖矩阵 | 零数据接触、零 access 需求 | R17 F9 的原话、R11 L-8、R15 §15.6.3 规则 7 |
| 用 R15 的 T3 `fact_status` 翻转（`DERIVED_TRANSFORM`）直接测「provenance 等级 != fact status」这条纪律 | Carty 与 LGSO 已冻结，近零采集成本 | R15 §15.6.4 |

---

## 6. Convergence Map

### 6.1 强收敛（四条及以上 lane 独立同意，且多为**否定性 / 限制性**主张）

| # | 收敛结论 | 参与的 lane |
|---|---|---|
| G-01 | **`State != Action`；行为 / proxy 不自动升格为 primitive** | R01、R02、R03（判 `DIRECT_PROXY`（对 Action 层）并「**本 packet 支持该降级**」）、R09、R13、R16、R17（A10 `UNCHALLENGED`）、R12——**8 lane，最强收敛** |
| G-02 | **关系终止是设计性删失，不能用受访者数据检验** | R06 U-3、R16（`R16-OC03` + `F-04` + L8）、R17 F6a、R04 §6（提供替代通道） |
| G-03 | **`MAPPING_FAILURE` 在当前 schema 下不可达；Case Bank 不具判别力** | R17 F1 + F11 + 退守条件 R1 / R5、R16 `F-08` + `F-SELF01`、R09 §7 O5——**方法独立** |
| G-04 | **方向性分解（SRM 三成分）在纯 dyad 数据下不可识别** | R05 I4 + I14、R12、R16 `F-07` + §13 I4、R11 §3.8、R14 §2.1——**5 lane**。**唯一例外：R01 与 R10（CF-10）** |
| G-05 | **关系科学的大规模纵向校准数据 100% 是恋爱 dyad** | R17 §1.3 + A8 + F6、R11 §3.7、R03 §3.4、R06 U-1 / U-3 |
| G-06 | **「逆变 / 未知 / 不可测」必须显式，不得静默 coerce** | R07、R11 §3.1（R11 自列的 X-3：「`Unknown` 是唯一非数值值类 -> 结构性不适用**必然**被 coerce 成 0」）、R15、R16、R06（`⊥` 规则）、R13 R4、R08 §4.2 槽位 5——**7 lane。收敛于原则，不收敛于类型**（CF-12） |
| G-07 | **PRQC 的二阶「总体关系质量」因子意味着 LHRM 8 维不是已发现的因子结构** | R14 §2.2 + F-4、R03 §3.3、R01 §2.3、R02 E1 |
| G-08 | **`fixture` / `Case Bank` 输入的独立性不足（准备者与 ontology 作者重叠）** | R17 F9 第 3 点、R00 §7 S-3 / S-4、R15 §15.6.3 规则 9 |
| G-09 | **文本 benchmark 不能验证状态表示（生态效度）** | R17 F7、R14 §2.5、R13 |
| G-10 | **有序 / 类别变量不能当连续处理** | R06 C-C、R09 §8.1(4)、R16 §3.4 `floor_ceiling_risk` |

**读法**：G-01 到 G-10 **全部是「什么不能做」或「什么不能声称」**。**全 swarm 在否定性主张上高度一致。** 这本身是本 attempt 最重要的元结论。

### 6.2 中度收敛（两条 lane 独立同意，方法不同）

| # | 收敛结论 | lane 对 |
|---|---|---|
| G-11 | **`Investment Model` 家族的系数跨关系类型漂移**，`Dedication` 的 universal basis 地位可疑 | R17 F8（Le & Agnew 2003 `10.1111/1475-6811.00035`「significantly stronger in relational domains」；Branje et al. 2007 `10.1111/j.1475-6811.2007.00173.x`；Brooks, Ogolsky & Monk 2019 `10.1177/0192513X18758343`；Sandberg et al. 2022 `10.3389/fpsyg.2022.912978`）x R11 §5 + L-3 x R02 §5.2 |
| G-12 | **`alternatives` / 比较型坐标必须带 `reference_class` 定义** | R10 §4.5 x R11 §6.5(c)——**独立收敛，应立即采纳** |
| G-13 | **实际相似度 vs 知觉相似度必须分成两个坐标** | R02 C5 / E11b / E11c / H5（Montoya, Horton & Kirchner 2008 `10.1177/0265407508096700`：actual `r = .08` vs perceived `r = .32`）x R11 §6.2 |
| G-14 | **`Ambivalence` 是一等现象，不能由「几个坐标低的组合」表达** | R11 §3.5 x R17 §3 F4——**证据互补而非竞争** |

### 6.3 真正的残余分歧（不是 scope 造成的）

| # | 分歧 | 为什么不是 scope 差异 |
|---|---|---|
| D-1 | `Dedication` 的层位（CF-01） | 双方读的是同一份 Investment Model 定义式；差别是**是否接受「primitive 可以在其源理论里被方程定义」**。这是记账原则之争 |
| D-2 | `PPR` 的层位（CF-03） | 三方对**同一个量**给出三种互斥处置，且 R14 把争议当作不存在。这是本体论之争 |
| D-3 | 是否允许 pair 级内容对象（CF-04） | R01 与 R10 各有独立经验证据，且两条证据测的不是同一个东西 |
| D-4 | `OutcomeDependence` 的本体归属（CF-07） | 四种互斥 ontology；R17 明确说「找不到直接反证」——**这是最诚实也最无解的一格** |
| D-5 | 缺口是 ontology hole 还是 query lens 太窄（CF-09） | 纯架构裁决。R10 的判别测试在当前 schema 下已可执行 |
| D-6 | `Distrust` 的独立性（CF-06） | R03 的直接证据在 workplace 域；R01 的 artifact 论证预测在关系域失效。**两条 lane 都没说清域** |
| D-7 | canonical `tau` 应是月—年级还是需事件内分辨率（CF-11） | 纯架构决定，但有直接后果：R06 律 E 的可证伪性与 R09 的 L-A–L-D 离散层二者只能选一个 |
| D-8 | `Role` 是 query lens 还是状态成分（N-11） | R11 直接挑战 `AGENTS.md` 正文。**必须上升到 Human 层级** |
| D-9 | `Satisfaction` 是 readout 还是 state（CF-02） | 主要是**术语**冲突，但若不区分「进入 dynamics 的输入」与「进入 state 坐标的元素」，R17 的 R2 退守会被误读为要求 R01 撤回 §9 R3 |

---

## 7. 剩余未知（remaining unknown）

| # | 未知 | 为什么本审计无法定 | 需要什么 |
|---|---|---|---|
| A2-U1 | `Dedication` 在控制 satisfaction + investment + alternatives 之后是否仍有稳定增量 | 需要纵向 dyad 数据；R02 U-1..U-10 全是需要新采集的研究 | 一次含 IMS 三成分 + 至少两个 outcome 的 >=3 wave dyad 面板 |
| A2-U2 | couple identity clarity 在加入 joint `Action/Event` 历史后是否仍有增量 | R10 已写出 falsifier（`10_MUTUALITY_POWER_DEPENDENCE.md:635`）但无 lane 执行 | 一次同时测 clarity + 共同行动事件史的 >=3 wave 研究 |
| A2-U3 | `PPR` 升入 state 层后，R06 判 B4（lag-0 联合模型）是否还有意义 | **语义层**问题，不是数据问题；在 Architect 裁决前无法回答 | Architect 对 CF-03 的裁决 |
| A2-U4 | `Role` 是否在 >=3 类 dyad 上是状态成分 | R11 挑战 `AGENTS.md` 正文；本审计无权裁决 Human requirement | **Human 裁决** |
| A2-U5 | 三个 `CALIBRATION_READY` 数据集是否含 LHRM 构念题项 | R04 U15；本审计无数据访问 | 取得 pairfam codebook / scales manual + SHARE / HARP 同类清单（`04_DATASET_LANDSCAPE.md:909` 已列为 P0） |
| A2-U6 | HARP T2/T3 微数据是否已 release | R04 U6：ICPSR 落地页与 datadocumentation 页互相矛盾 | 直接向 ICPSR 查询 |
| A2-U7 | `measurement_channel` 性别差异（男 .66 / 女 .26）在非二元性别样本上的复制 | R01 U12 | Chivers / Laan 综述的调节变量跨文化复制 |
| A2-U8 | 五个 lane 的「无值」词表在**实际 fixture 上**会产生多少 `UNKNOWN` vs `MAPPING_FAILURE` 混淆 | 需要在 schema 落地后统计；R07 FM-05 警告「大量输出 Unknown 不是好分数，必须同时报 coverage 趋势」 | 先有统一词表（CF-12 的修复），再跑 |
| A2-U9 | `FeltCompliance` 在控制 `PerceivedPower` 后的增量 | R10 U4 与 R11 U9 指向**同一未执行检验** | 同一样本同时测 RPI + chilling / compliance 量表 |
| A2-U10 | 是否存在「无标签、低语义冗余、语义跨关系类型稳定」的 6–9 维候选 basis | 全 swarm 的 basis 提案跨度 2 / 4 / 8 / 9+（N-19），且无任何 lane 提出裁决程序 | 先有裁决程序，再有数据 |
| A2-U11 | R04 / R15 / R16 三套 rights 字段集的合并 schema | 需要 Human 对「Case Bank 材料」是否单一 artifact 做裁决 | Architect 裁决 + R04 §5.2 建议 1 的字段落地 |
| A2-U12 | 若采纳 R17 R2，`PPR` 升为 state 层后 `Belief_i(X)` 与 `X` 的类型关系如何设计（循环风险） | R17 R2 自己点出该风险（其 U6），但未给出方案 | Architect 裁决 + 一次类型系统设计 |
| A2-U13 | `Mutuality / Asymmetry` 派生在 `R` / `T` 不可识别条件下应退回哪种表示 | R05 I4 禁止把 `R` / `T` 写成估计值；R10 A1 要求残差化；两者相加后派生式无输入 | 一次 round-robin / 交叉设计采集（当前无任何数据集满足） |

---

## 8. 明确不主张什么（explicit non-claims）

1. **不主张本报告的任何一条冲突裁决改变了 canonical ontology、参数、权重、公式或 schema。** 全部是 `RESEARCH_CANDIDATE` 观察。§10 的 `NARROW_REPAIR_REQUEST` 是给 parent / Architect 的**建议**，不是已执行的修改。
2. **不主张本审计重新核实了任何 lane 的经验主张。** A/B 两侧引文全部是**对 durable 正文的逐行引用**；两条 claim 之间的**相容性**由本报告裁决，两条 claim 各自的**真伪**由 A01 / A04 裁决。
3. **不主张 §2 里任何一条是「某 lane 写错了」。** 绝大多数是 scope 不同或从未被放在一起比较过（CF-00）。本报告明确把 **CF-15 / CF-16 / CF-20 / CF-21** 记为 `COMPATIBLE`，就是为了不制造矛盾。
4. **不主张 Crossref 核验之外的任何文献身份结论。** CF-18 是**唯一**一条本审计做了独立核验的引用裁决。
5. **不主张 R02 / R03 在 `r = .25` vs `.26` 上谁对**（CF-19）。三个数字可能全部正确，指向不同子估计。
6. **不主张 R11 对 `AGENTS.md` 第 3 条（Role 是 query lens）的挑战成立或不成立。** 本报告只记录挑战的存在与位置（N-11 / D-8），并把它标为**必须上升到 Human 层级**。
7. **不主张采纳 R10 的 `OutcomeDependence` 删除方案，也不主张驳回它。** 本报告只指出：R01 / R02 / R03 / R17 四条共享「关系级无验证量表」前提而 R10 是唯一主张删除的一方，且删除会引发 R06 `APES` 的重新推导。
8. **不主张 `PPR` 应升为 state 层，也不主张它应留在 Belief 层。** 本报告只指出这是三方互斥 + 一方（R14）把争议当作不存在，并把 R06 判 B4 的失效条件写明。
9. **不主张任何 `NARROW_REPAIR_REQUEST` 已被执行。** 它们是文本级建议，执行需走 `AGENTS.md` Mutation discipline（隔离 branch + PR）。
10. **不主张本审计读过 LHRM issue `#20` / `#21` / `#22`。** 未读取、未执行、未引用。沿用 R17 §0 的隔离姿态，同样未读取 `docs/research/RESEARCH_REPORT_*`。
11. **不主张 Eye / Juece / Juece `#30` / PR `#31` 的任何内容。** 未触碰。
12. **不主张本 swarm 的 150+ 指针目标已达成。** CF-00 的拓扑观测直接说明：在 A04 完成跨 lane 全局去重前，各 lane 自报指针数**不可相加**。
13. **不主张 `MGS-A/B/C` 中任何一个正确。** 本报告只指出 N-19 的规模跨度与程序性缺口。
14. **不主张「Gate C 不可执行」这一结论。** U-5 指出的是**排序死锁**，其解法可能是重排 Gate C 顺序而非取消 Gate C。
15. **不主张 R06 / R09 的尺度冲突应按 R09 或按 R06 解决。** 本报告只指出二者不能同时成立，并指出该冲突**未被任何 lane 记录**。
16. **不主张 R15 的 `SIT::` 锚点集应成为唯一的 dyad 分类法。** 本报告只指出 N-21 中三者是同一件事的三种命名，并建议合并为一份覆盖矩阵。

---

## 9. 建议状态

**`SUCCESS`**

理由：(a) 7 个类别全部有覆盖，每条冲突都给出了 lane + 精确主张 + `文件:行号` + `incompatibility_kind`，**无一条**是「语气不同」式观察；(b) 22 个被提议的新构念全部有 verdict，四值枚举无空缺；(c) 可组合性检查给出 11 条具名不可满足要求（U-1..U-11），其中 3 条（U-5 排序死锁、U-7 词表覆盖缺口、U-9 下游爆炸半径）是**本审计新发现的、任何单 lane 都不可能发现的**跨 lane 后果；(d) convergence map 给出 10 条强收敛 + 4 条中度收敛 + 9 条真残余分歧，并把「哪些分歧其实只是术语 / 范围差异」明确标出；(e) 12 条 `NARROW_REPAIR_REQUEST` 全部是文本级，**不需重做任何研究**；(f) 1 条独立核验（Crossref）定案了一条被 3 个 lane 依赖的引用冲突；(g) 明确记录了 4 处 `COMPATIBLE`，履行了「不制造矛盾」的义务。

**不是 `PARTIAL` 的理由**：本审计的输出是**比较性**的，其质量上限由 Wave 1 的可读集合决定，而该集合是完整的（18 份报告全部读到）。

**但必须随本文件一起传播的三条限制**：

1. 本审计的裁决对象是**文本**，不是**世界**。任何一条冲突都可能在其中一侧的引用被 A01 推翻后自动消失。
2. §6.1 的强收敛有一个共同特征：**全部是「什么不能做」或「什么不能声称」**。**全 swarm 在否定性主张上高度一致，在「什么该做」上分裂。** 这本身就是本 attempt 最重要的元结论，应写进 synthesis。
3. `00_MANIFEST.md` B-3（跨 lane 去重未做）在 A04 完成前仍然成立；本报告的 §2 与 §4 是**结构性去重**（哪些结论互斥 / 哪些重复），不是**来源去重**（哪些 DOI 重复）。

---

## 10. `NARROW_REPAIR_REQUEST`（发给指定 lane）

**全部为文本级，不需重做任何研究。** 执行需 parent / Architect 走 mutation discipline。

| id | 收件 lane | 请求 | 具体位置 | 理由 | 优先级 |
|---|---|---|---|---|---|
| **N-01** | **R07**（抄送 R11 / R13 / R15 / R16） | 请把 R07 §9.3 的 `Unknown.tag` + `value_class` 登记为**「无值」值类的 SSOT 提案**；R11 的 `structurally_not_applicable` / `scope_unknown`、R13 的 `AMBIGUOUS_NO_UNIQUE_ANSWER`、R15 的 `UNKNOWN` / `fact_status = DISPUTED`、R16 的 `NOT_MAPPED` / `UNDETERMINED` 各自映射到该 tag 集的子集 | `07_PARTIAL_OBSERVABILITY.md:470-486` ↔ `11_GENERAL_HUMAN_DYADS_SCOPE.md:79-85` / `13_LLM_SKILL_INTERVIEW_LAYER.md:470` / `15_CASEBANK_EXPANSION.md:198-201` / `16_EMPIRICAL_VALIDATION_PROTOCOL.md:63` | R07 是唯一超集且带正交性声明；R07 §6 FM-03 已诊断「disputed 与 unmeasured 不可比」，而另外四家各自重新发明了部分解且未引用 R07 | **P0** |
| **N-02** | **R16** | 请把 §12 `F-SELF20` 的「4/5」改为「5/5」，并加一句「R17 F2 已在 packet 初稿后自行更正；本表数字以 R17 durable 正文为准」 | `16_EMPIRICAL_VALIDATION_PROTOCOL.md:475` | R16 同格已列全 5 项且 5 项都标注在 `DirectedRelationshipState` 之外；R17 `17_RED_TEAM_FALSIFIERS.md:147` 明文记录了更正 | **P0** |
| **N-03** | **R03** | 请 (a) 修正 `03_MEASUREMENT_INSTRUMENTS.md:327` 与 `:87` 对 `10.1177/0146167205276865` 的归属（该 DOI = Sibley, Fischer & Liu 2005, PSPB 31(11):1524–1536，Crossref 2026-09-27 核验）；(b) 删除重复的第 5 条引用（`:325-326`）；(c) 修正 `:20` 的 Fraley 拼写；(d) 补 `G1`–`G10` 标签的定义（至少 `G9`，它被 R16 `F-06` 引用为阻断级依据） | `03_MEASUREMENT_INSTRUMENTS.md:20`、`:87`、`:262`、`:325-327` | 本审计独立核验；`G9` 悬空导致 R16 的阻断级 `F-06` 缺少被审计对象的原始定义 | **P0** |
| **N-04** | **R01** 与 **R10**（各一句） | 请在 R01 §9.1「所有 directed 构念的三分解进入 `StateCoordinate` 结构」与 R10 动作 A1「加入 SRM 残差化前置步骤」处，各加一句限定语：「`R_k(i)` / `T_k(j)` 在 round-robin / 交叉设计采集前是**架构占位符**，不得作为估计值进入任何结果陈述；R10 §4.1 的 falsifier 在纯 dyad 数据上不可执行（R05 I4 / R12 §3.1）」 | `02_CONSTRUCT_CONVERGENCE.md:419`、`10_MUTUALITY_POWER_DEPENDENCE.md:732` | R05 I4 已给出这个出口（`05_IDENTIFICATION_AND_STATISTICS.md:360`），R16 `F-07` 也已采纳（`16_EMPIRICAL_VALIDATION_PROTOCOL.md:395`）；缺的是 R01 / R10 侧的限定语 | **P0** |
| **N-05** | **R16**（抄送 R15） | 请在 §3.1 的 6 值 `mapping_status` 上补一条与 R17 F1 同型的**可达性分析**（R17 只对 R15 的 7 值表做了）；并把 R15 §15.6.3 规则 2 的九类 `MAPPING_FAILURE` 归因与 R07 的 `Unknown.tag` 做一张交叉映射表（`DATA_INSUFFICIENT` 当前无对应 tag） | `16_EMPIRICAL_VALIDATION_PROTOCOL.md:57-64` ↔ `15_CASEBANK_EXPANSION.md:198-199`、`07_PARTIAL_OBSERVABILITY.md:470-486` | CR-8 / U-7；R16 自己已在其失败清单里承认防线「不够」（`:456`） | **P1** |
| **N-06** | **R06** 与 **R09**（联合） | 请把 C-A 与 O8 的**尺度冲突**登记为一条显式待裁决项：R06 律 E 要求 event-internal ordering + lag-0 / lag-1 可分辨（事件内尺度），R09 O8 提议把项目 `tau` 固定在月—年级并拒绝 coordination dynamics 词汇。**二者不能同时成立**；若采 R09，律 E 应标 `NOT_EXECUTABLE` 并交由 R09 主导 | `06_TRANSITION_LAWS.md:74-81`、`:830-833` ↔ `09_DYNAMIC_SYSTEMS_AND_HYSTERESIS.md:510` | CR-7 / U-3。R06 §12 的 5 条裁决请求与 R09 §8.3 的 20 条 non-claim **都没有记录这条冲突** | **P0** |
| **N-07** | **R05** 与 **R11**（联合，转 Architect） | 请就 U-5 的排序死锁给出裁决：**R11 U1 要求 4 组 x >=300 dyad 的 invariance 序列在 Gate C 之前完成；R05 I11 判定 cross-context test `BLOCKED_BY_DATA`。** 若 R05 对，则 Gate C 在当前数据条件下不可执行。请在三条出路中选一：(i) 重排 Gate C 为「先 representation coverage、后 invariance」；(ii) 把 cross-context test 从 Gate C 准入条件降为 post-hoc 报告项；(iii) 明确接受 Gate C 停摆 | `11_GENERAL_HUMAN_DYADS_SCOPE.md:387` ↔ `05_IDENTIFICATION_AND_STATISTICS.md:367` | CR-6。**任何一条单 lane 都看不到这个死锁**——R05 不知道 R11 的排序要求，R11 不知道 R05 的 `BLOCKED_BY_DATA` | **P0** |
| **N-08** | **R14** | 请在 §2.1「`PPR` 属 Belief 层」行加一个脚注：「该层归属被 R17 F3 判为 `CHALLENGED`（A20），R01 判为 `BELIEF_ONLY`，R06 §4.9 的判据预设 `Z` 与 `PPR` 分属两层；三者互斥且未裁决。本行只主张『responsive action vs perceived PPR 的区分是 prior art』，**不主张** Belief 层归属已成定论」 | `14_PAPER_POSITIONING_NOVELTY.md:43` | CR-4。R14 是唯一一份把未裁决的层归属写成 prior art 的报告，而 R17 R2 明说这是「最可能发生的一条退守」 | **P0** |
| **N-09** | **R02** | 请统一 `PowerLevel_(i->j)` 的层位（mermaid `:74` 与节点表 `:203` 归 `DirectedState`，MGS-C `:458-459` 归 `derived / readout`）；并请明确它与 R10 `P3_perceived`（Belief 层）是否同一构念 | `02b_CONSTRUCT_REDUNDANCY_AUDIT.md:74` / `:203` / `:458-459` | CR-3 / N-03。两者引同一篇 Overall & Hammond 2026、同一结论，差别只在抽屉 | **P1** |
| **N-10** | **R15** | 请在 §15.6.3 记录两条尚未被消费的红队结论：(a) R17 F7（文本 benchmark 与生态效度正交：显式 vs 隐式 `r = .00` + 预测力双重分离）——当前规则 8 的泄漏探针**只测 future leakage，不测隐式 / 显式正交性**；(b) R17 F9 第 2 点（反例集 = 项目自己的假设列表，Gate B 是确认偏误装置）——T1–T5 `DERIVED_TRANSFORM` 是唯一的部分补救，但不覆盖「反例集本身由 schema 作者选定」。另请把 R15 的 `SIT::` 锚点集与 R11 的 9 类 dyad、R17 的 Gate B 11 类写成一张逐格映射表 | `15_CASEBANK_EXPANSION.md:196-206`、`:208-222` | U-11 / CF-15 / NR-8。R15 的补救方向正确但覆盖面不足，而 R15 是唯一拥有 fixture 设计权的 lane | **P1** |
| **N-11** | **R04** | 请把 §5.2 建议 1 的 `llm_use_condition: PERMITTED / RESTRICTED_LOCAL_ONLY / PROHIBITED` 与 `icpsr_llm_type: 1/2/3` 字段，正式交给 R15（fixture header）与 R16（`FREEZE_RECORD` 字段 2）作为**同一字段的三个实现** | `04_DATASET_LANDSCAPE.md:792` ↔ `15_CASEBANK_EXPANSION.md:136-161`、`16_EMPIRICAL_VALIDATION_PROTOCOL.md:417` | U-6。三套 rights 字段集对同一 artifact 无交叉映射 | **P1** |
| **N-12** | **R03** | 请在 §4.3「→ R09」条目中补一句：state 层测量的四条来源里，**只有 PRI 有配套的 actor-partner 行为锚定**；因此 R09 需要的「分钟级观测通道」在 R03 目录里**只对应 1 个 instrument 家族** | `03_MEASUREMENT_INSTRUMENTS.md:275` | 这是 CF-11 的测量侧证据（尺度冲突的第三条），目前只有本审计把 R03 的 §3.2 表与 R09 的 O8 连起来 | **P1** |

---

## 11. 一句话总结

> **Wave 1 的真实结构是 17 条独立单点研究 + 1 条 join lane，因此它产生的主要不是分歧而是「未被比较的并置」。全 swarm 在「什么不能做」上有 10 条强收敛，在「什么该做」上分裂成 9 处真残余分歧；其中 `PPR` 的层位、`OutcomeDependence` 的本体归属、`Unknown` 值类这三处最要紧，因为它们各自有三条以上互斥主张且其中一条被另一份报告当作既成事实写下。R03 的 instrument、R04 的 dataset、R06 的 law 与 R16 的 protocol 不能整体执行（11 条具名不可满足要求），但其中有唯一一条纯预测性实证是可执行的，而它的结果恰好能同时裁定前两处层位冲突。**
