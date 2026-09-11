# Validation Corpus v0.1 — Graded Material Harvest

- Parent issue: `youling/lhrm#16`
- Dispatch: `ARCHITECT_RESEARCH_DISPATCH_V1` (comment `5607914082`, as_of 2026-09-10)
- Work: `youling/lhrm#16@validation-corpus-v0.1-material-harvest`
- Role: Research (Fresh Research, independent harvest)
- Date: 2026-09-11
- Branch: `research/validation-corpus-v0.1`
- File: `docs/validation/VALIDATION_CORPUS_V0_1.md`

## Research independence statement

This harvest was executed as Fresh Research. No future Verifier output was read.
No LHRM mapping was performed. No canonical schema change is proposed.
Materials were selected for discriminative power, including potential to produce
`PARTIAL_MAPPING / MULTI_MAPPING / MAPPING_FAILURE` under the frozen schema.
All representational-challenge notes below are pre-mapping hypotheses, not mapping results.

## Selection method

- Priority: official / public-domain / open-access / stable-source with a stable pointer
  a future verifier can independently access.
- No generative-AI-invented stories. No three-rewrites-of-one-story counting as three.
- No bulk copying of copyrighted text into the repo; pointers + short cleaning notes only.
- Sensitive-content rule: no minors / sexual-violence material selected; bereavement /
  medical / coercive-control themes flagged where present and minimized.
- Verification (2026-09-11): every canonical pointer below was live-fetched
  (HTTP 200 / page load / PDF header) before inclusion.
- Required per-material fields follow the `#16` contract: `material_id / level /
  title / source_family / jurisdiction-culture-period / canonical pointer /
  access_status / copyright-license / approx_length / core_dyad / why_this_level /
  representational_challenges / future_leakage_risk / recommended_cleaning /
  recommended_fact_unit_count / sensitive_content_note`.

---

## L0 — Explicit / Linear / Low-Ambiguity

Target: `Agent / DirectedRelationship / PairState / Action-Event / Environment /
Constraint / Time` stable landing. Two main adults, linear timeline, explicit behavior,
10–40 atomic fact units.

### L0-001 — Official court / tribunal factual narrative

```text
material_id: L0-001
level: L0
title: Miss Z. Carty v Razors and Blades Limited — 2301968/2021 — Judgment and Reasons
source_family: official court / tribunal factual narrative (UK Employment Tribunal, London South, CVP 13 Oct 2023)
jurisdiction / culture / period: England, UK; events 2020-2021 (Covid closures); published 2023
canonical_source_pointer: https://assets.publishing.service.gov.uk/media/655b72e4544aea000dfb30d3/Miss_Z_Carty_v_Razors_and_Blades_Limited_2301968-2021_Judgment_and_Reasons.pdf
  index: https://www.gov.uk/employment-tribunal-decisions (search 2301968/2021)
access_status: open / stable / free (gov.uk + assets.publishing.service.gov.uk; verified HTTP 200, application/pdf, 181424 bytes)
copyright_or_license_note: UK tribunal judgment, Crown copyright, published openly under Open Government Licence; link + fact excerpt only, do not re-host full PDF text
approx_length: 9 pages PDF; ~3500-4500 words incl. law/remedy boilerplate; factual core ~1200-1800 words
core_dyad: Miss Z. Carty (claimant employee) <-> Mr M. Kaye, Development Operations Manager (employer side)
why_this_level: Two-adult employment dyad, linear observable timeline (employed -> Covid closure early 2021 -> no clear dismissal communication -> CAB May 2021 -> claim -> hearing). Facts are explicit actions (shop closed/reopened, wages/holiday unpaid, no contact). Minimal interiority in facts section.
representational_challenges: employment dates, closure/reopening events, payment/non-payment facts, who-said-what-when, CAB visit as timestamp anchor; must separate unfair-dismissal / wrongful-dismissal / redundancy-pay holdings from facts
future_leakage_risk: HIGH if uncleaned — operative judgment (paras 1-8, GBP 2719.64 award, recoupment/interest notices) leaks outcome/trajectory
recommended_cleaning: strip orders 1-8, award calculation, recoupment/interest notices, legal-tests section, post-hearing procedure; keep Introduction + employment/closure/non-payment/CAB/claim chronology; optionally role-label names
recommended_fact_unit_count: 22
sensitive_content_note: none — wage/employment dispute only; Covid context
```

### L0-002 — Official inquiry / institutional case summary

