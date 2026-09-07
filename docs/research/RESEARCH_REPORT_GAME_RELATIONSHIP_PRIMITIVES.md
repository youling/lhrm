# RESEARCH_REPORT_GAME_RELATIONSHIP_PRIMITIVES

```yaml
work_coordinate: youling/lhrm#3@deep-game-relationship-primitives
dispatch: youling/lhrm#3 issuecomment 5565247050 (ARCHITECT_RESEARCH_DISPATCH_V2)
supersedes: youling/lhrm#3 issuecomment 5565094319 (prior dispatch, current scope)
parent: youling/lhrm#2
current_rulings:
  - youling/lhrm#2 issuecomment 5565170990 (scope: general relationship system, non-hetero default, decoupling test)
  - youling/lhrm#2 issuecomment 5565245810 (domain boundary: human–human dyad; mechanism|primitive_state|observable_proxy|derived_outcome|role_constraint; minimal sufficiency)
role: Research
startup_mode: Fresh Research
status: DRAFT_FOR_ARCHITECT (研究交付物；不改写 canonical ontology)
as_of: 2026-09-07
language: zh-Hans
unit_of_analysis: Human–Human Dyad (两个具体的人及其关系边)
evidence_scale: E1/E2/E3/C/M（见 §2.1；对游戏来源标注设计真值等级）
```

本报告是 `youling/lhrm#3` 下、按 `ARCHITECT_RESEARCH_DISPATCH_V2`（comment `5565247050`）执行的深研交付。它回答：**游戏/生活模拟/恋爱模拟如何表示关系状态与亲密度？其中哪些表示法在 Human–Human Dyad 上值得作为 LHRM 最小充分 primitive 候选、哪些只是 observable_proxy / derived_outcome / role_constraint？** 本报告是研究产物，不冻结任何数值/权重，不修改 canonical ontology；全部建议交由 Project Architect 在 `#2` 统一仲裁。

---

## 0. Acknowledged Rulings

- `#2 5565170990`（scope amendment）：研究范围是**一般人际关系系统**，不是异性恋婚恋系统。不得默认异性、不得默认从陌生人开始、不得默认婚恋为唯一目标、亲缘不自动排除性/浪漫表达；必须覆盖同性/异性、亲缘/非亲缘、既有关系/分手/前任/第三者等形态。
- `#2 5565245810`（domain boundary）：研究域冻结为 **Human–Human Dyad**；动物/神经/生物研究只作为机制证据（mechanism evidence），不向下扩对象；目标是"最小充分关系状态变量"；更低层术语必须证明"语义独立性 + 预测充分性 + 可操作测量价值"才可能进入。
- 本报告把游戏视为**设计者故意构造的"玩具定律"**（toy laws）：它们的机制忠实记录于官方/社区 wiki，是"人工形式化系统的真值"，但其博弈目标未必模仿真实人类认知。因此游戏证据的推论价值是（a）证明某种状态表示法在交互循环中**可建模、可观测、可驱动进程**；（b）**跨游戏、跨类型独立趋同**的机制簇提示形式化结构；（c）角色/叙事的"民间智慧"提供可查证的代理词命名。游戏机制本身不足以作为人类关系高强度的实证。

---

## 1. 任务、边界与本报告地位

### 1.1 本报告做什么

- 调查 ≥12 个代表性游戏/生活模拟/恋爱模拟系统，记录其**关系状态的表示方式、更新时间、衰减规则、事件触发、角色约束**（§3）。
- 提取 ≥30 条"游戏机制词 → 关系科学构念候选"的映射示例，并标注五分类层（§4）。
- 对当前 LHRM 六维候选（Attraction / Bond / Trust / Commitment / Alignment / Dependence）给出游戏侧证据的 KEEP / SPLIT / MERGE / DERIVED / REJECT 裁决（§5），与 `#4` 科学版裁决互校。
- 给出重复计数风险（§6）、游戏 UI 表达的可迁移性（§7）、动力学特征汇总（§8）、assumption_stress_test（§9）、学术校准（§10）与剩余不确定性（§11）。

### 1.2 本报告不做什么（boundary）

- **不修改 canonical ontology**；不冻结数值、阈值、公式。
- **不把游戏机制当人类行为的实证**（见 §0、§2.1）：游戏只能佐证"可建模性/可表现性"，不能佐证"人真是这样"。
- **不以异性恋婚恋为默认模板**；恋爱模拟类游戏（如 Tokimeki Memorial）仅作为极端压力样例，不作为默认形态。
- **不为叙事服务而堆叠参数**：游戏的"剧情丰富度"诉求不等于人类关系建模需求；只提取有动力学意义的表示。
- **不与兄弟报告重复**：`#4`（科学构念）、`#6`（真实世界代理拆解）已有它们的切面，本报告聚焦"游戏作为人工形式化系统"这个证据源。

### 1.3 术语口径

沿用 `#2 5565245810` 的五分类（与 `#4` 报告一致）：

| 类别 | 含义 |
|---|---|
| `mechanism` | 解释"为何如此"的更低层机制/证据（游戏侧很少，若有则如"好感动画/数值演出"，仅作解释层） |
| `primitive_state` | 最小充分的关系状态变量：可作为模型状态、随事件更新、驱动转移 |
| `observable_proxy` | 可直接观测/汇报/测得的指标，用来向上推断 primitive 或向下被 primitive 解释 |
| `derived_outcome` | 由若干 primitive 计算出的高阶结果（关系质量、整体"好感分"、婚姻满意） |
| `role_constraint` | 由角色/契约/阶段/身份强加的条件（婚姻、亲缘、前任、伴侣排他、游戏中的 status） |

层标注沿用 `#2` 的 S/O/D/E 视图：primitive 大多落在有向 dyad 边（D）或 per-agent（S），E 为约束/上下文（如社区声誉、多边旁观者）。

