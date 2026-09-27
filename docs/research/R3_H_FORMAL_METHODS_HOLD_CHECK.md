# R3-H — C-P12 前置工程检查：Gate 是否组合偏更新算子

**Status:** `NOT_APPLICABLE_YET`（建议 C-P12 关闭为此值）
**As of:** 2026-09-28
**Child:** `R3-H`（Round-3 Track R3-H，fresh child，本 dispatch 授权的唯一 child）
**Authority:** `youling/lhrm#30` `ARCHITECT_ADJUDICATION_V1`（comment `5854920569`）· `ARCHITECT_ROUND3_DISPATCH_V1`（comment `5854930069`）Track R3-H
**Base:** `main` @ `ee393ca24f9fbf738ac0ed839e99bdc99de6fc3a`
**Scope:** **只做实现检查**。不改 canonical、不改实现、不跑任何 Gate、不实施任何 transition law。

---

## 0. 决策

```text
DECISION = NOT_APPLICABLE_YET
```

**当前与拟议的 Gate 均不组合偏更新算子**，因为它们**根本不定义任何更新算子**。
每一步的产物是**逐单位（per-unit）的分类记录**，`MAPPING_FAILURE` 的归因是**该单位自身**
的诊断，不经过任何跨单位的状态传递。因此 RULE-⊥ 的偏算子风险在现有实现中**没有落点**。

---

## 1. 被检查的对象：`RULE-⊥` 与它的自陈风险

`docs/research/overnight-2026-09-27/06_TRANSITION_LAWS.md`（兄弟轨 `a3c`，READ-ONLY）§1 记 `MH1`，
逐字（`:118-129`）：

```text
**共享的 ⊥ 规则（记为 RULE-⊥）：**
(1)  证据为 ⊥  ⇒  状态**不发生数值更新**，且**不**被填充为 0 / 均值 / 中性。
...
**已知的形式风险（U4）：** `⊥` 规则使更新算子成为**偏算子**（partial operator）。
偏算子在格上不一定满足结合律或可逆性。若 Gate A 的覆盖推理依赖算子组合，
必须先证其组合性与闭包性，否则 `MAPPING_FAILURE` 的归因会出错。此项 `UNKNOWN`。
```

**该文件自身已把它降级为 self-audit**（`:131-139` 逐字）：
**"U-4 是 `self-audit`，不是发现。"** · **"本文件不主张 Gate A 的归因推理会出错，也不主张它不会出错。"** ·
**"前置工程检查归 R3-H"** · **"若 R3-H 判 `NOT_APPLICABLE_YET`，则 C-P12 关闭为 `NOT_APPLICABLE_YET`。"**
§11 非主张 17（`:1424-1425`）再次登记：**"不主张 `⊥` 规则的形式风险已解决或已恶化。U-4 = `UNKNOWN`"**。

**⇒ repair round 的降级是到位的**：风险被标为自陈、自审计、状态 `UNKNOWN`，**未被当发现**。
本 memo 不推翻该降级。

**附带的两个开放问题（已定位，勿混）：**

| 开放问题 | 位置 | 状态 |
|---|---|---|
| `U4` 偏算子的结合性/闭包性 | `06` §1 `:127-129` | `UNKNOWN` · self-audit |
| `MH1` 的形式化地位（是否需要一个**非算子**的替代表达：把状态坐标集合本身扩展为含 `⊥` 的格） | `06` §12 裁决请求 1 `:1448-1455` | 已随 `C-P12` 改为 `HOLD / NOT_CANONICAL_NOW`，**等 R3-H** |

⚠ **文档事实登记（低严重度，非本轨所修）**：`06` §10 的未解问题登记表用 `U-1 … U-8` 编号，
其中 §10 的 `U-4`（`:1362`）是**另一件事**（`环境的直接通道 vs 经由行为的通道（MH6）`），
与 §1 的 `U4`（偏算子）**编号相撞**。且偏算子风险**不在** §10 登记表内，只活在 §1 与 §12。
⇒ 交回 parent / A3C 轨处置；本轨不编辑该文件。

---

## 2. 证据 A：canonical 流水线（`main`）是「逐单位分类 + 阈值」，不含算子

`docs/foundation/PARAMETER_CONVERGENCE_V0_1.md`（worktree `h`，= `main`）：

