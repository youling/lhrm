# R3-G 四类 dyad 的下一批 fixture 来源规划 v0.1

- work_coordinate: `youling/lhrm#30@round3-adjudication-implementation-v1`
- child: `G`（Round-3 build child，Track R3-G）
- 权威裁决: `#30 comment 5854920569`（`ARCHITECT_ADJUDICATION_V1`）
- 权威 dispatch: `#30 comment 5854930069`（`ARCHITECT_ROUND3_DISPATCH_V1`）
- 状态: **SOURCE PLANNING ONLY / NO DATA ACQUIRED / NO FIXTURE FROZEN**
- 探针日期: `2026-09-27T20:45:30Z`（本文所有 access 观察均来自这一次 run）
- 本文件不修改任何 canonical 文件，不修改 validation-corpus / gate 文档。

> 本文件是**规划**。未下载任何数据，未做 bulk acquisition，未绕过 auth/licence/robots，
> 未运行任何 gate 或 fixture mapping，未读/未执行/未引用 `#20`/`#21`/`#22`。

---

## 1. 记账口径（沿用兄弟轨 C 的 SSOT，本文不复制其定义）

本轨只做**来源规划**，因此不新建 taxonomy、不新建 cell 表。下列口径全部**引用**兄弟轨
`docs/foundation/VALIDATION_GATES_V0_2.md`（child `C`）的定义，本文不重复定义以免出现第二份 SSOT：

- 抽样框分类法 = `HD-ST-1`（`dyad_class` · `gender_composition` · `stage`）
- Table A 抽样框 cell = `HD-A01…HD-A15`；本文只触及
  `HD-A01` sibling、`HD-A02` parent–adult-child、`HD-A04` non-romantic friendship、`HD-A12` same-sex core dyad
- 覆盖列三值 = `PRESENT` / `CRITERION_DEPENDENT` / `ZERO_IN_AUDITED_CORPUS`（X-14 检索范围陈述，非存在性陈述）
- 门处置 = `KEEP | MERGE | DERIVE | REJECT | HOLD`；`HOLD_REASON ∈ {EVIDENCE_MISSING, ACCESS_OR_RIGHTS, BENCHMARK_NOT_BUILT, CRITERION_UNDEFINED, CONTESTED}`

**X-10 双层记账在本轨的位置**：层 1（canonical 清单对齐）不属本轨；**层 2（经验语料覆盖）才是本轨的交付物**。
本文只回答「哪些 lawful/stable 的候选来源可以补上这四类」，**不**回答「补齐之后这四类就被表示了」。

## 2. 本轨自定义的两个词表（仅用于来源规划，不进入 ontology）

### 2.1 `rights_status`（rights fail closed：只能变严，不能变松）

| 值 | 判据 | 可否作 fixture 来源 |
|---|---|---|
| `RIGHTS_CLEARED_AI_OK` | 观察到的 licence 字符串逐字含机器处理许可、**且无 `NoDerivatives` 子句** | 可 |
| `RIGHTS_CLEARED_CONDITIONAL` | 观察到的 licence 含 `NonCommercial` 或等价约束 | 仅在约束内可；**默认不得把衍生物入仓** |
| `RIGHTS_LICENCE_REQUIRED` | 来源方明示「computational analysis 需另行申请许可」 | 否（除非拿到许可） |
| `RIGHTS_ROBOTS_RESERVED` | 观察到机器可读的 AI 保留（`X-Robots-Tag: noai` / robots.txt AI 名单） | 否（不得绕过） |
| `RIGHTS_NOT_CLEARED` | 页面上**未观察到**任何开放 licence 字符串 | 否（fail closed） |
| `HUMAN_REVIEW_REQUIRED` | 沿用 Fixture 003 已记录状态 | 否；**任何观察都不得升级它** |

**Never-upgrade 规则（本文硬规则）**：`robots.txt` 变化、页面可达性变化、站点改版，**都不构成** rights 升级依据。

### 2.2 `access_status`（失败按失败记录）

`ACCESS_OK` · `ACCESS_LOGIN_WALL` · `ACCESS_403` · `ACCESS_MEMBERSHIP` · `ACCESS_PARTIAL` · `ACCESS_UNAVAILABLE_FROM_HERE`

---

## 3. 阻断性发现：Find Case Law 对本项目的 LLM 用途**不可用**（rights fail closed）

这是本轨最重要的发现，直接改变四类来源规划的形状，因此放在候选之前。

**观察（`2026-09-27T20:45:30Z`，逐条可复算）**：

1. `https://caselaw.nationalarchives.gov.uk/robots.txt` → HTTP 200，674 bytes。内容含
   `User-agent: GPTBot / ChatGPT-User / Google-Extended / PerplexityBot / Amazonbot / ClaudeBot / anthropic-ai /
   Claude-Web / Bytespider / Diffbot / Omgilibot / Omgili / YouBot / FacebookBot / Applebot` 全部 `Disallow: /`；
   仅 `User-Agent: *` 为 `Allow: /`。**AI/训练类爬虫被点名排除。**
2. 判决文档页响应头含 **`X-Robots-Tag: noindex, nofollow, noai`**
   （在 `ewhc/ch/2025/1367`、`ewca/civ/2008/904`、`ewca/civ/2018/2669`、`ewca/civ/2019/890`、
   `ewhc/ch/2024/2685`、`ewhc/ch/2024/2729` 六份上**逐一观察到**）。
3. `https://caselaw.nationalarchives.gov.uk/terms-and-policies` → HTTP 200，17012 bytes。逐字：
   > "You may use and re-use the contents of the Find Case Law service under the terms of the Open Justice Licence.
   > You must apply for a licence to do computational analysis if you wish to conduct computational analysis of the
   > information provided by Find Case Law."

