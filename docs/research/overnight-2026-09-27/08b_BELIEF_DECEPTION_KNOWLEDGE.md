# 08b — Belief / Observation / Deception / Nested Knowledge

> **状态：** `RESEARCH_CANDIDATE`。本文件是 `youling/lhrm#30@overnight-opencode-exploration-swarm-v1` 的 Wave 1 / lane `R08` 产出，**不是** canonical architecture，未经 Human/Architect 审阅。
> **日期：** 2026-09-27
> **范围：** 为 LHRM 的
>
> ```text
> TrueState != ObservedState != BelievedState
> Reality -> Observation -> Belief -> Evaluation
> ```
>
> 这条链提供形式化候选、最小必要原语、以及一份**最小 belief 层设计**。本文件的中心主张是**简约**：整条链可以用 **8 个逐记录带类型槽位 + 2 个逐 (持有者, 内容) 带类型标量 + 4 个派生类 + 1 个世界模式标签** 表达；其余全部是 readout。
> **本文件最重要的产出是它的删减论证，不是它的构造。** §3 逐项说明为什么不采用动态认知逻辑、公共知识、事件模型、POMDP 引擎、后验作为状态、完整信号检测参数、以及完整信念修正理论——不是因为它们不优雅，而是因为它们在这里**不划算或不可解**。
> **标签约定：** `ESTABLISHED`（已引同行评审结果）、`FORMAL-THEOREM`（所引形式系统内的已证结果）、`MODEL_HYPOTHESIS`（本文件的设计提议，未验证）、`NEGATIVE`（反证据）、`UNKNOWN`。
> **硬边界（本次 attempt）：** `MERGE = FORBIDDEN`；`CANONICAL_MUTATION = FORBIDDEN`；`PRODUCTION_MUTATION = FORBIDDEN`；`CROSS_PROJECT_MUTATION = FORBIDDEN`；未读/未引用 LHRM `#20/#21/#22`；未触碰 Juece `#30` / PR `#31`。
> **本文件引用编号** `[S1]`–`[S72]` 指向 §11 的完整列表。

---

## 0. 为什么这个 lane 值得存在，以及它最容易犯的错

`CURRENT_ARCHITECTURE.md` §3 已经写下 `Reality != Observation != Belief`，§8 已经写��� `SimWorld_(Agent,m) = fork(BeliefState_A, mode)`，`AGENTS.md` 当前架构方向第 10 条也已经写明梦境/幻想/计划/反事实应当作为 nested Belief 存在。**换言之，LHRM 已经决定要有 belief 层。剩下的唯一问题是它有多小。**

这个 lane 最大的失败模式不是设计不足，而是**设计过度**：模态逻辑、公共知识、POMDP、贝叶斯后验、SDT 的 `d′`/`β`、AGM 修正理论，每一个都有独立的学术合法性，堆在一起会得到一个既不可解、又无解释力、又把 `Unknown` 碾平的层——而这恰好是 `AGENTS.md`「representation-first invariant」所禁止的。本文件的 §3 是一份**逐项的过度工程审计**，其中三条判决是明确的 **REJECT**，两条是 **REUSE-EQUATION-ONLY**，一条是 **DEFER**。

第二个失败模式是**把不披露当成信息缺失**。这是本文件 §4.4 的核心设计修正，也是 §5 中四个硬失败案例的共同根源。

---

## 1. 问题陈述：这条链真正要求什么

把任务链展开成需要回答的问题：

| 链环节 | 需要表达的东西 | 是否需要形式化 |
| --- | --- | --- |
| `Reality` | `Θ(t)` — 关系世界的事实状态 | 已有：`WorldState` / `Agents` / `Relationships` / `Environment`（`CURRENT_ARCHITECTURE.md` §3） |
| `Observation` | 某人（或某来源）**实际接触到**的东西及其**类型** | 需要：类型很重要（见 §3.9 Kripke 区分） |
| `Belief` | 某人**持守**关于某内容的立场 + 其根据 + 其对来源的判断 | 需要：本文件的全部内容 |
| `Evaluation` | 从状态/信念生成 readout | 已有原则：downstream readout，不得反 definitional |

三条链（`TrueState != ObservedState != BelievedState` 与 `Reality -> Observation -> Belief -> Evaluation`）合起来只要求一件事：**存在一个不落在 `Θ` 上的、可寻址的、带根据的、可带来源的、带时间坐标的立场记录层**。它不要求模态逻辑，不要求公共知识，不要求 POMDP 策略求解。

**一个必须先说清的区分。** `Observation` 与 `Belief` 的分离，**不是**「事实 vs 信念」这一哲学区分的浅薄版。二者在实现上是不同类型：

```text
Observation  =  ( sensor, content, time, signal_type, discriminability_unknown )
Belief       =  ( holder,   content, time, stance,  ground,  source,  attributed_other_stance )
```

`Observation` 是 `Θ` 上的一次采样事件（可带噪、可被误分类）；`Belief` 是某个主体持有的一个持守态度（可错、可被隐藏、可被二阶审视）。LHRM 的链要求这两者**在类型上不同**，这与 SDT 的承重贡献一致：`signal` 与 `criterion` 必须可分离测量，若压缩成单一「信心」即失去可解释性 `[S19, S20]`。

---

## 2. 最小必要原语（parsimony-first）

**这是本文件的第一个交付项。** 下面列出 LHRM 真正需要的原语，按「不可再删」排序。每条给出**为什么不能更少**（最小性的反证尝试）。

### 2.1 内容（content）

```text
Φ  =  关系相关的内容集合
```

**不可更少：** 没有内容就无法寻址，`Θ` 与 `Bel` 无法分离。

**但** `Φ` 的元素**必须带类型**，这是本文件的一条硬要求（`MODEL_HYPOTHESIS`），理由不是「整洁」而是 **Biro 的证据/伪证据类型错误** `[S11]`：Kripke 的教条论证之所以成立，是因为它把「意在改变信念之物」与「只是自称为证据之物」混为一谈。因此 LHRM 的每条 `Observation` 与每个 `ground` 都必须回答：这个东西**是否自称为**该类型的根据？

`Φ` 至少需要能容纳**非命题内容**——因为 `AGENTS.md` representation-first invariant 明确要求「一个坐标可以是 interval、ordinal state、category、constraint、probability distribution、Unknown 或 estimate + uncertainty + evidence」。故 `Φ` 是**带类型的对象**，不是一阶命题逻辑的原子。这直接否定了「把 LHRM 的内容做成 Kripke 模型的原子命题」这一选项（§3.1）。

### 2.2 持有者（holder）

```text
H  ∈  { ι , ι' , ι⊛ }
      主体A   主体B   该 pair
```

**`ι⊛`（pair-level）不可省。** 这是本文件相对「只有两个 agent」的最重要扩展。理由：

1. 关系中存在**可被第三方观察的联合承诺**——「我们答应一起去看医生」「我们决定明年搬到 X」「我们家不接待人」。「双方都相信 p」与「双方以二人名义承诺 p」在法务与纪实材料中是**不同的事实**，前者不可由第三方证实，后者可以。
2. `sharing-is-believing` 表明沟通者会把描述调向伴侣态度，**且这会塑造其后对目标的记忆** `[S59]`。所以「我们共同生产了 `p` 这个信念」与「我们各自独立相信 `p`」在 provenance 上是不同的：一个有 `CO_CONSTRUCTED` 的 ground，一个没有。
3. 但 `ι⊛` **不是** common knowledge，也**不是**「双方的合取」（见 §4.3）。

**不可更少**（反证尝试）：若只有 `{ι, ι'}`，则 `ι⊛` 只能被表达为 `∧`，于是「共同生产」与「偶然收敛」不可区分，而 shared reality 的全部文献都建立在「共同生产」之上 `[S57, S58, S59, S60]`。→ 保留 `ι⊛`。

**明确不扩展到 `ThirdParty`。** 理由：法务材料中 `Observation` 常来自法官/第三方（`CURRENT_ARCHITECTURE.md` §10），但 LHRM 的最小查询单元是 HumanDyad（§2），且 R11 尚未收敛。→ `H = ThirdParty` 标为 `DEFER`（§9-6）。

### 2.3 时间/历史坐标

```text
τ  =  ( history_id , local_time )
```

**直接继承** `CURRENT_ARCHITECTURE.md` §8，**不新增**。注意 `τ` 已经是 lineage 版本坐标，所以「延迟知识」「承诺了但不实现」「后来才发现」这类 case **不需要新机制**，只需要 `τ` 排序。

### 2.4 世界模式（world mode）

```text
M  ∈  { ACTUAL , IMAGINED , PLANNED , CF , DREAM }
```

**这是 `AGENTS.md` 第 10 条的全部要求。** 一个枚举字段 + 一个 `parent` 结构指针，就把梦境/幻想/计划/反事实从真实 `WorldState` 中隔离出去，同时保留它们对现实的影响路径（经 `Belief` / `Emotion` / `ActionPolicy`，`CURRENT_ARCHITECTURE.md` §8）。

**不可更少**（反证尝试）：若去掉 `M` 而用 `Θ` 上的分支历史表示，则每个 `Bel` 记录都需要一个「它属于哪条历史」的解释，爆炸半径覆盖 `Θ`；且 `AGENTS.md` 明确要求这类世界**应作为 nested Belief** 而非污染 `WorldState`。→ 保留 `M`。

**注意 `CF` 与 `IMAGINED` 为什么要分开。** 「昨晚梦见…」与「我曾想过如果…」在 LHRM 中都不是真实世界状态，但它们回流到现实信念的**机制不同**：梦境回流经由情绪/记忆重构，反事实回流经由「已排除的选项集」。保留两值以免把这两条路径压成一条。`MODEL_HYPOTHESIS`。

### 2.5 立场（stance）

```text
k  ∈  { + , − , ? , ⊘ }
     真/承诺   反/否认   悬置   不涉及
```

**四个值，不是三个。** `?`（明确知道有这个问题但不定）与 `⊘`（没有这个问题）**必须分开**，因为：

- `AGENTS.md` 要求「Unknown/missing data must remain explicit; never silently coerce missing information into neutral values」。把「我不知道他是否出轨」与「我没想过这件事」压成一个 `UNKNOWN`，就恰好犯了这个错。
- `Harman` 的 defeat solution 与 `Kripke` 的两个残留 worries `[S5, S12]` 在结构上正是关于 `?` 这个状态：一个主体在 `?` 状态下遇到证据会转 `+` 或 `−`；一个主体在 `+` 状态下遇到反证据是否会转，是教条悖论的全部内容。把 `?` 折进 `⊘` 会让这个区分消失。
- 亲密关系材料中「我不敢问」是一个 `?`，而「我们不谈这个」是一个**双方共谋维持的 `?`**（§4.4）。压平会丢掉共谋。

**为什么不是概率？** 见 §3.4 与 §4.2 的 `credence` 判决。短版：`d′` 与 criterion 在真实数据中不独立 `[S20]`，且在最相关通道上人类接近随机 `[S22]`；把「敏感度」与「判准」压成一个概率数，就重犯 SDT 200 年来被反复纠正的那个错误 `[S19]`。

**为什么不用 outright-belief（`Gaultier` 的 sense）作为唯一正向值？** `Gaultier` 表明 outright belief 加上 doxastic closure 会直接产生悖论，并导出「我们的信念生活中几乎没有 outright belief」这一不可接受结论 `[S9]`。→ 不采用 outright-belief 语义；采用「`+` 是持守，**不蕴含** `p`」的朴素持守语义。

### 2.6 根据（ground）

```text
g  ∈  { FIRSTHAND , REPORTED , INFERRED , ASSUMED , CO_CONSTRUCTED , UNKNOWN }
```

**六值。** 每一值都对应一条独立的、可独立检验的处理规则：

- `FIRSTHAND`：`ι` 亲历/亲见/亲为。
- `REPORTED`：`ι' `（或第三方）断言。**必须伴随 `src` 指针。**
- `INFERRED`：从其他记录推出。**不追溯其基础**（不做全链展开）——理由：Fricker 的 `T` 说知识经信任证言总是二手，但**不**要求持有者持有整条上游链 `[S65]`；且全链展开在法务卷宗上是 O(链长) 爆炸。若需要，`INFERRED` 记录本身可作为另一条记录的 `src`。
- `ASSUMED`：前提，无证据支持。**不可省**：`AGENTS.md` 要求显式 Unknown/缺失，若没有 `ASSUMED`，「我假设他知情」会被静默塞进 `FIRSTHAND`。
- `CO_CONSTRUCTED`：**通过与 `ι' ` 的沟通而生产**。这是 `sharing-is-believing` 的 provenance 签名 `[S59]`，也是本文件与朴素层的关键差异（§5-1）。
- `UNKNOWN`：根据不可辨（丢失、未记录、法务材料中不可判定）。**这是一个正式的 `g` 值，不是 `null`。**

