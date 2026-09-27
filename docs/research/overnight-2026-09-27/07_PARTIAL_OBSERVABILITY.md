# 07 — 稀疏输入 / 缺失性 / 不确定性的深度审计

**Status:** `RESEARCH_CANDIDATE` — 未经 Human/Architect 审阅，不得当作已确立结论、参数或公式
**Lane:** R07 · Wave 1 · Work Order `youling/lhrm#30@overnight-opencode-exploration-swarm-v1`
**Scope:** 只审计「`Unknown` 应如何表示、应如何传播、应如何被读出」，不提出新的关系构念，不改动 ontology
**核实日期:** 2026-09-27（所有时效性声明均以此日为准）

> 证据等级约定：`CITED_PRIMARY`（读到原文或官方摘要全文）/ `CITED_METADATA`（只核到 DOI 元数据，未读正文）/ `CITED_SECONDARY`（转述页）/ `AGENT_RECALL`（先验，本次未核）。模型层面的推断一律标 `MODEL_HYPOTHESIS`，架构建议标 `AI_RECOMMENDATION`。**文献数量与 LLM 一致度不构成验证。**
>
> **`[ESTABLISHED]` 的处置（Round 3 修复，选「补进约定表」这一支）**：本文件正文用了 15 处 `[ESTABLISHED]`，而本约定表只定义了 6 个标签。Round-3 复核（review-r2 `E-C13` / `H-F13`）把这一项判为**缺陷**并要求二选一。**本 child 选「把它加进约定表并定义」，不选「停用」。** 理由：15 处使用全部出现在「有已核来源紧随其后、且本报告不做外推」的句子上；把它们删掉会丢掉「这条是承重的、不是本报告的推断」这一信息，而这正是 `MODEL_HYPOTHESIS` 标签要承担而本文件当时没有承担的工作。定义如下：
>
> ```text
> [ESTABLISHED]   不是第七个证据等级。它是一个「支撑」标签：
>                 该行的结论由紧随其后的 CITED_* 来源直接支撑，
>                 本报告在本格内不加任何外推。
>                 判定规则：一旦本格内出现外推、类比或强度提升，
>                 必须改标 MODEL_HYPOTHESIS（并写出外推的那一步）。
> ```
>
> **15 处使用点（Round 3 于 2026-09-28 逐条复核；按小节锚定，不按行号——行号会随其它修复漂移）**：
>
> | 小节 | 处数 |
> | --- | --- |
> | §6 FM-01 / FM-02 / FM-04 / FM-05 | 1 + 1 + 1 + 1 |
> | §6 FM-06 / FM-07 / FM-08 | 2 + 1 + 1 |
> | §7.1 / §7.2 / §7.3 | 1 + 2 + 2 |
> | §8.1 / §8.2 | 2 + 1 |
> | **合计** | **15** |
>
> 判定：15 处**全部**是「已引来源紧随其后、且本报告在该格内不加外推」——与上定义一致。其中 Round 3 改写了 FM-05（书目/术语）、FM-06（作者表）、§7.2（作者表）三处；改写后它们仍满足本定义。**全文不再出现未定义的标签。**

---

## Round 3 修复记录（`r3/a3d`，依 `ARCHITECT_ADJUDICATION_V1` + review-r2）

| # | 位置 | 缺陷 / 裁决 | 处置 | 依据 |
| --- | --- | --- | --- | --- |
| R3-1 | §2.3 | Belnap K4 两个序的**方向画反了**（`N`/`B` 的角色互换） | **重写整段**，保留旧文本于 `SUPERSEDED` 块 | review-r2 `R-E1` / `R-E2` / `E-C3`；`H-D4` 之上位条 `H-D3` |
| R3-2 | §5 开篇 / §5.3 / §9.1 #11 / §13 | 「15 条」实为 **19**；「9 条现在就能检查」不可执行 | 改为 19 + 逐条可执行性分类 | `R-E9` / `E-C12` / `E-C11` / `H-F12` / `H-F14` |
| R3-3 | 文件头 `:8` | 约定表缺 `[ESTABLISHED]`，正文用 15 处 | **补进约定表**（见上） | `R-E` 区 `E-C13` / `H-F13` |
| R3-4 | §0.1 | 「唯一 1 处命中」是检索范围产物，不能支撑穷举否定 | 改为**检索范围声明**，附 Round 3 复检 | Architect **X-14**；review-r2 `E-C2` |
| R3-5 | §2.2 / §4.3 | credal 组合「松的程度依赖一个未被声明的独立性假设」`UNSUPPORTED` | 标 `UNSUPPORTED` + 要求补 imprecise-probability 引文 | `H-D4` / `E-C6` |
| R3-6 | §2.2 | `2^B` 全幂集 NP-hard → `HOLD_FOR_EVIDENCE`，且须先声明 tractable subset | 标注 + 要求 `ORD-Horn` 之类声明 | `R-E4` / `E-C7` |
| R3-7 | §2.2 / §5.4 / §8.1 | imprecise-probability 正面结果缺 `no_evidence` / `refused-to-answer` 限定语 | 逐处补限定 | `E-C8` |
| R3-8 | §3.4 | 定理层接受、落地层（`Info` 定义、`RelMergeability`）仍是 proposal | 分层标注 | `H-D3` / `E-C5` |
| R3-9 | §6 FM-05 + 参考文献 [5] | 书目年错（2021 → 2023）；术语 `bounded-coverage` → `bounded-abstention`、`reject model` → `rejection model` | 改正 + 加 `REFUSE` 一等输出陈述 | `H-D5` / `E-C9` |
| R3-10 | 参考文献 [6] | 作者表**错误**（`Rajaraman, D.` 等） | 改为 `Ghosh, D., Rahme, J., Kumar, A., Zhang, A., Adams, R. P., & Levine, S.` | `E-C10` |
| R3-11 | §0 第二行 / §13 | 「missingness lowers certainty, not computability」在仓库内**字面不存在** | 标 **`NEGATIVE_RESULT`**（本 cluster 最有价值的一条） | `R-E3` / `E-C1` |
| R3-12 | §1 分类表 / §9.3 | `disputed` / `reporter_role` / `Divergent` 三处**同名不同义**；与 `08b` 零协调 | 显式标注重复 + 收敛路由给 taxonomy child；**不发明第三套编码** | `R-E8` / `E-C23` / `H-F15`；**C-P5** |
| R3-13 | §9.3 | 适用性必须是**独立轴** | 加 applicability 轴（`APPLICABLE / NOT_APPLICABLE_BY_RULE / APPLICABILITY_UNKNOWN`），**不**折进 `Unknown` 枚举、**不**折成 `0` | **C-P5** / X-5 / 裁决 §C.3 |
| R3-14 | §11-3 | 可观察性登记表缺口被本文件与 `08b` 各写一遍 | 合并为**一条**带唯一 owner 的阻塞项 + 指针 | **C-P13** / `E-C16` / `R-E6` |
| R3-15 | §5.4 | 「可安全落地」的落点写错 | 改标 `RECLASSIFY_AS_METHOD_LIMIT`，落点是研究纪律段而非构念变更 | dispatch `E-C8` 区 / `X-12` 同型 |
| R3-16 | §2.3 / §9.3 | 本文件把若干 belief 侧构造的**层归属**留作开放 | 补一段：PPR 类 belief 构造留在 BeliefState；改层位须走**明确架构修订** | Architect **X-1** / 裁决 §C.1 |
| R3-17 | §7.1–§7.3 / §6 FM-09 / §9.1 #10 | partial pooling 与方向性 invariant 冲突 | 标为**实现约定 + readout 要求**（proposal only） | `E-C15` |
| R3-18 | 全文 | Kuhn's dogmatism paradox | 标 `PLAUSIBLE`，作为 open question 路由 | `E-C25` |
| R3-19 | §3.2 引用 [24] | 「`ORD-Horn` 之类 tractable subset」尚无已打开来源 | 标 `NOT_OPENED` | 本 child 纪律 |

**本 child 未做**：任何 canonical 改动（`D1`–`D5` 由 sibling 落地）；任何 merge；任何 Gate A/B/C 运行；`#20`/`#21`/`#22` 未读未执行未引用；未做文献横扫（除为修 `E-C9`/`E-C10` 而定点打开的 2 条书目）。

---

## 0. 本报告的定位与两条主张的准确措辞

本 lane 被指派审计两条项目主张。核验结果：

| 指派中的主张 | 项目内实际文本 | 位置 | 判定 |
| --- | --- | --- | --- |
| `Unknown -> prior / conditional distribution` | `Unknown -> prior / uncertainty`（对照 `Unknown -> zero deviation`） | `docs/foundation/PROJECT_HISTORY_2026-09-10.md:102`、`:108` | 存在。**但作为恒等式成立，作为设计规则未经规定** |
| "missingness lowers certainty, not computability" | `Computable != Certain` | `docs/foundation/STAGE_SUMMARY_2026-09-07.md:162` | **字面形式不存在。** 项目持有的是**更弱**的区分性陈述 |

**第二个措辞的差异不是文字游戏：**

- `Computable != Certain` 只说「可计算与确定不是同一件事」。
- "missingness lowers certainty, not computability" 是一个**不变性主张**：它断言缺失作用在确定性上、**不**作用在可计算性上。

第二个更强，而**第二个部分为假**（§6）。本报告因此：

- **不**把项目判为「主张了错的东西」；
- **而是**给出：弱版本成立的理由、强版本失效的 8 个模式、以及两者之间那个恰好可写进 canonical 的中间版本（§5.4）。

### 0.0 `NEGATIVE_RESULT`（Round 3 登记；本 cluster 最有价值的单条发现）

```text
claim_id : A3D-NR-01
kind     : NEGATIVE_RESULT
strength : VERIFIED（可机械复算）
scope    : **项目文本面** = docs/foundation/** + AGENTS.md + README.md
           （**不**含本 overnight 研究语料，理由见下）
claim    : 字符串 "missingness lowers certainty, not computability"
           在**项目文本面**的任何一个文件中都不存在（Round 3 于 2026-09-28 复检：
           0 命中）。
held     : 项目实际持有的更弱区分性陈述
           `Computable != Certain`
           （docs/foundation/STAGE_SUMMARY_2026-09-07.md:162）
self_ref : 全树复检会命中 **本文件自己**（5 处），因为本文件必须**引用**
           被审计的那句话才能审计它。Round 3 之前已有 2 处同样性质的自我引用。
           ⇒ **该 NEGATIVE_RESULT 的可复算形式是「在项目文本面 0 命中」**，
             不是「全树 0 命中」。凡声称「全树 0 命中」的表述都不可复算。
implication: mission 指派给 07 的第二条主张，其**指派来源**不是项目文本。
             任何把它当「LHRM 已经持有的不变性主张」的引用都必须撤回。
review    : review-r2 REJECTED_OR_WEAK_FINDINGS.md R-E3 / CROSS_LANE_VERDICT_MATRIX.md E-C1
             —— 判语：「这是本 lane 最有价值的一条，应作为 NEGATIVE_RESULT 进入 join」
```

**指派的正确读法（Round 3 更正）**：mission 把该句交给 `07` 去**核验**，而不是断言项目持有它。`07` 的职责因此是 `(a)` 报告它不存在、`(b)` 给出项目实际持有的弱版本、`(c)` 说明强版本在哪些模式上失效。本文件原 §0 的表述已足以传达 (a)(b)，但**没有把结论登记为 `NEGATIVE_RESULT`**，也没有指出「指派来源 ≠ 项目文本」这一层。Round 3 补上。

> **这不是 blocker。** 按裁决 X-12，一条负面结果**不是**阻塞项；它的作用是阻止 join 阶段把该句当作已确立的项目主张传播。

### 0.1 一个必须先说的空白（Round 3 已重述为**检索范围声明**）

**原文本（`SUPERSEDED_BY_REPAIR`）**：

> 对 `D:\coding\lhrm\**\*.md` 全量检索 `refine|monoton|⊑|preorder|lattice|composabl|propagat`，**唯一 1 处命中**且与数学格无关：
>
> ```
> docs/RESEARCH_REPORT_DATING_APP_PARAMETER_PRIMITIVES.md:240
> | B12 | 家庭背景财富 | 家庭资源 + 赡养义务 | O/E | 百合字段；承担 lattice 但不可当个人资源 |
> ```
>
> **LHRM 现有 durable 资料中，没有任何关于 refinement、单调性、预序、数学格、或 `Unknown` 组合传播的形式化内容。**

**为什么必须改**：按 Architect **X-14**（"Replace field-wide existence claims with **search-scope claims** unless sampling supports population/general absence. 'No qualifying dataset found in this audited landscape' is allowed; 'the intersection is empty in the field' is not."）——「全量检索唯一 1 处命中」是一个**检索方法的陈述**，不是**总体不存在的证据**。理由具体有三条：

1. **7 个英文词根的正则无法支撑穷举否定。** 若项目内部曾用 `order-theoretic`、`supremum`、`infimum`、`coarse information`、`poset`、`join`、`meet`、`lattice-ordered`、`entailment` 表述同一件事，本检索**一条都抓不到**。
2. **检索发生在本轮研究语料落盘之前。** 当时 `D:\coding\lhrm\**\*.md` 里还没有 `07`/`08b`/`19`；今天同一检索在同一语料上会返回 **46 行 / 8 个文件**。命中数随语料增长而变 ⇒ 它测的是**当时那棵树**，不是「durable 资料」。
3. **唯一命中本身是假阳性。** 那一行里的 `lattice` 是「百合」的意思，与数学格无关——原文自己也这么写。它**不能**作为「全库只此一处」的锚点来支撑任何计数。

**Round 3 复检（本 child 实跑，见 packet `verification`）**：

| 范围 | 模式 | 结果 |
| --- | --- | --- |
| 本 worktree 全部 `*.md`（43 个文件） | `refine\|monoton\|⊑\|preorder\|lattice\|composabl\|propagat` | **46 行 / 8 个文件** |
| 同上，剔除 `docs/research/overnight-2026-09-27/**`（即只剩 durable 资料） | 同上 | **1 行 / 1 个文件**，且是上面那条假阳性 |
| canonical-only（`docs/foundation/**` + `AGENTS.md` + `README.md`） | `preorder` | **0** |
| canonical-only | `⊑\|subsumption\|refinement\|monotonic` | **0** |
| canonical-only | `partial order\|information order\|knowledge order` | **0** |
| canonical-only | `单调\|预序\|数学格\|缩窄\|双序\|bilattice` | **0** |
| canonical-only | `lattice\|格` | 8 行，**全部**是中文 `格` 的假阳性（`规格` / `严格` / `性格` / `可严格` / `缩略` 等），**无一条**是数学格 |

**重述后的结论（可按现状引用）**：

> **在 Round 3 复核的检索范围内**——即本 worktree 于 `8adcf0b` 的 canonical 面（`docs/foundation/**`、`AGENTS.md`、`README.md`）——**没有找到**任何关于 refinement / 单调性 / 预序 / 数学格 / bilattice / `Unknown` 组合传播的形式化内容。**这是一个检索范围结论，不是领域或仓库范围的否定存在结论。** 本报告因此**不是**对已有设计的修补建议，而是**新增候选**。
>
> **不主张**：LHRM 的 durable 资料「不存在」这类形式化。**不主张**一次关键词正则能覆盖中文或符号化的等价表述。若要升级为穷举否定，需要一次**按概念族**的系统检索（含等价术语表），本轮**未做**（`NOT_OPENED`）。

**对下游的净效果不变**：本文件仍然不是「修补一个已被违反的不变量」，而是新增候选。变的只是这句话的**可辩护性**。

---

## 1. 缺失性的机制分类：为什么 `Unknown` 不是一个类型

在讨论表示之前，必须先说清「缺失」有多少种，因为**不同种类的缺失在数学上不是同一个问题**。

`[MODEL_HYPOTHESIS]` 下面的分类是本报告的工作分类，用于后续类型化；每种给出机制类型、数学后果、以及它是否让「`Unknown → prior`」成立。

