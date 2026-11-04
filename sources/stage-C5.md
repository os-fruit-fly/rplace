# Stage C5. The account.

**Model:** as `arm.json` sets for this stage (your platform file lists the model and effort). **Legs:** build (one leg per pass of the account, closed at the pass's end or earlier when you
choose; every move logged with `mem.py log --kind move`, its Grodal, Anteby and Holm move named,
and snapped with `python3 tools/snap.py C5 move-<move>-<n>` when it is made);
dispatch (three readers on the platform's reviewer model, outside your session, sent by
`fleet.py`); check (you are relaunched, told the readers left their files in
`_fleet_raw/C5/`, and revise, one leg per pass). **Fleet:** three readers, once. **This is the
last stage before the model and the tiers are fixed.** After it nothing below the model moves
except as an affected-case-validated amendment at D3 (rule 11); D6 records separate unvalidated proposals, and stages D1 to E1 measure against it.

**Steps:** `C5a-01` ... one per pass of the account; `C5b` the readers' build (it ends at `--cut packets-out`), the dispatch, `C5c-01`, `C5c-02` ... the readers' check, one leg per pass over the returns; `C5d` the Gioia table, the dynamic model and the figure, the handback and the interview. Each leg is named by its step (STANDING §2).

**Safe stops:** after each logged move, after each section of the account, and after the data structure and the figure. At a safe stop, check for `.pause` (`ls .pause`); if it is there, log where to pick up, your working hypothesis and the next room or item
(`mem.py log "<hypothesis>; next: <item>" --kind pause`), and close with `done.sh C5 --pause` (STANDING §2).

**Startup packet:** `_head.md`, this file, the last five diary entries, `validate.py --open C5`;
the last story, `model/story-pN.md` of the pass C2 kept. In a check leg the harness adds one
line: the readers left their files in `_fleet_raw/C5/`.

**Reads allowed:** everything of yours: `model/` as it stands after C3 and C4 (`mem.py diff-model
<snap>`, with the name of C2's last close snap in `out/_snap/`, shows what they changed; its arrows carry the mechanisms C3 supplied and the `from-field`
hypotheses C4 entered, which the propositions run on; read `manifest-C4.txt` first, then `manifest-C3.txt`), `model.md`, `structure.md`, `dimensions.jsonl`, `fourth/fourth.jsonl`,
`concept.md`, `literature-C3.md`, `mapping-C3.jsonl`, `field-C4.md`, `findings.jsonl`, `within_case.md`,
`story_rooms-pN.jsonl`; your notes through `mem.py note`; `counts.py`; rooms by query (`mem.py
room`, `forest`, `where`, `codes`, `pairs`, `rooms --with`, `contrast`); quotes through
`cite.py`; `_fleet_raw/C5/` in check legs. **Forbidden:** new elements (the model is fixed at
the close of C5 except through validated amendments at D3); clustering anything (stage D4); the canvas as an undeclared ground
(rule 7); your notes to any reader.

**Outputs:** `account.md`, the final version of the model's explanation; `sketches.md`;
`account_passes.jsonl`; `prose-test-C5.md`; `propositions.jsonl`; `author_claims.jsonl`;
`RETURN-C5.md` and three packets; `readers-C5/` (three returns) and `notes-C5.md` answering
them; `data_structure-C5.md`; `figure-C5.md` (the model figure as text and as the generated
drawing); `implications-C5.md`; `findings.jsonl` lines; `tier_history.jsonl` and
`model/history.jsonl` lines for any recut; when the third-order tier is recut, `scheme_v2.jsonl` and `assignments_final.jsonl` rewritten
(`mem.py mint`, then `mem.py reassign`, as stage C2 says); a `run_manifest.json` entry; `handback-C5.md`; the
model frozen (`done.sh` records the hash of the model and its tiers at C5d's close,
`out/_closes/model-C5.sha256`).

Write sections 1 to 5 before 6, and 6 before the packets go out; the figure and the data
structure are re-emitted at `C5d` from the model that survives the readers. A cut
can still move here; test every one you suspect while the account is open. If a proposition
will not state because a fourth-order theme is wrong, move it now, logged and written as stage C2
says (`scheme_v2.jsonl` and `mem.py reassign` for a third-order recut),
re-placing what the amendment touches yourself and redrawing whatever depended on it.

## 1. Write the model as prose, before you draw anything