**为什么 `REPORTED` 不是一个 `src` 而是一个 `g`？** 因为二者回答不同问题：`g` 回答「这条信念的根据属于哪一类」，`src` 回答「具体是谁在什么时候说的」。Fricker 的异质性论证要求可靠性**按内容索引** `[S63]`，这由 `src` + `Rel` 承担，不由 `g` 承担。

### 2.7 来源记录（source）

```text
src  ∈  Agent  ×  τ   |   UNKNOWN
```

**一个指针，不是概率。** 它的作用是**不丢 provenance**（`AGENTS.md` research discipline）与支撑 Fricker 的二手不变式（§4.6）。

**为什么不是一个可靠性分数？** 因为可靠性必须按内容索引（`Lackey` / `Fricker`：testimony 不是一个统一类别 `[S63]`；`Polarization Paradox`：被极化主体不信任的是来源**关于 `¬p`** `[S10]`）。标量信任不可表达二者。→ 可靠性放在 `Rel`，标量形式**被禁止**（§4.6 的可检验不变式）。

### 2.8 归属他人立场（attributed other-stance）

```text
m  ∈  { + , − , ? , ⊘ }        默认 ⊘
```

含义：`h` 对「另一方对 `p` 有一个已定的 `+` 立场 / `−` 立场 / 未定立场」的**自己的**判断。

**这是本文件唯一真正需要二阶能力的地方，而它被压缩成了一个一阶记录上的可选字段。** 理由见 §4.3 的「把嵌套折进字段」。

它承载的四个现象：
- **透明度错觉**：`m = +` 而 `ι' ` 的实际 `k` 是 `?`。
- **非对称了解错觉**：`ι` 认为 `ι' ` 知情（`m = +`）而 `ι' ` 的 `k = ⊘`。
- **putative secret**：`ι` 知 `p`（`k = +`）且认为 `ι' ` 不知（`m = ?`），而 `ι' ` 实际知（`ι' ` 的 `k = +`）且认为 `ι` 知（`ι' ` 的 `m = +`）。**注意这需要三阶，但用字段读法只需两次一阶读。**
- **对关系的元信念**：「我认为他知道这段关系正在恶化」。

**已知代价（诚实记录）：** `m` 合并了「我认为他知道」与「我认为他相信 p 为真」。`Kripke` 的教条悖论明确反对这种合并（知识 vs 信念的强区分）`[S5]`。但**没有廉价的操作测试**能在关系材料中区分二者（没有任何研究告诉我们如何从文本判定「A 声称知道」是否意味「A 声称知道而非相信」）。→ 拆分**延后**（§9），`MODEL_HYPOTHESIS`。

### 2.9 证据策略（evidence policy）

```text
Pol( ι , p )  ∈  { OPEN , CONSERVING , UNKNOWN }
```

**逐 (持有者, 内容)，非逐记录。** 这是 dogmatism paradox 的唯一落地点（§3.9）。

**为什么必须独立于 `k`？** 因为教条主义**不是**一个「错误的信念」，它是一个**关于证据如何被处理的策略**。`Salow` 证明 dogmatic argument 的成败取决于 **Preservation**（修正结构的一个属性），**不取决于 `p` 是否为真** `[S7]`；`Kripke` 自己的论证 (i)–(vi) 依赖的是「我现在知道 `p`」这一**策略性前提** `[S6]`。把教条主义编码为「`k` 特别强」或「`k` 附一个高置信度」，都会让 `Pol` 的真实内容消失。

**为什么不能省（反证尝试）：** 省掉 `Pol` 后，模型只剩三种方式表达固着：(a) 抬高先验——但那是 credence 字段，已被禁（§3.4）；(b) 降低 `Rel`——但 `Rel` 按内容索引，无法表达「对 `p` 不利的一切来源都不可信」这一**类别**判断（§3.9 Polarization）；(c) 声明不更新——但这需要一条规则，而规则正是本字段。→ 保留。

### 2.10 来源可靠性（source reliability）

```text
Rel( ι' , p ; frame )  ∈  { Low , Mid , High , UNKNOWN }
frame  ∈  { conducive , obstructive }
```

**三个强制约束：**
1. **必须按内容 `p` 索引。** 依据：`Lackey` / `Fricker` 的异质性论证 `[S63]`。
2. **必须按 frame（有利于/不利于当前立场）索引。** 依据：Polarization Paradox——被极化主体的结构是「我信 `p`，且我信**所有会告诉 `p` 为假的来源在 `p` 上不可信**」`[S10]`。若无 frame 维度，该结构不可表达（正是 §4-C3 的 `NEGATIVE`）。
3. **禁止塌缩为标量 `Trust(ι')`。** 这是一条**可检验的不变式**（§4.6）。

**为什么用 Low/Mid/High 而不是概率或区间？** 简约：这是一个 `Pol` 式的**策略输入**，不是 `Θ` 的量。`AGENTS.md` 说「A coordinate may be an interval, ordinal state, category…」，序数在此足够；任何更细的量化在 §3.4 已论证为不划算。

**`Rel` 同时是 `Φ` 的一个元素。** 这是解决二阶问题的关键技巧：`Rel(ι', p; frame) = ρ` 是一条**普通内容**，因此「`ι` 关于「`ι' ` 在 `p` 上不可信」的信念」是一条**普通的一阶记录**（`p = Rel(...)`, `g = INFERRED`）。→ **二阶变成一阶，modality 深度归零。** 这是本文件最重要的简约技术。

### 2.11 派生关系（**永不存储**）

| 关系 | 定义 | 归约到 |
| --- | --- | --- |
| `BelievesBoth(p)` | `k_ι(p) = k_ι'(p) = +` | 两个持有者上的合取 |
| `Shared_Noted(p)` | `k_ι(p) = k_ι'(p) = ?` 或 `⊘` | 同上 |
| `Asymmetric(p)` | 恰有一个 `k ∈ {+,−}` | 同上 |
| `Divergent(p)` | `k_ι(p) = +, k_ι'(p) = −`（或反） | 同上 |
| `Overclaim(ι, p)` | `m_ι(p) ∈ {+,−}` 而 `k_ι'(p) ∉ {与 m 相应值}` | `m` vs `k` |
| `Meta_Unrealized(ι, p)` | `m_ι(p) = +` 而 `k_ι'(p) = ?` 或 `⊘` | `m` vs `k` |
| `NonDisclosure(ι, p)` | `k_ι(p) = +` ∧ `m_ι(p) ∈ {?, −}` ∧ `ι` 有保留 `p` 的记录 | `k` ∧ `m` ∧ `Behavior` |
| `Unreliable(ι, p)` | `Rel(ι', p; frame) ∈ {Low}` | `Rel` |

**关键：** `NonDisclosure` 需要一个**第三输入**——「`ι` 确实有东西没披露」。这只能是**行为记录**（`Action/Event` 层），不能是 `Bel` 层的字段。→ **LHRM 需要一个 `Disclosure` 事件类型**，其内容是「`ι'` 把 `p` 放在 `ι` 可及范围内 / 放在不可及范围内」。这是一个 `Action/Event`，不是 belief。这是一个重要的分层结论：**部分披露的表示不在 belief 层，而在 action 层**（§4.2 的 `g` 与 `src` 是 belief 侧的接收结构；披露动作本身是 `CURRENT_ARCHITECTURE.md` §6 的 `Action/Event`）。

---

## 3. 候选形式化审计：买什么 / 花什么 / 是否过度工程

**这是本文件的第二个交付项，也是强制交付项。** 每一项给出：买到了什么、代价是什么、以及**是否过度工程**。判决用 `ADOPT` / `REUSE-EQUATION-ONLY` / `DEFER` / `REJECT`。

### 3.1 Epistemic logic 与 modal logic

**买到的：** 一个能表达 `K_a φ` / `B_a φ` / 高阶归属 `B_a B_b φ` 的现成语言，配 Kripke 语义与可判定性结果 `[S1, S3]`。

**代价：**
1. `PAL` 与普通多模态逻辑**表达力等价**（PAL Expressivity Theorem）`[S1]`。唯一增益是**指数级简洁性**（Succinctness Theorem）`[S1]`。LHRM 按 `AGENTS.md` representation-first invariant 重视可审查性；用指数级简洁换零表征能力是**净负**。
2. `PAL` 语义预设公告**完全可信、真实、公开、被一致接收**，且沟通**只能带来信息变化不能带来事实变化**。SEP 自己写明这些假设在日常情境中「of course unrealistic」`[S1]`。LHRM 的目标对象逐条违反。
3. 需要一个**完备的原子命题语言 + 公理系统 + 可靠性/完备性证明**才能称为「形式化」。LHRM 的 `Φ` 元素是「interval、ordinal、constraint、probability distribution、estimate + uncertainty + evidence」（`AGENTS.md`），不是原子命题。→ **模态逻辑无法在不重新定义 `Φ` 的前提下承载 LHRM 的内容类型。**

**判决：REJECT（作为 LHRM 本体）。保留一处采纳。**

**保留的采纳：** `KD45` 读法。Gerbrandy–Groeneveld 的 update 允许可达关系**失去自反性**，理由是「belief need not be true」`[S4]`——这正是 `TrueState != BelievedState`。**只要把「知识」读成 `S5`、把「信念」读成 `KD45`，就免费得到正确的语义，而不需要任何模态框架。** 这是一次措辞改动，不是一个体系。`ADOPT`（最小切片）。

### 3.2 公共知识（common knowledge）

**买到的：** `[B*]F` 算子，及关于「互相都知道对方知道…」的无限递归语义 `[S1, S3]`。

**代价：**
1. 加入 common knowledge 后 **reduction theorem 失效**；`PAL+C` 与 `RCK` 的**可满足性为 EXPTIME-complete**（Lutz 2006）`[S1]`。
2. **迭代 PAL 不可递归公理化**（Miller & Moss 2005）`[S1]`。
3. 人类侧：博弈中平均推理深度约 **1.5 步**；人们「一般无法显式完成推理 common knowledge 所需的无限递归」`[S38]`。

**判决：REJECT。** 两条独立理由（形式不可解 + 经验不支持），任一条即足够。

### 3.3 递归（recursive ToM / "I think you think I think"）

**买到的：** 表达任意深度心智理论归属的语言；以及关于**哪一阶真正有用**的实证区间。

**代价与实证：**
- 人类**默认是一阶**；对手被建模为短视/零阶；成人二阶正确率约 65% 且**只在训练末期** `[S34]`。
- 二阶表现高度**脚手架敏感**（分步指导、带支持的训练、先预测再决策）`[S35]`。即成人有二阶能力，但**脆弱且指令约束**。
- 谈判中**收益在二阶饱和**：ToM1 > ToM0，ToM2 > ToM1，**「we find no additional benefit for third-order theory of mind」** `[S36]`。
- **反证**：更简单、零和、竞争性博弈中默认阶次**更高**，且高阶假设有时导致次优行为 `[S37]`。→ 深度是**任务依赖**的。
- 成人对高阶命题态度的**理解**可测到第 8 阶 `[S39]`。→ **理解**与**自发策略性使用**必须分开；不可用「能理解 8 阶」推出「会自发用 3 阶」。
- 无关系的两人 dyad 是一个深度上限为 2 的极小 agent 集合。3 阶以上需要至少 3 个主体或 1 个主体 + 关于嵌套的额外公理。LHRM 的最小查询单元是 HumanDyad（`CURRENT_ARCHITECTURE.md` §2）→ **3 阶在 LHRM 内的收益上限本就很小**。

**判决：ADOPT，有上限 —— 深度上限 2，且做深度为显式记录的字段。**
**特别说明（mixed-motive 例外）：** `[S36]` 是唯一发现更深阶次（ToM4）有优势的研究，且优势出现在**混合动机**（谈判）情境 `[S36]`。混合动机大致是浪漫 dyad 的最近类比。→ **LHRM 应当已允许在 `M` 非 `ACTUAL` 的计划/想象世界内使用 order-3。** 其余情况硬性截断在 2。这是本 lane 唯一一处主动保留的深度余量。

### 3.4 Bayesian 更新与后验作为状态

**买到的：** `b_{t+1} ∝ O(o|s_t)·T(s_{t+1}|s_t,a)·b_t` 的更新骨架；以及「信念是分布而非点估计」这一保护 `[S16]`。

