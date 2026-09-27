# R3-G construct-bearing ablation mini-benchmark 设计 v0.1

- work_coordinate: `youling/lhrm#30@round3-adjudication-implementation-v1`
- child: `G`（Round-3 build child，Track R3-G）
- 依据: `ARCHITECT_ADJUDICATION_V1` 的 **X-9**、**X-5**、**X-14**、**§C item 4**、**§C item 6**、**§C item 7**，
  C-P1（ACCEPT WITH MODIFICATION）、C-P2、C-P5、C-P6
- 状态: **DESIGN ONLY / FIXTURE NOT CREATED / NOT FROZEN / NOT RUN**
- 与 `docs/foundation/VALIDATION_GATES_V0_2.md`（child `C`）的关系: **本文不复制该文件的门定义**，
  只引用 `ARM-ABL-1` / `GATE_COVERAGE` / `GATE_MINIMALITY` / `HD-ST-1` / `HD-D10` / 5 值处置，
  避免出现第二份 SSOT。
- 来源侧结论: 见同分支 `docs/research/R3_G_DYAD_CLASS_SOURCE_PLAN_v0.1.md`（本文 §6 引用其 rights 词表与探针）。

> 未创建任何 fixture 文件，未冻结任何版本，未运行任何 arm，未执行任何 mapping。

---

## 1. 为什么需要它（X-9 的直接后果）

X-9 逐字：

> Fixture 001 is a test of **fact/observation/belief/action/history/provenance representation and mapping failure
> semantics**, not a valid test of all eight relationship-state constructs.

Fixture 001 的 core dyad 是 `Miss Z. Carty <-> her 2020 line manager / employer-side human contact`，
26 个原子事实是排班 / 停业 / 未付薪 / CAB / 申诉等**机构性事实**。
因此：

- 用 Fixture 001 主张「八项 basis 必要」= **范畴错误**；
- C 轨 `GATE_MINIMALITY` 的前置写着「**必须**有 construct-bearing 材料。未有 ⇒ 全部 §11 构念判 `UNTESTABLE`，
  处置 `HOLD` / `BENCHMARK_NOT_BUILT`」。**该前置今天不满足。**
- 本文是满足该前置的**设计与来源计划**，不是该 benchmark 本身。

## 2. 与三个既有冻结件的关系（明确不同）

| 维度 | Fixture 001 | Fixture 002 | Fixture 003 | **本 benchmark** |
|---|---|---|---|---|
| 测试对象 | fact/observation/belief/action/history/provenance 表示 + mapping-failure 语义 | 同上（加 belief-revision） | 同上（加隐喻 / 嵌套引语 / 阅读者-作者分离） | **构念是否必要**（necessity / redundancy） |
| core dyad | 雇主↔雇员（机构性） | 夫妻（O. Henry） | 夫妻（StoryCorps） | **至少 2 个 dyad，其中 1 个为 `KIN`**、1 个为非亲缘 |
| 双方各自报告 | 弱（单方陈述 + 机构记录） | 弱（对话式叙事） | **是**（DP/AP 交替） | **是（硬要求）** |
| 权利底座 | gov.uk OGL | public domain | `HUMAN_REVIEW_REQUIRED` / pointer-only | **要求 `RIGHTS_CLEARED_AI_OK`；排除 Fixture 003 底座** |
| 是否预映射 | 禁止（§2.6） | 禁止 | 禁止（§3.1） | **禁止**；另加 **probe 文件封存**（§4.2） |

**明确不做**：不复用 `L1-003`（Magi）作 ablation 材料。理由：它已被冻结为 Fixture 002 且已被用于 belief 追踪；
把它同时当 necessity 证据会使**同一个 `SCHEMA_PIN` 下的计数被两种用途污染**，并进一步触发 §7 的不可比较性问题。
需要它时，以**同作品的其他版本**（或同公共领域层级的替代作品）另立 `benchmark_id`。

---

## 3. 「load-bearing」的可操作定义

**定义（预注册，不可事后改）**：