`account.md` is the model in continuous prose, one to two pages: how organizing came about in
these rooms and how the parts worked together, so that a reader who was not here can follow it
once through and say what it claims. Tell it both ways: from the population down to a room,
and from three rooms up to the population. Every claim goes through an element id and a quote
or a transition; the concept sits in its place; the loops and the irreversibles across hour 73
are named; where the model should break is said in its own terms. It describes the universe,
not the mode: read it against a room you know is odd and make it say what happened there as one
way of running the same structure; every element should have a range. The last story of stage
C2 is its first draft, and the rooms that story could not tell (`story_rooms-pN.jsonl`) are its
first test. Name every community the account cannot reach, one clause each; the return (D1 to D3) returns
them anyway (rule 12) and stage D5 reads them inside their branches.

Three things this catches. A model you cannot write as prose is a taxonomy with arrows added;
if every paragraph is *and also*, say so. An arrow that will not survive being stated as *when
X, Y follows, because Z* is not grounded, whatever `arrows.jsonl` says. A probabilistic claim needs evidence for its tendency and scope. If the relevant condition is unknown, state that uncertainty; do not invent a boundary or turn uncertain support into a deterministic mechanism (rule 16).

## 2. The prose test on the names

Every fourth-order theme and dimension is a construct declared at stage C2 (borrowed, adapted,
coined). In `prose-test-C5.md`, write one sentence per construct in which the name does
theoretical work, *because the room had X, Y could happen*: the sentence a reader would say
about a room using the name and nothing else. A name that only labels the sentence's subject
and does no work in it is a description one tier too high; recut it under rule 11, logged, and
keep the grounded phrase as the gloss. A name a reader will mistake for its `mistaken_for`
construct without being told needs its difference stated in the account. A third-order theme
that turns out to be named for a construct is renamed in the material's words, logged.

## 3. Draw it more than one way

`sketches.md`: at least three arrangements of the same model, each with a paragraph on what it
showed and what it hid; by time on the canvas clock, by tier (conditions above, mechanisms in
the middle, what follows below), by trajectory (one room's path, then a second whose path
differs). If two drawings put the same element in different places, that element is doing two
jobs and is a candidate for a recut. Working sketches; section 10 specifies the figure.

## 4. Simplify, and say what it cost

Cut the model to what a reader can hold at the top; the count is yours, set by what keeps
composition and explanatory power alive (contract §2), with why in `notes-C5.md`. For every
element cut:
what it was doing and what the model can no longer account for without it. For every element
kept over an alternative: which alternative and why. A cut element keeps its id in `model/`
with its status changed and a `history.jsonl` line with the move, logged and snapped when it is
made.

## 5. Recut when the account says to

Rule 11 governs, and a recut here is the ordinary outcome, each a `tier_history.jsonl` line with
its move, logged and snapped when it is made. Keep the construct declaration current with every recut, and re-examine
every `findings.jsonl` line it touches in the same act (rule 14). Before pass 1, write in
`notes-C5.md` what would make you prefer a later account to this one; a criterion written after
the passes exist is not a criterion.

**A counterexample requires explanation.** Record the evidence and compare local adaptation,
construct or mechanism refinement, a supported scope condition, and withdrawal. Do not invent
a condition to preserve a claim. An isolated case can validate a local exception without
automatically revising the shared model. Preserve unresolved evidence and record the decision
in `findings.jsonl` and model history, including any weakened or withdrawn claim.

## 6. The propositions

**A proposition here can carry a number**: a claim of the form *authority is claimed and no
dated consequence of it appears anywhere* is answerable against the analysed set, whichever way
the count comes out.

Write the propositions the model implies into `propositions.jsonl`, one line each, numbered:
the figure tags its arrows with them and stage D5 says which hold in each branch.

```json
{"id": "N12", "statement": "...", "rests_on": ["A03", "A07"], "theorised": false,
 "finding": "F-031", "carried_by": "words|pattern|both", "rival": "one clause"}
```

For each, in the line or in its paragraph in `account.md`:

- **The claim**, in one sentence, in the model's own terms.
- **The mechanism**, carried up from the arrow that grounds it and marked `from-literature`
  where stage C3 supplied it. A proposition without a mechanism is a pattern. **Where the
  proposition sits at the dimension tier and the arrow that grounds it sits lower, say so**,
  and say whether every arrow beneath it shares that mechanism; if not, narrow the proposition
  to the subset that does, or drop it.
