# Stage D3. The return: adjudication by element.

**Model:** as `arm.json` sets for this stage (your platform file lists the model and effort). **Legs:** one per element group (a fourth-order theme's elements,
or one element with many lines), packets of at most one hundred lines; then one leg for the
unattached `propose` lines; then one for the verdicts and the uncomposed rooms; then the
re-check handoff; then the close. A leg may close earlier when you choose. Every model revision
is a move, logged with `mem.py log --kind move` (the Grodal, Anteby and Holm move named) and
snapped with `python3 tools/snap.py D3 move-<move>-<n>` when it is made. **Fleet:** the labelers again,
for the re-check rooms only, through the handler; the verdict fleet again for rooms whose
verdicts rested on a rewritten element. Both run outside your session.

**Steps:** `D3a-01`, `D3a-02` ... one per element group, then as further `D3a` legs the unattached `propose` lines and the verdicts with the uncomposed rooms; `D3b` the re-check, if you build one; `D3c` the freeze and the re-read, the handback and the interview. Each leg is named by its step (STANDING §2).

**Safe stops:** after each element group is ruled and logged. At a safe stop, check for `.pause` (`ls .pause`); if it is there, log where to pick up, your working hypothesis and the next room or item
(`mem.py log "<hypothesis>; next: <item>" --kind pause`), and close with `done.sh D3 --pause` (STANDING §2).

**Startup packet, every leg:** `_head.md`, this file, `SCHEMA-adaptations.md`, the last five
diary entries, `validate.py --open D3`; the `rooms-x-elements` view's summary for the group.

**Reads allowed:** `mem.py adaptations --element <id>`; the room's model and coder documents
by query when a line needs them (`mem.py room`, `forest`, `theme`, `codes`, `cite.py`);
`verdicts-D.jsonl`; `findings.jsonl` by `--touching`; `prior.md`; the last
`story_rooms-pN.jsonl`. **Forbidden:** the raw ledger as a list; loosening an element until a
room fits (rule 12); promoting a case-only element to the global model without a shared warrant; `EXPECTATIONS.jsonl` (stage E1 scores it); the
canvas as an undeclared ground (rule 7).

**Outputs:** `adjudications.jsonl`; `model/` revisions with `history.jsonl` lines;
`tier_history.jsonl` for any tier move; when the third-order tier is recut, `scheme_v2.jsonl` and `assignments_final.jsonl` rewritten
(`mem.py mint`, then `mem.py reassign`, as stage C2 says); `handoff-D/recheck/`, `adaptations-recheck.jsonl`;
`uncomposed-D.md`; `findings.jsonl` lines; `verdicts-D.jsonl` rulings; `exception-report-D.md`;
`notes-D3.md`; the model frozen as one version, hashed; `handback-D3.md`.

## 1. By element, never as a list

