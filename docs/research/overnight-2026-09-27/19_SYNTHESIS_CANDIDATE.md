# 19 — SYNTHESIS_CANDIDATE

> **`SYNTHESIS_CANDIDATE` 不是 canonical architecture。**
> 本文件是 parent（Research Orchestrator）对 18 条 Wave 1 lane 报告与 4 份 Wave 2 audit 报告的 **join**。它不修改 ontology / foundation / 公式 SSOT / schema / 权重 / 阈值。
> 未经 Human / Project Architect 审阅，本文件中的任何结论**不得**被当作已确立结论、参数、公式、公式 SSOT 或验证依据。
> 本文件不含任何新的文献主张。所有事实性陈述的指针在其来源 lane 报告中；本文件只做交叉引用与冲突登记。

- **Work Order**：`youling/lhrm#30@overnight-opencode-exploration-swarm-v1`
- **🔴 Round 3 修复（child `A2`）**：`base_sha` = `8adcf0bacc45c0feb5c14e65e2a45346dd488b43` · `branch` = `r3/a2`。
  **权威依据**：`#30 comment 5854920569`（`ARCHITECT_ADJUDICATION_V1`）+
  `#30 comment 5854930069`（`ARCHITECT_ROUND3_DISPATCH_V1`）。
  **本文件实现的是 adjudication V1 的裁决，不是 Round-1 swarm 的原始主张**；两者冲突处一律以 adjudication 为准，
  冲突逐条登记在文末 §10。本轮**未改任何 canonical 文件**（`docs/foundation/*` / `AGENTS.md` / `docs/validation/*`）、
  **未跑 Gate A/B/C**、**未 merge / push / 开 PR**、**未读 / 未执行 / 未引用** `#20`/`#21`/`#22`、
  **未碰 Eye/Juece**、**无受限数据下载**、**未做任何新的文献扫描**。
- **Base**：`youling/lhrm@main` = `ee393ca24f9fbf738ac0ed839e99bdc99de6fc3a`（2026-09-27 live 复核，无漂移）
- **Governance at run**：`youling/ai-use@main` = `64018d80443c1889c8aaf4a6d27ffe78f3e6dd90`
- **As of**：2026-09-27
- **构成**：18 lane 报告（R00–R17）+ 4 audit 报告（A01–A04）+ manifest + child contract = 24 份 / 1,706,903 字节

---

## 0. 读法与三条自我约束

0. **【Round 3 新增】本文件的收敛计数是「独立来源」计数，不是「转述次数」计数。**
   §1 的 `Lanes` 列已被 `independent_sources × methods` 取代（`X-8`）；§8 是**唯一**的未解项登记表（`X-12` / `C-P9`）。
   **凡本文出现「不存在 / 无 / 为零 / 交集为空」而未限定检索范围的句子，一律按 `X-14` 视为待收窄**，
   收窄后的版本在 §1.3 逐条列出。
1. **本文件不是裁决。** 下面 §2 登记的每一处矛盾都需要 Human / Architect 裁决。本 attempt 不裁决。
   **【Round 3 补注】**——依 `ADJUDICATION_V1` **X-1**（`PPR` = BeliefState）· **X-2**（F3 改判为
   `WRONG-SCOPE`）· **X-3**（D7 vs R3 无逻辑矛盾）· **X-11**（无律被冻结），
   `C-1` / `C-2` / `C-4` 的**当前架构答案已被裁定**；剩下的只是**是否登记条件性后果预注册**这一件事。
2. **本文件不把一致性当作正确性。** 多个 lane 独立收敛到同一结论**不构成** validation（Work Order 明确禁止把文献数量或 LLM 一致度当作 validation）。收敛只说明「多条独立文献线指向同一处」，不说明该处为真。
3. **本文件不含 filler。** 凡目标未达成处，写明未达成，不补。

---

## 1. 收敛条目（按**独立来源**审计后的 `N-A` 方案）

> **🔴 Round 3：本节整体重写。** 依 `ADJUDICATION_V1` **X-8**「Replace A1–A12 with the audited
> `N-A1…N-A12` scheme and report `independent_sources × methods`, not lane count」与
> `REVIEW_SWARM_MANIFEST.md` §3「重复 vs 独立」条。
>
> **被取代的旧列（原文逐字保留，不删除）**：
> > 标注格式：`Lanes` = 独立收敛的 lane 数；`Type` = `empirical`（有外部实证）/ `structural`（架构内在推论）/ `methodological`（方法学推论）。
> > `Type` 一律**不是**「已确立」。
>
> **为什么要换列**：`REVIEW_CONTRACT.md` §4 的硬规则是「本 swarm 有 N 个 lane 都这么说在任何情况下都不构成
> verdict 升级依据」。原 `Lanes` 列统计的是**转述次数**，不是**独立来源数**；两者在本次 attempt 里
> **至少有两处相差 4 倍以上**（见下方「两处最重的非独立性」）。
>
> **新列的含义**：
> - `independent_sources` = **独立来源数**。一份 primary study 被 4 个 lane 引用**记 1**，不记 4。
> - `methods` = **到达同一结论的方法/路径数**（含转引）。
> - `independent_sources = 0` 的条目**不得进本表**（`ADJUDICATION_V1` X-8 明文）。
> - `Type` 语义不变，且**一律不是**「已确立」。

### 1.0 审计后的 5 + 5 + 2 分布

> `ADJUDICATION_V1` X-8 要求「Preserve the 5 + 5 + 2 distinction」。
> `ADJ3` 的原表逐行给出 `独立来源 / 方法 / 强度上限`，但**未逐行标注它属于 5/5/2 哪一档**。
> 本文件按下列**可复算规则**归档，并在 §1.0.1 把该归档规则本身标成一次判断（不是 `ADJ3` 的原话）：

| 档 | 规则 | 条目 | 数 |
| --- | --- | --- | ---: |
| **存活**（robust agreement） | `independent_sources ≥ 2` **且**来源计数已 reconcile | `N-A1` `N-A2` `N-A3` `N-A4` `N-A5` | **5** |
| **降级为单源收敛** | `independent_sources = 1`（含「1 primary + 1 镜像」） | `N-A6` `N-A8` `N-A9` `N-A10` `N-A12` | **5** |
| **移出本表** | `independent_sources = 0`（`N-A11`）／来源计数**未 reconcile**（`N-A7`） | `N-A11` `N-A7` | **2** |

#### 1.0.1 本文件对「5 + 5 + 2」归档的一次判断（**不是 `ADJ3` 的原话**）

- `N-A11` 归「移出」是 `ADJUDICATION_V1` 明文（`independent_sources = 0` 不得进本表），无判断成分。
- `N-A7` 归「移出」是**本 child 的判断**：该行自身写「lane 数**不是 5 也不是 7**
  （A02 自身 CF-12 记 5、G-06 记 7），**须先 reconcile**」，而 `R-K6` 独立指出语料中至少还有第 6 套
  `UNKNOWN_AS_OF` 词表 ⇒ **来源计数本身未 reconcile 的条目不能计为「已核实的 agreement」。**
  它**仍保留在本表内**（其 `independent_sources` 不是 0），只是标 `NOT_COUNTED_AS_AGREEMENT`。
- 若 Architect 认为 `N-A7` 应回到「存活」档，则 5+5+2 变成 6+5+1。**本 child 不代替 Architect 决定这一点。**

### 1.1 收敛条目表

| id | 主张 | 原 id | `independent_sources` × `methods` | `Type` | 强度上限 | Round 3 必改之处 |
|---|---|---|---|---|---|---|
| **N-A1** | `OutcomeDependence` 理论地位最硬、测量地位最薄；**在本 attempt 已审计的仪器范围内未定位到关系层 validated 工具** | `A3` | **3**（R01 / R03 / R16）× 3 | `empirical` | `empirical` | 原 `A3` 的「关系层级**无可用工具**」是 field-wide absence claim，**已收窄为 search-scope**（§1.3 `X-14-3`）。**不得**写成「结构上不可测」 |
| **N-A2** | 无坐标同时具备「有向边 + 特定 j + state 层 + 第二条独立观测通道」 | `A4` | **3**（R03 / R16 / **R04**）× 3 | `empirical` | `empirical` | **删 `A02`**（类目错配：`Unknown` 值类不属于本命题）· **补 `R04`** |
| **N-A3** | 「完全公开 + 双报告 + 方向性 + 多波 + 关系状态构念」四条件交集为空 | `A5` | **2**（R04 / R05）× 2 | `empirical` | `empirical`（**search-scope**） | R16 标 `dependent (JOIN_LANE: R04)`，不计入独立来源；**「交集为空」必须限定检索范围**（§1.3 `X-14-7` + §5） |
| **N-A4** | 生理同步不能作 pair-level 关系的代理 | `A7` | **2**（R03 / R09）× 2 | `empirical` | `empirical` | **删「R10 未主张」**（那不是一条独立收敛） |
| **N-A5** | 迟滞在二元关系数据上的存在性未知 | `A9` | **2**（R09 / R06）× 2 | `empirical`（**负结果**） | 负结果 | 「在多数真实 dyad 中不成立」是**量纲错误**（研究层 → dyad 层），已改写（§8.4 `R-B-4` 下的 Round 3 补记） |
| **N-A6** | `PPR` / `Satisfaction` 的层归属被经验文献**逆向排序** | `A4` / `R17-F3`（新条目） | **1**（Joel et al. 2020 + Segal & Fraley 2016）× 2 | `empirical` | **`CONTESTED`** | **必须双分支登记**；`17` 的 F3 推理含 `WRONG-SCOPE`；**不是架构主张**（`ADJUDICATION_V1` X-2） |
| **N-A7** | 项目在 refinement / 单调性 / 预序 / 数学格上空白；`Unknown` 值类被多条 lane 各自重新发明 | `A8` | **5**（R07 诊断 + R11 / R13 / R15 / R16 重发明）× 5，**计数未 reconcile** | `structural` | `NOT_COUNTED_AS_AGREEMENT` | `A02` 标为 dependent auditor；**lane 数不是 5 也不是 7，须先 reconcile**（`R-K6`：至少 6 套） |
| **N-A8** | 现有验证门在当前定义下**不能产生否决**；`MAPPING_FAILURE` **类型上不可达** | **`A1` + `A10` 合并** | **1**（`PARAMETER_CONVERGENCE` `§13` / `§14` / `§15`）+ **1 镜像**（`AGENTS.md:62`）× 2 | `methodological` | `methodological` | **合并两条**（它们是同一段 canonical 文本的两种读法）· **删「`MERGE`/`REJECT` 从未签发」**· **catch-all 3 → 4**· **指针 `§14 Step 3` → `§14:679` + `§15 Gate A` 第 3 步**。完整新论证见 §1.4 |
| **N-A9** | 有向性在测量层成立，但确认出的是**逐构念**的不对称度 | `A2` | **1**（同一张 instrument 台账）× **3**（1 独立 + 2 转引） | `empirical`（带来源共享限定） | **不得**称 3 lane 独立收敛 | 改述为「**1 张 instrument 台账 + 2 处转引**」（§1.2） |
| **N-A10** | 领域最大规模预注册研究的结论**逆向于**当前工程优先级 | `A6` | **1**（**Joel et al. 2020, PNAS** 一篇 study）× **4**（3 转引 + 1 独立复核） | `empirical`（**population-level**） | **4 lane → 1 study** | **保留**（原文逐字）：「**注意这只是 population-level 的方差陈述，不是本体陈述**——R02/R17 均明确不作「partner 侧不存在」的主张；当前项目文档**未做**这个区分」（见 §1.2） |
| **N-A12** | 三张 cross-context 清单不一致 | `A12` | **1**（`CURRENT_ARCHITECTURE:53-56`）× 1 | `structural` | `structural` | 缺口是**双层**的：文档对齐（零成本）+ 语料覆盖（需采集）。见 `X-10` / C-P7 |

