# HIGH_CONFIDENCE_FINDINGS — Round 2 review swarm over `youling/lhrm#31`

> **入选门槛（三条同时满足）**
> 1. 至少一个 child **实际打开过**一手件（canonical 原文 / 被审报告原文 / 外部来源全文或摘要），且其 `verdict` 为 `VERIFIED`；
> 2. `corroboration` **不是** `NON_INDEPENDENT` / `SAME_SOURCE` / `TRANSITIVE` / `RELAYED_NOT_INDEPENDENT`，
>    或者该行是**缺陷发现**（对报告自身的可复算不一致），其独立性由重算本身提供；
> 3. 未被阶段 2 的 `EV1` / `EV2` / `EV3` 或 `ADJ1`–`ADJ3` 推翻。
>
> **不入选**：仅因「多 lane 同意」而成立的行；child 标 `PLAUSIBLE` 的行；被 `EV3` 判 `REFUTED` / `PARTLY_REFUTED` 的行。
> 未入选者不是错的，只是**未达此门槛**——它们的去处是 `CONTESTED_FINDINGS.md` 或 `REJECTED_OR_WEAK_FINDINGS.md`。
>
> 每条给出：`id` · 命题 · 证据（含指针）· 独立性 · 对 PR #31 的处置。
> **Round-3 supersession pointer.** 本文件未删改任何 Round-2 评审主张。
> 已被取代 / 已被本轮修复取代的主张，逐条登记在
> **`SUPERSEDED_REGISTER.md`**（stable id `SR-A*` = 被 `ARCHITECT_ADJUDICATION_V1`
> 取代，`SR-B*` = 被 Track R3-A 的 PR #31 修复取代，`SR-X*` = 明确不取代）。
> 取代依据：`youling/lhrm#30` comment `5854920569`（adjV1）与
> `r3/a1`…`r3/a4b` 的 repair commit（见该 register §2 表头）。
> **本文件是 Round-2 的记录；不得再把被取代的表述当作待议项引用。**



---

## A. Gate 的结构性事实（最高优先级）

> **取代指针**： 见 `SUPERSEDED_REGISTER.md` §SR-A3 · §SR-A22 · §SR-X1

### H-A1 — Gate A/B/C 在判据原文下不存在会被算作失败的结果

> **取代指针**： 见 `SUPERSEDED_REGISTER.md` §SR-A3（C-P1 修改条款：不得发明 N 阈值）· §SR-B16（严重性）· §SR-X1（事实层不取代）

- **判定**：`VERIFIED`（`I-C1`；`ADJ3` Q1 逐节点过；`EV1` §7 独立复现）
- **证据**：`PARAMETER_CONVERGENCE_V0_1.md` §15 Gate A/B/C 为纯 test-only 章节，全章唯一的后果句是 `:748` 的 keep-end；
  §13 的 failure 诊断词表（`:641-649`，被 `AGENTS.md:62` **逐字镜像**）是**纯加法封闭**的——6 个 hole 全是「某物无法被表示」，
  **没有 `redundancy` / `duplicate` 一类**。Gate C 若产出「`Trust` 与 `AttachmentSecurity` 冗余」，当前类型系统里无处可记。
- **独立性**：`I-C1` 标 `NON_INDEPENDENT`（A03 §1.4 自陈是对 `17` 的独立复核 ⇒ 复核不是独立源）。
  **但 `EV1` 与 `ADJ3` 各自独立复现**（`EV1` 全文逐行、`ADJ3` 逐节点过），且二者**未共享中间产物**。
  parent 判：`PROJECT_PRIMARY`，两份独立一手复现。
- **对 PR #31 的处置**：**保留这条 blocking finding，但必须换理由**（见 `REJECTED_OR_WEAK_FINDINGS.md` R-A1、R-A2）。
  `EV1` 给出的最小准确描述：缺的是「后果动词 + 阈值 + 一个诊断类型 + 一个 ablation 步骤」，**不是缺否决分支**——
  分支的意图在 `AGENTS.md:54`、`CURRENT_ARCHITECTURE.md:158`、`CONSTRUCT_SCOPE_DIRECTIONALITY.md:107` 四处都写清了。
- **工程含义**：`EV1` §9 明确「**只需要文档编辑**，不需要新实验、不需要新数据、不需要新文献」。约 5–8 句新增文字
  + 1 个 ablation 步骤定义 + 1 个诊断枚举值。`ADJ3` 另要求把变更面从 1 文件 / 2 节扩到 **4 文件 / ≥6 节**
  （`§2.1`–`§2.6` 全族 + `§13` 类表 + `§15` 三门 + `AGENTS.md:62`）。**parent 记录两者的并集，并采用 `EV1` 的成本更正。**

### H-A2 — `§2.6` line 86 是一句关于自身可测性的未兑现承诺

- **判定**：`VERIFIED`（`I-C3`；`ADJ3` Q2；`EV1` §6 第 3 点，三方独立）
- **证据**：`:86`「这项将在 Case Bank regression 中直接测试」；`:86` 描述的是 leave-one-out ablation。
  而 Gate A（`:707-715`，**它就是** Case Bank regression）的 5 个步骤里**没有任何一步**包含「移除某个 construct 再重测」。
  `16:117`、`VALIDATION_CORPUS` 全文亦无此臂。
- **独立性**：**三份互不共享中间产物**（`I` 自构造、`ADJ3` 逐节点过、`EV1` 从 `:86` vs Gate A 的内部矛盾切入）。
- **处置**：**这是唯一能让 8 项 basis 缩小的程序通道**。`19` 与 `A03` 给的修复动作只改 `§13` 与 `§2.6`，
  而缺的**是一条臂，不是一个阈值**（`ADJ3` rec 5）。