> 构念 `k` 在材料中 **load-bearing**，当且仅当存在至少一个 `RELATION_RELEVANT` 单位 `u`，
> 使得在 `ARM-W(−k)`（withheld arm）中 `u` 的表示发生**可记录的降级**，且该降级**不能**由
> 「另一个候选有向构念 + Belief + Action/Event + PairState + Constraint + Environment」**无损**恢复。

两条设计后果，缺一不可：

1. **只要该单位是 Action/Event 或 BeliefState 就能表示** ⇒ `k` 不 load-bearing。
   （所以材料必须是**关系状态命题**，不是行为记录，也不是某人的看法。）
2. **只要存在无损的派生式**（`Mutuality_k` / `Asymmetry_k` / 其它坐标的函数）⇒ `k` 判 `DERIVE` 候选，不是 primitive。
   这与 C 轨 5 值处置里的 `MERGE`（同义）**必须分开**。

**每个构念的结论不是布尔值，而是一个 5 值向量**（`load_bearing_status`），
benchmark **必须**把整个 8 维向量publish出来，并且**允许其中若干格为空**：

| 值 | 含义 |
|---|---|
| `WITNESSED` | baseline 覆盖 + withheld 后 ≥1 单位降级 ⇒ necessity 的必要条件成立 |
| `COVERED_BUT_NOT_WITNESSED` | baseline 覆盖，但 withheld 后**零降级** ⇒ **被覆盖且不必要**（这正是本 benchmark 要能表达的态） |
| `COVERED_BUT_NOT_APPLICABLE_IN_MATERIAL` | 该构念在这批 dyad 上按规则不适用 ⇒ 记 `HOLD` / `APPLICABILITY`，**不**记 necessity |
| `NOT_COVERED` | baseline 即无法合法表示 ⇒ 覆盖失败，先诊断，**不**直接 `REJECT`（C-P1 逐字） |
| `UNTESTABLE_NO_RIGHTS_CLEAR_SOURCE` | 权利侧不满足前置 ⇒ `HOLD` / `ACCESS_OR_RIGHTS` |

**「诚实报告哪些不是」的制度化**：设计**故意不追求** 8/8 全 `WITNESSED`。
如果跑出来 8/8，本设计是可疑的（说明材料被按构念反向定制，犯了 C-P2 §6.3.1 第 2 条禁的那件事）。

## 4. 两条臂如何在**同一批单位**上跑（这是覆盖/最小性可分离的机制）

C 轨 `ARM-ABL-1` 已规定 baseline arm 与 withheld arm 读同一份冻结输入。
本文补上**让两者可分离的三条具体规定**：

### 4.1 单位集逐字节相同

`ARM-BASE` 与 `ARM-W(−k)` 使用**同一份** `MATERIAL` 文件（同一 `material_version` hash、同一 `schema_pin`）。
因此覆盖计数在两臂之间**直接可比**，withheld 后覆盖数的下降是**代价度量**，不是失败。

### 4.2 两份冻结文件，`PROBE` 封存

| 文件 | 内容 | 是否含构念名 | 谁能看 |
|---|---|---|---|
| `MATERIAL` | 原子单位（含 `faithful_paraphrase`、`source_anchor`、`speaker_ref`、时间轴、敏感标记） | **否**（延续 Fixture 001 §2.6 / Fixture 003 §3.1 的禁预映射） | mapping executor 可看 |
| `PROBE` | `unit_id → intended_probe_construct` + `design_intent` + `structural_role` | 是 | **封存**；只在 Architect 做诊断时开封 |

**为什么必须拆**：`WITNESSED` 的定义要求「知道哪个单位在测哪个构念」。
若这一信息与材料同文件发布，mapping executor 在 withheld arm 里就等于**被告知了答案**——
`W(−k)` 只会退化成「把 `k` 从答案里删掉」，降级变成同义反复。

**因此硬规则**：
- `PROBE` 与 `MATERIAL` 分文件、分 hash、分发布；
- mapping executor 在完成 `ARM-BASE` 与 `ARM-W(−k)` 之前**不得**接触 `PROBE`；
- `BENCHMARK_OWNER`（构造材料）**不得**是 mapping executor（与 C-P2 §6.3.1 第 3 条一致）；
- 违反上述任一条 ⇒ 该次 run 记 `RUN_VOID_CONTAMINATED`，重跑。

