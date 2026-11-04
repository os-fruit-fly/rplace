# The leg handler (legs.py)

Target length: under 1,800 words. As it stands on 6 October 2026, before the first research leg.

Status, 6 October 2026: offline tests pass (handler 14 of 14, adapter 20 of 20); the live check `probe_lifecycle.py` passed 14 of 14 on J's Mac (claude 2.1.289); no research leg has run through it yet. A branch replaces its own `publish.sh` and `step.sh` (below).

J, 2026-10-05: "I need just a handler i can access via claude code/cowork that opens and close the sessions plus the ability to talk to EACH AGGREGATOR STAGE.LEG". No website.

## What it is

- One process on the Mac, `legs.py serve`, owns the analyst's sessions.
- Every other command is a client, the same from Terminal, Claude Code (on the Mac, or from the phone through Remote Control) and Cowork. It writes a request into the run's `CONTROL/legs/requests/` and reads the answer in `CONTROL/legs/results/`.
- The run's harness does the work: `step.sh --prepare`, one headless turn (`actor.py`), then `close.sh`, as when you type them.

## Start it once

In Terminal, in the repository folder:

```
python3 aggregator/handler/claude-adapter/legs.py serve
```

Leave the window open; the Mac stays awake. Ctrl-C stops the handler, not a turn: the next `serve` follows the turn again and pauses the list. Beside it: a Terminal window with `legs.py chat claude-v43-1`, where you talk to the agents, and Claude Code as the handler for the rest.

## Commands

| Command | What it does |
|---|---|
| `status [RUN]` | the list, running legs, questions, what needs you |
| `legs RUN` | every leg, its state and its interviews |
| `open RUN LEG` | `step.sh`, then the leg's first turn |
| `close RUN LEG [--force]` | `close.sh`, once, also for a leg opened in Terminal |
| `run RUN LEGS... [--through-interviews] [--accept LABEL]` | several legs in order (below) |
| `stop RUN [--now]` | the list stops after this leg; `--now` interrupts the turn |
| `pause RUN` | the running leg stops at its next safe stop (`done.sh --pause`) |
| `chat RUN [--full]` | one Terminal window to talk to every agent of the run (below) |
| `say RUN LEG TEXT` | one line to a leg, without the chat; TEXT `-` reads standard input |
| `interview RUN LEG TEXT [--new]` | an interview of a closed leg (below) |
| `note RUN TEXT` | the handler's line in the chat |
| `reply RUN LEG [--interview]` | the leg's last reply, or its interview's |
| `watch RUN [LEG] [-f] [--full]` | the analyst's words and tool calls; `-f` live, leg after leg; `--full` whole, with every output |
| `answer RUN QID TEXT` | answer a `mem.py ask` question: beside the running leg's next tool result, an open leg's next turn, and in any case the next leg's first message |
| `wait RUN [--timeout S]` | at once with every notice you have not seen through `wait`, else when one comes, or after S seconds (default 540) |
| `branch`, `branch-put`, `branch-status`, `prepare-branch`, `publish-branch` | an analysis branch (below) |

RUN is the run's folder name (`claude-v43-1`); LEG a leg id (`A1b-02`) or label (`A1.A1b-02`). `open` leaves the close to you; `run RUN A1a` closes one leg by itself. `--wait S` bounds how long `open`, `close`, `say` and `interview` wait; `wait` takes `--timeout S`. Cowork's shell stops after about three minutes, so it passes `--wait 150` or `--timeout 150` and reads the rest with `status` or `reply`. `wait` shows every notice not yet shown.

## Talking to a leg

Talk in one window, apart from the handler: `legs.py chat claude-v43-1` in Terminal (J, 2026-10-05: "a single chat where I talk to all the agents"). A line goes to the leg the prompt names; `@A1b-02 text` goes to that leg and keeps it; `?A1a text` goes to an interview of A1a, and `?A1a+ text` opens a new one. Every agent's words, tool calls and answers come back there live, each marked with its leg, and the handler's notices between them. `/tools` and `/full` show less or more. What a line to a leg does depends on the leg:

- **Its turn runs.** Your words reach the analyst beside its next tool result, with a receipt.
- **It is open and its turn has ended.** Your words start a new turn in the leg's own session.
- **It is the last close.** Its conversation goes on in the next leg, so the next leg gets your words: live or in a new turn when it is open, else in its first message, after the leg's own. Words that missed a closing leg's turn go there too.
- **It is an older close.** Refused: the run has moved on. Talk to it as it was in an interview.

An interview is you opening a closed leg to talk to it (J, 2026-10-05: "an interview is me, asking to open leg/stage x and talking to it"): a fork of its checkpoint in a copy of its folder, recorded in `CONTROL/interviews.tsv`. It remembers the leg; nothing said there reaches the run. Later words continue the leg's latest interview; `--new` opens another. At E2a, `step.sh` copies the listed interviews into the analyst's `handling/interviews/`; only the interviews you open count. A transcript is committed only if you decide so, interview by interview (HANDLER.md).

Your words to a leg, and their delivery, go into the run's `CONTROL/messages-to-legs.jsonl`, which `publish.sh` commits at every close. A message has at most 8,000 characters; send a longer one in parts.

## A list of legs

