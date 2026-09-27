# A01_EVIDENCE_QUALITY_AUDIT

> **Lane:** `A01` — Evidence quality audit（Wave 2 跨 lane 审计阶段）
> **Work Order:** `youling/lhrm#30@overnight-opencode-exploration-swarm-v1`
> **Status:** `PARTIAL`（见 §9 `status_recommendation`）
> **审计对象:** `docs/research/overnight-2026-09-27/` 下 18 份 Wave 1 报告（R00–R17）
> **审计基准（snapshot）:** 2026-09-27 09:1x 抓取的只读副本，逐文件 SHA-256 见 §2.3
> **权限:** 无 GitHub 写权限；本文件为 research packet，**未修改 `D:\coding\lhrm` 任何文件**
> **本文件不是 canonical architecture。** 本目录下所有文件都是 `RESEARCH_CANDIDATE`。

### Round 3 `A1` 修复记录（bookkeeping + citation repair，依 `ARCHITECT_ADJUDICATION_V1`）

本节声明 Round 3 对本文件做过的全部改动。**原始审计文本一律保留**，每处改动都带 `SUPERSEDED` 注记（原文 + 取代依据）。

| # | 位置 | 改动 | 依据 |
|---|---|---|---|
| 1 | §0 第 2 条 | 「10 个 DOI 完全不解析」→ **9** | manifest §7 **M-5** 关联项 / `EV2` §5.8 第二块 |
| 2 | §1.1 Crossref 解析行 | `353/353（100%）` → **`337/353（95.5%）`** | manifest §7 **M-5**（`J-C13`） |
| 3 | §1.1 反查行 | `11` 标 **`NOT_RECONCILED`**，不改数 | `EV2` §5.8 变更说明（四数互斥簇） |
| 4 | §1.1 词频行 | `17 个标签` → 标 `SUPERSEDED`，指向 §3.3 | Round 3 实测 |
| 5 | **§3.3（新增）** | 证据等级词汇台账：F-12 的 12 个变体逐个复跑 + 9 个未枚举写法 | Round 3 实测 |
| 6 | **F-12** | 订正 `UNVERIFIED_AGENT_RECALL`（R11）= **幽灵 token**，出现 0 次 | Round 3 实测 |
| 7 | **F-35** | 「逐 lane 相加的 **788+**」→ **878** | manifest §7 **M-2** / `EV2` §4.1 |
| 8 | **NR-ALL-1** | 标 **`PROPOSAL_NOT_APPLIED`** + 写明落地前置条件 | X-14（不得声称已实施） |
| 9 | **NR-ALL-5** | `788+` → **878** | 同 #7 |
| 10 | **NR-ALL-7（新增）** | 登记四个互斥「未命中」数的消解动作 | `EV2` §5.8 |
| 11 | **§10.3.0（新增）** | 83 项 `NARROW_REPAIR_REQUEST` 执行状态台账（`EXECUTED` 10 / `PARTIAL` 31 / `NOT_EXECUTED` 31 / `UNPROBEABLE` 11）+ (i)(ii)(iii) 三分类 | Round 3 派发「重新机械计数，绝不复制旧总数」 |
| 12 | **§13（新增）** | Round 3 的复算脚本、命令与逐项输出 | 可复现性 |
| 13 | §1.4（新增） | `[ESTABLISHED]` 与 Fixture 003 两项词表/边界声明 | 见 §1.4 |

**本 child 的白名单内另一份文件** `A04_CITATION_PROVENANCE_AUDIT.md` 同步修复（见该文件 §0 Round 3 记录）。**`00_MANIFEST.md` 与 `19_SYNTHESIS_CANDIDATE.md` 由 `A2` 拥有，本 child 未触碰。**

---

## 0. 一句话结论（先说最要紧的）

**没有发现任何一条"被凭空捏造的文献"（fabricated citation）。** 353 个被引 DOI 中 337 个（95.5%）在 Crossref 解析成功，另有 5 个为 DataCite 注册、3 个属报告自陈的 `FETCH_FAILED` 而**未被用于任何结论**。arXiv 预印本指针抽查 2 个全部真实存在。

**但发现 3 类实质缺陷：**

1. **29 个 DOI「解析到一篇真实论文，但不是报告所引的那一篇」**（作者/年份/期刊错配）。这比死链更危险：死链会自己暴露，错配不会。
2. **9 个 DOI 完全不解析**（Crossref 404 + `doi.org` 404），其中 3 个是承重引用。

> **`SUPERSEDED`（Round 3 `A1` 修复，依 manifest §7 M-5 / `EV2` §5.8）**：上一版本本行写「**10** 个 DOI 完全不解析」。该数与本文件其它三处互斥：`:15` 的 `337/353 = 95.5%`、§1.1 的 `353 − 337 = 16`（= 9 死链 + 5 DataCite + 1 `.pdf` 格式错 + 1 字面占位符）、§3.1 的 `DEAD_BOTH = 9`。**唯一与本文件 tier 表自洽的数是 9**（9/353 = 2.5%）。已改为 9。
> **仍未消解的一处**：§1.1「缺失引用反查」行写「**11 条**死链，9 条找到了正确 DOI」。`11` 与 §3.1 的 `DEAD_BOTH = 9` 不一致，但该行描述的是**反查步骤的输出**（含报告侧格式错与占位符），本轮**无法从本文件内部重算**，故标 `NOT_RECONCILED` 而非改数。见 `NR-ALL-7`。
3. **证据等级词表在 18 个 lane 之间漂移**，且存在 lane 间对 `CITED_PRIMARY` 的**互相矛盾定义**；R03/R13 两条产出来源最多的 lane 几乎不给证据等级。

**BLOCKER 3 条，MAJOR 12 条，MINOR 20 条（共 35 条 findings）。全部为指针/标签/措辞层，无一条要求重做构念裁决。**

---

## 1. 审计方法（可复现）

### 1.1 做了什么

| 步骤 | 工具 | 覆盖 |
|---|---|---|
| DOI 全量抽取 | Python 正则 `10\.\d{4,9}/[^\s CJK]+` + 尾缀规范化 | 18 份报告，**588 处出现 / 353 个唯一 DOI** |
| Crossref 解析 | `https://api.crossref.org/works/<DOI>` | **337/353（95.5%）**；余 16 条经 `doi.org` 定向探测，16/16 确认不解析（其中 5 条为 DataCite 注册、3 条为自陈 `FETCH_FAILED`） |
| `doi.org` 重定向探测 | `HEAD https://doi.org/<DOI>`（禁跟随重定向） | 16 个 Crossref 未命中者 **16/16** |
| 语义匹配（标题/作者/年份） | 人工逐条比对 Crossref 元数据 ↔ 报告行 | 353 中全部做过「作者是否出现在引用行」「CR 年份是否出现在引用行」自动筛查 + **48 + 18 条人工细读** |
| 承重数值核对 | Crossref abstract 抽取 | 9 个承重数字（Tran 2019 / Mayo 2021 / de Bel 2019 / Körner 2026 / Eberhardt 2025 / Hassebrauck 2002 / Falconier 2015 / Bodenmann 2011 / Liddell & Kruschke 2018） |
| arXiv 存在性 | `arxiv.org/abs/<id>` 直接抓取 | 40 个中抽 **2 个**（`2603.22735`、`2604.23178`），另 1 个经 API 单查（`2304.03442`） |
| 缺失引用反查 | Crossref `query.bibliographic` | 11 条死链，**9 条找到了正确 DOI** —— **`NOT_RECONCILED`**：`11` 与 §3.1 的 `DEAD_BOTH = 9` 不一致（见 §0 supersession）。本轮未重跑该步骤，**不擅自改数** |
| 证据等级词频 | 字符串计数 | 18 份报告 × **17 个标签** —— **`SUPERSEDED`**：Round 3 `A1` 实测，18 份 lane 文件里 tier 形态的 token 共 **21** 个不同写法（见 §3.2 词汇台账）。`17` 这个数在任何地方都无法复现 |
| 时间敏感性 | `As of` / 核实日期 头部字段扫描 | 18 份报告 |
| 语料稳定性 | 抓取前后 SHA-256 比对 | 20 个文件 |

### 1.2 抽样原则（按承重性排序，非随机）

优先审计：(a) 被多条其他主张依赖的承重引用；(b) 格式可疑的 DOI（旧式 Elsevier 带括号 DOI、含 `.pdf` 后缀、末位数字易位）；(c) 自陈 `PARTIAL` 的 lane（R02 / R04 / R11 / R15 / R16）；(d) R01 中 38 个自标 ✓ 的 DOI（全量核，见 §4.1）；(e) `00_MANIFEST.md` §2「核心证据指针」列出的每一条（这是 manifest 对外承诺的证据基础）。

### 1.3 明确没有做的

- **未逐条读取任何一篇论文全文。** 只用了 Crossref 元数据（title / author / year / container-title / abstract）与摘要级文本。
- **未重估任何数值。** 只核对「报告写的数字是否与我能拿到的元数据/摘要一致」。
- **未裁定任何构念裁决的对错。** 那是 A02/A03 与 Architect 的事。
- **未读取 `#20/#21/#22`**，未触碰 Eye / Juece。
- **未做跨 lane 全局去重**（A04 的职责）。本报告的行号与计数均以 §2.3 的 snapshot 为准。

### 1.4 Round 3 补充：两术语表与边界声明

#### 1.4.1 `[ESTABLISHED]` —— 本文件**不使用**该标签，故不新增定义

Round 3 派发要求：「`[ESTABLISHED]` 不在 A01 自己的 convention 表里 —— 若 A01 使用它，要么补定义，要么停止使用它。」

**处置选择：停止使用（事实上已经不用）。**

**实测依据**：对 `A01_EVIDENCE_QUALITY_AUDIT.md` 全文（1053 行）做大小写不敏感的字面检索，`ESTABLISHED` **命中 0 次**。本文件从 Wave 2 起草至今**从未使用**该标签。

**为什么选「停止使用」而不是「补定义」**：
1. **补定义等于凭空造一个等级。** 本文件的等级词汇现状已在 §3.3 记录为「21 个 tier 形态写法、11 个属 F-12 枚举、其中 1 个是幽灵 token、且 R10 与 R07 对 `CITED_PRIMARY` 的定义互相矛盾」。在这种状态下新增第 22 个 `ESTABLISHED`，会**加重** F-12 记录的那个缺陷，而不是缓解它。
2. **语义上它与本文件的职责不匹配。** AGENTS.md「Research discipline」要求区分 `Human requirement | empirical evidence | model hypothesis | architecture decision | implementation detail`，并明令「Do not label an unvalidated formula, parameter, weight, probability, causal relation, distance metric, normalization rule, or state transition as scientifically established」。本文件是**证据质量审计**，它的产出是**指针层缺陷裁定**，没有哪一条 finding 达到「scientifically established」。加一个 `ESTABLISHED` 等级等于给审计报告本身预留了一个会被误用的最高档。
3. **加定义需要裁决，不在 bookkeeping 修复的权限内。** 若 Architect 后续要在 18 lane 范围内确立一个可用的最高等级，它应当作为 `NR-ALL-1` 的**一部分**裁决（那才是规范化提案的落点），而不是由一个 bookkeeping repair child 单独引入。

**残留风险（记录）**：其它 lane 或 `A04` 若使用 `ESTABLISHED`，本文件不会因此失效，但**跨文件不可比性**会再增一项。已列入 packet 的 `conflicts_and_routes`，交 parent / Architect 决定是否需要一次全语料检索。

#### 1.4.2 Fixture 003 权利/归属边界（X-7）—— 本文件**不使用** Fixture 003 单元，故无权利义务，但记录边界

**Architect X-7 裁决（逐字要点）**：**未成立权利违反；已确认 provenance 遗漏。** LHRM 唯一被授权的 substrate 是**冻结的、仅含改写的（paraphrase-only）Fixture 003 包**；StoryCorps 正文/音频保持 `HUMAN_REVIEW_REQUIRED / pointer-only`。**不得**升级权利状态。

**本文件的使用情况（实测）**：
- 对 `A01_EVIDENCE_QUALITY_AUDIT.md` 全文检索 Fixture 003 的单元编号模式 `S\d{3}` → 命中 10 次，**逐条核对后全部是 Elsevier PII / DOI 字符串**（`S0010-0277(02)0549-8`、`S0065-2601(08)60144-6`、`S0140-1971(86)80043-4`、`S0004-3702(98)00023-X`、`S0378-8733(99)00010-6`、`S0065-2601(08)…` 等）与 lane 内编号 `[S34]`，**没有一个是 Fixture 003 的单元编号**。
- 检索 `Fixture 003` / `StoryCorps` / `pointer_only` / `HUMAN_REVIEW_REQUIRED` → 命中 **0** 次。

**结论**：**A01 不使用 Fixture 003 的任何单元，因此不产生权利陈述义务，也不存在「暗示曾取得 transcript / raw / anchored 证据」的措辞。** 本小节记录该边界，以便下游读者不必重新检索即可确认 A01 在 Fixture 003 上的地位。

**同一语料内其余文件的状态（只登记，不代为修复）**：`A04` §6 有完整的 Fixture 003 权利基线与逐 lane 传递审计（该文件由本 child 同步修复，X-7 相关措辞已按裁决调整）。**其它 21 份报告是否使用 Fixture 003 单元、以及是否遗漏权利陈述，不在本 child 的白名单内**，已列入 packet 的 `conflicts_and_routes`。

---

## 2. 覆盖声明（诚实版）

### 2.1 审计深度分级

| 深度 | 报告 | 说明 |
|---|---|---|
| **D3 全量机器核验 + 人工细读** | `01` `02` `02b` `03` `04` `05` `06` `07` `08b` `09` `10` `11` `12` `13` `14` `15` `16` `17` | 18/18 全部做过：DOI 全量解析、作者/年份自动筛查、证据等级词频、时间敏感性扫描、绝对化措辞扫描 |
| **D2 承重引用语义核对** | 同上 18 份，但只对 48 条「作者名不匹配」+ 18 条「年份不匹配」+ manifest 点名引用做了人工比对 | — |
| **D1 承重数字摘要核对** | `02` `02b` `03` `10` `11` `14` `09` | 9 个数字 |
| **D0 未做** | `15_CASEBANK_EXPANSION.md` 的 **法律文书实体内容**（`SUBSTANCE_NOT_READ` 是 R15 自陈的，我未推翻也未确认）；全部非 DOI 指针（URL、ISBN、issue 编号、dataset 官方文档）的可访问性 | 见 §2.2 |

### 2.2 明确的缺口（不要把本报告当已覆盖）

1. **非 DOI 指针未做可访问性探测。** 353 个 DOI 全部核过；报告里还有大量 `https://` URL（如 `exa.ai/library/...`、`sage.cnpereading.com`、`ir.lawnet.fordham.edu`、`xbgjxt.swu.edu.cn`、`link.springer.com/...pdf`），我**只**核了其中出现在 DOI 位置的那少数几条。URL 死链率本次**未知**。
2. **ISBN / 官方文档版本号 / issue comment id 未核。**
3. **arXiv 只核了 40 个中的 2–3 个。** arXiv API 在本次会话中持续返回 429/连接错误（这一点我必须写明：第一次批量查询 43 个 ID **全部**返回 MISSING，包括我已单独证明存在的 `2304.03442`——即该 API 通道整体不可用，不构成"指针无效"的证据）。改用 `arxiv.org/abs/` 直抓后 2/2 真实。
4. **未做内容级语义验证。** "这篇论文是否真的支持这句话"只在 9 个承重数字上做了摘要级核对；其余 340+ 条只核到"这篇论文存在且书目正确"。
5. **未审计 Wave 1 child packet**（`C:\Users\gg828\AppData\Local\Temp\opencode\lanes\R*_packet.md`）。只在 R01 的 durable 报告本身指不到证据等级表时，把这一点记为发现（见 F-11）。
6. **snapshot 之后 corpus 又被改过。** 见 §2.3。

### 2.3 ⚠ 语料在审计期间被并发修改（操作层发现）

我在同一会话内两次读取同一文件，得到不同的行号与不同的 DOI 出现次数（`11_GENERAL_HUMAN_DYADS_SCOPE.md` 从 52,133 B 增至 68,450 B；`02b_CONSTRUCT_REDUNDANCY_AUDIT.md` 从 46,006 B 增至 64,549 B）。**Wave 1 报告在本 lane 审计期间仍处于可写状态。**

因此本报告所有行号以如下 snapshot 为准（抓取时刻：2026-09-27，`mtime` 见括号）：

| 文件 | 字节 | 行 | SHA-256 前 16 | mtime |
|---|---|---|---|---|
| `00_CHILD_CONTRACT.md` | 4,121 | 64 | `c7731bcb1e0ac85d` | 07:14:41 |
| `00_MANIFEST.md` | 10,751 | 100 | `02589642a0456061` | 09:01:39 |
| `01_CURRENTNESS_AND_GAP_MAP.md` | 54,301 | 409 | `38dff89427c5138e` | 08:32:54 |
| `02_CONSTRUCT_CONVERGENCE.md` | 63,165 | 507 | `7abe9b27cf733bfd` | 08:32:56 |
| `02b_CONSTRUCT_REDUNDANCY_AUDIT.md` | 64,549 | 644 | `6ff63de9fc524809` | 09:08:11 |
| `03_MEASUREMENT_INSTRUMENTS.md` | 78,264 | 413 | `30aab4319ee3e02d` | 08:33:22 |
| `04_DATASET_LANDSCAPE.md` | 85,461 | 1022 | `6e4e905512cb736b` | 08:33:34 |
| `05_IDENTIFICATION_AND_STATISTICS.md` | 80,891 | 608 | `cfea2fd61b4b8aa8` | 08:33:35 |
| `06_TRANSITION_LAWS.md` | 71,246 | 1058 | `396c9dc2febd350d` | 08:32:51 |
| `07_PARTIAL_OBSERVABILITY.md` | 56,843 | 611 | `2bb99140ae9830b0` | 08:33:20 |
| `08b_BELIEF_DECEPTION_KNOWLEDGE.md` | 90,131 | 812 | `e1ea93a93dc10174` | 08:32:57 |
| `09_DYNAMIC_SYSTEMS_AND_HYSTERESIS.md` | 83,181 | 810 | `277aea98bece4b09` | 08:59:20 |
| `10_MUTUALITY_POWER_DEPENDENCE.md` | 77,608 | 838 | `5679a13784f6f4bd` | 08:33:16 |
| `11_GENERAL_HUMAN_DYADS_SCOPE.md` | 68,450 | 558 | `3d3c8748e16407d4` | 09:10:29 |
| `12_COMPUTATIONAL_MODELS_ABM.md` | 67,762 | 507 | `f754a6c4a79693f8` | 08:34:10 |
| `13_LLM_SKILL_INTERVIEW_LAYER.md` | 67,875 | 739 | `4642f1c8fc7b8ac6` | 08:33:20 |
| `14_PAPER_POSITIONING_NOVELTY.md` | 55,998 | 412 | `78194ee1959c9991` | 08:33:43 |
| `15_CASEBANK_EXPANSION.md` | 42,312 | 346 | `d022656afa726194` | 08:33:56 |
| `16_EMPIRICAL_VALIDATION_PROTOCOL.md` | 74,789 | 607 | `1c323be2d115ec3a` | 08:52:52 |
| `17_RED_TEAM_FALSIFIERS.md` | 62,803 | 618 | `7f8c9fb4809a8217` | 08:33:31 |

> **注意 R02b / R09 / R11 / R16 / `00_MANIFEST` 的 mtime 晚于 08:3x 的批量写入。** R11 与 R02b 很可能在本 lane 审计期间刚被追加了内容。**parent 在按本报告行号做 repair 前必须先冻结 corpus**，否则行号会再次失效。

**Git 层面的旁证（本 lane 只读 `git status` / `git diff --stat` / `git log`，无写操作）：**

```
$ git -C D:\coding\lhrm rev-parse --abbrev-ref HEAD
research/opencode-overnight-2026-09-27
$ git -C D:\coding\lhrm rev-parse HEAD
2d392bae1d60619575d90cf68e29b838d8f1043b
$ git -C D:\coding\lhrm log --oneline -3
2d392ba research: overnight-2026-09-27 manifest Wave 1 terminal state + blocker register
8ee07c2 research: overnight-2026-09-27 Wave 1 durable writeback (R00-R17, 18 lane reports)
ce1a774 research: overnight-2026-09-27 CP1 manifest skeleton + child contract

$ git -C D:\coding\lhrm status --porcelain
 M docs/research/overnight-2026-09-27/02b_CONSTRUCT_REDUNDANCY_AUDIT.md
 M docs/research/overnight-2026-09-27/11_GENERAL_HUMAN_DYADS_SCOPE.md

$ git -C D:\coding\lhrm diff --stat
 .../02b_CONSTRUCT_REDUNDANCY_AUDIT.md              | 107 +++++++++++++++++++--
 .../11_GENERAL_HUMAN_DYADS_SCOPE.md                |  98 +++++++++++++++++++
 2 files changed, 198 insertions(+), 7 deletions(-)
```

即：`00_MANIFEST.md` 声明的 Wave 1 终态 commit（`2d392ba`）**已经产生**，但 `02b` 与 `11` 在**工作区里还有 198 行未提交的追加内容**。**§5 中所有指向 `02b_*` 与 `11_*` 的行号都可能已被这 198 行推移。** 这两文件的 owner 应先说明这 198 行的来源（Wave 2 audit repair？还是 lane 重跑？），再由 parent 决定本报告哪些行号需要重算。

---

## 3. 量化总览

### 3.1 DOI 解析结果（353 个唯一 DOI）

| 状态 | 数量 | 占比 |
|---|---|---|
| Crossref `RESOLVED` + 书目与引用一致 | **308** | 87.3% |
| Crossref `RESOLVED` + **但书目与引用错配** | **29** | 8.2% |
| Crossref 404 且 `doi.org` 404（**死链**） | **9** | 2.5% |
| Crossref 404 但 `doi.org` 302（DataCite 注册，**有效**） | **5** | 1.4% |
| Crossref 404、报告侧带 `.pdf` 后缀（**格式错，实际可解析**） | **1** | 0.3% |
| 报告侧字面占位符 `10.1177/…`（R17 自陈 `FETCH_FAILED`） | **1** | 0.3% |
| **合计** | **353** | 100% |

**按"有效指针"口径：343/353 = 97.2% 可解析。**
**按"书目正确"口径：308/353 = 87.3%。**

### 3.2 证据等级标签使用量（跨 lane 漂移的证据）

| 报告 | `CITED_PRIMARY` | `CITED_SECONDARY` | `AGENT_RECALL` | `UNVERIFIED*` | DOI token 数 |
|---|---|---|---|---|---|
| `01` | 1 | 1 | 2 | 1 | 10 |
| `02` | 3 | 8 | 8 | 3+10 `NO_DOI_VERIFIED` | 51 |
| `02b` | 13 | 11 | 0 | 6 | 33 |
| `03` | **0** | 4 | 2 | 30 | **112** |
| `04` | 27 | 0 | 1 | 3 | 11 |
| `05` | 1 | 22 | 3 | 15 `UNKNOWN_AS_OF` | 53 |
| `06` | 1 | 2 | 2 | 1 | 23 |
| `07` | 30 | 5 | 1 | 2 | 21 |
| `08b` | **61** | 10 | 0 | 3 | 24 |
| `09` | 10 | 5 | 3 | 3 | 3 |
| `10` | 2 | 2 | 2 | 9 | 38 |
| `11` | 4 | 2 | 0 | 5 | 45 |
| `12` | 1 | 8 | 3 | 7 | 28 |
| `13` | 2 | 1 | 1 | 0 | 26 |
| `14` | **0** | 5 | 7 | 3 | 53 |
| `15` | 10 | 2 | 0 | 17 | 0 |
| `16` | 2 | 2 | 0 | 7 | 26 |
| `17` | 16 | 7 | 1 | 8 `FETCH_FAILED` | 33 |

> `CITED_PRIMARY` 的分布从 **0**（`03`、`14`）到 **61**（`08b`），跨度极大，且与各 lane 产出的具名指针数**不成比例**。这不是质量差异的直接证据，但它说明**该标签在不同 lane 不是一个可比较的量**——这本身是审计发现（见 F-12）。

### 3.3 证据等级词汇台账（Round 3 `A1` 实测；**这是枚举，不是规范化**）

**方法**：对 18 份 Wave 1 lane 报告全文跑 `\b(?:CITED|UNVERIFIED|AGENT|NO_DOI|SUBSTANCE|POINTER|NOT_VERIFIED)[A-Z_]*\b`，按 token 去重计数。

**本文件不定义 canonical 等级表。** 下面三张表是**观测到的写法枚举**，**不是**本审计批准的分级方案；把其中任何一个映射到统一的 5 级或任何级别，都需要 Architect 裁决（见 `NR-ALL-1`，该条是**提案**，状态 `PROPOSAL_NOT_APPLIED`）。

**表 A｜F-12（F-12 行）枚举的 12 个变体 —— 逐个复跑结果：11 个真实存在，1 个是幽灵 token。**

