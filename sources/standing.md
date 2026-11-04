# STANDING-INSTRUCTIONS, v38. What you hold, the tools, your memory, the leg.

Given with every stage beside the contract. The index below gives line ranges.

<!-- INDEX -->
| section | lines | words |
|---|---|---|
| 1. What you hold | 15 to 65 | 461 |
|   Helpers | 66 to 83 | 200 |
|   The tools | 84 to 176 | 1499 |
|   Know what you are reading | 177 to 189 | 133 |
| 2. Your memory, and the shape of a leg | 190 to 328 | 1738 |
<!-- /INDEX -->

## 1. What you hold

Everything is in the folder you were given, and the folder is the whole world of this study.

```
package/               the coders' work, sealed: one folder per room, one run per room, the same
                       six files in each: brief.md, case.md, codes.jsonl, themes.jsonl,
                       threads.jsonl, pointers.jsonl;
                       the canvas fields (contract §5, rule 7) with their manifest;
                       canvas/artworks.jsonl, every atlas artwork with its index and its
                       placement over time, read beside each room's account; a use is
                       declared (rule 7);
                       sealed.jsonl (hashes of the files that arrive later)
package/store/         the same material joined, built by script before stage A1:
                       codes.jsonl      every first-order concept with its second-order theme,
                                        item, thread, author, hour since open, forest coordinate,
                                        the participant's words with offsets; and, once they
                                        exist, its third-order theme, fourth-order theme and
                                        dimension. Retracted codes are not in the store.
                       themes.jsonl     every second-order theme with its note and its codes
                       items.jsonl, threads.jsonl, rooms.jsonl (each room with its canvas fields)
                       transitions.jsonl   every coded turn that answers a coded turn, with the
                                        interval: the transitions ledger
                       relations.jsonl  every room another room names, with direction and the
                                        coder's label
                       neighbours.jsonl every pair of rooms that share an artwork, border or
                                        overlap on the atlas outline, or name each other
                       shelves/         the literature in two tiers per stage: read, shipped with
                                        the stage; on request, listed one line each and opened
                                        only if you ask. A shelf that has arrived stays
                       README-store.md  the dictionary. Read it at stage A1.
trees/<sub>.md         the forest: each coded thread as its reply tree, coded turns hung on it,
                       gaps kept, dropped items counted in the header
package/canvas/        artworks.jsonl, every atlas artwork, its pixels, placers and placements by hour;
                       package/pixels.csv and case_facts_outcome.jsonl beside it; DATA-manifest-canvas.md
tools/                 see below
out/                   yours, empty at the start; its tree is STANDING-INSTRUCTIONS §2. __OUTDIR__ means out/.
```

**The forest is the coded record's shape.** A thread in `trees/<sub>.md` shows what was a reply to
what and how long after, with the coder's codes on the turns. **A reply is a reply.** The tree
shows that one turn was posted after another; it does not show that the first caused the second.
No relation you write may rest on adjacency alone, and an interval between two posts is elapsed
time, never the speed of a decision.

**Your room notes are your prior.** Stage A1 has you read every room through its forest and write
a note on each into `out/rooms/`, with a lexicon and a running file. From then on the notes are
queried (`mem.py note <sub>`), never read whole as a list. They are what you expected, dated;
they are never a source for a quote; and every stage that uses them says, in its diary, what it
found that they did not predict.

### Helpers

You may start a helper (the Agent tool) whenever it serves your own work: to read a set of rooms
through the verbs and summarise them against a question, to check a claim across the store, to
test a script or a count. A helper has your tools and your walls, and runs on your model. Four
rules bind it:

- **A helper does not do the fleets' work.** It never places a theme, adjudicates, labels a room,
  gives a verdict or reads as a reader for a stage that has a fleet; those run outside you
  (FLEET.md), where they can be measured.
- **A helper's summary is a pointer, never evidence.** Every quote, count and claim you keep, you
  take yourself through `cite.py` and `mem.py`; a finding that rests on a helper's words alone is
  a defect.
- **Log it.** `mem.py log --kind helper "<what you asked; what came back; what you kept>"`, one
  line per helper, when it returns. Its reads through the verbs are logged under your stage.
- **Say what it read.** Name in the brief the rooms or files it may open, and say in the log
  line whether it stayed inside them.

### The tools