```text
material_id: L0-002
level: L0
title: Midshires Care Limited (24 001 994) — Local Government and Social Care Ombudsman decision
source_family: official inquiry / institutional case summary (government ombudsman published decision statement)
jurisdiction / culture / period: England, UK adult social care; events 24 Jul-Dec (hospital admission, suspension, texts 3 Aug / 9 Aug, invoice Nov, complaints Dec); decision 05 Nov 2024
canonical_source_pointer: https://www.lgo.org.uk/decisions/adult-care-services/charging/24-001-994
access_status: open / stable / free (official permanent decisions database; full text live-fetched 2026-09-11)
copyright_or_license_note: (c) LGSCO; openly published and anonymised (Mrs X / Mrs A / office manager); link + short description only, no bulk copy
approx_length: 23 numbered paras; ~1300-1600 words
core_dyad: Mrs X (daughter/representative cancelling care) <-> office manager of care agency (counterparty via text/phone)
why_this_level: Strictly linear dated message behavior (24 Jul admission -> suspension + 2-day fee -> manager text "terminate by 9 Aug" -> 3 Aug cancel text -> GBP 1330.83 invoice -> Nov-Dec complaint stages). Contract clause quoted verbatim. Even the disputed phone call is two reported-speech claims, no metaphor.
representational_challenges: date arithmetic (3 Aug -> 9 Aug = 6 days vs 5-day vs 14-day clause), speech acts (suspend vs cancel vs terminate), invoice chain (GBP 1330.83 -> GBP 441 -> refund), three-stage complaint escalation; explicit obligation/notice-period reasoning
future_leakage_risk: MEDIUM-HIGH — Analysis (paras 19-20) + Agreed action (GBP 500 + apology + refund) + Final decision leak evaluation/trajectory
recommended_cleaning: strip role/powers boilerplate (paras 2-3), law/Reg-19 (paras 5-6), Analysis (19-20), Agreed action (21-22), Final decision (23); keep complaint summary (para 1) + What happened (paras 7-18); optionally strip mother's-death sentence (para 10) or keep as single timestamp with care flag; source anonymisation already done
recommended_fact_unit_count: 20
sensitive_content_note: low — bereavement context (Mrs A died September; invoice addressed to deceased mother "upsetting"); flag for annotator care, not exclusion; no minors, no sexual violence
```

### L0-003 — Open-access scholarly / clinical case narrative

```text
material_id: L0-003
level: L0
title: Hypertension management and drug-related problems. A case report of the 23-year history of Mr. Jonas — Treciokiene et al., Exploratory Research in Clinical and Social Pharmacy (2023)
source_family: open-access scholarly / clinical case narrative (peer-reviewed OA journal + PMC)
jurisdiction / culture / period: Lithuania, primary care / pharmacy; adult male followed 1998-2021 in same practice (GP changed 2016); published 2023
canonical_source_pointer: https://pmc.ncbi.nlm.nih.gov/articles/PMC10433230/
  DOI mirror: https://doi.org/10.1016/j.rcsop.2023.100313 (PMID 37601158, PMCID PMC10433230)
access_status: open / stable (PMC full text live-fetched 2026-09-11)
copyright_or_license_note: (c) 2023 The Authors, CC BY-NC-ND 4.0; link + fact excerpt only, do not ingest full article
approx_length: full article ~5000-6000 words + Fig.1/Fig.2 timelines + Tables 1-3; Case presentation (Sec.2) ~600-900 words
core_dyad: Mr. Jonas (white Lithuanian man, 41 at 1998 diagnosis -> 65 in 2021, chief executive) <-> GP / primary-care practice (longitudinal prescriber)
why_this_level: Explicit dated linear prescribing/visit behavior (1998 BP 150/110 + atenolol -> 2000 dry mouth/thirst 160/100 obese glucose 5.9 -> Mar 2001 nebivolol + nitrendipine -> mono->triple switches -> from 2010 fixed-dose combos -> 2007-08 fenofibrate/atorvastatin/rilmenidine windows -> 2010 thyroidectomy/levothyroxine -> 2019 T2D/metformin; 207 GP visits ~9/year). Minimal metaphor; interiority confined to Table 2 interview (strippable).
representational_challenges: medication start/stop/switch events, BP readings as measurements, comorbidity onsets, OTC concomitants, adherence gaps (20-40-day gaps 2004-05); long span requires windowing to 10-40 units without inventing causality
future_leakage_risk: HIGH if uncleaned — Sec.3-5 (PCNE classifications, Table 3, Discussion/Conclusion "never reached target BP", pharmacist-intervention judgments) leak clinical judgment and future-risk trajectory
recommended_cleaning: keep Sec.2 Case presentation + Fig.1/Fig.2 + Table 1 end-state meds; strip Abstract, Background, Sec.3 PCNE Table 3, Sec.4 Discussion, Sec.5 Conclusion, Funding/COI, References; strip Table 2 interview OR keep max 2-3 explicit adherence-behavior rows flagged; RECOMMENDED window 1998-2008 initiation phase (~20 units); do not use full 23-year span as single L0 item
recommended_fact_unit_count: 28 (full Sec.2) or 20 (1998-2008 window, preferred for L0)
sensitive_content_note: none — adult only; pseudonym "Mr. Jonas" with written consent stated; routine primary-care data handling
```

