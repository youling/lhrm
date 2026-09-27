# CROSS_LANE_VERDICT_MATRIX — Round 2 review swarm over `youling/lhrm#31`

> 本文件是 **mechanical join** 的产物：每一行直接来自某个 review child packet 的 `verdict_matrix` 字段抽取，
> parent 未重读被审报告、未改写 verdict、未合并任何两行。
> 生成方式见 `REVIEW_SWARM_MANIFEST.md` §5（join 规程）。

**被审对象**：`youling/lhrm#31` @ `8adcf0bacc45c0feb5c14e65e2a45346dd488b43`（25 份报告，本 swarm 只读不写）。
**统一 verdict 词表**（`REVIEW_CONTRACT.md` §4）：`VERIFIED | PLAUSIBLE | CONTESTED | UNSUPPORTED | WRONG-SCOPE`。

## 0. 读法与免责

- `verdict` 列保留 child 的**原始措辞**（含 `（…）` 限定），未做归一化。
- `primary` 列是 parent 为便于计数而抽出的**首个**枚举词；`MIXED:*` 表示该行同时给出两个枚举词（child 显式分项判定），
  `NOT_ENUM` 表示 child 使用了词表外的记法（如 `UNVERIFIABLE_HERE` / `REPRODUCED_BY_ME`）。**两者都不构成 parent 的改判。**
- `claim` 列截断到 300 字符、`verdict` 150、`recommendation` 110、`corroboration` 46。**完整原文在各 child packet 内**；
  packet 未随本 PR 提交（体量 1.5 MB），权威指针 = `claim_id` + lane cluster 对应的被审报告（lane → 报告映射见 manifest §3）。
- **`corroboration` 列必须与 verdict 一起读。** `NON_INDEPENDENT` / `RELAYED_NOT_INDEPENDENT` / `SAME_SOURCE` / `TRANSITIVE`
  的行**不得**因「别的 lane 也这么说」而升级（`REVIEW_CONTRACT.md` §4 硬规则）。
- `canon` 列 `YES` 只表示 child 判定需要 canonical 变更；**是否越过 proposal 由 Architect 决定**，见 `CANONICAL_CHANGE_PROPOSALS.md`。

## 1. 计数（`primary` 归一化，仅供分诊）

| primary | rows |
|---|---:|
| `CONTESTED` | 52 |
| `MIXED:CONTESTED+VERIFIED` | 2 |
| `MIXED:PLAUSIBLE+CONTESTED` | 1 |
| `MIXED:PLAUSIBLE+PLAUSIBLE` | 1 |
| `MIXED:PLAUSIBLE+UNSUPPORTED` | 3 |
| `MIXED:PLAUSIBLE+VERIFIED` | 3 |
| `MIXED:PLAUSIBLE+WRONG-SCOPE` | 4 |
| `MIXED:UNSUPPORTED+PLAUSIBLE` | 1 |
| `MIXED:UNSUPPORTED+VERIFIED` | 3 |
| `MIXED:UNSUPPORTED+WRONG-SCOPE` | 1 |
| `MIXED:VERIFIED+PLAUSIBLE` | 9 |
| `MIXED:VERIFIED+UNSUPPORTED` | 4 |
| `MIXED:VERIFIED+VERIFIED` | 2 |
| `MIXED:VERIFIED+WRONG-SCOPE` | 3 |
| `NOT_ENUM` | 34 |
| `PLAUSIBLE` | 66 |
| `UNSUPPORTED` | 52 |
| `VERIFIED` | 105 |
| `WRONG-SCOPE` | 51 |
| **合计** | **397** |

按 lane 的行数：

| lane | cluster | rows |
|---|---|---:|
| `A` | construct ontology / redundancy | 33 |
| `B` | measurement instruments / proxies | 24 |
| `C` | datasets / access / rights | 36 |
| `D` | statistics / identification / transition laws | 40 |
| `E` | belief / partial observability / knowledge | 21 |
| `F` | dynamics / hysteresis / pair-state emergence | 33 |
| `G` | general dyad scope / ABM / LLM layer | 30 |
| `H` | paper positioning / novelty | 57 |
| `I` | red-team falsifiers / Gate A-B-C | 30 |
| `J` | citation / provenance recheck | 23 |
| `K` | cross-lane contradiction map | 50 |
| `L` | actionability / next-work-order filter | 20 |

> 注：lane `E` 有 4 行、`H` 有若干行、`K` 有若干行的 `claim` / `verdict` 为空或非标准布局（child 用了不同字段名或子表），
> 机械抽取未能覆盖。这类行的实质内容在 `HIGH_CONFIDENCE_FINDINGS.md` / `CONTESTED_FINDINGS.md` 中按 child 的 `top_recommendations` 承接，
> **不得**据本表推断「E 只有 21 条结论」或「K 只有 50 条」。

## 2.A — lane `A`（construct ontology / redundancy）

| claim_id | primary | verdict（原文） | canon | corroboration | recommendation | claim（截断） |
|---|---|---|---|---|---|---|
| `A-C1` | `UNSUPPORTED` | UNSUPPORTED`（标签与自定规则之间无推导关系） | NO |  | RECLASSIFY_AS_METHOD_LIMIT` — 把 `02b` §4 判定列降为「未经规则推导的作者判断」~ | 02b` §2 声明 `INDEPENDENT` = 「至少 3 个 lens 有正面分离证据」；实算 6 条 `INDEPENDENT` 中 4 条不满足。 |
| `A-C2` | `UNSUPPORTED` | UNSUPPORTED | NO |  | RECLASSIFY_AS_METHOD_LIMIT` — `SUPPORTED_REDUNDANCY` 须按 l.1~ | 02b` l.11 声明「每一条 `SUPPORTED_REDUNDANCY` 都至少有一条**定义层或量表层**证据，绝不只靠相关系数」；E8 / E11b / E15 的 `S` 与 `F` 单元格均无支持。 |
| `A-C3` | `UNSUPPORTED` | UNSUPPORTED | NO |  | REJECT`（E11b 的 `SUPPORTED_REDUNDANCY` 标签），改按 §5.4 已有表述记为「条件预~ | E11b 判 `SUPPORTED_REDUNDANCY（作为驱动量）`，但 §5.4 结尾写「`r = 0.08` **不**证明 `ValueCongruence` 语义冗余。它证明的是……**条件预测效度不足**」。 |
| `A-C4` | `UNSUPPORTED` | UNSUPPORTED`（对这 11 条边的判定而言） | NO |  | HOLD_FOR_EVIDENCE`（E5、E17 两条边）；边表加一列 `source_refs` 为 `ACCEPT~ | §4 边表 21 条边 x 5 lens 共 105 个单元格，**无任何来源列**；E5、E6、E9、E11b、E11c、E13、E14、E15、E16、E17、E18 共 11 条边的判定无法追溯到 `02b` 内的具体引用编号。 |
| `A-C5` | `UNSUPPORTED` | UNSUPPORTED`（图与表至少一方错，报告未记录差异） | NO |  | RECLASSIFY_AS_METHOD_LIMIT` — 以 §4 边表为唯一 SSOT，三张图降为非规范性插图。 | §3.1 图例定义 `---` = 「判定为 `INDEPENDENT` 的边」，但 E1（`CONTESTED`，l.227）与 E18（`CONTESTED`，l.247，图中出现两次）都用 `---` 绘制；§3.2 ASCII 另标 E3 为 `CONTESTED/mod`，而边表 E3 的 `strength` 是 `STRONG`。 |
| `A-C6` | `UNSUPPORTED` | UNSUPPORTED | NO |  | RECLASSIFY_AS_METHOD_LIMIT` — 定义 E4a/E4b 或删除其引用；在此之前 MGS-C ~ | E4a`（l.112、l.153、l.529）与 `E4b`（l.155、l.493）被当作独立边使用，但 §2 与 §4 只定义了一个 `E4`；ASCII l.155 进一步写「(E4b 残余 INDEP/mod)」，即断言 E4b 判定为 `INDEPENDENT` — 边表从未如此判定。 |
| `A-C7` | `WRONG-SCOPE` | WRONG-SCOPE`（`attraction` 与 `Liking` 是不同构念；把二者混接正是本 lane 要防的 H5 型错误） | NO |  | REJECT`（该接法），改用独立 `ATTRACTION` 节点或删除该边。 | 边表 E11b/E11c 的 A 侧是 `attraction`，图（l.122-123）却把两条边接到 `LK`（= D1 Liking），未作任何标注。 |
| `A-C8` | `UNSUPPORTED` | UNSUPPORTED`（就「三者互相竞争」这一表述） | NO |  | RECLASSIFY_AS_METHOD_LIMIT` — 重新表述为「MGS-C 与两个被记录为失败的对照设计」，删~ | §9 声称「三者互相竞争」，但 MGS-A 与 MGS-B 所列「支持边」与其自身节点集无关，且其中一条（E2）判定为 `INDEPENDENT`，即**反对**把它们合并。 |
| `A-C9` | `UNSUPPORTED` | UNSUPPORTED`（对 `Caregiving` 的降级） | YES` — 若 MGS-C 被采纳，需改 `PARAMETER_CONVER~ |  | HOLD_FOR_EVIDENCE`（MGS-C 的 `Caregiving` 删除）；MGS-C 整体 `ACCEPT~ | MGS-C 的 directed basis 只保留 4 项（Liking / SexualDesire / AttachmentSecurity / OutcomeDependence），`Caregiving` 与 `Dedication` 双双降入 derived；其中 `Dedication` 有 E8 支撑，**`Caregiving` 没有任何边支撑**。 |
| `A-C10` | `PLAUSIBLE` | PLAUSIBLE`（清单存在且有用），**缺口** = 真正凭经验证据成立的残余只有 R3、R4（部分 R7/R11）；其余是索引原则的重述。 | NO |  | RECLASSIFY_AS_METHOD_LIMIT` — §6 重命名为「不可合并的通道/索引区分」，并把 R1 移~ | §6「不可消去残余清单」自陈为「即使激进 reduction 也大概率存活」的项；但 R1 自述是「架构不变量，非经验发现」，R2/R5/R6/R8/R9/R10 的内容是 reported-vs-perceived、actual-vs-perceived、arousal-vs-desire、global-vs-specific、non-complementarity 等**通道/索引区分** — 这些本就是 `CONSTRUCT_SCOPE_DIRECTIONALITY.md` §1/§3 ~ |
| `A-C11` | `PLAUSIBLE` | PLAUSIBLE`（作为审计发现），缺口 = 报告未做内部去重，parent join 时若按节引用会把同一主张计 3-4 次。 | NO |  | ACCEPT_AS_PROPOSAL`（durable writeback 时提供 C->H->R->E 交叉索引，并在~ | C1==H1、E4、§5.1；C2/C3==§5.3、H6、R7；C4==E8、§5.2；C5==§5.4、E11b、H5、R6；C7==§5.6、R8；C9==E13、R9。R11==H10==E9==§10.4。 |
| `A-C12` | `PLAUSIBLE` | PLAUSIBLE`，缺口 = 报告与 canonical 均未声明编号空间隔离；join 时必然碰撞。 | NO`（canonical 无需改；是研究侧编号问题） |  | ACCEPT_AS_PROPOSAL`（writeback 时把 `02b` 的 R 改为 `RES-1..RES-11~ | 02b` §6 用 `R1-R11` 表示「不可消去残余」；`PARAMETER_CONVERGENCE_V0_1.md` §9 已用 `R1`-`R5` 表示 `Derived / Readout` 清单。同 PR 内两套 `R` 编号语义完全不同。 |
| `A-C13` | `CONTESTED` | CONTESTED`（同一 cluster 内两侧不相容断言，按 contract §4 指名对立方：`02` §3.3/§5.6 对 `02b` §6 R2/§8 C6） | NO |  | RECLASSIFY_AS_METHOD_LIMIT` — 统一采用已核实的 .66/.26，或给 `.25` 标明确~ | 02` §3.3/§5.6 报「男性 r = .66，女性 r = .26」；`02b` §6 R2 与 §8 C6 报「女性 r = .25」，并把该数字同时挂在 Chivers 2010 与 Meston & Stanton 2018 两个来源上。 |
| `A-C14` | `MIXED:PLAUSIBLE+UNSUPPORTED` | PLAUSIBLE`（方向层） / `UNSUPPORTED`（量级与引文层）。缺口 = 摘要未含 70-75%、未含 actor/partner 相关方向、未含该引文句。 | YES` — 若采纳 `PowerLevel_(i->j)`，需改 `PARA~ |  | HOLD_FOR_EVIDENCE`（`PowerLevel_(i->j)` 不进入 canonical 候选表）。 | §5.3 用三条来自 `Overall & Hammond` 的断言支撑新增节点 `PowerLevel_(i->j)` 与 C2/R7/R1；三条在摘要层均无法确认。 |
| `A-C15` | `NOT_ENUM` | UNVERIFIABLE_HERE`（按 contract §3 记为不可核实，不记结论） | NO`（本条不要求改 canonical；但它使 `A-C14` 更难被接受） |  | HOLD_FOR_EVIDENCE` — H6 的严重度从 `HIGH` 下调，直到取得 RPI 原始文献指针。 | §5.3 的核心发现「直接 power 测量不与 dependence 相关（RPI 与 mutuality of dependence 不相关）」是 H6 从「双计」翻转为「漏计」的唯一支点；其来源 Sprecher & Felmhee 的 RPI 研究在本 lane 无法核实。 |
| `A-C16` | `PLAUSIBLE` | PLAUSIBLE`，缺口 = 引文原句未在摘要层确认（正文未打开）；「循环定义 dependence 是 power 的 base 还是 outcome / Thibaut & ~ | NO |  | ACCEPT_AS_PROPOSAL`（保留方向；把「原话」降级为「转述」并标 `NOT_OPENED`）。 | 「2022 年前 k=319 个 power 测量的系统检视」及「2022」这一时间窗**成立**；但被当作「结论原话」引用的 proxy-劝阻句在摘要中不存在。 |
| `A-C17` | `UNSUPPORTED` | UNSUPPORTED`（引文归属） | NO |  | ACCEPT_AS_PROPOSAL`（要求 `02b` 在 §5.3 为每条断言标注具体引用编号；当前该段引用不可追溯~ | §5.3 的「power 测量系统综述」段落所依赖的循环定义论证（Thibaut & Kelley 1959 / dependence 是 power 的 base 还是 outcome）在引用表里没有专属条目；同段落语境中最接近的 [28] 是一篇 **relationship quality** 测量综述，而 [28] 在 §6 R11 中被用于另一件事。 |
| `A-C18` | `UNSUPPORTED` | UNSUPPORTED`（就「排序」这一推论）。缺口 = 被排序的另一侧（`Satisfaction`）的未解释方差在同一节被自陈为「**未知**」（l.291），因此该排序在数学~ | YES` — 若采纳该反转，需改 `PARAMETER_CONVERGENCE~ |  | REJECT`（按当前形式重新分类）；`ACCEPT_AS_PROPOSAL`（改写为研究问题）。 | §5.2 主张「按经验残余量排序，LHRM 当前的分类很可能反了」— 即 `Dedication` 比 `Satisfaction` 更接近 derived。所用 R2 = .54 来自一篇对**互相关**的 meta 分析。 |
| `A-C19` | `CONTESTED` | CONTESTED`（两侧都是本 cluster 内的可信报告；对立方指针 = `02` §3.4/§4#4 对 `02b` §5.1/§9 MGS-C） | YES` — `PARAMETER_CONVERGENCE_V0_1.md` ~ |  | HOLD_FOR_EVIDENCE` — 这是本 lane 唯一必须提交 Human/Architect 仲裁的分歧；~ | 02` §3.4 判 `Trust` = `KEEP`，称其为「13 个候选中最稳的一个」，并强制 `domain` 索引；`02b` §5.1 判「`Trust` 与 `AttachmentSecurity`：**不是两个独立 primitive**，是一个共享内核加两个非零残余」，其 MGS-C 把 `Trust` 降为 `AttachmentSecurity` 的部分 facet。 |
| `A-C20` | `UNSUPPORTED` | UNSUPPORTED`（MGS-C 的 Trust 降级） | NO`（本条不单独要求；随 `A-C19` 处理） |  | REJECT`（以 E4a 为依据的降级），改为把 Trust 降级明确标注为「依赖未定义子边 E4a」。 | E4 判定为 `CONTESTED`，但 §5.1 的小节标题与 MGS-C 的 basis 都已按「Trust 降为 facet」处理，未登记该边为 `CONTESTED` 所带来的张力。 |
| `A-C21` | `WRONG-SCOPE` | WRONG-SCOPE`（组织情境的 trust 构造被用来规定 Human-Human 亲密 dyad 的必需字段） | YES` — `PARAMETER_CONVERGENCE_V0_1.md` ~ |  | ACCEPT_AS_PROPOSAL`（把「强制 domain 索引」降为「推荐 facet + 记录 domain 缺~ | §3.4/§4#4/§9.1 主张 `Trust` 的 signature **必须**含 `domain`（财务/身体/育儿/情感脆弱/决策委托），其决定性证据是 Schoorman, Mayer & Davis (2007)。 |
| `A-C22` | `WRONG-SCOPE` | WRONG-SCOPE`（该 meta 的标题与摘要对象是 **sexual arousal**，不是 sexual desire；`arousal 不等于 desire` 是 `~ | YES` — `PARAMETER_CONVERGENCE_V0_1.md` ~ |  | ACCEPT_AS_PROPOSAL`（并加注 E3 = `CONTESTED`）。 | §3.3 把 Chivers et al. (2010) 列为 `SexualDesire` 的「最硬边界」，并据此**强制** `SexualDesire` 与 `PhysiologicalArousal` 分坐标、每个 `StateCoordinate` 携带 `measurement_channel`。 |
| `A-C23` | `MIXED:UNSUPPORTED+PLAUSIBLE` | UNSUPPORTED`（该否定性断言）；`PLAUSIBLE`（方向层「关系级量表缺失」）。缺口 = 该句不在摘要层；且即便在正文，它是**引入该工具的那篇论文**对自身贡献前的~ | NO`（该判定若成立只是给 canonical §4 D8 的 candidat~ |  | RECLASSIFY_AS_METHOD_LIMIT` — 把 `MEASUREMENT_INFEASIBLE_AT_~ | §3.9/§4#9 判 `KEEP` + **`MEASUREMENT_INFEASIBLE_AT_RELATION_LEVEL`**，自称「本文最重要的判定」；其支柱是「关系级无被广泛接受、可比、验证过的 outcome dependence 量表」与一句标为 `[S28]` **原文明确** 的「no instrument has been [developed to measure all sub-dimensions of interdependence]」。 |
| `A-C24` | `PLAUSIBLE` | PLAUSIBLE`，缺口 = 报告的 delta 基准是 prior report 而非 canonical；§6 标题确实写明「对 **prior report** 的 aud~ | NO`（对这 4 条）；真正需要的见 `A-C25`。 |  | RECLASSIFY_AS_METHOD_LIMIT` — 要求 `02` 补一列「相对 canonical 是否为 ~ | §6 delta 表中至少 4 条（#2 PPR `改层`、#7 Cohesion `改层`、#10 Trust `加条件`、#13 Perceived Commitment）相对 **canonical** 并非变更，因为 canonical 已处在该层。 |
| `A-C25` | `MIXED:PLAUSIBLE+CONTESTED` | PLAUSIBLE`（(a) 的存在）/`CONTESTED`（(a) 的范围）。缺口 = `02` §6 Delta#3 说 canonical「未处理」，但 canonical~ | YES |  | ACCEPT_AS_PROPOSAL`（两处），其中 (a) 须同时登记为 **Gate C blocker**。 | 逐条核对后，`02`/`02b` 真正与 `PARAMETER_CONVERGENCE_V0_1.md` 现状冲突的只有：(a) §4 D7 与 §9 R3 的 `Satisfaction` <-> `Dedication` 层碰撞；(b) §9 R2「不先设一个独立『权力值』」被 `02b` 的 `PowerLevel_(i->j)` 反向挑战。 |
| `A-C26` | `UNSUPPORTED` | UNSUPPORTED`（`SUPERSEDED` 分类）。缺口 = `01` §3 自定 `SUPERSEDED` = 「已被更新的**durable 裁决**或事实取代」，而 ~ | NO`（`01` 是研究文档，不是 canonical） |  | RECLASSIFY_AS_METHOD_LIMIT` — S-I/S-J 改标 `OPEN_GAP`（与 G-04/~ | 01` §4.2 S-I（`SCIENTIFIC` §7.8 把 PPR 列入有向最小核心 -> `PARAMETER_CONVERGENCE` §5 B1 判 Belief layer）与 S-J（Trust KEEP + `C02 distrust` -> §4 D4 降为 Open question）被列入「已显式被取代的东西（`SUPERSEDED` 明细）」；但 S-I/S-J 自己写「两侧均自述非冻结；本文件只记录分歧，不裁决」。 |
| `A-C27` | `UNSUPPORTED` | UNSUPPORTED | NO |  | REJECT`（该交接指令不可执行）。**这是本 packet 的可执行性发现**：`02`/`02b` 实际覆盖的 4~ | 01` §9.1（本 cluster 两份报告的操作性 Work Order 交接）写「从 §7 的 **S-9（F-09 表）**开始，而不是从『重新审计 8 个 construct』开始」；`01` 全文不存在任何 `F-xx` 条目，而 S-9 讲的是 `#23` body 的 Juece surface 与 fixture 001 描述过期，与 PPR / OutcomeDependence / Cohesion / Distrust 无关。 |
| `A-C28` | `UNSUPPORTED` | UNSUPPORTED`（U2 的设计前提已被同 cluster 的另一份报告否掉）。缺口 = 若 Cohesion 已被判为两个 `PerceivedWeNess`，E12 就不~ | NO |  | RECLASSIFY_AS_METHOD_LIMIT` — E12 由「冗余实证问题」改标为「层归属已由 `02` 裁~ | 02` §3.11 判 `Cohesion/We-ness` = `BELIEF_ONLY`（不承认独立 pair latent），而 `02b` 仍把「`AttachmentSecurity` <-> `Cohesion` 是否冗余」当作需要 N>=600 情侣 ESEM 的**因子层实证问题**（E12 = `UNKNOWN`、U2）。 |
| `A-C29` | `WRONG-SCOPE` | WRONG-SCOPE`（检索覆盖不足被写成领域存在性结论） | NO |  | RECLASSIFY_AS_METHOD_LIMIT` — 改写为「本 lane 的检索未发现」；存在性否定需独立系统~ | §5.8 用 2 组 `websearch` 查询后写下「**再次确认** §10 的 `NEGATIVE`：这不是本轮检索不足，是文献里确实不存在」（关于中文 ESEM / bifactor 研究）。 |
| `A-C30` | `MIXED:PLAUSIBLE+UNSUPPORTED` | PLAUSIBLE`（勾号存在）/`UNSUPPORTED`（把它读成「主张已核实」）。缺口 = 勾号的定义域未声明；实测它对应 Crossref 题录可解析，不对应正文/摘要内容~ | NO |  | ACCEPT_AS_PROPOSAL`（durable writeback 时把勾号拆为 `CITATION_VERIF~ | 02` §10 以勾号标注「DOI 已核验」，并在 §5.11 记录 prior report 的 3 条检索失败 + 1 条 DOI 证伪 + 2 处记忆性错误；但 `02` 自身清单里至少有 3 处题录错误。 |
| `A-C31` | `PLAUSIBLE` | PLAUSIBLE`，缺口 = 缺口状态在 PR 内部已部分过时，但这是同一 attempt 内的先后问题，不涉及外部事实错误。 | NO |  | ACCEPT_AS_PROPOSAL`（parent join 时对 G-03/G-04/G-07/G-08 加一行 `~ | 01` §4.3 把 G-03（Gate C 六组攻击面）、G-04（`Distrust`）、G-07（shared latent `Cohesion`）、G-08（`Satisfaction` derived vs primitive）记为 `OPEN_GAP`，指针只指向四份 prior report；而同一 PR 的 `02`/`02b` 已对这四项给出部分答案，且 `01` 与 `02`/`02b` 互不登记对方产出。 |
| `A-C32` | `PLAUSIBLE` | PLAUSIBLE`，缺口 = 复合分类未拆行；G-23 的 `ACTIVE_DEPENDENCY` 相对于 R00 自身完成而言已过期。 | NO |  | ACCEPT_AS_PROPOSAL`（G-22 拆为 4 行；G-23 改 `RESOLVED_IN_ATTEMPT`~ | §4.3 表头声明该表是「开放研究项（`OPEN_GAP` 与 `ACTIVE_DEPENDENCY`）」，但 G-22 在一行内混用两种分类、G-23 把一个已完成的 lane 记为 `ACTIVE_DEPENDENCY`、G-24 在该表内被标为 `CURRENT`。 |
| `A-C33` | `PLAUSIBLE` | PLAUSIBLE`（机械缺陷），缺口 = 报告未说明第二次出现是同一节点还是另一个（per-person vs dyadic）版本。 | NO |  | RECLASSIFY_AS_METHOD_LIMIT` — 要求 `02b` 明确 MGS-C 中 `PowerLev~ | MGS-C 的 `MGS-C derived / readout` 块中 `PowerLevel_(i->j)` 出现两次：一次作为「继续 derived，但新增候选 PowerLevel_(i->j)」（PowerImbalance 行内），一次作为独立条目。 |