| F-12 枚举的 token | F-12 归属 | Round 3 实测出现次数 | 实测出现于 | 裁定 |
|---|---|---:|---|---|
| `CITED_PRIMARY` | 全 swarm | 172 | `01 02 02b 04 05 06 07 08b 09 10 11 12 13 16 17` | ✅ 存在 |
| `CITED_SECONDARY` | 全 swarm | 97 | 15 份 lane | ✅ 存在 |
| `AGENT_RECALL` | 全 swarm | 36 | `01 02 03 04 05 06 07 09 10 12 13 14 17` | ✅ 存在 |
| `UNVERIFIED_DOI` | R03 / R14 | 30 | `02 03 14` | ✅ 存在 |
| `UNVERIFIED`（裸用） | 未归属 | 32 | `02 02b 03 04 06 07 10 11 15` | ✅ 存在（F-12 未单列） |
| `NO_DOI_VERIFIED` | R02 / R03 | 10 | `02` | ✅ 存在（实测只在 `02`） |
| `UNVERIFIED_CANDIDATE` | R15 | 8 | `15` | ✅ 存在 |
| `CITED_PRIMARY_CONTENT` | R15 | 10 | `15` | ✅ 存在 |
| `SUBSTANCE_NOT_READ` | R15 | 7 | `15` | ✅ 存在 |
| `CITED_PARTIAL` | R09 | 4 | `09` | ✅ 存在 |
| `CITED_METADATA` | R07 | 3 | `07` | ✅ 存在 |
| `UNVERIFIED_POINTER` | R09 | 3 | `09` | ✅ 存在 |
| **`UNVERIFIED_AGENT_RECALL`** | **R11** | **0** | **无** | ❌ **幽灵 token —— 见下方 supersession** |

> **`SUPERSEDED`（Round 3 `A1` 实测）**：F-12 原文枚举 12 个变体并把 `UNVERIFIED_AGENT_RECALL` 归属 R11。实测：**(a) `UNVERIFIED_AGENT_RECALL` 在 18 份 lane 文件中出现 0 次**——该字符串只出现在 A01 自身（F-12 与 `NR-ALL-1`）；**(b) R11（`11_GENERAL_HUMAN_DYADS_SCOPE.md`）全文 `AGENT_RECALL` 出现 0 次**，因此 R11 不可能使用 `UNVERIFIED_AGENT_RECALL`。**「12 个变体」应改为「F-12 枚举 12 个，其中 11 个实测存在」。** 依据：Round 3 `A1` 对 18 份 lane 报告的全文 token 计数（脚本与输出见 §12）。

**表 B｜实测存在、但 F-12 未枚举的 tier 形态 token（9 个）—— F-12 的枚举不完备。**

| token | 实测次数 | 出现于 | 说明 |
|---|---:|---|---|
| `CITED_CLASSIC` | 6 | `17` | 疑似 `CITED_*` 家族的第四种写法 |
| `UNVERIFIED_AS_OF` | 9 | `04 16` | 形态上像 tier，实际语义是「截至某时未核」的时间限定符 |
| `UNVERIFIED_HYPOTHESIS` | 4 | `15` | 疑似字段限定符而非等级 |
| `UNVERIFIED_CONTENT` | 3 | `08` | 疑似字段限定符 |
| `UNVERIFIED_OR_UNKNOWN` | 3 | `12` | 疑似把「未核」与「未知」两个不同轴压进一个 token |
| `UNVERIFIED_OFFICIAL_ACCESS` | 2 | `15` | 疑似可达性轴而非证据等级轴 |
| `UNVERIFIED_VOL_PAGES` | 1 | `02` | 疑似字段级限定符 |
| `CITED_PRIMARY_SECONDARY` | 1 | `04` | **两个等级的合并写法，语义不可判定** |
| `CITED_PRIMARY_FULLTEXT` | 1 | `13` | 与 R07 的 `CITED_METADATA` 争夺「读到正文」这一格的定义权 |

**表 C｜Round 3 `A1` 的计数与限度。**

- F-12 枚举 **12** → 实测存在 **11**。
- 表 B 另有 **9** 个 F-12 未枚举的写法。
- 连同裸 `UNVERIFIED`，本轮实测的 tier 形态 token 合计 **21**。
- **但「21」同样是下限而非定论。** 三个理由：(1) 上表的 token 集合由正则 `[A-Z_]+` 决定，带连字符、小写、或以 `…_AS_OF_2026-09-27` 形式书写的等级（如 R11 的 `DOI_UNKNOWN_AS_OF_2026-09-27` 记法）**不在计数内**；(2) 哪些 token 是「等级」、哪些是「字段限定符」，**本文件与各 lane 都未定义**（例：`UNVERIFIED_VOL_PAGES` 到底是等级还是「卷期页码未核」的字段标记）；(3) 本轮**未**统计同一 token 在同一 lane 内的定义是否一致——已知 R10 与 R07 对 `CITED_PRIMARY` 给出互相矛盾的定义（F-12），同类冲突**必然还有**，只是本轮没有逐 lane 拉取定义文本。
- **因此本节的唯一结论是：跨 lane 的 `CITED_PRIMARY` 计数不可比较，跨 lane 的任何等级计数都不可相加。** 这个结论不依赖「到底是 12 个还是 21 个」——两者都 ≥ 12，都远超可比较的门槛。

---

## 4. 承重引用抽样核对（本次抽样声明）

### 4.1 `00_MANIFEST.md` §2「核心证据指针」列 —— 逐条核

manifest 向外承诺的每一条核心证据，我全部单独核对过。

| manifest 声明 | 核对结果 |
|---|---|
| R00 `main ee393ca2`；23 blob tree | 未核（GitHub API 写权限外，且 R00 自带 live recheck 记录） |
| R01 "45 条带 DOI 指针；Sibley 2012 / Lewicki 1998 / Chivers 2010 / Tran 2019" | Sibley 2012 = `10.1177/0146167205276865`（实为 **Sibley, Fischer & Liu 2005** ECR-R 量表题录）→ **年份/作者错，manifest 与报告同源错误**；其余三条 ✓ |
| R02 "Tran 2019 R²=.54" | ✓ 摘要确认 N=50,427 / 202 samples / r=.65·.53·−.43；R²=.54 与之自洽 |
| R03 "41 instrument family / 54 条目" | 计数自报，未核 |
| R04 "16 数据集" | 计数自报，未核 |
| R05 "Hamaker 2015 / Lucas 2023 / Robitzsch 2025" | `10.1111/pere.12072` 归属 R03；Hamaker 2015 = `10.1037/met0000701`（实为 **Hamaker et al. 2024** Psychological Methods）→ 见 F-06 |
| R06 "Joel 2020 PNAS；Schrodt 2014；Johnson 2022 PNAS" | Joel 2020 摘要确认"11,196 couples / 45% / 无人格特质加成 / 无法预测变化方向" ✓；其余未核 |
| R07 "QSR/Renz 2007" | 未核（`10.2307/2265159` 是 Belnap 1976，见 F-04） |
| R08 "W3C PROV；Kripke–Harman 修正 Kuhn 误引" | W3C PROV 未核；Kuhn 相关 4 条 DOI **全部错配**（F-05） |
| R09 "Bühler & Orth 2022/2024/2025；Mayo 2021 meta ES=.09" | Mayo 2021 DOI ✓ 存在；ES=.09 / I²=76% 我**未能在摘要层核对**（Crossref 无 abstract）→ 标 `NOT_VERIFIED_BY_A01` |
| R10 "Bodenmann 2011 判别实验 N=443；Falconier 2015 N=17,856" | 两篇书目 ✓（Bodenmann 2011 = `10.1027/1016-9040/a000068`, *European Psychologist* 16:255–266；Falconier 2015 = `10.1016/j.cpr.2015.07.002`, *Clinical Psychology Review* 42:28–46）。N 值我未在摘要层确认 |
| R11 "de Bel 2019 N=549；Bengtson 2002；Johnson 2006" | de Bel 2019 摘要**逐字确认** "Multilevel analyses of **549** sibling–parent–sibling triads from the **Netherlands Kinship Panel**" ✓ 且 enhancement 强 / loyalty conflict 弱 ✓ 与 R11 表述一致 |
| R12 "Windrum 2007；Galán 2009；Schindler 2013；Snijders 2010；Hills & Todd 2008" | 未逐条核；R12 引用指针本身 28 个 DOI 全部解析 |
| R13 "Gilardi 2023 vs Nakamura 2026 直接冲突" | 未核（Gilardi 2023 = CHI `10.1145/3544548.3581044` 族；本 lane 未核） |
| R14 "PRQC 2000；Joel 2020；Finkel 2017；Eberhardt 2025 ω=.953" | Eberhardt 2025 摘要**逐字确认** ω=0.953 / CFI=0.968 / SRMR=0.022 / RMSEA=0.108 / Llama 3.1 8B / 120 题取前 8 / 1,131 sessions / 155 patients ✓✓（全 swarm 核验最干净的一条）；Finkel 2017 = `10.1146/annurev-psych-010416-044038` ✓ |
| R15 "`Zapp` 官方原文级" | 未核（`FETCH_FAILED` 环境） |
| R16 "Kapoor 2023 leakage 八分类；Dwork 2015 reusable holdout" | 未核 |
| R17 "Joel 2020；Segal & Fraley 2016；Eastwick 2011" | 未逐条核 |

**manifest 核心指针中我确认错误的：R01 的 Sibley 年份、R05 的 Hamaker 年份、R07 的 Belnap 指针。3 条。**

### 4.2 9 个承重数字的摘要级核对

| 数字 | 出处 | 报告声明 | Crossref 摘要实际 | 判定 |
|---|---|---|---|---|
| `N=50,427` / `k=202` / `r=.65` | Tran, Judge & Kashima 2019 (`10.1111/pere.12268`) | R02b L286/L459 | "50,427 participants from 202 independent samples … satisfaction r=0.65, investments r=0.53, quality of alternatives r=−0.43" | **✓ 一致** |
| `R²=.54 (95% CI [.53,.55])`、`β²=.47/.32/−.19` | 同上，R02b L286 | — | 摘要给 r 值，**未给 R² 的 CI，也未给 β²** | **⚠ 精度超出来源**（F-15） |
| `N=1,304 dyads` / 4 samples / Truth-and-Bias | Körner & Overall 2026 (`10.1177/01461672251409849`) | R10 L332/L536 | "Across four samples of friendships, same-gender couples, and woman–man couples (**N = 1,304 dyads**), we used Truth and Bias models…" | **✓ 逐字一致** |
| `ω=.953` / `CFI=.968` / `SRMR=.022` / `RMSEA=.108` / 120 题取前 8 | Eberhardt et al. 2025 (`10.1038/s41598-025-14923-y`) | R14 L105 | "strong reliability (ω = 0.953), and acceptable fit (CFI = 0.968, SRMR = 0.022), except RMSEA = 0.108 … Llama 3.1 8B LLM rated 120 engagement items, averaging the top eight" | **✓ 逐字一致** |
| `N=549` sibling–parent–sibling triads / Netherlands Kinship Panel | de Bel et al. 2019 (`10.1177/0192513X19860181`) | R11 L149/L155 | 逐字一致 | **✓ 一致** |
| 四维 `intimacy/agreement/independence/sexuality`、德加复本、intimacy 最大 sexuality 最小 | R14 L63 用 `10.1111/1475-6811.00017` | 归给 "Neubauer, Voss & Asendorpf (2015)" | 摘要确认四维 + 德/加复本 + intimacy 最大 sexuality 最小；**但作者是 Hassebrauck & Fehr (2002)** | **✗ 指针错配**（F-03） |
| `100%` 用度量模型处理序数数据 | Liddell & Kruschke 2018 (`10.1016/j.jesp.2018.08.009`) | R09 L205/L536 | 摘要逐字："we surveyed all articles in JPSP, PS, and JEP:G that mentioned the term 'Likert,' and found that **100% of the articles that analyzed ordinal data** did so using a metric model"；"no sure-fire way to detect these problems"；"averaging across multiple ordinal measurements does not solve" | **✓ 逐字一致，且 R09 保留了 "that analyzed ordinal data" 这一关键限定** |
| `~45%` / 无人格加成 / 无法预测变化 | Joel et al. 2020 PNAS (`10.1073/pnas.1917036117`) | R14 O-13 | "11,196 romantic couples … explained approximately 45% of their current satisfaction. The partner's judgments did not add information, nor did either person's personalities or traits. Furthermore, **none of these variables could predict whose relationship quality would increase versus decrease over time**" | **✓ 一致** |
| `N=443` 瑞士伴侣 / `17,856` 人 / `k=202` | Bodenmann 2011 / Falconier 2015 | R10 L447/L453 | Crossref 无 abstract | **NOT_VERIFIED_BY_A01** |

---

## 5. findings table

> 严重度定义：
> **BLOCKER** = 承重引用不解析 / 指向错误作品，或标签错误足以使下游裁决失效。
> **MAJOR** = 书目错配、证据等级定义冲突、承重数字精度超出来源、审计基线不稳定。
> **MINOR** = 年份差一期、期刊名不符、格式瑕疵、措辞过强但方向正确。

