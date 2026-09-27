# REJECTED_OR_WEAK_FINDINGS — Round 2 review swarm over `youling/lhrm#31`

> 本文件收录**必须撤回、必须重述、或强度不足不可按现状引用**的 PR #31 主张。
>
> **重要限定**：`REJECTED_OR_WEAK` 中的「被拒绝」指的是**该表述不可按现状引用**，
> **不等于**「其为假」。`REVIEW_CONTRACT.md` §4：`UNSUPPORTED` = 断言存在但未找到足够证据，**不等于为假**。
> 本文件绝大多数条目是**表述、量词、层级、严重性、推论**的问题，不是「事实为假」。

---

## R-0 · 本轮识别的**首要失败模式**：检索覆盖不足被写成领域存在性结论

`WRONG-SCOPE` 的定义（`REVIEW_CONTRACT.md` §4）：命题本身可能成立，但**层级 / 总体 / 分析单位 / 时间尺度 / 情境域**
与被当作依据的那一层不匹配；或**方法学与数据访问限制被误读成 ontology 结论**。

本轮共 **5 处**同型错误，**全部必须重述**：

| # | 原文表述 | 正确表述 | 来源 |
|---|---|---|---|
| R-0.1 | `12` §0 headline：「**不存在**可与 LHRM 对象直接比较的既有关系 ABM」 | 「在本 lane 已检索场所内**未找到**任何一个」 | `G-C17` `WRONG-SCOPE` |
| R-0.2 | `04` §8.9：「四条件交集为空是**本 landscape 最重要的结构性事实**」 | 「这是**本次检索**的结构性结果」（且 Add Health 从未进入结构检验） | `C-C29` `CONTESTED` |
| R-0.3 | `04` §8.8：「intensive longitudinal 关系日记数据在本 landscape 中**不存在**」 | 「在本 16 个数据集的审计范围内未发现」 | `C-C30` `WRONG-SCOPE` |
| R-0.4 | `02` §5.8：「**再次确认**……这不是本轮检索不足，是文献里确实不存在」（中文 ESEM / bifactor） | 「本 lane 的检索未发现」；存在性否定需独立系统检索 | `A-C29` `WRONG-SCOPE` |
| R-0.5 | `03` §1.2 把 `NOT_IDENTIFIABLE` 定义为「结构上做不到」，却用它承载 9 条「层级不对 / 尚未检索」的条目，并据此建议降级两个 canonical candidate（D7 `Dedication`、D8 `OutcomeDependence`） | 这 9 条是**层级不匹配或检索不足**，不是结构上不可测 ⇒ **两条降级建议整体打回** | `B-C4` `CONTESTED`；`B` 的 top_rec 第 1 条：`RECLASSIFY_AS_METHOD_LIMIT` |

**同类但不同型的**（rights / 访问限制被误读为项目缺陷）：

| # | 原文 | 正确处置 | 来源 |
|---|---|---|---|
| R-0.6 | `17` §9.2-FACT-1 + `09` §5.4-3：「没有任何一层现在**有资格**充当 `F` 的引擎」 | 改为「目前**没有证据**支持任何一层充当引擎」。**方法/测量事实，不是资格判断** | `F-C12` `WRONG-SCOPE` |
| R-0.7 | `03` §3.3：工具在「关系不存在」状态造替代对象 = 「违反 `CURRENT_ARCHITECTURE.md` §9」 | 改到正确依据：§3 `Reality != Observation != Belief` + §9 原则 1 + §10 `unknown` 事实状态；ECR 的 trait 语言改判为「**诚实标注 Agent 层 scope**」，不是「静默伪造 target」 | `B` top_rec 第 6 条 `CONTESTED` |
| R-0.8 | `04` §8.6：「**ICPSR 全站 403**」 | 「本报告中**所有 ICPSR 系证据**强度为 MEDIUM」 | `C-C31` `CONTESTED` |
| R-0.9 | `04` §8.6：`hrs.isr.umich.edu` 正文页反复 timeout/403 ⇒ U4 记「条文 `UNKNOWN_AS_OF`」 | 失败记录真实，但**后果被高估**：CoU 页**可达且含完整 AI 禁令** ⇒ U4 应改为**已解** | `C-C33` `CONTESTED` + `C-C11` |
| R-0.10 | `19` 把 8 个 Work Order 呈现为 8 个待批事项 | 重分类为 **3 决策 + 3 派工 + 1 基础设施请求 + 1 书目核对** | `K-C44` `WRONG-SCOPE` |

---

## R-A · Gate / 门相关

### R-A1 — 「`MERGE` 与 `REJECT` 从未被签发过一次 ⇒ 8 项 candidate basis 单调增长」

- **判定**：**项目层为 `WRONG-SCOPE`（表述被换主语）**。`EV1` `PARTLY_REFUTED`；`ADJ3` Q1 三层裁定；`L-C3` `WRONG-SCOPE`；`J-C8` 侧同向。
- **被推翻的证据**（可 grep 复现）：
  - **L2 · canonical**：`PARAMETER_CONVERGENCE_V0_1.md` `§9 R4`「当前：`REJECT as primitive`」、`§9 R5`「当前：`REJECT as single primitive`」⇒ `REJECT` = **2 次**。
  - **L3 · 本次 attempt 全域**：`10:441/621/622`（`REJECT Cohesion_(A,B) as a scalar primitive`、`REJECT "we-ness" as a construct name`）；
    `08b:227/240/267/279/296/318/337`（该文件自报「含 3 项 `REJECT`」）；`02b:172/520`；`01:178`（三 fixture 门实际签发了 `REJECT` 档）；`14:282`。⇒ `≥8 次`。
  - **L1 · `R01` 报告内**：`MERGE` 与 `REJECT` 各 0 次作为**裁决值**（各 1 次 token 出现在词表声明行）。**这一层为真。**
- **`ADJ3` 的最高价值诊断**：这个断言**不是被夸大，而是被换了主语**。
  它在 `A03` 里是**一份报告的自评**（`R01` 的 7 值词表只用了 4 值），在 `19`/`00_MANIFEST` 里被**升格为项目级门控事实**并挂到 canonical §2.6 的论证链上。
  升格同时做了三件事：**丢限定语、换主语、换量词**（「一次也没有出现」→「从未被签发过一次」，后者是关于**签发行为**而非**词表使用**）。
- **可辩护的替代表述**（`L-C3` 的收紧版，`ADJ3` 采纳）：
  > **8 项 basis 在已执行的 gate 下从未被删减过一条；项目历史上确实签发过 `REJECT`，但那些全部由 drafting 时的散文判断作出，没有一条是由 §2 判据或 §15 门跑出来的。**
- **为什么这个措辞差异决定修法**（`ADJ3` rec 2）：它决定 WO-N1 是「改文化」还是「改一份门规范」，**后者便宜得多**。
- **`ADJ3` 的自我限制**：不主张 §9 R4/R5 的两个 `REJECT` 是「作者判断」而非「门产出」有**文本铁证**——
  canonical §9 通篇是「当前：」的宣告语气、无引用、无执行记录，**据此**判为作者判断；**不能排除**作者在别处跑过未记录的评估。
  durable artifact 应写「**无执行记录**」，**不应**写「确定为作者判断」。
- **`ADJ3` 亦不主张项目应引入 `MERGE`**：`MERGE` 的 0 次在三个层级上都成立。

### R-A2 — 「`§2.6` 是唯一能删除 construct 的准入侧判据」

- **判定**：`WRONG-SCOPE`（全称量词为假）。`EV1` `PARTLY_REFUTED`；`I-C2` `CONTESTED`（核心成立、两处子命题被推翻）；`ADJ3` Q2 `VERIFIED`（缺陷存在、范围比三家所述都大）。
- **`ADJ3` 的逐条后果分档**（读的是原文，不是任何 lane 的转述）：

  | 判据 | 原文行 | 后果句 | 档位 | 可失败？ |
  |---|---|---|---|---|
  | §2.1 Semantic independence | `:47` | **无后果句**（纯问句） | 无后果 | **否** |
  | §2.2 Counterexample decoupling | `:53` | 「若无法构造或观察解耦反例，**可能属于同一 latent state 的重复命名**」 | **降级/合并** | **是**（唯一带真失败条件者） |
  | §2.3 Conditional incremental info | `:57` | 无后果句；且「**仍可能**提供额外信息」是可能性陈述 | 无后果 | **否**（可能性陈述不可被否定） |
  | §2.4 Scope stability | `:61` | 无后果句（清单封闭，但无合格/不合格定义） | 无后果 | **否** |
  | §2.5 Layer test | `:80` | 「如果只是行为、标签、结果或 proxy，**不因常见就升级为 primitive**」 | **不晋升 / 降级** | **是**（但桶无优先级规则） |
  | §2.6 Representation necessity | `:84` | 「**若删除该 construct**，是否会存在重要现实句子/状态无法用剩余 schema 合法表示」 | **删除（显式反事实）** | 形式上是；**结构上恒假** |

