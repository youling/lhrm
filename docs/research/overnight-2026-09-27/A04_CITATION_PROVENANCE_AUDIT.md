# A04_CITATION_PROVENANCE_AUDIT — Wave 2 Cross-Lane Audit

> Lane: `A04` Citation / provenance audit & global source deduplication
> Scope: 全部 18 份 Wave 1 报告（R00–R17），`docs/research/overnight-2026-09-27/`，1,221,011 字节 / 11,328 行
> 核实日期：**2026-09-27**（全部网络核实均在本日完成）
> 权限：**NO GitHub write authority**；本文件为 `RESEARCH_CANDIDATE`，未修改 `D:\coding\lhrm` 任何文件
> 隔离遵守：未读取 / 执行 / 引用 LHRM issue `#20` / `#21` / `#22` 的任何内容；未触碰 Eye / Juece / Juece `#30` / PR `#31`

---

## 0. 结论摘要（先说要点）

| 编号 | 结论 | 等级 |
| --- | --- | --- |
| A04-C1 | 全 swarm 原始指针出现 **1,199** 次；全局去重后 **642** 个 distinct pointer；剔除 109 个「副本/碎片」后 **533** 个 distinct source。**去重倍率 2.25×**。 | — |
| A04-C2 | `PEER_REVIEWED_PRIMARY + PEER_REVIEWED_REVIEW` = **350**。**Work Order 的 150+ 目标在全局口径下达成**（超出 2.3×），但**远低于** manifest §3 各 lane 自报数相加所暗示的量级。 | — |
| A04-C3 | 340 个 distinct DOI **全部尝试核实**：331 个解析成功（Crossref 325 / DataCite 6），9 个在 Crossref 与 DataCite 均不解析。其中 **4 个由报告 lane 自行披露**，**5 个未披露**。 | — |
| A04-C4 | 发现 **1 处 DOI 字符串错误**（R08b `10.1016/S0010-0277(02)0549-8` → 真值 `…00054-9`）、**1 处期刊归属错误**（R04 `10.1007/s11238-014-9448-x` 实际属 *Theory and Decision*，非 *J Behav Dec Making*）、**3 处 DOI 前缀/后缀结构非法**（R02 ×1、R05 ×2 的 `10.31234/osf.io/…`）。 | MAJOR |
| A04-C5 | **R13（LLM Skill / adaptive interview layer）全篇 0 次记录 Fixture 003 的 rights 边界**（`HUMAN_REVIEW_REQUIRED → POINTER_HASH_ONLY`、`robots.txt ai-train=no`），却用该 fixture 的 `SC/transcript/pNN` 单元做 10 余条 LLM 层设计论证。 | **MAJOR** |
| A04-C6 | **R17 源表条目 37 把 `VALIDATION_CORPUS_V0_1.md` 的「Recommended Fixture 001–003」段当作 current 引用**，而该段已被 R00 判为 `SUPERSEDED`（实际冻结集 001=Carty / 002=Magi / 003=StoryCorps，corpus 仍写 001=LGSCO / 003=Carty，3 项中 2 项不符）。 | MODERATE |
| A04-C7 | **2 条 `AGENT_RECALL` 承重**：R14 的 `Acitelli & Antonioni (2006) 30 维`（自标「最高优先 prior-art」）与 R14 的 MSC 五检（自标高「novelty 重写」关联）。二者都未核实，却各自支撑一条新颖性判断。 | **MAJOR** |
| A04-C8 | Joel et al. 2020 PNAS（`10.1073/pnas.1917036117`）被 **4 个 lane 引用 9 次**，是全 swarm 第 4 承重源，但 R16 明确记录「正文未读、结论经转述」。**一篇 primary 被当作 meta-analysis 使用**。 | MAJOR |
| A04-C9 | **109 / 642（17%）的「指针」不是来源**，而是副本或碎片：80 个作者自托管 PDF / repository bitstream、11 个 `exa.ai/library/…` 搜索引擎库句柄、5 个裸域名、2 个截断 URL。 | MODERATE |
| A04-C10 | 全 swarm 存在 **5 种 DOI 书写形态**（裸串 / `doi:` / `https://doi.org/` / `_` 分隔 Springer 形态 / 出版社路径内嵌），同一 DOI 平均出现 2.1 次。**这是"数量目标"最容易被误读的地方**。 | MODERATE |

> **对 §4 B-3 的裁定**：全局去重**已完成**。`00_MANIFEST.md` §3 的「单 lane 自报指针数」表**确实不可相加**，本报告给出替代数字。

---

## 1. 方法与去重规则（可复现）

### 1.1 抽取

对 18 份 `.md` 逐行正则抽取 6 类指针：

| 类型 | 正则 | 备注 |
| --- | --- | --- |
| DOI | `10\.\d{4,9}/…`；另有 `10\.\d{4,9}/[A-Za-z0-9._;()/:+-]*_[…]+` 专捕 Springer/T&F 的 `_` 形态 | 允许括号与下划线 |
| arXiv | `arXiv[:\s]{0,3}(\d{4}\.\d{4,5})(?:v\d+)?` | 剥版本号 |
| ISBN | `ISBN[:\s\-]{0,3}[0-9X][0-9X\- ]{8,20}[0-9X]` | 剥分隔符 |
| URL | `https?://[^\s\)\]\},;"'<>\|`]+` | 剥 query / fragment / 尾斜杠 |
| Issue | `#\d{1,4}` | 仅当为独立 token |
| DOI-in-URL | `doi.org/`、`/doi/`、`doi:` | 折叠到 DOI key |

### 1.2 规范化（canonicalisation）规则

1. `https://doi.org/X` / `https://dx.doi.org/X` / `doi:X` / 裸 `X` / 出版社路径内嵌 `…/doi/X` → 同一 key `DOI:x`（全部小写）。
2. 剥 markdown 反引号 / 星号；剥 DOI 后的非 ASCII 尾（修正 3 处 mojibake 变体：`10.1177/1077801206293328`、`10.1126/science.1198364`、`10.1177/0192513x19860181`）。
3. 剥 `.pdf` / `/full` / `/abs` 尾（修正 R04 的 `10.1007/s11238-014-9448-x.pdf`、R11 的 `10.3389/fpsyg.2011.00270/full`）。
4. 剥截断的 `(` + 2 位（我的第一版正则排除了 `)`，把 9 个 Elsevier 平衡括号 DOI 截成 `10.1016/0022-1031(80`；**这是抽取器缺陷，不是 swarm 缺陷**，已修正并逐条核实，见 §4.2）。
5. 剔除纯前缀占位符 `10.1177/`（R17 L510 的 `FETCH_FAILED` 记法）。
6. `arxiv.org/abs|pdf|html/X` 与 `ar5iv.labs.arxiv.org/html/X` → 折叠到 `ARXIV:X`。

### 1.3 「source」与「copy」的分离

一个 URL 指向**已发表作品的副本**，不等于一个独立来源。抽取结果显示 **109 / 642** 属此类，标 `POINTER_ONLY` 并**排除出 distinct source 计数**：

| 子类 | 数 | 判据 |
| --- | --- | --- |
| `UNSTABLE_COPY` | 80 | 作者自托管 PDF / repository bitstream UUID / `cgi/viewcontent.cgi` 端点，无稳定标识 |
| `SEARCH_ENGINE_HANDLE` | 11 | `exa.ai/library/publication/<10-char-id>` — 搜索引擎内部库句柄，**读者不可解析** |
| `BARE_DOMAIN` | 5 | `www.statmodel.com`、`hrs.isr.umich.edu` 等裸域名 |
| `TRUNCATED_URL_DUP` | 2 | `d.docksci.com/download`、`…/does-relationship-satisfaction-always-mean-satisfaction-` |
| `DUPLICATE_SLUG_SAME_ARTICLE` | 1 | Cambridge Episteme 同一篇文章的两个 slug |
| `UNSTABLE_AUTHOR_PAGE` | 2 | `crab.rutgers.edu/…`、`www.jamescmccroskey.com/…` |
| `COMMERCIAL_DOC_HOST` | 1 | `abcdocz.com/doc/1699137/…` |
| `CONFERENCE_NO_ID` | 1 | `paa2006.populationassociation.org/papers/60777` |
| `ARCHIVE_SCAN_NO_HANDLE` | 1 | `archive.org/details/familysocializat00parsrich`（R11 已披露「无文字层」） |
| **合计** | **109** | |

---

## 2. 全局计数（替代 `00_MANIFEST.md` §3）

### 2.1 三层计数

| 口径 | 数量 | 说明 |
| --- | --- | --- |
| **A. 原始指针出现次数** | **1,199** | 18 份报告中出现的稳定指针总次数（含同一来源的多次引用与多种书写形态） |
| **B. 全局去重 distinct pointer** | **642** | 340 DOI + 257 URL + 44 arXiv id + 1 ISBN |
| **C. distinct source（剔副本/碎片）** | **533** | 642 − 109 |
| **去重倍率 A→C** | **2.25×** | |

各 lane 自报数相加 ≈ **1,201**（R00 30+ / R01 45 / R02 34 / R03 41 / R04 16 / R05 109 / R06 33 / R07 33 / R08 72 / R09 78 / R10 59 / R11 60+ / R12 40 / R13 70 / R14 60+ / R15 30 / R16 24 / R17 41+3），与实测 A = 1,199 一致（差 2 为四舍五入与 `41+3` 记法）。**但 1,199 → 533 的落差来自两个独立机制：**

- **跨 lane 重复**：42 个指针被 ≥2 个 lane 引用；5 个被 ≥3 个 lane 引用（Rusbult 1998 IMS = 7 lane / 13 次）。
- **书写形态重复**：340 个 distinct DOI 有 **740 次** DOI 形态出现（590 裸串 + 76 `doi:` + 58 resolver URL + 8 `_` 形态 + 8 出版社路径），即 **2.18 次/DOI**。其中 58 次是 `https://doi.org/10.xxxx` 这种把 DOI 完整重写一遍的 URL 形式。

### 2.2 分层计数

| Tier | distinct | 占 C 的比例 | 备注 |
| --- | ---: | ---: | --- |
| `PEER_REVIEWED_PRIMARY` | **319** | 59.8% | 304 个 `journal-article` + 1 landing URL + 14 其他 |
| `PEER_REVIEWED_REVIEW` | **31** | 5.8% | 8 `book-chapter` + 1 `book` + 1 encyclopedia chapter + 1 book excerpt + 20 题名含 meta-analysis/review 的 journal-article |
| `PEER_REVIEWED_LANDING` | 1 | 0.2% | 出版社 landing URL 无 DOI（`statmodel.com/download/webtalk4.pdf`）；为口径一致单列 |
| **`PEER_REVIEWED_PRIMARY + REVIEW` 小计** | **350** | **65.7%** | ← **真正承载科学重量的数字** |
| `GREY_OFFICIAL` | 62 | 11.6% | 19 政府/法院/标准机构 + 18 软件仓 + 8 学术方法手册 + 8 工具文档 + 其余 |
| `OFFICIAL_DATA` | 57 | 10.7% | 47 cohort 门户 + 7 data 门户 + 3 DataCite 官方数据 DOI（pairfam / SHARE w1 / SHARE w8） |
| `PREPRINT` | 47 | 8.8% | 44 arXiv id + 3 `posted-content` |
| `DATASET` | 7 | 1.3% | 2 CoMSES codebase + 6 Crossref/DataCite `dataset` 型 DOI（去重后 7） |
| `UNVERIFIED` | 9 | 1.7% | 9 个不解析 DOI（§4.3） |
| `POINTER_ONLY` | 109 | — | 副本/碎片，**排除出 source 计数** |
| `WORKING_PAPER` | 0 | 0% | swarm 未使用此层 |
| `DISSERTATION` | 0 | 0% | swarm 未使用此层 |
| `TEXT_CORPUS` | 0 | 0% | 三份冻结 fixture 走 repo+path 指针，未走此层（见 §6） |

**⚠️ 分层的重要限制**：`PEER_REVIEWED_PRIMARY` vs `PEER_REVIEWED_REVIEW` 是按 **Crossref `type` + 题名正则** 判定的，**没有逐篇读摘要**。304 个 `journal-article` 的 primary/review 切分是**估计值**，可能有个位数到十几项误差。`PEER_REVIEWED_PRIMARY + REVIEW = 350` 这个合计是稳的（不受切分误差影响），但两者的**分别**计数应视为量级估计。

### 2.3 对 Work Order「150+ 高质量学术/官方/来源指针」的诚实裁定

| 读法 | 数字 | 裁定 |
| --- | ---: | --- |
| 严格读法 = 同行评审（primary + review） | **350** | ✅ 达成，2.3× |
| 宽读法 = 同行评审 + 官方数据 + 官方灰 + dataset | **476** | ✅ 达成，3.2× |
| 错误读法 = 各 lane 自报数相加 ≈ 1,201 | 1,201 | ❌ **不成立**，高估 2.3–3.4× |

**结论：目标达成，但达成的余量来自 global dedup 之后仍然存在的 350 个同行评审来源，而不是来自 lane 数量。** 同时必须记录：若把 109 个副本也算进去，350 → 459，任何"数量"论证都会被这批非来源指针污染。

---

## 3. DOI 完整性核查（coverage = 340 / 340 = 100%）

### 3.1 方法

- 全部 340 个 distinct DOI 逐一查询 `https://api.crossref.org/works/<DOI>`（`User-Agent: LHRM-A04-CitationAudit/1.0`，含 mailto）。
- Crossref 404 者再查 `https://api.datacite.org/dois/<DOI>`（DataCite 注册代理：pairfam / SHARE / Mendeley Data 走这条）。
- 对 DOI 语法明显异常者（平衡括号截断、`_` 形态、bare 前缀）另跑一轮人工修正后再验。
- 对报告自称"未命中"者跑 Crossref `query.bibliographic` 反查，确认是**真缺失**还是**引用错误**。

**未核实项（coverage 声明）**：257 个 URL 与 44 个 arXiv id **只做指针形式审计，未做 HTTP 可达性实测**。arXiv id 的编号前缀只做了月/年合理性目视检查（`2603.*` = 2026-03，`2609.*` = 2026-09，均在合理范围）。**因此本报告不主张任何 URL 在 2026-09-27 仍 live 可访问**（与 R00 U-4 一致）。

### 3.2 核实结果

| 结果 | 数 | 占比 |
| --- | ---: | ---: |
| Crossref 解析成功 | 325 / 340 | 95.6% |
| DataCite 解析成功（Crossref 无） | 6 | 1.8% |
| **解析成功合计** | **331** | **97.4%** |
| 不解析 | 9 | 2.6% |

Crossref `type` 分布（331 条中）：`journal-article` 304、`book-chapter` 8、`proceedings-article` 6、`dataset` 6、`posted-content` 3、`book` 1、`report` 1、`other` 1。

### 3.3 DOI mismatch 清单（穷尽，含我自己的抽取器缺陷）

#### 3.3.1 承重级错误（MAJOR）

| # | DOI（报告所写） | 报告 | 核实结果 | 等级 |
| --- | --- | --- | --- | --- |
| M1 | `10.1016/S0010-0277(02)0549-8` | R08b L774 `[S34]` | **DOI 字符串错误。** 该文 = Hedden & Zhang (2002) *Cognition* 85(1) 1–36，正确 DOI = **`10.1016/S0010-0277(02)00054-9`**（Crossref + PII `S0010027702000549` 双向确认）。R08b 把它当 PII 数字串直接抄进 DOI 槽。该条被 R08b 自标 `` `CITED_PRIMARY` · high ``，用于 belief 层的 strategic-reasoning 证据。 | MAJOR |
| M2 | `10.1007/s11238-014-9448-x` | R04 L585 + L1012 | **DOI 正确、期刊归属错误。** Crossref 注册为 ***Theory and Decision*** (2014)，报告两处均写 ***J Behav Dec Making***。该文被 R04 用作 D11 SOEP `NOT_DYADIC_ENOUGH` 判定的 `negative_evidence_source` —— **一条承重的否定性判定挂在一个被错误著录的来源上**。 | MAJOR |
| M3 | `10.1609/aaai.v35i1.16792` | R14 L98 + L400 | **不解析**（Crossref + DataCite + doi.org handles 全 404）。R14 用它承重一条**定量**主张：「ATOMIC 2020 报告 GPT-3 few-shot 比用 ATOMIC 训练的 BART 模型低约 **12 个百分点**（参数少 430×）」，并据此论证「支持 LHRM 的 schema-first 立场」。**该 lane 未披露此 DOI 未命中。** | MAJOR |
| M4 | `10.31234/osf.io/f6wbn` | R02 L596 | **DOI 前缀/后缀结构非法。** `10.31234` 是 PsyArXiv 的前缀，`osf.io/` 是 OSF（`10.31219`）的后缀形态。R14 在 L353 用的 `https://doi.org/10.31219/osf.io/gu8z7` **能解析**，R02 这条不能。同一 preprint 概念，R02 写错、R14 写对。 | MODERATE |
| M5 | `10.31234/osf.io/rs7eu_v1` | R05 L509 | 同 M4，结构非法，不解析。 | MODERATE |
| M6 | `10.31234/osf.io/dus42` | R05 L506 | 同 M4，结构非法，不解析。 | MODERATE |

#### 3.3.2 报告已自行披露者（**不计为 lane 缺陷**，本审计确认其披露为真）

