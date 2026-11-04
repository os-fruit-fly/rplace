# Case-lead checkpoints

Only the **case lead** has a persisted native agent session. Brief writers and fleet
coders continue to use the existing workflow. Their completed files and transcripts
are inputs to the lead's filesystem snapshot; their native agent state is not needed.

`_tools/codex_lead.py` is the Codex adapter. `_tools/checkpoints.py` is the local,
content-addressed filesystem store. Neither replaces the research instrument.
The copies in `_instrument/v30` and `rooms/*/instrument` are unchanged.

## Start a room

Finish/check the room's brief first. From the yard directory:

```sh
python3 -B _tools/codex_lead.py --store _lead_sessions/Dorset init \
  --room rooms/Dorset --model gpt-6-astra --effort xhigh
python3 -B _tools/codex_lead.py --store _lead_sessions/Dorset turn \
  --message lead --label lead-first
```

`init` copies the room into `<store>/workspace/room`, then builds its run there.
It never changes the source room or its brief. All subsequent coders, collection,
checks and lead work for this reading must use this managed room, not `rooms/Dorset`.
`init` refuses a source room with an existing run; it does not silently import an old
lead's state. Set the chosen model explicitly. The same model belongs in coder manifests.

The adapter uses the existing Codex file login, borrowed into a private runtime home
for each invocation. The default source is `~/.codex/auth.json`; `--auth-source` can
select another login file. Authentication is removed when the runtime exits and is
excluded from checkpoint objects. A valid login is required when resuming later.

Normally the agent uses Codex's workspace-write sandbox. If the runner is already
inside an enclosing sandbox, such as a Codex desktop tool execution, macOS may refuse
to nest seatbelt. In that specific environment, pass `--host-sandbox` **at init**.
This uses the API's `externalSandbox` mode, relying on the enclosing sandbox's access
restrictions. Never use that flag from an ordinary unsandboxed terminal. It does not
create a per-room security boundary; scope restrictions still come from the contracts
and the host's permissions. No bypass-approvals or danger-full-access flag is used. This Codex version returns its
workspace-write config default on cold resume/fork; the adapter reapplies and verifies
the recorded external policy on every turn before accepting the checkpoint.

## What one turn saves

The runner starts/resumes the native lead, sends the scheduler message, and waits for
`turn/completed` with status `completed`. It verifies a final reply in the native
history, checks that no background terminals remain, shuts down the runtime, and
verifies the persisted rollout's matching `task_complete` marker. It then exports
the complete native history segments (including fork ancestors) as `run/out/_transcript.jsonl`, saves the final reply as
`run/out/final_message.md`, and commits one checkpoint binding:

- the native lead ID, completed turn ID, final reply, and exact native rollout;
- all files under `workspace/` (whole managed room, including state, instrument,
  source records, brief, run, fleet outputs, hidden files and empty directories);
- the isolated native Codex home, including saved history, fork ancestry, configuration and databases;
- runner state and the effective model, effort, sandbox, instruction-source hashes,
  runtime fingerprint, and absolute working directory.

A completed reply can report a problem. A checkpoint is evidence of a restorable
conversation boundary, **not** certification that the reading passed its checks.
Run `_tools/verify_room.py --room <store>/workspace/room` after the lead closes.

Objects are SHA-256 addressed and shared between checkpoints within the store, so
unchanged corpora and fleet outputs are not duplicated on every turn. Manifests and
named references are never overwritten. `HEAD` identifies the last committed state.
Capture scans twice to reject concurrent file changes. Every object is checked before
restore changes any live file. Credentials, logs, runtime tmp files and sockets are
excluded from the native home; workspace content has no such exclusion. Workspace
symlinks and special files fail closed, rather than creating uncaptured dependencies.

## Branch B: existing coders, persistent lead

After the first lead turn, use the managed room's `run/fleet/batch_NN` directory for
the external coder. Save its transcript and final reply and run the existing batch
checks. Native coder sessions are not required. Then:

```sh
python3 -B _tools/codex_lead.py --store _lead_sessions/COMMUNITY turn \
  --message collect --batch 01 --summary 'mechanical check counts' --label collected-01
```

The lead collects and dispatches the next batch. Its session and the whole room are
checkpointed when its reply completes. After the **last** batch, `collect` now tells
the lead to collect, record its remarks, and STOP without consolidating. Give that
turn the label `after-fleet`. This is the saved native fork point.

```sh
python3 -B _tools/codex_lead.py --store _lead_sessions/COMMUNITY turn \
  --message collect --batch NN --summary 'mechanical check counts' --label after-fleet
python3 -B _tools/codex_lead.py --store _lead_sessions/COMMUNITY turn \
  --message finish --batch NN --label lead-closed
```

