# Notes, stage E1: the audit

## E1a: the scripts

**The close-check report of D6a-18** (`_closes/D6-D6a-18-20261027T153104Z.validate.txt`): 0 errors, 0 warnings.

**What this leg did.** It wrote the scripts of stage E1 section 1, as the stage file declares them, and ran each once. Every script is in `audit-E1/`, with its rule in its docstring, declared before it ran, and its output beside it under the same stem. A stranger reruns one with `python3 out/audit-E1/<script>.py > out/audit-E1/<output>`. Where a first run had a fault, the output was kept under a `.superseded-N` name and the fault is named in the script's docstring or in the diary. The readings by hand that the scripts call for are left to the audit sections.

| script | output | what it computes | result |
|---|---|---|---|
| `quotes_resolve.py` | `.json` | every quote in every output, resolved against the store's participant words, labels, case accounts, the instrument's texts and the instructions | 3,230 cited concept quotes; 3,218 resolve to the concept they cite; 12 do not (2 to nothing, 2 to another concept, 1 to a label, 7 return lines quoted beside an evidence citation); 2,042 uncited spans of five words or more resolve to nothing; five spot-checks drawn by seed |
| `links_check.py` | `.txt` | `links.py` and `validate.py --links` | both exit 0; 3 files checked, all ids resolve |
| `quote_check_raw.py` | `.json` | the handler's `quote-check-E1.json` (seed 13, 80 rooms) | code_quote_found_share 1.0; case_quote_found_share 0.6573; 389 missing strings listed against 548 by the file's count; 227 of the 389 are in the room's coded passages once case and end punctuation are set aside |
| `store_figures.py` | `.tsv` | README-store.md, A1's recomputation and now, three columns | all 16 figures agree; the 158,227 item lines hold 137,732 distinct ids, 21,011 in the unnamed state `collapsed` (A1's defect) |
| `coverage.py` | `.json` | room, forest and case records in the read logs, by log | 705 rooms read by `room`, 705 by `forest` (704 whole), 705 case accounts; no room unread; the fleets apart |
| `canvas_uses.py` | `.json` | rule 7's uses, by log | `mem.py room` with the canvas shown: A1 715, B1 1,874, C2 22, C5 218, D3 4, D5 5; canvas files named in commands at C2a-03, D3b, D5a-40, D5b, D6b |
| `orderings.py` | `.json` | the orderings by snap, and every key file's hash history | the scheme before B3, prior.md before B1's first theme, the D1 seal before the return, and the branch cuts before the projection all held; 82 D4 snaps after the projection (the room forms) |
| `moves.py` | `.json` | both history ledgers by stage and move; the move snaps against the diary's move lines | diary move lines equal move snaps by count from C2 to D6; 'sequencing' (C2) and 'stabilizing' (D3) are not among the eight |
| `probes_score.py` | `.json` | the recall probe, as filed and re-read | 283 of 300 answer files are in bold markdown, which probe.py does not parse; goal right 17 as filed, 298 re-read |
| `element_reach.py` | `.json` | prior.md section 3's element-reach half | 4,759 of 5,380 themes with a coordinating turn (88.46 per cent) reached by a standing element; 297 of 696 rooms in full |
| `unplaced.py` | `.json` | the unplaced at each tier | 151 second-order themes unplaced (407 concepts); T3-017 and T3-133 in no fourth-order theme; every fourth-order theme in a dimension |
| `manifest.py` | `.json` | `run_manifest.json`, whole | 19 entries with model, seed and decoding; the D3 re-check return has none |
| `counts_rule.py` | `.json` | the census twice, D4 section 4's four counts, the ledgers against the head, the handbacks' count phrases | 705 and 705; 476 + 0 + 229 + 0 = 705; tier history 1,026 against the head's 1,020; 361 count phrases to check |
| `clocks.py` | `.json` | the coder's time against the item's; datings in written order | equal in all 115,350 joined concepts; 237 of 598 case chronologies step back; 14 of 21 arrows name such a room |
| `claims.py` | `.json` | propositions and branches by kind, evidence, rival and validation | 9 propositions (pattern 7, both 2), each with a rival; 35 branches (33 groupings, 2 forms) |
| `diary_transcript.py` | `.json` | the diary against the transcript, one leg per stage by seed | 17 legs; 392 of 905 diary lines found word for word; the rest are tool-written lines, to be read |
| `fleet_figures.py` | `.json` | the fleet figures beside FLEET.md section 2 | the verdict fleet's readers differ in 163 of 705 rooms (0.2312) |

