# Fixture 001 — L0-001 Carty Employment Tribunal 冻结事实包

状态：**CANDIDATE FOR ARCHITECT REVIEW / NO LHRM MAPPING**  
父任务：`#19`；验证 lanes：`#20/#21/#22`。  
准备者：LHRM Project Architect（2026-09-14）。原 LGSCO source 因 Eye rights gate 保持 fail-closed，本包按 `#19` durable source-switch 改用公开 OGL tribunal source。  

## 1. Source / provenance

- Case: `Miss Z. Carty v Razors and Blades Limited`
- Case number: `2301968/2021`
- Tribunal: Employment Tribunal, London South
- Judgment and Reasons date: 31 October 2023；hearing 13 October 2023
- official PDF: `https://assets.publishing.service.gov.uk/media/655b72e4544aea000dfb30d3/Miss_Z_Carty_v_Razors_and_Blades_Limited_2301968-2021_Judgment_and_Reasons.pdf`
- official index family: `https://www.gov.uk/employment-tribunal-decisions`
- licence/access: official gov.uk publication / Crown copyright / Open Government Licence; LHRM stores only paraphrased factual units and canonical pointer, not a full-text mirror.
- extraction boundary: **only `Findings of Fact`, paras 13–23**. Orders, legal tests, conclusions, holdings, remedies and award amounts are excluded from this fixture.

### Core dyad for this fixture

The relationship-relevant human pair is treated as:

`Miss Z. Carty <-> her 2020 line manager / employer-side human contact`

Mr M. Kaye's later tribunal representation role is procedural and is not imported into the relationship fact stream unless a later benchmark explicitly tests legal-process context.

## 2. Epistemic / freeze rules

1. `message was sent` and `message content is true` are different propositions.
2. Where the tribunal explicitly says the underlying ownership/management fact is unclear, keep it `unknown` even though the communication itself is established.
3. Claimant evidence is not silently upgraded when the Findings section merely reports it without an explicit acceptance cue; such units may remain `alleged` with attribution.
4. Where the judge says `I accept`, the accepted proposition may be marked `adjudicated` for this fixture.
5. Legal conclusions after para 23 are future leakage and are excluded.
6. Do not map any unit to LHRM constructs during material preparation.
7. Three independent Verifiers must consume the same merged exact version.

## 3. Atomic fact units