| tag | 机制 | 机制类型 | 对该 dyad 的正确数学类型 | `Unknown → prior` 是否成立 | 证据 |
| --- | --- | --- | --- | --- | --- |
| `no_evidence` | 无人报告、也无人不报告 | MCAR/MAR | 分布（可能是多峰） | 名义上成立（= 先验） | — |
| `refused` | 被问及但主体拒答 / 选「无意见」 | **MNAR** | **比先验更宽的集合**；不做插补 | **不成立** | Krosnick et al.：拒答主因是 satisficing（疲劳、低努力、题目靠后、低教育），且给出 "don't know" 选项**降低**了实质回答数却**不改变**重测信度（`CITED_PRIMARY`，完整书目 `PARTIAL_BIB`） |
| `private_to_partner` | 存在但只对 partner 可观测 | **结构性单侧可观测** | 需按 reporter 索引；`PairState` 上不 reporter-invariant | **不成立**（读者侧无信息 ≠ 人口先验） | Swann et al. (1994)：婚内伴侣报告呈 self-verification 系统偏倚，N=176 夫妻（`CITED_PRIMARY`，摘要） |
| `withheld_by_actor` | 主动隐瞒 | **MNAR 且机制内生** | 与 `refused` 同类，但机制模型不同 | **不成立** | 同上 + Belnap 1977 动机 |
| `disputed` | 存在相反证据 | **冲突** | 需独立于 `n` 的值（K4 的 `b`） | **不成立，且不可映射到 `n`** | Belnap 1977；Mundhenk et al.（`CITED_PRIMARY` / `CITED_SECONDARY`） |
| `censored` | 结构性空单元（如只对自报使用者询问使用行为） | **MNAR，按构造** | **结构性空**；不是小样本 | **不成立**（见 FM1） | Tennenholtz 2023 的 delphic 不可约性（`CITED_PRIMARY`） |
| `structurally_unobservable` | 原则上不可被该通道观测 | **非认知** | **不进入状态**；输出 "not addressable" | **不适用** | — |
| `not_yet_real` | 尚未发生 | **时间性** | **未来未定义**；需 trace/truncated 域 | **不适用** | 需与 §2.3.1 的两个序区分（`not_yet_real` 落在 K4 **之外**，需第三条正交轴） |
| `superseded` | 被更新证据取代 | 惰性 | 由 `history_id` DAG 承载 | — | `CURRENT_ARCHITECTURE.md:241-252` 已有 `tau = (history_id, local_time)` |
| `unmeasured_by_instrument` | 工具未测 | 测量层 | 需 measurement model，否则不可辨识 | **不成立** | Raykar et al. 2010（`CITED_PRIMARY`） |

**这张表是本报告最重要的产出之一。** 它的直接后果是：

> `Unknown` 不是一个类型，它是**至少四个不同数学对象**的共同标签。`AGENTS.md:24` 禁止了「静默压成 neutral」，但目前**没有**任何规则禁止「把 10 种 `Unknown` 压成一个 `Unknown`」——而后者是同一种违规的更隐蔽形式。

### 1.1 Round 3：这张表**不是**唯一编码，且**不得**被直接并入 canonical（`R3-12` / `R3-13`）

**显式声明：本表与 `08b_BELIEF_DECEPTION_KNOWLEDGE.md` 各自分别发明了一套「缺失 / 不适用 / 冲突 / 不可寻址」的分区，两者零协调。** 下面三条同名不同义是**已核实**的（`review-r2 H-F15` / `E-C23`）：

| 同名 / 近名 | 本文件（`07`）的含义 | 别处的含义 | 碰撞类型 |
| --- | --- | --- | --- |
| `disputed` | 缺失机制：存在相反证据（表第 6 行） | `CURRENT_ARCHITECTURE.md:315` 的**事实状态**：`adjudicated\|admitted\|alleged\|disputed\|unknown` | **同名不同义**（缺失机制 vs 事实状态） |
| `Divergent` | 不在本文件 | `08b` §4.3 的**主体立场对立**派生类（`k_ι=+, k_ι'=−`） | **同名不同义**（无争议 vs 对立） |
| `reporter_role` | §9.3 记录层的一个字段名 | canonical 的 `Role` 是 **query/evaluation lens**，不是世界状态（`CURRENT_ARCHITECTURE.md:96`；`AGENTS.md` 当前架构方向第 3 条） | **重复命名 + 层级混淆** |

**直接并入的后果**：10（`07`）+ 4（`08b` 的 `⊘` / `UNKNOWN` / `Divergent` / `ASYMMETRIC` 侧翼）+ canonical 的 5（`CURRENT_ARCHITECTURE.md:315`）去重后仍是一个 **14+ 值枚举**，直接违反 `AGENTS.md:22`（few stable constructs）与 `AGENTS.md:24`（不得静默压平）。**本 child 不发明第三套编码，也不做合并。** 收敛由 Track R3-F 的 taxonomy child 负责（`ARCHITECT_ROUND3_DISPATCH_V1` §Track R3-F：产出**两轴**候选分类——epistemic/measurement 不确定性轴 + 构念适用性轴——并给出所有既有词汇的转换表；`MAPPING_FAILURE` 留在两轴之外）。

**关于独立性的一句硬话**：`08b` 的存在**不是**对本表的存在性结果的独立佐证。`08b` 在写它的 §0 / §9-11 明确写了「本 lane 未读 `PARAMETER_CONVERGENCE_V0_1.md`…既有报告 A–D」。**它没有读本文件。** 因此「两个 lane 各自发现同一件事」在这两处**不成立**：它们是两次各自发明的**收敛**，不是两次独立发现的**复制**。（这与 `X-8` 的独立性审计是同一类错误：`independent_sources=0` 不构成 robust agreement。）

### 1.2 Round 3：适用性必须是**独立轴**（Architect **C-P5** / X-5 / 裁决 §C.3）

**本文件不主张**在这 10 个 tag 里加入任何一个「不适用」值。Architect 已裁定（X-5「**DECIDED: PERMISSIVE, NOT CLOSED**」）：

> 值域是**许可式**，不是封闭枚举。「Not applicable because the construct has no independent meaning in this dyad/context」**既不是 0，也不是 Unknown**；它必须落在**一个独立的适用性轴 / 规则元数据**上，并在适当时带 Boundary/Constraint provenance。**不要**把 `NA` 加进坐标值域。

因此：

- 本表 10 个 tag 全部属于**认知 / 测量侧的不确定性**，`structurally_unobservable`（第 8 行）虽然最接近「不适用」，但它仍是**测量侧**的（不可被该通道观测），**不是**构念在该 dyad 无独立语义；
- 构念适用性是一条**正交**的轴，最小候选词表 `APPLICABLE | NOT_APPLICABLE_BY_RULE | APPLICABILITY_UNKNOWN`，附 reason/provenance（`C-P5`、dispatch `D2`）；
- `MAPPING_FAILURE` 留在**两条轴之外**（它是表示失败，不是证据状态，见 `AGENTS.md` validation discipline）。

**本 child 不实施任何一条**（canonical 落地由 Track R3-D 的 measurement-semantics child 拥有）。

---

## 2. Unknown 表示的候选形式化菜单与代数性质

### 2.1 六个候选

| 编号 | 表示 | 载体 | 支持的运算 | 丢失什么 | 成本 | 是否过度设计 |
| --- | --- | --- | --- | --- | --- | --- |
| **R1** | 点 + 置信度 `(v, p)` | `ℝ × [0,1]` | 比较、排序、平均、欧氏距离 | **多峰性**、机制 tag、`Unknown` 的类型；把 `⊥` 与「0.5」混同 | 极低 | **不推荐。** `p = 0.5` 就是一个 neutral 值，直接违反 `AGENTS.md:24`；且它无法表达「我不知道」与「我认为是 0.5」的差别 |
| **R2** | 区间 `[a,b]` | 带 `⊥` 的 Scott 域上的闭区间 | `min`/`max`（t-norm/t-conorm）、宽度、外延原理（extension principle） | 形状（多峰）、联合分布（独立假设）、机制 | 低 | **推荐做 display 层**；不能替代 R3/R6 |
| **R3** | 分布 `π(·)` | 概率测度 | 全套概率运算、KL、credal 上下界 | **不可辨识性**（多个 `π` 同样拟合数据）、联合结构 | 中 | **推荐做 store 层。** `CURRENT_ARCHITECTURE.md:286` 已允许「estimate + uncertainty + evidence，甚至直接保存 posterior distribution」 |
| **R4** | credal 集 `K(π)` | `π` 的凸集 | lower/upper prevision、robust Bayes、m-convex 决策 | 集合内元素的相容性；**可组合性不平凡** | 中-高 | **延后。** 见 §9.2 |
| **R5** | refinement 预序 `⊑` | `Info` 上的预序 + 集族 | 不可逆更新、单调算子、**单调函数泛函** | 不给「值」，只给「更少/更多信息」；不提供 readout | 低（形式层）/ 中（要真的重写所有算子） | **推荐作为骨架。** 唯一能给出 refinement consistency 保证的结构 |
| **R6** | typed-Unknown 代数 | 小有限格（K4 双序 / RCC 族） | 完整组合表、一致性判定、refinement 变窄、temporal 序 | 数值；需先决定 base relations | 低-中 | **推荐做 Unknown 传播层。** 代数选型留给 Architect |

### 2.2 关键点：R5 + R6 是骨架，R3 是存储，R2 是展示，R1 不推荐、R4 延后

这不是个人偏好，而是成本账：

- **R4 的成本是可证的**，不是估计的。Liell-Cock & Staton (2025, POPL) 明确：把 credal set 用「凸分布幂集」monad 做组合**并不 compositional**，因为该 monad 非交换；他们用 graded monad 修正后得到**更紧**的界（`CITED_PRIMARY`，DOI `10.1145/3704890`）。含义：**朴素的 credal 组合会系统性地给出过松的界。** 这本身就是 `AGENTS.md:24` 同类违规。
  - **`UNSUPPORTED`（Round 3 删除的一句）**：原文在此处还写了「**且松的程度依赖一个未被声明的独立性假设**」。review-r2 `E-C6` / `H-D4` 判这一句**未被该来源支撑**——`10.1145/3704890` 陈述的是**monad 非交换导致组合不 compositional**，并**不**把松的程度归因于一个「独立性假设」。本文件**撤回**该因果归因。**保留成本结论**（不 compositional ⇒ 不能作为默认存储层）。
  - **待补引文**（Round 3 留下的缺口）：要论证「松的程度取决于独立性假设」是**正确**的，必须补一条 imprecise-probability 文献明确如此陈述。**本 child 未打开这样的来源** ⇒ 标 `HOLD_FOR_EVIDENCE` / `NOT_OPENED`。在那之前本文件**不主张**任何关于「松多少」的定量或归因性陈述。
- **R6 的成本是 `PLAUSIBLE`，不是可证的**（Round 3 降级）。原文写「RCC8/IA 的经验：只用 base relations 时一致性判定可算，允许 `2^B` 全部幂集时 NP-hard」。review-r2 `E-C7` 判 **`PLAUSIBLE`**，处置为 **`HOLD_FOR_EVIDENCE`**：**在打开 Renz 2007 正文之前，本条不进入任何排序、不进入 §2.4 的成本表、也不进入 §9.1 的「现在做」清单。**
  - **进入本文件的硬前置条件**（review-r2 明确要求补的一句）：若采用完整不定关系族，**必须先声明一个 tractable subset**（例如 `ORD-Horn` 一类），否则本条对 LHRM 没有可用内容。
  - **来源卫生**：本文件 §12 参考文献 [24] 把 `ORD-Horn` 与 Renz 2007 / Dylla-Botea-Renz / Bhattacharya-Renz 并列写成 `CITED_PRIMARY`。**Round 3 未打开这些正文**（`NOT_OPENED`）⇒ 该条目的支撑强度**就 R3 本轮而言**降为 `NOT_OPENED`，并登记给 Track R3-E 的 carrying-source check（`E3`）处理。本文件因此**只使用**该族的**定性**结论，不引用任何复杂度常数。
  - LHRM 的推论（**条件化**）：**不能**对全部 construct family 同时启用完整不定关系。若要用，**先声明** tractable subset。
- **R2 的成本几乎为零且收益明确**。而且有严格依据说明它能承载什么：Pelessoni & Vicig (2022) 证明，**Jensen / Markov / Cantelli 型界**在 imprecise 知识下仍然成立（在 `22`-coherence 下即可），因为"probability inequalities do not depend on the exact evaluations, hence are especially useful when its knowledge is vague or imprecise"（`CITED_PRIMARY`，arXiv:2211.01503）。
  - **Round 3 强制的限定语（review-r2 `E-C8`；本条是本文件自称「最重要的正面结果」，因此该限定是承重的）**：该定理的适用前提是**有非平凡的 imprecise 先验信息**。它**直接**覆盖 `no_evidence`（名义上 `= prior` 的那一支），但它**不直接**覆盖 `refused` / `refused-to-answer`：**在 MNAR 拒答下正确的类型是「比先验更宽的集合」（FM-08），而不是「一个 imprecise 先验」**——把后者套进 `22`-coherence 会把 `MNAR` 静默重写为 `MAR`。因此**必须**先按 §1 的 tag 分类分型，再决定能不能用 imprecise-probability 结论。**不主张** imprecise-probability 的结论对 `refused` 一支「自动成立」。
  - → **这是本报告给出的最重要的正面结果：缺失后仍可算的是「有界量」，不是「点值」。** 见 §5.3。

### 2.3 三个序，不是三个置信度

Belnap 的四值逻辑给出了一个反直觉但可形式化的结果（`CITED_PRIMARY`，Mundhenk et al.；`CITED_SECONDARY`，Belnap 1977 官方摘要）：

- 取值 `{T, F, B, N}`：`T` = 已知真，`F` = 已知假，`B` = 已知既真又假，`N` = 无信息。
- **`B` 与 `N` 是两个「彼此不相关」的中间值**（原文 "two intermediate (but unrelated) values, namely unknown (n) and known-both-true-and-false (b)"）。
- 该结构上有**两个序**，原文："the presence of **two ordering relations** on it (the **truth order** and the **knowledge order**) has given rise to the interesting notion of **bilattice**"。
- Belnap 自己的评价（S14 官方摘要转述）："**The worst thing is to be told something is false simpliciter.** You are better off (it is one of your hopes) in either being told nothing about it, or being told both that it is true and also that it is false; while of course best of all is to being told that it is true."

#### 2.3.1 两个序各自的极与不可比对（Round 3 更正；**这是本 cluster 唯一的实质内容错误**）

**Round 3 之前本节写的是错的**（`review-r2 R-E1` / `E-C3`：`UNSUPPORTED`）。原文把两个格的性质互换了。保留旧文本于下方 `SUPERSEDED_BY_REPAIR` 块。

**正确的形式化**（两个格，一个把 `N`/`B` 放两端，一个把 `T`/`F` 放两端）：

| 序 | 名称 | 底 | 顶 | 不可比的一对 | 覆盖关系的方向 |
| --- | --- | --- | --- | --- | --- |
| **近似 / 信息序**（`⊑_a`，knowledge order / approximation lattice） | 越多证据 = 越高信息 | **`N`** | **`B`** | **`T` 与 `F`** | `N → T`、`N → F`、`T → B`、`F → B` |
| **逻辑 / 真值序**（`⊑_t`，truth order / logical lattice `L4`） | 越"真"越高 | **`F`** | **`T`** | **`N` 与 `B`** | `F → N`、`F → B`、`N → T`、`B → T` |

**读法**：在信息序上 `N < T`、`N < F`、`T < B`、`F < B`，所以 **`N` 是底、`B` 是顶，而 `T` 与 `F` 不可比**。在真值序上 `T` 是顶、`F` 是底，而 `N` 与 `B` 在两翼不可比。**「`N` 与 `B` 不可比」这句话本身是对的，但它属于真值序，不属于信息序**——原报告把它安到了信息序上，于是把「`B` 是信息最多的值」读反成了「`B` 比 `N` 少」。

**`AI_RECOMMENDATION`（Round 3 更正后）**：

> 状态侧必须**至少有两个序**：
> 1. **信息 / 近似序**（`⊑_a`）：**`N` 是底、`B` 是顶**；`T` 与 `F` 不可比。因此「知道了才收窄」的正确方向是 `N → T`、`N → F`、`T → B`、`F → B`，**不是** `B → T` / `B → F`。
> 2. **真值 / 逻辑序**（`⊑_t`）：**`T` 是顶、`F` 是底**；`N` 与 `B` 在两翼不可比。**正因为不可比**，`B`（既真又假）与 `N`（无信息）不能被压到同一条 confidence 轴上。
> 3. **时序 / 可寻址序**（**正交，非 K4**）：`not_yet_real` 与 `structurally_unobservable` **不在** K4 里，需要另一个正交维度（trace / addressability）。