### 1.4 游戏侧证据的特殊语义

游戏关系状态有一个独特性质：**它是显式可见/半透明的形式化状态**（设计者编码、玩家可查）。因此"游戏如何拆分『好感』"直接暴露设计师的隐式本体论，是一份可以复用的"人工 schema"，但不是测量学数据。本报告对每条游戏证据同时给出：设计真值等级（G2 官方 wiki / 抓取真值、G3 社区 wiki、G4 未在会话内抓取的一般知识）与推论强度（对形式化的支持强度）。

---

## 2. 方法：证据与最小充分性判据

### 2.1 证据分级（游戏域适配）

| 等级 | 含义（游戏域） |
|---|---|
| `G2 designed-truth` | 机制来自官方文档/游戏内数据/可靠社区 wiki 可确证，代表"设计者故意构造的真值" |
| `G3 community` | 来自社区 wiki / 数据挖掘 / 玩家整理，机制基本可确证但细节有变体 |
| `G4 unverified` | 会话内未直接抓取、基于一般游戏知识的陈述，仅作补充，需核实 |
| `E*` | 引用的学术/经验证据沿用 `#4` 的 E1/E2/E3/C/M 定义（§10） |

> 推论纪律：`G2/G3` 证明的是"该系统确实如此表示"。要把它升格为"人类 dyad 的 primitive"仍需：跨系统趋同 + 与 `#4/#6` 的科学定义对齐 + MSC 判据。本报告通篇避免把设计真值说成人类经验事实。

### 2.2 方法与视角

- 每个系统记录：关系状态表示 → 更新触发 → 衰减规则 → 事件门 → 角色/身份约束 → 方向性（有向/无向/pair）。
- 全部系统先按"家族"归类（礼物/喜好门控型、双轴仪表型、事件日志型、等级+旗帜型、隐藏状态型、极简单元型），再在 §4/§5 做跨家族聚合。
- 对每个跨系统聚合出的"机制簇"，用 MSC（`#4` §2.3）检验，落入 §5 裁决。

---

## 3. 系统调查：13 个代表性的关系表示法

> 方向性标记：`有向` = A→B 独立于 B→A；`无向/pair` = 只有一个"我们"值；`旗标` = 分类状态（恋爱、已婚、仇敌…）。

### S01 Stardew Valley（星露谷，2016）

- 状态表示：对每个 NPC 独立的热情值（Friendship 0–2500，10 心；婚后 14 心）。旗标：dating（8 心+花束）、married、divorced。
- 更新触发：每日对话(+20)、礼物（爱 +80 / 喜欢 +45 / 中性 +20 / 讨厌 −20 / 恨 −40）、事件；**连续 ≥2 天不互动则衰减**；婚后不衰减。
- 事件门：心事件按分数阈值解锁剧情；约会/求婚有心的门槛。
- 揭示线索：单轴"好感"其实混装了（喜欢的增强、礼物所体现的"懂对方"、阶段里程碑）；衰减只发生在 non-institutional 阶段（婚前），婚后由"角色约束"接管维护。
- 方向性：每个 villager 对玩家的值是独立的（有向）；玩家角度无可见球迷宫中聚合。
- 来源：https://stardewvalleywiki.com/Friendship （G3，会话内抓取成功）

### S02 Rune Factory 4（符文工厂，2012）

- 状态表示：**FP（友好度）与 LP（恋爱值）双轴分开**，各自累计点数；告白/订婚/结婚以 LP 门槛为门。
- 揭示线索：游戏界罕见的"友好 ≠ 恋爱"显式分离，支持 Attraction 拆分为"亲和喜欢"与"浪漫/性吸引"两轨。
- 方向性：有向（每个候补对象各自计量）。
- 来源：https://therunefactory.fandom.com/wiki/Relationships_(RF4) （G3；会话内部分页面 transport 失败，以搜索快照补齐）

### S03 The Sims 系列（2/3/4，2000–）

- 状态表示：`好友度` 与 `浪漫度` 两个独立量尺；Sims 4 增设 `每日关系 vs 终身关系` 与 `Sentiments`（事件触发的限时情感）、`Relationship Bits`（分类关系标签）。Sims 3 即已区分 long-term / short-term。
- 衰减：两量尺随时间自然衰减（无互动/浪漫冷落）。
- 事件触发：第一次接吻、出轨被抓、吵架等生成 Sentiment 与标签。
- 揭示线索：①好友/浪漫双量尺 = liking 与 romantic desire 解耦；②短期/长期双表 = 双时间尺度（冲动态 vs 沉淀态）；③Sentiment = 事件触发的**瞬时情绪状态**，与长期量尺分工；④Relationship Bits = 分类边标签（情侣/敌人/前任），与数值量尺正交。
- 方向性：Sim 对玩家的值有方向；家族关系面板展示多人多边。
- 来源：https://sims.fandom.com/wiki/Relationship ；https://sims.fandom.com/wiki/Sentiment （G3；会话内 transport 出错，以搜索快照与系列知识补齐）

### S04 Dragon Age 2（龙腾世纪 2，2011）

- 状态表示：单一双极性好感条，两端为 friendship / rivalry；**rival 也能推进浪漫**（rivalmance），甚至与 high-friendship 不同的人物挣扎关系更"深"。
- 揭示线索：最有力的解耦证据——**commitment/浪漫推进可以发生在 low-liking 轴上**；"喜欢"不是推进关系承诺的必要条件（互补/冲突型相容）。
- 方向性：有向（每个同伴对该角色）。
- 来源：https://dragonage.fandom.com/wiki/Friendship_and_rivalry （G3，会话内抓取成功）

### S05 RimWorld（环世界，2018）

