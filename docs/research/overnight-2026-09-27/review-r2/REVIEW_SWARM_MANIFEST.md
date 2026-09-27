# REVIEW_SWARM_MANIFEST — Round 2 Review Swarm over `youling/lhrm#31`

> 本文件是 Round 2 review swarm 的**唯一入口**。它记录：被审对象、swarm 构成、独立性台账、join 规程、
> 本轮对 PR #31 durable 文本所作的**记账更正**、以及本轮**没有**做的事。
>
> **本 swarm 是审计，不是研究。** 目标是把 PR #31 的既有研究结果分块判定成可提交 Architect 审议的 verdict，
> **不产出任何新文献调研，不修改任何被审文件，不实施任何 Work Order。**

---

## 1. 被审对象与不变式

| 项 | 值 |
|---|---|
| PR | `youling/lhrm#31`（`open`，**未 merge**） |
| 被审 head | `8adcf0bacc45c0feb5c14e65e2a45346dd488b43` |
| base | `main` @ `ee393ca24f9fbf738ac0ed839e99bdc99de6fc3a` |
| 体量 | 25 files / +15,744 / -0，全部位于 `docs/research/overnight-2026-09-27/` |
| 上一轮终端指针 | `AGENT_CLAIMED` `issues/30#issuecomment-5850793190` · `CP2` `#issuecomment-5851651404` · `AGENT_TERMINAL_RESULT` `#issuecomment-5851720786` |
| 本轮 review branch | `review/overnight-2026-09-27-r2`（从被审 head 派生，**PR #31 的 branch 与 head 未被本轮触碰**） |
| 治理来源 | `youling/ai-use@AGENTS.md` (L0, `64018d80`) · `youling/lhrm@AGENTS.md` · `docs/research/overnight-2026-09-27/review-r2/REVIEW_CONTRACT.md` (commit `79f297d`) |

**被审对象只读。** Round 2 的全部 18 个 child 与 parent 都**未修改** `D:\coding\lhrm` 下任何被审文件、
`docs/foundation/*`、`docs/validation/*`、`AGENTS.md`、`README.md`。

## 2. Swarm 构成

18 个 child，分两阶段。**child 无 GitHub 写权限、只写自己的一个 packet 文件。**

### 阶段 1 — 12 个 cluster-isolated review child（并行）

| lane | cluster | 允许读取的被审报告（`REVIEW_CONTRACT.md` §2） |
|---|---|---|
| `A` | construct ontology / redundancy | `01` `02` `02b` |
| `B` | measurement instruments / proxies | `03` |
| `C` | datasets / access / rights | `04` |
| `D` | statistics / identification / transition laws | `05` `06` `16` |
| `E` | belief / partial observability / knowledge | `07` `08b` |
| `F` | dynamics / hysteresis / pair-state emergence | `09` `10` |
| `G` | general dyad scope / ABM / LLM layer | `11` `12` `13` |
| `H` | paper positioning / novelty | `14` |
| `I` | red-team falsifiers / Gate A-B-C | `17` `A03` |
| `J` | citation / provenance recheck | `A01` `A04` |
| `K` | cross-lane contradiction map（**唯一允许跨 cluster**） | `18` + A–I 一手报告（仅定位冲突） |
| `L` | actionability / next-work-order filter | `19` `00_MANIFEST` |

所有 lane 另可读：`AGENTS.md`、`REVIEW_CONTRACT.md`、`docs/foundation/*.md`、
`docs/validation/VALIDATION_CORPUS_V0_1.md` 与 `docs/validation/fixtures/`（仅 `I` / `K` 读 fixture 细节）。

### 阶段 2 — 6 个裁决 / 核查 child（并行，均在阶段 1 完成后启动）