**结论（rights fail closed）**：`Open Justice Licence` 的「可再利用」**不覆盖**本项目的核心用途
（把判决文本交给 mapping agent 做逐单位映射 = computational analysis），且站点同时做了机器可读的 AI 保留。
**因此 Find Case Law 在本项目中被判为 `RIGHTS_LICENCE_REQUIRED` + `RIGHTS_ROBOTS_RESERVED`，
不得作为任何新 fixture 的来源，除非先取得书面许可。本轨不绕过、不申请、不推断许可。**

**⚠ 与既有冻结材料的冲突（交回 parent，不自行修改）**：
`docs/validation/VALIDATION_CORPUS_V0_1.md` 的 `L2-001`（`Sharland v Sharland [2015] UKSC 60`，
`https://caselaw.nationalarchives.gov.uk/uksc/2015/60`）把权利记为
「UK Crown copyright / Open Justice Licence；free access and re-use with attribution per National Archives terms」，
**未记录**上述 `X-Robots-Tag: noai`、robots.txt AI 名单与「computational analysis 需申请许可」这三条。
该文件不属本轨白名单（归 Track R3-A / child `A`），**本轨一个字未改**，只在本节记录并路由。

---

## 4. 四类 × 候选来源（逐源五项记录）

`contains` / `access` / `rights` / `stability` / `still_not_enabled` 五项**分别**记录，不合并。
`both-party` = 双方各自报告；`multi-t` = 多个时间点；`directional` = 可读出方向。

### 4.1 sibling（`HD-A01`）

#### `S1` — `PMC11219362` · DOI `10.1007/s10508-024-02832-6` · *The Impact of Sibling Relationships on Behavioral and Sexual Health among Latino Sexual Minority Men*

| 项 | 记录 |
|---|---|
| contains | 混合方法；**dyadic qualitative interviews**，被访者是「一个 Latino 性少数男性 + 他信任的一位 sibling」；两位 sibling 被问**相同的问题**。原文可见双向发言：「At the end of the day he is my best friend, and it was nice to be able to talk to him about PrEP, so that he can trust me.」（按 `PMCID` 页面转录）。`both-party = YES`；`multi-t = PARTIAL`（`Impact of the Study Interview` 一节显示访谈**后**关系被参与者自述为改变，但非等距时间点）；`directional = YES`（弟弟说「我哥哥是直男，我以为聊 PrEP 会很别扭」→ 支持/提醒的方向由谁发起是可见的） |
| access | `ACCESS_OK`。2026-09-27 探针 HTTP 200 / `text/html; charset=utf-8` / 237633 bytes；无 `X-Robots-Tag`。`pmc.ncbi.nlm.nih.gov/robots.txt`：`User-agent: *` 组内 `Allow: /articles/` 与 `Disallow: /`，按最长匹配规则 `/articles/` 放行，且**无任何 AI 专用 UA 段** |
| rights | 页面逐字：`Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made` ⇒ `RIGHTS_CLEARED_AI_OK`（**无 `NoDerivatives`**）。**但见 §5 参与者同意的残留问题** |
| stability | 稳定：`PMCID`（`PMC11219362`）+ `DOI`（`10.1007/s10508-024-02832-6`）双标识；期刊为 `Archives of Sexual Behavior`（Springer Nature）。**注意**：本轨只观察到**当前**页面字节数，未逐次核对跨时间不变；「版本化/冻结发布」这一点**未被证实**，只证实了持久标识符 |
| still_not_enabled | ① 不提供 `t` 序列的等距 longitudinal 结构（只有一次访谈 + 一次回溯）；② 主题被限定在 HIV/PrEP 防治语境，**关系状态的其余维度不在材料内**；③ 材料本身已被研究者**编码过**（thematic analysis），取用时必须区分「参与者的话」与「作者的主题标签」，否则会把二手概括当一手报告；④ 不含 `RomanticAttraction`/`SexualDesire` 的 sibling-dyad 证据（兄弟情谊不是这些 construct 的 dyad class） |

#### `S2` — `PMC10068502` · DOI `10.1177/23333936231162230` · *Filling the Void: The Role of Adult Siblings Caring for a Brother or Sister With Severe Mental Illness*

| 项 | 记录 |
|---|---|
| contains | 叙事诠释学（narrative hermeneutic），对 2 位成年手足的访谈做二次分析，两篇文本（Alice / Jon）都进材料。`both-party = YES`（两位不同 sibling 各自讲述，但**不是同一个 dyad 的双方**——原文明确 Alice 与 Jon 是两位被试，Alice 的姊妹 Linn 与 Alice 是真正的 dyad）。`multi-t = YES`（原文自述「had taken care of her younger sister Linn with SMI since they were young adults」「monitored Linn's treatment and care through the years」）→ **可读出跨年序列，但只由一方叙述**。`directional = PARTIAL`（Alice → Linn 的照护方向明确；Linn 侧只有 Alice 的转述） |
| access | `ACCESS_OK`。2026-09-27 探针 HTTP 200 / 272065 bytes |
| rights | 页面逐字检出 `Creative Commons Attribution 4` + `creativecommons.org/licenses/by/4.0/` ⇒ `RIGHTS_CLEARED_AI_OK`（无 `NoDerivatives`）。**见 §5** |
| stability | `PMCID` + `DOI` 双标识；期刊 `Journal of Humanities in Healthcare`。同 `S1`：**未证实**跨时间字节不变 |
| still_not_enabled | ① 严格说**不提供同一条 dyad 的双方报告**（Alice 与 Jon 是两个 sibling 被试；Alice↔Linn 只有一方口述）——**若 `HD-A01` 要求 core dyad 双方都在场报告，本条不满足**；② 只覆盖「照护型手足」，不含非照护型 sibling dyad；③ 二手分析文本（`narrative hermeneutic` 的成文叙述），取用前须区分作者叙述与参与者引语；④ 敏感内容严重（严重精神疾病、寄养安置、自杀/暴力风险），不满足 corpus 的 sensitive-content 规则，须专门 human-review |

#### `S3` — `Rogers v Andrew Wills [2025] EWHC 1367 (Ch)` · `https://caselaw.nationalarchives.gov.uk/ewhc/ch/2025/1367`