---

## L1 — Subjective / Everyday / Mild Ambiguity

Target: `Observation != Belief != latent state`. Subjective feelings, indirect expression,
quotes, single main timeline + core dyad, 20–80 atomic units.

### L1-001 — Memoir / interview / oral-history

```text
material_id: L1-001
level: L1
title: "Never Say Goodbye": Remembering the Love Between Danny and Annie Perasa — StoryCorps interviews (2004 + 2006, rebroadcast 2021)
source_family: memoir / interview / oral-history excerpt (StoryCorps; originals in Library of Congress American Folklife Center, StoryCorps collection)
jurisdiction / culture / period: USA, Brooklyn NY, working-class; recorded 2004-08-11 and Feb 2006; rebroadcast 2021-08-20
canonical_source_pointer: https://storycorps.org/stories/never-say-goodbye-remembering-the-love-between-danny-and-annie/
access_status: open-access, no login; page incl. audio (~5:12) + full transcript; live-fetched 2026-09-11
copyright_or_license_note: (c) StoryCorps; free to view/read/listen; not public-domain, not CC; short excerpt under fair use only, retain link/attribution
approx_length: transcript ~950 words + intro ~200 words; usable core ~950 words
core_dyad: Danny Perasa (husband, OTB clerk) <-> Annie Perasa (wife, nurse); arc: first date/proposal (1978) -> married ritual (daily love notes) -> terminal diagnosis Jan 2006 -> final home interview -> death one week later + remembrance
why_this_level: Everyday domestic ritual (kitchen-table notes, ice-cream/water prompts), single dyad, linear timeline, heavy first-person evaluation ("shelter", "color TV", "busted old radio") and direct reported speech / letters read aloud. Ideal Observation vs Belief split (note-on-table vs "she loves me / marriage is shelter" vs latent devotion / anticipatory grief).
representational_challenges: metaphor ("color television", "beautiful song from a busted old radio"), nested quotes (Danny quoting himself, Annie reading Valentine letter), belief vs observation ("she'll do well after I pass", "never another Annie", "hope not that I'll live"), retrospective (2004 memory of 1978) retold under 2006 terminal illness; interviewer framing must stay attributed
future_leakage_risk: MEDIUM-HIGH — famous StoryCorps/NPR staple + animation, widely quoted; high pretraining likelihood; mitigate with excerpt + paraphrase probe, not verbatim-recall test
recommended_cleaning: transcript block only (DP/AP); strip header/share UI, Recent Stories footer, photo captions, 2013-update link text, editorial intro except 2-sentence provenance; keep speaker attribution; target ~700-900 words
recommended_fact_unit_count: 48
sensitive_content_note: terminal pancreatic cancer, dying, funeral/casket planning, grief; Annie died 2021 of COVID-19 (page note); bereavement handling, no graphic medical detail; no minors, no sexual violence
```

### L1-002 — High-quality long-form journalism / documented narrative

```text
material_id: L1-002
level: L1
title: "I haven't lived with my husband for 15 years – we're still happily married" (Margaret and Peter) — BBC News / Woman's Hour
source_family: high-quality long-form journalism / documented narrative
jurisdiction / culture / period: UK-Australia; London vs Brisbane; published 2025-09-07
canonical_source_pointer: https://www.bbc.com/news/articles/c5y21nvd56ko
access_status: open-access, stable BBC News URL, no paywall (live-fetched 2026-09-11)
copyright_or_license_note: (c) 2025-2026 BBC, all rights reserved; excerpt core dyad thread under fair use/fair dealing with attribution; do not copy full article
approx_length: full page ~850-950 words; core Margaret-Peter thread ~550-650 words (rest: celebrity examples + counsellor advice)
core_dyad: Margaret Murphy (wife, Education Officer Royal College of Surgeons, London) <-> Peter (husband, former full-time doctor, Brisbane family home); arc: Australia family life + 4 children -> Margaret age 57 PhD applied linguistics -> children leave -> London move 15 years ago -> 1 visit per 12-18 months + phone disclosure
why_this_level: Everyday mild ambiguity. No crime/investigation. Central tension is subjective: "happily married" despite 15-year intercontinental separation; loneliness vs fulfillment co-exist. Belief statements ("fulfilling marriage", "another dimension") vs observables (separate flats, visit frequency, "I tell Peter everything"). Tests co-residence-absent != relationship-absent.
representational_challenges: subjective language ("wonderful experience", "smooth sailing", "lonely", "love vs like"), multi-source quotes (Margaret / listener Kerry / counsellor Ammanda Major — must not merge), belief-vs-observation on fidelity/happiness/causality ("talking regularly" as cause), generic-vs-specific (3% ONS stat + celebrity LAT examples must not attach to dyad)
future_leakage_risk: LOW — recent Sep 2025 human-interest, non-viral, low verbatim-memorization risk
recommended_cleaning: keep headline/dek, Margaret biography, decision, disadvantages, communication routine, airport photo caption as provenance; remove 3% stat box (unless needed), all celebrity paragraphs, related-links, Kerry anecdote, Relate bullet list (or keep 1 line as excluded non-dyad context); target ~550 words
recommended_fact_unit_count: 42
sensitive_content_note: none as subjects (four children referenced as now-adult, left home); themes: ageing, late-career change, loneliness, chosen marital separation; no graphic content; no minors, no sexual violence
```

