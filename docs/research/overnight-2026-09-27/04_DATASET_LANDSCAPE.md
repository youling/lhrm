# 04 — Quantitative dyadic / longitudinal dataset landscape

- Lane: **R04**（Wave 1, overnight-opencode-exploration-swarm-v1）
- 角色: Research child（Fresh Research）｜ 无 GitHub 写权限，产出交 parent 做 durable writeback
- 核实日期: **2026-09-27**（全文所有 access 条件均以此日期为准）
- 状态: `RESEARCH_CANDIDATE`。本文件不是 canonical architecture，不含已确立的结论、参数或公式。
- 边界声明: 本 lane 只做 **consumer-side suitability audit**，**未接触任何数据文件**，**未克隆/读取 Eye 仓库**，**未重复 Eye 的 data-acquisition 工作**，**未绕过任何 access control**，**未修改 `docs/` 下任何文件**。

> **阅读提示（重要）**
> 本文件严格区分两件经常被混为一谈的事：
> 1. **「我们能用这个数据集」** = 该数据的**结构**支持方向化 (i→j / j→i)、纵向、部分信息二人状态模型；
> 2. **「我们能拿到这个数据集」** = 今天存在一条可复现、合规、且**允许 LHRM 计划用途**的获取路径。
>
> 本文件的主要发现之一（见 §5）就是：**在这两件事之间，2026-09 存在一条正在变宽的裂口。** 多个主力数据集的 use conditions 已在 2025–2026 年被收紧到禁止 LLM/AI 处理个体级数据。

---

## 1. 结论摘要

### 1.1 审计规模

| 项 | 数值 |
|---|---|
| 严肃 quantitative dyadic / longitudinal dataset 审计数 | **16** |
| 其中双方各自独立作答同一构念 | **4**（pairfam、SHARE、HARP、HRS 部分模块） |
| 其中 `CALIBRATION_READY` | **3**（pairfam、SHARE、HARP） |
| 其中带 intensive-longitudinal（密集日记）设计 | **1**（HARP，8–10 天日记 × 3 个时间点） |
| 覆盖国家/地区（跨文化） | 德国、欧盟 27+ 国、印尼、新西兰、美国、约 90 个 DHS 参与国 |
| 覆盖关系类型 | 已婚、同居/未婚、丧偶后随访、离婚/分居后续访、恋爱（首次约会）、亲子/代际、照护-被照护、青少年同伴关系（文件层未核实） |
| 覆盖同性关系 | **2** 有明确设计（HARP、pairfam `homosex`）；其余为 0 或未核实 |
| 完全公开无门槛（可立即下载） | **1**（Fisman–Iyengar speed dating 公开镜像） |

### 1.2 一句话结论

> **在方向化（i→j / j→i）双人自报 + 纵向 + 双方各自作答这三个条件同时成立的数据集里，本审计只找到 3 个（pairfam / SHARE / HARP），全部在 DUA 之后；而完全公开的那一个（speed dating）没有任何纵向结构。同时，Add Health、UAS、SHARE、ICPSR 已在 2025–2026 明确限制或禁止用 LLM/AI 处理个体级数据。LHRM 的 Case Bank 与 validation corpus 若要引入问卷型数据，必须先解决权利层问题，而不是先解决统计层问题。**

---

## 2. 判级标准

| 分类 | 定义 | 判定要点 |
|---|---|---|
| `CALIBRATION_READY` | 结构上足以支撑方向化纵向状态模型 | 稳定 dyad id + **双方各自作答** + ≥3 wave + codebook + outcome/event + 缺失/样本选择文档 + 可复现获取路径 |
| `MEASUREMENT_ONLY` | 可用作测量来源，但不足以支撑转移律或方向性分解 | 缺 1 wave / 双方测量不对称需外部假设 / 只有 pair-level 事实 / outcome 无后续时点 |
| `REPRESENTATION_ONLY` | 只用于让模型看到关系表述形态，不做参数估计 | **本 landscape 无此类 quantitative dataset**；该角色由 `VALIDATION_CORPUS_V0_1.md` 的叙事材料承担 |
| `ACCESS_BLOCKED` | 权利或使用条件使 LHRM 计划用途不可行，或获取需跨机构审批且无法确认可获得 | 须区分 *possession block*（拿不到）与 *use-condition block*（拿到了但不许这样用） |
| `NOT_DYADIC_ENOUGH` | **发货形态**没有可用 partner id，dyad 需分析者启发式重建 | 重建规则是模型假设，不是证据 |

---

## 3. 主表