`finish` assumes the last batch was already collected and does not collect it twice.
Do not start a coder or edit the managed room while a lead turn, capture, fork, or
restore is running. The runner locks out other runner operations on this store;
external coder/scheduler processes must respect this same serial workflow.

## Resume, fork, and switch branches

Use a text file to send an arbitrary follow-up without shell quoting hazards:

```sh
python3 -B _tools/codex_lead.py --store _lead_sessions/Dorset turn \
  --prompt-file follow-up.txt --label next-reply
```

The runtime is a new process on every invocation. This command resumes the saved lead
at its stable directory; it is not a new lead reading a handoff note.

```sh
python3 -B _tools/codex_lead.py --store _lead_sessions/Dorset fork \
  --checkpoint lead-first --name alternative-a
python3 -B _tools/codex_lead.py --store _lead_sessions/Dorset turn \
  --prompt-file follow-up-a.txt --label alternative-a-reply
python3 -B _tools/codex_lead.py --store _lead_sessions/Dorset fork \
  --checkpoint lead-first --name alternative-b
```

`fork` first restores the specified checkpoint. It calls native `thread/fork` through
the recorded completed turn, verifies the inherited final reply and configuration,
and saves the independent native thread without sending a new model message. The
child can remain idle until another day. The parent checkpoint remains immutable.

```sh
python3 -B _tools/codex_lead.py --store _lead_sessions/Dorset restore \
  --checkpoint alternative-a-reply
python3 -B _tools/codex_lead.py --store _lead_sessions/Dorset verify \
  --checkpoint alternative-a-reply
```

Restore materializes the files and native state at the **same absolute paths** used
in the conversation. It does not rewrite history, file paths, contracts, or hash
baselines. Thus branches of one store run serially; separate room stores can run
in parallel. Existing live trees are retained under `displaced/` during a switch.
The checkpoints themselves are deduplicated; these displaced recovery trees are
full copies and can be archived/removed later after verification.

## Recovery and portability

`RUNNING.json` blocks another operation after an interrupted or failed run. Inspect
its audit and process IDs. `recover-run` clears it only once those processes have
exited, preserving the failure record. Then restore a known checkpoint and retry.
No failed/interrupted turn is committed as a successful completed-turn checkpoint.

A filesystem restore stages all incoming files before replacing any live tree and
keeps `RESTORE.json` until verification finishes. After an interruption, `recover`
rolls the partially applied restore back using the retained trees. It does not delete
the displaced work. All runner operations on a managed room share one OS lock.

Back up the **whole store**, including `objects`, `checkpoints`, `refs`, `STORE.json`,
and any evidence you want from `audit`. Preserve the original store path when moving
machines (or use an environment mounted at that exact path). The Codex binary digest,
Python version/executable and OS platform are checked; changed runtimes fail closed.
Keep the matching runtime available and retain a valid account login separately.

The runtime may encode forks as copy-on-write links to ancestor rollouts. The whole
native home is saved, so those links and their history database remain intact. The
instrument transcript is an audit export of the native segments at their recorded
byte boundaries; it is never fed back as replacement model history.

This preserves durable native conversation state and files at completed-turn
boundaries. It does not promise to preserve live processes/REPL memory, machine clock,
remote services, or an unavailable/replaced model. It cannot recover information
already lost to prior compaction. It does not claim literal indistinguishability or
identical future answers. Native resume/fork fields are version-dependent, so the
installed runtime and the restore demonstration must be checked before an upgrade.

## Legacy research forks

`room.py snapshot` and `room.py fork` still implement the earlier **filesystem-only,
fresh-lead** research comparison. They are not native case-lead checkpoints. Their
last-collect/finish/fork messages are now consistent with the pre-consolidation
boundary; snapshot creation refuses an invalid `after-fleet` stage. Legacy forks
reject instrument drift before rewriting allowed paths, rather than adopting every
changed hash as a new baseline. Use the native adapter above for conversational
continuity. Do not send `room.py message fork` to a native fork; that message belongs
to the older fresh-lead comparison.

## Tests

`python3 -B _tools/test_checkpoints.py` covers content restoration, branch independence,
credential exclusion, corruption, immutable labels, deduplication, special-file
rejection, inter-process locking, fixed-path enforcement, interrupted-restore recovery,
and the last-batch boundary. The instrument's existing `selftest.py` and
`selftest_brief.py` remain separate. A real Dorset cold-resume/fork demonstration is
recorded separately, with its native sessions and checkpoint IDs retained in its store.
