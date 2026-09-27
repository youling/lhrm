# CANONICAL_CHANGE_PROPOSALS — Round 2 review swarm over `youling/lhrm#31`

> 本文件只收录**会触及 `docs/foundation/*` / `AGENTS.md` / `docs/validation/*` / `README.md`** 的条目。
> 纯研究文档（`docs/research/overnight-2026-09-27/*`）的更正**不在此文件**，见 `REJECTED_OR_WEAK_FINDINGS.md` 与 manifest §7。
>
> **本文件不实施任何一条。** 每条给出：目标文件与节 · 建议改动 · 证据 · 独立性 · **能否停在 proposal** · 裁决者。
>
> `REVIEW_CONTRACT.md` §5 字段 7 要求：`requires_canonical_change: YES` 时必须写明**具体要改哪个文件的哪一节**
> 以及**为什么不能停在 proposal**。**「不能停在 proposal」必须有理由；没有理由的一律标 `可停在 proposal`。**

---

## 状态汇总

| 状态 | 数量 | id |
|---|---:|---|
| **PROPOSED — 建议越过 proposal（低成本、无新证据）** | 2 | C-P1, C-P4a |
| **PROPOSED — 建议越过 proposal（但需 Architect 显式签署）** | 3 | C-P2, C-P3, C-P6 |
| **PROPOSED — 可停在 proposal** | 4 | C-P5, C-P7, C-P8, C-P9 |
| **NOT_YET — 前置未解，不得写入 canonical** | 3 | C-P10, C-P11, C-P12 |
| **WITHDRAWN — 原主张被阶段 2 推翻** | 5 | C-W1…C-W5 |
| **CONDITIONAL — 取决于一个尚未裁定的读法** | 1 | C-P13 |

---

## C-P1 — Gate 的后果动词、阈值、诊断类型与 ablation 臂

- **目标**：`docs/foundation/PARAMETER_CONVERGENCE_V0_1.md`
  **+ `AGENTS.md:62`（镜像同步）**
- **建议改动**（`EV1` §8 的 5 处 + 1 处镜像；`I-C1`/`I-C2`/`I-C3`；`ADJ3` rec 1/2/5）：

  | # | 位置 | 改动 |
  |---|---|---|
  | 1 | `§2.6`（`:84` 后） | 补一条**带阈值**的 `MERGE` / `REJECT` 后果句。需要三样当前缺失的东西：**动作动词**（`MERGE into <k>` / `REJECT` / `KEEP`）、**记录位置**（本文追加裁决与理由 + 同步 §11 basis 清单）、**阈值**（例：某 construct 被移除时，跨 ≥N 个 fixture 的全部单位中 `DIRECT_MAPPING` 降级数为 0 ⇒ 判 `MERGE` 或 `REJECT`）。同时定义 `:84` 中未定义的词「**重要**现实句子」（例：以 `DIRECT_MAPPING → PARTIAL/FAILURE` 的降级作为「重要」的可操作代理） |
  | 2 | `§15 Gate A`（`:707-715`） | 补一个 **leave-one-out ablation 步骤**：对 §11 的 8 项逐项 withheld 后重跑（或基于已记录的 mapping 重新判定），记录是否有任何单位发生 `DIRECT_MAPPING → PARTIAL/FAILURE` 的降级 |
  | 3 | `§13` 诊断词表（`:641-649`） | 补 **`redundancy hole`** 一类：「该 unit 可由 `<k>` 无损表示，故 `<m>` 非必要」。**并同步 `AGENTS.md:62`**。同时重新审视 `§13` 第 10 类 `Derived/Narrative-only` 这个 catch-all 的**宽度**——它会吸收掉大量本应是 construct 层的信息 |
  | 4 | `§2.2`（`:53`）+ `§15 Gate C`（`:735-746`） | 补对应的后果句，并把 Gate C 接到它上面（Gate C 是 §2.2 的 harness，两者目前都无后果）。同时给 Gate B 补一句 **pass criterion**（例：§2.4 的语义稳定性在 11 个 context 中全部保持，否则该 construct 拆分或降层），否则 Gate B 永远只是清单 |
  | 5 | `§2.3`（`:57`） | 把「**仍可能**提供额外信息」改成**可证伪**形式。例：「在已知其它候选后，该 construct 在 Case Bank / longitudinal 中**仍提供至少一处** `DIRECT_MAPPING` 增量」 |
  | 6（可选） | `§12`（`:590`–`:610`） | 为 6 项推测性排除（爱 / 亲密 / 嫉妒 / 控制欲 / 忠诚 / 化学反应）补 **re-entry criterion**。「什么证据会让它重新进入候选」比补 §2.6 更能防止假否决（`EV1` §6 第 7 点） |
  | 7（`ADJ3` 追加） | `§2.5` 的 10 层 × `§13` 的 10 类 | **必须先合并**。两表重叠 7 项、各有 3 项只在一边 ⇒ 否则任何 layer 判定都可被两套词表分别「证成」 |
  | 8（`ADJ3` 追加） | `§2.1` / `§2.4` | 补后果句或明写「无后果」。`ADJ3` 逐条确认这三条**连后果句都没有** |