- **正确的反驳不是「五条都蕴含删除」**（那是 lane I 的说法），而是：
  > **六条里只有一条用了删除框架（§2.6），两条用了降级框架（§2.2 / §2.5），三条连后果句都没有（§2.1 / §2.3 / §2.4）。**
- **`ADJ3` 的加强结论**：**六条全部无 procedure / required evidence / output field / threshold / designated executor。**
  `:43`「至少接受以下审计」是唯一的**程序性**句子，而它没指定审计者、没指定产出、没指定失败后果。
  ⇒ **全族不可执行，`A03` 的范围判定过窄。**（`A03` 只改写 §2.6 是不完整的。）
- **`EV1` 的加强结论**：Gate A 唯一的分析产物类型（`:641-649` 的 6 个 hole + `merely narrative/irrelevant`）是**纯加法封闭**的，
  **没有 redundancy/duplicate 这一类** ⇒ **一次「某 construct 冗余」的 gate 结果在当前类型系统里根本无法被表达（untypable）。**
  「这才是 delete 臂惰性的机械原因，比「没有阈值」精确一个层级。」
- **反向检验**（`EV1` §6 第 7 点）：gate 在两个方向上都是惰性的——缺失的后果句**对称地同时封死了真否决与假否决**。
  **唯一的例外已经发生且不可逆**：`PARAMETER:598`（嫉妒）`602`（控制欲）`590`（爱）`594`（亲密）`606`（忠诚）`610`（化学反应）
  以 `更可能` / `可能` 的推测措辞被排除出候选，且**没有任何 re-entry criterion**。
  **这 6 项是已经生效的、无阈值的、无回归路径的排除**——`EV1` 建议为它们补 re-entry criterion，认为这比补 §2.6 更能防止假否决。
- **`ADJ3` 明确不主张** §2.1–§2.6 的六条判据应当被**删除**：它们**缺可失败形式**；补程序与阈值是修法，删除是另一种未被论证的修法。
  且 §2.2/§2.5 的后果句**是**有效的判据文本，不该被当成噪声删掉。

### R-A3 — headline 的**严重性**（「昂贵 canonical patch + 重跑 Fixture」）

- **判定**：`EV1` `REJECT`（对严重性）
- **理由**：`A03` 与 `19:282` 已推导出「删掉 §13 的 3 个 catch-all 映射类与自由文本出口；把 §2.6 改写成可触发的准入侧判据（含至少一条 `MERGE` 与一条 `REJECT` 的判定规则）；重跑 Fixture 001」。
  **`EV1` §7：这个 patch 规模（删 3 个 catch-all + 重跑 fixture）与缺陷实际所需的规模不匹配。**
- **实际规模**（`EV1` §8）：约 **5–8 句新增文字 + 1 个 ablation 步骤定义 + 1 个诊断枚举值**，
  全部落在 `PARAMETER_CONVERGENCE_V0_1.md` 共 5 处，**外加 1 处 `AGENTS.md` 镜像同步**。
- **同时区分的三笔钱**（`EV1` §9）：
  1. **确立缺陷**：零成本（grep + 引用即可），已完成。
  2. **修复缺陷**：文档编辑，5–8 句。改动 2（ablation 步骤）是**协议定义**，不是实验设计。
  3. **（修复之外的另一件事）Gate A/B/C 至今从未被完整执行过一次**——这是**首个** Case Bank regression run 的成本，
     **与本缺陷的修复成本无关**。`EV1` 未执行它（契约禁止），**也不主张它是修复的前提**。
  **并明确反驳**：「如果有人主张『必须先做一次 Gate A 才能确认缺陷』，那是错的。」
- **parent 记录的一处张力**：`ADJ3` rec 5 要求把 WO-N1 的变更面扩到 **4 文件 / ≥6 节**。
  `EV1` 说 5–8 句。**parent 采信 `EV1` 的成本判断，同时采纳 `ADJ3` 的范围判断**——
  二者不矛盾：`ADJ3` 扩的是**必须一起改的面**（否则 delete 臂仍不可达），`EV1` 估的是**新增文字量**。

---

## R-B · 引用与证据分级

