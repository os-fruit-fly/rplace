# Case lead's contract, instrument __INSTRUMENT__

You are responsible for one community's whole account. **Read `CONTRACT.md` first and whole**:
the method, the register, the citation rule and the five steps hold for you unchanged. This file
says what is different when the room is too big for one reading, what the forest is, and what
you write. Where the two files disagree, this one wins on whatever it says differently, and
`CONTRACT.md` on everything this file does not mention.

Rule 1 for you reads: your corpus, your briefing, `openings.md` (§1a), `out/timeline.md`,
`out/lexicon.md`, and, in branch B, the pooled files under `package/` and the slice cases and
notes under `fleet/`. Nothing else.

---

## 1a. The openings file, read before the gate

`openings.md` in your run directory is the room's table of contents: every thread of the record
in time order of its opening post, with a metadata line (id, hour since the canvas opened, clock,
author and flair, the submission's flair, sticky and moderator marks), a line of counts over the
whole thread (comments in the window and in all; branches, which are the direct replies to the
opening post; depth, the longest reply chain; distinct authors; the sum of scores over every item
the record scores), the title, and the opening post's text cut at 500 words. `score` and
`stickied` are snapshots taken at retrieval, weeks after the event, and say nothing about the
week; `distinguished` is reliable.

**Read it in step 1, after the brief and before the gate (§1b)**, whole. In a large room the harness
also writes `openings_titles.md` (no text) and `openings_digest.md` (counts per hour, the ten
highest-scored titles per hour, every stickied or moderator post): read the digest first, then
the titles file, and open `openings.md` only for the hours you need; a file of a million tokens
read whole and then compacted is not held, it is forgotten with a summary in its place.

**What it is for.** The shape of the week before anyone reads it: what was posted when, which
threads grew and which did not, where the room's own business sits among the canvas threads,
what the room was doing when the canvas opened and what it went back to. In branch B it lets you
place every slice in the week before you dispatch it, and it gives you a check no script can
run: when a coder's dispositions arrive at collect, a thread whose title names the canvas and
whose verdict is `out_of_scope` is a thread to note, and, in step 5, to open with `read item`.

**What it is not.** Material. You code nothing from it and cite nothing from it but a title,
which `cite` reaches on the opening post as it always has. No relation in `## Relations` rests on
it. It is not served through `read.py`, so the read log does not show it. In branch B the
record of what you read before consolidation therefore stays what it was: nothing. In branch A
you then read the threads having already seen where the week went, which is deliberate: say in
`## Selection` that you read the openings before the triage, since the log will not. A lead
who has read the openings knows where the room's week went; a lead who has read the threads is
a coder who also adjudicates, and that is the line.

## 1b. The gate, decided once and recorded

`corpus_manifest.json` holds the counts the harness computed: `items_in_window`, and
`chars_by_people`. Run

    python3 tools/fleet.py plan

It decides the branch on `items_in_window` against the threshold, 500, and writes
`out/_gate.json`: the branch, the threshold, the two counts, and, in branch B, one line per
slice. It also starts `out/timeline.md` and `out/lexicon.md`.

- **Branch A: you read the room yourself.** Steps 1 to 3 as `CONTRACT.md` has them.
- **Branch B: a fleet reads it and you do not read the raw threads.** §3.

The threshold is the dispatcher's, not yours. Depart from it only with a reason, in `notes.md`.
Two branches are two instruments over one census; a branch that is not recorded is an
instrument change nobody can find later, so the gate record is an output. In branch B,
`notes.md` repeats it in this exact machine-checkable form, substituting the values from
`out/_gate.json`: `branch B; threshold N; items_in_window N; chars_by_people N`.

## 2. The order of the work, in both branches

Steps 1 to 3; then `emit.close()` once, which writes `out/codes.jsonl` and the other three files
from your journal; then the forest (§4); then the gate (§5); then step 4; then step 5; then
`emit.close(verdict=...)` once more. `close()` may be called again; each call is journalled,
and the run record counts them.

## 3. Branch B, the fleet

**Slices are whole threads in corpus order.** A slice ends at the last thread that fits the
budget of in-window items, which is the threshold unless you departed from it; a thread larger
than the budget is a slice by itself; a slice of fewer than 25 items joins the slice before it
(the first joins the one after), which may then exceed the budget by that much, so no coder is
sent a handful of comments stranded ahead of an oversized thread. A thread is never
split across coders. `plan` cuts them and records each slice's first and last thread with their
times.

**One coder per slice, in turn.** For each batch NN, in order:

    python3 tools/fleet.py dispatch --batch NN --model <model id>

builds `fleet/batch_NN/`: the coder contract, the fleet coder's contract, `AGENT.md`, the three
tools, the briefing, `timeline.md` and `lexicon.md` as `out/` holds them at that moment, and the
slice as the coder's own record and corpus. Where a thread of an earlier slice was still
receiving replies during this slice's span, its opening post is in the coder's corpus marked as
context; `emit` refuses a code on it. The coder's ids continue from the previous coder's.

The coder does steps 1 to 3 on its slice and writes a slice case and slice notes. It is not given
any other coder's codes, case or notes. After it finishes and before you dispatch the next, read
what it appended to `out/timeline.md` and `out/lexicon.md`: both are facts, one line each, with
item ids. Strike any line that is a reading, then dispatch.

**Your memory of the fleet is `out/ledger.md`, and the harness keeps it.** `collect` appends one
entry per batch: the slice, the counts, the facts lines added, the coder's final message where
the scheduler saved it, every episode the coder tagged `[unresolved]` or `[inherited]`, and its
anomalies and data problems, copied whole. Under each entry you write, at collect and not later,
which lines you struck and why, and what you mean to carry to step 5. Your conversation will be
compacted on a long run and a fork's lead has none; the ledger is what survives. Keep your own
running notes in `out/_lead_notes.md`, written at every collect and before every step and read
back after any compaction; it is part of the record.

A coder that failed its slice is not repaired: `python3 tools/fleet.py redispatch --batch NN
--model <model id>` sets its directory aside under `fleet/_failed/` and dispatches the slice
again with the same ids. Only the last batch can be redone, and only before it is collected. The
decision that a coder failed is the scheduler's (`CONTRACT-scheduler.md` where there is one),
made on the checks, not on the reading.

**You do not call `read` or `find` while the fleet runs, and not before step 4 is done.** In v32
the tools refuse a branch-B lead's raw read or search until `step5_counter` is recorded. A lead
who reads the raw threads is a coder who also adjudicates. After the last coder:

    python3 tools/fleet.py consolidate

closes each coder's journal, copies its codes, dispositions, pointers and read log into
`staging/`, pools them into `package/codes.jsonl`, `package/threads.jsonl` and
`package/pointers.jsonl`, and writes your `out/_journal.jsonl` so that your `emit` holds every
fleet code. From here `emit.close()`, the forest, the gate, step 4 and step 5 are as in §2.

**What branch B gives up, and `notes.md` says so.** No reader holds the whole week: `## Relations`
is assembled from slices you did not read, and it is weaker evidence than a single reader's; say
which relations you carried across a slice boundary and on what. One coder reads each slice, so
the room has no agreement measure. Slice boundaries are arbitrary with respect to the material;
an exchange that straddles one was read by two people, each seeing half. The forest makes the
sequence visible; it does not give anyone the week.

## 4. The forest

`tools/tree_builder.py` builds it from the reply structure and the codes. No agent draws a tree.

    python3 tools/tree_builder.py --sub __SUB__ --record coder_corpus.jsonl \
        --codes-file <codes file> --out-dir .

`<codes file>` is `out/codes.jsonl` in branch A and `package/codes.jsonl` in branch B. It writes
`trees/__SUB__.md`, the forest a reader reads; `package/forest.jsonl`, one line per coded thread;
and `package/tree_index.json`, thread id and coordinate to item id and metadata, so any line in
the forest can be opened with `cite`.

Coordinates are Dewey. The submission is `0`; its replies `1`, `2`, … in time order; theirs
`1.1`, `1.2`, …, to any depth. Five node states: `coded` carries a code; `bridge` carries none
but has a coded descendant and is kept, so the distance between two coded turns is visible;
`removed` is a distinguished comment saying a post was removed, carrying no code, the platform
speaking; `pruned` carries none and has no coded descendant, and is dropped; `collapsed` is a
run of dropped siblings shown as one node with its count. The header counts what was dropped
for the community, and every THREAD line for its thread.

Every line shows the record's metadata where the record has it: `↑N` the score, `⟨…⟩` the
author's flair, `{…}` the submission's flair, and [moderator], [sticky@retrieval], [edited],
[gilded]. `score` and `stickied` are as of `retrieved_on`, weeks after the event, not as of the
week.

**Every coded line carries the item's chunks in text order**, `[c0012 na c0015]`: a code id
where a chunk was coded, `na` where a stretch of forty characters or more was passed over,
then the labels in the same order. The index carries the sequence and each item's coverage,
the share of its text under a code, and the header the count of `na` stretches and the mean
coverage of coded items. So a thread reads as its items' chunks in order, every code sits on
a chunk of an item, and what a coder passed over is visible as a choice. Use the sequence in
step 5 as you use the tree: a long `na` inside a coded turn is a place to open with `read
item` if the account leans on that turn.

**A reply is a reply.** The tree shows that one turn was posted as a reply to another and how
long after. It does not show that the first caused the second. Say so in `notes.md`, and write no
relation in `## Relations` that rests on adjacency alone: adjacency plus what the two turns say
is evidence. Report latency as elapsed time between two posts.

## 5. The gate before step 4

    python3 tools/audit_fleet.py --run . --sub __SUB__

It checks that every code's text is the record's text at its offsets, that every coded thread
has a forest entry and every code sits on a node, that the rendered forest matches, and, in
branch B, that the pool is the staging files, that no thread was disposed twice, that every
batch disposed exactly its slice, and that the gate record is complete. On FAILED, stop: its
output goes into `notes.md` and your final message, and nothing else is done.

## 6. Step 4 and step 5 in branch B

**Step 4 is yours, over the pooled codes.** Read `package/codes_by_thread.md`, which
`consolidate` writes: every code's first-order line under its thread, threads in corpus order
with their slice and hour. Read it one slice at a time, in order, with that slice's case beside
it, opening themes with `emit.theme` as they appear and extending them with `emit.theme_add` as
later slices repeat them; a pool of thousands of codes is read this way or not at all, and a
theme's founding slice is then the saturation answer without a second pass. A theme assembled
inside one slice is a theme about that slice. `package/codes.jsonl` is the pool of record; you
cite codes from it, not from the reading file.

**Step 5 is `CONTRACT.md`'s step 5** with six additions. `## Chronology` is assembled from
`out/timeline.md`, the forest and the slice chronologies; say where a stretch of the week came
from a slice you did not read. It opens on what the room was doing when the canvas opened and
closes on what it went back to: the first coder's and the last coder's edges, which their
`case.md` files describe, are yours to carry, since no one else holds both. **Every time and
every interval you write is computed from `package/tree_index.json`, which carries each item's
time, or quoted from a coder with the coder's own figure; never restate a coder's measurement
from memory.** A gap you cannot compute or quote is not written. `## Relations` uses the forest for sequence under §4's limit; end
a relation that spans a boundary with `[crosses NN|NN+1]`. `## Posts against comments` is
carried from the slice cases, each contradiction marked with its batch; you add none, having
read neither layer. `## Saturation` answers one more question: did later slices bring new
practice or repeat settled ones? Answer it on the codes: every pooled code carries `batch`, so
for each theme name the batch of its first code.

The counter-reading runs as `CONTRACT.md` has it, with `find` and `read item`, once step 4 is
done: the fleet has finished and nothing you read now can reach a coder. A code it turns up is
yours and carries `step5`. Where a hit sits in a thread no coder read whole, call `read thread`
on it before coding anything from it, the one reading of raw threads step 5 allows, and record
in `notes.md` which thread that was and what changed. `## Counter-reading` names the single
strongest item against your reading wherever in the account it already sits, with its id,
before it reports what the search returned, and if no coder's case holds one it says that in
so many words; a section that reports thirty queries and no contrary item has not looked at
the coders' cases.

## 7. Outputs

`CONTRACT.md`'s six, in `out/`, plus:

    out/_gate.json              the branch, the threshold, the two counts, the slices with
                                their first and last thread and times, one line per coder
    out/timeline.md             facts: stickies, moderator posts, edits, with times and item ids
    out/lexicon.md              facts: the room's own words, each with the item of its first use
    out/ledger.md               branch B: one entry per collected batch, kept by the harness,
                                your strikes and remarks under each
    out/_lead_notes.md          your running notes, written at every collect and step
    package/codes_by_thread.md  branch B: the pool in reading order, written by consolidate
    trees/__SUB__.md            the rendered forest
    package/forest.jsonl        one line per coded thread
    package/tree_index.json     thread id and coordinate -> item id and metadata
    package/codes.jsonl         branch B: the pool, every coder's codes with their batch
    package/threads.jsonl       branch B: every disposition, with its batch
    package/pointers.jsonl      branch B: every pointer, with its batch
    staging/*_batch_NN.jsonl    branch B: each coder's codes, dispositions, pointers, read log
    fleet/batch_NN/             branch B: each coder's whole directory, case and notes in its out/

`emit.close()` carries `out/_gate.json` into `_run.json`. Nothing here is written by hand except
`case.md`, `notes.md`, and your lines in the two facts files. A script you write to help with
step 4, or to read times and intervals from `package/tree_index.json` for step 5, stays in your
run directory under a name beginning `_lead_`; it is part of the record and is not deleted.
Reading times from `tree_index.json` is the one exception to `CONTRACT.md` §10's rule against
recomputing; it computes nothing the header already gives.

Before your final message, run:

    python3 close_run.py . --role lead --preflight

Fix every reported failure and run it again until it passes. This is a check of the complete
case, including all slices. A retry instruction naming one defect adds that defect to the
checklist; it never narrows the assignment to that defect or to only the files named in the
failure report.
