# 03 — 测量工具与 Proxy 字典

**Status:** `RESEARCH_CANDIDATE`（未审阅） · **As of:** 2026-09-27 · **Lane:** R03（Wave 1）
**Round-3 修订:** R3-A3b（依 `ARCHITECT_ADJUDICATION_V1` / `#30 comment 5854920569`；裁决映射见 `lanes/R3_A3b.md`）

**Scope:** 为 `docs/foundation/PARAMETER_CONVERGENCE_V0_1.md` 的 candidate construct families 调查已验证的量表、item set、行为方法与被动感知方法，产出 proxy dictionary。

> 本文件不是参数表，不冻结任何尺度、权重、阈值或公式。
> 它回答的唯一问题是：**对 LHRM 当前候选构念族，测量学上已经有什么、没有什么，以及现有工具各自能支持与不能支持什么。**
> 所有工具分数都被当作 **proxy** 讨论，不被当作 latent 状态的观测值。

---

## 1. 本文件的读法

### 1.1 四条贯穿全篇的硬规则

1. **不把分数等同于真相。** 每条记录的 `Score is a proxy for` 列写明：该分数实际是哪一类东西的代理，以及它**默认假设了什么**（"关系已存在"？"对方值得被测"？"我的报告不会被反读？"）。
2. **不把 self-report 的分离性当作构念的分离性。** 关系科学的自我报告工具在同一次施测内的亚量表相关经常落在 .38–.58 区间（Fletcher et al. 2000 的 PRQC 数据：trust ↔ satisfaction .58 / commitment .38 / intimacy .47 / love .48，仅 passion .14 可分）。**在自陈通道上无法分离的构念，不等于在理论上无法分离，也不等于在行为/生理通道上无法分离。**
3. **区分"工具没测到"与"工具结构上测不了"。** 后者更严重，单独列于 §4。
4. **区分 trait 工具与 state 工具。** 依恋主流工具（ECR-R 等）在官方指引里就是 trait 语言：*"how you generally experience relationships, not just what is happening in your current relationship"*（Faley 官方量表页）。把它当状态坐标使用是**操作性决定**，不是工具属性。

### 1.2 分类定义（R3-A3b 重写；原四分类表被取代，见 §9 `supersessions` S-03-1）

依 adjudication §C item 6「Search failure/access restriction is not ontology evidence」，本表把**层级不匹配**、**检索不足**、**工具缺陷**、**来源未打开**从 `NOT_IDENTIFIABLE` 中拆出。`NOT_IDENTIFIABLE` 只保留给**有显式结构论证**的情形。

| 分类 | 含义 | 判定前提 |
|---|---|---|
| `DIRECT_PROXY` | 工具在结构上直接测该有向坐标（或该 belief 坐标），且有可查的信效度证据 | 来源已打开 |
| `NOISY_PROXY` | 工具测的是相邻/上位/下位构念，或抽样框/情境与 LHRM 需要错位；可用但必须附限制条件 | 来源已打开 |
| `DERIVED` | 工具测的量必须由多个底层坐标组合才能得到，或工具本身只能给出 pair-level / 派生量 | 来源已打开 |
| `LAYER_MISMATCH` | 工具是 **Agent 层 trait**，或没有 target slot —— 它给出 `Z[k, i, ·]` 而不是 `Z[k, i, j]`。**这不是"结构上测不了"**：它可通过 instrument rewriting 或坐标重述处理，是一个**范围**问题。 | 来源已打开 |
| `SEARCH_INCOMPLETE` | 本 lane 的检索未覆盖到该坐标的合适工具。**"还没人做"不构成任何坐标层判定。** 依 §C item 6，**不得**作为降级依据。 | 显式记录未检索范围 |
| `DEFECTIVE_INSTRUMENT` | 在**正确的 item construction** 下该工具不可用（其前身被判定存在根本测量缺陷）。这是**工具缺陷**，不是坐标层的结构限制。 | 来源已打开 |
| `NOT_ASSESSED` | 来源未打开（`UNVERIFIED_DOI` / `UNVERIFIED` / `AGENT_RECALL`）或原文未读。**本行不发出任何坐标层判定。** | — |
| `NOT_IDENTIFIABLE` | 现有工具**在结构上**无法支撑 LHRM 需要的那个坐标。**仅当本行给出该结构论证、且来源已打开时**才成立。（不因为"还没人做"，而是因为"这样做不了"） | 来源已打开 **且** 有显式结构论证 |

**记账规则（R3-A3b 新增）**：
1. 一行若带 `UNVERIFIED_DOI` / `UNVERIFIED` / `AGENT_RECALL` 标记，其分类列**必须**为 `NOT_ASSESSED`；行内可以补一条 `scope_note`，记录报告自身对层级/抽样框的**自述**，但该自述**不是判定**。
2. 一行若带 `NOT_IDENTIFIABLE`，其 `Score is a proxy for` 列**必须**写出为什么该坐标在本工具上**结构上不可分解/不可得**，而不是"没找到工具"。

---

## 2. 主表：instrument catalogue

**计数口径（R3-A3b 重算；原「41 个独立 instrument family / 54 个可引用条目」不可复现，已被取代，见 §9 `supersessions` S-03-2）**

原句「41 个独立 instrument family / 54 个可引用条目」给出两个数字，但**没有给出计算规则**，且两者都与本表实际行数不符。R3-A3b 重算并显式定义口径：

| 计数项 | 数值 | 口径定义 |
|---|---|---|
| `catalogue_rows` | **73** | §2.1–§2.9 全部表格数据行的行数（`L*` / `R*` / `S*` / `T*` / `A*` / `C*` / `D*` / `O*` / `X*`），**逐行可 grep 复现** |
| `duplicate_or_near_synonym_rows` | **7** | 同一工具 / 同一工具族在别处已有独立行的条目（`X5`=`L1`、`X6`=`L2`、`X7`=`X1` 的分量、`D2`=`D1` 的原始检验、`O8`=`D1` 的子分量、`C4`=`C3` 的两个前身、`O7` 仅经 `O6` 转述） |
| `distinct_instrument_or_family` | **66** | `73 − 7` |
| `non_instrument_evidence_rows` | **9** | 不是可用工具、而是**证据/心理测量旁证**的行（`S8` 通道等价性 meta、`T4` 方向性发现、`T6` trust–distrust 共存、`O6` 谱系审计、`A3` ECR-R 方法效应、`A10` 跨文化非不变性、`A11` 9 量表不变性检验、`X3` satisfaction 信度泛化 meta、`X11` 理论模型） |
| `separately_citable_instrument_entries` | **57** | `66 − 9`。**这是本目录当前唯一有效的"可引用条目"口径。** |
| `NOT_ASSESSED`（R3-A3b 后） | **13** | 来源未打开（`UNVERIFIED_DOI` / `UNVERIFIED` / `AGENT_RECALL`）→ 不发判定。清单见 §2.10 |
| `rows_with_resolvable_pointer` | **≤68** | 本目录**不**再声称全部行都带可解析指针；见 §8 修正与 §9 `supersessions` S-03-5 |

> 短版、修订版、跨文化再验证在**表内**并入母族并以 `(非独立工具)` 标注，但**不因此从 `catalogue_rows` 中删除** —— 这正是原「41/54」不可复现的原因之一。

### 2.1 Liking / Affiliative Valence

| # | Instrument | 引用 | Target | Informant | 方向性 | State/Trait | Time | 信效度与 confounds | Invariance | 分类 | Score is a proxy for / 静默假设 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| L1 | **Inclusion of Other in the Self (IOS) Scale**（单题图示，1–7） | Aron, Aron & Smollan (1992), *JPSP* 63(4):596-612, `10.1037/0022-3514.63.4.596` | perceived interpersonal closeness | self-report，图示单题 | i about j；**但构念近对称 → 拆两方向近似重复计数** | 关系 level（可指任一关系） | 瞬时 | 2 因子模型（Feeling Close / Behaving Close）；alternate-form + test-retest 可靠；minimal social desirability correlation | 2015 PLOS ONE 复检（`10.1371/journal.pone.0129478`）在更异质样本重复原结论 | `NOISY_PROXY` | 代理"自我—他人边界重叠度"，静默假设"重叠 = 亲密"。**唯一有陌生人 dyad 验证的 closeness 工具**（5 项附加研究） |
| L2 | **Relationship Closeness Inventory (RCI)**（Frequency / Diversity / Strength） | Berscheid, Snyder & Omoto (1989), *JPSP* 57(5):792-807, `10.1037/0022-3514.57.5.792` | closeness 三维 | self-report，**75 题**（3 + 38 + 34，见下注） | i about j；同上近对称 | 关系 level，**前提是"你与你最亲近的那段关系"** | 3–5 周稳定（retest total r=.82） | Frequency α=.56 / Diversity α=.81 / Strength α=.90；total α=.62–.66 | 2015 PLOS ONE 复检 RCI total α=.65（Gächter, Starmer & Tufano 2015, `10.1371/journal.pone.0129478`，本 packet 已实际打开原文） | `NOISY_PROXY` | 代理"互动频率 + 多样性 + 影响力"。**R3-A3b 更正**：原表写「10 题」是错的；本工具是 **75 题**的长表（见下方 R3-A3b 注）。**由「10 题」推出的「Frequency 与 Diversity 是弱信度分量」这一派生结论同时撤回**：75 题下 total α 仅 .62–.66 是**表长与计分粒度**的函数（Frequency 3 题被压成 1–10 分、Diversity 38 项被压成 1–10 分），不能直接读成「两个分量本身信度差」。分量级 α 本 packet **未在原文正文中核实**（Gächter et al. 2015 把它们放在 S1 Table）→ `NOT_REVERIFIED_HERE` |
| L3 | **Love Scale 的 Liking 分量** | Rubin (1970), *JPSP* 16:265-273, `10.1037/h0029841`（题名 "Measurement of romantic love"） | liking（与 loving 分离） | self-report | 可依施测指令指向特定 j | 关系 level | 瞬时 | 与 loving 的区分效度历史上被反复质疑；**"Liking 分量"作为独立工具的题数与信度 = `UNVERIFIED`（U19）** | 未见近期不变性证据 | **`NOT_ASSESSED`** | **R3-A3b（依 review-r2 §R-0）**：原判 `NOISY_PROXY`，但其题录**在已标记 `UNVERIFIED` 的同时**仍带坐标层判定 —— 违反新 §1.2 记账规则 1。→ `NOT_ASSESSED`。原行末句「**LHRM `Liking` 最贴近的经典锚点**」保留为**设计线索**（`PLAUSIBLE` 的定位，非工具判定）。**R3-A3b 附一条量化更正（本 packet 已打开 Gächter et al. 2015 原文）**：该文 methods 节记 "The **Liking Scale** and the **Loving Scale** each consist of **13 questions**"，9 点量表，分数区间 13–117 —— 故"题数 `UNVERIFIED`"对 **Liking 分量**一条**已可结**（13 题，9 点），仍 `NOT_REVERIFIED_HERE`（未与 Rubin 1970 原文 Table 1 核对）。 |
| L4 | **PRQC "Closeness" 分量**（3 题） | Fletcher, Simpson & Thomas (2000), *PSPB* 26:340-354, `10.1177/0146167200265007` | closeness（6 个一阶因子之一） | self-report | dyad-level，**归入二阶因子"总体关系质量"** | 关系 level | 瞬时 | 与同施测其他 5 分量共线 | 该 PRQC 在性取向不变性检验中被**列为推荐使用**（Elizabeth & Clark） | `DERIVED` | 代理"总体关系质量中的一个成分"。**结构上被绑进二阶总分，方向性被总分吞掉** |

> **R3-A3b 对 `L2`（RCI）题数的更正与依据** —— 依 review-r2 `R-B13`（`B-C6`/`B-C7` `CONTESTED`）。
>
> - 原表「self-report，**10 题**」是错的。
> - 本 packet 于 2026-09-27 **实际打开** Gächter, Starmer & Tufano (2015), *PLoS ONE* 10(6):e0129478, `10.1371/journal.pone.0129478` 正文（该文是本目录已引用的 2015 复检）。其 methods 节给出的 block 结构为：**Frequency = 3 题**（过去一周与 X 独处的上午/下午/晚上小时数 → 1–10 分）· **Diversity = 38 项活动清单**（勾选计数 → 1–10 分）· **Strength = 34 题**（7 点，理论区间 34–238 → 1–10 分）⇒ **3 + 38 + 34 = 75**。该文并称施测耗时 10–15 分钟。
> - **残留不一致（如实记录）**：同一篇正文在概念段又写 "the RCI is a **69-item** self-report"，与其自身 block 分解（75）不符。本 packet **未打开** BSO (1989) 原文的 Appendix A/B，故 75 这一计数判为 **`PLAUSIBLE`（本 packet 自算，未与原典核对）**，不是 `VERIFIED`。引用题数时**必须带这条限定**。
> - **连带撤回的派生结论**：原表末句「**Frequency 与 Diversity 是弱信度分量，等权入 total 会引入大量不可区分误差**」是从错误的「10 题」读出的。75 题下 total α = .62–.66（BOO 原文 .62 / AAS .66 / 本次复检 .65）应读作**长表被压成三个 1–10 分量后的表长上限**，而不是「两个分量本身信度差」。分量级 α **未在已打开原文正文中出现**（在 S1 Table）→ `NOT_REVERIFIED_HERE`。
> - 附带更正：`Gächter, Starmer & Tufano (2015)` 的作者全名单原标「**作者全名单本次未逐一核对**」（ref 52），本 packet 已由 Crossref + 正文双路确认，可取消该标注。

### 2.2 RomanticAttraction

| # | Instrument | 引用 | Target | Informant | 方向性 | State/Trait | Time | 信效度与 confounds | Invariance | 分类 | Score is a proxy for |
|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | **Passionate Love Scale (PLS)** 15 / 30 题，9 点 | Hatfield & Walther (1978)；心理测量见 Hatfield & Sprecher (1986), *J Adolescence* 9:383-410, `10.1016/S0140-1971(86)80043-4` | passionate love 的认知/情绪/行为/生理成分 | self-report | i about 特定 j，但**含 fallback 指令**：无恋爱对象时改想最近/最近似对象 | 关系 level | 过去/现在 | 官方给出 106–135 等 interpretative 切点 → **存在把连续分隐式分类的诱惑** | 未见跨文化不变性证据 | `NOISY_PROXY` | 代理"认知 + 生理 + 行为成分的合成强度"。**它把 attraction、理想化、生理性唤起、维持身体接近全绑在一起，与 LHRM 的 attraction 单一坐标不同构** |
| R2 | **Triangular Theory of Love Scale (TLS)** | Sternberg (1986), *Psych Review* 93:119-135, `10.1037/0033-295X.93.2.119`；信度与聚合效度见 Chojnacki & Britton (1990), *Psych Reports* 67:219, `10.2466/pr0.67.5.219-224` | intimacy / passion / commitment | self-report | i about j | 关系 level | 瞬时 | **分量间强互相依赖**；Hendrick & Hendrick (1989) 的 5 因子合并解（passionate love / closeness / ambivalence / secure attachment / practicality）经二手转述 | 未见近期不变性证据 | `DERIVED` | 代理"三成分标签的自评匹配"。**分量互相依赖意味着三分不独立；且 commitment 分量与 LHRM `Dedication` 语义重叠** |
| R3 | **PRQC "Romance" / "Passion" 分量** | Fletcher, Simpson, Thomas & Giles (2000)（PRQC 扩展版） | romance（3 题）、passion | self-report | dyad-level | 关系 level | 瞬时 | 与 love 高度共线 | 同 L4 | `DERIVED` | 代理"浪漫/激情作为总体关系质量的成分" |

### 2.3 SexualDesire

| # | Instrument | 引用 | Target | Informant | 方向性 | State/Trait | Time | 信效度与 confounds | Invariance | 分类 | Score is a proxy for |
|---|---|---|---|---|---|---|---|---|---|---|---|
| S1 | **Sexual Desire Inventory (SDI / SDI-2)** 14 题，9 点 | Spector, Carey & Steinberg (1996), *J Sex Marital Therapy* 22(3):175-190, `10.1080/00926239608414655`；三因子重提 Moyano et al. (2017), *J Sex Research* 54(1):105-116, `10.1080/00224499.2015.1109581` | dyadic / solitary sexual desire | self-report | **只有 dyadic 分量指向特定 j**；solitary 与 j 无关 | 回顾 | 过去 1 月 | SDI-1 阶段 **1–5 因子拟合均不佳 → 因子结构是事后修订的**；dyadic α=.86、solitary α=.96 | **本 packet 最强**：Castro-Calvo et al. (2024), *J Sex Research* 63:755-768, `10.1080/00224499.2024.2417023`，**N=82,243 / 42 国 / 26 语言**，三因子 CFI=.980 RMSEA=.060，跨国家、语言、性别、性取向不变性支持 | `NOISY_PROXY` | 代理"月度性欲频率/强度"。**三因子中 2/3 与"特定 j"无关**（attractive-person-related 是对"一个有吸引力的人"的类别化欲望）。工具族"英语主导、以女性为 hegemony"（Cartagena-Ramos et al. 2018, `10.1186/s12874-018-0570-2`） |
| S2 | **Hurlbert Index of Sexual Desire (HISD)** 25 题，0–100 | Apt & Hurlbert (1992), *J Sex Educ Therapy* 18:104-114（**无 DOI**） | general sexual desire | self-report | **报告自述：无特定 target 槽位 → 不能定向** | 泛 trait | 近期 | 13 题反向；简版 Eisert et al. (2026) `10.1007/s10508-026-03487-1`（`UNVERIFIED`，ref 72） | — | **`NOT_ASSESSED`** | **R3-A3b（依 review-r2 §R-0）**：原判 `NOT_IDENTIFIABLE`；来源无 DOI + 简版未核 → 不发判定。`scope_note`（自述，非判定）：该工具给 general sexual desire，**不是"对 j 的欲望"**；其 scope 差异属 `LAYER_MISMATCH`（无 target slot），**不是**结构不可测。 |
| S3 | **Partner-Specific Sexual Liking and Sexual Wanting Scale (PSSLW)** 15 题双因子 | Krishnamurti & Loewenstein (2011), *Arch Sex Behav* 41:467-476, `10.1007/s10508-011-9785-6` | partner-specific **liking**（享乐）vs **wanting**（动机） | self-report | **强 directed：明确针对特定伴侣** | 关系 level | 瞬时/近期 | Study 1 N=1145（63% female）、Study 2 N=67、Study 3 N=2589；PSSL α=.93、PSSW α=.87；重测 n=30 r=.75；CFA CFI=.97 TLI=.96 RMSEA=.06；与 SSI 的相关在男性显著弱于女性 | 未见跨文化不变性证据 | `DIRECT_PROXY` | 代理"对特定 j 的性享乐 vs 性动机"。**它恰好示范了 LHRM 想要的 liking ≠ wanting 分离** |
| S4 | **Global Measure of Sexual Experience (GMSEX)** 5 维双极 | Laurence & Byers (1995)；使用记录见 Impett et al. (2008) `10.1037/0022-3514.94.5.808` | 性经验总体评价（good–bad / pleasant–unpleasant / positive–negative / satisfying–unsatisfying / valuable–worthless） | self-report 双极 | i about j | 关系 level | 近期 | 三样本 α=.92–.94 | 未见跨文化不变性证据 | `DERIVED` | 代理"满意度型读出"，**不是欲望状态**。LHRM 若用它当 SexualDesire 坐标会混淆 desire 与 satisfaction |
| S5 | **Cues for Sexual Desire Scale (CSDS)** 40 题 / 4 因子 | `https://pmc.ncbi.nlm.nih.gov/articles/PMC2861288/`（**DOI `UNVERIFIED`**，ref 67） | 触发性欲的线索类型（Emotional Bonding / Erotic-Explicit / Visual-Proximity / Romantic-Implicit） | self-report | **报告自述：无特定 j；是 cue 类别而非 person-directed** | cue 敏感性 | 常态 | 初始 N=874 + 社区 N=138；筛选 loading>.40、item 间相关>.60 折叠。**本 packet 未打开原文 → 数字 `NOT_REVERIFIED_HERE`** | 未见 | **`NOT_ASSESSED`** | **R3-A3b（依 review-r2 §R-0）**：原判 `NOT_IDENTIFIABLE`；来源 `UNVERIFIED` → 不发判定。`scope_note`（自述，非判定）：它测「什么类型的线索会让我产生欲望」，**不测**「我对 j 的欲望是多少」；其 scope 差异属 `LAYER_MISMATCH`/构念错配，**不是**结构不可测。 |
| S6 | **Female Sexual Desire Questionnaire (FSDQ)** 50 题 / 6 域 + 6 题简版 | Goldhammer & McCabe (2011), *J Sex Med* 8:2512-2521，`https://www.sciencedirect.com/science/article/abs/pii/S1743609515336584` | 性欲的多面体验及影响因素 | self-report | i about 特定伴侣 | 关系 level | 近期 | **发展样本为异性恋 partnered 女性（澳洲为主）→ 性别与文化抽样框限制** | 未见 | `NOISY_PROXY` | 代理"女性视角的性欲生态"。**对 LHRM 的一般 Human Dyad 域，抽样框过窄** |
| S7 | **Decreased Sexual Desire Screener (DSDS)** | Clayton et al. (2009)，经 `10.1007/s13178-024-01040-0` 转述 | 性欲下降的临床筛查 | self-report（临床） | 无特定 j | state | 近期 | 临床量表，非关系状态 | 未见 | `NOISY_PROXY` | 代理"临床困扰"，不是关系状态 |
| S8 | **主观 vs 生殖器唤起一致性 meta 分析**（非量表，而是**测量通道等价性证据**） | Chivers, Seto, Lalumière, Laan & Grimbos (2010), *Arch Sex Behav* 39:5-56, `10.1007/s10508-009-9556-9` | 通道等价性 | self-report vs 生理（VCR / PPG） | — | — | — | **男 r=.66，女 r=.26**；同条件子样本 r=.66 / .44；中等调节：stimulus variability、自评时点 | — | — | **R3-A3b 限定（依 review-r2 `R-0`/`X-14`）**：这是**实验室唤起（laboratory arousal）条件下、self-report 与 genital/PPG 测量之间的一致性**的 scope-limited 发现。原句「不存在性别对称的、由自我报告锚定的性唤起通道」是**一般陈述**，**撤回**。可保留的表述为：**在该 meta 分析所覆盖的实验室唤起范式内**，self-report 与生理测量的相关性在女性样本上显著低于男性样本。**不主张**该结果适用于 LHRM 的 `SexualDesire_(i->j)` 状态坐标本身（自陈欲望 ≠ 唤起），**不主张**它适用于非实验室/自然情境，**不主张**它是领域一般结论。 |

