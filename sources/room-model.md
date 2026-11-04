# Contract: the case aggregator, one room

Target length: under 3,900 words. Fifth version, 7 October 2026: theory names for coder themes at R3 (J). Fourth version, the same day: what a count is for, search, the organizing-end record and typed episode kinds, after Claude's audit of the siblings and OpenAI's repair (J: "go ahead", 7 October). Third version, 5 October: Codex's sibling review, J's rule on theory; recovery from hidden snapshots (J, 6 October).

## What you are here to do

You are the case lead who coded this room. Coding is closed: never edit a code, a coder theme or any file the coding wrote. Now you build this room's model of organizing as Gioia, Corley and Hamilton (2013) describe it: theoretical themes above your coder themes, aggregate dimensions where the material carries them, a data structure, and a dynamic model that sets the structure in motion. Then you put it to the literature, write the account, grade your confidence, and close.

You are the global aggregator's sibling, working on one case. It models all the rooms together and has never seen yours; later the study compares the two models element by element. So you build with its questions, tiers, rules and file formats. This file holds only what differs for one room; for the rest, read the global text.

## What you are given, and how to read it

These files ship unchanged from the aggregator's instrument; `PINNED.tsv` holds each one's hash, and a check fails if any differs. `PROFILE.md`, marked *, is the siblings' own.

| File | What binds you |
|---|---|
| `global/CONTRACT-aggregator.md` | §1 the two questions, composition, the standing claim; §2 the tiers and the typed model; §3 the rules, as the table below says; §5's "mark every absence claim as weak"; §6's stopping rule for passes. Read §1 and §2 whole at R1. |
| `global/METHOD.md` | the first section, "What the method says, held at every stage", read whole at R1 and again at R4; and the paragraph on the four licences, for rule 17 |
| `global/WRITING.md` | every sentence you write in your own words |
| `global/SCHEMA-adaptations.md` | §1, the elements of the model |
| `global/stages/STAGE-C1`, `C2`, `C3`, `C5` | the procedures R3 to R6 follow, read through the key below |
| `global/stages/STAGE-E1` | the claims table `claims.md` follows |
| `PROFILE.md`* | every file you write: the global definition it follows, its path, its IDs, and the few fields it adds |
| `shelf/gioia-corley-hamilton-2013.md` | in full, from R1 |
| `shelf/puranam-alexy-reitzig-2014.md` | in full, arriving at R5 |

**The reading key.** The global texts speak of rooms, stages and tools you do not have. Read them through this key.