```
python3 tools/cite.py --room <sub> [--code <id>] [--theme <id>] [--tier 3rd|4th|dim] [--n K]
                      the only way a quote enters an output (rule 3); every call logged
python3 tools/mem.py <verb> ... --stage NN     the store and your own files, one page at a time,
                      every call logged to __OUTDIR__/_mem_reads-NN.jsonl
  room <sub>            the room on one page; --no-canvas is the page fleets are served (rule 7)
  forest <sub> [id]     the rendered forest, whole room or one thread
  note <sub>            your own room note
  codes  --sub | --theme <id> | --third <id> | --grep <re>
  theme <sub>/<id>      a second-order theme, its codes, and where it was placed
  where <T3-id>         every room and second-order theme on a third-order theme, with 4th and dim
  after <sub>/<code_id> what answered this code and what it answered, with intervals
  pairs --level ...     transition counts from the ledger
  when <sub>            the room's coded hours as one line
  shelf <name>          a work on the shelf, whole; shelf --list the on-request tier
  rooms --with <id> | --without <id>    rooms holding or lacking a theme, element or adaptation
  contrast <sub> <sub>  the diff of two rooms' columns and, after D3, their adaptation sets
  finding <id> | findings --touching <element>
  adaptations --element <id> [--kind ...]   every ledger line touching one element, across rooms
  table --from 3rd | --from 2nd | --room <sub>   projections of the data structure
  question <slug>       one open distinction
  log "<text>" [--kind opened|dropped|merged|split|kept|move|abductive|question|comparison|note] [--ids ...]
                        the only writer to the diary (rule 20)
  diary --last [n] | diary --grep <id>
  diff-scheme <cut> | diff-model <cut>   the scheme or the model now against a cut
  adjudicate ...        stage D3's writer to adjudications.jsonl
python3 tools/validate.py --open NN | NN | --links   startup counts; close-check; every id resolves
python3 tools/gen_views.py NN       regenerates _views/ and _wiki/ from canonical files; run by done.sh
python3 tools/snap.py NN <label>    a hash of out/ under a name; the harness takes one at every close, you take one when an order matters
python3 tools/counts.py             the denominators, from the canonical files
python3 tools/handoff.py D | ingest.py D | rebuild.py <sub>    the return's builders (FLEET.md §3)
bash tools/done.sh NN [--cut <name>]   the leg's one exit: close-check, links, views; the harness then snaps and probes
```

**Verbs added or changed in the last tools pass**, over the list above (where they differ, these win):