**代价：**
1. `[S16]` 自己就说：用最可能状态作行动依据「is not sufficient in general」——即**必须携带整个分布**。为 Case Bank 式逐句映射携带一个连续分布，是灾难性的表示选择。
2. 「分布是过去历史的 sufficient statistic」这一性质**仅在已知 transition model 与已知 observation model 时成立**。LHRM 两者皆无，且在**最关系相关的通道上**（是否在说谎）人类的传感器接近随机 `[S22]`。→ sufficient-statistic 前提在此**失效**。
3. 教条推理与 motivated reasoning 无法由一个后验解释。`Kunda`：accuracy goals 与 directional goals 是**不同机制**；accuracy goals → 更复杂加工；而**更复杂 ≠ 更理性**（accuracy-motivated 者对 dilution effect 反而更易感）`[S14]`。一个后验需要**另外的解释层**。→ 后验不省事，它把工作推给别处。
4. 一个后验字段一旦存在，下游几乎必然出现「置信度 = 0.73」这类 readout，即重犯 `d′`/criterion 混淆 `[S19, S20]`。

**判决：REJECT（后验作为状态）。REUSE-EQUATION-ONLY（更新骨架）。**
**替代方案（本文件的核心主张）：** 不存 `credence`。用 `k`（四值立场）+ `Rel`（序数可靠性）+ `Pol`（序数策略）**三元组**承担「信念强度」的全部表达需求。若某个下游任务确实需要数值，取 `(k, g, src, Rel, Pol)` 上的**计算 readout**，且该 readout **不得**被写回为状态。

### 3.5 Signal detection theory

**买到的（唯一值得买的）：** **discriminability 与 criterion 可分离**这一原则 `[S19, S20]`。任何单一信心数都混淆二者。

**代价（若把 `d′`/`β` 放进状态）：**
1. `d′` 假设（双分布正态 + **等方差**）在 yes/no 任务中**无法检验**，且等方差「particularly suspect」（Swets 1986）；一旦违反，`d′` **随 response bias 变动** `[S20]`。即「可辨别性」与「判准」在真实数据中**不独立**。
2. **当偏置由 payoff 驱动时 accuracy 不是正确目标函数**：liberal bias 条件下赚更多分而 accuracy 更低 `[S21]`。Line of Optimal Response 指出低 `d′` 应诱发**极端**偏置，故连规范上也不能独立读取。
3. 对 LHRM 最相关通道：人类识别谎言 **54% 正确，`d ≈ .40`**，47% 谎言被识破，61% 真话被识别；**人们认为自己的互动伙伴是诚实的**；**当人们希望被相信时会显得可疑** `[S22]`。

**判决：REJECT（`d′`/`β` 作为 belief 层参数）。ADOPT（分离原则）。**
**替代方案：** 观察通道的可辨别性属于**测量/评价层**（`Measurement / Canonicalization`，`CURRENT_ARCHITECTURE.md` §9），不是 belief 状态。`Θ` 侧只保留**两个强制要求**：
- **base-rate 通道必须存在。** 因为最优 criterion 由 base rate 与 payoff 加性决定 `[S19]`，无 base rate 的单次观测判读必然被 criterion 主导。
- **由线索推断出的「他在隐瞒」必须是带 provenance 标注的报告，不得静默升格为 fact。** 理由是 `[S22]`。

### 3.6 欺骗 / 印象管理 / 动机性推理 / 自我欺骗

**买到的：**
- **动机性推理**的分型：accuracy goals / directional goals 是不同机制 `[S14]`；**accuracy motive 本身可通过制造更充分的合理化而稳定扭曲**（哲学论证，非实证）`[S15]`。
- **协作性不诚实**的实证基线：87,771 次决策、k = 123；重复互动中双方不诚实**相关且随回合递增** `[S23]`；second mover 报出 payoff 结果比等价单人任务高 14%；激励在此起作用而单人任务中不起作用 `[S24]`。
- **亲密关系中不诚实的类型学与动机**：四种 form；Peterson (2010) 六类；**两个主导动机：self-protective 与 "(alleged) partner-protective"**；不论 form/content/motive，多为有害 `[S25]`。
- **隐瞒定义是合取的**：预期引发不满的行为 **AND** 故意不披露，**两者缺一不可** `[S26]`。

**代价与陷阱：**
1. 若把「欺骗」做成 dyad 级 trait，会与证据冲突：在 2,200 对美国夫妻样本中，**策略动机在金融信息分享中不起作用**，坏消息 spillover 反而更大 `[S31]`。策略效应出现在**实验室金钱激励任务**中 `[S23, S24]`。→ 合作性不诚实是**任务与激励条件化**的，不是 dyad 属性（§4-C4）。
2. 「不忠」标签本身高度依赖规范违反：52.13% 研究未确立规范违反，施加后 emotional infidelity 流行率由 35.23% 降至 17.38% `[S33]`。→ `deceptive` 记录**不蕴含**规范判断。

**判决：ADOPT（作为带动机的事件类型 + `NonDisclosure` 派生关系）。REJECT（作为 trait 或作为 belief 状态）。**
**关键设计：** 隐瞒是**关于一个 `Behavior` 的断言**，不是 belief 字段；`m`（归属他人立场）提供「我认为你不知道」这一必要侧翼；`Pol` 提供「我因此不听」的策略后果。**三层都不需要「deception」这个原语。**

### 3.7 POMDP

**买到的：** belief state `b ∈ Δ(S)` 与更新式 `b' = Σ_o Pr(o|a,b)·Pr(b'|a,b,o)` `[S16]`；以及「不确定时不应只看最可能状态」的保护 `[S16]`。

**代价：**
1. 需要**已知的 transition model、已知的 observation model 与一个 reward function**。LHRM 三者皆无且**刻意不要**（`AGENTS.md` 不冻结分数；`CURRENT_ARCHITECTURE.md` §6 转移是连续/混合状态上的演算，不是受控链；§11 明确不冻结统一权重/距离/分数）。
2. 一般情形精确解不可解：value iteration 展开 `|V_{t+1}|` 棵策略树，对 `|Ω|` **指数** `[S16]`；分段线性凸值函数上的 DP 更新**不可解** `[S18]`；witness 算法一般仍指数 `[S17]`。
3. 即使只取 belief state，「分布是 sufficient statistic」也需要已知 observation model —— 而这正是 `[S22]` 表明在相关通道上为假的东西。

**判决：REUSE-EQUATION-ONLY。**
**为什么不是 REJECT：** 更新骨架值得抄一行。但**不实现** policy solving、reward、belief-MDP。LHRM 需要的「值迭代」等价物是 R06 / R09 的 transition law，而那必须服从 `AGENTS.md` 的「Representation before scalarization」与「不以单一分数为第一阶段产物」。

### 3.8 证言 / 转述 / 来源可靠性

**买到的：**
- **异质性论证**：`testimony is not a unitary category`（Fricker, 经 Lackey 逐字引）`[S63]`。报告类型谱系化分布：时间 vs 政治对手人格 vs 视说话人而定的年龄/犯罪记录。
- **二手不变式**：通过信任证言获得的知识总是二手；**不存在只通过证言而被知的事实** `[S65]`。
- reductionism vs non-reductionism 之争，以及三条反驳（循环、无穷倒退、以及「人们不擅长察觉说谎」使 local reductionism 过于苛刻）`[S62]`。

**判决：ADOPT（异质性 + 二手不变式）。REJECT（reductionism / non-reductionism 之争）。**
**理由：** 这场哲学争论与 LHRM 无关。相关的是**可操作的结论**：`Rel` 必须按 (source, content) 索引，禁止标量（§2.10、§4.6）。
**术语判决：** 用 **testimony**，不用 hearsay。后者是**法律/规范**类别，用于本模型会引入一条非预期规范轴。

### 3.9 信念修正、信念固着与 dogmatism paradox

**先做一次文献更正（重要）。** mission 说「Kuhn's "dogmatism paradox" is directly relevant」。**规范对象是 Kripke–Harman dogmatism paradox**：Kripke 1972 年在 Cambridge Moral Sciences Club 讲授；Harman 在 *Thought* (1973, p.148) 传述 (i)–(vi) 版；Kripke 以 "Two Paradoxes of Knowledge" 收入 *Philosophical Troubles* vol.1 (2011), pp.39–49 `[S5, S6, S11, S12]`。Kuhn → Harman → Kripke 的谱系真实，但**经由 Gilbert Harman，不是经由 Kuhn 的教条论题**。任何归于 Kuhn 的表述会被熟悉文献的审稿人标记。
**另需分开：** Kuhn 的 *The Function of Dogma in Scientific Research* 是**另一个论题**；且「Kuhn 主张教条主义」的通行解读本身有争议 —— 有工作论证「Kuhn himself never espoused the language of dogmatism or uncritical attitude in *Structure*」，并把 Kuhn 读作主张**认识论证成 + 相对其他选项 pragmatically 保留**，以及 **revisionary rational reconstruction**（「not science is irrational but our notion of rationality needs adjustment」）`[S72]`。**本文件不引用 Kuhn 的该文作为任何主张的依据。**

**买到的（这是本文件 §2.9 存在的唯一理由）：**
1. **Doxastic coherence 是悖论的引擎。** `Gaultier` 表明：强加「信 `p` 且信 `p ⊨ q` 却不信 `q` 即不合理」，就使 closure + outright belief 产生悖论，代价是「我们的信念生活中几乎没有 outright belief」`[S9]`。→ **不要对本层强加 doxastic closure。** 这是一条**具体的实现禁令**。
2. **证据的类型区分是核心。** `Biro` 指出 Kripke 的论证混同 **"evidence"**（意在改变信念之物）与 **"purported/alleged evidence"**（只是自称为证据者）`[S11]`；`Veber`：人们「常常以为自己知道实际上不知道的东西」。→ **LHRM 的 `Observation` 与 `ground` 必须带「是否自称为该类型根据」这一维度。**
3. **真正的理论轴是修正结构，不是真值。** `Salow`：**Preservation**（若 `q` 与你当权 believed 的一切相容，发现 `q` 后仍可保留全部信念）vs Weak Dominance vs Conditional Dominance `[S7]`。dogmatic argument 在 Preservation 两种取值下都崩塌；可操作原则是**条件式**的：「若你将发现的证据强烈不利，则你很可能错了」。→ 这**就是**一条 evidence policy。`Pol` 因此是原语，不是便利。
4. **Harman 的 defeat solution 只处理历时性教条；共时性教条（现在就决定忽略一切未来反证据）是真问题** `[S5, S12]`。Kripke 的两个残留 worries：precautionary dogmatist（预先避开反证据来源），以及 weak evidence（未被 defeat 但忽略它仍属教条）。
5. **Polarization Paradox 是本文件最重要的相关结果。** Begby & Thi Nguyen：`"epistemically untrustworthy"` 明确包含 unreliable / uninformed / misinformed / **deceptive** / unconcerned with the truth 的来源 `[S10]`。一个既有好理由信 `p`、又有好理由不信任一切提供 `¬p` 证据的来源的主体，到达同一教条结论；此时 **defeat solution 可证失效**，因为反证据被先验不信任**先制**；Nguyen 的 **disagreement-reinforcement mechanism** 使每个新反例**反而加强** `p`。他们提出的「降权而非丢弃」修正版也被该机制反驳。净结论：**对被极化的主体，教条态度可能是理性的。**
   → 这正是一段长期伴侣学会了「在这类争议话题上不听对方」的处境。**这是 `Pol` 存在的经验理由，也是 `Rel` 必须带 frame 维度的原因。**
6. **教条主义不是常态。** 在 4 项研究中，人们**改变**信念朝向一致的清晰证据，即便它反自身立场；混合证据才产生固着 `[S68]`。→ 任何默认保守常数的 belief 层会**高估**教条主义。
7. **保守性可能根本不是规范缺陷。** experimental pragmatics：被试可能并未把实验者提供的证据当作完全可靠；**从贝叶斯视角，较低可靠性 ⇒ 较保守修正在规范上是恰当的** `[S66]`。→ 保守性必须条件于 `Rel`，不是常数。

**判决：ADOPT（Preservation / Conditional-Dominance 作为 `Pol` 的语义来源 + 强禁 doxastic closure + `Observation` 类型化 + frame-indexed `Rel`）。REJECT（AGM 的完整公理化与收缩算子 / 收缩 / 完备性公理表）。**
**为什么拒绝 AGM 完整实现：** AGM 的价值在于它的**序关系偏好**（最小修改、先解释后撤回）作为**可陈述、可被经验反驳的先验**，而不在于它的公理系统与不可能性定理。把一个不可反驳的公理系统装进一个以 Case Bank 表示覆盖为验证手段的项目里，等于把最重要的判据从「经验」换成「公理」——这与 `AGENTS.md` validation discipline 冲突。→ 取其序偏好作为**声明的先验**，不取其证明负担。

### 3.10 事件模型 / action model（保留项，DEFER）

