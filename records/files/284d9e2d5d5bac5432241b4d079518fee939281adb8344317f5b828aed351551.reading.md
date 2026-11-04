# Handback, stage D5, the room forms (D5a-36 to D5a-41): a supplement to `handback-D5.md`

Written at D5a-41, 27 October 2026. `handback-D5.md` was written at D5b and covers the 35 branch accounts, the waterfall and survival; it stands unchanged. On J's word through the PI (`departures.jsonl` line 17), D5 ran once more, one account per room form of the six-form cut J ruled at D4a-08. The six accounts are `room-form-A-account.md` to `room-form-F-account.md`, beside the room-forms files and not in `forms/` (line 18); their lines are in `room-forms-D5.jsonl` (6 lines: 705 rooms, 558 of them defining). The notes for the next stage are the six D5a-36 to D5a-41 sections of `notes-D5.md`, the last of which lists the six forms together.

## The claim

The six forms are poles of a continuum, not kinds: the cut's stability on matched subsamples is about 0.21. Each gathers rooms by the part of the model they changed most, and in each the rooms' lines say that the model's order runs differently there.
- **A, the terms between neighbours, with the plan announced** (166 rooms). Rooms make terms at the border, and terms and plans bind only the placers they reach. A form in a weak sense.
- **B, the work behind the thread** (141). The chat, the scripts and raiding, held by different rooms at about chance. A grouping, not a form.
- **C, the design and its marking** (125). The design is settled for a time and reopened, and informed keepers refuse changes. A form in a narrow sense.
- **D, keeping, with traded help and carrying on** (119). Keeping is shared and checked; help is sent from surplus or owed; carrying on begins before the close and returns to the call. A form in a weak sense.
- **E, the sub's April Fools play** (98). The host sub's play is organized work beside the canvas; it marks where the model's scope ends. A form in a narrow sense, of the sub's play rather than of canvas organizing.
- **F, the spot** (56). Rooms ask for space before they build, move for the spot's reasons more than for too few hands, and build again. A form in a narrow sense, on few rooms.

**The form that best supports the claim: C.** One change, collective representation, is held by 97.9 per cent of its defining rooms, and its members' words show relations the model does not state.

**The form that most threatens it: B.** Its three signatures are held by different rooms at about chance, and no relation joins them. A cut can gather rooms that share nothing but being left over.

**The condition between them** is whether one change is held by nearly all of a form's defining rooms. Where it is (C 97.9, F 94.1 per cent), the form states relations. Where the signatures are held by under half each (B), the form is a list.

## The return value

- **Forms accounted:** 6 of 6.
- **Failed the form test:** B, reported as a grouping.
- **Names that survived the members' reading:** A, B, C, E and F kept (C and E with a sharpening). D: a renaming proposal, *keeping, with traded help or carrying on*, because its two minor signatures are held together only at chance.
- **The form whose reading disagreed most with the room models:** none. In each account the room models I quoted agree with my reading of the members' lines.
- **Where the uncomposed rooms sit** (first-return verdicts, by the last ruling or else the readers' agreement): the one room that does not compose, r/picturegame (kind out of scope), is a thin room of E. Cannot tell: A 2, B 2, C 2, D 1, E 0, F 3; all ten are thin or core rooms.
- **Arrow absences:** none real. All 21 arrows are not-testable-here in every form; the largest expectation is 0.942 (form A), the smallest form's largest 0.318 (F).
- **Propositions that failed against a real expectation:** none. No `findings.jsonl` line is bounded from a form.
- **Subform candidates for the next stage:** A.2; B.2 and B.1.2; D.1 and D.2, with D.2.1 and D.2.2. None was cut.
- **The mixture rule** (logged at D5a-37): neither outcome at B, D and E; mixed at F (calls and border terms held by the same rooms, 8 against 6.2).

## Survival by form (from the record, never the canvas; not compared here)

| form | median organizing end (hour) | mean aftermath share | work_remained kept, lost, silent |
|---|---|---|---|
| A | 71.99 | 0.0159 | 79, 47, 40 |
| B | 72.30 | 0.0387 | 72, 42, 27 |
| C | 71.66 | 0.0164 | 71, 36, 18 |
| D | 72.05 | 0.0179 | 60, 39, 20 |
| E | 72.045 | 0.0145 | 45, 41, 12 |
| F | 70.86 | 0.0056 | 20, 13, 23 |

## The most consequential difference between two forms

D and E. Both hold the sub's April Fools play: D's part D.2 changes keying in 66.7 per cent of its defining rooms, E in 71.4. But D.2's rooms kept their canvas work inside the play (repair work 73.8 per cent), and E's record is the play itself (repair work 32.1 per cent). D.2 lies 0.270 from D's centre and 0.611 from E's. So the frame does not decide a room's form; what the room did with its canvas work beside the frame does. The restrict sort shows the same divide from the other side: where the record holds the work, the arrow mostly fails as stated (F, 63 per cent of its lines); where the record holds the play, it most often cannot show the arrow at all (E, 37 per cent).

## Licences exercised (METHOD.md)

- The path outside `forms/` (departures line 18), so the stage's close-check, which reads `forms/` as branch accounts, did not refuse the room-form accounts.
- The rules logged at D5a-36 and carried unchanged: thin and core rooms weigh less; representatives by distance to the centre; the split rule; the restrict sort's four classes, written to files before counting.
- The mixture rule, logged at D5a-37 and applied at B, D, E and F; `d5f_mixture.py` edited at D5a-41 to read a link signature, its earlier outputs unchanged in content.
- Descriptions beyond the walk, labelled so (`d5f_split.py --start`; the parts helpers at D and E; the propose lines read whole at E).
- At E and F the representative rule picked one room twice; three rooms were told.
- At F, rows below the table's floor reported and flagged.
- Before each account was written, its claims were checked against the sources by script and corrected (A to F: two rounds or one); after each was written, it was read whole and corrected by Edits, each logged.

## Slips

Logged in the diary as they happened: Python writing a file from inside Bash, once (D5a-39); commands refused by the guard (a `cut` after a helper, a shell variable, one Python read at D5a-41 whose pattern the guard refused), redone without the refused form and with nothing written; a no-op shell variable at the head of a command (D5a-40); two Edits to the head in one turn (D5a-40); a count logged as 25 that was 26, corrected by an appended line (D5a-39).