### 4.3 降级的预注册分类

对每个 `(unit, withheld construct)` 记一条 `ablation_record`，`degradation_kind` 取值**封闭**为 5：

| `degradation_kind` | 判据（可由第三方复核） | 是否构成 witness |
|---|---|---|
| `NONE` | 无 `k` 时单位仍得到**同一落点类**、同一方向性、同一 provenance 强度 | 否 |
| `LOSSY_DIRECTIONAL` | 只剩**无向/无版本**的部分（例：只能说「两人之间信任低」，不能说 `Trust(A→B)` 与 `Trust(B→A)` 不同） | **是** |
| `LOSSY_FUSION` | 只能靠**过载另一个构念**才说得出来（例：把 `Caregiving` 读进 `Dedication`） | **是**（且**同时**是 `redundancy hole` 证据） |
| `LOSSY_PROVENANCE` | 不确定性 / 归属层还在，但状态主张没了（例：只能说「A 觉得…」，说不了被主张的东西） | **是** |
| `UNRECOVERABLE` | 无 `k` 即无合法落点 ⇒ withheld arm 出现 `MAPPING_FAILURE` | **是** |

`witness_qualifies = (kind ≠ NONE) ∧ (unit.relation_relevance_assertion = RELATION_RELEVANT)`。

**`LOSSY_FUSION` 的双刃性必须写进台账**：同一单位可以**既**为 `k` 提供 necessity witness，
**又**为 `(k, k')` 提供 redundancy 证据。这两件事不能塞进同一个字段，
否则 `MERGE` 与 `KEEP` 的判定会互相污染。台账分两列：`necessity_evidence_ref` 与 `redundancy_evidence_ref`。

---

## 5. 单位 schema

`MATERIAL` 字段（**全部必填**，无默认）：

| 字段 | 说明 |
|---|---|
| `unit_id` | 稳定 id；一经发布不再复用 |
| `benchmark_id` · `material_version` | 内容 hash（`MATERIAL` 文件级） |
| `schema_pin` | `{tree_sha, canonical_files[], retrieval_date}`（§7） |
| `source_ref` | `PERSISTENT_ID`（DOI / PMCID / NCN）+ 访问日期 |
| `source_anchor` | 短锚点，**不得**是全文偏移（与 Fixture 003 的 `SC/...` 同形） |
| `dyad_id` · `dyad_class` · `gender_composition` · `stage` | 取值引用 `HD-ST-1`，本文不复制定义 |
| `t_index` · `t_label` | 离散时间点；`recording_time` 与 `event_time` 严格分开（Fixture 003 §3.2） |
| `speaker_ref` · `reported_speaker_ref` | 双方报告时**必须**能区分是谁说的 |
| `unit_type` | 沿用 Fixture 003 的九值枚举 |
| `fact_or_narrative_status` | 沿用 Fixture 003 的六值枚举 |
| `faithful_paraphrase` | 忠实转述；**逐字引语仅允许极短锚点**（§6.3） |
| `attribution_confidence` | `EXPLICIT` / `REPORTED` / `INFERRED` / `UNKNOWN` |
| `relation_relevance_assertion` | `RELATION_RELEVANT` / `NOT_RELATION_RELEVANT` / `CONTESTED` |
| `relation_relevance_reason` | **非 `RELATION_RELEVANT` 时必填**（C-P1 要求 reason） |
| `unmappability_justification` | 走 narrative/irrelevant 出口时**必填**（须与失败计数**分列**） |
| `applicability_hint_set` | 逐构念：`APPLICABLE` / `NOT_APPLICABLE_BY_RULE` / `APPLICABILITY_UNKNOWN` + `rule_ref`（**不**写入坐标值域，X-5 / C-P5） |
| `two_sided_flag` | 该单位是否同时涉及 `i→j` 与 `j→i`（§6.2 的必选单位用它） |
| `structural_role` | 仅在 `PROBE` 文件中出现 |
| `rights_ref` | 指向 `rights_status` + 观察到的 licence 逐字串 |
| `sensitive_content_note` | 沿用 corpus 规则；**无未成年人、无性暴力** |

