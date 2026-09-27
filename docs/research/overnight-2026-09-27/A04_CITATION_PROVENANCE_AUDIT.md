# A04_CITATION_PROVENANCE_AUDIT — Wave 2 Cross-Lane Audit

> Lane: `A04` Citation / provenance audit & global source deduplication
> Scope: 全部 18 份 Wave 1 报告（R00–R17），`docs/research/overnight-2026-09-27/`，1,221,011 字节 / 11,328 行
> 核实日期：**2026-09-27**（全部网络核实均在本日完成）
> 权限：**NO GitHub write authority**；本文件为 `RESEARCH_CANDIDATE`，未修改 `D:\coding\lhrm` 任何文件
> 隔离遵守：未读取 / 执行 / 引用 LHRM issue `#20` / `#21` / `#22` 的任何内容；未触碰 Eye / Juece / Juece `#30` / PR `#31`

### Round 3 `A1` 修复记录（bookkeeping + citation repair，依 `ARCHITECT_ADJUDICATION_V1`）

**原始审计文本一律保留。** 每处改动都带 `SUPERSEDED` 注记（原文 + 取代依据），无一处静默改写。

| # | 位置 | 改动 | 依据 |
|---|---|---|---|
| 1 | §0 A04-C2 / §2.1 / §2.3 | `1,201` → **878**；「高估 2.3–3.4×」→ **1.65× / 2.51×** | manifest §7 **M-6**（= M-2）· `EV2` §5.4/§5.5 |
| 2 | §0 A04-C4 / §3.3.1 M4–M6 / §10 P2 | 撤回「`10.31234` 前缀结构非法、不解析」这一**假技术事实**；P2 标 `REJECTED_WITH_REASON` | `EV2` §5.1 / §6.1（**HIGH** 操作风险）· R-B5 |
| 3 | §0 A04-C5 / §6.1 / §6.3 | 按 **X-7** 加权利/归属边界声明；去除任何暗示 transcript/raw/anchored 证据可得的措辞 | adjudication **X-7** |
| 4 | §2.2 / §8.2 U4 | 撤回「← **真正承载科学重量的数字**」；`PEER_REVIEWED_PRIMARY` 标为**系统性误标**，350 不得用作科学重量代理 | manifest §7 **M-7** 关联项 · R-B3 · `EV2` §5.10/§7.1 |
| 5 | §3.3.2 D5 | 撤回「前缀与著录期刊族不一致」这一**不成立的理由**；改记为 `UNVERIFIED_DOI` + 真实缺陷（分隔符） | manifest §7 **M-9** · R-B6 · `J-C14` |
| 6 | §3.3.4 | **撤回** `10.1037/h0046049` 的 ✅；整节改标「含错项的清单，不构成免检标记」 | manifest §7 **M-8** · R-B7 · `J-C15` |
| 7 | **§4.2 + §4.2.1（新增）** | 30 行承重表中 **16 行作者归属修正 + 2 行题录精化**；新增 `Author (Crossref)` / `Title (Crossref)` 两列；**撤回「28 项强度充分」** | manifest §7 **M-7** · R-B2 · `EV2` §5.9/§7.2 |
| 8 | §9 列定义 | 记录 §9 的 642 行表**结构上无法支持作者级检查**这一根因（诚实声明路线） | manifest §7 **M-7** 的「或」分支 |
| 9 | §7.2 / §8.1(6) / §10 / §11 | 同步 D5 裁定、撤回依赖旧表身份的 negative result、补新待办、修 Mission 计数 | 随上述各项连带 |
| 10 | §3.3.1 M1–M3 / §7.1 | **未改动**（本 child 独立 Crossref 复查确认原裁定仍成立） | 守卫复查 |

**本 child 的另一份文件** `A01_EVIDENCE_QUALITY_AUDIT.md` 同步修复。**`00_MANIFEST.md` 与 `19_SYNTHESIS_CANDIDATE.md` 由 `A2` 拥有，本 child 未触碰**——但 §0 A04-C4 / §3.3.1 M4–M6 / §10 P2 的 manifest 侧对应文本（`00_MANIFEST.md` §2b OSF 前缀段）**在 A2 的白名单内，本文件只登记不修改**。

**复算脚本与逐项 Crossref 输出**：`A01_EVIDENCE_QUALITY_AUDIT.md` §13（同一 child 的另一份交付物，含 `a1_lane_sum.py` / `a1_crossref.py` 的完整输出留存）。

---

## 0. 结论摘要（先说要点）

| 编号 | 结论 | 等级 |
| --- | --- | --- |
| A04-C1 | 全 swarm 原始指针出现 **1,199** 次；全局去重后 **642** 个 distinct pointer；剔除 109 个「副本/碎片」后 **533** 个 distinct source。**去重倍率 2.25×**。 | — |
| A04-C2 | `PEER_REVIEWED_PRIMARY + PEER_REVIEWED_REVIEW` = **350**。**Work Order 的 150+ 目标在全局口径下达成**（超出 2.3×），但**远低于** manifest §3 各 lane 自报数相加所暗示的量级。<br>**⚠️ Round 3 `A1` 限定（依 M-7 / R-B3）**：`350` **可用作「350 个同行评审来源」**，**不得用作科学重量的代理** —— `PEER_REVIEWED_PRIMARY` 被系统性误标，分层抽样 **9/16 ≈ 56%** 不是 primary empirical work。详见 §2.2 与 §2.2.1。 | — |
| A04-C3 | 340 个 distinct DOI **全部尝试核实**：331 个解析成功（Crossref 325 / DataCite 6），9 个在 Crossref 与 DataCite 均不解析。其中 **4 个由报告 lane 自行披露**，**5 个未披露**。 | — |
| A04-C4 | 发现 **1 处 DOI 字符串错误**（R08b `10.1016/S0010-0277(02)0549-8` → 真值 `…00054-9`）、**1 处期刊归属错误**（R04 `10.1007/s11238-014-9448-x` 实际属 *Theory and Decision*，非 *J Behav Dec Making*）、**3 处 `10.31234/osf.io/…` 指针形态问题**（R02 ×1、R05 ×2）。<br>**`SUPERSEDED`（Round 3 `A1`，依 `EV2` §5.1/§6.1，R-B5）**：本条原文写「**3 处 DOI 前缀/后缀结构非法**」。**该技术事实不成立** —— Crossref prefix registry 显示 `10.31234` 与 `10.31219` **两个前缀都 live，注册者同为 `Center for Open Science`**，不存在 preprint / project 之分；`10.31234/osf.io/dus42`、`10.31234/osf.io/rs7eu_v1`、`10.31234/osf.io/f6wbn_v1` **实测均解析成功**。**本报告自身在 §3.3.4 已把 `10.31219/osf.io/gu8z7` 记为 ✅ 一致，即 PR 内部文档直接反驳本条。** 已改为中性的「指针形态问题」表述，实测细节见 §3.3.1。 | MAJOR |
| A04-C5 | **R13（LLM Skill / adaptive interview layer）全篇 0 次记录 Fixture 003 的 rights 边界**（`HUMAN_REVIEW_REQUIRED → POINTER_HASH_ONLY`、`robots.txt ai-train=no`），却用该 fixture 的 `SC/transcript/pNN` 单元做 10 余条 LLM 层设计论证。<br>**⚠️ Round 3 `A1` 按 adjudication X-7 限定**：**未成立权利违反；已确认 provenance 遗漏。** X-7 裁定「未成立权利违反」**不是**说 R13 的缺陷不存在，而是说**该缺陷的性质是文档层 provenance 遗漏，不是权利违反**。`SC/transcript/pNN` 是**指针路径标签**，A04 未据此主张任何 transcript / raw / anchored 证据曾可得。详见 §6.1 与 §6.3。 | **MAJOR** |
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

各 lane 自报数相加 = **878**（R00 30+ / R01 45 / R02 34 / R03 41 / R04 16 / R05 109 / R06 33 / R07 33 / R08 72 / R09 78 / R10 59 / R11 60+ / R12 40 / R13 70 / R14 60+ / R15 30 / R16 24 / R17 41+3；`+` 项按下界计，`41+3` 记为 44）。

**（Round 3 `A1` 更正，依 manifest §7 M-6 / `EV2` §5.4）** 本句上一版本写「各 lane 自报数相加 ≈ **1,201**……与实测 A = 1,199 一致（差 2 为四舍五入与 `41+3` 记法）」。**该一致性校验从未成立，且是范畴错误**：

- **算术**：逐项相加 = **875**（`+` 项按下界）/ **878**（`41+3` 记为 44），与 1,201 差 **−323**，与 1,199 差 **−321**。**不是「差 2」。**
- **量纲**：lane 自报数是**各 lane 内去重后**的计数；`1,199` 是**跨文件、含重复与多书写形态**的原始出现数。一个被 3 个 lane 引用的来源，在 878 里最多计 1（若每 lane 都自报则计 3），在 1,199 里计 ≥3，在 533 里计 1。**二者不同量纲，不能相互校验。**
- **`+` 项下界不可救**：要让总和达到 1,201，三个 `+` 项（`R00 30+` / `R11 60+` / `R14 60+`）须合计 **473**（平均 158/lane），而**本报告所在语料中最大的单 lane 自报数是 R05 = 109**。**任何读法下 1,201 都不可辩护。**
- **真倍率**（本 child 用 `a1_lane_sum.py` 独立复算，逐项输出见 `A01` §13.1）：`878 / 533 = 1.6473 → 1.65×`；`878 / 350 = 2.5086 → 2.51×`。另：`878 / 642 = 1.37×`；`878 / 1199 = 0.73×`。
- **交叉确认**：本文件 §2.1 与 `A01` F-35 **各自独立列出同一串 18 个数**；本 child 的脚本显式做了跨文件逐 lane 比对，**0 处不符**，两处求和结果相同。

**定性结论不变且仍然成立**：lane 自报数**不可相加**、**不可对外声称为「N 个独立来源」**。错的只是倍率数字。`533` 应继续读作**上界**（本报告 U5/U6，见 §8.2）。

但 1,199 → 533 的落差来自两个独立机制（此项**不受**上面的更正影响）：

- **跨 lane 重复**：42 个指针被 ≥2 个 lane 引用；5 个被 ≥3 个 lane 引用（Rusbult 1998 IMS = 7 lane / 13 次）。
- **书写形态重复**：340 个 distinct DOI 有 **740 次** DOI 形态出现（590 裸串 + 76 `doi:` + 58 resolver URL + 8 `_` 形态 + 8 出版社路径），即 **2.18 次/DOI**。其中 58 次是 `https://doi.org/10.xxxx` 这种把 DOI 完整重写一遍的 URL 形式。

### 2.2 分层计数

| Tier | distinct | 占 C 的比例 | 备注 |
| --- | ---: | ---: | --- |
| `PEER_REVIEWED_PRIMARY` | **319** | 59.8% | 304 个 `journal-article` + 1 landing URL + 14 其他 |
| `PEER_REVIEWED_REVIEW` | **31** | 5.8% | 8 `book-chapter` + 1 `book` + 1 encyclopedia chapter + 1 book excerpt + 20 题名含 meta-analysis/review 的 journal-article |
| `PEER_REVIEWED_LANDING` | 1 | 0.2% | 出版社 landing URL 无 DOI（`statmodel.com/download/webtalk4.pdf`）；为口径一致单列 |
| **`PEER_REVIEWED_PRIMARY + REVIEW` 小计** | **350** | **65.7%** | ⚠️ **Round 3 `A1` 限定：这是「350 个同行评审来源」，不是「350 份一手经验数据」，也不是「真正承载科学重量的数字」。** 上一版本此格写「← **真正承载科学重量的数字**」，该措辞**已撤回**（依 M-7 / R-B3）。见 §2.2 与 §2.2.1 |
| `GREY_OFFICIAL` | 62 | 11.6% | 19 政府/法院/标准机构 + 18 软件仓 + 8 学术方法手册 + 8 工具文档 + 其余 |
| `OFFICIAL_DATA` | 57 | 10.7% | 47 cohort 门户 + 7 data 门户 + 3 DataCite 官方数据 DOI（pairfam / SHARE w1 / SHARE w8） |
| `PREPRINT` | 47 | 8.8% | 44 arXiv id + 3 `posted-content` |
| `DATASET` | 7 | 1.3% | 2 CoMSES codebase + 6 Crossref/DataCite `dataset` 型 DOI（去重后 7） |
| `UNVERIFIED` | 9 | 1.7% | 9 个不解析 DOI（§4.3） |
| `POINTER_ONLY` | 109 | — | 副本/碎片，**排除出 source 计数** |
| `WORKING_PAPER` | 0 | 0% | swarm 未使用此层 |
| `DISSERTATION` | 0 | 0% | swarm 未使用此层 |
| `TEXT_CORPUS` | 0 | 0% | 三份冻结 fixture 走 repo+path 指针，未走此层（见 §6） |

