# A03 — 可证伪性 / 事后拟合审计（Falsifiability & Hindsight-Fitting Audit）

- **Status**: `RESEARCH_CANDIDATE` — 不得作为 canonical 修改依据
- **As of**: 2026-09-27
- **Round-3 repair**: 2026-09-28（child `A4b`，branch `r3/a4b`）
- **Lane**: A03（Wave 2 cross-lane audit，`youling/lhrm#30@overnight-opencode-exploration-swarm-v1`）
- **Authority**: 本文不修改任何 canonical doc；所有"改写"均为**判据草案**，非 schema / 律 / 参数变更

---

## §R0 Round-3 修复声明（2026-09-28，child `A4b`）

**权威**：`youling/lhrm#30 comment 5854920569`（`ARCHITECT_ADJUDICATION_V1`）+ `youling/lhrm#30 comment 5854930069`（`ARCHITECT_ROUND3_DISPATCH_V1`）
+ `docs/research/overnight-2026-09-27/review-r2/`（`CONTESTED_FINDINGS.md` X-1 / X-2 / X-3 / X-8 / X-10 / X-12 / X-14；
`HIGH_CONFIDENCE_FINDINGS.md` §A（H-A1…H-A5）、H-F24…H-F28、H-F31、H-F33；
`REJECTED_OR_WEAK_FINDINGS.md` §R-I、§R-K、§R-4）。

**本节的作用**：Round 2 的评审发现 A03 自身有若干**可被再次误引**的表述、一处过窄的 scope 判定、三处自相矛盾的计数与一处悬空指针。
本节先给出**取代关系**，再在正文逐处落地。**取代原则 = 原文保留 + 标注取代**，不静默删除（`AGENTS.md` Mutation discipline）。

| # | 本报告的原始表述（**保留**，逐字） | 取代它的表述 | 取代依据 |
|---|---|---|---|
| **R-A** | `19:35` / `19:182`：「A03 把该主张修正为 **8/11**」 | **A03 从未提出 `8/11` 这个数字。** A03 驳回的是**措辞**（`§1.4` `F9` 要点 2 → 「**需更正**。11 类中**前 8 类是 scope / context 标签**」；`§7.1` `X-5` → 「8/11 是 scope 标签」；`§7.2` `N-A03-6` → 「字面表述 8/11 不成立」）。**A03 自己的结构是 8（抽样框 scope 标签）+ 3（构念组合复述）= 11，全部项目自产。** | `HIGH_CONFIDENCE_FINDINGS.md` H-A4；`§1.7` 为 A03 侧的独立重算 |
| **R-B** | `§1.3` 裁定：「**只有 §2.6 需要改写**」 | 六条判据**全族**都缺后果/程序/阈值/执行者；scope 判定**必须扩宽**（`§2.3` 标题与内容已改） | `H-A1`（`EV1` §9 要求变更面从 1 文件/2 节扩到 4 文件/≥6 节，含 `§2.1`–`§2.6` 全族）+ A03 自身逐条复核 |
| **R-C** | `19:282`：「§13 的 **3** 个 catch-all」 | **4 个** catch-all 类（`Environment` / `History` / `Derived-Narrative-only` + `Provenance/Uncertainty` 自由文本槽）**加** 1 个诊断出口（`merely narrative/irrelevant`）= **6 条逃逸通道**。**方向：synthesis 少算一个，把缺陷说得比 A03 小。** | `H-A3`；`PARAMETER_CONVERGENCE_V0_1.md:618-629` + `:641-649` + `AGENTS.md:62` |
| **R-D** | `§1.4` `F1` 行把 `MAPPING_FAILURE` 不可达归因于**单一** catch-all 机制 | **三个**文本上互不相同的机制，作用于流水线**三个不同阶段**；来源 = **1 份 primary + 1 份逐字镜像**（不是两个独立来源） | `H-A3`；`§1.4` 已改为三机制表 |
| **R-E** | `§2.6` 表：`SPAN_SUPPORT_RATE` / `ENTITY_INSERTION_RATE` 标 **`NOT_COMPUTABLE_ON_FIXTURE_003`** | 范围 = **三份 fixture 全部**，成因**两类**（`§2.6` 已改；`H-3` 已改） | `REJECTED_OR_WEAK_FINDINGS.md` R-I6 |
| **R-F** | `§1.3` / `§2.9` / `N-A03-3`：「`MERGE` 与 `REJECT` **一次也没有出现**」「在整个构念审计中**从未被签发过一次**」 | 这是**单份报告的词表使用率**，不是项目级事实。改为 **report-scoped** 陈述，并记录**把它提升为项目级事实这个动作本身**才是错误来源；另记录 token 计数细节（`§1.6`） | `H-A3` + A03 自身 token 复算 |
| **R-G** | `§1.4` `F11` 行：「`Step 3` ……§14 line 679」 | `§14` **无任何编号 step**。该 step 实际住在 **`§15` Gate A 第 3 步（`PARAMETER_CONVERGENCE_V0_1.md:713`）**；门槛句在 **`§14:679`**。两处都已指明（`§1.4` 已改） | `H-A3`（同一条悬空指针在 `19:102` 被复制） |
| **R-H** | `§4.4` 第一层：`NO_REWRITING_FOUND`，标为「最重要也最可核的一条**否定结果**」 | 降级为「**方向很可能对，覆盖不完整**」：缺 **R04** 与 **R10** 两条 lane（`§4.4` 已改） | `REJECTED_OR_WEAK_FINDINGS.md` R-I5 |
| **R-I** | `§1.6`：「§2.6 ……**在结构上永远不能触发**」 | 「**§2.6 承诺了一个 Gate A 不包含的检验**」——一条关于自身可测性的**未兑现承诺**，可作**可验证的内部不一致**记录（`§1.6` 已改） | `H-A2` |
| **R-J** | `§2.8` 行：「R17 `R1–R6` —— 6/6 `HAS` / `EXECUTABLE_TODAY`」 | **五条可触发、一条不可判定**（R6 不是实验）；并给出两条优先项（`§2.8` 已改） | A03 自身逐条重判（`§2.8`） |
| **R-K** | `§2.5` 末注「19 条中 14 条 `HAS`、**5** 条 `UNFALSIFIABLE*`」；`§2.9` 合计 `10 (8%) / 33 (25%) / 38 (29%)`；`§2.2` 注「13 条中 **7** 条（54%）不会因任何观测改变」；`§10 NR-8` 的「86 条 / 38 条」 | **三处 A03 自身的计数不自洽**，逐行重数后为：R07 = `14 / 2 / 3`（不是 `14 / ? / 5`）；`§2.9` 合计 = `86 (66.2%) / 13 (10.0%) / 31 (23.8%) / 42 (32.3%)`（求和式已列出，可复算）；R01 = `4 / 5 / 4`（不是 `3 / 5 / 5`）；R01「不会因观测改变」上界 = **9 条（69%）**，早先的 7 是更窄分组（`§2.2` 注） | 本报告 Round-3 逐行重数（求和式见 `§2.9`）；**`H-A1` 只要求换理由，不涉及本条**，本条是**本报告自查发现的第三处内部不自洽** |

> **X-14 适用**（`§11.5`）：本报告此后把一切**领域级/字段级**否定陈述改写为**检索范围陈述**。
> 例：不再写「仓库内不存在 Fixture 003 的原文」，改写为「**在本仓已提交材料中**检索不到 Fixture 003 的原文」。

> **未在本节实现的事**：`§4.1` 的泄漏列拆分建议**只登记为路由项**（属 Validation Gates PR / `C-P6`），本报告**不实施**；
> `§4.5` 的 `VALIDATION_CORPUS` 文档级冲突**修法在 canonical**，本报告**只记录**（`§4.5`）。

> **本报告的立场。** 本批其它报告审计的是**结论**（证据强度、跨 lane 矛盾、引用来源）。本报告审计的是**仪器**：
> 每一条拟议的律 / 裁决 / 不变量 / 指标 / 门，在其**判据原文**下，究竟有没有一个可能的观测结果能让它失败。
> 判定标准只有一条，且逐条回答：
>
> > **「在判据原文下，什么样的结果本来会被算作失败？」**
> > 答不出这句话的条目，一律不计入"已可证伪"。

> **本报告的一条方法论取舍。** 本报告**未打开任何外部来源**。全部 finding 都是关于**项目自身文档文本**的主张，
> 证据形态是 `PROJECT_PRIMARY`（仓库文件 + 行号）与 `WAVE1_PRIMARY`（sibling 报告 + 行号）。外部文献指针数为 **0**。
> 代价：本报告**不能**对任何外部实证结论的正确性发表意见。

### §0.0 独立性声明与**未声明的暴露面**（Round-3 补记）

**与 `17_RED_TEAM_FALSIFIERS.md` §0 独立性声明的关系**：A03 **实读了** sibling lane 的 durable 报告（这是 A03 的使命所必需），
**没有**声称「未读任何 sibling 产出」。A03 声明的是更窄的一条：
**A03 的第一批 packet 证据形态包含 `WAVE1_PACKET_PRIMARY`**（`§11.3` 的 16 份 `R*_packet.md`），
因此 **A03 的部分取证与被审对象同源**——这一点 A03 在 `§4.4` 第二层已自陈（`U-A`）。

**未声明的暴露面（Round-3 显式登记）**：

| 项 | 内容 | 处置 |
|---|---|---|
| **TEMP-1** | 本次审计的全部 scratch 产物（`Compare-Object` 中间表、token 计数脚本、packet 摘录）落在 `C:\Users\gg828\AppData\Local\Temp\opencode\lanes\` 与 `…\wt\` 下的临时工作区。**该目录树不在 `youling/lhrm` 的 Git 管理内，因此不受 `AGENTS.md` Mutation discipline 的 branch/PR 约束。** | **登记为未声明的暴露面。** 这不构成污染证据（无任何 scratch 产物被写回仓库），但它使「durable 文本是唯一证据面」这一前提**在本报告身上不严格成立**。同类登记见 `17` §0（`H-A5` 处置）。 |
| **TEMP-2** | `…\wt\a4b` 是本轮为 A03 修复创建的**隔离 worktree**，base = `8adcf0bacc45c0feb5c14e65e2a45346dd488b43`；A03 的 Round-3 改动**只**落在本报告一个文件内。 | 已记录。**未 push、未建 PR、未改任何 review state。** |

> **A03 不主张** TEMP-1 导致了任何具体错误。**它主张的是**：凡是依赖「durable 文本 vs packet 文本」之差的结论（含 `§4.4`），
> 都必须把这一未声明暴露面算进其不确定性预算。

---

## §0 方法

### 0.1 两个正交标签轴

**轴一 · 判据形态**

| 标签 | 定义 | 检验问题 |
|---|---|---|
| `HAS_EXPLICIT_FAILURE_CONDITION` | 判据原文含一句「若〔可观测量 X〕则〔地位变更 Y〕」，X 可取得，Y 是拒绝 / 降级 / 移层 / 标 `UNTESTABLE` | 代入否定支会发生什么？ |
| `NOMINAL_ONLY` | 有检查方式或标签，但**没有被命名的观测结果**会导致地位变更；或"检查"验证的是自身是否被绕过 | 检查不通过意味着什么？答不出即 `NOMINAL_ONLY` |
| `UNFALSIFIABLE_AS_WRITTEN` | 判据按字面被**任何**结果满足，含与主张相反的结果；或相反结果被吸收为"修正 / 加字段 / 换层 / 再跑一次" | 有与主张相反却被判"通过"的结果吗？ |

**轴二 · 可执行性**

`EXECUTABLE_TODAY` / `BLOCKED_NO_DATA` / `BLOCKED_NO_FIXTURE` / `BLOCKED_NO_INSTRUMENT` / `BLOCKED_NO_DESIGN` / `NOT_SPECIFIED`

> **两轴必须分开。** 一条判据可以形态完美而完全跑不动。**本次审计发现：LHRM 判据库在这一格上密度极高
> ——形态最好的判据恰好是最跑不动的判据。** 只报一轴会严重误导。

### 0.2 Gate 三测试（第三方可原样复算）

| 测试 | 问题 | 判定方法 |
|---|---|---|
| **T1 判决测试** | 门内是否存在一句「若〔可测量的 X〕则〔否决 Y〕」？ | 逐字读门文本，代入否定支 |
| **T2 终态测试** | 该门是否存在**修复以外**的终态？ | 追踪文档规定的失败后动作，看是否总能落回"诊断 → 修 schema → 重跑" |
| **T3 供给测试** | 门所需输入能否由**现存**材料产生？ | 把门要求的每项 cell / pair 与 `VALIDATION_CORPUS` 12 份 + 3 份 fixture 逐格对照 |

---

## §1 Gate A/B/C 可执行性裁定（最重要的单点结论）

### 1.1 判据原文（逐字）

**`PARAMETER_CONVERGENCE_V0_1.md` §13（line 616–649）**

```text
对任意一句关系相关事实，首先尝试落到：
 1. AgentState / Attribute      5. Action/Event
 2. DirectedRelationshipState   6. Constraint/Agreement
 3. PairState                   7. Environment
 4. BeliefState                 8. History/Timeline
                                9. Provenance/Uncertainty
                               10. Derived/Narrative-only
若一句话不能合法落入任何一类，标： MAPPING_FAILURE
禁止第一反应直接新增 primitive。
先诊断： ontology hole / construct hole / scope hole / temporal/history hole /
         belief/observation hole / measurement hole / or merely narrative/irrelevant
```

**`AGENTS.md` Validation discipline（line 62）**

```text
Record unmappable material as `MAPPING_FAILURE`; Architect diagnoses whether the failure is
ontology, construct, scope, temporal/history, belief/observation, measurement, or merely
narrative/irrelevant.
```

**`PARAMETER_CONVERGENCE_V0_1.md` §15（line 701–748）**

```text
### Gate A — Court-fact sentence coverage
1. 去掉法律条款、裁判理由、判决结果；
2. 只保留 fact narrative；
3. 独立 Agent 逐句映射；
4. 记录所有 `PARTIAL_MAPPING / MULTI_MAPPING / MAPPING_FAILURE`；
5. Architect 只分析 failure，不允许 Agent 为了通过测试现场发明变量。

### Gate B — Cross-context counterexamples
至少测试： same-sex / opposite-sex / kin / non-kin / friendship / romance /
           caregiving / conflict / unilateral attraction /
           high-dependence/low-liking / high-attraction/low-trust

### Gate C — Redundancy challenge
重点攻击： Liking vs RomanticAttraction / Trust vs AttachmentSecurity /
           Caregiving vs Dedication / AttachmentSecurity vs Cohesion/We-ness /
           OutcomeDependence vs structural derivation / PPR vs Trust/Care/Attachment
