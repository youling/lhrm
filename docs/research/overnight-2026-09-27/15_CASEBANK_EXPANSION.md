# 15 — Case Bank 扩展策略（Wave 1 / R15）

**Status:** Research candidate — 待 Architect review，**未冻结**，**未修改任何 canonical 文档**  
**As of:** 2026-09-27  
**Parent lane:** `youling/lhrm#30` Wave 1；长期 benchmark lane `#13`  
**Nature:** 采样框与 fixture 设计提案。**不含** 任何 LHRM mapping 结果，**不含** ontology/construct 变更建议。

## 15.0 定位声明：本报告的四类资产分离

`#13` comment 5 已要求把 `CaseBank narrative source` / `population-calibration dataset` / `measurement-representation benchmark` / `tooling-index` 分开。本报告把它作为第一原则：

| 资产类 | 定义 | 能回答 | 不能回答 | 本报告成员 |
|---|---|---|---|---|
| `CASE_BANK_NARRATIVE` | 冻结、权利已清理、时间索引、原子化的**人类可读**单一真实 dyad 记录 | representation completeness / closure / regression / adversarial | 任何 base rate、发生概率、参数权重 | N01–N19（22 条） |
| `CALIBRATION_DATASET` | 总体/面板统计数据 | prior、base rate、分布形状、measurement invariance | 单 dyad 状态值 | N24、N25、N26 |
| `MEASUREMENT_BENCHMARK` | 固定标签 + 固定指标的比较任务 | 仪器/标注/模型之间的一致性与回归 | 关系的经验事实 | §15.5 的 LHRM per-unit mapping harness（+ 外部 NLP 基准仅作 tooling sanity check，`UNVERIFIED_CANDIDATE`） |
| `TOOLING_INDEX` | 指针、镜像、检索界面、抓取器、rights gate、claim store | provenance 与可达性 | **事实权威** | N27、N28、N29、N30 |

**规则**：经 `TOOLING_INDEX` 取得的判决，事实权威必须回溯法院/机构自有稳定 ID（承接 `#13` comment 5）。LHRM 现有 Eye→Juece rights 链已属此类。

## 15.1 当前基线与两个隐性缺口

三份已冻结 fixture（`FIXTURE_001` Carty / `FIXTURE_002` Magi / `FIXTURE_003` StoryCorps）各自内部自洽，但**放在一起不可比**：

- 三套互不兼容的 `fact_status` 词表（法律轴 / 叙述轴 / 混合轴），且 Magi 无 `unknown`、StoryCorps 有 `other` 兜底；
- Fixture 001 连 `unit_type` 都没有；
- verdict 词表两份缺 `DIRECT` / `NARRATIVE_ONLY` / `IRRELEVANT`。

**Fixture 003 的可运行状态（X-7，Round-3 补记）**：`FIXTURE_001` 与 `FIXTURE_002` **可以运行**；`FIXTURE_003` **需要 Human 的权利裁决**才能计入"可运行的已冻结 fixture"。理由：其 `rights_policy = HUMAN_REVIEW_REQUIRED`、Eye 侧 `POINTER_HASH_ONLY` fail-closed、来源站 `robots.txt` 含 `ai-train=no` + `Disallow` for GPTBot/ClaudeBot/CCBot，且**canonical 页面地址在 2026-09-14 实测出现 404**（旧 `-perasa/` 路径；冻结包头部记录了据此所做的指针更正）。**该裁决与 fixture 记录是否需要重新定位，均属 Architect / Human 决定，本报告不裁定，也不自行重新定位。** §15.5 / §15.6 中一切以 F003 为载体的设计（尤其 §15.7 **A06**）在此裁决前**不得视为可执行**。

### 15.1.1 Fixture 001 的**被检验对象**（X-9 裁决，Round-3 补记）

**Fixture 001 是「事实 / 观察 / 信念 / 行为 / 历史 / provenance 的表示与映射失败语义」之测试。它不是"8 项 relationship-state 构念都必要"的有效测试。**

- 其 core dyad 是 `Miss Z. Carty ↔ her 2020 line manager`（**雇主↔雇员**），26 个原子事实是**机构性事实**：排班、停业、未付薪、CAB（咨询调解委员会）、申诉。
- 依据该件声称"8 维 basis（Liking / RomanticAttraction / SexualDesire / Trust / AttachmentSecurity / Caregiving / Dedication / OutcomeDependence）均必要"是**类目错误**：材料里没有可用于区分这 8 个有向关系状态坐标的关系内容；任何结果都落入 §15.1 已记录的退化（`PairState` 层事实齐备而 `DirectedRelationshipState` 层无实例），或落入"该件本就无此类内容"的平凡结论。
- **因此**：本报告的 §15.5 覆盖矩阵、§15.6.3 harness、§15.7 A01–A14 **全部只主张 representation 维度的判别性**，**不得**被读作构念最小性（minimality / ablation）的证据。
- **构念最小性需要一个独立的、承载构念的基准集（construct-bearing benchmark）**：其单元必须**以关系状态构念为目标**地采样，而不是以法律事实 / 叙事为载体。该基准集的规划**正在由另一个 child 进行，本报告只指出依赖，不在此建造**。在本报告新增的任何 fixture（N01–N30）**同样不构成构念承载材料**——它们全部是公开记录或公有领域叙事，取样理由是关系**情境**覆盖，不是构念**承载**。

**更重要的两个流程缺口**：

1. **`#13` comment 2（status CURRENT）强制 `INPUT PACKAGE` / `HOLDOUT PACKAGE` 分离，三份 fixture 均无 `t0` 锚点、无 `holdout` 标记。** 仅靠每行 `future_leakage_note` 不足以满足该要求。
2. **`#13` comment 3 的九类 failure taxonomy 与 `NARRATIVE_ONLY` 在 fixture 层从未被引用**；没有任何 fixture 声明自己含多少个预期 `NARRATIVE_ONLY` 单位，导致该 verdict 率无法比较。

## 15.2 下一批 22 条高价值 CaseBank narrative 指针

> 核实状态：`VERIFIED_2026-09-27` = 本轮实际 HTTP 200 / 完整页读取；`VERIFIED_VIA_SEARCH` = 本轮经 websearch 取得官方页面文字；`UNVERIFIED_CANDIDATE` = 本环境出口不可达，**不得当作已核实**。  
> 实质内容：`CITED_PRIMARY_CONTENT` = 判别性理由来自我本轮实读原文/原始摘要；`SUBSTANCE_NOT_READ` = 判别性理由是**待原文确认的预映射假设**。

### P0 — Official adjudicated / primary institutional（英国，Find Case Law）
统一权利：Crown copyright / Open Justice Licence，免费阅读与复用（署名）；LHRM 只存 paraphrase + pointer。

