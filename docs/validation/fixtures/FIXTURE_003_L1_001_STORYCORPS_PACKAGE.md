# Fixture 003 — L1-001 StoryCorps `Never Say Goodbye` 冻结口述史包

状态：**CANDIDATE FOR ARCHITECT REVIEW / NO LHRM MAPPING**  
父任务：`youling/lhrm#25`；关联 `#15` `#23` ；Corpus：`VALIDATION_CORPUS_V0_1.md` `L1-001`。  
准备者：LHRM Research（Fresh Research, `research/fixture-003-storycorps-package`，2026-09-14 warm resume）。  
基准：`LHRM main f2377849f71407013d5abe19fd0b4ff26f501066`（Fixture 001/002 frozen）+ `Eye main 8393cadc2e782f1d8d2adfa2b11d8329192cfcd0`（Batch B merged, StoryCorps rights correction）。

> 本包只做材料清洗与冻结，不做任何 `Liking / RomanticAttraction / SexualDesire / Trust / AttachmentSecurity / Caregiving / Dedication / OutcomeDependence` 映射，不修改 canonical schema。不把全文镜像进仓。

## 1. Source / provenance

- 作品：StoryCorps `“Never Say Goodbye”: Remembering The Love Between Danny And Annie`（Danny Perasa & Annie Perasa 口述访谈）
- canonical pointer（已校正，Eye 2026-09-14 live 200 验证）：`https://storycorps.org/stories/never-say-goodbye-remembering-the-love-between-danny-and-annie/`
  - 旧 Pack 地址 `…-perasa/`（后缀 `-perasa`）在 2026-09-14  live 校验为 **404**，已按 `listen-sitemap.xml` 校正为当前地址（`text/html; charset=UTF-8`，约 118031 bytes）。参见 `Eye spikes/lhrm-case-bank-intake-01/LHRM_CASE_BANK_BATCH_B_REPORT.md §3.1`。
  - Eye locator：`loc:lhrm/storycorps-perasa-canonical`（`source_relation=CANONICAL`）
- 关联页：`https://storycorps.org/podcast/storycorps-537-never-say-goodbye/`（podcast mirror，不得冒充 canonical）
- 官方索引：`https://storycorps.org/listen-sitemap.xml`（含 canonical loc）、站内搜索 `?s=Danny+Annie+Perasa`
- 版本/时间：页面 `datePublished 2021-08-20T03:30:24+00:00` / `dateModified 2021-08-21T04:27:52+00:00`；内文标注 `Originally aired August 11, 2004 on NPR's Morning Edition, rebroadcast August 20, 2021`；访谈本体为两次录制（2004-08-11 与 2006-02 Brooklyn home）。
- 抽取边界：**仅** `页面标题/参与人/Intro 4 段 editorial 叙事 + Transcript modal 内有效语义段落`（Eye 已验证 modal 存在但未持久化 body；原始 HTML 含 23 个 `<p>`，其中 1 个为 participants 行，语义段落为 21，另有 1 个 production cue）。`Recent Stories`、`Share/Replay` UI、 Podcast 订阅条、Google Classroom、footer 及站外动画/2013 update 链接仅作 pointer，不纳入冻结语义。
- licence / access：`© StoryCorps`，公开可读但**非 public-domain、非 CC**；`robots.txt` 含 `Content-Signal: search=yes,ai-train=no,use=reference`（EU 2019/790 reservation）+ `Disallow` for GPTBot/ClaudeBot/CCBot 等；无显式 transcript CC 授权。Eye 判定 `rights_policy=HUMAN_REVIEW_REQUIRED` → `POINTER_HASH_ONLY` fail-closed（`Eye rights.py decide("HUMAN_REVIEW_REQUIRED") → raw_allowed=false, representation_allowed=false, store_pointer_only=true`）。LHRM 本文件不存储 transcript/audio 原文，仅保存**忠实 paraphrase + 短锚点**（fair use / fair dealing, 保留归属），不镜像全文。
- Eye handoff（pointer-only, lawful boundary）：`eye-evidence-handoff/0.1`，`requirement_ref=lhrm#25`，`raw_artifact_ref=null`，`representation_artifact_refs=[]`，`content_hashes=[]`，`source_relation=CANONICAL`。下游可消费 canonical pointer / locator refs / observation metadata / rights_policy 及“transcript 存在但未持久化”的 provenance，不得通过 Eye 获取 transcript body / Audio / `long-text-anchored/0.1` Representation（详见 Eye Batch B §3.4–3.6）。
- 长度：可用语义约 `~950` 词 transcript + `~500` 词 editorial preamble（含 2 次录制跨度近 30 年回顾 + 临终当下 + 身后追记）。