通过后，才有资格把 v0.1 candidate 推向 `Minimal Sufficient State v0.1`。
```

### 1.2 三测试逐门应用

| 门 | T1 判决测试 | T2 终态测试 | T3 供给测试 |
|---|---|---|---|
| **Gate A** | **FAIL。** 5 步全是**记录义务**（"记录所有…"）。无阈值、无 `若…则否决` 句。step 5 提到"通过测试"却从未定义"通过" | **FAIL。** 失败后唯一规定动作是"Architect 只分析 failure"；诊断清单 7 项中 1 项（`merely narrative/irrelevant`）**本身不是失败**；其余 6 项的自然补救都是**加类或加字段**。§13 只禁止"**第一反应**直接新增 primitive"——诊断后新增被默许 | **PASS。** `FIXTURE_001` 给出 C001–C026 与明确抽取边界（"only `Findings of Fact`, paras 13–23"） |
| **Gate B** | **FAIL。** "至少测试"是**覆盖要求**，不是判决规则。cell 缺失、cell 构造不出反例的后果均未规定 | **FAIL。** 无失败态、无修复态、无降级态 | **FAIL。** 11 类中 **5 类零覆盖** |
| **Gate C** | **FAIL。** "通过"未定义：多高的因子相关算冗余、用哪个估计量、在哪个 `n` 上、哪个显著性水平、六条中哪一条失败算 Gate C 失败 | **FAIL。** 通过只**提升**；**无否决分支** | **FAIL。** 冗余是**测量工具的属性**。R03 把 `D7 Dedication` 标 `NOT_IDENTIFIABLE 直到自建工具`、把"无任何构念有两个独立通道"标为**架构级 gap** `G9`；R01 `U7` 所需的 5 构念多方法矩阵不存在。文档语料**无法**估计两个构念在同一被试、同一工具下的因子相关 |

**Gate B 供给测试逐格对照**

| Gate B cell | 语料现状 | 覆盖 |
|---|---|---|
| `romance` | L1-001/002/003、L2-001/002/003、L3-001/002/003 | 有（9 份） |
| `non-kin` / `opposite-sex` | 大多数 | 有 |
| `conflict` | L2-003、L3-001 | 部分 |
| `unilateral attraction` | L2-003。**L1-003 不是**：Magi 中二人各自**不知道**对方已献祭，其张力是信念不对称而非吸引不对称 | 仅 1 份，**未冻结** |
| `high-attraction/low-trust` | L3-001 | 1 份，**未冻结** |
| **`same-sex`** | 12 份中无一份以同性 dyad 为 core dyad | **0** |
| **`kin`** | L0-002 的母亲已故且不在 core dyad；L2-001/002 的孩子是第三方 | **0** |
| **`friendship`（非恋爱友谊）** | L1-001/002/003 全为**婚姻**；L2-002 为智力伙伴转恋爱 | **0** |
| **`caregiving`** | L0-002 是照护机构**合同 / 费用**争议（照护对象已故，不在 dyad 内）；L0-003 是医患 | **0** |
| **`high-dependence/low-liking`** | 无 | **0** |

> **5/11 cell 零覆盖。这 5 个 cell 恰好是 R15 判为"最缺"的几个（R15 `N16` 兄妹 dyad："性价比最高的对抗件"、
> "任何'以浪漫为默认 dyad'的映射会系统性误标"）。**
>
> **Round-3 更正 1（`caregiving` 不是 0，是口径依赖的 partial）。** `caregiving` 一格在本表被判 `0`，依据是
> 「L0-002 是照护机构**合同 / 费用**争议（照护对象已故，不在 dyad 内）；L0-003 是医患」。
> 这条判据把 `caregiving` 窄化成"**作为 core dyad 主轴的照护关系**"。按"该 dyad 是否含照护 / 被照护关系"的宽口径，
> `L0-003`（23 年医患纵向照护）与 `L3-001`（care/control 为 core dyad 轨迹）都算 ⇒ **口径依赖的 partial = 2/12，不是 0。**
> **并且成因不是 curation 缺陷**：`L0-002` 的照护对象已故、不在 core dyad 内，**这一格在权利与在场事实两层都不可补**
> （`§2.6` 与 `§2.7` 记录了同一条 rights fail-closed 约束）。**零覆盖里的至少一格是 rights / access gate 的结果，
> 把它记成"语料没选"是错误归因。**
>
> **Round-3 更正 2（`5/11` 这个分母本身不可用）。** Gate B 的 11 格**混了两种不同用途的条目**：
> **8 格是抽样框语境**（`same-sex` / `opposite-sex` / `kin` / `non-kin` / `friendship` / `romance` / `caregiving` / `conflict`），
> **3 格是构念解耦模式**（`unilateral attraction` / `high-dependence/low-liking` / `high-attraction/low-trust`）。
> 前者问「这类关系语料够不够」，后者问「这条反例在项目文本里已被写下来了吗」。**两者没有共同的分母**，
> 因此 `5/11` 这一比值**不是**一个有意义的判据。正确形式是**两张表 + 各自的合格判据**（`C-P2`：`C-P2` 要求
> "Split **sampling-frame contexts** from **construct-decoupling adversarial patterns**; do not mix them into one denominator"）。
> **本报告因此不再把 `5/11` 当结论，只把它降级为"在我自己定的窄口径下的一个数"。**

### 1.3 裁定

> **`Gate A`：可执行，但不可证伪（`EXECUTABLE_BUT_NON_FALSIFIABLE`）**
> **`Gate B`：既不可证伪，也不可执行（`NOT_EXECUTABLE` + `NON_FALSIFIABLE`）**
> **`Gate C`：既不可证伪，也不可执行（`NOT_EXECUTABLE` + `NON_FALSIFIABLE`）**
>
> **项目的首要验证门不是"可能被驳倒的检验"，而是三份记录表格 + 一份缺口清单。**
> 只有 Gate A 今天真能跑，而它无论跑出 0% 还是 100% 的 `MAPPING_FAILURE`，文档规定的下一步都是"Architect 诊断"。

**在 Gate A 判据原文下，什么结果本来会被算作失败？**
`0 个 MAPPING_FAILURE` 与 `26/26 MAPPING_FAILURE` 被同等接受。唯一在字面上接近"失败"的是 step 5
「不允许 Agent 为了通过测试现场发明变量」——但它约束的是**过程**，文档**未为违反它定义任何后果**。
**因此 Gate A 下不存在会被算作失败的结果。**

### 1.4 对 R17 `F1` / `F9` / `F11` 的独立复核

| R17 主张 | A03 裁定 | 依据 |
|---|---|---|
| `F1`：`MAPPING_FAILURE` 在设计上不可达 | **CONFIRMED，且 R17 低估**。**Round-3 更正：机制数是 3，不是 1；逃逸通道数是 6，不是 3。来源数是 1 primary + 1 逐字镜像，不是 2 个独立来源。** 逐条见下方「三机制表」。**R17 未指出：§13「禁止第一反应直接新增 primitive」把"诊断后新增"确立为规定补救，与 §15 step 5 组成无终止条件的修复环。出口没堵死，但唯一被写下来的动作就是修。** | §13 line 616–649；`AGENTS.md:62`；§15 line 707–715 |
| `F11`：Step 3 在结构上无法失败 | **CONFIRMED**。§14 明写"第一轮 Case Bank test **只要求语义有合法落点**"。**Round-3 指针更正：`§14` 内无任何编号 step（A03 早期把它写成「§14 Step 3」是悬空指针）。真实位置有两处：门槛句在 `§14:679`；"独立 Agent 逐句映射"这个动作在 `§15` Gate A **第 3 步**（`PARAMETER_CONVERGENCE_V0_1.md:713`）。两处缺一不可。** | §14 line 679 + §15 line 713 |
| `F9` 要点 2：「Gate B 的 11 类**全部**是 LHRM 自己候选构念的组合形态」 | **需更正**。11 类中**前 8 类是 scope / context 标签**，不是构念组合。但结论仍成立，依据更强：**后 3 类逐条是 §4「为什么保留」bullet 的复述** | 见 1.5 |
| `F9` 要点 5：法院「事实认定」是相关性预过滤后的语料 | **CONFIRMED，且低估**。实际是**三层**预过滤：① `Findings of Fact` 的定义（法律相关性）；② `recommended_cleaning` 按**争议时间中心性**裁剪；③ L0-003 被开窗到 1998–2008（"do not use full 23-year span as single L0 item"）。三个轴与"表示难度"正交或反相关 | `VALIDATION_CORPUS` L0-001 / L0-002 / L0-003 |
| `F9` 要点 3：Fixture 独立性不对称 | **CONFIRMED**（三份 fixture 头部自述） | 三份 fixture line 5 |
| `F9` 要点 4：最具判别力的测试被解除武装 | **CONFIRMED**（`do NOT test ending prediction`） | `VALIDATION_CORPUS` L1-003 |

### 1.4b `MAPPING_FAILURE` 不可达：三个互不相同的机制（Round-3 重算）

> **取代** `§1.4` `F1` 行早先把不可达归因于**单一** catch-all 的写法（原文保留在 `F1` 行内）。
> 本表把机制数、阶段数与来源数全部重列。**每一个计数都是本次重算的，不是转引的。**

| # | 机制 | 文本位置 | 流水线阶段 | 操作 | 逃逸通道计数 |
|---|---|---|---|---|---|
| **(1)** | 映射类表有 **4 个** catch-all | `PARAMETER_CONVERGENCE_V0_1.md:618-629` 的 10 类中第 **7 / 8 / 9 / 10** 类 = `Environment` / `History/Timeline` / `Provenance/Uncertainty` / `Derived/Narrative-only` | **分类** | 装不下的句子**找不到**可落类 ⇒ 失败**不被记录** | 4 |
| **(2)** | `Provenance/Uncertainty` 是**自由文本槽**，不是受控类 | 同上第 9 类 | **分类** | 任何句子都可以"归到 provenance"而不必命名构念 | （与 (1) 重叠，**单独再计会把通道数虚增**——本报告不重复计） |
| **(3)** | 诊断清单含 `or merely narrative/irrelevant` | `§13:641-649` **和** `AGENTS.md:62`（**同一串 7 项，两处**） | **分诊** | 已记录的失败**必然被解释掉** ⇒ 失败**永不升级** | 1 |
| **(4)** | 成功门槛被降到"有合法落点" | `§14:679` | **阈值** | 门槛低 ⇒ 失败**很少发生** | （阈值机制，不新增通道） |

**通道计数的诚实形式**：**4 个 catch-all 类 + 1 个自由文本槽（机制 (1) 内部）+ 1 个诊断出口（机制 (3)）= 6 条逃逸通道**。
若按"可被一句话指名的独立通道"计，则是 **4 + 1 = 5**。**两种数都对，但必须说明是按哪一条规则数的**——
`synthesis` 用的"**3** 个 catch-all"（`19:282`）**在两种规则下都偏低**，方向是**把缺陷说得比 A03 的原文更小**。
本报告采用 **6**（宽口径，含自由文本槽），并把 4 作为下限登记。

**独立来源数 = 1 primary + 1 逐字镜像**：`AGENTS.md:62` 与 `§13:641-649` 是**同一条 7 项诊断清单**，逐项措辞一致。
把它们当"§13 之外的第二个独立来源"来数机制是**把镜像当独立源**（`19:102` 的错误）。
⇒ **`MAPPING_FAILURE` 不可达这一主张的独立来源数 = 1**（canonical 内部一条文本链），方法数 = 3（分类 / 分诊 / 阈值）。

**两条必须同时记录的限定**：

1. `X-14` 口径：上表证明的是「**在本仓已提交的三份 canonical / 基础设施文件内**，`MAPPING_FAILURE` 没有可达路径」，
   **不是**「在 LHRM 项目中 `MAPPING_FAILURE` 永不可达」。任何实现层（未提交代码、未登记的 schema 变体）都在本表之外。
2. 即使三个机制全部堵死，**机制 (4) 的门槛仍使失败率可测而不可判定**；因此本报告的处置不是"加一个诊断类型"就够了，
   而是**必须有 (a) 后果动词 + (b) 阈值 + (c) 一个诊断类型 + (d) 一个 ablation 步骤** 四件套（`H-A1` 的最小描述）。

---

### 1.5 Gate B 三条构念组合类 = §4「为什么保留」的逐条复述

| Gate B cell | `PARAMETER_CONVERGENCE` §4 bullet（逐字） | 关系 |
|---|---|---|
| `unilateral attraction` | D2：「适用于**单向浪漫**、无性浪漫、性吸引但无恋爱意愿等反例。」（line 152） | **复述** |
| `high-dependence/low-liking` | D8：「可高 dependence 低 liking / low dedication。」（line 238） | **复述** |
| `high-attraction/low-trust` | D4：「**可高喜欢低信任**，也可低喜欢高制度性信任。」（line 179） | **复述** |

**Gate C 六条 attack pair 的同源检查**

| Gate C pair | 同源？ | 依据 |
|---|---|---|
| `Liking vs RomanticAttraction` | **复述** | D1：「可以喜欢但无 romantic attraction」（line 132） |
| `Trust vs AttachmentSecurity` | **新提出** | 无对应 bullet |
| `Caregiving vs Dedication` | **新提出** | 无对应 bullet |
| `AttachmentSecurity vs Cohesion/We-ness` | **复述** | §6 P1「`KEEP_CANDIDATE / contested scope`」（line 297） |
| `OutcomeDependence vs structural derivation` | **复述** | D8 Open question（line 241） |
| `PPR vs Trust/Care/Attachment` | **复述** | §5 B1 理由（line 267） |

> **Gate C 6 条中 4 条是项目已有论断的复述，2 条是新的；新信息量只有 `Trust/AttachmentSecurity` 与 `Caregiving/Dedication` 两对，
> 而这两对恰好也是 R02 判为 `CONTESTED` / 需新数据的两对。**

### 1.6 本报告对 R17 未命中之处的补足：§2.6 → Gate A 的**未兑现承诺**（Round-3 改写）

> **取代说明**：本节早先的标题与结论是「**§2.6 在结构上永远不能触发**」。该措辞**保留在 `§R0` 的 `R-I` 行**，
> 但**已被取代**。取代后的表述见下方「Round-3 结论」。

```text
§2.6 Representation necessity（line 82–86）：
  「若删除该 construct，是否会存在重要现实句子/状态无法用剩余 schema 合法表示？
    这项将在 Case Bank regression 中直接测试。」
      │  把"删除一个构念"的判据完全外包给 Case Bank regression
      ▼
§15 Gate A（唯一处理表示覆盖的门） → 5 步，无一步是"删掉 k 再重测"
      ▼
§13 的 10 个映射类（4 个 catch-all + 1 个自由文本槽，见 §1.4b）
      ▼
⇒ 「删掉 k 之后仍有句子无法表示」在被登记的判据文本下不可观测
```

**Round-3 结论（取代原「结构上永远不能触发」）**：

> **可验证的内部不一致**：`:86`（`§2.6`）是一句**关于这条判据自身可测性的承诺**——
> 「**这项将在 Case Bank regression 中直接测试**」。而 `:86` 描述的正是 **leave-one-construct-out 消融**。
> **`§14` 与 `§15` Gate A 的 5 个步骤里没有任何一步包含「移除某个 construct 再重测」**；Gate B 是**覆盖要求**，
> Gate C 只在**通过之后**才管升格（`:748`）。`16:117` 与 `VALIDATION_CORPUS_V0_1.md` 全文亦无此臂。
>
> **因此正确的事实陈述是**：**§2.6 承诺了一个 Gate A 不包含的检验。**
> 这**不等于**「§2.6 结构上不可触发」——后者是 A03 早先的**推论**，不是文档事实：
> 一旦有人**补上**这条消融臂，§2.6 **就有一个明确的可失败形式**（A03 `§5.2` 改写 2 就是这个形式）。
> **区别很重要**：原措辞把「文档缺一条臂」说成「判据不可能失败」，前者是可修的工程缺口，后者是不可修的逻辑命题。
> **本报告的立场：这是全项目最便宜的一处修复（缺的是一条臂，不是一个阈值）。**
>
> **留存的推论（已限定）**：在**当前已登记的判据文本**下，`Candidate Minimal Directed Basis v0.1` 的 8 项**没有一条被
> 登记的移除通道**。文档写下来的移除路径只有两条：
> **`R06 判 E`**（等价性检验后拒绝 `Dedication` 为独立 primitive —— 全项目措辞最好的一条移除判据）
> 与 **`R17 R3`**（invariance 失败后按 relation type 拆分）。**两条都需要项目目前没有的数据。**
> `R02`（唯一的冗余审计）自设「本文件**不**裁决哪些构念该留、该删」。
> `R01` 的裁决词表声明 `KEEP / SPLIT / MERGE / DERIVED / BELIEF_ONLY / REJECT / OPEN` 七个值。
> **Round-3 更正（见下方 `§1.6b`）**：A03 早先把「`MERGE` 与 `REJECT` 一次也没有出现」直接陈述为项目级事实（"在整个构念审计中从未被签发过一次"），
> **该陈述已按 report-scoped 形式重写**。

### 1.6b `MERGE` / `REJECT` 的"零签发"：**单份报告的词表使用率**，不是项目级事实（Round-3 重算）

**A03 早先的陈述（保留，逐字）**：`§1.6` 原文「**`MERGE` 与 `REJECT` 一次也没有出现**……在整个构念审计中**从未被签发过一次**」；
`§2.2` 注「**七个裁决值只用了四个。** `SPLIT` 出现 1 次（将来式），`MERGE` 0 次，`REJECT` 0 次」；
`§7.2` `N-A03-3` 同义；`§10` `NR-4` 同义。

**Round-3 重算（对 `02_CONSTRUCT_CONVERGENCE.md` 逐 token 计数）**：

| token | 全文出现次数 | 出现位置 | 作为**裁决值**被签发 |
|---|---|---|---|
| `MERGE` | **1** | `:37` 词表声明行（`| 7 | 值 | KEEP / SPLIT / **MERGE** / DERIVED / BELIEF_ONLY / **REJECT** / OPEN + 强制再次证据 |`） | **0** |
| `REJECT` | **1** | 同上（**同一行**） | **0** |
| `SPLIT` | **2** | `:37` 声明行 + `:140`「（…）**将触发** `SPLIT`」 | **0**（`:140` 是将来式） |
| `KEEP` | 36 | — | 多次 |
| `DERIVED` | 18 | — | 多次 |
| `BELIEF_ONLY` | 8 | — | 多次 |
| `OPEN` | 13 | — | 多次 |

**三条必须同时成立的限定**：

1. **"零"对的是裁决值的签发数，不是 token 数。** 在被审计的报告里，`MERGE` 与 `REJECT` **各出现 1 次**，
   且两次都落在**词表声明行本身**。⇒ 「这两个值从未被签发」成立；「这两个词一次也没有出现」**不成立**。
   A03 早先的措辞把**前一个命题**写成了**后一个命题的形状**，这是本报告自身的一处措辞缺陷。
2. **这是**单份报告**的词表使用率。** 把它写进 synthesis（`19:32` / `:103` / `:185` / `:282`）并升格为
   "⇒ 8 项 candidate basis 永不会被缩小" 的**项目级事实**，就是错误产生的位置。
   **本报告明确记录：错误不是出在计数上，是出在把一个 report-scoped 速率当成 project-level 事实这一提升动作上。**
3. **它也不是"本审计未发现问题"的证据。** A03 `§10 NR-4(c)` 早先自己提出的处置是正确的方向
   （"应记录为'**本审计工具未被使用**'，而不是'**本审计未发现问题**'"）；**该处置继续有效**。

**X-14 口径**：`MERGE` / `REJECT` 的零签发只在**这一份报告的 13 条裁决**范围内成立。
`02b`（R02）用的是**另一套四值 lens 枚举**（`SAME / INDEPENDENT / OVERLAPPING / UNKNOWN` 一族），
`R07` / `R13` / `R15` / `R16` 各有自己的值集（`§2.2`、`§2.7`）。**因此本节不得被读作"项目没有合并/否决工具"。**

---

### 1.7 Gate B 的 11 格：一次**独立重算**，以及为什么"8/11"不是 A03 的数字（Round-3）

> **本节回答一个问题**：`synthesis` 记录「A03 corrected the Gate B self-certification figure to **8/11**」。
> **A03 没有说过这句话，也没有给过这个数字。** A03 的两行原文是：
> (a) `§1.4` `F9` 要点 2 栏：「**需更正**。11 类中**前 8 类是 scope / context 标签**，不是构念组合。」
> (b) `§7.2` `N-A03-6` 行：「**`R17 F9` 要点 2 的字面表述 8/11 不成立。**」
>
> ⇒ **A03 驳回的是措辞，不是计数。** A03 自己的结构是 **8（抽样框 scope 标签）+ 3（构念组合复述）= 11，全部项目自产。**
> 把 A03 的立场记成「修正为 8/11」，等于**把 A03 已经否决的措辞又安回它头上**。

**独立重算（本次逐格重读 `PARAMETER_CONVERGENCE_V0_1.md` §15 Gate B 与 §4 D1–D8）**：

| Gate B cell | 类别 | 项目文本中的来源 | 本次独立判定 |
|---|---|---|---|
| `same-sex` / `opposite-sex` / `kin` / `non-kin` / `friendship` / `romance` / `caregiving` / `conflict` | **抽样框语境**（8 格） | 语境词表本身就是项目文本（`§2.4` 语境清单、`CONSTRUCT_SCOPE §7.6` 6 项、`§15 Gate B` 11 项**三张清单互不相同**） | **项目自产。** 且它们是**语境名**，不是构念的组合形态 |
| `unilateral attraction` | 构念解耦模式 | `§4` D2（`RomanticAttraction`）bullet：「适用于**单向浪漫**、无性浪漫、性吸引但无恋爱意愿等反例。」（`:152`） | **项目自产（复述成立）** |
| `high-dependence/low-liking` | 构念解耦模式 | `§4` D8（`OutcomeDependence`）bullet：「可高 dependence 低 liking / low dedication。」（`:238`） | **项目自产（复述成立）** |
| `high-attraction/low-trust` | 构念解耦模式 | A03 早先映射到 `§4` D4（`Trust`）`:179`「可高**喜欢**低信任……」 | **A03 这一格的归属本身是错的。** 见下 |

**第 11 格的归属错误（Round-3 新发现）**：

> Gate B 写的是 `high-**attraction**/low-trust`；`§4` D4 的 bullet 写的是「可高**喜欢**低信任」。
> 而**同一份文档**在 `D1`（`Liking`）`:131` 明写「**可以喜欢但无 romantic attraction**」，
> 并在 `:135-139` 明写「**不等于**：… romantic attraction」——
> **即 canonical 自己把 `Liking` 与 `RomanticAttraction` 判为两个不同构念。**
> ⇒ A03 用 `Liking`（D4 的 bullet）顶替 Gate B 那一格所指的 `Attraction`，
> **等于用一个被同一份文档显式区分开的构念，替掉了目标 cell 的构念。**
> **这条不能算作"项目自产的复述"**，因为它连映射关系都不成立。
>
> **修正后的独立计数**：`11` 格中 **`10` 格可归因于项目文本**（8 语境 + 2 构念复述），
> **第 11 格的归属关系不成立**。**A03 早先的"3 条构念组合逐条是 §4 bullet 的复述"因此高估了一格。**
>
> **不主张的替换数字**：**本报告不主张"10/11"是定案。** `high-attraction/low-trust` 是否真的对应 `§4` 中某一条
> （例如 D2 的「性吸引但无恋爱意愿」与 D4/D5 的组合）**需要读原文的人裁决**；
> 而且**更根本的问题是：这一格本身可能是唯一一个新 cell**（`ADJ3` 的读法），**而它的覆盖是 `0`**。
> **本报告只登记重算过程与已确认的那一处归属错误，不宣布替代数。**

**这一节唯一不依赖任何裁决的结论**：

> **Gate B 的 cell 清单混了两种不同用途的条目**（抽样框语境 × 构念解耦模式），
> **因此不存在有意义的单一分母**。任何形如 `k/11` 的比值——包括 A03 自己的 `5/11`——
> **都必须先说明它是在哪一张表上数的。**（`C-P2` 的明文要求。）

---

## §2 可证伪性记分卡

> 「失败结果」一栏为"无"的行，**不计入"已可证伪"**。

### 2.1 转移律族（R06）

| 判据 | 形态 | 可执行性 | 指针 | 判据原文下"什么结果会被算作失败" |
|---|---|---|---|---|
| **判 A**（拒绝"信念中介"） | `HAS_EXPLICIT_FAILURE_CONDITION` | `BLOCKED_NO_DATA` | §4.8 L249–254 | 「若对 `\|K_pre\|` 中**多数** `k`，`c` 的 CI **包含 0**，**且** `∂ΔZ/∂Resp`（不条件化）系数**不小于** `\|c\|`」 |
| **判 B**（拒绝归属门控） | `HAS` | `BLOCKED_NO_INSTRUMENT` | §4.8 L256–260 | `NO-ATTRIB` 与完整模型信息准则差落在**登记时冻结**的等价区间内 |
| **判 C**（空转） | `HAS` | `BLOCKED_NO_INSTRUMENT` | §4.8 L262–265 | `AR-ONLY` 与完整模型无实质差异 → 拒绝为独立律族，只保留 readout |
| **判 D**（拒绝"存量是独立动态通道"） | `HAS` | `BLOCKED_NO_DATA` | §5.8 L409–416 | ≥2 个预登记领域中 `Std`/`Alt`/`Inv` 的人内增量方差 95% CI 含 0 |
| **判 E**（拒绝 `Dedication`） | `HAS` | `BLOCKED_NO_INSTRUMENT` | §5.8 L418–423 | 已知 `D`/`Inv`/`Alt`/`Std` 后 `Ded` 无稳定额外动态信息（**等价性检验**）。**全项目唯一措辞合格的移除判据** |
| **判 F**（拒绝迟滞支） | `HAS` | `BLOCKED_NO_DATA` | §5.8 L425–428 | Preisach 型含记忆算子相对无记忆版**样本外**无实质改善 |
| **判 G**（拒绝段内实际化） | `HAS` | `BLOCKED_NO_DATA` | §6.8 L536–540 | 仅 `Level`（+per-person 随机截距）解释的人内变化方差**不少于** `Level+Slope` 合计，且交互 95% CI 含 0 |
| **判 H**（空转 / 符号） | `HAS` | `BLOCKED_NO_DATA` | §6.8 L542–545 | `Slope` 符号在预登记多数 `k` 上**为正** |
| **判 I**（不可识别） | `HAS` | **`EXECUTABLE_TODAY`** | §6.8 L547–550 | 起点波次回溯指定 → `UNTESTABLE_BY_DESIGN`，**不得以任何 post hoc 方式报告 slope 估计**。**形式最佳：纯文档判定** |
| **判 J**（拒绝 Ideal 漂移是状态过程） | `HAS` | `BLOCKED_NO_DATA` | §7.8 L692–700 | `Want` 不呈现对 `Actual` 的系统漂移；**并强制**并行 `REPORTING_ARTIFACT` 检验 |
| **判 K**（拒绝 partner 肯定通道） | `HAS` | `BLOCKED_NO_DATA` | §7.8 L702–705 | `Affirm→Movement` 控制 `Actual` 后 CI 含 0 |
| **判 L**（拒绝两通道分离 / MH3） | `HAS` | `BLOCKED_NO_DATA` | §7.8 L707–710 | 单通道与双通道**等价性检验通过** → 不得声称两条可分离通道 |
| **判 M**（拒绝分支结构） | `HAS` | `BLOCKED_NO_DATA` | §8.8 L856–862 | (i) `Λ⁺` 无 episode 内增量 **且** (ii) `s(n)` 等价性检验下恒为"中性" → 律 E **退出独立律族地位** |
| **判 N**（拒绝状态依赖） | `HAS` | `BLOCKED_NO_DATA` | §8.8 L864–869 | `s` 的跨 dyad 变异中 person 常数部分显著大于 dyadic-state → 构念移至 **Agent 层** |
| **判 O**（方向性） | `HAS` | `BLOCKED_NO_DATA` | §8.8 L871–874 | 控制 `Z` 后净效应为 0 或与 S09 / S10 相反 |
| **MH1**（`RULE-⊥`） | `UNFALSIFIABLE_AS_WRITTEN` | `NOT_SPECIFIED` | §1 L57–64；§11 非主张 8 | **无判据**（自承"完全未检验"） |
| **MH2**（迟滞） | `UNFALSIFIABLE_AS_WRITTEN` | `BLOCKED_NO_DATA` | §10 `U-2` | **无判据** |
| **MH3**（两通道） | `HAS` | `BLOCKED_NO_DATA` | `判 L` | 由判 L 承担 |
| **MH4**（`Girth`） | `UNFALSIFIABLE_AS_WRITTEN` | `NOT_SPECIFIED` | §7.4 L650 | **无判据** |
| **MH5**（`M` 漂移） | `UNFALSIFIABLE_AS_WRITTEN` | `NOT_SPECIFIED` | §4.5 L211–212 | **无判据** |
| **MH6**（环境直通） | `UNFALSIFIABLE_AS_WRITTEN` | `BLOCKED_NO_DESIGN` | §10 `U-4` | **无判据** |
| **`U-1`** 信念/现实分离 | `UNFALSIFIABLE_AS_WRITTEN` | — | §10 L911–916 | **无判据**。后果：**`判 A` 的可证伪性是条件性的** |
| **`U-2`** 迟滞 | `UNFALSIFIABLE_AS_WRITTEN` | — | §10 L918–922 | 无判据 |
| **`U-3`** 终止 = 设计性删失 | `HAS` | `EXECUTABLE_TODAY` | §10 L924–929 → R16 `R16-OC03` | 以 breakup/divorce 为 outcome 且未标 `CENSORING_BY_DESIGN` → 违规。**本项目把不可证伪项转为可执行标记的唯一成功案例** |
| **`U-4`** 环境直通 | `UNFALSIFIABLE_AS_WRITTEN` | — | §10 L931–933 | 无判据 |
| **`U-5`** 交换律负分支 | `UNFALSIFIABLE_AS_WRITTEN` | — | §10 L935–940 | 无判据 |
| **`U-6`** 火花/生长 | `UNVERIFIED`（引用缺口） | — | §10 L942–945 | 不适用 |
| **`U-7`** `Alt` 是否为 `Sat` 换名 | `UNFALSIFIABLE_AS_WRITTEN` | — | §10 L947–950 | 无判据 |
| **`U-8`** level/slope 二分 | `UNFALSIFIABLE_AS_WRITTEN` | — | §10 L952–956 | 无判据 |
| **`U-9`（新）** `Ĝ_k` 门控 | `UNFALSIFIABLE_AS_WRITTEN` | `NOT_SPECIFIED` | §4.1 L134；§4.5 L204–207 | **无任何判据。** `判 B` 测 `NO-ATTRIB`（`Ω` 是否依赖 `R_i`），**不测** `Ĝ` 是否依赖 `Z`。`Ĝ` 是三值分类器、由未观测函数决定，任何数据都可靠选 `Ĝ` 拟合。**而"状态依赖"正是律 A 区别于"行为直接更新状态"的全部内容** |
| **`U-10`（新）** `⊕` 聚合算子 | `UNFALSIFIABLE_AS_WRITTEN` | `NOT_SPECIFIED` | §4.1 L140；§11 非主张 1 | **无判据。** `⊕` 逐字为"求和 / 时间加权 / 名义型计数 / 序数聚合**皆可**"。若 `⊕` 自由则 `Net_k` 不可识别，一切经 `Net_k` 的效应**符号与量级均不可识别**；且 `NO-PARTNER` 获胜时可靠换 `⊕` 重参数化救回效应 |
| **`U-11`（新）** `K_pre` 选择自由度 | `UNFALSIFIABLE_AS_WRITTEN`（选择泄漏） | 缺陷本身 `EXECUTABLE_TODAY` | §4.8 L245–253 | **无判据且判据内含泄漏。**「对**预先登记的** `K_pre`（建议 ≤4 项，登记时冻结）」+「若对 `\|K_pre\|` 中**多数**」：登记者自选被审判的 4 个构念。若挑最有利者，需 3 项同时失败才触发拒绝。**预登记在此只约束顺序，不约束选择** |
| **`U-12`（新）** `RULE-⊥` 在 §10 范围外 | 覆盖范围错配 | — | §10 标题 | §10 只覆盖"**律**"，而五族**共享**的 `RULE-⊥` 不是律。**只读 §10 会得到"五族可测"的错觉** |
| **`U-13`（新）** `判 I` 未推广 | 内部不一致 | — | `判 I` vs §8.6 L837 | R06 对 DVA 写了「若起点波次回溯指定 → **不可检验**」；对 `RT` 它**自己写下**「**回溯填答的 `R_i` 会摧毁符号判定**」，**却无**配套 void 条款 |

**R06 小结**

- **15 条判据 A–O 全部 `HAS_EXPLICIT_FAILURE_CONDITION`** —— R06 的形态质量是全项目最高的。
- **14 条 `BLOCKED_NO_DATA` / `BLOCKED_NO_INSTRUMENT`；只有 `判 I` 今天可执行。**
- **6 个 `MH` 中 5 个 `UNFALSIFIABLE_AS_WRITTEN`。**
- R06 自列 `U-1…U-8` 全部诚实，**但遗漏 5 条**。
- `00_MANIFEST.md` L88 的「falsifiable transition-law family：5」应加注：**5 = in-principle；0 = 可用现存数据执行；2/5（DVA、RT）R06 自评"最可能被拒绝"**（§9 表「概率最高的结局」栏：DVA = "**被拒绝（初始差异胜）**"、RT = "退化为律 A"）。

### 2.2 构念裁决（R01）

| # | 构念 | 裁决 | 形态 | 「什么结果会改变裁决」 |
|---|---|---|---|---|
| 1 | `Liking` | `KEEP` + 三分解 | `NOMINAL_ONLY` | **无。** 三分解是附加条件，不是失败条件 |
| 2 | `RomanticAttraction` | `KEEP` + 边界 `OPEN` | `HAS`（单向） | 「若 Case Bank 出现「高择偶驱动力但零维持驱动力」的**稳定反例**，再启动 `SPLIT`」。`SPLIT` 从未执行；触发依赖 Gate B，而 Gate B 无 friendship 覆盖 |
| 3 | `SexualDesire` | `KEEP` + `measurement_channel` | `NOMINAL_ONLY` | 条件是设计强制，非可观测失败判据 |
| 4 | `Trust` | `KEEP` + `domain` | `NOMINAL_ONLY` | **无。** R01 §5.5 记录单极 vs 双极"30+ 年未决"——**裁决在争议两侧都成立** |
| 5 | `Distrust` | `OPEN`（倾向 `DERIVED`） | `HAS`（**形式最佳**） | `U3`：同一 domain 内能否与 `Trust` 同时高；需"非反向措辞的独立题目在同一 dyad 上同时测两维" |
| 6 | `AttachmentSecurity` | `KEEP` + `CONTESTED` | `UNFALSIFIABLE_AS_WRITTEN` | 争议被并列在**同一裁决内部**。任何一侧证据只更新天平，**不改变 `KEEP`** |
| 7 | `Caregiving` | `KEEP` + 双层 | `NOMINAL_ONLY` | 条件是记录纪律，无失败观测 |
| 8 | `Dedication` | `KEEP` + 「必须声明是否含 satisfaction 成分」 | **`UNFALSIFIABLE_AS_WRITTEN`（自相矛盾）** | R01 自认与 §9 R3 **内部不一致，需二选一**；处置是"强制声明"而非"二选一"，声明后两者仍并存 |
| 9 | `OutcomeDependence` | `KEEP` + `MEASUREMENT_INFEASIBLE` | `HAS` | `U5`：关系级量表 + 跨实验室信度。**但翻转方向是"变得可行"，不是"被删"** |
| 10 | `Satisfaction` | `DERIVED` | **`UNFALSIFIABLE_AS_WRITTEN`（吸收逃逸口）** | `U2` 若成立，处置是"**加 `comparison_baseline` 与 `observation_time` 字段**"，同时维持"不进 primitive 集合"。**唯一反证被吸收为新字段** |
| 11 | `Cohesion / We-ness` | `BELIEF_ONLY` | `HAS`（单向升级条件） | 「**升级条件**：出现独立 pair-level 观测通道（第三方编码 / 共同叙事）**且**纵向数据显示 `Cohesion_pair` 在已知 `PerceivedWeNess_A, _B` 之上仍有稳定增量信息」。**形式正确** |
| 12 | `PPR` | `BELIEF_ONLY` | **`UNFALSIFIABLE_AS_WRITTEN`（最重的一条构念发现）** | **无任何升降条件。** 理由是定义性的（信念 vs 现实的区分）⇒ 任何观测都相容：PPR 强预测 → "它是信念，而信念可以很强"；PPR 被分解 → "每块都是信念"。**R17 `F3` 持相反立场，而 R01 侧无判据可败** |
| 13 | `Perceived Commitment` | `BELIEF_ONLY` | `NOMINAL_ONLY` | **无。** 实为**别名折叠**：在不做任何检验的情况下把外部 top-1 predictor 并入既有构念的信念索引 |

> **七个裁决值只用了四个**（`KEEP` / `DERIVED` / `BELIEF_ONLY` / `OPEN`）。`SPLIT` 出现 1 次（将来式），`MERGE` 0 次，`REJECT` 0 次（**作用域见 `§1.6b`：这是本报告的 report-scoped 计数，不是项目级事实**）。
> **Round-3 更正**：A03 早先写「13 条中 **5** 条 `NOMINAL_ONLY` + **2** 条 `UNFALSIFIABLE_AS_WRITTEN` = **7** 条（54%）」。
> **逐行重数（上表 13 行）**：`NOMINAL_ONLY` = **5**（`#1` / `#3` / `#4` / `#7` / `#13`）；
> `UNFALSIFIABLE*` = **4**（`#6` `AttachmentSecurity` / `#8` `Dedication` / `#10` `Satisfaction` / `#12` `PPR`）。
> ⇒ **形态上不会因任何观测改变的是 5 + 4 = 9 条（69%），不是 7 条（54%）。**
> **早先的「7」是一个分组判断而非笔误**：它只把 `#10`（吸收逃逸口）与 `#12`（最重一条）算入，
> 把 `#6` / `#8` 排除——理由是这两条的缺陷是**自陈的内部冲突**（`CONTESTED` / 「需二选一」）而不是"不可证伪"。
> **本报告保留该分组，但**必须**在 7 与 9 两个数之间说清口径**，并以 **9** 为上界。

