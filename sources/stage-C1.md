# Stage C1. Model: structuring. Scheme v2, and the fourth-order themes.

**Model:** as `arm.json` sets for this stage (your platform file lists the model and effort). **Legs:** one per pass of revision, closed at the pass's end or earlier when you
choose. Every move (a split or merge of a theme, a fourth-order theme cut) is logged with `mem.py
log --kind move`, the Grodal, Anteby and Holm move named, and snapped with `python3
tools/snap.py C1 move-<move>-<n>` when it is made. **Fleet:** none; every
re-placement here is yours, and no reader runs.

**Steps:** `C1a-01`, `C1a-02` ... one per pass; the last pass ends with the handback and the interview. Each leg is named by its step (STANDING §2).

**Safe stops:** after each logged move, and after each pass. At a safe stop, check for `.pause` (`ls .pause`); if it is there, log where to pick up, your working hypothesis and the next room or item
(`mem.py log "<hypothesis>; next: <item>" --kind pause`), and close with `done.sh C1 --pause` (STANDING §2).

**Startup packet:** `_head.md`, this file, the last five diary entries, the frozen
`scheme_final.jsonl` paged (`scheme/scheme_current.jsonl` is stage B1's working grouping and
stops at the freeze), `validate.py --open C1`.

**Reads allowed:** `scheme_edits.jsonl` first, then `transmission-B4.md`, `disagreements.jsonl`,
`multiplacement_log.jsonl` with the pair table in `multiplacement_register-B3.md`,
`coder_conflicts.jsonl`, `assign_final.jsonl`, `reassign.jsonl`,
`transmission-after-revision-B4.md`, `notes-B3.md`, `confusions.md`, the frozen `scheme_final.*`; `counts.py`
for the analysed set; the views `_views/rooms-x-third.tsv`; items through the verbs (`mem.py
theme`, `where`, `codes --third`, `codes --grep`; quotes through `cite.py`). **Forbidden:**
dimensions (stage C2); the canvas as an undeclared ground (rule 7); re-emitting stage B4's figure; any reader.

**Outputs:** `scheme_v2.md`, `scheme_v2.jsonl`; `assignments_final.jsonl` with
`assignments_final.count.txt`; `assign_revisions_only.jsonl`; `fourth/fourth.jsonl` with
`fourth.md`; `form_pass-C1.md`; `tier_history.jsonl` appended for every change to the
third-order and fourth-order tiers; `notes-C1.md`; `handback-C1.md`.

## 1. Read the record before you touch a theme

`scheme_edits.jsonl` whole, then the pair table, then transmission's second row (fails to
transmit) and fourth row (teaches something unintended). These are the sources of every
revision; a revision with no source line is not allowed.

**The pair table first** (rule 0): every recurring `(primary, additional)` pair in stage B3's
table, computed from `multiplacement_log.jsonl`, is a boundary the scheme has not drawn, and a
theme that appears as `additional` far more often than as `primary` is a modifier to consider
folding.

**Then four sources say where the scheme is weak**, and a theme appearing in three of them is
not one to defend: `disagreements.jsonl`; `reassign.jsonl` (a fresh reader disagreed with the
adjudicated line); `coder_conflicts.jsonl`; and transmission's fourth row, where the readers
agreed with each other and not with you, the rarest and the most serious. Read `scheme_edits.jsonl`
beside them: a boundary that moved at B2 and split the readers again is one the wording cannot
draw, a candidate for the rare tier or a merge rather than for a third sentence.

## 2. Transmission's rows, and which one is yours to revise away

`transmission-B4.md` decomposes the splits against your own answers on the gold and pilot
items. *Split, and you were confident*: the scheme failed to transmit; **revise**. *Split, and
you were also unsure*: the tier does not decide this item; **leave it**, and an amendment that
lowers that count with no wording defect you can quote is fitting. *Agreed with each other,
diverged from you*: read every one. Either you were wrong, in which case record it and **do not
amend the scheme toward your own answer**, or the scheme taught something you did not intend and
the wording is yours to fix. Say in `notes-C1.md` which way each went.