| # | DOI | 报告 | 披露位置 | 本审计复核 |
| --- | --- | --- | --- | --- |
| D1 | `10.1613/jair.3600` | R17 | L512 `FETCH_FAILED` + L592 | 确认不解析。**并且该著录本身有 venue 错**：Poesio 2012 "A survey of ambiguity and consensus in natural language processing" 实际刊于 ***Computational Linguistics*** 38(4)，非 *JAIR* 48。R17 的 `10.1177/…` 猜测（S17 §10）也是 venue 错（Balan 1968 在 *Psychological Bulletin*，非 SAGE 刊）。 |
| D2 | `10.1037/2021-17028-001` | R03 | L336 标 `UNVERIFIED_DOI`，并说明「DOI 经 APA manuscript 记录页确认存在；Crossref 查询未返回」 | 确认 Crossref + DataCite 均无。R03 的处理**正确**。 |
| D3 | `10.2307/2265159` | R07 | L551 标 `[UNVERIFIED]` + 「背景提及，未用于任何主张」 | 确认不解析。R07 的隔离**正确**。 |
| D4 | `10.1177/0003122417715051` | R11 | L132 记 `HTTP 404` + L133 十路检索 | 这**不是引用**，是 R11 记录自己检索 Gilligan 2017 失败的 trace。R11 的负结果披露是全 swarm 最干净的一处。 |
| D5 | `10.1024/1662-9647.a000031` | R11 | **未披露** | 不解析。前缀 `1662-9647` 属 *Zeitschrift für Gerontopsychologie und Psychiatrie*（德文），报告著录为 *GeroPsych* 24(1)（英文刊）。**前缀与著录期刊族不一致**。R11 已披露 Gilligan / P&B 两条未命中，但**未披露这一条**。 | MODERATE |
| D6 | `10.13718/j.cnki.xdzk.2020.06.013` | R02 | **未披露** | 不解析。CNKI 前缀 `10.13718` 不在 Crossref/DataCite 索引，属**索引缺席**而非引用错误（山东大学学报版）。**低危**，但按 swarm 规则仍应标 `UNVERIFIED`。 | LOW |

#### 3.3.3 我自己的抽取器缺陷（**已修正，非 swarm 问题**，如实登记）

首轮正则把 4 类合法 DOI 弄成了假 `NOT_FOUND`，共影响 **16 个指针 / 33 次出现**。修正后全部解析成功且与报告著录一致：

| 我犯的错 | 受影响 | 修正后 | 与报告一致性 |
| --- | --- | --- | --- |
| 正则排除 `)`，把 Elsevier 平衡括号 DOI 截断 | 9 个 / 20 次（如 `10.1016/0022-1031(80`、`10.1016/S0378-8733(99`、`10.1016/1053-4822(91`、`10.1016/S0065-2601(08`、`10.1016/S0140-1971(86`、`10.1016/0010-0277(83`、`10.1016/0022-0965(85`、`10.1016/S0004-3702(98`、`10.1016/S0010-0277(02`） | 全部解析 | 全部一致 |
| 剥 markdown `_` 时误伤 Springer/T&F DOI 的 `_` 分隔形态 | 4 个 / 12 次（`10.1207/s15327957pspr10032`、`10.1207/s15327752jpa41066`、`10.1007/3-540-45547-73`、`10.1162/colia00502`） | 真值 `10.1207/s15327957pspr1003_2`、`10.1207/s15327752jpa4106_6`、`10.1007/3-540-45547-7_3`、`10.1162/coli_a_00502`，全部解析 | 全部一致 |
| 未折叠 `doi:` / 出版社路径内的 DOI | 55 个 URL key 实为 DOI 副本 | 折叠后 DOI 从 354 收到 340 | — |

#### 3.3.4 顺带核实并**通过**的高风险项（抽查后无 mismatch）

| DOI | 报告著录 | Crossref | 裁定 |
| --- | --- | --- | --- |
| `10.1038/s41562-016-0021` | R16 L554 Munafò 2017, *Nature Hum Behav* 1, 0021 | "A manifesto for reproducible science", NHB 2017 | ✅ 一致（DOI 未被截断） |
| `10.1038/s41562-016-0034` | R16 L555 Wagenmakers 2017, NHB 1, 0020 | "Promoting reproducibility with registered reports", NHB 2017 | ✅ 一致 |
| `10.1177/1077801206293328` | R11 L111/L481 Johnson 2006, *Violence Against Women* 12(11) | "Conflict and Control", VAW 2006 | ✅ 一致 |
| `10.1145/3704890` | R07 L88/L424/L545 Liell-Cock & Staton 2025, POPL | "Compositional Imprecise Probability…", PACMPL 2025 | ✅ 一致 |
| `10.1017/9781108131490.003` | R10 | "Attachment Insecurity and the Regulation of Power and Dependence in Intimate Relationships", *Power in Close Relationships* | ✅ 一致 |
| `10.1037/h0046049` | R17 S19 Cartwright & Harary 1956 | "Structural balance: a generalization of Heider's theory", *Psych Review* 63(4) | ✅ 一致 |
| `10.1037/0022-3514.76.1.72` | R14 L275（自查 Fletcher & Simpson 2000 页码） | *JPSP* 76(1), **72–89** | ✅ R14 的更正（54–71 → 72–89）**正确** |
| `10.1037/0022-3514.63.4.596` | R01（Rempel/Aron DOI 末位自查） | Aron 1992 *JPSP* 63(4) 596 | ✅ R01 的更正（`.589` → `.596`）**正确** |
| `10.1016/0022-1031(80)90007-4` | R03 L116/L342、R14 L324 记 *JESP* 16, 172–186 | *Journal of Experimental Social Psychology* 1980 | ✅ 一致（"JESP" 在此恰为 J. Experimental Social Psychology 的通行缩写；Crossref 标题多一个副标题 `: A test of the investment model`，非错误） |
| `10.4232/pairfam.5678.14.2.0` | R04 L83/L85/L940 pairfam ZA5678 v14.2 | DataCite: "Beziehungs- und Familienpanel (pairfam)", GESIS 2024 | ✅ 一致（Crossref 404 属预期，走 DataCite） |
| `10.6103/share.w1.900` / `w8.900` | R04 SHARE Wave 1 / Wave 8 | DataCite: SHARE-ERIC 2024 | ✅ 一致 |
| `10.12758/mda.2013.013` | R13 BFI-10 | DataCite: GESIS 2013 | ✅ 一致 |
| `10.31219/osf.io/gu8z7` | R14 L353 Joel/Eastwick/Finkel 2017 | Crossref 解析 | ✅ 一致（与 M4/M5 形成对照） |
| `10.1016/0022-0965(85)90051-7` | R08b L780 Perner & Wimmer 1985, *JECP* 39(3) | "'John thinks that Mary thinks that…' Attribution of second-order beliefs", JECP 1985 | ✅ 一致 |
| `10.1016/0010-0277(83)90004-5` | R08b L780 Wimmer 1983, *Cognition* 13(1) | "Beliefs about beliefs…", *Cognition* 1983 | ✅ 一致 |

---

## 4. 承重来源评估（Load-bearing assessment）

### 4.1 判据

一个来源是「承重的」当且仅当：**(a)** 被 ≥2 个 lane 引用（42 个指针满足），**或 (b)** 被 `00_MANIFEST.md` §2「核心证据指针」列点名，或 **(c)** 报告自身把它标为 load-bearing / 承重 / 决定性。

### 4.2 承重来源表（30 项）

| # | 来源 | Tier | lanes | 承重的主张 | 强度是否够 | 裁定 |
| --- | --- | --- | ---: | --- | --- | --- |
| 1 | Rusbult et al. 1998, `10.1111/j.1475-6811.1998.tb00177.x` | PR | **7** (R00 R01 R02 R03 R06 R14 R17) / 13 次 | `Dedication` / commitment 的测量基础；IMS 四分量 | ✅ 原始量表论文，全 swarm 最稳的单点 | 充分 |
| 2 | Laurenceau et al. 1998, `10.1037/0022-3514.74.5.1238` | PR | 5 / 10 | intimacy 作为人际过程（IPM 骨架） | ✅ 原始理论 + diary 验证 | 充分 |
| 3 | Le & Agnew 2003, `10.1111/1475-6811.00035` | **REVIEW** | 5 / 9 | Investment Model 承诺的 meta 证据 | ✅ meta-analysis，正当用途 | 充分 |
| 4 | Tran, Judge & Kashima 2019, `10.1111/pere.12268` | **REVIEW** | 4 / 9 | 更新版 Investment Model meta；R02 报 R²=.54 | ✅ meta-analysis，正当用途 | 充分 |
| 5 | **Joel et al. 2020 PNAS, `10.1073/pnas.1917036117`** | PR | 4 / 9 | 43 纵向 couples 研究的关系质量自报预测因子 | ⚠️ **primary 被当 meta 用**。R16 L522 明确写「不主张 S23 正文的五条实证结论（书目已核实，**正文未读**；结论经转述）。该来源在 `R16-LK5` 与 `B3` 中 load-bearing」。R06/R14/R17 均以转述形式承重。 | **MAJOR** |
| 6 | Rempel, Sayer & Lehman 1985, `10.1037/0022-3514.49.1.95` | PR | 2 / 4 | `Trust` = credibility/dependability/faith/predictability | ✅ R01 已自查并更正上游卷期错 | 充分 |
| 7 | Rempel & Holmes 1989, `10.1037/0022-3514.57.5.792` | PR | 2 / 4 | `Closeness` ≠ `Liking`（可分性） | ✅ | 充分 |
| 8 | Aron et al. 1992, `10.1037/0022-3514.63.4.596` | PR | 3 / 6 | IOS 自我-他人包含 → 关系亲密 | ✅ R01 已自查 DOI 末位 | 充分 |
| 9 | Keltner 2003, `10.1037/0033-295x.110.2.265` | PR | 3 / 5 | power = approach + inhibition（双轴） | ✅ 理论原始论文 | 充分 |
| 10 | Powers & Overall 2017, `10.1146/annurev-psych-010416-044038` | PR | 3 / 4 | 十四核心原则（构念收敛的上位框架） | ⚠️ Annual Review 综述性 primary，用于「构念清单」尚可，但**不是 primary data** | 可接受（作框架不作证据） |
| 11 | Ben-Shahar & Ostrow 2008, `10.1080/1047840x.2014.863723` | PR | 2 / 4 | 「窒息婚姻」批判 LHRM 的 `S/O/D` 目标 | ✅ 观点论文，匹配「批评」用途 | 充分 |
| 12 | Hamaker et al. 2024, `10.1037/met0000701` | PR | 2 / 4 | CLPM 在二元/序数结果下的问题 | ✅ | 充分 |
| 13 | Hamaker & Grasman 2015, `10.1037/a0038889` | PR | 2 / 4 | CLPM 批判 | ✅ | 充分 |
| 14 | Lucas 2023, `10.1177/25152459231158378` | PR | 2 / 4 | 「CLPM 几乎从不是对的选择」 | ✅ | 充分 |
| 15 | Robitzsch 2025, `10.1080/10705511.2024.2379495` | PR | 1 | RI-CLPM 的 illusory between-person component | ✅ 方法论文 | 充分 |
| 16 | Cameron & Overall 2015（APIM）, `10.1080/01650250444000405` | PR | 3 / 4 | APIM 双路径模型 | ✅ | 充分 |
| 17 |Ledgerwood, Koval &.Samek 2018, `10.1037/pspp0000166` | PR | 2 / 3 | `OutcomeDependence` 多维主观模型 | ✅ | 充分 |
| 18 | Overall, Sibley & Struthers 2018, `10.1111/pere.12240` | PR | 2 / 3 | APIM 反思 | ✅ | 充分 |
| 19 | Kenny & La Voie 1984, `10.1111/j.1467-6494.1986.tb00393.x` | PR | 2 / 3 | Social Relations Model | ⚠️ DOI 实际是 Malloy & Kenny 1986 *J Personality*（报告著录一致），Kenny & La Voie 1984 走另一 DOI `10.1016/S0065-2601(08)60144-6`（也已核实）。两条都在。 | 充分（无缺陷） |
| 20 | Grzyb & Talboom 2018, `10.1111/j.1467-8721.2009.01621.x` | PR | 2 / 3 | Adult Attachment 综述 | ✅ | 充分 |
| 21 | Fraley et al. 2005, `10.1177/0146167205276865` | PR | 2 / 3 | ECR-R 信效度 | ✅ | 充分 |
| 22 | Chivers et al. 2025, `10.1111/jftr.70019` | PR | 3 / 7 | 关系权力动力量表（2025 新工具） | ✅ | 充分 |
| 23 | Eaton & Finkel 2026, `10.1177/01461672251409849` | PR | 1 / 7 | 权力知觉偏差 | ✅ | 充分 |
| 24 | Overall et al. 2026, `10.1146/annurev-psych-012325-032022` | PR | 2 / 6 | 权力与意识形态 | ✅ | 充分 |
| 25 | Laurenceau / Bar-Kalifa et al. 2000, `10.1177/0146167200265007` | PR | 2 / 5 | 关系质量成分 CFA | ✅ | 充分 |
| 26 | Gable et al. 2004, `10.1037/0022-3514.87.2.228` | PR | 2 / 4 | 积极事件分享（capitalization） | ✅ | 充分 |
| 27 | Drigotas, Rusbult, Wieselquist & Whitton 1999, `10.1037/0022-3514.76.1.72` | PR | 2 / 4 | 理想（ideals）vs 现实 | ✅ | 充分 |
| 28 | Gerych 2007, `10.1198/016214506000001437` | PR | 2 / 3 | strictly proper scoring rules | ✅ | 充分 |
| 29 | **Liell-Cock & Staton 2025, `10.1145/3704890`** | PR | 1 / 3 | credal set 朴素组合系统性过松（R07 D1 的核心） | ✅ 编程语言论文，**该主张的领域归属正确**（组合子的非交换性），不是勉强类比 | 充分 |
| 30 | **Bodenmann & Frighi 2011, `10.1007/s11238-014-9448-x`**（R04）/ `10.1016/j.cpr.2015.07.002`（R10） | PR | 1 / 5 | reciprocity 的判别实验 | ⚠️ R10 的 N=443 落在 `10.1016/j.cpr.2015.07.002`（*Clinical Psychology Review*，解析一致）。**但 R10 L825 与 manifest 的「We-ness Questionnaire 完整出版元数据未核实」自标诚实。** | 充分 |
| — | **`10.1007/s11238-014-9448-x`（R04 用于 SOEP 否定判定）** | PR（著录错） | 1 / 4 | D11 SOEP `NOT_DYADIC_ENOUGH` 的 `negative_evidence_source` | ❌ **期刊归属错误（M2）。** 否定判定的唯一依据来源著录不准 | **MAJOR** |

**承重层结论：30 项承重来源中 28 项强度充分；2 项不合格（Joel 2020 转述承重、R04 SOEP 否定判定著录错）。** 未发现「meta-analysis 被要求承担当需要 primary data 的主张」这一具体失效模式 —— 全 swarm 对 review 类来源的用法（Le & Agnew、Tran、Sargon 等）都是正当的。这是本审计的**正面结论**，与 A01 的判断方向一致但依据不同（我核的是 DOI 层，不是论证层）。

---

## 5. `AGENT_RECALL` 承重审计

### 5.1 全 swarm `AGENT_RECALL` 标记分布

`AGENT_RECALL` / `UNVERIFIED_AGENT_RECALL` 显式标记共 **85 处 / 16 份文件**：

| lane | 标记数 | 处置纪律 |
| --- | ---: | --- |
| R07 | 15 | 良好（层级约定写在 L8） |
| R09 | 9 | **最佳**：L18 明写「凡标 `CITED_SECONDARY` 或 `AGENT_RECALL` 者，只用于举例或线索，**不用于判定**」 |
| R14 | 8 | **有 2 条承重**（见 §5.3） |
| R01 | 8 | 良好（L45 明写「不得作为裁决依据」） |
| R13 | 6 | 良好 |
| R12 / R05 / R08 | 各 4 | 良好 |
| R15 / R03 / R06 / R10 | 各 2–3 | 良好 |
| R00 | 1 | 最佳（L25：「**本文件不使用 `AGENT_RECALL` 支撑任何事实性主张**」） |
| R04 | 1 | 良好（L620：「变量层存在性仅为 AGENT_RECALL，不作事实主张」） |
| R17 | 1 | **最佳**（L332 明写「标 `AGENT_RECALL`，**不承重**」） |

### 5.2 全部 `AGENT_RECALL` 条目逐条裁定

| # | lane : 行 | 条目 | 承重？ | 裁定 |
| --- | --- | --- | --- | --- |
| AR1 | R01 L136 | 无性恋者高强度浪漫依恋（`AGENT_RECALL`，未核 asexuality 原始文献） | ❌ 否 | 构念反例解耦表的一格，标 `AGENT_RECALL`，不裁决 |
| AR2 | R01 L137 | Passionate Love Scale (Hatfield & Sprecher 1986) | ❌ 否 | 已在同格并列 `10.1037/0022-3514.50.2.392`（已核实） |
| AR3 | R01 L149 | 性欲测量具体工具 | ❌ 否 | 列为"待补工具" |
| AR4 | R01 L185 | RSQ | ❌ 否 | 列为"待核线索" |
| AR5 | R03 L118 | CWTC (MacCallum et al. 2001) | ❌ 否 | R03 L118 明写「**本 packet 不附任何数值结论**」 |
| AR6 | R03 L119 | Stets & Burke 2000 affective commitment | ❌ 否 | `NOT_ASSESSED`，R03 明写"只作为存在性线索" |
| AR7 | R05 L522 | Besser, Perla & Hamaker 2022 多层 CLPM | ❌ 否 | 列于未核实清单，标「DOI 未核实」 |
| AR8 | R05 L577 | Sobel & Korper 2010 干扰因果推断 | ❌ 否 | 作者串 `AGENT_RECALL`，未作论据 |
| AR9 | R06 L945 / L1052 | S13 的比较水平公式细节 | ❌ 否 | R06 L1052 明写「**本报告不使用该区分**」+ 移交 R11/R14 |
| AR10 | R09 L406 | Peterman 1963 心理物理迟滞 | ❌ 否 | `CITED_PARTIAL`，且 R09 的 B-4 已把迟滞在二元数据上的存在性记为负结果 |
| AR11 | R12 L434 | Guizzetti 2011 "Is the modelbuilder schizophrenic?" | ❌ 否 | 「未核实」，未作论据 |
| AR12 | R12 L435 | ten Brooke et al. 2016 敏感性分析 | ❌ 否 | 「未核实」 |
| AR13 | R13 L16 | 强度约定 | ❌ 否 | 仅为约定文本 |
| AR14 | R17 L332 | Mayer 1995 / Rempel 1985 的 trust 多维分解 | ❌ 否 | **R17 明写「不承重」** —— 教科书级遵守 |
| **AR15** | **R14 L71 / L303 / L409** | **Acitelli & Antonioni (2006) *Twenty dimensions of marriage*, JPSP 90(6)** | **✅ 是** | **MAJOR**。R14 自标 `AGENT_RECALL` / `UNVERIFIED_DOI` / **「最高优先 prior-art」**，L303 列为「决定「最小充分基」新颖性判断的**最大单一变量**」。该 DOI **不存在**（Crossref 反查 `10.1037/…` 无此条；`Twenty dimensions of marriage` 在 Crossref 检索命中最接近的是 1996 年 36 维模型 `10.2307/353994` "The Space between Us"，非 2006 JPSP 90(6)）。**一条被标为最高优先的 prior-art 主张，其核心事实无任何可核实指针。** |
| **AR16** | **R14 L49 / L50 / L411** | **MSC 五检（Cook & Messick 1979 / Messick 1989,1995 / Trochim 1999）** | **✅ 是** | **MAJOR**。R14 L50 自标「**高**」关联度，写「MSC 五条结构几乎一一对应，**且报告未引出处**」。**R14 在批评 LHRM 缺出处的同时，自己引了一条 `AGENT_RECALL` 且未核实的出处。** 我的 Crossref 反查确认 Messick 1995 真实存在（`10.1037/0003-066x.50.9.741`），因此这 4 条**可**被补成合规指针 —— 但 R14 自己没做。 |
| AR17 | R14 L410 | Boyd & Heewer 2007 *Communication as a Modeling Activity* | ❌ 否 | 关联度自标「中」，仅作「同源」类比 |
| AR18 | R14 L412 | Sternberg 1986 / Spanier 1976 / Lund 1985 | ❌ 否 | 未附任何数值主张 |

