# 06_TRANSITION_LAWS — 候选转移律族（RESEARCH_CANDIDATE）

**Status:** `RESEARCH_CANDIDATE` / NOT FROZEN / NOT VALIDATED
**As of:** 2026-09-27
**Lane:** R06（Wave 1）
**Parent:** `youling/lhrm#30@overnight-opencode-exploration-swarm-v1`
**Scope:** 把 `CURRENT_ARCHITECTURE.md` §6 的接口
`X_(t+1) = F(X_t, Action_t, Event_t, Belief_t, Constraint_t, Environment_t)`
落成 5 个**最小、可证伪**的候选转移律族。
**Authority:** 本文不是 canonical。未经 Human / Architect 审阅，不得当作已确立结论、参数、权重、阈值或公式。

---

## ROUND-3 REPAIR PASS（`A3c`，依 `ARCHITECT_ADJUDICATION_V1` / `X-11`）

> ### 裁决 §C 第 5 条（逐字）：**"No transition law is validated/frozen by PR #31/#32."**
> **本文件因此：`NO_LAW_FROZEN / NO_LAW_VALIDATED`。** 下面每条律的状态都是**未冻结**的。

### 0.1 逐律最终状态（Round-3 依 `X-11` 落地；`NONE FROZEN`）

| 律 | 族 | **Round-3 最终状态** | 保留什么 | 阻塞项（诚实措辞） |
|---|---|---|---|---|
| A | `BMR` | **`HOLD_FOR_EVIDENCE`** | **只保留方向性版本**（`∂(E[ΔZ^k]) / ∂ PPR_{i→j} > 0`）作为 research candidate | 判别版本（"信念而非行动驱动状态更新"）需要 relation-level dependence 工具。**原文"现有绝大多数 dyadic 面板只有自陈"是一个未被取样框架支持的 field-wide claim ⇒ 依 `X-14` 降级为检索范围表述**（见 §10 U-1） |
| B | `APES` | **`HOLD_FOR_EVIDENCE`** | 全部（`Std` / `Alt` / `Inv` 三通道的 directional 预测） | **未定位到已验证的关系层 dependence 工具，且经典的相互依赖工具文献未被检索。** ⛔ **不得**写成"结构性不可测" |
| C | `DVA` | **只保留为 `LEVEL_CONDITIONAL_SLOPE` 候选** | `Level → Slope` 交互这一个形状 | **删掉"incremental change 已被击败"的框架**（见 §6）。存活结论是 **level-conditional slope** |
| D | `RGM` | **`HOLD_FOR_EVIDENCE`** | 全部（`Gap` 与 `Movement` 两通道的 directional 预测） | **`Ideal` 来源未核实**（`S31` 为 `CITED_SECONDARY`；见 0.2）。排在 `Ideal` 裁决之后 |
| E | `RT` | **`MODEL_HYPOTHESIS` / `UNTESTABLE_WITH_CURRENT_ORDINARY_WAVE_DATA`** | 分支的形式（`Λ⁺` / `Λ⁻`） | **不是冻结。** 核心主张"`s` 由 dyadic state 决定"**零直接支持**——本文件 §8.4 自己写"无来源直接检验"。需要**事件内顺序** + **双方 + 双方信息源**，普通多波面板给不出 |

**逐条落地位置：** `BMR` → §4 标题块 · `APES` → §5 标题块 · `DVA` → §6 标题块与 §6.3 / §6.4 ·
`RGM` → §7 标题块 · `RT` → §8 标题块。全表另见 §9（跨律对照表的"状态"行）。

### 0.2 承载源状态（`PENDING_EVIDENCE_CHECK (R3-E3)`）—— **标记，不猜测**

sibling child 正在复核以下三个来源。**本轮未打开任何一个。**
**凡依赖它们的陈述一律标 `PENDING_EVIDENCE_CHECK (R3-E3)`；既不主张，也不否认。**

| 承载源 | 是什么 | 依赖它的本文件内容 | Round-3 处置 |
|---|---|---|---|
| **`S04`** = Joel, S., Eastwick, P. W., Allison, C. J., Arriaga, X. B., et al. (2020). *PNAS*, 117(32), 19061–19071. `10.1073/pnas.1917036117` | 43 数据集 / 11,196 对伴侣的预注册协作研究 | §3 总览 A 行与 C 行的"限制证据"；§4.3 第 2 条；§4.4 第 4 行；§6.4 第 6 行；§9 的"最强反证"；§11 非主张 5 | 标 `PENDING_EVIDENCE_CHECK (R3-E3)`。**本文件对该源的任何复述都不得被读作已核实。** |
| **`S19`** = Lavner, J. A., Bradbury, T. N., & Karney, B. R. (2012). *Journal of Family Psychology*, 26(4), 606–616. `10.1037/a0029052` | 婚姻 trajectories / 起点 vs 变化率 | §3 总览 C 行；§6.1–§6.4 的全部依据；§6.3 第 1–2 条；§9 | 标 `PENDING_EVIDENCE_CHECK (R3-E3)`。**Round-3 特别记录：Table 5 的精确数值与正文的逐字措辞都在复核范围内**；本文件不复述任何 Table 5 数字。 |
| **`S31`** = `Ideal` / RGM 的来源（本文件标 `CITED_SECONDARY`，**未读原文**） | 伴侣调整理想偏好以匹配实际伴侣 | §7.4 "Ideal 会随实际对象漂移"；§7.5；§9；§12 裁决请求 2 | 标 `PENDING_EVIDENCE_CHECK (R3-E3)`。**在核实前，`Ideal` 不得进入 `PARAMETER_CONVERGENCE`**（§12 裁决请求 2 已改为 `HOLD`） |

**未被复核、但本文件标 `AGENT_RECALL` / `UNVERIFIED` 的项（Round-3 保持原样）：** S13 的比较水平公式细节（`AGENT_RECALL`）；U-6 的"火花型 / 生长型"区分（`AGENT_RECALL` + `UNVERIFIED`）。**本轮未打开新来源。**

### 0.3 Round-3 落地的裁决清单

| 裁决 | 内容 | 落地位置 |
|---|---|---|
| **`X-11`** | 五条律 `NONE FROZEN`；逐律状态见 0.1 | §0.1、各律标题块、§9、§12 |
| **`X-14`** | field-wide existence claim → search-scope claim | §3、§4.4、§6.4、§10 U-1 / U-2 / U-5、§11 |
| **R-D6** | `06 §8` 两个分支行 `SUPPORTED` → `MODEL_HYPOTHESIS`（来源全是 outcome 层） | §8.4 |
| **R-D7** | "结构性" → "**数据收集方式的限制**" | §10 U-3、§12 裁决请求 5 |
| **R-D12** | `Ded` 与 `Trust` / `AttachmentSecurity` 解耦 = `SUPPORTED（现象存在）/ ILLUSTRATIVE` | §5.4 |
| **R-D13** | `Ideal` 裁决请求（唯一会改 schema 层的建议）→ `HOLD` 待来源核实 | §12 裁决请求 2 |
| **R-D14** | 判 H 与判 N **无法被空结果推翻** → 移入显式不可证伪/前提审计清单 | §2 的 G-2、§6.8、§8.8、§10 新增 `P-A1` / `P-A2` |
| **R-D15** | 功效护栏从"只给律 E"提升为**跨律通用** | §2 的 G-1、§8.7 第 5 条 |
| **R-B16**（`06 §6.4` Lavner 的 *limited evidence* 被标 `DIRECTION_NOT_SUPPORTED（明确反证）` = **标过头**） | 去掉"（明确反证）"后缀，改为无后缀 + 三条限定 | §6.4 第 4 行 |
| **R-L9** / **`X-11`**（`19:210` 把"性别不对称**未检出**"读成"kill criterion 已开火"） | 性别不对称判据 `NOT_TRIGGERED`；"明确不预测" ≠ "已检出不存在" | §4.4 末行、§8.4 末行 |
| **C-P12** | `⊥` 偏算子：**`HOLD / NOT_CANONICAL_NOW`**；U4 仍 `UNKNOWN` | §1 的 U-4、§12 裁决请求 1 |
| **R-D9（跨文件）** | `06 §12` "不要在 R16 之前冻结函数形式"与 `16` 的 freeze 漏洞合谋 | §12 明确不建议的动作 |
| **`X-6` / `C-P10`（镜像侧）** | 删掉"null 赢了"与"被拒绝（初始差异胜）"的措辞 | §6.3 第 1 条、§9 |

---

## 0. 阅读须知（先读这一节）

1. 本文**不给出任何参数、权重、阈值、滞后、尺度或归一化公式**。所有方程都是
   **schematic semantic equation**：其中的函数符号是被命名的**未定函数占位符**，不是建议的函数形式。
2. 本文**没有**声称任何一个律族正确描述人类关系。它们是提交审阅的 `RESEARCH_CANDIDATE`。
   **Round-3 追加（依裁决 §C 第 5 条）：没有一条律被验证或冻结。** 逐律状态见 §0.1。
3. 方向性主张只在**本次实际读到的来源**支持时才写。找不到支持的写
   `DIRECTION_NOT_SUPPORTED`，其含义是"**未确立**"，不是"为假"。
   **Round-3 追加：** `DIRECTION_NOT_SUPPORTED` 的**括号后缀**必须区分两种强度，
   本轮据此改写了三处：
   - **无后缀** = "本次读到的来源未确立"（默认强度）。
   - **（明确反证）** = 来源自己给出了**否定的实质结论**。
   ⚠ **误用记录：** §6.4 曾把来源的 *"limited evidence"* 标成 `DIRECTION_NOT_SUPPORTED（明确反证）`，
   而同一来源在另一侧写着 *"consistent with the incremental change model"* —— **这不是反证**。
   §8.4 曾把两个 **outcome 层**的分支标成 `SUPPORTED`。两处 Round-3 均已改写（见 §6.4 / §8.4）。
4. 凡超出任何文献支持的部分，逐条标 `MODEL_HYPOTHESIS`，并写明"无经验支持主张"。
   **Round-3 追加：** `MODEL_HYPOTHESIS` 有一个更弱的同义档：
   **"零直接支持"** —— 即本文件**自己**写"无来源直接检验"。这比"未确立"更弱，必须显式区分。
5. `⊥`（`UNKNOWN`）在形式化里是**一等值**，不是 0、不是均值、不是"中性"。

---

## 1. 记号约定（本文自定义）

| 符号 | 含义 | 层 / scope |
|---|---|---|
| `D = (i, j)` | 二人组；`i` = source / perceiver / actor，`j` = target | — |
| `τ = (h, t)` | 时间坐标；`h` = history lineage id，`t` = local time index。允许 `τ` 分叉 | history |
| `Δτ` | 两次观测间隔，**允许不等** | episode |
| `k` | 构念族索引（如 `Trust`、`Liking`、`Dedication`） | — |
| `Z^k_{i→j}(τ)` | `i` 对 `j` 的**有向**状态坐标 | directed-edge |
| `A_{i→j}(τ)` | `i` 对 `j` 发出的 Action/Event 流（带时间戳） | Action/Event |
| `Resp_{j→i}(τ)` | `j` 对 `i` 的**可观察**回应行为 | Observation |
| `PPR_{i→j}(τ)` | `i` 认为 `j` 回应了自己（perceived partner responsiveness） | **Belief** |
| `R_i(τ)` | `i` 持有的参考标准 / 期望 / 理想（comparison level、desired、ideal） | **Belief** |
| `M^k_{i→j}(τ)` | `i` **自己**在该构造上、该对象身上的习惯中心（person-specific reversion center） | person × edge |
| `H_i` | `i` 自身历史（对所有 `k`、所有 partner 的既往状态） | person |
| `C_D(τ)` | Constraint / Agreement（boundary rule、协议、制度事实） | Constraint |
| `E_D(τ)` | 与当前 query 相关的那一片 Environment | Environment |
| `d_k(a, b)` | 构念 `k` **自己**的 admissible discrepancy：区间可为差、序数可为秩距、类别可为指示函数 | per-construct |
| `σ`, `ξ`, `ε`, `ν` | 过程噪声，代表状态向量之外的一切 | — |
| `⊥` | `UNKNOWN`：**一等值**。不参与代数运算，不被替换为 0 / 均值 / 中性 | — |
| `Coord_k` | 构念 `k` 的**类型化坐标集**：可以是区间 / 序数状态 / 类别 / `⊥` / 概率分布 | per-construct |

**关于 `d_k` 的重要声明：** 本文的 `d_k` **不是**欧氏距离，**不**跨构念可比较，
**不**假设统一量纲。`‖Gap^k_{i→j}‖` 与 `‖Gap^m_{i→j}‖` 之间**不可比较**。
这是对 `AGENTS.md`「Representation-first invariant」第 4 条的直接执行，
不是待办事项。

**关于 `⊥` 的形式化地位（`MODEL_HYPOTHESIS` MH1）：** 下面所有律族共享同一条 `⊥` 规则。
它是把 `AGENTS.md`「Unknown/missing data must remain explicit」写成数学的**尝试**，
是**架构候选**而非经验发现。Architect 应按表示正确性而非证据强度评判它。

**共享的 `⊥` 规则（记为 RULE-⊥）：**

```text
(1)  证据为 ⊥  ⇒  状态**不发生数值更新**，且**不**被填充为 0 / 均值 / 中性。
(2)  缺乏自身历史 ⇒  M^k_{i→j} = ⊥  ⇒  回中通道在该区间**整条挂起**（不是"回中到 0"）。
(3)  ⊥ 通道挂起 ≠ 整个状态冻结：其余通道照常更新，该区间被标记 PARTIAL_INFORMATION。
(4)  任何下游 readout 遇到 ⊥ 必须显式传播 ⊥，不得静默替换。
```

**已知的形式风险（U4）：** `⊥` 规则使更新算子成为**偏算子**（partial operator）。
偏算子在格上不一定满足结合律或可逆性。若 Gate A 的覆盖推理依赖算子组合，
必须先证其组合性与闭包性，否则 `MAPPING_FAILURE` 的归因会出错。此项 `UNKNOWN`。

> **Round-3 记账（依 `C-P12`，`HOLD / NOT CANONICAL_NOW`）：**
> **U-4 是 `self-audit`，不是发现。** 本文件 §1 的 `MH1` 段落自己写明它是
> *"架构候选而非经验发现"*，且 `U4 = UNKNOWN`；本文件 §12 裁决请求 1 就是在请求 Architect 裁决它。
> ⇒ **本文件不主张 Gate A 的归因推理会出错**，也**不主张**它不会出错。
> **Architect 裁决（C-P12）：`HOLD / NOT_CANONICAL_NOW`** —— 只有当某个实现**确实**
> 为 Gate 归因而组合偏更新算子、且代数风险**确实**变成现实问题时，才考虑加前置条件。
> **前置工程检查项归 R3-H**（"判定当前/拟议的 Gate A 是否实际组合偏更新算子"）。
> **若 R3-H 判 `NOT_APPLICABLE_YET`，则 C-P12 关闭为 `NOT_APPLICABLE_YET`。**
> ⚠ **不得**把本段读成"`⊥` 规则已通过形式审查"——它是**未审查**。

---

## 2. 三个跨律的硬性设计约束 + **两条适用于全部 15 条判据的通用条款**（来自方法学文献，不是本 lane 的偏好）

**C-A（分辨率即识别参数）。** Granger (1969) 指出"apparent instantaneous causality"常常
"arises due to **slowness in recording information**"。Muthén & Asparouhov (2024) 进一步展示：
允许 lag-0 效应的模型能拟合同一批数据并给出**不同的** cross-lagged 结论，并引用
Greenberg & Kessler (1982) 的话——该做法"can be used in practice under a very restricted set of
circumstances"。

> **约束：** 年级面板**在结构上**无法分离"对方行动改变了我的状态"与"我们在同一测量窗口内共同生产一个状态"。
> 任何律族若要主张 partner effect，其测量间隔必须细到能产生 lag-0 与 lag-1 的可区分性。

**C-B（trait–state 混淆）。** Hamaker, Kuiper & Grasman (2015) 证明：当构念稳定性部分源于
trait-like 的时间不变成分时，CLPM 的自回归路径**不足以**控制它，得到的滞后参数
不代表真实的 within-person 关系，并可导致关于因果影响的**存在性、主次与符号**的错误结论。
Lucas (2023) 在模拟中给出更强的表述：标准 lag-1 CLPM 在现实假设下
"very likely to find **spurious** cross-lagged effects when they do not exist"，
并且在效应真实存在时也可能低估它。同时他指出 random-intercept 类模型会**丢掉**
between-person prospective effects。

> **约束：** 必须显式分离 stable between-person 成分与 within-person 成分，
> 并且**必须同时报告**被丢掉的那部分，否则检验有方向性偏误。

**C-C（ordinal / categorical 不能当 continuous 处理）。** Muthén, Asparouhov & Witkiewitz (2024)
指出：把 ordinal 变量当连续处理"can cause strong biases"。

> **约束：** 本项目的 `Coord_k` 允许区间 / 序数 / 类别 / `⊥` / 分布共存（invariant 4）
> **不只是**表示偏好，也是估计正确性的要求。

### 2.1 通用条款 G-1（功效护栏，**跨全部 15 条判据**）

