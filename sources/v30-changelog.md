# v28 to v29, and v29 to v30

**Written 2026-09-04, Layer A.** Two changes and one tool.

## 1. The case lead, and two branches

The coder contract assumed one reader reads the room whole. That holds to about 250 items; the
largest coded room in the census is 246, and rule 12's candidates run past 200,000. v29 adds a
case lead who reads the room whole when it fits (branch A) and runs a serial fleet when it does
not (branch B), then does step 4 and step 5 either way.

**The branch is recorded per community as a covariate**, with the counts it was decided on.
Two branches is two instruments over one census, and the lesson from this study's own coder tier
is that an unrecorded instrument change is invisible afterwards and contaminates everything
computed across it.

**What branch B gives up is written into the contract rather than left to be discovered.** No
reader holds the week; there is one coder per slice, so the largest rooms have no agreement
measure at all; and slice boundaries cut the material arbitrarily. All three go in `notes.md`.

## 2. The forest

`tools/tree_builder.py` joins first-order codes onto each coded thread's reply tree and emits
`trees/<sub>.md`, `package/forest.jsonl` and `package/tree_index.json`. Deterministic; no agent
draws a tree.

Four node states — coded, bridge, pruned, collapsed — and **the dropped are counted in the
header**, per thread and per community, so nobody mistakes what was not coded for what was not
said.

**Coordinates are pure Dewey**: the submission is `0`, its replies `1`, `2`, …, theirs `1.1`,
`1.2`, …, to any depth. Depth is the segment count and siblings share every segment but the last.
A draft scheme that made the top level `1.0`, `2.0` and hung `1.1` beneath `1.0` was rejected: it
makes `[1.1]` a child in one place and a sibling in another, and the worked example circulated
with it did not match what its own code produced — the demo output was written by hand, not run.
This one is tested; `--demo` prints the tree, the counts and an index lookup.

**A limit is written into both contracts.** A reply is a reply. The tree shows that one turn was
posted after another and how long after; it does not show that the first caused the second. No
relation may rest on adjacency alone, and latency is elapsed time between two posts, not the speed
of a decision. The forest was proposed as proof of causal direction, and it is not that.

## 2a. Additions of 2026-09-05

`lexicon.md` travels between coders with `timeline.md`, both facts and neither a reading, so the
room's own words reach every slice. The forest carries the record's metadata on each node beside
`retrieved_on`, with `stickied` marked as a retrieval-time snapshot, and a `removed` state for
platform removal notices, which are the platform speaking and not a participant.
`tools/audit_fleet.py` is the gate the case-lead contract names before step 4; it reports a check
that could not run as failed, never as passed.

## 3. Unchanged

Method, register, the citation rule, the five steps, the brief writer, and every output of v28.
Small rooms run as they did, now with a forest.

## 2026-09-05, afternoon: audited, made runnable, tested on r/liverpoolfc

Two auditors read the v29 files against the v28 harness before any run. Their finding, in one
line: v29 as shipped could not be run, in either branch. `newrun.py` dispatched v28's contract
and none of the v29 files; the harness carried three version strings; nothing cut a slice,
nothing consolidated a fleet, `emit` could not theme a pooled code, the forest command was fed a
file of dispositions and rendered blank labels, `audit_fleet.py` failed every correct run on one
check and passed vacuously on three, and the two role contracts named files nobody creates.

What changed:

- **v29 ships its own harness.** `read.py`, `cite.py`, `emit.py`, `close_run.py`, `newrun.py`,
  `newbrief.py`, `read_brief.py`, `render_corpus_v29.py`, `cut_window_v29.py`, all stamped v29.
  `newrun.py` dispatches the coder contract, the case lead's contract, `AGENT.md`, the three
  tools and `tools/`, substitutes the role placeholders, and writes `corpus_manifest.json` with
  the counts the branch gate reads.