## 2.B — lane `B`（measurement instruments / proxies）

| claim_id | primary | verdict（原文） | canon | corroboration | recommendation | claim（截断） |
|---|---|---|---|---|---|---|
| `B-C1` | `UNSUPPORTED` | UNSUPPORTED | NO | NON_INDEPENDENT`（自算，非独立来源） | RECLASSIFY_AS_METHOD_LIMIT` — 计数不可复现属报告编制缺陷，**不得**让 "41/54" ~ | 被审报告自述目录含 41 个独立 instrument family / 54 个可引用条目（§2 L35、§8 L405）。 |
| `B-C2` | `UNSUPPORTED` | UNSUPPORTED | NO | NON_INDEPENDENT | HOLD_FOR_EVIDENCE` — 在 join 时先确认 217/48 的出处 lane；不要把它当作 `03`~ | 我的审计任务书把被审报告描述为"claim of 217 DOI pointers with 48 `UNVERIFIED` flags"；文件内不存在该 claim。 |
| `B-C3` | `PLAUSIBLE` | PLAUSIBLE | NO` — 但**必须停在 proposal**。`PARAMETER_CONV~ | NON_INDEPENDENT`（仅本报告 + 其自引的 jftr ~ | RECLASSIFY_AS_METHOD_LIMIT` — "目录里没找到"是检索覆盖限制，不是"结构上做不到"的 on~ | OutcomeDependence_(i->j)` 这一关系层有向坐标没有现成可用工具；§4.1 据此建议把 canonical 候选 D8 **降级为 `NOT_IDENTIFIABLE`**。 |
| `B-C4` | `CONTESTED` | CONTESTED | NO | NON_INDEPENDENT | RECLASSIFY_AS_METHOD_LIMIT` — 需要一个"层级不匹配 / 抽样框错位"的独立类目；否则 `N~ | 报告把 9 个条目判为 `NOT_IDENTIFIABLE`（S2 HISD、D3 WTC-Trait、O3 3VDI、O4 Interpersonal Dependency、O5 Personal Sense of Power、T8 泛信任族、X14 Romantic Beliefs、X15 Reiss RPS、X8 ANS），但报告自己对这些条目的说明是"是 Agent 层 trait / 抽样框错 / 已在别处有替代"，属层级不匹配或检索不足，不是结构上不可测。 |
| `B-C5` | `VERIFIED` | VERIFIED | NO | NON_INDEPENDENT | ACCEPT_AS_PROPOSAL` — 目录的**内容**大体可用；只是计数口径需在 durable 版本里改成"去~ | 41/54 这套计数至少含 6 处重复或近同义 double-count，报告未标注。 |
| `B-C6` | `CONTESTED` | CONTESTED | NO | NON_INDEPENDENT | REJECT`（拒绝把这三行按原样并入任何 durable 引用表） | 被审报告有 3 处引用在 Crossref 上**解析到的不是它声称的作品**：`O1` RPI、`O2` RBA、`A13` 依恋日记。 |
| `B-C7` | `CONTESTED` | CONTESTED | NO | VERIFIED_BY_ME | REJECT`（"10 题"这一格必须改成 75；若要引用请同时写明 diversity 是 38 项 checklis~ | RCI 行报告 "self-report，**10 题**"，并推出 "**Frequency 与 Diversity 是弱信度分量**"。 |
| `B-C8` | `MIXED:VERIFIED+VERIFIED` | (a) `VERIFIED`；(b) `VERIFIED`；(c) `WRONG-SCOPE | NO | VERIFIED_BY_ME | RECLASSIFY_AS_METHOD_LIMIT` — (a)(b) 接受；(c) 降级为"实验室唤起通道的性别不对~ | (a) IOS = 单题图示 1–7、2 因子 "Feeling Close / Behaving Close"、minimal 社会赞许相关、5 项陌生人 dyad 附加研究；(b) Chivers et al. 2010 男 r=.66 / 女 r=.26、调节为 stimulus variability + 自评时点；(c) 由此推出 "`SexualDesire_(i->j)` 在女性方向上只有一条弱通道"。 |
| `B-C9` | `VERIFIED` | VERIFIED | NO | VERIFIED_BY_ME | ACCEPT | ECR-R = 36 题 2 维；IRT 分析 N=1,085；官方评分 1–18 anxiety（items 9/11 反向）、19–36 avoidance（12 题反向）；官方页明示可改写指向其他关系类型；官方指引即 trait 语言。 |
| `B-C10` | `CONTESTED` | CONTESTED | NO | VERIFIED_BY_ME | ACCEPT_AS_PROPOSAL` — 方向性论证接受，但必须先补 ECR-RS 并重算改写成本。 | 报告正确指出 ECR-R 定向化是 rewriting 决策且会牵动 IRT 标定，但只说"必须作为独立决策审计（交 R05）"，**没有核算代价**，也没有把已存在的官方 relation-target 工具纳入讨论。 |
| `B-C11` | `WRONG-SCOPE` | WRONG-SCOPE | NO` — 但**必须停在 proposal**。若 `G9` 要被写进任何 c~ | NON_INDEPENDENT`（⚠️ 提醒 parent：lane~ | RECLASSIFY_AS_METHOD_LIMIT` — `G9` 需先重述为"关系层有向坐标的 pair-level~ | 报告称 "没有任何已验证坐标同时拥有自陈信念通道与行为/生理独立通道"，并据此称 `G9` 为**架构级 gap**。 |
| `B-C12` | `VERIFIED` | VERIFIED | NO | VERIFIED_BY_ME | ACCEPT_AS_PROPOSAL` — durable 版本必须补齐这三项，否则方向性与双通道两条主结论都缺反例检验~ | 报告的 41 族目录遗漏了至少 3 个可直接回应其自身核心论点的已验证工具。 |
| `B-C13` | `PLAUSIBLE` | PLAUSIBLE | NO | NON_INDEPENDENT | HOLD_FOR_EVIDENCE` — 五个具体数字未核前，不得作为 D8 降级的承重依据。 | 报告称关系权力测量谱系"38 个有名有姓的量表各自仅被用 1–2 次，无一成为主流工具"，并判为"本 packet 对 `OutcomeDependence` 最重的一份证据：整个工具族不可比"。 |
| `B-C14` | `VERIFIED` | VERIFIED`（对"存在降级不合格"这一事实的判定） | NO | NON_INDEPENDENT | HOLD_FOR_EVIDENCE` — 全部降级为 `NOT_ASSESSED`，或补齐一手来源后再恢复裁决。 | 12 个条目的来源被标 `UNVERIFIED_DOI` / `UNVERIFIED` / `AGENT_RECALL`，但仍各自携带一个 `DIRECT_PROXY` / `NOISY_PROXY` / `NOT_IDENTIFIABLE` 裁决。 |
| `B-C15` | `UNSUPPORTED` | UNSUPPORTED | NO | NON_INDEPENDENT | RECLASSIFY_AS_METHOD_LIMIT | §8 L405 自称 54 个条目"**全部带真实指针（DOI、官方记录或可访问原文页）**"。至少 5 条没有。 |
| `B-C16` | `CONTESTED` | CONTESTED | NO | VERIFIED_BY_ME | ACCEPT_AS_PROPOSAL` — 保留证据，修正 confound 类别；并把 `C4` 的两个指针补上。 | RMBM = 26 题 / 7 因子；两个前代 RMSM 有 "fundamental measurement flaws" 且在正确 item construction 下均不可用；因子结构在 3 样本间稳定。报告把该证据归入 §3.3 的 "**求值者/施测者效应**" confound 行。 |
| `B-C17` | `VERIFIED` | VERIFIED | NO | VERIFIED_BY_ME | ACCEPT` — 这是本报告最扎实的单条，且它对 `CURRENT_ARCHITECTURE.md` §2 "神经/遗~ | 关系结局总体 `ES=.09`（边缘显著）、`I²=76.0%`；交感 `ES=+.19 (p=.02)`、副交感 `ES=−.21 (p=.03)`、合并 `ES=+.16`；结构上不可分解为 i→j / j→i；不能作任何 LHRM 构念的 proxy。 |
| `B-C18` | `VERIFIED` | VERIFIED | NO | VERIFIED_BY_ME | ACCEPT`（附一条：`§4.3 → R16` 把 PRI-8 列入"最小可用测量面板"，须同时标 `NOT_OPEN~ | PRI item pool = 19 量表 246 题、`N=2,334`；PRI-8 R `α=.93 ω_WP=.83`、I `α=.88 ω_WP=.77`；Study 3 APIM 161 对伴侣把 i 的知觉与 j 的自报行为对起来；`DIRECT_PROXY`。 |
| `B-C19` | `VERIFIED` | VERIFIED | NO | VERIFIED_BY_ME | ACCEPT | DAS 信度泛化 meta = 91 篇研究 / 128 样本 / 25,035 人；total 与 Cohesion/Consensus/Satisfaction 内部一致性可接受但低于 Spanier 原报告；Affective Expression 分量 α 差；reliability 不因 sexual orientation / gender / marital status / ethnicity 而异。 |
| `B-C20` | `CONTESTED` | CONTESTED | NO | NON_INDEPENDENT | RECLASSIFY_AS_METHOD_LIMIT` — `AGENTS.md` 那条保留（但表述改为"工具的 ina~ | "工具层面对'关系不存在'这一状态的处理方式是造一个替代对象 — 在 LHRM 框架里等于把 `Unknown` 静默 coerce 成一个值，**违反 `CURRENT_ARCHITECTURE.md` §9** 与 `AGENTS.md` 的 Unknown 保留原则"；并据此建议这些工具不能用于 Case Bank 中的陌生人/敌对/未确立关系材料。 |
| `B-C21` | `CONTESTED` | CONTESTED`（逐行不一致，见下） | UNSURE` — D7/D8 两条若要落地，**必须停在 proposal**~ | NON_INDEPENDENT | ACCEPT_AS_PROPOSAL | 报告对 `PARAMETER_CONVERGENCE_V0_1.md` D1–D8 / B1 / P1 / R3 逐项给出的 `KEEP` / `降级` 裁决。 |
| `B-C22` | `CONTESTED` | CONTESTED | NO | NON_INDEPENDENT | RECLASSIFY_AS_METHOD_LIMIT | 报告对 trust 类给了 3 个 `DIRECT_PROXY`（`T1` Rempel TS、`T2` 2025 重做、`T3` DTS），但同一报告承认 `T1` 的 1985 因子结构从未与竞争的 4 因子模型对拆、2025 重做发现一个反向措辞方法因子、`T3` 五年后被独立复核判定测的是 benevolence 而非 trust—这些证据强度足以把 ECR-R 判成 `NOISY_PROXY`，却不足以把 TS/DTS 判成 `DIRECT_PROXY`。 |
| `B-C23` | `PLAUSIBLE` | PLAUSIBLE | NO | NON_INDEPENDENT | HOLD_FOR_EVIDENCE | Larzelere & Huston (1980)：Female 对 partner 的 love `r=.23 (p<.05)`；Male 的 `r=−.06 (n.s.)`；作者解释为信任在依赖度低的一方更关键；因此 Trust 坐标在测量层与 OutcomeDependence 纠缠。§4.3 把这当作交给 R05 的量化警示。 |
| `B-C24` | `PLAUSIBLE` | PLAUSIBLE | NO | NON_INDEPENDENT | ACCEPT_AS_PROPOSAL` — 保留为结构性观察，但把"零证据"改为"本 packet 未检出不变性检验报告~ | "关系科学里'跨文化不变'的证据高度集中在两个构念族（依恋、性欲），而 LHRM 最缺的三个（Dedication、OutcomeDependence、Cohesion）恰好是零证据。" |

## 2.C — lane `C`（datasets / access / rights）

| claim_id | primary | verdict（原文） | canon | corroboration | recommendation | claim（截断） |
|---|---|---|---|---|---|---|
| `C-C1` | `VERIFIED` | VERIFIED | NO |  | ACCEPT | SHARE 使用条款 §7 明文禁止「非完全自管」应用处理 SHARE 数据、禁止用于训练 AI 模型（本地纯科学用途除外），并规定 AI/ML 产生的派生物受与原数据相同的限制。 |
| `C-C2` | `WRONG-SCOPE` | WRONG-SCOPE | NO**（在 §5 内部改写即可） |  | RECLASSIFY_AS_METHOD_LIMIT** — D02 `lhrm_impact` 改写为「§7 是限制~ | 报告 D02 `lhrm_impact` 断言「§7 使 SHARE 派生量在法务上不能进入一个 LLM 参与的公开验证流水线」，并在 §5.2 结论 3 推广为「把问卷数据限制在方法学标定侧（且仅在本地合规环境内）」。 |
| `C-C3` | `PLAUSIBLE` | PLAUSIBLE**（方向对，范围描述不准） | NO |  | ACCEPT_AS_PROPOSAL** — D02 §11 一行补上 "(cf. 6. above)" 限定，标为 ~ | 报告称「§11 违反后果：立即撤销使用权、要求删除全部副本；**严重违反**可在网上公开违规者身份」。 |
| `C-C4` | `CONTESTED` | CONTESTED | NO |  | RECLASSIFY_AS_METHOD_LIMIT** — 「矛盾 1」从"官方内部不一致"降级为"Week 9 已~ | 报告称 SHARE「≥8 完整常规 wave（2004–）+ 2 轮 COVID；第 9/10 wave 官方页面表述冲突 → UNKNOWN_AS_OF」。 |
| `C-C5` | `VERIFIED` | VERIFIED**（漏记） | NO |  | RECLASSIFY_AS_METHOD_LIMIT** — D02 `kin_coverage` 单元格与 `can~ | 报告在 D02 把 `CH`/`SP` 列为 SHARE 的 `kin_coverage` 资产，未记录官方对 CH 模块顺序/linkage 不可靠的明文警告。 |
| `C-C6` | `VERIFIED` | VERIFIED**（漏记） | NO |  | RECLASSIFY_AS_METHOD_LIMIT** — D02 的"双方各自作答 = 是"应加限定：「自报为默认~ | 报告 D02 `directionality` 判为 "SUPPORTED 但**模块级不对称**"，只标注 `fin_resp`/`fam_resp`/`hou_resp` 的单方报告；未标注 SHARE 存在 partly/fully **proxy interview**，即一方可代另一方作答。 |
| `C-C7` | `VERIFIED` | VERIFIED | NO |  | ACCEPT**（并建议把这一条作为 rights-first 筛选的**样板条款**） | Add Health 明文禁止用 LLM/AI 工具管理、处理或分析其数据，公版与 restricted 同等适用；LLM Type 1/2/3 的 Data Use 均为 None。 |
| `C-C8` | `VERIFIED` | VERIFIED | NO |  | ACCEPT**，并把 G2 的时间窗从 "2025–2026" 改为 "2024-12 起（ICPSR）→ 2025–~ | ICPSR LLM 政策为 Type 1 = None；Type 2 = Public-Use（须许可）；Type 3 = Public + Restricted（须许可）。 |
| `C-C9` | `VERIFIED` | VERIFIED | NO |  | ACCEPT_AS_PROPOSAL** — §5.1 HARP/ICPSR 行补 "个人存放 study：仅会员可再~ | ICPSR Redistribution Policy 要求任何再分发先经 Data Stewardship Policy Committee 批准；依据 Bylaws Art. 1.2.B；个人研究者存放的 study 仅对会员开放再分发。 |
| `C-C10` | `VERIFIED` | VERIFIED**（但**非我直接打开含该条款的页面**） | NO |  | ACCEPT**（条款），并追加 access-continuity 备注（见 C-C15）。 | CESR 明文禁止用 LLM/其他 AI 工具管理、处理或分析其分发的任何数据；构成对所有现行 DUA 的违反。 |
| `C-C11` | `CONTESTED` | CONTESTED** — 谨慎正确，但"不可得"前提**已被推翻 | NO**（但 C-C14 会触及 §6 与 §5.2） |  | RECLASSIFY_AS_METHOD_LIMIT** — U4 由 `UNKNOWN_AS_OF` 改为 `RES~ | 报告称 HRS CoU（2026-02-04）的 AI/LLM 政策「条文未取得 → `UNKNOWN_AS_OF`（U4）。**不得猜测条文内容**」，并在 §10 自评「HRS AI/LLM 政策条文未取得，而这**可能是最严的一份**」。 |
| `C-C12` | `PLAUSIBLE` | PLAUSIBLE**（实质成立，引文两处不准） | UNSURE** — 若 Architect 采纳 §5.2 结论 2 去改 ~ |  | HOLD_FOR_EVIDENCE** — 先补回 "generally" 与 CoC 覆盖 HRS data（不限 ~ | 报告 D10 逐字引 "investigators and others who have access to HRS restricted data are **prohibited** from disclosing identifiable, sensitive information... This protection applies even under court order or subpoena"，并归给 "RDA PDF 原文"。 |
| `C-C13` | `CONTESTED` | CONTESTED**（对报告的覆盖完整性） | NO**（若采纳 C-C36 的重述则改 §5.1 / §1.2 / §10） |  | ACCEPT_AS_PROPOSAL** — §5.1 补 SOEP 行（Type 1/2/3 全 None；派生分析~ | 报告 D11 审计了 SOEP，但 §5.1 权利汇总表**没有 SOEP 行**，G2 的「2025–2026 收紧」也未列 SOEP；报告未发现 DIW Berlin 已发布专门的 SOEP AI and LLM Use Policy。 |
| `C-C14` | `WRONG-SCOPE` | WRONG-SCOPE | NO**（若 §5.2/§6 的建议被写进任何方法学文档则必须改） |  | RECLASSIFY_AS_METHOD_LIMIT** — 把「唯一已知可行路径」拆成三句独立、各带条件与出处的陈述~ | 报告 §6 末行与 §10 断言「ICPSR SOMAR VDE / MiCDA Enclave — ICPSR 可在 VDE 内放自托管模型（Llama-3.2-3B-Instruct、gemma-3-4b-it 等）……**这是目前唯一已知可行的『合规地用 LLM 处理受限数据』路径**」。 |
| `C-C15` | `VERIFIED` | VERIFIED**（报告漏记） | NO |  | ACCEPT_AS_PROPOSAL** — D10 加一行 access-continuity 注记（含 2025-~ | 报告未记录 HRS 数据仓库自身的**可及性连续性风险**。 |
| `C-C16` | `WRONG-SCOPE` | WRONG-SCOPE | NO |  | RECLASSIFY_AS_METHOD_LIMIT** — 全文把"完全公开"统一改为「**技术上零门槛可下载（第三~ | 报告称「完全公开无门槛（可立即下载）：1（speed dating 公开镜像）」、「**完全公开**的那一个（speed dating）」、表内「**完全公开**：github.com/datasets/speed-dating」。 |
| `C-C17` | `MIXED:VERIFIED+PLAUSIBLE` | VERIFIED**（可用性与方向性设计结构）／**PLAUSIBLE**（变量名与 21 场） | NO |  | ACCEPT | 报告称镜像 2026-09-27 仍在线，并称该数据是"唯一能证明 Z[i→j] 与 Z[j→i] 确实是两个不同自由度"的数据集，含 6 项双向评分、`wave` = 21 场 session 而非同一 dyad 重复观测。 |
| `C-C18` | `PLAUSIBLE` | PLAUSIBLE | UNSURE** — 若 §5.2 的 `llm_use_condition`~ |  | HOLD_FOR_EVIDENCE** — 在拿到可读原文前，pairfam 的一切 rights 断言标 `PLAU~ | pairfam 条款 §3 只允许汇总呈现，即使无直接个人指向也不得发布个体级记录（报告逐字引德文）；§1 禁再识别、§4 禁商用、§5 禁第三方转发、§7 出版后 4 周内交 FDZ；2025-01 起取消旧的内部转发通道。 |
| `C-C19` | `CONTESTED` | CONTESTED**（事实误标 + 报告内部矛盾） | NO |  | RECLASSIFY_AS_METHOD_LIMIT** — D12 标题改为「Add Health (Nationa~ | 报告把 D12 命名为「**Add Health (NLSY97/ECLS)**」。 |
| `C-C20` | `CONTESTED` | CONTESTED | NO |  | RECLASSIFY_AS_METHOD_LIMIT** — (a) U7 由「不得主张存在」改为「官方用户指南已列 ~ | 报告 D12 写「**本 lane 未核实其文件存在性（U7）。不得主张该数据存在**」，§7 非主张 6 写「**不主张** Add Health 存在 friendship nomination 数据文件（U7）」；并在 D15 断言 Oregon Couples Study 是「本 lane 中**除 HARP 外唯一**明确『双报告恋爱 dyad』的美国数据集」。 |
| `C-C21` | `CONTESTED` | CONTESTED | NO |  | RECLASSIFY_AS_METHOD_LIMIT** — 「统一 `p` 前缀」改为「partner 侧主用 `p~ | 报告 D01 写「官方 GESIS 变量清单中 partner 侧变量统一 `p` 前缀（psex_gen, page, preldur, pmarstat, pincoecd, ...）」。 |
| `C-C22` | `PLAUSIBLE` | PLAUSIBLE**（版本过时风险；无法在本环境定论） | NO |  | HOLD_FOR_EVIDENCE** — 在 pairfam 波数被用作任何结论承重属性之前，先确认 2026-09~ | 报告 D01 写「`current_version_observed`: Release 14.2（14 survey waves, doi 10.4232/pairfam.5678.14.2.0）」，§3 表写「DOI 版本化（当前 14.2.0）」。 |
| `C-C23` | `PLAUSIBLE` | PLAUSIBLE**（未知登记**正确且必要**） | NO |  | ACCEPT**（把 U5 保持 `UNKNOWN` 是正确判断）；建议后续 lane 改用 `hrsdata.isr.~ | 报告标 HRS「稳定 couple id = **未核实**（HRS 正文页本环境不可达）」，§9 U5 记 `UNKNOWN`。 |
| `C-C24` | `CONTESTED` | CONTESTED | UNSURE** — 若 Architect 要把 CLOC 写进任何数据依赖~ |  | HOLD_FOR_EVIDENCE** — 分类结论我倾向保留 `MEASUREMENT_ONLY`，但**理由必须改~ | 报告把 CLOC 分类为 `MEASUREMENT_ONLY`；同时逐字记录了一个"双方同 record、四波、含妻 `V*` + 夫 `S*`"的设计，并称其为「本 lane 找到的**最早、最干净的双人同 record 四波设计**」。 |
| `C-C25` | `CONTESTED` | CONTESTED**（内部不一致） | NO |  | RECLASSIFY_AS_METHOD_LIMIT** — 二选一：(a) 承认分界为「重建是否有官方依据」并写成显~ | 报告把 SOEP 判为 `NOT_DYADIC_ENOUGH`（"发货形态没有可用 partner id，dyad 需分析者启发式重建"），把 IFLS 判为 `MEASUREMENT_ONLY`（"稳定 couple id = **未核实**；识别 spouse 是官方指引的构造过程"）。 |
| `C-C26` | `WRONG-SCOPE` | WRONG-SCOPE | NO |  | RECLASSIFY_AS_METHOD_LIMIT** — D12/D13 的 `cannot_identify` ~ | D12 `cannot_identify` 写「对 LHRM 计划用途 — **不可识别**」；D13 写「对 LHRM 计划用途 — **不可识别**（AI 政策）」。 |
| `C-C27` | `WRONG-SCOPE` | WRONG-SCOPE | NO |  | RECLASSIFY_AS_METHOD_LIMIT** — D15 同时标注两轴：结构轴 = `MEASUREMEN~ | D15 Oregon Youth Study Couples Study Time 6 判 `ACCESS_BLOCKED`，`cannot_identify` 写「获取（LHRM 无 ICPSR RDUA + IRB 的现实路径）」。 |
| `C-C28` | `CONTESTED` | CONTESTED | NO**（若 Architect 把"数据源清单"写进任何 canonical ~ |  | RECLASSIFY_AS_METHOD_LIMIT** — 改为**两级标签**：`CALIBRATION_READ~ | 报告把 pairfam / SHARE / HARP 判为 `CALIBRATION_READY`，§1.2 表述为「在方向化 + 纵向 + **双方各自作答**这三个条件同时成立的数据集里，本审计只找到 3 个」。 |
| `C-C29` | `CONTESTED` | CONTESTED | NO**（若被写进任何对外材料则必须先改） |  | RECLASSIFY_AS_METHOD_LIMIT** — 头条结论改写为：「在被**结构检验过**的 15 个数据~ | §8.9「最重要的整体否定结果」：「本审计**未发现**任何『**完全公开 + 双报告 + 方向性 + 多波 + 关系状态构念**』的数据集。**这四个条件的交集为空。** 这是本 landscape 最重要的结构性事实，比任何单个数据集的优劣都重要。」 |
| `C-C30` | `WRONG-SCOPE` | WRONG-SCOPE | NO |  | RECLASSIFY_AS_METHOD_LIMIT** — §8.8 改为「在本 16 个数据集的审计范围内未发现；~ | §8.8「『intensive longitudinal 关系日记数据』在本 landscape 中**不存在**公开可得的。」 |
| `C-C31` | `CONTESTED` | CONTESTED**（对报告的自我降级范围） | NO |  | RECLASSIFY_AS_METHOD_LIMIT** — §8.6 与 §11 注改为「ICPSR **`/web~ | §8.6「**ICPSR 全站 403**」→「本报告中**所有 ICPSR 系证据**强度为 MEDIUM」；§11 注「本 lane 对 icpsr.umich.edu 直接抓取一律 403」。 |
| `C-C32` | `CONTESTED` | CONTESTED**（失败记录真实；其后果被高估） | NO |  | RECLASSIFY_AS_METHOD_LIMIT** — §8.6 补记 `hrsdata.isr.umich.e~ | §8.6「`hrs.isr.umich.edu` **正文页**反复 timeout/403」；U4 记「HRS CoU（2026-02-04）AI/LLM 政策**具体条文** = 存在性已核实，正文 `UNKNOWN_AS_OF`」。 |
| `C-C33` | `VERIFIED` | VERIFIED**（作为方法论行为） | NO |  | ACCEPT** — 建议把这一处理方式作为全 swarm 的正面样板：`FETCH_FAILED`（我抓不到）/ `~ | 报告把 Family Life Survey / LSAF / New Study of Marriage 三者的任何属性记为 `FETCH_FAILED` / 不可主张，并自评这是「本 lane 最实质的覆盖缺口。如实记录，不用记忆填充」。 |
| `C-C34` | `PLAUSIBLE` | PLAUSIBLE**（整体自洽，三处越界） | NO |  | ACCEPT_AS_PROPOSAL** — 要求 R04 二次修订时给全部 `CITED_PRIMARY (inde~ | 报告 §7 非主张 1「**不主张**本报告涉及的任何数据集已被 LHRM 下载、打开、分析或映射。本 lane **零数据接触**」；§4 各卡片以 `CITED_PRIMARY` 标记所有属性判断。 |
| `C-C35` | `CONTESTED` | CONTESTED | NO |  | HOLD_FOR_EVIDENCE** — 把 D08 的方向性判定限定为「**Wave 1 单方报告（已核实）；Wa~ | D08 `directionality_critical_note` 断言「**配偶关系质量是单方报告**……→ **Z[i→j] 与 Z[j→i] 在 NSFH 中不可分离**」，依据是 Wave 1 的一句问卷描述。 |
| `C-C36` | `CONTESTED` | CONTESTED**（结论成立，表述需重述） | NO |  | RECLASSIFY_AS_METHOD_LIMIT** — G2 改写为：「LLM/AI use-condition~ | §1.2「Add Health、UAS、SHARE、ICPSR 已在 2025–2026 明确限制或禁止用 LLM/AI 处理个体级数据」；§10「发现了 **2025–2026 年 LLM/AI use-condition 收紧** 这一横跨 SHARE / ICPSR / Add Health / UAS / HRS 的系统性约束」。 |

## 2.D — lane `D`（statistics / identification / transition laws）

| claim_id | primary | verdict（原文） | canon | corroboration | recommendation | claim（截断） |
|---|---|---|---|---|---|---|
| `D-#1` | `WRONG-SCOPE` | WRONG-SCOPE | YES` — 改 `docs/foundation/CURRENT_ARCHIT~ |  | RECLASSIFY_AS_METHOD_LIMIT` — 把 §5 拆成 `I-STRUCTURAL` / `I-DE~ | 「换方法不能越过这一节」（`05:353`）：17 条是结构上不可能回答的问题，换方法也解决不了。 |
| `D-#2` | `WRONG-SCOPE` | WRONG-SCOPE | YES` — 但**必须停在 proposal，且本条应被驳回**。`CURRE~ |  | REJECT | 「这四条不是『暂时做不到』，是『换方法也做不到』」，应纳入 `CURRENT_ARCHITECTURE.md` 的显式非目标（`05:606`）。 |
| `D-#3` | `CONTESTED` | CONTESTED | NO |  | RECLASSIFY_AS_METHOD_LIMIT` — I8 应改写为「未测不变性时**强均值比较**未定义；ali~ | 任何动态结论前必须先做 invariance 层级序列，否则结论**未定义**（`05:364`）。 |
| `D-#4` | `WRONG-SCOPE` | WRONG-SCOPE | NO |  | RECLASSIFY_AS_METHOD_LIMIT | 同一 `psi(t)` 序列在不同 lag / 分辨率下给出不同 AR 系数；`+1` 不是自然量。 |
| `D-#5` | `CONTESTED` | CONTESTED | NO |  | RECLASSIFY_AS_METHOD_LIMIT` — 改写为「在**无外生约束变异**的设计中 constrain~ | Constraint 本身是「未发生的事件」，无反事实对照就无 estimand；统计上是 structural zero / undefined，不是 `0`。 |
| `D-#6` | `CONTESTED` | CONTESTED | NO |  | RECLASSIFY_AS_METHOD_LIMIT` — 统一为「二人 dyad 违反 no-interference~ | 05 I5：二人关系中「不得」给「A 导致了 B 的关系破裂」这类单向归因（`05:361`）。 |
| `D-#7` | `VERIFIED` | VERIFIED | NO |  | ACCEPT_AS_PROPOSAL` — 保留为方法限制，但**不得**作为 canonical 变更请求提出（已存在~ | 「从单个案例估计现实概率」在结构上无 estimand。 |
| `D-#8` | `VERIFIED` | VERIFIED | NO |  | ACCEPT_AS_PROPOSAL` — 保留一处即可，canonical 只写「F 的表述规范」一句。 | 不同 DAG / `F` 形式可给相同拟合；不得把最好拟合的 `F` 当机制。 |
| `D-#9` | `WRONG-SCOPE` | WRONG-SCOPE | NO |  | RECLASSIFY_AS_METHOD_LIMIT` — 归入 `I-LIT-OPEN` 类。 | TSE 会 improper solution；LST-AR 适用面窄；TSO 仍有 occasion factor stability 问题；不得把 Q2 当有唯一答案的分类问题。 |
| `D-#10` | `WRONG-SCOPE` | WRONG-SCOPE | NO`（若 `D-C1` 采纳则连带） |  | RECLASSIFY_AS_METHOD_LIMIT | §5 被呈现为一等交付物、单一逻辑类型。 |
| `D-#11` | `VERIFIED` | VERIFIED | NO |  | ACCEPT` — 判据与风险陈述准确；建议 `05` §7 补入上述反向批评。 | illusory between-person component 可能**只**来自省略的 time-varying covariate；不得把 `RIx` 的方差直接写成「稳定 trait」。 |
| `D-#12` | `VERIFIED` | VERIFIED | NO |  | ACCEPT | 分析单位是 **dyad**；200 人 × 2 方向 = 400 个数不等于 n=400。 |
| `D-#13` | `WRONG-SCOPE` | WRONG-SCOPE | NO |  | RECLASSIFY_AS_METHOD_LIMIT` — M11 整行降为 `○`；M6×Q8 / M7×Q7 降为 ~ | M11（multiverse / specification curve / power / 不确定性传播）在 Q1–Q10 十题上全是「主要落点」。 |
| `D-#14` | `VERIFIED` | VERIFIED | NO |  | ACCEPT` — 引文质量是 `05` 的强项，应保留；同时作为 `D-C3` 的内部矛盾证据。 | 测量不变性之争「有效性本位」阵营的引文。 |
| `D-#15` | `PLAUSIBLE` | PLAUSIBLE | NO |  | HOLD_FOR_EVIDENCE | ctsem` v3.11.1（2026-07-13）提供 SDE / 差分方程 + ML/EM 或 Stan HMC，可处理不等间隔观测。 |
| `D-#16` | `PLAUSIBLE` | PLAUSIBLE | NO |  | HOLD_FOR_EVIDENCE` — 判据**可失败**（无一完全不可失败），但需 (a) 为 判 C/F/G/L/~ | 五个律族各有「在看到数据之前固定」的明确证伪判据（`06` §4.8 / §5.8 / §6.8 / §7.8 / §8.8，判 A–判 O 共 15 条）。 |
| `D-#17` | `WRONG-SCOPE` | WRONG-SCOPE | NO |  | RECLASSIFY_AS_METHOD_LIMIT` — 两行改标 `MODEL_HYPOTHESIS`，理由写明「来~ | 「存在一条独立的正向（趋近）分支」与「存在一条独立的抑制/修复分支」均标 **SUPPORTED**。 |
| `D-#18` | `CONTESTED` | CONTESTED`（处理**基本诚实，但把一个未被检验的东西写成了被检验过**） | NO |  | ACCEPT_AS_PROPOSAL` — **判定：处理基本诚实，不应撤除该律，但必须重写措辞。** 三条：(a) *~ | 06:448-450`「评价读出的『下降』由两个**可分离**机制产生：起点选择（level）与段内实际化（slope）」；同页「**本律是本次五个律族中最可能先被拒绝的一个**」。 |
| `D-#19` | `WRONG-SCOPE` | WRONG-SCOPE`（且为**双重计数中的矛盾型**，见 `D-C29`） | NO |  | REJECT` — (a) 把 `B2` 重定义为与 `06 §6.3` 一致（`Level(τ₀) + 随机游走 + ~ | 16:203`「`B2` = `SELECTION_ONLY`（稳定 per-dyad 截距，**无增量**）… **本协议认为最重要的一条 null，因为它已经击败过一个候选**」。 |
| `D-#20` | `PLAUSIBLE` | PLAUSIBLE | NO |  | HOLD_FOR_EVIDENCE` — 先按逻辑类型重命名（`NULL_*` / `RIVAL_*` / `PROC_~ | 16` §7 的 8 项构成「候选方程必须配对击败」的 null 集。 |
| `D-#21` | `UNSUPPORTED` | UNSUPPORTED`（作为「封闭互斥受控表」这一断言） | NO`（`16` 是 candidate；若 Architect 接受，`#29~ |  | REJECT` — 现状不可作为受控表采纳。修正版：拆出独立 `reliability_class`；`CONFLICT~ | mapping_status ∈ {DIRECT_ITEM, DERIVED_COMPOSITE, BEHAVIORAL_PROXY, COVARIATE_ONLY, NOT_MAPPED, CONFLICTED}` 是封闭受控表。 |
| `D-#22` | `UNSUPPORTED` | UNSUPPORTED`（作为「封闭受控表」） | NO |  | REJECT` — 先修 `invariance_level_tested` 的枚举再采纳；把 `missingness~ | uncertainty` 五字段受控表：`estimated_uncertainty` / `measurement_error_known` / `floor_ceiling_risk` / `missingness_mechanism` / `invariance_level_tested`。 |
| `D-#23` | `UNSUPPORTED` | UNSUPPORTED`（作为「可操作、互斥、覆盖」的受控表） | NO |  | REJECT` — 补入 `SELF_REPORTED_EDGE`（或 `BELIEF_ABOUT_EDGE`）；为 `~ | directionality_class ∈ {DIRECTED_EDGE, TARGET_LEVEL, AGENT_LEVEL, PAIR_LEVEL, UNDETERMINED, NON_SEPARABLE}`。 |
| `D-#24` | `UNSUPPORTED` | UNSUPPORTED`（作为「满足 §6.1 理由的默认几何」） | NO |  | REJECT` — 必须新增 `G0_WHOLE_DYAD_OUT`（整 dyad + 全部 wave 留出，estim~ | 「⇒ 默认几何 = dyad 分组 × 时间前向，二维同时施加」；`G1_BLOCKED_FORWARD` 为「**首选默认**」。 |
| `D-#25` | `UNSUPPORTED` | UNSUPPORTED`（作为「能防止 L7 触发」的机制） | NO |  | REJECT` — 修法：把 `TBD_AT_FZ1` 从字段 12 移除；改为**两级冻结**且明确规定 FZ-1 必~ | 16:408`「在**任何 holdout 行被读取之前**… 下列 16 字段必须被写入一份不可变的 `FREEZE_RECORD`… `FREEZE_RECORD` 一旦生成，holdout 才解锁」。 |
| `D-#26` | `PLAUSIBLE` | PLAUSIBLE | NO |  | HOLD_FOR_EVIDENCE` — 要求补一条 `L7-A` 实施条款：holdout 的凭据持有者、访问日志的审~ | L7`（a）holdout 只能被查看一次；（b）偏离记入 deviation log 并标 `EXPLORATORY`；（c）若需自适应，改用带隐私预算的可复用 holdout，或改走 `B6`。 |
| `D-#27` | `MIXED:PLAUSIBLE+UNSUPPORTED` | PLAUSIBLE`（对量化面板部分）／`UNSUPPORTED`（对完整性） | NO |  | HOLD_FOR_EVIDENCE` — 补四条：`L9_PERSON_LEVEL_NONINDEPENDENCE`、`~ | 16:117`「L1–L8 是**本协议的实例化**」；`16:589`「8 条 leakage 规则每条带真实引用」。 |
| `D-#28` | `UNSUPPORTED` | UNSUPPORTED`（作为「该来源不可得」的断言） | NO |  | HOLD_FOR_EVIDENCE` — 要求补做一次 L1–L8 ↔ K&N 八分类的逐条映射，并把「编号为 8 是巧~ | 16:117`「L1–L8 是本协议的实例化，**不声称**复现 S01 的八分类（**S01 图 1 确切标签未取得**；对应关系标 `DESIGN_CHOICE`）」。 |
| `D-#29` | `UNSUPPORTED` | UNSUPPORTED`（作为独立交付物计数） | NO |  | RECLASSIFY_AS_METHOD_LIMIT` — `16` 应自我标注为 **join lane**（`16:~ | 16:589` 把「17 条不可建立事项」与「21 条失败模式」计入已达成的交付物。 |
| `D-#30` | `VERIFIED` | VERIFIED | NO |  | ACCEPT` — 建议把 `F-SELF19/20/21` 提升为 `16` 的**首要交付物**，并把 `F-SEL~ | 「前 18 条是『我们会不小心夸大』，后三条是『我们会认真地做对一件没有用的事』」（`16:478`）。 |
| `D-#31` | `CONTESTED` | CONTESTED | NO`（canonical 是对的；需改的是 `#29` 的 issue bod~ |  | ACCEPT_AS_PROPOSAL` — 要求 Architect 记录：`#29` D 层公式已过期，须与 `CUR~ | 16:11`「本协议是 `#29` C / D / F 三层的**操作化草案**。它**不改写** `#29` 的分层」。 |
| `D-#32` | `VERIFIED` | VERIFIED | UNSURE` — 若 Gate A 的归因推理确实按算子组合实现，则**需要*~ |  | ACCEPT_AS_PROPOSAL` — 这是本 lane 唯一一条「不是方法限制、而是关于 LHRM 自身形式化正确~ | 06:53-68`：RULE-⊥（MH1）把 `AGENTS.md:24`「Unknown/missing data must remain explicit」写成数学；已知形式风险（U4）`⊥` 规则使更新算子成为**偏算子**，偏算子在格上不一定满足结合律或可逆性，若 Gate A 的覆盖推理依赖算子组合则归因会出错。 |
| `D-#33` | `NOT_ENUM` |  | RECLASSIFY_AS_METHOD_LIMIT` — 该行改标 `SUPPORTED（现象存在）/ ILLUSTR… | 「`Ded` 可与 `Trust` / `AttachmentSecurity` 解耦 | **SUPPORTED** | S15：abusive relationship 中 commitment 仍高 → 高 dedication + 低 trust 可共存」。 |
| `D-#34` | `CONTESTED` | CONTESTED | UNSURE` — 若 Architect 认为该建议可成立，则需改 `PARA~ |  | HOLD_FOR_EVIDENCE` — 在 S31 原文与 S17 正文核实前，`Ideal` 不应进入 `PARAM~ | 06:995-997` 裁决请求 2：「裁决 RGM（律 D）是否要求 `Ideal` 成为动态 directed state。这是本 lane 提出的**唯一会改变 schema 层级**的建议（S31 + S17 提供支持…）」。 |
| `D-#35` | `VERIFIED` | VERIFIED | NO |  | ACCEPT` — 建议把 `16:392` 的「结构性」改为「**数据收集方式的限制**」，并保留 `06` 的「当前~ | 06 §10` 逐条点名八项「在现有可得数据下**无法被检验**」，并称「本节是本报告**最诚实**的部分」。 |
| `D-#36` | `VERIFIED` | VERIFIED`（须补两点限定） | UNSURE` — 建议在 `CURRENT_ARCHITECTURE.md` ~ |  | ACCEPT_AS_PROPOSAL | 「在指定 instrument I、采样协议 Π、`F` 形式假设 H 下，与数据 D 一致的 `F` 之一是 `F_1`。」被 `05:54` 称为「不是免责套话，是识别事实」。 |
| `D-#37` | `VERIFIED` | VERIFIED`（但应结案） | NO |  | ACCEPT_AS_PROPOSAL` — `05` 的 U5 应由 parent 在 join 阶段用 R04 的波数~ | 05:479`（U5）+ `05:608`（§12 建议 3）。 |
| `D-#38` | `PLAUSIBLE` | PLAUSIBLE | NO |  | HOLD_FOR_EVIDENCE` — 打开 Orth et al. 2021 与 Hussey & Hughes 全~ | 「45% 的文献用两波拟合 CLPM，此时 CLPM 饱和，无法谈 fit」；「按 modal practice 89% 尺度看似有效，全面评估后只剩 4%」。 |
| `D-#39` | `VERIFIED` | VERIFIED | NO |  | ACCEPT` — 「不给伪共识」的处理是 05 最强的方法学纪律，建议作为其它 lane 的模板；同时补入上述反向批评~ | CLPM vs RI-CLPM vs STARTS vs ARTS **未解决**；LHRM 立场「**不定论**。并行报告 + 明确 estimand 差异 + 不用 fit 选模型」。 |
| `D-#40` | `VERIFIED` | VERIFIED`（须补层级限定） | NO |  | ACCEPT` — 补一句「个体层面点不可识别；总体分布层面在已知测量模型下可识别」，并把 `R16-UC05` 的适用~ | 「即使完美模型，posterior 也不会坍缩到点」；任何 `Z` 必须**始终**表示为 estimate + uncertainty + evidence。 |

## 2.E — lane `E`（belief / partial observability / knowledge）

| claim_id | primary | verdict（原文） | canon | corroboration | recommendation | claim（截断） |
|---|---|---|---|---|---|---|
| `E-C1` | `VERIFIED` | VERIFIED | NO**（07 §9.1 #12 与 §13 自己把该项路由给 `A02` / ~ |  | ACCEPT** — 这是本 lane 最有价值的一条，应作为 `NEGATIVE_RESULT` 进入 join。 | 指派给 07 的第二条主张「missingness lowers certainty, not computability」在 `youling/lhrm` 仓库内**字面不存在**；项目实际持有的更弱区分性陈述是 `STAGE_SUMMARY_2026-09-07.md:162` 的 `Computable != Certain`。 |
| `E-C2` | `MIXED:UNSUPPORTED+VERIFIED` | UNSUPPORTED**（针对「唯一 1 处命中」这一**方法学陈述**）；同一段落的**实质结论**（durable 资料无形式化内容）**VERIFIED | NO |  | RECLASSIFY_AS_METHOD_LIMIT** — 实质结论接受，把「唯一 1 处命中」改写为「canonic~ | 对 `D:\coding\lhrm\**\*.md` 检索 `refine\|monoton\|⊑\|preorder\|lattice\|composabl\|propagat` **唯一 1 处命中**（DATING_APP 报告 B12 的「承担 lattice」），据此断言「LHRM 现有 durable 资料中没有任何 refinement/单调性/预序/数学格/Unknown 组合传播的形式化内容」。 |
| `E-C3` | `UNSUPPORTED` | UNSUPPORTED**（我找到直接反证，未找到 07 版本的任何支撑） | NO**（这是对报告的判定，不是对 canonical 的要求） |  | REJECT**（指 §2.3 的这一条，**不是**拒绝 §2.3 的双序结论）— 正确的形式化是：**信息/近似序上~ | 07 断言：在信息序 `⊑` 上 `N < B` 不成立，**`N` 与 `B` 不可比**；唯一单调方向是 `B → T`、`B → F`（知道了才收窄），`N → 任意`。并据此推出「状态侧必须至少有两个序」。 |
| `E-C4` | `VERIFIED` | VERIFIED | NO |  | ACCEPT** — 「双序」这一结论保留，但必须与 E-C3 一起修正后才能作为 `value_class` 的依据。 | Belnap 四值逻辑 `{T,F,B,N}` 上存在两个序（knowledge/information order 与 truth/logical order），该结构因此是 bilattice。 |
| `E-C5` | `VERIFIED` | VERIFIED**（充分性 + Belnap 归属） | UNSURE**（若采纳 `⊑`，需在 `CURRENT_ARCHITECTUR~ |  | ACCEPT_AS_PROPOSAL** — 定理层接受；落地层（`Info` 的定义、`RelMergeability~ | 定义 `s ⊑ s′ ⟺ s 可由 s′ 遗忘得到`（预序），refinement consistency 为 `T : Info → Info` 满足 `s ⊑ s′ ⟹ T(s) ⊑ T(s′)`；`T` 为 Scott-continuous（单调 + 保持定向上确界，定义域为 dcpo）是经典充分条件；Belnap 构造 K4 时明确采用了该条件。 |
| `E-C6` | `MIXED:VERIFIED+UNSUPPORTED` | VERIFIED**（可组合性 + 更紧的界）／**UNSUPPORTED**（「松的程度依赖一个未被声明的独立性假设」这一句） | NO |  | ACCEPT_AS_PROPOSAL**（成本结论）／要求 07 补引 imprecise-probability 文献~ | 用「凸分布幂集」monad 做 credal set 组合**不是 compositional**，因为该 monad 非交换；用 graded monad 修正后得到**更紧**的界。故朴素 credal 组合系统性过松。 |
| `E-C7` | `PLAUSIBLE` | PLAUSIBLE | NO |  | HOLD_FOR_EVIDENCE** — 在打开 Renz 2007 之前不进入排序；并要求 07 补一句「若只使用 ~ | RCC8/IA 中只用 base relations 时一致性判定可算；允许 `2^B` 全部幂集时 NP-hard；因此必须先声明 tractable subset（如 `ORD-Horn`）。 |
| `E-C8` | `PLAUSIBLE` | PLAUSIBLE | NO |  | HOLD_FOR_EVIDENCE** — §5.4 的替代文本应加限定语「对 `no_evidence` / `ref~ | Pelessoni & Vicig (2022) 证明概率不等式不依赖精确评估，故在 imprecise 知识（`22`-coherence）下仍成立；因此缺失后仍可算的是「有界量」而非「点值」。这是 07 自称「最重要的正面结果」。 |
| `E-C9` | `MIXED:VERIFIED+PLAUSIBLE` | VERIFIED**（定理 + 逐字引文）／**PLAUSIBLE**（迁移到 LHRM readout）／附带**两处书目错误 | UNSURE**（落点判定见下方专项 3 第 5 行） |  | ACCEPT_AS_PROPOSAL** — 定理接受；请 07 修正书目与术语，并把 FM-05 的 LHRM 后果从~ | Franc, Prusa & Voracek 证明 cost-based / bounded-improvement / bounded-coverage 三个 reject model **共享同一最优策略** = Bayes classifier + **randomized Bayes selection function**；选择函数不是可选附件。故成本敏感读出下 `REFUSE` 是一等输出。 |
| `E-C10` | `MIXED:VERIFIED+UNSUPPORTED` | VERIFIED**（引文）／附带 **`UNSUPPORTED` 的书目条目**（作者列表错误） | NO |  | REJECT**（针对 ref [6] 的书目条目，须修正后才能引用）／内容层 **ACCEPT**。这是 `A01_E~ | 在 fully-observable 域中，agent 的 epistemic uncertainty 使环境在 test-time **隐式部分可观测**；不显式处理它的方法在理论与实践中都可**任意次优**。 |
| `E-C11` | `PLAUSIBLE` | PLAUSIBLE**（集合整体）／分条见下 | UNSURE |  | REJECT**（对「9 条现在就能检查」这一计数）／**ACCEPT_AS_PROPOSAL**（对不变量集合本身）。~ | 给出 19 条候选可检验不变量，其中 9 条「现在就能检查」（I1、I2、I3、I4、I6、I7、I12、I14、I15）。 |
| `E-C12` | `VERIFIED` | VERIFIED**（缺陷确认） | NO |  | ACCEPT_AS_PROPOSAL**（要求 07 改 `:227` 为 19） | §5 开篇写「以下 **15 条**是候选可检验不变量」，但 §5.1 给出 I1–I15、§5.2 给出 I16–I9…即 I16–I19，合计 **19 条**。§13 也写「给出 19 条」。 |
| `E-C13` | `VERIFIED` | VERIFIED**（缺陷确认） | NO |  | REJECT**（对标签使用本身）／要求 07 二选一：把 `[ESTABLISHED]` 加进约定表并定义它与 `CI~ | 07 的证据等级约定（`:8`）只定义 `CITED_PRIMARY` / `CITED_METADATA` / `CITED_SECONDARY` / `AGENT_RECALL` / `MODEL_HYPOTHESIS` / `AI_RECOMMENDATION`，但正文 **15 处**使用 `[ESTABLISHED]`（`:292, 301, 317, 325, 331, 332, 338, 354, 372, 380, 382, 392, 394, 408, 422`），而 `AGE~ |
| `E-C14` | `PLAUSIBLE` | PLAUSIBLE**，且就其**叙事材料**适用范围应 **RECLASSIFY_AS_METHOD_LIMIT | UNSURE |  | RECLASSIFY_AS_METHOD_LIMIT** — 改写为「在**叙事/表达性压力测试**材料上，核心关系坐标~ | Trust(A→B)`、`Dedication(A→B)`、`SexualDesire(A→B)` 没有 gold standard；可能的锚点只有法院/官方裁定事实、强制性行为痕迹、已验证量表；**在叙事材料上三者皆无**。故这些坐标的后验在形式上必须是不可辨识的分布族，报告点值不是精度不足而是**指称缺失**。 |
| `E-C15` | `PLAUSIBLE` | PLAUSIBLE | UNSURE** — 若采纳，触及 `CURRENT_ARCHITECTURE.~ |  | ACCEPT_AS_PROPOSAL** — 接受为一条**实现约定 + readout 要求**；同时要求 07 补方~ | 若用**单一**人口超参数对 `Z[k,i,j,t]` 做向心收缩，`i→j` 与 `j→i` 共享同一收缩中心 → **非对称性被系统性压向对称**；`CURRENT_ARCHITECTURE.md:130-132` 要求三条 `X(A→B) != X(B→A)` 断言；故若采用 partial pooling，必须对两个方向使用分离的超参数或 `(1,−1)` contrast 建模，并把「收缩导致的非对称衰减量」作为 readout 显式报告。 |
| `E-C16` | `VERIFIED` | VERIFIED | UNSURE** — 07 把它标为「**人类/架构决定**，不是研究问题」（`~ |  | ACCEPT** — 这是本 lane 唯一的 head-of-list 阻塞项，且它**同时阻塞** 07 的 `⊑`~ | 项目内不存在「哪些构念原则上可被直接观察 / 哪些只能被报告 / 哪些只能被推断」的清单；`g = FIRSTHAND` 与 `structurally_unobservable` 因此都无法落地。这是落地 belief 层的头号阻塞。 |
| `E-C17` | `PLAUSIBLE` | PLAUSIBLE**（论证成立，但依赖的复杂度/等价性结果我 `NOT_OPENED`） | UNSURE** — 任何一项 REJECT 被 Architect 采纳都会写~ |  | ACCEPT_AS_PROPOSAL** — 三项 REJECT 的结论接受；要求 08b 把 §3.2(b) 与 §3~ | 三项 REJECT 的**论证**（非结论）是否成立。 |
| `E-C18` | `UNSUPPORTED` | UNSUPPORTED**（对「最小」这一强主张；设计本身可接受） | UNSURE**（落点判定见下方专项 3 第 3 行） |  | ACCEPT_AS_PROPOSAL** — 接受为 proposal；要求 08b (i) 把 `M` 明确标为「有意~ | 整条 `Reality → Observation → Belief → Evaluation` 链可用 **8 个逐记录带类型槽位 + 2 个逐 (持有者, 内容) 带类型标量 + 4 个派生类 + 1 个世界模式标签** 表达；「**没有第九个原语，没有 credence 字段，没有 modality 深度**」。 |
| `E-C19` | `VERIFIED` | VERIFIED**（论证成立 + 与 canonical 无冲突）／附带一条 canonical 缺口 | YES**（本 lane 三条 canonical 建议中**唯一**我判 YE~ |  | ACCEPT** — 论证成立、无冲突、是本 lane 唯一判 `YES` 的 canonical 建议；要求 08b ~ | 不披露（non-disclosure）不是一个信息缺失，而是一个**关于一个 `Behavior` 的断言**；`NonDisclosure` 需要第三个输入「`ι` 确实有东西没披露」，这只能来自 `Action/Event` 层的 `Disclosure` 记录，**不能是 belief 层的字段**。因此「部分披露的表示不在 belief 层，而在 action 层」。 |
| `E-C20` | `VERIFIED` | VERIFIED | NO**（这是对 canonical 的**确认**，不是变更要求） |  | ACCEPT** — 可作为「belief 层是 canonical 已决事项、非新增构念」的依据，用于回应 Archi~ | 08b 断言「LHRM 已经决定要有 belief 层」：`CURRENT_ARCHITECTURE.md` §3 已写下 `Reality != Observation != Belief`；§8 已写 `SimWorld_(Agent,m) = fork(BeliefState_A, mode)`；`AGENTS.md` 当前架构方向第 10 条已写明梦境/幻想/计划/反事实应作为 nested Belief。因此「剩下的唯一问题是它有多小」。 |
| `E-C25` | `PLAUSIBLE` | PLAUSIBLE | NO | 08b 的存在性结论**不是**对 07 的独立佐证（08b 未读 ~ | ACCEPT_AS_PROPOSAL** — 若 mission 确实写了「Kuhn's dogmatism parad~ |  |

## 2.F — lane `F`（dynamics / hysteresis / pair-state emergence）

| claim_id | primary | verdict（原文） | canon | corroboration | recommendation | claim（截断） |
|---|---|---|---|---|---|---|
| `F-#1` | `UNSUPPORTED` | UNSUPPORTED | NO |  | HOLD_FOR_EVIDENCE`** — 维持 `UNKNOWN` / `model hypothesis` 标签，~ | 在夫妻/恋爱/亲子/照护数据上未找到任何估计出迟滞环或路径依赖分支的同行评审实证研究；因此「迟滞是人类二人关系的可观测动力学性质」目前是 `model hypothesis`。 |
| `F-#2` | `WRONG-SCOPE` | WRONG-SCOPE | NO`（若写入 canonical 必须写成 method limit） |  | RECLASSIFY_AS_METHOD_LIMIT`** — 降级为「当前可用的耦合代理（生理同步 / 情绪协动）与关~ | 不是「我们还没测迟滞」，而是「我们测的那个过程（双向耦合）在多数 dyad 里不存在，所以迟滞的物理前提在多数 dyad 里不成立」。 |
| `F-#3` | `VERIFIED` | VERIFIED | NO |  | ACCEPT`** — 数值层完全可信；引用时必须同时带 `I²=76%`。 | 同步与关系结局 `ES = 0.09, p > .10, I² = 76.0%`；亚组交感 `+0.19`、副交感 `−0.21`、合并 `+0.16`；与表现结局 `ES = 0.26, I² = 52.7%`。 |
| `F-#4` | `VERIFIED` | VERIFIED | YES`** — `docs/foundation/CURRENT_ARCHIT~ |  | ACCEPT`** — 本 packet 中唯一一条我建议**直接升级为 durable change 而非 propo~ | JPSP / Psychological Science / JEP:General 中所有提及 Likert 的文章 **100%** 用度量模型处理序数数据；导致 false alarm、漏检、**系统性效应反转**（均值排序颠倒）；交互作用与趋势分析同样受影响；**对多个序数项取平均不能修复**；**不存在可靠的事后检出办法**；建议改用 ordered-probit。 |
| `F-#5` | `MIXED:VERIFIED+WRONG-SCOPE` | VERIFIED`（引文逐字命中；量词归属有轻微 `WRONG-SCOPE` 偏移） | NO |  | ACCEPT`**（引文层）— 同时要求修 `F4` 行的先行词与范围两处。 | Kelso (2012)` 明确—「亚稳态字面上是一种平稳瞬态」，而这类度量基于平稳性假设 → 「估计与定义冲突」。 |
| `F-#6` | `VERIFIED` | VERIFIED`（含引文卫生问题） | NO |  | ACCEPT`**（内容层）— 但要求把 `09` §5.2 的作者串统一为五人。 | 该文明确列出 `Tognoli et al. 2007; Oullier et al. 2008; Tognoli 2008` 作为 dyadic social coordination 的 metastability 发现，并含 Human Dynamic Clamp 实验。 |
| `F-#7` | `MIXED:VERIFIED+WRONG-SCOPE` | VERIFIED`（内容）** + **`WRONG-SCOPE`（把它称为「分岔 / bifurcation」） | NO |  | RECLASSIFY_AS_METHOD_LIMIT`** — 改称「**按离婚结果事后划分的两组轨迹**」，删除「真实~ | 不忠伴侣 5 年后分岔为「持续改善并维持」与「明显恶化并离婚」两条路径；不忠组离婚率超过对照组两倍；n=19；由「满意度读数 + 离婚这一离散标签事件」定义。 |
| `F-#8` | `PLAUSIBLE` | PLAUSIBLE | NO |  | ACCEPT_AS_PROPOSAL`**（限 `09` §4.4 已写下的限定条件内）。 | 148 个样本、153,396 名参与者、关系时长 3 个月–46 年、平均年龄 19–71 岁，个体差异秩序稳定性平均 `r = .76`（已校正测量误差衰减，平均时滞 2.30 年），且稳定性随年龄升高、在关系头几年较低。 |
| `F-#9` | `MIXED:PLAUSIBLE+WRONG-SCOPE` | PLAUSIBLE`（Hamaker 两句）/ `WRONG-SCOPE`（报告的转述与归因） | NO |  | HOLD_FOR_EVIDENCE`** — 保留 O2，但删去「这恰恰是关系数据最常见的情形」，把稳定性/trait ~ | (a) CLPM 的滞后参数不表示真实的 within-person 关系，可能导致对因果影响之**符号**的错误结论；(b) 当自回归参数极接近 0 时，难以区分测量误差方差与自回归过程的随机输入方差。推论：低自回归 = 低信噪比，而这是关系数据最常见的情形。 |
| `F-#10` | `MIXED:PLAUSIBLE+WRONG-SCOPE` | PLAUSIBLE`（Pohle 部分）/ `WRONG-SCOPE`（`N<50` 部分） | NO |  | RECLASSIFY_AS_METHOD_LIMIT`** — 把 `N<50` 那句从 O3 移出、单列为 estim~ | HMM 阶数选择是「notorious」问题；AIC/BIC 系统性偏向过多状态；不存在普适判据；状态数超数据支持时的非可识别性是阶数估计的隐含组成部分；随机效应方差在 `N<50` 时系统性正偏。 |
| `F-#11` | `PLAUSIBLE` | PLAUSIBLE`（且我认为这是 `09` 最正确的一节） | NO |  | ACCEPT`** — 补一条明确的 ESM/IL/EMA escape clause 到 §4.4（措辞建议见 `to~ | 在 3–7 波、12–21 年、`r≈.76`、单条自报满意度读数的条件下，组均值分段非线性趋势可估，dyad 层吸引域/停留时间/迟滞不可估；且报告明确**拒绝**给出任何所需波次数或功效值。 |
| `F-#12` | `WRONG-SCOPE` | WRONG-SCOPE`**（方法事实被用作本体/设计授权） | NO`（若写入 canonical 必须写成 method limit） |  | RECLASSIFY_AS_METHOD_LIMIT`** — 把「无资格」改为「无证据支撑」，并把 FACT-1 的定~ | FACT-1「没有任何一个框架在真实二元关系数据上有可接受的、可复现的动力学参数估计证据」+ FACT-4「迟存在性未知」⇒「任何离散层的位置，若要求它承担 `F` 的引擎角色，就必须先通过一个目前没有任何框架通过的证据门槛」⇒ 四层全部是非引擎位置。 |
| `F-#13` | `PLAUSIBLE` | PLAUSIBLE`**（L-A / L-B / L-C 成立；**L-D 不成立为独立层**） | NO`（`09` 已正确标为 `AI recommendation`） |  | ACCEPT_AS_PROPOSAL`** — 但改称「三层（L-A / L-B / L-C）+ 一个显式 join（`~ | 离散层应当存在且不止一层；四个具体位置为制度/协议事实层、观测者知识层、测量模型层、readout 层；任一层都不应是 `F` 的引擎。 |
| `F-#14` | `CONTESTED` | CONTESTED`** — 「K3 / K4 / K6 是真撤退条件」**成立**；「K1 / K5 / K7 / K8 / K9 是撤退条件」**不成立**。 | NO |  | REJECT`**（针对 K9；并对 K1 / K5 / K7 / K8 做定点修补）— 保留 K2 / K3 / K4~ | K1–K9 构成可被 reviewer 直接攻击的撤退条件集，其中 K4 的撤退成本最低、建议优先执行。 |
| `F-#15` | `PLAUSIBLE` | PLAUSIBLE | YES`** — `AGENTS.md`「Current architectur~ |  | ACCEPT_AS_PROPOSAL`** — 标 `HUMAN_GATED`；优先执行 §7-O5（先冻结可证伪转移律~ | 把 rule 9 的绝对否定降级为可证伪的分工主张：「标签序列不是状态的**充分**引擎。若在任何数据集上，给定底层状态后 label 序列不提供增量预测信息，则应正式承认 label 可作为可接受的粗状态层。」 |
| `F-#16` | `UNSUPPORTED` | UNSUPPORTED`**（作为累积论证）；`corroboration: NON_INDEPENDENT | NO |  | REJECT`**（作为累积论证）— 单一 absence，多处措辞不同但来源同一；parent join 时**不得*~ | 「无任何框架 / 无迟滞 / 无阈值」这一 absence 同时出现在 §2.1、§5.3、§8.4-A-4/5/6、§9.2-FACT-1/4、§9.8。 |
| `F-#17` | `VERIFIED` | VERIFIED`（引文与方向） | NO`（若采纳 A8，需连带 U6） |  | ACCEPT_AS_PROPOSAL`** — 引文与方向接受；措辞改为「在 relationship quality ~ | 在 443 对瑞士伴侣上，两个模型（comparative/discrepancy vs systemic）比较对关系质量的预测力，**systemic dyadic coping measure 是比 discrepancy measure 更强的预测者**。 |
| `F-#18` | `MIXED:UNSUPPORTED+VERIFIED` | UNSUPPORTED`**（就「唯一」与「涌现」两处用词；底层 Bodenmann 结果本身 `VERIFIED`，见 `F-C17`） | NO |  | HOLD_FOR_EVIDENCE`** — 删「唯一」与「真涌现」；保留为「文献中已知的、唯一一处两个有向状态的函数在~ | 10` §4.8 / §13：dyadic coping 是文献中**唯一**被实验证明「两个有向状态的函数不足」的构念；`CommonDyadicCoping_(A,B)` 是真正的 pair-level 涌现候选。 |
| `F-#19` | `PLAUSIBLE` | PLAUSIBLE | YES`** — `docs/foundation/PARAMETER_CONV~ |  | HOLD_FOR_EVIDENCE`** — 先要求 `10` 补上单 dyad / Case Bank 分支，再考虑写~ | Mutuality_k(A,B,t) = H(e_k(A->B,t), e_k(B->A,t))`，其中 `e_k(i->j) = D_k(i->j) − R_k(i) − T_k(j)`；朴素 `H(D_AB, D_BA)` 会系统性混入与本对无关的成分。falsifier：控制 `R,T` 后 `H(e)` 若不显著优于 `H(D)`，则残差化不必要。 |
| `F-#20` | `MIXED:VERIFIED+PLAUSIBLE` | VERIFIED`**（矛盾的存在性可由 canonical 文本本身证明；修正形式的合理性 `PLAUSIBLE`） | YES`** — `docs/foundation/CONSTRUCT_SCOP~ |  | ACCEPT`**（矛盾诊断）+ **`ACCEPT_AS_PROPOSAL`**（替换形式）。 | canonical 的 `Asymmetry_k(A,B) = distance(Z[k,A,B], Z[k,B,A])` 与 `AGENTS.md` representation invariant #4（不强迫 `0..1` / 欧氏 / 共同语义尺度）冲突；当 `Z` 是区间、序数、类别、概率分布或 `Unknown` 时 `distance` 未定义。修正为 `{left, right, comparison: 显式声明的比较器, comparator_id, evidence, unc~ |
| `F-#21` | `VERIFIED` | VERIFIED`**（relative / total / punitive 三分量）— 这是 `10` 最强的一节 | YES`** — `docs/foundation/PARAMETER_CONV~ |  | ACCEPT`** — 权力三分判定与所引主文献一致，punitive 分离有实验支持。 | relative power = power difference`（零和，可由两方向依赖不对称派生）；`total power = mutual dependence / relational cohesion`（非零和）；`punitive / retaliatory capacity` 不可由 dependence 派生。→ R2 作为完整表述 `NEGATIVE`；作为 relative power 分量的 readout **正确**。 |
| `F-#22` | `PLAUSIBLE` | PLAUSIBLE`**（处置正确，但执行必须分批） | YES`** — `PARAMETER_CONVERGENCE_V0_1.md`~ |  | ACCEPT_AS_PROPOSAL`**（附 R2-a / R2-b 拆分；R2-a 可直接 durable 化，R2~ | 把 R2 限定为「relative power 分量的 derived readout」，同时在 schema 中显式加入 punitive capacity、legitimacy/bases、perceived power、felt compliance 四个槽位 + 一个 domain 索引；`PowerImbalance_(A,B)` 保留为 derived readout。 |
| `F-#23` | `WRONG-SCOPE` | WRONG-SCOPE`**（技术性错配：把 Lawler 的 relational-cohesion 规格当成了 total-power 规格） | NO`（本条是缺陷诊断；修正后仍属 `F-C22` 的 R2-a） |  | REJECT`**（第 8 行的派生形式）— 改为：`TP` = 对称聚合（和）；`C`（relational cohe~ | total power` 可派生，形式为「对两条有向状态的对称聚合（Lawler 用几何平均）」；`10` 指出 R2 的写法遗漏此项。 |
| `F-#24` | `PLAUSIBLE` | PLAUSIBLE | NO`（属 `F-C22` 的 R2-a） |  | ACCEPT_AS_PROPOSAL`** — 依据 abstract 成立；请 lane 补 Overall & Ha~ | 真实亲密关系中 actor 与 partner 的**感知权力倾向正相关**而非反相关（若权力总是零和的话），且「few interactions involve one person having very high power and the other very low power」；因此 `f(dependence asymmetry)` 会把「双方都无权」与「双方都有权」判成同一状态。 |
| `F-#25` | `MIXED:PLAUSIBLE+PLAUSIBLE` | PLAUSIBLE`**（就「间接」这一自我定级 — `PLAUSIBLE` 恰是正确档位）；但**报告内部对该档级的表述不一致 | NO`（若采纳 A4，必须连带 U4） |  | HOLD_FOR_EVIDENCE`** — §13 的「间接但真实的支持」必须改回 §7 的定级；A4 的 felt-~ | 结构性权力不平等**不决定**顺从；`FeltCompliance_i(j, domain)` 是 `10` 唯一主张的「不可约关系-体验成分」，**但其证据是间接的**（`Lawler 1993` 明说抵抗 vs 顺从的条件**尚未解决**；没有任何研究在控制 perceived power 后检验 felt compliance 的增量）。 |
| `F-#26` | `PLAUSIBLE` | PLAUSIBLE`**（论证结构 sound；本体定位正确） | YES`** — `docs/foundation/CURRENT_ARCHIT~ |  | ACCEPT_AS_PROPOSAL`** — 接受 ontology-hole 的诊断；`SituationStruc~ | Interdependence Theory 的 interdependence matrix 提供 actor control / partner control / joint control 的 outcome-contingency 结构；该结构与 SRM 的 perceiver / target / relationship effect 三段分解**同构**，但 LHRM **没有** `actor × partner interaction` 这一层的**情境**表示。两个 dya~ |
| `F-#27` | `VERIFIED` | VERIFIED`**（含一处术语错配） | NO |  | ACCEPT`**（引文与 6→5 结论）— 删掉「（basis of dependence）」括注；两套六维命名必须择~ | 242 个条目；人们（in situ 与 ex situ）只能可靠区分 6 个维度中的 5 个，缺 **coordination**；得到的主观互赖模型仍解释 24% 的合作方差，超出 DIAMONDS。 |
| `F-#28` | `VERIFIED` | VERIFIED | NO`（§6.3 牵涉 P1，见 `F-C30`） |  | ACCEPT`**（引文层）— 修 issue 号（47(1)）；在 §6.2-B1 补一句「clarity 是 dir~ | clarity（「作为伴侣二人中的一员，我相信我们知道自己作为一对是谁」）与实际 agreement 相关，但**在 agreement 之外**预测 commitment（Study 2），并**预测 9 个月内解体可能性的降低**（Study 4）。四项研究：横断 1–2、实验 3、纵向 4。 |
| `F-#29` | `MIXED:VERIFIED+UNSUPPORTED` | VERIFIED`（数值）/ `UNSUPPORTED`（国别那一句的表述） | NO |  | ACCEPT`**（数值）— 改写国别那句为两篇文献分工陈述；修 `F-C30` 的作者名。 | 72 个独立样本 / 57 篇报告 / 17,856 人；total dyadic coping 与关系满意度的聚合零阶相关 `r = .45 (p=.000)`；按 partner 与按双方的知觉比按 self 的知觉预测更强；collaborative common / supportive / hostile-ambivalent coping 比 stress communication / delegated / protective buffering / overprotectio~ |
| `F-#30` | `VERIFIED` | VERIFIED`**（重复确实存在，且多处由报告**自己**的交叉引用证实） | NO`（报告内部记账问题） |  | REJECT`**（表格当前形态）— 合并第 4/7 行、第 21b/23 行；第 19 行的判定需撤回或改依据；G11~ | 10` §5 的 test table 与 §6.3 / §7 / §8 之间存在同义与双重计数。 |
| `F-#31` | `UNSUPPORTED` | UNSUPPORTED`**（就这些具体条目） | NO |  | HOLD_FOR_EVIDENCE`** — 要求 `10` 在 §12 加一列 `page_verified`（逐字引~ | 10` 建立三档证据分级（`CITED_PRIMARY` / `CITED_SECONDARY` / `AGENT_RECALL`）并据此把若干来源标为「本次实际读到原文」；我核实后发现若干条**分级或元数据与事实不符**。 |
| `F-#32` | `CONTESTED` | CONTESTED`**（两份报告均在 lane `F` 内，冲突可指名） | YES`** — `AGENTS.md` rule 5（shared pair ~ |  | HOLD_FOR_EVIDENCE`** — 不必等数据；这是一个**架构裁决**。请 Architect 明确写下 s~ | 09` §9.3.1 判 L-A（制度/协议事实层）合法，三条判据之一是 (ii)「**被关系状态更新而非生成关系状态**」。`10` §2 定义 `Φ(i,j,t) = shared pair facts：制度事实、约定、规范、分工、第三极、领域分区`，其中**分工**与**领域规范**被 `10` 自己的 §6.3-B3 证明会**直接改写有向状态**。 |
| `F-#33` | `VERIFIED` | VERIFIED`**（同一层的两个名字，跨报告同义） | NO`（命名统一属文档卫生） |  | ACCEPT_AS_PROPOSAL`** — 统一采用一个符号（建议 `Belief_i(·)`），并把 `09` 的~ | 09` §9.3.2 定义 L-B = `Belief_i(A–B 是什么) ∈ {friend, partner, married, ex, unknown, contested}`；`10` §2 定义 `B_i(X) = i 关于 X 的信念`，并注明 `[LHRM 已有层]`。 |

## 2.G — lane `G`（general dyad scope / ABM / LLM layer）

| claim_id | primary | verdict（原文） | canon | corroboration | recommendation | claim（截断） |
|---|---|---|---|---|---|---|
| `G-C1` | `VERIFIED` | VERIFIED`（对**算术**与**披露充分性**两项） | NO` — 研究制品的自我限定问题，不涉及 canonical。 |  | ACCEPT` — 接受 69/216 与零不变性研究这两个数字、接受四处披露的充分性；**但**要求把矩阵逐行重标为 ~ | 11` §1 修订块自报：24 行 × 9 类 dyad = **216 个判定格**，其中 **69 格**为 `MEANING_PRESERVED`，其背后有**零**项跨 dyad-type 测量不变性研究；这 69 格「是同一个未检验假设的 69 次重述，不是 69 条发现」，不可计数、不可聚合、不可当作相互独立的证据。 |
| `G-C2` | `MIXED:PLAUSIBLE+VERIFIED` | PLAUSIBLE` — 披露充分性 `VERIFIED_BY_ME`（见 `G-C1`）；缺陷定位是审计判断。 | NO |  | RECLASSIFY_AS_METHOD_LIMIT` — 把「216 格兼容性矩阵」整体降级重标为「216 个**待检~ | 216 格矩阵呈现 216 条等权点判定，其中 69 条（31.9%）是零证据支撑的语义判断；披露已做到可接受的上限，但**制品的证据状态编码**仍是缺陷。 |
| `G-C3` | `UNSUPPORTED` | UNSUPPORTED`（对这五个具体数字）— 我逐格重算后证伪。 | NO |  | REJECT` — 拒绝以现有形式引用 §6.1 的格统计。要求 parent 在 synthesis 中**只**引用~ | 11` §6.1（采样框架后果，全报告最承重的一节）引用了四个矩阵格统计，其中两个错误；§3.4 引用的 D 列统计两个都错。 |
| `G-C4` | `VERIFIED` | VERIFIED`（报告确实这样自述）→ 判定为**报告内部类目错误**，`RECLASSIFY` 目标 | YES`（见 `G-C5`） |  | ACCEPT` — 接受 §3.1 的分析，把它升级为 canonical-change 候选；同时**要求**把 `s~ | 11` §3.1 正确论证 `SexualDesire × {友谊,兄弟姐妹,亲子,敌对} = NA` 是**值类缺口**（b 类），报告原文写「这不是『加一个构念』，是给状态空间加一个值类，因此它**不在 8 维 basis 里**，不会被 `Gate C` 发现」；但 §2 仍把它记为语义矩阵里的 `NOT_APPLICABLE` 码，且 §1 码表里没有这个值类名。 |
| `G-C5` | `VERIFIED` | VERIFIED` — 我**独立地**用 canonical 文本复现了这个不相容，不需要任何文献。 | YES`** — `docs/foundation/CURRENT_ARCHIT~ |  | ACCEPT` — 这是我在本 cluster 里找到的**唯一**必须落到 canonical 而不能停在 propo~ | 11` §3.1：对兄弟姐妹的性欲坐标，正确值既不是 `Unknown`（可能高度确信其不存在）也不是 `0`（「被测到的零」是另一个断言），而是「结构性不适用」；现有值类集合里没有这一格，**唯一的合法表示方式就是把不适用填成 0 或 Unknown — 正是 `AGENTS.md` 禁止的动作**。 |
| `G-C6` | `MIXED:PLAUSIBLE+WRONG-SCOPE` | PLAUSIBLE` — 3 条证据在域内且强，1 条著录不完整，1 条 `WRONG-SCOPE`。 | NO` — **必须停在 proposal。** 三条理由：(a) 需 U6（承~ |  | ACCEPT_AS_PROPOSAL` — 接受为候选登记，但**必须**：(i) 把 `Meyer & Allen` ~ | 11` §3.2：五条独立证据线收敛到「obligation 与 affection/attachment 可分离，且在亲属与照护域承重」；提案新增 `Obligation_(i->j)` 为第九个 directed candidate，并把 `Dedication` 收窄为 affective dedication。 |
| `G-C7` | `VERIFIED` | VERIFIED`（三重计数确实存在）→ 判定为**计数缺陷 | NO |  | RECLASSIFY_AS_METHOD_LIMIT` — 要求 parent 把三项合并为**一条** canonic~ | 11` 的 §3.2（新增 `Obligation` directed construct）、§3.7（新增 `RoleContract_(A,B)` pair fact）、§4 `L-10`（`family obligations` 放在 Agent 层是层级错置）三项，最终都主张同一件事：**义务/契约性内容属于 pair-institutional 层，不是 dyadic-psychological 也不是 Agent 层**。 |
| `G-C8` | `PLAUSIBLE` | PLAUSIBLE` — 结构性论证可检验成立；**支撑引用的著录质量不配其安全权重**。 | NO` — **必须停在 proposal。** 理由：(a) 支撑引文全部 `~ |  | ACCEPT_AS_PROPOSAL` — 但把**主论据**从 §3.3（`Constrainedness` 提案）换~ | 11` §3.3：`ConstraintsAndAgreements` 与 P5 都内建「同意/consent」，但域已写入「违法或违反社会规范」；非自愿约束（coercive control、人身控制、勒索、囚禁）既不是 agreement 也不是 `Environment` 也不是 `Agent` — **违法性有轴，但约束能力本身没有坐标**。§5 排序明标「**安全价值最高**」。 |
| `G-C9` | `VERIFIED` | verdict:** `VERIFIED` — 我**独立地**用 canonical 文本复现，未依赖报告的外部引用。 | requires_canonical_change:** `NO`（本条）。但 ~ |  | recommendation_to_architect:** `ACCEPT` — 这是本 cluster 中**安全价~ | 11` §4 `L-1`：一个健康的高照护 dyad（受照护者高度依赖、方向不对称、替代方案少）与一个胁迫 dyad（intimate terrorism）在 `OutcomeDependence` (D8) 上**数值结构相同**，`R2 PowerImbalance` 会打成同一类，而它们在伤害上相反。措辞读起来是关于 i 的 option set 的中性事实，**而它实际是伤害结构本身**。 |
| `G-C10` | `WRONG-SCOPE` | WRONG-SCOPE` — 支撑这一判定的唯一实证来源是**一个** 定性同胞访谈研究，且 `11` §6.2 自己把同一格称为「**定义欠定**」而非「语义改变」。 | NO |  | REJECT` — 拒绝以现有形式接受 `Trust` 行的 5 个 `MEANING_SHIFTS`。要求：(i) 降~ | 11` §2 把 `Trust` 在 `S`(兄弟姐妹)、`K`(亲子)、`C`(照护)、`W`(专业)、`A`(敌对) 五列判为 `MEANING_SHIFTS`，理由是 `Trust` 定义「愿意把某类脆弱性暴露给 j」内建了**披露史**前提。 |
| `G-C11` | `MIXED:PLAUSIBLE+VERIFIED` | verdict:** `PLAUSIBLE`（值类论证 `VERIFIED`；`NA` 判定本身 `PLAUSIBLE`，但**最强反证未被处理**） | requires_canonical_change:** `NO`（本条）；值类~ |  | recommendation_to_architect:** `HOLD_FOR_EVIDENCE` — 保留 §3.1~ | 11` §2/§3.1 把 `SexualDesire` 在友谊、兄弟姐妹、亲子、敌对四列判为 `NOT_APPLICABLE`（结构性不适用），论证依据是状态空间缺「不适用」值类。 |
| `G-C12` | `PLAUSIBLE` | verdict:** `PLAUSIBLE` — 论证结构成立且是可证伪的；但三条支撑引用**著录不完整**。 | requires_canonical_change:** `NO` — **必须~ |  | recommendation_to_architect:** `ACCEPT_AS_PROPOSAL` — 接受为 Ga~ | SRM 式加法分解 `Construct(i->j,t) = population baseline + source_i + target_j + directed_dyad_(i->j) + context/history residual` 的可识别性要求 (a) target 属性与 source 的 dyad 进入/选择近似独立、(b) dyad 可重新选择；在亲属 dyad 上两条**按构造成立地失败**，故 `context/history residual` 不是残差而是主项，`~ |
| `G-C13` | `VERIFIED` | verdict:** `VERIFIED` — 我**独立地**逐条比对了三份 canonical 清单。 | requires_canonical_change:** **`YES`** —~ |  | recommendation_to_architect:** `ACCEPT` — 这是我在本 cluster 里找到的~ | 11` §4 `L-8`：`CONSTRUCT_SCOPE_DIRECTIONALITY.md` §7.6、`PARAMETER_CONVERGENCE_V0_1.md` §2.4、§15 Gate B 三处清单**互不相同**，且**都不含** `sibling`、`parent–adult-child`、`ex-partner`、`professional/cooperative`、`adversarial/harm-asymmetric`、`dating-stranger`；本 audit~ |
| `G-C14` | `MIXED:PLAUSIBLE+WRONG-SCOPE` | verdict:** `PLAUSIBLE`（对「专业 dyad 上 role 是承重变量」）/ `WRONG-SCOPE`（对「因此 `AGENTS.md` 第 3 条不成立」这~ | requires_canonical_change:** `NO` — **必须~ |  | recommendation_to_architect:** `HOLD_FOR_EVIDENCE` — (i) 更正 ~ | 11` §3.7：`AGENTS.md`「Keep `Role` explicit as a query/evaluation lens; it does not replace world state」在**专业 / 亲属 / 照护**三类 dyad 上不成立 — 约束、依赖、行动空间都是 role 决定的。提案保留 `Role` 作为 query lens，新增 `RoleContract_(A,B)` pair fact。 |
| `G-C15` | `MIXED:VERIFIED+PLAUSIBLE` | verdict:** `VERIFIED`（引语逐字无误）→ 但对「互斥」这一步推论判 `PLAUSIBLE`，对 `I4` 的「排除性证据」框架判 `WRONG-SCOPE | requires_canonical_change:** `NO |  | recommendation_to_architect:** `ACCEPT`（引语与 DOI 均 `VERIFIED_~ | Snijders, van de Bunt & Steglich (2010) 原文：tie 的存在被假定为**处于发送方单边控制之下**，因此**排除大多数需要协商才能成立的关系类型**；伴侣、亲属、照护、合作都属于「tie 的存在需要双方协商」的类型，因此 **SAOM 的成功前提与 LHRM 的对象前提互斥**。 |
| `G-C16` | `MIXED:VERIFIED+PLAUSIBLE` | verdict:** 第一条 `VERIFIED`；第二条 `PLAUSIBLE`（未找到出处）；`12` 的推论 `WRONG-SCOPE`（因为它遗漏了同页的例外句） | requires_canonical_change:** `NO |  | recommendation_to_architect:** `RECLASSIFY_AS_METHOD_LIMIT` ~ | 12` §3.1 C-SAOM：SAOM 状态**严格二值**（引 `Weighted networks are not allowed`）；且 creation / endowment / evaluation **三者不可同时出现在同一模型中（完美共线）**。`12` 据此判「二值化也直接违反 LHRM 的混合态表示」。 |
| `G-C17` | `WRONG-SCOPE` | verdict:** `WRONG-SCOPE` — 该负结论的**层级与被陈述的层级不匹配**：它是「在已检索场所内未找到」，被表述为「不存在」。 | requires_canonical_change:** `NO`（研究表述问题~ |  | recommendation_to_architect:** `REJECT` — 拒绝以「不存在」形式引用。**必须*~ | 12` §0 第 1 条（headline）：**不存在**可与 LHRM 对象直接比较的既有关系 ABM；LHRM 在「关系内部的、方向化的、保留 Unknown 的时间索引状态」这个维度上「不是落后，而是**孤立**」。§1：「通过 C5 的：**本 lane 未找到任何一个**。」 |
| `G-C18` | `PLAUSIBLE` | verdict:** `PLAUSIBLE` — 结论方向可辩护，但报告**低配了自己的正面证据**，且推导链依赖 `G-C17` 的未加限定负结论。 | requires_canonical_change:** `NO`（`12` §~ |  | recommendation_to_architect:** `HOLD_FOR_EVIDENCE` — **不要按 `~ | 对 LHRM 第一阶段目标（表示完备性 + Case Bank 逐句映射），ABM **不是正确工具**；「对 LHRM 声明的问题，ABM 目前主要是一个隐喻生成器」。 |
| `G-C19` | `MIXED:VERIFIED+VERIFIED` | verdict:** `JuSpace` `VERIFIED` / `smallslm` `VERIFIED` / `ASON` `PLAUSIBLE`（结论对，**检索不完整**~ | requires_canonical_change:** `NO |  | recommendation_to_architect:** `ACCEPT` — 三个名字的证伪**成立**，可作为「~ | 12` §2.3：任务书候选中的 `JuSpace` 实为 Julich 神经影像学工具箱（名字冲突，不采用）；`smallslm` 与 `ASON` 四路检索 0 命中，`UNVERIFIED_OR_UNKNOWN`，倾向不存在。 |
| `G-C20` | `MIXED:UNSUPPORTED+WRONG-SCOPE` | verdict:** **`UNSUPPORTED`（数字）+ `WRONG-SCOPE`（推论）**；规范性结论单独判 `PLAUSIBLE`，但**不成立于报告给出的证据链**~ | requires_canonical_change:** `NO`（研究表述与证~ |  | recommendation_to_architect:** `REJECT` — **拒绝以现有形式把「跨域 AURO~ | 13` §9.6（自标「**本报告最强的一条元论证**」）与 §0 立场声明：多个 LLM 在模糊输入上**自发收敛到同一似真解释**，多个模型一致「不是因为对，而是因为共享训练分布与『选取最连贯叙述』的归纳偏置」；检测 arXiv:2602.13224 的「检测 AUROC **域内 0.76–0.99 但跨域 0.50（随机）**，判别方向跨域近正交（平均余弦 **−0.07**）」；→ 「**自发产生的虚假内容与真实内容在可检测性上不可区分**」；推论「**『多个 LLM 达成一致』是 F~ |
| `G-C21` | `MIXED:VERIFIED+UNSUPPORTED` | verdict:** §13.1 目标重定向 `VERIFIED`（方法论论证成立）；§13.2 的指标集 `UNSUPPORTED` 为充分评估工具（存在两个平凡策略同时最大化全~ | requires_canonical_change:** `NO`（LLM 层评~ |  | recommendation_to_architect:** `ACCEPT` §13.1 的目标重定向（**保留**：~ | 13` §13.1 主张 LHRM 第一产物是 latent dyad state，没有 ground truth 也**不应该**有，因此「抽取准确率」在 LHRM 语境下**没有定义**；§13.2 提出六个**完全可机器判定**的表示忠实度指标替代之（`SPAN_SUPPORT_RATE`=1.0、`ENTITY_INSERTION_RATE`=0、`UNKNOWN_PRESERVATION_RATE`=1.0、`FUTURE_LEAK_RATE`=0、`HOLDER_LEAK_RATE`~ |
| `G-C22` | `VERIFIED` | verdict:** `VERIFIED` — 遗漏确实存在（穷尽检索）。 | requires_canonical_change:** `YES` — 但**~ |  | recommendation_to_architect:** `ACCEPT` — 要求 (i) `13` 在 §7（p~ | 13` 在 §1、§4.1、§5.3、§7.3、§9.2、§13.2 六处实质使用 `FIXTURE_003` 的 transcript 单元与 freeze rules，全文**不记录**该 fixture 的 `pointer_only` / `ai-train=no` / `GPTBot Disallow` 权利边界。 |
| `G-C23` | `VERIFIED` | verdict:** `VERIFIED` — 日期与 Recommendation 身份逐字核实通过。 | requires_canonical_change:** `NO |  | recommendation_to_architect:** `ACCEPT` — 事实无误。但要求 `13` §12 ~ | PROV Working Group 于 **2013-04-30** 发布 12 份文档，其中四项为 W3C Recommendation：`PROV-DM`、`PROV-O`、`PROV-N`、`PROV-CONSTRAINTS`。 |
| `G-C24` | `VERIFIED` | verdict:** `VERIFIED`（三处均经我独立核实） | requires_canonical_change:** `NO |  | recommendation_to_architect:** `RECLASSIFY_AS_METHOD_LIMIT` ~ | (a) `11` §9 的 Olson, Russell & Sprenkle (1983) DOI 不可解析；(b) `12` 附录 A 把 Edmonds 误写为 Edwards；(c) `13` §9.6 把 arXiv:2602.13224 的题名单数化。 |
| `G-C25` | `CONTESTED` | verdict:** `CONTESTED`（swarm 内 cluster `G` 内部）— `12` 提供了 `13` 标为「0 条文献」的一个**结构同构先例**；`13` ~ | requires_canonical_change:** `NO`（报告间的一致~ |  | recommendation_to_architect:** `RECLASSIFY_AS_METHOD_LIMIT` ~ | 13` §12 判定其 `Observation / Belief / Environment` 分层的外部证据为「**基本为空**… **0 条外部文献**。这是 LHRM 独有结构」；`12` §8 `I8` 判定 Concordia 的 GM/player 分离「在结构上**等价于** LHRM 的 `Reality != Observation != Belief` 分层」。 |
| `G-C26` | `VERIFIED` | verdict:** `VERIFIED`（三条记录确实存在且确实未被带入裁决）→ 判定为**报告内部权重分配缺陷 | requires_canonical_change:** `NO`（这三项**支~ |  | recommendation_to_architect:** `ACCEPT` — 要求 parent 在 synthe~ | 12` 记录了三条对 LHRM **已有 canonical 决策**的独立外部佐证，但三条全部只出现在 §2.1 / §8（作为「可复用想法」），从未进入 §10 的裁决，因此在本报告的最终结论里权重为零。 |
| `G-C27` | `MIXED:PLAUSIBLE+VERIFIED` | verdict:** `PLAUSIBLE`（Angus 那条我未核实原文）→ 但**依赖图**部分我判 `VERIFIED`，且方向与 `12` 所述相反（好消息）。 | requires_canonical_change:** `NO |  | recommendation_to_architect:** `ACCEPT` — 接受 C1/C2/C6 三条失败模式~ | 12` §4.2 元证据第 2 条：Grazzini & Richiardi (2015) 报告 Angus & Hassani-Mahmooei (2015) 扫描 100+ 篇 JASSS ABM 论文，「found **very few instances** of additional (statistical) modelling of TS data」。`12` 自称这是「本报告最有力的元证据之一」，并建议单独核实。 |
| `G-C28` | `WRONG-SCOPE` | verdict:** `WRONG-SCOPE` — 转述把来源的结论方向讲反了；`13` 自己引的发现 3 是该转述的反证。 | requires_canonical_change:** `NO |  | recommendation_to_architect:** `REJECT` — 拒绝采用「LLM 一致 = 对齐多数~ | 13` §2.2(c) 标题「**LLM 的一致性是『对齐多数派先验』，不是『更准』**」；推论「把『LLM 一致度高』当质量证据，等于说『LLM 和人群**平均/多数**读法一致』」，并据此推出「这在专家自己都分裂的文本上恰恰是误导」。 |
| `G-C29` | `WRONG-SCOPE` | verdict:** `WRONG-SCOPE` — `13` 对「与 LLM 一致度比」施加循环论证标准，对自己的 gold 不施加。 | requires_canonical_change:** `NO |  | recommendation_to_architect:** `ACCEPT`（保留 §13.2 的四项干净指标）**+~ | 13` §13.2 主张六项指标「在冻结 fixture 上**完全可机器判定**（因为 fixture 本身是冻结的、有明确 `fact_status` 与 `source_anchor`）」；但被抽取的文本与判定 gold 是同一批文本的同一批标签。 |
| `G-C30` | `CONTESTED` | verdict:** `CONTESTED`（报告内部自相矛盾） | requires_canonical_change:** `NO |  | recommendation_to_architect:** `REJECT` — 拒绝同时接受 §2 与 §6.2 对~ | 11` §2 把 `Trust × {S,K,C,W,A}` 判为 `MEANING_SHIFTS`；§6.2 对同一构念写「这一格判为『**定义欠定**，不是「数据缺失」」。 |

## 2.H — lane `H`（paper positioning / novelty）

| claim_id | primary | verdict（原文） | canon | corroboration | recommendation | claim（截断） |
|---|---|---|---|---|---|---|
| `H-C01` | `VERIFIED` | VERIFIED | NO |  | ACCEPT |  |
| `H-C02` | `PLAUSIBLE` | PLAUSIBLE | NO |  | HOLD_FOR_EVIDENCE`（补 §10 缺条 + 打开 1998 原文） |  |
| `H-C03` | `PLAUSIBLE` | PLAUSIBLE | NO |  | HOLD_FOR_EVIDENCE |  |
| `H-C04` | `PLAUSIBLE` | PLAUSIBLE | NO |  | HOLD_FOR_EVIDENCE |  |
| `H-C05` | `PLAUSIBLE` | PLAUSIBLE | NO |  | RECLASSIFY_AS_METHOD_LIMIT`（§2.1 与 §5.A4 二者取一） |  |
| `H-C06` | `MIXED:VERIFIED+PLAUSIBLE` | VERIFIED`（PRQC 部分）/ `PLAUSIBLE`（Sternberg、Reis&Shaver 部分） | NO |  | ACCEPT`（PRQC 主张）/ `HOLD_FOR_EVIDENCE`（Sternberg、Reis&Shaver ~ |  |
| `H-C07` | `MIXED:VERIFIED+PLAUSIBLE` | VERIFIED`（Fletcher 1999 元数据）/ `PLAUSIBLE`（因子数与纵向结果） | NO |  | ACCEPT |  |
| `H-C08` | `CONTESTED` | CONTESTED`（就 report 内部一致性） | NO |  | RECLASSIFY_AS_METHOD_LIMIT`（§2.1 与 §3 必须择一；我建议按 §3 走 NC-3，因为~ |  |
| `H-C09` | `PLAUSIBLE` | PLAUSIBLE | NO |  | HOLD_FOR_EVIDENCE |  |
| `H-C10` | `UNSUPPORTED` | UNSUPPORTED | NO |  |  |  |
| `H-C11` | `UNSUPPORTED` | UNSUPPORTED | NO |  | REJECT`**（「一一对应」这一断言） |  |
| `H-C12` | `PLAUSIBLE` | PLAUSIBLE | NO |  | RECLASSIFY_AS_METHOD_LIMIT`（§2.1 与 NC-5 择一） |  |
| `H-C13` | `PLAUSIBLE` | PLAUSIBLE | NO |  | ACCEPT_AS_PROPOSAL`（降级为「中」） |  |
| `H-C14` | `MIXED:VERIFIED+PLAUSIBLE` | VERIFIED`（Eberhardt 全部数字）/ `PLAUSIBLE`（Zhang 2024、QualiGPT 数字） | NO |  | ACCEPT |  |
| `H-C15` | `PLAUSIBLE` | PLAUSIBLE | NO |  | HOLD_FOR_EVIDENCE |  |
| `H-C16` | `PLAUSIBLE` | PLAUSIBLE | NO |  | HOLD_FOR_EVIDENCE |  |
| `H-C17` | `UNSUPPORTED` | UNSUPPORTED |  |  |  | §1 BLUF「LHRM 的 8 个有向构念全部是 REUSE，无一条可主张原创 / 强度=高（逐条有 DOI）」 |
| `H-C18` | `CONTESTED` | CONTESTED |  |  |  | NC-1** 以 N=1 个体、逐句可审计的「表示完备性」为主指标的关系状态表示语言 — 置信度 MEDIUM（窄化）/ LOW（按现状表述） |
| `H-C19` | `VERIFIED` | VERIFIED |  |  |  | NC-2** 逐维度双向有向状态 + 互惠/权力由派生 — 置信度 LOW，「会被一击击穿」 |
| `H-C20` | `CONTESTED` | CONTESTED |  |  |  | NC-3** `Agent｜Relationship｜Environment｜Belief` + `Reality≠Observation≠Belief` + 嵌套反事实世界 + history lineage DAG — 置信度 MEDIUM-LOW |
| `H-C21` | `PLAUSIBLE` | PLAUSIBLE |  |  |  | NC-4** 把「映射失败率 + 弃答率」作为第一指标 — 置信度 MEDIUM，「最可辩护的一条」 |
| `H-C22` | `CONTESTED` | CONTESTED |  |  |  | NC-5** 显式拒绝预枚举关系状态机 — 置信度 MEDIUM |
| `H-C23` | `PLAUSIBLE` | PLAUSIBLE |  |  |  | NC-6** 126 条 proxy 分解词典 — MEDIUM-LOW（科学）/ MEDIUM-HIGH（artifact） |
| `H-C24` | `UNSUPPORTED` | UNSUPPORTED |  |  |  | NC-7** LLM 作「自适应访谈器材」（EIG 选题、双人双向、维护非对称有向状态）— 置信度 MEDIUM，「网格中最空的一格」 |
| `H-C25` | `UNSUPPORTED` | UNSUPPORTED |  |  |  | §3 开头的通用警告（"这是定位失败最常见的模式"）足以防止本报告自己犯 novel-combination 错误 |
| `H-C26` | `WRONG-SCOPE` | WRONG-SCOPE |  |  |  | §2.5 + F-6 + F-16 用 Lalk et al. (2025) 证明「LLM 抽多类语义的上限是 κ=.42」 |
| `H-C27` | `UNSUPPORTED` | UNSUPPORTED |  |  |  | F-1…F-20 这 20 条禁止主张清单是完备的 |
| `H-C28` | `UNSUPPORTED` | UNSUPPORTED |  |  |  | F-6 与 F-16 各自独立 |
| `H-C29` | `CONTESTED` | CONTESTED`（重复计数） |  |  |  | F-1 与 REUSE 表 L40 是两条独立结论 |
| `H-C30` | `WRONG-SCOPE` | WRONG-SCOPE |  |  |  | §5.A2「你的 8 个有向坐标能复现已知因子结构吗？」是可被纯文档分析回应的（「这是最有杀伤力也最可修的批评」） |
| `H-C31` | `WRONG-SCOPE` | WRONG-SCOPE |  |  |  | O-13：Joel et al. 2020 是 `E` 层「不同环境 → 不同长期结果」这一主张的「直接反例」 |
| `H-C32` | `WRONG-SCOPE` | WRONG-SCOPE`（部分） |  |  |  | §5.A3「LHRM 把双向有向坐标当架构基石，恰落在文献中最不可靠的那一半上」（依据 Joel 2020） |
| `H-C33` | `VERIFIED` | VERIFIED |  |  |  | §5.E 组 E1「schema 有形式语义吗？是语法、本体、EBNF 还是散文？」= 致命，当前不能应答 |
| `H-C34` | `VERIFIED` | VERIFIED |  |  |  | §5.F 组「ML 会议 = dead end，不要投」 |
| `H-C35` | `PLAUSIBLE` | PLAUSIBLE |  |  |  | §5.C3「VALIDATION_CORPUS 已做敏感内容筛选（无未成年人、无性暴力），是加分项」 |
| `H-C36` | `UNSUPPORTED` | UNSUPPORTED |  |  |  | §6 结论「M0–M5 ≈ 5–7 个月单人全职」 |
| `H-C37` | `UNSUPPORTED` | UNSUPPORTED |  |  |  | M2（人类编码基线）估 4–6 周 |
| `H-C38` | `WRONG-SCOPE` | WRONG-SCOPE`（依赖倒置） |  |  |  | M7（测量学，2–4 个月，N≥数百）在 M0–M6 之后可达 |
| `H-C39` | `CONTESTED` | CONTESTED |  |  |  | M8（纵向 dyad 样本，1–3 年，≥200–500 对，≥3 时间点，双方独立测量）的估计与「阻塞后续：否」的标注 |
| `H-C50` | `PLAUSIBLE` | PLAUSIBLE`（建议改写为「README L5 的用途句未带状态标记，与 L7/L121 的下游定位措辞不对称」） |  |  |  |  |
| `H-C51` | `WRONG-SCOPE` | WRONG-SCOPE`**（正确说法：「目标句里的『数学』造成**期待风险**，不是 overclaim」） |  |  |  |  |
| `H-C52` | `WRONG-SCOPE` | WRONG-SCOPE`**（(a) 必须撤回；(c) 行号错；(b) 需补引 L166/L179） |  |  |  |  |
| `H-C53` | `WRONG-SCOPE` | WRONG-SCOPE |  |  |  |  |
| `H-C54` | `WRONG-SCOPE` | WRONG-SCOPE`**（引文截断 + 事实错误「Gate C 明确 PENDING」） |  |  |  |  |
| `H-C55` | `CONTESTED` | CONTESTED`（问题真实：以偏概全） |  |  |  |  |
| `H-C56` | `MIXED:CONTESTED+VERIFIED` | CONTESTED`（「无出处」= VERIFIED；「一一对应」= UNSUPPORTED） |  |  |  |  |
| `H-C57` | `NOT_ENUM` | Kenny |  |  |  |  |
| `H-C58` | `PLAUSIBLE` | PLAUSIBLE`（把批评从「实质经验主张」收窄为「`findings` 标签」） |  |  |  |  |
| `H-C59` | `MIXED:CONTESTED+VERIFIED` | CONTESTED`（Crossref 部分 VERIFIED；上游 CDPS 原文 NOT_OPENED；「STAGE_SUMMARY 写 72–89」= 不成立；行号 1440~ |  |  |  |  |
| `H-C60` | `PLAUSIBLE` | PLAUSIBLE`（降级：历史 draft 的措辞问题，不是 canonical 定位问题） |  |  |  |  |
| `H-C61` | `WRONG-SCOPE` | WRONG-SCOPE |  |  |  |  |
| `H-C62` | `WRONG-SCOPE` | WRONG-SCOPE |  |  |  |  |
| `H-C63` | `WRONG-SCOPE` | WRONG-SCOPE |  |  |  |  |
| `H-C64` | `WRONG-SCOPE` | WRONG-SCOPE |  |  |  |  |
| `H-C65` | `PLAUSIBLE` | PLAUSIBLE`（从「自相矛盾」降为「措辞不对称」） |  |  |  |  |
| `H-C66` | `VERIFIED` | VERIFIED`（并建议 Architect 把 O-17 当作其余各行的改写范本） |  |  |  |  |
| `H-C49` | `CONTESTED` | CONTESTED`（12 : 5） |  |  |  | 17 条 O-row 的引文准确性整体 |

## 2.I — lane `I`（red-team falsifiers / Gate A-B-C）

| claim_id | primary | verdict（原文） | canon | corroboration | recommendation | claim（截断） |
|---|---|---|---|---|---|---|
| `I-C1` | `VERIFIED` | VERIFIED | YES** — `PARAMETER_CONVERGENCE_V0_1.md` ~ | NON_INDEPENDENT`（A03 §1.4 明确是对 17 ~ | ACCEPT | Gate A/B/C 三门在判据原文下均不存在会被算作失败的结果 |
| `I-C2` | `CONTESTED` | CONTESTED**（核心成立，两处子命题被我推翻） | YES** — §2.1–§2.6 全族 + §2.6 line 86 的自我断~ | NON_INDEPENDENT`（A03 与 17 都未处理 §2.~ | ACCEPT_AS_PROPOSAL**（接受「无门产生否决」这一事实；不接受「§2.6 是唯一删除判据」与「basis~ | §2.6 `Representation necessity` 结构上永不触发，8 项 basis 单调增长 |
| `I-C3` | `VERIFIED` | VERIFIED | 阈值 | veto`，除 §2.6 自身提问外**无任何实现**。`FIXTU~ | YES** — `PARAMETER_CONVERGENCE_V0_1.md` §2.6 与 §15；不能停在 prop~ | §2.6` line 86「这项将在 Case Bank regression 中直接测试」是一句关于自身可测性的未兑现承诺**：全项目不存在「移除构念 k 后以同语料重跑」的测试臂 |
| `I-C4` | `VERIFIED` | VERIFIED | YES** — `FIXTURE_003` §7 的计数报告清单（但**不能改已~ | NON_INDEPENDENT`（A03 §1.4 是对 17 F1~ | ACCEPT**（并采用我补的 fixture 级证据） | MAPPING_FAILURE` 在类型上不可达 |
| `I-C5` | `VERIFIED` | VERIFIED**（采 A03 计数） | NO | NON_INDEPENDENT | RECLASSIFY_AS_METHOD_LIMIT**（把 17 的「三个」更正为 A03 的「4+1+1」；这是计数~ | catch-all 数量 = 4 个类 + 1 自由文本槽 + 1 诊断出口 |
| `I-C6` | `VERIFIED` | VERIFIED | YES — `PARAMETER_CONVERGENCE` §13 诊断出口需绑~ | INDEPENDENT**（17 未指出该措辞的循环效果） | ACCEPT | §13「禁止**第一反应**直接新增 primitive」+ §15 step 5 构成无终止条件的修复环；出口没堵死，但**唯一被写下来的动作就是「修」 |
| `I-C7` | `VERIFIED` | VERIFIED | YES — `PARAMETER_CONVERGENCE` §15 Gate B~ | INDEPENDENT**（`17` 与 `A03` 各给一个错数；~ | ACCEPT | Gate B 的 11 个 cell 中 10 个是项目自己既有文本的逐条复述，唯一新 cell 是 `high-attraction/low-trust |
| `I-C8` | `VERIFIED` | VERIFIED | NO | INDEPENDENT | RECLASSIFY_AS_METHOD_LIMIT**（`17` F9 表应重出；A03 的表更完整，两处 cell ~ | 17` 的 Gate B 覆盖表枚举不完整：含 1 个非 Gate B cell（`work colleague`），漏 2 个真 cell（`opposite-sex`、`non-kin`） |
| `I-C9` | `VERIFIED` | VERIFIED（`A03` 对，`17` 错） | L1-003、L2-003 \ | NO | I-C7 | Magi（`L1-003` / Fixture 002）**不**覆盖 `unilateral attraction |
| `I-C10` | `PLAUSIBLE` | PLAUSIBLE | YES — 与 `I-C7` 同处（§15 Gate B 需定义每个 cell ~ | INDEPENDENT | HOLD_FOR_EVIDENCE**（先定义 cell 判据，再重数；不要在定义前把 5 或 6 当定论） | caregiving` 与 `high-attraction/low-trust` 两个 cell 的覆盖被两份报告都判为 0，实际应为 partial / 0 |
| `I-C11` | `VERIFIED` | VERIFIED | NO（诊断性陈述） | INDEPENDENT（`17`/`A03` 均未查 fixture~ | RECLASSIFY_AS_METHOD_LIMIT | Gate B 零覆盖 cell 的**成因**部分来自 rights/access 约束，不是 curation 缺陷 |
| `I-C12` | `VERIFIED` | VERIFIED | YES** — `docs/validation/VALIDATION_CORP~ | INDEPENDENT | ACCEPT | VALIDATION_CORPUS_V0_1.md` 的「Recommended Fixture 001–003」已被实际冻结的三个 fixture 取代，canonical 内部存在**未更新的文档级冲突 |
| `I-C13` | `VERIFIED` | VERIFIED | NO（若要补，只需在 `17` 加一句 temp 目录声明；**但 `17` 是~ | INDEPENDENT（我自己做的 git + SHA + grep~ | ACCEPT_AS_PROPOSAL**（独立性成立，登记 temp 目录为**未声明的暴露面**；不构成污染证据） | 17` §0 独立性声明为真（Git 层与内容层均通过核查） |
| `I-C14` | `VERIFIED` | VERIFIED | NO | INDEPENDENT | HOLD_FOR_EVIDENCE**（`17` 的 12 条 `CHALLENGED` 中，至少 A2/A4/A5/A~ | 17` 的 S 编号体系（`S1`…`S29`）无法从其 §12 引用清单解析 |
| `I-C15` | `VERIFIED` | VERIFIED | NO | INDEPENDENT | RECLASSIFY_AS_METHOD_LIMIT | 17` §4 表实际裁定分布是 `CHALLENGED 12 / CONTESTED 6 / UNCHALLENGED 3 / NO_EVIDENCE 2 |
| `I-C16` | `VERIFIED` | VERIFIED**（3 条）/ **NOT_OPENED**（2 条） | NO | INDEPENDENT | ACCEPT_AS_PROPOSAL | 17` F2 的五条 Joel et al. (2020) 结论 |
| `I-C17` | `WRONG-SCOPE` | WRONG-SCOPE | YES** — `PARAMETER_CONVERGENCE` §5 B1（PP~ | INDEPENDENT | RECLASSIFY_AS_METHOD_LIMIT**（把「层被反向排序」降为**待检验的竞争假说**；`A03` 改~ | 17` F3：**LHRM 的层边界被经验文献反向排序**（PPR 应升为一等状态层 / Satisfaction 不应是 Derived） |
| `I-C18` | `PLAUSIBLE` | PLAUSIBLE | NO | INDEPENDENT | ACCEPT_AS_PROPOSAL**（保留结论，补上桥接假设） | 17` F7：基于文本的 benchmark 可取得 100% 映射覆盖率而与驱动现场行为的层完全无关 |
| `I-C19` | `UNSUPPORTED` | UNSUPPORTED**（就其结论链而言） | YES** — 若要保留「需模态层」这一主张，canonical 必须接受 la~ | INDEPENDENT | REJECT**（作为架构主张）；真实的现象改写为 Gate C 冗余条目 + 已有 Observation/Belie~ | 17` F4：复合态无法由「每构念一个坐标」表达，状态空间必须增加模态/析取层 |
| `I-C20` | `MIXED:VERIFIED+PLAUSIBLE` | VERIFIED**（引文）/ **PLAUSIBLE**（推论） | NO | INDEPENDENT | ACCEPT_AS_PROPOSAL | 17` F5a：一致性项在 actor/partner 主效应之外携带额外方差 |
| `I-C21` | `VERIFIED` | VERIFIED — 且为本报告最诚实的一处 | NO | INDEPENDENT | ACCEPT | 17` §9 item 14：Le & Agnew (2003) 自身同时说「moderators vary minimally」与「significantly stronger in relational domains」 |
| `I-C22` | `VERIFIED` | VERIFIED | NO | INDEPENDENT | ACCEPT_AS_PROPOSAL**（作为 `17` T1 的证据升级） | Le & Agnew (2003) 报告 IM 三分量解释 commitment 约 **2/3** 方差 |
| `I-C23` | `VERIFIED` | VERIFIED**（逻辑）；`NOT_OPENED`（D7 的最终处置需 sibling 报告） | YES — §4 D7 或 §9 R3 二选一 | INDEPENDENT | ACCEPT_AS_PROPOSAL | 17` T1 + F3/A21 合起来蕴含一个 `17` 自己没看见的二选一**：若 Dedication 由 (satisfaction, alternatives, investment) 决定，则 §4 D7（primitive）与 §9 R3（Satisfaction=DERIVED）不能同时成立 |
| `I-C24` | `VERIFIED` | VERIFIED | NO（流程） | INDEPENDENT | ACCEPT_AS_PROPOSAL**（采纳 `A03` H-10 的补充限定） | 17` A22 / F9(3)：Fixture 输入与 ontology 有共同作者 |
| `I-C25` | `PLAUSIBLE` | PLAUSIBLE**（设计异味成立），但取证偏重 | NO | INDEPENDENT | RECLASSIFY_AS_METHOD_LIMIT | 17` T5：`CONSTRUCT_SCOPE_DIRECTIONALITY` §1 的加性分解把跨时间常数/trait 静默导入时间索引状态 |
| `I-C26` | `PLAUSIBLE` | PLAUSIBLE**（我无法复现其 `Compare-Object`，但发现覆盖缺口） | NO | INDEPENDENT（我独立枚举了 temp 目录） | ACCEPT_AS_PROPOSAL**（结论方向很可能对，但必须补 R04/R10 才能称「Wave 1 全覆盖」） | A03` §4.4「writeback 阶段不存在判据弱化」这条机器可核否定结果 |
| `I-C27` | `VERIFIED` | VERIFIED**（就仓内证据而言） | NO | INDEPENDENT | ACCEPT_AS_PROPOSAL**（并把范围更正为「三份全部」，成因分两类） | A03` H-3：`SPAN_SUPPORT_RATE` / `ENTITY_INSERTION_RATE` 在 Fixture 003 上永久不可计算 |
| `I-C28` | `VERIFIED` | VERIFIED | YES** — `docs/validation/VALIDATION_CORP~ | INDEPENDENT | ACCEPT | A03` §4.1：`future_leakage_risk` 把「文档内/结局泄漏」与「预训练记忆泄漏」合并为一列，互相遮蔽 |
| `I-C29` | `PLAUSIBLE` | PLAUSIBLE**（5 条可触发 / 1 条不可判定） | 部分（见 `needs_experiment_or_data`） | ACCEPT_AS_PROPOSAL**（R1 与 R5 优先；R2~ |  | 17` §5 的 R1–R6 是否可触发 |
| `I-C30` | `VERIFIED` | VERIFIED | NO | INDEPENDENT | RECLASSIFY_AS_METHOD_LIMIT | 17` §12 line 549 的「所有卷期页均经 Crossref API 核验」这一**总括声明**不成立 |

## 2.J — lane `J`（citation / provenance recheck）

| claim_id | primary | verdict（原文） | canon | corroboration | recommendation | claim（截断） |
|---|---|---|---|---|---|---|
| `J-C1` | `VERIFIED` | VERIFIED | NO |  | ACCEPT | A01：353 DOI 中 337（95.5%）Crossref 解析成功 |
| `J-C2` | `VERIFIED` | VERIFIED | NO |  | ACCEPT | A01：29 个 DOI「解析到一篇真实论文但不是所引那一篇」 |
| `J-C3` | `VERIFIED` | VERIFIED | NO |  | ACCEPT | A04：1,199 → 642 → 533，倍率 2.25× |
| `J-C4` | `WRONG-SCOPE` | WRONG-SCOPE | NO`（但 manifest §4 B-9 需改数字） |  | RECLASSIFY_AS_METHOD_LIMIT | A04：各 lane 自报数相加 ≈1,201，"高估 2.3–3.4×" |
| `J-C5` | `VERIFIED` | VERIFIED | NO |  | ACCEPT | A04：5 种 DOI 书写形态、2.18 次/DOI |
| `J-C6` | `MIXED:VERIFIED+WRONG-SCOPE` | VERIFIED`（作为"peer-reviewed 计数"）/ `WRONG-SCOPE`（作为"科学重量"） | NO |  | RECLASSIFY_AS_METHOD_LIMIT | A04：350 个同行评审来源 |
| `J-C7` | `UNSUPPORTED` | UNSUPPORTED | NO |  | REJECT | A04：承重表 30 项"28 项强度充分" |
| `J-C8` | `UNSUPPORTED` | UNSUPPORTED | NO |  | REJECT | A04：「3 处 `10.31234/osf.io/…` 前缀结构非法、不解析」 |
| `J-C9` | `CONTESTED` | CONTESTED | `YES`（见 `00_MANIFEST.md` §2b） |  | ACCEPT | 修复 child 拒绝 `10.31234→10.31219`，理由「10.31234 解析、10.31219 404」——`EV2` 实测相反，且两个前缀同属 COS |
| `J-C10` | `VERIFIED` | VERIFIED`（窄） | NO |  | ACCEPT_AS_PROPOSAL | A04：无 meta-analysis 承担当需 primary data 的主张 |
| `J-C11` | `VERIFIED` | VERIFIED`（计数）/ 我的裁定见 §9.5 | NO |  | RECLASSIFY_AS_METHOD_LIMIT | A01：12 个证据等级词表变体 / 18 lane |
| `J-C12` | `VERIFIED` | VERIFIED | NO |  | ACCEPT | 修复正确性：9 条 applied repair |
| `J-C13` | `UNSUPPORTED` | UNSUPPORTED | NO`（报告内订正即可） |  | REJECT | A01 §1.1 L34「Crossref 解析 353/353（100%）」 |
| `J-C14` | `UNSUPPORTED` | UNSUPPORTED | NO |  | REJECT | A04 D5：`10.1024/1662-9647.a000031` 的问题是「前缀与著录期刊族不一致」 |
| `J-C15` | `UNSUPPORTED` | UNSUPPORTED | NO |  | REJECT | A04 §3.3.4「`10.1037/h0046049` Cartwright & Harary 1956, *Psych Review* 63(4)」判 ✅ 一致 |
| `J-C16` | `VERIFIED` | VERIFIED | NO |  | ACCEPT | Fixture 003 存在 `pointer_only` / `ai-train=no` / `GPTBot Disallow` 边界 |
| `J-C17` | `CONTESTED` | CONTESTED`（**我无权裁定**） | NO |  | HOLD_FOR_EVIDENCE | A04 §6.3 F1：`13` 全篇 0 次记录该边界却用其 transcript 单元 |
| `J-C18` | `VERIFIED` | VERIFIED | NO |  | ACCEPT | A04 的 642 行来源表结构上无法发现作者错配 |
| `J-C19` | `VERIFIED` | VERIFIED | NO |  | ACCEPT_AS_PROPOSAL | A01 83 条 `NARROW_REPAIR_REQUEST` 只执行了约 13 条 |
| `J-C20` | `UNSUPPORTED` | UNSUPPORTED | NO |  | ACCEPT | 00_MANIFEST.md` §2b 称 `08b` 修了"7 处" |
| `J-C21` | `UNSUPPORTED` | UNSUPPORTED | UNSURE |  | HOLD_FOR_EVIDENCE | 00_MANIFEST.md` §2b 称 `08b [S15]`「只改作者，未改年份」 |
| `J-C22` | `PLAUSIBLE` | PLAUSIBLE | NO |  | ACCEPT_AS_PROPOSAL | 两个审计的抽样是否偏倚 / 覆盖是否已知 |
| `J-C23` | `VERIFIED` | VERIFIED`（对我自己的抽样） | NO |  | ACCEPT | PR #31 的实际引用可靠性 |

## 2.K — lane `K`（cross-lane contradiction map）

| claim_id | primary | verdict（原文） | canon | corroboration | recommendation | claim（截断） |
|---|---|---|---|---|---|---|
| `K-C1` | `PLAUSIBLE` | PLAUSIBLE | NO | INDEPENDENT`（我重跑了扫描） | HOLD_FOR_EVIDENCE` — 要求 `18` 补一个可复现的扫描协议，并把结论改写为「Wave 1 内 17~ | 18` CF-00 的 sibling 引用数字在 durable 文本上不可复现，且系统性低报；但「17 独立单点 + 1 join lane」的**定性**结论成立 |
| `K-C2` | `WRONG-SCOPE` | WRONG-SCOPE | NO | INDEPENDENT | RECLASSIFY_AS_METHOD_LIMIT` — 改称「2 种层位处置互斥 + 1 条判据前提 + 1 张待修~ | 「`PPR` 三方互斥」在**形态**上不精确：`18` 列的 4 个 lane 里只有 2 个给出本体层位主张；R06 给的是 **null 判据的前提**，R14 给的是**优先级表条目**，二者都不是「层位处置」 |
| `K-C3` | `UNSUPPORTED` | UNSUPPORTED`（对 `18` 的完备性） | NO（但若采纳 R17，`PARAMETER_CONVERGENCE` §5 `~ | R11/R03 = `UNKNOWN`（grep 命中，未读上下文）~ | ACCEPT` — 要求 `18` 补齐这 5 行并把「三方互斥」改为逐 lane 枚举 | CF-03 **漏了 5 个触碰 `PPR` 层位的 lane**，其中 **R11 与 R03 独立支持 R01 的 `BELIEF_ONLY`**，R00 记录了 **canonical 内部自身**的分歧 |
| `K-C4` | `CONTESTED` | CONTESTED | NO | R10 = `INDEPENDENT`（R10 未读 R06 律 E~ | HOLD_FOR_EVIDENCE` — 并指出 `18` 的 **N-09 归因错误**：它把冲突归给 `R10 Ex~ | 新冲突（`18` 漏）**：`R10 G15` 判 accommodation / 克制过程及其恢复分叉是 **construct hole，「不可由瞬时状态表示」，应为 `Action/Event` 的结构化轨迹**；而 `R06` 律 E（`RT`）的核心主张是**存在一条状态级的抑制/修复分支 `Λ⁻`，其分支由 dyadic state 决定**。若 accommodation 确实只能是 Action/Event 轨迹，则 `Λ⁻` 分支**没有它所条件化的那个 state 通道 |
| `K-C5` | `CONTESTED` | CONTESTED | NO | SAME_SOURCE` 风险高：两者谈的是同一现象，但 `R06`~ | HOLD_FOR_EVIDENCE` — 要求把「`R06` 的 `RT` 经验支点是否可被 `R10` 的 `UNKN~ | 新冲突（`18` 漏）**：对**同一批文献**（demand–withdraw pattern）两条 lane 给出**不相容的证据地位**。`R06 §8` 判该模式族 `SUPPORTED`，并给出 Schrodt 2014「74 研究 / N = 14,255」+ 6 个 r 值；`R10 G16` 判同一现象是 **construct hole**，且其「关键引用」列写的是「**—（本 lane 未找到强引用，标 `UNKNOWN_AS_OF`）**」 |
| `K-C6` | `CONTESTED` | CONTESTED | NO | TRANSITIVE` 风险：`R10` 未读 `R06` §8.6 | RECLASSIFY_AS_METHOD_LIMIT` — 这是「lane 未互读导致的事实错误」，不是 ontolog~ | 新（`18` 漏）**：`R10 G16` 含一条关于 **`R06` 产出**的事实断言（「需 dyad 级记录，但 **R06 未提供**」），该断言与 `R06 §8.6` 的 durable 正文**直接矛盾 |
| `K-C7` | `UNSUPPORTED` | UNSUPPORTED`（对「五」） | YES（若采纳 `19` WO-N3：`AGENTS.md` + `CURREN~ | SAME_SOURCE`：`UNKNOWN_AS_OF` 是各 la~ | ACCEPT` — 改述为「**至少六套**，其中 `UNKNOWN_AS_OF` 覆盖 6 条 Wave 1 lane~ | 新（`18` + `19` 双漏）**：「`Unknown` 值类被**五**个 lane 各自重新发明」中的计数**偏低**。语料中至少存在**第 6 套**「无值」词表 `UNKNOWN_AS_OF` / `DOI_UNKNOWN_AS_OF_2026-09-27`，且它是**全语料使用最广**的一套 |
| `K-C8` | `WRONG-SCOPE` | WRONG-SCOPE | 同上 | INDEPENDENT`（我同时实读了两侧一手定义） | ACCEPT_AS_PROPOSAL` — 把 N-01 改写为**两轴合并**：`tag`（证据侧，R07 的 10 ~ | 18` N-01 的 SSOT 修法（把五套映射成 R07 §9.3 tag 集的子集）**在类型上不完整**：`R15` 的 `MAPPING_FAILURE` 是**表示失败**而非证据状态，`18` 自己已指出「它在 R07 的 tag 集合里**没有对应值**」，却仍把修法定为「映射到 tag 集的子集」 |
| `K-C9` | `WRONG-SCOPE` | WRONG-SCOPE | NO | R02 与 R10 引同一 DOI = `SAME_SOURCE`（~ | RECLASSIFY_AS_METHOD_LIMIT` — 把「同一个经验结论」改为「同一来源的**两个不同**读法，落~ | 18` CF-08 的核心叙述「R02 与 R10 引**同一篇** Overall & Hammond 2026，得出**同一个经验结论**」**不成立**：`R02` 读出的结论与 `R10 G6` 的结论**不是同一件事**；且两个具体数字（`70–75%`、`actor/partner 正相关`）**不在 Crossref abstract 中 |
| `K-C10` | `WRONG-SCOPE` | WRONG-SCOPE | NO | SAME_SOURCE`（N=443 只出现在 R10；`A01:2~ | RECLASSIFY_AS_METHOD_LIMIT | 18` N-08 的措辞「唯一有**直接判别实验**支持的 pair-level 涌现候选」是 **WRONG-SCOPE**：Bodenmann 2011 的判别发生在**操作化层**，不在**本体层 |
| `K-C11` | `UNSUPPORTED` | UNSUPPORTED | NO | INDEPENDENT | ACCEPT` — 要求 `18` 补一张 `CR-/NR-` 对照表，或把 §10 的理由码改指 `CF-xx`/`U~ | 18` 使用了**两个从未定义的编码命名空间** `CR-x` 与 `NR-x`；`CR-1/3/4/6/7/8` + `NR-1/8` 共 8 个码在 `18` 自身没有登记表，其中 5 个被 §10 的 `NARROW_REPAIR_REQUEST` 当作**理由码**引用 |
| `K-C12` | `NOT_ENUM` | R06\ | pairfam\ | APES\ | DVA\ | 19:353` 的方法学缺口第 3 条是错的**：`02b`（R02）**零**引用 `R04`/`R06`。它唯一的类 lane 字符串是自身 §6 残余表里的 `R1`–`R11` id |
| `K-C12b` | `CONTESTED` | CONTESTED | NO | TRANSITIVE`：`R06` → `R02` 是**单向**读~ | ACCEPT_AS_PROPOSAL` — 建议 `18` 在 CF-01 下补一行「依赖链」；建议 `19:353` ~ | 真正的、未被覆盖的依赖链是 `R06 → R02`（方向与 `19` 所述相反）**：`R06` 的律 B `APES` 表格里 `Dedication` 那一列的支撑直接写「**见 R02 裁决**」，且 `R06` 建议「**R02 优先裁决**『判 E 若成立应删除 `Dedication`』」；而 `R02` 的 `H2` 判 `Dedication ↔ Satisfaction` 双计为 `CRITICAL` — `R06` 从未读过 `H2 |
| `K-C31` | `UNSUPPORTED` | UNSUPPORTED`（对 `18` 的完备性） | NO | INDEPENDENT | ACCEPT` — 要求 `18` 补一节「否定型声明 vs 他 lane 的加法提案」，这是当前最大的冲突面空白 | 18` 的冲突面**系统性遗漏了「否定型」声明**：R10 §8 的 **16 条缺口登记**（含 **8 条 `construct hole`**、2 条 `ontology hole`、1 条 `projection hole`）是全语料最大的单张「不该加什么」清单，而 `18` 全文 grep `construct hole` / `UNKNOWN_AS_OF` / `G16` = **0 命中 |
| `K-C15` | `NOT_ENUM` |  |  |  |  |  |
| `K-C16` | `NOT_ENUM` |  |  |  |  |  |
| `K-C17` | `NOT_ENUM` |  |  |  |  |  |
| `K-C18` | `NOT_ENUM` |  |  |  |  |  |
| `K-C19` | `NOT_ENUM` |  |  |  |  |  |
| `K-C20` | `NOT_ENUM` |  |  |  |  |  |
| `K-C21` | `NOT_ENUM` |  |  |  |  |  |
| `K-C22` | `NOT_ENUM` |  |  |  |  |  |
| `K-C23` | `NOT_ENUM` |  |  |  |  |  |
| `K-C24` | `NOT_ENUM` |  |  |  |  |  |
| `K-C25` | `NOT_ENUM` |  |  |  |  |  |
| `K-C26` | `NOT_ENUM` |  |  |  |  |  |
| `K-C27` | `NOT_ENUM` |  |  |  |  |  |
| `K-C28` | `NOT_ENUM` |  |  |  |  |  |
| `K-C32` | `NOT_ENUM` |  |  |  |  |  |
| `K-C29` | `NOT_ENUM` |  |  |  |  |  |
| `K-C33` | `NOT_ENUM` | ACCEPT | NO | INDEPENDENT`（我对 5 条的机制与 null 集合作了逐~ |  | 19` §4 的 **5 条律是 5 个真正不同的机制族，不是同一机制的 5 种说法 |
| `K-C34` | `WRONG-SCOPE` | WRONG-SCOPE | NO | SAME_SOURCE`（我对 `18` 与 `19` 做了交叉比对~ |  | 19` §4 **未交叉引用** `18` §5.2/§5.3：按 `18` 的可组合性检查，**5 条律中至少 2 条（L1=`律A BMR` 经 U-1/U-2、L5=`律E RT` 经 U-3）的判别部分在当前数据下不可执行**，而 `19` 把它们列为「值得以后冻结」且未加任何限定 |
| `K-C35` | `CONTESTED` | CONTESTED | NO | SAME_SOURCE`（L1 与 C-1 引同一批 Laurenc~ |  | 19` 的 **L1 与 C-1 不是两个独立决定**：L1 `BMR` 的关键支持是 Laurenceau 1998/2005「PPR 为部分中介」，而 `C-1` 正在裁决 PPR 是否属于 Belief 层。若 C-1 判 R06 §4.9 的 B4 null 成立（`Z` 与 `PPR` 是同一测量，应**合并**），则 L1 的经验支点被吸收 |
| `K-C36` | `NOT_ENUM` |  |  |  |  |  |
| `K-C37` | `NOT_ENUM` |  |  |  |  |  |
| `K-C38` | `NOT_ENUM` |  |  |  |  |  |
| `K-C39` | `NOT_ENUM` |  |  |  |  |  |
| `K-C40` | `NOT_ENUM` |  |  |  |  |  |
| `K-C41` | `NOT_ENUM` |  |  |  |  |  |
| `K-C42` | `NOT_ENUM` |  |  |  |  |  |
| `K-C43` | `NOT_ENUM` |  |  |  |  |  |
| `K-C44` | `WRONG-SCOPE` | WRONG-SCOPE | — | INDEPENDENT`（我读了 `19` §7 全部 8 条的变更~ |  | 19` §7 抬头「**全部**为 AI 推荐…**均**不属本 Work Order 授权范围，需 Human 授权后另行派发」把**两种不同性质**的批准混为一谈：**(a) 因 canonical mutation 需 Human 主权批准**（N1 / N2 / N3 / N4-冻结部分）与 **(b) 仅因 Work Order 边界而需新派发**（N5-前半 / N6 / N7 / N8） |
| `K-C45` | `UNSUPPORTED` | UNSUPPORTED`（对自报依据） | NO | INDEPENDENT |  | 19` §7 自报排序依据是「**修起来便宜 / 收益大**」，但实际排序（canonical 最贵的 N1 打头，最便宜的 N8 垫底）遵循的是**架构依赖**，不是成本/收益 |
| `K-C46` | `WRONG-SCOPE` | WRONG-SCOPE | NO | INDEPENDENT |  | 19` 称 WO-N1 是「**唯一的真正阻塞项**」，这个断言**过强**：它把三种不同的「阻塞」压成一种 — N1 阻塞**验证程序整体**（门不能失败）；N2/N3 阻塞**内容**（层归属与值类未定，则新能失败的门是在测一个未定 schema）；N6 阻塞**经验接入 |
| `K-C47` | `NOT_ENUM` |  |  |  |  |  |
| `K-C48` | `NOT_ENUM` |  |  |  |  |  |
| `K-C49` | `NOT_ENUM` |  |  |  |  |  |
| `K-C50` | `NOT_ENUM` |  |  |  |  |  |
| `K-C51` | `VERIFIED` | VERIFIED |  | INDEPENDENT` — R07 与 R15 的 siblin~ |  |  |
| `K-C52` | `VERIFIED` | VERIFIED |  | TRANSITIVE`**（R03 → R11 的**显式交接**，~ |  |  |

## 2.L — lane `L`（actionability / next-work-order filter）

| claim_id | primary | verdict（原文） | canon | corroboration | recommendation | claim（截断） |
|---|---|---|---|---|---|---|
| `L-C1` | `VERIFIED` | VERIFIED`（对本 lane 的结构判定）；被 relay 的 A03 归因标 `RELAYED_NOT_INDEPENDENT | YES` — `docs/foundation/PARAMETER_CONVER~ |  | ACCEPT_AS_PROPOSAL`（先出 patch，后派工） | 让验证门「能失败」的缺陷位于 `PARAMETER_CONVERGENCE_V0_1.md` §15 Gate A（`通过` 从未定义），而 `19`/A03 给出的修复动作只改 §13 与 §2.6，不改 §15 ⇒ 按 WO-N1 执行后 Gate A 仍无判定规则。 |
| `L-C2` | `VERIFIED` | VERIFIED | YES` — 追加 `AGENTS.md`（Validation discipl~ |  | ACCEPT`（把变更面从 1 文件扩到 4 文件 + 1 fixture；这是 WO-N1 能否达成其自陈目标的**必~ | 即使按 WO-N1 删掉 §13 的 3 个 catch-all，`MAPPING_FAILURE` 仍类型上可达不到，因为同一出口还写在 `AGENTS.md:62`、`README.md:113`、以及 **Fixture 003 自己的 verdict 枚举**里。 |
| `L-C3` | `WRONG-SCOPE` | WRONG-SCOPE | NO`（这是 `19` 的表述问题，不是 canonical 问题） |  | REJECT`（按原措辞）；可辩护的改写：「**8 项 basis 在已执行的 gate 下从未被删减过一条**；项目历~ | 19`（L32、L103）转述的「`MERGE` 与 `REJECT` **从未被签发过一次** ⇒ 8 项 candidate basis 单调增长」在项目记录层面**为假**：`PARAMETER_CONVERGENCE_V0_1.md` §9 R4 / R5 已对具名 candidate 签发过 `REJECT`。 |
| `L-C4` | `VERIFIED` | VERIFIED`（结构判定由我自查）；A03 的 8/11 数字标 `RELAYED_NOT_INDEPENDENT | NO`（诊断本身不改文件；其后果指向 L-C5/L-C6） |  | ACCEPT`（作为**判别力缺陷**接受；即 Gate B 通过不构成跨域稳定性证据—`19` 已如此表述，正确） | 19` §1 A12 / R17 A6 的核心指控「Gate B 的反例清单 = 项目自己的假设列表」在结构上成立，且比 A03 转述的 8/11 更整齐。 |
| `L-C5` | `NOT_ENUM` | REPRODUCED_BY_ME`（复算自 canonical corpus）；claim 归属 `RELAYED_NOT_INDEPENDENT`（我没读 A03/R11） | NO |  | ACCEPT`（并把「5 类零覆盖」的口径写进决策文件：按 `core_dyad` 计） | 12 份语料对 `same-sex / kin / 非浪漫友谊 / caregiving / high-dependence-low-liking` 零 core-dyadic 覆盖—我在 corpus 文档的 12 个 `core_dyad` 字段上逐条复算，得到同一集合。 |
| `L-C6` | `WRONG-SCOPE` | WRONG-SCOPE`（对 `19` 的呈现方式） | YES`，但**极小**：`PARAMETER_CONVERGENCE_V0_1~ |  | RECLASSIFY_AS_METHOD_LIMIT` → 不，`19` 侧应 `ACCEPT` 但**重述为文档一致性~ | 19` §1 A12 把「Gate B 清单不含 sibling / parent–adult-child / ex-partner / professional / adversarial」呈现为覆盖缺口，但 `CURRENT_ARCHITECTURE.md` §2 已把这 5 类**逐一列为在域**；因此缺的是**测试清单**，不是**研究域**。 |
| `L-C7` | `VERIFIED` | VERIFIED | NO`（本条是成本更正） |  | ACCEPT`（`19` 必须在每个 WO 上区分「改文档的成本」与「得到一次运行结果的成本」；后者 = 3 次隔离派发~ | lhrm` 仓库只有 `AGENTS.md`、`README.md`、`docs/`；无 runner、无 CI、无 metric 实现、无 schema 文件。`19` §7 的排序依据「修起来便宜」对文档编辑成立，对「重跑 Fixture 001」不成立。 |
| `L-C8` | `VERIFIED` | VERIFIED | NO`（本条） |  | HOLD_FOR_EVIDENCE`（先解 B-5；`19` 的「前提：WO-N1 必须先完成」是必要但**不充分**条~ | WO-N7「把 3 份已冻结 fixture 跑一遍 LHRM 映射」与冻结 substrate 自带的验证协议冲突：fixture 明确要求 3 个独立 Verifier 消费同一 `main` 合并后的 exact file 版本，并指定验证 lane = `#20/#21/#22`；而 `#20/#21/#22` 按隔离契约本 attempt 不查、状态 UNKNOWN（B-5）。 |
| `L-C9` | `VERIFIED` | VERIFIED | NO |  | ACCEPT`（`19` 的 N1→N7 顺序**正确**；补一句 pin 后果即可，成本为零、价值明确） | Fixture 003 把验证 schema 钉在 `f237784`（`CURRENT_ARCHITECTURE + PARAMETER_CONVERGENCE + CONSTRUCT_SCOPE_DIRECTIONALITY @ f237784`）。因此 WO-N1 一旦落地，**所有在改动前产出的 mapping 计数都不可与之后的结果比较**。 |
| `L-C10` | `VERIFIED` | VERIFIED | NO`（是 Human 权利裁决） |  | HOLD_FOR_EVIDENCE`（001/002 可跑；003 需 Human 权利决定 + canonical U~ | WO-N7 写「3 份已冻结 fixture」；其中 Fixture 003（StoryCorps）带 `rights_policy=HUMAN_REVIEW_REQUIRED`、Eye 侧 `POINTER_HASH_ONLY` fail-closed、`robots.txt` `Content-Signal: ai-train=no` + `Disallow` GPTBot/ClaudeBot/CCBot，且其 canonical 页 URL 在 2026-09-14 实测 **404**。~ |
| `L-C11` | `CONTESTED` | CONTESTED`（对 relayed 建议提出反证；反证方 = 我对冻结 substrate 的直接读取） | NO |  | HOLD_FOR_EVIDENCE`（要求 `19`/R17 明确 WO-N1 的被检验对象是「事实态分离」还是「构念覆~ | Fixture 001 的 core dyad 是**雇主↔雇员**（`Miss Z. Carty <-> her 2020 line manager`），其 26 个原子事实是排班/停业/未付薪/CAB/申诉等**机构性事实**。用它检验 8 维 basis（Liking/RomanticAttraction/SexualDesire/Trust/AttachmentSecurity/Caregiving/Dedication/OutcomeDependence）大概率落到两种退化之一：几乎全~ |
| `L-C12` | `WRONG-SCOPE` | WRONG-SCOPE`（`19` 用「12 份」作分母偏大） | NO |  | RECLASSIFY_AS_METHOD_LIMIT`（「12 份语料」应改述为「12 份**已 harvest 未 m~ | 19` 与 A03 把「12 份语料」当作 Gate B 的既有语料面；实际 12 份中仅 2 份 `direct-use`，10 份 `needs cleaning`，且 corpus 作者自己写明 L2/L3 `deliberately deferred until Verifier protocol is frozen`。 |
| `L-C13` | `VERIFIED` | VERIFIED`（可行性层）；access status 与 rights 细节 `RELAYED_NOT_INDEPENDENT`（我未联网核实任何数据集） | NO`（但需要一次 **Human 决策**：数据落在哪、是否入库、许可/署名政~ |  | RECLASSIFY_AS_METHOD_LIMIT`（WO-N6 → 拆为「基础设施请求（egress）」+「数据存储~ | 19` §5 的 8 个数据集中，只有 D04（Fisman & Iyengar speed dating，标「完全公开，2026-09-27 HEAD 200」）在权利上今天可达；但它只有单一时点（不能支撑任何转移律），且本仓库**没有 data 面**（无 `data/` 目录）、当前 Work Order 的变更面仅限 `docs/research/overnight-2026-09-27/` ⇒ 即使 D04 也被**存储决策**阻塞。WO-N6 的三项核实（pairfam / SHAR~ |
| `L-C14` | `PLAUSIBLE` | PLAUSIBLE`（缺口 = 我未联网核实任何 CoU/许可原文；缺口 = D01 user contract 的 LLM 条款在 `19` 中未被记载） | NO`（本条是数据可得性） |  | HOLD_FOR_EVIDENCE`（`19` §4 把「冻结需 Human 授权的独立 Work Order」写成主要~ | L1/L2/L4/L5 需要同一 dyad 上**双方报告 + 至少两个时点**的合法数据。`19` §5 表内：满足双报告多波的只有 D01（pairfam）与 D02（SHARE），而 D02 的 CoU §7 明文禁 LLM 处理个体级数据、D01 需 user contract（其是否允许 LLM 处理，`19` 未记载）、D03 在本环境 403、D04 无第二时点、D05 单轮、D06 跨波 partner id 未核实、D07 配偶关系质量单方报告、D08 会员限定。⇒ **没有任~ |
| `L-C15` | `VERIFIED` | VERIFIED`（`19` 内部自洽性） | NO |  | REJECT`（对 L3/L5 的「candidate」身份）；改为 `NEGATIVE_RESULT` 记录：L3 →~ | 19` §4 自己在 L3 行写「**最佳可得证据逆向于本律的增量通道**。冻结前必须先解释这一冲突」，在 L5 行的证伪判据列写「性别不对称的耦合被检出（**当前最佳证据反对**）⇒ 律族须重写」。一条已触发自身 kill criterion 的律不是 candidate law。 |
| `L-C16` | `MIXED:UNSUPPORTED+VERIFIED` | UNSUPPORTED`（作为「需要 Architect 决策的发现」）；作为「外部文献与既有裁决一致」则 `VERIFIED`（我核对了词表与条文） | NO |  | REJECT`（不占用 Architect 决策；可作为「已决事项的外部佐证」归档） | 19` §1 A11（「爱/亲密/嫉妒/忠诚 不宜作 primitive 这一立场不能作为本项目的发现」）在 LHRM 内部**没有任何决策后果**，因为该裁决已是 `PARAMETER_CONVERGENCE_V0_1.md` §12 的现行条文，且词表逐条相同。 |
| `L-C17` | `VERIFIED` | VERIFIED | NO |  | ACCEPT`（要求 `19` 区分「阻塞证据生产」与「阻塞推导」，并据此重排） | 19` §7 优先级 1 写「**这是唯一的真正阻塞项**」；但 §2 把 C-1（PPR 层）、C-2（OutcomeDependence ontology）、C-3（Gate 可证伪性）、C-4（Unknown 类型学）四项标为「（阻塞级）」，C-5 标为「（排序死锁）」。 |
| `L-C18` | `VERIFIED` | VERIFIED | NO |  | ACCEPT`（parent join 时必须产出一份**单一、编号不冲突**的 blocker register，并把~ | 19` §8 有 **B-1…B-8**（8 项）；`00_MANIFEST.md` §4 有 **B-1…B-9**（9 项）；两者对 **B-3** 指不同事物；且 manifest 自身对「全局去重」同时使用 **B-3**（§4）与 **B-9**（§4 末）两个编号。 |
| `L-C19` | `PLAUSIBLE` | PLAUSIBLE`（披露**充分性**的判断本身带主观性；缺口 = 我未读 A01/A04 报告，无法核对其断言原貌） | NO |  | ACCEPT`（要求 parent 在 join writeback 中加一列 `finding_id → affect~ | manifest §2b 对「A04 的 OSF 前缀断言被实测推翻」的处理是本 attempt 里质量最高的记录（测了什么、结果、未应用、规则沉淀齐全），足以为「审计断言必须独立实测」背书。仍缺三件事。 |
| `L-C20` | `CONTESTED` | CONTESTED`（对「该 prior art 检索未命中」这一 relayed 结论） | NO |  | REJECT`（作为 Work Order）；改为一次 bibliographic check，**先修引文，再检索**~ | WO-N8 要求核实 `Acitelli & Antonioni (2006)` 与 `Boyd & Heewer (2007)`。后者极可能是 **Boyd & Hilton (2007), *The law of the wed: A lateral theory of marriage*, Cognition**（Heewer 是第三作者）。若如此，WO-N8 自己的前提引文就带一处与它要复核的 prior art 同类的作者错误—而本次 attempt 恰恰在 5 处修过同类错误。 |