### Core dyad for this fixture

`Danny Perasa <-> Annie Perasa`（夫妇，Brooklyn；访谈中互为 speaker/reported speaker）。页面未在当前 canonical HTML 中标注职业，Corpus 归档的 `OTB clerk / nurse` 来自既往档案背景，不作为本冻结包的 page-asserted fact 引入；本包仅保留页面与 transcript 中明确出现的 husband/wife 关系与 lived ritual。

## 2. Normalized source anchor convention

为便于 Eye `anchored Representation` 与 Juece `ClaimEvidenceLink` 的后续对齐，本包对当前 canonical HTML 按**非空可见段落**定义冻结锚点（仅用于本 fixture 语义定位，非 LHRM construct，亦不替代 Eye block id）：

- `SC/page/meta/p001` — `<title>` / `participants` 行
- `SC/page/intro/p001` — editorial intro 第 1 段（Danny 首次约会求婚概述）
- `SC/page/intro/p002` — editorial intro 第 2 段（2004 年到访 StoryCorps 回顾近 30 年经历）
- `SC/page/intro/p003` — editorial intro 第 3 段（2004 后持续参与至 2006 终末诊断、Brooklyn 家中访谈、一周后离世；冻结时按句切分为 p003-s1/s2/s3/s4 仍归同一页锚定）
- `SC/page/intro/p004` — editorial intro 第 4 段（Annie 身后收信与 2021 年离世）
- `SC/page/meta/p002` — `Originally aired / rebroadcast` 行（含 2004-08-11 / 2021-08-20）
- `SC/transcript/p001` … `SC/transcript/p021` — Transcript modal 内按 `<p>` 顺序的 21 个有效语义段落（含 `[Music]` 占位；已排除 participants/meta 行，对应本次抓取语义内容，participants 与 meta 始终归入 `SC/page/meta/*`，不计入 transcript 语义编号）：
  - `p001` DP 回忆首次约会时打断对方并预告将作发言的情景
  - `p002` DP 回忆对方当场答应求婚及次日清晨致电确认未改主意的情节
  - `p003` AP 插话说明对方习惯早起
  - `p004` DP 描述每年固定日期定时重温求婚问询的惯例
  - `p005` AP 回应肯定并提及已重复多年
  - `p006` DP 表达频繁示爱时的复杂心情并以收音机作比喻
  - `p007` AP 说明若晨间桌上无便条则会担心，提及每日晨间便条习惯
  - `p008` DP 以找不到书写工具作假设性解释
  - `p009` AP 朗读一封晨间便条示例（称呼、天气、约定通话时间等要素的概括）
  - `p010` DP 对该便条风格的评价
  - `p011` AP 补充便条结尾为重复的示爱语
  - `p012` DP 以居家安全感与媒介色彩作婚姻比喻
  - `p013` [Music] 制作间奏
  - `p014` AP 谈及疾病终末性带来的感受及对对方表现的评价
  - `p015` DP 以车辆下坡需推动作比喻，并表达对未来的期许重心
  - `p016` AP 评价对方已作周全安排
  - `p017` DP 谈及身后仪式安排及婚礼入场往事的长段（冻结时拆为 s1/s2/s3）
  - `p018` AP 简短肯定回应
  - `p019` DP 谈及面对离世的未完成接纳、赠予自我及提及节日信件
  - `p020` AP 朗读节日信件（节日问候、多年情感延续及艰难时期支撑等要素的概括）
  - `p021` DP 描述晨间与夜间的日常支持互动及对伴侣唯一性的信念（冻结时拆为 s1/s2/s3）

