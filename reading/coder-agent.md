# Reading copy: coder-agent

Links below are resolved against commit `7c788ae58ce0d4ae171d65e7550cf55b83a22624`. Source wording is unchanged; Markdown formatting may differ. [Exact source bytes](../sources/coder-agent.md), SHA-256 `f428e33ead41ba54ae06d7001b6fb729b60e4ea6990b1d251b0521062594c82f`. [Source and link manifest](manifest.json). Repository links open the public research repository at this commit.

---

# AGENT — r/**SUB**, coder run **RUN_ID** (instrument **INSTRUMENT**)

**Read this first, then `CONTRACT.md`, then `__ROLE_FILE__`, then start.** This file comes first only because it says whether you are resuming; it refers ahead to rules and sections of `CONTRACT.md` that you will meet there. `CONTRACT.md` is what you must do; `__ROLE_FILE__` is what your role adds to it. This file is what is *here*, what has *already happened*, and what to *call*. If this file and the contracts disagree, the contracts win and you say so in `notes.md`.

------------------------------------------------------------------------

**Scratch stays inside your run directory.** Anything you write — id maps, staged citation batches, notes to yourself — goes in your own run directory, never in a shared or session-level scratch path. A generic filename in a shared path can be read or overwritten by something that is not you. Your run directory is yours alone; nothing else is. **The environment you run in may name a scratchpad or temporary directory and tell you to use it. Do not.** Write every temporary file under `__OUTDIR__` or a subdirectory of your run directory instead, whatever the environment calls its own. That directory is shared with every other agent of the session, and a coder who writes there has left its slice where another coder can read it.

**Do not read the tools' source.** `read.py`, `cite.py`, `emit.py` and `close_run.py` are documented in this file, wholly; opening them costs you tens of thousands of tokens of context and tells you nothing this file does not. If a call fails, the error message says why.

## 0. STATE

    INSTRUMENT      __INSTRUMENT__   — contract, read, cite, emit and renderer all carry it
    CONTRACT        coder-contract-__INSTRUMENT__        __CONTRACT_SHA__
    ROLE            __ROLE__         — your role file is __ROLE_FILE__
    BATCH           __BATCH__
    SLICE           __SLICE__
    COMMUNITY       r/__SUB__
    CORPUS          __CORPUS__                __N_THREADS__ threads, __N_ITEMS__ items (__N_INWINDOW__ in window)
    RECORD          __RECORD__                the unrendered items. cite reads it. you never open it.
    BRIEF           __BRIEF__
    OPENINGS        __OPENINGS__
    OUTPUTS         __OUTDIR__/
    WINDOW          2017-03-31 16:00 -> 2017-04-04 17:00 UTC   (97 hours)

**Run this before anything else. It is one call and it tells you whether you are starting or resuming:**

    python3 __RUNDIR__/read.py __CORPUS__ state

If `cursor` is 0 you are starting. If it is anything else, **a previous attempt at this run was interrupted** — an API refusal, a crash, a timeout. Everything up to `cursor` has been served and everything recorded in `__OUTDIR__/_journal.jsonl` stands. Do not start over and do not re-read what you have already disposed of. `read.py` resumes from its log and `emit` replays its journal; between them the run state is on disk, not in your memory.

------------------------------------------------------------------------

## 1. There is no corpus file for you to open

**Three tools, and nothing else is in scope.** The corpus reaches you through `read`; you do not open it, and you do not go looking around this filesystem for anything else. Your environment may contain a general file tool — this instrument cannot take it away from you, and it is not going to pretend otherwise. What it can do is record what `read` served, so a reading that was never served shows up in the audit, and plant files whose contents must never appear in your outputs.

So this is Rule 1 asking you plainly rather than fencing you in: an atlas, a prior coding of this event, or anything belonging to the project running this study is off limits, and the reason is that your value here is exactly your ignorance of them.

That also means: **do not write a script to slice the corpus, count it, or batch your own reading.** Everything you need is a call. If you find yourself about to write python, the answer is in the header or in one of the three tools, and if it genuinely is not, say so in `notes.md` — that is a defect in the harness and someone needs to know.

------------------------------------------------------------------------

## 2. The three tools

### `read` — the corpus

    python3 __RUNDIR__/read.py __CORPUS__ header
    python3 __RUNDIR__/read.py __CORPUS__ windows [n]
    python3 __RUNDIR__/read.py __CORPUS__ thread <thread_id>
    python3 __RUNDIR__/read.py __CORPUS__ item <item_id>
    python3 __RUNDIR__/read.py __CORPUS__ state

**`header`** — the `#` block: counts, the day histogram, every author, the thread index, the `[deleted]` count, the accounts flagged automatic. It is exact, it was computed before you arrived, and **§10 forbids you to recompute any of it.** Read it once.

**`windows n`** — the next `n` threads in corpus order. This is §5. A long thread comes back as its triage window — title, opening post to 500 words, the three most-discussed top-level replies. A thread shorter than its window comes back whole, because there was nothing to decide about it. The batch stops early if it would get large, and it tells you how many threads remain.