> **Round-3 新增（依 R-D15 / `D-C16`）。** 本文件 Round-1 形态把功效护栏**只**写在 §8.7 第 5 条
> （律 E 专属）。逐字保留该条：*"必须在 protocol 中预先做功效计算，而不是事后解释不显著。"*
>
> **问题：** 护栏只给一条律，其余 14 条判据都会在功效不足时把"检不出"读成"律被拒"。
> **这是本文件最容易被误用的一处**，因为 15 条判据的措辞都是"**拒绝**…"。
>
> **G-1（适用于判 A – 判 O 的全部 15 条）：**
>
> 1. **任何判据的空结果 / 不显著 / CI 含 0 都不构成"该律被拒"。** 除非该设计对**目标效应量**
>    具备**预登记的充分功效**。三者的区别必须在结论里分开：
>    - 功效充分 + 未触发该判据 ⇒ 可按判据行动；
>    - 功效不足 + 未触发 ⇒ **`UNDERPOWERED_INCONCLUSIVE`（不等于拒绝）**；
>    - 触发判据（方向相反 / 等价性成立 / 交互 CI 排除）⇒ 按判据行动。
> 2. **每条判据在预登记时必须同时写下 `min_detectable_effect`**（可借 `16` 的 `R16-OC05` / `R16-UC02`）。
>    没有这一数字的判据，**登记时不成立**。
> 3. **等效性型判据**（判 B / 判 L 明确写"等价性检验 / 等价区间"；判 F 的 *"无实质改善"* 与
>    判 G 的 *"不少于"* 只有在**无差异区间于登记时冻结**的前提下才属这一类）**不受第 1 条的空结果保护**：
>    它们失败需要的是**等价性成立**，不是"没拒绝"。⚠ 反之，它们**也**不能被"不显著"**误判为通过**。
>    ⚠ **Round-3 记账：** 判 F 与判 G 在 Round-1 形态下**只写了"无实质改善" / "不少于"，
>    没有写那个区间**在哪冻结**。⇒ 在补上"等价/无差异区间于登记时冻结"这一句之前，
>    它们**实际上退化成了"无差异则失败"的单向规则**，而单向规则**是可以**被空结果触发的。
>    **本条因此是待补项，不是已完成项。**
> 4. **禁止的推理形态（逐字登记）：** "功效不足 → 结论一致 ⇒ 接受该律族" 与
>    "功效不足 → 结论不一致 ⇒ 拒绝该律族" **都是错的**；正确结论都是 `UNDERPOWERED_INCONCLUSIVE`。

**与 §8.7 第 5 条的关系（不重复、不冲突）：** §8.7 第 5 条是律 E 的**具体**应用
（破坏性事件在多数 dyad 中低频）；**G-1 是它的推广**。§8.7 第 5 条**继续有效**，并被 G-1 覆盖。

### 2.2 通用条款 G-2（哪些判据**不能**被空结果推翻 —— 前提审计，不是律的证伪）

> **Round-3 新增（依 R-D14 / `ADJ2` Q1）。**
>
> **问题：** 15 条判据被混在一个列表里，读者默认每一条都是"如果……就拒绝某律"。
> 但其中**两条**守的是**前提**，而这些前提**没有失败路径**：
> 空结果**不能**推翻它们，因为它们从不被"数据支持"——它们只在**前提被数据否定**时改变结论。
>
> | 判据 | 它实际守的是什么 | 为什么空结果不能推翻它 | Round-3 处置 |
> |---|---|---|---|
> | **判 H**（`06 §6.8`） | 前提"关系状态自然衰减" | 若 `Slope ≈ 0`，这只说明**衰减不明显**；它既不支持也不反对"自然衰减"这个前提。判据的**触发方向**是"`Slope` 符号为正"，而那需要**功效与符号**都足够。 | **移入 §10 的 `P-A1`（前提审计）**，原位留指针 |
> | **判 N**（`06 §8.8`） | 前提"分支由 dyadic state 决定" | `s` 的跨 dyad 变异的分解中，**空结果既可能**是 dyadic-state 部分为 0，**也存**是 person 常数部分为 0。判据的原措辞（"person 常数部分**显著大于**"）本身就是一个**单向比较**，不是双向分解，因此**单向 null 不能触发它**。 | **移入 §10 的 `P-A2`（前提审计）**，原位留指针 |
>
> **G-2（适用于全部 15 条判据）：**
>
> 1. **判据必须先被分类。** 本文件 15 条判据中：
>    **`LAW_FALSIFIER` 13 条**（A / B / C / D / E / F / G / I / J / K / L / M / O）——
>    它们有**空结果失败路径**，受 G-1 保护。
>    **`PREMISE_AUDIT` 2 条**（H / N）—— 它们**没有**空结果失败路径，**移入 §10 的显式清单**。
> 2. **`PREMISE_AUDIT` 不得被计为"已触发的证伪"或"已通过的验证"。** 它们的输出只有三种：
>    `PREMISE_NOT_ASSESSED` / `PREMISE_WEAKENED`（前提被数据削弱）/ `PREMISE_UNDERPOWERED`。
>    **没有** `PREMISE_CONFIRMED` —— 因为不存在能让前提"被确认"的观测。
> 3. **判 M（律 E 的分支证伪）用的是 AND 门**，其中 (ii) 就是 `P-A2` 的内容。
>    **Round-3 修正其记账：** 判 M 的 (ii) 在 `P-A2` 判为 `PREMISE_WEAKENED` 时**仍然成立**
>    （即分支选择器不可由 dyadic state 预测），但**不得**因此宣称"person trait 解释了它"——
>    那需要一个**单独的双向分解检验**，不属于判 M。

### 2.3 三条硬约束的适用范围（Round-3 明确）

`C-A` / `C-B` / `C-C` 适用于**全部** 15 条判据：任何判据若在**违反** `C-A`（分辨率不足）、
`C-B`（trait–state 未分离）、`C-C`（ordinal/categorical 当 continuous）的设计下被评估，
其结果标 `DESIGN_PRECONDITION_VIOLATED`，**不进入** G-1 的三分类。
**这一条在 Round-1 形态下是隐含的**（三条约束写在 §2，15 条判据写在 §4–§8，
中间没有任何交叉引用的句子）——本节把它显式化。

---

## 3. 律族总览

| # | 律族 id | 一句话主张 | **Round-3 状态**（`NONE FROZEN`） | 主要作用层 | 最重要的支持来源 | 最重要的限制证据 |
|---|---|---|---|---|---|---|
| A | `BMR` Belief-Mediated Responsiveness | `i` 的状态只经由 `i` **相信** `j` 做了什么而移动；归属（attribution）决定符号 | **`HOLD_FOR_EVIDENCE`** · 只保留**方向性版本**为 research candidate | Belief → Directed-edge | S01, S02（**方向性版本**） | S04（partner 报告几乎无增量）⚠ `PENDING_EVIDENCE_CHECK (R3-E3)`；**判别版本**的阻塞是 relation-level 工具未定位（§10 U-1） |
| B | `APES` Actor–Partner Exchange with Stock | 满意度–替代品–投入驱动一个**积累的** dependence 存量，dedication 是其下游读出 | **`HOLD_FOR_EVIDENCE`** | Directed-edge + Pair stock | S12（52 研究 / ≈2/3 方差）, S15 | S14（量表把 satisfaction 与 commitment 捆在一起）；**关系层 dependence 工具未定位**（§5 状态块） |
| C | `DVA` Deterioration vs Actualization | 评价读出的下降由两个**可分离**机制产生：起点选择 + 个体内实际化 | **只保留为 `LEVEL_CONDITIONAL_SLOPE` 候选** | Derived readout + History | S19（**level-conditional slope**）⚠ `PENDING_EVIDENCE_CHECK (R3-E3)` | S04（变化大体不可预测）⚠ `PENDING_EVIDENCE_CHECK (R3-E3)`；**起点波次可识别性**（§6.6） |
| D | `RGM` Reference Gap and Movement | 同一对方行为可通过**两条通道**缩小 gap：改变 Actual，或移动 Ideal | **`HOLD_FOR_EVIDENCE`**（待 `Ideal` 来源核实） | Belief(标准) + Agent + Edge | S16, S17, S18 | 自陈 common-method（S29）；**S31 未读原文** ⚠ `PENDING_EVIDENCE_CHECK (R3-E3)` |
| E | `RT` Rhythm and Threshold | 事件级互动有**两条分支**：放大（`Λ⁺`）与抑制/修复（`Λ⁻`）；分支选择由 dyadic state 决定 | **`MODEL_HYPOTHESIS` / `UNTESTABLE_WITH_CURRENT_ORDINARY_WAVE_DATA`** · **不是冻结** | Action ↔ Directed-edge 反馈 | S09, S10, S21 —— **全部 outcome 层**（§8.4 Round-3 改写） | S09 自陈反向因果；**核心主张零直接支持**（§8.4 末行） |

**Round-3 对本表两处措辞的改写（逐条）：**

1. **C 行"最重要的支持来源"：** ~~`S19（起点差异胜出）`~~ → **`S19（level-conditional slope）`**。
   **理由（依 `X-6` / `C-P10` 第 6 条 + `ADJ2`）：** "起点差异胜出"是把一条 *"limited evidence"* 的
   结果读成了判决。见 §6.4 的逐字改写。
2. **E 行"最重要的限制证据"：** ~~`S03 反对性别不对称`~~ → **"性别不对称判据 `NOT_TRIGGERED`"**。
   **理由：** `S03` 是"**未检出**性别差异"，不是"**检出**反对"。见 §8.4 的读法限定。
   `S09` 的 r = .380 vs .392 同理：是**近乎相等**，因此**未检出不对称**，**不是**"检出无不对称"。

**共享机制声明（N-6）：** 律族 A 的事件级证据项 `Net_k(τ,Δτ)` 被 B / C / D / E **刻意共享**。
五族争的不是"事件怎么被编码"，而是"聚合动力学的形状是什么"。

---

## 4. 律族 A — `BMR` Belief-Mediated Responsiveness

> ### Round-3 状态：`HOLD_FOR_EVIDENCE`（依 `X-11`：*"hold directional version as research candidate"*）
> **本律未被冻结，也未被验证。**
>
> | 本律的哪一部分 | Round-3 状态 | 理由 |
> |---|---|---|
> | **方向性版本**：`∂(E[ΔZ^k]) / ∂ PPR_{i→j} > 0` | **`RESEARCH_CANDIDATE`（保留）** | S01 / S02 支持；`X-11` 逐字是 *"hold directional version as research candidate"* —— 注意**不是** "freeze"：依裁决 §C 第 5 条 `NONE FROZEN`，本行是**保留为候选**，不是冻结 |
> | **判别版本**：`∂ΔZ/∂Resp` 在控制 `PPR` 之后的方向（§4.4 第 2 行、判 A） | **`HOLD_FOR_EVIDENCE`** | 需要 relation-level 的 dependence 观测（对方行为的独立观察 + 双方信念的独立报告）。见 §10 U-1 |
> | **归别门控**（`Ω_k` 依赖 `R_i`，判 B） | **`HOLD_FOR_EVIDENCE`** | `Ω_k` 是潜变量（§4.7 第 5 条自陈），与 `NO-ATTRIB` 几乎不可分离 |
>
> **阻塞项的诚实措辞（依 `X-14`）：**
> **"未定位到已验证的关系层 dependence 工具，且经典的相互依赖工具文献未被检索。"**
> ⛔ **不得**写成"结构性不可测"或"结构上不可证伪"——那是 field-wide absence claim，
> 而本 lane 的检索不支持该强度（见 §10 U-1 的 Round-3 改写）。
> ⚠ **特别记录：** Round-1 形态把这条写成了 `16` 的 `F-05`「现有绝大多数 dyadic 面板只有自陈
> → 律 A 与朴素的"行动→状态"律在数学上不可区分」。**该 field-wide 部分已被依 `X-14` 撤回**（`16 F-05` 已同步改写）。
> **"数学上不可区分"那半句本身仍然成立**——它说的是**在只有自陈的设计内**不可区分，是设计内的条件陈述。

> **中文名：** 信念中介的回应性更新律
> **主张（RESEARCH_CANDIDATE）：** `i` 的有向状态**只**经由 `i` 对 `j` 行为的**解释**而移动，
> 而非经由 `j` 实际做了什么。归属（attribution）在**门控符号**与**门控强度**两处起作用。

### 4.1 完整语义方程

对每个构念 `k`、每个方向 `i→j`：

```text
Z^k_{i→j}(τ+Δτ)  =  Θ_k( Z^k_{i→j}(τ),  Net_k(τ,Δτ),  Gate_k(τ,Δτ),  σ_k )

Net_k(τ,Δτ)     =  ⊕_{n ∈ W(τ)}   W_k(n) ⊗ Ω_k( A_{j→i}(n),  R_i(n),  P_i(n) )

Gate_k(τ,Δτ)    =  Ĝ_k(  Net_k(τ,Δτ),  Z^k_{i→j}(τ),  M^k_{i→j} )

Ĝ_k(·)           =  [ damp(·)  ∈ (0,1) ]  ⊕  [ full(·) = 1 ]  ⊕  [ amplify(·) ∈ (1,∞) ]
                         ↑ 符号由 Ω 决定        ↑ 无衰减        ↑ 放大/强化
```

**语义说明（逐符号）：**

- `⊕`：对事件窗口的**集合式**聚合，具体聚合算子未定（求和 / 时间加权 / 名义型计数 / 序数聚合皆可）。
- `W_k(n)`：事件 `n` 对构念 `k` 的**相关性权重**，即"这件事有多大概率与 `k` 有关"。
- `Ω_k(a, r, p)`：**带符号的归属核**。输入是"对方行为 `a`" + "`i` 的参考标准 `r`" +
  "`i` 的情境特征 `p`"，输出是对构念 `k` 的**证据贡献量（可正可负）**。
  这是本律的**判别核心**：同样的 `a`，在不同 `r` 下产生不同符号与不同量级。
- `Ĝ_k`：**门控/学习因子**。它允许"同样的输入在不同状态下产生不同的更新量"。
- `Θ_k`：合成算子。必须满足 `Θ_k(z, ⊥, ·, m, σ) = z`（RULE-⊥ (1)）。
- `P_i(n)`：`i` 在事件 `n` 时刻的情境/自我状态特征（可含疲劳、压力、既有情绪）。
  它允许**同一个人在同一行为面前给出不同归属**。

**RULE-⊥ 在本律的具体化：**

```text
Ω_k(a, r, p) = ⊥                      若  a = ⊥  或  r = ⊥  或  p = ⊥
Θ_k(z, ⊥, g, m, σ) = z                若  Net_k = ⊥   ⇒ 无更新，且不填充
M^k_{i→j} = ⊥                         若  |H_i^k ∩ (i,j)| < κ
                                          ⇒ 回中通道整条挂起（κ 未定，不预设数值）
Net_k(τ,Δτ) = ⊥                       若  窗口 W(τ) 内**没有任何**可归类的 A_{j→i} 事件
                                          ⇒ 注意这与"事件发生但归属不明"是**不同**的两种 ⊥
```

最后一条是刻意的：**"没发生"与"发生了但无法归因"在语义上必须分开**，
因为前者不提供任何信息，后者提供了"有事件但证据不足"这一事实。

### 4.2 变量与 scope

| 变量 | scope | 层 |
|---|---|---|
| `Z^k_{i→j}` | directed-edge（`i→j`） | Directed relationship state |
| `A_{j→i}`, `Resp_{j→i}` | directed-edge + episode | Action/Event + Observation |
| `PPR_{i→j}`, `R_i` | person × edge（belief 索引于对象） | **Belief** |
| `M^k_{i→j}` | person × edge | 回中中心（估计量，非 ontology primitive） |
| `P_i` | person × episode | Agent state / situation |
| `W_k` | construct family | measurement/readout 参数（未定） |
| `C_D`, `E_D` | dyad / environment | 本律未展开；见 §9 的 U5 |
| `h`（history id） | history | 允许 `τ` 分叉 |

### 4.3 必须击败的竞争模型（reduced / null）

1. **`AR-ONLY`（自回归基线）**：`Z(τ+Δτ) = a·Z(τ) + e`，无 partner 通道。
   这是最严格的基线。S03 的 LCM-SR 结果表明，within-person 自回归与 cross-lagged 路径
   **同时**存在且显著，因此"只有自回归"很可能不够——但这是必须被检验的，不是可以假设的。
2. **`NO-PARTNER`（无 partner 效应）**：`Net_k` 的系数全部约束为 0。
   S04 使这个 null **非常强**：跨 43 个数据集，partner 报告的变量在 actor 报告的关系变量之外
   "no predictive effects"。⚠ **`PENDING_EVIDENCE_CHECK (R3-E3)`：S04 的确切主张正在被复核；
   本段复述 S04 的内容一律视为待核。**
   注意 S04 说的是 *partner 的自我报告*，不是 *对方的可观察行为*；
   本律主张的是后者。二者不可混同，但这确实是一个必须认真对待的竞争者。
3. **`ACT-NOT-BELIEF`（行动而非信念驱动）**：直接用 `Resp_{j→i}` 预测 `Z`，
   不经 `PPR` 与 `Ω`。这是本律的**主要对手**。
4. **`NO-ATTRIB`（无归属门控）**：`Ω_k` 不依赖 `R_i`，即 `Ω_k(a, ·, p) ≡ Ω_k(a)`。
   若这一版与完整版拟合相同，归属门控无信息 → 律 A 的核心主张被削弱。
5. **`MEAN-REV-ONLY`（只有回中）**：只有 `M` 通道，无 `Net_k`。
6. **`RANDOM-EFFECTS-ONLY`（只有随机效应）**：只有 dyad 个体间截距与斜率，无任何机制项。

### 4.4 方向 / 形状预测（仅在文献支持处）

