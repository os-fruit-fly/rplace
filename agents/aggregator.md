---
kind: "handler-brief"
title: "Start from coded communities"
---

# Start from coded communities

Target length: under 750 words. Reading key for the existing Aggregator handler.

## Start here

Open one Aggregator handler chat in Codex or Claude, with shell and folder access. Give it the prompt in the [aggregator guide](../guides/aggregator.md), the instrument version and checked community-output paths. Prepare a new run outside the instrument checkout. Do not operate the shipped historical run.

Obtain the [pristine prepared run](../guides/download.md#get-the-instrument), or use the chosen repository version's `aggregator/input/` with its documented paths. Both are in the public research repository. The pristine archive is a starting filesystem, not a resumable conversation or a complete collection of all source data.

## Required inputs

Provide the census, community coder outputs, versions, collection/coding handoffs and declared context. The handler must check these against the chosen instrument before building. A prepared input table is not proof that every later stage can run.

Write `HANDOFF-aggregator.md` with this preflight table. Use actual paths and results, not assumed readiness:

| Point | Required material | If absent |
|---|---|---|
| Build and A1 | Instrument version, census, checked community outputs and startup context specified by the contract | Do not build or open A1 until the chosen handler's checks pass. |
| C4 | Field package, or the recorded decision allowed by the C4 card | Stop at the C4 boundary and resolve the missing package or decision. |
| D1 close and D3b | Give `out/handoff-D/HANDLER.md`, then `out/handoff-D/recheck/HANDLER.md`, to the chat holding the original community leads. That chat acts as adaptation handler. The PI dispatches the verdict fleet through `dispatch.sh`. | Stop the relevant handoff until its owner, lead packages and brief are confirmed. |
| D2 | Original community sessions, matching saved files, runtime provenance and handler registration | Stop the affected returns. Do not replace original leads with fresh agents. |
| E2 | Proposal/design and feedback materials required by its card | Stop before E2 until the handler has delivered them. |

The interview catalogue shares 14 community coding closes and 14 local-model closes. It does not establish availability of all original leads for the 705-community frame. A read-only interview bundle is not automatic admission to a research continuation. Request any unshared original lead packages from the study owner and verify them through the handler. If they are unavailable, record the limit and the last runnable stage rather than claim a complete reproduction.

## Read in this order

1. [Handler contract](../reading/handler.md), including its own head and memory in the selected run.
2. Choose one handler: [Claude legs](../reading/legs.md) or [Codex](../reading/codex.md). Resolve author-specific example paths to this new study.
3. [Build and run](../reading/how-to-run.md), [contract](../reading/contract.md), [method](../reading/method.md), [standing instructions](../reading/standing.md).
4. [Pinned source and dependency map](../reading/manifest.json), then each stage's reading key and full card.

The reading copies resolve links; exact canonical Markdown remains in `sources/`. Use one version throughout. An instrument/source hash identifies instructions; the historical checkpoint manifest separately identifies saved agent state.

## Check, deliver and advance

Run the chosen handler's build, acceptance and lifecycle checks. Record their versions and outcomes before launching A1. Verify original-lead availability early, even though D2 comes later. The Codex route provides `lead-status` and `register-lead`; use the selected controller's documented registration rules.

Deliver stage cards and startup inputs in order. The aggregator does the analysis; the handler checks deliverables and records the close. Keep the head, decisions and gaps on disk. Use only the prescribed checkpoint boundaries.

## Stop when

Stop at the relevant boundary for a missing input, failed acceptance, incompatible runtime or unmatched native session. Report the exact gap and who can resolve it. Historical publication status is never launch permission. This reading key does not waive scientific rules or change any stage.