**买到的：** BMS 的 action model 是 Kripke 模型的一个推广，SEP 明言它「可含 degrees of privacy, misdirection, **deception**, and suspicion」`[S1]`。这是本节列出的所有形式化中，**对 LHRM 最贴合**的一个。

**为什么仍然 DEFER：**
1. action model 的 precondition 是**模态公式**，即它预设了一个**已完备的原子命题状态语言** `[S1, S3]`。LHRM 的 `Φ` 元素不是原子命题（§3.1-3）。→ 它无法在当前 `Φ` 上运行。
2. 它的价值场景是「通信博弈的**语言级**规格」——前提、公理、协议正确性。LHRM 的第一目标不是通信协议，而是**关系状态表示**（`CURRENT_ARCHITECTURE.md` §1）。
3. 它会把 belief 层的复杂度从「几个带类型槽位」推到「嵌套的模型变换算子」，违反 `AGENTS.md`「Prefer few stable constructs + composition + time evolution over a growing checklist」。

**判决：DEFER。触发条件：** 若 Case Bank 出现一个**通信回合族**（有成对发言、有接收者、有可争议的「我当时说的是另一回事」），则 event model 是正确的升级路径。**在此之前不实现。** 这是一个有明确触发条件的延后，不是拒绝。

---

## 4. 推荐的最小 belief 层设计

### 4.1 类型

```text
Content   Φ
Holder    H  :=  ι | ι' | ι⊛
Time      τ  :=  ( history_id , local_time )
Mode      M  :=  ACTUAL | IMAGINED | PLANNED | CF | DREAM
Stance    k  :=  + | − | ? | ⊘
Ground    g  :=  FIRSTHAND | REPORTED | INFERRED | ASSUMED | CO_CONSTRUCTED | UNKNOWN
Attributed m :=  + | − | ? | ⊘          -- 默认 ⊘
Policy    Pol( ι , p )        :=  OPEN | CONSERVING | UNKNOWN
Reliability Rel( ι' , p ; frame ) :=  Low | Mid | High | UNKNOWN
frame                       :=  conducive | obstructive
```

### 4.2 记录层

```text
Record  =  ( p , H , τ , M , k , g , src , m , parent )

  p       ∈ Φ
  H       ∈ Holder
  τ       ∈ Time
  M       ∈ Mode
  k       ∈ Stance
  g       ∈ Ground
  src     ∈ (Agent × τ) | UNKNOWN
  m       ∈ Attributed            -- 可选，缺省 ⊘
  parent  ∈ Record* | ⊥          -- 仅当 M ≠ ACTUAL 时需要
```

**槽位表（八个逐记录槽位，每个都给出「为什么不可再删」）**

| # | 槽位 | 不可更少的理由 | 若删除会怎样 |
| --- | --- | --- | --- |
| 1 | `p` | 没有内容就不可寻址，`Θ` 与 `Bel` 无法分离 | belief 层退化为「关系有一个模糊印象」 |
| 2 | `H` | 「双方都相信」与「双方联合承诺」不同 `[S59]`；`sharing-is-believing` 改写记忆 | 共生产与偶然收敛不可区分；shared reality 文献全部失效 |
| 3 | `τ` | 「延迟知识」「先承诺后未实现」「后来才发现」全部是 `τ` 排序 | 需要引入独立的时间/事件机制（重复造轮子） |
| 4 | `M` | `AGENTS.md` 第 10 条**要求**这类世界作为 nested Belief | 梦/幻想/计划/反事实污染 `Θ` |
| 5 | `k` | `?` 与 `⊘` 必须分开（`AGENTS.md` 显式 Unknown；Harman/Kripke 的 `?` 状态是教条悖论的舞台） | 显式缺失被压成中性值；共谋维持的沉默与「没想过」混淆 |
| 6 | `g` | 六个值各有独立可检验的处理规则；`ASSUMED` 不可省（否则前提被塞进 `FIRSTHAND`）；`CO_CONSTRUCTED` 是共享实在的 provenance 签名 `[S59]` | 无法判断一条信念该怎么被检验；投射被误当知觉 |
| 7 | `src` | provenance 必须保留（`AGENTS.md`）；二手不变式 `[S65]` | 转述链断裂；「谁说的」丢失 |
| 8 | `m` | 承载透明度错觉、非对称了解错觉、putative secret、对关系的元信念（§4.3） | 这三类现象只能靠 order-2 modal 公式表达，即回到 §3.1 被 REJECT 的框架 |

**逐 (持有者, 内容) 的两个标量**

| 标量 | 不可更少的理由 | 若删除会怎样 |
| --- | --- | --- |
| `Pol(ι, p)` | 教条主义的真实内容是**证据处理策略** `[S7, S6]`；Polarization 使「对 `p` 不利的一切来源都不可信」成为可自洽的理性立场 `[S10]` | 固着只能被表达为「信念很强」或「来源权重低」，二者都无法表达类别级折损 |
| `Rel(ι', p; frame)` | testimony 异质性 `[S63]` + Polarization 的 frame 依赖 `[S10]` | 标量信任塌缩；对极化主体不可表达 |

**加一个派生类集合**（§4.3），**加一个 `M` 枚举**，**加一个 `parent` 指针**。**没有第九个原语，没有 credence 字段，没有 modality 深度。**

### 4.3 派生关系与 alignment 四分类

四个 alignment class 穷尽 `k` 对的 16 种组合，且**完全由记录派生，绝不存储**：

```text
( k_ι , k_ι' )  ∈  { + , − , ? , ⊘ }²            16

SHARED_HOLD     ( +, + )  ( −, − )                    2
SHARED_IGNORE   ( ?, ? )  ( ⊘, ⊘ )  ( ?, ⊘ )  ( ⊘, ? ) 4
ASYMMETRIC      恰有一个 ∈ { +, − }                    8
DIVERGENT       ( +, − )  ( −, + )                     2
--------------------------------------------------------  16 ✓
```

**诚实的自我批评：`ASYMMETRIC` 占 16 中的 8，说明这个维度几乎不携带信息。** 任何真实案例都落进 `ASYMMETRIC`。因此：

1. **`ASYMMETRIC` 必须配一个 motive 位才有信息量。** 至少三值：`UNKNOWN`（未检查是否知晓）/ `UNAWARE`（查明对方不知，且无隐瞒迹象）/ `CONCEALED`（查明对方不知，且有 `Action` 层的未披露行为记录）。这个位是 `ORDINAL | UNKNOWN`，由 `m` + `Behavior` 派生，**不是原语**。
2. `ASYMMETRIC` 的 8 种组合需要按方向（谁持）区分，方向从 `H` 直接得到。
3. **`Claim_ι⊛(p)`**（`H = ι⊛` 的记录）是**唯一**的 pair-level 原语。语义：**以二人名义的联合承诺，是一个第三方可观察的对象**。
   - **不是** `BelievesBoth(p)`（那是两个持有者上的合取，是派生）。
   - **不是** `CommonKnowledge(p)`（**刻意不表示**，§3.2）。
4. `CO_CONSTRUCTED` 的 `g` 值是「`Claim_ι⊛` 曾经存在」的**证据**，但不是它的定义 —— 因为 `CO_CONSTRUCTED` 可以发生在 `ι` 的私人信念上（`ι` 独自被 `ι' ` 的表述改变了记忆 `[S59]`）而不产生 `ι⊛` 记录。

### 4.4 嵌套世界（满足 `AGENTS.md` 第 10 条）

```text
SimWorld( ι , m )  =  { Record : M = m , H = ι }  ∪  closure under parent links
```

- 结构性、非认知性的 `parent` 指向承载它的 ACTUAL 记录（或最近的 ACTUAL 祖先）。
- **一个 `M ≠ ACTUAL` 的记录不得**：
  - 出现在任何 `Θ` 派生量中；
  - 被 `Claim_ι⊛` 引用；
  - 影响 `Rel`（对某来源可靠性的判断只能基于 `M = ACTUAL` 的根据）。
- **它可以**（`CURRENT_ARCHITECTURE.md` §8）：经由 belief / emotion / action-policy 影响现实。
- **深度余量（§3.3）**：`M ∈ {IMAGINED, PLANNED, CF}` 内部允许 order-3（因 mixed-motive 的经验证据 `[S36]`）；`M = ACTUAL` 硬性截断在 order-2。

### 4.5 显式不实现清单

| 不实现 | 理由 | 替代 |
| --- | --- | --- |
| modal logic / Kripke 模型 | §3.1：表达力零增益、假设与目标情境冲突、无法承载 `Φ` 的类型 | `k` 字段 + `m` 字段 |
| public announcement | §3.1：可信-真实-公开假设被违反 | `Disclosure` 的 `Action/Event` |
| common knowledge | §3.2：EXPTIME-complete + 人做不到 | `Claim_ι⊛` |
| 迭代嵌套 > 3 | §3.3 + Miller & Moss 不可递归公理化 | order-2 截断 + 混合动机例外 |
| event model | §3.10：需要完备原子命题语言 | `g` + `m` + `Disclosure` 事件 |
| `credence` / posterior 状态 | §3.4：需已知 observation model（`[S22]` 表明为假） | `k` + `Rel` + `Pol` |
| `d′` / `β` / criterion | §3.5：等方差假设不可检验且已知可疑 `[S20]` | 测量层的 discriminability 注解 |
| POMDP policy solving / reward | §3.7：需 reward 与受控链；一般不可解 | 借更新式；策略交 R06/R09 |
| AGM 完整公理化 / 收缩 | §3.9：把经验判据换成公理判据 | 声明的序偏好先验 |
| doxastic closure | §3.9：它是教条悖论的引擎 `[S9]` | 显式禁令 + `MAPPING_FAILURE` 记录 |
| 标量 `Trust(ι')` | §3.8：`testimony is not a unitary category` `[S63]` | `Rel(ι', p; frame)` |
| 关系级「deception」trait | §3.6：策略性是任务/激励条件化的 `[S31]` | `NonDisclosure` 派生 + `Behavior` |
| 「欺骗」作为规范判断 | §3.6：52.13% 的研究根本没确立规范违反 `[S33]` | 保留 `provenance` 与 `fact status` 分轴 |

### 4.6 可检验的不变式（作为 Case Bank 断言）

这些是**可以逐条被 Case Bank 测伪的**陈述，不是设计许愿：

| ID | 不变式 | 若违反 |
| --- | --- | --- |
| I1 | `⊘` 的记录不被计入任何 belief-derived readout 的分母 | 分母混入「不存在的问题」，违反 `AGENTS.md` 显式 Unknown |
| I2 | 任何 `M ≠ ACTUAL` 的记录不出现在 `Θ` 派生量中 | 梦/幻想污染真实状态（`AGENTS.md` 第 10 条） |
| I3 | `Rel` 从不以标量形式出现 | 违反 testimony 异质性 `[S63]` |
| I4 | 任何 `g = REPORTED` 的记录都有非 `UNKNOWN` 的 `src` | provenance 断裂；二手不变式 `[S65]`` 无法检查 |
| I5 | `NonDisclosure(ι, p)` 为真 ⟹ 存在一条 `ι` 的 `M = ACTUAL` 的 `Disclosure` 记录标记 `p` 为「未放在 `ι' ` 可及范围内」 | belief 层在断言一个没有行为支撑的行为事实 |
| I6 | 任何「他从线索看起来在隐瞒我」的断言带有 `g = INFERRED` 且 `src` 指向线索的 provenance | 把 `[S22]` 的 54% 判读静默升格为 fact |
| I7 | `k` 从不在 belief 层内被 belief 层自动改写（无隐式闭包） | 触发 `Gaultier` 悖论 `[S9]`，且掩盖了教条主义 |
| I8 | 任何「我们意见一致」的 readout 都同时报告其来源：是 `CO_CONSTRUCTED`、`ASYMMETRIC` 的 `m` 失配，还是两条独立收敛的 `k` | 把投射读成知觉（S48 的 indirect accuracy） |
| I9 | 任何「A 比 B 更了解对方」的 readout 都带 `Pol` 与 `Rel` 标注 | 把 motivated inaccuracy 读成低 empathy（S46, S52） |
| I10 | order-2 记录的数量被记录为统计量；超 3 阶的记录必须显式存在 | 无法诊断递归过深或过浅 |

---

## 5. 最小层会做错的硬案例，以及处理它们需要什么

**这是本文件的第三个交付项。** 每个案例：现象 → 最小层的具体失效 → 需要什么 → 最小代价的修法。

### 5-1 共享实在改写了个人的一手记忆（**最贵的漏洞**）

**现象：** `ι` 与 `ι' ` 谈论第三方 `c`。`ι` 把描述调向 `ι' ` 的态度。事后 `ι` **自己**关于 `c` 的一手记忆被改写 `[S59]`。现在 `ι` 的 `FIRSTHAND` 记录事实上是二人共同生产的，但 `ι`（和任何读模型的人）都以为它是独立的一手观察。`sharing-is-believing` 还显示这一改写**只在对互动伴侣有关系动机与认识动机时发生**——即它是关系状态的一个**函数** `[S59]`。