| # | 报告 · 行 | 具体主张 | 缺陷类型 | 严重度 | 修法 |
|---|---|---|---|---|---|
| **F-01** | `03_MEASUREMENT_INSTRUMENTS.md:146` 与 `:336` | `X9 \| Perceived Responsiveness and Insensitivity Scale (PRI-16/PRI-8) \| Crasta, Rogge, Maniaci & Reis (2021), Psychological Assessment, 10.1037/2021-17028-001`，判为 **`DIRECT_PROXY`**，并据此写「强 directed：i 感知 j 的 responsiveness」「Study 3 APIM 显示 i 的 PRI 与 j 的自报行为相关」「N=2,334；PRI-8 R α=.93 ω_WP=.83」 | `POINTER` | **BLOCKER** | DOI `10.1037/2021-17028-001` 在 Crossref **与 `doi.org` 均 404**。正确 DOI 是 **`10.1037/pas0000986`**（*Psychological Assessment* 2021，"Toward an optimized measure of perceived partner responsiveness: Development and validation of the perceived responsiveness and insensitivity scale"，Crasta, Rogge, Maniaci, Reis — 已实测解析，PsycTests 条目 `10.1037/t79142-000`）。**这是全 swarm 最承重的一条测量主张**：LHRM 的核心是 `DirectedState_(i→j)`，而 PRI 是 R03 里唯一被判为「强 directed」的 `DIRECT_PROXY`。 |
| **F-02** | `14_PAPER_POSITIONING_NOVELTY.md:98` 与 `:400` | 「ATOMIC 2020（`10.1609/aaai.v35i1.16792`）… 报告 **GPT-3 few-shot 比用 ATOMIC 训练的 BART 模型低约 12 个百分点**（参数少 430×）」 | `POINTER` | **BLOCKER** | `10.1609/aaai.v35i1.16792` 双 404。正确为 **`10.1609/aaai.v35i7.16792`**（**i7** 不是 i1；Hwang, Bhagavatula, Le Bras, Da… *AAAI* 2021, "(Comet-) Atomic 2020: On Symbolic and Neural Commonsense Knowledge Graphs" — 已实测解析）。R14 把它列为**「值得注意的反证」并用它支持 LHRM 的 schema-first 立场**，且 `00_MANIFEST.md` R14 行也复述。数字（12pp / 430×）我未核。 |
| **F-03** | `10_MUTUALITY_POWER_DEPENDENCE.md:786`（正文 `:461` 复述） | 「Lehne, Y., & Bodenmann, G. (2019). *Dyadic coping in couples: a conceptual integration and a research agenda*. *Frontiers in Psychology*, 10, 571. `10.3389/fpsyg.2019.00571` — **S38**」 | `POINTER` | **BLOCKER** | DOI 解析成功，但作者与副标题都不是它：Crossref = **Falconier, Mariana Karin; Kuhn, Rebekka**, "Dyadic Coping in Couples: A Conceptual Integration and **a Review of the Empirical Literature**"。Lehne & Bodenmann 的 Frontiers 2019 不是这一篇。R10 用它承载「评述 139 项研究」这条承重证据。 |
| **F-04** | `10_MUTUALITY_POWER_DEPENDENCE.md:804` | 「Emerson, R. M. (1962). Power-dependence relations. *American Sociological Review*, 27(3), 31–41. `10.2307/2092623` — **S49**」 | `POINTER` | **MAJOR** | `10.2307/2092623` = **Gouldner, A. W. (1960), "The Norm of Reciprocity: A Preliminary Statement", *ASR***。Emerson 1962 的正确 JSTOR id 是 **`10.2307/2089716`**（已实测解析）。这是整个 power/dependence 理论支点的引用。 |
| **F-05** | `08b_BELIEF_DECEPTION_KNOWLEDGE.md:752, 755, 777, 791, 800, 810` | 6 条 `CITED_PRIMARY`/`CITED_SECONDARY` 引用，作者/期刊系统性错配：Sharon→Borges(2015)；Bornstein→Goodie/Doshi/Young（且期刊 BJDM≠BJDP）；Bosson→Lackenbauer et al.；Uuk et al.→Bar-Shachar & Bar-Kalifa（且 JSPR≠JPSP）；Audi→Goldberg & Henderson（且 *Mind*≠*PPR*） | `POINTER` + `LABEL` | **MAJOR** | 逐条替换为 Crossref 实测作者/期刊。其中 `:810`（Audi / Goldberg-Henderson）最严重：**内容正确、指针指向另一篇同题论文**，读者按指针读会读到错误来源。R08b 同时是该 lane 唯一给出 61 个 `CITED_PRIMARY` 的 lane，标签强度与实际核验强度不匹配（F-12）。 |
| **F-06** | `05_IDENTIFICATION_AND_STATISTICS.md:539` 与 `:572` | 「Hoffmann, L., Lehrke, M., & Todt, E. (1985). *J. Educational Statistics*. `10.3102/10769986024002179`（DOI `UNKNOWN_AS_OF`）」；「*The Impact of Family Background and Early Marital Factors on Marital Disruption*. *JMF*. `10.1177/019251391012001003`（作者 `UNKNOWN_AS_OF`）」 | `POINTER` | **MAJOR** | 两个 DOI 都解析成功但都不是所指作品：前者 = **Vermunt, Langeheine & Bockenholt (1999), "Discrete-Time Discrete-State Latent Markov Models…", *JEBS***；后者 = **Bumpass, Martin & Sweet (1991), *Journal of Family Issues***（不是 *JMF*）。R05 已自标 `UNKNOWN_AS_OF`，但把一个**可解析且指向他人论文**的 DOI 标成"未核实"是错误的不确定性声明——它掩盖了"这是错的"而非"不知道"。 |
| **F-07** | `02b_CONSTRUCT_REDUNDANCY_AUDIT.md:533` / `:596`；`02b:576`；`02b:577`；`02b:589`；`02b:430` | 预印本 `https://doi.org/10.31234/osf.io/f6wbn` 双 404；`10.1177/0265407518822783` 归 "Le & Agnew (2006) *JPSP*"；`10.1002/ejsp.1926` 归 "Agnew et al. (2013)"；`10.1111/j.1475-6811.1997.tb00145.x` 归 "Acker, M. (1997)"；`10.1111/joop.12395` 与 "Zanella Delatorre & Wagner 2020" 并列 | `POINTER` | **MAJOR** | 正确值：预印本 = **`10.31234/osf.io/f6wbn_v1`**（带 `_v1`；对应期刊版 `10.1111/jftr.70019` = Junkins, Derringer, Ogolsky, Hardesty, Weisberg 2025 — R02b 未写作者）；`0265407518822783` = **Coy, Davis, Green & Etcheverry (2019), *JSPR***；`ejsp.1926` = **Macher, S. (2012)**；`tb00145.x` = **Lamm & Wiesmann (1997)**；`joop.12395` = **Gottfredson, Wright & Heaphy (2022)**（Zanella Delatorre & Wagner 是另一篇）。均已实测解析。 |
| **F-08** | `11_GENERAL_HUMAN_DYADS_SCOPE.md:502` | 「Geyer, S., et al. (1999). A typology of caregiving situations… *GeroPsych*, 24(1). `10.1024/1662-9647.a000031`」 | `POINTER` | **MAJOR** | 正确 DOI 是 **`10.1024/1662-9647/a000031`**（**斜杠**，不是点；已实测解析）。同一记录的实际作者是 **Di Rosa, M., Kofahl, C., McKee, K., Bień, B., et al. (2011)**，不是 "Geyer 1999"。R11 自陈 `PARTIAL`，这是其中一条可低成本修好的。 |
| **F-09** | `02_CONSTRUCT_CONVERGENCE.md:484` 与 `:465` | `:484`「Ackerman, S. J. (2021). *Social and Personality Psychology Compass*. `10.1111/spc3.12308` ✓」；`:465`「Roisman, G. I., & Fraley, R. C. (2019). Adult attachment: Toward a rapprochement of methodological cultures. `10.1111/j.1467-8721.2009.01621.x` ✓」 | `POINTER` + `LABEL` | **MAJOR** | 两条**自标 ✓**（R01 §10 声明「DOI 已核验者标 ✓」）但都错：`spc3.12308` = **Reis, Lemay & Finkenauer (2017), "Toward understanding understanding"**；`j.1467-8721.2009.01621.x` = **Roisman, G. I. (2009), "Adult Attachment", *Current Directions in Psychological Science***（单作者，2009）。后者尤其要注意：`14_PAPER_POSITIONING_NOVELTY.md:70` 用**同一个 DOI** 写 "Roisman (2009)"——R01 与 R14 对同一 DOI 给出互相矛盾的题录。R11（`:23`）与 R17（`:514`）还各自独立指出 §2.4 的跨文化稳定性判据"超出了文献共识"。**38 个 ✓ 中 2 个是错的（5.3%）。** |
| **F-10** | `02_CONSTRUCT_CONVERGENCE.md:457` | 「Sibley, C. G., Fischer, R. D., & Liu, J. H. (**2005**). *PSPB*, 31(11), 1524–1536. `10.1177/0146167205276865` ✓」 | `POINTER` | **MAJOR** | DOI 解析正确（Sibley, Fischer & Liu 2005, ECR-R 题录，*PSPB* 31(11)），**年份 2005 是对的**；错的是 `00_MANIFEST.md:49` 把它写成「Sibley **2012**」。manifest 错误会传染给任何只读 manifest 的下游。此项**报告侧无误，manifest 侧需修**。 |
| **F-11** | `02_CONSTRUCT_CONVERGENCE.md:503` | 「证据分级（`CITED_PRIMARY` / `CITED_SECONDARY` / `AGENT_RECALL`）见 parent packet `R01_packet.md` §2 的 sources 表，**该表应随本文一并 durable writeback**」 | `LABEL` + `AUTHORITY` | **MAJOR** | durable 报告本体**不含**证据等级表。R01 有 51 个 DOI token，但正文只有 3 `CITED_PRIMARY` / 8 `CITED_SECONDARY` / 8 `AGENT_RECALL` / 10 `NO_DOI_VERIFIED`；**manifest 承诺的「45 条带 DOI 指针」中，大部分在 durable 报告内没有可核的证据等级**。等级表停留在非 durable 的 temp packet 里 → 引用者无法判断任一主张的证据强度。 |
| **F-12** | 全 swarm；代表 `10:757` vs `07:8` | R10 定义 `CITED_PRIMARY` = 「本次实际读到原文/原始摘要/**出版元数据**」；R07 明确把 `CITED_METADATA`（只核到 DOI 元数据，未读正文）**单列为低于 `CITED_PRIMARY` 的等级** | `LABEL` | **MAJOR** | 两条 lane 对同一标签给出**互相矛盾**的定义。此外词表在 18 个 lane 间至少出现 12 个变体：`CITED_PRIMARY` / `CITED_SECONDARY` / `CITED_METADATA`（R07）/ `CITED_PARTIAL`（R09）/ `UNVERIFIED_POINTER`（R09）/ `AGENT_RECALL` / `NO_DOI_VERIFIED`（R02/R03）/ `UNVERIFIED_DOI`（R03/R14）/ `UNVERIFIED_AGENT_RECALL`（R11）/ `UNVERIFIED_CANDIDATE` / `CITED_PRIMARY_CONTENT` / `SUBSTANCE_NOT_READ`（R15）。**后果：跨 lane 的 `CITED_PRIMARY` 计数不可比较，`00_MANIFEST.md` §3 的"全 swarm 指针数"更不可相加。**<br>**`SUPERSEDED`（Round 3 `A1` 实测，详见 §3.3）**：本行枚举的 12 个变体中，`UNVERIFIED_AGENT_RECALL`（归属 R11）在 18 份 lane 文件中出现 **0 次**，且 R11 全文 `AGENT_RECALL` 亦为 0 次 —— **该 token 不存在，此条枚举有误**。实测存在的 F-12 变体为 **11** 个；另有 **9** 个 F-12 未枚举的 tier 形态写法（`CITED_CLASSIC` / `CITED_PRIMARY_FULLTEXT` / `CITED_PRIMARY_SECONDARY` / `UNVERIFIED_AS_OF` / `UNVERIFIED_HYPOTHESIS` / `UNVERIFIED_CONTENT` / `UNVERIFIED_OR_UNKNOWN` / `UNVERIFIED_OFFICIAL_ACCESS` / `UNVERIFIED_VOL_PAGES`）。**F-12 的核心结论（跨 lane 不可比较、不可相加）不受影响**：两个候选计数（12 / 21）都远超可比较门槛。 |
| **F-13** | `03_MEASUREMENT_INSTRUMENTS.md`（全篇） | 41 个 instrument family / 54 条目、112 个 DOI token、逐条给出 α / ω / N / 载荷 / 跨文化不变性结论，但 **`CITED_PRIMARY` 出现 0 次**，只有 4 `CITED_SECONDARY` | `LABEL` | **MAJOR** | R03 是产出具体心理测量数字最多的 lane，却是**唯一一条完全不给 `CITED_PRIMARY` 的 lane**。`X9`（F-01）的 `DIRECT_PROXY` 判定所依据的一整套信效度数字（`N=2,334`；`PRI-8 R α=.93 ω_WP=.83`）**没有任何证据等级标注**。要么补标等级，要么把这些数字降级为 `UNVERIFIED`。 |
| **F-14** | `03_MEASUREMENT_INSTRUMENTS.md:130` vs `:131` | `:130`「**38 个**有名有姓的 power/equity/balance 量表各自仅被用 1–2 次，**无一成为主流工具**」；`:131`「谱系审计指出 SRPS 是**最常用的性权力工具**」 | `OVERCLAIM` | **MAJOR** | 两条引用**同一个 DOI**（`10.1111/jftr.70019`）且**互相矛盾**。R10 对同一来源的引用（`:360-364`）是逐字引用并明确写着「There were **no established scales used repeatedly that were developed specifically with power bases in mind**」+「the measures were focused on White, younger, and heterosexual men and women in shorter-length relationships」——**R10 引对了，R03 把它改写成了一个更强的、且与自家下一行冲突的绝对命题**。另外 Crossref 摘要报告的是 **k=319** 份 power 测量，不是 38；「无一成为主流工具」在摘要层无支持。修法：R03 `:130` 改回 R10 的原句转述，并加人口学限定。 |
| **F-15** | `02b_CONSTRUCT_REDUNDANCY_AUDIT.md:286`（并被 `00_MANIFEST.md:50` 复述为承重指针） | 「三者联合解释 commitment 方差 `R² = .54 (95% CI [.53,.55])`；单项最强为 satisfaction（`β² = .47`），其次 investment（`.32`），再次 alternatives（`−.19`）」 | `OVERCLAIM` | **MAJOR** | `N=50,427` / `k=202` / `r=.65·.53·−.43` 全部与摘要一致 ✓，但**摘要没有给 R² 的置信区间，也没有给 `β²`**。一个宽度仅 ±.01 的 meta-analytic R² CI 极不寻常，报告未指页码/表号。`β²` 记法本身也含混（平方标准化 beta？）。manifest 把这条列为 R02 的头号证据指针。修法：补页码/表号，或把 CI 与 `β²` 降级为 `CITED_SECONDARY` 并注明"未在摘要层核对"。 |
| **F-16** | `04_DATASET_LANDSCAPE.md:585`、`:1012` | `:1012`「J Behav Dec Making. `https://link.springer.com/content/pdf/10.1007/s11238-014-9448-x.pdf`」——把一个 **PDF URL** 放在引用条目位置；`:585` 另有 `10.1007/s11238-014-9448-x.pdf` 被当作 DOI 使用 | `POINTER` | **MINOR** | 去掉 `.pdf` 即正确（`10.1007/s11238-014-9448-x` = **Bacon, Conte & Moffatt (2014), "Assortative mating on risk attitude", *Theory and Decision***，已实测解析）。注意期刊也不对：不是 *J Behav Dec Making*，是 *Theory and Decision*。 |
| **F-17** | `08b_BELIEF_DECEPTION_KNOWLEDGE.md:774` | 「Hedden, T., & Zhang, J. (2002). "What do you think I think you think? Strategic reasoning in matrix games." *Cognition* 85(1), 1–36. `10.1016/S0010-0277(02)0549-8`」 | `POINTER` | **MINOR** | 作者/标题/期刊/年**全对**，DOI 后缀被写错：正确的是 **`10.1016/s0010-0277(02)00054-9`**（`00054-9` vs `0549-8`，末位与位数双重易位）。已实测解析。这是全 swarm 最接近"内容完全正确、只是指针损坏"的一条。 |
| **F-18** | `08b_BELIEF_DECEPTION_KNOWLEDGE.md:742`；`12_COMPUTATIONAL_MODELS_ABM.md:491`；`10_MUTUALITY_POWER_DEPENDENCE.md:767` | `10.1007/978-1-4020-5839-4` 归 "van Benthem, van der Hoek, & Kooi (2010)"；`10.4324/9780203848852.ch17` 归 *Handbook of Multilevel Models*；Bodenmann 2011 标题写成 "…predicting relationship quality and individual well-being" | `POINTER` | **MINOR** | 前者实为 **van Ditmarsch, van der Hoek & Kooi, *Dynamic Epistemic Logic*, Synthese Library 337**（同书，作者名单错）；后者实为 ***Handbook of Advanced Multilevel Analysis*** ch.17；Bodenmann 2011 原题是 "…predicting **Relationship Satisfaction**"。三处都只影响题录准确性，不影响主张。 |
| **F-19** | `13_LLM_SKILL_INTERVIEW_LAYER.md:687` | 「Huang, L., et al. (**2024**). A Survey on Hallucination in Large Language Models… ***ACM Computing Surveys***. `10.1145/3703155`」 | `POINTER` | **MINOR** | DOI 解析正确，但 venue 是 ***ACM Transactions on Information Systems (TOIS)***，Crossref 年份 **2025**。 |
| **F-20** | `13_LLM_SKILL_INTERVIEW_LAYER.md:720` | 「Rammstedt, B., et al. (2013). A Short Scale for Assessing the Big Five… *MDA* 7(2). DOI `10.12758/mda.2013.013`」 | `POINTER` | **MINOR** | Crossref 无此记录，但 **`doi.org` 返回 302 → `http://mda.gesis.org/index.php/mda/article/view/2013.013`**。即：DOI **有效**（GESIS 自建注册，非 Crossref），只是不能用 Crossref API 核。建议全 swarm 的核验流程加一步 `doi.org` 302 探测（本次我做了，救回 5 条）。 |
| **F-21** | `13_LLM_SKILL_INTERVIEW_LAYER.md:682` | 「Yan, T., et al. (2022). Response Burden – Review and Conceptual Framework. ***Field Work and Social Research***. `10.2478/jos-2022-0041`」 | `POINTER` | **MINOR** | DOI 解析正确，但期刊是 ***Journal of Official Statistics***（`jos-` = J Official Statistics），不是 *Field Work and Social Research*；作者为 Yan, Ting & Williams, Douglas。 |
| **F-22** | `03_MEASUREMENT_INSTRUMENTS.md:145` | 「综述 **Mønster et al. (2016)** `10.1177/1088868316628405`」 | `POINTER` | **MINOR** | DOI 解析正确，但作者是 **Palumbo, Marraccini, Weyandt, Wilder-Smith et al. (2016), "Interpersonal Autonomic Physiology: A Systematic Review of the Literature", *PSPR***。这一条在 R03 `X8`（ANS synchrony，判 `NOT_IDENTIFIABLE`）的证据串里，承载「方向矛盾 + 高异质 + 综述明说含糊」三个判断中的第三个。 |
| **F-23** | `03_MEASUREMENT_INSTRUMENTS.md:125`、`:126`、`:64`、`:96` | `:125`「Relationship Power Inventory (RPI) \| **Beach (2017)**, *Personal Relationships*, `10.1111/pere.12072`」；`:126`「RBA \| **Lativos et al. (2017)**, `10.1007/s10591-017-9421-2`」；`:64`「DSDS \| Clayton et al. (2009)，**经** `10.1007/s13178-024-01040-0` 转述」；`:96`「依恋与日常互动的工作模型 \| **Pietromonaco & Laurenceau (1998)**, `10.1037/0022-3514.73.6.1409`」 | `POINTER` | **MINOR** | 四个 DOI 全解析，全部错配：`pere.12072` = **Farrell, Simpson & Rothman (2015)**「The relationship power inventory」；`s10591-017-9421-2` = **Luttrell, Distelberg, Wilson, Knudson-Martin et al. (2017)**「Exploring the Relationship Balance Assessment」；`s13178-024-01040-0` = **Ballester-Arnal et al. (2024)**, ASE 跨文化验证（**不包含 Clayton/DSDS**，转述链断裂）；`0022-3514.73.6.1409` = **Pietromonaco & Barrett (1997)**（不是 Laurenceau）。R03 自 `:399` 承认"第 … 条的完整作者名单或期刊卷期本次未逐一核对"——这四条落在那个未核对区里。 |
| **F-24** | `17_RED_TEAM_FALSIFIERS.md:512` / `:592`（`10.1613/jair.3600`）、`:510`（`10.1177/…` Balan 1968）、`:591`（Weiss & Murchison 2005 ASR） | 3 条双 404 / 检索未命中的指针 | `POINTER` | **MINOR** | **这一组是全 swarm 证据卫生的正例，不是缺陷。** R17 对每一条都显式标 `FETCH_FAILED`，写明"因此该条**未建立**""结论未受影响""我 FETCH_FAILED 了…因此我只用它证明 X，不用它证明 Y"，并把 F4 改由 MacDonald et al. (2013) + Zoppolat et al. (2023) 承担。我另外用 Crossref 书目检索也未命中 Poesio 2012 "A survey of ambiguity and consensus in NLP" 与 Balan 1968 的 DOI —— **R17 的"用不了"判断与我的独立核验一致**。唯一可改进：把"检索未命中"写成 `10.1177/…` 这种字面占位符会被下游误读为 DOI，建议统一写成 `DOI_UNKNOWN_AS_OF_2026-09-27`。 |
| **F-25** | `07_PARTIAL_OBSERVABILITY.md:551` | 「16. `[UNVERIFIED]` Belnap, N. D. (1976). *On a partial truth functional.* Inquiry 19(4), 490–499. DOI `10.2307/2265159`. — 背景提及，**未用于任何主张**」 | `POINTER` | **MINOR** | `10.2307/2265159` Crossref + `doi.org` 双 404，我用 Crossref 书目检索也未找到该文的可解析标识。R07 已标 `[UNVERIFIED]` 且明示"未用于任何主张"——处理正确，仅指针需清掉或换掉。（另：manifest `00_MANIFEST.md:57` 把 R07 的核心指针写成"QSR/Renz 2007"，与该行内容对不上。） |
| **F-26** | `03_MEASUREMENT_INSTRUMENTS.md:234` | 「**完全无不变性证据** \| RCI…PRI、PPRS \| 全部」 | `OVERCLAIM` | **MINOR** | 对 14 个工具族下了"完全无"的绝对否定，该表未附检索日志（检索了哪些库、哪些关键词、何时）。R03 其他地方的措辞纪律（`NOT_ASSESSED` / `UNKNOWN`）比这里严。修法：改为「本 lane 未检索到」+ 挂检索日志指针。同类：`:130` 见 F-14。 |
| **F-27** | `14_PAPER_POSITIONING_NOVELTY.md:20`、`:73`；`04` 各类 | 「LHRM 目前**所有**『有向关系状态构念』都能在 1970–2020 的成熟文献里找到对应的一等公民地位」（`:20`）；「**结论：不存在「无先例」的关系质量复合评分系统。**」（`:73`） | `OVERCLAIM` | **MINOR** | 两处都是对全领域的绝对否定/全覆盖肯定，且 R14 自己在 `:71` 承认最高优先 prior-art（Acitelli & Antonioni）仍是 `AGENT_RECALL` / `UNVERIFIED_DOI`——**在一个自认有未核 prior-art 的前提下写"不存在先例"，是本报告最容易被 reviewer 打穿的一类句式**。R14 自己在 `:167` F-4 写「**从未** head-to-head」，说明它知道该怎么措辞。修法：加"在本次检索覆盖的 M0 范围内"限定。注：R12（`:416`）对同类命题的措辞是正确示范——「不主张…已被证明『不存在』——只主张本次在指定渠道内未能核实（`NEGATIVE`，非 `DISPROVEN`）」。 |
| **F-28** | `14_PAPER_POSITIONING_NOVELTY.md:71` / `:409`；`:50` / `:411`；`:12`(row) / `:412` | 承重的 prior-art 与方法学锚点是 `AGENT_RECALL`：「Acitelli & Antonioni（**最高优先 prior-art**）`AGENT_RECALL` / `UNVERIFIED_DOI`」；「Cook & Messick (1979) / Messick (1989,1995) / Trochim (1999) 五检 `AGENT_RECALL`」；「Sternberg (1986) / Spanier (1976) / Lund (1985) `AGENT_RECALL`」 | `LABEL` | **MINOR** | 标签用得**诚实**（这是应当保留的正面做法），但 R14 的 **17 条 REUSE + F-1…F-20 禁止主张 + O-1…O-17 overclaim 全部建立在这批 `AGENT_RECALL` 之上**。也就是说：本 swarm 中"最容易被 reviewer 攻击的一节"，其证据基座是未经核实的先验。修法：给 R14 一份 5–8 条的必核 prior-art 清单（Acitelli & Antonioni 2006 尤其优先——我用 Crossref 书目检索**未**命中，需人工确认该文是否真实存在及其 DOI）。 |
| **F-29** | `09_DYNAMIC_SYSTEMS_AND_HYSTERESIS.md`、`14`、`16`、`17`（头部） | 这 4 份报告**没有** `As of` / 核实日期字段（其余 14 份都有，最早 `2026-09-27`） | `RECENCY` | **MINOR** | `00_CHILD_CONTRACT.md:29` 明文要求「时间敏感事实必须标注核实日期」。R09/R14/R16/R17 缺该字段。R13 有字段但全文只出现 **1 次**日期，而它正是**对模型版本最敏感**的 lane（见 F-30）。 |
| **F-30** | `13_LLM_SKILL_INTERVIEW_LAYER.md:133, 306, 373, 630` | 时间敏感主张无逐条核实日期：「arXiv:2603.22735…并给出 **gpt-5.2** 的实例」；「arXiv:2604.23178：…跨 **Google / Anthropic / Meta** 一致」；「通用 **GPT-5** 在临床域已达 domain F1 0.88」；`U-8` | `RECENCY` | **MINOR** | 两条 arXiv 指针**真实存在**（我已实测）：`2603.22735` = Chan, Zhao & Gaizauskas, "Explanation Generation for Contradiction Reconciliation with LLMs", 2026-03-24 提交 / 2026-05-27 v2，Preprint，18 个 LLM "most models achieve limited success" —— 与 R13 表述**一致**。`2604.23178` = Soumik, "Judging the Judges…", 2026-04-25 / 2026-06-24 v2，**已发表于 TMLR (2026)**，覆盖 **4 个** provider family（Google/Anthropic/OpenAI/Meta）、style bias 0.10–0.76 ≫ position bias ≤0.04、Claude 偏好更短（−0.12）、GPT-4o 中性（−0.04）—— 与 R13 表述**基本一致**。两处需修：(a) R13 说"跨 Google/Anthropic/Meta"漏了 OpenAI；(b) R13 说 style bias 大于 position bias **与** verbosity bias，而原文把 verbosity 单列为"异质"而非更小。修法：给模型版本类主张逐条加 `as of 2026-09-27`，并把 TMLR 出版事实写进去（这会**提高**该条的权威等级，R13 目前低报了）。 |
| **F-31** | `02b:166` / `:286` / `:320` | `R² = .54` 的一致性表格里混入 `r = 0.08（不显著，<1% 方差）`、以及 `actual similarity ↔ attraction` 行 | `OVERCLAIM` | **MINOR** | `:320` 的表把 Tran 2019 的 investment-model 相关矩阵与另一来源的 "actual similarity ↔ attraction" 估计并排，`R²=.54` 那一列在两行间被复用了。读者容易把 .54 误读为覆盖全部四行。修法：拆表或在表头注明 `.54` 只属前三行。 |
| **F-32** | `02:488`、`:447` | 「**Overall, J. A.**, Fletcher, G. J. O., & Simpson, J. A. (2010)」；「**Agnew, P. A. M.**, Van Lange, P. A. M., Rusbult… (1998)」 | `POINTER` | **MINOR** | 姓氏首字母错：Crossref 为 **Overall, Nickola C.**（N.C. 非 J.A.）与 **Agnew, Christopher R.**（C.R. 非 P.A.M.，后者是同文第三作者 Langston 的缩写位）。两条都自标 ✓。 |
| **F-33** | `05:509`、`:517`、`:546`；`06:1033`；`10:453`；`11:511`；`12:81`；`17:280` 等 | 单年差：Lucas 2025/2026、`s44159-026` 标 `年份 UNKNOWN_AS_OF`（实为 **2026**）、Neubauer 2019/2020、Pusch 2022/2023、Garcia 2014/2015、Moyano 2016/2017、Mudimu 2014/2015、JASSS JuSpace 2020/2021、Brooks 2018/2019、Hirsh 1976/1977、Graham 2010/2011 | `POINTER` | **MINOR** | 全部是 online-first 年与卷期年之差，属正常引用实践，不影响主张。唯一值得改的是 `05:546`：R05 把一个**可解析**的 2026 年文献标成 `年份 UNKNOWN_AS_OF`，属过度保守的不确定性声明（同 F-06 的模式）。 |
| **F-34** | `02:137`、`:149`、`:185`；`03:118`、`:119`；`04:620`；`12:434`、`:435`；`09:406` | `AGENT_RECALL` 出现在**测量族**与**反例**位置：「Hatfield & Sprecher 1986 `AGENT_RECALL`」（PLS）；「具体工具 `AGENT_RECALL`」；「MacCallum et al. (2001) `AGENT_RECALL`, U09」；「Stets & Burke (2000) `AGENT_RECALL`, U12」；「Peterman (1963) `CITED_PARTIAL`, 作者/卷期 `AGENT_RECALL` 未核实」 | `LABEL` | **MINOR** | 这些 lane 都**同时**声明了"`AGENT_RECALL` 不得作为裁决依据"（R02:45）/「只用于举例或线索，不用于判定」（R09:18）/「不承重」（R17:332）——**纪律是到位的**。但 R02 把 `AGENT_RECALL` 的 Hatfield & Sprecher PLS 列进 `SexualDesire` 的**测量族**格、R09 把 `AGENT_RECALL` 的 Peterman 1963 列为 hysteresis 存在性的**经典展示**格：一旦读者只看表格不看纪律声明，这些格子会被当作已核实。修法：在表格格内保留标签（现状正确），并在这两处加一句"本格不可作为证据"。 |
| **F-35** | 全 swarm；`00_MANIFEST.md:85` | 「单 lane 自报去重指针数：R00 30+ · R01 **45** · R02 34 · R03 41 family · R04 16 dataset · R05 **109** · R06 33 · R07 33 · R08 **72** · R09 78 · R10 59 · R11 60+ · R12 40 · R13 70 · R14 60+ · R15 30 · R16 24 · R17 41+3」 | `LABEL` | **MINOR** | manifest §4 B-3 已声明"在 A04 完成前，上表不可相加"——**这一点做得好，保留**。A01 补充一条实测：**我抽到 353 个唯一 DOI**（跨 18 lane），远低于 manifest 逐 lane 相加的 878。这个差值主要来自：(a) 非 DOI 指针（URL/ISBN/issue id）未计入我的口径；(b) 同 DOI 在多 lane 重复计数；(c) 若干 lane 的"指针"计数包含同一文献的多次引用。**因此 manifest 的"全 swarm 150+ 独立来源"目标尚不能由现有计数支撑。**<br>**`SUPERSEDED`（Round 3 `A1` 实测重算，依 manifest §7 M-2/M-5、`EV2` §4.1）**：本行原文写「逐 lane 相加的 **788+**」。该数**算术不成立** —— 本行自己列出的这 18 个数逐项相加 = **875**（`+` 项按下界计），`41+3` 记作 44 则 = **878**。**878 才是真值**；`788` 无论按哪种读法都得不到。已改为 878。<br>另注：`875 / 533 = 1.64×`、`878 / 533 = 1.65×`；`875 / 350 = 2.50×`、`878 / 350 = 2.51×`。脚本与逐项输出见 §12。**倍率的具体数值不影响本行的定性结论**（lane 自报数不可相加、不可对外声称为「N 个独立来源」）。 |

---

## 6. 全部核实过的 DOI（353 条）

口径：
- `RESOLVED` = Crossref 解析成功，且**作者/年份/期刊与报告引用一致**（308）
- `RESOLVED+MISMATCH` = Crossref 解析成功，但**指向报告所引作品之外的另一篇**（29，见 §5）
- `DEAD_BOTH` = Crossref 404 **且** `doi.org` 404（9）
- `DEAD_CROSSREF` = Crossref 404（报告侧格式错，实际可解析）（1）
- `DATACITE_ONLY` = Crossref 无记录但 `doi.org` 302 → 有效（5）
- `NOT_FOUND` = 报告侧字面占位符（1）

| DOI | 出现 | 状态 | CR 年 | CR 作者（前 3） | CR 标题（前 78 字符） |
|---|---|---|---|---|---|
| `10.1111/j.1475-6811.1998.tb00177.x` | 11 | RESOLVED | 1998 | RUSBULT, CARYL E.; MARTZ, JOHN M.; AGNEW, CHRISTOPHER R. | The Investment Model Scale: Measuring commitment level, satisfaction level, qu |
| `10.1037/0022-3514.74.5.1238` | 7 | RESOLVED | 1998 | Laurenceau, Jean-Philippe; Barrett, Lisa Feldman; Pietromonaco, Paula  | Intimacy as an interpersonal process: The importance of self-disclosure, partn |
| `10.1073/pnas.1917036117` | 7 | RESOLVED | 2020 | Joel, Samantha; Eastwick, Paul W.; Allison, Colleen J. | Machine learning uncovers the most robust self-report predictors of relationsh |
| `10.1111/1475-6811.00035` | 7 | RESOLVED | 2003 | Le, Benjamin; Agnew, Christopher R. | Commitment and its theorized determinants: A meta–analysis of the Investment M |
| `10.1111/pere.12268` | 7 | RESOLVED | 2019 | Tran, Peter; Judge, Madeline; Kashima, Yoshihisa | Commitment in relationships: An updated meta‐analysis of the Investment Model |
| `10.1037/0022-3514.63.4.596` | 5 | RESOLVED | 1992 | Aron, Arthur; Aron, Elaine N.; Smollan, Danny | Inclusion of Other in the Self Scale and the structure of interpersonal closen |
| `10.1111/jftr.70019` | 5 | RESOLVED | 2025 | Junkins, Eleanor J.; Derringer, Jaime; Ogolsky, Brian G. | Measures of Relationship Power Dynamics in Romantic Relationships |
| `10.1177/0146167200265007` | 5 | RESOLVED | 2000 | Fletcher, Garth J. O.; Simpson, Jeffry A.; Thomas, Geoff | The Measurement of Perceived Relationship Quality Components: A Confirmatory F |
| `10.1177/01461672251409849` | 5 | RESOLVED | 2026 | Körner, Robert; Overall, Nickola C. | Bias in Perceptions of Power in Close Relationships: The Role of Self-Protecti |
| `10.1007/s10508-009-9556-9` | 4 | RESOLVED | 2010 | Chivers, Meredith L.; Seto, Michael C.; Lalumière, Martin L. | Agreement of Self-Reported and Genital Measures of Sexual Arousal in Men and W |
| `10.1016/0022-1031(80)90007-4` | 4 | RESOLVED | 1980 | Rusbult, Caryl E | Commitment and satisfaction in romantic associations: A test of the investment |
| `10.1037/0022-3514.49.1.95` | 4 | RESOLVED | 1985 | Rempel, John K.; Holmes, John G.; Zanna, Mark P. | Trust in close relationships. |
| `10.1037/0022-3514.57.5.792` | 4 | RESOLVED | 1989 | Berscheid, Ellen; Snyder, Mark; Omoto, Allen M. | The Relationship Closeness Inventory: Assessing the closeness of interpersonal |
| `10.1037/0022-3514.76.1.72` | 4 | RESOLVED | 1999 | Fletcher, Garth J. O.; Simpson, Jeffry A.; Thomas, Geoff | Ideals in intimate relationships. |
| `10.1080/01650250444000405` | 4 | RESOLVED | 2005 | Cook, William L.; Kenny, David A. | The Actor–Partner Interdependence Model: A model of bidirectional              |
| `10.1146/annurev-psych-010416-044038` | 4 | RESOLVED | 2017 | Finkel, Eli J.; Simpson, Jeffry A.; Eastwick, Paul W. | The Psychology of Close Relationships: Fourteen Core Principles |
| `10.1037/0022-3514.78.2.350` | 3 | RESOLVED | 2000 | Fraley, R. Chris; Waller, Niels G.; Brennan, Kelly A. | An item response theory analysis of self-report measures of adult attachment. |
| `10.1037/0022-3514.87.2.228` | 3 | RESOLVED | 2004 | Gable, Shelly L.; Reis, Harry T.; Impett, Emily A. | What Do You Do When Things Go Right? The Intrapersonal and Interpersonal Benef |
| `10.1037/0033-295X.99.4.689` | 3 | RESOLVED | 1992 | Fiske, Alan P. | The four elementary forms of sociality: Framework for a unified theory of soci |
| `10.1037/a0038889` | 3 | RESOLVED | 2015 | Hamaker, Ellen L.; Kuiper, Rebecca M.; Grasman, Raoul P. P. P. | A critique of the cross-lagged panel model. |
| `10.1037/h0029841` | 3 | RESOLVED | 1970 | Rubin, Zick | Measurement of romantic love. |
| `10.1037/met0000701` | 3 | RESOLVED | 2024 | Muthén, Bengt; Asparouhov, Tihomir; Witkiewitz, Katie | Cross-lagged panel modeling with binary and ordinal outcomes. |
| `10.1038/s41598-025-14923-y` | 3 | RESOLVED | 2025 | Eberhardt, Steffen T.; Vehlen, Antonia; Schaffrath, Jana | Development and validation of large language model rating scales for automatic |
| `10.1111/j.1467-6494.1986.tb00393.x` | 3 | RESOLVED | 1986 | Malloy, Thomas E; Kenny, David A | The Social Relations Model: An integrative method for personality research |
| `10.1111/j.1467-8721.2009.01621.x` | 3 | RESOLVED+MISMATCH | 2009 | Roisman, Glenn I. | Adult Attachment |
| `10.1111/pere.12240` | 3 | RESOLVED | 2018 | Kenny, David A. | Reflections on the actor–partner interdependence model |
| `10.1145/3704890` | 3 | RESOLVED | 2025 | Liell-Cock, Jack; Staton, Sam | Compositional Imprecise Probability: A Solution from Graded Monads and Markov  |
| `10.1146/annurev-psych-012325-032022` | 3 | RESOLVED | 2026 | Overall, Nickola C.; Hammond, Matthew D. | Power and Ideology in Close Relationships |
| `10.1177/0146167205276865` | 3 | RESOLVED | 2005 | Sibley, Chris G.; Fischer, Ronald; Liu, James H. | Reliability and Validity of the Revised Experiences in Close Relationships (EC |
| `10.1177/1948550613509287` | 3 | RESOLVED | 2013 | Arriaga, Ximena B.; Kumashiro, Madoka; Finkel, Eli J. | Filling the Void |
| `10.1177/25152459231158378` | 3 | RESOLVED | 2023 | Lucas, Richard E. | Why the Cross-Lagged Panel Model Is Almost Never the Right Choice |
| `10.1198/016214506000001437` | 3 | RESOLVED | 2007 | Gneiting, Tilmann; Raftery, Adrian E | Strictly Proper Scoring Rules, Prediction, and Estimation |
| `10.4232/pairfam.5678.14.2.0` | 3 | DATACITE_ONLY | — | — | — |
| `10.1002/hbm.25244` | 2 | RESOLVED | 2020 | Dukart, Juergen; Holiga, Stefan; Rullmann, Michael | <scp>JuSpace</scp>
                    : A tool for spatial correlation analys |
| `10.1002/per.2410050503` | 2 | RESOLVED+MISMATCH | 1991 | Wiggins, Jerry S.; Broughton, Ross | A geometric taxonomy of personality scales |
| `10.1002/sim.3944` | 2 | RESOLVED | 2010 | White, Ian R.; Carlin, John B. | Bias and efficiency of multiple imputation compared with complete‐case analysi |
| `10.1007/3-540-45547-7_3` | 2 | RESOLVED | 2001 | Harrison McKnight, D.; Chervany, Norman L. | Trust and Distrust Definitions: One Bite at a Time |
| `10.1007/s10508-011-9785-6` | 2 | RESOLVED | 2011 | Krishnamurti, Tamar; Loewenstein, George | The Partner-Specific Sexual Liking and Sexual Wanting Scale: Psychometric Prop |
| `10.1007/s10508-026-03487-1` | 2 | RESOLVED | 2026 | Eisert, Brady C.; Anderson, Jared R.; Portillo, Maria F. | The Hurlbert Index of Sexual Desire-Short Form: Psychometric Properties |
| `10.1007/s10591-017-9421-2` | 2 | RESOLVED+MISMATCH | 2017 | Luttrell, Thomas B.; Distelberg, Brian; Wilson, Colwick | Exploring the Relationship Balance Assessment |
| `10.1007/s10902-020-00241-9` | 2 | RESOLVED | 2020 | Mund, Marcus; Johnson, Matthew D. | Lonely Me, Lonely You: Loneliness and the Longitudinal Course of Relationship  |
| `10.1007/s11121-017-0803-3` | 2 | RESOLVED | 2017 | Feinberg, Mark E.; Xia, Mengya; Fosco, Gregory M. | Dynamical Systems Modeling of Couple Interaction: a New Method for Assessing I |
| `10.1007/s11229-024-04527-w` | 2 | RESOLVED | 2024 | Schindler, Samuel | Normal science: not uncritical or dogmatic |
| `10.1007/s12110-998-1010-5` | 2 | RESOLVED | 1998 | Fisher, Helen E. | Lust, attraction, and attachment in mammalian reproduction |
| `10.1007/s13178-024-01040-0` | 2 | RESOLVED+MISMATCH | 2024 | Ballester-Arnal, Rafael; Elipe-Miravet, Marcel; Castro-Calvo, Jesús | Cross-cultural Validation of the Arizona Sexual Experience Scale (ASEX) in 42  |
| `10.1016/1053-4822(91)90011-z` | 2 | RESOLVED | 1991 | Meyer, John P.; Allen, Natalie J. | A three-component conceptualization of organizational commitment |
| `10.1016/B978-0-444-51726-5.50015-7` | 2 | RESOLVED | 2008 | Baltag, Alexandru; van Ditmarsch, Hans P.; Moss, Lawrence S. | EPISTEMIC LOGIC AND INFORMATION UPDATE |
| `10.1016/S0065-2601(08)60144-6` | 2 | RESOLVED | 1984 | Kenny, David A.; La Voie, Lawrence | The Social Relations Model |
| `10.1016/S0140-1971(86)80043-4` | 2 | RESOLVED | 1986 | Hatfield, Elaine; Sprecher, Susan | Measuring passionate love in intimate relationships |
| `10.1016/j.patter.2023.100804` | 2 | RESOLVED | 2023 | Kapoor, Sayash; Narayanan, Arvind | Leakage and the reproducibility crisis in machine-learning-based science |
| `10.1016/j.physbeh.2021.113391` | 2 | RESOLVED | 2021 | Mayo, Oded; Lavidor, Michal; Gordon, Ilanit | Interpersonal autonomic nervous system synchrony and its association to relati |
| `10.1017/9781108131490.003` | 2 | RESOLVED | 2019 | Overall, Nickola C.; Cross, Emily J. | Attachment Insecurity and the Regulation of Power and Dependence in Intimate R |
| `10.1023/A:1018721100903` | 2 | RESOLVED | 1998 | Kupek, Emil | Determinants of Item Nonresponse in a Large National Sex Survey |
| `10.1027/1015-5759/a000902` | 2 | RESOLVED | 2025 | Brauer, Kay; Proyer, René T. | A Study of the Measurement Invariance of the Experiences in Close Relationship |
| `10.1037/0022-3514.47.4.709` | 2 | RESOLVED | 1984 | Erber, Ralph; Fiske, Susan T. | Outcome dependency and attention to inconsistent information. |
| `10.1037/0022-3514.50.2.392` | 2 | RESOLVED | 1986 | Hendrick, Clyde; Hendrick, Susan | A theory and method of love. |
| `10.1037/0022-3514.60.1.53` | 2 | RESOLVED | 1991 | Rusbult, Caryl E.; Verette, Julie; Whitney, Gregory A. | Accommodation processes in close relationships: Theory and preliminary empiric |
| `10.1037/0022-3514.73.6.1409` | 2 | RESOLVED+MISMATCH | 1997 | Pietromonaco, Paula R.; Barrett, Lisa Feldman | Working models of attachment and daily social interactions. |
| `10.1037/0022-3514.74.6.1516` | 2 | RESOLVED | 1998 | Clary, E. Gil; Snyder, Mark; Ridge, Robert D. | Understanding and assessing the motivations of volunteers: A functional approa |
| `10.1037/0022-3514.77.2.293` | 2 | RESOLVED | 1999 | Drigotas, Stephen M.; Rusbult, Caryl E.; Wieselquist, Jennifer | Close partner as sculptor of the ideal self: Behavioral affirmation and the Mi |
| `10.1037/0022-3514.80.2.237` | 2 | RESOLVED | 2001 | Huston, Ted L.; Caughlin, John P.; Houts, Renate M. | The connubial crucible: Newlywed years as predictors of marital delight, distr |
| `10.1037/0022-3514.94.5.808` | 2 | RESOLVED | 2008 | Impett, Emily A.; Strachman, Amy; Finkel, Eli J. | Maintaining sexual desire in intimate relationships: The importance of approac |
| `10.1037/0033-295X.110.2.265` | 2 | RESOLVED | 2003 | Keltner, Dacher; Gruenfeld, Deborah H.; Anderson, Cameron | Power, approach, and inhibition. |
| `10.1037/0033-295X.93.2.119` | 2 | RESOLVED | 1986 | Sternberg, Robert J. | A triangular theory of love. |
| `10.1037/0882-7974.8.2.144` | 2 | RESOLVED | 1993 | Cicirelli, Victor G. | Attachment and obligation as daughters' motives for caregiving behavior and su |
| `10.1037/2021-17028-001` | 2 | DEAD_BOTH | — | — | — |
| `10.1037/a0022441` | 2 | RESOLVED | 2011 | Graham, James M.; Diebels, Kate J.; Barnow, Zoe B. | The reliability of relationship satisfaction: A reliability generalization met |
| `10.1037/a0024061` | 2 | RESOLVED | 2011 | Eastwick, Paul W.; Eagly, Alice H.; Finkel, Eli J. | Implicit and explicit preferences for physical attractiveness in a romantic pa |
| `10.1037/amp0000191` | 2 | RESOLVED | 2018 | Appelbaum, Mark; Cooper, Harris; Kline, Rex B. | Journal article reporting standards for quantitative research in psychology: T |
| `10.1037/e512142015-146` | 2 | RESOLVED | 2014 | Winczewski, Lauren A.; Bowen, Jeff; Collins, Nancy | Compassionate love for a romantic partner facilitates empathic accuracy |
| `10.1037/h0040084` | 2 | RESOLVED | 1957 | Poole, Aileen | Counselor judgment and counseling evaluation. |
| `10.1037/h0046049` | 2 | RESOLVED | 1956 | Cartwright, Dorwin; Harary, Frank | Structural balance: a generalization of Heider's theory. |
| `10.1037/met0000285` | 2 | RESOLVED | 2022 | Andersen, Henrik Kenneth | Equivalent approaches to dealing with unobserved heterogeneity in cross-lagged |
| `10.1037/met0000600` | 2 | RESOLVED | 2026 | Hamaker, Ellen L. | The within-between dispute in cross-lagged panel research and how to move forw |
| `10.1037/pspi0000097` | 2 | RESOLVED | 2017 | Huang, Karen; Yeomans, Michael; Brooks, Alison Wood | It doesn’t hurt to ask: Question-asking increases liking. |
| `10.1037/pspp0000166` | 2 | RESOLVED | 2018 | Gerpott, Fabiola H.; Balliet, Daniel; Columbus, Simon | How do people think about interdependence? A multidimensional model of subject |
| `10.1037/pspp0000358` | 2 | RESOLVED | 2021 | Orth, Ulrich; Clark, D. Angus; Donnellan, M. Brent | Testing prospective effects in longitudinal research: Comparing seven competin |
| `10.1037/rev0000360` | 2 | RESOLVED | 2023 | Eastwick, Paul W.; Finkel, Eli J.; Joel, Samantha | Mate evaluation theory. |
| `10.1038/s44159-026-00535-4` | 2 | RESOLVED | 2026 | Gordon, Ilanit; Bartsch, Ronny P. | Correlates of interpersonal physiological synchrony and sources of empirical h |
| `10.1080/00223890701268041` | 2 | RESOLVED | 2007 | Wei, Meifen; Russell, Daniel W.; Mallinckrodt, Brent | The Experiences in Close Relationship Scale (ECR)-Short Form: Reliability, Val |
| `10.1080/00224499.2015.1109581` | 2 | RESOLVED | 2016 | Moyano, Nieves; Vallejo-Medina, Pablo; Sierra, Juan Carlos | Sexual Desire Inventory: Two or Three Dimensions? |
| `10.1080/00224499.2024.2417023` | 2 | RESOLVED | 2024 | Castro-Calvo, Jesús; Beltrán-Martínez, Patricia; Ballester-Arnal, Rafa | Cross-Cultural Validation of the Sexual Desire Inventory (SDI-2) in 42 Countri |
| `10.1080/00926239608414655` | 2 | RESOLVED | 1996 | Spector, Ilana P.; Carey, Michael P.; Steinberg, Lynne | The sexual desire inventory: Development, factor structure, and evidence of re |
| `10.1080/1047840X.2014.863723` | 2 | RESOLVED | 2014 | Finkel, Eli J.; Hui, Chin Ming; Carswell, Kathleen L. | The Suffocation of Marriage: Climbing Mount Maslow Without Enough Oxygen |
| `10.1080/10705511.2014.961800` | 2 | RESOLVED | 2015 | Morin, Alexandre J. S.; Arens, A. Katrin; Marsh, Herbert W. | A Bifactor Exploratory Structural Equation Modeling Framework for the Identifi |
| `10.1080/10705511.2022.2065278` | 2 | RESOLVED | 2022 | Lüdtke, Oliver; Robitzsch, Alexander | A Comparison of Different Approaches for Estimating Cross-Lagged Effects from  |
| `10.1080/10705511.2024.2379495` | 2 | RESOLVED | 2024 | Robitzsch, Alexander; Lüdtke, Oliver | A Note on the Occurrence of the Illusory Between-Person Component in the Rando |
| `10.1101/2025.11.15.25339520` | 2 | RESOLVED | 2025 | Wang, Bo; Kabir, Dia; Clark, Cheryl R. | Extracting Social Determinants of Health from Electronic Health Records: Devel |
| `10.1111/1467-6494.00143` | 2 | RESOLVED | 2001 | Pincus, Aaron L.; Wilson, Kelly R. | Interpersonal Variability in Dependent Personality |
| `10.1111/1467-8721.00070` | 2 | RESOLVED | 2000 | Fletcher, Garth J.O.; Simpson, Jeffry A. | Ideal Standards in Close Relationships |
| `10.1111/1475-6811.00017` | 2 | RESOLVED+MISMATCH | 2002 | Hassebrauck, Manfred; Fehr, Beverley | Dimensions of Relationship Quality |
| `10.1111/j.1467-6494.2011.00734.x` | 2 | RESOLVED | 2012 | Anderson, Cameron; John, Oliver P.; Keltner, Dacher | The Personal Sense of Power |
| `10.1111/j.1475-6811.2007.00173.x` | 2 | RESOLVED | 2007 | BRANJE, SUSAN J. T.; FRIJNS, TOM; FINKENAUER, CATRIN | You are my best friend: Commitment and stability in adolescents’ same‐sex frie |
| `10.1111/j.1475-6811.2009.01221.x` | 2 | RESOLVED | 2009 | OVERALL, NICKOLA C.; SIBLEY, CHRIS G. | Attachment and dependence regulation within daily interactions with romantic p |
| `10.1111/j.1741-3737.2002.00568.x` | 2 | RESOLVED | 2002 | Bengtson, Vern; Giarrusso, Roseann; Mabry, J. Beth | Solidarity, Conflict, and Ambivalence: Complementary or Competing Perspectives |
| `10.1111/j.1741-3737.2006.00284.x` | 2 | RESOLVED | 2006 | Graham, James M.; Liu, Yenling J.; Jeziorski, Jennifer L. | The Dyadic Adjustment Scale: A Reliability Generalization Meta‐Analysis |
| `10.1111/joop.12395` | 2 | RESOLVED+MISMATCH | 2022 | Gottfredson, Ryan K.; Wright, Sarah L.; Heaphy, Emily D. | A critical review of relationship quality measures: Is a fresh start needed? A |
| `10.1111/pere.12072` | 2 | RESOLVED+MISMATCH | 2015 | FARRELL, ALLISON K.; SIMPSON, JEFFRY A.; ROTHMAN, ALEXANDER J. | The relationship power inventory: Development and validation |
| `10.1111/spc3.12308` | 2 | RESOLVED+MISMATCH | 2017 | Reis, Harry T.; Lemay, Edward P.; Finkenauer, Catrin | Toward understanding understanding: The importance of feeling understood in re |
| `10.1126/sciadv.aay3689` | 2 | RESOLVED | 2020 | Brady, Shannon T.; Cohen, Geoffrey L.; Jarvis, Shoshana N. | A brief social-belonging intervention in college improves adult outcomes for b |
| `10.1126/science.1185231` | 2 | RESOLVED | 2010 | Centola, Damon | The Spread of Behavior in an Online Social Network Experiment |
| `10.1126/science.1198364` | 2 | RESOLVED | 2011 | Walton, Gregory M.; Cohen, Geoffrey L. | A Brief Social-Belonging Intervention Improves Academic and Health Outcomes of |
| `10.1145/2382577.2382579` | 2 | RESOLVED | 2012 | Kaufman, Shachar; Rosset, Saharon; Perlich, Claudia | Leakage in data mining |
| `10.1145/2815620` | 2 | RESOLVED | 2015 | Sutcliffe, Alistair G.; Wang, Di; Dunbar, Robin I. M. | Modelling the Role of Trust in Social Relationships |
| `10.1145/3586183.3606763` | 2 | RESOLVED | 2023 | Park, Joon Sung; O'Brien, Joseph; Cai, Carrie Jun | Generative Agents: Interactive Simulacra of Human Behavior |
| `10.1145/3618260.3649777` | 2 | RESOLVED | 2024 | Kalai, Adam Tauman; Vempala, Santosh S. | Calibrated Language Models Must Hallucinate |
| `10.1146/annurev.psych.093008.100318` | 2 | RESOLVED | 2010 | Berscheid, Ellen | Love in the Fourth Dimension |
| `10.1146/annurev.psych.54.101601.145059` | 2 | RESOLVED | 2003 | Rusbult, Caryl E.; Van Lange, Paul A. M. | Interdependence, Interaction, and Relationships |
| `10.1177/0003122417715051` | 2 | DEAD_BOTH | — | — | — |
| `10.1177/0022022104266105` | 2 | RESOLVED | 2004 | Schmitt, David P.; Alcalay, Lidia; Allensworth, Melissa | Patterns and Universals of Adult Romantic Attachment Across 62 Cultural Region |
| `10.1177/0049124118789708` | 2 | RESOLVED | 2018 | Davidov, Eldad; Muthen, Bengt; Schmidt, Peter | Measurement Invariance in Cross-National Studies |
| `10.1177/0192513X18758343` | 2 | RESOLVED | 2018 | Brooks, James E.; Ogolsky, Brian G.; Monk, J. Kale | Commitment in Interracial Relationships: Dyadic and Longitudinal Tests of the  |
| `10.1177/0192513X19860181` | 2 | RESOLVED | 2019 | de Bel, Vera; Kalmijn, Matthijs; van Duijn, Marijtje A. J. | Balance in Family Triads: How Intergenerational Relationships Affect the Adult |
| `10.1177/0265407508096700` | 2 | RESOLVED | 2008 | Montoya, R. Matthew; Horton, Robert S.; Kirchner, Jeffrey | Is actual similarity necessary for attraction? A meta-analysis of actual and p |
| `10.1177/0265407510378125` | 2 | RESOLVED | 2010 | Stafford, Laura | Measuring relationship maintenance behaviors: Critique and development of the  |
| `10.1177/0265407512465221` | 2 | RESOLVED+MISMATCH | 2012 | MacDonald, Geoff; Locke, Kenneth D.; Spielmann, Stephanie S. | Insecure attachment predicts ambivalent social threat and reward perceptions i |
| `10.1177/0265407514536293` | 2 | RESOLVED | 2014 | Tan, Kenneth; Agnew, Christopher R.; VanderDrift, Laura E. | Committed to us |
| `10.1177/0265407515584493` | 2 | RESOLVED | 2015 | Segal, Noam; Fraley, R. Chris | Broadening the investment model |
| `10.1177/02654075211028654` | 2 | RESOLVED | 2021 | Brinberg, Miriam; Vanderbilt, Rachel Reymann; Solomon, Denise Haunani | Using technology to unobtrusively observe relationship development |
| `10.1177/0265407589064001` | 2 | RESOLVED | 1989 | Sprecher, Susan; Metts, Sandra | Development of the `Romantic Beliefs Scale' and Examination of the Effects of  |
| `10.1177/104973239500500306` | 2 | RESOLVED | 1995 | Neufeld, Anne; Harrison, Margaret J. | Reciprocity and Social Support in Caregivers' Relationships: Variations and Co |
| `10.1177/10693971211068971` | 2 | RESOLVED | 2022 | Lacko, David; Čeněk, Jiří; Točík, Jaroslav | The Necessity of Testing Measurement Invariance in Cross-Cultural Research: Po |
| `10.1177/1077801206293328` | 2 | RESOLVED | 2006 | Johnson, Michael P. | Conflict and Control |
| `10.1177/1088868316628405` | 2 | RESOLVED+MISMATCH | 2016 | Palumbo, Richard V.; Marraccini, Marisa E.; Weyandt, Lisa L. | Interpersonal Autonomic Physiology: A Systematic Review of the Literature |
| `10.1177/109442810031002` | 2 | RESOLVED | 2000 | Vandenberg, Robert J.; Lance, Charles E. | A Review and Synthesis of the Measurement Invariance Literature: Suggestions,  |
| `10.1177/1948550620944111` | 2 | RESOLVED | 2020 | Gunaydin, Gul; Selcuk, Emre; Urganci, Betul | Today You Care, Tomorrow You Don’t: Differential Roles of Responsiveness Varia |
| `10.1186/1471-2288-12-46` | 2 | RESOLVED | 2012 | Seaman, Shaun R; Bartlett, Jonathan W; White, Ian R | Multiple imputation of missing covariates with non-linear effects and interact |
| `10.1186/s12874-018-0570-2` | 2 | RESOLVED | 2018 | Cartagena-Ramos, Denisse; Fuentealba-Torres, Miguel; Rebustini, Flávio | Systematic review of the psychometric properties of instruments to measure sex |
| `10.1186/s12877-021-02425-1` | 2 | RESOLVED | 2021 | Gehr, Thomas Johann; Freiberger, Ellen; Sieber, Cornel Christian | A typology of caregiving spouses of geriatric patients without dementia: carin |
| `10.1186/s12955-020-01526-6` | 2 | RESOLVED | 2020 | Liu, Jing-Dong; You, Ri-Hong; Liu, Hao | Chinese version of the international positive and negative affect schedule sho |
| `10.1207/s15327752jpa4106_6` | 2 | RESOLVED | 1977 | Hirschfeld, Robert M.A.; Klerman, Gerald L.; Gouch, Harrison G. | A Measure of Interpersonal Dependency |
| `10.1207/s15327957pspr1003_2` | 2 | RESOLVED | 2006 | Bond, Charles F.; DePaulo, Bella M. | Accuracy of Deception Judgments |
| `10.1214/20-AOAS1322` | 2 | RESOLVED | 2020 | Zhang, Chelsea; Taylor, Sean J.; Cobb, Curtiss | Active matrix factorization for surveys |
| `10.1257/aer.p20161046` | 2 | RESOLVED | 2016 | Bergemann, Dirk; Morris, Stephen | Information Design, Bayesian Persuasion, and Bayes Correlated Equilibrium |
| `10.13072/midss.484` | 2 | RESOLVED | None | — | — |
| `10.1371/journal.pone.0129478` | 2 | RESOLVED | 2015 | Gächter, Simon; Starmer, Chris; Tufano, Fabio | Measuring the Closeness of Relationships: A Comprehensive Evaluation of the 'I |
| `10.1509/jmkr.44.2.175` | 2 | RESOLVED | 2007 | Bergkvist, Lars; Rossiter, John R. | The Predictive Validity of Multiple-Item versus Single-Item Measures of the Sa |
| `10.1609/aaai.v31i1.10730` | 2 | RESOLVED | 2017 | Lewenberg, Yoad; Bachrach, Yoram; Paquet, Ulrich | Knowing What to Ask: A Bayesian Active Learning Approach to the Surveying Prob |
| `10.1609/aaai.v35i1.16792` | 2 | DEAD_BOTH | — | — | — |
| `10.1613/jair.3600` | 2 | DEAD_BOTH | — | — | — |
| `10.18564/jasss.1912` | 2 | RESOLVED | 2012 | Sutcliffe, Alistair; Wang, Di | Computational Modelling of Trust and Social Relationships |
| `10.18564/jasss.1929` | 2 | RESOLVED | 2012 | Grazzini, Jakob | Analysis of the Emergent Properties: Stationarity and Ergodicity |
| `10.18564/jasss.2274` | 2 | RESOLVED | 2013 | Schindler, Julia | About the Uncertainties in Model Design and Their Effects: An Illustration wit |
| `10.18653/v1/2020.acl-main.442` | 2 | RESOLVED | 2020 | Ribeiro, Marco Tulio; Wu, Tongshuang; Guestrin, Carlos | Beyond Accuracy: Behavioral Testing of NLP Models with CheckList |
| `10.18653/v1/2024.acl-long.698` | 2 | RESOLVED | 2024 | Wang, Ruiyi; Yu, Haofei; Zhang, Wenxin | SOTOPIA-π: Interactive Learning of Socially Intelligent Language Agents |
| `10.18653/v1/2025.acl-long.1203` | 2 | RESOLVED | 2025 | Zhang, Wenyuan; Liu, Tianyun; Song, Mengxiao | SOTOPIA-: Dynamic Strategy Injection Learning and Social Instruction Following |
| `10.21105/joss.07668` | 2 | RESOLVED | 2025 | ter Hoeven, Ewout; Kwakkel, Jan; Hess, Vincent | Mesa 3: Agent-based modeling with Python in 2025 |
| `10.2307/349726` | 2 | RESOLVED | 1964 | Reiss, Ira L. | The Scaling of Premarital Sexual Permissiveness |
| `10.2307/350547` | 2 | RESOLVED | 1976 | Spanier, Graham B. | Measuring Dyadic Adjustment: New Scales for Assessing the Quality of Marriage  |
| `10.2307/351903` | 2 | RESOLVED | 1980 | Larzelere, Robert E.; Huston, Ted L. | The Dyadic Trust Scale: Toward Understanding Interpersonal Trust in Close Rela |
| `10.2307/352650` | 2 | RESOLVED | 1988 | Sprecher, Susan; McKinney, Kathleen; Walsh, Robert | A Revision of the Reiss Premarital Sexual Permissiveness Scale |
| `10.2307/353412` | 2 | RESOLVED | 1995 | Miller, Richard B.; Wright, David W. | Detecting and Correcting Attrition Bias in Longitudinal Family Research |
| `10.2466/pr0.1985.56.3.1001` | 2 | RESOLVED | 1985 | Schumm, Walter R.; Bugaighis, Margaret A.; Buckler, Deborra L. | Construct Validity of the Dyadic Trust Scale |
| `10.2466/pr0.67.5.219-224` | 2 | RESOLVED | 1990 | CHOJNACKI, JOSEPH T. | RELIABILITY AND CONCURRENT VALIDITY OF THE STERNBERG TRIANGULAR LOVE SCALE |
| `10.3386/w30439` | 2 | RESOLVED | 2022 | Jeong, Dahyeon; Aggarwal, Shilpa; Robinson, Jonathan | Exhaustive or Exhausting? Evidence on Respondent Fatigue in Long Surveys |
| `10.3389/fpsyg.2011.00270` | 2 | RESOLVED | 2011 | Ardito, Rita B.; Rabellino, Daniela | Therapeutic Alliance and Outcome of Psychotherapy: Historical Excursus, Measur |
| `10.3389/fpsyg.2011.00270/full` | 2 | DEAD_BOTH | — | — | — |
| `10.3389/fpsyg.2019.01249` | 2 | RESOLVED | 2019 | Zhou, Yan; Lemmer, Gunnar; Xu, Jing | Cross-Cultural Measurement Invariance of Scales Assessing Stigma and Attitude  |
| `10.3389/fpsyg.2022.912978` | 2 | RESOLVED | 2022 | Brozowski, Alexandra; Connor-Kuntz, Hayden; Lewis, Sanaye | A test of the investment model among asexual individuals: The moderating role  |
| `10.3389/fpsyg.2023.1176067` | 2 | RESOLVED | 2023 | Bode, Adam | Romantic love evolved by co-opting mother-infant bonding |
| `10.3389/fpsyt.2025.1504306` | 2 | RESOLVED | 2025 | Lalk, Christopher; Targan, Kim; Steinbrenner, Tobias | Employing large language models for emotion detection in psychotherapy transcr |
| `10.4324/9780203732496-5` | 2 | RESOLVED | 2018 | Reis, Harry T.; Shaver, Phillip* | Intimacy as an interpersonal process |
| `10.5964/ijpr.v6i1.88` | 2 | RESOLVED | 2012 | Neto, FÃ©lix | Compassionate Love for a Romantic Partner, Love Styles and Subjective Well-Bei |
| `10.6103/SHARE.w1.900` | 2 | DATACITE_ONLY | — | — | — |
| `10.6103/SHARE.w8.900` | 2 | DATACITE_ONLY | — | — | — |
| `10.1002/9781118001868.ch4` | 1 | RESOLVED | 2010 | Fournier, Marc A.; David, D. S. Moskowitz; Zuroff, David C. | Origins and Applications of the Interpersonal Circumplex |
| `10.1002/bdm.717` | 1 | RESOLVED+MISMATCH | 2010 | Goodie, Adam S.; Doshi, Prashant; Young, Diana L. | Levels of theory‐of‐mind reasoning in competitive games |
| `10.1002/ejsp.1926` | 1 | RESOLVED+MISMATCH | 2012 | Macher, Silvia | Social interdependence in close relationships: The actor–partner‐interdependen |
| `10.1007/978-1-4020-5839-4` | 1 | RESOLVED+MISMATCH | 2008 | van Ditmarsch, Hans; van der Hoek, Wiebe; Kooi, Barteld | Dynamic Epistemic Logic |
| `10.1007/s10508-017-1015-4` | 1 | RESOLVED | 2017 | Chivers, Meredith L. | Gender/Sex, Sexual Attractions, and the Specificity of Women's Sexual Arousal: |
| `10.1007/s10994-020-05910-7` | 1 | RESOLVED | 2020 | Cerqueira, Vitor; Torgo, Luis; Mozetič, Igor | Evaluating time series forecasting models: an empirical study on performance e |
| `10.1007/s11229-015-0715-3` | 1 | RESOLVED+MISMATCH | 2015 | Borges, Rodrigo | On synchronic dogmatism |
| `10.1007/s11229-025-05259-1` | 1 | RESOLVED | 2025 | Wehofsits, Anna | Convincing ourselves: accuracy motives and rationalization |
| `10.1007/s11238-014-9448-x` | 1 | RESOLVED+MISMATCH | 2014 | Bacon, Philomena M.; Conte, Anna; Moffatt, Peter G. | Assortative mating on risk attitude |
| `10.1007/s11238-014-9448-x.pdf` | 1 | DEAD_CROSSREF | — | — | — |
| `10.1007/s12144-025-08223-x` | 1 | RESOLVED | 2025 | Morales-Vives, Fabia; Ferre-Rey, Gisela; Ferrando, Pere J. | Can different adult attachment profiles be distinguished when categorical and  |
| `10.1016/0010-0277(83)90004-5` | 1 | RESOLVED | 1983 | Wimmer, H | Beliefs about beliefs: Representation and constraining function of wrong belie |
| `10.1016/0022-0965(85)90051-7` | 1 | RESOLVED | 1985 | Perner, Josef; Wimmer, Heinz | “John thinks that Mary thinks that…” attribution of second-order beliefs by 5- |
| `10.1016/S0004-3702(98)00023-X` | 1 | RESOLVED | 1998 | Kaelbling, Leslie Pack; Littman, Michael L.; Cassandra, Anthony R. | Planning and acting in partially observable stochastic domains |
| `10.1016/S0010-0277(02)0549-8` | 1 | DEAD_BOTH | — | — | — |
| `10.1016/S0378-8733(99)00010-6` | 1 | RESOLVED | 1999 | Iacobucci, Dawn; Neelamegham, R.; Hopkins, Nigel | Measurement quality issues in dyadic models of relationships |
| `10.1016/j.adolescence.2010.07.008` | 1 | RESOLVED | 2010 | Zimmer‐Gembeck, Melanie J.; Ducat, Wendy | Positive and negative romantic relationship quality: Age, familiarity, attachm |
| `10.1016/j.copsyc.2018.01.001` | 1 | RESOLVED | 2018 | Rossignac-Milon, Maya; Higgins, E Tory | Epistemic companions: shared reality development in close relationships |
| `10.1016/j.copsyc.2019.08.013` | 1 | RESOLVED | 2020 | Cho, Minha; Keltner, Dacher | Power, approach, and inhibition: empirical advances of a theory |
| `10.1016/j.cpr.2015.07.002` | 1 | RESOLVED | 2015 | Falconier, Mariana K.; Jackson, Jeffrey B.; Hilpert, Peter | Dyadic coping and relationship satisfaction: A meta-analysis |
| `10.1016/j.dr.2016.06.004` | 1 | RESOLVED | 2016 | Putnick, Diane L.; Bornstein, Marc H. | Measurement invariance conventions and reporting: The state of the art and fut |
| `10.1016/j.jml.2012.11.001` | 1 | RESOLVED | 2013 | Barr, Dale J.; Levy, Roger; Scheepers, Christoph | Random effects structure for confirmatory hypothesis testing: Keep it maximal |
| `10.1016/j.neuroimage.2014.01.060` | 1 | RESOLVED | 2014 | Winkler, Anderson M.; Ridgway, Gerard R.; Webster, Matthew A. | Permutation inference for the general linear model |
| `10.1016/j.neuroimage.2017.06.061` | 1 | RESOLVED | 2018 | Varoquaux, Gaël | Cross-validation failure: Small sample sizes lead to large error bars |
| `10.1016/j.socnet.2009.02.004` | 1 | RESOLVED | 2010 | Snijders, Tom A.B.; van de Bunt, Gerhard G.; Steglich, Christian E.G. | Introduction to stochastic actor-based models for network dynamics |
| `10.1017/CBO9780511996481.027` | 1 | RESOLVED | 2014 | Kenny, David A.; Kashy, Deborah A. | The Design and Analysis of Data from Dyads and Groups |
| `10.1024/1662-9647.a000031` | 1 | DEAD_BOTH | — | — | — |
| `10.1026/0932-4089/a000478` | 1 | RESOLVED | 2026 | Sonnentag, Sabine; Neumer, Anna; Partsch, Fabienne | Intensive Longitudinal Methods in Work and Organizational           Psychology |
| `10.1027/1016-9040/a000068` | 1 | RESOLVED | 2011 | Bodenmann, Guy; Meuwly, Nathalie; Kayser, Karen | Two Conceptualizations of Dyadic Coping and Their Potential for Predicting Rel |
| `10.1037/0003-066X.60.2.170` | 1 | RESOLVED | 2005 | Cumming, Geoff; Finch, Sue | Inference by Eye: Confidence Intervals and How to Read Pictures of Data. |
| `10.1037/0021-9010.88.5.879` | 1 | RESOLVED | 2003 | Podsakoff, Philip M.; MacKenzie, Scott B.; Lee, Jeong-Yeon | Common method biases in behavioral research: A critical review of the literatu |
| `10.1037/0022-0167.38.2.139` | 1 | RESOLVED | 1991 | Horvath, Adam O.; Symonds, B. Dianne | Relation between working alliance and outcome in psychotherapy: A meta-analysi |
| `10.1037/0022-3514.38.4.618` | 1 | RESOLVED | 1980 | Falbo, Toni; Peplau, Letitia A. | Power strategies in intimate relationships. |
| `10.1037/0022-3514.45.1.101` | 1 | RESOLVED | 1983 | Rusbult, Caryl E. | A longitudinal test of the investment model: The development (and deterioratio |
| `10.1037/0022-3514.52.3.511` | 1 | RESOLVED | 1987 | Hazan, Cindy; Shaver, Phillip | Romantic love conceptualized as an attachment process. |
| `10.1037/0022-3514.56.5.784` | 1 | RESOLVED | 1989 | Hendrick, Clyde; Hendrick, Susan S. | Research on love: Does it measure up? |
| `10.1037/0022-3514.66.5.857` | 1 | RESOLVED | 1994 | Swann, William B.; De La Ronde, Chris; Hixon, J. Gregory | Authenticity and positivity strivings in marriage and courtship. |
| `10.1037/0022-3514.72.5.1177` | 1 | RESOLVED | 1997 | Adams, Jeffrey M.; Jones, Warren H. | The conceptualization of marital commitment: An integrative analysis. |
| `10.1037/0022-3514.74.4.939` | 1 | RESOLVED | 1998 | Agnew, Christopher R.; Van Lange, Paul A. M.; Rusbult, Caryl E. | Cognitive interdependence: Commitment and the mental representation of close r |
| `10.1037/0022-3514.75.2.332` | 1 | RESOLVED | 1998 | Gilovich, Thomas; Savitsky, Kenneth; Medvec, Victoria Husted | The illusion of transparency: Biased assessments of others' ability to read on |
| `10.1037/0022-3514.78.6.1053` | 1 | RESOLVED | 2000 | Collins, Nancy L.; Feeney, Brooke C. | A safe haven: An attachment theory perspective on support seeking and caregivi |
| `10.1037/0022-3514.80.6.1011` | 1 | RESOLVED | 2001 | Fleeson, William | Toward a structure- and process-integrated view of personality: Traits as dens |
| `10.1037/0022-3514.80.6.972` | 1 | RESOLVED | 2001 | Feeney, Brooke C.; Collins, Nancy L. | Predictors of caregiving in adult intimate relationships: An attachment theore |
| `10.1037/0022-3514.88.3.480` | 1 | RESOLVED | 2005 | Neff, Lisa A.; Karney, Benjamin R. | To Know You Is to Love You: The Implications of Global Adoration and Specific  |
| `10.1037/0022-3514.92.3.458` | 1 | RESOLVED | 2007 | Bolger, Niall; Amarel, David | Effects of social support visibility on adjustment to stress: Experimental evi |
| `10.1037/0022-3514.92.4.678` | 1 | RESOLVED | 2007 | Roisman, Glenn I.; Holland, Ashley; Fortuna, Keren | The Adult Attachment Interview and self-reports of attachment style: An empiri |
| `10.1037/0033-2909.102.3.390` | 1 | RESOLVED | 1987 | Kenny, David A.; Albright, Linda | Accuracy in interpersonal perception: A social relations analysis. |
| `10.1037/0033-2909.116.3.457` | 1 | RESOLVED | 1994 | Collins, Nancy L.; Miller, Lynn Carol | Self-disclosure and liking: A meta-analytic review. |
| `10.1037/0033-295X.102.2.246` | 1 | RESOLVED | 1995 | Mischel, Walter; Shoda, Yuichi | A cognitive-affective system theory of personality: Reconceptualizing situatio |
| `10.1037/0033-295x.110.2.265` | 1 | RESOLVED | 2003 | Keltner, Dacher; Gruenfeld, Deborah H.; Anderson, Cameron | Power, approach, and inhibition. |
| `10.1037/0893-3200.19.2.314` | 1 | RESOLVED | 2005 | Laurenceau, Jean-Philippe; Barrett, Lisa Feldman; Rovine, Michael J. | The Interpersonal Process Model of Intimacy in Marriage: A Daily-Diary and Mul |
| `10.1037/1082-989X.10.1.3` | 1 | RESOLVED | 2005 | Cole, David A.; Martin, Nina C.; Steiger, James H. | Empirical and Conceptual Problems With Longitudinal Trait-State Models: Introd |
| `10.1037/1089-2680.2.2.175` | 1 | RESOLVED | 1998 | Nickerson, Raymond S. | Confirmation Bias: A Ubiquitous Phenomenon in Many Guises |
| `10.1037/a0019651` | 1 | RESOLVED | 2010 | Kenny, David A.; Ledermann, Thomas | Detecting, measuring, and testing dyadic patterns in the actor–partner interde |
| `10.1037/a0029052` | 1 | RESOLVED | 2012 | Lavner, Justin A.; Bradbury, Thomas N.; Karney, Benjamin R. | Incremental change or initial differences? Testing two models of marital deter |
| `10.1037/bul0000349` | 1 | RESOLVED | 2021 | Leib, Margarita; Köbis, Nils; Soraperra, Ivan | Collaborative dishonesty: A meta-analytic review. |
| `10.1037/dev0000902` | 1 | RESOLVED | 2020 | Bailey, Drew H.; Oh, Yoonkyung; Farkas, George | Reciprocal effects of reading and mathematics? Beyond the cross-lagged panel m |
| `10.1037/gpr0000066` | 1 | RESOLVED | 2016 | Lemay, Edward P.; Venaglia, Rachel B. | Relationship Expectations and Relationship Quality |
| `10.1037/met0000062` | 1 | RESOLVED | 2016 | Schuurman, Noémi K.; Ferrer, Emilio; de Boer-Sonnenschein, Mieke | How to compare cross-lagged associations in a multilevel autoregressive model. |
| `10.1037/met0000239` | 1 | RESOLVED | 2020 | Hamaker, Ellen L.; Muthén, Bengt | The fixed versus random effects debate and how it relates to centering in mult |
| `10.1037/met0000250` | 1 | RESOLVED | 2020 | McNeish, Daniel; Hamaker, Ellen L. | A primer on two-level dynamic structural equation models for intensive longitu |
| `10.1037/met0000624` | 1 | RESOLVED | 2025 | Maassen, Esther; D'Urso, E. Damiano; van Assen, Marcel A. L. M. | The dire disregard of measurement invariance testing in psychological science. |
| `10.1037/met0000720` | 1 | RESOLVED | 2025 | Muthén, Bengt; Asparouhov, Tihomir; Shiffman, Saul | Dynamic structural equation modeling with floor effects. |
| `10.1037/pas0000275` | 1 | RESOLVED | 2016 | Fried, Eiko I.; van Borkulo, Claudia D.; Epskamp, Sacha | Measuring depression over time . . . Or not? Lack of unidimensionality and lon |
| `10.1037/pspi0000266` | 1 | RESOLVED | 2021 | Rossignac-Milon, Maya; Bolger, Niall; Zee, Katherine S. | Merged minds: Generalized shared reality in dyadic relationships. |
| `10.1037/pspp0000551` | 1 | RESOLVED | 2025 | Bühler, Janina Larissa; Orth, Ulrich | Terminal decline of satisfaction in romantic relationships: Evidence from four |
| `10.1037/pst0000172` | 1 | RESOLVED | 2018 | Flückiger, Christoph; Del Re, A. C.; Wampold, Bruce E. | The alliance in adult psychotherapy: A meta-analytic synthesis. |
| `10.1037/t01997-000` | 1 | RESOLVED | 1990 | Collins, Nancy L.; Read, Stephen J. | Adult Attachment Scale |
| `10.1038/s41562-016-0021` | 1 | RESOLVED | 2017 | Munafò, Marcus R.; Nosek, Brian A.; Bishop, Dorothy V. M. | A manifesto for reproducible science |
| `10.1038/s41562-016-0034` | 1 | RESOLVED | 2017 | — | Promoting reproducibility with registered reports |
| `10.1073/pnas.1708274114` | 1 | RESOLVED | 2018 | Nosek, Brian A.; Ebersole, Charles R.; DeHaven, Alexander C. | The preregistration revolution |
| `10.1073/pnas.2209460119` | 1 | RESOLVED | 2022 | Johnson, Matthew D.; Lavner, Justin A.; Muise, Amy | Women and Men are the Barometers of Relationships: Testing the Predictive Powe |
| `10.1073/pnas.2305016120` | 1 | RESOLVED | 2023 | Gilardi, Fabrizio; Alizadeh, Meysam; Kubli, Maël | ChatGPT outperforms crowd workers for text-annotation tasks |
| `10.1080/00223891.2018.1521418` | 1 | RESOLVED | 2019 | Neubauer, Andreas B.; Voelkle, Manuel C.; Voss, Andreas | Estimating Reliability of Within-Person Couplings in a Multilevel Framework |
| `10.1080/00273171.2018.1446819` | 1 | RESOLVED | 2018 | Hamaker, E. L.; Asparouhov, T.; Brose, A. | At the Frontiers of Modeling Intensive Longitudinal Data: Dynamic Structural E |
| `10.1080/01621459.2023.2197686` | 1 | RESOLVED | 2023 | Bates, Stephen; Hastie, Trevor; Tibshirani, Robert | Cross-Validation: What Does It Estimate and How Well Does It Do It? |
| `10.1080/03637751.2013.813632` | 1 | RESOLVED | 2013 | Schrodt, Paul; Witt, Paul L.; Shimkowski, Jenna R. | A Meta-Analytical Review of the Demand/Withdraw Pattern of Interaction and its |
| `10.1080/10463283.2017.1333315` | 1 | RESOLVED | 2017 | Echterhoff, Gerald; Higgins, E. Tory | Creating shared reality in interpersonal and intergroup communication: the rol |
| `10.1080/1047840x.2014.876909` | 1 | RESOLVED | 2014 | Pietromonaco, Paula R.; Perry-Jenkins, Maureen | Marriage in Whose America? What the Suffocation Model Misses |
| `10.1080/10705511.2016.1253479` | 1 | RESOLVED | 2016 | Asparouhov, Tihomir; Hamaker, Ellen L.; Muthén, Bengt | Dynamic Latent Class Analysis |
| `10.1080/10705511.2017.1406803` | 1 | RESOLVED | 2017 | Asparouhov, Tihomir; Hamaker, Ellen L.; Muthén, Bengt | Dynamic Structural Equation Models |
| `10.1080/10705511.2019.1626733` | 1 | RESOLVED | 2019 | Asparouhov, Tihomir; Muthén, Bengt | Comparison of Models for the Analysis of Intensive Longitudinal Data |
| `10.1080/10705511.2020.1784738` | 1 | RESOLVED | 2020 | Mulder, Jeroen D.; Hamaker, Ellen L. | Three Extensions of the Random Intercept Cross-Lagged Panel Model |
| `10.1080/10705511.2020.1821690` | 1 | RESOLVED | 2020 | Usami, Satoshi | On the Differences between General Cross-Lagged Panel Model and Random-Interce |
| `10.1080/10705511.2023.2191292` | 1 | RESOLVED | 2023 | Robitzsch, Alexander; Lüdtke, Oliver | Why Full, Partial, or Approximate Measurement Invariance Are Not a Prerequisit |
| `10.1080/10705511.2024.2316586` | 1 | RESOLVED | 2024 | Mulder, Jeroen D.; Luijken, Kim; Penning de Vries, Bas B. L. | Causal Effects of Time-Varying Exposures: A Comparison of Structural Equation  |
| `10.1080/10705511.2024.2355579` | 1 | RESOLVED | 2024 | Mulder, Jeroen D.; Usami, Satoshi; Hamaker, Ellen L. | Joint Effects in Cross-Lagged Panel Research Using Structural Nested Mean Mode |
| `10.1080/10705511.2024.2406510` | 1 | RESOLVED | 2024 | Muthén, Bengt; Asparouhov, Tihomir; Keijsers, Loes | Dynamic Structural Equation Modeling with Cycles |
| `10.1080/10705511.2025.2608122` | 1 | RESOLVED | 2026 | Asparouhov, Tihomir; Muthén, Bengt | Three-Level Dynamic Structural Equation Modeling |
| `10.1080/14616734.2013.782654` | 1 | RESOLVED | 2013 | Feeney, Brooke C.; Collins, Nancy L.; Van Vleet, Meredith | Motivations for providing a secure base: links with attachment orientation and |
| `10.1086/226863` | 1 | RESOLVED | 1979 | Tuma, Nancy Brandon; Hannan, Michael T.; Groeneveld, Lyle P. | Dynamic Analysis of Event Histories |
| `10.1086/230539` | 1 | RESOLVED | 1994 | Kollock, Peter | The Emergence of Exchange Structures: An Experimental Study of Uncertainty, Co |
| `10.1086/231213` | 1 | RESOLVED | 1997 | Silverstein, Merril; Bengtson, Vern L. | Intergenerational Solidarity and the Structure of Adult Child‐Parent Relations |
| `10.1093/sf/55.1.123` | 1 | RESOLVED | 1976 | Bacharach, Samuel B.; Lawler, Edward J. | The Perception of Power |
| `10.1098/rspb.2011.0805` | 1 | RESOLVED | 2011 | Gneezy, Ayelet; Fessler, Daniel M. T. | Conflict, sticks and carrots: war increases prosocial punishments and rewards |
| `10.1111/1468-5884.00030` | 1 | RESOLVED | 2003 | Masuda, Masahiro | Meta‐analyses of love scales: Do various love scales measure the same psycholo |
| `10.1111/cdev.12660` | 1 | RESOLVED+MISMATCH | 2017 | Berry, Daniel; Willoughby, Michael T | On the Practical Interpretability of Cross-Lagged Panel Models: Rethinking a D |
| `10.1111/ecog.02881` | 1 | RESOLVED | 2017 | Roberts, David R.; Bahn, Volker; Ciuti, Simone | Cross‐validation strategies for data with temporal, spatial, hierarchical, or  |
| `10.1111/famp.12811` | 1 | RESOLVED | 2022 | Cruwys, Tegan; South, Erica I.; Halford, William Kim | Measuring “we‐ness” in couple relationships: A social identity approach |
| `10.1111/fare.12885` | 1 | RESOLVED | 2023 | Carrese‐Chacra, Emily; Hollett, Kayla; Erdem, Gizem | Longitudinal effects of pandemic stressors and dyadic coping on relationship s |
| `10.1111/j.1467-8721.2009.01657.x` | 1 | RESOLVED | 2009 | Rusbult, Caryl E.; Finkel, Eli J.; Kumashiro, Madoka | The Michelangelo Phenomenon |
| `10.1111/j.1467-9280.2009.02388.x` | 1 | RESOLVED | 2009 | Maisel, Natalya C.; Gable, Shelly L. | The Paradox of Received Social Support |
| `10.1111/j.1475-6811.1994.tb00068.x` | 1 | RESOLVED | 1994 | FEHR, BEVERLEY | Prototype‐based assessment of laypeople's views of love |
| `10.1111/j.1475-6811.1996.tb00116.x` | 1 | RESOLVED | 1996 | CARNELLEY, KATHERINE B.; PIETROMONACO, PAULA R.; JAFFE, KENNETH | Attachment, caregiving, and relationship functioning in couples: Effects of se |
| `10.1111/j.1475-6811.1997.tb00145.x` | 1 | RESOLVED+MISMATCH | 1997 | LAMM, HELMUT; WIESMANN, ULRICH | Subjective attributes of attraction: How people characterize their liking, the |
| `10.1111/j.1475-6811.1999.tb00202.x` | 1 | RESOLVED | 1999 | KENNY, DAVID A.; COOK, WILLIAM | Partner effects in relationship research: Conceptual issues, analytic difficul |
| `10.1111/j.1475-6811.2001.tb00034.x` | 1 | RESOLVED | 2001 | ACITELLI, LINDA K.; KENNY, DAVID A.; WEINER, DEBRA | The importance of similarity and understanding of partners' marital ideals to  |
| `10.1111/j.1475-6811.2010.01282.x` | 1 | RESOLVED+MISMATCH | 2010 | LACKENBAUER, SANDRA D.; CAMPBELL, LORNE; RUBIN, HARRIS | The unique and combined benefits of accuracy and positive bias in relationship |
| `10.1111/j.1545-5300.1983.00069.x` | 1 | RESOLVED | 1983 | OLSON, DAVID H.; RUSSELL, CANDYCE S.; SPRENKLE, DOUGLAS H. | Circumplex Model of Marital and Family Systems: Vl. Theoretical Update |
| `10.1111/j.1571-9979.2003.tb00771.x` | 1 | RESOLVED | 2003 | Boven, Leaf Van; Gilovich, Thomas; Medvec, Victoria Husted | The Illusion of Transparency in Negotiations |
| `10.1111/j.1741-3737.2007.00468.x` | 1 | RESOLVED | 2008 | Voorpostel, Marieke; Blieszner, Rosemary | Intergenerational Solidarity and Support Between Adult Siblings |
| `10.1111/j.1747-9991.2006.00035.x` | 1 | RESOLVED | 2006 | Lackey, Jennifer | Knowing from Testimony |
| `10.1111/j.1933-1592.2006.tb00586.x` | 1 | RESOLVED+MISMATCH | 2006 | GOLDBERG, Sanford; HENDERSON, David | Monitoring and Anti-Reductionism in the Epistemology of Testimony |
| `10.1111/jedm.12000` | 1 | RESOLVED | 2013 | Kane, Michael T. | Validating the Interpretations and Uses of Test Scores |
| `10.1111/jomf.12201` | 1 | RESOLVED | 2015 | Hardesty, Jennifer L.; Crossman, Kimberly A.; Haselschwerdt, Megan L. | Toward a Standard Approach to Operationalizing Coercive Control and Classifyin |
| `10.1111/pere.12060` | 1 | RESOLVED | 2014 | GARCIA, RANDI L.; KENNY, DAVID A.; LEDERMANN, THOMAS | Moderation in the actor–partner interdependence model |
| `10.1111/pere.12133` | 1 | RESOLVED | 2016 | RODRIGUEZ, LINDSEY M.; ØVERUP, CAMILLA S.; WICKHAM, ROBERT E. | Communication with former romantic partners and current relationship outcomes  |
| `10.1111/pere.12447` | 1 | RESOLVED | 2022 | Krueger, Kori; Forest, Amanda | Putting responsiveness in context: How a partner's responsiveness baseline sha |
| `10.1111/spc3.70042` | 1 | RESOLVED | 2025 | Joel, Samantha; Eastwick, Paul W.; Khera, Devinder | A Credibility Revolution for Relationship Science: Where Can We Step Up Our Ga |
| `10.1111/spc3.70045` | 1 | RESOLVED | 2025 | Sakaluk, John Kitchener; Joel, Samantha; Quinn‐Nilas, Christopher | A Renewal of Dyadic Structural Equation Modeling With Latent Variables: Clarif |
| `10.1126/sciadv.aap9815` | 1 | RESOLVED | 2018 | Bruch, Elizabeth E.; Newman, M. E. J. | Aspirational pursuit of mates in online dating markets |
| `10.1126/science.1116681` | 1 | RESOLVED | 2005 | Grimm, Volker; Revilla, Eloy; Berger, Uta | Pattern-Oriented Modeling of Agent-Based Complex Systems: Lessons from Ecology |
| `10.1126/science.aaa9375` | 1 | RESOLVED | 2015 | Dwork, Cynthia; Feldman, Vitaly; Hardt, Moritz | The reusable holdout: Preserving validity in adaptive data analysis |
| `10.1145/3703155` | 1 | RESOLVED+MISMATCH | 2025 | Huang, Lei; Yu, Weijiang; Ma, Weitao | A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Chal |
| `10.1146/annurev-psych-010416-044153` | 1 | RESOLVED | 2017 | Guinote, Ana | How Power Affects People: Activating, Wanting, and Goal Seeking |
| `10.1146/annurev-psych-010418-102813` | 1 | RESOLVED | 2019 | Fraley, R. Chris | Attachment in Adulthood: Recent Developments, Emerging Debates, and Future Dir |
| `10.1146/annurev-psych-012224-025712` | 1 | RESOLVED | 2025 | Eastwick, Paul W.; Joel, Samantha | How Do People Feel About Mates? |
| `10.1146/annurev-psych-040325-025418` | 1 | RESOLVED | 2026 | Laurenceau, Jean-Philippe; DiGiovanni, Ana M.; Bolger, Niall | Intensive Longitudinal Methods: Toward a Psychological Science of Daily Life |
| `10.1146/annurev-statistics-060116-054035` | 1 | RESOLVED | 2017 | Snijders, Tom A.B. | Stochastic Actor-Oriented Models for Network Dynamics |
| `10.1162/coli.07-034-R2` | 1 | RESOLVED | 2008 | Artstein, Ron; Poesio, Massimo | Inter-Coder Agreement for Computational Linguistics |
| `10.1162/coli_a_00502` | 1 | RESOLVED | 2024 | Ziems, Caleb; Held, William; Shaikh, Omar | Can Large Language Models Transform Computational Social
                    S |
| `10.1177/0146167203252807` | 1 | RESOLVED | 2003 | Feeney, Brooke C.; Collins, Nancy L. | Motivations for Caregiving in Adult Intimate Relationships: Influences on Care |
| `10.1177/0146167210383045` | 1 | RESOLVED | 2010 | Overall, Nickola C.; Fletcher, Garth J. O.; Simpson, Jeffry A. | Helping Each Other Grow: Romantic Partner Support, Self-Improvement, and Relat |
| `10.1177/0146167211432764` | 1 | RESOLVED | 2012 | Overall, Nickola C.; Fletcher, Garth J. O.; Kenny, David A. | When Bias and Insecurity Promote Accuracy |
| `10.1177/0146167220921717` | 1 | RESOLVED | 2020 | Emery, Lydia F.; Gardner, Wendi L.; Carswell, Kathleen L. | Who are “We”? Couple Identity Clarity and Romantic Relationship Commitment |
| `10.1177/01461672221113981` | 1 | RESOLVED | 2022 | Pusch, Sebastian; Neyer, Franz J.; Hagemeyer, Birk | Closeness Discrepancies in Couple Relationships: A Dyadic Response Surface Ana |
| `10.1177/0146167297234003` | 1 | RESOLVED | 1997 | Aron, Arthur; Melinat, Edward; Aron, Elaine N. | The Experimental Generation of Interpersonal Closeness: A Procedure and Some P |
| `10.1177/019251391012001003` | 1 | RESOLVED+MISMATCH | 1991 | BUMPASS, LARRY L.; MARTIN, TERESA CASTRO; SWEET, JAMES A. | The Impact of Family Background and Early Marital Factors on Marital Disruptio |
| `10.1177/0192513X211064876` | 1 | RESOLVED | 2022 | Blake, Lucy; Bland, Becca; Rouncefield-Swales, Alison | Estrangement Between Siblings in Adulthood: A Qualitative Exploration |
| `10.1177/0192513x10385788` | 1 | RESOLVED | 2010 | Owen, Jesse; Rhoades, Galena K.; Stanley, Scott M. | The Revised Commitment Inventory: Psychometrics and Use With Unmarried Couples |
| `10.1177/0265407500173006` | 1 | RESOLVED | 2000 | Weigel, Dan; Murray, Colleen | The Paradox of Stability and Change in Relationships: What Does Chaos Theory O |
| `10.1177/0265407507086804` | 1 | RESOLVED | 2008 | Kellas, Jody Koenig; Bean, Dawn; Cunningham, Cherakah | The ex-files: Trajectories, turning points, and adjustment in the development  |
| `10.1177/0265407510389126` | 1 | RESOLVED | 2010 | Graham, James M. | Measuring love in romantic relationships: A meta-analysis |
| `10.1177/0265407518822783` | 1 | RESOLVED+MISMATCH | 2019 | Coy, Anthony E.; Davis, Jody L.; Green, Jeffrey D. | A dyadic model of investments: Partner effects on commitment |
| `10.1177/02654075211017675` | 1 | RESOLVED+MISMATCH | 2021 | Bar-Shachar, Yael; Bar-Kalifa, Eran | Responsiveness processes and daily experiences of shared reality among romanti |
| `10.1177/026540758800500207` | 1 | RESOLVED | 1988 | Kenny, David A. | Interpersonal Perception: A Social Relations Analysis |
| `10.1177/0265407598152004` | 1 | RESOLVED | 1998 | Solomon, Denise Haunani; Samp, Jennifer Anne | Power and Problem Appraisal: Perceptual Foundations of the Chilling Effect in  |
| `10.1177/08902070221085877` | 1 | RESOLVED | 2022 | Eastwick, Paul W; Joel, Samantha; Carswell, Kathleen L | Predicting romantic interest during early relationship development: A preregis |
| `10.1177/0956797611417632` | 1 | RESOLVED | 2011 | Simmons, Joseph P.; Nelson, Leif D.; Simonsohn, Uri | False-Positive Psychology |
| `10.1177/0956797620980754` | 1 | RESOLVED | 2021 | Wolf, Wouter; Nafe, Amanda; Tomasello, Michael | The Development of the Liking Gap: Children Older Than 5 Years Think That Part |
| `10.1177/096228029900800105` | 1 | RESOLVED | 1999 | Kenward, M G; Molenberghs, G | Parametric models for incomplete continuous and categorical longitudinal data |
| `10.1177/1059712314547709` | 1 | RESOLVED | 2014 | Mudimu, Edinah; Engelbrecht, Gerhard Nieuwoudt | Agent-based model for social and sexual partnerships formation |
| `10.1177/16094069241231168` | 1 | RESOLVED | 2024 | Tai, Robert H.; Bentley, Lillian R.; Xia, Xin | An Examination of the Use of Large Language Models to Aid Analysis of Textual  |
| `10.1177/1745691616658637` | 1 | RESOLVED | 2016 | Steegen, Sara; Tuerlinckx, Francis; Gelman, Andrew | Increasing Transparency Through a Multiverse Analysis |
| `10.1177/1948550617693063` | 1 | RESOLVED | 2017 | Flake, Jessica K.; Pek, Jolynn; Hehman, Eric | Construct Validation in Social and Personality Research |
| `10.1177/2515245919882903` | 1 | RESOLVED | 2020 | Hussey, Ian; Hughes, Sean | Hidden Invalidity Among 15 Commonly Used Measures in Social and Personality Ps |
| `10.1177/25152459241302300` | 1 | RESOLVED | 2025 | Cole, David A.; Abitante, George; Kan, Hoi | Practical Problems Estimating and Reporting Power When Hypotheses Are Embedded |
| `10.1177/25152459251351286` | 1 | RESOLVED | 2025 | del Rosario, Kareena S.; West, Tessa V. | A Practical Guide to Specifying Random Effects in Longitudinal Dyadic Multilev |
| `10.1177/25152459251410153` | 1 | RESOLVED | 2026 | Lin, Zhicheng | Large Language Models as Psychological Simulators: A Methodological Guide |
| `10.1177/…` | 1 | NOT_FOUND | — | — | — |
| `10.1214/14-STS501` | 1 | RESOLVED | 2014 | Ogburn, Elizabeth L.; VanderWeele, Tyler J. | Causal Diagrams for Interference |
| `10.1214/16-AOAS1005` | 1 | RESOLVED | 2017 | Aronow, Peter M.; Samii, Cyrus | Estimating average causal effects under general interference, with application |
| `10.12758/mda.2013.013` | 1 | DATACITE_ONLY | — | — | — |
| `10.13718/j.cnki.xdzk.2020.06.013` | 1 | DATACITE_ONLY | — | — | — |
| `10.18653/v1/2025.emnlp-main.144` | 1 | RESOLVED | 2025 | Ivey, Jonathan; Gauch, Susan; Jurgens, David | NUTMEG: Separating Signal From Noise in Annotator Disagreement |
| `10.2117/psysoc.2016.1` | 1 | RESOLVED | 2016 | SINGH, Ramadhar; GOH, Amanda; SANKARAN, Krithiga | SIMILARITY AND LIKING EFFECTS ON INTERPERSONAL ATTRACTION: TEST OF THE TWO-DIM |
| `10.21248/jlcl.38.2025.289` | 1 | RESOLVED | 2025 | Münker, Simon | Political Bias in LLMs: Unaligned Moral Values in Agent-centric Simulations |
| `10.2307/2092623` | 1 | RESOLVED+MISMATCH | 1960 | Gouldner, Alvin W. | The Norm of Reciprocity: A Preliminary Statement |
| `10.2307/2265159` | 1 | DEAD_BOTH | — | — | — |
| `10.2307/2578749` | 1 | RESOLVED | 1987 | Lawler, Edward J.; Bacharach, Samuel B. | Comparison of Dependence and Punitive Forms of Power |
| `10.2307/352993` | 1 | RESOLVED | 1991 | Bengtson, Vern L.; Roberts, Robert E. L. | Intergenerational Solidarity in Aging Families: An Example of Formal Theory Co |
| `10.2478/jos-2022-0041` | 1 | RESOLVED | 2022 | Yan, Ting; Williams, Douglas | Response Burden – Review and Conceptual Framework |
| `10.3102/10769986024002179` | 1 | RESOLVED+MISMATCH | 1999 | Vermunt, Jeroen K.; Langeheine, Rolf; Bockenholt, Ulf | Discrete-Time Discrete-State Latent Markov Models with Time-Constant and Time- |
| `10.31219/osf.io/gu8z7` | 1 | RESOLVED | 2017 | Joel, Samantha; Eastwick, Paul Wolfe; Finkel, Eli | Is Romantic Desire Predictable? Machine Learning Applied to Initial Romantic A |
| `10.31234/osf.io/dus42` | 1 | RESOLVED | 2024 | Robitzsch, Alexander; Lüdtke, Oliver | Illusory Between-person Component in the Random Intercept Cross-lagged Panel M |
| `10.31234/osf.io/f6wbn` | 1 | DEAD_BOTH | — | — | — |
| `10.31234/osf.io/rs7eu_v1` | 1 | RESOLVED | 2025 | Lucas, Richard E.; Weidmann, Rebekka; Yang, Hyewon | Typical Patterns of Stability in Longitudinal Data: Implications for Model Cho |
| `10.3389/fphy.2018.00021` | 1 | RESOLVED | 2018 | Tuzón, Paula; Fernández-Gracia, Juan; Eguíluz, Víctor M. | From Continuous to Discontinuous Transitions in Social Diffusion |
| `10.3389/fpsyg.2014.00452` | 1 | RESOLVED | 2014 | Kyselo, Miriam; Tschacher, Wolfgang | An enactive and dynamical systems theory account of dyadic relationships |
| `10.3389/fpsyg.2019.00571` | 1 | RESOLVED+MISMATCH | 2019 | Falconier, Mariana Karin; Kuhn, Rebekka | Dyadic Coping in Couples: A Conceptual Integration and a Review of the Empiric |
| `10.3390/ejihpe12070054` | 1 | RESOLVED | 2022 | Robitzsch, Alexander | Exploring the Multiverse of Analytical Decisions in Scaling Educational Large- |
| `10.3390/ijerph17249306` | 1 | RESOLVED | 2020 | Guzmán-González, Mónica; Calderón, Carlos; Murray, Carol | Evidence for a Bifactor Structure of the Caregiving Questionnaire with Individ |
| `10.3724/SP.J.1041.2016.00989` | 1 | RESOLVED | 2016 | LI, Caina; SUN, Ying; TUO, Rui | The effects of attachment security on interpersonal trust: The moderating role |
| `10.4135/9781483327648.n3` | 1 | RESOLVED | 1996 | Moreland, Richard L.; Argote, Linda; Krishnan, Ranjani | Socially Shared Cognition at Work: Transactive Memory and
                     |
| `10.4324/9780203311851-29` | 1 | RESOLVED+MISMATCH | 2004 | — | Transactive memory in close relationships |
| `10.4324/9780203848852.ch17` | 1 | RESOLVED+MISMATCH | None | Kenny, David A.; Kashy, Deborah A. | Dyadic Data Analysis Using Multilevel Modeling |
| `10.5465/AMR.2007.24348410` | 1 | RESOLVED | 2007 | Schoorman, F. David; Mayer, Roger C.; Davis, James H. | An Integrative Model of Organizational Trust: Past, Present, and Future |
| `10.5465/amr.1998.926620` | 1 | RESOLVED | 1998 | Lewicki, Roy J.; McAllister, Daniel J.; Bies, Robert J. | Trust and Distrust: New Relationships and Realities |

---

## 7. `conclusions_and_negative_results`（证据基弱到连 hedge 都不该写的点）

1. **R03 `X9`（PRI）的整个测量学档案。** 承重 DOI 死链（F-01）+ 零 `CITED_PRIMARY`（F-13）。在 DOI 修正并补标证据等级之前，**不应**以任何强度引用「PRI 是强 directed `DIRECT_PROXY`」这一结论所依赖的 `N=2,334` / `α=.93` / `ω_WP=.83` / 「Study 3 APIM 显示 i 的 PRI 与 j 的自报行为相关」这组数字。构念层的判断（"i 感知 j 的 responsiveness" 是天然的 directed 构念）**不依赖**这组数字，仍然成立。
2. **R14 §2.4「跨关系类型稳定性是硬判据」。** R11（`:23`）与 R17（`:514`）已各自独立指出 Le & Agnew (2003) 内部自相矛盾（同时说 moderators vary minimally 与 significantly stronger in relational domains），R17 明确写「LHRM §2.4 把它当硬判据，**超出了文献共识**」。A01 追加一条：R01 给这个领域最核心的跨方法论综述（Roisman）配了一个**指向另一篇论文的、且自标 ✓ 的 DOI**（F-09）。**在 F-09 修好之前，"跨关系类型稳定性"这一整条判据的文献基础无法审计。**
3. **R14 的 novelty / REUSE 论证。** 全部建立在 F-28 那批 `AGENT_RECALL` 上，包括自称"最高优先 prior-art"的 Acitelli & Antonioni。**这条线目前不具备可辩护的证据基座**，无论结论方向如何。
4. **R03 `:130` 的"整个工具族不可比"。** R03 自己称之为"本 packet 对 `OutcomeDependence` 最重的一份证据"，但该断言改写了来源原句、与自己下一行矛盾、且用了来源没有的数字（F-14）。R10 的同源引用才是准确的。
5. **`R²=.54 (95% CI [.53,.55])` 与 `β²` 系列值。** `R²=.54` 本身可信；**CI 与 `β²` 不可信到可引用的程度**（F-15）。它已被 manifest 提升为 R02 的头号承重指针。
6. **全部非 DOI 指针的当前可访问性。** 本次**没有测**（§2.2 第 1 条）。`exa.ai/library/...`、`sage.cnpereading.com`、`link.springer.com/...pdf`、`xbgjxt.swu.edu.cn` 等大量指针的死链率**未知**。R03 `:78` 自己已标 `UNVERIFIED_DOI`（Wheeler et al. 2025 泛信任量表综述，走 exa.ai），这是**正确**的处理方式，但同样的纪律没有推广到其他 exa.ai 引用上。

---

## 8. `remaining_unknown`

1. **非 DOI / URL 指针的死链率**——本次完全未测，这是最大的未知。
2. **353 个 DOI 中 340+ 条的内容级匹配**。我只做到"这篇论文存在且书目正确"，没做"这篇论文支持这句话"。9 个承重数字的摘要级核对见 §4.2。
3. **arXiv 指针的 37/40 未核**。arXiv API 在本环境持续 429（我必须写明：批量查询曾对 43 个 ID 全部返回 MISSING，包括我已单独证实的 `2304.03442`——**该 API 通道在本环境整体不可用，其输出不构成任何证据**）。改用 `arxiv.org/abs/` 直抓的 2 条均真实。剩余 37 条状态 `UNKNOWN`。
4. **Poesio 2012 / Balan 1968 / Weiss & Murchison 2005 的真实 DOI**。R17 已正确弃用；我用 Crossref 书目检索也未命中。**这三篇文献是否真实存在于报告所述的卷期，本身我未能确认。**
5. **Acitelli & Antonioni (2006) "Twenty dimensions of marriage" 是否真实存在于 JPSP 90(6)**（F-28）。Crossref 书目检索未命中。
6. **ISBN / 数据集官方文档版本号 / GitHub issue comment id 的 currentness。** R04 `:141` 写 `SHARE release 9.0.0, 2024-03-28`、`:85` 写 `PAIRFAM Release 14.2`——我验证了这两个 DOI 有效（302 → share-eric.eu / gesis ZA5678），但**未验证版本号与日期**。
7. **R15 的法律文书实体内容。** `SUBSTANCE_NOT_READ` 是 R15 自陈的；A01 未推翻也未确认。
8. **审计基线本身不稳定**（§2.3）。本报告的行号在 parent 读到它时可能已失效。
9. **Crossref 之外的注册机构。** 我用 Crossref + `doi.org` 302 两条通道；DataCite 走 `doi.org` 时被救回 5 条。若某 lane 曾用别的核验通道（DataCite REST、OpenAlex、Semantic Scholar），其结论可能与我不同。

---

## 9. `explicit_non_claims`（我明确不主张什么）

1. **我不主张这个 swarm 的证据质量整体高或整体低。** 我只报告我测到的东西：353 个 DOI 中 87.3% 书目正确、97.2% 可解析；29 条错配集中在特定 lane；证据等级词表在 18 个 lane 间不统一。**这不支持任何关于"swarm 好/不好"的整体判断。**
2. **我不主张任何一条构念裁决错了。** F-01/F-03/F-14/F-28 会改变某些 lane 的证据强度，但不裁定"PRI 该不该是 `DIRECT_PROXY`""power 该不该有独立坐标""跨关系类型稳定性算不算硬判据"。那是 A02/A03 与 Architect 的事。
3. **我不主张发现了伪造引用。** 0 条。9 条死链里 5 条是报告侧格式错或可修的转写错，3 条是 R17 自陈并弃用的 `FETCH_FAILED`，1 条是字面占位符。**没有任何一条被用于承重结论而不自陈的。**
4. **我不主张 §5 里的 `MINOR` 项都需要修。** 19 条 MINOR 中有 7 条是 online-first 年与卷期年之差（F-33），属正常引用实践。
5. **我不主张 `AGENT_RECALL` 的使用有问题。** 相反：R01/R09/R17/R12/R13/R05/R10 都**显式声明了"`AGENT_RECALL` 不得作为裁决依据"**，R17 甚至写"不承重"。**这是本 swarm 做得最好的部分之一**，F-28/F-34 的对象是"承重位置上的 `AGENT_RECALL`"，不是"用了 `AGENT_RECALL`"。
6. **我不主张 §5 之外没有缺陷。** 我的自动筛查（作者名不匹配 48 条 / 年份不匹配 18 条）**只在这 66 条上做了人工细读**；剩余 287 条"自动匹配通过"的，我只核到解析成功 + 书目字段，不排除其中还有内容级错配。
7. **我不主张 arXiv 指针有问题。** 抽到的 2 条都真实，且 R13 对其内容的转述与摘要**高度一致**（包括 4 个而非 3 个 provider family 这一处小疏漏）。
8. **我不主张 `R12`「无一个可比先例」或 `R02`「该 ESEM 研究不存在」这类 `NEGATIVE` 结论错了。** R12 自己写了「不主张…已被证明『不存在』——只主张本次在指定渠道内未能核实（`NEGATIVE`，非 `DISPROVEN`）」，R02 写了「这不是本轮检索不足，是文献里确实不存在」并给了多路检索日志。**这两处的措辞纪律是全 swarm 的正面示范**，我未找到反证。
9. **我不主张我修改过任何东西。** 本 lane 全程只读 `D:\coding\lhrm`，唯一写入是 `C:\Users\gg828\AppData\Local\Temp\opencode\lanes\` 下的临时文件与本 packet。

### 9.1 Round 3 `A1` 追加的 non-claims（bookkeeping 修复轮）

10. **我不主张 A01 的内容层结论有任何一条是错的。** Round 3 改的是**记账、标签计数与内部一致性**：`100%` → `95.5%`、`10` → `9`、`788+` → `878`、F-12 的幽灵 token、§10.3 的执行状态台账。**F-01…F-35 的 35 条 findings 全部保留，严重度分布 `BLOCKER 3 / MAJOR 12 / MINOR 20` 经 Round 3 机械复算确认原样正确，未改动一条。**
11. **我不主张 878 是「独立来源数」。** 878 是**各 lane 自报数之和**，而 lane 自报数是**各 lane 内去重后**的计数。它与 A04 的 `1,199`（跨文件原始出现次数）、`642`（distinct pointer）、`533`（distinct source）**是四个不同量纲**，互相之间只能算比值，**不能相互校验、不能相互替代**。**`533` 仍是上界估计，本轮未上调也未下调。**
12. **我不主张 21 是「证据等级的准确个数」。** §3.3 的 21 是**本轮正则下界**。哪些 token 是「等级」、哪些是「字段限定符」在本文件与各 lane 中**都未定义**；且本轮**未**统计同一 token 在不同 lane 的定义是否一致（已知 R10/R07 对 `CITED_PRIMARY` 冲突，同类冲突必然还有）。**§3.3 的唯一可用结论是「跨 lane 不可比、不可相加」，这个结论不依赖 12 还是 21。**
13. **我不主张 `EXECUTED = 10` 与 Round 2 的「~13 项」矛盾。** 两者量级一致（10–13），差异来自「真正执行」的阈值判据不同，Round 2 未公开其判据。**我采用更严的判据（缺陷标记必须完全消失），并把 `PARTIAL` 单列。**
14. **我不主张 §10.3.0 的台账可以替代人工判读。** 该台账是**字符串探测**的产物。`PARTIAL` 类的 31 项里，多数是「缺陷标记与修正值并存」，**是否算修完取决于该条目原意要求改什么**。`NR-08-8` / `NR-03-8` / `NR-13-9` 三项被明确标为 `UNPROBEABLE` / 携带指针，正是因为字符串计数对「给全篇补等级」这类动作**没有判据**。
15. **我不主张 §1.1 的 `11` 是错的。** 我把它标为 **`NOT_RECONCILED`** 而非改数：该格描述的是**缺失引用反查步骤**的输出，Round 3 **未重跑该步骤**，因此**没有依据**说 `11` 错。只把它与 §3.1 的 `DEAD_BOTH = 9` 的不一致登记出来（`NR-ALL-7`）。
16. **我不主张 `[ESTABLISHED]` 应当被引入。** §1.4.1 记录了「停止使用」的选择与三条理由。**本文件不使用该标签；本轮也未新增定义。** 这**不是**对「全语料是否该有最高等级」这一问题的裁决——那属 `NR-ALL-1` 的 Architect 裁决范围。
17. **我不主张 A01 对 Fixture 003 有任何权利义务或已履行它。** §1.4.2 的实测结论是：**A01 不使用任何 Fixture 003 单元**（`S\d{3}` 命中 10 次逐条核对全为 Elsevier PII / lane 内编号；`StoryCorps` / `pointer_only` / `HUMAN_REVIEW_REQUIRED` 命中 0 次）。因此**无义务、也无履行**。**其余 21 份报告的 Fixture 003 使用与权利陈述状态不在本 child 白名单内，本轮未审。**

---

## 10. `status_recommendation`

### 10.1 A01 lane 自身

`PARTIAL`

理由：
- 18/18 报告做了全量 DOI 解析 + 标签词频 + 时间敏感性 + 措辞扫描（**广度完整**）
- 承重引用做了语义与数字核对（**深度足够**）
- 但**非 DOI / URL 指针完全未测**（最大缺口），arXiv 只核了 2/40，内容级语义验证只覆盖 9 个数字
- 审计基线在审计期间被并发修改（§2.3），结论的行号锚点会漂移

不是 `BLOCKED`：网络出口对 Crossref / `doi.org` / `arxiv.org/abs` / Google Scholar 均可用，缺口来自我主动的抽样边界与时间预算，不是环境限制。

### 10.2 对 Wave 1 各 lane 状态的影响

**我不建议任何 lane 因 A01 的发现而降级。** 3 条 BLOCKER 全部是**指针层**缺陷（DOI 写错/死链），不是**发现层**缺陷——lane 的分析本身没有被推翻。降级会让 manifest 的状态表失真。

### 10.3 `NARROW_REPAIR_REQUEST`（按 lane 路由，**由 parent 分发，我不自行修复**）

> 全部为**窄修复**：只改指针/题录/标签措辞，**不动任何裁决、结论、参数、schema**。
> 每项都给了实测过的正确值，可直接替换。
>
> **⚠️ Round 3 `A1` 补充：以下 83 项的执行状态台账（见 §10.3.0）。本节各条保留为原始请求文本，未删改。**
>
> **计数说明（避免读者误判为记账错）**：修复前本节共 **83** 项（77 项 lane 路由 + 6 项 `NR-ALL-*`）。§10.3.0 的台账覆盖的正是这**原有 83 项**。**Round 3 新增了 `NR-ALL-7`**（登记 §1.1 那个仍未消解的 `11`），因此**本节现在共有 84 行**（77 + 7）。**`NR-ALL-7` 本身没有执行状态** —— 它是本轮新开的待办，状态为 `NOT_EXECUTED_BY_DEFINITION`。

### 10.3.0 执行状态台账（Round 3 `A1` 实测，2026-09-27）

**为什么需要这张表**：本节列出 **83** 项窄修复请求。Round 2 的证据核查发现**其中只有约 13 项被真正执行**，但原文既没有记录执行了哪 13 项，也没有把「已执行」与「未执行」分开，导致**约 70 项待办持续稀释真正的 blocker**。本节补上这个记账缺口。

**方法（可复跑）**：对每项在**其目标文件的当前状态**上探测两个字符串——(a) 该项所指的**缺陷标记**（错误 DOI / 错误作者 / 错误期刊 / 缺失字段），(b) 该项给出的**修正值**。

| 判定 | 条件 |
|---|---|
| `EXECUTED` | 修正值存在 **且** 缺陷标记已消失 |
| `PARTIAL` | 修正值存在 **但** 缺陷标记仍在（只改了题录的一部分） |
| `NOT_EXECUTED` | 缺陷标记仍在，修正值不存在 |
| `UNPROBEABLE` | 该项是**跨 lane 的流程性动作**（如「统一词表」「每条 lane 加一步 `doi.org` 302 探测」），没有单一字符串特征；任何正则判定都会是编造的，故**明确不给判定** |

#### 计数（Round 3 `A1` 实测，n = 83 = 本节全部条目）

| 状态 | 数 | 占 83 |
|---|---:|---:|
| `EXECUTED` | **10** | 12.0% |
| `PARTIAL` | **31** | 37.3% |
| `NOT_EXECUTED` | **31** | 37.3% |
| `UNPROBEABLE` | **11** | 13.3% |
| **合计** | **83** | 100% |

**与 Round 2 复核口径的差异（记录，不是矛盾）**：Round 2 复核表述为「只有 ~13 项被真正执行」。本轮按上述判据实测得 `EXECUTED = 10`。两者量级一致（10–13），差异来自**「真正执行」的阈值**：Round 2 未公开其判据；若把 `PARTIAL` 中「作者已改对、仅副标题未改」这类（实测仅 `NR-10-2` 一项）计入，则为 11。**本报告采用更严的 `EXECUTED` 判据（缺陷标记必须完全消失），并把 `PARTIAL` 单独列出**，因为 `PARTIAL` 项在引用时仍会传播残留错误。

#### 逐项状态（互斥、穷尽，合计 83）

| 状态 | NR id（实测，无遗漏无重复） | 数 |
|---|---|---:|
| `EXECUTED` | `NR-02-1` `NR-03-1` `NR-03-10` `NR-05-2` `NR-08-1` `NR-08-2` `NR-08-4` `NR-08-7` `NR-10-1` `NR-14-1` | 10 |
| `PARTIAL` | `NR-01-3` `NR-01-4` `NR-02-6` `NR-02-7` `NR-03-5` `NR-03-6` `NR-04-1` `NR-04-2` `NR-05-1` `NR-05-4` `NR-05-5` `NR-08-3` `NR-08-5` `NR-08-6` `NR-08-8` `NR-09-2` `NR-10-2` `NR-10-3` `NR-10-4` `NR-10-5` `NR-11-2` `NR-11-4` `NR-13-1` `NR-13-7` `NR-13-9` `NR-14-3` `NR-14-4` `NR-14-5` `NR-15-1` `NR-17-2` `NR-17-3` | 31 |
| `NOT_EXECUTED` | `NR-01-1` `NR-01-2` `NR-01-5` `NR-02-2` `NR-02-3` `NR-02-4` `NR-02-5` `NR-03-2` `NR-03-3` `NR-03-4` `NR-03-7` `NR-03-9` `NR-05-3` `NR-07-1` `NR-00-1` `NR-11-1` `NR-11-3` `NR-12-1` `NR-13-2` `NR-13-3` `NR-13-4` `NR-13-5` `NR-13-6` `NR-14-2` `NR-14-6` `NR-14-7` `NR-14-8` `NR-17-1` `NR-ALL-3` `NR-ALL-4` `NR-ALL-5` | 31 |
| `UNPROBEABLE` | `NR-02-8` `NR-03-8` `NR-13-8` `NR-14-9` `NR-16-1` `NR-17-4` `NR-09-1` `NR-09-3` `NR-ALL-1` `NR-ALL-2` `NR-ALL-6` | 11 |
| | **合计** | **83** |

**`PARTIAL` 项的残留缺陷定位**（这 31 项不是「做了一半」，而是「修正值已落地一部分、缺陷标记仍在」，引用时仍会传播错误）：

- `NR-01-3` 证据等级表仍指向非 durable 的 `R01_packet.md` · `NR-01-4` `Overall, J. A.` / `Agnew, P. A. M.` 仍在（修正值已另有出现）
- `NR-02-6` `β² = .47` 仍在 · `NR-02-7` `.54` 仍跨行复用
- `NR-03-5` 转述链断裂仍在 · `NR-03-6` `Laurenceau` 仍在
- `NR-04-1` **期刊已改为 *Theory and Decision*，但 `.pdf` 后缀仍在（2 处）** —— 这是本轮唯一确认「改对一半」的 R04 项
- `NR-05-1` / `NR-05-4` / `NR-05-5` `UNKNOWN_AS_OF` 类过度保守声明仍在
- `NR-08-3` `Uuk` 仍在 · `NR-08-5` `Bornstein` 仍在 · `NR-08-6` `Sharon` 仍在（`Bar-Shachar` / `Goodie` / `Borges` 已部分落地）
- `NR-08-8` 61 个 `CITED_PRIMARY` **一个都没降级**（计数前后同为 61）
- `NR-10-2` **作者已改对（`Falconier, M. K., & Kuhn, R. (2019)`），但副标题仍写 "a research agenda"**，真值是 "a **Review of the Empirical Literature**"
- `NR-13-1` / `NR-14-3` / `NR-14-5` / `NR-17-3` / `NR-09-2` / `NR-15-1` / `NR-04-2` / `NR-13-7` / `NR-11-2` / `NR-11-4` / `NR-13-9` / `NR-10-3` / `NR-10-4` / `NR-10-5` / `NR-14-4` —— 缺陷标记与修正值并存，需逐条人工判读
- `NR-17-2` 正确 DOI 已落地，但 R17 原写的另一组题录（`JSPR 30(5), 647–661 (2013), N=1004`）是否已随之更正**未能机械判定**

#### 分类 (i)：零风险、已实测、可直接执行（不依赖任何裁决）

这些项的正确值 A01 当时已**实测过**（Crossref / `doi.org` 逐条确认），修正动作是纯字符串替换，**不需要新的文献核查、不需要 Architect 裁决**。

- **`EXECUTED` 10 项可从待办中移除**：`NR-02-1`（`f6wbn` → `f6wbn_v1`）· `NR-03-1`（`2021-17028-001` → `pas0000986`）· `NR-03-10`（Moyano / Hirsh 年份）· `NR-05-2`（Bumpass + *Journal of Family Issues*）· `NR-08-1`（`0549-8` → `00054-9`）· `NR-08-2`（Audi → Goldberg & Henderson）· `NR-08-4`（Bosson → Lackenbauer）· `NR-08-7`（van Benthem → van Ditmarsch）· `NR-10-1`（`2092623` → `2089716`）· `NR-14-1`（`v35i1` → `v35i7`）
- **`NOT_EXECUTED` 31 项 + `PARTIAL` 31 项 = 62 项仍是可执行待办**（其中 31 项的残留缺陷已定位到行）
- **`UNPROBEABLE` 11 项**不计入本类，因为它们要么是流程性动作（`NR-ALL-1` / `-2` / `-6`），要么在原文中就**自陈为「无需修改」/「不构成通过也不构成不通过」**（`NR-09-1` `NR-09-3` `NR-14-9` `NR-16-1` `NR-17-4`），要么是「给全篇补等级」这类无法用单字符串判定的批量标注（`NR-02-8` `NR-03-8` `NR-13-8`）

#### 分类 (ii)：携带指针的项（**带指针，不得当独立待办执行**）

以下项**本身不是修复动作**，而是「若要动 X，必须同时动 Y」的耦合声明。执行它们需要先决定**是否**动承重来源，**那是 Architect 的裁决，不是 bookkeeping 修复**：

| NR id | 携带的指针 | 为什么不能当独立待办 |
|---|---|---|
| `NR-08-8` | `08b` 的 **61 个** `CITED_PRIMARY` | 降级 61 条等级 = 宣告该 lane 的证据基座整体降级。Round 2 EV2 已实测其中 6 条作者错配。**这会改变 A01 §3.2 的分布表与 `08b` 的 lane 状态。** 实测：`EXECUTED/PARTIAL` 判定为**一个都没降级** |
| `NR-03-8` | `03` 的 **41 个** instrument family / 54 条目 | 同上，且 `03` 是 `F-01`（`X9` / PRI-16）的承重 lane，降级会连带影响 `DIRECT_PROXY` 判定 |
| `NR-13-9` | `13` 的 26 条 DOI | 同上 |
| `NR-14-4` | R14 自称「最高优先 prior-art」的 **Acitelli & Antonioni (2006)** | A01 当时用 Crossref 书目检索**未命中**。**「未命中」不等于「不存在」**（X-14：search-scope claim 不是 field-wide absence claim）。需人工确认，不能由本报告代判 |
| `NR-ALL-1` | 18 lane 的全部等级标签 | 这是**规范化提案**，不是修复。落地会改写 18 份报告的措辞，**必须先有 Architect 裁决**（当前状态 `PROPOSAL_NOT_APPLIED`，见下） |
| `NR-ALL-3` | 审计期间 **198 行**未提交追加（`02b` / `11`） | 依赖「先 commit 或 stash 并由其 owner 说明来源」这一**外部动作**，不在本报告权限内 |
| `NR-ALL-2` | 全 lane 核验流程 | 流程变更，影响后续所有 lane 的产出，不是一次窄修复 |
| `NR-ALL-6` | 4 份报告的头部字段 | 机械但跨 4 个文件，属流程一致性而非单点题录修复 |

#### 分类 (iii)：**接受为已知残余**（不再作为待办稀释 blocker）

以下项**已被显式接受为残余**，它们**不应**继续出现在任何「待修」清单里：

| NR id | 残余类型 | 接受残余的**确切含义** |
|---|---|---|
| `NR-14-4`（Acitelli & Antonioni 2006） | `KNOWN_RESIDUAL` | 存在性 `UNKNOWN`。由 `A04` §10 P0 单点跟踪。**接受残余的含义是：R14 的 prior-art 基座在解决前不得承重** —— 不是「这条可以不管」 |
| `NR-02-8` / `NR-09-2`（`AGENT_RECALL` 格加注） | `ACCEPTED_RESIDUAL / FORMULATION_ONLY` | 各 lane 的降级声明（R01 `:45`、R09 `:18`、R17 `:332`）在**纪律层面已到位**；表格单元格内加注是**表述增强**，不是缺陷闭合。**引用纪律不受影响** |
| `NR-11-4`（de Bel 2019 引摘要原句） | `ACCEPTED_RESIDUAL / OPTIONAL_STRENGTHENING` | 原文自陈「逐字核对通过」，本报告从未主张该 lane 缺证据。这是**可选加强** |
| `NR-09-3` / `NR-04-2` / `NR-15-1` / `NR-13-7` | `NOT_A_DEFECT` | 这四项在原文中就**自陈为「无需修改」/「非 Crossref 注册」/「无 DOI 可核，不构成通过也不构成不通过」**。留在待办表里会虚增待办数 |
| `NR-03-9` / `NR-01-5` | `MERGED_INTO_FINDING` | 这两项的**内容**已分别被 `F-26` / `F-27` 独立记录为 MINOR 措辞问题。`NR` 条目与 findings 行**重复计数**了同一缺陷；合并为单一待办，避免双份 |

#### 本节的记账结论

- **本节原有 83 项中，真正闭合的只有 10 项**（12.0%）。
- **31 项完全未执行、31 项部分执行、11 项无法机械判定。**
- **承接本轮 Round 3 派发的是 bookkeeping 与引用修复；执行这 70 余项 lane 内窄修是 Track R3-A3（lane-specific research repair）的职责，不在本 child 的白名单内。** 本节的唯一交付是**这张状态表**——它让下游能区分「已闭合」「部分闭合」「必须先裁决」三类，从而不再把全部 83 项当作同等重量的待办。
- **本节未删改任何一条原始 `NR` 文本**，以保留 A01 当时的判断与证据链。

---#### → `R01`（`02_CONSTRUCT_CONVERGENCE.md`）

| ID | 位置 | 动作 |
|---|---|---|
| **NR-01-1** | `:484` | `10.1111/spc3.12308` 的作者改为 **Reis, H. T., Lemay, E. P., & Finkenauer, C. (2017). Toward understanding understanding… *Social and Personality Psychology Compass***。**移除该行的 ✓**（自标已核验但错）。 |
| **NR-01-2** | `:465` | `10.1111/j.1467-8721.2009.01621.x` 的作者改为 **Roisman, G. I. (2009). Adult Attachment. *Current Directions in Psychological Science***。**移除 ✓**。**并与 `14:70` 统一题录**（两 lane 现给同一 DOI 两种题录）。 |
| **NR-01-3** | `:503` | 把证据等级表**写入 durable 报告**（当前指向非 durable 的 `R01_packet.md` §2）。这是 manifest "45 条带 DOI 指针" 可审计的前提。 |
| **NR-01-4** | `:488`、`:447` | 作者名修正：**Overall, N. C.**（非 J. A.）；**Agnew, C. R.**（非 P. A. M.）。 |
| **NR-01-5** | `:173`、`:221`、`:222`、`:238`、`:403`、§5 | 5 处绝对否定（「不存在一个被广泛接受…」「关系级无被广泛接受…」「所有『跨形态稳定性』判断」）加「**在本次检索覆盖范围内未找到**」限定，与 R12 `:416` 的 `NEGATIVE ≠ DISPROVEN` 纪律对齐。 |

#### → `R02`（`02b_CONSTRUCT_REDUNDANCY_AUDIT.md`）

| ID | 位置 | 动作 |
|---|---|---|
| **NR-02-1** | `:596` | 预印本 DOI 改为 **`10.31234/osf.io/f6wbn_v1`**（补 `_v1`）。同时给 `10.1111/jftr.70019` 补作者 **Junkins, Derringer, Ogolsky, Hardesty & Weisberg (2025)**。 |
| **NR-02-2** | `:576` | `10.1177/0265407518822783` → **Coy, A. E., Davis, J. L., Green, J. D., & Etcheverry, P. E. (2019). *JSPR***。 |
| **NR-02-3** | `:577` | `10.1002/ejsp.1926` → **Macher, S. (2012). *EJSP***。 |
| **NR-02-4** | `:589` | `10.1111/j.1475-6811.1997.tb00145.x` → **Lamm, H., & Wiesmann, U. (1997). *PR***。 |
| **NR-02-5** | `:430` / `:598` | `10.1111/joop.12395` → **Gottfredson, R. K., Wright, S. L., & Heaphy, E. D. (2022). *JOOP***；与它并列的 "Zanella Delatorre & Wagner 2020" 是**另一篇**，需分开或删除。 |
| **NR-02-6** | `:286` | `R²=.54` 保留；**`95% CI [.53,.55]` 与 `β²=.47/.32/−.19` 降级为 `CITED_SECONDARY` 并注明"未在摘要层核对，需页码/表号"**。 |
| **NR-02-7** | `:166` / `:320` | 拆表或加表头注：`.54` 只属 investment-model 三行，不覆盖 `actual similarity ↔ attraction` 行。 |
| **NR-02-8** | `:137` / `:149` / `:185` | 三处 `AGENT_RECALL` 格（PLS、目标特异欲望工具、RSQ）加一句"本格不可作为证据"。 |

#### → `R03`（`03_MEASUREMENT_INSTRUMENTS.md`）

| ID | 位置 | 动作 |
|---|---|---|
| **NR-03-1** ⚠ | `:146`、`:336` | `10.1037/2021-17028-001` → **`10.1037/pas0000986`**（可选补 `10.1037/t79142-000` PsycTests）。**在修好之前，`X9` 行的 `DIRECT_PROXY` 判定与全部信效度数字应标 `UNVERIFIED`。** |
| **NR-03-2** ⚠ | `:130` | 「38 个…无一成为主流工具」改为 **R10 `:360-364` 的原句转述**：「There were no established scales used repeatedly that were developed specifically with power bases in mind」+「the measures were focused on White, younger, and heterosexual men and women in shorter-length relationships」。**同时删掉 `38`（来源报告 k=319），并与 `:131`（SRPS 是最常用性权力工具）消除矛盾。** |
| **NR-03-3** | `:125` | `10.1111/pere.12072` → **Farrell, A. K., Simpson, J. A., & Rothman, A. J. (2015)**。 |
| **NR-03-4** | `:126` | `10.1007/s10591-017-9421-2` → **Luttrell, T. B., Distelberg, B., Wilson, C., Knudson-Martin, C., et al. (2017)**。 |
| **NR-03-5** | `:64` | `10.1007/s13178-024-01040-0` 归 Ballester-Arnal et al. (2024) **ASEX 跨文化验证**，不含 Clayton/DSDS。**转述链断裂**：改标 `TRANSITIVE_UNVERIFIED` 或另给 Clayton et al. (2009) 的真实 DOI（*J Sex Med*）。 |
| **NR-03-6** | `:96` | `10.1037/0022-3514.73.6.1409` → **Pietromonaco, P. R., & Barrett, L. F. (1997)**（去 "Laurenceau"）。 |
| **NR-03-7** | `:145` | 「Mønster et al. (2016)」→ **Palumbo, R. V., Marraccini, M. E., Weyandt, L. L., Wilder-Smith, O., et al. (2016), *PSPR***。并把 `10.1038/s44159-026-00535-4` 的年份从"未标"补为 **2026**（Gordon & Bartsch, *Nature Reviews Psychology*）。 |
| **NR-03-8** ⚠ | 全篇 | **给 41 个 instrument family 的信效度数字补证据等级。** 当前 `CITED_PRIMARY` = 0（§3.2）。最小改法：每个 family 的来源格加 `CITED_PRIMARY / CITED_SECONDARY / UNVERIFIED`。 |
| **NR-03-9** | `:234` | 「完全无不变性证据」改为「本 lane 未检索到」+ 挂检索日志（库/关键词/日期）。 |
| **NR-03-10** | `:58`、`:128` | 年份 ±1（Moyano 2017→2016；Hirsh 1976→**Hirschfeld** et al. 1977）。 |

#### → `R05`（`05_IDENTIFICATION_AND_STATISTICS.md`）

| ID | 位置 | 动作 |
|---|---|---|
| **NR-05-1** | `:539` | `10.3102/10769986024002179` 是 **Vermunt, Langeheine & Bockenholt (1999), *JEBS***，不是 Hoffmann et al. (1985)。**把 `UNKNOWN_AS_OF` 改为"指针错误"**，另给 Hoffmann 1985 的真实出处或删除。 |
| **NR-05-2** | `:572` | `10.1177/019251391012001003` = **Bumpass, Martin & Sweet (1991), *Journal of Family Issues***（不是 *JMF*）。补作者，改正期刊。 |
| **NR-05-3** | `:516` | `10.1111/cdev.12660` → **Berry, D., & Willoughby, M. T. (2017)**（不是 Allison 2021）。 |
| **NR-05-4** | `:546` | `10.1026/0932-4089/a000478` 的 Crossref 年份是 **2026**（Sonnentag, Neumer, Partsch & Völker）。把 `年份 UNKNOWN_AS_OF` 改为 2026。 |
| **NR-05-5** | 头部 | 补 `As of` 字段（实际已有 `核实日期 2026-09-26/27`，但**未在头部**）。 |

#### → `R08b`（`08b_BELIEF_DECEPTION_KNOWLEDGE.md`）

| ID | 位置 | 动作 |
|---|---|---|
| **NR-08-1** | `:774` | `10.1016/S0010-0277(02)0549-8` → **`10.1016/s0010-0277(02)00054-9`**（Hedden & Zhang 2002, *Cognition*）。 |
| **NR-08-2** | `:810` | `10.1111/j.1933-1592.2006.tb00586.x` → **Goldberg, S., & Henderson, D. (2006), *Philosophy and Phenomenological Research***（不是 Audi, *Mind*）。 |
| **NR-08-3** | `:800` | `10.1177/02654075211017675` → **Bar-Shachar, Y., & Bar-Kalifa, E. (2021), *JSPR***（不是 Uuk et al., *JPSP*）。 |
| **NR-08-4** | `:791` | `10.1111/j.1475-6811.2010.01282.x` → **Lackenbauer, Campbell, Rubin, Fletcher, Tomlinson, Eastwick et al. (2010)**（不是 Bosson）。 |
| **NR-08-5** | `:777` | `10.1002/bdm.717` → **Goodie, Doshi & Young (2010), *British Journal of Developmental…*→ 实为 *J. Behavioral Decision Making***（不是 Bornstein, *BJDP*）。 |
| **NR-08-6** | `:752` | `10.1007/s11229-015-0715-3` → **Borges, R. (2015)**（不是 Sharon）。 |
| **NR-08-7** | `:742` | `10.1007/978-1-4020-5839-4` → **van Ditmarsch, H., van der Hoek, W., & Kooi, B. (2010). *Dynamic Epistemic Logic*, Synthese Library 337**（不是 van Benthem）。 |
| **NR-08-8** ⚠ | 全篇 | **61 个 `CITED_PRIMARY` 需要降级复核。** 在其中 6 条已被我实测为作者错配（NR-08-2…7）的情况下，该 lane 的 `CITED_PRIMARY` 不能按面值使用。最小改法：把未能出示"我打开了哪一页"的条目降为 `CITED_SECONDARY`，或为每条补一个具体的页/段锚点。 |

#### → `R10`（`10_MUTUALITY_POWER_DEPENDENCE.md`）

| ID | 位置 | 动作 |
|---|---|---|
| **NR-10-1** ⚠ | `:804` | `10.2307/2092623` → **`10.2307/2089716`**（Emerson 1962, *ASR* 27(3):31–41）。`10.2307/2092623` 是 **Gouldner 1960**。 |
| **NR-10-2** ⚠ | `:786` / `:461` | `10.3389/fpsyg.2019.00571` → **Falconier, M. K., & Kuhn, R. (2019). "…A Conceptual Integration and a **Review of the Empirical Literature**"**（不是 Lehne & Bodenmann）。「139 项研究」需按该文正文复核。 |
| **NR-10-3** | `:757` | 删除 `CITED_PRIMARY` 定义中的「**出版元数据**」——这与 R07 的 `CITED_METADATA` 分级直接冲突（见 NR-ALL-1）。 |
| **NR-10-4** | `:767` | Bodenmann 2011 标题改为 "…potential for predicting **Relationship Satisfaction**"；补 DOI `10.1027/1016-9040/a000068`。 |
| **NR-10-5** | `:360` | 「(2025/2026, JFTR 18, 170–191)」→ Crossref 年份为 **2025**，请统一。 |

#### → `R11`（`11_GENERAL_HUMAN_DYADS_SCOPE.md`）

| ID | 位置 | 动作 |
|---|---|---|
| **NR-11-1** | `:502` | `10.1024/1662-9647.a000031` → **`10.1024/1662-9647/a000031`**（斜杠）；作者改为 **Di Rosa, M., Kofahl, C., McKee, K., Bień, B., et al. (2011)**, *GeroPsych* 24(1)（不是 Geyer 1999）。 |
| **NR-11-2** | `:506` / `:509` | `10.3389/fpsyg.2011.00270/full` → **`10.3389/fpsyg.2011.00270`**（去掉 `/full`）。 |
| **NR-11-3** | `:130` / `:132` | `10.1177/0003122417715051` 保留为「检索未命中」记录，但**不要写成 DOI 形式**（改成 `DOI_UNKNOWN_AS_OF_2026-09-27`）。 |
| **NR-11-4** | `:149` | de Bel 2019 逐字核对通过，建议在条目内直接引摘要原句（"549 sibling–parent–sibling triads from the Netherlands Kinship Panel"），使 N 与人口学自证。 |

#### → `R12`（`12_COMPUTATIONAL_MODELS_ABM.md`）

| ID | 位置 | 动作 |
|---|---|---|
| **NR-12-1** | `:491` | `10.4324/9780203848852.ch17` 的书名改为 ***Handbook of Advanced Multilevel Analysis*** ch.17（不是 *Handbook of Multilevel Models*）。 |

#### → `R13`（`13_LLM_SKILL_INTERVIEW_LAYER.md`）

| ID | 位置 | 动作 |
|---|---|---|
| **NR-13-1** | `:306` | 「跨 Google / Anthropic / Meta」→ 补 **OpenAI**（原文是 four provider families）。style bias 的对比对象是 **position bias**，verbosity bias 原文单列为"异质"而非"更小"。 |
| **NR-13-2** | `:306` | **补权威等级**：`arXiv:2604.23178` 已发表于 **TMLR (2026)**，不再是纯预印本。 |
| **NR-13-3** | `:133` | `arXiv:2603.22735` 补题录：Chan, J., Zhao, Z., & Gaizauskas, R. (2026)，Preprint（非 TMLR）。"gpt-5.2 的实例"与 "considering potentially relevant but unstated contexts" 引号内容**我未在摘要层核实**，若不能出示页码请降级。 |
| **NR-13-4** | `:687` | `10.1145/3703155` venue → ***ACM Transactions on Information Systems***，年 → **2025**。 |
| **NR-13-5** | `:682` | `10.2478/jos-2022-0041` venue → ***Journal of Official Statistics***，作者 **Yan, T., & Williams, D.**。 |
| **NR-13-6** | `:695` | `10.21248/jlcl.38.2025.289` 第一作者是 **Münker, Simon**（不是 "Li, D., et al."）。 |
| **NR-13-7** | `:720` | `10.12758/mda.2013.013` **有效**（GESIS 自建注册，`doi.org` 302 → mda.gesis.org），无需改 DOI；建议在 lane 内注明"非 Crossref 注册"。 |
| **NR-13-8** | 全篇 | **模型版本类主张逐条加 `as of 2026-09-27`**（当前全文只出现 1 次日期）。 |
| **NR-13-9** | 全篇 | `CITED_PRIMARY` = 2 / `CITED_SECONDARY` = 1 / DOI token = 26。**给承重的 26 条补证据等级。** |

#### → `R14`（`14_PAPER_POSITIONING_NOVELTY.md`）

| ID | 位置 | 动作 |
|---|---|---|
| **NR-14-1** ⚠ | `:98` / `:400` | `10.1609/aaai.v35i1.16792` → **`10.1609/aaai.v35i7.16792`**（i7）。作者 Hwang et al. 正确。「12 个百分点 / 430×」需给 ATOMIC 2020 正文页码。 |
| **NR-14-2** ⚠ | `:63` | `10.1111/1475-6811.00017` → **Hassebrauck, M., & Fehr, B. (2002)**（不是 Neubauer, Voss & Asendorpf 2015）。四维内容（intimacy/agreement/independence/sexularity、德加复本、intimacy 最大）**与摘要一致，可保留**。 |
| **NR-14-3** | `:70` | 与 R01 `:465` 统一 `10.1111/j.1467-8721.2009.01621.x` 的题录（见 NR-01-2）。 |
| **NR-14-4** | `:71` / `:409` | **Acitelli & Antonioni 的真实存在性与 DOI 需要人工确认**（我用 Crossref 书目检索未命中）。这是 R14 自称"最高优先 prior-art"。 |
| **NR-14-5** | `:20` / `:73` | 两处绝对否定加检索范围限定（见 F-27）。**注意 R14 自己在 `:167` F-4 已写出正确措辞（"从未 head-to-head"），照它自己的标准改即可。** |
| **NR-14-6** | `:336` | `10.1007/s12144-025-08223-x` → **Morales-Vives, Ferre-Rey & Ferrando (2025), *Current Psychology***（不是 Masopustová et al., *Journal of Individual Differences*）。 |
| **NR-14-7** | `:367` | `10.3389/fpsyg.2014.00452` → **Kyselo, M., & Tschacher, W. (2014)**（不是 de Haan, Thompson & Vogeley）。 |
| **NR-14-8** | `:368` / `:374` | `10.1177/0265407500173006` → **Weigel & Murray (2000)**；`10.1177/1059712314547709` → **Mudimu, E., & Engelbrecht, G. (2014)**。 |
| **NR-14-9** | 头部 | 补 `As of` 字段。 |

#### → `R16`（`16_EMPIRICAL_VALIDATION_PROTOCOL.md`）

| ID | 位置 | 动作 |
|---|---|---|
| **NR-16-1** | 头部 | 补 `As of` 字段（`00_CHILD_CONTRACT.md:29` 要求）。 |

#### → `R17`（`17_RED_TEAM_FALSIFIERS.md`）

| ID | 位置 | 动作 |
|---|---|---|
| **NR-17-1** | `:512` / `:592` | `10.1613/jair.3600` **保持弃用**（处理正确）。仅把字面 `10.1177/…` 改成 `DOI_UNKNOWN_AS_OF_2026-09-27` 形式，避免被下游当 DOI 解析。 |
| **NR-17-2** | `:181` | `10.1177/0265407512465221` 解析为 **MacDonald, Locke, Spielmann & Joel (2012), *JSPR*, "Insecure attachment predicts ambivalent social threat and reward perceptions in romantic relationships"**——与 R17 写的 "JSPR 30(5), 647–661 (2013), N=1004" 不是同一篇。**`S5` 承载 A9 的 CHALLENGED 裁定，需换正确指针或降级。** |
| **NR-17-3** | `:280` | `10.1177/0192513X18758343` 年份 2019 → **2018**（Crossref）。 |
| **NR-17-4** | 头部 | 补 `As of` 字段。 |

#### → `R09`

| ID | 位置 | 动作 |
|---|---|---|
| **NR-09-1** | 头部 | 补 `As of` 字段。 |
| **NR-09-2** | `:406` | Peterman (1963) 的作者/卷期仍 `AGENT_RECALL`；该格被用作 hysteresis 存在性的"经典展示"。加"本格不可作为证据"注。 |
| **NR-09-3** | — | **无需修改。** Liddell & Kruschke 的 `100%` 断言、期刊列表、"无可靠事后检出办法"、"取平均不能修复" **全部与摘要逐字一致**，包括 "that analyzed ordinal data" 这一关键限定。这是全 swarm 核验质量最高的一处。 |

#### → `R04`

| ID | 位置 | 动作 |
|---|---|---|
| **NR-04-1** | `:585` / `:1012` | 去掉 `.pdf` 后缀（`10.1007/s11238-014-9448-x`）；期刊改为 ***Theory and Decision***（不是 *J Behav Dec Making*）；作者 Bacon, Conte & Moffatt (2014)。 |
| **NR-04-2** | — | **`10.4232/pairfam.5678.14.2.0` 与 `10.6103/SHARE.w1.900` / `w8.900` 全部有效**（DataCite 注册，`doi.org` 302 → gesis ZA5678 / share-eric.eu）。**建议在 lane 内注明"非 Crossref"，避免下一轮审计误判为死链。** 版本号（14.2 / 9.0.0）A01 未核。 |

#### → `R15`

| ID | 位置 | 动作 |
|---|---|---|
| **NR-15-1** | — | **无 DOI 可核**（该报告 0 个 DOI token）。`UNVERIFIED_CANDIDATE` 的 7 条来源 A01 未测（§2.2 第 1 条）。**不构成通过，也不构成不通过。** |

#### → `R07`

| ID | 位置 | 动作 |
|---|---|---|
| **NR-07-1** | `:551` | `10.2307/2265159` 双 404。R07 已正确标 `[UNVERIFIED]` + "未用于任何主张"；**仅需清掉指针或标注 `DOI_UNRESOLVABLE_AS_OF_2026-09-27`**。 |

#### → `R00`

| ID | 位置 | 动作 |
|---|---|---|
| **NR-00-1** | `:338` | `10.1002/per.2410050503` = **Wiggins, J. S., & Broughton, R. (1991), "A geometric taxonomy of personality scales", *European Journal of Personality***——是 Interpersonal Circumplex 的**分类学前身**，不是 IPC 本身。IPC 的常引来源是 Wiggins, Broughton & Broughton (1998) *JPSP*。**建议把 review 指针 `10.1002/9781118001868.ch4`（Fournier, Moskowitz & Zuroff 2010，"Origins and Applications of the Interpersonal Circumplex" ✓ 正确）提为主指针。** |

#### → 全局（`parent` / Architect）

| ID | 动作 |
|---|---|
| **NR-ALL-1** ⚠ | **统一证据等级词表｜状态 `PROPOSAL_NOT_APPLIED`。** 现状见 §3.3 实测台账：**F-12 枚举 12 个变体，其中 11 个实测存在（`UNVERIFIED_AGENT_RECALL` 为幽灵 token），另有 9 个 F-12 未枚举的写法，实测 tier 形态 token 合计 21**。且 R10 与 R07 对 `CITED_PRIMARY` 的定义直接冲突。**以下 5 级方案是本审计的提案，不是已实施的规范化，任何 lane 都尚未采用**：建议固定 5 级：`CITED_PRIMARY`（读到原文/官方文档正文）· `CITED_ABSTRACT`（只读到出版方摘要）· `CITED_METADATA`（只核到 Crossref/DataCite 元数据）· `CITED_SECONDARY`（转述）· `UNVERIFIED`（含 `AGENT_RECALL`）。所有 lane 改用同一张表，**并且每个级别必须回答"我打开了哪一页"**。<br>**⚠️ 落地前置条件（Round 3 `A1` 记录）**：本条会改写 18 份报告的措辞，**必须先有 Architect 裁决**；且 §3.3 已实测出 9 个 F-12 未枚举的写法，**它们各自的落位在提案里没有对应项**（例：`UNVERIFIED_VOL_PAGES` 是等级还是字段限定符？`CITED_PRIMARY_SECONDARY` 这种合并写法归哪一级？）。**在这两点解决前，本条不得被当作可直接执行的待办。** |
| **NR-ALL-2** ⚠ | **在所有 lane 的核验流程里加一步 `doi.org` 302 探测。** 本次这一步救回 5 条有效指针（`10.12758/...`、`10.13718/...`、`10.4232/...`、`10.6103/SHARE.w1.900`、`10.6103/SHARE.w8.900`），并把"Crossref 无记录"与"真死链"区分开。 |
| **NR-ALL-3** ⚠ | **冻结 corpus。** §2.3：Wave 1 报告在 A01 审计期间仍被并发修改——`00_MANIFEST.md` 声称的终态 commit `2d392ba` 已产生，但 `02b_CONSTRUCT_REDUNDANCY_AUDIT.md` 与 `11_GENERAL_HUMAN_DYADS_SCOPE.md` 在工作区还有 **198 行未提交追加**（`git diff --stat`）。**在按本报告行号路由 NR 之前必须先 commit 或 stash 这 198 行，并请其 owner 说明来源**；否则 §5 中所有指向 `02b_*` 与 `11_*` 的行号都可能已被推移。 |
| **NR-ALL-4** | **修 `00_MANIFEST.md` 的 3 处**（本报告只报不改）：`:49` Sibley 2012 → **Sibley 2005**；`:53` 列出 R08 核心指针 "QSR/Renz 2007" 与 R07 `:551` 的 Belnap 1976 对不上；`:85` 的逐 lane 计数**不可相加**（B-3 已声明，保留），并补一句"实测唯一 DOI 353 个，含 29 条书目错配"。 |
| **NR-ALL-5** | **`00_MANIFEST.md` §3 的"150+ 独立来源"目标。** 我实测唯一 DOI 353 个，manifest 逐 lane 相加 **878**。<br>**`SUPERSEDED`（Round 3 `A1` 实测重算）**：本条原文写「manifest 逐 lane 相加 **788+**」——**该数算术不成立**，真值 **878**（`+` 项按下界计 = 875；`41+3` 记作 44 = 878）。差额来自非 DOI 指针与跨 lane 重复。**在 A04 完成全局去重前，不得对外声称 150+ 独立来源**（B-3 已声明，保留并强化）。 |
| **NR-ALL-6** | 4 份报告（`09` / `14` / `16` / `17`）补 `As of` 头部字段（F-29）。`00_CHILD_CONTRACT.md:29` 是硬要求。 |
| **NR-ALL-7** ⚠ | **（Round 3 `A1` 新增）消解 A01 内部四个互斥的「未命中」数。** §0 与 §1.1 现给出 `10`（已订正为 9）/ `11` / `16` / `9` 四个数。Round 3 已把 `10` 订正为 `9`（与 tier 表自洽），`16` 与 `9` 已在 §1.1 写清构成（16 = 9 死链 + 5 DataCite + 1 `.pdf` 格式错 + 1 字面占位符），**但 §1.1「11 条死链」仍未消解** —— 该数对应的是**缺失引用反查步骤**的输出，本轮**未重跑该步骤**，因此**不擅自改数**。**需要的动作**：重跑 Crossref `query.bibliographic` 反查，给出该步骤的输入集合定义，才能确定 `11` 是否包含那 2 个非死链项。**在消解前，§1.1 该格的 `11` 应读作 `NOT_RECONCILED`。** |

---

## 11. 正面发现（应当保留的具体做法）

审计报告如果只有缺陷清单会误导 parent。以下 6 项是**实测确认做得对**的做法，repair 时**不要顺手改掉**：

1. **R17 的 `FETCH_FAILED` 纪律。** 3 条检索未命中的引用全部显式登记、明确写"不用它证明 Y"、并把承重裁定改由其他来源承担（F-24）。我独立用 Crossref 检索复现了同样的未命中。
2. **R09 的 Liddell & Kruschke 转述。** `100%` 断言、期刊列表、"无可靠事后检出办法"、"取平均不能修复" **与摘要逐字一致**，且保留了 "that analyzed ordinal data" 这个决定性的限定词（F-33 之外，单独记为正面）。
3. **R10 对 Junkins et al. (2025) 的逐字引用**（`:360-364`），包括人口学限定（White / younger / heterosexual / shorter-length）。**同一来源 R03 `:130` 把它改写坏了**——对比之下 R10 是正确示范。
4. **R02b / R12 的 `NEGATIVE` 措辞。** R12 `:416`「不主张…已被证明『不存在』——只主张本次在指定渠道内未能核实（`NEGATIVE`，非 `DISPROVEN`）」；R02b `:546` 逐条列"不主张什么"。这是负结果该有的写法。
5. **`AGENT_RECALL` 的显式降级声明。** R01 `:45`「不得作为裁决依据」· R09 `:18`「只用于举例或线索，不用于判定」· R17 `:332`「不承重」· R12 `:9` / R13 `:16` / R05 `:10` 各有分级约定。**问题不是用了 `AGENT_RECALL`，是它出现在承重格子里**（F-28 / F-34）。
6. **R04 / R15 对不可达源的诚实处理。** `FETCH_FAILED` 逐条登记（`FETCH_FAILED` 计数：R04 = 4，R15 = 17 `UNVERIFIED*`），并明确写"不得主张该数据存在""不得填充"。`00_MANIFEST.md` §4 B-1 也把网络出口限制**如实标为 parent 无法修复**，而不是悄悄降低目标。

---

## 12. 引用与工具清单

**审计所用工具/端点（全部为只读 GET/HEAD，2026-09-27）**

- `https://api.crossref.org/works/<DOI>` — DOI 元数据（title / author / issued / container-title / abstract / type / publisher）
- `https://doi.org/<DOI>`（HEAD，禁跟随重定向）— 解析存在性 + 重定向目标 + 注册机构
- `https://arxiv.org/abs/<id>` — 预印本存在性与摘要
- Crossref REST `query.bibliographic` — 缺失引用的反查

**审计产物（临时目录，不在 repo 内）**

- `snapshot/` + `_manifest.json` — 20 文件只读副本与 SHA-256
- `a01_occ.csv` — 588 处 DOI 出现（file / line / raw / normalized）
- `a01_cr.csv` — 353 个 DOI 的 Crossref 元数据
- `a01_cmp.csv` — DOI ↔ 引用行 ↔ Crossref 的自动比对结果
- `verified_dois.md` — §6 的表格源

**未使用的**：任何 GitHub 写操作；任何需要 auth 的端点；任何受限数据下载。

---

## 13. Round 3 `A1` 的复算脚本与逐项输出（可复跑）

Round 3 派发的硬要求：「**重新机械计数；绝不复制旧总数。**」本节给出本 child 用来产生 §0 / §3.3 / §10.3.0 全部新数字的脚本与原始输出。**所有数字都由下列脚本实测产生，没有任何一处沿用旧总数。**

### 13.1 lane 自报数求和（产出 F-35 / NR-ALL-5 / `A04` §2.1–2.3 的修正值）

**脚本**：`C:\Users\gg828\AppData\Local\Temp\opencode\a1_lane_sum.py`
**命令**：`python C:\Users\gg828\AppData\Local\Temp\opencode\a1_lane_sum.py`

**方法**：正则定位 18 份 lane 报告中**携带完整 18-lane 清单**的行（命中 2 行：`A01` 的 F-35 行与 `A04` 的 §2.1 行）。**修复前行号分别为 `A01:267` 与 `A04:84`；因 Round 3 在两处之前插入了新章节，修复后分别为 `A01:369` 与 `A04:105`。** 逐项解析 `R<nn> <数字>`（允许 markdown 强调 `**45**`）与 `+` 尾注，逐项求和。

**实测输出（逐字）**：

```
A01_EVIDENCE_QUALITY_AUDIT.md:369   lanes parsed = 18
  R00=30+ · R01=45 · R02=34 · R03=41 · R04=16 · R05=109 · R06=33 · R07=33 · R08=72 ·
  R09=78 · R10=59 · R11=60+ · R12=40 · R13=70 · R14=60+ · R15=30 · R16=24 · R17=41+3
  SUM lower-bound ("+" at lower bound, 41+3 -> 41) = 875
  SUM 41+3 recorded as 44                          = 878
  "+" items: {R00:(30,'+'), R11:(60,'+'), R14:(60,'+'), R17:(41,'+3')}

  lower=875   / 533  = 1.6417  ->  1.64x   (533 distinct source)         diff +342
  lower=875   / 350  = 2.5000  ->  2.50x   (350 peer-reviewed)            diff +525
  lower=875   / 642  = 1.3629  ->  1.36x   (642 distinct pointer)         diff +233
  lower=875   / 1199 = 0.7298  ->  0.73x   (1199 raw occurrences)         diff -324
  41+3=44     / 533  = 1.6473  ->  1.65x   (533 distinct source)         diff +345
  41+3=44     / 350  = 2.5086  ->  2.51x   (350 peer-reviewed)            diff +528
  41+3=44     / 642  = 1.3676  ->  1.37x   (642 distinct pointer)         diff +236
  41+3=44     / 1199 = 0.7323  ->  0.73x   (1199 raw occurrences)         diff -321
  41+3=44     / 1201 = 0.7311  ->  0.73x   (1201 old A04 claim)           diff -323
  41+3=44     / 788  = 1.1142  ->  1.11x   (788+ old A01 claim)           diff  +90

A04_CITATION_PROVENANCE_AUDIT.md:105   lanes parsed = 18   (per-lane numbers IDENTICAL, 0 mismatches)
  A01 sum(lower)=875   A04 sum(lower)=875   delta=+0
```

**结论（本 child 独立算得，与 `EV2` §4.1 一致）**：
- 两份文件列出的是**同一串 18 个数，逐 lane 无一处不符**（脚本显式做了跨文件比对：`MISMATCHES: none`）。
- 和 = **875**（`+` 项按下界）= **878**（`41+3` 记作 44）。
- 真倍率：**878 / 533 = 1.65×**、**878 / 350 = 2.51×**。
- **878 − 1199 = −321**；**878 − 1201 = −323**。旧数 `1,201` 与实测和**差 −323，不是「差 2」**。
- **旧数 `788` 与实测和差 +90，任何读法都得不到 `788`。**
- 三个 `+` 项（`R00 30+` / `R11 60+` / `R14 60+`）按下界合计 **150**；即便全部按上界补满，也远不足以把 875 抬到 1,201。**旧数 `1,201` 在任何读法下都不可辩护。**

### 13.2 证据等级词汇台账（产出 §3.3）

**命令**：对 18 份 Wave 1 lane 报告全文跑
`\b(?:CITED|UNVERIFIED|AGENT|NO_DOI|SUBSTANCE|POINTER|NOT_VERIFIED)[A-Z_]*\b`，
按 token 去重计数；对 F-12 枚举的 12 个 token 另用 `(?<![A-Z_])TOKEN(?![A-Z_])` 精确计数并记录出现 lane。

**实测结果**：`F-12` 的 12 个 token 中 **11 个存在、1 个（`UNVERIFIED_AGENT_RECALL`）命中 0 次**；另有 **9 个** tier 形态写法未被 F-12 枚举；连同裸 `UNVERIFIED` 共 **21** 个。`R11` 全文 `AGENT_RECALL` 命中 **0** 次。逐 token 计数与出现 lane 见 §3.3 表 A / 表 B。

### 13.3 `NARROW_REPAIR_REQUEST` 执行状态（产出 §10.3.0）

**脚本**：`C:\Users\gg828\AppData\Local\Temp\opencode\a1_nr_ledger.py`
**命令**：`python C:\Users\gg828\AppData\Local\Temp\opencode\a1_nr_ledger.py`
**原始输出留存**：`a1_nr_ledger_out.txt`

**方法与判据**：对 §10.3 的 83 项，每项在**其目标文件的当前状态**上探测两个字符串——缺陷标记与修正值。判据 `EXECUTED` = 修正值在 ∧ 缺陷标记不在；`PARTIAL` = 修正值在 ∧ 缺陷标记仍在；`NOT_EXECUTED` = 缺陷标记在 ∧ 修正值不在；`UNPROBEABLE` = 该项无单一字符串特征（跨 lane 流程动作，或原文自陈「无需修改」），**明确不给判定**。

**探测器的两处已知假阳性（已修正，记录在此以免下游复用出错版本）**：
1. 首版把「缺陷 DOI」当探测键，误判了 5 项**缺陷在作者归属、DOI 本身正确**的条目（`NR-08-3` / `-5` / `-6` / `NR-05-2` / `NR-04-1`）。已改为探测**错误作者名 / 错误期刊名**。修正后 `NR-05-2` 由 `NOT_EXECUTED` 升为 `EXECUTED`（`:572` 现为 `Bumpass, L. L., Martin, T. C., & Sweet, J. A. (1991) … *Journal of Family Issues*`，`JMF` 全文命中 0）。
2. 首版把 `NR-04-1` 的修正值正则写成 `s11238-014-9448-x`，它**同时匹配**缺陷形态 `…-9448-x.pdf`，导致 `PARTIAL` 恒成立。已改为负向断言 `(?!\.pdf)`。修正后 `NR-04-1` = `PARTIAL`（期刊已改对、`.pdf` 后缀仍在 2 处）。

**实测输出（末 5 行，逐字）**：

```
TOTAL ITEMS PROBED : 83
  NOT_EXECUTED      31
  PARTIAL           31
  UNPROBEABLE       11
  EXECUTED          10
```

### 13.4 Crossref 复验（产出 `A04` §4.2 的作者修正与 M-8 / M-9 的裁定）

**脚本**：`C:\Users\gg828\AppData\Local\Temp\opencode\a1_crossref.py`
**命令**：`python C:\Users\gg828\AppData\Local\Temp\opencode\a1_crossref.py`
**原始输出留存**：`a1_crossref_out.txt`

**范围限定**：只查**本 child 实际改动或需要裁定的那 33 个 DOI**（`A04` §4.2 承重表的 30 个 DOI + 三个未改动行的守卫对照 + M-8 / M-9 两条）。**未做新的文献扫描**（Round 3 派发禁止）。UA `LHRM-R3A1-Repair/1.0`，端点 `https://api.crossref.org/works/<DOI>`，只读 GET。

**守卫对照的作用**：12 个被判定为**正确**的行（Rusbult 1998 / Laurenceau 1998 / Le & Agnew 2003 / Tran 2019 / Joel 2020 / Aron 1992 / Keltner 2003 / Hamaker & Grasman 2015 / Lucas 2023 / Malloy & Kenny 1986 / Gable 2004 / Liell-Cock & Staton 2025）被**一并复查以防误改**，实测全部与 `A04` 原文一致，**未改动**。详见 `A04` §4.2.1。

**本 child 独立发现（不在 `EV2` packet 中）**：`A04` §4.2 第 15 行 `Robitzsch 2025` 的 Crossref `issued` 年份是 **2024**（*Structural Equation Modeling* 32(1):36–45）。已修正并在 `A04` §4.2.1 登记。
