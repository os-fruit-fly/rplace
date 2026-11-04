# Notes, stage D1 (the return: the build)

The model is fixed at e15f96470271763d9913e79ed8e332c164a1f176106eefacfe8ffac8e1b3fecd, recorded at C5d-p2's close. `handoff.py --hash` agrees. J's rulings (17:40 Amsterdam, through the PI):
- Stage D runs at xhigh effort.
- The room, or a group of rooms, is the unit.
- The contract's two questions stay in view.
- My solo reads stand, with their limits as I stated them.

## prior.md §7 and §8, written first

Both were written at D1a before anything was built and before any adaptation was seen (diary, D1a).
- **§7:** `w = 4, 2, 1, 0.5` and `g = 1, 0.5, 0, -1`, each with its reason. `distance.py` reads both.
- **§8:** two review prompts for `cannot-tell`, served verbatim in every verdict packet. Each was set with its reason.
  - *The concept floor:* 10 first-order concepts. 42 of 705 rooms fall below it.
  - *The off-platform threshold:* 20 pointers, or at least 3 pointers and one or more for every four concepts. 68 rooms are past it.

## The story-miss rooms (from `story_rooms-p5.jsonl`)

The last story (C2, pass 5) told 16 of its 35 rooms with nothing left unexplained. It told 19 with a residue and left none untold. These 19 are the first rooms to watch at D3. Each is listed with the residue the story could not tell:
- **A faith in a colour names the rivals and rules on guests:** greenlattice, orderofthebluecorner, purplecorner, thebluecorner.
- **The room, or a host, rules on guests on its mark:** catalunya, placeDE, smashbros, sweden. Sweden carries a second residue as well.
- **What the mark brought back to the room:** scp, parahumans, TheAdventuresofTintin, shishamo, hunterxhunter, luciomains. The residue is newcomers, readers or players, or the fear of them.
- **Single residues:**
  - starcitizen: a rivalry held before the canvas shapes talk about an alliance;
  - texans: a mark built as a taunt at a league rival;
  - totallynotrobots: the sub's joke picked the room's one work;
  - epublica: an old quarrel names a rival for some members;
  - bih: members learn from others how large flags are made.

## The ceiling for MODEL.md, and what it cut from account.md

**The ceiling is 6,000 words for `MODEL-D1.md`,** the global part that every task carries. `handoff.py` appends per task the entries for the elements the room's themes were placed under. `MODEL-D1.md` holds 3,591 words (`_analysis/d1_model.py`, which refuses to write over the ceiling).

**What it holds.** It is written from `account.md`'s structure and the frozen ledgers:
- every standing element's statement and range, read from `model/elements.jsonl`;
- every arrow as "when X, Y follows, because Z", with its mechanism read from `model/arrows.jsonl` and its strength, theorised status and tentative status;
- the two claims, the two tentative elements and the tentative arrow;
- the five candidates, each marked as standing outside the model;
- where the model stops, in its own terms.

**What it cut from the account:**
- every room's name and every quote, including day9, ubc and ultrahardcore (the three rooms told from the room up);
- the counts of rooms behind each order (the model describes the universe, not the mode);
- the history of the passes, the readers and the cuts;
- the section on what the account answers of the two questions;
- the list of rooms told with a residue, which becomes "Where the model stops" in the model's terms.

**What remains and why:**
- *Two short quotes in element ranges* ('On it.', 'Did my part.', 'We did it!' and one in P21's range). They name no room. `LADDER.md` serves other rooms' quotes by design.
- *Counts inside two arrow mechanisms* (A12 and A16, from F-023 and F-014). These are the ledger's mechanisms as `VOCABULARY.json` carries them.

**A defect for the handback.** `handoff.py` serves candidate elements in the vocabulary with no status mark: it drops only withdrawn entries and marks only tentative ones. `MODEL-D1.md` therefore names the five candidates (K03, K04, P06, P19, R02) as standing outside the model.

## The rules for the expectations, written before they were generated

One line per room of the analysed set (705), from `implications-C5.md` (its thirteen expectations), `propositions.jsonl` and the room's placements (`assignments_final.jsonl` and the order tests' element themes, `_analysis/c2_elements_c5c2.json`). The script is `_analysis/d1_expectations.py`.

