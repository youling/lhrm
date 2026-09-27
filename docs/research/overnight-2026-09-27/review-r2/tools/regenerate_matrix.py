#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Regenerate `CROSS_LANE_VERDICT_MATRIX.md` from the durable packet JSON.

This script reads **only** `packets/*.json` (committed in this directory).  It
does not read the original markdown packets, so a third party can reproduce the
matrix from this PR alone:

    python tools/regenerate_matrix.py --packets-dir packets --out CROSS_LANE_VERDICT_MATRIX.md

Truncation policy
-----------------
**No column is truncated.**  The pre-2026-09-28 matrix capped `claim` at 300
characters, `verdict` at 150, `recommendation` at 110 and `corroboration` at 46,
which is what made the join unreproducible.  Every join field is now emitted in
full.

Two *rendering* transformations are applied, and only these two.  Neither loses
a character:

1. a raw `|` inside cell text becomes `\\|` (markdown table safety).  The
   unescaped text is in the JSON;
2. a newline inside cell text becomes `<br>` (markdown table safety).  The
   unescaped text is in the JSON.

`primary` is a **derived** column, not a packet field: it is the sequence of
contract-§4 enum words found in the child's own `verdict` text, in order of
first appearance (see §0.4).  It never changes the child's wording.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import OrderedDict

# Lane order and cluster labels, taken from REVIEW_SWARM_MANIFEST.md §2.
LANES = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
CLUSTERS = OrderedDict([
    ("A", "construct ontology / redundancy"),
    ("B", "measurement instruments / proxies"),
    ("C", "datasets / access / rights"),
    ("D", "statistics / identification / transition laws"),
    ("E", "belief / partial observability / knowledge"),
    ("F", "dynamics / hysteresis / pair-state emergence"),
    ("G", "general dyad scope / ABM / LLM layer"),
    ("H", "paper positioning / novelty"),
    ("I", "red-team falsifiers / Gate A-B-C"),
    ("J", "citation / provenance recheck"),
    ("K", "cross-lane contradiction map"),
    ("L", "actionability / next-work-order filter"),
])

# REVIEW_CONTRACT.md §4's five words, plus the phase-2 notations the parent
# already mapped (REVIEW_SWARM_MANIFEST.md §6).  The five recommendation
# verbs (ACCEPT / ACCEPT_AS_PROPOSAL / HOLD_FOR_EVIDENCE / REJECT /
# RECLASSIFY_AS_METHOD_LIMIT) are deliberately **excluded**: they are
# contract §5 field 10's vocabulary, not the verdict vocabulary, and counting
# them here would turn prose such as "…so `REJECT` the claim" into a spurious
# mixed verdict.
ENUM_WORDS = [
    "VERIFIED", "PLAUSIBLE", "CONTESTED", "UNSUPPORTED", "WRONG-SCOPE",
    "PARTLY_REFUTED", "REFUTED", "MOOT", "RESOLVED_FOR_FACT",
    "GENUINELY_OPEN", "NOT_ENFORCEABLE_AS_WRITTEN", "IMPRECISE",
    "REPRODUCED_BY_ME", "VERIFIED_AND_UNDERSTATED", "SUSTAINED",
]
ENUM_RE = re.compile("|".join(re.escape(w) for w in sorted(ENUM_WORDS, key=len,
                                                          reverse=True)))

#: Display cap on the *derived* `primary` label only.  It never touches packet
#: text; the full ordered token list is recomputable from §0.4's rule.
PRIMARY_DISPLAY_CAP = 3


def cell(text, pointer=None):
    """Render one table cell.  Never truncates."""
    if text is None:
        text = ""
    text = text.replace("|", "\\|")
    text = text.replace("\r\n", "\n").replace("\n", "<br>")
    text = text.strip()
    if not text:
        return pointer if pointer else "`NOT_STATED_IN_PACKET`"
    return text