| id | 案号 / pointer | 核实 | dyad / 时间 | 判别性（会抓到的表示失败） | 覆盖 cell |
|---|---|---|---|---|---|
| N01 | `N v ACCG` [2017] UKSC 22 — `caselaw.nationalarchives.gov.uk/uksc/2017/22`；官方 press summary `supremecourt.uk/uploads/uksc_2015_0238_press_summary_04af2a375a.pdf` | VERIFIED_2026-09-27 · `CITED_PRIMARY_CONTENT` | 无能力成年人 ↔ 父母（kin+照护）+ 机构（CCG/NHS、care home、Official Solicitor、Court of Protection）；care order 于 18 岁法定终止 | press summary 原文：Court of Protection 权限**仅等于 P 本人若有行为能力时能作的选项**（[24][26][29]），**不能命令第三方提供资金或服务**（[29][35]）；capacity 相对于具体决定（[26]）。→ (a)"照护"不是天然双向 dyad，边可被机构中介、部分不存在或被指令；(b)"机构无权"是**约束**不是状态；(c) 18 岁这一**无 dyad 内事件**改写照护结构 | kin / caregiving / institutional / non-romantic / longitudinal / adversarial |
| N02 | `H v H (Financial Relief)` [2022] UKPC 3 — `/ukpc/2022/3` | VERIFIED_2026-09-27 · `SUBSTANCE_NOT_READ` | 香港，分开后多年申请财产救济；t0 天然存在 | **第一优先**。`pair_status` ≠ `institutional_status`；"法律未认定"须表达为**未裁决区间**而非中性填零；"分居但不离婚" ≠ 关系终止 | cross-jurisdiction / ordinary 边界 / migration（待确认） |
| N03 | `Bigos v Hameed` [2015] UKSC 17 — `/uksc/2015/17` | VERIFIED_2026-09-27 · `SUBSTANCE_NOT_READ` | 成年女儿 ↔ 父亲；跨宗教/族群家庭 | 家庭信念 vs 单方叙事；"能力/同意"型构念在无事件下翻转；家族作为第三方决定 dyad。**须读原文确认事实段与 fact_status 分布** | kin / cross-cultural / deception / adversarial |
| N04 | `NG v PS` [2020] UKSC 51 — `/uksc/2020/51` | VERIFIED_2026-09-27 · `SUBSTANCE_NOT_READ` | 配偶；婚内秘密摄录 | 非法观察通道需 `evidence_channel=ILLEGAL_OBSERVATION`；法庭对构念的规范评价不得当 latent state | deception / adversarial / institutional |
| N05 | `Currie v Currie` [2016] UKSC 19 — `/uksc/2016/19` | VERIFIED_2026-09-27 · `SUBSTANCE_NOT_READ` | 配偶；关系不披露 | 第三方关系的 belief 与 truth 分离；披露义务是制度事实不是关系状态 | deception / institutional |
| N06 | `Dougherty v Dougherty` [2015] EWCA Civ 805 — `/ewca/civ/2015/805` | VERIFIED_2026-09-27 · `SUBSTANCE_NOT_READ` | 高龄新婚、无子女、未圆房 | "未圆房"是法律事实，不授权对任一方向状态做任何推断。极短的 legal-vs-relational 检验器 | ordinary 边界 / adversarial |
| N07 | `Sharland v Sharland` [2015] UKSC 60 — `/uksc/2015/60` | VERIFIED_2026-09-27 · `CITED_SECONDARY`（corpus L2-001） | 1993–2015，多方第三方 | 已在 corpus 未冻结；知识时间分歧、说谎证据、嵌套反事实 | deception / longitudinal / adversarial |

### P0/P0-like — 官方机构记录（含调查委员会）

| id | pointer | 核实 | 权利 / 合法访问 | 判别性 | 覆盖 cell |
|---|---|---|---|---|---|
| N08 | LGSO 决定 `24-001-994`（Midshires Care）— `lgo.org.uk/decisions/adult-care-services/charging/24-001-994` | VERIFIED_2026-09-27 · `CITED_SECONDARY` | © LGSCO，官方永久库，匿名化；**无显式 CC → `UNKNOWN_RIGHTS`** | corpus 曾推荐但 `#19` source-switch 后未冻结，仍是高价值件；其 `Agreed action`（道歉+退款）是**机构补救**而非 dyad 修复 —— 这个区别本身是判别点 | kin / caregiving / institutional / repair |
| N09 | LGSO 报告库（Public Interest Reports / Focus Reports / Good Practice Guides）— `lgo.org.uk/information-centre/reports` | VERIFIED_VIA_SEARCH | 同上 | 粒度取舍教学：PIR 多案汇编、匿名化粗，**适合 case discovery 入口，不适合逐句 mapping** | institutional / care |
| N10 | Commission of Investigation into Mother and Baby Homes, Final Report（2020-10-30 / 2021-01-12）— `gov.ie/en/department-of-children-disability-and-equality/publications/final-report-of-the-commission-of-investigation-into-mother-and-baby-homes/` | VERIFIED_VIA_SEARCH（读到完整目录）· `CITED_PRIMARY_CONTENT`（仅结构） | 爱尔兰政府官方；Part 1–3 公开；**Part 4 Confidential Committee 已删节 → `BLOCKED`** | 非浪漫 + kin + 照护 + 制度 + 迁移（Ch.7 "Pregnant from Ireland"）+ 死亡（Ch.33）+ 收养（Ch.32）。**待确认**：Ch.32 是否记载"制度系统性篡改登记以掩盖亲子关系"（若是，即 §15.6 A07） | kin / non-romantic / caregiving / institutional / migration / bereavement / adversarial |
| N11 | Independent Inquiry into CSE in Rotherham 1997–2013（Alexis Jay OBE）— `rotherham.gov.uk/downloads/file/279/independent-inquiry-cse-in-rotherham` | VERIFIED_VIA_SEARCH | 市政厅出版，**无明确许可 → `UNKNOWN_RIGHTS`**；含未成年人 | 高 `THIRD_PARTY_INSTITUTIONAL` 密度与"机构知情却不动"结构。**按 corpus sensitive-content 规则，不进 fixture 池** | institutional（**不入池**） |
| N12 | Report of Inspection of Rotherham MBC（2015）— `assets.publishing.service.gov.uk/media/5a8152f4ed915d74e33fd945/46966_Report_of_Inspection_of_Rotherham_WEB.pdf` | VERIFIED_VIA_SEARCH | **Crown copyright 2015, OGL v3.0** | 问责链断裂的制度侧参照。**不入池**（未成年人） | institutional（**不入池**） |

### P1/P2 — 历史信件 / 同时代私人记录

| id | pointer | 核实 | 权利 | 判别性 | 覆盖 cell |
|---|---|---|---|---|---|
| N13 | The Diary of Samuel Pepys（1660–1669，Wheatley 1893）— `en.wikisource.org/wiki/Diary_of_Samuel_Pepys` | VERIFIED_2026-09-27 · `CITED_PRIMARY_CONTENT` | PD worldwide；文本 CC BY-SA 4.0 | (a) Case Bank 用诉讼做框时最缺的**普通、摩擦性、长期**婚姻（1660 私奔→1663 分居/和解/复婚）；(b) 第一人称把观察/信念/自我辩护压进同句；(c) 传闻转述密度极高；(d) **待确认**：1661 年男性同性行为指控条目（`UNVERIFIED_HYPOTHESIS`） | ordinary/stable / longitudinal / deception / same-sex（待确认） |
| N14 | Pliny the Younger, *Letters* III.7 & IV.7（Gaius Cornelius Gallus） | `UNVERIFIED_CANDIDATE` | 公有领域英译可用；**Loeb 版受版权控制 → `BLOCKED`** | 若核实：历史 same-sex dyad 唯一高证据载体；且当事人之一本人写贬损信，关系证据与社会评价同源 | same-sex / cross-cultural / bereavement |

### 表达力压力 / 公有领域叙事（Wikisource 访问路径已核实）

> 权利提示：Wikisource 原作公有领域标签与**文本** CC BY-SA 4.0 是两个独立轴；N17 的英译是活例。