### H-A3 — `MAPPING_FAILURE` 在类型上不可达，由**三个**文本上互不相同的机制产生

- **判定**：`VERIFIED`（`I-C4`；`ADJ3` Q5 逐条核实；`EV1` §6 第 2 点）
- **机制与阶段**（`ADJ3` 表格，三者作用于流水线三个不同阶段、针对三个不同文本对象）：

  | # | 机制 | 文本位置 | 阶段 | 操作 |
  |---|---|---|---|---|
  | (1) | 映射类表有 **4 个** catch-all | `§13:618-629` 的 10 类中第 7/8/9/10 类 | 分类 | 装不下的句子**找不到**可落类 ⇒ 失败**不被记录** |
  | (2) | 诊断清单有 `merely narrative/irrelevant` | `§13:648` **和** `AGENTS.md:62`（**同一串，两处**） | 分诊 | 已记录的失败**必然被解释掉** ⇒ 失败**永不升级** |
  | (3) | 成功门槛被降到「有合法落点」 | `§14:679` | 阈值 | 门槛低 ⇒ 失败**很少发生** |

- **独立来源数 = 1 primary + 1 镜像**：`AGENTS.md:62` 与 `§13:641-649` 是**同一条 7 项诊断清单**（逐项措辞一致）。
  `19:102` 把它当「§13 之外的第二个来源」来数机制，是**把镜像当独立源**。
- **两处 `19` 自带的错**（`K` 与 `I` 均未抓到，`ADJ3` 抓到）：catch-all 是 **4 个不是 3 个**（`19` 少算一个，
  方向是**把缺陷说得比 A03 小**）；**「§14 Step 3」是悬空指针**——§14 无任何编号 step，该指针来自 §15 Gate A 第 3 步。
- **处置**：**必须**同时改 `PARAMETER_CONVERGENCE_V0_1.md` **与** `AGENTS.md:62`（追加 `redundancy hole` 一类），
  否则 delete 臂在类型上仍不可达。这是全 PR 最便宜的一处「不能停在 proposal」的修复之一。

### H-A4 — Gate B 的 11 个 cell 中 10 个是项目自身文本的逐条复述

> **取代指针**： 见 `SUPERSEDED_REGISTER.md` §SR-A22（C-P2 增补分表约束）· §SR-B17

- **判定**：`VERIFIED`（`I-C7`；`ADJ3` Q3 独立重算）
- **关键更正**：`19:35` 与 `19:182` 的「A03 修正为 **8/11**」是**误引**。`A03:736`（`X-5`）与 `A03:751`（`N-A03-6`）**逐字否决过 8/11**，
  理由是「8/11 是 scope 标签（§1.5）」。`ADJ3` 进一步发现 A03 自己的第 11 格也错：
  `A03:157` 把 `high-attraction/low-trust` 映射到 `§4 D4 :179`「可高**喜欢**低信任」，而 `:132`（D1）与 `:151`（D2）
  **明确把 Liking 与 Romantic Attraction 分为两个构念** ⇒ A03 用一个被显式区分开的构念顶替了 Gate B 的 cell。
- **`ADJ3` 逐格重算结论**：10 个 cell 自产，唯一新 cell = `high-attraction/low-trust`，而它的覆盖为 0。
- **必须同时记录的限定**（`ADJ3` rec 4）：Gate B **混合了两张不同用途的清单**（8 项是抽样框、3 项是构念解耦模式），
  因此**不存在有意义的单一分母**。`caregiving` 的零覆盖是**口径依赖的 partial = 2/12**（L0-003 医患 23 年 / L3-001 care-control），
  **不是 0**（`I-C11`：成因部分来自 rights gate，不是 curation 缺陷）。
- **处置**：接受 10/11；**同时**记录「分母无意义」；修法 = 把 §15 Gate B 重写为**外部生成**的反例集 + 给每 cell 定合格判据
  + 与 `§2.4` / `CONSTRUCT_SCOPE §7.6` / `CURRENT_ARCHITECTURE:53-56` 四方对齐。

### H-A5 — `17` §0 的独立性声明为真（Git 层与内容层均通过）

- **判定**：`VERIFIED`（`I-C13`；`I` 自做 git + SHA + grep）
- **处置**：`ACCEPT_AS_PROPOSAL` —— 同时登记 `docs/research/overnight-2026-09-27/` 下的 temp 目录为**未声明的暴露面**
  （不构成污染证据，但应在 `17` §0 补一句声明）。

---

## B. 引用与记账（`J` + `EV2`，两者独立复算）

> **取代指针**： 见 `SUPERSEDED_REGISTER.md` §SR-B4 · §SR-B5 · §SR-B6 · §SR-B7 · §SR-X2

### H-B1 — A01 的 DOI 解析率是 95.5%，不是 100%

> **取代指针**： 见 `SUPERSEDED_REGISTER.md` §SR-B4

- **判定**：`VERIFIED`（`J-C1`、`J-C13`；`EV2` §1 独立复核）
- **证据**：`A01:15` 自己写 `337/353 = 95.5%`；`A01:34` 写「353/353（100%）」。**同一文件两行直接冲突。**
  post-repair 残留 1/99（`10.1037/pas0000986` / `aaai.v35i7` / `S0010-0277(02)00054-9` / `osf.io/f6wbn_v1`）。
- **独立性**：`J` 与 `EV2` **各自**重算，结论一致（`EV2` 独立复算 878 亦与 `J` 完全一致）。
- **处置**：`REJECT` 「100%」这一格；见 manifest §7 M-5。

### H-B2 — 29 个 DOI 解析到的不是它声称的那一篇论文

- **判定**：`VERIFIED`（`J-C2`）——逐条点名，含 `03:146`+`03:336`（应 `10.1037/pas0000986` = Crasta, Rogge, Maniaci & Reis 2021,
  *Psychological Assessment* 33(4):338–355）。