未来若 StoryCorps 页面结构或 Eye parser 变更，只允许追加 `Eye representation/block ref -> SC/...` 对照，不得静默改写下列 frozen unit 的 `faithful_paraphrase`。

## 3. Freeze rules

1. 只保存页面/访谈中出现的 `observed_event / recalled_event / speech / quoted_letter / belief_or_evaluation / plan / metaphor / environment / other`，不做 LHRM construct 映射。
2. `recording_time != recalled_event_time != event_time` 严格分开；回忆 1978 first date 不得写成 2004 发生。
3. `said != believed != true`；人物说法、转述他人说法、读信内容、人物当下评价分层保留，`reported_speaker_ref` 用于嵌套引语（例：Danny 引用 1978 的自己、引用 Annie 过去关于 brother 的话）。
4. 隐喻（busted old radio / color TV / shelter / downhill car）保留为 `figurative_expression`，不按字面世界事实处理，不自动折算为 latent state。
5. 2006 临终段（illness / casket / Valentine）在 2004 录制切片中不得提前可见；身后追记（Annie 2021 去世）不得倒灌到访谈当时的 belief。
6. 纸面信件朗读（morning note / Valentine）标记为 `quoted_letter`，`speaker_ref` 为朗读者，`reported_speaker_ref` 为信件作者（若不同）。
7. 不把 `happily married / shelter / never another Annie` 等高层评价自动量化或当作客观关系真值。
8. 三个独立 Verifier 必须消费**同一个 merged exact version**；不得在验证过程中重写事实包或自行补充 transcript 原文。

## 4. Atomic narrative / fact units

`fact_or_narrative_status` 为材料层状态（非法律真值）：`editorial_asserted | habitual_asserted | character_report | quoted_letter | belief_expression | figurative_expression | other`。  
`unit_type` 按 issue 要求：`observed_event | recalled_event | speech | quoted_letter | belief_or_evaluation | plan | metaphor | environment | other`。