- **`tools/fleet.py`** is the case lead's harness for branch B: `plan` decides the branch, cuts
  whole-thread slices in corpus order and writes `out/_gate.json`; `dispatch` builds a coder's
  directory with its slice, the openings of earlier slices' threads still active in its span
  marked as context, and ids continuing from the previous coder; `consolidate` closes each
  batch, writes `staging/` and `package/`, and gives the lead a journal holding every code.
- **`emit.py`**: ids continue across a fleet from `_manifest.json`; a code or pointer on an
  earlier slice's opening is refused; duplicate detection survives across processes;
  `close()` carries `out/_gate.json` into `_run.json`.
- **`tools/tree_builder.py`**: `--record coder_corpus.jsonl` builds the forest from the run's
  own record; `first_order` is read where `label` is absent; retracted codes are not codes; a
  re-run replaces the community's forest lines instead of appending; every THREAD line carries
  its item, coded and dropped counts.
- **`tools/audit_fleet.py`** rewritten: seven checks that read what the tools write, a branch-A
  mode, and no check that can pass without its inputs.
- **`close_run.py --role fleet|lead`**: a fleet coder's directory holds no theme by contract;
  the lead's C6 reads the fleet's read logs from `staging/`.
- **The contracts.** The case lead's and fleet coder's contracts rewritten to the procedure the
  tools implement: the order of the work in both branches (steps 1 to 3, `emit.close()`, forest,
  gate, step 4, step 5, `emit.close(verdict)`), the slice rule and the context openings, the two
  facts files, the tags, the pool, the lead's step 5, every output by path. The precedence
  between the files is stated. `AGENT.md` carries the role, the batch and the slice in STATE.
  The coder contract's preamble says the one rule v29 adds inside it.
- `removed` stays what it was: a distinguished comment saying a post was removed. A body that
  reads `[removed]` or `[deleted]` is an absence and is rendered as one, not a removal notice.

## 2026-09-05, evening: the two runs, and what they found in the instrument

Fingerprint `e6a5732e7e854df9` for both runs; every coder and both leads on `claude-sonnet-5`.

**r/liverpoolfc, branch B, 33 slices, stopped after batch 07** (`50_coding_runs/run_v29_liverpoolfc_partial/`).
Seven coders, 12 to 26 minutes each, contexts of 202k to 296k tokens, 74 codes in all (3, 1, 0,
54, 16, 0, 0); batch 06 read the 2,030-item derby thread whole and recorded it out of scope.
Every batch's read claims hold against what `read.py` served. Stopped for time, not for a
defect: thirty-three serial coders is nine hours. The lead holds its journal at batch 07; the run
resumes from `dispatch --batch 08`. Three Fable coders ran slices 01 to 03 before the model was
corrected (`_lfc_v29_fable_partial/`): Fable minted 49 codes on slice 01 where Sonnet minted 3.
Examined 2026-09-06: all 49 sit in `62dd8q`, the derby pre-match thread, and are line-ups, alarms and pub talk, coded against scope; Sonnet's 3 there are the sub's restyle, coded as the contract asks. The gap is a Fable scope failure, not a reading.

**r/muse, branch B, 2 slices, complete** (`50_coding_runs/run_v29_muse/`). 442 items, 62 threads;
coders of 38 and 30 minutes, 176 and 173 codes; the lead consolidated, built the forest, passed
`audit_fleet` (349 codes at their offsets, 349 on nodes, both slices disposed exactly), grouped
21 themes, ran a 32-query counter-reading and closed `full`. `close_run` 7 of 7 for the lead and
both coders. Against the v27 single reader of the same cut: 34 coded threads to v27's 36, 286
coded items to 306, every fleet-coded thread and item inside the v27 set; the two threads only
v27 coded are the sub's own April Fools jokes, which the batch 01 coder ruled out of scope citing the Setting section; the section says to code such talk as conduct not about r/place, so this is a coder's misreading and the wording wants tightening. Ninety-six minutes end
to end.

**Defects found, not fixed, so that the fingerprint above is the instrument that ran:**