- 状态表示：每个 pawn 对其他 pawn 的 **Opinion（有向整数）**，由最近社交日志（好事/坏事、加/减）累加；关系类型边：lover / spouse / ex-lover / ex-spouse / affair。
- 更新触发：社交行为（谈话、安慰、求婚、拒约、背叛事件）；**求婚被拒 −10/−15、成功 +35**；出轨被抓 moodlet。
- 衰减：Opinion 由"近期社交记录窗口"驱动，旧好事逐渐退出窗口（隐形衰减）。
- 揭示线索：①Opinion = 事件记忆聚合的 summary proxy（derived），不是独立 primitive；②接受/拒绝**不对称**（成功大正、被拒小负）呼应"接受即奖赏、被拒即伤害"（Leary 社会计）；③lover/spouse/ex 等**分类边与数值边并存**；④出轨 = 多对并存边（multiplicity 来自多条边而非新变量）。
- 方向性：有向（A 对 B 与 B 对 A 独立）。
- 来源：https://rimworldwiki.com/wiki/Social （G3；直抓 403，以搜索快照记录）

### S06 Crusader Kings 3（十字军之王 3，2020）

- 状态表示：Opinion（有向 −100…+100，短期修饰随时间衰减 + 长期修饰持久）；关系类型：Friend / Rival / Lover / Soulmate；Hook（对本人的把柄/秘密）与 Scheme（浪漫/勾引计划、成功率与暴露）；性取向为角色属性门控浪漫交互。
- 揭示线索：①短期/长期修饰分离 = 双时间尺度；②Friend/Rival 等**分类边与 Opinion 数值是两个独立变量**（分类跳变不必然等于数值连续变化）；③Hook/秘密 = **信息与权力不对称层**（leverage），提示 dependence/power 是有方向、可变现的结构；④婚姻多为政治契约 = role_constraint 与 dedication 分离的例证。
- 方向性：有向（长短期).
- 来源：https://ck3.paradoxwikis.com/wiki/Opinions 、Character https://ck3.paradoxwikis.com/wiki/Character （G3，会话内抓取成功）

### S07 Dwarf Fortress（矮人要塞，2006–）

- 状态表示：关系类型阶梯（spouse / lover / kindred spirit / close friend / friend / acquaintance / grudge…），形成于阈值（相处时长/事件）；配偶、子女、前任等亲属边；同性婚姻常见；分手/误解会产生 grudge。
- 衰减/遗忘：**grudge 长期不忘**，acquaintance 在长期别离后可能被遗忘（退化）。
- 揭示线索：①定性阶梯（tier）+ 阈值 = "阶段/里程碑"表示；②**负面的持久性远强于正面遗忘**（负性不对称，呼应傅里叶/社会心理学 negativity bias）；③亲缘/婚姻/情感三层边混存（role 与 bond 分开）；④同性婚配自洽 = 语义跨形态稳定。
- 方向性：有向（每 dwarf 各自的 relation 表）。
- 来源：https://dwarffortresswiki.org/Relationship （G3，会话内抓取成功）

### S08 Persona 4 / 5（女神异闻录，2008/2016）

- 状态表示：Social Link / Confidant 等级 1–10 + 隐藏点数；靠对话/花时间（日历时间块）升级；**浪漫是特定等级对话选项产生的 flag**（P5 通常 rank 9 前后），友谊与恋爱共用同一等级楼梯直到 flag；多线恋爱 → 情人节"多人惩罚"事件。
- 揭示线索：①时间预算 = 机会成本与投入（investment proxy）；②同一楼梯 + 末尾 flag = 游戏把"喜欢/亲密度"与"浪漫关系"共用一个增长轴，只有 flag 处分开——**这就是 games 最常见的"共轴 + 旗标"模式**，与理论要求（浪漫 desire 独立轴）相左，反而是负面样例；③多线惩罚 = 多条 commitment flag 并存引发冲突检测。
- 方向性：pair-ish（等级是玩家↔对象的公共值）；flag 单向（玩家发起）。
- 来源：https://megamitensei.fandom.com/wiki/Social_Link （G3；部分 transport 失败）；gamerhorizon.blog 的 P4 romance 整理（G4）；会话内以搜索摘要为准

### S09 Fire Emblem: Three Houses（火焰纹章：风花雪月，2019）

- 状态表示：support points（战斗/训练/用餐累积）→ 阈值解锁 C / B / A 支援对话；S 支援（结局配对）为中止档选择；**同性 S 支援仅限部分角色**。
- 揭示线索：①阈值+里程碑事件（阶段门）；②S 支援 = 单向显式配对声明（commitment 的仪式化）；③同性支援受角色清单限制 = **identity/角色约束**可变，不是 primitive 不稳定。
- 方向性：pair-ish 支援值 + 单向 S 选择。
- 来源：https://fe3h.com/support_points （G3，数据挖掘，会话内抓取成功）

### S10 Tokimeki Memorial（心跳回忆系列，1994）

- 状态表示：隐藏好感度（不直接显示）+ 可观测参数（学力/容姿/运动…）+ 称号；约会邀请/拒绝、嫉妒炸弹（其他女生好感下降/坏话）、毕业告白阈值与炸弹清零条件。
- 揭示线索：①**hidden 状态 vs 可见 proxy 分离**（好感不可见，参数与其行动相关）——这是"部分观测/belief"预演；②炸弹 = 多边第三方嫉妒循环（同一群体中其他竞争者的情绪反作用于 dyad），提醒多边效应应由 per-pair 状态推导而非全局"嫉妒"变量；③约会被拒是长期负面事件（path dependence）。
- 方向性：有向（每位候补对玩家）；第三方边存在。
- 来源：https://namu.wiki/w/두근두근%20메모리얼~forever%20with%20you~ （G3，会话内抓取成功；页面为韩语社区整理）