| unit_id | unit_type | faithful_paraphrase | source_anchor | recording_time | event_time / sequence | speaker_ref | reported_speaker_ref | fact_or_narrative_status | future_leakage_note |
|---|---|---|---|---|---|---|---|---|---|
| S001 | recalled_event | Editorial states Danny proposed to Annie on their first date and she accepted. | SC/page/intro/p001 | 2004-08-11 (editorial frame, retelling 1978) | ~1978 (first date) | editorial | Danny (1978 self) / Annie (reply) | editorial_asserted | Do not import later illness/death into first-date belief. |
| S002 | recalled_event | Editorial states the pair came to StoryCorps in 2004 to talk about that first date and how love grew over nearly 30 years. | SC/page/intro/p002 | 2004-08-11 | 2004-08-11 (interview) ; recalled span ~1978–2004 | editorial | — | editorial_asserted | — |
| S003 | observed_event | Editorial states after the 2004 interview Danny became part of StoryCorps family and returned repeatedly to interview others and talk about love for Annie. | SC/page/intro/p003 s1 | 2004–2006 interval (retrospective) | 2004–2006 | editorial | — | editorial_asserted | — |
| S004 | environment | Editorial states in 2006 Danny was diagnosed with fast-spreading terminal cancer. | SC/page/intro/p003 s2 | 2006-02 editorial summary | Jan–Feb 2006 (diagnosis) | editorial | — | editorial_asserted | Do not use 2004切片 to explain 2006 diagnosis. |
| S005 | observed_event | Editorial states Danny wanted one last interview with Annie; StoryCorps went to their Brooklyn home. | SC/page/intro/p003 s3 | 2006-02 | Feb 2006 (home interview) | editorial | — | editorial_asserted | Brooklyn home location from editorial, not from transcript utterance. |
| S006 | observed_event | Editorial states Danny died about a week after that home interview. | SC/page/intro/p003 s4 | post-2006-02 (editorial) | ~one week after Feb 2006 home session | editorial | — | editorial_asserted | Keep death as editorial post-event; do not leak into K1/K2 belief slices. |
| S007 | observed_event | Editorial states after Danny’s passing Annie received thousands of condolence letters, read one daily until she died of COVID-19 in 2021 at age 79. | SC/page/intro/p004 | 2021-08 (editorial rebroadcast frame) | 2006–2021 (letters) ; 2021 death | editorial | — | editorial_asserted | Posterior bereavement trajectory must not be inserted into interview belief. |
| S008 | environment | Page metadata: original broadcast 2004-08-11 on NPR Morning Edition; rebroadcast 2021-08-20. | SC/page/meta/p002 | — | 2004-08-11 / 2021-08-20 | editorial/meta | — | editorial_asserted | — |
| S009 | speech | Danny recounts that on first date he interrupted Annie to say he would give a speech after which she would want to leave. | SC/transcript/p001 s1 | 2004-08-11 | ~1978 (recalled first-date speech) | Danny (2004) | Danny (1978 self) | character_report | Nested self-quote; do not treat as current directive. |
| S010 | speech | Danny paraphrases his past self framing love in colloquial four-letter-word terms, identifying that word as love. | SC/transcript/p001 s2 | 2004-08-11 | ~1978 | Danny | Danny (1978 self) | character_report | Figurative framing inside reported speech; paraphrased. |
| S011 | speech | Danny paraphrases his past self suggesting any onward movement together would be toward marriage, citing fatigue as a reason against other options. | SC/transcript/p001 s3 | 2004-08-11 | ~1978 | Danny | Danny (1978 self) | character_report | Proposal wording is reported speech, not present physical state. |
| S012 | recalled_event | Danny reports Annie accepted the proposal and he called early the next morning to confirm she had not changed her mind. | SC/transcript/p002 | 2004-08-11 | ~1978 next morning | Danny | Annie (1978 reply reported by Danny) | character_report | Reply is Danny-reported; keep attribution. |
| S013 | speech | Annie interjects that he always gets up early (laughs). | SC/transcript/p003 | 2004-08-11 | habitual / 2004 utterance | Annie | — | character_report | — |
| S014 | observed_event | Danny describes a yearly habit around a fixed April date in early afternoon of calling Annie to ask if she would accept again, with consistent affirmative answers so far. | SC/transcript/p004 | 2004-08-11 | yearly habit since ~1979, next occurrence ~Apr 22 | Danny | — | habitual_asserted | Habit report, not verified external log. |
| S015 | speech | Annie affirms with a short positive reply indicating about twenty-five repetitions (laughs). | SC/transcript/p005 | 2004-08-11 | 2004 utterance | Annie | — | character_report | Indicates ~25 anniversaries by 2004. |
| S016 | belief_or_evaluation | Danny says he feels self-conscious about saying affectionate phrases so often and does so to reassure her of the source of that affection. | SC/transcript/p006 s1 | 2004-08-11 | ongoing belief stated 2004 | Danny | — | belief_expression | Keep as self-evaluation, not objective attractiveness fact. |
| S017 | metaphor | Danny offers a metaphor of his affection as a song from an imperfect old radio, noting appreciation that she keeps it nearby at home. | SC/transcript/p006 s2 | 2004-08-11 | 2004 metaphor | Danny | — | figurative_expression | Do not literalize as separate object; paraphrased. |
| S018 | belief_or_evaluation | Annie says if there is no note on the kitchen table she worries, noting he writes her a morning letter daily. | SC/transcript/p007 | 2004-08-11 | daily habit ~1978–2004 | Annie | — | habitual_asserted / belief_expression | Habit + evaluative worry is her belief. |
| S019 | belief_or_evaluation | Danny says the only plausible reason for a missing note would be lacking a suitable pen. | SC/transcript/p008 | 2004-08-11 | hypothetical | Danny | — | belief_expression | Counterfactual explanation, not verified inventory. |
| S020 | quoted_letter | Annie reads an example morning note paraphrased as addressing her with an affectionate nickname, commenting on rainy weather and stating a planned mid-morning call time. | SC/transcript/p009 | 2004-08-11 | note written on a morning (unspecified date) | Annie (reader) | Danny (letter author) | quoted_letter | Keep quoted_letter layer distinct from Annie belief; paraphrased, no verbatim body. |
| S021 | belief_or_evaluation | Danny characterizes the note as a romanticized weather report. | SC/transcript/p010 | 2004-08-11 | 2004 utterance | Danny | — | belief_expression | Evaluation, not weather fact. |
| S022 | quoted_letter | Annie notes the same note ends with repeated affectionate closing phrases. | SC/transcript/p011 | 2004-08-11 | same note | Annie | Danny | quoted_letter | Paraphrased; no verbatim repetition. |
| S023 | metaphor | Danny describes married life as providing a sense of shelter at home where affectionate contact is safely received rather than rejected. | SC/transcript/p012 s1 | 2004-08-11 | 2004 belief | Danny | — | figurative_expression | Shelter is metaphor, not physical refuge fact; paraphrased. |
| S024 | metaphor | Danny compares married life to moving from monochrome to color viewing, expressing no desire to return to the prior state. | SC/transcript/p012 s2 | 2004-08-11 | 2004 belief | Danny | — | figurative_expression | Comparison, not media fact; paraphrased. |
| S025 | other | Transcript marks a music interlude. | SC/transcript/p013 | 2004/2006 edit | — | editorial/production | — | other | Production cue, not dyad fact. |
| S026 | belief_or_evaluation | Annie says the illness itself is not hard on her, only the finality, and that he copes with steadiness. | SC/transcript/p014 | 2006-02 (terminal phase) | Feb 2006 | Annie | — | belief_expression | Evaluative term paraphrased, not clinical status. |
| S027 | metaphor | Danny offers a metaphor of a car on a slope needing a push to move, crediting her for providing that push. | SC/transcript/p015 s1 | 2006-02 | Feb 2006 | Danny | — | figurative_expression | Paraphrased. |
| S028 | belief_or_evaluation | Danny says they try to give each other hope focused not on his own survival but on her future wellbeing, social support, and openness to a future partnership if she wishes. | SC/transcript/p015 s2 | 2006-02 | forward-looking belief/plan stated Feb 2006 | Danny | — | belief_expression | Hope is specified as post-pass wellbeing, not survival; paraphrased. |
| S029 | belief_or_evaluation | Annie responds he has everything planned. | SC/transcript/p016 | 2006-02 | Feb 2006 | Annie | — | belief_expression | — |
| S030 | plan | Danny reports Annie said it was her decision and she wants to walk behind the casket alone. | SC/transcript/p017 s1 | 2006-02 | plan stated by Annie (recalled by Danny) | Danny | Annie (reported) | character_report | Keep as Annie’s stated plan, not enacted fact. |
| S031 | speech | Danny recalls a wedding walk-in dilemma where Annie was uncertain which brother to walk with to avoid causing offense, and he suggested she walk in with him and therefore walk out with him. | SC/transcript/p017 s2 | 2006-02 (recalling ~1978) | ~1978 wedding | Danny | Annie (past) / Danny (past self) | character_report | Double nested reports; paraphrased. |
| S032 | speech | Danny recounts he recently asked who will support her walking behind the casket and she replied she wishes to do so alone, mirroring how she entered. | SC/transcript/p017 s3 | 2006-02 | Feb 2006 reported exchange | Danny | Annie (reported) | character_report | Casket walk plan, paraphrased attribution. |
| S033 | speech | Annie affirms with a minimal acknowledgment. | SC/transcript/p018 | 2006-02 | Feb 2006 | Annie | — | character_report | Minimal acknowledgment, not elaboration. |
| S034 | belief_or_evaluation | Danny reflects on the difficulty of coming to terms with dying, says he has not yet done so, and wants to be sure she understands the extent and endurance of his love. | SC/transcript/p019 s1 | 2006-02 | Feb 2006 | Danny | — | belief_expression | Endurance is evaluative future belief; paraphrased. |
| S035 | belief_or_evaluation | Danny says the only gift he had to give her was himself, which he consistently did, and expresses a counterfactual wish to return if possible, then asks about a holiday letter. | SC/transcript/p019 s2 | 2006-02 | Feb 2006 | Danny | — | belief_expression | Counterfactual/hope paraphrased, not plan fact. |
| S036 | quoted_letter | Annie reads a Valentine’s letter paraphrased as marking the day as special, noting their shared love has grown over many years and now sustains them through difficulty, closing with an enduring-affection sign-off and holiday greeting. | SC/transcript/p020 | 2006-02 | Valentine’s Day (Feb, likely 2006) letter | Annie (reader) | Danny (author) | quoted_letter | Long-term love claim inside quoted letter, keep attributed; paraphrased, no verbatim body. |
| S037 | observed_event | Danny says she brings brightness to the morning by instructing him to place hands on her shoulders for support. | SC/transcript/p021 s1 | 2006-02 | daily morning habit, Feb 2006 described | Danny | Annie (quoted instruction) | habitual_asserted / belief_expression | Support ritual description, not clinical measure; paraphrased. |
| S038 | speech | Danny says she brings brightness at night through caring prompts about food and hydration, which though not conventionally romantic still move him emotionally. | SC/transcript/p021 s2 | 2006-02 | nightly habit | Danny | Annie (quoted) | character_report / belief_expression | Caring prompts paraphrased; evaluative response retained. |
| S039 | belief_or_evaluation | Danny expresses a belief in the uniqueness of Annie across past, present and future. | SC/transcript/p021 s3 | 2006-02 | atemporal belief (past/present/future) | Danny | — | belief_expression | Future-inclusive monogamous belief, not verifiable fact; paraphrased. |
| S040 | environment | Participants are identified as Danny Perasa and Annie Perasa (Brooklyn couple, nearly 30-year relationship by 2004). | SC/page/meta/p001 / SC/page/intro/p002 | 2004 | — | editorial | — | editorial_asserted | — |
| S041 | environment | Editorial mentions StoryCorps animation “Danny & Annie” and 2013 Annie update “Never Say Goodbye” exist as separate surfaces; they are pointers, not source for this fixture’s units. | SC/page/intro/p004 link area | — | — | editorial | — | editorial_asserted | Do not merge 2013 update content into 2004/2006 units. |
| S042 | environment | Home interview location is Brooklyn (from editorial: StoryCorps went to their home in Brooklyn). | SC/page/intro/p003 s3 | 2006-02 | Feb 2006 | editorial | — | editorial_asserted | Location from editorial, not inferred. |