| 项 | 记录 |
|---|---|
| contains | 庭审记录。核心 dyad：**姐姐（claimant）对一个 sibling（被告，已故母亲遗产的 executor）**，争点是「为母亲照护所花的费用能否从遗产中受偿」。判决书逐字包含**双方的可引述通信**（例如被告方 WhatsApp：「Make sure that you are taking money for extra heating, food etc etc」（2018-02-16 21:48:26）；被告方邮件：「You are due payment for Mum's care and this has never been disputed. However, the costs for care have to be discussed and agreed once we see a complete breakdown of your estimate...」）。`both-party = YES`；`multi-t = YES`（约 2017-10 / 2018-02 / 2018-10 / 2020-06-01 / 审理）；`directional = YES`（谁在要求、谁在承诺、谁在质疑，都落在不同时间点的不同文本上） |
| access | `ACCESS_OK`（页面 200 / 316995 bytes），**但同时** `X-Robots-Tag: noindex, nofollow, noai`（见 §3） |
| rights | `RIGHTS_LICENCE_REQUIRED` + `RIGHTS_ROBOTS_RESERVED`。**这不是 `ACCESS` 问题，是 rights 问题；不得用「页面能打开」推断可用** |
| stability | 稳定：`Neutral Citation Number [2025] EWHC 1367 (Ch)` + Find Case Law 持久 URL。但站点自 2022-09 起为每份判决提供 `last verified` 日期戳（本次未在页面 HTML 匹配到该串，**未证实**） |
| still_not_enabled | ① 法院逐字声明它**不裁断**关系维度：「The moral position of any of the parties or their siblings is simply irrelevant.」「The court does not adjudicate... on questions as to whether one sibling has behaved better or worse towards the other siblings or their mother」。⇒ 这份材料**只提供「谁做了什么/说了什么」**，把它读成 `Trust`/`Caregiving`/`Dedication` 的真值是**类别错误**；② 遗产/金钱语境天然偏向 `OutcomeDependence`，对 `Liking`/`AttachmentSecurity` 几乎无信息；③ 引入已故母亲作为第三方，使 dyad 实际为三方 |

#### `S4` — `Lifely v Lifely [2008] EWCA Civ 904` · `https://caselaw.nationalarchives.gov.uk/ewca/civ/2008/904`

| 项 | 记录 |
|---|---|
| contains | 兄弟（Andrew / Nicholas）之间的继承与农场合伙之争。`both-party = YES`（双方证据均被记录与评断）；`multi-t = YES`（1980s 合伙、1990 会议、2006-09-07 一审、2008 判决）；`directional = YES` |
| access | `ACCESS_OK`（200 / 74308 bytes）+ `X-Robots-Tag: … noai` |
| rights | 同 `S3`：`RIGHTS_LICENCE_REQUIRED` + `RIGHTS_ROBOTS_RESERVED` |
| stability | `Neutral Citation Number [2008] EWCA Civ 904` + 持久 URL |
| still_not_enabled | ① 判决书自述其**能力边界**：「one hopes that the judgment of the court will at least bring an end to the wrangling, if not to the continuing reverberations of the fractured relationships and the wounded feelings」⇒ 同 `S3` 的类别错误风险；② 全部争议集中在合伙账目与继承，`Liking`/`RomanticAttraction`/`SexualDesire` 无材料；③ 「未供证的书信/日记」是**缺席证据**（`Nicholas's diary`），映射时须留在 `Provenance/Uncertainty`，不得当成「没发生」 |

### 4.2 parent–adult-child（`HD-A02`）

#### `P1` — `PMC12101125` · DOI `10.3389/fpsyg.2025.1551953` · *The impact of the reaction to diagnosis on sibling relationship: a study on parents and adult siblings of people with disabilities*

| 项 | 记录 |
|---|---|
| contains | 自我报告问卷（e-survey），**365 个 parent–sibling dyads**；家长 `M age = 51.2`（range 25–64），typically-developing sibling `M age = 23.2`（range 18–39）。双方皆为成年人 ⇒ 满足「parent–**adult**-child」。逐字可见双向条目（子方对「与父母的不独立」项；父母对「应对诊断」的反应项），并有 parent–sibling 双向模型对比。`both-party = PARTIAL`：**两方各自填表，但不是在同一对话里互相报告**；`multi-t = NO`（横断面）；`directional = PARTIAL`（各自报告自己这一侧，**无配对方向读**） |
| access | `ACCESS_OK`。2026-09-27 探针 HTTP 200 / 299100 bytes |
| rights | 页面逐字检出 `Creative Commons Attribution License (CC BY)` ⇒ `RIGHTS_CLEARED_AI_OK`。**见 §5** |
| stability | `PMCID` + `DOI`；`Frontiers in Psychology`。同前：**未证实**跨时间字节不变 |
| still_not_enabled | ① **不是双方互报**，也不是 longitudinal ⇒ 只能覆盖 `HD-A02` 的**存在性**，不能支撑任何需要「同一 dyad 两方向随时间」的设计；② 报告的「parent–sibling」是**被试组合名**，不必然是母子/父女；③ 全部是量表分与结构方程路径，**不是关系状态的叙述**——用它做 fixture 会把「被试的模型」当「关系的事实」；④ 主题（残障诊断）触发 corpus 的敏感内容规则 |

#### `P2` — `PMC8611109` · DOI `10.1177/07334648211016113` · *"I'm Getting Older Too": Challenges and Benefits Experienced by Very Old Parents and Their Children*