- **处置**：这些条目目前带 `UNVERIFIED_DOI` 标记（正确），但**必须**在引用任何一条前先修指针。

### H-B3 — 1199 → 642 → 533 的去重链成立，倍率 2.25×

- **判定**：`VERIFIED`（`J-C3`；`EV2` 未推翻）
- **处置**：保留。**但**它与 M-2 是两笔账：`533 distinct source` 可用，`1,201` 与「2.3–3.4×」不可用。

### H-B4 — A04 的 `PEER_REVIEWED_PRIMARY` 分层系统性错标

> **取代指针**： 见 `SUPERSEDED_REGISTER.md` §SR-B5

- **判定**：`VERIFIED`（`J-C6` 作为「peer-reviewed 计数」`VERIFIED` / 作为「科学重量」`WRONG-SCOPE`；`EV2` 实测更差）
- **证据**：`EV2` 对 319 行每 20 行取 1（n=16），**9/16 = 56%** 不是 primary empirical work（是 theory / methodology / review / 综述 / 计算模型）。
  `J` 说「至少 20–30% 名不副实」，方向一致、量级更差。
- **处置**：`350 peer-reviewed` **可**作为「350 个同行评审来源」使用；**不可**作为「科学重量」。
  在分层重出前，`350` 不得进入任何承重陈述。见 `REJECTED_OR_WEAK_FINDINGS.md` R-B3。

### H-B5 — A04 承重表 ≥16/30（53%）作者归属错，且该表结构上无法发现此类错误

> **取代指针**： 见 `SUPERSEDED_REGISTER.md` §SR-B5

- **判定**：`VERIFIED`（`J-C7`；`EV2` §1 + §6.3）
- **证据**：`J` 打开 19 行得 10 行错（其表内行数与散文的「11 行」不一致——`EV2` 已指出）；`EV2` 打开 J 未开的 11 行得 6/11 错。
  合并 16/30 = 53%。至少需改：`Chivers et al. 2025`→Junkins et al.、`Gerych 2007`→Gneiting & Raftery、
  `Bodenmann & Frighi 2011`→Bacon/Conte/Moffatt、`Ledgerwood et al.`→Gerpott et al.、`Cameron & Overall 2015`→Cook & Kenny、
  `Fraley et al. 2005`→Sibley/Fischer/Liu。
- **结构性根因**：`A04` 的 642 行来源表**没有 `author` 与 `title` 两列** ⇒ 语料的主导缺陷类（A01 实测 8.2%）在 A04 内**无法被发现**。
- **处置**：`REJECT` 「30 项中 28 项强度充分」（`J-C7` `UNSUPPORTED`）。**在任何人引用这张表之前必须重出。**

### H-B6 — 9 条 applied repair 中 8 条正确，1 条无效果

- **判定**：`VERIFIED`（`J-C12`）
- **残余**：`A01` 的 **83 条 `NARROW_REPAIR_REQUEST` 只执行了约 13 条**（`J-C19` `VERIFIED`），
  其中 ≥4 条为 `MAJOR`。建议只做两类：① 零风险且已实测的；② 承重指针。其余明确标为「接受为已知残余」，
  **不要让 70 条挂账稀释真正的 blocker**。

### H-B7 — Fixture 003 存在 `pointer_only` / `ai-train=no` / `GPTBot Disallow` 边界

> **取代指针**： 见 `SUPERSEDED_REGISTER.md` §SR-A9 · §SR-B7

- **判定**：`VERIFIED`（`J-C16`）
- **独立性**：`G-C22` 独立以穷尽检索确认「`13` 在六处实质使用该 fixture 却全文不记录边界」（`VERIFIED`）。
- **处置**：边界存在 = 高置信；**是否构成违反 = Human 权利裁决**（`J-C17` `CONTESTED`、lane `J` 自陈无权裁定）。
  见 `CONTESTED_FINDINGS.md` X-7。

---

## C. 权利与访问（lane `C`，逐条打开官方页面）

### H-C1 — 五份 CoU / 政策的原文级事实

| 数据集 | 事实 | 判定 |
|---|---|---|
| **SHARE** | 使用条款 §7 明文禁止「非完全自管」应用处理 SHARE 数据、禁止用于训练 AI 模型（本地纯科学用途除外）；AI/ML 派生量受同等限制 | `VERIFIED`（`C-C1`） |
| **Add Health** | 明文禁止用 LLM/AI 工具管理、处理或分析其数据，公版与 restricted 同等适用；LLM Type 1/2/3 Data Use 均为 None | `VERIFIED`（`C-C7`）—— `C` 建议把这条作为 rights-first 筛选的**样板条款** |
| **ICPSR** | Type 1 = None；Type 2 = Public-Use（须许可）；Type 3 = Public + Restricted（须许可）。Redistribution Policy 要求任何再分发先经 Data Stewardship Policy Committee 批准（Bylaws Art. 1.2.B） | `VERIFIED`（`C-C8`、`C-C9`） |
| **CESR** | 明文禁止用 LLM/其他 AI 工具管理、处理或分析其分发的任何数据；构成对所有现行 DUA 的违反 | `VERIFIED`（`C-C10`，但 `C` 自陈**非直接打开含该条款的页面**） |
| **HRS** | CoU（2026-02-04）**逐字禁止 AI 程序与 LLM 与 HRS 数据同用，且点名 open-source AI** | `VERIFIED`（`C-C11` —— `C` 直开 `hrsdata.isr.umich.edu/data-products/conditions-of-use` 确认） |
| **SOEP** | 存在专门的 SOEP AI and LLM Use Policy：Type 1/2/3 全 None，连 Type 3 都因 sandbox escape 不可靠而拒绝 | `VERIFIED`（`C-C13`）—— **`04` §5.1 权利汇总表没有 SOEP 行** |

