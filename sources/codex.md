# Run r/place with Codex

Guides: [automatic leg blocks](aggregator/handler/codex/BLOCKS.md), [remote access](aggregator/handler/codex/REMOTE.md), [analysis branches and Git lineage](aggregator/handler/codex/BRANCHES.md).

Target length: under 1,250 words. Installation does not start research.

## Start

From Terminal:

```bash
cd "$HOME/Jail"
python3 r-place/aggregator/handler/codex/run.py login
python3 r-place/aggregator/handler/codex/run.py serve
```

Login credentials and runtime state stay in `Jail/.rplace-runtime-v43/` (the folder that holds r-place). The controller prints a private loopback URL. Open it, or open `~/Jail/.rplace-runtime-v43/OPENAI-LIVE.html` while the controller runs. Do not share that URL: it controls the local agents. Closing a browser tab detaches; it does not stop an agent.

The controller owns all native sessions. Start it once. A second controller is refused. Independent studies, readers and interviews may overlap. Two processes cannot own the same actor; conflicting study operations are refused rather than racing.

## Handler and aggregator

Open a separate ordinary Codex chat as the handler and give it [HANDLER-CHAT.md](aggregator/handler/codex/HANDLER-CHAT.md). Keep this instrument-development chat separate. The handler reads state and operates the controller; it does not need a website actor or native checkpoint. Stage and leg agents keep their full native checkpoints.

Prepare a new study from the supplied material:

```bash
python3 r-place/aggregator/handler/codex/run.py build study-01 --fleet-arm codex
python3 r-place/aggregator/handler/codex/run.py status
python3 r-place/aggregator/handler/codex/run.py step study-01 A1a
```

Choose `--fleet-arm openrouter` for the alternative packet reader arm, or select it in the panel. See [two reader arms](FLEET-ARMS.md) for routing, credentials and recovery.

The panel offers stage/step dropdowns, **Prepare leg**, then **Start prepared leg**. Or use `step study-01 A1a --start`, then attach:

```bash
python3 r-place/aggregator/handler/codex/run.py chat ACTOR_ID
```

You can send messages while it works. Terminal `/pause` asks for a safe boundary; `/stop` interrupts and saves; `/save` archives an idle agent; `/quit` detaches. The panel has the same controls. Scientific work stays in `workspace/out/`. Instrument and input files are read-only. Actor scratch is private and excluded from archives; keep durable work in `out/`.

Talk to current analysts and interviews in the panel; the handler stays in its Codex chat. Messages and expandable tools stream live. Consequential questions show a reply form. Nothing is answered automatically. Native replies go to the exact turn. Drafts survive refresh. Terminal: `/answer text`, or `/answer {"question_id":"answer"}` for several questions. Stop interrupts a pending question. Private reasoning is not shown.

## Close and advance

The analyst closes its work with `tools/done.sh`. The controller detects the completed exit and closes it automatically. To retry closure after resolving a reported problem:

```bash
python3 r-place/aggregator/handler/codex/run.py close study-01 ACTOR_ID
```

The controller runs trusted validation and the recall probe, verifies the native boundary, and commits the archive. Failed validation returns to the same actor. A stopped or diagnostic archive does not count as a verified study leg.

A verified `packets-out` cut starts the declared fleet automatically. Each reader has an independent history and files. Multipart packets stay with the same reader. Concurrency defaults to three readers, configured in the study state. D2 labelers and verdicts remain separate jobs. Inspect asynchronous operations with `status` or `job JOB_ID`.

The next leg opens through `step` after its prerequisites pass, forking the preceding native checkpoint with its history and files. Notes orient the continuing actor; they do not replace it. Use `run-block STUDY --first A1b-01 --last A1b-03` for an explicitly approved range, with the actual last leg from the declared plan. The controller prepares and starts each leg after validation, stops at the range boundary or a required decision, and does not conduct the whole study. C4 may record an absent field model as its card permits. E2 requires the proposal and design note in the study's `drops/E2/handling/` folder.

## Resume and interviews

Codex checkpoints bind native history, files and the pinned runtime. Keep each complete folder under `.rplace-runtime-v43/checkpoints/`, including archives, receipts and its COMMITTED marker. Restores preserve the parent and its transcript. OpenRouter readers use API history replay.