- **证据**：`I-C1`（三门无判定句/阈值/失败终态，含「不修」）；`I-C2`（§2.6 结构上永不触发，8 项 basis 单调增长）；`I-C3`（`:86` 的未兑现承诺）；
  `ADJ3` Q2（**六条全部**无 procedure / required evidence / output field / threshold / designated executor；`:43` 是唯一程序性句子且未指定审计者、产出、失败后果）；
  `EV1` §7/§8（独立复现 + 最小 patch 描述 + 规模估计）。
- **独立性**：`ADJ3` 与 `EV1` **各自独立复现**，未共享中间产物（`ADJ3` 逐节点过 canonical 780 行；`EV1` 从 `:86` vs Gate A 的内部矛盾切入）。
  `I-C1` 标 `NON_INDEPENDENT`（A03 自陈是对 `17` 的复核）—— 但 parent 判 `PROJECT_PRIMARY` 双复现。
- **能否停在 proposal**：**不能。**
  - (a) **这是唯一能让 8 项 basis 缩小的程序通道**。停在 proposal 意味着 basis 继续单调增长，而 Gate A/B/C 的任何后续结果都不可解释。
  - (b) `AGENTS.md:62` 是 `§13:641-649` 的**逐字镜像**；只改一处会造成 canonical 内部冲突（而 `I-C12` 已证明本项目**已经发生过**一次同类文档级冲突）。
  - (c) 改动 2（ablation 臂）是**协议定义**，若停在 proposal，`:86` 的承诺永远是空话。
- **成本**（`EV1` §8）：约 **5–8 句新增文字 + 1 个 ablation 步骤定义 + 1 个诊断枚举值**。**不需要新文献、不需要新数据、不需要新模型。**
- **范围**（`ADJ3` rec 5）：**4 文件 / ≥6 节**。**parent 记录**：`EV1` 估的是新增文字量，`ADJ3` 扩的是必须一起改的面；二者不冲突。
- **裁决者**：Architect（签署）+ Human（`docs/foundation/*` 属架构面）。

---

## C-P2 — Gate B 重写为外部生成的反例集

- **目标**：`docs/foundation/PARAMETER_CONVERGENCE_V0_1.md` **§15 Gate B**
- **建议改动**（`I-C7` + `ADJ3` Q3 + `I-C8` + `I-C9` + `I-C10` + `I-C11` + `G-C13` + `L-C5`）：
  1. 把 §15 Gate B 从「项目自产的 11 个 cell」重写为**外部生成**的反例集。
  2. 给**每个 cell 定合格判据**（当前 11 个 cell 无一个有自己的判据定义）。
  3. 与 `§2.4` / `CONSTRUCT_SCOPE_DIRECTIONALITY §7.6` / `CURRENT_ARCHITECTURE:53-56` **四方对齐**（实测三张清单为 6 / 8 / 11 项，互不相同）。
  4. 移除 `harm-asymmetric` 的**类目错误**（它是不对称**轴**，不是 dyad **型**）。
  5. 补 `17` F9 表漏掉的 2 个真 cell（`opposite-sex`、`non-kin`），删掉 1 个非 Gate B cell（`work colleague`）。
  6. 修正第 11 格：Gate B 的 `high-attraction/low-trust` **不得**用 `Liking` 顶替 `Romantic Attraction`（`PARAMETER:132`（D1）与 `:151`（D2）明确区分二者，并说「可以喜欢但无 romantic attraction」）。
- **证据**：11 个 cell 中 **10 个是项目自身文本的逐条复述**（`ADJ3` 逐格重算；`I-C7` 独立得出同一结论），唯一新 cell = `high-attraction/low-trust`，其覆盖为 **0**。
- **独立性**：`I-C7` 与 `ADJ3` Q3 **各自重算**，结论一致；`I-C7` 明标这是它的**独立复算，不是三 lane 票数**。
- **能否停在 proposal**：**不能。** 测试集由被测对象自产 = **结构性确认偏误**。
  `19` 自己已经写对了「Gate B 通过不构成跨域稳定性证据」，但只要 cell 仍由项目自产，**这条限定就永远需要一个外部批注来兜**。
- **必须同时记录的限定**（`ADJ3` rec 4）：Gate B **混合了两张不同用途的清单**（8 项是抽样框、3 项是构念解耦模式）
  ⇒ **不存在有意义的单一分母**。`caregiving` 的覆盖是**口径依赖的 partial = 2/12**，不是 0。
- **裁决者**：Architect。

---

## C-P3 — `§4 D4` 增加具名 `FeltSecurity` facet 槽位 + `domain` 降级

- **目标**：`docs/foundation/PARAMETER_CONVERGENCE_V0_1.md` **§4 D4**（`:168-181`）
- **建议改动**（`ADJ1` Q4，`requires_canonical_change: YES`，但**极窄**）：
  - (a) 增加一个**具名 facet 槽位** `FeltSecurity`——**不预设它归 `Trust` 还是归 `AttachmentSecurity`**，只承认 `Trust` 内**存在**这一片语义。
  - (b) 把 `domain` 从「未提及」改为**显式登记为 `FACET_RECOMMENDED_NOT_REQUIRED`**，注明「必需与否待 measurement invariance」。
  - **`§4 D5` 本轮不需要改**（其 Open question「attachment security 是否应拆成更细 facet，暂不做」已足够容纳本条）。