### S11 Monster Prom（怪物舞会，2018）

- 状态表示：可见属性（SMARTS / BOLDNESS / CREATIVITY / CHARM / FUN / MONEY）+ **隐藏 LOVE POINTS**（每攻略对象各自累积，由选项加权）；属性门槛门控场景；事件与多线竞争。
- 揭示线索：①可见"资格属性"与隐藏"真实好感"分工 = desirability proxy vs affect latent；②多对象并行时选择本身即代价；③Love 隐藏 = 部分观测/信息策略（玩家不知对方确切态度）。
- 方向性：有向隐藏值 + 玩家属性（S 层）。
- 来源：https://monsterprom.wiki.gg/wiki/Stats （G3，会话内抓取成功）

### S12 Skyrim（上古卷轴 5，2011）

- 状态表示：极简——聊几句好感达阈值、戴 Amulet of Mara 出现求婚对话、"娶不娶"立即定；婚后关系几乎不再有状态；另有派系声望/好感（faction disposition）供任务门控（此为 group-context 状态）。
- 揭示线索：**极简反面**：无衰减、无阶段、无双轴——证明"缺少管理动机时设计者可以完全不建模"，也就是说关系状态的建模量与**玩法目标**强耦合；同时派系声誉是"环境/群体视角"状态（E 层），区别于 dyad 边。
- 方向性：pair-ish flag。
- 来源：https://en.uesp.net/wiki/Skyrim:Marriage （G4 补充，会话内未抓取；基于稳定设计知识）

### S13 Mass Effect 系列（质量效应，2007–）

- 状态表示：同伴批准（approval）随关键剧情选择涨跌；忠诚任务；浪漫沿剧情 auto-lock（一旦选长期伴侣进入"一段锁定"）；paragon/renegade 声誉（全局）。
- 揭示线索：①爱情常"略过漫游期直接进锁定" = path-dependence 与 lock-in 由决策序列造成；②全局声望（paragon/renegade）是**独立于 dyad 的第三人称声誉轴**。
- 方向性：有向 approval；lock-in 旗标。
- 来源：https://masseffect.fandom.com/wiki/Romance （G4 补充，会话内未抓取）

---

## 4. Proxy → 构念映射（≥30 条）

> 列：游戏机制/状态词（来源系统）→ LHRM 构念候选（层）→ 关键推理。`层` 为五分类。用 `#`/`#4`/`#6` 前缀关联兄弟报告的同一构念（名称对齐 `#4` §4）。