> **表内有 11 行，不是 12 行。** 缺失的一行是 **`N-A11`**（「爱 / 亲密 / 嫉妒 / 忠诚 不宜作 primitive」，
> `independent_sources = 0`）——依 `ADJUDICATION_V1` **X-8**「`independent_sources = 0` does not qualify as a
> robust agreement and must not appear in the table」，它**被移出本表**，
> 重新归档为 **`PARAMETER_CONVERGENCE_V0_1.md` `§12:590-610` 现行条文的外部文献佐证**（§1.5，**零 LHRM 决策后果**）。
> **加上 `N-A7`（`NOT_COUNTED_AS_AGREEMENT`），「12」必须读作 5 存活 + 5 降级 + 2 移出。**

### 1.2 两处最重的非独立性（**本节最实质的更正**）

#### `N-A10` — 「4 lane 收敛」实为 **1 篇 study 被 4 处转引**

> **原文（Round 1，已被取代 —— 逐字保留）**：
> 「### A6. 领域最大规模预注册研究的结论**逆向于**当前工程的优先级 — `empirical`
> - **Lanes**：R06（F1 / F2）、R14（N-1）、R16（null B1/B2/B3）、R17（F2）。」

**更正**：`independent_sources = 1`。`R06` / `R14` / `R16` / `R17` 全部转引**同一组数字**
（43 数据集 / 11,196 对 / 2,413 个测量），来自 **Joel et al. 2020, PNAS** 一篇
（`10.1073/pnas.1917036117`）。**收敛发生在 study 级，不在 lane 级。**
本 child 2026-09-27 机器复核：同一组数字的承载行出现在 `06:504`、`16:474`、`17:127`、`17:444`，
`A01:193` / `A01:219` 把 `R14 O-13` 也记在同一组数字上。**`K` 未 flag 此项；`ADJ3` 首次标出。**
**保留**（不变）：「**注意这只是 population-level 的方差陈述，不是本体陈述**」——
R02/R17 均明确不作「partner 侧不存在」的主张；当前项目文档**未做**这个区分。

#### `N-A9` — 「3 lane 收敛」实为 **1 张 instrument 台账 + 2 处转引**

> **原文（Round 1，已被取代 —— 逐字保留）**：
> 「### A2. 「有向性」在测量层被确认，但确认出的是**逐构念**的不对称度，不是统一的低不对称 — `empirical`
> - **Lanes**：R01（F0-2）、R02（E4 / R4）、R03（F1 / G9）。」

**更正**：`independent_sources = 1`、`methods = 3`。三组数
（照护者↔被照护者关系满意度 `r = .43`；伴侣报告关系信任 `r = .11`（不显著）；
正向浪漫关系行为 self–other agreement `r = .18` 而 projection `r = .90`）
**全部出自同一张 instrument 台账、同同一批 primary study**（`[S15]` / `[S36]`）。
**本 child 机器复核**：三组数在 `02_CONSTRUCT_CONVERGENCE.md:68-70` 是**同一张表的连续三行**；
`18:363–370` 独立引用了 `r = .11`。⇒ **不得**称 3 lane 独立收敛。
**⚠️ 未 reconcile 的指针**：`ADJ3` 把该台账指认为 `R03` 的 instrument table；本 child 的字面 grep 命中在
`02`（R01）的表内。**归属待核，标 `PENDING_EVIDENCE_CHECK (R3-E3)`；本文件不选边。**
**保留**（不变）：R01 推论 —— 不一致 / 不对称度是**构念自身的经验属性**，必须逐构念估计并记录，
不能作为全局架构假设。

### 1.3 随 `N-A` 审计一并收窄的表述（**X-14**：search-scope，不是 field-wide absence）

> `ADJUDICATION_V1` **X-14**：「No qualifying dataset found in this audited landscape」**允许**；
> 「the intersection is empty in the field」**不允许**。同一规则适用于格统计与文献/工具缺失陈述。

| # | 原文（逐字） | 收窄后 | 依据 |
|---|---|---|---|
| X-14-3 | 「`OutcomeDependence`（D8）**理论地位最硬、测量地位最薄**，且关系层级**无可用工具**」 | **在本 attempt 已审计的仪器范围内未定位到关系层 validated 工具** | `N-A1` 行；`R-0` 类模式 |
| X-14-4 | 「**38 个 power/equity/balance 量表各自只被用 1–2 次，无一成为主流工具**」 | **在 `JFTR` 系统综述所覆盖的范围内，38 个量表各自只被用 1–2 次；本 attempt 未检出任何一个成为主流工具** | 保留原 `JFTR` 归属 |
| X-14-5 | 「R03：`JFTR` 系统综述——38 个 power/equity/balance 量表……」 | 保留，但**必须带出处归属**（`JFTR` 系统综述），不得读作「全领域」 | 同上 |
| X-14-6 | §1 `A3` 的「原文明确「尚无工具测量全部互依子维」」 | 这是**来源自己的措辞**，按引用处理，不构成本 attempt 的存在性结论 | X-14 |
| X-14-7 | `19` §5 的「**这四个条件的交集为空**」 | **在 R04 本次审计的 15–16 个数据集上，四条件交集为空**；**Add Health 从未进入结构检验**（`ACCESS_BLOCKED` 是**许可**轴，不是结构轴） | `R-0.2` / `C-C29` / `C-C26` / `C-C20` |
| X-14-8 | `19` §1 `A9` / §5 的「**intensive longitudinal 关系日记数据在本 landscape 中不存在**」类表述 | **在本 attempt 审计的范围内未发现** | `R-0.3` / `C-C30` `WRONG-SCOPE` |
| X-14-9 | §1 `A12` / §7 `WO-N5` 把「**12 份语料**」当作 Gate B 的**既有语料面** | **12 份中只有 2 份 `direct-use`（L1-003 Magi / L3-001 Yellow Wallpaper），10 份是 `needs cleaning`**；且 corpus 作者自己写明 L2/L3 `deliberately deferred until Verifier protocol is frozen` | `R-C12` / `L-C12` `WRONG-SCOPE`（本 child 已逐行复核 `VALIDATION_CORPUS_V0_1.md:332-343`） |
| X-14-10 | §6.3「R11：24 × 10 矩阵共 216 个判定格，其中 69 个 `MEANING_PRESERVED`，**支撑它的 invariance 研究数 = 0**」 | **本 `R11` packet 未检出任何支撑性 invariance 研究报告**（不是「研究数 = 0」） | `R-D25`（同型模式） |
| X-14-11 | §6.4「LHRM 现有 126 条 proxy **无一条有跨语言不变性证据**」 | **本 `R13` packet 未检出任何一条带跨语言不变性证据的 proxy** | X-14 |

### 1.4 Gate rationale —— 缺陷保留，论证替换（**`R-A1` / `R-A2` / `R-A3` + `C-P1`**）

> **原文（Round 1，`A1` + `A10`，已被取代 —— 逐字保留）**：
>
> 「### A1. 现有的验证门在当前定义下**不能产生否决** — `methodological`
> - **Lanes**：R17（F1 / F9 / F11）、A03（独立判定，三项可复现检验 T1/T2/T3）。
> - A03 的判定比 R17 更强也更具体：Gate A `EXECUTABLE_BUT_NON_FALSIFIABLE`；Gate B / Gate C 既不可证伪也不可执行；
>   `PARAMETER_CONVERGENCE_V0_1.md` §2.6（**唯一能删除 construct 的准入侧判据**）结构上无法触发 ⇒
>   8 项 candidate basis 单调增长，`MERGE` 与 `REJECT` **从未被签发过一次**。
> …
> ### A10. `MAPPING_FAILURE` 当前**类型上不可达** — `methodological`
> - **Lanes**：R17（F1）、A03（T1/T2/T3 独立确认）、A02（cross-check）。
> - 三个独立机制：(1) §13 的 10 个映射类含 **3 个 catch-all** + 自由文本 ⇒ `MAPPING_FAILURE` 无路径可走；
>   (2) `AGENTS.md` 诊断清单含 \"or merely narrative/irrelevant\" ⇒ 每个失败都有合法出口；
>   (3) §14 明说 Step 3 **只测命名不测数值**。」

**更正后的表述（`N-A8`）—— 逐条对应：**

| # | 项 | Round 3 后的表述 |
|---|---|---|
| 1 | **保留的缺陷** | 当前 Gate A/B/C 在判据原文下**不存在会被算作失败的结果**；`MAPPING_FAILURE` **类型上不可达**。三条独立一手复现（`I-C1` / `ADJ3` Q1、Q2、Q5 / `EV1` §6–§7，未共享中间产物） |
| 2 | **删掉的支撑 (a)** | 「`§2.6` 是**唯一**能删除 construct 的准入侧判据」**为假**。六条准入判据中：**只有一条用删除框架**（`§2.6`）、**两条用降级框架**（`§2.2` / `§2.5`）、**三条连后果句都没有**（`§2.1` / `§2.3` / `§2.4`）；且**六条全部**无 procedure / required evidence / output field / threshold / designated executor。**本 child 逐行复核** `PARAMETER_CONVERGENCE_V0_1.md:45`（§2.1）· `:49`（§2.2 后果句 `:53`）· `:55`（§2.3）· `:59`（§2.4）· `:63`（§2.5 后果句 `:80`）· `:82`（§2.6 反事实 `:84`）。`§2.3` 的「**仍可能**提供额外信息」是可能性陈述，**不可被否定**。`:43`「至少接受以下审计」是全族唯一的程序性句子，而它**未指定审计者、未指定产出、未指定失败后果** |
| 3 | **删掉的支撑 (b)** | 「`MERGE` 与 `REJECT` **从未被签发过一次**」**在项目层为假**。`PARAMETER_CONVERGENCE_V0_1.md:499`（`§9 R4`）与 `:505`（`§9 R5`）各含一个 `REJECT`；本次 attempt 全域另有 **≥8 处** `REJECT` 承载行。**正确表述**：**8 项 basis 在已执行的 gate 下从未被删减过一条**；项目历史上确实签发过 `REJECT`，但那些**全部由 drafting 时的散文判断作出，没有一条是由 §2 判据或 §15 门跑出来的**（**无执行记录**）。**本文件不写「确定为作者判断」**——不能排除作者在别处跑过未记录的评估 |
| 4 | **`MAPPING_FAILURE` 不可达的机制数** | **三**个**文本上互不相同**的机制（原写「三个」但把 §13 与 `AGENTS.md` 当两个来源数）；作用于流水线的**三个不同阶段**：分类 / 分诊 / 阈值 |
| 5 | **catch-all 数** | **4** 个（原写 3 个；方向是**把缺陷说得比 A03 小**） |
| 6 | **来源数** | **1 primary file + 1 镜像**：`AGENTS.md:62` 与 `§13:641-649` 是**同一条 7 项诊断清单**（`ontology / construct / scope / temporal-history / belief-observation / measurement / or merely narrative-irrelevant`，措辞与次序逐项一致）。**把它当第二个独立来源是双重计数**。**本 child 已逐项复核（7/7 命中，顺序一致）** |
| 7 | **悬空指针** | 「`§14` 明说 **Step 3**」是**悬空指针**——`§14` **没有任何编号 step**。真实位置是 **`§14:679`** （「第一版 Case Bank test 只要**语义有合法落点**，不要求每句话产生精确数值变化」）**加上** `§15 Gate A` 第 3 步（`:713`「独立 Agent 逐句映射」）。**本 child 已 grep `§14` 全文：`Step N` 命中 0** |
| 8 | **两条合并** | `A1` 与 `A10` 是**同一段 canonical 文本的两种读法**（agreement 级双重计数）⇒ 合并为 `N-A8` |

#### 1.4.1 准确的最简描述（**替代原「昂贵 canonical patch + 重跑 Fixture」**）