| id | pointer | 核实 | 权利 | 判别性 | 覆盖 cell |
|---|---|---|---|---|---|
| N15 | 《紅樓夢》清，曹雪芹（前 80 回）/ 高鶚（後 40 回），120 回，庚辰本+程甲本汇校本 — `zh.wikisource.org/wiki/紅樓夢` | VERIFIED_2026-09-27 · `CITED_PRIMARY_CONTENT`（回目级） | PD（pma100 且 1931 前出版）；文本 CC BY-SA 4.0；CN/澳门/台湾**精神权**存续 | 回目即一级证据：第四十六回「鴛鴦女誓絕鴛鴦偶」、第六十九回「覺大限吞生金自逝」、第九十七回「林黛玉焚稿斷痴情 薛寶釵出閨成大禮」、第九十八回「苦絳珠魂歸離恨天」。判别点：同形式韵文在两个时点指向相反关系势能；"贞"被做成可被第三方裁决的制度程序；亲属称谓翻译塌陷致实体合并；第一回「甄士隱夢幻識通靈」/第五回「開生面夢演紅樓夢」直接给出嵌套模拟世界 | cross-cultural / kin / non-romantic / bereavement / deception / adversarial / L3 |
| N16 | George Eliot, *The Mill on the Floss*（1860）Book 3–7 — `en.wikisource.org/wiki/The_Mill_on_the_Floss` | VERIFIED_2026-09-27 · `CITED_PRIMARY_CONTENT`（章节清单+Index 入口） | PD worldwide；CC BY-SA 4.0 | **性价比最高的对抗件**：**兄妹 dyad**，强度极高、终生未言明 → 任何"以浪漫为默认 dyad"的映射会系统性误标。章节 `Illustrating the Laws of Attraction`、`A Family Council`、`A Day of Reckoning`、`St. Ogg's Passes Judgment`（社会评价 vs 事实）。**provenance 教学样本**：页面自述该书 loosely autobiographical、源自 George Eliot 与已婚男子的一段关系 —— **作者生平不得作为 dyad fact** | non-romantic / kin / ordinary / deception / third-party / adversarial |
| N17 | Ibsen, *A Doll's House*（1879，Sharp 英译）— `en.wikisource.org/wiki/A_Doll's_House` | VERIFIED_2026-09-27 · `CITED_PRIMARY_CONTENT`（页面元信息） | 原作 PD worldwide；**英译独立著作权轴**（页面自述译文另有版权状态，最长在世作者 1945 卒 → 美国 pre-1931 PD，life+80 按译者卒年）；**该英译无扫描背书（"source document not known"）→ provenance 下调** | 关系终止是**离开**：无离婚、无判决 → 检验 `pair_status` 与 `institutional_status` 是否真解耦；秘密借贷使约束与谎言并存 | opposite-sex / deception / separation / institutional(constraint) |
| N18 | Nguyễn Du, *Truyện Kiều*（*Đoạn Trường Tân Thanh*），20 関歌，Nôm 字 Chiêm Vân Thị 本转写 — `vi.wikisource.org/wiki/Truyện_Kiều` | VERIFIED_2026-09-27 · `CITED_PRIMARY_CONTENT`（实读前 ~1100 行） | PD worldwide（Nguyễn Du d.1820）；转写 CC BY-SA 4.0 | 实读原文：开篇「Trăm năm trong cõi người ta / Chữ tài chữ mệnh khéo là ghét nhau」把关系命运化；第 870–985 行金神诱骗→抵债→「Cầm dao tay áo tức thì giở ra」→「Một đao oan nghiệt đứt dây phong trần」。判别点：贞操检验是**被第三方执行的制度程序**；同形式律诗在求婚与送别指向相反势能；表面合法的再婚与实质胁迫并存 → 合法性/道德/关系状态三轴分离。**敏感**：成人胁迫，不含未成年人、不含露骨描写；按 câu 窗口化 | cross-cultural / opposite-sex / deception / separation / adversarial |
| N19 | Plato, *Symposium*（9 个公有领域英译）— `en.wikisource.org/wiki/Symposium_(Plato)` | VERIFIED_2026-09-27 · `CITED_PRIMARY_CONTENT`（**仅译本目录**；正文未读） | 各英译均 PD；CC BY-SA 4.0 | **仅 expressivity probe，永不进 completeness 池。** 判别点：关于同性欲望的段落以他人转述 + 戏剧反讽 + 醉语免责呈现，是"同一表面文字在不同 speaker/语境下含义不同"的最纯形态。**前置**：先读目标段（`UNVERIFIED_HYPOTHESIS`），预设高 MAPPING_FAILURE 率为设计目标 | same-sex / cross-cultural / expressivity / adversarial |

### 制度层 same-sex（CaseBank narrative 的边缘：制度性材料，非 dyad 叙述）

| id | pointer | 核实 | 判别性 | 覆盖 cell |
|---|---|---|---|---|
| N20 | `Zapp v Revenue Commissioners` [2006] IEHC 404（Ireland）— 官方应为 courts.ie（本次超时不可达）；仅在律所镜像读到判决文字 | `UNVERIFIED_OFFICIAL_ACCESS` | **最锋利的一条。** 判决原文同时写：不予承认该加拿大婚姻 **且** 原告"have amply demonstrated their love and commitment for one another"。→ **官方来源自己把描述性关系状态与法律地位显式分层**；任何把"不受承认"读成关系不存在/质量低的实现直接失败。同性 + 跨境（加拿大↔爱尔兰）+ 迁移/距离三 cell 同填 | same-sex / migration / cross-jurisdiction / adversarial / legal-vs-relational |
| N21 | `McD v L` [2009] IESC 81；`WOR v EH` [1996] IESC 4 | `UNVERIFIED_CANDIDATE` | 人工受孕 + 同性伴侣 + 生物学双亲权利 → 制度角色与关系状态彻底分离 | same-sex / kin / institutional |
| N22 | `Minister of Home Affairs v Fourie` [2005] ZACC 1（SA） | `UNVERIFIED_CANDIDATE`（saflii 403） | 制度层 same-sex；**宜作参照而非 dyad 主体** | same-sex / institutional |
| N23 | `Obergefell v Hodges`, No. 14-380 | `UNVERIFIED_CANDIDATE`（supremecourt.gov 与 govinfo 候选 URL 均 404；CourtListener API 200 可达索引） | 同上 + "索引层 ≠ 权威层"教学样本 | same-sex / institutional |

## 15.3 `CALIBRATION_DATASET`（不是 CaseBank narrative）

| id | pointer | 核实 | 为什么归 calibration | 合法用途 |
|---|---|---|---|---|
| N24 | ACF, *Child Maltreatment 2023*（2025-01-08，297 页，第 34 版）— `acf.gov/cb/report/child-maltreatment-2023`；PDF `acf.gov/sites/default/files/documents/cb/cm2023.pdf` | VERIFIED_VIA_SEARCH · `CITED_PRIMARY_CONTENT` | 原文：各州为"each report of **alleged** child abuse and neglect that received a CPS response"构造 child-specific 记录，且"only includes completed reports with a disposition (or finding)" → **字面意义上把 fact-status 做成主键**的总体级数据 | (a) 校准 allegation→substantiation 基率（**明确不进 Case Bank 概率推断**）；(b) 训练 "alleged ≠ adjudicated" 映射习惯；(c) 校准 `fact_status` 词表合法取值。**restricted-use 文件在 NDACAN（`ndacan.acf.hhs.gov`）需申请，不下载、不引用个人级记录** |
| N25 | Chinese Family Panel Studies — `isss.pku.edu.cn/cfps/` | VERIFIED_2026-09-27 (200) | 典型 panel 调查：可做 prior/分布/跨代比较，**不能**做 case narrative 重建 | 中文构念语义等价性的测量基础。须注册+签署协议；不镜像个人级数据 |
| N26 | National Elder Abuse Data (NEAD, DOJ APS) | `UNVERIFIED_CANDIDATE` | 若成立，是"报告未被证实"这一 adversarial 单元的结构化来源 | 只作 fact-status 校准，**不作 fixture** |

## 15.4 `TOOLING_INDEX`

| id | pointer | 核实 | 许可 / 角色 | 限制 |
|---|---|---|---|---|
| N27 | Find Case Law, TNA — `caselaw.nationalarchives.gov.uk/`（UKSC 2009–2026 近全覆盖；判例回溯至 2003，tribunal 多数至 2016） | VERIFIED_2026-09-27 | 官方 **source-of-record**；Open Justice Licence | 英国 P0 唯一权威入口；保存快照 + 取用日期；不得用镜像替代 |
| N28 | CourtListener REST API — `courtlistener.com/api/rest/v4/search/` | VERIFIED_2026-09-27 (JSON 200) | Free Law Project；API 需 token（认证非付费墙）；角色 = **mirror/index** | 硬规则：美判权威必须回溯 `supremecourt.gov` / 州法院 docket |
| N29 | `hueyy/lacuna-db` | VERIFIED_2026-09-27 | **`license=NOASSERTION` → `UNKNOWN_RIGHTS`**；Singapore | 仅 pointer |
| N30 | `vanga/indian-supreme-court-judgments` | VERIFIED_2026-09-27 | 代码 **CC BY 4.0**；数据经 AWS Open Data | 权威回溯 `api.sci.gov.in`；印度多属人法并存 → 潜在"同表面文字跨社群异义"富矿 |

## 15.5 覆盖矩阵

图例：`●` 实质填充 · `◐` 需加工/部分 · `○` 合法缺口 · `✗` 无候选

| 必需 cell | F001 Carty | F002 Magi | F003 StoryCorps | 本批主填 | 状态 |
|---|---|---|---|---|---|
| ordinary / stable | ○ | ●(单日高张力) | ○(临终) | N13 ●, N16 ◐, N02 ◐ | **◐ 靠 P2 代理**。**结构性发现：以诉讼/申诉为框的官方记录按构造无法产出"无争议的普通关系"** —— 必须写进 Case Bank 头部声明 |
| cross-cultural | ○ | ○ | ○ | N15 ●, N18 ●, N10 ●, N19 ◐, N20 ◐ | **●** |
| non-romantic | ✗ | ✗ | ✗ | N16 ●, N01 ●, N15 ◐, N10 ◐ | **●** |
| kin | ✗ | ✗ | ◐ | N01 ●, N10 ●, N16 ●, N03 ◐, N21 ◐ | **●** |
| caregiving | ✗ | ✗ | ◐ | N01 ●, N10 ●, N08 ●, N16 ◐ | **●** |
| same-sex | ✗ | ✗ | ✗ | N20 ◐, N19 ●(expressivity), N14 ◐, N21/N22/N23 ◐ | **◐ 结构性缺口**（**X-14：在本次检索范围内**未找到"当代、逐句、私域、已裁判"的合法同性 dyad 记录；本轮读到的官方材料一律为**制度性**材料。**不主张**该类记录在全部合法来源中不存在） |
| opposite-sex | ● | ● | ● | N04/N05/N06/N17/N18 ● | **● 已过度满足，需防失衡** |
| longitudinal | ◐ | ● | ● | N13 ●, N15 ●, N01 ●, N02/N07 ◐ | **●** |
| deception | ● | ● | ◐ | N04 ●, N15 ●, N18 ●, N03/N05/N10/N13 ◐ | **●** |
| recovery / repair | ✗ | ○ | ○ | N08 ◐, N13 ◐, N17 ◐ | **○→◐ 真实缺口**。**发现**：官方记录里的"修复"几乎都是**机构补救**，不是 dyad 内部修复 |
| breakup / reconciliation | ◐ | ○ | ○(丧偶) | N17 ●, N15 ●, N18 ●, N02/N13 ◐ | **◐** |
| migration / distance | ○ | ✗ | ✗ | N10 ●, N20 ●, N15/N18/N03 ◐ | **●**（首次真正补上） |
| bereavement | ○ | ✗ | ● | N15 ●, N18 ●, N14 ●, N10 ● | **●** |
| institutional / professional | ● | ○ | ✗ | N01 ●, N04 ●, N10 ●, N05/N17 ◐ | **●** |
| adversarial | ◐ | ◐ | ◐ | §15.6 A01–A14 + `DERIVED_TRANSFORM` 池 | **●** |

**诚实缺口（不可填充掩盖）**：① 当代私域 same-sex 逐句记录不存在；② 无争议普通稳定关系的 P0 记录按构造不存在；③ dyad 内部"修复"官方来源基本不产出；④ 中国大陆官方可稳定引用的家事判决本次不可达（`wenshu.court.gov.cn` 与最高法指导性案例 `UNVERIFIED`），中文需求暂由公有领域文本满足；⑤ 非西方/非英语 P0 裁判文书稳定全文入口本环境全部不可达 —— **这是核实限制，不是可用性结论**。

> **X-14 检索范围声明（Round-3 新增，适用于上列 ①–③ 与全表所有"不存在 / 缺口"格）**：以上一律是**本次检索范围**（本轮实读的 Find Case Law / LGSO / gov.ie / rotherham.gov.uk / 各类 Wikisource，以及 §15.12 记录的可达与不可达站点）下的结果，**不是**关于法律与档案可获得性的领域存在性结论。逐项改述为：
> ① 「在本次检索范围内未找到**当代、私域、逐句、已裁判**的合法同性 dyad 记录；本轮读到的官方材料一律为制度性材料」——**不说**"这种记录不存在"。
> ② 「以**诉讼 / 申诉**为框的官方记录**按构造**无法产出无争议的普通关系」——这是关于**该类来源的结构性限制**的陈述（可辩护），**不是**关于全部合法来源的存在性陈述（未主张）。
> ③ 「在本次检索范围内读到的官方记录里的'修复'几乎都是机构补救」——**不说**"dyad 内部修复在官方来源中不存在"。
> 同格处理：§15.5 `same-sex` 行的「不存在"当代、逐句、私域、已裁判"的合法同性 dyad 记录」与 §15.7 **C-3**、§15.11 U 系列的相关条目，均按上述口径读取。

## 15.6 Fixture 设计模板 v0.2

### 15.6.1 头部 metadata block

```text
fixture_id / fixture_status
package_kind: FACT_RECORD | NARRATIVE_TEXT | DERIVED_TRANSFORM | SYNTHETIC_PROBE
artifact_class: REAL_NARRATIVE | DERIVED_TRANSFORM | SYNTHETIC_PROBE
derivation_recipe: <变换 id + 参数 + 父 fixture_id + 逐条 diff>      # 仅 DERIVED_TRANSFORM

