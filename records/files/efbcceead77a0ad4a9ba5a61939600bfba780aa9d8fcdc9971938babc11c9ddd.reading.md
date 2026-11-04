# Handback, stage D1: the return, built

Leg D1a, 15 October 2026. The model is fixed at pass 15, recorded at C5d-p2's close. D1 serves that version and changes nothing in it. J's rulings (17:40 Amsterdam, through the PI):
- Stage D runs at xhigh effort.
- The room, or a group of rooms, is the unit.
- The contract's two questions stay in view.
- My solo reads stand, with their limits as I stated them.

## The return value

| What | Count |
|---|---|
| Tasks built | 705 (0 unbuilt) |
| Verdict packets built | 705 |
| Elements and arrows in `VOCABULARY.json` | 51: 30 elements (23 standing, 2 tentative, 5 candidates) and 21 arrows (20 standing, 1 tentative). Beside them: 197 third-order themes, 28 fourth-order themes, 8 dimensions |
| The `MODEL.md` ceiling | 6,000 words; 3,591 written |
| Expectation lines | 705, one per room: 9,329 expected to instantiate, 311 expected absent |
| Rooms `not-testable-here` on any element | 362 (42 of them below the concept floor) |
| Story-miss rooms carried | 19 of 19 (told with a residue at pass 5; none untold) |
| The largest payload | counting, 11,409,524 bytes |
| Folder hash | 61b03bbf67bc8f010774eadd364e8bf0f4e577e0b6608185893845229e508a5c |
| `VERSION` | e15f96470271763d9913e79ed8e332c164a1f176106eefacfe8ffac8e1b3fecd |

**Expected to instantiate, by element and arrow (rooms):** A01 126, A02 89, A03 190, A04 401, A05 158, A06 203, A07 182, A08 289, A09 145, A10 21, A11 185, A13 240, A14 214, A15 129, A16 104, A17 172, A18 68, A19 121, A20 155, C01 46, K01 368, K02 89, P01 370, P02 535, P03 237, P04 237, P05 526, P07 205, P08 467, P09 231, P10 124, P11 522, P12 381, P13 213, P14 236, P15 361, P16 284, P17 146, P18 116, P20 274, R01 169. One room has an empty list: none of its themes is placed on an element.

**Expected absent (rooms):** C01 286, P20 25.

**Expected nowhere:**
- **By rule:** the tentative entries (P21, P22, A21) and the five candidates (K03, K04, P06, P19, R02). The model makes no claim for them.
- **By the rules' reach:**
  - **A12:** its end P15 is never carried by a placement.
  - **C02:** expected nowhere by my omission (see "Limits of the expectations").

## The folder

`handoff.py D` built `handoff-D/`, `verdict-D/` and `sealed/` once. It wrote the folder hash to `handoff-D.sha256` and to `RUN.json` (`handoff_D.first`). `_analysis/d1_payload.py` recomputes the hash the way `handoff.py` does and gets the same value. `VERSION` equals `vlib.model_hash` in the folder and in every task. `notes-D1.md` holds the hash, the payload and the checks.

## The payload, and rooms too large for one session

- **Task payloads** (the bytes of the whole task folder): median 281,916, p90 408,944, largest 11,409,524. Each task carries the same 198,856 bytes of specification, vocabulary, ladder and global model.
- **Verdict packets:** median 30,314 bytes, p90 31,880, largest 34,955 (portugal). None is over the 50 KB ceiling.

No run document states a labeler's context, so I declared one session at about 1,000,000 bytes served, which is about 250,000 tokens. Four rooms exceed that figure. I cut, split and read none of them. The handler returns each whole, or marks it `unreturned` with the reason.
- **counting:** 11,409,524 bytes, about 2.9 million tokens. Its `forest.md` alone is 11,117,662 bytes. No single session holds it.
- **ainbowroad:** 1,316,658 bytes.
- **leagueoflegends:** 1,203,039 bytes.
- **theblackvoid:** 1,172,865 bytes.

The last three are near the figure, and a session may hold them.

## The checks (§4)

- **Ids:** every id a task names resolves against `VOCABULARY.json`.
- **Nothing beyond the room:** no task or packet holds a canvas field, a room note, my notes or another room's lines. Every task holds the same twelve files.
- **Every room:** each of the 705 rooms has a task, an `index.tsv` row, a verdict packet and an expectation line.
- **`MODEL.md`:** it equals `MODEL-D1.md` and fits the ceiling. Every task's `MODEL.md` begins with it.
- **The expectations:** `sealed/EXPECTATIONS.jsonl` equals `EXPECTATIONS-D1.jsonl`, and no copy sits in either served folder.
- **The packets:** every packet carries `prior.md` §8 verbatim, the room's concept count and its off-platform pointers, and ends with the end marker.