### 2.3 收敛判据（`PARAMETER_CONVERGENCE` §2，六条）—— **Round-3：scope 判定已扩宽到全族**

> **取代说明**：A03 早先的裁定是「**只有 §2.6 需要改写**」（原文保留在 `§5.1` 第 5 行与 `§R0` 的 `R-B` 行）。
> Round-3 逐条重读 `PARAMETER_CONVERGENCE_V0_1.md:41-86` 后，**该 scope 判定过窄**。逐条依据如下。

**逐条读出的 consequence frame**（本次逐行读原文，不是推断）：

| 判据 | 原文（摘） | 后果 frame | 形态 | 「什么结果会被算作失败」 |
|---|---|---|---|---|
| **2.1 Semantic independence** | 「不能被现有 construct **无损替代**的独立语义？」 | **无后果从句**（纯问句） | `NOMINAL_ONLY` | 「无损替代」**未定义**，无替代判定程序 |
| **2.2 Counterexample decoupling** | 「**若无法构造或观察解耦反例**，可能属于同一 latent state 的重复命名」 | **降级 frame**（重复命名） | `HAS`（"可能"软化） | 构造不出解耦反例 → 视为重复命名 |
| **2.3 Conditional incremental information** | 「已知其它候选后，该 construct 是否**仍可能**提供额外信息？」 | **无后果从句** | **`UNFALSIFIABLE_AS_WRITTEN`** | **不存在。** 可能性陈述无法被否定，除非逻辑上不可能。**"仍可能"使该判据无法失败** |
| **2.4 Scope stability** | 跨 same-sex / kin / romance / caregiving / conflict 等语境语义是否稳定 | **无后果从句** | `HAS` | 任一语境下不稳定。**`BLOCKED_NO_INSTRUMENT`**；R17 `F8` 另指出该判据的文献基础本身是争议区 |
| **2.5 Layer test** | 9 层 + 「如果只是行为、标签、结果或 proxy，不因常见就升级为 primitive」 | **降级 frame**（不升级为 primitive） | `NOMINAL_ONLY` | 判定规则本身有失败条件，但 **9 个桶无优先级规则** |
| **2.6 Representation necessity** | 「若删除该 construct，是否会存在重要现实句子/状态无法用剩余 schema 合法表示？」+「这项将在 Case Bank regression 中直接测试」 | **删除 frame**（唯一带 delete frame 的一条） | `HAS` **但承诺的检验不存在**（见 `§1.6`，Round-3 已把「结构上不可触发」改为「未兑现的承诺」） | 删除 k 后存在无法表示的句子；**在被登记的判据文本下不可观测** |

**Round-3 结论（六条全族，缺四件套）**：

> **六条里只有 `§2.6` 用删除 frame；`§2.2` 与 `§2.5` 用降级 frame；`§2.1` / `§2.3` / `§2.4` 连一句后果从句都没有。**
> **六条中没有任何一条写出了：程序（怎么做）、所需证据（拿什么跑）、输出字段（结果记在哪）、阈值（多少算失败）、指定执行者（谁跑）。**
> ⇒ **需要改写的是 `§2.1`–`§2.6` 全族（≥6 节），不是一节。** 这与 `H-A1` 记录的成本估计一致
> （`EV1` §9：约 5–8 句新增文字 + 1 个 ablation 步骤定义 + 1 个诊断枚举值；`ADJ3` 要求变更面扩到 4 文件 / ≥6 节）。
>
> **唯一一句纯程序性的话**是 `§2.6:86` 的「这项将在 Case Bank regression 中直接测试」。
> **逐字检查它的三个要素：**
> - **执行者**：无（"在 Case Bank regression 中"是一个场所，不是一个人/角色）。
> - **产物**：无（没说这次 regression 产出什么字段、什么判定）。
> - **失败后果**：无（这句话本身没有 `若…则…` 结构；它是一个**承诺**，不是一个判决）。
> ⇒ **它是本节唯一的程序性文本，而它三个要素全缺。** 这就是"程序要求存在但程序未被指定"的最小证据。

**X-14 口径**：`§2.4` 的「等语境」是**开放式**列举（原文用「等」），本报告**不**主张它是穷举清单，
也**不**主张语境覆盖等于表示能力证据（`H-A1` / `X-10` 的双层记账）。

### 2.4 门（§15）

| 门 | 形态 | 可执行性 | 「什么结果会被算作失败」 |
|---|---|---|---|
| **Gate A** | **`UNFALSIFIABLE_AS_WRITTEN`** | `EXECUTABLE_TODAY` | **无。** 0% 与 100% 同等接受 |
| **Gate B** | **`UNFALSIFIABLE_AS_WRITTEN`** | `NOT_EXECUTABLE` | **无。** "至少测试"是覆盖要求，缺失无后果 |
| **Gate C** | **`UNFALSIFIABLE_AS_WRITTEN`** | `NOT_EXECUTABLE` | **无。** "通过"未定义；只有提升分支 |

> **三条门判据的「失败结果」一栏全为"无"。按 mission 规定，三者不得计入"已可证伪"。**

### 2.5 不变量（R07 `I1–I19`）

R07 §5 自述"以下 15 条是**候选可检验不变量**……**不是**已验证的性质"；§6 非主张 10 自述"不主张本报告的任何一个不变量已被验证"。**该自述准确。**

| ID | 不变量（摘） | 形态 | 可执行性 | 「什么结果会被算作失败」 |
|---|---|---|---|---|
| I1 | Unknown 吸收 | `HAS` | `EXECUTABLE_TODAY` | composite 在 `⊥` 坐标上输出有限标量 |
| I2 | 底元素上不做算术 | `HAS` | `EXECUTABLE_TODAY` | 存在 `T` 使 `f(⊥_T)` 是数 |
| I3 | 有界读出的像集报告 | `HAS` | `EXECUTABLE_TODAY` | 对 `⊥` 成立的 readout 输出单值 |
| **I4** | tag 闭包 | **`NOMINAL_ONLY`（同义反复）** | 可跑但无意义 | 检查 = "枚举 diff（CI）"，反例 = "tag 数量随 case 数增长"。**注册表本身是 schema 约束，该检查只能发现绕过注册表，不能发现 ontology 蠕变** |
| I5 | tag 不可跨角色泄漏 | `HAS` | `EXECUTABLE_TODAY` | 交换 `S`/`O` 后 `private_to_partner` 被 S 侧解决 |
| I6 | 矛盾 ≠ 未知，且与来源顺序无关 | `HAS` | `EXECUTABLE_TODAY` | 打乱来源顺序后 `B` 改变 |
| I7 | 聚合顺序无关 | `HAS` | `EXECUTABLE_TODAY` | 打乱证据顺序改变 composite |
| I8 | 重复证据幂等 | `HAS` | `EXECUTABLE_TODAY` | 摄入两次状态改变；第二来源 `overwrite` |
| I9 | 逐坐标单调 | `HAS` | `EXECUTABLE_TODAY` | 更新 `j` 改变 `i` 而无已登记 `∂F_i/∂z_j≠0` |
| I10 | refinement 单调 | `HAS` | `BLOCKED_NO_DESIGN` | 丢证据反而变宽。**Round-3 限定（`A3d` 路由，child `A3d` CR-8）**：Round-3 判 `I10` **需先冻结 `width` 的定义**——`07` 未给 `width` 下定义，而 `07` 的 `I15` 明确禁止对非恒定函数取均值。**在 `width` 冻结前，`I10` 的失败条件不可构造。** 本报告**不**改判 `HAS → UNFALSIFIABLE`，**只**记录这一前置未定（判定属 `07` 的 owner） |
| I11 | 时间 refinement 单调 | `HAS` | `BLOCKED_NO_DESIGN` | refined 视图作为 refined 视图的 sibling |
| I12 | readout 不回写 | `HAS` | `EXECUTABLE_TODAY` | readout 像进入状态更新路径 |
| **I13** | 不可约性诚实 | `NOMINAL_ONLY` | `EXECUTABLE_TODAY` | 检查 = 字符串/模板审计。**只能检出特定措辞**；从不声称可识别的报告自动通过 |
| I14 | prior 支配标记 | `HAS` | `EXECUTABLE_TODAY` | 零观测坐标输出点值。`θ` 未定但禁令单侧 |
| I15 | 多峰不取均值 | `HAS` | `EXECUTABLE_TODAY` | 双峰后验输出点 readout |
| I16 | 校准单调 + 不劣于常数先验 | `HAS` | `BLOCKED_NO_DATA` | reliability diagram 劣于常数先验基线 |
| **I17** | coverage 显式 | **`UNFALSIFIABLE_AS_WRITTEN`（阈值未定 ⇒ 禁令空转）** | `BLOCKED_NO_DATA` | 阈值 `UNKNOWN` ⇒ 任何 coverage 数字都合法 |
| **I18** | REFUSE 可达性（「**必须存在一个状态**……使最优动作是 `REFUSE`」） | **`UNFALSIFIABLE_AS_WRITTEN`（存在量词 + 阈值未指定）** | 可跑 | **无。** 被全缺失状态平凡满足 |
| **I19** | 尖锐度非任意（「须随稀疏度**变化**」） | **`UNFALSIFIABLE_AS_WRITTEN`（方向未指定）** | 可跑 | **无。** 方向与参照分布均缺 |

> **Round-3 更正（`§2.9` 同步）**：A03 早先写的「19 条中 14 条 `HAS`、5 条 `UNFALSIFIABLE*`」**与上表不符**
> （`14 + 2 + 5 = 21 ≠ 19`，且上表只有 `I17` / `I18` / `I19` 三条 `UNFALSIFIABLE*`）。
> **逐行重数**：`HAS` = 14（`I1`–`I3`、`I5`–`I12`、`I14`–`I16`）/ `NOMINAL_ONLY` = 2（`I4` / `I13`）/ `UNFALSIFIABLE*` = 3（`I17`–`I19`）= **19**。
> 带 `EXECUTABLE_TODAY` 标签的 = **12**（`I1`–`I3`、`I5`–`I9`、`I12`–`I15`），**不是**早先写的 10。
> R07 §5.3 自评"9 条现在就能检查"—— **本报告裁定维持**：其中 8 条真正可失败，`I4` 是同义反复，`I13` 只是措辞审计。**0 条已执行。**

### 2.6 表征忠实度指标（R13 §13.2 / §13.3）

R13 §13.2 的**可判定性论证原文**：

> 「在冻结 fixture 上，下列量**完全可机器判定**（因为 fixture 本身是冻结的、有明确 `fact_status` 与 `source_anchor`）。」