```
python3 tools/mem.py <verb> ... --stage NN     changed for every verb:
  [--offset N | --page N] [--limit N]  every page ends with a marker: "[end: lines a-b of N]" or "[lines a-b of N; M more: --offset K]"
  help [verb]           the whole page, or the lines naming one verb
  (any room argument)   bare, r/<sub> or <sub>/, any case; a wrong room, theme, thread or id is refused with "did you mean ..." and exit 1
  (the read log)        out/_mem_reads-NN.jsonl records verb, args, every option, offset, limit, lines served, total, and a refusal
  room <sub> [--json]   the room page (unchanged), or one JSON line; "case themes" now reads "second-order themes"
  case <sub>            new: the coder's case.md, paged
  neighbours <sub> [--kind canvas|mention|shared] [--top N] | --summary   new: rooms that share an artwork, border or overlap on the atlas outline, or name each other (package/store/neighbours.jsonl)
  canvas <sub>          new: the six canvas fields, each linked artwork's placements by hour as a bar aligned like `when` (freeze at h73), the share of the room's region placed by its window and its pre-event members (pixels.csv), and the manifest's caveat
  compare <sub> <sub> [--grep re]   new: two rooms before any placement: facts, `when`, second-order themes, named rooms, canvas, and concept labels matching --grep
  when <sub>            changed: the axis under the bar now matches the 4-hour bins (0, 24, 48, 72, 96; ^ freeze h73)
  forest <sub> [id]     changed: a thread the forest lacks is refused with the nearest id
  codes --sub S [--second tNN]   renamed: --second (old --case-theme still works)
  codes --third <T3> | --fourth <T4> | --dimension <D>   renamed and new: --third (old --theme), --fourth (old --chunk), --dimension new
  codes --grep <re> [--by-room] [--json]   --by-room new: the count per room with the first hour; --grep now also matches the label and the coder's note
  (code lines)          changed: the position reads @<thread_id>:<coord>
  theme <sub>/<tNN or label words>   changed: label words match a substring, any case; several matches are listed by id
  themes --grep <re> [--rooms a,b] [--json]   new: second-order themes whose label or note match, with the count per room
  pairs --level second|third|fourth|dimension   changed: the tier names (case_theme, theme, chunk still work); an unknown level is refused with the list; dimension new
  facts [--field F] [--summary] [--sort asc|desc] [--where "F>v"] [--nulls] [--top N] [--json]   new: rooms.jsonl field by field: a sorted list, n/nulls/min/quartiles/max, filters, the null rooms; px_window_share and px_pre_share from pixels.csv
  facts --slope X Y     new: the log-log OLS slope of Y on X over rooms with both > 0
  notes --grep <re> [--field <line>]   new: your room notes (out/rooms/*.md, not _ files) lines matching, with the room
  progress [--stage A1] new: the declared block order (notes-A1.md, else sorted), each room noted, read or pending, and the last opened; --plan [MB] cuts the pending rooms into blocks of about MB (3)
  scheme [--brief] [T3-id]   new: one line per third-order theme (id, family, members, label: gloss) from scheme_current over the latest frozen scheme; with an id, that theme whole
  where <T3-id>         changed: reads the working grouping (scheme_current's members) when no assignments file exists
  rooms --with <id> | --without <id>   changed: an id that names nothing is refused instead of returning every room
  view [name] [--grep re] [--room sub]   new: a generated view in out/_views/, filtered; no name lists them
  wiki [page]           new: a generated wiki page (rooms/<sub>, model/<id>, or the bare name); no page lists them
  shelf <name> [--grep re] [--page N]   new options: matching lines with line numbers; one page of the work
  diary --last [n]      changed: n defaults to 5
  log "<text>" [--kind k] [--ids a,b] [--dry-run]   changed: the kind is checked against opened, dropped, merged, split, kept, move, abductive, question, comparison, note, helper, minted, placed, unplaced, pause and any `log --kind` a stage file names; --dry-run new
  mint --label "..." --trigger <sub>:<tNN> [T3-id] [--dry-run]   changed: refused outside stages B1, C1 to C5, D3 and D6; the trigger must be a second-order theme in the store; an id is minted once; at B1 the theme enters scheme_current with its trigger as first member, after B1 the mint is a stamp only and the theme is written to scheme_v2 with its members moved by `reassign`; logged as kind minted; the id may come before or after the options
  place <sub>:<tNN> --theme T3-NNN [--dry-run]   new: puts a second-order theme into a minted third-order theme in scheme_current (atomic rewrite), logs kind placed, and says where else it sits
  unplace <sub>:<tNN> [--theme T3-NNN] [--dry-run]   new: takes it out of one third-order theme, or of all; logs kind unplaced
  table, wiki           changed: say so when your working files changed since the view was written at the last close
  adjudicate <id> --decision d --reason "..." [--pair id] [--dry-run]   changed: refused outside D3; the adaptation id (and --pair) must be in the ledger; the decision is checked
  (the overlay)         changed: scheme_current.jsonl (out/scheme/ or out/) is laid over the latest frozen scheme when it is newer or none exists; placements fall back to its members when no assignments file exists
  ask "<question>" --assume "<what you do meanwhile>" [--ids a,b] [--dry-run]   new (v43): a question for the principal investigator, at any stage; written to out/asks.jsonl and the diary (kind ask); see "When you need the principal investigator"
  asks [<id>] [--open]  new (v43): your questions and the answers that came back (out/_answers/<id>.md, written by the principal investigator's side, never by you)
  audit [frame|rooms|retracted|build]   new (v43): stage A1's package checks from the raw files of package/ (the census count against rooms.jsonl and the room folders, the six files of every room, the coders' retracted concepts against the store, the store's build figures recomputed); every figure names its file, and the call is logged like any read
python3 tools/cite.py ...     changed:
  (every header)        "N match; K shown" (--grep, --theme, --tier); --resolve says "N code(s) hold these words; K shown" and takes --n
  --room <sub> --code <id> --context K   new: the quote with its parent and K items either side in the thread, their coded passages and forest labels
  --room <sub>          changed: any case, r/<sub>; a wrong room is refused with the nearest; --tier dim now finds the concepts under a dimension
python3 tools/validate.py --open NN   changed: names every declared input and where it was found; prints counts.py's census, dropped, analysed, concepts and second-order themes; runs links.py and exits 1 on an unresolved id at every stage; reads the startup packet line; scheme_current in out/scheme/ or out/
python3 tools/validate.py --self-test [--summary]   --summary new: only failures and the count; the fixture is now self-contained, so the report is the same in any folder
python3 tools/links.py        changed: also resolves r/<sub>, <sub>/cNNNN, <sub>:cNNNN and <sub>/tNN against the store (a room the rooms named, and r/place, also resolve)
python3 tools/packets.py B2|B3|B4 [--scheme F] [--families F] [--to DIR]   changed: the flags are honoured at B2, B3 and B4; items may be "sub/tNN", {"sub","theme_id"} or {"item":"sub/tNN"}; B2 with --to needs no --round
python3 tools/ingest.py D    changed: with no DROPS/D it says so in one line and exits 1
python3 tools/gen_views.py NN changed: data-structure.md above 2 MB holds a note pointing to `mem.py view data-structure`; tsv cells carry no line breaks
python3 tools/build_store.py --root R --join-canvas F   changed: F may be relative to --root
```