- **缺的最小集合**（`EV1` §8 + `ADJ3` Q2，两条可同时成立）：
  1. **一个后果动词**（`KEEP` / `MERGE` / `REJECT` / `HOLD`）+ **一个阈值**；
  2. **一个诊断类型**——一个 **`redundancy` 类**（Gate A 的诊断词表 `§13:642-648` 是**纯加法封闭**的，6 个 hole 全是「某物无法被表示」，**没有 `redundancy` / `duplicate` 一类** ⇒ 一次「某 construct 冗余」的 gate 结果在**当前类型系统里根本无法被表达**）；
  3. **一条 leave-one-out ablation 臂**（`§2.6:86` 承诺「这项将在 Case Bank regression 中直接测试」，而 `§15 Gate A`（`:707-715`）的 5 个步骤里**没有任何一步**包含「移除某个 construct 再重测」）；
  4. **补 re-entry criterion**（见下）。
- **相关的第二个缺陷**：`PARAMETER_CONVERGENCE_V0_1.md` `§12` 的**六项推测性排除**
  （`:590` 爱 / `:594` 亲密 / `:598` 嫉妒 / `:602` 控制欲 / `:606` 忠诚 / `:610` 化学反应）
  以「可能 / 更可能 / 需区分 / 保留为」这类**推测措辞**被排除出候选，且**没有任何 re-entry criterion**。
  ⇒ **这 6 项是已经生效的、无阈值的、无回归路径的排除。** 补 re-entry criterion 比补 `§2.6` 更能防止假否决。
- **严重性已降级**（`R-A3` / `EV1` §8）：约 **5–8 句文档编辑 + 1 个 ablation 步骤定义 + 1 个诊断枚举值**，
  落在 `PARAMETER_CONVERGENCE_V0_1.md` **5 处**，**外加 1 处 `AGENTS.md:62` 镜像同步**。
  **不需要新文献、不需要新数据、不需要新模型。**
  **⚠️ 变更面比成本大**：`ADJ3` 要求把面扩到 **4 文件 / ≥6 节**（`§2.1`–`§2.6` 全族 + `§13` 类表 + `§15` 三门 + `AGENTS.md:62`）。
  二者不矛盾：`EV1` 估的是**新增文字量**，`ADJ3` 扩的是**必须一起改的面**。
- **必须同时记录的一笔钱（`EV1` §9）**：「修复缺陷」与「Gate A/B/C 至今从未被完整执行过一次」是**两笔钱**。
  后者是**首个** Case Bank regression run 的成本，**与本缺陷的修复成本无关**；
  本文件**不**把它算进修复成本，也**不**主张「必须先跑一次 Gate A 才能确认缺陷」。

### 1.5 移出本表的一条（`N-A11` · `independent_sources = 0`）

> **原文（Round 1 `A11`，已被取代 —— 逐字保留）**：
> 「### A11. 「爱 / 亲密 / 嫉妒 / 忠诚」不宜作 primitive 这一立场**不能作为本项目的发现** — `empirical`
> - **Lanes**：R14（R7 / F-15）、R01（§3.2 F0-4）、R17（A11 `UNCHALLENGED`）。…」**处置**：

1. **本条不占用 Architect 决策**（`R-L5` / `L-C16`）：该立场**已经是 `PARAMETER_CONVERGENCE_V0_1.md` `§12`
   的现行条文**（`:590`–`:610`），且词表逐条相同。
2. ⇒ **在 LHRM 内部没有任何决策后果**。原标题「不能作为本项目的发现」被撤销：
   **它既不是本项目的发现，也不是待裁决项**——它是**已决事项的外部文献佐证**。
3. **重新归档为外部文献佐证**（保留全部原始内容，不删除）：Sternberg (1986) 三成分 ·
   Reis & Shaver (1988)（intimacy = 披露 × 响应的**过程结果**）· Fletcher et al. (2000) **二阶 quality 因子** ·
   Ideal Standards Model；R01 追加 Hendrick & Hendrick (1989) 合并多套 love 量表做因子分析
   **未复现任一既有 love 类型学的结构**；Berscheid (2010)「问人们是否爱伴侣，很可能对关系中存在的情感状态
   及其未来轨迹几乎不具信息量」。
4. **`independent_sources = 0` 的含义**：这三方（`R14` / `R01` / `R17`）**不是三个独立来源**——
   它们是**同一个外部文献簇**的三种转述。⇒ 依 `ADJUDICATION_V1` X-8，本条**不得进 §1.1 收敛表**。
5. **指针**：`14_PAPER_POSITIONING_NOVELTY.md` §3.1 R7 / §3.3 F-15；`02_CONSTRUCT_CONVERGENCE.md` §3.2 F0-4；
   `PARAMETER_CONVERGENCE_V0_1.md` `§12:590-610`。

## 2. Unresolved contradictions（需要 Human / Architect 裁决，本 attempt 不裁决）

> 完整证据链见 `18_CROSS_LANE_CONFLICT_AUDIT.md`。此处只登记**最高优先级**项。
>
> **🔴 Round 3（`X-12` / `C-P9`）：本节与 §8 已合并为**一份**登记表，唯一编号空间是 §8 的 `R-B-*`。**
> 本节保留 `C-n` 编号**仅作为历史 Round-1 记录**（不改写历史），但**「阻塞级」标签不再是分类依据**：
> 本节自己就标了 **4 项「阻塞级」（`C-1` / `C-2` / `C-3` / `C-4`）+ 1 项「排序死锁」（`C-5`）**，
> 与 §7 旧文「**这是唯一的真正阻塞项**」**直接矛盾**。依 `ADJUDICATION_V1` **X-12**
> 「Remove 'unique true blocker'」，该标签已删除，五分类见 §8。
> **本节 8 项与 §8 的 8 项曾「只有 `B-6 ↔ C-3` 一项对应」——那不是编号错乱，是分母不同**（`R-4` 第 2 点）。

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

> **🔴 Round 3：本条已重写（sibling `A1` 移交项 `C2`）。原裁决的两条支撑都错。**
> **原文（Round 1，逐字保留）**：
> - A04 主张 `10.31234/osf.io/…` 前缀/后缀结构非法，应改为 `10.31219/…`。
> - 修复 child 实测：`10.31234/osf.io/dus42` → **302 解析**；`10.31219/osf.io/dus42` → **404**。`10.31234` 是 OSF-preprint 前缀，`10.31219` 是 OSF **project** 前缀。
> - **裁决**：`10.31234` 正确，**未改**。这是本次 attempt 内**审计结论被实测推翻**的一例，记录为流程观察：**审计 child 的断言必须经独立实测复核后才能落到 durable artifact。**

| # | 原裁决的支撑 | Round 3 裁定 | 实测依据 |
|---|---|---|---|
| 1 | 「`10.31234` 是 OSF-preprint 前缀，`10.31219` 是 OSF **project** 前缀」 | **WRONG**。`10.31234` 与 `10.31219` **两个前缀都 live**，Crossref prefix registry 里**注册者是同一家**：`Center for Open Science` | prefix registry 逐条查 |
| 2 | 「`10.31219/osf.io/dus42` → **404**」 | 该 404 结论**不能支持**「`10.31219` 不可用」：真正 404 的是**前缀错配 + 无版本后缀**的组合。`10.31219/osf.io/gu8z7` → 302 → **终态 200** | 6 个 identifier 逐条 HEAD/GET |
| 3 | 「裁决：`10.31234` 正确，**未改**」 | **结论方向保留，但理由换掉**：`f6wbn` **只在 `10.31234` + `_v1` 形态下注册** ⇒ 真实缺陷是**缺版本后缀**，修法是**补后缀**、**不是换前缀** | `10.31234/osf.io/f6wbn_v1` **200** / `10.31234/osf.io/f6wbn` **404** |

- **流程观察保留不变**：**审计 child 的断言必须经独立实测复核后才能落到 durable artifact。**
  本条是该观察的**第二个实例**——第一次实例（A04 的前缀主张）也被证伪了，而当时的裁决文本
  **自己也带了两个未经实测的前缀语义断言**。
- **下游风险（必须阻断）**：若照原文去「把 `10.31234/osf.io/…` 统一改成 `10.31219/osf.io/…`」，
  会把 **live 指针 `10.31219/osf.io/gu8z7` 变成 404**，且不修复任何东西。
  ⇒ 该批量修改登记为 **`REJECTED_WITH_REASON`**（与 `A04` §10 P2 的同向结论一致）。
- **依据**：`REVIEW_SWARM_MANIFEST.md` §7 `M-1`；`REJECTED_OR_WEAK_FINDINGS.md` `R-B5`（`J-C8` `UNSUPPORTED`）;
  `ADJUDICATION_V1` §D。**本 child（`A2`）2026-09-27 独立复验 6 个 identifier**，未复制 A1 的结论。

---

## 3. Strongest red-team findings（R17 + A03）

R17 独立起草（首稿在任何 lane 报告写入之前完成，独立性 CONFIRMED），共裁定 23 条假设：`CHALLENGED` 8 · `CONTESTED` 8 · `UNCHALLENGED` 3 · `NO_EVIDENCE_FOUND_FOR_CHALLENGE` 2。

| # | 发现 | 破坏了什么 | 可定案的具体观察 | 独立复核 |
| --- | --- | --- | --- | --- |
| **R17-F3** | 层边界被经验文献**反向排序** | LHRM 把经验文献认定为因果最近端的两个变量（`PPR`、`Satisfaction`）都降级了 | 同一 dyad 上同时测 belief 与 state；若 belief 层的协变领先于 state 层则层位反了 | 见 C-1 |
| **R17-F1/F9/F11** | Case Bank 目前**不是测试** | 三个独立机制 | 删掉 catch-all 后重跑 Fixture 001，看 `MAPPING_FAILURE` 是否变得可达 | A03 独立确认（T1/T2/T3） |
| **R17-F2** | Joel 2020 的五条结论 | 动态工程（工程顺序 5/6）与增量预测主张 | 5/5 top predictor 落在 `DirectedRelationshipState` **之外** | ⚠️ **Round 3：不是「R06 / R14 / R16 独立采用」** —— 三者转引**同一篇** `Joel et al. 2020, PNAS`（`1 study`，`N-A10`） |
| **R17-F7** | 验证工具对目标现象的一部分**原理上盲** | 文本 benchmark 可 100% 覆盖而与真正驱动现场行为的层完全无关 | Eastwick (2011)：隐式 vs 显式吸引力偏好 `r = .00`，且显式偏好只预测照片、不预测现场 speed-dating | — |
| **R17 A6** | `Gate B` 的 11 类反例就是项目自己的假设列表 | 跨域稳定性门是同义反复 | 逐条核对清单文本 | A03 修正为 8/11，方向不变 |
| **R17 A14** | `Reality ≠ Observation ≠ Belief` 的**分离**存活，但**排序**被推翻 | 层位顺序 | — | A03/R14 一致 |
| **A03 H-4** | 存在**两条平凡通过路径**（全弃答 / 复制 fixture status 列）使 R13 的六个 faithfulness 指标全部最大化 | 指标的区分力 | 构造这两条路径并验证指标是否真的最大化 | A03 独立 |
| **A03 §2.6** | ~~唯一能删除 construct 的准入侧判据~~ **结构上无法触发** | basis 单调增长；`MERGE`/`REJECT` 从未签发 | 检查该判据的分支覆盖 | A03 独立 |

