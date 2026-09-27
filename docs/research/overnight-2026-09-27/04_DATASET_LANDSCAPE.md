# 04 — Quantitative dyadic / longitudinal dataset landscape

- Lane: **R04**（Wave 1, overnight-opencode-exploration-swarm-v1）
- **Round-3 修订:** R3-A3b（依 `ARCHITECT_ADJUDICATION_V1` / `#30 comment 5854920569`；裁决映射见 `lanes/R3_A3b.md`）
- 角色: Research child（Fresh Research）｜ 无 GitHub 写权限，产出交 parent 做 durable writeback
- 核实日期: **2026-09-27**（全文所有 access 条件均以此日期为准）
- 状态: `RESEARCH_CANDIDATE`。本文件不是 canonical architecture，不含已确立的结论、参数或公式。
- 边界声明: 本 lane 只做 **consumer-side suitability audit**，**未接触任何数据文件**，**未克隆/读取 Eye 仓库**，**未重复 Eye 的 data-acquisition 工作**，**未绕过任何 access control**，**未修改 `docs/` 下任何文件**。

> **R3-A3b 二次抓取声明（与上条并存，不矛盾）**
>
> - R3-A3b 于 2026-09-27 **重新抓取了若干 CoU / licence / policy 页面**（SHARE、Add Health、ICPSR LLM policy、ICPSR Redistribution Policy、ICPSR SOMAR VDE），用于更正**已撤回的**权利断言。
> - R3-A3b **仍然零数据接触**：未下载、未打开、未分析任何数据文件或受限数据；未使用任何凭据；未绕过 auth / licence / robots。
> - 抓取失败一律记为 `UNVERIFIABLE_HERE`（附 URL 与状态码），**不**由失败推出任何结论。清单见 §12。
> - **Rights fail closed 仍在执行。** R3-A3b 的全部改动方向都是**收紧或撤回**，**没有任何一处放宽任何数据集的权利条件**。

> **阅读提示（重要）**
> 本文件严格区分两件经常被混为一谈的事：
> 1. **「我们能用这个数据集」** = 该数据的**结构**支持方向化 (i→j / j→i)、纵向、部分信息二人状态模型；
> 2. **「我们能拿到这个数据集」** = 今天存在一条可复现、合规、且**允许 LHRM 计划用途**的获取路径。
>
> 本文件的主要发现之一（见 §5）就是：**在这两件事之间，2026-09 存在一条正在变宽的裂口。** 多个主力数据集的 use conditions 已在 2025–2026 年被收紧到禁止 LLM/AI 处理个体级数据。
>
> **R3-A3b 更正**：本段末句的「横跨 SHARE / ICPSR / Add Health / UAS / HRS 的**系统性**收紧」是**单源扩散**，不是 5 份彼此独立的证据。见 §1.3 与 §5.3。


---

## 1. 结论摘要

### 1.1 审计规模

| 项 | 数值 |
|---|---|
| 严肃 quantitative dyadic / longitudinal dataset 审计数 | **16**（D01–D16） |
| **其中进入结构检验的** | **15** —— **Add Health（D12）从未进入结构检验**：它被一条**许可 / use-condition** 理由排除在结构判定之外，而不是因为结构不合格（见 §8.9 与 §4.12） |
| 其中双方各自独立作答同一构念 | **4**（pairfam、SHARE、HARP、HRS 部分模块）—— **R3-A3b：这是数据集级近似，逐格事实见 §4.17；`CALIBRATION_READY` 已不再依赖该数据集级判断** |
| 其中 `STRUCTURAL_CALIBRATION_CANDIDATE` | **3**（pairfam、SHARE、HARP）—— **R3-A3b：该等级严格只成立于「结构层」**（U15 未解：构念内容未核实） |
| 其中带 intensive-longitudinal（密集日记）设计 | **1**（HARP，8–10 天日记 × 3 个时间点） |
| 覆盖国家/地区（跨文化） | 德国、欧盟 27+ 国、印尼、新西兰、美国、约 90 个 DHS 参与国 |
| 覆盖关系类型 | 已婚、同居/未婚、丧偶后随访、离婚/分居后续访、恋爱（首次约会）、亲子/代际、照护-被照护、青少年同伴关系（文件层未核实） |
| 覆盖同性关系 | **2** 有明确设计（HARP、pairfam `homosex`）；其余为 0 或未核实 |
| 完全公开无门槛（可立即下载） | **1**（Fisman–Iyengar speed dating 公开镜像）—— 依 review-r2 `R-C13`，全文统一为「**技术上零门槛可下载（第三方镜像）**」，不是「完全公开」 |

### 1.2 一句话结论

> **在方向化（i→j / j→i）双人自报 + 纵向 + 双方各自作答这三个条件同时成立的数据集里，本审计只找到 3 个（pairfam / SHARE / HARP），全部在 DUA 之后；而技术上零门槛可下载的那一个（speed dating 第三方镜像）没有任何纵向结构。同时，Add Health、UAS、SHARE、ICPSR 已在 2025–2026 明确限制或禁止用 LLM/AI 处理个体级数据。LHRM 的 Case Bank 与 validation corpus 若要引入问卷型数据，必须先解决权利层问题，而不是先解决统计层问题。**
>
> **R3-A3b 对本段的两处范围更正（依 adjudication **X-14**）**：
> 1. 「2025–2026 的收紧」是**单源扩散**，不是五个独立来源的**系统性**约束 —— 见 §1.3。
> 2. 「只找到 3 个」是**本次检索**的结果，**不是**「这样的数据集在字段上只有 3 个」或「不存在更多」。**Add Health 的官方文档确有 nomination / romantic-pair 结构，但它从未进入结构检验**（§8.9）。

### 1.3 「2025–2026 年 LLM/AI use-condition 收紧」的独立性核算（R3-A3b 新增；依 review-r2 `R-C7` / `C-C36` `CONTESTED`）

**被取代的原文**（逐字保留，§1.2 与 §10）：

> 「多个主力数据集的 use conditions 已在 2025–2026 年被收紧到禁止 LLM/AI 处理个体级数据」
> 「发现了 **2025–2026 年 LLM/AI use-condition 收紧** 这一横跨 **SHARE / ICPSR / Add Health / UAS / HRS** 的**系统性约束**」

**R3-A3b 改述为「单源扩散」（`SINGLE_SOURCE_DIFFUSION`），依据如下（三条均经 R3-A3b 于 2026-09-27 直开官方页面确认）**：

| 数据集 | 该数据集自己的政策自述 | 证据类型 |
|---|---|---|
| **ICPSR** | ICPSR Policy on the Use of Large Language Models 页首行逐字：**"Approved: December 11, 2024"**；末段 "Special Thanks: ICPSR would like to credit **Sebastian Karcher at Syracuse University for originating this taxonomy of LLMs.**" | **本族政策的源头**（已直开） |
| **Add Health** | Conditions of Use 页 "Acknowledgement" 段逐字："Thanks to **the University of Michigan's Health and Retirement Study and ICPSR** as well as **Sebastian Karcher at Syracuse University** for originating this taxonomy of LLMs and/or policy." | **官方自述为承袭**（已直开） |
| **SOEP** | 存在专门的 SOEP AI and LLM Use Policy（**`CITED_SECONDARY`：R3-A3b 的 4 次抓取尝试全部 404 / 500 / transport error，见 §12；本条依据 lane `C` / `C-C13` 的直开记录**） | 承袭（R3-A3b **未**直开） |
| **HRS** | CoU（2026-02-04）含新的 AI / LLM 政策（H-C1 `VERIFIED`，lane `C` 直开；**R3-A3b 两次抓取均 403，见 §12**） | 承袭（R3-A3b **未**直开） |
| **SHARE** | SHARE CoU（2026-04-30）§7 禁止「非完全自管」应用 + 禁止 AI 训练（**R3-A3b 已直开**）—— 但 SHARE 的条文**不提** HRS / ICPSR / Karcher 溯源，且**不采用** Type 1/2/3 分类法 | **独立成文**（已直开） |
| **UAS** | "large language models (LLMs) and other artificial intelligence tools may not be used to manage, process, or analyze any data distributed by CESR"（原 report 直开） | **独立成文**（R3-A3b 未复核） |

**结论（可引用版本）**：

> **ICPSR 的 Type 1/2/3 LLM 分类法是这一族政策的源头**（`Approved: December 11, 2024`，且 ICPSR 页面本身把该 taxonomy 归功于 Karcher）。**Add Health 与 SOEP 在其官方页面上各自把该 taxonomy 溯源到 HRS + ICPSR + Karcher。** 因此 **ICPSR / Add Health / SOEP / HRS 这四项不是四份彼此独立的证据，而是同一 taxonomy 的四次采纳（`SINGLE_SOURCE_DIFFUSION`）。** 它们**可以**作为"该 taxonomy 的采纳面很广"这一事实的证据；**不可以**作为"四个独立机构各自独立收紧"来计数。
>
> **SHARE 与 UAS 不在此扩散链内**：SHARE 独立成文（且不采用 Type 1/2/3 分类法），UAS 独立成文。
>
> **R3-A3b 的抓取缺口必须随引用携带**：HRS CoU 与 SOEP AI/LLM Use Policy **R3-A3b 本人未能打开**（403 / 404 / 500）。上述关于 HRS 与 SOEP 的表述是**转述**，不是 R3-A3b 的直开核实。

---

## 2. 判级标准（R3-A3b：分类改为两轴三分，`CALIBRATION_READY` 改为两级标签）

> **R3-A3b 的结构性更正（依 review-r2 `R-C5` / `R-C6` / `R-C8`）**
>
> 旧版把**两件不同的事**压在**一个**标签上：**(a) 数据集的结构能不能支撑方向化纵向状态模型**，与 **(b) 今天能不能合法拿到并按 LHRM 用途使用**。后果是 `D12` / `D13` 的 `cannot_identify: 不可识别` 与 `D15` 的 `ACCESS_BLOCKED` 混成一轴 —— 许可条件被写成了识别能力。本节改为**两轴**：**结构轴** 与 **访问/权利轴**，各自独立给值。

### 2.1 轴一：结构能力（`structural_verdict`）—— 旧 `CALIBRATION_READY` / `MEASUREMENT_ONLY` 归入此轴

| `structural_verdict` | 定义 | 判定要点 |
|---|---|---|
| `STRUCTURAL_CALIBRATION_CANDIDATE` | **结构上**足以支撑方向化纵向状态模型 | 稳定 dyad id + **双方各自作答** + ≥3 wave + codebook + outcome/event + 缺失/样本选择文档 + 可复现获取路径 |
| `STRUCTURAL_MEASUREMENT_ONLY` | 可用作测量来源，但不足以支撑转移律或方向性分解 | 缺 1 wave / 双方测量不对称需外部假设 / 只有 pair-level 事实 / outcome 无后续时点 |
| `STRUCTURAL_REPRESENTATION_ONLY` | 只用于让模型看到关系表述形态，不做参数估计 | **本 landscape 无此类 quantitative dataset**；该角色由 `VALIDATION_CORPUS_V0_1.md` 的叙事材料承担 |
| `STRUCTURAL_NOT_DYADIC_ENOUGH` | **发货形态**没有可用 partner id，dyad 需分析者启发式重建 | 重建规则是模型假设，不是证据 |
| `STRUCTURAL_UNKNOWN` | 结构属性本 lane 未核实 | 与 `NOT_ASSESSED` 同构 |

### 2.2 轴二：访问 / 权利（`access_rights_axis`）—— 旧 `ACCESS_BLOCKED` 归入此轴

| `access_rights_axis` | 定义 | 判定要点 |
|---|---|---|
| `ACCESS_OPEN` | 存在可复现、合规、且**允许 LHRM 计划用途**的获取路径 | — |
| `ACCESS_RESTRICTED_PERMISSIBLE` | 有获取路径但附带实质限制（用途、再分发、输出预审、成员机构限定等） | 须逐条写出限制 |
| `ACCESS_BLOCKED_USE_CONDITION` | **拿到了但不许这样用**（use-condition block）：许可 / CoU 明确禁止 LHRM 计划用途 | 须逐字引用条文 |
| `ACCESS_BLOCKED_POSSESSION` | 拿不到（审批链过长、无现实路径、需尚未获得的授权） | 须写出审批链 |
| `ACCESS_UNKNOWN` | 获取条件本 lane 未核实 | — |

**两轴不可互相推导**（`R-C5` / `R-C6`）：
- `ACCESS_BLOCKED_*` **不蕴含** `STRUCTURAL_*` 差。`D12` Add Health 与 `D13` UAS 的**结构**（双报告潜力、nomination 网络、6 wave）与其**权利**是两个独立事实。
- `STRUCTURAL_MEASUREMENT_ONLY` **不蕴含** `ACCESS_BLOCKED_*`。`D15` Oregon 的结构是 `STRUCTURAL_MEASUREMENT_ONLY`（单期、双报告恋爱 dyad），其访问是 `ACCESS_BLOCKED_POSSESSION`（RDUA + IRB，非公开下载）。
- **旧版的 `cannot_identify: 不可识别` 措辞已全部改写**：许可条件 ≠ 识别能力。R3-A3b 把这类行的字段名统一为 `cannot_identify_for_LHRM_use`（权利轴）并与 `cannot_identify_structurally`（结构轴）分列。

**旧字段名 → 新字段名映射（R3-A3b；便于交叉引用旧版文本）**

| 旧字段名 | 新字段名 | 轴 |
|---|---|---|
| `classification: CALIBRATION_READY` | `structural_verdict: STRUCTURAL_CALIBRATION_CANDIDATE` **+** `access_rights_axis: …` | 拆两轴 |
| `classification: MEASUREMENT_ONLY` | `structural_verdict: STRUCTURAL_MEASUREMENT_ONLY` **+** `access_rights_axis: …` | 拆两轴 |
| `classification: NOT_DYADIC_ENOUGH` | `structural_verdict: STRUCTURAL_NOT_DYADIC_ENOUGH` | 结构轴 |
| `classification: REPRESENTATION_ONLY` | `structural_verdict: STRUCTURAL_REPRESENTATION_ONLY` | 结构轴 |
| `classification: ACCESS_BLOCKED` | `access_rights_axis: ACCESS_BLOCKED_POSSESSION` **或** `ACCESS_BLOCKED_USE_CONDITION`（**须分清是哪一种**） | 访问轴 |
| `can_identify:` | `can_identify_structurally:` | 结构轴 |
| `cannot_identify:` | `cannot_identify_structurally:` | 结构轴 |
| `cannot_identify_without_assumption:` | `cannot_identify_structurally_without_assumption:` | 结构轴 |
| `cannot_identify: 对 LHRM 计划用途 —— 不可识别（…政策）` | `cannot_identify_for_LHRM_use（权利轴）:` **+** 独立的 `cannot_identify_structurally:` | **拆两轴 —— `R-C6` 的核心处置** |
| （无） | `classification_legacy_equivalent:` | 保留旧单轴值供交叉引用；**旧值不得进入任何跨表统计或 canonical 依据** |

**有意保留的两个未列入 §2.1 枚举的值**：`STRUCTURAL_MEASUREMENT_ONLY_PENDING`（显式的"待判定"标记，
见 D09 卡）与 `STRUCTURAL_UNKNOWN`（无一手结构文档在手，如 D14）。二者都**不是** §2.1 的第五类；
它们表示"按现有证据无法定级"，**不是**"结构不合格"。


### 2.3 轴三：逐格属性 —— `both_parties_answer_separately` 必须是 **per-dataset / per-module / per-condition** 列表（R3-A3b 新增）

旧版把「双方独立作答」当作**数据集级**属性（主表一列 + `CALIBRATION_READY` 的定义要点之一）。这是错的：**同一数据集内，模块之间可以不对称**（SHARE 官方明文区分 `hou_resp` / `fin_resp` / `fam_resp`；SECCYD 照护侧单方；NSFH 配偶关系质量单方、亲子双向）。R3-A3b 新增 §4.17 逐数据集 × 逐模块表，**`CALIBRATION_READY` 不再以「双方各自作答」作为数据集级条件**。

---

## 3. 主表

| ID | Dataset | 主办方 | 关系类型 | 双方独立作答 | Waves | 稳定 couple id | Codebook | Outcome/Event | Missingness/选择文档 | 跨文化 | 同性 | 未婚/同居 | 非浪漫/kin | Access 路径（2026-09-27） | `structural_verdict` | `access_rights_axis` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D01 | **The German Family Panel (pairfam)** / ZA5678 | LMU Munich + MPIDR，GESIS FDZ 分发 | 婚恋+家庭+亲子+代际 | **是**（`anchor$` + `partner$`）；**非共居 partner 不覆盖** | **14**（年度，2008/09–）—— **version-drift 风险，U18** | 是（`id` + `pid`，标准 key 变量可链接） | 是（14 wave 英/德 codebook + 问卷 + Data Manual + method reports） | 是（`biopart` 关系生命史 + 生育/健康/就业） | 是（method reports、`sample`/`cohort`/`demodiff` 标记） | 仅德国 | **是**（`homosex` / `homosex_new`） | 是（`relstat`/`marstat`） | 是（`parent$` 至 wave 8；`child$` 8–15 岁） | 免费；签署 user contract / Nutzungsantrag 交 GESIS；DOI 版本化 | `STRUCTURAL_CALIBRATION_CANDIDATE` | `ACCESS_RESTRICTED_PERMISSIBLE`；**AI 条款未核实（U18）→ fail closed** |
| D02 | **SHARE** (Survey of Health, Ageing and Retirement in Europe) | SHARE-ERIC，FDZ-SHARE (CentERdata / GESIS) | 婚恋+家庭经济+照护+健康 | **逐模块不同**（见 §4.17）—— 常规个人模块是；`fin_resp` / `fam_resp` / `cv_r` / SHARELIFE / end-of-life / proxy 段**否** | **到 Wave 9 (2021–2022) 常规 wave**（FAQ 4.3 逐字）；**Wave 10 = `UNKNOWN_AS_OF`** | **是**（`coupleid*w`，couple 不变则跨波固定；官方 FAQ 5.3 逐字） | 是（Release Guide、cross-wave comparison、methodology volumes、Scales Manual） | 是（SHARELIFE 回溯生命史；健康/退休/就业事件） | 是（methodology volumes、longitudinal weights、coverscreen `gv_allwaves_cv_r`） | **欧盟 27+ 国 + Israel** | 部分轮次含 | 是 | 是（`CH`/`SP` 模块；kin）—— **`CH` 顺序/linkage 官方声明不可靠（FAQ 5.8）** | 免费；个人注册 + SHARE User Statement | `STRUCTURAL_CALIBRATION_CANDIDATE` | `ACCESS_RESTRICTED_PERMISSIBLE` + §7 实质限制（**已直开逐字**） |
| D03 | **Health and Relationships Project (HARP)** / ICPSR 37404 | UT Austin（Umberson 等），ICPSR/NACDA | 已婚婚恋 + 健康 + 日常压力 | **是**（明令 spouses 分开作答） | **3 个时间点**（2014-15 / 2021-22 / 2024-25）**各含 8–10 天日记** | 是（couple-level recruitment + couple ids） | 是（baseline + diary 问卷、ICPSR datadocumentation） | 是（关系质量、健康、压力、离婚/分居/丧偶状态） | **是（最详细）**：逐时间点留存 n、分批投放设计、激励变化、per-diary 完成率 | 美国（马萨诸塞州） | **是**（同性+异性） | **否**（要求合法婚姻 + 同居≥3 年） | 否 | ICPSR 公版；"public-use data files are available for access by the general public"（但本环境 study 页未直开，见 §8） | `STRUCTURAL_CALIBRATION_CANDIDATE` | `ACCESS_RESTRICTED_PERMISSIBLE`（公版）+ ICPSR 再分发/ LLM 政策（**已直开**） |
| D04 | **Fisman & Iyengar Speed Dating Experiment** (2002–2004) | Columbia Business School | **首次约会**（4 分钟速配） | **是**（`dec` 单方意愿 + `match` 互惠 + 6 项双向评分） | `wave` = **21 场 session**，非同一 dyad 的重复观测 | 是（`wave` × 配对 id） | 是（Speed Dating Data Key） | 弱（仅「想不想再见」） | 弱（无官方 missingness 文档） | 美国（Columbia 活动） | **否**（"participant of the opposite sex"） | 否 | **是（关系形成前的最短交互）** | **技术上零门槛可下载（第三方镜像）**（2026-09-27 仍在线） | `STRUCTURAL_MEASUREMENT_ONLY` | `ACCESS_RESTRICTED_PERMISSIBLE`（**无门槛**；Columbia 原始数据政策未核实 → 保守按「引用而非再分发」） |
| D05 | **DHS Couples (CR) file** | The DHS Program | 婚恋（couple 为分析单位） | **是**（双方自述配对后链接） | **单轮/国** | 是（couple file 一对一条；ID 取女方 `caseid`） | 是（Guide to DHS Statistics、recode file naming、codebook） | 是（生育、避孕、HIV、健康、决策权、暴力） | 是（采样/权重/抑制规则、Data Suppression 章节） | **约 90 个 DHS 参与国** | 事实婚姻制国家极少 | 是（living together 计入） | 否 | 免费；电子注册 + 授权后下载 | `STRUCTURAL_MEASUREMENT_ONLY` | `ACCESS_RESTRICTED_PERMISSIBLE`（授权制） |
| D06 | **Indonesia Family Life Survey (IFLS1–IFLS5)** | RAND + 印尼合作机构 | 家庭+婚恋+亲属转移 | 部分（household head + spouse；`BA`/`TF` 亲属模块） | **5**（1993-94 / 1997 / 1998(25%子样本) / 2000 / 2007-08 / 2014-15） | **未核实**（官方 FAQ 指向 IFLS2 User's Guide 的 spouse 识别章）⇒ 方向性依赖重建假设 | 是（每波 6–7 卷：overview、user's guide、问卷、codebook、crosswalk） | 是（婚姻/生育/迁移/健康/教育/就业/亲属转移） | 是（re-contact 率、分波实地日期、`fixes` 文件、split-off 规则） | 印尼 13 省（≈83% 人口） | 未专项 | 是 | **是（非同住亲属 + 亲属转移）** | 免费；RAND 注册 + confidentiality declaration；**"Please do not distribute these data"**；受限地理码需另申请 | `STRUCTURAL_MEASUREMENT_ONLY`（**官方提供构造指引**） | `ACCESS_RESTRICTED_PERMISSIBLE`（**未见专门 AI 条文**） |
| D07 | **Growing Up in New Zealand (GUiNZ)** | University of Auckland | 亲子 + 青少年家庭 + 同住伴侣 | 部分（家庭成员 id 齐） | **~9**（2009 起；17 岁 wave 2026-05 启动） | 是（家庭成员 id） | 是（Data User Guides / Data Dictionaries / Questionnaires，需先接受 legal disclaimer） | 是（健康、发展、家庭、极端天气事件） | 是（Data Access Protocol 2026 v1.0、Data Output Guide） | 新西兰（多族裔） | 未专项 | 是（青少年/未婚） | **是** | **正式 Data Access Application**；PI 必须挂靠新西兰研究机构（Kaitiakitanga）；签 DAA；经 Secure Data Access Platform；**输出须预审**（≤4 工作日） | `STRUCTURAL_MEASUREMENT_ONLY` | `ACCESS_RESTRICTED_PERMISSIBLE` + **Kaitiakitanga 主权约束（§2.2 的独立轴，非 access 阻断）** |
| D08 | **National Survey of Families and Households (NSFH, W1–W3)** | Wisconsin–Madison CDHA / Temple ISR；ICPSR + CFDA + DISC | 家庭结构+亲子+跨代+同住非婚 | 部分（**亲子方向可测**；**配偶间：Wave 1 单方报告已核实，Wave 2+ `UNKNOWN_AS_OF`**） | **3**（1987-88 / 1992-94 / 2001-0x） | 是（个体 + 家庭级 id） | 是（Users' Guide、DDI XML、PI codebook + Appendix O 权重） | 是（婚姻/同居/离婚/再婚/监护/抚养/健康/照护责任） | 是（ICPSR/DISC 归档规范、地码版为 restricted） | 美国（**过抽样设计，非概率抽样**） | **否**（1987 起设计） | 是 | **是（亲子/跨代/继亲/kin contact）** | ICPSR/Child & Family Data Archive 公版；"Access does not require affiliation with an ICPSR member institution" | `STRUCTURAL_MEASUREMENT_ONLY` | `ACCESS_RESTRICTED_PERMISSIBLE`（公版）+ ICPSR 再分发 / LLM 政策（**已直开**） |
| D09 | **Changing Lives of Older Couples (CLOC)** / ICPSR 3370 | Univ. of Michigan（House / Wortman / Nesse） | **丧偶照护与哀伤** | **是**（Couples Only 数据集含妻 `V*` + 夫 `S*` 全 4 wave） | **4**（baseline 1987-88 + 配偶死亡后 6 / 18 / 48 月） | 是（Part 5 含 423 couples / 846 人） | 是（6 个子数据集 + 各年 codebook 文件） | 是（哀伤 6 子量表 + DSM-III-R 重性抑郁 + 生理/生化 MacBat 子样本） | 是（NDI + 州死亡记录确认；matched control 设计） | 美国（Detroit SMSA） | 否 | 否 | 是（配偶死亡事件） | ICPSR；"freely available to data users at ICPSR member institutions" | **`STRUCTURAL_MEASUREMENT_ONLY_PENDING`**（按本报告判据应更高；子集选择规则 `UNKNOWN`） | `ACCESS_RESTRICTED_PERMISSIBLE`（**限 member institution**）+ ICPSR 再分发 / LLM 政策（**已直开**） |
| D10 | **Health and Retirement Study (HRS)** | Univ. of Michigan ISR / NIA | 老年婚恋 + 照护 | 部分（夫妻同受访；**配偶常作 proxy respondent**） | **双年**，1992– | 未核实（HRS 正文页本环境不可达，U5） | 是 | **是（ADL/IADL 协助天然给出方向性照护行为）** | 是 | 美国 | 未专项 | 部分 | 是（同住 + 跨代） | 公版免费 + DUA；restricted 需 RDA + IRB + security plan + institutional counter-signature | `STRUCTURAL_MEASUREMENT_ONLY` | `ACCESS_RESTRICTED_PERMISSIBLE`（公版）/ `ACCESS_BLOCKED_POSSESSION`（restricted）+ **`ACCESS_BLOCKED_USE_CONDITION`（AI/LLM = 禁止）** |
| D11 | **SOEP** (German Socio-Economic Panel) | DIW Berlin | 家庭 | 部分 | 长期年度面板 | **公开标准文件无 partner id** | 是 | 是（如风险态度 0–10 双向个体变量） | 是 | 德国 | **构造后为 0**（"We do not find any same-gender couples"） | 是 | 部分 | 需向 DIW 申请 | `STRUCTURAL_NOT_DYADIC_ENOUGH`（**无官方构造指引**，见 §2 的 SOEP/IFLS 边界） | `ACCESS_RESTRICTED_PERMISSIBLE` + **`ACCESS_BLOCKED_USE_CONDITION`（SOEP AI and LLM Use Policy: Type 1/2/3 全 None；`CITED_SECONDARY`，U19）** |
| D12 | **Add Health (The National Longitudinal Study of Adolescent to Adult Health)** | UNC CPC | 同伴+恋爱+家庭 | **不判定** | **6 wave**（Wave I–VI） | **不判定**（nomination 文件存在性 = `UNVERIFIABLE_HERE`，U7） | 是（ACE codebook explorer、Add Health Navigator） | **不判定** | **不判定** | 美国 | **不判定** | **不判定** | **不判定** | 可申请（公版 + restricted） | **`NOT_ASSESSED`（从未进入结构检验）** | **`ACCESS_BLOCKED_USE_CONDITION`**（AI/LLM 全面禁止，公版与 restricted 同等） |
| D13 | **Understanding America Study (UAS)** | USC CESR | 家庭+健康+退休 | 部分 | 双年核心调查，自 2014 | **未核实** | 是（CF/CPD Data Description） | 是 | 是 | 美国 | — | 部分 | 是 | 注册 + Data User Agreement（免费） | `STRUCTURAL_MEASUREMENT_ONLY`（**本 packet 判定；旧版未判**） | **`ACCESS_BLOCKED_USE_CONDITION`**（AI 全面禁止）+ Enclave 限美国研究者 |
| D14 | **American Family Cohort (AFC)** | Stanford | **多代家庭** | 部分 | 多代纵向 | 未核实 | 是 | 是 | 是 | 美国 | 未核实 | 未核实 | **是（三代替代）** | **classified as PHI**；PHS Data Portal + ABFM 批准 + 第三方 DUA + IRB + 逐项目审批 | `STRUCTURAL_UNKNOWN` | `ACCESS_BLOCKED_POSSESSION` |
| D15 | **Oregon Youth Study Couples Study, Time 6** | Oregon Youth Study / Three Generational Study | **恋爱伴侣** | 是（受访者+其恋爱伴侣） | **单期（2003–2006）** | 是（couples study 结构） | 是 | 是（社会模式、性行为、物质使用、心理健康） | 是 | 美国（Oregon） | 未专项 | 是 | 否 | **Restricted Data Use Agreement + IRB approval/notice of exemption**；非公开下载 | **`STRUCTURAL_MEASUREMENT_ONLY`** | **`ACCESS_BLOCKED_POSSESSION`** + ICPSR 再分发 / LLM 政策（**已直开**） |
| D16 | **NICHD SECCYD (Phase I–IV)** | NICHD / 多点研究网络 | **母婴 / 照护者—儿童** | **否**（主要照护者单方报告，>90% 生母） | **4 phase**（Phase I 1991-94 起 1,364 儿童；Phase IV 1,056） | 是（child/family id） | 是（ADS 1–42 / SDS 43–55 / Raw 56–309 等 309 文件） | 是（照护安排、认知、语言、行为适应、身体健康） | 是（5 个主评估点 + 每 3 月电话；排除标准明列） | 美国 10 地 | 否 | 是（单亲家庭纳入） | **是** | ICPSR 公版；"available for access by the general public" | `STRUCTURAL_MEASUREMENT_ONLY` | `ACCESS_RESTRICTED_PERMISSIBLE`（公版）+ ICPSR 再分发 / LLM 政策（**已直开**） |