`legs.py run claude-v43-1 A1` runs A1a, one A1b leg per block declared in `out/order-A1.txt`, then A1c. Other repeated steps take a range (`B1b-01..B1b-06`). A closed leg is skipped and a paused one continues as `-p2`, so naming the same list again picks up where it stopped. A closed leg is skipped only if its snapshot verifies and its close can advance the run; a forced or incomplete close stops the list again until you name it with `--accept`.

It stops, and `status` and `wait` say why and what to do, when:
- `step.sh` refuses a leg;
- a turn fails, is interrupted, or is `uncertain` (it ended while another owner held the run's lock; opening the leg again finishes it);
- the analyst ends its turn without closing the leg;
- `close.sh` refuses;
- a leg closes at a pause, at its packets (you run the dispatch in Terminal), or at an interview point (unless `--through-interviews`);
- a close cannot advance the run (forced, or validation incomplete);
- a stage finishes before the listed legs run out;
- you stop it;
- the list ends.

A question the analyst asks does not stop the list: you are told, and you answer it.

## An analysis branch

J, 2026-10-05: fork a run and do a new C2 with all else equal, from a new card and files, the fork plain in Git. `branches.py` makes branches as the Codex controller does: the same verbs, records, rules, notice and Git refs.

```
legs.py branch claude-v43-1 C1a-03 claude-v43-1--C2-1 --leg C2a-01
legs.py branch-put claude-v43-1--C2-1 stages/STAGE-C2-model-the-loop.md --file NEW.md --stage C2
legs.py branch-put claude-v43-1--C2-1 shelves/NAME.csv --file NAME.csv --stage C2
legs.py prepare-branch claude-v43-1--C2-1
legs.py run claude-v43-1--C2-1 C2a-01
```

- `branch` builds `aggregator/runs/claude-v43-1--C2-1/` from one verified close (C1's last, say `C1a-03`). The run comes as `publish.sh` committed it at that close, checked against the close's archives; the analyst's folder and sessions come from the checkpoint. Nothing later comes along. The first leg must come right after the close.
- `branch-put`, while the branch is a draft, replaces a stage's card (same file name) or adds data (`package`, `trees`, `shelves`, `handling`, `attachments`), never code. A stage already handed changes in the analyst's folder too. `BRANCH.json` records each change with both hashes. Supply E2's `handling` files now: a branch's drops never change after it is made.
- `prepare-branch` seals the branch and commits its setup to the Git branch `analysis/claude-v43-1--C2-1`, whose parent is the close's commit on main (tagged `analysis-checkpoints/<id>`). It pushes when a remote is set, and prepares the first leg without starting it.
- The first leg continues the close's conversation. Its first message starts with Codex's notice: a branch, and what changed.
- Each later close is committed there as "Analysis RUN: verified LEG". Main never holds the branch (`.gitignore`: `aggregator/runs/*--*/`). A close not committed, or not pushed while a remote is set, stops the next leg until `publish-branch`.
- `git log --graph main analysis/claude-v43-1--C2-1` shows the fork. `git diff <fork commit> analysis/claude-v43-1--C2-1` shows the new card, the data and every leg after.
- The parent's interviews stay with the parent: their rows move from `interviews.tsv` to `BRANCH.json`, and a branch never publishes an interview. Its harness, arms and settings template are frozen like its drops, with their modes.
- The branch has its own Claude folder: log in once (`branch` prints the command). Run its legs through `legs.py`: its `step.sh` refuses the first leg from Terminal.

## From the phone, from Cowork

- **Phone.** On the Mac: `claude --remote-control "r/place handler"` in the repository folder. In the Claude app, that session runs the commands, or waits on `legs.py wait RUN` and tells you. The chat window stays on the Mac.
- **Cowork.** Its shell reaches the Jail folder, not the Mac's programs: it runs the same commands, and `serve` does the work.

## Where things are kept

- The run's `CONTROL/legs/`: `legs.json`, `job.json`, `events.log`, `needs-you.json`, `actors/<id>/` (each session's stream, events and inbox), `requests/`, `results/`. The analyst's settings deny it `CONTROL`; `.gitignore` keeps it out of git (added 2026-10-05).
- Beside the repository, `.rplace-claude-legs/` holds the heartbeat, lock and key.

## Not verified

- The adapter's items (README).
- That the analyst's sandbox cannot write `CONTROL/legs/`, while the hook can.
- That a headless turn compacts its context as a terminal leg does, with the after-compaction hook. A long leg depends on it.
- That Cowork's clock and the Mac's agree.

## Before the first real leg

1. `probe_lifecycle.py` passes on the Mac (README, Live acceptance): done on 6 October; again after a CLI update.
2. The run's `acceptance.sh` and `acceptance_v41.sh` end ALL CLEAR after the last change to its `CONTROL/harness/`.
3. The repository's first commit and push.
4. Start `serve` and, at the Mac, run A1a through it. A headless turn passes `--settings` with the inbox hook only; the run's own settings still applied in the probe (its `dontAsk` turn ran Bash under the run's allow rules), but that the run's guard hook fires in a headless turn is not yet seen. A refusal in A1a shows in `out/_closes/guard.log`.

**Fast mode** (J, 9 October 2026). `fast-mode.json` beside `actor.py` switches the analyst's fast mode: with `{"fastMode": true}`, each headless turn's `--settings` carries `"fastMode": true` (a `-p` session takes `/fast` only that way). It is read at each turn's launch; set it to false to turn fast mode off from the next turn. Fast mode is billed from usage credits, outside the plan's limits.