**Carried for this stage, and where each goes.**
- **prior.md section 3's measure, the element-reach half.** It is computed here, at E1a (`audit-E1/element_reach.py`). It will be reported in the audit section on composition (section 3). The other half, a validated adaptation or a theme listed as unresolved with its reason, is not computed, so local validation stays not established.
- **Defects 100 and 101** (the survival paragraph rests on work_remained; four timings the canvas contradicts) are reported open in the ledgers section, not rewritten.
- **PR-D6-10** stays an unvalidated proposal. It is checked against the D3a-55 ruling in the moves and provenance section. The script shows that all eleven proposals are 'unvalidated' on the base model 46384686…, the D3 freeze, and that `amendments-D6.jsonl` holds no line.
- **The D6 extra legs, D6a-09 to D6a-18**, are audited as part of the run. One of them, D6a-17, is in the diary draw. Their moves, snaps and outputs are read in the moves and provenance section.

**QE1-001, asked of J at this leg.** Stage E1's close-check counts each D4 snap that lists the projection as an error. There are 82 such snaps, which give 246 lines. They are the D4a-03 interview cut, the closes of D4a-04 to D4a-08, and the move snaps 238 to 313: the room forms, made after the projection at J's instruction. The branch cuts, moves 200 to 237, were all snapped before it. Rule 18 bars changing the snaps, and the snaps belong to the harness. So every E1 leg would fail its close-check on these lines until the check was changed or J ruled. My assumption, logged with the question: the check is changed to print these snaps as the audit's finding. The first done.sh of this leg failed on these 246 lines alone (`_closes/E1-E1a-20261027T172649Z.validate.txt`).

**QE1-001, answered** (J, 27 October 18:45 Berlin, through the PI): "Yes. I would not change the structure of the journey for bookkeeping." The handler amended `check_orderings`. A D4 snap now counts as a branch cut only where it changed `branches.jsonl` from the previous snap. A snap that lists the projection with `branches.jsonl` unchanged is printed as a finding, and the error stays for any snap that changed the branches after the projection. My assumption held as the answer states it, so nothing that rested on it changes. I checked the answer against the snaps by script: 82 D4 snaps list the projection, and none of them changed `branches.jsonl` from the previous snap. `validate.py E1` now gives 0 errors, 246 findings on those 82 snaps, and 1 warning for the stage's later outputs (`_analysis/e1a_validate_E1-2.txt`). The audit reports the 82 snaps, in the orderings section (E1b-02), as the finding they are: the room forms were made after the projection, by J's ruling, and they are not a recut of the branches.

