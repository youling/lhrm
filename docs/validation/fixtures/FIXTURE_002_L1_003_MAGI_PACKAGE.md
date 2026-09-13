# Fixture 002 — L1-003 《The Gift of the Magi》冻结叙事包

状态：**CANDIDATE FOR ARCHITECT REVIEW / NO LHRM MAPPING**  
父任务：`#24`，并服务 `#23` Juece compatibility pressure-test。  
准备者：LHRM Project Architect（2026-09-14）。原 Fresh Research lane 尚未产生 durable delivery；为保持项目推进，本包由 Architect 仅做**材料清洗与冻结**，不参与后续独立 mapping verdict。  

## 1. Source / provenance

- 作品：O. Henry, *The Gift of the Magi*
- Project Gutenberg eBook: `7256`
- canonical landing page: `https://www.gutenberg.org/ebooks/7256`
- acquired HTML used by Eye/LHRM: `https://www.gutenberg.org/files/7256/7256-h/7256-h.htm`
- Gutenberg source metadata: release 2005-01；页面标注 most recently updated 2021-12-25。
- 作品文本在美国为 public-domain；本仓库不镜像全文，只保存忠实 paraphrase 与定位锚点。
- Eye consumer contract 已于 `youling/eye#55` 合并到 Eye main：merge commit `2b4823901fa6926f1f66d2e3971ccc412c330047`。
- Eye 已对本材料证明 `eye-evidence-handoff/0.1` + `long-text-anchored/0.1`：真实抓取约 37,874 bytes，并产生 85 个 anchored blocks。LHRM 本文件不复制 Eye 本地 artifact；后续可从当前 Eye main 重放并把 stable evidence refs 追加为 provenance，不改变下列 frozen unit semantics。

### Normalized source anchor convention

本包把 Gutenberg HTML 中 `*** START OF ... ***` 后、正文标题之后的故事正文按**非空 prose paragraph**顺序编号为：

`PG7256/body/p001 ... PG7256/body/p049`

该编号只用于冻结本次输入语义；它不是 LHRM construct，也不替代 Eye block id。未来若 Eye parser/version 变化，只允许追加 `Eye representation/block ref -> PG7256/body/pNN` 对照，不得静默改写 unit 内容。

## 2. Freeze rules

1. 只保存故事中的 event / speech / thought-belief / plan / narrator-description / metaphor-evaluation / environment。
2. `said != believed != true`；人物说法、人物想法和故事世界叙述分层保留。
3. narrator 的审美/道德/夸张判断不升级为客观 latent relationship state。
4. Della 出售头发在她告诉 Jim 之前，不得写入 Jim 的 knowledge；Jim 出售手表在结尾披露之前，不得写入 Della 的 knowledge。
5. 不把结局信息倒灌到更早的 sequence。
6. 不做任何 `Liking / RomanticAttraction / SexualDesire / Trust / AttachmentSecurity / Caregiving / Dedication / OutcomeDependence` mapping。
7. 后续三个独立 Verifier 必须消费**同一个 merged exact version**；不得自行重写事实包。

## 3. Atomic narrative / fact units

`fact_or_narrative_status` 使用材料层状态，不表示法律真值：`story_world_asserted | habitual_asserted | character_report | character_thought | narrator_evaluation | figurative_expression`。