| ID | Dataset | 主办方 | 关系类型 | 双方独立作答 | Waves | 稳定 couple id | Codebook | Outcome/Event | Missingness/选择文档 | 跨文化 | 同性 | 未婚/同居 | 非浪漫/kin | Access 路径（2026-09-27） | 分类 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D01 | **The German Family Panel (pairfam)** / ZA5678 | LMU Munich + MPIDR，GESIS FDZ 分发 | 婚恋+家庭+亲子+代际 | **是**（`anchor$` + `partner$`） | **14**（年度，2008/09–，含 DemoDiff/refreshment/step-up） | 是（`id` + `pid`，标准 key 变量可链接） | 是（14 wave 英/德 codebook + 问卷 + Data Manual + method reports） | 是（`biopart` 关系生命史 + 生育/健康/就业） | 是（method reports、`sample`/`cohort`/`demodiff` 标记） | 仅德国 | **是**（`homosex` / `homosex_new`） | 是（`relstat`/`marstat`） | 是（`parent$` 至 wave 8；`child$` 8–15 岁） | 免费；签署 user contract / Nutzungsantrag 交 GESIS；DOI 版本化（当前 14.2.0） | `CALIBRATION_READY` |
| D02 | **SHARE** (Survey of Health, Ageing and Retirement in Europe) | SHARE-ERIC，FDZ-SHARE (CentERdata / GESIS) | 婚恋+家庭经济+照护+健康 | **是**（`mergeidp*w` = partner 的 mergeid） | **≥8 完整常规 wave**（2004–）+ 2 轮 COVID；第 9/10 wave 官方表述冲突 | **是**（`coupleid*w`，couple 不变则跨波固定） | 是（Release Guide、cross-wave comparison、methodology volumes、Scales Manual） | 是（SHARELIFE 回溯生命史；健康/退休/就业事件） | 是（methodology volumes、longitudinal weights、coverscreen `gv_allwaves_cv_r`） | **欧盟 27+ 国 + Israel** | 部分轮次含 | 是 | 是（`CH`/`SP` 模块；kin） | 免费；个人注册 + SHARE User Statement | `CALIBRATION_READY` |
| D03 | **Health and Relationships Project (HARP)** / ICPSR 37404 | UT Austin（Umberson 等），ICPSR/NACDA | 已婚婚恋 + 健康 + 日常压力 | **是**（明令 spouses 分开作答） | **3 个时间点**（2014-15 / 2021-22 / 2024-25）**各含 8–10 天日记** | 是（couple-level recruitment + couple ids） | 是（baseline + diary 问卷、ICPSR datadocumentation） | 是（关系质量、健康、压力、离婚/分居/丧偶状态） | **是（最详细）**：逐时间点留存 n、分批投放设计、激励变化、per-diary 完成率 | 美国（马萨诸塞州） | **是**（同性+异性） | **否**（要求合法婚姻 + 同居≥3 年） | 否 | ICPSR 公版；"public-use data files are available for access by the general public"（但本环境 403，见 §8） | `CALIBRATION_READY` |
| D04 | **Fisman & Iyengar Speed Dating Experiment** (2002–2004) | Columbia Business School | **首次约会**（4 分钟速配） | **是**（`dec` 单方意愿 + `match` 互惠 + 6 项双向评分） | `wave` = **21 场 session**，非同一 dyad 的重复观测 | 是（`wave` × 配对 id） | 是（Speed Dating Data Key） | 弱（仅「想不想再见」） | 弱（无官方 missingness 文档） | 美国（Columbia 活动） | **否**（"participant of the opposite sex"） | 否 | **是（关系形成前的最短交互）** | **完全公开**：github.com/datasets/speed-dating（2026-09-27 HEAD 200）、OpenML d/40536、OSF 8k7rf | `MEASUREMENT_ONLY` |
| D05 | **DHS Couples (CR) file** | The DHS Program | 婚恋（couple 为分析单位） | **是**（双方自述配对后链接） | **单轮/国** | 是（couple file 一对一条；ID 取女方 `caseid`） | 是（Guide to DHS Statistics、recode file naming、codebook） | 是（生育、避孕、HIV、健康、决策权、暴力） | 是（采样/权重/抑制规则、Data Suppression 章节） | **约 90 个 DHS 参与国** | 事实婚姻制国家极少 | 是（living together 计入） | 否 | 免费；电子注册 + 授权后下载 | `MEASUREMENT_ONLY` |
| D06 | **Indonesia Family Life Survey (IFLS1–IFLS5)** | RAND + 印尼合作机构 | 家庭+婚恋+亲属转移 | 部分（household head + spouse；`BA`/`TF` 亲属模块） | **5**（1993-94 / 1997 / 1998(25%子样本) / 2000 / 2007-08 / 2014-15） | **未核实**（官方 FAQ 指向 IFLS2 User's Guide 的 spouse 识别章） | 是（每波 6–7 卷：overview、user's guide、问卷、codebook、crosswalk） | 是（婚姻/生育/迁移/健康/教育/就业/亲属转移） | 是（re-contact 率、分波实地日期、`fixes` 文件、split-off 规则） | 印尼 13 省（≈83% 人口） | 未专项 | 是 | **是（非同住亲属 + 亲属转移）** | 免费；RAND 注册 + confidentiality declaration；**"Please do not distribute these data"**；受限地理码需另申请 | `MEASUREMENT_ONLY` |
| D07 | **Growing Up in New Zealand (GUiNZ)** | University of Auckland | 亲子 + 青少年家庭 + 同住伴侣 | 部分（家庭成员 id 齐） | **~9**（2009 起；17 岁 wave 2026-05 启动） | 是（家庭成员 id） | 是（Data User Guides / Data Dictionaries / Questionnaires，需先接受 legal disclaimer） | 是（健康、发展、家庭、极端天气事件） | 是（Data Access Protocol 2026 v1.0、Data Output Guide） | 新西兰（多族裔） | 未专项 | 是（青少年/未婚） | **是** | **正式 Data Access Application**；PI 必须挂靠新西兰研究机构（Kaitiakitanga）；签 DAA；经 Secure Data Access Platform；**输出须预审**（≤4 工作日） | `MEASUREMENT_ONLY` |
| D08 | **National Survey of Families and Households (NSFH, W1–W3)** | Wisconsin–Madison CDHA / Temple ISR；ICPSR + CFDA + DISC | 家庭结构+亲子+跨代+同住非婚 | 部分（主 respondent + spouse/partner 短问卷 + focal children + 随机一名家长） | **3**（1987-88 / 1992-94 / 2001-0x） | 是（个体 + 家庭级 id） | 是（Users' Guide、DDI XML、PI codebook + Appendix O 权重） | 是（婚姻/同居/离婚/再婚/监护/抚养/健康/照护责任） | 是（ICPSR/DISC 归档规范、地码版为 restricted） | 美国 | **否**（1987 起设计） | 是 | **是（亲子/跨代/继亲/kin contact）** | ICPSR/Child & Family Data Archive 公版；"Access does not require affiliation with an ICPSR member institution" | `MEASUREMENT_ONLY` |
| D09 | **Changing Lives of Older Couples (CLOC)** / ICPSR 3370 | Univ. of Michigan（House / Wortman / Nesse） | **丧偶照护与哀伤** | **是**（Couples Only 数据集含妻 `V*` + 夫 `S*` 全 4 wave） | **4**（baseline 1987-88 + 配偶死亡后 6 / 18 / 48 月） | 是（Part 5 含 423 couples / 846 人） | 是（6 个子数据集 + 各年 codebook 文件） | 是（哀伤 6 子量表 + DSM-III-R 重性抑郁 + 生理/生化 MacBat 子样本） | 是（NDI + 州死亡记录确认；matched control 设计） | 美国（Detroit SMSA） | 否 | 否 | 是（配偶死亡事件） | ICPSR；原文限定 "freely available to data users at ICPSR member institutions" | `MEASUREMENT_ONLY` |
| D10 | **Health and Retirement Study (HRS)** | Univ. of Michigan ISR / NIA | 老年婚恋 + 照护 | 部分（夫妻同受访；配偶常作 proxy respondent） | **双年**，1992– | 未核实（HRS 正文页本环境不可达） | 是 | **是（ADL/IADL 协助天然给出方向性照护行为）** | 是 | 美国 | 未专项 | 部分 | 是（同住 + 跨代） | 公版免费 + DUA；restricted 需 RDA + IRB + security plan + institutional counter-signature | `MEASUREMENT_ONLY` |
| D11 | **SOEP** (German Socio-Economic Panel) | DIW Berlin | 家庭 | 部分 | 长期年度面板 | **公开标准文件无 partner id** | 是 | 是（如风险态度 0–10 双向个体变量） | 是 | 德国 | **构造后为 0**（"We do not find any same-gender couples"） | 是 | 部分 | 需向 DIW 申请 | `NOT_DYADIC_ENOUGH` |
| D12 | **Add Health (NLSY97/ECLS)** | UNC CPC | 同伴+恋爱+家庭 | 部分 | **6 wave**（Wave I–VI） | 友谊提名网络（**文件名/变量名未核实**） | 是（ACE codebook explorer、Add Health Navigator） | 是 | 是 | 美国 | 变量层存在（文献侧） | 变量层存在 | 是 | 可申请（公版 + restricted） | **`ACCESS_BLOCKED`（use-condition）** |
| D13 | **Understanding America Study (UAS)** | USC CESR | 家庭+健康+退休 | 部分 | 双年核心调查，自 2014 | **未核实** | 是（CF/CPD Data Description） | 是 | 是 | 美国 | — | 部分 | 是 | 注册 + Data User Agreement（免费） | **`ACCESS_BLOCKED`（use-condition）** |
| D14 | **American Family Cohort (AFC)** | Stanford | **多代家庭** | 部分 | 多代纵向 | 未核实 | 是 | 是 | 是 | 美国 | 未核实 | 未核实 | **是（三代替代）** | **classified as PHI**；PHS Data Portal + ABFM 批准 + 第三方 DUA + IRB + 逐项目审批 | `ACCESS_BLOCKED` |
| D15 | **Oregon Youth Study Couples Study, Time 6** | Oregon Youth Study / Three Generational Study | **恋爱伴侣** | 是（受访者+其恋爱伴侣） | **单期（2003–2006）** | 是（couples study 结构） | 是 | 是（社会模式、性行为、物质使用、心理健康） | 是 | 美国（Oregon） | 未专项 | 是 | 否 | **Restricted Data Use Agreement + IRB approval/notice of exemption**；非公开下载 | `ACCESS_BLOCKED` |
| D16 | **NICHD SECCYD (Phase I–IV)** | NICHD / 多点研究网络 | **母婴 / 照护者—儿童** | **否**（主要照护者单方报告，>90% 生母） | **4 phase**（Phase I 1991-94 起 1,364 儿童；Phase IV 1,056） | 是（child/family id） | 是（ADS 1–42 / SDS 43–55 / Raw 56–309 等 309 文件） | 是（照护安排、认知、语言、行为适应、身体健康） | 是（5 个主评估点 + 每 3 月电话；排除标准明列） | 美国 10 地 | 否 | 是（单亲家庭纳入） | **是** | ICPSR 公版；"available for access by the general public" | `MEASUREMENT_ONLY` |