## Defects in the tools (I changed neither the model nor the folder)

1. **The dimension check, QD1-001 (answered; the check is repaired).**
   - `validate.py D1` gave 30 errors of the shape vocab:dim, and the first close-check failed on them alone.
   - `handoff.py` copies each element's `dimension` into `VOCABULARY.json` as the frozen `model/elements.jsonl` holds it, a list: 28 elements hold one id, one holds two and one holds an empty list. Every id is in `dimensions.jsonl`.
   - `tools/checks/stage_D1.py` read the field as one value. Stage C2's check (`stage_C2.py`, line 236) accepts the list, and `validate.py C5` passed on the same ledger.
   - I could not repair it from `out/`. I asked the PI and changed no model file, no tool and nothing in the folder.
   - **J's ruling (21:19 Berlin, through the PI):** an element may sit in two or more dimensions, so the list is right and the check was wrong. The check now reads one id or a list, as stage C2's does. `validate.py D1` gives 0 errors and 0 warnings, and the folder hash is unchanged.
2. **The candidates carry no status.** `handoff.py` drops withdrawn entries and marks tentative ones, but it serves the five candidates (K03, K04, P06, P19, R02) in `VOCABULARY.json` with no mark. A labeler who reads only the vocabulary sees them beside the standing elements. `MODEL.md` names them as standing outside the model, and D3 should read any line on them as a line on a candidate.

## Limits of the expectations

The expectations follow rules R1 to R6, which I wrote in `notes-D1.md` before I generated them. They were sealed and hashed before any return existed, so I changed none of them after the build.
- **C02 is expected in no room.** This is my omission, not a rule. R1 finds an element carried through the order tests' theme file (`_analysis/c2_elements_c5c2.json`), and that file has no line for C02, a standing claim on four fourth-order themes. E1 should read C02 as unpredicted.
- **The residue clause misses the host rooms.** Expectation 13 is carried in `why` for rooms placed on a colour faction's themes (T4-023's members) or on P19's host themes. It reaches the four colour-faction story-miss rooms, but none of the four host rooms: catalunya, placeDE, smashbros and sweden. Their themes are not on P19's themes. catalunya's line expects decided order (C01) absent.
- **P20's absence uses a stand-in.** A room with no posts in the week before the canvas stands in for a sub opened for the canvas. The record does not show when a sub began, so this expectation is weaker than the wording in `implications-C5.md`.
- **Rule 6 governs every absence.** C01 and P20 are expected absent only in rooms above the concept floor that call for hands. Where a room had no opportunity, the element is `not_testable_here`.

## The story-miss rooms

The 19 rooms told with a residue at C2's last pass are listed in `notes-D1.md` with their residues, and all 19 are carried. D3 counts how they fared:
- **Colour factions (4):** greenlattice, orderofthebluecorner, purplecorner, thebluecorner.
- **Hosts ruling on guests (4):** catalunya, placeDE, smashbros, sweden.
- **What the mark brought back (6):** scp, parahumans, TheAdventuresofTintin, shishamo, hunterxhunter, luciomains.
- **Single residues (5):** starcitizen, texans, totallynotrobots, epublica, bih.

## prior.md §7 and §8

I wrote both first, before the build and before any adaptation existed. `distance.py` reads both §7 lines.
- **§7:** `w = 4, 2, 1, 0.5` and `g = 1, 0.5, 0, -1`.
- **§8:** the concept floor is 10 first-order concepts (42 rooms fall below it). The off-platform threshold is 20 pointers, or at least 3 pointers and at least one for every four concepts (68 rooms are past it). Both are review prompts for `cannot-tell`, not rules.

`done.sh` seals `prior.md`'s hash at this close.

## What I did not do, and departures

- I wrote no adaptation or verdict, read nothing in `DROPS/`, and served no canvas field, room note, notes file or other room.
- **A departure from the stage card:** §3 asks for the payload figures before the folder is hashed. I wrote them after: `handoff.py` prints them only once it has written the folder, and it writes the folder once.
- **Slips:** the guard refused `cut -c` after a read twice (after `mem.py diary` and after a grep of findings). I reran both without the cut.
