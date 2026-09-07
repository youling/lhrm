# Research Report: Dating App Parameter Primitives

**work_coordinate:** `youling/lhrm#5@deep-dating-app-parameter-primitives`
**parent:** `youling/lhrm#2`
**role:** Research
**supersedes:** `youling/lhrm#5@research-dating-app-parameter-primitives`（dispatch `5565095981`）
**current_rulings:** `youling/lhrm#2` comments `5565170990`、`5565245810`
**as_of:** 2026-09-07
**version:** v1.0.0 (research deliverable, not canonical ontology)

> 本文是 Research 交付物：反向工程婚恋/相亲/约会产品如何把真实人际关系问题压缩进用户可填字段、偏好、过滤器与匹配信号，并把这些表面字段拆到更基础、低冗余的构念。本文**不修改 canonical ontology**；全部 primitive 候选均为供 Project Architect 在 join gate (`#2 comment 5565098184`) 处融合裁决的取证材料。
>
> **证据纪律**：官方文档/帮助中心/官方博客记作 `official`；可靠二手（分析、评测、一手体验报道）记作 `secondary`；无法由公开资料核验的算法细节一律标 `Unknown`。推断性建模结论明确标为 `hypothesis`，不与经验事实混同。

---

## 0. 摘要（结论先行）

婚恋/相亲/约会产品在做同一件事：把「两个人是否可能建立、维持某种关系」这个复杂动态问题，压成**一张有限枚举的表格**。产品不知道 D 层（二人互动层）的任何事，只能靠 S/O 层的自报字段 + 行为信号 + 事后反馈去逼近。本次反向工程确认了如下机制性结论：

1. **产品普遍存在 6 类字段压缩套路**（详见 §4）：身份与偏好合并、吸引与意图合并、历史与当前状态合并、资源几重含义叠加、派生标签冒充独立字段、行为信号被当成偏好；单位制字段（单选/多选的枚举）是压缩的直接载体。
2. **「说出口的理想型」与「做出来的选择」系统性不一致**，已在学术层面确立（Eastwick & Finkel 2008；Hitsch et al. 2010；Eastwick et al. 2014 meta；Finkel et al. 2012 PSPI 综述）。因此产品的 declared preference 字段只能当「自报信念」用，不能当真值；滑动/搜索行为是 revealed 信号，也需要区分「兴趣揭示」与「真实关系适配」。
3. **绝大多数产品默认「异性、陌生起点、单一浪漫目标」**，但这一默认是产品假设（市场选择），不是关系模型真值；甚至同一公司内「身份」「性吸引」「浪漫意图」「关系目标」被揉进一个字段的现象普遍存在。这些默认不得被带回 LHRM（#2 `5565170990`）。
4. **字段冗余最严重的是若干固定组合**：年龄/年轻外貌/生育代理；收入/资产/消费力/肯花钱；学历/智力/阶层/门当户对；陪伴/时间/可得性/响应；宗教身份/虔诚度/保守价值观；星座/生肖/血型 = 生日派生标签。这些组合在模型中若分别独立计数会系统性重复。
5. **产品的匹配分数没有任何一个可被当作现实真值**：算法全部闭源（除 OKCupid 的概念层公式和 Zoosk 的行为学习描述），且学术综述（Finkel 2012；Joel et al. 2020）显示人格问卷类输入对「关系走向变化」的预测力趋近于零。

**对 LHRM 的净结论**：产品字段是「可填写的观测」(Observation) 和「可声明的信念」(declared belief)，不是 primitive。能从中提炼的 primitive 候选是少数几个跨语境稳定的构念簇——资源、身份、身体、意图/目标、行为习惯、关系历史/义务、可得性/注意力、互动质量（仅能由行为信号逼近）。这组候选清单见 §8，全部标注为候选而非定论。

---

## 1. 方法与证据层级

### 1.1 反向工程方法

对每个产品，采集四类信息：(a) 档案字段本体（用户能填什么）；(b) 偏好/过滤字段（用户能声明什么要求）；(c) 权重/硬性表达机制（要求是否可分级、是否可作 dealbreaker）；(d) 匹配机制公开度（官方如何描述算法）。然后对表面词做「一对多」拆解，落到基础构念，并逐项做跨语境反例测试（§7）与重复计数审计（§9）。

### 1.2 证据层级

- **`official`**：官方帮助中心、官方博客、官方隐私政策/备案、App Store 官方页、学术论文原文。凡涉及产品字段/机制的直接引用，优先以此级为主。URL 见 §11。
- **`secondary`**：可靠二手（评测、行业分析、一手体验报道、存档镜像）。此类仅用于补足官方未公开的细节（如问卷措辞、过滤列表、算法传闻），并在报告中显式标注。
- **`Unknown`** / `unknown`：算法权重、排序公式、内部匹配度计算等无法公开核验的内容；报告中统一以 `Unknown` 标识，不补造数值。

### 1.3 样例规模

- 覆盖产品/系统 **19 个**（含 4 个中国平台、1 个学术性 speed-dating 系统）> dispatch 要求 10+。
- proxy 拆解 **144 条**（A–J 十簇，§6）> dispatch 要求 100+。
- 极端/跨语境反例在 §7 逐条给出核心测试结论，与 #4/#6 的 anti-例证方法对齐。

---

## 2. 产品/系统矩阵（10+）

代号：S=滑动类，Q=问卷/心理测评类，F=过滤/检索类，B=行为学习类，H=人工红娘+字段类，LBS=基于位置。