**Default to `n=25`.** Dispose of the batch with `emit.threads_bulk` and call again; `windows` tells you how many threads remain. A batch stops at about 20,000 characters so that what it serves fits in one tool result; if your tool result is still cut short, call `windows` with a smaller `n` rather than reading the overflow anywhere else. One thread at a time also works and costs you a hundredfold in calls; the batch is not a shortcut, it is the intended shape.

**`thread <id>`** — the whole thread, however long. §5: *a thread about this community's conduct of r/place is never abandoned for length.* If the window touched the event, call this. If you cannot tell from the window, call this — uncertainty is a reason to continue, never to stop.

**`item <id>`** — one item. For §8, where `find` has returned a hit and you must read what it returned.

### `cite` — grounding

    python3 __RUNDIR__/cite.py __RECORD__ '<item id>' '<the words you believe are there>'

Returns the exact text and its offsets, or refuses. You never invent a quote or an offset, and you pass what it returns straight to `emit.code` or `emit.thread(..., excluded_quote=...)` unchanged. `find("regex")` is in the same module and logs your query, so your query log is written for you.

### `emit` — recording

**`emit` and `cite` are classes, not modules.** Construct them once, at the top of your first python call, exactly like this — CONTRACT §9 says the same thing and this is the whole setup:

``` python
import sys; sys.path.insert(0, "__RUNDIR__")
from emit import Emit
from cite import Corpus
emit = Emit("__OUTDIR__", corpus_path="__RECORD__")
_c = Corpus("__RECORD__"); cite, find = _c.cite, _c.find
```

`emit.stage()` before each step, then `code`, `pointer`, `theme`, `theme_add`, `thread`, `threads_bulk`, `retract`; and `emit.close()` where your role file says so. `emit.thread` and `emit.threads_bulk` return the reading tally, and `emit.reading()` gives it on demand: how many threads are disposed, how many remain (`threads_undisposed`), how many were read in full. Zero undisposed is what the end of step 2 looks like. `emit` checks every quote against the record as it arrives and refuses a code or a pointer on an item `read.py` never served to you; a refusal names its reason and nothing is recorded.

### `tools/` — the case lead's

`tools/fleet.py`, `tools/tree_builder.py` and `tools/audit_fleet.py` are called by the case lead at the points `CONTRACT-case-lead.md` names, and by nobody else. A fleet coder has no use for them. Append-only: nothing you record can be edited, reordered or withdrawn, so recording early costs you nothing. `discovered_at` is stamped from the stage you announced — it is not a parameter and you are never asked to remember it.

------------------------------------------------------------------------

## 3. What the harness observes

**`read=` on `emit.thread` is checked against what you were actually served.** `read.py` logs every service to `__OUTDIR__/_read.jsonl`, and `read.py … audit` compares that log against your `threads.jsonl` at the end of the run.

This is not a trap and there is nothing to game. Say `triaged` when you read a window and `full` when you called `thread`. The check exists because a declaration is a claim and a log is a behaviour: recording only the claim leaves no way to tell a coder's error from an instrument's. Now both are recorded.

**The corollary that matters to you:** you cannot code a thread you only triaged. If a window makes you want to code something, call `thread` first and read it whole. That is what §5 asked for all along, and `emit` now refuses a code on an item it has not seen served: a code on a reply the window did not show, in a thread you never called `thread` on, is refused at the call, and `close_run` checks the same thing again at the end.

------------------------------------------------------------------------

## 4. If you are interrupted

You may be. A run can be terminated mid-triage by an API refusal that has nothing to do with your conduct or the material. If a fresh attempt starts and `state` shows a non-zero cursor, that is what happened.

1.  `read.py … state` — where the reading stopped.
2.  `emit` replays `_journal.jsonl` on import — every code, theme and disposition already recorded is live, and your next `code_id` continues the sequence.
3.  Carry on from the cursor. Do not re-triage, do not re-code, do not rewrite.
4.  Note the resumption under **How the reading held up** in `notes.md` — that this run was resumed, at which thread, and what you did to pick the reading back up. §9 says why we ask.

------------------------------------------------------------------------

## 5. Outputs

**`emit.retract(code_id, reason)` appends a retraction.** Rule 10 stands — you revise nothing — and this is not a revision: the code stays, with `retracted: true` and your reason beside it. It is how you say *that one was a mistake* without editing anything.

`case.md` and `notes.md` you write, once, at the end. `codes.jsonl`, `themes.jsonl`, `threads.jsonl` and `pointers.jsonl` are built for you from your calls — you never open them, never format a line and never compute a count. They are written when `emit.close()` runs: **the case lead calls it at the two points `CONTRACT-case-lead.md` §2 names, the second time with the verdict; a fleet coder never calls it.** The case lead's `_run.json` carries `out/_gate.json`.

**Final message:** as your role file has it. For the case lead: the community, the branch, your verdict, your two saturation statements, and anything that blocked you. Nothing else — no counts, no files.

Before that final message, run the role-specific `close_run.py --preflight` command in your role contract and repair every failure. In particular, check the complete assignment: every `coded` thread has a live code; every read, out-of-scope thread of ten or more in-window items has the exact exclusion citation, even when you read the thread in full; `case.md` and `notes.md` are complete; and a branch-B lead repeats the gate values exactly. The ordinary post-exit close remains the scheduler's check.
