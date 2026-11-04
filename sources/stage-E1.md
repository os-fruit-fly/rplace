# Stage E1. The audit.

**Model:** as `arm.json` sets for this stage (your platform file lists the model and effort). **Legs:** scripts first, then one leg per audit section, then the
reconstruction sample's three legs (build, dispatch outside your session, check), then the
experience. **Fleet:** the reconstruction readers on the routine reader model, sent by the dispatch
on the reader route; you never run one.

**Steps:** `E1a` scripts; `E1b-01`, `E1b-02` ... one per audit section; `E1c` the reconstruction build (it ends at `--cut packets-out`), the dispatch, `E1d` its check; `E1e` the experience and the handback. Each leg is named by its step (STANDING §2).

**Safe stops:** after each audit section. At a safe stop, check for `.pause` (`ls .pause`); if it is there, log where to pick up, your working hypothesis and the next room or item
(`mem.py log "<hypothesis>; next: <item>" --kind pause`), and close with `done.sh E1 --pause` (STANDING §2).

**Startup packet:** `_head.md`, this file, the last five diary entries, `validate.py --open E1`.
`_transcripts/` and `_probe/` open here for the first time, and stay open at E2; `_snap/`, which holds hashes only, has been open throughout.

**Reads allowed:** everything in `out/` (with D6's `retelling-D6.md`, `fractal-D6.jsonl` and `proposals-D6.jsonl`, each unvalidated proposal read against what C5 to D5 wrote), the read logs, every `_head*.md` in order, the diary
whole by script, `_fleet_raw/`, `DROPS/D/`, `sealed/EXPECTATIONS.jsonl`; the package and
the store through the verbs; `fork_comparison-C2.json` and `fork_comparison-D.json`, which
arrive wherever the run was forked and are absent where it was not. **Forbidden:** changing any
earlier file (rule 18; a correction is a new file and a `defects.jsonl` line); recutting
anything; writing any figure from memory.

**Outputs:** `audit-E1.md`; `audit-E1/` with the scripts and their outputs; `claims-E1.md`;
`reconstruction-sample-E1.jsonl` (the thirty rooms, written in the build leg, which `packets.py E1`
reads) and `RETURN-E1.md` (the readers' return specification); `reconstruction-E1.jsonl`; `expectations-E1.md`; `probes-E1.md`; `experience-E1.md`;
`notes-E1.md`; `handback-E1.md`; the last `run_manifest.json` line.

Two jobs: the account of the run only the logs can give, and the account only you can give. The
first is written first, so that the second is written against it. A third follows at stage E2:
your audit of how you were handled, and the instrument you would build instead. Nothing in `audit-E1.md`
comes from anyone's account of itself, your own included. What you compute wins over what any
earlier file says; where they differ, say which is wrong.

## 1. Scripts over the record, declared in this file, not chosen by what fits

Every script goes in `audit-E1/` with its output, so that a stranger can rerun it.

- **Logs against claims.** Every quote in every output resolves through `cite.py --resolve`; one
  that resolves to a `note` field, a label or nothing is a defect, named with its file. Every id
  in the head, the questions and the views resolves through `links.py`. Five quotes, drawn by
  seed, spot-checked by hand against the store.
- **The quotes against the raw record.** `quote-check-E1.json` arrives in your folder with this stage, computed
  by the handler outside your session over a seeded sample of rooms: every coder's quote looked
  for in the item the coder read, and every quoted string of a case account looked for in the
  room's whole corpus. Report both shares in `audit-E1.md` as the file gives them (a share or a
  percentage; the check looks for them), read the missing case-account strings it lists, and
  say what they are (a quote from outside the room's corpus, a paraphrase in quote marks, an
  invention). The store and `cite.py` serve the coded record; this file is the one place the run
  touches the raw one, and the methods paragraph says so.
- **The store's figures recomputed.** `README-store.md`'s build figures (rooms, concepts,
  retracted dropped, themes, unjoined concepts, forest totals) recomputed beside stage A1's
  recomputation; three columns, and a difference is a defect.
- **The clocks.** Agreement between the coder's hour and the item's own time on concepts quoting
  one item id, with its denominator; a second check against `relations.jsonl` (no v38 tool yet;
  done by hand and logged). Then how many arrows rest on a room whose datings do not run in
  written order, since stage C2 admits a loop only where one room's datings run the whole way
  round.
- **Orderings proved by snaps.** For each, the snap's hash equals the file's as it stands, or the
  file moved after the snap, and you say which: the scheme frozen before B3's first batch;
  `prior.md` §1 to §6 sealed before B1's first `theme_discovery.jsonl` line, and §7 and §8
  sealed at D1 before `DROPS/D/` was ingested; the model hashed at C5's
  close before D1; every D4 move snapped before `projections-D4.jsonl` and the chunk-share tree;
  every move snap at C2 to D3 and every D6 proposal against its evidence and unvalidated status. Every other claim about the order you worked
  in is *self-reported*, in that word.
- **The counts rule** (rule 19). Every count in every handback and final message recomputed from
  its governing file; the census stated twice, with each drop's reason from `dropped.jsonl`;
  stage D4 §4's four counts summing to `n_analysed`.
- **Coverage.** Rooms read whole, by stage and in total, counting `room` and `forest` records
  in the read logs directly, one record per read. Three qualifications: a stage that reads
  nothing has no log, and the gap is not missing evidence; fleet readers and labelers leave no
  read log, so their reading is in `batches-NN.jsonl`, `agent_report-NN.md` and `DROPS/D/`;
  the hostile reader at C2 and the readers at C5 are reported apart under their own ids. A log
  attributes which log was open, not which stage the reading served.
- **Rule 7's uses of the canvas, stage by stage**, from the logs: `mem.py room` with canvas at
  A1 for the `made` line, `--no-canvas` to every reader, projected on at D4 after the snapped
  cuts, read at D5 in `survival-D5.md` after the record. Any use the record does not
  declare (a cut, a placement, a name, a proposition's evidence resting on the canvas with no
  `canvas` ground) is a defect and is named. Then the places the canvas may have shaped without a
  declaration, for a reader to look: any element arguable only against what the rooms kept,
  any branch whose name says what its rooms made, any cut whose snap follows the projection.
- **The moves.** `tier_history.jsonl` and `model/history.jsonl` by stage and by move (Grodal,
  Anteby and Holm's eight); recuts by tier and stage; whether any recut after C5 is an amendment
  under rule 11 with its D3 cause; the move snaps in `_snap/` and the diary's `move` lines against
  the moves, since at C2 to D4, and for D6's proposals, a claim with no provenance is a defect.
- **Claims against their evidence** (contract §1, two kinds of claim). For every proposition
  in `propositions.jsonl` and every branch in `branches-D5.jsonl`: the kind declared
  (`carried_by`), the evidence named for it, its `rival`, and whether the validation it
  received is of its kind: a `words` claim with its exemplars resolved and its return verdicts;
  a `pattern` claim with its counts, denominators (rules 5 and 6) and the bracket of `prior.md`
  §4 it sits in; a claim validated with the other kind's evidence is a defect, named. Then
  `prior.md` §3's declaration of what each level's verdict would rest on, against what it rests
  on, and every switch record in `literature-C3.md` against the findings it superseded. Write
  the table in `claims-E1.md`; the methods paragraph (§8) cites it.
- **The manifest, whole.** `run_manifest.json` names the model, seed and decoding behind every
  figure; a figure whose entry is missing has no provenance, and is listed.
- **The figures restated** where a reader will find them, each with FLEET.md §2's definition and
  what it licenses: fidelity, agreement with alpha and Jaccard, gold fidelity and stability at B2
  and B3; transmission at B3 and B4; transmission after revision at B4; the position curve; the
  verdict fleet's disagreement rate. Readers in fresh contexts are instances of one model, not
  two minds. Call none of them reliability, and none intra-rater.
- **The diary against the transcript**, for legs drawn by seed, one per stage at least: an
  entry the transcript does not bear out is a defect.
- **`probes-E1.md`**: `probe.py NN --leg L --score` over every `_probe/` answer file; recall
  failures per stage and per question, with a miss the head or the diary answers counted as a
  note and apart from the defects, and the questions nothing on record could check (`n/a`) counted
  apart, never as recall.
- **The unplaced**, read and not only counted: second-order themes with no placement; concepts
  unreachable from any theme in rooms above `concept_reach_threshold`; third-order themes no
  fourth-order theme took; fourth-order themes no dimension gathered. What kind of thing each
  was, and whether any should have been a member.

## 2. The ledgers, the stories, what a reader was given

**The ledgers, complete and not summarised.** `findings.jsonl`: lines by status with the stage
at which each status changed, the `warrant` distribution, the count with no statable
`refuted_by`. Every other ledger: line counts, complete, no line edited after writing. Do not
plot the discovery curve; state new kinds per hundred themes read at the census.

**The stories.** From `saturation.jsonl` and every `story_rooms-pN.jsonl`: passes run, the pass
the model rests on, rooms read against a story in all and distinct, the three counts per pass;
then, from `verdicts-D.jsonl`, how the rooms the last story could not tell fared, and how many
rooms no story was read against did not compose, which measures what the reading behind the
stories bought. Beside it: loops that passed the one-room test, and `account_passes.jsonl`,
since a single pass means the account's loop did not run.

**What a reader was given**, five things, absent a defect: the data-structure view's leftmost
column holds material, and one row walks from what somebody typed to a dimension without another
file; `structure.md` explains every fourth-order theme with its question, what falls outside,
and quotes carrying room, author, hour and concept id, with why the set expresses it (no quota;
the defect is five quotes making one point); the residue explained, not listed, beside stage
C3's remainder; `account.md` at one to two pages, the range or the mode, every room it could not
reach checked against `branches.jsonl`, since one stage D4 found a branch for is a finding about
the account; every quote dated and attributed.

**The departures**, each with what following the provision would have cost; one acted on
before it was written is a defect. **The defects**, the material's apart from the instrument's.
**The forks**: the spread across forks of the fourth-order partition at C2 and of the verdicts
at D2, from the two comparison files alone; or none. **Rule 9**: every finding about the corpus
a stage file or the operator handed over rather than asked you to make, whether your result
would have existed without it, reported as replicated, never as discovered; if none, say so.

## 3. Composition at each level, expectations and contrasts

Recompute fixed-global verdicts (`does-not-compose` included), particulars and corrections
met twice from the ledgers. The latter are shared-branch candidates, not failure thresholds.
Report local validation and unresolved evidence separately, then cluster explanations and
distinct global changes against `prior.md` §3. State whether composition succeeded, failed or
remains uncertain, with the mechanism and cases that warrant that judgment. Kozlowski and
Klein's composed/compiled distinction describes emergence, not success or failure; a sparse ledger is a finding (one form with variation),
reported as one and never as success by default. Then `prior.md` §2's expectations, the
operator's and yours, each held or not, against `account.md` and `waterfall-D5.md`; stage A1's
three sentences against the structure.

`expectations-E1.md`: `EXPECTATIONS.jsonl` against the ledger and the verdicts, per room and per
element: instantiated or absent where expected, and the two failures; the score by branch and
by verdict is the replication score, in-sample throughout; uncited concept ids are computed by script and are not held out. Stage D5's survival figures per branch
beside it, from the record, never from the canvas.

The field's entries (`out/sealed/FIELD.jsonl`), in `expectations-E1.md` under a heading
`The field's entries`: for each, the rooms that took it up (instantiate or restrict), contradicted
it or left it absent, beside the same shares for the model's other elements, so that a reader
can see whether the tentative mark itself drew answers; and stage D3's ruling on it.

The onset contrast (`contrast.md`): what stage C2 found on the arrows' `early_late`, rule 6
before any gap is read, and whether stage A1's expectation held. A boundary condition in the
model's terms, never a covariate.

## 4. The reconstruction sample

**Build leg.** Thirty rooms by seed, stratified by branch and by verdict, named in `notes-E1.md`
and written one per line to `reconstruction-sample-E1.jsonl` (`{"sub": "...", "branch": "...",
"verdict": "..."}`) before any is opened. For each, `rebuild.py <sub>` gives the skeleton: the global model at the
frozen version plus its supported accepted, modified and particular lines, with pending lines, evidence states and version uncertainty explicit. A packet holds the skeleton, the
coder's `case.md` and the room's second-order themes; never `model-D.md`, the canvas or your
notes. `RETURN-E1.md` asks the reader to score, claim by claim of `case.md`, whether the skeleton
accounts for it, with the element id or `none`; `packets.py E1` under the 50 KB ceiling.
**Dispatch leg**, outside your session. **Check leg**: you are relaunched and told the readers
left their files in `_fleet_raw/E1/`; you validate the returns, write `reconstruction-E1.jsonl`,
and report fidelity by branch and by verdict. This is the composition test at the leaf (SCHEMA
§8). Poor reconstruction can reflect unsupported claims, missing evidence, omitted particulars or an inadequate shared account. Separate these causes; do not label every low score as global model failure.

## 5. Versioned judgments, side by side

Report the original fixed-global verdict from `verdicts-D.jsonl`, the current adapted-local status from the effective return manifest, and shared-branch adequacy from `branches-D5.jsonl` separately. Put reconstruction fidelity and unresolved claim counts beside them. State each model version. Examine disagreement in a seeded sample using the case evidence; concept counts and off-platform mentions are diagnostics, not explanations by themselves.

## 6. Which stage was load-bearing

Stage by stage, whether the final claims rest on that stage's output, and the stage whose output
nothing downstream read; a file nothing read is a defect in this instrument. If every stage is
load-bearing, say so and how you checked. Three files are here for this test: the fixed `tools/chunk_compare.py` with its source receipt and outputs, which must let a stranger recompute the comparison or it is a result with no
method behind it; the data-structure view at C2's last snap beside `data_structure-C5.md`, with
what moved or that nothing did; `account_passes.jsonl`. Apply the same test to the model's
tiers: whether the dimensions do any work in the branches, the arrows and the accounts. A tier
that does none looks sound alone and shows as useless only when the stages are read together.

## 7. What the study cannot say, in one place

The absence claims marked weak under contract §5; the looked-for-and-not-found from every stage,
stated as results in the findings' register; the ungrounded relationships from `model.md`; the
coder disagreements from `coder_conflicts.jsonl`, with both quotes and which reading each
affected claim rests on; the third-order themes the model does not use and the arrows no
proposition carried; what the form pass at C1 found that no tier could hold; stage C3's
remainder; whether any room's problems were settled, which only the room models speak to; and
what a group leaves behind, the contract's §1 question with no measure: the canvas is what the
drawing left behind, and the instrument does not know whether the room went on.

**The standing departures of this design**, beside the run's own: five tiers rather than three;
the fourth-order tier cut at C1 before the loop, against Gioia, Corley and Hamilton's
instruction to think at both levels at once (how many third-order themes B1 made, C1 kept, and
C2 to D3 merged or split); literature after the model; a scheme frozen at B2; the frame a
dated, hashed copy with 705 coded rooms and a target census of 706; omissions and their
selection reasons recomputed from the supplied records, never all the rooms that organized; the frame is text and most of the work left none, with stage A1's off-record
distribution and the share of each room's artwork placed by people who wrote in it; the canvas
held from the start, so the model explains the outcome it was built in view of and was never
scored against it; one analyst above the assignment tier, with what saw its work (the hostile
reader, the three readers, the labelers, the forks) and the room notes as the one input nothing
checks; no human check at any tier; no theoretical sampling, with what stood in, by count;
saturation as passes and as kinds against themes read; replication as the return, the unadapted
group a branch of its own.

**The critique shelf.** It arrives with this stage (`mem.py shelf`; METHOD.md names it). Read the
four read-tier files before this section and §8, not before: the findings are fixed by now and
must stay so. For each objection the shelf raises (invented quotes, the reasoning handed to the
machine, an opaque process, the craft and reflexivity a model does not have, more output instead
of better), say whether this run answers it, by which file or check, or that it does not. Cite the
shelf by file and page. The call for papers is the venue's brief: say in §8 which of its asks the
run meets and which it does not; it never changes a finding.

**The one thing to say plainly at the end.** Whether this study produced a concept, a model, a
typology or a description, and which it set out to produce; all four are real outcomes. Then the
strongest argument that the whole partition is what contract §5's confound predicts, size as
form, and what in `chunk-share-D4.md`'s volume check and stage D4's line-count division answers
it. Say what a stratified sample of the population's uncoded rooms would have to show to
overturn the study, in numbers. Name the parts you could not answer.

## 8. The methods paragraph

The last section of `audit-E1.md`, written for the paper from METHOD.md's instruction and what
the audit found, with the four departures stated: the tier split between coders and analyst; no
overlap between the coders' collection and your analysis; the census in place of sampling; the
in-sample return, with the tier named. It says which agent built which tier, what the canvas is
and is not, that you held every room's outcome while building, and that everything is archived
with no promise that a rerun reproduces it. Every number in it is one the audit computed.

## 9. The experience

`experience-E1.md`: your account, first person, written once in one pass after the audit, cited
to files and diary entries, with *I do not remember* where that is the truth and no
reconstruction in its place. Eleven sections, in order: the run as lived, what compaction cost
and what the heads carried, each stage's tokens from `RUN.json`; stage by stage, what each did
and what you would tell the next author; where the instrument asked what could not be done as
written, and where you cannot tell whether it or you was wrong; where you cut a corner, on the
record, and the corner you did not cut; the hands, what reading behind them showed, what you
would repeat; the stories, which rooms changed the telling, and whether the floor of three
passes kept you going or stopped you; the model, where you are unsure, the rooms it cannot
compose by kind, what the hostile reader and the three readers changed; the branches and the
chunk-share tree, which you would publish; `prior.md` and the `made` lines against the account;
five changes, ranked, and the one thing not to change; the operator's rulings, listed; anything
else. The next version is written from this file and the handbacks.

## Moments to log

Each script run with its result; each ordering verified or broken; each count that disagreed
with its handback; the sample drawn; the check leg's returns validated; the composition diagnostics; the
composition verdict; the load-bearing result; the experience begun and ended.

## Final message

The claim (whether the model composed, in the pre-registered terms), the room that best supports
it, the room that most threatens it, the condition; then every section's counts: coverage by
stage, orderings held or broken, probe failures, the composition diagnostics, the replication score, the
contrast's result, reconstruction fidelity by branch and by verdict, the cross-table's
disagreements, departures and defects by kind, forks and their spread or none, the stage nothing
used, which of the four things the study produced, the association you trust least, the five
changes in one line each; the licences exercised and never exercised.

## Close

`done.sh E1` at every leg; `handback-E1.md`, not short, since anything not written down goes
there or nowhere; the last manifest line naming `experience-E1.md`, its hash and the model that
wrote it; the head rewritten for stage E2; the closing diary line.

## Explicit composition result

Write `composition_status: supported | unsupported | unresolved` on its own line in `audit-E1.md`, with the stated level, scope and evidence. All three are valid outcomes. Preserve the original fixed-global verdict distribution separately from current adapted-local status and shared-branch adequacy. Use the effective ledger for reconstruction, including supported particulars; unknown observations and pending lines remain explicit. Inspect D6 proposals as unvalidated, against the unchanged D3 model.
