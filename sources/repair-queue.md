# Repair queue restart rules

Date: 2026-09-09

These rules govern `_tools/repair_queue.py` and the repair monitor for this moved yard.

## Goal

Keep six repair workers active when possible. The queue is not a batch barrier: when one worker
ends, the coordinator checks that room, records the outcome, archives the ended case-lead store,
updates status files, and starts the next smallest unresolved subreddit into the free slot.

## Scope

Use only the fixed unresolved repair pool in this yard. Do not start the broad coding queue. Do
not start sub-500 rooms outside the already authorised repair pool. New workers use
`gpt-5.6-sol`, medium. Existing live workers keep the model and effort already recorded in their
store.

## Ordering

Always sort unresolved rooms by `items_in_window`, then subreddit name. Remove rooms already in
`completed`, `failed`, or `active` from the launch queue before adopting or restarting. A failed
room may be retried only through an explicit repair pass or a targeted manual fix; the slot refill
should move to the next queued room instead of looping on the same failed room.

## Ended worker protocol

For each ended worker:

1. Read `rooms/<sub>/STATE.json`.
2. If `coding_status` is `verified` and `validation/RUN-RECEIPT.json` exists, record the token
   total and archive hash as completed.
3. Otherwise record `needs-attention` with the current room status, log path, and archive hash.
4. Run the yard status refresh and coding progress refresh.
5. Fill the free slot from the next queued room unless `STOP_AFTER_ACTIVE.json` exists.

The coordinator must not exit because one reconciliation step fails. If a status read, archive
read, or refresh command fails, record that room as `needs-attention` with the reconciliation
error and continue with the next room.

## Storage

After every ended attempt, keep only the compressed forkable case-lead store when archive
verification succeeds. The uncompressed `_lead_sessions/<sub>-gpt56-calibration-v1/` directory
should be absent for ended attempts. Store the SHA-256 in both the room state and `STATUS.tsv`.
Never delete an uncompressed store for a genuinely live worker.

## Moved yard rules

The live yard is:

`~/Obsidian/Research/Claude/rPlace/Layer A/50_coding_runs/yard_v30`

Repair scripts must derive the yard root from their own `_tools` location. Do not reintroduce
absolute references to `~/Documents/Codex/rplace/atlas_yard` in repair-control code.

Old archived case-lead stores may contain runtime descriptors and checkpoint manifests with the
old path. On restore, update `STORE.json`, `state/runtime.json`, and saved runtime evidence to the
new store and source-room paths. If the native case-lead history cannot fork because a source
rollout is missing after the move, preserve the old archive and start a fresh case lead from the
contract. Do not repeatedly try the broken fork lineage.

## Known repeated repair class

For new coding runs, final close validation is part of the live case-lead cycle. A failed final
room check must be returned to the same case lead with its exact output before the lead store is
archived or a fresh repair is queued. Allow at most two correction turns, and rerun both checkpoint
verification and room validation after each. This rule applies to final lead-output defects. It does
not apply to missing coder output, transport failures, or interrupted native turns. New fleet
coders have their own validation-bounded session: run the authoritative batch check before deleting
that temporary session, return failures to the same coder for at most two correction turns, and
restore the clean dispatched batch first when the check reports an append-only disposition defect.
Delete the temporary coder session and batch snapshot after validation. Do not retain a forkable
session for a fleet coder.

Several fresh or reforked coders still fail C5 by writing malformed `excluded_quote` data. Treat
these as repairable validation failures, not coordinator failures. Record them as
`needs-attention`, archive their stores, and continue to the next queued subreddit. Do not let
that repeated class stall the whole queue.

After Claude's `Coder Comments v1` audit, future new launches should use v32. v32 makes C5 fail at
`emit.thread`, before the bad row is recorded. If a running older store fails C5, do not edit its
copied instrument in place. Preserve the evidence and repair or rerun the room through the queue.


## Coordinator restart checklist

On every restart, first rebuild reality from the filesystem, not from stale memory. Check `_repair_queue/STATE.json`, the live process table, each active room `STATE.json`, and the room `validation/RUN-RECEIPT.json`. A room with `stage: verified` and a receipt is complete even if the queue state still lists the worker as active. A dead worker without verification is `needs-attention`; do not immediately relaunch it unless the user asked for that specific room.

When one slot opens, close exactly that ended worker: validate the room, write the result and token count if available, archive the forkable case-lead store, store the archive SHA-256, remove only the verified uncompressed store, append the queue event, then launch the next smallest unresolved room. Do not wait for the rest of the batch.

Keep the repair pool ordered by `items_in_window`. If a larger room appears before a smaller unresolved room, write why: already running, already finished, already failed in this pass, below the active threshold, missing brief, or blocked by a specific mechanical error.

Use a two-run failure limit per subreddit. First send authoritative closing errors back to the
same live coder or case lead. If the run remains invalid, preserve its archive and restart the
room from the contract. If that clean restart also fails, stop the subreddit, retain both failure
records, and report it. Never refill that subreddit for a third consecutive run without a
deliberate repair change.

For current repair work, use `gpt-5.6-sol` with medium effort for new starts. Preserve already-running model settings. Record model, effort, start time, end state, token count, and archive SHA in `status.tsv` or the queue state so future reports do not depend on chat memory.

## Stop marker

`_repair_queue/STOP_AFTER_ACTIVE.json` means drain only: adopt live workers, reconcile them when
they end, archive stores, and do not launch replacements. Remove or rename this marker only when
the user asks to resume slot-by-slot repair.

If the model service rejects a turn with `serverOverloaded`, treat it as transport failure. Preserve the failed attempt, recover the operation marker only after its processes exit, fork the last completed lead checkpoint, and redo the interrupted slice or finish turn. It does not count as a failed coding run or justify a new model.