> **🔴 Round 3：上表最后一行是本文件里最重的一处错误论证。缺陷保留，论证换掉。**
> **原文（Round 1，逐字保留）**：「唯一能删除 construct 的准入侧判据**结构上无法触发** …… basis 单调增长；
> `MERGE`/`REJECT` 从未签发」。
>
> | 删掉的支撑 | 为什么假 | 依据 |
> |---|---|---|
> | 「`§2.6` 是**唯一**能删除 construct 的准入侧判据」 | **全称量词为假**。六条准入判据里**只有一条用删除框架（`§2.6`）**、**两条用降级框架（`§2.2` / `§2.5`）**、**三条连后果句都没有（`§2.1` / `§2.3` / `§2.4`）**；且**六条全部**无 procedure / required evidence / output field / threshold / designated executor | `R-A2`（`ADJ3` Q2 逐行 / `EV1` §6 第 3 点）；本 child 逐行复核 `PARAMETER_CONVERGENCE_V0_1.md:45–:86` |
> | 「`MERGE`/`REJECT` **从未签发**」 | **项目层为假**。`PARAMETER_CONVERGENCE_V0_1.md:499`（`§9 R4`）/ `:505`（`§9 R5`）各一个 `REJECT`；本次 attempt 全域另有 **≥8 处** `REJECT` 承载行。**真正为真的那一层**是：「`R01` 报告内 `MERGE`/`REJECT` 各 0 次作为**裁决值**」 | `R-A1`（`EV1` `PARTLY_REFUTED` / `ADJ3` Q1 三层裁定） |
>
> **替代表述**（唯一可按现状引用的一条）：
> > **8 项 basis 在已执行的 gate 下从未被删减过一条；项目历史上确实签发过 `REJECT`，
> > 但那些全部由 drafting 时的散文判断作出，没有一条是由 §2 判据或 §15 门跑出来的。**
>
> **为什么这个措辞差异决定修法**：`ADJ3` rec 2 —— 它决定 WO-N1 是「改文化」还是「改一份门规范」，**后者便宜得多**。
> **严重性已降级**：从「昂贵 canonical patch + 重跑 Fixture」降为 **约 5–8 句文档编辑 + 1 个 ablation 步骤定义
> + 1 个诊断枚举值**（`R-A3` / `EV1` §8）。**完整新论证见 §1.4。**

**R17 攻击失败、明确站在项目一方的 3 条**（R17 自己记录，红队不说假话）：
- A10 `State ≠ Action`：Hui et al. (2014) Manhattan Effect 反而**支持**它。
- A11 拒绝「爱/亲密/嫉妒/忠诚」为 primitive：攻击不动。
- A12 Unknown 显式化：三个 fixture 构成真实压力测试并通过。

**R17 未能找到反证、如实登记为 `NO_EVIDENCE_FOUND_FOR_CHALLENGE` 的 2 条**：`OutcomeDependence`（项目自标 open question，诚实）；`Liking` vs `RomanticAttraction`（R17 判断 Sternberg (1987) 的存在本身即分离证据）。

**R17 对本项目最有价值的一句判断（parent 保留为待议观点，非结论）**：
> 最可辩护的项目是「带显式知识时间与 provenance 的 dyadic claim 证据表示语言」；最不可辩护的是「人类关系的 8 维潜在状态 basis」——后者是对一个 40 年过程模型的重新推导，测量姿态更差，且无数据。**LHRM 目前把可信度预算花在了后者上，而它本可以低成本地花在前者上。**

---

## 4. 候选经验律（5 条，**候选**，非已冻结）—— Round 3 已套用裁决状态

> **🔴 Round 3 首要声明（`ADJUDICATION_V1` §C 第 5 点 + **X-11**）**：
> **没有任何一条 transition law 被验证或冻结。** 全部为 `RESEARCH_CANDIDATE`。
> **无参数、无权重、无阈值、无拟合。** 冻结需 Human 授权的**独立** Work Order；
> 本 Work Order 明确禁止拟合与冻结。
>
> **表头已改**：原表的最后一列是「证伪判据（预登记）」，但**其中两格写的其实不是证伪判据，是一个注记**
> ⇒ 依 `X-11` / `R-L9`，本表把「裁决状态」与「证伪判据是否已触发」拆成两列，并把两处错格改写。

| id | 律 | 一句话 | 关键支持 | 裁决状态（**X-11**） | null（**X-6 / C-P10**） | 证伪判据是否**已触发** |
|---|---|---|---|---|---|---|
| **L1** | `BMR` Belief-Mediated Responsiveness | `i` 的有向状态**只**经由 `i` 对 `j` 行为的**解释**移动；归属在门控符号与门控强度两处起作用 | Laurenceau 1998/2005（PPR 为部分中介，96 对 × 42 天双报告）`PENDING_EVIDENCE_CHECK (R3-E3)` | **`HOLD_FOR_EVIDENCE`** —— **只保留「单向版本」作为研究候选**（`i` 的有向状态只经由解释移动）；归属符号分支仍未定 | `AR_ONLY` / `NO_PARTNER` / `ACT-NOT-BELIEF` / `NO-ATTRIB` / `MEAN-REV-ONLY` | **未触发**（`NO-ATTRIB` 与完整版拟合相同 ⇒ 核心主张被削弱） |
| **L2** | `APES` Actor–Partner Exchange with Stock | 满意度–替代品–投入驱动一个**积累的** dependence 存量；dedication 是其下游读出 | Le & Agnew 2003（52 研究，≈2/3 方差）；Rusbult & Martz 1995 | **`HOLD`** —— **阻塞点是关系级 `OutcomeDependence` 测量**，排在 D8 工具裁决之后。**注意**：工具阻塞应写「**未定位到已验证的关系层 dependence 工具**」，**不得**写成「结构上不可测」 | `B1` persistence · `B2_STABLE_LEVEL`（见 §4.1） | **未触发**（完整版未能击败 `AR_ONLY` ⇒ 退化为自回归，**拒绝其作为独立律族**） |
| **L3** | `DVA` Deterioration vs Actualization | 评价读出的下降由两个**可分离**机制产生：起点选择 + 个体内实际化 | Johnson 2022（LCM-SR，双方非零自回归 + 交叉滞后，**无性别差异**）；Lavner 2012 Table 5 —— **`PENDING_EVIDENCE_CHECK (R3-E3)`** | **`HOLD_FOR_EVIDENCE`** —— **只保留为「level-conditional-slope 候选」**。**「最佳可得证据逆向于本律的增量通道」这一 framing 已删除**（它写的是一个**注记**，不是已触发的 kill criterion） | `B2_STABLE_LEVEL` · **`N8_LEVEL_CONDITIONAL_SLOPE`** | **判 G 未触发**。`06:535-540` 的判 G 要求 `Level` 独解释的人内变化方差**不少于** `Level+Slope` 才拒绝。Lavner Table 5 脚注逐字「All parameter estimates significant at **p < .001**」；正文逐字「the majority of spouses actually exhibited stable satisfaction… **Changes in satisfaction were isolated among the subset of spouses who started with lower levels of satisfaction**」⇒ **这一张表是 `Level → Slope` 交互的直接证据** |
| **L4** | `RGM` Reference Gap and Movement | 同一对方行为可经**两条通道**缩小 gap：改变 Actual，或移动 Ideal | Drigotas 1999（Michelangelo 现象，4 研究）；Pusch 2023 —— **Ideal / S31 来源 `PENDING_EVIDENCE_CHECK (R3-E3)`** | **`HOLD`** —— **待 `Ideal` 来源核实**。`Ideal` 在 S31 原文与 S17 正文核实前**不应进入 `PARAMETER_CONVERGENCE`** | `B1` / `B5` label-only | **未触发**（两条通道无法在同设计中分离，各自解释 <50% 共享方差 ⇒ 拆成两条单通道律） |
| **L5** | `RT` Rhythm and Threshold（双分支） | 事件级互动有**两条分支**：放大（`Λ⁺`）与抑制/修复（`Λ⁻`）；分支由 dyadic state 决定 | Schrodt 2014（74 研究 / 14,255）；Gable 2004；Rusbult 1991 —— **全部是 outcome 层** | **`MODEL_HYPOTHESIS` / `UNTESTABLE_WITH_CURRENT_ORDINARY_WAVE_DATA`** —— **不冻结**。核心主张「`s` 由 dyadic state 决定」= **`MODEL_HYPOTHESIS`，零直接支持**（`06:810` 自陈「无来源直接检验」） | `B1` / `B3` no-partner | **未触发**（**方向反了**：`06:809` 逐字写「性别不对称 = **明确不预测**」，依据「S09 两方向近乎相等 `r = .380 vs .392`；S03 无性别差异」⇒ **不对称没有检出**） |

**为什么只列 5 条而不是更多**：R06 交付 5 族；R16 已为每族给出对应的 leakage 规则（L1–L8）与 null（B0–B6）；
R05 已给出每族对应 Q1–Q10 中哪几个**在当前数据下不可识别**。**再加律族不会增加信息，只会增加不可检验面。**

**R06 明确列为「当前不可证伪」的律族**（点名比隐藏更有价值）：依赖 `U-1`–`U-8`，其中 `U-3`
（关系终止的删失偏差）被 R16 升格为**最严重的结构性盲点**——离开的人停止作答，因此
**任何关于「关系最重要的一次转移」的律在受访者数据上都不可证伪**。

**Round 3 补记（`R-D14` / `R-D6` / `R-D27`）**：`L1` / `L5` 的两条判据（判 H / 判 N）
**守的是两个没有失败路径的前提**（「关系状态自然衰减」「分支由 dyadic state 决定」）
⇒ **无法被空结果推翻**，应移入 `06 §10` 的不可证伪清单，而不是继续挂在预登记判据位上。
`L5` 的两条分支存在性**全部是 outcome 层证据**，本表已改标 `MODEL_HYPOTHESIS`。

### 4.1 null registry（**X-6 / `C-P10`）—— Round 3 已重命名并扩容

> **原文（Round 1，逐字保留）**：`L2` 行写「`B2` selection-only」，`L3` 行写「`B2` selection-only（稳定 per-dyad 截距）」。

| 变更 | 原文 | Round 3 后 | 依据 |
|---|---|---|---|
| **改名** | `B2` / `SELECTION_ONLY`（`16:203`：**稳定 per-dyad 截距，无 wave-to-wave 增量** = 随机截距 only） | **`B2_STABLE_LEVEL`** / **random-intercept-only**。**停止使用 `SELECTION_ONLY` 这个名字** | `ADJUDICATION_V1` **X-6** / **C-P10** |
| **另一条 null 必须保持独立** | `06:488` 写「**`SELECTION-ONLY`（只起点，无 slope）：`E(τ) = Level(τ₀) + 随机游走 + 误差`**」 | **R06 的 `Level + random walk + error` 是与 `B2_STABLE_LEVEL` 不同的另一条 null**，**必须作为独立 null 保留**。Round 1 把两者当同一个名字，是本 PR 内最危险的一处**同名异义** | `ADJ2` Q2；本 child 复核 `06:488` 与 `16:203` 原文 |
| **角色** | `16:197` 主判定规则要求候选**配对地**击败 `B1` **与** `B2`；`16:203` 称 `B2` 是「**本协议认为最重要的一条 null，因为它已经击败过一个候选**」 | **`B2_STABLE_LEVEL` 是「相关时选用的诊断基线」**（`B2_DIAGNOSTIC`），**不是**普适的配对硬门。**不主张 `B2` 被 `B1` 在所有报告口径下严格数学支配**（若两者报告指标不同，配对检验在报告层面仍有意义） | `ADJUDICATION_V1` **X-6**「do not require every candidate to 'paired-beat B1+B2' as a universal hard rule」；`C-P10` |
| **删掉的措辞** | 「本协议认为**最重要**的一条 null」「**已经击败过**一个候选」「**已核实证伪**」 | **三处全部删除**。`REJECTED` / 不成立的是**推论**，不是来源的转述（`EV1` Claim 2：Lavner 摘要与 Table 5 的**描述逐字正确**，错的是从正确描述推出错误推论） | `R-A1` 同型 / `X-6` / `C-P10` 第 2 条 |
| **Lavner 的正确引用** | 旧 rationale 写「S19 在正面对决中 **initial-differences 击败 incremental-change**」 | 应为：**初始值对轨迹组的区分力强于所测风险变量的变化率**（`Across all predictor variables, initial values afforded stronger discrimination of outcome groups than did rates of change in these variables`）。**它讲的是 predictor 变量，不是 outcome 的人内斜率** | `C-P10` 第 3 条（逐字）；`R-0` 类模式 |
| **新增 null** | 无 | **`N7_UNDIRECTED_SCORE`**（把 `Z[k,i→j]` 与 `Z[k,j→i]` 合成单一无向分数）—— **唯一直接测本项目中心表示主张的 null**；独立支撑见 §1 `N-A2`（16 个已审计数据集中只有 1 个提供无外部假设的 `DIRECTED_EDGE` 双分量，而它没有第二个时间点）<br>**`N8_LEVEL_CONDITIONAL_SLOPE`**（Lavner 真正赢下的结构）—— **唯一能真正测 DVA 交互的模型，必须在 null 集里**，否则 DVA 的判 G 无参照物 | `ADJUDICATION_V1` **X-6**「Accept adding `N7_UNDIRECTED_SCORE` and `N8_LEVEL_CONDITIONAL_SLOPE`」；`C-P10` 第 4–5 条 |

