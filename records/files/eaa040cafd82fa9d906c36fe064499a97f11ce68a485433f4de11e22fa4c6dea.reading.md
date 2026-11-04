# Handback, stage C1: scheme v2, the form pass and the fourth-order themes

Written at C1a-11, 2026-10-14 (UTC), at the last pass of stage C1. The outputs are `scheme_v2.md` and `scheme_v2.jsonl` (the scheme every later stage keys to), `assignments_final.jsonl` with `assignments_final.count.txt` and the overlay `assign_revisions_only.jsonl`, `fourth/fourth.jsonl` with `fourth/fourth.md`, `form_pass-C1.md`, and `tier_history.jsonl`. The record of every step is `notes-C1.md` and the diary.

**What any agreement or transmission figure here licenses.** Every reader, fresh or of the fleet, shares an architecture with me, so each figure bounds whether the written instrument decides, not whether it is right. No figure here is reliability.

## The claim

**The revision kept what the rooms were mostly doing and changed how many things the line says each room did at once.** My re-decision of 200 placements agreed with the current line's primary act in 0.845 of them. What changed is the number of acts a line carries. Second and third themes that rested on my B1 grouping, or on fewer than three concepts of their own, came off the line (the class 2 ruling; J's floor, QC1-002). Placements fell from 13,365 on stage B's settled line to 10,593 over the same 7,844 lines. Where readers split on a sentence, I sharpened it: 35 gate sentences in 18 themes, on April Fools questions, help between rooms, borders and truces, and credit. The pair test found a seam in every frequent pair it called and no lump. Above the third-order tier, the 28 fourth-order themes say the rooms organized mostly without deciding how: decided order reaches 46 rooms, and repair and the completion ritual each reach more than 520.

- **The room that best supports it: naruto t04.** It holds two acts toward other rooms, help (T3-011, ten concepts) and alliance (T3-150, nine). Under the revised rules each act has concepts of its own, help is read from either room's record (gate:27), and the line places both. The revision left this line as it was and gave a reason for every theme on it.
- **The room that most threatens it: greenlattice t03.** More than ten concepts ask for peace or a pact, and the room's talk runs over borders, truces, alliances, barter, help, restraint and appeals. Nine themes have three concepts or more, so the line is a bag: T3-010 is placed on six concepts, and eight others sit under `also_present` with four or five each. J ruled that a bag is not cut. The line says the room settled borders, and most of what it did sits in a list beside the placement.
- **The condition that separates them** is how a room's acts spread over themes. Where a room does two or three things, each with many concepts, all of them are placed and the lean to one placement costs nothing. Where a room does many things, each with a few concepts, the bag rule places one and lists the rest. A reader of `assignments_final.jsonl` who ignores `also_present` will read such a room as narrower than it was.

## The counts

The next table gives stage C1's figures, each with where it is recorded.

| what | figure | where |
|---|---|---|
| lines of `assignments_final.jsonl` | 7,844, equal to `counts.py`'s `assignment_items_expected` (7,844) | `assignments_final.count.txt` |
| lines revised at C1 | 2,117 (2,175 move entries) | `assign_revisions_only.jsonl`; `scheme_v2.md`, by cause |
| placements | 10,593, against 13,365 on stage B's settled line | `c1_views_diff.py` |
| empty lines | 151 of 7,844 (1.9%), in 18 kinds | `out/_analysis/c1_empties_kinds.json` |
| the revision rate | 73 of 200 placed differently from the current line (36.5%); primary agreement 0.845; 34 errors, 29 moved and 5 unapplied; seed 20261013 | `out/_analysis/c1_revision/` |
| the corpus arguable rate | 0.613 (4,709 of 7,677 placed lines) at the pair test | `out/_analysis/c1_pair_test.json` |
| pairs carried by ten lines or more | 78; 76 materially above the corpus rate (bar 0.713) | the same |
| the 76 pairs called | 75 joints, 1 unresolved (T3-010 \| T3-149), 0 lumps | `out/_analysis/c1_pair_calls-*.json` |
| the arguables | 4,876 lines (rate 0.614 among placed lines at pass 8) | `out/_analysis/c1_arguables_list.md` |
| stage B1's prediction | held at the top: T3-005 \| T3-021 first of 922 confused pairs; 8 predicted pairs in the top 10, 13 in the top 20; five missed (#4, #7, #16, #17, #19) | `notes-C1.md`, pass 8 |
| gates amended | 35 sentences in 18 themes; 1,297 rechecks; two escalated (gate:6, 35 of 124 moved; gate:30, 23 of 183) | `gate_history.jsonl`, `rechecks-C1.jsonl` |
| tier changes | 1 theme moved to rare (T3-140); none added, split, merged or retired | `tier_history.jsonl` |
| fourth-order themes | 28 over 195 of 197 third-order themes; 2 unpicked | `fourth/fourth.jsonl` |
| form-pass findings | FP-01 to FP-08, never counted and never clustered | `form_pass-C1.md` |

