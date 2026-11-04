# Stage D1. The return: the build.

**Model:** as `arm.json` sets for this stage (your platform file lists the model and effort). **Legs:** one.
**Fleet:** none here; D2 runs them. You never run a labeler or a reader and never call a model.

**Steps:** `D1a`, one leg: `handoff.py` writes the folder once per version. Each leg is named by its step (STANDING §2).

**Safe stops:** before `handoff.py` runs (it writes the folder once, so a pause after it is a close). At a safe stop, check for `.pause` (`ls .pause`); if it is there, log where to pick up, your working hypothesis and the next room or item
(`mem.py log "<hypothesis>; next: <item>" --kind pause`), and close with `done.sh D1 --pause` (STANDING §2).

**Startup packet:** `_head.md`, this file, `FLEET.md`, `SCHEMA-adaptations.md`, the last five
diary entries, `validate.py --open D1`. The adaptation shelf arrives (METHOD.md).

**Reads allowed:** `model/` at its frozen hash; `account.md`; `implications-C5.md`;
`propositions.jsonl`; `assignments_final.jsonl`; `_views/data-structure.tsv`; `_wiki/`; the
last `story_rooms-pN.jsonl`; `prior.md`, into which you write §7 and §8 here; `rooms.jsonl` for each room's concept count and
off-platform pointers; `mem.py room --size`; the rooms' coder documents through the verbs.
**Forbidden:** writing any adaptation or verdict yourself; reading `DROPS/`; serving the canvas,
a room note, your notes or another room to any task or packet (rule 7).

**Outputs:** `handoff-D/` with `RETURN-D.md`, `VOCABULARY.json`, `VERSION`, `MODEL.md`,
`LADDER.md`, `tasks/<sub>/TASK.md` and the room's documents,
`tasks/index.tsv`, `HANDLER.md`; `verdict-D/` with `RETURN-D2v.md` and the verdict packets;
`prior.md` §7 and §8; `notes-D1.md`; `handback-D1.md`.

**`prior.md` §7 and §8 first.** Before you build anything, and before any adaptation is seen,
write the distance weights and grades for stage D4 (§7) and the concept floor and the
off-platform threshold for `cannot-tell` (§8), each with one line on why that figure. §7 carries
two lines in the form `distance.py` reads: `w = <third>, <fourth>, <dimension>, <target>` (the
weight of a meeting at each level) and `g = <same op>, <same kind>, <different kind>, <opposite>`
(the grades). You set them now because the model is fixed and no room has yet answered it.
`done.sh` records `prior.md`'s hash at D1's close (`out/_closes/prior-D1.sha256`), and stage D4
refuses weights that changed without a departure (rule 10).

**The model is fixed.** Nothing here changes an element, an arrow, a fourth-order theme or a
dimension. What a room does to the model is written against the model by a labeler and ruled on
at D3; a change after C5 is a D3 amendment under rule 11, logged with the adaptation lines that
caused it. This is the test the loop prepared for: stage C2 read rooms against every telling of
the story, and the rooms its last story could not tell are the first ones to watch. List them in
`notes-D1.md` from `story_rooms-pN.jsonl` before you build anything, so that D3 can count how
they fared. The return is Eisenhardt's replication only if something is predicted before it is
seen; `EXPECTATIONS.jsonl` is that prediction, and it is written here, before any return exists.

## 1. The handoff folder (SCHEMA §9)

`handoff.py D` builds it from your inputs; you check it and write what the script cannot. Before you run it, write the two files only you can write: `MODEL-D1.md` (the model as prose with ids, below) and `EXPECTATIONS-D1.jsonl` (below). The script copies them in, projects the rest from `model/`, the scheme, `fourth/`, `dimensions.jsonl`, `assignments_final.jsonl`, the store and the coder documents, writes `VERSION`, hashes the folder into `handoff-D.sha256` and `RUN.json`, and prints the payload distribution for §3. It will not overwrite a built folder.

- `RETURN-D.md`: the return specification for the labelers, verbatim in every task: the two
  outputs, the ledger line and its fields, the operations with their required fields, the room
  model's form and its grade line, the end marker, the reissue rule, the rule that every claim
  carries a node id and a concept id, the rule that free text lives only in `how`. The template
  ships with this stage; you do not rewrite it, and a defect in it goes to `handback-D1.md`.