**⚠️ 分层的重要限制**：本层的 primary/review 切分是**估计值，不是逐篇判定**。`PEER_REVIEWED_PRIMARY` vs `PEER_REVIEWED_REVIEW` 是按 **Crossref `type` + 题名正则** 判定的，**没有逐篇读摘要**。304 个 `journal-article` 的切分可能有个位数到十几项误差。`PEER_REVIEWED_PRIMARY + REVIEW = 350` 这个合计是稳的（不受切分误差影响），但两者的**分别**计数应视为量级估计。

### 2.2.1 `PEER_REVIEWED_PRIMARY` 的系统性误标（Round 3 `A1` 补测，依 M-7 / R-B3 / `EV2` §5.10+§7.1）

**上一版本 §2.2 的最后一句写**：「304 个 `journal-article` 的 primary/review 切分是**估计值**，可能有个位数到十几项误差。」

**Round 3 更正**：这不是「个位数误差」量级的问题，而是**判定规则的系统性偏误**。

**偏误机制**：以 `Crossref type == journal-article` + 题名正则判定 primary，**必然地把理论论文、方法论论文、综述论文与计算模型论文判为 PRIMARY** —— 因为它们在 Crossref 里的 `type` 同样是 `journal-article`，题名里也不出现 `meta-analysis` / `review` 这类词。

**分层抽样证据**（Round 2 `EV2` §7.1 执行；本 child **采信该抽样并复核其方法说明**，未重跑 —— 见下方限度）：

| A04 §9 行 | 抽样命中 | 分类 | 判定 |
|---:|---|---|---|
| 1 | Rusbult, Martz et al., "The Investment Model Scale", *Pers Relat* 5 | 量表原始论文 | ✅ primary empirical |
| 21 | Lucas, "Why the CLPM Is Almost Never the Right Choice", *AMPPS* 6 | 方法论 | ❌ |
| 41 | Brady, Cohen et al., 现场干预 RCT, *Sci Adv* 6 | 现场干预 | ✅ primary empirical |
| 61 | Dukart, Holiga et al., "JuSpace: a tool for…", *HBM* 42 | 工具/方法 | ❌ |
| 81 | Hazan & Shaver, *JPSP* 52 | 理论 + 自有 3 项研究 | ⚠️ 混合 |
| 101 | Andersen, "…unobserved heterogeneity in CLPMs?", *Psychol Methods* 27 | 方法论 | ❌ |
| 121 | Gneezy & Fessler, 现场实验, *Proc R Soc B* 279 | 现场实验 | ✅ primary empirical |
| 141 | Rodríguez & Verup, 调查, *Pers Relat* 23 | 调查 | ✅ primary empirical |
| 161 | Kellas, Bean et al., 纵向, *JSPR* 25 | 纵向 | ✅ primary empirical |
| 181 | Schindler, "About the Uncertainties in Model Design…", *JASSS* 16 | 方法/模型设定 | ❌ |
| 201 | Neto et al., 调查, *Interpersona* 6 | 调查 | ✅ primary empirical |
| 221 | Adams & Jones, "The conceptualization of marital commitment", *JPSP* 72 | 理论整合（无新数据） | ❌ |
| 241 | Hamaker, Asparouhov et al., "At the Frontiers of Modeling ILD", *MBR* 53 | 方法论综述 | ❌ |
| 261 | Kane, "Validating the Interpretations and Uses of Test Scores", *J Educ Meas* 50 | 方法论 | ❌ |
| 281 | Mudimu, Engelbrecht et al., Agent-based model…, *Adapt Behav* 23 | 计算模型（非一手人类数据） | ❌ |
| 301 | Schoorman, Mayer et al., "An Integrative Model of Organizational Trust", *AMR* 32 | 理论综述 | ❌ |

| 分类 | n / 16 | 占比 |
|---|---:|---:|
| 真 primary empirical | **6** | 37.5% |
| **非 primary**（理论 3 / 方法 4 / 综述 1 / 计算模型 1） | **9** | **56.3%** |
| 混合 | 1 | 6.3% |

**因此（`350` 的正确读法）**：

| 读法 | 是否允许 | 理由 |
|---|---|---|
| 「**350** 个同行评审来源」 | ✅ **允许** | 该合计不受 primary/review 切分误差影响 |
| 「**350** 份一手经验数据」/「350 份 primary data」 | ❌ **不允许** | 抽样估计 **56%** 不是 primary empirical work |
| 「**350** 真正承载科学重量」 | ❌ **不允许** | 上一版本 §2.2 的这句话**已撤回**。tier 只编码**出处类型**，不编码**证据强度**；把 tier 读成权重是层级混淆 |
| `PEER_REVIEWED_PRIMARY = 319` / `PEER_REVIEWED_REVIEW = 31` 的**分别**计数 | ❌ **不可引用** | 判定规则本身有系统性偏误（见上） |

**限度的诚实记录**：

1. **该抽样是系统抽样，不是随机抽样**（对 319 行每 20 行取 1，索引 0/20/…/300）。因此 **56.3% 是区间信息，不是点估计**；真实比例可能偏离。
2. **分类依据是题名与出处类型，不是对研究设计的判定。** `EV2` 未读方法部分。6 个 ✅ 只表示「题名与出处指向一手人类受试数据」，**不表示该研究设计无缺陷**。
3. **本 child 未重跑该抽样。** 理由：重跑需要把 `EV2` 的分类判读重做一遍，属「新的文献扫描」，Round 3 派发明令禁止（`No new literature sweep`）。本 child 做的是**采信 + 机制说明 + 限度记录**，并把「重出 primary-data 口径的分子」登记为待办（§10 P1）。
4. **未做的事**：要得到 primary-data 口径的分子，**必须逐篇读摘要重出**。本轮未做，`319` 不得被当作「319 篇一手经验研究」引用。

**这条限制此前已被本报告两次披露**（原 §2.2 与原 §8.3 non-claim #4），但**措辞仍会误导**（EV2 §6.4：「限制已披露但措辞仍会误导」）。Round 3 修的是**措辞**——把「真正承载科学重量的数字」这句话本身去掉，并把抽样证据与限度搬进正文。

### 2.3 对 Work Order「150+ 高质量学术/官方/来源指针」的诚实裁定

| 读法 | 数字 | 裁定 |
| --- | ---: | --- |
| 严格读法 = 同行评审（primary + review） | **350** | ✅ 达成，2.3×。**⚠️ Round 3 限定：读作「350 个同行评审来源」，不是 350 份一手经验数据**（§2.2.1） |
| 宽读法 = 同行评审 + 官方数据 + 官方灰 + dataset | **476** | ✅ 达成，3.2× |
| 错误读法 = 各 lane 自报数相加 = 878 | 878 | ❌ **不成立**，相对 533 distinct source 高估 **1.65×**、相对 350 同行评审高估 **2.51×** |

**（Round 3 `A1` 更正，依 M-6 / `EV2` §5.5）** 第三行上一版本写「各 lane 自报数相加 ≈ **1,201** | 1,201 | ❌ **不成立**，高估 **2.3–3.4×**」。`1,201` 与 `2.3–3.4×` **两个数都不成立**，已按 §2.1 的独立复算替换为 `878` / `1.65×` / `2.51×`。

**结论：目标达成，但达成的余量来自 global dedup 之后仍然存在的 350 个同行评审来源，而不是来自 lane 数量。** 同时必须记录：若把 109 个副本也算进去，350 → 459，任何"数量"论证都会被这批非来源指针污染。**且按 §2.2.1，350 本身是「同行评审来源数」，不是「科学重量」。**

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
| M4 | `10.31234/osf.io/f6wbn` | R02 L596 | **`SUPERSEDED`（Round 3 `A1`，依 `EV2` §5.1 / R-B5）** —— 上一版本本行写「**DOI 前缀/后缀结构非法。`10.31234` 是 PsyArXiv 的前缀，`osf.io/` 是 OSF（`10.31219`）的后缀形态**」。**该理由不成立**：`10.31234` 与 `10.31219` **两个前缀都 live，注册者同为 `Center for Open Science`**（Crossref prefix registry），不存在 preprint / project 之分。**真实缺陷**：`f6wbn` 这个 identifier **只在 `10.31234` + `_v1` 形态下注册** —— `10.31234/osf.io/f6wbn_v1` 解析成功（`https://osf.io/f6wbn_v1`），无 `_v1` 的 `10.31234/osf.io/f6wbn` 与 `10.31219/osf.io/f6wbn` 均 404。**修法是补版本后缀，不是换前缀**（补 `_v1` 已由修复轮应用）。 | MODERATE |
| M5 | `10.31234/osf.io/rs7eu_v1` | R05 L509 | **`SUPERSEDED`** —— 上一版本写「同 M4，结构非法，不解析」。**实测该 DOI 解析成功**（Crossref 200 / `doi.org` 302 → `https://osf.io/rs7eu_v1`）。**本条的前提被证伪，该行应从 mismatch 清单中移除。** | **已撤销（`UNRESOLVED_RETRACTED`）** |
| M6 | `10.31234/osf.io/dus42` | R05 L506 | **`SUPERSEDED`** —— 上一版本写「同 M4，结构非法，不解析」。**实测该 DOI 解析成功**（Crossref 200 / `doi.org` 302 → `https://osf.io/dus42_v1`）。**本条的前提被证伪，该行应从 mismatch 清单中移除。** | **已撤销（`UNRESOLVED_RETRACTED`）** |

> **⚠️ Round 3 `A1` 的连带警示（`EV2` §6.1 评为 `HIGH` 操作风险）**：本报告 §3.3.4 自己把 `10.31219/osf.io/gu8z7` 记为 ✅ 一致（即 PR 内**存在一条 live 的 `10.31219` DOI**，R14 L353），而 §10 P2 建议「把 `10.31234/osf.io/…` 改成 `10.31219/osf.io/…`」。**两条来源同出本 PR、指向同一个动作，而该动作会把一条 live 指针变成 404 —— 一次纯粹的净损失。** P2 已改标 `REJECTED_WITH_REASON`（见 §10）。**manifest 侧的对应段落（`00_MANIFEST.md` §2b）不在本 child 白名单内，已登记交 `A2` / parent。**
>
> **本 child 的实测来源**：**本 child 独立复验了全部 6 个 identifier 与 2 个前缀记录**（`https://api.crossref.org/works/<DOI>` 与 `https://api.crossref.org/prefixes/<prefix>`，只读 GET，UA `LHRM-R3A1-Repair/1.0`，2026-09-27），结果与 `EV2` §5.1 的逐 identifier 表**完全一致**：

> | 被测 identifier | Crossref | 标题（实测） |
> |---|---|---|
> | `10.31234/osf.io/f6wbn_v1` | **200** | "Measures of relationship power dynamics in romantic relationships" |
> | `10.31219/osf.io/gu8z7` | **200** | "Is Romantic Desire Predictable? Machine Learning Applied to Initial Romantic Att…" |
> | `10.31234/osf.io/rs7eu_v1` | **200** | "Typical Patterns of Stability in Longitudinal Data: Implications for Model Choic…" |
> | `10.31234/osf.io/dus42` | **200** | "Illusory Between-person Component in the Random Intercept Cross-lagged Panel Mod…" |
> | `10.31234/osf.io/f6wbn`（无后缀） | **404** | — |
> | `10.31219/osf.io/f6wbn` | **404** | — |
> | prefix `10.31234` | live，注册者 = **`Center for Open Science`** | |
> | prefix `10.31219` | live，注册者 = **`Center for Open Science`** | |
>
> **因此 M5 / M6 的撤销、M4 的理由替换、以及「补 `_v1` 而非换前缀」的正确修法，本 child 均有自己的实测依据**，不单是采信 `EV2`。**注意**：标题一栏还显示 `f6wbn_v1` 与 `jftr.70019` 是同一篇（Junkins et al. 2025 关系权力动力量表），与 `A04` §4.2 第 22 行的作者错配互相印证。

#### 3.3.2 报告已自行披露者（**不计为 lane 缺陷**，本审计确认其披露为真）