**最小层的具体失效：** `g` 有 `CO_CONSTRUCTED`，但该值**只对 `ι' ` 的信念**可用，对 `ι` 自己关于 `c` 的记录不可用（因为那是 `ι` 的记录，`ι` 自己的 `ι' `-tuned 记忆仍被记为 `FIRSTHAND`）。→ 模型把**共生产误标为个体误知觉**。这会直接导致错误的 Case Bank 映射（把一个关系层现象归档为个体感知问题）。

**需要什么：** 一个 **provenance-sharing / co-construction 标志**，能施加到 `ι` 对**第三方内容**的 `FIRSTHAND` 记录上，且能表达「该改写的触发条件是 `ι` 与 `ι' ` 的互动，强度取决于 `ι' ` 的态度」。

**最小代价修法：** 把 `g` 扩充一值 `FIRSTHAND_TUNED`，其语义是「`ι` 的亲历，但记忆已被 `ι' ` 的表述调谐」。**不加新槽位**，只加一值。代价：它无法表达调谐的**强度**；把强度交给 `g` 旁边的可选 `tuning_src` 指针，或交给 `Pol`（`ι'` 的沟通策略是 `OPEN` 还是 `CONSERTAINING`）——后者**零新增**。

### 5-2 透明度错觉与「我以为你知道」的错误方向

**现象：** `ι` 撒谎时**高估**自己被识破的概率；但**说真话时低估**（估计 63% 的观察者会看出其诚实，实际 73%）`[S41]`。机制是从自身 phenomenology 出发的 anchoring-and-adjustment，且**需要有可感的内部状态作为锚** `[S41]`。策略性情境中同样存在（隐藏偏好者高估泄漏；传达信息者高估对方辨别力）`[S42]`。另有非对称了解错觉：人们认为自己比对方了解自己更深，量级随**特质可观察性**而变 `[S43]`。

**最小层的具体失效：** `m = +` 与 `k_ι'(p) ≠ +` 之间的失配**可以被表示**（I-invariant §4.6 无需改）。但**分类会错**：最小层没有「透明度误差的符号依赖于 `ι` 自身的情感状态」这一维度。→ 任何把「透明 / 不透明」建成**单一参数**的下游 readout 都**必然**错：当 `ι` 平静诚实时，`ι` 的 `m` 系统性**低估**；当 `ι` 高度唤起时，`ι` 的 `m` 系统性**高估**。

**需要什么：** 把透明/不透明做成**逐 `(ι, p, τ)` 的有向失配**，而不是 trait 参���；并把「该失配依赖 `ι` 的内部状态」记为 `Θ` 侧的 Agent 层输入，而非 belief 层参数。

**最小代价修法：** 不加任何 belief 层结构，只需在 §4.3 的 `Meta_Unrealized` readout 上**禁止**跨 `p` 聚合。→ 一条 readout 禁令。`MODEL_HYPOTHESIS`。

### 5-3 准确性作为关系保护机制（motivated inaccuracy）

**现象：** 在不安全型恋爱情侣中，**更低**的判断准确率预测数月后关系**存续**概率更高 `[S46]`。威胁情境下更高准确率预测**亲密感下降** `[S45]`；distinctive emotion **meta-accuracy** 在冲突中与瞬时关系质量**负相关** `[S53]`。同时，偏置与准确是两种不同能力：越负的偏置预测**越准**的追踪 `[S54]`。正性情感结构下，对**负性**情绪的准确率下降而正性不变 `[S55]`。

**最小层的具体失效：** 模型能记录「`ι` 对 `ι' ` 的情绪的信念有偏」。它**没有槽位**记录该偏置的**功能作用**。`Pol` 捕捉机制（为何折损证据），但不捕捉**结果符号**（折损后关系变好还是变坏）。

**需要什么：** 一个**显式的 readout 禁令**，而不是新原语：**禁止**任何形如「belief accuracy ↑ ⇒ relation quality ↑」的单调 readout，除非它以威胁为调节变量。

**最小代价修法：** 把这条写成**架构约束**而非数据字段：任何 accuracy 类 readout 必须在输出中携带 `threat` 调节标记，未携带者标 `MAPPING_FAILURE`。`MODEL_HYPOTHESIS`，但被 `[S44, S45, S46, S53]` 四条独立线索强烈支持。

### 5-4 极化：把「`p` 为假的来源都不可信」当成一个**内容**信念

**现象：** 被极化主体既信 `p`，又信任何提供 `¬p` 证据的来源在 `p` 上不可信；此时 defeat solution **可证失效**，且每个新反例**加强** `p`（disagreement-reinforcement）`[S10]`。降权修正版也被反驳。

**最小层的具体失效：** 若 `Rel` 只有 `Rel(ι', p)` 而无 frame 维度，主体**无法**表达「`ι' ` 在 `p` 上不可信但在同一话题的正向表述上可靠」——而这正是被极化主体的实际结构。→ 模型会把它误读为「`ι' ` 整体不可信」，进而错误地把后续所有关于该话题的**顺向**证据也降权。

**需要什么：** `Rel` 的 **frame 维度**（§2.10），且 `Rel(ι', p; obstructive) = Low` 必须能**独立**于 `Rel(ι', p; conducive)` 取值。

**最小代价修法：** 已包含在本设计内（§2.10 三约束之一）。**这是本设计中唯一一处「文献直接开出实现要求」的地方。** 记录为 evidence-supported design constraint。

### 5-5 合作性不诚实的升级轨迹

**现象：** 重复互动中双方不诚实**相关**，且随回合**递增** `[S23]`；second mover 报出 payoff 结果比等价单人任务高 14%；激励在此起作用而单人任务中不起作用 `[S24]`；亲密关系中不诚实的两个主导动机是 self-protective 与 alleged partner-protective `[S25]`。

**最小层的具体失效：** 逐条 `NonDisclosure(ι, p, τ)` 是逐 `τ` 的，无法表达**轨迹**（"lie more when partners lie" 是关于 `τ` 序列的结构）。另外，若 `m` 只记 `+`/`?` 而不记**「我预期你会配合」**，则无法区分「独立隐瞒」与「共谋」。

**需要什么：** (a) 允许在 `τ` 轴上对 `Disclosure` 事件序列做序列分析（这是 `Action/Event` 层的，不是 belief 层的）；(b) `m` 需要能表达「我预期你对 `p` 也保持 `?`」——即**对他人 stance 的 stance**。

**最小代价修法：** (a) 零新增（`τ` 已在）；(b) 超出 `m` 的当前语义。**`MODEL_HYPOTHESIS` 的候选扩展**：`m` 增一值 `⊕`（我预期对方与我同向），或允许 `m` 的取值来自**另一条记录的 `k`**（即 `m` 指向一个 `(p, ι')` 记录而非枚举值）。后者**更简约**且能表达「我预期你会继续隐藏」。→ 建议 `m` 的第四种实现方式是**引用**而非枚举，但**标 `DEFER`**，因为它会引入记录间的引用环。

### 5-6 规范违反与「不忠」标签

**现象：** 52.13% 的不忠研究未确立信任/排他性规范违反；施加后 emotional infidelity 流行率由 35.23% 降至 17.38%；约 20% 美加成人报告过 CNM，在其中相关行为**不**构成不忠 `[S33]`。

**最小层的具体失效：** 若把 `deceptive` 作为 belief 层的一个**谓词**（而不是 `g` + provenance + `Behavior` 的组合），则该谓词隐含了规范判断，违反 `AGENTS.md`「descriptive / legal / moral / social-desirability 分轴」。

**需要什么：** `g` 与 provenance 只能表达**描述性**事实（说了什么、依据什么、谁可及）。规范违反必须**留在轴上**，不参与 belief 层的任何派生。

**最小代价修法：** 零新增。这条是**对已有设计的确认**，列出是因为它是第二种「必须在架构上显式禁止」的越轴（第一种是 `AGENTS.md` 已有的 descriptive/moral 分离）。

### 5-7 「我曾相信」与「我曾承诺」

**现象：** 某人现在不再相信 `p`，但其**过去的承诺**仍在约束对方（法务与纪实材料中的常见结构）。`AGENTS.md` §8 明确历史可 fork、旧历史不需合并回真相。

**最小层的具体失效：** 若 `Bel` 是**当前状态**（覆盖式），过去信念被删除，就无法表达「他曾经这样说过，所以有理由认为他知道」。若 `Bel` 是纯追加日志，则「当前信念」需要额外定义。

**最小代价修法：** `τ` 已是版本坐标，`k` 是时变记录；只需在数据结构上要求 **`Bel` 是追加日志**，`Current(τ) = latest record per (p, H, M)`。→ 零新增 + 一条显式数据结构要求。`MODEL_HYPOTHESIS`。

### 5-8 双方「共同相信一个假的东西」

**现象：** `ι` 与 `ι' ` 都信 `p`，`p` 为假。二人的 belief 集**互相一致**，世界不一致。合作关系可能在 `p` 上（如「我们相信对方会一直支持我们」）。

**最小层的具体失效：** 最小层**不要求** belief 集一致（§3.9 禁 doxastic closure），因此**技术上**可以表示。但任何自动施加的「一致性检查」都会误报。→ 需显式记录为**架构禁令**：belief 层**不**提供一致性服务。

**最小代价修法：** 零新增 + 一条禁令（与 I7 同族）。`MODEL_HYPOTHESIS`。

---

## 6. 亲密关系文献：朴素 belief 层会**误述**的发现

**这是本文件的第四个（也是对 LHRM 最具操作后果的）交付项。** 「误述」指：naive belief 层不只是「不够精确」，而是会给出一个**方向相反**或**结构性错误**的 readout。

### 6-1 「更了解对方 ⇒ 更好的关系」是错的或可忽略

四条独立线索：

| 来源 | 发现 | 量级 |
| --- | --- | --- |
| `[S44]` | EA 与关系满意度的关联 | 21 研究 / 2,739 人，`r = .134`；**正性**情绪 EA `r = .068`（n.s.） |
| `[S45]` | 伴侣内在状态具威胁性时，EA ↑ 伴随亲密感 ↓ | `b = −.017, β = −.31, t(108) = −3.49`；观察者评分复现 |
| `[S46]` | 不安全型恋爱中，**更低**准确率 ⇒ 数月后关系存续概率更高 | 方向相反 |
| `[S53]` | distinctive emotion **meta-accuracy** 与 meta-perceiver 的关系质量 | 冲突互动中**负相关** |

**→ 朴素层的误述：** 把「双方对彼此的模型更准」当作关系质量的 readout。**这是本文件发现的最严重的误述风险**，因为它是 belief 层最自然的下游用途。

### 6-2 「双方对某内容意见一致」度量的是**投射**，不一定是知觉

- assumed similarity（`b = .40` / `.28`）**超过** empathic accuracy（`b = .29` / `.18`），并在**负性**情感上占优 `[S48]`。
- **indirect accuracy**：因为偏差而碰巧正确 `[S48]`。
- 丈夫系统性**低估**妻子的正性情感（`b = −.30`）`[S48]`。

**→ 朴素层的误述：** 用 `|k_ι(p) − k_ι'(p)|` 当作「理解准确度」。**它在奖励投射。** 修正：区分三条独立来源（`CO_CONSTRUCTED` 收敛 / `m` 失配下的 `ASYMMETRIC` / 两条独立的 `k`），并把 `assumed similarity` 建成一个**可与 `g` 区分**的来源（`INFERRED` + `src` 指向 `ι` 自己的记录，而非 `ι' ` 的）。

### 6-3 准确与正向偏置是**独立且 additive** 的两种收益；正向幻觉是**自我实现**的

- Actor's Perceptions = Partner's Reality + Actor's Illusion；这些幻觉**自我实现**（buffering / transformation / reflected appraisal 三条机制）`[S49]`。
- **准确理解伴侣的自我观很少预测满意度**；系统性的不准确（正向幻觉）预测更高的同期幸福 `[S49]`。
- specific accuracy 与 **global enhancement** 并存 `[S50]`。
- accuracy 与 positive bias 有**独立且 additive** 的正向效应 `[S51]`。
- motivated inaccuracy 是**关系维持**机制 `[S46, S52]`。

**→ 朴素层的误述：** 把「不准确」一律标为误差，并把误差与关系质量挂钩。**误差与关系质量之间没有稳定的负向关系，甚至可能是正向。** 修正：把「准确度」在 readout 层与「关系质量」**解耦**，并把正向/负向偏置建成有向量而非标量。