| # | 产品 | 市场/类型 | 核心档案字段簇 | 偏好表达机制 | 权重/硬性表达 | 算法公开度 | 身份字段 | 意图字段 | 默认假设（异性/陌生/单一浪漫） |
|---|---|---|---|---|---|---|---|---|---|
| 1 | OKCupid | 国际 / Q+F+B | 年龄、性别、取向、身高、体型、学历、收入、族群、宗教、政治、烟酒、孩子、关系类型、星象、身份标签 | 过滤器 + 数百道题「可接受答案」 | 每题重要性 5 档，最高档 Mandatory = 硬性 | 概念层公开，公式闭源 `official` | 22 性别 / 20 取向 (official) | Looking For + 非一夫一妻支持页 | 不默认异性；仍默认陌生起点与浪漫目标（含朋友项） |
| 2 | eHarmony | 国际 / Q | 年龄、所在地、生活方式、关系目标；问卷驱动 | 无公开搜索，偏好全部来自问卷 | 问卷内部隐含权重 | 闭源；官方只述 60–140 分 | 男人/女人/非二元注册 + 寻求 (official) | 产品级默认长期/婚姻 | 默认陌生、婚恋；历史上异性导向为主，2019 后同性别可匹配 |
| 3 | EliteSingles | 国际 / Q | 年龄、身高、学历、职业、收入、关系状态、孩子、宗教、烟酒 | 年龄段/地区软参数 + Have-you-met | 问卷重要性 + 软过滤 | 闭源；官方述 Big Five + 每日 3–7 推荐 | 注册男人/女人 (+多数高学历定位) | 长期关系默认 | 默认陌生、长期、异性倾向 |
| 4 | Match.com | 国际 / F+B | 身高、体型、族群、宗教、学历、职业、收入、关系状态、烟酒、孩子「有/想要」、Core Values | 丰富过滤 + Dating Intention | 每属性 Must-Have / Nice-to-Have 两档 | 闭源（品牌名 Synapse） | 支持同性；面向取向选择 | Dating Intention 下拉 | 支持同性；仍默认陌生、浪漫目标 |
| 5 | POF | 国际 / Q+B | 族群、身高、体型、学历、职业、关系状态、孩子、烟酒、兴趣 | 细粒度搜索过滤 + Chemistry Predictor | 过滤硬参与；问卷五因素可见分 | 概念公开（五因素），权重闭源 | 历史上二值（secondary） | 关系目标过滤(secondary) | 异性默认（历史上）；陌生+浪漫 |
| 6 | Zoosk | 国际 / B | 照片、年龄、身高、体型、学历、职业、族群、宗教、烟酒、关系状态、孩子、兴趣、关系偏好 | Carousel 滑动 + 搜索过滤 | 无问卷；权重完全隐式化到行为 | 行为学习概念公开，模型闭源 | 男人/女人注册（非二元未见 official） | 关系偏好/目标字段 | 默认陌生+浪漫；对偶配对被弱化 |
| 7 | Tinder | 国际 / S+B | 照片、bio、兴趣、生活方式标签（烟酒/家庭计划/宠物）、代词、身高、关系目标、语言、学校/工作 | Discover 过滤（距离/年龄/同取向优先）| 无 dealbreaker 机制；唯一排序开关「同取向优先」 | 官方公开 like/nope 聚合 + 明示不考虑社会地位/宗教/族群 | Beyond Binary + 取向（≤3，可隐藏） | Relationship Goals 5 档 | 性别多样；仍默认陌生+浪漫（含 New friends）|
| 8 | Bumble | 国际 / S+B | 工作、学历、性别、所在地、故乡、关系状态 + 徽章（身高/运动/星座/宗教/政治/烟酒/孩子/家庭计划/约会意图）| 免费过滤（性别/年龄/距离/语言/相似兴趣）+ 高级过滤 | 无分级；但「只能过滤你自己填过的类别」（对偶披露）+ wiggle room 放宽 | `Unknown`（官方仅述基于档案/偏好/活动） | 性别多选、取向独立更新、可寻非二元/所有人 | Dating intentions 徽章 | 性别多样；仍默认陌生+浪漫 |
| 9 | Hinge | 国际 / S+B | 6 照片 + 3 提示词、性别、距离、年龄、族群、宗教、身高、孩子、政治、烟酒毒、教育、家庭计划、关系类型、Vices | 全用户过滤 + 订阅过滤；Flexible vs **Dealbreaker** | 唯一完整的三态权重要么表达（硬性/软性/「prefer not to say」参与过滤） | 官方公开推荐系统输入 + We Met 反馈环 | 性别+取向（取向不可过滤） | Relationship type + Dating intentions | 性别多样；默认陌生+浪漫（含非一夫一妻选项） |
| 10 | CMB | 国际 / S+B | 姓名、生日、性别（不可编辑三件套）、prompts、工作/学历、兴趣 | Suggested（双向偏好）vs Discover（仅我方偏好）| 无 dealbreaker；recent-activity 过滤 | 部分公开：Suggested 采用「双方偏好」，Discover 明确忽略对方偏好 | 性别必填 | Relationship goals | 默认陌生+浪漫 |
| 11 | Grindr | 国际 / LBS+F | 头像、About 225 字、身高、体重、体型、Position、族群、关系状态、Tribes | 网格长过滤列表（在线/年龄/体型/身高/体重/关系状态/Tribes/NSFW/Looking for/健康实践） | 无权重分级；「Popular」为参与度排序（beta） | `Unknown` | 性别弱字段；取向隐含 MSM；Tribes 是身份+审美复合 | Looking For 多选（聊/约/友/网/关系） | 不默认异性、不默认浪漫；仍默认陌生起点 |
| 12 | HER | 国际 / S+B | 性别认同、性身份、代词、Fun Facts（Sex/Kink/Intimacy）、Pride Pins、政治 Pins、生活方式开关 | 高级过滤与自披露对应（reciprocal） | 无分级；premium 过滤需自己先填同类偏好 | `Unknown` | 性别与性身份分离字段；代词高信息量 | 社区/群组承载意图，无独立意图字段 | 面向女同性恋/双性/跨；默认陌生 |
| 13 | Feeld | 国际 / Q+F | 性别(15+)、性取向(20+单选1)、关系类型(15+)、Desires(30+)、兴趣、bio、关联档案（Constellation ≤5）| 过滤器（Desires/位置/距离/年龄）+ Ping | 无分级；shared-desire 高亮作软信号 | `Unknown`（官方述按 Desire 过滤；历史排序按距离为 secondary） | 性别、取向、关系类型三字段分离 | Looking-for 多种（ENM/一夫一妻/Kink/长期/短期）| 不默认异性、不默认浪漫、不默认一夫一妻 |
| 14 | Muzz | 中东穆斯林 / F | 教派、祈祷程度、halal、烟酒、族群、学历、婚姻时间线、已有子女、冰breaker x3 | Deen 过滤（教派/祈祷/烟酒/halal/族群/学历）| **默认 must-have 硬性**（官方自述） | `Unknown`（官方述按过滤+自证匹配；Muzz AI = secondary） | 性别二值；教派身份明文 | Marriage timeline（目标+期限合一）| 默认异性、婚恋、陌生 |
| 15 | SilverSingles | 国际+50 / Q | 性别、希望对方性别、生日、婚况、学历、问卷(O: openness…) 及「partner 的 X 有多重要」| 无免费搜索；每日 3–7 匹配 | 问卷内 importance 分级（唯一完整权重 UI 之一的精简版） | 部分公开（OCEAN + 重要性 + 按位置/生活计划排序） | 性别二值+寻求性别 | 长期陪伴默认；无 casual | 默认陌生+长期；异/同可寻 |
| 16 | OurTime | 美国+50 / F | 发色、瞳色、身高、族群、体型、婚况、子女数、同住子女数、烟酒、Greeting、Topics | 付费高级过滤（children/religion/烟酒/体型等，secondary） | 无官方权重机制 | `Unknown` | 敏感数据条款列明性取向/性别认同/族裔/政治/宗教 | 「想要的 relationship type」advanced(secondary) | 默认异性+陌生+陪伴 |
| 17 | 珍爱网 | 中国 / H+F | 年龄、身高、体重、体型、婚况（未婚/离异/丧偶）、工作地、职业、收入区间、学历、籍贯、户口、房车、星座、民族、血型、爱好、内心独白 | 择偶条件：年龄/身高/婚况/收入下限/学历/地区 | 无分级；婚况可分「未婚/可接受离异」 | 部分公开（算法备案：注册+浏览/点赞/搜索行为画像）；红娘人工叠加 | 性别二值；可父母代注册 | 婚恋导向默认 | 默认异性、陌生、婚恋 |
| 18 | 世纪佳缘 | 中国 / H+F+Q | 年龄、身高、体重、学历(不可改)、收入区间、婚况、居住地、房车、籍贯、户口、血型、民族、学校、公司、职业、烟酒、有无孩子、是否想要孩子、何时结婚、外貌自评、标签≤5、爱情测试 | 择友要求6维（年龄/身高/所在地/学历/居住地/婚况）| 完整度权重中「择友要求」占 15%（官方帮助中心） | 部分公开（亲搜索+线下红娘+「爱情测试」）；权重重叠 | 性别二值；生肖/星座由生日派生不可编辑 | 什么时候结婚字段 | 默认异性、陌生、婚恋 |
| 19 | 探探 | 中国 / S+B | 照片、年龄、星座、距离、所在地、兴趣标签 | 性别/年龄段/距离开关 | 无显式条件表单；完全行为化 | 官方述位置+性别偏好+实时推送；王宇访谈述机器学习迭代（secondary） | 大陆版异性主导；国际版宣称「爱不设限」 | 恋爱交友默认 | 默认陌生+浪漫；大陆异性主导 |
| 20 | Soul | 中国 / Q+B | 灵魂测试（3层）、引力签、生日(→星座/年龄差)、所在地、学业、MBTI(青藤用) | 年龄滑块+星座单选+性别过滤 | 无权重 UI；匹配度黑箱 | 官方算法备案公开（画像+深度学习行为推送） | 弱化性别/照片 | 灵魂社交默认，非婚恋 | 默认陌生+弱浪漫 |
| 21 | 青藤之恋 | 中国 / Q+F | 实名+学历双认证、年龄、身高、学历、学校、职业、工作地、家庭、性格、三观、爱好、择偶要求、MBTI、128生活标签 | 按年龄/学历过滤（付费）+每日 15 精准推荐 | 无分级；MBTI 匹配信号 | 部分公开（每日 15 推荐 + MBTI + 双向喜欢） | 异性婚恋导向；四维认证 | 脱单/严肃婚恋默认 | 默认异性、陌生、婚恋 |

> 说明：21 个条目中，陌陌（#22，§3.22）因几乎零结构化字段，作为反例单独列出；矩阵主表计入 21 项即已超过 10+。学术性 speed-dating 系统（Fisman/Eastwick 数据）在 §5 作为「可观测行为市场」证据使用，不列入产品矩阵。

---

## 3. 逐产品字段与压缩机制（关键摘录 + 来源）

以下仅记录对 primitive 拆解最有价值的机制事实；完整字段清单见 §6 拆解表的「来源产品」列。