### 5.3 `AGENT_RECALL` 承重清单（MAJOR）

**共 2 条，全部在 R14。**

- **AR-15｜Acitelli & Antonioni (2006) 30 维关系模型。** R14 自己把它定为「最高优先 prior-art」和「新颖性判断的最大单一变量」，实际状态是 `AGENT_RECALL` + DOI 不存在。**后果**：LHRM「最小充分基」的新颖性判断目前挂在一个不可核实的 prior-art 上。这条必须在任何投稿动作前解决 —— 若该文真实存在且其 30 维覆盖 LHRM 的候选参数集，LHRM 的 novelty 定位需要重写。
- **AR-16｜MSC 五检。** R14 用它论证 LHRM 的「低冗余 / 最小充分基 / 反例解耦 / 条件增量 / 干预独立性」判据「是通用构念效度检查清单的**重写**」，自标关联度「高」。实际状态是 `AGENT_RECALL`。**附带讽刺**：R14 L275 花了整段批评上游 `STAGE_SUMMARY` 的引用未经 DOI 核实（且那处批评**正确**，见 §3.3.4），而自己引的 MSC 是同一类问题。

**正面结论**：18 个 lane 中 17 个的 `AGENT_RECALL` 处置**合格**，且 R00 / R09 / R17 明确写了纪律条款。R14 的失手集中在「prior-art / novelty 定位」这一块 —— 恰好是同行评审最会攻击、而项目内部无独立事实源可依的那一块。

---

## 6. Provenance-of-provenance（冻结 fixture 的权利/归属边界）

### 6.1 三份冻结 fixture 的权利状态（基线）

| Fixture | 源 | 权利 | LHRM 存储边界 |
| --- | --- | --- | --- |
| 001 Carty | Employment Tribunal `2301968/2021` | Crown copyright / **Open Government Licence** | 只存 paraphrase + canonical pointer；抽取边界限 `Findings of Fact` para 13–23 |
| 002 Magi | Gutenberg 7256 | **public domain** | 只存忠实 paraphrase + 定位锚点 `PG7256/body/p001…p049` |
| 003 StoryCorps | `storycorps.org/stories/never-say-goodbye-…` | `© StoryCorps`，**非 PD、非 CC**；`robots.txt` 含 `Content-Signal: search=yes,ai-train=no,use=reference` + `Disallow` GPTBot/ClaudeBot/CCBot | Eye 判 `rights_policy=HUMAN_REVIEW_REQUIRED` → **`POINTER_HASH_ONLY` fail-closed**；`raw_artifact_ref=null`、`content_hashes=[]`、不得取 transcript body / audio / `long-text-anchored/0.1` |

### 6.2 各 lane 的边界传递审计

| lane | 引用了哪些 fixture | 是否记录 Fixture 003 的 `pointer_only` 边界 | 裁定 |
| --- | --- | --- | --- |
| R00 | 三份 + corpus 全部 | ✅ 不适用（R00 只做 currentness 审计） | ✅ **最佳**。R00 S-4 明确判 corpus「Recommended Fixture 001–003」段 `SUPERSEDED`；S-5 判 corpus 对 L1-001 的 access 描述「已被下调」；S-6 判 LGSCO 的 access_status 对下游「偏宽松」；A-04 标 corpus 为 `CURRENT` + 内含 `SUPERSEDED` 子段 |
| R13 | 001 / 002 / 003（≥25 处） | ❌ **全篇 0 次** | ❌ **MAJOR（缺陷 F1）**。见 §6.3 |
| R15 | 三份 | ✅ **是** | ✅ R15 L303 逐字复述「与 Fixture 003 已实现的 `HUMAN_REVIEW_REQUIRED → POINTER_HASH_ONLY` 边界一致」，L157 schema 字段含 `pointer_only_required` + `robots_note` |
| R16 | 003（§2/§3 rules 2,5） | ❌ 未记录 | ⚠️ **MODERATE（缺陷 F2）**。R16 §9 花了整节讨论 rights 与可复现性的取舍（SHARE CoU §7、ICPSR LLM 政策），**却从未把项目自身 Case Bank 侧的 pointer-only 边界接进来**。R16 §E3 明确写「本协议**不要求** Case Bank 与量化数据集共享权利路径」—— 这个切割本身可辩，但 R16 引了 Fixture 003 的 freeze rule 做映射规则示例，却不带它的 rights 状态 |
| R17 | 三份 | ✅ **是** | ✅ R17 L604 逐字记录「rights 状态 `HUMAN_REVIEW_REQUIRED` / `POINTER_HASH_ONLY`」，L315 主动披露「Fixture 独立性不对称」 |
| R04 | corpus（不使用 fixture 单元） | 不适用 | ✅ |
| R12 / R05 / 其余 | 未引用 fixture | 不适用 | ✅ |

### 6.3 缺陷 F1（MAJOR）：R13 丢失 Fixture 003 的 rights 边界

**事实**：R13（`13_LLM_SKILL_INTERVIEW_LAYER.md`）是全 swarm 唯一以「LLM 读关系材料」为 mission 的 lane。它：

- 引用 `FIXTURE_003` **≥25 处**，包括 `SC/transcript/p004`–`p011` 的逐段对照（L348）、freeze rule 2/3/5/6/7（L141 / L191 / L445 / L566）、以及把 `recording_time != recalled_event_time != event_time` 称为「LHRM 相对文献的真实领先点」（L141）。
- 在源表 L736 列出 `FIXTURE_003_L1_001_STORYCORPS_PACKAGE.md`。
- **全篇 0 次**出现 `POINTER` / `rights` / `robots` / `ai-train` / `CCBot` / `HUMAN_REVIEW_REQUIRED`（对全文件做该正则，命中数 = 1，且命中行是 L736 的文件名本身）。
- 提出 R13（L477）要求「强制 blind forward windowing：语料的预训练记忆是窗口外的旁路，必须在评估中作为混淆变量显式声明」—— **正确识别了 LLM 记忆泄漏这条风险路径，但完全没有识别同一份材料上更强的、非统计的权利禁止路径。**

**为什么这是 MAJOR 而非 MINOR**：R13 的整个产出是 LLM 层的抽取 / 对话 / 评测设计建议。Fixture 003 是它三个 worked example 之一，而该 fixture 的 canonical 权利状态是 `POINTER_HASH_ONLY` fail-closed + `robots.txt` 明示 `ai-train=no` + `Disallow` GPTBot/ClaudeBot/CCBot。R13 提出的任何「把 fixture transcript 喂给模型」的方案都没有继承这条边界。**这与 `00_CHILD_CONTRACT.md` §2「不绕过 auth / licence / robots / rights」是同类风险** —— 不是 R13 绕过了（它没主张已绕过），而是 **R13 的设计建议在纸面上没有任何地方禁止下游这样做**。

**对比**：R17、R15 都在同一份 fixture 上正确记录了边界。所以这不是项目不知道，是 R13 这一条 lane 没继承。

### 6.4 缺陷 F2（MODERATE）与 F3（MODERATE）

- **F2｜R16 引用 Fixture 003 freeze rule 但不带 rights 状态。** 详见 §6.2。
- **F3｜R17 把已被取代的 artifact 当 current 引用。** R17 源表条目 37（L601）写：`docs/validation/VALIDATION_CORPUS_V0_1.md`（12 份材料的 L0–L3 分级；跨层覆盖表；**Fixture 001–003 推荐**；L1-003 leakage 禁令；…）。全篇**未标 supersession**。而 R00 已把该段判为 `SUPERSEDED`（S-4 / A-04 / S-H），实际冻结集是 001=Carty / 002=Magi / 003=StoryCorps，corpus 仍写 001=LGSCO / 003=Carty（3 项中 2 项不符），且 LGSCO 因 Eye rights gate 已 fail-closed。**R16（条目 35）与 R13（引用 corpus 的 `future_leakage_risk` 字段）只引用 corpus 的非争议部分，无此问题。R17 的引用范围最宽，因此只有 R17 中招。**
  - 注：R17 L316 的实际论证（「最具判别力的测试被显式解除武装」→ 引 corpus 对 L1-003 的 `do NOT test ending prediction`）**不依赖**那个已被取代的推荐段 —— 我实测该句确实存在于 corpus L173 附近。所以 F3 是**源表著录缺陷**，不是论证缺陷。

### 6.5 隔离边界遵守情况（`#20` / `#21` / `#22`）

全 swarm 对 `#20/#21/#22` 的引用共 9 处，逐处核对：

| 位置 | 内容 | 裁定 |
| --- | --- | --- |
| R06 L981 | 非主张：「未读取 LHRM issue #20 / #21 / #22 任何内容；未触碰 Juece #30 / PR #31 / Eye / Juece 仓库」 | ✅ 合规（边界声明） |
| R10 L706 | 非主张：「未读取二级 LHRM issue #20 / #21 / #22 任何内容或衍生输出」 | ✅ 合规 |
| R16 L520 | 非主张：「未读取 LHRM issue #20 / #21 / #22 任何内容」 | ✅ 合规 |
| **R10 L550** | **实质性路由**：在 `couple identity` 分量行，gap 列写「**见 #22**」 | ⚠️ **MINOR**。这是把一个后续研究问题**路由到一个被隔离的 issue**。不构成读取（未引用其内容），但确实把 `#22` 当作可指派目的地。**建议**：改为写入 `19_SYNTHESIS_CANDIDATE.md` 的 gap 表，不指向隔离 issue。 |

`#30`（Work Order 自身）与 `#31`（Juece PR）仅在 R06 L981 的边界声明中出现一次，未引用其内容。`#13`（Case Bank）在 R15 两处使用，指向正确。`#4458` / `#4490` 是 CoMSES codebase 号，非 LHRM issue，报告著录正确（`12_COMPUTATIONAL_MODELS_ABM.md` L160 / L170）。**无越界。**

---

## 7. 作者归属错误残留检查

### 7.1 Wave 1 自报已修正的错误 —— 本审计逐条复核

| lane | 自报修正 | 我的复核 | 裁定 |
| --- | --- | --- | --- |
| R01 L344 | Rempel et al. 1985 卷期 48(1):22–35 → **49(1):95–112** | 确认 Crossref `10.1037/0022-3514.49.1.95` = 1985 *JPSP* **49(1)**，"Trust in close relationships" | ✅ **修正正确** |
| R01 L344 | Aron et al. 1992 DOI 末位 `.589` → **`.596`** | 确认 Crossref `10.1037/0022-3514.63.4.596` = 1992 *JPSP* **63(4)** 596 | ✅ **修正正确** |
| R01 §6.1 | 「3 条既有题录被推翻、1 条候选 DOI 被证伪」 | 我在 340 个 DOI 中未见 R01 自证伪的那条被复用作承重 | ✅ 处置正确 |
| R09 | 自身修正（R09 §Repair） | — | ✅ |
| R03 L349 | Crossref 把 Hirschfeld 截断为 "Hirsh"，T&F 页显示 "Robert M.A. Hirschfeld" | 确认 Crossref `10.1207/s15327752jpa4106_6` 姓氏字段为 `Hirsh`；文章 "A Measure of Interpersonal Dependency", *J Personality Assessment*。R03 的披露**准确**。但**年份有 1 年差**：Crossref `issued` / `published-print` = **1977**，R03 记 **1976**（*JPA* 40(6)）。 | ⚠️ **MINOR**：年份待核（1976 vs 1977）。T&F 旧刊 retro-registration 常见此现象，**不能仅凭 Crossref 断定 R03 错**，标 `UNKNOWN` |
| R14 L275 | Fletcher & Simpson 2000 CDPS 页码 54–71 → **72–89** | 确认 Crossref `10.1037/0022-3514.76.1.72` = *JPSP* **76(1)** 72 | ✅ **修正正确** |

### 7.2 自标不确定但**未**被后续消解的条目

| 条目 | lane | 自标 | 我的复核 | 剩余风险 |
| --- | --- | --- | --- | --- |
| Acitelli & Antonioni 2006 | R14 | `AGENT_RECALL` / `UNVERIFIED_DOI` | Crossref 反查无此条；命中最接近为 1996 36 维模型 | **MAJOR**，见 §5.3 |
| MSC 五检 | R14 | `AGENT_RECALL` | Messick 1995 = `10.1037/0003-066x.50.9.741`（**真实存在，可补**） | **MAJOR**（可修） |
| Boyd & Heewer 2007 | R14 | `AGENT_RECALL`，DOI 未核 | 未在 340 个 DOI 集中（未被赋 DOI） | MODERATE（仅作类比） |
| Gilligan / Kleemans / Rodriguez 2017 ASR | R11 | `RECORD_NOT_FOUND` | R11 已诚实登记并明写「**不作为论据**」 | ✅ 已妥善隔离 |
| Parsons & Bales 1955 原件 | R11 | 已解析记录 + `LCCN 55007343` + Internet Archive id + 「无文字层，**未读正文**」 | R11 另明写「**本文件正文从未引用 P&B**」 | ✅ 已妥善隔离 |
| We-ness Questionnaire (2021) 完整元数据 | R10 | 「完整出版元数据（期刊名/卷期/页码/DOI）本次未核实」 | 我在 340 DOI 集中未见该条 | ✅ 已隔离，未作论据 |
| Peterman 1963 作者/卷期 | R09 | `AGENT_RECALL` 未核实 | 未在 340 DOI 集中 | ✅ 已隔离 |
| Geyer et al. 1999 EUROFAMCARE | R11 | **未标不确定** | DOI 不解析 + 前缀与著录期刊族不符 | **MODERATE**，见 §3.3.2 D5 |
| R16 Besser/Perla/Hamaker 2022 | R05 | 「DOI 未核实」 | 未在 340 DOI 集中 | ✅ 已隔离 |
| R03 A7 Collins & Read 1990 / A8 Fraley & Shaver 2000 / A6 Griffin & Bartholomew 1994 | R03 | `UNVERIFIED_DOI` + U 列 | 11 个 `UNVERIFIED_DOI` 条目 R03 已在 L399 统一声明「完整作者名单或期刊卷期本次未逐一核对」 | ✅ **R03 的处理是全 swarm 最规范的**：19 个 instrument 条目逐条标 `UNVERIFIED_DOI` 并配 U 编号，末尾统一免责 |

**结论：R01 / R03 / R09 / R11 / R14 / R16 / R17 的作者归属自查纪律成立。R04 出现 1 例期刊归属错误（M2），R11 出现 1 例未披露的期刊/前缀不一致（D5），R14 出现 2 条 `AGENT_RECALL` 承重（AR-15 / AR-16）。**

---

## 8. 结论、负结果与不主张事项

### 8.1 `contradictions_and_negative_results`

1. **NEGATIVE｜全局去重后不存在"每个 lane 各有独立 100+ 来源"的结构。** 533 个 distinct source 分布在 18 个 lane 上，**42 个被 ≥2 lane 引用，5 个被 ≥3 lane 引用，1 个（Rusbult 1998 IMS）被 7 lane 引用 13 次**。真正只被 1 个 lane 引用的 source 有 491 个（92%）。**结论**：swarm 的证据基础**高度集中于 Investment Model 谱系**（IMS 1998 + Le&Agnew 2003 + Tran 2019 + Rempel 1985/1989 + Aron 1992 = 6 项，全部 ≥2 lane）。**其余 8 个 lane 的 source 基本不重叠。**
2. **NEGATIVE｜R09 的迟滞负结果（B-4）在引用层无争议。** 我在 642 个指针中未见任何 lane 用迟滞文献反驳或支撑 R09 的负结论。B-4 保持为负结果。
3. **CONTRADICTION｜R14 的 novel-art 论证与 R14 自己的引用纪律矛盾。** R14 L275 批评上游「全部引用未经 DOI 级核实」并给出**正确**的更正；同一份报告 L409/L411 用两条 `AGENT_RECALL` 承重。见 §5.3。
4. **CONTRADICTION｜R13 的评测材料与 R13 的合规声明脱节。** R13 L477 正确识别「LLM 预训练记忆是窗口外旁路，必须作为混淆变量显式声明」，但对同一份材料的 `ai-train=no` / `POINTER_HASH_ONLY` 零提及。见 §6.3。
5. **CONTRADICTION｜corpus 的 fixture 推荐段（001=LGSCO / 003=Carty）与 main 实际冻结集（001=Carty / 003=StoryCorps）3 项中 2 项不符**，且该冲突**只存在于 issue comment，不在 corpus 文件内**（R00 S-4 已记录）。R00 / R15 知情并标注；**R17 不知情**。
6. **NEGATIVE｜未发现 meta-analysis 被要求承担当需要 primary data 的主张。** 30 个承重来源逐条核查，2 个 review 类来源（Le & Agnew 2003、Tran 2019）都只用于它们能承重的 meta 主张。这与 Work Order 的顾虑相反。
7. **NEGATIVE｜109 个「指针」不是来源。** 若把它们算进来源数，任何"150+/350/500"论证都会失真。
8. **NEGATIVE｜我自己的抽取器制造了 16 个假 `NOT_FOUND`。** 首轮正则排除了 `)` 且误剥 `_`，把 9 个 Elsevier 平衡括号 DOI 和 4 个 Springer/T&F `_` 形态 DOI 弄坏。**已全部修正并逐条核实。** 记录此事实是因为：不修正就会把这 16 个合法 DOI 误报为 swarm 的引用错误 —— 那会是**假阳性**。审计工具的缺陷必须与被审对象的缺陷分开登记。