provenance_grade: P0 | P0_like | P1 | P2 | P3 | P4
provenance_basis: ADJUDICATED_RECORD | STATUTORY_INQUIRY | PEER_REVIEWED | OFFICIAL_STATISTIC
                 | SCHOLARLY_EDITION | PUBLIC_DOMAIN_TEXT | FIRST_PERSON | EDITORIAL
source_of_record_pointer / retrieval_tools / retrieved_on / snapshot_ref

jurisdiction / culture / period
core_dyad / secondary_dyads
agent_register:  agent_id, kind ∈ {DYAD_MEMBER, THIRD_PARTY_PERSON, INSTITUTION},
                authority_scope, first/last_appearance_time

t0_anchor                                   # 落实 #13 comment 2；当前三份全缺
holdout_policy: STRICT | SOFT
expected_unit_count / expected_decorative_unit_band
coverage_cells_claimed / leakage_tier
sensitive_flags
rights: licence, redistributable, transform_allowed, verbatim_quota,
        pointer_only_required, robots_note, verified_on, verified_by
schema_ref: CURRENT_ARCHITECTURE + PARAMETER_CONVERGENCE + CONSTRUCT_SCOPE_DIRECTIONALITY @ sha
downstream_contract: Eye handoff ref + Juece Claim 规则
        + "observed_at（证据观测时间）≠ recording_time/event_time/knowledge_time（故事内时间）"