**`PENDING_EVIDENCE_CHECK (R3-E3)` 清单（本文件不猜）**：

| 承载源 | 用在哪 | 状态 |
|---|---|---|
| `S04` = Joel et al. 2020, PNAS（`10.1073/pnas.1917036117`） | `L1` 的「关系质量变化不可预测」转述 · `N-A10` 全条 · §3 `R17-F2` | **`PENDING_EVIDENCE_CHECK (R3-E3)`** |
| `S19` = Lavner et al. 2012, Table 5 | `L3` / `N8_LEVEL_CONDITIONAL_SLOPE` / 旧 `B2` rationale | **`PENDING_EVIDENCE_CHECK (R3-E3)`** |
| `S31` / `S17` = `Ideal` / `RGM` 来源 | `L4` 全部支持 | **`PENDING_EVIDENCE_CHECK (R3-E3)`** |

> **本 child 未做任何新的外部取样。** 上表三条由 sibling 复核（dispatch `R3-E3`）。
> **在复核落地前，这三处不得作为「已核实转述」引用**；本文件对它们**既不确认也不否认**。
> 另：`06:502` 把 Lavner 的「limited evidence」标为 `DIRECTION_NOT_SUPPORTED`（明确反证）**同样标过头了**——
> 来源说的是 limited evidence + 妻子侧 null，**不是 explicit refutation**；丈夫侧逐字「**Consistent with the incremental change model**」。

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

**R04 的结构性发现（比任何单个数据集的优劣都重要）**：**在 R04 本次审计的 15 个数据集上，这四个条件的交集为空。** 因此 `#29` F 层要求的**跨数据集泛化在本次审计范围内不可执行**。

> **🔴 Round 3（`X-14` / `R-0.2` / `C-C29` `CONTESTED`）**：原文「**这四个条件的交集为空**」是一个
> **field-wide absence claim**，本文件的 X-14 规则不允许。可辩护的表述只有 search-scope 形式。
> **必须同时记录两条限定**（否则收窄仍不完整）：
> 1. **Add Health 从未进入结构检验。** `C-C26` / `C-C20`：D12 是被**许可**条件（`ACCESS_BLOCKED`）排除的，
>    **不是**被结构条件排除的；且 Add Health 官方文档确有 nomination / romantic pair 结构。
>    ⇒ 「被结构检验的 15 个数据集」这个分母**不包含** Add Health。
> 2. **许可轴 ≠ 识别轴**（`R-C5` / `R-C6`）。D15 / D12 / D13 同时标注两轴
>    （结构轴 = `MEASUREMENT_ONLY`，egress 轴 = `ACCESS_BLOCKED`），**不得**把两轴压成一轴。
> **本 child 未做任何新的数据集检索。**

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

- R11：24 × 10 矩阵共 **216 个判定格，其中 69 个 `MEANING_PRESERVED`；支撑这 69 格的 invariance 研究，本 `R11` packet 未检出任何一份**。这 69 格**不可计数、不可聚合、不可视为独立**；若 `U1` 失败，相关格必须**重做**而非重新标度。
  > **🔴 Round 3（`X-14`）**：原文写「**支撑它的 invariance 研究数 = 0**」是 field-wide absence claim。
  > 收窄后只主张检索范围内的未命中。**这不削弱该格的不可聚合性**——它由**格数**与**判据未执行**支撑，
  > 不由「研究数 = 0」支撑。**本 child 未重跑该检索。**
- R03 N6：ECR 两维度「正交」是**工具假象**——CMB 方法因子可把理论正交的 anxiety–avoidance 相关从 `.17` 推到 `.41`。
- R16：`invariance_level_tested` 不得默认为 `NOT_TESTED` 而不显式标注；`#29` 分层与 R16 协议一致，但两者都**未**执行。

### 6.4 语言与文化覆盖缺口

- R13：LHRM 现有 126 条 proxy，**本 `R13` packet 未检出任何一条带跨语言不变性证据**。跨语言模型可能在**无告警**的情况下把 proxy 归到错误构念上（实测：专建多语模型在被问哈萨克语时**输出吉尔吉斯语**）。
  > **🔴 Round 3（`X-14`）**：原文「**无一条有跨语言不变性证据**」是 field-wide absence claim，收窄为检索范围内的未命中。
  > **保留**后半句的风险陈述——它由**实测**支撑（多语模型输出吉尔吉斯语），不依赖那句 absence claim。
- R02（repair 后）：中文覆盖从 0 增至 5 条来源，其中 3 条带可核实数字，但**没有一条能承载裁决**；中文的 Liking↔RomanticAttraction、trust↔attachment-security、dedication↔satisfaction 三处估计，**在本 lane 的检索范围内未找到**。
  > **🔴 Round 3（`X-14` / `R-0.4` / `A-C29` `WRONG-SCOPE`）**：`02` §5.8 原文是
  > 「**再次确认**……这不是本轮检索不足，是文献里确实不存在」（中文 ESEM / bifactor）。
  > **该表述被推翻**：可辩护的只有「**本 lane 的检索未发现**」；**存在性否定需独立系统检索**。
  > **本文件不主张该存在性否定成立，也不主张它为假。**
- R11：3 处 `cross-cultural` / cross-jurisdiction 域泄漏无 invariance 支撑。

---

## 7. Recommended next Work Orders

> **全部为 `AI recommendation`。均不属本 Work Order 授权范围。**

### 7.0 Round 3 对本节的三处更正

#### 7.0.1 「**这是唯一的真正阻塞项**」已删除（`X-12` / `C-P9` / `R-L2` / `R-K8`）

> **原文（Round 1，逐字保留）**：「### 优先级 1 — 让验证门能够失败（**这是唯一的真正阻塞项**）」

**该说法不可辩护，理由有二：**

1. **数量矛盾**：同一文件 §2 自己把 `C-1` / `C-2` / `C-3` / `C-4` 标为「**（阻塞级）**」、
   `C-5` 标为「**（排序死锁）**」⇒ **4 阻塞级 + 1 死锁** 与「唯一」并存。
2. **成员不相交**：§8 的 `B-1…B-8` 与 §2 的 `C-1…C-8` **只有 `B-6 ↔ C-3` 一项对应**。
   ⇒ **不是「编号错乱」，是「分母不同」**。

**更根本的一条**：优先级 1 阻塞的是**验证程序**（门不能失败）；`WO-N2` / `WO-N3` 阻塞的是**内容**
（层归属与值类未定，则新能失败的门是在测一个未定 schema）；`WO-N6` 阻塞的是**经验接入**。
**三种不同的「阻塞」被压成了一种。** 正确的分类见 §8。

#### 7.0.2 排序依据已换（`X-12` / `R-L3` / `K-C45` / `H-F36`）

> **原文（Round 1，逐字保留）**：「> 全部为 `AI recommendation`。排序依据：**修起来便宜 / 收益大**。」

**该依据不成立**：实际排序把**唯一最贵的**（canonical mutation，需 Human 显式授权）打头，
把**最便宜的**（一次书目核对）垫底 ⇒ 遵循的是**架构依赖**，不是成本/收益。

**依 `ADJUDICATION_V1` **X-12**（`Priority is dependency-unlock order, not 'cheapness'`），
本节排序依据改为：**

> **Priority = 依赖解锁序（dependency-unlock order），不是「便宜性」。**
> 「收益大」这一半**成立**；「修起来便宜」只在**编辑工时**意义上成立，在**授权**意义上是**反的**。

**必须诚实记录的判断**：`19` 对 `N1 → N7` 的**依赖顺序判断本身是正确的**（`ADJ3` Q7 明文「应保留」）。
**被推翻的是它所陈述的*理由***，**不是它的*序列***。⇒ 本节**保留原序列**，只换依据表述。

#### 7.0.3 8 个 Work Order 已重分类（`X-12` / `C-P9` 第 3 点 / `R-L1` / `R-0.10` / `K-C44` / `H-F35`）

> **原文（Round 1，逐字保留）**：「**均不属本 Work Order 授权范围**，需 Human 授权后另行派发。」

**该句把两种不同性质的批准混为一谈**：(a) 因 **canonical mutation** 需 **Human 主权**批准；
(b) **仅**因 Work Order 边界而需**新派发**。⇒ 重分类为 **3 决策 + 3 派工 + 1 基础设施请求 + 1 书目核对**：

| 类别 | 成员 | 需要的是 |
|---|---|---|
| **决策**（canonical mutation，Human 主权） | `WO-N1` · `WO-N2` · `WO-N3` | Human / Architect 签署 |
| **派工**（新 Work Order 即可，**不需** canonical 批准） | `WO-N5` · `WO-N7` · `WO-N4` | 一次新派发 |
| **基础设施请求**（无裁决者，只能提请求） | `WO-N6` | egress 环境 + **数据存储决策**（需 Human 决策：数据落在哪、是否入库、许可/署名政策） |
| **书目核对**（先修引文，再检索） | `WO-N8` | 一次 bibliographic check，**不是**一个 Work Order |

### 7.1 决策类（dependency-unlock order）

#### 决策 1（原优先级 1）— 让验证门能够失败

**WO-N1｜Gate A 可证伪性修复 + 首次真实否决尝试**
- **类别**：**决策**（`docs/foundation/PARAMETER_CONVERGENCE_V0_1.md` + `AGENTS.md:62` ⇒ canonical mutation）。
- 内容（Round 3 已按 `C-P1` 改写范围，**不再**是「删 3 个 catch-all + 重跑 Fixture」那个版本）：
  1. `§2.6`（`:84` 后）补一条**带阈值**的 `KEEP` / `MERGE` / `REJECT` / `HOLD` 后果句，并定义 `:84` 中未定义的「**重要**现实句子」；
  2. `§15 Gate A`（`:707-715`）补一条 **leave-one-out ablation 步骤**；
  3. `§13` 诊断词表（`:641-649`）补 **`redundancy hole`** 一类，**并同步 `AGENTS.md:62`**（只改一处会造成 canonical 内部冲突）；
  4. `§2.2` + `§15 Gate C` 补后果句并把 Gate C 接上；给 Gate B 补一句 **pass criterion**；
  5. `§2.3`（`:57`）把「**仍可能**提供额外信息」改成**可证伪**形式；
  6. （可选）`§12`（`:590`–`:610`）为 6 项推测性排除补 **re-entry criterion**；
  7. （`ADJ3` 追加）**`§2.5` 的 10 层 × `§13` 的 10 类必须先合并**（两表重叠 7 项、各有 3 项只在一边）；
  8. （`ADJ3` 追加）`§2.1` / `§2.4` 补后果句或明写「无后果」。
- 依据：`R17-F1` / `A03`（三条独立一手复现：`I-C1`、`ADJ3` Q1/Q2/Q5、`EV1` §6–§7）。完整论证见 §1.4。
- **成本（Round 3 更正）**：约 **5–8 句文档编辑 + 1 个 ablation 步骤定义 + 1 个诊断枚举值**。
  **不需要新文献、不需要新数据、不需要新模型。** 变更面 = **4 文件 / ≥6 节**。