**`transmission-after-revision-B4.md` is stage B4's file. Read it; do not rewrite or re-emit
it.** Its figures are per family; the per-theme figure you rank themes by is stage B3's
agreement, by family and by theme in its disagreement inventory (`notes-B3.md`), computed over
every item, and a theme the readers split on everywhere is weak whatever the blind sample says of
its family. If the revision changes the scheme enough that stage B4's figure no longer describes
it, say so in `notes-C1.md` and say which figure the write-up should use. Wherever you cite
stage B4's figures, say what each licenses in FLEET.md §2's words: they bound whether the
written descriptions decide, not whether they are right. Never call any of them reliability.

## 3. The revision rate

**Re-decide two hundred placements yourself**, drawn by seed from `assign_final.jsonl`, now that
the whole corpus has been through the scheme and you have read every disagreement, and report how
many you would move and where. That number is **the revision rate**: your agreement with the
settled line at the end of the assignment arc, a figure about the tier as it stands. It is not
saturation, since a census has no next case to add; it is not transmission after revision, which
is stage B4's; and it is not FLEET.md's stability, which is a reader arm's agreement with itself.
For something closer to saturation, record when each *kind* of unplaceable material first
appeared and say whether new kinds stopped appearing.

## 4. Recut the third-order tier, under rule 11

Read every disagreement first as a diagnosis, not as a verdict on the description. It may be an
underspecified boundary (readers who sent the same kind of material to different places), a
reader's error, bundled material (one item that carries two kinds), or a defensible second
reading. §2 says which to revise and which to leave.

The rule changes first and the items follow from it. Declare the stopping criterion before
the first recut: what would make you prefer a later cut to this one. Rule 7 stays shut, so no
recut can be fitted to an outcome.

**You may change the scheme itself**: add a theme, split one, merge two, retire one, or move one
to the **rare tier** (`"tier": "rare"` on its line; the event `moved_to_rare`), the home stage
B1's floor defines for a kind the corpus plainly carries below that floor. Use stage B1's floor,
two rooms unlike each other; do not invent one here. Merging is arithmetic (rule 10); splitting
is a re-read of every second-order theme the split theme held, by you, from the items. Declare
each change with its reason, append the event to `tier_history.jsonl` with its move, and
re-place every second-order theme it touches by applying the amended rule, **yourself, never a
reader**. Log every moved item: which second-order theme, out of which third-order theme, into
which, and the clause of the amended gate that decides it. **A theme that arrives here declares
its gate here**, in the form stage B1 uses, before any count appears anywhere (rule 5).

**A gate amended without a split or a merge owes rechecks too** (J, 2026-10-11). Record it with
`mem.py gate T3-NNN --field F --now "..." --reason "..."` (`out/gate_history.jsonl`), write the
sentence into `scheme_v2.jsonl`, then recheck the placements it could move: every one up to
thirty, else the seeded sample of thirty the line names, and every one once more than one in ten
of the sample moves. Each recheck is `mem.py recheck <sub>:<tNN> --change gate:<n> --theme ...
--codes ... --reason ...`; each moved one is then moved with `mem.py reassign`, which takes
`--codes`, the concepts behind each theme. Run `mem.py gates` on every theme you amend and confirm
each pair you read.

`assignments_final.jsonl` is every second-order theme with its placement under scheme v2, and it
is what stage C2 reads; nothing after C1 reads `assign_final.jsonl`.

## 5. Joints and lumps: the pair test

For **every pair of third-order themes carried together by ten or more second-order themes**,
report the pair's **arguable rate**, the share of the second-order themes carrying both that were
returned `arguable`, **with its confidence distribution**, against the corpus-wide arguable rate.

A **joint** is an act the material genuinely presents twice over, which any scheme cuts in two.
A **lump** is your scheme cutting where the material has no seam. In a rate the two look
identical. Confidence is a review cue, not a warrant for either. Reopen the act and its coded context: does the same act demonstrably perform both functions, or does the category bundle distinct acts? Cite the evidence and a plausible contrary reading. For every pair materially above the corpus arguable rate, report joint, lump or unresolved and the reason; then split, merge or retain it under rule 10's arithmetic. High confidence can be a shared error, and uncertainty can concern a real joint.

