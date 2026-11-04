# Handback, stage C5: the account

Written at C5c-13, 2026-10-15 (UTC), at the close of stage C5.

## C5d's work was redone in C5c-13, and why

C5d closed at 10:38 UTC with the table, the figure, the implications, this handback and the interview brief. After the C5d interview, J read six requests of mine and lifted the freeze for serial work in this branch (13:45 Amsterdam), with one problem per leg:
1. **The unit** (C5c-08). The room, or a group of rooms, is the actor where its members spoke or acted for it.
2. **Thin evidence** (C5c-09). The thin arrows were read in every room, and the field analyst's blind second coding of border talk was scored.
3. **Stigmergy and "aligned"** (C5c-10). The choice was argued from organization design.
4. **The reason test** (C5c-11). Survivor bias was weighed before the asymmetry of reasons was read.

Each problem wrote its finding to `serial-C5/`. C5c-12 folded the findings into the account, the propositions, the prose test and the model in one pass (pass 15).

**Why this leg exists.** The C5d outputs described the model before those changes. J ruled (16:29 Amsterdam) that the handler cannot reopen C5d, a closed leg, so this leg redoes C5d's work from the model as pass 15 left it, under a C5c label. The earlier outputs are kept as `data_structure-C5-p14.md`, `figure-C5-p14.md`, `implications-C5-p14.md` and `handback-C5-p14.md`. The C5d interview brief stays filed in `interview/`.

**The model freeze.** `done.sh` records the model's hash only when a C5d leg closes.
- `_closes/model-C5.sha256` holds the hash taken at C5d's close: 24d18e0e…216d7.
- The model as pass 15 left it hashes to e15f9647…b3fecd (`vlib.model_hash`).
- I asked how the freeze is to be re-recorded (QC5-003), and I left `_closes/` untouched.
- After the freeze, nothing below the model moves except as a validated amendment at D3.

**What stage D reads:**
- **The model:** `account.md` (pass 15), `propositions.jsonl` (9), `figure-C5.md`, `data_structure-C5.md`, and `implications-C5.md`, from which stage D1 writes `EXPECTATIONS.jsonl`;
- **The tiers:** `model/`, `fourth/fourth.jsonl` and `dimensions.jsonl`, as they stand.
- **The record of each step:** `notes-C5.md`, `account_passes.jsonl` (15 passes), `serial-C5/` and the diary.

## The claim

When strangers organize on a clock they did not set, with no way to compel anyone, rooms run one order: a start, the room's calls for hands, building, then keeping the work. They differ in what they meet after building:
- **neighbours,** with whom they make agreements no one can enforce, and trade help through deals;
- **a rival,** whose attack call the room's own members often refuse;
- **a loss,** after which the room judges its hands too few and moves or gives the work up;
- **or nothing.**

They also differ in how they coordinate many hands: by posting the work's state in the thread, by sharing a template, or both. Rooms aligned many hands without deciding how they were organized. Placement stopped at hour 73 for every room, and after it the room records the work and decides what to keep.

- **The room that best supports it: day9.** It offers a neighbour terms before any damage, loses the agreement at hour 48, judges its spot lost and moves within two hours, and finishes the new work at hour 53.
- **The room that most threatens it: thebluecorner.** It is a colour faction whose faith names its rivals and rules on guests.
- **The condition that separates them** is what decides whom a room fights and whom it admits. Where the work decides, the model tells the room. Where a faith or a host's rule decides, it does not.

## The passes, and what each changed

| pass | leg | what changed | criterion |
|---|---|---|---|
| 1 | C5a-01 | 28 fourth-order declarations amended under the prose rule; the account drafted | prefer |
| 2 | C5a-02 | seven dimensions amended; A04 bounded; P06, K01 and R02 cut; nine propositions | prefer |
| 3 | C5a-03 | K01 restored | prefer |
| 4 | C5a-04 | the rule that decides whether an element stays stated | no change |
| 5 | C5c-01 | the readers answered: ten errors fixed, 34 sentences rewritten | prefer |
| 6 | C5c-02 | Stigmergy recut by three codings; F-018; 94 pieces of field advice accepted, 30 kept | prefer |
| 7, 8 | C5c-03, C5c-04 | model statements took pass 6's wording | prefer |
| 9 | C5c-05 | K02, A10 and P13 restored to the room | prefer |
| 10 | C5c-06 | nothing changed; the passes stopped, and C5d followed | no change |
| 11 | C5c-08 | the unit: the room restored as actor in 5 declarations, 5 elements and 4 arrows | prefer |
| 12 | C5c-09 | thin evidence: the border range by two coders; A10, A05 and A14 read in every room; F-019, F-020 | prefer |
| 13 | C5c-10 | Stigmergy renamed Direct information sharing; "aligned" with its count; F-021, F-022 | prefer |
| 14 | C5c-11 | the reason test: survival first; calls to place read; F-023; F-014 superseded | prefer |
| 15 | C5c-12 | the fold-in: account, propositions, prose test and A16 | prefer |

The criterion written before pass 1 says "prefer" of pass 15, the pass kept.

## Arrangements, cuts and tier events