| id | 必须撤回 / 重述的表述 | 判定 | 依据 |
|---|---|---|---|
| **R-B1** | `A01` §1.1「Crossref 解析 **353/353（100%）**」 | `UNSUPPORTED`（`J-C13`） | 同文件 `:15` 写 `337/353 = 95.5%` |
| **R-B2** | `A04` 承重表「30 项中 **28 项强度充分**」 | `UNSUPPORTED`（`J-C7`） | ≥16/30 作者归属错（`EV2` 独立复核）。**「已通过」清单里有错项 = 假的免检标记** |
| **R-B3** | `350` **peer-reviewed** 作为「科学重量」 | `WRONG-SCOPE`（`J-C6`） | 分层抽样 **9/16 = 56%** 不是 primary empirical work（`EV2`）。**可**作为「350 个同行评审来源」使用 |
| **R-B4** | 各 lane 自报数之和 ≈ **1,201**；「高估 **2.3–3.4×**」 | `WRONG-SCOPE`（`J-C4`；`EV2` 独立复算） | 实际 **878**；`1.65×`（vs 533）/ `2.51×`（vs 350）。`1,199` 是原始出现次数，不同量纲 |
| **R-B5** | `A04`「3 处 `10.31234/osf.io/…` 前缀结构非法、不解析」 | `UNSUPPORTED`（`J-C8`） | **两个前缀均 live**（同属 COS）；`f6wbn` 只在 `10.31234` + `_v1` 下注册。`A04:193` 自己记 ✅ ⇒ **PR 内部文档直接反驳 manifest** |
| **R-B6** | `A04` D5：`10.1024/1662-9647.a000031` 的问题是「前缀与著录期刊族不一致」 | `UNSUPPORTED`（`J-C14`） | 该理由不成立 |
| **R-B7** | `A04` §3.3.4：`10.1037/h0046049` = Cartwright & Harary 1956, *Psych Review* **63(4)** 判 ✅ | `UNSUPPORTED`（`J-C15`） | 实为 **63(5):277–293** |
| **R-B8** | `00_MANIFEST` §2b：「`08b` 修了 **7 处**」 | `UNSUPPORTED`（`J-C20`；`EV2` 核实） | **8 处**（`git show 8adcf0b -- 08b`） |
| **R-B9** | `00_MANIFEST` §2b：「`08b [S15]` 只改作者，未改年份」 | `UNSUPPORTED`（`J-C21`；`EV2` 更错） | `08b:755` 的 `[S15]` **根本没有作者字段**；年份是 **2025**，A01 给的就是 2025。**A01 是对的，manifest 的转述在年份与性质上都错** |
| **R-B10** | `18` 的「`R02` 与 `R10` 引**同一篇** Overall & Hammond 2026，得出**同一个经验结论**」 | `WRONG-SCOPE`（`K-C9`） | `R02` 读出的结论与 `R10 G6` 的结论**不是同一件事**；且两个具体数字（`70–75%`、`actor/partner 正相关`）**不在 Crossref abstract 中** |
| **R-B11** | `18` N-08「唯一有**直接判别实验**支持的 pair-level 涌现候选」 | `WRONG-SCOPE`（`K-C10`） | Bodenmann 2011 的判别发生在**操作化层**，不在**本体层** |
| **R-B12** | `18` CF-03 / `19` C-1 的「三方互斥 / 三种互斥处置」 | `MOOT`（`ADJ1` Q1） | 见 `CONTESTED_FINDINGS.md` X-1。`18:114` 对 R01「未调和」的批注**经核对是错的** |
| **R-B13** | `03` §2.8 `O1` RPI = Beach 2017；`O2` RBA = Lativos；`A13` = Laurenceau 1998；§7 条 42 = Mønster 2016；§2.1 `L2` RCI = **10 题** | `CONTESTED`（`B-C6`）/`CONTESTED`（`B-C7`） | 应为 **Farrell, Simpson & Rothman 2015** / **Luttrell et al.** / **Pietromonaco & Barrett 1997** / **Palumbo et al. 2017, PSPR 21(2)** / **75 题** |
| **R-B14** | `07` 两条形式化来源的作者/年份 | `UNSUPPORTED`（`E` 指出） | Belnap K4 两条来源存在作者/年份引用错误 |
| **R-B15** | `07` ref [6] 的书目条目（作者列表错误） | `REJECT`（`E-C10`） | 内容层 `ACCEPT`，**书目须修正后才能引用** |
| **R-B16** | `06` §8.7 中 Lavner 的 limited evidence 被标为 `DIRECTION_NOT_SUPPORTED`（明确反证） | `ADJ2` Q1 指出**标过头了** | 来源说的是 limited evidence + 妻子侧 null，**不是 explicit refutation**；丈夫侧逐字「**Consistent with the incremental change model**」 |
| **R-B17** | `13` §9.6 的证据链：「跨域 AUROC **0.76–0.99 但跨域 0.50（随机）**，判别方向跨域近正交（平均余弦 **−0.07**）」→「**自发产生的虚假内容与真实内容在可检测性上不可区分**」 | **`UNSUPPORTED`（数字）+ `WRONG-SCOPE`（推论）**（`G-C20`）—— **`G` 判为本 packet 最高严重度项** | `G` 读了 `arXiv:2602.13224v3` 全文：近机会的数是 **AUROC 0.536** 且属于 **NLI 基线**、不是论文自己方法的结果、更不是「跨域」；「0.76」是 **paired cos = .766** 不是 AUROC；「0.99」在论文中不存在；论文自己的显著性陈述是「All Human and LLM rates **significantly above 50%** (p < 10⁻⁸)」，abstract 说的是 confabulation 的几何签名 **outperforms NLI**。**方向与被引论文相反。** 且该论文**完全没有跨模型一致性测量**（只用一个 LLM 生成 confabulation）⇒ 从「单输出难检测」到「多模型一致是失败模式」是**构念替换** |
| **R-B18** | `13` 对 `Nakamura et al.` 的用法 | `G-C24` 要求更正 | 其 abstract 结论是「little empirical basis for preferring **human** coding」，与 `13` 的用法**方向相反** |
| **R-B19** | `14` §9.1 / §9.2 的两项「最高优先未核实 prior art」 | `REJECT`（`H`）—— **应从 prior-art 表中删除**，而不是投入资源去「补验这两个 DOI」 | 见 `HIGH_CONFIDENCE_FINDINGS.md` H-F22 |
| **R-B20** | `14` O-3(a)「括号不匹配」 | `REJECT`（`H` 指出为假：2 开 2 闭） | 「**这是最需要撤回的一条——它是一条可以在任何学术会议现场被当场证伪的指控**」（`H`）。另 O-3(c) 行号 204→200、O-5「Gate C 明确 PENDING」在 `docs/foundation/` 中不存在、O-10 行号 1440→1438 且「STAGE_SUMMARY 写 72–89」不成立、O-12 行号 22→23。以 **`O-17`**（报告自己标「措辞正确，不是文档错误」）为范本重写其余各行 |
| **R-B21** | `19` §8 B-9 / `00_MANIFEST` §4 B-9 | `UNSUPPORTED` → 见 R-4.1 | manifest **一份之内**自相矛盾（`B-3` 与 `B-9` 指同一件事） |
| **R-B22** | `19:353` 的方法学缺口第 3 条（「`02b` 依赖 `R04`/`R06`」） | `VERIFIED` 为**假**（`K-C12`） | `02b` **零**引用 `R04`/`R06`。**这是 `19` 唯一的硬事实错误，且它在「诚实记录自身缺口」的段落里**。替换物：真实的 `R06 → R02` 依赖链（`R06` 律 B 的 `Dedication` 层级取自「见 R02 裁决」，而 `R02` 的 `H2 CRITICAL` 从未被 `R06` 消费） |

---

## R-C · 权利与数据可得性

| id | 必须撤回的表述 | 判定 | 依据 |
|---|---|---|---|
| **R-C1** | `04` §6 末行 + §10：「ICPSR SOMAR VDE / MiCDA Enclave …… **这是目前唯一已知可行的『合规地用 LLM 处理受限数据』路径**」 | **`WRONG-SCOPE`（`C-C14`）—— `C` 判为「本 packet 中唯一的、会导致真实合规后果的错误」** | `C` 直开三份官方页面：SOMAR VDE **只服务社交媒体受限数据**；ICPSR 自己的 VDE/PDE **明文「no LLMs available」**；HRS CoU **逐字禁止 AI 程序与 LLM 与 HRS 数据同用，且点名 open-source AI**。⇒ 建议拆成三句独立、各带条件与出处的陈述 |
| **R-C2** | `04` §11 违反后果：「立即撤销使用权、要求删除全部副本；**严重违反**可在网上公开违规者身份」 | `PLAUSIBLE`（方向对，范围描述不准）（`C-C3`） | 补 `(cf. 6. above)` 限定 |
| **R-C3** | `04` D02 `lhrm_impact`：「§7 使 SHARE 派生量在法务上不能进入一个 LLM 参与的公开验证流水线」 | `WRONG-SCOPE`（`C-C2`） | §7 是限制**使用与再分发**，不是禁止派生量进入流水线 |
| **R-C4** | `04` §10 自评：「HRS AI/LLM 政策条文未取得，而这**可能是最严的一份**」 | `CONTESTED`（`C-C11`）—— **不可得前提已被推翻** | `hrsdata.isr.umich.edu/data-products/conditions-of-use` 可达且含完整 AI 禁令。⇒ U4 由 `UNKNOWN_AS_OF` 改为**已解**，HRS 分级从「含新政策（未知）」改为「**全面禁止**」 |
| **R-C5** | `04` D15 Oregon Youth Study Couples Study Time 6 = `ACCESS_BLOCKED`，`cannot_identify` 写「**不可识别**」 | `WRONG-SCOPE`（`C-C27`） | D15 同时标注两轴：结构轴 = `MEASUREMENT_ONLY`，egress 轴 = `ACCESS_BLOCKED`。把两轴压成一轴 |
| **R-C6** | `04` D12 / D13 `cannot_identify`：「对 LHRM 计划用途 —— **不可识别**」 | `WRONG-SCOPE`（`C-C26`） | 许可条件 ≠ 识别能力 |
| **R-C7** | `04` §1.2 + §10：「**发现了 2025–2026 年 LLM/AI use-condition 收紧** 这一横跨 SHARE / ICPSR / Add Health / UAS / HRS 的**系统性约束**」 | `CONTESTED`（`C-C36`） | 改述为「**单源扩散**」：ICPSR 政策 `Approved: December 11, 2024`；Add Health 与 SOEP 各自在页面上把 taxonomy **溯源到** HRS + ICPSR + Karcher。**这些不得计为彼此独立的证据** |
| **R-C8** | `04` §7 非主张 1「本 lane **零数据接触**」+ §4 各卡片以 `CITED_PRIMARY` 标记所有属性判断 | `PLAUSIBLE`（整体自洽，三处越界）（`C-C34`） | 要求 R04 二次修订时给全部 `CITED_PRIMARY (indexed…)` 加限定 |
| **R-C9** | `03` §8 L405 自称 54 个条目「**全部带真实指针**」 | `UNSUPPORTED`（`B-C15`） | 至少 5 条没有 |
| **R-C10** | `03` 的「41 family / 54 条目」计数 | `UNSUPPORTED`（`B-C1`） | 实测 **73 行**；且含 **6 处**重复或近同义 double-count（`X5`/`X6`/`X7`…）未标注。**不得让 "41/54" 进入任何 canonical 依据** |
| **R-C11** | 「217 DOI pointers / 48 `UNVERIFIED` flags」 | `UNSUPPORTED`（`B-C2`） | **文件内不存在该 claim**（这是审计任务书的描述，不是报告的主张） |
| **R-C12** | `19` 与 A03 把「**12 份语料**」当作 Gate B 的既有语料面 | `WRONG-SCOPE`（`L-C12`） | 12 份中仅 **2 份 `direct-use`**，10 份 `needs cleaning`；corpus 作者自己写明 L2/L3 `deliberately deferred until Verifier protocol is frozen` |
| **R-C13** | `19` §5：8 个数据集中 D04（Fisman & Iyengar speed dating）标「**完全公开，2026-09-27 HEAD 200**」 | `WRONG-SCOPE`（`C-C17`） | 全文把「完全公开」统一改为「**技术上零门槛可下载（第三方镜像）**」 |
| **R-C14** | `03` §4.1：`G9` 是「**架构级 gap**」，措辞为「没有任何已验证坐标同时拥有自陈信念通道与行为/生理独立通道」 | `WRONG-SCOPE`（`B-C11`） | 按字面为假（trust 有行为博弈范式未检索；报告自己的 PRI Study 3 是双 informant 单通道）。收窄为「没有任何**关系层有向坐标**拥有 pair-level、关系特异的 自陈信念 + 独立观察/生理 双通道」后方成立；并把「架构级 gap」降为「**开放技术问题**」 |
| **R-C15** | `03` §6「工具的 inability 处理『关系不存在』是 LHRM 违反 Unknown 保留原则」 | `CONTESTED`（`B-C20`） | `AGENTS.md` 那条**保留**，但表述改为「工具的 inability **不构成对该状态的合法表示**」 |
| **R-C16** | `04` D08 方向性关键注 | `CONTESTED`（`C-C35`） | 限定为「**Wave 1 单方报告（已核实）；Wave 2 及以后未核实**」 |
| **R-C17** | `04` D12 命名「Add Health (**NLSY97/ECLS**)」；§7 非主张 6「**不主张** Add Health 存在 friendship nomination 数据文件（U7）」 | `CONTESTED`（`C-C19`、`C-C20`） | 误名 + 报告内部矛盾。U7 应由「不得主张存在」改为「**官方用户指南已列**」 |
| **R-C18** | `04` D01：「官方 GESIS 变量清单中 partner 侧变量统一 `p` 前缀」 | `CONTESTED`（`C-C21`） | 改为「partner 侧**主用** `p` 前缀」 |