`PROBE` 字段：`unit_id` · `intended_probe_construct` · `design_intent`（为什么这个单位在**不预映射**的意义上
构成对该构念的压力）· `expected_degradation_kind`（**假设**，不是预测承诺）· `sealed_until = ARM-COMPLETE`。

---

## 6. 必须存在的单位（缺任何一条 ⇒ 设计不成立）

### 6.1 双向依赖（corpus 最大簇）

**要求**：至少 1 个单位，其构念取值**必须是两个方向状态的函数**。

- 结构性理由：canonical 自身在 `CONSTRUCT_SCOPE_DIRECTIONALITY.md` §2 写明
  `Mutuality_k(A,B) = H(Z[k,A,B], Z[k,B,A])`、`Asymmetry_k(A,B) = distance(Z[k,A,B], Z[k,B,A])`，
  并逐字规定「**reciprocity / mutuality / asymmetry 优先由两条有向边派生，不额外重复设 primitive。**」
  在当前 basis 下，**8 个构念 × 2 个方向 = 16 个有向格**是最大的格族；
  凡涉及「互惠 / 我们 / 是否还像一家人」的命题都必须横跨两格。
- **⚠ 口径说明（诚实）**：本轨**未读、未执行、未引用** `#20` / `#21` / `#22`，
  因此**无法确认** Architect 所说的「corpus 自己的最大簇」具体指哪一簇。
  上面给出的「16 个有向格」是**从 canonical 自己推出的**最大格族，不是对研究侧簇的引用。
  若 Architect 指的是另一簇，本节需要改；已列入 `open_questions_for_architect`。
- 该单位的形态（**行为定义，不是范例文本**）：双方**各自**报告、两个方向值**不同**、
  且双方都声称一个 pair-level 的说法（例：「我们还算一家人」／「我们已经很久没真正说话了」）。
  **因为两个方向值不同，单一无向槽无法无损表示** ⇒ withheld `<k>` 必须产出 `LOSSY_DIRECTIONAL`。
- 关键设计点：这个单位**不得**借用 `Cohesion/We-ness`（P1，`KEEP_CANDIDATE / contested scope`）来表达。
  `P1` **不在**八项 basis 内；用 pair-level 构念表达会绕过 ablation 的对象。**pair-level 说法只能由两条有向边承载。**

### 6.2 applicability 轴与 uncertainty 轴都要被真正行使

要求**三个**单位，不是一个：

| 单位 | 构念 | 预设读法 | 为什么必须 |
|---|---|---|---|
| `U-NA-1`（clean） | 成年手足 dyad 中的 `RomanticAttraction` | `NOT_APPLICABLE_BY_RULE` | canonical §4 D2 把该构念定义为「i 对 j 的**浪漫伴侣式**特殊吸引/趋近倾向」，而 D1 明写 liking「朋友/亲属/同事均适用」⇒ 该构念在 `KIN` 上按规则无独立含义 |
| `U-NA-2`（**contested**） | 同一 dyad 中的 `SexualDesire` | **`APPLICABILITY_UNKNOWN`**（保守读法） | 保守读法不能排除、且 corpus 的 sensitive-content 规则不允许为此选材 ⇒ 不应断言 `NA`。**benchmark 必须同时记录两种读法及其后果，并把选择交回 Architect** |
| `U-UNK-1` | 任一 dyad 中某构念 | `APPLICABLE` + 估计值取 `Unknown`（含 uncertainty 与 evidence） | 用来证明 **uncertainty 轴 ≠ applicability 轴**：值域里的 `Unknown` 与 applicability 上的 `NOT_APPLICABLE_BY_RULE` **不可互换**（X-5 逐字：不是 0，也不是 Unknown） |

**`U-NA-2` 是这一节的重点**：如果 applicability 轴只在**容易**的情形上被行使，它就**没有被测试**。
benchmark 必须为 `U-NA-2` 产出**两个** `applicability_reading` 分支的结果，并报告分支间是否出现不同的
representation 后果；若后果相同，如实记录「该 contested 读法在本材料上不产生可观测差异」——
这也是一个合法且有信息量的结果。

### 6.3 收紧后的 narrative/irrelevant 出口必须被真正测试