### 3.1 OKCupid
核心机制：约 500 道题，每题的答案可以**多选接受项** + **重要性五档**（Irrelevant/A little/Somewhat/Very/**Mandatory**），`Mandatory` 即硬性 dealbreaker；答案可「私有但仍在匹配中计权」，可「标记 irrelevant 卸权」，不可删。过滤器被官方明确描述为软性（「略超出年龄/距离范围仍可能看到」）。身份字段丰富：22 性别、20 取向、50+ 身份标签。产品公开语境承认无法给全部细节（「we can't give it all away just yet」）。`official` 来源：help center 22982200783771、22770910347803、22907669592091、22907566093723。

**压缩视野**：OKCupid 是「declared 权重表达最完整」的产品——重要性档位表明产品自己也认为不同偏好强度不同；且其官方行为实验（2014「We Experiment On Human Beings!」，现 offline，存档于 gwern.net）直接证明**展示的匹配度分数会反推行为**：真实 30% 匹配、伪装 90% 展示的配对，用户更愿意写信、来回 ≥4 条消息、交换联系方式。这证实「宣称的契合分驱动行为 ≠ 计算所得的契合」，是 declared→revealed 的管道证据。

### 3.2 eHarmony
无公开搜索、无用户可声明偏好字段（偏好全部来自 70–80 题问卷）；输出 Personality Profile + 每对 60–140 的 Compatibility Score；「29 Dimensions」为营销遗产（旧页已占位，无法官方核验维度内容）。无偏好 UI 意味着「set preference」的唯一途径是**策略性填问卷**。`official` 来源：eharmony.com/tour/what-is-compatibility-system，eharmony.co.uk/tour/what-is-the-compatibility-quiz。

### 3.3 EliteSingles
Big Five（200+ 题）输出 O/C/E/A/N 五维 + 每日 3–7 推荐；软参数（年龄段宽于所设）+ Have-you-met 会故意带出参数外用户。**压缩点**：偏好与人格特质共用同一输入通道，无独立 dealbreaker 控件。`official`：elitesingles.com/mag/online-dating/personality-test、faq。

### 3.4 Match.com
每属性可设 **Must-Have / Nice-to-Have 两档**（仅二值强度，无第三档「拒绝但不绝对」）；Dating Intention 下拉合并 严肃/figuring-out 等意图；「Highlights」用**共享档案字段的同质**（年龄/职业/地点/学历/爱好）当契合 proxy。`official`：help 12625991507867、6241672918683、6241693282331、intl2.match.com/help。

### 3.5 POF
Chemistry Predictor 五因素（self-confidence、family orientation、self-control、social dependency/openness、easygoingness，`secondary` 经由 PinkNews 等）**显示在公开档案上**——把「性格契合分」双重应用为可炫耀/可鄙视的吸引力数字。`official`：help.pof.com、pof.com/hc/en-us/articles/360050341111（gender visibility）。

### 3.6 Zoosk
唯一跳过问卷的产品：SmartPick 纯行为学习（Pass/Match 质量都要记、搜索过滤行为、Carousel 上档案选择），且官方文档**同时运行两套偏好语义**——搜索过滤服从 declared，「Carousel 是介绍给你过滤条件之外的人」。`official`：support.zoosk.com 51223998344340、51223835191956、51224010205972；blog「From Swipe to Soulmate」。

### 3.7 Tinder
官方明确匹配 = like/nope 聚合，且**明确声明不追踪社会地位/宗教/族群**（这本身就是一种反压缩声明：把敏感性身份字段排除在排序外）。无 dealbreaker 分级；唯一的排序开关是「同取向优先」。身份：Beyond Binary（把 genderfluid/GNC/intersex 压进一个主桶）。`official`：help.tinder.com 115003339043、7606685697037、15668360470669。

### 3.8 Bumble
**reciprocal 过滤律**是最大特色：只能过滤你已自填的类别，把「筛选」变成「互相披露」，并加 wiggle room 自动放宽年龄/距离。—孩字段「有还是想要孩子」合并在一起（官方如此归类）。`official`：support.bumble.com、bumble.com/the-buzz（filters）。

### 3.9 Hinge
**dealbreaker 机制最完整**：每个偏好可设 Flexible / Dealbreaker；「Prefer not to say」会把你从他人 dealbreaker 筛选中排除（缺省也参与计权）。官方公开推荐系统输入：兼容设置、dealbreakers、活动、档案信息 + **他人偏好（双向互惠）** + 你的历史行为 + We Met 事后反馈环，且明示「快速跳过 = 系统认为你不喜欢这类人」。「children」单字段同时驱动 has-children 与 family-plans 两个过滤器；Vices 把烟/酒/毒四行为并作一类。`official`：help.hinge.co 360011063294、38014282744595；hinge.co/how-we-connect-daters。

### 3.10 CMB
两套表面 = 两套压缩语义：Suggested 服从「双方偏好 + 我方偏好」（互惠计算），Discover 明确忽略对方偏好；「recent activity」把**在场/活跃度**做进可搜索维度。`official`：coffeemeetsbagel zendesk 31212228097043、33782396591123。

### 3.11 Grindr
Position（Top/Vers/Bottom/Side，Side 为后补的非插入项）是**性行为角色单字段压缩**；Tribes（Bear/Daddy/Twink/Geek…）同时承担自我认同、体型、亚文化审美三重语义，且另设「Tribes I'm into」镜像偏好；Looking For 把聊/约/友/网/关系并进多选；Meet At 把地点偏好与容纳性压进 3 选项。`official`：help.grindr.com 4402336949523、12155443240851。

### 3.12 HER
性身份/性别/亲密偏好**三个字段分离**（面向性向光谱）；「prefer to self-describe」保留可过滤性；亲密偏好同时是自描述、过滤条件与自我展露——DESIRE = published profile data。`official`：support.weareher.com 36994637903515、15464152409748；weareher.com blog。

### 3.13 Feeld
性别(15+)、性取向(20+单选一)、关系类型(15+)、Desires(30+)、关联档案(Constellation≤5) **四字段分离**——是目前发现的最「不把身份/吸引/结构揉一起」的产品；但关系类型把 status(Dating/Married)、结构(ENM/Poly)、权力角色(Sub)、目标(Friends 等) 压成一字段；Desire 同时是自述、筛选、信号标记（shared desire 高亮）。`official`：support.feeld.co 18822038569884；feeld.co/ask-feeld。

### 3.14 Muzz
**Deen 过滤默认 must-have**（官方自述：设了族群过滤就只能看到匹配族群），其他字段用 yes/no/definitely-not；Marriage timeline 把「目标 + 期限」压进单选；教派字段把教派身份与严格度合并；Wali/父母参与是把**第三方**引入两方数据模型。`official`：muzz.com/us/en/help/muzz-101（ethnicity filter）、App Store listing。

### 3.15 SilverSingles / 3.16 OurTime
SilverSingles 是「importance 分级最朴素」的产品（partner 的 X 对你有何重要 → 权重向量）+ OCEAN 人格；OurTime 保留发色/瞳色字段（外观压缩的极端 atavism）、子女数/同住子女数分列（家庭结构离散化），并明示性取向/族裔/政治/宗教为「敏感数据可被用于增强推荐」。`official`：silversingles.com/mag/about-silver/our-site/profile & faq；help.ourtime.com 6619430860827、33951900727067。

### 3.17–3.19 珍爱网 / 世纪佳缘 / 百合网
中国婚恋三件套共享同一字段范式：**可声明择偶条件**（年龄/身高/婚况/收入下限/学历/地区），百合网明示「不符合择偶条件会被拦截发消息，付费可突破」——把标准刚性化做成商业机制。世纪佳缘从生日**自动派生生肖/星座**且不可改（年龄→代理标签的直接压缩）。百合把父母情况（排行/父母工作/父母经济/父母医保）、是否愿与对方父母同住、家务分工、厨艺全塞进个人档案；官方宣称「45 个婚恋特征 / 23 心理维度的心理匹配系统」。`official`：zhenai.com/help、jiayuan.com/helpcenter、baihe.com help（cat=list）。

### 3.20 探探 / 陌陌 / Soul / 青藤之恋
探探把显式择偶条件整体清空为滑动行为（「择偶标准=你说什么」完全行为化），星座+年龄+距离成卡片三标签，另有强制多轮文字、隐藏照片的「闪聊」；陌陌（反例）几乎零结构化关系字段，唯一显式筛选 = 地理位置；Soul 用「灵魂测试 + 引力签」替代门当户对整类条件，星座是它唯一可精细筛选的 A 类代理，匹配度以黑箱数字直接展示；青藤之恋最「高密度压缩」：128 个生活细节标签（吃辣/叠被子/写日记/记账）、MBTI 匹配、「独生女」「体制内」只能进自由文本择偶标准。`official`：tantanapp.com、immomo.com、soulapp.cn 备案页、qingtenglove.com。

---

## 4. 产品如何压缩：六类机制模板

对 §3 全部样本归纳，产品的「字段压缩」可拆成 6 种可复用模板。这一模板本身就是可复用交付物（不受任一产品字段变化影响）：

**M1 身份与偏好共用一格**（identity=preference）：一个字段同时是自描述、过滤条件和匹配信号。例：Grindr Tribes（自认同 vs 偏好镜像）；Bumble reciprocal「只能过滤已填类别」；HER「Fun Facts」亲密偏好 = 展露；Feeld Desire 三合一。**根本原因**：枚举字段省成本，且「偏好自述」反过来是最廉价的行为采集。

**M2 吸引方向 / 浪漫意图 / 关系目标 / 身份合并**：单字段把 sexual attraction、romantic intent、relationship goal、identity、partner-sex preference 混装。例：eHarmony「I am woman/man/nonbinary」注册 token（身份+隐藏吸引方向）；Match 的 Dating Intention 单下拉合并意图光谱；探探/Soul 完全没有 separating fields。此类是 #2 `5565170990` 点名要求记录的 **UI/proxy compression**，不是 primitive。见 §8.1 审计。

**M3 历史与当前状态合并**：一个枚举承载随时间演化的两类东西。例：婚况字段（未婚/离异/丧偶 = 法律状态 + 历史 + 当前可得性）；「婚姻状况」把「从未结婚」与「现处单身」混同；微信使用「离异」在婚恋语境下被当「有历史包袱」。**拆分规则**：current relationship availability ≠ relationship history ≠ obligations。

**M4 资源金字塔**：单字段承载存量/流量/预期/让渡四层。例：收入字段（当前流量）、房产（存量+稳定）、上进心（预期的 proxy）、肯花钱（让渡意愿）。产品把收入当一等筛选，把「肯花钱」留给自由文本或行为信号。**重复计数风险**：若 income+assets+知 spend 各自成参则三层被叠计。

**M5 显式偏好分级 vs 隐式行为**：所有产品最终都落在同一条光谱上——纯 declared（珍爱/佳缘/百合/Match）→ declared+权重（OKCupid/Hinge/SilverSingles）→ 混合（Tinder/Bumble/Zoosk）→ 纯 revealed（探探/陌陌）。权重控制越强，用户能表达的真实意图越细，但**表达本身就变成一种自我展露**（M1 的回环）。

**M6 派生标签冒充独立字段**：从已有原始字段派生的标签被当作新特征。例：星座/生肖/属相 = 生日派生（世纪佳缘/探探/Soul）；匹配度黑箱 = 产品自己算的二手分数（Soul 恋爱铃、POF Chemistry Predictor 上公表）；MBTI = 自报问卷高分压缩。派生标签在模型中是**派生判断（derived judgment）**，不得与底层状态并列。

---

## 5. Declared vs Revealed Preference：学术证据与产品管道

### 5.1 学术证据（`established`）

| 证据 | 内容 | 层级 |
|---|---|---|
| Buss (1989)，37 文化 N≈10,047 | 自报偏好：女性重赚钱能力/上进心，男性重年轻/外貌；贞洁跨文化变异最大；自报年龄偏好与实际婚配年龄差 r≈.68–.71（唯一的 revealed 佐证）。纯 declared。 | established（自报层）|
| Fisman, Iyengar, Kamenica & Simonson (2006, QJE) | speed-dating 行为决策：男性对「女更聪明/更上进」反而降低 yes；女性重智力/收入/同类族，男性重外貌；女性随候选池变大更挑剔。**revealed 行为与「性别差」自报方向在多个维度不一致**。 | established |
| Eastwick & Finkel (2008, JPSP)；Eastwick et al. (2014, Psych Bull 元分析 k=97) | 自报偏好只能预测「纸面/照片/完整履历」评估；在真实互动中，事件前填报的理想型偏好无法预测心动；外貌吸引力在真实互动中预测浪漫评价 r≈.40、赚钱潜力 r≈.10，两性相同。 | established |
| Hitsch, Hortaçsu & Ariely (2010, QME/AER) | 大型婚恋平台全量日志（首次发信=revealed）：强烈同族偏好但自报只一半吻合；女性重收入、男性重外貌；体重自报男高报身高女低报体重 6–20 磅；行为驱动的同配可解释婚恋市场大部分聚合模式。 | established |
| Finkel et al. (2012, PSPI) | 系统审查后发现「没有可信证据支持算法匹配网站『算法有效』主张」；自报契合对长期走向预测力弱。 | established（元综述结论）|
| Joel et al. (2020, PNAS)，43 数据集 11,196 对 2,413 变量 | 基线变量能预测「当前满意度」最多 ~45% 方差，但预测「关系会不会变好变坏」<5%——人格/个体差问卷是关系走向的糟糕原料。 | established |

### 5.2 产品管道：产品在哪一层接住偏好

产品实际上各自「采样」了偏好谱系的一段：婚恋三件套/Match/SilverSingles 接住**说得出口的理想型**（declared，且全部是纸面评估语境）；OKCupid 接住 declared+权重并能借实验证明分数反推行为；Tinder/探探/陌陌/Zoosk/Soul 接住**做出来的选择**（revealed 行为信号）；Hinge 唯一自带正字 We Met 事后反馈（约会后的再评估信号）。同一用户的 declared 与 revealed 系统性不一致（尤其种族、收入、认真度），已被 Hitsch 数据与 Eastwick 实验直接证实。

**LHRM 含义（`hypothesis` + 结论）**：模型把「偏好」建为 **主体信念**（S 层 belief，可随信息更新），与 **行为选择**（二维：兴趣揭示 vs 适配真相）分开；declared 字段落入 S-belief，like/skip/message/meet 落入 revealed-interest，两者都不等于关系适配。Missing/Unknown 一律保留为 Unknown，不得按平台惯例抹成中性默认值（AGENTS：unknown 显式化）。

**产品→模型的映射建议**（供 join gate 参考，非 canonical）：
- 归档字段（身高/婚况/学历）→ S/O 层 observation（带 verified flag）。
- 重要性档位（OKCupid/Match/Hinge）→ belief-importance 结构，可表达为区间而非单点。
- 滑动/搜索行为 → revealed 行为事件，进入 history，供 interest/persistence 推断，不直接入静态 preference。
- 匹配度数字（任何产品的）→ derived judgment of unknown quality，只当 observation 记，禁止当真值校准项。

---

## 6. 字段→构念反向工程：144 条 Proxy Decomposition

**类型码**（dispatch 要求的区分）：
- `O` direct observable —— 可直接观测/可验证的状态
- `L` latent construct —— 无法直接观测、需多指标测量的潜在构念
- `PR` preference region —— 偏好区域/阈值（主体信念）
- `DB` dealbreaker —— 硬性不可协商否决
- `RC` role-conditioned constraint —— 因关系角色/制度/家庭身份而生的约束，可在不同 ρ 下开关
- `RP` revealed preference —— 由行为揭示的兴趣/偏好
- `DJ` derived judgment —— 派生判断（对底层状态的复合评价/二手分数）
- `C` compression —— 单一产品字段把多个构念合并装（解开才是 primitive 的材料）

每个拆解给出「来源产品/信号」与「跨语境稳定性备注」。**关键测试**（§7）逐条检验「same-sex / opposite-sex / kin / non-kin / stranger / established-relationship」下语义是否稳定。

### 簇 A —— 人口学/物理外观（19）

| 号 | 表面词 | 拆解基础构念 | 类型 | 备注/反例 |
|---|---|---|---|---|
| A01 | 年龄 | 时间索引(t)；人生阶段/世代；可生育窗口（context）；无「魅力」本身 | O(索引) | 年龄只是索引：45 岁亲子 vs 45 岁丁克、同龄同性伴侣，语义完全不同 |
| A02 | 出生日期 DOB | 派生关键（→年龄/星座/属相）；契约字段 | O | 与 A16/A17 重复计数风险 |
| A03 | 身高 | 大体不可变物理属性；外观印象输入；身高偏好 PR | O | 同性/异性语境均适用；对「纸面匹配」贡献稳定但对现实契合低 |
| A04 | 体重 | 可变形体状态；健康信号；自报系统性低报（Hitsch） | O/RP | 跨语境稳定；但进入匹配时被当作偏好信号 |
| A05 | 体型 | 身体组成 + 外观标记 | L/O | Kin 语境下为健康照护输入，浪漫语境下为吸引输入 → 语义漂移，需按 ρ 切 |
| A06 | 发色/瞳色 | 外观物理属性（OurTime 字段） | O | 纯 decoration，模型价值近零（保留为 observation） |
| A07 | 脸型/魅力部位自评 | 外观自评（佳缘「神秘部位」） | DJ | 自报告知度低；UI-only |
| A08 | 肤色/种族 | 社会身份/群体成员；结构性环境(E)；偏好（社会敏感，revealed>declared） | 身份/RP | 跨语境稳定（亲属=背景），但作为偏好时 social-desirability bias 高 |
| A09 | 所在地 | 地理可得性/接触机会结构(E) | O/E | 对「陌生起点」是机会层；对已建立关系是共同环境层 |
| A10 | 距离 | 双人空间距离；互动成本(E) | O/E | 跨语境稳定（亲属/朋友/陌生人同解释） |
| A11 | 籍贯 | 文化群体认同 + 迁移史 | 身份 | 中国语境强负载；海外产品无此字段 → 制度性，非 universal |
| A12 | 户口 | 制度性权利/资源约束(E) | RC | 户籍制度特有，角色条件化 |
| A13 | 年龄区间偏好 | 对 A01 的偏好阈值 | PR | declared；Buss 显示其部分见于实际行为 |
| A14 | 身高偏好 | 对 A03 的阈值 | PR | 纯纸面偏好，Eastwick 显示 live 中不预测 |
| A15 | 体重/体型偏好 | 对 A04/A05 的阈值 | PR | 同上 |
| A16 | 星座 | 生日派生标签 | DJ | UI-only；删（避免与 DOB 双重计数） |
| A17 | 生肖 | 生日派生标签 | DJ | 世纪佳缘不可改；UI-only |
| A18 | 血型 | 民俗性格标签 | DJ | UI-only |
| A19 | 民族 | 群体身份 + 文化惯例 + 制度 | 身份/RC | 中国实名制下为身份属性；跨语境稳定 |

### 簇 B —— 资源/地位（16）

| 号 | 表面词 | 拆解基础构念 | 类型 | 备注/反例 |
|---|---|---|---|---|
| B01 | 收入 | 资源流量（当前）+ 生活水平 + 稳定性信号 | O(declared) | 未验证；语义在「当前收入」与「家庭共同生活资源」之间漂移 |
| B02 | 月薪区间 | 同上，粗粒度 | O | 佳缘/珍爱把门槛用下限表达 |
| B03 | 房产 | 资源存量 + 居住稳定 + 家庭资产信号 +（中国）婚姻制度刚性要求 | O/RC | 「有没有房」在中国语境 = 制度性婚配字条件 |
| B04 | 车 | 资源存量 + 流动性 | O | 语义弱、社会符号性强 |
| B05 | 职业 | 社会地位 + 时间模式（工作性质）+ 收入相关 | O | 需拆「地位/时间/收入」三通道 |
| B06 | 公司/行业 | 地位 + 稳定性 + 同侪认同 | O/DJ | 「体制内」= 稳定性+声望复合（青藤） |
| B07 | 学历 | 人力资本 + 阶层学徒 + 认知能力（弱proxy）+ 社会化程度 | O/L 复合 | 一兆种含义合一（见 §9 冗余组 #2） |
| B08 | 学校 | 教育质量 + 群体认同 + 阶层 | O | 「学院」≠「学历」 |
| B09 | 毕业院校/专业 | 同上 + 职业路径 | O | — |
| B10 | 上进心 | 未来资源预期 + 动机特质 | L | 吸引函数输入；自报不可信（Eastwick） |
| B11 | 肯花钱 | 资源让渡意愿（行为）≠资源量 | RP/DJ | App 无字段；只能从礼物/消费行为 RP 化。「肯花钱」对贫富语义相同但信号强度不同 → 需分解 |
| B12 | 家庭背景财富 | 家庭资源 + 赡养义务（父母医保/经济） | O/E | 百合字段；承担 lattice 但不可当个人资源 |
| B13 | 门当户对 | 家庭层级边界 + 家庭预期一致 | DJ/RC/E | 「家庭」作为第三参与者（§10 J2） |
| B14 | 独生女/独生子 | 赡养时间约束 + 家庭结构 + 习俗 | RC | 青藤 free-text 择偶例；跨语境规则随 ρ 变化 |
| B15 | 体制内工作 | 职业稳定 + 声望 +（中国）福利资源 | O/RC | 制度性偏好，非 universal |
| B16 | 未来收入预期 | 不可直测；上进心/学历/行业为 proxy | L | 与 B10 重叠，防三重计数 |

### 簇 C —— 婚姻/子女/家庭结构（14）

| 号 | 表面词 | 拆解基础构念 | 类型 | 备注/反例 |
|---|---|---|---|---|
| C01 | 婚姻状况 | 法律身份 + 当前关系状态 + 历史（+可得性） | C | 三概念压一字段：未婚≠现单身；离异=历史；已婚=不可得（部分语境） |
| C02 | 未婚/离异/丧偶 | 法律-历史状态 | O/RC | 与「当前是否可得」解耦测试：离异但已订婚 = RC+RP 冲突 |
| C03 | 可接受离异 | 对历史/状态的接受度 | PR | 佳缘只能隐含表达 |
| C04 | 有无子女 | 父职身份 + 照护义务 + 可得性 | O/RC | 与 A05 一样跨 ρ 语义漂移（爱侣 vs 亲子照护） |
| C05 | 想要孩子 | 生育意向（declared belief） | PR/L | 「想要孩子」≠「有能力生」≠「接受对方带娃」（C04） |
| C06 | 孩子同住 | 家庭结构/日常负载 | O | OurTime 单列「同住子女数」——对偶披露律 |
| C07 | 孩子数量 | 负担强度 | O | — |
| C08 | 家庭计划 | 生育意向 + 关系目标复合 | PR/C | Hinge/Bumble 都有 |
| C09 | 生育窗口/能力 | 生物状态（context） | O/L | 不把「年龄」直接射成 fertility proxy；窗口由医学事实决定；Unknown 化生理细节 |
| C10 | 愿与对方父母同住 | 角色条件化约束 + 家庭制度 | RC | 百合问题；ρ=共同育儿/赡养时才激活 |
| C11 | 婚后住在哪 | 地理制度 | RC/E | — |
| C12 | 赡养义务 | 时间/资源让渡（对非配偶方） | RC | 独生→压抑的赡养需求（B14） |
| C13 | 何时结婚 | 目标 + 期限（urgency）合并 | PR/DJ/C | Muzz 时间线；合并不当两概念 |
| C14 | 家务分工 | 角色预期 + 性别规范 | RC | 百合「家务分工/厨艺」是 ρ-role 下的期望，非人格 |

### 簇 D —— 身份/文化/价值（18）

| 号 | 表面词 | 拆解基础构念 | 类型 | 备注/反例 |
|---|---|---|---|---|
| D01 | 宗教信仰 | 团体身份 + 价值观 + 行为规则复合 | 身份/L/C | 身份 vs 行为强度必须分离（见 D02/D03） |
| D02 | 教派 | 教派身份 + 严格度合并（Muzz） | 身份/RC | Muzz 单选把归属与强度揉死 |
| D03 | 宗教实践程度 | 行为强度信号（祈祷/清真） | RP/O | Muzz 有独立「prayer level」——正面反例 |
| D04 | 清真/禁忌 | 行为约束 + 文化规则 | RC | 跨语境稳定但仅在有规范语境激活 |
| D05 | 政治观点 | 意识形态光谱 + 社会身份 | L/身份 | 单一光谱过粗；见 D06 |
| D06 | 政策立场 pins | 价值维度细分（HER Political Pins） | L | 优于单轴；仍为自报 |
| D07 | 核心价值观 | 价值系统对齐（Match Core Values） | L | 双重计数风险：与 D05/D08/D10 重叠 |
| D08 | 顾家 | 角色偏好 + 时间分配倾向 | DJ/L | 「顾家」= 时间给家庭 + 传统角色，需拆两轴 |
| D09 | 孝顺 | 家庭义务 + 价值 | L/RC | ρ-依赖（对父母 vs 对配偶） |
| D10 | 传统/保守 | 社会保守性（对变革偏好） | L | 跨文化不稳定（中国 vs 西欧含义不同） |
| D11 | 门当户对 | 见 B13（cross-ref） | — | 同一构念两次出现即重复计 |
| D12 | 语言 | 沟通可得性 + 文化圈 | O | — |
| D13 | 国籍 | 法律地位 + 资源 | O | — |
| D14 | 三观 | 价值观 umbrella（青藤） | L umbrella | 必须拆分才能用 |
| D15 | 性格/人格 | 大五/神经质/外向等 | L | 自报人格对走向预测力弱（Joel 2020） |
| D16 | 生活方式 | 行为簇（作息/兴趣/预算） | L/DJ | 拆到 E 簇与 B 簇 |
| D17 | 兴趣标签 | 行为、群体认同、自我展露 | O/DJ | 行为上倾向花时间的地方；标签本身低可靠 |
| D18 | 幽默感 | 互动特质（人际间） | L/DJ | app 只能自报；真幽默需 D 层互动才可测 |

### 簇 E —— 行为/习惯/健康（12）

| 号 | 表面词 | 拆解基础构念 | 类型 | 备注/反例 |
|---|---|---|---|---|
| E01 | 抽烟 | 健康风险状态 + 生活习惯兼容 | O | 天天抽 vs 年会抽：产品通常只给二态 |
| E02 | 喝酒 | 同上 + 社交行为 | O | 「喝酒的社交性」vs「酗酒」未分离 |
| E03 | 毒品/大麻 | 合法状态 + 风险 + 生活方式 | O/RC | 法律语境强依赖 |
| E04 | 饮食 | 生活习惯 + 健康（素食/清真） | O | 与 D04 重叠风险 |
| E05 | 运动程度 | 健康 + 时间模式 + 价值 | O/L | — |
| E06 | 作息 | 生活节奏兼容（熬夜发现） | O | 强对偶兼容面，产品少捕获 |
| E07 | 厨艺/家务 | 角色能力 + 分工偏好 | RC | 见 C14 |
| E08 | 健康状态 | 未来负担 + 吸引力 | O/L | App 基本无此字段——是盲区 |
| E09 | 生活方式健康度 | 派生综合 | DJ | — |
| E10 | 整洁/生活习惯细节 | 日常兼容 | O | 青藤 128 标签示例（叠被子） |
| E11 | 吃辣/饮食细节 | 生活兼容（青藤） | O | 标签化到百位=过度拆分信号 |
| E12 | 宠物 | 生活结构 + 责任 + 情感投入 | O | 宠物=「会照护」的行为 proxy 之一 |

### 簇 F —— 性格特质/他人评价（15）

| 号 | 表面词 | 拆解基础构念 | 类型 | 备注/反例 |
|---|---|---|---|---|
| F01 | 成熟 | 情绪调节 + 决策一致性 | DJ/L | 跨语境稳定但自报极不可信 |
| F02 | 责任心 | 行为一致性 / 承诺可靠性 | L/DJ | 需行为验证；「准时/说到做到」行为代理 |
| F03 | 情绪价值 | 互动回报能力（对特定 ρ） | DJ/D | 只能在互动后测（D 层）；app 无字段=被自由文本代替 |
| F04 | 陪伴 | 时间在旁 + 情感支持 | PR/RP | 需求方为 PR，提供方为行为 RP；两者不可同参 |
| F05 | 温柔/体贴 | 行为 + 气质 | L/DJ | — |
| F06 | 好脾气 | 冲突调节潜在界 | L | 「不发火」≠「不压抑」，负面反例 |
| F07 | 上进/勤奋 | 动机特质 | L | 与 B10 重复 |
| F08 | 聪明/才智 | 认知能力（latent） | L | 学历/谈吐为 proxy，无法自报测；「才智」偏好是 PR |
| F09 | 靠谱 | 可预测性 | L/DJ | — |
| F10 | 真诚 | 诚实/可信（行为一致性） | L | declared「真诚」零信息；需 revealed 一致性验证 |
| F11 | 会聊 | 互动节奏 | L/D | D 层属性 |
| F12 | 颜值/好看 | 外观吸引力复合 | DJ/L | Fisman：真实互动中预测浪漫评价 r≈.40 |
| F13 | 气场/魅力 | 社交能量 | L/DJ | — |
| F14 | 会照顾人 | 照护倾向 + 行为 | L/DJ/RC | 亲属语境给照护；浪漫语境给情感支持 → ρ-漂移 |
| F15 | 顾家 | 见 D08（cross-ref） | — | 防重 |

### 簇 G —— 吸引/性/亲密（14）

| 号 | 表面词 | 拆解基础构念 | 类型 | 备注/反例 |
|---|---|---|---|---|
| G01 | 性取向 | 方向构念（identity / attraction / behavior 三者可不同） | 身份/L | #2 `5565170990`：不可混同三概念 |
| G02 | 浪漫取向 | 与性取向可分离的浪漫吸引方向 | L | 产品几乎不分离（Feeld 部分）；面向模型需显式 |
| G03 | 性别认同 | 身份 | 身份 | — |
| G04 | 生理性别 | 生物属性（仅 as attribute，不作入口假设） | O | #2 ruling：性别是属性不是入口 |
| G05 | 择偶性别偏好 | 对 partner-sex 的偏好区域 | PR | 与 G01 混装的机率最高（见 §8.1 审计） |
| G06 | 性行为偏好 | acts 偏好簇 | PR | HER/Feeld 有；强 ρ-依赖 |
| G07 | 性角色 position | 行为偏好压缩字段 | PR/O | Grindr Top/Vers/Bottom/Side；Side 补丁证明 enum 不够 |
| G08 | 性欲强度 | 欲望强度构念 | L | 强度轴上独立于方向（G01） |
| G09 | 无性光谱 | 方向×强度×行为联合 | L/C | HER 提供 repulsed/neutral/positive——单轴也不够 |
| G10 | 浪漫行为意图 | 想不想恋爱 | PR | ≠ 性取向 ≠ 关系目标 |
| G11 | 身体接触态度 | 亲密度偏好 | PR | — |
| G12 | 亲密需求 | 依恋/连接需要强度 | L | — |
| G13 | 性化学反应/吸引 | D 层涌现，互动后才可测 | D | App 无法捕获（照片可 proxy 视觉吸引，化学由 F12/DJ） |
| G14 | 视觉吸引力 | 外观综合印象（照片为信号） | O/DJ | 最强初始过滤器（Fisman；Eastwick meta r≈.40） |

### 簇 H —— 关系目标/动机/情境（14）

| 号 | 表面词 | 拆解基础构念 | 类型 | 备注/反例 |
|---|---|---|---|---|
| H01 | 关系目标 | 长期/短期/婚姻/朋友… | PR | Tinder/Hinge/Bumble/Match 均有独立字段 |
| H02 | 约会意图 | 同上细分 + urgency | PR | — |
| H03 | 婚姻意向 | 目标 + 法律制度 | PR/DJ | 与 H04 合并成时间线即压缩 |
| H04 | 婚姻时间表 | 目标 + deadline | PR/C | Muzz 主例 |
| H05 | 关系结构 | 一夫一妻/ENM/开放 | PR/RC | Feeld/Match【关系类型】主例 |
| H06 | 初见目的 | chat/dates/friends/networking/hookups | PR | Grindr 多选；同屏多目标合法 |
| H07 | 寻求关系类型 | 情侣/朋友/聊天 | PR | — |
| H08 | 已有关系关联 | 现伴侣/第三人知情 | RC/D | Feeld Constellation；不只二人世界 |
| H09 | 当前可得性 | 关系状态 + 资源 | O/RC | 「有对象但 open」≠「不可得」 |
| H10 | 活跃度/在线 | present-behavior 信号 | RP | CMB recent-activity、Grindr online |
| H11 | 已聊对象管理 | D 层竞争结构 | D | — |
| H12 | 第三者知情度 | 制度/伦理约束 | RC/D | ENM 语境核心 |
| H13 | 开放关系状态 | 结构约束 | RC | — |
| H14 | 首次接触形式偏好 | 见面 vs 文本 | PR | — |

### 簇 I —— 行为信号/资源让渡（12）

| 号 | 表面词 | 拆解基础构念 | 类型 | 备注/反例 |
|---|---|---|---|---|
| I01 | 响应速度 | 时间让渡（注意力分配） | RP | 强兴趣信号；且与 E06 作息可交互 |
| I02 | 陪伴时间 | 可分配时间的容量 | O/RP | 需求 vs 供给拆开 |
| I03 | 线上活跃度 | 在场行为 | RP | 高频在线的意义依 intent 变化（找乐子 vs 找对象） |
| I04 | 见面频率 | 双向让渡 | RP/D | — |
| I05 | 礼物/仪式 | 资源让渡 + 仪式价值 | RP | — |
| I06 | 主动发消息 | 兴趣揭示 | RP | Hitsch 用首信=revealed |
| I07 | 回访 | 兴趣持续 | RP | OKCupid 用回访/来往次数 |
| I08 | 消息长度/质量 | 兴趣浓度 + 沟通质量 | RP/DJ | 单一信号噪声大 |
| I09 | 快速跳过 | 反感信号 | RP | Hinge 明示「快速跳过=不喜欢这类人」 |
| I10 | We Met/事后反馈 | 约会后再评估 | RP/D | Hinge；少数产品有真正的事后校准 |
| I11 | 喜欢存量 | 网络结构溢出 | D/E | — |
| I12 | 回复率 | 兴趣基线 | RP | — |

### 簇 J —— 第三方/环境/制度（10）

| 号 | 表面词 | 拆解基础构念 | 类型 | 备注/反例 |
|---|---|---|---|---|
| J01 | 父母代注册 | 第三方发起方（参与者身份错位） | E/RC | 珍爱父母模式 |
| J02 | Wali/家长参与 | 第三方在场/许可制度 | E/RC | Muzz Wali——两方模型至少三方数据 |
| J03 | 父母经济/医保 | 家庭负担结构 | E | 百合家庭字段 |
| J04 | 排行/兄弟姐妹 | 家庭结构 + 习俗 | E | 独生 vs 多子赡养负载 |
| J05 | 城市层级 | 阶层环境 + 机会结构 | E | — |
| J06 | 婚介服务制度 | GB/T 规范等制度约束 | E | 中国婚介标准化影响字段形态 |
| J07 | 市场结构 | 供需比/基数 | E | 「女性更挑剔随候选池增大」（Fisman）是 E 层效应 |
| J08 | 社会支持/反对 | 网络 approval | E/D | — |
| J09 | 共同朋友 | 网络重叠 | D/E | Hinge「社交图」隐式使用 |
| J10 | 迁移成本 | 地理-制度成本 | E | 与 A10 距离交互 |

> 簇 A–J 合计 144 条。交叉引用两次者（D11↔B13、F07↔B10、F15↔D08）与派生标签（A16/A17/A18/B07-F08 等）已在 §9 冗余表中显式挂账，避免重复计数时将同构念当两个参数。

---

## 7. assumption_stress_test：跨语境语义稳定性

**方法**：对每个候选构念做六个语境测试——same-sex / opposite-sex / kin / non-kin / stranger / established-relationship。#2 `5565170990` 要求「对所有候选参数做 cross-sex / same-sex / kin / non-kin / stranger / established-relationship 反例测试」。下表列出受测构念及结论；`稳定`=跨语境语义不漂移；`ρ-漂移`=同一状态在不同关系任务下的含义改变；`崩溃`=离开发明它的产品语境即失去意义。

| 构念（簇X.号） | opposite | same | kin | non-kin | stranger | established | 结论 |
|---|---|---|---|---|---|---|---|
| 年龄 A01 | 稳定 | 稳定 | 稳定（辈分差） | 稳定 | 稳定 | 稳定 | 索引变量，始终稳定 |
| 身高 A03 | 稳定 | 稳定 | 稳定 | 稳定 | 稳定 | 稳定 | 物理属性稳定 |
| 体型 A05 | 稳定 | 稳定 | ρ→照护输入 | 稳定 | 稳定 | 稳定 | ρ-漂移 |
| 肤色/族裔 A08 | 稳定 | 稳定 | 背景稳定 | 稳定 | 稳定 | 稳定 | 但作偏好时 biased |
| 距离 A10 | 稳定 | 稳定 | 稳定 | 稳定 | 稳定 | 稳定（共同居住则更高频） | 稳定 |
| 籍贯 A11 | 稳定 | 稳定 | 稳定（宗族语境） | 稳定 | 稳定 | 稳定 | 文化属性，universal 性弱 |
| 收入 B01 | 稳定 | 稳定 | ρ→赡养/共享预算 | 稳定 | 稳定 | 稳定 | 但「收入=共同生活资源」仅在 established 时成立 |
| 学历 B07 | 稳定 | 稳定 | 稳定 | 稳定 | 稳定 | 稳定 | 但 meaning 依文化制度变（海外 vs 中国） |
| 上进心 B10 | 稳定 | 稳定 | ρ→事业期待 | 稳定 | 稳定 | 稳定 | 语义相对稳定；测量（自报）不可靠 |
| 婚姻状况 C01 | **崩溃**：未定义于 kin/established 内层 | 崩溃于 poly/enm 语境 | 崩溃 | 稳定 | 稳定 | 崩溃 | **必须解耦**（当前可得 / 历史 / 义务） |
| 有无子女 C04 | 稳定 | 稳定 | 稳定（子女名词义同） | 稳定 | 稳定 | 稳定 | 但 obligation 语义依 ρ 变 |
| 想要孩子 C05 | 稳定 | 稳定 | 崩溃：kin 中不适用 | 稳定 | 稳定 | 稳定 | 仅在有生育计划的 ρ 下有意义 |
| 宗教严格度 D03 | 稳定 | 稳定 | 稳定 | 稳定 | 稳定 | 稳定 | 行为强度稳定；身份则另有 |
| 「顾家」D08 | ρ-漂移 | ρ-漂移 | 崩溃：对象不同（子/父母） | 稳定 | 稳定 | 稳定 | 需拆「时间给家」与「传统角色」 |
| 幽默感 D18 | 明显 ρ-漂移 | 明显 ρ-漂移 | ρ-漂移 | 稳定 | 稳定 | 稳定 | 「接梗」是 D 层涌现 |
| 性取向 G01 | 稳定 | 稳定 | 崩溃：kin 中性取向存在但关系边界不同 | 稳定 | 稳定 | 稳定 | 方向构念稳定；行为/身份必须分开（#2） |
| 生理性别 G04 | 稳定 | 稳定 | 稳定 | 稳定 | 稳定 | 稳定 | 仅属性，不作匹配入口 |
| 性角色 G07 | 稳定 | 稳定 | ρ-漂移/崩溃：kin 不适用 | 稳定 | 稳定 | 稳定 | **崩溃情境说明它是 PR/RC，不是 primitive** |
| 关系结构 H05 | 稳定 | 稳定 | 崩溃：kin 无此概念 | 稳定 | 稳定 | 稳定 | 仅浪漫/婚恋 ρ 下激活 |
| 响应速度 I01 | 稳定 | 稳定 | ρ→照护响应 | 稳定 | 稳定 | 稳定 | 行为信号跨语境稳定，语义依 ρ 调 |
| 陪伴 F04/I02 | 稳定 | 稳定 | 稳定 | 稳定 | 稳定 | 稳定 | 需求/供给两分即可稳定 |
| 星座 A16 | 崩溃：无跨语境意义 | 崩溃 | 崩溃 | 崩溃 | 崩溃 | 崩溃 | 派生标签，全语境崩溃 → UI-only |
| 匹配度数字（任何产品） | 崩溃：产品特异 | 崩溃 | 崩溃 | 崩溃 | 崩溃 | 崩溃 | derived judgment of unknown quality |

**净结论**：真正跨六语境稳定的候选构念是——**身体/生物状态（年龄-身高-性别-健康）**、**空间邻近（距离-地理位置）**、**资源存量（收入-资产-人力资本复合，需拆存量/流量/预期）**、**身份属性（族裔-宗教-文化-户籍，作为 attribute 而非偏好）**、**行为习惯（烟酒作息饮食）**、**关系状态与义务（需解耦当前/历史/义务）**、**注意力与可分配时间（响应-在场-陪伴供给）**、**方向性吸引/性偏好（取向、角色作为情境偏好 PR/RC）**。不稳定/崩溃项大多是因为产品把 **PR/RC/身份** 揉进了 **O** 字段（M2 压缩），其解法不是 p 化更多参数而是**拆分字段语义**。

---

## 8. 产品默认假设与混一字段审计

### 8.1 身份/吸引/意图混一字段审计（#2 `5565170990` 检查项）

| 产品 | 是否把 attraction / intent / goal / identity / partner-sex 混一字段 | 证据 | 裁决 |
|---|---|---|---|
| eHarmony | 是 | 注册 token「I am woman/man/nonbinary」同时定身份与吸引方向 | UI compression |
| POF | 是（历史） | 寻找性别二选一；无独立取向列表 | UI compression |
| 珍爱/佳缘/百合 | 是 | 「我是女生，找男士」= 身份+partner-sex 一并成型；无取向/非二元 | UI compression |
| 探探 | 是 | 无任何显式字段；滑动性别偏好隐含身份 | compression by omission |
| Tinder | 部分 | 身份（性别/取向）与意图（Relationship Goals）分开；但 Beyond Binary 主桶把 genderfluid/GNC/intersex 合并 | 部分解耦，OK |
| Hinge | 部分 | 性别可过滤但取向不可过滤、「prefer-not-to-say」参与计权 → 取向成为半隐藏偏好 | 部分混合 |
| Grindr | 部分 | 取向隐含（MSM 假设）；Position/Tribes 把性偏好与身份揉合 | UI compression |
| HER | 否 | 性别、性身份、亲密偏好三字段分离 | 正面反例 |
| Feeld | 否 | 性别/取向/关系类型/Desires 四字段分离 | 正面反例 |
| Muzz | 是 | 教派单选 = 身份+严格度；婚姻导向为产品级默认 | UI compression |

**报告结论**：混一字段清单 = 上述全部「是/部分」条目。#2 裁决要求把性别、性取向、亲缘、熟悉程度、既有关系历史分别建模，这些产品的混装字段就是最典型的反例素材。

### 8.2 三个默认假设检查

| 产品 | 异性默认？ | 陌生起点？ | 单一浪漫目标？ | 备注 |
|---|---|---|---|---|
| 珍爱/佳缘/百合 | 是 | 是 | 是（婚恋） | 父母代注册反将第三方引入 |
| eHarmony/EliteSingles/Match | 部分（近年开放同性） | 是 | 是（长期/婚姻） | Match 有 Dating Intention 光谱 |
| POF | 历史是 | 是 | 部分（intent 过滤 secondary） | — |
| OKCupid/Tinder/Bumble/Hinge/CMB | 否（多取向） | 是 | 部分（有 intent 独立字段） | 均含 friends/figuring-out 项 |
| Grindr | 否（MSM） | 是 | 否（含 hookups/friends/network） | 最不默认浪漫的产品之一 |
| HER/Feeld | 否 | 是 | 否（Feeld ENM/一夫一妻双开） | 结构字段分离典范 |
| Muzz/SilverSingles/OurTime | 是（异性为主） | 是 | 是（婚/长期） | 50+ 为长期陪伴 |
| 探探 | 大陆是（国际否） | 是 | 部分 | — |
| Soul | 弱化（非婚恋） | 是 | 弱浪漫 | 星座作为唯一 A 类精细筛选 |
| 陌陌 | 否 | 是 | 否（开放社交） | 零结构化关系字段反例 |

**对 LHRM 的约束结论**：19 个产品中 15 个默认异性、全部默认陌生起点、14 个默认浪漫/婚恋目标。这些是**产品市场选择**，不是关系模型真值；LHRM 必须像 #2 `5565170990` 所述，把性别/性取向/亲缘/熟悉度/历史当独立维度，用一对具体的人加关系（Human Dyad + D）表达，不以「匹配对象类型」一栏揉合。

---

## 9. 重复计数风险表

产品字段里最常被同一平台重复计数的构念组合（dispatch 明确点名的 age+appearance+fertility、income+assets+spending、companionship+time+availability+responsiveness 等），逐组列风险与拆分建议：

| # | 冗余组 | 表面字段组合 | 重复计数风险 | 建议（保留维度） |
|---|---|---|---|---|
| 1 | 年龄 / 年轻外貌 / 生育代理 | 年龄字段 + 照片青春感 + 星座/生肖 | 用年龄直接代理年轻与生育窗口，三者再各加参数=三倍计数 | 年龄=索引(O)；外貌=吸引力(DJ/照片revealed)；生育窗口=医学事实(O)，只在需表达时激活 |
| 2 | 收入 / 资产 / 消费力 / 肯花钱 | 收入字段 + 房产 + 车 + 「肯花钱」文本 | 存量×流量×让渡×欲望四层叠加 | 存量(资产)、流量(收入)、让渡(行为 RP)、消费欲望(PR) 四个异质维度 |
| 3 | 学历 / 智力 / 阶层 / 门当户对 | 学历 + 学校 + 职业 + 家庭背景 | 学历同时承载认知、阶层、文化、收入预期，一次计四个语义 | 认知能力(L)、阶层学徒(O)、收入预期(PR)、家庭制度(RC) 分开 |
| 4 | 陪伴 / 时间 / 可得性 / 响应 | 陪伴文本 + 在线/活跃 + 响应速度 | 「陪伴」同时=需求偏好、可分配时间、在场行为，三者互不替代却常同参 | 需求(PR)、供给容量(O)、在场(RP)、响应(RP)，不同层不合并 |
| 5 | 宗教身份 / 严格度 / 保守价值观 | 宗教 + 祈祷/清真 + 政治立场 | 宗教信仰一个字段=身份+行为+价值观 | 身份/行为强度/价值观三轴分离（Muzz 反例：已有三字段，方向对） |
| 6 | 星座 / 生肖 / 血型 / 生日 | 生日 + 派生标签 | 全由 DOB 派生，纳入即与生日双重计数 | 全部归派生标签 DJ，不进参数（只留 DOB） |
| 7 | 身高 / 体重 / 体型 | 三字段并列 | 共同样本同一物理对象的三视图，各自立参数=3 倍 | 物理状态(O) 整体描述即可；偏好则分开（自己是 PR 不是状态） |
| 8 | 心态 / 魅力 / 气场 / 幽默 | 文本评价词 | 全部是被更好者复合的派生判断 | 合成到 F 簇的 DJ；不单独成参 |
| 9 | 地域 / 籍贯 / 户口 / 城市层级 | 所在地 + 籍贯 + 户口 + 工作地 | 四个地理概念每个都各含「机会+身份+制度」三层 | 机会(E)、身份(E)、制度(RC) 按层计数，不按字段数 |
| 10 | 顾家 / 孝顺 / 传统 / 责任心 | 四文本词 | 高度重叠的传统角色偏好族 | 保留「时间分配+角色预期+价值」三轴，弃文本标签 |
| 11 | 匹配度 / 契合分 / 完整度 | OKCupid %、POF Chemistry、Soul 匹配度、佳缘完整度 15% | 平台自算分数被当作互不相关的独立证据源；实则同一产品一根功能 | 只作为 derived judgment observation，分开 productos |
| 12 | 择偶六维 vs 档案六维 | 择偶条件（年龄/身高等）与档案字段镜像 | 佳缘/百合把同一维度在「我的档案」和「我的要求」两头各计一次 | 拆分「自报状态」与「偏好区间」两个不同 predicate；匹配是他们的函数 |

---

## 10. 裁决：哪些字段留在 UI/Observation 层，哪些可能进入 primitive 候选

> 本裁决仅具取证性质：Project Architect 在 join gate 做最终 fusion。#2 `5565245810` 核心判据「最小充分性」被采纳为取舍标准——若已知更高层状态后，更底层细节不再提供独立信息，则更底层留在 mechanism 层。

### 10.1 明确留在 UI / Observation / derived 层（不进入 primitive 候选）

| 类别 | 字段 | 理由 |
|---|---|---|
| 派生标签 | 星座、生肖、血型、星象门户、MBTI 结果 | 完全从 DOB/问卷派生（DJ）；@#9 冗余组 6 |
| 装饰性物理 | 发色、瞳色、脸型、魅力部位、体重自报 | 纯外观装饰（O/DJ），模型价值近零 |
| 平台自算分数 | Match %、Chemistry score、Compatibility Score、匹配度、完整度 | derived judgment，来源闭源不可校验，禁当真值 |
| 纯自报评价 | 真诚、成熟、幽默、情绪价值、善良等词 | 自报不可信（Eastwick），只能当 DJ/文本，行为验证才可能 |
| 单平台制度字段 | 户口、籍贯、独生、「体制内」 | 制度性/地域性 RC，非 universal primitive |
| 民俗/身份标签 | 教派单选=身份+严格度、Tribes、Pride Pins（细分） | 身份-审美复合（M2），语义过重不可直接入参 |

### 10.2 可能进入 primitive 候选的构念簇（低冗余、跨语境稳定、有操作定义）

按 §7 稳定测试 + §9 去冗余后的**候选列表**（供 join gate 用，#2 裁决前不修改 ontology）：

1. **物理/生物状态**（O）：年龄作索引 + 身高 + 性别作属性 + 健康状况，仅在 ρ 相关时激活生育窗口。
2. **空间邻近**（O/E）：距离 / 所在地，作为接触机会结构与互动成本。
3. **资源堆栈**（O/PR/L）：存量（资产）· 流量（收入）· 预期（上进心/学历 proxy）· 让渡（RP 行为），四层分明。
4. **身份属性**（identity）：族裔 / 宗教 / 文化 / 语言 / 户籍，都是 attribute（不内嵌偏好方向），偏好另列 PR。
5. **行为习惯**（O）：烟酒毒品饮食作息运动宠物清洁，作为日常兼容面的状态。
6. **关系状态与义务**（RC，解耦三件）：当前关系/可得性 · 关系历史 · 义务负载（子女/赡养/家庭结构）。**这是产品做的最差的一块**。
7. **注意/时间/在场**（O/RP）：可分配时间、活跃度、响应速度——兴趣与投入的 revealed 信号。
8. **方向性吸引与性偏好**（PR/RC）：性取向（方向）、浪漫取向（方向）、性偏好（acts）、关系结构（monogamy/ENM），四成分明，行为与身份分离（#2）。
9. **关系目标/意图**（PR）：长期/短期/婚姻/朋友/ENM，独立于方向与身份。
10. **互动质量层（D）**：app 里最接近它的只有 prompts（「期望」的 proxy）与行为序列（like/message/meet/We Met）；prompts 无法测「接不接受得住」。互动质量是行业统一的字段盲区，本报告不提议补静态参数，而是建议保留为行为事件序列。

### 10.3 为什么产品的 enum 字段大多不适合直接当 primitive

理由三条：(1) 枚举字段把 PR/RC/DJ/identity 揉进一个 token（M1/M2），语义不可分离；(2) 自报在真实互动中预测力趋零（Eastwick；Fisman 子集），静态preference 只能当 belief；(3) 派生标签（星座匹配度）没有独立信息增量，违反最小充分性。所以**可填入的字段 = observation + declared-belief，可进入 primitive 的是 §10.2 的构念簇及其函数**。

---

## 11. 可复用 / 不可复用结论

### 11.1 可复用（进 join gate 或供后续方向用）

- **六类压缩模板**（§4 M1–M6）：可作为「字段→构念还原器」的机械规则，对任何新 app 字段做快速审计。
- **144 条拆解 + 类型码**（§6）：每个拆解带「来源产品 + 跨语境稳定性」，可与 #6 的 120 条现实词拆解做并查、差分去重。
- **declared/revealed 分离的机制构成**（§5.2）：把 app 字段进 S-belief、行为进 revealed-interest、匹配度进 observation；此规则可直接用。
- **冗余风险表**（§9）12 组：可直接作为 join gate 的重复计数 checklist。
- **产品默认假设审计**（§8.2）：「默认异性/陌生/浪漫」的清单 + 混一字段清单，确保不把产品假设带回 LHRM。
- **跨语境稳定性结论**（§7）：受测构念的六语境结果表，供 architect 直接引用。

### 11.2 不可复用 / 不应进入模型

- 任何产品的匹配分数公式（全部或闭源或主题有限）；Match %、Compatibility Score、完备度均不可当真值。
- 单平台制度字段（户口/独生/教派必填/「体制内」）作为 universal 参数——只能作为 E 层 context。
- 产品「异性/陌生/婚恋」默认作为入口假设——直接违反 #2 `5565170990`。
- 星座/生肖/血型/MBTI/魅力部位等派生标签——无独立信息增量。
- 学术结论不能直接变成权重：Buss/Fisman 的**自报性别差**只在纸面语境成立，不可 pin 成行为系数。

### 11.3 明确 Unknown / 局限

- 除 OKCupid（概念层 + Wayback 存档的 2014 行为实验）、Hinge（how-we-connect-daters）、Zoosk（SmartPick 描述）、Match（Synapse 存在无公式）、珍爱/佳缘/Soul（算法备案条文的粗粒度）外，**所有产品排序权重均为 Unknown**；本报告未注入任何推断值。
- 多数字段清单来自官方帮助中心（可能滞后于 App 实际版本）或二手评测（已标 `secondary`）；`(as of 2026, verify)` 项应在实际账号里复验。
- CMB 全字段清单、Hinge prompt 目录、Muzz AI、OurTime 过滤列表等细节仅二级来源，待核。
- 本报告是**建模推断**（hypothesis）的集合，除 §5.1 学术证据外不宣称经验成立。

### 11.4 与其他 Research 的边界

- 与 `#4@deep-scientific-relationship-primitives`：本文为 app 侧观测证据，学术构念的 KEEP/SPLIT 由其工程出；本文 §10.2 的构念簇与其 candidate 清单供交叉验证。
- 与 `#6@deep-real-world-proxy-decomposition`：两者都有 proxy 拆解（本文 144 条 app 词 vs #6 120 条现实词），join gate 应做并集去重；本文负责「产品字段→构念」，#6 负责「社会统计/真实案例→观测」，重叠主要在收入/婚况/宗教/陪伴等语义，已在 §9 冗余组标注。
- 与 `#3@deep-game-relationship-primitives`：游戏侧的状态机/数值化可视为「把关系显式参数化」的对照面，本文的「产品选择只填 S/O 层」「D 层只能由行为逼近」恰是游戏系统反过来能显式建模 D/E 层的补集。

---

## 12. 来源清单（primary 优先）

### 官方文档 / 官方博客（`official`）
- OKCupid help: okcupid-app.zendesk.com — 22982200783771 (How does OKCupid work), 22770910347803 (Match Questions), 22907669592091 (Preferences), 22907566093723 (Identity Tags)
- OKCupid blog (offline) — "We Experiment On Human Beings!" 2014-07-28，存档：gwern.net/doc/psychology/okcupid/weexperimentonhumanbeings.html
- eHarmony: eharmony.com/tour/what-is-compatibility-system; eharmony.co.uk/tour/what-is-the-compatibility-quiz; eharmony.com/dating-advice/dating/lgbtq-dating; glaad.org/eharmony-glaad-inclusive-updates-2023 (secondary-org primary about product)
- EliteSingles: elitesingles.com/mag/online-dating/personality-test; elitesingles.com/faq; elitesingles.com/hc/en-us/articles/203057292
- Match: help.match.com 12625991507867 (Edit Profile), 6241672918683 (Improving Matching Results), 6241693282331 (Searching on Match); intl2.match.com/help/help.aspx; match.com
- POF: help.pof.com; pof.com/hc/en-us/articles/360050341111 (Gender Visibility); blog.pof.com
- Zoosk: support.zoosk.com 51223998344340 (SmartPick), 51223835191956 (How does matching work), 51224010205972 (Carousel); zoosk.com/date-mix（From Swipe to Soulmate）
- Tinder: help.tinder.com 115003339043 (Edit profile), 7606685697037 (Powering Tinder), 15668360470669 (Gender & Sexual Orientation); tinderpressroom.com
- Bumble: support.bumble.com 28530815473949 (Adding info), 28423691289629 (Filters); bumble.com/the-buzz（filters posts）
- Hinge: help.hinge.co 360011063294 (Preferences), 38014282744595 (Subscription benefits), 36311352171539 (Prompts); hinge.co/how-we-connect-daters
- CMB: coffeemeetsbagel.zendesk.com 360019599254, 31212228097043 (Discover), 33782396591123 (Suggested), 51933595795731 (Topic Suggestions)
- Grindr: help.grindr.com 4402336949523 (Build Your Profile), 12155443240851 (Filters), 52087147268115 (Settings)
- HER: support.weareher.com 36994637903515 (Sex/Kink/Intimacy Preferences), 15464152409748 (Pronouns); weareher.com/launching-sex-intimacy-and-kink-preferences
- Feeld: support.feeld.co 18822038569884 (Desires/Relationship Types/Sexualities/Genders); feeld.co/ask-feeld; feeld.co/glossary; feeld.co/about/faq
- Muzz: muzz.com/us/en/help（Muzz-101 / ethnicity filter）; muzz.com/us/en/blog（Hello to new ethnicity filters）; apps.apple.com listing (id969997496)
- SilverSingles: silversingles.com/mag/about-silver/our-site/profile; .../faq
- OurTime: help.ourtime.com 6619430860827 (Edit profile), 33951900727067 (Sensitive data)
- 珍爱网: zhenai.com/help; i.zhenai.com/m/client/intro/policy.html; zhenai.com
- 世纪佳缘: jiayuan.com/helpcenter; jiayuan.com/bottom/private.html; vip.jiayuan.com/landing_page.php
- 百合网: help.baihe.com（index.php?action=list&cat=574&listid=28 隐私政策；cat=557&listid=11 匹配系统）; apph5.baihe.com/setup/help; my.baihe.com/register
- 探探: tantanapp.com/zhHant
- 陌陌: immomo.com; apps.apple.com listing (id448165862)
- Soul: themis.soulapp.cn/algorithms备案页; apps.apple.com listing (id1032287195)
- 青藤之恋: qingtenglove.com; apps.apple.com listing (id1472343551)

### 二手来源（`secondary`，均已标注于正文）
- POF five-factor / gender binary: thepinknews.com/2018/04/10/...; au.pcmag.com/dating/4352/pof
- Hinge dealbreakers corroboration: profilesharp.com/en/blog/hinge-dealbreakers-filters
- CMB prompt topics: sparking.chat/dating-apps/coffee-meets-bagel/prompts
- Grindr tribes: datingprofiles.ai/blog/grindr-tribes-explained
- Tinder algorithm history: swipestats.io/blog/tinder-algorithm
- 探探访谈/产品分析: code.python88.com/l/Q27x94pwGD（王宇访谈转载）; woshipm.com/evaluating/634781
- 陌陌/Soul 分析: news.iresearch.cn/yx/2026/02/546483（宣传稿，数值不可信）; woshipm.com/evaluating/3966616
- 青藤之恋技能: news.qq.com/rain/a/20240412A02LRJ00（一手体验报道）; baike.baidu.com（百科）
- 百合/世纪佳缘补充: 公开可核验的官网 help 页为主，均优先官方
- OurTime onboarding: cooldatingadvice.com/ourtime-review; seniordatingexpert（secondary 过滤列表）

### 学术（`established`，DOI/URL 见 §5.1）
- Buss (1989) BBS 37-cultures — cambridge.org/core（"Sex differences in human mate preferences…"）；PDF labs.la.utexas.edu/buss
- Eastwick & Finkel (2008) JPSP 94(2) — doi.org/10.1037/0022-3514.94.2.245
- Eastwick, Luchies, Finkel & Hunt (2014) Psych Bulletin — doi.org/10.1037/a0032432
- Fisman, Iyengar, Kamenica & Simonson (2006) QJE 121(2) — doi.org/10.1162/qjec.2006.121.2.673
- Hitsch, Hortaçsu & Ariely (2010) QME — doi.org/10.1007/s11129-010-9088-6；AER — doi.org/10.1257/aer.100.1.130
- Finkel, Eastwick, Karney, Reis & Sprecher (2012) PSPI — doi.org/10.1177/1529100612436522；APS Q&A psychologicalscience.org
- Joel, Eastwick, Finkel et al. (2020) PNAS 117(32) — doi.org/10.1073/pnas.1917036117
- Tennov, D. *Love and Limerence* (1979) — 引用为「对清单式选人持怀疑的立场来源」，未核验其针对商业兼容算法的实证（链条标 Unknown）

---

*End of report. Evidence discipline: `official` / `secondary` / `Unknown` 已显式区分；建模推断与经验事实分离；不修改 canonical ontology。*