---

## R-D · 统计 / 识别 / 律

| id | 必须撤回或重述的表述 | 判定 | 依据 |
|---|---|---|---|
| **R-D1** | `05` §12 建议 1：把 I4 / I11 / I14 写成 canonical 永久非目标 | `REJECT`（`D-C2`）—— **`D` 判「这是本 lane 唯一一条会主动损害项目的建议」** | 三者是**数据设计限制**（`05` 自己在 U8/U10 给出解法），写成永久非目标会**关闭唯一能解决它们的研究计划**。I8 已被 Robitzsch 2023 反驳，I12 其实是书写约定 |
| **R-D2** | `05` §5 被呈现为一等交付物、单一逻辑类型 | `WRONG-SCOPE`（`D-C1`/`D-C10`） | 「换方法不能越过这一节」成立，但应拆成 `I-STRUCTURAL` / `I-DESIGN` / `I-LIT-OPEN` / `I-CONVENTION` 四类，并指出问题清单**本身**缺「被识别/不可识别」的显式标记 |
| **R-D3** | `05` I8：任何动态结论前必须先做 invariance 层级序列，否则结论**未定义** | `CONTESTED`（`D-C3`） | 应改写为「**未测不变性时强均值比较未定义**；aliasing 仍可做**」 |
| **R-D4** | `05` I12：状态转换可识别性 | `WRONG-SCOPE`（`D-C4`） | 同一 `psi(t)` 序列在不同 lag / 分辨率下给出不同 AR 系数；`+1` 不是自然量 |
| **R-D5** | `05` I9 Constraint 的 effect estimand | `CONTESTED`（`D-C5`） | Constraint 是「未发生的事件」，无反事实对照就无 estimand；统计上是 **structural zero / undefined**，不是 `0` |
| **R-D6** | `06` §8 E 行：「存在一条独立的正向（趋近）分支」与「存在一条独立的抑制/修复分支」均标 **`SUPPORTED`** | `WRONG-SCOPE`（`D-C17`） | 两行改标 `MODEL_HYPOTHESIS`，理由写明「**来源全部是 outcome 层**」 |
| **R-D7** | `06 §10` 的「结构性」 | `ACCEPT` 但改词（`D-C35`） | `16:392` 的「结构性」改为「**数据收集方式的限制**」 |
| **R-D8** | `16` §6.1：「⇒ 默认几何 = dyad 分组 × 时间前向，二维同时施加」；`G1_BLOCKED_FORWARD` 为「**首选默认**」 | `UNSUPPORTED`（`D-C24`） | **`G1` 在逐字意义上就是 `16 §6.1` 自称「最危险的一种」**；`G1`/`G2`/`G3` 三者中**没有任何一种**实现「dyad 永不跨侧」。协议已把正确几何写进 `16:183` 的降级表，却没写进几何表 ⇒ **静默地把默认 estimand 降为 within-dyad 时间外推** |
| **R-D9** | `16` 的 freeze：字段 12 允许 `TBD_AT_FZ1` 而 holdout 在 FZ-0 后即解锁 | `NOT_ENFORCEABLE_AS_WRITTEN`（`ADJ2` Q4，`D-C25` 同向） | 存在一条**合规路径**做到「看数据后才定主 estimand」，正是 L7 要禁止的。`06 §12` 的「不要在 R16 之前冻结函数形式」与之合谋 |
| **R-D10** | `16` 的 `mapping_status` / `uncertainty` / `directionality_class` 三组枚举被称为「封闭受控表」 | `UNSUPPORTED`（`D-C21`/`D-C22`/`D-C23`） | 三处都缺值或缺互斥性。修法：拆出独立 `reliability_class`；补 `SELF_REPORTED_EDGE`（或 `BELIEF_ABOUT_EDGE`） |
| **R-D11** | `16` §5 的 `F-SELF19/20/21` 未被列为首要交付物 | `VERIFIED` 为**遗漏**（`D-C30`） | `F-SELF20`（「如果 schema 的层归属本身错了，本协议的全部 machinery 会忠实地验证一个错误的对象」+「**无。**」）是三份报告里最诚实的一句话。**建议提升为 `16` 的首要交付物** |
| **R-D12** | `06` §4.4「`Ded` 可与 `Trust` / `AttachmentSecurity` 解耦 = `SUPPORTED`」 | `WRONG-SCOPE`（`D-C33`） | 改标 `SUPPORTED（现象存在）/ ILLUSTRATIVE` |
| **R-D13** | `06` §9 裁决请求 2（`Ideal` 是否成为动态 directed state） | `CONTESTED`（`D-C34`） | 「**本 lane 提出的唯一会改变 schema 层级的建议**」——在 S31 原文与 S17 正文核实前，`Ideal` 不应进入 `PARAMETER_CONVERGENCE` |
| **R-D14** | `06` 判 H 与判 N | `ACCEPT` 但必须重写（`ADJ2` Q1） | **判 H 与判 N 无法被空结果推翻**——它们守的两个前提（「关系状态自然衰减」「分支由 dyadic state 决定」）没有失败路径。应重写或移入 `06 §10` 不可证伪清单 |
| **R-D15** | `06` §8.7 第 5 条的功效护栏只给律 E | `D-C16` 要求提升为跨律通用 | 否则判 A/D/G/K 会把**功效不足当成律被拒** |
| **R-D16** | `05` 判 I1 / I17 | `ACCEPT` 但补限定（`D-C9`） | trait 与 state 不可直接比较；`n=1` 时「不可识别」≠「换方法也做不到」 |
| **R-D17** | `10` §5 的 test table | `REJECT`（表格当前形态）（`F-C30`） | 合并第 4/7 行、第 21b/23 行；第 19 行的判定需撤回或改依据 |
| **R-D18** | `10` §4.8 / §13：dyadic coping 是文献中「**唯一**」被实验证明「两个有向状态的函数不足」的构念；`CommonDyadicCoping` 是「**真正的** pair-level 涌现候选」 | `UNSUPPORTED`（就「唯一」与「涌现」两处用词；底层 Bodenmann 结果本身 `VERIFIED`）（`F-C18`） | 删「唯一」与「真涌现」；保留为「文献中已知的、唯一一处两个有向状态的函数在**预测关系质量上**不足」 |
| **R-D19** | `10` 建立三档证据分级并据此把若干来源标为「本次实际读到原文」 | `UNSUPPORTED`（就这些具体条目）（`F-C31`） | 核实后发现若干条**分级或元数据与事实不符**。要求 `10` 在 §12 加一列 `page_verified` |
| **R-D20** | `09` §4.4 的三层（L-A/L-B/L-C + L-D） | `ACCEPT_AS_PROPOSAL` 但**改称**（`F-C13`） | 「L-D 不成立为独立层」⇒ 改称「**三层（L-A / L-B / L-C）+ 一个显式 join**」 |
| **R-D21** | `09` §9.6 的 **K9** | **`REJECT`**（`F-C14`；`ADJ2` 判 `VERIFIED`） | K9 把「**是否存在**已发表的双吸引域估计」这个**文献存在性问题**的否定答案计为对本报告结论的支持，而 §5.3 已自认检索有五条覆盖缺口 ⇒ **K9 不是 kill criterion，而是一台确认偏误机器**。必须换成数据条件。**同批修补**：K1 删掉使其几乎不可能触发的析取项；K7 被不充分证据预先回答，须重开；K8 的「若成立」分支改写为「若能证明 X」；K5 标为「已实现但未迁移」。**保留 K2 / K3 / K4 / K6 与整节撤退条件——那部分是本报告最好的可证伪设计** |
| **R-D22** | `09` 的「无任何框架 / 无迟滞 / 无阈值」absence 同时出现在 §2.1、§5.3、§8.4-A-4/5/6、§9.2-FACT-1/4、§9.8 | `UNSUPPORTED`（**作为累积论证**）；`corroboration: NON_INDEPENDENT`（`F-C16`） | **单一 absence，多处措辞不同但来源同一**。parent join 时**不得**把它当 5 条独立证据 |
| **R-D23** | `09` §7-O2 的 CLPM 推论：「低自回归 = 低信噪比，而这是**关系数据最常见的情形**」 | `PLAUSIBLE`（Hamaker 两句）/ `WRONG-SCOPE`（转述与归因）（`F-C9`） | 保留 O2，删去「这恰恰是关系数据最常见的情形」，把稳定性/trait 讨论分开 |
| **R-D24** | `09` §4.4 O3 的「`N<50` 时随机效应方差系统性正偏」 | `PLAUSIBLE`（Pohle 部分）/ `WRONG-SCOPE`（`N<50` 部分）（`F-C10`） | 把 `N<50` 那句移出 O3，单列为 estimand 限制 |
| **R-D25** | 「关系科学里跨文化不变的证据高度集中在依恋与性欲，而 LHRM 最缺的三个恰好是**零证据**」 | `PLAUSIBLE`（`F-C24`） | 保留为结构性观察，但把「零证据」改为「**本 packet 未检出**不变性检验报告」 |
| **R-D26** | `10` 的 `Mutuality_k(A,B,t) = H(D_AB, D_BA)` | `HOLD_FOR_EVIDENCE`（`F-C19`） | 朴素 `H(D_AB, D_BA)` 会系统性混入与本对无关的成分；应先残差化（控制 `R_k(i)`、`T_k(j)`）。**falsifier 已给出**：控制后 `H(e)` 若不显著优于 `H(D)`，则残差化不必要 |
| **R-D27** | `06 §4.3` 的 `RT`「由 dyadic state 决定」= `SUPPORTED` | `MODEL_HYPOTHESIS`（`ADJ2` Q1/Q5） | `06:810` 自陈「无来源直接检验」⇒ **律 E 的实质内容零直接支持** |