### 6-4 「我以为你知道」几乎是错的，而且**错的方向随情境反转**

- 透明度错觉在**撒谎时**存在（高估被识破），在**说真话时不存在**（估计 63% vs 实际 73%，方向相反）`[S41]`。
- 非对称了解错觉在个体间与个体内皆存在，且量级**随特质可观察性**而变 `[S43]`。
- 采取伴侣视角反而**更自我聚焦**且**更感透明**，并与感觉更不亲近、关系满意度更低相关 `[S56]`。
- 感到更透明者表达**更不**有效，其伴侣 empathic accuracy 更低 `[S56]`。
- Vorauer & Cameron：朋友相信能辨别 32% 的自我面向，**实际准确率也是 32%**，而参与者相信 **70%** `[S56]`。

**→ 朴素层的误述：** 把「我认为你知道」建模为一个**单调递增的能力或透明度**。现实是一个**逐内容、逐情境、符号可翻转**的失配。修正：§5-2 的 readout 禁令 + `m` 逐记录。

### 6-5 双方「维护一份共同叙事」是**关系状态的核心**，不是附带的

- shared reality 的四阶段：Shared Feelings → Shared Practices → Shared Coordination → Shared Identity `[S58]`。
- SR-G 预测关系与**认知确定性**双重结局 `[S57, S59]`。
- 决定性证据：在感知重叠被**实验威胁**后，高 SR-G 情侣**主动重申** SR-G（更多行为签名、更高潜在语义相似、更多 dyad-specific 指涉），且**基线 SR-G 是唯一预测该重申的伴侣构念** `[S57]`。
- 守住秘密、阻断 shared-reality 形成会**降低幸福感** `[S59]`。
- 甚至细微的话轮中断也会降低 SR 并提升被拒绝感 `[S59]`。
- 每天的 SR 受披露与感知到的建设性回应预测；**epistemic uncertainty（低感知共识）强化负性事件上的 SR 关联** `[S60]`。

**→ 朴素层的误述：** 只存「我们是否同意 `p`」，把 shared reality 当成一个**静态的 pair 属性**。它是一个**被主动维持的过程**，且其维持失败本身有后果。修正：§4.3 的 `Claim_ι⊛` + `g = CO_CONSTRUCTED` + 在 `τ` 轴上对 `Claim` 序列做分析（§5-5(a)）。**`MODEL_HYPOTHESIS`。**

### 6-6 「伴侣会串谋」不是一般事实

- 2,200 对美国夫妻样本中，**策略动机在金融信息分享中不起作用**；坏消息 spillover **更大**（19–22pp vs 7–8pp）；沟通摩擦大时更小；认知摩擦无作用 `[S31]`。
- 策略效应的证据来自**实验室金钱激励、无关系赌注**的任务 `[S23, S24]`。
- 配偶偏好上的信息不对称**确实存在**，且信息干预能减少**性别化**的误感知（对男性尤其），但**不改变**分配决策 `[S32]`。
- **选择性隐瞒内容而非收悉**：掌握私密信息者「不会隐瞒自己收到过信息，而可能策略性隐瞒其内容」`[S29]`；但只有在 **bargaining power 变化未达阈值**时才选择隐瞒 `[S30]`。
- 而且隐瞒是**反馈回路**：50 对夫妻 14 天日记中，自我隐瞒 ↔ 信任互为日层面因果 `[S27]`；putative secret 导致冲突**更高且波动更大** `[S28]`。

**→ 朴素层的误述：** 把「关系中有隐瞒」建成 dyad 特质。修正：§4.3 的 `NonDisclosure` + `m` + `Behavior`，并且**隐瞒必须随 `τ` 变化并与 `Trust` 耦合**。

### 6-7 动机不是单一方向：accuracy motive 可能**稳定**扭曲

- accuracy goals 与 directional goals 是**不同机制** `[S14]`。
- accuracy goals → 更复杂加工；而**更复杂 ≠ 更理性**（accuracy-motivated 者对 dilution effect 反而**更**易感）`[S14]`。
- 有哲学论证称 **accuracy motive 本身**可通过制造更充分的合理化而**稳定并扩大**扭曲 `[S15]`（**哲学论证，非实证发现；不得与 `[S14]` 并列为实证支持**）。

**→ 朴素层的误述：** 把「动机」建成单一方向的偏置标量。修正：至少记录 `Pol` 的两个正交成分——「**折损**（conserving）」与「**搜索/合理化的深度**」——但本设计**只**实现了前者（`Pol`）。后者**不实现**，理由：`[S14]` 表明其效应方向不确定（更复杂可能更偏），且无可靠参数化。记为 `DEFER`（§9）。

### 6-8 守恒不是默认，来源可靠性是条件

- 4 项研究中人们**改变**信念朝向一致的清晰证据，即便它反自身立场；混合证据才产生固着 `[S68]`。
- 保守性可能只是「被试并未把实验材料当作完全可靠」的**规范恰当反应** `[S66]`。
- 共识一致时学习被**放大**、不一致时被**抑制**，由个体特异 anchoring 参数中介 `[S69]`（**发表年份未核实**）。

**→ 朴素层的误述：** 设一个默认保守系数。修正：`Pol` 默认 `OPEN`；`CONSERVING` 必须被**显式标注**且可回溯到 `Rel` 的 frame-conditioned 取值。

### 6-9 递归深度：浪漫 dyad 的深度是 `UNKNOWN`，而这影响所有二阶设计

- 默认一阶；对手建模为短视/零阶；成人二阶 ~65% 且仅在训练末期 `[S34]`。
- 二阶高度脚手架敏感 `[S35]`。
- 收益在二阶饱和；「no additional benefit for third-order theory of mind」`[S36]`。
- 反证：更简单/更竞争的博弈中默认阶次更高且导致次优行为 `[S37]`。
- 平均 1.5 步；人一般无法完成推理 common knowledge 所需的无限递归 `[S38]`。
- 理解的深度远大于自发使用的深度 `[S39]`。

**→ 朴素层的误述：** 或 (a) 假设二人关系里存在稳定的「我们都知道我们在说谎」层，或 (b) 因为「人做不到 common knowledge」就完全不建模二阶（而这会丢掉 6-4 的全部现象）。修正：order-2 **默认开**、order-3 **默认关但允许于想象世界**、common knowledge **不实现**。

---

## 7. Case Bank 候选（本 lane 提议，10 条）

按对 belief 层的判别力排序。每条注明**测什么**、**预期映射**、**预期 `MAPPING_FAILURE`**。

| # | 案例型 | 测什么 | 预期 |
| --- | --- | --- | --- |
| CB-B1 | 一方明确说「我告诉你是因为我不想让你担心」，内容在事实上为真 | `g = REPORTED` + `src` + 动机（`[S25]` 的 partner-protective）vs 描述性不诚实 | 应成功映射；检验 `g` 是否被 `Deceives` 污染 |
| CB-B2 | 双方对同一已发生事件给出**互相矛盾但各自内部一致**的叙述，且双方都真诚 | `DIVERGENT` + I7（无隐式闭包） | 应成功；`?` 归属 vs `−` 归属的区分 |
| CB-B3 | A 知道 B 有秘密**且让 B 以为仍未知**（putative secret） | `NonDisclosure` + I5（须有 `Behavior` 记录支撑） | **预期 MAPPING_FAILURE** 若 `Action/Event` 层尚无 `Disclosure` 类型；这是设计缺口而非 bug |
| CB-B4 | A 谎称「没什么事」，B 事后从第三方得知 | `NonDisclosure` + I6（推断必须带 `g = INFERRED` 与线索 provenance） | 应成功；检验是否把「B 相信 A 在隐瞒」静默升格为 fact |
| CB-B5 | A 在某次谈话中把第三方 C 的行为描述得比实际更糟/更好，随后**自己**的回忆朝该方向偏移 | §5-1 `FIRSTHAND_TUNED` | **预期 MAPPING_FAILURE**：现有 6 值 `g` 无法表达 |
| CB-B6 | 一方平静诚实，另一方却确信「他在隐藏什么」；随后揭示并无隐瞒 | §5-2 透明度错觉在诚实态**反向** `[S41]` | 应成功；检验 readout 是否误把方向性写死 |
| CB-B7 | 一段共 5 手的转述链（甲→乙→丙→丁→戊），每一手都有细微添加 | `g = REPORTED` 链 + `[S65]` 二手不变式 + 链条长度 | 应成功；检验 I4 与链条深度策略 |
| CB-B8 | A 长期「在争议话题上不听 B」，并能指出 B 在该类话题上历史上多次被证实错误 | §5-4 极化 + `Pol = CONSERVING` + frame-conditioned `Rel` | **预期 MAPPING_FAILURE**：若 `Rel` 被实现为标量则不可表示；这是对 I3 的直接测伪 |
| CB-B9 | 双方对关系状态的 `Claim_ι⊛` 与各自私人 `k` 不一致（如「我们都说我们信任对方」但一方 `k = ?`） | `Claim_ι⊛` vs `BelievesBoth` 的区分 | 应成功；这是检验 `ι⊛` 是否被误并入合取的关键案例 |
| CB-B10 | 一方在反事实世界（「如果我们当初…」）里持守一个从未在 ACTUAL 中说出的判断，且该判断**改变了**其在 ACTUAL 中的行动 | `M = CF` + `parent` + I2（不入 `Θ` 派生） | 应成功；直接检验 `AGENTS.md` 第 10 条 |

---

## 8. 明确非主张

1. **不主张**本文件的任何原语（`k` 四值、`g` 六值、`m`、`Pol`、frame-indexed `Rel`、alignment 四类、`Claim_ι⊛`、I1–I10 不变式）已作为关系构念被实证验证。**全部是 `MODEL_HYPOTHESIS`。**
2. **不主张** alignment 四分类是**从**所引研究**推导**出来的。它**映射到**已记录的现象；命名与边界是建模提议。
3. **不主张** order-2 截断对 LHRM 的目标人群**正确**。它是**资源决策**，由三条理由支撑（经验饱和 `[S34, S36, S38]`、形式不可判定 `[S1]`、简约指令），不是关于人的发现。**真实伴侣的递归深度为 `UNKNOWN`。**
4. **不主张** shared reality 的四阶段 `[S58]` 映射到任何 LHRM 状态变量。
5. **不主张**任何 belief 量估计总体参数。Case Bank 是覆盖 / 闭合 / 回归 / 对抗测试。
6. **不主张**欺骗不可检测。**只**主张：在人类参照系中它接近随机（54%，`d ≈ .40`）`[S22]`，故不能静默升格为 fact。
7. **不主张** SDT 的 utility 分析可迁移到关系状态。`[S19, S21]` 的分析对象是知觉 / 医学诊断；本文件只取其**分离原则**。
8. **不主张** POMDP 的 belief state 就是正确对象。只主张其**更新式**可复用。
9. **不主张** Kuhn 主张教条主义；相反 `[S72]` 论证通行解读有误。且本文件**未读** Kuhn 的 "The Function of Dogma"（`[S71]`，`UNVERIFIED_CONTENT`）。
10. **不主张**教条悖论的任一解（defeat solution、Preservation、Conditional Dominance、Polarization 版的修正）**解决了**教条态度是否理性。`[S10]` 明确让步「dogmatism can be the rational attitude for polarized subjects」。
11. **不主张**「accuracy motive 会稳定扭曲」有实证支持（`[S15]` 是哲学论证）。
12. **不主张**「动机深度」应被建模（§6-7 的 defer 项）。
13. **不主张**文献数量或 LLM 一致度构成本文件任何主张的验证。
14. **不主张**本层对任何法律 / 道德 / 社会赞许性评价负责；`deceptive` 记录**不蕴含**规范判断（`[S33]`）。
15. **不主张**「互惠」「一致性」「对齐」「高透明度」是原语；它们是派生 readout。
16. **不主张**本文件与 `PARAMETER_CONVERGENCE_V0_1.md` 的现有候选 `k` 族兼容或冲突——**本 lane 未读该文件**（覆盖缺口，§9-10）。
17. **不主张** `k` 应当是 outright belief。`[S9]` 表明 outright-belief 语义 + doxastic closure 会产生悖论并导出不可接受结论。

---

## 9. 剩余未知