```

### 15.6.2 每行 atomic unit（单一受控词表）

```text
unit_id
unit_type ∈ { observed_event, reported_event, recalled_event, speech, written_document,
              thought, belief, habitual_pattern, plan, evaluation, metaphor, environment,
              institutional_record, third_party_report, metadata, other }
unit_type_note: <若 other 必须写理由；other 不得作兜底>

event_time / recording_time / publication_time
temporal_basis ∈ { EVENT_TIME, RECORDING_TIME, PUBLICATION_TIME,
                   RETROSPECTIVE_RECONSTRUCTION, UNKNOWN }
knowledge_time_by_agent: { agent_id -> 首次可知时间 / UNKNOWN }

speaker_ref / reported_speaker_ref(s)
attribution_depth ∈ 0..3                 # 让"多层转述"可被计数

fact_status ∈ { ADJUDICATED, ADMITTED, ALLEGED, DISPUTED, UNKNOWN }   # 单一受控表，必须含 UNKNOWN
assertion_mode ∈ { NARRATOR, SPEECH_ACT, CHARACTER_THOUGHT, CHARACTER_BELIEF, HABITUAL,
                   FIGURATIVE, INSTITUTIONAL_RECORD, EDITORIAL_FRAME, METADATA,
                   WRITTEN_DOCUMENT }
evidence_channel ∈ { DIRECT, TESTIMONIAL, DOCUMENTARY, INFERRED,
                     ILLEGAL_OBSERVATION, ABSENT }                   # 当前三份最大缺口
evidence_weight_note

holdout_class ∈ { PRE_T0, POST_T0 }                                # 落实 #13 comment 2
decidable_without_holdout ∈ yes/no
preparer_decorative_hint: yes/no/unknown                            # 仅 adjudicator 可见
mapping_expectation ∈ <七值> | UNSET                                 # 空白优先，禁止预设答案
```

**为何 `fact_status` 与 `assertion_mode` 必须是两个轴**：Carty 有法律轴（`adjudicated/disputed/unknown`），Magi 有叙述轴（`character_thought/narrator_evaluation`），StoryCorps 把两者混在一个 7 值表并多一个 `other`。任一份单独看都自洽，三份并列就不可比 —— 而 Case Bank 的全部价值来自跨 fixture 比较（regression 与语义漂移）。这是必须在上游修掉的隐性缺陷。

### 15.6.3 Mapping-test harness

> **覆盖 ≠ 最小性（X-9）**：本 harness 产出的是 **coverage / closure / mapping-failure profile**。它**不产出**构念最小性（"删掉某个 construct 后是否仍有无法表示的重要句子"）的任何证据。最小性需要 (a) 独立的 **construct-bearing 单元**（见 §15.1.1；`F001` 与本报告 N01–N30 **都不算**），与 (b) 一条 **leave-one-construct-out** 的臂——后者在本项目当前的任何门里都**不存在**（Round-3 记录，见 `17` §3 F1 的处置段）。两者都不可用时，本 harness 的结果**不得**被引用为 8 项 basis 的必要性证据。

1. **单一 verdict 词表**：`DIRECT | PARTIAL | MULTI | NARRATIVE_ONLY | IRRELEVANT | UNKNOWN | MAPPING_FAILURE`。
2. **`MAPPING_FAILURE` 必附九类之一**（`#13` comment 3）：`ONTOLOGY_HOLE / CONSTRUCT_HOLE / SCOPE_HOLE / TEMPORAL_HOLE / BELIEF_OBSERVATION_HOLE / TRANSITION_HOLE / MEASUREMENT_HOLE / NARRATIVE_ONLY / DATA_INSUFFICIENT`。
3. **`UNKNOWN` 与 `MAPPING_FAILURE` 必须分清**：`UNKNOWN` = 材料不足；`MAPPING_FAILURE` = 材料充分但表示装不下。
4. **盲化输入**：Verifier 只拿 `PRE_T0` 单位 + 冻结 schema + 本协议；`POST_T0` 只用于事后 hindcast 对照。
5. **禁止补参数**：不得新增 construct/scope/transition，不得改写 fixture。违规即使答案"对"也作废。
6. **必备统计**：`coverage_rate / partial_rate / failure_count / failure_clusters`（九类 × `unit_type` × `assertion_mode` 交叉）、`ad_hoc_parameter_count / new_top_level_category_count / UNKNOWN_vs_FAILURE_confusion_rate`。
7. **跨 fixture 语义漂移检查**（当前三份均不支持）：维护 12–20 条 `SIT::` 语义情境锚点集（`SIT::FAMILY_OBLIGATION / CARE_VS_AUTONOMY / INSTITUTIONAL_REMEDY / THIRD_PARTY_DECIDES / BELIEF_LAGS_OBSERVATION / LEGAL_STATUS_NOT_RELATIONAL_STATE / KINSHIP_TERM / SECRET_KEPT_FROM_PARTNER / SURFACE_FORM_POLYSEMY` …），每份 fixture 标注覆盖哪些 `SIT::`。这是 `#13` 成功标准 4 的唯一可执行落地方式 —— 三份 fixture 的 unit id 完全本地化、互不可比。
8. **泄漏探针**（低成本可跑）：向模型索要 `t0` 之后结局，记录其是否**无文本依据**地给出正确答案。`leakage_tier=HIGH/VERY_HIGH` 的 fixture 必须附探针结果，否则不得计入跨版本 coverage 上升趋势。
9. **独立性**：Verifier 不参与参数表设计；三个独立 Verifier 消费同一 `merged exact version`。

### 15.6.4 `DERIVED_TRANSFORM`：把不可获得的对抗性变成可获得

§15.5 的 6 个诚实缺口里，多个（ordinary、repair、same-sex 私域）在合法来源中按构造不存在；而 corpus 与 `#13` 均禁止"生成式 AI 发明故事"。

**建议（AI recommendation）**：引入第三类 fixture —— 由已冻结真实 fixture 派生的变换件，只允许**保持语义内容的机械变换**：

