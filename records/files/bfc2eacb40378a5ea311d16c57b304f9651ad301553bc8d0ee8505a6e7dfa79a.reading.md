# Notes, stage B2: the pilot

## Standing instruction from J (2026-10-11, 16:54 Berlin, through the handler)

"Stop cutting room reads to a line length (cut -c1-100 or any other cut). Read room lines whole. When a read is too long, page it by line ranges or by offset, never by truncating lines."

From B2a-r1 on, every room read is whole by line. A long read is paged by line range or offset. No `cut -c` and no other truncation is applied to room material.

J also said (17:01 Berlin): ask J whenever a question is needed, with `mem.py ask`; asking does not stop the run.

## Leg B2a-r1, build round 1, 2026-10-11

### Declarations, made before round 1

**The hard set: sizes and sources.** 40 items, drawn by `out/_analysis/b2_select.py` with the string seed `b2a-r1:hard`. The list is `out/_analysis/b2_hardset_r1.tsv`.
- 19 confusion-pair items, one for each pair in `confusions.md`: the 17 ranked at B1e and two sibling pairs added at this leg (T3-014/T3-152 and T3-015/T3-063). Ten of the nineteen pairs are siblings inside one family. Each pair uses the item `confusions.md` nominated, unless that item renders over 2,500 bytes. Then the pick is seeded from the pair's pool: second-order themes holding both kinds in `scheme_current.jsonl` and rendering at or under 1,600 bytes. Five nominated items were replaced this way (pairs 7, 8, 11, 12 and 19).
- 8 rule 0 bags: second-order themes with an `item_is_a_bag` line in `multiplacement_log.jsonl`, rendering at or under 1,600 bytes, seeded.
- 13 random items, seeded, from the 3,933 placed second-order themes rendering at or under 1,500 bytes.

**A departure from section 1, and why (QB2-001 asks J).** `packets.py B2` serves each round as one packet under the 50 KB ceiling. Section 1 asks for 40 to 60 items, including the ten biggest bags of `notes-B1.md`.
- Those ten hold about 3,500 concepts. leagueoflegends t02 alone renders 86,762 bytes, over the whole ceiling, and sweden t01 renders 43,314.
- The median second-order theme renders 1,470 bytes, so 40 items fit only near or below the median.
- Rule 0 bags stand in for the ten biggest; the ten stay for stage B3 to flag.
- The cost: the random sample covers only themes at or under the median rendered size. Small themes sit on one kind more often (70.4% at five concepts or fewer, B1e). So the random items are likely easier than the corpus, and the pair and bag items carry the hard part.
- The round-1 items render 49,401 bytes.

**The gold set.** 40 items by the same rule, seed `b2a-r1:gold`, in `out/_analysis/b2_goldset.tsv`: 19 pair items from the pairs' pools (none a round-1 item), 8 rule 0 bags and 13 random. No second-order theme sits in both sets. The items render 42,148 bytes. I placed them myself into `out/gold_items.jsonl` with confidence and reasons. They are shown to no pilot reader and kept outside the readers' directory.

**The stopping threshold.** Rounds stop when the mean pairwise agreement on the hard set reaches 0.70 (the definition is below). The other stops of section 5 also hold: a round with no scheme edit, or four rounds. Why 0.70: the set is drawn hard, half from pairs a reader is expected to confuse. On easy items the scheme should do far better, and stage B3 reports that.

**The agreement definition, which stages B3 and B4 reuse unchanged.**
- An item's placement is the set of third-order themes a reader returns (`third_order`).
- Two sets agree by their Jaccard index, |A ∩ B| / |A ∪ B|. `["T3-004"]` against `["T3-004","T3-011"]` scores 0.5, which is partial agreement. Disjoint sets score 0, and identical sets score 1.
- **Pairwise agreement** is the mean Jaccard over the three reader pairs of each item, then over items.
- **Fidelity** is the mean Jaccard between each reader's set and the author's set in `author_items.jsonl`, over readers and items.
- **Alpha** is Krippendorff's alpha with distance 1 − Jaccard between sets, over items run at more than one reader. Chance correction is over sets: the expected disagreement is computed from all placement sets returned in the round, pooled, as the values of the nominal-like distribution.
- Also reported, never in place of the above: exact agreement on the primary, the first theme of each set.

**The gold policy.**
- 40 gold items, placed by me, in `out/gold_items.jsonl`.
- Stage B3 seeds them unannounced into live batches at one gold item per 20 items, so about 5% of a batch, with no more than two in any batch.
- Each gold item is seeded at least once over the run.
- The policy names the rate and that gold is seeded, never which items.

**The batch cap for stage B3.** Set at the check leg B2b-r1, from the position curves of section 4. It is not set here.

**Author placements.** Every item of both sets was placed by me into `author_items.jsonl` and `gold_items.jsonl` before any packet existed. Each line has the set of third-order themes, a `why` per theme, a confidence (`clear` or `arguable`) and the concepts it rests on. I read each item through `mem.py theme <sub>/<tNN>`, whole, paged where long. That verb prints the working placements of `scheme_current.jsonl` above the concepts, so they were in view. Those placements are my own from B1. Each author placement was made against the shipped gates in `scheme.jsonl`, and where it differs from the working placement, the line says so.

### What was built

**The author's placements** (`out/_analysis/b2_author.py`, which checked every theme id against `scheme.jsonl` and every support concept against the item's own concepts in the store):
- `author_items.jsonl`: 40 items. 5 are clear and 35 arguable; 24 are placed on more than one kind; 25 differ from the B1 working grouping in at least one kind.
- `gold_items.jsonl`: 40 items. 4 are clear and 36 arguable; 17 are on more than one kind; 19 differ from the B1 working grouping.
- The many arguable placements fit how the sets were drawn: half the items come from pairs I predicted readers would confuse, and eight from rule 0 bags.
- Where my placement differs from the working grouping, it mostly drops a kind whose concepts the gate does not support on their own (`b2_author_vs_working.py`). In the hard set, 18 items only drop a kind, 5 only add one, and 2 do both; 15 are the same. In the gold set, 15 only drop, 4 only add and 21 are the same. My primary is among the working kinds in 39 of 40 hard items and 40 of 40 gold items. Three examples of a dropped kind: dofus t01 drops T3-002, GreenCorner t03 drops T3-069, and flashtv t13 drops T3-054.

**RETURN-B2.md.** It holds rule 0 in the contract's words and the return line of section 1. Rule 0's line for `multiplacement_log.jsonl` is carried on the return line as `multiplacement_log`, null when `multi` is false. The check leg copies those lines into the pilot's record, never into the B1 log. It also holds `item_is_a_bag`, the end marker `END-OF-RETURN` in the fenced block, and the line telling the reader to confirm it reached the marker.

**The packets.** `packets.py B2 --round 1 --scheme scheme.jsonl --items author_items.jsonl --seed 20261011 --to out/_packets-B2` wrote:
- `index.md` (33,148 bytes);
- 21 family pages (6,566 to 16,448 bytes);
- `P03-r1.md`, 40 items in seeded order, 49,720 bytes, sha256 1efc10ac60398acee09ad3503aca758803f96cd1fae8ee0afea3044d0bf868ff;
- `MANIFEST.json`.

No exemplar is served, and no gold file is in the folder. The scheme served is `scheme.jsonl` as shipped at B1e. `packets.py` would otherwise have preferred `scheme_current.jsonl`, which holds no gates, so `--scheme` was given.

**Where the packets live (QB2-002 asks J).** `packets.py` writes to `_packets-B2/round-1/` by default. HOW-TO-RUN.md and `validate.py B2` expect the packets flat in `_packets-B2/`. I built flat. The first, nested build is byte-identical and moved to `out/_analysis/b2_packets_round1_nested/`, so the dispatch finds one packet only.

**Manifest.** `run_manifest.json` has a B2 round-1 entry: readers on `@preset/cheap` through the gateway, three of them; the seeds; 40 items; and the packet's path and hash. The decoding settings are left to the dispatch, which records what served.

**Questions open:** QB2-001 (the 50 KB ceiling against the ten biggest bags) and QB2-002 (the packet path). Each carries its assumption, and the work above rests on both.

**Reading.** From this leg on, no room read was cut to a line length. The only "…" in the reads is `mem.py`'s own display of the label column; the quote column was whole in every read.

### The close-check, B2a-r1

`validate.py B2` reported:

```
stage B2:
  leg: build (0 dispatch folders with DONE)
  author items 40, gold items 40, scheme ids 197

0 errors (0 distinct shapes), 0 warnings
```

The leg closes with `done.sh B2 --cut packets-out`. The dispatch sends `P03-r1.md` to three fresh readers. The check leg B2b-r1 scores fidelity, pairwise agreement and alpha, sets the batch cap for stage B3, and makes the edits.

## Leg B2b-r1, check round 1, 2026-10-11

### What the PI and J ruled before and during this leg

- **QB2-001** (answered 15:15Z): serve oversize items in parts to the same reader, as stage B3 serves a large room. Do not cap the hard set by size. Each part stays under the 50 KB ceiling with its end marker, and the reader answers once per item after the last part. If `packets.py` cannot part a B2 item, the splitter is a helper in `out/_analysis/`, and the parts are recorded in `MANIFEST.json` and here. Round 1 goes out as built.
- **The round-2 rule** (same message): from round 2, the ten biggest bags of `notes-B1.md` are served in parts. No round may meet a stopping rule of section 5 before those ten have been read by the round's readers at least once.
- **QB2-002** was first answered "flat", then corrected by the handler at 15:29Z. `fleet.py` reads `*.md` flat in the folder it is given, but `CONTROL/harness/dispatch.sh` gives it `out/_packets-B2/round-K/` for B2 and refuses when that folder is missing. `packets.py`'s default, `round-K/`, is the right place. J copied round 1's packets into `out/_packets-B2/round-1/` to dispatch them. Later rounds are built in `round-K/`, and earlier rounds stay where they are. The flat copy in `out/_packets-B2/` is round 1's and stays.
- **QB2-003** (answered during this leg): repairs the gate check found are recorded in `scheme_edits.jsonl` with `caused_by ["gates:T3-a|T3-b"]`. A word-for-word mirror takes kind `gate-check` and owes no recheck and no tier_history line. A new sentence takes its ordinary kind and owes both. Repair all in this leg if possible, before round 2's packets.
- **v43.2 tools** (J, "Do all changes"):
  - `mem.py blind on|off`;
  - `--width` on reads, with the guard refusing `cut -c` after `mem.py`;
  - `mem.py gates` (with `--confirm`);
  - `tools/tokens.py`;
  - rule 0's `also_present` clause for bags, on the return line from the next round;
  - `support_by_theme` on my records;
  - rechecks owed by every edit (`mem.py rechecks --owed`, `mem.py recheck`).