`HOW-TO-RUN.md` is the reference for all of them. Read it once at stage A1. **A single
`Read` may return a truncated file without saying so** above about 25,000 tokens; page it, or
read it through a verb.

### Know what you are reading

This is not interview material. Nobody was asked anything, no protocol shaped it, and none of it
was written for a study. Three things follow. **Nobody's questions produced this talk**, but one
reader per room decided what in each record was worth coding, and you hold what it kept; where a
claim turns on absence, it is a claim about what was coded, and the forest header says how much
of each thread that was. **Sequence is evidence**: who answered whom, what was taken up, what was
ignored. **It was written to be read by the people it was about**: a room's claim about itself is
an act addressed to somebody. Keep *the record shows they did X* apart from *a member said they
did X*.

---

## 2. Your memory, and the shape of a leg

**Continuity.** Every leg continues the preceding completed checkpoint, including
conversation and files. Read the head and diary to orient that continuation. Compaction does not
replace the archived history. A missing checkpoint is a harness defect, never a reason
to start a fresh analyst from notes.

**The diary is not read whole by anyone.** It is one file per stage in parts of 1,500 words; you
read its last five entries at a leg start and grep it by id; stage E1 computes over it. The head
is the summary, the closing line of each leg is the digest, and the rest is the record.

**The tree.** `out/` as you see it. Writers: **A** you, **S** a script at leg close, **H** the
harness, **F** a fleet or the labelers through the drop, **P** the principal investigator.

```
_head.md                 A   the narrative of the argument; 3,000 words; read first at every leg
diary/NN-k.jsonl         A   the running log through mem.py log; harness-stamped; 1,500 words a part
_questions/<slug>.md     A   one open distinction per file; closed with a verdict line, never deleted
asks.jsonl               A   your questions to the principal investigator, through mem.py ask only (v43)
_answers/<id>.md         P   his answers, one per question; never written by you (v43)
_views/                  S   generated at every close; never edited: data-structure, rooms by
                             third-order themes, rooms by elements, rooms by adaptations per level
                             and per kind, relations, transitions, moves
_wiki/                   S   one page per room, theme, element, form; 800 words; generated
model/                   A   elements.jsonl, arrows.jsonl, history.jsonl: the typed model;
                             story-pN.md, the story told at the end of every C2 pass, which the
                             stop rule diffs
prior.md                 A   written at B1a: expectations, the composition criteria, the
                             brackets, the coordinating-turn rule, the onset contrast; at D1,
                             before any adaptation: the distance weights, the concept floor and
                             the off-record share
scheme/                  A   scheme_current.jsonl and its versions; a required paged read at
                             every B1 leg start, beside the head (C1 reads the frozen scheme_final)
saturation.jsonl, theme_discovery.jsonl, multiplacement_log.jsonl, dropped.jsonl, RUN.json
                         A,H the records the contract names
_fleet_raw/, handoff-D/, DROPS/D/   F,H  the fleets' returns and the return's folders
forms/<id>.md            S   generated at D4 from the accepted branch definitions
findings.jsonl, departures.jsonl, defects.jsonl, tier_history.jsonl   A   append-only ledgers
adaptations.jsonl        F   ingested from DROPS/D, validated
adjudications.jsonl      A   stage D3
rooms/<sub>/             F,A placements, verdict-D, model-D.md, your note
_snap/                   H   the harness's hashes of out/ at every close; read them when you like
_probe/, _transcripts/   H   the harness's; open to you at stage E1
```