## The recurring pairs, and what each became

Stage B3's pair table has 20 rows, 19 distinct pairs (T3-005 | T3-021 appears both ways). At C1, 17 were called joints and kept; the theme on each side has concepts of its own. T3-010 | T3-149 is the one unresolved pair, though gates 15, 16, 18 to 21 and 33 rewrote its sentences. T3-006 | T3-068 owed no call: its arguable rate, 0.708, sits under the bar. The two modifier candidates, T3-089 and T3-152, are not folded. Each is a second act that travels with its partner, called a joint with it, and J's floor already took off its additions under three concepts (`out/_analysis/c1_recurring_pairs-C1a-11.txt`).

## Transmission after revision, as stage B4 measured it

Stage B4 measured whether fresh readers holding only the frozen scheme reach the settled line. The figure is the mean Jaccard of each fresh reading against the settled set, over readings whose settled line is resolved, in two arms never pooled. Fresh against settled: arm 1 (DeepSeek) 0.657 on the uniform stratum and 0.544 on the adjudicated one; arm 2 (OpenAI) 0.622 and 0.554 (`transmission-after-revision-B4.md`). It bounds whether the written instrument decides, not whether it is right.

**It no longer describes the instrument stage C1 hands on.** It was measured with `scheme_final.jsonl` against `assign_final.jsonl`. Stage C1 amended 35 sentences in 18 themes, which no blind reader has seen. It also replaced the settled line in 2,117 of 7,844 lines, 1,990 of them by the class 2 ruling, which removed the B1 themes stage B4 found depressing the uniform figure. **The write-up should report stage B4's figure as the transmission of the frozen scheme against stage B's line, at stage B4, and say that scheme v2 and `assignments_final.jsonl` have no transmission figure.** One comes only when fresh readers test the revised scheme, which J ruled for after C1. I did not recompute stage B4's figure against the new line. The revision rate is my agreement with the line, not transmission.

## The form pass

Eight findings, FP-01 to FP-08, live in `form_pass-C1.md` and nowhere else. Stage C2 takes them from that file, by id. Their unit is the turn. They were never counted and never clustered, and no gate was written for them.
- The cheapest act is the one-line reply ("On it.", "Done.", "Agreed"): 590 concepts in 337 rooms.
- The edited post keeps a running record (418 rooms).
- Rooms time the work by who is awake (219 rooms).
- The vocabulary of state and war is the common speech of canvas work (4,759 concepts in 571 rooms, 145 line themes).
- The post speaks as "we" and the reply as "I".
- The canvas's large collectives are named as known actors; no one asks what the void is (453 rooms).
- A room's question to itself, posted as a submission, is answered least (37.7%).
- Who leads is neither asked nor named.

What the pass could not reach (stance, acts named by topic, dropped items, timing, case, language, links, who answers whom, the week before) is listed in both `form_pass-C1.md` and `notes-C1.md`.

## The fourth-order themes