| 项 | 记录 |
|---|---|
| contains | **设计是本轨在所检索范围内找到的最贴近 parent–adult-child 双向材料的一份**：114 个 parent–child dyads（parent `age ≥ 90`，child `age ≥ 65`），**parent 与 child 分别单独面访**，各约两小时；半结构式，混合开放式质性问答与「parent-child relationship」标准化量化评估；并用 McNemar 检验做**父报 / 子报的方向对比**（页面上可见成对的 `Parent reported` / `Child reported` 行）。`both-party = YES`；`multi-t = NO`（单时点，但同一单位内含**双向**）；`directional = YES`（父母视角与子女视角的差异被显式对照） |
| access | `ACCESS_OK`。2026-09-27 探针 HTTP 200 / 228123 bytes |
| rights | **未在 PMC 页面上检出任何 Creative Commons 字符串** ⇒ `RIGHTS_NOT_CLEARED`。期刊为 SAGE（`The Gerontologist` 系）。**rights fail closed：不得因「是 PMC 免费全文」而当作开放许可。** |
| stability | `PMCID` + `DOI` 稳定 |
| still_not_enabled | ① **在拿到书面许可之前根本不能用**；② 极老样本（parent ≥ 90）——`RomanticAttraction`/`SexualDesire` 在该 dyad 结构上接近 `NOT_APPLICABLE`，这既是**优势**（ applicability 轴）也是**限制**；③ 单时点；④ 被试含认知/生理衰退，映射时须把「健康事件」与「关系状态」分开 |

#### `P3` — `Roger Moore v Stephen Moore & Till Valley Contracting Ltd [2018] EWCA Civ 2669` · `https://caselaw.nationalarchives.gov.uk/ewca/civ/2018/2669`

| 项 | 记录 |
|---|---|
| contains | 父子（Roger / Stephen）之间的 proprietary estoppel 与农场合伙纠纷；原文含 1981 年起的合伙沿革、2008 年退休、逐项 `particulars of alleged detriment`。`both-party = YES`；`multi-t = YES`（约 1981 → 2008 → 2016 → 2018）；`directional = YES` |
| access | `ACCESS_OK`（200 / 177206 bytes）+ `X-Robots-Tag: … noai` |
| rights | `RIGHTS_LICENCE_REQUIRED` + `RIGHTS_ROBOTS_RESERVED` |
| stability | `Neutral Citation Number [2018] EWCA Civ 2669` + 持久 URL |
| still_not_enabled | ① 同 §3：法院处理的是**财产权利**，父亲方在审时已无诉讼能力（原文：`lacked capacity to conduct legal proceedings`，由其妻作 litigation friend），**父亲一侧的「报告」是第三人的代述**，不是本人报告 ⇒ `both-party` 实际为 `PARTIAL`；② 争议是钱与继承，关系状态只有间接痕迹；③ 「devoted parent … spent years caring for a disabled child」这类句子是**法官的描述**，不是当事人报告，不可直接当 `Caregiving` 的观察证据 |

#### `P4` — `Habberfield v Habberfield [2019] EWCA Civ 890` · `https://caselaw.nationalarchives.gov.uk/ewca/civ/2019/890`

| 项 | 记录 |
|---|---|
| contains | 母亲 Jane 与成年女儿 Lucy（另有三名成年兄妹）之间的农场权益安排与信赖。`both-party = YES`；`multi-t = YES`；`directional = YES`（Lucy 认为自己被父母与手足摆布；父母一方另有主张） |
| access | `ACCESS_OK`（200 / 105333 bytes）+ `X-Robots-Tag: … noai` |
| rights | `RIGHTS_LICENCE_REQUIRED` + `RIGHTS_ROBOTS_RESERVED` |
| stability | `Neutral Citation Number [2019] EWCA Civ 890` + 持久 URL |
| still_not_enabled | ① 同一 §3 类别错误风险（法院自述 "sad breakdown in relations"，但裁判的是 equity 的满足方式）；② 实际是**多方**（母 + 四名成年子女），core dyad 的选取需先写定判据（否则只能记 `CRITERION_DEPENDENT`）；③ 该案同时覆盖 `HD-A01`（兄妹）与 `HD-A02`（母女），**不能同时充当两类的独立证据**（否则等于用一份材料证明两格） |

### 4.3 non-romantic friendship（`HD-A04`）

#### `F1` — `PMC11686925` · DOI `10.1177/13591053241235846` · *Mechanisms through which befriending services may impact the health of older adults: A dyadic qualitative investigation*

| 项 | 记录 |
|---|---|
| contains | 12–13 个 befriending dyads（older person ↔ befriender）。**前三个 dyad 同时做了各自单独访谈 + 一次「双方同场」访谈（joint interview）**；dyad 4 起因疫情改为各自电话访谈。发言以 `BF3:` / `OP3:` 标签逐字标注，两方都在场。`both-party = YES`（含 joint interview）；`multi-t = PARTIAL`（关系时长 1–2 年，且报告了访谈前后的变化，不是等距时点）；`directional = YES`（谁先开口、谁在期待 visit，逐字可见：`OP12: 'I look forward to the visit now. It's the younger person's view'`） |
| access | `ACCESS_OK`。2026-09-27 探针 HTTP 200 / 208149 bytes |
| rights | 页面逐字检出 `Creative Commons Attribution 4.0 License (https://creativecommons.org/licenses/by/4.0/)` ⇒ `RIGHTS_CLEARED_AI_OK`。**见 §5** |
| stability | `PMCID` + `DOI`；`Journal of Interpersonal Psychology`。**未证实**跨时间字节不变 |
| still_not_enabled | ① friendship 的成立被**服务机制**（volunteer befriending）外生地安排，材料里同时含「志愿关系」与「真友谊」两层，不区分就会把**服务角色**误读成关系状态；② 年龄差极大（示例中 96 岁 ↔ 45 岁），是 `HD-A08`（照护/角色不对称）的邻近格，与 `HD-A04` 的「对等友谊」不完全同形；③ 被试为服务使用者 + 志愿者，存在**招募偏差**，不得据此推论人群；④ 无 `RomanticAttraction`/`SexualDesire` 维度（也不需要） |

#### `F2` — `PMC11904024` · DOI `10.1007/s42761-024-00277-7` · *Unraveling the Experience of Affection Across Marital and Friendship Interactions*