- `VOCABULARY.json`: the id vocabulary at the frozen model version: every element
  with id, kind, statement, tier and dimension, every arrow with id, kind, from, to and
  mechanism, and `status: tentative` where an entry is one; every third-order and fourth-order theme with id
  and name; the dimensions. Nothing else. Arrows are in it by id, so a room instantiates,
  restricts or contradicts an arrow as it does any element; an arrow with no concept in the
  room is not instantiated there.
  An element or arrow entered at stage C4 from the field carries `status: tentative` and nothing
  else that says where it came from; it goes to every room, which answers it from its own record
  like any other element, silence included (J, 2026-09-29). The mark `from-field` stays in
  `out/sealed/FIELD.jsonl`, which `handoff.py` writes and never serves; stages D3 and E1 read it
  and report the field's entries apart. An element on a form-pass tier (`FP-01` ...) also goes to
  every room, since no second-order theme lifts to it; its unit is the turn, and a room answers it
  from its turns.
- `VERSION`: the hash of the model and its tiers as `done.sh` recorded it at C5d's close (`out/_closes/model-C5.sha256`). `ingest.py` rejects a
  return written against any other version, whole, and the handler reissues it.
- `MODEL.md`: the global model as prose with ids, from `account.md`, cut to the ceiling the
  labeler's context allows and declared in `notes-D1.md`, with an entry for each of the elements
  the room's second-order themes were placed under appended per task. Every arrow in it reads
  *when X, Y follows, because Z*; it describes the universe, not the mode, so that a labeler can
  read an odd room as one way of running the same structure. Nothing in it refers to a room
  note, a branch, your notes or the canvas.
- `LADDER.md`: the coding table from quote to aggregate dimension with representative concepts
  for every tier the model uses, projected from `_views/data-structure.tsv` for the dimensions and
  elements in `MODEL.md`. A labeler that sees only its own concepts cannot understand a
  dimension, so it cannot say what the model fails to explain.
- `EXPECTATIONS.jsonl`, sealed in `out/sealed/` (out of the handler's and the labelers' reach), per room, from `implications-C5.md`, `propositions.jsonl` and the room's
  placements, which elements the model expects to instantiate and which to be absent, one line:
  `{"sub": "...", "expect_instantiate": ["P07", "A03"], "expect_absent": ["P03"], "from":
  ["implications-C5 §2", "placements"], "why": "one clause per element, in the model's terms"}`.
  Rule 6 governs every `expect_absent`: an element the room had no opportunity to carry is
  `not-testable-here`, not expected absent. Sealed by the harness, kept outside the readers'
  and the labelers' directories, never served, scored at E1. This is what makes the return a
  replication and not a re-reading.
- `tasks/<sub>/TASK.md`: the labeler's instruction (the template ships with this stage): read the
  coder documents, rewrite `case.md` in the model's vocabulary as `model-D.md`, write
  `adaptations.jsonl`, grade the fit; the room's `case.md`, `codes.jsonl`, `themes.jsonl`,
  `brief.md`, `forest.md` (the room's coded threads as reply
  trees, `trees/<sub>.md`, so that `evidence.transitions` rests on the forest); `placements.jsonl`, the placements of the room's
  second-order themes (third-order theme, fourth-order theme, dimension, or none); where the
  outputs go. Not in any task: the room note, the account beyond `MODEL.md`, your notes, the
  propositions, any canvas field, any other room. A labeler who sees a large area grades a
  success; rule 7 names this fleet.
- `tasks/index.tsv`: one row per room with `items_in_window` and the payload in bytes from
  `mem.py room --size` plus the documents served; the handler dispatches by it, size ascending.
- `HANDLER.md`: the adaptation handler's brief (ships with this stage): dispatch by size
  ascending; how to run a labeler in Codex, one fork of the matching original case-lead checkpoint per room, the model and session
  id recorded in `DROPS/D/<sub>/run.json`; the per-room check `ingest.py --check <sub>` and the
  repair; the return path `DROPS/D/<sub>/`; that completion comes before any limit and the
  handler marks a room `unreturned` in `DROPS/D/UNRETURNED.tsv` only when it cannot return it;
  `DROPS/D/DONE` with the counts; what never to do (no access to `out/` beyond this folder, no
  edits to the vocabulary, no merging of rooms, no summarising the model for a labeler).