---

## 4. 逐数据集详情卡

### D01 — The German Family Panel (pairfam) · ZA5678

```text
classification: CALIBRATION_READY
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
dyad_identifiability:  STRONG. anchor id `id` + partner id `pid`; 官方 GESIS 变量清单中 partner 侧变量统一 `p` 前缀
   (psex_gen, page, preldur, pmarstat, pincoecd, ...), anchor 侧为 `k*`/`yk*`/无前缀
directionality:        SUPPORTED. 双方各自作答 → Z[k, i, j, t] 与 Z[k, j, i, t] 可分别估计
waves:                 14 (annual). 另有 COVID-19 子研究 (ZA5959)
relationship_type_vars: relstat, marstat, cohabdur, mardur, reldur, meetdur, **homosex /ALKhomosex_new**
kin_coverage:          parents (to wave 8) + children (8-15y) + 继亲 → 非浪漫 dyad 有真实结构
codebook:              14 wave 全部 codebook (英/德) + 问卷 + instrument overview + scales manual +
   annual method reports + concept paper + Data Manual; 学术出版物需给 GESIS 副本
missingness:           method reports; 样本来源由 `cohort` / `demodiff` / `sample` 三变量标记
   (pairfam 主样本 / DemoDiff 样本 / refreshment 样本 / step-up 样本)
access_path:           免费。原文 "The use of this data is free of charge!" 需签署 Nutzungsantrag /
   user contract 发至 GESIS 或 pairfam user service (support@pairfam.de)
   教学另有 FReDA/pairfam Campus Use File（GESIS 免费注册即可），但 "not suitable for scientific publications"
rights_and_limits (CITED_PRIMARY 原文摘要):
   §1 禁止任何去匿名化/再识别行为; 禁止与其他数据合并以再识别受访者
   §3 "Zulässig sind nur zusammenfassende Darstellungen der Daten... Die Darstellung oder Publikation von
        Einzeldatensätzen oder Einzelfällen, auch wenn es keinen direkten Personenbezug gibt, ist nicht erlaubt."
        → **即使无直接标识，也不得发布个体级记录**
   §4 禁止商业用途
   §5 原则上不得向项目/机构外第三方转发; 教学仅可给 50% 教学版
   §7 出版后 4 周内须向 FDZ 提交电子版
   自 2025 年 1 月起，原 "Form for the Internal Distribution" 通道取消，一律走 user contract
   macro-level 汇总数据 "not freely accessible"
can_identify:
   - 双向自报的关系状态分量、其跨 14 年的演化
   - 关系类型/制度状态与关系状态的可分离（relstat/marstat vs 关系状态题）
   - 同性伴侣 dyad（德国样本）
   - 亲子/代际 dyad 的方向性
cannot_identify_without_assumption:
   - **非共居 partner 的独立测量**（partner survey 绑定 anchor 的 current partner）
   - pairfam 侧的关系状态构念清单未在本 lane 核实（见 U15）→ 不得预设它能标定 LHRM 构念
   - 跨文化（仅德国）
lhrm_impact:  最贴近 LHRM 需求形状的公开可得研究面板：双报告 + 长面板 + 同性 + 未婚 + kin 多 actor。
   但 §3 的「仅可汇总呈现」意味着 **不能把 pairfam 个体记录或其直接派生进入 Case Bank**。
```

### D02 — SHARE (Survey of Health, Ageing and Retirement in Europe)