- `read.py audit` reads `out/threads.jsonl`, which only `emit.close()` writes; in a fleet batch
  before `consolidate` it reports `checked: false` and 0 mismatches, which is not a pass. It
  should fall back to the journal's `thread` records. A scratch checker that does so found 0
  mismatches in 89 dispositions across nine batches.
- Coders write working scripts to the scratchpad directory the harness names in their
  environment, which is shared across every agent of the session, against AGENT.md's scratch
  rule. The dispatcher's prompt for the muse batch 02 coder forbade it and that sufficed; the
  sentence belongs in AGENT.md.
- Coders read the tools' source (`emit.py` three times, `read.py`, `cite.py`): about 49k chars,
  18k tokens, per coder, for nothing AGENT.md does not say. One line in AGENT.md.
- `fleet.py plan` closes a slice when the next thread would overflow the budget, so a slice can
  be one thread of five items (liverpoolfc slice 09) ahead of a 433-item thread. A slice under
  some floor should fold into its neighbour.
- Late slices carry many context openings (liverpoolfc slice 33: 169 openings for 85 items of
  its own). Bearable at one line each; the first thing to trim if a run must be cheaper.
- The lead wrote its step 4 with a script in its run directory and deleted it after; the record
  keeps the themes and not the script. Harmless, and worth a sentence in the lead's contract
  either way.


# v29 to v30 (2026-09-06)

Cut for the run yard, after the r/muse pilot and the seven liverpoolfc batches. Every file
renamed from `.v29.` to `.v30.`; every label `v29` in the tools now reads `v30`; the fingerprint
moves. What changed in substance:

- **Threshold and budget 500.** `fleet.py plan` defaults to `--threshold 500 --budget 500`, and
  the case lead's contract says 500. Grounds: the frame's 300 rooms stop at 501 items; on v27
  one reader read 91 per cent of the threads whole across the 250-to-501 band with no decline
  toward the top; a whole room at 500 items is about 100,000 tokens of corpus. Recorded in
  `claude/fleet-token-budget-and-the-two-slice-pilot.md`.
- **A slice floor.** `plan --floor 25`: a slice under 25 in-window items folds into the slice
  before it (the first, into the one after). liverpoolfc slice 09 was one thread of five items.
  `_gate.json` carries `floor_items` and the rule names it.
- **`read.py audit` reads the journal** when `out/threads.jsonl` is absent, so a fleet coder's
  reading claims are checked before consolidation; the result carries `source` and `declared`.
  On the nine fleet batches run so far: 0 mismatches.
- **AGENT.md** forbids the session-level scratchpad an environment may name, and forbids
  reading the tools' source (about 18,000 tokens a coder, for nothing).
- **The community's own April Fools joke** is disposed `coded`, never `out_of_scope` for being
  a joke; the r/muse batch 01 coder read the old wording the other way.
- **The case lead's step 5**: every time and interval computed from `package/tree_index.json`
  or quoted with the coder's own figure (the r/muse lead turned 51 minutes into "roughly nine
  hours" by restating); `## Counter-reading` names the strongest contrary item with its id
  before reporting the search; the chronology carries the first and last coders' edges; a
  lead's helper script stays in the run directory under `_lead_`.

- **`fleet.py redispatch --batch NN --model <id>`** sets a failed coder's directory aside under
  `fleet/_failed/` and dispatches the slice again with the same ids; only the last, uncollected
  batch. The gate record keeps the set-aside under `redispatched`.

- **The openings file** (`render_openings_v30.py`; asked for by J on 2026-09-06). `newrun`
  writes `openings.md` into the case lead's directory: every thread in time order of its
  opening post, with the metadata line, a counts line over the whole thread (comments in the
  window and in all, branches, depth, distinct authors, the sum of scores over every scored
  item), the title and the opening post's text cut at 500 words. Rooms over 1,500 threads also
  get `openings_titles.md` and `openings_digest.md`. The lead reads it in step 1; the contract's
  new §1a says what it is for and what it is not (orientation; nothing coded or cited from it
  but a title; not served through `read.py`). Fleet coders do not get it. AGENT.md's STATE
  block names it. In the fingerprint.