> **R3-A3b 关于 `S8` 保留的行级分层裁决**：本行的**全局层归属**（`S8` 记录的是通道等价性证据，故 §2.3 把它放在 `SexualDesire` 族下作为**旁证**而非工具）**保留不变**。被收窄的只是它派生出的那句一般性断言。依据：adjudication `X-14`（字段级存在性主张须改为检索范围主张）。

### 2.4 Trust

| # | Instrument | 引用 | Target | Informant | 方向性 | State/Trait | Time | 信效度与 confounds | Invariance | 分类 | Score is a proxy for |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T1 | **Trust in Close Relationships Scale (TS)** 17 题 / 3 维，7 点 | Rempel, Holmes & Zanna (1985), *JPSP* 49(1):95-112, `10.1037/0022-3514.49.1.95` | predictability / dependability / faith | self-report | i about j（可平行施测 j） | 关系 level | 现状 | 26 题池 → 17 题，EFA N=47 对；**2025 重做发现一个"含大量反向措辞题项"的因子，Rempel 当年未检验竞争性 4 因子模型**；bifactor 下 faith 题项残余特异性极低 | 2025 重做（N=494, N=847；newly-formed 387 / long-term 460）用 bifactor + invariance 检验，结论支持三分但需修订题项 | `DIRECT_PROXY` | 代理"对 j 的信任水平"。**只能给 level，不能给信任更新事件**；反向措辞方法因子未解决 |
| T2 | **TS 的现代再检验（修订题集）** | `https://pmc.ncbi.nlm.nih.gov/articles/PMC12316384/`（2025） | 同上 | self-report | i about j | 关系 level | 现状 | 明确批评 1985 年"数据与方法低于现代标准" | 对 newly-formed vs long-term 做了 invariance | `DIRECT_PROXY` | 若采用，应使用**该修订题集**而非 Rempel 原题集 |
| T3 | **Dyadic Trust Scale (DTS)** 8 题，7 点 | Larzelere & Huston (1980), *J Marriage Family* 42(3):595-604, `10.2307/351903` | 单维 dyadic trust | self-report | i about j | 关系 level | 现状 | 57 题池（含 Taylor & Altman 1966 亲密信任题池）→ 8 题；item-total r .72–.89；5 题反向；**α=.93；social desirability r=.00 (n.s.)——工具设计中少见的反社会赞许证据**；与泛信任几乎不相关（Wrightsman r=.17，Rotter r=−.02） | 未见跨文化不变性证据 | `DIRECT_PROXY` | 代理"benevolence 为主的可信度判断"。**5 年后独立复核认为它测到的更接近 benevolence 而非 honesty/trust**（Schumm et al. 1985, `10.2466/pr0.1985.56.3.1001`） |
| T4 | **DTS 的关键方向性发现**（非独立工具） | Larzelere & Huston (1980) | — | — | **Female 对 partner 的 love r=.23 (p<.05)；Male 的 r=−.06 (n.s.)** | — | — | 作者解释为"信任在依赖度低的一方（通常为女性）更关键" | — | — | **实测证据：trust 坐标的值本身依赖 i 的 dependence → Trust 与 OutcomeDependence 在测量层纠缠** |
| T5 | **Interpersonal Distrust Scale (IDS)** 15 题 / 3 维，5 点 | Hsu (2019), BGSU 博士论文，`https://stacks.cdc.gov/view/cdc/230061`（**作者本次未核实**，ref 57） | distrust 的 affect / cognition / behavioral intention | self-report | i about target | 关系/工作 level | 现状 | 141 题池 → 15 题；qualitative N=279，评分者一致率 91%→讨论后 100%；三因子 CFA χ²(87)=520.57, RMSEA=.077, CFI=.93, SRMR=.06（一因子 χ²(90)=2273.05, CFI=.70）；AVE>.50；对 interpersonal trust 与 distrust propensity 有 discriminant validity | Study 2 检验了性别间测量不变性 | `NOISY_PROXY` | 代理"对某人的负性预期（情感/认知/行为意向）"。**目标场景是 workplace，不是 close relationship**。*（来源为**非同行评审学位论文**，可引用但强度上限低）* |
| T6 | **trust–distrust 共存证据**（非工具） | Hsu (2019)，同上（**作者本次未核实**） | — | self-report | — | — | — | **279 名被试中 78% 报告曾对同一人同时经历 trust 与 distrust** | — | — | **R3-A3b 降级（依 review-r2 §R-0 / adjudication §C item 6）**：本行原写「为 §4 关于 `Distrust` 是否独立于 `1 − Trust` 的 open question 提供**首个直接经验支持**」。**撤回该派生权重**。理由：(a) 本行是**未读原文的转述**（报告自述「本 packet 不为其编造任何题数、alpha 或结构结论」在上方数行）；(b) 它的抽样框是 **workplace + 抽象定义**，不是关系场景；(c) 它**链自**一个同样未打开的来源 `T7`（见下行）。可保留的表述：本 lane 记录了「trust 与 distrust 可同时存在于同一对象身上」这一**待核实线索**（`CITED_SECONDARY`），场景为工作情境。 |
| T7 | **Interpersonal (dis)trust at work** 8 + 8 题 | Wildman, Thayer, Warren, Fiore & Salas (2025)，`https://exa.ai/library/publication/rchtdhlk6gl`（**`UNVERIFIED_DOI`**） | trust / distrust × competence / intent | self-report | i about target，**双向双轴** | 关系 level | 现状 | trust α=.924 / distrust α=.916；高阶两因子模型（competence / intent 负载于 trust / distrust）优于 Mayer et al. 单维理论模型与 Lewicki et al. 两维模型 | — | **`NOT_ASSESSED`** | **R3-A3b（依 review-r2 §R-0）：来源未打开 → 不发任何坐标层判定。** `scope_note`（报告自述，**非判定**）：该工具的抽样框是 workplace。上方信度与因子结构数字在本 packet **未打开原文**，`NOT_REVERIFIED_HERE`。 |
| T8 | **泛信任量表族（对照项）** | 综述：Wheeler, Ohan, Jackson & Bayliss (2025)，`https://exa.ai/library/publication/g32zr4m06b2`（**`UNVERIFIED_DOI`**） | general trust | self-report | **报告自述：结构上非关系性 → 不能定向** | trait | 常态 | COSMIN 标准评审 25 个工具，**仅 8 个达到全部信度/结构/聚合效度标准**（其中 6 个为成人工具） | 按 COSMIN 评 | **`NOT_ASSESSED`** | **R3-A3b（依 review-r2 §R-0）：来源未打开 → 不发判定。** 原判 `NOT_IDENTIFIABLE` 混淆了「**工具是 general trust（Agent 层 trait，无 j）**」与「**该坐标结构上不可测**」两件事。`scope_note`（自述，非判定）：当 LHRM 需要 Agent 倾向时它是对照项，**不应当作 `Trust_(i->j)`**；该 scope 差异的正确分类是 `LAYER_MISMATCH`，但**在打开来源之前不作此判定**。 |

> **R3-A3b 关于 `T7 → T6 → §4.1` 这条链的裁决（依 review-r2 §R-0 / adjudication §C item 6）**
>
> 原链条：`T7`（`UNVERIFIED_DOI`）→ `T6`（Hsu 2019 学位论文，作者未核实）→ §4.1「D4 `Distrust` **升级为独立候选**，理由从"待测"改为"**78% 共存的直接证据**"」。
>
> 该链条由**两个未打开的来源**串成，其上却挂了一个**canonical 层级的状态转移**（从 open question → 独立 candidate）。这违反 `AGENTS.md` 的 `Human requirement | empirical evidence | model hypothesis | architecture decision | implementation detail` 分离要求：一条**检索未完成**的证据链不能产生架构决定。
>
> **处置**：
> 1. `T7` 分类 → `NOT_ASSESSED`；`T6` 派生权重 → 撤回（见上）。
> 2. §4.1 的 `D4 open question（Distrust）` 建议行 → 由「**升级为独立候选**」改为 **`HOLD_FOR_EVIDENCE`**（依 adjudication **X-4**：`Trust` / `AttachmentSecurity` 保持分离候选，任何 Trust facet 工作须用更窄的语义标签并保持 candidate 状态，直到有 M2 式证据）。
> 3. 复通条件（可复现的退出门槛）：打开 `T7` 与 `T6` 的**一手原文**，并取得至少**一份关系场景**（非 workplace）的 trust–distrust 共存证据，且该证据能区分「`Distrust` 是独立状态」与「`Distrust = 1 − Trust` 的重新编码」。
> 4. **本 packet 不主张** `Distrust` 已是、也不是独立 candidate；亦不主张它不是。

### 2.5 AttachmentSecurity

| # | Instrument | 引用 | Target | Informant | 方向性 | State/Trait | Time | 信效度与 confounds | Invariance | 分类 | Score is a proxy for |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A1 | **Experiences in Close Relationships (ECR)** 36 题 / 2 维，7 点 | Brennan, Clark & Shaver (1998), in *Attachment Theory and Close Relationships* (Guilford, pp. 46-76)；官方摘要 `https://labs.psychology.illinois.edu/~rcfraley/measures/brennan.html` | attachment anxiety / avoidance | self-report | **Agent 层（trait 语言）**；官方允许改写指向特定对象 | trait | 常态 | 482 题池 → 323 题 → 60 子量表 → 12 个 specific-construct 因子 → 2 全局因子；α=.91 / .94 | 意大利版跨 4 组：configural + **partial-metric** + **partial-scalar**（Alessandri et al. 2013） | `NOISY_PROXY` | 代理"一般亲密关系中的被弃焦虑与回避不适"。**官方明示类型学（4 型）不成立，应作连续维度** |
| A2 | **ECR-R** | Fraley, Waller & Brennan (2000), *JPSP* 78(2):350-365, `10.1037/0022-3514.78.2.350`；IRT N=1,085 | 同上，IRT 精化版 | self-report | 同上 | trait | 常态 | 官方评分规则：1–18 anxiety（items 9/11 反向），19–36 avoidance（12 题反向） | 62 文化区（Schmitt et al. 2004, `10.1177/0022022104266105`）；对 gender / relationship status / dyad 内 partner 角色呈 scalar invariance（Brauer & Proyer 2025, `10.1027/1015-5759/a000902`，714 对/1428 人 + 1022 人） | `NOISY_PROXY` | 同 A1 |
| A3 | **ECR-R 的方法效应证据**（非独立工具） | Alessandri et al. (2013)，`https://d.docksci.com/download/...` | — | — | — | — | — | **存在 CMB 方法因子（正/反向措辞）；纳入 CMB 后除精神科组外 anxiety–avoidance 相关被归零**；引 242 研究 meta：合并 r=.20，**ECR .17 vs ECR-R .41** | — | — | **"两维度正交"是工具假象**：工具差异能把 .17 推到 .41 |
| A4 | **ECR-R 心理测量与行为效标** | Fraley, Waller & Shaver (2000), *Assessment*, `10.1177/0146167205276865` | — | self-report | — | trait（但有 diary 效标） | 3 周 | 3 周内 latent attachment **85% shared variance**；解释与伴侣互动中 attachment 情绪的 between-person 方差 30–40%，与家人朋友互动仅 5–15% | — | `NOISY_PROXY` | 提供"ECR-R 与互动层情绪有关"的效标证据 —— **trait 工具少有的行为效标** |
| A5 | **ECR-SF（12 题）** | Wei, Russell, Mallinckrodt & Vogel (2007), *J Personality Assessment* 88(2):187-204, `10.1080/00223890701268041` | 同上，短版 | self-report | 同上 | trait | 1 月重测 .80 / .83 | **2 个实质因子 + 2 个方法因子（正/反向措辞）→ "移除 response set 后"两因子才拟合好**；α .77–.86（anxiety）/ .78–.88（avoidance） | 需修改后才达 scalar invariance（性取向检验） | `NOISY_PROXY` | 同 A1。**其方法因子结构本身就是"反向措辞污染"的教科书案例** |
| A6 | **Relationship Scales Questionnaire (RSQ)** 30 题 / 4 型，5 点 | Griffin & Bartholomew (1994)，工具描述 `https://scales.arabpsychology.com/s/relationship-scales-questionnaire-rsq/`（**`UNVERIFIED_DOI`，U03**） | secure / dismissing / fearful / preoccupied | self-report | **报告自述：Agent 层**；且为**类型学**（Fraley 明确不推荐） | trait | 常态 | secure/dismissing 各 5 题，fearful/preoccupied 各 4 题 | 需修改后才达 scalar invariance（性取向检验） | **`NOT_ASSESSED`** | **R3-A3b（依 review-r2 §R-0）：来源未打开 → 不发判定。** `scope_note`（自述，非判定）：Agent 层 + 类型学（`10.1027/1015-5759/a000902` 路线已指出类型学不成立）。分类若在打开来源后仍成立，应为 `LAYER_MISMATCH`（Agent 层）**叠加** `DEFECTIVE_INSTRUMENT`（类型学），**不是** `NOT_IDENTIFIABLE`。 |
| A7 | **Adult Attachment Scale (AAS)** | Collins & Read (1990)（**`UNVERIFIED_DOI`，U04**）；构成经 Fraley et al. (2000) 转述 | close / depend / anxiety，各 6 题 | self-report | **报告自述：Agent 层** | trait | 常态 | 三分量结构在 IRT 框架下被比较 | 未见近期不变性证据 | **`NOT_ASSESSED`** | **R3-A3b（依 review-r2 §R-0）：来源未打开（原始题录未核实，构成为二手转述）→ 不发判定。** `scope_note`（自述，非判定）：Agent 层；三分量 vs 二维模型之争未解决。 |
| A8 | **Adult Attachment Questionnaire (AAQ)** | Fraley & Shaver (2000), *JPA* 4:150-156（**`UNVERIFIED_DOI`，U05**） | attachment avoidance / anxiety | self-report | **报告自述：Agent 层** | trait | 常态 | N=650 | **仅 partial strong invariance**（vs ECR-R 对 gender 与 relationship status 的 strict factorial invariance） | **`NOT_ASSESSED`** | **R3-A3b（依 review-r2 §R-0）：来源未打开 → 不发判定。** `scope_note`（自述，非判定）：Agent 层；不变性弱于 ECR-R。 |
| A9 | **ECR-R-GSF（20 题，一般关系版）** | Hao, J. et al.（**`UNVERIFIED_DOI`**，ref 62；**年份/卷期/作者全名单未核实**） | 同上，指向**非恋爱**关系 | self-report | 报告自述：Agent 层，但**抽样框扩展到所有亲密关系** | trait | 常态 | 澳洲 n=426 / 中国 n=626；两样本内部一致性良好 | **中国样本 2 因子模型拟合不令人满意；多组 CFA 仅 partial metric，未达 scalar** | **`NOT_ASSESSED`** | **R3-A3b（依 review-r2 §R-0）：来源未打开 → 不发判定。** `scope_note`（自述，非判定）：原表称本行是「LHRM 需要非恋爱关系也能测依恋时唯一方向正确的工具」——该说法**依赖一条未打开的来源**，一并降为待核实线索。（另：原行写「见 §1.4 与 U 列」，但**本文件不存在 §1.4** —— 属内部交叉引用错误，一并修正为指向本表 + §6。） |
| A10 | **ECR-R 跨文化非不变性** | Mastrotheodoros, Chen & Motti-Stefanidi (2015), *EJDP* 12:344-358（**`UNVERIFIED_DOI`，U17**；内容 `CITED_SECONDARY`） | — | — | — | — | — | 中文样本 2 因子结构成立，但用多重检验程序**检出部分参数不满足不变性**（**具体参数 = `UNKNOWN`**） | 部分参数不满足 | — | 边界案例，说明 scalar invariance 不是 ECR-R 的默认状态 |
| A11 | **9 个关系量表跨性取向不变性** | Elizabeth, H. S., & Clark, M. A.（**`UNVERIFIED_DOI`**，ref 60） | 9 个关系相关量表 | self-report | — | — | — | 近乎等量 straight / gay-lesbian / bisexual 样本 | **仅 4 个通过**（Fletcher et al. 2000；Park & MacDonald 2022；Mitchell et al. 2003；Lehmann et al. 2015）；McCroskey et al. (2011) 与 Fraley et al. (2000) 需修改；Gibbons & Buunk (1999) 仅 partial（"urge caution"）；**Cutrona & Russell 与 Hughes et al. (2020) 明确不推荐** | 分组变量 = 性取向 | — | **R3-A3b**：本行**没有坐标层判定**（分类列为 `—`），故不受 §R-0 的 `NOT_ASSESSED` 规则约束；但其**承载的「LHRM 需要的 same-sex 域中只有约一半可用」这一断言是经该未打开来源**。该断言在 §3.4 / §4.3 被再次引用（`S54`），因此在 §3.4、§4.3 两处加 `CITED_SECONDARY (UNVERIFIED_DOI)` 限定。**本 packet 不主张**该 4/9 比例，也不主张其反面。 |
| A12 | **依恋的 state 层日记范式** | Overall & Sibley (2009), *Personal Relationships* 16:239-261, `10.1111/j.1475-6811.2009.01221.x` | 互动中的 attachment 与 dependence 调节 | self-report 日记 | i about j，**互动层** | **state** | 逐次互动 | 本 packet 未读原文，**不附任何数值** | — | `NOISY_PROXY` | **R3-A3b**：这是本目录中**依恋的 state 形态**的既有工具指针（与 §3.2 的缺口登记不冲突 —— 缺口是「无**信任更新**或**欲望更新**的 state 工具」，不是「依恋无 state 工具」）。原 §4.1 写「**唯一** state 指针是 Overall & Sibley (2009)」——**"唯一"经 R3-A3b 新增的 A15（ECR-RS + Fraley et al. 2011）推翻**，见 §2.5 增补与 §9 `supersessions` S-03-4。 |
| A13 | **依恋与日常互动的工作模型** | **Pietromonaco, P. R., & Barrett, L. F. (1997)**, *JPSP* 73(6):1409-1423, `10.1037/0022-3514.73.6.1409`（`CITED_SECONDARY`） | 同上 | self-report 日记 | i about j | state | 逐次互动 | 未读原文 | — | `NOISY_PROXY` | 同 A12。**R3-A3b 引用更正（依 review-r2 `R-B13` / `B-C7`）**：原文与引用列表两处均误作「Pietromonaco & **Laurenceau** (1998)」。本 packet 于 2026-09-27 **直开 Crossref** `10.1037/0022-3514.73.6.1409`：`title` = "Working models of attachment and daily social interactions."；`author` = Pietromonaco, P. R. (first) + **Barrett, L. F.**；`container-title` = *Journal of Personality and Social Psychology*；**volume 73, issue 6, pages 1409-1423**；`published-online` = **1997**。⇒ **年份与第二作者均须改**。 |
| A14 | **同性关系中的依恋与关系功能** | `https://pubmed.ncbi.nlm.nih.gov/23356467/`（**`UNVERIFIED_DOI`**，ref 64） | attachment insecurity ↔ satisfaction / commitment / trust / communication / problem intensity | self-report | **自我与伴侣报告的 attachment 均进入模型** | 关系 level | 现状 | 274 对女性伴侣 + 188 对男性伴侣 + 34 单方女性 + 39 单方男性；模式在男女中相同，男性 couples 效应更强；依恋未调节 minority stress 与关系功能的关联 | — | — | 该设计中"伴侣报告的依恋"已进入解释变量 → 是 directed 化处理的先例。**R3-A3b**：分类列本就为 `—`（无坐标层判定），不受 §R-0 约束；但该行是「partner-report 可得」的**唯一指针**，其 `UNVERIFIED_DOI` 状态须随引用携带。 |