```text
classification: CALIBRATION_READY
canonical_pointer:
  data_access:   https://share-eric.eu/data/data-access
  conditions:    https://share-eric.eu/data/data-access/conditions-of-use   ("Last updated: April 30, 2026")
  releases:      https://share-eric.eu/data/data-documentation
  release_guide: https://share-eric.eu/fileadmin/user_upload/Release_Guides/SHARE_release_guide_9-0-0.pdf
  example_DOI:   10.6103/SHARE.w1.900 ... 10.6103/SHARE.w8.900 (release 9.0.0, 2024-03-28)
dyad_identifiability (CITED_PRIMARY 官方 FAQ 原文):
   "In SHARE, partners can be identified by the mergeidp'w' (where 'w' stands for the respective wave)
    which indicates the mergeid of a respondent's partner. Each couple has a coupleid indicated by the
    variable coupleid'w'. The coupleid is generated using mergeid of both partners and is therefore
    unique to each couple as well as fix across waves if the couple stays the same."
   → 这段是本 lane 找到的**对 LHRM「稳定 couple id」要求最干净的官方定义**。
directionality:  SUPPORTED 但**模块级不对称**。官方明确区分三类回答者角色 `hou_resp` / `fin_resp` / `fam_resp`:
   原文: "the answers to financial, housing and family questions in ... modules FT, AS, HO, HH, CO, CH and
     parts of SP are only available for the financial, family or household respondents"
   → 财务/住房/子女模块的 i→j 观测**只有一方**。不得把这些模块当双报告。
   - fam_resp 的选择规则本身带方向性: "The couple's first person interviewed is the family respondent."
waves:           ≥8 完整常规 wave (2004/05, 2006/07, 2008/09 SHARELIFE, 2010/11, 2012/13, 2014/15, 2016/17,
                 2017/18 Wave 8) + Wave 8 COVID + Wave 9 COVID
                 **第 9/10 wave 官方页面表述冲突 → UNKNOWN_AS_OF（见 §8 矛盾 1）**
kin_coverage:     CH (children) / SP (social support) 模块 + SHARELIFE 回溯；couples 亦含同住 partner
non-married:      是（"current partners living in the same household are interviewed regardless of their age"）
age_limits:       50+ 为主；"Younger partners, new partners and partners who never participated in SHARE
                  will not be traced" → 非同住 / 未受访 partner 不可追踪
codebook:         Release Guide（9.0.0）、cross-wave comparison、methodology volumes、Scales Manual、
                 cv_r / gv_allwaves_cv_r 技术变量模块
access_path:      免费，"Access to the data is provided free of charge for scientific use globally"；
                 个人注册 + 签署 SHARE User Statement；FDZ-SHARE（CentERdata / GESIS）下载
record_linkage:   SHARE-RV (德国养老金)、REGLINK-SHAREDK (丹麦)、REGLINK-SHAREFI (芬兰)、SHARE NL (荷兰 CBS)
                 —— 各自独立申请，**是否含伴侣级 linkage 未核实（U13）**
rights_and_limits (CITED_PRIMARY 原文，2026-04-30 版):
   §2 仅限科学用途
   §6 "Under no circumstance may users take any action aiming at a re-identification of participants"
   §7 保密规则 —— **本 lane 最重要的一条**:
     "when using modern data processing and storage solutions, such as AI tools and cloud services, users must
      ensure that no unauthorised data transfer occurs... Therefore, the use of applications that are not
      fully self-administered is strictly prohibited, unless it can be verified that no data is stored or
      processed by others. Moreover, the data shall not be used for the training of AI models unless such
      training is conducted locally and exclusively for scientific purposes...
      **Any derivative datasets, models, or analytical outputs generated through AI or machine learning
      processes remain subject to the same usage restrictions as the original data.**"
   §11 违反后果: 立即撤销使用权、要求删除全部副本；严重违反可在网上公开违规者身份
   §12 条款可变更，自通知起 21 天生效
   例外: easySHARE 教学简化程序允许教师分发给已注册学生（唯一明文的转供例外）
can_identify:
   - 跨 27+ 国、50+ 人群、双报告的 couple 级跨面板
   - 健康/照护/退休事件如何伴随关系状态演化
cannot_identify_without_assumption:
   - 财务/住房/子女模块的方向性（单方报告，须显式标注 fin_resp/fam_resp）
   - 关系状态构念本身（SHARE 不是关系质量面板；此处内容未核实 → U15）
   - 50 岁以下 partner、非同住 partner、从未受访 partner
lhrm_impact:  唯一具备「跨国 + 双报告 + 长面板 + 官方稳定 couple id 定义」的数据集。
   **但 §7 使 SHARE 派生量在法务上不能进入一个 LLM 参与的公开验证流水线。**
   建议定位为「内部方法学验证来源」而非「验证语料来源」。
```

### D03 — Health and Relationships Project (HARP) · ICPSR 37404

```text
classification: CALIBRATION_READY
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
can_identify:
   - 双配偶分开作答的关系质量 + 健康 + 日常压力 + 社交互动 + 健康行为
   - 稀疏面板内嵌密集日记 → 可观察 day-level 状态波动（对 LHRM 的 `t` 粒度极有价值）
   - 同性 vs 异性婚内关系状态（须带 §sampling_inequality 的选择警告）
cannot_identify_without_assumption:
   - 离婚/分居/丧偶后的**新关系**（T2/T3 只续访原配偶身份）
   - 非婚 / 未婚 / 未同居关系（入组硬门槛）
   - 跨文化（单州）
lhrm_impact:  形状上最贴近 LHRM「方向化 + 纵向 + 部分信息 + 密集观测」的候选；
   但「合法已婚 + 同居≥3 年」的入组条件使其**无法覆盖 LHRM 研究域中的陌生起点、非婚、第三方**。
   （`AGENTS.md` §当前架构方向第 2 条明确不预设异性、陌生起点、婚恋目标 → HARP 只能作为**局部**校准源。）
```

### D04 — Fisman & Iyengar Speed Dating Experiment (2002–2004)

```text
classification: MEASUREMENT_ONLY
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
can_identify:
   - 方向性不对称在**最短交互时间尺度**上的经验分布
   - mutuality / reciprocity 作为**派生量**的真实可观测性（match = dec_i AND dec_j）
   - 感知属性与自身属性的不对称（对方吸引 i ↔ i 自我知觉）
cannot_identify:
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
classification: MEASUREMENT_ONLY
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
can_identify:
   - 跨约 90 国的双人自报配对测量；决策权/避孕/暴力等**天然方向性**的题项
   - 跨人感知误差（配偶年龄互评）
cannot_identify:
   - 任何时间演化
   - 非 co-resident 伴侣
   - 同性配对（制度性缺失）
lhrm_impact:  **REPRESENTATION 覆盖面工具，而非校准工具**。
   它能证明 LHRM 的方向性坐标在任何一种人类学文化里都有真实对应物（不只西方恋爱样本），
   但不能提供任何动态信息。
```

### D06 — Indonesia Family Life Survey (IFLS1–IFLS5)

```text
classification: MEASUREMENT_ONLY
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
can_identify:
   - 5 波跨 21 年的家庭结构、婚育、迁移、健康、经济、亲属转移（含非同住）
   - 印尼语境下的家庭 dyad 与照护流动
cannot_identify_without_assumption:
   - 任何 i→j vs j→i 的关系状态分解（除非接受 spouse 重建假设）
   - 同性 dyad（未专项，且家庭问卷以户主-配偶为轴）
lhrm_impact:  提供「非西方、非个人主义语境下关系状态如何被登记」的对照；
   但因方向性需假设，不应被当作方向性证据。
```