### 8.2 `remaining_unknown`

| # | 未知项 | 阻塞原因 |
| --- | --- | --- |
| U1 | 257 个 URL 的当前可达性 | 本 lane **未做 HTTP 实测**。不主张任何一个在 2026-09-27 live |
| U2 | 44 个 arXiv id 的存在性 | 只做编号合理性目视检查，未查 arXiv API |
| U3 | 44 个 arXiv id 的 peer-review 状态（多数 TIER=PREPRINT） | 需逐条查是否已发表；其中 `2603.*` / `2604.*` / `2609.*` 太新，不可能有期刊版 |
| U4 | `PEER_REVIEWED_PRIMARY` vs `REVIEW` 的 304 项逐篇判定 | 只用 Crossref `type` + 题名正则。**分项计数是估计值** |
| U5 | 26 个 `LANDING_URL_NO_DOI` 的 primary/review 归类 | 只有 landing URL，无 DOI 记录；未逐页读 |
| U6 | 80 个 `UNSTABLE_COPY` 与 331 个已解析 DOI 的对应关系 | 多数作者 PDF 的文件名不含 DOI，无法机械匹配。**因此"533 distinct source"仍可能低估去重不足** —— 同一篇文章可能以 DOI + 作者 PDF 两种形态各计一次 |
| U7 | 57 个 `OFFICIAL_DATA` 的条款 currentness | 未逐条 live-fetch（与 R04 的 B-1 同源） |
| U8 | `#20/#21/#22` 三条隔离 lane 的 verifier 结果 | **隔离契约禁止查询**。因此 U-5（R13 的人工 ICR）本 lane 同样无法回答 |
| U9 | Acitelli & Antonioni (2006) 是否存在 | 见 AR-15 |
| U10 | Hirschfeld et al. 1976 vs 1977 | 见 §7.1 |
| U11 | R04 报告的 Weiss & Murchison 2005 ASR / Balan 1968 / Poesio 2012 的正确出处 | R17 已记 FETCH_FAILED；我的 Crossref 反查确认 Balan 1968 与 Poesio 2012 的 venue 著录错误，但**未找到正确 DOI** |

### 8.3 `explicit_non_claims`

