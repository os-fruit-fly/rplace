# Stage B3. Assignment: the fleet.

**Model:** build and check legs as `arm.json` sets (your platform file lists them); dispatch outside your session, the dispatch sending packets to
the routine readers on the platform's reader route (FLEET.md). **Legs:** build, dispatch, check; the
dispatch may be split into groups of batches of declared size, each with its own check. You
design the allocation, write the packets and the brief, and report what the fleet did as a
population; you place nothing, run no reader and call no model. The placements are stage B4's.

**Steps:** `B3a` build (it ends at `--cut packets-out`), the dispatch, `B3b` check; a check that spans more than one leg continues as `B3b-p2`, `B3b-p3` ..., as any leg after a pause does. Each leg is named by its step (STANDING §2).

**Safe stops:** after the packets are written (the build leg), and after each report of the check leg. At a safe stop, check for `.pause` (`ls .pause`); if it is there, log where to pick up, your working hypothesis and the next room or item
(`mem.py log "<hypothesis>; next: <item>" --kind pause`), and close with `done.sh B3 --pause` (STANDING §2).

**Startup packet:** `_head.md`, this file, `FLEET.md`, the last five diary entries,
`validate.py --open B3`. In a check leg the harness adds one line: the readers left their files
in `_fleet_raw/B3/`.

**Reads allowed:** the frozen `scheme_final.jsonl` with `families.jsonl`;
`exemplar_candidates.jsonl`; `pilot_report.md`; `stability-B2.md`; `notes-B2.md` (seeding rate,
batch cap, agreement definition); `notes-B1.md` (bag ranking); `gold_items.jsonl` in the build
leg, to seed; `counts.py`; the corpus through `cite.py`; the store through `mem.py` (`theme`,
`codes --sub`); `_fleet_raw/B3/` in check legs. **Forbidden:** the canvas to any reader (rule
7); your notes, the running file and `findings.jsonl` to any reader; `gold_items.jsonl` anywhere
a reader can reach; any reader's output to another reader.

**Outputs:** `RETURN-B3.md`; `batches-B3.jsonl` and the packets (`packets.py B3`);
`assign_raw.jsonl`; `assign_pass2.jsonl`; `multiplacement_log.jsonl`;
`multiplacement_register-B3.md`; `fidelity-B3.md`; `position-B3.md`; `agent_report-B3.md`;
`notes-B3.md`; an appended entry in `run_manifest.json`.

## 1. Build leg

**The unit is the second-order theme, every one of the analysed set, at `R = 2`.**

### 1.1 What each reader gets, and what it must not get