Click **Resume as interview** on a checkpoint, or:

```bash
python3 r-place/aggregator/handler/codex/run.py resume CHECKPOINT_ID --actor interview-01
python3 r-place/aggregator/handler/codex/run.py chat interview-01
```

Restore verifies hashes, creates a separate workspace, and forks the saved history using the recorded backend. The parent stays unchanged. Saved paths are mapped to the restored workspace and recorded in the continuation notice. Saving that interview creates another resumable checkpoint with parent lineage. No interview files enter the study without an explicit handoff.

Authentication is excluded. Restoring needs the recorded operating system and architecture, Python 3.11 or later, and access to the recorded model. Archives preserve persisted history and files, not a promise of the same next token. Historical Claude sessions remain historical; they are not converted into native Codex histories.

## Original case leads at D2

D2 restores each original case lead on its recorded model and effort. D3 continues that returned
lead. Both fleet arms use this rule. A new reader cannot substitute for a missing lead.

```bash
python3 r-place/aggregator/handler/codex/run.py lead-status
python3 r-place/aggregator/handler/codex/run.py register-lead SUBREDDIT CHECKPOINT_ID
```

`import-lead` can capture a completed native CLI lead whose home, workspace and runtime are
already inside the workspace (the folder that holds r-place). It requires `--home`, `--workspace`, `--executable`, `--thread`, `--model`
and `--effort`. It preserves original files and verifies the three coded files against the
current case snapshot. Old versions or missing native histories block the return.

The current 705-room dataset is present. Its matching native lead archives still need to be
registered before D2. Run the lead check before committing to the full study. The proposal
and design note are delivered only at E2.

## Models and tests

`aggregator/handler/claude/arm.codex.json` sets exact models and effort by leg. Defaults use Astra for the aggregator and Sol medium for routine fleets. The [per-step schedule](aggregator/instrument/PLATFORM-codex.md) is a pilot allocation, not a measured optimum. The [A1 card](aggregator/instrument/stages/STAGE-A1-reading-room-notes.md) gives the first stage. Do not substitute models silently.

```bash
python3 r-place/aggregator/handler/codex/run.py test
```

Use `stop-run STUDY` to stop the study and prevent pending jobs from starting. `continue-run STUDY` clears an actor-only stop without starting work. `recover DISPATCH_ID` or `recover-plan STUDY` resumes a blocked phase plan, retaining accepted returns and models. New dispatch cannot bypass a blocked plan.

`python3 r-place/aggregator/handler/codex/run.py acceptance --live` runs a small authenticated conversation and two archive/restore interviews. Run it after login before research. `bash r-place/verify.sh` checks the runtime, scientific tests and all 705 prepared room packages. Keep at least 8 GiB free. `prune` verifies committed archives before removing released redundant workspaces. It preserves checkpoint folders, current study files and interrupted stores. Restoring an evicted actor uses its checkpoint. D4 numeric comparison requires NumPy and SciPy in the controller Python environment.

Offline fixtures test lifecycle and concurrency; they do not prove real model continuation. Coordinator records live in `~/Jail/Orchestrator/OpenAI/` and `~/Jail/Orchestrator/HEAD.md`, outside the repository. Reusable checks and protocols stay in the repository's `orchestrator/`. New builds use the [v41 method](aggregator/instrument/METHOD.md) and its stage cards.

## v43 isolation and questions

The v43 controller uses port 8767 and private state in `~/Jail/.rplace-runtime-v43`. Phone ports are 8768 and HTTPS 8444. v42 stays separate. New login is required; startup starts no research.

The default build source is `~/Jail/.rplace-runtime-v43/prepared/openai-v43-1`, a pristine input build, never a copy of research outputs. Prepare it with the reusable check `python3 orchestrator/OpenAI/checks/prepare_v43.py --build`. Inspect the receipt before requesting `build openai-v43-1`.

`mem.py ask` questions appear alongside live questions, with their stated assumptions. Their answers persist in the study and are delivered to later legs. Answering alone never starts a turn. After closure, answers wait outside the immutable saved workspace until the next leg. A reply stops any automatic block for review. Native blocking questions still require their exact live request.

Claude's adapter remains a disabled v44 draft pending live lifecycle acceptance. This panel cannot yet operate a Claude CLI run.