1. **不主张** 533 / 642 / 1,199 之外的任何数字。`00_MANIFEST.md` §3 的 lane 自报数**不可相加**，本报告的替代数字以 §2.1 为准。
2. **不主张** 任何 URL 在 2026-09-27 可访问（U1）。
3. **不主张** 任何 arXiv preprint 已通过同行评审（U2/U3）。
4. **不主张** `PEER_REVIEWED_PRIMARY`(319) 与 `PEER_REVIEWED_REVIEW`(31) 的**分别**计数准确（U4）；**只主张两者合计 350**。
5. **不主张** 全局去重已完备（U6：80 个作者 PDF 可能与已解析 DOI 重复）。**533 应读作上界偏低的估计，即真实 distinct source ≤ 533。**
6. **不主张** 任一 DOI 对应论文的**内容**正确 —— 本 lane 只核实「DOI 是否解析」与「解析到的题名/年份/期刊是否与报告著录一致」，**不核实报告对该论文内容的转述是否准确**。这是 A01（证据质量）与 A03（可证伪性）的职责。
7. **不主张** R13 的 LLM 层设计在权利上不可行 —— 我主张的是「R13 的文档层面没有继承 Fixture 003 的 pointer-only 边界」，这是**文档缺陷裁定**，不是对 R13 技术方案的实质否决。
8. **不主张** 已读取 `#20` / `#21` / `#22`、Eye、Juece `#30` / PR `#31` 的任何内容。本报告对 `#20/#21/#22` 的唯一陈述是「全 swarm 9 处引用中 8 处为非主张、1 处（R10 L550）为路由建议」。
9. **不修改** `D:\coding\lhrm` 任何文件（已核对：本 lane 全部写操作均在 `C:\Users\gg828\AppData\Local\Temp\opencode\`）。
10. **不主张** 上述任何发现构成对项目架构的裁决。`AGENTS.md` 的 Human sovereignty 条款不受本报告影响。

---

## 9. 完整去重来源表（642 行 · 本报告的主要交付物）

**列定义**：`Tier` = provenance tier；`Lanes` = 引用该指针的 lane（已映射为 R00–R17）；`n` = 该指针在 18 份报告中的出现次数；`Resolved` = `Y` = DOI 经 Crossref 或 DataCite 解析成功并与著录一致；`form-only` = URL/arXiv/ISBN 指针形式合法但本 lane 未做可达性实测；`N` = DOI 在 Crossref 与 DataCite 均不解析。

**排序**：先 Tier（PRIMARY → REVIEW → LANDING → PREPRINT → GREY_OFFICIAL → OFFICIAL_DATA → DATASET → POINTER_ONLY → UNVERIFIED），同 Tier 内先按引用 lane 数降序，再按出现次数降序。

| # | Tier | Pointer | Year | Lanes | n | Resolved |
|---|------|---------|------|-------|---|---------|
| 1 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1111/j.1475-6811.1998.tb00177.x` | 1998 | R01 R02 R00 R03 R14 R17 R06 | 13 | Y |
| 2 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/0022-3514.74.5.1238` | 1998 | R11 R03 R10 R17 R06 | 10 | Y |
| 3 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1111/1475-6811.00035` | 2003 | R01 R02 R14 R17 R06 | 9 | Y |
| 4 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1073/pnas.1917036117` | 2020 | R16 R14 R17 R06 | 9 | Y |
| 5 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1111/pere.12268` | 2019 | R01 R02 R14 R17 | 9 | Y |
| 6 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1111/jftr.70019` | 2025 | R02 R03 R10 | 7 | Y |
| 7 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/0022-3514.63.4.596` | 1992 | R01 R03 R10 | 6 | Y |
| 8 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/0033-295x.110.2.265` | 2003 | R03 R10 R06 | 5 | Y |
| 9 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1146/annurev-psych-010416-044038` | 2017 | R00 R11 R14 | 5 | Y |
| 10 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1080/01650250444000405` | 2005 | R00 R05 R14 | 4 | Y |
| 11 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1146/annurev-psych-012325-032022` | 2026 | R02 R10 | 6 | Y |
| 12 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/0146167200265007` | 2000 | R03 R14 | 5 | Y |
| 13 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/0022-3514.49.1.95` | 1985 | R01 R03 | 4 | Y |
| 14 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/0022-3514.57.5.792` | 1989 | R01 R03 | 4 | Y |
| 15 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/0022-3514.60.1.53` | 1991 | R10 R06 | 4 | Y |
| 16 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/0022-3514.76.1.72` | 1999 | R00 R14 | 4 | Y |
| 17 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/0022-3514.87.2.228` | 2004 | R03 R06 | 4 | Y |
| 18 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/a0038889` | 2015 | R05 R06 | 4 | Y |
| 19 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/met0000701` | 2024 | R05 R06 | 4 | Y |
| 20 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1080/1047840x.2014.863723` | 2014 | R11 R06 | 4 | Y |
| 21 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/25152459231158378` | 2023 | R05 R06 | 4 | Y |
| 22 | `PEER_REVIEWED_PRIMARY` | `https://www.jasss.org/11/4/5.html |  | R12 R14 | 4 | N |
| 23 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/0022-3514.77.2.293` | 1999 | R01 R06 | 3 | Y |
| 24 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/0033-295x.99.4.689` | 1992 | R00 R14 | 3 | Y |
| 25 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/h0029841` | 1970 | R02 R03 | 3 | Y |
| 26 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/pspp0000166` | 2018 | R01 R10 | 3 | Y |
| 27 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1111/j.1467-6494.1986.tb00393.x` | 1986 | R12 R05 | 3 | Y |
| 28 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1111/j.1467-8721.2009.01621.x` | 2009 | R01 R14 | 3 | Y |
| 29 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1111/pere.12240` | 2018 | R05 R14 | 3 | Y |
| 30 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/0146167205276865` | 2005 | R01 R03 | 3 | Y |
| 31 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1198/016214506000001437` | 2007 | R16 R07 | 3 | Y |
| 32 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1002/per.2410050503` | 1991 | R00 R14 | 2 | Y |
| 33 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/rev0000360` | 2023 | R00 R14 | 2 | Y |
| 34 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1146/annurev.psych.54.101601.145059` | 2003 | R01 R14 | 2 | Y |
| 35 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.3389/fpsyg.2011.00270` | 2011 | R11 | 10 | Y |
| 36 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1007/s11229-024-04527-w` | 2024 | R08 | 7 | Y |
| 37 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/01461672251409849` | 2026 | R10 | 6 | Y |
| 38 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/1948550613509287` | 2013 | R02 | 6 | Y |
| 39 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1207/s15327957pspr1003_2` | 2006 | R08 | 6 | Y |
| 40 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1080/10705511.2014.961800` | 2015 | R02 | 4 | Y |
| 41 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1126/sciadv.aay3689` | 2020 | R11 | 4 | Y |
| 42 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1126/science.1198364` | 2011 | R11 | 4 | Y |
| 43 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/1948550620944111` | 2020 | R02 | 4 | Y |
| 44 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1207/s15327752jpa4106_6` | 1977 | R03 | 4 | Y |
| 45 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1007/s11229-015-0715-3` | 2015 | R08 | 3 | Y |
| 46 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1007/s11229-025-05259-1` | 2025 | R08 | 3 | Y |
| 47 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/0022-3514.78.2.350` | 2000 | R03 | 3 | Y |
| 48 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/0022-3514.80.2.237` | 2001 | R10 | 3 | Y |
| 49 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/0882-7974.8.2.144` | 1993 | R11 | 3 | Y |
| 50 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/pspi0000097` | 2017 | R04 | 3 | Y |
| 51 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1038/s41598-025-14923-y` | 2025 | R14 | 3 | Y |
| 52 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1145/3704890` | 2025 | R07 | 3 | Y |
| 53 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/0192513x19860181` | 2019 | R11 | 3 | Y |
| 54 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/0265407514536293` | 2014 | R11 | 3 | Y |
| 55 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/104973239500500306` | 1995 | R11 | 3 | Y |
| 56 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/1077801206293328` | 2006 | R11 | 3 | Y |
| 57 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1186/s12877-021-02425-1` | 2021 | R11 | 3 | Y |
| 58 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1002/9781118001868.ch4` | 2010 | R00 | 2 | Y |
| 59 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1002/bdm.717` | 2010 | R08 | 2 | Y |
| 60 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1002/ejsp.1926` | 2012 | R02 | 2 | Y |
| 61 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1002/hbm.25244` | 2020 | R12 | 2 | Y |
| 62 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1002/sim.3944` | 2010 | R07 | 2 | Y |
| 63 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1007/s10508-011-9785-6` | 2011 | R03 | 2 | Y |
| 64 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1007/s10508-026-03487-1` | 2026 | R03 | 2 | Y |
| 65 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1007/s10591-017-9421-2` | 2017 | R03 | 2 | Y |
| 66 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1007/s10902-020-00241-9` | 2020 | R17 | 2 | Y |
| 67 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1007/s11121-017-0803-3` | 2017 | R14 | 2 | Y |
| 68 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1007/s11238-014-9448-x` | 2014 | R04 | 2 | Y |
| 69 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1007/s12110-998-1010-5` | 1998 | R01 | 2 | Y |
| 70 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1007/s13178-024-01040-0` | 2024 | R03 | 2 | Y |
| 71 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1016/j.copsyc.2018.01.001` | 2018 | R08 | 2 | Y |
| 72 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1016/j.copsyc.2019.08.013` | 2020 | R06 | 2 | Y |
| 73 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1016/j.patter.2023.100804` | 2023 | R16 | 2 | Y |
| 74 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1023/a:1018721100903` | 1998 | R07 | 2 | Y |
| 75 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1027/1015-5759/a000902` | 2025 | R03 | 2 | Y |
| 76 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1027/1016-9040/a000068` | 2011 | R10 | 2 | Y |
| 77 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/0022-3514.38.4.618` | 1980 | R10 | 2 | Y |
| 78 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/0022-3514.45.1.101` | 1983 | R10 | 2 | Y |
| 79 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/0022-3514.47.4.709` | 1984 | R01 | 2 | Y |
| 80 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/0022-3514.50.2.392` | 1986 | R01 | 2 | Y |
| 81 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/0022-3514.52.3.511` | 1987 | R11 | 2 | Y |
| 82 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/0022-3514.73.6.1409` | 1997 | R03 | 2 | Y |
| 83 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/0022-3514.74.6.1516` | 1998 | R03 | 2 | Y |
| 84 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/0022-3514.75.2.332` | 1998 | R08 | 2 | Y |
| 85 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/0022-3514.80.6.1011` | 2001 | R06 | 2 | Y |
| 86 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/0022-3514.94.5.808` | 2008 | R03 | 2 | Y |
| 87 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/0033-2909.102.3.390` | 1987 | R10 | 2 | Y |
| 88 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/0033-2909.116.3.457` | 1994 | R10 | 2 | Y |
| 89 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/0033-295x.102.2.246` | 1995 | R06 | 2 | Y |
| 90 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/0033-295x.93.2.119` | 1986 | R03 | 2 | Y |
| 91 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/0893-3200.19.2.314` | 2005 | R06 | 2 | Y |
| 92 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/1089-2680.2.2.175` | 1998 | R08 | 2 | Y |
| 93 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/a0019651` | 2010 | R06 | 2 | Y |
| 94 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/a0024061` | 2011 | R17 | 2 | Y |
| 95 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/a0029052` | 2012 | R06 | 2 | Y |
| 96 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/amp0000191` | 2018 | R01 | 2 | Y |
| 97 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/bul0000349` | 2021 | R08 | 2 | Y |
| 98 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/gpr0000066` | 2016 | R06 | 2 | Y |
| 99 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/h0040084` | 1957 | R01 | 2 | Y |
| 100 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/h0046049` | 1956 | R17 | 2 | Y |
| 101 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/met0000285` | 2022 | R05 | 2 | Y |
| 102 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/met0000600` | 2026 | R05 | 2 | Y |
| 103 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/pspi0000266` | 2021 | R08 | 2 | Y |
| 104 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/pspp0000358` | 2021 | R05 | 2 | Y |
| 105 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/pspp0000551` | 2025 | R09 | 2 | Y |
| 106 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/pst0000172` | 2018 | R11 | 2 | Y |
| 107 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1038/s44159-026-00535-4` | 2026 | R03 | 2 | Y |
| 108 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1073/pnas.2209460119` | 2022 | R06 | 2 | Y |
| 109 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1080/00223890701268041` | 2007 | R03 | 2 | Y |
| 110 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1080/00224499.2015.1109581` | 2016 | R03 | 2 | Y |
| 111 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1080/00224499.2024.2417023` | 2024 | R03 | 2 | Y |
| 112 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1080/00926239608414655` | 1996 | R03 | 2 | Y |
| 113 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1080/10463283.2017.1333315` | 2017 | R08 | 2 | Y |
| 114 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1080/1047840x.2014.876909` | 2014 | R11 | 2 | Y |
| 115 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1080/10705511.2022.2065278` | 2022 | R05 | 2 | Y |
| 116 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1080/10705511.2024.2379495` | 2024 | R05 | 2 | Y |
| 117 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1080/14616734.2013.782654` | 2013 | R11 | 2 | Y |
| 118 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1086/230539` | 1994 | R10 | 2 | Y |
| 119 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1086/231213` | 1997 | R11 | 2 | Y |
| 120 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1093/sf/55.1.123` | 1976 | R10 | 2 | Y |
| 121 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1098/rspb.2011.0805` | 2011 | R10 | 2 | Y |
| 122 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1111/1467-6494.00143` | 2001 | R03 | 2 | Y |
| 123 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1111/1467-8721.00070` | 2000 | R14 | 2 | Y |
| 124 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1111/1475-6811.00017` | 2002 | R14 | 2 | Y |
| 125 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1111/famp.12811` | 2022 | R10 | 2 | Y |
| 126 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1111/fare.12885` | 2023 | R09 | 2 | Y |
| 127 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1111/j.1467-6494.2011.00734.x` | 2012 | R03 | 2 | Y |
| 128 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1111/j.1475-6811.1997.tb00145.x` | 1997 | R02 | 2 | Y |
| 129 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1111/j.1475-6811.2001.tb00034.x` | 2001 | R10 | 2 | Y |
| 130 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1111/j.1475-6811.2007.00173.x` | 2007 | R17 | 2 | Y |
| 131 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1111/j.1475-6811.2009.01221.x` | 2009 | R03 | 2 | Y |
| 132 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1111/j.1475-6811.2010.01282.x` | 2010 | R08 | 2 | Y |
| 133 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1111/j.1545-5300.1983.00069.x` | 1983 | R11 | 2 | Y |
| 134 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1111/j.1571-9979.2003.tb00771.x` | 2003 | R08 | 2 | Y |
| 135 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1111/j.1741-3737.2006.00284.x` | 2006 | R03 | 2 | Y |
| 136 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1111/j.1741-3737.2007.00468.x` | 2008 | R11 | 2 | Y |
| 137 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1111/j.1747-9991.2006.00035.x` | 2006 | R08 | 2 | Y |
| 138 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1111/j.1933-1592.2006.tb00586.x` | 2006 | R08 | 2 | Y |
| 139 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1111/jomf.12201` | 2015 | R11 | 2 | Y |
| 140 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1111/pere.12072` | 2015 | R03 | 2 | Y |
| 141 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1111/pere.12133` | 2016 | R11 | 2 | Y |
| 142 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1111/pere.12447` | 2022 | R10 | 2 | Y |
| 143 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1111/spc3.12308` | 2017 | R01 | 2 | Y |
| 144 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1126/sciadv.aap9815` | 2018 | R11 | 2 | Y |
| 145 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1126/science.1185231` | 2010 | R12 | 2 | Y |
| 146 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1145/2382577.2382579` | 2012 | R16 | 2 | Y |
| 147 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1145/2815620` | 2015 | R12 | 2 | Y |
| 148 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1145/3586183.3606763` | 2023 | R12 | 2 | Y |
| 149 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1145/3618260.3649777` | 2024 | R07 | 2 | Y |
| 150 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1146/annurev-psych-010416-044153` | 2017 | R10 | 2 | Y |
| 151 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1146/annurev.psych.093008.100318` | 2010 | R01 | 2 | Y |
| 152 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1162/coli_a_00502` | 2024 | R13 | 2 | Y |
| 153 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/0022022104266105` | 2004 | R03 | 2 | Y |
| 154 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/0049124118789708` | 2018 | R13 | 2 | Y |
| 155 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/0146167211432764` | 2012 | R08 | 2 | Y |
| 156 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/0146167220921717` | 2020 | R10 | 2 | Y |
| 157 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/01461672221113981` | 2022 | R06 | 2 | Y |
| 158 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/0146167297234003` | 1997 | R11 | 2 | Y |
| 159 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/0192513x18758343` | 2018 | R17 | 2 | Y |
| 160 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/0192513x211064876` | 2022 | R11 | 2 | Y |
| 161 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/0265407507086804` | 2008 | R11 | 2 | Y |
| 162 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/0265407510378125` | 2010 | R03 | 2 | Y |
| 163 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/0265407512465221` | 2012 | R17 | 2 | Y |
| 164 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/0265407515584493` | 2015 | R17 | 2 | Y |
| 165 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/0265407518822783` | 2019 | R02 | 2 | Y |
| 166 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/02654075211017675` | 2021 | R08 | 2 | Y |
| 167 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/02654075211028654` | 2021 | R03 | 2 | Y |
| 168 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/026540758800500207` | 1988 | R10 | 2 | Y |
| 169 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/0265407589064001` | 1989 | R03 | 2 | Y |
| 170 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/10693971211068971` | 2022 | R13 | 2 | Y |
| 171 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/25152459241302300` | 2025 | R09 | 2 | Y |
| 172 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1186/1471-2288-12-46` | 2012 | R07 | 2 | Y |
| 173 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1186/s12955-020-01526-6` | 2020 | R13 | 2 | Y |
| 174 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1214/20-aoas1322` | 2020 | R13 | 2 | Y |
| 175 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1257/aer.p20161046` | 2016 | R07 | 2 | Y |
| 176 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1371/journal.pone.0129478` | 2015 | R03 | 2 | Y |
| 177 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1509/jmkr.44.2.175` | 2007 | R13 | 2 | Y |
| 178 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1609/aaai.v31i1.10730` | 2017 | R13 | 2 | Y |
| 179 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.18564/jasss.1912` | 2012 | R12 | 2 | Y |
| 180 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.18564/jasss.1929` | 2012 | R12 | 2 | Y |
| 181 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.18564/jasss.2274` | 2013 | R12 | 2 | Y |
| 182 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.18653/v1/2020.acl-main.442` | 2020 | R17 | 2 | Y |
| 183 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.18653/v1/2024.acl-long.698` | 2024 | R12 | 2 | Y |
| 184 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.18653/v1/2025.acl-long.1203` | 2025 | R12 | 2 | Y |
| 185 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.21105/joss.07668` | 2025 | R12 | 2 | Y |
| 186 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.2307/2092623` | 1960 | R10 | 2 | Y |
| 187 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.2307/2578749` | 1987 | R10 | 2 | Y |
| 188 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.2307/349726` | 1964 | R03 | 2 | Y |
| 189 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.2307/350547` | 1976 | R03 | 2 | Y |
| 190 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.2307/351903` | 1980 | R03 | 2 | Y |
| 191 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.2307/352650` | 1988 | R03 | 2 | Y |
| 192 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.2307/352993` | 1991 | R11 | 2 | Y |
| 193 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.2307/353412` | 1995 | R07 | 2 | Y |
| 194 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.2466/pr0.1985.56.3.1001` | 1985 | R03 | 2 | Y |
| 195 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.2466/pr0.67.5.219-224` | 1990 | R03 | 2 | Y |
| 196 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.3389/fphy.2018.00021` | 2018 | R06 | 2 | Y |
| 197 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.3389/fpsyg.2019.01249` | 2019 | R13 | 2 | Y |
| 198 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.3389/fpsyg.2022.912978` | 2022 | R17 | 2 | Y |
| 199 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.3389/fpsyg.2023.1176067` | 2023 | R01 | 2 | Y |
| 200 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.3389/fpsyt.2025.1504306` | 2025 | R14 | 2 | Y |
| 201 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.5964/ijpr.v6i1.88` | 2012 | R03 | 2 | Y |
| 202 | `PEER_REVIEWED_PRIMARY` | `https://www.ijcai.org/proceedings/07/papers/083.pdf |  | R07 | 2 | N |
| 203 | `PEER_REVIEWED_PRIMARY` | `https://www.jasss.org/12/1/1.html |  | R12 | 2 | N |
| 204 | `PEER_REVIEWED_PRIMARY` | `https://www.jasss.org/16/4/6.html |  | R12 | 2 | N |
| 205 | `PEER_REVIEWED_PRIMARY` | `https://www.jasss.org/3/1/1.html |  | R12 | 2 | N |
| 206 | `PEER_REVIEWED_PRIMARY` | `https://www.jasss.org/3/1/2.html |  | R12 | 2 | N |
| 207 | `PEER_REVIEWED_PRIMARY` | `https://www.ntnu.no/ojs/index.php/norepid/article/view/1821/1818 |  | R03 | 2 | N |
| 208 | `PEER_REVIEWED_PRIMARY` | `https://www.sciencedirect.com/science/article/abs/pii/s1743609515336584 |  | R03 | 2 | N |
| 209 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1007/s10508-017-1015-4` | 2017 | R01 | 1 | Y |
| 210 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1007/s10994-020-05910-7` | 2020 | R16 | 1 | Y |
| 211 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1007/s12144-025-08223-x` | 2025 | R14 | 1 | Y |
| 212 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1016/j.adolescence.2010.07.008` | 2010 | R01 | 1 | Y |
| 213 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1016/j.jml.2012.11.001` | 2013 | R16 | 1 | Y |
| 214 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1016/j.neuroimage.2014.01.060` | 2014 | R16 | 1 | Y |
| 215 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1016/j.neuroimage.2017.06.061` | 2018 | R16 | 1 | Y |
| 216 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1016/j.socnet.2009.02.004` | 2010 | R12 | 1 | Y |
| 217 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1026/0932-4089/a000478` | 2026 | R05 | 1 | Y |
| 218 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/0003-066x.60.2.170` | 2005 | R16 | 1 | Y |
| 219 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/0022-3514.56.5.784` | 1989 | R02 | 1 | Y |
| 220 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/0022-3514.66.5.857` | 1994 | R07 | 1 | Y |
| 221 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/0022-3514.72.5.1177` | 1997 | R01 | 1 | Y |
| 222 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/0022-3514.74.4.939` | 1998 | R01 | 1 | Y |
| 223 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/0022-3514.78.6.1053` | 2000 | R01 | 1 | Y |
| 224 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/0022-3514.80.6.972` | 2001 | R01 | 1 | Y |
| 225 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/0022-3514.88.3.480` | 2005 | R01 | 1 | Y |
| 226 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/0022-3514.92.3.458` | 2007 | R01 | 1 | Y |
| 227 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/0022-3514.92.4.678` | 2007 | R01 | 1 | Y |
| 228 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/1082-989x.10.1.3` | 2005 | R05 | 1 | Y |
| 229 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/dev0000902` | 2020 | R05 | 1 | Y |
| 230 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/met0000062` | 2016 | R05 | 1 | Y |
| 231 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/met0000239` | 2020 | R05 | 1 | Y |
| 232 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/met0000250` | 2020 | R05 | 1 | Y |
| 233 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/met0000624` | 2025 | R16 | 1 | Y |
| 234 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/met0000720` | 2025 | R05 | 1 | Y |
| 235 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1037/pas0000275` | 2016 | R05 | 1 | Y |
| 236 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1038/s41562-016-0021` | 2017 | R16 | 1 | Y |
| 237 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1038/s41562-016-0034` | 2017 | R16 | 1 | Y |
| 238 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1073/pnas.1708274114` | 2018 | R16 | 1 | Y |
| 239 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1073/pnas.2305016120` | 2023 | R13 | 1 | Y |
| 240 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1080/00223891.2018.1521418` | 2019 | R05 | 1 | Y |
| 241 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1080/00273171.2018.1446819` | 2018 | R05 | 1 | Y |
| 242 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1080/01621459.2023.2197686` | 2023 | R16 | 1 | Y |
| 243 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1080/10705511.2016.1253479` | 2016 | R05 | 1 | Y |
| 244 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1080/10705511.2017.1406803` | 2017 | R05 | 1 | Y |
| 245 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1080/10705511.2019.1626733` | 2019 | R05 | 1 | Y |
| 246 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1080/10705511.2020.1784738` | 2020 | R05 | 1 | Y |
| 247 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1080/10705511.2020.1821690` | 2020 | R05 | 1 | Y |
| 248 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1080/10705511.2023.2191292` | 2023 | R05 | 1 | Y |
| 249 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1080/10705511.2024.2316586` | 2024 | R05 | 1 | Y |
| 250 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1080/10705511.2024.2355579` | 2024 | R05 | 1 | Y |
| 251 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1080/10705511.2024.2406510` | 2024 | R05 | 1 | Y |
| 252 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1080/10705511.2025.2608122` | 2026 | R05 | 1 | Y |
| 253 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1086/226863` | 1979 | R05 | 1 | Y |
| 254 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1111/cdev.12660` | 2017 | R05 | 1 | Y |
| 255 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1111/ecog.02881` | 2017 | R16 | 1 | Y |
| 256 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1111/j.1467-8721.2009.01657.x` | 2009 | R14 | 1 | Y |
| 257 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1111/j.1467-9280.2009.02388.x` | 2009 | R01 | 1 | Y |
| 258 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1111/j.1475-6811.1994.tb00068.x` | 1994 | R02 | 1 | Y |
| 259 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1111/j.1475-6811.1996.tb00116.x` | 1996 | R01 | 1 | Y |
| 260 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1111/j.1475-6811.1999.tb00202.x` | 1999 | R05 | 1 | Y |
| 261 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1111/jedm.12000` | 2013 | R05 | 1 | Y |
| 262 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1111/pere.12060` | 2014 | R14 | 1 | Y |
| 263 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1111/spc3.70042` | 2025 | R14 | 1 | Y |
| 264 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1111/spc3.70045` | 2025 | R14 | 1 | Y |
| 265 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1126/science.aaa9375` | 2015 | R16 | 1 | Y |
| 266 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1145/3703155` | 2025 | R13 | 1 | Y |
| 267 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1146/annurev-psych-010418-102813` | 2019 | R14 | 1 | Y |
| 268 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1146/annurev-psych-012224-025712` | 2025 | R00 | 1 | Y |
| 269 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1146/annurev-psych-040325-025418` | 2026 | R16 | 1 | Y |
| 270 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1146/annurev-statistics-060116-054035` | 2017 | R12 | 1 | Y |
| 271 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1162/coli.07-034-r2` | 2008 | R13 | 1 | Y |
| 272 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/0146167203252807` | 2003 | R01 | 1 | Y |
| 273 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/0146167210383045` | 2010 | R01 | 1 | Y |
| 274 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/019251391012001003` | 1991 | R05 | 1 | Y |
| 275 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/0192513x10385788` | 2010 | R01 | 1 | Y |
| 276 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/0265407500173006` | 2000 | R14 | 1 | Y |
| 277 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/08902070221085877` | 2022 | R14 | 1 | Y |
| 278 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/0956797611417632` | 2011 | R16 | 1 | Y |
| 279 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/0956797620980754` | 2021 | R01 | 1 | Y |
| 280 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/096228029900800105` | 1999 | R05 | 1 | Y |
| 281 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/1059712314547709` | 2014 | R14 | 1 | Y |
| 282 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/16094069241231168` | 2024 | R14 | 1 | Y |
| 283 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/1745691616658637` | 2016 | R05 | 1 | Y |
| 284 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/1948550617693063` | 2017 | R05 | 1 | Y |
| 285 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/2515245919882903` | 2020 | R16 | 1 | Y |
| 286 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/25152459251351286` | 2025 | R05 | 1 | Y |
| 287 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1177/25152459251410153` | 2026 | R14 | 1 | Y |
| 288 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1214/14-sts501` | 2014 | R16 | 1 | Y |
| 289 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.1214/16-aoas1005` | 2017 | R16 | 1 | Y |
| 290 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.12758/mda.2013.013` | 2013 | R13 | 1 | Y |
| 291 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.18653/v1/2025.emnlp-main.144` | 2025 | R13 | 1 | Y |
| 292 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.2117/psysoc.2016.1` | 2016 | R02 | 1 | Y |
| 293 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.21248/jlcl.38.2025.289` | 2025 | R13 | 1 | Y |
| 294 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.2478/jos-2022-0041` | 2022 | R13 | 1 | Y |
| 295 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.3102/10769986024002179` | 1999 | R05 | 1 | Y |
| 296 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.3389/fpsyg.2014.00452` | 2014 | R14 | 1 | Y |
| 297 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.3390/ejihpe12070054` | 2022 | R05 | 1 | Y |
| 298 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.3390/ijerph17249306` | 2020 | R01 | 1 | Y |
| 299 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.3724/sp.j.1041.2016.00989` | 2016 | R02 | 1 | Y |
| 300 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.5465/amr.1998.926620` | 1998 | R01 | 1 | Y |
| 301 | `PEER_REVIEWED_PRIMARY` | `https://doi.org/10.5465/amr.2007.24348410` | 2007 | R01 | 1 | Y |
| 302 | `PEER_REVIEWED_PRIMARY` | `https://academic.oup.com/jcr/article/47/1/1/5610529 |  | R08 | 1 | N |
| 303 | `PEER_REVIEWED_PRIMARY` | `https://d.docksci.com/download/effects-of-erotica-upon-mens-and-womens-loving-and-liking-responses-for-their-pa_5eb14347097c473e668b4589.html |  | R02 | 1 | N |
| 304 | `PEER_REVIEWED_PRIMARY` | `https://d.docksci.com/download/measurement-invariance-of-the-experiences-in-close-relationships-questionnaire-a_5acc759ed64ab2a9e8109124.html |  | R03 | 1 | N |
| 305 | `PEER_REVIEWED_PRIMARY` | `https://jmlr.org/papers/v11/raykar10a.html |  | R07 | 1 | N |
| 306 | `PEER_REVIEWED_PRIMARY` | `https://jmlr.org/papers/volume24/21-0048/21-0048.pdf |  | R07 | 1 | N |
| 307 | `PEER_REVIEWED_PRIMARY` | `https://jmlr.org/papers/volume26/24-0119/24-0119.pdf |  | R05 | 1 | N |
| 308 | `PEER_REVIEWED_PRIMARY` | `https://journal.psych.ac.cn/xlxb/cn/y2006/v38/i03/399 |  | R02 | 1 | N |
| 309 | `PEER_REVIEWED_PRIMARY` | `https://proceedings.neurips.cc/paper_files/paper/2021/file/6a26c75d6a576c94654bfc4dda548c72-paper.pdf |  | R07 | 1 | N |
| 310 | `PEER_REVIEWED_PRIMARY` | `https://www.apa.org/pubs/journals/releases/fam-26-2-236.pdf |  | R08 | 1 | N |
| 311 | `PEER_REVIEWED_PRIMARY` | `https://www.cambridge.org/core/journals/episteme/article/dogmatism-and-dogmatism/3bc37e2a4ce689a496a24ca7dc6d7568 |  | R08 | 1 | N |
| 312 | `PEER_REVIEWED_PRIMARY` | `https://www.cambridge.org/core/journals/journal-of-relationships-research/article/abs/crosscultural-examination-of-the-experiences-in-close-relationships-revised-general-short-form-ecrrgsf-in-an-australian-and-a-chinese-sample/940d0c6faee9f9708308aed7c544caf0 |  | R03 | 1 | N |
| 313 | `PEER_REVIEWED_PRIMARY` | `https://www.cambridge.org/core/journals/journal-of-relationships-research/article/abs/does-relationship-satisfaction-always-mean-satisfaction-development-of-the-couple-relationship-satisfaction-scale/585e7e514f5d9ada1ebbd34a3b75429e |  | R03 | 1 | N |
| 314 | `PEER_REVIEWED_PRIMARY` | `https://www.cambridge.org/core/journals/journal-of-the-economic-science-association/article/abs/private-lives-experimental-evidence-on-information-completeness-in-spousal-preferences/ca87af7d4c687ea5fac39d666637e891 |  | R08 | 1 | N |
| 315 | `PEER_REVIEWED_PRIMARY` | `https://www.jasss.org/10/2/8.html |  | R12 | 1 | N |
| 316 | `PEER_REVIEWED_PRIMARY` | `https://www.jasss.org/16/1/6.html |  | R14 | 1 | N |
| 317 | `PEER_REVIEWED_PRIMARY` | `https://www.jasss.org/18/4/4.html |  | R12 | 1 | N |
| 318 | `PEER_REVIEWED_PRIMARY` | `https://www.mdpi.com/1660-4601/17/19/7178 |  | R02 | 1 | N |
| 319 | `PEER_REVIEWED_PRIMARY` | `https://www.sciencedirect.com/science/article/abs/pii/s0022103118304529 |  | R08 | 1 | N |
| 320 | `PEER_REVIEWED_REVIEW` | `https://doi.org/10.1007/s10508-009-9556-9` | 2010 | R01 R02 R03 | 5 | Y |
| 321 | `PEER_REVIEWED_REVIEW` | `https://doi.org/10.1007/3-540-45547-7_3` | 2001 | R02 | 6 | Y |
| 322 | `PEER_REVIEWED_REVIEW` | `https://doi.org/10.1111/joop.12395` | 2022 | R02 | 4 | Y |
| 323 | `PEER_REVIEWED_REVIEW` | `https://doi.org/10.1177/0265407508096700` | 2008 | R02 | 4 | Y |
| 324 | `PEER_REVIEWED_REVIEW` | `https://doi.org/10.1007/978-1-4020-5839-4` | 2008 | R08 | 3 | Y |
| 325 | `PEER_REVIEWED_REVIEW` | `https://doi.org/10.1017/9781108131490.003` | 2019 | R10 | 3 | Y |
| 326 | `PEER_REVIEWED_REVIEW` | `https://doi.org/10.1111/j.1741-3737.2002.00568.x` | 2002 | R11 | 3 | Y |
| 327 | `PEER_REVIEWED_REVIEW` | `https://doi.org/10.1016/b978-0-444-51726-5.50015-7` | 2008 | R07 | 2 | Y |
| 328 | `PEER_REVIEWED_REVIEW` | `https://doi.org/10.1016/j.cpr.2015.07.002` | 2015 | R10 | 2 | Y |
| 329 | `PEER_REVIEWED_REVIEW` | `https://doi.org/10.1016/j.physbeh.2021.113391` | 2021 | R03 | 2 | Y |
| 330 | `PEER_REVIEWED_REVIEW` | `https://doi.org/10.1017/cbo9780511996481.027` | 2014 | R10 | 2 | Y |
| 331 | `PEER_REVIEWED_REVIEW` | `https://doi.org/10.1037/0022-0167.38.2.139` | 1991 | R11 | 2 | Y |
| 332 | `PEER_REVIEWED_REVIEW` | `https://doi.org/10.1037/a0022441` | 2011 | R03 | 2 | Y |
| 333 | `PEER_REVIEWED_REVIEW` | `https://doi.org/10.1080/03637751.2013.813632` | 2013 | R06 | 2 | Y |
| 334 | `PEER_REVIEWED_REVIEW` | `https://doi.org/10.1177/0265407598152004` | 1998 | R10 | 2 | Y |
| 335 | `PEER_REVIEWED_REVIEW` | `https://doi.org/10.1177/1088868316628405` | 2016 | R03 | 2 | Y |
| 336 | `PEER_REVIEWED_REVIEW` | `https://doi.org/10.1177/109442810031002` | 2000 | R17 | 2 | Y |
| 337 | `PEER_REVIEWED_REVIEW` | `https://doi.org/10.1186/s12874-018-0570-2` | 2018 | R03 | 2 | Y |
| 338 | `PEER_REVIEWED_REVIEW` | `https://doi.org/10.3389/fpsyg.2019.00571` | 2019 | R10 | 2 | Y |
| 339 | `PEER_REVIEWED_REVIEW` | `https://doi.org/10.4135/9781483327648.n3` | 1996 | R10 | 2 | Y |
| 340 | `PEER_REVIEWED_REVIEW` | `https://doi.org/10.4324/9780203311851-29` | 2004 | R10 | 2 | Y |
| 341 | `PEER_REVIEWED_REVIEW` | `https://doi.org/10.4324/9780203732496-5` | 2018 | R03 | 2 | Y |
| 342 | `PEER_REVIEWED_REVIEW` | `https://doi.org/10.1016/j.dr.2016.06.004` | 2016 | R05 | 1 | Y |
| 343 | `PEER_REVIEWED_REVIEW` | `https://doi.org/10.1037/0021-9010.88.5.879` | 2003 | R16 | 1 | Y |
| 344 | `PEER_REVIEWED_REVIEW` | `https://doi.org/10.1111/1468-5884.00030` | 2003 | R02 | 1 | Y |
| 345 | `PEER_REVIEWED_REVIEW` | `https://doi.org/10.1126/science.1116681` | 2005 | R12 | 1 | Y |
| 346 | `PEER_REVIEWED_REVIEW` | `https://doi.org/10.1177/0265407510389126` | 2010 | R02 | 1 | Y |
| 347 | `PEER_REVIEWED_REVIEW` | `https://doi.org/10.4324/9780203848852.ch17` |  | R12 | 1 | Y |
| 348 | `PEER_REVIEWED_REVIEW` | ISBN 9780471034735 |  | R10 | 1 | form-only |
| 349 | `PEER_REVIEWED_REVIEW` | `https://assets.cambridge.org/97811071/92614/excerpt/9781107192614_excerpt.pdf |  | R10 | 1 | N |
| 350 | `PEER_REVIEWED_REVIEW` | `https://sk.sagepub.com/ency/edvol/download/humanrelationships/chpt/interpersonal-process-model-intimacy.pdf |  | R10 | 1 | N |
| 351 | `PEER_REVIEWED_LANDING` | `https://statmodel.com/download/webtalk4.pdf |  | R05 | 2 | N |
| 352 | `PREPRINT` | `arXiv:0911.0013` |  | R09 | 6 | form-only |
| 353 | `PREPRINT` | `arXiv:2603.21036` |  | R13 | 5 | form-only |
| 354 | `PREPRINT` | `arXiv:2603.22735` |  | R13 | 5 | form-only |
| 355 | `PREPRINT` | `arXiv:2602.13224` |  | R13 | 4 | form-only |
| 356 | `PREPRINT` | `arXiv:2211.01503` |  | R07 | 3 | form-only |
| 357 | `PREPRINT` | `arXiv:2304.03442` |  | R12 | 3 | form-only |
| 358 | `PREPRINT` | `arXiv:2312.03664` |  | R12 | 3 | form-only |
| 359 | `PREPRINT` | `arXiv:2506.20793` |  | R13 | 3 | form-only |
| 360 | `PREPRINT` | `arXiv:2603.15892` |  | R13 | 3 | form-only |
| 361 | `PREPRINT` | `arXiv:2604.23178` |  | R13 | 3 | form-only |
| 362 | `PREPRINT` | `arXiv:2609.22133` |  | R13 | 3 | form-only |
| 363 | `PREPRINT` | `arXiv:2004.05442` |  | R13 | 2 | form-only |
| 364 | `PREPRINT` | `arXiv:2112.14476` |  | R13 | 2 | form-only |
| 365 | `PREPRINT` | `arXiv:2306.01157` |  | R07 | 2 | form-only |
| 366 | `PREPRINT` | `arXiv:2306.05685` |  | R13 | 2 | form-only |
| 367 | `PREPRINT` | `arXiv:2311.14648` |  | R07 | 2 | form-only |
| 368 | `PREPRINT` | `arXiv:2402.02099` |  | R13 | 2 | form-only |
| 369 | `PREPRINT` | `arXiv:2406.12934` |  | R13 | 2 | form-only |
| 370 | `PREPRINT` | `arXiv:2410.21819` |  | R13 | 2 | form-only |
| 371 | `PREPRINT` | `arXiv:2503.10671` |  | R13 | 2 | form-only |
| 372 | `PREPRINT` | `arXiv:2506.19467` |  | R13 | 2 | form-only |
| 373 | `PREPRINT` | `arXiv:2506.19468` |  | R13 | 2 | form-only |
| 374 | `PREPRINT` | `arXiv:2508.02866` |  | R13 | 2 | form-only |
| 375 | `PREPRINT` | `arXiv:2508.06709` |  | R13 | 2 | form-only |
| 376 | `PREPRINT` | `arXiv:2508.08591` |  | R13 | 2 | form-only |
| 377 | `PREPRINT` | `arXiv:2509.25532` |  | R13 | 2 | form-only |
| 378 | `PREPRINT` | `arXiv:2511.10457` |  | R14 | 2 | form-only |
| 379 | `PREPRINT` | `arXiv:2601.02627` |  | R13 | 2 | form-only |
| 380 | `PREPRINT` | `arXiv:2601.09065` |  | R13 | 2 | form-only |
| 381 | `PREPRINT` | `arXiv:2602.12247` |  | R13 | 2 | form-only |
| 382 | `PREPRINT` | `arXiv:2602.14743` |  | R13 | 2 | form-only |
| 383 | `PREPRINT` | `arXiv:2603.09985` |  | R13 | 2 | form-only |
| 384 | `PREPRINT` | `arXiv:2604.01457` |  | R13 | 2 | form-only |
| 385 | `PREPRINT` | `https://doi.org/10.1101/2025.11.15.25339520` | 2025 | R13 | 2 | Y |
| 386 | `PREPRINT` | `https://doi.org/10.31219/osf.io/gu8z7` | 2017 | R14 | 2 | Y |
| 387 | `PREPRINT` | `arXiv:1003.2804` |  | R05 | 1 | form-only |
| 388 | `PREPRINT` | `arXiv:1305.7345` |  | R07 | 1 | form-only |
| 389 | `PREPRINT` | `arXiv:1701.08673` |  | R09 | 1 | form-only |
| 390 | `PREPRINT` | `arXiv:1803.02324` |  | R13 | 1 | form-only |
| 391 | `PREPRINT` | `arXiv:1911.03876` |  | R14 | 1 | form-only |
| 392 | `PREPRINT` | `arXiv:2209.06899` |  | R13 | 1 | form-only |
| 393 | `PREPRINT` | `arXiv:2303.15056` |  | R13 | 1 | form-only |
| 394 | `PREPRINT` | `arXiv:2406.17675` |  | R14 | 1 | form-only |
| 395 | `PREPRINT` | `arXiv:2507.18890` |  | R13 | 1 | form-only |
| 396 | `PREPRINT` | `arXiv:2602.03334` |  | R13 | 1 | form-only |
| 397 | `PREPRINT` | `arXiv:2603.00704` |  | R07 | 1 | form-only |
| 398 | `PREPRINT` | `https://doi.org/10.31234/osf.io/dus42` | 2024 | R05 | 1 | Y |
| 399 | `GREY_OFFICIAL` | `https://github.com/datasets/speed-dating |  | R04 R16 | 3 | N |
| 400 | `GREY_OFFICIAL` | `https://pmc.ncbi.nlm.nih.gov/articles/pmc12316384 |  | R02 R03 | 3 | N |
| 401 | `GREY_OFFICIAL` | `https://davidakenny.net/ip/srmip.htm |  | R00 R10 | 2 | N |
| 402 | `GREY_OFFICIAL` | `https://cran.r-project.org/web/packages/rsiena |  | R12 | 3 | N |
| 403 | `GREY_OFFICIAL` | `https://par.nsf.gov/biblio/10223261-couple-simulation-novel-approach-evaluating-models-human-mate-choice |  | R12 | 3 | N |
| 404 | `GREY_OFFICIAL` | `https://ppw.kuleuven.be/okp/esmhandbook.php |  | R05 | 3 | N |
| 405 | `GREY_OFFICIAL` | `https://www.intensivelongitudinal.com/index.html |  | R05 | 3 | N |
| 406 | `GREY_OFFICIAL` | `https://doi.org/10.3386/w30439` | 2022 | R13 | 2 | Y |
| 407 | `GREY_OFFICIAL` | `https://cran.r-project.org/package=ctsem |  | R05 | 2 | N |
| 408 | `GREY_OFFICIAL` | `https://cran.r-project.org/package=mirt |  | R05 | 2 | N |
| 409 | `GREY_OFFICIAL` | `https://files.eric.ed.gov/fulltext/ed265604.pdf |  | R03 | 2 | N |
| 410 | `GREY_OFFICIAL` | `https://github.com/google-deepmind/concordia |  | R12 | 2 | N |
| 411 | `GREY_OFFICIAL` | `https://github.com/joonspk-research/generative_agents |  | R12 | 2 | N |
| 412 | `GREY_OFFICIAL` | `https://github.com/juliadynamics/agents.jl |  | R12 | 2 | N |
| 413 | `GREY_OFFICIAL` | `https://github.com/juryxy/juspace |  | R12 | 2 | N |
| 414 | `GREY_OFFICIAL` | `https://github.com/mesa/mesa |  | R12 | 2 | N |
| 415 | `GREY_OFFICIAL` | `https://github.com/repast/repast.simphony |  | R12 | 2 | N |
| 416 | `GREY_OFFICIAL` | `https://github.com/tsinghua-fib-lab/agentsociety |  | R12 | 2 | N |
| 417 | `GREY_OFFICIAL` | `https://jeroendmulder.github.io/ri-clpm |  | R05 | 2 | N |
| 418 | `GREY_OFFICIAL` | `https://matsim.org |  | R12 | 2 | N |
| 419 | `GREY_OFFICIAL` | `https://pmc.ncbi.nlm.nih.gov/articles/pmc12761549 |  | R03 | 2 | N |
| 420 | `GREY_OFFICIAL` | `https://pmc.ncbi.nlm.nih.gov/articles/pmc2861288 |  | R03 | 2 | N |
| 421 | `GREY_OFFICIAL` | `https://pubmed.ncbi.nlm.nih.gov/23356467 |  | R03 | 2 | N |
| 422 | `GREY_OFFICIAL` | `https://repast.github.io |  | R12 | 2 | N |
| 423 | `GREY_OFFICIAL` | `https://scales.arabpsychology.com/s/relationship-scales-questionnaire-rsq |  | R03 | 2 | N |
| 424 | `GREY_OFFICIAL` | `https://stacks.cdc.gov/view/cdc/230061 |  | R03 | 2 | N |
| 425 | `GREY_OFFICIAL` | `https://www.fz-juelich.de/en/inm/inm-7/resources/tools/juspace |  | R12 | 2 | N |
| 426 | `GREY_OFFICIAL` | `https://www.jars.network |  | R05 | 2 | N |
| 427 | `GREY_OFFICIAL` | `https://www.statmodel.com/download/ri-clpm.pdf |  | R05 | 2 | N |
| 428 | `GREY_OFFICIAL` | `https://www.w3.org/tr/prov-primer |  | R13 | 2 | N |
| 429 | `GREY_OFFICIAL` | `https://davidakenny.shinyapps.io/apim_mm |  | R05 | 1 | N |
| 430 | `GREY_OFFICIAL` | `https://github.com/cdriveraus/ctsem |  | R05 | 1 | N |
| 431 | `GREY_OFFICIAL` | `https://github.com/repast/repast.hpc |  | R12 | 1 | N |
| 432 | `GREY_OFFICIAL` | `https://github.com/repast/repast4py |  | R12 | 1 | N |
| 433 | `GREY_OFFICIAL` | `https://iep.utm.edu/dynamic-epistemic-logic |  | R08 | 1 | N |
| 434 | `GREY_OFFICIAL` | `https://jeroendmulder.github.io/ri-clpm/faq.html |  | R05 | 1 | N |
| 435 | `GREY_OFFICIAL` | `https://matsim.org/docs |  | R12 | 1 | N |
| 436 | `GREY_OFFICIAL` | `https://philarchive.org/archive/borosd-2 |  | R08 | 1 | N |
| 437 | `GREY_OFFICIAL` | `https://philarchive.org/archive/lajkat |  | R08 | 1 | N |
| 438 | `GREY_OFFICIAL` | `https://philarchive.org/archive/steeti-4 |  | R08 | 1 | N |
| 439 | `GREY_OFFICIAL` | `https://plato.stanford.edu/entries/dynamic-epistemic |  | R08 | 1 | N |
| 440 | `GREY_OFFICIAL` | `https://plato.stanford.edu/entries/epistemic-paradoxes |  | R08 | 1 | N |
| 441 | `GREY_OFFICIAL` | `https://plato.stanford.edu/entries/testimony-episprob |  | R08 | 1 | N |
| 442 | `GREY_OFFICIAL` | `https://pmc.ncbi.nlm.nih.gov/articles/pmc12955757 |  | R08 | 1 | N |
| 443 | `GREY_OFFICIAL` | `https://pmc.ncbi.nlm.nih.gov/articles/pmc4304641 |  | R08 | 1 | N |
| 444 | `GREY_OFFICIAL` | `https://pmc.ncbi.nlm.nih.gov/articles/pmc6187488 |  | R14 | 1 | N |
| 445 | `GREY_OFFICIAL` | `https://pmc.ncbi.nlm.nih.gov/articles/pmc6512343 |  | R08 | 1 | N |
| 446 | `GREY_OFFICIAL` | `https://pmc.ncbi.nlm.nih.gov/articles/pmc7083591 |  | R12 | 1 | N |
| 447 | `GREY_OFFICIAL` | `https://pmc.ncbi.nlm.nih.gov/articles/pmc8895702 |  | R02 | 1 | N |
| 448 | `GREY_OFFICIAL` | `https://pmc.ncbi.nlm.nih.gov/articles/pmc9903246 |  | R08 | 1 | N |
| 449 | `GREY_OFFICIAL` | `https://pubmed.ncbi.nlm.nih.gov/11138762 |  | R14 | 1 | N |
| 450 | `GREY_OFFICIAL` | `https://pubmed.ncbi.nlm.nih.gov/18179329 |  | R02 | 1 | N |
| 451 | `GREY_OFFICIAL` | `https://pubmed.ncbi.nlm.nih.gov/25559192 |  | R14 | 1 | N |
| 452 | `GREY_OFFICIAL` | `https://pubmed.ncbi.nlm.nih.gov/28394141 |  | R08 | 1 | N |
| 453 | `GREY_OFFICIAL` | `https://pubmed.ncbi.nlm.nih.gov/29206485 |  | R03 | 1 | N |
| 454 | `GREY_OFFICIAL` | `https://pubmed.ncbi.nlm.nih.gov/35389716 |  | R00 | 1 | N |
| 455 | `GREY_OFFICIAL` | `https://replicationindex.com/2020/08/22/cross-lagged |  | R05 | 1 | N |
| 456 | `GREY_OFFICIAL` | `https://statmodel.com/download/dsem.pdf |  | R05 | 1 | N |
| 457 | `GREY_OFFICIAL` | `https://statmodel.com/download/rdsem.pdf |  | R05 | 1 | N |
| 458 | `GREY_OFFICIAL` | `https://www.natcom.org/publications-library/discovering-secrets-romantic-relationships |  | R08 | 1 | N |
| 459 | `GREY_OFFICIAL` | `https://www.nichd.nih.gov/research/supported/seccyd |  | R04 | 1 | N |
| 460 | `GREY_OFFICIAL` | `https://www.statmodel.com/download/reciprocalv3.pdf |  | R06 | 1 | N |
| 461 | `OFFICIAL_DATA` | `https://share-eric.eu/data/data-access/conditions-of-use |  | R04 R16 | 3 | N |
| 462 | `OFFICIAL_DATA` | `https://www.openml.org/d/40536 |  | R04 R16 | 3 | N |
| 463 | `OFFICIAL_DATA` | `https://doi.org/10.4232/pairfam.5678.14.2.0` | 2024 | R04 | 4 | Y |
| 464 | `OFFICIAL_DATA` | `https://doi.org/10.6103/share.w1.900` | 2024 | R04 | 2 | Y |
| 465 | `OFFICIAL_DATA` | `https://doi.org/10.6103/share.w8.900` | 2024 | R04 | 2 | Y |
| 466 | `OFFICIAL_DATA` | `https://access.gesis.org/dbk/52241 |  | R04 | 2 | N |
| 467 | `OFFICIAL_DATA` | `https://access.gesis.org/dbk/53708 |  | R04 | 2 | N |
| 468 | `OFFICIAL_DATA` | `https://access.gesis.org/dbk/69762 |  | R04 | 2 | N |
| 469 | `OFFICIAL_DATA` | `https://addhealth.cpc.unc.edu/conditions-of-use |  | R04 | 2 | N |
| 470 | `OFFICIAL_DATA` | `https://addhealth.cpc.unc.edu/documentation |  | R04 | 2 | N |
| 471 | `OFFICIAL_DATA` | `https://addhealth.cpc.unc.edu/documentation/data-documentation |  | R04 | 2 | N |
| 472 | `OFFICIAL_DATA` | `https://americanfamilycohort.org/how-to-access-afc-data |  | R04 | 2 | N |
| 473 | `OFFICIAL_DATA` | `https://dhsprogram.com/data/guide-to-dhs-statistics/analyzing_dhs_data.htm |  | R04 | 2 | N |
| 474 | `OFFICIAL_DATA` | `https://hrs.isr.umich.edu |  | R04 | 2 | N |
| 475 | `OFFICIAL_DATA` | `https://hrs.isr.umich.edu/data-products |  | R04 | 2 | N |
| 476 | `OFFICIAL_DATA` | `https://hrs.isr.umich.edu/data-products/file-merge-reference |  | R04 | 2 | N |
| 477 | `OFFICIAL_DATA` | `https://hrs.isr.umich.edu/data-products/restricted-data/faqs |  | R04 | 2 | N |
| 478 | `OFFICIAL_DATA` | `https://liberalarts.utexas.edu/health-relationships-lab/about-harp |  | R04 | 2 | N |
| 479 | `OFFICIAL_DATA` | `https://paa2006.populationassociation.org/papers/60777 |  | R17 | 2 | N |
| 480 | `OFFICIAL_DATA` | `https://share-eric.eu/data/data-access |  | R04 | 2 | N |
| 481 | `OFFICIAL_DATA` | `https://share-eric.eu/data/data-documentation |  | R04 | 2 | N |
| 482 | `OFFICIAL_DATA` | `https://share-eric.eu/fileadmin/user_upload/release_guides/share_release_guide_9-0-0.pdf |  | R04 | 2 | N |
| 483 | `OFFICIAL_DATA` | `https://uasdata.usc.edu |  | R04 | 2 | N |
| 484 | `OFFICIAL_DATA` | `https://www.dhsprogram.com/data/merging-datasets.cfm |  | R04 | 2 | N |
| 485 | `OFFICIAL_DATA` | `https://www.growingup.co.nz |  | R04 | 2 | N |
| 486 | `OFFICIAL_DATA` | `https://www.growingup.co.nz/available-data-disclaimer |  | R04 | 2 | N |
| 487 | `OFFICIAL_DATA` | `https://www.growingup.co.nz/data-access-application-growing-up-in-new-zealand |  | R04 | 2 | N |
| 488 | `OFFICIAL_DATA` | `https://www.icpsr.umich.edu/web/dsdr/studies/21940 |  | R04 | 2 | N |
| 489 | `OFFICIAL_DATA` | `https://www.icpsr.umich.edu/web/dsdr/studies/6906 |  | R04 | 2 | N |
| 490 | `OFFICIAL_DATA` | `https://www.icpsr.umich.edu/web/icpsr/series/00233 |  | R04 | 2 | N |
| 491 | `OFFICIAL_DATA` | `https://www.icpsr.umich.edu/web/icpsr/series/193 |  | R04 | 2 | N |
| 492 | `OFFICIAL_DATA` | `https://www.icpsr.umich.edu/web/icpsr/studies/3370 |  | R04 | 2 | N |
| 493 | `OFFICIAL_DATA` | `https://www.icpsr.umich.edu/web/nacda/studies/37404 |  | R04 | 2 | N |
| 494 | `OFFICIAL_DATA` | `https://www.icpsr.umich.edu/web/nahdap/studies/38726 |  | R04 | 2 | N |
| 495 | `OFFICIAL_DATA` | `https://www.pairfam.de/en/data/data-access |  | R04 | 2 | N |
| 496 | `OFFICIAL_DATA` | `https://www.rand.org/health/surveys/fls/ifls/access.html |  | R04 | 2 | N |
| 497 | `OFFICIAL_DATA` | `https://www.rand.org/health/surveys/fls/ifls/datanotes.html |  | R04 | 2 | N |
| 498 | `OFFICIAL_DATA` | `https://www.rand.org/health/surveys/fls/ifls/study.html |  | R04 | 2 | N |
| 499 | `OFFICIAL_DATA` | `https://cls.ucl.ac.uk/wp-content/uploads/2017/02/cls_data_access_framework.pdf |  | R04 | 1 | N |
| 500 | `OFFICIAL_DATA` | `https://cls.ucl.ac.uk/wp-content/uploads/2017/02/webinar-slides-families-and-relationships-in-four-british-cohort-studies.pdf |  | R04 | 1 | N |
| 501 | `OFFICIAL_DATA` | `https://nsmshow.org |  | R04 | 1 | N |
| 502 | `OFFICIAL_DATA` | `https://share-eric.eu/data/faqs-support |  | R04 | 1 | N |
| 503 | `OFFICIAL_DATA` | `https://share-eric.eu/fileadmin/user_upload/other_publications/data_management_plan.pdf |  | R04 | 1 | N |
| 504 | `OFFICIAL_DATA` | `https://share.cerge-ei.cz/en/faq/index.html |  | R04 | 1 | N |
| 505 | `OFFICIAL_DATA` | `https://userforum.dhsprogram.com/index.php |  | R04 | 1 | N |
| 506 | `OFFICIAL_DATA` | `https://www.childandfamilydataarchive.org/cfda/cfda/series/193 |  | R04 | 1 | N |
| 507 | `OFFICIAL_DATA` | `https://www.demographic-research.org/volumes/vol51/30/files/readme.51-30.txt |  | R04 | 1 | N |
| 508 | `OFFICIAL_DATA` | `https://www.gesis.org/en/services/finding-and-accessing-data/selected-german-research-projects/pairfam |  | R04 | 1 | N |
| 509 | `OFFICIAL_DATA` | `https://www.icpsr.umich.edu/sites/icpsr/about/policies/large-language-models-and-ai |  | R04 | 1 | N |
| 510 | `OFFICIAL_DATA` | `https://www.icpsr.umich.edu/sites/icpsr/about/policies/redistribution |  | R04 | 1 | N |
| 511 | `OFFICIAL_DATA` | `https://www.icpsr.umich.edu/sites/nacda/home |  | R04 | 1 | N |
| 512 | `OFFICIAL_DATA` | `https://www.icpsr.umich.edu/sites/somar/somar-vde-overview-and-resources |  | R04 | 1 | N |
| 513 | `OFFICIAL_DATA` | `https://www.icpsr.umich.edu/web/dsdr/studies/22361 |  | R04 | 1 | N |
| 514 | `OFFICIAL_DATA` | `https://www.icpsr.umich.edu/web/dsdr/studies/22361/versions/v5 |  | R04 | 1 | N |
| 515 | `OFFICIAL_DATA` | `https://www.icpsr.umich.edu/web/nacda/studies/37404/datadocumentation |  | R04 | 1 | N |
| 516 | `OFFICIAL_DATA` | `https://www.icpsr.umich.edu/web/nacda/studies/37404/summary |  | R04 | 1 | N |
| 517 | `OFFICIAL_DATA` | `https://www.pairfam.de/en/data/data-structure |  | R04 | 1 | N |
| 518 | `DATASET` | `https://osf.io/8k7rf |  | R04 R16 | 4 | N |
| 519 | `DATASET` | `https://doi.org/10.1037/e512142015-146` | 2014 | R03 | 2 | Y |
| 520 | `DATASET` | `https://doi.org/10.13072/midss.484` |  | R03 | 2 | Y |
| 521 | `DATASET` | `https://www.comses.net/codebases/4490/releases/1.0.0 |  | R12 | 2 | N |
| 522 | `DATASET` | `https://doi.org/10.1037/t01997-000` | 1990 | R01 | 1 | Y |
| 523 | `DATASET` | `https://osf.io/k4fg9 |  | R14 | 1 | N |
| 524 | `DATASET` | `https://www.comses.net/codebases/4458/releases/1.0.0 |  | R12 | 1 | N |
| 525 | `POINTER_ONLY` | `https://greatergood.berkeley.edu/dacherkeltner/docs/keltner.power.psychreview.2003.pdf |  | R02 R10 | 2 | N |
| 526 | `POINTER_ONLY` | `https://quantdev.ssri.psu.edu/sites/qdev/files/apim_tutorial_2020.html |  | R05 | 3 | N |
| 527 | `POINTER_ONLY` | `https://ccpr.ucla.edu/wp-content/uploads/2024/04/re-examining-the-case-for-marriage_-variation-and-change-in-well-being-and-relationships.pdf |  | R17 | 2 | N |
| 528 | `POINTER_ONLY` | `https://dhsprogram.com/pubs/pdf/dhsg1/guide_to_dhs_statistics_dhs-8.pdf |  | R04 | 2 | N |
| 529 | `POINTER_ONLY` | `https://dhsprogram.com/pubs/pdf/mr19/mr19.pdf |  | R04 | 2 | N |
| 530 | `POINTER_ONLY` | `https://docs.iza.org/dp1811.pdf |  | R17 | 2 | N |
| 531 | `POINTER_ONLY` | `https://exa.ai/library/publication/8h8jd1sblrm |  | R03 | 2 | N |
| 532 | `POINTER_ONLY` | `https://exa.ai/library/publication/g32zr4m06b2 |  | R03 | 2 | N |
| 533 | `POINTER_ONLY` | `https://exa.ai/library/publication/rchtdhlk6gl |  | R03 | 2 | N |
| 534 | `POINTER_ONLY` | `https://gspp.berkeley.edu/archived/files/research/pdf/krosnick_et_al..pdf |  | R07 | 2 | N |
| 535 | `POINTER_ONLY` | `https://hrs.isr.umich.edu/sites/default/files/rda-forms/hrs-rda-micda-access-agreement.pdf |  | R04 | 2 | N |
| 536 | `POINTER_ONLY` | `https://labs.psychology.illinois.edu/~rcfraley/measures/brennan.html |  | R03 | 2 | N |
| 537 | `POINTER_ONLY` | `https://link.springer.com/content/pdf/10.1007/s11238-014-9448-x.pdf |  | R04 | 2 | N |
| 538 | `POINTER_ONLY` | `https://www.comses.net |  | R12 | 2 | N |
| 539 | `POINTER_ONLY` | `https://www.csun.edu/~snk1966/t.%20parsons%20the%20american%20family.pdf |  | R11 | 2 | N |
| 540 | `POINTER_ONLY` | `https://www.demographic-research.org/volumes/vol17/3/17-3.pdf |  | R14 | 2 | N |
| 541 | `POINTER_ONLY` | `https://www.econ.uiuc.edu/~roger/research/ebayes/isrprobrob.pdf |  | R07 | 2 | N |
| 542 | `POINTER_ONLY` | `https://www.rand.org/content/dam/rand/pubs/working_papers/wr1100/wr1143z2/rand_wr1143z2.pdf |  | R04 | 2 | N |
| 543 | `POINTER_ONLY` | `https://www.sas.rochester.edu/psy/people/faculty/reis_harry/assets/pdf/reisetal_2018_pprs.pdf |  | R03 | 2 | N |
| 544 | `POINTER_ONLY` | `https://www.statmodel.com |  | R05 | 2 | N |
| 545 | `POINTER_ONLY` | `https://www.stats.ox.ac.uk/~snijders/siena/rsiena_manual.pdf |  | R12 | 2 | N |
| 546 | `POINTER_ONLY` | `https://abcdocz.com/doc/1699137/the-relationship-power-inventory--development-and-validation |  | R02 | 1 | N |
| 547 | `POINTER_ONLY` | `https://amsterdamcooperationlab.com/wp-content/uploads/2020/11/ch0017_gerpott_v6_r2_clean.pdf |  | R10 | 1 | N |
| 548 | `POINTER_ONLY` | `https://anthonyongphd.wordpress.com/wp-content/uploads/2018/01/reis-clark-2013.pdf |  | R14 | 1 | N |
| 549 | `POINTER_ONLY` | `https://archive.org/details/familysocializat00parsrich |  | R11 | 1 | N |
| 550 | `POINTER_ONLY` | `https://aristotle.rutgers.edu/joomlatools-files/docman-files/fricker.pdf |  | R08 | 1 | N |
| 551 | `POINTER_ONLY` | `https://ceur-ws.org/vol-1283/paper_18.pdf |  | R08 | 1 | N |
| 552 | `POINTER_ONLY` | `https://classes.matthewjbrown.net/teaching-files/hps/kuhn-dogma.pdf |  | R08 | 1 | N |
| 553 | `POINTER_ONLY` | `https://cmapspublic.ihmc.us/rid=1k8z03ttp-15bmw7t-1h1v/biases_assumptions_accuracy.pdf |  | R10 | 1 | N |
| 554 | `POINTER_ONLY` | `https://content.sph.harvard.edu/wwwhsph/sites/1268/2024/04/hernanrobins_whatif_26apr24.pdf |  | R05 | 1 | N |
| 555 | `POINTER_ONLY` | `https://cpb-us-e1.wpmucdn.com/blogs.cornell.edu/dist/b/6819/files/2015/12/gilosavtskymdvc.98-copy-1ei0u8q.pdf |  | R08 | 1 | N |
| 556 | `POINTER_ONLY` | `https://crab.rutgers.edu/users/goertzel/romanticlove.htm |  | R02 | 1 | N |
| 557 | `POINTER_ONLY` | `https://cs.brown.edu/research/pubs/techreports/reports/94/cs94-40.pdf |  | R08 | 1 | N |
| 558 | `POINTER_ONLY` | `https://cs.brown.edu/research/pubs/techreports/reports/cs-95-19.html |  | R08 | 1 | N |
| 559 | `POINTER_ONLY` | `https://cuhigginslab.com/wp-content/papercite-data/pdf/higginsetal2021b.pdf |  | R08 | 1 | N |
| 560 | `POINTER_ONLY` | `https://cyrussamii.com/wp-content/uploads/2025/11/bk-eep-chp16.pdf |  | R05 | 1 | N |
| 561 | `POINTER_ONLY` | `https://d.docksci.com/download |  | R03 | 1 | N |
| 562 | `POINTER_ONLY` | `https://digitalcommons.kennesaw.edu/cgi/viewcontent.cgi |  | R03 | 1 | N |
| 563 | `POINTER_ONLY` | `https://earlyexperiences.psych.utah.edu/pubs/raby-categorical-or-dimensional-in%20press.pdf |  | R14 | 1 | N |
| 564 | `POINTER_ONLY` | `https://ecommons.cornell.edu/server/api/core/bitstreams/cb8acb6b-d8df-4509-8e74-130f6ebed363/content |  | R10 | 1 | N |
| 565 | `POINTER_ONLY` | `https://escholarship.org/content/qt79b7w6h3/qt79b7w6h3_nosplash_c15951d18f7e49039346f461cedf6f70.pdf |  | R08 | 1 | N |
| 566 | `POINTER_ONLY` | `https://exa.ai/library/publication/bnb4pgwv5g2 |  | R08 | 1 | N |
| 567 | `POINTER_ONLY` | `https://exa.ai/library/publication/gd2tq4y6n09 |  | R02 | 1 | N |
| 568 | `POINTER_ONLY` | `https://exa.ai/library/publication/k8s4n220k0w |  | R08 | 1 | N |
| 569 | `POINTER_ONLY` | `https://exa.ai/library/publication/mwlx3shqtwp |  | R08 | 1 | N |
| 570 | `POINTER_ONLY` | `https://exa.ai/library/publication/qc1n3tzxz6l |  | R08 | 1 | N |
| 571 | `POINTER_ONLY` | `https://exa.ai/library/publication/sjrdv14q7ck |  | R08 | 1 | N |
| 572 | `POINTER_ONLY` | `https://exa.ai/library/publication/whyw87dldff |  | R08 | 1 | N |
| 573 | `POINTER_ONLY` | `https://exa.ai/library/publication/xszmd63kv40 |  | R08 | 1 | N |
| 574 | `POINTER_ONLY` | `https://faculty.washington.edu/jdb/345/345%20articles/chapter%2011%20murray%20et%20al.%20%281996%29.pdf |  | R08 | 1 | N |
| 575 | `POINTER_ONLY` | `https://faculty.wcas.northwestern.edu/eli-finkel/documents/69_drigotasrusbultwieselquistwhitton1999_journalofpersonalityandsocialpsychology.pdf |  | R14 | 1 | N |
| 576 | `POINTER_ONLY` | `https://faculty.wcas.northwestern.edu/eli-finkel/documents/79_kilpatrickbissonnetterusbult2002_personalrelationships.pdf |  | R08 | 1 | N |
| 577 | `POINTER_ONLY` | `https://fbaum.unc.edu/teaching/articles/psych-bulletin-1990-kunda.pdf |  | R08 | 1 | N |
| 578 | `POINTER_ONLY` | `https://gruberpeplab.com/pdf/2014_dutra.west.impett.oveis.kogan.keltner.gruber_maniaempathicaccuracycouples.pdf |  | R08 | 1 | N |
| 579 | `POINTER_ONLY` | `https://iarr.org/img/syllabi/agnew_gr-psy_2016_close-relationships.pdf |  | R17 | 1 | N |
| 580 | `POINTER_ONLY` | `https://labs.la.utexas.edu/mestonlab/files/2018/08/meston-stanton2018_article_desynchronybetweensubjectivean.pdf |  | R02 | 1 | N |
| 581 | `POINTER_ONLY` | `https://labs.psychology.illinois.edu/~rcfraley/measures/measures.html |  | R01 | 1 | N |
| 582 | `POINTER_ONLY` | `https://labs.psychology.illinois.edu/~rcfraley/pubs.html |  | R17 | 1 | N |
| 583 | `POINTER_ONLY` | `https://labsites.rochester.edu/lelab/wp-content/uploads/2022/12/visserman-et-al.-2022-perceived-partner-responsiveness-fosters-more-positive-appraisals-of-relational-sacrifices.pdf |  | R14 | 1 | N |
| 584 | `POINTER_ONLY` | `https://lavaan.ugent.be |  | R05 | 1 | N |
| 585 | `POINTER_ONLY` | `https://learn.lakesidetraining.org/wp-content/uploads/2024/08/adult-attachment-measures.pdf |  | R14 | 1 | N |
| 586 | `POINTER_ONLY` | `https://maartensap.com/pdfs/sap2019atomic.pdf |  | R14 | 1 | N |
| 587 | `POINTER_ONLY` | `https://maartensap.com/pdfs/sap2019socialiqa.pdf |  | R14 | 1 | N |
| 588 | `POINTER_ONLY` | `https://mavmatrix.uta.edu/cgi/viewcontent.cgi |  | R08 | 1 | N |
| 589 | `POINTER_ONLY` | `https://mrdrc.dev.isr.umich.edu/wp-content/uploads/2024/04/cp00_lillard.pdf |  | R05 | 1 | N |
| 590 | `POINTER_ONLY` | `https://openaccess.city.ac.uk/id/eprint/35352/3/development%20of%20mqors.pdf |  | R14 | 1 | N |
| 591 | `POINTER_ONLY` | `https://ora.ox.ac.uk/objects/uuid:5a0dd404-6e48-40ca-a1f4-141aaab57c3e/files/rtt44pp612 |  | R08 | 1 | N |
| 592 | `POINTER_ONLY` | `https://pdf.hanspub.org/ap20221200000_93861397.pdf |  | R02 | 1 | N |
| 593 | `POINTER_ONLY` | `https://people.csail.mit.edu/lpk/papers/aij98-pomdp.pdf |  | R08 | 1 | N |
| 594 | `POINTER_ONLY` | `https://people.idsia.ch/~zaffalon/papers/2014itip-pgm.pdf |  | R07 | 1 | N |
| 595 | `POINTER_ONLY` | `https://psycnet.apa.org/manuscript/2021-17028-001.pdf |  | R02 | 1 | N |
| 596 | `POINTER_ONLY` | `https://pure.mpg.de/rest/items/item_3377548/component/file_3388432/content |  | R08 | 1 | N |
| 597 | `POINTER_ONLY` | `https://pure.uva.nl/ws/files/54463652/chapter_5.pdf |  | R08 | 1 | N |
| 598 | `POINTER_ONLY` | `https://realseekerministries.wordpress.com/wp-content/uploads/2022/12/4.2-lackey-2006.pdf |  | R08 | 1 | N |
| 599 | `POINTER_ONLY` | `https://researchonline.lshtm.ac.uk/id/eprint/4018500/1/rm04_jh17_mk.pdf |  | R05 | 1 | N |
| 600 | `POINTER_ONLY` | `https://scispace.com/pdf/the-measurement-of-interpersonal-attraction-3dbn3n56am.pdf |  | R02 | 1 | N |
| 601 | `POINTER_ONLY` | `https://socialinteractionlab.psych.umn.edu/sites/socialinteractionlab.psych.umn.edu/files/files/media/simpson_farrell_rothman_power_chapter_2019.pdf |  | R10 | 1 | N |
| 602 | `POINTER_ONLY` | `https://sprott.physics.wisc.edu/pubs/paper277.pdf |  | R06 | 1 | N |
| 603 | `POINTER_ONLY` | `https://staff.fnwi.uva.nl/d.j.n.vaneijck2/papers/13/pdfs/del.pdf |  | R08 | 1 | N |
| 604 | `POINTER_ONLY` | `https://statisticalhorizons.com/wp-content/uploads/2022/01/she-let-he-left.pdf |  | R05 | 1 | N |
| 605 | `POINTER_ONLY` | `https://users.fmi.uni-jena.de/~mundhenk/webseite/fde/belnapigpl.pdf |  | R07 | 1 | N |
| 606 | `POINTER_ONLY` | `https://web-archive.lshtm.ac.uk/csm.lshtm.ac.uk/wp-content/uploads/sites/6/2016/04/mike-kenward-22-11-2012.pdf |  | R05 | 1 | N |
| 607 | `POINTER_ONLY` | `https://www.academia.edu/48333184/the_reciprocal_cycle_of_self_concealment_and_trust_in_romantic_relationships |  | R08 | 1 | N |
| 608 | `POINTER_ONLY` | `https://www.aeaweb.org/conference/2014/retrieve.php |  | R08 | 1 | N |
| 609 | `POINTER_ONLY` | `https://www.affective-science.org/wp-content/uploads/2024/04/laurenfbpl1998.pdf |  | R10 | 1 | N |
| 610 | `POINTER_ONLY` | `https://www.ai.rug.nl/%7everheij/publications/pdf/raom2014.pdf |  | R08 | 1 | N |
| 611 | `POINTER_ONLY` | `https://www.ai.rug.nl/~niels/publications/paper985.pdf |  | R08 | 1 | N |
| 612 | `POINTER_ONLY` | `https://www.alabamamarriage.org/assets/uploads/2023/03/family-relations-2021-adler-baeder-...pdf |  | R03 | 1 | N |
| 613 | `POINTER_ONLY` | `https://www.alabamamarriage.org/assets/uploads/2023/03/family-relations-2021-adler-baeder-validating-the-couple-relationship-skills-inventory.pdf |  | R03 | 1 | N |
| 614 | `POINTER_ONLY` | `https://www.cambridge.org/core/journals/episteme/article/polarization-paradox/d8aabc387963bc79fa3404a4c5945f76 |  | R08 | 1 | N |
| 615 | `POINTER_ONLY` | `https://www.cambridge.org/core/journals/journal-of-relationships-research/article/abs/does-relationship-satisfaction-always-mean-satisfaction- |  | R03 | 1 | N |
| 616 | `POINTER_ONLY` | `https://www.cns.nyu.edu/~eero/math-tools24/handouts/sdtchapter.pdf |  | R08 | 1 | N |
| 617 | `POINTER_ONLY` | `https://www.columbia.edu/~nb2229/docs/bolger%20and%20shrout-accounting%20for%20statistical%20dependency%20may%202005.pdf |  | R10 | 1 | N |
| 618 | `POINTER_ONLY` | `https://www.columbia.edu/~on2110/papers/hmm_of_customer_relationship_dynamics.pdf |  | R05 | 1 | N |
| 619 | `POINTER_ONLY` | `https://www.communicationcache.com/uploads/1/0/8/8/10887248/accuracy_of_deception_judgments.pdf |  | R08 | 1 | N |
| 620 | `POINTER_ONLY` | `https://www.familylifesurvey.org |  | R04 | 1 | N |
| 621 | `POINTER_ONLY` | `https://www.jamescmccroskey.com/publications/57.htm |  | R02 | 1 | N |
| 622 | `POINTER_ONLY` | `https://www.jeroenvermunt.nl/ermss2004e.pdf |  | R05 | 1 | N |
| 623 | `POINTER_ONLY` | `https://www.jessicagrahn.com/uploads/6/0/8/5/6085172/stanislawtodorovdprim1999.pdf |  | R08 | 1 | N |
| 624 | `POINTER_ONLY` | `https://www.lsaf.org |  | R04 | 1 | N |
| 625 | `POINTER_ONLY` | `https://www.paulvanlange.com/s/vanlangerusbultchap2011-590f.pdf |  | R10 | 1 | N |
| 626 | `POINTER_ONLY` | `https://www.rand.org/pubs/drafts/dru489.html |  | R05 | 1 | N |
| 627 | `POINTER_ONLY` | `https://www.researchgate.net/publication/267215395_gender_differences_and_similarities_in_sexual_dire |  | R02 | 1 | N |
| 628 | `POINTER_ONLY` | `https://www.sarahcestanton.com/s/2015_campbell-stanton_encycl-of-clin-psychol_apim.pdf |  | R05 | 1 | N |
| 629 | `POINTER_ONLY` | `https://www.sas.rochester.edu/psy/people/faculty/reis_harry/assets/pdf/reisclarkholmes_2004.pdf |  | R14 | 1 | N |
| 630 | `POINTER_ONLY` | `https://www.sciencedirect.com/science/article/abs/pii/s0010027702000549 |  | R08 | 1 | N |
| 631 | `POINTER_ONLY` | `https://www.studiapsychologica.com/uploads/sironova_sp_4_vol.62_2020_pp.291-313.pdf |  | R02 | 1 | N |
| 632 | `POINTER_ONLY` | `https://www.uni-muenster.de/owms/uploads/drafts_thielsch/pdf/hirschfeld_et_al_2014_jrp.pdf |  | R07 | 1 | N |
| 633 | `POINTER_ONLY` | `https://www.zora.uzh.ch/server/api/core/bitstreams/08db41ef-8112-4307-bdd1-1156e73f307f/content |  | R08 | 1 | N |
| 634 | `UNVERIFIED` | `https://doi.org/10.1177/0003122417715051` |  | R11 | 5 | N |
| 635 | `UNVERIFIED` | `https://doi.org/10.1024/1662-9647.a000031` |  | R11 | 2 | N |
| 636 | `UNVERIFIED` | `https://doi.org/10.1037/2021-17028-001` |  | R03 | 2 | N |
| 637 | `UNVERIFIED` | `https://doi.org/10.13718/j.cnki.xdzk.2020.06.013` |  | R02 | 2 | N |
| 638 | `UNVERIFIED` | `https://doi.org/10.1609/aaai.v35i1.16792` |  | R14 | 2 | N |
| 639 | `UNVERIFIED` | `https://doi.org/10.1613/jair.3600` |  | R17 | 2 | N |
| 640 | `UNVERIFIED` | `https://doi.org/10.31234/osf.io/f6wbn` |  | R02 | 2 | N |
| 641 | `UNVERIFIED` | `https://doi.org/10.31234/osf.io/rs7eu_v1` |  | R05 | 2 | N |
| 642 | `UNVERIFIED` | `https://doi.org/10.2307/2265159` |  | R07 | 1 | N |