| # | DOI | 报告 | 披露位置 | 本审计复核 |
| --- | --- | --- | --- | --- |
| D1 | `10.1613/jair.3600` | R17 | L512 `FETCH_FAILED` + L592 | 确认不解析。**并且该著录本身有 venue 错**：Poesio 2012 "A survey of ambiguity and consensus in natural language processing" 实际刊于 ***Computational Linguistics*** 38(4)，非 *JAIR* 48。R17 的 `10.1177/…` 猜测（S17 §10）也是 venue 错（Balan 1968 在 *Psychological Bulletin*，非 SAGE 刊）。 |
| D2 | `10.1037/2021-17028-001` | R03 | L336 标 `UNVERIFIED_DOI`，并说明「DOI 经 APA manuscript 记录页确认存在；Crossref 查询未返回」 | 确认 Crossref + DataCite 均无。R03 的处理**正确**。 |
| D3 | `10.2307/2265159` | R07 | L551 标 `[UNVERIFIED]` + 「背景提及，未用于任何主张」 | 确认不解析。R07 的隔离**正确**。 |
| D4 | `10.1177/0003122417715051` | R11 | L132 记 `HTTP 404` + L133 十路检索 | 这**不是引用**，是 R11 记录自己检索 Gilligan 2017 失败的 trace。R11 的负结果披露是全 swarm 最干净的一处。 |
| D5 | `10.1024/1662-9647.a000031` | R11 | **未披露** | **`SUPERSEDED`（Round 3 `A1`，依 M-9 / R-B6 / `J-C14`）** —— 上一版本本行写「不解析。**前缀 `1662-9647` 属 *Zeitschrift für Gerontopsychologie und Psychiatrie*（德文），报告著录为 *GeroPsych* 24(1)（英文刊）。前缀与著录期刊族不一致**」。**该理由不成立**：`1662-9647` **正是 GeroPsych 的 ISSN 前缀**，报告著录的期刊族与前缀**是一致的**，二者并无冲突。<br>**真实缺陷（本 child 已实测）**：这是一个 **DOI 分隔符错误** —— 报告用**点**（`.a000031`），真值用**斜杠**（`/a000031`）。实测：<br>· `10.1024/1662-9647.a000031`（点） → Crossref **404**<br>· `10.1024/1662-9647/a000031`（斜杠） → Crossref **200**，**Di Rosa, M.; Kofahl, C.; McKee, K.; Bień, B.; Lamura, G.; Prouskas, C. (+2), 2011, *GeroPsych* 24(1):5–18**, "A Typology of Caregiving Situations and Service Use in Family Carers of Older People in Six European Countries"。**注意：作者也不是 R11 写的「Geyer et al. 1999」**（与 `A01` F-08 / `NR-11-1` 一致）。<br>**裁定改为 `UNVERIFIED_DOI`** —— **不解析这一事实保留，但必须以真实理由记录；本报告不为其提供任何错误的解释。** | MODERATE |
| D6 | `10.13718/j.cnki.xdzk.2020.06.013` | R02 | **未披露** | 不解析。CNKI 前缀 `10.13718` 不在 Crossref/DataCite 索引，属**索引缺席**而非引用错误（山东大学学报版）。**低危**，但按 swarm 规则仍应标 `UNVERIFIED`。 | LOW |

#### 3.3.3 我自己的抽取器缺陷（**已修正，非 swarm 问题**，如实登记）

首轮正则把 4 类合法 DOI 弄成了假 `NOT_FOUND`，共影响 **16 个指针 / 33 次出现**。修正后全部解析成功且与报告著录一致：

| 我犯的错 | 受影响 | 修正后 | 与报告一致性 |
| --- | --- | --- | --- |
| 正则排除 `)`，把 Elsevier 平衡括号 DOI 截断 | 9 个 / 20 次（如 `10.1016/0022-1031(80`、`10.1016/S0378-8733(99`、`10.1016/1053-4822(91`、`10.1016/S0065-2601(08`、`10.1016/S0140-1971(86`、`10.1016/0010-0277(83`、`10.1016/0022-0965(85`、`10.1016/S0004-3702(98`、`10.1016/S0010-0277(02`） | 全部解析 | 全部一致 |
| 剥 markdown `_` 时误伤 Springer/T&F DOI 的 `_` 分隔形态 | 4 个 / 12 次（`10.1207/s15327957pspr10032`、`10.1207/s15327752jpa41066`、`10.1007/3-540-45547-73`、`10.1162/colia00502`） | 真值 `10.1207/s15327957pspr1003_2`、`10.1207/s15327752jpa4106_6`、`10.1007/3-540-45547-7_3`、`10.1162/coli_a_00502`，全部解析 | 全部一致 |
| 未折叠 `doi:` / 出版社路径内的 DOI | 55 个 URL key 实为 DOI 副本 | 折叠后 DOI 从 354 收到 340 | — |

#### 3.3.4 顺带核实的高风险项 —— **⚠️ Round 3：原「已通过」清单含错项，不构成免检标记**

> **`SUPERSEDED`（Round 3 `A1`，依 M-8 / R-B7 / `J-C15`）**：本节上一版本的标题是「顺带核实并**通过**的高风险项（抽查后无 mismatch）」，并给出一律 ✅ 的裁定表。**该清单含一条错项，因此它不是一份有效的免检清单，而是**一份**其"已通过"标记不承载信息的清单。** 已做三件事：(1) 撤回 `10.1037/h0046049` 的 ✅；(2) 把本节标题改为「**含错项的清单，不构成免检标记**」；(3) 加一条全表重检要求（见 §3.3.5）。**其余各行的 ✅ 本 child 未复核**（见下方限度声明），**既不撤回也不背书。**

**错项逐条**：

| DOI | 报告著录 | Crossref **实测真值** | 原裁定 | Round 3 裁定 |
| --- | --- | --- | --- | --- |
| `10.1037/h0046049` | R17 S19 Cartwright & Harary 1956, ***Psych Review* 63(4)** | **Cartwright, D.; Harary, F. (1956), *Psychological Review* 63(5):277–293**, "Structural balance: a generalization of Heider's theory" | ✅ 一致 | ❌ **原「已通过」清单里的假 PASS —— 卷期错（63(4) vs 63(5)）。作者、年份、期刊名、标题全部正确，只错在期号，因此它正是最难被肉眼发现的一类错。** |

**该错项为什么严重（这才是重点）**：
- 本节的用途是给**未被列为 mismatch 的高风险项**打「已通过」标记，供下游直接采信。**一个含错项的「已通过」清单，其标记不承载信息** —— 它会让读者以为这一节提供了额外保证，实际上它只说明「这 15 行被抽查过」，而抽查本身有假阳性。
- 错项恰好落在**最难自查的字段**上：作者对、年份对、期刊对、标题对，只有 `(4)` 应为 `(5)`。**若抽查者只核对「作者在不在」「年份对不对」「期刊像不像」，这一行会通过。**
- **因此：在任何人引用本节任何一行之前，必须对本表做一次完整的 volume/issue/页码 级重检**（§3.3.5）。

**限度声明（Round 3 `A1` 逐字声明）**：本 child **只复验了上表这一行**（`10.1037/h0046049`），因为它是本节被指控的那一行。**其余 14 行的 ✅ 既未被本 child 复核，也未被本 child 撤回** —— 它们在本轮**处于 `NOT_REVERIFIED` 状态**。**特别地，本 child 不主张「除 `h0046049` 外其余 14 行都是对的」** —— 恰恰相反：既然本节已被证明会产生假 PASS，那么**其余各行通过的概率不能假定为高**。§3.3.5 就是为此而设。

#### 3.3.4（原表，保留原文；Round 3 已按上表改判其中一行）

| DOI | 报告著录 | Crossref | 原裁定 |
| --- | --- | --- | --- |
| `10.1038/s41562-016-0021` | R16 L554 Munafò 2017, *Nature Hum Behav* 1, 0021 | "A manifesto for reproducible science", NHB 2017 | ✅ 一致（DOI 未被截断）——**Round 3 `NOT_REVERIFIED`** |
| `10.1038/s41562-016-0034` | R16 L555 Wagenmakers 2017, NHB 1, 0020 | "Promoting reproducibility with registered reports", NHB 2017 | ✅ 一致 ——**Round 3 `NOT_REVERIFIED`** |
| `10.1177/1077801206293328` | R11 L111/L481 Johnson 2006, *Violence Against Women* 12(11) | "Conflict and Control", VAW 2006 | ✅ 一致 ——**Round 3 `NOT_REVERIFIED`** |
| `10.1145/3704890` | R07 L88/L424/L545 Liell-Cock & Staton 2025, POPL | "Compositional Imprecise Probability…", PACMPL 2025 | ✅ 一致 ——**Round 3 `NOT_REVERIFIED`**（本 child 已在 §4.2 承重表中独立复验过同一 DOI，作者/卷期/页码**一致**） |
| `10.1017/9781108131490.003` | R10 | "Attachment Insecurity and the Regulation of Power and Dependence in Intimate Relationships", *Power in Close Relationships* | ✅ 一致 ——**Round 3 `NOT_REVERIFIED`** |
| **`10.1037/h0046049`** | R17 S19 Cartwright & Harary 1956 | ~~"…", *Psych Review* 63(4)~~ → **实测 63(5):277–293** | ❌ **假 PASS，见上表** |
| `10.1037/0022-3514.76.1.72` | R14 L275（自查 Fletcher & Simpson 2000 页码） | *JPSP* 76(1), **72–89** | ✅ R14 的更正（54–71 → 72–89）**正确** ——**本 child 已独立复验同一 DOI：Fletcher, Simpson, Thomas & Giles 1999, *JPSP* 76(1):72–89，一致**（但本行**作者归属**在 §4.2 中是错的，见 §4.2.1） |
| `10.1037/0022-3514.63.4.596` | R01（Rempel/Aron DOI 末位自查） | Aron 1992 *JPSP* 63(4) 596 | ✅ R01 的更正（`.589` → `.596`）**正确** ——**Round 3 `NOT_REVERIFIED`** |
| `10.1016/0022-1031(80)90007-4` | R03 L116/L342、R14 L324 记 *JESP* 16, 172–186 | *Journal of Experimental Social Psychology* 1980 | ✅ 一致 ——**Round 3 `NOT_REVERIFIED`** |
| `10.4232/pairfam.5678.14.2.0` | R04 L83/L85/L940 pairfam ZA5678 v14.2 | DataCite: "Beziehungs- und Familienpanel (pairfam)", GESIS 2024 | ✅ 一致（Crossref 404 属预期，走 DataCite）——**Round 3 `NOT_REVERIFIED`** |
| `10.6103/share.w1.900` / `w8.900` | R04 SHARE Wave 1 / Wave 8 | DataCite: SHARE-ERIC 2024 | ✅ 一致 ——**Round 3 `NOT_REVERIFIED`** |
| `10.12758/mda.2013.013` | R13 BFI-10 | DataCite: GESIS 2013 | ✅ 一致 ——**Round 3 `NOT_REVERIFIED`** |
| `10.31219/osf.io/gu8z7` | R14 L353 Joel/Eastwick/Finkel 2017 | Crossref 解析 | ✅ 一致 ——**Round 3 已独立复验：Crossref 200，"Is Romantic Desire Predictable? Machine Learning Applied to Initial Romantic Att…"，一致**。**另注：本行是 §3.3.1 M4–M6 撤销的关键对照（`10.31219` 是 live 前缀）** |
| `10.1016/0022-0965(85)90051-7` | R08b L780 Perner & Wimmer 1985, *JECP* 39(3) | "'John thinks that Mary thinks that…' Attribution of second-order beliefs", JECP 1985 | ✅ 一致 ——**Round 3 `NOT_REVERIFIED`** |
| `10.1016/0010-0277(83)90004-5` | R08b L780 Wimmer 1983, *Cognition* 13(1) | "Beliefs about beliefs…", *Cognition* 1983 | ✅ 一致 ——**Round 3 `NOT_REVERIFIED`** |

#### 3.3.5 全表重检要求（Round 3 `A1` 新增待办）

**要求**：在**任何人**引用 §3.3.4 的任何一行之前，对该表 15 行做一次**完整的 volume / issue / 页码 级重检**（不是「作者/年份/期刊对不对」这一级）。

**为什么必须全检而不是只检 `h0046049` 一行**：本节已证明它的抽查判据（作者 / 年份 / 期刊 / 标题）**不足以发现期号错误**，而本节的用途正是给下游提供免检保证。**只撤回错项、保留其余 ✅，会让这 15 行的 ✅ 继续被当作保证使用，而它们已经不再可靠。** 把它们标为 `NOT_REVERIFIED`（本轮已做）是把「假保证」降级为「无保证」，这是本轮能诚实做到的最大程度；**真正的修复是全检。**

