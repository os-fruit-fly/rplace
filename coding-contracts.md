# The community coder's documents

Every document a community went through, from its brief to its local model, reproduced unchanged. How community coding works explains them in order.

## The coder instrument

Version 32 coded 603 communities and version 30 coded 102, r/PlaceNL among them. Version 32 is in the repository; version 30 comes from r/PlaceNL's checkpoint. In the four communities checked, the run contract differs from its template only in ten lines: the community's name and the paths to its record, brief, tools and outputs.

| Document | What it governs | v32 | v30 |
|---|---|---|---|
| Coder contract | the method, the rules, the five steps and the outputs | [v32](sources/coder-contract.html) | [v30](sources/v30-coder-contract.html) |
| Community coder, which the run calls the case lead | the gate between working alone and with a fleet, and the order of work in each branch | [v32](sources/case-lead.html) | [v30](sources/v30-case-lead.html) |
| Fleet coder | one slice of whole threads, coded, and nothing else | [v32](sources/fleet-coder.html) | [v30](sources/v30-fleet-coder.html) |
| Brief writer | the brief of the community's week before the event | [v32](sources/brief-writer.html) | [v30](sources/v30-brief-writer.html) |
| Launch file | what each agent is told when it starts | [v32](sources/coder-agent.html) | [v30](sources/v30-coder-agent.html) |
| Tools | how the agents read the record and cite it | [both](sources/coder-tools.html) | same file |
| The instrument | its files, and what changed from the version before | [files](sources/coder-instrument.html), [changes](sources/coder-changelog.html) | [changes](sources/v30-changelog.html) |

Why the instrument moved [from v30 to v31](sources/coder-v31-rationale.html) and [from v31 to v32](sources/coder-v32-rationale.html). Nearly every brief records the brief writer of version 30, with its revision of 7 September 2026, whichever version then coded the community; 17 record version 32's revision.

## The handler

- [The coding handler's contract](sources/scheduler.html): what it may read and write, the cycle for one community, the checks, failures, the record, and what is ours to decide.
- [The coding handler's queue](sources/coding-scheduler.html): how many communities run at once, and the order of the queue.
- [The case-lead prompt](sources/case-lead-prompt.html): how a community coder is launched and calibrated.
- [Checkpoints](sources/coder-checkpoints.html): the saved session of each community coder.
- [The brief coordinator](sources/brief-coordinator.html) and [the brief writer's prompt](sources/brief-writer-prompt.html): how the briefs were queued and written.
- [Repair-queue rules](sources/repair-queue.html): how failed work is restarted.
- [Verified archives](sources/verified-archives.html): how a finished community is archived and restored.

## The local model (R6)

These reach the repository only inside the R6 checkpoints.

- [The local model's contract](sources/room-model.html), fifth version of 7 October 2026, and [the pilot amendment](sources/pilot-amendment.html) of 11 October, which 13 of the 14 checkpoints carry.
- [The crosswalk](sources/room-crosswalk.html): the local model beside the aggregator, stage by stage.
- [The file profile](sources/room-profile.html): every file the local model writes.
- [The aggregator's contract](sources/room-contract-v43.html) and [C1 card](sources/room-stage-C1.html) as the checkpoints carry them, earlier than the copies the aggregator ran with. Its other stage cards, C2, C3, C5 and E1, are the aggregator's own.
- The [handler](sources/room-handler.html), its [snapshot policy](sources/room-snapshots.html) and [amendments](sources/room-amendments.html), as they stood on 2 November 2026, after the run.
