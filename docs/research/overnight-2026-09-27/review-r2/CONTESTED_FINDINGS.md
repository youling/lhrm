# CONTESTED_FINDINGS — Round 2 review swarm over `youling/lhrm#31`

> 本文件收录**两侧都有可信证据**、或**本 swarm 内部给出不相容断言**的命题。
> `REVIEW_CONTRACT.md` §4：`CONTESTED` 必须指名对立方与其指针。**parent 不做调和**——
> 阶段 1（lane A–L）与阶段 2（ADJ1–3 / EV1–3）之间的分歧、阶段 2 之间的分歧，一律原样进入本文件。
>
> 每条给出：`id` · 命题 · 对立读法（各带指针）· 阶段 2 裁决及其**适用范围** · 残余不确定性 · 谁能裁决。

---

## X-1 · `PPR` / `Satisfaction` 层归属（「三方互斥」之争）

**命题**：`19` §1 C-1 与 `18` CF-03 把 `PPR` 的处置写成「**三方互斥**」（R01 判 `BELIEF_ONLY` / R06 给 null 判据前提 / R14 给优先级表条目 / R17 判应升为一等状态层）。

| 读法 | 来源 | 断言 |
|---|---|---|
| 三方互斥 | `18:105-116`、`19` C-1 | 4 个 lane 给出 3 种互斥的层位处置 |
| 形态上不精确 | `K-C2` | 4 个 lane 里**只有 2 个**给出本体层位主张；R06 给的是 **null 判据的前提**，R14 给的是**优先级表条目**，二者都不是「层位处置」 |
| 漏了 5 个 lane | `K-C3` | CF-03 漏了 5 个触碰 `PPR` 层位的 lane，其中 **R11 与 R03 独立支持 R01 的 `BELIEF_ONLY`**；R00 记录了 **canonical 内部自身**的分歧（`SCIENTIFIC` §7.8 vs `PARAMETER_CONVERGENCE` §5 B1） |

**阶段 2 裁决（`ADJ1` Q1）**：`MOOT`（对「三方互斥」这一表述本身）→ 代之以**逐 lane 枚举**。
`K-C2` 与 `K-C3` **survive**；`18`/`19` 的「三方互斥 / 三种互斥处置」标签 **does not survive**。
`ADJ1` 另给出一条**对 `K` 是新信息**的已核实事实错误：`18:114` 写「R01 同时持有『PPR 是上游生成器』和『PPR 是下游 belief』两种读法，其 §3.12 **未调和**」——
`ADJ1` 读了 `02:258` 与 `02:260`，`02:260` **明确调和**（「[S33] 同时把 PPR 定位为 trust 与 commitment 的上游生成器（mutual cyclical growth），这进一步说明它应当是一个独立的 belief 变量」）。
⇒ **`18:114` 的「未调和」是误读，而它是 `18` 判定 R01 立场偏弱的唯一理由。**

**必须同时记录的两点**：
1. **canonical 自身在 `PPR` 层位上不一致**（`R00:S-I`）——这比任何 lane 间冲突都更靠前。
2. 「测量层冗余与层位正交」只在 `02b` 语境下成立（E5 的 `F` lens 判「✓失败」、判定限定在 `@ measurement`）。
   **若 Gate C 后续把 `Trust`/`PPR` 的测量冗余用于层归属，则正交性失效。这本身是一个未登记的耦合。**

**残余**：**没有实验能单独定层**。能定的是「`PPR` 是否有 state 性质」（见 `NEXT_EXPERIMENTS.md` E-3）；
即便该实验成立，仍需**额外前提**「时间在前的自陈量 = state」，而这个前提本身未被任何 lane 检验。

**裁决者**：Architect（层归属是架构裁决）+ Human（若要动 `§5 B1`）。

---

## X-2 · `17` F3 的层边界主张

**命题**：`17` F3 = 「**LHRM 的层边界被经验文献反向排序**」（`PPR` 应升为一等状态层 / `Satisfaction` 不应是 Derived）。

| 读法 | 来源 | 断言 |
|---|---|---|
| 反向排序成立 | `17` F3 / `A03` 改写 4 | 文献显示 `PPR` 应升、`Satisfaction` 应降 |
| `WRONG-SCOPE`（lane I） | `I-C17` | 「层被反向排序」是**待检验的竞争假说**，不是发现；`A03` 改写 4 应改为**双分支竞争假说登记**形式 |
| `WRONG-SCOPE` + **前提误述**（阶段 2） | `ADJ1` Q2 | 核心成立，但两处子命题被推翻（见下） |

**`ADJ1` Q2 裁决**：`RESOLVED_FOR_FACT`。(R-b) survives；(R-c) **新增成立**；(R-d) 部分成立（形式对，但 F3 本身不因此被救）。
**`F3` 的层边界主张 = `WRONG-SCOPE`；且其前提是对 canonical 的误述。**

**`ADJ1` 独立提出的三条理由（`INDEPENDENT`，本 packet 首次提出，未见于 A/I/K 任一 packet）**：
- E3：`CURRENT_ARCHITECTURE.md` §6 **已把 `Belief` 置于转移函数的一级 co-input** ⇒ `17:100`/`:373` 的「LHRM 把 Belief 当成 state 的下游」在 canonical 中**不存在**，须删。
- E4(ii)：Joel et al. 2020 的**纵向负结果**独立成立。
- E2：来源的构念名本身就是 perception。