### L1-003 — Realistic short fiction / public-domain literary excerpt

```text
material_id: L1-003
level: L1
title: "The Gift of the Magi" by O. Henry (1905)
source_family: realistic short fiction / public-domain literary excerpt
jurisdiction / culture / period: USA, New York City, early-20th c.; magazine 1905
canonical_source_pointer: https://www.gutenberg.org/ebooks/7256
access_status: open-access, public domain (USA), HTML/EPUB/TXT (live-fetched 2026-09-11)
copyright_or_license_note: Public domain (USA), Project Gutenberg eBook-No. 7256 (credits Susan Ritchie); may copy/re-use under Gutenberg License with header retained
approx_length: full story ~2100 words
core_dyad: Della (wife) <-> Jim (husband, James Dillingham Young); <24h Christmas Eve arc in $8/week flat: Della sells long hair ($20) for platinum fob chain for Jim's gold watch; Jim sells watch for tortoise-shell combs for Della's hair; evening mutual revelation
why_this_level: Canonical L1 — everyday domestic economy ($1.87, pennies, grocer), single timeline, single dyad + narrator; narratorial subjectivity + interiority + dialogue; each acts on false belief the other still holds the treasured object; belief-revision at reveal
representational_challenges: narrator moralizing ("wisest gifts", "magi") vs character belief; Della pride/shame; direct dialogue at reveal + self-talk vs narrator summary; pre-reveal beliefs vs post-reveal observations; counterfactual wishes
future_leakage_risk: HIGH — extremely famous, ubiquitous in pretraining, twist widely known; do NOT test ending prediction; use for belief-tracking / quote attribution / observation-belief split; consider held-out paraphrase or sentence-order probe
recommended_cleaning: TXT/HTML body between Gutenberg START/END markers; strip license header/footer; keep full story (twist required for belief-revision test); target ~2000 words
recommended_fact_unit_count: 60
sensitive_content_note: none — poverty theme, non-graphic hair-cutting, mild religious framing (Magi/Christ); no minors, no sexual violence
```

---

## L2 — Multi-Agent / Nonlinear / Concealment

Target: third parties / family / institutional context, deception / concealment /
disputed belief / reconciliation, nonlinear time, divergent agent knowledge-time,
50–150 atomic units.

### L2-001 — Complex court / family-law factual record

```text
material_id: L2-001
level: L2
title: Sharland v Sharland [2015] UKSC 60 — fraudulent non-disclosure in matrimonial financial remedy
source_family: complex court / family-law / civil-criminal factual record (UK Supreme Court)
jurisdiction / culture / period: England & Wales; marriage 1993-2010, trial Jul 2012, resumed hearing Apr 2013, EWCA 2014, UKSC 14 Oct 2015
canonical_source_pointer: https://caselaw.nationalarchives.gov.uk/uksc/2015/60
access_status: open-access, official, stable (National Archives Find Case Law; full neutral-citation judgment paras 1-44 live-fetched 2026-09-11)
copyright_or_license_note: UK Crown copyright / Open Justice Licence; free access and re-use with attribution per National Archives terms; not public-domain; use neutral text only
approx_length: ~9000-11000 words judgment + quoted High Court / Court of Appeal history
core_dyad: Alison Sharland (wife/appellant) <-> Charles Sharland (husband/respondent, AppSense software entrepreneur)
key_third_parties: 3 children (17/15/12 at trial; elder son severe autism); Goldman Sachs / AppSense Holdings Ltd / invited IPO banks; rival valuation experts; Sir Hugh Bennett (trial judge); Court of Protection proceedings; solicitors; Moore-Bick / Macur / Briggs LJJ
why_this_level: Dyad + family/org context; fraud/concealment central; multi-year history + valuation dispute + resumed hearing + appeal chain = nonlinear reconstruction needing 50-150 units
representational_challenges: knowledge-time divergence (Jul 2012 consent order on "no IPO on cards" vs Jan-Aug 2012 IPO planning in full swing, pre-sealing press leak, no IPO by Apr 2013); dishonest evidence / undisclosed bank pitches misleading both valuers; disputed belief (majority vs Briggs LJ dissent on materiality; Livesey warning reading); nonlinear time (marriage/separation/trial/agreement/press/Jan-2013 affidavit/Apr-2013/EWCA/UKSC); counterfactual judicial reasoning ("what would I have done") as belief, not fact
future_leakage_risk: HIGH — leading authority, heavily cited, textbooks/summaries, likely in pretraining; mitigate with National Archives neutral text only, own segmentation, holdout split
recommended_cleaning: UKSC judgment only; exclude press/commentary; redact children to roles (Child-1/2/3, Elder Son), minimize health detail; split procedural dicta (fresh action vs appeal, s.31F(6), FPR) from factual narrative; flag counterfactual reasoning as belief
recommended_fact_unit_count: 95
sensitive_content_note: minors present by age only; severe autism + Court of Protection context — minimize medical detail to judgment wording; no sexual content/violence
```