| # | 游戏机制/状态词 | 系统 | LHRM 构念候选（层） | 推理 |
|---|---|---|---|---|
| M01 | 对 NPC 独立好感分 0–2500 | SDV | positive regard / liking（D，有向 primitive） | 每对象各自计量 ⇒ 有向 per-pair 状态 |
| M02 | 爱/喜欢/讨厌/恨礼物 ±80…−40 | SDV | value/preference congruence（pair 属性）与 perceived responsiveness | "懂对方喜好并按之行动"是关系深化主手段 |
| M03 | 每日对话 +20 递增上限 | SDV | familiarity / acquaintance（D，暴露累积） | 仅暴露本身生成温和正向（mere exposure） |
| M04 | 连续 2 日不互动衰减 | SDV | neglect-decay 规则（primitive 动力学） | 弱表态下不维护即退化 |
| M05 | 婚后不衰减 | SDV | role_constraint 改变维护底线 | 婚姻契约把"默认不散"外置 |
| M06 | 心事件按阈值解锁 | SDV | stage / milestone（role_constraint + derived staging） | 阶段门 = 里程碑事件门槛 |
| M07 | 8 心+花束才可约会/求婚 | SDV | stage gate + declaration（role_constraint） | 显式声明/仪式改变角色 |
| M08 | 离婚后抹除记忆 | SDV | dissolution + belief 重置（derived） | 解除的副作用：清空部分历史 |
| M09 | FP/LP 双轴分开 | RF4 | liking（D）与 romantic/sexual desire（D）解耦 | SPLIT 直接证据 |
| M10 | 好友度 vs 浪漫度双量尺 | Sims | liking 与 romantic desire 两轴 | 跨游戏（RF4、Sims）趋同 ⇒ 强信号 |
| M11 | 短期关系 vs 终身关系 | Sims/Sims3/4 | transient 冲动态 vs 长期 bond（双时间尺度） | 短期＝快速变动层，长期＝慢变量 |
| M12 | Sentiment（限时情感） | Sims4 | event-triggered 瞬时情绪状态（derived/proxy） | 事件产生短暂显式标签，与量尺分工 |
| M13 | Relationship Bits 标签 | Sims4 | 分类边标签（lover/enemy/ex） | 数值与分类正交并存 |
| M14 | Turn on/off 偏好 | Sims | preference-orientation（S，gating 属性） | 择偶偏好是 Agent 平移属性而非 dyad 状态 |
| M15 | 出轨被抓声誉 | Sims | social/community approval（E，constraint） | 第三方视角声誉 ≠ dyad 状态 |
| M16 | friendship/rivalry 双极性单轴 | DA2 | valence 单轴 summary（derived） | 单一轴吞并多种内容 ⇒ 模型应拆 |
| M17 | rivalmance（rival 推开爱情） | DA2 | commitment 与 liking 解耦（decoupling 案例） | **低喜欢 ≠ 低承诺**：commitment 独立 |
| M18 | Opinion（有向整数） | RimWorld / CK3 | attitude summary（derived，不计 primitive） | 数值 = 事件记忆聚合 ⇒ 可用作观测输出 |
| M19 | 近期社交记录滑动窗口 | RimWorld | event-memory 带衰减（mechanism/proxy） | 提供"最近事件决定瞬时印象"的近因层 |
| M20 | 求婚成功 +35 / 被拒 −10/−15 | RimWorld | acceptance/rejection 奖罚不对称（primitive 动力学） | 接受大正、拒绝小负 ⇒ 不对称更新 |
| M21 | lover/spouse/ex/affair 边 | RimWorld | bond 类型边 + 同时并存多边 | multiplicitate 来自边集合，非新 primitive |
| M22 | 出轨 moodlet | RimWorld | 背叛/信任破坏事件（event） | 触发 trust 的负面更新 |
| M23 | 分手/丧亲 moodlet | RimWorld/DF | attachment 中断 → grief（derived） | 依恋断开有可观测代价 |
| M24 | 短期/长期 opinion 修饰 | CK3 | 快慢双时间尺度 | 同上 M11，独立来源 |
| M25 | Secret + Hook 把柄 | CK3 | 信息/权力不对称 → power / dependence（D，有望 primitive） | 可动用杠杆是有方向的结构状态 |
| M26 | 性取向门控浪漫 scheme | CK3/Persona | sexual orientation（S，gating 属性） | 身份层决定行为上限，非关系状态 |
| M27 | 对多人同时浪漫 scheme | CK3 | simultaneous courtship（多对并存） | 由边集合表达，无需全局花心变量 |
| M28 | 婚姻=政治契约 | CK3 | 制度/契约约束（role_constraint） | dedication 与 contract 分离的证据 |
| M29 | 关系类型阶梯 | DF | qualitative bond tier（derived stage） | 阈值切阶段 = 可数阶梯 |
| M30 | grudge 长期不忘 / acquaintance 遗忘 | DF | 负性不对称（primitive 动力学） | 遗忘方向不对称：敌意持久、温情流失 |
| M31 | 亲属/配偶/子女边 | DF/CK3 | kinship + marriage role edges（role_constraint） | 层级化 role 边与情感 bond 并存 |
| M32 | 同性配偶自洽 | DF/Sims | 跨形态稳定性（ruling #2） | 设计内含同性形态 ⇒ 语义不依赖于性别组合 |
| M33 | Social Link 等级楼梯 | Persona | 亲密度单轴（games 常见 conflate，负面样例） | 等级并吞 friendship+romance ⇒ 教训而非模板 |
| M34 | 末尾 romance flag | Persona/FE3H | 显式关系声明旗标（role_constraint/derived） | flag 转角色，不增加 primitive |
| M35 | 情人节多线惩罚 | Persona | 多条 commitment flag 冲突事件 | 承诺冲突是可观测事件（约束，非新变量） |
| M36 | 日历时间块 | Persona | investment / opportunity cost（proxy） | 投入是 proxy，不是关系状态本身 |
| M37 | 支援对话 C/B/A/S | FE3H | milestone 事件 + 阶段（derived staging） | 叙事门按阈值触发 = 阶段表示的成熟例子 |
| M38 | 同性 S 支援仅部分角色 | FE3H | identity/role 约束变体 | 角色约束可变，primitive 语义不受影响 |
| M39 | 隐藏好感 + 可见参数 | Tokimeki | latent state vs observable proxy（belief 层） | 部分观测预演：外在 proxy 推断内在状态 |
| M40 | 嫉妒炸弹 | Tokimeki | 多边竞争反作用（derived from per-pair 状态） | 三角嫉妒须由边集合推出，勿设全局变量 |
| M41 | 约会被拒长期负效果 | Tokimeki | rejection 事件 + path dependence | 拒绝是长期负性更新 |
| M42 | 称号/名誉（可见） | Tokimeki | 全局 reputation proxy（E） | 与 dyad 状态分离 |
| M43 | 可见属性门控场景 | MonsterProm | accessibility/eligibility proxy（S→D 供给) | 属性决定可选动作集，改变"可达性" |
| M44 | 隐藏 LOVE POINTS | MonsterProm | latent bond/desire（部分观测） | 与 M39 同类证据 |
| M45 | 多对象并行择偶 | MonsterProm/SDV | commitment 竞争结构 | 替代项显著 ⇒ dependence 低（Rusbult 替代） |
| M46 | Amulet of Mara 求婚门槛 | Skyrim | 显式同意/声明门（role_constraint） | 自愿声明是承诺的门槛 |
| M47 | 婚后零状态/零衰减 | Skyrim | 极简反面样例 | 无玩法动机则不建模 ⇒ 建模量与目标强耦合 |
| M48 | 派系声望 | Skyrim | group-context 立场（E） | 群体声誉 ≠ pairing 状态 |
| M49 | 剧情 auto-lock 浪漫 | MassEffect | path dependence + lock-in（derived） | 决策序列产生锁定，non-reversible |
| M50 | paragon/renegade 全局声望 | MassEffect | 第三人称声誉轴（E） | 独立于 dyad 的声誉量 |

> 共 50 条（≥30 达标）。注意 M33：Persona 的"共轴 + flag"是**被批判的收敛模式**，只作为 conflation 教训。

---

## 5. 候选 primitive 的裁决（对齐 `#4` 六维）

> 游戏侧证据以"机制簇是否跨系统独立趋同 + 是否能被 MSC 接住"为判据。以下裁决意见与 `#4` §0.2 一致或强化之；数字为构成证据的映射条目。