**因此**单条 confidence 轴在类型上就是错的，不是不够用。**理由现在写对了**：不是因为 `N` 与 `B` 在信息序上不可比（它们在信息序上**可比**），而是因为它们在**真值序**上不可比，而任何单条 confidence 轴都必须同时充当这两个序——两个序在 `T`/`F` 与 `N`/`B` 上给出**互相冲突**的极。FM-03 给出了一个不需要任何数据就能判定该错误为真的反例。

**层归属（Architect **X-1** / 裁决 §C.1；Round 3 补记）**：`⊑_a` / `⊑_t` / 时序轴这三者都是**信念 / 观测侧**的类型构造。本文件**不**把其中任何一个描述为 `Reality` / `DirectedRelationshipState` 的坐标；一个 belief 可以有持久性与因果 / 动力学重要性，而**不因此**成为 Reality-state 成员（这正是 Architect 对 `PPR` 的裁定：`PPR_(i about j,t)` **remains BeliefState**；「organizing variable」、持久性或预测强度**本身不蕴含** Reality-state 成员资格）。若将来要让本节任一构造升格，那是**一次明确的架构修订**，不是本轮证据触发的静默变更。

**Round 3 的核实方式（可复算）**：

- **主源**（本文件 §12 参考文献 [15]，Mundhenk, Rautmann & Schnoor）：下载 `BelnapIGPL.pdf` 并抽取正文，§2 得两条逐字句：
  - "In that diagram, the ordering relation ⊑ goes upwards, thus **f = min M4 and t = max M4**, that is, we are considering the so-called **truth-ordering** relation, which was the one originally considered by Belnap to define his entailment in the way we do in Definition 2.1. It is this ordering relation the one giving that set the structure of a De Morgan lattice."
  - "Note that another ordering relation is also possible (the **knowledge ordering**, going from left to right, **with n and b as bounds**) but then negation has quite a different behaviour; the notion of bilattice has been introduced to organize the coexistence of both orders…"

  即：真值序 `f = min`、`t = max`；知识序的**两个界是 `n` 与 `b`**。同一节还把 universe 写作 `M4 = {f, n, b, t}` 并称之为 `FOUR`。
- 该「`n`/`b` 为界」的构造与 `Belnap 1977` 的 K4 一致：`N` 无信息故在信息序上最低；`B` 收到真、假两路证据故信息量最高。
- **旁证（结构自洽性检查）**：真值序的基 `{f, n, b, t}`（`t` 顶、`f` 底、`n`/`b` 为两翼不可比中间元素）正是 `07` 引用 Belnap 时所说的 "two intermediate (but unrelated) values" 的落点——"unrelated" 指的就是**在真值序上不可比**。原报告把「unrelated」直接读成「在信息序上不可比」，这就是错误发生的机制。
- **本 child 未做**：未取 `M4` 的 Hasse 图原始图形做像素级判读（`Figure 1` 是位图）；依据是同段正文对图的两句**显式文字说明**。若要更硬的证据，需要打开 `Belnap 1977` 原书（`CITED_SECONDARY` 本就未读正文）。

**`SUPERSEDED_BY_REPAIR`（原 §2.3 末两段，逐字保留）**：

> **对 LHRM 的直接后果（原 `AI_RECOMMENDATION`，已撤回）：**
>
> ```text
> 状态侧必须至少有两个序：
> 1. 信息序（`⊑`）：`N < B`？**不，N 与 B 在信息序上不可比。** 唯一单调方向是 `B → T`、`B → F`（知道了才收窄），`N → 任意`。
> 2. 时序 / 可寻址序：`not_yet_real` 与 `structurally_unobservable` **不在** K4 里，需要另一个正交维度（trace / addressability）。
> ```
>
> 因此**单条 confidence 轴在类型上就是错的**，不是不够用。FM-03（N-03）给出了一个不需要任何数据就能判定该错误为真的反例。

**取代依据**：`review-r2 REJECTED_OR_WEAK_FINDINGS.md` **R-E1**（`UNSUPPORTED`，`E-C3`）——「**与 K4 的构造相反**：近似/信息序上 `N` 是底、`B` 是顶、`T` 与 `F` 不可比；逻辑/真值序上 `T` 是顶、`F` 是底、`N` 与 `B` 在两翼不可比。`07` **把两个格的性质互换了**」；及 **R-E2**（针对由错误方向推出的那一条 `AI_RECOMMENDATION` 判 `REJECT`）。

**保留的部分（review-r2 `E-C4` `VERIFIED`）**：「双序」这个**结论**成立，且已核实（`{T,F,B,N}` 上的四值逻辑是 bilattice）；**被换掉的只是理由与方向**。因为 `value_class` 的设计依据建立在这一段上，理由错 ⇒ 依据错，所以必须改而不是只加脚注。

**一处 Round 3 未保留的旧内部引用**：原文的「`FM-03`（**`N-03`**）」中的 `N-03` 是旧版 `07` 的 finding-id 命名空间残留，**本文件未定义 `N-xx` 空间**；Round 3 把它删掉（`N-04`、`N-06` 同）。这与内容更正无关，是一处悬空交叉引用。

### 2.4 成本小结

| | 便宜 | 昂贵 |
| --- | --- | --- |
| 数学 | Scott 域 + K4 是现成的；QCN 单调 refinement 引文可用 | `2^B` 全幂集族：**当前 `HOLD_FOR_EVIDENCE`**（§2.2 `R3-6`），不是「现成的便宜货」 |
| 实现 | `⊥` 传播规则、单调有界 readout、`evidence_mass` 标量、`REFUSE` 一等输出 | 完整 credal store、maximin 稳健决策、端到端不确定性传播、per-coordinate epistemic POMDP |
| 决策 | **现在做**（§9.1） | **延后**（§9.2） |

---

## 3. Refinement consistency：数学上是否可能

### 3.1 答案：可能，而且是经典结果

**定义（`MODEL_HYPOTHESIS`，但数学本身是标准的）**

令 `Info` 为证据状态集合，定义

```
s ⊑ s′   ⟺   s 可由 s′ 遗忘得到（s′ 至少确定与 s 一样多）
```

这是**预序**（自反 + 传递），一般**非**反对称（两个不同表示可能编码同一信息量）。它成为**格**需要额外条件：闭包于 ∧（信息交）与最小上界（相对可合并性，`RelMergeability`）。

**Refinement consistency 的定义：**

```
T : Info → Info   满足   s ⊑ s′  ⟹  T(s) ⊑ T(s′)
```

即：加入证据后跑一次更新，得到的状态**不会**比「少证据时跑一次更新」更不确定。

**经典充分条件：`T` 为 Scott-continuous**（单调 + 保持定向上确界），定义域为一个 dcpo。Belnap 在构造 K4 时**明确采用了这一条件**（`CITED_SECONDARY`：他 "Referring to Dana Scott, he assumes the connectives are Scott-continuous or monotonic functions"）。

### 3.2 三条独立的定理级支撑

| 来源 | 支撑什么 | 强度 |
| --- | --- | --- |
| Dynamic epistemic logic（Baltag, van Ditmarsch & Moss 2008, Handbook of the Philosophy of Science, DOI `10.1016/B978-0-444-51726-5.50015-7`） | public announcement `!φ` **就是一个 refinement 算子**（把 `S5` 模型限制到满足 `φ` 的世界子集），有完整公理化 | `CITED_PRIMARY`（官方摘要页 + 章节片段）。**未逐条核实定理原文** |
| QSR / QCN（Renz 2007, IJCAI-07, `https://www.ijcai.org/Proceedings/07/Papers/083.pdf`） | 不定信息 = `2^B`；传播 = 单调收缩迭代 `r_{x,y} ← r_{x,y} ∩ r_{x,z} ∘ r_{z,y}`，**有限网络必然终止** | `CITED_PRIMARY` |
| De Morgan 格 / bilattice（Mundhenk et al.） | K4 有双序，Scott 连续性定义 approximation lattice | `CITED_PRIMARY` |

**QCN 那个单调迭代是最便宜的落地形态**，值得逐字记下：

> "we can enforce the 3-consistency by iterating the refinement operation `r_{x,y} ← r_{x,y} ∩ r_{x,z} ∘ r_{z,y}` … For finite constraint networks this algorithm always terminates since **the refinement operation is monotone** and there are only finitely many relations."

并且注意 closure 是**不等式**而非等式（`CITED_PRIMARY`，algebraic-properties 文献）：

```
φ(t) ∩ φ(r)∘φ(s)  ⊆  φ(r)∘φ(s)
```

即 **只会变窄，不会变宽**。这正是 refinement-monotone 的精确表述。

### 3.3 会破坏它的四类动作

`[MODEL_HYPOTHESIS]` + 项目内 provenance：

| 破坏 | 机制 | LHRM 内触发点 | 现有防线 |
| --- | --- | --- | --- |
| **(a) forgetting 非单调** | 丢证据反而增不确定（先平均再补插） | 早期 `SoftDistance = sqrt(Σ w_i·dev_i²)` 叠加 `Unknown → prior` 后对已知项做平均（`PROJECT_HISTORY:94-102`） | 弱，仅文字纪律 |
| **(b) 别名 / 合并不当** | 把**不可比**的信息状态映射到同一表示 | 把 `disputed` 与 `unmeasured` 合成一个 `Unknown`（§1 分类表） | **无** |
| **(c) 转移算子非确定** | 状态是点值但 `F` 随机 → 同 history 两次运行给出不同状态 | `X_(t+1) = F(X_t, Action_t, Event_t, Belief_t, Constraint_t, Environment_t)`（`CURRENT_ARCHITECTURE.md:203`）中 `F` 的随机性来源未指定 | 部分。`Gamma_(A,B) = { X_(A,B)(τ) }`（:236）把轨迹写成集合，已隐含承认 |
| **(d) 点投影回写** | `set → point` 不是单调可逆；回写后 refinement 不可恢复 | 「输出 78/100」型 readout 若被写回 `ModelState` | **仅文字禁令**（`PROJECT_HISTORY:116`） |

### 3.4 判定

> **Refinement consistency 对 LHRM 是可达的，但代价是：必须显式声明 `⊑`，必须把所有状态算子重写为 `⊑`-单态。**
>
> **它不会自动成立。** 项目现在**没有** `⊑` 这个概念（§0.1），所以目前既谈不上违反、也谈不上满足。

**Round 3 的分层处置（`review-r2 H-D3` / `E-C5`：定理层 `VERIFIED`，落地层仍开放）**：

| 层 | 判定 | 内容 |
| --- | --- | --- |
| **定理层** | **`VERIFIED` / `ACCEPT`** | `s ⊑ s′ ⟺ s 可由 s′ 遗忘得到`（预序）；refinement consistency = `T : Info → Info` 满足 `s ⊑ s′ ⟹ T(s) ⊑ T(s′)`；`T` 为 **Scott-continuous**（单调 + 保持定向上确界，定义域为 dcpo）是**经典充分条件**；**Belnap 构造 K4 时明确采用了该条件** |
| **落地层** | **`ACCEPT_AS_PROPOSAL`（未决）** | ① `Info` 到底是什么（证据状态集合？含哪些坐标的哪一部分？）；② 何时成为**格**而非仅预序——需要闭包于 ∧（信息交）与存在**最小上界**，即**相对可合并性 `RelMergeability`**；③ 逐坐标依赖表的登记格式 |
| **QCN 可算性边界** | **`HOLD_FOR_EVIDENCE`** | 「有限网络必然终止（因为 refinement 单调且关系只有有限多个）」这条来自 Renz 2007 的引文是 `CITED_PRIMARY`，**该引文本身可用**；但**由它推出 LHRM 的可算性边界**需要 tractable subset 声明，见 §2.2 `R3-6` |

**因此本节的正确读法**：**定理可用，落地未定。** 本文件**不**主张 LHRM 已有 `⊑`，也**不**主张 QCN 的终止性自动适用于 LHRM（终止性要求关系集有限，而 LHRM 的 base relations 尚未选定）。

---

## 4. Unknown 的类型与组合传播

### 4.1 传播规则（`AI_RECOMMENDATION`，可检查）

设坐标 `k` 的状态在类型格 `T_k` 上取值，`T_k` 允许包含底元素 `⊥`。复合状态 `S = (v_1, …, v_n)`。

| 规则 | 内容 | 依据 | 可检查性 |
| --- | --- | --- | --- |
| **C1 吸收（meet）** | `v_k = ⊥` ⟹ `S` 在坐标 `k` 上为 `⊥`。**不得**输出点值 | Scott 域 | 直接 schema 约束 |
| **C2 宽度单调** | `width(composite) ≥ max_k width(component_k)` | QCN 单调收缩 | 属性测试 |
| **C3 有界函数合法、点函数不合法** | 若 `g` 是类型格上的**单调**泛函，则 `g` 在 `⊥` 状态上有良定义的**像集**；报告 `g ∈ g(K)`，**不**报告 `g = v` | Scott 连续性 | 单位测试 |
| **C4 tag 不吸收，取集合并** | 一个坐标可同时是 `private_to_partner` ∧ `not_yet_real` | §1 分类 | schema |
| **C5 逐坐标单调** | 更新坐标 `j` 不得 refinement / un-refine 坐标 `i`，除非存在**已登记**的结构依赖（`∂F_i/∂z_j ≠ 0`） | `CURRENT_ARCHITECTURE.md:209-226`（低冗余 ≠ 低动态耦合） | 属性测试 |
| **C6 `REFUSE` 可达** | 成本敏感读出下，动作集必须含 `REFUSE`，且当任何替代动作的条件风险超过登记阈值时 `REFUSE` 可达。**（Round 3：这是「一等输出」意义上的可达性，不是「默认输出」。见 FM-05 的 Round 3 段落与 §10 非主张 9。）** | Franc, Prusa & Voracek：三个 **rejection model**（cost-based / bounded-improvement / bounded-abstention）**共享同一最优策略** = Bayes classifier + **randomized Bayes selection function** | 存在性测试。**阈值未冻结 ⇒ 本条当前不可执行**（§5.0 的 E 列） |

### 4.2 关于 C3 的具体例示（这是本报告最实用的一条）

设 `Trust(A→B)` 的可信值集合为 `[0.1, 0.6]`，`Dedication(A→B)` 未知。

| 报告 | 是否合法 | 理由 |
| --- | --- | --- |
| `Trust(A→B) = 0.35` | **合法**（作为 display 层 R2） | 区间的中点是一个**展示选择**，不是状态主张 |
| `Trust(A→B) ∈ [0.1, 0.6]` | **合法**，且是推荐的 | 状态本身就是集合 |
| `Trust(A→B) = 0.35`（`Dedication` 已写回状态） | **非法** | 违反 C3 + 破坏 refinement（d） |
| `coverage(i,j) ≥ 0.3`（`coverage` = 非 `⊥` 坐标比例） | **合法** | `coverage` 对「信息变多」单调，可给界 |
| `relationship_quality = 0.62` | **非法** | 点函数、非单调、且坐标含 `⊥` |
| `mutuality 存在 / 不存在 / Unknown` | **合法**（枚举 + `⊥`） | 派生量，类型显式 |

### 4.3 不可复合的部分：credal 宽度的乘积是错的

`[MODEL_HYPOTHESIS]`，依据 `CITED_PRIMARY`（Liell-Cock & Staton 2025, DOI `10.1145/3704890`）：

- 朴素做法：composite 的不确定性 = 各分量 credal 宽度的（某种）乘积。
- 该做法**系统性过松**。
- 正确做法：先做 augmentation（credal 直积），并**明确声明**所用的独立性假设；或只报告**有界量**（C3）。
- 报告纪律：**不宣称「composite 的 credal 宽度 = 分量宽度的乘积」**。

**Round 3 删除的一句（`UNSUPPORTED`；`review-r2 E-C6` / `H-D4`）**：原文在这里写「**且松的程度依赖一个未被声明的独立性假设**」。