**R1. Carried.** An element is carried in a room when one of the room's second-order themes is placed on a third-order theme of that element. P15 and C01's form-pass tiers lift from no theme, so placements never carry them.

**R2. Expected to instantiate:**
- every element the room carries (from the placements);
- every arrow whose two ends the room carries. Where both occur, the model expects the order its arrow states (implications expectations 1 to 4 and 6 to 8; propositions N01 to N06, N08 and N09).

- P15, the bare answer, in a room above the concept floor that carries P01 (expectation 12; F-023). P15 lifts from no theme, so R1 alone would never expect it.

The tentative entries and the candidates are expected nowhere: the model makes no claim for them.

**R3. Expected to be absent.** This applies only in a room above the concept floor (10 concepts) that calls for hands (carries P01), and only for an element the room does not carry:
- **C01, decided order** (expectation 5; F-006). Expected absent unless the room carries a theme of a colour faction (T4-023's members) or of a host ruling on guests (P19's themes), where decided order is coded more often.
- **P20, the host's line** (expectation 6), in a room with no posts in the week before the canvas.
  - *This departs from a plain reading:* the absence of prior-week posts stands in for "a sub opened for the canvas". The record does not show when such a room began (N05's boundary), so the expectation is weaker than the implications' wording.

**R4. Not testable here** (rule 6). These are listed in `not_testable_here`, never in `expect_absent`:
- **A room below the concept floor:** every element and arrow it does not carry.
- **A room that carries no mark of its own** (none of R01, P02, P03, P05): upkeep and what follows from it (P05, P14, A03, A04, A06, A13, A19).
- **A room that carries no call** (no P01): the bare answer and the calls' arrows (P15, A01, A12, A15, A20).

**R5. The residue.** Expectation 13 (colour factions and hosts ruling on guests compose with a residue) names no element. For those rooms it is written in `why`, so stage E1 can read it beside the verdict. This departs from a plain reading of the implications only in where the line carries it.

**R6. Why.** Each line gives one clause per element and arrow listed, in the model's terms.

## The folder

**Folder hash: 61b03bbf67bc8f010774eadd364e8bf0f4e577e0b6608185893845229e508a5c** (`handoff-D.sha256`, the same in `RUN.json` under `handoff_D.first`). `_analysis/d1_payload.py` recomputes it the way `handoff.py` does and gets the same value. **VERSION:** e15f96470271763d9913e79ed8e332c164a1f176106eefacfe8ffac8e1b3fecd, equal to `vlib.model_hash` in the folder and in every task.

## The payload, measured (§3)

I wrote these figures after the hash, not before: `handoff.py` prints the distribution only once it has written the folder, and it will not write the folder twice. The figures come from `tasks/index.tsv` and `verdict-D/` (`_analysis/d1_payload.py`).
- **Task payloads** (705; the bytes of the whole task folder): median 281,916, p90 408,944, largest 11,409,524 (counting).
  - Every task carries the same 198,856 bytes: `RETURN-D.md`, `VOCABULARY.json`, `LADDER.md`, `VERSION` and the global `MODEL.md`.
  - The room's own part (`TASK.md`, the documents and the appended model entries): median 83,060, p90 210,088, largest 11,210,668.
- **Verdict packets** (705): median 30,314 bytes, p90 31,880, largest 34,955 (portugal). None is over the 50 KB ceiling. Every packet ends with the same end-marker line and carries `prior.md` §8 verbatim.
- **The ceiling for `MODEL.md`:** 6,000 words; 3,591 written (above).

**Rooms too large for one labeler session.** No stage file or run document states a labeler's context. I declare one session at about 1,000,000 bytes served, which is about 250,000 tokens at about 4 bytes a token. Four rooms exceed it:
- **counting:** 11,409,524 bytes, about 2.9 million tokens. Its `forest.md` alone is 11,117,662 bytes. No session holds it whole.
- **ainbowroad:** 1,316,658 bytes, about 330,000 tokens.
- **leagueoflegends:** 1,203,039 bytes, about 300,000 tokens.
- **theblackvoid:** 1,172,865 bytes, about 290,000 tokens.

The last three are near the figure, and a session may hold them. In each, the largest files are `codes.jsonl` and `forest.md`. In all, 33 rooms exceed 500,000 bytes and one exceeds 2,000,000. I cut, split and read none of them. The handler returns each whole, or marks it `unreturned` with the reason.

## The checks (§4)

These checks ran on the built folders, through `validate.py D1` and `_analysis/d1_payload.py`.
- **Ids.** Every id a task names resolves against `VOCABULARY.json`. `validate.py` gives no error of that shape.
- **Nothing beyond the room.**
  - `validate.py` finds no canvas field and no other room's lines in any task or packet.
  - Every task folder holds the same twelve files and nothing else: `TASK.md`, `RETURN-D.md`, `VOCABULARY.json`, `VERSION`, `MODEL.md`, `LADDER.md`, `case.md`, `codes.jsonl`, `themes.jsonl`, `brief.md`, `forest.md` and `placements.jsonl`. No room note, no notes file, no proposition and no part of the account other than `MODEL.md` is served.
  - `MODEL.md` uses the word "canvas" only for the setting, in the model's own element statements (for example P20's "canvas talk"). It never names a canvas field or what a room made.