- **The reader settings** (J, 20:42 Berlin): from round 2 the reader preset is pinned to one provider (Relace) at medium reasoning effort. Round 1's three readers ran at high effort on mixed providers (Relace, Baidu Qianfan, Reka AI), all on the same model, deepseek/deepseek-v4-flash-0731. A change in agreement between rounds 1 and 2 is partly the reader settings, not only my edits. This goes in the round-2 manifest entry too.
- **Corrections from the B1e interview**, made on the record (`notes-B1.md` and `handback-B1.md` carry an appended correction):
  - The T3-005 and T3-021 gates contradicted each other on repair during a raid. Corrected before the pair was scored (edit below).
  - F-001's grain bound does not hold across rooms. `out/_analysis/b2_grain_check.py`: Spearman −0.08 between a room's mean concepts per theme and its single-kind share (633 rooms). Within rooms, mean Spearman 0.28 between a theme's concepts and its kinds (positive in 482 of 619 rooms). `findings.jsonl` has the superseding F-001 line, status bounded.
  - "107 episode lines" is 106 (line, kind) pairs over 81 lines (`out/_analysis/b2_episode_kinds.py`).

### The dispatch, in `fleet.py`'s counts

`out/_fleet_raw/B2/round-1/` holds four attempts.
- The first (DONE, 17:08Z) returned nothing valid. The reader model reasoned before answering and used its whole 16k output budget. The gateway's response cache then handed eight reissues the same empty reply. `EXHAUSTED.tsv` names r5, r7 and r9: no end marker. The handler then changed `fleet.py`: the reader id opens each message, readers run in parallel, the output limit is raised, and the served model is read from the reply.
- Two more attempts failed the same way while those fixes went in (r10, r11; r13 was cut off). Every `*.failed.txt` is a failed attempt, not a reading.
- The round scored is the last, `PARTIAL-2026-10-11T183640Z.json`: three valid returns of 40 lines each, r12, r15 and r16. All were served by deepseek/deepseek-v4-flash-0731 (served matches the probe).

| reader | reissue | elapsed (s) | input tokens | output tokens (thinking) | cost (USD) |
|---|---|---|---|---|---|
| r12 | 0 | 582.7 | 158,259 | 85,776 (61,498) | 0.066 |
| r15 | 1 | 1,396.4 | 286,397 | 129,100 (117,668) | 0.099 |
| r16 | 1 | 273.0 | 133,410 | 60,104 (49,156) | 0.046 |

The whole last run cost 0.369 USD, with 747,469 input and 494,282 output tokens. Each reader's usage record shows one tool call; the record does not say what it was.

### Round 1's three numbers