要求**两个**单位：

| 单位 | 断言 | 期望行为 | 失败如何记 |
|---|---|---|---|
| `X-EXIT-1` | 与该 dyad 无关的第三方事务性插话 | 走 narrative/irrelevant 出口，且**必须**带 `relation_relevance_reason` + `unmappability_justification`；**计入独立的出口计数器** | 若缺 reason ⇒ `EXIT_REASON_MISSING`；若与失败计数混列 ⇒ `EXIT_ACCOUNTING_CONFLATED` |
| `X-TRAP-1` | **看起来**像场景描写、**实为**关系相关（例：以物件/空间细节承载对另一方的态度） | **必须不**走出口 | 走了 ⇒ `EXIT_ABUSE`，记为**收紧出口的失败**，**不是** mapping failure |

**为什么必须成对**：没有 trap 单位，就无法区分「收紧出口起作用了」与「mapper 根本不想用出口」——
两者在计数上都表现为「出口被用得很少」。`X-TRAP-1` 是让出口可证伪的最小装置。
这也是 dispatch R3-C 第 3 条（narrative/irrelevant 不能当无限制逃生舱）的直接可执行化。

---

## 7. 规模（由要求推出来，不选定）

**算术**：

```text
8 个构念 × 2 个 witness（每构念 1 个 1 保险）          = 16 单位
+ §6.2 的 applicability / uncertainty 单位              ≤  3 单位（其中 ≥1 可与上表重叠）
+ §6.1 的双向依赖单位（1 个即可，方向不同的 witness 可兼） =  0（重叠）
+ §6.3 的 X-EXIT-1 + X-TRAP-1                        =  2 单位
---------------------------------------------------------
推荐规模                                             = 18–24 单位
每构念 3 个 witness（稳健）                           = 24 + 5 = 29–32 单位
```

**结构性约束**：

- **≥ 2 个 dyad**：只有一个 dyad 就**无法区分**「在此 dyad 不适用」与「不必要」。
  因此 `U-NA-*` 所在的 `KIN` dyad 与另一个 `FRIEND_NONROMANTIC` dyad **必须**分开。
- **每 dyad ≥ 3 个 `t_index`**：withheld arm 必须测的是**状态**的降级，不是单次话语的降级。
  1 个时间点会让「状态」退化成「事件」。
- **硬上限 40 单位**。设计若需要超过 40，它就不是 mini-benchmark（§8.3）。

**下限为何是 18 而不是 10**：每构念 1 个 witness 时，一次转述缺陷就能翻转该构念的结论。
2 个 witness 使「一次缺陷」不致改变向量。**这是结构性理由，不是选定阈值。**

## 8. 诚实的采集代价（必须说清）

> **设计是 mini-benchmark；人口不是免费的。**

§6 的算术只锁住了「需要多少个**单位**」，没有锁住「需要多少份**来源**」。
在 sibling 来源规划那一轮里，本轨实际验证到的 rights-clean（`RIGHTS_CLEARED_AI_OK`，CC BY 4.0，无 `NoDerivatives`）
dyadic 来源只有 **4 份不同来源**：

| 来源 | 可提供 | 结构性短板 |
|---|---|---|
| `PMC11219362` | 双方互报、方向可见、含同性手足 | 单时点；主题被限定在性健康 |
| `PMC10068502` | 长跨度照护叙事 | **不是**同一 dyad 双方报告（§ sibling 源 `S2`） |
| `PMC11686925` | 双方互报 + joint interview、方向可见 | 友谊被服务机制外生安排；年龄差极大 |
| `PMC11904024` | 双方互报 + 同性别友谊 dyad | 观测量是评分非叙述；**含 15–17 岁未成年人** |

要在 rights-clean 前提下填满 **8 构念 × 2 witness**，还缺：

1. `RomanticAttraction` 与 `SexualDesire` 的**双方互报、含时间序列**的权利清晰材料——
   本轨在所检索范围内**未找到**（`PMC2844533` 是 `CC BY-NC` 且单方报告；`PMC4370347` / `PMC9451025` 页面**未检出** CC 串）。