| 候选维度 | 游戏侧裁决 | 游戏侧理由 | MSC 检查 |
|---|---|---|---|
| **Attraction（吸引）** | **SPLIT** 为 `liking/positive regard` 与 `romantic–sexual desire`（另计 `A05 orientation`） | RF4 FP/LP（M09）、Sims 双量尺（M10）、DA2 rivalmance 所示 liking≠romance 均独立出现，相互可解耦（M17） | 独立性：liking 高而 desire 低（DF kindred spirit）与 desire 高而 liking 低（Sims 一见钟情但无友情值）均可构造 ⇒ 可去耦 ✓ |
| **Bond（纽带）** | **SPLIT/REDEFINE** 为 `attachment 安全(base/working-model)` + `cohesion/we-ness` | DF bond 阶梯（M29）表达强度；Sims/DF 边类型（M21）表达类别；grief moodlet（M23）表达断开代价；SDV 婚后无衰减（M05）表达 institutionalized 依托。we-ness 更贴近 FE3H paired ending、夫妻房等"共有物/共有史" | 语义过宽：一个 primitive 同时吞强度、类别、依托 ⇒ 不可归约不成立 |
| **Trust（信任）** | **KEEP**（def: 风险下依赖对方善意可靠性的有向信念） | 游戏侧直接建模少，但背叛/信任破坏事件普遍（M22、CK3 泄露秘密、DA2 背叛剧情）；RimWorld 被拒/背叛 moodlet 表示"预测失效" | 语义独立（与喜好可解耦：DA2 的 rivalry 可预期但不受欢迎，即"可依赖"≠"喜欢"）＋可估计（行为/泄露上下文）⇒ 站得住；游戏侧支持弱，主要靠 `#4` |
| **Commitment（承诺）** | **KEEP/REDEFINE** 为 `dedication`；拆出 constraint/investment/dependence | DA2 rivalmance 直接给出"低 liking 高 commitment"反例（M17）；Persona 多线 flag 冲突（M35）、FE3H S 支援声明（M37）、Skyrim amulet（M46）都是"显式承诺声明"事件；CK3 婚姻契约（M28）= constraint 分离 | 可去耦：commitment 高/喜欢低（rivalmance）✓；commitment 低/喜欢高（玩家海王）✓ |
| **Alignment（三观/一致）** | **REJECT 作为 primitive；降为 DERIVED pair 属性** | 游戏把"契合"实现为 喜好评测（SDV 爱礼物 M02）、共时/期望重叠（Sims cycle）、配对兼容（FE3H 支援值）——无一处是有向、时变的状态本体 | 不可归约性成立的反面：它是可计算的偏好/目标距离 ⇒ 非状态 |
| **Dependence（依赖）** | **KEEP**（结构变量；导出 power） | 游戏侧无显式依赖值，但结构表现在 "CK3 Hook/秘密可作杠杆"（M25）、"替代对象丰富 ⇒ 择偶竞争"（M45 SDV 海王、MonsterProm 并行）、Sims 的"需求满足依靠某 Sim"（日常因依赖维稳） | 语义独立 ✓；可估计需资源流/替代集（`#6` 有资源层可接） |

**游戏侧额外值得提请 Architect 注意的两个 non-six 候选：**

- **`familiarity/acquaintance`（熟悉度，S01 M03、DF 遗忘 M30）**：累积不互动的正函数、可被遗忘衰减。它接近"暴露依赖的 schema 适配"，但更安全的是把它作为 **primitive 的动力输入（历史事件流强度）** 而非独立状态（`#4` B07 proximity 邻近）。
- **`acceptance/rejection 不对称更新`（M20）**：这不是一个新 primitive，而是所有 desire/attachment 共同遵循的**更新规则不对称**（接受大正、被拒小负）。建议写入动力学规则而非增加状态。

---

## 6. 重复计数风险

游戏把多个轴合并为单一数值是常态（这是设计取舍），LHRM 若照抄会双记：

| 合并模式 | 出现在 | 双记风险 | 建议 |
|---|---|---|---|
| 单一好感总分 | SDV、Sims 双量尺之和、RF4 FP+LP、Persona 等级 | 把 liking、desire、阶段、事件记忆揉成一个数 | 单数只作 derived 展示，不进 primitive 输入 |
| Opinion 即"关系值" | RimWorld、CK3 | opinion 本身 = 事件记忆聚合，再加"喜好"即双记 | opinion 按 derived proxy 处理，不再另设"整体关系值" |
| 好感 + 阶段门共用同一分 | SDV（8 心才可约）、FE3H（阈值解锁） | 分数既当状态又当阶段门，会把"身份转变"加成 | 阶段由 milestone 事件表达，不由分数累计承担 |
| 礼物喜好 = 契合 + 好感 | SDV（爱 +80） | 同一礼物同时贡献"契合度"又贡献"好感" ⇒ 若模型也两个都算则双记 | 礼物行为只作为 value-congruence 与 responsiveness 的**观测**，不由数值再入两个 primitive |
| 可见属性 = 资格 + 吸引 | MonsterProm、Tokimeki | 资格 proxy 与 desire 混谈 | 资格属性进 S 层供给（可达性），désir 独立 |
| 隐藏好感 + 可见属性同时估计 | Tokimeki、MonsterProm | 若把 proxy 当作另一状态 ⇒ 双记 | 明确"层"：proxy 用于推断 latent，不是第二个状态 |
| 荣誉/派系/声望 | Sims、MassEffect、Tokimeki | 第三方声誉与 dyad 状态相加 | 声誉进 E 层 constraint，不加进 per-pair primitive |

> 结构性结论：**游戏最常见的合并点是"好感总分"与"阶段门共用分数"**。这两处在 LHRM 应分别落到 derived display 与 milestone events。

---

## 7. 游戏 UI 表达 → LHRM 展示层的可迁移点

> 目的：LHRM 的"面向人展示"（presentation）可从成熟游戏 UI 借用信息架构，但**迁移的是展示，不是模型**（AGENTS：computation / presentation / prediction 分离）。

