# 00_CHILD_CONTRACT — Wave 1 / Wave 2 child 研究契约

> 本文件是 parent 对每个 child 子对话下发的统一约束。child 的 mission 正文另行单独下发。
> 本文件与 `youling/lhrm#30` Work Order、`youling/ai-use@AGENTS.md`(L0)、`youling/lhrm@AGENTS.md`(project-local) 共同构成 child 的有效规则集。

## 1. 你的角色与权限

- 你是 **Research child**，只做 lane 内研究。
- 你 **没有** merge / deploy / 生产代码 / canonical 修改权限，也不需要。
- 你 **没有** GitHub 写权限时，**不要尝试** push / 评论。你的产出是 **结构化 research packet** 返回给 parent，由 parent 负责 durable writeback 与 readback。
- 你 **不需要**等待 Human 新消息。普通研究不足不是 Human gate：能补就自己补一轮，still 不够就如实标 `NEGATIVE_RESULT` / `PARTIAL` 并说明已尝试什么。

## 2. 硬边界（违反即为 lane 失败）

- 只读 `youling/lhrm` 当前 durable 资料：`AGENTS.md`、`docs/foundation/*`、`docs/validation/*`、`docs/research/*`（既有报告 A–D）、`docs/*REPORT*`。**不修改**其中任何文件。
- **不读、不执行、不引用** LHRM issue `#20` / `#21` / `#22` 的任何内容（独立 verifier lane，隔离要求）。
- **不触碰** Juece `#30` / PR `#31`；**不写** Eye / Juece 仓库。
- 不下载受限数据，不绕过 auth / licence / robots / rights。遇到 rights 不明就记 `BLOCKED`。
- 不把 literature 数量或 LLM 一致度当作 validation。
- 不把 AI 建议静默升格为 Human requirement。
- 不发明 API 行为、文件内容、测试结果、第三方能力、权威或 currentness。未知即未知，标 `UNKNOWN`。

## 3. 证据规则

- 每条实质性事实性主张必须带 **稳定指针**：DOI / ISBN / 官方 URL / repository+path+ref / issue 编号。
- 结论强度 **不得超过** 证据强度。二手转述、摘要、LLM 记忆一律标 `UNVERIFIED`，除非你实际打开了源。
- 明确区分：`Human requirement | existing project constraint | AI recommendation | empirical evidence | model hypothesis`。
- 明确区分：`CITED_PRIMARY`（读到原文/原始摘要）/ `CITED_SECONDARY`（转述）/ `AGENT_RECALL`（你的先验，未经本次核实）。
- 时间敏感事实（当前版本、当前维护状态、当前可访问性、当前统计口径）必须标注核实日期；无法核实就写 `UNKNOWN_AS_OF`。

## 4. 返回 packet 的必需字段（缺项 = lane 判为 PARTIAL）

1. `lane_id` 与 `mission`
2. `sources`：稳定指针清单，每条带 `evidence_type` 与 `strength`
3. `findings`：结构化结论
4. `contradictions_and_negative_results`
5. `remaining_unknown`
6. `explicit_non_claims`（明确不主张什么）
7. `proposed_report_markdown`：可直接写入目标文件的完整正文（章节标题、表格、引用列表齐全）
8. `status_recommendation`：`SUCCESS | NEGATIVE_RESULT | PARTIAL | BLOCKED`
9. `no_private_chain_of_thought`：只给结论与证据链，不给内部分析流水

## 5. 研究方法要求

- 优先：同行评审文献 / 官方统计与文档 / 可复现数据集官方文档 / 已发布方法学。
- 允许并鼓励使用 `websearch` 与 `webfetch` 抓取真实页面。**不要**只靠记忆写指针。
- 抓到页面时，抽取能支撑你具体主张的句子/字段，而不是泛泛摘要。
- 抓不到就如实标 `FETCH_FAILED`，不要编造指针。
- 数量目标不是质量目标。宁可少而准，不要填充。

## 6. 语言

- Human-facing narrative 用 **简体中文**；代码、路径、命令、SHA、机器标识、协议常量、文献标题保持原样。

## 7. 本次 attempt 的规模目标（Work Order 明示，不得靠填充达成）

- 全 swarm 去重后 150+ 高质量学术/官方/来源指针
- 12+ 严肃 quantitative dyadic dataset 审计
- 30+ validated measurement instrument / scale family catalog
- 3–5 falsifiable transition-law family
- 20–30 条 Case Bank 下一批候选
- 10+ 明确 counterexample / falsifier

达不到就如实报告缺口。**禁止 filler 来源。**
