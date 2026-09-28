# X08 — Rights-safe empirical validation architecture

**Status:** RESEARCH_CANDIDATE / policy architecture input  
**As of:** 2026-09-28  
**Authority:** `youling/lhrm#30` Round-3 exploration queue X08  
**Base branch:** `research/round3-exploration-v0.1` from `main@ee393ca24f9fbf738ac0ed839e99bdc99de6fc3a`  
**Scope:** Separate raw-data execution from AI-readable reasoning while preserving dataset-specific rights, confidentiality, access, and output restrictions.  
**Non-claims:** not legal advice; no restricted data downloaded; no DUA accepted; no Eye/Juece mutation; no permission inferred from “open”, “public-use”, or “aggregate” wording.

---

## 1. Executive verdict

A single boolean such as `AI_OK=true/false` is not adequate for LHRM empirical validation.

The current policy landscape supports a **multi-plane architecture**:

```text
AI Design Plane
    |
    | code/specification only
    v
Raw Deterministic Execution Plane
    |
    | candidate output
    v
Policy-specific Output Release Gate
    |
    | only outputs explicitly permitted for this dataset/project
    v
Approved Aggregate Evidence Plane
    |
    v
AI Analysis / LHRM evidence synthesis
```

The critical boundary is the **Policy-specific Output Release Gate**. HRS and UAS explicitly allow some derived analytic output to be shared with an LLM while prohibiting microdata. ICPSR is type- and study-specific and may require prior permission. SHARE is materially stricter and states that AI/ML-generated derivative datasets, models, or analytical outputs remain subject to the same usage restrictions as the original data.

Therefore:

> **“Microdata cannot go to an LLM” does not imply “AI cannot participate in the project”; and “output is aggregated” does not imply “AI may read it.”**

Every dataset needs its own current policy record.

---

## 2. Verified policy facts

### 2.1 HRS — split between microdata and derived output is explicit

Official source: Health and Retirement Study, **AI and LLM Use Policy**, updated 2026-08-04.  
Source: https://hrsdata.isr.umich.edu/data-products/ai-llm-use-policy

Verified:
- LLMs/AI may not be used to manage, process, or analyze HRS-distributed microdata, including RAND HRS and Gateway Harmonized HRS.
- Public-facing documentation, codebooks, study-level metadata, and group/population estimates may be used with AI.
- An LLM may write Stata/Python/R analysis code **if no HRS microdata are uploaded**.
- Derived analytic output such as **model coefficients or summary statistics may be shared with an LLM**, provided no HRS microdata are uploaded.
- AI-assisted development tools that automatically index a working directory containing HRS microdata are not allowed.

**Architecture implication:** HRS is a strong positive example for:
`AI design -> non-AI raw execution -> aggregate release -> AI analysis`.

### 2.2 UAS — same core separation, plus air-gapped exception path

Official source: Understanding America Study, **AI and Data Use** / FAQ.  
Source: https://uasdata.usc.edu/

Verified:
- UAS microdata may not be shared with LLMs or other AI tools under existing data use agreements.
- Public-facing documentation, codebooks, study-level metadata, and group/population estimates may be used under the stated non-retention conditions.
- AI code generation is allowed if no microdata are uploaded.
- Derived analytic output, including model coefficients and summary statistics, may be shared with an LLM if no UAS microdata are uploaded.
- AI-assisted development tools must not index directories containing UAS microdata.
- Some air-gapped AI projects may be considered case-by-case.

**Architecture implication:** UAS supports the same plane separation, while also showing that `AIR_GAPPED_AI` must be a separate policy state rather than silently treated as allowed.

### 2.3 ICPSR — type-specific and permission-specific

Official source: ICPSR, **Policy on the Use of Large Language Models (LLMs) and Other Forms of AI**, approved 2024-12-11 and published 2025-01-20.  
Source: https://www.icpsr.umich.edu/sites/ICPSR/news/can-i-use-large-language-models-and-other-ai-such-as-chatgpt-google-gemini-etc-with-icpsr-data

ICPSR classifies:
- **Type 1**: retains user data / may train on it.
- **Type 2**: institutionally licensed, non-retaining.
- **Type 3**: Type 2 plus isolation in a secure network with no Internet access.

