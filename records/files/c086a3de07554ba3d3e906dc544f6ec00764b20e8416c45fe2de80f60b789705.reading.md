# Audit of the run (stage E1)

Assembled at E1d, 28 October 2026, by `audit-E1/assemble.py` from the parts in `audit-E1/`, joined whole and in this order. Every figure in it comes from a script in `audit-E1/`, with its rule in its docstring and its output beside it, or from a reading by hand that the diary logs. Nothing in it comes from anyone's account of itself, mine included. Where a figure computed here differs from an earlier file, the part says which is wrong.

| part | stage E1 section | written at |
|---|---|---|
| section 1, parts 1 to 5 | 1: scripts over the record | E1b-01 to E1b-05 |
| section 2 | 2: the ledgers, the stories, what a reader was given | E1b-06 |
| section 3 | 3: composition at each level, expectations and contrasts | E1b-07 |
| section 4 | 4: the reconstruction sample | E1d |
| section 5 | 5: versioned judgments, side by side | E1d |
| the composition result | 3 and the closing instruction | E1d |
| sections 6 and 7 | 6: which stage was load-bearing; 7: what the study cannot say | E1b-08 |
| the methods paragraph | 8 | E1d |

The parts written before E1d say that the reconstruction had not yet run. Sections 4 and 5 and the composition result report it. Where section 3 and sections 6 and 7 say the leaf waits on the reconstruction, the composition result gives its outcome.

# Audit, section 1, part 1: the quotes and the clocks (E1b-01)

Written at E1b-01, 27 October 2026. This part covers four items of stage E1 section 1: the logs against the claims (every quote and every id), the quotes against the raw record, the store's figures recomputed, and the clocks. Every figure below comes from a script in `audit-E1/`, with its output beside it under the same stem, or from a reading by hand that the diary logs. A stranger reruns a script with `python3 out/audit-E1/<script>.py > out/audit-E1/<output>`. The scripts written at this leg are `unresolved_read.py`, `unresolved_hand.py`, `quote_sources_check.py`, `labels_read.py`, `case_missing_read.py`, `relations_clock.py` and `links_views.py`. Each states its rule in its docstring, written before it ran. Nothing here comes from any account of the run, my own included; where an earlier file differs, this part says which is wrong.

## 1. Logs against claims

### Every quote in every output

`quotes_resolve.py` (E1a) scanned 5,953 files I wrote: every `.md` file under `out/` and the string fields of my ledgers. It left out the harness's, the fleets', the principal investigator's and the generated files, which its docstring names. 5,166 of the files hold a quote. A quote is a span between paired double quotes on one line. The script resolved each span in a fixed order: the participant's words of a concept, then a label or note, then the coder's case account, then the instrument's texts, then the instructions, then nothing.

| quotes | spans | resolve to |
|---|---|---|
| cited to a concept (`sub/cNNNN`) | 3,230 | 3,218 to the concept cited (99.63 per cent); 12 do not |
| cited to an item (`` `itemid` ``) | 405 | 361 to a concept's words, 34 to the case account alone, 2 to a label, 8 to nothing |
| uncited, five words or more, in `.md` files | 76,848 | 69,079 to a concept's words, 3,639 to a label or note, 1,955 to the instrument's texts, 73 to the instructions, 68 to a case account, 2,034 to nothing |

**The 12 cited quotes that do not resolve to their concept**, read by hand in their files against `cite.py`. Two are faults of form. Ten are faults of the script, not of the quote.

| file, line | cited | what it is |
|---|---|---|
| `account-p1.md` 23 | suomi/c0098 | **Fault.** My English translation of the Finnish post is set in quotation marks beside the original, which resolves, with no word saying it is a translation. |
| `notes-A1.md` 700 | predators/c0047 | **Fault by the stage's rule.** The quote is the concept's label, and the sentence says it is a label. Nothing is passed off as a member's words. |
| `forms/F06-account.md` 100, `forms/F10-account.md` 164, `forms/F23-account.md` 125, `notes-C5.md` 564 | rust/c0144, buffalobills/c0127, greyblob/c0037, pokemon/c0506 | The quote is a coder's or reader's return line, or an element's statement, named as such; the citation belongs to the next sentence. |
| `serial-C5/finding-1-unit.md` 71 to 74 | fireemblem/c0412, utahjazz/c0030, lakers/c0155 | The quote is the model's wording, in a table beside a column of evidence ids. |
| `forms/F16-account.md` 161 | pcmasterrace/c0596 | "focus on the plan" is in pcmasterrace/c0593, cited one clause before for the same member's post. |
| `serial-C5/finding-2-reason-test.md` 82 | polyamory/c0002 | The store writes the slash as `/r\/place`; the quote is word for word. |

**The 2,042 spans that resolved to nothing** (2,034 uncited and 8 cited to an item). `unresolved_read.py` sorts them. 983 are field values of JSON records printed inside `.md` files (the structure files hold 927 of them), not quotes. 975 are found whole once the store's escapes, asterisks and backticks are set aside: 131 in a concept's words, 31 in the forest, 2 in a case account, 320 in the readers' and coders' returns, 5 in the operator's texts and 486 in the run's own other files. The 8 cited to an item are the field's quotes, found whole in `out/field/`. That leaves 84, 52 near a source and 32 near none. `unresolved_hand.py` finds where each first appears in the transcripts, and I read each in its line.

- **63 in my files.**
  - 16 are the operator's or the harness's words. Each first appears in a message to me: J's rulings in the head, the principal investigator's leg messages, a ruling that came as an attachment, and the brief's phrase "N threads out of scope".
  - 8 are texts I first saw in a tool's output: shelf pages, and counts quoted from an earlier file.
  - 8 are literature quotes that `quote_sources_check.py` puts beside the shelf. The shelf files are two-column extractions, so the words come interleaved with the other column and broken at line ends. Read through, each quote is the paper's words. One example: Felin and Zenger's "a set of contrarian beliefs" is "a set of con-trarian beliefs" across a line break.
  - 24 are my own earlier wordings, quoted as such: statements under test, an earlier version of a proposition, a sentence later corrected.
  - 1 is a translation I declared as mine (`literature-C3.md` line 235, "My translation").
  - 2 are small misquotes of the instrument. `notes-C1.md` line 144 has "apply" where the stage has "applying". Line 453 has "a rivalry" where the scheme has "A dispute or rivalry".
  - 3 are examples of my own in quotation marks, which a reader could take for members' words: "help us at 200, 300" (`_adjudication-B4/boundaries.md` 59), "those were not our people" (`confusions.md` 47) and "defending the script as fun" (`coordinating-rule-A1.md` 32). No concept holds them.
  - 1 cannot be checked. J's instruction on reading is quoted in `notes-B2.md` line 5, but no transcript holds its words before my own Write at B2a-r1. The message that carried it is outside my reach, so the wording rests on my record alone.
- **21 in the readers' room models** (`rooms/<sub>/model-D*.md`, written by the D2 and D3 readers, not by me). 11 quote a concept with small changes: a word dropped, a spelling corrected, a contraction opened. 3 paraphrase inside quotation marks: r/armenia's line on the Dutch, r/zootopia's "patch of artwork" for "patch of space", and r/straya's "breaking the truce is Un-Australian". 7 are in no concept of the room. They may come from uncoded items, which the forest drops, or they may not; I cannot tell.

**The 3,641 spans that resolve to a label or note** (3,639 uncited and 2 cited to an item). The stage counts a quote that resolves to a label as a defect. `labels_read.py` sorts them. 3,560 are the `second_order` field of the JSON exemplar records in the structure files, not quotes. Of the 81 in prose, I read a seeded 25.
- In my files, 16 name a label as a label: a theme by its name, or a room note's "struck by" line. 1 is a packet's line format, and 1 is a defect.
- In the readers' room models, 4 are faithful quotes whose concept text holds link or emphasis markup. 2 paraphrase inside quotation marks (r/asexuality, r/smite), and 1 cannot be told (r/norge).

The 2 cited to an item are both defects of mine, made at D6a-17 and D6a-18. In `dutch-telling-D6/greece.md` line 36, "the heart was placed cooperatively later" is the coder's English for a Greek post (greece/c0126, item `dfrvs5t`), and I gave it as a member's words with no original. In `form-telling-D6-r2/room-E-paladins.md` line 26, "April Fools' shenanigans" is the coder's wording; the post says "April Fools' Day, so expect shenanigans" (paladins/c0001). I carried both from the case account. My D6 quote check tested quotes against the case account, so it passed them.

**Five quotes drawn by seed** (`cd472a6087a223d4`, from the cited quotes that resolve), checked by hand with `cite.py --room --code`. All five hold word for word, with the room, the concept and the hour the accounts give:
- Moondye7/c0066 (`forms/F19-account.md` 17);
- lebanon/c0105 (`forms/F35-account.md` 60);
- fivenightsatfreddys/c0074 (`forms/F07-account.md` 160, "at h+7"; the store has 7.15);
- OnePiece/c0228 (`forms/F27-account.md` 9, "hour 51.18"; the store has 51.18);
- Rainbow6/c0589 (`forms/F20-account.md` 162, "at the close"; the store has 73.29).

### Every id in the head, the questions and the views

`links.py` and `validate.py --links` both exit 0, and all ids resolve (`links_check.txt`). But `links.py` reads three files only: `_head.md` and the two question files. It does not read the views. `links_views.py` applies its own resolver, imported, to the 35 text files of `out/_views/`. They hold 537,153 tokens of an id's shape, and 487 do not resolve. I read all 487:
- 413 are in `data-structure.tsv`, and all are members' words in its material column: 363 subreddit names as typed (210 distinct, typos among them), and 50 tokens such as "the D2 logo" and the names of a game console and of a gun, each a capital letter and two digits.
- 40 are the proposition ids N01 to N09 in `figure-model.md`. `propositions.jsonl` holds them, but `links.py` does not load it.
- 32 are stage names written bare in the generated views (D2, D3, D4 and D6).
- 1 is a logo name in a reader's line, a capital letter and two digits.
- 1 comes from one store pointer that names two rooms in one string.

No id of the model, the scheme or the store fails to resolve.

## 2. The quotes against the raw record

`quote-check-E1.json` was computed by the handler outside my session, over 80 rooms drawn with seed 13. It is the one place where the run touches the raw record. The store and `cite.py` serve only the coded record, and the methods paragraph says so. The file gives two shares:

- **code_quote_found_share: 1.0** (100 per cent). Of 14,587 coded quotes, 13,374 are at their offsets in the item and 1,213 are elsewhere in it; 0 are absent and 0 items are missing.
- **case_quote_found_share: 0.6573** (65.73 per cent). Of 1,599 quoted strings of 25 characters or more in the case accounts, 1,051 are found in the room's corpus.

**The 548 against the 389.** The file lists 389 missing strings, against 548 by its own count (1,599 less 1,051). It lists at most ten a room. In the 13 rooms where it lists fewer than it counts, 289 are missing and 130 are listed; 289 less 130 is 159, and 548 less 159 is 389.

**What the 389 are** (`case_missing_read.py`, then a reading by hand):

| kind | strings | what it is |
|---|---|---|
| in the room's coded passages | 242 | Participant words. The raw check missed them because the coder put punctuation inside the closing quote, or because the item holds link markup or other quote marks. |
| the coder's own labels | 85 | Theme or concept labels, quoted in the case account as labels. |
| near quotes | 10 | Participant words with link markup removed or inner quote marks changed. |
| thread titles | 7 | Titles of the room's threads. |
| another room's concept | 1 | A quote from outside the room's corpus: the r/PokemonSage account quotes a post that r/TheFarLeftSide's record holds. |
| the coder's translations | 5 | English in quotation marks beside the Albanian originals, which are quoted and cited (r/albania). |
| the coder's own phrases | 6 | A counter-reading's wording in quotation marks ("negotiated rather than destructive", "failure caused the strategy change"). |
| participant words from uncoded items, cited by item id | 33 | Outside my reach. The forest drops uncoded items, so I cannot check these against the raw record. Five are titles of threads the store does not hold. |

So, of the strings I could check, none is an invention. The missing share is mostly a matter of punctuation and markup, of the coder's own labels and phrases, and of translations. The five translations among the 389 are set beside their originals. The r/greece translation found in part 1, outside this sample, has none. 33 strings remain unchecked.

## 3. The store's figures recomputed

`store_figures.py` (E1a) sets `README-store.md`, stage A1's recomputation and the store as it stands in three columns. All 16 figures agree, so there is no defect. A dash in the table means the source gives no figure.