### 2.5a R3-A3b 增补：三项遗漏的已验证工具（**目录增补，非本体变更**）

依 review-r2 `R-B13` 附带的覆盖缺口指认与本 packet 的 Crossref 复核，以下三项**此前缺席**，且**直接反驳**本文件原有的两条"唯一/只有"式断言。**增补它们不改变任何 canonical 构念、层级或坐标。**

| # | Instrument | 引用 | Target | Informant | 方向性 | State/Trait | Time | 信效度与 confounds | Invariance | 分类 | Score is a proxy for / 静默假设 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **A15** | **Experiences in Close Relationships—Relationship Structures Questionnaire (ECR-RS)**，10 题 / 2 维 | **Fraley, R. C., Heffernan, M. E., Vicary, A. M., & Brumbaugh, C. C. (2011).** The experiences in close relationships—Relationship Structures Questionnaire: A method for assessing attachment orientations across relationships. *Psychological Assessment*, 23(3), 615-625. `10.1037/a0022898`（本 packet 2026-09-27 直开 Crossref 确认：题名、4 位作者、卷期页码全部一致） | attachment anxiety / avoidance | self-report | **按关系逐个施测 → 关系特异**（同一受访者可对不同关系分别作答）；报告自述仍含 Agent 层成分 | trait-per-relationship | 现状（**跨关系**，非跨时间） | 10 题短表；**本 packet 未打开全文，不附任何 α、因子拟合或样本量** | **未核实** → `UNKNOWN` | `NOISY_PROXY` | 代理"我对**这一段**关系的依恋取向"。**它证伪了「ECR 族只有 Agent 层 trait 工具」这一前提**：ECR-RS 提供了**关系特异**的施测形态。静默假设：受访者能识别并排序自己的若干段关系；对"依恋"一词的理解不因关系类型而变。 |
| **A16** | **ECR-RS 的跨时间稳定性证据**（非独立工具） | **Fraley, R. C., Vicary, A. M., Brumbaugh, C. C., & Roisman, G. I. (2011).** Patterns of stability in adult attachment: An empirical test of two models of continuity and change. *JPSP*, 101(5), 974-992. `10.1037/a0024150`（本 packet 2026-09-27 直开 Crossref 确认：题名 "Patterns of stability in adult attachment: An empirical test of two models of continuity and change."；4 位作者；**volume 101, pages 974-992**；2011） | 依恋的**跨时间连续性 vs 变化**模式 | self-report（纵向） | 关系特异 | **state/trait 混合问题** | **纵向** | **本 packet 未打开全文，不附任何方差成分、样本量或模型比较结果** | `UNKNOWN` | `NOISY_PROXY` | **这是本文件原 §3.2「没有信任更新或欲望更新的 state 工具」那条缺口的直接反例入口**（对 AttachmentSecurity 而言）。它把「依恋是 trait」从**假设**变成**可检验的竞争模型**（稳定性 vs 变化性）。**本 packet 不主张**哪一种模型成立 —— 那是需要读原文的实证问题（`Fraley et al. 2011` 的判别结果本身即为一个待取的 carrying source）。 |
| **A17** | **Perceived Inclusion Scale (PICS)** | **`NOT_OPENED`** —— 本 packet 于 2026-09-27 在 Crossref 做过 3 次不同检索式（`query.title="Perceived Inclusion Scale"`、`query.bibliographic` 含 `closeness accommodation`、PsycTESTS 域），**均未命中一条可确认的题录**；`psychology.unl.edu` 上的量表页抓取报 transport error。⇒ **本行不携带任何题数、α、因子结构或年份断言。** | 报告自述：被纳入者对"我被包含"的主观感受 | self-report | 报告自述：与 IOS 同族，故**近对称** | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | **`NOT_ASSESSED`** | 列入本目录的**唯一理由**：它被 R3 派工列为三项遗漏工具之一，且 IOS 族在 LHRM 的 `Liking` 候选上只有**单题**工具。**它对 `G9`（双通道）与「IOS 是唯一 closeness 工具」这两条主张的影响，在打开来源之前不成立。** 复通条件：取得一份可解析的原始题录 + 官方量表页，并确认它是 person-directed 还是 pair-directed。 |

> **R3-A3b 对本节增补的效力边界（逐条）**
>
> - `A15` / `A16` **推翻**的两条旧断言：(a) §3.1 类 1 列出的 `ECR` 族全部属「target slot 结构上为空」；(b) §4.1 D5 行「主流工具是 trait；**唯一** state 指针是 Overall & Sibley (2009)」。**纠正方向**是：ECR 族有**关系特异**的施测形态（`A15`），且依恋的**跨时间稳定性是一个已被实证检验的竞争问题**（`A16`），不是被假定为 trait 后就不再问。
> - `A15` / `A16` **不**推翻 §3.2 的缺口登记本身：缺口说的是「**没有**"信任更新"或"欲望更新"的 state 工具」，`A16` 属于**依恋**族，不是信任或欲望。**本 packet 不主张** A16 使信任/欲望的 state 缺口消失。
> - `A15` / `A16` **不改变** §4.1 D5 的建议标记（仍为 `KEEP` + 标注），也**不构成** canonical §2.6 的删除/合并判据（C-P1 明确：`MAPPING_FAILURE` 是待诊断事件，不是自动本体拒绝）。
> - `A17` **不推翻任何东西**。它是一个 `NOT_ASSESSED` 占位行。
> - 本节全部为**目录增补**。依 adjudication **X-3**（D7 保持 directed-state candidate）、**X-4**（Trust/AttachmentSecurity 保持分离）、**X-1**（PPR 属 BeliefState、Satisfaction 属 Derived）—— 本节**不触及**这些已裁定的层归属。

### 2.6 Caregiving

| # | Instrument | 引用 | Target | Informant | 方向性 | State/Trait | Time | 信效度与 confounds | Invariance | 分类 | Score is a proxy for |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C1 | **Volunteer Functions Inventory (VFI)** 30 题 / 6 功能，7 点 | Clary, Snyder, Ridge, Copeland, Stukas, Haugen & Miene (1998), *JPSP* 74(6):1516-1530, `10.1037/0022-3514.74.6.1516` | values / understanding / career / social / protective / enhancement | self-report | **无特定 j；被测者是志愿者，目标是公益服务** | 动机 trait-like | 常态 | N=321F/144M/2；principal components 6 个 eigenvalue>1.0；6 因子 principal-axis 结构"近乎完美干净"；各动机之间只中度相关（这本身是好性质） | 未见跨文化不变性证据 | `NOISY_PROXY` | 代理"我从志愿服务中获得什么心理功能"。**`understanding` 与 `protective` 可勉强借作 caregiving 动机的类比，但抽样框（志愿者）与 LHRM 需要的（对特定 j）差距过大** |
| C2 | **Caregiver Motivation Scale (CMS)** 13 题 / 2 因子 | Wang, Yang, Cary & Hendrix (2025), *Innovation in Aging*，`https://pmc.ncbi.nlm.nih.gov/articles/PMC12761549/` | **intrinsic motivation (9 题) / obligatory motivation (4 题)** | self-report | i about 被照护者（**家庭照护者情境**） | 动机 state-ish | 常态 | 227 名家庭照护者；concept analysis + 20 人访谈 + 4 人专家组；S-CVI=1、α=.764、MSA=.875、RMSR=.046；收敛效度用 Old Caregiver Motive Scale，区分效度用 Caregiver Preparedness Scale；作者明说需 longitudinal 与更广照护人群检验 | 未见 | `NOISY_PROXY` | **本 packet 中因子结构最贴近 LHRM `D6` 的工具**：intrinsic ≈ Caregiving 状态，obligatory ≈ 约束/义务。**但抽样框是"慢性病/残障家庭照护者"** |
| C3 | **Relational Maintenance Behavior Measure (RMBM)** 26 题 / 7 因子 | Stafford (2010), *J Social Personal Relationships* 28(2):278-303, `10.1177/0265407510378125` | positivity / understanding / self-disclosure / relationship talks / assurances / tasks / networks | self-report **行为** | i about j（各报自己的行为）→ **可定向** | **行为，不是状态** | 现状 | **作者明说被取代的两个前代 RMSM 存在 "fundamental measurement flaws"，在正确 item construction 下均不可用**；RMBM 因子结构在 3 样本间稳定；3 样本主要为白人已婚者/伴侣 | 未见 | `DIRECT_PROXY`（对 `Action/Observation` 层） | 代理"我为维持关系做了哪些事"。**与 `PARAMETER_CONVERGENCE_V0_1.md` §8 把照护行为降级为 Action/Observation 完全一致 —— 本 packet 支持该降级** |
| C4 | **Relational Maintenance Strategies Measure (RMSM)** 5 因子 / 修订 7 因子 | Stafford & Canary (1991)；Stafford, Dainton & Haas (2000) | — | self-report 行为 | 同上 | 行为 | 现状 | **被 Stafford (2010) 判定为存在根本测量缺陷，不推荐使用** | — | **`DEFECTIVE_INSTRUMENT`** | **R3-A3b 重新分类（依 review-r2 `B` top_rec / §R-0）**：原判 `NOT_IDENTIFIABLE` 的理由是「被判定为存在根本测量缺陷」—— 那是**量表题项构造缺陷**，不是 `OutcomeDependence`/`Caregiving` 坐标层的**结构上不可测**。新分类 `DEFECTIVE_INSTRUMENT` 只表示**在正确 item construction 下该工具不可用**，**不**对任何 LHRM 坐标作判定。保留在表中的唯一目的是记录"**不要用它**"。另：S34（Stafford 2010）在本文件 §3.3 的 confound 行已由「求值者/施测者效应」**移至「量表题项的语义溢出/构造缺陷」**行，见 §3.3。 |
| C5 | **Perceived Responses to Capitalization Attempts** | Gable, Reis, Impett & Asher (2004), *JPSP* 87(2):228-245, `10.1037/0022-3514.87.2.228` | 伴侣对"分享好消息"的回应 | self-report（**行为 + 被感知行为**） | i about j（我感知 j 的回应）→ **可定向** | 事件层 | 逐事件 | 正/负关系事件清单（9 + 9 项）在 Impett et al. (2008) 的日记中被实际使用 | — | `DIRECT_PROXY` | 代理"积极事件被如何回应"。**这是把 PPR 的行为侧做成可编码事件清单的既有范式，与 LHRM 的 Action/Event + Belief 分离相容** |
| C6 | **Compassionate Love for a Partner Scale** | Beatson, Dickson, van Dellen & Vatcher (2008), *JPSP* 95(5)（**`UNVERIFIED_DOI`，U07**）；量表存在性侧证：Winczewski, Bowen & Collins (2014) `10.1037/e512142015-146`、Neto (2012) `10.5964/ijpr.v6i1.88` | 对伴侣的 compassionate love | self-report | i about j | 关系 level | 现状 | **原始题录未核实 → 不附任何题数、alpha 或结构结论** | 未见 | `NOISY_PROXY` | **概念上最贴近 `Caregiving_(i->j)`**（是关切/慈悲的关系倾向，不是照护行为、不是照护情境）。但本 packet 不能为其背书任何心理测量细节 |
| C7 | **Multidimensional Valid Profile (MVP)** 15 题 | Fawcett et al. (2013)，经 Adler & Baeder (2021) 转述，`https://www.alabamamarriage.org/assets/uploads/2023/03/Family-Relations-2021-Adler-Baeder-...pdf` | admiration / understanding / sacrifice / generosity / fairness | self-report | i about j | 关系 level | 现状 | **Adler & Baeder 指出 MVP 多数题项实为"伴侣的行为"评估**，更像 relational skills 实践量表 | — | `NOISY_PROXY` | 代理"伴侣在关系实践上的 5 种表现" |

### 2.7 Dedication

| # | Instrument | 引用 | Target | Informant | 方向性 | State/Trait | Time | 信效度与 confounds | Invariance | 分类 | Score is a proxy for |
|---|---|---|---|---|---|---|---|---|---|---|---|
| D1 | **Investment Model Scale (IMS)**：commitment level / satisfaction / quality of alternatives / investment size | Rusbult, Martz & Agnew (1998), *Personal Relationships* 5(4):357-387, `10.1111/j.1475-6811.1998.tb00177.x` | 四成分 | self-report | i about 该关系 | 关系 level | 现状 | 3 研究、good internal consistency、4 个独立因子；与 dyadic adjustment / trust / IOS 中度相关而与个人倾向基本无关；**Study 3 中早期 IMS 预测后期 DAS 与关系存续** | 未见跨文化不变性证据 | `DERIVED` | 代理"**一个把 satisfaction、替代选项、投资规模合成的复合分**"。**定义层即合并了 LHRM 想分离的 dedication / outcome dependence / constraint** |
| D2 | **IMS 的原始检验** | Rusbult (1980), *JESP* 16:172-186, `10.1016/0022-1031(80)90007-4` | commitment / satisfaction | self-report | i about 该关系 | 关系 level | 现状 | **commitment 对 relationship costs 的效应很弱；investment size 与 alternatives 才是主因** | — | `DERIVED` | 同 D1；进一步说明"投入/替代"而非"意愿"驱动 commitment |
| D3 | **Willingness to Communicate (WTC) Trait Form** 12 计分题 | McCroskey (1985)，ERIC ED265604 `https://files.eric.ed.gov/fulltext/ED265604.pdf` | 跨情境/跨接收者的沟通意愿 | self-report | **报告自述：i about 一般接收者；无特定 j** | trait | 常态 | α=.92；分情境 α=.65–.76、分接收者 α=.74–.82；因子分析单维；**原文自承 WTC 只是实际行为的中等预测因子**（与 VAS 相关 r=.41） | — | **`LAYER_MISMATCH`** | **R3-A3b 重新分类（依 adjudication §C item 6）**：原判 `NOT_IDENTIFIABLE`。但该行**自己的说明**写的是「无特定 j」+ trait —— 这是**Agent 层 scope 错配**（给 `Z[k,i,·]` 而非 `Z[k,i,j]`），**不是**「该坐标结构上无法观测」。按新 §1.2 vocab 应为 `LAYER_MISMATCH`。**结构不可测的主张在 `WTC-Trait` 上不成立。** |
| D4 | **Close Willingness to Communicate (CWTC)** | MacCallum, Matuschka, Coulson, Lock & Robins (2001), *JPSP* 81(3):505-514（**`AGENT_RECALL`，U09**） | 对伴侣的沟通意愿 | self-report | i about j | 关系 level | 现状 | **本 packet 不附任何数值结论** | — | **`NOT_ASSESSED`** | **R3-A3b（依 review-r2 §R-0）：题录为 `AGENT_RECALL`（凭记忆写出的年份/卷期/页码）→ 不发判定。** 概念上是 Dedication 的行为化代理候选，但**只作为待核线索**；本 packet 不为其背书任何题数、版本或信度。 |
| D5 | **Affective Commitment Mechanisms（identity theory 系）** | Stets & Burke (2000)（**`AGENT_RECALL`，U12**） | affective commitment 的机制 | self-report | i about 关系身份 | — | — | 未核实 | — | `NOT_ASSESSED` | 保留为"identity theory 系的 commitment 测量"这一**存在性线索**。**本 packet 不主张**该工具存在、不主张其形态；仅记录这是一个待取证的检索方向。 |

> **R3-A3b 关于 `D3` 的效力边界**：`LAYER_MISMATCH` 判定**只**说明"`WTC-Trait` 是 Agent 层工具"这一 scope 事实。它**不**主张 Dedication（`D7`）在测量学上可得或不可得 —— 后者是 §4.1 的独立问题，且按 adjudication **X-3**，`Dedication` **保持 directed-state candidate**，本文件**不**对其作降级建议。

### 2.8 OutcomeDependence