- **证据**：`ADJ1` 独立复核 `02b:225-247` 边表确认**无 `E4a`**（`A-C6`，本簇唯一有独立一手支撑的条目）；
  `18` CF-05 自己已把冲突定性为「**定义冲突**」+ `OVERLAPPING_NEEDS_SCOPE_RULE`；
  `A-C21` 的 `WRONG-SCOPE` 存活（`02:158` 自己的引文是**工作场所例子**）。
- **能否停在 proposal**：**第一步可以且应当停在 proposal**（需 Architect 一次显式签署，且**不得**写成「已验证的构念事实」）。
  **但不能停在 proposal 作为终态**，理由有二（`ADJ1` 原文）：
  - (a) 若不写，`02b` 的 `FeltSecurity` 重叠与 `02` 的 `KEEP` 在 canonical 中仍表现为「同一语义只被登记一次」，**Gate C 的冗余判定不可解释**。
  - (b) 若不写，后续任何动 `Trust` 的提案都会缺少锚点。
- **明确不做**（`ADJ1`）：**`REJECT`「强制 `domain` signature 字段」**——canonical §4 D4 **本轮不新增 `domain` 必需字段**。
  **同时**把 `A-C21` 的 scope 缺陷记在 `02 §3.9` 的 `OutcomeDependence`「同 Trust」上（`:218`），因为它**复用了同一条 organizational 依据**。
- **裁决者**：Architect。

---

## C-P4 — 权力三分的落地（须拆 R2-a / R2-b）

- **目标**：`docs/foundation/PARAMETER_CONVERGENCE_V0_1.md`（R2 相关节）+ `docs/foundation/CURRENT_ARCHITECTURE.md`（P1 槽位）
- **建议改动**（`F-C21` `VERIFIED`；`F-C22`；`F-C23` `WRONG-SCOPE`；`ADJ2` rec 4）：
  - **R2-a（可越过 proposal）**：把 R2 限定为「relative power 分量的 **derived readout**」；在 schema 中显式加入 **total power 对称 readout** + **domain 索引**。
    **证据已由 Lawler 1993 原文与 Lawler & Bacharach 1987 实验逐字核实**（`F` 与 `ADJ2` 均 `VERIFIED`）。
  - **R2-b（`HOLD_FOR_EVIDENCE`）**：`punitive capacity` / `legitimacy & bases` / `perceived power` / `felt compliance` 四个槽位。
    - `legitimacy` 被 `10` **自己**引用的 Junkins「没有成熟量表」否定。
    - `felt compliance` 被 `10` **自己**的 §7 定级为「不应被当作已确立的发现」，且其关键来源 Solomon & Samp 被 `10` 自标「**内容未读**」。
- **必须同时修的实现规格**（`F-C23` + `ADJ2` 独立复核）：`total power` 的正确形式是**对称聚合（和）**；
  `C`（relational cohesion）是 `TP` 与 `RP` 的**关系**，**不是** `TP` 的定义。`10` 把 Lawler 的 relational-cohesion 规格当成了 total-power 规格。
- **能否停在 proposal**：**R2-a 不能**（纯增补、无新数据、证据已逐字核实）；**R2-b 必须停在 proposal**。
- **裁决者**：Architect。

---

## C-P5 — 值类清单：增补「构念 × dyad-type 适用性元数据」的登记位

- **目标**：`docs/foundation/CURRENT_ARCHITECTURE.md` §9 原则 4（值类清单）+ `AGENTS.md` 对应条
- **建议改动**：**不是**补一个「不适用」值类（该主张已被推翻，见 C-W1），而是**增补一个登记位**：
  记录「某构念在某 dyad-type 上不具独立语义」这条**负面知识**。
- **证据**：`EV3` Claim 1 的**残留内核**，判 `PLAUSIBLE`：
  canonical 的值类清单是**许可式**（`可以` / `may be`），两份清单互不一致，全库无封闭性声明；
  而「该维度在本 dyad 被规则/边界支配而非被取值」这条语义**目前只能写在报告正文里**，没有正式位置。
  `ADJ3` Q8 独立把 `C-4`（`Unknown` 类型学）列为**必须由 Human / Architect 裁决的架构设计任务**；`E-C23` 独立发现 `07` 与 `08b` 各自发明平行编码且**三处同名不同义**；
  `K-C8` 独立指出 `18` 的 N-01 SSOT 修法**类型上不完整**（`MAPPING_FAILURE` 是**表示失败**而非证据状态，`18` 自己已指出「它在 `R07` 的 tag 集合里没有对应值」）。
- **能否停在 proposal**：**可以。** 但 `E-C23` 指出**直接并入会得到 14+ 值枚举，违反 `AGENTS.md:22`/`:24`** ⇒ 落地时**必须两轴分离**
  （`tag` 证据侧 + `applicability` 适用性侧），不能合并成一个枚举。