**Gets:** rule 0, stated first, in the contract's wording and not restated in other words;
`scheme_final.jsonl` with `decide_when_both` served, as an index page (every family, every
third-order theme's id, name and gloss) read whole, and one file per family opened as the reader
needs it, so that a scheme of hundreds costs each reader the index and the families its items
reach, not the whole; its batch of second-order themes, each with the coder's label, the
`theme_note`, and every first-order concept beneath it with the participants' words; **the
sibling block** for each room in the batch; and the exemplars only if the arm is served (§1.3).

**The sibling block** introduces each room once, at the top of the batch, by the **labels** of
all its second-order themes, so a reader can see what a theme is not: labels only, not their
`theme_note`s, not the chronology, not the coder's account. In the batch header, never on the
item.

**Must not get:** any other reader's output; the corpus beyond its own items; the canvas in any
form (`rooms.jsonl`'s canvas fields, `canvas/artworks.jsonl`); your notes, the running file or
`findings.jsonl`; or any indication of how many items it holds relative to the whole.

**Every reader runs in a fresh context.** `packets.py B3` (`scheme` and `batch` verbs) builds the
index page, the family pages and each batch file from `batches-B3.jsonl` and the store, every
file under FLEET.md's 50 KB ceiling, which it asserts (a batch above it is split into parts for
one reader, §1.2), each batch ending with the end marker and the confirmation line.

### 1.2 The allocation: whole rooms, crossed with readers

**Every room of the analysed set is in the fleet, with every one of its second-order themes. Each
reader gets whole rooms, no room is ever split, and each room's replicates land on different
readers.** Randomise which rooms a reader holds, never which items. The allocator packs whole
rooms greedily to the item cap and computes the fleet from its own packing, never from
`ceil(items / cap)`; `readers = batches × R`.

**A room larger than the cap is a batch by itself, and a batch over the 50 KB ceiling is served
in parts to one reader** (J, 2026-09-25). At the 2026-09-25 snapshot, some rooms rendered above
50 KB on their own; `packets.py B3` reports the count for this frame. `packets.py B3` splits such a batch into parts
(`B017-p1`, `B017-p2`, ...), each under the ceiling, each carrying the room's full sibling block,
positions running on across parts; `fleet.py` serves the parts to the same reader as turns of one
conversation, so one reader reads the whole room, and validates each part's reply against its
own item count. The prediction line comes in part 1 only and the second pass after the last part.
The returns are keyed by batch as for any other (`_fleet_raw/B3/B017/<reader>.jsonl`). Report the
split batches apart in the position curve (§3): a reader on its second or third part is deeper
into its context than a reader of a whole batch.

**Before the packets are built, assert from the batches** that the union of rooms across them is
the analysed set and the union of items is `counts.py`'s `assignment_items_expected`. A coverage
claim computed from the draw rather than from the batches cannot fail.

**Two gates run before any packet is written.**

1. **No room may meet the same reader twice.** Reject and redraw on collision.
2. **The room-reader graph must be one connected component.** Build the bipartite graph of rooms
   against batches, walk it, and refuse to build if it is in pieces; redraw on failure.

Declare in `notes-B3.md`, before any packet exists:

- **the seed**, from which the allocation is reproducible;
- **the item cap per batch**, from `notes-B2.md` (v37's default was fifty, about 35k tokens of
  context before the scheme), set so that every batch file stays under 50 KB, with its reason,
  costed with the index page and the families a batch's rooms are likely to open; and the whole
  fleet's cost from that, for the token record (no stage carries a budget, contract §4);
- **the warm-up block**, if stage B2 found a convention still forming inside a round: ten
  declared items with the answers given, then the cap's items that count; otherwise in reserve;
- **the replication factor** `R`, which is 2: two readers make a disagreement visible, and stage
  B4 rules on it; a third reader costs half the fleet again to turn a disagreement into a vote,
  and rule 13 says a vote is not a warrant. Say so, and say what a higher `R` would have bought;
- **the gold seeding rate**, restated from `notes-B2.md`, and the gold policy of §1.6;
- **the batch count and reader count** the allocator computed;
- **the exemplar arm**, declared once, served to every reader or to none;
- **the order of batches**, seeded and recorded, and the groups the dispatch is split into;
- **the reissue policy** `fleet.py` runs (§2);
- **the bag flags**: the top ten from `notes-B1.md`, marked in the batch, instruction unchanged:
  *place from the concepts, not from the coder's grouping*.

**Append this stage's entry to `run_manifest.json` at the close of the build leg**, on stage
A1's schema: the readers' model (the cheap arm, as FLEET.md declares it), the seed, the decoding
settings, and `n_agents` at `R`.

`batches-B3.jsonl`, one line per batch; gold tags, duplicate tags and reissues go on it too:

```json
{"batch": "B017", "agent": "a017", "n_items": 48, "replicate": 2,
 "rooms": ["...", "..."], "exemplar_items": ["sub/theme_id", "..."],
 "gold_items": ["sub/theme_id"], "duplicate_items": ["sub/theme_id"],
 "warmup_items": [], "reissue": 0, "original_agent": null,
 "seed": 20260827, "items": ["sub/theme_id", "..."]}
```

### 1.3 The exemplar arm

**Declared once, and served to every reader or to none**, from `exemplar_candidates.jsonl`
through `packets.py B3 --exemplars` onto the family pages. A reader told it may consult a sheet
may never open it, so the return line carries `exemplar_read: true|false` per item when the arm
is served, `null` when not, and every figure of this stage is reported conditional on it; without
the field, report no exemplar result at all. Stage B2 measured the description alone, so a
comparison with its figures is across arms, and FLEET.md requires the serving arm declared on
both sides. Stage B4's blind sample serves exemplars only if you did.

### 1.4 The shuffle, the duplicate, and the warm-up in reserve

**Items are interleaved across rooms in random order inside every batch.** Grouped by room,
position tracks room and the position curve (§3.3) is confounded with what it exists to be free
of.

**Put one duplicate item in each batch**: the same item twice, in different positions, presented
as two items. Report disagreement as within-reader instability beside the between-reader disagreement rate.
It can reflect stochastic variation, ambiguous gates, position, context or recall; it does not
identify any one cause. Preserve positions and intervening material for inspection.

**If a single reader is far out of line, the fix is not a bigger batch** but the warm-up block
that does not count. Hold it in reserve until the measurement says it is needed. A drift across
the whole fleet is a cap set too high, and the fix for that is a smaller batch.

### 1.5 `RETURN-B3.md`: what a reader returns

One return specification, frozen with this file; the packet builder emits it verbatim, the brief
cites it, and `fleet.py`'s schema check is generated from it (FLEET.md). In this order:
rule 0 in the contract's words (a second placement owes its `why_not_one` and a
`multiplacement_log.jsonl` line; three at most; beyond three place one, record `item-is-a-bag`,
and name the others under `also_present` with their concepts); the prediction line; the return line; the multiplacement record; the second
pass; the end marker and the confirmation line.