2. `Trust` / `AttachmentSecurity` 的**双方互报**材料。
3. 至少 **4–8 份**额外的 rights-clean dyadic 来源，或对 `PMC8611109`（parent–adult-child 双方分开面访）
   取得**书面许可**。

**结论**：
> 诚实的最小实现 = 一次**有界且具名**的 `clearing + selection` 步骤
> （4–8 份来源的许可确认 + 双方互报筛选 + 未成年人过滤），
> 外加一次 rights-clean 的**人工快照采集**（因为没有任何候选被证实为 `FROZEN_RELEASE`，见来源规划 §7）。
>
> **这一步本身就是一次采集战役。** 本轨不把它称作「零成本」。
> 如果 Architect 要求零采集战役，则 `ROMANTICATTRACTION` 与 `SEXUALDESIRE` 必然落进
> `COVERED_BUT_NOT_WITNESSED` 或 `UNTESTABLE_NO_RIGHTS_CLEAR_SOURCE`，
> **不得**用「结构性不够真实」的材料去凑 witness。

## 9. 每一臂的 pass/fail

### 9.1 `ARM-BASE`（Coverage 臂）

| 项 | 内容 |
|---|---|
| 通过条件 | 每个 `RELATION_RELEVANT` 单位有合法落点；`MAPPING_FAILURE = 0`；未结清 `catchall_used = YES` = 0；每个走出口的单位带 `relation_relevance_reason` + `unmappability_justification`，且**出口计数与失败计数分列** |
| 阈值性质 | 结构性零 N（由成功定义推出） |
| 失败处置 | 单个 `MAPPING_FAILURE` → 进诊断台账，**不**产生 `REJECT`（C-P1 逐字） |
| 额外记录 | `load_bearing_status` 的 8 维向量（本臂只能填 `NOT_COVERED` / `COVERED_BUT_NOT_*` 这几格） |

### 9.2 `ARM-W(−k)`（Minimality 臂，k 逐个跑）

| 项 | 内容 |
|---|---|
| 通过条件 | `necessity_k ≡ ∃ u : witness_qualifies(u, k)`。**不设**「跑几份 fixture」型阈值（C-P1 明令） |
| 无 witness | `k` 记 `COVERED_BUT_NOT_WITNESSED` ⇒ **`NON_NECESSARY`** ⇒ 进 `MERGE` / `DERIVE` **候选** |
| 硬规则 | withheld 期间**不得**新造构念；一旦为通过而新造 ⇒ `ontology hole` ⇒ 该次 run 作废重跑（沿用 `ARM-ABL-1`） |
| 不得越权 | 本臂**不签** `REJECT`。`KEEP` 的签署条件（K1–K4）在 C 轨，本文不改 |

### 9.3 `ARM-EXIT`（收紧出口臂）

| 项 | 内容 |
|---|---|
| 通过条件 | `X-EXIT-1` 带完整 reason 且计数分列；`X-TRAP-1` **未**走出口 |
| 失败码 | `EXIT_REASON_MISSING` · `EXIT_ABUSE` · `EXIT_ACCOUNTING_CONFLATED` |

## 10. 什么会**否证**最小性（预注册的 falsifiers）

| id | 情形 | 结论 |
|---|---|---|
| **F1** | 构念 `k` 在**全部**单位上 withheld 后零降级 | `k` 在本材料上 `NON_NECESSARY` ⇒ **否证**「8 项都必要」；路由 `MERGE`/`DERIVE` |
| **F2** | 某 witness 的降级只因转述/归属塌缩（两方被并成一方、时点被压平） | 该 witness **作废**，重选；`k` 回到 `COVERED_BUT_NOT_WITNESSED` |
| **F3** | 两个构念 `k`/`k'` 在**同一**单位上以**同一**修复方式降级 | 这**不是**两个独立的必要性，而是 redundancy 证据 ⇒ `MERGE` 候选 |
| **F4** | withheld arm 迫使**新增**构念 | `ontology hole` ⇒ run 作废（不是构念被否证） |
| **F5** | 8 项全部 `WITNESSED` | 与 basis 相容，但**不**证明最小充分；本 benchmark **不能**把 v0.1 推进为 `Minimal Sufficient State v0.1`（该推进还受 C-P1 的 K1–K4 约束） |
| **F6** | `k` 的所有 witness 落在 `relation_relevance_assertion = CONTESTED` 的单位上 | 必要性证据建立在争议材料上 ⇒ `HOLD` / `CONTESTED` |
| **F7** | `k` 只在 §6.2 的 `NOT_APPLICABLE_BY_RULE` 情境下 `WITNESSED` | 自相矛盾 ⇒ 记为 `applicability_contradiction`，进诊断 |

