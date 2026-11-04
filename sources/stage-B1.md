# Stage B1. Coding: the third-order scheme.

**Model:** as `arm.json` sets for this stage (your platform file lists the model and effort). **Legs:** one per step, and one per stretch of the order in the
steps that walk it. **Fleet:** none. **Be thorough here, beyond what seems enough.** A fleet
places after you, but it places only onto what this stage makes; a kind missed here is missed
for the rest of the run.

**Steps:** `B1a` prior; `B1b-01`, `B1b-02` ... getting lost, one stretch of the order per leg; `B1c` the saturation test; `B1d-01` ... the second pass; `B1e` the scheme standing, the handback and the interview. Each leg is named by its step (STANDING §2).

**Safe stops:** after each room's themes are placed in the working scheme and logged, and after
each stretch. At a safe stop, check for `.pause` (`ls .pause`); if it is there, log where to pick up, your working hypothesis and the next room or item
(`mem.py log "<hypothesis>; next: <item>" --kind pause`), and close with `done.sh B1 --pause` (STANDING §2).

**Startup packet, every leg:** `_head.md`, this file, the last five diary entries,
the output of `mem.py scheme --brief` (the working grouping of
`scheme/scheme_current.jsonl` on one screen; page the file itself only for a theme you are
about to change), `validate.py --open B1`. First leg only: `prior.md`
written before any second-order theme is opened (§1), then `METHOD.md`'s Grodal, Anteby and
Holm paragraph.

**Reads allowed:** second-order themes room by room through `mem.py theme <sub>/<id>` and
`codes --sub`; `pairs --level second`; a room's forest and material on demand, when a theme
cannot be placed without it (`mem.py forest`, `mem.py room`, `mem.py case`), each read logged
with `mem.py log --kind opened --ids <sub>` and why; your notes through `mem.py note`;
`contrast.md`; `running-A1.md`; `lexicon-A1.md`; `dropped.jsonl`; `leads-A1.jsonl`;
`coordinating-rule-A1.md`; `organizing_end-A1.jsonl`; `handback-A1.md`; `mem.py neighbours`; quotes through
`cite.py` only. **Forbidden:** cutting fourth-order themes or dimensions (that is
C1 and C2); citing a note as a source.

**Outputs:** `prior.md`, written first; `scheme/scheme_current.jsonl` (working); `scheme.md`;
`scheme.jsonl`; `families.jsonl`; `confusions.md`; `theme_discovery.jsonl`; `saturation-B1.md`
(steps c and d); `stopping-B1.md` (the stopping rule's report); `kinds-B1.jsonl` (the rule's record, written by
`mem.py`); `pass2-chosen-B1.txt` and `pass2-B1.jsonl` (the second pass's chosen rooms and its record, the second written by `mem.py reread`); `stopping-B1-decision.jsonl` (the PI's, written by `saturation.py decide`, never by
you); `ideas-B1.jsonl`; `episodes-B1.jsonl`; `unplaced-B1.jsonl`; `tier_history.jsonl`
opened, appended to by every stage that recuts; `findings.jsonl` opened with
the scheme's claim in rule 14's form; `notes-B1.md`.

`scheme.md` is not frozen here. Stage B2 tightens it against fresh readers and freezes it.

## 1. `prior.md` first

From `PRIOR-template.md`, every section filled and dated before the first second-order theme is
opened: what you expect the scheme to hold, from the reading, and the two or three kinds the
material will refuse; the expectations about the model; the
composition criteria; the brackets from the canvas events; the coordinating-turn rule copied from
`coordinating-rule-A1.md`; the onset contrast; the exemplar rule (§3). Sections 7 and 8 (the distance weights, the
concept floor and the off-platform threshold) stay empty here: they are written at D1, before
any adaptation is seen. The harness seals what you write; a change after that is a departure
(rule 10), and a change to the coordinating-turn rule is reported with the figures under both
rules. Stage C3 reads it against the structure. Do not edit it after the first theme is opened.

## 2. The steps

You hold the run's notes, not its memory: stage A1 was read by another model, and what reached
you is the notes, the running file, the leads, the head and the diary. What you read here is every second-order
theme of the analysed set, about 8,500 of them in the frame, each with its `theme_note` and the concepts
beneath it, and they do not fit one context. So the stage walks in steps, and every step ends a
leg.