- **独立性**：`C` 逐条直开官方页面；parent 未复核。`C` 自陈「本 lane 零数据接触」，全部为属性判断。
- **处置**：这六条是本轮**唯一一类可以直接改文档、不需要任何新证据**的高置信事实。
  特别注意：**`19`/A03 的「HRS 政策条文未取得，可能是最严的一份」这一 `UNKNOWN` 已被推翻**（见 R-C4）。

### H-C2 — 唯一的「零门槛可下载」数据集是 speed dating，且它只有一个时点

- **判定**：可用性与方向性设计结构 `VERIFIED`（`C-C17`）；变量名与 21 场 `PLAUSIBLE`
- **证据**：镜像 2026-09-27 仍在线；含 6 项双向评分；`wave` = 21 场**独立 session**，不是同一 dyad 重复观测。
- **处置**：它能支撑「`Z[i→j]` 与 `Z[j→i]` 确实是两个不同自由度」，**不能**支撑任何转移律
  （`L-C13`：`19` §5 的 8 个数据集中只有它在权利上今天可达，但单一时点）。

---

## D. 测量学（lane `B` / `F` 的逐字核实项）

### H-D1 — 序数数据必须用量度模型：六点逐字核实

- **判定**：`VERIFIED`（`F-C4` —— `F` 自称「本 packet 中唯一一条我建议越过 proposal 直接 durable 化」）
- **证据**：JPSP / *Psychological Science* / *JEP:General* 中所有提及 Likert 的文章 **100%** 用度量模型处理序数数据；
  后果 = false alarm、漏检、**系统性效应反转**（均值排序颠倒）；交互作用与趋势分析同样受影响；
  **对多个序数项取平均不能修复**；**不存在可靠的事后检出办法**；建议改用 ordered-probit。
- **独立性**：`F` **逐字核实全部五点**。parent 未发现反证。
- **处置**：`ACCEPT` —— 写入 `CURRENT_ARCHITECTURE.md` §9（CC-8）作为**纯增补 rationale**：
  不改本体、不依赖新数据，并**独立加强**项目已有的 invariant 4。这是本轮性价比最高的 canonical 增补。

### H-D2 — 三个测量工具的关键数字逐字命中

| 工具 | 数字 | 判定 |
|---|---|---|
| **ANS**（自主神经系统同步） | 关系结局 `ES=.09`（边缘显著）、`I²=76.0%`；交感 `ES=+.19 (p=.02)`、副交感 `ES=−.21 (p=.03)`、合并 `ES=+.16`；表现结局 `ES=.26`、`I²=52.7%`。**结构上不可分解为 i→j / j→i** | `VERIFIED`（`B-C17`，`F-C3` 独立复核）。`B` 判「这是本报告最扎实的单条」 |
| **PRI** | item pool = 19 量表 246 题、`N=2,334`；PRI-8 `R α=.93 ω_WP=.83`、`I α=.88 ω_WP=.77`；Study 3 用 APIM 161 对伴侣把 i 的知觉与 j 的自报行为对起来 | `VERIFIED`（`B-C18`）。**附一条**：`§4.3 → R16` 把 PRI-8 列入「最小可用测量面板」，须同时标 `NOT_OPENED` |
| **DAS** | 信度泛化 meta = 91 篇研究 / 128 样本 / 25,035 人；total 与 Cohesion/Consensus/Satisfaction 内部一致性可接受但低于 Spanier 原报告；Affective Expression 分量 α 差 | `VERIFIED`（`B-C19`） |
| **ECR-R** | 36 题 2 维；IRT `N=1,085`；官方评分 1–18 anxiety（items 9/11 反向）、19–36 avoidance（12 题反向）；官方页明示可改写指向其他关系类型 | `VERIFIED`（`B-C9`）—— `B` 判 `ACCEPT` |
| **RMBM** | 26 题 / 7 因子；两个前代 RMSM 有 fundamental measurement flaws 且在正确 item construction 下均不可用；因子结构在 3 样本间稳定 | `VERIFIED`（`B-C16`）。**但 `03` 把该证据归入「求值者/施测者效应」 confound 行是错的**（`B-C16` `CONTESTED`），须改到量表 item construction 缺陷 |

### H-D3 — Belnap K4 的 refinement consistency 条件成立；Scott-continuous 是经典充分条件

- **判定**：`VERIFIED`（`E-C5`；Belnap 构造 K4 时明确采用该条件）
- **处置**：`ACCEPT_AS_PROPOSAL` —— 定理层接受；落地层（`Info` 的定义、`RelMergeability`）待定。
  **注意 `07` §2.3 的序方向陈述是错的**（见 R-E1），本条不救它。

### H-D4 — Credal set 组合用「凸分布幂集」monad **不是** compositional

- **判定**：`VERIFIED`（可组合性 + 更紧的界，`E-C6`）；「松的程度依赖一个未被声明的独立性假设」这一句 `UNSUPPORTED`
- **处置**：`ACCEPT_AS_PROPOSAL`（成本结论）；要求 `07` 补引 imprecise-probability 文献。

### H-D5 — 三个 reject model 共享同一最优策略 = Bayes classifier + **随机化** Bayes 选择函数

- **判定**：定理 + 逐字引文 `VERIFIED`（`E-C9`）；迁移到 LHRM readout `PLAUSIBLE`；**附带两处书目错误**
- **处置**：定理接受；**请 `07` 修正书目与术语**。选择函数不是可选附件 ⇒ 成本敏感读出下 `REFUSE` 是一等输出。

### H-D6 — 三条 belief 层 REJECT 的论证可接受；belief 层已是 canonical 既决事项

