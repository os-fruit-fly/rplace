# Notes, stage C5 (the account)

## The criterion (section 5), written before pass 1

Written at C5a-01, 2026-10-14 (UTC), before any pass of the account exists. I will prefer a later account to an earlier one when all of the following hold.

1. **It states fewer untested claims.** Every sentence that says one thing brings about another rests on an arrow whose order count beats its null, on a finding, or on a test that could have failed. Any other causal sentence is marked theorised or thin. The later account has fewer unmarked causal sentences than the earlier one.
2. **It tells at least as much with no more elements.** The story rooms of passes 1 to 5 (`story_rooms-p5.jsonl`: 16 told, 19 told with a residue, none untold) are the first test. The later account tells at least as many of them without a residue, using the same or fewer elements at the top.
3. **It keeps every tested arrow.** An account that drops an arrow whose order count beats its null, in order to read more simply, is rejected.
4. **More names pass the prose test.** In the later account, more fourth-order themes and dimensions do theoretical work in a sentence of the form "because the room had X, Y could happen".
5. **At the check legs, the readers recover more of what I meant.** The readers recover more of my claims in `author_claims.jsonl` and fewer claims I did not write.

I reject a later account that gains reach by loosening an element, by a sentence that no count or quote supports, or by a claim the readers recover that I did not intend. When the criteria conflict, the order above is the order of priority.

## J's rulings of 15 October (01:29 Berlin), as the handler relayed them

1. **Work after hour 73 is curation.** Organizing to make the artwork ends at hour 73. After it, members curate: they clean, copy, record and argue over which version of the canvas and of the event is kept. The account tells this as curation of the record (P12, with P22 tentative), apart from carrying on (P13), and not as a fourth part of making the work.
2. **The declaration prose pass comes first, in this pass.** The rule is written first. Each of the 28 declarations is read against its members' quotes, starting with Stigmergy, Completion ritual, Live and let live and Mobilization. Each amendment is logged as a move. A cut moves only where the members' quotes force it.
3. **The two sources for Stigmergy.** Heylighen (2016) and Grassé (1959) are in `out/sources-from-J/`. I read both whole before amending Stigmergy, and mark each claim I take from them verified, with its page. I recut Stigmergy only if, as cut, it joins things the field keeps apart.
4. **The second reader is stage C5's three readers.** The rule and the amended declarations go into the C5b packets with the quotes each declaration rests on, and the readers' disagreements are recorded.
5. **J's language ruling stands.**

QC4-002: the renamed link `out/_field-link-superseded-C4a` stays as it is, and I read the field only from `out/field`.

## The declaration prose rule, written before the pass

Written at C5a-01, 2026-10-14 (UTC), before I read any declaration in this pass.

**What the rule reads.** In each of the 28 construct blocks in `fourth/fourth.jsonl`, the rule reads every sentence of the `prose`, `changed` and `mistaken_for` fields that says something about these rooms or their members. A sentence about a source construct, saying what Gieryn or Mintzberg holds, is about the literature. It is read only for its mark, verified or recalled.

**Which sentences are in question.** A sentence is in question when it is:
- **universal:** every, all, no one, nothing, never, always, any, only;
- **comparative:** more, most, less, fewer, strongest, than, as much as;
- **causal:** because, so, makes, brings, turns into, leads to, keeps alive, why, explains, or a verb that gives one act as the cause of another;
- **cyclic:** again, each time, returns, renews, a loop.