- **双小量尺（好友/浪漫）不加总分**（Sims）：正向支持"不合并成 LoveScore"的展示原则。
- **短期 vs 终身双刻度**（Sims3/4）：表达"最近的热度"与"沉淀的稳固"两个时态，避免一轴糊两态。
- **隐藏/可见分层**（Tokimeki、MonsterProm）：游戏"不显示真实好感、只显示可推断 proxy"与 LHRM 的 belief/部分观测理念一致——**UI 可以选择性地展示**，不必全摊牌。
- **事件性 Toast/Sentiment**（Sims4）：瞬时状态用短命小标而非永续长条，防止"情绪"被误当长期状态。
- **分类徽章（lover/ex/rival）+ 数值条并存**（Sims 标签、DF 阶梯）：分类边与数值条的并置正是模型的两类变量。
- **里程碑/心事件叙事门**（SDV、FE3H）：阶段变化用"内容解锁"而非"数字跳变"来传达，对防"数值拜物"有效。
- **警告徽标（炸弹/竞对提醒）**（Tokimeki）：多边风险以"第三方警告"呈现，不污染主 dyad 视图。
- **警示：游戏 UI 服务于玩法可读性，常故意"压缩维度"**（单好感条、明暗两级）。LHRM 可借鉴信息架构，但不得借"展示简化"反推"模型也该单轴"。

---

## 8. 动力学特征汇总（跨系统）

> 均标注出自哪些 §3 系统；这是对"关系状态应有什么动力学形状"的机制级证据汇总。

- **方向性 & 不对称**：有向 per-pair 状态普遍（SDV/Sims/RimWorld/CK3/DF）；无向"我们值"仅见于升级式等级（Persona）与契约旗标（FE3H S 支援）。→ 模型默认有向边，pair 属性显式单列。
- **可接受性不对称**：RimWorld 求婚 +35 / 拒绝 −10/−15（M20）；拒绝被记为长期负事件（SDV、Tokimeki）→ 更新函数应按"接受/拒绝/忽略"分别设不对称或然率。
- **双时间尺度**：Sims 短期/终身、CK3 short/long-term 修饰、RimWorld 滑动窗口 vs 长期记忆（M11/M19/M24）→ 快慢两层状态（transient vs settled）是跨类型共识。
- **阶段/里程碑**：SDV 心事件-约会-求婚-婚姻、FE3H C/B/A/S、DF 阶梯、Persona rank（M06/M37/M29/M33）→ 阶段由显式声明/关键事件切换（role_constraint 跃迁），不是分数滑动渐变。
- **衰减与遗忘**：SDV 连续 2 日不互动即衰减、Sims 自然衰减、RimWorld 窗口滚出、DF acquaintance 遗忘（M04/M30）→ 弱表态需要维护；**但 grudge 例外**（负性不对称）。
- **路径依赖**：Persona 浪漫 flag 在特定等级才可选、Mass Effect auto-lock、SDV 离婚抹除记忆（M08/M34/M49）→ 历史事件序列改变后续可用动作集与可达状态（non-Markov unless history kept）。
- **事件触发**：Sentiment、Hook、出轨、炸弹、S 支援结尾（M12/M22/M25/M35/M37/M40）→ **事件是状态更新的主力**；事件类型是模型的输入接口。
- **多边/社区效应**：RimWorld 出轨与多人 moodlet、Tokimeki 炸弹、Persona 情人节、CK3 联姻（M21/M40/M35）→ 三角/群体效应一律由 per-pair 边集合推导，**不引入"嫉妒/花心"全局变量**。
- **部分观测（belief）**：Tokimeki / MonsterProm 隐藏好感（M39/M44）→ 玩家（以及模型人设中的各 Agent）对他人状态只能观测 proxy；模型应有 belief/latent 界面。

---

## 9. assumption_stress_test（跨形态稳定性，游戏域证据）

对 §5 存活/拆分的候选，用 `#2` 要求的形态坐标做检验。`stable` / `stable-as-role-variant` / `meaningless-here`。

| 候选 primitive | 同性/异性 | 亲缘/非亲缘 | 陌生人/既有 | 说明（游戏证据） |
|---|---|---|---|---|
| liking（有向正向意念） | stable | stable | stable | SDV/Sims/DF 均与性别组无关；亲缘也可 liking（DF 家人） |
| romantic–sexual desire | stable-as-role-variant | stable-as-role-variant（亲缘处受角色禁令门控） | stable | DF 同性婚配、Sims 同性恋爱为普通 case；CK3 近亲婚姻有 penalty（role gate）；Tokimeki 为异性默认 → 记为该形态的退化为 chiefly 单性别激发（meaningless-in-other-sex 在它那个设计里即角色约束） |
| attachment/bond（分层） | stable | stable | stable | DF spouse/kindred spirit/lover 同性自洽；亲缘 bond 与婚姻 bond 层不同（staged） |
| trust/distrust | stable | stable | stable | DA2 背叛/神秘、CK3 秘密泄露不随组合变化 |
| commitment/dedication | stable-as-role-variant | stable-as-role-variant（婚姻义务为契约变体） | 陌生人开始时 commitment 通常低（无声明/无历史） | FE3H S 同性支援 subset 是角色约束变体而非语义漂移 |
| dependence/power | stable | stable | stable | 杠杆（Hook、资源依赖）不随性/亲缘组合改变 |
| value–goal congruence（pair） | stable | stable | stable | 礼物口味（SDV）、支援值（FE3H）与组合无关 |

**游戏侧 decoupling 构造（反例解耦）**：

- liking 高 ∧ desire 低：DF kindred spirit、Sims 挚友间零浪漫 → 支持 SPLIT。
- desire 高 ∧ liking 低：RimWorld 求婚在 opinion 尚低时可发生（浪漫接受 +35 推高 opinion）→ 决策先于好感积累。
- commitment 高 ∧ liking 低：DA2 rivalmance（M17）→ dedication 独立。
- commitment 低 ∧ liking 高：SDV 玩家同时约会多人（海王）表现 High liking 而低 dedication。
- trust 高 ∧ liking 低：DA2 rivalry 对象被反复证明"可预期"（客观可靠）但不受欢迎 → trust 不随 liking。
- bond 深 ∧ desire 无：DF spouse 与 kindred spirit 共享 tier 而未暗示性 → bond 与 desire 分离。