**登记为 §10 P1。** 本 child **未执行**该全检：它需要 15 次 Crossref 逐条卷期比对且**属于一次新的核查扫描**，Round 3 派发限定「只可复验你实际改动的 DOI，不得扩大范围」。本 child 实际改动的 DOI 已全部复验完毕（见 §4.2.1）。

---

## 4. 承重来源评估（Load-bearing assessment）

### 4.1 判据

一个来源是「承重的」当且仅当：**(a)** 被 ≥2 个 lane 引用（42 个指针满足），**或 (b)** 被 `00_MANIFEST.md` §2「核心证据指针」列点名，或 **(c)** 报告自身把它标为 load-bearing / 承重 / 决定性。

### 4.2 承重来源表（30 项）—— **⚠️ Round 3 `A1`：新增 `Author (Crossref)` / `Title (Crossref)` 两列，16 行作者归属修正，「28 项强度充分」已撤回**

> **`SUPERSEDED`（Round 3 `A1`，依 M-7 / R-B2 / `EV2` §5.9+§6.3）**
>
> **上一版本本节的根因**：表列定义为 `Tier / Pointer / Year / Lanes / n / Resolved`（§9），**没有 `author` 列，也没有 `title` 列**。**因此「作者归属错误」这一缺陷类在本报告内部结构上不可能被发现** —— 审计者的注意力被结构性地引导到 DOI 是否解析、期刊/年份是否一致，而「这个 DOI 指向的是谁」根本没有列可以写、也没有列可以查。**这不是一次疏忽，是一个 schema 缺陷。**
>
> **Round 3 做的三件事**：(1) **给本表新增 `Author (Crossref)` 与 `Title (Crossref)` 两列**，30 行的 Crossref 真值全部实测填入 —— 这样本表**现在可以自我纠错**；(2) **修正 16 行作者归属 + 2 行题录精化**（§4.2.1 逐条记录，含原值、真值、影响）；(3) **撤回本节结论「30 项中 28 项强度充分」**。
>
> **为什么必须撤回而不是就地改数**：原结论「28 项强度充分」是在一张**身份错了 ≥16 行**的表上作出的。**你无法为一个你叫不出名字的来源背书强度。** 更严格地说：那 28 个 ✅ 中的每一个，其 ✅ 都是对**错误的论文**作出的。**逐格改数会保留「这张表已被完整评估过」这个印象，而那个印象正是错的。**
>
> **§9 的 642 行表未加这两列** —— 见 §9 的结构性限制声明。加列需要为 642 行逐条取回 author/title，其中 **257 个 URL + 44 个 arXiv + 109 个 `POINTER_ONLY` 根本没有 Crossref 记录可取**，实际只有 DOI 行可填。这既是一次新的扫描（Round 3 禁止），也会产生一半空格一半实值的混合表。**本节选择「明确的诚实声明 + 已知坏行列表」这条 M-7 允许的替代路线**（见 §9）。

**表（新列：`Author (Crossref)` / `Title (Crossref)` 均为本 child 2026-09-27 实测；删除线为原表著录）**

| # | 来源（原表著录） | **`Author (Crossref)`** | **`Title (Crossref)`** | Tier | lanes | 承重的主张 | 强度是否够 | 裁定 |
|---|---|---|---|---|---|---|---|---|
| 1 | Rusbult et al. 1998, `10.1111/j.1475-6811.1998.tb00177.x` | Rusbult, C. E.; Martz, J. M.; Agnew, C. R. | "The Investment Model Scale: Measuring commitment level, satisfaction level, quality of alternatives, and investment size" | PR | **7** (R00 R01 R02 R03 R06 R14 R17) / 13 次 | `Dedication` / commitment 的测量基础；IMS 四分量 | ✅ 原始量表论文，全 swarm 最稳的单点 | 充分 |
| 2 | Laurenceau et al. 1998, `10.1037/0022-3514.74.5.1238` | Laurenceau, J.-P.; Barrett, L. F.; Pietromonaco, P. R. | "Intimacy as an interpersonal process…" | PR | 5 / 10 | intimacy 作为人际过程（IPM 骨架） | ✅ 原始理论 + diary 验证 | 充分 |
| 3 | Le & Agnew 2003, `10.1111/1475-6811.00035` | Le, B.; Agnew, C. R. | "Commitment and its theorized determinants: a meta-analysis of the Investment Model" | **REVIEW** | 5 / 9 | Investment Model 承诺的 meta 证据 | ✅ meta-analysis，正当用途 | 充分 |
| 4 | Tran, Judge & Kashima 2019, `10.1111/pere.12268` | Tran, P.; Judge, M.; Kashima, Y. | "Commitment in relationships: an updated meta-analysis of the Investment Model" | **REVIEW** | 4 / 9 | 更新版 Investment Model meta；R02 报 R²=.54 | ✅ meta-analysis，正当用途 | 充分 |
| 5 | **Joel et al. 2020 PNAS, `10.1073/pnas.1917036117`** | Joel, S.; Eastwick, P. W.; Allison, C. J.; Arriaga, X. B.; Baker, Z. G.; Bar-Kalifa, E.; (+80) | "Machine learning uncovers the most robust self-report predictors of relationship quality across 43 longitudinal datasets" | PR | 4 / 9 | 43 纵向 couples 研究的关系质量自报预测因子 | ⚠️ **primary 被当 meta 用**。R16 L522 明确写「不主张 S23 正文的五条实证结论（书目已核实，**正文未读**；结论经转述）。该来源在 `R16-LK5` 与 `B3` 中 load-bearing」。R06/R14/R17 均以转述形式承重。 | **MAJOR** |
| 6 | ~~Rempel, Sayer & Lehman 1985~~ → **Rempel, Holmes & Zanna 1985**, `10.1037/0022-3514.49.1.95` | **Rempel, J. K.; Holmes, J. G.; Zanna, M. P.** | "Trust in close relationships" | PR | 2 / 4 | `Trust` = credibility/dependability/faith/predictability | ✅ 修正后**更贴合**（原归属的 "Sayer & Lehman" 不在该文的作者名单内）· *JPSP* 49(1):95–112 · R01 已自查并更正上游卷期错 | 充分 |
| 7 | ~~Rempel & Holmes 1989~~ → **Berscheid, Snyder & Omoto 1989**, `10.1037/0022-3514.57.5.792` | **Berscheid, E.; Snyder, M.; Omoto, A. M.** | "The Relationship Closeness Inventory: Assessing the closeness of interpersonal relationships" | PR | 2 / 4 | `Closeness` ≠ `Liking`（可分性） | ✅ 修正后**恰好命中**——RCI 的原始量表论文 | 充分 |
| 8 | Aron et al. 1992, `10.1037/0022-3514.63.4.596` | Aron, A.; Aron, E. N.; Smollan, D. | "Inclusion of Other in the Self Scale and the structure of interpersonal closeness" | PR | 3 / 6 | IOS 自我-他人包含 → 关系亲密 | ✅ R01 已自查 DOI 末位 | 充分 |
| 9 | Keltner 2003, `10.1037/0033-295x.110.2.265` | Keltner, D.; Gruenfeld, D. H.; Anderson, C. | "Power, approach, and inhibition" | PR | 3 / 5 | power = approach + inhibition（双轴） | ✅ 理论原始论文 | 充分 |
| 10 | ~~Powers & Overall 2017~~ → **Finkel, Simpson & Eastwick 2017**, `10.1146/annurev-psych-010416-044038` | **Finkel, E. J.; Simpson, J. A.; Eastwick, P. W.** | "The Psychology of Close Relationships: **Fourteen Core Principles**" | PR | 3 / 4 | 十四核心原则（构念收敛的上位框架） | ✅ 修正后**恰好命中**（标题即含 "Fourteen Core Principles"）；仍属 Annual Review 综述性文章，**作框架不作证据** | 可接受（作框架不作证据） |
| 11 | ~~Ben-Shahar & Ostrow 2008~~ → **Finkel, Hui, Carswell & Larson 2014**, `10.1080/1047840x.2014.863723` | **Finkel, E. J.; Hui, C. M.; Carswell, K. L.; Larson, G. M.** | "The **Suffocation of Marriage**: Climbing Mount Maslow Without Enough Oxygen" | PR | 2 / 4 | 「窒息婚姻」批判 LHRM 的 `S/O/D` 目标 | ✅ 修正后**恰好命中**（标题即含 "Suffocation of Marriage"）；观点论文，匹配「批评」用途 | 充分 |
| 12 | ~~Hamaker et al. 2024~~ → **Muthén, Asparouhov & Witkiewitz 2024**, `10.1037/met0000701` | **Muthén, B. M.; Asparouhov, T.; Witkiewitz, K.** | "Cross-lagged panel modeling with **binary and ordinal outcomes**" | PR | 2 / 4 | CLPM 在二元/序数结果下的问题 | ✅ 修正后**恰好命中** | 充分 |
| 13 | Hamaker & Grasman 2015, `10.1037/a0038889` | Hamaker, E. L.; Kuiper, R. M.; Grasman, R. P. P. P. | "A critique of the cross-lagged panel model" | PR | 2 / 4 | CLPM 批判 | ✅ | 充分 |
| 14 | Lucas 2023, `10.1177/25152459231158378` | Lucas, R. E. | "Why the Cross-Lagged Panel Model Is Almost Never the Right Choice" | PR | 2 / 4 | 「CLPM 几乎从不是对的选择」 | ✅ | 充分 |
| 15 | Robitzsch ~~2025~~ **2024**, `10.1080/10705511.2024.2379495` | Robitzsch, A.; Lüdtke, O. | "A Note on the Occurrence of the Illusory Between-Person Component in the Random Intercept Cross-Lagged Panel Model" | PR | 1 | RI-CLPM 的 illusory between-person component | ✅ 方法论文；**年份订正 `2025` → `2024`**（Crossref `issued`；*Structural Equation Modeling* 32(1):36–45） | 充分 |
| 16 | ~~Cameron & Overall 2015（APIM）~~ → **Cook & Kenny 2005**, `10.1080/01650250444000405` | **Cook, W. L.; Kenny, D. A.** | "The **Actor–Partner Interdependence Model**: A model of bidirectional effects in developmental stu…" | PR | 3 / 4 | APIM 双路径模型 | ✅ 修正后**恰好命中**（标题即含 "Actor–Partner Interdependence Model"）· *Int. J. Behav. Dev.* 29(2):101–109 | 充分 |
| 17 | ~~Ledgerwood, Koval &.Samek 2018~~ → **Gerpott, Balliet, Columbus, Molho & de Vries 2018**, `10.1037/pspp0000166` | **Gerpott, F. H.; Balliet, D.; Columbus, S.; Molho, C.; de Vries, R. E.** | "How do people think about interdependence? A multidimensional model of **subjective outcome interdependence**" | PR | 2 / 3 | `OutcomeDependence` 多维主观模型 | ✅ 修正后**恰好命中**（原归属 Ledgerwood 是**另一构念族**）· *JPSP* 115(4):716–742 | 充分 |
| 18 | ~~Overall, Sibley & Struthers 2018~~ → **Kenny 2018**（单作者）, `10.1111/pere.12240` | **Kenny, D. A.** | "Reflections on the actor–partner interdependence model" | PR | 2 / 3 | APIM 反思 | ✅ 修正后**恰好命中**（单作者文章，原表三人署名不可能成立）· *Personal Relationships* 25(2):160–170 | 充分 |
| 19 | Kenny & La Voie 1984, `10.1111/j.1467-6494.1986.tb00393.x` | **Malloy, T. E.; Kenny, D. A.**（1986） | "The Social Relations Model: An integrative method for personality research" | PR | 2 / 3 | Social Relations Model | ⚠️ 原表已自行披露：DOI 实际是 **Malloy & Kenny 1986** *Journal of Personality* 54(1):199–225（报告著录一致）；Kenny & La Voie 1984 走另一 DOI `10.1016/S0065-2601(08)60144-6`（也已核实）。两条都在。**本行是原表中唯一一处「已知不一致但已披露」的项，Round 3 复验确认该披露为真。** | 充分（无缺陷） |
| 20 | ~~Grzyb & Talboom 2018~~ → **Roisman 2009**（单作者）, `10.1111/j.1467-8721.2009.01621.x` | **Roisman, G. I.** | "Adult Attachment" | PR | 2 / 3 | Adult Attachment 综述 | ✅ 修正后**年份与作者同时订正**（`2018` → `2009`）；*Current Directions in Psychological Science* 18(2):122–126。**注意：该文是 CDPS 的短篇综述，不是 meta-analysis**，措辞不宜用「meta」 | 充分 |
| 21 | ~~Fraley et al. 2005~~ → **Sibley, Fischer & Liu 2005**, `10.1177/0146167205276865` | **Sibley, C. G.; Fischer, R.; Liu, J. H.** | "Reliability and Validity of the Revised Experiences in Close Relationships (**ECR-R**) Self-Report Measure of Adul…" | PR | 2 / 3 | ECR-R 信效度 | ✅ 修正后**恰好命中**（标题即含 "ECR-R"）· *PSPB* 31(11):1524–1536 | 充分 |
| 22 | ~~Chivers et al. 2025~~ → **Junkins, Derringer, Ogolsky, Hardesty & Weisberg 2025**, `10.1111/jftr.70019` | **Junkins, E. J.; Derringer, J.; Ogolsky, B. G.; Hardesty, J. L.; Weisberg, Y.** | "**Measures of Relationship Power Dynamics** in Romantic Relationships" | PR | 3 / 7 | 关系权力动力量表（2025 新工具） | ✅ 修正后**恰好命中**（标题即含 "Measures of Relationship Power Dynamics"）· *JFTR* 18(1):170–191。**⚠️ 交叉印证**：`10.31234/osf.io/f6wbn_v1`（§3.3.1 M4）实测标题与此**同一篇** | 充分 |
| 23 | ~~Eaton & Finkel 2026~~ → **Körner & Overall 2026**, `10.1177/01461672251409849` | **Körner, R.; Overall, N. C.** | "**Bias in Perceptions of Power** in Close Relationships: The Role of Self-Protection, Pro-Relationship, and Power …" | PR | 1 / 7 | 权力知觉偏差 | ✅ 修正后**恰好命中** · *PSPB* | 充分 |
| 24 | Overall ~~et al.~~ **& Hammond** 2026, `10.1146/annurev-psych-012325-032022` | **Overall, N. C.; Hammond, M. D.**（仅 2 位作者） | "Power and Ideology in Close Relationships" | PR | 2 / 6 | 权力与意识形态 | ✅ 题录精化：2 位作者不应用 "et al." · *Annu. Rev. Psychol.* 77(1):393–421 | 充分 |
| 25 | ~~Laurenceau / Bar-Kalifa et al. 2000~~ → **Fletcher, Simpson & Thomas 2000**, `10.1177/0146167200265007` | **Fletcher, G. J. O.; Simpson, J. A.; Thomas, G.** | "The **Measurement of Perceived Relationship Quality Components**: A Confirmatory Factor Analytic Approach" | PR | 2 / 5 | 关系质量成分 CFA | ✅ 修正后**恰好命中** · *PSPB* 26(3):340–354 | 充分 |
| 26 | Gable et al. 2004, `10.1037/0022-3514.87.2.228` | Gable, S. L.; Reis, H. T.; Impett, E. A.; Asher, E. R. | "What Do You Do When Things Go Right? The Intrapersonal and Interpersonal Benefits of Sharing Positive Events" | PR | 2 / 4 | 积极事件分享（capitalization） | ✅ | 充分 |
| 27 | ~~Drigotas, Rusbult, Wieselquist & Whitton 1999~~ → **Fletcher, Simpson, Thomas & Giles 1999**, `10.1037/0022-3514.76.1.72` | **Fletcher, G. J. O.; Simpson, J. A.; Thomas, G.; Giles, L.** | "**Ideals** in intimate relationships" | PR | 2 / 4 | 理想（ideals）vs 现实 | ✅ 修正后**恰好命中** · *JPSP* 76(1):72–89（R14 自查页码 54–71 → 72–89 正确） | 充分 |
| 28 | ~~Gerych 2007~~ → **Gneiting & Raftery 2007**, `10.1198/016214506000001437` | **Gneiting, T.; Raftery, A. E.** | "**Strictly Proper Scoring Rules**, Prediction, and Estimation" | PR | 2 / 3 | strictly proper scoring rules | ✅ 修正后**恰好命中** · *JASA* 102(477):359–378 | 充分 |
| 29 | **Liell-Cock & Staton 2025, `10.1145/3704890`** | Liell-Cock, J.; Staton, S. | "Compositional Imprecise Probability: A Solution from Graded Monads and Markov Categories" | PR | 1 / 3 | credal set 朴素组合系统性过松（R07 D1 的核心） | ✅ 编程语言论文，**该主张的领域归属正确**（组合子的非交换性），不是勉强类比 · *PACMPL* 9(POPL):1596–1626 | 充分 |
| 30 | ~~Bodenmann & Frighi 2011~~ → **Bacon, Conte & Moffatt 2014**, `10.1007/s11238-014-9448-x`（R04）/ `10.1016/j.cpr.2015.07.002`（R10） | **Bacon, P. M.; Conte, A.; Moffatt, P. G.** | "**Assortative mating on risk attitude**" | PR | 1 / 5 | reciprocity 的判别实验 | ❌ **撤回**。`10.1007/s11238-014-9448-x` 实为 *Theory and Decision* 77(3):389–401 的**风险态度同类婚配**研究，**与「reciprocity 的判别实验」无关**（即 M2 的期刊归属错误之外的**第二重**身份错误：作者也错）。R10 的 N=443 落在**另一个 DOI** `10.1016/j.cpr.2015.07.002`（*Clinical Psychology Review*，Falconier et al.）。**「We-ness Questionnaire 完整出版元数据未核实」的自标诚实（R10 L825 / manifest）保持有效。** | **WITHDRAWN / 需重新指向** |
| — | **`10.1007/s11238-014-9448-x`（R04 用于 SOEP 否定判定）** | Bacon, P. M.; Conte, A.; Moffatt, P. G. | "Assortative mating on risk attitude" | PR（著录错） | 1 / 4 | D11 SOEP `NOT_DYADIC_ENOUGH` 的 `negative_evidence_source` | ❌ **期刊归属错误（M2）+ 作者归属错误（第 30 行）。否定判定的唯一依据来源著录不准。** | **MAJOR** |