- `T1_time_shift`：事件链整体平移一个已显式声明的 `Δt` → 检验 `TEMPORAL_HOLE` 与绝对日期泄漏。
- `T2_holder_swap`：交换 `knowledge_time_by_agent` / `attribution_depth` → 检验 belief/observation 分离。
- `T3_status_flip`：`fact_status` 在 `ADJUDICATED ↔ DISPUTED ↔ UNKNOWN` 间重标（**不改文字**）→ 直接检验"provenance 等级 ≠ fact status"这条核心纪律。
- `T4_holdout_withhold`：删掉 `t0` 之后单位、保留时序缺口 → 检验模型是否把"未记录"填成"未发生"。
- `T5_surface_form_reuse`：同一引语复制到另一时点/说话人 → 检验是否 keying on surface form。

规则：逐条 diff 写入 `derivation_recipe`；继承父件 rights 与 `fact_status`，绝不升级证据等级；`DERIVED_TRANSFORM` 与 `REAL_NARRATIVE` **不得混入同一 coverage 统计**（前者只测敏感性，后者才测完备性）；它**不是绕过缺口的借口** —— 对应格在矩阵中仍标 `○`，仅加注"有诊断代理"。

**成本收益**：这是本报告里单份成本最低、对抗性收益最高的一条。Carty 与 LGSO 已冻结，`T1–T5` 几乎零采集成本。

## 15.7 对抗性 fixture 清单（A01–A14）

> **本清单的被检验对象（X-9）**：以下 14 条全部是 **representation / mapping-failure 判据**，**不是**构念最小性判据。它们测的是"某一类现实句子能否被合法表示"，**不测**"8 项 relationship-state 构念是否都必要"。用它们支持构念 ablation 是类目错误（见 §15.1.1）。另注：**A06** 以 F003 为载体，在 Fixture 003 的权利裁决落地前**不可执行**（见 §15.1）。

| id | 对抗类型 | 载体 | 失败判据 |
|---|---|---|---|
| A01 | 同一段表面文字在不同时间含义不同 | N18（求婚/送别同形式律诗）、N15 | 按 surface form 建边界的实现给出同一条边；正确行为是边语义随 `event_time` 变 |
| A02 | 同时为真、被相信、且为假 | N07 C012+C013+C017 | 单一真值字段二选一即失败；须三轴并存 |
| A03 | 嵌套反事实 | N07 法官"换我会怎么做"；N02 拒绝裁判的关系事实 | 反事实被提升进 `WorldState` 即失败；须留在 nested `Belief` 并带 `history_id` |
| A04 | 第三方实质决定 dyad | N01（NHS/CCG 而非父母决定照护）、N10、N03 | 把照护建成天然双向 dyad 即失败；须支持部分不存在/机构中介/被指令的边 |
| A05 | 构念在无可观测事件下翻转 | N02（多年无接触） | 带时间衰减先验的模型**自信地**产生零证据轨迹即失败；须保持区间 + `DATA_INSUFFICIENT` |
| A06 | 唯一证据是单方多年后的重构 | F003（Danny 2004 回忆 1978）、N10 幸存者陈述 | 证据来源权重被当均匀即失败 |
| A07 | 记录本身被制度篡改 | N10 Ch.32（**待原文确认**，`UNVERIFIED_HYPOTHESIS`） | 把文档当独立第二真相源即失败。**最强的单条** |
| A08 | 构念是法律类别、关系内容为零 | N06（未圆房） | 从法律类别向任一方向状态做推断即失败 |
| A09 | 非法观察通道 | N04（婚内秘密摄录） | 未经 `evidence_channel=ILLEGAL_OBSERVATION` 过滤即摄取即失败 |
| A10 | 关系存续与法律解体相互独立 | N02；N17（离开 = 无法律事件） | `pair_status` 与 `institutional_status` 合并即失败 |
| A11 | 同一事件存在两套互不兼容的官方叙述 | N07 C025 | last-write-wins 真值累积即失败 |
| A12 | 非浪漫但极强强度的 dyad | N16（兄妹） | 需要浪漫先验才能表达高强度 directed state 即失败；亲属称谓不得塌陷 |
| A13 | 亲属术语在非西方体系中的歧义 | N15（`姨娘/庶出/嫡出/舅父/表兄`） | 翻译归一化导致实体合并即失败 |
| A14 | 制度性不承认 ≠ 关系不存在 | **N20 `Zapp` [2006] IEHC 404** | 把"不受承认"读成关系不存在/质量低即失败。**官方原文级检验** |

## 15.8 排序提案

准则：(1) 合法可读、权利清楚、无需等 gate；(2) 每份打一个当前三份没打过的**结构性假设**；(3) 至少一半为非对抗性材料，防止 Case Bank 退化成极端案例动物园；(4) 跨语言标注成本单列。

### Wave A —— 立刻做（4 份，无需任何 rights gate）

| 序 | fixture | t0 | 理由 |
|---|---|---|---|
| A-1 | **N02 `H v H` [2022] UKPC 3** | 起诉/申请日 | 唯一能一次性落实 `#13` comment 2 的 `INPUT/HOLDOUT` 分离的短件；"法律结论 ≠ 关系状态"最便宜检验器；无未成年人、无性内容。**须先读原文确认 fact_status 分布** |
| A-2 | **N16 `The Mill on the Floss` Book 3–7**（`A Family Council` → `Conclusion`） | 订婚破裂 / `St. Ogg's Passes Judgment` | 最便宜的"非浪漫 + kin"击穿件；公有领域、无 gate、无敏感内容、章节清单已核实 |
| A-3 | **N06 `Dougherty v Dougherty` [2015] EWCA Civ 805** | 传票日 | 极短；高龄/无子女/未圆房，一次打掉"典型恋爱 dyad"先验与"法律类别→latent state"泄漏 |
| A-4 | **N10 Mother & Baby Homes，Ch.7 + Ch.32 窗口** | 某具体收容年度 | 结构载荷最高（非浪漫+kin+照护+制度+迁移+死亡）。**前置：先读 Ch.32 确认 A07** |

三份为非对抗性材料。N02/N06 官方 URL 本轮已 200 核实；N16 无 gate。

### Wave B —— 下一批（4 份）

| 序 | fixture | 理由 |
|---|---|---|
| B-1 | **N01 `N v ACCG` [2017] UKSC 22**（t0 = care order 终止 / 18 岁） | 唯一我有**官方原文级证据**（press summary 全文）的候选；kin+照护+制度+无能力+第三方决定全在一件；t0 干净 |
| B-2 | **N18 `Truyện Kiều`**（câu 窗口化，避 brothel 章） | 跨文化 + 制度化贞操检验 + 表面形式多义。**成本警告**：需越南语/中文标注能力；不具备时 A15 紅樓夢可替代并同样满足 cross-cultural |
| B-3 | **N13 `Pepys` Diary**（一月窗口） | 唯一合法可得的高质量"普通+摩擦+长期"第一人称婚姻记录，压 ordinary 与 repair 两格。**高 leakage + 须先定位 1661 条目** |
| B-4 | **`DERIVED_TRANSFORM` T1–T5**（父件 Carty + LGSO） | 采集成本≈0，对抗/回归收益最高；**必须与真实件隔离评分** |

### Wave C —— 需 gate 或跨语言资源，defer

C-1 N15 紅樓夢 选章（需中文标注 + 120 回切分）；C-2 N17（英译 provenance 弱）；C-3 N19（**仅 expressivity probe，永不进 completeness 池**）；C-4 N20（gate：courts.ie 官方 URL）；C-5 N04/N05/N03/N07（官方源成本低但同类已饱和，**过早加入会继续放大 `#13` 已警告的 selection bias**）。

### 明确不做

