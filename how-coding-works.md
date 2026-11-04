# How community coding works

Each community is read by its own community coder, a model conversation that sees no other community and no earlier coding. The coding handler prepares each community, launches its coder, checks the result and keeps the record. Communities with more than 500 items divide their threads among fleet coders, and the community coder brings their work together. In this study: 705 communities, coded from 7 September to 4 October 2026, with 115,388 first-order codes and 7,844 second-order themes.

## Its contracts

- [The coder contract](sources/coder-contract.html), version 32 (version 30 for 102 communities, r/PlaceNL among them): the method, the rules, the five steps and the outputs.
- [The community coder's contract](sources/case-lead.html), which the run calls the case lead's: the gate between working alone and with a fleet, and the order of work in each branch.
- [The fleet coder's contract](sources/fleet-coder.html): one slice of whole threads, coded, and nothing else.
- [The brief writer's contract](sources/v30-brief-writer.html): the brief of the community's week before the event. Nearly every brief records version 30, with its revision of 7 September 2026, whichever version then coded the community; 17 record [version 32's](sources/brief-writer.html).
- [The coding handler's contract](sources/scheduler.html): the cycle for one community, the checks, and what happens when one fails.

A fresh gpt-5.6-sol conversation writes each community's brief, and a script writes an empty brief where the week before holds nothing. The briefs were written in three runs, from 7 to 30 September: the first two at high reasoning effort, the third at medium. Of the 705 briefs, 626 come from a writer (373 at high effort, 246 at medium, 7 not recorded), 78 are empty, and r/Dorset's records no writer.

[The community coder's documents](coding-contracts.html) lists every document in both versions, with the handler's and the local model's.

## The steps

| Step | What happens | In the contract |
|---|---|---|
| 1. The briefing | The coder reads a brief of the community's ordinary week before the event, written by a different reader, and flags any claim without a quote. | [coder contract, step 1](sources/coder-contract.html#4-step-1--the-briefing) |
| 2. Every thread | It passes over every thread in time order, twenty-five at a time, and records whether each belongs to the case. Nothing is coded yet. | [coder contract, step 2](sources/coder-contract.html#5-step-2--go-through-every-thread-and-decide-what-this-case-is) |
| The gate | Above 500 items, a fixed gate divides whole threads among fleet coders; below it, the community coder works alone. Decided once and recorded. | [community coder, the gate](sources/case-lead.html#1b-the-gate-decided-once-and-recorded) |
| 3. First-order codes | Codes stay close to how members put it. A code cites its item by reference; no coder types quotation text. | [coder contract, step 3](sources/coder-contract.html#6-step-3--first-order-codes) |
| 4. Themes | Codes are grouped into second-order themes, named in the members' words where they have one. | [coder contract, step 4](sources/coder-contract.html#7-step-4--themes) |
| 5. The case account | A chronology, then what set off what, with a stated reason for each relation, and a counter-reading before the verdict. | [coder contract, step 5](sources/coder-contract.html#8-step-5--the-within-case-account) |
| Checks and close | The coding handler resolves every cited quote against the record and runs end checks; a failed check sends the work back. | [coding handler, the checks](sources/scheduler.html#3-the-checks) |

## After the coding: the return

At the return ([D2](stages/D2.html)), an adaptation handler forks, for each community, the checkpoint of the community coder that coded it, with its conversation and files, and gives it a new task in a separate folder. Under the return contract the coder recodes its whole community in the population model's terms; its first coding stays as it was. It reads its own case account, themes, codes, brief and reply trees against the model, the coding structure and the model's vocabulary of element and arrow ids. It then writes two files:

- a model of the community: its case account rewritten section by section in the model's terms, each claim tied to an element id or marked as new and cited to the community's own codes, ending with its own grade and the exceptions it found;
- one line for each change the model needs: an element instantiated, marked absent, given a condition or a finer step, linked, restricted or contradicted, or a new element proposed.

A script checks every return, and the same session repairs what fails. Two separate readers judge, from the evidence, whether the model composes the community. The aggregator rules on every line and revises the model ([D3](stages/D3.html)); each community's return checkpoint then continues with the revised model for the re-check. The results are on [the population return page](results/population-return.html).

## After the coding: the local model (R6)

The local model is a second branch from the coding close, and the aggregator did not use it. Admissions stopped on 28 October; by 29 October, 173 communities had finished it and the other 532 had not run it. The site shares 14 of the 173. For each, a copy of the closed community coder resumed its own session under [the local model's contract](sources/room-model.html), fifth version of 7 October 2026, and [a pilot amendment](sources/pilot-amendment.html) authorized on 11 October. r/Goodboye, the first, ran without the amendment.

The contract tells the coder that coding is closed and that no code, theme or coding file may change. It asks for the community's own model in the manner of Gioia, Corley and Hamilton (2013): themes above the coder's themes, aggregate dimensions where the material carries them, a coding structure and a dynamic model. The coder then sets the model against the literature, writes an account, grades its confidence and closes. Each of its six stages follows a stage of the aggregator; R6, the last, names the checkpoint.

| Stage | What the coder does | The aggregator's stage |
|---|---|---|
| R1 prior | writes what the coding taught it to expect, before it reopens its codes | B1 |
| R2 reading | reads its codes in clock order, one note per block, and keeps a list of episodes | A1 |
| R3 structure | reads its codes for form, then groups its themes into higher themes and dimensions | [C1](sources/room-stage-C1.html), [C2](sources/stage-C2.html) |
| R4 the model | builds the model in numbered passes until two in a row change nothing; a fresh critic returns errors and a rival grouping of its themes | [C2](sources/stage-C2.html) |
| R5 literature | receives the paper by Puranam, Alexy and Reitzig (2014) and maps each higher theme to the problem of organizing it handles | [C3](sources/stage-C3.html) |
| R6 account and close | writes the account, propositions, the coding structure, claims and an interview, then grades its confidence last | [C5](sources/stage-C5.html), [E1](sources/stage-E1.html) |

[The local model's other documents](coding-contracts.html#the-local-model-r6): how it maps onto the aggregator, the files it writes, the aggregator's texts as the checkpoints carry them, and the handler's.

| | |
|---|---|
| Model | for the 14 shared, a naming turn on gpt-5.6-sol at medium, then gpt-6.1-sol at medium; the coding close ran on gpt-5.6-sol at medium |
| Critic | gpt-6.1-sol at medium, the route the runner requests and checks; its record was read for 7 of the 14 |
| Dates | for the 14 shared, 20 October 15:39 to 21 October 13:47 UTC; r/Goodboye also ran on 9 and 10 October |
| Outputs | for r/PlaceNL, six higher themes, two dimensions, 12 elements and four propositions ([its outputs](records/community--PlaceNL--R6.html)) |
| Lineage | same session and same source checkpoint as the coding close; the return (D2) forked the coding close, not R6 |
| Not recorded | a commit for the contract and the amendment, which reach the repository only inside each R6 checkpoint |

[Run it](guides/communities.html)