| 项 | 记录 |
|---|---|
| contains | 两个观测研究：婚姻 dyads（21–65 岁）与**友谊 dyads（15–26 岁）**，双方在录像互动中分别报告情感体验与关系满意度。友谊部分使用 16 题 `MFQ-RA`；并**显式含同性别与混合性别友谊 dyads**（原文：`the Friendship Study, which contained both same- and mixed-gender dyads`）。`both-party = YES`；`multi-t = NO`；`directional = PARTIAL`（双方各自评分，可算方向但**不是各自叙述**） |
| access | `ACCESS_OK`。2026-09-27 探针 HTTP 200 / 221503 bytes |
| rights | 页面逐字检出 `Creative Commons Attribution 4` + `creativecommons.org/licenses/by/4.0/` ⇒ `RIGHTS_CLEARED_AI_OK`。**见 §5** |
| stability | `PMCID` + `DOI`；`Current Psychology`（Springer）。**未证实**跨时间字节不变 |
| still_not_enabled | ① **敏感内容不合规**：友谊样本年龄 15–26 ⇒ 含未成年人；`VALIDATION_CORPUS_V0_1.md` 的 sensitive-content 规则明令「no minors」。**若采用，只能取 18+ 子集，且必须在 fixture 内记录该裁剪**；② 输出是**量表与评分**，不是叙述 ⇒ 适合做「双方都读、但读数不等于话」的场景，不适合做 `Belief` 层的 fixture；③ 婚姻部分与 `HD-A05` 混在同一篇里，须在切割时**不得**把婚姻单位混进友谊格；④ 本条同时是 `HD-A12`（same-sex **friendship** dyad）的 rights-clean 候选——见 §4.4 |

#### `F3` — `Julie Palmer & Anor v Daniel Sans [2024] EWHC 2685 (Ch)` · `https://caselaw.nationalarchives.gov.uk/ewhc/ch/2024/2685`

| 项 | 记录 |
|---|---|
| contains | 判决书逐字确认朋友关系与共同意思：「The evidence which is not really in issue is that Mr Collins and Mr Sans were friends. I accept the evidence of Mr Collins on this point.」「It is incredible to imagine that Mr Sans and his family would have allowed Ms Newby to sell her Property at such a significant undervalue to **a friend of Mr Sans** without there being some further agreement or arrangement between the parties.」`both-party = PARTIAL`（法官采信一方证据，贬低另一方；非双方并陈）；`multi-t = YES`（2013 协议 → 转让 → 2020 判决 → 2024 上诉/重审语境）；`directional = YES`（谁出钱、谁签字、谁在追讨） |
| access | `ACCESS_OK`（200 / 59971 bytes）+ `X-Robots-Tag: … noai` |
| rights | `RIGHTS_LICENCE_REQUIRED` + `RIGHTS_ROBOTS_RESERVED` |
| stability | `Neutral Citation Number [2024] EWHC 2685 (Ch)` + 持久 URL |
| still_not_enabled | ① 朋友身份是**财产共有人之间的事实认定**，friendship 本身不是争议核心 ⇒ 材料的 richness 落在所有权/对价，不在关系状态；② 实际是三人（Collins、Sans、Newby），core dyad 判据需先写定；③ 关系很可能早已破裂且以法律程序终止——**结构上是 adversarial friendship，不是对等友谊**（更接近 `HD-A09`） |

### 4.4 same-sex core dyad（`HD-A12`）

`HD-A12` 的定义是「same-sex **core dyad**」且 `dyad_class = any`。本轨据此把「同性**手足** dyad」与「同性**友谊** dyad」都算作 `HD-A12` 的合法实例。
**这是一个判据依赖的记账，不是既成事实**：若 Architect 要求 `HD-A12` 必须是**伴侣** dyad，则以下两条都要改记为 `CRITERION_DEPENDENT`。已列入 `open_questions_for_architect`。

#### `X1` — `PMC11219362`（与 `S1` 同一份）· **同一**同性手足 dyad 材料

| 项 | 记录 |
|---|---|
| contains | 原文可见**同性与异性混合**的 sibling 配对：「I guess since we are both gay, we could remind each other...」「I thought talking to my brother who is straight about PrEP would be uncomfortable, but it wasn't.」⇒ 该材料内**同时**含 `gender_composition = SAME_SEX` 与 `MIXED_SEX` 的 sibling dyads。`both-party = YES`；`directional = YES` |
| access | `ACCESS_OK`（200 / 237633 bytes） |
| rights | `RIGHTS_CLEARED_AI_OK`（CC BY 4.0，无 `NoDerivatives`）。**见 §5** |
| stability | `PMCID` + `DOI` |
| still_not_enabled | ① 同一材料**横跨 `HD-A01` 与 `HD-A12` 两格**⇒ 若同时计入两格，等于用一份材料证明两格覆盖，**违反「覆盖矩阵不得互相折叠」**。本轨的处置建议：二选一优先，或两格各用**不同单位**并显式记录同源；② 该材料中 `gender_composition` 需**逐 dyad 判定**（不能整篇当 `SAME_SEX`）；③ 主题是性少数男性的性健康，`RomanticAttraction`/`SexualDesire` 的**手足 dyad 版本**不由此材料支持 |

#### `X2` — `PMC11904024`（与 `F2` 同一份）· **同一**同性友谊 dyad 材料

| 项 | 记录 |
|---|---|
| contains | 友谊 dyads 中**同时**含同性与异性对；友谊双方各自报告 affection。`both-party = YES`；`directional = PARTIAL` |
| access | `ACCESS_OK`（200 / 221503 bytes） |
| rights | `RIGHTS_CLEARED_AI_OK`（CC BY 4.0）。**见 §5** |
| stability | `PMCID` + `DOI` |
| still_not_enabled | ① 同行 `F2` 的未成年人问题（15–26 岁）；② 观测量是评分不是叙述；③ 同一材料横跨 `HD-A04` 与 `HD-A12`，同 `X1` 的同源折叠问题；④ **不含**同性**伴侣** dyad |

