# Stage C2. The model: the loop.

**Model:** as `arm.json` sets for this stage (your platform file lists the model and effort). **Legs:** one per pass, closed at the pass's end or earlier when you
choose. Every move inside a pass (a dimension cut, a fourth-order recut, an arrow added, bounded
or withdrawn, a hypothesis kept or dropped) is logged when it is made (`mem.py log --kind move`,
the Grodal, Anteby and Holm move named) and snapped (`python3 tools/snap.py C2
move-<move>-<n>`). **Fleet:** one hostile reader, once, before the final passes (§6): build
(the pass you expect to keep, with the packet), dispatch (outside your session, one reader on
the platform's reviewer model, sent by the dispatch), check (you are relaunched).
You never run the reader and never call a model.

**Steps:** `C2a-01` ... one per pass; `C2b` the reviewer's build (the pass you expect to keep, with the packet; it ends at `--cut packets-out`), the dispatch, `C2c` the reviewer's check and the mid-stage interview; `C2d-01`, `C2d-02` the closing passes. Each leg is named by its step (STANDING §2).

**Safe stops:** after each logged move, after each whole room read for the story, and after each pass. At a safe stop, check for `.pause` (`ls .pause`); if it is there, log where to pick up, your working hypothesis and the next room or item
(`mem.py log "<hypothesis>; next: <item>" --kind pause`), and close with `done.sh C2 --pause` (STANDING §2).

**Startup packet, every leg:** `_head.md`, this file, the last five diary entries,
`validate.py --open C2`; the previous pass's `model/story-pN.md` and `saturation.jsonl` tail.
First leg only: `METHOD.md` whole, the tier A shelf (`mem.py shelf`), `prior.md`, `contrast.md`.
In the check leg the harness adds one line: the reader left its file in `_fleet_raw/C2/`.

**Reads allowed:** `scheme_v2.*`, `fourth/fourth.jsonl`, `assignments_final.jsonl` (never
`assign_final.jsonl`), `multiplacement_log.jsonl`, `coder_conflicts.jsonl`, `form_pass-C1.md`
(the form-pass findings, `FP-01` on, which exist there and nowhere else); rooms and themes by
query (`mem.py rooms --with`, `contrast`, `where`, `pairs`, `after`, `forest`, `room`, `when`,
`codes --third`, `codes --fourth`); your notes by `note`; `finding`, `findings --touching`,
`question`; the views; quotes through `cite.py`; `counts.py`; `_fleet_raw/C2/` in the check
leg. **Forbidden:** the explanation literature (stage C3); rooms in order; the canvas as an
undeclared ground (rule 7); your notes, findings or prior to the reader.

**Outputs:** `model/elements.jsonl`, `model/arrows.jsonl`, `model/loops.jsonl` (empty if no grounded loop), `model/history.jsonl`;
`fourth/fourth.jsonl` recut in place; `dimensions.jsonl`; `structure.md`; `concept.md`;
`model.md`; `within_case.md`; `model/story-pN.md` and `story_rooms-pN.jsonl` per pass;
`saturation.jsonl`; `findings.jsonl`, opened here if not before; `tier_history.jsonl` lines for
every recut and every item it moved; when the third-order tier is recut, `scheme_v2.jsonl` and
`assignments_final.jsonl` rewritten (below); `_questions/<slug>.md`; `RETURN-C2.md` and one packet;
`review-C2.md` answered in `notes-C2.md`; a `run_manifest.json` entry for the reader;
`notes-C2.md`; `handback-C2.md`.

Structure, concept and model are one loop: **Part A** the data structure (dimensions, and the
fourth-order tier recut where it must be), **Part B** the concept, **Part C** the model, and at
the end of every pass **the story**, told again and read against rooms. Read all four before
starting any. The order inside a pass is yours.

## 1. Before pass 1

**Read the shelf.** `METHOD.md` says what each work on the read tier is for here and how they
rank; its hierarchy governs. Re-read Gioia, Corley and Hamilton whole (`mem.py shelf`). The
on-request tier (`mem.py shelf --list`) may name and recognise, and nothing else; the
explanation literature stays shut until stage C3. Re-read `prior.md` and the contract's §1
beside it.

**Read the ledger**: `mem.py pairs --level third` and `--level second`: which third-order themes
answer which, in how many rooms, with the limit printed. The ledger shows members belong
together in the record; it is never, on its own, an arrow.

**Write the criterion**, one paragraph in `notes-C2.md`: what would make you prefer a later pass
to this one. The loop's failure is ratcheting; a criterion written after the passes exist is not a
criterion. Number every pass; keep every version (`structure.md`, `structure-p2.md`,
`model-p2.md`, `model/story-p2.md`; rule 18); say at the end which pass the model rests on. **The
stopping rule** (contract §6) is a guide: stop after two consecutive passes in which no
`tier_history` event occurred, no arrow was added, bounded, demoted or withdrawn in
`arrows.jsonl`, and no sentence of the story that names an arrow or an element changed. From the
third pass on you may declare the stop before that, with written reasons in `notes-C2.md`: what
the last passes changed, why another would not change more, and the rooms that argue against
stopping. One line per pass in `saturation.jsonl`. The rule watches the arrows and the story's sentences as well as the
tiers because a rule that watches the tiers alone cannot see an arrow, which is how v35 stopped
too early. Read §5's three counts as a trend across passes; a pass in which `told-with-residue`
rose is a stopping failure, and the residues are the next pass's material. A curve still climbing
at the last pass is a finding about the structure. From pass 4 on, keep the pass that best
satisfies the criterion, not the last, and report what you discarded. The floor is there because
the first telling that holds is the one you most want to stop at.

**The tiers stay open up to the line** (rule 11), the third-order tier too, the rule amended
first and the touched second-order themes re-placed by you. A recut third-order theme is written into
`scheme_v2.jsonl` in place (its line edited; a new theme added with the next free id, minted with
`mem.py mint`, and its gate), and each re-placed second-order theme goes through `mem.py reassign
<sub>:<tNN> --theme T3-NNN --reason "..."`, which rewrites that theme's line of
`assignments_final.jsonl` and records the move on it; stage D1 lifts the rooms from these two files. Every recut is a `tier_history` line
with its move, logged and snapped when it is made, every item it moved is logged, and every `findings.jsonl` line it
touches is re-examined in the same act (rule 14).

**The fork.** Where the operator forks the loop, the fork is taken as C1 closes, so every fork
holds the same `assignments_final.jsonl` and `form_pass-C1.md` and diverges from this stage's
first pass; each fork runs C2 to D3; the carried fork is chosen by the rule declared in `RUN.json`
before any fork ran (`HOW-TO-RUN.md`). You are not told you are a fork and you do not choose the
carried one.

**Open distinctions.** Where two readings of a partition, an arrow or a bound stay open across a
pass, open `_questions/<slug>.md` (one per file, 600 words; `mem.py question <slug>`) and close
it with a verdict line, never by deleting it. The recall probe asks for the open slugs.

## 2. Part A: the data structure

No relationships in this part.

**The fourth-order tier**, cut at C1, is recut here where the material demands (rule 11), each
recut declared as a construct again if its name changes. A fourth-order theme is a named group
of third-order themes. **No number is set for you.** The count is whatever the material
carries: enough that each answers a question no member answers alone, few enough that each is a
step up in abstraction and not a rename of its members; say in `notes-C2.md` and the diary what
the count is and why the material carries that many. The contract's §1 and §2 govern the label:
any literature may name a fourth-order theme, the four universal problems' vocabulary included,
under the declaration, and a borrowed or adapted name carries one sentence saying what this
material's version cannot do that the source's can (*task allocation without anyone who can
allocate*); the third-order tier beneath keeps its descriptive names. Every third-order theme
no fourth-order theme picked up is listed at the foot of `fourth.md` with one clause. The `T4-`
line keeps stage C1's fields and gains here `changed`, `mistaken_for`, `in_model` and `pass`;
`fourth/fourth.jsonl` and `dimensions.jsonl` are edited in place with no second version, since
every change is a `tier_history.jsonl` line carrying the old line as `was`. The form-pass
findings enter the structure by their `FP-` ids on the same terms as a third-order theme,
marked as ones whose unit is the turn rather than the topic, never counted.

**Dimensions.** Build one where it gathers at least two fourth-order themes answering a common question, adds an explanatory distinction none answers alone, and can be placed against literature. Each has a construct block and explicit evidence. A theme no dimension gathers carries `"dimension": []` with a reason. Zero or one dimension is a valid finding; do not add dimensions to satisfy a preferred shape. Where several are warranted, distinguish each pair by its members and explanatory question. Record considered alternatives without requiring a runner-up or new dimension.

```json
{"id": "D01", "label": "...", "members": ["T4-003", "T4-011"],
 "construct": {"status": "borrowed|adapted|coined", "source": "...", "changed": "...",
               "mistaken_for": "...", "disconfirm_elsewhere": "...", "gloss": "..."},
 "question": "what this dimension answers that no member answers alone",
 "confidence": "clear|arguable", "pass": 2}
```

**`structure.md`**: per third-order theme, what it is and is not, the repaired borderline
description (from stage C1's disagreements), nearest neighbours and the separating test, what
varies and between what extremes, its gate quoted from `scheme_v2.md`, the three counts summing
to the analysed set from `counts.py` or the sentence that it travels on exemplars (rule 5),
three exemplars through `cite.py`, and, where one of `coder_conflicts.jsonl`'s pairs was placed
here, both coders' words under *read another way* with which reading your count rests on; per
fourth-order theme and dimension, the id, the label and declaration with a one-sentence gloss,
what holds its members together in your words and not as a list, the question it answers, what
falls outside with one near case, the member you were least sure of with both sides, for a
dimension its membership predicate and gate, for a fourth-order theme its material:

```json
{"fourth": "T4-003", "third": "T3-007", "second_order": "<the coder's label>",
 "code_id": "c0113", "sub": "<community>", "author": "<handle as the record carries it>",
 "created_utc": 1491012345, "hour_since_open": 10.1,
 "quote": "the participant's own words, unedited",
 "position": "core|side|between", "nearest_neighbour": "T4-007 or null",
 "why_this_one": "one clause: what it shows that the others do not"}
```

Three to five quotes from two to four second-order themes per fourth-order theme, through
`cite.py --tier 4th --id <T4-id> --n K`, chosen for breadth and depth, the spread stated: where
the good material sits at two edges with nothing between, take two from each and say the middle
was empty; if every quote comes from one room, say so. The same rule governs the third-order
exemplars. **What no fourth-order theme picked up**, one section: how many, of how
many, and the code mass they carry; what they were in general; two or three quotes; whether any
should have been one, and why not. Stage E1 reads it. The data-structure view is generated
(`_views/data-structure`); you do not write it.

**Two more things Part A owes.** The pairs: rule 0's log grouped by `(primary, additional)`,
the supporting concepts, one quote doing both things, whether the pair crosses a dimension
boundary, rooms beside themes (how many rooms produced a second-order theme spanning it, beside
how many themes did; the community count decides, rule 4). This is Part C's raw material. The
onset contrast: your themes and dimensions crossed against the two sides `contrast.md`
declared, with the denominator from `counts.py`; say whether stage A1's expectation held.

Compute every count from `assignments_final.jsonl`; never by hand. State in `notes-C2.md` that
every third-order theme in the assignments is defined and sits in a fourth-order theme's
members or in the unpicked list, every fourth-order theme sits in a dimension's members or
carries `"dimension": []`, every dimension used is defined, and the three counts sum.

**Part A's return**, per pass: third-order themes per fourth-order theme and fourth-order themes
per dimension, with the pairwise separation for the two dimensions you are least sure of; the
construct status of each; the alternative grouping you rejected and why; how many coder
conflicts reached `structure.md`; whether the contrast showed anything; the fourth-order theme
you are least sure of.

## 3. Part B: the concept

Name the one concept, two at the outside, that the literature has no adequate word for: not the
largest theme, the one unaccounted for. Per candidate in `concept.md`: what it is, in a sentence
a stranger could use; the nearest existing concept from recollection, said to be so, and
precisely how this differs; how many communities carry it and how
you counted, with the gate declared before the count (rule 5); three quotes through `cite.py`;
what having it lets you explain that you could not before. Choose, say why not the others, and
keep the rejected candidates in the file. A concept that is a relabelling of something the
literature handles is not a finding, and saying so is an answer: *this study produced a
description* is complete, with what would have had to be different. A candidate that is the
model's whole storyline is Part C's material, not a concept. *Not yet* is an answer on any pass
but the last.

**Part B's return**: the concept in one sentence; the nearest existing concept and the
difference; how many communities; the candidate you came closest to choosing instead; the
literature a reader would say already covers it, and how this differs from it.

## 4. Part C: the model, typed

The model is elements and arrows with ids (SCHEMA-adaptations.md §1): processes `P`, conditions
`K`, claims `C`, roles `R`, arrows `A`. Every element has a statement, the tier and dimension it
belongs to (a third-order theme, a fourth-order theme, a dimension, or a form-pass finding by
its `FP-` id), its range, its evidence (finding ids; concept ids), the leg it entered, and a
status; ids are minted here, kept through stage C5, and keyed on by stage C5's readers and
D2's labelers and verdict fleet; ids are never reused; every change is a
`model/history.jsonl` line with its move, one of Grodal, Anteby and Holm's eight, and the
harness's stamp (the leg, the rooms, second-order themes and tokens read so far, the room and
theme that prompted it). A thing is in the model if the model would say something different
about the concept or one of §1's four things without it. Name what you dropped and which of the
five it failed. **How many elements stand at the top is yours to choose**: as many as keep composition and
explanatory power alive (contract §2), with why in `notes-C2.md`, and as many beneath as the
material carries; if more than a third are named for what they are about rather than
for what they do, you have a lattice.

**Three rooms first.** Before any arrow, `within_case.md`: one ordinary room, one whose form the
scheme could not have predicted, one that stopped early; three to five hundred words each from
the room's concepts, forest and timeline (`mem.py forest`, `after`, `when`), using no theme above
the second tier. Name them in `notes-C2.md` first, with why. When the model exists, read it
against all three; a room the model cannot narrate is a finding.

**How an arrow gets in.** You form it, then you substantiate it, from the pair list and the
pairs crossing a dimension boundary. Evidence in `grounding`: coder-dated order (a dated passage
in the coder's `case.md` (its Chronology section); no v38 verb serves the coder's chronology as
structured entries, so it is read by hand and logged), coder-stated connection, the concepts
read across rooms, the ledger (`after`, `pairs`) as elapsed order and never as cause, whatever
else you devise if you can say what you looked at and what would have disconfirmed it. An arrow
may stand on your reading alone, `"grounding": "reading-alone"`. **Every arrow rests on an
instance a reader can be shown**, since yours come from what participants wrote and the order
they wrote it in: a participant's words through `cite.py` in `support`, or a transition in
`support_transition` (two coded turns in one thread, in order, cited by item and concept, with
the interval, from `mem.py after` or the forest itself). An arrow with neither is `"in_model":
false` whatever its count; stage C5's figure draws no arrow that has
none. **Every arrow is sampled against**: before you set `strength`, go by query to rooms not in
its `subs` where it should hold and could fail (theoretical sampling inside the corpus), and
record them.

```json
{"id": "A03", "from": "P02", "to": "P07", "kind": "order|transition|co-occurrence",
 "grounding": "coder-dated|coder-stated|codes-read|ledger|reading-alone|<yours>",
 "grounding_note": "what you looked at and what you would have accepted as disconfirming",
 "sampled_against": [{"sub": "...", "why_chosen": "...",
 "found": "holds|fails|not testable"}], "strength": "strong|fair|thin", "subs": ["..."],
 "mechanism": "what the one does to the other, in one sentence",
 "mechanism_fails_if": "the observation that would show it did not operate here",
 "mechanism_failure_present": "true|false|not-addressed",
 "negative_check": "tested-absent|counterexample|not-addressed",
 "base_rate_beaten": "true|false|null",
 "early_late": {"early": 7, "late": 2}, "bound": "the condition a counterexample added, or null",
 "in_model": true, "support": [{"sub": "...", "code": "...", "quote": "..."}],
 "support_transition": [{"sub": "...", "thread": "...", "items": ["...", "..."],
 "codes": ["...", "..."], "interval_min": 14}], "gloss": "...",
 "since": "C2-pass-2", "status": "standing"}
```

`mechanism` says what the one thing does to the other, concretely enough to imagine it failing;
`mechanism_fails_if` is written before `strength`, and an arrow without it is not an arrow. An
arrow with a count and no mechanism is a correlation, `"in_model": false`, listed in `model.md`
under *ungrounded relationships*, expected non-empty; stage C5 marks every proposition that
rests wholly on theorised arrows, so list every one here. `negative_check` is never silent.
Where both elements' themes carry *what varies inside it* and a coder wrote the covariation
down, you may draw an arrow between degrees and say so; otherwise say in `model.md` that the
model relates presences and not amounts. **A counterexample requires a reasoned response** (rule 16). Record `counterexample_response`
with the case evidence, alternatives considered and the chosen local adaptation, refinement,
scope condition, uncertainty or withdrawal. A supported scope condition belongs in `bound`.
An isolated exception need not change the shared model; an unsupported universal claim cannot
remain universal. Open or update the finding and retain the original arrow in its history. Two counting traps: a fixed minimum count may filter nothing, because carry counts at
this size clear small overlaps by chance; a co-occurrence count tested against the product of
two carry rates tests presence, not connection, so build the null on the population the arrow
is drawn from, define a connection statement in writing before you count, and let a relation
that holds nearly everywhere stand as constitutive rather than be deleted by its base rate.
**The onset contrast is carried to the arrows.** Test each strong arrow on both sides and
record `early_late`, rule 6 before reading a gap. An arrow holding on one side is a boundary
condition in the model's own terms; on both, a stronger arrow.

**Stating the model.** Every element carries its dimension, so project the arrows onto the
dimensions in `model.md`'s apparatus, from `arrows.jsonl` and `elements.jsonl`: an arrow stated
at the dimension's level carries `mechanism` and `mechanism_fails_if` written at that level and
the strongest instance from beneath it in `support` or `support_transition`; where the
mechanisms beneath will not abstract into one account, report the pair as mass, not as an
arrow. Report per dimension the in-mass, out-mass and internal mass, with and without the
doubles (the second-order themes rule 0 placed on two themes); a dimension with no in-arrows is
a condition, one with no out-arrows is residue, asymmetry is drift. **If you built no
dimensions**, state the model over the elements the concept and §1's four things require, tied
to their fourth-order or third-order themes, and name the rest as unused. Neither route is
preferred.

**`model.md`**: one to two pages of prose, then the apparatus. Two tests before you call it
finished: read it against a room you know is odd and make it say what happened there as one way
of running the same structure; check that every element has a range. Then the elements with
ids, the arrows with their fields, theorised arrows listed apart and the model shown once with
them and once without, the dynamics (loops, what returns a room to a state it had left, what is
irreversible across hour 73). For a within-room loop, one room's dated evidence must run the whole cycle. An inter-room loop may use joint evidence from several rooms, with the claimed level explicit. In both cases use the forest's hours since open on cited items, not incomparable coder day labels. Record every claimed loop in `model/loops.jsonl`; an empty file means no grounded loop. Each row has `id: LNN`, `level: within-room|inter-room`, an ordered closed `arrows` list and one `events` object per arrow with `arrow`, `sub`, `code`, exact `item`, numeric `hour` and `clock: forest-hours-since-open`. Dates run forward. Include `mechanism`, a plausible `alternative` and `why_not_alternative`. Similar codes or a graph cycle alone never establish process feedback. Everything looked for and not grounded goes under
*looked-for-and-not-found*, in the results (rule 8). State which tier the arrows run between,
which third-order themes the model does not use, by name and count, and where the model should
break in its own terms (corpus size and topic are limits on the sample, not boundary
conditions). For your three strongest arrows, write the argument that each is an artefact of
which coders wrote about connections at all, and what in the record separates the two.

## 5. The story, at the end of every pass, read against rooms

A model that has only ever been read against the rooms its arrows were drawn from has not been
read; D2's verdict fleet is the test, and you prepare for it here, pass by pass.

`model/story-pN.md`: one to two pages that say what these rooms did, in the model's terms, as a
stranger could follow it, from a scattered readership to whatever they left behind, with the loops
and the irreversibles across hour 73 in their places, naming every arrow it uses by id in brackets
after the sentence that uses it (*and the call went out [A03]*), so that *no change to the story*
is checked against `arrows.jsonl` and not against the feel of the prose; the stop rule diffs
consecutive stories. Then read whole rooms against it, as many as the story needs (fifteen is a
guide), named in `story_rooms-pN.jsonl`
before any is opened, by a rule written there: the three within-case rooms, every time; every room
`told-with-residue` or `not-told` last pass; rooms whose form the story does not name; rooms from
the contrast side the story has visited least; every `sampled_against` room marked `fails`; one
room from each quartile of `items_in_window`, every time, so the confound that decided v35 is in
every draw; and rooms drawn by seed from the rest. Draw by query (`mem.py rooms`), never by
opening notes, so what a room made does not pick it. A room read against an earlier story counts
again only if the story has changed materially since, the three within-case
rooms excepted. Read each whole, `mem.py room` and its forest, and answer one question per room,
on its line: can the story be told of this room in the room's own terms, and if not what would
have to be added, changed or bounded. `told`, `told-with-residue`, `not-told`, with the residue or
the reason in one clause. The rooms that could not be told and the residues are the next pass's
material: what they need is a recut, an arrow, a bound or a new element, or it is the finding that
the model does not reach that kind of room, which rule 12 makes a boundary at the return (D1 to D3) and not a
weakness. Do not loosen an element until a room fits; say what the room would need and whether the
model should have it. One line per pass in `saturation.jsonl` with the story's number, the rooms,
and the three counts, read as a trend; a rise in `told-with-residue` is a stopping failure. A
story is not improved by reading fewer rooms against it. The story is not the account: stage C5
writes the account from the model that survives, the stories are the loop's record of how the
telling changed, and the last one is the account's first draft.

## 6. One reviewer, once, before the final passes

The adversaries of earlier versions are gone as a system; one instance stays (rule 8), because
a hostile reader found v35's false premise when nobody else did, and its rival partition showed
how under-determined the top tier was. When the pass you expect to keep is written and before
the last passes that would close the loop: one fresh reader, one context.

**Build leg.** Append this stage's entry to `run_manifest.json` (the reader's model, seed,
decoding). Write `RETURN-C2.md`, the one return specification (FLEET.md): the return line, the
end marker, and the line telling the reader to confirm it reached it. Build one packet
(`packets.py files --stage C2 --name C2-reviewer <files>`, which asserts the ceiling and adds the end line), under the 50 KB ceiling,
with `structure.md`, `fourth/fourth.jsonl`, `dimensions.jsonl`, `model.md`, `model/`, the last
story, the criterion paragraph, and the verbs (`mem.py`, `cite.py`) with `room` served
`--no-canvas`; nothing else of yours: no room note, no findings, no prior. Its instruction,
verbatim, copied into `review-C2.md` above its return: *Find errors: a quote that does not show
what it is said to show, a contradiction, a count that cannot be right, a loop no room runs the
whole way round, an arrow whose instance does not show the order claimed. Separately, propose
one partition of the third-order themes into fourth-order themes that meets the criterion you
were given and differs from the analyst's, with what holds each together. A disagreement is
never a verdict: your reading decides nothing.* The return line carries the sha256 of
`model.md` served, each error with its kind (quote, contradiction, count, loop, order), where
and what, and the partition as labelled member lists with what holds each. **Stop here.** Close with `done.sh C2 --cut packets-out`. Your session ends; nothing more of this stage runs on your model until the check leg. The dispatch runs without you, on the platform's reviewer route, each reader in a session of its own. The next launch of stage C2 is the check leg, and its packet tells you one thing: the readers left their files in `_fleet_raw/C2/`.