- **裁决者**：Architect（值类清单是许可式还是封闭集——**这是唯一的裁决点**，见 `CONTESTED_FINDINGS.md` X-5 (c)）。

---

## C-P6 — `VALIDATION_CORPUS` 的两处文档级冲突

- **目标**：`docs/validation/VALIDATION_CORPUS_V0_1.md`
- **建议改动**（`I-C28` + `I-C12`，**成本最低、无判据语义变更**）：
  1. 把 `future_leakage_risk` **拆成两列**：「文档内 / 结局泄漏」与「预训练记忆泄漏」。当前合并为一列 ⇒ **互相遮蔽**。
  2. 把「Recommended Fixture 001–003」小节**标注为已被 `#19` / `#24` / `#25` 取代**。
- **证据**：`I-C12` `VERIFIED` —— canonical 内部存在**已经发生过的**文档级冲突（不是假设）。
  `I` 自做 git + SHA + grep 确认；**两份报告都靠读文件而非索引躲过了它**。
- **能否停在 proposal**：**不能。** 这是**已发生的**冲突，不是待评估的变更。
  成本：2 处标注，**零 canonical 设计成本**。
- **裁决者**：Architect。

---

## C-P7 — 域枚举与三张 cross-context 清单的文档对齐

- **目标**：`CONSTRUCT_SCOPE_DIRECTIONALITY.md` §7.6 · `PARAMETER_CONVERGENCE_V0_1.md` §2.4 与 §15 Gate B（→ `CURRENT_ARCHITECTURE.md:53-56`）
- **建议改动**：**层 1（零成本）**——三张清单与 `CURRENT_ARCHITECTURE` §2 的**文档对齐**。
  `CURRENT_ARCHITECTURE:53-56` 已把 A12 点名的 5 类中的 **4 类逐一列为在域**（`亲属` / `前任` / `同事` + `合作` / `敌对`）；
  `AGENTS.md`「向下追机制，但不向下扩研究对象」是同一立场，**无冲突**。
- **层 2（有成本，本文件不提议）**：`sibling` / `parent–adult-child` / `non-romantic friendship` / `same-sex` 在 12 份语料里**零 core-dyadic 实例**——这需要**采集**，不是文档编辑。
- **证据**：`ADJ3` Q4 逐条映射（4/5 逐字或直接蕴含，1/5 是类目错误）；`G-C13` 独立逐条比对三份 canonical 清单（6 / 8 / 11 项，互不相同）。
- **能否停在 proposal**：**可以。** 但 `ADJ3` 采纳 lane `L` 的自我反驳并加强：
  > 既然研究域已声明、`AGENTS.md` 又禁止向下扩域，那 A12 **唯一可能的读法**就是「表示能力无证据」，
  > 而**表示能力的证据只能由 corpus 覆盖给出，不能由域声明给出**。⇒ **不要把层 1 的文档对齐当作层 2 的替代。**
- **裁决者**：Architect（接受双层记账）+ 语料采集（层 2）。

---

## C-P8 — `§9 R3` 追加后果预登记

- **目标**：`docs/foundation/PARAMETER_CONVERGENCE_V0_1.md` **§9 R3**（`:489-495`）
- **建议改动**：追加一句**后果预登记**：
  > 「若本判据成立并提升 Satisfaction，§4 D7 的 basis 地位与 §11 的 8 项 basis 需重新审议；本条只登记后果，不预设结论。」
- **证据**：`ADJ1` Q2（`A-C25`(a) 存活）。`ADJ1` 独立复核了 D7 `:224` 与 R3 `:489-495` 两段原文，结论与 `A-C25` 一致。
- **能否停在 proposal**：**第一步必须停在 proposal**（需先解 `[S05]` 事实前提 + 审 `17` T1）。
  **不能停在 proposal 作为终态**的理由（`ADJ1` 原文）：若不预登记，R3 判据一旦触发，
  **Gate C 会在两层同时占用同一语义时给出不可解释结果**。
  **`§4 D7` 本体不需要改。**
- **明确不做**（`ADJ1` Q2）：**删除前提** `17:100`/`:373`（「LHRM 把 Belief 当成 state 的下游」在 canonical 中不存在）；
  **重标主张**（F3 的**层位部分**改 `WRONG-SCOPE` + `UNVERIFIABLE_AS_WRITTEN`，把 Segal & Fraley 的因果发现**保留**为 dynamics evidence）；
  **不实施 R2 退守**（在层归属被**单独**重裁前，不得把 `Belief < DirectedRelationshipState < Derived` 的层排序改动排入 work order）。
- **裁决者**：Architect。

---

## C-P9 — 单一 blocker register + Work Order 重分类（**Architect 决议，不是文件改动**）