- **The timeline is seeded by the harness.** `fleet.py plan` starts `out/timeline.md` with
  every stickied or moderator-distinguished post, hour, author, title and id, from the record's
  metadata, so coders extend a record of facts instead of starting one.

- **The lead's memory** (J, 2026-09-06). `collect` keeps `out/ledger.md`: per batch the slice,
  the counts, the facts lines added, the coder's final message when saved, its `[unresolved]`
  and `[inherited]` episodes and its anomalies and data problems copied from its case and
  notes; the lead writes its strikes under the entry at collect. `consolidate` writes
  `package/codes_by_thread.md`, the pool in reading order, and step 4 reads it one slice at a
  time. The lead keeps `out/_lead_notes.md`. A fork's lead reads the ledger and the notes
  first. Fleet coders get no such file: what travels between coders is facts, not readings.

## After the audit (2026-09-06, evening)

Four auditors read the contracts against Gioia, Corley and Hamilton (2013), Eisenhardt (1989)
and Langley (1999), and the tools against the contracts (a Sonnet and a Fable each; the reports
are in `Layer A/10_instrument/v30/audit_20260906/`). What changed, and why:

- **Contracts.** §1 no longer describes the coder's themes with Gioia's words for his second
  order ("researcher-centric ... abstraction"); themes are "still descriptive", his first-order
  concepts, and the second order and the aggregate dimensions belong to a reader the coder is
  now told about: §1's "Write so another reader could follow you" says the outputs go to a
  reader that builds the account across three hundred communities and does the abstracting.
  §7: a theme names the doing, not how it came out. §8 Relations: a link needs a passage in
  which the later turn answers, names or recalls the earlier; order alone is reported as
  *follows*. §2: day markers are the corpus's (`d0` from 03-31 16:00, twenty-four hours each,
  as printed on every item line), written only in the form `d1 04-01 16:08`; the earlier
  sentence called them calendar days, which the corpus never did. §9 maps the seven
  `emit.stage` names onto the steps (`step6_account` is `case.md`, `step7_write` is
  `notes.md`). §0 says in one clause what a fleet coder does not do. The lead file: §1a
  (openings) now precedes §1b (the gate) on the page as it does in the work; precedence in
  one form; branch A says in `## Selection` that the openings were read before the triage;
  branch B carries `## Posts against comments` from the slice cases; a counter-search hit in a
  thread no coder read whole may be read with `read thread`; the `_lead_` script may read
  times from `tree_index.json`, the one exception to §10; the fold rule says which neighbour.
  The fleet file: "no theme" rather than "no pattern above a code"; the two-themes question
  is not asked; `step6_account` and `step7_write` are announced; the corpus's counts include
  the context openings. AGENT.md: scratch goes under `out/` or the run directory; the tally
  has `threads_undisposed`; `emit` refuses what it now refuses.
- **`emit`** verifies every quote against the record as it arrives (a code, a pointer, an
  `excluded_quote`): the text is a non-empty slice of the item's body, the item is in the
  thread named, the body is not `[deleted]`/`[removed]` (Rule 7). It refuses a code or a
  pointer on an item `read.py` never served (a thread read whole, a window's items, or an
  `item` read; `read.py` now logs `window_items`). `close()` is a journal record, so
  `close_calls` and the verdict outlive the process. A refused `code()` no longer registers
  its duplicate key first. `theme()` refuses an empty code list; `thread()` needs a stage and
  a thread of the corpus. `item_kind`, `author` and `created_utc` are on every code, as §9 had
  promised.