| 指标 | 目标 | 形态 | 可执行性（**Round-3 扩宽**） | A03 的独立问题 |
|---|---|---|---|---|
| `SPAN_SUPPORT_RATE` | 1.0 | `HAS` | **`NOT_COMPUTABLE_ON_ANY_FROZEN_FIXTURE`**（**A03 早先只写 `_ON_FIXTURE_003`，范围偏窄**） | 判据要求"span 真实包含该断言"⇒ 需要 **span 原文**。**成因两类（见下表）** |
| `ENTITY_INSERTION_RATE` | 0 | `HAS` | **`NOT_COMPUTABLE_ON_ANY_FROZEN_FIXTURE`** | 需要"源窗口"原文，同上 |
| `UNKNOWN_PRESERVATION_RATE` | 1.0 | `HAS` | 可跑 | 真空满足（见 §4.3） |
| `FUTURE_LEAK_RATE` | 0 | `HAS` | 可跑 | 真空满足 |
| `HOLDER_LEAK_RATE` | 0 | `HAS` | 可跑 | 真空满足 |
| `DISTINCTION_LEAK_RATE` | 0 | `HAS` | 可跑 | 真空满足；且可被"把 fixture 的 `fact_or_narrative_status` 列直接复制进输出"平凡满足 |

**Round-3 范围更正：不是"一份 fixture"，是"三份全部"，且成因有两类**（`REJECTED_OR_WEAK_FINDINGS.md` R-I6）

| # | 成因 | 命中范围 | 逐字证据 | 后果 |
|---|---|---|---|---|
| **(i)** | **仓内不镜像源文本**，只存 paraphrase + 指针/锚点 | **`FIXTURE_001` + `FIXTURE_002` + `FIXTURE_003`（三份全部）** | `FIXTURE_001` §1：「LHRM stores only **paraphrased factual units and canonical pointer**, not a full-text mirror」；`FIXTURE_002` §1：「本仓库**不镜像全文**，只保存忠实 paraphrase 与定位锚点」；`FIXTURE_003` §1：「LHRM 本文件**不存储 transcript/audio 原文**，仅保存**忠实 paraphrase + 短锚点**」；`VALIDATION_CORPUS_V0_1.md:394`：「**No bulk text ingested into repo**」 | 即使重新取回 001 / 002 的公开文本（OGL / public domain，**法律上可做**），**在冻结 substrate 本身内**这两项仍不可算——它们测的是「抽取对源文本的忠实度」，而源文本不在被测物里 |
| **(ii)** | **rights gate fail-closed**，指针-only | **仅 `FIXTURE_003`** | `FIXTURE_003` §1：`rights_policy=HUMAN_REVIEW_REQUIRED` → `POINTER_HASH_ONLY` fail-closed（`raw_allowed=false, representation_allowed=false, store_pointer_only=true`）；`raw_artifact_ref=null`；`representation_artifact_refs=[]`；`content_hashes=[]`；`robots.txt` 含 `Content-Signal: ai-train=no` + `Disallow` GPTBot/ClaudeBot/CCBot；「不得通过 Eye 获取 transcript body」 | **这一格在任何权利状态下都不可补。** 与 (i) 叠加 |

> **X-14 口径**：上表证明的是「**在本仓已提交的三份 fixture 中**，需要源文本的两项忠实度指标不可计算」，
> **不是**「这两个指标在任何 substrate 上不可计算」，**也不是**「Fixture 003 的权利状态被违反」。
> 权利判定属 Human（`X-7`：fail-closed 是既定状态，本条不主张任何违反）。
>
> **与 `H-3` 的关系**：`§4.2` 的 `H-3` 行保留原文，但其"范围"按上表扩宽为**三份全部 + 两类成因**。

> **六个目标值全部位于区间端点（1.0 / 0），且六项中没有任何一项与弃答率或 coverage 配对报告。**
> R14 `F-13` 已独立指出需配对报告（"弃答率与覆盖率必须一起报告"），`M4` 要求 coverage–construct-count trade-off 曲线，
> **但 R13 §13.2 的表内没有这一对。**

| 统计量（R13 §13.3） | 形态 | 「什么结果会被算作失败」 |
|---|---|---|
| `CROSS_RUN_DISPERSION` | `NOMINAL_ONLY` | **无。** R13 自承"**不是精度**"；无参照分布、无目标值 |
| `HUMAN_LLM_LEAVE_ONE_OUT` | `NOMINAL_ONLY` | **无。** R13 自承"不是'LLM vs 人类'的胜负" |
| `MAPPING_FAILURE_PROFILE` | **`UNFALSIFIABLE_BY_CONSTRUCTION`** | **无。** 该统计量的支撑集被**三个互不相同的机制**压到近零（分类 / 分诊 / 阈值，见 `§1.4b`），而 R13 明确说它"**不是**失败率 KPI。它是**表示完备性的诊断 profile**"——一个完备性 profile 的一个支撑元素在**当前已登记的判据文本内**恒为 0。**独立来源数 = 1 primary（`§13`）+ 1 逐字镜像（`AGENTS.md:62`）** |
| `DIVERGENCE_CONCENTRATION` | **`UNFALSIFIABLE_AS_WRITTEN`（方向未定义）** | **无。**「若分歧**不**集中……那是**坏消息**」——但**零分歧**同时满足"不集中"与"无噪声"。判据无法区分"无语义歧义"与"什么都没做" |

### 2.7 泄漏规则 L1–L8 与 null B0–B7（R16）

| 规则 | 形态 | 可执行性 | 触发条件 / 失败结果 |
|---|---|---|---|
| L1 构念跨 split 泄漏 | `HAS` | `EXECUTABLE_TODAY` | outcome 由 `k` 的函数定义；或 `k` 唯一工具同兼 predictor 与 criterion → `NOT_IDENTIFIABLE` |
| L2 派生量含结果 | `HAS` | `EXECUTABLE_TODAY` | 派生量构造读取了 outcome 时点或之后的数据。**机械可判定** |
| L3 dyad 级泄漏 | `HAS` | `EXECUTABLE_TODAY` | 同一 `dyad_id` 的任何行落入两侧 |
| L4 时间泄漏 | `HAS` | `EXECUTABLE_TODAY` | predictor / 标准化 / 模型选择 / 填补 / 因子载荷读取 `> t` |
| L5 informant 泄漏 | `HAS` | **部分不可执行** | (b) 单方报告被解释为状态不对称。**但 R16 自引 R05 I3 指出 SRM accuracy 需 round-robin，两人 dyad 不满足 ⇒ (b) 只能靠标注** |
| L6 同源题项复用 | `HAS` | **`UNSATISFIABLE`** | R16 `F-06` 自承「R03 G9 标为**架构级 gap** → L6 **无法被经验地满足**」。**一条永远无法满足的规则不是检验** |
| L7 holdout 单次查看 | **`NOMINAL_ONLY`（自证）** | 可跑但**检测靠自证** | 触发明确，唯一执行者是分析者自写的 `deviation_log`。R16 `F-SELF11` 自评防线"**中。S07 表明这是制度问题而非备忘录问题**"；§11.4 自承"不主张'由分析者自己签'是充分的" |
| L8 选择 / 流失泄漏 | `HAS` | `EXECUTABLE_TODAY` | 入选概率依赖 outcome 或代理 → 必须报 attrition 表 + MNAR 敏感性 + `OUTCOME_CONDITIONED_SAMPLE` |
| B0 边际率 | `HAS` | `EXECUTABLE_TODAY` | 下限地板 |
| **B1 `AR_ONLY`** | `HAS` | `EXECUTABLE_TODAY` | 主判定规则原文：「候选方程必须……**配对地**击败 `B1`（persistence）与 `B2`（selection-only）。**只击败 `B0` 不算。**」——**全项目最锐的一条判据** |
| **B2 `SELECTION_ONLY`** | `HAS` | `EXECUTABLE_TODAY` | 稳定 per-dyad 截距无 wave-to-wave 增量。R16 自评「**最重要的一条 null，因为它已经击败过一个候选**」 |
| B3 `NO_PARTNER` | `HAS` | `EXECUTABLE_TODAY` | 移除 partner 侧信息后不损失 |
| B4 `MEASUREMENT_NULL` | `HAS` | `EXECUTABLE_TODAY` | 「**击败即推翻模型结构**」：同构念 `t` 与 `t+1` 联合估计后效应消失 → 合并而非两留 |
| B5 `LABEL_BASELINE` | `HAS` | `EXECUTABLE_TODAY` | 双有向坐标不比制度事实多提供什么 |
| B6 `MODEL_UNCERTAINTY_FLOOR` | `HAS` | `EXECUTABLE_TODAY` | 报告分布而非点估计（报告形式要求） |
| B7 `FIT_BASELINE` | `HAS` | `EXECUTABLE_TODAY` | 与最简饱和模型比较 |
| **`R16-UC08`** | `HAS` | `EXECUTABLE_TODAY` | 「**禁止**把 `R²` / fit / effect size 当作'模型是对的'的证据」。**把禁令写成禁令，是本项目最有效的一种可证伪写法** |
| **`FZ-0`** | `HAS` **但 `NOT_ENFORCEABLE_AS_WRITTEN`** | 见 §6 | 见 §6 |

> **记数更正**：mission 简报写「null 模型 B0–B6」，R16 报告实际为 **B0–B7（8 条）**。以报告为准。
> R16 §12 的 21 条 `F-SELF` 是本项目最有价值的自我批评；其中 `F-SELF20` 自评防线为「**无**。**无防线，本协议最严重的设计级风险**」——
> **`R16 对自身最致命缺陷的表述比本报告任何批评都更准确。**

### 2.8 对抗件判别式、撤退条件、消融计划

| 判据 | 形态 | 可执行性 | 说明 |
|---|---|---|---|
| **R15 `A01–A14`** | **14/14 `HAS`** | **`BLOCKED_NO_FIXTURE`（13/14）** | 每条写成「若〈具体失效模式〉**即失败**」，如 A05「带时间衰减先验的模型**自信地**产生零证据轨迹即失败」、A07「把文档当独立第二真相源即失败。**最强的单条**」、A11「last-write-wins 真值累积即失败」、A12「需要浪漫先验才能表达高强度 directed state 即失败」。**全项目形式最佳的判据集。** 但载体 `N15`/`N16`/`N18`/`N19`/`N20` 大量标 `SUBSTANCE_NOT_READ` / `UNVERIFIED_HINTESIS`，尚未冻结 ⇒ **A07 / A14 无法执行**。R15 同时设了正确的反泄漏纪律（N16「作者生平不得作为 dyad fact」；N19「**仅 expressivity probe，永不进 completeness 池。预设高 `MAPPING_FAILURE` 率为设计目标**」——**全项目唯一一处显式的"以高失败率为目标"，方向正确**） |
| **R09 `K1–K9`** | **9/9 `HAS`，且双分支** | 9/9 `NOT_ESTIMATED` | §9.6 表头原文：「每一条都写成「**若 X 则 Y**」……**当前九条全部处于未执行状态**」；列为「检验 / **若成立** / **若不成立** / 当前状态」。**全项目唯一一份两分支都写出后果的判据表。** `K5` 的否定支直接写「任一不满足 → **必须停在 `model hypothesis`**」 |
| **R17 `R1–R6`** | 6 条中 **5 条** `HAS` + **1 条不可判定** | **5 条可触发**（R1 / R2 / R3 / R4 / R5），**R6 不可判定** | **Round-3 更正（A03 早先写「6/6 `HAS` / `EXECUTABLE_TODAY`」）。** 逐条触发条件：**R1** 删 catch-all 后重跑 Fixture 001，**可跑**（动作 = 一次 schema 删改 + 一次三 verifier 盲跑；`#20/#21/#22` 隔离不构成阻碍，因为这是**新**执行而非读取既有 verifier 输出）；**R2** 层审计读数，**可跑但先决于 Architect 的层裁决**（`X-1`/`X-2` 已把层归属判为架构裁决项，实验本身不解决它）；**R3** invariance，**在当前数据下不可跑**（`R05 I11 BLOCKED_BY_DATA` + `R11 U1` 排序要求 ⇒ `18` U-5 死锁）；**R4** lattice/interval 表达力，**可跑但先决于 `Z` 的形式化被冻结**（`07` §2.3 自陈未冻结）；**R5** 同 R1 的更宽形式，**可跑**；**R6**「无法说出任何一条本 schema 会预测而领域现有 instrument 不会预测的命题」——**这不是实验，是一次无法封闭的搜索**，因此**不可判定**（穷举不能证明命题集为空）。**优先两项：R1 与 R5**，理由 = 二者动作同源（同一删改 + 同一次重跑），**边际成本为零**，而 R5 是 R1 的更宽形式（覆盖 `IRRELEVANT` / `NARRATIVE_ONLY` 之外的全部出口）。**R6 标记为 `UNDECIDABLE`，不得列为待办实验。** 每条都写明"放弃什么"（弱预登记，理由同本行） |
| **R17 `F1` 的可定案观察** | `HAS`（**全项目唯一真正可执行且后果明确的 falsifier**） | `EXECUTABLE_TODAY` | 「删除三个出口后，对 Fixture 001 的 C001–C026 重跑三 Verifier。若仍无一次 `MAPPING_FAILURE`，则该出口是唯一失败通道，须永久删除。」——有动作、有样本、有后果。**代价极低** |
| **R14 `M4` 消融** | **`UNFALSIFIABLE_BY_CONSTRUCTION`（限定为「当前已登记判据文本内」）** | — | 判据为「逐个删除 construct k → 记录 **`MAPPING_FAILURE` 上升**」。**在被登记的判据文本内，该上升的支撑集被三个机制压到近零（`§1.4b`）⇒ 消融几乎必然"成功" ⇒ 几乎必然得出"8 维是最小充分基"。** R14 用来解除 `F-14` 的唯一计划，**其成功判据在当前文本下是一个近似常数**。**Round-3 限定**：一旦 `§1.4b` 的三机制被修（尤其加一个 `redundancy` 类 + 收紧 `§14:679` 门槛），本行**不再是构造性的**——修法见 `§5.2` 改写 2 |
| **R14 `M2` 人类编码基线** | `HAS` | `EXECUTABLE_TODAY` | IRR **可以真的低**（R13 引 S02 专家 ICR 可低至 0.533；PedSHAC 事件-论元级 81.9 F1）。**全项目唯一一条"人做也会失败"的判据** |
| **R02 五 lens 判定枚举** | `HAS`（`INDEPENDENT` 需 ≥3 lens 正面分离证据；`UNKNOWN` 明示"**不作为'没有反例'的证据**"） | `BLOCKED_NO_DATA` | **但 R02 自设「本文件不裁决哪些构念该留、该删」⇒ 对 Gate C 无约束力。** R02 另指出 `F` lens 的方法学天花板（bifactor ESEM 与 ESEM 拟合等价） |

### 2.9 记分卡汇总（**Round-3 逐格重算，不转引任何旧合计**）

> **本表的每一格都是本次按 `§2.1`–`§2.8` 的行**逐行重数**得到的**。
> A03 早先的合计（`130 / 86 (66%) / 10 (8%) / 33 (25%) / 38 (29%)`）**保留在 `§R0` 之外**，
> 但其**三类不可比较**：(a) `§2.3` 六条的 `HAS` 计数未区分「有后果从句」与「无后果从句」；
> (b) `R17 R1–R6` 的 6 条被整行记为 `HAS / 今日可执行`，而其中 1 条不可判定、1 条在当前数据下不可跑；
> (c) `R13 §13.2` 的「今日可执行 = 4」隐含"两项只在 Fixture 003 上不可算"，范围已按 `§2.6` 扩宽为**三份全部**。

| 组 | 条目数 | `HAS` | `NOMINAL_ONLY` | `UNFALSIFIABLE*` | 今日可执行 / 可触发 |
|---|---|---|---|---|---|
| R06 判据 A–O | 15 | **15** | 0 | 0 | 1（`判 I`，纯文档判定） |
| R06 `MH1–MH6` | 6 | 1 | 0 | **5** | 0 |
| R06 `U-1…U-8`（自列） | 8 | 1 | 0 | 7 | 1（`U-3` → `R16 R16-OC03`） |
| R06 `U-9…U-13`（本 lane 新增） | 5 | 0 | 0 | **5** | 1（`U-11` 的缺陷本身） |
| R01 构念裁决 | 13 | **4** | 5 | **4** | 0 |
| `PARAMETER_CONVERGENCE` §2.1–2.6 | 6 | **2** | 3 | **1** | **0**（`§2.3` 见下注） |
| Gate A / B / C | 3 | **0** | 0 | **3** | 1（Gate A 可跑但不可证伪） |
| R07 `I1–I19` | 19 | **14** | 2 | **3** | **12**（**`I10` 因 `width` 未定义而不可构造，见 `§2.5`**） |
| R13 §13.2 六指标 | 6 | 6 | 0 | 0 | **4**（两项在**三份** fixture 上均不可算） |
| R13 §13.3 四统计量 | 4 | 0 | 2 | **2** | 2 |
| R16 `L1–L8` | 8 | 7 | 1 | 0 | 6（`L6` = `UNSATISFIABLE`，**恒不可满足 ⇒ 不是可跑检验**；`L7` 可跑但检测靠自证） |
| R16 `B0–B7` | 8 | **8** | 0 | 0 | 8 |
| R15 `A01–A14` | 14 | **14** | 0 | 0 | 1（13/14 `BLOCKED_NO_FIXTURE`） |
| R09 `K1–K9` | 9 | **9** | 0 | 0 | 0（`NOT_ESTIMATED`） |
| R17 `R1–R6` | 6 | **5** | 0 | **1** | **5 可触发**（R6 `UNDECIDABLE`） |
| **合计** | **130** | **86 (66.2%)** | **13 (10.0%)** | **31 (23.8%)** | **42 (32.3%)** |

**逐列求和的算式（供复算）**：
条目数 `15+6+8+5+13+6+3+19+6+4+8+8+14+9+6 = 130`；
`HAS` `15+1+1+0+4+2+0+14+6+0+7+8+14+9+5 = 86`；
`NOMINAL_ONLY` `0+0+0+0+5+3+0+2+0+2+1+0+0+0+0 = 13`；
`UNFALSIFIABLE*` `0+5+7+5+4+1+3+3+0+2+0+0+0+0+1 = 31`；
今日可执行 / 可触发 `1+0+1+1+0+0+1+12+4+2+6+8+1+0+5 = 42`。
**校验**：`86 + 13 + 31 = 130` ✓。

**与 A03 早先合计（`130 / 86 (66%) / 10 (8%) / 33 (25%) / 38 (29%)`）的差异来源（逐项）**：

| 列 | 早先 | Round-3 | 差异来源 |
|---|---|---|---|
| 条目数 | 130 | **130** | 无 |
| `HAS` | 86 | **86** | 抵消：R01 +1（`#11 Cohesion` 是 `HAS`，早先漏计）、`§2.4` −1（无后果从句，降为 `NOMINAL_ONLY`）、`R17 R1–R6` −1（R6 不可判定） |
| `NOMINAL_ONLY` | 10 | **13** | R07 +0 / R01 0 / `§2.1`–`§2.6` +1（`§2.4`）/ R01 分组更正不改变列计 / R06 `U-1…U-8` 的 `U-6` 记 `UNVERIFIED`（引用缺口）仍归 `UNF*` ⇒ 净 +3 |
| `UNFALSIFIABLE*` | 33 | **31** | R01 −1（`#6`/`#8`/`#10`/`#12` 实为 4 条，早先 5）、R07 −2（实为 3 条，早先 5） |
| 今日可执行 | 38 | **42** | R07 +2（实为 12，早先 10）、`§2.1`–`§2.6` −1（早先 1，实为 0）、R17 −1（R3 不可跑 / R6 不可判定 / R2 R4 需前置 ⇒ 早先 6 偏高 1） |

**`§2.1`–`§2.6` 六条的 Round-3 记法**（`HAS` 只给"带真失败条件"）：

| 判据 | Round-3 记法 | 理由 |
|---|---|---|
| `§2.1` Semantic independence | `NOMINAL_ONLY` | 问句，「无损替代」未定义 |
| `§2.2` Counterexample decoupling | **`HAS`** | 唯一带真失败条件者（但被"可能"软化） |
| `§2.3` Conditional incremental information | `UNFALSIFIABLE_AS_WRITTEN` | 「仍可能」无法被否定 |
| `§2.4` Scope stability | `NOMINAL_ONLY` | **Round-3 更正**：A03 早先记 `HAS`，但该条**没有任何后果从句**——"不稳定"没有写出会发生什么。降为 `NOMINAL_ONLY` |
| `§2.5` Layer test | `NOMINAL_ONLY` | 9 桶无优先级规则；降级 frame 存在但不可判定 |
| `§2.6` Representation necessity | `HAS`（承诺的检验不存在） | 保持 `HAS`，但加限定：**它承诺的臂不在 Gate A 内**（`§1.6`） |

⇒ 六条：**`HAS` = 2**（`§2.2` 带真失败条件；`§2.6` 带真失败条件但**承诺的检验不存在**），
`NOMINAL_ONLY` = 3（`§2.1` / `§2.4` / `§2.5`），`UNFALSIFIABLE*` = 1（`§2.3`），**今日可执行 = 0**。