- **被撤回的**是这个**因果归因**，不是成本结论。`10.1145/3704890` 陈述的是「凸分布幂集 monad **非交换** ⇒ 组合 **not compositional**；改用 graded monad 得到**更紧**的界」。它**没有**说「松的程度随独立性假设变化」。
- **保留为 `[MODEL_HYPOTHESIS]` 的只有**：上面的「正确做法」一条——即本文件**自己**主张组合前必须显式声明独立性假设。这是建模纪律，**不**是被引用来源的结论。
- **待补**：若要把「松的程度 ↔ 独立性假设」写成一条有来源的结论，需要一条 imprecise-probability 文献明确作此陈述。**本 child 未打开这样的来源**（`NOT_OPENED`）⇒ 该归因 `HOLD_FOR_EVIDENCE`，在补上之前**不得**被引用。
- **成本结论照旧有效**：R4（credal set 作为默认存储层）**延后**（§9.2 `D1`），理由是组合不平凡 + 朴素组合系统性过松。

---

## 5. 可检验不变量

**Round 3 更正（`review-r2 R-E9` / `E-C12` `VERIFIED` / `H-F12`）**：本节原文开篇写「以下 **15** 条」，而 §5.1 给 I1–I15、§5.2 给 I16–**I19**，合计 **19** 条（§13 也写 19）。**15 是错的，正确数字是 19。**

**以下是 19 条候选可检验不变量**。它们现在是命题，**不是**已验证的性质（§10 非主张 10）。

### 5.0 Round 3：逐条可执行性分类（取代原文「9 条现在就能检查」的计数）

**原计数已被否决（`review-r2 E-C11` / `H-F14`：`REJECT`）**。原文 §5.3 写「I1、I2、I3、I4、I6、I7、I12、I14、I15 —— 这 **9** 条不需要任何新数学……**建议优先落这 9 条**」。**该 9 条计数不成立**，因为其中：

- `I14` 的判据含一个**本报告自己拒绝给值的阈值 `θ`**（§11-2 明确说「`evidence_mass` 的度量与阈值未冻结」「本报告不推荐具体采用任何一个」）⇒ 判据不可求值；
- `I17` 的判据含**未定义的 coverage 阈值**（§5.2 自己写「未定义阈值（`UNKNOWN`）」）⇒ 判据不可求值；
- `I18` 需要一个成本模型，而项目**明确不冻结**分数 / 成本函数（`CURRENT_ARCHITECTURE.md` §11；`AGENTS.md` representation-first invariant 1/2）⇒ 存在性测试无定义域；
- `I19` **空过**：「报告置信度的分布尖锐度不得是自由参数；须随输入稀疏度变化」——**任何非恒定函数都满足**「随输入变化」，所以它不排除任何实现，是**空判据**（`VACUOUS`）。FM-07 的论证（monofact ⇒ 校准与正确率不可兼得）**有内容**，但它**不能**由 I19 这条判据机械检验。

**Round 3 的分类**（四档）：

| 档 | 定义 | 条目 |
| --- | --- | --- |
| **E1 · 现在可执行** | 判据完全在本文件内闭合（无未赋参数、无未定义阈值、无外部数据、无待登记的表）；只需 schema 约束 / 属性测试 / 输出纪律 | `I1`、`I2`、`I3`、`I4`、`I6`、`I7`、`I8`、`I12`、`I15` —— **9 条** |
| **E2 · 结构上可执行，但缺一份待建的表** | 判据闭合，但需要一份**尚不存在**的登记物；该登记物是**一条已裁定的落地项**，不是研究问题 | `I9`（需逐坐标依赖表）、`I11`（需 `history_id` DAG 已成形）、`I13`（需 `structurally_unobservable` / `censored` 已被登记——依赖 **C-P13** 可观察性登记表） |
| **E3 · 当前不可执行（缺数据 / 缺冻结决策）** | 缺 held-out 数据，或缺一个项目已明确不冻结的决策 | `I16`（无 held-out set）、`I17`（无 coverage 阈值）、`I18`（无成本模型） |
| **E4 · 判据有缺陷，不可作为判据** | 要么**空过**（任何实现都满足），要么**可被反例击穿** | `I19`（**空过**：`VACUOUS`）、`I10`（**可被击穿**，见下） |

**`I10` 的击穿（Round 3 记录，源自 review-r2 的要求）**：`I10` 断言「证据集 `E ⊆ E′` ⟹ 每个坐标的宽度 `width(post(E′)) ≤ width(post(E))`」。这不是一个**无条件的**单调性定理：它可被一个**博弈式反例**击穿——若后验是**多峰**的，且新证据消掉一个峰，则新后验的**点估计宽度**（例如 `max − min`）可以**变宽**而同时**方差**变小；反过来，若实现把 `width` 定义为**多峰分量的包络**，则「更多证据」可能迫使实现承认一个此前被忽略的峰。**更根本的问题**：`I10` 的 `width` 是什么**没有定义**——`max − min`、方差、`22`-coherence 的 `[lower, upper]`、credal 集的直径，四者对 `I10` 的真值不同。⇒ **`I10` 从「可立即检查」降为 `HOLD_FOR_DEFINITION`**：它需要先**冻结 `width` 的定义**，而那是一个 Architect 决策（`AGENTS.md`：`Do not label an unvalidated … normalization rule as scientifically established`）。

**因此，Round 3 的净计数**：

- `E1`（现在可执行）= **9 条**，但**清单与原文不同**（去 `I14`、加 `I8`）；
- `E2` = **3 条**（`I9`、`I11`、`I13`），全部收敛到**同一个**前置：待建的登记物（含 **C-P13** 可观察性登记表）；
- `E3` = **3 条**（`I16`、`I17`、`I18`）；
- `E4` = **2 条**（`I19` 空过、`I10` 待定义）；
- 合计 9 + 3 + 3 + 2 = **17** ≠ 19 ⇒ 剩余 **2** 条（`I5`、`I14`）单列如下。

**两条例外，诚实列出而不是硬塞进四档**：

- `I5`（`private_to_partner` 坐标不得被 S 侧观测 refinement）**在结构上可执行**（角色置换测试），但它的**方向依赖 canonical 的 `Role` 语义**（`CURRENT_ARCHITECTURE.md:96`：`Role` 是 query lens，不是世界状态），而 §1.1 已指出本文件原用 `reporter_role` 与之重名 ⇒ 归为 **`E2 · 需先解决命名与层级澄清`**。
- `I14`（`evidence_mass < θ` 时禁止点 readout）**在形式上可执行**（合成稀疏状态上的属性测试），但**没有 `θ` 就没有判据**；本报告**坚持不给 `θ`**（§11-2）⇒ 归为 **`E3 · 缺一个本报告拒绝冻结的决策`**。注意 §5.4 与 FM-07 给出的是**不受 `θ` 约束**的版本（`MAPPING_FAILURE` / `REFUSE` 作为合法终态输出），**那**才是可执行的方向。

### 5.1 结构与传播类

| ID | 不变量 | 检查方式 | 预期反例 |
| --- | --- | --- | --- |
| **I1** | **Unknown 吸收**：`v_k = ⊥` ⟹ composite 在 `k` 上为 `⊥`；任何 readout 不得对 `k` 输出有限标量 | schema 约束 + 单元测试 | 平均/求和把 `⊥` 当 0 处理 |
| **I2** | **底元素上不做算术**：`f(⊥_T)` 不得是数；全函数必须返回 `⊥` 或显式标记值 | 属性测试：对每个 `T` 的每个算子 | `⊥ + 0 = ⊥` 被实现成 `0` |
| **I3** | **有界读出的像集报告**：任何对 `⊥` 状态成立的 readout 必须是 `g ∈ g(K)`，不得是 `g = v` | 输出 schema 检查 | 输出单值 |
| **I4** | **tag 闭包**：tag 取值是已登记的有限枚举；复合后 tag 只增不减（取集合并）；**新 tag 不得未经登记出现** | 枚举 diff（CI） | tag 数量随 case 数增长 → ontology 蠕变 |
| **I5** | **tag 不可跨角色泄漏**：`private_to_partner` 坐标不得被 S 侧的观测 refinement | 角色置换测试：交换 `S`/`O` 后 `private_to_partner` 应仍在 partner 侧 | S 侧报告把 J 侧的私域 Unknown「解决」了 |
| **I6** | **矛盾 ≠ 未知**：相反来源必须产出 `B`，且**与来源顺序无关** | 顺序置换测试：打乱来源顺序，`B` 不变 | 按顺序「后者覆盖前者」→ 变 `T` 或 `F` |
| **I7** | **聚合顺序无关**：composite 是证据**集合**的函数，不是摄入顺序的函数（lattice join 的交换律） | 打乱证据顺序重跑，比对 | 「最后一条说了算」 |
| **I8** | **重复证据幂等**：同一事实摄入两次，状态不变；同事实的第二来源应 **refine** 而非 **overwrite** | 幂等测试 | 第二来源覆盖第一来源 |
| **I9** | **逐坐标单调（C5）**：更新 `j` 不改变 `i`，除非有已登记的 `∂F_i/∂z_j ≠ 0` | 逐坐标消融测试 | 隐式耦合无处登记 |
| **I10** | **refinement 单调**：证据集 `E ⊆ E′` ⟹ 每个坐标的宽度 `width(post(E′)) ≤ width(post(E))` | 随机抽 `E ⊆ E′` 反复测 | 丢证据反而变宽（forgetting 非单调） |
| **I11** | **时间 refinement 单调**：`history_id` 的 DAG 中，refined 视图不得作为 refined 视图的 sibling 出现 | DAG 不变量检查 | 旧 lineage 被新证据改写 |
| **I12** | **readout 不回写**：`readout : State → Readout` 的像**不是**状态更新路径的输入 | 依赖图 / 静态检查 | 78/100 型结果被写回 `ModelState` |
| **I13** | **不可约性诚实**：对被标为 `structurally_unobservable` / `censored` 的坐标，「增加证据会确定它」**不得**作为默认承诺出现在任何输出里 | 字符串/模板审计 | 报告暗示「再问几个问题就能确定」 |
| **I14** | **prior 支配标记**：`evidence_mass < θ` 时禁止点 readout | 属性测试（生成合成稀疏状态） | 零观测坐标输出点值 |
| **I15** | **多峰不取均值**：坐标后验非单峰时，禁止输出点 readout | 在合成双峰后验上跑 readout | 报告双峰后验的均值（无指称） |

### 5.2 评测类（需要 held-out 数据，当前无法执行）

| ID | 不变量 | 检查方式 | 现状 |
| --- | --- | --- | --- |
| **I16** | **校准**：报告的置信度必须随留出集上的经验准确率单调；且校准曲线不得劣于常数先验基线 | reliability diagram + 严格 proper scoring rule 分解（Gneiting & Raftery 2007, JASA 102(477):359–378, DOI `10.1198/016214506000001437`，`CITED_METADATA`，**未读正文**） | **无 held-out Case Bank set，`UNKNOWN`** |
| **I17** | **coverage 显式**：每个 Case Bank item 必须报告非 `⊥` 坐标比例；coverage 低于登记阈值时不得作完备性主张 | 报告 schema | 未定义阈值（`UNKNOWN`） |
| **I18** | **REFUSE 可达性**：必须存在一个状态（`⊥` 覆盖率达某水平）使最优动作是 `REFUSE` | 存在性测试（依据 Franc et al. 2021 的选择函数） | 未实现 |
| **I19** | **confidence-尖锐度非任意**：报告置信度的分布尖锐度不得是自由参数；须随输入稀疏度变化 | 分布对比 | 尚无实现 |

### 5.3 哪些是「便宜且高价值」的

**Round 3：本小节整体重写，原「9 条」计数被否决。** 判定依据见 §5.0 的逐条分类表；这里只给**建议的落地顺序**，并把每一条的前置条件写明。

**第一批（E1，9 条，现在可执行）**——判据完全在本文件内闭合，只需要 schema 约束、属性测试与输出纪律：

```text
I1  Unknown 吸收            I2  底元素上不做算术
I3  有界读出的像集报告       I4  tag 闭包
I6  矛盾 ≠ 未知            I7  聚合顺序无关
I8  重复证据幂等            I12 readout 不回写
I15 多峰不取均值
```

**与原清单的差异（Round 3）**：

- **移出** `I14`（含未赋值的 `θ`）、**移入** `I8`（幂等性判据闭合，只需幂等测试）。
- 保留 `I1`、`I2`、`I3`、`I4`、`I6`、`I7`、`I12`、`I15` 八条不变。

**第二批（E2，3 条 + 1 条）——只卡在同一件事上**：

- `I9`（逐坐标单调）、`I11`（时间 refinement 单调）、`I13`（不可约性诚实）、`I5`（tag 不跨角色泄漏）
- **共同前置**：① §3.1 的 `⊑` 形式定义 + 逐坐标依赖表；② **C-P13** 可观察性 / 锚点登记表（`I13` 需要知道哪些坐标是 `structurally_unobservable` / `censored`）；③ `Role` 命名与层级的澄清（§1.1）。
- **这三类前置不是研究问题**：`⊑` 的定义与依赖表是**登记/决策**，可观察性登记表已被 Architect 裁定为**测量元数据**（C-P13），**不是本体扩张**。

**第三批（E3，3 条）——缺数据或缺冻结决策**：`I16`（需 held-out Case Bank set）、`I17`（需 coverage 阈值）、`I18`（需成本模型；项目明确不冻结）、`I14`（需 `θ`；本报告拒绝给）。

**不进入任何清单（E4，2 条）**：`I19`（**空过**，`VACUOUS`）、`I10`（**需先冻结 `width` 定义**，`HOLD_FOR_DEFINITION`）。**这一档的处置不是「以后再说」，而是「判据本身有缺陷，必须重写后才能成为判据」**——按裁决 X-12，这**不是 blocker**（负面结果不是阻塞项），但也不得被引用为「可检验」。

**本节不给「优先落这 N 条」的措辞。** 原文写的「**建议优先落这 9 条**」暗示了一个已就绪的执行序列；Round 3 判定：E1 那 9 条**判据**已就绪，但**是否现在落地**属于 Architect 的排程决定，且它们的落地形态（schema 约束 vs 报告纪律 vs 单元测试）各不相同，不能作为一个整体被"落"。见 §5.4 的 `RECLASSIFY_AS_METHOD_LIMIT`。

### 5.4 一句可以直接引用的替代文本（Round 3：`RECLASSIFY_AS_METHOD_LIMIT`）

**分类（原「可以安全落地」已改标）**：**`RECLASSIFY_AS_METHOD_LIMIT`**。

- **落点是**一个**研究纪律 / 文档措辞段**（形如 `STAGE_SUMMARY_2026-09-07.md:162` 那一行所在的**研究纪律**上下文），**不是** schema 变更，**不是**构念变更，**不是**状态空间变更。
- **它不引入任何新字段、不改任何值类、不改任何算子。** 它唯一做的事是：把一条**过强的不变性表述**换成一条**可辩护的**表述。
- **因此它不构成一个「canonical 构念变更提案」**，不应进入任何以「构念 / schema 变更为单位」的 register（例如 Track R3-C 的 Gate 协议），否则会把一条措辞修订伪装成架构变更。
- **本报告不写 canonical。** 提交 Architect 审阅（§9.1 #12）是本文件能做的全部。

`[AI_RECOMMENDATION]`（**不改 canonical，仅建议措辞**）：

```text
Computable != Certain
```

建议扩为：

```text
Missingness removes point identification.
It preserves:  (a) non-trivial bounds;  (b) monotone partial functionals.
It does NOT preserve:  point readouts;  comparisons;  transition-law identification.
Unknown / Disputed / Not-addressable are legal terminal outputs, not failures.
```

**Round 3 强制的限定语（承重；`review-r2 E-C8`）**：上面这段文本**只对 `no_evidence` 一支**是无条件成立的。对 `refused` / `refused-to-answer`（MNAR）一支，**必须**先说「应答过程不是 missing-at-random」，再谈「保留有界量」——否则它会**静默把 MNAR 重写为 MAR**。因此建议把最后一行改成条件式：

```text
For no_evidence missingness:  bounds and monotone partial functionals survive;
                              point readouts, comparisons and
                              transition-law identification do not.
For refused-to-answer (MNAR): the correct type is a set WIDER than the prior,
                              not an imprecise prior; do not impute.
Unknown / Disputed / Not-addressable are legal terminal outputs, not failures.
```

