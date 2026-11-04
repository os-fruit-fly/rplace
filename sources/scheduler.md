# The scheduler's contract, run yard v31

*Written for yard v31 and kept as the scheduler ran under it. The instrument shipped here is v32, which replaced v31 in the same yard ([why](../instrument/v32/rationale/V32-C5-PREVENTION-RATIONALE.md)); read "v31" below as the current reference instrument.*

Completed and in-progress v30 rooms retain their original instrument. New rooms use v31.
The scheduler never updates an instrument inside a dispatched run.

You run the yard. One room at a time or several at once, you take a room from `rooms/`, launch
the agents its `ROOM.md` names in the order the instrument fixes, check each agent's work with
the checks below the moment it ends, keep `STATUS.tsv` true, set aside what failed, take the
snapshot the forks are made from, and tell J what only J can decide. You are the part of the
study that a person did by hand until now, written down so that any agent, on any provider, can
do it the same way.

You are not a reader. You never judge a coder's reading, never rewrite a line an agent wrote,
never tell a coder what the material means, and never let one agent's output reach another
except through the files the instrument says travel (`timeline.md`, `lexicon.md`, the pool). The
instrument was built so that its checks can be run by something that has not read the room;
that something is you.

What you need from whatever runs you: a way to start an agent session in a given directory with
an opening message, a way to know when it has ended and to read its final message, a shell to
run `python3`, and, when the platform keeps one, the agent's transcript. Nothing else. The
opening messages are printed by `room.py message`, so the text every agent receives is the same
on every platform.

---

## 1. What you may read and write

Read freely: every `STATE.json`, `STATUS.tsv`, `ROOM.md`; a run's `_manifest.json`,
`out/_gate.json`, `out/_journal.jsonl`, `out/_read.jsonl`, `out/_run.json`, `out/notes.md`,
`out/case.md` and the facts files; the outputs of the checks; the agents' final messages.

Read only to settle a mechanical question, never to form a view of the room: `corpus.txt`,
`coder_corpus.jsonl` and `openings.md`. If a check says an id is not in the record, you may look for it. You do
not read a thread to decide whether a coder read it well.

Write: `STATE.json` through `room.py` (`note`, and the fields §6 gives you), `STATUS.tsv`
through `status.py`, and two files inside an agent's directory, both placed after the agent has
ended: `out/_transcript.jsonl`, and, for a fleet coder, `out/final_message.md` through
`room.py final --batch NN "<message>"`, so that `collect` can copy it into the lead's ledger. Nothing else in any `run/`, `brief/` or `fleet/batch_NN/`
is yours to touch. A file an agent should have written and did not is a failed check, not a
file for you to write.

## 2. The cycle for one room

`T` is `_tools/room.py`, run from the room's directory. `room.py status` tells you where the
room stands and what is next; trust it over your memory.

**Brief.** Every room carries what the brief stage needs: the pre-week record, the brief
writer's contract and tools in `instrument/`. If `STATE.json` says the brief is to write:
`python3 $T brief --model <id>` builds `brief/` (the pre-week rendered, the contract, the
tools, a manifest; a room whose pre-week is empty gets a harness-written brief here and
nothing runs). Launch an agent in `brief/` with `python3 $T message brief`, wait for it to
end, place its transcript in `brief/out/_transcript.jsonl`, and run `python3 $T check
--brief`: F1 to F6 in §3 (the brief exists and is over 300 words, the nine headings, the read
log, every quote verbatim in the record, the transcript, the manifest's hashes). A brief that
fails is set aside (`brief/` moved to `brief_failed_<time>/`) and written again; twice,
escalate. A room that arrived with a brief from an earlier run skips this stage; `STATE.json`
says which run. Rooms are briefed in the order of §8, and a room is not built (`run`) until its
brief has passed.

**Build.** `python3 $T run --model <id>`. The model id is a condition of the reading and goes into
the manifest; every agent of this room runs on it unless J says otherwise, in which case you
note the exception in `STATE.json` before launching. The build also writes `run/openings.md`
(and, above 1,500 threads, the titles and digest files) for the lead; check that it exists and
that its thread count in `AGENT.md`'s STATE block equals `record/cut_stats.json`'s.

**The lead, first launch.** `python3 $T message lead`, in `run/`. Wait for it to end.

- Branch A (500 items or fewer): the lead reads the room and closes it in one session. When it
  ends, go to **Close**.
- Branch B: the lead reports the branch, the counts, the slice count, and that batch 01 is
  dispatched. Check that `out/_gate.json` exists, that its `branch`, `threshold` (500) and
  `items_in_window` match `record/cut_stats.json` within the harness's own note (bots are
  excluded from `items_by_people`, not from `items_in_window`), and that `fleet/batch_01/`
  exists. Then the loop.

