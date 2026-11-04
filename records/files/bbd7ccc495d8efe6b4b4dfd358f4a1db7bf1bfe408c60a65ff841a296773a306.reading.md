# Handback, stage B4: adjudication, and transmission after revision

Written at B4c, 2026-10-13. The reports are `adjudication_report.md` (the seven packets of rulings), `transmission-B4.md` (transmission decomposed, section 3), `transmission-after-revision-B4.md` (the blind sample) and `coder_conflicts.jsonl` (72 conflicts). The record of every step is `notes-B4.md`. The placements final are `assign_final.jsonl`.

**What these figures license.** The readers share an architecture with me, so every agreement and transmission figure here bounds whether the written instrument decides, not whether it is right.

## The claim

**The scheme decides G14, space and help between rooms, worst.** On fresh readers against the settled line, G14 is among the three worst families for both arms in both strata. The figures are 0.507 and 0.310 in the uniform stratum and 0.423 and 0.385 in the adjudicated one. At stage B3 it was a middling family (0.697). Its themes turn on who asked whom for what: a border settled (T3-010), help sent (T3-011), space asked of a host (T3-035), help asked of a room (T3-084), a host's approval disputed or given (T3-094, T3-162). Their neighbours in G13 and G15 turn on the same questions (T3-039, T3-149, T3-150, T3-151). One exchange between rooms usually holds several of these acts at once, so readers count the same concepts under different siblings.

- **The item that best supports it: warframe t11.** Four fresh readings give three different primaries: T3-010, T3-094 and T3-162. GreenLattice's permission, its no-build zone and a member's "The people who made /r/GreenLattice have no authority" each meet a different G14 gate. Here the readers disagree with each other, not only with my line.
- **The item that most threatens it: witcher t05.** It is a G14 item on which the fleet and all four fresh readings agree (T3-010). Its low score comes only from the B1 themes the class 2 rule kept in the settled line (T3-046, T3-050).
- **The condition that separates them** is whether one room asks another for something: space, help or approval. Where it does, the siblings split. Where the item is a border talked over with no request, readers agree, and only how the settled line was built lowers the figure. The adjudicated stratum holds no class 2 item, and G14 is still second worst there for both arms, so the claim does not rest on class 2.

## The placements final

`assign_final.jsonl`, sha256 d3506a88…, holds 7,844 lines, one per second-order theme of the analysed set, with nothing pending.
- Classes 1 (2,566) and 2 (1,990) stand from the fleet; class 2 keeps my B1 grouping, tagged `b1_grouping_kept`.
- Classes 3, 4 and 5 (3,288) carry their rulings.
- The blind sample's check revised no ruling.

## The counts

- **Contested items inherited and adjudicated:** 3,288 of 3,288 (class 3 2,393, class 4 837, class 5 58), in seven packets.
- **Rulings by taxonomy:** genuine-joint 1,651, author-error 571, scheme-ambiguous 451, item-is-a-bag 255, author-disagrees 208, reader-error 152.
- **author-error and author-disagrees:** 571 and 208.
- **The three themes with the most scheme-ambiguous rulings:** T3-017 (55), T3-033 (34), T3-001 (32).
- **The field that failed most:** `must_show`, 252 of 451; then discriminators 114, `must_not_show` 57, `decide_when_both` 28.
- **named_neither and unresolved:** 757 (23.0%) and 185 (5.6%).
- **Boundaries ruled once:** 64 sibling pairs, deciding 817 items. The largest are T3-005|T3-021 (90 items), T3-010|T3-149 (62), T3-009|T3-043 (62) and T3-017|T3-031 (39). Each has its paragraph in `boundaries.md` and its item list in `adjudication_report.md`.
- **Whether the pilot's predictions held:** 17 of the 19 pairs of `confusions.md` split readers at least once; pairs 17 (T3-044|T3-082) and 18 (T3-014|T3-152) never did. B2 missed G20's pairs with T3-031 and G21's with T3-073 and T3-117.
- **The four transmission rows** (`transmission-B4.md`; gold items, then pilot items): the scheme decides 21 and 30; fails to transmit 1 and 0; the instrument does not decide this item 6 and 12; teaches something unintended 12 and 8.

## Transmission after revision

**The definition** is stage B2's: Jaccard on placement sets, alpha with distance 1 − Jaccard and chance over the pooled sets, primary match beside it, pass 1 only. A reading whose settled line is unresolved leaves the denominator.

