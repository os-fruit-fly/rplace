# Run yard, coder instrument v32

> **Layout in this repository (2026-10-02).** The yard's folders sit here under other names:
> `_instrument/` is `instrument/`, `_tools/` is `handler/tools/`, `_lead_sessions/` is `lead-sessions/`, and the
> scheduler's documents (CONTRACT-scheduler.md, CHECKPOINTS.md and the rest) are in `handler/`. `census/` and
> `rooms/` keep their names. The text below describes a working yard. The tools expect that layout
> (`_tools/` beside `_instrument/` and `rooms/`): to run them, copy these folders into a yard folder of
> yours under the yard's names. `handler/refresh_examples.py` refreshes `rooms/` here from the study's yard.

One folder per community of the r/place census, each holding everything a case lead and its
fleet need to code that community's week: the instrument, the record, the seven days before,
the brief where one exists, and the state of the work. Nothing here depends on which model runs
the agents or on which program launches them; a folder is complete on its own and runs from any
machine with `python3`.

    coder/
      README.md                  this file
      CONTRACT-scheduler.md      what the scheduler does between the agents (the job that
                                 was done by hand on v29, written down)
      STATUS.tsv                 one line per room; regenerated, never edited
      _instrument/v32/           the reference instrument (every room carries its own copy; rooms
                                 coded on v30 keep v30, which is in archive/)
      census/                    which communities are rooms, and why
      _tools/
        room.py                  one room, driven from outside: status, brief, run, message,
                                 check, snapshot, fork, note
        verify_room.py           the scheduler's checks: the brief, each batch, the end
        status.py                rebuilds STATUS.tsv from every room's STATE.json
        compare_forks.py         a room's run and its forks side by side
        build_room.py            how a room was made from raw24 (to rebuild one)
        update_instrument.py     copy the reference instrument into every room, in place
        add_openings.py          write record/openings*.md into rooms that lack them
        selftest.py, simcoder.py a scripted run of the whole procedure, no model called
        selftest_brief.py, simbrief.py   the same for the brief stage
      rooms/<sub>/
        ROOM.md                  the room's numbers and the commands, in order
        STATE.json               the room's memory
        instrument/              the room's version, whole
        record/coder_corpus.jsonl.gz   the 97-hour cut: threads whole, context marked
        record/preweek.jsonl.gz        the seven days before the canvas opened
        record/cut_stats.json          the counts, computed at build
        record/openings.md             every thread's metadata, counts, title and opening text,
                                       for the case lead (plus titles-only and digest files
                                       above 1,500 threads); `room.py run` copies it into run/
        brief/                   built by `room.py brief` where no brief exists: the pre-week
                                 rendered, the brief writer's contract and tools, out/brief.md
                                 when written (298 rooms arrived with one from an earlier run)
        run/                     built by `room.py run`: the case lead's directory, the fleet
                                 under run/fleet/batch_NN/
        snapshots/after-fleet.tgz      the fork point
        forks/<name>/run/        a fresh lead's copy of the snapshot

**Which rooms.** The population is the 706 communities with `handable = 1` in [census/MASTER-census.csv](census/README.md); [the census page](../Manual/census.md) explains the judgements that made that list. The scheduler codes the rooms listed in `STATUS.tsv` (rebuilt by `_tools/status.py`) from the bottom up, smallest first. The study's yard held 741 rooms on 27 September 2026, 33 of them outside the 708 of that day: r/place, the field, coded apart (Manual/census.md), and 32 because they were built before the screen closed them. On 4 October 2026 r/lehigh and r/upvote left the population (no writing about the event while the canvas was open), so 35 of the yard's 741 are outside the 706.

## Persistent case-lead continuation

For a snapshot of both the **case lead's native conversation and the whole room's
filesystem**, use `_tools/codex_lead.py` as described in [CHECKPOINTS.md](handler/CHECKPOINTS.md).
Only the case lead needs a saved native session; brief writers and fleet coders do not.
The adapter works in an isolated managed copy and checkpoints each completed lead reply.

The `room.py snapshot`/`fork` commands below are the older filesystem-only, fresh-lead
research comparison. They do not restore the original agent's conversation. On the last
batch, `message collect` now stops the lead before consolidation; checkpoint there, then
send `message finish`, which no longer collects the same batch a second time.

## What was done to a room before the yard (`PRIOR-RUNS.tsv`, and four columns of `STATUS.tsv`)

