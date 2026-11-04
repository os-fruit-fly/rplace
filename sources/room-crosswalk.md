# The three model-building instruments, side by side

Target length: under 1,950 words. Sixth, 7 October: coder-theme names at R3; C4 not given to the field lead (J). Fifth, 7 October: the tools and the organizing-end record, after Claude's audit and OpenAI's repair. Fourth, 5 October: after Codex's sibling-contract review (`REVIEW-codex.md`), J's rule on theory and an independent check; then the field's Part I set to J's order and Codex's field review; recovery from hidden snapshots (J, 6 October).

Three instruments build models: the global aggregator (the rooms together), the case aggregator (one room, run per room) and the field model (r/place, run once). The two new ones are siblings of the global one. They share its questions, tiers, rules and file formats by shipping the same files, pinned by hash in `PINNED.tsv`, never by paraphrase. Each sibling's contract holds a reading key, a rule table and its own stages; `PROFILE.md` holds the fields its files add or replace. If a pinned file changes, the siblings fail their check until rebuilt, so the three cannot drift apart unnoticed.

## Shared files

| File | Global aggregator | Case aggregator | Field model |
|---|---|---|---|
| `CONTRACT-aggregator.md` | the contract | §1 to §3, §5's weak-absence rule, §6's stopping rule | the same, through the room contract |
| `METHOD.md` | whole | first section | first section |
| `WRITING.md` | whole | whole | whole |
| `SCHEMA-adaptations.md` | whole, from D1 | §1 | §1 |
| stage cards C1, C2, C3, C5 | the stages | R3 to R6 follow them | the same |
| `FLEET.md`, stage cards B2, B3, B4 | at fleet stages | none | Part I's pilot, placement fleet and adjudication |
| v32 coder contracts and tools (`emit.py`, `close_run.py`, `cite.py`, `read.py`, `fleet.py`, `audit_fleet.py`, `tree_builder.py`) | none | none: the coding is closed | Part I, from F0 through the fleet |
| stage card E1 | the claims audit | `claims.md` | `claims.md` |
| stage card C4; `HANDLER.md` on the field | the stage | none | not given; `field/` follows it |
| `room-model/CONTRACT.md` | none | the contract | Part II |
| `PROFILE.md` | none | every file | every file |
| full papers | the shelves | Gioia, Corley and Hamilton; Puranam, Alexy and Reitzig | its own shelf and `READING.md`: Gioia, Corley and Hamilton at FA; Puranam, Alexy and Reitzig, Padgett and Powell, Lewin and Volberda, and Ostrom at R5 |

## The tiers, the IDs, and where theory enters

| Gioia's name | Global aggregator | Case aggregator | Field model |
|---|---|---|---|
| first-order concepts | `sub:c0042` | `c0042` | `c0042` |
| first-order, consolidated within a case | coder themes `sub:t07` | coder themes `t07`, closed | coder themes `t01` on, v32's IDs: gates `g01` built after every return is read, placed by a fleet, adjudicated, then emitted |
| first-order, consolidated across cases | `T3-`, never a construct's name | none | none |
| second-order themes | `T4-`, constructs | `T4-`, constructs | `T4-`, constructs |
| aggregate dimensions | `D`, constructs | `D`, constructs | `D`, constructs |
| the model | `P K C R A L`, findings `F`, propositions `N` | the same | the same, with `field_level`, `groups`, `room_side` |

**Theory** (J, 5 October 2026: "In gch one cannot use theory for the first order ... Only first order get no theory in the labeling"). In all three, the first order carries no theory: codes, coder themes as coded, and the global third-order themes. Second-order themes (`T4`) and dimensions are constructs from the cut, declared borrowed (recalled until the literature stage), adapted or coined, and may take any literature's names, the four problems' included; no `T4` tier copies the four problems. The siblings have three levels to the global's four, so theory enters one step earlier in their build, at the same Gioia tier. From R3 a sibling may also give a coder theme a theory name (`names.jsonl`), exports keeping its label (J).

IDs are bare inside each instrument. On export the controller prefixes every ID and reference with `sub:` or `field:`, so `denmark:T4-002` and the global `T4-002` can share a ledger line.

r/place's coder themes are built after reading every return, under gates, placed by a fleet: a declared difference. Its unresolved codes form one residue theme, marked in `theme_map.jsonl` and never read as a kind. The global aggregator receives only `field/`.

## Deliverables

| Global aggregator (stage) | Case aggregator | Field model |
|---|---|---|
| none | none | F0: v32 steps 1 to 3 through the fleet; snap `after-fleet` |
| `prior.md` (B1) | R1, written after the coding, and so marked | FA, after the v32 boundary steps and before the returns are read, saying what the lead had seen; with the group and phase rules |
| reading notes and `organizing_end-A1.jsonl` (A1) | R2: block notes, `episodes.jsonl`, `organizing_end.json` | FA: block notes, `episodes.jsonl`, `groups.jsonl`, `interactions.jsonl`, `phases.jsonl`, `organizing_end.json` |
| scheme, gates, pilot, fleet, adjudication (B1 to B4) | none | FB and FC: the gates; pilot with fresh readers; a placement fleet over whole threads; snap `after-placement` |
| none | none | FD: adjudication and the blind sample; emission with `theme_map.jsonl`; counter-reading; the six v32 outputs, `INTERVIEW-coding.md`; snap `coding-closed` |
| form pass (C1 §7) | R3, over the room's codes | R3, over r/place's codes |
| `fourth/fourth.jsonl`, `dimensions.jsonl`, `assignments_final.jsonl`, `structure.md` (C1, C2) | R3, `assignments.jsonl` placing coder themes | R3, the same, with `field_level` |
| `concept.md`, `model/` files, `model.md`, stories (C2) | R4; stories read against episodes | R4, with levels and room side; read against episodes and phases |
| one reviewer, before the final passes (C2 §6) | one critic inside R4, before the final passes; its session discarded | the same, its session kept |
| `literature-C3.md`, `mapping-C3.jsonl`, switch records (C3) | R5: C3 §1 and leg 3; legs 1 and 2 do not run | R5, with levels and the four works of `READING.md` |
| `field-C4.md` (C4) | none | supplies `field/` |
| `account.md`, `propositions.jsonl`, `data_structure-C5.md`, `figure-C5.md` (C5) | R6; no third-order column | R6 |
| three readers (C5) | none | two readers |
| `findings.jsonl` | same | same |
| `claims-E1.md` (E1) | `claims.md` | `claims.md` and the audit scripts |
| none | `confidence.jsonl`, sealed | `confidence.jsonl`, sealed |
| interview briefs | `INTERVIEW.md` at the close | `INTERVIEW-coding.md` at `coding-closed`, `INTERVIEW.md` at the close |
| D1 to D6, E2 | none | none |