- **目标**：**不触碰 canonical 文本。** 需要的是一次**决议** + 对 `19` / `00_MANIFEST` 两份 register 的合并。
- **决议内容**（`ADJ3` Q8 + `K-C44` + `L-C17`/`L-C18` + `K-C45`/`K-C46`）：
  1. **接受 `ADJ3` 的 blocker 四分类**（A 架构 4 项 / B 研究设计 2 项 / C 环境治理 3 项 / D 负结果 2 项 / E 尺度冲突 1 项）。
  2. **修三处 register 缺陷**（否则 join 会产出错误数字）：`B-3` 编号冲突、成员不相交、`B-4` 双重分类（见 `REJECTED_OR_WEAK_FINDINGS.md` R-4）。
  3. **把 8 个「Work Order」重分类为 3 决策 + 3 派工 + 1 基础设施请求 + 1 书目核对**（`K-C44` `WRONG-SCOPE`：
     `19` §7 抬头把**两种不同性质**的批准混为一谈——(a) 因 canonical mutation 需 Human 主权批准，与 (b) 仅因 Work Order 边界而需新派发）。
  4. **把 8 个 blocker 中的 6 项从「待办」移出**：`B-1`（基础设施）、`B-2`/`B-7`（永久文献/工具缺口）、`B-3`/`B-4`（负结果不该占编号）、`B-5`（契约约束）。
  5. **重排优先级**（`L` top_rec 4 + `ADJ3` Q7）：
     `N1a(提案) → N3(词表) → N5a(矩阵) → N5b(对齐) → N2(裁决 memo) → N4(条件) → D04(标定) → N7(HOLD) → N8(DROP)`。
     **保留** `19` 对 N1→N7 的依赖顺序判断（`ADJ3` Q7 判它**正确**）。
  6. **把「唯一的真正阻塞项」这个标签撤掉**（`ADJ3` Q7：4 阻塞级 + 1 死锁 与「唯一」并存）。
- **能否停在 proposal**：**可以**，但**它必须在其它任何 canonical 改动之前决议**——
  因为「阻塞」是否分类决定了 Architect 面对的是 8 个待修项还是 3 个（且只有 1 个需要他本人裁决）。
- **裁决者**：Architect。

---

## C-P10 — `B2` null 的重定义（**CONDITIONAL**）

- **目标**：`docs/research/overnight-2026-09-27/16_EMPIRICAL_VALIDATION_PROTOCOL.md`（`§7` 的 `B1`/`B2`/主判定规则）
  与 `#29` issue body。**注意：这不在 `docs/foundation/*` 内**，故严格说不是 canonical 变更；
  列出是因为它是本轮**最便宜**的一处修复，且若随 `#29` 落地则需 issue 变更。
- **三方无争议、必须做的**（`D-C19` / `EV3` Claim 2 / `ADJ2` Q2 一致）：
  1. 把 `B2` 从 `16:197` 的「**配对地**击败 `B1` 与 `B2`」中**删除**（被 `B1` 严格支配 ⇒ 那一半恒真），改标 `B2_DIAGNOSTIC`。
  2. **删掉三处措辞**：「本协议认为最重要的一条 null」「已经击败过一个候选」「已核实证伪」。
  3. **改写 rationale**：换成 Lavner 的**实际**发现逐字——
     「起点值对轨迹组的区分力强于所测风险变量的变化率」（`Across all predictor variables, initial values afforded stronger discrimination of outcome groups than did rates of change in these variables`），
     并注明它讲的是 **predictor 变量**，不是 outcome 的人内斜率。
  4. **新增 `N7_UNDIRECTED_SCORE`**：把 `Z[k,i→j]` 与 `Z[k,j→i]` 合成单一无向分数。
     它是**唯一直接测本项目中心表示主张**的 null。独立支撑：`19:62`「在 16 个已审计数据集中，**只有 1 个**（速配）提供无外部假设的 `DIRECTED_EDGE` 双分量，而它**没有第二个时间点**」。
  5. **新增 `N8_LEVEL_CONDITIONAL_SLOPE`**：Lavner 真正赢下的结构 = `06` 判 G 的形状。**这是唯一能真正测 DVA 交互的模型，必须在 null 集里**，否则 DVA 的判 G 无参照物。
  6. 另修 `06:489`（「S19 正是它赢了」）与 `06:901`（「概率最高的结局：被拒绝（初始差异胜）」→ 应改为「**被重写为 level-conditional slope**」）。
- **CONDITIONAL — 改名与否**（`CONTESTED_FINDINGS.md` X-6）：
  - `ADJ2` 要求改名（`B2` → **`B2_LEVEL_PLUS_RW`**，采用 `06:488` 的 `E(τ) = Level(τ₀) + 随机游走 + 误差`），
    理由：「现名 `SELECTION_ONLY` 同时出现在 `16:203`（平）与 `06:488`（随机游走），是 PR 内最危险的一处同名异义」。
  - `EV3` 判该子命题（2d）**`IMPRECISE`**，并指出：**若 `16:203` 的「无 wave-to-wave 增量」= `06:488` 的「只起点，无 slope」（含随机游走），则 2d 完全错误，`D-C19` 第 (1) 条应撤回。**
    `EV3` 自陈这是「`D-C19` 唯一可能整条崩塌的支点，我承认它脆弱」。
  - **parent 不裁定。** 需要 Architect 读 `16` §7.1 一行原文即可定。