| # | Instrument | 引用 | Target | Informant | 方向性 | State/Trait | Time | 信效度与 confounds | Invariance | 分类 | Score is a proxy for |
|---|---|---|---|---|---|---|---|---|---|---|---|
| O1 | **Relationship Power Inventory (RPI)** | **Farrell, A. K., Simpson, J. A., & Rothman, A. J. (2015)**, *Personal Relationships* 22(3):387-413, `10.1111/pere.12072` | 控制过程 / 控制结果 / 双向性 | self-report | **双向双轴：自我权力 + 感知对方权力** | 关系 level | 现状 | **Study 3 revealed RPI scores predict observer ratings of power during decision-making discussions and showed the RPI has good test–retest reliability**（本 packet 已打开 Crossref abstract 逐字核对）；**R3-A3b 未打开全文，题数/分量表/α 未核实** | 未见 → `UNKNOWN` | `NOISY_PROXY` | 代理"我能多大程度影响决策"。**是权力，不是依赖。** **R3-A3b 引用更正（依 review-r2 `R-B13` / `B-C6`）**：原文与 ref 25 两处均误作「**Beach (2017)**」。本 packet 2026-09-27 **直开 Crossref** `10.1111/pere.12072`：`author` = **FARRELL, ALLISON K. (first) / SIMPSON, JEFFRY A. / ROTHMAN, ALEXANDER J.**，三人均 University of Minnesota；`container-title` = *Personal Relationships*；**volume 22, issue 3, pages 387-413**；`published-online` = **2015-03-26**。⇒ **作者、年份、卷期页码三项均须改。** |
| O2 | **Relationship Balance Assessment (RBA)** 35 题 / 12 因子 | **Luttrell, T. B., Distelberg, B., Wilson, C., Knudson-Martin, C., & Moline, M. (2017)**, *Contemporary Family Therapy* 40(1):10-27, `10.1007/s10591-017-9421-2` | Time Discretion / Relational / Emotional Power（Expression & Avoidance）/ Accommodation / Spending & Saving / Union or Sexual Dominance / Rational / Economic Role（Status & Childcare）/ Social | self-report，**双方在同一连续体作答** | **真正 dyadic：要求比较两人知觉** | 关系 level | 现状 | EFA on 268 individuals + 91 couples；**作者警告："Equal" 置中评分无法区分"双方都同等投入"与"双方都同等退出"**；也警告"取双方平均会掩盖预测冲突的知觉差异"。**R3-A3b**：题数 35、因子 12、样本 268/91 与 EFA 细节**本 packet 未打开全文** → `NOT_REVERIFIED_HERE` | 未见 → `UNKNOWN` | `NOISY_PROXY` | 代理"12 个领域上的相对平衡"。**它自己暴露了 LHRM 必须区分的 outcome dependence vs disengagement 混淆。** **R3-A3b 引用更正（依 review-r2 `R-B13` / `B-C6`）**：原文与 ref 26 两处均误作「**Lativos et al. (2017)**」。本 packet 2026-09-27 **直开 Crossref** `10.1007/s10591-017-9421-2`：`author` = **Luttrell, Thomas B. (first) / Distelberg, Brian / Wilson, Colwick / Knudson-Martin, Carmen / Moline, Mary**；`title` = "Exploring the Relationship Balance Assessment"；`container-title` = *Contemporary Family Therapy*；**volume 40, issue 1, pages 10-27**；`published-online` = 2017-07-20 / print 2018-03。⇒ **姓氏须改（`Lativos` → `Luttrell`）**；ref 26 原注「**作者全名单本次未逐一核对**」可取消。 |
| O3 | **3 Vector Dependency Inventory (3VDI)** | Pincus & Gurtman (1995)；Pincus & Wilson (2001), *J Personality* 69(2):223-251, `10.1111/1467-6494.00143` | submissive / exploitable / love 三个依赖向量 | self-report | **报告自述：Agent 层** | trait | 常态 | 两个大样本（N=921, N=472）因子验证；**love dependence 与安全依恋、parent affiliation 正相关，与病理性依恋负相关 → 依赖有适应性维度** | 未见 | **`LAYER_MISMATCH`** | 代理"我这一型的依赖"。**R3-A3b 重新分类**：原判 `NOT_IDENTIFIABLE`，但该行自己的说明是「**不是"我依赖 j"**」+ Agent 层 = **层级/靶位错配**，不是结构不可测。**结构不可测的主张在 3VDI 上不成立。** |
| O4 | **Interpersonal Dependency Inventory** 48 题 | Hirshfeld, Klerman, Gouch, Barrett, Korchin & Chodoff (1976), *J Personality Assessment* 40(6):610-618, `10.1207/s15327752jpa4106_6` | emotional reliance on another / lack of social self-confidence / assertion of autonomy | self-report | **报告自述：Agent 层** | trait | 常态 | 220 正常 + 180 患者 + 两批交叉验证；**原文即称既有自评清单"没有一个能充分评估人际依赖"** | 未见 | **`LAYER_MISMATCH`** | 同 O3。**R3-A3b 重新分类**：层级错配，非结构不可测。 |
| O5 | **Personal Sense of Power Scale** | Anderson, John & Keltner (2012), *J Personality* 80(2):313-344, `10.1111/j.1467-6494.2011.00734.x` | 个人权力感 | self-report | **报告自述：Agent 层** | trait | 常态 | — | — | **`LAYER_MISMATCH`** | 代理"我通常多有力量感"。**R3-A3b 重新分类**：原判 `NOT_IDENTIFIABLE`，但其说明是「**不是"我依赖 j"**」+ Agent 层 = 层级错配。另注：这是**权力感**（Agent 层），与 `OutcomeDependence` 是不同构念 —— 即便层级对齐也不构成该坐标的工具。 |
| O6 | **关系权力测量谱系的权威审计**（非工具） | `10.1111/jftr.70019`（*J Family Theory & Review*；**作者全名单本次未逐一核对**，ref 50） | — | — | — | — | — | **R3-A3b 逐项降级为 `HOLD_FOR_EVIDENCE`**：该审计被本文件用来支撑一个**具体数字** —— 「**38 个有名有姓的 power/equity/balance 量表各自仅被用 1–2 次，无一成为主流工具**」。本 packet 于 2026-09-27 **未打开**该文（仅持有 DOI 与本文件既有的转述），因此：**38** 这个数、**1–2 次** 这个使用频次、以及**"无一成为主流"** 这个全称否定，**全部**标 `HOLD_FOR_EVIDENCE`。依 adjudication **X-14**，`无一成为主流` 是**字段级存在性否定**，即使核实为真也只能表述为「该审计所覆盖的范围内未发现主流工具」。可保留的：**方法学警示**方向 —— 作者明确说「经常有人用一个 dependence scale 去研究 power」并警告「难以确定研究结果是否真的反映同一底层构念」。 | 谱系审计 | — | **方法学警示 = PLAUSIBLE（方向可辩护，数字未核）**。**`38` / `1–2` / `无一` 三个具体数字 = `HOLD_FOR_EVIDENCE`。** |
| O7 | **Sexual Relationship Power Scale (SRPS)** | 经 `10.1111/jftr.70019` 转述（Emerson 1991 / Anderson et al. 2002） | 性关系中的控制与决策支配 | self-report | i about j | 关系 level | 现状 | 谱系审计指出它是**最常用的性权力工具**，但"因在 HIV/AIDS 特定情境中开发，不应视为一般关系权力动态的评估" | 谱系审计指出其样本在种族/族裔/国籍上最异质 | `NOISY_PROXY` | 代理"性关系中的控制感"。**结论域被原作者明确限定** |
| O8 | **IMS 的 quality of alternatives + investment size** | Rusbult, Martz & Agnew (1998)，`10.1111/j.1475-6811.1998.tb00177.x` | 关系外的替代选项质量；对关系的投入规模 | self-report | **i about 该关系 vs 关系外选项** | 关系 level | 现状 | 见 D1 | — | `NOISY_PROXY` | **目前最接近 `OutcomeDependence_(i->j)` 的现成读出**。但 `alternatives` 测的是"**该关系之外**的选项"，不是"j 对我结果的控制力"；`investment` 测的是"已投入"，不是"依赖" |

### 2.9 Contested — Distrust / Satisfaction / Cohesion / PPR

| # | Instrument | 引用 | Target | Informant | 方向性 | State/Trait | Time | 信效度与 confounds | Invariance | 分类 | Score is a proxy for |
|---|---|---|---|---|---|---|---|---|---|---|---|
| X1 | **Dyadic Adjustment Scale (DAS)** 32 题 / 4 因子 | Spanier (1976), *J Marriage Family* 38(1):15-28, `10.2307/350547` | dyadic satisfaction / cohesion / consensus / affectional expression | self-report | **dyad-level**（可建成两方向但设计上不是） | 关系 level | 现状 | 作者自承"若干方法学问题留待未来研究" | **信度泛化：91 篇研究 / 128 样本 / 25,035 人；total 与 Cohesion/Consensus/Satisfaction 内部一致性可接受但低于原报告；Affective Expression 分量 alpha 差；reliability 不因 sexual orientation / gender / marital status / ethnicity 而异**（`10.1111/j.1741-3737.2006.00284.x`） | `DERIVED` | 代理"婚姻/同居关系的总体适配"。**它把 satisfaction 混在 adjustment 里，与 LHRM `Satisfaction = DERIVED` 的判定同向** |
| X2 | **Relationship Satisfaction Scale (RS10 / RS5)** | Røysamb, Vittersø & Tambs (2014), *Norsk Epidemiologi* 24:187-194，`https://www.ntnu.no/ojs/index.php/norepid/article/view/1821/1818` | 单维 global relationship satisfaction | self-report | dyad-level | 关系 level | 现状 | **MoBa N=117,178 + QUSF N=347**；单因子模型拟合良好；与 QMI 高相关、与 SWLS 中等相关；预测未来分手 | **跨性别 measurement invariance 成立**（CFI 差 <.01） | `DERIVED` | 代理"对关系的总体评价"。**大规模人口样本 + 跨性别不变性 → LHRM 若要一个 satisfaction 读出，这是最可靠的单一选择** |
| X3 | **关系满意度的信度泛化 meta**（非工具） | Graham, Diebels & Barnow (2011), *J Family Psychology* 25(1):39-48, `10.1037/a0022441` | LWMAT / KMS / QMI / RAS / MOQ / Karney & Bradbury semantic differential / CSI | self-report | dyad-level | 关系 level | 现状 | **639 个信度系数 / 398 篇文章 / 636,806 人；KMS 最强、LWMAT 最弱**；强调 reliability invariance 是跨群比较的前提 | 逐工具 | `DERIVED` | **提供"哪一个 satisfaction 工具更值得信"的排序证据；也是 LHRM 不能随手挑一个 satisfaction 尺的原因** |
| X4 | **Couple Relationship Satisfaction Scale (CRSS)** | *Does Relationship Satisfaction Always Mean Satisfaction? Development of the Couple Relationship Satisfaction Scale*, *J Relationships Research*，`https://www.cambridge.org/core/journals/journal-of-relationships-research/article/abs/does-relationship-satisfaction-always-mean-satisfaction-...`（**`UNVERIFIED_DOI`**，ref 69；年份/卷期未核实） | 把 relationship quality 与 satisfaction 语义分离的 satisfaction | self-report | dyad-level | 关系 level | 现状 | 两因子结构（n=372 / n=1,185）；收敛/区分/known-groups 效度。**R3-A3b：未打开原文 → 数字 `NOT_REVERIFIED_HERE`** | — | **`NOT_ASSESSED`** | **R3-A3b（依 review-r2 §R-0）：来源未打开 → 不发判定。** `scope_note`（自述，非判定）：原表称它「概念上最接近 LHRM 对 `Satisfaction` 的界定」。**该定位本身不需要打开全文即可保留为一条待核实的设计线索**，但它**不构成**一个可引用的工具判定。 |
| X5 | **IOS**（作为 Cohesion 工具） | 同 L1 | we-ness / closeness | self-report 图示单题 | i about **pair** | 关系 level | 瞬时 | 单题；正题 ceiling 类问题（PRI 论文对同类正题的观察） | 2015 PLOS ONE 复检 | `NOISY_PROXY` | 代理"A 对 pair 的 closeness 感知"。**不能裁决"A 比 B 更 cohesive"** |
| X6 | **RCI**（作为 Cohesion 工具） | 同 L2 | 互动频率/多样性/影响力 | self-report | i about pair | 关系 level | 3–5 周 | Frequency α=.56 | 2015 PLOS ONE 复检 | `NOISY_PROXY` | 同 X5 |
| X7 | **DAS 的 dyadic cohesion 分量** | 同 X1 | dyadic cohesion | self-report | dyad-level | 关系 level | 现状 | 信度低于 Spanier 原报告 | 信度泛化 | `DERIVED` | 同上 |
| X8 | **人际自主生理同步（ANS synchrony）** | Mayo, Lavidor & Gordon (2021), *Physiol Behav* 235:113391, `10.1016/j.physbeh.2021.113391`；综述 **Palumbo, R. V., Marraccini, M. E., Weyandt, L. L., Wilder-Smith, O., McGee, H. A., Liu, S., & Goodwin, M. S. (2017)**, *Personality and Social Psychology Review* 21(2):99-141, `10.1177/1088868316628405`；Nature Rev Psych (2026) `10.1038/s44159-026-00535-4` | 自主神经活动的跨时间协调 | **physiological / wearable，双人同步记录** | **结构上不可分解为 i→j 与 j→i**（本身是两信号的耦合/互相关） | 瞬时（需数分钟共同记录） | 逐次互动 | **关系结局总体 ES=.09（边缘显著），I²=76.0%；交感 ES=+0.19 (p=.02)，副交感 ES=−0.21 (p=.03)，合并 ES=+0.16**；2026 年综述称"其心理意义仍然含糊"；Gates et al. (2015) 发现 couples' RSA 同步与自报婚姻冲突**正**相关；Thomsen & Gilbert (1998) 冲突讨论中 SC 同步个体差异大。**引用约束（review-r2 R-F1）：引用这组数字时必须同时带 `I²=76%`** | 不适用（非自陈量表） | `NOT_IDENTIFIABLE` | **不能作为 Cohesion / Care / Trust 的 proxy。** 方向矛盾 + 高异质 + 综述明说含糊。**R3-A3b 对本行分类的依据（新增，按 §1.2 记账规则 2 显式写出结构论证）**：判 `NOT_IDENTIFIABLE` 的**唯一**成立理由是**结构论证** —— 「两信号的耦合/互相关**本身不含方向性信息**；分解为 i→j 与 j→i 需要额外的、可争议的假设（如"谁跟随谁"）」。**与结局关联弱（ES=.09）、I²=76%、方向矛盾**这三条是**另一类证据**（效应证据），**不是**结构论证的依据；它们支持的是"不可作 proxy"，不支撑"不可分解"。两者不得混用。**R3-A3b 引用更正（依 review-r2 `R-B13` / `B-C7`）**：原文与 ref 42 两处均误作「**Mønster et al. (2016)**」/「*Soc Personal Relat*」。本 packet 2026-09-27 **直开 Crossref** `10.1177/1088868316628405`：`author` = **Palumbo, Richard V. (first) / Marraccini, Marisa E. / Weyandt, Lisa L. / Wilder-Smith, Oliver / McGee, Heather A. / Liu, Siwei / Goodwin, Matthew S.**；`title` = "Interpersonal Autonomic Physiology: A Systematic Review of the Literature"；`container-title` = **Personality and Social Psychology Review**（**不是** *Soc Personal Relat*）；**volume 21, issue 2, pages 99-141**；online 2016-02-26 / print 2017-05。⇒ **作者、年份、期刊、卷期页码四项均须改**。ref 42 原注「**作者全名单本次未逐一核对**」可取消。 |

| X9 | **Perceived Responsiveness and Insensitivity Scale (PRI-16 / PRI-8)** | Crasta, Rogge, Maniaci & Reis (2021), *Psychological Assessment*，`10.1037/pas0000986` | responsiveness / insensitivity | self-report | **强 directed：i 感知 j 的 responsiveness**；**Study 3 APIM 显示 i 的 PRI 与 j 的自报行为相关** | 关系 level（**对短期变化敏感**） | 每两周 × 8 周 | item pool = 19 量表 246 题，N=2,334；PRI-8 R α=.93 ω_WP=.83，I α=.88 ω_WP=.77；对 CSI-16 有 incremental validity；**caring 题项因与 global satisfaction 交叉负荷被剔除**；**正题 ceiling 低，均值 +1.5SD 以上区分力差** | 检验了性别组不变性 | `DIRECT_PROXY` | 代理"**我感到** j 理解并重视我"。**绝不能推断 j 的客观 responsiveness** |
| X10 | **Perceived Partner Responsiveness Scale (PPRS)** 18 题 / 12 题版 | Reis, Clark & Holmes et al. (2018) 手册章节，`https://www.sas.rochester.edu/psy/people/faculty/reis_harry/assets/pdf/reisetal_2018_pprs.pdf` | understanding + validation | self-report，9 点锚定 | i about j | 关系 level | 现状 | consistencies .91–.98（多数样本）；12 题版源自 Reis, Maniaci, Caprariello, Eastwick & Finkel (2011)，18 题版源自 Birnbaum & Reis (2006) | — | `DIRECT_PROXY` | 同 X9 |
| X11 | **Reis & Shaver (1988) 亲密过程模型** | in Duck (Ed.), *Handbook of Personal Relationships*, pp. 367-389；2018 重印 `10.4324/9780203732496-5` | self-disclosure + partner responsiveness → intimacy | 理论 / 操作化 | i about j | **state（互动层）** | 逐次互动 | — | — | — | 提供 PPR 的理论定义。**其"行为响应 vs 感知响应"的区分是 LHRM §5 B1 架构判断的证据支持** |
| X12 | **互动层 PPR 的实际测量形态** | Laurenceau, Barrett & Pietromonaco (1998), *JPSP* 74(5):1238-1251, `10.1037/0022-3514.74.5.1238` | 互动中感知到的 accepted / understood / cared for | self-report diary | i about j | **state，逐次互动** | 事件后即时（event-contingent diary，1–2 周） | **Study 1 的 PPR 只有 1 题（felt accepted），Study 2 只有 3 题** → 互动层 PPR 在文献中本就是极简测量 | — | `DIRECT_PROXY` | 代理"在这一次互动中我感到被接受/被理解/被关心" |
| X13 | **数字轨迹（短信）** | Brinberg, Vanderbilt, Solomon, Brinberg & Ram (2021), *JSPR* 38(12):3429-3450, `10.1177/02654075211028654` | 短信行为的跨人分布与时序 | **passive sensing / mobile data donation** | **可按 sender/receiver 分解 → 方向性可得** | 行为/过程 | 逐条消息 | 41 对大学年龄伴侣、**1,000,000+ 条短信**、关系建立前 + 关系转变期；**作者结论含"需要更多关于不同沟通行为如何/为何随关系发展的理论特异性"** | 不适用 | `DIRECT_PROXY`（对 Action/Event 层） | 代理"谁在什么时候向谁发了什么"。**其自身结论即说明：目前没有理论把 trace 映射到关系构念** |
| X14 | **Romantic Beliefs Scale** | Sprecher & Metts (1989), *J Social Clinical Psychology* 6(4)，`10.1177/0265407589064001` | Love Finds a Way / One and Only / Idealization / Love at First Sight | self-report | **报告自述：Agent 层：浪漫主义意识形态** | trait | 常态 | N=730；与 gender 与 gender-role orientation 相关 | — | **`LAYER_MISMATCH`** | **反面教材**：它测的是"对文化脚本的态度"，与关系状态无关。**R3-A3b 重新分类**：原判 `NOT_IDENTIFIABLE`；但其自身说明就是「Agent 层 + 规范态度」= **层级错配**，不是结构不可测。分类改为 `LAYER_MISMATCH` 后，**它的教学价值不变**：LHRM 处理"真爱""门当户对"等高层标签时应明确拒绝此类工具。**注意**：依 adjudication **X-1**，Satisfaction 保持 `Derived` / evaluation-state candidate，`PPR` 保持 BeliefState —— 本行不触及该已裁定层归属。 |
| X15 | **Reiss Premarital Sexual Permissiveness Scale (RPS)** | Reiss (1964), *J Marriage Family* 26(2):188, `10.2307/349726`；修订版 Sprecher, McKinney, Walsh & Anderson (1988), `10.2307/352650` | 婚前性行为许可规范 | self-report | **报告自述：Agent 层：规范态度** | trait | 常态 | Reiss et al. (1989) 与 Sprecher (1989) 的公开争论即针对修订版是否仍是 RPS | — | **`LAYER_MISMATCH`** | 同 X14：文化脚本态度。**R3-A3b 重新分类**：层级错配，非结构不可测。 |
| X16 | **Companionate Love Scale** | 数据集记录 `10.13072/midss.484`（**作者字段为空 → 原始出处 `UNKNOWN`，U20**） | companionate love | self-report | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | **本 packet 不为其编造任何题数、alpha 或结构结论** | 未知 | `NOT_ASSESSED` | 存在性已确认（Crossref 记录存在），但**无法给出可复核的出处** |

### 2.10 `NOT_ASSESSED` 登记表（R3-A3b 新增；依 review-r2 §R-0 / adjudication §C item 6）

派工书写「12 条」；本 packet **重算为 13 条**。差异原因：派工的 12 条未把 `L3`（Rubin Liking 分量，`UNVERIFIED` 标记与 `NOISY_PROXY` 判定并存）计入 —— 该行同样违反新 §1.2 记账规则 1。**以 13 为准。**

| # | 来源状态 | 原判定 | 现判定 | 触发标记 | 复通条件 |
|---|---|---|---|---|---|
| `L3` | Rubin 1970 Liking 分量：题数/信度 `UNVERIFIED`（U19） | `NOISY_PROXY` | **`NOT_ASSESSED`** | 行内 `UNVERIFIED` | 打开 Rubin (1970) 原文 Table 1 核对 Liking 分量题数与计分 |
| `S2` | Apt & Hurlbert (1992) **无 DOI**；简版 Eisert et al. (2026) `UNVERIFIED` | `NOT_IDENTIFIABLE` | **`NOT_ASSESSED`** | 无 DOI + `UNVERIFIED` | 取得可解析题录；确认是否真的无 target slot |
| `S5` | PMC2861288，DOI `UNVERIFIED` | `NOT_IDENTIFIABLE` | **`NOT_ASSESSED`** | `UNVERIFIED` | 取得 DOI 或原刊题录 |
| `T7` | Wildman et al. (2025) 经 exa.ai 检索元数据，`UNVERIFIED_DOI` | `NOISY_PROXY` | **`NOT_ASSESSED`** | `UNVERIFIED_DOI` | 取得出版方 DOI；§4.1 的 `Distrust` 建议依赖此行 |
| `T8` | Wheeler et al. (2025) 经 exa.ai，`UNVERIFIED_DOI` | `NOT_IDENTIFIABLE` | **`NOT_ASSESSED`** | `UNVERIFIED_DOI` | 取得 DOI 与 COSMIN 评审原文 |
| `A6` | Griffin & Bartholomew (1994) 工具描述页，`UNVERIFIED_DOI`（U03） | `NOISY_PROXY` | **`NOT_ASSESSED`** | `UNVERIFIED_DOI` | 取得原刊题录 |
| `A7` | Collins & Read (1990) `UNVERIFIED_DOI`（U04），构成为二手转述 | `NOISY_PROXY` | **`NOT_ASSESSED`** | `UNVERIFIED_DOI` | 取得原刊题录与题本 |
| `A8` | Fraley & Shaver (2000) *JPA* `UNVERIFIED_DOI`（U05） | `NOISY_PROXY` | **`NOT_ASSESSED`** | `UNVERIFIED_DOI` | 取得 DOI |
| `A9` | Hao et al. ECR-R-GSF，`UNVERIFIED_DOI`（年份/卷期/作者全名单未核） | `NOISY_PROXY` | **`NOT_ASSESSED`** | `UNVERIFIED_DOI` | 取得 DOI 与卷期 |
| `C6` | Beatson et al. (2008) *JPSP* 95(5) `UNVERIFIED_DOI`（U07） | `NOISY_PROXY` | **`NOT_ASSESSED`** | `UNVERIFIED_DOI` | 取得 DOI；原行已自承「原始题录未核实 → 不附任何题数、alpha 或结构结论」 |
| `D4` | MacCallum et al. (2001) `AGENT_RECALL`（U09） | `NOISY_PROXY` | **`NOT_ASSESSED`** | `AGENT_RECALL` | 用 Crossref 核 `10.1037/…` 或期刊页核实卷期页码 |
| `D5` | Stets & Burke (2000) `AGENT_RECALL`（U12） | `NOT_ASSESSED` | `NOT_ASSESSED`（**不变**） | `AGENT_RECALL` | 取得题录 |
| `X4` | CRSS 剑桥页 `UNVERIFIED_DOI` | `DERIVED` | **`NOT_ASSESSED`** | `UNVERIFIED_DOI` | 取得 DOI 与年份/卷期 |
| `A17` | PICS —— 本 packet 三次 Crossref 检索均未命中可确认题录 | （原无此行） | **`NOT_ASSESSED`** | `NOT_OPENED` | 取得可解析题录 + 官方量表页；并确认 person- 还是 pair-directed |