**Before the first placement**, each reader writes which pair of third-order themes it expects to
find hardest to tell apart, one line, first in its return:

```json
{"agent": "a017", "predicted_confusion": ["T3-007", "T3-011"], "why": "one sentence"}
```

The check leg compiles these into `agent_report-B3.md` and onto the batch record, and scores
them against what actually divided the readers, as the pilot scores `confusions.md`.

**The line a reader returns**, the stage B2 line with `replicate` 1 or 2, `exemplar_read` and
`bag`:

```json
{"sub": "...", "theme_id": "...", "batch": "B017", "agent": "a017", "replicate": 2,
 "position": 23,
 "third_order": ["T3-007"], "multi": false,
 "why": {"T3-007": "what about THIS theme put it here rather than its nearest neighbour"},
 "confidence": "clear|arguable",
 "read": "whole|theme-block",
 "exemplar_read": null,
 "families_opened": ["G03", "G09"],
 "bag": false,
 "t_start": "...", "t": "...",
 "support": ["c0013"],
 "also_present": {}}
```

`third_order` carries one id in the ordinary case, and the first id is always the primary.
`batch` and `position` are the packet heading and the cell number the return is keyed on.
`families_opened` names the families the reader read the full tests of before placing this item;
a placement into a family the reader never opened is a placement from the gloss alone, and stage
B4 reads those first. `multi: true` requires a matching record in `multiplacement_log.jsonl`.
Both timestamps: per-reader elapsed time is what a cost estimate is built from. **`read:
"label-only"` is not a permitted value**; the check refuses it, and you screen the returned
lines for it in the check leg as well, because a reader that read only the label placed the
coder's grouping, not the material.

**The multiplacement record.** Every placement beyond the first is written by the reader, on the
same line it places, one record per extra theme; the check leg assembles them into
`multiplacement_log.jsonl`:

```json
{"sub": "...", "theme_id": "...", "key": "sub/theme_id", "batch": "B017", "agent": "a017",
 "replicate": 2, "position": 23,
 "primary": "T3-007", "additional": "T3-011",
 "why_not_one": "what this material carries that T3-007's gate does not reach",
 "why_this_one": "what in the material satisfies T3-011's gate, and its distinct supporting concept",
 "support_primary": ["c0013"], "support_additional": ["c0027"],
 "dispensable": "which of the two you would drop if forced to one, and what would be lost"}
```

Four rules on it, in the brief:

- **Distinct support.** The additional theme needs its own supporting concept id; the same
  concept twice is the same reading twice, and is refused.
- **`why_not_one` is about the material, not the scheme.** *Both gates are satisfied* is not a
  justification, since `decide_when_both` settles that case; it must name what the single
  placement would fail to carry.
- **`dispensable` is compulsory and may not be `null`.**
- **No line carries more than three themes.** A third requires its own record and its own
  `why_not_one` against **both** the others. Beyond three, place one and record the item as
  `item-is-a-bag` for stage B4, `"bag": true` on the line, and name every other theme the
  material satisfies under `also_present`, `{"T3-011": ["c0027"]}`, each with its own concepts
  (J, 2026-10-11): the cap drops no theme from the record. `also_present` is `{}` on every other
  line.

**Two passes, and the second never overwrites the first.** Every reader makes a second pass over
its own batch after finishing it, and both are kept. The revision rate between them is
within-batch formation measured a second way. Pass 2 goes to `assign_pass2.jsonl` and never back
into `assign_raw.jsonl`; every pass-2 line names the pass-1 line it revises. A revision is a
record, not a correction. **Stage B4 adjudicates pass 1**: pass 2's answer depends on what else
was in the batch, so a different seed would give a different corpus.

### 1.6 The gold items, seeded and unannounced

**Seed `gold_items.jsonl` into the live batches at the rate declared in `notes-B2.md`**,
shuffled so no reader can tell a gold item from a corpus item and no two readers holding the same
gold item hold it in the same position.

- **Tagged in `batches-B3.jsonl`, never in the payload.** Gold items are corpus items too, so the
  seeded copy is told apart from the live reading by `(item, agent, replicate)`, never by key:
  the scorer, not the reader, can tell them. Report the seeded and the corpus readings of those
  items separately, and say in `notes-B3.md`, before seeding, that this is the policy.
- **Excluded from every denominator downstream.** Stage B4 drops them before it writes
  `assign_final.jsonl`.
- **The answer key stays outside the readers' directory** (FLEET.md): neither `_fleet_raw/B3/`
  nor the packets directory ever holds `gold_items.jsonl` or anything derived from it.

**Stop here.** Close with `done.sh B3 --cut packets-out`. Your session ends; nothing more of this stage runs on your model until the check leg. The dispatch runs without you, on the platform's reader route. The next launch of stage B3 is the check leg, and its packet tells you one thing: the readers left their files in `_fleet_raw/B3/`.

## 2. Dispatch leg

Not yours. The dispatch sends each batch packet to a fresh reader on
the routine reader model, never the same reader for both replicates, collects the returns into
`_fleet_raw/B3/<batch>/<reader>.jsonl`, validates each against `RETURN-B3.md`'s schema, and reissues under the
policy you declared: a batch that comes back missing, truncated, malformed, or short of its item
count (the returned line count is checked against it before acceptance) is not a disagreement
and is not absorbed; the whole batch goes to a fresh reader id holding none of its rooms, up to
twice, recorded as `reissue: 1` or `2` with the original reader id. A partial return is never a
return: four of twelve items written is four placements and eight gaps, different data. When
reissues are exhausted on a batch, the dispatch stops and reports, and the build leg rebuilds
those packets (FLEET.md). Nothing in the dispatch reads your files; its log leaves, per reader,
reissues, elapsed time, and anything outside the return format.

## 3. Check leg