- **另一处未闭缺口**（`EV3` 明确）：若 `B1`/`B2` 的**报告指标**不同（例如 `B2` 报方差成分分解），则配对检验在**报告层面**仍有意义 ⇒ 「被 `B1` 支配 → 冗余」在报告层面不成立。`EV3` **未读 `16` §7.1**。
  `ADJ2` 则**未读 `06` N1 原文**。⇒ **两个子点都需要一行文档级确认，不需要外部取样复核。**
- **裁决者**：Architect（读两行原文即可结清）。

---

## C-P11 — `Disclosure` 作为 `Action/Event` 子类型

- **目标**：`docs/foundation/CURRENT_ARCHITECTURE.md` §6（`Action/Event` 子类型表）
- **建议改动**：新增 `Disclosure` 作为 `Action/Event` 的子类型。
- **证据**（`E-C19` —— lane `E` 判 `requires_canonical_change: YES` 中**唯一**一条 `ACCEPT` 的）：
  「不披露（non-disclosure）不是一个信息缺失，而是一个**关于一个 `Behavior` 的断言**；
  `NonDisclosure` 需要第三个输入「`ι` 确实有东西没披露」，这只能来自 `Action/Event` 层的 `Disclosure` 记录，**不能是 belief 层的字段**。
  因此『部分披露的表示不在 belief 层，而在 action 层』。」
  论证成立、与 §6 无冲突、**不新增构念**；且它是 `08b` 最小层唯一的外部依赖（`NonDisclosure` 不可求值 → `CB-B3` 预期 `MAPPING_FAILURE`）。
- **能否停在 proposal**：**可以，但形态需 Architect 裁决，且措辞必须从「持续的不可及性」收紧为「一次披露/不披露的动作」**，
  否则会落进 `Constraint` 而非 `Action/Event`（`CURRENT_ARCHITECTURE.md:190` 的先例）。
- **裁决者**：Architect。**本 packet 不实施。**

---

## C-P12 — Gate A 归因推理的 `⊥` 偏算子前置检查

- **目标**：`docs/foundation/PARAMETER_CONVERGENCE_V0_1.md` §15 Gate A（若采纳）
- **候选内容**（`D-C32`）：把「Gate A 的归因推理是否按算子组合实现」作为一条**前置工程检查项**加入 Gate A。
- **证据**（`D-C32`，`D` 自陈「这是本 lane 唯一一条**不是方法限制、而是关于 LHRM 自身形式化正确性**的发现」）：
  `06:53-68` 的 `RULE-⊥`（MH1）把 `AGENTS.md:24`「Unknown/missing data must remain explicit」写成数学；
  **已知形式风险（U4）**：`⊥` 规则使更新算子成为**偏算子**，偏算子在格上不一定满足结合律或可逆性，
  若 Gate A 的覆盖推理依赖算子组合，则**归因会出错**。
- **不能停在 proposal，也不能现在写入 canonical**（`ADJ2` 原文）：
  > 若 Architect 认定 Gate A 的归因推理按算子组合实现，则需在 `PARAMETER_CONVERGENCE_V0_1.md` §15 Gate A 加一条前置条件
  > ——**但现在不能写进 canonical，因为 U4 本身是 `UNKNOWN`**（`06:68`）。**停 proposal。**
- **`ADJ2` 的独立限定**：`D-C32` 是**自审，不是发现**——`06:53-55` 自己写明这是「架构候选而非经验发现」，且 `U4` 状态为 `UNKNOWN`。
  `06:991-994` 本身就是这个请求。
- **裁决者**：Architect（形式化选择由 Architect 裁决，不需新证据）。

---

## C-P13 — 构念可观察性 / 锚点登记表（`NOT_YET`）

- **目标**：`docs/foundation/CURRENT_ARCHITECTURE.md` §9 或 §10 前置条件
- **候选内容**（`E-C16`）：建立「哪些构念原则上可被直接观察 / 哪些只能被报告 / 哪些只能被推断」的登记表。
- **证据**（`E-C16` —— `E` 判为**本 lane 唯一的 head-of-list 阻塞项**）：
  `07 §11-3` 与 `08b §9-1` **从相反方向独立发现同一缺口**。项目内不存在该清单 ⇒
  `g = FIRSTHAND` 与 `structurally_unobservable` **都无法落地**。
  它同时阻塞：`07` 的 `Unknown` 类型学落地、`07` 的 `⊑` 程序（I9 需依赖表）、`08b` 的整个 belief 层、
  以及 `02` 已局部提出的单构念登记（`coordination` 不可知觉）。
- **性质**：**它是一条 Architect 裁决，不是研究问题**（`07` 自己的定性正确）。
- **能否停在 proposal**：**不能**——但它是**登记表的建立**，不是任何既有构念的改动。
- **裁决者**：Human / Project Architect。

---

## WITHDRAWN — 被阶段 2 推翻或无授权的 canonical 变更候选

### C-W1 — 值类集合是穷举集、存在逻辑矛盾（原 `G-C4` / `G-C5`）

- **原主张**：`requires_canonical_change: YES`，**不能停在 proposal**；`11` 把它标为 "proposal only" 是**过度保守**；
  `G` 判这是它「唯一必须落到 canonical 而不能停在 proposal 的项目」。
