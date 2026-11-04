# Stage B2. Assignment: the pilot.

**Model:** build and check legs as `arm.json` sets (your platform file lists them); dispatch outside your session, the dispatch sending packets to
the routine readers on the platform's reader route (FLEET.md). **Legs:** per round, build, dispatch,
check; the check leg of round k decides whether round k+1 opens. **This stage freezes the scheme.**
You hand it, with a small set of deliberately hard second-order themes, to fresh readers, and
treat every divergence as a defect in the description rather than in the reader.

**Steps:** `B2a-r1` build round 1 (it ends at `--cut packets-out`), the dispatch, `B2b-r1` check round 1; then `B2a-r2`, `B2b-r2` ... while a round is needed; after the freeze, `B2c` builds the gold round and
the two stability rounds (it ends at `--cut packets-out`), three dispatches, and `B2d` checks them. Each leg is named by its step (STANDING §2).

**Safe stops:** after the packets are written (the build leg), and after each section of the check leg. At a safe stop, check for `.pause` (`ls .pause`); if it is there, log where to pick up, your working hypothesis and the next room or item
(`mem.py log "<hypothesis>; next: <item>" --kind pause`), and close with `done.sh B2 --pause` (STANDING §2).

**Startup packet:** `_head.md`, this file, `FLEET.md`, the last five diary entries,
`validate.py --open B2`. In a check leg the harness adds one line: the readers left their files
in `_fleet_raw/B2/round-k/`.

**Reads allowed:** `scheme.md`, `scheme.jsonl`, `families.jsonl`, `confusions.md`, `notes-B1.md`;
the corpus through `cite.py`; second-order themes through `mem.py theme`, concepts through
`codes --sub`; `_fleet_raw/B2/` in check legs. **Forbidden:** your room notes, the running file
and `findings.jsonl` to any reader; `gold_items.jsonl` to any reader; exemplars to any reader in
this stage.

**Outputs:** `author_items.jsonl`; `gold_items.jsonl`; `RETURN-B2.md`; `pilot_rounds.jsonl`;
`scheme_edits.jsonl`; `exemplar_candidates.jsonl`; `stability-B2.md`; `pilot_report.md`; the
frozen `scheme_final.md` and `scheme_final.jsonl`; `notes-B2.md`; a `run_manifest.json` entry.

## 1. Build leg, round 1: the hard set, the gold set, the declarations

**Place every item yourself first**, into `author_items.jsonl`, each with `confidence`
(`clear|arguable`), which stage B4's transmission rows split on, before any packet exists.
Whether a reader holding only the scheme lands where you would have landed has an answer only if
your answers were written down first; a scheme edited with your own placements in front of you
is edited to justify them. Three sources, mixed and shuffled so a reader cannot tell them apart,
sizes declared in `notes-B2.md` before round 1: the second-order themes you nominated in
`confusions.md` to expose each ranked pair, at least half sibling pairs inside one family, since
that is where a scheme of hundreds divides readers (the pilot scores that prediction); the ten
biggest bags from `notes-B1.md`; a random sample, seeded and recorded. Forty to sixty items.

**The gold set**: a second hard set by the same rule and seed discipline, placed by you, shown to
no pilot reader, written to `gold_items.jsonl` with placements, confidence and reasons, and kept
outside the readers' directory (FLEET.md). It is scored once, after the last round (§5). Stage B3
seeds it unannounced into the live batches at the rate you declare.

**Declared before round 1, in `notes-B2.md`:** the stopping threshold (pairwise agreement on the
hard set at which rounds stop); the agreement definition stages B3 and B4 reuse unchanged
(whether `["T3-004"]` against `["T3-004","T3-011"]` is agreement, disagreement or partial:
agreement on sets by Jaccard where rule 0 allowed more than one placement, alpha computed on it;
and whether chance correction is over themes, over sets, or over presence and absence per
theme); the gold policy (count, seeding rate, and that they are seeded; never the items); the
batch cap stage B3 runs under, set from §4 below after round 1.

**`RETURN-B2.md`**, the one return specification (FLEET.md): the return line below, rule 0 in the
contract's words and not restated (a reader that places a second theme owes rule 0 its line in
`multiplacement_log.jsonl`, here as at stage B3), the end marker, and the line telling the reader
to confirm it reached the marker. `packets.py B2` builds one packet per reader under the 50 KB
ceiling: `scheme.jsonl` as it currently stands, served as stage B3 serves it, the index page
whole and the families opened as the reader needs them; the hard set's items with label,
`theme_note` and concepts; and no exemplars: stage B3 may ship them; this stage measures the
description alone. **From the round after 2026-10-11 (J)** the return line also carries
`also_present`: `{}` unless `item_is_a_bag` is true, and then every theme beyond the one placed,
each with its own concept ids (rule 0 as amended); `support` holds the concepts behind the
primary, and each further theme's concepts are in its `multiplacement_log` record. Rounds sent
before the amendment are scored as they were sent. Oversized items are served in parts to the
same reader (`MANIFEST.json` groups, as stage B3 serves a large room), never dropped for size.