Verified:
- Type 1: no ICPSR dataset may be shared.
- Type 2: ICPSR may permit use with public-use datasets; prior contact/permission is required.
- Type 3: ICPSR may permit public-use and restricted-use datasets if consistent with security requirements and approved.
- Restricted secure-download data require an isolated environment and security-plan compliance.
- ICPSR VDE/PDE currently do **not** provide an LLM option.
- ICPSR metadata are treated separately.
- Study-specific terms may be stricter than ICPSR’s general policy.

Concrete stricter example: **Add Health / ICPSR 21600** explicitly bars LLMs and other AI tools from managing, processing, or analyzing both public-use and restricted-use data.  
Source: https://www.icpsr.umich.edu/web/ICPSR/studies/21600/terms

**Architecture implication:** an ICPSR-level policy record is insufficient. The release gate must apply:
`study-specific terms > archive-general terms`.

### 2.4 ICPSR restricted enclaves already implement an output-vetting pattern

Official source: ICPSR/DSDR restricted-data documentation.

Verified:
- Restricted data may be used through Secure Download, VDE, or PDE depending on study.
- VDE/PDE outputs are reviewed for disclosure risk before release.
- Approved researchers may share/discuss **vetted** results outside the enclave.

This is structurally similar to the LHRM Output Release Gate even when no LLM is involved.

**Architecture implication:** output vetting is not an AI-specific invention; it is already a standard controlled-data pattern.

### 2.5 SHARE — no blanket “aggregate output is AI-safe” inference

Official source: SHARE-ERIC, **Conditions of Use**, last updated 2026-04-30.  
Source: https://share-eric.eu/data/data-access/conditions-of-use

Verified:
- SHARE access is individual and for scientific use under its conditions.
- Users must prevent unauthorized access and third-party data processing.
- Applications that are not fully self-administered are prohibited unless it can be verified that no data are stored or processed by others.
- Local AI-model training may be allowed only locally and exclusively for scientific purposes under the stated conditions.
- **Any derivative datasets, models, or analytical outputs generated through AI or machine-learning processes remain subject to the same usage restrictions as the original SHARE data.**

**Architecture implication:** do not generalize the HRS/UAS “coefficients/summary statistics may go to an LLM” rule to SHARE.

For SHARE, `aggregate_output_to_external_ai` must remain:
`UNKNOWN_OR_REQUIRES_EXPLICIT_POLICY_CLEARANCE`
unless the current terms or SHARE support provide a dataset/project-specific basis.

---

## 3. Required policy model

Do not use one `AI_OK` flag.

Minimum candidate record:

```text
DatasetAIPolicy =
{
  dataset_id,
  source_owner,
  policy_snapshot_date,
  policy_source_url,
  study_specific_terms_url,

  access_class,
  raw_microdata_ai_policy,
  code_generation_policy,
  metadata_ai_policy,
  aggregate_output_ai_policy,
  local_airgapped_ai_policy,
  external_nonretaining_ai_policy,
  third_party_indexing_policy,

  execution_environment_requirements,
  output_vetting_required,
  reidentification_prohibition,
  redistribution_constraints,
  derivative_output_constraints,

  human_permission_required,
  unresolved_questions,
  provenance
}
```

Recommended value vocabulary per policy field:

```text
PERMITTED
PROHIBITED
PERMISSION_REQUIRED
TYPE2_ONLY
TYPE3_ONLY
LOCAL_ONLY
VETTED_OUTPUT_ONLY
STUDY_SPECIFIC
UNKNOWN
NOT_APPLICABLE
```

A field remains `UNKNOWN` until an applicable current policy or written permission resolves it.

---

## 4. Plane architecture

### Plane A — AI Design Plane

Allowed inputs should be limited to material explicitly cleared for AI use:
- public documentation;
- codebooks;
- study-level metadata;
- public publications;
- synthetic/mock schemas;
- approved aggregate estimates.

Outputs:
- analysis plans;
- code templates;
- variable mappings;
- model specifications;
- preregistered tests.

**Hard rule:** generated code is not permission to expose data.

