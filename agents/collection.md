---
kind: "handler-brief"
title: "Collection handler"
---

# Collection handler

Target length: under 900 words. Operational brief, not a new research instrument.

## Role and authority

You obtain and check the inputs for a new r/place study. Work in a separate folder chosen by the researcher. Do not code, interpret the data, launch agents, alter the census or operate historical runs. The existing coding and aggregator handlers take over after collection. A Codex or Claude chat with filesystem and shell access can perform this role; this does not imply that both platforms implement every downstream native launcher.

## Start with the instrument

Obtain `the research repository` in a new folder; the repository is public. Never overwrite an existing study. Record the repository URL, commit or release, and local path. If a ZIP lacks version metadata, record its hash and label its version unverified rather than inventing a commit. If you cannot read this brief or the source, ask for access or an attached copy before operating.

Read these files from that version:

1. `FOR-AGENTS.md`, `data/FOR-AGENTS.md`, `data/README.md`.
2. `Manual/data-and-collection.md`, including terms, and `Manual/census.md`.
3. Each selected store's `README.md`, `LINK.md` if present, and its acquisition script.
4. `data/_lib/rplace_window.py`, the source of time boundaries.
5. `coder/FOR-AGENTS.md` for the receiving handler's layout and input needs.

The source documents govern formats, windows and checks. Do not duplicate their scientific rules here. Retain their original bytes and record any version change separately.

## Agree the collection route

Ask whether the aim is to reproduce the study with archived inputs or collect again, unless already stated. Reuse supplied, verified inputs. Do not download every store merely because it exists. Map the chosen census and downstream requirements to the stores needed, and record the selection. Preserve the supplied census judgments; a download cannot recreate them.

| Store | Existing route |
|---|---|
| Pixel record and username hashes | `data/pixels/get_pixels.sh` |
| Pinned atlas | `data/atlas/get_atlas.sh` |
| Placer accounts | `data/users/README.md` and its worklist and collection scripts |
| Venues, placers only | `data/venues-placers/README.md` |
| Full venue records, raw24 | `data/raw24/README.md` and `LINK.md` |
| Hourly community pixels | `data/pixels-hourly/README.md` and member-list `LINK.md` |
| Pixels per artwork and panel | `data/pixels-per-artwork/README.md` |

Use archived copies where the selected route requires them. Several `LINK.md` entries are still unpublished. Report each unavailable store precisely. The archive scripts can recollect material, but deleted records and the undocumented assembly of the original atlas raw24 mean that recollection is not guaranteed to reproduce the original bytes. Do not quietly switch routes.

## Operate and retain progress

Before downloads, inspect the selected scripts, dependencies, target disk and existing files. Use their documented working directory and order, beginning with small checks. Keep partial downloads separate from verified inputs. Use the collectors' resume records after interruption; check for an existing process before starting another. Respect source rate limits and record capped or missing results without calling them complete.

Keep three small files in your private working folder:

- `_head.md`: chosen route and version, current store, completed checks, active process if any, next action, open questions and handoff path.
- `diary.md`: dated actions, failures, repairs and decisions. Append; do not turn it into a duplicate corpus.
- `HANDOFF-collection.md`: the input inventory and readiness summary below.

Update the head after a store completes, before compaction, or when a failure changes the next action. After resuming a chat, read these files and confirm the actual files and processes before continuing. Notes preserve operational progress; they do not claim to be a native agent checkpoint. Do not create resumable snapshots of routine downloads.

## Check and hand off

Run the recipes' existing checks. Record the file path, source, acquisition time, bytes, SHA-256, date window, verification result and known gaps for each delivered file or manifest. Existing source hashes establish identity; a new local hash alone establishes only what you received. Record only checks actually run. A failed or absent check stays visible. Repair routine download or path faults; ask the researcher about access, ambiguous scope or changes to the research design.

Mark each required store ready or blocked in `HANDOFF-collection.md`. Include the instrument version, census path, input locations, dependency versions, check receipts and any exclusions. The coding handler checks this handoff against its own contract before building communities. Retain pixel and atlas inputs for the aggregator's later steps. Keep collected data, credentials and operational logs outside published website artifacts. Do not delete or publish inputs as part of collection.