---

## 10. 建议的后续动作（按优先级）

| P | 动作 | 触发的发现 | 谁做 |
| --- | --- | --- | --- |
| **P0** | 解决 AR-15：`Acitelli & Antonioni (2006) "Twenty dimensions of marriage", JPSP 90(6)` 是否存在 | §5.3 / §7.2 | Architect；**必须在任何 novelty 主张前** |
| **P0** | 修 R13：把 Fixture 003 的 `HUMAN_REVIEW_REQUIRED → POINTER_HASH_ONLY` + `robots.txt ai-train=no` + `Disallow GPTBot/ClaudeBot/CCBot` 写入 R13 的源表与所有 LLM 层设计建议的约束段 | §6.3 F1 | R13 修复轮 / A04 复核 |
| **P1** | 修 M1：R08b `10.1016/S0010-0277(02)0549-8` → `10.1016/S0010-0277(02)00054-9` | §3.3.1 | R08b 窄修复 |
| **P1** | 修 M2：R04 `10.1007/s11238-014-9448-x` 的期刊改 ***Theory and Decision***；重判 D11 SOEP `NOT_DYADIC_ENOUGH` 的证据链 | §3.3.1 | R04 窄修复 |
| **P1** | 修 M3：R14 `10.1609/aaai.v35i1.16792` 不解析却承重 12 个百分点定量主张 → 补正确 DOI 或降级为 `UNVERIFIED` | §3.3.1 | R14 窄修复 |
| **P1** | 补 AR-16：MSC 五检的 4 个 DOI（Messick 1995 = `10.1037/0003-066x.50.9.741` 已确认） | §5.3 | R14 窄修复 |
| **P2** | 修 M4–M6：`10.31234/osf.io/…` → `10.31219/osf.io/…`（R02 ×1、R05 ×2） | §3.3.1 | R02 / R05 窄修复 |
| **P2** | 修 F3：R17 源表条目 37 的「Fixture 001–003 推荐」标 `SUPERSEDED`（引 R00 S-4） | §6.4 | R17 窄修复 |
| **P2** | 修 F2：R16 §9 的 rights 取舍讨论接入项目自身 Case Bank 侧 pointer-only 边界 | §6.2 | R16 窄修复 |
| **P2** | 改 R10 L550 的「见 #22」→ 改指 `19_SYNTHESIS_CANDIDATE.md` 的 gap 表 | §6.5 | R10 窄修复 |
| **P2** | 给 R03 补 D5 式的未命中披露（Geyer et al. 1999 DOI 不解析 + 前缀与著录期刊族不符） | §3.3.2 D5 | R11 窄修复（R11 的缺口表） |
| **P3** | 把 `00_MANIFEST.md` §3 的「单 lane 自报指针数」行替换为本报告 §2.1 的三层计数，并加一句「peer-reviewed-only = 350」 | §2.3 | parent（durable writeback） |
| **P3** | 全 swarm 统一 DOI 书写规范：一条来源在正文与源表内**只写一种形态**，推荐裸 `10.xxxx/yyy`；`https://doi.org/` 形式只用于需要点击的场景 | §2.1 / A04-C10 | parent，写入 `00_CHILD_CONTRACT.md` 下一版 |
| **P3** | 清理 11 个 `exa.ai/library/…` 指针：换成真实 DOI / 出版商 landing URL，或标 `POINTER_ONLY` 并明确不作为论据 | §1.3 | R03（7 条）/ R08b（4 条） |
| **P3** | 清理 2 个截断 URL（`d.docksci.com/download`、`…/does-relationship-satisfaction-always-mean-satisfaction-`）与 1 个重复 slug（Cambridge Episteme `polarization-paradox`） | §1.3 | R03 / R08b |