**Dispatch leg.** Not yours. The dispatch sends the packet to a fresh reader on the platform's reviewer model, collects the
return into `_fleet_raw/C2/`, validates it against `RETURN-C2.md`, reissues if it fails the
schema, and closes. Nothing in it reads your files.

**Check leg.** You are relaunched. Copy the validated return into `review-C2.md`. Answer every
item in `notes-C2.md` under rule 13: an error is fixed and logged; the rival partition is read
for what it shows about how determined your tier is, and answered with a sentence saying why
yours and not it, or with a recut under rule 11. The reader is not a judge; it runs once. A fix
reopens the loop: the stopping rule counts from after it.

**Interview point, mid-stage.** The check leg that reads the reviewer's file writes `out/interview/C2c.md` (under 800 words: what the reader found, what you accept, what you refuse and why, what the final passes will change) and closes with `done.sh C2 --cut interview`. The final passes run in the legs after it.

## Moments to log

Every move by name; the criterion, before pass 1; the three within-case rooms, with why; each
dimension cut with its pairwise separation, and each fourth-order recut with the items it
moved; the concept chosen and the candidates rejected; every arrow added, bounded, demoted or
withdrawn; every `sampled_against` room and what it found; the story rooms drawn, with the rule;
every room read against a story with its verdict; each pass's saturation line; the reviewer's
packet, its items and your answers; the pass chosen and what was discarded; what the structure
showed that your notes did not predict.

## Final message

The claim, the room that best supports it, the room that most threatens it, the condition that
separates them. Then: the pass the model rests on, with Part A's and Part B's returns for that
pass; passes run; rooms read against a story in all and those the last story could not tell, by
name; elements by kind, and how many third-order themes the model does not use; arrows by kind,
theorised apart and the model without them, with mechanism and failure clause and how many were
demoted, bounded and from which rooms, beating their base rate with the connection statement in
one line, carrying a real negative check, resting on a quote against a transition; loops
surviving the one-room test; the three counts per pass as a table, and whether
`told-with-residue` ever rose; what the reviewer found, by kind, and what its partition showed;
what the structure showed that the notes did not predict; the relationship you most expected and
could not ground; the licences exercised (METHOD.md) and those not. A return value.

## Close

`done.sh C2` at the end of every pass, or earlier when you choose, every move logged and snapped
as it was made; paste the close-check's report into
`notes-C2.md`; `handback-C2.md`; the head; the closing diary line.
