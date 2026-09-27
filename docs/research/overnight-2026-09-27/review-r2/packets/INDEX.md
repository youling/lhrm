# `packets/` — durable Round-2 review child packets (machine-readable)

> **本目录是 PR #32 对 `ARCHITECT_ADJUDICATION_V1` §D 第 7 条
> （"Preserve audit child packets or an equivalent complete machine-readable
> verdict artifact so third parties can reproduce the join"）的应答。**
> 由 `tools/extract_packets.py` 生成，**不要手改**。
> 重新生成：`python tools/extract_packets.py --packets-dir <18 个 R2_*.md 所在目录> --out-dir packets --assert-complete`
>
> **简体中文摘要**：
>
> * **18 个 child、438 条 record**，11 个契约字段**逐字**保存，**零截断**。
> * 源 packet **不在本 PR 内**；§2 给出它们的 **sha256**，这是第三方校验的锚点。
> * §3 是**抽取契约**（6 种布局变体、列名别名表、11 个字段、完备性断言、
>   捕获/不捕获范围、派生字段、CoT 筛查）——规范文件是
>   `../tools/packet_contract.py`，第三方可以审计 scoping 本身。
> * §4 是**体量预算**：JSON 为源 markdown 的约 1.27×，差额全部是键名与断言，
>   不是内容膨胀；**可评审性靠结构**（18 文件 / 438 主键 / 11 字段 / `_locator`
>   行号 / 机器断言 / 矩阵由本目录生成），不靠体量。
> * **完备性证明**在 `COMPLETENESS.md`；**CoT 筛查**在 `SANITISATION.md`。

## 0. 一句话

18 个 child packet 的**每一个结构化字段**都在这里，且**未截断**。
438 条 record，全部有稳定 `claim_id` 主键、11 个命名字段、
每个 record 一个 `_locator`（回指源 packet 的行号与节路径）。
源 markdown 共 1551099 字节 / 6 种互不相同的布局；这里是同样的内容加上键、
索引与断言。**这不是 markdown 的转储。**

## 1. 文件清单（18 个）

| JSON | lane / child | cluster | role | records | `claim` 非空 | `verdict` 非空 | `recommendation_to_architect` 非空 | 源 packet 字节 |
|---|---|---|---|---:|---:|---:|---:|---:|
| `R2_A.json` | `A` | construct ontology / redundancy | cluster_review | 33 | 33 | 33 | 33 | `86591` |
| `R2_B.json` | `B` | measurement instruments / proxies | cluster_review | 24 | 24 | 24 | 24 | `90236` |
| `R2_C.json` | `C` | datasets / access / rights | cluster_review | 36 | 36 | 36 | 36 | `116384` |
| `R2_D.json` | `D` | statistics / identification / transition laws | cluster_review | 40 | 40 | 40 | 40 | `112504` |
| `R2_E.json` | `E` | belief / partial observability / knowledge | cluster_review | 25 | 25 | 25 | 25 | `95325` |
| `R2_F.json` | `F` | dynamics / hysteresis / pair-state emergence | cluster_review | 33 | 33 | 33 | 33 | `128442` |
| `R2_G.json` | `G` | general dyad scope / ABM / LLM layer | cluster_review | 30 | 30 | 30 | 30 | `153723` |
| `R2_H.json` | `H` | paper positioning / novelty | cluster_review | 57 | 40 | 57 | 40 | `84719` |
| `R2_I.json` | `I` | red-team falsifiers / Gate A-B-C | cluster_review | 30 | 30 | 30 | 30 | `75733` |
| `R2_J.json` | `J` | citation / provenance recheck | cluster_review | 23 | 23 | 23 | 23 | `64453` |
| `R2_K.json` | `K` | cross-lane contradiction map | cluster_review | 50 | 50 | 26 | 42 | `79260` |
| `R2_L.json` | `L` | actionability / next-work-order filter | cluster_review | 20 | 20 | 20 | 20 | `87248` |
| `R2_ADJ1.json` | `ADJ1` | PPR / F3 / D7-vs-R3 / Trust adjudication | adjudication | 4 | 4 | 4 | 4 | `60652` |
| `R2_ADJ2.json` | `ADJ2` | transition-law / null / geometry / freeze adjudication | adjudication | 6 | 6 | 6 | 6 | `75366` |
| `R2_ADJ3.json` | `ADJ3` | meta-claim arbitration (8 items) | adjudication | 8 | 8 | 8 | 0 | `82111` |
| `R2_EV1.json` | `EV1` | independent evidence check: Gate A/B/C headline | evidence_check | 6 | 6 | 6 | 0 | `41456` |
| `R2_EV2.json` | `EV2` | independent evidence check: lane J + manifest arithmetic | evidence_check | 10 | 10 | 10 | 0 | `48580` |
| `R2_EV3.json` | `EV3` | independent evidence check: G-C5 / D-C19 / hysteresis | evidence_check | 3 | 3 | 3 | 0 | `68316` |

