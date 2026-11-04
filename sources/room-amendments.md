# Paused-boundary amendments

2026-10-07T20:08Z. Target: under 450 words. Controller operations, not a scientific protocol.

`amend-plan` and `amend-apply` are for an approved change of instrument or controller at an idle boundary. They do not replace interruption recovery. The lead must be ready, PAUSE must exist, the last native turn must be complete, and no owned actor may still be running.

Run from `Jail/community coder` with the managed Python 3.11 and `-B -m sibling_model`. Inspect `--help`; do not use placeholder paths as commands.

`amend-plan JOB` takes `--frozen`, `--previous-source`, `--previous-sha256` and `--declaration-file`. The declaration is JSON with `reason` and an `overrides` list naming each changed provision, including rule 19. The previous source must actually exist and match its hash. The plan binds the current state, complete files, old/new source and build hashes. It starts no native process.

Give J this plan. Approval JSON must contain `origin: J`, `decision: apply`, the exact `plan_sha256`, and J's approval text. Never manufacture this for a research pilot.

`amend-apply JOB` takes `--plan-sha256`, `--approval-file`, `--executable`, `--credential`, `--capacity` and `--slots`. It retains both code/build versions and both cold native/filesystem checkpoints. The native session and transcript stay the same. Tools are disabled in the separate discarded recall probes; a separate grader checks remembered replies. Neither probe is the research agent. The amended workspace is a new owned generation. Original preparation and generation stay intact.

Application keeps PAUSE, clears admission and runs no research turn. The next admitted opening reports what changed. Old-stage checks and judgments are not rewritten or silently repeated. A failed probe or partial preparation leaves the original active. A crash after the commit but before the state switch can finish that switch once, provided the saved generation is unchanged. Partial preparation requires inspection, not automatic retry.

Amendment records and snapshots enter the final archive. Field private-controller files are included. No command edits a yard, alters the native model/runtime, substitutes an agent, commits or pushes.

Current limits: no real pilot has undergone this operation; frozen scientific amendments and full release acceptance are pending. Placement-reader recovery now uses `field-recover --actor reader:REQUEST:AGENT`; it requires an unchanged controller and is not an amendment route. The operation is tested on synthetic room and field files, with live cold recall on one synthetic room session.