- **判定**：三项 REJECT 的**结论** `PLAUSIBLE`（论证依赖的复杂度/等价性结果 `NOT_OPENED`）（`E-C17`）；
  「LHRM 已经决定要有 belief 层」 `VERIFIED`（`E-C20`）
- **处置**：`ACCEPT`（三项 REJECT 的结论）+ `ACCEPT`（belief 层是 canonical 已决事项、非新增构念）。
  剩余的**唯一**问题是它有多小 ⇒ 见 R-E5（`08b` 主张「没有第九个原语」`UNSUPPORTED`，因为「最小」是强主张）。

---

## E. 动力学与权力（lane `F`）

### H-E1 — 六个效应量逐字命中，零误差

- **判定**：`VERIFIED`（`EV3` Claim 3 (a)：「六个数字全部逐字命中，零误差」；`F-C3`）
- **数值**：`ES = 0.09, p > .10, I² = 76.0%`；亚组交感 `+0.19`、副交感 `−0.21`、合并 `+0.16`；表现结局 `ES = 0.26, I² = 52.7%`。
- **独立性**：`EV3` 与 `F` 未共享中间产物（`EV3` 从 `09` 的文本读，`F` 从 meta 原文读）。
- **处置**：**数字保留；由它推出的结论全部撤回**（见 R-F1）。`B` 补充：引用这组数字时**必须同时带 `I²=76%`**。

### H-E2 — 权力三分（relative / total / punitive）是本轮唯一被逐字核实且三份俱全的本体判定

- **判定**：`VERIFIED`（`F-C21`：「这是 `10` 最强的一节」）
- **内容**：`relative power = power difference`（零和，可由两方向依赖不对称派生）；
  `total power = mutual dependence / relational cohesion`（非零和）；`punitive / retaliatory capacity` **不可**由 dependence 派生。
  → R2 作为完整表述 `NEGATIVE`；作为 relative power 分量的 readout **正确**。
- **处置**：`ACCEPT`（三分判定）+ `ACCEPT_AS_PROPOSAL`（须拆成 **R2-a** / **R2-b** 执行，见 C-P4）。
  **但 `F-C23` 独立指出 `total power` 的实现规格被写错**（见 X-4）。

### H-E3 — Interdependence matrix 的可识别性要求在亲属 dyad 上按构造成立地失败

- **判定**：`VERIFIED`（`G-C12` 的依赖图部分；`G` 自称方向与 `12` 所述**相反**——好消息）
- **内容**：SRM 式加法分解 `Construct(i->j,t) = population baseline + source_i + target_j + directed_dyad_(i->j) + context/history residual`
  要求 (a) target 属性与 source 的 dyad 进入/选择近似独立、(b) dyad 可重新选择。在亲属 dyad 上两条**按构造成立地失败**，
  故 `context/history residual` 不是残差而是主项。
- **处置**：`ACCEPT_AS_PROPOSAL`（作为 Gate C 的识别性前置检查）。**支撑引用著录不完整**，需补。

### H-E4 — 6 个维度中人们只能可靠区分 5 个，缺 `coordination`；所得主观互赖模型仍解释 24% 的合作方差

- **判定**：`VERIFIED`（`F-C27`，含一处术语错配）
- **处置**：`ACCEPT`（引文与 6→5 结论）。**必须**删掉「（basis of dependence）」括注；两套六维命名必须择一。

### H-E5 — CLARITY 在 agreement 之外预测 commitment，并预测 9 个月内解体可能性的降低

- **判定**：`VERIFIED`（`F-C28`）
- **内容**：clarity（「作为伴侣二人中的一员，我相信我们知道自己作为一对是谁」）与实际 agreement 相关，
  **在 agreement 之外**预测 commitment（Study 2），并**预测 9 个月内解体可能性的降低**（Study 4）。四项研究：横断 1–2、实验 3、纵向 4。
- **处置**：`ACCEPT`（引文层）；修 issue 号（47(1)）；在 §6.2-B1 补一句「clarity 是 direction 变量」。

### H-E6 — 系统性 dyadic coping measure 比 discrepancy measure 更强地预测关系质量

- **判定**：`VERIFIED`（`F-C17`，443 对瑞士伴侣）
- **处置**：`ACCEPT_AS_PROPOSAL` —— 引文与方向接受；措辞改为「在 relationship quality 的预测上」。

### H-E7 — 三个「候选 ABM」名字的证伪成立

- **判定**：`JuSpace` `VERIFIED` / `smallslm` `VERIFIED` / `ASON` `PLAUSIBLE`（结论对，**检索不完整**）（`G-C19`）
- **内容**：`JuSpace` 实为 Julich 神经影像学工具箱（名字冲突，不采用）；`smallslm` 与 `ASON` 四路检索 0 命中，
  `UNVERIFIED_OR_UNKNOWN`，倾向不存在。
- **处置**：`ACCEPT` —— 可作为「不存在的候选工具」清单的样板。

### H-E8 — W3C PROV 的日期与 Recommendation 身份

- **判定**：`VERIFIED`（`G-C23`，逐字核实）
- **内容**：PROV Working Group 于 **2013-04-30** 发布 12 份文档，其中四项为 W3C Recommendation：`PROV-DM`、`PROV-O`、`PROV-N`、`PROV-CONSTRAINTS`。
- **处置**：`ACCEPT`（事实无误）；要求 `13` §12 补一处归属。

---

## F. 已知缺陷（child 直接重算或重读得出，可复现）

> **取代指针**： 见 `SUPERSEDED_REGISTER.md` 逐行指针见本表新增的 `supersession` 列；总表见 `SUPERSEDED_REGISTER.md`

这些不是「结论」，是**对 PR #31 制品本身的可复算不一致**。它们全部 `VERIFIED`，且不需要任何新证据。

