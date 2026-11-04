# Stage B4. Assignment: adjudication, and transmission after revision.

**Model:** build and check legs as `arm.json` sets (your platform file lists them); the blind sample's dispatch outside your session
(FLEET.md). **Legs:** adjudication (one or more, bounded by packets of contested items), then
build, dispatch and check for the blind sample.

**Steps:** `B4a-01`, `B4a-02` ... one per adjudication packet; `B4b` the blind sample's build (it ends at `--cut packets-out`), the dispatch, `B4c` its check, the placements final (`assign_final.jsonl`), the handback and the interview. Each leg is named by its step (STANDING §2).

**Safe stops:** after each adjudication packet is ruled and logged, and after each section of the transmission check. At a safe stop, check for `.pause` (`ls .pause`); if it is there, log where to pick up, your working hypothesis and the next room or item
(`mem.py log "<hypothesis>; next: <item>" --kind pause`), and close with `done.sh B4 --pause` (STANDING §2).

**Startup packet:** `_head.md`, this file, `FLEET.md`, the last five diary entries,
`validate.py --open B4`; in the check leg, the harness's one line: the readers left their files
in `_fleet_raw/B4/`.

**Reads allowed:** `assign_raw.jsonl`, `b3_classes.jsonl` (the contested inventory, §1), `multiplacement_log.jsonl` (every `why_not_one`),
`fidelity-B3.md`, `position-B3.md`, `notes-B3.md` (the disagreement inventory, the gloss-only
placements), stage B3's gold keys (the tags in `batches-B3.jsonl`), `author_items.jsonl`, `gold_items.jsonl`, `scheme_final.*`
with `families.jsonl`, `confusions.md` and `pilot_report.md` (stage B2's predictions),
`stability-B2.md`, `notes-B2.md` (the agreement definition); the contested items through
`mem.py theme` and `codes --sub`, quotes through `cite.py`; `_fleet_raw/B4/` in the check leg.
**Forbidden:** the canvas as an undeclared ground (rule 7); your notes as a ground for a ruling; a reader's identity
while you rule; any edit to the scheme; to a blind reader, everything §10 withholds.

**Outputs:** `disagreements.jsonl`; `assign_final.jsonl`; `transmission-B4.md`;
`coder_conflicts.jsonl`; `adjudication_report.md`; `RETURN-B4.md`; `reassign.jsonl`;
`transmission-after-revision-B4.md`; `notes-B4.md`; a manifest entry.

## 1. What comes here

**Only the contested items, and the placements made from a gloss.** Three placements decide which
items are contested (J, 2026-10-12): the two readers' pass-1 lines, replicates 1 and 2, and your
B1 grouping, the item's third-order themes among the members of `scheme/scheme_current.jsonl`
(sha256 `8b67360b8d0dfefc`), joined by sub and second-order label through
`package/store/themes.jsonl`, a set with no order. A reader's list is its `third_order` in order.
Gold copies and the duplicate's second copy are left out. `tools/assemble.py B3` writes each item's
class into `b3_classes.jsonl`; that file is the contested inventory, built by the tool, not by hand.

The placement stands, with no adjudication:

1. The two readers return the same list, order included, and its set equals the B1 grouping. The
   readers' list stands, `multi` or not.
2. The two readers return the same list, and its set is smaller than the B1 grouping and inside it.
   The B1 grouping stands: the readers' list first, then B1's other themes in ascending id order.
   Its line in `assign_final.jsonl` carries `"source": "b1_grouping_kept"`, so that stage C1 can
   tell it from placements made under the frozen scheme.

The item comes here:

3. The readers differ, including the same themes in another order (J: "just add the case to
   adjudication"); and an item with one replicate missing, which cannot be agreed
   (`missing_replicate` in `b3_classes.jsonl`).
4. The readers agree on a set that is not inside the B1 grouping.
5. The item has no B1 grouping (58 at B1).

One exception stands whatever the class: a placement into a family neither reader opened
(`families_opened` without the chosen family; `unopened_family` in `b3_classes.jsonl`) is read by
you, since two readers can agree from a gloss; where you move one, it is logged as a ruling like
any other. An item two readers holding the same written scheme placed differently is a boundary
the scheme did not decide, with the alternatives attached.

## 2. The gold placements come out first

**Drop the seeded gold placements before you adjudicate anything**, using stage B3's keys. A
seeded placement is measurement, not corpus evidence; left in, it enters `assign_final.jsonl` and
every denominator below, and breaks rule 4 quietly.

**What is dropped is the gold placement, not the second-order theme.** A theme carrying gold
placements is still a theme of the analysed set and still owes `assign_final.jsonl` its line,
taken from the live replicates. Drop by `(item, agent, replicate)` on the gold-keyed rows, never
by key. After the drop the line count still reconciles to `counts.py`'s
`assignment_items_expected` over the analysed set; if it does not, you dropped themes.

Fidelity on the gold placements is stage B3's figure, in `fidelity-B3.md`. Read it, do not
recompute it, and say in `notes-B4.md` how many placements the drop removed.

## 3. Transmission, decomposed

**Compute it before anything here touches the file.** Drop the gold placements from the rates as
§2 drops them from `assign_final.jsonl`, but keep them for the decomposition, which is what your
own answers are for. Your answer exists for every gold item and every item stage B2 piloted, in
`gold_items.jsonl` and `author_items.jsonl`; FLEET.md's four rows are computed there:

| the readers | you | what it is |
|---|---|---|
| agree with each other and with you | | the scheme decides |
| **split** | **were confident** | **fails to transmit**: a wording defect; the sentence stage C1 must repair |
| **split** | **were also unsure** | **the instrument does not decide this item**: a finding, kept |
| agree with each other, **diverge from you** | | **teaches something unintended**: read every one |

The third row is never revised away. **The fourth row's items never reach the adjudication**,
because both readers agreed: they are in `assign_raw.jsonl` and nowhere else, and `author-error`
below catches only the items that split. Split the fourth row both ways, you were wrong or the
scheme taught something you did not intend, and say in `notes-B4.md` which way each went. Outside
the gold and pilot sets your own answer does not exist, so the split rate there cannot be
decomposed: say so, and do not extrapolate from the gold set, which was drawn to be hard.

`transmission-B4.md` gives the rows with their items, by family. Name it in `handback-B4.md`;
stage C1 reads it among its sources.

## 4. The conflicts pass

**`coder_conflicts.jsonl` is produced here, once, and nowhere else**: two coders describing the
same practice in incompatible terms, seen only by reading across communities; the second-order
themes whose `theme_note` and concepts pull apart under the scheme. The pass runs over
`theme_note` alone, with no concepts beneath it. Run it before you rule: a conflict between coders
explains some of the disagreements between readers, and you want to know which first. Stages C1
and C2 read this file.

## 5. Declared before the first item, in `notes-B4.md`

The ruling policy. At `R = 2` every split is one reading against another and there is no
majority to lean on:

- how many items you expect to rule on, from stage B3's inventory, and how many packets that is
  at five hundred per leg (v42; one hundred before): a large inventory means more legs, never a rule applied in bulk. A
  scheme of hundreds splits more than a scheme of forty, mostly between siblings in one family,
  where the discriminator is the sentence to quote; gloss-only placements are ruled first; and
  where many splits fall on one sibling pair, the boundary is ruled once, in one paragraph quoting
  the discriminator, applied to every item on the pair and logged as one ruling with its item
  list, because a boundary ruled item by item is ruled inconsistently;
- what a reader's `confidence` and `why` count for, and whether a `clear` reading against an
  `arguable` one is a prior or nothing;
- whether an adjudicated placement may name a third-order theme **neither reader chose**: it may,
  logged loudly, because it means both readers missed something the file did say;
- what you do when the honest answer is that the scheme does not decide. That must be available
  as an outcome, recorded as `unresolved` and carried, not resolved by preference.

## 6. Blindness, and its limits

**You see the item, the scheme, and the two placements, not who made them.** Agent id, batch,
replicate, position and timestamps are stripped from the packet before you look (no v38 tool yet
for the stripping; done by hand and logged); the funnel is a property of the fleet, not evidence
about this item. **Both readings are shown**, with their `why` and `confidence`: two readings,
neither a prior over the other. You wrote the scheme, and no procedure removes your pull toward
your own reading; record `named_neither` every time your placement is one no reader chose.

## 7. Adjudication, by packet

One packet of at most five hundred contested items per leg (v42), by family, gloss-only placements
first. For each item you rule: the taxonomy from stage B2, the placement that stands, and one
clause of why from the item's material through `mem.py theme` and `codes`, the deciding sentence
quoted through `cite.py`. A ruling never cites a room note. The classification matters more than
the placement:

- **`scheme-ambiguous`**: the belonging test or the discriminator does not decide. Name the field
  and quote the sentence. These aggregate into stage C1's revision list.
- **`item-is-a-bag`**: the coder's second-order theme holds two practices, so no single placement
  is right. Not a scheme defect.
- **`reader-error`**: the file does decide and a reader missed it. **Suspect this last**, and
  never assign it when two independent readers made the same miss: that is a scheme defect that
  looks like reader error.
- **`author-error`**: you were wrong and the readers were right. It exists wherever your own
  answer is on record, the gold items and anything you placed at stage B2; **an adjudication
  that never returns one is measuring obedience.** Carry the count to `adjudication_report.md`.
- **`genuine-joint`**: the material satisfies two gates and one placement cannot carry it, rule
  0's exception on the record. A split here is readers applying rule 0 differently; the count
  measures how well the rule travelled, a fact about the instructions, not the readers.

Where the two readers agree and you would not have, you may overrule with the same line and the
taxonomy value `author-disagrees`, counted separately; you do not re-read the agreed items in
search of these.

```json
{"sub": "...", "theme_id": "...", "readers": [["T3-007"], ["T3-011"]], "ruling": ["T3-007"],
 "unresolved": false, "taxonomy": "scheme-ambiguous", "field": "must_not_show",
 "theme": "T3-007", "quote": "the sentence that failed to decide",
 "boundary_ruling": "T3-007|T3-011 or null",
 "named_neither": false, "confidence": "clear|arguable", "why": "...", "leg": "...",
 "support_by_theme": {"T3-007": ["c0013"]}, "also_present": {}}
```

Every ruling names the concepts behind each theme it places (`support_by_theme`, rule 0 as
amended, J 2026-10-11); a bag keeps the themes it does not place under `also_present`, each with
its concepts. `assign_final.jsonl` carries both from the ruling or from the readers' lines.

`ruling` is empty and `unresolved` true where the scheme does not decide; a boundary ruled once
carries the pair in `boundary_ruling` on every item it decided, and the ruling itself is one
paragraph in `adjudication_report.md` with its item list. `assign_final.jsonl` is every item of
the analysed set with its standing placement.

## 8. Three things not to do

**Do not let a `clear` reading decide silently.** A reader's confidence may weigh on the
placement; the disagreement still gets its row, its taxonomy, and its quoted sentence.

**Do not revise the scheme here.** Stage C1 does that with the whole inventory in front of it;
fixing a sentence mid-adjudication adjudicates the items before and after it against different
files. Log the defect and leave the file alone.

**Do not let the `unresolved` count reach zero by effort.** An adjudication that resolves
everything has resolved some things by preference.

## 9. `adjudication_report.md`

- **Items adjudicated**, against stage B3's disagreement inventory.
- **The taxonomy split**, the most important result: mostly `item-is-a-bag` is a good scheme
  meeting messy material; mostly `scheme-ambiguous` is a scheme that did not survive being handed
  over.
- **Third-order themes by ambiguity**, ranked. Stage C1 opens with this list.
- **Fields by ambiguity**: `must_show`, `must_not_show`, `decide_when_both` or the
  discriminators. Four numbers.
- **The `named_neither` rate**, and your reading of it.
- **The `unresolved` count**, named, with the `author-error` and `author-disagrees` counts.
- **The boundary rulings**, one paragraph each with its item list.
- **Agreement before and after**, with the note that the figure after is not a reliability figure;
  it is agreement following an adjudication you performed.
- **Whether stage B2's predictions held**, now that every theme in the analysed set has answered.

## 10. The blind sample: build leg

**This measures transmission after revision** (FLEET.md), never called reliability: whether
the line you settled can be reached again by readers who were not here. Fleet agreement is
already computed, corpus-wide, at stage B3, before anyone decided; this adds fresh readers against
the record every later stage rests on. It is small by design: the fleet already read everything
twice.

Declared before you draw, in `notes-B4.md`:

- **The sample**: five hundred items, two hundred and fifty drawn uniformly at random from the
  analysed set and two hundred and fifty from the adjudicated items, by a recorded seed (J,
  2026-10-12: "250 each for adjudication and random"). The two strata are reported separately
  and never pooled: the first says whether the scheme decides the ordinary item, the second
  whether your rulings can be reached by a stranger. Within the uniform stratum, the items kept
  under §1's rule 2 are reported as a row of their own: they were neither adjudicated nor placed
  under the frozen scheme.
- **Two fresh readers per item**, as `arm.json` sets this stage's readers, with no memory of the
  run, one dispatch. Each reading is compared with the settled line on its own: one thousand
  comparisons, a rate over readings; the readers' agreement with each other is reported beside it.
- **The agreement definition**, stage B2's and B3's from `notes-B2.md`, unchanged, or the
  figures cannot be set beside each other: sets by Jaccard where rule 0 allowed more than one
  placement, alpha computed on it; whether `["T3-004"]` against `["T3-004","T3-011"]` is
  agreement, disagreement or partial; whether chance correction is over themes, over sets, or
  over presence/absence per theme.
- **Exemplars**: none unless stage B3 served them, and then the same arm, declared on both sides
  of the comparison (FLEET.md). This measures whether the written scheme decides.

**`RETURN-B4.md`** as at B3: the return line, rule 0 in the contract's words, the end marker and
the confirm line. `packets.py B4` builds the packets under the 50 KB ceiling: the scheme as frozen
(the index page, the family pages as the reader opens them), the sampled second-order themes with
their `theme_note` and concepts, and no ruling in sight. **Nothing else.** Not
`assign_final.jsonl`, not `disagreements.jsonl`, not `gold_items.jsonl`, not a hint that these
items were decided before, and never your room notes, the head or `findings.jsonl`. If a reader
needs your notes to decide, the scheme did not decide, and that is the finding. Append the
manifest entry on stage A1's schema (readers' model, seed, decoding, reader count) before the
first packet leaves. **Stop here.** Close with `done.sh B4 --cut packets-out`. Your session ends; nothing more of this stage runs on your model until the check leg. The dispatch runs without you, on the platform's reader route. The next launch of stage B4 is the check leg, and its packet tells you one thing: the readers left their files in `_fleet_raw/B4/`.

## 11. Dispatch leg

Not yours. The dispatch sends each packet to two fresh readers on
the routine reader model, never the same reader for both readings of an item, collects the returns into
`_fleet_raw/B4/`, validates them against `RETURN-B4.md`, reissues what fails the schema, and
closes. Nothing in it reads your files.

## 12. Check leg: the comparison and the figures

You are relaunched. Assemble the returns keyed on packet heading and cell number. **The
comparison, per reading, the fresh placement against the settled one**, into `reassign.jsonl`:

- **agrees**: the scheme decides, and the same way twice;
- **disagrees, and the item was a disagreement here**: expected. Compare the two rates; a
  boundary that split the fleet and then split a fresh reader shows consistency, not a new
  problem;
- **disagrees, and the item was unanimous in the fleet**: either the fleet shared an assumption
  the scheme does not license, or the adjudication moved something it should not have. Name these
  individually, and give each a paragraph;
- **disagrees, and the settled placement was `unresolved`**: no information. Exclude these from
  the denominator rather than counting them as a failure, and say how many.

**`transmission-after-revision-B4.md`**: the headline figures side by side, fleet agreement from
stage B3 and fresh-against-settled agreement per stratum, with alpha per stratum on its two
hundred and fifty items and the stability floor from `stability-B2.md` beside them, the uniform
stratum's rule-2 items in a row of their own, the definition stated once above them; per family,
not per theme: two hundred and fifty items a stratum over nearly two hundred themes leave most
themes with one or two items, or none, in the sample. The per-theme figure stage C1 needs is stage B3's agreement, over every item and
every theme; point to it, do not recompute it. Then the unanimous-but-disagreed items, listed;
and the gap between the uniform stratum's figure and stage B2's gold figure: the pilot measured
the scheme on deliberately hard items, and where the gold number is not the lower of the two, the
hard set was not hard. Wherever a figure from this section appears, say what it licenses, in
FLEET.md's words: readers share an architecture with you, so the figure bounds whether the
written instrument decides, never whether it is right.

## Moments to log

The gold drop with its count; the transmission rows; the conflicts pass; each declaration of §5;
each packet ruled with its taxonomy counts; each boundary ruled once, with its item list; each
overrule; the blind sample's draw with its seed, its build, its dispatch and its result; every
unanimous item a fresh reader placed elsewhere.

## Final message

The claim (which family the scheme decides worst and why), the item that best supports it, the
item that most threatens it, and the condition that separates them; then the counts: contested
items inherited and adjudicated; rulings by taxonomy; `author-error` and `author-disagrees`; the
three third-order themes with the most `scheme-ambiguous` rows; the field that failed most; the
`named_neither` and `unresolved` counts; boundaries ruled once, and the items they decided;
whether the pilot's predictions held on the full corpus; the four transmission rows; transmission
after revision per stratum with its definition, alpha against the stability floor, the three
worst families, and the unanimous items a fresh reader placed elsewhere; the single boundary you
most expect stage C1 to have to move; the licences exercised.

## Close

`done.sh B4` at every leg; paste `validate.py B4`'s report into `notes-B4.md`; `handback-B4.md`;
the head; the closing diary line.

**Interview point.** `B4c` writes `out/interview/B4c.md` (under 800 words: what you did, what you found, what surprised you, what you doubt, and the three questions you would most like to be asked) and closes with `done.sh B4 --cut interview`: the placements final after the fleet placed every theme and the adjudication ruled: where the readers and you disagreed, what the pilot and the fleet taught you. The principal investigator may talk with you here, in a fork of this leg, run in a copy of your folder as it stood at the close (not read-only; nothing done there reaches the run); the run goes on from the cut either way. `done.sh` files the brief under the leg, the stage, the step and the minute, and refuses the cut without the brief (and, at a stage's end, without the handback).