**另有 3 行带 `UNVERIFIED*` 标记但分类列本就是 `—`（无坐标层判定）**，故不受记账规则 1 约束，但其承载的断言已在使用处加限定：`A10`（ECR-R 跨文化非不变性，`U17`）· `A11`（9 量表性取向不变性 4/9）· `A14`（同性关系依恋，partner-report 先例）。

**并且**：另有若干行引用了带 `UNVERIFIED_DOI` 标注的**参考条目**，但其**自身**的指针已可解析（如 `S6` → ref 66 Goldhammer & McCabe `UNVERIFIED_DOI`；`X6`/`X7` → 依赖 `L2`/`X1`）。这些行的判定**保留**，但其**传递依赖**须随引用携带（见 §3.4 与 §5 的限定语）。

**这张表的效力**：`NOT_ASSESSED` **不是**对构念的否定，也**不是**对工具的否定。它只表示：**在打开一手来源之前，本 packet 不对任何坐标层关系发言。** 依 adjudication §C item 6，这些缺口**不得**被任何 lane 当作「该坐标无可用工具」的证据。

---

## 3. 横向分析

### 3.1 方向性：哪些工具**结构上不可能**表示 directionality

这是本文件对 LHRM 最重要的一张表。分四类。

#### 类 1 — Agent 层工具：target slot 结构上为空

`ECR / ECR-R / ECR-SF / RSQ / AAS / AAQ / WTC-Trait / VFI / HISD / 3VDI / Interpersonal Dependency / Personal Sense of Power / Romantic Beliefs Scale / Reiss RPS / 泛信任量表族`

可索引为 `Z[k, i, ·]`，但 `Z[k, i, j]` 不可得。

> **R3-A3b 的两处限定**（依 adjudication §C item 6 与 review-r2 §R-0）：
> 1. 本表**不是**「该坐标 `NOT_IDENTIFIABLE`」的证据集。按新 §1.2，它是一个 **`LAYER_MISMATCH` 清单** —— 每一条的正确分类是层级/靶位错配。`ECR-R / ECR-SF / WTC-Trait / 3VDI / Interpersonal Dependency / Personal Sense of Power / Romantic Beliefs Scale / Reiss RPS` 已据此在 §2 逐行改判；`RSQ / AAS / AAQ / HISD / 泛信任量表族` 因来源未打开而为 `NOT_ASSESSED`。
> 2. **「ECR 族全部只有 Agent 层 trait 工具」这一概括已被 `A15`（ECR-RS, `10.1037/a0022898`）推翻** —— ECR-RS 提供**关系特异**的施测形态。类 1 清单应读作「**这些具体子工具**是 Agent 层」，不是「ECR 族是 Agent 层」。

**关键细节**：Fraley 官方页面明确说 ECR-R 可被改写指向母亲/特定对象。这意味着"定向化"是一个 **instrument rewriting 决策**，会牵动 IRT 标定的有效性。LHRM 若采用，必须作为独立决策审计（交 R05）。**R3-A3b**：该"可改写"陈述在本 packet **未重新核实官方页面** → 记为 `CITED_PRIMARY (relay, 未由 R3-A3b 重开)`；但 **ECR-RS（`A15`）已提供一条不依赖改写的既有路径**，其引用已由 Crossref 确认。

#### 类 2 — 构念本身近对称，拆两方向会重复计数

`IOS / RCI / PRQC / DAS / CSI / QMI / KMS / RAS / RS(10/5)`

- IOS 测"自我—他人边界重叠度"，RCI 测"互动频率/多样性/影响力"，DAS/PRQC 归入二阶总分。
- 把 IOS 记成 `WeNess(A→B)` 与 `WeNess(B→A)` 两个独立坐标，**其语义差异远小于同一坐标的测量误差**。
- 这与 `CURRENT_ARCHITECTURE.md` §7 相关，但性质不同：这里不是"动态耦合"问题，是**重复计数**问题 —— LHRM 的低冗余判据在这里会失手，因为两个方向的差异是**测量噪声**而非**状态差异**。

#### 类 3 — pair-level 指标，结构上无法分解

`ANS 生理同步`（X8）

- **结构论证（本 packet 唯一据以判 `NOT_IDENTIFIABLE` 的理由）**：本身是两信号的耦合/互相关。分解为 i→j 与 j→i 需要额外的、可争议的假设（如"谁跟随谁"）。**耦合本身不含方向性信息。**
- **与结局的关联证据（另一类，不得混用）**：与关系结局的关联方向矛盾（交感 +、副交感 −）、异质性高（**I²=76%**，引用时必须同时带上）、2026 年综述称"心理意义仍含糊"，甚至与自报婚姻冲突正相关。
- 结论：**不能作为任何 LHRM 构念的 proxy，只能作为 mechanism evidence。** 这与 `CURRENT_ARCHITECTURE.md` §2"神经/遗传/进化研究只作 mechanism evidence"的定位一致。
- **R3-A3b 补充**：`01:326` 同型来源（de Paula / Stanford）在**文献检索层**上支持一个比"结构不可分解"更弱也更稳的结论：生理通道缺少**关系特异**的方向性。**本 packet 不主张**存在任何"双通道有向"生理工具 —— 那是 §4.2 Q1 的开放问题，且本 packet 的检索不构成字段级否定。

#### 类 4 — 行为/观察类，可定向但需要额外条件

`RMBM / PRCA / Gable et al. (2004) 事件清单 / SMS 数字轨迹`

需要：(a) 每人分别报告或分别编码；(b) 时间戳；(c) 编码者信度。SMS 数字轨迹满足 (a)(b)，但缺 (c) 的"关系构念映射理论"（作者自己指出）。

#### 方向性良好的族（真正的 `DIRECT_PROXY` 候选）

`Rempel TS / DTS`（trust）· `SDI-2 partner-related / PSSLW`（sexual desire）· `PRI / PPRS`（PPR）· `RPI / RBA`（power/balance）· `RMBM`（maintenance 行为）

其中**只有 PRI 的 Study 3（161 对伴侣 APIM）把"i 的知觉"与"j 的自报行为"在同一模型里对起来** —— 这是本 packet 找到的最接近 LHRM `Belief_i(Z[j→i])` 与 `Z[j→i]` 分离并联结的既有范式。

> **R3-A3b 对本小节两处范围限定的补充**（依 adjudication **X-14** / review-r2 §R-0）：
> 1. "**本 packet 找到的**"这一措辞**保留且是准确的** —— 本目录内唯一一条。上位断言「**没有任何已验证坐标同时拥有自陈信念通道与行为/生理独立通道**」（见 §4.2 Q1）**按字面为假，已被收窄**，本小节不承担该断言。
> 2. "**只有 PRI 的 Study 3**"是**本目录内**的计数，不是领域计数。本 packet **未**系统检索 trust 的行为博弈范式（trust game / prisoner's dilemma 类），**未**检索 observer-coded relationship-process research。⇒ **不得**把本小节读成「只有 PRI 一条双通道研究存在」。

### 3.2 State vs Trait 与时间尺度

| 时间尺度 | 本 packet 中可用的工具 | 缺口 |
|---|---|---|
| 逐次互动（state） | Overall & Sibley (2009) 日记；**Pietromonaco & Barrett (1997)** 日记（原表误作 Pietromonaco & Laurenceau 1998，R3-A3b 已引 Crossref 更正）；Laurenceau et al. (1998) event-contingent diary；PRI-8 每两周 × 8 周 RI-CLPM | **没有"信任更新"或"欲望更新"的 state 工具。PPR 有 state 化证据，trust 没有** |
| 日 / 周 | Impett et al. (2008) 的 2 题 partner-specific 性欲双周题（波内 α_wave .69–.98）；SMS 数字轨迹 | 依恋的日常波动（除 Overall & Sibley） |
| 月 | SDI-2（过去 1 月） | 除性欲外几乎无月度工具 |
| 单次 / 现状 | 几乎全部自陈关系工具 | — |
| 回溯年度 | **无** | — |
| 跨文化恒定 | ECR-R（62 文化区）；SDI-2（42 国 / 26 语言） | **只有这两个构念族有大规模跨文化证据；其余均为单点或未测** |

> **R3-A3b 对本表的两处更正与一处限定**
>
> 1. **更正**：`Pietromonaco & Laurenceau (1998)` → **`Pietromonaco & Barrett (1997)`**（Crossref 直开，DOI `10.1037/0022-3514.73.6.1409`）。同一错误在 §2.5 的 `A13` 行、§4.3 的 R09 输入、ref 11 三处出现，已同步。
> 2. **更正**：「依恋的日常波动（除 Overall & Sibley）」**不完整** —— `A16`（Fraley, Vicary, Brumbaugh & Roisman 2011, *JPSP* 101(5):974-992, `10.1037/a0024150`）已对**依恋的跨时间稳定性 vs 变化性**做了实证比较。**但本 packet 未打开该文全文**，故不主张其结果方向；能说的只是：**依恋的 trait-vs-state 问题是已被实证检验的竞争模型，而不是一个已定事项。**
> 3. **限定（X-14）**：最后一行「**只有这两个构念族有大规模跨文化证据**」是一个**字段级存在性否定**，而本 packet 的跨文化检索只覆盖了 §3.4 表内已列的工具。改述为：**在本目录已检索的范围内，只有 AttachmentSecurity（ECR-R，62 文化区）与 SexualDesire（SDI-2，42 国 / 26 语言）两个构念族有大规模跨文化不变性证据；其余构念族在本目录内均为单点证据或未测。** 本 packet **不主张**其余构念族在字段上缺乏跨文化证据。
> 4. 本表「没有信任更新或欲望更新的 state 工具」这条缺口**保留**：`A16` 属**依恋**族，不覆盖 trust 或 sexual desire 的更新测量。**本 packet 不主张**该缺口已消失，亦不主张它是字段级事实。

### 3.3 已知 confounds 汇总

| Confound | 具体证据 | 对 LHRM 的含义 |
|---|---|---|
| **反向措辞 / 方法因子** | ECR-SF 的 2 个方法因子（正/反向措辞，"移除 response set 后"才拟合好，A5）；ECR 的 CMB 使 anxiety–avoidance 相关归零（S53）；Rempel 1985 的反向措辞因子（S05）；DTS 8 题中 5 题反向（S17） | **不可区分的方差会同时落在多个构念上**，污染任何 redundancy 检验 |
| **共同方法方差 (CMV)** | PRQC trust ↔ satisfaction .58 / commitment .38 / intimacy .47 / love .48，仅 passion .14（S46） | LHRM Gate C 的三对挑战（Trust vs AttachmentSecurity、PPR vs Trust/Care/Attachment、Liking vs RomanticAttraction）**在自陈通道上都缺乏分离性证据** |
| **社会赞许** | IOS 自称 minimal；**DTS r=.00 (n.s.) 是少见的反证据**（S17）；RCI / PLS / PRQC 未报告 | 社会赞许在 trust 与 closeness 上表现不一 → 不能用一个统一的"correction"处理 |
| **Faking / demand characteristics** | 本 packet 未检索专门的 faking 研究 → `NOT_ASSESSED` | 在线施测（MTurk、AMT）扩大了此类风险（IOS 复评、PRI item pool 均用 MTurk/在线样本） |
| **求值者/施测者效应** | **Schumm et al. (1985) 判定 DTS 测的是 benevolence 而非 trust**（S18） | **"某量表被广泛使用"不能作为其可用的证据** |
| **量表题项的构造缺陷（scale item construction defect）** | **Stafford (2010) 判定两个广泛使用的关系维持量表（`C4` RMSM 及其前身）有 "fundamental measurement flaws"，在正确 item construction 下均不可用**（S34）；ECR-SF 的 2 个方法因子（正/反向措辞，"移除 response set 后"才拟合好，A5）；ECR 的 CMB 使 anxiety–avoidance 相关归零（S53）；Rempel 1985 的反向措辞因子（S05）；DTS 8 题中 5 题反向（S17） | **R3-A3b 移动记录**：`Stafford (2010)` 原挂在「求值者/施测者效应」行 —— **错行**。该判定**不是**施测者/评分者效应，而是**量表题项构造缺陷**：两个前代工具在同一正确 item construction 下不可用。移入本行后它承担两个不同的作用：(a) 对 `C4` 的**工具级**判定 → `DEFECTIVE_INSTRUMENT`；(b) 对**任何**构念的判定 → **无**。**它不构成**「`Caregiving` 坐标结构上不可测」或「`Dedication` 坐标结构上不可测」的任何证据。 |
| **量表题项的语义溢出** | PRI 的 caring 题项因与 global satisfaction 交叉负荷被剔除（S12） | PPR 的理论三成分（understanding / validation / caring）在测量上无法三者并存 |
| **ceiling** | PRI 正题均值 +1.5SD 以上区分力差（S12）；IOS 单题 | 高信任 / 高 closeness 区间不可区分 → **正态分布假设在该区间失效** |
| **回顾性记忆偏差** | SDI-2 回顾过去 1 月（S24）；DAS / IMS 为现状 | 月度尺度的性欲数据有明显的记忆重构 |
| **fallback 指令 / 工具层对"关系不存在"的处理** | PLS："若从未恋爱过，请想最接近那种关心的那个人"（S23）；ECR 的 trait 语言（S02） | **R3-A3b 重新锚定（依 review-r2 `R-0.7` / `B` top_rec 第 6 条）** —— 详见下方专段 |

#### 3.3a 「工具在『关系不存在』状态造替代对象」的正确依据（R3-A3b 重新锚定）

**被取代的原文**（逐字保留）：

> | **fallback 指令 = 静默伪造 target** | PLS："若从未恋爱过，请想最接近那种关心的那个人"（S23）；ECR 的 trait 语言（S02） | 工具层面对"关系不存在"这一状态的处理方式是**造一个替代对象** —— 在 LHRM 框架里等于把 `Unknown` 静默 coerce 成一个值，**违反 `CURRENT_ARCHITECTURE.md` §9 与 `AGENTS.md` 的 Unknown 保留原则** |

**取代它的重述**（依 review-r2 `R-0.7`：`B` top_rec 第 6 条 `CONTESTED`；及 adjudication **X-14**）：

| 项 | 内容 |
|---|---|
| **正确依据** | 旧文把依据挂在 `CURRENT_ARCHITECTURE.md` §9 —— **错位**。正确依据是三条并列：① `CURRENT_ARCHITECTURE.md` **§3** `Reality != Observation != Belief`（**一个被工具换题对象造出来的目标，既不是外部现实，也不是对外部现实的观察，而是一个 belief 对象 —— 但工具没有把它标成 belief**）；② **§9 原则 1**（`S / O / D / E` 是**局部评价视图**，不是完整世界本体 —— 工具用一个"最接近的那个人"充当当前关系，本身是把局部视图当成了世界本体）；③ **§10 `unknown` 事实状态**（把该状态留成 `unknown` 是一个**合法表示**，而 fallback 指令使它**不可表示**）。 |
| **对 ECR trait 语言的改判** | 旧文把它与 PLS 的 fallback 指令并列为「**静默伪造 target**」。**改判**为：**ECR 的 trait 语言是"诚实标注 Agent 层 scope"** —— 官方指引明说它测的是「how you generally experience relationships, not just what is happening in your current relationship」（§1.1 规则 4），即**它宣称自己不在测当前关系**。把一个明确声明了 scope 的 trait 工具说成"静默伪造"是**不成立的**。 |
| **对 PLS fallback 指令的保留表述** | `AGENTS.md`「Unknown/missing data must remain explicit; never silently coerce missing information into neutral/perfect-match values」这一条**保留**。但表述改为：**工具的 inability 不构成对该状态的合法表示** —— fallback 指令**不是**一个 `Unknown` 保留，它是一个**替换**，且替换后的值不带 provenance 标记。**本 packet 不主张**任何工具"违反 `AGENTS.md`"；`AGENTS.md` 不是被违反的规范，而是本 packet 用来**判读工具行为**的参照。 |
| **不得推出的结论** | 依 adjudication §C item 6：以上是**工具层的表示缺陷**，**不是**任何 LHRM 坐标不可识别的证据。也**不是**「陌生人 dyad 不能进入 Case Bank」的证据 —— 后者是 §4.2 Q3 的**抽样框**问题，须单独裁决。 |

### 3.4 跨文化 / 测量不变性证据总览

| 层级 | 有证据的 | 明确失败或缺失的 |
|---|---|---|
| **多国 · 大样本 · 跨性别 · 跨性取向** | **仅 SDI-2**（N=82,243 / 42 国 / 26 语言 / 跨性别 / 跨性取向） | — |
| **多文化区** | ECR-R（62 文化区） | ECR-R-GSF **中国样本未达 scalar**；ECR-R China/Greece **部分参数不满足不变性** |
| **跨性别 / 关系状态** | ECR（scalar，含 dyad 内 partner 角色）；RS10/RS5；ECR-R（strict factorial） | AAQ 仅 partial strong invariance（`A8` 本身为 `NOT_ASSESSED`：`UNVERIFIED_DOI`） |
| **跨性取向** | 9 个关系量表中**仅 4 个通过** | ECR-R 需修改；Gibbons & Buunk (1999) 仅 partial 且被 "urge caution"；Cutrona & Russell 与 Hughes et al. (2020) **不推荐**。**R3-A3b 限定**：本行**全部**内容来自 `A11`（Elizabeth & Clark，`UNVERIFIED_DOI`，**本 packet 未打开**）→ 整行为 `CITED_SECONDARY (UNVERIFIED_DOI)`，**不得**作为定量的跨性取向可用性结论引用 |
| **跨临床 / 非临床人群** | ECR（configural + partial-metric + partial-scalar） | CMB 存在 → 建议用 latent means 而非原始分比较 |
| **跨性别/性取向（性欲族）** | ASEX 达 configural/metric/partial scalar/partial residual | **latent mean 与 latent variance invariance 均不成立**。**R3-A3b 限定**：来源 ref 65 `10.1007/s13178-024-01040-0` 标 `UNVERIFIED_DOI` → 整行 `CITED_SECONDARY (UNVERIFIED_DOI)` |
| **完全无不变性证据** | RCI（2015 复检是同文化复检）、DTS、IMS、VFI、RMBM、IOS-原始研究、RPI、RBA、3VDI、Interpersonal Dependency、Personal Sense of Power、PRI、PPRS | 全部。**R3-A3b 限定**：「完全无」是**本目录内**的判断，**不是**字段级否定（依 X-14）；且 RPI / RBA 的不变性状态本 packet 记为 `UNKNOWN`（未打开全文），非"无证据" |