| figure | README-store.md | A1 | now |
|---|---|---|---|
| rooms | 705 | 705 | 705 |
| concepts | 115,388 | 115,388 | 115,388 |
| retracted, dropped | 175 | 175 | 175 |
| second-order themes | 7,844 | 7,844 | 7,844 |
| unjoined concepts | 38 | 38 | 38 |
| items in the store | 158,227 | 158,227 | 158,227 |
| threads in the store | 42,906 | 42,906 | 42,906 |
| pointers | 20,110 | 20,110 | 20,110 |
| briefs | 705 | 705 | 705 |
| transitions | 62,838 | - | 62,838 |
| forest: threads given | - | 42,906 | 42,906 |
| forest: items | - | 531,851 | 531,851 |
| forest: coded | - | 109,807 | 109,807 |
| forest: bridge | - | 28,350 | 28,350 |
| forest: removed | - | 617 | 617 |
| forest: dropped | - | 393,077 | 393,077 |

The 158,227 item lines hold 137,732 distinct room and item ids. 21,011 lines are in the state `collapsed`, which `README-store.md` does not name; stage A1 recorded this as a defect.

## 4. The clocks

**The coder's time against the item's** (`clocks.py`, E1a). In all 115,350 concepts whose item the store holds, the concept's `created_utc` equals the item's. Every concept's `hour` matches its own `created_utc`. The denominator is 115,350 of 115,388 concepts; the 38 others are the unjoined concepts. One limit: the store's builder, `tools/build_store.py`, is not in the folder. So I cannot tell whether the coder wrote the concept's time or the build copied it from the item. If the build copied it, the agreement holds by construction and says nothing about the coder.

**The second check, against `relations.jsonl`** (`relations_clock.py`; `tools/relations.py` builds the graph and checks no clock). A pair counts where both rooms are studied, each room's coder recorded the other, and the two sides record one act from both ends (attacked and attacked-by, gave and asked help, negotiated, allied). There are 476 such pairs. For each, the script takes the smallest gap between a concept of one side and a concept of the other:
- 187 lie within 1 hour;
- 142 more lie within 6 hours;
- 105 more lie within 24 hours;
- 42 lie further apart.

Ten pairs drawn by seed, read by hand with `cite.py`:
- **Four date one encounter close together, as the words say.**
  - r/anime and r/satania, 0.91 hours: the sign's maker thanks r/satania, and r/satania gathers its threads.
  - r/europe and r/formula1, 2.6 hours: "let them have their white border", then "EU flag overlaps with our logo".
  - r/chibears and r/finland, 0.04 hours: one member's comment, whose edit links the plea that member then posted in r/finland.
  - r/suomi and r/unitedkingdom, 0.83 hours.
- **Four hold different moments of a longer tie:** r/uiuc and r/uofm, r/stevenuniverse and r/yogscast, r/OnePiece and r/pathofexile, r/lakers and r/nbaspurs.
- **Two hold concepts that do not speak of each other:** r/placestart and r/thebluecorner; r/argentina and r/uruguay, where the nearest r/argentina concept is about the room's own work, not about r/uruguay's call for help.

No pair dates one encounter at two times. One order is unsettled. In r/suomi a member writes "I have opened negotiations" 0.83 hours before the same member's opening post in r/unitedkingdom. The concept's label ties the negotiation to r/argentina's offer, so the words do not settle with whom it was opened.

**Datings in written order** (`clocks.py`). In 237 of the 598 case accounts with two or more datings in their Chronology, the datings step back at least once. Each model arrow names 2 to 4 rooms (A21 names none), and 14 of the 21 arrows name at least one such room. This does not touch a loop: stage C2 admits a loop only where one room's datings run the whole way round, and the model grounds no loop. The arrows' order rests on the items' own times, which the transitions carry, not on the order in which a case account tells its threads. A Chronology that steps back tells one thread and then returns to an earlier one.

## 5. Defects named at this leg

Eight lines were appended to `defects.jsonl` (lines 102 to 109, stage E1, leg E1b-01), by `_analysis/e1b01_defects_lines.py`. No earlier file is changed.
- **The instrument's (5):**
  - my translation in quotation marks (`account-p1.md` 23);
  - the two D6 quotes carried from case accounts (r/greece, r/paladins);
  - two small misquotes of the instrument (`notes-C1.md` 144 and 453);
  - three examples of my own in quotation marks;
  - five paraphrases in quotation marks in the readers' room models.
- **Provenance (1, not sure):** J's reading instruction in `notes-B2.md` has no record before my own Write.
- **The material's (2):**
  - the case accounts' translations, labels and phrases in quotation marks;
  - one store pointer whose name holds two rooms.

## What this part cannot say

- Whether 33 case-account strings and 7 reader quotes are the participants' words. They come from uncoded items, which neither the store nor the forest holds.
- Whether the coder or the build wrote each concept's time.
- Whether J's reading instruction was worded as `notes-B2.md` quotes it.
- How the 80 rooms of the raw check would compare with the other 625. The 0.6573 is that sample's share, and my sorting of its 389 listed strings is a reading of the listed strings only.

# Audit, section 1, part 2: the orderings, the counts, coverage and the canvas (E1b-02)

Written at E1b-02, 27 October 2026. This part covers four items of stage E1 section 1: the orderings proved by snaps, the counts rule, coverage, and rule 7's uses of the canvas. It also reports J's answer to QE1-001. Every figure comes from a script in `audit-E1/`, with its output beside it, or from a reading by hand that the diary logs. The scripts written at this leg are `prior_sections.py`, `snap_order.py`, `counts_phrases.py` and `counts_sample_check.py`; E1a's `orderings.py`, `counts_rule.py`, `coverage.py` and `canvas_uses.py` are read here. Each script states its rule in its docstring, written before it ran. A first run with a fault is kept under a `.superseded-N` name.

## 1. Orderings proved by snaps

A snap (`out/_snap/<name>.sha256`) holds the hash, size and time of every file in `out/` at one moment. At E1a's count there were 658 snaps with a header, from 6 October 12:29 to 27 October 15:33. For each ordering the stage names, the table says whether the snap's hash equals the file's as it stands, or whether the file moved after the snap, and which.

| ordering | result | what the snaps show |
|---|---|---|
| The scheme frozen before B3's first batch | **held** | `scheme_final.jsonl` has two hashes in all snaps. `fb8b543a9898` is at B2b-r3-p3's close (12 October 12:43:18Z). `4b471d29dd41` is in 541 snaps, from B2c's packets-out (13:10:24Z) to now. B3's first fleet call was at 15:17:38Z. The file has not moved since. |
| `prior.md` sections 1 to 6 sealed before B1's first `theme_discovery.jsonl` line | **held**, proved by rebuilding the text | `prior.md` has two hashes in all snaps. `7aa5240047ce` is in 321 snaps, from B1a's close (7 October 13:16:39Z) to C5. The first theme line is at 13:56:08. `prior_sections.py` rebuilt the file from the analyst's writes in the transcripts: a Write at 13:13:59Z and an Edit at 13:15:03Z give `7aa5240047ce`. Two Edits at D1a (15 October 15:56Z) give `720068eeaf87`, the file as it stands. Section by section, the preamble and sections 1 to 6 are the same, byte for byte, then and now. Only sections 7 and 8 changed: at B1 both held the same placeholder text, and now each holds its own. No shell command wrote `prior.md`. |
| Sections 7 and 8 sealed at D1 before `DROPS/D/` was ingested | **held** | `720068eeaf87` is first snapped at D1a's packets-out (15 October 19:44:16Z). The first snap that lists `adaptations.jsonl`, the ingested return, is D2a's adaptations-in (16 October 10:17:19Z). The file has not moved since. |
| The model hashed at C5's close before D1 | **held; the model moved after, by declared amendments** | `e15f96470271…` is at C5c-13's close (15 October 14:42:06Z), and D1's first snap is at 19:44:16Z. The model moved at D3, to `46384686d617…`, by the return's rulings (moves 172 to 197). That is the model at D6 and now. |
| Every D4 move snapped before `projections-D4.jsonl` and the chunk-share tree | **held for the branch cuts; the room forms came after, by J's ruling** | 34 D4 move snaps changed `branches.jsonl` from the snap before (moves 201 to 236). The last, `D4-move-merging-236`, is at 25 October 16:21:31Z. The first snap that lists the projection is D4a-03's interview cut at 19:16:07Z. 82 D4 snaps list the projection or the chunk-share files, and none of them changed `branches.jsonl`. `branches.jsonl` as it stands equals its last D4 snap. |
| Every move snap at C2 to D3 | **held** | 198 move snaps carry the move numbers 1 to 197, with none missing. Sorted by number, they are sorted by time, but for one pair. `D3-move-181-1` (21 October 09:31:59Z) is a second snap of move 181's state, 24 seconds before `D3-move-developing-181`. The diary named it as wrongly named and unused at D3a-53. |
| Every D6 proposal against its evidence and status | **status held**; evidence in part 3 | `proposals-D6.jsonl` holds 11 lines, all `unvalidated`, all on base `46384686d617…`, the D3 freeze. `amendments-D6.jsonl` holds 0 lines. The file has 6 hashes in 19 D6 snaps, and each change falls at the leg its new lines name (D6a-01 to D6a-07). It is unchanged from D6a-07's close to D6a-18's. |

A hash shows a whole file, not each of its lines. So these are self-reported:
- that the earlier lines of `proposals-D6.jsonl` stayed as written while lines were added;
- every other claim the run makes about the order of its work.

**QE1-001.** Stage E1's close-check first counted as errors the 82 D4 snaps that list the projection. J ruled on 27 October (18:45 Berlin, through the principal investigator): "Yes. I would not change the structure of the journey for bookkeeping." The handler amended the check. A D4 snap now counts as a branch cut only where it changed `branches.jsonl`, and the 82 are printed as findings. `snap_order.py` confirms that none of the 82 changed the branches. They are the six room forms, made after the projection at J's instruction: the D4a-03 interview cut, the closes of D4a-04 to D4a-08, and moves 238 to 313. They are not a recut of the branches.

## 2. The counts rule (rule 19)

**The census, stated twice** (`counts_rule.py`):
- `package/store/rooms.jsonl` lists 705 rooms, and 705 room folders hold a case account. They are the same set.
- `dropped.jsonl` holds 0 lines, so there is no drop and no reason to give.
- `tools/counts.py` gives 705 analysed rooms, 115,388 concepts and 7,844 second-order themes.

**Stage D4 section 4's four counts:** 476 in a branch + 0 unadapted + 229 in no branch + 0 unreturned = 705, which is `n_analysed`.

**The head's ledger figures**, against the ledgers as the head stands now (`counts_phrases.py`). All seven agree: adjudications 96,568, verdicts 1,029, tier history 1,026, model history 182, findings 45, elements 45 and arrows 21. E1a's `counts_rule.json` shows tier history 1,020 against 1,026. That is no longer true: it read the head before E1a's own Edit.

**Every count in every handback.** `counts_rule.py` found 361 phrases of a number and a counted noun in the 18 handbacks.
- `counts_phrases.py` sets aside 32 that are not counts: 26 whose number is followed by a comma (an id, a move number or a list item) and 6 decimals. That leaves 329 counts.
- Checking 329 by hand is more than one leg can do, so a seeded sample of two per handback, 36, was checked by `counts_sample_check.py` and by hand. The sample is drawn by `out/seed.txt`, and its rule was written before the run.

| result | counts | which |
|---|---|---|
| recomputed from the governing file, and agree | 27 | One of them, handback-A1's "7 lines" of defects, became 8 later in A1, as the same handback's line 72 records. |
| agree with a stated parameter or list | 4 | 500 shuffles (twice) is `c2_arrow_evidence.py`'s default; the 6 items are `field-C4.md`'s list 3; the 20 arrows are the 20 drawn in `figure-C5.md`, where A21 is not drawn. |
| rest on a judgment by hand that no file lets me recompute | 3 | A1's "79 of 100 concepts" (`coordinating-rule-A1.md` line 85); C4's "78 rooms" (`field-C4.md` line 115); D3's "48 rooms" (`notes-D3.md` line 6965). |
| **disagree** with the governing file | 2 | See below. |

- **handback-B1.md line 20** says "107 episode lines" whose kinds none of their rooms holds. `notes-B1.md` line 3108, written at B2 with `_analysis/b2_episode_kinds.py`, counts 106 (line, kind) pairs over 81 lines and says the 107 is wrong. The handback was not corrected. The handback is wrong.
- **handback-C5-p14.md line 45** says the model's history holds "31 lines (12 element, 12 arrow, 5 condition, 1 role, 1 claim)". `model/history.jsonl` holds 45 lines of stage C5 up to pass 14's leg, C5c-11: 16 element, 21 arrow, 5 condition, 1 role and 2 claim, over 30 distinct ids. 31 matches neither count, and the handback does not say how it counted. The handback is wrong.