| 预测 | 状态 | 依据 |
|---|---|---|
| `∂(E[ΔZ^k]) / ∂ PPR_{i→j}` > 0 | **SUPPORTED** | S01：PPR 在 self-disclosure → intimacy 过程中是 **partial mediator**；S02：96 对伴侣、连续 42 天、双方每日报告，多层次模型中 PPR 部分中介了 self-disclosure 与 partner disclosure 对 intimacy 的作用 |
| `∂(E[ΔZ^k]) / ∂ Resp_{j→i}` **在控制 `PPR_i` 之后** | **`DIRECTION_NOT_SUPPORTED`** | 本 lane 读到的来源中，没有任何一个在 dyad 纵向设计中控制信念而检验"行动→状态"。这恰恰是本律的判别预测，因此它是 `MODEL_HYPOTHESIS`。 |
| `∂(E[ΔZ^k]) / ∂(actor 自身历史)` 的存在性 | **SUPPORTED（个体层）** | S22：个体在行为分布上的**中心趋势**差异"almost perfectly stable"，且单次状态水平本身不可高度预测。这支持"存在一个 person-specific 中心"这个结构，但**不支持**它在关系状态上的具体形式。 |
| partner 回应对**对方**状态的效应大小 vs 对**自己**状态 | **`DIRECTION_NOT_SUPPORTED`** | S04 明确报告 partner 报告几乎无增量；不支持任何方向性断言。 |
| 性别不对称 | **明确不预测** | S03：日间与年间两个尺度上，约束男女路径相等后拟合**未变差**。S09：wife-demand r = .380 vs husband-demand r = .392，量级近乎相同。 |

> **⚠ Round-3 读法限定（依 `X-11` / **R-L9**（`ADJ2`）；适用于本表末行，也适用于 §8.4 的同名行）：**
> **"明确不预测" = 本文件不提出任何性别不对称的方向预测，NOT "已检出不存在性别不对称"。**
> `S03` 的结果是**约束相等后拟合未变差**（`NOT_DETECTED`）；`S09` 的 r = .380 vs .392 是**近乎相等**
> （同样是 `NOT_DETECTED`）。**推论三条：**
> 1. 任何形如 **"当前最佳证据反对性别不对称耦合 ⇒ 律族须重写"** 的括号读法
>    **误述了一个未触发的判据**——本文件从未把性别不对称写成一条 kill criterion，因此**没有**判据开火。
>    逐字保留该误述形态供检索：*"性别不对称的耦合被检出（**当前最佳证据反对**）⇒ 律族须重写"*
>    —— **该形态已判定为 `WRONG-SCOPE`，不成立**（**R-L9** / `X-11`；`19:210` 的原文即该误述形态）。
> 2. **"未检出"不等于"已检出为无"。** 在功效不足时它是 `UNDERPOWERED_INCONCLUSIVE`（§2.1 的 G-1）。
> 3. 性别不对称是**本文件不预测**的量，因此它**不构成对任何律的证据**，无论正反。
>    ⇒ **它不能被计入"律被拒绝"的证据清单。**

### 4.5 值得考虑的非线性 / 阈值 / 迟滞变体

- **饱和 / 习惯化（`damp` 支）**：`Ĝ_k` 随 `|Net_k|` 递减。`MODEL_HYPOTHESIS`。
  S22 确实记载"amount of behavioral variability (and skew and kurtosis)"是稳定的个体差异，
  即**分布形状**本身有稳定个体差异，可作为该支的间接依据，但未直接检验关系状态上的饱和。
- **归属符号翻转（阈值）**：`Ω_k` 的符号在 `Resp` 越过 `i` 自己的期望带时翻转
  （expectancy-violation 风格）。**阈值位置是 person-specific 的**（`R_i`），
  不是全局常数。这一点与 S26 一致：期望本身有害时也可能生效。
- **`M` 的漂移（MH5）**：`M^k_{i→j}(τ)` 自身是慢变潜变量（习惯水平），
  于是回中中心是内生的。`MODEL_HYPOTHESIS`，无直接支持。
- **两通道不对称放大**：`Ĝ` 允许在某些 state 下 `> 1`（放大），
  这与"关系突然升温"以及"报复性升级"共用同一个形式。这同时是律 E 的分支结构的来源。

### 4.6 检验所需数据

| 需求 | 具体要求 | 依据 |
|---|---|---|
| **双方均在场** | 双方都是被试，不是单方报告 | S02：96 对双方每日；S03：双方 |
| **双方均作信息源** | 每人报告：自己的 `Z`、自己的 `PPR`、对**对方** `Z` 的估计 | S29：共同事实的报告一致性远低于直觉（如家庭月收入加权 kappa 报为 0.68，约 40.2% 的伴侣不一致） |
| **事件级观察** | 事件触发式记录（event-contingent），带时间戳，非回忆式 | S01：event-contingent diary，1–2 周；S02：连续 42 天 |
| **测量间隔细到能识别 lag-0 vs lag-1** | 由约束 C-A 强制 | S07, S28 |
| **≥3 wave** | 供 AR 与 cross-lag 分离 | S05, S06 |
| **显式 `⊥` 记录** | 缺失原因需分类（未发生 / 发生但未观察 / 观察但无法归因 / 未询问） | RULE-⊥ (3) |
| **非随机缺失的处理** | partner 未作答不可当 MCAR | S30：partner 缺失会改变样本构成与协变量均值 |

### 4.7 识别风险（什么会让它不可测）

1. **同窗口互为因果。** `Resp` 与 `PPR` 在同一次互动内被共同生产。
   约束 C-A 是唯一出路；年级面板无效。
2. **trait–state 混淆。** 约束 C-B。S06 甚至指出：即使存在真实 cross-lag，
   CLPM 也可能低估它。
3. **共同方法方差。** `Z` 与 `PPR` 若在同一自陈问卷上，`PPR→Z` 路径会被系统性高估。
   这是本律最严重的内生威胁。
4. **partner 效应的基线可能为 0。** 见 §4.3 第 2 条。若 `NO-PARTNER` 赢，本律的判别部分
   （`∂ΔZ/∂Resp | PPR`）**不可测**，因为要条件化的那个量本身不存在。
5. **归属不可直接观测。** `Ω_k` 是**潜变量**。只有把 `PPR` 作为它的 proxy 才能识别，
   于是 §4.3 第 4 条（`NO-ATTRIB`）与本律几乎不可分离 —— 这是本律的结构性弱点。
6. **`κ`（历史长度门槛）本身是超参数**，未经表示覆盖检验前无法设定。
   若为了通过而调 `κ`，就是 p-hacking。

### 4.8 明确的证伪判据（**在看到数据之前**固定）

记 `c = ∂[ Z^k_{i→j}(τ+Δτ) ] / ∂[ PPR_{i→j}(τ) ]`
在控制 `Z^k_{i→j}(τ)` 与 `Resp_{j→i}(τ)` 之后、在 §4.6 所列设计下估计，
对**预先登记的** `k` 集合 `K_pre`（建议 ≤4 项，登记时冻结）。

**判 A（拒绝「信念中介」这一判别主张）：**

> 若对 `|K_pre|` 中**多数** `k`，`c` 的置信区间**包含 0**，
> **且** `∂ΔZ/∂Resp`（**不**条件化于 PPR）的系数**不小于** `|c|`，
> 则**拒绝**「信念、而非行动，驱动状态更新」这一主张。
> 换言之：若一旦控制信念，行动本身仍解释同样多或更多，本律的判别内容即被清空。

**判 B（拒绝「归属门控」）：**

> 若 `NO-ATTRIB`（`Ω_k` 不依赖 `R_i`）与完整模型的**信息准则差异落在预先设定的等价区间内**
> （等价区间在登记时冻结，不由数据反推），则归属门控无信息 → 拒绝 §4.4 中
> "同行为不同符号"的机制主张。

**判 C（空转检验）：**

> 若 `AR-ONLY` 与完整模型无实质差异，则本律退化为自回归 → **拒绝**本律作为独立律族，
> 保留它作为 readout。

### 4.9 什么证据会导致**修正**而非拒绝

- **符号对、效应在联合建模 lag-0 时消失。** → 说明 `Z` 与 `PPR` 是**同一测量**，
  不是两层。**修正方向：** 合并，而非各留一个 primitive。
  这与 R02（冗余审计）直接相关，应主动移交。
- **`c` 稳定但 `Gate` 的 `damp/amplify` 不可识别。** → **修正方向：** 把 `Ĝ` 降级为
  报告性的不确定度，不再作为状态变量的一部分。
- **`c` 只在部分 `k` 上成立。** → **修正方向：** 把本律改为**构念族特异**的律，
  并把"哪些 `k` 属于该族"本身交给 Gate C 决定，而不是由本律假定。
- **partner 缺失非随机且与 `PPR` 相关（S30 情形）。** → **修正方向：** 改为
  报告 `selection_on_observables` 假设，并把它写进 README 级别的限制，而不是当作已解决。

---

## 5. 律族 B — `APES` Actor–Partner Exchange with Stock

> ### Round-3 状态：`HOLD_FOR_EVIDENCE`（依 `X-11`：*"hold pending relation-level dependence measurement"*）
> **本律未被冻结，也未被验证。**
>
> **阻塞项的诚实措辞（依 `X-14`；逐字登记）：**
> **"未定位到已验证的关系层 dependence 工具，且经典的相互依赖工具文献未被检索。"**
>
> ⛔ **不得**写成 **"结构性不可测" / "结构上不可证伪" / "在关系层不存在可测的 dependence"**。
> **理由：** 那是一条 **field-wide absence claim**，而本 lane 的检索框架**不支持**该强度
> （本 lane 未做工具学检索；`X-14` 要求把 field-wide claim 降级为 search-scope claim）。
> **本文件只主张：** 它**本次没有找到**工具，**并且承认自己没有去找过那个文献群**。
>
> **因此本律的两类主张状态不同，不可混读：**
>
> | 本律的哪一部分 | Round-3 状态 | 理由 |
> |---|---|---|
> | **方向性预测**（`∂Ded/∂Std′ > 0`、`∂Ded/∂Alt < 0`、`∂Ded/∂Inv > 0`、`Ded → 解体`） | **`RESEARCH_CANDIDATE`（保留）** | S12（一手 meta 分析，`CITED_PRIMARY`）。这些是**个体层 / 关系层结果变量**上的关联，不需要关系层 dependence **工具** |
> | **"dependence 是一个积累的存量"这一动力学主张** | **`HOLD_FOR_EVIDENCE`** | 它需要一个**关系层 dependence 的独立测量**（不是 `Ded` 的自陈），才能把"存量"与"流量"分开。见 §5.3 第 1 条与 §5.7 第 1 条 |
> | **迟滞支** | **`MODEL_HYPOTHESIS`（无任何经验支持）** | §5.5；§10 U-2。**本 lane 未找到**任何支持人类关系状态存在迟滞的来源 |

> **中文名：** 主—客互依交换（带存量）律
> **主张（RESEARCH_CANDIDATE）：** 满意度、替代品、投入驱动一个**积累的** dependence 存量；
> `Dedication` 是该存量的**下游读出**，而不是同一件事的另一个名字。
> 这一点直接呼应 `PARAMETER_CONVERGENCE_V0_1.md` §4 D7 对 Investment Model 的提醒。

### 5.1 完整语义方程

```text
D^d_{i→j}(τ+Δτ)  =  D^d_{i→j}(τ)
                  +  η_d ⊗ Φ_d(  Net_k(τ,Δτ),  Std^d_i(τ),  Alt^d_i(τ),  Inv^{i→j}(τ) )
                  −  Λ_d ⊗ [ D^d_{i→j}(τ) ⊖ M^d_i ]
                  +  ξ_d(τ)

Ded^{i→j}(τ+Δτ)  =  Ψ( D^d_{i→j}(τ),  Inv^{i→j}(τ),  Alt^d_i(τ),  Std^d_i(τ),  GapB(τ) )
```

**语义说明：**

- `D^d_{i→j}`：`i` 的结果依赖度（`d` 为领域：经济 / 照护 / 居住 / 社会 / 身份）。
  **它是存量**：跨期积累。
- `Net_k(τ,Δτ)`：与律 A **共享**的事件级证据项（S01, S02 支持的 interpersonal process）。
- `Std^d_i(τ)`：`i` 在领域 `d` 上的**比较标准**（belief 层、内生漂移）。S26 支持期望有害的可能。
- `Alt^d_i(τ)`：`i` 认为 `(i,j)` **之外**的替代方案有多好。这是关于**反事实世界**的 belief，
  不是事实。S12 支持 `∂Ded/∂Alt < 0`。
- `Inv^{i→j}(τ)`：已投入（时间、共同历史、连带责任、沉没成本）。
  **这是 pair 级、路径依赖的存量，不是 `i→j` 有向状态。**
- `Λ_d`：耗散。`M^d_i`：`i` 在领域 `d` 上的**习惯依赖水平**（回中中心，person-specific）。
- `GapB(τ)`：只读入、不在本方程中演化；若下游需要，它是派生量。

**RULE-⊥ 在本律的具体化（关键，且与直觉相反）：**

```text
Alt^d_i(τ) = ⊥   ⇒  Φ_d 的 Alt 通道在该区间**单独挂起**
                  ⇒  该区间标记 PARTIAL_ALTERNATIVES_INFORMATION
                  ⇒  D^d 只由 Net_k 通道更新，**不是**"保持原值"、**不是**"替代品=好"

Inv^{i→j}(τ) = ⊥  ⇒  Inv 通道单独挂起（常因观察者根本未记录投入历史）

Std^d_i(τ) = ⊥   ⇒  报酬评价**不能**折算为"高于/低于标准"，
                  只能作为**未折算的原始事件序列**保留（Net_k 仍可用）
```

**为什么必须这样：** S15 表明，在极端情形下 commitment 可以**很高**，因为
替代品差 + 投入高 + 调整后报酬**为负**。若系统把 `⊥` 填成"中性/无投入"，
就会系统性地把非自愿依赖读成低承诺。**这是本律最重要的表示后果。**

### 5.2 变量与 scope

| 变量 | scope | 层 |
|---|---|---|
| `D^d_{i→j}` | directed-edge × domain | Directed relationship state（存量） |
| `Ded^{i→j}` | directed-edge | Directed relationship state（派生读出） |
| `Inv^{i→j}` | **pair**（`i,j` 共享） | Pair state / 投入事实 |
| `Alt^d_i` | person（对 `(i,j)` 而言的外推） | **Belief about a counterfactual world** |
| `Std^d_i` | person × domain | **Belief**（内生漂移） |
| `Net_k` | episode | 共享机制（律 A） |
| `GapB` | dyad | Derived readout |

**注意与 `CURRENT_ARCHITECTURE.md` §4 的一致性：** `D`、`Ded` 建成**有向**；
`Inv` 建成 **pair 级共享**（符合 §4 "shared pair facts separate from directional states"）；
`Alt` 建成 belief（符合 §8 允许 nested simulated worlds）；
`PowerImbalance` 保持 derived（R2），可由 `D` 双向不对称 + `Inv` + `C_D` 派生。

### 5.3 必须击败的竞争模型

1. **`MEMORYLESS`（无存量）**：`D(τ+Δτ) = f(Net, Std, Alt, Inv)`，无累加项、无耗散项。
   S12 所依据的 Investment Model 本身就是**无记忆**的。
2. **`AR-ONLY`**：只有 `D` 的自回归。
3. **`NO-STOCK-DED`（Dedication 是 Satisfaction 的同义词）**：`Ded ≡ g(Satisfaction)`。
   S14 提示这一 null 有相当分量：Investment Model Scale **把 commitment 与 satisfaction 捆在
   同一工具里**。若去掉 `Ded` 后信息不丢，律 B 的独立性主张失败。