**修正计数（本 child 独立实测，见 §4.2.1）**

| 类别 | 行 | 数 |
|---|---|---:|
| **作者归属错误** | 6 · 7 · 10 · 11 · 12 · 16 · 17 · 18 · 20 · 21 · 22 · 23 · 25 · 27 · 28 · 30 | **16 / 30 = 53.3%** |
| 题录精化（非作者） | 15（年份 `2025`→`2024`）· 24（2 位作者不应用 `et al.`） | 2 / 30 |
| 原表即正确 | 1 · 2 · 3 · 4 · 5 · 8 · 9 · 13 · 14 · 19 · 26 · 29 | 12 / 30 |
| **合计** | | **30 / 30** |

### 4.2.1 修正审计记录（Round 3 `A1`）

**方法**：对**本表 30 行的 30 个 DOI + 12 个守卫对照行**逐条 `GET https://api.crossref.org/works/<DOI>`（UA `LHRM-R3A1-Repair/1.0`，2026-09-27），取 `author` / `title` / `issued` / `container-title` / `volume` / `issue` / `page`。**脚本 `a1_crossref.py`，完整原始输出留存于 `a1_crossref_out.txt`；调用与逐行输出见 `A01` §13.4。**

**守卫对照的作用（防误改）**：12 个被判定为**原表即正确**的行被**一并复查**以确保本轮没有把它们改坏。实测结果：**12 / 12 与原表著录一致，未改动。** 若不做这一步，「批量修正」很容易把对的行一起改错，而那正是本节要修的缺陷类本身。

**修正的净效果（必须与缺陷计数一起读）**：

| 结果 | 行 | 数 |
|---|---|---:|
| 修正后**该来源与承重主张更贴合**（原归属根本不是这篇论文） | 6 · 7 · 10 · 11 · 12 · 16 · 17 · 18 · 20 · 21 · 22 · 23 · 25 · 27 · 28 | **15** |
| 修正后**该来源不再支撑其承重主张** | **30** | **1** |
| 题录精化，主张不变 | 15 · 24 | 2 |

**这 15 行的修正方向值得单独记录**：原审计把它们记成了 A、B、C 三位并不在作者名单里的人（例如把 "Fourteen Core Principles" 记给 Powers & Overall、把 "Suffocation of Marriage" 记给 Ben-Shahar & Ostrow、把 APIM 记给 Cameron & Overall）。**修正后 Crossref 标题往往与承重主张逐字吻合** —— 这说明**这些主张本身多半是对的，错的是它们被归属给的作者**。**但这不构成对主张内容的背书**：本 child 只读了 Crossref 元数据与题名，**未读任何一篇论文的正文或摘要**，因此**只裁定「身份」，不裁定「该论文是否真的支持该主张」**。后者是 `A01` / `A03` 的职责。

**第 30 行是本轮唯一的实质损失**：「reciprocity 的判别实验」这一承重主张，在其原本指向的 DOI 上**找不到支撑**。该主张可能由 R10 的另一个 DOI（`10.1016/j.cpr.2015.07.002`，Falconier et al. 2015）承载 —— **但本 child 未核该 DOI 是否真的包含一个 reciprocity 判别实验**（那需要读正文）。已登记为 §10 P1。

**与 Round 2 复核的关系**：Round 2 lane `J` 打开 19 行、实测 10 行错；Round 2 `EV2` 独立打开 J 未开的 11 行、实测 6 行错；两者合并覆盖 30 行中的 30 行，得 `≥16/30 ≈ 53%`。**本 child 未复跑 J 与 EV2 的抽样，而是对全部 30 行做了完整复验**（因此本节的分母是确定的 30，不是「至少 30」）。**结果与 `J`/`EV2` 的头条数字一致：16 行作者归属错。** 两处口径差异记录在案：(a) `EV2` §7.2 指出 J 的表实际列 **10** 个 ❌ 而非其散文的 11 —— **本 child 的 16 是独立计数，不依赖该纠正**；(b) `EV2` §7.2 判第 24 行（Overall 2026）为 ✅ —— **本 child 判为「✅ 但需题录精化」**，因为该文只有 2 位作者，写 "et al." 不准确。这是**本 child 与 `EV2` 唯一的实质分歧，且方向是 `EV2` 更宽松。**

**责任归属（沿用 `EV2` §8 non-claim #4，本 child 无新证据改变它）**：本 child **未读 Wave-1 报告正文**，因此**不主张这 16 处错著录是从 lane 继承的还是 `A04` 自行编造的**。`UNDETERMINED`。本 child 主张的是两件可验证的事：**(a) 在 `A04` 的交付物内部，身份列与它自己记录的指针不一致**；**(b) `A04` 的方法声明（§8.3.6 声称核过题名/年份/期刊一致性）与其表结构（无 author/title 列）不相容。**

### 4.2.2 承重层结论（Round 3 重写；**「28 项强度充分」已撤回**）

> **`SUPERSEDED`（Round 3 `A1`，依 M-7 / R-B2）**：上一版本本节结论逐字为：
>
> 「**承重层结论：30 项承重来源中 28 项强度充分；2 项不合格（Joel 2020 转述承重、R04 SOEP 否定判定著录错）。未发现「meta-analysis 被要求承担当需要 primary data 的主张」这一具体失效模式 —— 全 swarm 对 review 类来源的用法（Le&Agnew、Tran、Sargon 等）都是正当的。这是本审计的正面结论，与 A01 的判断方向一致但依据不同（我核的是 DOI 层，不是论证层）。**」
>
> **该结论撤回。** 三条理由：
> 1. **它的分母不可信。** 「28 项强度充分」是在一张 **≥16 行身份错误**的表上作出的。那 28 个 ✅ 每一个都是对**错误的论文**作出的判断，因此**不构成 28 项肯定证据，只构成 28 次未生效的检查**。
> 2. **它的第二句（negative result）现在有反例。** 「未发现 meta-analysis 被要求承担当需要 primary data 的主张」—— 修正后可见第 11 行（`Finkel et al. 2014`，*Psychological Inquiry* 的**观点/评论**文章）与第 20 行（`Roisman 2009`，*CDPS* 的**短篇综述**）都曾被当作 primary 承重。**更根本的是 §2.2.1：tier 判定规则本身把 56% 的非 primary 工作标成了 PRIMARY，所以「未发现误用」这一观察的检出力接近于零 —— 判定规则与被检测对象用了同一套（错误的）primary 定义。** 这不是发现了误用，而是**这个 negative result 不具备发现误用的能力**。
> 3. **它与本报告自身的 §2.2.1 冲突。** 上一版本同时写「350 ← 真正承载科学重量的数字」（已撤回）与「28/30 强度充分」——两者都在用 tier 与计数承载科学重量，而 §2.2.1 证明 tier 不编码证据强度。