### L2-002 — Biography / historical relationship reconstruction

```text
material_id: L2-002
level: L2
title: Harriet Taylor Mill — Stanford Encyclopedia of Philosophy entry (biographical + authorship controversy + correspondence-based reconstruction)
source_family: biography / historical relationship reconstruction
jurisdiction / culture / period: Victorian England; 1807-1858, relationship arc 1830-1858; entry first publ. 2002, substantive revision 29 Jul 2022
canonical_source_pointer: https://plato.stanford.edu/entries/harriet-mill/
access_status: open-access, stable, official (SEP; Sections 1-5 + Bibliography live-fetched 2026-09-11)
copyright_or_license_note: (c) Metaphysics Research Lab, Stanford; open to read, not CC / not public-domain; paraphrase-derived atomic facts under fair use/research with citation; no large republication
approx_length: ~12000-15000 words main entry excl. bibliography
core_dyad: Harriet Hardy Taylor Mill (1807-1858) <-> John Stuart Mill
key_third_parties: John Taylor (first husband 1826-1849); children Herbert, Algernon ("Haji"), Helen ("Lily"); Rev W. J. Fox; Mill family estrangement; Carlyles, Bain, Eliza Flower, Louis Blanc, Morley/Laski network; East India Company / Unitarian circle
why_this_level: Dyad + dense third-party context; concealment/disputed-belief core (nightly visits facilitated by husband's club absence, separate residence from 1833, forbidden dedication pasted only in gifted Principles copies, radically conflicting ability reports, disputed co-authorship of Principles / On Liberty / Enfranchisement); multi-year + flashback via Autobiography/letters/retrospective assessments
representational_challenges: knowledge-time divergence (what each knew 1830-1849 vs Autobiography/On Liberty dedication claims vs later stylometric re-attribution); socially concealed intimacy while married; hidden dedication; destroyed/missing letters as absent evidence; disputed belief (Mill "deification" vs Carlyle/Bain/Borchard/Laski detraction vs balanced middle; minimalist vs maximalist influence schools); nonlinear time (1826 marriage, 1830 meeting, 1833 separation, 1841 illness, 1848 dedication refusal, 1849 widowhood, 1851 remarriage, 1858 Avignon death, posthumous 1859 On Liberty + later scholarship)
future_leakage_risk: HIGH — SEP widely crawled, stable IDs, likely in training; mitigate with 2022-revision snapshot, own fact-writing, avoid Wikipedia/Hayek/Jacobs sprawl
recommended_cleaning: SEP entry only; do not ingest linked Complete/Collected Works full text; separate (a) dated life events, (b) contemporaries' quotes as attributed beliefs, (c) authorship evidence as disputed; minimize children to roles; flag Schmidt-Petri et al. 2022 stylometry as method-contested, not ground truth
recommended_fact_unit_count: 105
sensitive_content_note: adult non-monogamous/adulterous relationship by Victorian standards, chronic illness/tuberculosis, death, bereavement; factual, non-salacious; no graphic medical content; no minors / sexual violence
```

### L2-003 — Realistic novella / long short story

