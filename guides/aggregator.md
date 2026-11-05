# 3. Open the aggregator handler

Open a third Codex or Claude chat. Name it **Aggregator handler** and give it the collection handoff and the coding handler's output locations. Paste:

```text
You are the aggregator handler for my r/place study. Use the existing handler in the research repository Read FOR-AGENTS.md, aggregator/FOR-AGENTS.md and aggregator/handler/HANDLER.md first, including its memory and open items.

Read my collection and coding handoffs. Obtain any missing instrument folders and required inputs, record their versions, and prepare a separate run using the chosen platform's existing controller. Follow its build and acceptance procedure before opening analysis. Keep your head, decisions and progress on disk. Deliver the prescribed stage cards and inputs, check each close, and preserve the declared checkpoints. Bring research decisions and unresolved failures to me. Do not operate the repository's historical run or rewrite its protocol.
```

The aggregator handler already exists. Choose its Claude or Codex route and confirm that route's requirements. The chat coordinates the run; the aggregator works in its own session for each stage or leg.

This step starts from the checked community outputs, the census and the context the instrument requires. The handler prepares a separate run, checks the build and opens the stages in order. The aggregator reads, codes, builds a model, returns it to the cases and writes the resulting account. Keep each stage's outputs, reasoning record and declared checkpoints. Move to the next stage when its outputs and checks meet its contract and the handler records the close.

The aggregator develops the account, and the authors remain responsible for its interpretation. The handler is a separate agent that operates the run and brings decisions to them. A stage card gives the full instructions for one stage; an agent reading key lists what the agent must read. A stage is one part of the analysis, and legs divide its larger tasks.

## Starting from communities already coded

You can open this handler directly with checked coded inputs; no new collection is needed. Use the agent reading key, under Documents for this handler, to list the inputs and boundaries before launch. It covers the untouched starting folder, the original community coders for D2, the Field package or the recorded decision for C4, and the proposal material for E2.

The 12 shared community checkpoint pairs do not include every original community coder of the 705-community frame. Missing community coders limit the later returns, even when the earlier aggregator stages can run. The handler requests the missing packages, records the last stage that can run, and never replaces a saved community coder with a fresh agent.

## Return the model to communities

At the D1 close, give `out/handoff-D/HANDLER.md` to the chat that holds the original community coders. That chat acts as the adaptation handler. At D3b, give it `out/handoff-D/recheck/HANDLER.md` so it can return to the D2 sessions. The authors dispatch the verdict readers through `dispatch.sh`. Only the saved community coders answer the return.

## Documents for this handler

- [Handler protocol](../sources/handler.html): how the handler operates the run and brings decisions to the authors.
- [Build and run](../sources/how-to-run.html): building a separate run and its acceptance checks.
- [Agent reading key](../agents/aggregator.html): what the handler must read, and the inputs and boundaries when starting from coded communities.

## Stage map

Choose a stage for its purpose, expected outputs, full card and saved checkpoints. Status is as of the indexed publication.
