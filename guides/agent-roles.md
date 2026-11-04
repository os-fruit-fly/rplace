# Agents and their roles

The work is divided so that preparing evidence, interpreting it and checking an interpretation are separate jobs. A handler manages the process. A community coder or the aggregator owns an account. A reader answers a bounded question from specified evidence. The authors set the study's scope and answer for its claims.

An agent is a model conversation with a task and the files it may use. The names below are roles; checkpoint records name the model and saved state used at each point.

[Prepare the record](#prepare-the-record) · [Understand a community](#understand-a-community) · [Build the shared model](#build-the-shared-model) · [Return and audit](#return-and-audit) · [Interview a saved agent](#interview-a-saved-agent)

## AI use in v43

The paper reports this division of work. Exact settings, changes of model and fork boundaries are recorded with each saved checkpoint.

| Work | Model and environment |
|---|---|
| Community coding, fleet coders included | gpt-5.6-sol in Codex. |
| Community returns to the population model | gpt-6.1-sol in Codex. |
| Population analysis | Claude Opus 5.5 in Claude Code. |
| Routine reading checks, and the aggregator's fleet of independent readers | DeepSeek V4.1 Flash. |

Table: Each kind of work, with its model and environment

The authors designed the instrument and ruled on questions during the run. The agents code and compose descriptions; the authors judge the theoretical contribution and answer for the claims. Claude and Codex also helped edit the paper and build the figures and website. [Inspect recorded model settings and lineage](history.html#models-and-lineage).

## Prepare the record

### Collection handler

Obtains the selected pixel, Reddit and atlas data through the repository's download routes, checks what arrived and records gaps. Its handoff gives the coding handler verified input paths and versions. Choosing research categories and interpreting communities fall to later roles. [Collection brief](../agents/collection.html).

### Brief writer

Reads the community's record from the week before the event and writes a brief of it. The brief gives the community coder background on the community and leaves the reading of its r/place activity to the coder. The brief and its quotations are checked before coding begins.

## Understand a community

### Coding handler, also called the scheduler

Prepares each community's working folder, launches its agents, checks their outputs and keeps the progress record. It handles failed jobs and keeps completed work. What a quotation means is the coders' question, and the handler changes no coder's answer to pass a check. [Scheduler contract](../sources/scheduler.html).

### Fleet coder

Reads an assigned slice of whole threads in a large community and writes first-order codes tied to participants' words. Its work passes to the community coder. It runs in the community coder's model; the aggregator's fleet, the independent readers, is a separate one. [Fleet coder contract](../sources/fleet-coder.html).

### Community coder

Owns the community's whole account. It codes a small community itself; for a larger one it brings together the fleet coders' work, groups the codes into second-order themes and writes the case account. Its saved conversation and matching files allow later continuation and interviews. [Community coder contract](../sources/case-lead.html).

### Community coder, for the local model (R6)

Builds a model of organizing within its own community from its coded evidence. The R6 close comes after the coding close and belongs to a separate local-model workflow outside the coding scheduler. Compare [r/PlaceNL after coding](../records/community--PlaceNL--coding-close.html) with [its R6 model](../records/community--PlaceNL--R6.html).

## Build the shared model

### Aggregator handler

Builds the population-level run, opens and closes its legs, supplies the permitted inputs and dispatches reader jobs. It records checks, keeps checkpoints and brings research decisions to the authors. [Handler protocol](../sources/handler.html).

### Aggregator

Reads across communities, builds common categories, develops the population model, assesses returns and explains organizational forms. Stages divide this work into steps that can be inspected. One aggregator carries the work across stages and legs, through its saved conversation, files and recorded lineage. [Follow the stages](aggregator.html#stage-map).

### Independent readers

Use the common scheme to place second-order themes in categories. They test the rules in [B2](../stages/B2.html), apply them across the collection in [B3](../stages/B3.html), and check settled placements in [B4](../stages/B4.html). Their separate readings expose disagreement, and the aggregator settles each case from the evidence, with no vote.

### Critical readers

Challenge a developing explanation. The [C2](../stages/C2.html) reader examines the model; the [C5](../stages/C5.html) readers test claims in the integrated account against cases. Their replies stay beside the aggregator's responses, including criticism that remains unresolved.

### Field agent

Reads the central r/place subreddit, where communities recruit, negotiate and discuss the event, and gives a view across communities. It supplied an interim reading and comments at [C4](../stages/C4.html) while its own analysis was unfinished. This site has no launch guide for it yet.

## Return and audit

### Adaptation handler

Delivers the fixed population model to each saved community coder, checks the returns and sends required repairs back to that coder. It keeps local histories separate and records missing returns. It passes the model on unsummarized, and the aggregator decides which corrections to accept. [Return preparation](../stages/D1.html).

### Returning community coder

The saved community coder reads the population model against its own community and writes a local account in the model's terms. It records needed detail, conditions, contradictions or missing ideas. If the model changes, the affected community coders return for the [D3 re-check](../stages/D3.html). A return compares the model with the community's record; the original participants are not asked.

### Verdict readers

Judge independently, from specified evidence, how well the model accounts for each community. Their reasons can disagree with each other or with the returning community coder. [D2](../stages/D2.html) keeps these judgments; D3 rules on disputed ones and decides any change to the model.

### Reconstruction readers

In [E1](../stages/E1.html), check whether the shared model plus the supported local adaptations can account for claims in a sample of community accounts. Their test shows missing links between population explanations and local evidence, within that sample.

## Interview a saved agent

A checkpoint interview opens a disposable fork of a saved agent with its matching historical files. It is the aggregator at a chosen point, restored from its own saved state. Its answers are new, given in the interview, and the original analysis stays unchanged.

The [interview catalog](../interviews.html) lists the community and aggregator checkpoints available. Not every brief writer or fleet coder has a conversational checkpoint there. [Reading keys for agents](../agents.html) give the operational instructions; this page explains the division of work.