支撑 `(a)` 的严格依据：Pelessoni & Vicig (2022)，arXiv:2211.01503 —— 概率不等式在 imprecise 知识下仍成立（`CITED_PRIMARY`）。**该定理覆盖 `no_evidence`；它不自动覆盖 `refused` 一支**（理由同 §2.2 的 Round 3 段落）。
支撑后半段的依据见 §6。

**Kuhn's dogmatism paradox（Round 3 新增登记）**：review-r2 `E-C25` 提到 mission 的措辞「Kuhn's 'dogmatism paradox'」。本文件**未**处理该材料；`08b` §3.9 已独立核实规范对象是 **Kripke–Harman dogmatism paradox**（经 Gilbert Harman，不是经 Kuhn 的教条论题）。⇒ **状态 `PLAUSIBLE`**，作为**开放问题**路由给 Track R3-F / `NEXT_EXPERIMENTS`，**不在本文件内主张任何与之相关的 K4 结论**。

---

## 6. 「缺失降低确定性但不影响可计算性」失效的具体模式

以下 8 条，每条给出**为什么该句在这一点上为假**、**证据**、**LHRM 内的具体触发场景**。

### FM-01 — 结构性空单元：不是小样本，是**永远没有样本**

`[ESTABLISHED]` 若缺失指示 `M` 是取值的确定函数（`M = 1 ⟺ X = 1`，例如「只对自报使用某 App 的人询问其使用行为」），则分层 `X = 1` 的观测**永远为空**。

- 这不是低数据，是**条件空单元**。加大 N 无用。
- Tennenholtz (2023, arXiv:2306.01157) 给出了这类不可约性的一个干净陈述：**delphic uncertainty "cannot be diminished, even in deterministic environments and infinite data"**（`CITED_PRIMARY`）。
- **`Unknown → prior` 在此仅在空洞意义上成立**：该分层的先验**就是**目标量本身，所以推断是循环的、vacuous 的。
- **LHRM 触发场景**：任何「只有在 X 已经发生时才被问到」的坐标。典型：性行为史（Kupek 1998 在**国家级性调查**中实证研究了 item nonresponse 的系统性决定因素，`CITED_METADATA`，**未读正文**）；「吵架次数」（只在吵架时才记录）；「是否已分手」（只在分手样本中采集）。

### FM-02 — 核心坐标本身 latent 且无 gold standard：点 readout 是**无指称**，不只是「不精确」

- `[ESTABLISHED]` Raykar et al. (2010, JMLR 11(43):1297–1322)：多标注者 + **无 gold standard** 时，联合估计真标签与标注者混淆矩阵存在 "chicken-and-egg problem"，真标签估计**只相对于一个测量模型**成立（`CITED_PRIMARY`，读到引言）。
- **对 LHRM**（`[MODEL_HYPOTHESIS]`，但类型上很硬）：`Trust(A→B)`、`Dedication(A→B)`、`SexualDesire(A→B)` **没有 gold standard**。可能的锚点只有：法院/官方裁定事实、强制性行为痕迹、已验证量表。**在叙事材料上三者皆无。**
- 后果：这些坐标的「后验」在形式上必须是**不可辨识的分布族**，报告点值不是精度不足，而是**指称缺失**。
- **这条目前不在任何 canonical 文档里，是本报告最重要的结构性发现。**

### FM-03 — `disputed` 与 `unmeasured` 不可比

- **反例（不需要任何数据即可判定）：**
  - Case A：两份来源对 `Trust(A→B)` 给出相反结论（法院文书 vs 私人聊天记录）→ 值 `B`。
  - Case B：无人报告过 `Trust(A→B)` → 值 `N`。
  - 任何把两者映射到同一 confidence 值的表示，都在做一次**不可比 → 可比**的压缩。该压缩**不是** refinement 映射。
- 依据：Belnap 1977 与 Mundhenk et al. 给出 `{T,F,B,N}` 上的两个序。
- **Round 3 精确化（这一条现在有了正确的形式依据）**：本反例成立**不是**因为「`N` 与 `B` 在信息序上不可比」——**它们在信息序上是可比的**（`N ⊑_a B`）。它成立是因为 `N` 与 `B` 在**真值序**上**不可比**：`⊑_t` 上 `F` 是底、`T` 是顶，`N` 与 `B` 是两翼；`N` 真值上"什么也没说"，`B` 真值上"真且假"，这两者**没有共同的严格真值位置**。任何把二者压到一个数上的 confidence 轴，就是要求一个标量同时读出 `⊑_a` 的高度与 `⊑_t` 的高度，而这两个高度在 `N`/`B` 上给出相反的读数。详见 §2.3.1。
- **可作为 Case Bank 条目立即落地。**

### FM-04 — 填补会改变 estimand

- `[ESTABLISHED]` White & Carlin (2010, *Statistics in Medicine* 29:2920–2931, DOI `10.1002/sim.3944`)：当缺失独立于给定协变量的结果时，**complete-case 几乎无偏，而 multiple imputation 偏离零假设**；而在 MAR 下 complete-case 偏向零假设（`CITED_PRIMARY`，读到摘要）。
  原文：*"the choice of method should not be based on comparison of standard errors."*
- 补充：Seaman, Bartlett & White (2012, *BMC Med Res Methodol* 12:46, DOI `10.1186/1471-2288-12-46`)：MAR 下 JAV 可有偏，logistic 情形 "JAV's performance was **sometimes very poor**"（`CITED_PRIMARY`）。
- **后果**：「用先验补 Unknown」不是「加点噪声」，而是**改变估计目标**。可计算的东西取决于你静默采纳的机制假设。**这就是「影响可计算性」的直接反例。**
- **可用工具**：White & Carlin 提出 **FICO** = "the fraction of incomplete cases among the observed values of a covariate"——这是一个现成的、可直接实现为 LHRM `evidence_mass` 候选的指标（`[AI_RECOMMENDATION]`，但**本报告不推荐具体采用**，只指出它存在）。

### FM-05 — 最优动作可能是「不算」

- `[ESTABLISHED]` Franc, Prusa & Voracek（**Round 3 已修书目与术语，见下**）：三个 **rejection model** 共享同一最优策略。
  - 逐字（摘要）："We prove that despite their different formulations **the three rejection models** lead to the same prediction strategy: **the Bayes classifier endowed with a randomized Bayes selection function**."（`CITED_PRIMARY`）
  - 逐字（摘要，三个模型的名字）："The classical **cost-based** model of a reject option classifier requires the rejection cost to be defined explicitly. The alternative **bounded-improvement** model and the **bounded-abstention** model avoid the notion of the reject cost."
- **后果**：在成本敏感的读出下，稀疏 dyad 的正确输出常常是「状态未定，给出界」。主张「可计算性不受影响」等于否认「拒答」属于正确的输出类。
- **Round 3 的强结论（承重，`review-r2 H-D5` / `E-C9`）**：**在成本敏感的 readout 下，`REFUSE` 是一个一等输出。** 这不是「可选附加项」：原文说选择函数是 "endowed with"（**被赋予**）给最优策略的，即三个形式化不同的模型最终都**退化为同一个** Bayes 分类器 + 一个**随机化**选择函数。任何声称「我可以只要分类器、拒答另说」的实现都在**重述**该定理。
- **迁移到 LHRM 的强度（Round 3 降级为 `PLAUSIBLE`）**：上面**定理**是 `VERIFIED`；「因此 LHRM 的 readout 应当有 `REFUSE`」是**迁移**，判 `PLAUSIBLE`。本文件**不主张**它是定理的直接应用。
- **限制（自我约束）**：Salez et al. (NeurIPS 2021) 明确警告拒答可能成为不公平来源，且"**it should not serve as an excuse not to collect representative data**"（`CITED_PRIMARY`）。→ 「大量输出 Unknown」**不是**一个好的分数，必须同时报告 coverage 趋势（→ I17，而 I17 当前 `E3` 不可执行，见 §5.0）。

**Round 3 的书目与术语更正（本 child 定点打开核实，2026-09-28）**：

| 项 | 原文本（`SUPERSEDED_BY_REPAIR`） | 更正后 | 依据 |
| --- | --- | --- | --- |
| 出版年 | `Franc, V., Prusa, D., & Voracek, V. (2021). … JMLR, 24, 21-0048.` | **JMLR 版本记录是 2023**：`Franc, V., Prusa, D., & Voracek, V. (2023). *Optimal Strategies for Reject Option Classifiers.* Journal of Machine Learning Research, 24(11), 1–49. `https://jmlr.org/papers/v24/21-0048.html` | JMLR v24 目录页逐字："Vojtech Franc, Daniel Prusa, Vaclav Voracek ; **24(11):1−49, 2023**"；页脚 "© JMLR 2023" |
| 预印本 | （未著录） | **arXiv:2101.12523**（v1 提交 2021-01-29） | arXiv abs 页逐字："[Submitted on 29 Jan 2021] … V. Franc, D. Prusa, V. Voracek" |
| 第三个模型名 | `bounded-coverage` | **`bounded-abstention`** | arXiv v1 摘要用 "bounded-coverage"（"We coin a symmetric definition, the bounded-coverage model"）；**JMLR 正式版改名为 bounded-abstention**。本文件原先引的是 JMLR 版却用预印本版的名 ⇒ **术语与所引版本不一致** |
| "reject model" | "三个 reject model" | **"三个 rejection model"** | 两个版本的摘要均用 "the three **rejection** models" |
| `randomized Bayes selection function` | 保留 | 保留（逐字正确） | 两个版本摘要均为 "a randomized Bayes selection function" |

**因此**：本文件引用的**定理内容与逐字引文不变**（`review-r2 E-C9` 判 "定理 + 逐字引文 `VERIFIED`"），**改的只是书目与术语**。本 child 未读 JMLR 正文 §2.4（本轮只核到官方摘要页 + 目录页），故原先 "读到摘要与 §2.4" 的自陈**降级为「读到官方摘要全文」**。

### FM-06 — 快照 ≠ 轨迹：没有观测模型就没有动力学

- `[ESTABLISHED]` **Ghosh, Rahme, Kumar, Zhang, Adams & Levine**（NeurIPS 2021，*Why Generalization in RL is Difficult: Epistemic POMDPs and Implicit Partial Observability*，arXiv:2107.06277）："even in fully-observed domains, the agent's epistemic uncertainty renders the environment **implicitly partially observed** at test-time"；不显式处理它的方法"can be **arbitrarily sub-optimal** for test-time generalization in theory and in practice"（`CITED_PRIMARY`）。
  - **Round 3 书目更正（`review-r2 E-C10`：`REJECT` 对书目条目，内容 `ACCEPT`）**：本文件原参考文献 [6] 的作者表写作 `Rajaraman, D., Han, T., Yang, P., Ramchandran, K., Van Dyke, D., Peng, X., & Levine, S. (2021)`。**这是错的。** 本 child 于 2026-09-28 定点核实（OpenAlex + arXiv abs 页，两处独立）：
    - arXiv abs 页逐字：**"Authors: Dibya Ghosh, Jad Rahme, Aviral Kumar, Amy Zhang, Ryan P. Adams, Sergey Levine"**，`[Submitted on 13 Jul 2021]`，DOI `10.48550/arXiv.2107.06277`，Comments: "First two authors contributed equally"。
    - OpenAlex `W3181634442` / `W4287078276` 的 `authorships` 与之一致。
    - 结论：**该文与 *Epistemic POMDPs* 主题相符，但作者是 Ghosh 等，不是 Rajaraman 等。** 原作者表**不得**被引用。**内容层不变**（本文件引的那两句确为该文内容）。
- `[ESTABLISHED]` Tennenholtz, Hallak, Dalal, Mannor, Chechik & Shalit (NeurIPS 2021 DeepRL Workshop)：缺失协变量存在任意分布漂移时，模仿学习有 **possibility/impossibility 结果**（`CITED_PRIMARY`）。
- **对 LHRM**（`[MODEL_HYPOTHESIS]`）：`X_(t+1) = F(...)` 是一个**条件**陈述。**在稀疏事件序列上无法从一次快照区分「没变」与「变了但没被观测到」。** 这需要显式的观测模型（哪些事件会留下痕迹、哪些不会），而项目目前没有这个层。
- **诚实标注**：RL 设定到关系设定的迁移是**类比**。网络动力学里「homophily vs. contagion 需要观测过程才能区分」这一对应结论我**未核实**（Shalizi & Thomas 2011 未获取，见 §11），因此**不写入本报告**。

### FM-07 — 校准在稀疏输入下是**被定理强制的取舍**

- `[ESTABLISHED]` Kalai & Vempala (*arXiv:2311.14648*; STOC 2024, DOI `10.1145/3618260.3649777`)：对**真实性无法从训练数据判定的任意外部事实**，满足其语义校准条件的生成器**必须**以至少

  ```
  Hallucination rate  ≥  MF̂  −  Miscalibration  −  300·|Facts|/|Possible hallucinations|  −  7/√n
  ```

  的速率产生幻觉，**即使训练数据完美**。`MF̂` 是 Good–Turing **MonoFacts** 估计，即训练集中**恰好出现一次**的事实所占比例（`CITED_PRIMARY`，读到 abstract + v3 PDF 引言与 Cor 1）。

- **对 LHRM 的结构性后果**（`[MODEL_HYPOTHESIS]`，强度 `moderate`）：LHRM 的核心输出是 **per-dyad 的一次性事实**。这在结构上就是 **monofact**。因此：
  - 若 per-dyad 置信度**完全校准** ⟹ **必须有正比例的一部分是错的**；
  - 若它们**全对** ⟹ 置信度**系统性过度自信**。
  - **「稀疏输入 + 高置信」不是可修的 bug，而是必须被显式暴露的强制取舍。**
  - **Round 3 更正这一条与 I19 的挂钩**：本文件原写「报告置信度的**尖锐度不能是自由参数**（→ I19）」。**该挂钩已删除**：`I19` 被 review-r2 判为**空判据**（任何非恒定函数都满足，见 §5.0 的 E4 档），所以本段论证**不能**挂在 `I19` 上。本文件**不**从本定理推出任何可机械检验的不变量。**这一段是一个结构性论证（`[MODEL_HYPOTHESIS]`，强度 `moderate`），不是一个判据。**
- **限制**：该文证明的是 next-token 生成器 + monofact 事实分布。搬到 LHRM 是**类比 + 结构性论证**，不是定理的直接应用。

### FM-08 — 拒答 ≠ 无内部状态

- `[ESTABLISHED]` Krosnick, Presser & Tan（*The Impact of "No Opinion" Response Options on Data Quality*，`https://gspp.berkeley.edu/archived/files/research/pdf/Krosnick_et_al..pdf`，`CITED_PRIMARY`，**完整书目 `PARTIAL_BIB`**）：
  - 拒答主因是 **satisficing**（疲劳、题目靠后、低努力、低教育），不是真的「无意见」；Study 3 中「reported effort was **negatively** related to no-opinion reporting, suggesting that choosing a no opinion response option was more likely the result of **satisficing** than of optimizing」。
  - 给出 "don't know" 选项**减少**了事实题的实质回答数，但**未改变**重测信度（Foe et al. 1988，转引自该文）。
- **后果（对 `Unknown → prior` 的定点反例）**：对 tag = `refused`，**不得**用先验插补。正确类型是**比先验更宽的集合**，理由是应答过程本身不是 missing-at-random——先验反映的是「愿意回答的人」的分布，不是「这些人」或「那些人」的分布。

### FM-09（附加）— 方向性 invariant 的具体威胁：partial pooling 人为制造 mutuality

**Round 3 分类（`review-r2 E-C15`）：`ACCEPT_AS_PROPOSAL` —— 一条**实现约定 + readout 要求**，`proposal only`。本文件不实施、不写 canonical、不主张它已被验证。**

