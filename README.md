# LHRM

**Li-Hong Relationship Model / 礼宏关系模型**

LHRM 是一个用于研究、表达与仿真人类二人关系的开放研究项目。

当前第一目标不是制造单一“恋爱打分器”，而是建立一套 **可解释、方向化、时间索引、保留 Unknown 与不确定性的人际关系状态表示语言**：能够把现实/叙事中的人物、双向关系、Belief、Action/Event、Environment、Constraint 与 history 统一映射到动态 state space，再由下游任务选择是否做距离、预测、仿真或决策。

核心原则：

```text
Representation before scalarization.
State-space before score.
```

## 当前阶段

项目已完成第一轮四源 Research 发散：

- 游戏/人生模拟中的关系状态建模；
- 关系科学/认知生物中的基础构念；
- 婚恋/约会 App 的字段、偏好与 revealed behavior；
- 社会现实/统计/极端案例中的 proxy decomposition。

当前进入：

```text
Parameter Convergence
-> Candidate Minimal Sufficient State
-> representation coverage regression
-> Measurement & Canonicalization
```

当前 candidate directed relationship basis v0.1（尚未冻结）包括：

```text
Liking
RomanticAttraction
SexualDesire
Trust
AttachmentSecurity
Caregiving
Dedication
OutcomeDependence
```

这些只描述 directed relationship state。Agent 属性、Pair state、Belief、Constraint/Agreement、Action/Event、Environment、History 与 uncertainty/provenance 分层保存，不强行塞入同一个向量。

## 当前架构入口

- `AGENTS.md` — 项目本地 Agent 规则与治理指针
- `docs/foundation/CURRENT_ARCHITECTURE.md` — **当前 canonical architecture snapshot**
- `docs/foundation/PARAMETER_CONVERGENCE_V0_1.md` — 当前候选参数收敛与下一验证门
- `docs/foundation/CONSTRUCT_SCOPE_DIRECTIONALITY.md` — construct family、方向性与跨 scope 表示原则
- `docs/foundation/PROJECT_HISTORY_2026-09-10.md` — 从项目起点到当前的 provenance 梳理
- `docs/foundation/STAGE_SUMMARY_2026-09-07.md` — 历史阶段 checkpoint
- `docs/foundation/RELATIONSHIP_EVALUATION_FOUNDATION.md` — 早期关系评价坐标系研究稿
- `docs/ARCHITECT_BOOTSTRAP_REPORT.md` — 架构师接管记录
- `docs/ARCHITECT_RECONNAISSANCE_REPORT.md` — 早期架构预研与外部对齐

## Research evidence

首轮四源报告：

- `docs/research/RESEARCH_REPORT_GAME_RELATIONSHIP_PRIMITIVES.md`
- `docs/research/RESEARCH_REPORT_SCIENTIFIC_RELATIONSHIP_PRIMITIVES.md`
- `docs/RESEARCH_REPORT_DATING_APP_PARAMETER_PRIMITIVES.md`（历史路径，后续可整理到 `docs/research/`）
- `docs/research/RESEARCH_REPORT_REAL_WORLD_PROXY_DECOMPOSITION.md`

长期 benchmark：GitHub issue `#13` — 现实世界关系 Case Bank / completeness regression。

## 当前建模边界

LHRM 的最小研究对象是两个具体的人及其关系：

```text
HumanDyad(i,j)
= Person_i + Person_j + Relationship_ij
```

不默认异性、陌生起点、恋爱/婚姻目标，也不把动物研究扩成模型对象。第三者、父母、孩子、朋友、同事、制度、文化等作为更大社会网络/环境进入。

当前 relationship 结构优先表示为：

```text
Relationship_ij
= DirectedState_(i->j)
+ DirectedState_(j->i)
+ PairState_(i,j)
```

世界层同时区分：

```text
Reality != Observation != Belief
```

状态演化采用：

```text
CurrentState
+ Action/Event
+ Belief
+ Constraint
+ Environment
-> NextState
```

核心不以预写 relationship state machine、统一欧氏距离、统一权重或强制 `0..1` 总分作为地基。

## 验证路线

项目新增长期 Case Bank：优先从法院/官方事实材料提取关系事实链，让独立 Agent 逐句测试是否能映射到当前 schema；无法表示的句子记录为 `MAPPING_FAILURE`，再由 Architect 判断是 ontology / construct / scope / temporal / belief / measurement hole，还是仅为叙事修辞/无关信息。

真实案例用于 completeness / closure / regression，不用于从个案估计人口概率。

## 治理

LHRM 的全局 Agent 治理遵循 `youling/ai-use` 当前规范；Git/GitHub 是 durable truth。Human 对目标、范围、风险与重大架构方向拥有最终权威；Project Architect 在当前授权内默认持续推进普通架构与研究收敛。

研究结论不得强于证据。未经真实数据校准的参数、权重、概率、距离与转移公式不得表述为已验证预测模型。