**B1a, the prior.** `prior.md` (§1), then the order. **The order is random, and not yours:**
`mem.py next --stage B1` draws it from a seed no one chooses (the sha256 of the store's
`rooms.jsonl`, tag B1, frozen in `out/seed.txt` at the first draw). A random order is what makes the stopping
rule's estimates mean something, and it keeps related rooms from being read one after another,
so that one room's account does not prime the next. Say in `notes-B1.md` what you expect of it.

**B1b-01, B1b-02 ... getting lost.** One stretch of the order per leg: about 1 MB of the rooms' second-order
themes and their concepts (`mem.py room <sub> --size`: codes plus second-order themes, not the forest), several rooms (1 MB, J 2026-10-07; 3 MB before, v42, J 2026-10-03), the stretch (first and last `order`) declared in the diary
when the leg opens. **The next room is always `mem.py next --stage B1`**, at the start of every
leg and after every compaction: it follows the order and the stopping rule below. A room is done when every one of its second-order themes is placed in
`scheme_current.jsonl`, or listed in `unplaced-B1.jsonl` (`{"sub", "second_order", "why"}`) when it
cannot be placed at all; a theme that stands alone is placed on the rare tier, not left out. The
close-check refuses a room read out of the rule's turn, and at the last leg a walk that has
neither reached the order's end nor stopped by the PI's decision. For each room: its second-order themes and their concepts, grouped as you go
into third-order themes; for any room whose themes you cannot place with confidence, and any
room your A1 note marks as unsettled or unsure, the forest and the case as well (`mem.py forest`, `mem.py case`),
logged with why. Read the room on its own first. Then read it against the rooms it is tied to
that you have already read (`mem.py neighbours`, `mem.py compare`, and any line of
`leads-A1.jsonl` that names it).

**One episode seen twice.** Where two rooms tell one episode, it is one episode, not two
instances. The test is the record, not the likeness of the accounts: the two rooms' concepts
cite the same thread, or they tell the same artwork in the same hours. Record it in
`episodes-B1.jsonl`, one line per episode:

```json
{"episode": "E001", "rooms": ["hatsune", "vocaloid"], "same": "thread|artwork",
 "evidence": "the thread id, or the artwork and the hours", "themes": ["T3-014"],
 "why": "both rooms tell the deal with r/placestart over one drawing, hours 30 to 34"}
```

The episode is corroborated: two rooms that could not compare notes tell it, and that makes the
account of it stronger. For the floor (below) it still counts as one room. Where the two rooms'
accounts disagree, say where in `why`, and place each room's second-order theme on what its own
words show. Two episodes alike in shape but on different threads or artworks are two instances.

