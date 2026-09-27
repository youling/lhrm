# 01 — LHRM Currentness / Gap Map

**Status:** `RESEARCH_CANDIDATE` — 本文件是研究地图，不是 canonical architecture，不含任何架构裁决。
**As of:** 2026-09-27（所有时间敏感事实的核实日期）
**Lane:** R00（Wave 1）
**Base:** `youling/lhrm@main = ee393ca24f9fbf738ac0ed839e99bdc99de6fc3a`（2026-09-27 live recheck）
**Governance at recheck:** `youling/ai-use@main = 64018d80443c1889c8aaf4a6d27ffe78f3e6dd90`
**Work branch:** `research/opencode-overnight-2026-09-27 @ ce1a774d4ca678346b2cccdd600fa19f4d30c534`（相对 main ahead 1 / behind 0）
**Round-3 repair:** 2026-09-27，lane child `A3a`（base `8adcf0bacc45c0feb5c14e65e2a45346dd488b43`）。依 Architect adjudication V1（`X-1` / `X-2` / `X-4` / `X-8` / `X-10` / `X-12`；`C-P3` / `C-P5`；`review-r2` R-A2）修订。**本次修复改了 4 处自指/分类缺陷**：§9.1 的不可执行交接（`F-09` 悬空指针）、§4.2 的两处误标 `SUPERSEDED`、§4.3 `G-22` 的双分类混写 + 已完成 lane 被记为 `ACTIVE_DEPENDENCY`、§4.3 `G-17` 的同一处悬空指针。被取代的原文**逐字保留**在各行删除线内。**本文件不含任何 canonical 改动，不含任何架构裁决。**

> 本文件严格遵守 `#30` 的边界：不改 canonical ontology / foundation / 公式 SSOT / schema / 权重 / 阈值；不 merge；不写 Eye / Juece；不污染独立 verifier lane。
> 本文件的分类标签是**映射结果**，不是**裁决结果**。任何 lane 读到 `OPEN_GAP` 时不得据此推断「应该新增 construct」；任何 lane 读到 `SUPERSEDED` 时不得据此删除历史证据。

---

## 0. 阅读须知

1. 本文件只回答两个问题：**现在什么是 current**，以及**哪些开放研究项还没有 durable 答案**。它不回答「答案应该是什么」。
2. 标签语义见 §3。分类采用「恰好一个」的互斥分配；一个对象若同时具备两种性质，按「当前对后续 lane 是否仍可作为依据」来判。
3. 标注体系严格区分：
   - `Human requirement` — Human 当前方向，已 durable 记录；
   - `existing project constraint` — 仓库内已存在的规则 / 契约 / 边界；
   - `AI recommendation` — Agent 侧建议，含 Architect 的研究性建议；
   - `empirical evidence` — 外部实证；
   - `model hypothesis` — 建模假说，未经检验。
4. 证据类型标注：`CITED_PRIMARY`（本 lane 实际打开了源）、`CITED_SECONDARY`（经转述，未打开源）、`AGENT_RECALL`（本 lane 先验，未核实）。**本文件不使用 `AGENT_RECALL` 支撑任何事实性主张。**
5. 独立 verifier lane（契约指定隔离范围，共 3 条）在本 lane 全程未打开、未列举、未总结。下文所有相关表述均以「隔离 lane」指代。

---

## 1. 核实方法与已核实基线

### 1.1 核实动作（2026-09-27）

| 动作 | 结果 |
|---|---|
| `GET /repos/youling/lhrm/branches/main` | `ee393ca24f9fbf738ac0ed839e99bdc99de6fc3a`，committer `2026-09-14T18:08:39Z`，msg `validation: freeze Fixture 003 StoryCorps oral-history package` |
| `GET /repos/youling/lhrm/git/trees/ee393ca…?recursive=1` | 23 entries，`truncated=false`；取得全仓 blob SHA |
| `GET /repos/youling/lhrm/issues?state=all&per_page=100` | 30 items（13 PR + 17 issue）；剔除隔离 lane 后 open issue = **10**；**open PR = 0** |
| `GET /repos/youling/lhrm/issues/{2,3,4,5,6,13,15,23,29,30}/comments` | 逐条 architect ruling / dispatch / delivery 原文 |
| `GET /repos/youling/ai-use/branches/main` | `64018d80443c1889c8aaf4a6d27ffe78f3e6dd90`，committer `2026-09-26T17:59:09Z` |
| 本地 `git log --diff-filter=A/--format` × 18 文件 | 取得逐文件首次落地 commit（见 §2.3） |
| `git ls-remote --heads origin` | 15 个远端分支；**无任何 `verify/*` 分支** |
| `git status --porcelain` | 空（工作副本干净） |

### 1.2 结论

`#30` body 与 `00_MANIFEST.md` 记录的 LHRM main 基线与治理基线，**在 2026-09-27 live recheck 下均无漂移**。本次 attempt 的写入面限制（仅 `docs/research/overnight-2026-09-27/`）与「不 merge / 不改 canonical / 不跨项目写入」的边界在当前状态下仍然成立。

---

## 2. 当前架构快照引用（authority map）

### 2.1 五个定义面

| 面 | 文件 | main blob SHA（不可变引用） | 关键 section anchor |
|---|---|---|---|
| **架构本体** | `docs/foundation/CURRENT_ARCHITECTURE.md` | `9fffacb31f919174b17e428c471a9c82ed1d6806` | §1 当前第一目标（L12–38）；§2 研究域与最小对象（L40–62）；§3 世界层与局部投影（L64–98）；§4 二人关系的方向性（L100–136）；§5 Construct family across scopes（L138–162）；§6 State/Action/Belief/Constraint 分离（L164–206）；§7 低冗余≠低动态耦合（L208–228）；§8 时间、轨迹与历史分支（L230–266）；§9 Measurement / Canonicalization 原则（L268–290）；§10 Case Bank 与表示完备性验证（L292–330）；§11 当前非目标（L332–346）；§12 当前工程顺序（L348–361） |
| **候选参数收敛** | `docs/foundation/PARAMETER_CONVERGENCE_V0_1.md` | `2fe7f5284d591aca96c59fb6d83221502e632755` | header `Status: CANDIDATE / NOT FROZEN`（L3）；§2 收敛判据 2.1–2.6（L41–88）；§3 顶层 state container（L90–115）；§4 D1–D8（L117–243）；§5 Belief 层 B1–B2（L245–288）；§6 Pair 层 P1–P5（L291–369）；§7 Agent 层（L371–414）；§8 降级为 Action/Observation/Proxy（L416–459）；§9 降级为 Derived/Readout R1–R5（L461–517）；§10 非 universal primitive 的表面字段（L518–548）；§11 Candidate Minimal Directed Basis v0.1（L550–583）；§12 为何暂不设「爱/亲密/嫉妒/控制欲/忠诚/化学反应」（L586–612）；§13 第一轮 representation schema 10 槽（L614–651）；§14 Measurement 暂不冻结（L653–700）；§15 Gate A/B/C（L701–750）；§16 当前结论（L752–780） |
| **构念跨域与方向性** | `docs/foundation/CONSTRUCT_SCOPE_DIRECTIONALITY.md` | `744c6e448991b9ebe2337f07ea359fde446576ce` | §1 核心原则（L12–38）；§2 方向性是一级属性（L40–93）；§3 跨 scope 不机械复制 + Attraction/Trust/Caregiving 三例（L95–147）；§4 低冗余≠动态独立（L149–183）；§5 状态/行动/策略分离（L185–211）；§6 数学直觉 `G_t` / `X_(S,O,t)`（L213–253）；§7 对 Parameter Convergence 的 6 项约束测试（L255–265）；§8 一句话结论（L267–270） |
| **验证语料** | `docs/validation/VALIDATION_CORPUS_V0_1.md` | `672de46c6692dd882a7eb348e1d54b7122ea127b` | header 元数据（L1–9）；Selection method（L19–34）；L0 段（L37–106）；L1 段（L110–176）；L2 段（L180–250）；L3 段（L254–324）；Cross-level coverage map（L328–346）；**Recommended Fixture 001–003（L348–369）→ 见 §7 S-4，已过期**；Readiness（L371–378）；What was NOT done（L380–386）；Verification log（L387–394） |
| **冻结输入**（不是 mapping 结果） | `docs/validation/fixtures/FIXTURE_001_L0_001_CARTY_FACT_PACKAGE.md` | `bdefaf73002d2a421ed755af267aa33050b3529c` | §1 Source/provenance（L7–24，含 Core dyad L18–24）；§2 Epistemic/freeze rules 7 条（L26–34）；§3 Atomic fact units C001–C026（L36–65）；§4 Frozen temporal/knowledge boundaries K0–K4（L67–73）；§5 Downstream validation rule（L75–79） |
| | `docs/validation/fixtures/FIXTURE_002_L1_003_MAGI_PACKAGE.md` | `310139be19666b71dfe2686cc56e28ecf0cf18b4` | §1 Source/provenance（L7–24）；§2 Freeze rules（L26–34）；§3 Atomic narrative/fact units（L36–103）；§4 Frozen knowledge boundaries（L104–112）；§5 Downstream use（L113–128） |
| | `docs/validation/fixtures/FIXTURE_003_L1_001_STORYCORPS_PACKAGE.md` | `0fb2184b29751e1812957d02084b80c13d020cd3` | §1 Source/provenance + rights（L10–26）；§2 Normalized source anchor convention（L28–62）；§3 Freeze rules（L63–73）；§4 Atomic units S001–S042（L74–125，Total 记于 L124）；§5 Frozen temporal/knowledge boundaries（L126–136）；§6 Eye/Juece 可消费性（L137–147）；§7 Downstream validation rule（L148–160） |

`AGENTS.md`（blob `a19d9e5ef99bd8c2e6cbd8357267d52e7dbc5eb8`）是项目本地规则入口：Representation-first invariant（6 条）、Current architecture direction（11 条）、Validation discipline、Mutation discipline。

### 2.2 三份非权威但必须保留的文档