> **对 mission 问题 1 / 2 / 3 的直接回答（Round-3 版）**
> - 转移律：**15/15 形态合格**，但只有 1 条今天可执行；`MH` 层 5/6 不可证伪；R06 自列清单**诚实但漏 5 条**。
> - 构念裁决：**13 条中 9 条（69%）不会因任何观测改变**（早先的「7 条 / 54%」是一个更窄的分组，见 `§2.2` 注）；
>   `MERGE` 与 `REJECT` 在**这一份报告**内从未被签发（report-scoped，见 `§1.6b`）。
> - 收敛判据：**六条全族缺四件套**（程序 / 证据 / 输出字段 / 阈值 / 执行者），需要改写的是**全族**不是一节（`§2.3`）。
> - 不变量：**14/19 形态合格、12 条带 `EXECUTABLE_TODAY` 标签、0 条已执行**；`I4` 同义反复，`I13` 只是措辞审计，
>   `I17` 阈值未定而空转，`I18`/`I19` 方向或阈值未指定，`I10` 因 `width` 未定义而不可构造。
>   **A03 早先写的「14/19 形态合格、10 条今天可执行」中，形态数正确，可执行数应改为 12**；
>   早先的「5 条 `UNFALSIFIABLE*`」应为 **3**（`§2.5` 末注）。
> - 泄漏规则与 null：**R16 是全项目形态与自我批评质量最高的一份**；唯一弱点是 `L7` 自证、`L6` 不可满足。
> - **门：3/3 不可证伪。** 这是本报告最重要的单一结论。

---

## §3 R06「当前不可证伪」清单的完整性核验

### 3.1 已列 8 条：诚实

| U-id | R06 要点 | 核验 |
|---|---|---|
| `U-1` | 「在只有自陈的设计中，律 A 与一个朴素的'行动→状态'律**在数学上不可区分**」 | **诚实且正确。** 它使 **`判 A` 的可证伪性成为条件性的**；R06 没有假装 `判 A` 可测 |
| `U-2` | 「**本 lane 未能验证**任何关于人类关系状态存在迟滞的来源」 | **诚实。** 与 R09 独立的 `NEGATIVE_RESULT` 方向一致 |
| `U-3` | 「终止事件是**设计性删失**，不是可处理的缺失」 | **诚实，且被 R16 `R16-OC03` 成功转为可机检标记**——本项目该转化的唯一成功案例 |
| `U-4` | 环境直通与行为通道「**尺度不匹配、不可分离**」 | **诚实** |
| `U-5` | 交换律负分支「**点名，不建设**」 | **诚实** |
| `U-6` | 火花/生长分类 | 属**引用缺口**而非可证伪性缺口；R06 已标 `AGENT_RECALL` + `UNVERIFIED` 并声明不使用该区分 |
| `U-7` | 「律 B 的 `Alt` 通道**在其自身被独立验证之前不可证伪**」 | **诚实，且是循环性警告** |
| `U-8` | level/slope 二分是否穷尽 | **诚实** |

> **裁定：R06 §10 在其自列范围内完整、诚实、无自我美化。** 一份把 5/6 个 `MH` 列为无支持、主动点名 8 条不可证伪项的报告，
> **其自我批评质量高于本批任何其它 lane。**

### 3.2 五处遗漏（本 lane 新增）

| 新增 | 内容 | 为什么漏了 | 严重度 |
|---|---|---|---|
| **`U-9`** | **`Ĝ_k` 门控无任何判据。** `判 B` 测 `NO-ATTRIB`（`Ω` 是否依赖 `R_i`），**不测** `Ĝ` 是否依赖 `Z`。`Ĝ` 由未观测函数决定，任何数据都可靠选 `Ĝ` 拟合。**而"状态依赖"正是律 A 区别于"行为直接更新状态"的全部内容。** | §4.5 承认 `damp` 支是 `MODEL_HYPOTHESIS`，§4.9 给了**事后**降级路径，但**无事前**判据；§10 把它归入"律 A"未单列 | **高** |
| **`U-10`** | **`⊕` 未预登记 ⇒ `Net_k` 不可识别 ⇒ 一切经 `Net_k` 的效应符号与量级均不可识别。** | §10 讨论"律不可证伪"，未讨论"**律的输入量不可识别**"这一更基础的障碍。**后果可写**：`NO-PARTNER` 获胜时可靠把 `⊕` 从求和换成序数聚合救回一个效应，从而**消解 `判 A` 的否定支** | **高** |
| **`U-11`** | **`K_pre` 选择自由度 = 预登记内部的选择泄漏。** | §10 未涉及"判据的参数由谁选"。**最隐蔽的一处**：预登记保证 `K_pre` 在看数据前冻结，但没保证它不是按"信念中介最可能成立"挑的 | **高** |
| **`U-12`** | **`RULE-⊥` 落在 §10 覆盖范围外**（§10 标题限定"不可证伪的**律**"）。五族**共享** `RULE-⊥`，而 `MH1` 无判据 | **只读 §10 的读者会得到"五族可测"的错觉** | 中 |
| **`U-13`** | **`判 I` 未推广。** R06 对 DVA 写了 void 条款；对 `RT`，它**自己在 §8.6 写下**「回溯填答的 `R_i` 会摧毁符号判定」，**却无**配套 void 条款 | R06 拥有全项目最好的判据模板，却没在自己最需要的四处使用（`判 A` 需实时 `R_i`；`判 B`/`判 D` 需 `Alt` 非回溯；`判 J` 需 `Ideal` 实时；`判 M`/`判 N` 需 `R_i` 实时） | 中–高 |

---

## §4 事后拟合（hindsight-fitting）风险登记册

### 4.0 关键前提

> **LHRM 项目至今没有产生任何一条 LHRM 映射输出。**
> 依据（全部本次实读）：`VALIDATION_CORPUS` L377「None of the 12 includes any mapping result」；
> `FIXTURE_001`/`002`/`003` 头部均标「**NO LHRM MAPPING**」；`00_MANIFEST` L36–37 与 `B-5`（`#20/#21/#22` 结果按隔离契约不查）；
> Wave 1 全部 18 份报告均自述 `RESEARCH_CANDIDATE`。
>
> **推论**
> 1. **LHRM 自己的数据上不可能发生阈值的事后拟合——因为没有数据。**
> 2. 真实风险因此不是"看到有利数据后改判据"，而是三种：
>    - **(a) 仪器与案例共设计**（判据从它将要测试的案例中抽象出来）；
>    - **(b) 从外部研究中继承阈值**（选那个恰好报出所需结果的研究作为 null / 对照）；
>    - **(c) 首次运行即首视**（所有判据 ex ante 且从未校准，第一跑同时是"检验"与"发现"）。
> 3. **(a) 最严重**：不产生可见痕迹，且无法从文档内部完全排除。

### 4.1 泄漏分级

判据：预训练中见到该文本的概率 × 该文本对"关系状态"的判别贡献。

| 层级 | 定义 | 成员 | 后果 |
|---|---|---|---|
| **T0 — 逐字 + 情节** | 全文或详尽复述高度可能在预训练中；**结局已知** | `L1-003` Magi（`HIGH — extremely famous, ubiquitous in pretraining, twist widely known`）；`L3-001` Yellow Wallpaper（`HIGH — ending widely known`）；`L2-003` Aspern（`VERY HIGH — canonical James, widely crawled, adaptations/summaries`）；`L3-003` Orpheus（`HIGH — myth ending universally known`）；`L3-002` Looking Backward（`MEDIUM-HIGH`） | 任何 `DIRECT_MAPPING` 率**不可识别**为表示质量 |
| **T1 — 情节 / 摘要** | 广被爬取与综述；措辞未必逐字 | `L2-002` Harriet Mill（`HIGH — SEP widely crawled`）；`L2-001` Sharland（`HIGH — leading authority, textbooks/summaries`）；`L1-001` StoryCorps（`MEDIUM-HIGH — famous StoryCorps/NPR staple + animation, widely quoted`） | 同上；语料已给出缓解（paraphrase probe、非逐字回忆） |
| **T2 — 低 fame 官方 / 近期** | 预训练中不太可能；结构可预测但内容不可预测 | `L0-001` Carty（其 `HIGH` 指**文档内**结局泄漏：`operative judgment (paras 1-8, GBP 2719.64 award…)`）；`L0-002` LGSCO（`MEDIUM-HIGH`，`Analysis + Agreed action + Final decision leak evaluation/trajectory`）；`L0-003` Mr. Jonas（`HIGH if uncleaned`，`Sec.3-5 … leak clinical judgment`，同为文档内泄漏）；`L1-002` BBC LAT（`LOW`） | **唯一可用于分离"表示质量"与"记忆量"的一层。语料中仅 4 份，其中 3 份未冻结** |

> **关键不对称**：语料的 `future_leakage_risk` 测的是**文档内 / 结局泄漏**（T2 的主要风险），
> 而本 audit 问的是**预训练记忆泄漏**（T0/T1 的主要风险）。**两轴被合并成一个字段，因而互相遮蔽。**
> 例：`L1-003` 字段值 `HIGH` 指结局，而它的**预训练记忆风险是全表最高**。
>
> **建议（finding，非 canonical 变更）**：该字段应拆为 `within_document_outcome_leakage` 与 `pretraining_memorization_risk` 两列。
>
> **Round-3 处置：登记为路由项，本报告不实施**（`C-P6` = `ACCEPT IMMEDIATE REPAIR`，落地在 canonical / Validation Gates PR）。
> **理由（可执行性，不是偏好）**：(a) 拆分要改 12 份材料的字段集 + `VALIDATION_CORPUS_V0_1.md` 的 schema 说明，
> 后者是 **canonical 文档**，本报告的 `Authority` 行禁止任何 canonical 变更；
> (b) 拆分后必须**重跑**任何引用该字段的判读（`H-1`…`H-10`、`R15` 的 `future_leakage_risk` 引用），
> 那属 Validation Gates PR 的变更面；(c) `AGENTS.md` Mutation discipline 要求 isolated branch + PR。
> ⇒ **本报告的责任止于：把"两列一格"的缺陷、可遮蔽的机制、以及最小修法写清，并交出路由。**

### 4.2 风险条目（severity 排序）

| id | 风险 | 严重度 | 证据 | 裁定 |
|---|---|---|---|---|
| **H-1** | **判据从它将要测试的案例中抽象出来（仪器–案例共设计）。** R07 §1.1 自述"**只读三份冻结件**的穷尽 harvest"；其 `FM-03` 的示例直接就是 Carty 的 `C013`/`C025` 与 Magi 的知识切片，并写「**可作为 Case Bank 条目立即落地**」——不变量与其测试对象是同一次阅读的产物 | **最高** | R07 §1.1、§6 `FM-03`；`FIXTURE_001` C013/C025；`FIXTURE_002` K1–K4 | **在三份 fixture 上测 `I1–I19` 不可能失败。** 不是造假，但必须披露，且新 fixture 上须重跑并预期不同结果 |
| **H-2** | **指标被设计成恰好可判定它所选那批 fixture 的字段。** R13 §13.2 的论证是"因为 fixture 本身有明确 `fact_status` 与 `source_anchor`"；R15 下一批将引入 `evidence_channel=ILLEGAL_OBSERVATION`（N04）、`t0_anchor`、`holdout_class`，**R13 的六指标一个都不读** | **最高** | R13 §13.2 vs R15 §15.1 | **六指标对 Fixture 001–003 会被完美满足，对 R15 下一批不保证迁移** |
| **H-3** | **`SPAN_SUPPORT_RATE` / `ENTITY_INSERTION_RATE` 在 Fixture 003 上永久不可计算** —— **Round-3 范围更正：范围是三份 fixture 全部，成因分两类**（见 `§2.6` 的成因表：(i) 三份都不镜像源文本；(ii) 仅 003 额外受 rights gate fail-closed） | **高** | R13 §13.2；`FIXTURE_001` §1 / `FIXTURE_002` §1 / `FIXTURE_003` §1 rights 状态；`VALIDATION_CORPUS:394` | **R13「完全可机器判定」的论证把 `source_anchor`（指针）当成了 span 文本。** X-14 口径：**在本仓已提交材料内**不可计算 |
| **H-4** | **全弃答与复制 fixture 列两条路径同时最大化 R13 全部六项**（六目标值全在端点，且无配对弃答率） | **高** | R13 §13.2 表；R14 `F-13` / `M4` 已指出需配对，R13 表内无 | 见 §4.3 |
| **H-5** | **语料在三个正交轴上被预过滤**：① 法律相关性；② 争议时间中心性（`recommended_cleaning` 保留 employment/closure/non-payment/CAB/claim chronology）；③ 事件密度（L0-003 开窗 1998–2008，`do not use full 23-year span`） | **高** | `VALIDATION_CORPUS` L0-001 / L0-002 / L0-003 | R17 `F9` 只指出第 ① 层。**三层叠加使全部官方材料的覆盖率成为过滤函数的产物** |
| **H-6** | **三份冻结 fixture 恰好是 12 份中歧义最低的三份。** `L2/L3 deliberately deferred until Verifier protocol is frozen` ⇒ 冻结集 = L0+L1；且 L0-001 的 `why_this_level` 自述「Facts are explicit actions … **Minimal interiority in facts section**」——语料把"内省性最低"当入选理由，而 LHRM schema 恰恰为 `Observation ≠ Belief ≠ latent state` 分离设计（该分离在内省 / 隐喻 / 嵌套引语上最费力） | **高** | `VALIDATION_CORPUS` L369 + L0-001 `why_this_level` | **"以最有利于自己 schema 的语料做第一轮"的最强证据，且写在语料自己的字段里。** 是选择效应，不是恶意 |
| **H-7** | **从外部研究继承阈值。** ① `判 G` 的形式来自 initial-differences 胜出的结果；② `B2 = SELECTION_ONLY` 自评「最重要，因为它已经击败过一个候选」；③ R17 `F2` 的层审计「5/5」**无预登记阈值** | 中 | R06 判 G；R16 §7 `B2`；R17 `F2` | ①② 是**正确**做法（null 越强越好，R16 明说 B2 已击败过一个候选）。③ 是**弱判据**：`5/5` 与 `2/5` 会被同一段文字处理 |
| **H-8** | **`判 A` 内部的 `K_pre` 选择泄漏**（`U-11`） | 中–高 | R06 §4.8 | 预登记只约束**顺序**，不约束**选择** |
| **H-9** | **R14 `M4` 的成功判据是可证明为常数的量** | 中–高 | R14 `M4` vs R17 `F1` | 修复计划内含一个被同一批报告证伪的指标 |
| **H-10** | **Fixture 输入与 ontology 有共同作者**（001/002 由 Architect 准备；002 明写"仅做材料清洗与冻结"） | 中 | 三份 fixture 头部 | R17 `A22` 已 `CHALLENGED`。补充：**共同作者 + T0/T1 泄漏 = 两种混淆源叠加**；且"选哪一段做 fixture"这一决定不在"仅做材料清洗"的覆盖范围内 |

### 4.3 「所有模型都会通过的测试」：两条平凡通过路径

> **是，存在。R13 §13.2 的六个指标构成一个被平凡满足的集合。**
>
> **路径 1 — 全弃答**（对每个冻结单元输出 `⊥` / 不产出任何 slot）：
> `SPAN_SUPPORT_RATE` = 1.0（无"无 span 的 slot"）✔；`ENTITY_INSERTION_RATE` = 0 ✔；
> `UNKNOWN_PRESERVATION_RATE` = 1.0（标 unknown 的单元"保留"为未抽取）✔；`FUTURE_LEAK_RATE` = 0 ✔；
> `HOLDER_LEAK_RATE` = 0 ✔；`DISTINCTION_LEAK_RATE` = 0 ✔。**六项全中。**
>
> **路径 2 — 复制 fixture 状态列**（把 `fact_status` / `fact_or_narrative_status` / `unit_type` 原样搬进输出）：
> `DISTINCTION_LEAK_RATE` = 0、`UNKNOWN_PRESERVATION_RATE` = 1.0 按构造成立；`SPAN_SUPPORT_RATE` 只需 anchor 存在（存在）。
>
> **为什么这不是吹毛求疵**：R13 §13.4 第 3 条自己写「任何单一数字（例如"抽取准确率 91%"）都应被视为**误导性产物**」；
> R14 `F-13` 写「**弃答率与覆盖率必须一起报告**」；`M4` 要求 trade-off 曲线。**三份报告都指出需要配对量，而 R13 的表里没有它。**
>
> **修法（只改判据）**：R13 六指标表**必须**在同一张表内为每项配一个**同向的弃答 / 覆盖率读数**，
> 且**六项的合格判定必须以"存在至少 N 个非 `⊥` 断言"为前提**（N 在登记时冻结）。
> **缺了这个前提，六项指标不是检验，是恒真式。**

### 4.4 「判据在看到结果后被改写」的机器可复核答案（**Round-3 降级**）

**第一层（packet → durable writeback）：A03 早先标 `NO_REWRITING_FOUND`（原文保留）。**

> **Round-3 降级（`REJECTED_OR_WEAK_FINDINGS.md` R-I5）**：这条**不是**高置信的机器否定结果。
> **方向很可能对，覆盖不完整。** 逐条依据：
> - **覆盖面 16 / 18。** Wave 1 有 **18** 条 lane（R00–R17）。本节逐行比对的只有 **16** 条：
>   已比对 = R00 / R01 / R02 / R03 / R05 / R06 / R07 / R08 / R09 / R11 / R12 / R13 / R14 / R15 / R16 / R17；
>   **未比对 = `R04`（`04_DATASET_LANDSCAPE.md`）与 `R10`（`10_MUTUALITY_POWER_DEPENDENCE.md`）。**
>   在这两条 lane 上，本报告**没有**任何 `Compare-Object` 记录。
> - **可复现性未被第三方验证。** Round-2 评审（`I-C26`）自陈**无法复现**本节的 `Compare-Object`，
>   且本节方法依赖 packet 文件的 `proposed_report_markdown` 段边界——**段边界的选择本身**就是一个未登记的自由度。
> - **未声明暴露面**（`§0.0` `TEMP-1`）：比对用的中间产物落在仓外临时目录，不受 `AGENTS.md` Mutation discipline 约束。
>
> ⇒ **本节现在支持的命题是**：「在已比对的 16 条 lane 上，未发现 writeback 削弱；**两条 lane 未覆盖**。」
> **本节不再支持**：「Wave 1 全覆盖、无判据弱化。」**`19:38` 记录的后者应改为本行。**

方法：把 16 份 child packet 的 `proposed_report_markdown` 段与 `docs/research/overnight-2026-09-27/` 下对应 durable 文件
做逐行 `Compare-Object`（trim + 去空行归一化）。

| lane | 仅见于 packet | 仅见于 durable | 判定 |
|---|---|---|---|
| R00 / R01 / R03 / R05 / R06 / R07 / R08 / R12 / R13 / R14 / R15 / R16 | 2–6 行（wrapper / 说明行） | **0** | 未改写 |
| R02 | 14 | **73** | **只增加**；新增内容把 E1 降为 `CONTESTED`、五个 lens 格全置 `?` —— **削弱性修复** |
| R09 | 2 | **210** | **只增加**；新增 §8 是**反对本 lane 自己头条结论**的论证 |
| R11 | 2 | **72** | **只增加**；新增内容自陈「结论强度被消解」「不推荐判 `PASS`（应改为 `UNKNOWN`）」 |
| R17 | — | — | **`R17_report_body.md` 与 durable 文件 SHA256 完全一致**（`7F8C9FB4…58D0`） |
| **R04** | **无记录** | **无记录** | **未比对**（Round-3 补记） |
| **R10** | **无记录** | **无记录** | **未比对**（Round-3 补记） |

> **降级后的结论：在已比对的 16 条 Wave 1 lane 中，0 条在 writeback 时削弱过任何判据；
> 3 条 repair pass（R02 / R09 / R11）全部只增不减，且新增内容一律使本 lane 自己的结论更弱或更有限定。
> `R04` 与 `R10` 未被覆盖，"Wave 1 全覆盖"这一说法不成立。**

**第二层（判据在作者自己的工作中是否后于发现）：部分存在**，见 `H-7` ③ 与 `H-8`。
无法从外部完全排除，因为 packet 与 durable 同源（见 `§8` `U-A`）。

### 4.5 Round-3 新增：`VALIDATION_CORPUS` 的「Recommended Fixture 001–003」是一处**已发生的**文档级冲突

> **性质**（`H-F28`）：**已发生**，不是假设。**A03 与 `18` 两份审计报告都因为「读文件而不是读索引」而躲过了它。**
> **修法在 canonical**（把旧文本标为被 `#19`/`#24`/`#25` 取代），**本报告不实施，只记录并路由**。

**冲突逐字对照**（本次实读两份文件）：

| 来源 | 逐字内容 | Fixture 001 | Fixture 002 | Fixture 003 |
|---|---|---|---|---|
| `docs/validation/VALIDATION_CORPUS_V0_1.md:348-365`（标题「**Recommended Fixture 001–003 (start here)**」） | 「**1. Fixture 001 — L0-002 (LGSCO Midshires Care, 24 001 994).**」「**2. Fixture 002 — L1-003 (Gift of the Magi, Gutenberg 7256).**」「**3. Fixture 003 — L0-001 (Carty tribunal, 2301968/2021).**」 | **L0-002** | **L1-003** | **L0-001** |
| `docs/validation/fixtures/`（**实际冻结的三份**） | `FIXTURE_001_L0_001_CARTY_FACT_PACKAGE.md` / `FIXTURE_002_L1_003_MAGI_PACKAGE.md` / `FIXTURE_003_L1_001_STORYCORPS_PACKAGE.md` | **L0-001** | **L1-003** | **L1-001** |

