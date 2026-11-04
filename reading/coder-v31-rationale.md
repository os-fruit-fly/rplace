# Reading copy: coder-v31-rationale

Links below are resolved against commit `7c788ae58ce0d4ae171d65e7550cf55b83a22624`. Source wording is unchanged; Markdown formatting may differ. [Exact source bytes](../sources/coder-v31-rationale.md), SHA-256 `076c254784cbc43c0163ea3756dc8bb029c38f51f0b8c165280b5736554a554f`. [Source and link manifest](manifest.json). Repository links open the public research repository at this commit.

---

# Why the yard moved from v30 to v31

Date: 2026-09-08

## Decision

Use instrument v31 for new rooms. Preserve every completed or already-dispatched v30 room with its original instrument and hashes. Active v30 repairs continue on v30; they receive the parts of the new completion checklist that do not require a v31 tool.

## Evidence

The first blocked-room audit found four repeated validation classes in at least 34 of the 60 rooms selected for repair:

| preventable class | rooms |
|----|---:|
| missing exact exclusion citation on a read, out-of-scope thread of at least ten in-window items | 12 |
| thread disposed as `coded` but left with no live code | 11 |
| branch-B notes did not repeat the gate completely | 9 |
| branch-B lead read or searched raw material before step 4 was complete | 2 |

The broader attribution was 41 coder-stage failures, 16 lead or final-stage failures, and three fresh-run or infrastructure failures. The high repair rate came largely from discovering mechanical defects only after the agent had exited. A reminder alone leaves the same timing problem in place.

## Changes

v31 lets the working agent run `close_run.py --preflight` before sending its final message. The preflight omits only the checks that cannot exist until after exit: the stored native transcript (C2) and the final journal-tail check (C10). Full scheduler validation still runs after exit.

Two checks make frequent implicit requirements explicit. C11 rejects a `coded` disposition that has no live code. C12 verifies the exact gate record in branch-B notes. The existing C5 check is called out in the fleet-coder checklist so the agent supplies the citation while the source passage is still in context.

The v31 reading and search tools also refuse a branch-B case lead's raw access until the journal records `step5_counter`. That makes the lead-order rule executable instead of relying on memory. Fleet coders are unaffected because their slice directories do not contain the lead's branch gate. Branch-A leads remain unrestricted by this guard.

Retry instructions now state that the named defect is additional guidance. The agent must check the complete slice or case before ending; a retry is not a one-file patch unless the complete preflight confirms that nothing else is missing.

## What did not change

The case, time window, 500-item branch threshold, whole-thread slicing, Gioia register, within-case method, counter-reading requirement, citation standard, output set, and model-facing evidence are unchanged. v31 does not add a code quota, theme quota, search quota, or preferred reading.

## Rollout and version integrity

`_instrument/v30/` remains untouched. `_instrument/v31/` is a complete independently stamped package with v31 filenames, imports, manifests, and fingerprints. New room builds derive the instrument number from the selected package instead of writing `v30` into room state. Room status reads the version stamped in `newrun.py`.

No instrument is replaced inside a dispatched run. This keeps existing v30 manifests and archive hashes valid while making v31 the documented default for later work.

## Follow-up from the resumed repair pass, 2026-09-08

soylent and apocalypserising again failed C5 in fleet batch 01. The preserved soylent coder transcript contains no invocation of the supplied preflight, and thread `62lywc` has exactly ten in-window items but no exclusion citation. A replay of its saved journal reproduces that defect.

The scheduler now runs the journal preflight as mandatory B8 in `verify_room.py --batch` before collection. This catches the same defect even if a coder skips its instructed check, before later slices and the lead's account consume more work. It does not change the copied v30 instrument or any research output. Three model-free preflight fixtures pass, including a missing citation at the ten-item boundary. The preserved failing soylent batch was also replayed and rejected.

The resumed redhotchilipeppers and winnipegjets leads later passed the coder and close checks but failed E5 because their notes omitted the required branch/threshold record. Their saved conversations predate the revised opening prompt. The scheduler now repeats the gate-record and complete-record checklist in every `message finish`, so an existing lead receives it at the point of consolidation too. This is a compatible v30 reminder; it changes neither the instrument nor existing outputs. Finish messages already sent are unaffected.