4. **`NO-DISSIPATION`**：有累加无 `Λ_d`（无回中）——若拟合不差，耗散项是冗余的。
5. **`NO-ALT` / **`NO-INV**：逐项消融。
6. **`RANDOM-EFFECTS-ONLY`**：只有 dyad 随机截距。

### 5.4 方向 / 形状预测

| 预测 | 状态 | 依据 |
|---|---|---|
| `∂Ded/∂(标准调整后报酬) > 0` | **SUPPORTED** | S12 |
| `∂Ded/∂Alt < 0` | **SUPPORTED** | S12（替代品质量与 commitment 显著负相关） |
| `∂Ded/∂Inv > 0` | **SUPPORTED** | S12（三者共同解释 commitment 方差近三分之二） |
| `Ded → 关系解体` | **SUPPORTED** | S12：commitment 是解体的显著预测因子 |
| 该关系在**关系域**强于非关系域 | **SUPPORTED** | S12：关系域支持"significantly stronger" |
| 该关系随**关系时长**减弱 | **`DIRECTION_NOT_SUPPORTED`（明确反证）** | S12 原文：各关联"vary **minimally** as a function of demographic (e.g., ethnicity) or relational (e.g., **duration**) factors"。**这是一条被最好的一手 meta 分析直接否定的通俗说法，必须写进非主张。** |
| `Ded` 可与 `Trust` / `AttachmentSecurity` 解耦 | **`SUPPORTED（现象存在）/ ILLUSTRATIVE`**（Round-3 改标，依 **R-D12** / `D-C33`） | S15：abusive relationship 中 commitment 仍高 → 高 dedication + 低 trust 可共存。**Round-3 限定：** S15 支持的是**现象存在**（这两个量在某些 dyad 中**可以**不同向），**不是**它们在**统计上可分离**、也**不是**它们**应当**是两个 primitive。⚠ "可共存" ⇒ "可解耦"这一步**不成立**：共存不排除两者由同一潜在因子驱动。**因此本行不得被引用为"`Dedication` 是独立 primitive"的证据**——那是判 E 的任务，判 E 未触发。 |
| 积累是**路径依赖**（迟滞）还是**无记忆** | **`MODEL_HYPOTHESIS`（MH2）** | 本 lane **未找到**任何支持人类关系状态存在迟滞的来源。见 §10 |
| `Inv` 与关系时长可分离 | **SUPPORTED（设计含义）** | S12 的"duration 不调节"意味着二者可分离；因此**不能用时长作为 `Inv` 的工具变量** |

### 5.5 非线性 / 阈值 / 迟滞变体

- **存量饱和**：`η_d` 随 `D` 增大而递减（沉没成本边际效应递减）。
  `MODEL_HYPOTHESIS`。
- **`Alt` 的双重含义**：`Alt` 高但**上升中** vs `Alt` 低但**在恶化**，可能对 `Ded` 影响相反。
  `MODEL_HYPOTHESIS`。
- **阈值/开关**：`Inv` 越过某值后 `Ded` 对 `Net` 的敏感度骤降
  （"我不会走了"效应）。`MODEL_HYPOTHESIS`，无支持。
- **迟滞（可选支）**：把 `Λ_d · [D − M]` 换成带记忆的 Preisach 型算子。
  `MODEL_HYPOTHESIS`，**本 lane 无任何经验支持**（见 §10）。R09 应主导该支。

### 5.6 检验所需数据

- **≥ 4 wave，且间隔不等亦可**。**硬约束：** 存量与流量在 2 个 wave 下**不可识别**。
  这是设计要求，不是偏好。
- **双方 + 双方信息源。** `D` 与 `Ded` 高度依赖内省自陈（S14）。
- **`Inv` 需要历史记录**（关系起点、共同事件时间线），而不仅是当前回忆。
- **`Alt` 允许 `⊥`。** 若问卷强制"从 1 到 9 你有多好的替代品"，就把 `⊥` 消灭了，
  也就消灭了本律最重要的表示后果（S15 情形）。
- **需要能在同一 dyad 内同时出现高 `Ded` + 低 `Trust` 的样本**（例如存在严重冲突的伴侣、
  经济依赖不对称的伴侣），否则第 5.4 行的解耦预测无法检验。

### 5.7 识别风险

1. **存量 / 流量在短面板上不可识别**（最硬）。
2. **同波次 common-method。** `Std`、`Alt`、`Inv`、`Ded` 在同一问卷同一次施测 → 全部互相关。
   S14 的工具本身就是一次施测。
3. **`Ded` 与 satisfaction 的测量纠缠。** 见 §5.3 第 3 条。
4. **反向因果。** 高 `Ded` 会改变什么算作"报酬"，也会降低 `Alt` 的可感知性。
   本 lane 读到的来源**没有检验过**这个方向。`DIRECTION_NOT_SUPPORTED`。
5. **`Inv` 与时长的构造性混淆。** S12 说 duration 不调节，但设计上也意味着
   缺乏外生变化源。
6. **域 `d` 的可分离性是假设。** 也许只有一个 global `D`，分域没有增量信息。
   应逐域做消融而不是假定。

### 5.8 明确的证伪判据（**在看到数据之前**固定）

**判 D（拒绝「存量是独立动态通道」）：**

> 在 ≥4 wave、双方、双方信息源的**人内**设计中，
> `Std`/`Alt`/`Inv` 相对于（i）律 A 的 `Net_k` 通道、
> （ii）**自身先前的** `Ded` 所能解释的**人内增量方差**，
> 在 ≥2 个预登记领域中的 95% CI **包含 0** → **拒绝**「交换/存量是一条独立的动态通道」。
>
> **注意判据的边界：** 被拒绝的是"**额外通道**"，**不是**这些构念的描述性价值。

**判 E（拒绝「Dedication 是独立 primitive」）：**

> 若在已知 `D`、`Inv`、`Alt`、`Std` 之后，`Ded` 不携带任何稳定的额外动态信息
> （等价性检验而非仅"不显著"）→ 依 `PARAMETER_CONVERGENCE_V0_1.md` §4 D7 的逻辑，
> **拒绝 `Dedication` 作为独立 directed primitive**，降级为 derived。
> 这是本 lane 唯一会**建议删除**某个候选 primitive 的判据，须优先提交 R01 / R02。

**判 F（拒绝「迟滞」）—— 若迟滞支被检验：**

> 若含记忆的 Preisach 型算子相对无记忆版本的样本外预测无实质改善 → 拒绝迟滞支，
> 保留 `MEMORYLESS` 形式。

### 5.9 什么证据会导致**修正**而非拒绝

- **`D` 的更新完全由 `Net_k` 决定，`Std`/`Alt`/`Inv` 无增量。** →
  **修正方向：** 把 `D` 降级为 `Net_k` 的**重参数化**，
  并把 `OutcomeDependence` 从动态坐标改判为 derived readout。
  `PARAMETER_CONVERGENCE_V0_1.md` §4 D8 已经把这列为 open question，本 lane 只是把它变成可判定的形式。
- **分域无信息。** → **修正方向：** 去掉 `d` 索引，用单一 `D`，域只保留在 readout 层。
- **`Alt` 恒为 `⊥`（真实场景中人们不知道自己的替代品）。** →
  **修正方向：** 承认该通道**不可用**，把本律降级为只含 `Std` + `Inv` 的二因子形式，
  并在 README 中显式记录该通道永久 `⊥`。**不要**用"替代品=当前关系质量"来填补。
- **`Ded` 与 satisfaction 高度纠缠且无法分离。** → **修正方向：** 拆分测量工具后重测，
  而不是合并 primitive。合并会同时破坏两者的语义。

---

## 6. 律族 C — `DVA` Deterioration vs Actualization

> ### Round-3 状态：**只保留为 `LEVEL_CONDITIONAL_SLOPE` 候选**（依 `X-11`：*"keep only as level-conditional-slope candidate, not 'incremental change defeated'"*）
> **本律未被冻结，也未被验证；也未被拒绝。**
>
> **Round-3 逐字改写的主张行（被取代的原文在上）：**
> 逐字保留：*"评价读出的"下降"由两个**可分离**机制产生：起点选择（level）与段内实际化（slope）。把两者混为一谈是本文献最常见的错误。"* ·
> *"**本律是本次五个律族中最可能先被拒绝的一个。**"*
>
> **取代后的主张（`LEVEL_CONDITIONAL_SLOPE` 候选）：**
> **"在本文件读到的证据中，评价读出的段内变化速率本身依赖起点水平；
> 因此可保留的候选不是"起点 vs 增量"的对立，而是"`Level` 条件化的 `Slope`"这一个交互形状。"**
>
> **三条必须一起读的记账：**
> 1. **判 G 未触发。** 判 G（§6.8）是 DVA 唯一的真证伪判据，它要求"`Level` 独解释的人内变化方差
>    **不少于** `Level + Slope`"。`19` 的 L3 格写的**不是**判 G，是一个注记；
>    **本文件从未报告过判 G 的计算结果** ⇒ **无任何判据开火。**
> 2. **"incremental change 已被击败"被撤回。** 来源说的是 *"limited evidence"*，
>    而**同一来源在另一侧写着** *"consistent with the incremental change model"*。
>    **既不是"击败"，也不是"被反驳"。** 见 §6.4 的逐字改写。
> 3. **S19 正在被复核。** `PENDING_EVIDENCE_CHECK (R3-E3)`。⚠ **本文件不复述 S19 Table 5 的任何数值。**
>
> **对 `16` 的镜像处置（依 `X-6` / `C-P10` 第 6 条）：**
> `16` 的 `B2` rationale 与本节的 §6.3 第 1 条**同源**。`16` 已把 `B2` 改名 `B2_STABLE_LEVEL`、
> 停止使用 `SELECTION_ONLY`、删除"已经击败过一个候选"、并把本节的 Level+RW 模型另立为 `B8_LEVEL_PLUS_RW`。
> **`16` 的 `N8_LEVEL_CONDITIONAL_SLOPE` 就是本节保留的那个候选的模型形式。**

> **中文名：** 起点选择 vs 段内实际化
> **主张（RESEARCH_CANDIDATE，`LEVEL_CONDITIONAL_SLOPE` 版本）：** 见上方 Round-3 主张行。
> **中文名的 Round-3 限定：** 逐字保留"起点选择 vs 段内实际化"，但该二分的**对立**读法已被撤回；
> 保留的是**条件化**读法（`Slope` 依赖 `Level`），不是二选一。

### 6.1 完整语义方程

令 `E^k_{i→j}(τ)` 为**评价类读出**（候选：`Satisfaction`，依
`PARAMETER_CONVERGENCE_V0_1.md` §9 R3 属 `DERIVED / evaluation-state candidate`）：

```text
E^k_{i→j}(τ)  =  Level^k_{i→j}(τ₀)  ⊕  Slope^k_{i→j}(τ)  ⊕  ⊕_{n ≤ τ} ε_n

Level^k_{i→j}(τ₀)  =  g( E^k_{i→j}(τ₀),  AgentState_i(τ₀),  AgentState_j(τ₀),
                          C_D(τ₀),  E_D(τ₀),  Noise^k_{i→j}(τ₀) )

Slope^k_{i→j}(τ)  =  ∫_{τ₀}^{τ} [ Φ_k( X(s),  M_i,  M_j,  H_i )
                            ⊖  Λ_k ⊗ ( E^k(s) ⊖ M_i ) ] ds
```

- `τ₀`：**关系起点**（不是研究起点）。这是本律最关键的定义。
- `X(s)`：律 A / B 提供的状态与事件通道。
- `M_i`：**`i` 自己的**习惯水平，不是人群均值（S22 支持这种 person-specific 中心存在）。
- `Noise^k_{i→j}(τ₀)`：起点测量误差。这一项使 `Level` 与"真起点"分离。

### 6.2 变量与 scope

| 变量 | scope | 层 |
|---|---|---|
| `E` | directed-edge | **Derived readout**（不是 primitive） |
| `Level` | dyad（起点值） | 起点选择（selection） |
| `Slope` | dyad × 时间 | 段内变化 |
| `τ₀` | dyad | **history 坐标**（必须被显式记录，不能事后指定） |
| `M_i` | person | 回中中心（person-specific） |
| `Noise(τ₀)` | dyad | 测量层 |

**本律与架构的一致性：** `E` 走 derived 而非 primitive，符合
`CURRENT_ARCHITECTURE.md` §11「不冻结单一 LoveScore」与 `§6`「label 是 coarse-graining」。

### 6.3 必须击败的竞争模型

1. **`LEVEL_PLUS_RANDOM_WALK`（只起点 + 随机游走，无 slope）**：`E(τ) = Level(τ₀) + 随机游走 + 误差`。
   **这是本律最强、最危险的对手。**
   > **⚠ Round-3 逐字改写（依 `X-6` / `C-P10`）：**
   > **被取代的原文（逐字保留）：** ~~**`SELECTION-ONLY`（只起点，无 slope）** …… **这是本律最强、最危险的对手。** S19 正是它赢了。~~
   > **三处改动：**
   > (a) **名称改为 `LEVEL_PLUS_RANDOM_WALK`（并停止使用 `SELECTION_ONLY`）。**
   >     `SELECTION_ONLY` 这个名字在 `16` 与本节指向**两个不同的模型**（`16` 的旧 `B2` 是**纯随机截距**，
   >     本节的是**随机游走**），是 PR 内最危险的一处同名异义。`16` 已同步改名为
   >     `B2_STABLE_LEVEL`（纯随机截距）与 `B8_LEVEL_PLUS_RW`（本节这个模型）。
   > (b) **删掉"S19 正是它赢了"。** §6.4 的三条限定说明：来源给的是 *"limited evidence"*，
   >     **不是**"它赢了"；且论断对象是 `predictor` 变量，不是 outcome 的人内斜率。
   > (c) **保留"这是本律最强、最危险的对手"这半句。** 它是**关于模型难度**的陈述（不含随机变化的模型
   >     总是更容易拟合），**不依赖**任何来源结论，因此**继续有效**。
   > ⚠ **本条的 null 身份（依 `X-6`）：** 它在 `16` 中是 `B8_LEVEL_PLUS_RW`，
   > **与** `B2_STABLE_LEVEL`（纯随机截距，**没有**随机变化的增量）是**两个不同的 null**。
2. **`DECAY-ONLY`（无条件衰减）**：`Slope = −δ`，与起点无关。
   > **⚠ Round-3 逐字改写（依 **R-B16**，与 §6.4 第 4 行同源）：**
   > **被取代的原文（逐字保留）：** ~~"S19 直接反对。"~~
   > **取代为：** **S19 未确立该方向。** 原文是 *"limited evidence"* + 妻子侧 null，
   > 而**丈夫侧逐字** *"Consistent with the incremental change model"*。
   > ⇒ **既不得**写"直接反对"（那是把证据不足读成证据相反），**也不得**写"已确立"。
   > ⚠ `PENDING_EVIDENCE_CHECK (R3-E3)`（S19 精确措辞与 Table 5 正在复核）。
3. **`AR-ONLY`**。
4. **`COHORT-MODEL`**：`Slope` 由出生队列/时期解释，与个体无关。
5. **`RANDOM-SLOPES-ONLY`**：每个 dyad 一个随机斜率，无任何机制解释。
6. **（Round-3 新增，必需）`N8_LEVEL_CONDITIONAL_SLOPE` 的对照项。** 若要测"slope 依赖起点"这个交互，
   必须有一个**把交互显式写出来**的模型与一个**不写交互**的模型对照。
   在 `16` 中这是 `N8`；在本节，判 G（§6.8）是它的判据形态。
   **没有这一项，本律保留的候选形状就没有参照物。**

### 6.4 方向 / 形状预测

> **⚠ Round-3：本表的承载源 `S19` 与 `S04` 均标 `PENDING_EVIDENCE_CHECK (R3-E3)`。**
> 本表所有依赖它们的行**都是待核复述**；Round-3 **不新增也不否认**任何一行。
> **本轮改写的只有一件事：把两行过强的状态标签降级（见下方批注）。**

| 预测 | 状态 | 依据 |
|---|---|---|
| 下降**集中**在起点低者 | **SUPPORTED** ⚠待核 | S19："declines were isolated to partners who began their marriages with lower levels of satisfaction" |
| 最严重的下降限于**起点最低**的一个子集 | **SUPPORTED** ⚠待核 | S19 同上 |
| `Level → Slope` 存在交互（即斜率本身依赖起点） | **`SUPPORTED（存在性）` = 本节 Round-3 保留的唯一候选** ⚠待核 | S19 的"subset"表述即此含义。**这就是 `LEVEL_CONDITIONAL_SLOPE` 候选的全部内容**；它在 `16` 中对应 `N8_LEVEL_CONDITIONAL_SLOPE` |
| **段内实际化模型**能解释不同满意度组 | ~~**`DIRECTION_NOT_SUPPORTED`（明确反证）**~~ → **Round-3 改标：`DIRECTION_NOT_SUPPORTED`（无后缀 = 本次未确立），并附三条限定** ⚠待核 | S19 原文逐字保留："we found **limited evidence** to support an incremental change model in which differences in patterns of change **in these predictor variables** distinguished among trajectory groups" |
| 中高满意度组的离婚率无差异 | **SUPPORTED** ⚠待核 | S19：引用 Amato & Hohmann-Marriott (2007)，并与"S09 之外"的一致性判断 |
| 人内变化幅度随时间 | **`DIRECTION_NOT_SUPPORTED`** ⚠待核 | S04：**"relationship-quality change was largely unpredictable from any combination of self-report variables"**（43 数据集 / 2,413 工具） |
| 关系状态本身（而非 satisfaction）是否也遵循"起点差异优先" | **`DIRECTION_NOT_SUPPORTED`** ⚠待核 | S19 只测 satisfaction；外推到 `Trust`/`Liking` 等无依据 |

> **⚠ Round-3 对第 4 行的逐字改写与三条限定（依 `X-11` / `C-P10` 第 6 条 / `ADJ2`）：**
>
> **被取代的原文（逐字保留）：** `**DIRECTION_NOT_SUPPORTED**（明确反证）`
> **该标注被删除。** **理由（三条，每条对应来源自身的一句话）：**
> 1. **来源说的是 *"limited evidence"*，不是 explicit refutation。** "有限证据"是**证据弱**，
>    不是**证据反向**。标"明确反证"是把**证据不足**读成了**证据相反**。
> 2. **该论断的对象是 `predictor` 变量。** 逐字：*"differences in patterns of change **in these predictor
>    variables** distinguished among trajectory groups"*。**它讲的是预测变量的变化率，
>    不是 outcome 的人内斜率。** 本文件 §6.4 第 1–3 行讲的才是 outcome 侧的 level-conditional 形状。
>    **两者不是同一个命题，因此不能互相裁决。**
> 3. **同一来源在另一侧写着** *"Consistent with the incremental change model"*。
>    ⇒ **既不得**写"initial differences 击败了 incremental change"，**也不得**写"incremental change 已被反驳"。
>
> **存活下来的结论（唯一）：** **`LEVEL_CONDITIONAL_SLOPE`** ——
> 段内变化的**形状**依赖起点水平。这既不是"起点赢了"，也不是"增量输了"。
> **它是一个交互形状，因此必须有交互模型才能测** ⇒ `16` 的 `N8_LEVEL_CONDITIONAL_SLOPE` 是必需项。
>
> **不主张：** Round-3 **不主张** `LEVEL_CONDITIONAL_SLOPE` 为真。它是**待核的**候选，
> 且其形式依据（S19 的精确措辞与 Table 5）正在被 R3-E3 复核。

### 6.5 非线性 / 阈值 / 迟滞变体

- **`Level` 依赖的平衡点**：设 `Slope = 0` 求解 `Level`，得到"该起点会稳定在哪里"。
  `MODEL_HYPOTHESIS`，本 lane 未找到支持来源。
- **段内转折（inflection）**：`Slope` 本身在时间上非单调（先缓后急）。`MODEL_HYPOTHESIS`。
- **`Level` 阈值**：低于某起点后进入不同机制域。S19 的"subset"表述**弱支持**其存在，
  但未验证阈值形式。`MODEL_HYPOTHESIS`。

### 6.6 检验所需数据

- **必须在关系起点（或其附近）有真实测量。** 若 `τ₀` 是事后回溯指定的，
  整个分解**不可识别**。这是本律最硬的设计要求。
- ≥3 wave；双方；双方信息源；`E` 由双方各自报告。
- `AgentState`、`C_D`、`E_D` 在起点同步测量。
- 必须允许 `E = ⊥`（例如一方不愿回答），并按 §4.7 记录非随机性。

### 6.7 识别风险

1. **起点后置偏差**（最致命）。
2. **`Level` 与 cohort / period 混淆**（横截面设计中）。
3. **范畴错误风险。** 在 derived readout 上检验转移律，检验的是 readout 而非 primitives。
   `AGENTS.md` §6 明确警告过这一点。此风险**必须**在 protocol 中显式写入。
4. **与 S04 的一致性问题。** 若 S04 的一般性结论成立，`Slope` 可能≈0 且不可预测。
5. **`τ₀` 定义随关系类型变化**（dating / cohabitation / marriage 的"起点"不同），
   跨类型合并会引入伪差异。

### 6.8 明确的证伪判据（**在看到数据之前**固定）

**判 G（`LAW_FALSIFIER`；拒绝「段内实际化」通道）：**

> 在**有真实起点波次**的 dyadic panel 中，仅 `Level`（+ per-person 随机截距）
> 解释的人内变化方差，**不少于** `Level + Slope` 合计所解释者，
> 且 `Level → Slope` 交互项的 95% CI **包含 0**
> → **拒绝**律 C 的段内实际化通道。
>
> **Round-3 三条记账（必读）：**
> 1. **判 G 是 DVA 唯一的真证伪判据，且它【未触发】。** `19` 的 L3 格写的**不是**判 G，
>    是一个注记；本文件从未报告判 G 的计算结果。⇒ **不得**写"判 G 已开火"或"已核实证伪"。
> 2. **G-1 适用于判 G。** "CI 包含 0"这一半**不**自动导致拒绝：
>    若对目标交互效应的功效不足，结论是 `UNDERPOWERED_INCONCLUSIVE`（§2.1）。
> 3. **判 G 是"不少于"型（等价性型）判据**：它的失败需要 `Level` 独解释**不少于**合计者，
>    即**等价性成立**。因此它**也不**能被"不显著"**误判为通过**（§2.1 第 3 条）。

**判 H → 已移出本节（Round-3；依 R-D14 / `ADJ2` Q1）：**

> **被取代的原文（逐字保留）：**
> **判 H（空转）：** *"若 `Slope` 的**符号**在预登记的多数 `k` 上为正（即人内实际上升而非下降），
> → **拒绝**"关系状态自然衰减"这一前提，律 C 退化为"起点 + 无变化"。"*
>
> **移出理由：** 判 H 守的是**前提**"关系状态自然衰减"，而这个前提**没有空结果失败路径**：
> `Slope ≈ 0` 既不支持也不反对"自然衰减"这个前提。把它与判 G 并列放在"证伪判据"标题下，
> 会让读者以为"判 H 没开火"是**支持**本律——**那是误读**。
> **新位置：§10 的 `P-A1`（`PREMISE_AUDIT`）。** 它的输出只有
> `PREMISE_NOT_ASSESSED` / `PREMISE_WEAKENED` / `PREMISE_UNDERPOWERED`，**没有** `PREMISE_CONFIRMED`。

**判 I（`LAW_FALSIFIER`；不可识别）：**

> 若起点波次是回溯指定的 → 本律**不可检验**，标 `UNTESTABLE_BY_DESIGN`，
> 不得以任何 post hoc 方式报告 slope 估计。

### 6.9 什么证据会导致**修正**而非拒绝

- **`Level` 主导但 `Level` 可由起点可观测变量预测。** →
  **修正方向（对架构有实质影响）：** LHRM 的贡献重心应转向
  **起点表示质量**（representation at entry），而不是动力学引擎。
  这是一个**合法的、可交付的架构结论**，不是失败。
- **`Slope` 存在但只在少数 `k` 上。** → **修正方向：** 律 C 降为
  "部分构念的起点条件化实际化"，并明确列出哪几个 `k` 属于该子集。
- **`Slope` 不可预测但幅度稳定。** → **修正方向：** 保留 `Slope` 作为**轨迹描述量**
  （downstream readout），不主张任何机制。这是完全可接受的定位。

---

## 7. 律族 D — `RGM` Reference Gap and Movement

> ### Round-3 状态：`HOLD_FOR_EVIDENCE`（依 `X-11`：*"hold pending Ideal-source verification"*）
> **本律未被冻结，也未被验证。**
>
> **阻塞项（逐字登记）：** **`Ideal` 来源未核实。** `S31` 在本文件是 **`CITED_SECONDARY`（未读原文）**，
> 而"伴侣调整理想偏好以匹配实际伴侣"这一条**正是本律的 `Movement` 通道的唯一经验支点**。
> ⇒ 标 **`PENDING_EVIDENCE_CHECK (R3-E3)`**，排在 `Ideal` 裁决之后。
>
> **本律两部分的状态不同：**
>
> | 部分 | Round-3 状态 | 理由 |
> |---|---|---|
> | **`Gap` 通道**（`Actual` 低于 `Desired` → 关系质量更低；两侧都可能有代价） | **`RESEARCH_CANDIDATE`（保留）** | S17（`CITED_PRIMARY`）。这些是**结果变量**上的关联，不依赖 `S31` |
> | **`Movement` 通道**（对方肯定行为 → 移动自己的 `Ideal`） | **`HOLD_FOR_EVIDENCE`** | S16 支持 `Affirm → Movement` 与 `Affirm → 关系功能`；但"`Ideal` 会随实际对象漂移"这条**只**由 `S31` 支撑，而 `S31` 未读原文 |
> | **两通道可分离（MH3）** | **`MODEL_HYPOTHESIS`** | S16 + S31 各自支持一半；**无来源同时检验两半**。Round-1 形态已经这样标，**Round-3 确认不变** |
> | **`Ideal` 成为动态 directed state**（本文件唯一的 schema 层建议） | **`HOLD`** | 见 §12 裁决请求 2（依 **R-D13**）。⚠ **在 `S31` 核实前，`Ideal` 不得进入 `PARAMETER_CONVERGENCE`** |

> **中文名：** 参考落差与自我移动
> **主张（RESEARCH_CANDIDATE）：** `Actual` 与 `Ideal` 的落差是一个通道；
> 对方行为**移动 `i` 自己的理想**是**另一个**通道。文献支持两半各自存在，
> 但**没有**任何我读到的来源在同一个设计中同时识别这两条通道。

### 7.1 完整语义方程

```text
Actual^k_{i→j}(τ)  ∈  Coord_k
Ideal^k_{i→j}(τ)   ∈  Coord_k            # i 对 j 在坐标 k 上的标准
Want^k_i(τ)        ∈  Coord_k            # i 在关系领域 d 上对自己应得水平的标准