⇒ **3 个位置里 2 个不一致**（001 与 003），且 `Fixture 003` 的**材料层完全不同**（L0-001 Carty vs L1-001 StoryCorps）。
`VALIDATION_CORPUS:369` 末句「**L2/L3 deliberately deferred until Verifier protocol is frozen**」进一步说明
该推荐清单是**推荐**，从未被回写更新。

**为什么它对 A03 的结论有直接影响**（这是它落在本报告而不是只落在别处的原因）：

1. A03 §1.2 的 **Gate B 供给测试逐格对照**与 §2.6 的**六指标可计算性**都直接引用三份 fixture 的**身份**。
   **若某人照 `VALIDATION_CORPUS:348-365` 的索引去做，会把 Fixture 003 当成 Carty（官方公开、可取全文）**，
   从而把 `§2.6` 的 `NOT_COMPUTABLE_ON_ANY_FROZEN_FIXTURE` 判成 `COMPUTABLE`**——**结论直接翻转。**
2. §2.6 的成因 (ii)（rights gate fail-closed）**只**对 StoryCorps 版 Fixture 003 成立。索引与实物的这一处错位，
   使「哪一份 fixture 受权利限制」这个问题**可以答错**。
3. A03 §11.1 第 4 条引用了「Fixture 001–003 推荐 line 348–369」**而没有登记它已被取代**——本节补上。

**路由**（本报告不实施）：

| # | 修法 | 归属 | 依据 |
|---|---|---|---|
| **R-4a** | 在 `VALIDATION_CORPUS_V0_1.md:348-369` 加一行 supersession 注记：「本推荐清单已被实际冻结的 `FIXTURE_001/002/003` 取代（见 `docs/validation/fixtures/`）」，并把 3 条编号逐条改成实际映射 | **canonical（`docs/validation/`）**，属 Validation Gates PR（`C-P6` 同 PR） | `H-F28`；`AGENTS.md` Mutation discipline |
| **R-4b** | 交叉检查 `A01` / `A04` 的 fixture 相关指针是否也读了索引 | A01 / A04 的 owner（sibling `A1`） | 同上 |
| **R-4c** | 本报告 §11.1 第 4 条指针加「**已 superseded**」标记 | **本报告内，已完成**（见 `§11.1`） | — |

> **X-14 口径**：本节的命题是「**在本次实读的这两处文本之间**，Fixture 001 与 Fixture 003 的映射不一致」。
> **本报告不主张**任何一份材料被非法取用，**也不主张** Fixture 003 的 rights 状态被违反。

---

## §5 过弱判据清单与前 5 条改写

### 5.1 过弱到不起约束力的判据（完整清单）

| # | 判据 | 位置 | 为什么过弱（一句话） |
|---|---|---|---|
| 1 | **Gate A 全文** | `PARAMETER_CONVERGENCE` §15 | 5 步全是记录义务；无阈值、无 `若…则否决`、无修复外终态 |
| 2 | **Gate B 全文** | 同上 | 「至少测试」是覆盖要求；cell 缺失零后果；5/11 cell 无语料 |
| 3 | **Gate C 全文** | 同上 | 「通过」未定义；只有提升分支；6 条攻击中 4 条是复述 |
| 4 | **§2.3 Conditional incremental information** | 同上 §2 | 「是否**仍可能**提供额外信息」——可能性陈述无法被否定 |
| 5 | **§2.6 Representation necessity** | 同上 §2 | 唯一能删构念的准入判据，**但它承诺的 leave-one-out 检验在 Gate A 的 5 步里不存在**（`§1.6`）。**Round-3 措辞更正：不是"恒为假"，是"承诺的检验缺席"。** **且 scope 不止这一条**——六条判据全族都缺程序 / 证据 / 输出字段 / 阈值 / 执行者（`§2.3`） |
| 6 | **R01 `PPR = BELIEF_ONLY`** | R01 §4 | 信念/现实之别是定义性的，任何观测都相容；与 R17 `F3` 直接冲突且 R01 侧无判据 |
| 7 | **R01 `Satisfaction = DERIVED`** | R01 §4 | 唯一反证被吸收为"加一个 `comparison_baseline` 字段" |
| 8 | **R01 `Dedication = KEEP`** | R01 §4 + delta #3 | 自承与 §9 R3 内部不一致，处置是"强制声明"而非"二选一" |
| 9 | **R07 `I18` REFUSE 可达性** | R07 §5.2 | 存在量词 + 「某水平」未指定 ⇒ 被全缺失状态平凡满足 |
| 10 | **R07 `I19` 尖锐度非任意** | R07 §5.2 | 「须随稀疏度**变化**」未指方向、无参照分布 |
| 11 | **R07 `I17` coverage 显式** | R07 §5.2 | 禁令挂在「登记阈值」上，阈值 `UNKNOWN` ⇒ 禁令空转 |
| 12 | **R07 `I4` tag 闭包** | R07 §5.1 | 检查的是"是否绕过注册表"，不是"是否发生 ontology 蠕变" |
| 13 | **R13 六指标无配对弃答率** | R13 §13.2 | 全弃答与复制 fixture 列两条路径同时最大化全部六项 |
| 14 | **R13 `DIVERGENCE_CONCENTRATION`** | R13 §13.3 | 方向未定义；零分歧同时满足"不集中"与"无噪声" |
| 15 | **R13 `MAPPING_FAILURE_PROFILE`** | R13 §13.3 | 支撑集退化（`MAPPING_FAILURE` 不可达）⇒ 完备性 profile 信息量低于其声称 |
| 16 | **R16 `L7` holdout 单次查看** | R16 §4 | 唯一执行者是分析者自写的 `deviation_log`（自证） |
| 17 | **R16 `L6` 同源题项** | R16 §4 | R16 `F-06` 自承「**无法被经验地满足**」⇒ 恒真 |
| 18 | **R16 `FZ-0` freeze** | R16 §11 | 16 字段中至少 4 项不可在无数据接触下填写 ⇒ 「holdout 行未被读取」事后不可审计 |
| 19 | **R17 `F2` 层审计「5/5」** | R17 §3 | 无预登记阈值；`2/5` 会被同一段文字处理 |
| 20 | **R14 `M4` 消融** | R14 §6 | 成功判据 `MAPPING_FAILURE 上升` 恒为 0 |

### 5.2 前 5 条改写

> **改写原则**：只做三件事——(i) 把"记录义务"变成"判决"；(ii) 给 catch-all **吸收率**设**上限**（而不是给失败率设下限，
> 因为后者在 catch-all 存在时不可达）；(iii) 把"跑一次"变成"绑定 `(schema 版本, 语料版本)` 的一次性 freeze，变更须新起版本"。
> 数值以 `θ` 给出并标为占位；**约束力来自三条程序要求**（与 schema 同版本冻结 / 必须同时报告全部分项 / 变更必须新起版本），
> **不来自 `θ` 的具体取值**。`θ` 的取值属 Human / Architect 权限。
> **本节不写任何律、公式、参数、权重、阈值语义。**

#### 改写 1 — Gate A（追加于 §15 Gate A 之后）

```text
### Gate A — Court-fact sentence coverage（含判定）
[前置] 判定只允许对一对版本作出：S_k（schema 版本号）与 C（冻结单元全集）。
       S_k 必须在运行前 durable writeback；C = 全部冻结单元（当前 = 26+61+42 = 129）。
[执行] 1. 去掉法律条款、裁判理由、判决结果；2. 只保留 fact narrative；
       3. 独立 Agent 逐句映射；4. 记录所有 PARTIAL_MAPPING / MULTI_MAPPING / MAPPING_FAILURE。
[报告] 必须在同一份记录中同时给出以下四个计数，缺一即该次 Gate A 判定无效：
       (a) MAPPING_FAILURE 率
       (b) 三类"非失败出口"合计率 = NARRATIVE_ONLY ∪ IRRELEVANT ∪ Derived/Narrative-only
       (c) 三类"口袋类"合计率 = Environment ∪ History/Timeline ∪ Provenance/Uncertainty
       (d) 3 名盲 verifier 中 verdict 三者全同的单元比例
[删除] Gate A 期间必须物理删除三个出口：Derived/Narrative-only、IRRELEVANT、自由文本 provenance。
       若某单元确实无合法落点，唯一合法输出是 MAPPING_FAILURE。
[判定] 满足任一即 Gate A = FAIL（θ_1..θ_4 在 S_k freeze 时一次性固定，不得由数据反推）：
       (a) MAPPING_FAILURE 率 ≥ θ_1
       (b) 非失败出口合计率 ≥ θ_2
       (c) 口袋类合计率 ≥ θ_3
       (d) verdict 三者全同的比例 ≥ θ_4
[FAIL 之后] 唯一合法动作是记录 S_{k+1} 的变更 diff。S_{k+1} 上的一次 Gate A 是一次新判定，
       必须重新报告 (a)–(d)，并同时给出 S_k 的历史值。
       任何"只报告 verdict 分布而不报告 (b)(c) 分项"的记录无效。
```

**为什么这样变锐**：(b)(c) 之所以可达，是因为它们测的是 **catch-all 的使用量**而不是失败率——在 catch-all 存在时失败率不可达，
但 catch-all 的**使用量**总是可测的。R17 `F1` 建议的"删除三个出口后重跑"是同一思路的更激进版本；
本改写保留该删除要求，同时**在删除之前也给出可失败的判据**，使 Gate A 第一次运行就不是恒真。

#### 改写 2 — §2.6 Representation necessity

```text
### 2.6 Representation necessity（改为可失败形式）
令 C_k = 全部冻结单元中，3 名盲 verifier 独立判定其主落点不是 k 的单元集合
       （verdict 含 MULTI_MAPPING 时按该 k 计入 C_k）。

断言：|{ u ∈ C_k : 在不含 k 的 S_k 上给出 MAPPING_FAILURE }| ≥ θ_5。

失败条件（满足任一即 k 不通过 §2.6，从 candidate basis 移除或降级为 derived，并记录理由）：
  (a) 上式分子 = 0；
  (b) 上式分子 ≤ θ_5；
  (c) 3 名 verifier 对 C_k 中任一 u 的 verdict 不一致 → 记 REPRESENTATION_NECESSITY_UNDECIDED。

移除后必须重跑改写 1 的 (a)–(c) 并报告新值。
禁止的豁免：不得以"该单元是叙事性的 / 与关系无关"为由把 u 移出 C_k；
若认为该单元不需表示，必须走 §2.5 layer 判定并留下单独记录（不可与本条合并）。
```

**为什么这样变锐**：把"是否存在无法表示的句子"从**存在量词**变成**可数阈值**，并**显式封掉"叙事性豁免"这条逃逸口**——
而"叙事性豁免"正是 `Derived/Narrative-only` + `IRRELEVANT` + `merely narrative/irrelevant` 三者在 §13 / `AGENTS.md:62` 中共同提供的出口。
**不封这条，改写 1 的 (b) 也会被绕过。**

#### 改写 3 — §2.3 Conditional incremental information

```text
### 2.3 Conditional incremental information（改为可失败形式）
[登记] 每个候选 k 的判别设计 D_k：instrument、wave 数、side 绑定、样本量下界、方向性通道。
[断言] 在 D_k 下，k 在已知其余全部候选后，对 [当前状态 | 未来 Δt 转移] 的人内增量信息下界 > 0。
[失败条件（满足任一即 k 不通过 §2.3）]
  (a) 等价性检验（界在登记时冻结）判定 k 的增量信息与 0 等价；
  (b) 增量信息的 95% dyad-level 区间上界 ≤ 0；
  (c) D_k 所需数据在项目可及范围内不存在 → k 标 NOT_YET_TESTED，且不得计为通过。
[删除] 现措辞"是否仍可能为当前状态或未来转移提供额外信息"必须删除：
       可能性陈述不能被任何观测否定，因此该句在 §2 中不构成准入判据。
```

**为什么这样变锐**：把"可能"换成"在指定设计上被观测到"，并加 (c)。**(c) 是关键**：没有它，
一个构念可以靠"我们还没做那个实验"永远停留在 basis 里。R02 判定枚举里的 `UNKNOWN` 已写「**不作为"没有反例"的证据**」，
本改写把同一纪律推广到 §2.3。

#### 改写 4 — R01 `PPR` 的层归属

```text
PPR 层归属：改为双分支可失败登记（替换现 "BELIEF_ONLY" 单向表述）

H_state : PPR ∈ layer = Directed relationship state
H_belief: PPR ∈ layer = Belief（现裁决）

[判 H_belief 失败 → 改判 H_state] 满足任一：
  (a) 在控制全部 8 个 directed 坐标后，PPR 仍携带稳定的人内增量信息，
      且该增量在 ≥2 种关系类型上同号复制；
  (b) 存在一项观测显示 PPR 与 directed 坐标的残差相关在时间上先于 directed 坐标变化，
      且两个时点由外部锚定（非同一问卷施测）确定；
  (c) ResponsiveAction_(j->i) 的独立编码与 PPR 的分歧，在预测下游行为上互不冗余
      （二者各自在对方之外有增量）。

[判 H_state 失败 → 维持 Belief] 满足任一：
  (a) PPR 的分歧性预测力在控制 ResponsiveAction 后，区间含 0（等价性检验，非仅不显著）；
  (b) PPR 在跨关系类型上不满足 scalar invariance。

[程序] 两个分支的判据必须在同一次登记中一并写下；登记后不得只执行对己有利的一侧；
      只执行一侧者，该次执行结果标 INCOMPLETE_ASYMMETRIC_EVALUATION。
```

**为什么这样变锐**：R01 的现行裁决在**定义层**就把 PPR 定为 belief，因此"信念 vs 现实"的区分对它永远成立。
改写把它变成**两个竞争假说**，各配至少一条失败条件，并显式封掉"只做有利的一侧"这一典型 researcher-DoF。
R17 `F3` 提供的正是 (b) 与 (c) 的具体形式；**本改写不新增任何实证要求。**

#### 改写 5 — R16 `FZ-0` freeze

```text
FZ-0 拆为两个时点（替换"在任何 holdout 行被读取之前"这一无法事后审计的条款）：

FZ-A（零数据接触）：只填 §11.2 的字段 1,2,5,6,7,9,10,11,12,13,15,16。
      产物 = FREEZE_RECORD_A，含 code_commit 与 mapping_table_ref 的 commit hash。
      FZ-A 不成立 ⇒ 不得打开数据文件。

FZ-B（FZ-A durable writeback 之后）：才允许打开数据文件。
      此后只允许读取 calibration 侧行 + dyad_id / wave_id 清单；
      holdout 侧任何列不得进入任何进程、任何中间文件、任何 prompt。

新增两条可事后审计的机器证据（缺任一 ⇒ 该次 freeze 视为未发生）：
  (a) holdout_access_log：FZ-B 之后每一次数据文件打开的
      {timestamp, file, columns_read, filter}；columns_read 与 holdout 列清单的交集必须为空，
      由 CI 强制检查，不接受人工声明。
  (b) split_assignment_hash 的生成代码必须在 FZ-A 的 commit 中，
      且生成过程只依赖 dyad_id 清单（不得读入任何 outcome 列）。

两处硬性收紧：
  (c) estimator_family 不得取 TBD_AT_FZ1。若 estimator 未定，则 FZ-A 不成立，holdout 不解锁。
      （现文本允许占位符进入已冻结记录，使"冻结"在最关键的一项上是空的。）
  (d) L7 的触发不再由分析者自证：holdout_access_log 中任何一次列交集非空 → 自动 EXPLORATORY。
```

**为什么这样变锐**：现文本的 16 字段中，字段 4（`dyad_id`/`side`/`wave_id` 的**确切变量名及其发货状态**）、
字段 7（`每个 holdout 的 wave 列表`）、字段 8（**完整 assignment 列表 + 其 hash**）、字段 14（`min_detectable_effect`）
都要求接触数据清单。生成 assignment 列表必须知道 `dyad_id` 清单，而清单在数据文件里。
⇒ **要么这些字段在无数据接触下填不出来（则 §11.1 的时点前提与 §11.2 的必填清单自相矛盾），
要么分析者在 freeze 前已打开数据文件（则"任何 holdout 行被读取之前"已被违反或不可证）。**
改写把可审计性建立在**机器可查的访问日志**上。**只增加审计机制，不改变任何科学主张，也不构成合规判定。**

---

## §6 预登记现实性：R16 `FZ-0` 的可执行性裁定

**R16 自己的提问与自答（逐字）**

> §12 `F-SELF11` 防线栏：「**中。** S07 表明这是**制度**问题而非**备忘录**问题」。
> §11.4：「本协议也不主张'由分析者自己签'是充分的 —— 那正是 S07 描述的自适应反馈通道。」

**A03 独立裁定：`NOT_ENFORCEABLE_AS_WRITTEN`，四条可复算理由**

| # | 理由 | 证据 |
|---|---|---|
| 1 | **必填字段不可从文档导出。** 字段 4 要求"`dyad_id`/`side`/`wave_id` 的**确切变量名及其发货状态**"；字段 8 要求"**完整 assignment 列表 + 其 hash**"；字段 14 要求"由 `… 的 dyad 数`推出"最小可检测效应。生成 assignment 列表必须知道 `dyad_id` 清单，而清单在数据文件里 ⇒ **§11.1 的时点前提与 §11.2 的必填清单自相矛盾，或该前提不可证** | R16 §11.1 vs §11.2 字段 4/7/8/14 |
| 2 | **`estimator_family` 允许占位符。** 字段 12 逐字：「**若 R06 的律族形式尚未被 Architect 裁决，写 `TBD_AT_FZ1`**」；而 R06 §12 明确请求 Architect 裁决 MH1 与 RGM，R16 §17 也把它登记为待裁决项 ⇒ **在最关键的一项（估计量族）上，freeze 允许为空** | R16 §11.2 字段 12；R16 §17 |
| 3 | **"不可变"由 Git 承担，而 Git 提供持久性而非不可变性。** §11.1 要求 Architect durable writeback；`AGENTS.md` Mutation discipline 规定 material semantic changes 走 branch + PR —— **但没有任何一处说 `FREEZE_RECORD` 必须走 PR 审查**。同一位分析者既有写权限、又有 commit 权限、又有把偏离记为 `EXPLORATORY` 的裁量权；§11.3 的"未记录的偏离 → 结论作废"依赖**记录本身的诚实性**。**本次审计实测到一个实例**：Wave 1 报告在 `8ee07c2`（manifest 记为终稿写回）之后，`02b_CONSTRUCT_REDUNDANCY_AUDIT.md` 与 `11_GENERAL_HUMAN_DYADS_SCOPE.md` 仍在工作树中被追加 repair-pass 内容（+107/−7 与 +98 行，mtime 09:08 / 09:10，HEAD = `2d392ba`）。**即：被用作证伪判据输入的报告，其自身在写回后仍在变动。**（该改动不是 A03 造成的；A03 全程只读。） | R16 §11.1 / §11.3；`AGENTS.md` §Mutation discipline；`git status` / `git log` 实测 |
| 4 | **`R16-ID11` 主动放弃了第三方复核能力。**「`FREEZE_RECORD` **不得包含个体级数据行**」→ 外部第三方**无法独立复核映射行**。R16 §9 末段自陈：「**它使外部第三方无法独立复核 `FREEZE_RECORD` 的映射行**……本协议**不**把它包装成已解决。」⇒ **在这个取舍下，freeze 的可审计性只能由内部人完成** | R16 `R16-ID11`；R16 §9 末段 |

> **结论：R16 的 freeze 目前是一份备忘录 + 一个约定，不是机制。**
> R16 的自评（"制度问题而非备忘录问题"）**准确且诚实**；A03 的贡献是把"为什么"具体化为上面 4 条。
> **成本判断：这是全项目最便宜的一处修复**——改写 5 只增加一个 CI 检查与两条记录字段，
> 不需要新数据、不需要新的科学主张、不触碰任何权利判定。

---

## §7 矛盾与负结果

### 7.1 跨 lane 矛盾