| 文件 | blob | 分类 | 说明 |
|---|---|---|---|
| `docs/foundation/PROJECT_HISTORY_2026-09-10.md` | `10e252836ec6712fbfc7bd90ddc7acf956c379ae` | `HISTORICAL_EVIDENCE` | provenance 梳理，文件自述「不与 CURRENT_ARCHITECTURE.md 竞争 current authority」 |
| `docs/foundation/STAGE_SUMMARY_2026-09-07.md` | `ea324a10bd08a9e2d88fb1162e68447537c03fa2` | `HISTORICAL_EVIDENCE`（文件内 Status 行过期，见 §7 S-7） | 唯一集中登记 8 个成熟理论 canonical pointer（含 DOI）的地方 |
| `docs/foundation/RELATIONSHIP_EVALUATION_FOUNDATION.md` | `aa98e35bc8dea52dab5c1f4ab530c70e9d8a59c5` | `SUPERSEDED`（部分保留，见 §7 S-8） | 迁自 `youling/an#15` / blob `f7d95b6192b8a53b46905c4a67998ff1d3ca7896` |
| `docs/ARCHITECT_RECONNAISSANCE_REPORT.md` / `docs/ARCHITECT_BOOTSTRAP_REPORT.md` | `1fadbab6…` / `d8132433…` | `HISTORICAL_EVIDENCE` | 2026-09-07 接管记录 + 外部对齐（含 2 个 DOI/URL） |

### 2.3 Git provenance（逐文件首次落地 commit）

| 文件 | 首次落地 commit | 日期 | 主题 |
|---|---|---|---|
| `AGENTS.md` | `07f4d3b` | 2026-09-07 | 初始化 LHRM 并迁移关系模型基础文档 |
| `README.md` | `07f4d3b`（后经 `fd4f0e6`、`18cd72c` 修改） | 2026-09-07 | 同上 |
| `docs/ARCHITECT_BOOTSTRAP_REPORT.md` | `30ef10b` | 2026-09-07 | initialize architect bootstrap record |
| `docs/ARCHITECT_RECONNAISSANCE_REPORT.md` | `07f4d3b` | 2026-09-07 | 同上 |
| `docs/foundation/RELATIONSHIP_EVALUATION_FOUNDATION.md` | `07f4d3b` | 2026-09-07 | 同上 |
| `docs/foundation/STAGE_SUMMARY_2026-09-07.md` | `fd4f0e6` | 2026-09-07 | 固化阶段性研究 checkpoint |
| `docs/research/RESEARCH_REPORT_GAME_RELATIONSHIP_PRIMITIVES.md` | `6abd4b8` | 2026-09-07 | 合并游戏关系系统反工程报告（PR `#7`） |
| `docs/research/RESEARCH_REPORT_SCIENTIFIC_RELATIONSHIP_PRIMITIVES.md` | `ebdc4b7` | 2026-09-07 | 合并科学关系构念深研报告（PR `#8`） |
| `docs/research/RESEARCH_REPORT_REAL_WORLD_PROXY_DECOMPOSITION.md` | `14344dc` | 2026-09-07 | 合并现实世界代理词拆解报告（PR `#10`） |
| `docs/foundation/CONSTRUCT_SCOPE_DIRECTIONALITY.md` | `a025754` | 2026-09-07 | 固化构念跨域作用与方向性原则（PR `#11`） |
| `docs/RESEARCH_REPORT_DATING_APP_PARAMETER_PRIMITIVES.md` | `8074726` | 2026-09-07 | 婚恋产品字段与匹配变量反向工程（PR `#12`） |
| `docs/foundation/CURRENT_ARCHITECTURE.md` | `18cd72c` | 2026-09-10 | representation-first 项目总梳理与 Parameter Convergence v0.1（PR `#14`） |
| `docs/foundation/PARAMETER_CONVERGENCE_V0_1.md` | `18cd72c` | 2026-09-10 | 同上 |
| `docs/foundation/PROJECT_HISTORY_2026-09-10.md` | `18cd72c` | 2026-09-10 | 同上 |
| `docs/validation/VALIDATION_CORPUS_V0_1.md` | `1a02d96` | 2026-09-11 | validation corpus v0.1 material harvest（PR `#17`） |
| `docs/validation/fixtures/FIXTURE_002_L1_003_MAGI_PACKAGE.md` | `e26a8da` | 2026-09-14 | freeze Fixture 002 Magi（PR `#26`） |
| `docs/validation/fixtures/FIXTURE_001_L0_001_CARTY_FACT_PACKAGE.md` | `f237784` | 2026-09-14 | freeze Fixture 001 Carty（PR `#27`） |
| `docs/validation/fixtures/FIXTURE_003_L1_001_STORYCORPS_PACKAGE.md` | `d54779a`，后经 `9580577`（Repair A）修正 | 2026-09-14 | freeze Fixture 003 StoryCorps（PR `#28`） |

**观察（currentness 相关）**：自 `ee393ca`（2026-09-14）之后，**`docs/foundation/*` 与 `docs/validation/*` 全部零修改**。也就是说 2026-09-14 至今（13 天），架构本体、候选参数、语料都没有变化；所有新动静都发生在 issue 层与本次研究分支上。这是本次 attempt 判断「架构面已稳定、缺口在执行与证据面」的直接依据。

---

## 3. 分类法

| 标签 | 判定规则 |
|---|---|
| `CURRENT` | 当前对后续 lane 仍是有效依据；或仍是待执行的正式门/契约。 |
| `SUPERSEDED` | 已被更新的 durable 裁决或事实取代；**保留作历史证据，不删除**。 |
| `HISTORICAL_EVIDENCE` | 已 merge 的研究证据 / provenance；可引用、可审计，但不自动成为架构。 |
| `ACTIVE_DEPENDENCY` | 未完成但由其它 lane / 外部项目拥有；本项目只能等待或对接，不能自行推进。 |
| `OPEN_GAP` | 属于 LHRM 自身、当前无 durable 答案、且是明确记录的待办。 |
| `CONTESTED` | 存在**两个以上仍未冻结的**来源给出不相容的结论；本文件只记录分歧，**不裁决**。**Round-3 新增**。 |
| `EXTERNAL_GAP` | **Round-3 新增**。所属 lane **已关闭 / 已交付完毕**，但 LHRM 侧**从未拿到**其产物 ⇒ **等不到**，只能换路径、补做或重新派工。**依 `X-12`：这不是 blocker**（负结果 / 访问限制不是 blocker）。 |

> **`ACTIVE_DEPENDENCY` 的 Round-3 收紧（`A3a`）**：原定义「未完成但由其它 lane / 外部项目拥有」把**「仍在进行」**与**「已完成待消费」**混为一谈。本轮在 §4.3 的 `G-19`…`G-22` 四行加了一个**正交的状态标注**（不新增分类值，避免破坏「恰好一个」的互斥分配）：

| 状态标注 | 含义 | 仍可推进吗 |
|---|---|---|
| `进行中` | 外部 lane 仍在跑 | 只能等 |
| `已交付待消费` | 外部 lane **已完成并有交付物**，LHRM 尚未消费 | **可推进**（去接那份交付物） |
| `已关闭且无 durable 交付` | 外部 lane 已结束且明确未交付 | **不可等**（须换路径） |

> **`SUPERSEDED` 的 Round-3 收紧**：原判定规则要求「已被更新的 durable 裁决或事实取代」。§4.2 的 `S-I` / `S-J` **两侧均自述非冻结**，本文件也只记录分歧 ⇒ **不满足该规则**，本轮改标。**「Architect 已裁决 X 条」不等于「原文本已被取代」**：裁决可以与一份未冻结的旧报告并存。

---

## 4. 开放研究项分类总表

### 4.1 durable artifact 分类

| id | 对象 | 分类 | 依据指针 |
|---|---|---|---|
| A-01 | `CURRENT_ARCHITECTURE.md` | `CURRENT` | header `Status: CURRENT canonical architecture snapshot`；`AGENTS.md` 指为 canonical pointer |
| A-02 | `PARAMETER_CONVERGENCE_V0_1.md` | `CURRENT`（候选，未冻结） | header `CANDIDATE / NOT FROZEN`；§11 candidate basis；§15 三门未执行 |
| A-03 | `CONSTRUCT_SCOPE_DIRECTIONALITY.md` | `CURRENT`（表示原则） | header `Architecture note v0.1`；§7 六项测试 |
| A-04 | `VALIDATION_CORPUS_V0_1.md` | `CURRENT`（素材清单）+ 内含 `SUPERSEDED` 子段 | 12 份素材 metadata 仍有效；§「Recommended Fixture 001–003」已过期（§7 S-4） |
| A-05 | `FIXTURE_001_L0_001_CARTY_FACT_PACKAGE.md` | `CURRENT`（冻结输入） | §5 `This package is input, not a mapping result` |
| A-06 | `FIXTURE_002_L1_003_MAGI_PACKAGE.md` | `CURRENT`（冻结输入） | §5 同义 |
| A-07 | `FIXTURE_003_L1_001_STORYCORPS_PACKAGE.md` | `CURRENT`（冻结输入） | §7 同义 |
| A-08 | `RESEARCH_REPORT_SCIENTIFIC_RELATIONSHIP_PRIMITIVES.md` | `HISTORICAL_EVIDENCE` | 尾注「不修改 canonical ontology…由 `#2` 架构仲裁」；PR `#8` architect note |
| A-09 | `RESEARCH_REPORT_GAME_RELATIONSHIP_PRIMITIVES.md` | `HISTORICAL_EVIDENCE` | PR `#7`：机制不升格为人类经验事实 |
| A-10 | `RESEARCH_REPORT_REAL_WORLD_PROXY_DECOMPOSITION.md` | `HISTORICAL_EVIDENCE` | header `status: DRAFT_FOR_ARCHITECT_JOIN`；PR `#10` |
| A-11 | `RESEARCH_REPORT_DATING_APP_PARAMETER_PRIMITIVES.md` | `HISTORICAL_EVIDENCE` | PR `#12`：merge 仅代表接纳 research evidence |
| A-12 | `PROJECT_HISTORY_2026-09-10.md` | `HISTORICAL_EVIDENCE` | 文件自述不竞争 current authority |
| A-13 | `STAGE_SUMMARY_2026-09-07.md` | `HISTORICAL_EVIDENCE` | PR `#14`「保留为 historical provenance」；文件内 Status 行过期（S-7） |
| A-14 | `RELATIONSHIP_EVALUATION_FOUNDATION.md` | `SUPERSEDED`（部分原则保留） | 见 S-8 |
| A-15 | `ARCHITECT_RECONNAISSANCE_REPORT.md` / `ARCHITECT_BOOTSTRAP_REPORT.md` | `HISTORICAL_EVIDENCE` | 2026-09-07 接管记录 |
| A-16 | `README.md` 阶段描述 | `CURRENT` | 「当前进入 Parameter Convergence → Candidate Minimal Sufficient State → representation coverage regression → Measurement & Canonicalization」 |
| A-17 | `#30` Work Order 与本目录 `00_MANIFEST.md` / `00_CHILD_CONTRACT.md` | `CURRENT`（本 attempt 契约） | 只存在于研究分支 `ce1a774`，不在 main |

