# Instrument v32

One integer, no decimals. `CHANGELOG-v32.md` says what moved and when.

## The files

| file | |
|---|---|
| `CONTRACT.v32.md` | the coder contract. Ten sections; every role reads this first |
| `CONTRACT-case-lead.v32.md` | the case lead: the branch gate, the fleet, the forest, step 4 and 5 over a pool |
| `CONTRACT-fleet-coder.v32.md` | a fleet coder: one slice, steps 1 to 3, a slice case |
| `AGENT.v32.md` | operating notes beside the contracts: the tools, the role, what to do when interrupted |
| `CONTRACT-brief-writer.v32.md` | the brief writer: the seven days before the canvas opened |
| `read.py`, `cite.py`, `emit.py` | the three tools a coder calls |
| `read_brief.py` | the brief writer's reading tool; `cite.py` is shared |
| `TOOLS-SPEC.md` | what the reading, citing and searching tools do the same way across the brief writer, the coder and the aggregator, and what differs |
| `tools/fleet.py` | the case lead's harness: `plan`, `dispatch`, `consolidate`, `status` |
| `tools/tree_builder.py` | the forest, from the record and the codes |
| `tools/audit_fleet.py` | the gate before step 4 |
| `close_run.py` | pre-final and post-exit gates: C1 to C12, `--role lead|fleet`, `--preflight` |
| `newrun.py`, `newbrief.py` | build a run directory |
| `render_corpus_v32.py`, `cut_window_v32.py` | the renderer and the window cut |
| `render_openings_v32.py` | the openings file the case lead reads first: every thread's metadata, counts, title and opening text |

## A run

    python3 newrun.py RUNDIR SUB CORPUS.jsonl BRIEF.md MODEL     # the case lead's directory
    cd RUNDIR
    python3 tools/fleet.py plan                                   # the branch, the slices
    python3 tools/fleet.py dispatch --batch 01 --model MODEL      # branch B: one coder at a time
    ...                                                           # the coder runs in fleet/batch_01
    python3 tools/fleet.py consolidate                            # after the last coder
    python3 tools/tree_builder.py --sub SUB --record coder_corpus.jsonl --codes-file package/codes.jsonl --out-dir .
    python3 tools/audit_fleet.py --run . --sub SUB
    python3 close_run.py . --role lead                            # after the lead's step 5

The case lead's contract gives the same commands at the points where the lead runs them.