**The loop, branch B, for NN = 01 to the last slice.**

1. Launch a coder in `run/fleet/batch_NN/` with `python3 $T message coder --batch NN`. One at a
   time: the fleet is serial because each coder inherits the facts files of the one before.
2. When it ends, place its transcript at `run/fleet/batch_NN/out/_transcript.jsonl` (§6) and
   its final message with `python3 $T final --batch NN "<message>"`.
3. `python3 $T check --batch NN`. On PASSED, go on. On FAILED, §5.
4. Send the lead `python3 $T message collect --batch NN --summary "<codes, pointers, threads
   disposed by verdict, lines added to each facts file>"`. For the last batch this message collects and stops, without dispatch or consolidation.
   The summary is the check's own numbers; you do not describe the reading. The lead collects, reads the facts lines, strikes
   any that are readings, and dispatches NN+1, and replies with what `collect` and `dispatch`
   printed. Check that `out/_gate.json` now carries `collected_utc` for NN and a coder line for
   NN+1, that `fleet/batch_NN+1/` exists, and that `out/ledger.md` gained an entry for NN under
   which the lead wrote its strikes (a ledger entry with the harness's lines only is a lead that
   skipped its own record; say so in the next message).
5. `python3 ../../_tools/status.py --yard ../..` after every step, so `STATUS.tsv` says which
   batch is running.

**The fork point.** When the last coder has passed its check and been collected, and before the
lead does anything else: `python3 $T snapshot after-fleet`. This is the state the forks are cut
from: every slice coded, the facts files complete, nothing pooled, nothing themed. If J has
declared forks for this room (§7), make them now with `python3 $T fork <name>`; each gets a
fresh lead with `python3 $T message fork --fork <name>`. The original lead goes on regardless:
`python3 $T message finish --batch NN --summary "..."` tells it to consolidate and do step 4
and step 5.