| Global text says | For you |
|---|---|
| the rooms, the analysed set | this room |
| a community count; carries / had the opportunity / had no opportunity | one declared unit per count (codes, coded items, threads or authors in this room) and its population; the three numbers only for a prevalence claim (rule 5) |
| stage A1 | R2, reading |
| stage B1 `prior.md` | R1 |
| stages B1 to B4, the third-order tier, its gates, the fleet | none: one case has no cross-case tier |
| stage C1 §7, the form pass | R3, over this room's codes |
| stage C1 §8, cutting fourth-order themes | R3, `T4` themes cut from your coder themes |
| stage C2 | R4, the model in passes |
| C2's "three rooms first", `within_case.md` | episodes first, in `within_case.md`: one ordinary, one the structure could not have predicted, one that stopped early; as many as the record holds, up to three, as the global check takes `min(3, available)`, and each missing kind named as unavailable; the three kinds typed in `within_case.jsonl` |
| stage C3 | R5, the literature, with two papers |
| stage C4, the field | none |
| stage C5 | R6, the account and the close |
| stages D1 to E2 | none in this run |
| `cite.py`, `mem.py`, `counts.py`, `snap.py` | `tool.py`: `context` (also by ID), `read`, `find` (a search grounds a claim and never chooses a reading: rule 2), `cite` (a code's span or a verbatim part of it, or a seeded draw from a declared set), `note`, `head`, `count` (three modes, below), `move`, `check`; r/place adds `snap` |
| `story_rooms-pN.jsonl`, rooms read against the story | `story_episodes-pN.jsonl`, episodes read against the story |
| `sampled_against` rooms | `sampled_against` episodes |
| `early_late`, the onset contrast across rooms | none: one room has one onset. On each strong arrow, where C2 asks `early_late`, you add `live_aftermath`, the arrow's evidence at or before hour 73 and strictly after it, as a declared extension |

## Your part in the two questions

Global §1 states both questions. Here is what they ask of one room.

**The theory question.** Did organizing happen here, and what form did it take? How did it work? Did it keep the work alive, as the room's own record tells it? The four things global §1 says the model has to say apply to this room: how a scattered readership became something that could act and settled what to act on; what sent it back to that beginning; what brought organizing about when it came, and what followed; and what it left behind. None is assumed. A room that did not organize is a finding, and so is one whose organizing lived elsewhere.

**The method question.** Your model is one of the independently reconstructed case histories the study tests for composition: you see no other room and no global model before you close. When the global model returns, the difference between the two, element by element, shows whether this room composes, and your model keeps the room's supported particulars. Both uses need the global schema, with evidence on every element.

## Theory, and where it may enter

J, 5 October 2026: in Gioia, Corley and Hamilton, the first order carries no theory. This instrument has three levels, so theory enters at the second.

- **First order, no theory.** Your codes stay in the participants' terms.
- **A coder theme may take a theory name, at R3's opening** (J, 7 October 2026). The coding named them descriptively, for the global model; your model may use apt names, or keep these. Each name is declared in `names.jsonl` as a `T4` name is, beside the coded label. A theme's ID, label, codes and note never change, and every file the global reads keeps the label as coded.
- **`T4` themes and dimensions are constructs from the moment you cut them**, as global §2 says of fourth-order themes and dimensions. Any literature may name them, the four problems' vocabulary included, declared as global §2 says (borrowed, `recalled` until R5, adapted or coined; what would disconfirm it; the grounded phrase as gloss).
- **The standing claim** (global §1): an organization is a group with a goal, and every such group must solve task division, task allocation, reward provision and information provision. You know it from R1. **Do not build the `T4` tier as a copy of the framework**: four themes matching four problems is the framework restated, and so are coder themes renamed after them. **Whether a goal was inherited, negotiated, contested or changed here is a finding, never a premise.** R5 puts the frame to your structure.

## The tiers

Global §2 binds you, with one tier fewer and the IDs of `PROFILE.md`. When your files leave this room, the controller adds `sub:` to each ID.

| Tier | IDs | Who | Gioia's name |
|---|---|---|---|
| first-order concepts | `c0042` | coding, closed | first-order concepts |
| coder themes | `t07` | coding, closed | first-order concepts, consolidated within a case |
| `T4` themes | `T4-001` | you | second-order themes |
| aggregate dimensions | `D01` | you | aggregate dimensions |
| the model | `P01`, `K01`, `C01`, `R01`, `A01`, `L01`; findings `F-001`; propositions `N01` | you | the grounded model |

There is no `T3` tier: it consolidates across cases, and a room has none to consolidate across. You cut `T4` themes straight from your coder themes. Each `T4` theme carries a gate, as a third-order theme does in the global (§2): the condition a coder theme's material must meet, a discriminator against the nearest theme, what varies inside it, what it is not, `decide_when_both`, and `gate_parts` for a two-part move. Each coder theme sits in one `T4` theme by its gate (rule 0), or is split code by code with a recorded move, or is marked contextual, out of scope or unresolved with a reason. The gate places coder themes; it is never a count of the codes they carry. No number is set. Zero `T4` themes, zero or one dimension, are findings to report, with the partitions you tried.

## The rules

Global §3, rule by rule. "Binds" means the whole pinned rule, not its heading.

| Rule | For you |
|---|---|
| 0 single placement | binds, for coder themes on `T4` themes by the `T4` gates, with `why_not_one`, the dispensable placement and the cap of three; `multiplacement_log.jsonl` |
| 1 the log is an output | binds and does not move. Every read, of the record or of your own files, goes through `tool.py` |
| 2 search does not choose | binds: say what chose your reading, each time |
| 3 quote from the bottom tier | binds and does not move: through `tool.py cite`; an exemplar passes its `T4` theme's gate on the quote alone |
| 4 counts are of communities | replaced: each count declares one unit (codes, coded items, threads or authors), never a mix, and its population |
| 5 gate before count | binds where counting is the claim: the gate is the claim's own, named in the count; the population is this room's units in the window; the three numbers sum to the testable units, and units that are not testable are listed and counted beside them, never as zero |
| 6 unmeasured is not zero | binds and does not move |
| 7 the canvas | replaced: you see text only (J: "They just see the text."). No canvas field, no atlas, no artwork. A participant's report of the canvas is their words, cited as such |
| 8 looked for and not found | binds: the critic comes inside R4, before the final passes |
| 9 no worked example decides | binds and does not move |
| 10 departures | binds: `departures.jsonl` before you act. Rules 1, 3, 6, 9, 13 and §5's weak-absence rule do not move |
| 11 recutting | binds for `T4` and `D` through R6, with `tier_history.jsonl` (the move, `was`, `prompted_by`, why); coder themes are never recut |
| 12 validate locally | at the return, not in this run; there the fixed-global verdict, your local judgment and the joint elaboration stay separate |
| 13 what a challenge decides | binds and does not move: an error is fixed; a disagreement is answered; no vote is a warrant |
| 14 findings are held | binds: `findings.jsonl`, append-only; a recut re-examines every finding it touches |
| 15 a display owes its file | binds: the controller renders figures and tables |
| 16 counterexamples | binds at R4 to R6, with `counterexample_response` |
| 17 final messages | one, at the close: the claim, the episode that best supports it, the episode that most threatens it, the condition that separates them, the counts, and which of METHOD.md's four licences you exercised and which not |
| 18 working files | binds, with one declared difference: you take no move snapshots. Every move is a `tier_history.jsonl` or `model/history.jsonl` line stamped by the controller. The controller's hidden recovery snapshots (below) are not yours |
| 19 counts and amendments | binds: counts from `tool.py count` in the same act, in the mode the claim needs (below); an override names what it overrides |
| 20 the diary | binds: through `tool.py note` as you work, stamped by the controller with the time and the stage; a closing line is the last entry, not the diary |

## What a count is for

J, 7 October 2026. A count does one of three jobs, and `tool.py count` has a mode for each.

- **Coverage**: how far a search or a reading reached, as matched IDs over a named population. Report it wherever it says how far a pass went. It never gates a claim, and no prevalence or adequacy follows from it.
- **Prevalence**: a claim that is itself a quantity (most, rare, the commonest act). Rule 5 applies.
- **Aftermath**: R2's share, as global A1 counts it (R2 below).

Every other claim (a `T4` theme, an arrow, a mechanism, a form-pass finding) rests on episodes, sequences, contrasts and counterexamples, and a count beside it is context. A dated sequence in this room warrants a process claim without a denominator; a claim about how often a sequence occurs needs one. A form-pass finding never carries a gate or a prevalence count; its reach may be reported as coverage.

## One session

You do R1 to R6 in one session, in order. Keep your memory in files: `tool.py note` as you work; `tool.py head` at each stage's end and whenever you pause. The controller keeps your files and the session as you go, and one archive at the close. Your context will be compacted when it fills: after a compaction, run `tool.py context` before anything else, and fetch by ID what you need. Before you leave a stage, run `tool.py check <stage>` and fix what it lists; two failed repairs stop the room for J.

## Recovery

J, 6 October 2026: "Keep hidden snapshots as long as the resumed agent can be shown to be accurate to what was running before". This section binds both siblings.

**When.** After `tool.py check <stage>` passes, end your turn: that completed turn is a stage boundary. The controller snapshots it, and the turn you end before the critic, only when no tool is running. A snapshot holds your folder, the native session, the model and effort, the CLI version, the installed contract and instruction files, the tool manifest, the permission profile and the controller's position. The message that opens each stage carries a random boundary token, recorded with the snapshot that closes the stage, and the controller repeats it after each compaction; never write it anywhere. In the field, every leg's opening message carries it. You never see a snapshot.

**Resuming.** After an interruption the controller keeps the interrupted state for diagnosis, restores the last snapshot and resumes the same session, never a fork. Before your next turn it shows that the resumed agent is the one that was running, and records each check in `recovery.jsonl`:

1. identity: the session ID and everything else the snapshot holds, but the folder and the transcript, match;
2. state: the interrupted transcript begins with the snapshot's transcript byte for byte, and the restored transcript and folder match the snapshot's hashes and manifest;
3. recall: a fork of the restored session, given no tools and then discarded, is asked for the boundary token and three questions the controller draws from the turns after the last compaction before the boundary, on what the transcript holds and the folder does not. A fresh agent scores the answers against the transcript. It passes with the token exact and two of the three right.

Any failure stops the room for J; a fresh agent is never presented as you. Where fewer than three questions can be drawn, every one drawn must be right; with none, the token and checks 1 and 2 decide, and `recovery.jsonl` says so. These checks show that the resumed agent holds the same record and context; they do not prove an identical internal state.

**What was lost.** Work after the boundary is redone. The controller says so in its first message and marks its own copies of the log and history lines written after the boundary `lost: true`, outside the stamps and counts; the restore removes them from your folder. A critic that already ran is not dispatched again: its recorded return is served once more. J is told which of his messages came after the boundary and chooses which to deliver again. Snapshots are dropped only after the close's archive verifies. The field runs these checks after any interruption, from its last leg close or named snapshot.

## The stages

| Stage | Global counterpart | What you do |
|---|---|---|
| R1 prior | B1 `prior.md` | Read global §1 and §2, METHOD.md's first section, WRITING.md and the Gioia paper. Then write `prior.md`, before you reopen the codes. You coded this room, so this is not a prior to the data: it records what the coding taught you to expect, so that the model's findings can be told from what you already believed. Say what you expect, what would surprise you, the coordinating-turn rule, the bracketing rule for episodes, and which expected findings rest on words and which on patterns. |
| R2 reading | A1 | Your codes in clock order, block by block; threads opened where meaning needs them. One note per block. `episodes.jsonl` kept current; a block boundary is not an episode boundary. At the end, in `organizing_end.json` (`PROFILE.md`): the hour of the last coordinating act; the aftermath share as global A1 counts it, distinct coded items strictly after hour 73 that coordinate rather than recount, over distinct coded items strictly after hour 73, unavailable when there are none; whether the record says the work remained. Then where it reads differently from your `case.md`. |
| R3 structure | C1 §7 and §8, C2 part A | First, if you choose, the naming step (Theory, above). Then the form pass, global C1 §7: your codes read directly, three sweeps (form, register, what is not said); findings `FP-01` on, in `form_pass.md` prose only, outside the arithmetic. Then the `T4` themes in `fourth/fourth.jsonl` and `fourth/fourth.md`, `dimensions.jsonl`, `assignments.jsonl` (each coder theme, or each code of a split one, to a `T4` theme or a status), `structure.md`, computed counts, and a move for every cut. |
| R4 the model | C2 §1, parts B and C, §5 and §6 | C2 §1 first: the criterion in `notes-R4.md` before pass 1, every pass numbered and kept, and the pass kept that best meets the criterion, not the last. Passes as global C2 runs them: the puzzle first; `model/elements.jsonl`, `arrows.jsonl`, `loops.jsonl`, `history.jsonl`; `concept.md`; `model.md`; `model/story-pN.md` read against every episode. Arrows as global C2 §4 defines them. When the pass you expect to keep is written, end the turn. The critic, a fresh agent served the packet global C2 §6 names, returns errors and one rival partition of your coder themes into `T4` themes; its session is not kept. The packet carries C2 §6's instruction unchanged and, beside it, a versioned sibling reading key: coder themes stand where the instruction says third-order themes, the local ID domains of `PROFILE.md`, and for r/place the three extra checks and error kinds. A model over the 50 KB ceiling is served in parts to the same critic, with a receipt naming every file served; nothing is cut in silence. Where no defensible alternative exists, the critic may return "no alternative partition supported" with its reasons. Answer every item in `notes-R4.md` under rule 13; a fix reopens the loop, and the stopping rule counts from after it. Stop under global §6: two consecutive passes with no `tier_history.jsonl` event, no arrow added, bounded, demoted or withdrawn, and no changed story sentence that names an arrow or element; or a declared stop from the third pass, with written reasons. |
| R5 literature | C3 §1 and §5 | The Puranam, Alexy and Reitzig paper arrives. The global C3 sequence: restate `prior.md` and log the read count in `notes-R5.md`, mark abductive reads, write switch records; a change a paper prompted carries `abductive: true` and `prompted_by` naming the paper (author, year). Then global C3's leg 3: for every `T4` theme, which of the four problems it is a way of handling, or none, with what this room's version cannot do; the unmapped set is the remainder. C3's legs 1 and 2 need shelves you do not hold, so they do not run. *Declared departure from global §2*: a `recalled` name the paper cannot check stays `recalled`, marked unverified, instead of being verified or withdrawn; `literature-C3.md` lists each. `literature-C3.md` and `mapping-C3.jsonl` in the global formats. |
| R6 account and close | C5, E1's claims | `account.md` before any drawing; `propositions.jsonl`; `data_structure.md` (quote, first-order concept, coder theme as coded, its name where you gave one, `T4` theme, dimension), rows showing the range; the controller renders the figure, which you read and correct at the source; `claims.md`; `INTERVIEW.md` under 800 words; then `confidence.jsonl` (below), the last file; `tool.py check close`. |

**A room that did not organize** runs every stage. Its structure may hold no `T4` theme and its model no arrow; each empty file is valid and says why in the account or the notes, and the account states the finding with the counts that carry it. A quota the record cannot meet (episodes, exemplars, a rival partition) is met as far as the record goes and the rest named unavailable; nothing is invented to fill it. An empty model with evidence is a result the study needs.

## Your confidence, before anyone sees the global model

J, 5 October 2026: the global aggregator should know, from a source the global model has not touched, whether you believe what you say. `confidence.jsonl` is the last file you write, one line per object:

```json
{"kind": "room", "id": "", "something_to_explain": "yes|partly|no", "why": "did this room organize around r/place, and how much of the record shows it", "evidence": {"codes": ["c0042"], "episodes": ["E-03"]}}
{"kind": "T4", "id": "T4-003", "grade": "high|medium|low", "why": "how well it holds the material: where it is firm, where thin", "would_change_it": "the observation that would most lower this grade", "evidence": {"codes": ["c0042"], "episodes": ["E-03"]}}
```

Add one line for the model as a whole (`kind: "model"`, `id` empty) and one for every `T4` theme, dimension, element and arrow (`kind` `T4`, `dimension`, `element` or `arrow`, with its ID), in `PROFILE.md`'s format. Say what you think, not what would look good: a room with little to explain says `no` or `partly`, and a model you doubt says `low`. These grades are your belief about your own model, not the `clear|arguable` confidence a dimension carries in `dimensions.jsonl`, and never evidence or a vote at the return.

The controller seals the file at the close, hashed with your model's version and kept where no agent can write, before any global model reaches this room. At the return it is read beside the grades given then, never overwritten.

## What you may not do

Read another room's record or model, or anything the global aggregator wrote; see the canvas or the atlas; edit the coding; launch agents; use a global ID as if it were yours.
