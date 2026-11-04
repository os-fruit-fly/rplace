# Handback, stage E1: the audit

Written at E1e, 28 October 2026. Every figure comes from a script in `audit-E1/`, with its output beside it, or from a part of `audit-E1.md`, which names its script. The experience is `experience-E1.md`. Its hash and model are the last line of `run_manifest.json`.

## The claim

**Whether the model composed, in the pre-registered terms: unresolved** (`composition_status: unresolved`, `audit-E1.md`, the composition result).
- **The population: supported.** At the re-check the frozen model 46384686… composes in 630 of 705 rooms, composes with residue in 56, and fails in none. The expectations score 0.924, in-sample.
- **The forms and subforms: compiled**, in Kozlowski and Klein's sense. Shared adequacy is met by 2 of the 35 branches (F09, F32).
- **The leaf: the shared account holds, but local adequacy is not established.** Reconstruction fidelity is 0.871 over 30 rooms, and no claim is contradicted. Of the 200 lines read for the causes of a loss, 7 point at the shared account. The validated half of `prior.md` section 3's local measure was never computed, and the effective manifest gives every room local status unresolved.
- `prior.md` section 3 rests composition on local and shared adequacy, and bars calling local fit evidence of global composition by itself. Neither ground is established, and no failure condition is met. So the whole is unresolved.

**The room that best supports it: day9.** It offers a neighbour terms before any damage, loses its border at hour 48, moves within two hours, and finishes the new work at hour 53.

**The room that most threatens it: thebluecorner.** It is a colour faction whose faith names its rivals and rules on guests.

**The condition between them** is what decides whom a room fights and whom it admits. Where the work decides, the model tells the room. Where a faith or a host's rule decides, it does not. At the leaf, the condition is whether the room's record is its work for the canvas: ReBoot (0.975) and thenetherlands (0.971) are reconstructed most fully, and simonfraser (0.637) least, through its counterparts, intervals and layers rather than through the shared account.

## Every section's counts

- **Coverage by stage** (`audit-E1.md`, section 1, part 2). All 705 rooms were read by `mem.py room`, 705 through the forest (704 whole), 705 through the case account, and all 705 cited.
  - A1: 1,936 room reads over 705 rooms, the forest for 155, the case account 887 times over 705.
  - B1: 1,873 room reads (705), the forest for 110 rooms.
  - C2: 343 room reads (67), the forest for 67.
  - C5: 261 room reads (218).
  - D3: the forest 14,054 times over 703 rooms, and 77,047 cite reads over 705.
  - B2 to B4, D1 and D4 read no room through these verbs; their reading is the fleets'.
- **Orderings.** All held, broken none.
  - The scheme was frozen before B3's first batch.
  - `prior.md` sections 1 to 6 were sealed before B1's first theme, rebuilt byte for byte from the transcripts.
  - Sections 7 and 8 were sealed at D1, before `DROPS/D/` was ingested.
  - The model was hashed at C5's close before D1, and moved at D3 by declared amendments.
  - The D4 branch cuts were snapped before the projection; the room forms came after, by J's ruling (QE1-001).
  - Every move snap at C2 to D3 is present.
  - The D6 proposals stand unvalidated.
- **Probe failures** (`probes-E1.md`). 300 answer files; as filed, `probe.py` read 17. Re-read by its own rules:
  - goal right 298, wrong 2;
  - open 26 and 135;
  - rooms 48 and 125;
  - changed 50 and 13;
  - next 11 and 12;
  - n/a 780, apart.
  
  Of the wrong answers, 269 are notes, since the head, the diary or the questions held the answer, and 18 are defects.
- **The composition diagnostics.**
  - Fixed-global verdicts: 201, 489, 14 and 1 at the first return, and 630, 56, 19 and 0 at the re-check.
  - Particulars: 2,749 lines in 545 rooms.
  - Distinct shared changes: 223. Their curve in A1's seeded order runs 184, 211 and 223 by thirds, and flattens.
  - Element reach: 4,759 of 5,380 themes with a coordinating turn (88.46 per cent); 297 of 696 rooms in full.
  - Local validation: not established.
- **The replication score:** 0.924, in-sample (8,034 met of 8,696 met or failed; 944 untested), by branch and by verdict in `expectations-E1.md`.
- **The contrast:** untested. Each arrow's late side holds 0 to 15 rooms, so by rule 6 no gap is read.
- **Reconstruction fidelity.**
  - By verdict: composes 0.911 (8 rooms), composes with residue 0.875 (19), cannot tell 0.770 (2), does not compose 0.680 (1).
  - By branch: 20 branches of one room each, from 0.637 (F30) to 0.971 (F02); 10 rooms in no branch, 0.860.
  - All rooms: 0.871 over 1,788 claims; 15 unresolved, 0 contradicted.
- **The cross-table's disagreements:** 25 of the 30 rooms. 23 changed verdict at the re-check; ucf, penguins and python compose with fidelity below the median. In the seeded five, the verdict moved with the model, not with new evidence about the room.
- **Departures and defects, by kind.**
  - Departures: 21 lines (A1 9, D4 7, D5 2, D6 3). 18 state no cost, and 2 were acted on before they were written.
  - Defects: 125 lines (A1 8, B3 55, D5 38, E1 24). At E1b-06's sorting, the material's were A1 6, D5 9 and E1 2, and the rest the instrument's.
  - E1's 24 lines by their labels: the instrument's 19, the material's 2, mine 2 (lines 123 and 124), and one line of provenance.