---

## R-E · belief / 形式化

| id | 必须撤回或重述的表述 | 判定 | 依据 |
|---|---|---|---|
| **R-E1** | `07` §2.3：在信息序 `⊑` 上 `N < B` 不成立，`N` 与 `B` **不可比**；唯一单调方向是 `B → T`、`B → F` | **`UNSUPPORTED`（`E-C3`）—— `E` 判「这是我在本 lane 找到的唯一内容错误，且它出现在承重的 `AI_RECOMMENDATION` 上」** | **与 K4 的构造相反**：近似/信息序上 `N` 是底、`B` 是顶、`T` 与 `F` 不可比；逻辑/真值序上 `T` 是顶、`F` 是底、`N` 与 `B` 在两翼不可比。`07` **把两个格的性质互换了**。「双序」这个**结论**保留（`E-C4` `VERIFIED`），但**理由与方向必须改**——否则 `value_class` 的设计依据是错的 |
| **R-E2** | `07` §2.3 据此推出「状态侧必须至少有两个序」 | `REJECT`（针对 §2.3 这一条，**不是**拒绝双序结论） | 正确的形式化见 R-E1 |
| **R-E3** | `07` 对「missingness lowers certainty, not computability」的指派 | `VERIFIED` 为**不存在**（`E-C1`）—— **`E` 判「这是本 lane 最有价值的一条，应作为 `NEGATIVE_RESULT` 进入 join」** | 该句在 `youling/lhrm` 仓库内**字面不存在**。项目实际持有的更弱区分性陈述是 `STAGE_SUMMARY_2026-09-07.md:162` 的 `Computable != Certain` |
| **R-E4** | `07` §2.1 的 `2^B` 组合复杂度 | `PLAUSIBLE`（`E-C7`） | `HOLD_FOR_EVIDENCE` —— 在打开 Renz 2007 之前不进入排序；并要求 `07` 补一句「若只使用 `ORD-Horn` 之类 tractable subset」 |
| **R-E5** | `08b`：「整条链可用 **8 个逐记录带类型槽位 + 2 个逐 (持有者, 内容) 带类型标量 + 4 个派生类 + 1 个世界模式标签** 表达；**没有第九个原语，没有 credence 字段，没有 modality 深度**」 | `UNSUPPORTED`（对「**最小**」这一强主张；设计本身可接受）（`E-C18`） | `ACCEPT_AS_PROPOSAL`，但要求 `08b` (i) 把 `M` 明确标为「**有意的设计选择，不是最小性证明**」 |
| **R-E6** | `07` 的部分可观察性论证 + 「`g = FIRSTHAND` 可赋值」 | `VERIFIED` 引文（`E-C10`）；**但** `07`/`08b` 的 `g` 赋值依赖「哪些构念原则上可被直接观察」的清单，而**项目内不存在该清单** | `E-C16` 判 `ACCEPT`，并列为**本 lane 唯一的 head-of-list 阻塞项**：它同时阻塞 `07` 的 `Unknown` 类型学落地、**`07` 的 `⊑` 程序（I9 需依赖表）**、`08b` 的整个 belief 层、以及 `02` 已局部提出的单构念登记。**它是一条 Architect 裁决，不是研究问题。** |
| **R-E7** | `07` §9.3 / `08b` §2 的 `Belief_i(·)` 命名 | `ACCEPT_AS_PROPOSAL`（`F-C33`） | `09` 与 `10` 对同一层用了两个名字（`L-B = Belief_i(A–B 是什么)` vs `B_i(X) = i 关于 X 的信念`）⇒ 统一采用一个符号 |
| **R-E8** | `07` §11-3 与 `08b` §9-1 各自的 Unknown 编码 | `VERIFIED`（`E-C23`） | 见 `HIGH_CONFIDENCE_FINDINGS.md` H-F15。**处置**：`ACCEPT` —— 把「缺失性 / 不适用性 / 冲突 / 不可寻址」的分区作为**一条** canonical 决议，强制 `07` 与 `08b` 合并 |
| **R-E9** | `07` §5「以下 15 条」与「9 条现在就能检查」 | `VERIFIED` 缺陷（`E-C12`）/ `REJECT` 计数（`E-C11`） | 应为 **19 条**；且 I14 / I17 / I18 不可执行、**I19 空过**（任何非恒定函数都满足）、I10 可被博弈式反例击穿 |

---

## R-F · 动力学

### R-F1 — 「生理同步 `ES=.09` ⇒ 强耦合前提在多数真实 dyad 中不成立」