You are relaunched. Assemble `assign_raw.jsonl`, `assign_pass2.jsonl` and
`multiplacement_log.jsonl` from the returns, keyed on packet heading and cell number, with the
typed theme id as a label (FLEET.md); copy `fleet.py`'s counts and durations into
`notes-B3.md`, counts and durations, not readings. Then, in this order.

### 3.1 Accept and screen

- **Re-run the connectivity check** against what the fleet returned, after every reissue.
- **If a batch could not be filled after two reissues and its rebuilt packets came back short
  again**, name its rooms in `notes-B3.md`, mark them `coverage_short` in `batches-B3.jsonl`, and
  exclude them from the variance decomposition. Do not fill the gap with a duplicate of a reader
  that already read those rooms.
- **Screen by hand** for `read: "label-only"`, and for a `multi` placement whose log record is
  missing or whose `why_not_one` is empty: each is a defect in `defects.jsonl`, and the line is
  reduced to its primary before stage B4 opens.
- A reader that reports the scheme did not decide is reporting a material defect; its words go
  in `defects.jsonl` verbatim.

### 3.2 Gold fidelity, live

Into `fidelity-B3.md`, per batch and per reader, never only in aggregate: how many of each
reader's gold items matched your placement, and which themes it missed on. Stage B4 reads that
file and does not recompute it. Read the movement against stage B2's frozen figure on the same
items, not the level: the set was drawn hard, and the figure is agreement with your own
placements. **A fall beyond the stability floor of `stability-B2.md` stops the dispatch and
reopens the build leg.** Payload assembly, model, batch size or sibling block changed; say what
in `notes-B3.md` before the packets are rebuilt. Where the dispatch is split into groups, this
check runs after each group and decides whether the next is sent.

### 3.3 The position curve

Into `position-B3.md`, the drift check, pooled across the whole fleet. Regress agreement, the
multi-assignment rate and the arguable rate on position within batch, with batch fixed effects.
Report a curve by decile of position with a fitted slope and an interval as the test, and the
multi-assignment rate as a distribution over readers beside it. A position effect is a diagnostic of changing responses, not an identified cause. Inspect
context saturation, warm-up, attention, prior answers and convention formation before choosing a remedy.
Use intervals respecting batch and reader dependence. Declare a tolerable change across a batch
before fitting; report its interval and design-based power or simulation sensitivity. A nonsignificant
slope alone does not establish stability. Log detected trends in `defects.jsonl` as unresolved
diagnostics, with the evidence needed to distinguish explanations. Beside the curve: the pass-1 to
pass-2 revision rate, and formation per reader, first ten items against last ten, on arguable
rate and on agreement with the readers holding the same rooms; the diagnostic, where the pooled
curve is the test.

### 3.4 The multiplacement register

`multiplacement_register-B3.md` is rule 0's log read as a measurement:

- **The multiplacement rate**, overall and per reader, on a funnel against batch size.
- **The pair table.** Every `(primary, additional)` pair with its count, ordered; the top twenty
  listed for stage C1. A pair that recurs across many readers and rooms is a boundary the scheme
  has not drawn; stage C1 reads this table first.
- **Whether the recurring pairs are the pairs the readers predicted** (§1.5).
- **The justifications, read.** At least thirty `why_not_one` texts across readers, each classed
  *material genuinely spans two themes*, *scheme lacks a theme for this*, *reader hedging*, or
  *restatement of both gates being satisfied*, which is a defect. Report the counts.
- **Per-theme exception load.** A theme that appears as `additional` far more often than as
  `primary` is a candidate for review. Inspect designation rules and supporting concepts before
  deciding whether it is a modifier, an overlapping construct or a missing boundary.
- **The empties**: the rate, and the characterisation rule 0 requires of each.

### 3.5 The fleet as a population

- **Per-reader dispersion, with the room component separated.** Room and reader are crossed, so
  fit the simplest model that estimates both variance components and report both. Put the
  per-reader figures (multi-assignment rate, empty rate, mean themes per line) on a funnel against
  batch size; a reader outside it is reading the scheme differently, and stage B4 needs its items
  named. Do not rank readers.