**F1 的方向性**（重要）：F1 才是**否证最小性**的事件。
F5 **不**是。benchmark 的默认结果既可能是 F1 也可能是 F5；**两者都不是「八项 basis 已验证」**。

## 11. 冻结 / 版本化纪律

### 11.1 `schema_pin`（直接对应 dispatch R3-C 第 8 条 + `H-F38`）

每个 fixture / benchmark 文件**必须**携带：

```text
schema_pin = {
  tree_sha,               # 写作时的 canonical tree
  canonical_files[],      # 逐个列出依赖的 canonical 文档路径
  retrieval_date,         # 来源抓取日期
  schema_fingerprint      # 对 basis 清单 + 落点分类法 + 处置枚举 的内容 hash
}
```

### 11.2 不可比较性（这是 brief 点名的核心问题）

> **变更 schema 前后产出的 mapping 计数不可直接比较。**

具体化为**四条硬规则**：

1. 以下任一变化**立即**使跨该变化的计数**不可比**：
   `Candidate Minimal Directed Basis` 的构念清单 · 落点分类法 · applicability 词表 · 处置枚举 · 诊断清单。
2. 每次变化记一条 `SCHEMA_DRIFT { before_tree_sha, after_tree_sha, changed_files[], date }`。
3. 计数只在 `(schema_pin, run_id)` **之内**可比。schema 变化后重跑 = **新** `run_id`；
   旧计数标 `SUPERSEDED_BY_SCHEMA_DRIFT`，**不得**与新计数合并、平均或并列成一张趋势表。
4. 已在 `f237784` 上冻结的材料（Fixture 003 明文钉住该版本；Fixture 001 / 002 各有自己的 pin）
   与本 benchmark 的计数**天然不可比**。任何把两者并列成一张表的写法都是错误。

### 11.3 append-only

冻结的 `faithful_paraphrase` **不得**被静默改写。
更正只能**追加**（新 `unit_id` 或新 `source_anchor` + `supersedes_ref`），
沿用 Fixture 003 §2 末句的规则。锚点映射变化时**只允许**追加对照，不得重写既有行。

### 11.4 三 verifier 同版本（**前置，当前 UNKNOWN**）

- Fixture 001 §2 第 7 条与 Fixture 003 §3 第 8 条逐字要求：
  **三个独立 Verifier 必须消费同一个 merged exact version。**
- **本轨的诚实状态**：在 child 隔离契约下，`#20` / `#21` / `#22` 的状态是 **UNKNOWN**。
  本轨**未读、未执行、未引用**这三个 issue，也没有任何其它渠道可确认其 merged exact version。
- **因此**：在本 benchmark 获得**一个确定的 merged exact version**（含 tree sha 与 `MATERIAL` 文件 hash）
  之前，**不得冻结、不得运行、不得签署任何 arm 的结果**。
- 本文件是**设计与来源计划**，不是可冻结件——这是**设计使然**。

### 11.5 封存规则

`PROBE` 文件在 `ARM-BASE` + 全部 `ARM-W(−k)` 完成前保持封存。
`BENCHMARK_OWNER ≠ MAPPING_EXECUTOR`。违反 ⇒ `RUN_VOID_CONTAMINATED`（§4.2）。

## 12. 权利立场