- **判定**：**推论 `REFUTED`**（`EV3` Claim 3 (b)）；**效应量与方向 `VERIFIED`**（`EV3` (a)）
- **严重度**：`EV3` 自评**中等**（措辞/推论层严重，承重性可低成本切除）
- **`EV3` 的五条理由**：
  1. `09` **没有**在任何地方声称 Mayo 测量了「多数真实 dyad」。`09:441` 的措辞是「**强耦合在多数真实 dyad 中不成立**」，
     即一个由 pooled 研究层统计量推出的 **dyad 层**结论。**这是报告的量纲错误（研究层 → dyad 层）**，独立于其它四条理由，也独立成立。
     Mayo 报告的是 k 项研究的合并相关，其抽样单元是**研究**，不是 **dyad**。**`I²=76%` 恰恰意味着研究间不一致，进一步阻止向 dyad 层外推。**
     `EV3`：「这一条我认为是 (b) 最难辩护的部分。」
  2. **方向不可分解**（独立成立）。
  3. **尺度错置**（独立成立）。
  4. 作者说的是 `point to the need for`（指向需要），是对**未来研究议程**的建议，**不是「禁止引用 pooled 估计」**。
     `EV3` 把理由 4 从「无效」降为「**强烈提示误用**」。
  5. 若有人主张生理同步**是** mechanism evidence，则「mechanism evidence 可以约束状态结构假设」可以辩护——
     **但这救不了 (b)**，因为 `03:185` 自己在同一 PR 里把 ANS 归为 mechanism evidence 并判 `NOT_IDENTIFIABLE`。理由 1 应被视为**加强项**而非独立承重项。
- **`EV3` 反对把严重度定为严重的三条理由**（其中两条是**对 `09` 有利的**）：
  - `09:434` **独立地**（文献检索负结果）得出「迟滞是 `model hypothesis`」；`09:576` 声明「不主张迟滞已被证明，也不主张迟滞已被排除」；
    `09:648` 声明「若它将来出现，本节的判断必须重做」。⇒ **「报告结论错误」不成立——错的只是通往结论的中间一步。**
  - 若连 `FACT-1` 的锚点也须切除，§9 的论证会变薄——**但 `FACT-1` 的命题（无框架有合格参数估计）是文献缺失断言，可独立于 Mayo 成立**；
    被切除的只是它的一个**不合格锚点**。⇒ **修复是「换锚点」，不是「塌房」。**
- **替代表述**：把「强耦合前提在多数 dyad 中不成立」改写为「**当前可用的耦合代理与关系结局关联弱且 `I²=76%`、情绪协动超伪伴侣仅 14–38%**」这一**方法/测量事实**。
- **引用约束**：`B` 补充——引用这组数字时**必须同时带 `I²=76%`**。

### R-F2 — 「迟滞是人类二人关系的可观测动力学性质」

- **判定**：`UNSUPPORTED`（`F-C1`）—— 维持 `UNKNOWN` / `model hypothesis` 标签
- **重要限定**：`F-C1` 自陈**「在已检索场所内未找到」≠「不存在」**。`09` §5.3 已自认五条覆盖缺口。
  ⇒ 这是 `NEGATIVE_RESULT` 级的 `UNKNOWN`，**不是**领域否定。
- **不得**与 R-F1 混用：R-F1 的推论错，但 R-F2 的 `UNKNOWN` 标签**正确**。

### R-F3 — 「四层皆非引擎」的可撤销性

- **判定**：`ACCEPT` 但换依据（`F-C12`）
- **必须同时换掉 K9**（R-D21）：否则 `09` §9 的「四层皆非引擎」判决**不可被证据撤销**。
  `ADJ2` rec 5 独立指出同一点，并要求把 `F-C11` 的 ESM/IL/EMA escape clause 补进 `09` §4.4 ——
  **这一条同时是 `RT` 的唯一可行数据 regime 的入口**（律 E 需要事件内顺序 = 密集设计）。

---

## R-G · 一般 dyad 范围 / ABM / LLM 层

| id | 必须撤回的表述 | 判定 | 依据 |
|---|---|---|---|
| **R-G1** | `11` §3.1 的**值类封闭集逻辑矛盾**主张（`G-C4` / `G-C5`）——「唯一的合法表示方式就是把不适用填成 0 或 Unknown」「U1…U12 任何实验都无法裁决」 | **`REFUTED`（`EV3` Claim 1）** | 值类清单是**许可式而非封闭集**（`可以` / `may be`；两份清单互不一致；全库无封闭性声明）；canonical **已有**具名槽位 `BoundaryRule_(A,B,domain)`（`PARAMETER:359-367`）与针对 `性欲` 的 worked example（`CURRENT_ARCHITECTURE:190`）。详见 `CONTESTED_FINDINGS.md` X-5 |
| **R-G2** | `12` §0 headline「不存在可比 ABM」+ §1「LHRM 不是落后，而是**孤立**」 | `REJECT`（`G-C17`） | 见 R-0.1。**必须**改述为「在本 lane 已检索场所内未找到」 |
| **R-G3** | `12` §3.1 C-SAOM 推论：「二值化也**直接违反** LHRM 的混合态表示」 | `WRONG-SCOPE`（`G-C16`） | 推论**遗漏了同页的例外句**。第一条（SAOM 状态严格二值）`VERIFIED`；第二条（creation/endowment/evaluation 不可共线）`PLAUSIBLE`（未找到出处） |
| **R-G4** | `12` 对 ABM 的正面定位 | `HOLD_FOR_EVIDENCE`（`G-C18`） | 方向可辩护，但报告**低配了自己的正面证据**（`Grazzini & Richiardi 2015` 的依赖图部分 `G` 判 `VERIFIED`，**且方向与 `12` 所述相反**——好消息）。**不要按「ABM 是隐喻生成器」的现有形式引用** |
| **R-G5** | `11` §2 把 `Trust` 在 S/K/C/W/A 五列判为 `MEANING_SHIFTS` | `REJECT`（`G-C10`） | 唯一支撑是一个**定性同胞访谈研究**；`11` §6.2 **自己**把同一格称为「**定义欠定**」而非「语义改变」。另 `G-C30` 判 `CONTESTED`（报告内部自相矛盾） |
| **R-G6** | `11` §4 `L-1`：`OutcomeDependence` (D8) 的措辞读起来是关于 i 的 option set 的中性事实 | `VERIFIED` 为**安全价值最高**的措辞缺陷（`G-C9`） | 一个健康的高照护 dyad 与一个胁迫 dyad（intimate terrorism）在 D8 上**数值结构相同**，`R2 PowerImbalance` 会打成同一类，**而它们在伤害上相反**。**措辞读起来是中性事实，它实际是伤害结构本身。** |
| **R-G7** | `11` §3.2（`Obligation` directed construct）+ §3.7（`RoleContract` pair fact）+ §4 `L-10`（`family obligations` 放 Agent 层是层级错置） | `REJECT` 三项分列（`G-C7`） | 三项**最终都主张同一件事**：义务/契约性内容属于 pair-institutional 层。**三重计数** ⇒ 合并为**一条** canonical 候选 |
| **R-G8** | `11` §3.3（`Constrainedness` 提案）作为**主论据** | `ACCEPT_AS_PROPOSAL` 但换主论据（`G-C8`） | 支撑引用全部著录不完整。改用 §3.3 的结构性论证（`ConstraintsAndAgreements` 与 P5 都内建同意/consent，但域已写入「违法或违反社会规范」；非自愿约束既不是 agreement 也不是 `Environment` 也不是 `Agent`——**违法性有轴，但约束能力本身没有坐标**）。`11` §5 排序明标「**安全价值最高**」 |
| **R-G9** | `11` §3.7：「`AGENTS.md`『Keep `Role` explicit as a query lens』在专业/亲属/照护三类 dyad 上**不成立**」 | `HOLD_FOR_EVIDENCE`（`G-C14`） | `PLAUSIBLE`（对「专业 dyad 上 role 是承重变量」）/ `WRONG-SCOPE`（对「因此 AGENTS.md 第 3 条不成立」这一步）。**保留 `Role` 作为 query lens**；新增 `RoleContract_(A,B)` pair fact |
| **R-G10** | `13` §13.1 的目标重定向 | `ACCEPT`（保留）（`G-C21`） | 「LHRM 第一产物是 latent dyad state，没有 ground truth 也**不应该**有，因此『抽取准确率』在 LHRM 语境下**没有定义**」= 方法论论证 `VERIFIED` |
| **R-G11** | `13` §13.2 的六项指标作为**充分**评估工具 | `UNSUPPORTED`（`G-C21`） | 存在**两个平凡策略同时最大化全部六项**。另见 H-F20（对自己的 gold 不施加循环论证标准） |
| **R-G12** | `12` §4.2 元证据第 2 条（Grazzini & Richiardi / Angus & Hassani-Mahmooei 扫描 100+ 篇 JASSS ABM） | `PLAUSIBLE`（Angus 那条 `G` 未核实原文）；**依赖图部分 `VERIFIED` 且方向相反**（`G-C27`） | 保留 C1/C2/C6 三条失败模式；元证据须单独核实 |
| **R-G13** | `11` §9 的 Olson, Russell & Sprenkel (1983) DOI；`12` 附录 A 的 Edmonds→Edwards；`13` §9.6 的 arXiv 题名单数化 | `RECLASSIFY_AS_METHOD_LIMIT`（`G-C24`，三处均经独立核实） | — |