> **R3-A3b 对本表的重构（依派工 item 14）**
> - **最后一列从一个分类改为两列**（`structural_verdict` / `access_rights_axis`），依据 `R-C5` / `R-C6`。
> - **`CALIBRATION_READY` / `MEASUREMENT_ONLY` / `NOT_DYADIC_ENOUGH` 三个旧值仅作为 legacy 标签**保留在各卡片内，**不得**进入任何跨表统计或 canonical 依据。
> - 「双方独立作答」列的 D02 / D08 / D10 / D12 条目改为**逐格引用 §4.17**，本列不再作数据集级断言。
> - **D12 全行按 `structural_examination_status` 标为「不判定」** —— 它从未进入结构检验（`R-C6` / X-14）。
> - D09 的 `structural_verdict` 标 **`..._PENDING`** 并附理由（D09 卡）。
> - D14 的 `structural_verdict` 标 **`STRUCTURAL_UNKNOWN`**（旧版把它与审批链一起归 `ACCESS_BLOCKED`）。
> - D04 的 access 措辞由「**完全公开**」改为「**技术上零门槛可下载（第三方镜像）**」（`R-C13`）。
> - D06 / D11 按 §2 的 **SOEP/IFLS 单一边界**分列。


---

## 4. 逐数据集详情卡

### D01 — The German Family Panel (pairfam) · ZA5678

```text
structural_verdict:  STRUCTURAL_CALIBRATION_CANDIDATE
access_rights_axis:  ACCESS_RESTRICTED_PERMISSIBLE（免费；需签 user contract）+ **AI / LLM 条款未核实（U18）**
classification_legacy_equivalent: CALIBRATION_READY（旧单轴标签，保留以便交叉引用；**旧标签不作 canonical 依据**）
canonical_pointer:
  study:        https://www.pairfam.de/en/data/data-access/
  archive:      https://access.gesis.org/dbk/52241
  data_manual:  https://access.gesis.org/dbk/53708  (Brüderl et al. 2024, doi 10.4232/pairfam.5678.14.2.0)
  usage_form:   https://access.gesis.org/dbk/69762
  current_version_observed: Release 14.2  (14 survey waves, doi 10.4232/pairfam.5678.14.2.0)
design (CITED_PRIMARY, 2026-09-27):
  - "Panel Analysis of Intimate Relationships and Family Dynamics"
  - 年度全国性调查; 初始样本 >12,000 名随机个体, 出生队列 1971-73 / 1981-83 / 1991-93
  - multi-actor: anchor (主受访者) + 其 current partner; 第 2 wave 起加 (step)parents 与 8 岁以上 children;
    parent survey 于 wave 8 结束; 另有 parenting survey on children (wave 2 起)、PAYA (wave 9-13)、
    parenting U6 partner survey (wave 11-13)、step-up sample (wave 4 起)
  - 实地执行: Kantar Public (前身 TNS Infratest Social Research), Munich
  - 数据按 wave / actor / instrument 三重组织: anchor1..anchor14, partner1..partner14, parent$, child$, paya$, stepup_$
  - 官方原文: "By using a standardized key variable it is possible to link those data sets for
     longitudinal or dyadic analyses."
dyad_identifiability:  STRONG. anchor id `id` + partner id `pid`; 官方原文: "By using a standardized key
   variable it is possible to link those data sets for longitudinal or dyadic analyses."
   **R3-A3b 更正（依 review-r2 `R-C18` / `C-C21` `CONTESTED`）**: 旧版写「官方 GESIS 变量清单中 partner 侧变量
   **统一** `p` 前缀」。改为「partner 侧变量**主用**（mainly）`p` 前缀」。
   **R3-A3b 的抓取状态**: `https://www.pairfam.de/en/data/data-structure/` 返回 **HTTP 500**（2026-09-27）
   ⇒ 该前缀规则**未被 R3-A3b 重新核实**，标 `CITED_PRIMARY (relay, 未由 R3-A3b 重开)`。
   旧版所列的 `psex_gen, page, preldur, pmarstat, pincoecd, ...` 与 anchor 侧 `k*` / `yk*` / 无前缀一并保留，
   但**不得**由它们推出「统一前缀」。
   **"统一前缀"本身是可证伪的强主张**（存在 `parent$` / `child$` / `paya$` / `stepup_$` 这些多 actor 文件
   命名，不属于 `p*` 单一族）⇒ 收窄为「主用」在证据上更稳，且与文件组织一致。
waves:                 14 (annual). 另有 COVID-19 子研究 (ZA5959)
   **R3-A3b 时效标注**: 波次数是 **version-drift 风险项**。旧版记 "Release 14.2 (14 survey waves,
   doi 10.4232/pairfam.5678.14.2.0)"。R3-A3b **未重开** pairfam 数据页（data-structure 500），
   故 **14 / 14.2.0 这个值是 time-sensitive，且在被用作承重输入前必须重新确认**（U18）。
   引用该波次数的任何下游文档必须带 **取用日期**，不得把它当稳定事实。
rights_evidence_status (R3-A3b 新增; 依派工 item 14 "rights assertions stay PLAUSIBLE with explicit gaps"):
   旧版 rights 摘要（§3 only / §4 no commercial / §5 no third-party forwarding / 50% teaching version /
   deposit within 4 weeks / macro-level aggregates "not freely accessible"）**整体标 `PLAUSIBLE`**，
   **不是 `CITED_PRIMARY`** —— 理由：这些条文出自 pairfam / GESIS 的 Nutzungsantrag 与 ZA5678
   documentation，**R3-A3b 本轮未打开任何一份**（`pairfam.de/en/data/data-access/` 未重开；
   `access.gesis.org` 三个 dbk 链接未打开）。
   **显式缺口**: (a) 条文编号（§1/§3/§4/§5/§7）**未逐条核对**；(b) 德文原句**未取得**；
   (c) §3 那句「即使无直接标识，也不得发布个体级记录」是**旧 report 的转述**，本 packet 不为其背书；
   (d) **pairfam 的 AI / LLM use condition 完全未核实** —— 本文件**不主张** pairfam 允许或禁止
   任何 LLM 处理。**Rights fail closed ⇒ 在核实前按"不得送入外部 LLM 服务"处理。**（U18）
relation_type_vars: relstat, marstat, cohabdur, mardur, reldur, meetdur, **homosex /ALKhomosex_new**
kin_coverage:          parents (to wave 8) + children (8-15y) + 继亲 → 非浪漫 dyad 有真实结构
codebook:              14 wave 全部 codebook (英/德) + 问卷 + instrument overview + scales manual +
   annual method reports + concept paper + Data Manual; 学术出版物需给 GESIS 副本
missingness:           method reports; 样本来源由 `cohort` / `demodiff` / `sample` 三变量标记
   (pairfam 主样本 / DemoDiff 样本 / refreshment 样本 / step-up 样本)
access_path:           免费。原文 "The use of this data is free of charge!" 需签署 Nutzungsantrag /
   user contract 发至 GESIS 或 pairfam user service (support@pairfam.de)
   教学另有 FReDA/pairfam Campus Use File（GESIS 免费注册即可），但 "not suitable for scientific publications"
can_identify_structurally:
   - 双向自报的关系状态分量、其跨 14 年的演化
   - 关系类型/制度状态与关系状态的可分离（relstat/marstat vs 关系状态题）
   - 同性伴侣 dyad（德国样本）
   - 亲子/代际 dyad 的方向性
cannot_identify_structurally:
   - **非共居 partner 的独立测量**（partner survey 绑定 anchor 的 current partner）
   - 跨文化（仅德国）
structural_dependencies_unverified:
   - pairfam 侧的关系状态构念清单未在本 lane 核实（见 U15）→ 不得预设它能标定 LHRM 构念
lhrm_impact:  最贴近 LHRM 需求形状的公开可得研究面板：双报告 + 长面板 + 同性 + 未婚 + kin 多 actor。
   **R3-A3b 限定**: 「双报告」现应读作 §4.17 的**逐格事实**（partner survey 覆盖 anchor 的 current
   partner，但非共居 partner 不覆盖）。
   **R3-A3b 更正（rights 侧）**: 旧版末句「§3 的『仅可汇总呈现』意味着 **不能把 pairfam 个体记录或其
   直接派生进入 Case Bank**」。**该断言标 `PLAUSIBLE`（`CITED_SECONDARY`）** —— 依据是未打开的 §3 转述。
   **Rights fail closed**: 在拿到逐字条文前，**按"个体记录与其直接派生不得进入 Case Bank"处理**
   （这是收紧方向，不是放宽）。**本 packet 不主张** pairfam 允许其派生量进入任何 LLM 参与的流程。
```

### D02 — SHARE (Survey of Health, Ageing and Retirement in Europe)

```text
structural_verdict:  STRUCTURAL_CALIBRATION_CANDIDATE
access_rights_axis:  ACCESS_RESTRICTED_PERMISSIBLE（免费；个人注册 + SHARE User Statement），
                     且 §7 对处理方式与再分发设实质限制
classification_legacy_equivalent: CALIBRATION_READY（旧单轴标签，保留以便交叉引用；**旧标签不作 canonical 依据**）
canonical_pointer:
  data_access:   https://share-eric.eu/data/data-access
  conditions:    https://share-eric.eu/data/data-access/conditions-of-use   ("Last updated: April 30, 2026")
  releases:      https://share-eric.eu/data/data-documentation
  release_guide: https://share-eric.eu/fileadmin/user_upload/Release_Guides/SHARE_release_guide_9-0-0.pdf
  faqs:          https://share-eric.eu/data/faqs-support
  example_DOI:   10.6103/SHARE.w1.900 ... 10.6103/SHARE.w8.900 (release 9.0.0, 2024-03-28)
R3-A3b_fetch_record (2026-09-27):
  conditions-of-use  直开 **成功** → 全文逐字引用见下（§7 / §11 / §12 三段）
  faqs-support       直开 **成功** → 逐字引用见下（§3.3 回应者类型 / §3.4 proxy / §4.3 波次 / §5.8 CH / §5.9 Wave 4 linkage）
  release_guide_9-0-0.pdf  抓到二进制 PDF，**未能抽取文本** → `UNVERIFIABLE_HERE`（该 PDF 不作为本轮任何断言的来源）
dyad_identifiability (CITED_PRIMARY 官方 FAQ 5.3 原文, R3-A3b 直开确认):
   "In SHARE, partners can be identified by the mergeidp'w' (where 'w' stands for the respective wave)
    which indicates the mergeid of a respondent's partner. Each couple has a coupleid indicated by the
    variable coupleid'w'. The coupleid is generated using mergeid of both partners and is therefore
    unique to each couple as well as fix across waves if the couple stays the same."
   → 这段是本 lane 找到的**对 LHRM「稳定 couple id」要求最干净的官方定义**。
   **R3-A3b**: 该句在 2026-09-27 的直抓中**同时出现在 CoU 页正文与 FAQ 5.3**，两处逐字一致。
directionality:  SUPPORTED **但模块级不对称**（R3-A3b 升级为 §4.17 的逐格事实；见下 `both_parties_answer_separately`）
   官方 FAQ 3.3 原文（R3-A3b 直开，**注意 "on behalf of the couple" 这半句旧版未引**）:
   "…not every eligible household member is asked every questionnaire module. Household respondents answer
    questions on housing, household income and consumption representative for all household members. **On
    behalf of the couple**, financial respondents answer financial transfer and asset questions and family
    respondents answer questions on children and social support – **also on behalf of the couple**. The
    respondent types are indicated by the variables hou_resp (household respondent), fin_resp (financial
    respondent) and fam_resp (family respondent) in the cv_r module as well as in the technical variables
    module."
   → **R3-A3b 的方向性更正**：旧版把这些模块的单方报告描述为"i→j 观测**只有一方**"。
   官方措辞是 **"on behalf of the couple"** ⇒ 该报告既不是 `i→j` 也不是 `j→i`，
   而是**代表 couple 的 pair-level 归属**。这在 LHRM 里对应的是 **pair fact / 制度事实**，
   **不是**有向关系状态。⇒ **不得**把这些模块当双报告，**也不得**把它们当任一方向的有向测量。
   旧版表述保留于下（原 "原文" 块）。
   【原文 · 被取代】: "官方明确区分三类回答者角色 hou_resp / fin_resp / fam_resp: 原文: "the answers to
   financial, housing and family questions in ... modules FT, AS, HO, HH, CO, CH and parts of SP are only
   available for the financial, family or household respondents" → 财务/住房/子女模块的 i→j 观测**只有一方**。"
   【R3-A3b 更正】: 该英文原句出自 CoU / methodology volume（旧 report 的转述），**R3-A3b 未在已打开的
   CoU 页正文中找到它**；已打开的 FAQ 3.3 给的是 "on behalf of the couple" 版本。两者不冲突但侧重不同。
   **R3-A3b 只引用它实际打开的 FAQ 3.3 文本**，并把旧句标 `CITED_PRIMARY (relay, 未由 R3-A3b 重开)`。
   - fam_resp 的选择规则本身带方向性: "The couple's first person interviewed is the family respondent."
both_parties_answer_separately (R3-A3b 逐格; 依据 FAQ 3.3 直开):
   模块 / 条件                              双方是否各自作答        备注
   常规个人模块 (DN/PH/BR/CF/MH/HC/EP/SN/AC…)   是（双方各自）         CAPI main questionnaire 按人施测
   FT / AS / HO / HH / CO                    **否** —— `fin_resp` 单方  官方措辞 "on behalf of the couple"
   CH（子女）/ SP（社会支持）部分              **否** —— `fam_resp` 单方  官方措辞 "also on behalf of the couple"
   coverscreen (cv_r)                        **否** —— 一名家庭成员代全体  官方 2.2: "completed by only one member of the household on behalf of all household members"
   SHARELIFE (w3 / w7)                       **否** —— 官方 3.3 末句: "The SHARELIFE questionnaire does not differentiate between respondent types."（即不按 couple 角色分派）
   end-of-life (XT)                          **否** —— proxy respondent  官方 4.11
   partly / fully proxy interview            **可能是** —— 官方 3.4 允许（见下）
proxy_interview (R3-A3b 新增; 官方 FAQ 3.4 逐字, 直开确认):
   "If physical and/or cognitive limitations make it too difficult for a respondent to complete the
    interview her-/himself it is possible that the sample respondent is assisted by a so-called **proxy
    respondent** to complete the interview ("partly proxy" interview). If the proxy respondent answers
    the entire questionnaire in lieu of the respondent, the interview is referred to as a "fully proxy"
    interview. … Proxy respondents are also asked for end-of-life interviews in case of a respondent´s
    decease. Some questionnaire modules are defined as **non-proxy sections** because those cannot be
    answered by other persons. Cognitive functioning, mental health (partly), grip strength, walking speed,
    activities, and expectations modules are non-proxy sections. The other sections contain the information
   on **who answered the section at the end of the respective questionnaire module: (1) respondent only,
   (2) respondent and proxy or (3) proxy only.**"
   → **R3-A3b 结论**: SHARE **允许 partly / fully proxy interview**。因此「双方各自作答」这一格
   **不是 SHARE 的数据集级属性** —— 它是一个 **per-module / per-condition** 属性，且
   **同一受访者内部**可能出现 (1)(2)(3) 三种状态混在同一份问卷中。
   **对 LHRM 的直接后果**: 任何以 SHARE 标定 `Z[k,i,j,t]` 的设计，**必须**逐格读取模块末的
   "who answered the section" 字段，并**显式排除** proxy-only 段；否则
   `Z[k,i,j,t]` 会在某些段上退化为「代理者的转述」，即 `Belief about j` 与 `Observation of i`
   混在一个数里。**这与 adjudication §C item 6 无关，属测量学事实。**
   **本 packet 不主张** proxy 段与非 proxy 段的系统差异大小（未核实）。
waves:           **R3-A3b 更正（直开 FAQ 4.3 确认）**: 官方 FAQ 4.3「Which countries have
                 participated in each SHARE wave?」**把 Wave 9 (2021–2022) 列为常规 wave**（28 国），
                 另有 "Wave 9 – COVID Survey (2021)"（28 国）。⇒ 常规 panel 的官方波次文档**到 Wave 9**。
                 旧版「≥8 完整常规 wave」**偏保守**，本 packet 未打开 Data Releases 表与 SHARE-CZ FAQ，
                 故**不**把上限定为 9，只记录 FAQ 4.3 的逐字内容。
                 完整波次列表（FAQ 4.3 逐字）: W1 (2004–2006) 12 国 · W2 (2006–2010) 15 · W3 (2008–2010) 14 ·
                 W4 (2010–2012) 16 · W5 (2013) 15 · W6 (2015) 19 · W7 (2017–2018) 28 · W8 (2019–2020) 28 ·
                 W8–COVID (2020) 28 · W9–COVID (2021) 28 · **W9 (2021–2022) 28**。
                 *"(Netherlands\*: In SHARE Waves 6 and 7, the Netherlands did not participate in the regular
                 SHARE wave but conducted a mixed mode experiment.)"*
                 **第 9/10 wave 状态**: 旧版列为「官方站点内部不一致」的**矛盾**。
                 **R3-A3b 改判为 `UNKNOWN_AS_OF`（文档版本差，不是事实矛盾）** —— 依派工 item 14。
                 已抓到的页面里，CoU 页与 FAQ 页的导航均只列到 **Wave 9**（外加 Corona Questionnaire 1/2）；
                 而 FAQ 2.1 的 "Table 1: Overview of documentation files for waves **1 to 8**" 仍只到 Wave 8。
                 ⇒ **同一官方站点上「波次存在性」与「文档覆盖」两张表版本不同步**。
                 SHARE-CZ FAQ 的 "Wave 10 (2023–2024)" 说法 **R3-A3b 未重开** → `UNKNOWN_AS_OF`。
                 **不主张** Wave 10 不存在，**也不主张**它存在。
kin_coverage:     CH (children) / SP (social support) 模块 + SHARELIFE 回溯；couples 亦含同住 partner
non-married:      是（FAQ 3.2 逐字: "in all waves – **current partners living in the same household are
                  interviewed regardless of their age**"）
age_limits:       50+ 为主；FAQ 3.2 逐字: "Younger partners, new partners and partners who never
                  participated in SHARE will not be traced and are not eligible for an end-of-life interview."
                  → 非同住 / 未受访 partner 不可追踪
CH_module_known_defect (R3-A3b 新增; 官方 FAQ 5.8 逐字, 直开确认):
   "**For longitudinal analyses on children users cannot rely on the order of the children in the CH module.**
    It is necessary to match them on gender and year of birth - this will lead to correct merges in most
    cases. There are a couple of reasons behind this. First, respondents are supposed to report on their
    children in a defined order, but they may not necessarily do so. Second, partners may change and
    respondents always are supposed to report on both partners´ children. Third, you can never exclude
    reporting errors."
   → **`CH` 模块的子女顺序与跨波 linkage 是官方声明为不可靠的。** 官方推荐的替代键是
   **gender + year of birth**（官方措辞 "will lead to correct merges in **most** cases" ——
   **"most" 不是 "all"**）。
   **R3-A3b 对 LHRM 的后果**: 任何以 `CH` 模块构造亲子 dyad id 的设计，**不得**使用行序或位置索引，
   且必须承认官方推荐的键本身只有 "most cases" 的正确率。
CH_to_SP_FT_linkage_defect (R3-A3b 新增; 官方 FAQ 5.9 逐字, 直开确认):
   "Yes, in general, this is possible. **The only exception here is Wave 4** in which children named by the
    respondents in the CH module cannot be linked directly to the SP and FT module. The reason is a change
    in the so-called list with relations … Unlike the other waves, the list with relations in Wave 4
    includes up to 7 social network members and just one 'other child' option."
   → **Wave 4 的 `CH` → `SP` / `FT` linkage 不可用。** 这是逐波差异，不是数据集级属性。
codebook:         Release Guide（9.0.0）、cross-wave comparison、methodology volumes、Scales Manual、
                  cv_r / gv_allwaves_cv_r 技术变量模块。**R3-A3b: release guide PDF 本轮未能抽取文本（`UNVERIFIABLE_HERE`）**
access_path:      免费，"Access to the data is provided free of charge for scientific use globally"；
                  个人注册 + 签署 SHARE User Statement；FDZ-SHARE（CentERdata / GESIS）下载
record_linkage:   SHARE-RV (德国养老金)、REGLINK-SHAREDK (丹麦)、REGLINK-SHAREFI (芬兰)、SHARE NL (荷兰 CBS)
                  —— 各自独立申请，**是否含伴侣级 linkage 未核实（U13）**
