# Stage D2. The return: the labelers in Codex, and the verdict fleet.

**The dispatch and the check leg of the return.** Two things run outside your session, and you are launched only when both have left their files. The adaptation handler runs
one resumed original case lead per room, retaining its Codex history and matching files;
the handoff task is delivered in a separate return folder alongside its original workspace,
without another room's private history, holding the room's coder documents,
`MODEL.md`, `LADDER.md` and `VOCABULARY.json`, and returning `model-D.md` and
`adaptations.jsonl` into `DROPS/D/<sub>/` with `run.json` (the labeler's model and session id);
the handler runs `ingest.py --check <sub>` after each room, has the failing rule repaired, keeps
returning rooms before any limit, marks a room `unreturned` in `DROPS/D/UNRETURNED.tsv` only
when it cannot return it, and writes `DROPS/D/DONE` with the counts. The verdict fleet runs on
the reader route, the dispatch sending packets to the routine readers, from `verdict-D/`, two
readers per room, returning into `_fleet_raw/D2v/` and validated against `RETURN-D2v.md`, with
reissues for what fails the schema; when reissues are exhausted `fleet.py` stops and the
packets are rebuilt (FLEET §1). Neither reads your files. When both have returned, the harness
runs `ingest.py D` and relaunches you for the check leg with one line: the labelers and the
readers left their files.

**Check leg. Model:** as `arm.json` sets. **Steps:** `D2a`, the check, once both the labelers and the verdict fleet have returned. Each leg is named by its step (STANDING §2).

**Safe stops:** after each section of the check leg. At a safe stop, check for `.pause` (`ls .pause`); if it is there, log where to pick up, your working hypothesis and the next room or item
(`mem.py log "<hypothesis>; next: <item>" --kind pause`), and close with `done.sh D2 --pause` (STANDING §2).

**Startup packet:** `_head.md`, this file, `SCHEMA-adaptations.md`,
`FLEET.md`, the last five diary entries, `validate.py --open D2`.

**Reads allowed:** `ingest.py`'s report; `adaptations.jsonl` by count and by the views, never as
a list; `verdicts-D.jsonl`; `_fleet_raw/D2v/`; `DROPS/D/UNRETURNED.tsv` and `DONE`; sampled
`model-D.md` files by query; `prior.md` §8. **Forbidden:** adjudicating a line (that is D3);
editing a return; re-running a labeler or a reader; editing the task template or the criterion
mid-return; `EXPECTATIONS.jsonl` against the ledger (that is stage E1).

**Outputs:** `adaptations.jsonl` (ingested, validated); `verdicts-D.jsonl`; `ingest-D.md`;
`_views/rooms-x-elements.tsv` (generated); `rooms/<sub>/model-D.md` and `verdict-D` copied
from the drops; `notes-D2.md`; the D2 counts in `RUN.json`; a `run_manifest.json` entry for
the labelers' model and the readers' model; `handback-D2.md`.

## 1. What ingest did

`ingest.py D` validated every line against SCHEMA §4: the schema (a known op, its required
fields, no extra fields); the model version against `handoff-D/VERSION`, with element ids in
`VOCABULARY.json` and not withdrawn; concept ids in the room's `codes.jsonl` and not retracted,
transition ids in the room's forest; `how` one sentence under forty words; portability (no
census subreddit name and no proper name from the room's lines in your `lexicon-A1.md` in `condition`,
`statement` or `how`, except in `relation`), a failing line kept with `portable: false` and a
particular by construction; the end marker matching the line count and `model-D.md` ending
with its marker. It lifted every source node through `assignments_final.jsonl` at the model
version (second-order theme, third-order theme, fourth-order theme, dimension, `null` where
never placed), computed `kind` and `portable`, stamped `origin` and `labeler_run`, checked that
every adaptation's element appears in the room model, and compiled the ledger; it reported per
room what failed and why, and the handler reissued what it could. A room with nothing to adapt
returned one `none` line with evidence for the fit; silence is a missing return, not a verdict.

You read `ingest-D.md`: rooms returned, lines accepted, lines flagged by rule, rooms
`unreturned` with the handler's reason, the distribution of lines per room and of ops, the share
of `portable: false`, the share of `none` rooms, the share of unplaced source themes (the lines
D3 may mint from). `ingest.py` wrote the counts of accepted, reissued and unreturned rooms into
`RUN.json` (SCHEMA §4), copied the room models and verdicts beside the notes, and marked every room
it rejected unreturned; check the counts against the report, since stage D4 reconciles every room
against them.

## 2. The verdicts

`verdicts-D.jsonl`: one line per room from the fleet, with each reader's themes, sentence and
`cannot_tell_under`, at `R = 2`; where the two readers differ, the room is listed for D3 to
rule with the criterion in front of it, and the disagreement rate is reported, by verdict pair.
Report `cannot-tell` by threshold (`coded-share`, `off-platform`, `both`), and check each against
the room's concept count and off-platform pointers on the line: one the numbers do not support is
listed for D3 beside the splits. The figure bounds whether the written criterion decides a
room, never whether the model is right (FLEET §2); say so where it appears. The labeler's grade
from `model-D.md` sits beside the verdict in the same file and never replaces it; the
cross-table of grade against verdict is reported here and again at E1.

## 3. What you check by sampling

Ten `model-D.md` files drawn by seed, stratified on verdict: does the room model cite element
ids where the model applies, `[absent <id>]` where it did not apply and was not needed, and
`[new: ...]` where no element covers what the room did; does every adaptation's element appear in
it; does every claim carry a concept citation from the room's own codes; does the prose read as
the room's organizing in the model's words rather than as a summary of the model; does the
grade's sentence name what the ledger names. Every quote you carry into `notes-D2.md` goes
through `cite.py`. What you find goes in `notes-D2.md` and, where it is a defect in the task
template, the return specification or the criterion, in `handback-D2.md` for the operator: none
of the three is edited mid-return, and a labeler is never re-run by you.

## 4. Verbal before numeric

No verdict and no line is revisited because of a count. A share that looks bad (many
`does-not-compose`, many particulars, a thin ledger) is a fact to report; D3 assesses fixed-global fit, local adequacy and shared composition separately against
`prior.md`. Repeated corrections and a sparse ledger alone establish neither failure nor success.

## Moments to log

The ingest report read, with the rule that flagged most lines; the `RUN.json` counts written;
the verdict disagreement rate and the `cannot-tell` lines the numbers do not support; each
sampled room model and what it showed; each defect sent to `handback-D2.md`.

## Final message

Counts: rooms returned, reissued, unreturned, lines accepted and flagged by rule, lines per
room, ops by kind, `none` rooms, non-portable share, unplaced-source share, verdicts by value
with the disagreement rate, `cannot-tell` by threshold, the labeler grade against the fleet
verdict as a cross-table, the labelers' model and the readers' model from the manifest. A return
value.

## Close

`done.sh D2 --cut adaptations-in`: the adaptations and verdicts have arrived and nothing is yet
ruled on them, the moment D3's rulings are measured from; `gen_views.py` builds the element
views and the wiki pages; `handback-D2.md`;
the head; the closing diary line.
