# Expectations against the ledger and the verdicts (stage E1)

Written at E1b-07, 27 October 2026, from `audit-E1/expectations.py` and its output, `expectations.json`. `sealed/EXPECTATIONS.jsonl` holds one line per analysed room (705). Each line names the elements and arrows the room was expected to instantiate and those expected to be absent, with the source of each expectation (the implications of C5, the propositions and the placements).

A room's evidence on an element is its accepted return lines on that element, from the first return and the re-check, with the last ruling of each line:
- **Taken up:** an accepted instantiate, restrict, add-condition, add-step or link line.
- **Contradicted:** an accepted contradict line.
- **Absent:** only an accepted absent line.
- **Untested:** no line.

The score is **in-sample throughout**: the expectations were written from the same rooms whose return scores them, and the uncited concept ids are computed by script, not held out.

## The replication score

| outcome | expectations |
|---|---|
| met | 8,034 |
| failed: absent where it was expected | 575 |
| failed: taken up where absence was expected | 87 |
| untested: no line | 944 |

**The replication score is 0.924** (8,034 met of 8,696 met or failed).

**By verdict**, the first return's (both readers agreeing, else split):

| verdict | score | met | failed |
|---|---|---|---|
| composes | 0.933 | 1,443 | 104 |
| composes with residue | 0.917 | 4,703 | 425 |
| split | 0.933 | 1,846 | 133 |
| cannot tell | 1.0 | 40 | 0 |
| does not compose | 1.0 | 2 | 0 |

**By branch**, the score runs from 0.887 (F16) to 0.964 (F04). The 229 rooms in no branch score 0.919. Every branch's score is in `expectations.json`.

**The two failures, by element.**
- **Expected absent, taken up:** C01, decided order, in 81 rooms. This is the largest single failure. The return finds decided order in many rooms the coding did not.
- **Expected present, absent:** A04 (62), A08 (61), A06 (59), A13 (52) and A19 (48). In those rooms, the return's only accepted word on the arrow is that it is absent.

**Stage D5's survival figures per branch**, from the record and never from the canvas, are in `survival-D5.md` and `branches-D5.jsonl` (`work_remained` re-read for the 476 rooms in a branch, agreeing with the field in 248). They stand beside these scores. D5's reading of `work_remained` is an open defect (line 100), so no score here is set against survival.

## The field's entries

The field model handed over three entries at C4a (`sealed/FIELD.jsonl`). Over the 705 rooms:

| entry | taken up | contradicted | absent | no line | D3's ruling |
|---|---|---|---|---|---|
| P21 (members say an agreement cannot bind every placer) | 166 | 0 | 490 | 49 | standing (D3a-26, rule 11): shown in the rooms' own lines |
| P22 (rooms contest which version of the work is kept) | 223 | 0 | 463 | 19 | standing (D3a-06, rule 11): shown in the rooms' own lines |
| A21 (an agreement, or the making of terms, brings the disclaimer) | 112 | 0 | 567 | 26 | standing with a bound (D3a-27, rule 11): counted in the rooms' own lines |
| the model's other 48 standing elements and arrows, mean per element | 382.6 | 0.1 | 235.3 | 87.0 | |

The tentative mark drew answers, but fewer than the model's other elements. All three were taken up in 112 to 223 rooms, and none was contradicted. Each is absent in more rooms than the mean element, so the return speaks of them less often.

## The onset contrast

`contrast.md` (A1, recomputed at A1b-20) sets two sides: 131 early rooms and 61 late, with a held-size comparison of 41 early and 12 late. Stage C2 recorded each arrow's `early_late` counts.

**Rule 6, the denominators before any gap:**
- 19 arrows carry the counts. The late side holds 0 to 15 rooms per arrow (95 over all 19), and the early side 4 to 93 (818).
- No arrow's late side is large enough to read a gap. The pooled figures (578 of 818 early, 54 of 95 late) are not independent, because the same rooms recur across arrows. So no gap is read.

**A1's expectations:**
- *Late rooms organize around finding room; their organizing lives are shorter; early rooms name rivals more; the held-size comparison keeps the first difference and loses the third.*
- They are **untested** by these counts. They are neither held nor failed.
- The contrast is a boundary condition that the model's terms could not test on this record, not a covariate.