## 6. The empties, and the arguables

Read every `third_order: []` line and every `confidence: "arguable"` line.

**The empties:** group them into kinds and say, for each kind, whether the scheme is too narrow
or the material too varied. If more than one in five of the corpus is empty, that is a finding
about the scheme and goes at the top of `notes-C1.md`.

**The arguables:** check them against **stage B1's written prediction** in `confusions.md` of
which pairs would be confused, and say whether the prediction held.

## 7. The form pass

Forms (turn position, register, length, timing, who answers whom) are scattered under the
coders' topic groupings (contract §5), so **go over the first-order concepts directly, on
participants' quoted words, not through second-order themes**. Count before you read:
`mem.py codes --grep <re>` runs over the whole store with no limit on the count, and its first
line gives the concepts matched and the rooms they fall in, under one log record; `cite.py
--grep` grounds what you then quote. Say in `form_pass-C1.md` which patterns you counted, and run
the pass **three times over**, saying what you swept for each time:

1. **Form**: turn shape, position in a sequence, length, timing. What is the cheapest act in
   this corpus, and how would you know?
2. **Register**: any vocabulary that cuts across subjects. A register that appears widely and is
   owned by no theme is a tier, not a residue.
3. **What is not said**: terms used without gloss, roles invoked without introduction, questions
   nobody answered. What a room does not bother to explain is what it takes for granted.

**Write `form_pass-C1.md`**: what you searched, at what limits, what you found, and how many
communities and how many lines each finding covers. **Then name what the pass could not reach**:
a search over quoted words finds vocabulary, while a register or a stance is a property of a
whole utterance and invisible to string matching, and no route through second-order themes
reaches an act whose themes name what it was *about* rather than what it *was*. Write both in
`notes-C1.md`, which stage E1 and the write-up's *what the study cannot say* inherit.

**What you find is a tier of its own, with ids `FP-01` on, living in `form_pass-C1.md` prose
and nowhere else**: no schema, no line in any JSONL. (The prefix `FP-` keeps them apart from the findings in `findings.jsonl`,
`F-001`, from stage D4's branches, `F01`, and from stage C5's propositions, `N01`.) Write each with its id, its one-line statement, and the communities and lines it
covers, in a block a later stage can quote whole. **Stage C2 reads them from that file, by id**,
and they enter the structure and the model on the same terms as any third-order theme, marked
as ones whose unit is the turn rather than the topic.

**A form-pass finding does not enter the arithmetic**, and `form_pass-C1.md` says so: no line in
`assignments_final.jsonl`, no three counts, no share in the chunk-share tree at stage D4, no
branch contrast at stage D5. It travels on exemplars under rule 5's carve-out, and the write-up
says in your own sentence that it was never counted and never clustered. **Do not invent a gate
to make one look promotable**; rule 5 forbids it.

## 8. Cut the fourth-order themes

This is where the model begins. To bundle third-order themes into a fourth-order theme you must
already theorize: what story lies behind the bundle, and how holding these kinds together helps
explain what the rooms did. Write that story for every bundle, however provisional; it is the
structure the loop (C2) starts from, and the loop is free to change any of it. A bundle you
cannot tell a story for is not yet a fourth-order theme.