### 4.2 已显式被取代的东西（`SUPERSEDED` 明细）

> **Round-3 分类更正（`A3a`，2026-09-27）**：本节原标题把全部 10 行都归为「已显式被取代 / `SUPERSEDED`」。逐行核对后，**最后两行（`S-I` / `S-J`）不满足该分类**，本轮已改标并逐条注明理由。`S-A`…`S-H`（8 行）**不撤回**——它们各自都有一个**单一明确的取代者**（issue comment / `ARCHITECT_*_SUPERSESSION` / main 实际冻结集），属真正的 supersession。

| id | 被取代对象 | 取代者 | 指针 | 分类 |
|---|---|---|---|---|
| S-A | 「参数低相关 / 零统计相关」为收敛目标 | 「低语义/条件冗余，而非动态独立」 | `#2` comment `5567353344`；`CURRENT_ARCHITECTURE.md` §7；`CONSTRUCT_SCOPE_DIRECTIONALITY.md` §4 | `SUPERSEDED` |
| S-B | `S/O/D/E` 是完整世界本体 | `S/O/D/E` 是 query-local evaluation view；世界层 = `Agents + Relationships + Environment` + `Reality != Observation != Belief` | `#2` comment `5565245810`；`CURRENT_ARCHITECTURE.md` §3；`STAGE_SUMMARY` §2.1–2.2 | `SUPERSEDED` |
| S-C | 「先算出一个 0..1 分数/距离」为第一目标 | `Representation before scalarization. State-space before score.` | `#2` comment `5606209093`（`ARCHITECT_REPRESENTATION_FIRST_RULING`）；`AGENTS.md` Representation-first invariant | `SUPERSEDED` |
| S-D | 时间是单一线性标量 `t` | `tau = (history_id, local_time)`，历史可 fork；dream/plan/counterfactual 为 nested Belief 内模拟世界 | `#2` comment `5606838728`；`CURRENT_ARCHITECTURE.md` §8 | `SUPERSEDED` |
| S-E | 关系演化由预写状态机驱动 | `X_(t+1) = F(X_t, Action_t, Event_t, Belief_t, Constraint_t, Environment_t)` | `CURRENT_ARCHITECTURE.md` §6；`AGENTS.md` Current architecture direction #9 | `SUPERSEDED` |
| S-F | 「一个 verifier 自行选材 + 清洗 + 映射」的验证设计 | 三 verifier 同冻结输入的受控实验 | `#15` comment `5638300950`（`ARCHITECT_PROTOCOL_SUPERSESSION_V2`，明示 `SUPERSEDED BEFORE EXECUTION`） | `SUPERSEDED` |
| S-G | LGSCO（`L0-002`）作为首个可执行 fixture | OGL Carty Employment Tribunal（`L0-001`） | `#19` `ARCHITECT_SOURCE_SWITCH`；`#15` comment `5655058405` | `SUPERSEDED` |
| S-H | corpus 推荐的 fixture 顺序（001=LGSCO / 003=Carty） | main 实际冻结 001=Carty / 002=Magi / 003=StoryCorps | `git log`（`e26a8da` / `f237784` / `d54779a`+`9580577`）；`#23` comment `5660916430`、`5668514104` | `SUPERSEDED` |
| S-I | `SCIENTIFIC` §7.8 把 PPR 列入有向最小核心 | `PARAMETER_CONVERGENCE_V0_1.md` §5 `B1` 把 PPR 判为 Belief layer | 同上 | **`CONTESTED`（Round-3 改标）** —— **两侧均自述非冻结**（`SCIENTIFIC` §7.8 与 `PARAMETER_CONVERGENCE` header `CANDIDATE / NOT FROZEN`）；**本文件只记录分歧，不裁决**。`SUPERSEDED` 要求存在一个**已生效的取代者**，此处不存在。⇒ 本行是**记录在案的层位分歧**，不是取代。**Round-3 附记**：adjudication `X-1` 已 `DECIDED` —— `PPR` 留在 `BeliefState` / relationship-specific perception；`X-2` 把「层序被文献反转」作为**架构主张**驳回（前提不成立：`CURRENT_ARCHITECTURE.md` §6 已把 `Belief` 列为转移算子一等共输入），但保留为 dynamics evidence。**该裁决属 `X-1`，不使本行变成 `SUPERSEDED`**——`SCIENTIFIC` §7.8 的文本仍在，两侧仍未冻结。 |
| S-J | `SCIENTIFIC` §7.7 裁决 Trust KEEP 并保留 `C02 distrust` | `PARAMETER_CONVERGENCE_V0_1.md` §4 `D4` 把 Distrust 降为 Open question | 同上 | **`OPEN_GAP`（Round-3 改标）** —— 同 `S-I`：**两侧均自述非冻结，本文件只记录分歧**。另：adjudication `X-4` `DECIDED` —— `Trust` 与 `AttachmentSecurity` **保留为两个分开的 candidate**，`domain` 为**可选 facet / 上下文索引，不是必需 signature 字段**。该裁决**同样不**把本行变成 `SUPERSEDED`：`SCIENTIFIC` §7.7 的文本仍在。 |

**⇒ 分类计数更正**：本节 `SUPERSEDED` = **8**（`S-A`…`S-H`）；`CONTESTED` = **1**（`S-I`）；`OPEN_GAP` = **1**（`S-J`）。**Round-3 前本节把 10 行全记为 `SUPERSEDED`。**
**本文件 §4.3 的 `G-17` 仍把这四处分歧列为 `OPEN_GAP`（见该行），与本节改标后的口径一致。**

### 4.3 开放研究项（`OPEN_GAP` 与 `ACTIVE_DEPENDENCY`）

> **Round-3 分类更正（`A3a`）**：本节原表把 `ACTIVE_DEPENDENCY` 记在若干**其指针所指的外部 lane 已被记录为 completed / closed**的行上，并把两种分类混写在同一行（`G-22`）。本轮：(i) 拆开 `G-22` 为 `G-22a`…`G-22d`；(ii) 在 `G-19`…`G-22c` 的**分类格内**补一个**正交的状态标注**（`进行中` / `已交付待消费` / `已关闭且无 durable 交付`，定义见 §3 表后）——**本轮刻意不新增表格列**，以免再次制造「表头声明与实际列数不符」的问题；(iii) 修掉 `G-17` 的**悬空指针**（见下）。
> **`ACTIVE_DEPENDENCY` 的定义（本轮写明）**：**LHRM 侧尚缺、且只能由 LHRM 之外的东西补上的输入。** 它**不是**「未完成」的同义词——一个外部 lane **已完成**而 LHRM 仍缺其产物时，分类应是 `ACTIVE_DEPENDENCY` + `已交付待消费`；一个外部 lane **已关闭且未交付**时，分类应是 `EXTERNAL_GAP`（见 `G-19`）。**负结果不是 blocker。**