```text
material_id: L2-003
level: L2
title: The Aspern Papers by Henry James (1888 novella, Venice)
source_family: realistic novella / long short story
jurisdiction / culture / period: Anglo-American expatriate Venice, late-19th c.; publ. 1888
canonical_source_pointer: https://www.gutenberg.org/ebooks/211
access_status: open-access, stable, public-domain (Gutenberg page + EPUB 150kB / TXT 229kB live-fetched 2026-09-11)
copyright_or_license_note: Public domain (USA) (James d.1916); Gutenberg transcription (Judith Boss / David Widger); free use with credit line; use plain-text version for segmentation
approx_length: novella ~30000-35000 words (9 chapters + frame)
core_dyad (for LHRM use): unnamed narrator-lodger (Aspern scholar/biographer) <-> Juliana Bordereau (aged former lover guarding Aspern letters); alternate framing: narrator <-> Miss Tita (courtship-deception dyad)
key_third_parties: Jeffrey Aspern (deceased poet, absent centre); Miss Tita; Mrs Prest (introducer/confidante); Venetian household (servants/gardener/gondolier); publisher/biographer milieu
why_this_level: Sustained bilateral concealment (false name, lodger/flower-garden pretext, considered feigned courtship of Tita; Juliana rations access to letters/past); disputed belief (Aspern affair nature, papers' value/authenticity, narrator reliability/ethics); decades-old past intruding via letters/relics = flashback + confrontation beats
representational_challenges: knowledge-time divergence (what narrator knows vs what Juliana/Tita know he wants; gradual motive reveal); withheld letters as hidden objects; ambiguous marriage/sale offer; disputed belief on liaison and paper fate; nonlinear time (present quest intercut with reconstructed decades-old past via memory/gossip/letters; final reversal reframes earlier scenes); unreliable narration
future_leakage_risk: VERY HIGH — canonical James, widely crawled, adaptations/summaries; mitigate by segmenting from primary text only, avoiding introductions/SparkNotes, own paraphrase units
recommended_cleaning: Gutenberg plain text only; chapter-wise chunking; tag each unit as observed-action vs reported-memory vs letter-content vs narrator-inference; do not import Wikipedia note beyond provenance; keep romance/coercion-pressure beats factual and non-graphic (source has no sexual explicitness)
recommended_fact_unit_count: 100
sensitive_content_note: no minors, no sexual violence; adult themes: deceptive courtship proposal, elderly vulnerability, death/mourning, privacy violation / biographical predation; minimize romantic-pressure detail to concealment modelling needs
```

---

## L3 — Branching / Nested / High-Expressivity

Target: dream / fantasy / counterfactual / unreliable narration, time travel /
alternate timeline / memory reconstruction, metaphor-rich nonlinear prose, same person
across reality / memory / dream / plan / hypothetical; at least one Human–Human
dyad trajectory.

### L3-001 — Dream / unreliable-narrator literary work

```text
material_id: L3-001
level: L3
title: The Yellow Wallpaper — Charlotte Perkins Gilman (1892)
source_family: dream / unreliable-narrator literary work (Project Gutenberg short story)
jurisdiction / culture / period: USA, 1892
canonical_source_pointer: https://www.gutenberg.org/ebooks/1952
  direct text: https://www.gutenberg.org/files/1952/1952-h/1952-h.htm
access_status: openly accessible, no login, EPUB/HTML/TXT (live-fetched 2026-09-11)
copyright_or_license_note: Public domain (USA); author d.1935, publ.1892; Gutenberg terms (free re-use in USA, check local law elsewhere)
approx_length: ~6000 words / 51KB plain text
core_dyad: Narrator (unnamed wife / new mother / secret diarist) <-> John (husband / physician / rest-cure enforcer); trajectory: care/control -> prohibition of work/writing -> nursery confinement (barred windows) -> concealment -> obsession -> final inversion
why_this_level: Canonical unreliable narration — first-person secret journal, hallucination vs perception, dream-like wallpaper figures, metaphor-rich nonlinear prose, plan vs reported fact diverge; still one identifiable marital dyad
representational_challenges: belief vs perception vs hallucination (wallpaper woman, smell, creeping); reliability (claims John loving/caring while describing coercive confinement); nested worlds (remembered house / described room / wallpaper world / inferred motive); counterfactual branching (what John says will happen vs what narrator does secretly)
future_leakage_risk: HIGH — ending widely known; model may inject final creeping / fainted John without textual warrant if windowed; enforce blind forward windowing
recommended_cleaning: plain text; strip Gutenberg header/footer + illustration captions; keep full story intact (do not excerpt); normalize wall-paper/wallpaper; keep Jennie/Mary/baby as supporting, not core dyad
recommended_fact_unit_count: 35-45
sensitive_content_note: postpartum distress, coercive medical control, confinement, deteriorating mental health; no erotic detail; mental-health framing care; no minors / sexual violence
```

### L3-002 — Time-travel / alternate-history / SF relationship narrative