**`ADJ1` 要求的三项处置**：
1. **删除前提**（`17:100`/`:373`）。
2. **重标主张**：`17` §3 F3 / §1.3(1) / §5 R2 / §11 建议 1 的**层位部分**改标 `WRONG-SCOPE` + `UNVERIFIABLE_AS_WRITTEN`；把 Segal & Fraley 的因果发现**保留**为 dynamics evidence。
3. **不实施 R2 退守**：在层归属被**单独**重裁前，不得把 `Belief < DirectedRelationshipState < Derived` 的层排序改动排入 work order。

**`ADJ1` 明确保护 canonical**：本裁决**保护** `PARAMETER_CONVERGENCE` §5 B1（`:249-275`）与 §9 R3（`:489-495`）**不因 F3 而改动**。
若 Architect 因其它理由要动 B1，那是独立议题，**不得以 F3 为依据**。

**必须注意的独立性陷阱**：`17` F3 的三条来源是 `SAME_SOURCE` 内部三条；`16:475` F-SELF20 对 F3 的「独立确认」是 `NON_INDEPENDENT`（`16:571` 自陈转述 R17 packet 1）。
`A03` 改写 4 自陈「**不新增任何实证要求**」（`A03:666`）⇒ **它不能被算作对 F3 的反证，也不应被算作 F3 的替代表述已获支持**。

**裁决者**：Architect（是否登记为双分支竞争假说）。

---

## X-3 · `§4 D7` 与 `§9 R3` 是否逻辑上不能同时成立

**命题**：`I-C23` 主张 `17` T1 + F3/A21 合起来蕴含一个二选一：若 `Dedication` 由 (satisfaction, alternatives, investment) 决定，则 `§4 D7`（primitive）与 `§9 R3`（Satisfaction=DERIVED）不能同时成立。

| 读法 | 来源 | 断言 |
|---|---|---|
| 逻辑强制二选一 | `I-C23` `VERIFIED`（逻辑） | D7 与 R3 不能同时成立 |
| 二选一**被推翻** | `ADJ1` Q3 | (R-a) **does not survive**（逻辑强制力不成立）；`I-C23` 的 `VERIFIED` 与「二选一」处置**均被推翻** |
| 让步形式存活 | `ADJ1` Q3 (R-b) | `I-C23` 自身的让步是唯一正确形式；`I-C23` 揭示的 **facet 切点** 是 |

**`ADJ1` Q3 裁决**：`RESOLVED_FOR_FACT`。**冲突形式：否**（是记账/文档层级问题）。**残留的 facet 切点：是**（即 `02b` U4 + `18` CF-05 的 facet 分配表）。

**`ADJ1` 要求**：
1. **驳回** `I-C23` 的「§4 D7 或 §9 R3 二选一」处置（**无二选一可做**）。
2. 要求 `17` T1 在被引用前先过仲裁（其「方程定义」读法是本条全部张力的前提）——**`ADJ1` 明确声明未审 T1**。
3. 要求 `02` §3.8 撤回「canonical 内部不一致」表述，改用其自己 §4（`:275`）的版本。
4. 要求 canonical 在 §9 R3 `:495` 追加一句**后果预登记**：「若本判据成立并提升 Satisfaction，§4 D7 的 basis 地位与 §11 的 8 项 basis 需重新审议；本条只登记后果，不预设结论。」

**独立性**：`I-C23` 的逻辑步骤 `INDEPENDENT`（lane I 自构造），**但条件于 `ADJ1` 未审的前提**。
`A-C25`(a) 的 canonical 侧：`A-C25` 自标 `VERIFIED_BY_ME`，`ADJ1` **独立复核**了 D7 `:224` 与 R3 `:489-495` 两段原文，结论一致 ⇒ 该侧 `INDEPENDENT`。

**残余**：`[S05]`（Overall/Fletcher/Simpson 2010, `10.1177/0146167210383045`）**未被任何一方独立核实**。
`ADJ1` 明标：若该事实前提为假，本条整体变 moot。**`A-C25` 与 `ADJ1` 均 `NOT_OPENED`。**

**裁决者**：Architect（是否加后果预登记）+ 取样复核（本轮最需要的下一处外部取样之一）。

---

## X-4 · `Trust` 的层级与 `domain` 强制条件

**命题**：`A-C19` = `02` §3.4 判 `Trust` = `KEEP` + **强制 `domain` 索引**（「13 个候选中最稳的一个」）；
`02b` §5.1 + MGS-C 判「`Trust` 与 `AttachmentSecurity` 不是两个独立 primitive」，把 `Trust` 降为部分 facet。

| 读法 | 来源 | 断言 |
|---|---|---|
| 真冲突 | `A-C19` `CONTESTED` | 两侧给出不相容的层级结论 |
| **artifact** | `ADJ1` Q4 | 「冲突本身：独立性 = 0」——单 lane、同两文档、同源族。是 section-type 误读 |
| 残留开放 | `ADJ1` Q4 | `FeltSecurity` facet 切点 `GENUINELY_OPEN` |
| `domain` 强制 = `WRONG-SCOPE` | `A-C21` + `ADJ1` Q4 | **`A-C21` survives**，`RESOLVED_FOR_FACT` |

