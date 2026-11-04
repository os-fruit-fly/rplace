# Notes, stage B3

## Leg B3a, the build, 2026-10-12

### Declarations, made before any packet exists

The allocator is `out/_analysis/b3_allocate.py`. Its dry run gave the counts below; the batches are written after these declarations.

**The unit and the frame.** Every second-order theme of the analysed set: 705 rooms (the census; none dropped) and 7,844 second-order themes, which is `counts.py`'s `assignment_items_expected`.

**R = 2.** Each room is read by two readers, one per replicate, never the same reader. Two readers make a disagreement visible, and stage B4 rules on it. A third reader would cost half the fleet again to turn a disagreement into a vote, and rule 13 says a vote is not a warrant. A higher R would have bought a per-item majority and an estimate of each item's reliability; it would not have bought a better placement, and stability was measured once, in the pilot (`stability-B2.md`, 0.807).

**The seed.** 20261015. The connectivity gate forced 7 redraws; the allocation stands under the suffix `20261015:redraw7`, from which it is reproducible.

**The item cap per batch: 40**, from `notes-B2.md`. Every packet file must stay under FLEET.md's 50 KB ceiling, which the B3 check asserts. So the allocator packs whole rooms to 40 items and 44,000 bytes of rendered text (the items in fleet ids and the rooms' sibling blocks), leaving room under the ceiling for the batch's header, its gold copies and its duplicate.

A room that leaves less than 6,000 bytes or 4 items under those limits is large: it opens a batch of its own, which takes at least one more room so that it is no island in the room-batch graph, and is served in parts to one reader in one conversation (stage B3 section 1.2). Such a batch holds up to 40 items and 160,000 bytes, or the large room's own size and 12,000 bytes more. Two rooms hold more than 40 items; each takes at most 3 more items beside it, so its batch may exceed the cap by that much (54 positions at most, with its copies). B2's pilot rounds served packets of up to 135,742 bytes of item text to one reader without fault; 160,000 bytes in parts keeps a reader's conversation near that.

Batches: one-file batches hold a median of 27 positions. 332 of the 624 batches are served in parts.

**The cost**, for the token record (no stage carries a budget, contract section 4). B2's gold round cost 0.026 USD a reader for 14 items, about 32,000 input tokens (the index and the families opened, about 28,000) and 25,000 output tokens. Here: about 40 MB of item text over the whole fleet (about 11 million input tokens) and 624 readers' shared pages (about 17 million), with about 1,800 output tokens a position for 17,089 positions and the second pass (about 31 million or more). By B2's gold round's prices the fleet costs about 30 to 40 USD.

**The warm-up block: in reserve.** Stage B3 section 1.2 uses a warm-up only if stage B2 found a convention still forming inside a round, its readers improving from first items to last. B2 found the opposite: agreement with the other two readers fell from the first half of a packet to the last in 9 of 12 readers at round 2 and 9 of 15 at round 3, on packets too short (7 to 15 items) for a first-ten against last-ten curve. `notes-B2.md` had declared a 10-item warm-up at B2a-r1; this declaration replaces it, and the position curve of the check leg decides whether it is needed (QB3-001).

**The gold seeding rate: one gold copy per 20 items**, as `notes-B2.md` declared, at most two per batch. In each batch the expected number is its item count over 20; the whole part is seeded and the fraction seeded by a seeded draw. 777 gold copies are seeded; each of the 40 gold items is seeded 19 or 20 times, drawn round-robin from a seeded order.

**The gold policy (stage B3 section 1.6).**
- A gold copy goes into a batch that does not hold its room, at most once, at a position no other reader holds that gold item at.
- Gold copies are tagged in `batches-B3.jsonl` (`gold_items`), never in the payload: the packet shows a gold copy as any other item, under its fleet id, and the reader cannot tell it from a corpus item.
- A gold item is also a corpus item, read in its own room's batch. The scorer tells the seeded copy from the live reading by (item, agent, replicate). The check leg reports the seeded readings and the corpus readings of those items separately.
- Seeded copies are excluded from every denominator downstream; stage B4 drops them before it writes `assign_final.jsonl`.
- `gold_items.jsonl` and nothing derived from it reaches `_packets-B3/` or `_fleet_raw/B3/`.
- A gold copy is listed in its batch's `items` as well as in `gold_items`, so that `n_items` counts every position the reader answers (QB3-001).

**The duplicate.** One item per batch, an item of the batch's own, presented twice at positions at least a quarter of the batch apart, tagged in `duplicate_items`.

**The batch count and the reader count**, computed by the allocator from its own packing: 624 batches, 624 readers (one reader per batch), 17,089 positions in all (15,688 readings at items × R, 624 duplicates, 777 gold copies).

**The exemplar arm: none.** No exemplar is served to any reader, as in B2, so that B3's figures compare with B2's within one arm (the description alone). The return line carries `exemplar_read: null`.

**The order of batches.** A seeded shuffle of the 624 batch ids (`out/_analysis/b3_dispatch_order.json`), dispatched in two groups: the first 60 batches, then the other 564. The gold fidelity check of stage B3 section 3.2 runs after group 1 and decides whether group 2 is sent.