```json
{"sub": "...", "theme_id": "...", "batch": "...", "agent": "...", "replicate": 1, "position": 23,
 "third_order": ["T3-007"], "multi": false,
 "why": {"T3-007": "what about THIS theme put it here rather than its nearest neighbour"},
 "confidence": "clear|arguable", "read": "whole|theme-block", "exemplar_read": null,
 "families_opened": ["G03", "G09"], "t_start": "...", "t": "...", "support": ["c0013"],
 "also_present": {}}
```

Append the round's manifest entry: readers' model, seed, decoding, count. Every later fidelity is
compared against this stage's figure. **Stop here.** Close with `done.sh B2 --cut packets-out`. Your session ends; nothing more of this stage runs on your model until the check leg. The dispatch runs without you, on the platform's reader route. The next launch of stage B2 is the check leg, and its packet tells you one thing: the readers left their files in `_fleet_raw/B2/round-k/`.

## 2. Dispatch leg

Not yours. The dispatch sends each packet to three fresh readers, collects the returns into
`_fleet_raw/B2/round-k/`, validates them against `RETURN-B2.md`, reissues what fails the
schema, and closes. Nothing in it reads your files. A partial return is not a return: its
unwritten items are gaps, not verdicts, and are reissued; when reissues are exhausted the stage
stops and you rebuild the packets (FLEET.md). No reader gets a stronger model for a hard item:
readers are interchangeable or fidelity means nothing. In the check leg copy `fleet.py`'s
counts into `notes-B2.md`: readers, reissues, durations. Counts, not readings.

## 3. Check leg: the three numbers and the edit

You are relaunched. Validate, then score, in this order: **fidelity** against
`author_items.jsonl`, the primary figure; **pairwise agreement** among the three readers,
secondary, since three readers can agree with each other and all diverge from you; **your own
consistency**, by re-placing ten of the hard set blind (after the last round only): open a blind
window first (`mem.py blind on --reason "..."`), read the ten through `mem.py theme` and the
packets' family pages, write your placements, then `mem.py blind off`; the read log is the
evidence that the window held. If you disagree with yourself more than the readers disagree with
you, the fleet is not the problem.
Every item where any two disagree is a finding and the material for the edit. One line per round
in `pilot_rounds.jsonl`:

```json
{"round": 1, "n_items": 52, "agents": 3, "exemplars": false, "fidelity_vs_author": 0.0,
 "agreement_pairwise": 0.0, "alpha": 0.0, "items_with_disagreement": ["..."], "seed": 0}
```

**The edit, every one logged** in `scheme_edits.jsonl` with stage B4's taxonomy, so the pilot and
the run share one set of names: `scheme-ambiguous` (the belonging test or the discriminator does
not decide; fix the sentence); `item-is-a-bag` (the coder's theme holds two practices, so no
single placement is right; not a scheme defect; flag the item and move on); `reader-error` (the
file does decide and the reader missed it; suspect this last: two independent readers making the
same miss is a scheme defect that looks like a reader error); `author-error` (you were wrong and
the readers were right; a pilot that never returns it measures obedience); `genuine-joint` (the
material satisfies two gates and one placement cannot carry it, rule 0's exception on the record;
check that the readers actually differed rather than one recording the exception).

```json
{"round": 1, "theme": "T3-007", "field": "must_not_show", "caused_by": ["sub/theme_id", "..."],
 "was": "...", "now": "...",
 "why": "two of three readers placed a coordination-of-labour item here because the test said nothing about who was named"}
```

An edit with no `caused_by` is not allowed; stage C1 opens `scheme_edits.jsonl` before it
revises anything. Every edit is a `tier_history` line with its move (`relabelled` or `rescoped`,
move `asking questions` or `splitting`). **Never tighten by narrowing until a theme becomes
rare**: it looks like success here and makes that theme's prevalence wrong everywhere after.
Watch every theme's base rate across rounds and report it.