**`ADJ1` Q4 拆分裁决**：
- facet 切点（`FeltSecurity` 归属）：**`GENUINELY_OPEN`**（= `02b` U4）
- **`domain` 强制条件**：**`RESOLVED_FOR_FACT`** —— **`A-C21` survive（`WRONG-SCOPE`）**
- 架构侧无数据部分：**`RESOLVED_FOR_RULING`** —— 可立即裁定

**`ADJ1` 的两条独立复核路径（均强于 `A-C21` 所用）**：(i) Crossref 题名逐字；(ii) **`02:158` 自己的引文是工作场所例子**。
`ADJ1` 另发现 scope 缺陷**不限于 `Trust`**：`02 §3.9`（`:218`）对 `OutcomeDependence` 写「**必须 domain-indexed（同 Trust）**」——
**其依据仍是同一条 organizational 来源**。

**`ADJ1` 给出的可立即执行处置（不需新数据）**：
1. **`REJECT`「强制 `domain` signature 字段」** —— canonical §4 D4 本轮不新增 `domain` 必需字段。替代：`domain` 作为**推荐 facet + 记录缺省值**，并登记为「待 invariance 检验」。
2. **`ACCEPT_AS_PROPOSAL`「`Trust` 增加一个具名 `FeltSecurity` facet 槽位」** —— 纯 schema 决定，解除 Gate C 的解释阻塞，**代价为零**。
3. **`HOLD_FOR_EVIDENCE` facet 切点**（`02b` U4）。**在 U4 前，禁止 MGS-C 的整体 `Trust` 降级（`02b:503`）被当作结论引用。**
4. 要求 `02` 修正 §10 页码（343-356 → 344-354）。

**`ADJ1` 明确的一条硬约束**：M1 与 M2 **都不判「`Trust` 是否该降为 `AttachmentSecurity` 的 facet」这一层问题** ——
那只能由 Architect 在 M1/M2 之后裁定，**或按上述第 2 项先做无数据部分**。

**裁决者**：Architect（第 1、2 项可立即签）；`FeltSecurity` 切点需 E-2。

---

## X-5 · 值类集合的封闭性（lane `G` vs `EV3`）— **本轮分歧最大的一处**

**命题**（`G-C5`，lane `G` 判为**唯一必须落到 canonical 而不能停在 proposal** 的发现）：
`11` §3.1 论证 `SexualDesire × {友谊,兄弟姐妹,亲子,敌对} = NA` 是**值类缺口**；正确值既不是 `Unknown` 也不是 `0`；
而现有值类集合里没有这一格 ⇒ **唯一的合法表示方式就是把不适用填成 0 或 Unknown —— 正是 `AGENTS.md` 禁止的动作** ⇒ **逻辑矛盾，不是经验问题**。

| 读法 | 来源 | 断言 |
|---|---|---|
| 逻辑矛盾 / 无合法表示 | `G-C4`、`G-C5`（`VERIFIED`，「我**独立地**用 canonical 文本复现了」）、lane `G` 自己的 `top_recommendations` 第 2 条 | 值类集合是穷举的且无「不适用」⇒ 存在一个坐标其正确值不在集合内 ⇒ U1…U12 任何实验都无法裁决 ⇒ 必须 durable |
| **`REFUTED`（对整体框架）** | `EV3` Claim 1 | 值类清单是**许可式而非封闭集**（`可以` / `may be`；两份清单互不一致；全库无封闭性声明）；且 canonical **已有一个具名槽位** `BoundaryRule_(A,B,domain)`（`PARAMETER:359-367`，`KEEP as Constraint/Agreement`）与一个针对 `性欲` 的 **worked example**（`CURRENT_ARCHITECTURE:190`「更接近 Agent boundary / constraint，而不是『性欲为零』」）承接该语义 ⇒ **不存在逻辑矛盾** |

**`EV3` 的检索证据**（全部 `VERIFIED_BY_ME`，全文逐行）：全库检索 `穷举|closed set|仅限|只允许|exclusive|不适用|not applicable`
于 `docs/foundation/*.md` + `AGENTS.md` ⇒ **唯一命中**为 `PARAMETER_CONVERGENCE_V0_1.md:343` `exclusive romantic partners`（关系标签，**不是值类封闭性声明**）。
并反驳了「`PARAMETER_CONVERGENCE` 是 `CANDIDATE / NOT FROZEN`（`:3`）所以不能当作现有合法表示」的抗辩：
`CANDIDATE` 指**参数值**未冻结（`:9`），**不指** schema 的落点集合未定义；§13 的 10 个落点是 schema 层，`:631-637` 明确它是诊断入口。

**`EV3` 的残余内核**（**这才是本条留下的东西**）：
**canonical 缺少一个正式位置来登记「某构念在某 dyad-type 上不具独立语义」这条负面知识**——目前只能写在报告正文里。
`EV3` 对该残余判 **`PLAUSIBLE`**。