### D07 — Growing Up in New Zealand (GUiNZ)

```text
classification: MEASUREMENT_ONLY
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
can_identify:
   - 多族裔（Māori / Pacific / 移民社群）语境下的亲子与青少年家庭 dyad 纵向
   - 青少年非婚关系、同住伴侣的形成
   - 家庭层面的事件（极端天气等）对关系/照护的冲击
cannot_identify:
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
classification: MEASUREMENT_ONLY
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
directionality_critical_note:
   **配偶关系质量是单方报告**。主受访者被问 "Respondents were also asked about the relationship of
   household members to each other and the quality of their relationships with their parents, children,
   and in-laws."
   → 配偶**之间**的关系状态由一个人报告。→ **Z[i→j] 与 Z[j→i] 在 NSFH 中不可分离。**
   但 **亲子/跨代方向是真实可测的**（子女 + 随机一名家长 + 关系质量题）→ 这是 NSFH 的真正方向性资产。
codebook:  PI Codebook（+ Appendix O: NSFH2 Final Weights and Weighting Procedure）、DDI XML、
   ASCII/R/SPSS/SAS/Stata + PDF 文档
access:  "The public-use data files in this collection are available for access by the general public.
   Access does not require affiliation with an ICPSR member institution."
   三波地码版为 **restricted-use**（ICPSR 严程序）
cross_cultural:  仅美国
same_sex:  **否**（1987 起采集，同性婚姻不存在）
can_identify:
   - 亲子 dyad 的方向性（家长→子、子→家长；跨代关系质量；非同住父/母联系）
   - 3 波的关系/同居/离婚/再婚/继亲/监护事件史
   - 同居（非婚）家庭
cannot_identify:
   - 配偶间关系状态的方向性（单方报告）
   - 同性关系
lhrm_impact:  **NSFH 印证 `AGENTS.md` 的一个架构判断**：
   即使是最著名的家庭纵向调查，「关系质量」也是单方报告的。
   这说明 LHRM 的 `Z[k,i,j,t]` 双报告要求在**大规模代表性调查**里基本无法满足，
   只能在**专门为双人设计的研究**（pairfam / SHARE / HARP）里满足。
   → 对参数收敛的含义：**LHRM 的方向性 primitive 只能在窄样本上标定，不能在宽样本上验证。**
   （此为 observation，非建议。）
```

### D09 — Changing Lives of Older Couples (CLOC) · ICPSR 3370

```text
classification: MEASUREMENT_ONLY
canonical_pointer:  https://www.icpsr.umich.edu/web/ICPSR/studies/3370
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
can_identify:
   - 丧失事件前后、双人同 record 的多波状态演化（照护 → 丧失 → 哀伤轨迹）
   - 双人方向性在同一 record 内可直接估计（V 变量 vs S 变量）
cannot_identify:
   - 新配对关系（不观测重组）
   - 一般婚姻过程（被丧偶条件化）
   - 跨文化（Detroit SMSA）
lhrm_impact:  提供 **caregiving / illness / bereavement** 这条 LHRM 明确需要的轴，
   且提供「关系终点」的可观测事件。可作为极端案例的 stress test 参照
   （`AGENTS.md`："Extreme real-world cases are stress tests for representation and dynamics"），
   但不能作为一般转移律的标定源。
```

### D10 — Health and Retirement Study (HRS)

```text
classification: MEASUREMENT_ONLY
canonical_pointer:
  home:          https://hrs.isr.umich.edu/
  data_products: https://hrs.isr.umich.edu/data-products
  file_merge:    https://hrs.isr.umich.edu/data-products/file-merge-reference
  rda_pdf:       https://hrs.isr.umich.edu/sites/default/files/rda-forms/HRS-RDA-MiCDA-Access-Agreement.pdf
  faqs:          https://hrs.isr.umich.edu/data-products/restricted-data/faqs
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
     （传统许可）或经 MiCDA Secure Data Enclave（VDI）
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
unknown:
   - **HRS CoU（更新于 2026-02-04）关于 AI/LLM 的具体条文未取得**（页面 banner 原文已核实：
     "All data files are subject to the Conditions of Use for HRS data, updated 02/04/2026. Please review
     the updated conditions, which include a new policy on use of AI and Large Language Models."）。
     → `UNKNOWN_AS_OF`（U4）。**不得猜测条文内容。**
   - HRS 是否发货跨波稳定的 partner/couple id → `UNKNOWN`（U5）
can_identify:
   - 方向性照护行为（照护方 → 被照护方）、跨双年面板
   - 双成员互相代理作答这一「信息源即关系成员」结构
cannot_identify_without_assumption:
   - 跨波 partner id 绑定（未核实）
   - 关系状态自报（SHARE/HRS 都不是关系质量面板）
lhrm_impact:  **rights 层面比统计层面更重要**。
   HRS 的 NIH Certificate of Confidentiality 是本 lane 找到的**对 Case Bank 路线最硬的单点约束**：
   它意味着即便法院命令，HRS restricted 也不能作为 Case Bank 材料披露。
   建议 Architect 把这一条写进 Case Bank 的选材规则。
```

### D11 — SOEP (German Socio-Economic Panel)

```text
classification: NOT_DYADIC_ENOUGH
canonical_pointer:
  archive: DIW Berlin
  negative_evidence_source: BACON, P., CONTE, A.M. & MOFFATT, P.G. (2014) "Assortative mating on risk
    attitude", J Behav Dec Making (https://link.springer.com/content/pdf/10.1007/s11238-014-9448-x.pdf)
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
can_identify:  个体层面跨年变量（如 0–10 风险态度）确实双报告
cannot_identify:  **发货形态下不存在可用的 i↔j 绑定** → `Z[k,i,j,t]` 需先付重建成本
lhrm_impact:  作为**方法学反面教材**纳入，而非作为数据源纳入。
   建议在后续方法学文档中引用本条作为「dyad 构造必须自报规则与损失」的模板。
```

### D12 — Add Health (NLSY97 / ECLS)