**The reissue policy** (`fleet.py`, stage B3 section 2): a batch that comes back missing, truncated, malformed or short of its item count goes whole to a fresh reader id holding none of its rooms, up to twice, recorded as `reissue` 1 or 2 with the original reader id. When reissues are exhausted on a batch, the dispatch stops and reports, and the build leg rebuilds those packets.

**The bag flags.** The ten biggest bags of `notes-B1.md`: 2007scape t04, theblackvoid t12, ainbowroad t04, t03 and t07, sweden t01, leagueoflegends t02, theblackvoid t09, ainbowroad t11 and dota2 t05. Each is marked in its packet, on the item, with the instruction unchanged: place from the concepts, not from the coder's grouping. `batches-B3.jsonl` lists them in `bag_flags`.

**Fleet ids (J).** Every packet carries only fleet ids for concepts and second-order themes, in headings, concept lines and sibling blocks alike, and each MANIFEST entry carries `codes_by_item` for `fleet.py`'s citation check. Returns are translated back to room ids before scoring.

**What rests on QB3-001 (asked 2026-10-12).** The 50 KB file ceiling with parts for large rooms; leagueoflegends t02 (89 KB alone) split across two consecutive parts of one reader, one item and one line; gold copies listed in `items`; the multiplacement records riding on the item line and the second pass in lines carrying `revises`; the warm-up in reserve and no exemplars.

### The build

**The allocation** (`out/_analysis/b3_allocate.py --seed 20261015`, written to `batches-B3.jsonl`).
- **Packing.** For each replicate, the 705 rooms are shuffled under the seed and packed by first fit into the open batches.
- **Large rooms.** A large room opens a batch served in parts, which first takes one ordinary room beside it.
- **Why that rule.** Two earlier drafts left large and near-large rooms alone in both replicates. Each such room was an island, and the connectivity gate could not pass on any of 20 redraws.
- **Redraws.** The final rule passed after 7 redraws.
- **Coverage, from the batches.** Each replicate holds the 705 rooms and the 7,844 items, every room whole, in one batch per replicate.
- **Gates.** Gate 1 holds: one reader per batch, and a room's two batches sit in different replicates. Gate 2 holds: the room-batch graph is one component.

The next table lists the counts.

| figure | value |
|---|---|
| batches (one reader each) | 624 (replicate 1: 310, replicate 2: 314) |
| batches served in parts | 313 |
| packet files | 1,080, every one under 50 KB (largest 50,878 bytes) |
| positions | 17,089 (15,688 readings, 624 duplicates, 777 gold copies) |
| gold copies per gold item | 19 or 20 |
| items per batch | 13 to 54, median 27 |

**The packets** (`out/_analysis/b3_packets_fleet.py`, in `out/_packets-B3/`).
- **Structure.** `index.md` and `G01.md` to `G21.md` come from `scheme_final.jsonl` with no exemplars. Each batch file has a title naming the batch and its replicate, the brief, a sibling block per room, the items in position order and the end line.
- **Fleet ids.** Only fleet ids appear: `T2-` ids in item headings and sibling blocks, `C` ids on concept lines.
- **Rooms.** A gold copy's room gets a sibling block like the batch's own rooms, so no reader can tell the copy from a corpus item.
- **Bag flags.** The ten flagged bags carry one line under the heading: "flagged as a bag: place from the concepts, not from the coder's grouping."
- **MANIFEST.json.** It gives each file the lines due from it, bytes, sha256, the count key and `codes_by_item`, and for parts the group, part and part count. It lists 17,089 due lines in all.

**One coder note held a room id.** nyjets t11's `theme_note` says "Code c0104 remains instead with...". The packet serves that code as its fleet id; the note's words are unchanged. No other label or note in the store holds a room id.

**Strings shaped like room ids.** Two packets (B059, B449) carry "t34" and "t90" in a warthunder participant's words. These are tank names (the T-34 and the T-90) and no id of any room in those packets; warthunder's themes run t01 to t15. Participants' words are never altered (QB3-002, point c).

**Items longer than a part.** Five placements run over two consecutive parts of one reader. leagueoflegends t02 (89 KB) is in B282 and B463. ainbowroad t11 (48 KB) is in B157, and twice in B523, as that batch's duplicate. The heading repeats with "(continued)", and the item's line is due after the part it ends in, so some parts are due 0 lines, B282-p2 for one (QB3-001, point 2; QB3-002, point d).

**The return specification.** `RETURN-B3.md` sets the order: rule 0 in the contract's words; the prediction line; the return line, with `bag` and with `also_present` under J's two rulings, word for word; the multiplacement record on the line; the second pass, one line per position carrying `revises`; the end marker and the confirmation.

**The manifest.** `run_manifest.json` has a B3 entry, 10 entries in all. It records the readers (deepseek/deepseek-v4.1-flash, direct, medium effort, max_tokens 128,000), the seed and its suffix, R, 624 agents, the counts, the groups (60 and 564), the frozen scheme's sha256 and `RETURN-B3.md`'s.

### The close-check, B3a

`validate.py B3` reported:

```
stage B3:
  batches 624, R 2, rooms 705, graph one component
  leg: build (0 dispatch folders with DONE)

ERROR  batches-B3.jsonl B001 lists item polska/t10 from a room not in its rooms; a batch holds whole rooms  [777 lines with this shape; first: B001]
ERROR  batches-B3.jsonl B157 holds room ainbowroad without 20 of its second-order themes (['t14', 't15', 't16']); no room is ever split  [10 lines with this shape; first: B157]
ERROR  batches-B3.jsonl: replicate 1 lacks 56 of the 7900 items assignment_items_expected counts (['2007scape/t15', '2007scape/t16', '2007scape/t17'])
ERROR  batches-B3.jsonl: replicate 2 lacks 56 of the 7900 items assignment_items_expected counts (['2007scape/t15', '2007scape/t16', '2007scape/t17'])

789 errors (4 distinct shapes), 0 warnings
```

**What the errors are.**
- **The 777 gold copies.** These are listed in `items` so that `n_items` counts every position. The check's whole-room rule has no exemption for them (QB3-001, point 3).
- **The other three shapes.** They come from the check reading the 56 children of the withdrawn split from `out/recut/`. It counts 7,900 items where the analysed set holds 7,844, and it says 10 rooms are split where the batches hold them whole (QB3-002, point a).

None of these is a fault in the batches. The leg stays open until the handler answers QB3-001 and QB3-002. Nothing is rebuilt meanwhile.

### Declarations revised under J's ruling (QB3-001, QB3-002; 16:37 Berlin), before the new packets

**J's ruling.**
- **Packet shape.** B3 uses B2's packet shape. Every packet is self-contained: at most 15 items and 180,000 bytes of item text, no MANIFEST group, part or parts, and its own item count. No item is split across packets.
- **Rooms.** A room may be spread over several packets; each packet carries the sibling block of every room it holds items from.
- **Gold copies.** They are listed in `items` and in `gold_items`, exempt from room membership and left out of coverage.
- **Returns.** Multiplacement records ride on the item line. Pass-2 lines carry `revises` after the pass-1 lines in the same return.
- **Warm-up and exemplars.** The warm-up stays in reserve, and no exemplars are served.
- **The handler's fixes.** The check now expects 7,844 items and ignores the withdrawn split. `fleet.py`'s room-id guard reads id positions only. A packet with 0 lines due is accepted.

**What changed in the build.**
- **Superseded, kept under new names.** The first build's whole-room batches served in parts: `out/_analysis/batches-B3_parts_superseded.jsonl`, `packets-B3_parts_superseded/`, `b3_dispatch_order_parts_superseded.json` and `RETURN-B3_parts_superseded.md`. The split of leagueoflegends t02 over two parts goes with them.
- **Stand as declared above:** R = 2; the seed 20261015; the gold rate and policy; one duplicate a batch; no exemplars; the warm-up in reserve; the reissue policy; the bag flags.