- **X-9：本 Work Order 的被检验对象必须写清（`L-C11` `CONTESTED` / `ADJUDICATION_V1` **X-9**）**：
  > **Fixture 001 是对「事实/观察/信念/行动/历史/provenance 的表示能力 + `MAPPING_FAILURE` 语义」的测试，
  > 不是「8 个关系状态构念都必要」的有效测试。** 其 core dyad 是**雇主↔雇员**
  > （`Miss Z. Carty <-> her 2020 line manager`，`VALIDATION_CORPUS_V0_1.md:56`），
  > **26 个原子事实是排班 / 停业 / 未付薪 / CAB / 申诉等机构性事实**（`C001`–`C026`）。
  > ⇒ **不得**用雇主–雇员机构性事实叙事去主张 8-basis 的必要性。
  > **构念极小性（construct minimality）需要一个独立的、承载构念的 benchmark set。**
  > **在那个 benchmark 存在之前，任何「8 维 basis 是最小充分集」的结论都没有证据基础。**
- 建议同时补上：`UNKNOWN`（材料不足）vs `MAPPING_FAILURE`（材料充分但表示装不下）的分离记账
  —— R07 的 C1 吸收规则已给出可检查形式。

#### 决策 2（原优先级 2）— 层位裁决（阻塞后续一切推导）

**WO-N2｜`PPR` / `Satisfaction` 层归属裁决 + 连带重新推导**
- **类别**：**决策**（`PARAMETER_CONVERGENCE_V0_1.md` §5/§9 ⇒ canonical mutation）。
- 内容：Human / Architect 裁决 C-1；若采纳 R17，须同时授权 R06 五族的**重新推导**（不是重新拟合）。
- **🔴 Round 3 状态更新（`ADJUDICATION_V1` X-1 / X-2 / X-3）**：
  - **`PPR` 层位在当前架构下已定**：`PPR_(i about j,t)` 保持 **BeliefState / 关系特异知觉**。
    信念可以有时间持续性与因果/动力学重要性，**不必**因此成为 Reality/DirectedRelationshipState 的坐标。
  - **`Satisfaction` 层位在当前架构下已定**：**Derived / evaluation-state candidate**，不是 primitive basis。
    晋升是**条件性且已预登记**的，**不由预测强度蕴含**。
  - **F3 改判**：`17` F3「层边界被经验文献反向排序」**作为架构主张被拒绝**，但其 Segal & Fraley 的
    动力学发现**保留为 dynamics evidence**；F3 改作**竞争性经验假说**登记（关于持续性/预测角色），**不是层位判决**。
  - **D7 vs R3 无逻辑矛盾**：采纳**条件性后果预登记**（若 `Satisfaction` 日后满足自身晋升判据，
    则 D7 / basis 冗余必须重新审计）。**现在不做 D7-vs-R3 二选一。**
  - 依据：C-1；`R-B12` / `ADJ1` Q1–Q3。
- ⚠️ **前置于 WO-N1 的是 Architect 裁决，不是 WO-N1 本身**；两者都属决策类，**可并行签署**。

**WO-N3｜`Unknown` 类型学统一**
- **类别**：**决策**（`AGENTS.md` + `CURRENT_ARCHITECTURE.md` §9 ⇒ canonical mutation）。
- 内容：以 R07 的 K4 双序 + 10 类 tag + C1–C6 传播规则为基线，吸收 R11 / R13 / R15 / R16 各自的分类，产出**单一受控词表**。
- **🔴 Round 3 补记（`R-K6` / `R-K7` / `E-C23`）**：原文写「`Unknown` 值类被**五**个 lane 各自重新发明」
  **计数偏低**——语料中至少存在**第 6 套**无值词表 `UNKNOWN_AS_OF` / `DOI_UNKNOWN_AS_OF_2026-09-27`，
  且它是**全语料使用最广**的一套。⇒ 改为「**至少六套**」。
  且**必须两轴分离**（`tag` 证据侧 + `applicability` 适用性侧），**不得**并成一个 14+ 值枚举
  （否则违反 `AGENTS.md:22`/`:24`）。见 §1 `N-A7`。
- 依据：`N-A7`；`ADJ3` Q8 `C-4`。

### 7.2 派工类（不需 canonical 批准）

#### 优先级 3 — 采样与语料（可与优先级 1 并行，且不需要 canonical 变更）

**WO-N4｜Case Bank Wave A 冻结**
- **类别**：**派工**（`docs/validation/fixtures/` ⇒ 仍是 canonical 面，**需 Human 确认**，
  但**不是**「canonical ontology 变更」那一类主权批准）。
- 内容：冻结 R15 的 3 份（`H v H` [2022] UKPC 3 / *The Mill on the Floss* Book 3–7 / `Dougherty v Dougherty` [2015] EWCA Civ 805），
  并落实 `#13` comment 2 的 `t0` / `INPUT|HOLDOUT` 分离。
- 依据：R15 Wave A；R15 明确「这 3 份不依赖任何待确认项」。
- **🔴 Round 3 补记（`R-H8`）**：`15_CASEBANK_EXPANSION.md` **无 lane 覆盖**（`I` / `K` 均声明未读），
  ⇒ R15 **不是**「Wave 1 全覆盖」意义上的上游依据。
- 附：R15 同时提出 `DERIVED_TRANSFORM`（T1–T5）作为新 fixture 类——**这是 Human 决定**，本 attempt 不主张。

**WO-N5｜Gate B 覆盖矩阵发布 + 清单对齐**
- **类别**：**派工**（新增研究文档 ⇒ 前者可做；可能的 foundation 清单对齐 ⇒ 需 `C-P7` 签署）。
- **X-10 双层记账（`ADJ3` Q4）**：缺口是**双层**的，两层要分开记账：
  - **层 1（零成本）**：三张清单与 `CURRENT_ARCHITECTURE.md:53-56` 的**文档对齐**。
    逐条映射结果：`sibling` → `亲属`（**蕴含**，未具名）· `parent–adult-child` → `亲属` + `照护`（**蕴含**）·
    `ex-partner` → `前任`（**逐字命中**）· `professional/cooperative` → `同事` + `合作`（**逐字命中**）·
    `adversarial/harm-asymmetric` → `敌对`（**部分**；`harm-asymmetric` 是不对称**轴**，不是 dyad **型** —— **类目错误**）
    ⇒ **4/5 逐字或直接蕴含，1/5 是类目错误**。
  - **层 2（有成本，本节不提议）**：`sibling` / `parent–adult-child` / `non-romantic friendship` / `same-sex`
    在 12 份语料里**零 core-dyadic 实例** —— **这需要采集，不是文档编辑**。
- **不得把层 1 的文档对齐当作层 2 的替代**（`ADJ3` 采纳并加强 lane `L` 的自我反驳）：
  > 既然研究域已声明、`AGENTS.md` 又禁止向下扩域，那 A12 **唯一可能的读法**就是「表示能力无证据」，
  > 而**表示能力的证据只能由 corpus 覆盖给出，不能由域声明给出**。

#### 优先级 5 — 投影层（条件新颖性最高）

**WO-N7｜以 `CITED_PRIMARY` 复核既有 fixture 的 LHRM 映射**
- **类别**：**派工**（不需 canonical 批准）。
- 内容：把 3 份已冻结 fixture 跑一遍 LHRM 映射，作为**可执行的首次 falsification 尝试**；
  R17 R3 写出的「唯一命题」（写不出就诚实降级为知识表示产物）是其候选。
- 依据：R17 §11 优先建议 ⑤；R14 NC-1；R13 的 6 个 representation-faithfulness 指标。
- **前提**：WO-N1 必须先完成，否则跑出来的是又一次不可否决的覆盖。
- **🔴 Round 3 补记（`R-G11` / `H-F20`）**：R13 的六项指标**不是充分**评估工具——
  **存在两个平凡策略同时最大化全部六项**（全部弃答 / 直接复制 fixture 的 status 列）。
  且 fixture 本身被抽取的文本与判定 gold 是**同一批文本的同一批标签**（对自己的 gold 不施加循环论证标准）。
- **注意 R13 的度量立场**：「抽取准确率」在本项目**无定义**（无 ground truth）。可用的替代是 6 个
  `representation faithfulness` 指标，且必须**同时报告 `CROSS_RUN_DISPERSION` 不得被当作精度**。

#### 优先级 4 — 测量（需要网络出口，不是需要设计）

**WO-N6｜数据集出口核实 + 构念内容核实**
- **类别**：**基础设施请求** + **数据存储决策**（`R-L8` / `L-C13`：`RECLASSIFY_AS_METHOD_LIMIT`）。
  拆为两件独立的事：
  1. **基础设施请求（egress）**：在**可访问 ICPSR / `pairfam.de` / Gutenberg / `wenshu.court.gov.cn` / `courts.ie`
     的网络环境**下，核实三份 `CALIBRATION_READY` 数据集实际**问了哪些关系状态构念**
     （R04 `U15`，这是 `N-A3` / `N-A1` 能否推进的唯一钥匙），并重跑 R15 §3 全部核实。
     **无裁决者**——只能提请求。
  2. **数据存储决策（需 Human 决策）**：数据落在哪、是否入库、许可/署名政策。
     **本仓库没有 data 面**（无 `data/` 目录）⇒ **即使 egress 通了，存储决策仍会阻塞 D04。**
- 依据：R04 `U15` / blocker `R-B-1`；R15 `U6`。
- **不得**以任何方式绕过 access / rights（Work Order 明确禁止）。

#### 优先级 6 — 定位（若考虑对外表述）

**WO-N8｜prior-art 定位补验** → **降级为一次 bibliographic check（`R-L7` / `L-C20` `REJECT`）**
- **类别**：**书目核对**。**先修引文，再检索。**
- **原 Work Order 已撤销**，理由：`WO-N8` 要核的 `Boyd & Heewer (2007)` 极可能是
  **Boyd & Hilton (2007), *The law of the wed: A lateral theory of marriage*, Cognition**（Heewer 是第三作者）
  ⇒ **`WO-N8` 自己的前提引文就带一处与它要复核的 prior art 同类的作者错误。**
- **范围收窄**：`14` §9.1 / §9.2 的两项「最高优先未核实 prior art」极可能**都是不存在的引用**
  （`H-C24`）：`Acitelli & Antonioni (2006)`（JPSP 90(6)，Crossref 该期无此文；真人姓氏是 **Antonucci**）·
  `Boyd & Heewer (2007)`（Crossref `query.author=Heewer` = **0 results**）。
- **本 child 未做任何新的外部检索。** `Acitelli & Antonioni (2006)` 的状态保持 **`UNKNOWN`**，
  **不代判为「不存在」**（`X-14`）。
- **在此之前不得对新颖性做任何表述。**

---

## 8. 未解项登记表（终态 · **唯一编号空间**）

> **🔴 Round 3（`X-12` / `C-P9` / `R-4` / `R-L4` / `R-L6` / `H-F34` / `H-F39`）**：
> 本节是**唯一一份**未解项登记表。`00_MANIFEST.md` §4 现在只提供状态注记，**不引入新编号**。
> §2 的 `C-1`…`C-8` **保留为历史 Round-1 记录**（不改写历史），但不再是分类依据。
>
> **同时修掉的三处 register 缺陷**（`R-4`，`ADJ3` Q8：**不修就会让 join 产出错误数字**）：
> 1. **`B-3` 编号冲突** —— 原 `19:343` 的 `B-3` = ESEM 负结果；`00_MANIFEST:125` 的 `B-3` = 跨 lane 全局去重
>    （并指向 `§4 B-9`），而 `:131` 的 `B-9` = **同一件事** ⇒ manifest **内部**重复编号。
>    **本轮把全局去重并为单一 `R-B-9`。**
> 2. **成员不相交** —— 原 §8 的 `B-1…B-8` 与 §2 的 `C-1…C-8` **只有 `B-6 ↔ C-3` 一项对应**；
>    `C-1` / `C-2` / `C-4` / `C-5` / `C-6` 在 §8 无编号。
>    ⇒ **这不是「编号错乱」，是「分母不同」**（H-F39）。
> 3. **`B-4` 双重分类** —— §1 `A9` 当作重要负结果，§8 当作 blocker ⇒ **同一份文件对同一件事给了两种分类**。
>    **本轮把 `B-3` / `B-4` 移出 blocker 列表**（归 `D` 类）。
>
> **四条分类的定义**（`ADJ3` Q8 + `K-C44` + `L-C17`/`L-C18`）：
> **负结果不是 blocker。** 成员划分依据是「**解决它需要谁做什么**」，不是「它有多痛」。