```text
material_id: L3-002
level: L3
title: Looking Backward, 2000 to 1887 — Edward Bellamy (1888)
source_family: time-travel / alternate-history / SF relationship narrative (Project Gutenberg utopian SF novel)
jurisdiction / culture / period: USA, 1888
canonical_source_pointer: https://www.gutenberg.org/ebooks/624
  direct text: https://www.gutenberg.org/files/624/624-h/624-h.htm
access_status: openly accessible, no login, EPUB/HTML/TXT (live-fetched 2026-09-11)
copyright_or_license_note: Public domain (USA); author d.1898, publ.1888; Gutenberg terms
approx_length: full novel ~75000-80000 words / 456KB plain text — TOO LARGE for validation as whole; excerpt strategy required (see cleaning)
core_dyad: Julian West (1887 Bostonian, time-sleeper) <-> Edith Leete (2000 host's daughter / love interest); shadow dyad: Julian <-> Edith Bartlett (1887 fiancee, Edith Leete's great-grandmother, same first name); romance + memory reconstruction across 113-year sleep
why_this_level: Time-displacement + alternate-timeline + memory/dream branching — hypnotic sleep 1887->2000, explanatory utopia dialogues, Ch.27-28 dream-return where 2000 reads as dream, identity confusion between two Ediths; same person across reality/memory/dream/plan/hypothetical while dyad persists
representational_challenges: nested time layers (birth narrative / 1887 Boston / 2000 Boston / dream-1887-return); belief vs dream vs plan (characters debate mad vs dreaming vs displaced); same-name conflation (Edith Bartlett vs Edith Leete — entity-merge risk); hypothetical exposition in present tense as fact
future_leakage_risk: MEDIUM-HIGH — utopian system + Edith-descendant twist + dream-return resolution may be known; window chapters, do not feed synopsis
recommended_cleaning: DO NOT use full novel. L3 slice: Ch.1-4 (sleep + awakening) + Ch.13-14 / Ch.25-26 (Edith romance reveal) + Ch.27-28 (nightmare return + awakening); strip Author's Preface, Gutenberg header/footer, Marxist-archive mirrors; keep Dr. Leete as facilitator only
recommended_fact_unit_count: 45-60 for recommended slice (350+ if full novel — not recommended)
sensitive_content_note: outdated 19th-c gender / paternalist utopian views, class polemic, anxiety/dream distress; no erotic detail; no minors / sexual violence
```

### L3-003 — Myth / strange tale / magical-realism / fantasy relationship narrative

```text
material_id: L3-003
level: L3
title: Orpheus and Eurydice — Ovid, Metamorphoses, Book X opening (1717 Dryden/Garth et al. English translation)
source_family: myth / strange tale / magical-realism / fantasy relationship narrative (Internet Classics Archive / MIT Classics)
jurisdiction / culture / period: Augustan Rome, Ovid c.8 CE; translation England 1717
canonical_source_pointer: https://classics.mit.edu/Ovid/metam.10.tenth.html
access_status: openly accessible, no login, HTML + text-only download (live-fetched 2026-09-11; opens with "The Story of Orpheus and Eurydice")
copyright_or_license_note: Latin original public-domain by antiquity; 1717 English translation public-domain; MIT 1994-2009 educational archive; excerpt with attribution, no site-frame redistribution
approx_length: target episode ~2500-3000 words English (full Book X page 10000+ words incl. unrelated tales)
core_dyad: Orpheus (Thracian bard / husband) <-> Eurydice (bride / Naiad companion / shade); trajectory: wedding -> snakebite death -> katabasis plea -> conditional release -> backward-look violation -> second loss -> mourning; gods/Hades are grantors, not core dyad
why_this_level: Mythic/fantasy branching — living world / Hades / return road as nested worlds, divine conditional "do not look back" as counterfactual branch, metaphor-rich archaic prose, song-within-story suspending Hell; same two persons across alive / shade / revived / re-lost states
representational_challenges: world-switching (upper air / Tenarian road / Stygian shore / ascent; dyad changes ontological status); belief vs performative song vs granted fact (Orpheus argument moving Furies/Tantalus/Ixion/Sisyphus as causal); counterfactual condition (if look back then void — leakage-prone); archaic metaphor (saffron robe, hissing torch, bloodless shades — must not literalize as separate entities)
future_leakage_risk: HIGH — myth ending universally known; model may assert second death before ascent text warrants it; cut window before backward-look passage in annotation
recommended_cleaning: CRITICAL — excerpt ONLY "Thence, in his saffron robe..." through "...incessant he complains, And Hell's inexorable Gods arraigns." + 7-days shore mourning. EXCLUDE remainder of same URL: Cyparissus, Ganymede, Hyacinthus, Pygmalion, Cinyras/Myrrha, Venus/Adonis, Atalanta (incest / non-consensual / erotic content, out of dyad scope). Strip TOC nav, Commentary links, Download footer.
recommended_fact_unit_count: 22-30 for Orpheus-Eurydice episode only
sensitive_content_note: target episode only: sudden viper-bite death, grief, underworld imagery, double death; no sexual violence in target episode; risk ONLY if scrolled past episode into Myrrha/Cinyras incest + Adonis/Venus erotic tales — excluded above; no minors in target episode
```