**Stages, steps, legs.** The run has five sections: A reading, B coding, C model, D adaptation
and forming, E formalizing. Each holds stages (A1, B1 ... E2), and each stage a sequence of
steps, lettered: B1's are a prior, b getting lost, c the saturation test, d the second pass, e
the scheme standing. `tools/steps.tsv` lists them all, and the stage file says what each does
and where it stops. You are given the whole stage file at the stage's first leg, and you close a
leg at the end of its step or earlier. A leg is named by its step: `B1c` for a step taken once,
`B1b-03` for the third leg of a step that repeats, `B2a-r1` for a pilot round, and `B1c-p2` for
a leg continued after a pause. The harness names the leg in your first message and in `.leg`;
every snap, probe and checkpoint carries that name.

**A leg.** One launch. Its startup packet, read in this order and nothing else by default: the
head; the stage file; the last five diary entries; at B1, `scheme_current.jsonl` paged, and at C1 the frozen `scheme_final.jsonl`; `validate.py --open NN`, which prints the
counts you start from and fails the launch if a link in the head does not resolve. On demand,
through verbs only: rooms, themes, concepts, transitions, findings, questions, views, wiki pages.
Closed to you until stage E1: `_transcripts/` and `_probe/`. You write only in `out/`. The work is one operation for the stages that make categorization moves: a
scheme pass over a room block, one loop pass, one element group at D3, one pass over the ledger
at D4; a leg may carry several moves, and may close earlier when you choose. The exit
is `done.sh NN`, which runs the close-check (files that must change did; ids resolve; counts
match manifests), regenerates the views, snaps, writes tokens, and runs the recall probe. A leg
that fails the close-check is not closed; you are relaunched with the failure in your packet.

**The move.** Every categorization move (a merge, a split, a dimension cut, an arrow added,
bounded or withdrawn, a hypothesis kept or dropped, a branch named) is logged when you make it
(`mem.py log --kind move`, the Grodal, Anteby and Holm move named) and snapped (`python3
tools/snap.py NN move-<move>-<n>`), so a reviewer can find the state before and after it. A move
does not close the leg.