My checking scripts had faults; the outputs of each first run are kept:
- `counts_phrases.py` first took any comma into the number and set aside no phrase.
- `counts_sample_check.py` first read a key the B3 defects lack.
- It also first read the analyst's D3 rulings in place of the re-check readers' verdicts.
- It then grouped those verdicts by the readers' own spelling of the room ("LAX" and "lax", "The R" and "The_R") until the room's folder was used.

The final message of each stage is in its transcript and is read with the diary in part 5. **293 handback counts were not checked.**

## 3. Coverage

Rooms read whole, counted from the read logs (`coverage.py`), one record per read. A log names the log that was open, not the stage the reading served.

| log | `mem.py room`: reads (rooms) | `mem.py forest`: reads (rooms; read whole) | case account: reads (rooms) | `cite.py`: reads (rooms cited) |
|---|---|---|---|---|
| A1 | 1,936 (705) | 205 (155; 1) | 887 (705) | 4,681 (663) |
| B1 | 1,873 (705) | 305 (110; 110) | 0 | 2,562 (455) |
| B2, B3, B4 | 0 | 0 | 0 | 0 |
| C1 | 0 | 1 (1; 0) | 0 | 71 (111) |
| C2 | 343 (67) | 498 (67; 67) | 0 | 1,144 (364) |
| C3 | 0 | 0 | 0 | 36 (30) |
| C4 | 0 | 0 | 0 | 14 (12) |
| C5 | 261 (218) | 32 (32; 32) | 0 | 2,254 (431) |
| D1, D4 | 0 | 0 | 0 | 0 |
| D2 | 0 | 0 | 0 | 2 (2) |
| D3 | 4 (4) | 14,054 (703; 703) | 0 | 77,047 (705) |
| D5 | 10 (8) | 0 | 0 | 6,848 (470) |
| D6 | 0 | 0 | 77 (40) | 845 (372) |
| **in all** | **705** | **705; 704 read whole** | **705** | **705** |

- **No room is unread.** Every one of the 705 analysed rooms was read by `mem.py room`, by `mem.py forest` and through its case account. 704 forests were read whole. The one short is r/COSI. Its forest was read once, at A1, from line 11 to line 18 of 18, so the ten header lines were skipped and every line of its tree was read.
- **A log that reads nothing is no gap.** B2, B3, B4, D1, D2 and D4 read no room through `mem.py`, because the fleets read for those stages. Readers and labelers leave no read log. Their reading is in `_fleet_raw/`:
  - B2: 6 rounds;
  - B3: 1,223 entries;
  - B4: 51 entries, and 55 for the OpenAI arm;
  - D2v and D3v: 708 entries each;
  - `DROPS/D/` holds 706 room entries.
- **Reported apart:** the hostile reader at C2 (`_fleet_raw/C2/C2-reviewer`) and the three readers at C5 (`readers-C5/`, one line each).
- **Refusals:** the read logs hold 3 refused room reads, 1 at B1 and 2 at D5.

## 4. Rule 7's uses of the canvas, stage by stage

Rule 7 lets me read the canvas with every room. It asks that wherever a canvas figure shaped a reading, a cut, a placement, a name or an element, the record says so, with `canvas` among its grounds or in its note. The fleets are never served the canvas. `canvas_uses.py` counts the uses in the logs, and I read the model's and the tree's files for canvas figures.

| stage | use in the logs | declared? |
|---|---|---|
| A1 | `mem.py room` with the canvas, 715 reads; `mem.py canvas`, 722 calls over 705 rooms | Yes: the `made` line and the reading route (`departures.jsonl` line 5). |
| B1 | 1,874 room reads showed the canvas (with `--size`) | The reads are allowed. No placement carries a canvas ground, and the record names nothing they shaped. |
| C2 | 22 room reads with the canvas (19 rooms); 321 with `--no-canvas` | The same as B1. |
| C5 | 218 room reads with the canvas; 43 with `--no-canvas` | The same as B1. |
| D3 | 4 room reads with the canvas | The same as B1. |
| D4 | the projection (`projections-D4.jsonl`, the chunk-share tree), after the branch cuts | Yes, and in order (part 1). The 75 D4 tier-history grounds that name the canvas all say that no canvas field was used. |
| D5 | 5 room reads with the canvas; `mem.py canvas` twice (D5a-40, D5b); the canvas fields of `branches-D5.jsonl` (35 branches) | Yes: `survival-D5.md` reads them after the record. |
| D6 | D6b read D5's survival output | Yes: `notes-D6.md` says the survival reading by form comes from the record and that the canvas is not read. |

**Undeclared uses found: none.** No element, arrow, proposition, finding or branch carries a canvas figure. The passages that name the atlas, artwork or survival are members' own acts or the coded record:
- P12's "atlas entries" are entries members wrote;
- "artwork" in A05's support is in a member's quote;
- F-021's bound says "The canvas is not evidence (rule 7)";
- in F-023, F-027, F17 and F18, what "survives" is in the coded record or in the rooms' own judgment.

The B1, C2, C5 and D3 reads are the open question. The canvas was on the page while I placed and ruled, and the record names nothing it shaped. The logs cannot tell whether it shaped nothing or shaped something undeclared, so that is self-reported.

**Where the canvas may have shaped the work without a declaration**, for a reader to look:
- **Elements argued mostly from what rooms kept:** P12 (records), P13 (carrying on), P22 (which version is kept), A09 (the record carried on), and the account's survival paragraph, which rests on the `work_remained` field (defects line 100).
- **Branch names that say what rooms did with their work:** F09 (rooms rebuild after moving), F12 (the spine restarted on another canvas), F17 and F18 (success judged by what survives), F23 (the close scoped to the original canvas) and F32 (rooms keep after marking).
- **The cuts made after the projection:** the six room forms, cut with `projections-D4.jsonl` and the chunk-share tree in the folder (the 82 snaps of QE1-001). Their grounds say no canvas field was used.

## 5. Defects named at this leg

Two lines were appended to `defects.jsonl` (lines 110 and 111, stage E1, leg E1b-02) by `_analysis/e1b02_defects_lines.py`. They are the two handback counts that disagree with their governing files (handback-B1.md line 20; handback-C5-p14.md line 45). Both are the instrument's. No earlier file is changed.

## What this part cannot say

- Whether the 293 unchecked handback counts agree with their files. The sample of 36 found 2 that do not.
- Whether the earlier lines of `proposals-D6.jsonl`, or of any other file, stayed as written while the file grew. A hash covers the whole file.
- Whether the canvas, on the page in 2,118 of my room reads at B1, C2, C5 and D3, shaped a placement, a ruling or a name that the record does not declare.

# Audit, section 1, part 3: the moves, provenance, the manifest and the figures (E1b-03)

Written at E1b-03, 27 October 2026. This part covers four items of stage E1 section 1:
- the moves;
- the provenance of D6's proposals, with PR-D6-10 against the ruling of D3a-55, and the extra legs D6a-09 to D6a-18;
- the manifest, whole;
- the fleet's figures, restated with their definitions.

Every figure comes from a script in `audit-E1/` with its output beside it, or from a reading by hand that the diary logs. The new script is `provenance_D6.py`. E1a's `moves.py`, `manifest.py` and `fleet_figures.py` are read here.

## 1. The moves

**`tier_history.jsonl`, 1,026 lines, by stage and tier.**

| stage | third order | fourth order | dimension | the tree |
|---|---|---|---|---|
| B1 | 252 | | | |
| B2 | 140 | | | |
| C1 | 1 | 28 | | |
| C2 | 6 | 40 | 9 | |
| C3 | | 2 | | |
| C4 | | 2 | | |
| C5 | 2 | 61 | 18 | |
| D4 | | | | 459 (branch 35, cross-link 348, room form 43, room sub-form 33) |
| D6 | | | | 6 (room form, final names) |

By move, the tier history uses seven of Grodal, Anteby and Holm's eight moves, and the run's joint label "relating or contrasting": relating 357, asking questions 255, merging 105, dropping 93, relating or contrasting 76, developing or dropping working hypotheses 76, splitting 58, contrasting 6. "Focusing on puzzles" is never named.

**`model/history.jsonl`, 182 lines.** By stage: C2 82, C3 3, C4 3, C5 46, D3 38, D4 10. Two names are not among the eight:
- **"Stabilizing"**: 2 lines at D3. An appended D3 line corrects move 174's name to developing working hypotheses.
- **"Sequencing"**: 18 lines at C2a-01 to C2a-03, where arrows were added. No line or note declares or corrects the name. This is a defect of naming. Each of these moves has its snap, so the provenance stands.