## The critic

J, 5 October 2026: every room gets the critic where the global reviewer sits (C2 §6): inside R4, after the pass the lead expects to keep and before the final passes, so its fixes can reopen the loop. r/place's runs the same way.

## Order, sealing, and confidence

1. The case aggregators and the field model close, and the controller seals each `confidence.jsonl` (hashed with the model version, kept where no agent can write) before anyone sees the global model.
2. The global aggregator reads no case-aggregator output before its own freeze. It reads `field/` at C4 and nothing else from the field.
3. At the return, D2 sends the case aggregators if enough rooms have one by then, else the case leads (J, 5 October 2026).

The siblings implement points 1 and 2. Point 3 and the use of the sealed grades change the global aggregator; they are listed for J, not made:

- **D1** writes a routing manifest: which rooms go to a case aggregator and which to the original case lead, with each sibling's checkpoint and model version. J defines "enough", and whether routing is per room (mixed) or for the whole cohort.
- **D2** resumes the matching case-aggregator session (its model already in the global schema), else the original case lead, keeping the original codes' and coder themes' provenance and the global lift beside the local ladder. The fixed-global verdict readers stay as they are and never see the sealed grades.
- **Ex-post grades**: each adaptation's confidence at D2 needs a ledger field in `SCHEMA-adaptations.md` or a keyed sidecar, D1's return specification and ingest to match.
- **D3** reads the sealed and ex-post grades side by side as cues, never evidence or votes, and rechecks what an amendment touches.
- **E1** audits seal hashes, exposure order, routing coverage, paired grades and model versions.
- **C4** checks `field/` before reading it: `MANIFEST.tsv` against the sealed hash, every evidence line joined to its quote. `stage_C4.py` does neither.

## What the runtime has to do

The contracts assume a controller the community-coder runtime (`coder_model/`) does not yet have; the coding handler confirms and sizes this:

- One session per room through R1 to R6, with compaction; recovery from hidden stage-boundary snapshots, shown accurate before the next turn (room contract), tested by a cold restore; one archive at the close.
- The critic inside R4: the lead ends its turn, a worker reads a packet, the lead resumes.
- The confidence seal, outside every agent's write scope.
- `tool.py`: `context` (also by ID), `read`, `find`, `cite` (whole span, verbatim part or seeded draw), `note`, `head`, `count` in three modes (coverage, prevalence, aftermath), `move` and `check`, and `snap` for r/place; read logs; the controller's stamp on history lines.
- A validator and renderer from `PROFILE.md`, in place of `model.py`'s single `model.json`.
- A room with no codes still runs, and its empty model is valid (`evidence.build` now refuses it).
- For r/place: v32 from the verified brief through the fleet (about 415 slices expected), snap `after-fleet`; the boundary steps under v32 tools and branch B permissions; the pilot and the placement fleet, snap `after-placement`; adjudication, the blind sample and emission; `coding-closed`; then Part II in legs. The package is built, read by the lead, then sealed with `confidence.jsonl` and the model hash; a correction after the seal is a new version.
- A pause and resume rule for long rooms, beyond the 30-minute turn and 200-turn default.
- The export prefixer, recursive through every reference, and the `field/` package writer.
- For r/place's Part I: a packet builder and return validator at the grain of a code, for the pilot, the placement fleet and the blind sample, in place of the global stage tools.
- A build lock: `PINNED.tsv` lists everything a sibling build copies, imports or runs (v32's whole fingerprinted set and `newrun.py`, the reused global checkers, `vlib.py` and the three modules it loads); a changed dependency is refused before dispatch, and v32's run fingerprint is recorded with the lock.
- Fixtures before a real trial: one per waiver; cold restore after a compaction and after an interruption; no tool running at capture; a recall probe denied tools; the parent unchanged; the critic's return replayed, not redispatched; J's re-delivery choice; seal write denial; the final archive restored; a model over the critic's ceiling; rooms with zero, one and two episodes and no defensible arrow; a boundary with fewer than three recall questions. For r/place also every named snapshot, the paired-reader allocation, adjudication, v32's close and C4 reading `field/` in isolation, with a transition-only arrow, a coder theme as a `T4` member and an `FP-` element, which fails when either definition is removed. Forks for interviews, source isolation and recall probes stay; only recovery stops forking.
- `protocol.py` installing these contracts in place of `CODER-MODEL.md`; routes for the field's critic and its two R6 readers.
- Before a lead is resumed: its runtime still exists, and its history shows no earlier canvas or global exposure. A fresh agent is never presented as the original lead.