- `CURRENT_ARCHITECTURE.md:130-132` 要求 `SexualDesire(A→B) != SexualDesire(B→A)` 等三条。
- 若用**单一**人口超参数对 `Z[k,i,j,t]` 做向心收缩，`i→j` 与 `j→i` 共享同一收缩中心 → **非对称性被系统性地压向对称**。
- **这是本次审计发现的唯一一条「统计方法与 canonical 架构 invariant 直接冲突」的机制，项目中没有任何记载。**
- **Round 3 的处置分三部分（缺一不可）**：
  1. **实现约定（如果采用 partial pooling）**：对 `i→j` / `j→i` 使用**分离的超参数或分离的随机效应**，或用 `(1,−1)` contrast 建模；**不得**让两个方向共享同一收缩中心。
  2. **readout 要求**：把「**收缩导致的非对称衰减量**」作为**一等 readout** 显式报告。**只报均值不报衰减量，就把架构 invariant 的违反藏进了汇总统计里。**
  3. **顺序依赖**：本条**只在 partial pooling 被采用时**才激活。项目当前**未冻结**是否使用 partial pooling（`AGENTS.md`：`A coordinate may be …`；`CURRENT_ARCHITECTURE.md` §11 不冻结统一权重表）⇒ 因此本条是**条件义务**，不是**当前义务**。
- **`PLAUSIBLE`，不是定理。** 收缩把非对称性往对称方向推，是一个**方向性明确但幅度未量化**的论证；本文件**不主张**它对任何给定 `N` 或 `k` 的具体效应量。
- **与本文件 §5.0 的接口**：`I9`（逐坐标单调）**不覆盖**本条——`I9` 讲的是「更新 `j` 是否改变 `i`」的结构依赖，而本条讲的是**估计器层面的收缩对两个方向的对称化作用**。两者是不同层的风险，**不要**把本条算作 `I9` 的一个实例。

---

## 7. 稀疏 per-dyad 数据的 partial pooling 与不可辨识性

### 7.1 pooling 帮什么

`[ESTABLISHED]` 稀疏 N 下 factor loading 高度不稳定。Hirschfeld et al.（*J. Research in Personality*，`https://www.uni-muenster.de/OWMS/uploads/drafts_thielsch/pdf/Hirschfeld_et_al_2014_JRP.pdf`，`CITED_PRIMARY` 摘要；**完整作者表 / 卷页未核**）：

> "primary factor loadings are highly variable in smaller samples (n < 500) and **some primary loadings are not stable with 10,000 participants**. … **Most studies will not have adequate sample size** to yield stable loading patterns."

**这条对 LHRM 的含义比它看起来更重：加大 N **不能**修复**测量层**的稀疏。** 参数估计的方差与测量结构的稳定性是两个不同的问题。

### 7.2 pooling 不帮什么

`[ESTABLISHED]` **Ghosh, Rahme, Kumar, Zhang, Adams & Levine**（2021，arXiv:2107.06277；见 §12 [6] 的 Round 3 书目更正）：即使观测完全可得，有限训练上下文也会让测试时环境变成**隐式部分可观测**；不显式处理的方法"can be **arbitrarily sub-optimal**"。

`[ESTABLISHED]` Tennenholtz (2023)：delphic uncertainty 在确定性环境 + 无限数据下**仍不下降**。

**推论**（`[MODEL_HYPOTHESIS]`）：

> **partial pooling 降低的是参数估计的方差，不是可辨识性。**
> 若某 dyad 落在一个人口先验覆盖不到的分层里，pooling 只会把错误**传播到更多 dyad**。
> 因此 partial pooling 必须 **按分层**做（relationship type × 阶段 × Environment），并且必须把「该 dyad 的 posterior 有多少由 pooling 决定」作为**一等输出**（即 `evidence_mass` / shrinkage 幅度）。

### 7.3 先验的质量在稀疏区恰好最差