- **The evidence in this corpus**, with its count, its gate (rule 5), and the contract's §5
  warning where the count is an absence; rule 6 governs every absence: say how many
  communities could have carried the thing before you say it is missing from any of them.
- **Whether the arrows beneath it are observed or theorised** (`theorised`). A proposition
  resting wholly on `reading-alone` arrows is a conjecture drawn from the data structure, and
  legitimate. Mark it.
- **What carries it** (`carried_by`, contract §1): `words`, a claim about what rooms did or
  meant, validated by exemplars that pass its gate and by the return; `pattern`, a claim about
  a distribution, an order on the clock or a difference between groups of rooms, validated by
  counts with their denominators and by the documented events of the 73 hours; `both` only
  with one named primary in the paragraph. The evidence you name is of the kind you declare;
  a `pattern` claim offered quotes as its proof, or a `words` claim offered a count, is the
  defect stage E1 looks for.
- **The strongest rival** (`rival`): the other reading of the same evidence that a careful
  stranger would offer, and what in the record decides between them; where nothing in the
  record does, the claim is thin (rule 8) and says so.
- **What would falsify it in a population that is not this one.**
- **Where it should not hold**: the boundary, in the constructs the model is built from. Corpus
  size, subreddit topic and which rooms the frame holds are limits on the sample, not boundary
  conditions; a boundary that names a surface feature of the setting is not one.

**Do not write more than the model earns**: four defensible propositions are better than a
dozen padded ones. **A thin claim is made and labelled thin** (rule 8), with what it would take
to firm it up; *the evidence is weak, but the difference was large and the record suggests why*
is preferred to silence.

**A proposition that says a problem was solved is a claim, not a report.** One about task
division, task allocation, reward provision or information provision is stated from your
structure and `mapping-C3.jsonl`; the return (D1 to D3) reads it room by room. Write it so that it
can fail.

## 7. The passes

Every pass, in the build leg and in the check leg, is one leg and one line in
`account_passes.jsonl`:

```json
{"pass": 2, "t": "<ISO>", "leg": "C5-build-2", "what_changed": "one clause",
 "tier_events": ["<ids from tier_history.jsonl and model/history.jsonl>"],
 "sketches_tried": 3, "elements_cut": ["..."], "criterion_says": "prefer|reject|no change"}
```

Stop when a pass changes no element and no cut. No cap; from pass 4 on say in `notes-C5.md`
what the criterion says about each. When the passes stop, build the packets and close.

## 8. Three readers

**Build leg, last pass.** Append this stage's entry to `run_manifest.json` (the readers' model,
seed, decoding, count). Then, in this order:

1. `author_claims.jsonl` first: five to nine lines, each one claim you believe `account.md`
   makes, in a form a reader could agree or disagree with: `{"id": "c3", "claim": "...",
   "where": "paragraph 4"}`.
2. Three rooms named in `notes-C5.md`: one the account reaches easily, one the last story could
   not tell, one from the side of the onset contrast the account has visited least. Draw them by
   query, never by opening notes.
3. `RETURN-C5.md`, the one return specification (FLEET.md): the return line below, the end
   marker, and the line telling the reader to confirm it reached it. Three packets
   (`packets.py files --stage C5 --name C5-reader-k <files>`, the three rooms dumped first from the verbs into files), each with
   `account.md`, `figure-C5.md`, `propositions.jsonl`, the three rooms through the verbs with
   `room` served `--no-canvas`, `forest` and `cite.py` (never your notes), and nothing else of
   yours, under the 50 KB ceiling. The instruction, verbatim: *Read the account as a stranger.
   Say where it carries what it means and where it does not, both ways: a sentence you cannot
   follow, a claim you cannot find the evidence for, a room you can name that the account does
   not fit, jargon a reader would not accept. Do not propose another model. A disagreement is
   never a verdict.* Then: *For each of the three rooms you were given, say whether the account
   describes what happened there and, where it does not, what the room did instead, one
   paragraph per room.*

The return line: `{"reader": "r1", "served": "<sha256 of account.md>", "claims": ["..."],
"relations": ["A03 acts on P04"], "could_not_follow": ["quoted"], "unsupported": "...",
"rooms": [{"sub": "...", "fits": true, "instead": "..."}]}`, five to nine claims in the reader's
own words. **Stop here.** Close with `done.sh C5 --cut packets-out`. Your session ends; nothing more of this stage runs on your model until the check leg. The dispatch runs without you, on the platform's reviewer route, each reader in a session of its own. The next launch of stage C5 is the check leg, and its packet tells you one thing: the readers left their files in `_fleet_raw/C5/`.

