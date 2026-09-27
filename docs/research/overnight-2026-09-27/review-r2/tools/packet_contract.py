#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Frozen extraction contract for the Round-2 review child packets.

This module is the *normative* description of what `extract_packets.py` is
allowed to capture out of the 18 Round-2 review child packets.  It is a frozen
registry: every scoping decision below is explicit, so a third party can audit
the scoping itself and not only the parse result.

Nothing in here is derived from the packets at run time.  If a packet does not
match the declared layout, `extract_packets.py` fails loudly (non-zero exit)
instead of silently emitting fewer records.
"""

from __future__ import annotations

# --------------------------------------------------------------------------
# 0. Provenance constants
# --------------------------------------------------------------------------

#: PR that was under review when the packets were written (read-only target).
PR_UNDER_REVIEW = "youling/lhrm#31"
PR_UNDER_REVIEW_HEAD = "8adcf0bacc45c0feb5c14e65e2a45346dd488b43"
PR_BASE_MAIN = "ee393ca24f9fbf738ac0ed839e99bdc99de6fc3a"

#: The 18 packets, in the order the Architect/manifest lists them.
CHILDREN = [
    "R2_A", "R2_B", "R2_C", "R2_D", "R2_E", "R2_F",
    "R2_G", "R2_H", "R2_I", "R2_J", "R2_K", "R2_L",
    "R2_ADJ1", "R2_ADJ2", "R2_ADJ3",
    "R2_EV1", "R2_EV2", "R2_EV3",
]

#: lane -> (cluster, role) as declared in `REVIEW_SWARM_MANIFEST.md` §2.
LANE_ROLE = {
    "R2_A": ("construct ontology / redundancy", "cluster_review"),
    "R2_B": ("measurement instruments / proxies", "cluster_review"),
    "R2_C": ("datasets / access / rights", "cluster_review"),
    "R2_D": ("statistics / identification / transition laws", "cluster_review"),
    "R2_E": ("belief / partial observability / knowledge", "cluster_review"),
    "R2_F": ("dynamics / hysteresis / pair-state emergence", "cluster_review"),
    "R2_G": ("general dyad scope / ABM / LLM layer", "cluster_review"),
    "R2_H": ("paper positioning / novelty", "cluster_review"),
    "R2_I": ("red-team falsifiers / Gate A-B-C", "cluster_review"),
    "R2_J": ("citation / provenance recheck", "cluster_review"),
    "R2_K": ("cross-lane contradiction map", "cluster_review"),
    "R2_L": ("actionability / next-work-order filter", "cluster_review"),
    "R2_ADJ1": ("PPR / F3 / D7-vs-R3 / Trust adjudication", "adjudication"),
    "R2_ADJ2": ("transition-law / null / geometry / freeze adjudication", "adjudication"),
    "R2_ADJ3": ("meta-claim arbitration (8 items)", "adjudication"),
    "R2_EV1": ("independent evidence check: Gate A/B/C headline", "evidence_check"),
    "R2_EV2": ("independent evidence check: lane J + manifest arithmetic", "evidence_check"),
    "R2_EV3": ("independent evidence check: G-C5 / D-C19 / hysteresis", "evidence_check"),
}

# --------------------------------------------------------------------------
# 1. Record scope: which layout, which section holds the records
# --------------------------------------------------------------------------
#
# `kind` is the layout variant handled by the extractor.
# `sections` is a list of *heading regexes*; a section is in scope when its
# `##`-level heading matches.  Every record must live inside an in-scope
# section.  This is what makes "missed rows" detectable: a packet that puts a
# verdict row outside the declared section fails the completeness assertion.
#
# Layout variants (six, all implemented):
#   block_numbered : `### <id> — title` heading + `N. <field>: value` lines
#                    (also `N. **<field>:** value` and doubled keys
#                     `N. **<field>:** **<field>:** value`)
#   block_bullet   : `**<id> — title**` standalone line + `- <field>: value`
#   table_wide     : markdown tables; columns resolved through COLUMN_ALIASES
#   qblock_h3      : `## ... Q<n> — <question>` + `### \`<field>\`` sub-blocks
#   qblock_bold    : `# Q<n> — <question>` + `**<field>**` blocks
#   qblock_h1      : `# Claim <n> — <title>` + `### \`<field>\`` sub-blocks

RECORD_SCOPE = {
    "R2_A":    ("block_numbered", [r"verdict_matrix"]),
    "R2_B":    ("kv_table",       [r"verdict_matrix"]),
    "R2_C":    ("block_numbered", [r"verdict_matrix"]),
    "R2_D":    ("block_numbered", [r"verdict_matrix"]),
    "R2_E":    ("block_numbered", [r"verdict_matrix"]),
    "R2_F":    ("block_bullet",   [r"verdict_matrix"]),
    "R2_G":    ("block_numbered", [r"verdict_matrix"]),
    "R2_H":    ("table_wide",     [r"verdict_matrix"]),
    "R2_I":    ("table_wide",     [r"verdict_matrix"]),
    "R2_J":    ("table_wide",     [r"verdict_matrix"]),
    "R2_K":    ("table_wide",     [r"verdict_matrix"]),
    "R2_L":    ("block_numbered", [r"verdict_matrix"]),
    "R2_ADJ1": ("qblock_h3",      [r"Q\d+"]),
    "R2_ADJ2": ("qblock_bold",    [r"Q\d+"]),
    "R2_ADJ3": ("qblock_h3",      [r"Q\d+"]),
    "R2_EV1":  ("table_wide",     [r"per_subclaim_table"]),
    "R2_EV2":  ("table_wide",     [r"per_item_table"]),
    "R2_EV3":  ("qblock_h1",      [r"^# Claim \d"]),
}

#: Human label for the record unit, per child.
RECORD_UNIT = {
    **{c: "verdict_matrix_row" for c in CHILDREN[:12]},
    "R2_ADJ1": "adjudication_question",
    "R2_ADJ2": "adjudication_question",
    "R2_ADJ3": "adjudication_question",
    "R2_EV1":  "verification_subclaim",
    "R2_EV2":  "verification_item",
    "R2_EV3":  "verification_claim",
}

#: id pattern used by the packet itself.  Used as a *second* completeness
#: signal: any anchor that does not look like a claim id is reported.
ID_PATTERN = r"^(?:[A-Z]{1,4}-)?(?:C|#)?\d+[a-z]?$|^[A-Z]{1,4}-C\d+[a-z]?$|^\(?[a-z]\)?$"

# --------------------------------------------------------------------------
# 2. The 11 canonical fields
# --------------------------------------------------------------------------
# 10 of them are `REVIEW_CONTRACT.md` §5's mandatory fields.  The 11th,
# `corroboration`, is the §4 hard-rule field (recorded as `independence` in
# lanes I/J/K headers).

FIELDS = [
    "claim_id",
    "claim",
    "source_report",
    "verdict",
    "supporting_refs",
    "strongest_counterevidence",
    "requires_canonical_change",
    "needs_experiment_or_data",
    "duplicate_of",
    "corroboration",
    "recommendation_to_architect",
]

#: Fields the mechanical join consumed, and which therefore must never be
#: truncated in the JSON.  `primary` (the normalised first enum word) is
#: *derived* at matrix-render time and is not a packet field.
JOIN_FIELDS = [
    "claim_id", "claim", "verdict",
    "requires_canonical_change", "corroboration", "recommendation_to_architect",
]

# --------------------------------------------------------------------------
# 3. Column alias registry for the `table_wide` layout
# --------------------------------------------------------------------------
# Order matters: the first matching entry wins, and a column may only be
# claimed once.  Headers are normalised before matching (see
# `normalise_header` in extract_packets.py): markdown emphasis removed,
# text before the first full-width parenthesis kept, lower-cased, spaces and
# `+` collapsed to single spaces.

COLUMN_ALIASES = [
    # --- identity -----------------------------------------------------------
    # Two entries on purpose: an explicit `claim_id` header always wins over a
    # positional `#` / `item` column, so a table that has both is not
    # double-claimed.
    (r"^claim_id$|^claim id$",                        "claim_id"),
    (r"^#$|^id$|^item$|^编号$",                        "claim_id"),
    # --- claim text ---------------------------------------------------------
    (r"^claim$|^claims$|^结论$|^子命题$|^j 的 claim$|^19 的条目$"
     r"|^新发现的 genuine agreement$|^18 的 compatible$|^wo$", "claim"),
    # --- source pointer -----------------------------------------------------
    (r"^source_report|^source report|^指针$|^文件:行|^文件 : 行|^报告声称",
        "source_report"),
    # --- verdict ------------------------------------------------------------
    (r"^verdict$|^我的 verdict$|^判定$",                 "verdict"),
    # --- evidence / counter-evidence ---------------------------------------
    (r"^supporting_refs|^支撑$|^精确引用$|^我的 method", "supporting_refs"),
    (r"^strongest_counterevidence|^最强反证$|^反证"
     r"|^反证 / 缺口$|^决定性检验$",                    "strongest_counterevidence"),
    # --- contract-impact flags ---------------------------------------------
    (r"^requires_canonical_change$|^我的判定 : 是否改 canonical$"
     r"|^我的判定:是否改 canonical$",                      "requires_canonical_change"),
    (r"^needs_experiment_or_data$",                        "needs_experiment_or_data"),
    (r"^duplicate_of$",                                    "duplicate_of"),
    # --- independence -------------------------------------------------------
    (r"^corroboration$|^independence$|^independence_status$|^独立性$"
     r"|^我的独立性判定$",                                  "corroboration"),
    # --- recommendation -----------------------------------------------------
    (r"^recommendation_to_architect$|^recommendation$|^建议$|^结论$",
        "recommendation_to_architect"),
    # --- packed composite ---------------------------------------------------
    (r"^其余字段$|^10 字段摘要$",                          "__composite__"),
]

#: Composite `其余字段` columns pack the four tail fields positionally in the
#: order used by `REVIEW_CONTRACT.md` §5, separated by ` · `:
#:   requires_canonical_change · needs_experiment_or_data · duplicate_of ·
#:   recommendation_to_architect
COMPOSITE_ORDER = [
    "requires_canonical_change",
    "needs_experiment_or_data",
    "duplicate_of",
    "recommendation_to_architect",
]
COMPOSITE_SEPARATOR = "·"

# --------------------------------------------------------------------------
# 4. Section capture registry (the contract-mandated extras)
# --------------------------------------------------------------------------

#: heading regex -> capture key.  First match wins; a section may be captured
#: once.  These are the packet sections the deliverables require to be present.
CAPTURE_SECTIONS = [
    (r"files_audited",                              "files_audited"),
    (r"coverage_statement|覆盖声明",                 "coverage_statement"),
    (r"top_recommendations",                        "top_recommendations"),
    (r"explicit_non_claims",                        "explicit_non_claims"),
    (r"packet_sha_note|decisive_evidence|读了哪些源",
        "provenance_note"),
]

#: The four contract §6 specialty answers.  A section is taken as the
#: specialty block when its heading matches this regex *and* it has exactly
#: four `###` subsections.
SPECIALTY_SECTION_RE = r"必答|专项"
SPECIALTY_SUBSECTION_COUNT = 4

# --------------------------------------------------------------------------
# 5. Sanitisation registry (private chain-of-thought)
# --------------------------------------------------------------------------
# The 18 packets were written to `REVIEW_CONTRACT.md` §7's standard ("no
# private chain-of-thought; only conclusion + evidence chain + uncertainty").
# `extract_packets.py` still runs a deterministic detector over every captured
# string and records each hit with its disposition.  The extractor NEVER
# rewrites captured text: rewriting quoted verdict text would break the
# contract's §4 rule that quotes stay verbatim.  Only whole captured *regions*
# that are pure session state are dropped, and those are listed in
# `PACKET_REGION_EXCLUSIONS` below.
#
# Rule ids -> (regex, what it detects, disposition when matched, why)
SANITISATION_RULES = [
    ("PCOT-1",
     r"我要(?:采纳并加强|修正|给出比[^，。；、]{0,40}?更准的诊断)",
     "first-person stance / self-positioning with no audit content",
     "retained_as_conclusion_text",
     "The surrounding sentence carries the audit content (which lane is right "
     "and why); only the first-person subject is speaker-facing. Deleting a "
     "clause would break a quoted verdict, so the text is kept verbatim and "
     "flagged."),
    ("PCOT-2",
     r"我(?:推翻|推翻 lane|驳回)",
     "first-person authorial-action subject",
     "retained_as_conclusion_text",
     "The proposition itself is the child's verdict on which side prevails. "
     "That is a conclusion, not private reasoning; contract §4 requires the "
     "child's own wording to be preserved."),
    ("PCOT-3",
     r"DRAFT FOR ARCHITECT|DRAFT\b|草稿(?!期)",
     "authoring-session staging state",
     "excluded_by_capture_scope",
     "A staging marker of the writing session, not a verdict. It lives in a "
     "packet header, and packet headers are outside the capture scope "
     "(PACKET_REGION_EXCLUSIONS)."),
    ("PCOT-4",
     r"(?:让我|我先|先让我|下一步我|我打算|我准备|回头再|先放着|待补|TODO|FIXME)",
     "internal deliberation / planning narration / unfilled placeholder",
     "retained_as_uncertainty",
     "The 2 matches are both `待补核实` and both are **quotations of the audited "
     "report's own wording** (`12` §13 action item 5), i.e. evidence about the "
     "audited text, not the child's private note. The 1 `我先` match is lane "
     "`EV1`'s method disclosure (read canonical first, then grep), which "
     "`REVIEW_CONTRACT.md` §5 field 6 requires. **0 captured fields excluded.**"),
    ("PCOT-5",
     r"(?:P\.S\.|PS:|内部讨论|私下|不外传|not for (?:public|publication))",
     "author-private annotation",
     "retained_as_evidence_chain",
     "No genuine match. The `ps:` hits in the corpus are substrings of "
     "`https:` in URLs."),
    ("PCOT-6",
     r"(?:我想|我感觉|我直觉|我猜|我怀疑|我担心|我估计|我大概|我可能是|随便|"
     r"懒得|脑补|凭印象|吐槽)",
     "unverified speculation by the author about their own belief",
     "retained_as_uncertainty",
     "Where present these sit inside `residual_uncertainty` or "
     "`explicit_non_claims`, where the deliverable standard explicitly "
     "permits (and requires) stated uncertainty."),
]

#: Packet regions that are deliberately NOT captured, with the reason.  Listed
#: per child by the extractor into each JSON as `capture_scope.not_captured`.
PACKET_REGION_EXCLUSIONS = {
    "_default": [
        ("packet header block (title / lane / cluster / PR / date / status line)",
         "session metadata; the same facts are captured structurally as "
         "child_id / lane / role / base_sha / pr_under_review"),
        ("preamble and method narration not bound to a required field",
         "no join field consumes it; the method facts that matter are inside "
         "`coverage_statement` and `provenance_note`"),
    ],
    "R2_H": [
        ("§9.x duplicate/synonym tables and §12 A-D external recheck tables",
         "not part of contract §5's per-claim fields"),
    ],
    "R2_I": [
        ("§5 the ten focus-question rulings", "not part of contract §5"),
        ("§6 top_recommendations is captured; §7 explicit_non_claims is captured",
         "no exclusion"),
    ],
    "R2_J": [
        ("§3 the 105-DOI verification log and §4 recomputation sections",
         "evidence detail, not per-claim fields"),
        ("§9 the ten focus answers", "not part of contract §5"),
    ],
    "R2_K": [
        ("§3 sibling-lane citation topology scan", "not a verdict record"),
        ("§6.2 corpus-level duplicate/synonym main table (D-01..D-24)",
         "a corpus-level artefact, not a per-claim field; the three "
         "most-Architect-relevant duplicates are in §6.3 and are part of the "
         "captured specialty answer 4"),
    ],
    "R2_ADJ1": [("§0 decisive_evidence source inventory", "captured as provenance_note")],
    "R2_ADJ2": [("# per_law_disposition_table",
                  "a summary table of the six Q verdicts; the per-law detail "
                  "lives inside the captured Q blocks")],
    "R2_EV1": [("§3-§13 narrative sections",
                "captured as `narrative_sections` verbatim so nothing is lost; "
                "not part of the record set")],
    "R2_EV2": [("§3 doi_resolution_table and §5 verbatim replacement text",
                "replacement text belongs to the PR #31 repair, not to the "
                "review verdict record set; §5.1-§5.11 is reproduced by "
                "`R3_A2` in the repair wave")],
    "R2_EV3": [("§0.1/§0.2 files/coverage", "captured as files_audited / coverage_statement")],
}