---

## 10. 学术校准（仅作术语锚定；直接实证在 `#4/#6`）

- **接受/拒绝奖罚不对称 → Leary 社会计 / 归属需要**（Baumeister & Leary, 1995；Leary「被拒即脆弱」）。解释 RimWorld +35/−15 的模型可为什么是 asymmetric，而非对称更新。（E2，经典）
- **mere-exposure → familiarity 正积累**（Zajonc, 1968）解释 SDV"每日对话+分"。（E2，经典复习）注：游戏+20 是设计数字，非暴露效应量。
- **Rusbult 投资模型**：commitment = satisfaction + investment − alternatives。完美解释 SDV 海王/替代集与 CK3 联姻替代（M45）——投入、替代为结构输入，commitment 是状态输出。（E2）
- **Sternberg 爱情三角（intimacy+passion+commitment）**：与 §5 SPLIT 一致——游戏把这三者各自拆成量尺（Sims friendship/romance、Persona flag、婚姻契约）。（E2 经典，C 于范围）
- **Bowlby 依恋 & 断联代价**：game-side grief moodlet（M23）映射分离痛苦；支持 bond 作为独立 primitive。（E2）
- **互依理论（Kelley & Thibaut；Rusbult）**：outcome dependence / CL（比较水准）→ 支撑 Dependence 与 power asymmetry（CK3 Hook）。（E2）
- **负性不对称（negativity bias，Baumeister et al. 2001）**：负事件影响更强更久 than positive——DF grudge 持久 vs acquaintance 遗忘（M30）的经验学底座。（E2）
- **感知回应性（perceived responsiveness，Reis & Shaver）**：亲密感来自"被接纳/被理解"——SDV 礼物品味（M02）正是"懂我"的 proxy。（E2）
- **社会渗透/自我表露（Jourard 等）**：Persona 靠对话选项升级（自我表露→亲近）机制与此一致。（E2/E3）

> 声明：以上为术语锚定引用，终身/具体效应量均来自既有社会科学文献，游戏数字（±80、+35 等）不得当效应量引用。

---

## 11. 剩余不确定性、缺口与对 `#2` 融合的建议

### 11.1 剩余不确定性

- 游戏域对 **Trust 的直接显式建模极少**（多为背叛事件而非信任状态），游戏侧对 Trust 的支持主要是反向（背叛事件普遍）+ `#4` 正向，权重建议以 `#4` 为主。
- 游戏对 investment / dependence 一般不显式建模，多半表现为"资源/时间投入"与"不可逆锁定"（Mass Effect），dependence 的结构定义主要靠 `#6` 资源层接住。
- 游戏对 **负面情感（羞耻、内疚、宽恕）几乎不建模**（RimWorld moodlet 只是简化），负面半轴仍是经验空白。→ 建议 `#2` 将负面更新规则优先列为开放问题。
- 样本覆盖偏差：所调查 13 系统中恋爱模拟浓度高，**平台/合作类多人关系系统（如公会、同事、长程远程）较少**；familiarity 在远程场景的"无物理接近"变体未充分覆盖。
- Evidence 分级限制：部分来源为售后社区 wiki（G3），个别为未抓取的一般知识（G4），个别 Fandom 页面会话内 transport 出错，以搜索快照为准。

### 11.2 对 `#2` 融合的三点建议

1. **primitive 集收敛意见**（与 `#4` §0.2 一致强化）：有向 per-pair 状态建议 = `liking`、`romantic–sexual desire`、`attachment/bond(tiered)`、`trust(distrust 分面)`、`commitment(=dedication)`；pair 属性 = `value–goal congruence`；结构 = `dependence/power`；角色/身份/制度 = role_constraint 层；瞬时情绪 = 事件驱动 derived。不新增"整体好感度""嫉妒""花心"等全局变量。
2. **更新规则优于加状态**：把"接受/拒绝不对称""双时间尺度""阶段由事件切换""负性不对称衰减/遗忘"写成动力学规则（§8），避免用加参数的方式复制游戏的好坏走高。
3. **展示与模型脱钩**：单轴"亲密值"/"LoveScore"只允许作为 derived 的面向人评级，禁止进入 primitive 输入（§6/§7）。UI 可借鉴双量尺、双时态、里程碑事件、隐藏/部分观测的交互设计。

---

## 附：指令对照（DISPATCH acceptance mapping）

| 要求（#3 dispatch） | 交付位置 |
|---|---|
| ≥12 个游戏/模拟系统 | §3：13 系统（S01–S13） |
| ≥30 条 proxy→构念映射 | §4：50 条（M01–M50） |
| KEEP/SPLIT/MERGE/DERIVED/REJECT 裁决 | §5（六维 + 2 个 non-six 候选） |
| 重复计数风险 | §6（7 类合并模式） |
| 游戏 UI 表达可迁移点 | §7（8 条） |
| 五分类 mechanism/primitive_state/observable_proxy/derived_outcome/role_constraint | §1.3、§4 每行、§5 |
| assumption_stress_test | §9（6 候选 × 形态矩阵 + decoupling 6 例） |
| 方向性/不对称/双时间尺度/阶段/衰减/路径依赖/事件触发/多边 | §8 |
| 学术来源校准 | §10（8 组） |
| 主要来源 URL + 证据分级 + 剩余不确定性 | §3 各系统、§2.1、§11.1 |
| 覆盖同性/异性/亲缘/非亲缘/陌生人/已有关系 | §0、§9 |
| 对齐 S/O/D/E 与 `#2` 裁决 | §1.3、§2.2、§5、§9 |