> Total: **42 atomic units**（S001–S042），满足 #25 约 30–60 目标；材料层以 paraphrase 保留原文语义，压缩 verbatim 引用长度以符合 fair use；除个别极短通用短语外无原文照搬。

## 5. Frozen temporal / knowledge boundaries

后续 replay / verifier 必须遵守以下信息边界，不得把结局倒灌：

- `K0_editorial`: 知道 2004 与 2006 两次录制的存在及身后追记（S006–S007 死亡/追思），但以下 `K1/K2` 内部切片各自隔离。
- `K1`（2004-08-11 首次访谈切片，S001–S025）：人物尚无 2006 终末诊断；所有关于 shelter / color TV / daily notes / busted radio 的陈述只能在“长期婚姻回顾”语境下解释，不得用 cancer/finality 重写其 motive。
- `K2`（2006-02 Brooklyn home 切片，S026–S039）：人物已知 terminal diagnosis 与 one-week horizon；所有关于 finality / hope-she’ll-do-well / casket walk / Valentine letter / ice-cream-water 的陈述在此知识下产生，但 `K2` 的信息不得回写到 `K1` 的更早回忆（如把 1978 proposal motivation 用 2006 临终心境解释）。
- `K3`（Editorial posteriori, S006–S007/ S008 rebroadcast）：Annie 读信 2006–2021、2021 年去世等为后视信息，仅供完整 provenance，不得作为访谈当下人物 belief 的证据。
- `Recording vs recalled`：凡 S009–S012、S031 涉及 1978 事件，其 `event_time` 为 1978，`recording_time` 为 2004/2006；下游不得把 `recording_time` 当 `event_time`。
- 知识泄漏禁令：Danny 2021 身后追记、动画、2013 update 的语义不得回填到 S009–S039 的人物当下 knowledge。