rights_and_limits (CITED_PRIMARY 原文，2026-04-30 版；**R3-A3b 已直开逐字核对**):
   §2 仅限科学用途。逐字: "the SHARE data may be used for **scientific purposes only** (cf. 6.-8. below)"
   §6 "Under no circumstance may users take any action aiming at a re-identification of participants of the study"
   §7 Confidentiality rules —— 逐字（已直开；旧版引文有删节与一处加粗差异，本次以直开文本为准）:
     "Users are not allowed to make copies of the data available to others and/or enable any third party
      access to the database. Access to the SHARE data is only granted on an individual basis. Please note
      that this means that even within a specific scientific project each person working with the data on
      the project has to register and download the data individually. Furthermore, when using modern data
      processing and storage solutions, such as AI tools and cloud services, users must ensure that no
      unauthorised data transfer occurs. **It is noted that such transfers can occur inherently upon the
      entry of data into an application.** Therefore, the use of applications that are **not fully
      self-administered is strictly prohibited**, unless it can be verified that no data is stored or
      processed by others. Moreover, the data shall not be used for the training of AI models unless such
      training is conducted locally and exclusively for scientific purposes (cf. 2. above); **any use for
      commercial purposes is expressly excluded**.
      **Any derivative datasets, models, or analytical outputs generated through AI or machine learning
      processes remain subject to the same usage restrictions as the original data.**"
   §11 违反后果 —— 逐字（已直开）:
     "In the event of breach of the present Conditions of Use, SHARE-ERIC has the right to **withdraw the
      right of use** of the SHARE data (including the user's access to the SHARE Research Data Center) **with
      immediate effect** from the user at any time and **request him/her to delete all copies of the data
      immediately**.
      In particular, in case of doubt whether or not the data have been used for purely scientific research
      only, SHARE-ERIC furthermore **reserves the right to take any legal action** against users who may
      have violated this basic usage requirement (**cf. 2. above**).
      **In case of an intentional or serious breach of the data protection and privacy rules (cf. 6. above),
      or attempts thereof, SHARE-ERIC reserves the right to make public the data protection violation
      including the identity of the user.**"
     ⇒ **R3-A3b 对旧版「§11 违反后果」的更正（依 review-r2 `R-C2` / `C-C3`）**:
        【旧版, 被取代】"立即撤销使用权、要求删除全部副本；**严重违反**可在网上公开违规者身份"
        【更正】: 公开身份条款的**完整触发条件**是 **"an intentional or serious breach of the data
        protection and privacy rules (cf. 6. above), or attempts thereof"** —— 即 (i) 须是
        **intentional 或 serious** 的违反, (ii) 违反的是 **§6 数据保护与隐私规则**（不是 §7 保密规则）,
        (iii) **包括未遂（attempts thereof）**, (iv) 须带 `(cf. 6. above)` 交叉引用。
        旧版漏了 (ii)(iii)(iv)。**本 packet 不主张**该公开条款的适用范围比上述更宽或更窄
        —— 这是文本层面的逐字记录，不构成法律意见。
   §12 条款可变更，自通知起 21 天生效
   例外: easySHARE 教学简化程序允许教师分发给已注册学生（唯一明文的转供例外）
can_identify_structurally:
   - 跨 27+ 国、50+ 人群、常规个人模块双报告的 couple 级跨面板
   - 健康/照护/退休事件如何伴随关系状态演化
cannot_identify_structurally:
   - FT/AS/HO/HH/CO/CH/SP 模块的**有向**关系状态（单方代 couple 报告 → pair fact，非有向测量）
   - 50 岁以下 partner、非同住 partner、从未受访 partner
cannot_identify_for_LHRM_use（权利轴）:
   - 任何**非完全自管**应用处理个体级 SHARE 数据（§7，除非能核实无第三方存储/处理）
   - 非本地、非纯科学用途的 AI 训练（§7）
   - 向第三方提供数据副本 / 使第三方可访问（§7，individually-granted 原则）
   - 任何 re-identification 尝试（§6）
structural_dependencies_unverified:
   - 关系状态构念本身（SHARE 不是关系质量面板；此处内容未核实 → U15）
lhrm_impact:  唯一具备「跨国 + 双报告 + 长面板 + 官方稳定 couple id 定义」的数据集。
   **【被取代的原文 · 依 review-r2 `R-C3` / `C-C2` `WRONG-SCOPE`】**:
      "**但 §7 使 SHARE 派生量在法务上不能进入一个 LLM 参与的公开验证流水线。**"
   **R3-A3b 更正 —— §7 实际管的是「使用」与「再分发」，不是「派生量能否进入流水线」**:
      §7 逐字规定的是三件不同的事: (a) **哪些应用**可以处理个体级数据（非完全自管者禁止）；
      (b) **AI 模型训练**的地点与用途限制；(c) **数据副本不得提供给第三方**（个体授权原则）。
      另有一句继承条款: "**Any derivative datasets, models, or analytical outputs … remain subject to
      the same usage restrictions as the original data.**"
      **该继承条款的正确读法是「派生量继承原始数据的限制」，不是「派生量被禁止存在或被禁止进入任何流水线」。**
      一个**非个体级**的派生量（尺度分、拟合参数、结构不变性结论）是否可进入一个 LLM 参与的流程，
      由 **§6（anonymity / re-identification）** 与 **§2（scientific purpose）** 管辖，
      **不由 §7 单独决定**；且依 §6(a) SHARE 数据本身受 "factual anonymity" 保护。
      ⇒ **不得**由 §7 单独推出「SHARE 派生量在法务上不能进入一个 LLM 参与的公开验证流水线」。
   **R3-A3b 的可辩护替代定位（不构成权利升级）**:
      建议把 SHARE 定位为「**内部方法学验证来源**」（在**完全自管**的环境内处理个体级数据），
      而非「验证语料 / Case Bank 来源」。**理由不是 §7 禁止派生量，而是：**
      (i) §7 的"非完全自管应用禁止"使**任何把个体级 SHARE 数据送入外部 LLM 服务**的方案不可行；
      (ii) §6 + §11 的后果（撤销使用权 + 要求删除全部副本 + 法律行动）在"公开验证流水线"
      这种**多方参与 + 可复现归档**的场景下不可控。
      **这是本 packet 的风险判断（`AI recommendation`），不是对 SHARE 条款的法律解读，
      也不是任何权利条件的放宽。Rights fail closed。**
   **日期戳**: SHARE CoU 逐字 "Last updated: April 30, 2026"。任何引用必须带该日期戳。
```

### D03 — Health and Relationships Project (HARP) · ICPSR 37404

```text
structural_verdict:  STRUCTURAL_CALIBRATION_CANDIDATE
access_rights_axis:  ACCESS_RESTRICTED_PERMISSIBLE（ICPSR 公版）+ ACCESS_BLOCKED_POSSESSION（任何 individually-deposited 子集）
                     + ICPSR 再分发 / LLM policy（**R3-A3b 已直开**，见 §5.1a）
classification_legacy_equivalent: CALIBRATION_READY（旧单轴标签，保留以便交叉引用；**旧标签不作 canonical 依据**）
canonical_pointer:
  study:   https://www.icpsr.umich.edu/web/NACDA/studies/37404
  summary: https://www.icpsr.umich.edu/web/NACDA/studies/37404/summary
  doc:     https://www.icpsr.umich.edu/web/NACDA/studies/37404/datadocumentation
  lab:     https://liberalarts.utexas.edu/health-relationships-lab/about-harp/
design (CITED_PRIMARY, ICPSR datadocumentation):
   同性婚姻 + 异性婚姻，合法已婚，T1 时 35–65 岁。
   每个时间点：baseline questionnaire + 连续 10 天 daily diary questionnaire，全部在线，
   "spouses were asked to complete the surveys separately"
   入组要求: 合法已婚 + **已同居至少 3 年**
   daily diary 入组门槛: 10 天中完成 ≥6 天
waves_and_attrition (CITED_PRIMARY 数字):
   T1 (2014-15): n = 838 individuals / 419 couples；日记 378 couples (756 人)，90% 完成全部 10 天
   T2 (2021-22): 投放 326 couples → 主问卷 308 couples (652 人)；日记 288 couples (603 人)，
                 88% 完成全部 10 天；279 couples (571 人) 当时仍已婚
   T3 (2024-25): 主问卷 268 couples (584 人)；日记 260 couples (547 人)，79% 完成 10 天、
                 97% 至少 8 天；249 couples 仍已婚
   **couple 层留存 T1→T3 = 268/419 ≈ 64%**
sampling_inequality (CITED_PRIMARY 原文，本 lane 认为是最有价值的发现之一):
   "Same-sex couples who married between 2004 and 2012 ... were identified through the Massachusetts
    Registry of Vital Records and invited to participate through letters mailed to their address.
    About 70% of same-sex couples were recruited in this way. **Because of restrictions at the
    Massachusetts Registry of Vital Records**, different-sex couples were recruited using publicly
    available demographic city lists in Massachusetts... About 40% of different-sex couples were
    recruited in this way."
   → 同性组与异性组**抽样框不同、招募率不同（70% vs 40%）**。任何「同性 vs 异性」比较都内含选择差异。
   → 这是 LHRM 关心的「数据生成过程本身携带隐藏选择」的一个可核实实例。
intensive_longitudinal:
   唯一同时提供「稀疏面板 (3 点) + 密集日记 (8–10 天 × 3)」的设计。
   T3 因留存压力把日记天数从 10 天降到 8 天 → 密集窗长度本身随时间变化，**wave 不完全可比**。
access_path:  ICPSR 公版；原文 "The public-use data files in this collection are available for access by the
   general public. Access does not require affiliation with an ICPSR member institution."
   ICPSR LLM 政策适用（见 D12/D14 共通条款）
unknown:  **T2/T3 微数据是否已实际 release 无法确认**。ICPSR 落地页仍显示 "Version Date: Jan 4, 2022"
   且标题仍为 "2014-2015"、内容仅描述 T1；`/summary` 与 `/datadocumentation` 索引则显示 2014-2025。
   → `UNKNOWN_AS_OF`（见 §8 矛盾 3）
can_identify_structurally:
   - 双配偶分开作答的关系质量 + 健康 + 日常压力 + 社交互动 + 健康行为
   - 稀疏面板内嵌密集日记 → 可观察 day-level 状态波动（对 LHRM 的 `t` 粒度极有价值）
   - 同性 vs 异性婚内关系状态（须带 §sampling_inequality 的选择警告）
cannot_identify_structurally_without_assumption:
   - 离婚/分居/丧偶后的**新关系**（T2/T3 只续访原配偶身份）
   - 非婚 / 未婚 / 未同居关系（入组硬门槛）
   - 跨文化（单州）
lhrm_impact:  形状上最贴近 LHRM「方向化 + 纵向 + 部分信息 + 密集观测」的候选；
   但「合法已婚 + 同居≥3 年」的入组条件使其**无法覆盖 LHRM 研究域中的陌生起点、非婚、第三方**。
   （`AGENTS.md` §当前架构方向第 2 条明确不预设异性、陌生起点、婚恋目标 → HARP 只能作为**局部**校准源。）
```

### D04 — Fisman & Iyengar Speed Dating Experiment (2002–2004)

```text
structural_verdict:  STRUCTURAL_MEASUREMENT_ONLY（单一时间点）
access_rights_axis:  ACCESS_RESTRICTED_PERMISSIBLE（技术上零门槛可下载，**第三方镜像**；**Columbia 原始数据政策未核实**
                     → 保守按「引用而非再分发」处理，**不是** ACCESS_OPEN）
classification_legacy_equivalent: MEASUREMENT_ONLY（旧单轴标签，保留以便交叉引用；**旧标签不作 canonical 依据**）
canonical_pointer:
  paper:      Fisman, R. & Iyengar, S. "Gender Differences in Mate Selection: Evidence From a Speed
              Dating Experiment" (Columbia Business School)
  mirrors:    https://github.com/datasets/speed-dating      (CSV, HEAD 200 @ 2026-09-27)
              https://www.openml.org/d/40536
              https://osf.io/8k7rf/                         (HEAD 200 @ 2026-09-27)
  reanalysis: Huang, Yeomans, Brooks, Minson & Gino (2017) JPSP, doi 10.1037/pspi0000097 —
              原始数据亦发布于 https://osf.io/8k7rf/
design:  2002–2004 期间 21 场实验速配 session。每位参加者与**每一位异性参加者**进行 4 分钟「first date」。
        每段结束时该参加者被问: 是否想再见该对象 (dec) + 在 6 个属性上评分
        (Attractiveness, Sincerity, Intelligence, Fun, Ambition, Shared Interests)。
        另有 session 前后问卷（人口、约会习惯、自我知觉、择偶信念、生活方式）。
        `match` = 双方都想再见的互惠标记。
directionality:  **本 lane 找到的最好的方向性非对称公开样本**。
        同一 (i,j) 上同时有 i 对 j 的 6 项评分 + i 的再意愿，和 j 对 i 的 6 项评分 + j 的再意愿。
        → Z[k,i,j] 与 Z[k,j,i] 在同一 dyad、同一时刻直接可测，无需任何外部假设。
waves:     `wave` = session 编号（21 场），**不是对同一 dyad 的重复观测**。
        跨场次的是不同的人，不是同一对人的第 2 次约会。
        → 只能标定 t=0 的方向性，**不能标定任何转移律、任何持续性、任何路径依赖**。
outcomes:  极弱。仅「想不想再见」。无后续接触、无关系持续、无健康/行为后果。
sample_selection:  自我选择 + 城市 + 单一机构（Columbia）活动参加者。
        本 lane 未找到官方 sampling/attrition 文档 → missingness 文档视为 **弱**。
cohort_diversity:  "every other participant of the opposite sex" → **异性单性**。无同性配对。
codebook:  "Speed Dating Data Key.doc" 随数据集发布
access:    **完全公开，无注册**。这是本 landscape 中唯一的零门槛数据。
can_identify_structurally:
   - 方向性不对称在**最短交互时间尺度**上的经验分布
   - mutuality / reciprocity 作为**派生量**的真实可观测性（match = dec_i AND dec_j）
   - 感知属性与自身属性的不对称（对方吸引 i ↔ i 自我知觉）
cannot_identify_structurally:
   - 任何时间演化、持续性、惯性、路径依赖
   - 关系建立后的任何状态
   - 同性配对
   - 一般人群（自我选择的速配参加者）
lhrm_impact:  **对 LHRM 的价值不在参数，在拓扑**。
   它是唯一能证明「Z[i→j] 与 Z[j→i] 在真实数据中确实是两个不同自由度」的数据集，
   可作为 `Mutuality = H(Desire(i→j), Desire(j→i))` 与 `Asymmetry = d(·,·)` 的**存在性证据**，
   而非取值证据。把 4 分钟速配的评分当 attraction 的量纲是越界。
```

### D05 — DHS Couples (CR) file

```text
structural_verdict:  STRUCTURAL_MEASUREMENT_ONLY（每国单轮）
access_rights_axis:  ACCESS_RESTRICTED_PERMISSIBLE（免费；电子注册 + 授权）
classification_legacy_equivalent: MEASUREMENT_ONLY（旧单轴标签，保留以便交叉引用；**旧标签不作 canonical 依据**）
canonical_pointer:
  guide:  https://dhsprogram.com/data/Guide-to-DHS-Statistics/Analyzing_DHS_Data.htm
  merge:  https://www.dhsprogram.com/data/Merging-Datasets.cfm
  guide8: https://dhsprogram.com/pubs/pdf/DHSG1/Guide_to_DHS_Statistics_DHS-8.pdf
  mr19:   https://dhsprogram.com/pubs/pdf/mr19/mr19.pdf
unit_of_analysis (CITED_PRIMARY 原文):
   "For each DHS survey that includes a survey of men as well as a survey of women, a 'couples' file is
    constructed, consisting of a single record for each co-resident woman and man who self-identify
    as partners."
   "The ID for couples is that of the woman (caseid - as opposed to mcaseid for the man) because in
    polygynous countries a man can be the partner for more than one woman."
   → 官方分析单位就是 couple；配对依据是**双方互相声明的伴侣关系**（不是分析者推断）。
dyad_identifiability:  STRONG，但**非共居、非事实婚姻制外的 partner 不覆盖**。
cross_cultural:       **本 landscape 中最强**（约 90 个 DHS 参与国；跨国 recode 变量命名标准化）
waves:                **每国单轮**。跨文化覆盖靠「多国同轮」而非「同国多轮」→ 无法识别动态。
directionality:  SUPPORTED（双方都在同一 record）。官方 MR19 直接做跨人不对称测量:
   "the data include the person's own age and the person's report (estimate) of their partner's age ...
    the correspondence between a respondent's reported age and their spouse's estimate of the
    respondent's age in 113 surveys for men and 67 surveys for women."
   → 这是一个**可核实的方法学先例**：DHS 官方就把「我报你的年龄」与「你自报年龄」当两个不同测量对象。
      正是 LHRM 的 `Observation != Belief` 与方向性分离在人口统计层面的实例。
outcomes:  强。生育、避孕、HIV 状态、健康利用、决策权、暴力、收入。
negative_result (本 lane 记录的诚实反面):
   DHS 官方 user forum 记录了一次明确失败: "A couples dataset could not be generated since the household
   line number of the wife/partner (used to create variable MV034 and to link the man with his wife/partner)
   was not recorded in the Man's Questionnaire."
   → **「DHS 有 couples 数据」必须降级为「逐轮/逐国需查，不能默认」**。
access:  免费；电子注册 + 授权（Guide 原文: "DHS policy is to release survey data to researchers after
   [the] main survey report is published, generally within 12 months after the end of fieldwork"）。
can_identify_structurally:
   - 跨约 90 国的双人自报配对测量；决策权/避孕/暴力等**天然方向性**的题项
   - 跨人感知误差（配偶年龄互评）
cannot_identify_structurally:
   - 任何时间演化
   - 非 co-resident 伴侣
   - 同性配对（制度性缺失）
lhrm_impact:  **REPRESENTATION 覆盖面工具，而非校准工具**。
   它能证明 LHRM 的方向性坐标在任何一种人类学文化里都有真实对应物（不只西方恋爱样本），
   但不能提供任何动态信息。
```

### D06 — Indonesia Family Life Survey (IFLS1–IFLS5)

```text
structural_verdict:  STRUCTURAL_MEASUREMENT_ONLY（方向性依赖 spouse 重建假设，见 §2 的 SOEP/IFLS 边界）
access_rights_axis:  ACCESS_RESTRICTED_PERMISSIBLE（免费；RAND 注册 + confidentiality declaration）；**未见专门 AI / LLM 条文**
classification_legacy_equivalent: MEASUREMENT_ONLY（旧单轴标签，保留以便交叉引用；**旧标签不作 canonical 依据**）
canonical_pointer:
  design:      https://www.rand.org/health/surveys/FLS/IFLS/study.html
  datanotes:   https://www.rand.org/health/surveys/FLS/IFLS/datanotes.html
  userguide5v2: https://www.rand.org/content/dam/rand/pubs/working_papers/WR1100/WR1143z2/RAND_WR1143z2.pdf
  access:      https://www.rand.org/health/surveys/FLS/IFLS/access.html
waves (CITED_PRIMARY 实地日期原文):
  IFLS1   Sept 1993 – Feb 1994     (7,224 households; 22,000 individual interviews)
  IFLS2   Aug–Dec 1997 + long-distance tracking to Mar 1998
  IFLS2+  1998  (25% subsample, 衡量亚洲金融危机即时冲击)
  IFLS3   late Jun – end Oct 2000 + tracking to end Dec 2000 (10,574 户接触 / 10,435 户实访;
          95.3% IFLS1 户再接触率; 90.9% 的 IFLS1 户在 IFLS1/2/3 三波全在)
  IFLS4   late Nov 2007 – end Apr 2008 + tracking to end May 2008
  IFLS5   late Oct 2014 – end Apr 2015 + tracking to end Aug 2015
          (16,204 households; 50,148 individuals; 另有 2,662 份由熟悉者的代理退出访谈)
dyad_identifiability:  **UNVERIFIED（U8）**。
  官方 FAQ 明确: "Users should look at the IFLS2 User's Guide as it talks about family relationships and how
  to identify spouses, children, and parents across modules. That information holds for all IFLS waves."
  → 识别 spouse 是**官方指引的构造过程**，不是发货的现成 partner id。
  → 后果: Z[k,i,j,t] 的 i/j 绑定依赖分析者的重建规则 → **方向性依赖重建假设**（模型假设，不是证据）
  → 本 lane 明确不主张 IFLS 存在跨波 partner id 变量。
codebook:  每波 6–7 卷（overview & field report / user's guide / 问卷 / 问卷交叉表 / codebook）
  + IFLS1-IFLS2 crosswalk + IFLS1-RR 重发布说明（专为跨波链接而设）
kin_coverage:  **强**。BA (Non-Coresident Family Roster) + TF (Transfers) 模块 → 非同住亲属 + 家庭内转移
   IFLS1-IFLS2 问卷目录: "3.14. Section BA (Non-Coresident Family Roster and Transfers) ... 4.15. Section TF (Transfers)"
data_hygiene_note:  IFLS 官方采取 "not over-cleaning" 政策，另发 `fixes` 文件列出疑似错误值 ——
   这本身是 LHRM「Unknown 必须显式」原则的**真实数据工程对应物**：官方都不确定的值，不应被默默填补。
access:  免费；RAND 注册。
   条款原文: "Please do not distribute these data. The data are freely available on our website."
   confidentiality declaration 必签: "The IFLS data are placed in the public domain to support research
   analyses. As a user of the IFLS public use files, you are expected to respect the anonymity of all our
   respondents."
   受限项: "Community coordinates and village-level BPS codes are restricted data and must be separately requested."
cross_cultural:  印尼 13 省 ≈ 全国 83% 人口。**单国**，但内部文化多样性高。跨文化价值在于「非西方 +
   高多样性」，不在于跨国比较。
can_identify_structurally:
   - 5 波跨 21 年的家庭结构、婚育、迁移、健康、经济、亲属转移（含非同住）
   - 印尼语境下的家庭 dyad 与照护流动
cannot_identify_structurally_without_assumption:
   - 任何 i→j vs j→i 的关系状态分解（除非接受 spouse 重建假设）
   - 同性 dyad（未专项，且家庭问卷以户主-配偶为轴）
lhrm_impact:  提供「非西方、非个人主义语境下关系状态如何被登记」的对照；
   但因方向性需假设，不应被当作方向性证据。
```

### D07 — Growing Up in New Zealand (GUiNZ)

```text
structural_verdict:  STRUCTURAL_MEASUREMENT_ONLY（以儿童-家长为中心，成人伴侣间双报告不覆盖）
access_rights_axis:  ACCESS_RESTRICTED_PERMISSIBLE + **输出预审义务** + **Kaitiakitanga 数据主权约束**（后者**独立于** access，见 §2.2）
classification_legacy_equivalent: MEASUREMENT_ONLY（旧单轴标签，保留以便交叉引用；**旧标签不作 canonical 依据**）
canonical_pointer:
  home:         https://www.growingup.co.nz/
  access:       https://www.growingup.co.nz/data-access-application-growing-up-in-new-zealand
  docs:         https://www.growingup.co.nz/available-data-disclaimer   (需先接受 legal disclaimer)
  protocol:     Data Access Protocol 2026 v1.0 (PDF, 官方站内链接)
  output_guide: Data Output Guide v1.3, July 2026 (PDF, 官方站内链接)
cohort:   Aotearoa 最大纵向儿童健康与福祉研究，>6,000 rangatahi 及其家庭
waves:    自 2009 起多个年龄点；官方 nav 显示 birth / 2y / 4.5y / 6y / 8y / 10y / 12y / 15y
          + "17 Year Data Collection"（官网新闻 2026-05-01: "Growing Up in New Zealand begins its
          17-Year Data Collection"）+ Extreme Weather Survey + 15 Year Catch-Up
dyad_coverage:  家庭成员 id 齐 → 亲子 dyad、同住伴侣 dyad、青少年-家长 dyad。
   官方另有 StatsNZ IDI linkage 子样本。
access_path (CITED_PRIMARY 原文流程):
   1. 确认研究方案符合 criteria（含 Data Access Protocol）
   2. 填 Data Access Application（项目起止、摘要、背景、目标、方法、所需数据集与变量、理由、
      **Kaitiaki 承诺大纲**、产出、需访问人员名单）
   3. Data Access Coordinator 10 工作日内初审
   4. **Data Access Committee** 审议（成员含 GUiNZ、Kaitiaki Group、University of Auckland、
      MSD、Ministry of Health、Stats NZ、Ministry of Education）→ 书面接受/拒绝
   5. 签 Data Access Agreement（由 PI 代表全体成员签）
   6. 经 Secure Data Access Platform 开通（需 UoA 登录），按项目期限授权
   7. **产出前须按 Data Output Guide 提交预审，checking 最多 4 工作日方可发布**
hard_constraints (CITED_PRIMARY 原文，本 lane 视为独立于许可的伦理/主权约束):
   "the Principal Investigator (PI) needs to be based at and affiliated with a research institution that
    is located in Aotearoa New Zealand **as a prerequisite to ensure Kaitiakitanga is upheld**"
   "Growing Up in New Zealand data is held securely by two organisations" (University of Auckland 全队列;
    Stats NZ 子样本经同意后进 IDI，受 Stats NZ 协议 + "5 Safes" 约束)
   → 这不是 licence 问题，是**数据主权问题**。LHRM 任何跨境或纯 AI 化的使用方案都需先与之协商。
can_identify_structurally:
   - 多族裔（Māori / Pacific / 移民社群）语境下的亲子与青少年家庭 dyad 纵向
   - 青少年非婚关系、同住伴侣的形成
   - 家庭层面的事件（极端天气等）对关系/照护的冲击
cannot_identify_structurally:
   - 成人伴侣间的双方自报关系状态（本研究以儿童-家长为中心）
   - 同性伴侣的双报告（未专项）
   - 跨国可比性（单国）
lhrm_impact:  **对 LHRM 的独特价值是「关系尚未成为恋爱关系」这一时段**——
   `AGENTS.md` 明确「不预设异性、陌生起点、婚恋目标」，而 GUiNZ 提供的正是关系未定型阶段。
   但 PI 属地限制 + 输出预审 + Kaitiakitanga 使其**几乎不可能**作为 LHRM 验证流水线的数据源。
   更可能的角色是**伦理/主权先例参考**。
```

### D08 — National Survey of Families and Households (NSFH, Wave 1–3)

```text
structural_verdict:  STRUCTURAL_MEASUREMENT_ONLY（亲子方向可测；配偶间 Wave 1 单方已核实、Wave 2+ `UNKNOWN_AS_OF`）
access_rights_axis:  ACCESS_RESTRICTED_PERMISSIBLE（ICPSR/Child & Family Data Archive 公版；地码版 restricted）
                     + ICPSR 再分发 / LLM policy（**R3-A3b 已直开**，见 §5.1a）
classification_legacy_equivalent: MEASUREMENT_ONLY（旧单轴标签，保留以便交叉引用；**旧标签不作 canonical 依据**）
canonical_pointer:
  series_icpsr:  https://www.icpsr.umich.edu/web/ICPSR/series/193
  wave2_icpsr:   https://www.icpsr.umich.edu/web/DSDR/studies/6906
  cfda:          https://www.childandfamilydataarchive.org/cfda/cfda/series/193
  design_paper:  Seltzer, Bachrach, Bianchi, Bledsoe, Casper, Chase-Lansdale et al. (2005)
                 "Explaining Family Change and Variation: Challenges for Family Demographers",
                 JMF 67(4):908–925
waves (CITED_PRIMARY 原文):
  Wave 1: 1987–1988（第一波即含 5 年随访设计）  |  Wave 2: 1992–1994  |  Wave 3: 2001-02 或 2001-03
  (ICPSR series 页记 "2001-2002"；NIH grant R03-AG045503-01 记 "2001-2003"。→ 官方内部年份不一致，见 §8 矛盾 2)
multi_member_design (CITED_PRIMARY 原文，Wave 1):
  "One adult per household was randomly selected as the primary respondent, and there was a total of
   13,007 respondents. In addition to the main interview conducted with the primary respondent, a
   shorter, self-administered questionnaire was given to the spouse or cohabitating partner, and also
   administered to the householder if he or she was a relative of the primary respondent."
  (Wave 1 样本: 9,643 户主样本 + 对黑人/波多黎各人/墨西哥裔美国人/单亲/继子女家庭与同居或新婚夫妇的双重抽样)
  Wave 2 组件: (1) 原样本存活成员面访 (2) **现任配偶或同居伴侣**的几乎相同的完整个人访谈
               (3) 关系已终止时**原配偶/原伴侣**的个人访谈 (4)(5) focal children 电话访谈
               (6) 代理访谈 (7) **随机一名受访者的家长**电话访谈
  Wave 3 组件: 原主受访者 + 有合格 focal child 的配偶/伴侣 + focal children（现 18–34 岁）
directionality_critical_note (R3-A3b 收窄; 依 review-r2 `R-C16` / `C-C35` `CONTESTED`):
   **被取代的原文**（逐字保留）:
      "**配偶关系质量是单方报告**。主受访者被问 "Respondents were also asked about the relationship of
       household members to each other and the quality of their relationships with their parents, children,
       and in-laws."
       → 配偶**之间**的关系状态由一个人报告。→ **Z[i→j] 与 Z[j→i] 在 NSFH 中不可分离。**"
   **R3-A3b 收窄后的表述**:
      "**Wave 1 单方报告（已核实）**。支撑它的**唯一**一句是 Wave 1 questionnaire 的一句措辞：
       "Respondents were also asked about the relationship of household members to each other and the
       quality of their relationships with their parents, children, and in-laws."
       这句话在**结构上**只要求 primary respondent 作答，因而**在 Wave 1** 支持「配偶间关系状态为
       单方报告」的读法。
      **Wave 2 及以后：未核实（`UNKNOWN_AS_OF`）。** 旧版把 Wave 1 的单句措辞**外推**到整个 W1–W3
      series。**本 packet 未打开 Wave 2 / Wave 3 的 questionnaire 措辞**，因此：
      - **不主张** NSFH 的配偶关系质量在 Wave 2 / Wave 3 是双报告；
      - **也不主张**它是单方报告。
      **该不确定性必须随任何 NSFH 方向性主张携带。**"
   **保留的、与之无关的方向性资产（不受上述限定影响）**:
      亲子 / 跨代方向**在结构上可测** —— Wave 1 有 focal children 电话访谈 + 关系质量题;
      Wave 2 组件含"**随机一名受访者的家长**"电话访谈; Wave 3 含现 18–34 岁的 focal children。
      ⇒ `Z[parent→child, child→parent]` 有独立测量来源，**不需要**外推 Wave 1 的措辞。
   **R3-A3b 明确不主张**: 不主张 NSFH 的方向性能力在 Wave 之间发生变化；只主张
   **本 packet 只有 Wave 1 的措辞证据**，其余波次为 `UNKNOWN_AS_OF`。
can_identify_structurally:
   - 亲子 dyad 的方向性（家长→子、子→家长；跨代关系质量；非同住父/母联系）
   - 3 波的关系/同居/离婚/再婚/继亲/监护事件史
   - 同居（非婚）家庭
   - **Wave 1 的**配偶间关系状态（单方报告 → pair fact）
cannot_identify_structurally:
   - 同性关系
cannot_identify_structurally_VERIFICATION_DEPENDENT:
   - 配偶间关系状态在 **Wave 2 / Wave 3** 的方向性 → `UNKNOWN_AS_OF`（见上）
structural_dependencies_unverified:
   - 同居伴侣问卷在 Wave 2 的覆盖是否同样为单方 → `UNKNOWN`
lhrm_impact:  **NSFH 印证 `AGENTS.md` 的一个架构判断**：
   在最著名的家庭纵向调查里，**至少 Wave 1** 的「关系质量」是单方报告的。
   这说明 LHRM 的 `Z[k,i,j,t]` 双报告要求在**大规模代表性调查**里难以满足，
   只能在**专门为双人设计的研究**（pairfam / SHARE / HARP）里满足。
   → 对参数收敛的含义：**LHRM 的方向性 primitive 可能在窄样本上标定，而不能在宽样本上验证。**
   （此为 observation，非建议。）
   **R3-A3b 限定**: 该推论的证据基础是 **Wave 1 的一句 questionnaire 措辞**。作为「现象存在」的
   observation 它成立；作为「**大规模代表性调查一律单方报告**」的一般化，它**超出本 packet 的证据**，
   且 NSFH **不是**大规模代表性调查（Wave 1 有针对黑人/波多黎各人/墨西哥裔美国人/单亲/继子女家庭
   与同居或新婚夫妇的**双重抽样**，是**过抽样**设计，不是概率抽样）⇒ 旧版「最著名的家庭纵向调查」
   这一定位本身在**抽样框**上不准确。**本 packet 不主张** NSFH 可代表任何总体。
codebook:  PI Codebook（+ Appendix O: NSFH2 Final Weights and Weighting Procedure）、DDI XML、
   ASCII/R/SPSS/SAS/Stata + PDF 文档
access:  "The public-use data files in this collection are available for access by the general public.
   Access does not require affiliation with an ICPSR member institution."
   三波地码版为 **restricted-use**（ICPSR 严程序）
   **R3-A3b**: 本 packet **未重开** 该 ICPSR 页面（旧 report 记 icpsr.umich.edu 全站 403）；
   该引文标 `CITED_PRIMARY (relay, 未由 R3-A3b 重开)`。**ICPSR 的再分发要求见 §5.1a。**
cross_cultural:  仅美国
same_sex:  **否**（1987 起采集，同性婚姻不存在）
```

### D09 — Changing Lives of Older Couples (CLOC) · ICPSR 3370

```text
structural_verdict:  STRUCTURAL_MEASUREMENT_ONLY
access_rights_axis:  ACCESS_RESTRICTED_PERMISSIBLE（ICPSR，但**限 member institution**）
classification_legacy_equivalent: MEASUREMENT_ONLY（旧单轴标签，保留以便交叉引用；**旧标签不作 canonical 依据**）
CLOC_justification_matching_criteria (R3-A3b 重写; 依派工 item 14):
   **被取代的 justification**（旧版隐含）: 旧版把 `MEASUREMENT_ONLY` 的理由写成
      "→ **随访对象 = 丧偶者 + 匹配对照**。这是一个**条件于丧偶**的样本，不能读作「一般老年婚姻样本」"
   **问题**: 「样本条件于丧偶」是一条**外推限制**（external-validity limitation），
   **不是**本报告 §2.1 所定义的 `STRUCTURAL_MEASUREMENT_ONLY` 判据。
   §2.1 对该类的定义是「缺 1 wave / 双方测量不对称需外部假设 / 只有 pair-level 事实 /
   outcome 无后续时点」—— 四条结构性判据。
   **R3-A3b 按判据逐条重判（可复现）**:
   | §2.1 判据 | CLOC 是否满足 | 证据 |
   |---|---|---|
   | 稳定 dyad id | **是** | Part 5 含 423 couples / 846 人；妻 `V*` + 夫 `S*` 同 record |
   | **双方各自作答** | **是** | 逐字: "contains data collected from **both the husband and the wife** of 423 couples (n = 846)" |
   | ≥3 wave | **是** | baseline + 3 个随访（6 / 18 / 48 月）= 4 个时点 |
   | codebook | **是** | 6 个子数据集 + 各年 codebook 文件 |
   | outcome/event | **是** | 丧偶事件本身即 outcome，3 个随访时点 |
   | 缺失/选择文档 | **是** | NDI + 州死亡记录核销；matched control 设计 |
   | 可复现获取路径 | **部分** | "freely available to data users at **ICPSR member institutions**" → 非成员无路径（→ 归 `access_rights_axis`，不归结构轴） |
   ⇒ **七项结构判据中六项满足**，第七项是访问问题。**按报告自己写下的判据，CLOC 不满足
   `STRUCTURAL_MEASUREMENT_ONLY`。**
   **但仍不升为 `STRUCTURAL_CALIBRATION_CANDIDATE`**，理由是**另一条**（同样是结构性的）:
     **Part 5 "Couples Only" 子集是 423 couples / 846 人的一个子样本，而完整样本是 1,532 人。**
     该子集是 baseline 时**双方均在册且均完成全部四波**的那部分 —— 即**按完整留存筛选过的样本**。
     这使得 dyad 层的人内演化与 dyad 间的构成都与总体不同。
     ⚠️ **该子集的精确选择规则原文 R3-A3b 未取得** ⇒ 这一理由本身标 `PLAUSIBLE`，
     **不作为升/降级的决定性依据**。
   **因此（R3-A3b 的现行判定）**:
      `structural_verdict` = **`STRUCTURAL_MEASUREMENT_ONLY_PENDING`**（**待判定**）
      理由: 按 §2.1 的字面判据它应当更高；按"是否为留存筛选子样本"它应当更低；
            而**支持任一方向的一手证据都未在本 packet 取得**。
   **明确不主张（避免把"待判定"读成任一方向的结论）**:
      - **不主张** CLOC 是 `CALIBRATION_READY`（旧标签）—— 该判定所需的"双方各自作答 + ≥3 wave"虽满足，
        但**构念内容**（U15）与**选择规则**均未核实。
      - **不主张** CLOC 只是"一个条件于丧偶的样本"（那是外推限制，不是结构判据）。
      - **不主张** CLOC 不可用于方向化纵向标定。
      **复通条件（可执行）**: 取得 (a) "Couples Only" 子集的选择规则原文;
      (b) 1,532 与 846 之间的排除原因分布; (c) Part 5 的 codebook 中关系状态类题项清单（解 U15）。
canonical_pointer:  https://www.icpsr.umich.edu/web/ICPSR/studies/3370
   **R3-A3b 抓取记录**: `icpsr.umich.edu` 本轮**未**返回 403 —— §5.1a 的 ICPSR LLM policy 页与
   Redistribution Policy 页**均直开成功**（见 §5.1a）。但**本研究的落地页 `/studies/3370`
   R3-A3b 未单独重开** ⇒ 该 study 页内文仍标 `CITED_PRIMARY (relay)`。
waves (CITED_PRIMARY 原文):
  baseline 面访 1987-06 – 1988-04
  follow-up: 配偶死亡后 6 个月 (Wave 1)、18 个月 (Wave 2)、48 个月 (Wave 3)
  配偶死亡监测: "using state-provided monthly death records and through daily obituaries from local area
   newspapers. The National Death Index (NDI) and direct ascertainment of death certificates were used to
   confirm all deaths."
dyad_structure:
  完整样本 1,532 人
  **Part 5 "Couples Only" 数据集: "contains data collected from both the husband and the wife of 423 couples
   (n = 846) and includes all available data from all four waves of data collection (baseline, W1, W2, W3).
   Each record contains data for the wife (the 'V' variables) and data for the husband (the 'S' variables)."**
  → **这是本 lane 找到的「最早、最干净的双人同 record 四波设计」**（1987–1993），比 pairfam 早 15 年。
  MacBat 生理/内分泌/生化子样本 n = 432
measures:
  - 专为本研究编制的 global grief scale + **6 个哀伤分量表**
  - 每一波都用三种抑郁概念化 + DSM-III-R 重性抑郁发作
  - 人口 / 财务 / 住房 / 生活事件 / 社会支持 / 工作与活动 / 婚姻与家庭 / 宗教 / 健康与福祉
outcomes:  强（丧偶事件本身即 outcome，且有 3 个随访时点）
selection (CITED_PRIMARY 设计本质):
  "Each widowed person was assigned a same-age, same-sex, same-race matched control from the baseline
   sample. Controls were interviewed again at each of the three follow-ups as well."
  → **随访对象 = 丧偶者 + 匹配对照**。这是一个**条件于丧偶**的样本，
     不能读作「一般老年婚姻样本」。存活-与丧偶-条件化的选择必须显式写入任何分析。
access:  "These data are freely available to data users at ICPSR member institutions."
   → **限 member institution**。非成员需另议。
   **R3-A3b**: 本 packet **未重开**该 study 页的 access 段（ICPSR policy 两页已直开，见 §5.1a）。
   **新增的、已直开的 ICPSR 级要求（对本卡同样适用）**:
   (i) 任何再分发须先经 **Data Stewardship Policy Committee** 批准（逐字见 §5.1a）;
   (ii) "for data deposited by **individual investigators** … these studies are **available to members
   only and cannot be redistributed**"（逐字见 §5.1a）;
   (iii) CLOC 适用 **ICPSR LLM policy**：Type 1 = None；Type 2 = Public-Use；Type 3 = Public + Restricted
   （逐字见 §5.1a），且 "Providing ICPSR data to any large language model (LLM) which retains data …
   **is redistribution of ICPSR data and is barred by our terms of use**"。
   **R3-A3b 未取得的信息**: CLOC 是否属 "deposited by individual investigators" 一类
   ⇒ 该分句是否适用**未核实**（`UNKNOWN`）。**不主张**其适用，**也不主张**其不适用。
can_identify_structurally:
   - 丧失事件前后、双人同 record 的多波状态演化（照护 → 丧失 → 哀伤轨迹）
   - 双人方向性在同一 record 内可直接估计（V 变量 vs S 变量）
cannot_identify_structurally:
   - 新配对关系（不观测重组）
   - 跨文化（Detroit SMSA）
   - 条件于丧偶 + 存活的一般婚姻过程
structural_dependencies_unverified:
   - "Couples Only" 423 couples 子集的选择规则（见 CLOC_justification_matching_criteria）
   - 关系状态构念内容（U15）
lhrm_impact:  提供 **caregiving / illness / bereavement** 这条 LHRM 明确需要的轴，
   且提供「关系终点」的可观测事件。可作为极端案例的 stress test 参照
   （`AGENTS.md`："Extreme real-world cases are stress tests for representation and dynamics"），
   但不能作为一般转移律的标定源。
   **R3-A3b 限定**: 「不能作为一般转移律的标定源」的依据是**样本条件于丧偶 + Detroit SMSA 单城**
   这两条**外推限制**（不是结构判据）。作为 `MEASUREMENT_ONLY` / `MEASUREMENT_ONLY_PENDING` 的
   判定理由**不使用**这两条（见上）。两者在文中分开记账。
```

> **R3-A3b 关于 `D09` 的一条通则（适用于本文件全部卡片）**
>
> 本文件多处把**外推限制**（样本条件于事件、单城、单州、异性单性、50+ 门槛、已过抽样设计）
> 与**结构判据**（双方各自作答、波次数、pair-level 不可分解、outcome 无后续时点）
> 混写在同一个 `classification` 字段的 justification 里。R3-A3b 的处置：
> **外推限制一律归入 `cannot_identify_structurally` 的说明性条目或 `lhrm_impact`，并显式标注
> "外推限制，非结构判据"；`structural_verdict` 的 justification 只允许引用 §2.1 的四类结构判据
> 加 dyad id / codebook / 缺失文档三项。** 这不是对 D09 的特例处置，是对全文件记账口径的统一。

### D10 — Health and Retirement Study (HRS)

```text
structural_verdict:  STRUCTURAL_MEASUREMENT_ONLY
access_rights_axis:  ACCESS_RESTRICTED_PERMISSIBLE（公版免费 + DUA）但 **AI/LLM 用途 = ACCESS_BLOCKED_USE_CONDITION**
                     （见 critical_rights_finding_ai_llm；分级由旧版「含新政策（未知）」改为「**禁止**」）
classification_legacy_equivalent: MEASUREMENT_ONLY（旧单轴标签，保留以便交叉引用；**旧标签不作 canonical 依据**）
canonical_pointer:
  home:          https://hrs.isr.umich.edu/
  data_products: https://hrs.isr.umich.edu/data-products
  file_merge:    https://hrs.isr.umich.edu/data-products/file-merge-reference
  rda_pdf:       https://hrs.isr.umich.edu/sites/default/files/rda-forms/HRS-RDA-MiCDA-Access-Agreement.pdf
  faqs:          https://hrs.isr.umich.edu/data-products/restricted-data/faqs
  cou:           https://hrsdata.isr.umich.edu/data-products/conditions-of-use
                 **R3-A3b 抓取记录：HTTP 403（2026-09-27）；备选 host `hrs.isr.umich.edu/data-products/conditions-of-use` 亦 403。
                  ⇒ `UNVERIFIABLE_HERE`。下面的 AI/LLM 条文是【转述 lane C 的直开结果 C-C11 / H-C1】，不是 R3-A3b 的直开核实。**
scope:  "longitudinal panel study that surveys a representative sample of approximately 20,000 people in
   America, supported by the National Institute on Aging (NIA U01AG009740) and the Social Security
   Administration."
directionality_asset (本 lane 判断):
   HRS 的价值不在「关系状态自报」，而在**配偶 ADL/IADL 协助题天然是方向性照护行为测量**：
   谁帮助谁、哪一类活动、频率。这正是 `CONSTRUCT_SCOPE_DIRECTIONALITY.md` §示例 C 的
   `Caregiving_(i->j)` vs `CareNeed_j` 的可观测对应物。
   同时配偶常充当 proxy respondent → 兼有「信息源即关系成员」这一 LHRM 关心的结构。
access (CITED_PRIMARY):
   公版: 注册 + DUA（免费）
   restricted: RDA + institutional counter-signed confidentiality agreement + **proof of current federal
     funding** + **proof of current human subjects review (IRB)** + research plan + data security plan
     （传统许可）
   导出限制: "No research identifiable information (anything at respondent level) may ever be exported.
     Enclave users may only export statistical summary information."
   地理: "prohibited from publishing results that identify geographic areas below the level of Census Division"
   合并: "Merging Social Security administrative data with Geographic Information is PROHIBITED for
     traditional license users."
critical_rights_finding (CITED_PRIMARY, RDA PDF 原文):
   "The Health and Retirement Study (HRS) is protected by a **Certificate of Confidentiality** issued by
    the National Institutes of Health (NIH). Under this Certificate, investigators and others who have
    access to HRS restricted data are **prohibited from disclosing identifiable, sensitive information
    about research participants in any civil, criminal, administrative, legislative, or other proceedings
    at the federal, state, or local level. This protection applies even under court order or subpoena.**"
   → **对 LHRM Case Bank 的直接后果**：若某 Case Bank 项拟走 FOIA / 司法调取途径，
     HRS restricted 数据**在任何法院命令下都不得披露**。这与
     `VALIDATION_CORPUS_V0_1.md` 偏好的「官方法院文书」路线**互斥**。
critical_rights_finding_ai_llm (R3-A3b 改判; CITED_SECONDARY — 依 review-r2 R-C4 / C-C11 + H-C1):
   **被取代的原文**（逐字保留）:
      "**HRS CoU（更新于 2026-02-04）关于 AI/LLM 的具体条文未取得**（页面 banner 原文已核实：…）。
       → `UNKNOWN_AS_OF`（U4）。**不得猜测条文内容。**"
   **取代它的表述**:
      HRS Conditions of Use（更新 2026-02-04）**含完整的 AI / LLM 禁令**：CoU
      **逐字禁止 AI 程序与 LLM 与 HRS 数据同用，且点名 open-source AI**。
      旧版把该页的 banner（"…which include a new policy on use of AI and Large Language Models"）
      读成"政策存在但内容未知"——**banner 本身已说明这是一份新政策，而 lane C 直开该页后确认
      其内容为全面禁止。**
      ⇒ **U4 由 `UNKNOWN_AS_OF` 改为「已解（resolved）」。HRS 的 AI/LLM 分级由「含新政策（未知）」
      改为「**禁止**」（`ACCESS_BLOCKED_USE_CONDITION`）。**
   **R3-A3b 的抓取状态（如实记录）**:
      R3-A3b 于 2026-09-27 两次尝试打开 `https://hrsdata.isr.umich.edu/data-products/conditions-of-use`
      与 `https://hrs.isr.umich.edu/data-products/conditions-of-use`，**均返回 HTTP 403**。
      ⇒ **R3-A3b 标 `UNVERIFIABLE_HERE`，不冒充直开核实。** 上面的条文内容是
      **lane `C` 的直开结果（`C-C11`，经 `H-C1` 判 `VERIFIED`）的转述**。
      **判 `resolved` 的依据是 review-r2 的 `R-C4` 裁决（"不可得前提已被推翻"），不是 R3-A3b 自己的抓取。**
   **失败记录的处置（R-0.9 的核心）**:
      `hrs.isr.umich.edu` 的 timeout / 403 **仍然如实保留在 §8.6 与 §12**，
      但其**后果被高估**的部分已删除：旧版由"抓不到"推出"**条文未知**"，这一推论**不成立** ——
      **抓取失败是访问限制，不是关于政策内容的本体/证据结论**（adjudication §C item 6）。
   **明确不主张**: R3-A3b 不主张自己已核实该条文；不主张该禁令的具体措辞；
   也不主张 HRS 政策此后未再变更（**日期戳 2026-02-04 必须随引用保留**）。
unknown:
   - HRS 是否发货跨波稳定的 partner/couple id → `UNKNOWN`（U5）
   - **R3-A3b 新增 U17**: R3-A3b 未能直开 CoU 页 ⇒ 若要把该禁令用于任何**可执行的**
     合规动作（例如写进 DUA 申请模板），须由能打开该页的人再取一次逐字文本。
can_identify_structurally:
   - 方向性照护行为（照护方 → 被照护方）、跨双年面板
   - 双成员互相代理作答这一「信息源即关系成员」结构
cannot_identify_structurally:
   - 关系状态自报（SHARE/HRS 都不是关系质量面板）
cannot_identify_for_LHRM_use（权利轴）:
   - **AI / LLM 与个体级 HRS 数据的任何同用 —— CoU 全面禁止**
   - respondent-level 信息的任何导出（即使在 enclave 内）
   - 受 Certificate of Confidentiality 约束的任何披露，包括法院命令下
structural_dependencies_unverified:
   - 跨波 partner id 绑定（未核实）
lhrm_impact:  **rights 层面比统计层面更重要。**
   HRS 的 NIH Certificate of Confidentiality 是本 lane 找到的**对 Case Bank 路线最硬的单点约束**：
   它意味着即便法院命令，HRS restricted 也不能作为 Case Bank 材料披露。
   **R3-A3b 追加**: CoU 的 AI/LLM 全面禁令使 HRS 成为一个明确的**排除项**而非"待定项"——
   按 adjudication **§C item 7（Rights fail closed）**，即便未来条文允许某类使用，
   在**重获逐字条文并记录日期戳**之前，HRS 仍按"AI 不可用"处理。
   建议 Architect 把 Certificate of Confidentiality 这一条写进 Case Bank 的选材规则。
```

### D11 — SOEP (German Socio-Economic Panel)

```text
structural_verdict:  STRUCTURAL_NOT_DYADIC_ENOUGH（旧单轴标签；**旧标签不作 canonical 依据**）
access_rights_axis:  ACCESS_RESTRICTED_PERMISSIBLE（需向 DIW 申请）+ **AI/LLM 用途 = ACCESS_BLOCKED_USE_CONDITION**
                     （SOEP AI and LLM Use Policy: Type 1/2/3 **全 None**；**R3-A3b 未直开**，见下）
SOEP_ifls_boundary (R3-A3b 新增; 依派工 item 14「make the boundary explicit and single」):
   **本文件此前对 SOEP 与 IFLS 应用了不一致的边界**:
   - 对 **IFLS**：判 `MEASUREMENT_ONLY`（结构轴），理由 = spouse id 需**官方指引的构造过程**、
     跨波 partner id 未核实 ⇒ 方向性依赖重建假设。
   - 对 **SOEP**：判 `NOT_DYADIC_ENOUGH`（同样指向"需构造"），理由 = 公开标准文件无 partner id。
   ⇒ **同一件事（发货形态无 partner id ⇒ dyad 需分析者重建）在两个数据集上拿到了两个不同的标签。**
   **R3-A3b 统一为单一边界**（下表），并**同时**把两者的 rights 侧单独记账:
   | 判据 | IFLS (D06) | SOEP (D11) |
   |---|---|---|
   | 发货形态是否含 partner/couple id | **未核实**（官方 FAQ 指向 IFLS2 User's Guide 的 spouse 识别章） | **明确无**（公开标准文件无 partner id；S47 佐证） |
   | 官方是否提供了构造指引 | **是**（FAQ 指向 User's Guide） | 旧 report 记录**未见**官方 couples 构造程序 |
   | `structural_verdict`（R3-A3b 统一） | **`STRUCTURAL_MEASUREMENT_ONLY`** —— dyad 可**按官方指引**构造，方向性须显式标注为重建假设 | **`STRUCTURAL_NOT_DYADIC_ENOUGH`** —— 构造**无官方指引**，dyad 集合本身是分析者产物 |
   | 差别的一句话形式 | "官方告诉你怎么造，且造法有文档" | "没有官方造法，造什么由你决定" |
   | `access_rights_axis` | `ACCESS_RESTRICTED_PERMISSIBLE`（RAND 注册 + 保密声明；**未见专门 AI 条文**） | `ACCESS_RESTRICTED_PERMISSIBLE` + **AI 全面禁止**（专有 SOEP AI and LLM Use Policy） |
   **该边界的后果（这是本文件用 SOEP 反例想说清的事）**:
   IFLS 的"方向性需假设"是一个**标注义务**；SOEP 的"dyad 需重建"是一个**认识论义务** ——
   后者意味着 dyad 集合本身就是模型假设，故本文件把 SOEP 当**方法学反面教材**。
   **R3-A3b 明确不主张**: 不主张 IFLS 与 SOEP 的数据质量有任何差别;只主张两者的
   **dyad 可构造性**与**官方指引可得性**不同，因此**判据不同**。
SOEP_ai_llm_policy (R3-A3b 新增; **R3-A3b 未直开 — `UNVERIFIABLE_HERE`; CITED_SECONDARY 依 H-C1 / C-C13**):
   存在专门的 **SOEP AI and LLM Use Policy**: **Type 1 → None; Type 2 → None; Type 3 → None**。
   **连 Type 3 也被拒**，官方理由是 **sandbox escape 不可靠**（"LLMs are not available within the
   secure enclave / sandbox escape cannot be relied on" 一类措辞，见 lane `C` / `C-C13` 的直开记录）。
   ⇒ **SOEP 是本审计中唯一一个 Type 3 也被拒绝的数据集。** 这与 ICPSR（Type 3 允许，须与 security plan
   一致并获批）和 Add Health（Type 3 因 "LLMs are not available within the UNC SRW" 被拒，理由**不是**
   sandbox 不可靠）**都不同**。
   **R3-A3b 的抓取记录（如实）**: 4 次尝试全部失败 ——
   `https://www.diw.de/documents/1848/1848.pdf` → **HTTP 500**;
   `https://www.diw.de/en/about-us/legal-terms/soep-terms-and-conditions/` → **404**;
   `https://www.diw.de/en/soep/soep-en/terms-of-use/` → **404**;
   `https://www.diw.de/en/soep/soep-en/data-and-terms-of-use/` → **404**;
   `https://www.diw.de/en/soep/soep-en/data-access/` → **404**;
   `https://www.diw.de/en/soep/soep-en/service/` → **404**。
   `https://www.diw.de/en/soep/` 根页**可打开**，但页面为导航骨架，**本次抓取的输出中未出现
   "LLM" / "artificial intelligence" / "Terms" 字样**（已对该次抓取结果做过全文 grep，0 命中）。
   ⇒ **本 packet 不冒充直开核实。** 上面的 Type 1/2/3 全 None 与 sandbox 理由标
   `CITED_SECONDARY (lane C 直开，R3-A3b 转述)`，并挂 `U19`。
   **Rights fail closed**: 在直开该政策之前，**SOEP 按"个体级数据不得送入任何 LLM"处理**。
canonical_pointer:
   archive: DIW Berlin
   negative_evidence_source: BACON, P., CONTE, A.M. & MOFFATT, P.G. (2014) "Assortative mating on risk
     attitude", Theory and Decision (https://link.springer.com/content/pdf/10.1007/s11238-014-9448-x.pdf)

why_not_dyadic (CITED_PRIMARY_SECONDARY 方法节原文):
   "For the purposes of this research, a subset of 'household couples' is extracted from the panel,
    comprising 7,761 couples, observed on average 3.1 times over the four years.
    In constructing the couples dataset a number of items were taken into account. From the variable
    'relationship to head' we determine the 'head' and 'spouse' for each household for each survey year.
    We are careful to check that they both report having a partner or being married... This filtering
    rule excludes: elderly parent heads who have older children living with them; households headed by
    single heads; and 'non-head' households, in which the spouse remains following separation, divorce
    or bereavement."
   "**We do not find any same-gender couples.**"
negative_result_value:  **这是本 lane 最有价值的反例证据之一。**
   用泛家庭面板造 dyad 的做法会**静默地**：
     (a) 依赖一个建模者的启发式规则（"relation to head" + 婚姻状态）；
     (b) 排除「非户主但仍有配偶」的家庭（即分离/离婚/丧偶后仍同住）；
     (c) 产生**同性覆盖 = 0** 的构造结果。
   → 对 LHRM 的含义：**任何「我们从通用面板造了 dyad」的说法，必须同时交出构造规则、构造掉的样本量、
     以及构造后的同性/非婚/非共居覆盖。** 否则该 dyad 集合是模型假设，不是证据。
can_identify_structurally:  个体层面跨年变量（如 0–10 风险态度）确实双报告
cannot_identify_structurally:  **发货形态下不存在可用的 i↔j 绑定** → `Z[k,i,j,t]` 需先付重建成本
cannot_identify_for_LHRM_use:  **任何 LLM / AI 工具对 SOEP 个体级数据的使用**（SOEP AI and LLM Use
   Policy: Type 1/2/3 全 None; **该政策 R3-A3b 未直开**，见上）
structural_dependencies_unverified:
   - SOEP 是否提供官方 couples 构造程序（U10）
lhrm_impact:  作为**方法学反面教材**纳入，而非作为数据源纳入。
   建议在后续方法学文档中引用本条作为「dyad 构造必须自报规则与损失」的模板。
```

### D12 — Add Health (The National Longitudinal Study of Adolescent to Adult Health)

> **R3-A3b 更正 1（标题误名；依 review-r2 `R-C17` / `C-C19`）**
>
> **被取代的标题**（逐字保留）：`### D12 — Add Health (NLSY97 / ECLS)`
> 以及主表 `| D12 | **Add Health (NLSY97/ECLS)** | UNC CPC | …`
>
> **正确名称**：**The National Longitudinal Study of Adolescent to Adult Health (Add Health)**。
> **R3-A3b 于 2026-09-27 直开** `https://addhealth.cpc.unc.edu/conditions-of-use/`，
> 页面页脚逐字："**The National Longitudinal Study of Adolescent to Adult Health (Add Health)**"。
> 已打开的**全部三个** Add Health 页面（Conditions of Use / Data Documentation）页脚均为此名。
> **NLSY97 与 ECLS 是另外两个独立调查**（National Longitudinal Survey of Youth 1997 /
> Early Childhood Longitudinal Study），把它们放进 Add Health 的标题是**误标**。
> **R3-A3b 一并修正 §9 U7 与主表的相应单元格。**
>
> **R3-A3b 更正 2（非主张的改写；依 review-r2 `R-C17` / `C-C20`）**
>
> **被取代的原文**（逐字保留，§7 非主张 6）：「**不主张** Add Health 存在 friendship nomination 数据文件（U7）。」
>
> **该非主张被撤回**，理由有两条：
> 1. **它把"抓取失败"写成了"不存在"**。R3-A3b 于 2026-09-27 直开
>    `https://addhealth.cpc.unc.edu/documentation/data-documentation/`，**页面可达**，但文件清单表
>    **由 JavaScript 渲染**：抓到的 HTML 里只有表头（`File Name | Dataset Title | Wave Number | Wave |
>    # Variables | Release Date | Access | Category | Directory Path | User Guide | Codebook | Description`）
>    与说明文字，**没有行级数据**。原文逐字："Data-specific codebooks and user guides are available by
>    clicking the green plus sign on the left side of a row in the table below. The table can be filtered
>    by Wave, Access type, or Category…" ⇒ **R3-A3b 抓取状态 = `UNVERIFIABLE_HERE`（JS 渲染，未取得行级清单）**。
>    **抓取失败不是"文件不存在"的证据**（adjudication §C item 6）。
> 2. **review-r2 `C-C20` 报告官方用户指南已列出该文件。**
>
> **取代它的非主张（现行版本）**：
> > **不主张** Add Health 存在 friendship nomination 数据文件。
> > **也不主张**它不存在。
> > **已核实的事实仅有一条**：Add Health 的 Data Documentation 页的**文件清单表由 JS 渲染**，
> > 因此**任何一方都无法从该页的行级清单得出结论**；`R3-A3b` 标 `UNVERIFIABLE_HERE`。
> > **待核实**：`REPORTED_SECONDARY` —— review-r2 的 `C-C20` 记「官方用户指南已列」。
> > 本 packet **未打开**该用户指南，**不为其背书**文件存在性、文件名或变量名。
> > **复通条件**：打开 Add Health 的 Wave I / Wave III in-school nomination user guide
> > （或 ACE Aggregated Codebook Explorer）并逐字记录文件名与 nomination 变量名。
>
> **R3-A3b 的记账纪律**：这是本文件里最好的一处「`FETCH_FAILED` 纪律」被自己破坏的例子 ——
> 旧版把"没拿到"升级成了"不存在"。**R3-A3b 明确记录这一点，并把它作为 §7 纪律条款的一个反例。**

```text
structural_verdict:  **NOT_ASSESSED**（**从未进入结构检验**；见下 `structural_examination_status`）
access_rights_axis:  ACCESS_BLOCKED_USE_CONDITION（AI/LLM 用途全面禁止，公版与 restricted 同等）
classification_legacy_equivalent: ACCESS_BLOCKED（旧单轴标签，保留以便交叉引用；**旧标签不作 canonical 依据**）
structural_examination_status (R3-A3b 新增; 依 review-r2 `R-C6` / `C-C26` + X-14):
   **Add Health 从未进入本审计的结构检验。** 旧版把它按 `ACCESS_BLOCKED` 处理，
   等于把一条**许可 / use-condition** 理由当成了**结构检验的结论**。
   ⇒ 它**不在** §8.9 那个"15 个数据集"的结构否定结果的样本框内。
   ⇒ 它**也**不能被说成"结构不合格"。
   **本 packet 对 Add Health 的结构属性（双报告潜力、nomination 网络、6 wave）不作判定。**
waves:  Wave I–VI（Wave I 1994-95）
dyad_potential:  **报告自述：可能提供方向性友谊提名网络的大型美国纵向数据集**
   （Wave I / Wave III in-school nomination）。**R3-A3b: 该属性的核实状态见上方更正 2
   —— `UNVERIFIABLE_HERE`（JS 渲染），且 `REPORTED_SECONDARY` 称官方用户指南已列。**
   **本 packet 不主张**该 nomination 文件存在，**也不主张**它不存在。
critical_rights_finding (CITED_PRIMARY 原文; **R3-A3b 于 2026-09-27 直开逐字确认**):
   "All users of Add Health restricted-use data agree to the following conditions:
     - The data files will be used solely for statistical analyses.
     - No attempt will be made to identify specific individuals, families, households, schools,
       institutions, or geographic locations...
     - **No list of sensitive data at the individual or family level will be published or otherwise
       distributed.**"
   + 结果呈现门槛: "In no case should a cell frequency of a cross-tabulation be fewer than ten (10) cases."
     （并含三条同门槛：任一行/列全部个案同格；行/列合计 < 10；数量值基于 < 10 个案）
   + "All journal articles ... will receive a PubMed Central reference number (PMCID)."
   + "Data Files released should never permit disclosure when used in combination with other known data."
   + 资助致谢必须包含在每份报告: "Each written report or other publication based on analysis of Add Health
     restricted-use data will include the acknowledgements of funding that can be found on the Add Health
     website"
   **AI and LLM Use Policy (逐字, R3-A3b 直开确认；适用范围已按 review-r2 H-C1 收紧):**
   "In addition, **all users of Add Health data, both public-use and restricted-use**, agree to abide by
    the following LLM and AI Use Policy."
   "Large language models (LLMs) and other AI tools (e.g., ChatGPT, Claude AI, Microsoft Copilot,
    Google Gemini) **may not be used to manage, process, or analyze data distributed by Add Health. This
    policy applies to both public-use and restricted-use data.**"
   "Under Add Health Data Use Agreements, researchers are forbidden to distribute data or other materials
    we supply (apart from codebooks and metadata, described below) to other members, organizations, or
    individuals. **This means that use of LLMs or other AI is a violation of all existing data use
    agreements.**"
   LLM 三分法表（官方原文）: **Type 1 → None; Type 2 → None; Type 3 → None**
   理由（官方原文，逐字）: Type 1 "ingest and make use of the data. This counts as redistributing the data to
   the company operating the LLM"; Type 2 "do not retain or make use of the data, so this does not count as
   redistribution. However, they are not isolated from broader networks or the Internet and heighten external
   data merge risks, so they would not comply with data security plans for Restricted-Use data and are not
   permitted"; Type 3 "do not retain or make use of the data, and they are also isolated on individual
   machines or within secure networks; **however, LLMs are not available within the UNC SRW, so this is not
   an option for Restricted-Use data. At present, we are also not accepting requests for this kind of data
   use for Home Institution Hosting Agreements.**"
   唯一许可: "It is permissible to use LLMs and AI tools with our **public-facing documentation, codebooks,
   and study-level metadata, including group or population estimates**. However, **use of individual-level
   data is not permissible**."
   taxonomy 溯源（官方逐字, R3-A3b 直开确认 —— 单源扩散的直接证据）: "Thanks to **the University of
   Michigan's Health and Retirement Study and ICPSR as well as Sebastian Karcher at Syracuse University** for
   originating this taxonomy of LLMs and/or policy."
   ⇒ **这是「单源扩散」（`SINGLE_SOURCE_DIFFUSION`）的一手证据**：Add Health **自己**说该 taxonomy
   源自 HRS + ICPSR + Karcher。详见 §1.3。
can_identify_structurally:  **不判定**（`structural_examination_status`）
cannot_identify_structurally:  **不判定**（`structural_examination_status`）
cannot_identify_for_LHRM_use（权利轴）:
   - **任何 LLM / AI 工具对 Add Health 个体级数据的管理、处理或分析** —— 官方逐字禁止，
     **公版与 restricted 同等适用**; Type 1/2/3 **全部为 None**
   - 因此其 Codebook / metadata / 群体估计可被 LLM 使用，但**个体级数据不可**。
   **R3-A3b 明确不把这一条读成"识别能力"** —— 这是**使用条件**，不是测量或识别问题。
structural_dependencies_unverified:
   - nomination 文件的存在性与结构（U7，见上方更正 2）
   - 关系状态构念内容
lhrm_impact:  **这是本 lane 最重要的 use-condition 反例**：
   一个在学术上完全合格、在获取上完全可行的顶级青少年纵向数据集，
   因为 **AI 政策**（而非因为拿不到、也并非因为 IRB 强度）而对本项目不可用。
   建议 Architect 把它作为「rights-first 筛选」的示例 —— **`C-C7` 已把它称为样板条款，本 packet 同意。**
   同时其 codebooks / metadata / 群体估计仍可用于 LHRM 的 measurement 文档工作（官方明示允许）。
   **R3-A3b 追加的边界**: 由于 Add Health **从未进入结构检验**，
   §8.9 的"15 个数据集"结论**不能**被用来预测 Add Health 补上结构检验后会怎样，
   反之亦然。**它是一个已知权利结局、未知结构结局的对象。**
```

### D13 — Understanding America Study (UAS)

```text
structural_verdict:  STRUCTURAL_MEASUREMENT_ONLY
access_rights_axis:  ACCESS_BLOCKED_USE_CONDITION（AI 全面禁止）+ ACCESS_RESTRICTED_PERMISSIBLE（Enclave 限美国研究者）
classification_legacy_equivalent: ACCESS_BLOCKED（旧单轴标签，保留以便交叉引用；**旧标签不作 canonical 依据**）
two_axis_split (R3-A3b; 依 review-r2 `R-C6` / `C-C26` `WRONG-SCOPE`):
   **被取代的原文**（逐字保留）: "cannot_identify: 对 LHRM 计划用途 —— **不可识别**（AI 政策）。"
   **问题**: 「不可识别」是一个**测量/识别**词，被用在了**许可**事实上。
   **取代它的分列**:
     cannot_identify_structurally:  家庭 + 健康 + 退休的个体-波次面板；**若存在 partner / household
       linkage 则可谈 dyad（未核实，U10 类）**；**本 packet 不判定其方向性能力** —— 无一手结构文档在手。
     cannot_identify_for_LHRM_use:  **任何 LLM / AI 工具对 CESR 分发的任何数据的管理、处理或分析**
       —— 官方逐字禁止，且官方自陈这 "constitutes a violation of all existing Data Use Agreements";
       Enclave（LINKAGE）"due to federal security requirements … restricted to **US-based researchers**"。
   **R3-A3b 明确不主张**: 不主张 UAS 的结构能力差；只主张**其 AI 用途被官方禁止**。
   **R3-A3b 抓取记录**: **未重开** `https://uasdata.usc.edu/`。上列逐字引文 = `CITED_PRIMARY (relay)`。
canonical_pointer:  https://uasdata.usc.edu/  （CESR, USC）
scope:  双年核心调查（自 2014 起）+ UAS-HRS；Comprehensive File (CF, wide) 与
   Comprehensive Panel Dataset (CPD, long, 每行 respondent-by-wave，2026-03 更新)
   域: demographics / health / cognition / financial wellbeing / retirement
critical_rights_finding (CITED_PRIMARY 原文):
   "At this time, **large language models (LLMs) and other artificial intelligence tools may not be used
    to manage, process, or analyze any data distributed by CESR.** Under the terms of our Data Use
    Agreements, researchers may not share or distribute the data or related materials we provide to any
    other individuals, organizations, or entities. **Accordingly, the use of LLMs constitutes a violation
    of all existing Data Use Agreements.**"
   + "All UAS survey data and data products are coded human subjects data files"
   + Enclave (LINKAGE) 访问 "at the moment, due to federal security requirements, access to the Enclave
     is restricted to **US-based researchers**"
dyad_identifiability:  **UNKNOWN**（本 lane 未核实 UAS 是否有 household-level partner linkage）→ U10 类
can_identify_structurally:  **不判定**（无一手结构文档在手）
cannot_identify_structurally:  **不判定**（同上）
cannot_identify_for_LHRM_use:  **任何 LLM / AI 工具对 CESR 数据的处理**（AI 政策）；若走 Enclave，仅限美国研究者
lhrm_impact:  与 Add Health 同类：可用作**测量/文档参考**，不可用作数据源。
   **R3-A3b 的区分**: 与 Add Health 的**共同**点 = AI 禁令。
   **不同**点 = (i) Add Health **自己声明**承袭 HRS/ICPSR 的 taxonomy（⇒ 扩散链内），
   UAS **不声明**（⇒ 独立，见 §1.3）；(ii) Add Health 的禁令**公版与 restricted 同等**，
   UAS 的措辞是 "any data distributed by CESR"（同样覆盖公版，但**本 packet 未取得**其分类型表格）。
   **R3-A3b 不主张**两者是同一份政策。
```

### D14 — American Family Cohort (AFC)

```text
structural_verdict:  STRUCTURAL_UNKNOWN（本 packet 未核实任何 AFC 结构属性）
access_rights_axis:  ACCESS_BLOCKED_POSSESSION（审批链：机构邮箱 + PHS + ABFM + 第三方 DUA + IRB）
classification_legacy_equivalent: ACCESS_BLOCKED（旧单轴标签，保留以便交叉引用；**旧标签不作 canonical 依据**）
two_axis_note (R3-A3b):
   旧版把审批链长度当成了 `ACCESS_BLOCKED` 的**全部**理由。
   R3-A3b 分列: **结构未知**（不是"结构不合格"）+ **持有阻断**（`ACCESS_BLOCKED_POSSESSION`）。
   ⇒ 依 adjudication §C item 6（"access restriction is not ontology evidence"），
   **审批链长度不得被读成对 AFC 结构能力的任何判断**。
canonical_pointer:  https://americanfamilycohort.org/how-to-access-afc-data/
   **R3-A3b 抓取记录**: **未重开**。逐字引文仍为 relay。
scope:  Stanford 三代替代纵向家庭队列
access (CITED_PRIMARY 原文):
   "The American Family Cohort (AFC) data are very rich and **classified as PHI**. Consequently, there
    are a number of regulatory and security steps to gaining access. These steps are managed on the PHS
    Data Portal."
   步骤: 机构邮箱注册 → 明确 aims（"PHS does not approve overly broad protocols"；任何 linkage/file/year/aim
   变更都需重新 PHS + ABFM 批准）→ 第三方机构签署 Third Party Data Use Agreement（逐项目）→
   ABFM `Restricted Data Application Form` → PHS Data Access
   访问环境: PHS Data Portal + Redivis（docs.redivis.com）
rights:  "Researchers may not share or distribute the data"（DUA 类）
dyad_identifiability:  未核实是否存在 couple-level 双方报告关系状态 → U10 类
lhrm_impact:  作为 **「多代家庭队列需要何种审批」的量级参照** 记录。
   审批链长度（机构第三方协议 + 联邦 IRB 类审查 + 逐项目 aims 审批）与 LHRM 的开放研究节奏不兼容。
   **不建议纳入 LHRM 数据计划。**
```

### D15 — Oregon Youth Study Couples Study, Time 6 (ICPSR 38726)

> **R3-A3b 两轴分离（依 review-r2 `R-C5` / `C-C27` `WRONG-SCOPE`）**
>
> **被取代的原文**（逐字保留，旧版 `D15` 行 + 卡片末行）：
> - 主表：`| D15 | **Oregon Youth Study Couples Study, Time 6** | … | **`ACCESS_BLOCKED`** |`
> - 卡片：`classification: ACCESS_BLOCKED` 且 `cannot_identify: … 不可识别`（旧版把两轴压成一轴）
>
> **问题**：旧版在同一行同时标注了**结构轴 = `MEASUREMENT_ONLY`**（单期、双方报告的恋爱 dyad）与
> **egress 轴 = `ACCESS_BLOCKED`**（RDUA + IRB、非公开下载），但**只输出后者**。
> ⇒ 下游读者会把"拿不到"读成"这个数据集不适合 LHRM"。
>
> **R3-A3b 的分列（现行）**：
> | 轴 | 值 | 依据 |
> |---|---|---|
> | `structural_verdict` | **`STRUCTURAL_MEASUREMENT_ONLY`** | 单期（Time 6, 2003–2006）⇒ 无转移律；双方报告的恋爱 dyad ⇒ 方向性可测 |
> | `access_rights_axis` | **`ACCESS_BLOCKED_POSSESSION`** | 逐字: "Access to these data is restricted… must complete a **Restricted Data Use Agreement**… and **obtain IRB approval or notice of exemption**"；"Restricted data files are **not available for direct download** from the website." |
>
> **R3-A3b 明确不主张**（避免把分离读成升级）:
> - **不主张** D15 的结构质量差 —— 它是本 lane 中除 HARP 外唯一明确"双报告恋爱 dyad"的美国数据集。
> - **不主张** D15 可用于 LHRM —— 取得路径（RDUA + IRB + 非公开下载）在 LHRM 的条件下不现实。
> - **不主张**它因"不可识别"而被排除。**排除理由仅是访问。**
> - **Rights fail closed**: 访问轴的 `ACCESS_BLOCKED_POSSESSION` **不因结构轴好看而放松**。

```text
structural_verdict:  STRUCTURAL_MEASUREMENT_ONLY
access_rights_axis:  ACCESS_BLOCKED_POSSESSION
classification_legacy_equivalent: ACCESS_BLOCKED（旧单轴标签，保留以便交叉引用；**旧标签不作 canonical 依据**）
canonical_pointer:  https://www.icpsr.umich.edu/web/NAHDAP/studies/38726
   **R3-A3b 抓取记录**: **未重开**。逐字引文仍为 relay。
scope (CITED_PRIMARY 原文):
   "This study is part of the Oregon Youth Study, which began in 1983 and has now become the Three
    Generational Study (3GS)… This study explores behaviors among the respondents **and their romantic
    partners**, covering topics such as social patterns, sexual behavior, drug and alcohol use, and
    mental health. The rationale for examining the data is that trends in romantic partnerships may play
    a significant role in physical health outcomes."
   期间: 2003–2006 (Time 6)
access (CITED_PRIMARY 原文):
   "Access to these data is restricted. Users interested in obtaining these data must complete a
    **Restricted Data Use Agreement**, specify the reason for the request, and **obtain IRB approval or
    notice of exemption** for their research."
   "One or more files in this data collection have special restrictions. Restricted data files are not
   available for direct download from the website."
   **R3-A3b 追加的 ICPSR 级要求**（已直开，见 §5.1a）: 任何再分发须先经 **Data Stewardship Policy
   Committee** 批准；individually-deposited studies 为 **members only and cannot be redistributed**；
   适用 ICPSR LLM policy（Type 1 = None / Type 2 = Public-Use / Type 3 = Public + Restricted）；
   且 "Providing ICPSR data to any large language model (LLM) which retains data … **is redistribution …
   and is barred by our terms of use**"。D15 是否属 individually-deposited 一类**未核实**。
dyad:  受访者 + 其恋爱伴侣 → **双方报告**（这是本 lane 中除 HARP 外唯一明确「双报告恋爱 dyad」
   的美国数据集）
waves:  **单期（Time 6）** → 不构成多波双人面板 ⇒ 结构轴 `STRUCTURAL_MEASUREMENT_ONLY`
can_identify_structurally:
   - 恋爱 dyad 的行为与健康（一次性）
   - 双向报告的关系-行为配对（同 record / 可链接性未核实）
cannot_identify_structurally:
   - 时间演化；转移律；路径依赖
structural_dependencies_unverified:
   - 受访者与伴侣的链接键是否为交付形态（未核实）
lhrm_impact:  作为 **「存在但本次不可及」 的登记项** 记录。
   它的存在证明「双报告恋爱 dyad 数据确实被采集过」，但对 LHRM 无操作价值。
   **R3-A3b**: 旧版末句「但对 LHRM 无操作价值」的**依据是访问**（RDUA + IRB 无现实路径），
   **不是**「它不适合 LHRM」。该区分在 §2 的两轴结构下是强制的。
```


### D16 — NICHD SECCYD (Phase I–IV)

```text
structural_verdict:  STRUCTURAL_MEASUREMENT_ONLY（照护侧单方报告）
access_rights_axis:  ACCESS_RESTRICTED_PERMISSIBLE（ICPSR 公版）+ ICPSR 再分发 / LLM policy（**R3-A3b 已直开**，见 §5.1a）
classification_legacy_equivalent: MEASUREMENT_ONLY（旧单轴标签，保留以便交叉引用；**旧标签不作 canonical 依据**）
canonical_pointer:
  series:   https://www.icpsr.umich.edu/web/ICPSR/series/00233
  phase1:   https://www.icpsr.umich.edu/web/DSDR/studies/21940
  phase4:   https://www.icpsr.umich.edu/web/DSDR/studies/22361/versions/V5
scope (CITED_PRIMARY 原文):
   "The SECCYD is a multi-site, prospective, longitudinal study of the experiences of **1,364 children and
    their families**... Respondents were sampled from a catchment of some 6,189 children."
   5 个主评估点: 1 month (enrollment) / 6 months / 15 months / 24 months / 36 months
   "Phone call data were collected every three months between major assessments."
   Phase IV (2005-2007) 追踪 1,056 名入组儿童与家庭
   309 文件按 ADS (Parts 1-42) / SDS (43-55) / Raw (56-309) 组织
dyad_type:  **主要照护者 — 儿童**（kin dyad，非浪漫）
directionality_limit (CITED_PRIMARY 设计原文):
   "The primary interviewee in each household is the participant's **primary caregiver**, with whom the
    child must be living. In the vast majority (over 90%) of cases, this is the child's biological mother."
   → 照护侧**单方报告**。儿童自报（部分年龄）与照护者报告**不是同一构念的双向测量**。
   → Z[caregiving, parent→child] 可测；Z[caregiving, child→parent] 基本不可测。
sampling (CITED_PRIMARY 原文): 有条件随机抽样，确保 60% 计划全职/全职就学、20% 兼职、20% 全职母亲；
   排除标准明列: 母亲 <18 岁、不预期留在 catchment 3 年、出生明显障碍或住院 >7 天、非英语流利
   "Both two-parent and single-parent families were included."
access:  "The public-use data files in this collection are available for access by the general public."
   地码（Raw Census-Related）子集为更高披露等级
can_identify_structurally:  kin dyad 的纵向（照护安排、发展结果、照护决策）
cannot_identify_structurally:  双向自报；恋爱关系；成人伴侣
lhrm_impact:  覆盖 LHRM 研究域中的 **kin / 照护 dyad**（`AGENTS.md` 明确「允许亲属、朋友、同事、前任…
   等现实存在的关系结构进入描述」）。但因单方报告，只能标定 parent→child 单方向。
   价值主要是「证明 kin dyad 在数据世界里存在且可获取」。
```

---

### 4.17 `both_parties_answer_separately` 逐格表（R3-A3b 新增；依派工 item 14）

> **为什么必须逐格**：旧版把「双方独立作答」当作**数据集级**属性（主表一列 + `CALIBRATION_READY` 的定义要点之一）。
> 同一数据集内，**模块之间可以不对称**，而且**同一受访者内部**可以出现 proxy 段。
> R3-A3b 把该属性降为 **per-dataset × per-module × per-condition** 三元组。
> **`STRUCTURAL_CALIBRATION_CANDIDATE` 的定义已删除「双方各自作答」这一数据集级条件**（见 §2.1）。

| 数据集 | 双方各自作答**是**的条件 | **否** / 需外部假设的条件 | 证据状态 |
|---|---|---|---|
| **D01 pairfam** | anchor survey + partner survey 分开施测 | **非共居 partner** 不覆盖（partner survey 绑定 anchor 的 current partner）；`parent$` / `child$` / `paya$` 等多 actor 文件的对应关系未逐项核实 | relay（旧 report） |
| **D02 SHARE** | 常规个人模块（DN/PH/BR/CF/MH/HC/EP/SN/AC…） | **FT / AS / HO / HH / CO** = `fin_resp` 单方；**CH / SP 部分** = `fam_resp` 单方；**cv_r** = 一人代全体；**SHARELIFE** = 不按 couple 角色分派；**end-of-life** = proxy；**proxy 段**（partly / fully）可能一方代答 | **已直开逐字**（FAQ 3.2 / 3.3 / 3.4 / 2.2；CoU §7） |
| **D03 HARP** | 逐字 "spouses were asked to complete the surveys **separately**"（baseline + 每一轮日记） | 无（同一调查内全部双报告） | relay |
| **D04 speed dating** | 每位参加者对**每一位**配对对象各自评分（6 项 + 再意愿）；`match` = 双方都想再见 | 无 —— 但只有 **单一时间点** | relay（`CITED_PRIMARY (relay)`） |
| **D05 DHS Couples** | 双方在同一 record 内各自作答 | 非 co-resident 伴侣不覆盖；polygynous 情境下配对取女方 `caseid` | relay |
| **D06 IFLS** | 部分（household head + spouse；`BA` / `TF` 亲属模块） | **i↔j 绑定需按官方 User's Guide 构造**（U8）⇒ 方向性依赖重建假设 | relay |
| **D07 GUiNZ** | 家庭成员 id 齐 | 成人伴侣间双方自报关系状态**不覆盖**（本研究以儿童-家长为中心） | relay |
| **D08 NSFH** | **亲子 / 跨代**：focal children + 随机一名家长 | **配偶间关系质量：Wave 1 单方报告（已核实）**；**Wave 2 / Wave 3 = `UNKNOWN_AS_OF`**；随机选出的"另一名家长"并非双方 | relay（Wave 1 一句 questionnaire 措辞） |
| **D09 CLOC** | Part 5 "Couples Only"：妻 `V*` + 夫 `S*` 同 record（423 couples / 846 人） | 完整样本 1,532 人中只有这 846 人在该子集内 ⇒ **子集选择规则 `UNKNOWN`** | relay |
| **D10 HRS** | 部分（夫妻同受访） | **配偶常作 proxy respondent** ⇒ 代理者转述与自报混在同一 record；跨波 partner/couple id **未核实**（U5） | relay |
| **D11 SOEP** | 个体层面双报告（如 0–10 风险态度） | **发货形态无可用 i↔j 绑定** ⇒ dyad 需重建；**构造后同性覆盖 = 0**（构造掉） | `CITED_PRIMARY_SECONDARY`（Bacon et al. 2014 方法节） |
| **D12 Add Health** | **不判定**（`structural_examination_status` = 从未进入结构检验） | 同左 | — |
| **D13 UAS** | **不判定**（无一手结构文档在手） | 同左 | — |
| **D14 AFC** | **不判定**（无一手结构文档在手） | 同左 | — |
| **D15 Oregon Time 6** | 受访者 + 其恋爱伴侣（双方报告） | 无 —— 但只有**单期** | relay |
| **D16 SECCYD** | **否**（主要照护者单方报告，>90% 生母） | 儿童自报（部分年龄）与照护者报告**不是同一构念的双向测量** | relay |

**R3-A3b 的记账纪律**：本表全部为**结构轴**事实。**`ACCESS_BLOCKED_*` 的四个对象（D12 / D13 / D14 / D15）在本表中的"不判定"与"双方各自作答"都不得被读作"不合格"** —— 那是访问轴的事（adjudication §C item 6）。

---

## 5. 权利 / 同意 / 再分发限制专章（对本项目影响最大的一章）

### 5.1 汇总表

| 数据集 | 能否公开发布**个体级记录** | 能否发布**派生量**（尺度/参数/嵌入） | LLM/AI 处理个体级数据 | 关键法律工具 | 证据状态（R3-A3b） |
|---|---|---|---|---|---|
| **SHARE** | **否**（CoU §6/§7） | **受限**：§7 明文 "Any derivative datasets, models, or analytical outputs generated through AI or machine learning processes remain subject to the same usage restrictions as the original data" —— **注意该句的读法是「派生量继承限制」，不是「派生量不得存在/不得进入任何流水线」；见 D02 卡的 `lhrm_impact`** | 禁止「非完全自管」的应用；禁止用于 AI 训练（除非本地且纯科学）；"any use for commercial purposes is expressly excluded" | 个人注册 + SHARE User Statement；GDPR；German Federal Statistics Act 下 "factual anonymity" | **§7 / §11 / §12 已于 2026-09-27 直开逐字核对**（CoU "Last updated: April 30, 2026"） |
| **pairfam (ZA5678)** | **否**，且转述称「即使无直接标识也不得发布个体记录」 | **否**（§3 只允许汇总呈现 —— **转述，未直开**） | **未见专门条文 → 未核实。Rights fail closed** | 签署的 user contract；§2 目的限定；§5 禁止向第三方转发 | **`PLAUSIBLE`（旧 report 转述；R3-A3b 未打开 Nutzungsantrag / dbk 任何一份）** |
| **HARP / ICPSR** | 须 ICPSR **书面许可**（Redistribution Policy + Data Stewardship Policy Committee 批准，见 §5.1a） | 同上 | **ICPSR LLM policy**：Type 1 = None；Type 2 = Public-Use（须许可）；Type 3 = Public + Restricted（须许可）。**且 VDE/PDE 内"no LLMs available"** | ICPSR Bylaws Art. 1.2.B；Redistribution Policy；LLM Policy（`Approved: December 11, 2024`） | **policy 两页已直开（2026-09-27）**；HARP study 页为 relay |
| **Add Health** | **否**（"No list of sensitive data at the individual or family level will be published or otherwise distributed"） | 未明示，但受同一 DUA 约束 | **全部禁止**（Type 1/2/3 均为 None；**公版与 restricted 同等适用**；官方自陈使用 LLM "is a violation of all existing data use agreements"） | Add Health DUA；AI and LLM Use Policy；Type 3 目前不接受申请 | **已直开逐字核对（2026-09-27）**；taxonomy 溯源 = HRS + ICPSR + Karcher（⇒ 单源扩散） |
| **SOEP** *(R3-A3b 新增行 —— 旧版**缺**此行，属覆盖缺陷)* | **未核实**（R3-A3b 未直开 SOEP CoU / user contract） | **未核实** | **全部禁止**：专有 **SOEP AI and LLM Use Policy**，**Type 1 / 2 / 3 全 None**；**连 Type 3 都因 sandbox escape 不可靠而拒绝** | SOEP AI and LLM Use Policy；DIW user contract（条文未取得） | **`CITED_SECONDARY`（lane `C` / `C-C13`）；R3-A3b 4 次抓取全部失败（500 / 404 ×5）⇒ `UNVERIFIABLE_HERE`，挂 `U19`** |
| **UAS (CESR)** | 须 DUA 限定 | 同上 | **全部禁止**（明文 "violation of all existing Data Use Agreements"） | UAS Data User Agreement；Enclave 限美国研究者 | relay（**R3-A3b 未重开**） |
| **HRS** | Enclave 用户**永远不得导出** respondent-level；仅统计汇总 | 同上 | **CoU（2026-02-04）逐字禁止 AI 程序与 LLM 与 HRS 数据同用，且点名 open-source AI** ⇒ **分级 = 禁止**（旧版「含新政策（未知）」已废止；U4 已解） | **NIH Certificate of Confidentiality（即使法院命令/传票也不得披露）**；RDA；DCP | **条文 = `CITED_SECONDARY`（lane `C` 直开 / `C-C11` / `H-C1`）；R3-A3b 两次抓取均 403 ⇒ `UNVERIFIABLE_HERE`，挂 `U17`** |
| **IFLS** | 匿名码外不得识别 | 未明示，但 "Please do not distribute these data" | 未见专门条文 | 保密声明（confidentiality declaration）；RAND 注册 | relay（R3-A3b 未重开） |
| **DHS** | 须授权后使用；要求尊重受访者匿名 | 未明示 | 未见专门条文 | 授权制；Data Suppression 规则（括号值） | relay |
| **GUiNZ** | **须输出预审通过**方可发布 | 同上 | 未见专门条文 | Data Access Protocol 2026 v1.0；DAA；**Kaitiakitanga（新西兰数据主权）**；Stats NZ 5 Safes | relay |
| **NSFH / SECCYD** | ICPSR 公版，但结果须遵守 cell ≥10 与地理抑制规则 | 同上 | 适用 ICPSR LLM policy | ICPSR Terms of Use；**Redistribution Policy（见 §5.1a）** | relay；policy 侧已直开 |
| **CLOC** | ICPSR 公版，**限 member institution** | 同上 | 适用 ICPSR LLM policy | ICPSR Terms of Use；**Redistribution Policy（见 §5.1a）** | relay；policy 侧已直开 |
| **speed dating** | **是**（第三方公开镜像） | **是** | 无明文限制 | 公开仓库；**原始研究机构（Columbia）的数据政策未在本 lane 核实** → 保守按「引用而非再分发」处理。**R3-A3b 更正：不是"完全公开"，是"技术上零门槛可下载（第三方镜像）"**（review-r2 `R-C13`） | relay |

#### 5.1a ICPSR 再分发与 LLM 政策（R3-A3b **新增**；两页均于 2026-09-27 直开成功）

> **这是旧版 §5 缺失的一整类要求。** 旧版表格只写了「须 ICPSR 书面许可（Redistribution Policy）」
> 一句，**漏掉了许可的机制、成员限定、以及再分发本身构成 LLM 违规这三条**。
> **R3-A3b 直开确认（逐字）**：

**ICPSR Redistribution Policy**（`https://www.icpsr.umich.edu/sites/ICPSR/about/policies/redistribution`）

> "ICPSR encourages data reuse and **strongly encourages sharing links to ICPSR study home pages** using the
> persistent identifier (DOI) found in the study citation. This has the advantage that potential users will
> receive the most up-to-date version of the data and documentation…"
>
> "**Requests for permission to redistribute ICPSR data (rather than simply links to study homepages) must
> first be approved by the ICPSR Data Stewardship Policy Committee**…"
>
> Bylaws Art. 1.2.B 逐字: "**Members will not distribute data or other materials supplied by ICPSR to other
> members, organizations, or individuals at other institutions, without the written agreement of ICPSR.**"
>
> "**Providing ICPSR data to any large language model (LLM) which retains data, or uses provided data for
> training (e.g., ChatGPT, Microsoft Copilot, Google Gemini, etc.), is redistribution of ICPSR data and is
> barred by our terms of use.** Using an LLM with more restrictive terms may be permissible, but **contact
> ICPSR beforehand for permission.**"
>
> "This policy also applies to data and documentation materials supplied to institutions and organizations
> that are not members of ICPSR."
>
> **成员限定的再分发**逐字: "**For data deposited by individual investigators, these curation costs are borne
> by the ICPSR membership, and thus, these studies are available to members only and cannot be
> redistributed.**"
>
> "Approved requests may be asked to pay a fee to enable co-distribution of the processed version of the
> data and documentation… ICPSR will need to receive authorization for this action from the principal
> investigator or the principal investigator's university."
>
> "Note: this policy does not apply to self-published data."

**ICPSR Policy on the Use of Large Language Models**（`https://www.icpsr.umich.edu/sites/icpsr/about/policies/large-language-models-and-ai`）

> 首行逐字: "**Approved: December 11, 2024**"（⇒ §1.3 单源扩散的**源头日期**）
>
> "Large language models (LLMs) may only be used to manage, process, or analyze data distributed by ICPSR
> **if the LLM meets specific criteria** regarding retention of user-supplied data and/or placement within a
> secure network."
>
> Type 1 = **None**; Type 2 = **Public-Use Datasets**; Type 3 = **Public-Use Datasets + Restricted-Use Datasets**
>
> Secure download 逐字: "…access to restricted-use datasets via secure download requires that the user
> specify and adhere to a data security plan. While there are several different possible plans, all of them
> require the data set to be **isolated from the internet**… Therefore, **the only type of LLM that can be
> used with restricted data is Type 3**, and then only if the use is consistent with the security plan and
> **approved by ICPSR**."
>
> **VDE / PDE 逐字**: "**At present, no LLMs are available within the VDE or PDE, so this is not an
> option.**" （⇒ §6「唯一已知可行路径」的撤回依据之一）
>
> Study-level metadata 逐字: "ICPSR metadata records are licensed under a Creative Commons
> Attribution-Noncommercial 4.0 United States License. Be aware that **the license requires that any user of
> the records gives credit to ICPSR, which can be a challenge with respect to LLMs.**"
>
> taxonomy 溯源逐字: "Special Thanks: ICPSR would like to credit **Sebastian Karcher at Syracuse University
> for originating this taxonomy of LLMs.**"

**R3-A3b 的三条跨卡片后果**：
1. **任何把 ICPSR 数据交给"会保留数据 / 用于训练"的 LLM，本身就是再分发，被条款禁止** —— 这比旧版
   "须 ICPSR 书面许可"更严格，也更明确。
2. **"individually-deposited studies 为 members only and cannot be redistributed"** ⇒ 对 HARP / CLOC /
   NSFH / SECCYD / D15 这五张 ICPSR 卡，**是否属该类未核实**；若属，则连"链接到 study home page"
   之外的任何再分发安排都不成立。
3. **VDE/PDE 内无 LLM** ⇒ 旧 §10 的 P2 行动项（调研 VDE 内自托管模型的可行性）**已被官方文本否决**，
   不应作为后续动作派工。**但 SOMAR VDE 是另一个环境**（范围限社交媒体），未被这一条否决。


### 5.2 对 LHRM Case Bank 与 validation corpus 的三条可执行结论

> 以下为 **AI recommendation（架构建议）**，不是 Human requirement，也不构成已确立结论。

> **R3-A3b 对这三条的限定（依 review-r2 `R-C8` / `C-C34`）**
>
> **`C-C34` 指出的三处越界，R3-A3b 的处置**：
>
> | 越界 | 旧文本 | R3-A3b 处置 |
> |---|---|---|
> | (a) 全部属性判断标 `CITED_PRIMARY` | D01 卡 `design (CITED_PRIMARY, 2026-09-27)`；D01 `rights_and_limits (CITED_PRIMARY 原文摘要)`；D03 / D08 / D09 / D10 / D16 等多处以 `CITED_PRIMARY 原文` 为行标签 | **逐条降级**：R3-A3b 亲自打开并逐字核对的 6 组页面保持 `CITED_PRIMARY`；**未打开的一律标 `CITED_PRIMARY (relay, 未由 R3-A3b 重开)`**。pairfam 的 `rights_and_limits` 整块降为 **`PLAUSIBLE`（`CITED_SECONDARY`）**。 |
> | (b) 与"本 lane 零数据接触"并存 | §7 非主张 1「本 lane **零数据接触**」 | **不矛盾，但必须限定**：`CITED_PRIMARY` 指的是**文档属性判断**（读了官方页面并逐字引录），不是**数据接触**。"零数据接触"指的是**未下载/未打开/未分析任何数据文件**。R3-A3b 把这两件事在文件头与本节**分开定义**（见下方 §2.4）。 |
> | (c) 全部 `FETCH_FAILED` 记录被保留了，但**后果**被高估 | §8.6 由 `icpsr.umich.edu` 403 推出"所有 ICPSR 系证据 MEDIUM"；由 `hrs.isr.umich.edu` 403 推出"U4 条文 `UNKNOWN_AS_OF`" | 已按 `R-0.8` / `R-0.9` 更正（见 §8.6 与 D10）。**`FETCH_FAILED` 纪律本身保留并被推荐为全文件范式** —— R3-A3b 把它作为 §12 的组织方式，并新增 11 条自己的失败记录。**唯一被 R3-A3b 判定为违反该纪律的，是旧版非主张 6**（把"未核实存在性"写成"不得主张存在"）—— 已撤回并留作反例。 |
>
> ### 2.4 `CITED_PRIMARY` / `zero data contact` 的定义分离（R3-A3b 显式化）
>
> | 标签 | 定义 | 是否需要数据接触 |
> |---|---|---|
> | `CITED_PRIMARY` | 本 packet（或被标注的 lane）**直接打开了官方页面并逐字引录** | **否** |
> | `CITED_PRIMARY (relay)` | 该引文由上游 lane 直开；**本 packet 未重开**，只做转录 | 否 |
> | `CITED_SECONDARY` | 引自学术论文的方法节 / 二手转述 | 否 |
> | `PLAUSIBLE` | 方向可辩护，但支撑它的原文未取得 | 否 |
> | `UNVERIFIABLE_HERE` | **本 packet 尝试过且失败**（URL + 状态码见 §12） | 否 |
> | `UNKNOWN_AS_OF` | 状态是文档版本 / 页面覆盖问题，非事实矛盾 | 否 |
> | **零数据接触** | **未下载、未打开、未分析任何数据文件或受限数据**；未用凭据；未绕过 auth / licence / robots | — |
>
> ⇒ **这些标签全部属于"文档接触"层，与"数据接触"层正交。** 声明 `zero data contact` 的同时使用
> `CITED_PRIMARY` 是**自洽的**，前提是 `CITED_PRIMARY` 指的是**页面**而不是**数据**。
> 旧文件的问题是它没有把这两层分开写，读者只能猜。R3-A3b 把它显式化。

1. **`VALIDATION_CORPUS_V0_1.md` 现有的 `access_status` / `copyright-license` 字段不足以表达 use-condition 限制。**

   现有 12 个材料全部是公开叙事来源（gov.uk、StoryCorps、Gutenberg、National Archives、SEP、MIT Classics、PMC），不受上述任何 use-condition 管辖。但一旦引入问卷型个体级数据，**「能否获得」与「能否用于 LLM 参与的验证流水线」是两个独立且可能互相矛盾的位**。
   建议为 Case Bank 材料增加一个显式字段，例如 `llm_use_condition: PERMITTED | RESTRICTED_LOCAL_ONLY | PROHIBITED`，并把 `icpsr_llm_type: 1|2|3` 之类的可执行约束写进选材规则。

2. **HRS 的 NIH Certificate of Confidentiality 与 Case Bank 的「官方法院文书」路线互斥。**
   该证书禁止在任何民事/刑事/行政/立法程序中披露可识别的敏感参与者信息，**即使法院命令或传票**。
   `VALIDATION_CORPUS_V0_1.md` §10 建议把「法院/官方材料」作为 Case Bank 第一优先来源。
   → 结论：**Case Bank 的材料选择不能同时依赖「行政/司法渠道获取」与「个体级问卷数据」**。这两条路在制度上分岔。

3. **「公开叙事语料」与「问卷型个体级数据」在 rights 上是两个不重叠的世界。**
   前者（gov.uk 判决、National Archives、StoryCorps、Gutenberg、SEP、MIT Classics）目前不受任何 LLM 政策约束；后者（Add Health / UAS / ICPSR / SHARE / **SOEP** / pairfam）已被 2025–2026 的新政策实质或明文覆盖。
   → 这为 LHRM 提供了一个结构性回旋空间：**把 Case Bank 保持在公开叙事语料侧，把问卷数据限制在方法学标定侧（且仅在本地合规环境内）。**
   **R3-A3b 的两点收紧**：
   (a) 「已被 2025–2026 的新政策覆盖」是**单源扩散**，不是五个独立来源（§1.3）。**四个（Add Health / ICPSR / SOEP / HRS）承袭同一 taxonomy；SHARE 与 UAS 独立成文。**
   (b) **pairfam 未被列入已覆盖名单是正确的** —— 本 packet **未核实** pairfam 是否有任何 AI/LLM 条款（U18）。
       **Rights fail closed** ⇒ 在核实前，pairfam 按"个体级数据不得送入外部 LLM 服务"处理。
       **本 packet 不主张** pairfam 允许这样做。
   **R3-A3b 对第 3 条的整体评估**: 它是本文件**唯一一条仍然完全成立且未受任何 review finding 影响**的结论
   —— 因为它不依赖任何字段级存在性主张，也不依赖"唯一路径"。


---

## 6. 非数值但结构化来源（event history / 行政记录 / 文本）及其 rights

| 来源 | 结构化程度 | 对 LHRM 的潜在用途 | Rights 现状（2026-09-27） | 状态 |
|---|---|---|---|---|
| **Vital registration**（如 Massachusetts Registry of Vital Records） | 事件级（婚/离婚/死亡 + 日期） | 关系状态机的事件锚点 | 机构限制真实存在且有文档 | **间接已核实**：HARP 文档原文证明该登记处对同性婚姻记录的招募渠道有限制（导致同性/异性抽样框不同）。直接申请条件未核实 |
| **National Death Index (NDI) / 州死亡记录** | 事件级（死亡 + 日期） | 关系终点事件 | 受 NDI 与州级协议约束 | **间接已核实**：CLOC 文档原文确认使用 NDI + 州月度死亡记录 + 死亡证明核销 |
| **SHARE record linkage projects**（SHARE-RV / REGLINK-SHAREDK / REGLINK-SHAREFI / SHARE NL） | 行政记录级（养老金/医保/税） | 关系状态的**环境/约束层**（收入、医保、养老金） | 各自独立申请；**是否含伴侣级 linkage 未核实（U13）** | 存在性已核实 |
| **UK data linkage**（SAIL Databank / UK LLC / EGA） | 行政 + 电子健康记录 | 跨代/多来源关系环境 | 需安全环境（SecureLab / SP / V3）；CLS 分 tier 1b/2/3 | 已核实（CLS Data Access Framework 原文） |
| **CLS partnership / fertility harmonised histories**（NCDS / BCS70 / Next Steps） | 事件史级（start/status/end date/prior status/sex） | 关系形成与解体的**事件序列** | UKDS 免费（EUL）；协调版本 "Partnership harmonized histories update deposited ... 2026" | 已核实（CLS webinar 原文；"available"） |
| **PSID / CDS / TA** | 面板 + 事件 | 家庭经济/迁移事件 | 需注册；CDS 由 primary caregiver 报告 | **二手证据**（学术论文方法节）→ 未作为主数据集审计 |
| **DHS vital registration linkage**（部分国家） | 事件级 | 死亡/迁移事件 | 依国而异，逐国申请 | 未核实 |
| **公开的已发表 event-history 表**（如离婚风险表） | 表格级 | 极端值 sanity check | 版权保护；只能引用 | 未核实具体实例 |
| **关系类 App / 手机日记研究** | 个体/日记级 | 密集纵向 + belief 捕捉 | — | **在本审计的 16 个对象中未发现任何公开 release**（U14）。**R3-A3b 范围更正**：这是**检索范围**内的结果（依 adjudication **X-14**），不是领域存在性结论 |
| **ICPSR Virtual / Physical Data Enclave (VDE / PDE)** | 计算环境 | 在隔离环境内处理 ICPSR 的 **Restricted-Use** 数据 | 需 RDUA + IRB；**由 ICPSR 的 LLM policy 管辖** | **`NOT_A_PATH_FOR_LLM`（R3-A3b 重新抓取核实）** —— ICPSR LLM policy 逐字："*Restricted-Use Datasets via the ICPSR Virtual or Physical Data Enclaves (VDE or PDE) — **At present, no LLMs are available within the VDE or PDE, so this is not an option.***"（`https://www.icpsr.umich.edu/sites/icpsr/about/policies/large-language-models-and-ai`，2026-09-27 直开成功）。⇒ **ICPSR 自己的 enclave 不是一条「用 LLM 处理受限数据」的路径。** |
| **SOMAR VDE（ICPSR 社交媒体档案）** | 计算环境，**限 SOMAR 的社交媒体受限数据** | 在隔离环境内处理**社交媒体**受限数据 | 需 RDUA + IRB；自托管模型须经 ICPSR staff 安全审查 | **R3-A3b 重新抓取核实**：该页首句即限定范围 —— "*The SOMAR Virtual Data Enclave (VDE) is a secure, remote desktop research environment operated by the **Social Media Archive at ICPSR (SOMAR)**. The VDE enables researchers to work with sensitive or restricted **social media** datasets*"。列出可自托管模型 `bert-base-uncased` / `Llama-3.2-3B-Instruct` / `gemma-3-4b-it`（"More models available by request"）。**另有一条本文件原先没有的成本事实**：自 2026 年初起，每团队 **$371 / 月** + 一次性 **$1,000 setup**（2026-01-01 之后 onboarded 的团队适用）⇒ **不是零门槛**。`https://www.icpsr.umich.edu/sites/somar/somar-vde-overview-and-resources`，2026-09-27 直开成功 |

> **R3-A3b 最高严重度处置：撤回「唯一已知可行的合规路径」（依 review-r2 `R-C1` / `C-C14` `WRONG-SCOPE`；`C` 判为本 packet 中唯一会导致真实合规后果的错误）**
>
> **被取代的原文**（逐字保留，§6 表末行 + §10）：
>
> > 「已核实（SOMAR 页原文）——**这是目前唯一已知可行的『合规地用 LLM 处理受限数据』路径**」
> > 「并给出**唯一已知可行的合规路径**（ICPSR SOMAR VDE / MiCDA Enclave 内的自托管模型）」
>
> **这句断言有三重错误，且三重都经 R3-A3b 于 2026-09-27 直开官方页面后确认：**
>
> | # | 断言成分 | 官方页面实测 | 状态 |
> |---|---|---|---|
> | 1 | 「ICPSR 自己的 VDE/PDE」是处理受限数据的 LLM 路径 | ICPSR LLM policy：`Restricted-Use Datasets via the ICPSR Virtual or Physical Data Enclaves (VDE or PDE)` 小节首句：**"At present, no LLMs are available within the VDE or PDE, so this is not an option."** | **证伪**（ICPSR 自己明文否认） |
> | 2 | SOMAR VDE 是一条通用的「受限数据 + LLM」路径 | SOMAR VDE 页把自身范围限定为 **social media** 受限数据 | **范围错置**（它服务社交媒体，不是通用问卷数据） |
> | 3 | 这是**「唯一已知可行的」**路径 | 这是一个**全称存在性主张**，而本 lane 从未做过一次「LHRM 计划用途下、受限数据、LLM、可得路径」的**系统枚举**。依 adjudication **X-14**，「在本次检索中未找到」**不等于**「唯一」。 | **检索范围越界** |
>
> **取代它的三条分别成源、各带条件与出处的陈述（R3-A3b 现行版本）**：
>
> 1. **ICPSR Restricted-Use 数据 + LLM 的唯一被官方允许的组合是 `Type 3` LLM + 安全的 secure-download 路径，且须与 data security plan 一致并经 ICPSR 批准。** 出处：ICPSR LLM policy，2026-09-27 直开，逐字："*access to restricted-use datasets via secure download requires that the user specify and adhere to a data security plan… Therefore, **the only type of LLM that can be used with restricted data is Type 3**, and then only if the use is consistent with the security plan and approved by ICPSR.*" `Type 3` = 机构许可、不保留用户数据、**且**被隔离在无互联网的安全网络内。
> 2. **ICPSR 的 VDE/PDE 本身不是 LLM 路径**（逐字见上表 #1）。⇒ 「SOMAR VDE / MiCDA Enclave 内跑自托管模型」这条**旧建议已被官方文本否决**；§10 的 P2 行动项据此改写。
> 3. **SOMAR VDE 是一个真实存在、但范围受限、且非零门槛的选项**：限 SOMAR 社交媒体受限数据；无外网、无导出、无截屏；自托管模型须经 ICPSR 安全审查；自 2026 年初起 $371/月 + $1,000 一次性费用。**本文件不主张**它适用于 LHRM 的问卷型 dyad 数据集（D01–D16 无一在 SOMAR 托管）。
>
> **同时撤回 §10 的自评"最有价值的产出"**（见 §10 重写）。
>
> **明确不主张（避免把撤回读成相反的过度主张）**：本文件**不主张** LHRM 存在任何可用的「受限数据 + LLM」路径；**也不主张**不存在。这是一次**未做过的系统枚举**（U16），不是一次否定结果。**Rights fail closed**：在枚举完成之前，任何受限数据 + LLM 的组合**按不可用处理**。


---

## 7. 明确非主张（explicit non-claims）

1. **不主张**本报告涉及的任何数据集已被 LHRM 下载、打开、分析或映射。本 lane **零数据接触**。
   **R3-A3b**: R3-A3b 亦零数据接触（只重开了 CoU / licence / policy 页面）。
2. **不主张** pairfam / SHARE / HARP 能标定 LHRM 的具体关系状态构念。其**结构**已核实，**构念内容**未核实（U15）。「结构合适」≠「参数可标定」。
3. **不主张**任何数据集具有代表性或可外推性。各样本的硬门槛（合法已婚+同居 3 年 / 50+ / 异性单性 / 0–3 岁 / 配偶已故 / co-resident / 过抽样设计）已逐条列出。
   **R3-A3b 追加**: NSFH 尤其**不是**概率抽样（Wave 1 对若干家庭类型做双重抽样 / 过抽样）⇒ 旧版称其"最著名的家庭纵向调查"在**抽样框**上不准确。
4. **不主张** speed dating 的 `dec`/`match` 等于 attraction / trust / dedication。它是单一决策变量。
5. **~~不主张 HRS CoU（2026-02-04）AI/LLM 政策的具体内容。只核实其存在（U4）。~~**
   **R3-A3b 撤回该非主张**（依 review-r2 `R-C4` / `C-C11`；`H-C1` 判 `VERIFIED`）：U4 **已解**。
   **现行非主张**: **R3-A3b 自己未能直开该 CoU 页**（403 × 2）⇒ 本 packet 引用的禁令内容是
   **lane `C` 直开结果的转述**，标 `CITED_SECONDARY`。**不主张**本 packet 已核实该条文；
   **不主张**该政策此后未变更（**日期戳 2026-02-04 必须随引用保留**）。
6. **~~不主张 Add Health 存在 friendship nomination 数据文件（U7）。~~**
   **R3-A3b 撤回该非主张**（依 review-r2 `R-C17` / `C-C20`；并按 adjudication §C item 6：
   抓取失败不是存在性否定）：**现行非主张 = 既不主张存在，也不主张不存在**；
   已核实的事实仅是「文件清单表由 JS 渲染 ⇒ 本 packet 无法从该页得出结论」；
   `REPORTED_SECONDARY`（`C-C20`）称官方用户指南已列，**本 packet 未打开该指南**。见 D12 卡。
7. **不主张** IFLS 存在现成跨波 partner id（U8）。
8. **不主张** Family Life Survey / LSAF / New Study of Marriage 的任何属性（U1–U3，本 lane 无法访问）。
9. **不主张**本 landscape 覆盖了所有重要数据集。已知缺口见 §9 与 U1–U15（+ R3-A3b 新增 U16–U20）。
10. **不主张** §5.2 的三条结论是 Human requirement。它们是 **AI recommendation**，需 Human / Architect 判定。
11. **不主张**任何 LLM 政策将来不会变。SHARE CoU §12 明文可变更（21 天生效）；ICPSR LLM policy 首行
    标 `Approved: December 11, 2024`；Add Health 与 SOEP 各自把 taxonomy 溯源到 HRS + ICPSR + Karcher，
    即**政策在生态内联动演进**。**日期戳必须随引用保留。**
12. **不主张**本 lane 规避、绕过或尝试规避任何 access control。所有 blocked 项按 blocked 记录。
13. **不主张**本 lane 的任何权利解读构成法律意见。本 lane 只做文本层面的事实记录。
14. **（R3-A3b 新增）不主张**存在任何「合规地用 LLM 处理 LHRM 相关受限数据」的可行路径。旧 §6 / §10
    的「**唯一已知可行路径**」已撤回 —— 但**撤回的不是它的反面**：本 packet **既不主张**存在这样的
    路径，**也不主张**不存在。这是一次**未做过的系统枚举**（U16）。**Rights fail closed：在枚举完成前，
    任何受限数据 + LLM 的组合按不可用处理。**
15. **（R3-A3b 新增）不主张** Add Health 的**结构**能力（旧版从未作结构判定，R3-A3b 也不补判）。
    它是一个**已知权利结局、未知结构结局**的对象。
16. **（R3-A3b 新增）不主张** pairfam 的 `p` 前缀是"统一"的（已收窄为"主用"），也不主张其 rights 条款
    内容（旧 report 转述，R3-A3b 未打开任何一份 Nutzungsantrag / dbk ⇒ `PLAUSIBLE`）。
17. **（R3-A3b 新增）不主张** SOEP 的 AI / LLM 政策条文内容（R3-A3b 4 次抓取全部失败 ⇒
    `UNVERIFIABLE_HERE`）；只记录 lane `C` 的直开结论（Type 1/2/3 全 None、Type 3 因 sandbox escape 不可靠
    而拒）。
18. **（R3-A3b 新增）不主张** NSFH 的配偶间关系质量在 Wave 2 / Wave 3 是单方还是双方报告
    （`UNKNOWN_AS_OF`）—— 旧版由 Wave 1 一句 questionnaire 措辞外推至全 series，本 packet 不接受该外推。
19. **（R3-A3b 新增）不主张** CLOC 的 `structural_verdict`。按报告自己的判据它应当更高，按"留存筛选
    子样本"它应当更低，两条方向的一手证据都未取得 ⇒ `STRUCTURAL_MEASUREMENT_ONLY_PENDING`。
20. **（R3-A3b 新增）不主张**本文件对"哪些数据集是 `CALIBRATION_READY`"给出了最终判断。
    旧单轴标签已拆为两轴；`STRUCTURAL_CALIBRATION_CANDIDATE` 严格只成立于**结构层**，
    且 U15（构念内容）未解。
21. **（R3-A3b 新增 · 记账纪律的自指）不主张**本文件 §7 各条非主张本身已被完整遵守。
    **旧版非主张 6 是一个反例**：它把"本 lane 未核实文件存在性"升级成了"不得主张该数据存在"，
    即**把抓取失败写成了存在性否定**。R3-A3b 已撤回该条并保留此记录，作为纪律条款的可见反例。


---

## 8. 矛盾与否定结果

1. **SHARE wave 数：官方站点内部的**文档覆盖版本差**，不是事实矛盾。**
   **被取代的原文**（逐字保留）: 「**SHARE wave 数：官方站点内部不一致。** … 这是官方文档矛盾，非本 lane 读取错误。」
   **R3-A3b 改判为 `UNKNOWN_AS_OF`**（依派工 item 14）。依据（2026-09-27 直开观察）:
   - `Conditions of Use` 页与 `FAQs & Support` 页的左侧导航**均只列到 Wave 9**（外加 `Corona Questionnaire 1/2`）。
   - `FAQs & Support` §4.3「Which countries have participated in each SHARE wave?」**把 "Wave 9
     (2021–2022) — 28 countries" 列为常规 wave**，并另列 "Wave 9 – COVID Survey (2021) — 28 countries"。
   - 但同一站的 `FAQs & Support` §2.1 "Table 1: **Overview of documentation files for waves 1 to 8**"
     仍只到 **Wave 8**。
   ⇒ **同一官方站点上，「哪些 wave 存在」与「哪些 wave 有已发布文档」两张表版本不同步。**
   **R3-A3b 未重开** `Data Releases` 表（release 9.0.0, 2024-03-28）与 SHARE-CZ FAQ
   （其 "Wave 10 (2023–2024)" 说法）⇒ Wave 10 状态 `UNKNOWN_AS_OF`。
   **不主张** Wave 10 不存在，**也不主张**它存在。
   **现行表述**: 已核实完整常规 wave **到 Wave 9 (2021–2022, 28 国)**（依 FAQ 4.3 逐字）；
   Wave 10 状态 `UNKNOWN_AS_OF`；release 9.0.0 的 DOI 覆盖到 `10.6103/SHARE.w8.900`。


2. **NSFH Wave 3 年份：两个官方来源不一致。** ICPSR series 页记 "conducted in 2001-2002"；NIH grant R03-AG045503-01 记 "2001-2003"。→ 标并存，不选边。

3. **HARP：ICPSR 落地页与 datadocumentation 页互相矛盾。** 落地页 "Version Date: Jan 4, 2022"、标题 "2014-**2015**"、内容仅 Time 1；`/summary` 与 `/datadocumentation` 显示 "2014-**2025**" 并含 T2/T3 完整留存数字。
   → **T2/T3 微数据是否已实际 release 无法确认**，`UNKNOWN_AS_OF`。
   → 这是一条对本 lane 不利的否定结果：HARP 虽被列为 `CALIBRATION_READY`，但**该判定基于招募与设计文档，而非基于微数据可得性的确认**。

4. **DHS couples file 不是每轮都有。** 官方 user forum 原文记录因 Men's Questionnaire 未记录配偶 household line number 而 "could not be generated"。→ "DHS 覆盖约 90 国"必须降级为「逐轮/逐国需查」。

5. **SOEP：已发表的 couples 研究自陈构造后无同性 couples。** 原文 "We do not find any same-gender couples."（2004–2009 构造的 7,761 couples 子样本）。
   → 对「从通用面板造 dyad」这一做法的**直接反例**：构造规则会静默删掉同性关系。

6. **站点可达性受限。** ICPSR 全站 403；`hrs.isr.umich.edu` 正文反复 timeout/403；`familylifesurvey.org` / `lsaf.org` / `nsmshow.org` 连接失败；`www.nichd.nih.gov` 拒绝抓取。
   → **本报告中所有 ICPSR 系证据强度为 MEDIUM**（经搜索引擎索引的一手页面文本）。
   → **Family Life Survey、LSAF、New Study of Marriage 三个文献常用核心 panel 无法审计** —— 本 lane 最实质的覆盖缺口。如实记录，不用记忆填充。

   **R3-A3b 对本条的修正（依 review-r2 `R-0.8` / `C-C31` `CONTESTED` + `R-0.9` / `C-C33`）**
   - **「ICPSR 全站 403」被撤回**（作为一句**全站**断言）。2026-09-27 直开结果:
     **两个 ICPSR policy 页面均返回 200 并取得完整正文** ——
     `https://www.icpsr.umich.edu/sites/icpsr/about/policies/large-language-models-and-ai` ✓
     `https://www.icpsr.umich.edu/sites/ICPSR/about/policies/redistribution` ✓
     `https://www.icpsr.umich.edu/sites/somar/somar-vde-overview-and-resources` ✓
     ⇒ **`icpsr.umich.edu` 至少这三个页面在本环境可达。** 旧 report 的"全站 403"是**过度概括**
     （很可能只对 `/web/...` 的 study 页面成立）。**R3-A3b 未重开任何 `/web/...` study 页**，
     故不主张 study 页也可达。
     **可辩护的现行表述**: 「**本报告中所有 ICPSR 系证据的强度依页分级** ——
     ICPSR **policy 页 = `CITED_PRIMARY`（R3-A3b 直开）**；**ICPSR study 页 = `CITED_PRIMARY (relay)`
     且本 packet 未直开**。§8.6 原先那种"整片 ICPSR 一律 MEDIUM"的写法被这条分级取代。」
   - **`hrs.isr.umich.edu` 的 timeout/403 记录保留**，但**其后果被高估的那部分已删除**:
     旧版由此推出「HRS CoU 条文 `UNKNOWN_AS_OF`（U4）」。**该推论不成立** —— 抓取失败是**访问限制**，
     不是关于政策内容的**证据**（adjudication §C item 6）。R3-A3b 于 2026-09-27 两次抓取仍 403
     ⇒ 标 `UNVERIFIABLE_HERE`（U17），而**U4 的结论按 review-r2 `R-C4` 裁决改为"已解、分级 = 禁止"**，
     条文来源标 `CITED_SECONDARY`（lane `C` 直开）。见 D10 卡与 §5.1 HRS 行。
   - `familylifesurvey.org` / `lsaf.org` / `nsmshow.org` / `nichd.nih.gov` 的失败记录**全部保留**（U1–U3）。
   - **R3-A3b 新增的抓取失败记录**见 §12（ICPSR 无失败；HRS 403×2；SOEP 500/404×5；pairfam 500；
     SHARE release-guide PDF 无法抽取文本；Add Health 文件清单表 JS 渲染）。

7. **Add Health Data Documentation 的数据文件表为 JS 渲染，未取得行级清单。**
   → **R3-A3b 确认此失败记录仍然成立**（2026-09-27 直开，页面可达、表格行级数据缺失）。
   → **但其后果被改写**（依 adjudication §C item 6；review-r2 `R-C17` / `C-C20`）:
     **不得**由此推出「不主张该文件存在」。现行非主张见 §7 第 6 条与 D12 卡。
   → friendship nomination 文件名/变量名 `UNVERIFIABLE_HERE`（JS 渲染）+ `REPORTED_SECONDARY`（`C-C20`）。

8. **「intensive longitudinal 关系日记数据」的可得性 —— 检索范围内的结果，非领域存在性结论。**
   **被取代的原文**（逐字保留）: 「**「intensive longitudinal 关系日记数据」在本 landscape 中不存在公开可得的。**」
   **R3-A3b 改述（依 adjudication **X-14** / review-r2 `R-0.3` / `C-C30` `WRONG-SCOPE`）**:
   > **在本审计的 16 个对象中未发现公开可得的 intensive longitudinal 关系日记数据。**
   > 16 个对象中唯一密集设计是 HARP 的 8–10 天日记（嵌套于稀疏面板，且 **T3 天数由 10 降至 8**，
   > **密集窗长度本身随时间变化，wave 不完全可比**）。
   > **不主张**该类数据在字段上不存在或不可得。**不主张**它公开可得。
   > **未审计的对象**见 §9 U1–U3（Family Life Survey / LSAF / New Study of Marriage **无法访问**）
   > 与 U11 / U12 / U14 —— 这些正是最可能容纳密集日记设计的对象，且**本 packet 未审计它们**。
   > ⇒ **该否定结果的样本框是 16 个已审计对象，其中 3 个核心 panel 从未成功访问。**

9. **本次检索的结构性结果（依 adjudication **X-14** / review-r2 `R-0.2` / `C-C29` `CONTESTED` 重写）。**
   **被取代的原文**（逐字保留）:
   > 「**最重要的整体否定结果**：本审计**未发现**任何「完全公开 + 双报告 + 方向性 + 多波 + 关系状态构念」
   > 的数据集。**这四个条件的交集为空。** 这是本 landscape 最重要的结构性事实，比任何单个数据集的优劣都重要。」

   **R3-A3b 改述（逐条）**:
   > **(a) 范围**：在本审计**进入结构检验的 15 个数据集**上，本检索未找到同时满足
   > **「技术零门槛可下载 + 双报告 + 方向性 + 多波 + 关系状态构念」**的数据集。
   > —— **不是**「四条件交集在 landscape 上为空」，**不是**「这是本 landscape 最重要的结构性事实」。
   > **(b) 样本框的关键限定**：**Add Health（D12）从未进入结构检验**。它被一条**许可 / use-condition**
   > 理由排除，而不是因为结构不合格。而 review-r2 `C-C20` 记 **Add Health 官方文档确有
   > nomination / romantic-pair 结构**。
   > ⇒ 因此本条的**样本框是 15，不是 16**；且**一个结构上可能合格的对象从未被检验**。
   > **(c) 第五条条件的措辞**：旧版把四条说成"这四个条件"却又列了五个（"关系状态构念"是第五项）。
   > 现按五项列举。
   > **(d) 仍可保留的结论（不需要字段级否定即可成立）**:
   > 　· 三个 `STRUCTURAL_CALIBRATION_CANDIDATE`（pairfam / SHARE / HARP）**全部**要求 DUA 或机构申请；
   > 　· 唯一技术零门槛可下载的对象（speed dating 第三方镜像）**只有单一时间点**；
   > 　· ⇒ **「零门槛」与「多波 + 双报告」在本审计的 16 个对象中不相容。**
   > 　这条是关于**本审计样本**的可核实观察，**不**是关于 landscape 的存在性结论。
   > **(e) 本 packet 既不主张**该交集在字段上非空，**也不主张**它为空。
   > 复通条件：解 U1–U3（三个无法访问的核心 panel）+ 对 Add Health 做结构检验（解 U7）
   > + 解 U15（构念内容）后重跑。


10. **反向（有利）否定结果**：本审计**未发现**任何问卷型数据集会与 `VALIDATION_CORPUS_V0_1.md` 现有 12 个公开叙事材料的权利条款发生冲突。→ 现有 Case Bank 路线在权利上是干净的。

---

## 9. 剩余未知

| # | 未知项 | 状态 |
|---|---|---|
| U1 | Family Life Survey（Larimer）当前 wave / couple id / codebook / access 条款 | `FETCH_FAILED`（4 次尝试） |
| U2 | LSAF 是否仍采集 / 当前申请路径 | `FETCH_FAILED` |
| U3 | New Study of Marriage 当前 wave 数与获取路径 | `FETCH_FAILED` |
| U4 | **~~HRS CoU（2026-02-04）AI/LLM 政策具体条文~~** | **R3-A3b: 已解（resolved）。** 分级 = **禁止**（`ACCESS_BLOCKED_USE_CONDITION`）。**证据状态**: 条文 = `CITED_SECONDARY`（lane `C` 直开，`C-C11` / `H-C1` 判 `VERIFIED`）；**R3-A3b 两次抓取 403 ⇒ `UNVERIFIABLE_HERE`**（另立 U17） |
| U5 | HRS 是否发货跨波稳定 partner/couple id | `UNKNOWN` |
| U6 | HARP T2/T3 微数据是否已 release | 页面矛盾，`UNKNOWN_AS_OF` |
| U7 | ~~Add Health friendship nomination 文件名/变量名~~ | **R3-A3b 改判**: 旧版把它记为"**不主张该数据存在**" —— 该非主张已撤回。**现行**: 文件清单表 **JS 渲染 ⇒ `UNVERIFIABLE_HERE`**；`REPORTED_SECONDARY`（`C-C20`）称官方用户指南已列。**不主张存在，也不主张不存在** |
| U8 | IFLS 是否有现成跨波 partner id 变量 | `UNKNOWN`（官方 FAQ 把识别章指向 IFLS2 User's Guide ⇒ 是**官方指引的构造**，不是发货变量） |
| U9 | pairfam 非共居 partner 的测量覆盖 | `UNKNOWN` |
| U10 | SOEP / PSID / NLSY79-97 / Understanding Society 扩展文件是否发货 partner id | `UNKNOWN`；标准文件无（S47 佐证 SOEP）。**R3-A3b**: SOEP 侧另需确认官方是否提供 couples 构造程序（§2 的 SOEP/IFLS 边界） |
| U11 | ML-SAAF（Midwest Longitudinal Study of Asian American Families，含跨种族伴侣）access 状态与 wave 数 | `UNKNOWN_AS_OF` |
| U12 | SNAP（Timmermann, Nowak & Krabill 2015）纵向友谊网络数据可申请性 | **本 lane 未核实，不作主张** |
| U13 | 北欧/荷兰行政登记联动是否含伴侣级 linkage | `UNKNOWN`（SHARE 侧 linkage 项目存在性已核实） |
| U14 | 关系类 App / 日常日记研究是否有任何公开 de-identified release | `UNKNOWN_AS_OF` |
| U15 | **pairfam / SHARE / HARP 问卷中实际含哪些「关系状态」构念**（而非家庭经济/健康/人口变量） | **未核实**。这一项直接决定它们能否标定 LHRM 构念，是后续 lane 最应优先补齐的缺口 |
| **U16** | **（R3-A3b 新增）「LHRM 计划用途 + 受限数据 + LLM + 可得路径」的系统枚举** | **从未做过**。旧 §6/§10 的「唯一已知可行路径」即由此产生并已撤回。**Rights fail closed ⇒ 在枚举完成前按不可用处理。** 这是 §7 第 14 条非主张的依据 |
| **U17** | **（R3-A3b 新增）HRS CoU 页的直开核实** | `UNVERIFIABLE_HERE`：`https://hrsdata.isr.umich.edu/data-products/conditions-of-use` → **HTTP 403**；`https://hrs.isr.umich.edu/data-products/conditions-of-use` → **HTTP 403**（均 2026-09-27）。U4 的结论依 review-r2 `R-C4` 成立，但**本 packet 未直开**。若该禁令将被用于**可执行的**合规动作（如写进 DUA 申请模板），须由能打开该页者再取一次逐字文本 |
| **U18** | **（R3-A3b 新增）pairfam 的 (a) AI / LLM use condition 与 (b) release 波次数 / 版本号的当前值** | `UNVERIFIABLE_HERE`：`https://www.pairfam.de/en/data/data-structure/` → **HTTP 500**（2026-09-27）；`pairfam.de/en/data/data-access/` 与 `access.gesis.org` 的三个 dbk 链接**未打开**。⇒ 波次数 14 / 版本 14.2.0 是 **version-drift 风险**，在作承重输入前必须重新确认；rights 条文整体 `PLAUSIBLE`（U18 覆盖 §5.1 pairfam 行） |
| **U19** | **（R3-A3b 新增）SOEP AI and LLM Use Policy 的直开核实** | `UNVERIFIABLE_HERE`：5 个 URL 尝试全部失败（`diw.de/documents/1848/1848.pdf` → **500**；`/en/about-us/legal-terms/soep-terms-and-conditions/` → **404**；`/en/soep/soep-en/terms-of-use/` → **404**；`/en/soep/soep-en/data-and-terms-of-use/` → **404**；`/en/soep/soep-en/data-access/` → **404**；`/en/soep/soep-en/service/` → **404**）。`/en/soep/` 根页可达但为导航骨架（grep `LLM` / `artificial intelligence` / `Terms` = 0 命中）。⇒ §5.1 的 SOEP 行标 `CITED_SECONDARY`，**Rights fail closed** |
| **U20** | **（R3-A3b 新增）Add Health nomination 文件的存在性与结构 + SHARE release guide 的正文** | `UNVERIFIABLE_HERE`：Add Health `documentation/data-documentation/` 表格 **JS 渲染**（见 U7）；SHARE `SHARE_release_guide_9-0-0.pdf` 抓到二进制 PDF 但**未能抽取文本**。⇒ 本 packet 的 SHARE 断言**只**来自 CoU 页与 FAQ 页（两者已直开），**不**来自 release guide |

---

## 10. 建议状态（R3-A3b 重写）

**`status_recommendation: PARTIAL`（保留）**，但**理由结构已重写**：旧版把「发现了 2025–2026 的系统性收紧」列为**最有价值的产出**，该定位已撤回。

**达成的**：
- 16 个数据集审计（目标 12），每个都有 2026-09-27 的核实日期、稳定指针、逐项属性判定、**两轴分类**（`structural_verdict` × `access_rights_axis`）、逐格 `both_parties_answer_separately`（§4.17）、独立的非数值结构化来源清单。
- **R3-A3b 直开并逐字核对了 6 个官方页面**（SHARE CoU、SHARE FAQ、Add Health CoU、Add Health Data Documentation、ICPSR LLM policy、ICPSR Redistribution Policy、ICPSR SOMAR VDE）—— 这是本文件唯一一类"可以直接改文档、不需要新证据"的高置信事实。

**被撤回的（不可按现状引用）**：
1. 「ICPSR SOMAR VDE / MiCDA Enclave 是**目前唯一已知可行的『合规地用 LLM 处理受限数据』路径**」—— §6 + §10，两处，**已撤回**（VDE/PDE 内 `no LLMs available`；SOMAR VDE 范围限社交媒体；「唯一」是未做的枚举）。**R-C1 / C-C14。**
2. 「2025–2026 的**系统性**收紧」—— 改为**单源扩散**（§1.3）。**R-C7 / C-C36。**
3. 「HRS AI/LLM 政策条文未取得，**可能是最严的一份**」—— U4 已解，HRS 判为**禁止**。**R-C4 / C-C11。**
4. 「**ICPSR 全站 403**」—— 改为逐页分级的证据强度。**R-0.8 / C-C31。**
5. 「**§7 使 SHARE 派生量在法务上不能进入一个 LLM 参与的公开验证流水线**」—— 依 review-r2 `R-C3` 撤回，改为分层的可辩护表述（D02 卡）。**C-C2。**
6. 「SHARE 第 9/10 wave 官方页面**矛盾**」—— 改判 `UNKNOWN_AS_OF`（文档版本差）。**派工 item 14。**
7. 「四条件交集为空 = 本 landscape 最重要的结构性事实」—— 改为 15 个数据集的检索范围结果 + Add Health 从未进入结构检验。**R-0.2 / C-C29 + X-14。**
8. 「intensive longitudinal 关系日记数据**不存在**」—— 改为 16 个对象范围内的未发现。**R-0.3 / C-C30 + X-14。**
9. 「Add Health (**NLSY97/ECLS**)」标题 + 「**不主张** Add Health 存在 friendship nomination 数据文件」—— 均已更正。**R-C17 / C-C19 / C-C20。**
10. D12 / D13 `cannot_identify: 不可识别`、D15 `ACCESS_BLOCKED` 单轴 —— 已拆为两轴。**R-C5 / R-C6。**
11. §5.1 **缺 SOEP 行** —— 已补（`CITED_SECONDARY` + `UNVERIFIABLE_HERE`）。

**未达成的（故非 SUCCESS）**：
1. **U15 未解** —— 三个 `STRUCTURAL_CALIBRATION_CANDIDATE` 数据集的**构念内容**（而非结构）未核实。
2. **U1–U3 覆盖缺口** —— 三个文献常用核心 panel 无法访问，构成实质盲区。**这三个恰恰是最可能容纳密集日记设计的对象**（U14 / §8.8）。
3. **U16 未做** —— 「受限数据 + LLM 的可行路径」的系统枚举从未做过。旧版的"唯一路径"断言即由此产生。**这是本文件第二轮最该补的缺口。**
4. **U17 / U19 = `UNVERIFIABLE_HERE`** —— HRS CoU 与 SOEP AI/LLM 政策，R3-A3b 本人未能直开（403 / 500 / 404）。相关表述为转述。
5. **U7 / U20** —— Add Health nomination 文件（JS 渲染）与 SHARE release guide（PDF 无法抽取）未取得。
6. **D09 `STRUCTURAL_MEASUREMENT_ONLY_PENDING`** —— 按报告自己的判据该判定应为更高或更低，两条方向的一手证据都未取得。

**建议的后续动作（AI recommendation，非 Human requirement；P2 已按 §6 撤回重写）**：

| 优先级 | 动作 | 目标 lane | R3-A3b 备注 |
|---|---|---|---|
| P0 | 取得 pairfam / SHARE / HARP 的 codebook / scales manual 中**关系状态类题项**清单（解 U15） | R03 或本 lane 二轮 | 仍是最高优先；它决定三个 `STRUCTURAL_CALIBRATION_CANDIDATE` 是否真的可用 |
| **P0（新）** | **做 U16：「LHRM 计划用途 + 受限数据 + LLM + 可得路径」的系统枚举。** 在此之前，任何受限数据 + LLM 按不可用处理 | 本 lane 二轮 / Architect | **R3-A3b 新增。** 这是旧版"唯一路径"断言失败后留下的空洞 |
| P0 | ~~取得 HRS CoU（2026-02-04）AI/LLM 政策全文（解 U4）~~ | — | **已完成（依 review-r2 `R-C4`）**；剩余的是 U17（直开核实），仅在需要可执行动作时才做 |
| P1 | 换网络环境重试 `familylifesurvey.org` / `lsaf.org` / `nsmshow.org` / `nichd.nih.gov`（解 U1–U3） | 本 lane 二轮 | 仍成立；且这三个是 §8.8 / §8.9 两条否定结果的主要盲区 |
| P1 | 向 Architect 提交「Case Bank 材料增加 `llm_use_condition` 字段」的建议 | R15 / Architect | 旧 §5.2 建议 1，**保留**。R3-A3b 建议把取值域改为**引用上游的 Type 1/2/3 与 SOEP/Add Health 的全 None**，而不是自造枚举 |
| ~~P2 | 调研 ICPSR SOMAR VDE / MiCDA Enclave 内自托管模型的实际可行性~~ | — | **已撤回**：ICPSR LLM policy 明文 "At present, **no LLMs are available within the VDE or PDE**, so this is not an option."。**不再作为后续动作派工。**（SOMAR VDE 是另一个环境，未被此条否决，但它服务社交媒体数据，不服务本文件的问卷型数据集。） |
| P2 | 核实 U10（PSID / NLSY / Understanding Society 扩展文件的 partner id），以判断是否存在低成本 dyad 重建路径 | R05 / R07 | 仍成立；与 §2 的 SOEP/IFLS 边界直接相关 |
| **P2（新）** | 确认 HARP / CLOC / NSFH / SECCYD / D15 中哪些属 "deposited by individual investigators"（⇒ members only, cannot be redistributed） | 本 lane 二轮 | **R3-A3b 新增**，来自 §5.1a 的 ICPSR Redistribution Policy 逐字条款 |
| **P2（新）** | 对 Add Health 做**结构检验**（含 nomination 文件，U7），使其进入 §8.9 的样本框 | 本 lane 二轮 | **R3-A3b 新增**。在此之前 §8.9 的样本框只能是 15 |

---

## 11. R3-A3b 取代记录（`supersessions`）

> 契约 §3.7：被裁决取代的旧文本逐条列出「原文 + 取代依据」。**原文本均已在正文相应位置以引用块或表格行逐字保留。**

| id | 位置 | 被取代的原文（逐字要点） | 取代依据 | 落地形态 |
|---|---|---|---|---|
| **S-04-1** | §6 表末行 + §10 | 「这是目前**唯一已知可行的『合规地用 LLM 处理受限数据』路径**」 | review-r2 `R-C1` / `C-C14`（"本 packet 中唯一的、会导致真实合规后果的错误"）；adjudication **X-14** | §6 拆为**三条分别成源、各带条件与出处**的陈述；新增「ICPSR VDE/PDE」与「SOMAR VDE」两行；§10 P2 行动项撤回 |
| **S-04-2** | §1.2 末 + §10 | 「横跨 SHARE / ICPSR / Add Health / UAS / HRS 的**系统性**约束」/「**系统性**收紧」 | review-r2 `R-C7` / `C-C36`（改述为**单源扩散**；ICPSR `Approved: December 11, 2024`；Add Health / SOEP 各自溯源到 HRS + ICPSR + Karcher） | 新增 §1.3 独立性核算表（6 行，含 R3-A3b 的直开/未直开标注） |
| **S-04-3** | §1.1 + §9 U4 + §10 | 「HRS CoU … 关于 AI/LLM 的具体条文未取得 … `UNKNOWN_AS_OF`（U4）**不得猜测条文内容**」；§10「而这**可能是最严的一份**」 | review-r2 `R-C4` / `C-C11`（"不可得前提已被推翻"）；`H-C1` `VERIFIED` | U4 改为**已解**；HRS 的 AI/LLM 分级由「含新政策（未知）」改为「**禁止**」；条文标 `CITED_SECONDARY`；R3-A3b 的 403 记为 `UNVERIFIABLE_HERE`（U17） |
| **S-04-4** | §8.6 | 「**ICPSR 全站 403**」 | review-r2 `R-0.8` / `C-C31`（"本报告中所有 ICPSR 系证据强度为 MEDIUM"） | 改为**逐页分级**：ICPSR **policy 页 = `CITED_PRIMARY`（R3-A3b 直开）**；ICPSR **study 页 = relay**。R3-A3b 列出 3 个直开成功的 URL |
| **S-04-5** | §8.6 | 「`hrs.isr.umich.edu` 正文反复 timeout/403 ⇒ U4 记「条文 `UNKNOWN_AS_OF`」的**后果** | review-r2 `R-0.9` / `C-C33`（"**失败记录真实，但后果被高估**"）；adjudication §C item 6 | 失败记录保留于 §8.6 + §12；**后果删除**（U4 已解） |
| **S-04-6** | §8.8 | 「「intensive longitudinal 关系日记数据」**在本 landscape 中不存在公开可得的**」 | adjudication **X-14**；review-r2 `R-0.3` / `C-C30` | 改为「**在本审计的 16 个对象中未发现**」+ 样本框说明（U1–U3 三个核心 panel 从未访问） |
| **S-04-7** | §8.9 | 「**这四个条件的交集为空。这是本 landscape 最重要的结构性事实，比任何单个数据集的优劣都重要。**」 | adjudication **X-14**；review-r2 `R-0.2` / `C-C29` | 改为**本次检索的结构性结果**，样本框 = **进入结构检验的 15 个**；显式记录 **Add Health 从未进入结构检验**；列出仍可保留的三条局部观察；声明**既不主张成立也不主张反面** |
| **S-04-8** | D02 卡片 + §5.1 SHARE 行 | 「**§7 使 SHARE 派生量在法务上不能进入一个 LLM 参与的公开验证流水线。**」 | review-r2 `R-C3` / `C-C2`（"§7 是限制**使用与再分发**，不是禁止派生量进入流水线"） | D02 卡重写：逐条拆出 §7 实际管的三件事 + 继承条款的正确读法；给出**不构成权利升级**的替代定位（风险判断，非法律解读） |
| **S-04-9** | D02 卡片 §11 | 「立即撤销使用权、要求删除全部副本；**严重违反**可在网上公开违规者身份」 | review-r2 `R-C2` / `C-C3`（补 `(cf. 6. above)` 限定） | 改为 §11 逐字全文 + 完整触发条件四要素（intentional/serious · §6 数据保护与隐私规则 · **或未遂** · `cf. 6. above`） |
| **S-04-10** | §8 矛盾 1 + D02 `waves` | 「**SHARE wave 数：官方站点内部不一致** … 这是官方文档矛盾」 | 派工 item 14（"the wave-9/10 'official pages conflict' item is a `UNKNOWN_AS_OF`, **not a contradiction**"） | 改判为 `UNKNOWN_AS_OF`；记录 2026-09-27 直开观察（导航到 Wave 9；FAQ 4.3 列 Wave 9 (2021–2022) 常规 wave；FAQ 2.1 文档表仍到 Wave 8）；旧文本在 §8.1 引用块保留 |
| **S-04-11** | D02 卡片 | （旧版无 proxy interview 条目）`both_parties_answer_separately` 作数据集级属性 | 派工 item 14（"SHARE permits partly/fully **proxy** interview … which qualifies the 'both parties answer separately' cell"） | 新增 `proxy_interview` 段（FAQ 3.4 逐字）+ `both_parties_answer_separately` **逐模块表** + 新增 §4.17 全局逐格表；`CALIBRATION_READY` 定义删除该数据集级条件 |
| **S-04-12** | D02 卡片 | （旧版无 CH 缺陷条目） | 派工 item 14（"add the official warning that `CH` module ordering/linkage is unreliable"） | 新增 `CH_module_known_defect`（FAQ 5.8 逐字）+ `CH_to_SP_FT_linkage_defect`（FAQ 5.9 逐字，Wave 4 特例） |
| **S-04-13** | D12 标题 + 主表 | 「Add Health (**NLSY97/ECLS**)」 | review-r2 `R-C17` / `C-C19` | 改为「The National Longitudinal Study of Adolescent to Adult Health (Add Health)」（CoU 页页脚逐字） |
| **S-04-14** | §7 非主张 6 + D12 卡 | 「**不主张** Add Health 存在 friendship nomination 数据文件（U7）」 | review-r2 `R-C17` / `C-C20`；adjudication §C item 6 | **撤回**，改为**双向非主张**（既不主张存在也不主张不存在）+ 记录「JS 渲染 ⇒ `UNVERIFIABLE_HERE`」+ `REPORTED_SECONDARY`（`C-C20`）+ 复通条件 |
| **S-04-15** | D12 / D13 卡片 + 主表 | `cannot_identify: 对 LHRM 计划用途 —— **不可识别**`；`ACCESS_BLOCKED` | review-r2 `R-C6` / `C-C26`（"许可条件 ≠ 识别能力"） | §2 拆为两轴；字段拆为 `cannot_identify_structurally` / `cannot_identify_for_LHRM_use` / `structural_dependencies_unverified`；D12 增设 `structural_examination_status = 从未进入结构检验` |
| **S-04-16** | D15 卡片 + 主表 | `classification: ACCESS_BLOCKED`（单轴，压掉结构轴） | review-r2 `R-C5` / `C-C27` | 改为 `structural_verdict = STRUCTURAL_MEASUREMENT_ONLY` + `access_rights_axis = ACCESS_BLOCKED_POSSESSION`；四条「不主张」显式列出 |
| **S-04-17** | D01 卡片 | 「官方 GESIS 变量清单中 partner 侧变量**统一** `p` 前缀」 | review-r2 `R-C18` / `C-C21` | 改为「partner 侧变量**主用**（mainly）`p` 前缀」+ 记录 R3-A3b 抓取 500 ⇒ relay |
| **S-04-18** | D01 卡片 | `rights_and_limits (CITED_PRIMARY 原文摘要)` …「§3 的『仅可汇总呈现』意味着 **不能把 pairfam 个体记录或其直接派生进入 Case Bank**」 | 派工 item 14（"rights assertions stay `PLAUSIBLE` with explicit gaps"） | rights 整体降为 **`PLAUSIBLE`（`CITED_SECONDARY`）** + 四条显式缺口；波次数标 **version-drift 风险**（U18）；**Rights fail closed 方向的替代处置**（不是放宽） |
| **S-04-19** | D08 卡片 | 「配偶关系质量是单方报告 … **Z[i→j] 与 Z[j→i] 在 NSFH 中不可分离**」（由 Wave 1 一句外推全 series） | review-r2 `R-C16` / `C-C35`（"限定为 **Wave 1 单方报告（已核实）；Wave 2 及以后未核实**"） | 改为「**Wave 1 单方报告（已核实）；Wave 2+ `UNKNOWN_AS_OF`**」+ 双向不主张；亲子方向资产独立保留；追加「NSFH 非概率抽样」对「最著名的家庭纵向调查」定位的限定 |
| **S-04-20** | D09 卡片 | `classification: MEASUREMENT_ONLY`（justification = 「条件于丧偶」= **外推限制**） | 派工 item 14（"the current justification (sample conditioned on bereavement) is an **extrapolative limitation** and does not match the report's own stated criteria"） | 改为 **`STRUCTURAL_MEASUREMENT_ONLY_PENDING`**；按 §2.1 判据**逐条重判**（7 项中 6 项满足）；给出真正的待决理由（"Couples Only" 子集的选择规则 `UNKNOWN`）与复通条件；另立**全文件记账通则**（外推限制 ≠ 结构判据） |
| **S-04-21** | D11 vs D06 | SOEP 判 `NOT_DYADIC_ENOUGH`、IFLS 判 `MEASUREMENT_ONLY`（同一现象、两个标签） | 派工 item 14（"The SOEP vs IFLS boundary is applied inconsistently in the same file; make the boundary explicit and single"） | D11 新增 `SOEP_ifls_boundary` 统一边界表（3 个判据 × 2 数据集）；两者的 rights 侧单独记账 |
| **S-04-22** | §5.1 汇总表 | **缺 SOEP 行** | `H-C1`（"`04` §5.1 权利汇总表没有 SOEP 行"）；派工 item 14 | 补入 SOEP 行（Type 1/2/3 全 None；Type 3 因 sandbox escape 不可靠而拒）+ `UNVERIFIABLE_HERE`（U19） |
| **S-04-23** | §5.1 汇总表 + 各 ICPSR 卡 | 「须 ICPSR 书面许可（Redistribution Policy）」（**漏机制、漏成员限定、漏 LLM=再分发**） | 派工 item 14（"add the redistribution-policy requirement … and the member-only redistribution of individually-held studies"） | 新增 §5.1a（两页逐字 + 三条跨卡片后果） |
| **S-04-24** | §2 | `CALIBRATION_READY` 等 5 类单轴分类 | 派工 item 14（"`CALIBRATION_READY` must become a **two-level** label"；"separate the **structural axis** from the **access/rights axis**"） | §2 重写为三节：轴一 `structural_verdict`（5 值）· 轴二 `access_rights_axis`（5 值）· 轴三逐格 `both_parties_answer_separately` + 新增 §4.17 |
| **S-04-25** | §3 主表 | 「完全公开无门槛（可立即下载）」 | review-r2 `R-C13`（"全文把「完全公开」统一改为「**技术上零门槛可下载（第三方镜像）**」"） | 统一措辞；§5.1 speed dating 行同步；§8.9(d) 同步 |

---

## 12. R3-A3b 抓取记录（2026-09-27）

**成功直开并逐字核对（6 组）**：

| # | URL | 用于 |
|---|---|---|
| 1 | `https://share-eric.eu/data/data-access/conditions-of-use` | §5.1 SHARE 行 · D02 `rights_and_limits` §2 / §6 / §7 / §11 / §12 |
| 2 | `https://share-eric.eu/data/faqs-support` | D02 `dyad_identifiability`(5.3) · `directionality`(3.3) · `proxy_interview`(3.4) · `waves`(4.3) · `CH_module_known_defect`(5.8) · `CH_to_SP_FT_linkage_defect`(5.9) · `non_married` / `age_limits`(3.2) |
| 3 | `https://addhealth.cpc.unc.edu/conditions-of-use/` | D12 `critical_rights_finding` 全文 · §5.1 Add Health 行 · §1.3 单源扩散溯源 · 页脚确认研究全名 |
| 4 | `https://addhealth.cpc.unc.edu/documentation/data-documentation/` | **页面可达，但文件清单表 JS 渲染** → U7 / U20 |
| 5 | `https://www.icpsr.umich.edu/sites/icpsr/about/policies/large-language-models-and-ai` | §5.1a · §6 ICPSR VDE/PDE 行 · §1.3 `Approved: December 11, 2024` + Karcher 溯源 |
| 6 | `https://www.icpsr.umich.edu/sites/ICPSR/about/policies/redistribution` | §5.1a（Data Stewardship Policy Committee · Bylaws Art. 1.2.B · LLM=再分发 · members only） |
| 7 | `https://www.icpsr.umich.edu/sites/somar/somar-vde-overview-and-resources` | §6 SOMAR VDE 行（社交媒体范围限定 · 自托管模型清单 · $371/月 + $1,000） |

**失败（`UNVERIFIABLE_HERE`）—— 一律不由失败推出结论**：

| # | URL | 状态 | 落到哪 |
|---|---|---|---|
| F1 | `https://hrsdata.isr.umich.edu/data-products/conditions-of-use` | **HTTP 403** | U17 · D10 |
| F2 | `https://hrs.isr.umich.edu/data-products/conditions-of-use` | **HTTP 403** | U17 · D10 |
| F3 | `https://www.diw.de/documents/1848/1848.pdf` | **HTTP 500** | U19 · D11 |
| F4 | `https://www.diw.de/en/about-us/legal-terms/soep-terms-and-conditions/` | **HTTP 404** | U19 |
| F5 | `https://www.diw.de/en/soep/soep-en/terms-of-use/` | **HTTP 404** | U19 |
| F6 | `https://www.diw.de/en/soep/soep-en/data-and-terms-of-use/` | **HTTP 404** | U19 |
| F7 | `https://www.diw.de/en/soep/soep-en/data-access/` | **HTTP 404** | U19 |
| F8 | `https://www.diw.de/en/soep/soep-en/service/` | **HTTP 404** | U19 |
| F9 | `https://www.diw.de/en/soep/` | **200，但为导航骨架**（`LLM` / `artificial intelligence` / `Terms` grep = 0 命中） | U19 |
| F10 | `https://www.pairfam.de/en/data/data-structure/` | **HTTP 500** | U18 · D01 |
| F11 | `https://share-eric.eu/fileadmin/user_upload/Release_Guides/SHARE_release_guide_9-0-0.pdf` | 200，但**二进制 PDF，未能抽取文本** | U20 · D02 `codebook` |
| F12 | （Crossref 无关）`https://www.psychology.unl.edu/williams/PerceivedInclusion.html` | **Transport error** | 属 `03` 的 U25（A17 PICS） |
| F13 | 旧 report 记的 `familylifesurvey.org` / `lsaf.org` / `nsmshow.org` / `nichd.nih.gov` | `FETCH_FAILED`（旧 report） | U1–U3 —— **R3-A3b 未重试** |

**纪律声明**：
- 失败记录**全部保留**，且**没有一处**被用来推出"某物不存在"或"某政策内容未知"。
- 上表 11 个 R3-A3b 失败项中，**只有 F1–F2 与 F10 影响了既有断言的方向**，且影响的**方向是收紧**
  （HRS 由"未知"改为"按禁止处理"；pairfam 由 `CITED_PRIMARY` 降为 `PLAUSIBLE`），**不是放宽**。
- **Rights fail closed 仍在执行。R3-A3b 没有放宽任何数据集的任何一条权利条件。**


---

## 13. 引用清单（stable pointers，核实日期均为 2026-09-27）

> **R3-A3b 的证据等级分布**（依 review-r2 `R-C8` / `C-C34` 的「全站 MEDIUM」过度概括修正）:
> `CITED_PRIMARY (R3-A3b 直开逐字)` = 7 组 URL，见 §12 · `CITED_PRIMARY (relay)` = 大部分条目页
> （含全部 ICPSR `/web/...` study 页、UAS、AFC、GUiNZ、IFLS、DHS、pairfam）·
> `CITED_SECONDARY` = 学术论文方法节（SOEP couples 构造）· `PLAUSIBLE` = pairfam rights 整块 ·
> `UNVERIFIABLE_HERE` = §12 的 11 条失败记录。
> **本文件仍声明零数据接触** —— 这些标签全部属于**文档接触**层，与**数据接触**层正交（见 §2.4）。


```text
SHARE-ERIC
  https://share-eric.eu/data/data-access
  https://share-eric.eu/data/data-access/conditions-of-use            (Last updated: April 30, 2026)
  https://share-eric.eu/data/data-documentation
  https://share-eric.eu/data/faqs-support
  https://share-eric.eu/fileadmin/user_upload/Release_Guides/SHARE_release_guide_9-0-0.pdf
  https://share-eric.eu/fileadmin/user_upload/Other_Publications/Data_Management_Plan.pdf
  https://share.cerge-ei.cz/en/faq/index.html
  DOIs: 10.6103/SHARE.w1.900 ... 10.6103/SHARE.w8.900

pairfam / GESIS ZA5678
  https://www.pairfam.de/en/data/data-access/
  https://www.pairfam.de/en/data/data-structure/
  https://access.gesis.org/dbk/52241
  https://access.gesis.org/dbk/53708
  https://access.gesis.org/dbk/69762
  https://www.gesis.org/en/services/finding-and-accessing-data/selected-german-research-projects/pairfam
  Brüderl, Edinger, Eigenbrodt, Garrett, Hajek, Herzig, Lorenz, Schütze, Schumann & Timmermann (2024).
    pairfam Data Manual, Release 14.2. LMU Munich: Technical Report. GESIS Data Archive, Cologne.
    ZA5678 Data File Version 14.2.0. https://doi.org/10.4232/pairfam.5678.14.2.0
  Naujoks, T. (2024). The Division of Housework and Childcare from a Dyadic Perspective.
    Demographic Research 51(30). https://www.demographic-research.org/volumes/vol51/30/files/readme.51-30.txt

ICPSR / NACDA
  https://www.icpsr.umich.edu/sites/icpsr/about/policies/large-language-models-and-ai
  https://www.icpsr.umich.edu/sites/ICPSR/about/policies/redistribution
  https://www.icpsr.umich.edu/sites/nacda/home
  https://www.icpsr.umich.edu/sites/somar/somar-vde-overview-and-resources
  https://www.icpsr.umich.edu/web/NACDA/studies/37404        (HARP; 2014-2015 vs 2014-2025 页面矛盾)
  https://www.icpsr.umich.edu/web/ICPSR/studies/3370          (CLOC)
  https://www.icpsr.umich.edu/web/NAHDAP/studies/38726       (Oregon Youth Study Couples Study)
  https://www.icpsr.umich.edu/web/ICPSR/series/193           (NSFH)
  https://www.icpsr.umich.edu/web/DSDR/studies/6906          (NSFH W2)
  https://www.icpsr.umich.edu/web/ICPSR/series/00233         (SECCYD)
  https://www.icpsr.umich.edu/web/DSDR/studies/21940         (SECCYD Phase I)
  https://www.icpsr.umich.edu/web/DSDR/studies/22361         (SECCYD Phase IV)
  https://liberalarts.utexas.edu/health-relationships-lab/about-harp/
  (注: 本 lane 对 icpsr.umich.edu 直接抓取一律 403；以上内容经搜索引擎索引的同一页面取得，
   evidence_type = CITED_PRIMARY（索引）, strength = MEDIUM)

Add Health
  https://addhealth.cpc.unc.edu/conditions-of-use/            (含完整 AI and LLM Use Policy)
  https://addhealth.cpc.unc.edu/documentation/
  https://addhealth.cpc.unc.edu/documentation/data-documentation/

DHS
  https://dhsprogram.com/data/Guide-to-DHS-Statistics/Analyzing_DHS_Data.htm
  https://www.dhsprogram.com/data/Merging-Datasets.cfm
  https://dhsprogram.com/pubs/pdf/DHSG1/Guide_to_DHS_Statistics_DHS-8.pdf
  https://dhsprogram.com/pubs/pdf/mr19/mr19.pdf
  https://userforum.dhsprogram.com/index.php?S=Google&t=msg&th=1369

RAND / IFLS
  https://www.rand.org/health/surveys/FLS/IFLS/study.html
  https://www.rand.org/health/surveys/FLS/IFLS/datanotes.html
  https://www.rand.org/content/dam/rand/pubs/working_papers/WR1100/WR1143z2/RAND_WR1143z2.pdf
  https://www.rand.org/health/surveys/FLS/IFLS/access.html
  Strauss, Witoelar, Sikoki & Wattie (2009). The Fourth Wave of the Indonesia Family Life Survey (IFLS4).
    RAND WR-675.  /  Strauss, Witoelar, Sikoki et al. IFLS5 User's Guide Vol.2. RAND WR-1143.

Growing Up in New Zealand
  https://www.growingup.co.nz/
  https://www.growingup.co.nz/data-access-application-growing-up-in-new-zealand
  https://www.growingup.co.nz/available-data-disclaimer

HRS
  https://hrs.isr.umich.edu/
  https://hrs.isr.umich.edu/data-products                              (banner: CoU updated 02/04/2026)
  https://hrs.isr.umich.edu/data-products/file-merge-reference
  https://hrs.isr.umich.edu/sites/default/files/rda-forms/HRS-RDA-MiCDA-Access-Agreement.pdf
  https://hrs.isr.umich.edu/data-products/restricted-data/faqs

American Family Cohort
  https://americanfamilycohort.org/how-to-access-afc-data/

Understanding America Study
  https://uasdata.usc.edu/

Speed dating
  https://github.com/datasets/speed-dating
  https://www.openml.org/d/40536
  https://osf.io/8k7rf/
  Huang, Yeomans, Brooks, Minson & Gino (2017). "It Doesn't Hurt to Ask: Question-Asking Increases
    Liking." JPSP. doi:10.1037/pspi0000097

CLS (英国 cohort 关系/生育 harmonised histories)
  https://cls.ucl.ac.uk/wp-content/uploads/2017/02/CLS_Data_Access_Framework.pdf
  https://cls.ucl.ac.uk/wp-content/uploads/2017/02/Webinar-slides-Families-and-relationships-in-four-British-cohort-studies.pdf

方法学反面教材
  Bacon, P., Conte, A.M. & Moffatt, P.G. (2014). "Assortative mating on risk attitude."
    Theory and Decision. https://link.springer.com/content/pdf/10.1007/s11238-014-9448-x.pdf
  Seltzer, J.A., Bachrach, C.A., Bianchi, S.M., Bledsoe, C., Casper, L.L., Chase-Lansdale, P.L. et al. (2005).
    "Explaining Family Change and Variation: Challenges for Family Demographers." JMF 67(4):908-925.

抓取失败（FETCH_FAILED，2026-09-27）
  https://www.familylifesurvey.org/      (TLS 握手失败 x4)
  https://www.lsaf.org/                  (连接失败)
  https://nsmshow.org/                   (连接失败)
  https://www.nichd.nih.gov/research/supported/seccyd  (URL rejected)
  hrs.isr.umich.edu 正文页 (timeout / 403)
```

R3-A3b 抓取补充（2026-09-27；失败项的完整清单见 §12）
  https://hrsdata.isr.umich.edu/data-products/conditions-of-use   (403, 2026-09-27 -> U17)
  https://www.diw.de/documents/1848/1848.pdf                      (500, 2026-09-27 -> U19)
  https://www.pairfam.de/en/data/data-structure/               (500, 2026-09-27 -> U18)
  share-eric.eu .../SHARE_release_guide_9-0-0.pdf                (200 but text not extractable -> U20)
  addhealth.cpc.unc.edu/documentation/data-documentation/      (200 but file table is JS-rendered -> U7 / U20)
  R3-A3b 直开成功: share-eric.eu CoU + FAQ · addhealth.cpc.unc.edu CoU + DataDoc ·
  icpsr.umich.edu LLM-policy + Redistribution + SOMAR-VDE  (见 §12 表)