| fact_id | paraphrased_fact | source_paragraph(s) | event_time | knowledge_time_by_agent | fact_status | speaker/source attribution | future_leakage_note |
|---|---|---|---|---|---|---|---|
| C001 | Miss Carty had been employed by Razors and Blades Limited since 26 September 2017 as an evening cleaner. | 13 | from 2017-09-26 | both employment sides from start | adjudicated | Tribunal finding | Do not import later dismissal holding. |
| C002 | Her normal schedule was 2 hours per day, 3 days per week (6 hours weekly), and she was paid the applicable minimum wage. | 13 | pre-2020 ongoing | both employment sides | adjudicated | Tribunal finding | — |
| C003 | Around the time she stopped working, her line manager had suggested she might not be an employee, while the written contract indicated employee status. | 13 | around cessation / 2020 | claimant + manager at/around communication | disputed | line-manager suggestion contrasted with contract/Tribunal finding | Keep the suggestion as a disputed communication, not truth. |
| C004 | On 23 March 2020, the line manager texted Carty that the shop was closed until further notice because of Covid-19 and that she did not need to clean unless told otherwise. | 14 | 2020-03-23 | claimant upon receipt; manager at send | adjudicated | manager text, recorded in Tribunal finding | Do not infer permanent termination. |
| C005 | Shortly afterward, Carty was told she could not be paid until 1 April 2020 because of the business's financial impact from Covid-19. | 15 | late Mar 2020 | claimant upon communication | adjudicated | employer-side communication as recorded by Tribunal | The causal explanation is attributed communication. |
| C006 | On 1 April 2020 she received pay covering work up to 23 March 2020. | 15 | 2020-04-01 | claimant and payer at payment | adjudicated | Tribunal finding | Exclude later legal finding about arrears. |
| C007 | Around 3 April, Carty asked whether the employer would use the Coronavirus Job Retention Scheme for later payments; the employer said it was looking into government support and recommended she apply to her local council. | 16 | ~2020-04-03 | each party as exchange occurred | adjudicated | claimant request + employer response, Tribunal finding | Message content does not prove actual support application. |
| C008 | Carty made further attempts to clarify her employment situation and, on 9 April, asked for a letter setting out that situation. | 16 | 2020-04-09 and surrounding period | employer on receipt; claimant at send | adjudicated | Tribunal finding | — |
| C009 | On 23 April, she asked whether she was on furlough and received no response. | 16 | 2020-04-23 | claimant knows no response after waiting; employer request receipt if delivered | adjudicated | Tribunal finding | No-response fact does not itself specify intent. |
| C010 | On 11 July 2020, the line manager asked whether Carty could return to work from the following Tuesday and sent further messages trying to contact her. | 17 | 2020-07-11 onward | claimant on receipt; manager at send | adjudicated | manager messages, Tribunal finding | — |
| C011 | Carty's evidence was that she continued asking for furlough because another lockdown remained possible. | 17 | Jul 2020 period | claimant at request; employer if received | alleged | claimant evidence reported in Findings | Preserve attribution because this sentence is framed as claimant evidence rather than an explicit `I accept`. |
| C012 | On 2 August 2020, the line manager emailed Carty saying the business had been sold to a new owner. | 18 | 2020-08-02 | claimant upon receipt; manager at send | adjudicated | manager email occurrence/content | This establishes the message, not the truth of the sale. |
| C013 | The Tribunal record says it was unclear whether the business had actually been sold or whether only new management had been installed. | 18 | underlying change around Aug 2020 | unknown to Tribunal on evidence available | unknown | Tribunal explicit uncertainty | Do not choose either branch in replay. |
| C014 | On 4 August 2020, the line manager emailed that Carty's contract was being terminated and that a further written communication would be sent shortly. | 18 | 2020-08-04 | claimant upon receipt; manager at send | adjudicated | manager email occurrence/content | Do not import later legal effective-date conclusion. |
| C015 | Carty replied the same day that she had not known about the management change, asked why she had not been furloughed, and said she would wait for the promised dismissal letter. | 18 | 2020-08-04 | manager on receipt; claimant at send | adjudicated | claimant email, Tribunal finding | This is evidence of her stated knowledge at that time. |
| C016 | The findings state that no further dismissal letter appears to have been sent to Carty. | 19 | after 2020-08-04 | claimant observes non-receipt over time | adjudicated | Tribunal finding with cautious wording | Preserve `appears`; do not strengthen to impossible/certain beyond record. |
| C017 | Carty said, and the judge accepted, that she was unsure whether she had been dismissed or remained employed; she still held the shop keys and had not been asked to return them. | 19 | Aug 2020 onward | claimant during uncertain period | adjudicated | claimant evidence explicitly accepted + Tribunal observation | Do not backfill later dismissal conclusion into this belief state. |
| C018 | From 28 September 2020, Carty began claiming Jobseeker's Allowance and looked for alternative daytime work, including fortnightly job-centre visits and nanny websites. | 20 | from 2020-09-28 | claimant contemporaneously | adjudicated | Tribunal finding | Do not infer she believed the evening employment definitively ended. |
| C019 | Around 15 January 2021, she obtained new employment paying about £360 per week. | 20 | ~2021-01-15 | claimant upon obtaining role | adjudicated | Tribunal finding | — |
| C020 | The judge accepted Carty's evidence that she had not known she could bring an unfair-dismissal/employment-tribunal claim. | 21 | before May 2021 advice | claimant lacked this knowledge | adjudicated | claimant evidence explicitly accepted | This is knowledge-state evidence, not a judgment about reasonableness. |
| C021 | The respondent business closed again in early 2021; by May, businesses were reopening and Carty still had not received clarification about whether she remained employed, so she visited Citizens Advice. | 21 | early 2021 to May 2021 | claimant by May | adjudicated | Tribunal finding | Exclude later legal assessment of delay. |
| C022 | At/after Citizens Advice, Carty learned that an employment-tribunal claim might be possible; she contacted ACAS, supplied employment documents, and was told she had been dismissed on 4 August 2020. | 21 | May 2021 | claimant as advice received | adjudicated | Tribunal finding / advice communication | The ACAS/advice statement is what she was told, not imported as legal truth for earlier slices. |
| C023 | On 4 May 2021, Carty contacted RXB Barbers to raise complaints about her employment. | 22 | 2021-05-04 | business on receipt; claimant at send | adjudicated | Tribunal finding | — |
| C024 | In a 25 May reply, Mr Hernani D'Abreu told Carty that a newly registered business had taken over from September 2020, that her employment had been terminated the prior year in writing, and that her role was unavailable with the new company. | 22 | 2021-05-25 | claimant upon receipt; D'Abreu at send | adjudicated | D'Abreu email occurrence/content | Treat as attributed claims; it does not overwrite C013/C016. |
| C025 | The Tribunal record explicitly says it was unclear whether the claimed business takeover was correct; the assertion that termination had been done formally in writing also sits alongside the earlier finding that no further letter appeared to have been sent. | 22 + 19 | underlying 2020 events / evaluated in record | unresolved across evidence | disputed | Tribunal uncertainty + cross-record inconsistency | Keep contradiction/uncertainty visible for evidence-lineage testing. |
| C026 | Carty received an early-conciliation certificate and submitted her tribunal claim on 2 June 2021. | 23 | 2021-06-02 | claimant + institutions at filing | adjudicated | Tribunal finding | This is the final chronology point retained; all later legal conclusions are excluded. |

## 4. Frozen temporal / knowledge boundaries

- `K0` (before 2020-03-23): normal employment arrangement applies; no shutdown message yet.
- `K1` (2020-03-23 to 2020-08-01): Carty knows work is suspended/unclear and repeatedly seeks payment/furlough/status clarification; no termination message yet.
- `K2` (2020-08-02): she has received the manager's `business sold` claim, but the underlying ownership/management fact remains unknown.
- `K3` (2020-08-04 onward): she has received a termination email but is waiting for promised further written confirmation and is explicitly uncertain whether she is dismissed or still employed.
- `K4` (May 2021): after advice, she learns of the possibility of a tribunal claim and is told that dismissal occurred on 4 August 2020; this later knowledge must not be inserted into `K1–K3`.

## 5. Downstream validation rule

This package is **input**, not a mapping result.

Every Verifier must map all C001–C026 against the same frozen LHRM schema. A unit may legitimately yield `PARTIAL_MAPPING / MULTI_MAPPING / UNKNOWN / MAPPING_FAILURE`; Verifiers must not repair the fixture or invent constructs during the test.