**The arms.** Arm 1 is DeepSeek V4.1 Flash at medium effort, the fleet's model and stage B2's. Arm 2 is OpenAI gpt-6-astra at medium effort under Codex's built-in instruction. They are reported apart and never pooled.

The next table gives the two figures per arm and stratum, with the stability floor and stage B3 beside them.

| arm | stratum | fresh against settled | readers' agreement | readers' alpha | B3 readers, same items |
|---|---|---|---|---|---|
| 1, DeepSeek | uniform | 0.657 | 0.781 | 0.776 | 0.781 |
| 1, DeepSeek | adjudicated | 0.544 | 0.664 | 0.658 | 0.514 |
| 2, OpenAI | uniform | 0.622 | 0.872 | 0.869 | 0.781 |
| 2, OpenAI | adjudicated | 0.554 | 0.804 | 0.801 | 0.514 |

- **Against the floor.** The stability floor is 0.807 and B3's corpus agreement is 0.786. Arm 1's readers agree with each other in the uniform stratum exactly as the fleet did on the same items, inside the floor. They reach the settled line less often than they reach each other.
- **Where the line comes from matters.** Fresh DeepSeek readers reach the line in 0.930 of class 1 (fleet agreed, equal to my B1) and in 0.491 of class 2, where the line keeps my B1 grouping. Without class 2 the uniform figure is 0.703. Stage B2's gold figure (0.624, same model) is the lower, so the hard set was harder, by a small margin.
- **Arm 2's agreement is an upper bound.** Its two replications read byte-identical messages, and on the 18 items read twice they agree within a packet (0.889, 0.861) far more than across packets (0.653).
- **The three worst families** on fresh against settled (10 items or more): arm 1 uniform G14, G07, G08; arm 1 adjudicated G10, G14, G02; arm 2 uniform G14, G07, G08; arm 2 adjudicated G07, G14, G04.
- **Stratum R** (all 185 unresolved items) has no settled line. Fresh DeepSeek readers agree with each other at 0.623 there (the fleet 0.543), and most land on a placement someone already made, which does not resolve the items. 104 and 134 of 370 readings fall wholly outside every earlier placement.

**The unanimous items a fresh reader placed elsewhere:** 79 in either arm (62 in arm 1, 74 in arm 2), each named with a paragraph in `transmission-after-revision-B4.md`. The verdicts:
- the fleet's shared assumption 25;
- the settled line keeps my B1 themes 22;
- rule 0 applied differently 24;
- the scheme does not decide 6;
- the fresh reading misses a field 2.

In most of the 25, the fleet's two readers counted concepts under a theme whose own `must_not_show` or discriminator names a sibling. Examples are defence calls under T3-002 and a homeland flag under T3-002 or T3-038. Two readers agreeing is not the scheme deciding, and classes 1 and 2 stood without adjudication.

## For stage C1

- **The boundary I most expect stage C1 to have to move: T3-017|T3-031, the canvas condition.** T3-017's discriminator lets a room's in-joke be T3-031 when carried "into the canvas talk or the day", while T3-031's `must_show` and discriminator require the canvas. It was ruled once over 39 items and failed 47 rulings, the most of any sentence. Fresh readers split on it again (danganronpa t01, metroid t16).
- **The homeland flag.** Fresh readers placed T3-065 where the fleet placed T3-002 or T3-038, in AmericanFlaginPlace t03, FaroeIslands t01 and wales t02. T3-002's `must_not_show` sends the flag to T3-065, but the other siblings' `must_not_show` lines do not.
- **G14's request siblings**, as in the claim above.
- **The class 2 settled line.** It keeps B1 themes placed under the B1 scheme. In the sample, 22 of 53 such items keep themes no reader of the fleet or of either arm placed.
- **Sources.** `transmission-B4.md` and `transmission-after-revision-B4.md` are among stage C1's sources. The per-theme agreement C1 needs is stage B3's (`out/_analysis/b3_check_record.json`).

## The licences exercised

- **FLEET.md's licence** on every figure: it bounds whether the written instrument decides, not whether it is right.
- **J's rulings.** 500 items, 250 uniform and 250 adjudicated; the OpenAI arm, reported apart; stratum R holding all 185 unresolved items, its 18 that are also in U or A read twice.
- **My choices under J's latitude.** The three-concept floor for a lone B1 theme in class 4 (J: "whatever the agent feels more comfortable with"); the strata drawn disjoint; class 2 reported on its own row, with a second figure against its placed themes; one reading refused under the declared assembly rule; the fixed verdict test for the 79 paragraphs.
