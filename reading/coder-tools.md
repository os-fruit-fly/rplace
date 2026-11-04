# Reading copy: coder-tools

Links below are resolved against commit `7c788ae58ce0d4ae171d65e7550cf55b83a22624`. Source wording is unchanged; Markdown formatting may differ. [Exact source bytes](../sources/coder-tools.md), SHA-256 `345ecc3e886596f9a537b2e1728e0647063edd0854694c53aa0538a3cf17bf70`. [Source and link manifest](manifest.json). Repository links open the public research repository at this commit.

---

# The tools, one way across the tiers

Three agents read this study's material through tools: the brief writer (the seven days before the canvas), the coder (one community's week, or a slice of it), and the aggregator (the coders' cases, codes and notebooks across three hundred communities). Each has a reading tool, a citing tool and a search; a fourth, `emit`, records what the coder decides. This page says what every one of them does the same way, so that an agent that has used one is not surprised by another, and it lists the differences that remain and why. It binds `read.py`, `read_brief.py`, `cite.py` and `emit.py` now; the aggregator's `cite_case.py` and `mem.py` are to be brought to it at v37, and their present differences are listed at the end.

## The shell grammar

    python3 <tool>.py <CORPUS> <verb> [arg] [--flag ...]

`CORPUS` is the file the agent was told is its corpus; the verb comes second; one positional argument at most. `--help` prints the docstring, which lists every verb. Nothing else is positional. A refusal prints one line, `<Error>: <why>`, to stderr and exits 2: `ReadError: no thread 'x' in this corpus`, `CiteError: not found in dfnrqjq. ...`. A refusal is the tool saying the call was wrong, never the tool breaking; a traceback is a defect.

## The reading tools: `read.py` (coder), `read_brief.py` (brief writer)

Both serve the rendered corpus verbatim and log every service. Shared verbs, same meaning:

| verb | serves | logs |
|----|----|----|
| `header` | the block of `#` lines: every count, exact | `kind: header, chars` |
| `thread ID` | one thread, whole | `kind: thread, thread_id, items, chars` |
| `item ID` | one item, verbatim, for what `find` returned | `kind: item, item_id, chars` |
| `state` | where you are: `tool, corpus, threads_in_corpus, threads_served, chars_served`, then the tool's own fields | not logged |

Own verbs, because the two agents ask different questions of the text: the coder asks *does this thread touch the event*, so `read.py` has `windows [n]` (the next n threads as triage windows, or whole when shorter than a window) and `audit` (served against declared); the brief writer asks *what is ordinary here*, so `read_brief.py` has `titles [n] [--day d]` and `sample [n]` (whole threads drawn to fill the thinnest days first). `read.py` has a cursor that advances on serving; `read_brief.py` has a reference budget and a hard ceiling. Those are the differences, and each has its reason in the tool's docstring.

The log is `out/_read.jsonl` beside the corpus for both, one JSON record per service: `{seq, t, kind, tool, chars, ...}` with the verb's own keys as in the table. The log is the record of what the agent saw; it is replayed on construction, so every call is a fresh process and nothing lives in memory. The environment variable `READ_LOG_DIR` moves the log and is the scheduler's, never the agent's: the shell form has no `--out`.

## The citing tool: `cite.py`, the same file in both tiers

    from cite import Corpus
    C = Corpus(RECORD); cite, find = C.cite, C.find
    cite(item_id, "the words you believe are there")   -> {item_id, start, end, text}
    find("regex", limit=200)                            -> FindResult

`cite` searches the item's body (a post: `title + "\n\n" + selftext`), returns the exact span cut from the body with its offsets in Unicode code points, and refuses a quote that is not there, that occurs twice (extend it), or that matches only after normalising quotes and dashes when that match is ambiguous. What the agent typed is discarded; what comes back is the record's. The agent never computes an offset. The shell form is `cite.py RECORD ITEM_ID '<quote>'` and `cite.py RECORD --find '<regex>' [limit]`.

`find` returns a `FindResult`: a list of `{item_id, thread_id, start, end, text, snippet}`, one hit per item, first match only, that also carries `truncated`, `limit`, `scanned` and `not_scanned`; the flag, not the hit count, says whether the scan was complete. Every call is appended to `<record>.queries.jsonl` as `{t, kind: find, tool, pattern, n_items_matched, limit, items_scanned, items_not_scanned, truncated}`. `find` grounds a claim; it does not choose what the agent reads (coder Rule 5; brief writer rule 3 allows it freely because the brief describes rather than samples).

## The recording tool: `emit.py`, coder only

`emit.code`, `emit.pointer` and `emit.thread(excluded_quote=...)` take `cite`'s return value unchanged and verify it against the record at the call; a code or a pointer is refused on an item `read.py` never served. Everything is appended to `out/_journal.jsonl` as `{seq, t, stage, kind, ...}`; nothing is edited. The brief writer records nothing through a tool: its brief is prose, checked afterwards by the scheduler (`verify_room.py --brief`, which resolves every quoted string in the brief through `cite` against the pre-week record).

## What stays different, and why

- The coder's `read.py` serves triage windows and keeps a cursor; the brief writer's serves samples and keeps a budget. Two questions, two tools; the verbs they share behave the same.
- The brief writer has no `emit` and no dispositions: a brief is a description with quotes, and the quotes are checked where they land.
- Neither Layer A tool has `count`: coder Rule 10 says counting is done for the coder in the header, and a brief writer is told the same.

## The aggregator's tools, as they stand (to align at v37)

`cite_case.py` reads the coders' outputs, not a corpus, so its address is `(case, section)` rather than `item_id`:

- `Cases.cite(case, section, quote, collection="cases")` returns `{case, collection, section, start, end, text}`; the coder's returns `{item_id, start, end, text}`. Same rule (verbatim or refuse, ambiguous refused), different address. To align: the same key names for what is shared (`start, end, text`) hold already; the log record should carry `kind: cite` the way the reading tools name their kinds.
- `Cases.find(pattern, collection, section, limit=2000)` returns a `FindResult` with `truncated`; the coder's now does too. The aggregator's hit is `{case, collection, text, snippet}` without offsets; the coder's carries `start, end`. To align: add offsets.
- `Cases.count(pattern, ...)` exists for the aggregator's form pass and has no Layer A counterpart, by design.
- Its log is one file per stage, `out/_aggregator_reads-NN.jsonl`, records `{seq, t, kind, tool, ...}` with `cited: true` on a cite; the Layer A reading tools log to `out/_read.jsonl` and `cite` to `<record>.queries.jsonl`. To align: one log per tool per directory, the same base record, and `kind: cite` rather than a flag.
- Its shell grammar is `cite_case.py ROOT --find PATTERN`, `--count`, `--section CASE NAME`, and a bare `cite_case.py ROOT CASE SECTION QUOTE`; the Layer A grammar is `TOOL CORPUS verb [arg]`. To align: verbs without dashes, one positional argument.
- Errors: `CiteError` raised and, from the shell, a traceback. To align: print and exit 2.
- `mem.py` has no Layer A counterpart (the store is the aggregator's).

The aggregator's v36 run is built and stage 00 has run; these changes wait for v37 so the run's tools stay what its manifest recorded.