**When a sentence in question stands.** It stands only if one of these supports it:
- an order count in `model/arrows.jsonl` that beats its null;
- a line in `findings.jsonl`;
- a count in `structure-C4.md` (rule 5's three numbers, or the rooms carrying a theme);
- a fact of the setting as the contract states it. The setting facts are: one pixel per interval for each account; anyone may change any pixel; placement stopped at hour 73; no one holds authority over another's placing.

**Otherwise the sentence is rewritten.** The new sentence says what members did, in how many rooms, in the members' own terms. Each act it names must be shown by at least one member's quote. The quotes are the exemplars and material in `structure-C4.md`, and for the first four declarations a further seeded draw through `cite.py`.

**What does not change.** Names, members and the cut do not change, unless the members' quotes show that the theme joins acts the declared construct keeps apart. A recut needs that showing, written down before it is made.

**How each amendment is recorded.** Each amended declaration gets one `tier_history.jsonl` line with the old line as `was`. It is logged with `mem.py log --kind move`, naming the move:
- **developing or dropping working hypotheses,** when an untested claim is dropped or rewritten as a description;
- **relating or contrasting,** when the amendment compares the theme with a source.

Each amendment is snapped as `C5 move-<move>-<n>`.

## Stigmergy against its sources: the rules for an abductive read, written first

**The question.** J's question is whether Stigmergy, as cut, joins things its sources keep apart. Both sources separate coordination through the work itself from communication between members:
- Grassé (1959, pp. 65, 74 to 75);
- Heylighen (2016, pp. 9 to 10).

Heylighen admits a shared record of the work's state, kept with markers, as a stigmergic medium (p. 9). The record of my rooms holds only talk. So the test reads what the talk under each member of Stigmergy does.

**The sample.** For T3-038 (building and reporting the mark) and T3-041 (extending the room's work), 24 records each, drawn from the store with seed 20261015, at most two per room. For T3-060 (adding a personal piece), every record, up to 24. Each record is read whole.

**The codes.**
- **M, the trace or a marker.** The member reports the state of the work to the thread (what is placed, done, missing, or where). Or the member says they acted on what the canvas showed. Or the member points others to the canvas's state.
- **MP, a proposal grounded in the trace.** The record proposes an addition and names, in the same record, the state of the canvas that prompts it. It counts with M, since the trace is "an opportunity for advancement" (Heylighen 2016, p. 8).
- **P, a proposal or request.** The member proposes, asks, invites or instructs other members or another room about what to add, where or how. The record names no state of the canvas that prompts it.
- **O, other.** A celebration, a call for hands, upkeep, a joke, or talk off the work.

**The decision rules.**
- A member joins what the sources keep apart if P is at least half of its records that are not O.
- **If T3-041 meets the rule,** it moves to Collective representation, where proposals of what the mark shows already sit (T3-033, T3-004). Its C1 note named that as the alternative.
- **If T3-038 meets the rule,** I report it. The theme would need a third-order split, which reassigns second-order themes, and I do not make it in this pass.
- **If no member meets the rule,** Stigmergy keeps its cut. Its declaration then says that the record holds talk that registers the state of the work, and members' words about reading the canvas, not the placing itself.

**The result.** No member met the rule.
- T3-038: P in 5 of the 15 records that are not O.
- T3-041: P in 8 of 17.
- T3-060: P in 8 of 20.

Stigmergy keeps its cut. T3-041 is close: one doubtful code would move it to 9 of 17 (`c5_stigmergy_codes.json`, "doubtful"). Across the three members, 31 of 52 records report the work's state or act on the canvas, and 21 propose or ask what to add. The amended declaration says both. Coded by me alone. The C5b readers check the prose against these quotes.

## Pass 1 (C5a-01)

**What the pass did.**
- **The declaration prose pass.** All 28 fourth-order declarations were read against their members' quotes and amended under the rule: `prose`, and `changed` and `mistaken_for` where they made claims. Each amendment is a `tier_history.jsonl` line, a logged move and a snap (C5-move-relating-53, C5-move-developing-54 to 80). No name, member or cut changed.
  - **What the pass dropped.** These sentences made causal claims with no count behind them ("explains", "turns ... into", "pays"), universal claims ("every", "no one", "only"), uncounted comparisons ("most", "constantly"), and figures of speech.
  - **What replaced them.** Each declaration now gives its acts with their rooms, the counted orders that touch it, and its sources marked recalled or verified.
  - **What the run's own tests contradicted.** Attribution called itself the hinge between restraint and attack. Collective efficacy said doubt shapes whether hands come. Both claims were tested and not found.
- **Stigmergy.** I read its two sources whole, and the abductive read above kept its cut.
- **Rule 14.**
  - mapping-C3.jsonl was corrected in place for Attribution, Visibility returns and Completion ritual.
  - F-016 was superseded, because Completion ritual is now mapped to reward by reading, not by construction. No count changed.
  - A21 got the `negative_check` the arrow checks require.
- **The account, the prose test and the sketches.** `account.md` was drafted from the pass 5 story, with curation after hour 73 apart from carrying on (J's ruling 1). `prose-test-C5.md` passes all 36 names and flags four. `sketches.md` holds three arrangements.

**What the criterion says.** Prefer, against the pass 5 story as the first draft.
- **Unmarked causal sentences: fewer.** The story said, unmarked, that one-line answers are "how a room with no membership list sees its numbers", which F-015 failed. The account marks each thin or theorised arrow, and the declarations it rests on no longer carry untested causal sentences.
- **Rooms told: unchanged.** The account names the same 19 rooms the story told with a residue, and I did not read the story rooms again in this pass.
- **Tested arrows: all kept.** All 18 counted arrows are in the account.
- **The prose test:** all 36 names pass. There is no earlier test to compare against.
- **Readers:** not applicable before the check leg.

**Section 4, simplification: nothing cut in pass 1, three candidates.** P06 (attribution), K01 (the April Fools frame) and R02 (the envoy) are standing elements with no arrow.
- **Cutting P06** loses the model's statement that members work out who changed their work (155 rooms). The account could still say the step was tested and not found.
- **Cutting K01** loses the condition the odd room runs inside. F-009 would carry the finding that the frame did not delay the work.
- **Cutting R02** loses the named role. P08 already holds envoys.

Each cut would lower the count of elements and might add residue at the return, since the rooms still carry these acts. I decide in pass 2, after the account is cut toward two pages and the story rooms are read against it.

**Section 5, recuts: none in pass 1, three candidates from the sketches.**
- **P08 (border talk)** holds both terms offered before any damage (day9 at h33.9; the field's buffer at h5) and talk after erosion (A04). The test for pass 2 is to read P08's first concepts in the 166 rooms where A04's order fails, and count those that offer terms before any damage.
- **P05 (upkeep)** sits in two places in two drawings. I read this as the spine passing through it, and I check it again in pass 2.
- **P10 (the move)** ends a fight and starts new work, and no counted arrow returns from it to building. This is not a recut. It is the loop the model cannot ground.

**Limits of the pass.**
- **Fields outside the rule's scope.** The rule read `prose`, `changed` and `mistaken_for`. It did not read the `adaptation` field, the `disconfirm` field, or the question each theme answers. Some of these still hold sentences the rule would flag, such as Completion ritual's question "How a room pays members no one could pay". `structure-C4.md` still prints them, and its prose lines are now stale beside `fourth/fourth.jsonl`. For the C5b packets I generate the declarations from the ledger, not from `structure-C4.md`.
- **The dimensions.** The eight dimension declarations were not read under the rule. D03 Maintenance says attribution decides between repair, forgiveness and retaliation, which the run's test contradicts. Pass 2 reads the eight under the same rule.
- **The record cannot show who placed a pixel.** I first wrote that no one could see who placed a pixel. That was a claim about the setting the contract does not state, and it is withdrawn wherever it appeared (Attribution, mapping-C3.jsonl).

**Slips, C5a-01.**
- **Two parallel writes to the same files.** Two amendment scripts that write `fourth/fourth.jsonl` and `tier_history.jsonl` (T4-015, T4-005) ran as parallel calls. Both writes landed, and the harness appears to have run them one after the other. Snap C5-move-developing-55 may or may not include T4-005's change.
- **Writes and their checks in one turn,** twice: the mapping Edit and the C3 validator, and the prose test's Write and its word count.
- **A malformed field.** The superseding F-016 line first carried `supersedes: 'F-016 (C3c)'`. The check refused it. It was fixed in place, and the writing script was fixed too.
- **A read twice.** The account's 44 quotes were served twice, once to measure the output and once to read it.
- **A wrong format for tier events.** The pass 1 line first listed tier events as 'ledger:id:event' strings. The check resolves ids, so the line was rewritten with the ids, and the writing script was fixed.
- **A no-op command.** One shell call only printed a word, which breaks the rule against no-op commands.
- **A hedge in the account.** The account said "in some rooms" for C02. It now gives F-013's count.
- **Parallel edits to one file, at the close.** The head's last four Edits ran as parallel calls. Each changed a different passage, and each reported success. The head was checked afterwards in a turn of its own.

## Pass 2 (C5a-02): the rule extended to the dimensions, written before reading them

Written at C5a-02, before I read any dimension declaration under the rule.

**The scope.** The declaration prose rule above now also reads the eight dimension declarations in `dimensions.jsonl`. It reads every sentence of the `construct` block's `changed` and `mistaken_for` fields that says something about these rooms or their members. The `question` and `predicate` fields define what the dimension gathers. They are read only for a claim about the rooms stated as fact.

**What stays the same.** The word classes, the four supports, the rewrite and the record are as in the rule above. A dimension amendment is a `tier_history.jsonl` line with `tier: dimension`, the old line as `was`, a logged move and a snap. Names and members do not change unless the members' declarations show that the dimension joins what its source keeps apart.

## Pass 2: the P08 question, rules written before the read

**The question.** Does border talk (P08) hold two things: terms offered before any damage, and talk after damage? The sketches put P08 in two places. In day9, members offered terms at h33.9, before any loss. A04 holds border talk as what follows upkeep.

**What a result can change.** Stage C5 forbids a new element, so P08 cannot become two elements. Both kinds of talk settle order between two rooms by talk, which is what Negotiated order (T4-016) declares. They differ in when they come, not in what members do. So a recut of the tier by kind is not in question. A result can change only A04's bound, by giving it a count.

**The read.**
- **The rooms:** those carrying both P05 and P08 in which A04's order fails, so that the first concept of P08 comes before the first concept of P05 (`c2_first_concepts.py --pair P05:P08 --rooms BOTH --fails --n 1`, on `c2_elements_p4.json`).
- **The sample:** 40 rooms drawn with seed 20261015, and the first P08 concept of each, read whole.

**The codes.**
- **T, terms before damage:** a member proposes or asks for a border, space, a truce or a deal with a neighbour, and the concept names no damage to the room's own work.
- **D, talk after damage:** the concept names damage to the room's work (overrun, covered, attacked, encroached), or answers it.
- **O, other:** news of other rooms' deals, disputes about who speaks for a room, and anything else.

**The rule.** If T is at least half of T plus D, A04's bound says that where border talk comes first it mostly offers terms before any damage, with the count. If D is more than half, the bound says that in those rooms damage came before any upkeep was coded.

## Pass 2 (C5a-02): what the pass did

- **The dimensions.** Under the extended rule, seven of the eight dimension declarations were amended (moves C5-move-developing-81 to 87). Host framing (D06) needed nothing. The dropped sentences:
  - Maintenance said attribution "decides between quiet repair, forgiveness and retaliation", which the run's test contradicts.
  - Critical mass said the room "reads it off the canvas and the thread", and F-015 found that members did not read their numbers from the replies.
  - Contention said "the repertoire is learned in hours" and "often played for sport", with no count behind either.
  - Collective identity said membership was "mostly carried in", which was uncounted and now carries its rooms.
- **The P08 test.** Rules were written first, and the first border talk was read in 40 of the 166 rooms where A04's order fails.
  - T 34, D 4, O 2. With every doubtful code turned against the reading, T is 28 of 38.
  - Where border talk comes first, it mostly offers terms before any damage.
  - A04's bound now carries the count (C5-move-relating-88). P08 stays one element: a new element is forbidden, and the two kinds of talk differ in time, not in kind.
- **Three cuts (section 4).** P06, K01 and R02 changed from standing to candidate (C5-move-dropping-89 to 91). Each carried no arrow, against the model's own rule that a process or condition enters only with one. What each cut cost:
  - **P06 (attribution):** the model no longer says that working out who changed the work is part of organizing. The step was tested twice as the step between restraint and attack, and was not found.
  - **K01 (the April Fools frame):** the model no longer names the frame the odd room ran inside. F-009 keeps the finding that the frame did not delay the work.
  - **R02 (the envoy):** the model no longer names the role. P08 still holds deals made through envoys.
  - **Local adequacy.** Under the A1 rule, April Fools talk and blaming or wondering hold no coordinating turn. The envoys' theme sits in Negotiated order, which P08 reaches. So no coordinating turn is left unreached.
  - **The count.** 22 elements stand, against 25 before. Every standing process and condition now carries an arrow.
- **Elements kept over an alternative (section 4).**
  - P08 is kept whole rather than split into terms and talk after damage. A split would be a new element, and the test showed a difference of time.
  - P05 is kept whole: the sketches put it in two places, but the spine passes through it (A03 in, A04, A06, A13 and A19 out).
  - K02 is kept although its one arrow is thin. Without it the model has no conditions side, and the move (P10) has no counted cause.
- **The propositions (section 6).** Nine are in `propositions.jsonl`. Three are thin (N07, N08, N09). One rests wholly on theorised arrows (N07). Two carry a mechanism from the literature (N03, through A16; N07, through A12). Each carries its rival and what decides it, what would falsify it elsewhere, and its boundary. No proposition carries A21.
- **The account, pass 2.** It is 1,631 words, with pass 1 kept as `account-p1.md`. It states the four differences the prose test asked for, ties each part to its proposition, and names the three cut elements as out of the model.
- **A sketch, the fourth arrangement.** The tier drawing after the cuts has a wide middle column and one condition. The figure must say so.

**What the criterion says: prefer pass 2 over pass 1.**
- **Unmarked causal sentences: fewer.** The dimension declarations lost their untested causal sentences. The account marks every thin and theorised arrow. Each proposition names its rival.
- **Rooms told: unchanged, with fewer elements.** The account names the same 19 rooms with a residue, now with 22 standing elements against 25.
- **Tested arrows: all kept.** No counted arrow was dropped, since the three cut elements carried none.
- **The prose test:** all 36 names still pass, and the four differences are now stated.

Pass 2 changed three elements' status, so by section 7 another pass is due before the packets.

**Slips, C5a-02.**
- **Proposition ids.** They were first written as N1 to N9, and the check requires N01. The keys were renamed by script and the file rewritten. I had not read the id pattern first.
- **Parallel edits.** Two Edits to `account.md` ran as parallel calls. Both landed, and a later turn checked them.
- **Proposition ids in the head.** The head first named N01 to N09, which the link check does not resolve. They were replaced by the propositions' names before the close.

## Pass 3 (C5a-03): the cuts read against the story rooms

**What the pass did.**
- **The scan.** I scanned the 35 pass 5 story rooms (`story_rooms-p5.jsonl`) for tellings that used a cut element, by id and by the words that stood for each: attribution, tracing and blame for P06; April Fools and prank for K01; envoy, diplomat and ambassador for R02.
- **What it found.**
  - **K01:** the April Fools frame is told through K01, beside the work, in 16 story rooms. Ten of them are among the 16 told with no residue: ubc, ultrahardcore, CKCrusaders, cardinals, completeanarchy, lakers, rpi, unitedkingdom, NieR and bannedfromanime_irl. For example: "The April Fools swap with SFU runs beside the work" (ubc).
  - **P06:** no telling rested on it.
  - **R02:** no telling rested on it. One residue room, starcitizen, names an ambassador, and it carries a residue for another reason.
- **What would follow from the K01 cut.** With K01 out of the model, the frame in those ten rooms would be residue, as Visibility returns was carried as residue at C2. The account would then tell 6 rooms with no residue, not 16.
- **The decision.** The criterion, written before pass 1, ranks rooms told without a residue above fewer elements. So the K01 cut is reversed (C5-move-developing-92), and K01 stands again with no arrow. P06 and R02 stay cut. 23 elements stand.
- **The pass 2 line.** It now records K01 under `cut_then_reversed`, with the pass that reversed it.
- **The account and the sketch.** The account tells the frame beside the work (368 rooms, 88 testing whether a post was meant; F-009) and names K01 in ultrahardcore. The fifth arrangement in `sketches.md` shows the conditions side with K01 and K02.

**What the criterion says: prefer pass 3 over pass 2.** The tie goes to its second item. Pass 3 tells the same 16 story rooms with no residue as the pass 5 story. Pass 2's cut would have turned ten of them into rooms told with a residue. The cost is one more element.

**Section 4, kept over an alternative.** K01 is kept over cutting it, for the reason above. A condition with no arrow is still a statement the model makes: the play ran beside the work in 368 rooms, and it did not delay it (F-009).

Pass 3 changed one element's status, so by section 7 another pass is due before the packets.

**Slip, C5a-02, found at C5a-03.** I cut K01 at pass 2 without first reading the story rooms against the cut. The criterion, written before pass 1, names the story rooms as its second test. I applied it after the cut, not before.

**Slips, C5a-03.**
- **A miscount.** The pass 3 notes first said the frame is told in 17 story rooms. The scan printed duplicate lines, and a script then counted 16.
- **Parallel edits.** Two Edits to the head ran as parallel calls. Both landed, and a later turn checked them.

## Pass 4 (C5a-04): the rule that decides whether an element stays

**The handler's point, not a ruling.** In pass 2 I cut P06, K01 and R02 under the model's rule that a process or condition enters only with an arrow. K01 now stands with no arrow. Say which rule governs, and why, so that the C5b readers see it.

**The answer.** The criterion written before pass 1 decides whether an element stays. The arrow rule decides only what the account may say an element brings about.
- **Why the criterion.** Section 4 sets the count of elements "by what keeps composition and explanatory power alive", with why in this file. Section 5 asks for the criterion before the first pass, and a criterion written after the passes is not one. The criterion ranks story rooms told with no residue (item 2) above a smaller count of elements. The arrow rule is not one of its items.
- **Why not the arrow rule.** The model stated it ("Each process and condition enters only with a grounded arrow", `model-C4.md`) and did not keep it. K01 stood with no arrow from C2's first pass (`model.md`: "a condition with nothing tested from it"). `model-C4.md` lists five standing elements with no arrow: P06, K01, C01, C02 and R02. A rule the model broke from its first pass cannot decide a cut alone.
- **What the arrow rule still does.**
  - It names the candidates. An element with no arrow is the first read for a cut, as P06, K01 and R02 were at pass 1.
  - It limits what the account says. An element with no arrow is told by what members did, and no effect of it is claimed. The account tells K01 that way: the play ran in 368 rooms, and F-009 found no delay of the work (59 frame-filled rooms against 275, permutation p 0.43).
- **How the three cases fall under it.**
  - P06 and R02 carry no arrow, and no story telling rested on them. Cutting them costs no room told, so the criterion prefers the smaller model.
  - K01 carries no arrow, and ten of the 16 rooms told with no residue tell the frame through it. Cutting it costs ten rooms told, so the criterion keeps it.
- **Where pass 2 went wrong.** Pass 2 used the arrow rule as if it decided the cut, and read the story rooms after. That slip is recorded under pass 3. The pass 2 line "Every standing process and condition now carries an arrow" stopped holding at pass 3.
- **Where the readers see it.** `account.md`, in its last section, has the paragraph "The cuts, and the rule that decides whether an element stays". The sentence in `model-C4.md` stays as written, since that is a C4 file. `account.md` is the final version of the model's explanation, and it states the rule as it now stands.

**What else pass 4 read.**
- **Cuts I suspect (section 5).** None beyond those read. P06 and R02 were read against the story rooms at pass 3. K03, K04 and P19 are candidates from C2, and nothing in passes 1 to 4 bears on them.
- **The four flagged names.** Only Live and let live is named in the account, and its difference from an explicit truce is stated. Critical mass, Reciprocity and Collective efficacy are not named in the account. Each passes the prose test, so none is recut.
- **Changes.** No element, arrow, tier or finding changed. No sketch was tried: the fifth arrangement still holds. The pass 3 account is kept as `account-p3.md`, and `account.md` is 1,869 words.

**What the criterion says about pass 4: no change.**
1. **Unmarked causal sentences.** None added. The new paragraph says what decides a cut, and it claims no effect of K01.
2. **Rooms told.** The same 16 story rooms are told with no residue, with the same 23 elements.
3. **Tested arrows.** Every arrow is kept.
4. **The prose test.** Unchanged: 36 names pass, and 4 are flagged.
5. **The readers.** They have not read the account yet.

**The passes stop.** Pass 4 changed no element and no cut, so by section 7 the passes stop. I choose to move to C5b next.

**Slips, C5a-04.**
- **Parallel edits.** Two Edits to the head ran as parallel calls while I cut it below 3,000 words. Both landed, and a later turn counted the words and ran the link check.
- **The head's length.** The head first came to 3,118 words. I cut repeated lines until it was 2,995 words.

## The close-check, C5a-04

`python3 tools/validate.py C5`, run after the pass 4 line and before the head was rewritten:

```
stage C5:
  leg: build; passes 4, propositions 9, elements 30, arrows 21, history lines 94


0 errors (0 distinct shapes), 0 warnings
```

## The close-check, C5a-03

`python3 tools/validate.py C5`, run after the pass 3 line and before the head was rewritten:

```
stage C5:
  leg: build; passes 3, propositions 9, elements 30, arrows 21, history lines 94


0 errors (0 distinct shapes), 0 warnings
```

## The close-check, C5a-02

`python3 tools/validate.py C5`, run after the pass 2 line and before the head was rewritten:

```
stage C5:
  leg: build; passes 2, propositions 9, elements 30, arrows 21, history lines 93


0 errors (0 distinct shapes), 0 warnings
```

## The close-check, C5a-01

`python3 tools/validate.py C5`, run after the notes body and before the head was rewritten:

```
stage C5:
  leg: build; passes 1, propositions 0, elements 30, arrows 21, history lines 89


0 errors (0 distinct shapes), 0 warnings
```

`done.sh C5` runs the same check at the close. Its report is in the leg's closing diary line.