**Recuts after C5.**
- No third-order, fourth-order or dimension line was written after C5. The D4 and D6 lines of the tier history are the tree's: the branches, the cross-links and the room forms.
- The model history holds 48 lines after C5: 38 at D3 and 10 at D4. All 48 name a D3 cause: return lines, the re-check, or the lines they correct.
- Two of the 48 carry the held-proposal mark (P05 and A11, moves 198 and 199), and two are the reverts (move 203, J's QD4-001).
- So every model change after C5 is either a rule 11 amendment with its D3 cause or a held proposal.

**The move snaps against the diary's move lines.** From C2, a claim with no provenance is a defect.

| stage | diary move lines | move snaps | how compared |
|---|---|---|---|
| C2 | 47 | 47 | by count (the diary's lines carry no number) |
| C3 | 3 | 3 | by count |
| C4 | 2 | 2 | by count |
| C5 | 119 | 119 | by count |
| D3 | 27 (26 numbered) | 27 | by number: no numbered line lacks its snap; the one snap with no line is the duplicate `D3-move-181-1`, declared at D3a-53 |
| D4 | 116 | 116 | by number, one to one (moves 198 to 313) |
| D6 | 6 | 6 | by number, one to one (moves 314 to 319) |

Before C2 the snaps are numbered per move name, so they are counted only. B1 has 6 lines and 6 snaps. C1 has 214 diary move lines against 29 snaps. The 29 are the 28 fourth-order cuts and one moved theme, and they match C1's 29 tier-history lines. The other 185 lines all begin "reassigned": each moves one room's second-order theme from one placement to another.

## 2. D6's proposals and the legs D6a-09 to D6a-18

**The eleven proposals** (`proposals-D6.jsonl`, `provenance_D6.py`). All 11 are `unvalidated` on base `46384686d617…`, the D3 freeze, and `amendments-D6.jsonl` holds 0 lines.
- **Evidence.** The proposals name 254 concept ids, and all are in the store. They name 61 other items (fractal lines, files, room lists and one finding, F-026, which exists), and none fails to resolve.
- **Record.** Each proposal has at least one diary line at the leg that wrote it, D6a-01 to D6a-07.
- **Provenance.** No proposal lacks it.

**PR-D6-10 against D3a-55.** The scope rule, written in `notes-D3.md` at D3a-55 before any propose line was read (lines 1464 and 1475), put "the subs' own April Fools pranks, styling and games (T4-001's themes)" outside the model's scope, as particulars. PR-D6-10 proposes a process element under Host framing: the sub administers its play. Its `change` field says that it "would bring into the model what the ruling of D3a-55 put outside its scope", and it leaves "whether the scope is widened" to a later model. So the proposal names the ruling it would reverse, and it changes nothing: it is a proposal, not an amendment. Its evidence holds 89 concept ids, all in the store.

**The extra legs D6a-09 to D6a-18** (the form telling, its second round and the Dutch telling). Between the close of D6a-08 and the close of D6a-18:
- **Unchanged:** the model, its history, the tiers, the scheme, the assignments, the branches, the cross-links, the return's ledgers, the verdicts, the findings, the propositions, the proposals, the amendments, the fractal lines, the room forms, the defects and the account.
- **Changed:** `departures.jsonl` gained line 21 at D6a-09. Under J's ruling 1d, it records as a dated amendment a widening of D6's branch-naming rule, and it says the amendment applies backwards. The amendment states that the widened readings were in use from D6a-02, before they were written down at D6a-04. That makes it a provision acted on before it was written, and it is reported in the departures section (part 6). No branch line was rewritten.
- **Added:** `retelling-D6.md` was written at D6b, between the two closes.

## 3. The manifest, whole

`run_manifest.json` holds 19 entries, for stages A1, B2, B3, B4, C2, C5 and D2, and each names a model, seeds and decoding. These fleet figures have complete provenance:

| file | entries |
|---|---|
| `stability-B2.md` | 8 |
| `fidelity-B3.md` | 2 |
| `position-B3.md` | 2 |
| `transmission-B4.md` | 5 |
| `transmission-after-revision-B4.md` | 5 |
| `review-C2.md` | 1 |
| `account-readers-C5.md` | 1 |
| `verdicts-D.jsonl` | 1 |

**Missing:** the D3 re-check return (`adaptations-recheck.jsonl` and each room's `verdict-D-recheck.jsonl`) has no entry. Each room's `run-recheck.json` names the readers' model (gpt-6.1-sol) and a session, but no seed and no decoding. The re-check's figures, among them the verdicts of all 705 rooms at the re-check, therefore have partial provenance. The analyst's own figures come from scripts in `out/_analysis/` and `audit-E1/`, which state their seeds. The analyst's model and effort per stage are set in `arm.json`, not in the manifest.

## 4. The figures restated

FLEET.md section 2 defines each figure, and says what all of them license: "readers share an architecture with you or with each other, so they bound whether the written instrument decides, never whether it is right." Readers in fresh contexts are instances of one model, not two minds. None of these figures is given either of the two names FLEET.md section 2 bars. No file of the run gives any of them those names; the one passage near them, in `notes-B3.md` line 11, discusses what a second reader per item would have bought.

| figure | FLEET.md section 2's definition | the run's value | where |
|---|---|---|---|
| fidelity | how often a reader holding only the frozen instrument lands where I did | gold fidelity 0.624 at B2; 0.645 at B3 (the whole fleet); corpus readings of gold items 0.683 | `pilot_report.md`, `fidelity-B3.md` |
| agreement | how often the readers of one item agree with each other, with Krippendorff's alpha, and Jaccard where rule 0 allowed more than one theme | B2: 0.800 and 0.756 inside the two stability rounds, 0.818 inside gold, alpha 0.784 (six readers) and 0.794 (nine); B3 corpus: 0.786, alpha 0.782 | `stability-B2.md`, `handback-B3.md` |
| gold fidelity | fidelity on gold items seeded unannounced into live batches | 0.645 at B3; its fall against B2 on the same items, -0.014 (interval -0.031 to 0.003), sits inside the floor of 0.193 | `fidelity-B3.md` |
| stability | the same reader arm agreeing with itself on the gold set under two rewordings of the brief | 0.807 (B2) | `stability-B2.md` |
| transmission | whether the written instrument carries my judgement, decomposed over items where my answer is on record (40 gold, 50 pilot) | the scheme decides 21 and 30; fails to transmit 1 and 0; the instrument does not decide 6 and 12; teaches something unintended 12 and 8 | `transmission-B4.md` |
| transmission after revision | how often fresh readers holding only the revised instrument reproduce the adjudicated line, which is my own line | arm 1's two readers agree at 0.781 on the uniform stratum, under the floor of 0.807; arm 1 disagrees with the settled line on 0.742 of readings of contested items and 0.400 of unanimous ones | `transmission-after-revision-B4.md` |
| position curve | the outcome against position within the batch | agreement +0.003 over 14 positions (interval -0.015 to +0.022; the fit would catch 0.027); the arguable rate rises +0.040 | `position-B3.md` |
| the verdict fleet's disagreement rate | how often the D2 readers' verdicts differ | 163 of 705 rooms with two readers (0.2312) | `verdicts-D.jsonl` first return (`fleet_figures.py`) |

## 5. Defects named at this leg

Two lines were appended to `defects.jsonl` (lines 112 and 113, stage E1, leg E1b-03), both the instrument's:
- the 18 C2 model-history lines named "sequencing";
- the D3 re-check return with no manifest entry.

No earlier file is changed.

## What this part cannot say

- Whether each of C1's 185 reassignments matches its line in the assignments ledger. They are counted by their first word, not read one by one.
- The seed and decoding of the D3 re-check readers.
- Whether the earlier lines of `proposals-D6.jsonl` stayed as written while the file grew (part 2 of this section).

# Audit, section 1, part 4: claims against their evidence (E1b-04)

Written at E1b-04, 27 October 2026. The table is `claims-E1.md`, which the methods paragraph cites. It is built from `audit-E1/claims.py` (E1a), `audit-E1/claims_returns.py` (this leg) and a reading by hand of `prior.md` section 3 and of the switch records in `literature-C3.md`.

**The propositions (9).**
- 7 declare pattern and 2 declare both. Every one names a rival and a falsifier elsewhere.
- The pattern evidence is of its kind: counts with their denominators, and an order beating a null of 500 shuffles within each room, for 18 of the 20 arrows the propositions rest on.
- The words evidence holds: the arrows' 57 support quotes all resolve, and the 8 findings named all resolve.
- N07 declares both, but its pattern half is not established. A11 does not beat its null, and A12 has no order count. N07 says so, being marked theorised and thin. It rests on read replies and on the return's 691 accepted instantiations of A12, so it is half-validated, not validated with the other kind's evidence.
- **No proposition is validated with the other kind's evidence.**

**The branches (35).**
- Each rests on its shared key for membership and on its account's cited concepts (38 to 89 each) for what it is, so each is validated by both kinds, as `prior.md` section 3 asks of forms.
- 2 are forms with a supported warrant (F09, F32) and 33 are groupings with the warrant unresolved.
- Local validation is established for none.

**prior.md section 3, declared against done.**
- The population pattern was to be supported at held size and read against section 4's brackets. No arrow's order test was run at held size. Only A20 is read inside a bracket, before hour 73.
- This is the one gap between what was declared and what was done, and it is in `defects.jsonl` (line 114, the instrument's).
- The forms rest on both kinds, as declared.
- The particular histories rest on the room models and the case accounts. The element-reach half of the local measure is 4,759 of 5,380 themes with a coordinating turn (88.46 per cent). The other half was not computed, so local validation is not established.

**The switch records (2)**, both against the ledger.
- Leg 1 records none, and none happened: F-006 was bounded by another count.
- Leg 2 moved the concept's name to the literature's, and moved its form claim from exemplars to a pattern across rooms (F-014). Its function claim failed (F-015). It superseded no finding, as it says.

## What this part cannot say

- Whether the arrows' order would hold at held size. The test was declared and not run.
- Whether the order of A07 to A09 is the clock's, as N04's rival says. Their counts are not read against the hour-73 bracket.

# Audit, section 1, part 5: the diary, the probes and the unplaced (E1b-05)

Written at E1b-05, 27 October 2026. This part covers three items of stage E1 section 1: the diary against the transcript, the recall probes (whose full tables are in `probes-E1.md`), and the unplaced, read. The new scripts are `diary_tool_lines.py`, `probes_notes.py` and `unplaced_kinds.py`. E1a's `diary_transcript.py`, `probes_score.py` and `unplaced.py` are read here.

## 1. The diary against the transcript

`diary_transcript.py` (E1a) drew 17 legs by seed (`cd472a6087a223d4`): one per stage, and one more among the extra legs D6a-09 to D6a-18. They are A1b-16, B1b-30-p2, B2b-r1, B3a-p2, B4a-05, C1a-07, C2a-02, C3a, C4a, C5c-02-p2, D1a, D2a, D3a-15, D4a-03, D5a-31, D6a-10 and D6a-17. Every drawn leg has its transcript.

Of their 905 diary lines, 392 are found word for word in the leg's transcript. The other 513 are lines a tool writes from its own arguments ("placed", "opened", moves, asks, adjudication notes), so their words are not the command typed. Each was read against the tool calls of its leg:

| how it is borne out | lines |
|---|---|
| a tool call or output within ten minutes holds the line's ids (`diary_tool_lines.py`) | 185 |
| a row of the files that B1b-30-p2's `b1_multiplace_write4.py` runs read (`b1_multiplace_b1b30.tsv`, `b1_multiplace_b1b30p2.tsv`) | 282 |
| a single placement in that leg's `b1_place.py` commands (`<sub> t07=T3-043` and the like), all 19 matched | 19 |
| the 27 move lines of C5c-02-p2, written in 41 seconds by `c5c2_decl_amend.py` from `c5c2_decl_spec.json`, both written and dry-run in the transcript a minute before | 27 |

**All 905 diary lines are borne out by the transcript, and no entry is a defect.** The loosest test is the one for the 282 TSV rows. It shows each row in a file the leg's script read, not a time-matched call for each line.

## 2. The recall probes

`probes-E1.md` holds the tables. The figures:
- **300 answer files.** As filed, `probe.py` could not read 283 of them, which are written in bold markdown, so goal is right 17 times and missing 283 times.
- **Re-read** by `probe.py`'s own rules against the expected values stored at each close:
  - goal: right 298, wrong 2;
  - open: right 26, wrong 135;
  - rooms: right 48, wrong 125;
  - changed: right 50, wrong 13;
  - next: right 11, wrong 12.
- **n/a**: 780 answers, apart and never counted as recall.
- **The wrong answers**: 269 are notes, because the head, the diary or the question files held the answer at the close. **18 are defects**, because none did: the rooms of 13 B1 legs and one D5 leg, and the changed ids of D4a-06, D4a-07, D4a-08 and D6a-01.
- **A second count for rooms.** The declared test read rooms in the leg's own diary lines, and gave 101 defects on rooms. But the harness's expected rooms are the last three on record, which repeat across legs that opened none. Read over the stage's diary up to the close, 14 of those remain defects. Both counts are on file.

## 3. The unplaced, read

| what | count | what each was |
|---|---|---|
| second-order themes with no placement | 151 of 7,844, holding 407 concepts | the sub's own April Fools play 42 (165 concepts); talk about the event with no organizing act, such as asking what an effort is, admiring, reacting or arguing about the canvas, 72 (186); lost posts whose body is gone, or of which only a title or marker is left, 18 (24, all of them in `unplaced-B1.jsonl`); labels that name an act, 19 (32) |
| concepts unreachable from any theme | 0 | every concept has its theme |
| third-order themes no fourth-order theme took | 2 | T3-017, "carrying on ordinary sub talk" (334 themes placed), outside the model's scope by design (the scope rule written at D3a-55); T3-133, "recovering a hacked sub" (1 theme, rare tier), a host sub's act that could have sat with Boundary work |
| fourth-order themes no dimension gathered | 0 | |

The kinds come from a keyword rule declared in `unplaced_kinds.py` and were then read.

**Whether any should have been a member.** Of the 19 labels that name an act, 10 name one the scheme holds, and they should have been placed:
- germany/t19, a build report;
- h3h3productions/t27, welcoming people into the drawing;
- h3h3productions/t30, arguing over duplicate logo proposals;
- hungary/t05, a call to turn a neighbour's flag;
- linux/t03, writing a bot;
- oman/t06, telling a late helper the work was done;
- opticgaming/t12, mourning the lost work;
- orderofthebluecorner/t02, planning the sign;
- rainbowgrid/t06, taking the grid to other canvases;
- romania/t18, the flag's design.

Six of the ten hold one concept each. The other nine of the 19 are jokes, ordinary sub talk or a bare message. The other 132 unplaced themes are rightly outside: play, talk about the event, or posts with nothing left to read.

## 4. Defects named at this leg

Two lines were appended to `defects.jsonl` (lines 115 and 116, stage E1, leg E1b-05), both the instrument's:
- the 18 probe misses that no record answered;
- the 10 unplaced themes that should have been placed (sure false, a reading of short labels).

No earlier file is changed.

## What this part cannot say

- Whether each of the 282 TSV-borne diary lines was written at the moment of its row's run. The check matches the row, not the second.
- Whether the 10 themes would change any count of the model. Each holds one to five concepts, and none was placed.

# Audit, section 2: the ledgers, the stories, what a reader was given (E1b-06)

Written at E1b-06, 27 October 2026. This part covers stage E1 section 2. Its script is `audit-E1/ledgers_stories.py`, with its rule in its docstring and its output beside it. The readings by hand are logged in the diary.

## 1. The ledgers, complete

**`findings.jsonl`.**
- 45 lines over 27 findings: 32 lines say standing and 13 say bounded. By each finding's last line, 17 stand and 10 are bounded.
- **The status changes**, each the stage of the line that changed it, all from standing to bounded: F-001 at B2; F-002 and F-010 at C2; F-006 at C3; F-014 and F-018 at C5. No finding was withdrawn.
- **The warrant**, by each finding's last line: read 13, inferred 14.
- **No statable `refuted_by`:** 8 findings, F-002 to F-007, F-009 and F-012.

**Every other ledger.**
- 150 jsonl files were counted, each with its lines now. The table is in `ledgers_stories.json`.
- A hash shows whether a file moved, not which line, so "no line edited after writing" can be shown only in part: through the file's size in each snap that lists it. A size that falls shows an edit or a cut; a size that rises proves nothing.
- The append-only ledgers never shrink: the adjudications, both histories, findings, verdicts, defects, departures and asks.
- Nine files do shrink:
  - **State files rewritten by design**, whose changes the histories hold: `model/elements.jsonl` (13 times), `fourth/fourth.jsonl` (7), `dimensions.jsonl` (4), `model/arrows.jsonl` (3), `propositions.jsonl` (2) and `scheme_final.jsonl` (1).
  - **`author_items.jsonl` and `gold_items.jsonl`**, once each, at B2's pilot rerun (B2a-r3 to B2a-r3-p2), before B3 used them.
  - **`fractal-D6.jsonl`**, once, at D6a-02. Its 42 form lines moved to `fractal-forms-D6.jsonl` under departure line 20. The two were compared equal, with one correction made on its own line, and the move is declared in `notes-D6.md`.

**New kinds per hundred themes, at the census:** 197 kinds over 7,844 second-order themes, which is 2.51.

## 2. The stories

| pass | rooms | told | told with residue | not told |
|---|---|---|---|---|
| 1 | 20 | 0 | 20 | 0 |
| 2 | 32 | 14 | 18 | 0 |
| 3 | 32 | 16 | 16 | 0 |
| 4 | 32 | 11 | 21 | 0 |
| 5 | 35 | 16 | 19 | 0 |

- **Passes and rooms.** Five passes ran (`saturation.jsonl`), and the model's story rests on pass 5. Rooms read against a story: 151 in all, 67 distinct.
- **The last story.** It failed to tell no room outright, and told 19 of its 35 rooms only in part.
- **What the reading behind the stories bought.** Of the 638 rooms no story was read against, the first return gives one that does not compose. None of the 67 read against a story is among those that do not compose. Most of each group composes with residue (346 of the 638; 41 of the 67, by a single verdict).
- **Loops.** None passed the one-room test, and the model grounds no loop.
- **The account's passes.** `account_passes.jsonl` holds 15, so the account's loop ran.

## 3. What a reader was given

| the five things | held? |
|---|---|
| the data-structure view's leftmost column holds material, and one row walks from what somebody typed to a dimension | **Held.** The columns run from room, concept id and the member's words to the dimension, in one file. |
| `structure.md` explains every fourth-order theme with its question, what falls outside, and quotes carrying room, author, hour and concept id, with why the set expresses it | **Held.** Every theme has its sections and five quotes (140 `why_this_one` lines). Whether any five make one point was not read. |
| the residue explained, not listed, beside C3's remainder | **Not held.** `account.md` says the last story told 19 of its 35 rooms only in part, and lists those parts rather than explaining them. C3's remainder is 19 themes. |
| `account.md` at one to two pages | **Not held.** It is 3,326 words. |
| every quote dated and attributed | **Not held, in part.** 37 cited quotes; 34 carry an hour and 3 do not. |

**The rooms the account names, against `branches.jsonl`.** The account names 22 rooms, and 17 of them are in a branch. The five in no branch are r/TeamYellowPlace, r/aceattorney, r/anarcho_capitalism, r/cardinals and r/monsterhunter. r/monsterhunter is the account's room for the return's claim.

## 4. The departures, the defects, the forks, rule 9

**The departures**, 21 lines (A1 9, D4 7, D5 2, D6 3).
- **Cost.** Three state what following the provision would have cost, in their own field. **Eighteen do not.**
- **Acted on before written: two.**
  - Line 5, A1's reading route, says it was logged late, at A1c.
  - Line 21, D6's widened branch-naming rule, was in use from D6a-02, before it was stated at D6a-04 and written at D6a-09 under J's ruling 1d.
- Both are defects.

**The defects**, 119 lines in `defects.jsonl` (A1 8, B3 55, D5 38, E1 18). They were sorted by a keyword rule, and the E1 lines by my own labels.
- **The material's:** A1 6, D5 9, E1 2. These concern the store, the packages and the coders' case accounts.
- **The instrument's:** the rest. Among them are the B3 fleet's record slips, the D5 lines on the `work_remained` field (A1's own) and E1's lines on my outputs.
- **One E1 line is provenance:** J's reading rule.
- **Still open from D5:** lines 100 and 101.

**The forks.** No comparison file arrived (`fork_comparison-C2.json` and `fork_comparison-D.json` are absent). So the spread of the fourth-order partition across forks at C2, and of the verdicts at D2, is **none**: there is nothing to compare.

**Rule 9.**
- **What was handed over:** the field's model handed over P21, P22 and A21 at C4a (`origin: from-field`). None of the three was in the model before.
- **Replicated, not discovered:** D3 ruled each standing, shown in the rooms' own lines, so they are reported as replicated.
- **Nothing else:** no other finding about the corpus was handed over by a stage file or the operator. J's words on national content and on reading are instructions, not findings.
- **Still to come:** `EXPECTATIONS.jsonl`, the operator's sealed expectations, is scored in the next section.

## 5. Defects named at this leg

Three lines were appended to `defects.jsonl` (lines 117 to 119, stage E1, leg E1b-06), all the instrument's:
- the account as a reader was given it;
- the 18 departures with no stated cost;
- the two departures acted on before they were written.

## What this part cannot say

- Whether any line of an append-only ledger was edited in place without changing its size, or with a larger replacement. A hash or a size cannot show it.
- Whether any of `structure.md`'s fourth-order themes is given five quotes that make one point.
- What following each of the 18 uncosted departures would have cost.

# Audit, section 3: composition at each level, expectations and contrasts (E1b-07)

Written at E1b-07, 27 October 2026. The figures come from `audit-E1/expectations.py` and E1a's `element_reach.py`, each with its output beside it. The expectations and the field's entries are tabled in `expectations-E1.md`.

## 1. The composition diagnostics, recomputed

**Fixed-global verdicts**, ruled (both readers agreeing, or the analyst's D3 ruling on a split):

| return | model | composes | composes with residue | cannot tell | does not compose |
|---|---|---|---|---|---|
| first | e15f9647… (C5, pass 15) | 201 | 489 | 14 | 1 |
| re-check | 46384686… (D3, the freeze) | 630 | 56 | 19 | 0 |

The readers agreed on 542 rooms at the first return and split on 163. At the re-check they agreed on 544 and split on 161.

**Particulars and corrections met twice.**
- **Particulars:** 2,749 lines were ruled particular, in 545 rooms.
- **Distinct shared changes:** 223, counting one op on one element accepted in two or more rooms. These are the candidates for shared branches, not failures.
- **Accepted changes met in one room only:** 20.

**Limited branching or unbounded revision** (prior.md section 3).
- In A1's seeded reading order, the distinct shared changes number 184 after the first third of the rooms (235), 211 after two thirds and 223 at the end.
- The curve flattens over the last third, which is section 3's sign of limited branching.
- How many rooms carry a particular touching the model's top elements was not counted at this leg.

**Local validation, apart.**
- The element-reach half of section 3's measure was computed at E1a: 4,759 of 5,380 second-order themes that hold a coordinating turn are reached by a standing element (88.46 per cent), and 297 of the 696 rooms with a turn are reached in full.
- The other half, a validated adaptation or a theme listed as unresolved with its reason, was not computed.
- **Local validation is not established.**

**Unresolved evidence, apart:** 14 rooms could not be told at the first return and 19 at the re-check. 944 expectations had no line to test them (`expectations-E1.md`).

**Clusters and distinct global changes, against prior.md section 3.**
- The 223 shared changes gather into 35 branches, which overlap as facets: 476 rooms sit in a branch and 229 in none. Two branches pass the form test (F09, F32); 33 are groupings.
- Six room forms were cut from changes and codes at D4a-05 to D4a-08, by J's ruling.
- A branch's members share a key and the words of their records. A stated condition explains its members jointly only in the two forms.

## 2. Whether composition succeeded, failed or remains uncertain

**At the population level, the model composes in the return's terms.**
- The re-check finds the frozen model composing in 630 of 705 rooms, and in 56 more with residue. No room fails to compose.
- The expectations score 0.924, in-sample.
- The mechanism the composite rests on is the spine, start, call, build and keep, whose order counts beat their nulls; the propositions are tabled in `claims-E1.md`.

**Below it, the population compiles rather than composes**, in Kozlowski and Klein's sense: different rooms contribute different configurations. The facets, the two forms, the six room forms and the particulars in 545 rooms all show it. That word describes how the levels emerge. It is not a success grade.

**At the leaf, composition remains uncertain.**
- Local validation is not established.
- The reconstruction sample, the test at the leaf, has not yet been run; it comes at E1c and E1d.
- The `composition_status` line is written in `audit-E1.md` after that check. Until then, the stated level, scope and evidence are these: the population level is supported in the return's own terms; the leaf is unresolved.
- The original fixed-global verdicts above are kept apart from the current adapted-local status and from shared-branch adequacy, as the stage asks.

## 3. prior.md section 2's expectations, and stage A1's three sentences

| expectation | held? | against |
|---|---|---|
| (operator's) continuity at the top, drops at the bottom, a model all the way down | **In part.** The top holds at the re-check. The branches state mostly restrictions, and the levels go down to room forms, branches and particulars. | the verdicts, `branches-D5.jsonl` |
| becoming able to act rests on a find more than on persuasion; a call alone often draws nothing | **In part.** The start comes before the call in the spine. Most calls get no written reply. | `account.md`, the spine's arrows |
| what to act on is settled before the room speaks, by the canvas, a host or one member's start; votes are rare and late | **In part.** Decided order is rare in the coding but often in the return (C01 taken up where absence was expected in 81 rooms). A template does not settle the design for good (the A11 proposal held). | `expectations-E1.md`, `claims-E1.md` |
| loss of the spot sends a room back; then it moves, shrinks, joins or stops | **Held, thin.** A10, on 21 rooms. F09: rooms rebuild after moving. | `claims-E1.md` |
| what follows organizing is talk about it, and the end clusters near hour 73 | **Held.** The close: celebration, record and carrying on. | the propositions, `waterfall-D5.md` |
| a handful of forms, differing in where work is coordinated and on whose terms the room holds its space; the national rooms not one form | **In part.** Six room forms, two of them (behind the thread; moving for the spot) close to the expected kinds. The national rooms spread across forms (the Dutch telling of D6). The branches are facets, not forms. | `room-forms-names.md` |
| at the top the population compiles; limited branching for deals and venues; particulars for rooms carried by one member | **Held for compilation and limited branching.** Particulars are far wider than expected: 545 rooms. | this section |

**Stage A1's three sentences** (`notes-A1.md`, "Three sentences on what I expect"), against the structure:
- *One burst of calls, coordinates and reports, then a long tail of defence and looking back, stopping near hour 73.* **Held.** The dimensions of coordination, upkeep and imprinting carry it.
- *Fights with canvas neighbours more than distant rivals; deals about borders and space, in the thread or sent to Discord.* **Held in part.** Border terms and the chat carry it, but a tie from before the canvas can name the rival (C02, untested for order).
- *The goal settled in the first hours by one person's call, and changed only under a neighbour's pressure or a loss, rarely by argument inside the room.* **Not held.** Form C, "the design reopened" (96 defining rooms), and the return's 627 accepted restrict lines on A11 show the design argued and reopened inside rooms.

## 4. The onset contrast

The late side of every arrow holds 0 to 15 rooms, so by rule 6 no gap is read. A1's four expectations on onset are untested by these counts, as a boundary condition the record could not test. `expectations-E1.md` gives the figures.

## What this part cannot say

- Whether the model composes at the leaf. That is the reconstruction's test (E1c, E1d).
- How many rooms carry a particular that touches the model's top elements.
- Whether any expectation scored here would hold out of sample. None was held out.

# Audit, section 4: the reconstruction sample (E1c, E1d)

Written at E1d, 28 October 2026. The figures come from `audit-E1/reconstruction_validate.py`, `audit-E1/reconstruction_causes.py` and `audit-E1/reconstruction_tables.py`, each with its rule in its docstring and its output beside it. The return, one line per room, is `reconstruction-E1.jsonl`.

## 1. The build and the dispatch

- **The sample (E1c).** Thirty rooms were drawn by seed from the ledgers before any was opened (`audit-E1/reconstruction_draw.py`; `reconstruction-sample-E1.jsonl`). By the first return's ruled verdict: does-not-compose 1, cannot-tell 2, composes 8, composes-with-residue 19. They fall in 20 branches, one room each, and 10 rooms sit in no branch. `notes-E1.md` names them.
- **The packets.** Each holds the skeleton from `rebuild.py` at the frozen model 46384686…, the coder's `case.md` and the room's second-order themes. They run from 29,610 to 47,848 bytes. `RETURN-E1.md` asks the reader to score each claim of `case.md` as accounted yes, partly, no or unresolved, with the element or arrow id.
- **The dispatch**, outside my session, ran from 22:29Z to 22:40Z on 27 October. One reader per room, deepseek/deepseek-v4.1-flash on the gateway route at medium reasoning effort (`_fleet_raw/E1/arm.json`), cost 1.728235 USD for 916,006 input and 2,267,673 output tokens (`_fleet_raw/E1/DONE`).
- **The defect that stopped it.** fleet.py judged 0 returns valid and all 30 rooms exhausted after three attempts each. Every packet ends by asking the reader to return its lines "and then the end marker the return specification names". `RETURN-E1.md`, which I wrote at E1c, names no marker. So each reader ended with a marker of its own: END OF PACKET in 22 rooms, END OF RETURN in 6, and two other forms in 1 room each. That last line is not JSON, and fleet.py rejected the whole return (`defects.jsonl` line 121). At the PI's instruction there was no re-dispatch.

## 2. The returns validated

- **The rule**, written before the run: for each room, the newest raw file; one final line that is not JSON is dropped and recorded; any other line that is not JSON makes the return invalid; the claim lines carry the room and one of the four values; the summary's counts equal the claim lines.
- **The result.** In all 30 rooms the newest raw file is the third attempt, by modification time and by attempt number alike. Its one final line is a marker, and it was dropped. Every other line parses. The summary's counts equal the claim lines in all 30, and every summary states the model 46384686d617.
- **25 rooms are valid under the rule as first written.** The readers of picturegame, python, ReBoot, tagpro and Madeon wrote the room as "r/" with its name on every line. The packets name each room that way, and `RETURN-E1.md` does not say which form it wants (`defects.jsonl` line 122). An amendment made after the first run, and dated in the script, reads that form as the room. Under it, all 30 are valid. The first output is kept (`reconstruction_validate.superseded-1.json`), and both counts are reported.

## 3. Fidelity, by verdict and by branch

Fidelity, as `RETURN-E1.md` defines it, is yes plus half of partly, over yes, partly and no. Unresolved claims are reported apart and are never failures. A no whose reason begins "contradicts" is counted as contradicted.

**Fidelity by verdict** (the first return's ruled fixed-global verdict, model e15f9647…)

| verdict | rooms | mean fidelity | claims | yes | partly | no | unresolved | contradicted |
|---|---|---|---|---|---|---|---|---|
| composes | 8 | 0.911 | 537 | 474 | 29 | 31 | 3 | 0 |
| composes-with-residue | 19 | 0.875 | 1,161 | 965 | 112 | 73 | 11 | 0 |
| cannot-tell | 2 | 0.770 | 40 | 25 | 10 | 4 | 1 | 0 |
| does-not-compose | 1 | 0.680 | 50 | 26 | 16 | 8 | 0 | 0 |
| all | 30 | 0.871 | 1,788 | 1,490 | 167 | 116 | 15 | 0 |

- The mean is 0.871 over the 30 rooms, and 0.884 over the 25 valid under the first rule. The range is 0.637 (simonfraser) to 0.975 (ReBoot), and the median is 0.910.
- **No claim is contradicted.** 15 of 1,788 claims are unresolved, 8 of them in mls.
- By the first return's verdict, mean fidelity falls in the verdicts' own order, from 0.911 (composes) to 0.680 (does-not-compose). The two lower strata hold 2 rooms and 1, so this is an observation, not a test.

**Fidelity by branch** (the room's most specific branch; each sampled branch holds one room)

| branch | room | verdict | fidelity | claims | yes | partly | no | unresolved |
|---|---|---|---|---|---|---|---|---|
| F01 | ethoslab | composes | 0.932 | 81 | 74 | 3 | 4 | 0 |
| F02 | thenetherlands | composes-with-residue | 0.971 | 70 | 67 | 2 | 1 | 0 |
| F03 | hunterxhunter | composes | 0.911 | 45 | 38 | 6 | 1 | 0 |
| F06 | mls | composes-with-residue | 0.891 | 86 | 68 | 3 | 7 | 8 |
| F07 | puzzleanddragons | composes-with-residue | 0.959 | 62 | 57 | 3 | 1 | 1 |
| F08 | slovenia | composes-with-residue | 0.735 | 49 | 25 | 22 | 2 | 0 |
| F10 | seolhyun | composes-with-residue | 0.925 | 40 | 35 | 4 | 1 | 0 |
| F15 | ucf | composes | 0.896 | 74 | 64 | 1 | 7 | 2 |
| F16 | dwarffortress | composes-with-residue | 0.910 | 78 | 70 | 2 | 6 | 0 |
| F18 | kirby | composes | 0.939 | 107 | 98 | 5 | 4 | 0 |
| F23 | physical_removal | composes-with-residue | 0.930 | 72 | 64 | 4 | 3 | 1 |
| F24 | hyperlightdrifter | composes-with-residue | 0.940 | 92 | 86 | 1 | 5 | 0 |
| F25 | picturegame | does-not-compose | 0.680 | 50 | 26 | 16 | 8 | 0 |
| F26 | python | composes | 0.822 | 46 | 33 | 8 | 4 | 1 |
| F28 | necrodancer | composes-with-residue | 0.917 | 42 | 36 | 5 | 1 | 0 |
| F29 | tagpro | composes-with-residue | 0.906 | 53 | 45 | 6 | 2 | 0 |
| F30 | simonfraser | composes-with-residue | 0.637 | 51 | 19 | 27 | 5 | 0 |
| F33 | superman | composes-with-residue | 0.927 | 55 | 51 | 0 | 4 | 0 |
| F34 | penguins | composes | 0.862 | 58 | 48 | 4 | 6 | 0 |
| F35 | mamamoo | composes-with-residue | 0.843 | 51 | 42 | 2 | 7 | 0 |
| none | gameboy | composes-with-residue | 0.797 | 37 | 27 | 5 | 5 | 0 |
| none | Goodboye | composes-with-residue | 0.910 | 78 | 69 | 4 | 5 | 0 |
| none | Madeon | composes-with-residue | 0.662 | 40 | 25 | 3 | 12 | 0 |
| none | pansexual | composes-with-residue | 0.942 | 77 | 72 | 1 | 4 | 0 |
| none | PinkUnion | composes-with-residue | 0.921 | 64 | 55 | 6 | 2 | 1 |
| none | quq | cannot-tell | 0.750 | 21 | 12 | 6 | 2 | 1 |
| none | ReBoot | composes | 0.975 | 20 | 19 | 1 | 0 | 0 |
| none | sakartvelo | cannot-tell | 0.789 | 19 | 13 | 4 | 2 | 0 |
| none | sonicthehedgehog | composes | 0.948 | 106 | 100 | 1 | 5 | 0 |
| none | TeamYellowPlace | composes-with-residue | 0.906 | 64 | 52 | 12 | 0 | 0 |
| none, together | 10 rooms | | 0.860 (mean) | 526 | 444 | 43 | 37 | 2 |

- Each sampled branch holds one room, so a branch's figure is one room's. F30 (simonfraser) is the lowest and F02 (thenetherlands) the highest. The 10 rooms in no branch average 0.860.

**What the figure licenses.** Like the fleet figures of FLEET.md section 2, fidelity bounds whether the written skeleton decides a reader's scoring, not whether the skeleton is right. Each room had one reader, an instance of one model. The test is in-sample: the skeleton was built from the room's own return lines, and the packet held the room's own themes. SCHEMA-adaptations.md section 8 calls it "an in-sample preservation and composition check, not independent truth estimation".

## 4. The causes of a low score, separated

- **The rule**, written before any line was read (`audit-E1/reconstruction_causes.py`). A low score is fidelity below 0.8. That takes 7 rooms: simonfraser, Madeon, picturegame, slovenia, quq, sakartvelo and gameboy. I read every no, partly and unresolved line in them (120), and every no line in the other 23 rooms (80), so that a cause found in the low rooms can be set beside the rest. I gave each line one cause, from the claim, the reader's reason, the packet's skeleton and the room's themes (`audit-E1/reconstruction_causes.tsv`). After the first page, and before any cause was written, I wrote down how two of the causes would be read; the script's docstring holds it.
- **The causes.** *Unsupported*: the coder's claim goes past the room's record. *Evidence*: the record cannot show it, or the skeleton's line on it is absent or not testable. *Particular*: a fact of the room that the coder's account states and no skeleton line carries. *Shared*: the model's element does not hold what the room did, or the model has no element for a kind of act that is not one room's alone. *Reader*: the reader's no or partly is mistaken, or the line is not a claim of the account.

| cause | the 7 rooms below 0.8 (no, partly, unresolved) | the other 23 rooms (no lines) | all |
|---|---|---|---|
| particular | 102 | 65 | 167 |
| evidence | 7 | 6 | 13 |
| reader | 10 | 2 | 12 |
| shared | 0 | 7 | 7 |
| unresolved | 1 | 0 | 1 |
| unsupported | 0 | 0 | 0 |
| all | 120 | 80 | 200 |

Inside particular: detail 44; off the canvas 42; a room named 23; an interval 19; an order 15; a layer 12; the coder's synthesis 6; a line the room proposed 6.

**Fidelity lost in each room below 0.8, by cause** (a no line costs 1 and a partly line 0.5, over yes, partly and no)

| room | fidelity | particular | evidence | reader | unresolved |
|---|---|---|---|---|---|
| simonfraser | 0.637 | 0.353 | 0.010 | 0.000 | 0.000 |
| Madeon | 0.662 | 0.225 | 0.000 | 0.112 | 0.000 |
| picturegame | 0.680 | 0.280 | 0.000 | 0.040 | 0.000 |
| slovenia | 0.735 | 0.265 | 0.000 | 0.000 | 0.000 |
| quq | 0.750 | 0.200 | 0.025 | 0.025 | 0.000 |
| sakartvelo | 0.789 | 0.079 | 0.105 | 0.026 | 0.000 |
| gameboy | 0.797 | 0.176 | 0.027 | 0.000 | 0.000 |

**What each cause holds.**
- **Particulars, 167 of the 200 lines.** The skeleton carries acts by element. It does not carry the room's other business, its counterparts by name, its clock, or the layer that carried an act.
  - *Off the canvas* (42): the room's ordinary traffic before, beside and after the event. Examples are picturegame's numbered game relay, ucf's campus questions, Madeon's trade in concert recordings and gameboy's hardware talk. The coder's account covers the room's whole window; the model covers its organizing for the canvas.
  - *Details, rooms named, intervals, orders and layers*: a counterpart named, a gap the coder measured to the second, which of two threads came first, and whether posts or comments carried an act. simonfraser and slovenia lose most of their fidelity here.
  - *Synthesis and proposed lines*: the coder's reading of the room as a whole, and lines the room proposed at the return that the model did not take, such as Madeon's real concert recordings.
- **Evidence, 13 lines.** The skeleton's line on the act is absent or not testable in the room (P04, P10, P12, P23, P27, P28, P32 and P33, and the arrow A17). In sakartvelo, a room with 5 concepts, evidence carries 0.105 of the 0.211 the room lost.
- **Reader, 12 lines.** None is a fault of the skeleton. The readers of Madeon and quq scored the room's theme list as claims (5 lines). Other readers scored sentences about the coder's evidence, which `RETURN-E1.md` says are not claims (7 lines).
- **Shared, 7 lines: two facts in two rooms.** In mamamoo, members placed pixels at random, without a plan (4 lines of one fact), and the model has no element for placing that organizes nothing. In hyperlightdrifter, a member warned that a rival might attack (3 lines of one fact); P05 holds watching and defence under attack, not the warning. Each is a kind of act, not one room's alone, and so a candidate for a shared change. Neither was tested beyond its room.
- **Unsupported, none found.** I took the coder's claims as the packet gives them and did not test them against the raw record. That test is section 1's: the handler's check found 0.6573 of the case accounts' quoted strings in the room's corpus. Three of the thirty were in its sample (ethoslab, PinkUnion and tagpro), and every quoted string of their accounts was found (15, 13 and 7).

**So no low score here is a failure of the global model.** The low scores come from what the skeleton is not built to carry, from particulars the return did not record, from evidence the record lacks, and from readers who scored lines that are not claims. 7 of the 200 lines point at the shared account, and no line contradicts it.

## 5. What this part cannot say

- Whether a second reader, or a reader of another model, would score the same. Each room had one reader.
- Anything out of sample.
- The causes of the 84 partly lines in the 23 rooms at or above 0.8. I did not read them.
- A branch's fidelity beyond its one sampled room.
- Whether anyone else would give the same causes. They are one analyst's reading, and nobody checked it.

# Audit, section 5: versioned judgments, side by side (E1d)

Written at E1d, 28 October 2026. The figures come from `audit-E1/versioned_judgments.py`, with its rule in its docstring and its output beside it. `audit-E1/reconstruction_tables.py` prints the table.

## 1. The four judgments and their versions

- **The original fixed-global verdict**, from `verdicts-D.jsonl`: the first return, served at pass 15 (model e15f9647…), ruled where the readers split. Over the population: composes 201, composes with residue 489, cannot tell 14, does not compose 1 (section 3).
- **The fixed-global verdict at the re-check**, at the frozen model 46384686…: 630, 56, 19 and 0.
- **The current adapted-local status**, from the effective return manifest (`adaptation-returns.jsonl`, read through `tools/adaptation_ledger.py`). Every one of the 705 rooms has phase recheck, model 46384686…, local status unresolved and grade composes-with-residue. The status is the same in every room, so it cannot set one room against another. Local validation is not established.
- **Shared-branch adequacy**, from `branches-D5.jsonl`: 33 of the 35 branches have shared status unresolved, and F09 and F32 have supported. Every branch line names the global model e15f9647… and the local model 46384686…. Neither supported branch is in the sample.
- **The reconstruction**: fidelity and unresolved claims (section 4), at 46384686…, the version every reader's summary states.

| room | branch | fixed-global, first return | fixed-global, re-check | adapted-local status / grade | shared-branch status | fidelity | unresolved claims |
|---|---|---|---|---|---|---|---|
| picturegame | F25 | does-not-compose | composes-with-residue | unresolved / composes-with-residue | unresolved | 0.680 | 0 |
| sakartvelo | none | cannot-tell | composes | unresolved / composes-with-residue | no branch | 0.789 | 0 |
| quq | none | cannot-tell | composes | unresolved / composes-with-residue | no branch | 0.750 | 1 |
| hunterxhunter | F03 | composes | composes | unresolved / composes-with-residue | unresolved | 0.911 | 0 |
| ethoslab | F01 | composes | composes | unresolved / composes-with-residue | unresolved | 0.932 | 0 |
| python | F26 | composes | composes-with-residue | unresolved / composes-with-residue | unresolved | 0.822 | 1 |
| kirby | F18 | composes | composes | unresolved / composes-with-residue | unresolved | 0.939 | 0 |
| ucf | F15 | composes | composes | unresolved / composes-with-residue | unresolved | 0.896 | 2 |
| penguins | F34 | composes | composes | unresolved / composes-with-residue | unresolved | 0.862 | 0 |
| ReBoot | none | composes | cannot-tell | unresolved / composes-with-residue | no branch | 0.975 | 0 |
| sonicthehedgehog | none | composes | composes | unresolved / composes-with-residue | no branch | 0.948 | 0 |
| mamamoo | F35 | composes-with-residue | composes | unresolved / composes-with-residue | unresolved | 0.843 | 0 |
| superman | F33 | composes-with-residue | composes | unresolved / composes-with-residue | unresolved | 0.927 | 0 |
| physical_removal | F23 | composes-with-residue | composes | unresolved / composes-with-residue | unresolved | 0.930 | 1 |
| thenetherlands | F02 | composes-with-residue | composes | unresolved / composes-with-residue | unresolved | 0.971 | 0 |
| tagpro | F29 | composes-with-residue | composes | unresolved / composes-with-residue | unresolved | 0.906 | 0 |
| gameboy | none | composes-with-residue | composes | unresolved / composes-with-residue | no branch | 0.797 | 0 |
| necrodancer | F28 | composes-with-residue | composes | unresolved / composes-with-residue | unresolved | 0.917 | 0 |
| simonfraser | F30 | composes-with-residue | composes | unresolved / composes-with-residue | unresolved | 0.637 | 0 |
| Goodboye | none | composes-with-residue | composes | unresolved / composes-with-residue | no branch | 0.910 | 0 |
| Madeon | none | composes-with-residue | composes-with-residue | unresolved / composes-with-residue | no branch | 0.662 | 0 |
| dwarffortress | F16 | composes-with-residue | composes | unresolved / composes-with-residue | unresolved | 0.910 | 0 |
| TeamYellowPlace | none | composes-with-residue | composes | unresolved / composes-with-residue | no branch | 0.906 | 0 |
| hyperlightdrifter | F24 | composes-with-residue | composes | unresolved / composes-with-residue | unresolved | 0.940 | 0 |
| puzzleanddragons | F07 | composes-with-residue | composes | unresolved / composes-with-residue | unresolved | 0.959 | 1 |
| seolhyun | F10 | composes-with-residue | composes | unresolved / composes-with-residue | unresolved | 0.925 | 0 |
| pansexual | none | composes-with-residue | composes | unresolved / composes-with-residue | no branch | 0.942 | 0 |
| PinkUnion | none | composes-with-residue | composes | unresolved / composes-with-residue | no branch | 0.921 | 1 |
| mls | F06 | composes-with-residue | composes | unresolved / composes-with-residue | unresolved | 0.891 | 8 |
| slovenia | F08 | composes-with-residue | composes | unresolved / composes-with-residue | unresolved | 0.735 | 0 |

## 2. Where the judgments disagree

- **The rule**, written before the run: a room disagrees where its first-return and re-check verdicts differ, or where it composes at the first return with fidelity below the thirty's median (0.910), or cannot be told or does not compose with fidelity at or above it. The manifest and the branch status mark no room, since they are the same across the sample, and the rule does not use them.
- **25 of the 30 disagree.** 23 changed verdict at the re-check: 18 from composes-with-residue to composes, 2 from cannot-tell to composes, and one each from does-not-compose to composes-with-residue (picturegame), from composes to composes-with-residue (python) and from composes to cannot-tell (ReBoot). ucf and penguins compose with fidelity below the median, and so does python.
- ReBoot, which the re-check could not tell, has the highest fidelity of the thirty, 0.975 over 20 claims. It is outside the seeded sample and was not examined.

## 3. The seeded sample, examined with the case evidence

The seeded five are sakartvelo, picturegame, Goodboye, dwarffortress and necrodancer. In all five the verdict changed at the re-check. For each I read the verdict lines at both returns, and the case account and the skeleton in its packet.

- **sakartvelo** (no branch; cannot-tell, then composes; 0.789). Both first readers could not tell: the room holds 5 concepts, below the floor of 10. At the re-check, one reader found it composing under P27 and P31, the candidates for choosing where to start and for arguing over an occupied spot, and one still could not tell; I ruled that it composes. The case account describes a late, small exchange over where to start a Georgian flag. The skeleton accounts for 13 of its 19 claims, and half the fidelity lost is evidence: P04 and P12 are not testable in the room. **Both judgments hold.** The revised model states what the room did, and the record shows little. The verdict moved with the model, which gained two candidates, not with new evidence about the room. The concept count explains why the first return could not tell. It does not say whether the model fits.
- **picturegame** (F25; does-not-compose, then composes-with-residue; 0.680). Both first readers found a room whose themes are a game of sound rounds, picture hints and emoji proposals, not a canvas mark. Both re-check readers found it composing with residue under K01, P23 and P24, with the sound round and the emoji proposals as the residue. The case account says that the room's sustained conduct was its own April Fools round and its ordinary numbered relay, and that the canvas appears in one emoji proposal. Of its 24 lines read, 8 are the relay and 4 are which layer carried the proposal. **The reconstruction agrees with the first return in substance**: the skeleton holds the room's few canvas acts and not its main business. The change of verdict follows the model's wider frame and its candidates, not more organizing for the canvas.
- **Goodboye** (no branch; composes-with-residue, then composes; 0.910). Both first readers named residue: a guest asking the host's permission to build above its mark, and the mark bringing newcomers back; one added a leader's commands. Both re-check readers found it composing, and named no element for that residue. The skeleton accounts for 69 of 78 claims. Its 5 no lines are two gaps, two orders and ordinary dog sharing, all particulars. **The re-check and the reconstruction agree.**
- **dwarffortress** (F16; composes-with-residue, then composes; 0.910). The readers split at both returns. At the first, I ruled residue: decisions taken in a chat, and canvas events turned into the game's stories. At the re-check, one reader kept the chat as residue because P23 is a candidate with no arrows, and I ruled that it composes, since P23 states the chat. The reconstruction reader scored all 6 claims it placed on P23 as accounted. Its 6 no lines are ordinary game talk (3), P10 not testable (2) and a visitor from another room (1). **The reconstruction agrees with the ruling.** The readers' split is over whether a candidate without arrows composes.
- **necrodancer** (F28; composes-with-residue, then composes; 0.917). The readers split at both returns. At the re-check I ruled that the residue of my first ruling, a visitor answered and editing sent to a chat, is now P25 and P23, and that the move ahead of a neighbour's announced taskbar is P27. The one no line of the reconstruction is the answer to a visitor's criticism of the game's music (claim 26). The room's line on P25 holds a member explaining the game's genre to a passer-by [necrodancer/c0069], not that answer. **The judgments differ in grain.** My ruling read the theme t08 as P25 and named c0067. The reconstruction reads the claim, and the room's line on P25 cites another concept.

**What the five show.** In all five the verdict moved with the model at D3, as candidates entered, and not with new evidence about the room. The reconstruction agrees with the re-check where the room's record is mostly its work for the canvas (Goodboye, dwarffortress and necrodancer, 0.910 to 0.917). It agrees with the first return's doubt where the record is small or lies mostly off the canvas (sakartvelo and picturegame).

## 4. What this part cannot say

- Room by room, whether the local adaptations hold. The adapted-local status is the same in all 705 rooms, so it says nothing about any one of them.
- Whether a shared branch is adequate for its sampled room. Every sampled branch is unresolved.
- Why the 20 disagreeing rooms outside the seeded five disagree. I did not examine them.

# The composition result (E1d)

Written at E1d, 28 October 2026, after the reconstruction's check. It reads the audit's sections 3, 4 and 5 against `prior.md` section 3, the composition criteria fixed before the scheme.

composition_status: unresolved

- **Level.** The method question's, read at each of `prior.md` section 3's three levels. At the population level, composition is supported. At the level of the forms and subforms, the population compiles rather than composes, in Kozlowski and Klein's sense, and shared adequacy is met by 2 of 35 branches. At the leaf, the shared account holds in the reconstruction, but local adequacy is not established.
- **Scope.** The frozen model 46384686…, without the two held proposals, in-sample throughout. The population level covers the 705 rooms of the re-check, in the return's own terms. The leaf covers the 30 rooms of the reconstruction, each scored once by one reader of one model. Nothing here was held out.
- **Why the whole is unresolved.** `prior.md` section 3 makes two criteria the grounds: local adequacy, each room accounted for by the model plus validated adaptations, and shared adequacy, clusters that explain their members jointly through a stated condition. Neither is established. The validated half of the local measure was not computed, and the effective manifest gives every room local status unresolved. 33 of the 35 branches have shared status unresolved. The same section forbids calling exact local fit evidence of global composition by itself, so the reconstruction's fidelity cannot settle the whole. None of the failure conditions is met either: no adequately observed room needs only unrelated particulars, and no claim of the model meets contrary validated local evidence. An insufficient record yields uncertainty, not demonstrated failure.

**The evidence, level by level.**
- **The population: supported.** At the re-check the frozen model composes in 630 of 705 rooms and with residue in 56, and in none does it fail to compose. The expectations score 0.924, in-sample. The mechanism is the spine: a member starts a mark, the room calls for hands, builds and keeps it, and keeping holds the known form. Its order counts beat their nulls (`claims-E1.md`). The case that best supports it is day9, and the case that most threatens it is thebluecorner, where a faith, not the work, decides whom the room fights.
- **The forms and subforms: compiled, unresolved.** The 223 distinct shared changes gather into 35 branches that overlap as facets, and the curve of distinct changes flattens over the last third of the seeded order, which is the section's sign of limited branching. Only F09 (rooms rebuild after moving) and F32 (rooms keep after marking) explain their members jointly. The share of rooms carrying a particular that touches the model's top elements was not counted.
- **The leaf: the shared account holds; local adequacy is not established.** The skeleton, the global model with each room's effective lines, accounts for the coder's account with fidelity 0.871 (0.637 to 0.975) over 1,788 claims. No claim contradicts it. Of the 200 lines read for the causes of a loss, 167 are particulars the skeleton does not carry, 13 are evidence the record lacks, 12 are readers' errors, and 7 point at the shared account (two facts, in mamamoo and hyperlightdrifter). The leaf's limit is the room's own history: its counterparts by name, its intervals and orders, and its business off the canvas. `prior.md` section 3 rests a particular history on a dated sequence of the room's own turns that the model's elements reach. The elements reach the acts, and the skeleton does not carry their dating.

**Kept apart, as the stage asks.** The original fixed-global verdicts (201, 489, 14 and 1 at the first return, model e15f9647…) stand beside the re-check's (630, 56, 19 and 0, model 46384686…), the current adapted-local status (unresolved and composes-with-residue in all 705 rooms) and shared-branch adequacy (2 branches supported, 33 unresolved). The D6 proposals stay unvalidated against the unchanged D3 model (part 3 of section 1).

**The held proposals (QD4-001; never served, not re-checked).** The model reported here is 46384686… without them.
- **P05** (move 198, history lines 173 to 176; reverted by move 203, line 181). The statement would gain: "This holds where the keepers can learn of a planned change only by being told, and no informed member holds it." Status bounded. The bound names completeanarchy, polska, satania, halo, bangtan and thesilphroad (the keepers read the change from its shape) and armok, maryland and oneshot (informed members hold it), with their nine re-check lines.
- **A11** (move 199, history lines 177 to 180; reverted by move 203, line 182). The arrow from P02 to P04 would be withdrawn under rule 14. It never beat its null. Template first (98 rooms) is nearly as common as the transition (111). The failure clause stands alone in 117 rooms, 31 of them talk only. 261 accepted restrict lines say that a template does not settle the design for good.

# Audit, sections 6 and 7: what bore the load, and what the study cannot say (E1b-08)

Written at E1b-08, 27 October 2026. The figures come from `audit-E1/load_limits.py` and `audit-E1/shelf_terms.py`, each with its output beside it, and from E1a's and the earlier legs' outputs.

## 1. Which stage was load-bearing

**By stage.**
- Every stage from A1 to D6 has outputs that a later stage names in its commands or reads:

| stage | outputs named later | outputs | stage | outputs named later | outputs |
|---|---|---|---|---|---|
| A1 | 13 | 20 | C4 | 6 | 10 |
| B1 | 15 | 25 | C5 | 13 | 74 |
| B2 | 18 | 61 | D1 | 54 | 722 |
| B3 | 11 | 1,266 | D2 | 4 | 7 |
| B4 | 10 | 146 | D3 | 4 | 23 |
| C1 | 6 | 16 | D4 | 20 | 70 |
| C2 | 15 | 37 | D5 | 11 | 48 |
| C3 | 4 | 9 | D6 | 7 | 271 |

- So every stage was load-bearing for something downstream, and no stage is the one whose output nothing read.
- The files no later stage names are mostly fleet packets, superseded copies, answers, notes and handbacks. Fleets, tools or the harness read these without naming them in a command, so this test cannot call them unread.
- By hand, some look read by nothing: `lexicon-A1.md`, `leads-outside-frame-A1.jsonl`, `ideas-B1.jsonl`, `kinds-B1.jsonl`, `form_pass-C1.md`, `gate_history.jsonl`, `within_case.md`, `sketches.md` and `author_claims.jsonl`.
- These were not checked against every tool's inputs. They are listed as candidates for a file nothing read, a defect in this instrument (`defects.jsonl` line 120, not sure).

**The three files given for this test.**
- **`tools/chunk_compare.py`.** Its sha256 now equals the receipt in `departures.jsonl` (chunk-comparison-v1.1, `c8d2eb8c7c309c02…`), and its outputs are present (`chunk-share-D4.jsonl` and `.md`, `projections-D4.jsonl`). A stranger can rerun it. I did not.
- **The data-structure view.** It moved between C2's last snap (`57f68644867d`) and C5's (`c4a4c4884570`), and it is unchanged since. `data_structure-C5.md` is present. The C5 passes, which rewrote the declarations under the prose rule, moved it.
- **`account_passes.jsonl`.** It holds 15 passes, so the account's loop ran.

**The model's tiers: do the dimensions do any work?**
- **Where they work:** the dimensions sort the elements (44 lines of `model/elements.jsonl` name one). They state the propositions' levels (14 times by name in `propositions.jsonl`). They order D6's retelling (`retelling-D6.md`, by its parts). They weigh 1.0 in D4's distance.
- **Where they do not:** they appear in no line of `branches.jsonl`, `branches-D5.jsonl` or `model/arrows.jsonl`, and nowhere in `account.md`, by id or by name.
- So the dimension tier works in the model's layout and in the retelling, but does no work in the account's argument, the arrows or the branches' keys. Read alone, it looks sound. Read with the stages, it is the tier the account never uses.

## 2. What the study cannot say, in one place

- **Absence claims marked weak:** F-015 (the rooms do not read their numbers off the replies to a call).
- **Looked for and not found**, stated as results:
  - no loop passed the one-room test;
  - A11's order never beat its null, and A12 has no order count;
  - the held-size test of the arrows, declared in `prior.md` section 3, was not run;
  - the onset contrast cannot be read, since each arrow's late side holds 0 to 15 rooms;
  - the "dear enemy" and superordinate-goal predictions were declined, because no query recovers their targets (`literature-C3.md` lines 84 and 89).
- **Relationships weaker than the rest of the model:** two arrows are theorised (A11, A12), four are thin (A05, A10, A14, A19) and two are partly constitutive (A16, A20). A21 is the one arrow no proposition rests on.
- **The coders' disagreements:** 72 lines in `coder_conflicts.jsonl`. Which reading each affected claim rests on, with both quotes, was not read line by line at this leg. That is a limit.
- **Third-order themes the model does not use:** 35 of 195 are reached by no standing element.
- **What C1's form pass found that no tier could hold**, four kinds:
  - April Fools play that stages no fake (17 lines in 15 rooms);
  - another sub's April Fools change seen from this room (8 in 8);
  - the sub's own moderation outside the canvas (8 in 7);
  - disputes over the room's own jokes (4 in 4).
- **Stage C3's remainder:** 19 themes, covering talk in 694 rooms.
- **Whether any room's problems were settled:** only the room models speak to it, and nothing measures it.
- **What a group leaves behind:** the contract's section 1 question has no measure. The canvas is what the drawing left behind, and the instrument does not know whether the room went on.

**The standing departures of this design**, beside the run's own:
- **Five tiers** rather than three.
- **The fourth-order tier cut at C1**, before the loop. B1 made 197 third-order themes, C1 kept 195 inside fourth-order themes, and C2 to C5 wrote 8 third-order tier lines, merges and splits.
- **Literature after the model.**
- **A scheme frozen at B2**, before B3 (part 2 of the audit).
- **The frame:** 705 coded rooms against a target census of 706, with no drops. `leads-outside-frame-A1.jsonl` names 2 rooms outside it.
- **The canvas held from the start**, never scored against.
- **One analyst above the assignment tier**, seen by the hostile reader at C2, the three readers at C5, the labelers and the return's readers. There were no forks, and the room notes are the one input nothing checks.
- **No human check at any tier**, beyond J's rulings.
- **No theoretical sampling.** What stood in: the census, and 67 distinct rooms read against the stories.
- **Saturation** as 5 story passes and 2.51 new kinds per hundred themes.
- **Replication as the in-sample return.**

**The critique shelf.** I read the four read-tier files after the findings were fixed: Jowsey et al. (2025) and the call for papers whole, and O'Sullivan and Ravasi (2026) and Schildt (2026) by the objections' terms with their pages.

| objection | the shelf | does this run answer it? |
|---|---|---|
| invented quotes | O'Sullivan and Ravasi, p. 16; Schildt, pp. 1, 4 | **In large part.** 3,218 of 3,230 cited quotes resolve to their concept. The handler's raw check finds every coder quote in its item, and none of the case-account strings I could check is an invention. 33 strings from uncoded items stay unchecked (part 1). |
| the reasoning handed to the machine (cognitive offloading) | Schildt, p. 1; O'Sullivan and Ravasi, p. 2 | **No.** The design hands every tier above the coders to a model, and J's rulings are the only human steer. The run shows its reasoning; it does not keep a human doing it. |
| an opaque process | O'Sullivan and Ravasi, p. 17; Schildt, p. 1 | **For the record of decisions, yes.** Every move is snapped, every diary line drawn is borne out by its transcript (905 of 905), and every script states its rule. **For the reasons inside a model's judgment, no.** |
| the craft and reflexivity a model does not have | Jowsey et al., pp. 1 and 2; O'Sullivan and Ravasi, p. 13; Schildt, p. 14 | **No.** No positioned human researcher read the rooms. The experience file will be a model's account of itself. |
| more output instead of better | the call, p. 1; Schildt, pp. 1 and 2 | **No.** The run wrote thousands of files. The audit found the account at 3,326 words, not one to two pages, and 293 handback counts unchecked. |
| harm to the environment and to data workers | Jowsey et al., p. 2 | **Not addressed.** |

**The call for papers' asks**, for section 8, without changing a finding:
- **Met in kind:** an AI-enabled research loop under human direction; qualitative theory-building with a stated test; boundary-setting work, which this audit is.
- **Partly met:** reproducibility, since scripts declare their rules, but no rerun is promised. A repository-like artifact also exists, since `out/` holds every file.
- **Not met:** ethicality, as the call frames it, is not examined.

**The one thing to say plainly.**
- **What the study produced:** a **model**, the frozen spine and its arrows, with a **typology** below it (six room forms over 35 facet branches). It set out to produce a model.
- **The strongest argument that the partition is size as form** (contract section 5): D4's volume verdict. The cluster labels explain 0.255 of the variance in log concepts, at the 100th percentile of the permutation null (null maximum 0.026). The branches lean to large rooms.
- **What answers it, in part:** D6's size-matched test, under which 62 of the forms' 72 changed cells survive. I did not locate stage D4's line-count division at this leg.
- **What would overturn the study:** the re-check composes 686 of 705 rooms (0.973). If 4 or more of a stratified sample of 30 uncoded rooms did not compose (6 or more of 60), the uncoded rooms would fall outside the coded rate at the 1 per cent level.
- **What I could not answer:**
  - whether the forms survive outside the sample;
  - the coders' disagreements, read one by one;
  - D4's line-count division;
  - the leaf, which is the reconstruction's test.

## 3. Defects named at this leg

One line was appended to `defects.jsonl` (line 120, stage E1, leg E1b-08, not sure): the files that no later stage names and that look read by nothing.

# The methods paragraph (stage E1 section 8)

We follow Gioia, Corley and Hamilton for stages A1 to D3, with five tiers and the loop. One coder instrument, run once per community by a reader sealed from every other, wrote the first two tiers for 705 rooms: 115,388 first-order concepts in the participants' words, 7,844 second-order themes and a case account per room. The audit did not establish the coders' model. One analyst, a Claude model (claude-opus-5-5), built every tier above them. It made 197 third-order themes at B1, kept 195 inside fourth-order themes at C1, and built the dimensions and the model with its arrows. It also ruled every split of the readers. Fleets of readers in fresh contexts checked the written instrument: deepseek-v4-flash and deepseek-v4.1-flash readers at B2 and B3, two arms at B4, a claude-opus-5-5 hostile reader at C2 and claude-opus-5-5 readers at C5, labelers at D2, gpt-6.1-sol readers at the D3 re-check, and deepseek-v4.1-flash readers at E1. Readers of one model are instances of it, not separate minds, and they are critics, never judges. In Shrestha, He, Puranam and von Krogh's terms, the coder tier and the fleets detect patterns and the analyst abducts. We cite Grodal, Anteby and Holm for the record of the categorization moves, each snapped from C2 on, and not for replicability.

The design departs from the method in four ways. First, the tiers are split between coders and analyst: the analyst coded no room, and the coders compared none. Second, there is no overlap between the coders' collection and the analysis: the analyst read the rooms only through the coders' store. Third, a census stands in place of sampling: 705 coded rooms against a target census of 706, with no drops. What stood in for theoretical sampling was sampling inside the corpus at C2 and the return to every room at D1 to D3. Fourth, the return is in-sample. It follows Eisenhardt's replication logic and is never a hold-out test. It is in-sample at the tier the model was built from, the coders' second-order themes. The expectations' replication score of 0.924 and the reconstruction's fidelity of 0.871 over 30 rooms are in-sample throughout.

The taxonomy classifies rooms by shared changes to the model: 223 distinct shared changes, gathered into 35 branches. The branches are a similarity hierarchy with no claim of descent, and the chunk-share tree is kept as the theory-free comparison. The canvas is what the drawing left behind at the last hour of a 97-hour event. It is not a measure of skill or intent, and the instrument has no measure of whether a room went on. I held every room's canvas outcome while building, and the record declares its use at A1 (each room's made line), at D4 (projected after the snapped cuts) and at D5 (`survival-D5.md`, read after the record). The store and `cite.py` serve the coded record only. The run's one touch of the raw record is the handler's quote check over 80 rooms: it found every coder quote in its item (a share of 1.000) and 0.6573 of the case accounts' quoted strings in the room's corpus. Every prompt, input, output, transcript and model identifier is archived, so any claim can be traced to its source. The study does not promise that a rerun reproduces it.