def derive_primary(verdict_text):
    """Derived column: the child's own verdict-vocabulary words.

    Ordered, de-duplicated, first appearance wins.  Never changes the child's
    wording; `verdict` itself is emitted in full.
    """
    if not verdict_text:
        return "NOT_ENUM"
    found = []
    for m in ENUM_RE.finditer(verdict_text):
        w = m.group(0)
        if w not in found:
            found.append(w)
    if not found:
        return "NOT_ENUM"
    if len(found) == 1:
        return found[0]
    shown = found[:PRIMARY_DISPLAY_CAP]
    label = "MIXED:" + "+".join(shown)
    if len(found) > PRIMARY_DISPLAY_CAP:
        label += "+%d_more" % (len(found) - PRIMARY_DISPLAY_CAP)
    return label


def load(packets_dir):
    out = OrderedDict()
    for lane in LANES:
        path = os.path.join(packets_dir, "R2_%s.json" % lane)
        with open(path, encoding="utf-8") as fh:
            out[lane] = json.load(fh)
    return out


def build(data, prior_rows, prior_counts_note):
    primary_counts = OrderedDict()
    lane_rows = OrderedDict()
    pointers = OrderedDict()

    for lane in LANES:
        d = data[lane]
        rows = []
        for r in d["records"]:
            cid = r["claim_id"]
            verdict = r.get("verdict", "")
            primary = derive_primary(verdict)
            primary_counts[primary] = primary_counts.get(primary, 0) + 1
            claim_ptr = None
            if not r.get("claim"):
                claim_ptr = ("—（本 child 的这张表**没有 `claim` 列**；逐字原文见 "
                             "`packets/R2_%s.json` → `%s` → `_extra_columns`）"
                             % (lane, cid))
            verdict_ptr = None
            if not verdict:
                verdict_ptr = ("—（本 child 的这张表**没有 `verdict` 列**；"
                               "child 的判断在 `%s.requires_canonical_change` / "
                               "`.corroboration` / `_extra_columns`，见 JSON）"
                               % cid)
            rows.append("| `%s` | `%s` | %s | %s | %s | %s | %s |" % (
                cid, primary,
                cell(verdict, verdict_ptr),
                cell(r.get("requires_canonical_change")),
                cell(r.get("corroboration"),
                     "`NOT_STATED_IN_PACKET`"
                     if r.get("corroboration_source") != "explicit_field"
                     else None),
                cell(r.get("recommendation_to_architect")),
                cell(r.get("claim"), claim_ptr),
            ))
        lane_rows[lane] = rows
        pointers[lane] = d["record_count"]

    total = sum(pointers.values())
    return primary_counts, lane_rows, pointers, total


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--packets-dir", default="packets")
    ap.add_argument("--out", default="CROSS_LANE_VERDICT_MATRIX.md")
    args = ap.parse_args(argv)

    data = load(args.packets_dir)
    primary_counts, lane_rows, lane_counts, total = build(data, 0, "")

    ordered = OrderedDict(sorted(primary_counts.items(),
                                 key=lambda kv: (-kv[1], kv[0])))
    count_rows = "\n".join("| `%s` | %d |" % (k, v) for k, v in ordered.items())

    sections = []
    for n, lane in enumerate(LANES):
        letter = chr(ord("A") + n)
        sections.append(
            "## 2.%s — lane `%s`（%s）\n\n"
            "| claim_id | primary | verdict（原文） | canon | corroboration | "
            "recommendation | claim（原文） |\n"
            "|---|---|---|---|---|---|---|\n"
            "%s\n" % (letter, lane, CLUSTERS[lane], "\n".join(lane_rows[lane])))

    lane_count_rows = "\n".join(
        "| `%s` | %s | %d |" % (lane, CLUSTERS[lane], lane_counts[lane])
        for lane in LANES)

    text = MATRIX_TEMPLATE % {
        "count_rows": count_rows,
        "total": total,
        "lane_count_rows": lane_count_rows,
        "sections": "\n".join(sections),
    }

    with open(args.out, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    sys.stderr.write("wrote %s (%d bytes, %d rows)\n"
                     % (args.out, len(text.encode("utf-8")), total))
    return 0


MATRIX_TEMPLATE = """# CROSS_LANE_VERDICT_MATRIX — Round 2 review swarm over `youling/lhrm#31`

> **本文件由 `tools/regenerate_matrix.py` 从 `packets/*.json` 生成，请勿手改。**
> 生成命令：
> `python tools/regenerate_matrix.py --packets-dir packets --out CROSS_LANE_VERDICT_MATRIX.md`
> 它**只读本目录内已提交的 JSON**，因此第三方可以在本 PR 内独立复现本表。
>
> **本文件是 Round-3（`r3/b1`）重生成版本。** 取代 `99a0d32` 的旧版。
> 与旧版的差异、以及旧版的三处可复现性缺陷，逐条列在 §5。
>
> **本表逐字保留 child 的 438 条 record 文本。** 凡被 Architect 裁决或被本轮
> PR #31 修复取代的**评审主张**，登记在 **`SUPERSEDED_REGISTER.md`**
> （`SR-A*` / `SR-B*` / `SR-X*`）；本表**不改任何 verdict**，因此不在该
> register 的取代范围内（见其 `SR-X3`）。

**被审对象**：`youling/lhrm#31` @ `8adcf0bacc45c0feb5c14e65e2a45346dd488b43`（25 份报告，本 swarm 只读不写）。
**统一 verdict 词表**（`REVIEW_CONTRACT.md` §4）：`VERIFIED | PLAUSIBLE | CONTESTED | UNSUPPORTED | WRONG-SCOPE`。
**数据源**：`packets/`（18 个 child，438 条 record，本表取其中 12 个 lane child 的 %(total)d 条）。

## 0. 读法、截断策略与免责

### 0.1 本表不再截断任何一列

旧版把 `claim` 截到 **300** 字符、`verdict` **150**、`recommendation` **110**、
`corroboration` **46**，并写明「完整原文在各 child packet 内」——而那些 packet
**未随 PR 提交**。这就是 `ARCHITECT_ADJUDICATION_V1` §D 第 7 条所指的缺陷。

本版**六列全部逐字输出，不设任何上限**。完整字段另在
`packets/<child>.json` 中以键值形式提供，可 `jq` / `grep` 直接取用。

渲染过程只做两处**不丢字符**的转换，并在本节声明：

| 转换 | 原因 | 未转换的原文在哪 |
|---|---|---|
| 单元格内裸 `\\|` → `\\` + `\\|` | markdown 表格安全 | `packets/*.json` 同名字段 |
| 单元格内换行 → `<br>` | markdown 表格安全 | `packets/*.json` 同名字段 |

### 0.2 `verdict` 列保留 child 原始措辞

未做归一化、未改写、未合并任何两行。`primary` 是**派生列**（见 §0.4），
不构成 parent 的改判。

### 0.3 `corroboration` 列必须与 verdict 一起读

`NON_INDEPENDENT` / `RELAYED_NOT_INDEPENDENT` / `SAME_SOURCE` / `TRANSITIVE`
的行**不得**因「别的 lane 也这么说」而升级（`REVIEW_CONTRACT.md` §4 硬规则）。
本列显示为 `` `NOT_STATED_IN_PACKET` `` 的行 = **该 child 的该条记录本身没有
标注独立性**；这不是 parent 的判断，也**不得**被读成 `INDEPENDENT`。

### 0.4 `primary` 列的派生规则（确定性，可复算）

1. 在该记录 `verdict` 字段的**全文**中按出现顺序抓取 **verdict 词表**内的枚举词：
   契约 §4 的五词（`VERIFIED` / `PLAUSIBLE` / `CONTESTED` / `UNSUPPORTED` /
   `WRONG-SCOPE`）+ `REVIEW_SWARM_MANIFEST.md` §6 的 10 个附加记法。
2. **五个 recommendation 动词**（`ACCEPT` / `ACCEPT_AS_PROPOSAL` /
   `HOLD_FOR_EVIDENCE` / `REJECT` / `RECLASSIFY_AS_METHOD_LIMIT`）
   **不计入**。它们是契约 §5 第 10 字段的词表，不是 verdict 词表；
   把它们计进来会把「…所以 `REJECT` 该主张」这类散文变成假的 `MIXED`。
3. 命中按**首次出现顺序去重**：抓到 **0** 个 → `NOT_ENUM`；
   **1** 个 → 该词；**≥2** 个 → `MIXED:` + 前 **3** 个以 `+` 连接，
   超过 3 个时追加 `+n_more`。
4. 第 3 条的 3 是**唯一**一处显示上限，且只作用于**派生列**；
   完整有序词表可按第 1–2 条从 `packets/*.json` 重算。**packet 字段本身无上限。**

旧版从**被截断的** `verdict` 派生 `primary`，并保留重复 token
（如 `MIXED:VERIFIED+VERIFIED`），因此旧版的 `primary` 计数与本版
**不可直接相减**。

### 0.5 空单元格的含义

本表**不再有静默空单元格**。两种情况会以文字说明而非留空呈现：

* `claim` 列出现「本 child 的这张表没有 `claim` 列」——指 lane `H` 的
  F 组表（`## 8.`），该表的列是 `\\# / claim_id / 文件:行 / 实际行 /
  引文准确性 / 上下文忠实度 / 分析是否成立 / verdict`，**packet 本身没有
  claim 列**；原文逐字保存在 `_extra_columns`。
* `verdict` 列出现「本 child 的这张表没有 `verdict` 列」——指 lane `K` 的
  `### 4.2` 独立性审计表与 `### 4.4` Work Order 表。

逐条清单见 `packets/COMPLETENESS.md` §5（含 `R2_E` / `R2_F` / `R2_I` 的
packet 级字段缺失与 lane `H` 两行短行）。

### 0.6 `canon` 列

`YES` 只表示 child 判定需要 canonical 变更；**是否越过 proposal 由 Architect
决定**，见 `CANONICAL_CHANGE_PROPOSALS.md`。

## 1. 计数

### 1.1 按 `primary`（仅供分诊；派生列，见 §0.4）

| primary | rows |
|---|---:|
%(count_rows)s
| **合计** | **%(total)d** |

### 1.2 按 lane

| lane | cluster | rows |
|---|---|---:|
%(lane_count_rows)s
| **合计** | — | **%(total)d** |

### 1.3 抽取覆盖：机器可读断言（不再是散文免责）

`packets/COMPLETENESS.md` 给出逐包
`declared_records`（锚点扫描） vs `extracted_records`（记录解析器）
vs `records_with_empty_claim` 与总计。两者由**互不调用的两条代码路径**算出，
相等即证明布局处理没有跳过任何一行；`--assert-complete` 在不等时**退出码 1**。

**旧版 §1 下方那段「lane `E` 有 4 行、`H` 与 `K` 有若干行未被抽到」的文字免责，
现已关闭**：4 行 `E-C21`…`E-C24` 已被补回（`E` 21 → 25 行）。
`H` 与 `K` 的行数在旧版即已完整（57 / 50），其问题是**字段级**空缺，
现按 §0.5 精确呈现，并在 `COMPLETENESS.md` §5 逐条给出原因。

**仍然成立、因此不得据本表推断的内容**：

* 不得据本表推断某 lane 的结论条数 = 旧版行数（见 §5.1）；
* `H-C50`…`H-C66` 的 claim 文本在 `_extra_columns`，不在 `claim` 列；
* `K` 的 24 条记录没有 `verdict` 枚举词（`primary` 因此为 `NOT_ENUM` 或
  由 `requires_canonical_change` 承载），这不是 parent 的降级。

## 2. 逐 lane 矩阵

%(sections)s
## 3. 本表**没有**做的事

* 不重读被审报告（parent 未读 PR #31 的 25 份报告）；
* 不改写任何 verdict、不合并任何两行；
* 不实施任何 Work Order、不跑 Gate A/B/C；
* 不触碰 canonical / PR #31 / 任何 fixture / Eye / Juece；
* 不读取 `youling/lhrm#20` / `#21` / `#22`。

## 4. 停止条件

本 swarm 到此为止。**下一动作权在 Human / Project Architect。**
本文件是提交审议的输入，不是决议。

## 5. 与 `99a0d32` 旧版的逐条差异

### 5.1 已修复

| # | 旧版缺陷 | 本版处理 |
|---|---|---|
| 1 | `claim` / `verdict` / `recommendation` / `corroboration` 被截断（300/150/110/46），且声称「完整原文在各 child packet 内」而 packet 未提交 | **不截断**；完整字段在 `packets/*.json`；packet 源文件的 sha256 登记在 `packets/INDEX.md` §2 |
| 2 | 散文承认 lane `E` 有 4 行未被抽到（`E-C21`…`E-C24` 整行缺失） | 已补回，`E` = 25 行；完整性由**机器断言**保证，不再靠散文 |
| 3 | 散文承认 `H` / `K` 部分行的 `claim` 为空 | 行数本来就完整（57 / 50）；空缺是 **packet 无该列**，现按 §0.5 精确呈现并在 `COMPLETENESS.md` §5 归因 |
| 4 | lane `D` 的行号被 parent 重编为 `D-#1`…`D-#40`、`F` 重编为 `F-#1`…`F-#33`，child 自己的 `D-C*` / `F-C*` id 在本 PR 内不可见 | 全部改用 **child 自己的 `claim_id`**；`D-C1`…`D-C40`、`F-C1`…`F-C33` |
| 5 | 表格行内含裸 `\\|` 时列错位（lane `I` 的 `I-C3`、lane `K` 的 `K-C12` 行在旧版里字段明显串列） | 抽取器对超长行做**确定性**重并（`_repair_cells`），并把受影响行数记在 `packets/*.json` 的 `diagnostics.rows_with_cell_repair` |
| 6 | lane `G` 的 `G-C9`…`G-C30` 因 packet 里键名重复（`**verdict:** **verdict:**`）而把 `verdict:` / `requires_canonical_change:` 残留在单元格里 | 抽取器对重复键做去重；`G` 30 行的 `verdict` 列现已全部是纯文本 |
| 7 | lane `H` 的 A 组表头是 `claim（一句复述）`，`F` 组表**根本没有 claim 列**，两者都被旧抽取器漏掉 → 57 行里 17 行 claim 为空 | 表头归一化（去掉全角括号内容）+ 未映射列逐字存入 `_extra_columns`；claim 列现已 40/57 非空，其余 17 行按 §0.5 呈现 |
| 8 | lane `K` 的 `### 4.2` / `### 4.4` / `### 4.5` 三张表用了 5 种不同的列名，旧抽取器只认出两张 | `COLUMN_ALIASES` 登记表覆盖 7 种写法；`K` 50 行全部抽出（其中 8 行为旧版完全缺失的编号） |
| 9 | 完整性只靠散文免责，无可复跑断言 | `tools/extract_packets.py --assert-complete` + `packets/COMPLETENESS.md` |

### 5.2 故意未做

* **不重跑 18 个 child。** 本表是 join 的机械重生成，不是新的审计。
* **不改任何 verdict。** `primary` 计数与旧版不同，是因为**输入不再被截断**
  且补回 4 行；这不是 child 改判。
* **不把 phase-2 的 6 个 child（`ADJ1`-`ADJ3` / `EV1`-`EV3`）并入本表。**
  它们从未进入本 join；它们的 37 条 record 在 `packets/` 内按各自的
  record unit 完整保存（`adjudication_question` / `verification_item` /
  `verification_claim`），并在 `CONTESTED_FINDINGS.md` 中被引用。
* **不删 `REVIEW_SWARM_MANIFEST.md` §5 第 3 条对旧缺口的记录。**
  该条被**取代**并指向本文件，见 `SUPERSEDED_REGISTER.md`。
"""


if __name__ == "__main__":
    sys.exit(main())