---

## R-H · 定位 / 新颖性

| id | 必须撤回或降级的表述 | 判定 | 依据 |
|---|---|---|---|
| **R-H1** | `14` §1 BLUF：「LHRM 的 8 个有向构念**全部是 REUSE，无一条可主张原创** / 强度=高（逐条有 DOI）」 | `UNSUPPORTED`（`H-C17`） | 至少两条 REUSE 断言的证据分级与元数据不符；`H` 的 §12 指出「14 §9.3 的 7 条 O-row 中 5 条引用问题」 |
| **R-H2** | `14` 的 novel-combination 论证；「F-1…F-20 这 20 条禁止主张清单是完备的」；「F-6 与 F-16 各自独立」 | `UNSUPPORTED`（`H-C25`/`H-C27`/`H-C28`） | §3 开头的通用警告（"这是定位失败最常见的模式"）**足以防止本报告自己犯 novel-combination 错误**；20 条清单不完备；F-6 与 F-16 **不独立**（`H-C29` `CONTESTED` 判「重复计数」） |
| **R-H3** | `14` 的 NC-1 / NC-3 / NC-5 置信度 | `CONTESTED`（`H-C18`/`H-C20`/`H-C22`） | NC-1 窄化后 MEDIUM / 按现状表述 LOW；NC-3 MEDIUM-LOW；NC-5 MEDIUM |
| **R-H4** | 「F-1 与 REUSE 表 L40 是两条独立结论」 | `CONTESTED`（重复计数）（`H-C29`） | — |
| **R-H5** | `14` §6 的 M0–M5 ≈ 5–7 个月单人全职；M2 估 4–6 周 | `UNSUPPORTED`（`H-C36`/`H-C37`） | 工期估计无任何可核依据 |
| **R-H6** | M7（测量学，2–4 个月，N≥数百）在 M0–M6 之后可达 | `WRONG-SCOPE`（**依赖倒置**）（`H-C38`） | — |
| **R-H7** | M8 的估计与「阻塞后续：否」的标注 | `CONTESTED`（`H-C39`） | — |
| **R-H8** | `15`（CASEBANK_EXPANSION）被当作 `16` 的上游依据 | 覆盖缺口 | **无 lane 覆盖 `15`**；`I-C26` 自陈「要补 R04/R10 才能称『Wave 1 全覆盖』」 |
| **R-H9** | `14` 的 README / `STAGE_SUMMARY` 相关 6 条（`H-C50`–`H-C66`） | 混合：多数 `WRONG-SCOPE`（措辞问题被读成能力/验证陈述），`H-C58` 建议**收窄为 `findings` 标签问题**，`H-C60` 建议**降级为历史 draft 的措辞问题，不是 canonical 定位问题**，`H-C66` `VERIFIED`（建议把 `O-17` 当作其余各行的改写范本） | `H` §9.4-§9.5 |

---

## R-I · red-team / Gate

| id | 必须撤回的表述 | 判定 | 依据 |
|---|---|---|---|
| **R-I1** | `17` F4：复合态无法由「每构念一个坐标」表达，状态空间**必须增加模态/析取层** | **`REJECT`（作为架构主张）**（`I-C19`） | MacDonald 是**冗余证据**，Zoppolat **支持**现有分离。真实的现象改写为 Gate C 冗余条目 + 已有 Observation/Belief 分离条目。**不要据此引入 lattice/析取状态空间** |
| **R-I2** | `17` F3 / A5 / A20 / A21 的**单向提升**形式 | `RECLASSIFY_AS_METHOD_LIMIT`（`I-C17`） | 采用 `A03` 改写 4 的**双分支竞争假说登记**形式，不采用单向提升。**必须**连带处理 X-3 的残留 facet 切点 |
| **R-I3** | `17` T5：`CONSTRUCT_SCOPE_DIRECTIONALITY` §1 的加性分解 | `PLAUSIBLE`（设计异味成立，但取证偏重）（`I-C25`） | 降为待检验命题 |
| **R-I4** | `17` §4 表的 12 条 `CHALLENGED` 的可攻击性 | `HOLD_FOR_EVIDENCE`（`I-C14`） | S 编号不可解析 ⇒ 至少 A2/A4/A5/A… 无法被外部复核 |
| **R-I5** | `A03` §4.4「writeback 阶段不存在判据弱化」这条**机器可核否定结果** | `PLAUSIBLE`（`I-C26` 自陈「我无法复现其 `Compare-Object`」） | 结论方向很可能对，但**必须补 R04/R10 才能称「Wave 1 全覆盖」** |
| **R-I6** | `A03` H-3 的范围 | `ACCEPT_AS_PROPOSAL` 但**更正范围为「三份全部」**（`I-C27`） | `SPAN_SUPPORT_RATE` / `ENTITY_INSERTION_RATE` 在 Fixture 003 上**永久不可计算**（就仓内证据而言），成因分两类 |

---

## R-K · cross-lane 冲突图

| id | 必须撤回或重述的表述 | 判定 | 依据 |
|---|---|---|---|
| **R-K1** | `18` CF-00 的 sibling 引用数字 | `PLAUSIBLE`（`K-C1`） | 「17 独立单点 + 1 join lane」的**定性**结论成立；数字在 durable 文本上不可复现且**系统性低报**。要求 `18` 补可复现的扫描协议并把结论改写为「Wave 1 内 17…」 |
| **R-K2** | `18` 的冲突面**完备性** | `UNSUPPORTED`（`K-C3`、`K-C31`） | CF-03 漏了 5 个触碰 `PPR` 层位的 lane；**更严重**：`18` 的冲突面**系统性遗漏了「否定型」声明**——`R10 §8` 的 **16 条缺口登记**（含 **8 条 `construct hole`**、2 条 `ontology hole`、1 条 `projection hole`）是全语料最大的单张「不该加什么」清单，而 `18` 全文 grep `construct hole` / `UNKNOWN_AS_OF` / `G16` = **0 命中** |
| **R-K3** | `19` §4 的「5 条律是 5 个真正不同的机制族」 | `ACCEPT`（`K-C33` 成立）**但** `19` §4 **未交叉引用** `18` §5.2/§5.3 | 按 `18` 的可组合性检查，**5 条律中至少 2 条（L1=`律A BMR` 经 U-1/U-2、L5=`律E RT` 经 U-3）的判别部分在当前数据下不可执行**，而 `19` 把它们列为「值得以后冻结」且**未加任何限定**（`K-C34` `WRONG-SCOPE`） |
| **R-K4** | `19` 的 L1 与 C-1 是两个独立决定 | `CONTESTED`（`K-C35`） | L1 `BMR` 的关键支持是 Laurenceau 1998/2005「PPR 为部分中介」，而 C-1 正在裁决 PPR 是否属于 Belief 层。若 C-1 判 `R06 §4.9` 的 B4 null 成立（`Z` 与 `PPR` 是同一测量，应**合并**），则 L1 的经验支点被吸收。`SAME_SOURCE` |
| **R-K5** | `19` 的 lane 计数 | `ACCEPT_AS_PROPOSAL` 全面重标（`K` top_rec 7） | 至少 **A4（删 `A02`）、A6（4→2）、A1/A10（合并，D-02 与 D-03 是同一段 canonical 文本）、A7（删「R10 未主张」）、A10 机制 3→2**；并**补入 D-01**（8 lane 的 `State != Action`，全语料最强收敛却未进 §1）。另修 `19:352`：A01×A04 的 DOI **语料**重叠实测 352/363 |
| **R-K6** | 「`Unknown` 值类被**五**个 lane 各自重新发明」 | `UNSUPPORTED`（对「五」）（`K-C7`） | 改述为「**至少六套**」，并指出 `UNKNOWN_AS_OF` 覆盖 6 条 Wave 1 lane 且是**全语料使用最广**的一套 |
| **R-K7** | `18` N-01 的 SSOT 修法（把五套映射成 `R07 §9.3` tag 集的子集） | `WRONG-SCOPE`（`K-C8`） | **类型上不完整**：`R15` 的 `MAPPING_FAILURE` 是**表示失败**而非证据状态，`18` 自己已指出「它在 `R07` 的 tag 集合里**没有对应值**」，却仍把修法定为「映射到子集」。应改为**两轴合并**（`tag` 证据侧 + `applicability` 适用性侧） |
| **R-K8** | `19` 声称 WO-N1 是「**唯一的真正阻塞项**」 | `WRONG-SCOPE`（`K-C46`） | 它把**三种不同的「阻塞」压成一种**：N1 阻塞**验证程序整体**（门不能失败）；N2/N3 阻塞**内容**（层归属与值类未定，则新能失败的门是在测一个未定 schema）；N6 阻塞**经验接入** |