| id | 矛盾 | 状态 | A03 备注 |
|---|---|---|---|
| **X-1** | **PPR 层归属。** R01 判 `BELIEF_ONLY`；R17 `F3` 判这是**承重错误**（引 Segal & Fraley 2016 的「PPR … **serves as an organizing variable**」+ Joel et al. 2020 的 top-1 predictor = `perceived partner commitment`） | **Round-3：`UNRESOLVED`，但「R01 侧无判据可败」这一措辞已被 `X-2` 的裁决取代。** Architect 已把 `PPR` 判为 **BeliefState（settled for current architecture）**，并把 `17` F3 的层边界主张降为 `WRONG-SCOPE` 的**竞争经验假说**（`C-1` / `X-2`）。**因此本行的"未解"应读作"层归属已定，被争论的是预测/持久性角色"。** A03 的改写 4（双分支登记）**只适用于角色问题，不适用于层归属** | R16 `F-SELF20` 已登记为「**无防线。本协议最严重的设计级风险**」。**A03 补充（保留）**：这不是"两说并存"，而是"一方写了一条无判据的裁决" → 改写 4（**限定为角色分支**） |
| **X-2** | **`Satisfaction` 的层。** R01 判 `DERIVED`（但要求 `DerivedEvaluation` 并保留时序能力）；R17 `A21` 判「CHALLENGED」，理由是它是该领域**唯一**纵向验证的 DV、外部效度锚点 | **Round-3：层已定为 Derived / evaluation-state candidate（`C-2`）。** 残留 = **条件后果预登记**（若日后满足自己的提升判据，须重审 D7 / basis 冗余），**不是**现在的二选一 | R01 的处置是"加 `comparison_baseline` 字段"（吸收逃逸口）——**该吸收口被 `C-8` 条件后果注记部分封住，但未封死** |
| **X-3** | **`Dedication` 的地位（四方并存）。** R01 `KEEP`（自承与 §9 R3 内部不一致）；R02 `E8` `SUPPORTED_REDUNDANCY（~54%）`；R03 `NOT_IDENTIFIABLE 直到自建工具`；R06 `判 E` 会**拒绝**它为 primitive | **Round-3：`NO_LOGICAL_CONTRADICTION`（`X-3`）。** D7 / R3 不构成二选一；残留的是 **facet 切点**（`02b` U4 + `18` CF-05）。A03 本行早先的"既不会被删，也不会被确认"是**对四方并存的事实描述**，不是逻辑矛盾判定——保留 | `判 E` 是唯一能删它的判据，被 R03 的测量纠缠阻塞。**A03 Round-3 补充**：这条链有一个未覆盖的**单向依赖**（`06` → `02b`，见 `18` §5.3b `U-12`） |
| **X-4** | **`§9 R2 PowerImbalance = f(OutcomeDependence, …)` 的输入不可测。** R01 判 `OutcomeDependence` `MEASUREMENT_INFEASIBLE_AT_RELATION_LEVEL`；R02 把它放在"必然出现但未冻结的隐变量"格 | 一致，但后果未被追到底 | **A03 追到底：由一个无工具的量做派生的派生式，无法被证伪。`§9 R2` 应标 `UNFALSIFIABLE_AS_WRITTEN`**。**Round-3 限定（`X-13`）**：`TotalDependence/TotalPower` 已判为**对称派生聚合**、`RelativePower/PowerImbalance` 判为**方向性读出**，二者都仍依赖 D8 的工具地位；`X-13` **不**解决工具问题 |
| **X-5** | **R17 `F9` 要点 2 的字面表述** | **需更正**（原文保留） | **Round-3 精确化**：8/11 是 **scope 标签**（`§1.5`、`§1.7`）。**注意：A03 驳回的是 `R17` 的措辞，不是提出一个替代数字。** `19:35` / `19:182` 把 A03 记成"修正为 8/11"是**误引**——`§1.7` 给出 A03 的真实结构与独立重算 |
| **X-6** | **`R16` §11.1 vs §11.2 字段 12** | 未解 | §6 理由 2 |
| **X-7** | **`R13` §13.2「完全可机器判定」vs fixture rights 状态** | **Round-3：范围扩宽为三份 fixture 全部、两类成因**（原 `X-7` 只写 Fixture 003） | H-3 + `§2.6` |
| **X-8** | **`R14` `M4` 的成功判据 vs `R17` `F1`** | 未解 | H-9。**Wave 1 内部一处未被任何人指出的矛盾** |
| **X-9** | **Gate B 要求 friendship / caregiving / kin / same-sex / high-dependence-low-liking，而语料对这 5 类零覆盖；R15 把补齐列为下一批且多数标 `UNVERIFIED_CANDIDATE`** | 已知（manifest `B-1`） | **A03 补充**：这使 Gate B 在语料层就 `NOT_EXECUTABLE`，因此"Gate B 未通过"与"Gate B 未执行"在当前文档中无法区分。**Round-3 两处限定**：① `caregiving` 一格按宽口径是 **partial = 2/12，不是 0**，且成因部分来自 **rights / access gate**（`§1.2` 注）；② `5/11` 的分母不可用，Gate B 须拆成两张表（`C-P2`） |
| **X-10** | **Round-3 新增：`VALIDATION_CORPUS` 的「Recommended Fixture 001–003」与实际冻结的三份在 2 / 3 个位置上不一致** | **已发生**（`H-F28`） | `§4.5`。**修法在 canonical，本报告只记录并路由** |
| **X-11** | **Round-3 新增：五条候选律的处置** | **全部 `NONE FROZEN`**（`X-11`） | A03 §2.1 的 15 条判据 A–O 仍是各律的**判别模板**；**但没有一条律被冻结**。`§2.1` 的 `HAS` 计数**不得**被读作"律已成立" |

### 7.2 本 lane 的负结果

| id | 负结果 | 强度 |
|---|---|---|
| **N-A03-1** | **Gate A / B / C 三者在判据原文下均不存在会被算作失败的结果。** 独立于 R17，用 T1/T2/T3 得出。**Round-3 修正理由**：`EV1` 指出**缺的不是否决分支**（分支意图在 `AGENTS.md:54` / `CURRENT_ARCHITECTURE.md:158` / `CONSTRUCT_SCOPE_DIRECTIONALITY.md:107` 四处都写清了），**缺的是「后果动词 + 阈值 + 一个诊断类型 + 一个 ablation 步骤」四件套** | 高（可复算；结论不变，**理由须换**） |
| **N-A03-2** | **`§2.6`（唯一能删构念的准入判据）承诺了一个 Gate A 不包含的 leave-one-out 检验。** 文档写下来的移除路径只有 `R06 判 E` 与 `R17 R3`，二者都需项目没有的数据。**Round-3 更正措辞：不是"结构上永远不能触发"（那是推论），而是"承诺的检验缺席"（那是可验证的文档事实）。** | 高（文档事实部分可逐行复算） |
| **N-A03-3** | **在 `02_CONSTRUCT_CONVERGENCE.md` 这一份报告内，7 值裁决词表的 `MERGE` 与 `REJECT` 各出现 1 次（均在 `:37` 词表声明行）且从未作为裁决值被签发；13 条裁决中 7 条（54%）不会因任何观测改变。** **Round-3 更正作用域：这是 report-scoped 的词表使用率，不是项目级事实**（`§1.6b`） | 高（token 计数可 grep 复算；**提升为项目级事实这一步是错误来源**） |
| **N-A03-4** | **`R13` 六指标存在两条平凡通过路径（全弃答 / 复制 fixture 状态列）；2/6 在三份已冻结 fixture 上均不可计算（成因两类：(i) 三份都不镜像源文本；(ii) 仅 Fixture 003 额外受 rights gate fail-closed）。** | 高（`§2.6` 逐条列证据） |
| **N-A03-5** | **`R06` §10 遗漏 5 条（`U-9…U-13`），其中 3 条高严重度。** 已自列的 8 条则全部诚实 | 中–高 |
| **N-A03-6** | **`R17 F9` 要点 2 的字面表述 8/11 不成立。** | 中（对 sibling lane 的可验证更正） |
| **N-A03-6b** | **Round-3 新增：`§15 Gate B` 的 11 格混了抽样框语境（8）与构念解耦模式（3）两种条目，因此不存在有意义的单一分母；A03 早先自己用的 `5/11` 同样不可用。** | 高（`§1.2` 注 + `§1.7`） |
| **N-A03-6c** | **Round-3 新增：A03 自己在 `§1.5` 把 Gate B 的 `high-attraction/low-trust` 映射到 `§4 D4` 的「可高**喜欢**低信任」，而同一份文档在 D1 明写 Liking 与 RomanticAttraction 是两个构念 ⇒ 该格的归属关系不成立。独立重算 = 11 格中 10 格可归因于项目文本，第 11 格归属不成立；**本报告不宣布替代分母。** | 高（可逐行复算：`PARAMETER_CONVERGENCE:131` vs `:179`） |
| **N-A03-7** | **Wave 1 writeback 阶段不存在判据弱化。** —— **Round-3 降级为「在已比对的 16 / 18 条 lane 上未发现；`R04` 与 `R10` 未覆盖」。** 3 个 repair pass 只增不减且新增内容一律削弱自身结论；`R17` body 与 durable SHA256 一致。**`19:38` 记录的项目级版本不成立。** | 中（**从"高（可机器复算）"降级**：覆盖面 16/18，且方法被第三方判为不可复现，R-I5） |
| **N-A03-8** | **项目至今无任何 LHRM 映射输出，因此"看到有利数据后改判据"在项目数据上不可能发生。** 真实风险是仪器–案例共设计。**X-14 口径**：依据是 `VALIDATION_CORPUS:377` + 三份 fixture 头部 + `00_MANIFEST` `B-5`，即**在本仓已提交材料内**无映射输出 | 高 |
| **N-A03-9** | **`R16 FZ-0` 不可执行性：16 字段中至少 4 项不可在无数据接触下填写 ⇒「holdout 行未被读取」事后不可审计。** | 高 |
| **N-A03-10** | **`VALIDATION_CORPUS` 的 `future_leakage_risk` 把「文档内 / 结局泄漏」与「预训练记忆泄漏」合并为一列，互相遮蔽。** **Round-3：登记为路由项（`C-P6`），本报告不实施**（`§4.1`） | 中–高 |
| **N-A03-11** | **Round-3 新增：`VALIDATION_CORPUS:348-365` 的「Recommended Fixture 001–003」与实际冻结的三份在 2 / 3 个位置不一致（001 = L0-002 vs L0-001；003 = L0-001 vs L1-001）。这是**已发生**的文档级冲突，两份审计报告都因读文件而非索引而躲过。** | 高（逐字对照可复算；`§4.5`） |
| **N-A03-12** | **Round-3 新增：`R17 §5` 的六条退守实验中，五条可触发、`R6` 不可判定（它是一次无法封闭的搜索）。** A03 早先记 `6/6 HAS / EXECUTABLE_TODAY`。优先项 = `R1` + `R5`（动作同源、边际成本零） | 中–高（`§2.8`） |

---

## §8 剩余未知

| id | 未知 | 为什么重要 | 需要什么 |
|---|---|---|---|
| **U-A** | 各 Wave 1 lane 的判据在**作者自己的工作中**是否曾按已见结果调整。`§4.4` 第一层在已比对的 16 / 18 条 lane 上未发现 writeback 弱化，但 packet 与 durable 同源，第二层不可从外部检验。**Round-3 新增两条缺口：`R04` / `R10` 未被比对；scratch 产物落在仓外未声明暴露面（`§0.0` `TEMP-1`）** | 决定 `H-7` / `H-8` 的实际严重度 | 各 lane 的中间工作稿 / 检索日志 / 被否决的候选判据；`R04` / `R10` 的 packet-vs-durable 比对。**本次不可得** |
| **U-B** | 三份 fixture 上人工 verifier 的**真实 ICR**。R13 `U-5` 已登记；`#20/#21/#22` 按隔离契约不查 | 若 ICR 极低，则改写 1 的 (d) 在任何阈值下都会 FAIL，Gate A 的可用性本身受质疑 | 隔离解除后由 Architect 提供 |
| **U-C** | `Ĝ_k` 在任何真实数据上是否可识别 | 决定 `U-9` 是"暂缺判据"还是"根本不可识别" | R06 提供 `Ĝ` 的候选形式与识别条件 |
| **U-D** | `⊕` 的可选聚合算子集合是否有任一在关系数据上被独立比较过 | 决定 `U-10` 的严重度 | 检索序数聚合 / 名义型计数在 dyadic panel 上的比较研究 |
| **U-E** | Gate B 缺失 5 类语料的**可获得性**。R15 的 `N13`（Pepys 1661 条目）与 `N14`（Pliny Ⅲ.7 / Ⅳ.7）是唯二高证据候选，且 R15 自标 `UNVERIFIED_HINTESIS` / `UNVERIFIED_CANDIDATE` | 决定 Gate B 能否从 `NOT_EXECUTABLE` 变成可执行 | 实读 Pepys 1661 条目与 Pliny 原信。**本次未尝试外部抓取** |
| **U-F** | **若执行 R17 `F1` 的"删除三个出口后重跑"，Fixture 001 的 26 个单元会产生几次 `MAPPING_FAILURE`。** 这是全项目唯一一条可执行且后果明确的 falsifier，**尚未运行** | 这是本报告中唯一能给项目一个真实负结果的实验 | 一次三 verifier 盲跑。**成本极低** |
| **U-G** | 若按改写 5 拆成 FZ-A / FZ-B，16 字段中是否还有字段无法在 FZ-A 填写。本报告只证明了"至少 4 项需数据清单" | 决定改写 5 是否够 | 对 16 字段逐项分类 |
| **U-H** | A01 / A02 / A04 是否已发现同类问题（本报告未读它们，避免跨 lane 重复） | 避免 Wave 2 三份报告重复计票 | 由 parent 交叉比对 |

---

## §9 明确不主张

1. **不主张任何外部实证结论为真或为假。** 本 lane 未打开任何外部来源；文献名只作为"某 lane 如此声明"的转录（`VIA_WAVE1`）。
2. **不主张 LHRM 项目应被放弃，也不主张它应被继续。** 本报告只审计仪器，不审计目的。
3. **不主张 Gate A/B/C 应被删除。** 本报告主张它们**按原文不能失败**——**Round-3 补一句理由上的更正**：
   **缺的不是否决分支**（否决意图在 `AGENTS.md:54` / `CURRENT_ARCHITECTURE.md:158` /
   `CONSTRUCT_SCOPE_DIRECTIONALITY.md:107` 四处都写清了），**缺的是「后果动词 + 阈值 + 一个诊断类型 + 一个 ablation 步骤」四件套**。
   删除、改造或降级为"缺口清单"是 Architect / Human 权限。
4. **不主张本报告的 `θ1..θ5` 取值是恰当的。** 改写只主张三条程序要求（与 schema 同版本冻结 / 必须同时报告全部分项 / 变更必须新起版本）。
5. **不主张改写 1–5 构成 canonical 变更建议。** 它们是判据草案；`CANONICAL_MUTATION = FORBIDDEN`。
6. **不主张 R06 / R13 / R16 / R17 的结论为假。** R17 `F1`/`F9`/`F11` 经独立复核为 CONFIRMED（`F9` 一处需更正）；R06 §10 与 R16 §12 的自评**准确**。本报告批评的是**未覆盖处**。
7. **不主张 §4.4 第一层的"无改写"结论适用于 packet 生成之前。**
8. **不主张 R07 中未通过的 5 条不变量应被删除。** `I17`/`I18`/`I19` 只需阈值与方向。
9. **不主张 Fixture 001–003 应被替换。** 本报告主张的是"第一次 Gate A 运行前必须先做改写 1 的 (b)(c) 分项统计"。
10. **不主张任何 Case Bank 材料的 `future_leakage_risk` 评级是错的。** 本报告主张该字段**混合了两个正交轴**。
11. **不主张读过 LHRM issue `#20`/`#21`/`#22` 的任何内容。** `U-B` 保持 open。
12. **不主张本报告的记分卡标签是唯一正确的分类。** §0 的三测试与 §4.4 的比对方法可原样复算；标签本身可被不同分类替换。
13. **不主张文献数量或 LLM 一致度构成验证**（承接 `00_CHILD_CONTRACT.md` §2）。
14. **不主张 14（Round-3 新增）** 上面 `§1.7` 的独立重算给出了 `10/11` 这个替代数。**本报告明确不宣布替代分母**：
    `high-attraction/low-trust` 应归属哪一条 `§4` bullet，需要读原文的人裁决；
    而且更根本地，**Gate B 的清单混了两种条目，替代分母这个提法本身就不成立**（`C-P2`）。
15. **不主张 `caregiving` 一格"应当算作已覆盖"。** 本报告只指出 A03 早先的 `0` 是**口径依赖的**，
    并给出宽口径下 `partial = 2/12` 这个数；**哪一个口径被采纳是 Gate B 重写时的设计决定**（`C-P2`）。
16. **不主张 Fixture 003 的 rights 状态被违反，也不主张任何权利裁定。** `§2.6` 成因 (ii) 只陈述
    `rights_policy=HUMAN_REVIEW_REQUIRED → POINTER_HASH_ONLY fail-closed` 这一**已记录状态**；`X-7` 把"是否构成违反"留给 Human。
17. **不主张 `VALIDATION_CORPUS` 的推荐清单应当被删除。** `§4.5` 的主张是它**已被实际冻结取代**，
    **修法是加 supersession 注记**（canonical，Validation Gates PR），不是删段落。
18. **不主张 R17 §5 的 `R6` 是可判定的，也不得把它列为待办实验**（`§2.8`）。
    本报告同样**不主张**它已被证伪——**不可判定与已证伪是两件事**。
19. **不主张 §0.0 `TEMP-1` 的未声明暴露面导致了任何具体错误。** 本报告只主张：凡是依赖
    "durable 文本 vs packet 文本"之差的结论，必须把它算进不确定性预算。
20. **不主张 `17:549` 的 Crossref 总括声明已造成任何具体误引**（`§11.5`）。本报告只主张该量词在
    `17` 自身内部即不成立（`H-F24`），并**不重复**该声明。
21. **不主张本报告的 Round-3 记分卡（`§2.9`）比 A03 早先的记分卡"更正确"。** 两者都用同一套 `§0.1` 标签；
    Round-3 的差别来自 (a) 六条判据按"有无后果从句"重判、(b) `R17 R1–R6` 逐条判可触发性、
    (c) fixture 不可计算范围扩宽、(d) 早先三处**求和不自洽**被逐行重数修正。
    **分类约定仍可被不同约定替换**（承接第 12 条）。**特别是**：`§2.2` 的「7 条 / 54%」是一个**更窄的分组判断**，
    本报告只把 **9 条 / 69%** 记为**上界**，**不主张** 7 这个分组本身是错的。
22. **不主张本报告的 repair 请求必须被采纳。** 它们按"修起来便宜 / 收益大"排序，是建议不是要求。

---

## §10 给各 lane 的窄修复请求（`NARROW_REPAIR_REQUEST`）

> 每条只要求**一处**修改，且**不新增任何律、构念、参数、权重、阈值语义**。按"修起来便宜 / 收益大"排序。

### NR-1 → `R13`（最高优先，因为它修的是"恒真式"）

**问题**：§13.2 的六个 faithfulness 指标没有配对弃答率 ⇒ 全弃答与复制 fixture 状态列两条路径同时最大化全部六项；
且 2/6 需要 span 原文。**Round-3 范围更正：这一格在 `FIXTURE_001` / `002` / `003` **三份全部**上不可计算**（成因两类，见 `§2.6`）——
`001` / `002` 的成因是"仓内不镜像源文本"（可依法重新取回后补算），`003` 的成因**叠加** rights gate fail-closed（不可补）。

**请求**（二选一，或都做）：
- (a) 在 §13.2 表内为每一项**增加一列同向的弃答 / 覆盖率读数**，并加一条前置条件：
  「六项的合格判定必须以'存在至少 N 个非 `⊥` 断言'为前提；N 在登记时冻结。」
- (b) 把 `SPAN_SUPPORT_RATE` 与 `ENTITY_INSERTION_RATE` 的定义从"span 原文包含"改为
  「**anchor 存在**且**抽取值与该 unit 的 `faithful_paraphrase` 无 token 级增删**」——
  后者只依赖 fixture 内的 paraphrase，**在 `FIXTURE_003` 上可算**。
  若采用 (b)，必须在正文写明「因此这两项**不再**检测对源文本的逐字忠实度，只检测对冻结 paraphrase 的忠实度」。

**成本**：约半天，零新数据。**收益**：把两个恒真式变成可失败判据。

### NR-2 → `R16`

**问题**：`FZ-0` 的 16 字段中至少 4 项（字段 4 / 7 / 8 / 14）不可在无数据接触下填写 ⇒「holdout 行未被读取」事后不可审计；
字段 12 允许 `TBD_AT_FZ1`；`L7` 靠自证。

**请求**：把改写 5 整段纳入 §11（FZ-A / FZ-B 拆分 + `holdout_access_log` + `split_assignment_hash` 生成代码入 FZ-A commit +
禁止 `TBD_AT_FZ1` + `L7` 由日志自动触发）。**并把 `L6` 标为 `UNSATISFIABLE_BY_CURRENT_INSTRUMENTS`**，
使它不再被计入"已建立的防线数"（`F-06` 已自承，但未在 §4 表中标出）。

**成本**：约 1 天，零新数据。**收益**：全项目最便宜的一处修复；把 freeze 从备忘录变成机制。

### NR-3 → `R06`

**问题**：`§10` 遗漏 5 条；`K_pre` 存在选择泄漏；`Ĝ` 与 `⊕` 无判据；`判 I` 未推广。

**请求**（四处，各自独立）：
- (a) §10 增补 `U-9` … `U-13`（本报告 §3.2 已给出可直接粘贴的文本）。
- (b) `判 A` 增补一句：「`K_pre` 必须由**与结果无关的规则**选定（例如：`Candidate Minimal Directed Basis` 的前 4 项，或按 id 排序取前 4）；
  选定规则与被选集合必须与 `FREEZE_RECORD` 同时 durable writeback。」
- (c) 增补一条判据：「若 `⊕` 未在登记时固定，则**不得**对 `Z` 报告任何经 `Net_k` 的效应符号或量级，
  只能报告 `Net_k` 未识别。」