Gap^k_{i→j}(τ)  =  d_k( Actual^k_{i→j}(τ),  Ideal^k_{i→j}(τ) )     ∈  ℝ≥0 ∪ {⊥}
GapWant^k(τ)    =  d_k( Actual^k_{i→j}(τ),  Want^k_i(τ) )           ∈  ℝ≥0 ∪ {⊥}

Movement^k_i(τ+Δτ) = Movement^k_i(τ)
                    ⊕ Ψ_k( Affirm^k_{i←j}(τ),  GapWant^k(τ),  Girth^k_i(τ) )

Actual^k_{i→j}(τ+Δτ) = Actual^k_{i→j}(τ) ⊕ Χ_k( Net_k(τ,Δτ) )
```

- `d_k`：**构念自有的** admissible discrepancy（见 §1；**非**欧氏，**不**跨 `k` 可比）。
- `Affirm^k_{i←j}`：**`i` 感知到的** `j` 对 `i` 理想的肯定。
  **注意：S16 的构念是 "perceived partner affirmation"，不是客观肯定。**
- `Girth^k_i`：**可以移动的空间**（人愿意/能够朝自己理想移动多远）。
  `MODEL_HYPOTHESIS`（MH4），**本 lane 未找到支持来源**。

**RULE-⊥ 在本律的具体化：**

```text
d_k(a, b) = ⊥          若  a = ⊥  或  b = ⊥
                          ⇒  落差是 ⊥，**不是** 0，**不是** "没有落差"

GapWant^k(τ) = ⊥       ⇒  Ideal 通道整条挂起
                          （与 Actual 通道可独立挂起：两者可一活一死）

Movement 的累积：若某区间 GapWant = ⊥，该区间 Movement **不更新**，
                  而不是"按 0 更新"
```

**`Gap` 的可比性声明（架构性主张）：**
`Gap^k` 与 `Gap^m`（`k ≠ m`）**不可比较**。任何"落差越大越差"的跨构念比较
都超出本文的形式化范围。

### 7.2 变量与 scope

| 变量 | scope | 层 |
|---|---|---|
| `Actual^k_{i→j}` | directed-edge | Directed relationship state |
| `Ideal^k_{i→j}` | person × edge（**必须随时间演化**） | **Belief（内生的标准）** |
| `Want^k_i` | person × domain | **Belief（内生的标准）** |
| `Gap^k` | directed-edge × construct | 派生比较量（**构念内**可比） |
| `Affirm^k_{i←j}` | person（对 partner 的知觉） | **Belief** |
| `Movement^k_i` | **person**（不是 edge！） | Agent self-process |
| `Girth^k_i` | person | `MODEL_HYPOTHESIS` |

**注意 scope 的一个易错点：** `Movement` 是 **person 层**（朝自己的理想移动），
`Actual` 是 **edge 层**（对特定 `j` 的状态）。二者**不同 scope**，不可混同。
这正是 `CONSTRUCT_SCOPE_DIRECTIONALITY.md` §3 `scope test` 要求的区分。

### 7.3 必须击败的竞争模型

1. **`GAP-ONLY`（只有落差，无移动通道）**：`Ideal` 是固定 agent 属性。
2. **`SELF-IDEAL-ONLY`（移动通道存在但由 self-determination 驱动，无 partner 通道）**。
3. **`ACTUAL-ONLY`（`Ideal` 纯粹是 `Actual` 的单调重命名）** —— 即
   "落差 = `Actual` 与其自身的历史基线之差"。这是很危险的 null：
   若成立，理想/标准层是多余的。
4. **`REPORTING-ARTIFACT`（理想漂移只是回溯性重新校准的测量伪影）**。
   **这是本律最危险的对手**，见 §7.7。
5. **`AR-ONLY` / `RANDOM-EFFECTS-ONLY`**。

### 7.4 方向 / 形状预测

| 预测 | 状态 | 依据 |
|---|---|---|
| `Actual` 低于 `Desired` → 关系质量更低 | **SUPPORTED** | S17："discrepancies between actual and desired closeness are detrimental to relationship satisfaction and well-being"；"low levels of closeness paired with a strong desire for closeness can impair **both** partners' relational well-being" |
| `Actual ≈ Desired` → 关系质量最高 | **SUPPORTED** | S17（引 Frost & Forrester 2013、Frost et al. 2017、Mashek & Sherman 2004） |
| **两侧都可能有代价**（"感觉太近"也有害） | **SUPPORTED（现象存在）** | S17："Feeling too close … may … propel individuals to distance themselves from their partners … likely inducing dissatisfaction on the partner's side" |
| 两侧代价的**相对大小 / 对称性** | **`DIRECTION_NOT_SUPPORTED`** | 未找到任何来源确立两侧对称或不对称。**不得**假设对称。 |
| `Affirm → Movement` 正；`Affirm → 关系功能/稳定性` 正 | **SUPPORTED** | S16：4 项研究；"perceived partner **behavioral** affirmation was strongly associated with quality of couple functioning and stability" |
| `Ideal` 会**随实际对象漂移** | **SUPPORTED（作为现象）** ⚠ `PENDING_EVIDENCE_CHECK (R3-E3)` | S31：伴侣调整理想偏好以匹配实际伴侣；另见年龄/偏好文献中"进入关系者调整了对伴侣的偏好，未进入者下调了预期"的转述（**`CITED_SECONDARY`**）。⚠ **Round-3：`S31` 是本文件 `Movement` 通道的唯一经验支点，而它是 `CITED_SECONDARY`（未读原文）** ⇒ 本行是**待核复述**，`RGM` 因此为 `HOLD_FOR_EVIDENCE`。见 §7 状态块 |
| 期望为正可能有**负面**效果 | **SUPPORTED** | S26："some evidence that positive relationship expectations may sometimes have negative effects" |
| 同一对方行为可经由**两条可分离通道**缩小落差 | **`MODEL_HYPOTHESIS`（MH3）** | S16 + S31 各自支持一半；**无来源同时检验两半** |
| `Girth` 是独立潜变量 | **`MODEL_HYPOTHESIS`（MH4）** | 无支持 |
| 落差**跨构念**可比较 | **明确不预测**（架构性拒绝） | invariant 4 |

### 7.5 非线性 / 阈值 / 迟滞变体

- **双侧非单调（U 型）**：`Gap` 的符号本身可能重要（"低于标准" vs "高于标准"），
  即实际效果可能依赖 `sign(Actual − Ideal)`。S17 支持现象，形状未定。`MODEL_HYPOTHESIS`。
- **`Ideal` 的滞后**：`Ideal` 可能以显著滞后追随 `Actual`，产生**过冲与振荡**。
  这就是本律的迟滞支，且是**唯一**有部分经验支撑的迟滞形态
  （因为 `Ideal` 漂移本身有 S31 支撑）。但振荡形态 `MODEL_HYPOTHESIS`。
- **阈值化的 `Affirm`**：低于某水平时 `Movement` 归零（"不再被看见"）。
  `MODEL_HYPOTHESIS`。
- **不对称移动**：`Actual` 通道通常比 `Ideal` 通道快（改变现实比改变标准容易）。
  `MODEL_HYPOTHESIS`。

### 7.6 检验所需数据

- **双方 + 双方信息源 + 双方各自报告 `Actual` 与 `Ideal`/`Want`。**
  这是本 lane 五个律族中**数据要求最苛刻**的一个：多数关系面板只测满意度，
  不分别测"实际"与"理想"。
- **`Affirm` 的知觉版与客观版都要。** 只测知觉版则 Belief/Observation 分离不可测
  （这正是 R08 的问题，也会使本律的判别内容落空）。
- **对方肯定行为的独立观察或编码**（非自陈）。
- ≥3 wave，供 `Ideal` 的漂移可测。
- `d_k` 必须在每个 `k` 内部良定义；若某 `k` 的 `Coord_k` 只能是无序类别，
  `d_k` 退化为指示函数，落差信息几乎为零 → 该 `k` 应标 `GAP_UNDEFINED` 而非硬算。

### 7.7 识别风险

1. **自利偏差 / common-method（最严重）。** `Actual`、`Ideal`、`Want` 由**同一自陈**
   构造。人在关系好时会把伴侣评得更接近理想，落差被系统性压低。
   S29 表明共同事实的报告一致性远低于直觉。
2. **回溯性重新校准伪影。** 若 `Ideal` 是**现在**测的，`Ideal` 向 `Actual` 的"漂移"
   可能只是**回溯**记忆的产物，而非一个过程。**这是本律的判 G/A 判据的直接对象。**
3. **`Affirm` 与 `Movement` 同为自陈** → 几乎不可解释的正相关。
4. **跨构念可比性被架构性拒绝** → 任何"多落差叠加成风险"的模型都需要
   架构决策，本 lane 不做该决策。
5. **`Coord_k` 类型异质。** 序数/类别坐标的 `d_k` 信息量远低于区间坐标，
   跨 `k` 比较"落差大小"会系统性偏向区间型构念。

### 7.8 明确的证伪判据（**在看到数据之前**固定）

**判 J（拒绝「Ideal 漂移是一个状态过程」）：**

> 在双方信息源、≥3 wave、且已控制 `Actual` 自回归的**人内**设计中，
> 若 `Want` 坐标**不**呈现对 `Actual` 的系统性漂移 → **拒绝** Ideal 漂移通道。
>
> **并行的必要检验：** 若 `Want` 的漂移在**全部**出现在"测量当下"、而在
> **滞后一期的** `Actual` 上不成立 → 判定为 `REPORTING_ARTIFACT`，
> **拒绝**把 `Ideal` 建模为状态；改判为 observation-layer（对过去的信念）。
> 这两个判据必须在登记时一并写下，不得只做前一半。

**判 K（拒绝「partner 肯定通道」）：**

> 若 `Affirm` 对 `Movement` 的效应在控制 `Actual` 后 CI 包含 0
> → **拒绝**律 D 的 `Movement` 通道，只保留 `Gap` 作为读出。

**判 L（拒绝两通道分离，即 MH3）：**

> 若"仅 Actual 通道"与"Actual + Ideal 双通道"模型**不可区分**（等价性检验通过），
> → **拒绝** MH3，即不得声称存在两条可分离通道。

### 7.9 什么证据会导致**修正**而非拒绝

- **理想漂移真实存在但只是回溯伪影。** → **修正方向：** 把 `Ideal` 从 state 移到
  observation / belief-about-past 层。这是一个**实质性的架构修正**，
  应主动提交 Architect。
- **`Gap` 有效但 `Affirm` 不可识别。** → **修正方向：** 保留 `Gap` 读出，
  删除 `Movement` 与 `Girth`；律 D 降为单通道。
- **`Actual ≈ Desired` 的最优只出现在部分 `k`。** → **修正方向：**
  把"落差"限定在 `Coord_k` 为区间型的构念上；序数/类别构念标 `GAP_UNDEFINED`。
  **不要**为了统一而强行构造落差。
- **两侧代价显著不对称。** → **修正方向：** 在 `d_k` 的返回值中保留 `sign`，
  即落差从 `ℝ≥0` 升为 `ℝ`（带符号），并**记录**该修正 —— 这会改变 `ℝ≥0` 的形式化，
  因此必须作为 schema 变更提交，不能就地改。

---

## 8. 律族 E — `RT` Rhythm and Threshold

> ### Round-3 状态：`MODEL_HYPOTHESIS` / `UNTESTABLE_WITH_CURRENT_ORDINARY_WAVE_DATA`（依 `X-11`）
> **本律未被冻结，也未被验证，也未被拒绝。**
>
> **必须先读的三条（本文件最容易被误用的三处）：**
>
> 1. **核心主张零直接支持。** 本律的实质内容是 **"`s` 由 dyadic state 决定"**（§8.4 末行）。
>    **本文件 §8.4 自己写：** *"无来源直接检验。"* ⇒ 这是**零直接支持**，
>    比 `MODEL_HYPOTHESIS` 的通常强度**更弱**（§0 第 4 条的区分档）。
>    **Round-3 确认：** 该行 Round-1 已标 `MODEL_HYPOTHESIS`；Round-3 **不**把它升级，
>    并把它**明确记为零直接支持**（`ADJ2` Q1 第 (b) 点）。
> 2. **两个分支的存在性是 `MODEL_HYPOTHESIS`，不是 `SUPPORTED`。** 见 §8.4 的 Round-3 改写：
>    Round-1 形态把"存在一条独立的正向（趋近）分支"与"存在一条独立的抑制/修复分支"标 `SUPPORTED`，
>    而**所引来源（S21 / S10 / S11）全部是 outcome 层**——它们测的是正性情感、满意度、承诺、
>    投入、关系中心性、视角采择、替代品，**没有**任何一项测"下一次行为被放大/抑制"。
>    **现象在 outcome 层存在 ≠ 分支在行为层存在。**
> 3. **性别不对称的判据【未触发】。** 见 §8.4 末行下的读法限定：
>    *"性别不对称的耦合被检出（**当前最佳证据反对**）⇒ 律族须重写"* 这一读法
>    **误述了一个从未写下的 kill criterion**。
>
> **`UNTESTABLE_WITH_CURRENT_ORDINARY_WAVE_DATA` 的诚实含义（逐字）：**
> **普通多波问卷面板给不出本律需要的东西。** §8.6 列的硬要求是
> **事件触发式记录 + 事件内顺序 + 双方 + 双方信息源 + 编码手册信度**。
> **"普通多波数据不可测"是【数据收集方式的限制】，不是"本律为假"。**
> ⚠ **与 §12 裁决请求 5 的"结构性"改词同源**（依 R-D7）。
> **本文件不主张**本律在**任何**数据上不可测——行政记录、行为观察、ESM 编码都可能给得出。

> **中文名：** 互动节律与分支阈值
> **主张（RESEARCH_CANDIDATE）：** 事件级互动不是"行为更新状态"这么简单；
> 某些行为是**状态依赖的控制信号**，对下一次行为要么**放大**（`Λ⁺`）、
> 要么**抑制/修复**（`Λ⁻`）。同一个事件可以许可其中任一分支。
> **这是本 lane 中唯一以"分支的存在"而非"幅度"作为实质主张的律族。**

### 8.1 完整语义方程

令 `a^n_{i→j}`、`a^n_{j→i}` 为 episode `n` 中**有序**的事件对行为：

```text
A_{i→j}(n+1)  =  ψ( Z^k_{i→j}(n),  Z^k_{j→i}(n),  Env(n),  Con(n) )
              ⊕  γ_up ⊗ Λ⁺( a^n_{j→i},  R_i(n) )
              ⊕  γ_dn ⊗ Λ⁻( a^n_{j→i},  R_i(n) )
              ⊕  ν_n