| child | 任务 | 独立性定位 |
|---|---|---|
| `ADJ1` | `PPR` 三方互斥、`17` F3 层边界主张、T1+F3 是否逻辑强制 D7/R3 二选一、`A-C19` `Trust` 冲突是 artifact 还是真冲突 | 与 A–L 全部隔离（只读 `17` / `A03` / `02` / `02b` / canonical） |
| `ADJ2` | 5 条候选律逐条处置、`B2` null 争议、默认 split 几何、freeze 漏洞、律 E 处置、「0/5 有可及数据集」 | 隔离（只读 `06` `16` `19` + Lavner 一手全文） |
| `ADJ3` | 8 个 meta-claim 仲裁：`MERGE/REJECT` 签发史、§2.6 唯一性、Gate B 计数、5 类 dyad 缺口、`MAPPING_FAILURE` 机制数、12 条 robust agreements 独立性、优先级与「唯一真正阻塞项」、blocker 真分类 | 隔离（只读 canonical 全文 + 3 fixtures + `17` `18` `19` `A03` `02` `02b`） |
| `EV1` | 独立证据核查：`Gate A/B/C 无法产生 rejection` 这条 headline | `PARTLY_REFUTED`：操作内核成立、两条支撑论证为假 |
| `EV2` | 独立证据核查：lane `J` 的 7 项 + manifest 算术与 DOI 前缀 | J 的 7 项 7 成立（6 `VERIFIED` + 1 `VERIFIED-AND-UNDERSTATED`），0 `REFUTED` |
| `EV3` | 独立证据核查：`G-C5` 值类封闭性 / `D-C19` `B2` null / `09` 迟滞前提推论 | `REFUTED` + `PARTLY_REFUTED` + `REFUTED`（推论层） |

### 阶段 2 的效力

阶段 2 child 的裁决**优先于**阶段 1 child 在同一命题上的判定，但**只在它们实际打开过一手件的那部分**。
parent 在 join 时逐条标注二者是否一致（见 `CONTESTED_FINDINGS.md`）。
**EV3 与 ADJ2 在 `B2` 上不一致、EV3 与 lane `G` 在 `G-C5` 上不一致** —— 这两处没有被调和成单一结论，
而是作为 `CONTESTED` 原样进入最终产物。

## 3. 独立性台账（含已披露的越界）

`REVIEW_CONTRACT.md` §4 的硬规则：**「本 swarm 有 N 个 lane 都这么说」在任何情况下都不构成 verdict 升级依据。**

| 项 | 状态 |
|---|---|
| 阶段 1 的 cluster 隔离 | 除下述两条已披露事件外，全部 lane 只读本 cluster 报告 |
| `K` 跨 cluster 读取 | **contract 明确允许**。`K` 的全部结论标 `RELAYED_NOT_INDEPENDENT`；parent 在 join 时**不把 `K` 当独立票** |
| lane `B` 越界 | `B` 用宽范围 `Grep` 时看到少量 cluster 外 `G1` 等匹配行。`B` 已在 packet 中声明**未据此形成任何 verdict**。parent 判定：不污染，**但这些片段不得作为证据使用** |
| lane `L` 越界 | `L` 用 repo 级 `git grep` 看到约 50 行 cluster 外文本（多为 Stage summary 残留）。`L` 已声明**未形成 verdict**。同上处置 |
| parent 的读取 | parent **未重读** PR #31 的 25 份报告。parent 读了 `REVIEW_CONTRACT.md`、`AGENTS.md`，以及 18 份 child packet（机械抽取后的结构化字段） |
| 重复 vs 独立 | 阶段 2 的 `ADJ3` 发现：PR #31 自称的 12 条 robust agreement 中，**5 条存活 / 5 条降级为单源收敛 / 2 条必须移出**。最重一处非独立是「最大预注册研究结论逆向于工程优先级」——**1 篇 primary study（Joel et al. 2020）被 4 个 lane 转引同一组数字** |

## 4. Parent 的角色边界（自我约束）

