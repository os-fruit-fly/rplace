# Handback, stage D2: the return, checked

Leg D2a, 16 October 2026. The labelers returned all 705 rooms and the verdict fleet returned two readers for each, against the model frozen at pass 15 (e15f96470271763d9913e79ed8e332c164a1f176106eefacfe8ffac8e1b3fecd). I checked what `ingest.py D` compiled. I ruled on nothing, edited no return, and re-ran no labeler or reader. The detail and the scripts are in `notes-D2.md`.

## The return value

| What | Count |
|---|---|
| Rooms returned and accepted | 705 |
| Rooms reissued (`RUN.json`) | 0. Every `run.json` records one attempt; the handler's recap reports same-session repairs in 378 rooms |
| Rooms unreturned | 0 |
| Lines accepted | 42,243 |
| Lines flagged, by rule | portability (rule 5): 763. Rules 1 to 4 and 6 reject a room whole, and no room was rejected |
| Lines per room | min 21, median 60, p90 68, max 91 |
| Ops | instantiate 17,648; absent 14,675; restrict 4,406; add-step 1,889; add-condition 1,408; propose 1,362; link 844; contradict 11 |
| Ops by kind (as ingest stamps them) | specification 32,323; correction 4,417; elaboration 4,141; proposal 1,362 |
| Absent lines by evidence | evidenced 67 (observed-absent 36, not-needed 31); evidence limits 14,608 (unobserved 7,806, not-testable 6,802) |
| `none` rooms | 0 |
| Non-portable share | 1.81% of lines (763), in 356 rooms |
| Unplaced-source share | 0.5% of sourced lines (134 of 27,571), 0.3% of all lines, in 98 rooms |
| Reader verdicts (1,410) | composes-with-residue 927; composes 432; cannot-tell 49; does-not-compose 2 |
| Room verdicts | agreed in 542 rooms (with-residue 387, composes 140, cannot-tell 14, does-not-compose 1); split in 163 |
| Disagreement rate | 23.1% of rooms: composes against with-residue 142; cannot-tell against with-residue 11; cannot-tell against composes 10 |
| Cannot-tell, by threshold | coded-share 39; off-platform 10; both 0. All 49 supported by the room's numbers; none listed as unsupported |
| Labelers' model (manifest) | `gpt-6.1-sol` in all 705 rooms, resumed with `gpt-5.6-sol`, at medium effort (the recap) |
| Readers' model (manifest) | `deepseek/deepseek-v4.1-flash`, verified, medium effort, two per room |

**The labeler's grade against the fleet's verdict:**

| labeler grade | composes | composes-with-residue | does-not-compose | cannot-tell | split |
|---|---|---|---|---|---|
| composes-with-residue | 140 | 387 | 1 | 14 | 163 |

The disagreement rate bounds whether the written criterion decides a room, not whether the model is right.

## Defects for the operator

I edited none of these mid-return.

1. **The labeler's grade does not vary (task template and return specification).**
   - All 705 `model-D.md` files grade composes-with-residue, and all 705 say `local_status: unresolved`.
   - **The cause:** `RETURN-D.md` asks the labeler not to assert exact fit while evidence remains unresolved, and to list each unresolved claim. Every room's record leaves some element unobserved, so `composes` and `validated` are out of reach.
   - **The effect:** the cross-table of grade against verdict has one row, so E1 cannot use it. The grade's sentence often reads as a formula.
   - **What would make the grade vary:** separate the claims the room bears on from the elements its record cannot show, and grade fit on the first.
2. **Ingest stamps every absent line as specification.**
   - `SCHEMA` §2 counts only `observed-absent` and `not-needed` as evidenced. `unobserved` and `not-testable` support neither specification nor correction.
   - 14,608 of the 14,675 absent lines mark limits of the evidence. `ingest-D.md`'s kind counts therefore overstate evidenced specification by those lines.
   - D3 and E1 should split absent lines by `observation`.
3. **The repairs are not in the run's record.**
   - `RUN.json` says 0 rooms reissued, because ingest counts attempts above one, and every `run.json` records one attempt.
   - The handler's recap reports one to four same-session repairs in 378 rooms. No file this stage may read records them, or the rules they fixed. So ingest's flags cover only portability.
   - D4's reconciliation should know the repairs exist.