- N11 / N12（未成年人性剥削）—— 只作 case discovery 与设计输入，**不进 fixture 池**（与 `VALIDATION_CORPUS_V0_1.md` 已有 sensitive-content 规则一致）。
- N24 / N25 / N26 —— 只作 calibration / `fact_status` 词表校准，**禁止转成 CaseBank 叙述**。
- N27–N30 —— 只作 tooling/index。

## 15.9 权利与许可（汇总）

| 范围 | 状态 | 处理 |
|---|---|---|
| N01–N07（Find Case Law 判例） | Crown copyright / **Open Justice Licence**，免费阅读复用（署名） | paraphrase + pointer；不镜像全文 |
| N08–N09（LGSO） | © LGSCO，匿名化官方库；**无显式 CC → `UNKNOWN_RIGHTS`** | pointer + paraphrase；`repr_text` 体积设上限 |
| N10 | 爱尔兰政府官方；Part 1–3 公开；**Part 4 已删节 → `BLOCKED`** | 窗口化 + pointer；**不得索取或重建 Part 4** |
| N11 | **无明确许可 → `UNKNOWN_RIGHTS`**；含未成年人 | 仅 pointer，**不入池** |
| N12 | **Crown copyright 2015, OGL v3.0** | 可读复用；**不入池** |
| N13 | PD worldwide；文本 CC BY-SA 4.0 | 可引用改写，保留出处与许可标注 |
| N14 | 公有领域英译可用；**Loeb 版受控 → `BLOCKED`** | 采用前须核实版本与许可 |
| N15 | PD（pma100 + 1931 前）；文本 CC BY-SA 4.0；**CN/澳门/台湾精神权存续** | 保留出处与许可标注 |
| N16 | PD worldwide；CC BY-SA 4.0；有 Index 扫描件可回溯 | 另：**作者生平不得作 dyad fact** |
| N17 | 原作 PD；**英译独立著作权轴**；**无扫描背书** | provenance 下调；只作 L2 表达力件 |
| N18 | PD worldwide（Nguyễn Du d.1820）；转写 CC BY-SA 4.0 | 窗口化；敏感标注 |
| N19 | 各英译均 PD；CC BY-SA 4.0 | 仅 expressivity probe |
| N20 | 爱尔兰判决 Crown copyright；**官方 host 不可达，镜像不得当 canonical** | 待确认后入池 |
| N21–N23 | `UNVERIFIED`；Obergefell 若为美国政府作品则 PD，但**官方 PDF 位置需重新确认** | 全部 gate 在官方 source-of-record 指针 |
| N24 | 美国联邦政府作品，公有领域；**case-level restricted-use 需向 NDACAN 申请** | 只作 calibration；不下载个人级记录 |
| N25 | 官方站；**须注册 + 签署协议** | 不镜像个人级数据 |
| N26 | `UNVERIFIED` | gate |
| N27 | 官方 source-of-record；Open Justice Licence | 发现 + 版本固定 |
| N28 | Free Law Project；API 需 token（认证非付费墙）；**mirror/index** | 权威回溯法院 |
| N29 | **`NOASSERTION` → `UNKNOWN_RIGHTS`** | 仅 pointer |
| N30 | 代码 **CC BY 4.0**；判决为官方公开文书 | 权威回溯 `api.sci.gov.in` |

**统一规则（AI recommendation）**：`pointer_only_required = yes` 的 fixture，下游（Eye/Juece/LHRM）一律不得持久化正文，只存 anchor + paraphrase + 事实摘要。与 Fixture 003 已实现的 `HUMAN_REVIEW_REQUIRED → POINTER_HASH_ONLY` 边界一致（**AI recommendation，具体 rights 决策权在 Eye / Human**）。

## 15.10 明确不主张

1. **不主张**任何"判别性"判断是实验结论。除 N01/N10/N24/N25/N30/N15/N16/N17/N18/N19 的实读部分外，均为**预映射假设**（`SUBSTANCE_NOT_READ` / `UNVERIFIED_HYPOTHESIS`）。
2. **不主张** LHRM 当前 schema 在任何一条上有 `MAPPING_FAILURE`。本 lane 未做任何 mapping。
3. **不主张**任何材料能提供 base rate、发生概率或参数权重。
4. **不主张** `DERIVED_TRANSFORM` 能替代缺失的真实材料。
5. **不主张**中国/爱尔兰/南非/印度/荷兰/澳洲官方源"不存在"或"不可用" —— 本次是**本环境出口网络**无法访问（超时/403/TLS/404）。这是核实限制，不是可用性结论。
6. **不主张**项目当前存在 ontology 缺口。§15.7 每条都是判据，不是已观察到的失败。
7. **不主张**三份已冻结 fixture 有错；意见是关于**跨 fixture 可比性**与 `#13` comment 2 合规性**的流程缺口**。
8. **不主张**读过 `#20`/`#21`/`#22`、Eye、Juece、`#30`、PR31。未读、未引、未改。
9. **不主张**任何 unit 数、unit_type 或词表属于 LHRM 本体。它们是材料层标签。
10. **不主张** Fixture 001 能检验 8 项 relationship-state 构念的必要性（X-9）。它检验的是事实 / 观察 / 信念 / 行为 / 历史 / provenance 的**表示与映射失败语义**；其 core dyad 为雇主↔雇员，26 个原子事实为机构性事实。**构念最小性需要独立的 construct-bearing benchmark；本报告只指出该依赖，不建造它。**
11. **不主张**本报告新增的 N01–N30 构成 construct-bearing 材料。它们是公开记录或公有领域叙事，取样理由是关系**情境**覆盖，不是构念**承载**。
12. **不主张** Fixture 003 的权利状态可由本报告推进。`HUMAN_REVIEW_REQUIRED` / `POINTER_HASH_ONLY` fail-closed / `ai-train=no` + GPTBot/ClaudeBot/CCBot `Disallow` 全部继续生效；权利裁决与 canonical 指针重新定位均属 Human / Architect（见 §15.1）。
13. **不主张** §15.5 / §15.7 / §15.11 的任何"不存在 / 缺口"是领域存在性结论（X-14）；一律为**本次检索范围**下的结果。

## 15.11 剩余未知

U1 N02–N07 实质事实段与 fact_status 分布（阻塞其 `t0`/unit 数/赋值）· U2 N10 Ch.32 是否记载系统性篡改登记（阻塞 A07 载体）· U3 N20 courts.ie 官方 URL（阻塞 Wave C）· U4 Pepys 1661 条目是否存在（决定 N13 是否同填 same-sex）· U5 `wenshu.court.gov.cn` 与最高法指导性案例可用性（阻塞中国 P0）· U6 非西方官方源可用性（`courts.ie`/`saflii`/`austlii`/`uitspraken.rechtspraak.nl`/`judiciary.ie`/`rcirc`/`agedcarecommission`/`justice.gov`/`ons.gov.uk`/`pair.wustl.edu` 本次全部不可达）· U7 N17 英译无扫描背书是否满足 corpus 的 scan-backed 要求 · U8 项目是否接受 `DERIVED_TRANSFORM` 这一 fixture 类（**Human decision**）· U9 `SIT::` 锚点集最终条目（需 Verifier×3 共识轮）· U10 三份已冻结件是否**追补** `t0`/`holdout_class`（**Human decision**；本报告不主张回改）· U11 N16 目标章节确切情节（我只核实到标题）· U12 N19 目标段落行文（正文未读）· **U13（Round-3 新增）** `FIXTURE_003` 的权利裁决（`HUMAN_REVIEW_REQUIRED` + Eye `POINTER_HASH_ONLY` fail-closed + `robots.txt` `ai-train=no` + canonical 页 URL 2026-09-14 实测 404）及其是否计入"3 份已冻结 fixture"，以及现行 canonical 指针是否需重新定位（**Human 权利裁决 + Architect 记录裁决**；本报告不裁定，§15.7 A06 在此之前不可执行）· **U14（Round-3 新增）** 构念承载基准（construct-bearing benchmark）的规格与落点（**由另一个 child 规划中**；本报告只指出依赖，见 §15.1.1。`N01`–`N30` 与 F001/F002/F003 **均不构成**构念承载材料）· **U15（Round-3 新增）** §15.5 / §15.7 中"不存在 / 缺口"类陈述的**完整总体口径**：当前全部为检索范围陈述（X-14），是否需要一次专门的可获得性调研属 Human 决定。