| 读到的原文 | 行 | 为什么它排除算子组合 |
|---|---|---|
| Gate A 步骤 3：`独立 Agent 逐句映射`；步骤 4：`记录所有 PARTIAL_MAPPING / MULTI_MAPPING / MAPPING_FAILURE` | `:713-715` | 输入是**句子**，输出是**该句子的标签**。无状态向量在句间传递。 |
| §14 成功判据：`因此第一轮 Case Bank test 只要求 **语义有合法落点**，不要求每句话产生精确数值变化。` | `:679` | 门不要求数值变化 ⇒ 门内没有**任何**被应用的对象，更没有被组合的对象。 |
| §14 反例：`而不是未经校准就写：` / `Liking += 1` | `:693-697` | canonical **显式拒绝**累积式更新被写进第一轮测试。 |
| Gate A 第 5 步：`Architect 只分析 failure，不允许 Agent 为了通过测试现场发明变量` | `:715` | 归因是**Architect 逐条诊断**，不是从组合结果反推。 |
| Gate C 六对构念挑战（`Liking vs RomanticAttraction` 等） | `:735-746` | 是**成对语义对照清单**，无算子、无顺序。 |

**结论：canonical §15 三门里没有任何一步会组合更新算子；它们是逐单位分类 + 结构性零 N 判据。**

### 2.1 canonical 中「transition」的三处出现，都不构成算子组合

- `:442` `然后通过 observation / belief / transition 更新 state。` —— **散句，描述尚不存在的下游能力**，
  未绑定任何门步骤、未绑定任何判据。
- `:450` `-> possible Trust/Care/Attraction/Dedication transition` —— 带 `possible` 的**假设性示意**，
  同样未绑定门。（这两行在 §8「降级为 Action / Observation 的变量」内，是 canonical **主动降级**变量的段落。）
- `AGENTS.md:52` `it is modeled as state transition over continuous/mixed state.` —— **架构方向**；
  且裁决 §C item 5 逐字：**"No transition law is validated/frozen by PR #31/#32."**

⇒ 架构层面承认有 transition，但**没有任何一个被实现、被门读取、或被组合**。

---

## 3. 证据 B：拟议四门协议同样不组合偏算子；ablation 臂是**从头重分类**

兄弟轨 `c`，`docs/foundation/VALIDATION_GATES_V0_2.md`（READ-ONLY，head `83ff2e3436260f70e381b1aff7e6060d65142753`）。

**决定性段落 —— `§6.0` 共享程序步骤 `ARM-ABL-1`（`:246-262`），逐字：**

```text
  baseline arm : 完整 basis 映射，记录每个单位的 mapping_outcome
  withheld arm : 逐一 withheld <k>（<k> 从 §11 basis 清单移出，不新增任何构念），
                 重跑同一批单位，记录 mapping_outcome 的变化
  记录         : ablation_record（含 downgraded_unit_ids 与 downgrade_kind）
  硬规则       : withheld 期间**不得**新造构念；新造构念 = `ontology hole`，
                 该次 withheld run 作废并重跑（记录作废理由）
  不可比较性   : 变更 schema 前后产出的 mapping 计数**不可**直接比较
```

**裁决：ablation 臂是「换一个 basis 清单，把同一批单位重跑一遍」，不是「把偏算子依次作用」。**
理由逐条：

1. **操作对象不同。** withheld arm 的动作是 `重跑同一批单位` —— 输入是**句子 + 落点词表**，
   输出是**该句子的 `mapping_outcome`**。它不是「把 `T_<k1>` 作用在 `T_<k2>` 的结果上」。
2. **结果是并置的，不是嵌套的。** `ablation_record` 的字段是
   `downgraded_unit_ids` 与 `downgrade_kind ∈ { DIRECT→PARTIAL, DIRECT→FAILURE }`（`:223`）
   —— 两条臂的结果按 **unit id 做集合差**，标的是**标签的迁移**，不是状态的递推。
3. **协议自己禁止代数读法。** `不可比较性`（`:260-261`）明写变更 schema 前后的 mapping 计数
   **不可直接比较**。若存在被组合的算子，就不会有这条约束——这条约束正是**「不存在共同代数」的旁证**。