**Round 3 的替代结论（三层，逐层降强度）**：

| 层 | 结论 | 强度 |
|---|---|---|
| **L1 身份层** | 30 行的 DOI 身份现已**逐行实测并写入表内**（含 `Author` / `Title` 两列）。**30 / 30 可自证**。「哪一个 DOI 指向谁」这个问题在 `A04` 内部现在**可回答**。 | **可复现的强陈述** |
| **L2 身份-主张匹配层** | 15 行的修正后身份**比原归属更贴合**其承重主张（题名逐字吻合）；12 行原表即正确；**1 行（第 30 行）不再支撑其主张**。**但本 child 只核了题名，未读正文/摘要** —— 因此这一层是「题名层面的匹配」，**不是「论文是否真的支持该主张」的判定**。 | **中等强度的陈述，带明确限度** |
| **L3 强度层** | **`WITHDRAWN`。** 本 child **不主张** 30 项中有多少项「强度充分」。该判断需要读正文，而本轮范围禁止。已登记为 §10 P2。 | **不主张** |

**仍然成立的正面结论（缩小后仍然成立的部分）**：§2.2.1 之外，A04 关于**全局去重**的三层计数（`1,199 → 642 → 533`）与 109 个 `POINTER_ONLY` 的显式剔除**未被本轮任何修正触及**，本 child 独立复算确认其内部算术自洽（`642 − 109 = 533`；tier 表逐行加总 = 533）。**这与承重评估是两件事，不应互相引用。**


---

## 5. `AGENT_RECALL` 承重审计

### 5.1 全 swarm `AGENT_RECALL` 标记分布

> **`SUPERSEDED`（Round 3 `A1` 实测）**：本节上一版本首句写「`AGENT_RECALL` / `UNVERIFIED_AGENT_RECALL` 显式标记共 **85 处 / 16 份文件**」。该句有两个问题：
>
> **(1) `UNVERIFIED_AGENT_RECALL` 在 18 份 lane 文件中出现 0 次。** 本 child 对 18 份 Wave 1 报告做严格 token 检索（`(?<![A-Z_])UNVERIFIED_AGENT_RECALL(?![A-Z_])`），命中 **0**。该字符串在**整个 `docs/research/overnight-2026-09-27/` 语料内只出现在审计文件自身**（`A01` 的 F-12 与 `NR-ALL-1`、以及本行）。**顺带定位了 `A01` F-12 的同一处错误**：F-12 把该 token 归属 **R11**，而 **R11 全文 `AGENT_RECALL` 出现 0 次** —— 一个不写 `AGENT_RECALL` 的 lane 不可能使用 `UNVERIFIED_AGENT_RECALL`。`A01` §3.3 已据此订正，本行同步订正。
>
> **(2) `85 处 / 16 份文件` 不可复现，但本 child 不宣称它错。** 严格 token 计数（把散文中的纪律声明一并计入）实测为 **36 处 / 13 份文件**，逐 lane 为 `01`=2 `02`=8 `03`=2 `04`=1 `05`=3 `06`=2 `07`=1 `09`=3 `10`=2 `12`=3 `13`=1 `14`=7 `17`=1，**其余 5 份为 0**。本 child **不知道 A04 的计数规则**（是否区分「标记」与「纪律声明里的提及」、是否含大小写变体、是否含 `AGENT_RECALL（` 之类的行内用法）。**因此本行标 `NOT_REPRODUCIBLE`，不擅自改数。** 需要 A04 公开其计数规则才能对齐 —— 已登记为 §10 P2。**关键差异点是 R11**：A04 的 16 份文件清单包含 R11，而 R11 的 `AGENT_RECALL` 实测为 **0**。
>
> **本节下方的逐 lane 分布表按原文保留**（其逐 lane 数与本 child 的严格计数口径不同，且其**处置纪律**列的内容 —— 各 lane 的降级声明 —— 本 child 抽样核对后确认在文中确实存在，见 §11 Mission 5）。

`AGENT_RECALL` / ~~`UNVERIFIED_AGENT_RECALL`~~ 显式标记共 **85 处 / 16 份文件**（`NOT_REPRODUCIBLE`，见上方 supersession 注）：

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

> ### ⚠️ Round 3 `A1` 权利/归属声明（依 Architect adjudication **X-7**，逐字要点）
>
> **X-7 裁定：`NO RIGHTS VIOLATION ESTABLISHED; PROVENANCE OMISSION CONFIRMED.`**
>
> 1. **唯一被授权的 LHRM substrate 是冻结的、仅含改写的 Fixture 003 包（frozen paraphrase-only Fixture 003 package）。**
> 2. **StoryCorps 正文 / 音频保持 `HUMAN_REVIEW_REQUIRED / pointer-only`。**
> 3. **不得升级权利状态**（`No rights upgrade`）；**fail-closed 仍然有效**（adjudication §C.7）。
> 4. **本报告（A04）自身不使用任何 Fixture 003 单元。** 实测：对本文件全文检索 Fixture 003 单元编号模式 `S\d{3}` → 命中 5 次，**逐条核对后全部是 Elsevier PII / DOI 字符串**（`S0010-0277(02)0549-8`、`S0065-2601(08)60144-6`）与 lane 内编号 `[S34]`，**没有一个是 Fixture 003 的单元编号**。**A04 未引用、未改写、未重建任何 Fixture 003 正文。**
> 5. **`SC/transcript/pNN` 是指针路径标签，不是证据可得性的主张。** 本报告 §6.3 描述 R13 的做法时使用该路径标签，**其含义是「R13 的文档里出现了这个路径」，不意味着 A04 或任何人曾取得该 transcript 单元**。**本报告不主张、也未依赖任何 transcript / raw / anchored 证据。**
> 6. **本节的缺陷裁定性质**：§6.3 的 F1 与 §6.2 的 F2 是**文档层 provenance 遗漏**（某 lane 的文档没有继承它所用 substrate 的权利边界），**不是**「某 lane 取得了不该取得的材料」的认定。**X-7 明确「未成立权利违反」与本节的两条缺陷裁定不矛盾** —— 前者裁定的是权利事实，后者裁定的是文档完整性。
> 7. **本 child 未做也不主张**：未审计其余 21 份报告的 Fixture 003 使用与权利陈述状态（**不在白名单内**）；未对任何 Fixture 003 单元做内容级评估；未主张任何 rights 状态应当被放宽。

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

> **Round 3 `A1` 按 X-7 限定本节的裁定性质**：F1 是**文档层 provenance 遗漏**，**不是**「权利违反已发生」的认定（X-7：`NO RIGHTS VIOLATION ESTABLISHED; PROVENANCE OMISSION CONFIRMED`）。本节描述的 `SC/transcript/p004`–`p011` 是**R13 文档中出现的指针路径标签**；**A04 自身未取得、未引用、未重建任何 transcript / raw / anchored 证据**，本节不依赖也不主张这类证据可得。见 §6 顶部 Round 3 声明第 4–6 条。

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
| Geyer et al. 1999 EUROFAMCARE | R11 | **未标不确定** | DOI 不解析 —— 但**「前缀与著录期刊族不符」这一理由不成立**（`1662-9647` 正是 GeroPsych 的 ISSN 前缀）。**真实缺陷是 DOI 分隔符错误**：报告写 `10.1024/1662-9647.a000031`（点），真值 `10.1024/1662-9647/a000031`（斜杠）= **Di Rosa, M.; Kofahl, C.; McKee, K.; Bień, B.; Lamura, G.; Prouskas, C. (+2), 2011, *GeroPsych* 24(1):5–18**；**作者也不是 Geyer 1999**。裁定改记 **`UNVERIFIED_DOI`**，见 §3.3.2 D5 | **MODERATE**（理由已订正，缺陷本身仍成立） |
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
6. ~~NEGATIVE｜未发现 meta-analysis 被要求承担当需要 primary data 的主张。30 个承重来源逐条核查，2 个 review 类来源（Le & Agnew 2003、Tran 2019）都只用于它们能承重的 meta 主张。这与 Work Order 的顾虑相反。~~
   > **`SUPERSEDED`（Round 3 `A1`，依 M-7 / R-B2）—— 该 negative result 撤回。**
   >
   > **撤回理由一：分母不可信。** 该结论建立在「30 个承重来源**逐条核查**」之上，而 §4.2.1 实测该表 **16 / 30 行作者归属错误**。**一个身份错了 16 行的表，不能支撑「逐条核查」这四个字。**
   > **撤回理由二（更根本）：该 negative result 不具备发现误用的能力。** 它的检测方式是「检查是否出现 meta-analysis 承担当需要 primary data 的主张」，而**判定 primary 与 meta 的规则本身**（Crossref `type` + 题名正则）**系统性地把理论、方法论、综述、计算模型论文判为 PRIMARY**（§2.2.1 实测 **9/16 ≈ 56%**）。**判定规则与被检测对象共用同一套错误的 primary 定义，因此「未发现误用」的观察接近于零检出力** —— 这不是「查过没查到」，而是「这种查法查不出来」。
   > **撤回理由三：修正后已能举出反例。** 第 11 行（`Finkel et al. 2014`，*Psychological Inquiry* 的**观点/评论**文章）与第 20 行（`Roisman 2009`，*CDPS* 的**短篇综述**）都曾被当作 primary 承重。
   > **仍然成立的部分（缩小后）**：本报告**未发现** Work Order 所担心的那种**具体**失效模式（把一个明确的 meta-analysis 逼去承担当需要 primary data 的主张）在**作者归属原本就正确**的 12 行里发生。**但这不是「未发生」，是「在检出力接近零的检查下未被发现」。** 登记为 §10 P2。
7. **NEGATIVE｜109 个「指针」不是来源。** 若把它们算进来源数，任何"150+/350/500"论证都会失真。
8. **NEGATIVE｜我自己的抽取器制造了 16 个假 `NOT_FOUND`。** 首轮正则排除了 `)` 且误剥 `_`，把 9 个 Elsevier 平衡括号 DOI 和 4 个 Springer/T&F `_` 形态 DOI 弄坏。**已全部修正并逐条核实。** 记录此事实是因为：不修正就会把这 16 个合法 DOI 误报为 swarm 的引用错误 —— 那会是**假阳性**。审计工具的缺陷必须与被审对象的缺陷分开登记。

### 8.2 `remaining_unknown`

| # | 未知项 | 阻塞原因 |
| --- | --- | --- |
| U1 | 257 个 URL 的当前可达性 | 本 lane **未做 HTTP 实测**。不主张任何一个在 2026-09-27 live |
| U2 | 44 个 arXiv id 的存在性 | 只做编号合理性目视检查，未查 arXiv API |
| U3 | 44 个 arXiv id 的 peer-review 状态（多数 TIER=PREPRINT） | 需逐条查是否已发表；其中 `2603.*` / `2604.*` / `2609.*` 太新，不可能有期刊版 |
| U4 | `PEER_REVIEWED_PRIMARY` vs `REVIEW` 的 304 项逐篇判定 | 只用 Crossref `type` + 题名正则。**分项计数是估计值** —— **Round 3 `A1` 已把这一点加重**：该规则有**系统性偏误**（理论 / 方法 / 综述 / 计算模型论文被系统性判为 PRIMARY），分层抽样 **9/16 ≈ 56%** 非 primary empirical work（§2.2.1）。**因此 `PRIMARY = 319` 与 `REVIEW = 31` 的分别计数不仅"不精确"，而是"方向性错误"；`350` 的合计仍可用。** 重出 primary-data 口径的分子需逐篇读摘要，**本轮未做**（§10 P1） |
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

### 8.4 Round 3 `A1` 追加的 non-claims（bookkeeping + citation 修复轮）

