# The multiplacement register, stage B3

**Basis: the assembly of record.** `tools/assemble.py B3 --supersede --accept-sub-label --families out/families.jsonl` on 1,212 accepted returns (the four halves of B0192 and B0927 in fleet ids, J at QB3-003), figures by `out/_analysis/b3_check.py --tag record`. The trial versions written while QB3-003 was open are kept under superseded names.

Rule 0's log read as a measurement: pass 1, corpus copies.

**The rate.** 0.158 of corpus lines place more than one theme (2866 records; 394 lines place three). 0 lines are empty. The per-reader rates and the funnel are in `agent_report-B3.md`.

## The pair table

The next table lists the twenty most frequent (primary, additional) pairs, with the readers and rooms they span and how many readers predicted the pair as their hardest.

| rank | primary | additional | count | readers | rooms | predicted by |
|---|---|---|---|---|---|---|
| 1 | T3-009 | T3-043 | 114 | 112 | 83 | 22 |
| 2 | T3-005 | T3-021 | 114 | 113 | 92 | 245 |
| 3 | T3-021 | T3-005 | 59 | 56 | 50 | 245 |
| 4 | T3-001 | T3-032 | 48 | 46 | 34 | 6 |
| 5 | T3-014 | T3-152 | 39 | 37 | 32 | 10 |
| 6 | T3-038 | T3-021 | 34 | 34 | 27 | 13 |
| 7 | T3-028 | T3-027 | 34 | 34 | 23 | 2 |
| 8 | T3-010 | T3-151 | 32 | 32 | 27 | 26 |
| 9 | T3-028 | T3-089 | 30 | 30 | 20 | 2 |
| 10 | T3-004 | T3-020 | 28 | 26 | 20 | 6 |
| 11 | T3-010 | T3-149 | 27 | 27 | 26 | 58 |
| 12 | T3-023 | T3-032 | 27 | 27 | 22 | 13 |
| 13 | T3-005 | T3-087 | 24 | 24 | 19 | 7 |
| 14 | T3-002 | T3-033 | 24 | 24 | 22 | 24 |
| 15 | T3-023 | T3-097 | 24 | 24 | 17 | 12 |
| 16 | T3-006 | T3-068 | 24 | 24 | 19 | 15 |
| 17 | T3-010 | T3-150 | 22 | 22 | 17 | 8 |
| 18 | T3-023 | T3-095 | 22 | 22 | 19 | 21 |
| 19 | T3-028 | T3-088 | 21 | 21 | 15 | 2 |
| 20 | T3-009 | T3-105 | 20 | 20 | 14 | 6 |

Every pair in the table recurs across many readers and rooms; each is a boundary the scheme has not drawn, and stage C1 reads this table first. T3-005/T3-021 appears in both orders.

**Against the predictions.** The readers' most predicted pairs: T3-005/T3-021 by 245; T3-010/T3-149 by 58; T3-001/T3-095 by 48; T3-010/T3-151 by 26; T3-001/T3-023 by 26; T3-009/T3-073 by 25; T3-002/T3-033 by 24; T3-009/T3-043 by 22. Pairs in the top twenty that readers also predicted often: those with "predicted by" above twenty in the table.

## The justifications, read

I read 40 `why_not_one` texts, one per reader, drawn by seed 20261015 (`out/_analysis/b3_why_not_one_sample_*.tsv`). The next table counts them by class.

| class | texts |
|---|---|
| material genuinely spans two themes | 40 |
| scheme lacks a theme for this | 0 |
| reader hedging | 0 |
| restatement of both gates being satisfied (a defect) | 0 |

Every text names an act in the material that the single placement would leave out (a thanks beside a celebration, quiet repair beside a called defence, a chat's decisions carried back beside the move to the chat). None restates the gates. Three (iastate t03, frc t04, ohio t04) also name a theme that is not on their line; one (malaysia t04) is short but still names the acts.

## Per-theme exception load

The next table lists themes placed as `additional` at least ten times, ordered by additional ÷ primary.

| theme | as additional | as primary | ratio |
|---|---|---|---|
| T3-089 | 30 | 6 | 5.00 |
| T3-152 | 41 | 15 | 2.73 |
| T3-066 | 10 | 6 | 1.67 |
| T3-153 | 26 | 19 | 1.37 |
| T3-195 | 14 | 12 | 1.17 |
| T3-088 | 32 | 30 | 1.07 |
| T3-119 | 10 | 11 | 0.91 |
| T3-032 | 79 | 88 | 0.90 |
| T3-043 | 131 | 159 | 0.82 |
| T3-141 | 14 | 17 | 0.82 |
| T3-097 | 37 | 46 | 0.80 |
| T3-055 | 14 | 21 | 0.67 |
| T3-072 | 34 | 55 | 0.62 |
| T3-068 | 33 | 55 | 0.60 |
| T3-150 | 50 | 94 | 0.53 |

T3-089 and T3-152 stand out: each is placed far more often beside another theme than alone. Before C1 decides whether either is a modifier, an overlapping construct or a missing boundary, it should read their designation rules and supporting concepts.

**The empties.** 0 corpus lines place no theme. Rule 0's characterisation of empties therefore has nothing to describe.

**Screen** (section 3.1): read values whole 17624, theme-block 29; no `label-only`; multi lines without their record or with an empty `why_not_one`: 0; lines reduced to their primary: 0.

**What these figures license.** The readers share an architecture with me and with each other, so a figure here bounds whether the instrument decides, not whether it is right.