4. **硬规则是否定式的。** withheld 期间新造构念 ⇒ `ontology hole` ⇒ 该次 run **作废重跑**。
   即：withheld arm 每次都从**干净起点**重跑，不累积前一轮的部分更新。

**其余三门同样无算子：**

| 门 | 证据（`VALIDATION_GATES_V0_2.md`） | 无算子的理由 |
|---|---|---|
| `GATE_COVERAGE` | `:273` 步骤「逐单位落点」；`:275` 通过判据 `MAPPING_FAILURE 计数 = 0 且未结清的 catchall_used = YES 计数 = 0` | 纯计数。 |
| `GATE_CROSS_CONTEXT` | `:306` 步骤「对 `RUN` cell 逐实例记录 `reading` → 判 `STABLE` / `UNSTABLE` / `NOT_RUN`」 | 逐 cell 判定，表 A / 表 B **两表不相除不相加**（`:443-446`），无跨 cell 运算。 |
| `GATE_REDUNDANCY` | `:34`「对每个候选签发终局处置」；`:66-70` 逐值执行语义 | 是**清单级裁决**，由 Project Architect 签发，不是算子输出。 |
| 修复后流水线 | `:170-176` `STAGE 0 relation-relevance pre-check` → `STAGE 1 landing-class assignment` → `STAGE 2 diagnosis` → `STAGE 3 triage` → `STAGE 4 gate accounting` | 五个阶段全部是**逐单位、无状态传递**的分类/记账步骤。 |

**结论：拟议四门协议不含任何算子，更不含偏算子的组合。**

---

## 4. 载体结构：canonical 的 `Coord_k` 里没有 `⊥`

要让偏算子风险落地，先要有一个**能承载 `⊥` 的被更新对象**。canonical 的坐标定义是
`PARAMETER_CONVERGENCE_V0_1.md:658-677`，逐字：

```text
StateCoordinate
=
{
  estimate_or_region,
  uncertainty,
  evidence,
  provenance,
  observation_time
}
甚至：
P(Z_k | Evidence_<=t)
都合法。
```

⇒ **`⊥` 不在 canonical 坐标里**；`⊥` 是 `a3c` §1 `:106` 自定义的记号
（`⊥` = `UNKNOWN`：**一等值**）。`AGENTS.md:37` 确实把 `Unknown` 列为**合法坐标取值**
（`A coordinate may be an interval, ordinal state, category, constraint, probability distribution, Unknown, or estimate + uncertainty + evidence.`），
但那是**坐标取值**，不是**更新算子**；`Unknown` 的定义归兄弟轨 D（`C-P13` observability registry 依赖它）。

**⇒ 没有算子被定义，也就没有「偏」算子。风险的第一步就落空。**

---

## 5. 什么会让它将来变得适用（**使本项不被丢失**）

以下任一出现，本 memo 立即失效，C-P12 重开：

1. **门开始要求数值更新。** 若 `GATE_COVERAGE` 的通过判据从「有合法落点 / 计数为零」
   改为要求单位引起坐标的数值变动（即 `PARAMETER_CONVERGENCE` §14 `:679` 那句被取代），
   就第一次出现**被作用的对象**。
2. **出现跨单位的顺序化臂。** 若 ablation 或任何新臂改为「在同一状态上**依次**作用
   多个更新」，而不是 `VALIDATION_GATES_V0_2` §6.0 的 `重跑同一批单位`，
   则**组合**出现，`⊥` 传播（RULE-⊥ (4)「任何下游 readout 遇到 ⊥ 必须显式传播 ⊥」）
   与更新的顺序绑定 ⇒ 结合律/闭包性问题变成真问题。
3. **`GATE_REDUNDANCY` 的 `DERIVE` 处置被激活，且输入含 `Unknown`/`⊥`。**
   这是**唯一已在文本中存在的、接近组合**的形状（`VALIDATION_GATES_V0_2.md:68`：
   `DERIVE` = `<k>` 的内容是其它保留坐标/记录的**函数**，须填 `DERIVATION`）。
   `DERIVE` 本身是**静态读出函数**（`PARAMETER_CONVERGENCE` §9 `R1` `Mutuality_k = H(Z[k,A,B], Z[k,B,A])`），
   不是更新算子；今日**不构成**偏算子风险。
   ⚠ **但若某个 `DERIVATION` 真的在含 `Unknown` 的坐标上求值**，
   `H(Unknown, …)` 是否定义就成为真问题——那时需要的是
   **「`DERIVATION` 必须在 `Unknown` 坐标上显式给出值（`⊥` 或省略）」这一条前置条件**，
   **不是**把 RULE-⊥ 写进 canonical。