`_tools/prior_runs.py` reads every earlier coder run under `50_coding_runs/` (the batch tarballs
and the run folders, the hub runs too) and `40_analysis/coder_version/coder_version.csv`, and
writes `PRIOR-RUNS.tsv`: one line per (room, run) with the instrument version and fingerprint,
the variant, the model that did the reading, when it ran, whether it completed, and whether it is
the run whose codes are in the v35 aggregator package. It also stamps `prior_runs` into each
room's `STATE.json`, and `status.py` summarises that into four columns of `STATUS.tsv`:
`coded_before` (the runs, oldest first; `(partial)` where a run did not close), `coded_under` (the
instrument version of each), `coded_by` (the model of each) and `in_v35_package` (yes for the 298
package rooms the yard holds; `hyperlightdrifter` and `PokemonSage` have no room). Re-run
`prior_runs.py` when a run is added under `50_coding_runs/`; `status.py` keeps the columns.

Where the model comes from: the manifests from v26 on record it; before v26 no manifest has a
model field, and the model is read from the run's transcript (`out/_transcript.jsonl`, the first
assistant message), which is how the rank-band runs of v19 to v24 are known to have run on
`claude-opus-5`, the dispatcher having passed no model argument; `unrecorded` where neither
exists (the hub runs, the v15 pilot). Of the 298 package rooms in the yard, 281 were coded by
Opus and 17 (the tail of the v27 draw) by Sonnet.

## Before anything runs on a machine

    python3 _tools/selftest.py --instrument _instrument/v32 \
        --record <any room>/record/coder_corpus.jsonl --sub <sub>

(`gunzip -k` the record first.) It runs a room through the gate, the fleet, the pool, the
forest, the audit and the close with scripted agents in under a minute and prints
`SELFTEST PASSED`. `python3 _tools/selftest_brief.py --room rooms/<sub>` does the same for the
brief stage on a copy of the room and prints `SELFTEST-BRIEF PASSED`. If either does not,
nothing else should run.

## Running one room by hand

From `rooms/<sub>/`, with `T=../../_tools/room.py`:

    python3 $T status                    where the room stands, and what is next
    python3 $T brief --model <id>        if the brief is to write; then launch an agent in
    python3 $T message brief             brief/ with this message
    python3 $T check --brief             when the writer ends (place its transcript first)
    python3 $T run --model <id>          builds run/
    python3 $T message lead              launch the case lead in run/ with this message
      branch A: it reads and closes the room; then `check`
      branch B: it dispatches batch 01 and stops; then, for each batch:
    python3 $T message coder --batch NN  launch a coder in run/fleet/batch_NN/
    python3 $T check --batch NN          when it ends (place its transcript first)
    python3 $T message collect --batch NN --summary "..."   send to the lead
    python3 $T snapshot after-fleet      when the last batch is collected
    python3 $T message finish --batch NN send to the lead: consolidate, steps 4 and 5
    python3 $T check                     when the lead has closed
    python3 ../../_tools/status.py --yard ../..

`CONTRACT-scheduler.md` is the whole of it, with what to look for and what to do when a check
fails.

## In Claude Code

Each agent is a session in its directory. Open a terminal in `rooms/<sub>/run` (or
`run/fleet/batch_NN`, or `brief/`), start `claude` with the model you chose, paste the message
`room.py message ...` printed, and let it run to its final message. The scheduler can be a
person doing this, or a Claude Code session opened in the yard's root with
`CONTRACT-scheduler.md` as its instructions and permission to run `python3` and to start the
agent sessions. The transcript of a session is under `~/.claude/projects/`; copy it to the
agent's `out/_transcript.jsonl` before the check.

The same holds for any other runner that can start an agent in a directory with a message: the
messages, the checks and the files are the same; only the launching differs.

## The instrument

v30 is v29 with the threshold and budget at 500, a slice floor of 25, the read audit reading
the journal, four rules for the case lead's step 5, `redispatch`, two sentences in AGENT.md,
the openings file the case lead reads before the gate (`CONTRACT-case-lead.md` §1a), a
timeline seeded by the harness from the record's sticky and moderator marks, the lead's ledger,
and, after the audit of 2026-09-06, `emit` checking every quote and every coded item against
the record and the read log as it arrives, `close_run` C8 to C10, and the contract edits the
audit asked for. `_instrument/v30/CHANGELOG-v30.md` has the list and the reasons; the r/muse pilot and
the liverpoolfc batches that produced them are in `Layer A/50_coding_runs/` and in the project
notes. The instrument fingerprint every run records is over the files in
`newrun.py`'s `INSTRUMENT_FILES`; a room whose fingerprint differs from another's was not coded
on the same instrument, and `close_run` C7 fails a run whose files changed after dispatch.

## Sizes

The record and the pre-week are gzipped; `room.py run` and `room.py brief` unpack them beside
their `.gz` when a room starts. The four rooms above 50,000 items unpack to hundreds of
megabytes and cut into 100 to 400 slices each.