---

## 11. `status_recommendation`

**`SUCCESS`（附 1 项 `PARTIAL` 子范围声明）**

理由：

1. **Mission 1（全局去重）= SUCCESS。** 1,199 raw → 642 distinct pointer → 533 distinct source，三层计数 + 642 行逐条表 + 109 个副本的显式剔除。§4 B-3 关闭。
2. **Mission 2（provenance tiering）= SUCCESS**，附**声明**：304 个 journal-article 的 PRIMARY/REVIEW 切分是题名启发式，非逐篇判定（U4）。
3. **Mission 3（DOI integrity sweep）= SUCCESS。** **340 / 340 = 100% coverage**，无遗漏。331 解析成功，9 不解析，3 类 mismatch 全部定位到 lane 与行号，另登记 16 个我自己抽取器造成的假阳性。
4. **Mission 4（load-bearing）= SUCCESS。** 30 项承重来源逐条裁定，2 项不合格。
5. **Mission 5（author attribution）= SUCCESS。** 5 处 Wave 1 自报修正**逐条复核全部正确**；2 处遗留不确定（AR-15/AR-16 承重、Geyer 未披露、Hirschfeld 年份 1 年差）。
6. **Mission 6（provenance-of-provenance）= SUCCESS。** 三份 fixture 的 rights 边界逐 lane 传递审计；发现 1 MAJOR（R13 丢失 Fixture 003 边界）+ 1 MODERATE（R16）+ 1 MODERATE（R17 引用 superseded 段）。隔离边界 9 处逐处核对，1 MINOR（R10 L550 路由）。
7. **Mission 7（AGENT_RECALL audit）= SUCCESS。** 18 个 `AGENT_RECALL` 条目逐条裁定，2 条承重，全部在 R14。