4. **The verdict return line (`RETURN-D2v`).**
   - **`served`:** it asks the reader to copy a value the packet states. 1,409 of 1,410 lines copied it exactly; one (ducks, r1) dropped two characters, and 24 of the 32 invalid attempts lacked the field. `fleet.py`'s meta files hold the packet's digest independently, so `served` records copying, not what was served.
   - **`sub`:** 225 reader lines wrote the room's name another way, 24 of them as another name. No verdict changed rooms, because ingest takes the room from the dispatch folder.
   - **No count:** the line carries no concept count or pointer count, though contract §5 says every verdict carries the count. My check used the figures in `rooms.jsonl`, which each packet stated.
5. **`[new: …]` is used for more than organizing (task template, minor).**
   - The template does not limit `[new: …]` to organizing that no element covers.
   - In the sample, most markers name such practices. Others name conduct that is not organizing (replying to a bot, sympathy in a joke thread), serve as a residue tag, or once repeat a theme the vocabulary holds (T3-017).

6. **A dimension as the element outside `link` (QD2-001, answered; the check is repaired).**
   - 121 ledger lines name a dimension as their element. 113 are `link`, which SCHEMA §3 allows.
   - Eight are restrict, add-condition or add-step lines: 4chan-013, SquareSpiral-014, borussiadortmund-013, cowchop-030, spain-058, torontoraptors-009, ucf-004 and vermont-011.
   - `ingest.py`'s rule 2 (line 186) accepts a dimension for any op. The stage check (`stage_D2.py`, line 273) accepts one only for `link`. So `validate.py D2` fails on these eight lines alone.
   - I may not edit a return or re-run ingest. I asked the PI whether the check should accept them, so that D3 rules on them as they stand, or whether ingest should be tightened and the eight rooms returned to their labelers.
   - **J's answer (option 1):** the check accepts a dimension for these ops, and D3 rules on the eight lines as they stand. The handler changed `stage_D2.py`; I changed no line, tool or return.
   - `ingest.py`'s rule 2 still admits a dimension for every op, including instantiate, absent and contradict. The operator may want ingest and the check to name the same ops.

## For D3: facts, not rulings

- **The split rooms.** All 163 are listed in `notes-D2.md`, by pair. D3 rules on each with the criterion in front of it.
- **Picturegame,** a guessing-game sub, is the only room both readers judged does-not-compose.
- **Candidates and tentative entries.** These rooms hold a line other than absent on each entry:

  | entry | status | rooms |
  |---|---|---|
  | P06 | candidate | 564 |
  | K04 | candidate | 530 |
  | R02 | candidate | 500 |
  | P19 | candidate | 240 |
  | K03 | candidate | 124 |
  | P22 | tentative | 191 |
  | P21 | tentative | 128 |
  | A21 | tentative | 101 |

  The labelers name the candidates as candidates.
- **The sample of ten room models** (seed 20261016, stratified on the room verdict).
  - **Every file** follows the dimensions, cites a resolving concept on every claim, and names every adapted element.
  - **The prose** reads as the room's organizing in the model's words.
  - **Recurring changes:** five labelers restrict A11 (a posted template did not settle the design). Four fold the start and the call into one act (A02). Four make restraint (A05) depend on something other than an agreement.
- **The story-miss rooms by room verdict:** composes-with-residue 14, composes 4, split 1.
- **Contradict:** 11 lines (P13 5, P10 3, A10, A04 and A07 one each).

## What I did not do

- I read the ledger by count and through the views, never as a list.
- I did not read `EXPECTATIONS.jsonl`.
- In `DROPS/D/` I read `DONE` and `UNRETURNED.tsv`, and I listed the folder's room names once.

## Slips

- **A miscounted figure.** I first wrote the story-miss rooms judged composes-with-residue as 13, from reading a printed list rather than a count. A script gives 14, and the notes and this handback carry 14; the correction is logged.
- **A wrong comparison, corrected before anything was written.** My first comparison of `served` used the packet file's hash rather than the value the packet states. I found the cause, fixed the script, and reported the corrected count.