**Dispatch leg.** Not yours. The dispatch sends each packet to a fresh reader on the platform's reviewer model, collects the
returns into `_fleet_raw/C5/`, validates them against `RETURN-C5.md`, reissues what fails the
schema, and closes. Nothing in it reads your files.

**Check leg.** You are relaunched. Copy the validated returns into `readers-C5/`. Score fidelity
both ways in `notes-C5.md`: your claims each reader recovered, and claims they recovered that
you did not write. A claim all three found that you never intended is the account teaching
something unintended. Every divergence is a defect in the account, not the reader;
`author-error` is a permitted verdict. Answer every item under rule 13: an error is fixed; a
room the account does not describe is a bound written at section 5 or a residue named for
the return (D1 to D3); a disagreement about how to tell it is printed beside the account; every change is
logged and is a pass (section 7). Nothing a reader says changes an arrow's grounding. The
readers are not judges: they tell you whether the account carries what you meant and whether
it describes their three rooms, and nothing else. They run once; no second round.

## 9. The data structure, final: `data_structure-C5.md`

Nothing is moving now. The display over every concept is generated: `gen_views.py` writes
`_views/data-structure.md` and `.tsv` at every close, one row per first-order concept up to its
dimension, never edited (rule 15). What you write is `data_structure-C5.md`, the table this
method is named for, from the tiers as they finally stand, all five of them: full over the
tiers, representative in its quotes. Six columns, one row per third-order theme at minimum,
more where a theme needs them, so that every third-order theme, fourth-order theme and
dimension appears:

| representative quote | first-order concept | second-order theme | third-order theme | fourth-order theme | aggregate dimension |
|---|---|---|---|---|---|
| the participant's words | the coder's concept | the coder's theme | the theme it was placed on | the theme it feeds | the dimension it feeds |

**The leftmost column is material through `cite.py`, never a label you wrote.** Where a quote
will not carry a row on its own, use the coder's second-order theme label and say so in the
cell. **Every row's quote carries its metadata**, in the row or in a footnote keyed to it:
community, author handle as the record carries it, the hour since the canvas opened, and the
concept id. **Rows show the range rather than the centre**; name in `notes-C5.md` the rule that
chose them, and the paper's figure is a sample of these rows chosen by that rule. **Carry the
residue**: below the table, the third-order themes no fourth-order theme picked up and the
fourth-order themes no dimension gathers, each with the account from `structure.md` and one of
its quotes. **Keep it to what one person can read**; `structure.md` carries the rest.

## 10. The figure

One figure, taken in at one pass, in `figure-C5.md`, drawn once with the theorised arrows and
once without; `gen_views.py` draws both from `model/` and `propositions.jsonl` into
`_views/figure-model.md` (Mermaid) at every close, and the text beside them is yours.

- **The things at the top and the arrows among them**, the size section 4 reduced the model to
  (as many as a reader can take in at one pass; say why the count), every element and arrow by
  id.
- **Every arrow is tagged with the id of the proposition that carries it. An arrow no
  proposition carries is not drawn.**
- Conditions on one side, what follows on the other, and **things named for what they do in
  the middle**, the mediators. If the figure has no middle column, say so: a two-column lattice
  with tagged arrows is a taxonomy, and a reader should be told which they are looking at. Show
  loops as loops, only where `model/loops.jsonl` records the full dated cycle at its stated within-room or inter-room level. Do not turn cross-case similarity into a process loop.
- The imposed terminus belongs in the picture: placement stopped at hour 73 for everyone.

The text specifies the figure precisely enough that someone else could draw it: every box,
every arrow, what each arrow is grounded in, the instance shown for it (the quote or the forest
transition from its `support` or `support_transition`, so that the arrow is a thing that
happened and not a line), its proposition id, and the community count on it. An arrow with no
instance is not drawn (contract §2). Then, in one paragraph, **what the figure leaves out**:
the arrows no proposition carried, the third-order themes the model does not use, the register
the topic-based coder tier scattered.

## 11. Transferability, and where the model should fail