| id | 缺陷 | 判定 | 独立性 | supersession |
|---|---|---|---|---|
|---|---|---|---|
| **H-F1** | `02b` §2 声明 `INDEPENDENT` = 「≥3 个 lens 有正面分离证据」；实算 6 条 `INDEPENDENT` 中 **4 条不满足**（E2=2、E11=1、E11c=2、E14=2）。同样 2-lens 的 E3 却判 `CONTESTED` | `A-C1` `UNSUPPORTED`（标签与自定规则无推导关系） | `A` 用脚本重算 21×5 单元格，未采信报告自述 | `SR-B21`
| **H-F2** | `02b` §4 边表 105 个单元格**无任何来源列**；11 条边的判定无法追溯到 `02b` 内的引用编号。**E5 与 E17 在四节中均无对应行** | `A-C4` `UNSUPPORTED` | 同上 | `SR-B21`
| **H-F3** | `02b` §6 用 `R1`–`R11` 表示「不可消去残余」，而 `PARAMETER_CONVERGENCE` §9 已用 `R1`–`R5` 表示 `Derived/Readout` 清单。**同 PR 内两套 `R` 编号语义完全不同**，且无编号空间隔离声明 | `A-C12` `PLAUSIBLE` | `A` 逐条核对 | `SR-B21`
| **H-F4** | `02b` §3.1 图例定义 `---` = 「判定为 `INDEPENDENT` 的边」，但 E1、E18（均 `CONTESTED`）都用 `---` 绘制；ASCII 另标 E3 为 `CONTESTED/mod` 而边表 E3 的 `strength` 是 `STRONG` | `A-C5` `UNSUPPORTED` | `A` | `SR-B21`
| **H-F5** | `01` §9.1 的操作性交接写「从 §7 的 **S-9（F-09 表）**开始」，而 **`01` 全文不存在任何 `F-xx` 条目** | `A-C27` `UNSUPPORTED`（该交接指令不可执行） | `A`。**这是 packet 的可执行性发现** | `SR-B21`
| **H-F6** | `02` 与 `02b` 报同一个数不同值：男性 `r=.66` / 女性 `r=.26`（`02`）vs 女性 `r=.25`（`02b`，且同时挂在两个来源上） | `A-C13` `CONTESTED` | `A` 两侧同 cluster | — （未修：仍是真冲突）
| **H-F7** | `05` §5 把 17 条「不是可回答清单」当作**单一逻辑类型**呈现 | `D-C10` `WRONG-SCOPE` | `D` | `SR-B10`
| **H-F8** | `05` §7：把 `RIx` 的方差直接写成「稳定 trait」是错的——illusory between-person component 可能**只**来自省略的 time-varying covariate | `D-C11` `VERIFIED` | `D` | `SR-B10`
| **H-F9** | `16` 把「17 条不可建立事项」与「21 条失败模式」计入已达成的交付物 | `D-C29` `UNSUPPORTED`（作为独立交付物计数） | `D` | `SR-B11`
| **H-F10** | `16:117` 称「L1–L8 是本协议的实例化」，但同时自陈「**不声称**复现 S01 的八分类（S01 图 1 确切标签未取得）」⇒ 两者不能同时成立 | `D-C28` `UNSUPPORTED`（作为「该来源不可得」的断言） | `D` | `SR-B11`
| **H-F11** | `05` §1 的「45% 的文献用两波拟合 CLPM」与「89% 尺度看似有效、4% 全面评估后」两条被并列引用，但后者的语境（Orth 2021 / Hussey & Hughes）未开 | `D-C38` `PLAUSIBLE` | `D` | `SR-B10`
| **H-F12** | `07` §5 开篇写「以下 **15 条**是候选可检验不变量」，但 §5.1 给 I1–I15、§5.2 给 I16–**I19**，合计 **19 条**；§13 也写「给出 19 条」 | `E-C12` `VERIFIED`（缺陷确认） | `E` | `SR-B12`
| **H-F13** | `07` 的证据等级约定（`:8`）只定义 6 个等级，但正文 **15 处**使用 `[ESTABLISHED]` | `E-C13` `VERIFIED` | `E` | `SR-B12`
| **H-F14** | `07` §5 的 19 条中，`I14` / `I17` / `I18` **不可执行**（判据含 `07` 自己拒绝给值的 `θ`、未定义的 coverage 阈值、需成本模型而项目明确不冻结分数）；`I19` **空过**（任何非恒定函数都满足） | `E-C11` | `E`。「9 条现在就能检查」这一计数 `REJECT` | `SR-B12`
| **H-F15** | `07` 与 `08b` 在同一 PR 内**各自发明一套平行编码**（缺失性/不适用性/冲突/不可寻址的分区），零协调，且存在**三处同名不同义**：`disputed`（07 缺失机制）vs `disputed`（`CURRENT_ARCHITECTURE.md:315` fact status）vs `Divergent`（08b 主体立场对立）、`reporter_role`（07）vs `Role`（canonical）。直接并入会得到 14+ 值枚举，违反 `AGENTS.md:22`/`:24` | `E-C23` `VERIFIED`（重叠存在且未被协调） | `E`。**但**「08b 的存在性结论是对 07 的独立佐证」不成立——`08b` 未读 `07` | `SR-B12`
| **H-F16** | `10` §5 的 test table 与 §6.3 / §7 / §8 之间存在同义与双重计数（多处由报告**自己**的交叉引用证实） | `F-C30` `VERIFIED` | `F` | `SR-B11`
| **H-F17** | `09` §0 第 1 条（headline）：「**不存在**可与 LHRM 对象直接比较的既有关系 ABM」；而 §1 写「通过 C5 的：**本 lane 未找到任何一个**」 | `G-C17` `WRONG-SCOPE` | `G` | `SR-A14` · `SR-B8`
| **H-F18** | `13` §12 判定其 `Observation / Belief / Environment` 分层的外部证据「**基本为空**… **0 条外部文献**。这是 LHRM 独有结构」；而 `12` §8 `I8` 判定 Concordia 的 GM/player 分离「在结构上**等价于** LHRM 的 `Reality != Observation != Belief` 分层」 | `G-C25` `CONTESTED`（cluster `G` 内部） | `G` | `SR-B15`
| **H-F19** | `13` §2.2(c) 标题「LLM 的一致性是『对齐多数派先验』，不是『更准』」，但转述把来源的结论方向讲反——`13` 自己引的发现 3 就是该转述的反证 | `G-C28` `WRONG-SCOPE` | `G` | `SR-B15`
| **H-F20** | `13` §13.2 主张六项指标「在冻结 fixture 上**完全可机器判定**（因为 fixture 本身是冻结的、有明确 `fact_status` 与 `source_anchor`）」；但被抽取的文本与判定 gold 是**同一批文本的同一批标签** | `G-C29` `WRONG-SCOPE`（对自己的 gold 不施加循环论证标准） | `G` | `SR-B15`
| **H-F21** | `12` 记录了三条对 LHRM **已有 canonical 决策**的独立外部佐证，但三条全部只出现在 §2.1 / §8（作为「可复用想法」），**从未进入 §10 的裁决** ⇒ 在该报告的最终结论里权重为零 | `G-C26` `VERIFIED` | `G` | — （权重发现，未修）
| **H-F22** | `14` §9.1 与 §9.2 的两项「最高优先未核实 prior art」极可能都是**不存在的引用**：`Acitelli & Antonioni (2006)`（JPSP 90(6)，Crossref 该期无此文，真人姓氏是 **Antonucci**）；`Boyd & Heewer (2007)`（Crossref `query.author=Heewer` = **0 results**） | `H-C24` `UNSUPPORTED` + `H` 的专项 9.1-1/2 | `H` 与 `L-C20` **各自**查了不同的一半（`H` 查 Crossref 该期；`L` 指出 Heewer 极可能是第三作者，且正确项应为 **Boyd & Hilton (2007), *The law of the wed*, Cognition**）⇒ `PARTIALLY_INDEPENDENT`。**这两项被列为「决定新颖性判断的最大单一变量」却零证据** | `SR-B14`
| **H-F23** | `14` §2.5 + F-6 + F-16 用 Lalk et al. (2025) 证明「LLM 抽多类语义的上限是 κ=.42」——**原文是** GoEmotions 28 类公开数据集 → 翻译德语 → fine-tune 预训练 LLM → 应用于 reddit 心理治疗评论；且该数据集的**人类标注一致性本身就是 κ=.331–.468**，模型的 .42 **达到而非低于**天花板 | `H-C26` `WRONG-SCOPE` | `H` | `SR-B14`
| **H-F24** | `17` 的 S 编号体系（`S1`…`S29`）无法从其 §12 引用清单解析 | `I-C14` `VERIFIED` | `I` | — （未修）
| **H-F25** | `17` 的 Gate B 覆盖表枚举不完整：含 1 个非 Gate B cell（`work colleague`），漏 2 个真 cell（`opposite-sex`、`non-kin`） | `I-C8` `VERIFIED` | `I` | `SR-A22` · `SR-B15`
| **H-F26** | `17` §4 表实际裁定分布是 `CHALLENGED 12 / CONTESTED 6 / UNCHALLENGED 3 / NO_EVIDENCE 2`（23 条） | `I-C15` `VERIFIED` | `I` | `SR-B15`
| **H-F27** | `17` §12 line 549 的「所有卷期页均经 Crossref API 核验」这一**总括声明**不成立 | `I-C30` `VERIFIED` | `I` | `SR-B15`
| **H-F28** | `VALIDATION_CORPUS_V0_1.md` 的「Recommended Fixture 001–003」已被实际冻结的三个 fixture 取代 ⇒ **canonical 内部存在未更新的文档级冲突**（已发生过，不是假设） | `I-C12` `VERIFIED` | `I` 自己做的 git + SHA + grep；两份报告都靠读文件而非索引躲过了它 | `SR-A18`
| **H-F29** | `04` D12 命名为「**Add Health (NLSY97/ECLS)**」 | `C-C20` `CONTESTED`（事实误标 + 报告内部矛盾） | `C` | `SR-B9`
| **H-F30** | `04` D08 断言「**配偶关系质量是单方报告**……→ `Z[i→j]` 与 `Z[j→i]` 在 NSFH 中不可分离」，依据是 **Wave 1 的一句问卷描述** | `C-C35` `CONTESTED` | `C` | `SR-B9`
| **H-F31** | `18` 使用了两个从未定义的编码命名空间 `CR-x` 与 `NR-x`；`CR-1/3/4/6/7/8` + `NR-1/8` 共 8 个码在 `18` 自身没有登记表，其中 5 个被 §10 的 `NARROW_REPAIR_REQUEST` 当作**理由码**引用 | `K-C11` `UNSUPPORTED` | `K` | `SR-B17`
| **H-F32** | `19:353` 的方法学缺口第 3 条（「`02b` 依赖 `R04`/`R06`」）是错的：`02b` **零**引用 `R04`/`R06`（全文正则计数 `R04`=0 `R06`=0 `pairfam`=0 `APES`=0 `DVA`=0 `BMR`=0） | `K-C12` `VERIFIED` | `K` 用机器可复算的正则计数。**这是 `19` 唯一的硬事实错误，且它在「诚实记录自身缺口」的段落里** | `SR-B17`
| **H-F33** | 「`Unknown` 值类被**五**个 lane 各自重新发明」中的计数**偏低**：语料中至少存在**第 6 套**「无值」词表 `UNKNOWN_AS_OF` / `DOI_UNKNOWN_AS_OF_2026-09-27`，且它是**全语料使用最广**的一套 | `K-C7` | `K` | `SR-B17`
| **H-F34** | `19` §8 有 **B-1…B-8**（8 项）；`00_MANIFEST` §4 有 **B-1…B-9**（9 项）；两者对 **B-3** 指不同事物；且 manifest 自身对「全局去重」同时使用 **B-3**（§4）与 **B-9**（§4 末）两个编号 | `L-C18` + `ADJ3` Q7/Q8 独立核实 | `L` 与 `ADJ3` **各自**读两份 register 并逐项比对，结论一致 ⇒ `INDEPENDENT` | `SR-A13` · `SR-B17`
| **H-F35** | `19` §7 抬头「**全部**为 AI 推荐…**均**不属本 Work Order 授权范围，需 Human 授权后另行派发」把**两种不同性质**的批准混为一谈：**(a)** 因 canonical mutation 需 Human 主权批准（N1/N2/N3/N4-冻结部分）与 **(b)** 仅因 Work Order 边界而需新派发（N5-前半/N6/N7/N8） | `K-C44` `WRONG-SCOPE` | `K` 读了 `19` §7 全部 8 条的变更面 | `SR-A13`
| **H-F36** | `19` §7 自报排序依据是「修起来便宜 / 收益大」，但实际排序（canonical 最贵的 N1 打头，最便宜的 N8 垫底）遵循的是**架构依赖**，不是成本/收益 | `K-C45` `UNSUPPORTED` | `K`。`ADJ3` Q7 独立得出同一结论并补充：N1 的**编辑工时**确实最低，真实排序依据是「**依赖解锁序**」 | `SR-A13` · `SR-B17`
| **H-F37** | `lhrm` 仓库只有 `AGENTS.md`、`README.md`、`docs/`；**无 runner、无 CI、无 metric 实现、无 schema 文件** ⇒ `19` §7「修起来便宜」对文档编辑成立，对「重跑 Fixture 001」不成立 | `L-C7` `VERIFIED` | `L` | — （未修）
| **H-F38** | Fixture 003 把验证 schema 钉在 `f237784`（`CURRENT_ARCHITECTURE + PARAMETER_CONVERGENCE + CONSTRUCT_SCOPE_DIRECTIONALITY @ f237784`）⇒ WO-N1 一旦落地，**所有在改动前产出的 mapping 计数都不可与之后的结果比较** | `L-C9` `VERIFIED` | `L` | — （未修）
| **H-F39** | `19` §8 的 B-1…B-8 与 §2 的 C-1…C-8 **只有 `B-6 ↔ C-3` 一项对应**；`C-1`/`C-2`/`C-4`/`C-5`/`C-6` 在 §8 无编号，反向 `B-1`/`B-2`/`B-5`/`B-7`/`B-8` 在 §2 不是「阻塞级」⇒ **两份 register 不是「编号错乱」，是「分母不同」** | `ADJ3` Q7 | `ADJ3` 逐项核实。`L-C18` 抓到编号冲突但**未抓到成员不相交**——后者更难修 | `SR-A13` · `SR-B17`
| **H-F40** | Fixture 001 的 core dyad 是**雇主↔雇员**（`Miss Z. Carty <-> her 2020 line manager`），其 26 个原子事实是排班/停业/未付薪/CAB/申诉等**机构性事实** | `L-C11` | `L` 直读冻结 substrate。**这使 WO-N1 的被检验对象成为开放问题**（见 X-9） | `SR-A11`