- **推翻**：`EV3` Claim 1 `REFUTED`（见 `CONTESTED_FINDINGS.md` X-5）。
  值类清单是**许可式**；canonical **已有** `BoundaryRule_(A,B,domain)` 具名槽位与针对 `性欲` 的 worked example。
- **残留**：以**缩小形式**进入 C-P5（`PLAUSIBLE`）。
- **注意**：`G-C4`（值类分析未进码表）在本 verdict 下从 `YES` 降为 `NO`；`G-C11`（`NA` 判定本身）`HOLD_FOR_EVIDENCE`。

### C-W2 — 引入 lattice / 模态 / 析取状态空间（`17` F4）

- **原主张**：`I-C19` 的 `requires_canonical_change: YES`（若要保留「需模态层」这一主张，canonical 必须接受 lattice）。
- **处置**：`REJECT`（**作为架构主张**）。MacDonald 是**冗余证据**，Zoppolat **支持**现有分离。
  ⇒ 真实的现象改写为 **Gate C 冗余条目** + **已有 Observation/Belief 分离条目**。

### C-W3 — 新增 `PowerLevel_(i->j)` 节点（`02b` §5.3）

- **原主张**：`A-C14` 的 `requires_canonical_change: YES`（若采纳 `PowerLevel_(i->j)`，需改 `PARAMETER_CONVERGENCE` §9 R2）。
- **处置**：`HOLD_FOR_EVIDENCE` —— 该节点在语义上是 §9 R2「不先设一个独立『权力值』」的**反面**；
  其三条量化断言（70–75%、actor/partner 正相关、引文句）在摘要层**全部不可核实**；
  其最具决策性的单个数据点（RPI 与 dependence 不相关）`UNVERIFIABLE_HERE`。
  **它不进入 canonical 候选表。**

### C-W4 — MGS-C 对 `Trust` / `Caregiving` 的降级（`02b` §9）

- **原主张**：`A-C9`（MGS-C 的 `Caregiving` 删除）+ `A-C20`（以 E4a 为依据的 `Trust` 降级）+ `A-C21`（强制 `domain`）。
- **处置**：
  - `Caregiving` 删除 → `HOLD_FOR_EVIDENCE`：**`Caregiving` 没有任何边支撑**（`Dedication` 有 E8 支撑）。
  - `Trust` 降级 → `REJECT`（以 E4a 为依据）：**`02b` 从未定义 `E4a`**（`A-C6`，`ADJ1` 独立复核 `02b:225-247` 确认）；
    `E4` 判定为 `CONTESTED`，而 §5.1 的小节标题与 MGS-C 的 basis 都已按「`Trust` 降为 facet」处理。
    **在 `02b` 定义或删除 `E4a`/`E4b` 之前，MGS-C 的 `Trust` 降级不得被引用为 `02b` 的结论。**
  - 强制 `domain` → `REJECT`（见 C-P3）。
- **canonical 本体不需要改**（`ADJ1` Q4）：`PARAMETER_CONVERGENCE` §4 D4/D5 **本轮不需要因本冲突改动**
  ——canonical 现在并列 `Trust` 与 `AttachmentSecurity`，与 `02b` §5.1 的保守结论（两者都留）**一致**。

### C-W5 — 依据 `NOT_IDENTIFIABLE` 降级 D7 `Dedication` / D8 `OutcomeDependence`

- **原主张**：`03` §4.1 建议把两个 canonical candidate 降级。
- **处置**：`RECLASSIFY_AS_METHOD_LIMIT` —— **这两条降级建议应整体打回**（`B` top_rec 第 1 条）。
  `NOT_IDENTIFIABLE` 的语义门槛（结构上做不到）必须**先裁决**，再谈降级。
  `ADJ2` 补充：`APES` 的工具阻塞点应写成「**未定位到已验证的关系层 dependence 工具；且经典互依工具文献未被检索**」，**不能**写成「结构上不可测」。
  `03:253` 的 `D7 = NOT_IDENTIFIABLE` 本身应**接受为报告自陈**。
- **canonical 本体不需要改。**

---

## 不构成 canonical 变更、但必须修的**研究侧**更正（索引）

以下条目会改动 `docs/research/overnight-2026-09-27/*`，**不在本文件授权范围内**，但 Architect 若要修订 PR #31 必须知道它们存在：

