# Snapshot policy for cases and r/place

Target length: under 220 words. J's ruling, 2026-10-08T19:57Z.

One resumable snapshot per completed major stage. No snapshots per leg, slice, tool action, model pass or worker handoff. Global aggregator policy stays separate and unchanged.

- Case models: R1, R2, R3, R4, R5 and R6.
- r/place: F0, FA, FB, FC, FD, R3, R4, R5 and R6. Its F0/FC/FD snapshots also carry the names after-fleet/after-placement/coding-closed; no duplicate snapshot for an alias.
- Original source and naming/model-transition checkpoints remain inputs.
- Each stage snapshot binds the same native session, workspace, instructions, runtime, model/effort and controller position.
- Fleet execution remains serial. Ordinary workers retain checked outputs, transcripts and audit provenance; they need no permanent resumable package.
- Head, diary, live working files and compact journals continue within stages. Their presence does not require a new full snapshot.
- A before-critic or per-leg snapshot is no longer mandatory for these siblings. Retain critic returns so accepted review is not silently lost or repeated.

Status: implemented in release development/speed-retention-20261008, source ffafd23b. Field's stopped lead is amended; Coder has adopted the release for future cases. Existing pilot archives and controllers remain. Internal hash receipts are not restorable. Recovery across accepted post-milestone worker or critic results stops for handler reconciliation instead of silently discarding or repeating them. Original decision: Orchestrator/messages/2026-10-08T19-57Z_from-openai_to-field-coder-and-claude_stage-milestones-only.md.