Λ⁺(a, r)  =  ϑ( a, r )      # ϑ = 该行为相对 i 的参考标准中的"趋近"分量
Λ⁻(a, r)  =  ρ( a, r )      # ρ = "厌离"分量

# 分支选择器（substantive claim）
∂ A_{i→j}(n+1) / ∂ Z^k_{i→j}(n)  =  s(n),      s(n) ∈ { 放大, 中性, 抑制 }
```

**语义说明：**

- `Λ⁺` 与 `Λ⁻` **必须分开**，因为**同一个行为对一个人可能是趋近的、对另一个人是厌离的**
  （reasons 不同于 reasons for actions）。这是关于**有向不对称**的主张。
- `s(n)` 是真正的实质内容：若 `s` 恒等于"中性"，本律退化为
  "行为更新信念/状态"（即律 A），分支结构被证伪。
- `γ_up`、`γ_dn` 是**结构占位符**，不是可调参数。

**RULE-⊥ 在本律的具体化：**

```text
Λ⁺(a, r) = ⊥   若  a = ⊥  或  r = ⊥
Λ⁻(a, r) = ⊥   若  a = ⊥  或  r = ⊥
             ⇒  γ_up ⊗ ⊥  与  γ_dn ⊗ ⊥  **都**从该 episode 的更新中移除
             ⇒  该 episode 仍可贡献 A_{i→j}(n+1) 的 ψ 项（状态/环境/约束）
             ⇒  标记 PARTIAL_EPISODE

s(n) = ⊥      若  使 s 可判定的 dyadic state 任一为 ⊥
             ⇒  **不默认取"中性"**（那会系统性地抹掉所有分支）