**跨表结论（R3-A3b 收窄）**：旧文写「**关系科学里"跨文化不变"的证据高度集中在两个构念族（依恋、性欲），而 LHRM 最缺的三个（Dedication、OutcomeDependence、Cohesion）恰好是零证据。这是一个不应被"文献量"掩盖的结构性问题。**」——

**"零证据"是字段级存在性否定，本 packet 的检索不支持它**（依 adjudication **X-14** / review-r2 **R-D25** 同型处置）。改述为：

> **在本目录已检索的范围内**，跨文化 measurement-invariance 证据只出现在 AttachmentSecurity（ECR-R，62 文化区）与 SexualDesire（SDI-2，42 国 / 26 语言）两个构念族；Dedication / OutcomeDependence / Cohesion 在本目录内**没有**不变性证据条目。**这是一个关于本目录覆盖面的观察，不是关于这三个构念在文献中的存在性的结论。** 要把它变成后者，需要一次覆盖这三个构念族的独立系统检索 —— 本 packet 不主张该命题成立，**也不主张其反面**。
>
> 可保留的**结构性**观察（本目录内成立）：**LHRM 最缺工具的三个构念，恰好也是本目录跨文化证据最少的三个。** 这个"覆盖与需求错位"本身是关于**本项目测量资源分配**的事实，不需要字段级否定即可成立。

---

## 4. 对 LHRM 各文档的具体建议（`AI recommendation`，非 Human requirement）

### 4.1 对 `PARAMETER_CONVERGENCE_V0_1.md` 的候选构造的测量学裁决建议

> **R3-A3b 最高严重度裁决：D7 / D8 两条降级建议整体打回（依 review-r2 `R-0.5` / `B-C4` `CONTESTED`；派工 top_rec 第 1 条 `RECLASSIFY_AS_METHOD_LIMIT`；adjudication §C item 6）**
>
> **被取代的原文**（逐字保留，两行）：
>
> | 候选 | 被取代的建议 | 被取代的理由 |
> |---|---|---|
> | D7 Dedication | 「**降级为 `NOT_IDENTIFIABLE` 直到自建工具**；IMS 只能作为 `DERIVED` 混合读出」 | F7 / G3 |
> | D8 OutcomeDependence | 「**降级为 `NOT_IDENTIFIABLE`**；两端（dependence 工具、power 工具）皆空」 | F8 / G1 |
>
> **打回依据**：本文件 §1.2 旧定义把 `NOT_IDENTIFIABLE` 规定为「**结构上**无法支撑（不因为"还没人做"，而是因为"这样做不了"）」，但这两行所依据的 9 条 `NOT_IDENTIFIABLE` 条目，其**自述理由**是「**是 Agent 层 trait**」「**抽样框不匹配**」「**替代方案在别处**」—— 即**层级不匹配**与**检索不足**。**用一类被重载的标签去产生 canonical 层级的状态转移，是本文件最高严重度的缺陷。**
>
> **本 packet 的处置（作为一块，逐条）**：
> 1. **两条降级建议整体撤回**，改为 `RECLASSIFY_AS_METHOD_LIMIT`：本目录缺少 relation-level 工具，这是**工具层的限制**，**不是** `D7` / `D8` 的层级判定。
> 2. **本文件自报的 `D7 / D8 = NOT_IDENTIFIABLE` 文本，保留为「报告自述」（report self-description）**，其效力仅限"本 lane 在其检索范围内未找到工具"；**不作为架构裁决**，也不得被任何下游文档当作架构前提。
> 3. 依 adjudication **X-3**：`Dedication` **保持 directed-state candidate**；`Satisfaction` **保持 `Derived` / evaluation-state candidate**，其晋升是**条件预登记**，不由预测强度蕴含。本 packet **不实施**任何层级变更。
> 4. 依 adjudication **X-1**：`PPR` 保持 `BeliefState`；`Satisfaction` 保持 `Derived`。§4.1 中 B1 / R3 两行与该裁定一致，**保留**。
> 5. **新 §1.2 已把 9 条重载条目重新归类**（`LAYER_MISMATCH` / `SEARCH_INCOMPLETE` / `DEFECTIVE_INSTRUMENT` / `NOT_ASSESSED`），`NOT_IDENTIFIABLE` 现仅剩 **1 条**（`X8` 生理同步，且已补上其结构论证）。逐行见 §2 与 §2.10。

**下表为 R3-A3b 修订后的现行建议。**

| 候选 | 建议标记 | 理由 |
|---|---|---|
| D1 Liking | `KEEP` + 标注"**测量仅能经 IOS/RCI 借 closeness**" | 无专门的 directed liking 工具；IOS 是唯一有陌生人验证的。**R3-A3b 限定**：「唯一有陌生人验证」是**本目录内**陈述；`A17`（PICS）若在打开来源后确认 IOS 族定位，此处须重述 |
| D2 RomanticAttraction | `KEEP` + 标注"**测量只能经 PLS/TLS，且与 love/passion 不可分**" | TLS 分量互相依赖；PLS 绑定多成分 |
| D3 SexualDesire | `KEEP` + 标注"**partner-specific 只占 SDI-2 三分之一；实验室唤起范式内女性方向的自陈–生理一致性显著低于男性方向**" | F5 + `S8`。**R3-A3b 限定**：后半句已从「女性方向无等价生理通道」收窄为 scope-limited 的实验室唤起发现（依 X-14） |
| D4 Trust | `KEEP` + 新增 open question: **"Trust 是否有事件层表示？现有工具全部是 level"** | F3 / G2。**注意**：本 packet 的检索**不**构成「trust 无行为通道工作」的字段级否定（§3.1 末限定） |
| D4 open question（Distrust） | **`HOLD_FOR_EVIDENCE`** —— 原「**升级为独立候选**，理由从"待测"改为"78% 共存的直接证据 + trust/distrust 分别测量的工具化路径**」被取代** | 依 adjudication **X-4** + review-r2 §R-0。理由：该建议的唯一证据链是 `T7`(`UNVERIFIED_DOI`) → `T6`(Hsu 2019 学位论文，作者未核实) → §4.1，**两个未打开来源串成一次 canonical 层级转移**。复通条件见 §2.4 末专段 |
| D5 AttachmentSecurity | `KEEP` + 标注"**主流工具是 trait；依恋的 state 指针见 Overall & Sibley (2009)，且 trait-vs-state 已是实证比较问题（`A16`, `10.1037/a0024150`）**" | F12 / G10 + §2.5a。**R3-A3b 修正**：原「**唯一** state 指针」被 `A16` 推翻；同时「ECR 族只有 Agent 层工具」被 `A15`（`10.1037/a0022898`）推翻 |
| D6 Caregiving | `KEEP` + **明确标注为 `instrument gap`**，理由：VFI/CMS 抽样框均不覆盖"对特定 j 的一般照护倾向" | F6 / G4。**R3-A3b 限定**：「instrument gap」= **`SEARCH_INCOMPLETE`**，**不是** `NOT_IDENTIFIABLE`（依 §C item 6） |
| **D7 Dedication** | **`KEEP`（维持 directed-state candidate）+ 标注 `RECLASSIFY_AS_METHOD_LIMIT`** —— 「**本目录中没有 relation-level Dedication 工具**」；IMS 只能作为 `DERIVED` 混合读出 | **降级建议已撤回**（见上方裁决）。依 **X-3**，`D7` 保持 candidate。**本 packet 不主张** Dedication 不可测；只主张**本目录内**无对应工具。**唯一可辩护的**「缺工具」措辞是：唯一在 relation level 给出承诺性读出的是 **IMS 的复合分**，而 IMS 的**定义层**即把 satisfaction / alternatives / investment 合成为单一读出 ⇒ 它是 `DERIVED`，不是 `D7` 的直接测量 |
| **D8 OutcomeDependence** | **`KEEP`（维持 directed-state candidate）+ 标注 `RECLASSIFY_AS_METHOD_LIMIT`** —— 「**本目录中没有 relation-level OutcomeDependence 工具**」 | **降级建议已撤回**（见上方裁决）。依 **X-4**，`domain` 保持 `FACET_RECOMMENDED_NOT_REQUIRED`。**本 packet 不主张** D8 不可测；只主张**本目录内**无对应工具。**两端的具体状态**（保留原观察）：dependence 侧 —— `3VDI` / `Interpersonal Dependency` / `Personal Sense of Power` 全为 **Agent 层**（现判 `LAYER_MISMATCH`）；power 侧 —— `RPI` / `RBA` 测的是**权力与平衡**，不是依赖。**承载 D8 的最接近现成读出是 `O8`（IMS 的 quality of alternatives + investment size）**，但 `alternatives` 测的是"**该关系之外**的选项"，`investment` 测的是"**已投入**"，两者都不是"j 对我结果的控制力"。**O6 谱系审计的具体数字（38 / 1–2 次 / 无一主流）已降为 `HOLD_FOR_EVIDENCE`，不作为承重证据**（依 X-14） |
| B1 PPR | `KEEP`，并**追加正面确认**：Reis 学派的"行为 responsiveness vs 感知 PPR"区分与 LHRM §5 B1 完全一致 | F10。依 adjudication **X-1**，`PPR_(i about j,t)` 保持 **BeliefState**；本 packet **不**主张它应升为 Reality/DirectedRelationshipState |
| P1 Cohesion | 保持 `contested`，**追加：工具侧无法裁决 shared latent 是否存在** | F9 / G6。**R3-A3b 限定**：「无法裁决」是**本目录内**判断，非字段级否定 |
| R3 Satisfaction | 保持 `DERIVED`；若需要一个读出，**RS10/RS5 是本目录内唯一有跨性别不变性 + 10 万人样本的候选** | X2。依 adjudication **X-1**，`Satisfaction` 保持 **Derived / evaluation-state candidate**，晋升是条件预登记 |

### 4.2 三个需要 Architect 明确裁决的架构问题

**Q1 — 是否为每个有向坐标建立"双通道"要求？**

> **R3-A3b 收窄（依 review-r2 `R-C14` / `B-C11` `WRONG-SCOPE`）**
>
> **被取代的原文**（逐字保留）：「本 packet 的最重要发现是 **G9：没有任何已验证坐标同时拥有自陈信念通道与行为/生理独立通道**。LHRM 当前的 `Reality != Observation != Belief` 三分在**测量学上没有现成实现**。」
>
> **旧措辞按字面为假**，两条理由：
> 1. **trust 有行为博弈范式工作**（trust game / prisoner's dilemma 类），本 lane **未检索**该文献族；
> 2. 报告自己的 **PRI Study 3**（`X9`）是**双 informant、单通道**（两方都是自陈），它证明的是「把 i 的知觉与 j 的自报行为放进同一模型」这条**方法学形态**可实现，**不是**「存在两条独立通道」。
>
> **收窄后的表述（可引用版本）**：
>
> > **G9（收窄版）**：在**本目录已检索的范围内**，**没有任何 `relation-level directed coordinate`** 同时拥有 **pair-level、关系特异的自陈信念通道**与**一条独立的观察 / 生理通道**。
> >
> > **这不是架构级 gap。** 它是一个**开放的技术问题**（open technical question），需要一次覆盖 (a) trust 的行为博弈范式文献族与 (b) observer-coded relationship-process 文献族的独立检索才能回答。依 adjudication §C item 6（"Search failure/access restriction is not ontology evidence"），**本 packet 的检索不足不得**被写成「测量学上没有现成实现」。
>
> **同时明确（本 packet 不主张）**：不主张存在这样的双通道坐标；也不主张不存在。**待检索范围已被显式登记**（见 §6 新增的 `U21`）。
>
> Architect 需要裁决的**问题本身不变**：`Reality != Observation != Belief` 三分是否要求一个测量实现？—— 但**举证责任现在落在"要求方"**：主张需要双通道的一方，须先补上上述两次检索。

**Q2 — 对称性 vs 有向性：哪些 LHRM 坐标是**结构性对称**的？**
`IOS / RCI / DAS / PRQC` 一旦记成两个独立有向坐标，测到的差异是**状态差异**还是**测量噪声**？本 packet 无法回答（因为没有工具能同时测两个方向并报告其重测信度）。若 Architect 认为某些坐标本应是对称的，应显式声明"该坐标的 i→j 与 j→i 是同一参数的两个标签"，否则冗余检验会在噪声上运行。

**Q3 — 抽样框：LHRM 是否承认"多数关系工具假设关系已存在"？**
`RCI`（"最亲近的关系"）、`PLS`（fallback 指令）、`ECR`（trait 语言）都隐含该假设。若 LHRM 的人类 dyad 域包含陌生人、敌对、第三方、尚未确立的关系（`CURRENT_ARCHITECTURE.md` §2 明确允许），则**这些工具不能直接用于 Case Bank 的那部分材料**。这与 R11 应合并处理。

### 4.3 给其他 lane 的直接输入

- **→ R01 / R02（构念收敛与冗余）**：PRQC 的 trust ↔ satisfaction .58 / commitment .38 / intimacy .47 / love .48（S46）是"Trust vs AttachmentSecurity"与"PPR vs Trust"冗余挑战的**第一个实测数字**；且这些数字来自同一自陈通道，因此**不构成构念可分性的证据，只构成自陈不可分性的证据**。
- **→ R05（识别/统计）**：DTS 的方向性发现（S17：Female r=.23 vs Male r=−.06）提示 `Trust` 与 `OutcomeDependence` 存在**内生的测量耦合**；任何把两者当独立坐标的模型都会遇到不可忽略的共线性。ECR-R 的方法效应（.17 vs .41，S53）是"工具选择会改变结论"的量化警示。
- **→ R07（部分可观测/缺失）**：PLS 的 fallback 指令与 ECR 的 trait 语言说明**工具层面存在把 `Unknown` 静默 coerce 的系统性倾向**（S23, S02）。这是 LHRM Unknown 原则在**测量采集端**的具体对手。
- **→ R09（动态系统/迟滞）**：能提供 state 层测量的只有 Overall & Sibley (2009)、**Pietromonaco & Barrett (1997)**、PRI-8 的 RI-CLPM、X13 的数字轨迹。**Transfer-law 的 intensive-longitudinal 证据来源只有这四条**，其中只有 PRI 有配套的 actor-partner 行为锚定。**R3-A3b 限定**："只有这四条"是**本目录内**计数；`A16`（`10.1037/a0024150`）增加了**依恋的跨时间稳定性比较**这一条纵向证据来源，但它测的是依恋、不是转移律所需的关系状态多波序列。
- **→ R10（互惠/权力/依赖）**：`OutcomeDependence` 与 `Power` **在本目录内**都没有 relation-level validated 工具（`RECLASSIFY_AS_METHOD_LIMIT`，见 §4.1）。R10 若要给出 power 的测量方案，需自建。**R3-A3b 修正**：旧文写「F8（两端都没有可用的 validated 工具）」隐含字段级否定；依 **X-14** 只能作本目录内陈述。**另注**：依 adjudication **X-13**，`TotalDependence/TotalPower` 是**对称派生聚合**、`RelativePower/PowerImbalance` 是**方向性派生读出**，**无独立 Power primitive**；R2-b 的 slot（punitive / legitimacy / felt compliance）保持 `HOLD_FOR_EVIDENCE`。`O6` 谱系审计的具体数字已降为 `HOLD_FOR_EVIDENCE`，**不作为 R10 的承重依据**。
- **→ R11（一般 Human Dyad 域）**：抽样框假设（F12）+ 性取向不变性只通过一半（S54，**`CITED_SECONDARY (UNVERIFIED_DOI)`，见 §3.4**）= 该 lane 的两个量化约束。**R3-A3b 限定**：第二个约束的数值目前**未被一手来源支撑**，只作线索。
- **→ R16（经验验证协议）**：若要一个"最小可用测量面板"，本 packet 的证据支持：`ECR-R`（或 ECR-SF）+ `PPRS/PRI` + `PSSLW partner-specific` + `RMBM` + `RS10`。**但请注意：本 packet 明确不建议把它们当 LHRM 的状态坐标，只建议把它们当"外部效标"（external criterion）** —— 这样既利用了它们的心理测量积累，又不违反 `Representation before scalarization`。**R3-A3b 补充**：面板若需要依恋的**关系特异**（而非 Agent 层 trait）读出，应加 **`A15` ECR-RS**（`10.1037/a0022898`）作为候选 —— 这是本次增补中唯一直接扩大面板覆盖的工具。**不得**因本 packet 未打开其全文而断言其心理计量优于 ECR-R。

---

## 5. 明确非主张（explicit non-claims）

1. **不主张**任何量表分数等于其目标 latent 状态的真值。
2. **不主张** LHRM 的 D1–D8 中任何一个构念已被证实为可独立测量的 latent variable。本文件的结论恰恰相反。
3. **不主张** Rempel 的 trust 三维度、ECR 的两维度、SDI 的两/三维度这些"教科书结构"是稳定的。
4. **不主张**生理同步（ANS）测量关系状态。
5. **不主张**"trust 与 distrust 是独立构念"已在关系场景被证明。
6. **不主张** `Sprecher & Metzler (1989) Sexual Trust Scale`、`Larzelere & Muth (2005) PTS`、`Beatson et al. (2008) Compassionate Love Scale`、`MacCallum et al. (2001) CWTC`、`Deuflhard et al. (2008) Stroop trust task`、`Collins & Read (1990) AAS`、`Griffin & Bartholomew (1994) RSQ`、`Fraley & Shaver (2000) AAQ` 的任何具体题数、版本或信度。
7. **不主张** LHRM 应采纳任何已验证量表作为 LHRM 的默认测量层。
8. **不主张**本文件的四分类是唯一或最终分类。**R3-A3b**：`NOT_ASSESSED` / `LAYER_MISMATCH` / `SEARCH_INCOMPLETE` / `DEFECTIVE_INSTRUMENT` 是本轮为解除 `NOT_IDENTIFIABLE` 重载而引入的**记账工具**，其边界本身待检验。
9. **不主张**文献数量 = validation。
10. **不主张**"关系满意度可作为状态转移的自变量"。
11. **不主张**数字轨迹可直接作为关系状态证据。
12. **不主张**本文件的仪器目录已覆盖测量学。它**不覆盖**：冲突 / 修复 / 背叛 / 嫉妒、关系识别（`P4 Relationship Identity`）的形成与解体、第三方/旁观者编码、网络与生态层测量、临床诊断性访谈（LCCA / Adult Attachment Interview）、跨文化翻译与语义等价性程序、抽样框与匹配（matching hypothesis）方法、`Objective`（第三方参照标准）类工具。
13. **（R3-A3b 新增）不主张**`D7 Dedication` 或 `D8 OutcomeDependence` 因本目录缺工具而应被降级。这两条降级建议已被撤回；本 packet 既不主张降级，**也不主张**两者的层级地位 —— 依 adjudication **X-3** / **X-4**，它们保持 candidate。
14. **（R3-A3b 新增）不主张**`G9`（双通道）在字段上成立或不成立。本 packet 只登记一个**收窄后的、检索范围明确的**否定结果，并把两次缺失的检索显式挂为 `U21`。
15. **（R3-A3b 新增）不主张**`Distrust` 是、也不是 `Trust` 的独立构念。`HOLD_FOR_EVIDENCE` 状态下，两种读法都开放。
16. **（R3-A3b 新增）不主张**`A15`（ECR-RS）或 `A16`（Fraley et al. 2011）在心理计量上优于 ECR-R。本 packet 只确认了它们的**题录存在**与**研究问题**，**未打开全文**。
17. **（R3-A3b 新增）不主张**`A17`（PICS）存在。本 packet 在 Crossref **三次检索均未命中**可确认题录，`psychology.unl.edu` 量表页抓取报 transport error ⇒ 该行是 `NOT_OPENED` 占位，**其存在性本身未被本 packet 确认**。
18. **（R3-A3b 新增）不主张** RCI 的题数是 75。本 packet 自算得 3+38+34=75，但**所依据的已打开原文在同一段又写 69-item**；原典（BSO 1989 Appendix A/B）**未打开** ⇒ 该计数为 `PLAUSIBLE`，不是 `VERIFIED`。

---

## 6. 剩余未知（remaining unknown）