### Plane B — Raw Deterministic Execution Plane

Runs the approved deterministic analysis against microdata.

Expected properties when required by terms:
- no external LLM endpoint;
- no AI editor/file indexing over protected directories;
- no unapproved telemetry;
- access restricted to approved researchers/environment;
- reproducible code and environment hash;
- logs that do not leak row-level values;
- storage/destruction rules matching the DUA.

This plane can be:
- local secure workstation;
- approved secure-download environment;
- VDE/PDE;
- approved institutional enclave.

### Plane C — Policy-specific Output Release Gate

No result crosses automatically.

The gate checks:
1. dataset-specific terms;
2. study-specific terms;
3. requested output class;
4. disclosure/re-identification risk;
5. whether formal output vetting is required;
6. whether AI use of that output is explicitly permitted;
7. whether the project requires prior written approval.

Possible terminal decisions:

```text
RELEASE_TO_AI
RELEASE_TO_HUMAN_ONLY
VETTING_REQUIRED
PERMISSION_REQUIRED
REDACT_AND_RECHECK
HOLD
REJECT
```

### Plane D — Approved Aggregate Evidence Plane

Only stores artifacts cleared by Plane C.

Examples:
- coefficients;
- uncertainty intervals;
- pre-approved aggregate tables;
- disclosure-cleared model diagnostics;
- machine-readable metadata about the run;
- hashes/pointers to code and execution provenance.

**Important:** “aggregate” is a data shape, not a permission state.

### Plane E — AI Analysis Plane

AI may:
- interpret cleared outputs;
- compare candidate laws;
- detect inconsistencies;
- draft research memos;
- propose next tests.

AI may not infer that hidden/raw data are accessible merely because aggregate results exist.

---

## 5. LHRM empirical-run contract

Each empirical validation run should produce a durable **run manifest** without exposing protected microdata:

```text
EmpiricalRunManifest =
{
  run_id,
  dataset_id,
  policy_snapshot,
  approved_project_scope,
  analysis_code_sha,
  environment_fingerprint,
  executed_by,
  execution_time,

  input_schema_hash,
  row_count_band_or_approved_count,
  requested_outputs,

  output_gate_decision,
  output_vetting_pointer,
  released_artifacts,
  withheld_artifacts,

  statistical_checks,
  provenance,
  limitations
}
```

The manifest should be safe to store in GitHub only if every field is allowed by the applicable terms.

No row-level examples, rare-cell values, free-text respondent content, or reconstructable microdata are included unless explicitly authorized.

---

## 6. Dataset policy examples

| Dataset / archive | Raw microdata to external AI | AI code generation without microdata | Aggregate/model output to AI | Air-gapped AI | Required handling |
|---|---|---:|---|---|---|
| HRS | PROHIBITED | PERMITTED | PERMITTED if no microdata | policy-specific | keep microdata outside AI-indexed dirs |
| UAS | PROHIBITED | PERMITTED | PERMITTED if no microdata | PERMISSION_REQUIRED / case-by-case | contact UAS for planned AI use |
| ICPSR generic public-use | Type 1 PROHIBITED | generally separable from data | STUDY_SPECIFIC | Type2/3 may be permitted | contact ICPSR before data-to-AI use |
| ICPSR restricted secure download | Type 1/2 not sufficient | separable | STUDY_SPECIFIC / gate required | TYPE3_ONLY + approval | security plan + approval |
| ICPSR VDE/PDE | no LLM currently available | outside-data code design possible | VETTED_OUTPUT_ONLY before leaving enclave; AI permission still separate | not currently available in enclave | staff output review |
| Add Health via ICPSR 21600 | PROHIBITED for data processing/analysis | metadata/support-material use separate | do not infer permission | PROHIBITED unless terms change | study-specific prohibition overrides generic ICPSR |
| SHARE | external third-party processing generally fail-closed | design with public docs only | **no blanket clearance**; AI/ML-generated outputs retain original restrictions | LOCAL_ONLY may be possible under conditions | fully self-administered scientific environment; apply SHARE terms |

---

## 7. Architect decisions enabled by X08

### X08-A — accept five-plane separation

`ACCEPT_AS_ARCHITECTURE_CANDIDATE`