```

最后一条是本律最重要的 `⊥` 规则：`s` 不可判定时，**不能**默认"中性"。
默认中性会让"我们不知道"变成"没有放大也没有抑制"，这是一个**方向性偏误**。

### 8.2 变量与 scope

| 变量 | scope | 层 |
|---|---|---|
| `A_{i→j}(n)` | directed-edge × episode | **Action/Event**（不是 state） |
| `s(n)` | dyad × episode | 派生分支变量 |
| `Λ⁺`, `Λ⁻` | directed-edge × episode | Action 分类（对 `i` 的参照系） |
| `Z`（判分支用） | directed-edge | Directed state（被读，不被本律改） |
| `R_i` | person × episode | Belief |
| `Env`, `Con` | environment / constraint | 只读入 |

### 8.3 必须击败的竞争模型

1. **`LINEAR-RECIPROCITY`（单支线性互惠）**：`A(n+1) = α·A(n) + β·a_{j→i}(n) + ν`，
   无分支、无 `s`。
2. **`NO-FEEDBACK`（`s ≡ 中性`）**：只有行为更新状态，无状态反馈到行为。
   这正是**律 A**，因此它是本律最直接的对手。
3. **`SYMMETRIC-ESCALATION`（对称升级）**：隐含"冲突必然变坏"。S03、S09 反对其角色不对称版本。
4. **`AR-ONLY`**。
5. **`TRAIT-MODERATED`（分支由 person 常数而非 dyadic state 决定）**：
   若成立，`s` 应移到 Agent 层，律 E 的核心（状态依赖）被削弱。

### 8.4 方向 / 形状预测

| 预测 | 状态 | 依据 |
|---|---|---|
| demand–withdraw **模式**与关系 / 沟通结果相关 | **SUPPORTED** | S09：总体 r = .360；关系类 r = .423、沟通类 r = .418；人口统计类 r = .239、幸福感类 r = .249；74 研究 / N = 14,255 |
| 模式在临床/高困扰样本中更强 | **SUPPORTED** | S09：distressed r = .413 vs non-distressed r = .345 |
| 两个方向角色的量级**近乎相同** | **SUPPORTED** | S09：wife-demand r = .380；husband-demand r = .392 |
| **存在一条独立的正向（趋近）分支** | ~~**SUPPORTED**~~ → **Round-3 改标：`MODEL_HYPOTHESIS`**（依 **R-D6** / `D-C17`） | S21：分享正面事件带来**超出事件本身的日间正性情感与幸福感**（4 项研究）。⚠ **Round-3 的理由（逐字登记）：来源全部是 outcome 层。** S21 测的是**正性情感与幸福感**，**不是**"下一次行为被放大"。**"分享正面事件 → 更高的当日正性情感"** 与 **"某行为是状态依赖的放大控制信号"** 是**两个不同命题**：前者是 event → outcome 的**跨结果**关联，后者是 event → **next behavior** 的**序列内**分支。**Round-1 形态的 `SUPPORTED` 把前者当成了后者的证据**（`WRONG-SCOPE`）。 |
| **存在一条独立的抑制/修复分支** | ~~**SUPPORTED**~~ → **Round-3 改标：`MODEL_HYPOTHESIS`**（依 **R-D6** / `D-C17`） | S10：accommodation（抑制破坏性回击、改为建设性回应）与更高满意度、承诺、投入、关系中心性、视角采择、较差替代品相关；承诺起中介作用；自我控制促进 accommodation，**当下自我调节耗竭降低** accommodation（4 项研究）。S11 独立确认定义与建设性/破坏性 × 主动/被动四类响应。⚠ **Round-3 的理由（逐字登记）：来源全部是 outcome 层。** 全部关联变量是**满意度、承诺、投入、关系中心性、视角采择、替代品**——**没有一个是"下一次行为"**。⚠ **但是** S11 的四类响应分类**本身**是行为层分类学，**它使 `Λ⁻` 的操作化成为可能**；这是**形式**贡献，不是**存在性**证据。**因此本行标 `MODEL_HYPOTHESIS`，而"S11 提供了可用的分类手册"这一半继续有效。** |
| demand–withdraw **导致**不满（方向） | **`DIRECTION_NOT_SUPPORTED`（来源自陈反向因果可能）** | S09 作者自述："although researchers have generally examined DM/W as a predictor of relational dissatisfaction, it is certainly plausible that dissatisfied partners are motivated to communicate desires for change that lead to DM/W behaviors" |
| 性别不对称（谁在升级 / 谁在撤退） | **明确不预测** | S09 两方向近乎相等；S03 无性别差异 |
| `s` 由 dyadic state（而非 person 常数）决定 | **`MODEL_HYPOTHESIS` / 零直接支持**（Round-3 强化标注） | 无来源直接检验（**本文件 §8.4 自陈**）。S15 给出"高 commitment + 恶劣情形下仍承诺"的**个例提示**，属定性支持，非证据。⚠ **Round-3：这是本律的实质内容，其直接支持为【零】。** 定性个例提示**不构成**对"`s` 由 dyadic state 决定"的检验（个例不能排除 person 常数解释）。 |

> **⚠ Round-3 读法限定（依 `X-11` / **R-L9**（`ADJ2`）；适用于本表倒数第二行）：**
> **"明确不预测" = 本文件不提出性别不对称的方向预测，NOT "已检出不存在性别不对称"。**
> `S09` 的 r = .380 vs .392 是**近乎相等**（`NOT_DETECTED`）；`S03` 是**约束相等后拟合未变差**（`NOT_DETECTED`）。
> **推论三条：**
> 1. 逐字保留的误述形态：*"性别不对称的耦合被检出（**当前最佳证据反对**）⇒ 律族须重写"*
>    —— **判定 `WRONG-SCOPE`，不成立。** 本文件**从未**把性别不对称写成 kill criterion，
>    因此**没有任何判据开火**。"当前最佳证据反对"这个括号把
>    **"本文件不预测"** 读成了 **"证据已检出反向"**。
> 2. **"未检出"不等于"已检出为无"**；功效不足时是 `UNDERPOWERED_INCONCLUSIVE`（§2.1 的 G-1）。
> 3. 性别不对称既**不构成**对律 E 的证据，也**不构成**反证据。**它不能进"律被拒绝"的清单。**
>
> **⚠ 与 §4.4 同名行的关系：** 两条读法限定**内容一致**，**分别就地写出**是为了
> 两处都不需要跳转即可正确阅读（`05` 的"一份 SSOT"纪律在研究文档层不适用：
> 读者常常只读其中一节）。

### 8.5 非线性 / 阈值 / 迟滞变体

- **双稳（bistable）区域**：在同一 `(γ_up, γ_dn, s)` 参数域内，
  相同输入既可收敛到升级、也可收敛到修复，取决于初始状态。
  迟滞形态有**已发表的社交动力学对应物**（S32：social diffusion 的双稳区与显式迟滞，
  `Frontiers in Physics` 6:21），但那是**采纳扩散**，不是 dyadic 关系状态。
  **在人类关系状态上的迟滞 = `MODEL_HYPOTHESIS`（MH2），本 lane 无经验支持。**
- **升级/修复的阈值切换**：`s(n)` 是 dyadic state 的**非连续**函数
  （存在"还没到升级"与"已过升级点"的分界）。`MODEL_HYPOTHESIS`。
- **自我调节耗竭作为衰减器**：`γ_dn` 随 `i` 的自我调节资源下降而下降
  （S10 直接支持"耗竭降低 accommodation"），这把 Agent 层资源接入了事件层动力学。
  这是 S10 支持的**方向**，但把它写成 `γ_dn(state)` 是 `MODEL_HYPOTHESIS`。
- **耦合 love ODE 类比**：S33 的双体耦合 ODE 在不同参数域给出鞍点、互爱/互恨、
  周期轨道。**这些是 `MODEL_HYPOTHESIS` 语料，本 lane 未找到把它们标定到人类
  dyadic 数据的证据。** 列出仅为记录"该形式在文献中已被写出来过"。

### 8.6 检验所需数据

- **事件触发式（event-contingent）记录，含事件内顺序。** 这是律 E 的**硬性**要求：
  没有事件内顺序就无法定义 `a^n_{j→i} → a^{n+1}_{i→j}`。
- **双方 + 双方信息源**（律 E 的分支选择器 `s` 依赖双方状态，故必须双方报告）。
- **分辨率由约束 C-A 强制**（需能区分 lag-0 与 lag-1）。
- **需要包含破坏性事件的 dyad**（否则 `Λ⁻` 分支无变异可估）。
- 需要**包含正面事件的 dyad**（否则 `Λ⁺` 分支无变异可估）—— 这直接对应 S21 的资本化研究。
- **理想/期望的实时记录**（`R_i(n)`）以支持 `Λ⁺`/`Λ⁻` 的符号判定；
  但**回溯填答的 `R_i` 会摧毁符号判定**，这是 S26 强调期望本身会漂移的必然后果。

### 8.7 识别风险

1. **同 episode 内的互为因果。** 一次互动内 `a_{j→i}` 与 `a_{i→j}` 同时发生，
   事件内顺序的可信度是**首要威胁**（时间戳精度 vs 回忆偏差）。
2. **反向因果，且是来源自陈的。** 见 §8.4。
3. **`s` 与 `Z` 的循环性。** `s` 由 `Z` 决定，`Z` 由行为更新；
   同时 `Z` 又是行为的输出。这是**真正的内生循环**，
   C-B 的 trait–state 分离在这里**不足以**解决。
4. **分类学依赖。** `Λ⁺`/`Λ⁻` 的判定若依赖行为编码（人工 SPAFF 类编码），
   编码者对"回应 vs 压制"的判定本身就是理论负载的。
   **必须在登记时公布编码手册与其信度**，否则 `s(n)` 不可复制。
5. **极端事件稀疏。** 升级与破坏性事件在多数 dyad 中低频，
   导致 `Λ⁻` 估计的置信区间极宽 —— 可能是**功效问题**而非**效应不存在**。
   必须在 protocol 中预先做功效计算，而不是事后解释不显著。

### 8.8 明确的证伪判据（**在看到数据之前**固定）

**判 M（`LAW_FALSIFIER`；拒绝分支结构）：**

> 若（i）`Λ⁺`（放大）相对"自身先前行为的自回归 + 对方当前行为"**无 episode 内增量预测力**，
> **且**（ii）升级 vs 修复的分支选择器**不可由 dyadic state 预测**
> （即 `s(n)` 在等价性检验下恒等于"中性"），
> → **拒绝**律 E 的分支结构，只保留"行为经归属更新状态"（律 A）。
> **律 E 降级为律 A 的一个特例并退出独立律族地位。**
>
> **Round-3 三条记账（必读；依 R-D14 / `ADJ2` Q1 第 (d) 点）：**
> 1. **判 M 是 AND 门 ⇒ 它的两个分支的失败条件不同。** (i) 与 (ii) 都可以单独失败；
>    (i) 失败而 (ii) 成立，**不足以**拒绝分支结构。Round-1 形态没有说这一点。
> 2. **G-1 适用于 (i)，但对 (ii) 的保护是反向的。** (i) 是"无增量预测力"型 ⇒ 功效不足时是
>    `UNDERPOWERED_INCONCLUSIVE`，**不是**"分支结构被拒"。(ii) 是**等价性型** ⇒
>    它失败需要**等价性成立**（`s` 确实恒为中性），**不是**"没拒绝"；
>    但它**同样不能**被"不显著"**误判为通过**（§2.1 第 3 条）。
> 3. **判 M 的 (ii) 与 `P-A2`（原判 N）是同一件事的两面。** (ii) 成立（`s` 不可由 dyadic state 预测）
>    **不足以**推出"person trait 解释了它"。**后者需要一个单独的双向分解检验**，
>    而那正是原判 N——它**没有**空结果失败路径，已被移入 §10（见下）。

**判 N → 已移出本节（Round-3；依 R-D14 / `ADJ2` Q1）：**

> **被取代的原文（逐字保留）：**
> **判 N（拒绝状态依赖，改为特质依赖）：** *"若 `s` 的跨 dyad 变异中，**person 常数**部分显著大于 dyadic-state 解释部分
> → **拒绝**"状态依赖分支"这一实质主张；
> **修正方向：** 把相应构念移至 **Agent 层**（person trait），
> 而非保留为 directed relationship state。**这是层级变更，须提交 R01 / R02。**"*
>
> **移出理由（两条）：**
> 1. **它守的是前提，不是律。** 它守的前提是"分支由 dyadic state 决定"，而这个前提
>    **没有空结果失败路径**：`s` 的变异分解中，**空结果既可能**是 dyadic-state 部分为 0，
>    **也可能**是 person 常数部分为 0。
> 2. **它的原措辞是单向比较。** "person 常数部分**显著大于** dyadic-state 解释部分"
>    是一个**单向**比较，不是**双向分解**。⇒ **单向 null 不能触发它**，
>    而"没触发"在"证伪判据"的标题下会被误读成"支持本律"。
>
> **新位置：§10 的 `P-A2`（`PREMISE_AUDIT`）。**
> ⚠ **其"修正方向"（把构念移到 Agent 层）本身是一条真实的架构后果**，
> 但它现在挂在 `P-A2` 的 `PREMISE_WEAKENED` 分支上，**不是**挂在一条不会触发的判据上。

**判 O（`LAW_FALSIFIER`；方向性证伪）：**

> 若在**控制** `Z` 之后，`a^n_{j→i} → a^{n+1}_{i→j}` 的净效应为 0 或与 S09/S10 相反
> → **拒绝**律 E 的全部方向性主张，只保留"状态读出"部分。
> ⚠ **G-1 适用于判 O**：在破坏性事件稀疏的设计中（§8.7 第 5 条），
> 净效应估不出来时结论是 `UNDERPOWERED_INCONCLUSIVE`，**不是**"方向性主张被拒"。

### 8.9 什么证据会导致**修正**而非拒绝

- **分支存在但强度随 dyad 剧烈异质。** → **修正方向：** 承认 dyad-level 随机斜率是必需的，
  并**不要**把分支结构推广为总体规律。
- **`Λ⁺` 与 `Λ⁻` 无法分离（高度共线）。** → **修正方向：** 合并为单一
  "回应性"通道，律 E 退化为律 A 的强化版。**这是最可能的修正路径。**
- **事件内顺序不可信。** → **修正方向：** 只在 episode **之间**（而非之内）定义转移，
  放弃 lag-0 结构，律 E 降级为律 A。**必须如实记录这一降级。**
- **迟滞支无法与随机斜率区分。** → **修正方向：** 删除迟滞支，
  并把"是否可能存在迟滞"登记为 R09 的开放问题（`UNKNOWN`）。

---

## 9. 跨律对照表

| 维度 | A `BMR` | B `APES` | C `DVA` | D `RGM` | E `RT` |
|---|---|---|---|---|---|
| **Round-3 状态（`NONE FROZEN`）** | **`HOLD_FOR_EVIDENCE`**（只保留方向性版本） | **`HOLD_FOR_EVIDENCE`** | **只保留 `LEVEL_CONDITIONAL_SLOPE` 候选** | **`HOLD_FOR_EVIDENCE`**（待 `Ideal` 来源） | **`MODEL_HYPOTHESIS` / `UNTESTABLE_WITH_CURRENT_ORDINARY_WAVE_DATA`** |
| 主要主张层次 | Belief → edge | edge 存量 + pair 存量 | derived readout + history | 标准(Belief) + Agent + edge | Action ↔ edge 反馈 |
| 共享事件机制 | `Net_k`（本体） | `Net_k` | 经由 A/B | `Net_k` → `Actual` | `Λ⁺`/`Λ⁻`（本体） |
| 是否路径依赖 | 否（可含 `M` 漂移，MH5） | **是**（`Inv` + `D` 累加） | 否（`Slope` 积分） | **是**（`Ideal` 漂移，⚠ 待核 S31） | **可选**，无支持（MH2） |
| 显式 `⊥` 的关键作用 | 证据为 `⊥` ⇒ 不更新不填充 | `Alt = ⊥` ⇒ 该通道单独挂起（S15 情形） | 起点波次缺失 ⇒ **不可测** | `d_k` 任一为 `⊥` ⇒ 落差为 `⊥` 非 0 | `s` 不可判定 ⇒ **不得默认中性** |
| 最强支持 | S01, S02 | S12, S15 | S19（⚠ 待核；**支持的是 level-conditional slope**） | S16, S17（⚠ S31 待核） | S09, S10, S21 —— **全部 outcome 层** |
| 最强反证 / 限制 | S04 ⚠待核 | S14（测量纠缠） | S19（*"limited evidence"*，**不是**击败）, S04 ⚠待核 | 自陈 common-method | S09 自陈反向因果；**核心主张零直接支持** |
| 主要识别威胁 | 同窗口互为因果 | 存量/流量不可识别 | 起点后置偏差 | 自利偏差 / 回溯重校 | 事件内顺序不可信 |
| 最小可测设计 | ≥3 wave，日间，双方+双方信息源 | **≥4 wave**，含高 `Ded`+低 `Trust` 的 dyad | **真实起点波次** + ≥3 wave | 双方各自测 `Actual` 与 `Ideal` + `Affirm` 客观版 | 事件触发式 + 事件内顺序 + 编码手册 |
| 概率最高的结局 | 部分 `k` 成立 → 收敛为部分构念的律 | `Ded` 与 `Satisfaction` 难分离 → 降级 | ~~**被拒绝（初始差异胜）**~~ → **Round-3 改写为：被重写为 `LEVEL_CONDITIONAL_SLOPE`**（依 `X-6` / `C-P10` 第 6 条） | `Ideal` 漂移 = 回溯伪影 → 移出 state | 退化为律 A |
| 与架构的关系 | 支持 Belief 独立层 | 支持 `Dedication` 独立（**待 R02 裁决**；且 §5.4 解耦行已降为 `SUPPORTED（现象存在）/ ILLUSTRATIVE`） | 支持"起点表示优先于动力学" | **要求 `Ideal` 成为动态 state** —— ⚠ **`HOLD`，在 `S31` 核实前不得进入 `PARAMETER_CONVERGENCE`** | 支持无 FSM 的连续转移 + 分支（**形式**支持；`Λ⁺`/`Λ⁻` 的**存在性**是 `MODEL_HYPOTHESIS`） |

---

## 10. 「看似合理但**当前不可证伪**」的律（点名比隐藏更有价值）

> 本节是本报告**最诚实**的部分。以下各项在现有可得数据下**无法被检验**。
> 它们被点名，是因为把不可证伪的东西写进架构的风险，大于承认它不可证伪。
>
> **⚠ Round-3：本节新增两个 `PREMISE_AUDIT` 条目（`P-A1` / `P-A2`），并给全节加 `X-14` 的检索范围限定。**
> **分类纪律（依 R-D14 / `ADJ2` Q1，配套 §2.2 的 G-2）：**
> 本节的每一项属于**两类之一**，不可混读：
> - **`UNTESTABLE_WITH_AVAILABLE_DATA`**（U-1 … U-8）：**有**失败路径，只是现有数据给不出。
>   它们**可以**在某一天被数据检验。
> - **`PREMISE_AUDIT`**（`P-A1` / `P-A2`）：守的是**前提**，**没有**空结果失败路径。
>   它们**永远不会**输出 `CONFIRMED`。⚠ **它们"没开火"绝不等于"本律得到支持"。**
>
> **`X-14` 限定（逐字登记）：** 本节每一项的"未找到"都是**本 lane 检索范围内的结论**，
> **不是**关于领域的结论。**逐字保留的过强形态（供检索）：** *"没有任何公开数据集做后者。"*（U-2）
> *"本 lane 在 Human–Human 关系语境中**未找到**任何支持来源"*（U-5）——
> 这两句**本身是合规的检索范围表述**；不合规的是把它们**升格**为"结构性 / 领域性"结论的那一步
> （Round-1 形态在 U-3 走了这一步，本轮已改词，见下）。

**P-A1 前提审计（原判 H，Round-3 移入；依 R-D14）。**

> **逐字保留的原文：** *"若 `Slope` 的**符号**在预登记的多数 `k` 上为正（即人内实际上升而非下降），
> → **拒绝**"关系状态自然衰减"这一前提，律 C 退化为"起点 + 无变化"。"*
> **守的前提：** "关系状态自然衰减"。
> **为什么不能被空结果推翻：** `Slope ≈ 0` 既不支持也不反对这个前提；它只说明**衰减不明显**。
> **输出三态：** `PREMISE_NOT_ASSESSED` / `PREMISE_WEAKENED`（`Slope` 显著为正）/ `PREMISE_UNDERPOWERED`。
> **⛔ 没有 `PREMISE_CONFIRMED`。**
> **⚠ 它不是判 G 的辅助判据**：`P-A1` 与判 G 守的是**不同的**东西
> （前提 vs 段内实际化通道），二者的结论不可互相代替。

**P-A2 前提审计（原判 N，Round-3 移入；依 R-D14）。**

> **逐字保留的原文：** *"若 `s` 的跨 dyad 变异中，**person 常数**部分显著大于 dyadic-state 解释部分
> → **拒绝**"状态依赖分支"这一实质主张；**修正方向：** 把相应构念移至 **Agent 层**（person trait）…"*
> **守的前提：** "分支由 dyadic state 决定"。
> **为什么不能被空结果推翻：** 变异的双向分解中，**空结果既可能**是 dyadic-state 部分为 0，
> **也可能**是 person 常数部分为 0；而原措辞是**单向比较**，单向 null 不触发它。
> **输出三态：** `PREMISE_NOT_ASSESSED` / `PREMISE_WEAKENED`（双向分解显示 dyadic-state 部分不占优）/
> `PREMISE_UNDERPOWERED`。**⛔ 没有 `PREMISE_CONFIRMED`。**
> **⚠ 与判 M 的分工：** 判 M 的 (ii) 只需"`s` 不可由 dyadic state 预测"；
> `P-A2` 的 `PREMISE_WEAKENED` 还需要**正向**指出 person 常数部分占优。
> **前者可以成立而后者不成立**，此时**不得**宣称"person trait 解释了它"。
> **⚠ 架构后果仍在：** `P-A2` 的 `PREMISE_WEAKENED` 分支仍然要求
> "把相应构念移至 Agent 层，须提交 R01 / R02" —— 层级变更请求**不因移位而消失**。

**U-1 信念层与现实层的普遍分离。**
所有"由信念而非行动驱动"的律（含律 A 的判别部分）都要求同时拥有
**对方行为的独立观察** + **双方各自信念的独立报告**。
> **⚠ Round-3 改词（依 `X-14`）：** 逐字保留的原文 *"现有的绝大多数 dyadic 面板**只有自陈**"*
> 是**未被取样框架支持的 field-wide claim**。
> **取代后的表述（检索范围）：** **"在 R06 本次检索到的来源中，未发现同时满足
> '对方行为的独立观察 + 双方各自信念的独立报告'的 dyadic 面板；
> 且 R06 **未**做工具学检索（见 §5 状态块的阻塞项措辞）。"**
> **下面这半句继续有效（它是设计内的条件陈述，不依赖 field-wide claim）：**
> 在只有自陈的设计中，律 A 与一个朴素的"行动→状态"律**在数学上不可区分**。
→ **在只有自陈的设计内不可证伪。** 这是 R08 的核心问题，也会使律 A 的判别内容落空。
⇒ **`BMR` 的状态因此是 `HOLD_FOR_EVIDENCE`（等工具），不是"结构性不可证伪"**（§4 状态块 / §0.1）。

**U-2 人类关系状态中的迟滞 / 路径依赖（MH2）。**
本 lane **未能验证**任何关于人类关系状态存在迟滞的来源。
可验证的只有社交采纳扩散中的迟滞（S32）与无标定的耦合 love ODE（S33）。
检验迟滞需要：足够细的事件级数据 + **在固定当前状态的前提下操纵历史**的实验。
> **⚠ Round-3 降级（依 `X-14`）：** 逐字保留的原文 *"没有任何公开数据集做后者。"*
> **取代后的读法：** **"在 R06 本次检索中，未发现做后者的数据集。"**
> **这是检索范围结论，不是领域存在性结论。** "未找到"与"不存在"之间隔着取样框架。
> ⚠ **保留的一半：** "检验迟滞需要操纵历史的实验"这一**要求**完全正确，
> 且它解释了为什么**普通观测数据不足以支持迟滞主张**。

→ **在本次检索到的数据下不可证伪。** R09 应主导。

**U-3 关系终止作为状态转移。**
> **⚠ Round-3 改词（依 R-D7 / `D-C35`；与 `16 F-04` 同步）：**
> **被取代的原文（逐字保留）：** ~~*"但**自陈面板在结构上无法观测它**"* ~~+~~ ~~"这是本次 lane 发现的**最重要的结构性盲点**。"~~
> **取代措辞：**
> **"自陈面板这一【数据收集方式】无法观测它。"**
> **"这是本次 lane 发现的【最重要的数据收集方式盲点】。"**
> **改词理由：** 终止事件**不是**"关系这个对象在原理上不可观测终止"——
> 行政记录、法律记录、事件记录**可以**观测它。**"结构性"这个词把一个采集方式的缺陷
> 升格成了对象的本体属性**，而 `AGENTS.md` 的 representation-first invariant 要求这两者分开。
> ⚠ **保留的一半（继续有效）：** **"用受访者数据不可证伪"** 这一**设计内**的结论成立，
> 且**"需要行政 / 法律 / 事件记录，而非问卷"** 这条出路完全正确。
> ⚠ **连带改词（`16`）：** `16 F-04` 的 severity 由 `结构性` 改为 **"数据收集方式的限制"**；
> `16 R16-OC03` 引用的"最重要的结构性盲点"这句话随之改读本节。

律族把 `exit`（离开、解散）当作最大的转移，但**自陈面板这一数据收集方式无法观测它**：
离开的人停止了作答。终止事件是**设计性删失（censoring by design）**，
不是可处理的缺失。任何关于"关系最重要的一次转移"的律，
用受访者数据都不可证伪。→ **需要行政 / 法律 / 事件记录，而非问卷。**
这是本次 lane 发现的**最重要的数据收集方式盲点**。

**U-4 环境的直接通道 vs 经由行为的通道（MH6）。**
几乎所有设计中，环境/压力在 person-year 层测量，而行为在 event 层测量。
两条通道**尺度不匹配、不可分离**。→ 用现有设计不可证伪。

**U-5 交换律的负分支 —— 主动反协调体制。**
若存在稳定"合在一起反而更糟"的 dyad 域（协调失败域），
更贴切的不是协调律而是 coordination-game 式的阈值 / 反协调律。
本 lane 在 Human–Human 关系语境中**未找到**任何支持来源；
该语料主要来自协调博弈与计算模型（属 R12 领域）。
→ **点名，不建设。** 标 `MODEL_HYPOTHESIS`。

**U-6 「火花型 vs 生长型」的轨迹分类作为转移律的性质。**
初始轨迹分类（fizzle-out vs. grow）对**转移律的形式**有强约束
（不同初始条件落入不同吸引域），但本 lane 未能在本次核实中找到可靠出处。
→ `AGENT_RECALL` + `UNVERIFIED`。**移交 R11 / R14。** 本报告不使用该区分。

**U-7 `Alternatives` 是否只是"当前关系质量的换名"。**
若 `Alt` 与 `Satisfaction` 是同一潜变量的两个问法，
则律 B 的 `Alt` 通道是循环的。本 lane 读到的任何来源都**未检验**这一点。
→ 律 B 的 `Alt` 通道**在其自身被独立验证之前不可证伪**。

**U-8 `0/1` 强制的"分解即完备"假设。**
律 C 的 level/slope 二分是否穷尽了轨迹信息的其他形态
（例如突变式 step change、季节性）？本 lane 未检验。
→ 若轨迹中存在未被二分覆盖的形态，`Slope` 会被错误地解释为平滑积分。

---

## 11. 明确非主张（Explicit non-claims）

1. **不主张任何参数、权重、阈值、滞后、尺度、归一化被冻结或被建议。**
   所有函数符号（`Ω` `Θ` `Φ` `Ψ` `Χ` `ϑ` `ρ` `γ_up` `γ_dn` `Λ` `Ĝ` `η` `ψ` `g` `⊕` `⊖` `⊗`）
   均为**未定函数的命名占位符**。本文方程是 **schematic semantic equation**，不是可估计模型。
2. **不主张任何律族正确描述人类关系。** 全部是提交审阅的 `RESEARCH_CANDIDATE`。
3. **不主张层归属已被验证。** 各律**假定** `PARAMETER_CONVERGENCE_V0_1.md` 现有层归属
   （B1 PPR 属 Belief；R3 Satisfaction 属 derived；P4/P5 属 pair/institutional；
   R2 Power 属 derived）。若 Gate C 冗余审计合并其中任一项，对应律族**必须重新推导**，
   不能只重新拟合。
4. **`DIRECTION_NOT_SUPPORTED` 的含义是"本次读到的来源未确立"**，
   不是"为假"，也不是"预测为零"。
5. **不主张 partner 效应存在。** S04 是"在现有效度下 partner 效应可能近似为零"的证据。
   `NO-PARTNER` 竞争模型在全文中被当作**真实对手**。
6. **不主张五族互相排斥、联合充分或互相独立。** 律 A 的 `Net_k` 被 B/C/D/E 刻意共享。
7. **不主张任何人群基础概率、规范主张、或"关系应当如何"。**
   本文不做排序、打分或建议。
8. **不主张 `⊥` 规则在经验上更优。** 它是架构要求（MH1）的数学表达，
   "显式 Unknown 处理是否改善预测或覆盖"完全未检验。
9. **不主张本文所述验证计划在成本、可行性或时间上可实现。**
10. **不主张来源数量或模型一致度构成验证。** 每条方向性主张都绑定具体来源 id；
    绑定不到就写 `DIRECTION_NOT_SUPPORTED`。
11. **不引用 LHRM issue #20 / #21 / #22 的任何内容。** 未触碰 Juece #30 / PR #31 / Eye / Juece 仓库。
12. **（Round-3）不主张任何律族被冻结或被验证。** 依裁决 §C 第 5 条：
    **"No transition law is validated/frozen by PR #31/#32."** 逐律状态见 §0.1，全部为未冻结。
13. **（Round-3）不主张 `DVA` 被拒绝。** 它被**重写为** `LEVEL_CONDITIONAL_SLOPE` 候选；
    判 G **未触发**。⚠ "被重写"既不是"被拒"也不是"被接受"。
14. **（Round-3）不主张 `RT` 的两个分支存在。** §8.4 的两行由 `SUPPORTED` 改标 `MODEL_HYPOTHESIS`
    （所引来源**全部是 outcome 层**）。⚠ 同时**不主张**它们不存在——改标只是把"未确立"写对。
15. **（Round-3）不主张性别不对称已被检出为无。** `S09` / `S03` 给的是**未检出**
    （r = .380 vs .392；约束相等后拟合未变差）。见 §4.4 与 §8.4 的读法限定。
16. **（Round-3）不主张 `BMR` / `APES` 结构上不可测。** 阻塞项的措辞是
    **"未定位到已验证的关系层 dependence 工具，且经典的相互依赖工具文献未被检索"** ——
    这是**检索范围**结论（`X-14`）。
17. **（Round-3）不主张 `⊥` 规则的形式风险已解决或已恶化。** U-4 = `UNKNOWN`，
    且它是 `self-audit` 不是发现；Architect 裁决 `HOLD / NOT CANONICAL_NOW`（C-P12）。
18. **（Round-3）不主张判 H 与判 N 是"通过"的。** 它们是 `PREMISE_AUDIT`，
    **没有** `CONFIRMED` 档；"未触发"**不等于**"支持本律"。
19. **（Round-3）不主张 `S04` / `S19` / `S31` 的任何内容成立或不成立。** 三者标
    `PENDING_EVIDENCE_CHECK (R3-E3)`；本轮**未打开**任何一个。
20. **（Round-3）不主张本文件的关系终止盲点是"结构性"的。** 它是**数据收集方式的限制**
    （R-D7 改词；`16 F-04` 同步）。

---

## 12. 建议状态与下一步

> **⚠ Round-3 对本节状态词的改写（依 `X-11` + 裁决 §C 第 5 条）：**
> **逐字保留的原文：** *"**建议状态：`SUCCESS`（`RESEARCH_CANDIDATE`，待 Human / Architect 审阅）。**"*
> **Round-3 限定（保留 `SUCCESS` 这一 lane 级自评，但堵掉它的误读）：**
> **`SUCCESS` 在此只表示"本 lane 完成了它被指派的事"（提出 5 个可证伪候选 + 固定 15 条判据），
> 不表示任何律被验证。** 依裁决 §C 第 5 条与 `X-11`：
> **`NO_LAW_FROZEN / NO_LAW_VALIDATED`。** 逐律状态见 §0.1。
> ⚠ **`SUCCESS` 与 `NO_LAW_FROZEN` 并不矛盾**，但把 `SUCCESS` 读成"律站得住"就是误读 ——
> 本文件 Round-1 形态没有堵这个漏洞。

**给 Architect 的具体裁决请求（按优先级）：**

1. **裁决 MH1（`⊥` 规则）的形式化地位。** 它是架构要求而非经验发现；
   若形式化不可行（例如偏算子的结合性/闭包性在 Gate A 推理中不可用，见 U4），
   需要一个**非算子**的替代表达（例如把状态坐标集合本身扩展为包含 `⊥` 的格，
   而非在算子中处理 `⊥`）。
   > **⚠ Round-3：本项已被 Architect 裁决为 `HOLD / NOT CANONICAL_NOW`（C-P12）。**
   > **前置工程检查归 R3-H**："判定当前/拟议的 Gate A 是否实际组合偏更新算子"。
   > 若 R3-H 判 `NOT_APPLICABLE_YET`，C-P12 关闭为 `NOT_APPLICABLE_YET`。
   > ⇒ **本请求从"待裁决"改为"等 R3-H 的结果"**；U-4 仍是 `UNKNOWN`。
2. ~~**裁决 RGM（律 D）是否要求 `Ideal` 成为动态 directed state。**~~ →
   **`HOLD`（Round-3 改写，依 R-D13 / `D-C34`）。**
   **逐字保留的原文：** *"这是本 lane 提出的**唯一会改变 schema 层级**的建议（S31 + S17 提供支持，
   但 MH3 仍是 `MODEL_HYPOTHESIS`）。它会连带影响 `PARAMETER_CONVERGENCE_V0_1.md` §5。"*
   **Round-3 处置：** **在 `S31` 原文核实之前（`PENDING_EVIDENCE_CHECK (R3-E3)`），不裁决。**
   ⛔ **`Ideal` 不得进入 `PARAMETER_CONVERGENCE`。**
   **理由：** 这是本文件**唯一**会改 schema 层的建议，而它的唯一经验支点（`Ideal` 漂移）
   是一条**未读原文**的 `CITED_SECONDARY` 转述。**把一个未核实来源支撑的层级变更写进 canonical，
   是本文件能犯的最贵的错误。** 核实成本很低（一个来源），因此先核实。
   ⚠ **`D-C34` 的同一顾虑也适用于 `S17` 那一半**：`Gap` 通道有 `S17`（`CITED_PRIMARY`）支撑，
   但 `Gap` 通道**不要求** schema 变更——**要求 schema 变更的是 `Movement` / `Ideal` 那一半**。
3. **裁决 APES（律 B）的判 E。** 若该判据成立，应**删除** `Dedication` 这个候选 primitive。
   本 lane 建议把判 E 优先转交 R02（冗余审计），因为 S14 的工具纠缠使这更像
   测量问题而非动力学问题。
   > **⚠ Round-3 补一条约束：** 判 E **不得**被 §5.4 的解耦行
   > （已降为 `SUPPORTED（现象存在）/ ILLUSTRATIVE`）当作已获支持。
   > **"可共存"不等于"可解耦"**（见 §5.4 的 Round-3 限定）。判 E 未触发。
4. **确认 R09 对 U-2（迟滞）与律 E 迟滞支的主导权。** R06 只登记
   "关系状态迟滞 = `MODEL_HYPOTHESIS`"这一事实，不主张任何形式。
5. **把 U-3（终止的数据收集方式删失）升级为独立议题。**
   本 lane 认为这是**本次最重要的数据收集方式盲点**（Round-3 改词，依 R-D7），
   且它不属于 R06 的可解范围。
   若无人认领，`Case Bank`（R15）与 `Empirical Validation Protocol`（R16）
   应当显式记录该盲点，而不是让"关系会结束"默认为可观测。
6. **（Round-3 新增）裁决 `P-A1` / `P-A2` 的登记形式。** 它们现在是 §10 的显式不可证伪/前提审计条目。
   需裁决：它们是否应进入 `#29` 的 protocol 正文（因为 `#29` 的字段表里目前没有
   "前提审计"这一类输出档）。