| 允许 | 禁止 |
|---|---|
| 机械聚合 child 的结构化 verdict 字段 | 重读并总结 25 份被审报告 |
| 记录 EV/ADJ 与 lane 之间的不一致 | 「补研究」：本轮无任何新文献检索被 parent 执行 |
| 指出 child 结论的记账冲突 | 把 child 的 `PLAUSIBLE` 升为 `VERIFIED` |
| 生成本目录下的 7 份产物 | 修改 canonical / PR #31 / 任何 fixture |
| 提交本 review branch | merge PR #31；实施 `WO-N1` / `WO-N2` / `WO-N3` |
| 在 PR #31 留指针 | 触碰 Eye / Juece；读取或引用 `youling/lhrm#20/#21/#22` |

## 5. Join 规程（可复现）

1. **抽取。** 对 18 份 packet 做字段级抽取，只取 `claim_id / claim / verdict / requires_canonical_change /
   needs_experiment_or_data / corroboration|independence_status / recommendation_to_architect`。
   三种 packet 布局（编号字段块、markdown 宽表、markdown 键值表）分别处理。
2. **归一化只作用于展示。** `CROSS_LANE_VERDICT_MATRIX.md` 的 `primary` 列是 parent 为计数抽出的首个枚举词；
   `verdict` 列保留 child 原文。**parent 未改写任何 verdict、未合并任何两行。**
3. **抽取覆盖缺口是公开的。** lane `E` 有 4 行、`H` 与 `K` 有若干行因 child 使用了非标准字段名而未被抽到；
   矩阵中这些行以空 `claim` 呈现，并在矩阵 §1 下方显式声明。**不得据矩阵推断某 lane 的结论条数。**
4. **不重复计票。** 跨 lane 的一致性只在 child 自己已标注 `INDEPENDENT` 且未共享来源时才被记为强化。
5. **冲突不调和。** 阶段 1 与阶段 2 的分歧、以及阶段 2 之间的分歧，一律进 `CONTESTED_FINDINGS.md`。
6. **计数更正优先。** 凡 `J` / `EV2` 指出 PR #31 durable 文本的记账错误，本 review **记录更正**（§7），
   **但不修改 PR #31**。PR #31 的更正由其自身后续 commit 或 Architect 决定。

## 6. Verdict 词表

阶段 1 使用 `REVIEW_CONTRACT.md` §4 的五词（`VERIFIED / PLAUSIBLE / CONTESTED / UNSUPPORTED / WRONG-SCOPE`）。
阶段 2 为裁决需要使用了以下附加记法，parent 保留原记法并给出映射：

| 附加记法 | 含义 | 映射到五词 |
|---|---|---|
| `PARTLY_REFUTED` | 操作内核成立、支撑论证被推翻 | 按子命题分别记 `VERIFIED` / `UNSUPPORTED` |
| `REFUTED` | 命题（含其框架）不成立 | `UNSUPPORTED`（对断言本身）；不等于「为假」 |
| `MOOT` | 表述被换主语/换量词后不再可判 | 记录原表述并给替代表述 |
| `RESOLVED_FOR_FACT` | 靠重读一手行即可结清 | `VERIFIED`（结清的是记账事实，不是真值） |
| `GENUINELY_OPEN` | 无数据不可判 | 保持 `CONTESTED` / `UNKNOWN` |
| `NOT_ENFORCEABLE_AS_WRITTEN` | 文本写了但不可执行 | `WRONG-SCOPE` 的近亲，parent 单列 |
| `IMPRECISE` | 方向对、措辞不精确 | `PLAUSIBLE` + 需改写 |
| `REPRODUCED_BY_ME` | 复算自 canonical corpus | 视复算对象而定 |

## 7. 本轮对 PR #31 durable 文本的记账更正（记录，不改 PR #31）

以下全部来自 `J` 与 `EV2`，`EV2` 已独立复算。**这些是本 review 交付物的实质内容之一**：
PR #31 的 manifest 与两份审计报告的记账与引用分级**不可按现状引用**。