| id | 开放项 | 隐含研究问题 | 分类 | 指针 |
|---|---|---|---|---|
| G-01 | **Gate A**：court-fact 逐句 representation coverage | 当前 candidate schema 能否在不新增 ad-hoc primitive 的前提下映射真实事实句？失败集中在哪里？ | `OPEN_GAP` | `PARAMETER_CONVERGENCE_V0_1.md` §15 Gate A；main tree 中无任何 mapping 产出 |
| G-02 | **Gate B**：跨语境反例（11 类） | 8 个 directed construct 在 same-sex / opposite-sex / kin / non-kin / friendship / romance / caregiving / conflict / unilateral attraction / high-dependence-low-liking / high-attraction-low-trust 下语义是否稳定？ | `OPEN_GAP` | §15 Gate B；最接近的既有材料：`GAME` §9、`DATING_APP` §7（研究证据层，非对当前 basis 的执行） |
| G-03 | **Gate C**：冗余挑战（6 组指定攻击面） | Liking vs RomanticAttraction；Trust vs AttachmentSecurity；Caregiving vs Dedication；AttachmentSecurity vs Cohesion；OutcomeDependence vs structural derivation；PPR vs Trust/Care/Attachment | `OPEN_GAP` | §15 Gate C；最接近：`REAL_WORLD` §6 + §8、`SCIENTIFIC` §6 + §7、`02b`（**Round-3 附注**：`02b` §4 判定列已降级为**作者判断、不可由其规则导出**，其 `INDEPENDENT` 标签**不得**作 Gate C 证据） |
| G-04 | Q-1 `Distrust` 是否独立 construct | 二元（trust/distrust）还是单极（trust 强度 + 否定）？ | `OPEN_GAP` | `PARAMETER_CONVERGENCE_V0_1.md` §4 D4；既有立场 `SCIENTIFIC` §7.7、§10.1(2)、§10.3(2)。**Round-3 附注**：`X-4` 已把 `Trust` / `AttachmentSecurity` 判为各自保留的 candidate，`domain` 为可选 facet ⇒ **本行的范围收窄为「`Trust` vs `Distrust`」本身**，不再与 facet 切点混谈 |
| G-05 | Q-2 attachment security 是否拆 facet | anxiety / avoidance 是 dyad facet 还是 Agent 属性？ | `OPEN_GAP` | §4 D5；既有立场 `SCIENTIFIC` §3.1 依恋理论行、§9.3。**Round-3 附记**：`X-4` 把 `Trust` 侧更窄的 facet 切点列为**待 M2 式证据**，并**拒绝**新增 `FeltSecurity` 槽位（canonical D5 已占有该措辞） |
| G-06 | Q-3 `OutcomeDependence` 是否可由结构性量完全导出 | 若可由 resources / alternatives / constraints 完全推出，则不应是独立 latent state | `OPEN_GAP` | §4 D8；既有立场 `SCIENTIFIC` §3.1 互依理论行、§5.2、§7.6 |
| G-07 | Q-4 是否需要 shared latent `Cohesion_(A,B)` | 「我们感」是真实 pair process，还是双方 perception 的组合？ | `OPEN_GAP` | §6 P1；既有立场 `SCIENTIFIC` §6.18、§7.2（`B05`） |
| G-08 | Q-5 `Satisfaction` 是 derived 还是 primitive | 已知底层状态后 satisfaction 是否仍携带稳定独立动态信息？ | `OPEN_GAP` | §9 R3；既有立场 `SCIENTIFIC` §6.14、`C12`。**Round-3 附记**：`X-1` `DECIDED` —— `Satisfaction` **留在 Derived / evaluation candidate**；`C-P8` 只追加**条件后果预登记**（若该判据成立并提升 `Satisfaction`，则 `§4 D7` 的 basis 地位与 `§11` 的 8 项 basis 需重新审议）。⇒ **本行仍是 `OPEN_GAP`**，但**不再是一个待二选一的冲突** |
| G-09 | Q-6 `ValueCongruence` / `GoalAlignment` 的「量度」归属 | pair 属性、慢状态，还是 belief？ | `OPEN_GAP` | §6 P2/P3；`SCIENTIFIC` §10.3(3) |
| G-10 | Measurement & Canonicalization（工程顺序第 4 步） | 观测变量/行为代理如何稳定映射到 latent construct family，且保留 uncertainty？ | `OPEN_GAP` | `CURRENT_ARCHITECTURE.md` §9、§12；`PARAMETER_CONVERGENCE_V0_1.md` §14；`#29` 分层验证 C |
| G-11 | State transition / dynamics（工程顺序第 5 步） | 哪些状态/行为/环境变量对后续状态变化提供增量解释？ | `OPEN_GAP` | `CURRENT_ARCHITECTURE.md` §6、§12；`#29` 分层验证 D |
| G-12 | Longitudinal parameter estimation（工程顺序第 6 步） | 参数估计、holdout、跨数据集泛化、uncertainty calibration | `OPEN_GAP` | `CURRENT_ARCHITECTURE.md` §12；`#29` 分层验证 F |
| G-13 | validated measurement instrument 目录 | 每个 candidate construct 的成熟量表/行为测量家族、方向性、state vs trait、跨文化不变性证据 | `OPEN_GAP` | `PARAMETER_CONVERGENCE_V0_1.md` §2.6、§14；仓库内**无** instrument 目录（`REAL_WORLD` §5 只列 prior/base-rate 用途的数据源）。**Round-3 附注**：canonical §2 的**六条**判据中只有 §2.6 用了删除框架、§2.2/§2.5 用了降级框架、**三条（§2.1/§2.3/§2.4）连后果句都没有**，且**六条全部无 procedure / required evidence / output field / threshold / designated executor**（`review-r2` R-A2）⇒ 本行的难度**不只是「目录不存在」**，还有「即使建成也无处写入结论」 |
| G-14 | 严肃 quantitative dyadic dataset 审计（`#29` 数据要求：dyad id + 两方可区分 + ≥2 wave + codebook + outcome/event + missingness 文档 + rights 可复现） | 哪些 dataset 满足 LHRM 需要的 dyadic 测量形态？ | `OPEN_GAP` | `#29`「数据要求」段；`REAL_WORLD` §5 的 20 个源**主要是 person/household 级 panel**，不满足 dyad 形态要求 |
| G-15 | Case Bank 从 3 份扩到 sampling frame | 下一批覆盖 ordinary / cross-cultural / non-romantic / kin / caregiving / longitudinal / repair 等 | `OPEN_GAP` | `#13`「最低覆盖维度」；`#15`；corpus「Readiness for next-round verification」。**Round-3 附注**：`X-10` `DECIDED` —— Human-dyad domain **已**含 kin / ex / professional / cooperative / adversarial 类；真实缺口是 (1) canonical 清单对齐 (2) 经验语料覆盖。**domain 声明不是 representation 证据** |
| G-16 | `Dataset-to-LHRM Mapping Spec` 实体 | 仓库内不存在该 schema 的任何实例 | `OPEN_GAP` | `#29` 定义了字段清单；main tree 内无实例 |
| G-17 | PPR / OutcomeDependence / Cohesion 的层归属分歧收敛 | 见 §4.2 `S-I`（PPR）、本表 `G-06`（OutcomeDependence）、`G-07`（Cohesion）；Distrust 见 `G-04` | `OPEN_GAP` | `SCIENTIFIC` §7.8 vs `PARAMETER_CONVERGENCE` §4/§5/§6。**Round-3 修掉悬空指针**：原写「见 §7 S-9/**F-09**」——**本文件没有任何 `F-xx` 条目**（§7 只有 `S-1`…`S-13`），而 §7 的 `S-9` 讲的是 `#23` body 的 Juece surface 与 fixture 001 描述过期，**与层归属分歧无关**。已改为指向本表与 §4.2 的实际条目 |
| G-18 | 三套 corpus 分级轴（L0–L3 难度 / P0–P4 provenance / Level 0–6 curriculum）对齐 | 下一批采样按哪套轴？corpus 未填 `source_grade` | `OPEN_GAP` | 见 §7 S-13 |
| G-19 | 隔离 verifier lane 的 durable 结果 | 是否已有任何 representation coverage 结果可 join | **`EXTERNAL_GAP`**（Round-3 由 `ACTIVE_DEPENDENCY` 改标）+ 外部状态：**已关闭且无 durable 交付** | `#15` comment `5655058405`（解除封锁）；`#23` comment `5813587483`（2026-09-24 复核：**无 durable delivery**）。**Round-3 理由**：该 lane **已关闭**且**明确未交付** ⇒ 这不是「还在进行中的依赖」，而是一个**外部空缺**。按 `X-12`，它也**不是 blocker**（负结果 / 访问限制不是 blocker） |
| G-20 | Eye 侧 LHRM consumer MVP / **≥2 个可取得 dyadic dataset 或明确 access gate** | `LHRM_CONSUMER_MVP_READY` 之后的 dataset access | `ACTIVE_DEPENDENCY` + 外部状态：**`youling/eye#54` ACCEPT（consumer 侧已交付）；`youling/eye#57` completed/closed** ⇒ **依赖的「consumer 侧」已完成，缺的是 dataset / access gate 本身** | `#13` comment `5638240071`；`#23` comment `5813587483`。**Round-3 理由**：原表把本行整行记为 `ACTIVE_DEPENDENCY`，而其指针里的 `eye#57` 已 `completed/closed`；**「已交付待消费」与「仍在进行」必须分开记**，否则 join 会把一个已完成的外部 lane 算成活跃依赖。**未打开 `eye#57`，本行状态为经 LHRM issue comment 的转述（`TRANSCRIBED_NOT_OPENED`）** |
| G-21 | Juece thin-adapter compatibility 结论 | 三 fixture 的 `KEEP/ADAPTER/GENERIC_EXTEND_CANDIDATE/REJECT` 矩阵 | `ACTIVE_DEPENDENCY` + 外部状态：**`THREE_FIXTURE_GATE = CLEARED`（`#23` comment `5668514104`）；`ACTIVE_EXECUTION = youling/juece#30`** | `#23` comment `5668514104`。**Round-3 理由**：门**已 clear**，执行**已派发**到 `youling/juece#30`。本行应读作「**等一份已派发的执行结果**」，不是「等一个尚未开始的前置条件」。**本 lane 未打开、未执行、也未推断 `youling/juece#30` 的内容**（契约禁止项） |
| G-22a | `#29` 第一阶段 Gate 条件 (1)：隔离 lane durable 结果 | 是否已有可 join 的 coverage 结果 | **`EXTERNAL_GAP`**（**Round-3 新拆出**） | 见 `G-19`：**已关闭且无 durable 交付** ⇒ 条件 (1) 当前**不满足**，且**不能**靠等待满足 |
| G-22b | `#29` 第一阶段 Gate 条件 (2)：Juece smoke 完成 | thin-adapter smoke 是否已跑完 | `ACTIVE_DEPENDENCY` — **已交付待消费**（**Round-3 新拆出**） | 见 `G-21`：`THREE_FIXTURE_GATE = CLEARED`。**状态未经本 lane 独立核实** |
| G-22c | `#29` 第一阶段 Gate 条件 (3)：Eye 至少 2 个可取得 dataset 或明确 access gate | 是否已有可取得的 dyadic/longitudinal 数据 | `ACTIVE_DEPENDENCY` — **consumer 侧已交付，dataset 侧仍缺**（**Round-3 新拆出**） | 见 `G-20`。本行亦是 §11 `U-2` 的同一未知 |
| G-22d | `#29` 第一阶段 Gate 条件 (4)：选定 ≤3–5 条可证伪候选关系与 outcome 定义 | 哪 3–5 条关系值得先被证伪？ | `OPEN_GAP`（**Round-3 新拆出；原与 (1)(2)(3) 混在同一行**） | `#29`「第一阶段 Gate」段。**这是四条里唯一 LHRM 侧自己能做的一条** |
| G-23 | 本次 overnight swarm 的 18 条 Wave 1 lane | 见 §8 | `ACTIVE_DEPENDENCY`（对 R00 而言） | `00_MANIFEST.md` §2 lane 表。**Round-3 附记**：adjudication `X-8` 要求把「12 robust agreements」换成审计过的 `N-A1…N-A12` 独立来源记账，`00_MANIFEST` 由 sibling `A2` 负责 |
| G-24 | 治理 ref 的持续锁定 | 本 attempt 起点 `64018d…`；下一次 attempt 必须 live recheck | `CURRENT`（可执行约束） | `AGENTS.md` Governance；`#30` body「Execution start MUST live-recheck」 |

---

## 5. 开放 issue / research gap map

> 说明：下表覆盖 2026-09-27 实测的全部 10 条 open issue。契约指定隔离的独立 verifier lane 已整体排除，未打开、未列举、未总结。

| # | 标题（简） | 隐含研究问题 | 实测状态 | 分类 | 关键指针 |
|---|---|---|---|---|---|
| `2` | Research Program：关系参数最小词汇表与低冗余分解 | 什么是低冗余的最小关系状态基？哪些是 primitive、哪些是 proxy/derived/observation？ | `open`，12 comments，**最后一条 2026-09-09 19:52:41** | `CURRENT`（作为 parent program）+ 呈现过期（§7 S-1） | body；comment `5565170990` / `5565245810` / `5567353344` / `5570072094` / `5606209093` / `5606838728` / `5607830389` |
| `3` | Research A：游戏/人生模拟中的关系状态与亲密度参数反向工程 | 游戏设计者为了避免单一好感度失真，把哪些关系构念拆开了？哪些仍被错误揉成一个值？ | `open`；交付 comment `5565417228`；PR `#7` merged `6abd4b8` | `HISTORICAL_EVIDENCE`（交付物）+ 状态过期（§7 S-2） | `RESEARCH_REPORT_GAME_RELATIONSHIP_PRIMITIVES.md`；comment `5565247050` |
| `4` | Research B：关系科学/认知神经/生物与计算项目中的基础构念 | 哪些构念在理论与测量上足够独立，值得成为 primitive？哪些只是别的构念的指标/结果/高阶合成？ | `open`；交付 comment `5565432939`；PR `#8` merged `ebdc4b7` | 同上 | `RESEARCH_REPORT_SCIENTIFIC_RELATIONSHIP_PRIMITIVES.md`；comment `5565248580` |
| `5` | Research C：婚恋/相亲应用中的偏好、过滤与匹配变量反向工程 | 哪些字段只是方便填写的表面代理词？declared vs revealed preference 如何不一致处理？ | `open`；先 `BLOCKED_DURABLE_DELIVERY`（`5565636030`）后 `ACCEPTED_AS_RESEARCH_EVIDENCE`（`5570070634`）；PR `#12` merged `8074726` | 同上 | `docs/RESEARCH_REPORT_DATING_APP_PARAMETER_PRIMITIVES.md`；comment `5565249963` |
| `6` | Research D：社会现实/统计/案例中的代理词拆解与极端压力测试 | 现实高频词最少要拆成哪些彼此独立的基础构念？哪些变量在极端现实里会解耦？ | `open`；PR `#10` merged `14344dc` | 同上 | `RESEARCH_REPORT_REAL_WORLD_PROXY_DECOMPOSITION.md`；comment `5565251603` |
| `13` | Research E：现实世界关系案例库与完备性压力测试基准 | 长期 Case Bank 从哪里取材、如何分级、如何采样？法院文书的事实状态如何与 Belief/Observation 分层对齐？ | `open`，6 comments（最后 2026-09-11 17:30:49） | `CURRENT`（长期 lane）+ 呈现过期（§7 S-6） | body 的 P0–P4；comment `5606725482`（coverage test protocol + Level 0–6）、`5607832083`、`5636840975`（GitHub/Research data hub sweep）、`5638240071`（Eye handoff ACCEPT） |
| `15` | Validation Fixture 001：法院事实逐句 Representation Coverage | 第一轮 black-box representation coverage regression；`MAPPING_FAILURE` 出现在哪里？ | `open`，3 comments（最后 2026-09-13 18:01:48） | `CURRENT`（门）+ 呈现过期（§7 S-3、S-5） | body 的 frozen baseline `18cd72c` 与产出路径；comment `5607828367`（V1，后被取代）、`5638300950`（V2 supersession）、`5655058405`（`f237784` + C001–C026 + 隔离 lane 解除封锁） |
| `23` | Juece Compatibility Pressure Test：Eye Evidence → Atomic Claims → LHRM | LHRM 能否把 Juece Epistemic Kernel 当通用中间层复用，而不重复建设 claim/lineage/subject-resolution？ | `open`，10 comments（最后 2026-09-24 11:56:03）——**公开 issue 中最近活动的一条** | `CURRENT`（active cross-project lane）+ 呈现过期（§7 S-9） | body；comment `5638318724`、`5638404800`、`5647569382`、`5659975181`、`5660140919`（corrected handoff）、`5660196595`（`LHRM_CONSUMER_ACK = YES`）、`5660916430`、`5668514104`（`THREE_FIXTURE_GATE = CLEARED`）、`5813587483`（09-24 currentness 复核） |
| `29` | Empirical Validation Lane v0.1：从 Evidence/Claims 到关系方程结构与参数验证 | 哪些数学假设可以被数据证伪/估计/校准？分层验证 A–F 如何组织？ | `open`，**0 comments**（实测） | `CURRENT`（新建、尚无 durable 执行） | body 的分层验证 A–F、数据要求、`Dataset-to-LHRM Mapping Spec` 字段、第一阶段 Gate 4 条件、关键纪律 8 条 |
| `30` | Overnight Exploration Swarm v1 总工单 | 用一批互不相关的探索性 lane 把 LHRM 尚未充分探索的问题一次性铺开 | `open`，2 comments | `CURRENT`（本 attempt 契约） | comment `5850761496`（dispatch）、`5850793190`（`AGENT_CLAIMED`） |

**已关闭但仍在被引用的问题记录**：`#16`（corpus v0.1 采集，closed 2026-09-11）、`#19` / `#24` / `#25`（三份 fixture 准备，closed 2026-09-13/14）——它们的交付物即 `VALIDATION_CORPUS_V0_1.md` 与三份 `fixtures/*PACKAGE.md`，均已在 main。

---

## 6. 既有报告已回答的问题（「不要重做」映射）

下表把 `#30` 各 lane 的任务，对齐到**已经存在的 durable 答案**。右列「仍缺什么」是本 lane 的映射结论，不是要求。

| `#30` lane | 已被回答的部分 | 精确指针 | 仍缺什么 |
|---|---|---|---|
| R01 Construct convergence | 62 个候选构念语义边界审计（A01–G08）；20 组成对易混淆比较；六维逐项 KEEP/SPLIT/MERGE/REJECT；`primitive/latent/observable/derived` 四类判定总表；跨学科构念地图 | `SCIENTIFIC` §4（L257–1033）、§6（L1091–1176）、§7（L1177–1266）、§5.4（L1078–1090）、§3.1（L233–247） | 对**当前 8 项 candidate basis** 逐项的 scope/directionality/measurement family 复核；§7.8 与 `PARAMETER_CONVERGENCE` 的 4 处分歧收敛（G-17） |
| R02 Redundancy / double-count | 126 条现实 proxy 拆解 + 重复计数风险矩阵（族×族）；低冗余四关审查规程 + 两例手做演示（`肯花钱`、`陪伴`）；漏项清单 7 项 / 过度拆分清单 10 项；20 组成对构念比较 | `REAL_WORLD` §3、§6、§7.1、§7.2、§8；`SCIENTIFIC` §6；`DATING_APP` §9（12 组）；`GAME` §6（7 类合并模式） | Gate C 指定 6 组攻击面在**当前 basis** 上的执行结果；条件增量信息的**形式化可识别性**讨论 |
| R03 Measurement instruments | 代理词→构念映射表：科学侧 52+ 条、现实侧 126 条、产品侧 144 条、游戏侧 50 条；`observable_or_latent` 字段；`future_leakage_risk` / `state vs trait` 提示散见 | `SCIENTIFIC` §8、§4 各行；`REAL_WORLD` §3；`DATING_APP` §6；`GAME` §4；`VALIDATION_CORPUS_V0_1.md` 各素材 `representational_challenges` 字段 | **validated instrument 目录本身不存在**（G-13）：无 scale/item 家族、无信度效度、无 measurement invariance、无 dyadic directionality 元数据 |
| R04 Dataset landscape | 20 个统计/研究数据源 → observable / prior / base-rate 映射，及每源「不能冒充什么」 | `REAL_WORLD` §5（L306–333） | 该清单**几乎全是 person/household 级 panel**，不满足 `#29` 的 dyad 形态要求（dyad id + 两方可区分 + ≥2 wave + outcome/event）。真正接近 dyadic 的只有表中 2–3 行（Joel et al. 2020 的 43 数据集 / 11,196 对；Gottman Love Lab 编码；Rusbult 投资模型四量表）。→ R04 不是重复，而是**在另一个形态层上新建**（G-14） |
| R05 Identification / statistics | 方法学分类骨架已列（APIM / 条件冗余 / 因子分析 / 条件独立性 / 干预独立 `do()`） | `REAL_WORLD` §8（L384–421）、§8.5；`STAGE_SUMMARY` §5.2（APIM DOI） | APIM / DSEM / RI-CLPM / state-space / hazard / ESM 的方法-问题矩阵、失败模式、不可作因果主张的边界（G-10/G-11 依赖） |
| R06 Transition laws | 跨系统动力学特征汇总：方向性/不对称、可接受性不对称、双时间尺度、阶段/里程碑、衰减与遗忘、路径依赖（`non-Markov unless history kept`）、事件触发、多边效应、部分观测 | `GAME` §8（L308–321）；`GAME` §11.2 建议 2「更新规则优于加状态」 | 3–5 条**可证伪**的候选 law family 及其 competing null、识别风险、falsification criterion（尚不存在） |
| R07 Sparse input / missingness | Unknown 不得静默转成 neutral/perfect；`RawObservation → CanonicalRepresentation → ModelState`；坐标可为区间/序数/类别/约束/分布/Unknown | `CURRENT_ARCHITECTURE` §9；`PARAMETER_CONVERGENCE` §14；`STAGE_SUMMARY` §3.4–3.5 | 可检验的不变量（partial pooling / MNAR / uncertainty calibration / refinement consistency）尚未形式化 |
| R08 Belief / deception | `Reality != Observation != Belief`；`WorldState` 与 `BeliefState` 分层；partial observation 的游戏侧证据（Tokimeki / MonsterProm 隐藏好感） | `CURRENT_ARCHITECTURE` §3、§6；`CONSTRUCT_SCOPE_DIRECTIONALITY` §6；`GAME` §8 末条 | 最小可用 epistemic primitives 尚未收敛；`#23` 的 corrected handoff 已给 8 条 consumer 语义不变量（`asserted(P) != believed(P) != P-is-true` 等）可作为对接基线 |
| R09 Dynamics / no-FSM | 不采用预写关系状态机；连续/混合状态转移；路径依赖；阶段作为 role_constraint 跃迁而非分数滑动 | `CURRENT_ARCHITECTURE` §6；`AGENTS.md` Current architecture direction #9；`GAME` §8、§11.2 | 阈值/迟滞/吸引子/亚稳态/repair-after-perturbation 的文献与形式化对比（FSM/HMM/state-space 三选项的显式比较尚未做） |
| R10 Mutuality / power | mutuality/asymmetry 优先由双向有向状态派生；power 优先由 dependence 不对称 + alternatives/resources/constraints 派生 | `CURRENT_ARCHITECTURE` §4；`CONSTRUCT_SCOPE_DIRECTIONALITY` §2；`PARAMETER_CONVERGENCE` §9 R1/R2；`SCIENTIFIC` §5.2(4)、§6.9 | 「是否有任何当前 pair candidate 真需要独立 pair state 而非派生」的逐项判定（G-07） |
| R11 General Human Dyad scope | 跨语境语义稳定性标注：游戏侧 6 候选 × 形态矩阵、产品侧 6 语境结果表、科学侧 `assumption_stress_test` | `GAME` §9；`DATING_APP` §7；`SCIENTIFIC` §2.4 | 全部是**研究证据层的形态标注**，不是对 Gate B 11 类反例的执行；且当前唯一冻结的 L0 官方 fixture 是**雇佣 dyad**（§7 S-11） |
| R12 Computational / ABM | 计算/形式化视角的三条已总结（状态/观测/信念三层分离；事件驱动有向路径依赖边；低层机制可被高层状态吸收）；互依博弈化、状态转移、贝叶斯更新、ABM 传统的建模语法参考 | `SCIENTIFIC` §3.1 末行、§3.2（4 条）、§11 计算/形式化启发行 | 系统化的 computational model / ABM benchmark 尚不存在（state repr、transition rules、calibration source、validation method 抽取） |
| R13 LLM Skill / interview | LLM 作为 `semantic interpreter + adaptive interviewer + result explainer`，与 LHRM core 解耦的分工已定；分层链路 `NL → parsing → proxy extraction → canonical state → inference → uncertainty-aware result → explanation` | `#2` comment `5565326424`；`STAGE_SUMMARY` §4；`CURRENT_ARCHITECTURE`（Role 作为 query lens） | 结构化抽取可靠性、歧义处理、矛盾检测、expected information gain 追问策略、LLM confidence vs evidence 的经验评估 |
| R14 Positioning / novelty | 9 个成熟理论/方法锚点含 DOI，并给出 `REUSE/ADAPT/BUILD/REJECT` 判定 | `STAGE_SUMMARY` §5.1–5.8（L206–261）；`ARCHITECT_RECONNAISSANCE_REPORT` 外部证据 2 条（L30–37）；`SCIENTIFIC` §11（author-year，无 DOI） | 与最新工作的直接比较、reviewer 可能反驳点、投稿前的经验里程碑 |
| R15 Case Bank expansion | 12 份素材 metadata 已按 `L0–L3` 分级完成；每份含 rights/access、leakage risk、cleaning 建议、unit 数、敏感内容标注；`#13` 给出 15 项最低覆盖维度 | `VALIDATION_CORPUS_V0_1.md` 全文；`#13`「最低覆盖维度」段 | 20–30 条下一批高价值 fixture 指针尚未产出；且三套分级轴未对齐（G-18） |
| R16 Validation protocol join | `#29` 已定义分层验证 A–F、数据要求 7 条、`Dataset-to-LHRM Mapping Spec` 字段、8 条关键纪律、4 条第一阶段 Gate | `#29` body | 仓库内无该 spec 的任何实例（G-16）；leakage 规则、outcome 定义、train/holdout 切分、preregistration-like freeze point 尚无候选实现 |
| R17 Red team | 反例素材已在库：38 个 adversarial cases（`REAL_WORLD` §4）、`assumption_stress_test` 多处、`GAME` §9 decoupling 6 例、corpus 各素材 `representational_challenges` | `REAL_WORLD` §4；`GAME` §9；`SCIENTIFIC` §2.4 | 尚未系统搜索「当前 LHRM 假设不成立」的外部证据（falsifier 层面） |

---

## 7. 过期呈现 vs 已合并证据

> 处置原则：这些都是 **bookkeeping / presentation drift**，不是架构错误。本文件**不主张**回改任何已 merge 文件；`AGENTS.md` Mutation discipline 要求「preserve provenance」「不擦除旧证据」。正确处置是：在新 artifact 中显式记录 supersession，或由 Architect 在 issue 层给出 status 收口。

### S-1 — `#2` 的呈现停留在 2026-09-07 之前

- body 目标仍写「基础参数词汇尚未冻结」、研究原则第 2 条仍写「彼此尽可能低相关/低重叠」、交付字段仍写 `layer: Agent / Relationship / Environment / Belief`，Work Graph 只列 `#3–#6`。
- 实际已被 durable 取代：低相关 → 低语义/条件冗余（`#2` comment `5567353344`）；S/O/D/E → query-local view + Belief 分层（`5565245810`）；representation-first 优先级（`5606209093`）；时间分支（`5606838728`）；四源 join 已完成（`5570072094`）且 convergence 已交付（`18cd72c`）。
- 且 `#2` 最后一条 comment 停在 2026-09-09 19:52:41，此后仓库推进了 5 轮（§1.2），`#13/#15/#23/#29/#30` 均未进入 `#2` 的 Work Graph。

### S-2 — `#3/#4/#5/#6` 仍 open，但 deliverable 早已 durable

四条都有交付/验收 comment 与已 merge PR（§4.1 A-08…A-11）。残余语义「等 `#2` join」也已完成（`18cd72c`）。**这是纯 bookkeeping 漂移**。

### S-3 — `#15` 的 frozen baseline、协议、产出路径、素材类型描述均已过期

| 项 | body 写的 | 实际 |
|---|---|---|
| 冻结基线 | `18cd72c99b354c003f98ae2a7b7c4148f15a20af` | `f2377849f71407013d5abe19fd0b4ff26f501066`（comment `5655058405`） |
| 协议 | 单 verifier 自行选材/清洗/映射 | 三 verifier 同冻结输入（comment `5638300950` 明示 V1 `SUPERSEDED BEFORE EXECUTION`） |
| 建议产出 | `docs/validation/FIXTURE_001_COURT_FACT_MAPPING.md` | main 上不存在该文件；材料侧产出是 `docs/validation/fixtures/FIXTURE_001_L0_001_CARTY_FACT_PACKAGE.md` |
| 素材类型 | 「婚姻、分居、欺骗、财产/照护/冲突」 | 实际是**英国 Employment Tribunal 雇佣争议**（employee ↔ line manager） |

### S-4 — `VALIDATION_CORPUS_V0_1.md` 的 fixture 推荐段与 main 实际冻结集冲突

corpus 写 `001 = L0-002 LGSCO` / `002 = L1-003 Magi` / `003 = L0-001 Carty`；main 实际为 `001 = Carty(L0-001)` / `002 = Magi(L1-003)` / `003 = StoryCorps(L1-001)`。3 项中 2 项不符。变更原因只存在于 issue comment（`#19` `ARCHITECT_SOURCE_SWITCH`；`#25` body），**不在 corpus 文件内**。

### S-5 — corpus 对 `L1-001`（StoryCorps）的 access/licence 描述已被下调

corpus：`open-access, no login`、`free to view/read/listen; not public-domain, not CC`。
Fixture 003 §1：旧址 404；现址取自 `listen-sitemap.xml`；`robots.txt` `Content-Signal: search=yes,ai-train=no,use=reference`；`Disallow` for `GPTBot`/`ClaudeBot`/`CCBot`；EU 2019/790 reservation；无 CC transcript 授权；`rights_policy=HUMAN_REVIEW_REQUIRED` → `raw_allowed=false, representation_allowed=false, store_pointer_only=true`。

### S-6 — corpus 对 `L0-002`（LGSCO）的 access_status 对下游执行者偏宽松

corpus 记「open / stable / free（official permanent decisions database; full text live-fetched 2026-09-11）」；但 durable source switch 明确记录 merged Eye rights policy 使该源保持 `HUMAN_REVIEW_REQUIRED` / pointer-only，故它**不能**作为首个可执行 fixture。corpus 本身作为「候选素材」仍有效，作为「可执行 fixture 建议」已失效。

### S-7 — `STAGE_SUMMARY_2026-09-07.md` 的自述 Status 与仓库分类矛盾

文件内写 `**Status:** Current research checkpoint`；`README.md` 把它列为「历史阶段 checkpoint」；PR `#14` 写「旧 `STAGE_SUMMARY_2026-09-07.md` 保留为 historical provenance」。以 `README.md` + PR `#14` 为准。**注意：这是全仓唯一带 9 个 DOI 的成熟理论指针集中地**（§5.1–5.8），不要因为它被降级为历史证据就忽略它的指针价值。

### S-8 — `RELATIONSHIP_EVALUATION_FOUNDATION.md` v0.1.1 部分被取代

| 保留（仍 `CURRENT`） | 被取代（`SUPERSEDED`） |
|---|---|
| Unknown / 未形成阶段不得用想象值补齐（§4.4） | `X¹→X²→X³→X⁴` 阶段门控作为**表示本身**（`CURRENT_ARCHITECTURE` §3 改为 query-local view + `Reality != Observation != Belief`） |
| 不把「漂亮/贤惠/有魅力/高价值」当底层输入（§4.1） | 统一函数族 `F_visual/F_sexual/F_interaction/F_chemistry/F_trust/F_role/F_stability`（§3）未进入当前 basis |
| `ρ = Role/Task` 是评价镜头而非底层变量（§2.2） | 「`E` 排第四」被读作完整环境本体（`CURRENT_ARCHITECTURE` §3 明确 `E` 只是与当前问题相关的环境） |
| 不强迫线性加权（§4.3） | — |

### S-9 — `#23` body 的 Juece surface 与 fixture 001 描述过期

- body：「Relevant Juece surfaces: `docs/EPISTEMIC_KERNEL.md`, issue `#21`, PR `#22`（当前 OPEN / NOT MERGED；仅作 future-contract reference，不当作 current-main API）」——此 `issue #21` / `PR #22` 指 **`youling/juece` 仓库编号**，与本 lane 排除的 LHRM 隔离 lane 无关 → 实际已有 corrected handoff（comment `5660140919`）并被 LHRM `ACK / ACCEPT`（`5660196595`，含 8 条 consumer 不变量 + 2 条 LHRM 侧澄清）；2026-09-24 复核记录 Juece main 已前进且 epistemic-contract 面无变化（`5813587483`）。
- body：「Fixture 001 — `#19` LGSCO official case fact package」→ 实际冻结的 Fixture 001 是 OGL Carty。
- body 目标「3–5 个 frozen fixtures」→ 2026-09-14 起 `THREE_FIXTURE_GATE = CLEARED`（`5668514104`）。

### S-10 — `#29` 的第一阶段 Gate 条件与 2026-09-24 durable 状态不匹配

- Gate 条件 1「Fixture 001 independent representation results 有 durable 输出」：2026-09-24 的 durable 复核（`#23` comment `5813587483`）记录**无 durable delivery**。
- Gate 条件 2「Juece thin-adapter smoke 完成」：LHRM 侧最后记录为 `RELEASED/DISPATCHED`（`5668514104`，2026-09-14），此后无 durable 更新 → `UNKNOWN_AS_OF_2026-09-27`。
- Gate 条件 3「Eye 提供至少 2 个可实际取得的 dyadic/longitudinal quantitative datasets 或明确 access gate」：`UNKNOWN_AS_OF_2026-09-27`（跨项目，本 lane 未核实）。
- `#29` 自身 **0 条 comment**——它是全仓最新的架构 lane，却完全没有 durable 讨论记录。

### S-11 — 首个（且唯一）已冻结的 L0 官方事实 fixture 是**雇佣 dyad**

`FIXTURE_001_L0_001_CARTY_FACT_PACKAGE.md` §1：core dyad = `Miss Z. Carty <-> her 2020 line manager / employer-side human contact`。这与 `#15` body 的婚恋/家庭素材描述、以及 `AGENTS.md` 强调的 general Human Dyad 范围之间存在一个**未被显式承认的覆盖偏移**。含义：当前 durable 证据对 romance / kin / caregiving dyad 的**表示覆盖测试**仍为 0。

### S-12 — `docs/RESEARCH_REPORT_DATING_APP_PARAMETER_PRIMITIVES.md` 路径未归一

PR `#12` architect note 与 `README.md` 都记录了「位于 `docs/` 根目录而非 `docs/research/`」；截至 `ee393ca` 未整理。**更关键的后果**：`#30` body 的「Relevant LHRM durable sources」清单只点名 `docs/foundation/*` 三件与 `docs/validation/VALIDATION_CORPUS_V0_1.md`，**没有点名四份 prior report**，只写一句「Existing Research A-D / merged reports are prior evidence」。只按 `#30` 清单找资料的 lane 会完全找不到 Research A–D。

### S-13 — 三套并行的 corpus 分级轴未对齐

| 轴 | 定义处 | 含义 |
|---|---|---|
| `L0`–`L3` | `VALIDATION_CORPUS_V0_1.md`（`level` 字段） | **表示难度** |
| `P0`–`P4` | `#13` body（`source_grade` 字段，自称「暂定…待 Research 预研后修订」） | **provenance 等级** |
| `Level 0`–`Level 6` | `#13` comment `5606725482` | **curriculum benchmark**（7 级） |

corpus 实际只填了 `level`，**没有填 `source_grade`**；`#13` body 的 15 项「最低覆盖维度」也未映射到任一轴。

---

## 8. 「Do not redo」清单

> 供所有 lane 使用。以下条目**已经以 durable 形式存在于 `youling/lhrm@main@ee393ca`**；引用即可，**不要从零重做**。

### 8.1 不要重做的研究工作

1. **四源发散研究已完成**（2026-09-07，全部 merged）：
   - 游戏/生活模拟 13 系统反工程 → `RESEARCH_REPORT_GAME_RELATIONSHIP_PRIMITIVES.md`（`§3` 系统、§4 50 条 M01–M50、§5 六维裁决、§6 重复计数、§7 UI 可迁移、§8 动力学、§9 assumption_stress_test、§10 学术校准、§11 剩余不确定性）
   - 关系科学构念深研（62 构念 / 20 组成对比较 / 52+ 代理词映射） → `RESEARCH_REPORT_SCIENTIFIC_RELATIONSHIP_PRIMITIVES.md`（`§2.5` 裁决索引、`§4` 语义边界审计、`§5.4` 四类判定总表、`§6`、`§7`、`§8`、`§9`、`§10`）
   - 婚恋/约会产品反向工程（20 产品 / 144 条 proxy） → `docs/RESEARCH_REPORT_DATING_APP_PARAMETER_PRIMITIVES.md`（`§2` 矩阵、`§4` 六类压缩模板、`§5` declared vs revealed、`§6` 144 条、`§7` 跨语境、`§8` 默认假设审计、`§9` 冗余表、`§10` 裁决、`§11` 可复用/不可复用）
   - 现实世界 proxy 拆解（126 条 / 38 adversarial / 20 统计源） → `RESEARCH_REPORT_REAL_WORLD_PROXY_DECOMPOSITION.md`（`§3`、`§4`、`§5`、`§6`、`§7.1`、`§7.2`、`§8`、`§9`）
2. **第一次正式 candidate convergence 已完成** → `PARAMETER_CONVERGENCE_V0_1.md`（含 §2 收敛判据、§4 D1–D8、§5 Belief、§6 Pair、§8/§9 降级清单、§11 candidate basis、§13 十槽 schema、§15 三门）。**不要重新发明一套 candidate basis 再与它比较**；要改就指出与 §4/§6/§11 的具体偏离。
3. **representation-first 转向与其纪律已成文** → `AGENTS.md`（Representation-first invariant 6 条 + Current architecture direction 11 条）+ `CURRENT_ARCHITECTURE.md` §1/§3/§6/§7/§8/§11。**不要重新论证「是否该先算分」**。
4. **验证语料 12 份 + 三份冻结 fixture 已完成** → `VALIDATION_CORPUS_V0_1.md` + `fixtures/FIXTURE_00{1,2,3}`。**不要重新选材**；要做的是 Gate A/B/C 的执行或下一批 sampling frame（G-15）。
5. **跨项目 consumer 语义不变量已 ACK** → `#23` comment `5660196595` 的 8 条不变量（current-main 能力边界、anchor 非独立 evidence root、ClaimKind 与 stance 正交、`unit_ref -> claim_refs[]` 基数契约、`asserted != believed != true`、fixture-scoped subject ref 不是 Subject Resolution 输出、observed/effective/story/knowledge time 语义分离且不得伪造 UTC）与 2 条 LHRM 侧澄清。**不要重新设计 Eye→Juece→LHRM 的对接语义**。
6. **经验验证通道的分层与纪律已成文** → `#29`（A–F 分层、数据要求 7 条、`Dataset-to-LHRM Mapping Spec` 字段、8 条关键纪律）。**不要另起一套验证分层**。

### 8.2 不要重做的 canonical pointer 清单（已有 DOI/URL）

| 主题 | 指针 | 出处 |
|---|---|---|
| Social Relations Model | `https://davidakenny.net/ip/srmip.htm` | `STAGE_SUMMARY` §5.1 |
| APIM | DOI `10.1080/01650250444000405` | `STAGE_SUMMARY` §5.2 |
| Investment Model | DOI `10.1016/0022-1031(80)90007-4`；DOI `10.1111/j.1475-6811.1998.tb00177.x` | `STAGE_SUMMARY` §5.3 |
| Interpersonal Circumplex | DOI `10.1002/per.2410050503`；review `https://onlinelibrary.wiley.com/doi/10.1002/9781118001868.ch4` | `STAGE_SUMMARY` §5.4 |
| Relational Models Theory | DOI `10.1037/0033-295X.99.4.689` | `STAGE_SUMMARY` §5.5 |
| Ideal Standards Model | DOI `10.1037/0022-3514.76.1.72` | `STAGE_SUMMARY` §5.6 |
| Mate Evaluation Theory | DOI `10.1037/rev0000360` | `STAGE_SUMMARY` §5.7 |
| Fourteen Core Principles of Close Relationships | DOI `10.1146/annurev-psych-010416-044038` | `STAGE_SUMMARY` §5.8 |
| Mate evaluation 年度综述 | DOI `10.1146/annurev-psych-012224-025712`；`https://pubmed.ncbi.nlm.nih.gov/35389716/` | `ARCHITECT_RECONNAISSANCE_REPORT` 外部证据 1–2 |

> 注意：`SCIENTIFIC` §11 使用 author-year 简引并自述「文献细节请在外部库核对」，**不含 DOI**。因此上述 9 条是仓库内**唯一**带 DOI 的成熟理论锚点集合；R14/R01 若要建立可核验文献库，必须自己补 DOI，不能引用 §11 当作已核实来源。

### 8.3 不要重复的 discipline（已成文，反复被重申）

- 不把 literature 数量或 LLM 一致度当 validation（`#30` body、`00_CHILD_CONTRACT` §5）。
- 不把 AI 建议静默升格为 Human requirement（`#30` body）。
- Unknown 不等于 neutral / perfect（`AGENTS.md`、`STAGE_SUMMARY` §3.4、`RELATIONSHIP_EVALUATION_FOUNDATION` §4.4）。
- Case Bank ≠ population calibration；Longitudinal dyadic dataset ≠ case narrative（`#13`「核心研究纪律」第 1 条）。
- provenance quality ≠ fact status（`#13` 第 2 条、`CURRENT_ARCHITECTURE` §10、`AGENTS.md` Validation discipline）。
- 映射失败先诊断 hole 类型，禁止现场新增 primitive（`PARAMETER_CONVERGENCE` §13、`#13` comment `5606725482` §6）。
- 虚构世界规则优先进 Environment/History，不污染 Human relationship primitives（`AGENTS.md`、`CURRENT_ARCHITECTURE` §10）。
- 神经/生物术语默认留 mechanism 层，不因「更底层」升级为 primitive（`SCIENTIFIC` §5.4/§9.4、`AGENTS.md`、`STAGE_SUMMARY` §3.2）。

---

## 9. 给后续 lane 的操作性映射（不是裁决）

1. **R01 / R02**：**Round-3 更正——本条原为不可执行**。原文写「从 §7 的 **S-9（F-09 表）**开始」。**两处指针都不成立**：(i) **本文件没有任何 `F-xx` 条目**（§7 只有 `S-1`…`S-13`；机械核对：全文 `F-09` 只出现在本行与 §4.3 `G-17` 行内，**无任何定义**）；(ii) §7 的 `S-9` 讲的是「`#23` body 的 Juece surface 与 fixture 001 描述过期」，**与构念层归属分歧无关**。**原样保留在此供 grep**：
   > ~~从 §7 的 S-9（F-09 表）开始，而不是从「重新审计 8 个 construct」开始。~~
   **改指（可执行）**：从 §4.3 的 **`G-17`**（层归属分歧，指向已改为 §4.2 `S-I` + `G-04`/`G-06`/`G-07`）与 **§4.3 的 `G-01`–`G-03`**（Gate A/B/C）开始。至少要处理 PPR、OutcomeDependence、Cohesion、Distrust 四处分歧——**但注意 Round-3 已裁决其中一处**：`X-1` `DECIDED`（`PPR` 留在 `BeliefState`）、`X-4` `DECIDED`（`Trust` 与 `AttachmentSecurity` 各自保留为 candidate，`domain` 为可选 facet），故后两处的可执行范围是 **`OutcomeDependence` 与 `Cohesion`**，以及 **`Trust` vs `AttachmentSecurity` 的 facet 切点（待 M2 式证据）**。
   注意 `PARAMETER_CONVERGENCE` §4/§6/§9 已经给了每项的**降级理由**，`SCIENTIFIC` §6/§7 已经给了**成对比较与裁决**，两者结合才是完整起点。**另注**：canonical §2 的六条判据**全部无 procedure / required evidence / output field / threshold / designated executor**，且只有 §2.6 用删除框架、§2.2/§2.5 用降级框架、**三条（§2.1/§2.3/§2.4）没有后果句**（`review-r2` R-A2）⇒ 「从判据开始」本身也不可直接执行。
2. **R03**：仓库内**没有** instrument 目录（G-13）。可以从 §6 的映射表反推「哪些 construct 已被反复拆过」，但 scale/item/信度/效度/不变性必须新建。
3. **R04**：`REAL_WORLD` §5 是 prior/base-rate 清单，**不是** dyadic 测量清单。不要把它当成 20 个 dataset 候选交差（G-14）。
4. **R05**：`STAGE_SUMMARY` §5.2 的 APIM 指针是仓库内唯一已登记的 dyadic 统计方法锚点，可直接继承。
5. **R15**：先解决三套分级轴的对齐（G-18 / S-13），否则下一批 fixture 会重复 corpus 的轴不一致。同时注意 S-11：当前 romance/kin/caregiving 的表示覆盖证据为 0。
6. **R16**：`#29` 已给全部字段；缺的是实例与 leakage/outcome 切分规则。
7. **R17**：本文件 §4.3 的 G-01…G-18 全部是**尚未被证伪也尚未被证实**的项，可直接作为 falsifier 搜索靶点。但请注意独立性约束：R17 首稿不得读 R01–R16 输出，也不应把本文件当作「已确认的漏洞清单」——本文件只做了**映射**，没有做**判断**。
   **Round-3 附注**：`X-8` 要求「12 robust agreements」换成审计过的 `N-A1…N-A12` 独立来源 × 方法记账（`00_MANIFEST` / `19` 由 sibling `A2` 负责）；`X-12` 要求移除「唯一真 blocker」并把**负结果移出 blocker 列表**——本节 `G-19` 已按此改标为 `EXTERNAL_GAP`（见 §4.3 表前定义）。
8. **Parent（join 时）**：
   - `#2` 建议补一条 status 收口 comment（不必改 body）；
   - `#3/#4/#5/#6` 建议在 `#2` join 已交付（`18cd72c`）的前提下由 Architect 收口；
   - corpus 与 issue body 的 stale 内容建议**新写 supersession 记录**（例如本文件或后续 `19_SYNTHESIS_CANDIDATE.md`），**不要回改已 merge 文件**；
   - `DATING_APP` 报告路径归一可作为独立小 PR，但注意 `#30` 禁止本 attempt 改 canonical 面——报告路径属研究目录整理，需 Architect 明确授权。

---

## 10. 明确不主张（explicit non-claims）

本文件**不主张**：

1. 不主张任何架构 verdict、参数裁决、层级归属；§4.3 G-17 的四处分歧只被记录，未被裁决。**Round-3 附注**：`X-1` / `X-4` 已**由 Architect 裁决**其中两处（`PPR` 留 `BeliefState`；`Trust` / `AttachmentSecurity` 各自保留、`domain` 为可选 facet）。本文件记录该裁决**已被签发**，**不主张**本文件有权裁决其余两处（`OutcomeDependence` / `Cohesion`）。
2. 不主张 `#2/#3/#4/#5/#6/#15` 应当关闭，也不主张任何 issue body 应当被改写。
3. 不主张 `VALIDATION_CORPUS_V0_1.md` 的任何素材指针在 2026-09-27 仍 live 可访问（其 verification log 记于 2026-09-11；已知 `L1-001` 旧址在 2026-09-14 已 404）。
4. 不主张四份 `RESEARCH_REPORT_*` 的外部引用正确——`UNVERIFIED_AS_OF_2026-09-27`；`SCIENTIFIC` §11 为 author-year 简引无 DOI；`REAL_WORLD` §5 的统计数字未给逐条 URL/DOI。
5. 不主张 Eye / Juece 当前状态；相关陈述全部为经 LHRM issue comment 的转述。**Round-3 追加**：`G-20` / `G-21` / `G-22b` / `G-22c` 新增的外部状态（`eye#54` ACCEPT、`eye#57` completed/closed、`THREE_FIXTURE_GATE = CLEARED`）**同样只是转述**（`TRANSCRIBED_NOT_OPENED`）——本 lane **未打开** `youling/eye` 或 `youling/juece` 的任何 issue。**Round-3 追加**：`X-7` 裁定 rights fail closed；`G-19` 的「已关闭且无 durable 交付」同样只是转述。
6. 不主张任何 construct、量表、transition 形式、统计数字已被验证。
7. 不主张「多份报告互相一致」构成 validation。
8. 不主张 sibling lane 的任何结论；本文件与其它 lane 相互独立产出。
9. **Round-3 新增**：不主张 `G-20` / `G-21` / `G-22b` / `G-22c` 的外部状态为**当前**状态——它们是 2026-09-24 / 本 attempt 起点时的转述快照，需 live recheck。
10. **Round-3 新增**：不主张 §4.2 的 `S-I` / `S-J` 是 `SUPERSEDED`（本轮已改标为 `CONTESTED` / `OPEN_GAP`），也**不主张**它们已被 `X-1` / `X-4` 取代——`SCIENTIFIC` §7.8 / §7.7 的文本仍在，两侧仍未冻结。

---

## 11. 剩余未知

| id | 未知项 | 为何未知 |
|---|---|---|
| U-1 | 隔离 verifier lane 是否已有任何 durable 结果 | 隔离契约禁止本 lane 查询；唯一可用的 LHRM 侧间接证据是 `#23` comment `5813587483`（2026-09-24：无 durable delivery） |
| U-2 | Eye 是否已提供 ≥2 个可取得的 dyadic/longitudinal dataset 或明确 access gate | 跨项目禁令范围 |
| U-3 | Juece thin-adapter smoke 是否完成 | 跨项目禁令范围；LHRM 侧最后记录为 2026-09-14 `RELEASED/DISPATCHED` |
| U-4 | corpus 12 份素材指针的当前可访问性 | 未做 live re-fetch；corpus log 记于 2026-09-11 |
| U-5 | prior report 的外部文献正确性 | 未打开任何外部来源 |
| U-6 | `docs/foundation/*` 与四份 report 之间是否还有第 5、第 6 处分歧 | 本 lane 只做了定向比对，未做逐条 semantic diff |
| U-7 | 是否存在任何形式的 `Dataset-to-LHRM Mapping Spec` 实体 | LHRM repo 内未找到；Eye 侧 `UNKNOWN` |
| U-8 | R01–R17 其它 lane 的产出 | 按设计隔离 |

---

## 12. 一句话总结

**架构面（`docs/foundation/*`）自 2026-09-10 起零修改、语料与三份冻结 fixture 自 2026-09-14 起零修改，当前架构 currentness 无漂移；真正的开放研究面集中在三处：`PARAMETER_CONVERGENCE_V0_1.md` §15 的 Gate A/B/C 尚无任何 durable 执行证据、§4/§6/§9 内记录的 6 个显式 open question 尚无数据答案、以及 `#2/#3/#4/#5/#6/#15/#23` 七条 issue 的呈现相对已合并证据已经过期（纯 bookkeeping，不是架构错误）。**