- **Every room.** The store, the task folders, the `index.tsv` rows, the verdict packets and the expectation lines each hold the same 705 rooms, once each. No task went unbuilt.
- **`MODEL.md`** equals `MODEL-D1.md`: 3,591 words, under the 6,000-word ceiling. Every task's `MODEL.md` begins with it.
- **The expectations.** `sealed/EXPECTATIONS.jsonl` equals `EXPECTATIONS-D1.jsonl`, and no copy sits in `handoff-D/` or `verdict-D/`. The search's one hit, `verdict-D/sheffield.md`, is a room's name.
- **VERSION and the hash.** Both are as above.

**Two defects for the handback.** I edit neither the model nor the built folder.
1. **The candidates carry no status.** `VOCABULARY.json` serves the five candidates (K03, K04, P06, P19, R02) with no status mark, beside the standing elements. Only `MODEL.md` says they stand outside the model.
2. **The dimension check failed on lists (QD1-001, answered).** `validate.py D1` gave 30 errors of the shape vocab:dim. `handoff.py` copies each element's `dimension` as the frozen `model/elements.jsonl` holds it, a list: 28 elements hold one id, one holds two and one holds an empty list, and every id is in `dimensions.jsonl`. `tools/checks/stage_D1.py` read the field as one value. Stage C2's check (`stage_C2.py`, line 236) accepts the list, and `validate.py C5` passed on the same ledger. I asked the PI as QD1-001 and changed nothing meanwhile.
   - **The answer (J's ruling, 21:19 Berlin, through the PI):** an element may sit in two or more dimensions, so the list is right and the check was wrong. The check now reads one id or a list, as stage C2's does.
   - `validate.py D1` now gives 0 errors and 0 warnings. The model, the vocabulary and the folder hash are unchanged; the hash still recomputes to the value above.

## Two limits of the expectations, found after the build

I found both while checking the story-miss rooms and the ids that no line expects. The expectations were sealed and hashed before any return, so I change neither (diary, D1a).
1. **C02 is expected in no room.** R1 finds an element carried through the order tests' theme file, and that file has no line for C02, a standing claim on T4-020, T4-021, T4-022 and T4-004. This is my omission, not a rule; E1 reads C02 as unpredicted. A12 is expected nowhere for a different reason: its end P15 is never carried by a placement.
2. **Expectation 13 misses the host rooms.** The residue clause reaches the four colour-faction story-miss rooms but none of the four host rooms (catalunya, placeDE, smashbros, sweden), because their themes are not on P19's host themes. catalunya's line expects C01 absent.

Every packet states the room's concept count and off-platform pointers exactly as `rooms.jsonl` holds them (705 of 705).