Read `_views/rooms-x-elements.tsv` first: where the mass is. Then one element group per leg:
`mem.py adaptations --element P07` returns every accepted-or-pending line touching P07, sorted
by op. For each line: accept, modify (with `revised`, which passes the same
portability check as the labeler's line; the original stays in the ledger), reject, or
particular, with one reason from the line's evidence and the room's material, into
`adjudications.jsonl` through `mem.py adjudicate` (SCHEMA §6), with `pair` where a second
room's accepted line meets the same correction and `kind` where you reclassify. A portable line
with no shared warrant is a locally supported `particular` if its evidence suffices, otherwise `pending` and unresolved. A line naming the room itself
in `condition` is a particular; one naming another room in `relation` is not. Quotes go
through `cite.py`.

## 2. Corrections met twice

Two accepted corrections with the same target and the same lifted node at the third or fourth
level are the trigger: you re-examine the element in the same leg, and your written reason is
the warrant (rule 12), never a count. A revision is a `history.jsonl` line with the
move (one of Grodal, Anteby and Holm's eight), the adaptation ids that caused it, a `move`
line in the diary and a snap, made when you revise; substantive alignment warrants a cluster branch or a change of global scope, construct or
mechanism. The count does not choose the revision; retain the formulation with a written
reason if the alleged alignment does not hold; every finding touching the element is
re-examined under rule 14 in the same act, as a new `findings.jsonl` line carrying the id it
supersedes. A tier move is a `tier_history.jsonl` line under rule 11's amendment regime.
`absent` is ordinary and never a correction unless the model stated the element as universal,
which you decide here and log. You do not loosen an element until a room fits.

## 3. The unattached lines

`propose` lines touch no element. Read them by lifted node: several rooms' unplaced
second-order themes pointing at the same target with no third-order theme holding them are
minted as one (`mem.py mint`, a `tier_history` line with move `splitting` or `merging`, logged and snapped),
the new theme written to `scheme_v2.jsonl` and its members moved with `mem.py reassign`, and the lines
are re-lifted (`python3 tools/ingest.py D --relift`). A proposal you accept becomes an element with status `candidate`
(`since: D3`), and the model is rewritten with it; one you reject is a particular with a
reason. An element supported only in one room remains in that local model and adaptation; it does
not enter the global model solely to fit the case.

## 4. The verdicts, and the rooms the model cannot compose

Rule the split verdicts with the criterion in front of you, and the `cannot-tell` lines stage D2
listed as unsupported by the room's numbers: a ruling is a `verdicts-D.jsonl` line with
`ruled_by: analyst`, `changed_from` (the readers' verdicts) and the reason; the readers' lines
stay. Rule 13 governs; the readers are not judges.

Then `uncomposed-D.md`: every `does-not-compose` room read whole through its forest, in its
own words (rule 12): what it did, what the model would need in order to say it, whether the
model should have that, and the condition that separates it from the rooms that compose. Name
the kind, yours and not the reader's: `outside-the-model`, the room organized and the model
cannot say how, the counterexample that bounds the model; `out-of-scope`, the room did not
organize, or did something the model is not about (received the event as news, talked about
another room's work, played), which bounds the model's scope and not its claims; `too-thin`, the
room is above `prior.md`'s floor and its record still does not show how it organized, which
bounds the record, read with its off-platform pointers beside it. The `out-of-scope` rooms are also
read together, since what they did instead may be a kind of its own.

**Local validation precedes a shared claim.** Resolve each supported exception in its local
model and ledger, including unshared particulars. Shared conditions require substantive
comparison of the rooms and a written warrant. Repeated corrections can define a cluster
branch; they do not force the same revision everywhere. If no defensible formulation survives,
replace or withdraw the claim under rule 14. Record unresolved local evidence explicitly.
An exception cannot be printed beside an unchanged universal claim as a substitute for a
scope decision. Preserve every pre-adaptation verdict alongside local and cluster judgments. The
list is carried to D4, D5 and E1. This is an in-sample return run as a census, in the spirit of Eisenhardt's replication logic: a
model that composes everything by being loose is weaker than one that composes most rooms and
can say which it cannot and why.

**The field's entries.** `out/sealed/FIELD.jsonl` names the tentative entries stage C4 took
from the field. Rule them as any element, by the rooms' lines: each becomes standing, bounded or
withdrawn under rule 11, with its `history.jsonl` line, and none stays tentative past the freeze.
Report them apart in `notes-D3.md` under a heading `The field's entries`, one line per id: how
many rooms instantiated, restricted, contradicted and left it absent, and the ruling.

## 5. The re-check

For every rewritten element, all rooms whose adapted account relies on it go back to their
resumed return lead against the revised model. Include positive and contrasting cases and
record how affected rooms were identified. Write `recheck-scope.json` with `affected_rooms`
(a list), `unaffected_rooms` (a room-to-reason mapping) and `reason` for the scope. These sets
must partition the analysed corpus. If the scope is uncertain, recheck all rooms. Every affected
room needs a revised local account with its local status; unresolved cases stay explicit.
Do not freeze a newer model hash than the one returned to the affected cases. A three-room sample may pilot the revision; it
does not certify untouched affected accounts. Preserve both versions.
First write `MODEL-D3.md`, the revised model as prose with ids (the re-check never reads the
prose written before the revision); then `handoff.py D --recheck <sub>,<sub>` builds
`handoff-D/recheck/` with the revised vocabulary, `VERSION` and model, and the verdict packets
for the same rooms in `verdict-D/recheck/`. Close the leg with `done.sh D3 --cut packets-out`.
The handler runs the labelers under the same brief into `DROPS/D/recheck/`, and
`dispatch.sh D3` sends the verdict packets to the verdict fleet (`_fleet_raw/D3v/`); when both
have returned, the harness runs `ingest.py D --recheck`, which compiles
`adaptations-recheck.jsonl` (ids `R-<sub>-<content-and-version-digest>-NNN`) and `verdicts-recheck-D.jsonl`, and opens `D3b`.
You read the before-and-after ledgers of those rooms and say in `notes-D3.md` whether the rewrite
fixed what the evidence pointed at; E1 reports them. Both verdict lines stand, with the version
on each.

## 6. The close

Pending lines retain their unresolved status and are counted separately from supported particulars. A locally validated account cannot contain pending claims. Adjudicate every original and recheck line; a completed recheck never silently accepts its lines. `exception-report-D.md`: per room,
particulars against accepted shared lines; per element, rooms adapting it by op; the
composition criteria in `prior.md`. Report fixed-global verdicts, local validation status,
particulars and corrections met twice separately. Repeated corrections are candidates for
clusters, never a failure threshold. Count distinct shared changes as well as ledger lines;
assess cluster adequacy at D4 to D5. Where all adaptations remain unrelated particulars, say:
*a model whose adaptations are all particulars has not composed*. The model at the close is
frozen as one version: `done.sh` records its hash at D3c's close (`out/_closes/model-D3.sha256`), and
the hash goes into `RUN.json`; `python3 tools/ingest.py D --relift` then re-lifts every ledger line to
it (the check at D3c and at D4 refuses a ledger that is not re-lifted); every ledger line is
re-lifted to it before stage D4, and the account, the figure and the data structure are re-read
against every amendment (rule 11). Write the re-read into `notes-D3.md` under a heading
`Re-read against the amendments`, one line per amendment: its id, what in the account, the
figure or the data structure it changed, or "nothing".

**The counts, last.** After every ruling is written and not before, `validate.py D3` computes
and you read: the four verdicts' counts over the analysed set, and `does-not-compose` by kind;
`cannot-tell` by threshold; the rooms stage C2's last story could not tell, how many of them
compose now, how many do not, and whether any room that story told does not compose here, the
measure of how well the loop prepared for this test; the composition rate of the rooms read
against a story at C2 beside the rate of the rooms never read against one, from
`story_rooms-pN.jsonl` and `verdicts-D.jsonl`, the nearest the run comes to measuring what the
stories were worth. Report them in `notes-D3.md`. No ruling is revisited because of a count: a
bad number is a fact to report, not a thing to fix.

## Moments to log

Each element group opened and closed with its counts by decision; each revision with its
adaptation ids and move; each minting and candidate element; each verdict ruled with
`changed_from`; each uncomposed room with its kind and condition; each finding bounded, and
each condition left as one room's description; the re-check rooms named; the composition criteria;
the counts read.

## Final message

The claim (what the return taught the model), the room that best supports it, the room that
most threatens it, the condition that separates them; then: lines by decision, revisions and
their causes, elements bounded, minted or made candidate, re-check rooms and what the rewrite
fixed, the diagnostics against `prior.md`, verdicts ruled, the four verdicts and the kinds of
`does-not-compose`, the bounds with their second room and the conditions still one room's
description, residue kinds named, how the last story's misses fared and the two composition
rates, what the return showed that the room notes did not predict; the licences exercised
(METHOD.md). A return value.

## Close

`done.sh D3` at every leg, every revision logged and snapped as it was made; the close-check report into
`notes-D3.md`; `handback-D3.md`; the head; the closing diary line.

**Interview point.** `D3c` writes `out/interview/D3c.md` (under 800 words: what you did, what you found, what surprised you, what you doubt, and the three questions you would most like to be asked) and closes with `done.sh D3 --cut interview`: the model returned to every room and adjudicated: where it composed, where it did not, what the corrections changed. The principal investigator may talk with you here, in a fork of this leg, run in a copy of your folder as it stood at the close (not read-only; nothing done there reaches the run); the run goes on from the cut either way. `done.sh` files the brief under the leg, the stage, the step and the minute, and refuses the cut without the brief (and, at a stage's end, without the handback).