---

## G. 独立性坍缩（`ADJ3` Q6 — 12 条 robust agreements 的重判）

> **取代指针**： 见 `SUPERSEDED_REGISTER.md` §SR-A10（adjV1 `X-8` 要求改用 `independent_sources × methods`）

`19` §1 的 12 条「robust agreement」经独立性审计后：**5 条存活、5 条降级为单源收敛、2 条必须移出**。
「12」应读作「5 + 5 + 2」。完整重判表见 `CONTESTED_FINDINGS.md` X-8；此处只记**独立**的两条最重发现：

### H-G1 — 「最大预注册研究结论逆向于工程优先级」是 1 篇 study 被 4 个 lane 转引

> **取代指针**： 见 `SUPERSEDED_REGISTER.md` §SR-A10 · §SR-B2（`r3/a2` S15：1 study × 4 = 3 转引 + 1 独立复核）

- **判定**：`ADJ3` 独立裁定（原 `A6`）
- **内容**：`R06` / `R14` / `R16` / `R17` 四个 lane 全部转引**同一组数字**（43 数据集 / 11,196 对 / ≤45% / ≤18%），来自 **Joel et al. 2020, PNAS** 一篇。
- **独立性**：**零**。`K` 未 flag 此项，`ADJ3` 首次标出。
- **处置**：`19` 的 Lanes 行必须从「4 lane」改为「**1 study**」；保留 `19:76` 的「这只是 population-level 方差陈述」限定。

### H-G2 — 「有向性在测量层被确认」是 1 个 instrument 台账 + 2 处转引

> **取代指针**： 见 `SUPERSEDED_REGISTER.md` §SR-A10

- **判定**：`ADJ3`（原 `A2`）
- **内容**：`r=.43` / `r=.11` / `r=.18 vs .90` 三组数**全部来自 `R03` 的 instrument table**；`R01`/`R02` 大概率转引同一批 primary study。
  **收敛发生在 study 级，不在 lane 级。**
- **处置**：改述为「1 个 instrument 台账 + 2 处独立转引」，**不得**称 3 lane 独立收敛。