### 8.1 A 类 · 架构设计任务（4 项 · 需 Human / Project Architect 裁决）

| id | 未解项 | 证据指针 | 需要什么 |
|---|---|---|---|
| **`R-B-6`** | **Gate A/B/C 在当前定义下不能产生否决**（`MAPPING_FAILURE` 类型上不可达） | §1.4 `N-A8`；`R17-F1/F9/F11`；`A03` `T1/T2/T3`；`H-A1`/`H-A2`/`H-A3` | 一次 canonical 变更签署（`C-P1`）+ `AGENTS.md:62` 镜像同步。**成本已降级为 ~5–8 句文档编辑** |
| **`R-B-10`** | **`PPR` / `Satisfaction` 层归属**（原 `C-1`） | §2 `C-1`；`X-1`/`X-2`/`X-3` | 一次层位裁决。**X-1/X-2 已把当前架构下的答案定死**（`PPR` = BeliefState；`Satisfaction` = Derived）；未决的是**是否登记条件性后果预注册**（`C-P8`） |
| **`R-B-11`** | **`OutcomeDependence` 被四种互斥 ontology 指派**（原 `C-2`） | §2 `C-2` | 一次 ontology 裁决。这是**唯一**支撑 `PowerImbalance` 派生链的候选（见 §1 `N-A1`），也是 `L2` `APES` 的 `HOLD` 阻塞点 |
| **`R-B-12`** | **`Unknown` 的类型学**（原 `C-4`） | §2 `C-4`；§1 `N-A7`；`E-C23` | 一次类型学裁决。**必须两轴分离**（证据侧 `tag` + 适用性侧 `applicability`），**不得**并成 14+ 值枚举 |

> **原 §1 `A3` 的「`OutcomeDependence` 关系级无可用工具」**不在 A 类：它是**测量任务**，不是架构任务。
> 它以 **`R-B-8`（B 类）** 登记。

### 8.2 B 类 · 研究设计任务（2 项 · 需统计 / 测量专家 + Human 授权采样，**不需架构裁决**）

| id | 未解项 | 证据指针 | 需要什么 |
|---|---|---|---|
| **`R-B-7`** | **`Liking ↔ RomanticAttraction` 仍缺同样本斜交因子相关 / CFA 判别检验** | `E1` 维持 `CONTESTED`（R02 repair 后仍如此） | 一次专门设计研究（`L-C15` 的 E1 缺口清单） |
| **`R-B-8`** | **`OutcomeDependence` 关系级可测性** —— **在本 attempt 已审计的仪器范围内未定位到 validated 工具** | `19` §6.1 `G1`；`03` §2.7 + §2.3 缺口表 `G1`；`10` §7/§8 `G1–G16` | 一次专门设计研究。**注意措辞**：`C-W5` 判「结构上不可测」的降级建议**整体打回** —— 工具阻塞应写「**未定位到已验证的关系层 dependence 工具；且经典互依工具文献未被检索**」，**不是**「结构上做不到」 |

### 8.3 C 类 · 环境 / 治理限制（3 项 · **无裁决者**，contract §3 禁止绕过）

| id | 未解项 | 证据指针 | 需要什么 |
|---|---|---|---|
| **`R-B-1`** | **网络出口不可达**（`icpsr` 403 / `hrs` / `saflii` 403 / `courts.ie` / `wenshu` / `gutenberg`）⇒ 三份 `CALIBRATION_READY` 的**构念内容**未核实；R15 的 7 条来源仍 `UNVERIFIED_CANDIDATE` | `R04` `U15`；`R15` `U6` | **基础设施请求（egress）+ 数据存储决策**。Work Order 禁止绕过 access / rights ⇒ **不得**以任何方式规避 |
| **`R-B-2`** | **一个来源不可得** —— R11 的 Gilligan / Kleemans / Rodriguez (2017) ASR 记录经 10 路检索**在检索范围内确认不可得**；Parsons & Bales 1955 原件同 | `R11` `UNVERIFIED_AGENT_RECALL` 条目 | **无人可裁决**。已记为**该来源在本 attempt 内**的永久缺口。**⚠️ `X-14`：这是 search-scope 断言，不是「该文献不存在」** |
| **`R-B-5`** | **`#20/#21/#22` 隔离 lane 的 durable 结果仍未知** | `R13` 记录的 `U-5`（fixture 上人工 verifier 的真实 ICR）因此无法回答 | **无裁决者**。按隔离契约本 attempt 不查、**不引用、不猜测其内容** |

### 8.4 D 类 · **负结果，不是 blocker**（2 项 · 必须移出 blocker 列表）

> **`ADJUDICATION_V1` X-12 明文：「Negative results are not blockers.」**
> 这两项**曾经**占着 `B-3` / `B-4` 两个编号。本轮把它们**移出** blocker 列表并重新归档。
> **`ADJ3` 明确：留一个「待修的负结果」长期占编号，本身就是下一轮误引用的入口。**

| id | 负结果 | 正确归档 | 证据指针 |
|---|---|---|---|
| **`R-B-3`** | **R02「全候选电池单次 ESEM / bifactor」在文献中未找到** | **`NEGATIVE_RESULT`** —— `R02` 自陈 `NEGATIVE`、非「未找到」。**🔴 `X-14` / `R-0.4`：`02` §5.8 原文「这不是本轮检索不足，是文献里确实不存在」被推翻**；可辩护的只有「**本 lane 的检索未发现**」，存在性否定需独立系统检索 | `R-0.4` / `A-C29` `WRONG-SCOPE` |
| **`R-B-4`** | **R09：迟滞在二元关系数据上无任何已发表估计** | **`NEGATIVE_RESULT` 级 `UNKNOWN`** —— `F-C1` 自陈「**在已检索场所内未找到**」≠「不存在」；`09` §5.3 自认五条覆盖缺口。**不得**与 `R-F1` 混用（`R-F1` 的推论错，但 `R-F2` 的 `UNKNOWN` 标签正确） | `19` §1 `N-A5`（原 `A9`）；`R-F1` / `R-F2` |

> **⚠️ `N-A5` 里原 `A9` 的一处量纲错误已修（`R-F1` / `EV3` Claim 3(b) `REFUTED`）**：
> 原文「其必要前提**在多数真实 dyad 中不成立**」是**研究层 → dyad 层**的量纲错误
> （`Mayo` 报告的是 k 项研究的合并相关，抽样单元是**研究**不是 **dyad**；`I² = 76%` 恰恰意味着研究间不一致，
> 进一步阻止向 dyad 层外推）。**替代表述**：**当前可用的耦合代理与关系结局关联弱且 `I² = 76%`、
> 情绪协动超伪伴侣仅 14–38%`——这是一个方法/测量事实。引用这组数字时必须同时带 `I² = 76%`。**

### 8.5 E 类 · 尺度冲突（1 项 · 需 Human / Architect；同 A 类但登记在 §2）

| id | 未解项 | 证据指针 | 需要什么 |
|---|---|---|---|
| **`R-B-14`** | **尺度冲突 `CR-7`**（原 §2 `C-6`）：R06 的 C-A 约束要求**事件内分辨率**（否则无法分离「对方行动改变了我的状态」与「同一测量窗口内共同生产」）；R09 O8 提议把 `tau` 固定在月—年级并拒绝该词汇；而 R03 的仪器台显示**月—年级尺度上根本没有 `Trust` / `Dedication` 的 state 工具** | §2 `C-6` | 一次尺度裁决。**三者不可能同时满足** ⇒ 这是**真冲突**，不是缺口 |

### 8.6 已关闭项（不再是未解项）

| id | 项 | 状态 | 依据 |
|---|---|---|---|
| **`R-B-9`** | 跨 lane 全局去重（原 manifest 同时记作 `B-3` 与 `B-9`，**同一件事两个编号**） | **已完成**，但**不得对外声称 lane 自报数之和** | 见 §8.7 |

### 8.7 登记表的记数字账（**`M-2` / `M-6`**）

> **原文（Round 1 §8 方法学缺口第 1 条，逐字保留）**：
> 「- 跨 lane **全局去重**已由 A04 完成（1,199 原始出现 → 642 distinct pointer → 533 distinct source，
> 其中 `PEER_REVIEWED_*` **350**）。**各 lane 自报数相加 ≈1,201 不成立，高估 2.3–3.4×。**
> 因此**不得**对外声称「1,201 个独立来源」。」

**取代它的表述**：

| 项 | 值 | 说明 |
|---|---|---|
| 各 lane 自报数之和 | **878** | 不是 ≈1,201。相对 **533** distinct source 高估 **1.65×**、相对 **350** 高估 **2.51×**（不是「2.3–3.4×」）。**本 child 2026-09-27 逐项解析 `00_MANIFEST.md` §3 的 18 个 addend 后相加，未复制任何旧总数** |
| `1,199` 是什么 | **原始出现次数** | 与「lane 内去重后计数」**不是同一量纲**。**四个数（878 / 1,199 / 642 / 533）只能算比值，不能相互校验或替代** |
| `642 − 109 = 533` | **仍成立** | 本轮未触及 |
| tier 表逐行加总 `= 533` | **仍成立** | 本轮未触及。**但 `350` 只能读作「350 个同行评审来源」**，**不是**「350 份一手经验数据」，也不是「真正承载科学重量的数字」 |

**其它记账缺口（Round 3 更正）**：

- ~~「A04 与 A01 各自的 DOI 抽样**不重合**，两次审计的合并覆盖率未单独计算。」~~
  **【Round 3：`K` 独立实测为伪 —— 语料重叠 352/363。**原文把一个**已被机器否证**的印象当事实记录，且方向是
  **高估**审计的独立性。**取代它**：「A01 与 A04 的 DOI 语料重叠实测 **352/363** ⇒ 两次审计的独立性
  **远低于**其表面印象；两次审计**不构成相互独立的复现**。**本 child 未重跑该计数，沿用 `K` 的机器计数。**】**
- **🔴 「`02b` 依赖 `R04` / `R06`」是本文件唯一的硬事实错误（`R-B22` / `K-C12` `VERIFIED` 为假），已撤回。**
  > **原文（Round 1 方法学缺口第 3 条，逐字保留）**：
  > 「- 报告体量的**最小可解释性**：`02b` 的多数结论依赖 `R04`/`R06` 的 sibling 输出，而 R04 与 R06 之间
  > **从未互相读取** ⇒ 存在一条未被任何单点研究覆盖的依赖链（A02 已标记为 CR-7 尺度冲突）。」
  >
  > **撤回理由（本 child 2026-09-27 机器复算，`.md` 全文正则计数）**：
  > `02b_CONSTRUCT_REDUNDANCY_AUDIT.md` 中 `\bR04\b` = **0**、`\bR06\b` = **0**、
  > `04_DATASET_LANDSCAPE` = **0**、`06_TRANSITION_LAWS` = **0**、`pairfam` = **0**、
  > `APES` = **0**、`DVA` = **0**、`BMR` = **0**、`RGM` = **0**。⇒ **零引用。**
  > **这条硬事实错误出现在「诚实记录自身缺口」的段落里。**
  >
  > **真实的依赖链是 `R06 → R02`（方向相反，且是单向的）**：
  > - `06_TRANSITION_LAWS.md:902` 律 B 的「与架构的关系」格写「支持 `Dedication` 独立（**待 R02 裁决**）」；
  >   `06:1009` 写「**不要在 R02 完成之前把 `Dedication` 视为已收敛**」。
  >   ⇒ **R06 律 B 的 `Dedication` 层级是取自「见 R02 的裁决」的。**
  > - 而 R02（`02b_CONSTRUCT_REDUNDANCY_AUDIT.md:439`）的 **`H2` 判 `CRITICAL`**
  >   （`Dedication` ≈ `Satisfaction` + `Investment` + `Alternatives`）**从未被 R06 消费**。
  > - 反向核对：`02` 中 `\bR06\b` = **0**、`06_TRANSITION_LAW` = **0** ⇒ **这条链是单向的 `R06 → R02`。**
  > ⇒ **未被任何单点研究覆盖的依赖链确实存在，但它的两端是 `R06` 与 `R02`，不是 `02b` 与 `R04`/`R06`。**
  > **本 child 不主张这条链导致任何具体结论为假** —— 只主张**原文的那条链不存在**。

---

## 9. 本文件明确不主张

1. **不主张** 本文件或本目录下任何文件是 canonical architecture、参数表、公式 SSOT、schema 或验证依据。
2. **不主张** §1 的任何 `N-A*` 条目为「已确立」。它们记录的是**若干独立来源指向同一处**，不是该处为真。
   **【Round 3】** 原 §1 的 `A*` 已被 `N-A*` 取代（`X-8`）。
   **并且**：`N-A6` 的强度上限是 **`CONTESTED`**、不是收敛结论；`N-A7` 标 **`NOT_COUNTED_AS_AGREEMENT`**；
   `N-A8` 记录的是一个**门不能失败**的缺陷，不是「门已失败」；`N-A9` / `N-A10` 的 `independent_sources` 都是 **1**。
   **「12」这个数字必须读作「5 存活 + 5 降级 + 2 移出」，不是「12 条稳健一致」。**
3. **不主张** §4 的 5 条律为真 —— **【Round 3：依 `X-11`，没有任何一条 transition law 被验证或冻结】**。
   `L1` = `HOLD`（只保留单向版本）· `L2` = `HOLD`（待关系级 `OutcomeDependence` 测量）·
   `L3` = `HOLD`（只保留为 **level-conditional-slope 候选**；「最佳可得证据逆向于增量通道」这个 framing 已删除）·
   `L4` = `HOLD`（待 `Ideal` 来源核实）· `L5` = `MODEL_HYPOTHESIS / UNTESTABLE_WITH_CURRENT_ORDINARY_WAVE_DATA`。
   **三处承载源（`S04` Joel 2020 / `S19` Lavner Table 5 / `S31`-`S17` Ideal）标 `PENDING_EVIDENCE_CHECK (R3-E3)`** ——
   本文件对它们**既不确认也不否认**。
   **也不主张「`B2_STABLE_LEVEL` 被 `B1` 在所有报告口径下严格数学支配」** —— 本文件明确**不**主张这一点。
4. **不主张** §5 的数据集**已被获取、已下载、已打开或已跑过映射**。全部为 suitability 描述，零数据接触。
5. **不主张** §6 的任何缺口可由「多找几个量表」关闭。G1/G2/G3/G6/G9 是**架构级**缺口。
6. **不主张** 本 attempt 的文献数量、child 数量或一致性构成任何形式的 validation。
7. **不主张** 本 attempt 对 §2 的任何矛盾作出了裁决。**全部留给 Human / Architect。**
8. **不主张** `AGENT_RECALL` / `UNVERIFIED` / `POINTER_ONLY` 级来源可承载任何裁决。
9. **不主张** 本 attempt 读取、执行或引用了 LHRM `#20` / `#21` / `#22` 的任何内容；未写 Eye / Juece；未做 merge。
10. **不主张** R17 的项目取舍判断（§3 末段）是结论。它是**一个独立红队的保留意见**，采纳与否属 Human。