## 6. Eye / Juece 可消费性

- 本包遵循 `Eye → Juece → LHRM` 链路设计（`#23`；Juece 合同以 `#23` 定版为准）：
  - Eye 已提供 `pointer-only` handoff + 真实 `rights_policy` + provenance（`HUMAN_REVIEW_REQUIRED`），未提供 `Representation` block；本包的 `SC/...` anchors 为 LHRM 侧人工短锚点，遵守 `no body persisted` 边界。`SC/...` 仅为材料定位，不等同 Eye `block_id`。
  - Juece 侧以 `unit_ref -> claim_refs[]` 消费本包：每个 `Sxxx` 可按语义拆为 1..N 个原子命题对应的 `Claim`（`kind: FACT | OPINION`，保留 `speaker_ref / reported_speaker_ref / source_anchor / lineage_status`）；`observed_at` 为证据观测/获取时间（Juece Evidence 观测侧），`recording_time / event_time / knowledge_time` 为故事内时间与知识切片侧的独立语义，需在 adapter/sidecar 中分别保留，不得将 `recording_time` 等同于 Juece `observed_at`；经 `ClaimEvidenceLink + EvidenceLineageEdge` 再由 LHRM thin adapter 消费。fixture-unit 数量不等于 Claim 数量（1:N）。
  - LHRM 测 `speaker attribution / memory time / belief vs observation / metaphor / nested quote` 时，应对下列情况报 `PARTIAL_MAPPING / MULTI_MAPPING / UNKNOWN / MAPPING_FAILURE` 而非现场发明 construct：
    - 隐喻（S017/S023/S024/S027）是否可落到 latent state 仍保持区分；
    - 转述引语（S009–S012/S030–S032/S036）的双层 attribution；
    - 信件朗读（S020/S022/S036）的 `reader vs author`；
    - habitual vs episodic（S014/S018/S037/S038）。

