# Handback, stage B3: the fleet

Written at B3b, 2026-10-12. Figures come from the assembly of record (`tools/assemble.py B3 --supersede --accept-sub-label --families out/families.jsonl`) and `out/_analysis/b3_check_record.json`. The reports are `fidelity-B3.md`, `position-B3.md`, `multiplacement_register-B3.md` and `agent_report-B3.md`; the record of every step is `notes-B3.md`.

**What these figures license.** The readers share an architecture with me and with each other, so a figure here bounds whether the instrument decides, not whether it is right.

## The fleet as built and run

- **Allocation.** Seed 20261015 (under `:redraw2`; the connectivity gate forced 2 redraws). The cap is 15 positions and 180,000 bytes of item text a packet (J, QB3-001). R = 2. No exemplars were served, and the warm-up stayed in reserve.
- **Batches and readers.** The allocator computed 1,210 batches, one reader each. B0192 and B0927 failed six tries each. The handler split them into halves in room ids; under J at QB3-003 I rebuilt the halves in fleet ids as B0192c, B0192d, B0927c and B0927d. The record holds 1,212 batches and 1,212 readers, and the room-batch graph is one component on what the fleet returned.
- **Coverage, from the batches.** Every one of the 705 rooms and 7,844 second-order themes of the analysed set has two returns, one per replicate. There are 17,653 pass-1 lines: 15,688 corpus readings, 1,210 duplicate copies and 755 gold copies. No item is unreturned.
- **Replies.** The dispatch logged 1,303 replies. 87 failed and were sent again, 72 of them because they cited a concept from another item. Of the 454 off-item concepts in failed replies, 453 belong to a neighbouring item of the same packet, mostly in `also_present`. No accepted line cites a concept outside its item. Cost was 33.75 USD over the five dispatch records.

## Gold, against stage B2 and the floor

All 755 gold copies came back. The next table compares them with B2's nine frozen-scheme readings of the same items.

| set | copies | fidelity | primary | B2 fidelity, same copies | B2 primary, same copies |
|---|---|---|---|---|---|
| group 1 | 72 | 0.637 | 0.833 | 0.625 | 0.812 |
| group 2 | 683 | 0.646 | 0.814 | 0.632 | 0.800 |
| whole fleet | 755 | 0.645 | 0.816 | 0.631 | 0.801 |

The fall in fidelity is −0.014 (95% interval −0.031 to +0.003). The floor is 0.193, from `stability-B2.md`. Gold did not fall, and no gold item's own fall reaches the floor. Per batch and per reader: `fidelity-B3.md`.

## Agreement

Agreement is between the two replicates over all 7,844 items, as `notes-B2.md` defines it: Jaccard on placement sets, so `["T3-004"]` against `["T3-004","T3-011"]` scores 0.5. Alpha uses distance 1 − Jaccard.

| Jaccard | exact set | primary | alpha |
|---|---|---|---|
| 0.786 | 0.703 | 0.838 | 0.782 |

Corpus-wide Jaccard sits at the stability floor (0.807): most of what the readers split on is the arm's own variation. The family that disagreed most is G18, politics, history and hate symbols (Jaccard 0.552 over 99 items), then G15, pacts and envoys between rooms (0.582). Per family and per theme, with presence agreement and kappa: `agent_report-B3.md`.

## The position curve and the second pass

The next table gives each outcome's change across 14 positions, its interval and the fit's sensitivity. The tolerance, declared before fitting, is 0.10.

| outcome | change over 14 | 95% interval | sensitivity |
|---|---|---|---|
| agreement | +0.003 | −0.015 to +0.022 | 0.027 |
| multi rate | +0.017 | −0.001 to +0.035 | 0.026 |
| arguable rate | +0.040 | +0.017 to +0.063 | 0.033 |

Agreement holds across the batch. The arguable rate rises, inside the tolerance; it is in `defects.jsonl` as an unresolved diagnostic.

The second pass changed 0.01% of lines. All 1,210 duplicates agree with their first copy, because the readers recognised the repeat: 911 copy the first `why` word for word. So the duplicate measured recall here, not within-reader instability.

## Multiplacement

The multi rate is 0.158 over corpus lines. Per reader it is 0 for at least a quarter of readers, 0.15 at the median, 0.23 at the 75th percentile, 0.38 at the 90th and 0.85 at most. 88 readers sit above the funnel limits and none below. They held longer items (41,185 bytes against 34,056), called more lines arguable (0.55 against 0.44) and took longer. Their items also drew more second placements from the other replicate's readers (0.287 against 0.158), so part of the excess is in the items. Room and reader variance components are both small beside the residual, and the reader component is larger (multi: reader 0.012, room 0.007, residual 0.114).

The three most frequent (primary, additional) pairs:
- **T3-009 celebrating the finished work + T3-043 crediting who made the work** (114 lines, 112 readers, 83 rooms). Close-of-event threads mix "we did it" with thanks to named makers. The scheme separates the acts, but the material holds both, so this pair is a boundary rather than a confusion.
- **T3-005 defending the work against attackers + T3-021 watching and repairing the work** (114, and 59 in the other order). The pair `confusions.md` predicted hardest. Readers keep both when a stretch holds both quiet repair and a called defence, and the primaries split on 38 items.
- **T3-001 staging April Fools fake news + T3-032 objecting to April Fools posts** (48). A sub's prank and its members' objections sit in one theme.

T3-089 (switching off stale scripts) and T3-152 (announcing what the chat decided) are placed far more often as an addition than alone (30 to 6, 41 to 15). Stage C1 should read their designation rules.

Justifications: 40 `why_not_one` texts were read, one per reader. All 40 name material that one theme leaves out, and none restates the gates.

## Readers' predictions

1,180 of 1,212 returns carry a prediction; J waived the 32 without one (QB3-004). 539 readers predicted one of the 19 pairs of `confusions.md`, 245 of them T3-005/T3-021. One pair split the readers' primaries often but was rarely predicted: T3-017 carrying on ordinary sub talk against T3-031 playing the room's in-jokes (29 splits, 4 readers predicted it, not in `confusions.md`).

## What I reduced, and what stage B4 inherits

- **Reductions.** I reduced no placement to its primary. No line reads `label-only`, and every multi line has its records and a non-empty `why_not_one`.
- **Record slips (QB3-005).** The close-check refuses 22 readers' record slips: 10 loose multiplacement records, 8 multi lines whose `support` lists only the primary's concepts, and 4 single-theme lines with no `multi` field. Each added theme has a concept of its own. They are in `defects.jsonl`, kept as given, and J waived them by name (QB3-005; `return_waivers.jsonl`, keyed by batch and position).
- **The disagreement inventory.** 5,443 items placed alike and 2,401 split: 1,200 on the primary, 1,132 on an additional theme only, 69 on order only. 2,472 corpus lines place more than one theme, and 680 are flagged bags. The assembler's classes: 1, 2,566; 2, 1,990 (these stand); 3, 2,393; 4, 837; 5, 58 (these go to B4, 3,288 items).
- **The theme the fleet handled worst.** T3-152, announcing what the chat decided. Both readers name it on 33% of the 42 items where either does (kappa 0.50). It lives as an addition to T3-014, moving planning into a chat.