4. **某条 transition law 被实现且被门读取。** 裁决 §C item 5 现在禁止（`NONE FROZEN`）。
   一旦解除且 `Θ_k` / `Ĝ_k` 真的在门内被组合，本项立即重开。

**建议 parent 记录的最小可触发条件（一句话）：**
**「任何门步骤第一次要求把更新作用到一个含 `Unknown` 的共享状态上。」**
在此之前，本项是纯形式学整洁性问题。

---

## 6. 残余（诚实记账）

1. **`U4` 的状态未被本 memo 改变。** 本 memo 判的是**实现适用性**，不是形式风险本身。
   `U4 = UNKNOWN` 仍然成立；`06` §1 的自陈风险**未被证伪也未被消解**。
   本 memo 只证明**它当前没有实现落点**。§11 非主张 17 的措辞**继续有效**。
2. **RULE-⊥ 本身仍未被形式审查。** 逐字（`06` `:139`）：
   **"不得把本段读成『`⊥` 规则已通过形式审查』——它是未审查。"** 本 memo 不改变这句。
3. **判定绑定于 inspected snapshot。** 绑定 `main @ ee393ca`、
   `wt/c @ 83ff2e3`、`wt/a3c @ 3f96eae`。若 sibling `C` 的协议或 canonical 之后引入
   数值更新臂（§5 第 1/2 条），判定即失效。
4. **无代码可查。** 本仓 `git ls-files` 共 **18 个文件，`.md` 18 个，源码文件 0 个**
   （`AGENTS.md` / `README.md` / `docs/**`）。因此「实现」一词在本仓**只能指文本协议**。
   若将来存在仓外实现（Case Bank `#13` 的标注流程、Gate 执行脚本），
   本 memo **不覆盖**它；那是重开本项的理由之一。
5. **三轨文档的 base 各不相同**（`h` = `ee393ca`、`c` = `83ff2e3`、`a3c` = `3f96eae`）。
   引用均为各该 snapshot 的行号，跨轨行号不可比。
6. **`06` §10 的 `U-4` 编号相撞**（见 §1 末）已登记但**未修**——本轨无权编辑该文件。

---

## 7. `explicit_non_claims`（本 memo **没有**主张的东西）

1. **未主张 Gate A 的归因会出错。** 与 `06` `:134` 一致：**也不主张它不会出错。**
2. **未主张 RULE-⊥ 可行 / 不可行。** 未做形式审查，未验证任何格论性质。
3. **未主张 `⊥` 不需要进入 canonical。** 只判**当前无实现落点**；是否需要是 Architect 的裁决。
4. **未主张 `DERIVE` 处置有代数缺陷。** §5 第 3 条是**触发条件**，不是缺陷指控。
5. **未跑任何 Gate。** 全文不含任何 mapping 结果、计数或 cell 状态。
6. **未验证任何构念的必要性。** Fixture 001/002/003 未被使用。
7. **未裁定 applicability / observability / `Unknown` 的定义。** 属兄弟轨 D（`C-P5` / `C-P13`）。
8. **未修改任何 canonical 或实现文件。** 白名单 = 本文件一个。
9. **未读 / 未执行 / 未引用 `#20` / `#21` / `#22`。** 未碰 Eye/Juece。
10. **未 push、未开 PR、未改 review state、未改 history。** 交付 = branch + commit + packet。
11. **未做文献检索。** 本项是代码与文本检查，不是研究任务；§5 的四条触发条件来自
    上述文档，**不来自外部文献**。

---

## 8. 给 Architect 的一行请求

**依 `C-P12` 的条件（「only add if an implementation actually composes partial update operators」），
本轨未发现这样的实现。建议 C-P12 关闭为 `NOT_APPLICABLE_YET`，
并把 §5 的最小触发条件（「门第一次要求把更新作用到含 `Unknown` 的共享状态上」）作为**唤醒条件**留在案卷上，
使该项在实现改变时可被重新调起，而不是被静默遗忘。**