## 7. Downstream validation rule

本包是**输入**，不是映射结果。

每个 Verifier 必须在同一冻结 LHRM schema（`CURRENT_ARCHITECTURE.md + PARAMETER_CONVERGENCE_V0_1.md + CONSTRUCT_SCOPE_DIRECTIONALITY.md @ f237784`）下对 **全部 S001–S042** 独立给出映射 verdict：`DIRECT_MAPPING | PARTIAL_MAPPING | MULTI_MAPPING | NARRATIVE_ONLY | IRRELEVANT | UNKNOWN | MAPPING_FAILURE`，并按 `#15` 保留 `uncertainty / ambiguity note`。  
`PARTIAL / MULTI / UNKNOWN / FAILURE` 为合法结果，不得通过改写本 fixture 或新增 LHRM construct 来“修复”输入。  
三个 Verifier 必须消费同一个 `main` 合并后的 exact file 版本，并报告 `direct / partial / multi / unknown / failure` 计数与 `ad_hoc_parameter_required`。

---
### Appendix — Rights & reuse note

- Source rights remain with StoryCorps; this file contains **no transcript body mirror**, only faithful paraphrases with `SC/...` anchors for research fair use. Aside from unavoidable very short generic phrases, no nontrivial verbatim transcript or letter text is reproduced. Reproducing the full modal transcript or audio into the repo or as Eye `RawEvidence` remains prohibited until an explicit versioned rights clearance (Eye `HUMAN_REVIEW_REQUIRED` → `RAW_ALLOWED` transition) is granted. Alternative search-feed or podcast mirror bytes must not be presented as the canonical story evidence.
- Eye provenance for batch review: `youling/eye#60` live-validation logs (200 StoryCorps canonical 118031 bytes, modal semantic paragraphs; 404 prior-suffix, sitemap lookup; `robots.txt Content-Signal search=yes,ai-train=no,use=reference`) are the durable external evidence for address truth; LHRM does not duplicate Eye local artifacts.