11. **我不主张 30 项承重来源中有多少项「强度充分」。** §4.2.2 的 **L3 强度层 `WITHDRAWN`**。本 child 只读了 Crossref 元数据（author / title / issued / container-title / volume / issue / page），**未读任何一篇论文的正文或摘要**。因此本 child **只裁定「身份」，不裁定「该论文是否真的支持该主张」**。
12. **我不主张那 16 处作者错著录的责任归属。** 本 child **未读 Wave-1 报告正文**，因此不主张这些错是**从 lane 继承**的还是 **`A04` 自行编造**的。`UNDETERMINED`（沿用 `EV2` §8 non-claim #4，本 child 无新证据改变它）。
13. **我不主张 §4.2 修正后「更贴合」等于「已被验证」。** 15 行修正后 Crossref **题名**与承重主张逐字吻合，这**只说明身份找对了**。**题名吻合不证明该论文的结论支持该主张。** 这是两个不同的判断。
14. **我不主张 §3.3.4 原清单中除 `h0046049` 外的 14 行是正确的。** 恰恰相反：该节已被证明会产生**假 PASS**（作者 / 年份 / 期刊 / 标题全对，只错在期号），因此其余各行通过的概率**不能假定为高**。它们在本轮一律标 **`NOT_REVERIFIED`** —— 那是把「假保证」降级为「无保证」，**不是**宣称它们错（§3.3.5 的全表重检**未执行**）。
15. **我不主张 `85 处 / 16 份文件` 这个 `AGENT_RECALL` 计数是错的。** 我实测的严格 token 计数是 36 处 / 13 份文件，但**我不知道 A04 的计数规则**，因此标 `NOT_REPRODUCIBLE` 并**不改数**（§5.1）。**唯一确定的是：`UNVERIFIED_AGENT_RECALL` 在 18 份 lane 文件中出现 0 次**，该 token 应从本节的 token 清单中删除。
16. **我不主张 §2.2.1 的 56% 是点估计。** 该抽样是**系统抽样**（每 20 行取 1），**不是随机抽样**；分类依据是**题名与出处类型**，不是对研究设计的判定；本 child **未重跑该抽样**（重跑属新的文献扫描，Round 3 禁止）。它是**区间信息**。
17. **我不主张 `533` / `642` / `1,199` 这三个数被本轮修正触及。** 本轮修正的是 `1,201` 与 `2.3–3.4×`（**这两个数在 A04 侧原本就是错的**），以及 `878` / `1.65×` / `2.51×`。**`642 − 109 = 533` 与 tier 表逐行加总 = 533 这两处算术本 child 复算确认仍成立，未改动一个数字。**
18. **我不主张 M5 / M6 背后的 R05 内容有问题。** 本轮**只撤销了 A04 对这两条 DOI 的错误判定**（实测它们解析成功）。**R05 L506 / L509 的指针是否被正确使用，是 R05 的事，不在本 child 白名单内。**
19. **我不主张任何 Fixture 003 的权利状态应当被放宽或升级。** X-7 明确 `No rights upgrade`，fail-closed 继续有效。本 child 只陈述边界与 provenance 遗漏，**不做任何权利裁定**（权利裁定属 Human）。
20. **我不主张本 child 审计了 Fixture 003 在其余 21 份报告中的使用情况。** §6 顶部声明第 7 条已登记该缺口。

---

## 9. 完整去重来源表（642 行 · 本报告的主要交付物）

**列定义**：`Tier` = provenance tier；`Lanes` = 引用该指针的 lane（已映射为 R00–R17）；`n` = 该指针在 18 份报告中的出现次数；`Resolved` = `Y` = DOI 经 Crossref 或 DataCite 解析成功并与著录一致；`form-only` = URL/arXiv/ISBN 指针形式合法但本 lane 未做可达性实测；`N` = DOI 在 Crossref 与 DataCite 均不解析。

> ### ⚠️ Round 3 `A1`：本表**结构上无法支持作者级检查**（manifest §7 M-7 的根因声明）
>
> **本表没有 `author` 列，也没有 `title` 列。** 这是 §4.2 承重表 **16 / 30 行作者归属错误**能够长期存在于本报告内部的**结构原因**，不是一次抽查疏漏：
>
> - 本表的列把审计者的注意力固定在「**这个指针存不存在、解析到哪、出现在哪些 lane、出现几次、属于哪一层**」这五个问题上。**「这个 DOI 指向的是谁」既没有列可以写，也没有列可以查。**
> - 因此**作者归属错误这一缺陷类在 `A04` 内部不可能被发现** —— 不是「没查」，是**无处可查**。`Resolved = Y` 这一列只保证「DOI 解析到了某篇论文」，**完全不保证「那篇论文是报告想引的那一篇」**。`A04` 的 §8.3 non-claim #6 早已声明「不主张 DOI 对应论文的**内容**正确」，但**作者身份**是一个比「内容」弱得多、也该容易得多的检查 —— 它当时同样没有做，而这一轮证明它会出错 53%。
> - **本表的 `Resolved` 列因此不得被读作「引用正确」。** 它只读作「指针形式有效」。
>
> **为什么本轮没有给这 642 行加 `author` / `title` 两列**（M-7 允许「加两列」或「明确的诚实声明 + 已知坏行列表」二选一，本 child 选后者）：
>
> 1. **只有一部分行能填。** 642 行中 **340 个 DOI** 有 Crossref/DataCite 记录可取；**257 个 URL + 44 个 arXiv + 1 个 ISBN 没有任何作者字段来源**；**109 个 `POINTER_ONLY` 按定义就不是来源**。加列后会得到一张**约 47% 有值、约 53% 空值**的表 —— **空值会被下一位读者误读为「无作者」或「未检查」**，这比没有列更危险。
> 2. **取数据需要一次新的扫描。** 为 340 个 DOI 批量取 author/title 属于新的文献核查动作，Round 3 派发限定「只可复验你实际改动的 DOI，不得扩大范围」。
> 3. **会改动本表 642 行的字节内容**，从而破坏 §12 的字节状态声明与本表的逐行可复现性。**保持本表字节不变 + 另加声明，是本轮可做到的最大诚实度。**
>
> **本 child 的实际处置**：
> - 在**能够逐行复验的地方**（§4.2 的 30 行承重表）**加了 `Author (Crossref)` / `Title (Crossref)` 两列并填满实测值** —— 见 §4.2 与 §4.2.1。
> - **已知坏行清单（即本表的已知作者级缺陷）**：§4.2 的 **16 行**（行 6 · 7 · 10 · 11 · 12 · 16 · 17 · 18 · 20 · 21 · 22 · 23 · 25 · 27 · 28 · 30），其 DOI 全部以 `10.` 开头、**全部可在本表的 DOI 分区中按指针检出**，逐条对应见 §4.2.1。
> - **本表其余 324 个 DOI 行的作者归属状态是 `UNKNOWN`**，既未被验证为正确，也未被验证为错误。**不得假定它们比那 16 行更干净。** 抽样证据表明作者错配率约 **53%**（§4.2.1），**若该比例适用于本表其余部分，本表可能还有约 170 行同类缺陷未被检出** —— **这是本 child 明确不主张已排除的风险**。
> - **登记为 §10 P1**：为 §9 的 340 个 DOI 行取回 author/title 并加列（需 Architect 先裁决范围与是否分批）。

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
| **P2** | ~~修 M4–M6：`10.31234/osf.io/…` → `10.31219/osf.io/…`（R02 ×1、R05 ×2）~~ **`REJECTED_WITH_REASON`（Round 3 `A1`）** | §3.3.1 | **不执行。** `10.31234` 与 `10.31219` **两个前缀都 live、注册者同为 `Center for Open Science`**（本 child 已实测 Crossref prefix registry，2026-09-27）。**执行本建议会把 PR 内一条 live 指针 `10.31219/osf.io/gu8z7`（R14 L353，本 child 实测 Crossref 200）变成 404，且不修复任何东西**（`10.31234` 侧的 M5 / M6 实测本来就解析成功，已撤销）。`f6wbn` 的正确修法是**补 `_v1`**，该修法已由修复轮应用 | **无人（已否决）** |
| **P2** | 修 F3：R17 源表条目 37 的「Fixture 001–003 推荐」标 `SUPERSEDED`（引 R00 S-4） | §6.4 | R17 窄修复 |
| **P2** | 修 F2：R16 §9 的 rights 取舍讨论接入项目自身 Case Bank 侧 pointer-only 边界 | §6.2 | R16 窄修复 |
| **P2** | 改 R10 L550 的「见 #22」→ 改指 `19_SYNTHESIS_CANDIDATE.md` 的 gap 表 | §6.5 | R10 窄修复 |
| **P2** | 给 R03 补 D5 式的未命中披露（Geyer et al. 1999 DOI 不解析 + 前缀与著录期刊族不符） | §3.3.2 D5 | R11 窄修复（R11 的缺口表） |
| **P3** | 把 `00_MANIFEST.md` §3 的「单 lane 自报指针数」行替换为本报告 §2.1 的三层计数，并加一句「peer-reviewed-only = 350」 | §2.3 | parent（durable writeback） |
| **P3** | 全 swarm 统一 DOI 书写规范：一条来源在正文与源表内**只写一种形态**，推荐裸 `10.xxxx/yyy`；`https://doi.org/` 形式只用于需要点击的场景 | §2.1 / A04-C10 | parent，写入 `00_CHILD_CONTRACT.md` 下一版 |
| **P3** | 清理 11 个 `exa.ai/library/…` 指针：换成真实 DOI / 出版商 landing URL，或标 `POINTER_ONLY` 并明确不作为论据 | §1.3 | R03（7 条）/ R08b（4 条） |
| **P3** | 清理 2 个截断 URL（`d.docksci.com/download`、`…/does-relationship-satisfaction-always-mean-satisfaction-`）与 1 个重复 slug（Cambridge Episteme `polarization-paradox`） | §1.3 | R03 / R08b |

### 10.1 Round 3 `A1` 新增 / 改判的待办

| P | 动作 | 触发的发现 | 谁做 | 状态 |
|---|---|---|---|---|
| **P0** | **修第 30 行的承重主张「reciprocity 的判别实验」**：其原本指向的 DOI（`10.1007/s11238-014-9448-x`）经实测是 Bacon, Conte & Moffatt 2014 的风险态度同类婚配研究，**与该主张无关**。需确定该主张的正确来源（候选：R10 的另一 DOI `10.1016/j.cpr.2015.07.002` = Falconier et al. 2015），**或降级该主张** | §4.2 第 30 行 / §4.2.1 | R10 窄修复 + A04 复核 | **未执行**（需读正文才能确认候选 DOI 是否含 reciprocity 判别实验） |
| **P1** | **对 §3.3.4 的 15 行做完整的 volume / issue / 页码 级重检。** 该节已被证明会产生假 PASS（`10.1037/h0046049` 实为 *Psych Review* **63(5):277–293**，原记 63(4) 判 ✅）。**只撤回错项、保留其余 ✅ 会让那些 ✅ 继续被当作保证使用** | §3.3.4 / §3.3.5 | 需 Architect 先裁决是否分批 | **未执行**（属新的核查扫描，Round 3 范围禁止） |
| **P1** | **为 §9 的 340 个 DOI 行取回 `author` / `title` 并加两列**，消解「本表结构上无法支持作者级检查」这一根因。**注意：只有 DOI 行可填；257 URL + 44 arXiv + 109 `POINTER_ONLY` 无作者字段来源** | §9 Round 3 声明 | 需 Architect 先裁决范围 | **未执行** |
| **P1** | **重出 primary-data 口径的分子**：逐篇读摘要，把 `PEER_REVIEWED_PRIMARY = 319` 中真正的一手经验研究与理论/方法/综述/计算模型分开。**在此之前 `319` 不得被引用为「319 篇一手经验研究」** | §2.2.1（9/16 ≈ 56% 非 primary） | 需 Architect 先裁决是否值得做 | **未执行** |
| **P2** | **公开 §5.1 的 `AGENT_RECALL` 计数规则**，使 `85 处 / 16 份文件` 可复现（本 child 严格 token 计数为 36 处 / 13 份文件；关键差异点是 R11 实测为 0）。同时从 §5.1 的 token 清单中删除 `UNVERIFIED_AGENT_RECALL`（**该 token 在 18 份 lane 文件中出现 0 次**） | §5.1 Round 3 supersession | A04（自身） | **部分执行**：token 清单已删；计数规则未公开 |
| **P2** | **把 §4.2 的 L3 强度层重出**：读 30 篇正文，判定每项是否真的支撑其承重主张。**当前状态 `WITHDRAWN`，不得引用「28 项强度充分」** | §4.2.2 | 需 Architect 先裁决 | **未执行** |
| **P2** | **改写 `00_MANIFEST.md` §2b 的 OSF 前缀段**（「`10.31219` 是 OSF project 前缀」为事实错误；「`10.31234` 前缀非法」不成立） | §3.3.1 Round 3 警示 | **`A2` / parent**（`00_MANIFEST.md` **不在本 child 白名单内**） | **已路由，未执行** |
| **P2** | **同步改写 `19_SYNTHESIS_CANDIDATE.md` §2 C-8 的同源陈述** | §3.3.1 Round 3 警示 | **`A2` / parent**（同上） | **已路由，未执行** |

---

## 11. `status_recommendation`