| 规则 | 内容 |
|---|---|
| 硬前置 | 每个来源的 `rights_status` ∈ `{RIGHTS_CLEARED_AI_OK}`。其余全部 ⇒ `HOLD` / `ACCESS_OR_RIGHTS`，**记为 `NOT_RUN`**，**不得**记为 pass，**也不得**记为「不存在该构念」（C-P2 §6.3.1 第 4 条 + 裁决 §C item 6） |
| 禁止 | 需要 `NonCommercial` 的来源（`RIGHTS_CLEARED_CONDITIONAL`）、页面未检出开放 licence 的来源（`RIGHTS_NOT_CLEARED`）、要求另行申请 computational-analysis 许可的来源（`RIGHTS_LICENCE_REQUIRED`）、有机器可读 AI 保留的来源（`RIGHTS_ROBOTS_RESERVED`）——**全部 fail closed** |
| 明确排除 | **Fixture 003 底座（StoryCorps）完全不可用**：`HUMAN_REVIEW_REQUIRED` + pointer-only + 已证明会移动的指针（三条理由见 sibling 来源规划 §6.2） |
| 明确排除 | **Find Case Law 全部不可用**：`X-Robots-Tag: noai` + robots.txt AI 名单 + 条款逐字「You must apply for a licence to do computational analysis…」（同来源规划 §3） |
| 参与者同意残留 | 即使 licence 是 CC BY 4.0，**逐字访谈引语**的受访者同意范围不等于 CC BY 覆盖范围。**默认形态 = faithful paraphrase + 极短锚点**，不整段复制引语。是否连极短锚点都需单独同意，**本轨不判定**，交 Architect / Human |
| 署名 | 任何 `CC BY` 派生物必须携带：作者、原标题、DOI/PMCID、licence 名称与链接、是否已改动（licence 逐字要求 "indicate if changes were made"） |
| 永不升级 | robots / 可达性 / 站点改版**不构成**权利升级（见 sibling 来源规划 §6.2 对 StoryCorps 的处置） |

## 13. 本 benchmark **不能**做的事（防止被过度使用）

1. **不能**验证任何 transition law（裁决 §C item 5：无任何律被冻结）。
2. **不能**给出任何人群统计或总体结论（单 dyad、单时点、小样本；`AGENTS.md` 的 Case Bank 纪律）。
3. **不能**裁定 applicability 的规范读法——它**暴露** `U-NA-2` 的分歧，选择权在 Architect。
4. **不能**对 `PPR` 作任何断言：`PPR` 是 Belief 层（X-1 逐字「layer = Belief / relationship-specific perception」），
   **不在**八项 basis 内 ⇒ 对八项做 ablation 对 `PPR` **零信息**。
5. **不能**对 `Cohesion/We-ness` 作任何断言（P1，`KEEP_CANDIDATE / contested scope`，不在八项内）；
   这正是 §6.1 禁止用 pair-level 构念表达双向单位的原因。
6. **不能**触及 `Satisfaction`（R3，Derived / evaluation candidate，X-1 / C-P8）。
7. **不能**替代四个未覆盖 dyad class 的采集（那是 sibling 文件的工作，且那里**也没有**在 prerequisite 未满足前冻结）。
8. **不能**在没有 `schema_pin` 的情况下与 Fixture 001/002/003 的计数并列（§11.2）。
9. **不能**被用来补 `HD-A03`（other adult kin）/ `HD-A10`（stranger start）——那两格的零覆盖是
   sibling 来源规划所附带的发现，不在本 benchmark 的范围内。

## 14. 本设计**没有**做的事

1. 没有创建 `MATERIAL` 或 `PROBE` 文件，没有写任何 `unit_id`、任何 `faithful_paraphrase`、任何 `t_index`。
2. 没有冻结任何版本，没有跑任何 arm，没有产出任何 mapping 计数、任何 `degradation_kind` 实例。
3. 没有声称 8 项中任何一项已必要、已冗余、或已被否证。
4. 没有引入新构念、新值类、新枚举、新权重、新尺度。
5. 没有设定任何普适数值阈值（只有 3 处结构性条件，且都不是 N-fixture 型）。
6. 没有编辑任何既有文件。
7. 没有读/执行/引用 `#20` / `#21` / `#22`；没有运行 Eye/Juece；没有下载受限数据；没有绕过 robots。
8. 没有把 PR #31/#32 的 swarm 主张当作已验证科学；实现的是 adjudication V1。
9. 没有主张「同性伴侣 dyad 在权利清晰材料中不存在」——那只能是检索范围陈述（X-14），且本文件不作此主张。
