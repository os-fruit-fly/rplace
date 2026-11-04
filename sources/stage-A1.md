# Stage A1. The reading.

**Model:** as `arm.json` sets for this stage (your platform file lists the model and effort). **Legs:** one per declared room block, plus a first leg for the checks, the screen and what
is written before you read. A block is a set of rooms whose material sums to about 3 MB (v42; 0.6 MB before, J 2026-10-03)
(`python3 tools/mem.py room <sub> --size` gives a room's bytes); a large room may be a block of
its own. A block this size compacts several times in a leg; that is routine, and the room
notes on disk are why it costs nothing (STANDING, Compaction). The blocks are declared in `notes-A1.md` before the first is opened. **Fleet:** none. The note is your prior, and a prosthesis would write
someone else's.

**Steps:** `A1a` checks and screen (and the blocks declared); `A1b-01`, `A1b-02` ... one per reading block; `A1c` the lexicon and the analysed set, and the handback (an interview point). Each leg is named by its step (STANDING §2).

**Safe stops:** after each room note is written and logged. At a safe stop, check for `.pause` (`ls .pause`); if it is there, log where to pick up, your working hypothesis and the next room or item
(`mem.py log "<hypothesis>; next: <item>" --kind pause`), and close with `done.sh A1 --pause` (STANDING §2).

**Startup packet, every leg:** `_head.md` (empty at the first leg; you write it at the close of
the first), this file, the last five diary entries, `validate.py --open A1`. First leg only:
`HOW-TO-RUN.md`, `package/store/README-store.md`, `METHOD.md`, whole.

**Reads allowed:** everything in the package and the store through the verbs; the canvas fields
in every room (rule 7); `canvas/artworks.jsonl` beside each room's account. **Forbidden:** nothing yet exists that is.

**Outputs:** `rooms/<sub>.md` one per room of the analysed set; `lexicon-A1.md`; `running-A1.md`;
`contrast.md`; `dropped.jsonl` (written even when empty); `notes-A1.md`; `coordinating-rule-A1.md`;
`organizing_end-A1.jsonl`; `order-A1.txt`; `leads-A1.jsonl` (written even when empty);
`departures.jsonl` and `defects.jsonl` opened, empty or not;
`run_manifest.json`;
`handback-A1.md`; `_head.md`, written for the first time at the first close. **No scheme is
written in this stage.**

## 1. The first leg: the tools and the package

Run `python3 tools/mem.py help`, then every read verb once with `--stage A1` (`mint`, `idea`,
`place`, `unplace` and `adjudicate` belong to later stages and refuse here, as they should), and one call of
`cite.py`; the logs are `_mem_reads-A1.jsonl` and `_cite_reads-A1.jsonl` (rule 1). A call that
fails is a defect in the package: write it to `defects.jsonl` and say so in your final message.
Run `validate.py --self-test` once and paste its report into `notes-A1.md`: it plants a known
defect for every close-check it has, stage by stage, and shows each firing once; a check that
does not fire is a defect, and a stage whose close-check the report does not list has no
close-check, which you will know before you reach it. The harness snaps `out/` at every close; you call `snap.py` yourself only when an order matters.

Check the package before you trust it; every result into `notes-A1.md`, every failure a
`defects.jsonl` line. `python3 tools/mem.py audit` serves the raw fields these checks need (the
census count, the six files of every room, the retracted concepts, the store's build figures),
each figure with its file, and its call is logged like any read (v43); for anything it does not
serve, a saved script in `out/_analysis/` that prints each input's path, size and sha256 beside
its counts, logged as a departure:

- **The census.** `package/FRAME.md` names the copy date, the count and the hash; reconcile the
  count against `rooms.jsonl`, the room folders under `package/`, and the distinct rooms in
  `codes.jsonl` and `themes.jsonl`. Report N.
- **One run per room.** Every room folder under `package/` holds the same six files
  (`brief.md`, `case.md`, `codes.jsonl`, `themes.jsonl`, `threads.jsonl`, `pointers.jsonl`) and a
  forest in `trees/`; a room that does not is a defect.
- **The canvas, present and whole.** The six canvas fields (`canvas_entries`, `canvas_area_px`,
  `canvas_centre`, `canvas_ring`, `canvas_artwork`, `canvas_source`) on every room of the
  census in `rooms.jsonl`; `canvas/artworks.jsonl` readable, with its index and its placement
  over time. Report the distribution of `canvas_area_px` and of the share of each room's own
  artwork placed by the people who wrote in it; the contract's §5 says what that share
  measures. A room in the census with no canvas line is a defect.
- **The clocks.** `onset_first_code_hour`, `onset_last_code_hour`, `items_in_window`: null
  counts, rooms named. The two clocks of ending: `onset_last_code_hour` against the last
  `last_hour` over the room's threads in `threads.jsonl`; report how many rooms have each null.
- **Off the record.** `n_off_platform` in `rooms.jsonl` (off-platform pointers the coder
  recorded): its distribution over the census, and the rooms with the most named; every verdict
  at the return (D1 to D3) carries it.
- **The nulls.** The rooms whose concentration fields (`coded_authors`, `top1_share`,
  `herfindahl`) are null, named; carry that denominator with any claim resting on
  concentration.
- **The instrument's shape, recomputed.** Log-log slopes of first-order concepts and of
  second-order themes against `items_in_window`, over the census, as you find them; there is
  no target figure. Report beside them the second-order theme count against `items_in_window` and against
  the concept count, raw, log and rank, all six. Then the share of each room's concepts
  reachable from a second-order theme (a concept with a `theme_id`), against items; declare the
  room size above which the share falls below the median of the smallest quartile. Write it to
  `notes-A1.md` as `concept_reach_threshold`; the contract's §5 says what it does at C2 to D3.
- **The concepts and the themes.** The sum of per-room concept counts in `rooms.jsonl` against
  the lines of `codes.jsonl`, and against the coder's own count (`n_codes_coder` less the
  retractions); second-order themes in total, rooms with none, rooms with one or two.
- **Retracted concepts** are absent from the store; the count dropped at build is in
  `README-store.md`; confirm it against `_retracted.jsonl` and against the coder's
  `codes.jsonl` in each room folder.
- **The store against the package.** `counts.py` first: its concept, second-order theme and
  coded-room totals against the collections, exactly. Then the store's own build figures in
  `README-store.md` recomputed: the count of concepts whose item the record does not hold
  (`_unjoined.jsonl` against `codes.jsonl` and `items.jsonl`), the retracted count, and the
  forest header totals over `trees/`; say whether they agree. What you compute wins; carry both
  to stage E1.
- **The analysed set is null until `dropped.jsonl` exists.** Re-run `counts.py` after the
  screen and report the count of second-order themes to be placed at B3. If you dropped
  anything, the count must fall by exactly what the dropped rooms carried.

## 2. The screen

Contract §5: a room that wrote nothing about the event is a negative screen on the frame, not a
case at zero; a room that tried and failed is a case. Read the rooms whose coder coded one thread or none
(`threads_coded` in `rooms.jsonl`), any room whose first coded turn falls after hour 73
(`onset_first_code_hour`; the census admits only rooms that wrote about the event while the canvas
was open, v43, so such a room is a defect of the frame as well as a screen), and any room the coder's own documents (`case.md`, `threads.jsonl`)
give you reason to doubt: account, notes and forest for each. Every drop to `dropped.jsonl` as
`{"sub": "...", "why": "..."}`, and `why` says what the analysed set loses with the room, not
only what the room lacks (a screen is a move on the frame, and the frame is where the
population patterns come from: contract §1, two kinds of claim); a room kept against a doubt
gets a line in `notes-A1.md` saying what the doubt was. If you drop nothing the file is written empty. From here on the
census is two numbers, and `counts.py` is re-run.

## 3. Written before you read

Into `notes-A1.md`: the blocks, each a list of rooms with its summed bytes, the order and why; three sentences on what you expect the material to
show. Into `order-A1.txt`: the same order as a file the tools read, one line per room of the
analysed set, `<block><TAB><sub>` (`01	denmark`), every room once. It is the order: `mem.py next`
names the first room in it with no note, the compaction hook prints that room, and the close-check
fails a block that leaves a room behind. A run before this one carried its order as a list in its
head, lost rooms from that list across compactions without knowing, and found them only
when the reading was over. Into `contrast.md`: the onset contrast (contract §5) on `onset_first_code_hour`, with the
rule that defines each side, the named members, the size of each, and what you expect to
differ. Stage C2 puts it to the model's arrows, and stage E1 reports what it showed.

## 4. The reading, block by block

Read every room of the analysed set whole, in the declared order, through its forest: `mem.py
room --no-canvas`, `forest`, `when`, then the concepts with their words (`codes --sub`, and
`cite.py --room` for the passages), then `case.md` and the brief, and
`mem.py room` with its canvas fields last, for the `made` line, read against the room's
placement in `canvas/artworks.jsonl`. **Write the room's note before you open the next room**,
and log it (`mem.py log --kind opened --ids <sub>`, then `mem.py log "noted" --kind note --ids <sub>`
when the note is written, naming that one room). The harness refuses a note whose room's
concepts were not read, and checks the note's form the moment it is written.
**The next room is always `mem.py next`**, at the start of every leg and after every compaction;
never a room you remember as next, and never one from the summary of a compacted context. **Read
the room's concepts before its account.** The close-check requires, for every note, a logged
`mem.py codes --sub <sub>` or `cite.py --room <sub>` call for that room made before its `note`
line: a run before this one wrote its notes from the coders' accounts and inherited their leaps.
A block closes with `done.sh A1`; the next leg starts from the head. The note is what survives;
a room you read and did not write about is a room you have not read. If compaction happens
inside a block, the harness names the head and this file and refuses every other call until you
have read them and the diary, and you resume at a room
boundary from `_head.md` and `mem.py note`: the notes, the lexicon, the running file and your
`_` files are the carrier, and nothing that is not in them survives. No fleet reads for you
here.

**`rooms/<sub>.md`, one fixed form, dated; about 350 words is a guide, not a limit:** the note is yours, for your own later reading, so write what you need; the fixed lines and their checks stand, the length and the wording are your judgement, and you may ask J. Short notes link and read sideways better than long ones (J, 7 October 2026).

```
# r/<sub>  (read <ISO>)   coded share <n>   off-platform pointers <n>
doing:      what these people were doing, in their words (no quotes; concept ids in brackets)
week:       what changed across the 97 hours, by hour
named:      who they named, and what for
goal:       what they were trying to make or hold, when that became settled, and whether it changed
unsettled:  what the room could not settle
coder unsure: what the coder said she could not place or resolve (in case.md), with thread
            ids; or none
carrying:   three concepts that carry the room (ids only)
not this:   one thing a reader would assume about this room that the record does not show
ended:      last observed coordination hour in the forest, its evidential limit, and what is observed after
struck by:  the phrase or moment that struck you, in the room's words; free, and never cited as evidence
made:       what was on the canvas at the freeze, from the fields, against the room's own account;
            written last
```

The ten lines other than `struck by:` are fixed; `struck by:` is the one free line, a trace of
your reading and not a finding, so no stage cites it. The header figures come from `rooms.jsonl` (`item_coded_share`, `n_off_platform`); a null is
written as null. Write `made` last: the note is what the room did, and what it kept is read beside that
(rule 7); when the canvas changed what you looked for in the room, the note says so. A later stage that re-reads the room appends
one dated `later:` line below `made`, one clause of your own on what you make of the room,
amended and never deleted, so that the note carries your judgement of the room and not only
its facts.

`lexicon-A1.md`: the rooms' own words, one per line with the room and the item id of first use,
facts only. `running-A1.md`: what you keep seeing, unpruned and unordered, one entry per line
with the room it came from; a few hundred entries out of the first block is the right order of
magnitude. Both are appended at every block and never rewritten.

**Leads.** When a room makes you suspect a tie to another room (the same drawing, the same fight,
a treaty one side names), and you have not checked the other room, append one line to
`leads-A1.jsonl` at once: `{"sub": "hatsune", "other": "vocaloid", "why": "names r/Vocaloid as the
party that struck the deal; same line about being eaten", "item": "<item id>"}`. A suspicion held in
context does not survive a compaction; a line does. Stage B1 reads them when it meets those rooms; no stage resolves them for you.

**The notes are a prior** (STANDING-INSTRUCTIONS §1), never a source for a quote, and **they
are queried, never read as a list.** `mem.py note <sub>` serves one; `mem.py notes --grep <words>`
serves a query over them.

## 5. The coordinating-turn rule, and the hour organizing ended

After the last block, in that block's leg and before its close, write `coordinating-rule-A1.md`:
the rule that says which first-order concepts count as a coordinating turn (a call, an
assignment, a plan, a report of placement, a defence, an alliance, a correction of another's
placement) and which do not (recounting, joking, mourning), in the lexicon's words, with ten
concept ids on each side as examples. Stage B1 copies it into `prior.md` §5. It may be amended
later only by a logged departure (a `departures.jsonl` line and a diary line through `mem.py log`) that
says what changed and why, and every figure computed under it is then reported twice, under the
rule before and after the change.

Under that rule, and from the forest and never from the canvas, write `organizing_end-A1.jsonl`,
one line per room of the analysed set: `{"sub": "...", "organizing_end_hour": <the hour of the
last coordinating turn>, "aftermath_share": <coded turns after hour 73 that coordinate rather
than recount, over coded turns after hour 73>, "coordinating_turns": <n>, "turns_after_73":
<n>, "work_remained": "kept" | "lost" | "silent", "work_remained_codes": [<concept ids>]}`, with
the `ended` line of each note reconciled to it and a disagreement logged. Two more fields make
the figures checkable: `"last_coordinating_code"` (the concept id of the last coordinating turn,
null with the hour) and `"aftermath_coordinating_codes"` (the concept ids after hour 73 that
coordinate). `work_remained` is what
the room's own record says became of its work: `kept` or `lost` when its last word on the matter
says so, cited by the concepts that say it; `silent` when the record never says, with no ids.
Silence marks an unknown outcome in this public record. It does not establish that organizing
stopped, especially where activity moved off platform. The
close check recomputes the hour, the turns after hour 73 (distinct coded items) and the share
from the store's hours and those ids; a difference is an error, so the figure stage D5 reports
per branch (contract §1) is the store's.

## 6. `run_manifest.json` and `notes-A1.md`

```json
{"stage": "A1", "written_utc": "...", "package_sha256": "...", "tools_commit": "...",
 "model": "<id of the model running this stage>", "decoding": {"temperature": 0.0, "top_p": 1.0},
 "seeds": {}, "n_agents": null, "notes": "..."}
```

Written here with the package hash (from `package/FRAME.md`) and the tools commit. Stages B2,
B3, B4, C2 (its one reviewer), C5 (its three readers) and D2 (the labelers and the verdict
fleet) append an entry with their seed, agent count, model and decoding, and stage E1 writes the
last line and reports the whole file; a figure whose manifest cannot name its model has not
been reported.

`notes-A1.md` at the end: the order, the contrast and the three sentences, written first; every
check in §1 with its result; what you read, from the logs and not from memory; what this
material is, under 400 words; three things you expected to find and did not; the one room that
fits nothing else; what the canvas lines showed against the `doing` lines, in three sentences,
without a claim.

## Moments to log

A room opened; a note written; a block closed; a drop; a check failed, with its defect line; the
contrast picked; `concept_reach_threshold` declared; the coordinating-turn rule written;
anything you keep seeing for the third time (`--kind note`).

## Final message

Counts: rooms read whole, notes written, lexicon and running entries, dropped and remaining,
checks passed and which failed, the contrast picked, the threshold declared, the rooms with an
`organizing_end_hour`; then the three things you keep seeing and the one that most surprised
you. A return value.

## Close

`done.sh A1` at the end of `A1a` and of every block (`A1b-NN`); it runs `validate.py A1`, and you
paste the report into `notes-A1.md`. At `A1c`, the last: `_head.md` rewritten whole in the standing instructions' form; `handback-A1.md`; the closing diary line, three sentences through `mem.py log`; then the brief, `out/interview/A1c.md`, and `done.sh A1 --cut interview` (STANDING §2, interview points). From here
on every leg opens with `validate.py --open NN` after the head and the last five diary entries. Stage B1 reads your room notes as its prior.