```text
classification: ACCESS_BLOCKED（**use-condition block**，非 possession block）
canonical_pointer:
  conditions:  https://addhealth.cpc.unc.edu/conditions-of-use/   （本 lane 全文抓取）
  docs:        https://addhealth.cpc.unc.edu/documentation/
  data_docs:   https://addhealth.cpc.unc.edu/documentation/data-documentation/
waves:  Wave I–VI（Wave I 1994-95）
dyad_potential:  **唯一可能提供方向性友谊提名网络的大型美国纵向数据集**
   （Wave I / Wave III in-school nomination）。→ **但本 lane 未核实其文件存在性（U7）。
      不得主张该数据存在。** 变量层存在性仅为 AGENT_RECALL，不作事实主张。
critical_rights_finding (CITED_PRIMARY 原文，本 lane 全文抓取):
   "All users of Add Health restricted-use data agree to the following conditions:
     - The data files will be used solely for statistical analyses.
     - No attempt will be made to identify specific individuals, families, households, schools,
       institutions, or geographic locations...
     - **No list of sensitive data at the individual or family level will be published or otherwise
       distributed.**"
   + 结果呈现门槛: "In no case should a cell frequency of a cross-tabulation be fewer than ten (10) cases."
   + "All journal articles ... will receive a PubMed Central reference number (PMCID)."
   + "Data Files released should never permit disclosure when used in combination with other known data."
   **AI and LLM Use Policy:**
   "Large language models (LLMs) and other AI tools (e.g., ChatGPT, Claude AI, Microsoft Copilot,
    Google Gemini) **may not be used to manage, process, or analyze data distributed by Add Health.
    This policy applies to both public-use and restricted-use data.**"
   "Under Add Health Data Use Agreements, researchers are forbidden to distribute data or other materials
    we supply (apart from codebooks and metadata) to other members, organizations, or individuals.
    **This means that use of LLMs or other AI is a violation of all existing data use agreements.**"
   LLM 三分法表（官方原文）: **Type 1 → None; Type 2 → None; Type 3 → None**
   理由（官方原文）: Type 1 "ingest and make use of the data. This counts as redistributing the data to the
   company operating the LLM"; Type 2 "they are not isolated from broader networks or the Internet and
   heighten external data merge risks, so they would not comply with data security plans"; Type 3
   "LLMs are not available within the UNC SRW, so this is not an option for Restricted-Use data. At present,
   we are also not accepting requests for this kind of data use for Home Institution Hosting Agreements."
   唯一许可: "It is permissible to use LLMs and AI tools with our public-facing documentation, codebooks,
   and study-level metadata, including group or population estimates. However, use of individual-level
   data is not permissible."
   taxonomy 溯源（官方自述）: "Thanks to the University of Michigan's Health and Retirement Study and ICPSR
   as well as Sebastian Karcher at Syracuse University for originating this taxonomy of LLMs and/or policy."
can_identify:  （若 friendship nomination 文件存在）方向性友谊 dyad
cannot_identify:  对 LHRM 计划用途 —— **不可识别**。个体级数据在三种 LLM 类型下均不允许，
   且公版与 restricted 同等适用。
lhrm_impact:  **这是本 lane 最重要的 use-condition 反例**：
   一个在学术上完全合格、在获取上完全可行的顶级青少年纵向数据集，
   因为 **AI 政策**（而非因为拿不到、也并非因为 IRB 强度）而对本项目不可用。
   建议 Architect 把它作为「rights-first 筛选」的示例。
   同时其 codebooks / metadata / 群体估计仍可用于 LHRM 的 measurement 文档工作。
```

### D13 — Understanding America Study (UAS)

```text
classification: ACCESS_BLOCKED（use-condition block）
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
can_identify:  个体-波次面板（若存在 partner 变量则可谈 dyad）
cannot_identify:  对 LHRM 计划用途 —— **不可识别**（AI 政策）。
   且若走 Enclave，仅限美国研究者。
lhrm_impact:  与 Add Health 同类：可用作**测量/文档参考**，不可用作数据源。
```

### D14 — American Family Cohort (AFC)

```text
classification: ACCESS_BLOCKED
canonical_pointer:  https://americanfamilycohort.org/how-to-access-afc-data/
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

```text
classification: ACCESS_BLOCKED
canonical_pointer:  https://www.icpsr.umich.edu/web/NAHDAP/studies/38726
scope (CITED_PRIMARY 原文):
   "This study is part of the Oregon Youth Study, which began in 1983 and has now become the Three
    Generational Study (3GS)... The longitudinal study expanded and now includes this study, the Oregon
    Youth Study Couples Study. This study explores behaviors among the respondents **and their romantic
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
dyad:  受访者 + 其恋爱伴侣 → **双方报告**（这是本 lane 中除 HARP 外唯一明确「双报告恋爱 dyad」
   的美国数据集）
waves:  **单期（Time 6）** → 不构成多波双人面板
can_identify:  恋爱 dyad 的行为与健康（一次性）
cannot_identify:  时间演化；获取（LHRM 无 ICPSR RDUA + IRB 的现实路径）
lhrm_impact:  作为 **「存在但不可及」 的登记项** 记录。
   它的存在证明「双报告恋爱 dyad 数据确实被采集过」，但对 LHRM 无操作价值。
```

### D16 — NICHD SECCYD (Phase I–IV)

```text
classification: MEASUREMENT_ONLY
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
can_identify:  kin dyad 的纵向（照护安排、发展结果、照护决策）
cannot_identify:  双向自报；恋爱关系；成人伴侣
lhrm_impact:  覆盖 LHRM 研究域中的 **kin / 照护 dyad**（`AGENTS.md` 明确「允许亲属、朋友、同事、前任…
   等现实存在的关系结构进入描述」）。但因单方报告，只能标定 parent→child 单方向。
   价值主要是「证明 kin dyad 在数据世界里存在且可获取」。