### 9-R3 Round 3 追加的 non-claims（`A2`）

11. **不主张** Round-2 review swarm 的任何外部实证主张为真或为假。`N-A1`–`N-A12` 的
    `independent_sources` 审计是**关于项目自身文档文本的**（`PROJECT_PRIMARY`）——
    它判定「几条 lane 转引同一篇 study」，**不判定那篇 study 的结论**。
    本 child **未做任何新的外部取样**，`S04` / `S19` / `S31` 全部 `PENDING_EVIDENCE_CHECK (R3-E3)`。
12. **不主张** `1,199` / `642` / `533` / `350` 任何一个被本轮修正触及。§8.7 只重算了
    **lane 自报数之和 = `878`** 与两个倍率（`1.65×` / `2.51×`）。`533` 仍是**上界**，本轮未上调也未下调。
    **且不主张 `878` 是「独立来源数」** —— 它是 lane 自报数之**和**，与 `1,199` / `642` / `533`
    是**四个不同量纲**，只能算比值。
13. **不主张**「1,201」这个旧值是「错的统计」—— 它的**加总**与正确值不符（`878`），
    但 `1,199`（原始出现次数）**本身没有被推翻**，它只是**不同量纲**。
14. **不主张** §1.0.1 的「5 + 5 + 2」逐条归档是 `ADJ3` 的原话。`N-A11` 归「移出」是 `X-8` 明文；
    **`N-A7` 归「移出」是本 child 的判断**，理由是它自己的来源计数未 reconcile。
    若 Architect 认为 `N-A7` 应回到「存活」档，则分布变成 6 + 5 + 1。**本 child 不代替 Architect 决定。**
15. **不主张** Gate 缺陷的**修法**已获签署。§1.4 给出的是**准确的最简描述**与**已降级的成本**；
    `WO-N1` 仍需 Human / Architect 签署，且**变更面（4 文件 / ≥6 节）大于其新增文字量**。
16. **不主张** Fixture 001 能检验 8 个关系状态构念的必要性（`X-9`）。它的 core dyad 是**雇主↔雇员**，
    26 个原子事实是**机构性事实**。**构念极小性需要一个独立的、承载构念的 benchmark set，本文件不提供该集合。**
17. **不主张** `#20` / `#21` / `#22` 的内容。**未读 / 未执行 / 未引用**，不猜测。
    `R-B-5` 的状态一律 `UNKNOWN`。
18. **不主张** §1.1 表中任何 `Lanes`→`independent_sources` 的映射之外的东西。列的替换只回答
    「几个**独立来源**指向同一处」，不回答「该处是否为真」。

---

## 10. Round 3 冲突登记（adjudication V1 vs Round-1 swarm 原始主张）

> 契约要求：「实现 adjudication V1 的裁决，不是 swarm 的原始主张。凡两者冲突，一律以 adjudication V1 为准，
> 并在 packet 里记录该冲突。」本节是**文件内**的冲突登记（完整清单见 packet `R3_A2.md` §5）。

| # | Round-1 swarm 的主张 | adjudication V1 的裁决 | 本文件落地位置 | 性质 |
|---|---|---|---|---|
| 1 | `A1`「`MERGE` 与 `REJECT` **从未被签发过一次**」 | 项目层为假；正确表述是「8 项 basis 从未被**能失败的门**删减过」 | §1.4 第 3 条 · §3 表下注 | **支撑论证被推翻**（缺陷保留） |
| 2 | `A1`「`§2.6` 是**唯一**能删除 construct 的准入侧判据」 | 全称量词为假（六条里 1 删 / 2 降 / 3 无后果） | §1.4 第 2 条 | **支撑论证被推翻**（缺陷保留） |
| 3 | `A1`/`A10` 合计「12 条 robust agreements」 | `N-A1`…`N-A12`；报 `independent_sources × methods`；`=0` 不得进表 | §1 全部 | **呈现方式取代** |
| 4 | `A1` 的严重性「昂贵 canonical patch + 重跑 Fixture」 | ≈**5–8 句文档编辑 + 1 ablation 步骤 + 1 诊断枚举值** | §1.4.1 · §7.1 决策 1 | **严重性下调** |
| 5 | `A10`「3 个 catch-all」「§14 Step 3」 | **4** 个 catch-all；`§14` 无编号 step，真实位置 `§14:679` + `§15 Gate A` 第 3 步 | §1.4 第 5–7 条 | **数字与指针更正** |
| 6 | `A1` 把 `AGENTS.md:62` 当第二个独立来源 | **1 primary file + 1 镜像** | §1.4 第 6 条 | **独立性更正** |
| 7 | §7「**这是唯一的真正阻塞项**」 | 删除；四分类 + 依赖解锁序 | §7.0.1 · §8 | **框架取代** |
| 8 | §7「排序依据：**修起来便宜 / 收益大**」 | `Priority is dependency-unlock order, not 'cheapness'` | §7.0.2 | **依据取代，序列保留** |
| 9 | §7 8 个 WO 一律「需 Human 授权」 | 3 决策 + 3 派工 + 1 基础设施请求 + 1 书目核对 | §7.0.3 | **分类取代** |
| 10 | `WO-N1` 用 Fixture 001 检验 8 维 basis | Fixture 001 测**表示能力 + mapping-failure 语义**；极小性需独立 benchmark | §7.1 决策 1（**X-9**） | **被检验对象更正** |
| 11 | §4 五条律「值得以后冻结」 | **无律被冻结**；逐条 `HOLD` / `MODEL_HYPOTHESIS` | §4 表 | **状态取代** |
| 12 | §4 `B2` = `SELECTION_ONLY` | `B2_STABLE_LEVEL`；R06 `Level+RW` 独立；诊断基线非普适硬门；加 `N7`/`N8` | §4.1 | **命名与角色取代** |
| 13 | 四条件交集「为空」（field-wide） | search-scope；Add Health 从未进入结构检验 | §1.3 `X-14-7` · §5 | **范围收窄** |
| 14 | 「12 份语料」= Gate B 既有语料面 | **2 `direct-use` / 10 `needs cleaning`**；无单一分母 | §7.2 `WO-N5` | **分母更正** |
| 15 | §8 方法学缺口「`02b` 依赖 `R04`/`R06`」 | **零引用**；真实链是 `R06 → R02` | §8.7 | **硬事实错误撤回** |
| 16 | §2 `C-8`「`10.31219` 是 OSF project 前缀」「`10.31219` 404」 | 两前缀**都 live**、同一 registrant；`f6wbn` 只在 `10.31234` + `_v1` 注册 | §2 `C-8` | **支撑论证被推翻** |
| 17 | §8 方法学缺口「A01 与 A04 抽样不重合」 | 语料重叠实测 **352/363** | §8.7 | **方向相反的错误** |

### 10-R3 Round 3 落地清单（逐条可 grep）

| 裁决 | 落地位置 |
|---|---|
| **X-8** | §1 全部重写（`N-A1`…`N-A12` 表 · 5+5+2 分布 · §1.2 两处非独立性 · §1.5 `N-A11` 移出） |
| **X-9** | §7.1 决策 1 的「被检验对象」段 |
| **X-11** | §4 表（逐条裁决状态列）+ §4.1 + `PENDING_EVIDENCE_CHECK` 清单 |
| **X-12 / C-P9** | §7.0.1 · §7.0.2 · §7.0.3 · §8 全节（`R-B-*` 五分类唯一 register） |
| **X-14** | §1.3（`X-14-3`…`X-14-11`）· §2 header · §5 `R04` 结构性发现 · §6.3 · §6.4 · §7.2 `WO-N5` · §8.3 `R-B-2` · §8.4 `R-B-3` |
| **X-6 / C-P10** | §4.1 null registry（`B2_STABLE_LEVEL` · `N7` · `N8`） |
| **Gate rationale** | §1.4（`N-A8`）+ §1.4.1 + §3 表下注 |
| **sibling `A1` `C2`** | §2 `C-8` |
| **sibling `A1` `C3`（`19` 侧）** | §8.7（`878` / `1.65×` / `2.51×`） |