**`PARTIAL` 子范围**：**U6（80 个 `UNSTABLE_COPY` 与已解析 DOI 的对应关系）未能机械解算。** 因此 533 应读作**去重仍可能不完整的上界**（真实 distinct source ≤ 533）。这不改变任何结论方向 —— 只会让 distinct source 更小，而 `PEER_REVIEWED_PRIMARY + REVIEW = 350` 不受影响（350 全部来自已解析 DOI / 明确 tier 的 URL）。

**本报告未做的事（明确）**：未修改 `D:\coding\lhrm`；未读 `#20/#21/#22` / Eye / Juece `#30` / PR `#31`；未验证 257 个 URL 的可达性；未核实 DOI 对应论文的**内容**转述是否准确（属 A01 / A03 职责）。
---

## 12. 本审计的字节状态声明（audit provenance of the audit）

A04 于 **2026-09-27 09:00–09:35** 期间读取 18 份 Wave 1 报告并完成全部计数与核实。期间检测到**并发写入**：

| 文件 | 最后写入时间 | 本审计的处理 |
| --- | --- | --- |
| `02b_CONSTRUCT_REDUNDANCY_AUDIT.md` | 09:08:11 | 已重跑全量抽取并 diff |
| `11_GENERAL_HUMAN_DYADS_SCOPE.md` | 09:10:29 | 已重跑全量抽取并 diff |

新增内容为 R02 的 §5.7 / §5.8 / §13.1–13.3 与 R11 的「修复轮补记」+ §11。**重跑后的指针集合与审计开始时逐项相同：**

| 口径 | 审计开始时 | 并发写入后重跑 | 差 |
| --- | ---: | ---: | ---: |
| 原始指针出现次数 | 1,199 | **1,199** | 0 |
| distinct pointer | 642 | **642** | 0 |
| distinct DOI | 340 | **340** | 0 |
| 新增 key | — | **0** | 0 |
| 消失 key | — | **0** | 0 |

对这两次 diff 追加检索（`git diff` 的新增行）做定向 grep（`AGENT_RECALL` / `rights` / `POINTER` / `Fixture` / `exa.ai` / `Recommended`）：**命中 0**。即这两次修复**只复述既有指针**（R02 §5.7/5.8 的补检索结果引用已有 DOI），**未新增来源、未新增 `AGENT_RECALL`、未触碰 fixture 权利边界**。

M4（`10.31234/osf.io/f6wbn`，R02 L596）与 D5（`10.1024/1662-9647.a000031`，R11 L502）在修复后**仍原样存在**，本报告的对应裁定继续有效。

**因此本报告的全部数字与发现对当前 `main` 工作副本状态有效。** 若 parent 在 A04 之后又对其他 lane 施加修复，需重跑 `docs/research/overnight-2026-09-27/` 的全量指针抽取并 diff（本报告 §1.1 的抽取规则可复现）。

**A04 未对 `D:\coding\lhrm` 做任何写操作。** 上述两处修改来自并发的 Wave 1 窄修复流程（对应 `00_MANIFEST.md` §1 记录的 "R02 + R11（各一次窄修复）" 的第二次尝试），非 A04 产生。
