# Reading copy: coder-v32-rationale

Links below are resolved against commit `7c788ae58ce0d4ae171d65e7550cf55b83a22624`. Source wording is unchanged; Markdown formatting may differ. [Exact source bytes](../sources/coder-v32-rationale.md), SHA-256 `8fd2a2a842b0d9ecd540e38b454c4db0081cf8870a0b4afffc558968b5bcd4a2`. [Source and link manifest](manifest.json). Repository links open the public research repository at this commit.

---

# Why the yard moved from v31 to v32

Date: 2026-09-09

## Decision

Use instrument v32 for future room launches. Preserve completed rooms and active stores with the instrument already copied into their run directory. Do not edit a dispatched run to make it look like a v32 run.

## Evidence

`CLAUDE_COMMENTS/Coder Comments v1.md` reports one systematic defect in completed v30 coding outputs. Among read `out_of_scope` threads with ten or more in-window items, many lacked `excluded_quote`. The defect was most common when the thread had been read in full, which implies the rule was misread as if full reading replaced the cited exclusion line.

The quote matters because it is the evidence that a substantial discarded thread was checked before it was set aside. If it is missing, the exclusion cannot be reconstructed later without reading the thread again.

## Changes

v32 makes C5 executable at write time. `emit.thread` now refuses a read `out_of_scope` disposition for a ten-plus-item thread unless `excluded_quote` is the exact dictionary returned by `cite.py`. `emit.threads_bulk` uses the same path, so bulk exclusions cannot bypass the rule.

The final gate still checks C5. It uses the in-window counts in `coder_corpus.jsonl`, preferring the header and falling back to rows that are not marked context. `_read_index.json` is not the C5 source because its thread item counts can include context openings.

The contract, fleet-coder contract, and agent note now say plainly that reading the whole thread does not replace the cited line. The trigger is size, read state, and exclusion.

## Queue rule

If this defect appears in an active v30 or v31 store, treat it as a repairable validation failure and keep the evidence. Do not mutate the copied instrument in that store. Future starts should use v32 after the coordinator drain is cleared.

## What did not change

The research method, evidence standard, output set, branch threshold, and model plan did not change. This is a guardrail against a preventable recording defect.