`[ESTABLISHED]` Gu & Koenker (2015, *International Statistical Review*，`http://www.econ.uiuc.edu/~roger/research/ebayes/isrProbRob.pdf`，`CITED_PRIMARY`）：Robbins (1951) 的 compound decision 设定下，`n = 20` 时方法矩估计在 `p → 1/2` 附近有 "modest disadvantage"；换 beta prior 收缩后 "deliver better performance than the MoM procedure **while sacrificing some of their advantage when p is near 0 or 1**"。

`[ESTABLISHED]` 另经转述（Berger 1985, *Statistical Decision Theory*，转引自 *Robustifying Empirical Bayes*，`PARTIAL_BIB`）：

> "A natural objection to many empirical Bayes procedures is that they place **unjustified reliance on an initial prior**. While such procedures may still perform well with respect to ensemble risk, they may also **fail spectacularly for some subpopulations or individuals**."
>
> Berger (1985): "it is very difficult to determine such δ\*; furthermore, this 'optimal' δ\* is **usually extremely messy and difficult to work with**."

**这条的含义**：稀疏区的先验既无数据约束、又在数学上难处理。**「Unknown → prior」在稀疏区的收益与代价都集中在这里**——不是一个可以靠调参解决的问题，而是**设计选择**。

---

## 8. 稳健读出与稳健决策

### 8.1 现在就能用的：有界量

`[ESTABLISHED]` Pelessoni & Vicig (2022)：Markov / Cantelli / Jensen 型界在 imprecise 知识下仍成立（`22`-coherence 即可），因为这些不等式**不依赖精确评估**。

**Round 3 强制的限定语（承重；`review-r2 E-C8`）**：上面这一定理的前提是**存在非平凡的 imprecise 先验**。因此下面这张表**只对 `no_evidence` 一支**（以及任何已确证为 MAR / MCAR 的机制）是无条件可用的。对 `refused` / `refused-to-answer`（MNAR，FM-08）、`censored`（按构造 MNAR，FM-01）、`withheld_by_actor`（内生 MNAR，§1 表）这四支，**正确类型是「比先验更宽的集合」或「结构性空」，而不是一个 imprecise 先验**；把后者套进 `22`-coherence 会把 `MNAR` 静默重写为 `MAR`。**用法**：先按 §1 的 tag 分类分型，再决定能不能用这张表。

**因此，以下 readout 在 `⊥` 状态上合法且有严格依据（条件：上述分型已通过）**：

```text
coverage(i,j)                  = fraction of coordinates with value ≠ ⊥
width_k                        = upper_k − lower_k
P(X ≥ c) ≥ 1 − μ/c             若只有 [μ, ·] 与上界信息
count_k(tag) ≥ / ≤             某 tag 的坐标数
lower / upper of any monotone g
```

**Round 3 对 `width_k` 的一处收窄**：`width_k = upper_k − lower_k` 这一行在 §8.1 里是**定义式**的（读 `⊑_a` 上的高度差），但 §5.0 的 `I10` 之所以不可执行，正是因为 `I10` 里的 `width` **没有**这样定义。若 `I10` 采用本节的定义（`upper_k − lower_k`），它在**单峰**后验上是单调的；但在**多峰**后验上（`I15` 承认其存在），`upper_k − lower_k` 会被一个远离主体质量的分量支配，**从而在新证据消掉次峰时反而变宽**。⇒ 报告 `width_k` 时**必须**同时报告分量的个数与位置（`I15`）。这是本节与 §5.0 之间的**显式接口**，原文件两处不一致。

### 8.2 延后的：credal 决策

`[ESTABLISHED]` 成本依据：

- credal set 作为**存储层**会引入**可组合性**问题，且朴素组合**系统性地过松**（Liell-Cock & Staton 2025, POPL, DOI `10.1145/3704890`）。**Round 3**：本条只主张「不 compositional / 系统性过松」；**不**主张「松的程度依赖某个未声明的独立性假设」（`UNSUPPORTED`，见 §2.2 与 §4.3 的 Round 3 段落）。
- credal network 是 Bayesian network 的**严格推广**（Antonucci, de Campos & Zaffalon 2014, in Augustin et al. (eds.), *An Introduction to Imprecise Probabilities*, Wiley, ISBN `0470973811`；`CITED_PRIMARY`，读到章节 PDF）——推广意味着**更贵**，且该章自己列出 "some important challenges and open problems"。

**结论**：credal 决策（maximin / m-convex / 后悔）作为**默认**读出是过度设计。它应在**一个明确场景**下才启用——见 §9.2。

### 8.3 拒答的合法性与限度

见 FM-05。**Round 3 更正**：原文写「`REFUSE` 是一等输出（I6 / I18）」。`I6` 是「矛盾 ≠ 未知」，与 `REFUSE` 无关；`I18` 当前是 **`E3` 不可执行**（无成本模型，§5.0）。⇒ 正确的引用是 FM-05 的定理层（`VERIFIED`：三个 rejection model 共享 Bayes classifier + randomized Bayes selection function）加上**迁移层（`PLAUSIBLE`）**；`REFUSE` 是**一等输出**这一判断是 **`PLAUSIBLE` 迁移**，不是可执行不变量。Salez et al. 的公平性警告必须同时写进报告规范（且该警告与 `I17` 的 coverage 报告要求绑定，而 `I17` 当前不可执行）。

---

## 9. 建议

### 9.1 最小可行处理（现在做）

按「成本 / 收益」排序。全部不需要 LHRM 自创数学。

| # | 动作 | 成本 | 收益 | 对应不变量 |
| --- | --- | --- | --- | --- |
| **1** | 引入 `⊥` 作为每个坐标类型的底元素，**禁止对 `⊥` 做算术**（返回 `⊥` 或显式标记，不返回数） | 极低 | 消除 `AGENTS.md:24` 的最隐蔽违规形式 | I1, I2 |
| **2** | 引入 `evidence_mass` 标量（先验主导程度）作为**一等输出**；`evidence_mass < θ` 时禁止点 readout。度量与阈值留给 Architect | 低 | 让「`Unknown → prior`」的后果**可见** | I14, I17 |
| **3** | 引入 §1 的 **tag 分类**（10 值），tag 复合取**集合并**。**不**引入代数语义（只做类型排除） | 低 | 让 8 个失效模式可被区分 | I4, I5 |
| **4** | 采用 C1–C6 六条传播规则作为**实现约束** | 低 | 让 composite 的类型有定义 | I1, I3, I6, I7, I9 |
| **5** | 引入 **refinement 单调性**作为 readout 层的必要条件：**`readout` 的像不是状态更新路径的输入**（readout 不回写） | 极低 | 把 `PROJECT_HISTORY:116` 的文字禁令变成可检查条件 | I10, I11, I12 |
| **6** | 多峰后验**禁止取均值** readout | 低 | 消除「无指称点值」 | I15 |
| **7** | 引入 `REFUSE` / `Not-addressable` 作为**一等终态输出**，与 `Unknown` 区分 | 低 | 让「不算」成为合法答案 | I18 |
| **8** | 报告 coverage 数字（每个 Case Bank item） | 极低 | 防止「大量 Unknown」被当成质量 | I17（**E3，当前不可执行**；但**报告**这一动作本身零成本，缺的只是「低于何值算不完备」那个阈值） |
| **9** | 声明 `⊑`（信息 / 近似序）为一个显式概念，并登记逐坐标依赖表 | 中 | 为 I9/I11 提供前提 | I9（E2）, I11（E2） |
| **10** | 若采用 partial pooling：分离 `i→j` / `j→i` 的超参数或随机效应（或 `(1,−1)` contrast），**并把收缩导致的非对称衰减量作为一等 readout 报告** | 低 | 保护方向性 invariant | FM-09（`PLAUSIBLE`）。**注意：这不是 `I9` 的实例** |
| **11** | ~~优先落 9 条可立即检查的不变量~~ **（`REJECT`，见下）** | — | — | — |
| **12** | 把 §5.4 的替代文本提交 Architect 审阅（**本报告不改 canonical**；落点是**研究纪律段**，不是构念/schema 变更） | 极低 | 修正一条过强表述 | — |

**Round 3 对 #11 的处置（`review-r2 E-C11` / `H-F14`：`REJECT` 该计数）**。原文 #11 写「优先落 9 条**可立即检查**的不变量（I1–I4, I6, I7, I12, I14, I15）」。

- **数字巧合**：那一串枚举恰好**列出 9 个 ID**（I1、I2、I3、I4、I6、I7、I12、I14、I15），但 `I14` 不可执行（无 `θ`），所以**「9 条可立即检查」是错的**。
- **替换文本（Round 3 版）**：

```text
11'. 先落 E1 那 9 条判据已闭合的不变量：
     I1, I2, I3, I4, I6, I7, I8, I12, I15
     （与旧清单差一条：去 I14（有未赋值 θ），加 I8（幂等性，判据闭合））
     落地形态按条各不相同：schema 约束 / 属性测试 / 输出纪律 / CI 枚举 diff。
     **本报告不建议把它们当作一个整体"落"**——是否现在落地是 Architect 的排程决定，
     不是本文件的结论。
```

- **本 child 不主张** #1–#10、#12 中任何一条的**排程**。本表是**成本 / 收益的候选清单**，不是 Work Order。

### 9.2 应该延后

| # | 项目 | 为什么延后 | 触发升级的条件 |
| --- | --- | --- | --- |
| **D1** | credal set 作为默认存储层 | 组合不平凡（Liell-Cock & Staton 2025）；朴素组合系统性过松 | 出现一类 tag，其**先验**已知是多峰且机制不可辨识（典型：FM-01 的结构性空单元） |
| **D2** | maximin / m-convex / 后悔稳健决策 | 需要先有成本函数；没有决策场景就无对象 | 出现明确的成本敏感 readout 场景 |
| **D3** | 端到端不确定性传播（transition 层的 epistemic 状态） | 属于 R06 / R09 lane 的 territory；本 lane 不越界 | R06 交付 transition law 家族后 |
| **D4** | 完整 QSR 代数（RCC8/IA/STPA×/RCC9） | 需先决定 base relations；且全幂集 NP-hard（**该复杂度陈述当前 `PLAUSIBLE` / `HOLD_FOR_EVIDENCE`**，见 §2.2），**必须先声明 tractable subset**（例如 `ORD-Horn` 一类） | 需要对 construct family 做**关系型**（而非数值型）推理时，**且**已声明 tractable subset |
| **D5** | per-coordinate epistemic POMDP 建模 | **Ghosh, Rahme, Kumar, Zhang, Adams & Levine** 的框架是 RL 专用；迁移到关系状态未验证 | LHRM 引入可学习的 action policy 后 |
| **D6** | 与 K4 竞争的代数选型（`B` 是否需要细分为 `B_priv` / `B_public`） | 无明确需求 | 出现「私域矛盾 vs 公共矛盾」需要区分的 Case |
| **D7** | 校准指标（Brier / 严格 proper scoring rule）落地 | 需要 held-out Case Bank set，当前不存在 | Case Bank 达到可留出规模后 |
| **D8** | `I10` 作为一个判据 | `width` 未定义；多峰后验下 `I10` 可被反例击穿（§5.0 E4 档） | Architect 冻结 `width` 的定义（`upper_k − lower_k`？方差？credal 直径？分量的包络？） |
| **D9** | `I19` 作为一个判据 | **空判据**：任何非恒定函数都满足（§5.0 E4 档） | `I19` 被**重写**为一个非空的判据（FM-07 的论证需要另找形式化） |

### 9.3 一个具体的 canonical 形状（候选，非提议修改）

```text
CoordinateValue(k, i, j, t) =
    Known { value, kind, provenance, history_id, role_lens }
  | Unknown {
        tag ∈ { no_evidence, refused, private_to_partner, withheld_by_actor,
                disputed, censored, structurally_unobservable,
                not_yet_real, superseded, unmeasured_by_instrument },
        prior_set,          # tag 蕴含机制多重性时是集合，否则是单分布
        evidence_mass,      # 先验主导程度；一等输出
        value_class,        # ⊑_a 位置 / ⊑_t 位置 / 未来未定义 / 不可寻址 —— 互不同类
        provenance
      }
  + （独立的正交元数据，见下）
    Applicability { APPLICABLE | NOT_APPLICABLE_BY_RULE | APPLICABILITY_UNKNOWN,
                    reason, provenance }      # **不是值域的一元**（C-P5）
```

与现有架构的对应关系：

- `value_class` 承载 §2.3.1 的**两个**序（`⊑_a` 与 `⊑_t`）——注意**不是**旧版写的「F-01 的双序」，那措辞暗示了旧的错误方向；它与 `tag` **正交**（一个坐标可以同时是 `private_to_partner` 与 `not_yet_real`）。
- **Round 3：应用性性必须是独立的一层，不是 `tag` 的一元，也不是值域的一元**（Architect **C-P5** / X-5）。明确地：值域**保持许可式**；「该构念在本 dyad 无独立语义」**既不是 `0` 也不是 `Unknown`**；它落在**独立的适用性轴**上，词表 `APPLICABLE | NOT_APPLICABLE_BY_RULE | APPLICABILITY_UNKNOWN` + reason/provenance。**不要**把 `NA` 加进 `tag` 枚举。收敛由 Track R3-F 产出转换表，本文件不合并（§1.1）。
- **Round 3：`reporter_role` → `role_lens`（`SUPERSEDED_BY_REPAIR`）**。canonical 的 `Role` 是 **query/evaluation lens**，不是世界状态（`CURRENT_ARCHITECTURE.md:96`；`AGENTS.md` 当前架构方向第 3 条："Keep `Role` explicit as a query/evaluation lens; it does not replace world state"）。本文件原用 `reporter_role` 作为**记录层字段名**，与之同名不同层（§1.1）⇒ 会造成「reporter 是世界状态的一部分」这一误读。**本文件不新增 `reporter_role` 字段**：FM-08 的方向性要求（`PairState_(i,j)` 必须按 reporter 索引，或显式声明为 reporter-invariant）应当表达为**在 `Role` query lens 下取两个投影**，而不是给状态加一个角色标签。
- `history_id` 复用 `CURRENT_ARCHITECTURE.md:241` 已有的 `tau = (history_id, local_time)`。
- **这个形状不新增任何人类关系构念**，只新增**证据侧的类型**。这是它符合 `AGENTS.md`「few stable constructs」纪律的原因。**Round 3 补**：它也**不**把适用性折进值类（那会新增一个构念级语义单位），符合 **C-P5**。
- **本 child 不实施这个形状。** 它是 proposal；canonical 落地由 Track R3-D（`D2`）拥有。

### 9.4 状态建议

见 §11。

---

## 10. 明确非主张（Explicit non-claims）

1. **不主张** LHRM 现有 canonical 文档有任何错误。§0.1 的检索结果只说明**在本检索范围内**形式化内容缺失，不是**内容错误**。缺失 ≠ 缺陷。
2. **不主张** 项目实际持有的 `Computable != Certain` 为假。它成立。§6 的反例针对的是 mission 的**强版本**。**并且不主张项目持有那个强版本**——见 §0.0 的 `NEGATIVE_RESULT`：强版本在仓库内**字面不存在**。
3. **不主张** 任何 LHRM 坐标的先验、任何缺失机制在关系数据中的**具体分布**、任何 attrition 率。S19 / S20 只支撑「该问题存在且被领域当作问题处理」。
4. **不主张** Kalai–Vempala 定理**直接**适用于 LHRM（见 FM-07 的限制说明）。
5. **不主张** credal set / imprecise probability 是 LHRM 的「正确答案」。§9.2 明确列为延后项。
6. **不主张** K4 / RCC8 / IA / STPA× 中任一个是 LHRM 应选的具体代数。§9.3 给的是**形状**。
7. **不主张** 任何具体数值：阈值 `θ`、credal 集合大小、可接受 coverage 下限、refinement 收敛判据、**`width` 的定义**（见 §9.2 `D8`）。
8. **不主张** Belnap 关于「被告知为假最糟」的话是 LHRM 的决策规则建议。那是对**信息论意义上被告知为假**的评价。
9. **不主张** 拒答 / `REFUSE` 应成为 LHRM 的**默认**输出。Salez et al. 明确警告了其公平性代价。**（Round 3 精化：「成本敏感读出下 `REFUSE` 是一等输出」是 `PLAUSIBLE` 迁移；「它是默认输出」不是本文件的结论，且本文件从未这样主张。）**
10. **不主张** 本报告的任何一个不变量已被验证。它们是**可检验的候选**，目前无实现可检验。**且**：`I19` 是**空判据**、`I10` 的 `width` **未定义**（§5.0）——这两条**连"可检验"都算不上**，不得被引用为可检验不变量。
11. **不主张** 网络动力学里「homophily vs. contagion 需要观测过程才能区分」这一对应结论（Shalizi & Thomas 2011 **未获取**，见 §11）。
12. **不主张** 我读过任何 LHRM issue `#20`/`#21`/`#22`、Eye、Juece、PR31 的内容。**未读取、未执行、未引用。**
13. **Round 3 新增 — 不主张** §0.1 的检索支撑任何**穷举存在性**否定。它支撑的是一个**检索范围结论**（Architect **X-14**）。要升级为穷举否定需要一次按概念族的系统检索，本轮**未做**。
14. **Round 3 新增 — 不主张** `08b` 的存在性结果是对本文件 §1 的独立佐证。**`08b` 未读本文件**（§1.1）。两次发明**收敛**到相似的地方，不是**两次独立发现**的复制。
15. **Round 3 新增 — 不主张** 本文件 §1 的 10 值分类、或 §9.3 的形状，是 LHRM 应采用的 `Unknown` 编码。它是**一份待收敛的输入**（Track R3-F），不是答案。
16. **Round 3 新增 — 不主张** 任何 belief 侧构造（`k` / `m` / `Pol` / `Rel` / `g` / `value_class` / `tag`）是 `Reality` / `DirectedRelationshipState` 坐标。Architect **X-1** / 裁决 §C.1 已裁定 `PPR_(i about j,t)` **remains BeliefState**；「organizing variable」、持久性或预测强度**本身不蕴含** Reality-state 成员资格。改层位须走**明确的架构修订**，不是证据触发的静默变更。
12. **不主张** 我读过任何 LHRM issue `#20`/`#21`/`#22`、Eye、Juece、PR31 的内容。**未读取、未执行、未引用。**

---

## 11. 剩余未知与本次未做到的事

1. **LHRM 自己的 prior 来源未定义。** `Unknown -> prior` 在 `PROJECT_HISTORY:102` 被提出，但 `docs/foundation/*` 中没有任何一处说明 prior 是什么、按什么分层、如何做 prior-sensitivity。`UNKNOWN_AS_OF_2026-09-27`。
2. **`evidence_mass` 的度量与阈值未冻结。** FICO（White & Carlin 2010）、posterior/prior KL、variance ratio、shrinkage 幅度都是候选。**本报告不推荐具体采用任何一个。**
3. **哪些坐标在结构上不可观测，从未被枚举。** 需要 Architect 逐构念族判定。这是**人类/架构决定**，不是研究问题。
   - **Round 3：这一条已被 Architect 收编为一条带唯一 owner 的阻塞项，见本节顶部的 `BLOCKER-OBS-01`。本条原文**保留**（作为本文件的发现记录），但**不再**在别处重复陈述。**
4. **LHRM 稀疏输入下的实际 calibration 未知。** 无 held-out Case Bank set，未报告过 reliability diagram。`UNKNOWN`。
5. **只核到元数据的来源**（未读正文，因此本报告只使用其标题/存在性可支撑的定性表述）：Miller & Wright (1995, JMF 57(4):921, DOI `10.2307/353412`)；Kupek (1998, Arch Sex Behav 27(6):581–594, DOI `10.1023/A:1018721100903`)；Gneiting & Raftery (2007, JASA 102(477):359–378)；Bergemann & Morris (2016, AER 106(5):586–591, DOI `10.1257/aer.p20161046`)。
6. **检索失败导致的缺口**（`websearch` 多次返回 HTTP 429 / 限流）：
   - couples / relationship longitudinal attrition 的**定量**文献（Lavner & Karney 2010 类型的 RDD 选择论证、Couple Study 的 attrition 描述）**未核实**。
   - **STPA× 的 13 元代数未核实**（第一次查询被 429 打断且未重试成功）。因此本报告**只使用 RCC8 / IA / RCC9 这一族已核实的 QSTR 结论**，不引用 STPA× 的具体性质。
   - **Dynamic epistemic logic 第 5.1 节的定理原文未逐条核实**。本报告只说「public announcement 是一个 refinement 算子且有完整公理化」这一层，不引用具体公式。
   - **Shalizi & Thomas (2011) 未获取**，故 §6 FM-06 不使用 homophily/contagion 对应。
7. **K4 是否足以表达 LHRM 需要的全部 `Unknown` 种类未验证。** K4 只有一个 `n`，而 §1 的分类至少需要 epistemic / temporal / structural / conflict 四个正交维度。**可能需要 K4 的扩张。选型未做。**
8. **C1–C6 对全部 construct family 是否封闭，未检验。**
9. **`F` 是否已被要求为随机/确定，未定义。** `CURRENT_ARCHITECTURE.md:203` 写作 `F(...)` 未指明。§3.3(c) 因此只能是风险提示，不能是缺陷认定。
10. **Round 3 新增 — `2^B` 组合复杂度的来源仍未打开。** §2.2 引用 [23] Renz 2007 与 [24] Dylla-Botea-Renz / Bhattacharya-Renz 作为 `CITED_PRIMARY`，但 **Round 3 未打开这些正文**（`NOT_OPENED`）⇒ 「全幂集 NP-hard / base relations 可算 / 需要 `ORD-Horn` 一类 tractable subset」这一串陈述在**本轮**降为 `PLAUSIBLE` + `HOLD_FOR_EVIDENCE`。**路由**：Track R3-E `E3`（carrying-source check）负责打开。**在那之前本文件不进入任何排序。**
11. **Round 3 新增 — 「松的程度依赖一个未声明的独立性假设」这一句的来源未找到。** `10.1145/3704890` 不作此陈述（§2.2、§4.3）。**路由**：需要一条 imprecise-probability 文献；本 child **未做**文献横扫（`NOT_OPENED`）。
12. **Round 3 新增 — `width` 的定义未冻结。** `I10` 与 §8.1 的 `width_k` 各自隐含一个不同定义。**这是 Architect 决策，不是研究问题**（见 §9.2 `D8`）。
13. **Round 3 新增 — `Kuhn's dogmatism paradox` 的指派仍未澄清。** `08b` §3.9 已独立指出规范对象是 Kripke–Harman paradox；本文件**不**就此下结论，标 `PLAUSIBLE` 并路由为开放问题（§5.4 末）。

---

## 11.0 `BLOCKER-OBS-01` — 可观察性 / 锚点登记表（**唯一一条、单一 owner**）

**Round 3 把本文件与 `08b` 各自的重复陈述合并为一条（`review-r2 R-E6` / `E-C16`；Architect **C-P13**）**：

| 字段 | 内容 |
| --- | --- |
| `id` | `BLOCKER-OBS-01` |
| `nature` | **一条 Architect / Human 裁决，不是一个研究问题。** 本文件原 §11-3 的定性是**正确的**（「需要 Architect 逐构念族判定。这是人类/架构决定，不是研究问题。」） |
| `gap` | 项目内**不存在**「哪些构念 / facet 原则上可被直接观察、只能自报、只能由伴侣报告、有行为锚、只能推断为 latent、**结构性不可观测**」的清单 |
| `blocks` | ① 本文件 §1 的 `Unknown` 分类落地（`structurally_unobservable` 无法赋值）；② 本文件的 `⊑` 程序——**`I9` / `I13` 需要一份已登记的依赖 / 锚点表**（§5.0 E2 档）；③ `08b` 的**整个** belief 层——`g = FIRSTHAND` 无法落地（`08b` §9-1）；④ `02` 已局部提出的单构念登记（`coordination` 不可知觉） |
| `status` | **`ACCEPT`（C-P13）** —— 逐 construct / facet 建立一份**候选**登记表，记录：direct observation possible? / self-report? / partner-report? / behavioral anchor? / inferred latent only? / structurally unobservable? / applicable scopes / evidence-provenance |
| `性质` | **测量元数据，不是本体扩张**（C-P13 逐字："This registry is measurement metadata, not a new primitive list"） |
| `owner` | **Track R3-D 的 measurement-semantics child**（`ARCHITECT_ROUND3_DISPATCH_V1` §Track R3-E→`D5`：`architect/measurement-semantics-v0.1`），**唯一 owner**。本文件与 `08b` **都**只是**提出者** |
| `本文件的角色` | **需求方 + 转换表的一列。** 本文件**不**建这份表，**不**改任何 canonical 文件，**不**发明第三套编码 |
| `dependency` | 该表是未来 `Unknown` / `Belief` 映射规则的依赖项（dispatch `D5` 原话："It should become the dependency for future Unknown/Belief mapping rules"） |
| `priority` | **head-of-list。** 按裁决 **X-12**，优先级是**依赖解锁序**，不是「便宜」；并且**一条负面结果不是阻塞项** |

**并且：它不阻塞 §2.3 的 K4 修正。** K4 的两个序是**纯数学事实**，不依赖可观察性清单；本文件已用主源逐字核实（§2.3.1）。把这两件事绑在一起是 Round 2 的一个耦合错误。

---

## 12. 参考文献

> 标注约定：`[PRIMARY]` 读到原文或官方摘要全文；`[ABSTRACT]` 读到官方摘要；`[METADATA]` 只核到 DOI 元数据；`[SECONDARY]` 转述页；`[PARTIAL_BIB]` 正文读到但书目不完整；`[UNVERIFIED]` 本次未核。

1. `[ABSTRACT]` Kalai, A. T., & Vempala, S. S. (2023; v3 2024-03). *Calibrated Language Models Must Hallucinate.* arXiv:2311.14648. STOC 2024. DOI `10.1145/3618260.3649777`. — FM-07；quote: "Hallucination rate ≥ MF̂ − Miscalibration − 300|Facts|/|Possible hallucinations| − 7/√n"。
2. `[PRIMARY]` Raykar, V. C., Yu, S., Zhao, L. H., Valadez, G. H., Florin, C., Bogoni, L., & Moy, L. (2010). *Learning From Crowds.* Journal of Machine Learning Research, 11(43), 1297–1322. `https://jmlr.org/papers/v11/raykar10a.html` — FM-02。
3. `[ABSTRACT]` Swann, W. B. Jr., De La Ronde, C., & Hixon, J. G. (1994). *Authenticity and positivity strivings in marriage and courtship.* JPSP, 66(5), 857–869. DOI `10.1037/0022-3514.66.5.857`. PMID 8014831. — FM-08 / §9.3。
4. `[PARTIAL_BIB]` Krosnick, J. A., Presser, S., & Tan, P. *The Impact of "No Opinion" Response Options on Data Quality: Distinguishing satisficing from optimizing in the survey interview.* `https://gspp.berkeley.edu/archived/files/research/pdf/Krosnick_et_al..pdf`（完整出版信息未核） — FM-08。
5. `[ABSTRACT]` `[ROUND-3 CORRECTED]` Franc, V., Prusa, D., & Voracek, V. (2023). *Optimal Strategies for Reject Option Classifiers.* Journal of Machine Learning Research, 24(11), 1–49. `https://jmlr.org/papers/v24/21-0048.html`. 预印本：arXiv:2101.12523（v1 提交 2021-01-29）。 — FM-05, C6, I18。
   - **Round 3 更正（`review-r2 E-C9`「两处书目错误」之一）**：原条目写 `JMLR, 24, 21-0048. … (2021)`，**年错**。JMLR v24 的目录页逐字给出 `24(11):1−49, 2023`，页脚 `© JMLR 2023`。`21-0048` 这个 article id 是**对的**，**卷/期/页与年**需按 v24 目录页写。
   - **证据档从 `[PRIMARY]` 降为 `[ABSTRACT]`**：Round 3 只读到 JMLR 官方摘要页 + 目录页，**未读正文 §2.4**；原条目自陈「读到摘要与 §2.4」，本轮不能维持。
   - **术语提示**（同一处错误的另一面）：JMLR 正式版把第三个模型写作 **bounded-abstention**；只有 arXiv v1 预印本用 **bounded-coverage**。引用哪个版本就用哪个名字。
6. `[ABSTRACT]` `[ROUND-3 CORRECTED]` Ghosh, D., Rahme, J., Kumar, A., Zhang, A., Adams, R. P., & Levine, S. (2021). *Why Generalization in RL is Difficult: Epistemic POMDPs and Implicit Partial Observability.* NeurIPS 2021. arXiv:2107.06277. — FM-06, §7.2。
   - **Round 3 更正（`review-r2 E-C10`；本条的处置是 `REJECT` 对书目条目、`ACCEPT` 对内容）**：原条目写 `Rajaraman, D., Han, T., Yang, P., Ramchandran, K., Van Dyke, D., Peng, X., & Levine, S. (2021)`。**作者表错误。**
   - **核实（两处独立，2026-09-28）**：① arXiv abs 页逐字 "Authors: Dibya Ghosh, Jad Rahme, Aviral Kumar, Amy Zhang, Ryan P. Adams, Sergey Levine"，`[Submitted on 13 Jul 2021]`，DOI `10.48550/arXiv.2107.06277`，Comments "First two authors contributed equally"；② OpenAlex `W3181634442` 与 `W4287078276` 的 `authorships` 与之一致。
   - **内容不变**：本文件 FM-06 / §7.2 引用的那两句确出自该文；改的只是书目。**原作者表不得再被引用。**
7. `[PRIMARY]` Tennenholtz, G. (2023). *Delphic Offline Reinforcement Learning under Nonidentifiable Hidden Confounding.* arXiv:2306.01157. — FM-01。
8. `[ABSTRACT]` Tennenholtz, G., Hallak, A., Dalal, G., Mannor, S., Chechik, G., & Shalit, U. (2021). *Covariate Shift of Latent Confounders in Imitation and Reinforcement Learning.* NeurIPS 2021 Workshops (DeepRL). — FM-06。
9. `[ABSTRACT]` Baltag, A., van Ditmarsch, H. P., & Moss, L. S. (2008). *Epistemic Logic and Information Update.* Handbook of the Philosophy of Science, 8, 361–455. DOI `10.1016/B978-0-444-51726-5.50015-7`. — §3.2。
10. `[PRIMARY]` Liell-Cock, J., & Staton, S. (2025). *Compositional Imprecise Probability: A Solution from Graded Monads and Markov Categories.* Proc. ACM Program. Lang. 9 (POPL), Article 54. DOI `10.1145/3704890`. — §2.2, §4.3, D1。
11. `[SECONDARY]` Augustin, T., Coolen, F. P. A., de Cooman, G., & Troffaes, M. C. M. (Eds.) (2014). *An Introduction to Imprecise Probabilities.* Wiley. ISBN `0470973811`.
12. `[PRIMARY]` Antonucci, A., de Campos, C. P., & Zaffalon, M. (2014). *Probabilistic graphical models.* Ch. in [11]. `https://people.idsia.ch/~zaffalon/papers/2014itip-pgm.pdf` — §8.2。
13. `[PRIMARY]` Pelessoni, R., & Vicig, P. (2022). *Jensen's and Cantelli's Inequalities with Imprecise Previsions.* arXiv:2211.01503. — §2.2, §5.3, §8.1。
14. `[SECONDARY]` Belnap, N. D. (1977). *A useful four-valued logic.* In J. M. Dunn & G. Epstein (Eds.), *Modern Uses of Multiple-Valued Logic.* D. Reidel. — §2.3, FM-03, FM-08。
15. `[PRIMARY]` Mundhenk, J., Rautmann, S., & Schnoor, A. (n.d.). *Belnap's Four-Valued Logic and De Morgan Lattices.* `https://users.fmi.uni-jena.de/~mundhenk/Webseite/FDE/BelnapIGPL.pdf` — §2.3, §2.3.1, FM-03。
    - quote 1（bilattice）："the presence of two ordering relations on it (the truth order and the knowledge order) has given rise to the interesting notion of bilattice"
    - quote 2（**Round 3 用于纠正 K4 序方向**，`CITED_PRIMARY`，本 child 于 2026-09-28 下载并抽取 PDF 正文 §2 逐字核到）：
      > "In that diagram, the ordering relation ⊑ goes upwards, thus **f = min M4 and t = max M4**, that is, we are considering the so-called **truth-ordering** relation, which was the one originally considered by Belnap to define his entailment in the way we do in Definition 2.1. It is this ordering relation the one giving that set the structure of a De Morgan lattice."
      >
      > "Note that another ordering relation is also possible (the **knowledge ordering**, going from left to right, **with n and b as bounds**) but then negation has quite a different behaviour; the notion of bilattice has been introduced to organize the coexistence of both orders, and of their respective lattice operations …"
      >
      > 同节：universe `M4 = {f, n, b, t}`，此集合在文献中亦称 `FOUR`。
    - ⇒ **truth order：`F` 底 / `T` 顶；knowledge（信息 / 近似）order：`N` 与 `B` 为两界（即 `N` 底 / `B` 顶），`T` 与 `F` 不可比。** 这条 quote 是 §2.3.1 更正的唯一依据。
16. `[UNVERIFIED]` Belnap, N. D. (1976). *On a partial truth functional.* Inquiry 19(4), 490–499. DOI `10.2307/2265159`. — 背景提及，未用于任何主张。
17. `[PRIMARY]` White, I. R., & Carlin, J. B. (2010). *Bias and efficiency of multiple imputation compared with complete-case analysis for missing covariate values.* Statistics in Medicine, 29, 2920–2931. DOI `10.1002/sim.3944`. — FM-04。
18. `[PRIMARY]` Seaman, S. R., Bartlett, J. W., & White, I. R. (2012). *Multiple imputation of missing covariates with non-linear effects and interactions.* BMC Medical Research Methodology, 12, 46. DOI `10.1186/1471-2288-12-46`. — FM-04。
19. `[METADATA]` Miller, R. B., & Wright, D. W. (1995). *Detecting and Correcting Attrition Bias in Longitudinal Family Research.* Journal of Marriage and the Family, 57(4), 921. DOI `10.2307/353412`. — §1 分类表（`refused` / attrition 行）。
20. `[METADATA]` Kupek, E. (1998). *Determinants of Item Nonresponse in a Large National Sex Survey.* Archives of Sexual Behavior, 27(6), 581–594. DOI `10.1023/A:1018721100903`. — FM-01。
21. `[METADATA]` Gneiting, T., & Raftery, A. E. (2007). *Strictly Proper Scoring Rules, Prediction, and Estimation.* JASA, 102(477), 359–378. DOI `10.1198/016214506000001437`. — I16。
22. `[SECONDARY]` Walley, P. (1991). *Statistical Reasoning with Imprecise Probabilities.* Chapman & Hall. ISBN `978-0-412-28660-5`. — 术语出处。quote（转述）："precision is often mistaken for accuracy, whereas an imprecise representation may be more accurate than a spuriously precise representation"。
23. `[PRIMARY]` Renz, J. (2007). *Qualitative Spatial and Temporal Reasoning.* IJCAI-07, 519–526. `https://www.ijcai.org/Proceedings/07/Papers/083.pdf` — §3.2。
24. `[ROUND-3 DOWNGRADED → NOT_OPENED]` Dylla, M., Botea, D., & Renz, J. (2013). *Algebraic Properties of Qualitative Spatio-Temporal Calculi.* arXiv:1305.7345. + Bhattacharya, M., & Renz, J. (2023). *Decomposition and tractability in qualitative spatial and temporal reasoning.* EPFL LIA. — §2.2, §3.2。
    - **Round 3 降级（`review-r2 E-C7`）**：本 child **未打开**这两条正文（`NOT_OPENED`）⇒ 该族所支撑的「`2^B` 全幂集 NP-hard / base relations 可算 / 需 tractable subset」在**本轮**降为 `PLAUSIBLE` + `HOLD_FOR_EVIDENCE`。**路由**：Track R3-E `E3` carrying-source check。**在打开之前本文件不进入任何排序。**
    - 同理，[23] Renz 2007 的**引文本身**（有限网络必然终止，因为 refinement 单调）**可用**；不可用的是**由它外推出的 LHRM 可算性边界**（终止性要求关系集有限，而 base relations 尚未选定）。
25. `[PRIMARY]` Hirschfeld, …, Thielsch, M. T., et al. (2014). *Selecting items for Big Five questionnaires: At what sample size do factor loadings stabilize?* J. Research in Personality.（完整作者表 / 卷页未核） — §7.1。
26. `[PARTIAL_BIB]` *Robustifying Empirical Bayes.* arXiv preprint. `https://arxiv.org/html/2603.00704v2`（arXiv id 与日期异常，需复核；正文已读，含对 Berger 1985 的引文） — §7.3。
27. `[PRIMARY]` Gu, J., & Koenker, R. (2015). *On a Problem of Robbins.* International Statistical Review. `http://www.econ.uiuc.edu/~roger/research/ebayes/isrProbRob.pdf` — §7.3。
28. `[PRIMARY]` Salicz, T., et al. (2021). *Towards optimally abstaining from prediction with OOD test examples.* NeurIPS 2021. `https://proceedings.neurips.cc/paper_files/paper/2021/file/6a26c75d6a576c94654bfc4dda548c72-Paper.pdf` — FM-05。（`N-06` 是旧版 `07` 的 finding-id 命名空间残留，**本文件未定义 `N-xx` 空间**；Round 3 删去该悬空交叉引用。其内容归 FM-05。）
29. `[METADATA]` Bergemann, D., & Morris, S. (2016). *Information Design, Bayesian Persuasion, and Bayes Correlated Equilibrium.* AER, 106(5), 586–591. DOI `10.1257/aer.p20161046`. — §2.2 延伸阅读（仅定性）。

### 12.1 项目内 provenance（本 lane 只读，未修改任何文件）

```text
AGENTS.md:24                       缺失不得静默压成 neutral / 完美匹配
AGENTS.md:26-27                    高层标签不作 primitive；低冗余 ≠ 零相关/动态独立
AGENTS.md:37                       坐标可为 interval / ordinal / category / constraint /
                                    probability distribution / Unknown /
                                    estimate+uncertainty+evidence
AGENTS.md:26, 35-38                representation-first invariant
docs/foundation/CURRENT_ARCHITECTURE.md:18          第一目标含「保留 Unknown 与不确定性」
docs/foundation/CURRENT_ARCHITECTURE.md:104-134     方向性 invariant（三条 != 断言）
docs/foundation/CURRENT_ARCHITECTURE.md:203         X_(t+1) = F(...)（F 的随机性未指明）
docs/foundation/CURRENT_ARCHITECTURE.md:236         Gamma_(A,B) = { X_(A,B)(tau) }（集合形式）
docs/foundation/CURRENT_ARCHITECTURE.md:241         tau = (history_id, local_time)
docs/foundation/CURRENT_ARCHITECTURE.md:284         混合状态空间中类型可共存（**无组合规则**）
docs/foundation/CURRENT_ARCHITECTURE.md:315         adjudicated|admitted|alleged|disputed|unknown
docs/foundation/CURRENT_ARCHITECTURE.md:96          Role 是 query/evaluation lens，不是世界状态
docs/foundation/CURRENT_ARCHITECTURE.md:80          Reality != Observation != Belief
docs/foundation/CURRENT_ARCHITECTURE.md:190         「订婚前不发生性行为」更接近 Agent boundary/constraint
                                                    而不是「性欲为零」——**不可适用性 ≠ 0** 的
                                                    canonical 先例（C-P5 / X-5 的锚点）
docs/foundation/STAGE_SUMMARY_2026-09-07.md:145-147  稀疏输入须允许；不得为公式完整而压平
docs/foundation/STAGE_SUMMARY_2026-09-07.md:162      Computable != Certain
docs/foundation/PROJECT_HISTORY_2026-09-10.md:74     Unknown 不能当成 0 或完美匹配
docs/foundation/PROJECT_HISTORY_2026-09-10.md:94-108 SoftDistance / hard vs soft / Unknown -> prior
docs/foundation/PROJECT_HISTORY_2026-09-10.md:115-116 稀疏输入须 graceful degradation；不得伪造 78/100
```

**Round 3 补的 provenance（逐字检索后新增）**：

```text
NEGATIVE_RESULT  A3D-NR-01（§0.0）
                 「missingness lowers certainty, not computability」在仓库内**字面不存在**。
                 项目实际持有：STAGE_SUMMARY_2026-09-07.md:162  Computable != Certain
                 （本 child 于 2026-09-28 在本 worktree 全部 *.md 上复检）
```

---

## 13. 建议状态与后续

**建议状态：`SUCCESS`（含 1 条 `NEGATIVE_RESULT` 子项），但附 Round 3 的降级项。**

**Round 3 状态修订（`review-r2` 汇总）**：

| 项 | 原自陈 | Round 3 处置 |
| --- | --- | --- |
| `SUCCESS` | `SUCCESS` | **保留**，但下方三条降级必须随状态一起引用 |
| 交付物 1–5 完成 | ✔ | ✔ 保留 |
| 3 条项目内未记载的结构性问题 | ✔ | ✔ 保留；**第 1 条（`Unknown` 缺类型学）现降为「一份待收敛的输入」**（§1.1），因为它与 `08b` 平行且未协调 |
| 「给出 19 条可检验不变量，其中 **9 条现在就能检查**」 | ✔ | **部分撤回**：数字 19 正确（`E-C12` `VERIFIED`）；**「9 条现在就能检查」被 `REJECT`**（`E-C11`）。Round 3 的分类是 **E1 = 9 条（清单不同）/ E2 = 4 条 / E3 = 4 条 / E4 = 2 条**，见 §5.0。且 `I19` **空过**、`I10` 的 `width` **未定义** ⇒ 这两条**不是**可检验不变量 |
| `NEGATIVE_RESULT` 子项 | 提到 | **升格为正式条目** `A3D-NR-01`（§0.0），并更正**指派**的读法：该句在仓库内字面不存在，且 mission 交给 `07` 的是**核验**任务而非持有断言 |
| §2.3 的 K4 序 | （隐含正确） | **已更正**（§2.3.1）。原 §2.3 全文保留在 `SUPERSEDED_BY_REPAIR` 块内 |

**明确降级为非主张的（Round 3）**：

- `2^B` 组合复杂度族（`[24]` 及其支撑）→ **`HOLD_FOR_EVIDENCE` / `NOT_OPENED`**（§2.2、§9.2 `D4`、§11-10）；
- 「松的程度依赖一个未声明的独立性假设」→ **`UNSUPPORTED`**，已从 §2.2 与 §4.3 撤回（§11-11）；
- Rajaraman 作者表 → **`REJECT`**（书目），作者改为 Ghosh 等（§12 [6]）；
- Franc 等的出版年与第三个模型名 → **已更正**（§12 [5]）；
- `I19` / `I10` → **不作为可检验不变量**（§5.0 E4、§9.2 `D8`/`D9`）。

**建议的后续工作（不属于本 lane；Round 3 已按 Round 3 的 owner 重新指派）**：

1. **A02 / 合成层** 处理 `A3D-NR-01` 的 claim-attribution correction。**Round 3 注**：原写的「§1.2」在本文件中**不存在**（本文件没有 §1.2；`§1.2` 是旧版 `07` 的编号残留）⇒ 正确指向是 **§0.0**。
2. **Track R3-D / measurement-semantics child**：`BLOCKER-OBS-01` 可观察性 / 锚点登记表（唯一 owner，§11.0）。
3. **Track R3-F / taxonomy child**：把 §1 的 10 值分类 + `08b` 的平行分类 + canonical 的 `CURRENT_ARCHITECTURE.md:315` 收敛成**两轴**候选分类（epistemic/measurement 不确定性轴 + 适用性轴）+ 转换表；`MAPPING_FAILURE` 留在两轴之外。**不得**生成 14+ 值单一枚举（§1.1）。
4. **Track R3-D（`D2`）**：独立 applicability 轴 `APPLICABLE | NOT_APPLICABLE_BY_RULE | APPLICABILITY_UNKNOWN` + reason/provenance，**不**折进 `Unknown` 值域、**不**折成 `0`（C-P5 / X-5）。
5. **Track R3-D（`D3`）/ Architect sign-off**：`InformationAction` 家族（`Disclose` / `Withhold` / `Misrepresent`）—— 见 `08b` §2.11 的 Round 3 段；本文件不实施。
6. **Track R3-E（`E3`）carrying-source check**：打开 `2^B` / tractable-subset 一族的原文（§11-10）。
7. **R05** 处理 §9.1 #9（`⊑` 的形式定义 + 逐坐标依赖登记），与 R06 的 transition law 对接。
8. **R13** 处理 §9.1 #7（`REFUSE` 作为一等输出，`PLAUSIBLE`）在 LLM Skill 层的行为。
9. **R15** 把 FM-03 的 Case Bank 反例（「`disputed` vs `unmeasured` 不可比」）作为 representation test 条目收录。**Round 3 注**：命名要避开与 `CURRENT_ARCHITECTURE.md:315` 的 `disputed` 冲突（§1.1）。
10. **R16** 在 Case Bank 达到可留出规模后，执行 I16（校准）——`I16` 当前 `E3`。
11. **Architect 决策请求（本文件不自行决定）**：冻结 `width` 的定义（§9.2 `D8`），否则 `I10` 永远不可执行。