**When to stop (the PI's rule, 2026-09-29).** An earlier run stopped after 127 rooms with both
curves still climbing, and the tier it froze collapsed; this one stops only by a rule, and goes past
its own first stop. `python3 tools/saturation.py status --stage B1` replays it from the
files at any time, and `mem.py next --stage B1` follows it; you never count by hand.
What it counts is `kinds-B1.jsonl`, which `mem.py mint` and `place` append with the room you are
reading, which says when a theme is new, and the room whose second-order theme was placed, where
the estimates count it (a theme placed into an earlier room counts in that room); a merge or a split, logged with `mem.py log --kind merged|split --ids <T3 ids>`, is a new
theme there too (J, 2026-09-29). The file is never rewritten, so a later regrouping leaves the
rule's past as you read it; a theme placed without `mint` or `place` is a defect.

- Material is counted in words, in average rooms (the analysed set's mean). No estimate is made
  before 50 average rooms, and 25 rooms, are read. While a new third-order theme has come in the
  last 10 average rooms (and the last 10 rooms), you read on down the list.
- After 10 without one, a round begins: the estimate from what you have read (Chao et al. 2014;
  the formulas are in the tool) predicts how far the next new theme is, and you read that far,
  never more than you have already read, and never more than 25 average rooms. A new theme inside a
  round resets everything, and so does a new theme in the draw (J, 2026-09-29).
- Three empty rounds in a row are **marker 1**, the first stop. Three more are
  **marker 2**. Then **the draw**: rooms taken at random from those not yet read, as many words
  as the three rounds between the markers; `mem.py next` names them. The draw read is **marker 3**.
- A round predicted longer than 10 average rooms is logged when it begins (`mem.py log --kind note
  "round <n>: <rooms>"`).
- At marker 3, write the report, `python3 tools/saturation.py report --stage B1` (it writes
  `stopping-B1.md`: rooms read, share of the words, rooms left, words left in average rooms, the
  three markers, every round, when each theme first came, and what the draw rules out), log it,
  and close with `done.sh B1 --pause`. The PI decides: finish the list, or stop. The decision is
  logged with `python3 tools/saturation.py decide --stage B1 finish|stop --why "<the PI's words>"`;
  `mem.py next` then follows it.
- **The check-in.** If 60% of the words are read before marker 3, write the same report, log it and
  close with `done.sh B1 --pause`: the PI decides to continue under the rule, finish the list or stop
  (`saturation.py decide --stage B1 continue|finish|stop --why "..."`).
- If the list ends before marker 3, every room has been read, and the report says so.
- **What the numbers are.** The thresholds (10 average rooms, rounds of at most 25, three empty
  rounds to a marker, the check-in at 60%) are this design's discovery heuristic, the PI's recorded
  choice (J, 2026-09-29). The literature gives the rule its form, a run with nothing new after a
  base; it does not fix the numbers. `stopping-B1.md` says so, and so does the write-up.

Log a prospective theme when you first think of it, before it is minted: `mem.py idea "<label>"
--trigger <sub>:<tNN>`; the idea log is stamped as the mints are, and the report sets the two
curves side by side. The mints drive the rule.

**B1c, the saturation test.** When the walk has stopped (the list's end, or the PI's decision
after marker 3), draw a seeded sample of the rooms read (the seed and the rule in `notes-B1.md`),
and read them again at the concept level, fresh, holding
only `scheme --brief` and the gates. Count what does not fit: a concept or theme that needs a
new kind, a split, or a gate that fails. Report it in `saturation-B1.md` with new kinds per
hundred second-order themes read in the first pass (from `theme_discovery.jsonl`, by room) beside it.

**B1d-01, B1d-02 ... the second pass, at twice the depth.** Read again, concepts and forests,
the rooms the test found not fitting, the rooms with the most hesitations in your log, and the
contrary rooms of `contrast.md`. Before the first, write them to `out/pass2-chosen-B1.txt`, one room
a line; add to it as you find more, never take one off. Read them in the order (`python3
tools/saturation.py order --stage B1` prints it), one stretch per leg, and when a room is read
whole, record it: `mem.py reread <sub>`. **Stop only when both hold** (J, 2026-10-07):
every chosen room has been read, and the rooms read since this pass's last new third-order theme
are at least as many as the first pass's empty run at marker 1, counted both in average rooms and
in rooms, and never fewer than thirty rooms. Marker 1's empty run runs from the first pass's last new
kind to marker 1; if the first pass never reached marker 1, the run is thirty rooms and thirty average
rooms. The first pass gives the run its length, the literature its form: a run with nothing new after
a base (Francis et al. 2010; Guest, Namey and Chen 2020). If the chosen rooms are read and the run is
short, go on down the seeded order with rooms this pass has not read. There is no ceiling; the PI
sets one if he wants one. `python3 tools/saturation.py pass2 --stage B1` (and `mem.py reread`) says
where the run stands and which room is next; you never count by hand. Record each stretch's new
kinds in `saturation-B1.md` as you go. A count still climbing when every room is read is a finding
about the material, written down, not a reason to have stopped, and not a reason to stop. (Before
2026-10-07: thirty rooms in a row; before that, two stretches of at least twenty rooms each.)

**B1e, the scheme standing.** `scheme.md`, `scheme.jsonl`, `families.jsonl`, `confusions.md`
(§3 to §5), the hand-over (§7), the handback, and the interview.

`theme_discovery.jsonl` (§6) is the saturation record of the first pass; `saturation-B1.md`
holds the test and the second pass.

**`scheme/scheme_current.jsonl` is the grouping on disk**, one line per theme as it stands,
`{"theme": "T3-007", "label": "...", "members": [{"sub": "...", "second_order": "...", "codes":
["c0013"]}]}`, rewritten at every room boundary. Three verbs write it for you, atomically, and
log what they did: `mem.py mint` adds a new theme with its trigger as first member, `mem.py
place <sub>:<tNN> --theme T3-NNN --codes c1,c2` puts a second-order theme in with the concepts
that carry it, `mem.py unplace <sub>:<tNN> [--theme T3-NNN]` takes it out. **A theme has a gate
from the moment it is minted** (J, 2026-10-11): `mint --gate "..."` writes a provisional gate, what
a second-order theme must show to be placed there; `mem.py gate T3-NNN --field provisional_gate
--now "..." --reason "..."` revises it at each relabel, and each revision owes rechecks of the
members it could move (`mem.py rechecks --owed`, `mem.py recheck`), so placement never runs ahead
of the gate it rests on. Edit it only through these verbs: the stopping rule counts what
they record in `kinds-B1.jsonl`, and a placement made by hand is a defect. With
`theme_discovery.jsonl` it is what you read, through `scheme --brief`, at every leg start and after any compaction, before the next room, so that the
grouping in your head and on disk are one; a theme the file does not hold does not exist. It is a working file (rule 18): it ships to nobody, and the fleet at B3 places from
the gates, not from your grouping.

**This is Gioia's first-order analysis consolidated across cases, and it has that freedom.**
Their account is the instruction: adhere faithfully to the material's terms; make little
attempt to distill, so that the number explodes on the front end; get lost before you get
found; then seek similarities and differences among the many categories until the germane kinds
stand, labelled in the material's words. The hands at stage B3 remove one head's limit, so the count is set by the
material's kinds and by what is germane to the two questions, and by nothing else.

Build **third-order themes**: cross-case, near the material, in your words and not the coders'.
You decide how many; say why that number and not half or double it. **No ceiling**: earlier
versions capped the tier near forty, and a compression here cannot be recovered from below,
because everything after it is placed under the frozen scheme. Two things set the count, and neither is a number:

- **Kinds, not sizes.** Two second-order themes from different rooms are one third-order theme
  when they are the same doing; two whose `theme_note`s a stranger would tell apart are not one
  unless you can say what makes them one. A theme that holds many because many rooms did the
  same thing stays one and carries its variation; a theme is never
  split by degree.
- **The asymmetry.** Merging later is arithmetic, the placements on either become placements
  on one and nothing is re-read; splitting later is a re-read of every second-order theme the
  theme held (rule 10). When in doubt, keep two. The order of magnitude that follows is hundreds, not
  tens; say what yours came to and why, and report the size distribution (second-order themes
  per theme). A theme holding more than one second-order theme in ten is read again for the
  kinds inside it, and is either split or has its internal variation written out.

**Do not cut fourth-order themes or dimensions.** That is C1 and C2: Gioia, Corley and
Hamilton's reduction to twenty-five or thirty came from theorizing while consolidating, which is
how the story compresses the kinds; this instrument departs from that on purpose, and stage E1
reports it. The tier saturates in kinds while
second-order themes keep coming.

Three things to state before any theme exists: `prior.md`; **the floor**; and **the gate block**,
one paragraph per theme stating what a community must have had for the theme to be available to
it (rule 5). **The floor is two rooms unlike each other** (in size, in side of the contrast, or in form as
your notes have it): a kind seen in two such rooms enters the main scheme. Each main theme in
`scheme.jsonl` names them: `"floor": {"rooms": ["<sub>", "<sub>"], "unlike": "size" | "side" |
"form", "why": "one clause"}`; unlike in size means one room holds at least twice the other's
items in the window, and the check reads that from the store. Two rooms that
tell one episode (`episodes-B1.jsonl`) count as one room here. Do not raise the floor; the v35
analyst's floor of five rooms capped its tier near fifty. A kind seen in one room only goes to the
rare tier,
which ships in `scheme.jsonl` with every field a theme has and `"tier": "rare"`, so that the
fleet can place onto it and its count is measured rather than guessed; a rare theme is never
folded into a neighbour to keep the count down.

**Every grouping move is logged with its name** (`mem.py log --kind merged|split|dropped
--ids ...`) and, when it touches an existing theme, a `tier_history.jsonl` line with its `move`. The gates at §3 are the asking-questions move; write the question you
asked into the gate.

The notes are your prior, not a source. Nothing in the scheme cites one, and `notes-B1.md` says
what the second-order themes showed that the notes did not predict.

## 3. `scheme.md`, per third-order theme

The scheme goes to strangers holding fifty second-order themes and one family's tests, and
nothing else; refer to nothing they have not been given. Every field is a test, not a
description, and every token is paid once per reader.

- **An id, `T3-001` on.** Every later stage keys on it.
- **A name, 2 to 5 words, near the material**, gerund-led where the material allows, never a construct's name, never one of the four problems:
  this tier stays descriptive through every recut (the contract's §1).
- **A gloss**, one sentence carrying what the name does not.
- **The gate**, the field the fleet runs on, as conditions: `must_show`, `must_not_show`,
  `decide_when_both` (rule 0's tiebreak; the awkward cases show both), written so that a reader
  who still needs a second placement can state its `why_not_one` in terms of what the single
  placement fails to carry. A stranger holding this and nothing else places the same theme you
  would.
- **Discriminators**: for each near neighbour, the question that separates them, answerable
  from the second-order theme in front of the reader, written from both sides.
- **What varies inside it, and between what extremes.**
- **What it is not**: one boundary case that looks like it and is not.
- **A family.** At hundreds of themes no reader holds every gate at once, so the scheme carries
  an index: every theme belongs to one family, a group a reader would confuse, named for what
  its members are about in the material's words. A family is an index and nothing else: not a
  tier, not a construct, never named after one of the four problems or any construct, and
  nothing downstream counts, clusters or reasons on it. The index page lists every family with
  its themes' names and glosses; `scheme.md` is organised by family.
- **`gate_parts`** where the gate names a two-part move, with a pair that satisfies it while
  neither half does (contract §2).
- **Three exemplars**, participants' words through `cite.py --room <sub> --code <id>`, each
  satisfying the gate on the quote alone (rule 3). Where several quotes pass the gate, choose by
  the rule you wrote in `prior.md` (`exemplar rule:`) before the first theme was opened; the
  default is the line that meets the gate most directly. Name the passing quotes you did not
  choose in the exemplar's `rivals` (their code ids), so a reader can check the choice. The close-check resolves every exemplar
  through `cite.py --resolve` and rejects one that resolves to a coder's note or a label. Whether a reader sees exemplars is a declared condition of
  stage B3; by default they do not ship.

No counts; the counts are computed from `assignments_final.jsonl` once stage C1 has written it.

## 4. `scheme.jsonl` and `families.jsonl`

One line per theme, the file that ships to the fleet and that every validator resolves ids
against; the prose file stays authoritative for a human. `families.jsonl` beside it, one
line per family: `{"family": "G03", "name": "...", "themes": ["T3-007", "T3-011"]}`. The harness
assembles the fleet's index page and per-family files from these two (`packets.py`, FLEET.md).

```json
{"id": "T3-007", "name": "...", "gloss": "...", "family": "G03", "tier": "main|rare",
 "must_show": "...", "must_not_show": "...", "decide_when_both": "...",
 "discriminators": [{"vs": "T3-011", "question": "..."}],
 "varies": "...", "is_not": "...", "gate_parts": null,
 "exemplars": [{"sub": "...", "quote": "...", "code_id": "...", "rivals": ["c0412"]}]}
```

## 5. `confusions.md`

The pairs you expect to be confused, ranked, with what the confusion will look like; for each,
the second-order theme you would put in front of a fresh reader to expose it; your estimate of
the disagreement rate on the hardest pair. Stage B2 scores it.

## 6. Two records

Record; do not compute.

**`theme_discovery.jsonl`**: one line the first time a third-order theme exists, written as it
happens by `mem.py mint --label "..." --trigger <sub>:<theme_id> --gate "..." --codes c1,c2`, stamped by the harness,
never edited: `{"theme": "T3-007", "label": "...", "t": "<ISO>", "leg": "...",
"sub": "...", "trigger": "<sub>:<theme_id>", "rooms_read": 37, "themes_read": 521, "codes_read":
3902, "tokens_read": ...}`. New kinds per hundred second-order themes read is computed from
these lines and nothing else.

**`tier_history.jsonl`**: one line per event over every tier you own, from here to D5 and for
every amendment after C5 (rule 11): `{"t": "<ISO>", "stage": "B1", "leg": "...", "tier":
"third", "id": "T3-003", "move": "splitting", "event": "split", "was": {"label": "...",
"members": [...]}, "now": [{"id": "T3-003", "members": [...]}, {"id": "T3-041", "members":
[...]}], "prompted_by": "what made you look: a room, a theme, a check, a reader, a paper",
"why": "one clause: what the tier after the move carries that it did not before"}`. `event` is one of `created`, `relabelled`, `split`, `merged`, `retired`, `members_changed`,
`rescoped`, `moved_to_rare`; `move` is one of Grodal, Anteby and Holm's eight. A `split`, a
`merged`, a `retired`, a `rescoped` and a `moved_to_rare` line carries `prompted_by` (the check
refuses one without it): a consequential move is recorded as what prompted it, the move, what
changed (`was` and `now`) and why the new state explains the material better (Günther, Joshi and
Constantinides 2026, METHOD.md); where you weighed another move and set it aside, name it in
`why`. An id is never
reused.

## 7. Before you hand over

For each theme, the strongest argument that it is two or half of another. The stranger test:
read only the gates and discriminators of three themes and place five second-order themes you
have not looked at recently; report where you hesitated. Keep the ten biggest bags (second-order
themes ranked by the concepts under them) in `notes-B1.md`; stage B3 flags them so readers place
them from the concepts. Say which running-file entries you dropped and why. Write
the token size of `scheme.md` and of the index page into `notes-B1.md`, with what you cut to get
there.

## Moments to log

A room opened; a theme minted (through `mint`, which logs); every merge, split, drop and
relabel; a question opened (`_questions/<slug>.md`); a room boundary, with the rewrite of
`scheme_current.jsonl`; an episode seen twice; a stretch's end, with its new kinds; the
saturation test's count; the second pass's stop, with its run since the last new theme against its target (`saturation.py pass2`).

## Final message

The claim the scheme makes about what these rooms did, the room that best supports it, the room
that most threatens it, and the condition that separates them. Then: themes and rare
themes; that `prior.md` came first; the order and that every room was walked; new kinds per
hundred, first hundred against last; the saturation test's count; the stretches of the second
pass and the two that added nothing; the episodes seen twice; the two rooms that admitted the last theme; themes rejected
and why, from `notes-B1.md`; the ranked confusions; families and the largest; the size
distribution, the largest theme and what you did with it; the token sizes from `notes-B1.md`; the one second-order theme the scheme handles badly; which of
the four licences in `METHOD.md` you exercised and which not (rule 17).

## Close

`done.sh B1` at the end of every leg; a merge or split of a theme already holding more than twenty
members is logged with `mem.py log --kind move` and snapped with `python3 tools/snap.py B1
move-<move>-<n>` when it is made; and `B1e` closes at the interview point below, so the third-order tier as it stood before any
reader tested it can be reopened and asked why. The close-check resolves every exemplar and every id; paste its report into
`notes-B1.md`. At the last: `handback-B1.md`; the head updated; the closing diary line.

**Interview point.** `B1e` writes `out/interview/B1e.md` (under 800 words: what you did, what you found, what surprised you, what you doubt, and the three questions you would most like to be asked) and closes with `done.sh B1 --cut interview`: the third-order tier standing, before any reader tests it: the kinds you made, the ones you nearly made, what you are unsure of. The principal investigator may talk with you here, in a fork of this leg, run in a copy of your folder as it stood at the close (not read-only; nothing done there reaches the run); the run goes on from the cut either way. `done.sh` files the brief under the leg, the stage, the step and the minute, and refuses the cut without the brief (and, at a stage's end, without the handback).
