# How to run the tools, v43

Everything works from inside the folder you were given. Nothing reaches outside it. Read this
once, at stage A1. Tools marked *new* do not exist in v37 and are built before the run
(`CHANGELOG-v37-to-v38.md`, "Not yet done").

## Quotes and the store

```bash
python3 tools/cite.py --room hsv --grep "." --n 3              # quotes from a room, a seeded draw
python3 tools/cite.py --room hsv --code c0031                 # one concept's words with offsets
python3 tools/cite.py --room hsv --theme t03 --n 5            # a theme's concepts
python3 tools/cite.py --tier 3rd --id T3-007 --n 5            # exemplars under a third-order theme
python3 tools/cite.py --resolve "the words"                   # which concept holds these words; rejects a label
python3 tools/mem.py room hsv [--no-canvas] [--size]
python3 tools/mem.py forest hsv [63x9ab]
python3 tools/mem.py note hsv
python3 tools/mem.py codes --sub hsv | --theme t03 | --third T3-007 | --grep "discord"
python3 tools/mem.py theme hsv/t03
python3 tools/mem.py where T3-007
python3 tools/mem.py after hsv/c0031 | pairs --level second|third | when hsv
python3 tools/mem.py shelf --list | shelf <name>
python3 tools/mem.py rooms --with T3-007 | --without P07 | --with restrict:P07:T3-014   # new
python3 tools/mem.py contrast hsv denmark                                              # new
python3 tools/mem.py finding F-031 | findings --touching P07                           # new
python3 tools/mem.py adaptations --element P07 [--kind correction]                    # new
python3 tools/mem.py ask "is r/hsv one room or two?" --assume "one room"            # v43: a question for J
python3 tools/mem.py asks [QA1-001] [--open]                                         # v43: the questions and answers
python3 tools/mem.py audit [frame|rooms|retracted|build]                             # v43: A1 package checks
python3 tools/mem.py table --from 3rd | --from 2nd | --room hsv                        # new
python3 tools/mem.py question <slug> | contract --section 3                            # new
python3 tools/mem.py log "opened hsv for the contrast" --kind opened --ids hsv         # new
python3 tools/mem.py diary --last 5 | diary --grep P07                                 # new
python3 tools/mem.py mint --label "..." --trigger hsv:t07                              # B1; after B1 the stamp only (C1 to D6)
python3 tools/mem.py place hsv:t07 --theme T3-007 | unplace hsv:t07                    # B1 only
python3 tools/mem.py reassign hsv:t07 --theme T3-012 --reason "the split"              # new, C1 to D6: a recut's re-placement
python3 tools/mem.py adjudicate <adaptation-id> --decision accept --reason "..."       # new, D3
python3 tools/mem.py diff-scheme <snap> | diff-model <snap>                            # new
python3 tools/mem.py next --stage A1|B1 | progress --stage A1                          # the next room: A1 from order-A1.txt, B1 from the stopping rule
python3 tools/mem.py idea "..." --trigger hsv:t07                                      # a prospective theme, stamped (B1)
python3 tools/saturation.py status --stage B1 | report --stage B1 | order --stage B1  # B1's stopping rule: where it stands, the report, the order
```

Every call is logged to `out/_mem_reads-NN.jsonl` (NN from `--stage`, else the `.stage` file the
harness writes at every hand-over). Pages are 80 lines; `--offset` and `--limit` page through.
Placements, fourth-order themes, dimensions and elements are overlaid from `out/` at query time.

## The fleet's pages

```bash
python3 tools/packets.py B2|B3 --scheme out/scheme_final.jsonl --families out/families.jsonl \
        --to out/_packets-NN [--exemplars]
python3 tools/handoff.py D --verdict-only     # the verdict packets alone, from the frozen MODEL-D1.md and model/
```

The index page, one file per family, a batch's themes with their sibling block; 50 KB ceiling
asserted, end marker appended. The dispatch (`FLEET.md`) is the operator's `fleet.py`, not yours.

## The return

```bash
python3 tools/handoff.py D                       # builds out/handoff-D/ from the frozen model
python3 tools/handoff.py D --recheck hsv,denmark  # the named affected rooms, from MODEL-D3.md
python3 tools/ingest.py D [--check <sub>]  # new: validates DROPS/D, lifts, compiles the ledger
python3 tools/rebuild.py hsv                 # the current local model: accepted, modified and supported particular lines; pending lines listed as unresolved (from the effective adjudicated ledger, tools/adaptation_ledger.py)
python3 tools/adaptation_tree.py --out out    # D4: the adaptation dendrogram as HTML, SVG and JSON
python3 tools/chunk_compare.py --out out --store package/store   # D4: the fixed chunk-share comparison, replayable
```

## Open, close, cut, views

```bash
python3 tools/validate.py --open NN          # startup counts; fails on an unresolved link
python3 tools/validate.py NN                 # the close-check; refuses by name what it cannot check
python3 tools/validate.py --links            # new: every id in head, questions, views resolves
python3 tools/validate.py --self-test        # once, at A1
python3 tools/gen_views.py NN                # new: _views/ and _wiki/ regenerated, hashed
bash tools/done.sh NN [--cut <name>]         # new: close-check, views, snap, tokens, probe, session id
python3 tools/snap.py NN move-<move>-<n>     # a move's snap, taken when the move is made; the leg stays open
python3 tools/counts.py . out/               # the denominators; run it, never read the copy
```

`done.sh` is the leg's one exit. It runs the close-check, the links check and `gen_views.py`,
and marks the leg closed. Then stop: what happens next (the snap, the recall probe in a fork of
your session, the checkpoint) is your platform's, and your platform file says how.

## Your platform

The instrument runs on two platforms, Claude and Codex (since v41). Everything in this folder is the
same on both but two files: `PLATFORM-claude.md` and `PLATFORM-codex.md` name the models, the
efforts, the reader routes and how a leg is opened, closed, paused and compacted. Read yours
(`CLAUDE.md` points Claude to its own, `AGENTS.md` points Codex to its own).

- **Legs.** Every stage is legs; fleet stages are build, dispatch, check; C2 to C5 one leg per
  pass, every move logged and snapped as it is made; D3 one leg per element group. Each ordinary
  leg continues the previous leg's conversation from its committed checkpoint, in the same folder;
  the startup packet (the standing instructions') orients that continuation and does not replace it.
- **`_head.md`** is at most 3,000 words, rewritten at every close and before every cut.
- **Three limits of the runner.** A tool result can be clipped without saying so above a fixed size:
  page long files. A shell call past its timeout is killed: run long scripts in the background
  with output to a file. Nothing in `out/` is deleted.
- **Forks.** The operator may fork the run at a stage boundary (after A1, after C1, after C5,
  and at any cut). You are not told you are a fork; the carried fork is chosen by the rule in
  `RUN.json`, declared before any fork ran.

## Stage 00's builders

```bash
python3 tools/build_store.py --root . --input RUN/INPUT/coders   # drops retracted concepts; writes README-store.md
python3 tools/transitions.py --root .
python3 tools/relations.py --root .                                # new: the mention graph and canvas adjacency
```
