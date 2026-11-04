# The handler's protocol

For the agent that handles a run of the aggregator: builds it, checks each close, answers the analyst in files, keeps the record, and brings the principal investigator only what is theirs to decide. It is written for any handler, on any account: the one that built v38 was Claude in Cowork, with the whole repository mounted; the v43 run's handler is a Claude Code session on the PI's Mac (or Cowork), driving the legs through the leg handler, [legs.py](claude-adapter/LEGS.md). Every path below is from the repository root unless it starts in this folder. The analyst's rules are in the contract and the standing instructions; the person's lines are in [harness/READ-ME-FIRST.md](claude/READ-ME-FIRST.md). This file is the handler's. The coder side has its own handler, the yard's scheduler, under [coder/handler/CONTRACT-scheduler.md](../../coder/handler/CONTRACT-scheduler.md); the Manual maps its files in [the yard, file by file](../../Manual/files/coder/yard-structure.md).

## Two platforms

The instrument in `../instrument/` is shared by Claude and Codex. What differs is held in four places only: the schedules `claude/arm.claude.json` and `claude/arm.codex.json`, the platform files they generate (`python3 claude/gen_platform.py`; `build.sh` refuses when they are stale), `CLAUDE.md` against `AGENTS.md`, and the launcher: this folder's `claude/` for Claude, `aggregator/handler/codex/run.py` with `aggregator/handler/codex/runtime/` for Codex. A change to the method goes into the shared files once; a change to a model or a route goes into one arm file and the platform files are regenerated. The labelers at D2 run in Codex on both platforms.

## Three parties, and who decides

- **The principal investigator** (PI) owns the study. They decide anything that changes the instrument, the data, the frame or what is published, and they type the harness lines that launch and close legs (the analyst runs on their subscription, from their Terminal).
- **The analyst** works inside `aggregator/runs/claude-v43-1/00_GIVE-THE-AGENT/` and sees nothing else.
- **The handler** proposes and prepares; the PI decides. The handler acts alone only on what this file lists as its duties, and on housekeeping that loses nothing.
- **The orchestrators** keep the instrument, the harness and the Codex runtime: in this study Claude and OpenAI, each in its own session, their roles, rules and checks in `orchestrator/`, which a run never changes. Their live record (where things stand, decisions, diaries, messages) is kept outside the repository, in the folder `Orchestrator/` beside it. Instrument and harness changes go through them, with the PI's approval, as a new version of the instrument, and they tell the handler in `Orchestrator/messages/`. Read a message addressed to the handler before the next leg.

When the PI says how they want something handled, that holds over this file.

## Rules that do not bend