| **合计** | — | — | — | **438** | — | — | — | — |

JSON 合计 **1975118 字节（1928.8 KiB）**。

## 2. 源 packet 的 sha256（第三方校验锚点）

源 packet **不在本 PR 内**（它们当时只存在于作者的临时目录）。下表是唯一
的权威指针：任何第三方可用同样的 sha256 校验自己手上的源文件。

| 源文件 | sha256 | bytes | lines |
|---|---|---:|---:|
| `R2_A.md` | `a46ab2ed77ca377ae31c7d378c4e9cbf6e59f6cc7afe49109d2ad829f5f37692` | 86591 | 706 |
| `R2_B.md` | `a956ebf566edfd9c5de8fd5315ab68dd7fb3213d24cedd1d699d15ac7513ab51` | 90236 | 705 |
| `R2_C.md` | `cc0b9266635e2fe3c61c6c85daf1d77858af2a2f264c2b169237342ff4ed999b` | 116384 | 923 |
| `R2_D.md` | `0359afe2b6df69a2811c152cfe1ccf5369c8c584c24d6d1320f50ddfa97f7bad` | 112504 | 866 |
| `R2_E.md` | `b6581a07d29f168cd9f41af384a6d5e8a01e75d1444e1f486480d67eee8ab18f` | 95325 | 586 |
| `R2_F.md` | `3189d251d87a1af9a95b7a2a2f35b345faaf67a4e2cc6cf02a48ed4b955f062e` | 128442 | 822 |
| `R2_G.md` | `30bdebe7b17ea4f484a0ee20696add8c9216e2c3fe32ecd118586486d0c2b9a5` | 153723 | 797 |
| `R2_H.md` | `e124248cbb4d9a3d116dfe7ecfbd9687afdd4492bae16a490f4e96f26425e7b2` | 84719 | 326 |
| `R2_I.md` | `516e8e8cd02eb0be7b4cb111647bf1a6dc5f9ba102a1b75a5ece4e420b99f8b2` | 75733 | 329 |
| `R2_J.md` | `474bb498074599a6f785fb1d67489c0aadd0899b52e66df6a7c4d4ff604be07c` | 64453 | 461 |
| `R2_K.md` | `c77de37aef7aaaaeee09e521dc44f196460ba9026d7da906fb6b1c602fa4f8f7` | 79260 | 371 |
| `R2_L.md` | `61a49ff8f047c9652c26144bbe4946bee43726dba2358060ea395f0627fd3fc8` | 87248 | 645 |
| `R2_ADJ1.md` | `8ed7199675a53804ffcfb880554ff86328dcefd1124f5e5c4fb7a27d9ec8e03b` | 60652 | 517 |
| `R2_ADJ2.md` | `d80e32b6dd83ec2a9138e588bc913eaf1bb7afb4a486a8eb26e5259640d3433f` | 75366 | 471 |
| `R2_ADJ3.md` | `3e357b0df261fc54b27f7291571b273b68ffeff1fbc0d90174e72af2b9ea991e` | 82111 | 606 |
| `R2_EV1.md` | `7e3552baad7341e3897b2d234b22f9960f44077172ea385e6ecf900e5f31f83a` | 41456 | 272 |
| `R2_EV2.md` | `bb0add74a6a1c01b9360e6f3fabd38cf317aa843bfb892d953385f03dfcf92db` | 48580 | 451 |
| `R2_EV3.md` | `439577c39249bca217b822825cedb1d982686e1d3ba6a33a73c5ec5a02ce5b68` | 68316 | 559 |

## 3. 抽取契约（extraction contract）

规范文件：**`../tools/packet_contract.py`**。它是一份**冻结的登记表**，
每一次 scoping 决策都写在里面，第三方可以审计 scoping 本身而不只是解析结果。

### 3.1 记录的 11 个字段

`claim_id` · `claim` · `source_report` · `verdict` · `supporting_refs` ·
`strongest_counterevidence` · `requires_canonical_change` ·
`needs_experiment_or_data` · `duplicate_of` · `corroboration` ·
`recommendation_to_architect`

前 10 个是 `REVIEW_CONTRACT.md` §5 的必填字段；第 11 个 `corroboration`
是 §4 硬规则字段（lane `I`/`J`/`K` 的表头写作 `independence`）。

**join 使用的 6 个字段**（`JOIN_FIELDS`）：`claim_id` / `claim` /
`verdict` / `requires_canonical_change` / `corroboration` /
`recommendation_to_architect`。这 6 个字段**在任何地方都不截断**。
`primary`（用于计数的首个枚举词）不是 packet 字段，由
`../tools/regenerate_matrix.py` 在渲染时派生。

### 3.2 六种布局变体