- (d) `Ĝ_k` 增补一条判据，与 `判 B` 平行：「若 `Ĝ ≡ 1`（即 `damp` / `amplify` 支不改变任何更新量）与完整模型等价，
  则拒绝律 A 的**状态依赖**主张，保留其信念中介部分。」**这一条使 `U-9` 从"无判据"变成 `HAS`。**
- (e) 把 `判 I` 的 void 条款形式推广到 `判 A` / `判 J` / `判 M` / `判 N`（各自对应的回溯填答风险 R06 已在 §4.6 / §7.6 / §8.6 写下）。

**成本**：约 1 天，纯文本。**收益**：`U-9` 由 `UNFALSIFIABLE` 升为 `HAS`；`判 A` 堵住选择泄漏。

### NR-4 → `R01`

**问题**：`PPR = BELIEF_ONLY` 无升降条件（与 R17 `F3` 冲突且本侧无判据）；`Satisfaction = DERIVED` 有吸收逃逸口；
`Dedication = KEEP` 与 §9 R3 的内部不一致被"强制声明"而非"二选一"处理；`MERGE` / `REJECT` 从未签发。

**请求**（三处）：
- (a) §4 `PPR` 行替换为改写 4 的双分支登记。
- (b) §4 `Satisfaction` 行增补：「若 `U2` 成立，**则 `Satisfaction` 升为 `DirectedRelationshipState` 的可选坐标**，
  本裁决作废；不得以'增加 `comparison_baseline` 字段'为由维持 `DERIVED`。」
- (c) §7 非主张 3 已说 `KEEP` 不等于 validated；请**再加一条**：「本审计**未使用** `MERGE` 与 `REJECT`；
  若后续无任何构念被这两值签发，则应记录为'**本审计工具未被使用**'，而不是'**本审计未发现问题**'。」

**成本**：约半天，纯文本。**收益**：把一条无判据的承重裁决变成可失败的双分支登记。

### NR-5 → `R14`（因为它的修复计划内含一个已被证伪的指标）

**问题**：`M4` 的产出判据是「逐个删除 construct k → 记录 **`MAPPING_FAILURE` 上升**」，
而 R17 `F1`（本报告已独立确认）证明 `MAPPING_FAILURE` 构造上不可达 ⇒ 消融必然"成功" ⇒ 必然得出"8 维是最小充分基"。

**请求**：把 `M4` 的产出判据从"失败率上升"改为**强制选择判别**（`forced-choice discrimination`）：
> 对每个候选 k，构造 N 组配对单元，使**正确落点是 k 以外的某个构念**；若 mapper 在 k 存在与不存在两种条件下
> **给出相同 verdict**，则记 `k_NO_DISCRIMINATIVE_WORK`。
> `M4` 的成功判据改为「**存在至少一个** `k_NO_DISCRIMINATIVE_WORK`」。
> 若全部 8 项都有判别工作，`M4` 才允许支持"最小充分基"。

**同时**：`M4` 必须与改写 1 的 (b)(c) 分项统计同时报告，因为 catch-all 的使用量是唯一在当前 schema 下可测的删减信号。

**成本**：约 2 天（需构造配对单元），零新数据。**收益**：把一个恒真的消融变成可能为真的消融。

### NR-6 → `R15`（低成本、高回报）

**问题**：`future_leakage_risk` 把「文档内 / 结局泄漏」与「预训练记忆泄漏」合并为一列，互相遮蔽。

**请求**：把该字段拆为两列 `within_document_outcome_leakage` 与 `pretraining_memorization_risk`，
并对 12 份材料重填。**特别要求**：对 `L1-003` / `L3-001` / `L2-003` / `L3-003` / `L3-002` 显式标注
「**该材料上的任何映射覆盖率不得单独作为表示质量证据；必须与同 level 的 T2 材料配对报告**」。

**成本**：约 2 小时。**收益**：使"覆盖率"第一次成为可解释的量。

### NR-7 → `R07`（最便宜的一条）

**问题**：`I4` 是同义反复；`I17` 阈值未定而禁令空转；`I18` 存在量词 + 阈值未指定；`I19` 方向未指定。

**请求**（四处，各一行）：
- `I4`：改为「tag 集合在**连续 N 次 fixture 运行间**不得单调增长；增长即 `ONTOLOGY_CREEP`，无论是否已登记」——
  这样检查对象从"注册表"变成"实际 tag 集合"。
- `I17`：给出 `θ`（Architect 填），并写「未填 `θ` 之前，**任何 coverage 数字都不得出现在对外文本中**」。
- `I18`：改为「**存在**一个状态使 `REFUSE` 为最优，**且**该状态不是全缺失状态」——
  加上"且不是全缺失状态"即堵住平凡满足。
- `I19`：改为「报告置信度的分布尖锐度须**随输入稀疏度单调下降**，且在登记的参照分布之上"——
  指定方向并要求参照分布。

### NR-8 → parent（不是 lane 修复，是排序修复）

**问题**：Wave 1 已经产出了 130 条判据。**Round-3 重算（`§2.9`，逐列求和式已列出）**：`HAS_EXPLICIT_FAILURE_CONDITION` **86** 条、
`NOMINAL_ONLY` **13** 条、`UNFALSIFIABLE*` **31** 条、今天可执行 / 可触发 **42** 条、已执行 **0** 条。
**A03 早先写的「86 条 / 38 条」中形态数正确，可执行数应改为 42**（差异来源见 `§2.9` 的逐项差异表）。
R09 自己写「**当前九条全部处于未执行状态**」，R13 `U-5` 与 manifest `B-5` 共同说明三个 verifier lane 的结果仍未知。

**请求**：在推进任何新一 lane 之前，先执行**一条**：
**R17 `F1` 的"删除三个出口后重跑 Fixture 001"**（`U-F`）。
理由：它是全项目**唯一**一条(a) 可执行、(b) 后果明确、(c) 成本极低（一次三 verifier 盲跑 + 一次 schema 删改）、
(d) 可能真的产生一个负结果的 falsifier。
**如果它跑出 0 次 `MAPPING_FAILURE`（R17 预测的结果），那么本报告 §5 的改写 1 与 NR-1 就从"建议"升级为"必需"，
因为那将证明 catch-all 是唯一的失败通道。**
**如果它跑出 ≥1 次，则 Gate A 第一次有了真实的负结果，而 §15 可以按现状继续用。**
**两种结果都比"再增加一批判据"更有价值。**

---

## §11 引用清单

> **本报告的外部文献指针数为 0。** 以下全部是本次实际逐行读取的**项目内文件**，以 `文件 + 行号 / 章节` 为稳定指针。

### 11.1 `PROJECT_PRIMARY`（canonical / 基础设施）

1. `youling/lhrm@main` = `ee393ca24f9fbf738ac0ed839e99bdc99de6fc3a`（manifest live-rechecked 2026-09-27）
2. `AGENTS.md`（70 行）—— §Validation discipline line 58–63；§Mutation discipline line 65–70
3. `docs/foundation/PARAMETER_CONVERGENCE_V0_1.md`（780 行）—— §2 line 41–86；§4 line 117–241；§5 line 245–287；
   §6 line 291–367；§9 line 461–515；§11 line 550–582；§13 line 614–649；§14 line 653–697；§15 line 701–748
4. `docs/validation/VALIDATION_CORPUS_V0_1.md`（394 行）—— L0-001 line 43–63；L0-002 line 65–84；L0-003 line 86–106；
   L1-001 line 115–134；L1-002 line 136–155；L1-003 line 157–176；L2-001 line 186–206；L2-002 line 208–228；
   L2-003 line 230–250；L3-001 line 261–281；L3-002 line 283–303；L3-003 line 305–324；
   跨层覆盖表 line 328–346；**Fixture 001–003 推荐 line 348–369（⚠ 已与实际冻结的三份不一致，见 `§4.5`；建议 parent 标 `SUPERSEDED_BY_REPAIR`）**；Verification log line 387–394（**line 394「No bulk text ingested into repo」是 `§2.6` 成因 (i) 的直接证据**）
5. `docs/validation/fixtures/FIXTURE_001_L0_001_CARTY_FACT_PACKAGE.md`（79 行）—— line 5（准备者）；line 16（抽取边界）；
   C001–C026 line 40–65；K0–K4 line 69–73；§5 line 77–79
6. `docs/validation/fixtures/FIXTURE_002_L1_003_MAGI_PACKAGE.md`（128 行）—— line 5（准备者）；line 14（不镜像全文）；
   M001–M061 line 42–102；K1–K4 line 108–111；§5 line 115–128
7. `docs/validation/fixtures/FIXTURE_003_L1_001_STORYCORPS_PACKAGE.md`（160 行）—— line 5（准备者）；
   line 19–22（抽取边界 + rights 状态 + `raw_artifact_ref=null` / `representation_artifact_refs=[]` /
   `POINTER_HASH_ONLY` fail-closed）；S001–S042 line 81–122；K0–K3 line 130–135；§7 line 148–154

### 11.2 `WAVE1_PRIMARY`（本次审计的 sibling 报告）

8. `docs/research/overnight-2026-09-27/00_MANIFEST.md`（100 行）—— line 34–37（Wave 1 写回）；line 48–65（lane 表）；
   line 78–90（计数汇总）；line 92–99（blocker `B-1…B-5`）
9. `…/00_CHILD_CONTRACT.md`（64 行）—— §2 硬边界；§3 证据规则；§4 必需字段
10. `…/06_TRANSITION_LAWS.md`（1058 行）—— §1 line 26–70（`RULE-⊥`）；§3 line 102–114；§4.1 line 123–162；
    §4.8 line 243–266（判 A/B/C）；§4.9 line 268–277；§5.8 line 407–428（判 D/E/F）；§6.8 line 533–551（判 G/H/I）；
    §7.8 line 690–711（判 J/K/L）；§8.8 line 854–875（判 M/N/O）；§9 line 889–903；§10 line 906–956（`U-1…U-8`）；
    §11 line 959–981（11 条非主张）
11. `…/17_RED_TEAM_FALSIFIERS.md`（618 行）—— §0 line 15–45（独立性）；`F1` line 108–122；`F2` line 125–152；
    `F3` line 155–177；`F9` line 294–321；`F11` line 342–352；§4 裁定表 line 356–383；§5 line 386–406（`R1–R6`）
12. `…/16_EMPIRICAL_VALIDATION_PROTOCOL.md`（607 行）—— §2 line 35–49（`R16-ID01–11`）；§3.1 line 55–64（六值词表）；
    §3.2 line 66–85；§4 line 115–130（`L1–L8`）；§5 line 134–142（`R16-OC01–05`）；§6 line 146–191；
    §7 line 195–208（`B0–B7`）；§7.1 line 210–223（`R16-UC01–08`）；§10 line 385–400（`F-01…F-12`）；
    §11 line 404–446（`FZ-0` / 16 字段 / 偏离政策 / 签名）；§12 line 450–478（`F-SELF01–21`）；§13 line 482–502（`I1–I17`）
13. `…/02_CONSTRUCT_CONVERGENCE.md`（507 行）—— §1 line 30–40（7 值裁决词表）；§3 line 120–260（13 构念逐条裁决，
    含 `Cohesion` 升级条件 line 248 与 `PPR` line 255–260）；§4 line 264–280（裁决速览表）；§5 line 284–345（文献争议）；
    §6 line 349–366（audit delta，含 #3 内部不一致）；§7 line 370–386（15 条非主张）；§8 line 390–405（`U1–U12`）
14. `…/02b_CONSTRUCT_REDUNDANCY_AUDIT.md`（551 行）—— §2 line 34–56（五 lens / 四值枚举 / `F` lens 天花板）；
    §3 line 59–250（冗余图与边表，含 `E8`）；§9 line 430–470（`MGS-A/B/C`）；§10 line 470–484（12 条非主张）
15. `…/07_PARTIAL_OBSERVABILITY.md`（611 行）—— §1 line 36–55（只读三份冻结件的穷尽 harvest）；§5 line 225–262
    （`I1–I19` + 检查方式 + 现状 + §5.3 便宜清单）；§6 line 286–683（`FM-01…FM-09`）；§6 非主张 10 line 508
16. `…/13_LLM_SKILL_INTERVIEW_LAYER.md`（739 行）—— §13.1 line 547–555；§13.2 line 557–570（六指标）；
    §13.3 line 572–579（四统计量）；§13.4 line 581–585；§13.5 line 587–599；§14 line 603–615（非主张）；§15 line 619–633（`U-1…U-11`）
17. `…/09_DYNAMIC_SYSTEMS_AND_HYSTERESIS.md`（810 行）—— §4 line 130–160（识别性）；§5 line 400–420（迟滞 `NEGATIVE_RESULT` 与检索交代）；
    §7 line 325–376（`O1–O7`）；§9.6 line 750–770（`K1–K9` 双分支表 + 「当前九条全部处于未执行状态」）
18. `…/15_CASEBANK_EXPANSION.md`（346 行）—— §15.0 line 8–19；§15.1 line 21–32（两个隐性缺口：`t0_anchor` / `holdout_policy` 缺失）；
    §15.2 line 34–80（`N01–N20`）；§15.6 line 210–222（`T1–T5`）；§15.7 line 224–241（`A01–A14`）；
    §15.8 line 250–260；§11 line 319（`U1–U12`）
19. `…/14_PAPER_POSITIONING_NOVELTY.md`（412 行）—— §4 line 160–183（`F-1…F-20`）；§5 line 185–239（审稿攻击面，
    含 `A7` line 195、`G2` line 233、**§5.H 元审稿攻击 line 235–239**）；§6 line 241–258（`M0–M9`，含 `M2` / `M4`）；§7 line 260–300（`O-1…O-17`）
20. `…/03_MEASUREMENT_INSTRUMENTS.md`（78264 bytes）—— instrument family 表（D7 `Dedication = NOT_IDENTIFIABLE`；`G9` 架构级 gap）；
    L4 级分类（line 28）；D1–D2 line 115–116；X1–X7 line 138–144
21. `…/01_CURRENTNESS_AND_GAP_MAP.md`（54301 bytes）—— §4.3 line 154–175（`G-01…G-18` 缺口表，含 `G-01` Gate A、`G-02` Gate B、`G-03` Gate C）
22. `…/10_MUTUALITY_POWER_DEPENDENCE.md` / `…/12_COMPUTATIONAL_MODELS_ABM.md` / `…/08b_BELIEF_DECEPTION_KNOWLEDGE.md` /
    `…/05_IDENTIFICATION_AND_STATISTICS.md` / `…/04_DATASET_LANDSCAPE.md` —— 仅用于交叉确认（`R16 §13` 已复述 `R05 I1–I17`；`R16 §6.3` 已复述 `R04 §4 矛盾 9` 四条件交集为空）

### 11.3 `WAVE1_PACKET_PRIMARY`（writeback 完整性取证）

23. `C:\Users\gg828\AppData\Local\Temp\opencode\lanes\R00_packet.md` … `R17_packet.md`（16 份）
24. `…\R17_report_body.md` —— SHA256 = `7F8C9FB4809A821730CE0043F6B097A43550363AAA08145E3A5F506216C058D0`，与
    `docs/research/overnight-2026-09-27/17_RED_TEAM_FALSIFIERS.md` 相同

### 11.4 `VIA_WAVE1`（转录，**未读原文，不承重**）

25. Joel, S., Eastwick, P. W., Allison, C. J., Arriaga, X. B., … & Wolf, S. (2020). *PNAS* 117(32), 19061–19071. DOI `10.1073/pnas.1917036117`（`VIA_WAVE1`：R17 `F2` / R06 `S04` / R16 `S23`）
26. Segal, N., & Fraley, R. C. (2016). *J. Social & Personal Relationships* 33(5), 581–599. DOI `10.1177/0265407515584493`（`VIA_WAVE1`：R17 `F3` / R06）
27. Rusbult, C. E., Martz, J. M., & Agnew, C. R. (1998). *Personal Relationships* 5(4), 357–387. DOI `10.1111/j.1475-6811.1998.tb00177.x`（`VIA_WAVE1`：R01 / R06 `S14`）
28. Lavner, J. A., Bradbury, T. N., & Karney, B. R. (2012). *Journal of Family Psychology* 26(4), 606–616. DOI `10.1037/a0029052`（`VIA_WAVE1`：R06 `S19` / R16 `B2`）
29. Lakatos, I. (1970). *Criticism and the Growth of Knowledge*, pp. 91–196（`VIA_WAVE1`：R17 `F1`）
30. Morin, A. J. S. (2015). `doi:10.1080/10705511.2014.961800`（`VIA_WAVE1`：R02 `F` lens 天花板）
31. Dwork, C., Feldman, V., Hardt, M., Pitassi, T., Reingold, O., & Roth, A. (2015). *Science* 349(6248), 636–638（`VIA_WAVE1`：R16 `L7`）
32. Simmons, J. P., Nelson, L. D., & Simonsohn, U. (2011). *Psychological Science* 22(11), 1359–1366（`VIA_WAVE1`：R16 `L7`）

### 11.5 Round-3 补记：检索口径（`X-14`）与两处**本报告不重复**的上游声明

**`X-14` 适用声明**：Round-2 裁决 `X-14` 要求把**领域级 / 字段级**存在性断言改写为**检索范围断言**。
本报告在 Round-3 中**逐处**改写了下列四类表述，正文相应位置均已带「在本仓已提交材料内 / 在本次实读的 N 处文本之间」等限定：

| 原表述类型 | Round-3 改写后 | 位置 |
|---|---|---|
| 「仓库内不存在 Fixture 003 的原文」 | 「**在本仓已提交的三份 fixture 中**检索不到源文本」 | `§2.6`、`§4.2 H-3`、`§7.1 X-7` |
| 「`MERGE` / `REJECT` 从未被签发」 | 「**在 `02_CONSTRUCT_CONVERGENCE.md` 这一份报告内**从未作为裁决值被签发」 | `§1.6b`、`§7.2 N-A03-3` |
| 「Wave 1 全覆盖，无判据弱化」 | 「**在已比对的 16 / 18 条 lane 上**未发现削弱；`R04` / `R10` 未覆盖」 | `§4.4`、`§7.2 N-A03-7` |
| 「`MAPPING_FAILURE` 构造上不可达」 | 「**在被登记的三份 canonical / 基础设施文件内**没有可达路径」 | `§1.4b`、`§2.6`、`§2.8` |

**两处本报告明确不重复、且建议上游撤回的上游声明**：

1. **`17_RED_TEAM_FALSIFIERS.md:549`：「所有卷期页均经 Crossref API 核验（2026-09-27）」** —— **本报告不重复该声明**，
   并**建议上游撤回**：`H-F24` 已验证 `17` 的 `S1`…`S29` 编号体系**无法从其 §12 引用清单解析**，
   因此"所有"这一总括量词在**该文件自身内部**就无法成立。`17` 不在本报告白名单内，**修法交 `17` 的 owner**。
2. **`H-A5` 的独立性结论（`17` §0 为真）** —— 本报告**不**据此声称 `17` 无暴露面：
   `§0.0 TEMP-1` 登记了**本报告自己的**未声明暴露面，两条并列，不相互抵消。

**Round-3 本报告的检索协议（可复现）**：

| 步骤 | 命令 / 口径 | 结果用途 |
|---|---|---|
| P1 | 逐行 `[regex]::Matches(line, '\bR(0[0-9]|1[0-7])\b')`，**排除自引用 lane** | 本报告不产出 sibling 拓扑数字（那属 `18`）；此步仅用于确认 `§4.4` 的 lane 清单完整性 |
| P2 | 逐 token 计数（`MERGE` / `REJECT` / `SPLIT` / `KEEP` / `DERIVED` / `BELIEF_ONLY` / `OPEN`），**大小写敏感**，`02_CONSTRUCT_CONVERGENCE.md` | `§1.6b` |
| P3 | 逐格重读 `PARAMETER_CONVERGENCE_V0_1.md:41-86`（六条判据）× `:618-649`（§13）× `:679`（§14）× `:707-748`（§15） | `§1.2` / `§1.4b` / `§1.5` / `§1.7` / `§2.3` / `§2.4` |
| P4 | 逐 token 计数 `construct hole` / `ontology hole` / `projection hole` / `UNKNOWN_AS_OF`，`10_MUTUALITY_POWER_DEPENDENCE.md` 与全目录 | `§1.4b` 交叉核对；`18` §2 的新冲突面 |
| P5 | 逐字对照 `VALIDATION_CORPUS_V0_1.md:348-365` ↔ `docs/validation/fixtures/` 三份文件头 | `§4.5` |
| P6 | 逐字读三份 fixture §1 的 licence / rights / mirror 段 | `§2.6` 成因表 (i)(ii) |
| P7 | **0 次联网。** 未打开任何外部来源 ⇒ `§11.4` 的 8 条 `VIA_WAVE1` 全部保持 `NOT_OPENED`，本报告不核实也不否认其内容 | 全报告 |

> **本报告没有做的事（`X-14` 之外的显式声明）**：没有做文献横扫；没有读 / 执行 / 引用 `#20` / `#21` / `#22`；
> 没有跑 Gate A/B/C；没有下载任何受限数据；没有触碰 Eye / Juece；没有写任何 canonical 文件。

---

*本报告由 Research child lane A03 按 `youling/lhrm#30` overnight swarm Work Order 与 `00_CHILD_CONTRACT.md` 生成。
不修改任何 canonical doc；所有改写均为判据草案，最终由 Human / Project Architect 仲裁。*