**The audit sections I plan: eight, E1b-01 to E1b-08.** Each leg writes its section to its own file, `audit-E1/section-NN.md`. The reason: the close-check reads `audit-E1.md` whole as soon as it exists, and it requires the composition line and the methods paragraph, which can only be written last. `audit-E1.md` is assembled from the eight files at the check leg, E1d. That leg adds stage section 5, the methods paragraph and the `composition_status` line, all of which need the reconstruction's fidelity.
1. **E1b-01, the quotes and the clocks** (section 1): the 12 cited-quote defects and the 2,042 unresolved spans, read; the five spot-checks by hand; the 389 missing case-account strings, read, and the 548 against 389; links; the store's figures in three columns; the clocks, with relations.jsonl by hand.
2. **E1b-02, the orderings, the counts, coverage and the canvas** (section 1): each ordering held or broken; the 361 count phrases of the handbacks against their files; coverage by stage; every canvas use named, declared or not, with the places the canvas may have shaped unseen; QE1-001's answer.
3. **E1b-03, the moves and provenance** (section 1): the moves by stage and by the eight, including 'sequencing' and 'stabilizing'; the recuts after C5; the D6 proposals against their evidence, with PR-D6-10 against D3a-55; D6a-09 to D6a-18; the manifest; the figures restated with FLEET.md section 2's definitions.
4. **E1b-04, claims against their evidence** (section 1): `claims-E1.md`, every proposition and branch by kind and validation; prior.md section 3's declaration against what each level rests on; the switch records of `literature-C3.md`.
5. **E1b-05, the diary, the probes and the unplaced** (section 1): the 17 drawn legs read against their transcripts; `probes-E1.md`, per stage and per question, as filed and re-read, with notes apart from defects and n/a apart from recall; the 151 unplaced themes, T3-017 and T3-133, read.
6. **E1b-06, the ledgers, the stories and what a reader was given** (section 2): findings by status, warrant and refuted_by; every ledger's lines; new kinds per hundred themes; the stories and the account's passes; the five things a reader was given; the departures with their costs; the defects, the material's apart from the instrument's, 100 and 101 open; the forks (none arrived); rule 9.
7. **E1b-07, composition and expectations** (section 3): the diagnostics recomputed against prior.md section 3, with the element reach; local validation and unresolved evidence apart; clusters and distinct global changes; prior.md section 2's expectations; `expectations-E1.md` with the field's entries; the onset contrast.
8. **E1b-08, what bore the load and what the study cannot say** (sections 6 and 7): stage by stage, the replay of `tools/chunk_compare.py`, the data-structure view at C2's last snap against `data_structure-C5.md`, the tiers' work; the absences, the ungrounded, the coder conflicts, the standing departures; the critique shelf; the one thing to say plainly.

**Licences exercised at E1a.**
- probe.py's `--score` was not rerun. It writes into `_probe/`, which belongs to the harness, and it scores the open distinctions against the question files as they stand now. I read the filed scores and re-read the answers by its rules against the expected values the harness stored at each close.
- The scripts read `package/<sub>/case.md` and the store's files directly, as stage A1's checks did under the departure in `departures.jsonl` line 1. They print only counts and the strings the stage asks to be read.
- The coordinating rule is A1's own code (`_analysis/a1_ends.py`), imported, not rewritten. It reproduces `organizing_end-A1.jsonl` in all 705 rooms.

**Slips at E1a.**
- A survey command piped a helper through `cut -c` and was refused; it was re-run without it. A shell loop was refused too; I used the peek script instead.
- Two Edits to `moves.py` went in one turn. They touched separate lines and both applied.
- Five scripts needed a second run, and the first output of each is kept: `quotes_resolve` (twice: the pairing of quotes, and a citation taken from the next quote), `store_figures` (distinct ids counted as lines), `canvas_uses` ('placements' matched theme placements), `moves` (twice: 'move N' in lower case only, and the eighth move bucketed as dropping) and `probes_score` (one leading mark stripped).

## E1b-01: the quotes and the clocks