**Every edit owes its rechecks** (J, 2026-10-11). After you change a gate, place again every
placement of yours it could move: the items of `author_items.jsonl` and `gold_items.jsonl` on the
edited theme, or on a theme its old or new sentence names. `mem.py rechecks --owed` lists them
(the edit is `edit:<n>`, its line in `scheme_edits.jsonl`; above thirty a seeded sample of thirty,
and all of them once more than one in ten of the sample moves); `mem.py recheck <sub>:<tNN>
--change edit:<n> --theme ... --codes "T3-a=c1,c2" --reason "..."` records each, with the concepts
behind each theme. `author_items.jsonl` stays as you wrote it: from the next round report
fidelity twice, against it and against the rechecked placements, and say in each moved recheck's
reason whether it is an `author-error` or the edit doing its work. The close refuses an edit
whose rechecks are missing. Then run `mem.py gates` and read every pair an edited theme belongs
to (`mem.py gates T3-a T3-b`), confirming each with `--confirm --reason`: a discriminator that
runs one way, or a `must_not_show` that sends material to a theme with no discriminator against
it, is fixed before the packets are rebuilt, and the freeze refuses a scheme that carries either.

Then decide: another round opens if no stopping condition holds (§5), and its build leg
rebuilds the packets from the edited scheme.

## 4. Two things this stage owes the fleet

**How long a convention takes to form.** Compare each reader's first ten items against its last
ten on the arguable rate and on agreement with the other two; report where the curve flattens.
If either still improves inside a round, formation is still happening and stage B3's cap is too
small; the fix is a warm-up block that does not count, not a bigger batch. **Which items make
good exemplars.** Export the items that divided readers to `exemplar_candidates.jsonl`; stage
B3's exemplar arm draws from them, not from clear cases.

## 5. Stopping, the freeze, stability, the gold score

Rounds stop when one holds: a round produces no scheme edit; pairwise agreement on the hard set
clears the declared threshold; four rounds. After four, a scheme that still divides three readers
is telling you about the tier, not the wording: report it and carry it into B3.

Freeze the scheme as `scheme_final.md` and `scheme_final.jsonl`, the rare tier inside it under
`"tier": "rare"`, `families.jsonl` beside it. Then, in `B2c`, the dispatches on the frozen scheme:
one round of fresh readers on the gold set (`packets.py B2 --round gold --items gold_items.jsonl`);
and the **stability check** (FLEET.md), the gold set served to the same reader arm under two
rewordings of the brief that change no test (`out/brief-stab-1.md` and `out/brief-stab-2.md`,
written by you; `packets.py B2 --round stab-1 --items gold_items.jsonl --brief brief-stab-1.md`,
and the same for 2), whose disagreement with itself is written to `stability-B2.md` and is the floor
every later figure is read against. Report gold fidelity beside the last pilot round's fidelity
(close means clearer, much worse means fitted); pairwise agreement and alpha on the gold set
beside the final round's; per-family agreement, and per theme only where a theme has three or
more items in the set, since at hundreds of themes over sixty items a per-theme figure is one
item wide; your `confusions.md` predictions scored: which pairs confused readers, in what order,
and how the observed rate compared with your estimate.

Gold fidelity is a trend against this stage's frozen figure, not a level: the set was drawn hard,
and the figure is agreement with your own placements. Wherever a figure from this stage appears,
say what it licenses in FLEET.md's words, and which claim you are making: *what you would have
produced at a scale one analyst cannot reach* is supported; *what any competent reader would have
produced* is not.

## 6. `pilot_report.md`

The rounds, with agreement climbing or not; every edit grouped by theme with the disagreement
that caused it; the gold number beside the last pilot number and what the gap means; the
`author-error` verdicts, listed; the themes that never stabilised, named, with what stage B4
should expect from them; the prediction scorecard; the stability figure; what it cost: readers,
items, tokens (`tools/tokens.py --dispatched` gives the tokens each packet cost, as the gateway
counted them).

## Moments to log

Each declaration; each round opened and closed with its three numbers; each edit; the freeze;
the stability result.

## Final message

Rounds run; fidelity at round 1 and at the end; the gold figure with agreement and alpha
beside it; the stability figure; `author-error` count; your blind re-placement score; edits by
field; which predicted confusions were real; themes that did not stabilise; any theme whose
base rate fell while tightened; the one sentence in the scheme you are least confident a
stranger reads as you meant. A return value.

## Close

`done.sh B2` at every leg (its close-check is `validate.py B2`; paste the report into
`notes-B2.md`); `--cut packets-out` at every build leg; where a check leg's edit recuts a theme, the move
logged with `mem.py log --kind move` and snapped with `python3 tools/snap.py B2 move-<move>-<n>`; `handback-B2.md`; the head; the closing diary line.