#### `X3` — `PMC2844533` · DOI `10.1007/s11199-009-9701-x` · *Fairy Tales: Attraction and Stereotypes in Same-Gender Relationships*

| 项 | 记录 |
|---|---|
| contains | 同性关系中「什么最初吸引了我」的问卷 + 开放式作答。`both-party = PARTIAL`（各自报告自己的吸引，**不覆盖对方的吸引**）；`multi-t = NO`；`directional = PARTIAL`（有 i→j 方向，无 j→i 反向） |
| access | `ACCESS_OK`。2026-09-27 探针 HTTP 200 / 249681 bytes |
| rights | 页面逐字检出 `Creative Commons Attribution Noncommercial License` / `Attribution-NonCommercial` ⇒ `RIGHTS_CLEARED_CONDITIONAL`（**有 `NonCommercial`**）。**无 `NoDerivatives`**。是否满足本项目对「机器处理 + 入仓」的用途**须 Human 确认**，本轨 fail closed |
| stability | `PMCID` + `DOI`；`Sexuality and Culture`（Springer，2009） |
| still_not_enabled | ① `NC` 约束未解决前不可用；② **单方报告**（只有 i 对 j 的吸引），无法支撑「双方对彼此」的任何读；③ 研究自身预设「同一性别关系」的**浪漫**框架，把同性**非浪漫** dyad 排除在外；④ 横断面 |

#### `X4` — 公开领域路径（`www.govinfo.gov` + 17 U.S.C. §105）

| 项 | 记录 |
|---|---|
| contains | 美国联邦政府出版物。`https://www.govinfo.gov/` 探针 200 / 65445 bytes。`/about` 页面逐字：「In general, GovInfo documents fall under Title 17, Section 105, United States Code, which provides that: Copyright protection under this title is not available for any work of the United States Government…」以及限定句「However, Government publications may contain copyrighted material which was used with permission of the copyright owner.」 |
| access | `ACCESS_OK`（2026-09-27 探针 200）。`www.govinfo.gov/robots.txt` 200，**无任何 AI 专用 UA 段**，仅对 `/admin/`、`/search/`、`/core/` 等路径 Disallow |
| rights | 美国联邦作品**不受版权保护**（§105）⇒ 就版权而言最宽松的一族。**但**：① 上述 §105 限定句意味着**政府出版物可能内含第三方已授权的有版权材料**，必须逐件核对；② `govinfo` 也有**「Apply for a licence」**式的既有做法（未在本轮逐条核对其 reuse 页，故此处**不主张**「无许可要求」） |
| stability | 有 `package id` / `granule id` / 集合路径，属**版本化仓库**；本轨只验证了根页与 `/about`，**未**验证任一具体 granule 的可取性（**未主张**） |
| still_not_enabled | ① **本轨未在该路径上找到「核心 dyad 本身就是同性伴侣」的判决**：所检索到的美国联邦同性与婚姻/就业类判决，其当事人是「个人 vs 政府机构」，**不是**同性 dyad。因此该路径目前只能支持 `gender_composition` 可声明、**dyad class 仍是 `professional/cooperative` 或 `adversarial`**；② 若最终采用的联邦材料中含第三方引用文本，须按 §105 限定句逐件剥离 |

**X-14 记账（必须逐字成立）**：
> 在本轨**实际检索过**的下列位置——`caselaw.nationalarchives.gov.uk`（站内检索 + 外部检索）、
> `pmc.ncbi.nlm.nih.gov`（站内检索 + 外部检索）、`www.govinfo.gov`、`www.gutenberg.org`、
> `storycorps.org`、`www.lgo.org.uk`、`www.bailii.org`——**未找到**「核心 dyad 本身是一对同性伴侣、
> 且权利清晰到可做 LLM fixture 映射」的来源。
> 这是**检索范围陈述**。本轨**不主张**该类来源在字段上不存在。

### 4.5 逐类小结（含覆盖记账与「仍然不是证据」的东西）

| 类 | rights-clean（`AI_OK`）候选数 | rights 受限候选数 | 覆盖记账建议 | **这些来源仍然买不到的东西** |
|---|---|---|---|---|
| sibling `HD-A01` | 1（`S1`） | 3（`S2` 条件合规但 core-dyad 判据不满足；`S3`/`S4` 需许可） | `ZERO_IN_AUDITED_CORPUS` → 候选**已就位**，**未执行、未验证** | 跨时点的同一条 dyad 双向报告；非照护型 sibling dyad；`Liking` 与 `Caregiving` 的解耦证据 |
| parent–adult-child `HD-A02` | 1（`P1`，但为自评问卷） | 2（`P2` 需许可；`P3`/`P4` 需许可） | 同上 | **双向互报 + 纵向**的 parent–adult-child 材料在 rights-clean 一侧**未找到**（`P2` 设计最好但 rights 未清） |
| non-romantic friendship `HD-A04` | 2（`F1`/`F2`） | 1（`F3` 需许可） | 同上 | 对等友谊的**双方叙述**（`F2` 是评分）；`F1` 的服务角色与真友谊之分 |
| same-sex core dyad `HD-A12` | 2（`X1`/`X2`，且均为跨格同源） | 1（`X3` `NC` 未解） | 同上 + 判据依赖待裁 | **同性伴侣** dyad；`RomanticAttraction`/`SexualDesire` 在同性 dyad 中的读 |

---

## 5. 一个 rights-clean 但仍需 Human 裁决的残留问题（fail closed，不自行放行）

CC BY 4.0 **许可的是「作品」**，不是「作品里的每一位受访者」。上面 `RIGHTS_CLEARED_AI_OK` 的六份材料
（`S1`/`S2`/`P1`/`F1`/`F2`/`X1`/`X2`）**全部含逐字访谈引语**。受访者的知情同意是向**期刊/出版社**作出的，
其范围**不一定**覆盖「把引语交给 LLM 逐句映射后再派生 fixture」。