| # | 位置 | 现状 | 更正 | 依据 |
|---|---|---|---|---|
| M-1 | `00_MANIFEST.md` §2b（OSF 前缀段） | 「`10.31234` 解析、`10.31219` 404」；`10.31219` 是 OSF project 前缀 | 两个前缀**均 live**（同属 `Center for Open Science`）；`f6wbn` 只在 `10.31234` + `_v1` 下注册。`10.31219/osf.io/gu8z7` → 302 → 终态 200 | `EV2` 实测 + `A04:193` 自己记 ✅ ⇒ PR 内部文档直接反驳 manifest |
| M-2 | `00_MANIFEST.md` §4 B-9 | 18 lane 自报数之和 ≈ **1,201**；高估 **2.3–3.4×** | 之和 = **878**（脚本相加，两处清单各自求和一致）；相对 533 distinct source = **1.65×**，相对 350 = **2.51×**。`1,199` 是原始出现次数，与 lane 内去重计数不同量纲 | `EV2` §4（独立复算）+ `J-C4` |
| M-3 | `00_MANIFEST.md` §2b（`08b` 修复计数） | 「修了 7 处」 | **8 处**（`git show 8adcf0b -- 08b` 改动行 `[S2][S12][S13][S34][S37][S51][S60][S70]`） | `EV2` §1（`J-C20` 成立） |
| M-4 | `00_MANIFEST.md` §2b（`08b [S15]`） | 「只改作者，未改年份」；A01 给 2008 / action 行给 2010 | `08b:755` 的 `[S15]` **根本没有作者字段**；其年份是 **2025**，A01 实际给的就是 2025（`A01:456`）。**A01 是对的，manifest 的转述在年份与性质上都错** | `EV2` §1（`J-C21` 成立且更错） |
| M-5 | `A01_EVIDENCE_QUALITY_AUDIT.md` §1.1 line 34 | 「Crossref 解析 **353/353（100%）**」 | **337/353 = 95.5%**（`A01:15` 自己已写对）。同一文件两行冲突 | `EV2` §1（`J-C13` 成立） |
| M-6 | `A04` §2.1 / §2.3 | `1,201` 与「2.3–C3.4×」 | 见 M-2 | `EV2` §5.4 / §5.5（提供 verbatim 替换文本） |
| M-7 | `A04` §4.2 承重表作者列 | 「30 项中 28 项强度充分」 | **≥16/30（53%）作者归属错**。`EV2` 独立打开 J 未开的 11 行，测得 6/11 错，与 J 的 53% 合并成立。另：`A04` 的 642 行来源表**结构上没有 author / title 两列** ⇒ 该缺陷类在 A04 内**无法被发现** | `EV2` §1、§6.3（`J-C7` 成立） |
| M-8 | `A04` §3.3.4 | `10.1037/h0046049` = Cartwright & Harary 1956, *Psych Review* **63(4)** 判 ✅ 一致 | 实为 **63(5):277–293** ⇒ **「已通过」清单里有错项** | `J-C15` `UNSUPPORTED` |
| M-9 | `A04` D5 | `10.1024/1662-9647.a000031` 的问题是「前缀与著录期刊族不一致」 | 该理由不成立 | `J-C14` `UNSUPPORTED` |
| M-10 | `A04` §6.3 F1 / Fixture 003 权利边界 | `13` 全篇 0 次记录 `pointer_only` / `ai-train=no` / `GPTBot Disallow`，却用其 transcript 单元 | **边界存在**（`J-C16` `VERIFIED`）；是否构成违反由 Human 权利裁决，`J` 与 `G` 均标 `CONTESTED` / 无权裁定 | `J-C16` `VERIFIED` + `J-C17` `CONTESTED` |

`EV2` §5 另提供了 **10 块 verbatim 替换文本**（每块标明目标文件与行号），可直接用于 PR #31 的后续修订。
本 review 不代为 paste（PR #31 不在本轮变更面内）。