## 2. The verdict fleet's packets

`handoff.py D` writes them too, into `verdict-D/` (`--verdict-only` rebuilds them alone): per room, the model as prose with ids, the room's second-order
themes with their placements, the room's concepts the model did not use (those of themes placed
nowhere, and a seeded sample of those no element cites), the verdict criterion from FLEET.md §3
verbatim, and none of the coder's prose (no `case.md`, no theme notes), no other room, under
the 50 KB ceiling with the end marker and the line telling the reader to confirm it reached it.
The concept floor and the off-platform threshold for `cannot-tell` are read from `prior.md` into
the specification, and each packet states the room's concept count and off-platform pointers
from `rooms.jsonl` beside them, so that the reader does not estimate what the store already
holds; every verdict carries the count (contract §5).

`RETURN-D2v.md`, frozen with this file, and `RETURN-D2v.schema.json`, which `fleet.py` checks every
line against (`tools/dreturn.py`): the verdict, the themes and the unused concepts it rests on,
one sentence, the end marker. The return line:

```json
{"sub": "...", "reader": "r1", "verdict": "composes|composes-with-residue|does-not-compose|cannot-tell",
 "themes": ["t03", "t07"], "concepts": ["c0041"], "residue": ["t11"],
 "cannot_tell_under": "coded-share|off-platform|both|null",
 "sentence": "one sentence, in the criterion's terms", "served": "<sha256 of the packet>"}
```

The reader's id is the name of its return file (`ingest.py` sets it). `residue` lists the themes
or concepts with no element and is null unless the verdict is
`composes-with-residue`; `cannot_tell_under` names the threshold and is null otherwise. `R = 2`
readers per room, so that a disagreement is visible (FLEET §1). A verdict is one value and is a
reading with a reason, never a profile, a score or a coordinate: stage D4 projects it onto the
branches afterwards and never clusters on it.

## 3. The payload, measured

Before the folder is hashed, write in `notes-D1.md` the distribution of task payloads and of
verdict packets (median, p90, largest, from `tasks/index.tsv`), the ceiling declared for
`MODEL.md` and what it cut from `account.md`. No stage carries a budget (contract §4): a room
whose documents exceed what one labeler session can hold is not cut, not split and not read by
you; name it in `notes-D1.md` and `handback-D1.md`, and the handler returns it whole or marks
it `unreturned` with the reason. The tokens go to `RUN.json` through `done.sh`.

## 4. What you check

Every task resolves every id it names against `VOCABULARY.json`; no task and no packet holds a
canvas field, a room note or another room's material; every room of the analysed set has a task,
an `index.tsv` row and a verdict packet; `MODEL.md` fits the declared ceiling; `EXPECTATIONS.jsonl`
has a line per room and sits outside both served folders; `VERSION` equals the harness's hash of
`model/`; the folder is hashed and the hash is in `notes-D1.md` and `RUN.json`. A room whose
task could not be built goes to `handback-D1.md` with why; you do not invent a document.

## Moments to log

The story-miss rooms listed; the ceiling declared; each expectation line written that departs
from a plain reading of `implications-C5.md`, with why; the payload distribution; the folder
built and hashed; any room whose task could not be built and why.

## Final message

Counts: tasks built, verdict packets built, elements and arrows in the vocabulary, the
`MODEL.md` ceiling, expectations written (instantiate and absent, by element), rooms
`not-testable-here` on any element, story-miss rooms carried, the largest payload; the folder's
hash and `VERSION`. A return value.

## Close

**Stop here.** `done.sh D1 --cut packets-out`; `handback-D1.md`; the head; the closing diary line. Your session ends. The labelers run in Codex and the verdict fleet on the reader route without you, and nothing of the return (D1 to D3) runs on your model until D2 is launched as the check leg, told that the labelers and the readers left their files in `DROPS/D/` and `_fleet_raw/D2v/`.