**The item cap: 15 positions a batch** (corpus items, gold copies and the duplicate's second copy) **and 180,000 bytes of item text** (J). The allocator (`out/_analysis/b3_allocate2.py`) works as follows:
- **Order.** For each replicate it shuffles the 705 rooms under the seed and pours their items in that order. A room's items stay together and run on into the next batch when one is full.
- **Room left in each batch.** It holds back one position for the duplicate's second copy and one for an expected gold copy. It also holds back 40,000 bytes of the byte cap.
- **The largest item fits.** leagueoflegends t02 (89,161 bytes) fits whole in one packet. No item is over 180,000 bytes.

**The allocation** (seed 20261015, under the suffix `20261015:redraw2`: the connectivity gate forced 2 redraws).
- **Batches.** 1,210 batches (605 a replicate), one reader each: 1,210 readers.
- **Positions.** 17,653 in all: 15,688 readings at items × R, 1,210 duplicates and 755 gold copies. Each gold item is seeded 18 or 19 times.
- **Batch size.** Batches hold 5 to 15 positions, median 15, and at most 178,588 bytes of item text.
- **Rooms.** 996 of the 1,410 room-replicates are spread over more than one batch; one room is spread over 22.
- **Coverage, from the batches.** Each replicate places each of the 7,844 items exactly once.
- **Gate 1, per item.** An item's two replicates sit in different batches, on different readers.
- **Gate 2.** The room-batch graph over the corpus items is one component.

**The gold positions.** Each gold item is seeded 18 or 19 times, more often than a batch has positions, so no rule can keep every reader of a gold item on a different position. Each copy instead takes a position at which its gold item has been seeded least often so far, which spreads each gold item over the positions.

**The duplicate.** One item a batch, from its own corpus items, presented twice. The two copies sit at least a third of the batch apart, or as far apart as a small batch allows.

**The rooms on a packet.** A batch's `rooms` are the sibling blocks its packet carries: the rooms of its corpus items, and the rooms of its gold copies, so that a gold copy looks like any other item.

**The order of batches.** A seeded shuffle of the 1,210 batch ids (`out/_analysis/b3_dispatch_order.json`), in two groups: the first 100 batches, then the other 1,110. The gold check of stage B3 section 3.2 runs between them.

**The cost.** 1,210 readers, each reading the index and the families it opens (about 28,000 input tokens, as at B2's gold round), about 34 million input tokens. The item text over the whole fleet is about 11 million more. Output runs about 1,800 tokens a position for 17,653 positions, about 32 million, and more for the second pass. By B2's gold round's prices the fleet costs about 40 to 55 USD.

### The rebuild in B2's packet shape

- **Packets** (`out/_analysis/b3_packets_fleet2.py`, in `out/_packets-B3/`). `index.md` and `G01.md` to `G21.md` come from `scheme_final.jsonl`, with no exemplars and every page under 50 KB. There are 1,210 self-contained packets, one per batch. Each carries a title naming the batch and its replicate, the brief with its own item count, the sibling block of every room in the batch's `rooms`, the items in position order and the end line.
- **Sizes.** At most 15 items and 178,758 bytes of item text a packet.
- **MANIFEST.json.** It gives each packet its items, bytes, `item_bytes`, sha256, count key and excludes, and `codes_by_item`, with no group, part or parts. It lists 17,653 lines due.
- **Fleet ids only.** nyjets t11's coder note serves c0104 as its fleet id. The tank names "t34" and "t90" in a warthunder participant's words stand in B0075 and B0819; `fleet.py`'s guard now reads id positions only (QB3-002).
- **`RETURN-B3.md`.** It no longer speaks of parts. The second pass comes after the last first line and before the end marker. J's two rulings stand word for word.
- **`run_manifest.json`.** A B3 entry of this shape supersedes the first (11 entries).

### The close-check, B3a

`validate.py B3` reported:

```
stage B3:
  batches 1210, R 2, rooms 705, items 7844, graph one component
  leg: build (0 dispatch folders with DONE)


0 errors (0 distinct shapes), 0 warnings
```

The leg closes with `done.sh B3 --cut packets-out`. J runs the dispatch in two groups, the first 100 batches and then the other 1,110, with the gold check of section 3.2 between them.

## Leg B3a-p2: the gold check after group 1

J dispatched group 1 (the first 100 batches of `b3_dispatch_order.json`) at 15:17Z. It ended at 15:32Z: 100 valid returns, 0 exhausted, 4 replies reissued (3 cited a concept outside the item, 1 line not JSON). The record is `out/_fleet_raw/B3/PARTIAL-2026-10-12T153202Z.json`. No DONE exists, since group 2 has not gone out. This leg is a continuation of the build leg (the PI, 15:51Z): it runs the gold check and closes at `--cut packets-out`.

**The stop rule, declared before any gold figure is computed.** The build leg declared no number for "a fall beyond the stability floor". I fix it here.
- **The comparison.** Each gold copy that group 1 returned is scored against my placement in `gold_items.jsonl` (Jaccard), against the rechecked placement, and on primary match. The B2 figure for the same copy is the mean over B2's nine frozen-scheme readings of that item (the gold round, stab-1 and stab-2: the same reader model, the same scheme). The fall is the B2 mean minus the B3 mean over the same copies, so both sides weigh the items alike.
- **The floor.** `stability-B2.md` gives 0.807: readers differ on about 0.193 of a placement whatever the brief's wording. A fall in fidelity or in primary match larger than 0.193 is beyond the floor. Group 2 then does not go out as built, and J is asked before any batch or packet changes.
- **Reported beside the rule, deciding nothing:** a bootstrap 95% interval for the fall, resampling batches; the figures per batch and per reader; the themes each reader missed; and the items whose own fall is beyond the floor.
- **How lines are read.** One valid reply per packet (its `meta.json` says `valid`). Each line is keyed on its batch and position, and the item is the one `batches-B3.jsonl` puts at that position. The typed fleet theme id is checked against that item through `fleet_ids.jsonl`, as a label. A gold copy is the position in a batch whose item is in that batch's `gold_items`. The allocator never seeds a gold copy into a batch that already holds the item, so the key is unambiguous.

**What group 1 returned** (`out/_analysis/b3_gold_group1.py`; per copy in `b3_gold_group1.tsv`, figures in `b3_gold_group1.json`).
- **Returns.** 100 packets, one valid reply each, 1,470 pass-1 lines. Every packet's pass-1 positions run 1 to n. Every typed fleet theme id names the item its position holds. No line reads `label-only`.
- **Gold.** All 72 gold copies seeded in group 1 came back: 34 of the 40 gold items, one copy in each of 72 batches (31 in replicate 1, 41 in replicate 2). No reissued packet held a gold copy.

The next table compares group 1's gold copies with B2's nine frozen-scheme readings of the same items, weighted copy by copy. The fall is B2 minus B3, and the interval resamples batches.

| figure | B3 group 1 | B2, same copies | fall | 95% interval of the fall |
|---|---|---|---|---|
| fidelity against `gold_items.jsonl` | 0.637 | 0.625 | -0.011 | -0.065 to +0.045 |
| fidelity against the rechecked placements | 0.657 | 0.646 | -0.011 | -0.065 to +0.045 |
| primary match | 0.833 | 0.812 | -0.022 | -0.071 to +0.028 |

**Decision: group 2 goes out as built.** Group 1 scored slightly above B2 on gold, not below it. The upper end of every interval (+0.045 at most) lies far inside the floor of 0.193. No batch or packet changes, and no question goes to J.

**Per copy.** 31 of the 72 copies match my set exactly, and 11 score 0. No set is empty. The misses follow the pattern B2 found. Readers drop my second placement, most often T3-063 (9 copies), T3-004 (5) and T3-039 (4). They add T3-033 on 4 copies.

**Items whose own fall exceeds the floor.** These are one to four copies each, read as cases and not as a figure:
- ukraine t07, one copy, in B1150. The reader placed T3-073, while my placement is T3-009. B2's readers took T3-009 on 8 of 9 readings. T3-009/T3-073 is one of the three pairs that split B2's readers more than once.
- shitredditsays t09, two copies (B0261, B0975). Both readers placed T3-182 against my T3-063. B2's readers matched T3-063 on only 2 of 9 readings.
- cloud9 t12, one copy, in B0850. The reader placed T3-117 against my T3-002. B2's readers matched T3-002 on only 2 of 9 readings.
- nuclearthrone t06 and roosterteeth t03. These are partial losses.

**What the figure licenses.** The readers share an architecture with me and with each other. So the figure bounds whether the written instrument decides the same way at fleet scale as in the pilot, not whether it is right.

**Left to the check leg.** `fidelity-B3.md` (per batch and per reader over both groups), the screen of section 3.1, the position curve and the register. This leg writes none of them. The copy-level table above is their input for group 1.

**The close-check, B3a-p2.** `validate.py B3` reads the leg as a build leg with no DONE, so the PARTIAL record needs no question to J. It reported:

```
stage B3:
  batches 1210, R 2, rooms 705, items 7844, graph one component
  leg: build (0 dispatch folders with DONE)

0 errors (0 distinct shapes), 0 warnings
```

The leg closes with `done.sh B3 --cut packets-out`. Group 2 (1,110 batches) is J's to send.

## Leg B3b: the check

**What the dispatch left** (the PI, 20:02Z). `out/_fleet_raw/B3/DONE` and four PARTIAL records. Per `DONE`, 1,204 of 1,210 packets were valid on the main run, at 32.78 USD. Every packet now has a valid return except B0192 and B0927, which failed six tries each (`EXHAUSTED.tsv`). Under J's ruling (21:39 Berlin), the handler rebuilt those two in halves with `tools/packets.py` (`out/batches-B3-split.jsonl`, `out/_packets-B3-split/`). All four halves came back valid on the first try. B0019a and B0019b are unused spares, since B0019 passed on retry.

### The split put into the fleet's record

J's ruling 2 for this leg: the record must show the batches as served, never deleting. `out/_analysis/b3_split_merge.py` did this:
- **Batches.** `batches-B3.jsonl` is kept as `batches-B3.superseded-20261012T200341Z.jsonl`. It was rewritten with B0192 and B0927 replaced in place by B0192a/b and B0927a/b, with the B0019 spares left out. The record now holds 1,212 batches and the same 17,653 positions.
- **What the halves keep.** Each pair holds its original's items. The original order is kept, except that the duplicate's second copy moved into half a, so both copies sit in one half. The replicates are kept, and the agents are new (a1213 to a1216, `original_agent` the old one). The gold copies sit in B0192a (mit t01) and B0927b (lego t13).
- **Packets.** B0192.md and B0927.md moved to `out/_analysis/packets-B3_exhausted_superseded/`, and the four halves were copied into `_packets-B3/`. The old `MANIFEST.json` is kept as `out/_analysis/packets-B3_MANIFEST_before_split.json`. The new MANIFEST has 1,212 entries and 17,653 lines due. Each half's sha256 matches its MANIFEST entry and the packet its accepted return was served.

**A fault in the halves (QB3-003).** `tools/packets.py` writes room ids. The four halves were served with room ids in their headings and lines (t01, c0009) and with no `codes_by_item`. So their 30 positions reached readers against J's fleet-id ruling, and `fleet.py` could not check their concepts. A hand check (`out/_analysis/b3_halves_support.py`) found no harm: all 289 concepts these lines cite belong to their own items, and every typed id matches its cell. But `tools/assemble.py` refuses all 30 lines, because "t01" does not resolve in `fleet_ids.jsonl`, and it writes nothing. J's ruling 1 forbids a hand assembly. So QB3-003 asks J for one of three choices:
- (a) the handler lets the tool read room-id returns;
- (b) the halves are rebuilt in fleet ids and sent again;
- (c) the halves are left out as missing replicates.

### The failed replies, read as one set (J's ruling 3)

`out/_analysis/b3_failed_review.py` reads every `*.failed.txt` (the dispatch's reason on the first line, then the reply). It classes every concept each reply cites against the item at the line's cell. Figures are in `b3_failed_review.json`.

**86 failed replies over 55 packets** (1,298 replies in `log.jsonl`). The next table counts them by the dispatch's reason.

| reason | replies |
|---|---|
| a concept outside the item | 71 |
| a line not JSON (cut off mid-line) | 6 |
| a partial return: 5 to 15 lines against 14 or 15 due | 5 |
| `also_present` naming a theme with fewer than three concepts | 4 |

**The concept failures are concepts of a neighbouring item in the same packet.** Of the 71 replies:
- 65 cite only concepts of another item in their own packet;
- 1 (B0927, r77) cites those and also one concept of another room;
- 5 cite an id the fleet table lacks, a made-up id.

The dispatch names only the first bad line, but the failed replies cite 453 off-item concepts in all, and 452 belong to another item of the same packet. The neighbour usually sits close by: 347 of the 453 come from an item one to three positions away.

They sit mostly where a reader names other themes:
- 332 in `also_present`;
- 95 in `support`;
- 26 in the multiplacement records.

So a reader filling `also_present` reaches into the items around it. The handler's count holds: almost all failures cite a neighbour's concepts.

Six packets failed more than twice: B0192 and B0927 (six each), B0019 (five), B0822 (four), B0880 and B1194 (three each). B0192 and B0927 both hold r/MMA's eight items, whose concepts readers carried from one item to the next.

**The accepted replies hold no concepts from neighbouring items.** I screened all 1,212 accepted replies: 17,653 pass-1 lines and 17,653 pass-2 lines.
- **Cited ids.** 120,119 concepts are cited in fleet ids (`support`, `also_present`, the multiplacement records), and every one belongs to its item. The other 289 are the halves' room ids (above).
- **Ids in the readers' reasons.** No check reads the `why` texts. They hold 4,971 concept ids, and all are the item's own.
- **Pass 2.** Pass-2 lines cite no concepts (fields: pass, revises, third_order, changed, why_changed).
- **Assembler check.** The dry run of `tools/assemble.py` found no line whose typed theme id names another cell than its own.

So a neighbouring item's concepts reached no accepted line in any field. The screen cannot see whether a neighbour swayed a reading without being cited.

### Declarations for the check, made before any figure is fitted

- **Lines that count.** Agreement and the population figures read pass 1, corpus copies only. Gold copies and duplicates' second copies are left out, as J ruled that no seeded copy counts as a corpus reading. Gold copies are scored apart in `fidelity-B3.md`. Duplicates are scored apart as within-reader disagreement.
- **Agreement**, as `notes-B2.md` defined it and not redefined. It is the Jaccard of replicate 1's set against replicate 2's set for each item: `["T3-004"]` against `["T3-004","T3-011"]` scores 0.5. Exact-set agreement and primary agreement are reported beside it. Alpha uses the distance 1 − Jaccard, with chance taken over the pooled sets.
- **Per-theme presence.** For each theme, over the items with both replicates, positive agreement is (items where both readers name the theme) ÷ (items where either does). Cohen's kappa on the theme's presence is reported beside it.
- **The position curve.** Each corpus line has three outcomes:
  - agreement: Jaccard with the other replicate's line for the same item;
  - multi: more than one theme;
  - arguable: confidence "arguable".

  Each outcome is regressed on position within the batch, with batch fixed effects (outcomes demeaned within the batch) and standard errors clustered by batch. One reader holds each batch, so batch clusters are reader clusters. The curve is drawn by decile of relative position, (p − 1) ÷ (n − 1).
- **Tolerable change.** At most 0.10 in each outcome across a 15-position batch, that is, over 14 steps. That is about half the 0.193 placement disagreement behind the stability floor. The sensitivity is the change across 14 steps that the fit detects with 80% power at two-sided 5%, which is 2.80 × SE × 14. A slope inside the tolerance and a sensitivity inside it together count as stability. A slope that is not significant counts for nothing.
- **Formation per reader.** Batches hold at most 15 positions, so "first ten against last ten" would overlap. I compare the first five with the last five instead, in batches of ten or more.
- **Variance components.** Room and reader are crossed. For multi, the empty set and the theme count, I fit a linear mixed model with crossed random intercepts for room and batch (reader), using statsmodels MixedLM with variance components.
- **The funnel.** Each reader's rate is plotted against its batch size, with limits at the fleet rate ± 3 binomial standard errors. A reader outside the limits is named.
- **The justifications.** I read at least 30 `why_not_one` texts, drawn by seed 20261015 across distinct readers. I class each as one of four kinds: the material spans two themes; the scheme lacks a theme; the reader is hedging; or it restates that both gates are met, which is a defect.
- **Runs before the real assembly.** While QB3-003 is open, the scripts run on a trial assembly with the halves left out (option (c)), in a scratch folder outside `out/` (`out/_analysis/b3_scratch_c.py`). The figures of record come from the assembly J rules on.

### Where the check stands (QB3-003 and QB3-004 open)

**The meanwhile line of QB3-003 does not work as written.** It said that, without an answer, I would assemble on option (c) in `out/`. But the assembler reads `out/batches-B3.jsonl`, which now holds the halves under J's ruling 2. Leaving them out there would undo that ruling. So `out/` holds no assembly yet: no `assign_raw.jsonl`, no `assign_pass2.jsonl` and no `b3_classes.jsonl`. B1's `multiplacement_log.jsonl` (6,663 lines) still stands, and the real assembly's `--supersede` will rename it.

**The check folder.** `checks/stage_B3.py` reads the last folder named `_packets-B3*`. The handler's `_packets-B3-split/` therefore hid `_packets-B3/`, and the check reported 1,208 batches "without a packet". I moved `_packets-B3-split/` to `out/_analysis/packets-B3-split_handler_merged/`; its four halves used in the fleet were already in `_packets-B3/`.

**QB3-004.** The check refuses 32 accepted returns that carry no prediction line (`fleet.py` accepted them). I asked J to waive them by name or have them sent again.

**Reports from the trial assembly.** `fidelity-B3.md`, `position-B3.md`, `multiplacement_register-B3.md` and `agent_report-B3.md` are rendered by `out/_analysis/b3_check.py` and `b3_reports.py` from `b3_check_scratch_c.json`. Each opens by saying it is a trial. Once J rules, the real assembly runs (`tools/assemble.py B3 --supersede --accept-sub-label --families out/families.jsonl`), then `b3_check.py --from out --tag record --write-defects`, then `b3_reports.py --tag record --write`, which keeps the trial reports under superseded names. `defects.jsonl` and `handback-B3.md` wait for that run.

The trial figures (halves left out, 19 items missing a replicate):
- **Screen.** 17,623 pass-1 lines (15,662 corpus). `read` is "whole" on 17,594 lines and "theme-block" on 29; no line is `label-only`. Every multi line has its records and a non-empty `why_not_one`, so no line is reduced to its primary. No reader text says the scheme did not decide. Positions run 1 to n in every batch. The room-batch graph is one component.
- **Gold.** 753 copies: fidelity 0.645 against 0.631 for B2 on the same copies (fall −0.014, interval −0.030 to +0.003); primary match 0.815 against 0.801. Group 2 alone: 0.645 against 0.632. No gold item has its own fall beyond the 0.193 floor.
- **Agreement**, over 7,825 items: Jaccard 0.786, exact set 0.703, primary 0.838, alpha 0.782. The family that agreed least is G18 (0.552). The theme handled worst is T3-152: positive agreement 0.333 over 42 items.
- **Position.** Agreement moves +0.003 over 14 positions (sensitivity 0.027), and the multi rate +0.018. The arguable rate rises +0.040 (0.017 to 0.063). That is inside the 0.10 tolerance, but it is a diagnostic for `defects.jsonl`.
- **Pass 2.** It changed 0.01% of lines.
- **The duplicate.** Both copies agree on every one of 1,208 duplicates. The readers recognised the repeat: 911 repeat the first copy's `why` word for word. So the duplicate does not measure within-reader instability in this fleet.
- **Multiplacement.** The multi rate is 0.158. 88 readers sit above the funnel limits; they held longer items and called more lines arguable. The commonest pairs are T3-009/T3-043 and T3-005/T3-021, 114 each. All 40 sampled `why_not_one` texts name material that one theme leaves out.
- **Variance components.** The reader share exceeds the room share (multi: reader 0.012, room 0.007, residual 0.114).

### J's answers to QB3-003 and QB3-004 (22:30 Berlin)

**QB3-004: the 32 returns are waived by name.** `out/_analysis/b3_waivers_qb3004.py` found the accepted returns without a prediction line from the returns themselves. They are exactly the 32 named in the question. It wrote one line for each to `return_waivers.jsonl`, in the form J gave: stage B3, the file, check "no_prediction", a reason, and "J, 2026-10-12, QB3-004". The file now holds 52 lines. `validate.py B3` counts them aloud: "returns without a prediction line waived by J by name: 32". My assumption was a waiver by name, and it stands. The item lines are scored as given, `agent_report-B3.md` names the 32, and each still goes into `defects.jsonl` as a reader omission.

**QB3-003: (b), the four halves rebuilt in fleet ids and sent again.** J ruled that the error was the handler's. `out/_analysis/b3_halves_fleet.py` rebuilt them under new batch names, so no folder holds two accepted returns. The next table gives the old and new names.

| room-id half (superseded) | rebuilt in fleet ids | agent | replicate | items | item bytes | gold copy | duplicate |
|---|---|---|---|---|---|---|---|
| B0192a | B0192c | a1217 | 1 | 9 | 75,877 | mit t01 | ucf t12 |
| B0192b | B0192d | a1218 | 1 | 6 | 12,512 | - | - |
| B0927a | B0927c | a1219 | 2 | 9 | 75,912 | - | MMA t02 |
| B0927b | B0927d | a1220 | 2 | 6 | 29,547 | lego t13 | - |

- **Renderer.** The rebuild uses the main build's renderer (`b3_packets_fleet2.py`): the same brief, sibling blocks, item text and checks. Rendered by this script, B0001, B0500 and B1100 match their main-build sha256, so the renderer is the same.
- **Packets.** Each half keeps its items in the same order, its rooms, its gold copy, its duplicate and its replicate. Each has a new agent and a `supersedes` field naming the room-id half. Fleet ids only: no room id of a packet's rooms stands anywhere in it, and no other string shaped like a room id appears. Each MANIFEST entry carries `codes_by_item`, so `fleet.py` checks the concepts.
- **Superseded under new names, nothing deleted:**
  - `batches-B3.jsonl` → `batches-B3.superseded-20261012T203637Z.jsonl`. The new file has 1,212 batches and 17,653 positions.
  - the room-id packets B0192a.md, B0192b.md, B0927a.md and B0927b.md → `out/_analysis/packets-B3_roomid_halves_superseded/`.
  - the MANIFEST before this change → `out/_analysis/packets-B3_MANIFEST_before_fleet_halves.json`.
  - the raw folders `out/_fleet_raw/B3/B0192a`, `B0192b`, `B0927a` and `B0927b` → `out/_analysis/fleet_raw-B3_roomid_halves_superseded/`.
- **Close-check.** `validate.py B3` now reads 1,212 batches, R 2, 705 rooms and 7,844 items, with the graph one component. No packet error remains. The errors left are the assembly, which waits for the four returns.

**What rested on my assumption for QB3-003.** I had assumed (c). Nothing in `out/` was assembled on it, because that would have undone J's ruling 2. The four reports remain marked as trial, and they will be replaced. The trial assembly in `$TMPDIR` is not the record.

**Dispatch.** J sends the four from `out/_packets-B3`. The command, built from the handler's words and the PARTIAL records' `only` field:

```
python3 tools/fleet.py B3 --only B0192c,B0192d,B0927c,B0927d
```

**After the four returned** (J, 20:45Z; B0192c valid on its second try), the check leg ran the steps below. Their results are in the next section.
1. `python3 tools/assemble.py B3 --supersede --accept-sub-label --families out/families.jsonl`;
2. `python3 out/_analysis/b3_check.py --from out --tag record --write-defects`;
3. `python3 out/_analysis/b3_reports.py --tag record --basis "<the record>" --write`;
4. `handback-B3.md`, the head, and `done.sh B3`.

### The check of record

**The assembly** (J's flags):
- **Returns.** 1,212 accepted, none exhausted or missing.
- **`assign_raw.jsonl`.** 17,653 pass-1 lines: 15,688 corpus readings, 755 gold copies and 1,210 duplicate copies.
- **The other outputs.** `assign_pass2.jsonl` holds 17,653 lines, `multiplacement_log.jsonl` 3,171 records and `predicted_confusion-B3.jsonl` 1,180 predictions.
- **`b3_classes.jsonl`.** 7,844 items: class 1 2,566; class 2 1,990; class 3 2,393; class 4 837; class 5 58.
- **Coverage.** 100% in both replicates.
- **Other.** B1's `multiplacement_log.jsonl` is kept by the tool as `multiplacement_log.jsonl.superseded-20261012T205314Z`. 22 lines carry `sub_typed` under J's flag.

**Figures** (`b3_check_record.json`). They match the trial assembly to the third decimal, and coverage is now complete:
- **Gold.** Fidelity 0.645 against B2's 0.631 on the same 755 copies; the fall is −0.014 (−0.031 to +0.003).
- **Agreement.** Jaccard 0.786, exact set 0.703, primary 0.838, alpha 0.782.
- **Position.** The arguable rate rises +0.040 across 14 positions; agreement moves +0.003.
- **Multiplacement.** The multi rate is 0.158, and 88 readers sit above the funnel limits.
- **Worst cases.** The family that agreed least is G18 (0.552). The theme handled worst is T3-152 (0.333 over 42 items).

**Two faults in my scripts, fixed:**
- `b3_check.py` refused to write because `defects.jsonl` exists. That file is the run's ledger and holds 8 lines from A1, so the script now appends stage B3 lines once.
- `b3_failed_review.py` read only the newest superseded batch file, which no longer holds B0192. It now reads every superseded file.

**The failed replies, again.** There are 87 over 56 packets: the earlier 86, plus B0192c's first try, which cited a neighbour's concept. The accepted replies cite 120,413 concepts in fleet ids, all from their own item.

**The justifications.** The sample from the record is not the trial's sample. I read its 40 texts too. All 40 name material that one theme leaves out, and the counts in the register are unchanged.

**`defects.jsonl`.** 55 stage B3 lines were appended after A1's 8, 63 lines in all:
- 32 returns without a prediction line (waived, QB3-004);
- the trend in the arguable rate (a diagnostic);
- 22 readers' record slips (below).

**The close-check (QB3-005).** `validate.py B3` reports 23 errors on 22 lines, read one by one in `out/_analysis/b3_support_defects.py`:
- 10 lines whose multiplacement record shares a concept between `support_primary` and `support_additional`;
- 8 multi lines whose `support` field lists only the primary's concepts;
- 4 single-theme lines from B0192c with no `multi` field.

On every multi line, each added theme has at least one concept of its own. So none is "the same reading twice", and none meets section 3.1's reduction. I asked J to waive the 22 by name (QB3-005). Meanwhile they are kept as given and listed in `defects.jsonl`. No waiver is written without J's word.

**Written:**
- the four reports of record, with the trial versions kept as superseded;
- `handback-B3.md`;
- the head.

**QB3-005, answered (J, 23:09 Berlin): the 22 are waived by name and the placements kept as given.** `out/_analysis/b3_waivers_qb3005.py` finds them with the check's own tests and writes one line for each to `return_waivers.jsonl`, keyed by batch and position as J asked:
- 10 `support_overlap` (the record's batch and position);
- 8 `support_count`;
- 4 `no_multi`.

The file now holds 74 lines. My assumption was a waiver by name, with the placements kept and the 22 listed in `defects.jsonl`. It stands, so no figure, report or defect line changes.

### The close-check, B3b

`validate.py B3` reported:

```
  returns without a prediction line waived by J by name: 32 (return_waivers.jsonl)
  lines waived by J by name (return_waivers.jsonl): no_multi 4, support_count 8, support_overlap 11
0 errors (0 distinct shapes), 0 warnings
```

It counts 11 `support_overlap` against 10 waiver lines because two positions each carry two multiplacement records. The leg closes with `done.sh B3`.