1. `U01` / `U02`（Partner Trustworthiness Scale、Kwapil 等）未核实 → trust 工具族仍有未覆盖部分。
2. `U08`（Sexual Trust Scale）未核实 → 性信任子领域只有综述性侧证。
3. `U09` / `U12`（CWTC、Stets & Burke）未核实 → Dedication 的 identity-theory 系测量证据缺失。
4. `U19`（SRM 系工具）本 lane 未检索 → Liking 的 behavioral-anchor 侧证据不完整；Rubin 1970 的 Liking 分量题数/信度未读到原文。
5. `U13`（smartphone / wearable 被动感知）`FETCH_FAILED` → **没有任何生理/可穿戴的关系状态测量工具被核实**。
6. `U18`（CAAS 等互动编码）未核实 → observer-report 一族实际只有自报行为，**无第三方观察编码工具**。
7. `U11`（Rusbult et al. 1999）未核实 → Dedication 的行为化路径证据缺失。
8. `G9`（双通道）是否真的在测量学上不可得 → **开放的技术问题**。
9. 所有"当前可得性 / 当前使用频率"判断均为 2026-09-27 观察。
10. `U17`（ECR-R China/Greece）具体哪些参数不满足不变性 = `UNKNOWN`。
11. 所有"跨 X 不变"的陈述只在**各自被检验的样本与分组变量**内成立，**不构成普遍不变性**。
12. `U20` "Companionate Love Scale" 原始出处 `UNKNOWN`。
13. 本 packet 未检索"冲突 / 修复 / 背叛 / 嫉妒"族工具 → Dedication 与 Trust 的**负向转移**侧无工具证据。
14. **`U17`（ECR-R China/Greece）具体哪些参数不满足不变性 = `UNKNOWN`**。
15. **（R3-A3b 新增）`U21` — 两次缺失的检索，构成 `G9`（收窄版）的完整边界。** 本 packet **未**检索：(a) **trust 的行为博弈范式文献族**（trust game / prisoner's dilemma / dictator–dictator 类）；(b) **observer-coded relationship-process 研究**（第三方编码的关系过程研究）。在 (a)(b) 未检索前，`G9` 只能表述为 §4.2 Q1 的收窄版。**依 adjudication §C item 6，`U21` 未解**不得**被写成「测量学上没有现成实现」。**
16. **（R3-A3b 新增）`U22` — 13 条 `NOT_ASSESSED` 条目的一手来源**（清单与复通条件见 §2.10）。在这些来源被打开前，本 packet **不**对它们与任何 LHRM 坐标的关系发言。
17. **（R3-A3b 新增）`U23` — RCI 的确切题数。** 已打开的 Gächter et al. (2015) 自身 block 分解为 75，同一文概念段写 69；BSO (1989) 原典**未打开** ⇒ `U23` 未解，任何引用 RCI 题数的地方必须带此限定。
18. **（R3-A3b 新增）`U24` — `A15`（ECR-RS, `10.1037/a0022898`）与 `A16`（`10.1037/a0024150`）的全文。** 两者题录已由 Crossref 确认，但**心理计量与实证结果均未读取**。特别是 `A16` 的稳定性 vs 变化性判别结果，是本文件关于「依恋是 trait 还是 state」的唯一潜在 carrying source，须打开后才能被引用。
19. **（R3-A3b 新增）`U25` — `A17`（PICS）是否存在。** Crossref 三次检索未命中；`psychology.unl.edu` 量表页 `transport error`。`A17` 是 `NOT_OPENED` 占位行，**其存在性未确认**。
20. **（R3-A3b 新增）`U26` — `O6` 谱系审计（`10.1111/jftr.70019`）全文。** 旧文倚重的三个具体数字（38 个具名量表 / 各自仅被用 1–2 次 / 无一成为主流）全部 `HOLD_FOR_EVIDENCE`；且 `无一` 即使核实为真，按 **X-14** 也只能表述为该审计覆盖范围内的结果。

---

## 7. 引用列表（去重后的稳定指针）

**Journal articles（Crossref 已核实题录，2026-09-27）**

1. Rempel, J. K., Holmes, J. G., & Zanna, M. P. (1985). Trust in close relationships. *JPSP*, 49(1), 95-112. `10.1037/0022-3514.49.1.95`
2. Aron, A., Aron, E. N., & Smollan, D. (1992). Inclusion of Other in the Self Scale and the structure of interpersonal closeness. *JPSP*, 63(4), 596-612. `10.1037/0022-3514.63.4.596`
3. Berscheid, E., Snyder, M., & Omoto, A. M. (1989). The Relationship Closeness Inventory. *JPSP*, 57(5), 792-807. `10.1037/0022-3514.57.5.792`
4. Brennan, K. A., Clark, C. L., & Shaver, P. R. (1998). Self-report measurement of adult attachment: An integrative overview. In Simpson & Rholes (Eds.), *Attachment theory and close relationships* (pp. 46-76). Guilford. `https://labs.psychology.illinois.edu/~rcfraley/measures/brennan.html`
5. Fraley, R. C., Waller, N. G., & Brennan, K. A. (2000). An item response theory analysis of self-report measures of adult attachment. *JPSP*, 78(2), 350-365. `10.1037/0022-3514.78.2.350`
5. Fraley, R. C., Waller, N. G., & Brennan, K. A. (2000). An item response theory analysis of self-report measures of adult attachment. *JPSP*, 78(2), 350-365. `10.1037/0022-3514.78.2.350`
6. Fraley, R. C., Waller, N. G., & Shaver, P. R. (2000). Reliability and validity of the Revised Experiences in Close Relationships (ECR-R) self-report measure of adult romantic attachment. *Assessment*. `10.1177/0146167205276865`
7. Wei, M., Russell, D. W., Mallinckrodt, B., & Vogel, D. L. (2007). The Experiences in Close Relationship Scale (ECR)-short form. *J Personality Assessment*, 88(2), 187-204. `10.1080/00223890701268041`
8. Schmitt, D. P., Alcalay, L., Allensworth, M., et al. (2004). Patterns and universals of adult romantic attachment across 62 cultural regions. *J Cross-Cultural Psychology*, 35(4), 367-402. `10.1177/0022022104266105`
9. Brauer, K., & Proyer, R. T. (2025). A study of the measurement invariance of the Experiences in Close Relationships (ECR) questionnaire across relationship status, romantic partners, and gender. *EJPA*. `10.1027/1015-5759/a000902`
10. Overall & Sibley (2009). Attachment and dependence regulation within daily interactions with romantic partners. *Personal Relationships*, 16, 239-261. `10.1111/j.1475-6811.2009.01221.x`
11. **Pietromonaco, P. R., & Barrett, L. F. (1997).** Working models of attachment and daily social interactions. *JPSP*, 73(6), 1409-1423. `10.1037/0022-3514.73.6.1409`（**R3-A3b 引用更正（`R-B13`）**：原误作 "Pietromonaco, P. R., & **Laurenceau**, J.-P. (1998)"。2026-09-27 直开 Crossref：`author` = Pietromonaco (first) + **Barrett, Lisa F.**；`published-online` = **1997**。`CITED_SECONDARY`，原文本次未打开）
12. Laurenceau, J.-P., Barrett, L. F., & Pietromonaco, P. R. (1998). Intimacy as an interpersonal process. *JPSP*, 74(5), 1238-1251. `10.1037/0022-3514.74.5.1238`
13. Reis et al. (2018). Perceived Partner Responsiveness Scale (PPRS) 手册章节（**作者全名单本次未逐一核对**）。`https://www.sas.rochester.edu/psy/people/faculty/reis_harry/assets/pdf/reisetal_2018_pprs.pdf`
14. Reis, H. T., & Shaver, P. (1988). Intimacy as an interpersonal process. In Duck (Ed.), *Handbook of Personal Relationships* (pp. 367-389). 2018 重印 `10.4324/9780203732496-5`
15. Crasta, D., Rogge, R. D., Maniaci, M. R., & Reis, H. T. (2021). Toward an optimized measure of perceived partner responsiveness: Development and validation of the perceived responsiveness and insensitivity scale. *Psychological Assessment*. `10.1037/pas0000986`（DOI 经 APA manuscript 记录页确认存在；Crossref 查询未返回 → 标 `UNVERIFIED_DOI`，但论文正文与全部数值已实际读到）
16. Gable, S. L., Reis, H. T., Impett, E. A., & Asher, E. R. (2004). What do you do when things go right? *JPSP*, 87(2), 228-245. `10.1037/0022-3514.87.2.228`
17. Larzelere, R. E., & Huston, T. L. (1980). The Dyadic Trust Scale. *J Marriage and Family*, 42(3), 595-604. `10.2307/351903`
18. Schumm, W. R., Bugaighis, M. A., Buckler, D. L., Green, D. N., & Scanlon, E. D. (1985). Construct validity of the Dyadic Trust Scale. *Psychological Reports*. `10.2466/pr0.1985.56.3.1001`
19. Spanier, G. B. (1976). Measuring dyadic adjustment. *J Marriage and Family*, 38(1), 15-28. `10.2307/350547`
20. Rusbult, C. E., Martz, J. M., & Agnew, C. R. (1998). The Investment Model Scale. *Personal Relationships*, 5(4), 357-387. `10.1111/j.1475-6811.1998.tb00177.x`
21. Rusbult, C. E. (1980). Commitment and satisfaction in romantic associations. *JESP*, 16, 172-186. `10.1016/0022-1031(80)90007-4`
22. Fletcher, G. J. O., Simpson, J. A., & Thomas, G. (2000). The measurement of Perceived Relationship Quality Components. *PSPB*, 26, 340-354. `10.1177/0146167200265007`
23. Stafford, L. (2010). Measuring relationship maintenance behaviors. *J Social and Personal Relationships*, 28(2), 278-303. `10.1177/0265407510378125`
24. Clary, E. G., Snyder, M., Ridge, R. D., Copeland, J., Stukas, A. A., Haugen, J., & Miene, P. (1998). Understanding and assessing the motivations of volunteers. *JPSP*, 74(6), 1516-1530. `10.1037/0022-3514.74.6.1516`
25. **Farrell, A. K., Simpson, J. A., & Rothman, A. J. (2015).** The relationship power inventory: Development and validation. *Personal Relationships*, 22(3), 387-413. `10.1111/pere.12072`（**R3-A3b 引用更正（`R-B13`）**：原误作 "Beach, S. R. H. (2017)"。2026-09-27 直开 Crossref：三位作者均 University of Minnesota；online 2015-03-26 / print 2015-09。abstract 已逐字核对，含 "Study 3 revealed RPI scores predict observer ratings of power during decision-making discussions and showed the RPI has good test–retest reliability"）
26. **Luttrell, T. B., Distelberg, B., Wilson, C., Knudson-Martin, C., & Moline, M. (2017).** Exploring the Relationship Balance Assessment. *Contemporary Family Therapy*, 40(1), 10-27. `10.1007/s10591-017-9421-2`（**R3-A3b 引用更正（`R-B13`）**：原误作 "Lativos et al. (2017)"，且注「作者全名单本次未逐一核对」。2026-09-27 直开 Crossref：五位作者全名单已确认；online 2017-07-20 / print 2018-03。全文未打开）
27. Pincus, A. L., & Wilson, K. R. (2001). Interpersonal variability in dependent personality. *J Personality*, 69(2), 223-251. `10.1111/1467-6494.00143`
28. Hirschfeld, R. M. A., Klerman, G. L., Gouch, H. G., Barrett, J., Korchin, S. J., & Chodoff, P. (1976). A measure of interpersonal dependency. *J Personality Assessment*, 40(6), 610-618. `10.1207/s15327752jpa4106_6`（Crossref 将姓氏截断为 "Hirsh"；Taylor & Francis 页显示 "Robert M.A. Hirschfeld"）
29. Anderson, P. A., John, O. P., & Keltner, D. (2012). The Personal Sense of Power. *J Personality*, 80(2), 313-344. `10.1111/j.1467-6494.2011.00734.x`
30. Keltner, D., Gruenfeld, D. H., & Anderson, P. A. (2003). Power, approach, and inhibition. *Psych Review*, 110(2), 265-284. `10.1037/0033-295x.110.2.265`
31. Spector, I. P., Carey, M. P., & Steinberg, L. (1996). The Sexual Desire Inventory. *J Sex & Marital Therapy*, 22(3), 175-190. `10.1080/00926239608414655`
32. Moyano, N., Vallejo-Medina, P., & Sierra, J. C. (2017). Sexual Desire Inventory: Two or three dimensions? *J Sex Research*, 54(1), 105-116. `10.1080/00224499.2015.1109581`
33. Castro-Calvo, A., Beltrán-Martínez, M., Ballester-Arnal, V., et al. (2024). Cross-cultural validation of the Sexual Desire Inventory (SDI-2) in 42 countries and 26 languages. *J Sex Research*, 63, 755-768. `10.1080/00224499.2024.2417023`
34. Krishnamurti, S., & Loewenstein, G. (2011). The Partner-Specific Sexual Liking and Sexual Wanting Scale. *Archives of Sexual Behavior*, 41, 467-476. `10.1007/s10508-011-9785-6`
35. Chivers, M. L., Seto, M. C., Lalumière, M. L., Laan, E., & Grimbos, T. (2010). Agreement of self-reported and genital measures of sexual arousal in men and women. *Archives of Sexual Behavior*, 39, 5-56. `10.1007/s10508-009-9556-9`
36. Cartagena-Ramos, D., Fuentealba-Torres, M., Rebustini, F., et al. (2018). Systematic review of the psychometric properties of instruments to measure sexual desire. *BMC Medical Research Methodology*, 18, 109. `10.1186/s12874-018-0570-2`
37. Hatfield, E., & Sprecher, S. (1986). Measuring passionate love in intimate relationships. *J Adolescence*, 9, 383-410. `10.1016/S0140-1971(86)80043-4`
38. Sternberg, R. J. (1986). A triangular theory of love. *Psych Review*, 93(2), 119-135. `10.1037/0033-295X.93.2.119`
39. Chojnacki et al. (1990). Reliability and concurrent validity of the Sternberg Triangular Love Scale. *Psychological Reports*, 67, 219. `10.2466/pr0.67.5.219-224`（**第二作者本次未核实**）
40. Graham, J. M., Diebels, K. J., & Barnow, Z. B. (2011). The reliability of relationship satisfaction. *J Family Psychology*, 25(1), 39-48. `10.1037/a0022441`
41. Mayo, O., Lavidor, M., & Gordon, I. (2021). Interpersonal autonomic nervous system synchrony and its association to relationship and performance. *Physiology & Behavior*, 235, 113391. `10.1016/j.physbeh.2021.113391`
42. **Palumbo, R. V., Marraccini, M. E., Weyandt, L. L., Wilder-Smith, O., McGee, H. A., Liu, S., & Goodwin, M. S. (2017).** Interpersonal Autonomic Physiology: A Systematic Review of the Literature. *Personality and Social Psychology Review*, 21(2), 99-141. `10.1177/1088868316628405`（**R3-A3b 引用更正（`R-B13`）**：原误作 "Mønster et al. (2016). … *Soc Personal Relat*"，且注「作者全名单本次未逐一核对」。2026-09-27 直开 Crossref：**七位作者全名单已确认**；`container-title` = **Personality and Social Psychology Review**（非 *Soc Personal Relat*）；online 2016-02-26 / print 2017-05。全文未打开）
43. Nature Reviews Psychology (2026). Correlates of interpersonal physiological synchrony and sources of empirical heterogeneity. `10.1038/s44159-026-00535-4`
44. Brinberg, M., Vanderbilt, R. R., Solomon, D. H., Brinberg, D., & Ram, N. (2021). Using technology to unobtrusively observe relationship development. *J Social and Personal Relationships*, 38(12), 3429-3450. `10.1177/02654075211028654`
45. Sprecher, S., & Metts, S. (1989). Development of the Romantic Beliefs Scale. *J Social and Clinical Psychology*, 6(4). `10.1177/0265407589064001`
46. Rubin, Z. (1970). Measurement of romantic love. *JPSP*, 16, 265-273. `10.1037/h0029841`
47. Reiss, I. L. (1964). The scaling of premarital sexual permissiveness. *J Marriage and Family*, 26(2), 188. `10.2307/349726`
48. Sprecher, S., McKinney, K., Walsh, R. H., & Anderson, C. M. (1988). A revision of the Reiss Premarital Sexual Permissiveness Scale. *J Marriage and Family*, 50(3), 821. `10.2307/352650`
49. Impett, E. A., Strachment, E., Finkel, E. J., & Gable, S. L. (2008). Maintaining sexual desire in intimate relationships. *JPSP*, 94(5), 808-823. `10.1037/0022-3514.94.5.808`
50. Measures of relationship power dynamics in romantic relationships: A systematic review. *J Family Theory & Review*. `10.1111/jftr.70019`（**作者全名单本次未逐一核对**）
51. The Dyadic Adjustment Scale: A reliability generalization meta-analysis. *J Marriage and Family*. `10.1111/j.1741-3737.2006.00284.x`（**作者全名单本次未逐一核对**）
52. Gächter, S., Starmer, C., & Tufano, F. (2015). Measuring the closeness of relationships: A comprehensive evaluation of the 'Inclusion of the Other in the Self' Scale. *PLoS ONE*, 10(6), e0129478. `10.1371/journal.pone.0129478`（**R3-A3b**：作者全名单已由 Crossref + **已打开正文**双路确认；正文另给出 RCI 的 block 结构 3 + 38 + 34 = 75，以及 Rubin Liking / Loving Scale **各 13 题、9 点**；同文概念段又写 RCI 为 "69-item" ⇒ 见 §2.1 注与 `U23`）
53. Trust in close relationships revisited (2025). `https://pmc.ncbi.nlm.nih.gov/articles/PMC12316384/`（**作者与期刊本次未核实**）
54. Development of New Family Caregiving Motivation Scale (2025). *Innovation in Aging*. `https://pmc.ncbi.nlm.nih.gov/articles/PMC12761549/`（作者姓氏 Wang / Yang / Cary / Hendrix 经检索结果确认；**确切题录未核实**）
55. Alessandri, G., Fagnani, C., Di Gennaro, G., et al. (2013). Measurement invariance of the Experiences in Close Relationships questionnaire across different populations. `https://d.docksci.com/download/measurement-invariance-of-the-experiences-in-close-relationships-questionnaire-a_5acc759ed64ab2a9e8109124.html`（**期刊名本次未核实**）
56. Røysamb, E., Vittersø, J., & Tambs, K. (2014). The Relationship Satisfaction Scale — Psychometric properties. *Norsk Epidemiologi*, 24, 187-194. `https://www.ntnu.no/ojs/index.php/norepid/article/view/1821/1818`
57. (2019). The development and validation of an interpersonal distrust scale (doctoral dissertation, Bowling Green State University). `https://stacks.cdc.gov/view/cdc/230061`（**作者本次未核实**）
58. Wildman, J. L., Thayer, A. L., Warren, C., Fiore, S. M., & Salas, E. (2025). Interpersonal trust and distrust at work: Scale validation and theoretical exploration. `https://exa.ai/library/publication/rchtdhlk6gl`（**`UNVERIFIED_DOI`**，年份/作者来自检索元数据）
59. Wheeler, A. R., Ohan, J. L., Jackson, H. M., & Bayliss, D. M. (2025). A systematic review of psychometric properties of general trust measures across the lifespan. `https://exa.ai/library/publication/g32zr4m06b2`（**`UNVERIFIED_DOI`**）
60. Elizabeth, H. S., & Clark, M. A. Tests of measurement invariance for nine relationship relevant scales across straight, gay/lesbian, and bisexual individuals. `https://exa.ai/library/publication/8h8jd1sblrm`（**`UNVERIFIED_DOI`；发表年份/期刊未核实**）
61. Mastrotheodoros, S., Chen, B.-B., & Motti-Stefanidi, F. (2015). ECR-R: Measurement (non-)invariance across Chinese and Greek samples. *EJDP*, 12, 344-358.（**`UNVERIFIED_DOI`**）
62. Hao, J. et al. A cross-cultural examination of the ECR-R-GSF in an Australian and a Chinese sample. *J Relationships Research*. `https://www.cambridge.org/core/journals/journal-of-relationships-research/article/abs/crosscultural-examination-of-the-experiences-in-close-relationships-revised-general-short-form-ecrrgsf-in-an-australian-and-a-chinese-sample/940D0C6FAEE9F9708308AED7C544CAF0`（**`UNVERIFIED_DOI`；年份/卷期未核实**）
63. Structure and measurement invariance of adult romantic attachment: AAQ and ECR-R. `https://pubmed.ncbi.nlm.nih.gov/29206485/`（**`UNVERIFIED_DOI`**）
64. Romantic attachment and relationship functioning in same-sex couples. `https://pubmed.ncbi.nlm.nih.gov/23356467/`（**`UNVERIFIED_DOI`**）
65. Cross-cultural validation of the Arizona Sexual Experience (ASEX). *Archives of Sexual Behavior*. `10.1007/s13178-024-01040-0`（**`UNVERIFIED_DOI`**）
66. Goldhammer, D. L., & McCabe, M. P. (2011). Development and psychometric properties of the Female Sexual Desire Questionnaire. *J Sex Med*, 8, 2512-2521. `https://www.sciencedirect.com/science/article/abs/pii/S1743609515336584`（**`UNVERIFIED_DOI`**）
67. Cues Resulting in Desire for Sexual Activity in Women. `https://pmc.ncbi.nlm.nih.gov/articles/PMC2861288/`（**`UNVERIFIED_DOI`**）
68. Adler, H., & Baeder, K. (2021). Validating the Couple Relationship Skills Inventory. *Family Relations*. `https://www.alabamamarriage.org/assets/uploads/2023/03/Family-Relations-2021-Adler-Baeder-Validating-the-Couple-Relationship-Skills-Inventory.pdf`（姓氏来自文件 URL，**`UNVERIFIED`**）
69. Does Relationship Satisfaction Always Mean Satisfaction? Development of the Couple Relationship Satisfaction Scale. *J Relationships Research*. `https://www.cambridge.org/core/journals/journal-of-relationships-research/article/abs/does-relationship-satisfaction-always-mean-satisfaction-development-of-the-couple-relationship-satisfaction-scale/585E7E514F5D9ADA1EBBD34A3B75429E`（**`UNVERIFIED_DOI`**）
70. Trust and Distrust Scale Development: Operationalization and Instrument Validation (doctoral dissertation, Kennesaw State University). `https://digitalcommons.kennesaw.edu/cgi/viewcontent.cgi?article=1043&context=dba_etd`（`CITED_SECONDARY`，非同行评审）
71. "Companionate Love Scale"（数据集记录，**作者字段为空 → 原始出处 `UNKNOWN`**）。`10.13072/midss.484`
72. Eisert, B. C., Anderson, J. R., & Portillo, M. F. (2026). The Hurlbert Index of Sexual Desire-Short Form. *Archives of Sexual Behavior*. `10.1007/s10508-026-03487-1`（**`UNVERIFIED`**，Crossref 未核）
73. McCroskey, J. C. (1985). Willingness to Communicate. ERIC ED265604. `https://files.eric.ed.gov/fulltext/ED265604.pdf`
74. Griffin, D., & Bartholomew, K. (1994). Relationship Scales Questionnaire 描述页. `https://scales.arabpsychology.com/s/relationship-scales-questionnaire-rsq/`（**`UNVERIFIED_DOI`**）
75. Winczewski, Bowen, & Collins (2014). Compassionate love for a romantic partner facilitates empathic accuracy. `10.1037/e512142015-146`（**`UNVERIFIED_DOI`；全名单未逐一核对**）
76. Neto (2012). Compassionate Love for a Romantic Partner, Love Styles and Subjective Well-Being. *Interpersona*, 6, 23-39. `10.5964/ijpr.v6i1.88`