Scored by `out/_analysis/b2_score.py` on r12, r15 and r16 only, by the definitions declared above:
- **Fidelity** against `author_items.jsonl`: mean Jaccard 0.594. The primary matches mine in 0.742 of reader-items.
- **Pairwise agreement**: 0.733 (mean Jaccard; primary pairwise 0.767).
- **Alpha** (distance 1 − Jaccard, chance over the round's pooled sets): 0.726.
- **Disagreement**: 18 of 40 items have two readers differing.

What licenses these figures, in FLEET.md's words: readers share an architecture with me or with each other, so the figures bound whether the written instrument decides, never whether it is right. The claim they support is what I would have produced at a scale one analyst cannot reach, not what any competent reader would have produced.

By source and by my confidence:
- confusion-pair items: fidelity 0.558, pairwise 0.755;
- bags: fidelity 0.500, pairwise 0.749;
- random items: fidelity 0.705, pairwise 0.692;
- items I marked clear: fidelity 0.833; arguable: 0.560.

**The main finding is mine to own.** I placed 24 of the 40 items on two kinds. The readers placed one kind in most items: 3, 6 and 1 multi lines out of 40. In 14 items all three readers placed one theme that is among mine, so the item scores 0.5 against me while the readers agree perfectly. Rule 0 asks for a second placement only where one cannot carry the material. The readers read it more strictly than I did. Those second placements are author-errors (the rechecks below record them). The readers are not wrong.

**Stopping.** Pairwise agreement (0.733) clears the declared threshold of 0.70. Under the round-2 rule no round may stop before the ten biggest bags have been read, and this round made edits. So round 2 opens.

### What divided readers, and the verdicts

`out/_analysis/b2_r1_items.tsv` has every item.

- **Author-error** (readers right, me wrong):
  - My second kind was not needed, all three readers placing one: 4chan t07, GreenCorner t03, england t03, flashtv t13, floridagators t09, harrypotter t08, kpop t04, megaman t11, redhotchilipeppers t09, furry t10 and nyu t01 (T3-004 never chosen), signal t01, WisconsinBadgers t04, simonfraser t08.
  - My primary was wrong: orderofthebluecorner t08 (all three placed T3-121, exclusion, against my T3-087); stardustcrusaders t19 (all three placed T3-043, thanks, where the gate's default made T3-009 primary).
- **Scheme-ambiguous** (edited):
  - guatemala t02 (a national flag started and announced; readers placed T3-026 twice and T3-002 once, none T3-065) and catalunya t01 (one reader T3-002);
  - dofus t01 (T3-092, T3-038 and T3-002);
  - cubers t12 (T3-002, T3-041 and T3-169);
  - nVade t04 (all T3-005, where the work defended is another room's);
  - WisconsinBadgers t04 (one reader T3-042);
  - farmcarrots t15 (one reader T3-031).
- **Item-is-a-bag** (flagged, no edit): acecombat t05, Goodboye t03 and simonfraser t08. They hold four or more kinds and were bags in the B1 record.
- **Genuine-joint, or one reader recording rule 0's exception** (no edit): Slovakia t07, anarcho_capitalism t12, parabola t02, korea t15, furry t10 (T3-034) and donaldglover t04 (two readers added T3-032).
- **Reader-error**: none named. The single-reader misses (catalunya, n64, signal, farmcarrots) are covered by edits or by discriminators that already decide.

### The edits

`scheme_edits.jsonl`: 272 lines, all round 1.

The first record bundled mirrors and new questions one line per theme and field (36 lines). After QB2-003 it moved to `out/_analysis/scheme_edits_b2b-r1_bundled.jsonl`, and the record was rewritten one line per change. The 36 tier_history lines written for the bundled record (253 to 288) are superseded by the per-edit lines that follow them.

- **Sentence changes, 6:**
  - T3-005 must_not_show: repair "with or without an attacker in view, where no fight is called" goes to T3-021 (the contradiction).
  - T3-021 must_show: repair during a raid counts there when the fixing leads.
  - T3-009 and T3-043 decide_when_both: the side with more concepts is primary (author-error).
  - T3-065 must_show: announcements and calls for the room's own flag go there.
  - T3-092 decide_when_both: a piece begun alone and offered to the room is T3-033 when the offer leads.
- **8 discriminators from round-1 splits:** T3-087/T3-121 (author-error), T3-005/T3-011, T3-026/T3-065 and T3-002/T3-169, each in both gates.
- **Gate repairs no item caused** (QB2-003), until `mem.py gates` found no defect:
  - 202 word-for-word mirrors of one-way discriminators (kind gate-check);
  - 28 new questions, each written into both gates (56 lines), for `must_not_show` lines that sent material to a theme with no discriminator. 7 in the first pass are in `b2_edits_r1.py`; 21 are in `out/_analysis/b2_newpairs_r1b.json`.
  - Together with the 6 sentence changes and the 8 split-driven discriminators, that makes 70 edits that owe rechecks and tier_history lines.
- **After the edits:** `mem.py gates` reports 0 one-way discriminators, 0 such `must_not_show` lines and 0 unknown ids. Eleven pairs were read and confirmed (`out/gate_checks.jsonl`): T3-005/T3-021, T3-009/T3-043, T3-002/T3-065, T3-087/T3-121, T3-005/T3-011, T3-026/T3-065, T3-042/T3-076, T3-062/T3-084, T3-033/T3-092, T3-002/T3-169 and T3-004/T3-070. The other pairs of edited themes are not yet confirmed; they are read before the freeze.
- No theme was narrowed, and no theme's members changed. **Base rates** (author against readers, over 40 items):
  - T3-004: 2 against 0;
  - T3-021: 1 against 0;
  - T3-011: 3 against 1;
  - T3-014: 2 against 8 (2.7 per reader);
  - T3-005: 3 against 9 (3.0 per reader);
  - T3-121: 0 against 3.

  The full table is in the score script's output. Round 2 watches T3-004 and T3-021, which no reader chose.

### The rechecks

Every edit that is not a gate-check owes rechecks of my own placements on the themes it touches. There are 70 such edits; they owe 594 records over 78 items. `out/_analysis/b2_rechecks_r1.py` decides each item once and records it under every edit that owes it, with `mem.py recheck` and the concepts behind each theme.
- **22 items move:** 18 are author-errors, mostly second kinds that rule 0 does not need, and 4 are the edits doing their work (GreenCorner t03, dofus t01, stardustcrusaders t19, guatemala t02).
- The rest are unchanged, each with its reason.
- `author_items.jsonl` stays as written. From round 2, fidelity is reported twice: against it, and against the rechecked placements.

### Section 4

**Position curves** (each reader's items at positions 1 to 10 against 31 to 40):
- r12: arguable 6 then 5; agreement with the other two 0.70 then 0.80.
- r15: arguable 8 then 6; agreement 0.65 then 0.70.
- r16: arguable 6 then 4; agreement 0.75 then 0.70.

Two of three readers still improve inside the round, so convention formation is not over at 40 items. Ten items per bin and three readers make this weak evidence. Following section 4, the remedy is a warm-up block, not a bigger batch.

**The batch cap for stage B3** (declared here): 40 items per batch, the first 10 of them a warm-up block that is placed and not counted. To be revisited with round 2's curves.

**Exemplar candidates:** the 18 items that divided readers are in `exemplar_candidates.jsonl`, with the readers' sets and mine.

### Predicted confusions, so far

Of the 19 pairs in `confusions.md`, round 1's readers split on:
- pair 6 (dofus t01, T3-002/T3-033), though not along the predicted line;
- pair 8 (furry t10, T3-004/T3-070), by adding T3-034;
- pair 10 (signal t01, T3-038 against T3-009, not T3-004);
- pairs 2, 7 and 12 by adding a second kind (anarcho_capitalism t12, korea t15, parabola t02);
- pair 11 by moving off both themes (acecombat t05, T3-014 and T3-062).

The hardest predicted pair, T3-005/T3-021, did not split: GreenCorner t03 went to T3-005 for all three readers. The scored scorecard comes after the gold round.

### Next

Round 2 is built at `B2a-r2`, in `out/_packets-B2/round-2/`, from the edited `scheme.jsonl`:
- the ten biggest bags served in parts (the splitter as a helper if `packets.py` cannot part a B2 item);
- `RETURN-B2.md` with the `also_present` clause;
- the manifest entry noting the reader settings.

### Added after the section above, in the same leg

**The deal cluster.** Reading T3-010's 17 pairs found seven where a decide_when_both names T3-010 but no discriminator separates the pair: T3-012, T3-035, T3-039, T3-040, T3-084, T3-123 and T3-139. `mem.py gates` checks only `must_not_show` lines, so it does not see this shape. Seven questions were written into both gates (`out/_analysis/b2_newpairs_r1c.json`; scheme_edits 273 to 286). They are kind scheme-ambiguous, with `caused_by gates:A|T3-010` and 14 tier_history lines.

The final counts are:
- `scheme_edits.jsonl`: 286 lines, 202 gate-check mirrors and 84 edits that owe rechecks;
- `tier_history.jsonl`: 372 lines;
- `mem.py gates`: no defect; 28 pairs confirmed, 0 stale, 464 unconfirmed. The unconfirmed pairs are read before the freeze.

**The rechecks, final.** 697 recheck records, none owed. 22 items moved from my original placement: 18 author-errors and 4 edits doing their work.
- 70 records failed when first tried. An earlier recheck had already moved those items off the themes the later edits touch, so `mem.py` no longer counted them as owed; the record was right to refuse them.
- `mem.py recheck` takes about 4.5 seconds a record, and the first run went past the ten-minute foreground limit into the background. The rest ran in the foreground in slices (`--max`).

### The close-check, B2b-r1

`validate.py B2` reported:

```
stage B2:
  leg: check (1 dispatch folders with DONE)
  _fleet_raw/B2/round-1: 3 readers, 120 return lines
  author items 40, gold items 40, rounds scored 1, edits 286 (author-error 4), scheme ids 197 (scheme/scheme_current.jsonl)

0 errors (0 distinct shapes), 443 warnings
warn   scheme.jsonl: the pair T3-001|T3-017 touches an edited theme and is not confirmed against its current sentences (mem.py gates T3-001 T3-017 --confirm --reason ...)  [443 lines with this shape; first: T3-001|T3-017]
```

The 443 warnings are pairs touching an edited theme that are not yet confirmed. They are read and confirmed before the freeze, where they become errors. The check counts 120 return lines because `round-1` holds only the three valid readers' `.jsonl` files; the failed attempts are `.failed.txt`.

The leg closes with `done.sh B2`. Round 2's build leg, B2a-r2, comes next.

## Leg B2a-r2, build round 2, 2026-10-11

### QB2-003, revisited

The PI's answer to QB2-003 arrived during B2b-r1, and that leg applied it in full. Every repair is a `scheme_edits.jsonl` line with `caused_by` `gates:T3-a|T3-b`; mirrors are kind gate-check, with no recheck and no tier_history line; new sentences are scheme-ambiguous and owe both. My assumption, to repair only the pairs round 1's edited themes belong to, was dropped in that leg. No work of this leg rested on it. `mem.py gates` on the scheme served this round finds 0 one-way discriminators, 0 `must_not_show` lines without a discriminator and 0 unknown ids. 28 pairs are confirmed and 464 are not. The answer asks me to confirm each pair I read; the 464 are read and confirmed before the freeze.

### The ten biggest bags, placed

I read all ten second-order themes whole, paged with `--limit` and `--offset` and never cut. Then I placed them, before any round-2 packet existed. `out/_analysis/b2_author_r2.py` appended them to `author_items.jsonl`. It checked every theme id against `scheme.jsonl`, and every concept against the item's own concepts with `vlib.support_problems` and `vlib.also_present_problems`. It also checked that no item was already in the hard or gold set, and it took each item's rank from `notes-B1.md`'s list. Each line carries `source` "biggest-bag", `support_by_theme`, `item_is_a_bag` and `also_present`. All ten are arguable. The hard set is now 50 items.

Rule 0, as amended, decides the form. Round 1 showed that my second kinds were author-errors whenever one theme carried the material. So no line places more than one theme. A bag, an item that needs more than three themes, places one and names the rest under `also_present`, each with its own concepts.

The next table lists the ten items: the theme placed, the themes named under `also_present`, and the B1 working kinds.

| rank | item | concepts | placed | also_present | B1 working kinds |
|---|---|---|---|---|---|
| 1 | leagueoflegends t02 | 798 | T3-023 | none | T3-023 |
| 2 | theblackvoid t09 | 389 | T3-006 | none | T3-006, T3-080, T3-085 |
| 3 | ainbowroad t11 | 361 | T3-035 | none | T3-035, T3-084, T3-139 |
| 4 | 2007scape t04 | 349 | T3-038 | T3-005, T3-123, T3-010, T3-179, T3-157 | T3-038 |
| 5 | theblackvoid t12 | 335 | T3-174 | T3-006, T3-163, T3-190, T3-005 | T3-031, T3-163, T3-174 |
| 6 | ainbowroad t04 | 327 | T3-021 | T3-139, T3-024, T3-011, T3-084 | T3-021 |
| 7 | ainbowroad t03 | 326 | T3-005 | T3-084, T3-149, T3-050, T3-124 | T3-005 |
| 8 | dota2 t05 | 314 | T3-023 | none | T3-023, T3-032 |
| 9 | ainbowroad t07 | 311 | T3-041 | T3-035, T3-160, T3-033, T3-061 | T3-038, T3-041, T3-160 |
| 10 | sweden t01 | 310 | T3-065 | T3-035, T3-012, T3-061, T3-113, T3-151 | T3-065 |

Six are bags and four take one theme. Points from the reads:
- leagueoflegends t02 and dota2 t05 are the two moderator makeovers (Marc Merrill, and Arteezy as r/tz). Objections to the joke, reactions to Riot's own jokes and asks to keep the theme are present, but the takeover carries them.
- theblackvoid t09 calls attacks on named targets: national flags, the EU flag, the trans ribbon, "the slimy swedes". The B1 working kinds added T3-080 and T3-085. I found the calls to attack carry the material and placed T3-006 alone.
- ainbowroad t11 is outside rooms addressing Rainbow Road as host. Requests for space, pleas for help and pleas not to be run over sit on one host relation, and T3-035 carries them.
- theblackvoid t12: I placed T3-174 (loyalty to the Void's colour: hails, the oath, anthems) over the B1 working T3-031. The creeds are professions of loyalty, not in-jokes played inside the room.
- ainbowroad t07: I placed T3-041 (extending strands, adding features) over T3-038. The road was already built; these concepts extend it.
- ainbowroad t03 holds the line "KILL THE GAYS" (c1395), posted to the room. It is served to readers as it stands.

### What was built

**`RETURN-B2.md`.** It gains the `also_present` clause in J's words of section 1. A bag places one theme and names every other with its own concept ids; otherwise the field is `{}`. It also gains a paragraph on parts: read every part, reply with the end marker alone on every part but the last, and answer for all items on the last. The batch name is now `P03-r2`. The round-1 text is kept as `out/_analysis/RETURN-B2_round1.md`; round 1 is scored as it was sent.

**The packets, in parts (QB2-001).** `packets.py B2` writes one packet and exits when it is over 50 KB. Round 2 renders to about 513 KB, and leagueoflegends t02 alone is about 87 KB. So the splitter `out/_analysis/b2_parts_r2.py` imports `packets.py` and uses its own `Store.item` and `scheme_pages`. It shuffles the 50 items as `packets.py` does, with seed 20261012. Then it cuts the rendered lines into parts. An item that does not fit runs on into the next part under its heading marked "(continued)". A concept line always travels with its quote line, and positions run on across parts. The helper checks that every concept of every item is served exactly once. It wrote `out/_packets-B2/round-2/`:
- `index.md` (33,542 bytes) and 21 family pages (7,839 to 19,772 bytes), from the edited `scheme.jsonl`, with no exemplars;
- `P03-r2-p1` to `P03-r2-p11`. Ten parts are 50,254 to 50,394 bytes and the last is 9,799; each is under 51,200 bytes with its end line, 513,096 bytes in all;
- `MANIFEST.json`.

The next table lists the positions each part holds.

| part | positions | part | positions |
|---|---|---|---|
| p1 | 1-8 | p7 | 37 |
| p2 | 8-19 | p8 | 37-39 |
| p3 | 19-27 | p9 | 39-43 |
| p4 | 27-28 | p10 | 43-47 |
| p5 | 28-36 | p11 | 47-50 |
| p6 | 36-37 | | |

Position 37 runs over four parts (p5 to p8); it is leagueoflegends t02. The seeded order and the positions per part are in `out/_analysis/b2_order_r2.json`, outside the readers' folder. Round 1's packets are where they were: flat in `out/_packets-B2/`, and J's copy in `round-1/`. No gold item and no room note is in the folder.

**MANIFEST.json, on QB2-004's assumption.** QB2-004 is open. It asks what form `fleet.py` expects when one item is larger than a part. Until it is answered, each part carries `count_key` position, the B3 exclusions, `group` P03-r2, `part` k and `parts` 11. Parts 1 to 10 carry `items` 0, since their reply is the end marker alone, and part 11 carries all 50. Each entry also records its positions and the seed. If J answers otherwise, the next build leg rebuilds from the same helper.

**Manifest.** `run_manifest.json` has a B2 round-2 entry (`out/_analysis/b2_manifest_r2.py`). It records the model, deepseek/deepseek-v4-flash-0731, and J's reader settings: one provider (Relace) and medium reasoning effort. Round 1 ran at high effort on mixed providers. A change in agreement between the rounds is therefore partly the settings and not only the edits. The entry also records the seed, 3 agents, 50 items, and every part's bytes and sha256.

**The PI's round-2 rule.** No round may meet a stopping rule before the ten biggest bags have been read once. Round 2 serves all ten, so its check leg may apply the stopping rules.

**Questions open:** QB2-004.

### The rechecks the ten new items owed

The ten bags sit on themes that round 1's edits changed. The first run of `validate.py B2` in this leg therefore found 57 rechecks owed under 42 edits, one error line per edit. No edit can have moved a placement made after it. The check still asks for the record, so `out/_analysis/b2_rechecks_r2.py --show` printed each edit's changed sentence beside the items it owes. I read each and wrote one reason per edit. None moves a placement. The 57 records went in through `mem.py recheck`, all unchanged, with the concepts from each line's `support_by_theme`. `rechecks-B2.jsonl` now has 754 records, and none is owed.

### The close-check, B2a-r2

`validate.py B2` reported:

```
stage B2:
  leg: check (1 dispatch folders with DONE)
  _fleet_raw/B2/round-1: 3 readers, 120 return lines
  author items 50, gold items 40, rounds scored 1, edits 286 (author-error 4), scheme ids 197 (scheme/scheme_current.jsonl)

warn   scheme.jsonl: the pair T3-001|T3-017 touches an edited theme and is not confirmed against its current sentences (mem.py gates T3-001 T3-017 --confirm --reason ...)  [443 lines with this shape; first: T3-001|T3-017]

0 errors (0 distinct shapes), 443 warnings
```

The 443 warnings are the unconfirmed pairs that touch an edited theme. They are read and confirmed before the freeze. The check calls the leg "check" because round 1's dispatch folder holds DONE; this leg is round 2's build. The leg closes with `done.sh B2 --cut packets-out`. The dispatch sends the eleven parts of P03-r2 to each of three fresh readers. The check leg B2b-r2 scores fidelity against `author_items.jsonl` and against the rechecked placements, with pairwise agreement and alpha.

## Leg B2b-r2, round 2 rebuilt, 2026-10-12

### Why round 2 was rebuilt

Round 2's dispatch ran three times, and every reader was exhausted. There is no valid return. `out/_fleet_raw/B2/round-2/` holds DONE, `EXHAUSTED.tsv` and `log.jsonl`; nothing in it is scored. The handler gave two causes, both in the log.
- Every reader got HTTP 400 at part 6. Part 5 carried 149,007 input tokens and passed; part 6 would carry about 163,000. The provider's window looks to be about 164,000 tokens (the handler inferred this from the log; it is not confirmed). One conversation over eleven parts cannot fit, since the shared pages alone are about 95,000 tokens.
- Some readers closed part 1 with the packet's end line instead of `END-OF-RETURN`. `fleet.py` now names the marker in every message.

QB2-004 was answered before the dispatch: J confirmed my MANIFEST form for parts. J's ruling of 2026-10-12 replaces the parts design, so nothing rests on that answer any longer.

### J's ruling, as applied

The ruling asks for self-contained packets: at most 15 items and at most 180,000 bytes of item text each; no item split across packets; no MANIFEST group, part or parts; the same 50 items, shared pages and RETURN-B2.md, minus its parts paragraph.

`out/_analysis/b2_packets_r2b.py` built them with `packets.py`'s own `Store.item`. It keeps round 2's seeded order (seed 20261012, `out/_analysis/b2_order_r2.json`) and cuts it into consecutive packets, choosing the cut points that make the largest packet smallest. No item is over the cap; the largest, leagueoflegends t02, is about 87,000 bytes. Four packets would meet the caps, but one would hold 166,501 bytes of item text, close to the cap. I built five, so the largest holds 128,155 bytes and each reader has more room inside the window.

The next table lists the five packets that the dispatch must read, all in `out/_packets-B2/round-2/`.

| packet | items | bytes of item text | bytes in all |
|---|---|---|---|
| `P03-r2-1.md` | 15 | 58,210 | 58,656 |
| `P03-r2-2.md` | 12 | 96,519 | 96,965 |
| `P03-r2-3.md` | 9 | 128,155 | 128,599 |
| `P03-r2-4.md` | 3 | 125,484 | 125,928 |
| `P03-r2-5.md` | 11 | 97,101 | 97,547 |

Each packet numbers its items from 1 and says how many lines to return. `MANIFEST.json` gives each packet its own item count, with count_key position, and no group or part. The items per packet are in `out/_analysis/b2_order_r2b.json`. The shared pages beside them are `index.md` and `G01.md` to `G21.md`, unchanged from B2a-r2. Packet 4 holds three items: leagueoflegends t02, acecombat t05 and dota2 t05.

The packets are over FLEET.md's 50 KB ceiling by J's ruling, which sets the byte cap at 180,000 of item text. `packets.py`'s writer asserts 50 KB, so the helper writes the files itself.

**Superseded, not deleted.** The eleven parts `P03-r2-p1.md` to `P03-r2-p11.md` and their `MANIFEST.json` moved to `out/_analysis/b2_packets_round2_parts/`. The dispatch must not read them.

**RETURN-B2.md** loses its paragraph on parts. The batch field is now the name on the packet's title line, such as `P03-r2-3`. The parts version is kept as `out/_analysis/RETURN-B2_round2_parts.md`.

**Manifest.** `run_manifest.json` has a new round-2 entry from this leg (`out/_analysis/b2_manifest_r2b.py`). It supersedes the B2a-r2 entry, which stays. It records the five packets with bytes and hashes, J's caps, and the same reader settings: one provider (Relace) and medium effort.

### The close-check, B2b-r2

`validate.py B2` reported:

```
stage B2:
  leg: check (2 dispatch folders with DONE)
  _fleet_raw/B2/round-1: 3 readers, 120 return lines
  _fleet_raw/B2/round-2: 0 readers, 0 return lines
  author items 50, gold items 40, rounds scored 1, edits 286 (author-error 4), scheme ids 197 (scheme/scheme_current.jsonl)

ERROR  _fleet_raw/B2/round-2 holds a finished dispatch and pilot_rounds.jsonl has no line for round 2; the check leg scores it (fidelity, pairwise agreement, alpha) before it closes
warn   scheme.jsonl: the pair T3-001|T3-017 touches an edited theme and is not confirmed against its current sentences (mem.py gates T3-001 T3-017 --confirm --reason ...)  [443 lines with this shape; first: T3-001|T3-017]

1 errors (1 distinct shapes), 443 warnings
```

The error conflicts with J's ruling. The failed folder holds no reading, so there is nothing to score, and the check accepts no line without numbers. QB2-005 asks J how to record a failed dispatch. Meanwhile I write no `pilot_rounds.jsonl` line for round 2 and leave `_fleet_raw/B2/round-2/` as the dispatch left it. A diary line of kind ask at 03:56 carries the same question without an id; I wrote it with `mem.py log` by mistake, and QB2-005 is the record.

The 443 warnings are the unconfirmed gate pairs, read before the freeze.

### QB2-005, answered: the failed dispatch moved aside

J ruled (2026-10-12, 06:55 Berlin). The failed folder is renamed and no `pilot_rounds.jsonl` line is written for it. I ran `mv out/_fleet_raw/B2/round-2 out/_fleet_raw/B2/round-2-failed`; nothing was deleted. J dispatches round 2 again into a fresh `round-2/` folder.

`round-2-failed/` holds the three exhausted dispatches of the eleven-part packet and no reading. Its DONE file counts 11 packets, 3 readers, 0 valid returns and 3 exhausted, on deepseek/deepseek-v4-flash-0731. They used 1,873,195 input tokens and 10,054 output tokens, at a cost of 0.087 USD. The log holds 70 calls from 14 reader ids (r1 to r14). The folder holds 13 failure files:
- 9 failed at part 6 with HTTP 400. Part 5 carried 149,007 input tokens and passed; part 6 would carry about 163,000. The provider's window looks to be about 164,000 tokens; the handler inferred this from the log, and it is not confirmed.
- 4 failed at part 1 because the reply ended with the packet's end line ("END OF PACKET" or "END-OF-PACKET") instead of `END-OF-RETURN` (r6, r8, r10, r14).
- r4 appears in the log with no failure file of its own.

My assumption under QB2-005 was to write no line and leave the folder alone. The first half stands; the folder is now renamed as J ruled.

### The close-check after the rename (QB2-006)

After the rename, `validate.py B2` reported:

```
stage B2:
  leg: check (2 dispatch folders with DONE)
  _fleet_raw/B2/round-1: 3 readers, 120 return lines
  _fleet_raw/B2/round-2-failed: 0 readers, 0 return lines
  author items 50, gold items 40, rounds scored 1, edits 286 (author-error 4), scheme ids 197 (scheme/scheme_current.jsonl)

ERROR  stage output 'scheme_final.md' was not written
ERROR  stage output 'scheme_final.jsonl' was not written
ERROR  stage output 'stability-B2.md' was not written
ERROR  stage output 'pilot_report.md' was not written
warn   _fleet_raw/B2/round-2-failed returned but no pilot_rounds.jsonl line is flagged "gold": true; the gold figure is reported beside the last round's
warn   scheme.jsonl: the pair T3-001|T3-017 touches an edited theme and is not confirmed against its current sentences [443 lines with this shape]
```

The round-2 error is gone. The check treats every folder in `_fleet_raw/B2/` that holds DONE and is not named `round-N` as a gold or stability dispatch, so it reads the stage as finished and asks for the freeze outputs. The stage is not finished, and writing those files now would be false. `round-2-failed/` still holds the dispatch's own DONE file, which I leave untouched. QB2-006 asks J which fix he wants: move the folder out of `_fleet_raw/B2/`, have the dispatch rename DONE, or have the check skip folders named `*-failed`. Meanwhile the folder stays where J named it, and the leg stays open if `done.sh` refuses. The five packets in `out/_packets-B2/round-2/` are ready for the new dispatch either way.

### QB2-006, answered: the failed dispatch moved out of `_fleet_raw/B2/`

J ruled at 06:55, and the handler placed the folder under that ruling. The check is not changed. I moved `out/_fleet_raw/B2/round-2-failed/` whole to `out/_analysis/fleet_B2_round2_failed/` (mv). Nothing was deleted, and its DONE, `EXHAUSTED.tsv`, `arm.json`, `log.jsonl` and 39 reader files are inside, untouched. The new path is where the failed first dispatch of round 2 lives; it holds no reading and is never scored. `_fleet_raw/B2/` now holds `round-1/` only, and J dispatches round 2 again into a fresh `round-2/`.

`validate.py B2` after the move:

```
stage B2:
  leg: check (1 dispatch folders with DONE)
  _fleet_raw/B2/round-1: 3 readers, 120 return lines
  author items 50, gold items 40, rounds scored 1, edits 286 (author-error 4), scheme ids 197 (scheme/scheme_current.jsonl)

warn   scheme.jsonl: the pair T3-001|T3-017 touches an edited theme and is not confirmed against its current sentences (mem.py gates T3-001 T3-017 --confirm --reason ...)  [443 lines with this shape; first: T3-001|T3-017]

0 errors (0 distinct shapes), 443 warnings
```

The 443 warnings are the unconfirmed gate pairs, read before the freeze. The leg closes with `done.sh B2 --cut packets-out`. The dispatch must read the five packets `P03-r2-1.md` to `P03-r2-5.md` in `out/_packets-B2/round-2/`.

## Leg B2b-r2-p2, check round 2, 2026-10-12

### QB2-005 and QB2-006, revisited

Both were applied at B2b-r2. The failed first dispatch is at `out/_analysis/fleet_B2_round2_failed/`, and it is never scored. No work of this leg rested on either assumption.

### Rounds 1 and 2 had different readers (J, 2026-10-12 07:34 Berlin)

- **Round 1:** deepseek/deepseek-v4-flash-0731, through `@preset/cheap`, at high reasoning effort on mixed providers.
- **Round 2:** deepseek/deepseek-v4.1-flash, called directly, at medium reasoning effort, with max_tokens 128,000.

J's reading: the preset refused even a 32-token probe with HTTP 400. So the part-6 failures of the first dispatch were most likely the preset or its provider pin, not the context window (OpenRouter lists V4.1 Flash at 1,048,576 tokens). The same readers serve B3 and B4. Every change from round 1 to round 2 below is partly a change of readers, not only of the scheme.

### The dispatch, in `fleet.py`'s counts

`_fleet_raw/B2/round-2/DONE` and `log.jsonl` record 5 packets, each sent to 3 fresh readers (15 readers, r1 to r3 inside each packet folder). There were 15 valid returns, 0 exhausted and 0 reissues. Calls took 67.6 to 235.7 seconds each. The round used 751,923 input and 489,651 output tokens, at a cost of 0.598 USD. All 150 lines came back.

One line mistyped its heading. In `P03-r2-5/r2`, position 7 returned AyyMD t02, where the packet holds AyyMD t08. Its concepts (c0037, c0041) are t08's, so it is scored as t08 by position.

### Round 2's three numbers

`out/_analysis/b2_score_r2.py` scores the round by the declared definitions, reusing `b2_score.py`'s Jaccard and alpha. `out/_analysis/b2_rechecked.py` builds the rechecked placements: each item's latest recheck, which moves 19 hard items. The next table gives the figures for the whole set and for its two parts.

| set | fidelity | primary match | fidelity vs rechecked | pairwise | primary pairwise | alpha |
|---|---|---|---|---|---|---|
| all 50 (the hard set) | 0.639 | 0.747 | 0.701 | 0.718 | 0.833 | 0.710 |
| the 40 round-1 items | 0.572 | 0.683 | 0.648 | 0.685 | 0.792 | 0.676 |
| the ten biggest bags | 0.911 | 1.000 | 0.911 | 0.850 | 1.000 | |

Round 1, on its 40 items, scored fidelity 0.594, pairwise 0.733 and alpha 0.726. On the same 40 items round 2 is lower on all three. 27 of 50 items have two readers differing; 24 of them are round-1 items.

The largest change is in how many themes a reader places. Round 2's readers placed more than one theme on 47 of 150 lines; round 1's placed more than one on 10 of 120. Most of round 2's divisions are a second or third theme added by one or two readers. Each comes with a `why_not_one` that reads "carry" as "cover every concept". Rule 0's words are the contract's and stay. The rate of second placements is a property of the reader model, and B3, which uses these readers, should expect it.

What these figures license, in FLEET.md's words: they support the claim "what you would have produced at a scale one analyst cannot reach". They do not support "what any competent reader would have produced".

**The ten biggest bags.** All 30 lines put my placed theme first (primary 1.000). Readers marked the six bags as bags on 11 of 18 lines. They also marked bags I did not: ainbowroad t11, dota2 t05, leagueoflegends t02 and theblackvoid t09 each drew one or two bag lines. `also_present` diverges widely. The themes a reader names, placed and also present, score a mean Jaccard of 0.283 against mine. On 2007scape t04 one reader named 85 themes (the other two 29 and 16). On sweden t01 the three named 34, 35 and 25; I named 5. QB2-008 asks J for a concept floor.

### The verdicts

The next table gives one verdict for each item that divided readers, and for each where all three readers left my placement. Stage B4's taxonomy names the kinds. "Rechecked" means my placement after round 1's rechecks.

| item | readers | verdict |
|---|---|---|
| guatemala t02 | all three T3-002, T3-167, T3-026; none T3-065 | scheme-ambiguous: the concepts say only "a flag" in r/guatemala, and two readers never opened G17. Edits 287, 290, 293, 294 |
| nVade t04 | T3-195, T3-195, T3-005 | scheme-ambiguous: a pledge honoured by defending had no T3-195 question against T3-011 or T3-005. Edits 288, 289, 295 |
| n64 t02 | T3-033+T3-002, T3-033+T3-038, T3-038 | scheme-ambiguous: no question between T3-033 and T3-038. Edits 291, 292 |
| dofus t01 | T3-033 in all three, seconds T3-092, T3-038 | the same pair; edits 291, 292 |
| AyyMD t08 | T3-001, T3-023, T3-023 | author-error: the moderator's takeover and CSS change (c0041, c0042) make it T3-023, as T3-023's question asks |
| nyu t01 | T3-070, T3-070, T3-004+T3-020 | author-error: coordinates, a moved spot and a template handed out are T3-070 |
| cubers t12 | T3-038, T3-044+T3-005, T3-044+T3-005+T3-021 | author-error: the tag is made to send lost cubers to the sub (c0075), so T3-044, not T3-169 |
| harrypotter t08 | T3-159, T3-031, T3-017+T3-159 | author-error: house points awarded for r/place work are a reward to helpers (T3-159) |
| farmcarrots t15 | T3-031 in all three, T3-050 in two | author-error: the room's carrot-joke replies lead; the taunt is the provocation |
| parabola t02 | T3-010 in all three, T3-150 in two | author-error: the border settled leads; my single T3-150 missed it |
| redhotchilipeppers t09 | T3-009, T3-009+T3-072+T3-073, T3-009 | author-error on my second theme, T3-043, which the readers do not need; T3-009 is primary in all three |
| Slovakia t07 | T3-065+T3-024, T3-024+T3-060, T3-024 | primary T3-024 matches all three; my second, T3-079, was drawn by none: author-error (Slovak hearts in the placehearts grid join no flags) |
| kpop t04 | all three T3-033, T3-066, T3-136 | genuine-joint: three readers agree on three themes; the vote proposal (c0024) and the turnout doubt have concepts of their own |
| floridagators t09 | T3-014+T3-152 in all three, T3-153 in two | genuine-joint: my original pair, plus the alliance meeting in the chat (c0124) |
| 4chan t07 | T3-010 in all three, T3-149 in two | genuine-joint: peace asked of the blue box (c0136, c0143) |
| anarcho_capitalism t12 | T3-149 and T3-010 in two, T3-149 alone in one | genuine-joint, as I placed it; one reader's T3-153 is a reader-error |
| simonfraser t08 | T3-084, T3-011+T3-084, T3-011+T3-084+T3-170 | genuine-joint: help sent (c0029, c0043) beside help asked |
| korea t15 | T3-015 in all three, T3-075 in one | genuine-joint by one reader, my original second |
| Goodboye t03, acecombat t05 | divided across T3-084, T3-151, T3-011; T3-010, T3-014, T3-062 | item-is-a-bag, as at round 1 |
| flashtv t13 | T3-009, T3-073, T3-073+T3-009 | two readers hold my rechecked T3-073; round 1's question holds; reader-error for the third |
| drumcorps t07, furry t10, placestart t15, stardustcrusaders t19, orderofthebluecorner t08 | one reader adds themes; the others hold my rechecked placement | reader-error: unneeded second placements |
| dota2 t05, leagueoflegends t02, theblackvoid t12 | all hold my primary; one or two add the themes I left in `why` | reader-error by rule 0, read strictly |

GreenCorner t03, WisconsinBadgers t04, england t03, megaman t11 and signal t01 are unanimous. Each falls on my rechecked placement: round 1's author-error verdicts, confirmed by new readers. There are eight author-error verdicts this round: AyyMD t08, nyu t01, cubers t12, harrypotter t08, farmcarrots t15, parabola t02, redhotchilipeppers t09 and Slovakia t07. They change no sentence, so they are listed here and not in `scheme_edits.jsonl`. `author_items.jsonl` stays as written.

### The edits

`out/_analysis/b2_edits_r2.py` wrote `scheme_edits.jsonl` lines 287 to 295, all scheme-ambiguous, with tier_history lines 373 to 381. They change 9 fields over 8 themes:
- T3-065's gloss now says a flag built in a room named for a land is that land's flag, unless its concepts name another.
- The T3-002/T3-065 and T3-026/T3-065 questions say so in both gates.
- A new T3-033/T3-038 question asks whether an idea is offered or a mark placed and reported. For a proposal followed by its placing, the side with more concepts is primary.
- New T3-195/T3-011 and T3-195/T3-005 questions ask whether an agreement is invoked, or the work helped or defended with the pledge only the reason.

No edit narrows a theme. `b1e_assemble.py --write` rebuilt `scheme.jsonl`, `families.jsonl` and `scheme.md`. `mem.py gates` finds no defect.

**The rechecks.** The nine edits owed 133 records over 59 items in the hard and gold sets. `out/_analysis/b2_rechecks_r2b.py` read each against its edit's sentence; none moves. `rechecks-B2.jsonl` holds 887 records, and none is owed.

**The gates.** I read ten pairs and confirmed them (`out/_analysis/b2_confirm_r2.json`): the five new or reworded pairs, and five whose confirmation the edits had made stale. 31 pairs are confirmed, 0 are stale and 464 are unconfirmed.

### Section 4

Round 2's packets hold 3 to 15 items, so round 1's curve (first ten items against last ten) cannot be drawn. Within the four packets of 9 or more items, I compared each reader's first half with its last half. The arguable rate falls in 8 of 12 readers and rises in 3. Agreement with the other two falls in 9 and rises in 2. The curve shows no sign that agreement grows with position. The B3 batch cap stays as declared: 40 items, the first 10 a warm-up block.

### Stopping (QB2-007)

Section 5 stops the rounds when pairwise agreement on the hard set clears the threshold. Round 2's figure on the 50-item hard set is 0.718, above 0.70. The PI's round-2 rule holds: the ten biggest bags have now been read once. But the 40 items both rounds share fell from 0.733 to 0.685, with new readers, and the ten bags lift the whole. QB2-007 asks J whether the rounds stop and the scheme freezes, or round 3 opens. Meanwhile the rounds stop under the declared rule, with the 40-item figure reported beside it. This leg does not freeze: the freeze needs the 464 unconfirmed pairs read and the decide_when_both clusters checked. The leg closes with `done.sh B2`.

**Questions open:** QB2-007 (stopping), QB2-008 (a floor for `also_present`).

### The close-check, B2b-r2-p2: return lines that break the specification (QB2-009)

`validate.py B2` reported 44 errors in 9 shapes, all in `_fleet_raw/B2/round-2/`. `fleet.py` had accepted every line. `out/_analysis/b2_r2_return_problems.py` lists 16 of 150 lines in `out/_analysis/b2_r2_return_problems.txt`:
- One line is incomplete: `P03-r2-2/r1`, ainbowroad t04, has third_order and why only. It lacks confidence, read, exemplar_read, families_opened, t_start, t and support.
- One line mistypes its heading: `P03-r2-5/r2` position 7 returned AyyMD t02 where the packet holds t08. Its five support concepts are t08's.
- 14 lines cite concept ids that are not the item's own, in support, also_present or multiplacement_log. They are on sweden t01 (three readers), ainbowroad t04 (two), 2007scape t04 (two), theblackvoid t09, theblackvoid t12, leagueoflegends t02, dota2 t05, donaldglover t04, duckgame t02 and ainbowroad t07. Each cited id belongs to another second-order theme of the same room, except c1636 on 2007scape t04, which is not a concept of r/2007scape at all.

Every line carries its third_order, and the scores use nothing else. The stage says a return that fails the specification is reissued, not scored. Reissuing is the dispatch's work, not mine. QB2-009 asks J whether the dispatch reissues the ten affected returns (packet 2 r1, r2, r3; packet 3 r1, r2; packet 4 r1, r3; packet 5 r1, r2, r3), or the lines are scored as they stand with their errors on the record.

Meanwhile the scores stand as computed on all 150 lines (`pilot_rounds.jsonl` line 2). No edit rests on an affected line: edits 287 to 295 came from guatemala t02, nVade t04, n64 t02 and dofus t01, whose lines are all within the specification. The AyyMD t08 author-error verdict rests partly on the mistyped line, one of its two T3-023 placements. The bag figures (primary 1.000, also_present Jaccard 0.283) rest partly on the affected lines. If the returns are reissued, I rescore, write a superseding pilot_rounds line, and revisit these. The leg stays open until the close-check passes.

### The bag recut: a proposal to J (QB2-010), not yet acted on

J ruled (QB2-008) that a second-order theme whose concepts spread over 16 to 85 third-order themes was cut too coarse. One item should sit in one theme most of the time, a few in two or three. Nothing below is cut until J's word.

**How coarse the themes are** (`out/_analysis/b2_recut_survey.py`, one line per theme in `b2_recut_survey.tsv`):
- The store's 7,844 second-order themes hold a median of 8 concepts (90th percentile 31, 99th 111, maximum 798).
- B1 placed 3,977 on one kind, 1,972 on two and 1,837 on three. It recorded 846 as bags, themes needing more than three kinds.
- 98 themes hold 100 or more concepts, together 14.5% of all concepts; 49 of them are B1 bags.
- With J's floor applied to round 2's also_present (three concepts of the item's own), readers still name 14 to 43 kinds on 2007scape t04 and 21 to 24 on sweden t01.

**A cut by thread does not work.** The bags were gathered across threads by what the concepts do. On ainbowroad t03, 309 of 326 concepts are alone in their thread; on sweden t01, 202 of 310. A neutral cut by thread would leave hundreds of one-concept parts. The cut has to be by doing, which is coding work.

**The sibling citations.** Most of round 2's failing lines cite concepts of sibling themes of the same room. They split into two groups:
- In packets 3 and 5 the sibling was in the same packet: theblackvoid t09 beside t12, ainbowroad t11 beside t07. The reader mixed two items of one room.
- In packets 2 and 4 the room had one item in the packet (sweden t01, ainbowroad t04, dota2 t05, leagueoflegends t02), so the cited ids were never shown. Room ids run in sequence, and an invented number in range nearly always lands on a sibling.

So the citations are not evidence that sibling themes overlap, and the proposal does not regroup siblings. Fleet ids stop the second group. For the first group, the packet builder could keep one item per room in a packet, with J's agreement.

**The proposal.**
1. **Which items.**
   - At once, before round 3: the hard set's six author bags (2007scape t04, theblackvoid t12, ainbowroad t03, t04 and t07, sweden t01) and the gold set's bags.
   - Before B3, by the same rule: every B1 bag (846 themes), and every theme of 100 or more concepts that round 3 shows to need more than three kinds.
   - The round-1 items I placed as bags in round 1 (Goodboye t03, acecombat t05) follow the same rule if they still need more than three kinds.
2. **By what rule.**
   - I read the theme whole, in a blind window (`mem.py blind on`), so B1's working placements are hidden.
   - I group its concepts into children, each one doing in the room's own terms. Each child gets a label and a note written as a second-order theme, with no third-order ids and no scheme words.
   - A child needs at least three concepts (J's floor). A concept that fits no child of three joins the nearest child by its doing.
   - Every concept goes to exactly one child, and the parent's concept ids are kept.
   - Then, outside the window, each child is placed like any item, with a target of one third-order theme and at most three. A child that still needs more than three is cut again.
3. **With which verbs.** No verb cuts a second-order theme today: `package/store` is read-only, and `reassign` re-places a theme only after a recut. I propose J adds two verbs:
   - **A recut writer**, `mem.py recut <sub>:<tNN> --child "label|note|c1,c2,..." --reason ...`. It writes a recut layer beside the store (`out/recut/themes.jsonl`, the children with new room ids after the room's last tNN, and `out/recut/codes.jsonl`, each concept's child). It marks the parent superseded, never deletes it, and logs kind split.
   - **Store readers** (`mem.py theme`, `codes --sub`, `packets.py`'s Store) that read the layer.

   The children also need fleet ids. J's table maker would draw new T2 ids from the same space, so `fleet_ids.jsonl` covers them.
4. **What it reopens of B1.**
   - `scheme_current.jsonl`: the parents' placements are superseded by the children's (13,432 placements and 7,786 placed themes change by the cut).
   - `multiplacement_log.jsonl`: the parents' bag records and rule 0 lines are superseded.
   - F-001's within-room grain claim, which counts kinds per theme, is recomputed.
   - Each third-order theme's member counts are recomputed, so its tier (rare at under two unlike rooms) is checked again; rooms per theme do not change.
   - `confusions.md` rates are recomputed where they count parents.

   Not reopened: the codes themselves (episodes and exemplars cite concept ids, which stay), the third-order scheme's sentences, and the rooms' notes.
5. **What it changes in B2.** `author_items.jsonl` stays as written. The children are appended as new lines (source "recut", with their parent), and the parents leave the hard set from round 3, so round 3's set is not round 2's on those items. Round 3's comparison with round 2 is reported on the 40 unchanged round-1 items. J may also prefer that round 3 keeps the parents beside the children, for one round's comparison.

**Fleet ids.** Round 3 is the first round with fleet ids. `out/_analysis/b2_packets_fleet.py` builds the packets: room name plus `T2-` theme ids and `C` concept ids; no room id in an id position; J's caps of 15 items and 180,000 bytes. A dry run on the current hard set (seed 20261013) gives five packets of 7 to 13 items. `out/_analysis/b2_translate_fleet.py` translates returns back before scoring and reports every id the table lacks, or that belongs to another room or theme. RETURN-B2.md now asks for fleet ids, and it carries J's floor: a theme enters `also_present` only with at least three concepts of its own. Its round-2 text is kept as `out/_analysis/RETURN-B2_round2.md`. B3's specification does not exist yet; the head carries both rules for it.

Two points for J:
- `validate.py` checks returns against room ids in `_fleet_raw`, so a fleet-id round will fail its concept check unless the check reads the translated copies (`out/_analysis/b2_r<K>_returns/`) or the table.
- No round-3 packet is built until J's word on the recut.

### QB2-007 and QB2-008, answered; fleet ids (J, 2026-10-12)

**QB2-007.** J rules that round 3 runs on the edited scheme with round 2's readers: deepseek-v4.1-flash, called directly, at medium effort. Round 3 is the first round in which only the scheme changes. My assumption, that the rounds stop, is withdrawn, and nothing is frozen. `pilot_rounds.jsonl` line 2 stands as round 2's record. The section "Stopping (QB2-007)" above is superseded by this ruling.

**QB2-008.** Yes to the floor: a theme enters `also_present` only with at least three concepts of its own. It is now in RETURN-B2.md, and the head carries it for B3's specification, which does not exist yet. J adds that the bags need a recut, proposed before round 3's packets and not cut before his word. The proposal follows (QB2-010).

**Fleet ids.** From round 3, and in B3, packets carry only fleet ids for codes and second-order themes (`out/fleet_ids.jsonl`, seed 20261012). My own files keep the room ids, and returns are translated back before scoring. Round 3 is the first round with fleet ids. A made-up code id lands on a real code about 7.5% of the time, and a made-up theme id about 7.8%; with room ids, an invented c-number in range almost always landed on a sibling.

### QB2-009, answered: the 16 lines waived, round 2 scored as it stands

J ruled (2026-10-12, 09:27 Berlin): no reissue of round 2. The 16 lines in `out/_analysis/b2_r2_return_problems.txt` are waived by name, in `out/return_waivers.jsonl` (`out/_analysis/b2_waivers_r2.py`). Each line names the round folder, the file, the item as the line writes it, the problem as listed, and J's ruling. The AyyMD line's reason also names its mistyped heading. `validate.py B2` skips the waived lines and counts them aloud.

Round 2 stays scored on third_order, as before. `pilot_rounds.jsonl` line 2, the verdicts and edits 287 to 295 stand unchanged; nothing rested on a reissue.

The 16 lines are reader faults:
- one incomplete line: packet 2 r1, ainbowroad t04;
- one mistyped heading: packet 5 r2, AyyMD t02 for t08;
- 14 lines citing concepts that are not the item's own.

The faults came from two things, and both are artefacts of room ids:
- **Room ids repeat across rooms.** c0006 names two different concepts in packet 2, one in each of two rooms.
- **Invented ids land on sibling codes.** A room's ids run in sequence, so an id a reader makes up within range nearly always names a real concept of a sibling theme. Examples are c0558 on sweden t01 and c1556 on ainbowroad t04, neither ever shown in their packets. Where two items of one room shared a packet (theblackvoid t09 and t12, ainbowroad t07 and t11), readers also took concepts from the other item.

From round 3 the fleet ids of `out/fleet_ids.jsonl` end both: no id repeats, and a made-up id lands on a real code about 7.5% of the time. `fleet.py` rejects, and reissues in the dispatch, a line citing an id not under its item. For that check, round 3's builder `out/_analysis/b2_packets_fleet.py` writes `codes_by_item` into each packet's MANIFEST entry: the item's fleet theme id, as the line writes theme_id, with the fleet code ids served under it. Tested on guatemala t02 (8 codes) and sweden t01 (310). No round-3 packet is built yet: QB2-010, the recut, waits for J's word.

### The close-check, B2b-r2-p2

`validate.py B2` reported:

```
stage B2:
  leg: check (2 dispatch folders with DONE)
  _fleet_raw/B2/round-1: 3 readers, 120 return lines
  _fleet_raw/B2/round-2: 15 readers, 150 return lines, 16 waived by J (return_waivers.jsonl)
  author items 50, gold items 40, rounds scored 2, edits 295 (author-error 4), scheme ids 197 (scheme/scheme_current.jsonl)

warn   scheme.jsonl: the pair T3-001|T3-017 touches an edited theme and is not confirmed against its current sentences (mem.py gates T3-001 T3-017 --confirm --reason ...)  [443 lines with this shape; first: T3-001|T3-017]

0 errors (0 distinct shapes), 443 warnings
```

The 443 warnings are the unconfirmed pairs that touch an edited theme; they are read before any freeze. The leg closes with `done.sh B2`. Round 3 opens (QB2-007). Its build waits for J's word on the recut (QB2-010), and its packets carry fleet ids.

### QB2-010: the bags split (J approved, 2026-10-12 09:32 Berlin)

J approved the cut as proposed, at medium effort. The handler installed `mem.py split`. It writes `out/recut/themes.jsonl` and `out/recut/codes.jsonl` beside the read-only store and gives each child the room's next free tNN and a fleet id in `out/fleet_ids.jsonl`. The parent is superseded, never deleted. Each child names me ("analyst") as its author and names the parent it supersedes.

**How the cut was made.** I read every bag whole in one blind window (`mem.py blind on`, closed at 07:49:15), with B1's placements hidden. I grouped each bag's concepts into children by what the concepts do; each child has at least three concepts, and every concept is in one child. Each cut is written in `out/_analysis/b2_split_<sub>_<tNN>.txt` and was run by `out/_analysis/b2_split_run.py`. The helper checks coverage and the three-concept floor against the store before it calls `mem.py split`.

`mem.py theme` printed some concept lines blank (c0084, c0505, c0595 and c0960 of 2007scape t04, for example). I read the bags with `mem.py codes --sub S --second tNN`, and the helper's coverage check named every concept I had not yet assigned. Each one was read and assigned.

**The six hard-set bags became 54 children.** The next table lists each bag with its children and their sizes.

| bag | children | the children (concepts) |
|---|---|---|
| 2007scape t04 (349) | t15 to t28 | proposing what to make 48; the design's spot, size and look 20; building and reporting 85; coordinates and references 12; fixing misplaced pixels 22; defending the corner 11; covering others' art 13; refusing to give up the corner 6; dealing with neighbours 35; Trump politics with r/The_Donald 13; pride in working together 35; the flood of r/place posts 7; jokes and asides 38; pushing posts up 4 |
| sweden t01 (310) | t08 to t17 | building, cleaning and holding the flag 54; defending it and calling out vandals 18; taking over the Danish flag and neighbours 28; Swedish emblems on the flag 44; other rooms asking for space 51; other rooms asking for help 22; settling with neighbours and letting art stay 31; Nordic friendship 9; looking back and the Maryland friendship 27; off-topic talk 26 |
| theblackvoid t12 (335) | t16 to t25 | hailing the Void and its creed 88; calling it to consume named targets 71; keeping and defending the cores 43; arguing what the true Void is 30; leaving other colours for the Void 11; other rooms dealing with the Void 15; critics and taunts 21; looking back after its end 10; jokes and asides 36; new cores elsewhere 10 |
| ainbowroad t03 (326) | t14 to t21 | alarms and fighting the Void 59; alarms about other attacks and collisions 70; calls to attack other rooms' work 22; war and peace with Blue and others 33; dealing with the Void 38; other rooms asking for help or to be spared 61; routing the road and proposing designs 30; hostility and insults against the road 13 |
| ainbowroad t04 (327) | t22 to t27 | repairing the road itself 103; repairing and protecting other rooms' art 74; deciding to spare and share space 38; other rooms asking to be spared or helped 96; defending the road 12; looking back 4 |
| ainbowroad t07 (311) | t28 to t33 | extending the road and planning its course 50; proposing pictures and features for it 156; other rooms asking for space on it 38; working beside neighbours without harming their art 39; the Gilbert Baker memorial 5; shards, takeovers and disputes over its spread 23 |

The hostility child of ainbowroad t03 holds "KILL THE GAYS" (c1395), posted to the room; it is kept and served as it stands.

**The gold set's eight B1 bags.** One was cut: dankmemes t16 (12 concepts) became t18, pointing out drawings on the canvas (5), and t19, reporting the build failed and mourning the canvas (7). Seven were not cut:
- cuboulder t04 and ukraine t07 hold 5 concepts each, so no two children of three exist.
- Villanova t01 (building a logo together), tinytardis t06 (negotiating shared space), edboxes t02 (recruiting hands and arranging the next shift) and alberta t04 (arguing whether to attack the Quebec flag) each read as one doing.
- finland t06 holds one doing of 5 concepts (moderators gathering the canvas posts) and three single concepts that each do something different; a second child would mix doings.

These small themes were B1 bags because nearly every concept did something different. With a floor of three concepts per child, they cannot be cut.

**The children placed.** I placed the 56 children like any item after the window closed (`out/_analysis/b2_author_split.py`). The 54 hard-set children were appended to `author_items.jsonl` and the 2 gold children to `gold_items.jsonl`. Each line carries its parent, source "split", `support_by_theme` and its fleet theme id. 40 children take one theme and 16 take two; each second theme has concepts of its own, named on the line. No child needs more than three themes, so none is a bag. The parents' lines stay as written. `author_items.jsonl` now has 104 lines and `gold_items.jsonl` 42. Round 3's hard set is the 44 unsplit items and the 54 children: 98 items.

**The rechecks.** The children sit on themes that earlier edits changed, so 86 edits owed them 526 rechecks. I read each edit's changed sentence against the children it owes (`out/_analysis/b2_rechecks_split_show.txt`), and none moves a child. The closest call is ainbowroad t24's second theme, T3-010: three of its five concepts invoke agreements already made, which T3-195 names. It stays, because the trimming to the agreed size is itself the border being settled. The 526 records were written with `out/_analysis/b2_rechecks_split.py`, one reason per edit. `rechecks-B2.jsonl` has 1,413 records, and none is owed.

**What the split leaves for the check (QB2-011).** `validate.py B2` reports 698 errors in five shapes. All come from the split layer meeting records made before it:
- 56 items not in `package/store/themes.jsonl`: the item check reads the store, not the split layer.
- 186 round-2 return lines and 454 rechecks whose concepts now resolve to the children, not the parents they name.
- `pilot_rounds.jsonl` lines 1 and 2: n_items 40 and 50 against a hard set counted as 104, the parents included.

QB2-011 asks J whether the check should read the split layer for items, keep a parent's own concepts for records that name the parent, and count the hard set without the superseded parents. Meanwhile the leg stays open. No round-3 packet is built. The 846 B1 bags wait for J's word.

### QB2-011, answered: the check reads the split layer

The handler fixed the three error shapes in `tools/vlib.py` and `tools/checks/stage_B2.py`. They were faults of the check, not of the run.
- A split child counts as a second-order theme, and its parent stays one. `author_items.jsonl` and `gold_items.jsonl` resolve both.
- A split concept belongs to its child and to every theme it was split from. Records made before the split about a parent pass; a concept of a sibling child still fails.
- A round's n_items is held to the items its own MANIFEST sent (`out/_packets-B2/round-K/MANIFEST.json`), as the handler's correction says.

My assumption needed no revisit. I recorded the 526 rechecks and left these shapes to the check, which now passes. Round 3's packets carry the children, not their parents.

### The close-check, B2b-r2-p2, after the split

`validate.py B2` reported:

```
stage B2:
  leg: check (2 dispatch folders with DONE)
  _fleet_raw/B2/round-1: 3 readers, 120 return lines
  _fleet_raw/B2/round-2: 15 readers, 150 return lines, 16 waived by J (return_waivers.jsonl)
  author items 104, gold items 42, rounds scored 2, edits 295 (author-error 4), scheme ids 197 (scheme/scheme_current.jsonl)

warn   author_items.jsonl has 104 items; section 1 says forty to sixty
warn   scheme.jsonl: the pair T3-001|T3-017 touches an edited theme and is not confirmed against its current sentences (mem.py gates T3-001 T3-017 --confirm --reason ...)  [443 lines with this shape; first: T3-001|T3-017]

0 errors (0 distinct shapes), 444 warnings
```

`author_items.jsonl` holds 104 lines: the six superseded parents kept as written, beside their 54 children. Round 3 sends 98 items. The 443 pair warnings are the unconfirmed pairs, read before any freeze. The leg closes with `done.sh B2`. Next comes round 3's build: `b2_packets_fleet.py --round 3` on the 98 items, with the superseded parents left out and fleet ids only. The 846 B1 bags wait for J.

## Leg B2a-r3, build round 3, 2026-10-12

### The answers this leg was told to read

QB2-007 to QB2-011 were all applied at B2b-r2-p2:
- round 3 runs on the edited scheme with round 2's readers;
- `also_present` takes a theme only with three concepts of its own, and the bags were split;
- the 16 faulty lines are waived;
- the split was approved;
- the check reads the split layer.

Nothing in this leg rests on an assumption.

### What was built

Round 3 is the first round in which only the scheme changes (QB2-007), and the first with fleet ids (J, 2026-10-12).

**Items.** Round 3 serves 98 items: the 44 unsplit hard items and the 54 children of the six split bags. The six parents (2007scape t04, sweden t01, theblackvoid t12, ainbowroad t03, t04 and t07) are not served. `author_items.jsonl` keeps their lines as written, so it holds 104 lines.

**The packets.** `out/_analysis/b2_packets_fleet.py` built the round, with two changes this leg. It now reads the split layer by giving `packets.py`'s Store the `out/` path. It also leaves out any item whose children are in `out/recut/themes.jsonl`. The round has seven self-contained packets in `out/_packets-B2/round-3/`, cut from the order seeded with 20261013. The next table lists them.

| packet | items | bytes of item text |
|---|---|---|
| `P03-r3-1.md` | 10 | 113,527 |
| `P03-r3-2.md` | 13 | 112,021 |
| `P03-r3-3.md` | 15 | 42,159 |
| `P03-r3-4.md` | 15 | 48,792 |
| `P03-r3-5.md` | 15 | 88,494 |
| `P03-r3-6.md` | 15 | 31,082 |
| `P03-r3-7.md` | 15 | 91,999 |

Each packet is within J's caps: at most 15 items and 180,000 bytes of item text, with no item split. The items per packet are in `out/_analysis/b2_order_r3.json`. Beside the packets are `index.md` and `G01.md` to `G21.md`, built from the edited `scheme.jsonl`.

**Fleet ids.** Each item is headed by its room and its `T2-` id, and each concept by its `C` id. The builder stops if a room id would stand in an id position, and none did. `MANIFEST.json` gives each packet its item count and `codes_by_item`: the fleet theme id of each item with the fleet code ids served under it. With that entry, `fleet.py` rejects and reissues any line that cites a code its item does not hold (QB2-009). Returns are translated back to room ids with `out/_analysis/b2_translate_fleet.py` before scoring; the check translates them through `out/fleet_ids.jsonl` itself (QB2-010).

**RETURN-B2.md.** It is unchanged since B2b-r2-p2. It asks for fleet ids and carries the floor of three concepts of its own for `also_present`.

**Manifest.** `run_manifest.json` has a round-3 entry (`out/_analysis/b2_manifest_r3.py`). It records the same readers as round 2 (deepseek/deepseek-v4.1-flash, called directly, medium effort, max_tokens 128,000), the seed, 98 items, and every packet's bytes and hash.

**One packing matter for J.** Some packets hold several children of one parent; for example, packet 3 holds ainbowroad children beside one another. At round 2, readers took concepts from a sibling item in the same packet. With fleet ids and `codes_by_item`, `fleet.py` now catches such a citation and reissues the reader. Packing one item per room per packet was proposed at B2b-r2-p2 and not ruled on, so it is not applied.

### The close-check, B2a-r3

`validate.py B2` reported:

```
stage B2:
  leg: check (2 dispatch folders with DONE)
  _fleet_raw/B2/round-1: 3 readers, 120 return lines
  _fleet_raw/B2/round-2: 15 readers, 150 return lines, 16 waived by J (return_waivers.jsonl)
  author items 104, gold items 42, rounds scored 2, edits 295 (author-error 4), scheme ids 197 (scheme/scheme_current.jsonl)

warn   author_items.jsonl has 104 items; section 1 says forty to sixty
warn   scheme.jsonl: the pair T3-001|T3-017 touches an edited theme and is not confirmed against its current sentences (mem.py gates T3-001 T3-017 --confirm --reason ...)  [443 lines with this shape; first: T3-001|T3-017]

0 errors (0 distinct shapes), 444 warnings
```

The leg closes with `done.sh B2 --cut packets-out`. The dispatch sends each of the seven packets to three fresh readers.

## Leg B2a-r3-p2, the split withdrawn and round 3 rebuilt, 2026-10-12

### The split, withdrawn

**What was cut.** At B2b-r2-p2 (QB2-010) I split six bags of the hard set and one gold bag with `mem.py split`, in one blind window. 2007scape t04 became 14 children, sweden t01 10, theblackvoid t12 10, ainbowroad t03 8, ainbowroad t04 6 and ainbowroad t07 6. In the gold set, dankmemes t16 became 2. The 56 children are in `out/recut/themes.jsonl`, and their concepts in `out/recut/codes.jsonl`. I placed each child and recorded 526 rechecks for them. The B2a-r3 round 3 served 98 items: 44 unsplit items and 54 children.

**Why J withdrew it** (J, 2026-10-12, 12:04 to 12:10 Berlin). Bags are a coder problem. Second-order themes are the coders' to cut, and the aggregator takes them as given. The split was a mistake, so the run goes back to before any cut and goes on from there, inside this run, with nothing deleted.

**What the withdrawal did.**
- `out/recut/WITHDRAWN.json` holds J's ruling word for word. From it on, every tool reads the store as it was before the split: the six parents and the gold bag stand again, and the 56 children are gone from every view. `out/recut/` stays as written.
- `out/_analysis/b2_split_withdraw.py` moved the children's placement lines, unchanged and in order, to `out/_analysis/author_items_split_withdrawn.jsonl` (54 lines) and `out/_analysis/gold_items_split_withdrawn.jsonl` (2 lines). `author_items.jsonl` again holds 50 lines and `gold_items.jsonl` 40, the counts J named.
- `mem.py split` now refuses. A bag stays one item: one theme placed, and every other theme under `also_present` with at least three concepts of its own (QB2-008).

**Records that belong to the withdrawn split.** No figure counts these. `out/_analysis/b2_split_withdrawn_count.py` matched each file against the 56 children.
- `out/recut/` (themes and codes, kept as written).
- `out/_analysis/author_items_split_withdrawn.jsonl` and `gold_items_split_withdrawn.jsonl`.
- `rechecks-B2.jsonl` lines 888 to 1,413: 526 rechecks of the children, all from B2b-r2-p2. They stay in the file so that they still resolve. Lines 1 to 887 stand.
- The 56 lines of `out/fleet_ids.jsonl` marked `"split": true`.
- The 98-item round 3: its packets, moved to `out/_analysis/b2_packets_round3_split_withdrawn/`, its order, renamed `out/_analysis/b2_order_r3_split_withdrawn.json`, and the B2a-r3 round-3 entry in `run_manifest.json`.
- The cut files and scripts in `out/_analysis/`: `b2_split_*.txt`, `b2_split_run.py`, `b2_author_split.py` and `b2_rechecks_split.py`.
- In this file: "QB2-010: the bags split", "QB2-011, answered", "The close-check, B2b-r2-p2, after the split", and the B2a-r3 section.

The split wrote no line on a child in `scheme_current.jsonl`, `multiplacement_log.jsonl`, `tier_history.jsonl`, `exemplar_candidates.jsonl` or `scheme_edits.jsonl`, so nothing there needs superseding.

**What stands.** Round 2's scores. The 16 waivers in `return_waivers.jsonl` (QB2-009). Edits 287 to 295 and their 133 rechecks (records 755 to 887). The 31 confirmed gate pairs.

**The B1 bags.** This run splits none of them. J will decide how the coders recut them. J's ruling counts 841 B1 bags; my head said 846, and I have not reconciled the two counts.

### Round 3 is round 2's set

Round 3 serves round 2's 50 hard items, each bag as one item. The six parents are served whole; for example, sweden t01 is served as one item with its 310 concepts. `out/_analysis/b2_packets_fleet.py` now leaves out no parent when `out/recut/WITHDRAWN.json` exists. It built five self-contained packets from the order seeded with 20261013. The next table lists the packets.

| packet | items | bytes of item text |
|---|---|---|
| `P03-r3-1.md` | 12 | 89,418 |
| `P03-r3-2.md` | 13 | 135,742 |
| `P03-r3-3.md` | 8 | 98,208 |
| `P03-r3-4.md` | 7 | 98,843 |
| `P03-r3-5.md` | 10 | 95,887 |

Each packet is within J's caps: at most 15 items and 180,000 bytes of item text, with no item split. The items per packet are in `out/_analysis/b2_order_r3.json`. `index.md` and `G01.md` to `G21.md` are built from the edited `scheme.jsonl`. Each `MANIFEST.json` entry carries `codes_by_item`. `RETURN-B2.md` is unchanged.

**Fleet ids** (J, 12:15 Berlin: `fleet.py` refuses a packet with `codes_by_item` if any room code or room theme id appears in its text, headings included). `out/_analysis/b2_r3_roomid_scan.py` scanned the five packets and the 22 shared pages and found 0 room ids. The same pattern finds 50 room ids in `b2_order_r3.json`. All 50 item headings carry `T2-` ids, and all 4,094 concept lines carry `C` ids.

**Manifest.** `run_manifest.json` now has 6 entries. The new round-3 entry (`out/_analysis/b2_manifest_r3b.py`, leg B2a-r3-p2) records 50 items in 5 packets and supersedes the B2a-r3 entry. The readers are round 2's: deepseek/deepseek-v4.1-flash, called directly, medium effort, max_tokens 128,000.

Round 3 is the first round in which only the scheme changes (QB2-007). Its check compares it with round 2 item for item.

### The close-check, B2a-r3-p2

`validate.py B2` reported:

```
stage B2:
  leg: check (2 dispatch folders with DONE)
  _fleet_raw/B2/round-1: 3 readers, 120 return lines
  _fleet_raw/B2/round-2: 15 readers, 150 return lines, 16 waived by J (return_waivers.jsonl)
  author items 50, gold items 40, rounds scored 2, edits 295 (author-error 4), scheme ids 197 (scheme/scheme_current.jsonl)

warn   scheme.jsonl: the pair T3-001|T3-017 touches an edited theme and is not confirmed against its current sentences (mem.py gates T3-001 T3-017 --confirm --reason ...)  [443 lines with this shape; first: T3-001|T3-017]

0 errors (0 distinct shapes), 443 warnings
```

The leg closes with `done.sh B2 --cut packets-out`. The dispatch sends each of the five packets to three fresh readers.