- **Forks:** none arrived, so the spread is none.
- **The stage nothing used:** none. Every stage from A1 to D6 has outputs a later stage names. Nine files look read by nothing (`defects.jsonl` line 120, not sure). The dimension tier does no work in the account, the arrows or the branches.
- **What the study produced:** a model, with a typology below it (six room forms over 35 facet branches). It set out to produce a model.
- **The association I trust least: A11**, design settled by a template (P02 to P04). It never beat its null. Template first (98 rooms) is nearly as common as the transition (111), and 261 accepted restrict lines say that a template does not settle the design for good. Its withdrawal is held, not served.
- **Five changes, one line each:**
  1. Hold rooms out before building, so that the return and the reconstruction can test out of sample.
  2. Compute local adequacy inside the return, so that `prior.md` section 3 can be decided.
  3. Let the return contradict as easily as it restricts, and put a second ruler on a seeded share of the splits.
  4. Cut tiers and files no downstream reader names; the dimension tier did no work.
  5. Build every packet and its return specification from one source, and dry-run one before each dispatch.

## The licences

**The four of METHOD.md.**
- *The in-sample return*: exercised at E1, in the expectations' score and the reconstruction, each called in-sample wherever it is reported.
- *Gioia's explosion at the front end*, *Langley's strategy* and *the count set by kinds*: not exercised at E1, which builds nothing.
- Across the run, the handbacks record:
  - Langley's strategy exercised in part at C2, C3, C5 and D3, as temporal bracketing at D5b, and not at D4;
  - the count set by kinds exercised at C2 and C5, and not at C3;
  - the explosion exercised at C5, and not at C2 or C3.

**E1's own**, each in `notes-E1.md`:
- arrows counted as taken up by any accepted line (E1b-07);
- two shelf files searched by terms, not read whole, and files named read by nothing from their names (E1b-08);
- the validation rule amended after its first run to read a room written as "r/" with its name;
- two causes clarified after the first page;
- the coders' claims read as given;
- earlier parts superseded by listed replacements;
- `unresolved` chosen for the composition line (E1d).

**Never exercised at E1:** a recut, a dropped room, a re-dispatch, a change to any earlier stage's file.

## What I did not do as the stage file says

- **The heads in order.** Only `_head.md` is on file. Each leg rewrote it in place, and the snaps keep hashes, not text.
- **The coders' disagreements.** I did not read the 72 lines of `coder_conflicts.jsonl` one by one with both quotes.
- **D4's line-count division.** Not located.
- **293 handback counts.** Not checked.
- **What following each of the 18 uncosted departures would have cost.** Not written.
- **The held-size test of the arrows,** declared in `prior.md`. Not run.
- **The share of rooms carrying a particular that touches the model's top elements.** Not counted.
- **At the reconstruction:** the 84 partly lines of the 23 rooms above 0.8 were not read; the coders' claims were not tested against the raw record; the causes are my reading alone.

## What is wrong with the instrument, or unclear

- **The packet trailer and the return specification disagree** (line 121). The packet asks for an end marker the specification does not name, and all 30 returns failed `fleet.py` for it.
- **The return specification does not say how to write the room** (line 122).
- **The E1 check's id pattern** reads members' words such as a console's name, and a gate rule's number, as model ids. It also bars two words even in the sentence that says no figure is either (line 123).
- **The E1 dispatch and the D3 re-check wrote no manifest entry** (line 125). I appended the E1 fleet's entry at E1e from `arm.json` and `DONE`. The arm file records no temperature or top_p.
- **`probe.py` cannot read answers written in bold markdown:** 283 of 300.
- **`run_manifest.json` is one JSON list,** so "the last manifest line" means rewriting the whole file. I kept the list as it stood (`audit-E1/run_manifest.before-E1e.json`) and copied the new list over it.
- **The PI's message at E1d named the readers' route "direct"; `arm.json` names the gateway.** I wrote "called directly" in the audit from the message, and corrected it at E1e (line 124).

## Slips at E1

- **E1b-03 and E1b-07:** two Edits to one file in one turn.
- **E1b-07:** two glosses beyond what I had checked, cut before the checks.
- **E1b-08 and E1d:** a read piped through `cut` was refused by the guard, and re-run whole.
- **E1d:** two figures typed into the diary before the check (12, not 11; 23, not 24), corrected in the diary. The first assembly of `audit-E1.md` failed the check on wording in three earlier parts. The readers' route was taken from a message rather than from the dispatch's record.
- **E1e:** four phrases of the experience went past the record. Each was corrected, one Edit per turn, before the file was hashed.

## For stage E2

- **The handling is on record.**
  - 53 answers are in `out/_answers/`.
  - Four were the handler's, under J's delegation or as the handler's view J had not seen: QC1-003, QC2-001, QD6-001 and QD6-002.
  - J's rulings carried in the head are listed in `experience-E1.md`, section 11.
  - The guard's refusals are in the diary and the handbacks' slips.
- **The run's size:** 315 legs, 154,504,719 output tokens, 25,543 diary lines, and at least 157 compactions (`audit-E1/experience_facts.json`). D3 alone wrote more than a third of the output.
- **The E1 dispatch.** It failed on a mismatch between the tool's trailer and my specification. The PI chose validation over a re-dispatch, and the returns were complete. That episode belongs in the audit of how I was handled.
- **Still open from earlier stages:**
  - `defects.jsonl` lines 100 and 101: the survival paragraph's field, and four timings the canvas contradicts;
  - the held proposals P05 and A11;
  - the paladins and portugal proposal;
  - the colour-faction doubt.