```

---

## 5. 权利 / 同意 / 再分发限制专章（对本项目影响最大的一章）

### 5.1 汇总表

| 数据集 | 能否公开发布**个体级记录** | 能否发布**派生量**（尺度/参数/嵌入） | LLM/AI 处理个体级数据 | 关键法律工具 |
|---|---|---|---|---|
| **SHARE** | **否**（CoU §6/§7） | **受限**：§7 明文 "Any derivative datasets, models, or analytical outputs generated through AI or machine learning processes remain subject to the same usage restrictions as the original data" | 禁止「非完全自管」的应用；禁止用于 AI 训练（除非本地且纯科学） | 个人注册 + SHARE User Statement；GDPR；German Federal Statistics Act 下 "factual anonymity" |
| **pairfam (ZA5678)** | **否**，且明文「即使无直接标识也不得发布个体记录」 | **否**（§3 只允许汇总呈现） | 未见专门条文 → 保守按 §3/§5 处理 | 签署的 user contract；§2 目的限定；§5 禁止向第三方转发 |
| **HARP / ICPSR** | 须 ICPSR 书面许可（Redistribution Policy） | 同上 | **ICPSR LLM 政策**：Type 1 = None；Type 2 = Public-Use（须许可）；Type 3 = Public + Restricted（须许可） | ICPSR Bylaws 1.2.B；Redistribution Policy；LLM Policy |
| **Add Health** | **否**（"No list of sensitive data at the individual or family level will be published or otherwise distributed"） | 未明示，但受同一 DUA 约束 | **全部禁止**（Type 1/2/3 均为 None；公版与 restricted 同等） | Add Health DUA；LLM/AI Use Policy；Type 3 目前不接受申请 |
| **UAS (CESR)** | 须 DUA 限定 | 同上 | **全部禁止**（明文 "violation of all existing Data Use Agreements"） | UAS Data User Agreement；Enclave 限美国研究者 |
| **HRS** | Enclave 用户**永远不得导出** respondent-level；仅统计汇总 | 同上 | **CoU 2026-02-04 含新 AI/LLM 政策**（条文未取得 → U4） | **NIH Certificate of Confidentiality（即使法院命令/传票也不得披露）**；RDA；DCP |
| **IFLS** | 匿名码外不得识别 | 未明示，但 "Please do not distribute these data" | 未见专门条文 → 保守处理 | 保密声明（confidentiality declaration）；RAND 注册 |
| **DHS** | 须授权后使用；要求尊重受访者匿名 | 未明示 | 未见专门条文 | 授权制；Data Suppression 规则（括号值） |
| **GUiNZ** | **须输出预审通过**方可发布 | 同上 | 未见专门条文 | Data Access Protocol 2026 v1.0；DAA；**Kaitiakitanga（新西兰数据主权）**；Stats NZ 5 Safes |
| **NSFH / SECCYD** | ICPSR 公版，但结果须遵守 cell ≥10 与地理抑制规则 | 同上 | 适用 ICPSR LLM 政策 | ICPSR Terms of Use |
| **CLOC** | ICPSR 公版，**限 member institution** | 同上 | 适用 ICPSR LLM 政策 | ICPSR Terms of Use |
| **speed dating** | **是**（公开镜像） | **是** | 无明文限制 | 公开仓库；原始研究机构的数据政策未在本 lane 核实 → 保守按「引用而非再分发」处理 |

### 5.2 对 LHRM Case Bank 与 validation corpus 的三条可执行结论

> 以下为 **AI recommendation（架构建议）**，不是 Human requirement，也不构成已确立结论。

1. **`VALIDATION_CORPUS_V0_1.md` 现有的 `access_status` / `copyright-license` 字段不足以表达 use-condition 限制。**
   现有 12 个材料全部是公开叙事来源（gov.uk、StoryCorps、Gutenberg、National Archives、SEP、MIT Classics、PMC），不受上述任何 use-condition 管辖。但一旦引入问卷型个体级数据，**「能否获得」与「能否用于 LLM 参与的验证流水线」是两个独立且可能互相矛盾的位**。
   建议为 Case Bank 材料增加一个显式字段，例如 `llm_use_condition: PERMITTED | RESTRICTED_LOCAL_ONLY | PROHIBITED`，并把 `icpsr_llm_type: 1|2|3` 之类的可执行约束写进选材规则。

2. **HRS 的 NIH Certificate of Confidentiality 与 Case Bank 的「官方法院文书」路线互斥。**
   该证书禁止在任何民事/刑事/行政/立法程序中披露可识别的敏感参与者信息，**即使法院命令或传票**。
   `VALIDATION_CORPUS_V0_1.md` §10 建议把「法院/官方材料」作为 Case Bank 第一优先来源。
   → 结论：**Case Bank 的材料选择不能同时依赖「行政/司法渠道获取」与「个体级问卷数据」**。这两条路在制度上分岔。

3. **「公开叙事语料」与「问卷型个体级数据」在 rights 上是两个不重叠的世界。**
   前者（gov.uk 判决、National Archives、StoryCorps、Gutenberg、SEP、MIT Classics）目前不受任何 LLM 政策约束；后者（Add Health / UAS / ICPSR / SHARE / pairfam）已被 2025–2026 的新政策实质或明文覆盖。
   → 这为 LHRM 提供了一个结构性回旋空间：**把 Case Bank 保持在公开叙事语料侧，把问卷数据限制在方法学标定侧（且仅在本地合规环境内）。**

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
| **关系类 App / 手机日记研究** | 个体/日记级 | 密集纵向 + belief 捕捉 | — | **本 landscape 中未发现任何公开 release**（U14） |
| **ICPSR SOMAR VDE / MiCDA Enclave** | 计算环境 | 在隔离环境内跑 LLM 处理受限数据 | 需 RDUA + IRB；ICPSR 可在 VDE 内放自托管模型（Llama-3.2-3B-Instruct、gemma-3-4b-it 等） | 已核实（SOMAR 页原文）——**这是目前唯一已知可行的「合规地用 LLM 处理受限数据」路径** |

---

## 7. 明确非主张（explicit non-claims）

1. **不主张**本报告涉及的任何数据集已被 LHRM 下载、打开、分析或映射。本 lane **零数据接触**。
2. **不主张** pairfam / SHARE / HARP 能标定 LHRM 的具体关系状态构念。其**结构**已核实，**构念内容**未核实（U15）。「结构合适」≠「参数可标定」。
3. **不主张**任何数据集具有代表性或可外推性。各样本的硬门槛（合法已婚+同居 3 年 / 50+ / 异性单性 / 0–3 岁 / 配偶已故 / co-resident）已逐条列出。
4. **不主张** speed dating 的 `dec`/`match` 等于 attraction / trust / dedication。它是单一决策变量。
5. **不主张** HRS CoU（2026-02-04）AI/LLM 政策的具体内容。只核实其存在（U4）。
6. **不主张** Add Health 存在 friendship nomination 数据文件（U7）。
7. **不主张** IFLS 存在现成跨波 partner id（U8）。
8. **不主张** Family Life Survey / LSAF / New Study of Marriage 的任何属性（U1–U3，本 lane 无法访问）。
9. **不主张**本 landscape 覆盖了所有重要数据集。已知缺口见 §9 与 U1–U15。
10. **不主张** §5.2 的三条结论是 Human requirement。它们是 **AI recommendation**，需 Human / Architect 判定。
11. **不主张**任何 LLM 政策将来不会变。SHARE CoU §12 明文可变更（21 天生效）；Add Health 注明 taxonomy 源自 HRS + ICPSR + Karcher，即政策在生态内联动演进。**日期戳必须随引用保留。**
12. **不主张**本 lane 规避、绕过或尝试规避任何 access control。所有 blocked 项按 blocked 记录。
13. **不主张**本 lane 的任何权利解读构成法律意见。本 lane 只做文本层面的事实记录。

---

## 8. 矛盾与否定结果

1. **SHARE wave 数：官方站点内部不一致。** `Data Releases` 表（release 9.0.0, 2024-03-28）列 Wave 1–8 主发布 + Wave 8 COVID + **Wave 9 COVID-19 Survey**；同站导航在 `Questionnaires` 下有 `Wave 9` 页；国家伙伴站 SHARE-CZ FAQ 写 "Wave 9 and SHARE Covid (2021–2023)" 及 "**Wave 10 (2023–2024)**"。
   → 本报告采用保守表述：**已核实完整常规 wave ≥ 8（2004–）；第 9/10 wave 状态在官方站点间冲突，标 `UNKNOWN_AS_OF`。** 这是官方文档矛盾，非本 lane 读取错误。

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

7. **Add Health Data Documentation 的数据文件表为 JS 渲染，未取得行级清单。** → friendship nomination 文件名/变量名 `UNVERIFIED_AS_OF`。

8. **「intensive longitudinal 关系日记数据」在本 landscape 中不存在公开可得的。** 16 个审计对象中唯一密集设计是 HARP 的 8–10 天日记（嵌套于稀疏面板，且 T3 天数由 10 降至 8，**密集窗长度本身随时间变化，wave 不完全可比**）。

9. **最重要的整体否定结果**：本审计**未发现**任何「完全公开 + 双报告 + 方向性 + 多波 + 关系状态构念」的数据集。**这四个条件的交集为空。** 这是本 landscape 最重要的结构性事实，比任何单个数据集的优劣都重要。

10. **反向（有利）否定结果**：本审计**未发现**任何问卷型数据集会与 `VALIDATION_CORPUS_V0_1.md` 现有 12 个公开叙事材料的权利条款发生冲突。→ 现有 Case Bank 路线在权利上是干净的。

---

## 9. 剩余未知

| # | 未知项 | 状态 |
|---|---|---|
| U1 | Family Life Survey（Larimer）当前 wave / couple id / codebook / access 条款 | `FETCH_FAILED`（4 次尝试） |
| U2 | LSAF 是否仍采集 / 当前申请路径 | `FETCH_FAILED` |
| U3 | New Study of Marriage 当前 wave 数与获取路径 | `FETCH_FAILED` |
| U4 | HRS CoU（2026-02-04）AI/LLM 政策**具体条文** | 存在性已核实，正文 `UNKNOWN_AS_OF` |
| U5 | HRS 是否发货跨波稳定 partner/couple id | `UNKNOWN` |
| U6 | HARP T2/T3 微数据是否已 release | 页面矛盾，`UNKNOWN_AS_OF` |
| U7 | Add Health friendship nomination 文件名/变量名 | `UNVERIFIED_AS_OF` |
| U8 | IFLS 是否有现成跨波 partner id 变量 | `UNKNOWN` |
| U9 | pairfam 非共居 partner 的测量覆盖 | `UNKNOWN` |
| U10 | SOEP / PSID / NLSY79-97 / Understanding Society 扩展文件是否发货 partner id | `UNKNOWN`；标准文件无（S47 佐证 SOEP） |
| U11 | ML-SAAF（Midwest Longitudinal Study of Asian American Families，含跨种族伴侣）access 状态与 wave 数 | `UNKNOWN_AS_OF` |
| U12 | SNAP（Timmermann, Nowak & Krabill 2015）纵向友谊网络数据可申请性 | **本 lane 未核实，不作主张** |
| U13 | 北欧/荷兰行政登记联动是否含伴侣级 linkage | `UNKNOWN`（SHARE 侧 linkage 项目存在性已核实） |
| U14 | 关系类 App / 日常日记研究是否有任何公开 de-identified release | `UNKNOWN_AS_OF` |
| U15 | **pairfam / SHARE / HARP 问卷中实际含哪些「关系状态」构念**（而非家庭经济/健康/人口变量） | **未核实**。这一项直接决定它们能否标定 LHRM 构念，是后续 lane 最应优先补齐的缺口 |

---

## 10. 建议状态

**`status_recommendation: PARTIAL`**

理由：

- **达成的**：16 个数据集审计（目标 12），远超数量要求；每个都有 2026-09-27 的核实日期、稳定指针、7 项属性逐条判定、四类分类、「能/不能识别」说明、以及独立的非数值结构化来源清单。
- **最有价值的产出（超出原任务书预期）**：发现了 **2025–2026 年 LLM/AI use-condition 收紧** 这一横跨 SHARE / ICPSR / Add Health / UAS / HRS 的系统性约束（§5、§5.2），并给出唯一已知可行的合规路径（ICPSR SOMAR VDE / MiCDA Enclave 内的自托管模型）。
- **未达成的（故非 SUCCESS）**：
  1. **U15 未解** —— 三个 `CALIBRATION_READY` 数据集的**构念内容**（而非结构）未核实。这使 `CALIBRATION_READY` 判定严格来说只成立于「结构层」，须由 R03（measurement instruments）或后续 lane 补齐。
  2. **U1–U3 覆盖缺口** —— 三个文献常用核心 panel 无法访问，构成实质盲区。
  3. **U4** —— HRS AI/LLM 政策条文未取得，而这可能是最严的一份。

**建议的后续动作（AI recommendation，非 Human requirement）**：

| 优先级 | 动作 | 目标 lane |
|---|---|---|
| P0 | 取得 pairfam 14 wave 的 codebook / scales manual 中**关系状态类题项**清单，以及 SHARE / HARP 同类清单（解 U15） | R03 或本 lane 二轮 |
| P0 | 取得 HRS CoU（2026-02-04）AI/LLM 政策全文（解 U4） | 本 lane 二轮 / R00 |
| P1 | 换网络环境重试 `familylifesurvey.org` / `lsaf.org` / `nsmshow.org` / `nichd.nih.gov`（解 U1–U3） | 本 lane 二轮 |
| P1 | 向 Architect 提交「Case Bank 材料增加 `llm_use_condition` 字段」的建议 | R15 / Architect |
| P2 | 调研 ICPSR SOMAR VDE / MiCDA Enclave 内自托管模型的实际可行性（是否满足 LHRM 的验证需求） | R13 / R16 |
| P2 | 核实 U10（PSID / NLSY / Understanding Society 扩展文件的 partner id），以判断是否存在低成本 dyad 重建路径 | R05 / R07 |

---

## 11. 引用清单（stable pointers，核实日期均为 2026-09-27）

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
    J Behav Dec Making. https://link.springer.com/content/pdf/10.1007/s11238-014-9448-x.pdf
  Seltzer, J.A., Bachrach, C.A., Bianchi, S.M., Bledsoe, C., Casper, L.L., Chase-Lansdale, P.L. et al. (2005).
    "Explaining Family Change and Variation: Challenges for Family Demographers." JMF 67(4):908-925.

抓取失败（FETCH_FAILED，2026-09-27）
  https://www.familylifesurvey.org/      (TLS 握手失败 x4)
  https://www.lsaf.org/                  (连接失败)
  https://nsmshow.org/                   (连接失败)
  https://www.nichd.nih.gov/research/supported/seccyd  (URL rejected)
  hrs.isr.umich.edu 正文页 (timeout / 403)
```
