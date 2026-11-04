# Handback, stage B2

Written at stage B2, leg B2d, 2026-10-12.

## What the stage delivers

- **The frozen scheme.** `scheme_final.jsonl` (197 themes, tier "main" 183 and "rare" 14, J at QB2-014) and `scheme_final.md`, with `families.jsonl` (21 families) beside them. All 496 gate pairs are confirmed against the frozen sentences in `gate_checks.jsonl`.
- **The record of the pilot.**
  - `scheme_edits.jsonl` (306 lines) with its `tier_history.jsonl` lines.
  - `rechecks-B2.jsonl` (1,594 records). 526 of them are the withdrawn split's and enter no figure.
  - `pilot_rounds.jsonl` (6 lines: rounds 1 to 3, gold, stab-1, stab-2).
  - `exemplar_candidates.jsonl` (68 lines, hard-set items only).
- **The reports.** `stability-B2.md` (the stability figure, 0.807) and `pilot_report.md` (the rounds, the gold number, the edits by theme, the author-error verdicts, the prediction scorecard, the cost).
- **The return specification.** `RETURN-B2.md` carries fleet ids, the three-concept floor for `also_present`, the rule that a bag with no other theme at the floor is not flagged, and "twenty themes at most".

## What I did not do as the stage file says

- **The packets.** Rounds 2 and 3, gold and the stability rounds were not built by `packets.py B2`. My own builders (`out/_analysis/b2_packets_r2b.py`, `b2_packets_fleet.py`, `b2_packets_fleet2.py`) built them. They apply J's rulings: self-contained packets under the caps, fleet ids only, and `codes_by_item` in each MANIFEST entry. The shared pages still come from `packets.py`'s `scheme_pages`.
- **The blind window.** The ten hard items of the blind re-placement had been visible to me in round tables earlier in this session. The window guarded the reads, not my memory, so the self-agreement of 0.883 is an upper bound.
- **The bag split, made and withdrawn.** At B2b-r2-p2 I split six bags into children. J withdrew the split. No one cuts the bags (J, 12:24 Berlin), and the records stay in `out/recut/` and `out/_analysis/`.

## What is wrong with the instrument, or unclear

Four gold items show sentences a stranger reads otherwise. The scheme is frozen, so they go to C1:
- **T3-001 against T3-048** on an unattributed fake (uofmn t01, nine of nine readers against me).
- **T3-004 against T3-033** on a new plan for a mark already standing (cuboulder t04).
- **T3-084 against T3-002 and T3-005** when the asker is from another room (mariokart t04).
- **T3-160 against T3-002** on calls to join a memorial (ireland t12).

**Pairs that stayed divided.** T3-004/T3-070 and T3-009/T3-073 are the only predicted confusions that divided readers more than once.

**The cluster's count rule.** The rule in T3-002, T3-033 and T3-038 asks a reader to sort concepts by act before counting. It is the sentence I am least sure a stranger reads as I meant.

**Second placements.** Readers drop most second placements. The deals with neighbours (G14) show it most: readers place T3-010 alone.

## What I ask for

- The ruling on C1's handling of the four gold-item wording defects above, since the scheme is frozen.
- **The bag count.** J counts 841 B1 bags, and my head has said 846. It is not reconciled.
- **Fleet ids in the validator.** `validate.py` reads room ids in `_fleet_raw` through the fleet table. B3's returns will be in fleet ids from the start, and the check should keep reading them so.

## What stage B3 should know

- **Gold placements.** The gold set's own placements carry the round-1 author-error: on ten items I placed a second theme no reader keeps. Gold fidelity in B3 should be read against the rechecked gold placements as well as against `gold_items.jsonl`. Even so, seven of the ten are not yet rechecked to one theme.
- **Floor and reference figures.** The stability figure, 0.807, is the floor for agreement. On gold, primary match is 0.800, fidelity 0.624 and pairwise 0.818.
- **Return specification.** Carry `RETURN-B2.md`'s bag rule and the phrase "twenty themes at most" word for word, with fleet ids and `codes_by_item`.
- **Batch cap.** The B3 cap stays at 40 items with a 10-item warm-up. The packets of this stage were too short to show a first-ten against last-ten curve.
- **No gold exemplars.** No exemplar may come from the gold set. `exemplar_candidates.jsonl` holds hard-set items only.

This handback reports agreement with my own placements. It bounds whether the instrument decides, not whether it is right.