**`EV3` 自陈的最强反证（对自己）**：
(a) `CURRENT_ARCHITECTURE:190` 的 worked example 案例是**未婚夫妻**，非 sibling；论证不依赖同构 case（它依赖 (i) `constraint` 是合法值类、
(ii) 边界/规则类事实归 `Constraint/Agreement` 落点、(iii) 不得写成「欲望为零」；`PARAM:359-367` 的 `BoundaryRule_(A,B,domain)` 是 `domain` 索引的通用槽位）。
(b) 若某 sibling dyad 确实存在被记载的性欲坐标，则 `NA` 判定本身错误——**这会同时推翻 G-C5 与 G-C11 的前提**，但不改变通道 1/2/5 提供的合法表示仍存在。
(c) 「许可式 ≠ 封闭」是本 verdict 中**最依赖解释力**的一环；**若 Architect 裁定为封闭集，则本条需重审**。

**parent 处置**：
- **`G-C5` 的原主张进入 `REJECTED_OR_WEAK_FINDINGS.md` R-G1**（被 `EV3` `REFUTED`）。
- **残留项以缩小形式进入 `CANONICAL_CHANGE_PROPOSALS.md` C-P5**（`PLAUSIBLE`，`RECLASSIFY_AS_METHOD_LIMIT`）。
- **不得**因 `G` 判 `VERIFIED` 且 `EV3` 判 `REFUTED` 就取「更严的一方」——这是两个不同问题（**是否存在逻辑矛盾** vs **是否缺登记位**），
  `EV3` 只推翻了前者。
- `G-C11`（`NA` 判定本身）判 `PLAUSIBLE`，最强反证未处理 ⇒ 一并 `HOLD_FOR_EVIDENCE`。

**裁决者**：Architect（值类清单是许可式还是封闭集——这是**唯一的裁决点**）。

---

## X-6 · `B2` null（lane `D` vs `EV3` vs `ADJ2`）

**命题**：`16:203` 的 `B2 = SELECTION_ONLY`（稳定 per-dyad 截距、无 wave-to-wave 增量）被称为「**本协议认为最重要的一条 null，因为它已经击败过一个候选**」。

| 子命题 | `D-C19` | `EV3` Claim 2 | `ADJ2` Q2 |
|---|---|---|---|
| 2a `B2` 被 `B1` 严格支配，「配对击败 B1 与 B2」的判定规则冗余 | `VERIFIED`（`WRONG-SCOPE` 的一部分） | **`VERIFIED`**（纯逻辑，零来源依赖） | **`VERIFIED`**（自证 `16:202` vs `16:203`） |
| 2b `B2` 不是 Lavner 实际检验的模型 | `VERIFIED` | **`VERIFIED`**（摘要逐字） | `VERIFIED` |
| 2c 「已核实证伪 / already empirically falsified」是对来源的误述 | `VERIFIED` | **`VERIFIED`**（摘要 + Table 5 逐字） | `VERIFIED` |
| 2d `16` 的 `B2` 与 `06` 的 `SELECTION-ONLY` 是「同名不同模」 | `VERIFIED` | **`IMPRECISE`** —— 若 `16:203` 的「无 wave-to-wave 增量」= `06:488` 的「只起点，无 slope」，则 2d **完全错误**，`D-C19` 第 (1) 条应撤回 | 判为**三重缺陷**之一，主张**改名**为 `B2_LEVEL_PLUS_RW` 并采用 `06:488` 的「随机游走」定义 |

**`EV3` 对 `D-C19` 的关键反驳**：`16:203` 对 Lavner head-to-head 的**描述逐字正确**——
`initial-differences 击败了 incremental-change` ✓、`衰退集中在起点低的人身上` ✓、`最严重的一群是起点最低的子集` ✓、
`对 incremental-change 模型只有 "limited evidence"` ✓。
**`D-C19` 的问题不是「描述错了」，而是「从正确的描述推出错误的推论」。这是一个更细的批评，而 `D-C19` 的措辞把批评落错了位置。**

**`ADJ2` Q2 裁决**：`D-C19` = `VERIFIED`（三处全对），**且 D 低估了严重性**。`ADJ2` 加了第四处（Lavner Table 5 的 −1.31 / −1.05, p<.001），
并**修正 D 的重定义方案**（要求改名 + 从主判定清单降级 + 改写 rationale + 新增 2 个 null + 删 3 处措辞）。

**parent 处置（取三方交集，不取最严）**：
1. **必须做的**（三方无争议）：删掉「最重要」与「已经击败过一个候选」与「已核实证伪」三处措辞；
   把 rationale 换成 Lavner 的**实际**发现逐字：「起点值对轨迹组的区分力强于所测风险变量的变化率」，并注明它讲的是 **predictor 变量**，不是 outcome 的人内斜率。
2. **2a 必须落地**：把 `B2` 从 `16:197` 的「配对击败 B1 与 B2」中删除（被 B1 支配 ⇒ 冗余），改标 `B2_DIAGNOSTIC`。
   **但保留 `EV3` 的抗辩空间**：若 `B1`/`B2` 的**报告指标**不同（例如 `B2` 报方差成分分解），则配对检验在**报告层面**仍有意义。
   `EV3` 自陈**未读 `16` §7.1**。⇒ **这是唯一需要 Architect 读一行原文才能定的子点。**
