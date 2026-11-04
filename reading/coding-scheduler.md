# Reading copy: coding-scheduler

Links below are resolved against commit `7c788ae58ce0d4ae171d65e7550cf55b83a22624`. Source wording is unchanged; Markdown formatting may differ. [Exact source bytes](../sources/coding-scheduler.md), SHA-256 `22eb395d7e79a10570846846d68db9ea3a85fad8a411fb1e43fa23d7e58a1952`. [Source and link manifest](manifest.json). Repository links open the public research repository at this commit.

---

# Coding scheduler

The coordinator supports up to twenty rooms at once. The current storage-safe cap is six because a twenty-worker launch exhausted the volume during concurrent archive restoration. New case leads and temporary fleet coders use **GPT-5.6 Sol, medium**. Existing rooms retain the effort recorded in their native lead store, so an in-flight xhigh room remains internally consistent. Changing the coordinator's model does not change those workers. Only case leads retain native sessions and filesystem checkpoints.

`_tools/coding_queue.py` chooses the smallest event-window item count among rooms with a currently passing brief (or an eligible legacy imported brief), breaking ties by subreddit name. The authorised range is 500 through 50,000 items inclusive. It excludes rooms below 500, earlier coder runs, existing runs/stores, failed queue attempts and rooms above 50,000 items. Large rooms require a separate scheduling review. It notices new briefs while work is active and stops when no active or ready rooms remain.

`liverpoolfc` is an explicit recode exception to the earlier-coder-run exclusion. Its older v16 and partial v29 Claude runs do not satisfy the current contract, so the coordinator admits it at its normal smallest-first position based on 8,929 items.

Queued repairs launch before new upward rooms. A repair that is already running only occupies its own worker slot; it does not freeze the other slots. When any worker ends, the coordinator checks that room, records the outcome, archives the case-lead store when verified, then fills the free slot from queued repairs first and otherwise from the smallest ready upward room.

For each room, correct checker failures in the same coder or case-lead session before closing. If that run still fails, preserve it and restart the whole room from the contract. A second consecutive failed run stops that subreddit, records `repair-stopped-after-two-failures`, and requires a progress report. The scheduler must not launch a third consecutive attempt.

BritishColumbia (300 items) and Connery (276 items) were completed during initial validation before the lower-bound guard was encoded. Their preserved runs are scope exceptions and do not count toward completion of the authorised missing-room set.

Each launch uses the existing `start_yard_lead.py --complete` pipeline: first lead checkpoint, serial temporary fleet coders where required, a saved lead checkpoint after the final collection and before consolidation, final verification, then an exact archival mirror into `rooms/<sub>/run/` with validation receipts. Each fleet coder keeps its isolated session only until the authoritative batch check runs. A failed batch check goes back to that same coder for up to two correction turns. An append-only disposition failure first restores the clean dispatched batch, then asks the same coder to redo the slice with its prior reading context. The temporary coder session and clean batch snapshot are deleted after validation. Only the case lead remains forkable. If the final room check fails, the coordinator likewise keeps the original case lead available and sends it the exact checker output for up to two correction turns. The coordinator reruns checkpoint and room validation after each turn. It archives the store only after validation passes or both correction turns fail. Transport failures keep their existing repair path. Failures retain their evidence for review.

The queue can adopt existing room controllers after an interruption. It groups nested controllers by room, checks live process identity, reserves a room before launch, and uses one operating-system lock to prevent duplicate queue drivers. New controllers run in separate process sessions with retained logs, so stopping the queue does not stop their current work. Independent duplicate controllers or unexplained exits pause new launches. Existing stores are never silently restarted.

Runtime state and event history are under `_coding_queue/STATE.json` and `_coding_queue/EVENTS.jsonl`; new controller logs are under `_coding_queue/logs/`. `CODING-PROGRESS.md` lists running rooms and reported completed-run tokens, including cached input. Failed-attempt totals remain separate where recorded.

The `Atlas Yard coding coordinator` heartbeat checks this task every 15 minutes, including newly arriving briefs after the queue becomes idle. It reports new completions or material failures. Before reporting, read `_coding_queue/REPORT-STATE.json`; after reporting newly completed rooms, record their receipt token totals there so later checks do not repeat them.

The external verifier documents one narrow v30 compatibility rule: a fleet slice with no exported or journal codes, matching nonempty all-out-of-scope dispositions, an archived record, and every other close check passed can satisfy E2 when raw C3 is the sole failure. Raw C3 otherwise requires a verdict that fleet coders are forbidden to give. The copied instrument, contract, and research outputs remain unchanged. Buffalo's original failed check and the repair receipt are preserved in its validation directory and `_changes/coding-zero-code-fleet-2026-09-07`.

Read-only inspection: `python3 -B _tools/coding_queue.py --inspect`.

Current user setting: six GPT-5.6 Sol medium rooms at a time, queued repairs first, then untouched rooms ascending by items_in_window. Refill one freed slot immediately after that room finishes and validates; do not wait for the other workers in the batch. Current restart command: `python3 -B _tools/coding_queue.py --parallel 6 --requeue-failed`. Change the cap only on a new user request. The scheduler waits when a launch would breach its 8 GiB free-space floor. The parent needs authorized access to this canonical yard; model workers retain their ordinary workspace sandbox. A second driver exits without launching work. Native lead continuation or forks use the original `_lead_sessions/<sub>-gpt56-calibration-v1` store, not its archival room mirror.

If a Codex turn reports a usage or credit limit, the coordinator records a pause without counting a coding failure or launching the next room. Leave the failed store intact for repair when the user later authorizes resumption. A temporary model-capacity error remains a repairable service interruption, not a token-limit stop.

After diagnosing and resolving a recorded launch pause, `--clear-pause` permits a new launch check; unresolved conditions immediately pause again. This does not erase failed attempts or authorize restarting an existing native store.

A `serverOverloaded` or "Selected model is at capacity" turn is a service interruption, not a failed coding run. Preserve the failed attempt. After confirming the runner and server processes have exited, archive the stale `RUNNING.json` with `codex_lead.py recover-run`, fork the last completed lead checkpoint, and redo the interrupted slice or finish turn. The rejected turn may have changed native history, so do not resume it directly. Do not count this toward the two-run coding limit or change models.

An explicit user stop during drain mode is a pause, not a failed coding run. Stop both the room controller group and any detached Codex coder process, then preserve the partial store as an extraction-tested `.tar.zst` with its SHA-256 in room `STATE.json` and `status.tsv`. Record the pause in `_coding_queue/USER-STOPPED.json`, clear any false failure streak after the coordinator exits, and use a clean completed lead checkpoint when the user later authorizes resumption. Do not resume a partial fleet coder session or launch a replacement during drain mode.