- **Arrangements drawn.** `sketches.md` holds five: by the canvas clock; by tier; by trajectory; by tier after the cuts; and by tier with K01 restored. The account rests on the arrangement by tier, with the clock written into its last section.
- **What was cut.** Two elements:
  - **P06, attribution.** The model no longer says that working out who changed the work is part of organizing. It was tested twice as the step between restraint and attack and was not found.
  - **R02, the envoy.** The model no longer names the role, though deals made through envoys stay in P08.

  K01 was cut and restored.
- **Tier events:**
  - **Fourth order:** 59 construct amendments (28, 27, 3 and 1 by leg) and 2 membership changes (Stigmergy's recut).
  - **Dimensions:** 18 construct amendments.
  - **Third order:** 2 themes moved to another fourth-order theme (T3-041 and T3-060, to Collective representation). No third-order theme was split or merged, so no second-order theme moved.
  - **The model's history:** 46 lines in C5.
- **Names.**
  - No name failed the prose test.
  - One was renamed by the choice rule of C5c-10: Stigmergy became Direct information sharing (Okhuysen and Bechky 2009, p. 474). Its records are members' posts of the work's state, and the old name claimed the placing that would answer them, which the record does not hold.
  - Collective efficacy, Live and let live and Reciprocity now have read evidence for their mechanisms (F-019, F-020).
  - Critical mass stays flagged.

## The readers

- **Fidelity both ways.** The three readers recovered four of my nine claims whole and three in part. None recovered that the mark tells members what is missing, or where the account stops. They recovered three claims I did not list, all of them in the account. No claim that all three found was unintended.
- **Their items.** Ten errors were fixed and 34 unclear sentences rewritten. Their disagreements are printed beside the account.
- **Their rooms.** cardinals was judged unfit from seven passages, my packet's error. luciomains and mysterydungeon were judged to fit.
- **The second reading.** The field analyst's reading of all 36 declarations led to 94 sentences rewritten. Its blind codes decided Stigmergy's recut, and its second coding of 40 border records gave A04's range.

## Propositions, figure, data structure and expectations

- **Propositions:** nine.
  - Three are thin (N07, N08, N09).
  - One rests wholly on theorised arrows (N07). It now rests primarily on counts: F-021, F-023 and F-006.
  - Two carry a mechanism from the literature (N03, N07).
  - N09 is narrowed to the channel for help, with sparing by a settled line marked theorised.
- **The figure:**
  - 23 standing elements: 21 boxes in three columns, with two claims beside them;
  - 20 arrows, each tagged with its proposition: 19 shown by an audited transition, 1 by a quote;
  - drawn with and without the theorised arrows A11 and A12; A05's mechanism is marked theorised;
  - not drawn: the field's tentative arrow, which no proposition carries;
  - no loop is grounded.
- **The data structure:** 195 rows, one per third-order theme a fourth-order theme gathers, plus the two residue themes below the table. The rows come by the rule logged before C5d's table: within each fourth-order theme, rooms are taken from the four size quarters in turn, with seeded draws. The rule is written in `notes-C5.md`.
- **Expectations for the return:** thirteen, in `implications-C5.md`.

## What the account showed that the room notes did not predict

- Most border talk that comes before upkeep offers terms before any damage, by two coders at both ends of their range.
- In written replies, refusals give a reason and acceptances come bare. Most calls get no written reply at all.
- After doubt and a loss, rooms give the work up about as often as they move (11 against 10).
- A room spares a neighbour's work mostly on its own norm, not on a settled border.
- Posting the work's state and sharing templates are two routes, carried largely apart.

## The sentence I am least sure a reader will take as meant

"In 233 of the 370 rooms that called for hands, the room's record reports a work up after its first call; in the others, the room tried." "Aligned" rests on the room's own report that the work was up. A reader may take it to mean that the placers aligned on the canvas, which the record cannot show.

## Licences exercised (METHOD.md)

- **Gioia's explosion at the front end:** exercised. The tiers rest on the coders' 115,388 concepts and 7,844 second-order themes. The data structure shows all five tiers.
- **An in-sample return in Eisenhardt's spirit:** prepared, not yet run. The thirteen expectations are written for stage D1.
- **Langley's strategy, declared:** exercised in part. Temporal bracketing (hour 73), narrative (the account, told both ways) and visual mapping (the figure) were used.
- **The count set by kinds, not by a head's capacity:** exercised. The 23 elements stand by the criterion written before pass 1.

## Confidence, and what the serial work changed

- **Sure:** the spine and the contest, as orders of first concepts in what members wrote, each beating a null of 500 shuffles within each room.
- **Less sure:**
  - the thin and theorised arrows;
  - the one-member theme Direct information sharing;
  - the border reading, where the two coders agree only slightly (kappa 0.19);
  - the refusal side of the reason test on calls to place, which rests on 3 replies.
- **What the serial work restored or corrected:**
  - the room as the actor;
  - "aligned", now with its count;
  - a construct name that claimed more than its records;
  - one mechanism (A05) that the members' words do not show.
- **What it found:** that thin evidence, read in every room, can show a mechanism (A10) or overturn my belief in one (A05).