**说明**：第 12、13、39、50、51、54、55、58、59、60、62–70、72、75、76 条的**完整作者名单或期刊卷期本次未逐一核对**，已在条目内显式标注。**R3-A3b 取消**第 26、42、52 三条的「作者全名单未逐一核对」标注（已由 Crossref 直开确认）。所有"当前可得性 / 当前版本"判断截至 **2026-09-27**。

**R3-A3b 增补（目录增补；题录已于 2026-09-27 由 Crossref 直开确认，全文均未打开）**

78. Fraley, R. C., Heffernan, M. E., Vicary, A. M., & Brumbaugh, C. C. (2011). The experiences in close relationships—Relationship Structures Questionnaire: A method for assessing attachment orientations across relationships. *Psychological Assessment*, 23(3), 615-625. `10.1037/a0022898`（**`A15` ECR-RS**。Crossref: `title` / 四位作者 / volume 23 issue 3 pages 615-625 / 2011 全部一致。funder NSF 0443783。**全文未打开** ⇒ 除题数外不附任何心理计量数字）
79. Fraley, R. C., Vicary, A. M., Brumbaugh, C. C., & Roisman, G. I. (2011). Patterns of stability in adult attachment: An empirical test of two models of continuity and change. *JPSP*, 101(5), 974-992. `10.1037/a0024150`（**`A16`**。Crossref: `title` / 四位作者 / **volume 101 pages 974-992** / 2011 全部一致。funder NSF BCS-0443783（与 ref 78 同一项目）。**全文未打开** ⇒ **不主张**其判别结果方向；见 `U18`）
80. **Perceived Inclusion Scale (PICS)** —— **`NOT_OPENED`**。2026-09-27 Crossref 三次检索（`query.title="Perceived Inclusion Scale"` / `query.bibliographic` 含 `closeness accommodation` / PsycTESTS 域）**均未命中可确认题录**；`https://www.psychology.unl.edu/williams/PerceivedInclusion.html` 抓取报 `Transport error`。⇒ 无题数、无 α、无年份、无 DOI。见 `U25`

---

## 8. lane 结论（R3-A3b 重写；旧 §8 的计数与指针断言被取代，见 §9 `supersessions` S-03-3）

- **计数（唯一有效口径见 §2 口径表）**：`catalogue_rows` = **73**；`distinct_instrument_or_family` = **66**；`separately_citable_instrument_entries` = **57**；`NOT_ASSESSED` = **13**。
  - **旧版「41 个独立 instrument family / 54 个可引用条目」不可复现，已废止。** 依 review-r2 `R-C10`：**41/54 不得进入任何 canonical 依据。**
- **指针完整性（更正）**：旧版称「**全部带真实指针**（DOI、官方记录或可访问原文页）」。**该断言为假**：§2.10 登记的 **13 条** `NOT_ASSESSED` 中，**至少 5 条**没有可解析的 DOI 或官方记录 —— `S2`（**原刊无 DOI**）、`S5`（DOI `UNVERIFIED`）、`T7` / `T8`（仅 exa.ai 检索元数据 URL）、`A6` / `A7` / `A8` / `A9`（`UNVERIFIED_DOI`）、`C6`（`UNVERIFIED_DOI`）、`D4` / `D5`（`AGENT_RECALL`，**纯凭记忆写出的卷期页码**）、`X4`（仅剑桥摘要页）、`A17`（`NOT_OPENED`）。**新表述：本目录中「指针已解析」与「指针仅为检索元数据 / 无指针」的行必须分别标注；本文件不再给出「全部带真实指针」这类全称断言。**
- **分类分布（R3-A3b 后）**：`NOT_IDENTIFIABLE` 由旧版 **9 条**降至 **1 条**（`X8` 生理同步，且已补上其显式结构论证）；新增 `LAYER_MISMATCH`（7 条：`D3` / `O3` / `O4` / `O5` / `X14` / `X15` + `ECR-R` 族的层级说明）、`NOT_ASSESSED`（13 条，见 §2.10）、`DEFECTIVE_INSTRUMENT`（1 条，`C4`）。`SEARCH_INCOMPLETE` 作为**概念**在 §4.1 的 D6 / D7 / D8 行使用（以 `RECLASSIFY_AS_METHOD_LIMIT` 措辞承载）。
- **降级建议**：**`D7 Dedication` 与 `D8 OutcomeDependence` 的两条降级建议已整体撤回**（`RECLASSIFY_AS_METHOD_LIMIT`）。两条**保持 candidate**（依 adjudication **X-3** / **X-4**）。
- **`D4 open question（Distrust）`**：由「升级为独立候选」改为 **`HOLD_FOR_EVIDENCE`**。
- **10 项 instrument gap**（G1–G10）保留；**G9 已按 §4.2 Q1 收窄**，并由「**架构级 gap**」降为「**开放技术问题**」。
- **12 项 negative result / contradiction**（N1–N12）保留。
- **3 项需 Architect 裁决的架构问题**（Q1–Q3）保留；Q1 的举证方向已反转。
- **9 项给其他 lane 的直接输入**保留（两条已加范围限定）。
- **目录增补**：`A15` ECR-RS · `A16` Fraley et al. 2011 · `A17` PICS（`NOT_OPENED`）。**增补为目录行为主，不构成 ontology 变更。**

**`status_recommendation: PARTIAL_SUCCESS`（R3-A3b 改写；旧版 `SUCCESS` 被取代，见 §9 S-03-3）**

理由：Work Order 的检索目标已达成且未 filler，`03` 仍是一份有价值的工具台账。**但 R3-A3b 撤销旧版的 `SUCCESS`**，因为该判定建立在一组**现已失效的计数与判定**之上（41/54 不可复现；9 条重载的 `NOT_IDENTIFIABLE`；两条针对 canonical candidate 的越权降级建议；一处错误锚定的 canonical 引用；一条由两个未打开来源串成的状态转移；四处传播性引用错误）。

**该改写不改变本文件对 LHRM 最有价值的那条观察，但改变它的措辞与责任归属**：本目录**没有** relation-level `Dedication` 与 `OutcomeDependence` 工具，**也没有**带 pair-level 关系特异自陈信念 + 独立观察/生理双通道的 relation-level directed coordinate。**这三条是关于本目录覆盖面的测量学事实，是待补的研究输入（`SEARCH_INCOMPLETE`），不是对 `D7` / `D8` 层级地位的裁决，也不是对 `Reality != Observation != Belief` 三分在测量学上可否实现的结论。** Architect 需要知道的是**条件**（补检索、或自建 measurement layer），而不是**判决**。

---

## 9. R3-A3b 取代记录（`supersessions`）

> 契约 §3.7 要求：被裁决取代的旧文本逐条列出「原文 + 取代依据」。以下为完整清单，供 parent 生成 `SUPERSEDED_BY_REPAIR` 标记。**原文本均已在正文相应位置以引用块或表格行逐字保留。**

| id | 位置 | 被取代的原文（逐字） | 取代依据 | 落地形态 |
|---|---|---|---|---|
| **S-03-1** | §1.2 | 「`NOT_IDENTIFIABLE` \| 现有工具在结构上无法支撑 LHRM 需要的那个坐标（不因为"还没人做"，而是因为"这样做不了"）」—— 被一个**同时承载 4 种不同理由**的分类取代 | adjudication §C item 6（"Search failure/access restriction is not ontology evidence"）；review-r2 `R-0.5` / `B-C4` `CONTESTED`；派工 item 1 | §1.2 重写为 8 类 + 2 条记账规则；新增 `LAYER_MISMATCH` / `SEARCH_INCOMPLETE` / `DEFECTIVE_INSTRUMENT` / `NOT_ASSESSED` |
| **S-03-2** | §2 抬头 | 「**41 个独立 instrument family / 54 个可引用条目。** 短版、修订版、跨文化再验证并入母族并在备注中注明。」 | review-r2 `R-C10`（`B-C1` `UNSUPPORTED`；实测 **73 行**、**≥6 处**重复未标注；"**41/54 不得进入任何 canonical 依据**"） | §2 抬头替换为显式口径表：`catalogue_rows=73` / `duplicate=7` / `distinct=66` / `non_instrument_evidence=9` / `separately_citable=57` / `NOT_ASSESSED=13` |
| **S-03-3** | §8 | 「**统计**：41 个独立 instrument family / 54 个可引用条目，**全部带真实指针**（DOI、官方记录或可访问原文页）。」+「`status_recommendation: SUCCESS`」 | 计数：同 S-03-2；指针：review-r2 `R-C9`（`B-C15` `UNSUPPORTED`，"至少 5 条没有"） | §8 重写：计数指向 §2 口径表；指针改为逐条区分「已解析」/「仅检索元数据」/「无指针」；`status_recommendation` → `PARTIAL_SUCCESS` |
| **S-03-4** | §4.1 | 「D7 Dedication \| **降级为 `NOT_IDENTIFIABLE` 直到自建工具**；IMS 只能作为 `DERIVED` 混合读出」/「D8 OutcomeDependence \| **降级为 `NOT_IDENTIFIABLE`**；两端（dependence 工具、power 工具）皆空」 | adjudication §C item 6 + **X-3** + **X-4**；review-r2 `R-0.5`（`B-C4` `CONTESTED`；"**两条降级建议整体打回**"）；派工 top_rec 第 1 条 `RECLASSIFY_AS_METHOD_LIMIT` | 两条改为 `KEEP`（维持 candidate）+ `RECLASSIFY_AS_METHOD_LIMIT`；旧文本在 §4.1 前的裁决块中**逐字引用保留**；D8 的实质观察（两端的具体工具状态 + `O8` 为最接近读出）**保留** |
| **S-03-5** | §4.1 | 「D4 open question（Distrust） \| **升级为独立候选**，理由从"待测"改为"**78% 共存的直接证据 + trust/distrust 分别测量的工具化路径**"」 | adjudication **X-4**（`Trust` / `AttachmentSecurity` 保持分离候选，须待 M2 式证据）；review-r2 §R-0（两个未打开来源串成的 canonical 状态转移） | 改为 **`HOLD_FOR_EVIDENCE`** + 复通条件（§2.4 末专段） |
| **S-03-6** | §4.2 Q1 | 「本 packet 的最重要发现是 **G9：没有任何已验证坐标同时拥有自陈信念通道与行为/生理独立通道**。LHRM 当前的 `Reality != Observation != Belief` 三分在**测量学上没有现成实现**。」 | review-r2 `R-C14`（`B-C11` `WRONG-SCOPE`；"**按字面为假**"）；adjudication **X-14** | 收窄为「在本目录已检索的范围内，没有任何 **relation-level directed coordinate** 同时拥有 **pair-level、关系特异的自陈信念通道**与**一条独立的观察 / 生理通道**」；「架构级 gap」→ 「**开放技术问题**」；举证方向反转；缺失检索挂 `U21` |
| **S-03-7** | §3.3 | 「**fallback 指令 = 静默伪造 target** \| … **违反 `CURRENT_ARCHITECTURE.md` §9 与 `AGENTS.md` 的 Unknown 保留原则**」 | review-r2 `R-0.7`（`B` top_rec 第 6 条 `CONTESTED`；`AGENTS.md` 那条**保留**但表述改为「工具的 inability **不构成对该状态的合法表示**」）；adjudication **X-14** | §3.3a 新增专段：重新锚定到 `CURRENT_ARCHITECTURE.md` **§3** `Reality != Observation != Belief` + **§9 原则 1** + **§10 `unknown` 事实状态**；ECR trait 语言改判为「**诚实标注 Agent 层 scope**」，不再是「静默伪造 target」；旧行**逐字保留**于 §3.3a 表首 |
| **S-03-8** | §3.3 | 「**求值者/施测者效应** \| **Stafford (2010) 判定两个广泛使用的关系维持量表有 "fundamental measurement flaws"**（S34）；**Schumm et al. (1985) 判定 DTS 测的是 benevolence 而非 trust**（S18）…」 | 派工 item 7（"其两个前身有 fundamental measurement flaws、**在正确 item construction 下**不可用" ⇒ 属**量表题项构造缺陷**） | `Stafford (2010)` **移出**该行，**移入**新建的「**量表题项的构造缺陷（scale item construction defect）**」行；并写明它对 `C4` 产生 `DEFECTIVE_INSTRUMENT`（工具级）、对任何构念**不**产生判定 |
| **S-03-9** | §2.1 `L2` | 「self-report，**10 题**」+「**Frequency 与 Diversity 是弱信度分量，等权入 total 会引入大量不可区分误差**」 | review-r2 `R-B13`（`B-C7` `CONTESTED`；应为 **75 题**；派生结论须相应重述） | 改为 **75 题**（3 + 38 + 34，附 `U23` 的 69/75 冲突限定）；派生结论撤回并改述为**表长与计分粒度**问题；分量级 α 标 `NOT_REVERIFIED_HERE` |
| **S-03-10** | §2.8 `O1` / §7 ref 25 | 「**Beach (2017)**, *Personal Relationships*，`10.1111/pere.12072`」 | review-r2 `R-B13`（`B-C6` `CONTESTED`） | **Farrell, Simpson & Rothman (2015)**, *Personal Relationships* 22(3):387-413（Crossref 直开确认） |
| **S-03-11** | §2.8 `O2` / §7 ref 26 | 「**Lativos et al. (2017)**, *Contemporary Family Therapy*，`10.1007/s10591-017-9421-2`」 | 同 S-03-10 | **Luttrell, Distelberg, Wilson, Knudson-Martin & Moline (2017)**, *Contemporary Family Therapy* 40(1):10-27（Crossref 直开确认） |
| **S-03-12** | §2.5 `A13` / §3.2 / §4.3 / §7 ref 11 | 「**Pietromonaco & Laurenceau (1998)**, *JPSP* 73(6):1409-1423, `10.1037/0022-3514.73.6.1409`」（共 4 处） | review-r2 `R-B13`（`B-C6` `CONTESTED`） | **Pietromonaco & Barrett (1997)**（Crossref 直开：`author` = Pietromonaco + Barrett；year 1997） |
| **S-03-13** | §2.9 `X8` / §7 ref 42 | 「综述 **Mønster et al. (2016)** `10.1177/1088868316628405`」/「Mønster et al. (2016). … *Soc Personal Relat*.」（共 2 处） | review-r2 `R-B13`（`B-C7` `CONTESTED`；应为 **Palumbo et al. 2017, PSPR 21(2)**） | **Palumbo, Marraccini, Weyandt, Wilder-Smith, McGee, Liu & Goodwin (2017)**, *Personality and Social Psychology Review* 21(2):99-141（Crossref 直开确认，含期刊名） |
| **S-03-14** | §2.3 `S8` | 「**结论：不存在性别对称的、由自我报告锚定的性唤起通道。** LHRM 若把 `SexualDesire_(i->j)` 当可观测 latent，必须承认女性方向上只有一条弱通道」 | adjudication **X-14**；派工 item 8（"必须标为 scope-limited laboratory-arousal finding, not a general statement"） | 改为**实验室唤起范式内**的 scope-limited 表述，并显式列出三条不主张。`S8` 的**全局层归属保留** |
| **S-03-15** | §2.8 `O6` | 「**38 个有名有姓的 power/equity/balance 量表各自仅被用 1–2 次，无一成为主流工具**」+「**本 packet 对 `OutcomeDependence` 最重的一份证据：整个工具族不可比**」 | adjudication **X-14**；派工 item 8（"五个具体数字未验证 → `HOLD_FOR_EVIDENCE`，**不得**成为 D8 降级的承重支柱"） | 三个具体数字全部标 `HOLD_FOR_EVIDENCE`；「无一」即使核实为真也只能表述为该审计覆盖范围内的结果；「最重的一份证据」定位撤回；方法学警示方向保留为 `PLAUSIBLE`；挂 `U26` |
| **S-03-16** | §3.4 跨表结论 | 「…而 LHRM 最缺的三个（Dedication、OutcomeDependence、Cohesion）恰好是**零证据**。这是一个不应被"文献量"掩盖的结构性问题。」 | adjudication **X-14**；review-r2 `R-D25`（同型处置：把"零证据"改为"**本 packet 未检出**"） | 改为「**在本目录已检索的范围内**没有不变性证据条目」，并显式声明**既不主张该命题成立也不主张其反面**；保留可辩护的**覆盖—需求错位**观察（不需字段级否定） |
| **S-03-17** | §2.5 `A12` / §3.1 类 1 / §3.2 / §4.1 D5 | 「`ECR` 族全部属 target slot 结构上为空」；「主流工具是 trait；**唯一** state 指针是 Overall & Sibley (2009)」 | 派工 item 3（ECR-RS 与 Fraley et al. 2011 "**直接**证伪 'only one directionally correct tool' 与 'only state pointer' 两条主张"） | §2.5a 增补 `A15` / `A16` / `A17`；四处「唯一」措辞**逐处加限定并注明被推翻** |
| **S-03-18** | §2.5 `A9` | 「`UNVERIFIED_DOI`（见 **§1.4** 与 U 列）」 | 内部一致性：本文件**不存在 §1.4** | 改为指向本表 + §2.10 + §6（`U22`） |
| **S-03-19** | 全文 | 原文件**无**取代机制；superseded 文本会被静默覆盖 | `AGENTS.md` "Do not erase old evidence merely because a newer model supersedes it"；契约 §3.7 | 新增本 §9；全部旧文本以**引用块 / 表格行逐字保留** + 本表给出取代依据 |