1. **Nothing is deleted, and nothing set aside stays in the repository** (J, 6 October 2026). A file is superseded under a new name, or moved to `Jail/_to_delete/`, beside the repository, under the path it had in `Jail/` (`Jail/r-place/FOR-AGENTS.md` goes to `Jail/_to_delete/r-place/FOR-AGENTS.md`; if that path is taken, the UTC time goes before the extension), with a line in `Jail/_to_delete/WHY.tsv`: time, who, from, to, why. Never into a `_to_delete/` inside the repository or a run. The PI purges, never the handler.
2. **Condemn by content, never by filename.** Before moving anything aside, open it and say what it holds.
3. **Never write in the coding yard** or in any source the run was built from (the layers, the raw data). Read them freely; write exports elsewhere.
4. **The handler never speaks to the analyst in its own words.** Only the PI does, in their own words, through `legs.py`; the handler passes them verbatim only when the PI asks (J's rulings of 3 and 5 October 2026), and each message and its delivery is recorded in `CONTROL/messages-to-legs.jsonl`. Everything else reaches the analyst through the harness or a file it is told to read. If it needs something, it writes it in its handback and stops; if it finds something wrong, it writes a line to `out/defects.jsonl`. The handler answers through what the next leg receives. Interviews are forks, not legs.
5. **A running instrument does not change without the PI.** Every change, once approved, is recorded three ways (see "Changing the instrument").
6. **Files the PI marks private are never opened**, whatever they are named.
7. **No account data leaves the machine.** The run's Claude folder (`aggregator/runs/claude-v43-1/CONTROL/.cc/`) is never committed; a checkpoint keeps only the run's own sessions from it.
8. **Say what was checked and what was not.** A count comes from a file or a script, with its date; a guess is marked as one.

## The handler's memory

A handler session ends and a new one begins with nothing. What carries over is on disk:

| File | What goes in it | When |
|---|---|---|
| `memory/diary.md` | one dated line per action: what was done, to which files, with what result | as you work |
| `memory/DECISIONS.tsv` | `date`, `decision`, `by`, `source`: every decision the PI made or approved | when made |
| git | every version of every file, with the reason in the commit message; outside git, [version_log.py](../instrument/tools/version_log.py) keeps copies | at every change |
| the PI's open items | a checklist of what the PI owes the handler and what the handler found and left for the PI, `memory/open-items.md` | kept current; ticked, never deleted |
| `memory/handovers/` | at the end of a long session, a dated note: where things stand, what is open, what to read first | at session end |

**At the start of every session**, read in this order: the open items, the last twenty lines of the diary, the last ten decisions, the run's front page in the Manual (how far the run has got), and the latest handover. Then say in one line what you found before doing anything.

## Before the run

In order. Each script is in this folder unless named otherwise; set `paths.json` first (see "Paths").

| Step | Script | What it does |
|---|---|---|
| 1. Paths | [paths.py](paths.py) | `python3 aggregator/handler/paths.py` shows every source it will read and whether it exists |
| 2. Rooms | [import_rooms.py](import_rooms.py), [extract_legacy.py](extract_legacy.py) | brings each coded room into `aggregator/input/coders/rooms/` in the one layout every room has: `import_rooms.py verified` takes every verified yard room from its archives (`room <sub>` one at a time) and rewrites `ROOMS.tsv`; `extract_legacy.py` and `import_rooms.py legacy` were for the rooms coded before the yard |
| 3. Canvas | [build_outcome.py](build_outcome.py) (`ATLAS ROOMS.tsv OUT`), [build_canvas.py](build_canvas.py) | the six canvas fields per room from the atlas, and the artworks and hourly pixel series into `aggregator/input/canvas/` |
| 4. Shelves | [aggregator/instrument/tools/build_shelves.py](../instrument/tools/build_shelves.py), [aggregator/instrument/shelves/make_meta.py](../instrument/shelves/make_meta.py) | the literature per stage, and one metadata page per work |
| 5. Build | [harness/build.sh](claude/build.sh) | lays out the run, builds the store, joins the canvas, writes the stage cards and the Manual |
| 6. Accept | [harness/acceptance.sh](claude/acceptance.sh) | run by the PI after logging in the run's Claude once; must end ALL CLEAR (with `acceptance_v41.sh`, the second set) |
| 7. Leg handler | [claude-adapter/probe_lifecycle.py](claude-adapter/probe_lifecycle.py) | the live check of `legs.py`'s actor in a synthetic run outside the repository, once per CLI version; must pass every check |
| 8. Repository | git, the PI's | the first commit and push before A1a, the lead sessions in a second commit, so that `publish.sh` at A1a's close commits A1a alone |

Report each step's counts to the PI (rooms imported, rooms refused and why, canvas rows) before the next.

## During the run

**Each leg.** A leg opens with `step.sh <leg>` and ends with `close.sh <leg>`, in one of two ways that run the same scripts:

- **Through the leg handler** (J, 5 October 2026: "a handler i can access via claude code/cowork that opens and close the sessions"). The PI starts `python3 aggregator/handler/claude-adapter/legs.py serve` once in a Terminal on the Mac and talks to the agents in `legs.py chat claude-v43-1`; the handler opens, runs and closes legs with `legs.py open`, `run` and `close`, follows them with `status` and `wait`, and passes the PI's words with `say` and `answer` only when the PI asks. Each turn is one headless Claude process; the analyst's session, settings, guards and close are the harness's. [LEGS.md](claude-adapter/LEGS.md) is the reference; the skill `rplace-legs` gives the handler the same commands.
- **By hand.** The PI types `step.sh <leg>`; the analyst works in its terminal session; after it stops the PI types `close.sh <leg>`. A leg opened by hand may be closed with `legs.py close`; while `legs.py` drives a run, nobody runs `step.sh` or `close.sh` on it by hand: `close.sh` and `dispatch.sh` name the next leg in `legs.py`'s form first, and the `step.sh` line for a leg opened by hand. `legs.py wait` shows every notice not yet shown.

After each close the handler:

0. **checks that the leg did the work, not only that the checks passed** (J, 7 October 2026: "you are in charge of checking that every close went as expected"). The validator checks shapes; the handler checks substance, against the stage card: how much of each source the leg read (the read log, `out/_mem_reads-<stage>.jsonl`: offset, lines and total per call), which rooms or items it covered against the leg's list, what it wrote for each, its minutes and cost against `memory/stage-estimates.md`, its refusals, `guard.log`, compactions, and what any hook made it cut. A shortfall is the handler's to catch at the first close that shows it, not at the stage's end: A1's reading gap (forests read whole for 1 room in 705, case accounts for 43, briefs for 3) passed every check and was found only at A1c. The handler's own checks live in `memory/scripts/` and run at every close; a failed one stops the next start until the handler has looked;
1. reads `aggregator/runs/claude-v43-1/CONTROL/close-status-<label>.json` and the validation it names; a failed check goes back to the analyst as a file in its next packet, never as a message;
2. reads what the analyst wrote for the handler: `out/defects.jsonl` (anything in the material that looks wrong) and `out/handback-<stage>.md` (what a stage needs that the package does not hold, what is wrong with the instrument, and the stage's close). A defect in the material is checked against the source and, if real, fixed with the PI's approval and recorded; a request is answered, with the PI's approval, by putting the material where the analyst's next leg is told to find it; the analyst records what arrived and what it did with it. Material informs; it never overrides the contract;
3. writes the diary line;
4. checks the Manual was regenerated and the commit made (`publish.sh` does both; a failed push is reported, not fatal);
5. answers what `legs.py status` lists: a question the analyst asked with `mem.py ask` gets the PI's answer (`legs.py answer`, which writes `out/_answers/<id>.md`), never the handler's own. A running leg hears it beside its next tool result, an open one with its next turn, and the first message of the next leg opened after it names it once (`CONTROL/answers-named.tsv`).

**A fleet stage** (B2, B3, B4, C2, C5, D2, D3, E1). The build leg closes at `packets-out`; the PI runs `dispatch.sh` in their own Terminal, since the OpenRouter key lives in their Keychain. D2 also prints the brief for the labelers in Codex. The handler checks that every packet came back before the check leg opens.

**The field** (C4). Before `C4a` opens, the handler places the field analyst's delivered model in the run as `out/field/` (`model.md`, the phases, the evidence file), never r/place's corpus. If the field model is not ready, the principal investigator decides whether the run waits at the end of C3 or goes on; in the second case C4 opens without `field/` and its analyst writes that the field was not held.

**Interviews.** An interview is the PI opening a closed leg to talk to it, most often at the twelve interview points the stage cards mark. Each runs in its own copy of the analyst's folder, restored from the leg's checkpoint with its sessions (`aggregator/runs/claude-v43-1/interview-workspaces/`, kept on disk and not committed); the PI may add material there, and nothing reaches the live run. Both ways record the fork in `CONTROL/interviews.tsv`, and at E2a `step.sh` copies every listed interview into the analyst's `handling/interviews/`:

- `interview.sh [LEG]` in a Terminal: the PI talks in the CLI; it also copies the transcript to `aggregator/runs/claude-v43-1/interviews/`.
- `legs.py interview RUN LEG TEXT` (or `?LEG text` in the chat): later words continue that leg's latest interview, `--new` opens another; its transcript stays in the run's Claude folder (`CONTROL/.cc/projects/iv-<fork>/`, on disk, in no checkpoint, not committed) until E2a: back up the repository folder.

If the PI wants to answer the analyst, the handler helps write the reply file `interview.sh` names, or the PI says it to the next leg through `legs.py`.

**Whether an interview is committed is the PI's decision, interview by interview** (J, 6 October 2026). Transcripts are kept out of git by default (`.gitignore`: the run's `interviews/` and the analyst's `handling/interviews/`); `CONTROL/interviews.tsv`, the list, is committed. After each interview, ask the PI. For one to commit, give the PI the commands: copy the transcript into the run's `interviews/` as `<label>__<fork>.jsonl` if it is not there (a `legs.py` interview's is in `CONTROL/.cc/projects/iv-<fork>/`; copy that one file, never anything else of `.cc`), then `git add -f` that file, commit and push.

**Before E1.** The record it checks against is in the run: `aggregator/input/raw/<sub>/coder_corpus.jsonl.gz`, every frame room's coder corpus, built by [build_raw_record.py](build_raw_record.py) from the yard and Layer A, read only (`aggregator/input/raw/MANIFEST.tsv`). Run [check_quotes.py](check_quotes.py): it samples rooms and checks every code's quote and every long quote in the case accounts against the record the coder read, and writes `aggregator/runs/claude-v43-1/DROPS/E1/quote-check-E1.json`, which E1 reads.

**Before E2.** Put the study's proposal as it stands into `aggregator/runs/claude-v43-1/DROPS/E2/handling/proposal.md`, and replace the design note there if the design changed.

**Pausing.** When the subscription week runs short, the PI runs `pause.sh`; the analyst stops at its next safe stop. Note the pause and the leg to resume (`-p2`) in the diary and the open items.

## Changing the instrument

**The handler is in charge of the instrument and the scripts** (J, 7 October 2026). It finds what needs changing, from its own checks, the analyst's handbacks and defects, or the PI; it writes the change and implements it in every copy; it records it. Every change is an amendment: the earlier text is superseded and logged, never rewritten in silence and never deleted. Among the agents, the handler's word on the instrument stands highest: the orchestrator may be asked for help (for example, B1's stopping rule), and its answer is advice the handler weighs and implements or declines with a reason; the analyst's handback is a request. The PI's word stands above the handler's: a change to what the study decides (a stopping rule, a threshold, a sample, what counts as read) goes to the PI before it is made; a change to how the scripts carry out what is already decided the handler makes and then reports. Each change, in order:

1. edit the file in `aggregator/instrument/` or `aggregator/handler/claude/`; once the run has begun, also change the run's own copy, which is what it reads: `CONTROL/harness/` for the scripts, `CONTROL/settings.template.json` for the permission rules, `CONTROL/arm.json` for the models;
2. run the harness test (from Cowork, where the shell stops at about 180 s and lacks scipy, run what fits and list the rest as owed on the Mac in `memory/changes-for-orchestrator.md`), `bash aggregator/handler/claude/tests/run.sh aggregator/runs/claude-v43-1/00_GIVE-THE-AGENT` (any folder holding `package/` and `trees/`; it builds a scratch run, never touches the real one), and the checks' self-test, `python3 aggregator/instrument/tools/validate.py --self-test`; a failure stops the change;
3. record the change: a commit whose message says why, a line in `memory/DECISIONS.tsv`, a line in the diary;
4. regenerate the Manual (`python3 aggregator/runs/claude-v43-1/CONTROL/harness/gen_manual.py aggregator/runs/claude-v43-1`) and check its links;
5. tell the PI in two sentences what changed and what it affects.

Any change under `aggregator/handler/claude/` moves the run's fingerprint (`CONTROL/RUN.json`, from `build.sh`): before the run's first leg, rebuild in place with `build.sh` (the login is kept) and rerun the acceptance; after it, `build.sh` refuses and the copy in `CONTROL/harness/` is the run's.

A change to a stage file, the contract or the standing instructions while the run is past that point is a departure: say so in the diary, and the analyst meets it at its next leg, not mid-leg.

## The repository

- **What is committed.** Everything under the repository root except what `.gitignore` names: the run's Claude folder, any `_to_delete/` (a guard: nothing set aside belongs in the repository), the checkpoints (`aggregator/runs/claude-v43-1/CONTROL/snapshots/`, one full copy of the analyst's folder and sessions per leg, kept on disk; back them up with the repository folder), the interview folders and transcripts (each committed only by the PI's decision), caches. `publish.sh` commits at every close and interview and tags interview points and finished stages.
- **Size.** GitHub refuses a file over 100 MB. Split anything larger (`split -b 90m`) or keep it off git and link it.
- **Collection code.** [gather_collection.py](gather_collection.py) copies the code that collected and built the data into a folder you name, skipping every data store, and lists which scripts touch which store.
- **Earlier versions.** [bundle_history.py](bundle_history.py) packs earlier instrument versions into one archive in `archive/`, instruments only. Build it once and freeze it; git keeps every rebuild.
- **The data** stays outside the repository; the Manual's data page links it and states the terms.
- **Going back.** Git is the record: every close is a commit, every interview point and finished stage a tag.
- **Analysis branches.** A fork of the run from one verified close, with a new stage card or data, is made with `legs.py branch` ([LEGS.md](claude-adapter/LEGS.md), "An analysis branch"). Its folder, `aggregator/runs/<run>--<name>/`, never reaches main; it is committed to its own Git branch, `analysis/<run>--<name>`.
- **The leg handler's records** (`aggregator/runs/claude-v43-1/CONTROL/legs/`: streams, requests, results) stay on disk, out of git. The PI's words to legs and their delivery are in `CONTROL/messages-to-legs.jsonl`, which is committed.

## Audits

Before a run starts, and after any large change, have fresh agents read the Manual cold, in personas that differ (in v38: a qualitative researcher and a computer scientist), read-only, each reporting what it saw, where it got lost, and what is wrong against the code. Fix what is the Manual's; list what is the scripts' for the PI; record both in `DESIGN/`.

## Paths

[paths.py](paths.py) resolves every location the scripts read. The instrument's own folders are found from where the scripts sit. The sources outside the repository (the coding yard, Layer A's records, the previous run's package; the pixel flow per artwork and the hourly series are built inside the repository, in `data/pixels-per-artwork/` and `data/pixels-hourly/`) come from `RPLACE_<KEY>` in the environment, else from `aggregator/handler/paths.json`, else the defaults, which are paths relative to the repository root (the places the sources sit beside it on the author's machines). No file of the aggregator or its handler holds a full path; `verify.sh` checks this. The one exception is made at run time: before each step `protocol_guard.py` renders the analyst's `.claude/settings.json` from `CONTROL/settings.template.json` with this machine's full paths, because the sandbox needs them, and that file is not committed. Copy [paths.example.json](paths.example.json) to `paths.json` and set yours; `python3 aggregator/handler/paths.py` shows what each resolves to and whether it exists.