**The close-check report of E1a** (`_closes/E1-E1a-20261027T174924Z.validate.txt`): 0 errors, 1 warning (the stage's later outputs not yet written), and 246 findings on the 82 D4 snaps after the projection (QE1-001). **QE1-001** was read again at this leg's start, as the leg message asked. The answer had been reconciled at E1a, and nothing else rested on my assumption, so no work changed.

**What this leg did.** It wrote `audit-E1/section-01.md`, part 1 of the audit's section 1, on four items: the quotes and ids against the logs, the quotes against the raw record, the store's figures, and the clocks. It wrote seven scripts, each with its rule in its docstring, declared before the run, and its output beside it:
- `unresolved_read.py`: what the 2,042 spans resolved to nothing are;
- `unresolved_hand.py`: where the 84 left over first appear in the transcripts;
- `quote_sources_check.py`: quotes of a named source, beside the source;
- `labels_read.py`: the 3,641 spans that resolve to a label;
- `case_missing_read.py`: the handler's 389 missing case-account strings;
- `relations_clock.py`: two rooms' records of one encounter;
- `links_views.py`: `links.py`'s resolver over the views.

The readings by hand are logged one by one in the diary.

**What it found.**
- **Cited quotes.** 3,218 of 3,230 cited concept quotes resolve to the concept cited. Of the 12 that do not, 2 are faults of form and 10 are faults of the script.
- **Invented quotes.** I found no invented quote in my files.
- **Defects of mine.** Two D6 quotes give the coder's wording as members' words, carried from the case accounts. Two small misquotes of the instrument's own text. Three examples of my own wording in quotation marks.
- **The handler's file.** It gives code_quote_found_share 1.0 and case_quote_found_share 0.6573. Its 389 listed strings are mostly participant words missed on punctuation and markup, the coder's own labels and phrases, and translations. 33 come from uncoded items, beyond my reach.
- **The store's figures.** All 16 agree with README-store.md and with A1.
- **Ids.** No id of the model, the scheme or the store fails to resolve in the head, the questions or the views.
- **The clocks.** The coder's time equals the item's in all 115,350 joined concepts. The store's builder is absent, so this may hold by construction. No pair of two rooms' records dates one encounter at two times.
- **Defects ledger.** Eight lines were appended to `defects.jsonl`: 5 the instrument's, 1 provenance, 2 the material's.

**Licences exercised at E1b-01.**
- I read `_transcripts/`, open at this stage, by script for where a span first appears.
- The handler's `quote-check-E1.json` is read from the folder root, where it arrived.
- I count the readers' room models, which the E1a rule did not leave out, as outputs. Their quotes are reported apart from mine.

**Slips at E1b-01.**
- The first `unresolved_read.py` run kept the earlier class and so moved nothing. Its output is kept as `.superseded-1`.
- Two `unresolved_hand.py` runs with `grep` were too slow and were stopped. Their empty outputs are kept as `.superseded-1` and `-2`.
- A survey command piped `tail` into `cut` and was refused; it was re-run without the cut.
- Two diary lines needed correcting lines after them: the count of the instrument's defects lines (5, not 6), and the r/argentina and r/uruguay pair, which I first read as one encounter.

## E1b-02: the orderings, the counts, coverage and the canvas

**The close-check report of E1b-01** (`_closes/E1-E1b-01-20261027T191229Z.validate.txt`): 0 errors, 1 warning (the stage's later outputs not yet written).

**What this leg did.** It wrote `audit-E1/section-02.md`, part 2 of the audit's section 1. It wrote four scripts, each with its rule in its docstring, declared before the run, and its output beside it:
- `prior_sections.py`: `prior.md` rebuilt from the transcripts' writes, matched to the snaps and compared section by section;
- `snap_order.py`: the move snaps in number order, the D4 branch cuts against the projection, and the D6 proposals;
- `counts_phrases.py`: the 361 handback count phrases sorted, a seeded sample of 36, and the head's ledgers;
- `counts_sample_check.py`: the 36 recomputed where a governing file can be counted.

It read E1a's `orderings`, `counts_rule`, `coverage` and `canvas_uses` outputs, and it appended 2 lines to `defects.jsonl`.

**What it found.**
- **Orderings.** All seven orderings the stage names held. `prior.md` sections 1 to 6 are byte for byte what was snapped before B1's first theme. The model moved after C5's hash only by D3's declared amendments. The D4 branch cuts all came before the projection, and the 82 snaps after it are the room forms by J's ruling (QE1-001). One move snap is a declared duplicate.
- **Counts.**
  - The census is 705 twice, with 0 drops, and the four D4 counts sum to 705.
  - The head's seven ledger figures agree.
  - Of the 36 sampled handback counts: 27 recompute and agree, 4 agree with a stated parameter or list, and 3 rest on a judgment by hand.
  - 2 sampled counts disagree: handback-B1's 107 and handback-C5-p14's 31. 293 counts were not checked.
- **Coverage.** All 705 rooms were read by `room`, `forest` and their case account. 704 forests were read whole; r/COSI's skipped its ten header lines.
- **The canvas.** No undeclared use was found. The canvas was on the page in 2,118 room reads at B1, C2, C5 and D3, and whether it shaped anything there is self-reported.

**Licences exercised at E1b-02.**
- I checked the handback counts by a seeded sample of 36 and not all 329. The sample and the 293 unchecked counts are both reported.
- I rebuilt `prior.md` from the transcripts' tool calls, which are open at this stage, to tell its sections apart where a hash cannot.

**Slips at E1b-02.**
- `counts_phrases.py`'s first run took any comma into the number and set aside nothing.
- `counts_sample_check.py` had three faults, fixed over two reruns (the first two together):
  - it read a key the B3 defects lack;
  - it read the analyst's D3 rulings in place of the re-check readers' verdicts;
  - it grouped those verdicts by the readers' own spelling of the room.
- The first outputs are kept as `.superseded-1` and `-2`.

## E1b-03: the moves, provenance, the manifest and the figures

**The close-check report of E1b-02** (`_closes/E1-E1b-02-20261027T193841Z.validate.txt`): 0 errors, 1 warning (the stage's later outputs not yet written).

**What this leg did.** It wrote `audit-E1/section-03.md`, part 3 of the audit's section 1, and one script, `provenance_D6.py`, with its rule in its docstring and its output beside it. The script covers the D6 proposals' evidence and diary lines, the data files across D6a-09 to D6a-18, and the tier history by stage and tier. The leg read E1a's `moves`, `manifest` and `fleet_figures` outputs and the files they name, and appended 2 lines to `defects.jsonl`.

**What it found.**
- **The moves.** Every move after C5 is either a rule 11 amendment with its D3 cause or a held proposal, and no coding tier was recut after C5. Move snaps and diary move lines agree from C2 to D6. 18 C2 model-history lines are named "sequencing", which is not one of the eight and was never corrected. This is a defect.
- **The D6 proposals.** All eleven are unvalidated on the D3 freeze, their 254 concept ids resolve, and each has its diary line. PR-D6-10 names the D3a-55 ruling it would widen, and it changes nothing.
- **The extra legs.** No data file moved across D6a-09 to D6a-18 except `departures.jsonl` line 21. That line is the dated amendment of the branch-naming rule, in use before it was written; it goes to the departures section.
- **The manifest.** It gives complete provenance for every fleet figure but the D3 re-check, whose runs name a model with no seed or decoding. This is a defect.
- **The figures.** They are restated with FLEET.md section 2's definitions and licence. None is called reliability.

**Licences exercised at E1b-03.**
- I read the diary whole by script, for the proposals' lines and C1's move lines.
- I counted C1's 185 reassignment lines by their first word, not one by one.

**Slips at E1b-03.**
- Two Edits to `section-03.md` went in one turn. They touched separate lines and both applied.
- A first draft of the section said the tier history used six of the eight moves; it uses seven.
- The same draft said, before I had read them, that C1's 185 extra move lines were re-placements under the amended gates. They are reassignments, read by their first word. Both were corrected before the checks.

## E1b-04: claims against their evidence

**The close-check report of E1b-03** (`_closes/E1-E1b-03-20261027T195759Z.validate.txt`): 0 errors, 1 warning (the stage's later outputs not yet written).

**What this leg did.** It wrote `claims-E1.md`, the table the stage asks for and the methods paragraph cites, and `audit-E1/section-04.md`, part 4 of the audit's section 1. It wrote one script, `claims_returns.py`: the return's accepted lines by op on each arrow, and whether each arrow's order test is read against a bracket, the onset contrast and held size. It read E1a's `claims.json`, `prior.md` sections 3 and 4, and the switch records of `literature-C3.md`. It resolved the arrows' 57 support quotes against the store, and appended 1 line to `defects.jsonl`.

**What it found.**
- **No claim is validated with the other kind's evidence.**
- **The pattern propositions** rest on counts with denominators and beaten nulls.
- **N07** declares both, and its pattern half is not established. It says so.
- **The branches** rest on both kinds, as `prior.md` section 3 asks.
- **The one gap against the declaration:** the population pattern was never tested at held size, and only A20's order is read inside a bracket.
- **The two switch records** agree with the findings ledger.

**Licences exercised at E1b-04.**
- I counted the return's verdicts per arrow from the last ruling of each line, across the first return and the re-check together.
- I named N07 half-validated, not a defect, because it declares itself theorised and thin.

**Slips at E1b-04.**
- The first draft of `claims-E1.md` said "18 of the 20 counted arrows" where A21 has counts but no null test. It now says the 20 arrows the propositions rest on. Corrected before the checks.

## E1b-05: the diary, the probes and the unplaced

**The close-check report of E1b-04** (`_closes/E1-E1b-04-20261027T201650Z.validate.txt`): 0 errors, 1 warning (the stage's later outputs not yet written).

**What this leg did.** It wrote `probes-E1.md` and `audit-E1/section-05.md`, part 5 of the audit's section 1. It wrote three scripts, each with its rule in its docstring and its output beside it:
- `diary_tool_lines.py`: the diary lines E1a could not find word for word, against their leg's tool calls;
- `probes_notes.py`: every wrong probe answer, sorted into a note or a defect;
- `unplaced_kinds.py`: the 151 unplaced themes, by kind.

It appended 2 lines to `defects.jsonl`.

**What it found.**
- **The diary.** All 905 diary lines of the 17 drawn legs are borne out by the transcript: 392 word for word, 185 by a nearby tool call, 282 as rows of the files a B1 script read, 19 in `b1_place.py` commands, and 27 written by one C5 script.
- **The probes.** The method question was right in 298 of 300 re-read answers. 269 wrong answers are notes the record answered. 18 are defects no record answered: the rooms of 14 legs, and the changes of 4.
- **The unplaced.** 151 themes: 42 April Fools play, 72 talk about the event, 18 lost posts and 19 naming an act. 10 of the 19 should have been placed. T3-017 is outside the scope by design. T3-133 is one rare host act.

**Licences exercised at E1b-05.**
- I did not rerun `probe.py --score`: it writes into the harness's `_probe/`.
- I added a second test for the rooms question beside the declared one, once the first run showed the harness's expected rooms repeat across legs. Both counts are kept.
- I counted the unplaced kinds by a keyword rule, then read them.

**Slips at E1b-05.**
- A first draft of `probes-E1.md` said every missed answer stayed in the read logs and the ledgers, which I had not checked. Corrected before the checks.
- A B1 check by script first used the wrong separator. It found none of the 301 rows, against 282 by the regular test, and the regular test stands.

## E1b-06: the ledgers, the stories, what a reader was given

**The close-check report of E1b-05** (`_closes/E1-E1b-05-20261027T203818Z.validate.txt`): 0 errors, 1 warning (the stage's later outputs not yet written).

**What this leg did.** It wrote `audit-E1/section-06.md`, the audit's section 2, with one script, `ledgers_stories.py`, whose rule is in its docstring and whose output is beside it. It appended 3 lines to `defects.jsonl`.

**What it found.**
- **Findings.** 45 lines over 27 findings. Six changed from standing to bounded. 8 have no statable `refuted_by`.
- **Ledgers.** The append-only ledgers never shrink. Nine files do: six state files by design, two pilot files at B2, and `fractal-D6.jsonl` by a declared move.
- **Kinds.** 2.51 new kinds per hundred themes.
- **The stories.** Five passes, and 67 distinct rooms read against a story. The one room that does not compose at the first return is among the 638 no story was read against. The account's loop ran 15 passes.
- **What a reader was given.** Two of the five things held. The account is 3,326 words, 3 of its quotes are undated, and it lists the residue rather than explaining it.
- **The departures.** 18 of 21 state no cost, and 2 were acted on before they were written.
- **Forks and rule 9.** There are no forks to compare. Rule 9's handed-over findings are P21, P22 and A21, from the field, replicated at D3.

**Licences exercised at E1b-06.**
- I sorted the defects by a keyword rule, and the E1 lines by my own labels.
- I read the residue and the departures' costs from their files' own words.

**Slips at E1b-06.** None noticed.

## E1b-07: composition and expectations

**The close-check report of E1b-06** (`_closes/E1-E1b-06-20261027T205719Z.validate.txt`): 0 errors, 1 warning (the stage's later outputs not yet written).

**What this leg did.** It wrote `expectations-E1.md` and `audit-E1/section-07.md`, the audit's section 3. It wrote one script, `expectations.py`. Its first run ordered rooms by name and read only the readers' verdicts, and is kept as `.superseded-1`.

**What it found.**
- **Verdicts.** The ruled fixed-global verdicts are 201, 489, 14 and 1 at the first return, and 630, 56, 19 and 0 at the re-check.
- **Particulars and shared changes.** 2,749 particular lines in 545 rooms. 223 distinct shared changes, whose curve in A1's seeded order flattens over the last third (184, 211, 223).
- **The expectations.** The in-sample replication score is 0.924, with C01's 81 rooms the largest failure.
- **The field's entries.** They were taken up in 112 to 223 rooms and never contradicted, against a mean of 383 for the other elements.
- **The onset contrast.** Untested: the late side holds 0 to 15 rooms per arrow.
- **Composition.** The population level is supported in the return's terms. Below it the population compiles. The leaf is unresolved until the reconstruction.

**Licences exercised at E1b-07.**
- I counted an arrow as "taken up" when any accepted line changes or instantiates it, and as "absent" only when no line takes it up.
- I put off the `composition_status` line to `audit-E1.md`, after the reconstruction's check.

**Slips at E1b-07.**
- Two Edits to `expectations.py` went in one turn. They touched separate lines and both applied.
- Two glosses in `expectations-E1.md` went beyond what I had checked, and were cut before the checks.
- One watch-word ("stands as") was rewritten.

## E1b-08: what bore the load, and what the study cannot say

**The close-check report of E1b-07** (`_closes/E1-E1b-07-20261027T211544Z.validate.txt`): 0 errors, 1 warning (the stage's later outputs not yet written).

**What this leg did.** It wrote `audit-E1/section-08.md`, the audit's sections 6 and 7. It wrote two scripts, each with its rule in its docstring and its output beside it:
- `load_limits.py`: the outputs named downstream by stage, the chunk-comparison receipt, the data-structure view's hashes, the dimensions' work and the limits' counts;
- `shelf_terms.py`: the critique files' passages, by objection and page.

It read Jowsey et al. (2025) and the call for papers whole, and appended 1 line to `defects.jsonl`.

**What it found.**
- **The stages.** Every stage was load-bearing for something downstream. Nine files look read by nothing (not sure).
- **The chunk comparison.** It matches its receipt and can be rerun.
- **The data-structure view.** It moved at C5 and has been unchanged since.
- **The dimensions.** They do no work in the account, the arrows or the branches.
- **The critique shelf.** The run answers the invented-quotes objection in large part, and the opacity objection for its record of decisions. It does not answer the objections on offloading, reflexivity, more output, or harm.
- **What the study produced.** A model with a typology. The strongest size argument is D4's volume verdict. A sample of 30 uncoded rooms with 4 or more not composing would overturn the population claim.

**Licences exercised at E1b-08.**
- I searched O'Sullivan and Ravasi (2026) and Schildt (2026) by the objections' terms with their pages, rather than reading them whole.
- I named files read by nothing from their names and the commands, not from every tool's inputs.

**Slips at E1b-08.**
- A diary read piped through `cut` was refused by the guard; it was re-run whole.
- My first read of the stage file began at section 6; the rest was read before any write.

## E1c: the reconstruction build

**The close-check report of E1b-08** (`_closes/` for E1b-08): 0 errors, 1 warning (the stage's later outputs not yet written).

**The sample, named before any room is opened.** `audit-E1/reconstruction_draw.py` drew it from the ledgers alone and wrote it to `reconstruction-sample-E1.jsonl`. Its rule is in its docstring, declared before the run:
- **Verdict:** the first return's ruled fixed-global verdict.
- **Branch:** the room's most specific branch, or none.
- **Strata:** does-not-compose 1, cannot-tell 2, composes 8, composes-with-residue 19.
- **Draw:** a seeded shuffle (`out/seed.txt`) that spreads the rooms over branches, with at most 10 rooms in no branch.

The thirty rooms (room, branch, verdict):

| verdict | rooms |
|---|---|
| does-not-compose | picturegame (F25) |
| cannot-tell | sakartvelo (none); quq (none) |
| composes | hunterxhunter (F03); ethoslab (F01); python (F26); kirby (F18); ucf (F15); penguins (F34); ReBoot (none); sonicthehedgehog (none) |
| composes-with-residue | mamamoo (F35); superman (F33); physical_removal (F23); thenetherlands (F02); tagpro (F29); gameboy (none); necrodancer (F28); simonfraser (F30); Goodboye (none); Madeon (none); dwarffortress (F16); TeamYellowPlace (none); hyperlightdrifter (F24); puzzleanddragons (F07); seolhyun (F10); pansexual (none); PinkUnion (none); mls (F06); slovenia (F08) |

They spread over 20 branches, and 10 are in no branch.

## E1d: the check

**The close-check report of E1c** (`_closes/E1-E1c-20261027T215904Z.validate.txt`): 0 errors, 1 warning (the stage's later outputs not yet written).

**The dispatch, and the PI's message** (27 October, 22:51Z, for J). The readers ran from 22:29Z to 22:40Z. fleet.py found 0 valid returns and 30 rooms exhausted, because each reader ended with a marker the packet asked for and `RETURN-E1.md` did not name. The PI's instruction: validate the returns from the newest raw file per room, drop only a final marker line and record it, log the mismatch as a defect of the instrument, and do not re-dispatch.

**What this leg did.** It wrote `reconstruction-E1.jsonl`, the audit's sections 4 and 5, the composition result and the methods paragraph (`audit-E1/section-09.md` to `section-12.md`), and assembled `audit-E1.md`. It wrote eight scripts, each with its rule in its docstring and its output beside it:
- `reconstruction_validate.py`: the returns validated, and fidelity by verdict and by branch;
- `reconstruction_causes.py`: the lines read for the causes of a low score, tallied from my reading in `reconstruction_causes.tsv`;
- `versioned_judgments.py`: the four judgments side by side, and the seeded sample of disagreements;
- `reconstruction_tables.py`: the tables of sections 4 and 5;
- `assemble.py` and `supersede_parts.py`: the audit joined from its parts, three of them as superseding copies;
- `defects_E1d.py` and `defects_E1d-2.py`: 3 lines appended to `defects.jsonl` (lines 121 to 123).

**What it found.**
- **The returns.** All 30 are complete. Each ends with one marker line, dropped and recorded. 25 are valid under the rule as first written; the other 5 wrote the room as "r/" with its name, which an amendment made after the first run reads as the room.
- **Fidelity.** 0.871 over 30 rooms (0.637 to 0.975), 1,788 claims, 15 unresolved, 0 contradicted. By the first return's verdict: composes 0.911, composes with residue 0.875, cannot tell 0.770, does not compose 0.680.
- **The causes.** Of 200 lines read, 167 are particulars the skeleton does not carry (the room's other business, its counterparts by name, its clock, its layers), 13 are missing evidence, 12 are readers' errors and 7 point at the shared account (two facts in two rooms). No low score is a failure of the global model.
- **The judgments side by side.** The adapted-local status is the same in all 705 rooms, and 33 of 35 branches are unresolved. 25 of the 30 rooms disagree, 23 of them because the verdict changed at the re-check. In the seeded five, the verdict moved with the model, not with new evidence about the room.
- **Composition.** `composition_status: unresolved`: supported at the population level; compiled at the forms; at the leaf the shared account holds, but local adequacy is not established.

**Licences exercised at E1d.**
- I amended the validation rule after its first run, so that a room written as "r/" with its name reads as the room, and I report both counts.
- I wrote down how two causes would be read after the first page of lines, before any cause was written.
- I read the coders' claims as the packets give them and did not test them against the raw record.
- I joined three earlier parts as superseding copies with listed replacements, rather than editing them.
- I chose `unresolved` for the composition line, reading `prior.md` section 3's two grounds as unmet.

**Slips at E1d.**
- Two figures in my diary lines were typed before the check (12 lines of picturegame, not 11; 23 rooms changed at the re-check, not 24). Both were corrected in the diary.
- A validate run piped through `cut` was refused by the guard; it was re-run whole.
- The first assembly failed the close-check on wording in three earlier parts.