1. **LHRM 的可观察性通道结构。** 哪些构念原则上可被直接观察、哪些只能被报告、哪些只能被推断——项目内不存在这样的列表。`g = FIRSTHAND` 因此无法落地。**这是落地 belief 层的头号阻塞。** 建议与 R07、R03 联合处理。
2. **真实亲密 dyad 的递归心智理论深度。** 未找到专门测量亲密关系中 ToM 阶次的研究。现有证据来自矩阵博弈、谈判、重复博弈。向 romantic dyad 的外推是 `UNKNOWN`。**建议作为 R16 的一个具体实验设计目标。**
3. **二阶 `Rel` 的表示冲突。** `Rel(ι', p; frame)` 既是 ground 家族的一个注解，又是 `Φ` 中的一等内容项。二者在实现层是否碰撞**未知**。
4. **alignment 四分类在 Case Bank 逐句映射下的稳定性。** 四类穷尽 16 种组合（可证），但 `ASYMMETRIC` 占 8 种说明该维度几乎不携带信息。`ASYMMETRIC` 是否需要按方向与 motive 再细分——**未决**。交 R15 / R16。
5. **规范违反作为 deception 判据的建模归属。** 应归属哪一轴、是否允许参与 `deceptive` 判定——**未决**，需 Architect 裁决（§5-6）。
6. **`Observed` 层若为第三方时的建模。** 法务材料中 `Observation` 常来自法官 / 第三方。是否有 `H = ThirdParty` 的必要——**未决**（本文件只给 2-person 保守版本并标 `DEFER`）。与 R11 耦合。
7. **belief 层与 transition law 的接口。** `Belief_t` 如何进入 `X_{t+1} = F(X_t, Action_t, Event_t, Belief_t, …)`——本文件**不**提出任何 `F`。交 R06 / R09。本文件的唯一主张是：`Pol` 与 `Rel` 的存在会**约束** R06 所能提出的 transition law 家族的形式。
8. **transcript 中 testimony chain 的实用长度上限。** `[S65]` 排除了「只经证言被知」，但**未**给出链条长度上限。`UNKNOWN`。
9. **`m` 是否需要拆成「我认为他知道」与「我认为他相信」。** `[S5]` 反对合并；但关系材料中没有廉价操作测试可分。`DEFER`。
10. **`Disclosure` 作为 `Action/Event` 类型的具体形态。** §4.3 的 `NonDisclosure` 依赖它，但本文件**未**设计它（它属于 `CURRENT_ARCHITECTURE.md` §6 的 `Action/Event` 层）。**这是本设计的最大外部依赖。**
11. **coverage 缺口。** 本 lane 未读 `PARAMETER_CONVERGENCE_V0_1.md`、`CONSTRUCT_SCOPE_DIRECTIONALITY.md`、既有报告 A–D、validation fixtures。

---

## 10. 建议状态

**`SUCCESS`**（对 lane `R08` 而言），并附以下限定：

- mission 的每一个 bullet 都得到了有真实指针的覆盖。
- 产生了一条**对 mission 前提的实质性更正**（C1：不存在「Kuhn's dogmatism paradox」，规范对象是 Kripke–Harman paradox）。
- 产生了一个**可落地且简约**的 belief 层设计（8 槽位 + 2 标量 + 4 派生类 + 1 枚举 + 1 指针），并给出 10 条**可证伪**的不变式。
- 产生了一份**强制的过度工程审计**，含 3 项 `REJECT`（modal logic、common knowledge、后验作为状态）、2 项 `REUSE-EQUATION-ONLY`（POMDP、AGM）、1 项 `DEFER`（event model）。
- 产生了一份**naive layer 误述清单**（§6，9 项），其中 4 项给出**方向相反**的 readout。

**限定（诚实记录）：**
1. **`[S69]` 的发表年份未核实**（PMC 编号暗示为近期）。写入前必须复核，否则按 `UNKNOWN_AS_OF` 处理。
2. **`[S71]`（Kuhn）未读**，本文件任何主张都不基于它。
3. **head-of-list 阻塞**是 §9-1（可观察性通道表不存在）与 §9-10（`Disclosure` 未设计）。**本设计不能在这两项解决前进入表示测试。**
4. 本 lane 未读项目内既有报告 A–D，故**不主张**跨 lane 一致性或冲突。
5. 本文件是 `RESEARCH_CANDIDATE`，**不是** canonical。采纳任何部分都需要 reviewed 的 Human/Architect 决策。

**对 manifest 的状态建议：** lane `R08` → `SUCCESS`；报告文件状态 `RESEARCH_CANDIDATE`；Wave 2 中 `A01`（证据质量）应复核 `[S69]` 年份与 `[S71]` 的 `UNVERIFIED_CONTENT` 标记；`A03`（可证伪性）应把 §4.6 的 10 条不变式与 §7 的 10 条 Case Bank 候选作为具体测伪清单。

---

## 11. 引用列表

> `evidence_type` 与 `strength` 的定义见 `00_CHILD_CONTRACT.md` §3。核实日期：2026-09-27。