因此本轨加一条**设计约束**（不是权利判定）：

> 新 fixture **不得**整段复制 CC BY 论文里的逐字引语。默认形态 = **faithful paraphrase + 极短锚点**
> （与 Fixture 003 已有做法同形：`SC/...` 锚点 + 忠实转述，不镜像原文）。
> 是否连极短锚点都需要单独同意，本轨**不判定**，交 Architect / Human。

这条约束同时满足「rights fail closed」与「不新增第二份 SSOT」。

---

## 6. 本规划依赖的前置条件（preconditions）

### 6.1 三 verifier 同版本合并件（**状态：UNKNOWN**）

Fixture 003 §3 第 8 条与 Fixture 001 §2 第 7 条都逐字要求：**三个独立 Verifier 必须消费同一个 merged exact version**。
`VALIDATION_GATES_V0_2.md` §6.1/§6.2 沿用这一纪律。

**本轨的诚实状态**：在 child 隔离契约下，`#20`/`#21`/`#22` 的状态是 **UNKNOWN**——本轨**未读、未执行、未引用**这三个 issue，
也**没有**任何其它渠道可确认它们的合并件版本。

**因此**：
> 任何「必须以标准方式验证」的 fixture，在拿到**一个确定的 merged exact version**（含其 tree sha 与文件 sha）
> 之前**不得冻结**。本轨规划的全部来源都受这条约束。
> 本轨交付的是**来源计划**，不是**可冻结的 fixture**——这是设计使然，不是遗漏。

### 6.2 明确排除的既有材料

Fixture 003（L1-001 StoryCorps）在本规划中**完全不可作为来源**，三条各自独立的理由：

1. 它在 fixture 内已记录 `rights_policy=HUMAN_REVIEW_REQUIRED` → Eye 判 fail-closed 为
   `POINTER_HASH_ONLY`（`raw_allowed=false, representation_allowed=false, store_pointer_only=true`）。
2. 它是 **pointer-only**、**无 transcript body 持久化**，因此**拿不到可切分的原子单位**。
3. 它的 canonical 地址**至少变动过一次**：Fixture 003 §1 记载旧地址 `…-perasa/` 在 2026-09-14 live 校验为 **404**，
   已改指 `…-remembering-the-love-between-danny-and-annie/`。
   本轨 2026-09-27 复核：**新地址 HTTP 200**（`text/html`），旧地址未复测。
   **稳定性因此不足**：新 fixture 不得依赖一个已证明会移动的指针。

**⚠ 一条必须记录、但不得升级权利的观察**：Fixture 003 §1 与其附录记录
`robots.txt` 含 `Content-Signal: search=yes,ai-train=no,use=reference` + 对 GPTBot/ClaudeBot/CCBot 的 `Disallow`。
本轨 2026-09-27 复核 `https://storycorps.org/robots.txt`：**该 AI 名单与 `Content-Signal` 已不在文件里**，
现内容为普通 WordPress/Yoast 段（仅 `Disallow: /wp-json/`、`/?rest_route=`，并对 `AdsBot` Disallow），
另有 `Crawl-delay: 10` 与 `Crawl-delay: 600` 两处。

**处置（关键）**：robots 层的变化**不是**权利升级依据。Fixture 003 的
`HUMAN_REVIEW_REQUIRED` / pointer-only 状态**保持不变**（裁决 X-7 + §C item 7）。
本轨**不**因为 robots 变了就把 StoryCorps 重新列为 rights-clean 来源。
同理，本轨**不主张**「该变化意味着权利方已许可 AI 处理」——**这需要版权方（StoryCorps）的明示许可，属于 Human 裁决**。

---

## 7. 稳定性的诚实定义

`VALIDATION_CORPUS_V0_1.md` 的选择方法要求「versioned / stable-source with a stable pointer」。
本轨把「稳定」拆成**四项可分别核验**的东西，并逐源记录，避免把「有 DOI」当成「已冻结」：

| 分项 | 含义 | 本轮观察结果 |
|---|---|---|
| `PERSISTENT_ID` | 持久标识符（DOI / PMCID / NCN / PG ebook no.） | 全部候选**有** |
| `FROZEN_RELEASE` | 存在**版本化/冻结发布**（如带版本号的 snapshot） | **无一份候选被证实**。PMC 论文是**最终版**，不是冻结发布；只有 §4.5 提到的 `2022-revision snapshot` 做法是 corpus 自己在 `L2-002` 用的手工方案 |
| `BYTE_STABLE` | 跨时间字节不变 | **未测**（单次探针，无纵向比对）。只有 `findcase`/`govinfo` 属仓库型（有 package/granule 概念），但本次也未做纵向比对 |
| `MOVE_HISTORY` | 是否已证明会移动 | **StoryCorps 已证明会移动**（`…-perasa/` → 404）。**其余候选未证明稳定，也未证明不稳定** |

**因此本轨的结论是**：本轮候选满足 `PERSISTENT_ID` 与「2026-09-27 可达」两项，
**不满足**「已冻结 / 已证明字节稳定」。若 Architect 要求 `FROZEN_RELEASE`，
则**四类都需要一次人工快照采集**——那已不是 mini-benchmark 的规模。

---

## 8. 拒设的阈值（本轨不发明数字）

| # | 拒设项 | 理由 | 什么证据会产生一个值 |
|---|---|---|---|
| 1 | 「每类需 N 个 fixture」 | C-P1 明令；N 与表示能力无推导关系 | 已论证的 `dyad_class` ↔ fixture 对应 + 每类实例数下限（由 §4.4 的判据先写定） |
| 2 | 「同一 dyad 需 N 个时间点」 | 需要的点数由具体 transition 问题决定，不由规划决定 | 一次预注册的 transition 问题清单 |
| 3 | 「双方报告的比例下限」 | 比例阈值会重新引入 C-P2 禁止的单一分母 | 逐 dyad 的 `both_party` 三值判定表（`YES`/`PARTIAL`/`NO`）先跑过 |
| 4 | 「权利受限来源占比上限」 | 无推导基础 | 一份**书面的**来源许可协议（改变的是权利本身，不是阈值） |
| 5 | 「候选来源条数下限（2–3）」 | 2–3 是 dispatch 的**规划工作量**约定，不是门判据 | 不适用（工作量约定，不是阈值） |