---

## R-L · actionability / Work Order

| id | 必须撤回或重述的表述 | 判定 | 依据 |
|---|---|---|---|
| **R-L1** | `19` §7 的 8 个「Work Order」作为 8 个待批事项 | `WRONG-SCOPE`（`K-C44`） | 重分类为 **3 决策 + 3 派工 + 1 基础设施请求 + 1 书目核对**（见 `CANONICAL_CHANGE_PROPOSALS.md` C-P9） |
| **R-L2** | `19` §7 优先级 1 = 「**唯一的真正阻塞项**」 | `UNSUPPORTED`（`L-C17`；`K-C46`；`ADJ3` Q7） | 见 `CONTESTED_FINDINGS.md` X-12 |
| **R-L3** | `19` §7 排序依据「修起来便宜 / 收益大」 | `UNSUPPORTED`（`K-C45`） | 见 H-F36。**但** `19` 对 N1→N7 的**依赖顺序判断是正确的**，应保留 |
| **R-L4** | `19` 的 8 个 blocker 里有 8 个待修项 | `WRONG-SCOPE`（`ADJ3` Q8） | **真·架构设计任务 = 1 项**（`B-6`）；**研究设计任务 = 2 项**（`B-7`/`B-8`）；**环境/治理限制 = 3 项**（`B-1`/`B-2`/`B-5`）；**负结果误占 blocker 位 = 2 项**（`B-3`/`B-4`）。`19` 自己在 A9 已把 `B-4`（迟滞无估计）正确处理为负结果，**同一份文件对同一件事给了两种分类** |
| **R-L5** | `19` §1 A11（「爱/亲密/嫉妒/忠诚 不宜作 primitive」）作为**需要 Architect 决策的发现** | `UNSUPPORTED`（`L-C16`）—— `REJECT`（不占用 Architect 决策） | 该裁决已是 `PARAMETER_CONVERGENCE` §12 的**现行条文**，且词表逐条相同。⇒ 在 LHRM 内部**没有任何决策后果**，可作为「已决事项的外部文献佐证」归档（`ADJ3` N-A11 同判，标 `independent_sources = 0`，**移出 agreement 表**） |
| **R-L6** | `19` §8 的 B-1…B-8 与 `00_MANIFEST` §4 的 B-1…B-9 可互指 | `VERIFIED` 为**编号冲突 + 成员不相交**（`L-C18` + `ADJ3` Q7/Q8） | 见 H-F34、H-F39。`00_MANIFEST:133` 还把 Architect 指向「`19` §8 与 `AGENT_TERMINAL_RESULT` comment 为准」——**指向两份成员不相交的 register** |
| **R-L7** | `WO-N8` 作为 Work Order | `REJECT`（`L-C20`） | 改为一次 **bibliographic check，先修引文，再检索**。`WO-N8` 要核的 `Boyd & Heewer (2007)` 极可能是 **Boyd & Hilton (2007), *The law of the wed: A lateral theory of marriage*, Cognition**（Heewer 是第三作者）⇒ **`WO-N8` 自己的前提引文就带一处与它要复核的 prior art 同类的作者错误** |
| **R-L8** | `19` §5 的 WO-N6（三项数据集核实） | `RECLASSIFY_AS_METHOD_LIMIT`（`L-C13`） | 拆为「**基础设施请求（egress）**」+「**数据存储决策（需 Human 决策：数据落在哪、是否入库、许可/署名政策）**」。本仓库**没有 data 面**（无 `data/` 目录）⇒ 即使 D04 也被**存储决策**阻塞 |
| **R-L9** | `19` §4 的 L3 / L5 是「candidate law」 | `REJECT`（对 candidate 身份）（`L-C15`）**—— 但 `ADJ2` 推翻了理由** | `ADJ2`：`L-C15` 是 `WRONG-SCOPE`（不是 `VERIFIED`），且**单 lane 且错误**——判 G 未触发、性别不对称**未检出**。⇒ 两条仍是 `RESEARCH_CANDIDATE`，但 `19` 的两格措辞必须改。见 `CONTESTED_FINDINGS.md` X-11 |
| **R-L10** | `19` 的「A01 83 条 `NARROW_REPAIR_REQUEST` 已大部分修复」 | `VERIFIED` 为**约 13 条**（`J-C19`） | ~13 已修、~70 未动、其中 ≥4 条 `MAJOR` |

---

## R-4 · 结构性记账（不是单条主张，是**三处必须先修的 register 缺陷**）

`ADJ3` Q8 明确：**register 层面必须先修三处，否则 join 会产出错误数字**。

1. **`B-3` 编号冲突**：`19:343` = ESEM 负结果；`00_MANIFEST:125` = 跨 lane 全局去重（并指向 `§4 B-9`），而 `:131` 的 `B-9` = **同一件事**。
   ⇒ manifest **内部** `B-3` 与 `B-9` 重复编号。
2. **成员不相交**：`19` §8 的 B-1…B-8 与 §2 的 C-1…C-8 **只有 `B-6 ↔ C-3` 一项对应**；
   `C-1`/`C-2`/`C-4`/`C-5`/`C-6` 在 §8 无编号。⇒ **不是「编号错乱」，是「分母不同」**（H-F39）。
3. **`B-4` 双重分类**：§1 `A9` 当作重要负结果，§8 当作 blocker。

**`ADJ3` 给出的替代 blocker 分类**（见 `CANONICAL_CHANGE_PROPOSALS.md` C-P9）：

| 真类别 | 计数 | 成员 | 需谁裁决 |
|---|---|---|---|
| **A · 架构设计任务** | **4** | `B-6`（门不能产生否决）+ `C-1`（`PPR` 层归属）+ `C-2`（`OutcomeDependence` 四种互斥 ontology）+ `C-4`（`Unknown` 类型学） | **Human / Project Architect** |
| **B · 研究设计任务** | **2** | `B-7`（`Liking ↔ RA` 判别效度检验）+ `B-8`（`OutcomeDependence` 关系级工具） | 统计 / 测量专家 + Human 授权；**不需架构裁决** |
| **C · 环境 / 治理限制** | **3** | `B-1`（egress）+ `B-2`（Gilligan 2017 不可得）+ `B-5`（`#20-22` 隔离） | **无人可裁决**；contract §3 禁止绕过 |
| **D · 负结果（不是 blocker）** | **2** | `B-3`（ESEM/bifactor 负结果）+ `B-4`（迟滞无估计） | 无。**须移出 blocker register** |
| **E · 尺度冲突（同 A 类但登记在 §2）** | **1** | `C-6`（`CR-7`：事件内分辨率 / 月–年级 `tau` / 月–年级无 `Trust`/`Dedication` state 工具） | Human / Architect |