**[S1]** Stanford Encyclopedia of Philosophy. "Dynamic Epistemic Logic." https://plato.stanford.edu/entries/dynamic-epistemic/ — `CITED_PRIMARY` · high
**[S2]** van Benthem, J., van der Hoek, W., & Kooi, B. (2010). *Dynamic Epistemic Logic*. Synthese Library 337. Springer. https://link.springer.com/book/10.1007/978-1-4020-5839-4 — `CITED_SECONDARY` · med
**[S3]** van Eijck, J. "Dynamic Epistemic Logics" (ch. in [S2]). https://staff.fnwi.uva.nl/d.j.n.vaneijck2/papers/13/pdfs/del.pdf — `CITED_PRIMARY` · high
**[S4]** Internet Encyclopedia of Philosophy. "Dynamic Epistemic Logic." https://iep.utm.edu/dynamic-epistemic-logic/ — `CITED_SECONDARY` · med
**[S5]** Stanford Encyclopedia of Philosophy. "Epistemic Paradoxes" (T. Sorensen). §6.2 "Dogmatism paradox: A puzzle about losing knowledge." https://plato.stanford.edu/entries/epistemic-paradoxes/ — `CITED_PRIMARY` · high
**[S6]** Kripke, S. (2011). "Two Paradoxes of Knowledge." In *Philosophical Troubles*, vol. 1, pp. 27–51. Oxford University Press.（dogmatism 部分 pp. 39–49）— `CITED_SECONDARY`（经 [S5][S11][S12]）· high
**[S7]** Salow, B. (2024). "Fallibility and Dogmatism." https://ora.ox.ac.uk/objects/uuid:5a0dd404-6e48-40ca-a1f4-141aaab57c3e/files/rtt44pp612 · PhilArchive LAJKSAL — `CITED_PRIMARY` · high
**[S8]** Lajevardi, K. "Kripke and the dogmatism paradox." https://philarchive.org/archive/LAJKAT — `CITED_PRIMARY` · high
**[S9]** Gaultier, B. "…a paradox of belief." INQUIRY 7. https://www.zora.uzh.ch/server/api/core/bitstreams/08db41ef-8112-4307-bdd1-1156e73f307f/content — `CITED_PRIMARY` · high
**[S10]** "The Polarization Paradox." *Episteme* (2025). https://www.cambridge.org/core/journals/episteme/article/polarization-paradox/D8AABC387963BC79FA3404A4C5945F76 — `CITED_PRIMARY` · high
**[S11]** Biro, J. (2022/2024). "'Dogmatism' and Dogmatism." *Episteme* 21(2), 540–544. https://www.cambridge.org/core/journals/episteme/article/dogmatism-and-dogmatism/3BC37E2A4CE689A496A24CA7DC6D7568 — `CITED_PRIMARY` · high
**[S12]** Sharon, A. (2015). "On synchronic dogmatism." *Synthese*. https://link.springer.com/article/10.1007/s11229-015-0715-3 — `CITED_PRIMARY` · high
**[S13]** Borges, M. (2013). "Dogmatism repuzzled." *Philosophical Studies* 148, 307–321. https://philarchive.org/archive/BOROSD-2 — `CITED_PRIMARY` · med
**[S14]** Kunda, Z. (1990). "The Case for Motivated Reasoning." *Psychological Bulletin* 108(3), 480–498. https://fbaum.unc.edu/teaching/articles/Psych-Bulletin-1990-Kunda.pdf — `CITED_PRIMARY` · high
**[S15]** "Convincing ourselves: accuracy motives and rationalization." *Synthese* (2025). https://link.springer.com/article/10.1007/s11229-025-05259-1 — `CITED_PRIMARY` · med（**哲学论证，非实证发现**）
**[S16]** Kaelbling, L. P., Littman, M. L., & Cassandra, A. R. (1998). "Planning and acting in partially observable stochastic domains." *Artificial Intelligence* 101(1–2), 99–134. doi:10.1016/S0004-3702(98)00023-X — https://people.csail.mit.edu/lpk/papers/aij98-pomdp.pdf — `CITED_PRIMARY` · high
**[S17]** Littman, M. L., Cassandra, A. R., & Kaelbling, L. P. (1994). "The Witness Algorithm: Solving Partially-Observable Markov Decision Processes." Brown CS TR CS-94-40. https://cs.brown.edu/research/pubs/techreports/reports/94/cs94-40.pdf — `CITED_PRIMARY` · high
**[S18]** Bazik, J., Littman, M. L., Cassandra, A. R., & Kaelbling, L. P. Brown CS TR CS-95-19. https://cs.brown.edu/research/pubs/techreports/reports/CS-95-19.html — `CITED_SECONDARY` · med
**[S19]** Landy, M. S. (2024). "Signal detection theory." NYU Math Tools. https://www.cns.nyu.edu/~eero/math-tools24/Handouts/sdtchapter.pdf — `CITED_PRIMARY` · high
**[S20]** Stanislaw, H., & Todorov, N. (1999). "Calculation of signal detection theory measures." *Behavior Research Methods* 31, 137–149. https://www.jessicagrahn.com/uploads/6/0/8/5/6085172/stanislawtodorovdprim1999.pdf — `CITED_PRIMARY` · high
**[S21]** "Utilizing Signal Detection Theory." PMC4304641. https://pmc.ncbi.nlm.nih.gov/articles/PMC4304641/ — `CITED_PRIMARY` · med
**[S22]** Bond, C. F., & DePaulo, B. M. (2006). "Accuracy of Deception Judgments." *Personality and Social Psychology Review* 10(3), 214–234. doi:10.1207/s15327957pspr1003_2 — https://journals.sagepub.com/doi/10.1207/s15327957pspr1003_2 · full PDF: http://www.communicationcache.com/uploads/1/0/8/8/10887248/accuracy_of_deception_judgments.pdf — `CITED_PRIMARY` · high
**[S23]** Leib, M., Köbis, N., Soraperra, I., Weisel, O., & Shalvi, S. (2021). "Collaborative dishonesty: A meta-analytic review." *Psychological Bulletin* 147(12), 1241–1268. doi:10.1037/bul0000349 — https://pure.mpg.de/rest/items/item_3377548/component/file_3388432/content — `CITED_PRIMARY` · high
**[S24]** Weisel, O., & Shalvi, S. "(Dis)honesty in collaborative settings: A meta-study." UvA-DARE, ch. 5. https://pure.uva.nl/ws/files/54463652/Chapter_5.pdf — `CITED_PRIMARY` · high
**[S25]** Mazzini, R., Malfilâtre, A. L., Lilleholt, L., Power, S. A., & Zettler, I. (2025). "Dishonesty in Romantic Relationships: A Framework of Forms, Content, Dominant Motives, and Consequences." https://exa.ai/library/publication/xszmd63kv40 — `CITED_PRIMARY` · med
**[S26]** Fincke, T. L., & Zeelenburg, I. M. (2019). "Love, Lies, and Money: Financial Infidelity in Romantic Relationships." *Journal of Consumer Research* 47(1), 1–. https://academic.oup.com/jcr/article/47/1/1/5610529 — `CITED_PRIMARY` · high
**[S27]** Uysal, A., et al. (2012). "The reciprocal cycle of self-concealment and trust in romantic relationships." *European Journal of Social Psychology* 42(6), 844–851. https://www.academia.edu/48333184/The_reciprocal_cycle_of_self_concealment_and_trust_in_romantic_relationships — `CITED_PRIMARY` · high
**[S28]** Slapac, B. J., & Moretz, M. L. "Discovering Secrets in Romantic Relationships." NCA. https://www.natcom.org/publications-library/discovering-secrets-romantic-relationships/ — `CITED_PRIMARY` · med
**[S29]** Anderberg, D., Cassidy, R. N., Dam, A., Janssens, W., Morsink, K., & van Veldhoven, A. (2024). "Keeping the peace whilst getting your way: Information, persuasion and intimate partner violence." https://exa.ai/library/publication/sjrdv14q7ck — `CITED_PRIMARY` · med
**[S30]** Ashraf, N. "Bargaining Power and Income Concealing between Spouses in India." AEA (2014). https://www.aeaweb.org/conference/2014/retrieve.php?pdfid=496 — `CITED_PRIMARY` · med
**[S31]** Delavande, A., Koşar, G., & Zafar, B. (2025). "Information Spillovers Within Couples: Evidence from a Sequential Survey of Spouses." https://exa.ai/library/publication/bnb4pgwv5g2 — `CITED_PRIMARY` · med
**[S32]** "Private lives: experimental evidence on information completeness in spousal preferences." *Journal of the Economic Science Association*. https://www.cambridge.org/core/journals/journal-of-the-economic-science-association/article/abs/private-lives-experimental-evidence-on-information-completeness-in-spousal-preferences/CA87AF7D4C687EA5FAC39D666637E891 — `CITED_PRIMARY` · med
**[S33]** Warach, B., Bornstein, R. F., Gorman, B. S., & Moyer, A. E. (2024). "The current state of affairs in infidelity research: A systematic review and meta-analysis." https://exa.ai/library/publication/k8s4n220k0w — `CITED_PRIMARY` · med
**[S34]** Hedden, T., & Zhang, J. (2002). "What do you think I think you think? Strategic reasoning in matrix games." *Cognition* 85(1), 1–36. doi:10.1016/S0010-0277(02)0549-8 — https://www.sciencedirect.com/science/article/abs/pii/S0010027702000549 — `CITED_PRIMARY` · high
**[S35]** Meijering, B., van Rijn, H., Taatgen, N., & Verbrugge, R. "I Do Know What You Think I Think: Second-Order Theory Of Mind In Strategic Games Is Not That Difficult." AAMAS paper 985. https://www.ai.rug.nl/~niels/publications/paper985.pdf — `CITED_PRIMARY` · high
**[S36]** Verheij, F., van der Velden, H., & Verbrugge, R. (2014). "The effectiveness of higher-order theory of mind in negotiations." AAMAS. https://www.ai.rug.nl/%7Everheij/publications/pdf/raom2014.pdf — `CITED_PRIMARY` · high
**[S37]** Bornstein, G. (2010). "Levels of theory-of-mind reasoning in competitive games." *British Journal of Developmental Psychology*. doi:10.1002/bdm.717 — `CITED_PRIMARY` · med
**[S38]** "Theory of mind in the Mod game: An agent-based model of strategic reasoning." CEUR vol. 1283, paper 18. https://ceur-ws.org/Vol-1283/paper_18.pdf — `CITED_PRIMARY` · high
**[S39]** Vega, J. A., Wheeler, B. J., & Bova, N. (2007). "Thinking About Me, You, and Them: Understanding Higher-Order Propositional Attitudes." https://exa.ai/library/publication/whyw87dldff — `CITED_PRIMARY` · med
**[S40]** Perner, J., & Wimmer, H. (1985). *Journal of Experimental Child Psychology* 39(3), 437–471. doi:10.1016/0022-0965(85)90051-7；Wimmer, H. (1983). *Cognition* 13(1), 103–128. doi:10.1016/0010-0277(83)90004-5 — `CITED_SECONDARY` · med
**[S41]** Gilovich, T., Savitsky, K., & Medvec, V. H. (1998). "The illusion of transparency: Biased assessments of others' ability to read one's emotional states." *JPSP* 75(2), 332–346. doi:10.1037/0022-3514.75.2.332 — https://cpb-us-e1.wpmucdn.com/blogs.cornell.edu/dist/b/6819/files/2015/12/GiloSavtskyMDVC.98-copy-1ei0u8q.pdf — `CITED_PRIMARY` · high
**[S42]** Gilovich, T., Medvec, V. H., & Savitsky, K. (2000). "The Illusion of Transparency in Negotiations." *Negotiation Journal*. https://onlinelibrary.wiley.com/doi/10.1111/j.1571-9979.2003.tb00771.x — `CITED_PRIMARY` · med
**[S43]** Steffel, M., Väljataga, E., Malle, B. F., & Nomura, Y. "A biased accommodation account" (on the illusion of asymmetric insight). PhilArchive STEETI-4. https://philarchive.org/archive/STEETI-4 — `CITED_PRIMARY` · high
**[S44]** Sened, H., Lavidor, O., Bar-Kalifa, E., Rafaeli, A., & Ickes, W. (2017). "Empathic accuracy and relationship satisfaction: A meta-analytic review." *Frontiers in Psychology* 8:861. https://pubmed.ncbi.nlm.nih.gov/28394141/ — `CITED_PRIMARY` · high
**[S45]** Ickes, W., Oriña, M. M., & Simpson, J. A. "When Accuracy Hurts, and When It Helps: A Test of the Empathic Accuracy Model in Marital Interactions." *JPSP*. https://mavmatrix.uta.edu/cgi/viewcontent.cgi?article=1031&context=psychology_facpubs — `CITED_PRIMARY` · high
**[S46]** Simpson, J. A., Oriña, M. M., Ickes, W., & Blackstone, J. (2003). "Eye of the Beholder: The Individual and Dyadic Contributions of Empathic Accuracy and Perceived Empathic Effort to Relationship Satisfaction." *Family Psychology* 26(2), 236–. https://www.apa.org/pubs/journals/releases/fam-26-2-236.pdf — `CITED_PRIMARY` · high
**[S47]** Kilpatrick, S. D., Bissonnette, J. J., & Rusbult, C. E. (2002). "Empathic accuracy and accommodative behavior among newly married couples." *Personal Relationships*. https://faculty.wcas.northwestern.edu/eli-finkel/documents/79_KilpatrickBissonnetteRusbult2002_PersonalRelationships.pdf — `CITED_PRIMARY` · high
**[S48]** "Couples' Perceptions of Each Other's Daily Affect: Empathic Accuracy, Assumed Similarity, and Indirect Accuracy." PMC6512343. https://pmc.ncbi.nlm.nih.gov/articles/PMC6512343/ — `CITED_PRIMARY` · high
**[S49]** Murray, S. L., Holmes, J. G., & Griffin, D. W. (1996b). "The self-fulfilling nature of positive illusions in romantic relationships: Love is not blind, but prescient." *JPSP* 71, 1155–1180. https://faculty.washington.edu/jdb/345/345%20Articles/Chapter%2011%20Murray%20et%20al.%20%281996%29.pdf — `CITED_PRIMARY` · high
**[S50]** Murray, Holmes & Griffin (1996a) *JPSP* 70, 79–98；Neff, L. A., & Karney, B. R. (2002) *J. Personality* 70, 1079–1112；Neff & Karney (2005) *JPSP* 88, 480–497 — `CITED_SECONDARY` · med
**[S51]** Bosson, J. K. (2010). "The unique and combined benefits of accuracy and positive bias in relationships." *Personal Relationships* 17(3). https://onlinelibrary.wiley.com/doi/10.1111/j.1475-6811.2010.01282.x — `CITED_PRIMARY` · med
**[S52]** Royle, C., et al. (2023). "When only one of us thinks the discussion went well: How positive illusions impact relationship satisfaction following disagreements." https://exa.ai/library/publication/qc1n3tzxz6l — `CITED_PRIMARY` · med
**[S53]** Tissera, H., Heyman, J. L., & Human, L. J. (2022). "Do People Know How Their Romantic Partner Views Their Emotions? Evidence for Emotion Meta-Accuracy and Links with Momentary Romantic Relationship Quality." *PNAS*. https://pmc.ncbi.nlm.nih.gov/articles/PMC9903246/ — `CITED_PRIMARY` · high
**[S54]** "When Bias and Insecurity Promote Accuracy." *Personality and Social Psychology Bulletin* (2012). https://sage.cnpereading.com/doi/10.1177/0146167211432764 — `CITED_PRIMARY` · med
**[S55]** Dutra, N., West, E., Impett, E. A., Oveis, K., Kogan, D. M., Keltner, D., & Gruber, A. H. (2014). "Mania symptoms predict biased emotion experience and perception in couples." http://gruberpeplab.com/pdf/2014_Dutra.West.Impett.Oveis.Kogan.Keltner.Gruber_ManiaEmpathicAccuracyCouples.pdf — `CITED_PRIMARY` · med
**[S56]** Winczewski, L. A., et al. (2017). "Dyadic Effects of Feeling Transparent" (doctoral dissertation). https://exa.ai/library/publication/mwlx3shqtwp — `CITED_SECONDARY` · med
**[S57]** Rossignac-Milon, M., Bolger, N. P., Zee, K. S., Boothby, E. J., & Higgins, E. T. (2021). "Merged minds: Generalized shared reality in dyadic relationships." *JPSP* 120(4), 882–911. doi:10.1037/pspi0000266 — `CITED_PRIMARY` · high
**[S58]** Rossignac-Milon, M., & Higgins, E. T. (2018). "Epistemic companions: shared reality development in close relationships." *Current Opinion in Psychology* 23, 66–71. doi:10.1016/j.copsyc.2018.01.001 — `CITED_PRIMARY` · high
**[S59]** Higgins, E. T., Rossignac-Milon, M., Jones, M. C., Uuk, S., Koenig, J. D., & Bryant, G. (2021). "Shared Reality: From Sharing-Is-Believing to Merging Minds." *Current Directions in Psychological Science*. https://cuhigginslab.com/wp-content/papercite-data/pdf/higginsetal2021b.pdf — `CITED_PRIMARY` · high
**[S60]** Uuk, S., Boothby, E. J., Hughes, J., Hasselman, F., & Higgins, E. T. (2021). "Responsiveness processes and daily experiences of shared reality among romantic couples." *JPSP*. https://journals.sagepub.com/doi/10.1177/02654075211017675 — `CITED_PRIMARY` · med
**[S61]** Echterhoff, G., & Higgins, E. T. (2017). "Creating shared reality in interpersonal and intergroup communication: the role of epistemic processes and their interplay." *European Review of Social Psychology* 28(1), 175–226. doi:10.1080/10463283.2017.1333315；Hardin, C. D., & Higgins, E. T. (1996). "Shared reality: How social verification makes the subjective objective." *Handbook of Motivation and Cognition* 28–84. Guilford. — `CITED_SECONDARY` · med
**[S62]** Stanford Encyclopedia of Philosophy. "Epistemological Problems of Testimony." (2021) https://plato.stanford.edu/Entries/testimony-episprob/ — `CITED_PRIMARY` · high
**[S63]** Lackey, J. (2006). "Knowing from Testimony." *Philosophy Compass* 1(5), 432–448. doi:10.1111/j.1747-9991.2006.00035.x — https://realseekerministries.wordpress.com/wp-content/uploads/2022/12/4.2-lackey-2006.pdf — `CITED_PRIMARY` · high
**[S64]** Coady, C. A. J. (1992). *Testimony: A Philosophical Study*. Oxford University Press.；Coady (1998). "The epistemology of testimony." *BJPS*. — `CITED_SECONDARY` · high
**[S65]** Fricker, E. (2005). "Knowledge from Trust in Testimony is Second-Hand Knowledge." https://aristotle.rutgers.edu/joomlatools-files/docman-files/Fricker.pdf — `CITED_PRIMARY` · med
**[S66]** "Conservatism in Belief Revision and Participant Skepticism." https://escholarship.org/content/qt79b7w6h3/qt79b7w6h3_noSplash_c15951d18f7e49039346f461cedf6f70.pdf — `CITED_PRIMARY` · high
**[S67]** Nickerson, R. S. (1998). "Confirmation bias: A ubiquitous phenomenon in many guises." *Review of General Psychology* 2(2), 175–220. doi:10.1037/1089-2680.2.2.175 — `CITED_PRIMARY` · med
**[S68]** Tannenbaum, M. B., Bielinski, E. M., & Fedor, A. P. (2018). "Do beliefs yield to evidence? Examining belief perseverance vs. change in response to congruent empirical findings." *Journal of Experimental Social Psychology* 86, 105–116. https://www.sciencedirect.com/science/article/abs/pii/S0022103118304529 — `CITED_PRIMARY` · med
**[S69]** "Anchored and Propagated Updating Within Pseudoscientific Belief Systems." https://pmc.ncbi.nlm.nih.gov/articles/PMC12955757/ — `CITED_PRIMARY`（摘要）· med-low — **发表年份与期刊 `UNKNOWN_AS_OF`，写入前须复核**
**[S70]** Audi, R. (2006). "Monitoring and Anti-Reductionism in the Epistemology of Testimony." *Mind* 115. doi:10.1111/j.1933-1592.2006.tb00586.x — `CITED_SECONDARY` · med
**[S71]** Kuhn, T. S. "The Function of Dogma in Scientific Research." https://classes.matthewjbrown.net/teaching-files/hps/kuhn-dogma.pdf — **`UNVERIFIED_CONTENT`**（抓取截断，未读）· none — **本文件任何主张都不基于它**
**[S72]** "Normal science: not uncritical or dogmatic." *Synthese* (2024). doi:10.1007/s11229-024-04527-w — https://link.springer.com/article/10.1007/s11229-024-04527-w — `CITED_PRIMARY` · high
