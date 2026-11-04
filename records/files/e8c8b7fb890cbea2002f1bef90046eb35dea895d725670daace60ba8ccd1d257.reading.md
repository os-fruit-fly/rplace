# Stability, stage B2

Written at stage B2, leg B2d, 2026-10-12. The stability check (FLEET.md) serves the gold set to the same reader arm under two rewordings of the brief that change no test. The arm's disagreement with itself is the floor every later figure is read against.

## What was served

- **Set.** The 40 items of `gold_items.jsonl`, on the frozen scheme (`scheme_final.jsonl`).
- **Readers.** deepseek/deepseek-v4.1-flash, called directly, medium effort, max_tokens 128,000, the readers of rounds 2 and 3.
- **Packets.** Three packets of 14, 14 and 12 items, three fresh readers each. All three rounds (gold, stab-1, stab-2) used seed 20261014. The same items fall in the same packets in the same order, so only the brief differs.
- **Briefs.**
  - The gold round used the builder's own brief.
  - Stab-1 used `out/brief-stab-1.md`, a rewording of that brief.
  - Stab-2 used `out/brief-stab-2.md`, a second rewording.
- **Content of the briefs.** No brief names a theme, a test or a placement.
- **Returns.** 9 valid returns each, none exhausted, 120 lines a round. All lines were translated back to room ids with 0 id problems (`out/_analysis/b2_translate_fleet.py`).

## The stability figure

`out/_analysis/b2_score_final.py` computed it. For each item, every stab-1 reader's set is compared with every stab-2 reader's set by Jaccard, nine pairs, and the nine are averaged. The mean over the 40 items is the stability figure.

**Stability: 0.807** (primary placements alike in 0.853 of the cross pairs).

The next table sets it beside each round's agreement within itself.

| figure | value |
|---|---|
| stab-1 against stab-2, mean Jaccard over the nine reader pairs per item | 0.807 |
| the same, primary placement alike | 0.853 |
| pairwise agreement inside stab-1 | 0.800 |
| pairwise agreement inside stab-2 | 0.756 |
| pairwise agreement inside the gold round | 0.818 |
| gold round against stab-1 | 0.826 |
| gold round against stab-2 | 0.796 |
| alpha over the six stability readers | 0.784 |
| alpha over all nine readers | 0.794 |
| mean change of an item's fidelity between stab-1 and stab-2 | 0.076 |

**What it shows.** Readers given differently worded briefs agree with each other (0.807) as much as readers given the same brief do (0.800 and 0.756). The rewording adds no disagreement beyond what three fresh readers already show under one brief. So about one placement in five differs between readers whatever the wording. That share is the floor: a later figure within it says nothing about the scheme.

**Fidelity under the rewordings.** It barely moves: 0.624 for gold, 0.636 for stab-1, 0.631 for stab-2. The primary match with my placement is 0.800 in all three.

**Items under 0.5 across the rewordings.** Five items: cuboulder t04, mariokart t04, mit t01, overwatch t23 and rit t01. Each is an item the gold readers already split on, or a two-act item where readers add or drop one theme. None moves because of a word in the brief.

## What this figure licenses

This figure bounds whether the instrument decides, not whether it is right. It says how much of the readers' disagreement belongs to the readers rather than to the scheme or the brief. It is agreement with my own placements and with each other. In FLEET.md's terms, it supports the claim that the fleet produces what I would have produced, at a scale one analyst cannot reach. It does not support the claim that any competent reader would have produced it.