The project should not treat AI access as all-or-nothing. Raw execution and AI reasoning can be separated.

### X08-B — add Output Release Gate

`ACCEPT_AS_REQUIRED_CONTROL`

This is necessary because:
- HRS/UAS explicitly permit some derived output;
- ICPSR requires type/study/permission checks;
- SHARE prevents the blanket assumption that all derivatives are AI-readable.

### X08-C — rights metadata must be fielded, not boolean

`ACCEPT`

At minimum separate:
`access | ordinary reuse | AI/microdata | AI/aggregate-output | air-gapped/local AI | robots/technical controls | privacy/ethics | provenance`.

This extends the earlier PR #37 ruling.

### X08-D — deterministic execution may remain AI-independent

`ACCEPT`

An LLM can design code without receiving the protected data. A non-AI process can execute it in the approved environment. This is explicitly compatible with the HRS/UAS code-generation FAQ pattern.

### X08-E — no automatic release from aggregate status

`HARD FAIL-CLOSED RULE`

`aggregate != permitted_for_AI`.

The release decision comes from current applicable terms or written approval, not from a statistical aggregation threshold invented by LHRM.

---

## 8. Human/action gates before real restricted-data validation

No restricted run should start until all applicable items are resolved:

1. researcher/institution eligibility;
2. DUA/project approval;
3. IRB if required;
4. approved storage/execution environment;
5. AI policy classification for the exact dataset;
6. study-specific override check;
7. output-release/vetting procedure;
8. whether AI may receive the intended outputs;
9. destruction/retention requirements;
10. whether the intended LHRM use remains inside the approved scientific purpose.

These are real authority/rights gates, not architecture TODOs.

---

## 9. Final X08 packet

### VERIFIED_FACTS
- HRS and UAS prohibit LLM exposure of microdata while explicitly allowing AI code generation without microdata and AI use of derived coefficients/summary statistics under their stated conditions.
- ICPSR distinguishes LLM types and requires permission; study-specific terms can be stricter.
- ICPSR VDE/PDE use output vetting and currently provide no LLM option.
- Add Health’s ICPSR terms explicitly prohibit AI/LLM use for managing, processing, or analyzing its data.
- SHARE requires strict third-party/self-administered controls and keeps AI/ML-derived datasets/models/analytical outputs under original restrictions.

### NEGATIVE_RESULTS
- There is no archive-wide rule that “public-use data are safe for ChatGPT”.
- There is no general rule that “aggregate output is safe for an LLM”.
- “No LLM on raw data” does not imply that AI-assisted code design is forbidden.

### OPEN_GAPS
- Dataset-by-dataset output-release terms for the X03 candidates.
- Whether specific ICPSR/HARP/NCHAT project terms allow a particular Type 2/3 setup.
- Whether SHARE would permit external AI analysis of non-AI-generated, publication-safe aggregates without additional clarification.

### ARCHITECTURE_IMPLICATIONS
- Add a policy-specific Output Release Gate between raw execution and AI analysis.
- Replace boolean AI-rights fields with a multi-axis policy record.
- Keep raw-data execution reproducible and AI-independent by default.
- Make study-specific policy override archive-general policy.

### NON_CLAIMS
- This memo does not grant data access.
- It does not approve any restricted dataset for LHRM.
- It does not provide legal advice.
- It does not claim that every aggregate statistic is disclosure-safe or AI-permitted.

### SOURCE POINTERS
- HRS AI/LLM policy: https://hrsdata.isr.umich.edu/data-products/ai-llm-use-policy
- UAS AI/Data Use: https://uasdata.usc.edu/
- ICPSR LLM policy: https://www.icpsr.umich.edu/sites/ICPSR/news/can-i-use-large-language-models-and-other-ai-such-as-chatgpt-google-gemini-etc-with-icpsr-data
- ICPSR Add Health 21600 terms: https://www.icpsr.umich.edu/web/ICPSR/studies/21600/terms
- ICPSR restricted data/output vetting: https://www.icpsr.umich.edu/sites/dsdr/restricted-data
- SHARE Conditions of Use: https://share-eric.eu/data/data-access/conditions-of-use