**已给出的判据共三处，全部是结构性（由成功定义直接推出，非选定数字）**：
① 「至少 1 个单位在 withheld 后降级」= necessity 的存在条件；
② 「未结清的 `catchall_used = YES` = 0」= coverage 的结清条件（沿用 C 轨）；
③ 「`rights_status` 无 `HUMAN_REVIEW_REQUIRED` / `RIGHTS_NOT_CLEARED` / `RIGHTS_LICENCE_REQUIRED`」
= 来源可用的前置条件。

---

## 9. 本轨**没有**做、也**不主张**的事

1. 没有下载、缓存或镜像任何一份材料；探针为单次 GET/HEAD，落盘仅限响应头与状态码。
2. 没有应用任何 licence、没有绕过任何 robots、没有登录、没有绕过 paywall。
3. 没有运行任何 gate、没有执行任何 fixture mapping、没有产生任何 mapping 计数。
4. 没有读/执行/引用 `#20`/`#21`/`#22`，因此**没有**关于其状态的任何断言（除「UNKNOWN」这一由隔离契约推出的状态）。
5. 没有修改 `VALIDATION_CORPUS_V0_1.md`、三个 fixture、`AGENTS.md`、`CURRENT_ARCHITECTURE.md`、
   `PARAMETER_CONVERGENCE_V0_1.md`、`VALIDATION_GATES_V0_2.md` 中的任何一个字节。
6. 没有把「四类有候选来源」说成「四类已被覆盖」——`ZERO_IN_AUDITED_CORPUS` 的改变需要执行，本轨不执行。
7. 没有声称任何来源能提供 **construct 语义**（`Liking` / `RomanticAttraction` / `SexualDesire` /
   `Trust` / `AttachmentSecurity` / `Caregiving` / `Dedication` / `OutcomeDependence` 的读法与互斥性）。
   来源只提供**原子单位**；construct 语义是 schema 的事。
8. 没有把 `HD-A12` 的「同性 core dyad」读法自行定案（伴侣 vs 任何同性 dyad）——见 §4.4。
9. 没有主张 §4.4 末尾 X-14 检索范围之外的任何存在性/不存在性断言。
10. 没有把 StoryCorps robots 的变化当作权利变化（§6.2）。

---

## 10. 探针原始记录（可复算）

`PROBE_DATE_UTC = 2026-09-27T20:45:30Z`，共 23 个 URL 的一次 GET 探测，**全部 200**：

| URL | 状态 | content-type | bytes | `X-Robots-Tag` |
|---|---|---|---|---|
| `pmc…/PMC11219362` | 200 | text/html | 237633 | — |
| `pmc…/PMC10068502` | 200 | text/html | 272065 | — |
| `pmc…/PMC12101125` | 200 | text/html | 299100 | — |
| `pmc…/PMC11686925` | 200 | text/html | 208149 | — |
| `pmc…/PMC11904024` | 200 | text/html | 221503 | — |
| `pmc…/PMC2844533` | 200 | text/html | 249681 | — |
| `pmc…/PMC12629515` | 200 | text/html | 205617 | — |
| `pmc…/PMC8611109` | 200 | text/html | 228123 | — |
| `pmc…/PMC4683933` | 200 | text/html | 184687 | — |
| `pmc…/PMC4370347` | 200 | text/html | 185991 | — |
| `pmc…/PMC9451025` | 200 | text/html | 203779 | — |
| `caselaw…/ewhc/ch/2025/1367` | 200 | text/html | 316995 | `noindex,nofollow,noai` |
| `caselaw…/ewca/civ/2008/904` | 200 | text/html | 74308 | `noindex,nofollow,noai` |
| `caselaw…/ewca/civ/2018/2669` | 200 | text/html | 177206 | `noindex,nofollow,noai` |
| `caselaw…/ewca/civ/2019/890` | 200 | text/html | 105333 | `noindex,nofollow,noai` |
| `caselaw…/ewhc/ch/2024/2685` | 200 | text/html | 59971 | `noindex,nofollow,noai` |
| `caselaw…/ewhc/ch/2024/2729` | 200 | text/html | 78993 | `noindex,nofollow,noai` |
| `gutenberg.org/ebooks/158` | 200 | text/html | 23041 | — |
| `gutenberg.org/ebooks/45` | 200 | text/html | 24861 | — |
| `gutenberg.org/ebooks/7256` | 200 | text/html | 22530 | — |
| `www.govinfo.gov/` | 200 | text/html | 65445 | — |
| `www.bailii.org/` | 200 | text/html | 4446 | — |
| `www.lgo.org.uk/decisions/adult-care-services/charging/24-001-994` | 200 | text/html | 48621 | — |

**非 200 的观察（如实记录为失败）**：

| URL | 结果 | 处置 |
|---|---|---|
| `https://www.bailii.org/robots.txt` | **502 Bad Gateway**（两次尝试均失败） | `ACCESS_PARTIAL`：站点根页可达，但**无法读取其机器策略**⇒ 在拿到其 robots/条款前**不可用** |
| `https://www.gutenberg.org/ebooks/134` / `/5146` / `/2759` | 200，但**标题不是我预期的作品** | 记录为**否定观察**：本轮**不**引用这些 ebook 号作为任何具体作品的标识（避免凭记忆写 ID） |

**未探测（明确不做）**：任何需要登录、订阅或付费墙的来源；任何 `403` 目标（未尝试绕过）。
`StoryCorps` 旧地址 `…-perasa/` 未复测（旧 404 状态沿用 Fixture 003 §1 的 2026-09-14 记录，本轨不重复断言）。