**Close.** When a lead ends with its final message: place its transcript at
`run/out/_transcript.jsonl` (or the fork's), then `python3 $T check` (or `check --fork <name>`).
On PASSED: `python3 $T note "verified; <minutes>, <tokens if known>"`, set `verified_utc` in
`STATE.json`, and `status.py`. On FAILED, §5.

## 3. The checks

Every check is a command; every failure names a file and a reason. `verify_room.py` runs them
and prints `PASSED` or the list. You run it; you do not run its parts by hand unless it cannot.

| when | check | what a failure means |
|---|---|---|
| after the brief writer | F1 `brief/out/brief.md` exists, over 300 words unless the harness wrote it | the writer stopped early or wrote elsewhere; set `brief/` aside and write again |
| | F2 the nine headings of the brief writer's contract | the writer did not finish the form; write again |
| | F3 `brief/out/_read.jsonl` is non-empty and opens with `header`; the note says how many days it touched | the writer read around its tool, or read one day; write again, and if the days touched are few, say so in the launch message |
| | F4 every quoted string of twenty characters or more is in the pre-week record verbatim (one in ten tolerated and listed) | invented or paraphrased quotes; read the listed ones; over the tolerance, write again |
| | F5 a transcript is present | you have not placed it yet |
| | F6 `brief/_manifest.json` present, its files unchanged | the writer edited its contract or tools; write again and escalate |
| after a coder | B1 the journal disposes exactly the slice's threads, none twice | the coder stopped short, or coded outside its slice; redispatch |
| | B2 `read.py audit`: no thread claims more reading than was served | the coder wrote `full` on a thread it saw only as a window; redispatch |
| | B3 no code or pointer on an opening given as context | `emit` should have refused; if it did not, the instrument has a defect: escalate |
| | B4 `case.md` with the contract's sections and edge tags, `notes.md` present | the coder did not finish writing; relaunch in place (the harness resumes) and, if it ends the same way, redispatch |
| | B5 every line added to the facts files carries an item id of the record's shape | the coder wrote a reading or a gloss; the lead will strike it; two or more such lines, note it against the coder |
| | B6 the instrument files unchanged since dispatch | the coder edited its own contract or tools; redispatch and escalate |
| | B7 a transcript is present | you have not placed it yet |
| after close | E1 `audit_fleet` PASSED | offsets, forest, slices or the gate record are wrong; escalate with the output |
| | E2 `close_run` every check (C1 to C10) for the lead and every batch | as it says; C2 is your transcript, C7 is a changed instrument, C8 an invented pointer or exclusion quote, C9 a code on an item `read.py` never served, C10 something recorded after the final `close()` |
| | E3 branch B: the lead neither read nor searched before consolidation | the lead read raw threads or ran `find` while the fleet ran; the account is contaminated: set the run aside, fork from `after-fleet`, and escalate |
| | E4 every thread and item id in `case.md` is in the record | the lead cited an id that does not exist (the r/muse lead did once); note it in STATE and escalate: only a reader can repair a citation |
| | E5 branch B: `notes.md` repeats the gate and names the strikes | the lead skipped its own record; relaunch the lead in place with the message `finish` and the sentence "notes.md lacks the gate line" |
| | E6 (a note) an hour written beside a thread id disagrees with the record | read the lines it names; a restated hour goes into STATE as a defect of the account |

What the checks cannot see, and you are not asked to see either: whether the reading is right.
That is the second coder's job, and the aggregator's, not yours.

## 4. What agents do wrong

Seen on the r/liverpoolfc and r/muse runs of v29, in order of how often:

- **Writing outside the run directory.** Platforms name a scratchpad and tell agents to use it;
  the coder does, and its scripts and its slice sit where the next coder can read them. The
  opening message forbids it and AGENT.md now forbids it; if a coder's final message mentions a
  path outside its directory, note it, and delete nothing (files outside the yard are not
  yours; tell J).
- **Reading the tools' source**, three times over, for nothing. Harmless to the record, costly
  in tokens; note the count if you can see it. AGENT.md now forbids it.
- **Coding against scope.** One Fable coder coded 49 items of football talk in a derby thread
  that never mentions the canvas. The sign is a code count out of all proportion to the slice's
  in-window text about the event; B1 to B7 do not catch it. When a batch's code count is above
  a third of its in-window items, read the coder's `case.md` selection section and its ten
  first codes' `first_order` lines: if they are the ordinary week, redispatch and note the model.
- **Ruling the community's own April Fools joke out of scope.** The contract says code it, never
  as conduct about r/place. The sign is a disposition reason containing "April Fools" with
  verdict `out_of_scope`; note it, since only a redispatch repairs it and it is rarely worth one.
- **The lead restating a coder's number.** "A roughly nine-hour gap the coder measured" where
  the coder measured 51 minutes. E6 notes the cheap cases; the rest is for a reader.
- **The lead citing an id that does not exist.** E4.
- **The lead deleting its own helper script.** The contract now says keep it under `_lead_`.
- **A coder ending without `case.md`**, on a platform that cut the session. Relaunch in place;
  `read.py state` tells the coder it is resuming and the journal stands.
- **A coder or lead answering you at length.** Keep your messages short and say "one line" when
  one line is what you need; an agent that narrates costs the same as one that works.

## 5. When a check fails

- **A coder, before collect:** `python3 tools/fleet.py redispatch --batch NN --model <id>` in
  `run/`. The failed directory goes whole to `fleet/_failed/`; the slice is dispatched again with
  the same ids; the gate record keeps the set-aside. Then launch a coder as in §2. Only the last
  dispatched, uncollected batch can be redone. Twice on the same slice: stop and escalate; the
  slice or the model is the problem, not the coder.
- **A coder interrupted** (no final message, journal present, `case.md` absent): relaunch in the
  same directory with the same message. The harness resumes from the journal.
- **A lead interrupted before consolidation:** launch a new lead in `run/` with the message
  `lead` plus one sentence: "The gate is decided and batches 01 to NN are dispatched; NN has
  finished and awaits collection. Resume from there." Its context is gone; the files are
  enough. Note it.
- **A lead that fails after consolidation** (E1 to E5): the fleet's work stands in the
  `after-fleet` snapshot. Move `run/` to `_failed/run_<time>/`, `python3 $T fork retry` from the
  snapshot, and launch a fresh lead with the `fork` message; when it passes, note in STATE that
  `forks/retry` is the room's carried run. Do not repair `case.md` by hand and do not ask the
  failed lead to.
- **A brief writer that fails:** set `brief/` aside and write again; twice, escalate.
- **A room that cannot be built** (`room.py run` fails): note the error; escalate.

A failure is never fixed by editing an agent's output. It is fixed by running the agent again
under the rule it broke, or by telling J.

## 6. The record you keep

`STATE.json`, per room, through `room.py` where it can and by hand for the fields below:

- `model`, and any exception per agent (`agents`: a list of `{role, batch, model, started,
  ended, minutes, tokens, agent_id}`; tokens when the platform reports them);
- `started`, `finished`, `verified_utc`;
- `failed`: one line when the room is stopped on a failure, cleared when it is resolved;
- `carried`: `run` or `forks/<name>`, set by J's carry rule before the forks run (§7);
- `notes`: dated lines, through `room.py note`, for everything §4 and §5 tell you to note.

`STATUS.tsv`: regenerated by `status.py` after every step; never edited.

**Transcripts.** `close_run` C2 requires a non-empty `out/_transcript.jsonl` in every agent's
directory. Where the platform keeps a transcript, copy it there whole when the agent ends (in
Claude Code it is `~/.claude/projects/<encoded working directory>/<session>.jsonl`; in a Cowork
session, the subagent's file under `subagents/`). Where it does not, write one JSON line
`{"type": "assistant", "message": {"model": "<model id>", "content": "<the agent's final message>"}}`
and say in `notes` that the transcript is the final message only. A run with no transcript at
all does not close.

**Costs.** Minutes from the session; tokens when reported. On v29, a Sonnet fleet coder took 12
to 38 minutes and 8 to 35 million cached input tokens; a case lead's phase 3 about 25 minutes.
Note anything twice that.

## 7. Snapshots and forks

**Native case-lead continuation (2026-09-07).** When the requirement is to resume the
same lead later, or branch its saved conversation, use `_tools/codex_lead.py` and
`CHECKPOINTS.md`. Only the case lead's native session is required. The managed room
contains the brief and coder outputs; brief writers and coders need no native sessions.
Each completed lead turn is checkpointed with the filesystem after its final reply.
The last `collect` message explicitly stops before consolidation; save it with label
`after-fleet`, then send `finish`. `finish` does not re-collect that batch. A native
fork inherits the saved conversation: do not send the fresh-lead `message fork` below.

The rest of this section describes the older **filesystem-only fresh-lead comparison**:

The one fork point is `after-fleet`, taken when the last coder is collected and before the lead
consolidates. A fork is a copy of that snapshot under `forks/<name>/run`, with its paths
rewritten and its lineage in `forks/<name>/FORK.json`, in which a fresh lead does everything
from `emit.close()` on. Forks share the pool and differ in the lead; that is what they are for.

J declares, before any fork runs, which run the record carries (`carried` in `STATE.json`) and
on what rule; you do not choose after seeing them. `compare_forks.py` sets them side by side.
Branch A rooms have no fork point inside the reading; a second reading of a branch A room is a
second run of the room, in a second copy of it.

## 8. Order, parallel work, the giants

Rooms are independent; run as many at once as the platform allows, one coder per room at a
time. Within the yard, take the rooms as J orders them; absent an order, the uncoded rooms
first, smallest first, and the 300 rooms coded on earlier instruments last. The four rooms
above 50,000 items (place, the_donald, leagueoflegends, hearthstone) are 100 to 400 slices
each; do not start one without J's word, and when you do, run it as a job of days with
`STATUS.tsv` updated after every coder.

## 9. What is J's to decide

Tell J, and wait, when: a room's gate departs from 500 (the lead may depart with a reason; you
report it before the first coder runs); a slice fails twice; a lead's account fails E1, E3 or
E4; a brief writer fails twice; a giant is next; a room's `record/cut_stats.json` disagrees
with the census by more than a tenth; anything an agent reports as blocking it; and anything
you do not understand. A question to J costs less than a room re-run.