28 constructs over 195 of 197 third-order themes, each cut from a written story with a grounded gloss, a declaration and a disconfirmer (`fourth/fourth.md`). 13 are borrowed, 14 adapted and 1 coined (Visibility returns). 22 cuts were merging and 6 relating. Unpicked, and listed rather than gathered: T3-017 (the sub's ordinary talk, the ground boundary work protects) and T3-133 (one hacked sub). No dimension was cut; that is stage C2's.

## For stage C2, and the stages after it

- **The forced placements.** 13 third-order themes could sit in two fourth-order themes. `notes-C1.md` (pass 10) lists where each went: T3-076, T3-061, T3-169, T3-188, T3-058, T3-159, T3-090, T3-153, T3-172, T3-173, T3-081, T3-130 and T3-141. They are the first candidates for a recut.
- **Thin constructs.** Decided order (48 lines in 46 rooms), Neo-tribes (56 in 35) and Symbolic boundaries (54 in 49). Stigmergy rests on two large themes, building and extending, which could be read as plain production.
- **27 recalled sources for stage C3.** Every borrowed or adapted fourth-order theme names a source I recalled; stage C3 verifies or withdraws each:
  - T4-001 Keying: Goffman (1974), Frame Analysis; Bateson (1972), A theory of play and fantasy.
  - T4-002 Boundary work: Gieryn (1983), American Sociological Review.
  - T4-003 Sensemaking: Weick (1995), Sensemaking in Organizations.
  - T4-004 Frame bridging: Snow, Rochford, Worden and Benford (1986), American Sociological Review.
  - T4-005 Mobilization: McCarthy and Zald (1977), American Journal of Sociology.
  - T4-006 Collective representation: Durkheim (1912), Les formes elementaires de la vie religieuse.
  - T4-007 Stigmergy: Grasse (1959), Insectes Sociaux; Heylighen (2016), Cognitive Systems Research.
  - T4-008 Standardization of output: Mintzberg (1979), The Structuring of Organizations.
  - T4-009 Workarounds: Gasser (1986), ACM Transactions on Office Information Systems.
  - T4-010 Backstage decision-making: Goffman (1959), The Presentation of Self in Everyday Life.
  - T4-011 Decided order: Ahrne and Brunsson (2011), Organization.
  - T4-012 Collective efficacy: Bandura (1997), Self-Efficacy; Bandura (2000), Current Directions in Psychological Science.
  - T4-013 Repair work: Jackson (2014), Rethinking repair, in Media Technologies.
  - T4-014 Territoriality: Brown, Lawrence and Robinson (2005), Academy of Management Review.
  - T4-015 Live and let live: Axelrod (1984), The Evolution of Cooperation; Ashworth (1980), Trench Warfare 1914-1918.
  - T4-016 Negotiated order: Strauss (1978), Negotiations; Strauss and colleagues (1963), The hospital and its negotiated order.
  - T4-017 Reciprocity: Gouldner (1960), American Sociological Review.
  - T4-018 Meta-organization: Ahrne and Brunsson (2008), Meta-Organizations; (2005), Scandinavian Journal of Management.
  - T4-019 Attribution: Heider (1958), The Psychology of Interpersonal Relations; Kelley (1967), Nebraska Symposium on Motivation.
  - T4-020 Repertoire of contention: Tilly (1978), From Mobilization to Revolution; Tilly (1995), Popular Contention in Great Britain.
  - T4-021 Rivalry: Kilduff, Elfenbein and Staw (2010), Academy of Management Journal.
  - T4-022 Flagging the nation: Billig (1995), Banal Nationalism.
  - T4-023 Neo-tribes: Maffesoli (1996), The Time of the Tribes.
  - T4-024 Symbolic boundaries: Lamont and Molnar (2002), Annual Review of Sociology.
  - T4-026 Completion ritual: Collins (2004), Interaction Ritual Chains; Durkheim (1912).
  - T4-027 Collective memory: Halbwachs (1950), La memoire collective; (1925), Les cadres sociaux de la memoire.
  - T4-028 Transition: Lundin and Soderholm (1995), Scandinavian Journal of Management.
- **The watch items** of `scheme_v2.md`:
  - osugame t04, where T3-063's gate:23 and T3-090's must show overlap;
  - the named words of T3-010 | T3-149 against FP-04's finding that war words are the common speech, even for builders;
  - the unresolved pair T3-010 | T3-149;
  - two boundaries barred from a third sentence, T3-033 | T3-041 and T3-002 | T3-005.
- **Five errors no C1 verb applies** (`out/_analysis/c1_unapplied.jsonl`, QC1-003). They count in the revision rate and stay as found until J opens a verb.
  - harrypotter t11: empty the line (now T3-001). A bare April Fools greeting image; no act any theme takes.
  - tampabaylightning t08: empty the line (now T3-023). A header change is noticed, and nothing shows it is an April Fools change.
  - heroesofthestorm t11: place T3-005; list T3-021, T3-070 and T3-087 under `also_present` (now T3-021). A bag.
  - stevenuniverse t02: place T3-038; list T3-009, T3-073 and T3-082 under `also_present` (now T3-009, T3-038). A bag.
  - radiohead t04: place T3-010; list T3-011, T3-072, T3-149 and T3-084 under `also_present` (now T3-011, T3-084). A bag.
- **Twenty placements kept as found** (`out/_analysis/c1_pair_carried_decisions.json`). The pair test's samples found them; correcting only sampled lines would treat them unlike unsampled ones. 12 sit on the two barred boundaries, 2 are gate:27 items outside its recheck sample, 5 are defensible readings, and 1 (de t08) is an error that leaves its themes and order unchanged.
- **Four kinds the scheme lacks** (pass 8's empties): April Fools play that stages no fake (17 lines in 15 rooms); another sub's April Fools change seen from this room (8 in 8); the sub's own moderation outside the canvas (8 in 7); disputes over the room's own jokes (4 in 4). No theme was added at C1: a new theme would change the instrument after the readers ran, and J's rule for re-reads would still leave these lines empty.
- **Rule 0 departures, measured and not swept.** 104 multi-theme lines put a theme with fewer concepts first, most by a decide-when-both that names the primary. 1,069 hold a later theme under three concepts, J's lean.
- **Carried from B1.** The ruling on testing G13, G14 and G15 as one index page; the bag count (J counts 841 B1 bags, an older head said 846, not reconciled).

## The licences exercised

- **FLEET.md's licence on every figure:** it bounds whether the written instrument decides, not whether it is right.
- **Stage C1's licence to change the scheme.** I used it once: T3-140 moved to the rare tier (the event moved_to_rare, its floor under stage B1's two rooms unlike each other). No theme was added, split, merged or retired.
- **J's rule of 11 October on amended gates.** 35 gate sentences amended with `mem.py gate`, each with its rechecks, two escalated to every placement they could move.
- **J's rulings for C1.** The class 2 ruling: the readers' list stands, and B1 themes no reader placed are a flagged record; one flagged record was promoted where its concepts supported it. No fleet re-read. QC1-001: rechecks placed each item by the amended gates over the whole scheme, and the guard counted each pass's moves to a theme neither reader nor my B1 placed. The count was 0 at pass 1, 33 at pass 2 (32 of them onto T3-084: under gate:6 and the visitor rule, another room's request for help arriving in this room's threads is a request, not this room's help, and no reader had placed T3-084 there), 11, 8, 6 and 4 at passes 3 to 6, and 0 at passes 7 to 10: 62 in all (`c1_guard_moves.py`). QC1-002: lean to one placement at three concepts. QC1-003 (the handler's ruling under J's delegation): no verb opened.
- **My choices under J's latitude.** The lone-B1 floor for class 4, revised at pass 4 to apply only where the readers' theme takes concepts (J: "whatever the agent feels more comfortable with"); 16 empties placed under it at pass 8. The reading rules, the visitor rule first, which J left to me. The stopping criterion, declared before the first recut.
- **Rule 5's carve-out for the form pass.** The findings travel on exemplars and never enter the arithmetic.
- **Contract section 2's naming of constructs.** Each fourth-order theme was named as a construct when cut and declared borrowed, adapted or coined, every source marked recalled for stage C3.