---

## Cross-level coverage map

| level | material | source family | est. units | leakage | readiness |
|---|---|---|---|---|---|
| L0 | L0-001 Carty tribunal | court | 22 | high (outcome) | needs cleaning (strip orders/remedy) |
| L0 | L0-002 LGSCO care | inquiry/summary | 20 | med-high | needs cleaning (strip analysis/action) |
| L0 | L0-003 Mr. Jonas | OA clinical | 20-28 | high (judgment) | needs cleaning + windowing (1998-2008) |
| L1 | L1-001 StoryCorps | oral history | 48 | med-high | needs cleaning (transcript only) |
| L1 | L1-002 BBC LAT | journalism | 42 | low | needs cleaning (core thread only) |
| L1 | L1-003 Magi | public-domain fiction | 60 | high (fame) | direct-use (full story) |
| L2 | L2-001 Sharland | family-law record | 95 | high | needs cleaning (facts vs dicta) |
| L2 | L2-002 Harriet Mill | biography/SEP | 105 | high | needs cleaning (events vs quotes vs disputed) |
| L2 | L2-003 Aspern Papers | novella PD | 100 | very high | needs cleaning (chapter chunk + tag) |
| L3 | L3-001 Yellow Wallpaper | unreliable PD | 35-45 | high | direct-use (full story) |
| L3 | L3-002 Looking Backward | SF time-travel PD | 45-60 slice | med-high | needs cleaning (chapter slice only) |
| L3 | L3-003 Orpheus/Eurydice | myth PD | 22-30 episode | high | needs cleaning (episode excerpt only) |

Style spread per level: satisfied (court / inquiry / clinical; oral-history /
journalism / fiction; family-law / biography / novella; unreliable / SF / myth).

## Recommended Fixture 001–003 (start here)

Per dispatch ("recommend which 3 to start with as Fixture 001–003") and `#15`
(one short official-court fixture first, 10–30 units, two adults, minimal sensitivity):

1. **Fixture 001 — L0-002 (LGSCO Midshires Care, 24 001 994).**
   Shortest stable official narrative (~20 units after cleaning), two-adult dyad,
   linear dated texts, lowest sensitivity of the L0 set, no windowing ambiguity.
   Best first black-box run per `#15` (official primary source, stable case ID).
2. **Fixture 002 — L1-003 (Gift of the Magi, Gutenberg 7256).**
   Public-domain, direct-use full story (~60 units), single dyad + single day,
   canonical Observation-vs-Belief revision test (false-belief gifts). Leakage is
   high but harmless for representation testing (do not test ending prediction).
3. **Fixture 003 — L0-001 (Carty tribunal, 2301968/2021).**
   Second official-court confirmation with different dyad type (employment vs care
   contract), still L0-linear (~22 units), stable gov.uk PDF. Pairs with 001 to
   check cross-case stability before moving to L1-subjectivity (L1-001/L1-002)
   and L2/L3 stress.

Rationale: 001 establishes the official-source pipeline; 002 adds subjectivity
without adding multi-agent or branching load; 003 checks L0 generalization.
L2/L3 deliberately deferred until Verifier protocol is frozen.

## Readiness for next-round verification

- Direct-use after trivial strip: L1-003, L3-001.
- Usable after specified cleaning/windowing (no new collection needed):
  L0-001, L0-002, L0-003 (windowed), L1-001, L1-002, L2-001, L2-002, L2-003,
  L3-002 (sliced), L3-003 (episode only).
- None of the 12 includes any mapping result (per prohibition).
- All 12 keep original narrative style; no "pre-translation into LHRM".

## What was NOT done (per dispatch)

- No sentence-by-sentence LHRM mapping.
- No schema completeness claim; no new-parameter proposal.
- No `Candidate Minimal Directed Basis v0.1` evaluation.
- No Verifier-output reading (none exists yet at harvest time).

## Verification log

- 2026-09-11, executor live-fetched all 12 canonical pointers:
  gov.uk PDF (HTTP 200, application/pdf, 181424 bytes),
  lgo.org.uk decision (full text), PMC10433230 (full text),
  StoryCorps transcript + audio page, BBC LAT article, Gutenberg 7256/211/1952/624,
  National Archives UKSC 2015/60 (paras 1-44), SEP harriet-mill, MIT Classics Ovid X.
- No bulk text ingested into repo. Pointers above are the durable references.