## 15.12 核实日志（2026-09-27）

**成功（HTTP 200 / 完整页读取）**：`caselaw.nationalarchives.gov.uk` 6 个 judgment 页（`/uksc/2015/17` 157,606B、`/uksc/2016/19` 97,563B、`/uksc/2020/51` 241,614B、`/uksc/2017/22` 82,434B、`/uksc/2015/60` 70,580B、`/ewca/civ/2015/805` 78,071B、`/ukpc/2022/3` 58,400B）；`lgo.org.uk`(54,148B) + 决定 `24-001-994`(48,621B)；`courtlistener.com/api/rest/v4/search`(JSON 55,658B)；`api.github.com` × 3；`isss.pku.edu.cn/cfps/`(10,988B)；`zh.wikisource.org/wiki/紅樓夢`；`en.wikisource.org` 的 `Symposium_(Plato)` / `The_Mill_on_the_Floss` / `Diary_of_Samuel_Pepys` / `A_Doll's_House`；`vi.wikisource.org/wiki/Truyện_Kiều`（并实读前 ~1100 行）。

**成功（经 websearch 取得官方页面文字）**：`gov.ie` Mother & Baby Homes 报告页（含完整目录）；`rotherham.gov.uk` Jay Inquiry；`assets.publishing.service.gov.uk` Rotherham 监察报告（OGL v3.0 明示）；`supremecourt.uk` N v ACCG press summary 全文片段；`acf.gov/cb/report/child-maltreatment-2023` 与 `cm2023.pdf`；`files.localgov.co.uk` LGSO 年报；`lgo.org.uk/information-centre/reports`。

**失败（负面结果）**：
- `caselaw.nationalarchives.gov.uk/uksc/2017/58` → **404**（记忆中的 `ML v DL [2017] UKSC 58` 引证不存在，**该案未采用**）。
- `gutenberg.org`（www/非 www、`/ebooks/*`、cache 直链、`gutendex.com`）→ 全部超时（curl + webfetch 双路）。**本轮无法核实任何 Gutenberg 书目号**；F002 依赖的 `7256` 沿用 corpus 2026-09-11 的 live-fetch 记录。
- `en.wikisource.org` 的 `Persuasion_(Austen)` / `Chaereas_and_Callirhoe` / `Sappho:_A_Portrait_in_Broken_Verses` / `Njal's_Saga` → **404**，相应候选未采用。
- `motherandbabyhomes.com` 404；`motherandbabyhomes.ie` transport error。
- `saflii.org` 403；`jade.io` / `austlii.edu.au` / `indiankanoon.org` / `uitspraken.rechtspraak.nl` / `courts.ie` / `ons.gov.uk` / `acf.gov`(直连) / `justice.gov` / `doj.gov` / `pair.wustl.edu` / `rcirc.gov.au` / `agedcarecommission.gov.au` / `catalog.afs.gov` / `archive.org` → 超时或 schannel TLS 失败。
- `judiciary.ie` → schannel `SEC_E_WRONG_PRINCIPAL`。
- `supremecourt.gov/opinions/14pdf/14-380_3204.pdf` 404；`govinfo.gov` USCOURTS-scotus-14-380 package 404。
- `websearch` 两次 **429**、一次 transport error。
- GitHub 许可核实：`DyadicDataAnalysis` = GPL-3.0 / pushed 2022-04-26 / stars 1（**几乎无人维护，视为示例代码而非可复用库**）；`lacuna-db` = `NOASSERTION` / pushed 2026-09-13；`vanga/indian-supreme-court-judgments` = CC-BY-4.0 / pushed 2026-07-17 / stars 91。
- 未读、未引、未改：`#20`/`#21`/`#22`；Eye；Juece；`#30`；PR31。未 push / comment / PR。

## 15.13 状态建议

**`PARTIAL`**

- **设计侧完成**：四类分离、30 条指针、覆盖矩阵（含 6 个诚实缺口）、设计模板 v0.2（13 项改进 + harness 9 条 + `DERIVED_TRANSFORM`）、14 条 adversarial、排序、逐源权利 —— 全部交付，**无一条来源是编造的**。
- **未升 SUCCESS 的原因**：① 30 条中 7 条为 `UNVERIFIED_CANDIDATE` / `UNVERIFIED_OFFICIAL_ACCESS`，主因本环境出口对 `courts.ie`/`saflii`/`rcirc`/`agedcarecommission`/`justice.gov`/`pair.wustl.edu`/`gutenberg.org` 全部不可达；② N02–N07 的判别性理由是未读原文的假设；③ 4 个必需 cell 只能标 `○` 或 `◐`，其中"当代私域 same-sex 逐句记录"按我的判断在合法来源中不存在 —— 但我没有权威来源支撑"不存在"，故亦为带保留的判断。
- **升 SUCCESS 的条件**：换网络出口重跑 §15.2–15.4 全部核实（U6），补读 N02–N07 原文（U1）与 N10 Ch.32（U2），确认 N20 官方 URL（U3）。这是纯核实工作，不需新设计。
- **给 parent 的最小建议**：**Wave A-1 / A-2 / A-3 可立即授权开工** —— N02、N06 官方 URL 本轮已 200 核实，N16 公有领域无 gate；三者不依赖任何待确认项，且分别打 `#13` comment 2 合规性、非浪漫 kin、legal-vs-relational 三个当前空缺或结构性有缺的假设。**明确不建议**：在剩余核实完成前，不要把 N02–N07 的 `t0`、unit 数或 `fact_status` 赋值写进任何 durable fixture。
- **Round-3 追加（不改变 `PARTIAL` 定级）**：
  - **X-9 已补记**（§15.1.1）：Fixture 001 的被检验对象是**表示与映射失败语义**，**不是** 8 项 relationship-state 构念的必要性；构念最小性需要独立的 construct-bearing benchmark，其规划在另一个 child 处进行，本报告只指出依赖。**§15.8 的 Wave A/B/C 排序不受影响**（三条都是材料获取排序，不是构念排序），但任何以本批 fixture 支持"8 构念必要"的说法都应撤回。
  - **X-7 已补记**（§15.1）：`F001` / `F002` 可运行；`F003` **需 Human 权利裁决**（+ canonical 指针重新定位，属 Architect/Human）。**§15.7 A06 与 §15.5 中以 F003 为载体的格在该裁决前不可执行。**
  - **X-14 已补记**（§15.5 表下）：全表"不存在 / 缺口"改为检索范围陈述；`PARTIAL` 定级不受影响（缺失是真的，本轮只是把它从存在性命题降为检索结果）。