## 8. 覆盖缺口与本轮的非主张

**parent 的非主张（explicit non-claims）**

1. 不主张 PR #31 的任何一条实质经验结论为假。本轮改的是**记账、标签、严重性与推论层级**。
2. 不主张 `J` / `EV2` 的抽样无偏。两者都自陈抽样覆盖未知（`J-C22` `PLAUSIBLE`）。
3. 不主张 `EV1` 的「只需文档编辑」包含 Gate A/B/C 从未完整执行过一次的成本——那是**另一笔钱**。
4. 不主张 `ADJ3` 的 blocker 分类是唯一正确的分类；它给的是四类分诊，成员划分依据「解决它需要谁做什么」。
5. 不对 `#20` / `#21` / `#22` 的内容做任何猜测、引用或推断。三者状态一律 `UNKNOWN`（隔离契约）。
6. 不主张 rights / egress / timeout 类限制背后存在 ontology 结论。全部按 `RECLASSIFY_AS_METHOD_LIMIT` 处理。
7. 不把 packet 未随本 PR 提交当作可接受的长期状态：这是本轮的一个**已知交付缺陷**，见 §9。

**swarm 的结构性覆盖缺口**

| 缺口 | 后果 |
|---|---|
| packet 未随 PR 提交（18 份共 ~1.5 MB） | 矩阵的 `claim` 列被截断；第三方无法在本 PR 内复核完整 `verdict` 字段。**这是本轮最需要 Architect 知晓的交付缺陷。** |
| `E` / `H` / `K` 部分行未被机械抽取 | 这些 lane 的实质内容靠 `top_recommendations` 承接，可能有结论未进入矩阵 |
| 无 lane 覆盖 `15_CASEBANK_EXPANSION.md` | `I` / `K` 均声明未读 |
| 0 次外部 DOI 复核（`ADJ3`） | `ADJ3` 对 `A6`（Joel 2020）、`A7`（`ES=.09`）等外部主张**不发表意见**——包括不确认也不否认 |
| 未运行 Gate A/B/C 任何一次 | 契约禁止实施。**因此本 review 无法确认「门实际上会产出什么」** |

## 9. 本目录 7 份产物

| 文件 | 内容 | 读法 |
|---|---|---|
| `REVIEW_SWARM_MANIFEST.md` | 本文件。入口 | 先读 §2 §3 §7 |
| `CROSS_LANE_VERDICT_MATRIX.md` | 397 行 mechanical verdict 矩阵（12 lane） | 分诊用；**先读 §0 免责** |
| `HIGH_CONFIDENCE_FINDINGS.md` | 站得住的结论与缺陷发现 | Architect 优先读 |
| `CONTESTED_FINDINGS.md` | 两侧都有证据 / 阶段间不一致的命题 | **需 Architect 或 Human 裁决的都在这里** |
| `REJECTED_OR_WEAK_FINDINGS.md` | 被推翻、需撤回或需重述的 PR #31 主张 | 引用 PR #31 前必读 |
| `CANONICAL_CHANGE_PROPOSALS.md` | 需要动 `docs/foundation/*` / `AGENTS.md` 的候选 + 撤回项 | 需显式签署 |
| `NEXT_EXPERIMENTS.md` | 分层的后续动作（可立即 / 需授权 / 需数据 / 本轮禁止） | 派工前读 |

## 10. 停止条件

本 swarm 到此为止。它**没有**：

- 实施任何 Work Order（`WO-N1` / `WO-N2` / `WO-N3` 明确禁止）；
- 修改 canonical、`docs/validation/*`、fixture、`AGENTS.md`、`README.md`；
- 修改或关闭 PR #31；
- 读取 `#20` / `#21` / `#22`；
- 执行 Gate A/B/C；
- 触碰 Eye / Juece；
- 执行任何新文献调研。

下一动作权在 **Human / Project Architect**。本目录 7 份产物是提交审议的输入，不是决议。