> ### ⚠️ Round 3 `A1` 改判（依 M-5…M-9）
>
> **上一版本的总评是 `SUCCESS`（附 1 项 `PARTIAL` 子范围声明）。Round 3 改判为 `PARTIAL`（3 项 `PARTIAL` mission + 2 项限定 + 3 项 `WITHDRAWN`）。**
>
> **改判理由（一句话）**：本报告在其**自身承载结论的三处**上被证伪 —— §2.1 的 lane 求和（`1,201` 不成立）、§4.2 的承重表（**16/30 作者归属错**，且结构上无法自查）、§3.3.4 的「已通过」清单（含假 PASS）。**这三处都不是「估计误差」，而是「检查已执行但产生了错误结论」。** 一个 mission 自评为 `SUCCESS` 却在三处产出错误结论的审计，其总评不能是 `SUCCESS`。
>
> **未被证伪、且本 child 独立复算确认仍成立的部分**：§2.1 的三层计数（`1,199 → 642 → 533`）、`642 − 109 = 533`、tier 表逐行加总 = `533`、109 个 `POINTER_ONLY` 的显式剔除、§3.3.3 的 16 个抽取器假阳性自陈、§5.2 的 18 条 `AGENT_RECALL` 逐条裁定、§6.5 的隔离边界 9 处核对。**这些是本报告真正扎实的部分。**

**`PARTIAL`（Round 3 改判；Mission 2 / 4 / 5 降级，Mission 3 加限定）**

理由：

1. **Mission 1（全局去重）= SUCCESS。** 1,199 raw → 642 distinct pointer → 533 distinct source，三层计数 + 642 行逐条表 + 109 个副本的显式剔除。§4 B-3 关闭。
2. **Mission 2（provenance tiering）= `PARTIAL`（Round 3 `A1` 改判，原为 `SUCCESS`）。** 附**声明**：304 个 journal-article 的 PRIMARY/REVIEW 切分是题名启发式，非逐篇判定（U4）。**Round 3 加重**：该规则有**系统性偏误** —— 理论 / 方法论 / 综述 / 计算模型论文被系统性判为 PRIMARY，分层抽样 **9/16 ≈ 56%** 非 primary empirical work（§2.2.1）。**因此 tier 编码的是「出处类型」，不是「证据强度」；`350` 可用作「350 个同行评审来源」，不得用作科学重量的代理。** 上一版本把 `350` 标为「← **真正承载科学重量的数字**」，该措辞**已撤回**。
3. **Mission 3（DOI integrity sweep）= `SUCCESS`（Round 3 部分限定）。** **340 / 340 = 100% coverage**，无遗漏。331 解析成功，9 不解析，3 类 mismatch 全部定位到 lane 与行号，另登记 16 个我自己抽取器造成的假阳性。<br>**Round 3 限定一**：M4 / M5 / M6 三条 mismatch 的**判定前提被证伪并已撤销**（实测 `10.31234/osf.io/rs7eu_v1` 与 `…/dus42` 解析成功；两个前缀都 live）。**M1 / M2 / M3 三条本 child 独立复查确认仍成立。**<br>**Round 3 限定二**：§3.3.4 的「已通过」清单**含一条假 PASS**（`10.1037/h0046049`），已撤回并改标 `NOT_REVERIFIED` + 全表重检要求（§3.3.5）。**该节不再作为免检清单使用。**
4. **Mission 4（load-bearing）= `PARTIAL`（Round 3 `A1` 改判，原为 `SUCCESS`）。** 30 项承重来源**已逐行复验身份**并新增 `Author` / `Title` 两列（§4.2.1），实测 **16 / 30 行作者归属错误（53.3%）**。<br>**原结论「30 项中 28 项强度充分」已撤回**（§4.2.2）：L1 身份层 `SUCCESS`（30/30 可自证）· L2 身份-主张匹配层 `PARTIAL`（题名层面，**未读正文**）· **L3 强度层 `WITHDRAWN`**。
5. **Mission 5（author attribution）= `PARTIAL`（Round 3 `A1` 改判，原为 `SUCCESS`）。** 5 处 Wave 1 自报修正**逐条复核全部正确**；2 处遗留不确定（AR-15/AR-16 承重、Geyer 未披露、Hirschfeld 年份 1 年差）。<br>**Round 3 加重**：本 mission 在**本报告自身的承重表上**实测出 **16 / 30 = 53%** 的作者归属错误，且根因是**表结构缺 `author` / `title` 列**（§9 Round 3 声明）。**「author attribution = SUCCESS」这一自评在 Round 3 之后不成立。**
6. **Mission 6（provenance-of-provenance）= `SUCCESS`（Round 3 按 X-7 加权利/归属声明，mission 本身不改判）。** 三份 fixture 的 rights 边界逐 lane 传递审计；发现 1 MAJOR（R13 丢失 Fixture 003 边界）+ 1 MODERATE（R16）+ 1 MODERATE（R17 引用 superseded 段）。隔离边界 9 处逐处核对，1 MINOR（R10 L550 路由）。<br>**Round 3 补充**：按 adjudication **X-7**（`NO RIGHTS VIOLATION ESTABLISHED; PROVENANCE OMISSION CONFIRMED`）在 §6 顶部加了权利/归属声明，并把 F1 / F2 的性质明确为**文档层 provenance 遗漏**而非权利违反认定；同时记录 **A04 自身不使用任何 Fixture 003 单元**（`S\d{3}` 命中 5 次逐条核对全为 Elsevier PII / lane 内编号）。**本 mission 的三条缺陷裁定在 X-7 之后全部仍成立** —— X-7 裁定的是权利事实，与文档完整性是两件事。
7. **Mission 7（AGENT_RECALL audit）= `PARTIAL`（Round 3 `A1` 改判，原为 `SUCCESS`）。** 18 个 `AGENT_RECALL` 条目逐条裁定，2 条承重，全部在 R14。<br>**Round 3 限定**：§5.1 首句的 token 清单含 `UNVERIFIED_AGENT_RECALL` —— **该 token 在 18 份 lane 文件中出现 0 次**（本 child 实测），应从清单删除；`85 处 / 16 份文件` 的计数**不可复现**（本 child 严格 token 计数 = 36 处 / 13 份文件），但**因 A04 的计数规则未公开，本 child 不宣称它错**，标 `NOT_REPRODUCIBLE`。**18 条逐条裁定本身未被证伪。**

**`WITHDRAWN`（Round 3 新增；这些结论已被撤回，不得再被引用）**

| 原结论 | 位置 | 撤回理由摘要 |
|---|---|---|
| 「30 项承重来源中 **28 项强度充分**」 | §4.2.2 | 分母不可信（16/30 身份错）；L3 强度层需读正文，本轮未做 |
| 「**未发现** meta-analysis 被要求承担当需要 primary data 的主张」 | §8.1(6) | 该 negative result 的检出力接近于零 —— 判定规则与被检测对象共用同一套错误的 primary 定义（§2.2.1） |
| 「`PEER_REVIEWED_PRIMARY + REVIEW = 350` ← **真正承载科学重量的数字**」 | §2.2 | tier 编码出处类型，不编码证据强度；抽样 9/16 ≈ 56% 非 primary empirical |
| 「各 lane 自报数相加 ≈ **1,201**……与实测 A = 1,199 一致（差 2）」 | §2.1 | 真值 875 / 878；与 1,201 差 −323。且 lane 自报数与原始出现数**不同量纲**，该「一致性校验」是范畴错误 |
| 「**3 处 DOI 前缀/后缀结构非法**」 | §3.3.1 M4–M6 | 两个前缀都 live、注册者同为 `Center for Open Science`；M5 / M6 实测解析成功，已撤销 |
| 「前缀与著录期刊族不一致」（D5） | §3.3.2 D5 | `1662-9647` 正是 GeroPsych 的 ISSN 前缀，并无冲突；真实缺陷是 DOI 分隔符 |
| §3.3.4 的「**已通过**」标记 | §3.3.4 | 含假 PASS（`10.1037/h0046049` 实为 63(5)）；该标记**不承载信息**，其余各行改标 `NOT_REVERIFIED` |

**`PARTIAL` 子范围（原有 1 项 + Round 3 新增 1 项）**：
1. **（原有）U6** —— 80 个 `UNSTABLE_COPY` 与已解析 DOI 的对应关系未能机械解算。因此 533 应读作**去重仍可能不完整的上界**（真实 distinct source ≤ 533）。这不改变任何结论方向 —— 只会让 distinct source 更小，而 `PEER_REVIEWED_PRIMARY + REVIEW = 350` 不受影响（350 全部来自已解析 DOI / 明确 tier 的 URL）。
2. **（Round 3 新增）§4.2 的 L2 / L3 层** —— 30 行身份已实测可自证，但「该论文是否真的支持该承重主张」**需要读 30 篇正文，本轮范围禁止**。因此**不得引用任何关于承重强度的判断**，包括本报告上一版本自己给出的那个。已登记 §10.1 P2。

**本报告未做的事（Round 3 追加）**：未对 §3.3.4 做全表 volume/issue/页码 重检（§10.1 P1）；未重出 primary-data 口径的分子（§10.1 P1）；未为 §9 的 340 个 DOI 行取回 author/title（§10.1 P1）；未公开 §5.1 的 `AGENT_RECALL` 计数规则（§10.1 P2）；未审计其余 21 份报告的 Fixture 003 使用与权利陈述状态（**不在本 child 白名单内**）；未修改 `00_MANIFEST.md` / `19_SYNTHESIS_CANDIDATE.md`（**`A2` 拥有**）。

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

### 12.1 Round 3 `A1` 对本节的影响（字节状态）

**Round 3 修改了本文件的哪些字节，逐项声明**：

| 区域 | 是否改动 | 理由 |
|---|---|---|
| §0 结论摘要（A04-C2 / C4 / C5） | **已改** | 追加 Round 3 限定，未删除原句 |
| §1 方法与去重规则（§1.1–§1.3） | **未改一字节** | 全局去重规则与三层计数未被本轮修正触及 |
| §2.1 三层计数表（`1,199` / `642` / `533` / `2.25×`） | **未改** | 本 child 独立复算确认自洽 |
| §2.1 lane 求和句 | **已改**（`1,201` → `878`） | M-6 |
| §2.2 tier 表的数字 | **未改**（`319` / `31` / `350` / `62` / `57` / `47` / `7` / `9` / `109`） | 数字未被证伪；被证伪的是**把 350 读作科学重量**的措辞 |
| §2.3 裁定表 | **已改**（第三行） | M-6 |
| §3.2 / §3.3.1（M1–M3 未改，M4–M6 已改）/ §3.3.2（D5 已改，D1–D4/D6 未改）/ §3.3.3 | 见各行 | — |
| §3.3.4 整节 | **已改** | M-8：标题、假 PASS 撤回、逐行 `NOT_REVERIFIED` 标注 |
| §4.2 承重表 | **已改**（新增 2 列 + 18 行修正） | M-7 |
| §5.1 | **已改**（首句加 supersession） | `UNVERIFIED_AGENT_RECALL` 幽灵 token |
| §5.2 / §5.3 逐条裁定 | **未改** | 18 条裁定未被本轮证伪 |
| §6.2 / §6.3 / §6.4 裁定 | **未改**（仅加 Round 3 限定段） | X-7 是限定不是推翻 |
| §6.5 | **未改** | 隔离边界 9 处核对未被证伪 |
| §7.1 | **未改一字节** | 本 child 未复跑该 6 行（其结论仍成立） |
| §7.2 | **已改**（Geyer 行） | D5 理由订正的连带 |
| §8.1 | **已改**（第 6 条撤回） | M-7 |
| §8.2 | **已改**（U4 加重） | M-7 关联 |
| **§9 的 642 行表本体** | **未改一字节** | 见 §9 Round 3 声明第 3 条：保持本表字节不变 + 另加声明 |
| §10 | **已改**（P2 改判 + 新增 §10.1） | 见 §10.1 |
| §11 | **已改**（总评 `SUCCESS` → `PARTIAL`） | M-5…M-9 |
| §12 本节 | **已改**（追加 §12.1） | — |

**因此：§9 的 642 行表仍可按 §1.1 的抽取规则复现，本文件 §2.1 的三层计数仍有效。** Round 3 **没有**重跑全量指针抽取（那会是一次新的扫描），**只复验了本 child 实际改动的 33 个 DOI**（`a1_crossref.py`，输出留存 `a1_crossref_out.txt`）。**若 parent 在 Round 3 之后对 lane 文件施加了新的窄修复，需按 §1.1 重跑抽取并 diff。**