| unit_id | unit_type | faithful_paraphrase | source_anchor | story_time / sequence_index | speaker_or_holder | fact_or_narrative_status | future_leakage_note |
|---|---|---|---|---|---|---|---|
| M001 | environment | Della 手头一共只有 1.87 美元，其中相当一部分是零散硬币。 | PG7256/body/p001 | T0 / 001 | — | story_world_asserted | 不推断家庭全部资产，仅限当时她可用的这笔钱。 |
| M002 | environment | 第二天是圣诞节。 | PG7256/body/p001 | T0 / 002 | — | story_world_asserted | — |
| M003 | observed_event | Della 因当前处境倒在旧沙发上哭了一阵。 | PG7256/body/p002 | T0 / 003 | Della | story_world_asserted | 不把 narrator 对“人生”的评论当事实。 |
| M004 | environment | 两人住在一个每周租金 8 美元、陈设寒酸的公寓。 | PG7256/body/p003 | T0 / 004 | — | story_world_asserted | — |
| M005 | environment | 楼下信箱和门铃都不好用，门牌写着 James Dillingham Young。 | PG7256/body/p004 | T0 / 005 | — | story_world_asserted | — |
| M006 | environment | Jim 的周薪曾约 30 美元，后来降到约 20 美元。 | PG7256/body/p005 | T0 / 006 | — | story_world_asserted | 不将收入自动映射成关系质量。 |
| M007 | observed_event | Jim 回家时，Della 通常称他为 Jim，并热烈拥抱他。 | PG7256/body/p005 | T0 / 007 | Della/Jim | habitual_asserted | 是 narrator 描述的习惯模式，不等于每次均发生。 |
| M008 | observed_event | Della 哭完后整理了脸，然后站到窗边。 | PG7256/body/p006 | T0 / 008 | Della | story_world_asserted | — |
| M009 | plan | Della 已经连续数月尽量省钱，目的是给 Jim 买圣诞礼物。 | PG7256/body/p006 | T0 / 009 | Della | story_world_asserted | 只冻结明确目的，不推断更高层 construct。 |
| M010 | thought_or_belief | Della 认为 1.87 美元不足以买到她想送给 Jim 的礼物。 | PG7256/body/p006 | T0 / 010 | Della | character_thought | 这是她的评价，不是物价模型。 |
| M011 | plan | 她此前多次设想给 Jim 找一件精致、稀有且配得上他的东西。 | PG7256/body/p007 | T0 / 011 | Della | character_thought | — |
| M012 | observed_event | Della 利用窄镜子观察自己的外表。 | PG7256/body/p008 | T0 / 012 | Della | story_world_asserted | — |
| M013 | observed_event | 她突然转向镜子，把头发完全放下来。 | PG7256/body/p009 | T0 / 013 | Della | story_world_asserted | — |
| M014 | narrator_description | Jim 的一件贵重私人物品是继承自父亲和祖父的金表。 | PG7256/body/p010 | T0 / 014 | narrator | story_world_asserted | “pride” 的程度不转成数值。 |
| M015 | narrator_description | Della 的长发被叙述为两人家中另一件格外珍视的东西。 | PG7256/body/p010 | T0 / 015 | narrator | narrator_evaluation | “珍视/漂亮”保留为叙述层，不映射 latent state。 |
| M016 | metaphor_or_evaluation | narrator 用 Sheba 女王的夸张比较来形容 Della 对自己头发的珍视。 | PG7256/body/p010 | T0 / 016 | narrator | figurative_expression | 非故事世界真实人物互动。 |
| M017 | metaphor_or_evaluation | narrator 用 Solomon 国王的夸张比较来形容 Jim 对金表的珍视。 | PG7256/body/p011 | T0 / 017 | narrator | figurative_expression | 非故事世界真实事件。 |
| M018 | observed_event | Della 的头发垂到膝盖以下；她随后又快速盘起头发，并流下眼泪。 | PG7256/body/p012 | T0 / 018 | Della | story_world_asserted | — |
| M019 | observed_event | Della 穿上旧外套和帽子，离开公寓上街。 | PG7256/body/p013 | T1 / 019 | Della | story_world_asserted | — |
| M020 | environment | 她到了一家经营头发制品、招牌写着 Mme. Sofronie 的店。 | PG7256/body/p014 | T1 / 020 | — | story_world_asserted | — |
| M021 | speech | Della 询问店主是否愿意购买她的头发。 | PG7256/body/p015 | T1 / 021 | Della | character_report | 此时 Jim 尚不知她的计划。 |
| M022 | speech | 店主表示收购头发，并要求先看头发。 | PG7256/body/p016 | T1 / 022 | Mme. Sofronie | character_report | — |
| M023 | observed_event | Della 把头发放下来给店主查看。 | PG7256/body/p017 | T1 / 023 | Della | story_world_asserted | — |
| M024 | speech | 店主给 Della 的头发报价 20 美元。 | PG7256/body/p018 | T1 / 024 | Mme. Sofronie | character_report | — |
| M025 | speech | Della 要求尽快成交。 | PG7256/body/p019 | T1 / 025 | Della | character_report | — |
| M026 | observed_event | 成交后，Della 花了大约两小时在商店里寻找 Jim 的礼物。 | PG7256/body/p020 | T2 / 026 | Della | story_world_asserted | — |
| M027 | observed_event | 她最终找到一条设计简洁的铂金表链。 | PG7256/body/p021 | T2 / 027 | Della | story_world_asserted | — |
| M028 | thought_or_belief | Della 看到表链后认为它特别适合 Jim，也配得上他的金表。 | PG7256/body/p021 | T2 / 028 | Della | character_thought | “像 Jim”是她/叙述的评价，不是客观人格测量。 |
| M029 | observed_event | Della 为表链支付 21 美元，之后剩下 87 美分。 | PG7256/body/p022 | T2 / 029 | Della | story_world_asserted | — |
| M030 | narrator_description | narrator 说明 Jim 当时用旧皮带代替表链，有时会低调地查看金表。 | PG7256/body/p022 | T2 / 030 | narrator/Jim | habitual_asserted | 不推断羞耻等未明说心理。 |
| M031 | observed_event | 回家后 Della 用卷发工具整理剪短后的头发。 | PG7256/body/p023 | T3 / 031 | Della | story_world_asserted | Jim 此时仍不知道她卖了头发。 |
| M032 | observed_event | 大约四十分钟后，她把短发整理成紧密小卷，并长时间照镜子检查。 | PG7256/body/p024 | T3 / 032 | Della | story_world_asserted | — |
| M033 | thought_or_belief | Della 担心 Jim 第一眼会强烈不喜欢她的新发型，并自问在只有 1.87 美元的情况下还能怎么办。 | PG7256/body/p025 | T3 / 033 | Della | character_thought | 这是预期/担忧，不代表 Jim 的真实反应。 |
| M034 | environment | 晚上 7 点左右，咖啡和煎锅已经准备好，晚餐尚待最后烹调。 | PG7256/body/p026 | T3 / 034 | — | story_world_asserted | — |
| M035 | observed_event | Jim 平时不迟到；Della 拿着表链坐在他惯常进门附近等待。 | PG7256/body/p027 | T3 / 035 | Della/Jim | habitual_asserted | “从不迟到”按 narrator 的习惯性断言保留。 |
| M036 | speech | 听见 Jim 上楼后，Della 低声祈求，希望 Jim 仍觉得她漂亮。 | PG7256/body/p027 | T3 / 036 | Della | character_report | 这是愿望，不是关于 Jim 当前 belief 的事实。 |
| M037 | observed_event | Jim 进门并关门。 | PG7256/body/p028 | T4 / 037 | Jim | story_world_asserted | — |
| M038 | narrator_description | narrator 描述 Jim 很瘦、神情严肃、22 岁，并缺少新外套和手套。 | PG7256/body/p028 | T4 / 038 | narrator | story_world_asserted | “burdened with a family”属 narrator framing，不单列客观因果。 |
| M039 | observed_event | Jim 进门后停住，持续盯着 Della；Della 无法读懂他的表情。 | PG7256/body/p029 | T4 / 039 | Jim/Della | story_world_asserted | 不提前用结尾解释 Jim 此刻为何震惊。 |
| M040 | thought_or_belief | Della 因 Jim 的难以理解的表情而害怕，并排除自己原先预想的几种反应。 | PG7256/body/p029 | T4 / 040 | Della | character_thought | 她对 Jim 情绪的分类是不确定观察。 |
| M041 | observed_event | Della 从桌边下来，朝 Jim 走过去。 | PG7256/body/p030 | T4 / 041 | Della | story_world_asserted | — |
| M042 | speech | Della 告诉 Jim：自己剪掉并卖了头发，因为她无法接受圣诞节不给他礼物。 | PG7256/body/p031 | T4 / 042 | Della | character_report | 这是 Jim 首次被明确告知头发出售原因。 |
| M043 | speech | Della 说头发会再长，询问 Jim 是否介意，并表示想一起开心过圣诞。 | PG7256/body/p031 | T4 / 043 | Della | character_report | 不把请求自动当 Jim 已接受。 |
| M044 | speech | Jim 反复确认 Della 是否真的剪掉了头发。 | PG7256/body/p032 + p035 | T4 / 044 | Jim | character_report | 只表示确认行为；不预先推断具体心理原因。 |
| M045 | speech | Della 再次说明头发已经卖掉，并问没有长发时 Jim 是否仍一样喜欢她。 | PG7256/body/p033 | T4 / 045 | Della | character_report | 问句不是 Jim belief 的证据。 |
| M046 | speech | Della 告诉 Jim 不必寻找头发，并说卖头发是为了他；随后以夸张措辞表达自己对他的感情难以计数。 | PG7256/body/p036 | T4 / 046 | Della | character_report | “无法计数”保留为人物表达，不转成强度数值。 |
| M047 | observed_event | Jim 从僵住的状态恢复后拥抱 Della。 | PG7256/body/p037 | T4 / 047 | Jim/Della | story_world_asserted | narrator 中关于贫富的评论另处理，不混入动作。 |
| M048 | observed_event | Jim 从外套口袋取出一个包裹，放到桌上。 | PG7256/body/p038 | T5 / 048 | Jim | story_world_asserted | 此时 Della 尚不知道包裹内容及 Jim 卖表。 |
| M049 | speech | Jim 告诉 Della，剪发等外表变化不会让他减少对她的喜欢，并让她打开包裹理解他刚才的反应。 | PG7256/body/p039 | T5 / 049 | Jim | character_report | 这是 Jim 自己的明确陈述；仍不自动量化。 |
| M050 | observed_event | Della 打开包裹后先表现出强烈喜悦，随后哭泣。 | PG7256/body/p040 | T5 / 050 | Della | story_world_asserted | — |
| M051 | narrator_description | 包裹里是一套 Della 曾长期想要、但认为自己难以拥有的昂贵发梳；现在发梳属于她，但她的长发已经不在。 | PG7256/body/p041 | T5 / 051 | narrator/Della | story_world_asserted | 关于她“渴望”的信息来自 narrator 回述。 |
| M052 | speech | Della 抱着发梳，平静下来后告诉 Jim 她的头发长得很快。 | PG7256/body/p042 | T5 / 052 | Della | character_report | — |
| M053 | observed_event | Della 随即想起 Jim 还没有看到她给他的礼物，并把表链拿出来给他。 | PG7256/body/p043 + p044 | T5 / 053 | Della | story_world_asserted | — |
| M054 | speech | Della 说自己跑了很多地方才找到表链，并让 Jim 拿出手表试试看。 | PG7256/body/p045 | T5 / 054 | Della | character_report | 此时她仍不知道手表已被卖掉。 |
| M055 | observed_event | Jim 没有拿出手表，而是坐/躺到沙发上，微笑。 | PG7256/body/p046 | T5 / 055 | Jim | story_world_asserted | 不先解释原因。 |
| M056 | speech | Jim 建议暂时把两人的圣诞礼物收起来，因为眼下无法使用。 | PG7256/body/p047 | T5 / 056 | Jim | character_report | — |
| M057 | speech | Jim 明确告诉 Della：他已经卖掉自己的金表，用所得的钱给她买了发梳。 | PG7256/body/p047 | T5 / 057 | Jim | character_report | 这是 Della 首次得知手表出售；此前切片不得倒灌。 |
| M058 | speech | Jim 在披露卖表后建议 Della 去准备晚餐。 | PG7256/body/p047 | T5 / 058 | Jim | character_report | — |
| M059 | narrator_description | narrator 总结两人都为给对方送礼而牺牲了各自最珍贵的财物，导致礼物暂时失去实际用途。 | PG7256/body/p048 | T6 / 059 | narrator | narrator_evaluation | “牺牲/最珍贵”是叙事总结；下游可拆事件但不得当作 primitive 参数。 |
| M060 | metaphor_or_evaluation | narrator 把两人称作“愚蠢的孩子”，同时把他们与圣经中的 Magi 作比较。 | PG7256/body/p048 | T6 / 060 | narrator | figurative_expression | 文学/道德评价，不是事实状态。 |
| M061 | metaphor_or_evaluation | narrator 最终评价两人在赠礼者之中反而是“最智慧的”。 | PG7256/body/p049 | T6 / 061 | narrator | narrator_evaluation | 结尾价值判断必须保持 Derived/Narrative 层。 |

## 4. Frozen knowledge boundaries

后续 replay / verifier 至少应遵守以下信息边界：

- `K1`: M001–M041：Jim 尚未从文本中得知 Della 已卖掉头发；Della 已知自己的出售与购链计划。
- `K2`: M042–M048：Jim 已知 Della 卖头发；Della 尚未知 Jim 的发梳礼物及卖表事实。
- `K3`: M049–M056：Della 已知 Jim 买了发梳，但**仍未被明确告知** Jim 为此卖掉金表。
- `K4`: M057 之后：Della 得知 Jim 卖表；此前时间切片不得使用这一事实解释她的先前 belief。

## 5. Downstream use

本文件冻结的是**统一输入材料**，不是 LHRM mapping result。

后续允许：

`source / Eye anchor -> Juece Claim candidate -> LHRM mapping`

后续禁止：

`结局已知 -> 回写早期人物知识`  
`narrator metaphor -> 直接设定 latent construct`  
`speech -> 自动当真`  
`question/request -> 自动当对方 belief`  

若 Verifier 认为某 unit 过度合并，应标 `PARTIAL_MAPPING / MULTI_MAPPING / MAPPING_FAILURE` 或记录 fixture-granularity concern；**不得在验证过程中自行改写本文件。**