- **Agreement.** Pairwise across replicates, corpus-wide, per family and per theme, exact-set and
  Jaccard, with Krippendorff's alpha on the overlap (FLEET.md), under the definition declared in
  `notes-B2.md` and not redefined: whether `["T3-004"]` against `["T3-004","T3-011"]` is
  agreement, disagreement or partial. Report per-theme presence/absence agreement whatever else
  you report, and the duplicate rate beside it.
- **The exemplar figures**, conditional on `exemplar_read`, the serving arm declared on both
  sides of any comparison with stage B2.
- **`families_opened` as a distribution**: families opened per placement, its median, and the
  share of placements into a family the reader never opened. A low median prompts review of prior access, retrieval logs and gloss-only decisions.
  It does not alone establish a defective index. Stage B4 reads placements with no recorded
  relevant family access first and records demonstrated defects with their evidence.
- **The disagreement inventory**: how many items the two readers placed alike, how many they
  split, and of the splits how many differ on the primary and how many only on an additional
  theme, by family and by theme, with the `multi` and `item-is-a-bag` counts. Stage B4's
  workload.
- **Coverage**, computed from the batches: every second-order theme of the analysed set has two
  returns, or is named in the unreturned list with why.
- **The multiplacement register**, as its own file, referenced here.

Wherever a figure from this stage appears, say what it licenses, in FLEET.md's words: readers
share an architecture with you or with each other, so a figure bounds whether the written
instrument decides, never whether it is right.

### 3.6 The close-check

This stage's record is what every later stage rests on, and the v35 analyst found its missing
`read` field at the end of the run, on every row. `validate.py B3`, run by `done.sh B3`, checks
each of these and refuses by name what it cannot. Read the report rather than trusting it, and
screen the last two by hand as well, since a check reads a field and not a reading:

- Every `third_order` id exists in `scheme_final.jsonl`.
- Every `support` id resolves in `package/store/codes.jsonl`.
- Every multi-assigned line names at least one distinct concept per theme and has its records in
  `multiplacement_log.jsonl`.
- Line count equals items × `R`, where items is `assignment_items_expected`, with any reader
  failure named rather than absorbed.
- No reader appears in two replicates of the same item.
- The room-reader graph is one connected component, re-checked against what the fleet returned.
- `assign_pass2.jsonl` exists and has not been merged into `assign_raw.jsonl`.
- Every line carries `position`, and positions within a batch are a permutation of 1..n.
- Every line carries `read`, `families_opened` and both timestamps.
- No line carries `read: "label-only"`.

## Moments to log

Each declaration; the coverage assertion and each gate passed or redrawn; each batch built,
dispatched and checked with its gold fidelity; each reissue and each `coverage_short`; each
defect written; any stop.

## Final message

Seed, cap and `R`, and the batch and reader counts the allocator computed; confirmation from
the batches that every room and second-order theme of the analysed set is in the fleet; readers
run and failed; redraws the connectivity gate forced, and whether the graph was connected at
the end; total lines and replicates; gold seeded and returned, and gold fidelity by batch
against stage B2's figure and the stability floor; corpus-wide, per-family and per-theme
agreement, exact-set and Jaccard, with alpha and its definition; the exemplar figures if the
arm was served; the position curve by decile with its slope, interval and computed power; the
pass-1 to pass-2 revision rate; the multiplacement rate and its spread across readers; the
three most frequent `(primary, additional)` pairs and what each says about the scheme; how many
placements you reduced to their primary; how many readers fell outside the funnel and what they
had in common; how many readers' predicted confusions matched yours; the disagreement inventory
stage B4 inherits, with the family that disagreed most; the unreturned items; and the single
theme the fleet handled worst. A return value.

## Close

`done.sh B3` at every leg; `handback-B3.md`; the head; the closing diary line.