| 变体 | 用它的 child | 形态 |
|---|---|---|
| `block_numbered` | `A` `C` `D` `E` `G` `L` | `### <id> — 标题` + `N. \`字段\`: 值`（含 `**字段:**` 与键重复两种写法） |
| `kv_table` | `B` | `### <id> — 标题` + 每记录一张 `\| 字段 \| 内容 \|` 两列表 |
| `block_bullet` | `F` | `**\`<id>\` — 标题**` + `- \`字段\`: 值` |
| `table_wide` | `H` `I` `J` `K` `EV1` `EV2` | markdown 宽表；列名经 `COLUMN_ALIASES` 解析；`其余字段` / `10 字段摘要` 复合列按契约 §5 顺序拆分 |
| `qblock_h3` | `ADJ1` `ADJ3` | `## Q<n> — 问题` + `### \`字段\`` 子块 |
| `qblock_bold` | `ADJ2` | `# Q<n> — 问题` + `**字段**` 块 |
| `qblock_h1` | `EV3` | `# Claim <n> — 标题` + `### \`字段\`` |

### 3.3 完整性断言

`--assert-complete` 在下列任一情况**退出码 1**：

1. 任一 child 的 `declared_records != extracted_records`；
2. 任一 child 内 `claim_id` 重复；
3. `claim_id` 不符合该 child 声明的 id 约定；
4. record 落在声明的 record scope 之外；
5. 声明的 record scope 各节行区间互相重叠。

`declared_records` 由**锚点扫描**得到，`extracted_records` 由**记录解析器**
得到，两条代码路径互不调用，因此该断言不是同义反复。
逐包结果见 **`COMPLETENESS.md`**；字段覆盖矩阵见其 §2；
字段缺失的逐条原因见其 §5。

### 3.4 捕获范围

**捕获**：`records[]`（全部字段、逐字）、`files_audited`、
`coverage_statement`、`specialty_answers[]`（12 个 cluster child 各 4 条）、
`top_recommendations`、`explicit_non_claims`、`provenance_note`、
`sections_index`（全 packet 的节标题与行区间，便于定位未捕获内容）。

**不捕获**（逐 child 列在每个 JSON 的 `capture_scope.not_captured`）：
packet 抬头块、未绑定到必填字段的方法叙述、lane 内部的 10 个 focus 问题节、
语料级重复映射表、DOI 逐条核验日志、以及 `EV2` §5 的 verbatim 替换文本
（后者属 PR #31 的修复面，已由 Round 3 的 repair children 重新生产）。

### 3.5 派生字段

`claim_source` · `corroboration_source` · `_composite_raw` ·
`_composite_slots` · `_extra_columns` · `_extra_fields` · `_locator` ·
`_title` · `_claim_id_raw` · `_claim_id_disambiguated`

前两个说明该字段的值来自哪里；`_extra_*` 保存布局处理器**未能**绑定到
11 个规范字段的原文（逐字，不丢弃）；`_locator` 回指源 packet 行号。
每个 JSON 顶层的 `schema.derived_fields` 列出同一张表。

### 3.6 private chain-of-thought

抽取器**不重写任何已捕获文本**（重写会破坏 `REVIEW_CONTRACT.md` §4
"引用原文逐字" 的要求，也会使 artifact 无法对 sha256 校验）。
它改为跑一份冻结的检测器（`SANITISATION_RULES`，6 条规则），
逐条记录命中与**处置**。逐条结果见 **`SANITISATION.md`**。

## 4. 体量预算

| 项 | 字节 | 占 JSON 总量 |
|---|---:|---:|
| `records[]`（438 条，11 字段逐字） | 892295 | 45.2% |
| 其余捕获节 + `sections_index` + `schema` + `capture_scope` + `sanitisation` | 434125 | 22.0% |
| JSON **格式开销**（`indent=1` 的换行与缩进；**不含任何内容**） | 648698 | 32.8% |
| **JSON 合计** | **1,975,118** | 100% |
| （对照）源 18 个 markdown 合计 | 1,551,099 | — |

体量结论：JSON 为源 markdown 的 **1.27×**。差额是键名、`_locator`、schema
与断言，加上 `indent=1` 的格式开销；**内容本身没有被复制或膨胀**。
`records[]` 那 892,295 字节是「不截断 + 逐字」的**下界** —— 那 11 个字段就是
`CROSS_LANE_VERDICT_MATRIX.md` 的 join 输入，删任何一个都会重新制造
可复现性缺陷。**可评审性不靠体量，而靠结构**：

* 18 个文件 = 18 个 child，一一对应，无单体 dump；
* 438 条 record 全部有稳定 `claim_id` 主键，可 `grep '"claim_id": "A-C19"'`；
* 11 个字段名固定，schema 写在每个 JSON 顶部；
* `_locator.line_start` 让任何一条都能回到源 packet 的具体行；
* `COMPLETENESS.md` 给出机器可读的抽取完备性证明；
* `../CROSS_LANE_VERDICT_MATRIX.md` 由本目录**生成**，因此矩阵与 packet
  不可能不一致。