3. **改名与否 = `CONTESTED`**：`ADJ2` 要求改名（认为「同名异义」是 PR 内最危险的一处记账缺陷）；
   `EV3` 认为 2d `IMPRECISE` 且该支点脆弱。**parent 不裁定**，登记为待决（见 `CANONICAL_CHANGE_PROPOSALS.md` C-P10）。
4. **两侧一致同意新增**：`N7_UNDIRECTED_SCORE`（唯一直接测本项目中心表示主张的 null）与
   `N8_LEVEL_CONDITIONAL_SLOPE`（唯一能真正测 DVA 交互的模型）。
5. **成本**：`ADJ2` 判「这是全 PR 最便宜的一处修复」——改一张表的两个 id、一个 rationale 单元格、三处措辞。

**裁决者**：`ADJ2` 声明**不需要外部取样复核**；但残留 `06` N1 原文与 `16` §7.1 两个文档级缺口（`EV3` 未覆盖）。

---

## X-7 · Fixture 003 的权利边界是否被违反

**命题**：`13` 在六处实质使用 `FIXTURE_003` 的 transcript 单元与 freeze rules，**全文不记录**该 fixture 的
`pointer_only` / `ai-train=no` / `GPTBot Disallow` 边界。

| 读法 | 来源 | 断言 |
|---|---|---|
| 边界存在，遗漏存在 | `G-C22` `VERIFIED`（穷尽检索）；`J-C16` `VERIFIED` | 边界是真实的，遗漏是真实的 |
| **是否构成违反 = 无权裁定** | `J-C17` `CONTESTED`（`J` 自陈「我无权裁定」）；`L-C10` `HOLD_FOR_EVIDENCE` | Fixture 003 带 `rights_policy=HUMAN_REVIEW_REQUIRED`、Eye 侧 `POINTER_HASH_ONLY` fail-closed、`robots.txt` `Content-Signal: ai-train=no` + `Disallow` GPTBot/ClaudeBot/CCBot，**且其 canonical 页 URL 在 2026-09-14 实测 404** |

**parent 处置**：**边界存在 = 高置信**（进 `HIGH_CONFIDENCE_FINDINGS.md` H-B7）；
**是否构成违反 = Human 权利裁决**，本 swarm 不裁定（`REVIEW_CONTRACT.md` §3：不绕过 rights）。

**裁决者**：Human（权利）+ Architect（若 canonical 页 404 需重新定位 fixture 记录）。

---

## X-8 · 12 条 robust agreement 的独立性（`ADJ3` Q6 重判）

`19` §1 的「12 条 robust agreement」经逐条独立性审计后：**5 条存活、5 条降级、2 条移出**。
**「12」应读作「5 + 5 + 2」。**