7. **（Round-3 新增）认领 `F-SELF19/20/21` 的归属。** **记账更正（R-D11 要求，`A3c` 复核）：**
   `F-SELF01`–`F-SELF18` 不是本 lane 的产物——它们逐条对应 `05 §6` 的 `SD` 项与
   `R17 F1` / `PROJECT` P03（**不是**全部来自 `SD1–SD20`：`F-SELF01` = R17 F1、
   `F-SELF02` = P03 §6、`F-SELF15` 含 P03 §9）。
   `F-SELF19` / `20` / `21` 同样**不是**本 lane（`R06`）的产物：**它们是 `16`（R16）的独立观察**，
   其中 `F-SELF20` 的防线列答复逐字是 **"无。"**（英文写法 `None.`；**该英文写法不是原文**）。
   ⇒ **`F-SELF19/20/21` 应计为 `16` 的首要交付物**（`16 §12` / `16 §17` 已同步改标为
   `JOIN LANE` 的首要交付物）。本 lane **不**认领这三条。

**明确不建议的动作：** 不要在 `FZ-1` 之前冻结任何转移律的函数形式（原措辞 *"不要在 R16 之前冻结任何转移律的函数形式"*，**仍然有效**；Round-3 只把它的时间锚从 "R16" 改成 `FZ-1`）；
不要在 R02 完成之前把 `Dedication` 视为已收敛。
> **⚠ Round-3 交叉注记（与 `16` 的 freeze 漏洞相关；依 R-D9）：**
> 逐字保留的原文 *"不要在 R16 之前冻结任何转移律的函数形式"* **方向正确，但与 `16` 的
> freeze 漏洞**同向**：`16` 的 `FREEZE_RECORD` 字段 12 允许写 `TBD_AT_FZ1`，
> 于是"不冻结函数形式"会被读成"主 estimand 也可以晚定"。
> **Round-3 的区分（`16 §11.2` 已落地）：**
> **"不冻结函数形式"与"冻结 estimand"是两件事。前者可以晚，后者不能。**
> ⇒ **本文件的建议已据此改写（不是新增一条禁令，是把原句的时间锚从 "R16" 换成 `FZ-1`）：**
> **不要在 `FZ-1` 之前冻结任何转移律的函数形式（`16` 要求 `FZ-1` 在看 holdout 之前）；
> 但 `primary_estimand` 必须在 `FZ-1` 冻结，与函数形式是否已裁决无关。**
> ⚠ **"不要在 R16 之前冻结函数形式"这句话在 `16` 的语境下继续有效**；
> 需要被禁止的只是**由它推出的**"estimand 也可以晚定"。

---

## 13. 引用列表

`CITED_PRIMARY`（本次实际读到摘要 / 全文 / 出版方记录，2026-09-27 核实）：

1. S01 Laurenceau, J.-P., Barrett, L. F., & Pietromonaco, P. R. (1998). *JPSP*, 74(5), 1238–1251. https://doi.org/10.1037/0022-3514.74.5.1238
2. S02 Laurenceau, J.-P., Barrett, L. F., & Rovine, M. J. (2005). *Journal of Family Psychology*, 19(2), 314–323. https://doi.org/10.1037/0893-3200.19.2.314
3. S03 Johnson, M. D., Lavner, J. A., Muise, A., Mund, M., Neyer, F. J., Park, Y., Harasymchuk, C., & Impett, E. A. (2022). *PNAS*, 119(30), e2209460119. https://doi.org/10.1073/pnas.2209460119
4. S04 Joel, S., Eastwick, P. W., Allison, C. J., et al. (2020). *PNAS*, 117(32), 19061–19071. https://doi.org/10.1073/pnas.1917036117
5. S05 Hamaker, E. L., Kuiper, R. M., & Grasman, R. P. P. P. (2015). *Psychological Methods*, 20(1), 102–116. https://doi.org/10.1037/a0038889
6. S06 Lucas, R. E. (2023). *Advances in Methods and Practices in Psychological Science*, 6(1), 25152459231158378. https://doi.org/10.1177/25152459231158378
7. S07 Muthén, B., & Asparouhov, T. (2024). *Psychological Methods*. 预印本 https://www.statmodel.com/download/ReciprocalV3.pdf
8. S08 Muthén, B., Asparouhov, T., & Witkiewitz, K. (2024). *Psychological Methods*. https://doi.org/10.1037/met0000701
9. S09 Schrodt, P., Witt, P. L., & Shimkowski, J. R. (2014). *Communication Monographs*, 81(1), 28–58. https://doi.org/10.1080/03637751.2013.813632
10. S10 Rusbult, C. E., Verette, J., Whitney, G. A., Slovik, L. F., & Lipkus, I. (1991). *JPSP*, 60(1), 53–78. https://doi.org/10.1037/0022-3514.60.1.53
11. S11 Rusbult, C. E., Bissonnette, V. L., Arriaga, X. B., & Cox, C. L. (2009). Accommodation processes during the early years of marriage. In Bradbury, T. N. (Ed.), *The Developmental Course of Marital Dysfunction*, 74–113. Cambridge University Press.
12. S12 Le, B., & Agnew, C. R. (2003). *Personal Relationships*, 10(1), 37–57. https://doi.org/10.1111/1475-6811.00035
13. S13 Rusbult, C. E. (1980). *Journal of Experimental Social Psychology*, 16(2), 172–186. PII 0022103180900074
14. S14 Rusbult, C. E., Martz, J. M., & Agnew, C. R. (1998). *Personal Relationships*, 5(4), 357–387. https://doi.org/10.1111/j.1475-6811.1998.tb00177.x
15. S15 Rusbult, C. E., & Martz, J. M. (1995). *JPSP*, 62(1), 62–87.
16. S16 Drigotas, S. M., Rusbult, C. E., Wieselquist, J., & Whitton, S. W. (1999). *JPSP*, 77(2), 293–323. https://doi.org/10.1037/0022-3514.77.2.293
17. S17 Pusch, S., Neyer, F. J., & Hagemeyer, B. (2023). *Personality and Social Psychology Bulletin*, 49(12), 1709–1724. https://doi.org/10.1177/01461672221113981
18. S18 Finkel, E. J., Hui, C. M., Carswell, K. L., & Larson, G. M. (2014). *Psychological Inquiry*, 25(1), 1–41. https://doi.org/10.1080/1047840X.2014.863723
19. S19 Lavner, J. A., Bradbury, T. N., & Karney, B. R. (2012). *Journal of Family Psychology*, 26(4), 606–616. https://doi.org/10.1037/a0029052
20. S21 Gable, S. L., Reis, H. T., Impett, E. A., & Asher, E. R. (2004). *JPSP*, 87(2), 228–245. https://doi.org/10.1037/0022-3514.87.2.228
21. S22 Fleeson, W. (2001). *JPSP*, 80(6), 1011–1027. https://doi.org/10.1037/0022-3514.80.6.1011
22. S23 Mischel, W., & Shoda, Y. (1995). *Psychological Review*, 102(2), 246–268. https://doi.org/10.1037/0033-295X.102.2.246
23. S24 Keltner, D., Gruenfeld, D. H., & Anderson, C. (2003). *Psychological Review*, 110(2), 265–284. https://doi.org/10.1037/0033-295X.110.2.265
24. S25 Cho, M., & Keltner, D. (2020). *Current Opinion in Psychology*, 33, 196–200. https://doi.org/10.1016/j.copsyc.2019.08.013
25. S26 Lemay, E. P., & Venaglia, R. B. (2016). *Review of General Psychology*, 20(1), 43–68. https://doi.org/10.1037/gpr0000066
26. S28 Granger, C. W. J. (1969). *Econometrica*, 37(3), 424–438. JSTOR 1912791.
27. S32 Tuzón, A., et al. (2018). *Frontiers in Physics*, 6:21. https://doi.org/10.3389/fphy.2018.00021
28. S33 Sprott, J. C. (2004). Dynamical models of love. *Nonlinear Dynamics, Psychology, and Life Sciences*, 8(3). https://sprott.physics.wisc.edu/pubs/paper277.pdf
29. Cook, W. L., & Kenny, D. A. (2005). The Actor–Partner Interdependence Model: A model of bidirectional effects in developmental studies. *Developmental Science*, 8(4), 275–279. PsycNet 2005-01893-002.
30. Kenny, D. A., & Ledermann, T. (2010). Detecting, measuring, and testing dyadic patterns in the actor–partner interdependence model. *Journal of Family Psychology*, 24(3), 359–366. https://doi.org/10.1037/a0019651

`CITED_SECONDARY`（转述，未读原文）：S20, S27, S29, S30, S31。

> **⚠ Round-3：三个承载源标 `PENDING_EVIDENCE_CHECK (R3-E3)`（sibling child 正在复核；本轮未打开）。**
> **标记，不猜测 —— 既不主张也不否认其内容：**
> - **`S04`**（第 4 条，Joel et al. 2020）：精确主张待核。
> - **`S19`**（第 19 条，Lavner et al. 2012）：**精确措辞与 Table 5 待核。**
>   ⚠ **本文件不复述 Table 5 的任何数值**，也**不**据其判定 `DVA` 的胜负。
> - **`S31`**：`Ideal` / RGM 的来源。⚠ **在核实前，`Ideal` 不得进入 `PARAMETER_CONVERGENCE`**
>   （§12 裁决请求 2 = `HOLD`；§7 状态块）。
>
> **本轮（R06 的 Round-3 pass）未打开任何新来源。** 凡标 `NOT_OPENED` 者即为未打开；
> 标 `AGENT_RECALL` / `UNVERIFIED` 者本轮**同样未打开**（状态不变）。

`FETCH_FAILED`（如实记录，未用作支撑）：F01–F08（见 packet §2.2）。

`AGENT_RECALL`（本次未核实，已在使用处标注）：S13 的比较水平公式细节。

`MODEL_HYPOTHESIS`（本报告构造，**无经验支持主张**）：MH1–MH6。
`MODEL_HYPOTHESIS` 文献语料（耦合 love ODE，无标定）：S33 及其相关文献
（Rinaldi 1998a/b; Rinaldi & Gragnani 1998; Radzicki 1993; Gragnani, Rinaldi & Feichtinger 1997; Ran 2007）。

**核实日期：2026-09-27。** 任何时间敏感事实（版本、维护状态、可访问性）以该日为准。