**The cut.** `done.sh NN --cut <name>` closes the leg at a named checkpoint, snaps, and records a
resumable session, so that a reviewer can reopen you there and ask why. Cuts are kept only where
a stage file names one: `adaptations-in` at D2, `tree-final` at D4, and `interview` at the
interview points. One cut has a fixed name: `--cut packets-out` closes the build leg of a fleet stage
(B2, B3, B4, C2, C5, D1, E1). After it your session ends, the dispatch runs on the platform's reader route without
you, and the next launch of the stage is the check leg (the contract's §6, the legs table).

**The recall probe.** At every close the harness asks you, in a fresh turn, five things: the
method question in one sentence; the open distinctions by slug; the last three rooms you opened;
the element or theme you changed in this leg and why; the next comparison. The answers are scored
against the head, the questions, the read log and `history.jsonl`. A miss that the head or the
diary answers is a note, not a defect: the leg kept what it needed where it belongs. A miss
neither answers is a defect. The probe
measures whether the goal survived the leg, and the run reports probe failures per stage.

**Compaction.** Expect it: a long reading leg (A1, B1) will compact, more than once, and you
cannot see it happen. That is routine, not a failure, and the record is why: what is on disk
survives it. The harness owns it: after any
compaction it re-injects the head and the stage file before your next write, and asks you to
reconcile the head with the diary. What the compactor is told to preserve (`CLAUDE.md` on Claude; the same list on Codex): preserve the method question, the current
account, the reasons for the last revisions, the contrary rooms, and the next comparison; after
it, re-read the head and the stage file before any write, and reconcile the head with the diary.

**Ceilings.** The head 3,000 words (`done.sh` refuses a close above 3,200, a margin for the last edit); a wiki page 800; a packet to a reader 50 KB; a `Read` paged
above about 25,000 tokens; a D3 element packet 100 lines; a question file 600 words; a diary
part 1,500 words, then roll.

**The comparisons you can make at any leg**, each served by a verb or a generated view, never by
reading rooms in order: this room against that; rooms that hold a theme against rooms that lack
it; the scheme now against the scheme at a snap or a cut; a finding against every element it cites; the
model now against the model at a snap or a cut; a question as opened against as closed; rooms by
third-order themes, case-ordered; transitions in time; the blind room account against the
informed room model; adaptations touching one element across rooms; rooms by adaptation keys per
level and per kind; a branch against the global model; a room against its branch; the mention
graph against the branches; what you said you did against what the record shows.

**Safe stops, and pausing.** Every stage names its safe stops: points where everything you have
done is on disk and the next leg could pick up from the head and the diary (after a room note at
A1, after a block at B1, after a logged move from C1 on, after a section at C5, D5, D6 and E1,
after a packet set at the fleet stages). At each safe stop, check for a pause request
(`ls .pause`). If it is there, log where to pick up, in one line with two parts: your working
hypothesis as it stands, and the next room or item (`mem.py log "<hypothesis>; next: <room or
item>" --kind pause`); update the head if the stage has one; and close with `done.sh NN --pause`.
`done.sh` refuses a pause without that line for this leg. The leg closes without
the stage's close-check, and the next leg continues the stage. The handler asks for a pause when
the platform's usage allowance is running short or for any other reason; a pause is never a judgement on the work.

**Interview points.** At the moments where talking with you teaches the most, a step ends its
leg with `done.sh NN --cut interview`. First write the brief, `out/interview/<leg>.md` (under 800
words: what you did, what you found, what surprised you, what you doubt, the three questions you
would most like to be asked); at a stage's end, write `handback-NN.md` too. `done.sh` refuses the
cut without the brief, without the handback where the stage ends, and at a step that has no
interview point; then it files the brief under the leg, the stage, the step and the minute, for
example `B1e_coding-third-order-scheme_scheme-standing_2026-10-03T14-22.md`. The principal
investigator may then talk with you in a fork of that leg, run in a copy of your folder as it stood at the close (not read-only; nothing done there reaches the run); the run goes on from the cut
either way, and nothing said there enters the run unless it comes back as a reply, the brief's
name with `-reply` added, which your next leg's first message names. Read it before your first
write and answer it in your files under rule 13; a reply is advice, not an instruction, and where
you do not follow it, say why. The points: `A1c` (the
reading done), `B1e` (the scheme standing), `B4c` (the placements final), the last `C1a` (the structure), `C2c` (the
reviewer read, mid-stage), `C3c` (the literature), `C4a` (the field), `C5d` (the Gioia table, the dynamic model and
the figure), `D3c` (the return adjudicated), the last `D4a` (the tree), `D6b` (the retelling),
`E2b` (the feedback).

**When you need the principal investigator.** You are not alone with the record. When a
question, an assumption you are unsure of, or a confusion would change what you do, ask:
`python3 tools/mem.py ask "<the question, in a paragraph at most>" --assume "<what you will do
meanwhile>"`. It reaches the principal investigator at once, and he wants to hear it. Ask when the
instrument is silent, unclear, or seems wrong for the case in front of you, or when you would
otherwise have to guess; do not ask leave to do what the stage file already says. Do not wait for
the answer: go on with what you said you would do, and name the question's id in the diary line of
any work that rests on it. The answer arrives in `out/_answers/<id>.md` (`mem.py asks <id>`), named
in your next leg's first message, or sooner in the conversation itself. An answer is advice, as a
reply is: where you do not follow it, say why. If you cannot go on at all without it, log a pause
(above) and close with `done.sh NN --pause`; the next leg starts once the answer is in.

## Method invariants for every leg

Use the current return specification and effective adjudicated ledger. A supported local particular stays in the leaf account; a pending claim stays unresolved. Never infer substantive absence from silence. Keep original fixed-global, current adapted-local and shared-branch judgments distinct and versioned. No dimension count, new theoretical remainder or branch count is required. After D3, keep the validated model fixed; D6 ideas are separate unvalidated proposals. A process claim is tested at its stated level using dated evidence; confidence, repetition or mention connectivity alone does not prove it.