| 位置 | 更正 | 来源 |
|---|---|---|
| `00_MANIFEST` §2b / §4 B-9 / `08b` 计数 / `[S15]` | 见 manifest §7 M-1…M-4 | `J` + `EV2` |
| `A01` §1.1 | 「100%」→「95.5%」 | `J-C13` |
| `A04` §2.1 / §2.3 / §4.2 / §4.3.4 / D5 | 见 manifest §7 M-6…M-9 | `J` + `EV2` |
| `02b` §4 判定列 | 降为「未经规则推导的作者判断」；加 `source_refs` 列；定义/删除 `E4a`/`E4b`；三张图降为非规范性插图 | `A` top_rec 3 + `A-C1`…`A-C6` |
| `02b` §6 的 `R1`–`R11` | 改为 `RES-1..RES-11`（编号空间隔离） | `A-C12` |
| `02` §10 | 勾号拆为 `CITATION_VERIFIED` 等；修 §10 页码 343-356 → 344-354 | `A-C30` + `ADJ1` Q4 |
| `02` §3.4 / §3.9 | 强制 `domain` → 推荐 facet | `A-C21` + `ADJ1` Q4 |
| `03` §2.5 / §2.8 / §7 / §8 | 5 处引用错误 + 3 个漏掉的已验证工具（ECR-RS `10.1037/a0022898`；PICS；Fraley et al. 2011 JPSP 101:974–992） | `B` top_rec 2/3 |
| `03` §4.1 | `T7`(`UNVERIFIED_DOI`)→`T6`(Hsu 2019 学位论文)→「D4 `Distrust` 升级为独立候选」整条链降为 `NOT_ASSESSED` | `B-C14` |
| `03` §1.2 / §8 | 统计口径重出（73 行 / 6 处重复） | `B-C1`/`B-C5`/`B-C15` |
| `04` §5.1 | 补 SOEP 行；补 HRS access-continuity 注记；G2 改述为单源扩散 | `C-C13`/`C-C15`/`C-C36` |
| `04` §6 / §10 | 撤回 SOMAR VDE「唯一可行路径」 | `C-C14` |
| `04` §9 U4 | `UNKNOWN_AS_OF` → 已解（全面禁止） | `C-C11` |
| `04` D09 | CLOC 分类理由必须改（结论倾向保留） | `C-C24` |
| `05` §12 建议 1 | 驳回；I1–I17 按四类重写 | `D` top_rec 1 |
| `06` §2.3 / §3.2 / §8.7 / §9 | 后果类型改标；功效护栏跨律通用；判 H/N 移入不可证伪清单 | `D` top_rec 6 |
| `07` §2.3 / §5 / §8 / 证据等级表 | 序方向反转；15→19；19 条的可执行性分类；`[ESTABLISHED]` 入表 | `E-C3`/`E-C11`/`E-C12`/`E-C13` |
| `07` / `08b` | 合并 Unknown 编码（**两轴分离**） | `E-C23` + C-P5 |
| `08b` §3 | 结论以 §3 正文为准；`M` 标为「有意的设计选择，不是最小性证明」 | `E-C21`/`E-C18` |
| `09` §5.2 / §5.4-3 / §9.2 / §9.6 | 作者串统一为五人；两处方法→本体滑坡改写；K9 换掉；K1/K5/K7/K8 修补 | `F` top_rec 2/3 |
| `09` §4.4 | 补 ESM/IL/EMA escape clause | `F-C11` + `ADJ2` rec 5 |
| `10` §4.8 / §5 / §12 | 删「唯一」与「真涌现」；合并双重计数；加 `page_verified` 列 | `F-C18`/`F-C30`/`F-C31` |
| `10` §2 / §4 | `TP` 实现规格改为对称聚合 | `F-C23` + C-P4 |
| `11` §2 / §3.1 / §3.7 / §4 / §6.1 / §9 | 五处 `Trust` 判定撤回；值类发现改述；`RoleContract` 保留 `Role`；格统计重算；三处书目修正 | `G-C10`/`G-C30`/`G-C3`/`G-C24` |
| `12` §0 / §3.1 | headline 改述；二值化推论补例外句 | `G-C17`/`G-C16` |
| `13` §2.2(c) / §7 / §9.6 / §12 / §13.2 | 转述方向更正；补 Fixture 003 权利边界；数字与归属更正；PROV 归属；六指标降为非充分 | `G-C28`/`G-C22`/`G-C20`/`G-C23`/`G-C21` |
| `14` §2.5 / §9.1 / §9.2 / §3 / §5 / §6 | 撤回 Lalk；删两项不存在的 prior art；7 条 O-row 重写；工期估计撤回 | `H` top_rec 1/2/3 |
| `17` §0 / §1.3 / §3 / §4 / §5 / §9.3 / §10 / §11 / §12 | 补 temp 目录声明；删前提；重标 F3；F9 表重出；S 编号修复；R1/R5 立即跑；补组织变量原句；「所有卷期页均经 Crossref 核验」撤回 | `I` + `ADJ1` Q2 |
| `18` CF-00 / CF-03 / CF-08 / N-01 / N-08 / §10 | 补扫描协议；逐 lane 枚举；补 R06→R02 依赖链；补否定型冲突面；`CR-/NR-` 码表；Unknown 两轴合并 | `K` |
| `19` §1 / §2 / §3 / §4 / §5 / §7 / §8 / §9 | A1–A12 → N-A1…N-A12；四 blocker 分类；B2 重定义；格统计删除；L3/L5 两格改写；依赖顺序重排；`MERGE/REJECT` 措辞；B-1…B-8 → 四分类 | `ADJ2` + `ADJ3` + `L` + `K` |
| `19` WO-N1…N8 | 拆 N1a/N1b；N3 词表两轴合并；N7 加四个前置；N8 降为 bibliographic check | `L` top_rec 1/4/6 |