- **`close_run`** C8 (pointers and exclusion quotes verified), C9 (every live code and
  pointer on a served item), C10 (nothing after the last close); C3 no longer passes an empty
  text at an out-of-range offset; the verdict is read from `_run.json` first; `--help`.
  `audit_fleet` verifies pointers and exclusion quotes too. `newrun` hashes `tools/` into the
  manifest, so C7 sees an edit to `fleet.py`. `consolidate` marks the coders' stage and close
  records `coder_stage`/`coder_close`, so the lead's journal starts with no stage and its
  `_run.json` reports the lead; it catches an overclaim with a sentence instead of a traceback.
  `collect` refuses a second call without `--force`; the context span ends at the window's
  end; `fleet.py --help` explains every flag. `cite`'s shell form prints a refusal and exits 2
  instead of a traceback, requires a quote, and its normalised path refuses an ambiguous quote.
  `read.py` has no `--out` (the environment variable `READ_LOG_DIR` is the scheduler's).
  `tree_builder` opens files as UTF-8 and prints usage on missing arguments instead of running
  the demo. `emit.py --help` lists the calls.
- **Yard tools.** `room.py check --fork` checks the fork; `room.py fork` recomputes the hashes
  of the files it rewrites and records the parent's, so a fork passes C7; B5 uses the record's
  id shape; E3 reads the query log too, and counts the consolidation second as before; the
  self-test's scripted case passes B4.

Fingerprint after the audit: `17ae5d4fb7912406`.

J's three answers (2026-09-06, later): the room's own April Fools joke is in scope as conduct,
§5 now says so beside §2, with the note on every such code mandatory. A score is a number
taken at retrieval; it may be reported beside an item and is never coded as something these
people did (§2). And instead of defining an episode, the thread tree is coded: every code is a
cited chunk of an item (a sentence or a paragraph, cited whole), and the forest now shows each
coded item as its chunks in text order, `[c0012 na c0015]`, with `na` for a stretch of forty
characters or more that no code covers; the index carries the sequence and each item's
coverage, the header the count of `na` stretches and the mean coverage. §6 says a passage is
cited whole and that an uncoded stretch is a visible choice; §8 says an episode is a stretch of
the coded threads bounded by item ids and resting on the codes in the forest; the lead's §4
describes the sequence line. Fingerprint: `6560df4fd13c1618`.

Not changed by the audit: the citation rule, the append-only journal, the counter-reading
procedure, Rule 6, "a reply is a reply", the pointer schema, the forest, the slice rule, the
seeded timeline, the ledger. Open, J's to decide: the community's own April Fools joke against
§5's scope test; whether a score may be coded as conduct; whether an episode is defined.

## The brief stage and the tools aligned (2026-09-06, night)

J asked for the equivalent of the yard for briefs and for the tools of the brief writer, the
coder and the aggregator to be defined the same way unless there is a reason. Every room
already carried the brief stage; what it lacked was the scheduler's side. Added: `verify_room
--brief` (F1 to F6: the brief over 300 words unless harness-written, the nine headings, a read
log opening with `header` and a note on the days touched, every quoted string of twenty
characters or more verbatim in the pre-week record against the item id written beside it or
anywhere, one in ten tolerated and listed; the transcript; the manifest's hashes), `room.py
check --brief`, the stages `brief to write` and `brief built, writer to run` with their next
steps, the scheduler contract's brief cycle and F rows, `simbrief.py` and `selftest_brief.py`.

The tools: `TOOLS-SPEC.md` says what the reading, citing and searching tools do the same way
and what differs with reason. `read_brief.py` now logs to `out/_read.jsonl` with `read.py`'s
record shape (a thread read carries `thread_id`), has the `item` verb, no `--out`
(`READ_LOG_DIR`), the same `state` keys, and prints `ReadError:` like `read.py`. `cite.find`
returns a `FindResult` with `truncated`, `limit`, `scanned`, `not_scanned`, as the aggregator's
does, and logs `kind: find, tool, items_scanned, items_not_scanned`. The aggregator's
`cite_case.py` and `mem.py` are left as v36 built them, with their differences listed in the
spec for v37. The brief writer's contract, `read_brief.py` and `newbrief.py` are in the
fingerprint now. Fingerprint: `1d758e5427e622df`.