Named groups of third-order themes, constructs from the moment they are cut (contract §2). They
partition the third-order tier: a third-order theme sits in one fourth-order theme, and a
second-order theme reaches two only through its own placements (rule 0). Each is declared
borrowed (with `"recalled": true` until stage C3 checks it against a text), adapted or coined,
with a source named for a borrowed or adapted one (a coined one is this corpus's), with what
would disconfirm it in another setting, with the grounded phrase kept as a gloss, and with prose that says what holds its members
together without listing them. A fourth-order theme with no prose is a heading. No number is
set. A third-order theme no fourth-order theme picks up is reported as a list, never gathered
into a catch-all. Each cut is a `tier_history` line (`tier: "fourth"`, move `merging` or
`relating`), a `move` line in the diary and a snap, made when you cut it.

```json
{"id": "T4-003", "name": "...", "gloss": "...", "declared": "borrowed|adapted|coined",
 "source": "...", "disconfirm": "...", "members": ["T3-007", "T3-011"], "prose": "..."}
```

## 9. `scheme_v2` and `assignments_final.jsonl`

**`scheme_v2.jsonl` mirrors `scheme_final.jsonl` field for field.** After this stage the frozen
instrument is `scheme_v2`: it is the scheme every later stage keys its theme ids to, and what
the validator resolves them against. **`scheme_v2.md` is the whole scheme, not a diff**: every
theme, including the untouched ones, with every field, plus the complete gate block including
gates declared here, and each change declared with what changed, why, and which placements it
moves.

**`assignments_final.jsonl` is every placement line, not only the ones you changed.** An overlay
under the name every later stage lists as *the* assignment input is indistinguishable from a
complete file, and a stage that reads it literally works on whatever fraction of the corpus it
covers and never finds out. Unchanged lines carried through verbatim, changed lines superseding,
same schema as stage B3, one line per `(sub, theme_id)`. Nothing is deleted. Keep the
overlay as `assign_revisions_only.jsonl`; stage E1 reports it. Once `assignments_final.jsonl` is
written, re-place a second-order theme with `mem.py reassign <sub>:<tNN> --theme T3-NNN --codes "c1,c2" --reason
"..."`, which rewrites its line and keeps the overlay in step.

**The line count goes in `assignments_final.count.txt`, not at the top of the JSONL**, which
stage C2 and the scripts parse line by line. It must equal the number of distinct `(sub,
theme_id)` keys in `assign_final.jsonl`, one line per second-order theme in the analysed set,
**not** the number of lines the readers returned, which is that number times `R`. Take the
expected value from `counts.py`'s `assignment_items_expected`.

## 10. `_views/` after the recut

`gen_views.py` regenerates the case-ordered matrix (rooms by third-order themes) and the
data-structure file at every close; read them before the next leg to see what the recut did to
the rooms, and log what you saw.

## Moments to log

Each source line read; the stopping criterion, before the first recut; each gate amended with
the items it moved; each theme added, split, merged, retired or moved to rare; the revision
rate; each pair called joint or lump; the empties by kind; each sweep of the form pass; each
fourth-order theme cut; the views read after each close.

## Final message

The claim (what the revision changed about what these rooms did), the room that best supports
it, the room that most threatens it, the condition that separates them; then: the recurring
pairs and what each became; the revision rate; stage B4's transmission after revision as you
read it, with its definition, not recomputed; which pairs came out above the corpus arguable
rate, and which of those were joints and which lumps; how many empties, of how many kinds;
whether stage B1's prediction held; recuts by kind, items moved, themes retired or moved to
rare; the line count of `assignments_final.jsonl` against what `counts.py` expects; what the
three sweeps found; the form-pass ids you minted, with the statement that stage C2 takes them
from `form_pass-C1.md`, the only place they exist; fourth-order themes cut and the third-order
themes left unpicked; the licences exercised.

## Close

`done.sh C1` at the end of every pass, or earlier when you choose, each move logged and snapped
as it was made; paste the close-check's report into `notes-C1.md`; `handback-C1.md`; the
head; the closing diary line.

**Interview point.** The last `C1a` leg writes `out/interview/<its leg id>.md` (for example `C1a-04.md`) (under 800 words: what you did, what you found, what surprised you, what you doubt, and the three questions you would most like to be asked) and closes with `done.sh C1 --cut interview`: scheme v2 and the fourth-order themes cut: the first abstraction above the rooms, and what you gave up to reach it. The principal investigator may talk with you here, in a fork of this leg, run in a copy of your folder as it stood at the close (not read-only; nothing done there reaches the run); the run goes on from the cut either way. `done.sh` files the brief under the leg, the stage, the step and the minute, and refuses the cut without the brief (and, at a stage's end, without the handback).