| 新 id | 主张 | `19` 原 id | 独立来源 | 方法 | 强度上限 | 必改之处 |
|---|---|---|---|---|---|---|
| **N-A1** | `OutcomeDependence` 理论地位最硬、测量地位最薄；关系层级无可用工具 | A3 | **3**（R01/R03/R16） | 3 | `empirical` | 无 |
| **N-A2** | 无坐标同时具备「有向边 + 特定 j + state 层 + 第二条独立观测通道」 | A4 | **3**（R03/R16/**R04**） | 3 | `empirical` | **删 `A02`**（类目错配）、**补 `R04`** |
| **N-A3** | 「完全公开 + 双报告 + 方向性 + 多波 + 关系状态构念」四条件交集为空 | A5 | **2**（R04/R05） | 2 | `empirical` | R16 标为 `dependent (JOIN_LANE: R04)` |
| **N-A4** | 生理同步不能作 pair-level 关系的代理 | A7 | **2**（R03/R09） | 2 | `empirical` | R10 标为「未主张」 |
| **N-A5** | 迟滞在二元关系数据上的存在性未知，且其必要前提在多数真实 dyad 中不成立 | A9 | **2**（R09/R06） | 2 | `empirical`（负结果） | 无 |
| **N-A6** | `PPR` / `Satisfaction` 的层归属被经验文献**逆向排序** | A4 / R17-F3 | **1**（Joel 2020 + Segal & Fraley 2016） | 2 | **`CONTESTED`** | **必须双分支登记**；`17` 的 F3 推理含 `WRONG-SCOPE` |
| **N-A7** | 项目在 refinement/单调性/预序/数学格上空白；`Unknown` 值类被 **4 条 lane 独立重发明** | A8 | **5**（R07 诊断 + R11/R13/R15/R16 重发明） | 5 | `structural` | **A02 标为 dependent auditor**；lane 数**不是 5 也不是 7**（A02 自身 CF-12 记 5、G-06 记 7），**须先 reconcile** |
| **N-A8** | 现有验证门在当前定义下**不能产生否决**；`MAPPING_FAILURE` **类型上不可达** | **A1 + A10 合并** | **1**（`PARAMETER_CONVERGENCE` §13/§14/§15）+ 1 镜像（`AGENTS.md:62`） | 2 | `methodological` | **合并两条**；删「`MERGE`/`REJECT` 从未签发」；catch-all **3→4**；指针 `§14 Step 3`→`§14:679` + `§15 Gate A step 3` |
| **N-A9** | 有向性在测量层成立，但确认出的是**逐构念**的不对称度 | A2 | **1**（R03 instrument 台账） | 3（1 独立 + 2 转引） | `empirical`（带来源共享限定） | 改述为「1 台账 + 2 转引」；**不得**称 3 lane 独立收敛 |
| **N-A10** | 领域最大规模预注册研究的结论**逆向于**当前工程优先级 | A6 | **1**（Joel et al. 2020 PNAS） | 4 | `empirical`（population-level） | **4 lane → 1 study**；保留 `19:76` 的限定 |
| **N-A11** | 「爱/亲密/嫉妒/忠诚」不宜作 primitive | A11 | **0** | — | — | **移出本表**；改列为「`PARAMETER_CONVERGENCE` §12 `:586-610` 的**外部文献佐证**」 |
| **N-A12** | 三张 cross-context 清单不一致 | A12 | 1（`CURRENT_ARCHITECTURE:53-56`） | 1 | `structural` | 见 X-10 |

**`ADJ3` 的规则**：> `Lanes` 列改为 **`independent_sources × methods`**；`independent_sources = 0` 的一律不得进本表。

**parent 必须记录的两条限制**：
1. **`ADJ3` 0 次联网**，全部结论是关于**项目自身文档文本**的（`PROJECT_PRIMARY`）。
   因此 `ADJ3` 对 `A6`（Joel 2020）、`A7`（`ES=.09`）、`A11`（Sternberg/Reis/Fletcher）等**外部实证主张不发表任何意见**——包括不确认也不否认。
2. **`ADJ3` 未核** `README.md`、`CONSTRUCT_SCOPE_DIRECTIONALITY.md`、`R00`–`R17` 各报告本体、`A01`/`A02`/`A04` 本体。
   因此 `19` 的 `Lanes` 行是否虚报**未核**；`A12` 所称「三张清单」中的第三张标 `RELAYED_NOT_OPENED`。

**裁决者**：Architect（接受 N-A1…N-A12 替换 A1–A12）。

---

## X-9 · WO-N1 的被检验对象（`L-C11` 对被 relay 建议的反证）

**命题**：`WO-N7` / `WO-N1` 用 Fixture 001 检验 8 维 basis。

| 读法 | 来源 | 断言 |
|---|---|---|
| 建议侧（relayed） | `19` / R17 | 用 Fixture 001 检验 8 维 basis 的 fact-state 分离 |
| **反证** | `L-C11` `CONTESTED`（反证方 = 对冻结 substrate 的直接读取） | Fixture 001 的 core dyad 是**雇主↔雇员**，其 26 个原子事实是排班/停业/未付薪/CAB/申诉等**机构性事实**。用它检验 8 维 basis（Liking / RomanticAttraction / SexualDesire / Trust / AttachmentSecurity / Caregiving / Dedication / OutcomeDependence）大概率落到两种退化之一 |

**parent 处置**：**这是本轮唯一一个 child 对**自己 lane 的 relayed 建议**提出反证的条目**，独立性最强。
`L-C11` 判 `CONTESTED` 并要求 `19`/R17 明确 WO-N1 的被检验对象是「**事实态分离**」还是「**构念覆盖**」。

**裁决者**：Architect（在派工前必须回答，否则 N1 的结果不可解释）。

---

## X-10 · 「5 类 dyad 零覆盖」是 test-list gap 还是 domain gap

**命题**：`19` §1 A12 / R17 A6 把「Gate B 清单不含 sibling / parent–adult-child / ex-partner / professional / adversarial」呈现为覆盖缺口。

| 读法 | 来源 | 断言 |
|---|---|---|
| domain gap（读作要扩研究域） | `19:117-119` | 缺的是研究域 |
| **`WRONG-SCOPE`（针对呈现方式）** | `L-C6` + `ADJ3` Q4 | 缺的是**测试清单**，不是**研究域**。`CURRENT_ARCHITECTURE.md:53-56` **已把 A12 点名的 5 类中的 4 类逐一列为在域** |
| 三张清单互不相同 | `G-C13` `VERIFIED`（逐条比对三份 canonical 清单） | `CONSTRUCT_SCOPE §7.6`（6 项）、`PARAMETER_CONVERGENCE §2.4`（8 项）、`§15 Gate B`（11 项）**互不相同**，且都不含那 5 类 |

**`ADJ3` Q4 的逐条映射**：

| A12 说的缺失类 | `CURRENT_ARCHITECTURE` §2 的对应 | 覆盖度 |
|---|---|---|
| `sibling` | 「**亲属**」 | **蕴含**（未具名） |
| `parent–adult-child` | 「**亲属**」+「**照护**」 | **蕴含**（未具名） |
| `ex-partner` | 「**前任**」 | **逐字命中** |
| `professional/cooperative` | 「**同事**」+「**合作**」 | **逐字命中** |
| `adversarial/harm-asymmetric` | 「**敌对**」 | **部分**（`harm-asymmetric` 是不对称**轴**，不是 dyad **型**——A12 把一个轴混进了型清单） |

⇒ **4/5 逐字或直接蕴含，1/5 是类目错误。**

**`ADJ3` 采纳并加强了 lane `L` 的自我反驳**（`L-C6` 第 151 行自写「在域 ≠ 可表示」）：
> 既然研究域已声明、`AGENTS.md` 又禁止向下扩域，那 A12 **唯一可能的读法**就是「表示能力无证据」，
> 而**表示能力的证据只能由 corpus 覆盖给出，不能由域声明给出**。⇒ 缺口是**双层**的，且两层要分开记账：
> - **层 1（零成本）**：三张清单 vs `CURRENT_ARCHITECTURE` §2 的**文档对齐**。
> - **层 2（有成本）**：`sibling` / `parent–adult-child` / `non-romantic friendship` / `same-sex` 在 12 份语料里**零 core-dyadic 实例**——这需要**采集**，不是文档编辑。

**parent 补充的第三条独立发现**：`L-C5` 在 12 个 `core_dyad` 字段上逐条复算，**独立得到与 lane `I` 相同的 5 类集合**
⇒ 该集合是 `REPRODUCED_BY_ME`（`L`）**且** `VERIFIED`（`I` 查 fixture）⇒ **X-10 的「哪 5 类」部分是本轮少数真正独立的复现**。
**但**`L` 与 `ADJ3` 都明确：在 Gate B 的 cell 判据被定义之前，**任何零覆盖计数都不可锁定**（`L` 给的是「口径依赖的 partial = 2/12」）。

**裁决者**：Architect（接受双层记账）+ 语料采集（层 2）。

---

## X-11 · 五条候选律的处置（lane `L` vs lane `D` vs `ADJ2`）

| 律 | `L-C15`（lane L） | lane D | **`ADJ2` 逐律裁定** |
|---|---|---|---|
| `BMR`（A） | — | 判别部分 `UNTESTABLE_WITH_CURRENT_DESIGN` | **`HOLD_FOR_EVIDENCE`（只冻结单向版本）** |
| `APES`（B） | — | 工具阻塞 = 未定位到已验证的关系层 dependence 工具 | **`HOLD_FOR_EVIDENCE`**，排在 D8 工具裁决之后 |
| `DVA`（C） | **撤下**（kill criterion 已触发） | **不撤除**（`ACCEPT_AS_PROPOSAL`） | **`HOLD_FOR_EVIDENCE`**——**DVA 正确，但理由与两侧都不同** |
| `RGM`（D） | — | 需 S31 原文 + S17 正文 | **`HOLD_FOR_EVIDENCE`**，排在 `Ideal` 裁决之后 |
| `RT`（E） | **撤下** | — | **`RECLASSIFY_AS_METHOD_LIMIT`** → 记为 `MODEL_HYPOTHESIS / UNTESTABLE_WITH_CURRENT_DATA`，**不冻结** |

**`ADJ2` 推翻 lane `L` 的关键**：`L-C15` 是 `WRONG-SCOPE`（不是 `VERIFIED`），且**单 lane 且错误**——
它读的是 `19` 自己的表格，而 `19` 那一格与 `06` 的实际内容不一致，**lane L 没有回到 `06` 核对**。
- `19:208`（L3 行）写的**不是证伪判据，是一个注记**；`06:535-540` 的**判 G**（DVA 唯一的真证伪判据）要求 `Level` 独解释的人内变化方差
  **不少于** `Level+Slope` 才拒绝。**判 G 未触发。**
- `19:210`（L5 行）写「性别不对称的耦合被检出（**当前最佳证据反对**）⇒ 律族须重写」。但 `06:809` 逐字写：
  `性别不对称` = **「明确不预测」**，依据「S09 两方向近乎相等；S03 无性别差异」（`06:805` 给 `r = .380 vs .392`）。
  **即：不对称没有检出。判据未触发。`19` 的括号把「证据不支持本律的某个预测」写成了「kill criterion 已开火」——方向反了。**

**`ADJ2` 对 DVA 的理由（比 lane D 更强）**：`D` 的理由是「措辞强于来源」；`ADJ2` 的理由是**一手数据**——
**Lavner 2012 Table 5**（`ADJ2` 亲开 PMC3513382）：Husbands Low 组 intercept 86.24 / linear **−1.31**；Wives Low 组 86.58 / **−1.05**；
脚注逐字「All parameter estimates significant at **p < .001**」。正文逐字：
「the majority of spouses actually exhibited stable satisfaction… **Changes in satisfaction were isolated among the subset of spouses who started with lower levels of satisfaction**」。
**这一张表就是 DVA 的 `Level → Slope` 交互的直接证据，而且是 outcome 层的人内斜率，不是预测变量的斜率。**
`D` 没打开 Table 5，只读了摘要与 Discussion。

**`ADJ2` 同时指出 `06` 的两处过头**：
- `06:502` 把「limited evidence」标为 **`DIRECTION_NOT_SUPPORTED`（明确反证）**——**这也标过头了**：
  来源自己说的是 limited evidence + 妻子侧 null，**不是 explicit refutation**；而丈夫侧逐字「**Consistent with the incremental change model**」。
- `19` 表「概率最高的结局：被拒绝（初始差异胜）」应改为「**被重写为 level-conditional slope**」。

**`ADJ2` 对律 E 的四点拆解**：(a) 现象存在（事件内顺序 / Gable 等 / Rusbult 1991）`SUPPORTED`，但**全是 outcome 层**；
(b) 核心主张「`s` 由 dyadic state 决定」= **`MODEL_HYPOTHESIS`，零直接支持**（`06:810`）；
(c) `s` 与 `Z` 混层；(d) 判 M 用 **AND 门**、判 N 空结果**不触发**。

**裁决者**：Architect（是否冻结）+ 取样复核 `S04`（Joel 2020）的转述状态——`ADJ2` 声明这是「本包最需要 Architect 指定的下一处取样复核」。

---

## X-12 · 优先级排序与「唯一的真正阻塞项」

**命题**：`19` §7 优先级 1 写「**这是唯一的真正阻塞项**」。

| 读法 | 来源 | 断言 |
|---|---|---|
| 不可辩护（数量矛盾） | `L-C17` / `K-C46` | 同一文件 §2 把 C-1/C-2/C-3/C-4 标为「（阻塞级）」、C-5 标为「（排序死锁）」⇒ 4 阻塞级 + 1 死锁 与「唯一」并存 |
| 不可辩护（**成员不相交**） | `ADJ3` Q7 | 矛盾不是「数量对不上」，而是**两份 register 成员不相交**。`19` §8 的 B-1…B-8 与 §2 的 C-1…C-8 **只有 `B-6 ↔ C-3` 一项对应** |
| 排序依据不成立 | `K-C45` | 「修起来便宜 / 收益大」不成立：排在最前的恰是 8 条里唯一最贵的（canonical mutation，需 Human 显式授权） |
| 但可救回 | `ADJ3` Q7 | 真实排序依据是「**依赖解锁序**」；「收益大」成立，「修起来便宜」只在**编辑工时**意义上成立、在**授权**意义上是反的。而 `19` 对 N1→N7 的**依赖顺序判断是正确的**，应保留 |

**裁决者**：Architect（`L-C18` + `ADJ3` Q8 的 blocker 四分类见 `CANONICAL_CHANGE_PROPOSALS.md` C-P9）。

---

## X-13 · `total power` 的实现规格（`F-C21` vs `F-C23`）

- `F-C21`（`VERIFIED`，含全部引文）：`total power = mutual dependence / relational cohesion`（非零和）。
- `F-C23`（`WRONG-SCOPE`，**技术性错配**）：`10` 把 **Lawler 的 relational-cohesion 规格**当成了 **total-power 规格**。
  正确形式：`TP` = 对称聚合（和）；`C`（relational cohesion）是 `TP` 与 `RP` 的关系，**不是** `TP` 的定义。
- `ADJ2` rec 5 独立要求：「总 power 的实现规格须改（`F-C23`）——对称聚合是 `TP` 的正确形式」。

⇒ **`F-C23` 成立**（同一 packet 内的自我修正 + `ADJ2` 独立复核），但**它与 H-E2 的三分判定不矛盾**：
三分判定本身 `VERIFIED`，错的是 `10` 给 `TP` 写的**实现公式**。见 `CANONICAL_CHANGE_PROPOSALS.md` C-P4（拆 R2-a / R2-b）。

---

## X-14 · `11` §6.1 的格统计（`G-C3` `UNSUPPORTED`）与 `04` 的头条否定（C-C29）

- `G-C3`：`11` §6.1（采样框架后果，全报告最承重的一节）引用了四个矩阵格统计，**其中两个错误**；§3.4 引用的 D 列统计**两个都错**。`G` 逐格重算后证伪这五个具体数字 ⇒ `REJECT` 拒绝以现有形式引用 §6.1 的格统计。
- `C-C29`：§8.9「最重要的整体否定结果」——「本审计**未发现**任何『完全公开 + 双报告 + 方向性 + 多波 + 关系状态构念』的数据集。**这四个条件的交集为空。** 这是本 landscape 最重要的结构性事实」。
  `C` 判 `CONTESTED`：**交集为空在被结构检验的 15 个数据集上成立**，但 D12 是被**许可**条件而非结构条件排除的（`C-C26`），
  而 Add Health 官方文档确有 nomination / romantic pair 结构（`C-C20`）⇒ 「Add Health 从未进入结构检验」。
  ⇒ 请把「本 landscape 最重要的**结构性事实**」改为「**本次检索**的结构性结果」。

**共同点**：两者都是**「检索覆盖不足被写成领域存在性结论」**（这一模式另见 `A-C29`、`C-C30`、`G-C17`）。
`A` 把它命名为 `WRONG-SCOPE` 并给出判据：命题本身可能成立，但**层级 / 总体 / 分析单位 / 时间尺度 / 情境域**与被当作依据的那一层不匹配。
**parent 判：这是本轮最常见的单一失败模式，共 5 处，全部进 `REJECTED_OR_WEAK_FINDINGS.md`。**