Say what carries. Establish from the evidence the relevant conditions: voluntary participation,
existing authority, resource access, legal or informal commitments, the external clock and
whether failure dissolves a group. Do not assume all rooms share these conditions. Name
settings where the conditions plausibly hold and where they do not, what the model predicts,
and what this record cannot check. State the frozen frame and A1 exclusions from their files:
705 rooms in this snapshot, with 706 a target census, not complete observational coverage.
The artwork-based frame cannot warrant claims about all communities that organized.

Name the conditions under which the model should hold and should break, in the things the model
is built from. Corpus size, subreddit topic and which rooms the frame holds are limits on the
sample and do not count here.

## 12. Implications

`implications-C5.md`: what the model implies for the theory question, in the model's own terms;
what a counterfactual at a leaf would borrow from a neighbouring leaf, with the mechanism
explicit (contract §1, prediction secondary); what the return (D1 to D3) should find if the model
composes, written as expectations the handoff can carry (which elements should instantiate in
which kinds of room, which should be absent), so that the return (D1 to D3) is a replication in Eisenhardt's
sense and not a re-reading. Stage D1 writes `EXPECTATIONS.jsonl` from this file; stage E1
scores the ledger against it. It also says, in one paragraph, what the model implies for which
forms keep the work alive, answered from the record (contract §1): `organizing_end_hour`, the
aftermath share and `work_remained` in `organizing_end-A1.jsonl`, where silence leaves the outcome unknown and the last coordinating turn is a last
observation, not a demonstrated end. The canvas is not evidence here.

## 13. What you may not do, and what the canvas is here

You may not cluster anything; that is stage D4. A room the account cannot reach is named, not
fitted with a new element. If the account claims which of the contract's §1 four problems your
structure reaches richly and which thinly, that claim is stage C3's mapping restated, and the
return (D1 to D3) reads it beside the ledger.

The canvas is what was made (rule 7). The account may say, in one paragraph, how the rooms whose
record says their work was kept (`work_remained`, stage A1) organized differently from those
whose record says it was lost or falls silent, in the model's terms; you held
the canvas throughout, so this is a comparison and never a prediction, and stage D5 reads it
against the canvas by branch. The paragraph
says whose pixels it is about: much of a room's artwork was placed by people who never wrote in
the room (stage A1 reported the share placed by those who wrote in it), so a claim about what
the room's members kept and a claim about what survived on the room's patch are two claims, and
the paragraph makes one of them by name or is not written. It may not be built from the canvas:
no element is cut, kept or named because of what a room drew, and no proposition takes the
canvas as its evidence.

## Moments to log

The criterion; the account's drafts, one entry per pass; each sketch and what it hid; each
element cut and what it cost; each name that failed the prose test; each recut with its move;
each finding bounded or changed; each proposition written, thin ones marked; the three rooms
named for the readers; each reader item and its answer; the rule that chose the table's rows;
each expectation written for the return.

## Final message

The claim, the room that best supports it, the room that most threatens it, and the condition
that separates them. Then: passes run and what each changed; arrangements drawn and which the
account rests on; what you cut and what the model can no longer account for; tier events by
tier, and whether any third-order recut moved second-order themes; names recut by the prose
test; the readers' fidelity both ways, their items by kind and what changed, and what they said
of their three rooms; the criterion and what it says about the pass you kept; propositions,
how many thin, how many wholly on theorised arrows, how many `from-literature`; things and
arrows in the figure, arrows shown by a quote and by a transition, arrows dropped; rows in the
data structure and the rule that chose them; the expectations written for the return; what the account
showed that the room notes did not predict; the sentence in `account.md` you are least sure a
reader will take as meant; the licences exercised (METHOD.md). A return value.

## Close

`done.sh C5` at the end of every pass, or earlier when you choose, every recut, element cut or
dropped hypothesis logged and snapped as it was made; paste the close-check report into `notes-C5.md`; the harness hashes `model/` and
the account; `handback-C5.md`; the head; the closing diary line.

**Interview point.** `C5d` writes `out/interview/C5d.md` (under 800 words: what you did, what you found, what surprised you, what you doubt, and the three questions you would most like to be asked) and closes with `done.sh C5 --cut interview`: the model finished: the data structure (the Gioia table) written, the dynamic model explained, the figure plotted. The principal investigator may talk with you here, in a fork of this leg, run in a copy of your folder as it stood at the close (not read-only; nothing done there reaches the run); the run goes on from the cut either way. `done.sh` files the brief under the leg, the stage, the step and the minute, and refuses the cut without the brief (and, at a stage's end, without the handback).
