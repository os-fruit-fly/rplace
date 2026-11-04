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

## C5b: the readers' build

**The manifest entry.** Stage C5's entry is in `run_manifest.json`.
- **The readers:** claude-opus-5-5, one per packet, through the Claude CLI, sent by the operator's `fleet.py`. There are three readers, and they run once.
- **Seeds and decoding:** the seed is 20261015 throughout, and the dispatch sets the decoding.
- **Pinned:** `account.md` (sha256 77b5e35d…), `figure-C5.md`, `propositions.jsonl`, `author_claims.jsonl` and `RETURN-C5.md`. The packets' hashes are added once they are built.

**author_claims.jsonl.** Nine claims, c1 to c9, each tied to its paragraph:
- c1: the order from a start to keeping the work;
- c2: the bare answer;
- c3: the mark tells members what is missing;
- c4: neighbours, and agreements no one can enforce;
- c5: the contest and how members answer it;
- c6: a template settles a design, and decided order is rare;
- c7: hour 73, and curation after it;
- c8: where the account does not reach;
- c9: the rule that decides whether an element stays.

**The three rooms (section 8), drawn by query.**
- **The side visited least.** `account.md` cites or names 7 early-side rooms and 2 late-side rooms (`c5b_room_sizes.py`). So the third room comes from the late side.
- **The rule, logged before the draw.** There are three pools, and one room is drawn from each with `random.Random(20261015)`:
  1. a pass 5 story room told with no residue, not cited or named in the account, with at least 8 coded passages (10 rooms);
  2. a pass 5 story room told with a residue (19 rooms; none was untold);
  3. a late-side room not cited or named in the account, not a story room, with at least 8 coded passages (43 rooms).
- **The rooms drawn:**
  - cardinals, from pool 1, with 102 coded passages;
  - luciomains, from pool 2, with 103 coded passages, on the early side;
  - mysterydungeon, from pool 3, with 54 coded passages; its first coded turn is at h52.62.
- **How the rooms are served, and why it changed twice.**
  - The first rule served each room whole: its facts, its forest and every quote, up to 4,500 bytes. No room in pools 1 or 2 fitted.
  - The second rule served each room's facts and 10 passages by `cite.py`'s seeded draw. The packets then measured 54,154 to 54,815 bytes.
  - The third rule, which is served, gives 7 passages per room. The forest's summary line is left out of the facts, since the forest is not served.
  - Each revision was logged before the pages were opened for content. Seven passages are a random sample of each room's record. A reader's paragraph on a room judges that sample, not the whole room. The size rule is a limit of the packet, not of the model.

**J's ruling 4 and the Stigmergy codes: the second reading.**
- **What fits.** Each packet holds `account.md` (10,839 bytes), `figure-C5.md` (5,032) and `propositions.jsonl` (19,202), with the instruction and the rooms, under 51,200 bytes. The 36 amended declarations come to about 40 KB before their quotes. They do not fit beside the rest, even split across three readers.
- **The declarations served.** They are read from the ledger (`fourth/fourth.jsonl`, `dimensions.jsonl`), not from `structure-C4.md`.
  - The rule is served: its reading parts, and the scope paragraph of the C5a-02 extension.
  - The 40 sentences of the 36 declarations that hold a word from the rule's lists are served (`c5b_in_question.py`). Quotes and citations are not searched for the words. These are the sentences the rule puts in question, and the reader says whether each stands.
  - Each declaration goes whole to one reader, split by bytes: reader 1 has 8 declarations (12 sentences), reader 2 has 9 (13) and reader 3 has 9 (15).
  - Ten declarations have no sentence in question and are not served: Keying, Sensemaking, Collective efficacy, Reciprocity, Neo-tribes, Completion ritual, Collective memory, Transition, Critical mass and Contention.
- **The Stigmergy codes.**
  - The 72 records drawn at C5a-01 are served, 24 per reader by member theme: reader 1 has T3-038, reader 2 T3-041 and reader 3 T3-060.
  - Each record goes through `cite.py` with its words, citation and hour. My codes and the coders' labels are not shown, so each reader codes blind.
  - The code definitions are served as written before the read; the decision rule is not.
  - The account states the result (31 of 52), so a reader may be anchored by it.
- **What is not served.** The whole declarations are not served, nor their sentences outside the rule's word lists, with the members' quotes those carry. The rooms' forests are not served either. J asked for the amended declarations with their members' quotes. The ceiling allows the sentences the rule puts in question, with the quotes inside them. I record this as a departure from the letter of the ruling and asked the handler (QC5-001). Meanwhile the packets go out as built.
- **The return.** `RETURN-C5.md` carries the stage's return line and two keys for the second reading: `declarations`, one verdict per sentence served, and `codes`, one code per record.

**Slips, C5b.**
- **Order.** The stage sets this order: the manifest entry, the claims, the rooms named in these notes, then `RETURN-C5.md` and the packets. I drew the rooms and wrote `RETURN-C5.md` before the manifest entry, and drew the rooms before the claims. The claims were written from `account.md` alone.
- **A no-op command.** I ran a command with an empty heredoc. It changed nothing.
- **Parallel edits.** Two Edits to `c5b_figure.py` ran as parallel calls. Both landed, and the script's output was checked after.
- **The figure named A21.** The paragraph on what the figure leaves out named A21 by id. The check reads every arrow id in the figure as drawn, so it reported two errors. The paragraph now names the arrow by its ends (P08 to P21). `figure-C5.md` was written again, the three packets were rebuilt, and the manifest entry's digests were read again.

**The packets as sent.** C5-reader-1 is 50,998 bytes, C5-reader-2 is 51,023 and C5-reader-3 is 51,040, under the 51,200 ceiling. Each carries the instruction verbatim and the end line, and none names these notes.

## C5c-01: the readers' check (pass 5)

**What came back.**
- **The returns.** J ran the dispatch at 07:06Z. There are three valid returns, one reader per packet, on claude-opus-5-5 through the CLI at its default effort, each about 10,000 output tokens. They are copied unchanged into `readers-C5/`. Each names reader `r1`, since the dispatch ran one reader per packet; the packet name keeps them apart.
- **What was served.** All three name `account.md` 77b5e35d…, the digest the manifest records. The dispatch's packet hashes and its return-spec hash match mine.
- **The size the dispatch printed.** About 54,000 bytes per packet is the packet with `RETURN-C5.md` served beside it: 50,998 + 2,970 = 53,968 for reader 1. The packet alone is under the 51,200 ceiling.

**Fidelity, both ways.** The three readers run on the same model as I do, so they share an architecture with me. Their recovery bounds whether the written account carries what I meant, not whether it is right.

| my claim | reader 1 | reader 2 | reader 3 |
|---|---|---|---|
| c1 the order from a start to keeping | yes | yes | yes |
| c2 the bare answer | yes | yes | yes |
| c3 the mark tells what is missing | no | no | no |
| c4 neighbours, and agreements no one can enforce | in part | in part | in part |
| c5 the contest and its answers | yes | yes | yes |
| c6 a template settles a design; decided order is rare | yes | yes | yes |
| c7 hour 73, and curation after it | in part | in part | in part |
| c8 where the account does not reach | no | no | no |
| c9 the rule that decides whether an element stays | in part | in part | in part |

- **Recovered.** All three recovered c1, c2, c5 and c6 whole.
- **Recovered in part.** All three recovered part of c4, c7 and c9:
  - c4: the talk with neighbours, but not that no one can make every placer keep an agreement;
  - c7: the curation after hour 73, but not that it is apart from carrying on and from making the work;
  - c9: the April Fools play beside the work with no effect claimed, but not the rule that decides whether an element stays.
- **Not recovered.** No reader recovered c3 or c8.
- **Claims they recovered that I did not write.** Three propositions that the account states and `author_claims.jsonl` left out:
  - the host's line (readers 2 and 3);
  - scripts under strain (readers 2 and 3);
  - the move after a loss (readers 1 and 2).

  Reader 3 read the host's line as an answer to a flood of calls. That is N05's stated mechanism, so the reading is intended. No claim that all three found is one I did not intend.
- **Relations.** Each reader listed all 20 arrows in the model with their direction. Readers 1 and 3 added K01 with no arrow. Reader 2 added C01 and C02 with no arrow, and no loop.
- **The defects behind the misses (author-error).**
  - c3: the paragraph led with the sample and the name, not the claim. All three listed Stigmergy among the terms they could not follow.
  - c8: the residue list said the account "cannot reach" rooms that the last story told in part, and luciomains, on that list, fitted the account for all three.
  - c9: the rule's paragraph used "story rooms" and "residue" without saying what they are.

  Pass 5 rewrote all three paragraphs. Whether they now carry the claims is untested, since the readers run once.

**The readers' items, by kind, and the answers (rule 13).**
- **Errors in the account (author-error), each fixed in pass 5:**
  1. "Each order beats a null … unless called thin or theorised" (all three readers). The arrows called thin, A05, A14 and A19, beat their nulls by 0.009 to 0.041. A10 rests on 21 rooms. Only A11 fails its null, and A12 has no count. The note now says what thin and theorised mean.
  2. Findings cited but not served, and counts with no source (all three): 368 and 88, 281 and 96, F-002, F-006's factions, F-009. The numbers of F-009, F-002 and F-006 are now in the account, and the counts are marked as the rooms carrying each theme.
  3. "The field's analyst found the same in r/place" names no source (all three). The account now says who the second analyst was and what they did not see.
  4. "A template does not make placers follow it" has no count or quote (reader 2). It now rests on the setting fact.
  5. The 31 of 52 has no null and no arrow (readers 2 and 3). It is now called a reading of a sample, not an order test, and the second coding is added.
  6. A12 rests on 3 rooms and was never counted (reader 1). It is now marked theorised in its own paragraph, with its base.
  7. ultrahardcore had "no neighbour", against its own quote on taking other works' hearts (readers 2 and 3). The account now says "no border talk and no upkeep".
  8. ubc's refusal answers no attack call shown (reader 3). The call is now quoted [ubc/c0064, h53.63].
  9. "A pass 4 account cites a pass 5 story" (reader 3). The story is now called "the model's last story".
  10. luciomains sat on the list of rooms the account "cannot reach" (all three). The list names rooms the last story told only in part. The heading now says so, and luciomains' residue is named: jokes that turned the work into the room's own game.
  11. The sentences the readers could not follow: 34 items over three readers, most named by two or three. Each was rewritten in plain words: the preferred acceptance, F-015's test, "a decided element of order", "a decision for one work within hours", the thin note, the field's analyst, the ranking rule, the K01 restoration, the residue list's heading, the late rooms and uncoded replies, the tie that names a rival, the curation sentence, open source's task architecture, reward provision, O'Mahony and Ferraro. Stigmergy, story rooms and residue are now glossed where they first appear.
- **Rooms the readers say the account does not describe.**
  - **cardinals** (all three: fits false). The seven passages served, of 102, show no build. The full record, read whole for the model's last story, shows the chain:
    - the call: "[Season 3] Let's make the Cardinals logo in /r/place!" [cardinals/c0024, h36.28];
    - a build report: "Nice start just below the blue note. Could use some fixing up" [cardinals/c0035, h57.09];
    - the finished work: "...and it's done." [cardinals/c0039, h73.15];
    - help to the Blues logo (A13), the Cubs attacks and the restraint (A15, A16), and the host's line (A20).

    The call at h36.28 comes before the rival talk at h41.05 that reader 3 placed first. Verdict: author-error in the packet. Seven passages are too few for a reader to see a room's chain, and no bound is written for the room. Two things the readers saw stand:
    - the room was slow: the call at h36.28 produced no reported build until h57.09;
    - one answer commits on a condition [cardinals/c0062]. The account now says such answers exist and are not counted. This is named for the return.
  - **mysterydungeon** (all three: fits true). Reader 2 notes celebration before upkeep in this room. The account claims no order between celebration and upkeep: P05 after P03 and P11 after P03 both hold here. All three readers note that the sample shows no doubt about hands before the Time Gear move. A10 is thin and its one instance failed its audit, so nothing changes. Printed beside the account.
  - **luciomains** (all three: fits true). See item 10.
- **Disagreements about how to tell it,** printed beside the account in `account-readers-C5.md`: cardinals as the readers saw it; celebration before upkeep in mysterydungeon.

**The second reading of the declarations: the readers' verdicts.** The readers judged 40 sentences: 33 stand and 7 do not.
- T4-002 (prose): "Most rooms were standing communities before the canvas opened…": it has no count.
- T4-010 (prose): "What a chat decided reaches the record only when a member brings it back to the thread.": it has no count and is not a setting fact.
- T4-011 (prose): "The form pass, which counted nothing, found the question who leads almost never asked.": "almost never" rests on nothing counted.
- T4-005 (prose): "Here no one could hold a member's time or assign it.": the setting fact covers placing, not time.
- T4-019 (prose): "Members work out who changed their work and why.": the causal "why" has no support.
- D04 (mistaken_for): "There is no common pool to manage here, only adjacent works.": no support, and the canvas reads more like a common pool.
- D05 (mistaken_for): "…identity is the membership the work…": a claim about the rooms with no support.

My answer: these seven, with all 36 declarations whole, go to the field analyst (QC5-001). I amend the declarations once, after both readings are in. The two readers then judge the same text, and their verdicts on the 40 sentences can be compared.

**The Stigmergy codes.** Each reader coded one member theme's 24 records blind (`c5c_codes_score.py`).

| member theme | agree | kappa (4 codes) | P of not O, mine | P of not O, reader | meets the rule, mine / reader |
|---|---|---|---|---|---|
| T3-038 (reader 1) | 21 of 24 | 0.81 | 5 of 15 | 4 of 14 | no / no |
| T3-041 (reader 2) | 15 of 24 | 0.48 | 8 of 17 | 8 of 14 | no / yes |
| T3-060 (reader 3) | 20 of 24 | 0.75 | 8 of 20 | 10 of 20 | no / yes |

- **Across the three member themes,** trace or marker is in 31 of 52 records by my codes and in 26 of 48 by the readers'. The decision that kept Stigmergy's cut rests on codes two coders do not agree on. For two of the three member themes, the second coding reverses it.
- **What I do.** I do not settle my own disagreements with a reader alone. The 72 records go blind to the field analyst as a third coder, in the QC5-001 packages. The cut is decided in a later check pass with three codings in hand. The account now says the cut is open.

**What the criterion says about pass 5: prefer.**
1. **Unmarked causal sentences: fewer.** The thin note, the template sentence and the curation sentence now rest on what supports them.
2. **Rooms told:** the same story rooms, with the same 23 elements.
3. **Tested arrows:** every arrow is kept.
4. **The prose test:** unchanged.
5. **The readers:** they recovered 4 of my 9 claims whole and 3 in part. Pass 5 rewrote the paragraphs behind the misses. The readers run once, so no figure tests the rewrite.

**What is still due.** Pass 5 changed no element and no cut. Two things are open: the Stigmergy cut, which waits for the third coding, and the amendments to the declarations, which wait for the field reading. So another check pass is due when the field reading returns.

**The field analyst's packages (QC5-001).** They are in `out/field-packages-C5/`, built by `c5c_field_packages.py`; no fleet ceiling binds them. J takes them to the field analyst: a fork of the analyst who wrote the field model and the C4 check, or a fresh session on the same model with that field model as context.
- **What the folder holds:**
  - `00-READ-FIRST.md`: who reads; the one rule for the reader, to judge each sentence against the members' quotes and the rule, not against its own model; the study in brief; what to read and what to judge;
  - `01-the-rule.md`: the rule whole, with its dimension extension and the four setting facts;
  - eight packages by dimension, `02-D01` to `09-D08`. They hold all 36 declarations as they stand, the ten the fleet packets left out included, with 268 sentences numbered. Each declaration comes with its members by name, the quotes it cites or rested on, and 3 quotes per member theme drawn by `cite.py` under seed 20261015;
  - `10-findings.md`: the 11 findings the declarations cite;
  - `11-stigmergy-records.md`: the 72 records in a seeded order, with no one's codes, for a third coding;
  - `RETURN-field-C5.md` and `MANIFEST.json`.
- **What is kept from the field reader.** Nothing of the fleet readers' returns is served.
- **What waits for it.** I would rather the field reading come back before I amend the declarations or settle the Stigmergy cut, so both wait for it.

**Slips, C5c-01.**
- **Two dead lines in scripts.** A no-op line in `c5c_codes_score.py` and a dead conditional in `c5c_field_packages.py` were written and removed before either script ran.
- **A quote cut mid-sentence.** One reader quote in `account-readers-C5.md` was cut mid-sentence and was not an exact substring of the return. A check found it, and the quote now ends at the reader's full sentence.
- **Split member quotes.** The first build of the field packages split members' quotes at their question marks. The splitter now keeps a quote with its citation whole, and the packages were rebuilt before delivery.
- **A late-room sentence.** I first wrote that late rooms "joined the canvas by helping another room's work". A19's and A04's bounds say they entered through another room: its coalition, its offer of space, or a request for space. The sentence was corrected before the check.
- **Parallel edits.** Two Edits to the head ran as parallel calls. Both landed, and a later turn counted the words and ran the link check.

## C5c-02: the second check pass (pass 6), paused once and resumed as C5c-02-p2

**What came back.** The field analyst's second reading is in `sources-from-J/RETURN-field-C5.jsonl`. It holds 268 sentence verdicts, of which 117 are marked as not standing, codes for the 72 Stigmergy records, and 36 notes on declarations. The reader saw none of my codes and none of the fleet's verdicts.
- **J's word (11:02 Amsterdam).** The 117 are advice to improve the model, not evidence that it does not apply, unless a verdict says so.
- **The handler.** The count of 117 measures nothing. I change a sentence where the advice, read against the members' quotes, convinces me, and keep my wording otherwise, with a line saying why.

**Stigmergy, with three codings.** The rule was logged before the tally (`c5c2_stigmergy_three.py`). Each record takes the code that at least two of the three coders gave: me, the fleet reader of its member theme, and the field analyst. MP counts as M. A member theme leaves if P is at least half of its records that are not O. The destinations were written before the read; T3-060's was written before this tally.

| member theme | P of not O, by the code two coders gave | meets the rule |
|---|---|---|
| T3-038 building and reporting the mark | 4 of 14 | no |
| T3-041 extending the room's work | 8 to 10 of 15 (two three-way splits) | yes, either way |
| T3-060 adding a personal piece | 10 of 20 | yes, at exactly half |

- **Agreement.** Mine and the fleet's agree on 57 of 72 (kappa 0.69), mine and the field's on 47 (0.47), and the fleet's and the field's on 48 (0.50). The field analyst's codes alone would move T3-041 only (T3-060: 9 of 19).
- **The decision, as the rule written first sets it.** T3-041 and T3-060 move to Collective representation (C5-move-merging-93).
- **One member left.** Stigmergy keeps T3-038 alone (C5-move-splitting-94). A fourth-order line must keep members, and withdrawing Stigmergy would leave T3-038 in no fourth-order theme, and P03, on the spine, outside its dimension. The three coders read 10 of T3-038's 14 bearing records as reports of the work's state, which is the trace the construct names. The cost is said in the declaration: a one-member theme breaks C2's criterion for a group, since it answers no question its member does not answer alone.
- **The field analyst's advice on this.** Its note advised keeping the members and reconciling first. The codes were reconciled, by the rule logged before the tally, and that rule moved two themes. The field's narrower points on Stigmergy's wording were accepted (below).
- **What the recut touched.** All of these were logged and validated:
  - `fourth.jsonl` (T4-006 now has 14 members and 535 rooms; T4-007 has 1 member and 237 rooms; Stigmergy's gloss replaced, since starbound/c0082 sits under celebration);
  - P02 and P03 restated;
  - A01, A03, A07 and A11 recounted on the recut elements (C5-move-relating-95):

    | arrow | was | now | null p95 |
    |---|---|---|---|
    | A01 P01 to P03 | 137 of 190 | 81 of 126 (0.643), strong to fair | 0.571 |
    | A03 P03 to P05 | 182 of 291 | 148 of 190 (0.779) | 0.389 |
    | A07 P03 to P11 | 182 of 282 | 139 of 182 (0.764) | 0.434 |
    | A11 P02 to P04 | 100 of 166 | 111 of 185 (0.600), still not beaten | 0.670 |

    Every tested arrow still beats its null. A01 without joining lines: 78 of 126 (p95 0.540). A07's touhou transition, which had failed its audit, now starts outside P03 and is noted, not removed;
  - F-016 superseded (534 rooms for information provision, not 555); F-018 written for the three codings; `mapping-C3.jsonl` T4-007 amended, its old reason kept;
  - `propositions.jsonl` regenerated: only N01, N04 and N07's mechanisms changed. Pass 5 is kept as `propositions-p5.jsonl`;
  - the prose test's Stigmergy entry, the figure, and the account.

**The field reading of the declarations.** The rule for accepting or keeping was logged before any amendment.
- **Accept** where the advice shows a sentence claiming more than supports it:
  - (a) a universal or categorical claim with no count, finding or setting fact;
  - (b) a count stated without its finding's limits;
  - (c) an outcome where the quotes show a call or report;
  - (d) a motive or time the quotes do not state;
  - (e) a quote misdescribed.
- **Keep** where the only objection is that the package showed no quote for each act in a list of member themes (each has exemplars in `scheme_v2.jsonl` that the package did not serve), or where a sentence about the literature or the study was read as being about the rooms.
- **The outcome.** 35 declarations were amended, one move each (C5-move-developing-96 to 130), and T4-017 is unchanged. 94 pieces of advice were accepted:
  - (a) 35, such as "only", "no one", "never" or "nothing is owned" outside the setting facts;
  - (c) 25, such as "keep everyone on one template", "they keep the work" or "rooms settle deals", now calls, proposals and reports;
  - (d) 10, such as "for fun", "within hours" or "already held";
  - (e) 10, such as a quote offering a program read as one running, or "I am in." with no citation;
  - (b) 9: F-009, F-014, F-015 and F-006 with their own numbers;
  - 5 other: the recut's counts in T4-005, T4-013 and T4-026, and Stigmergy's old sentences.
- **What was kept.** 30 pieces of advice:
  - 23 are lists of member themes;
  - the rest are the Stigmergy reconciliation (above), D06's scope, the fleet's verdict on T4-019's "why" (the members' question, not my causal claim), and three sentences the field itself found shown.
- **Where to read it.** Each declaration's `tier_history.jsonl` line lists the sentences accepted and kept, each with its line.

**The two readers compared** (`c5c2_two_readers.py`). The fleet and the field analyst both judged 40 sentences. They agree on 21: both let 16 stand, and both find 5 do not. Of the 19 they split on, the field is stricter on 17 and the fleet on 2:
- D05's emblem sentence: accepted from the fleet, now resting on a member's words;
- T4-019's "why": kept.

The field's sentence units are sometimes longer than the fleet's, so part of the split is in how the sentences were cut.

**The account, pass 6** (2,437 words; pass 5 kept as `account-p5.md`).
- **From the recut:** the four counts; the Stigmergy paragraph on the three codings (F-018); the two moved acts under what members settle the mark will show.
- **From the advice I accepted:**
  - F-009 told as a held-size test that found no delay;
  - many placements, not many members;
  - F-014 told as counted on replies to attack calls, not calls to place;
  - decided order's duration untested;
  - A16 told as an order of first concepts;
  - credit nearly all after the work, so the completion ritual is not shown to be reward provision;
  - curation's arguing part tentative;
  - templates by count, not "any member";
  - Live and let live holding some treaty records.

**What the criterion says about pass 6: prefer.**
1. **Unmarked causal and universal sentences: fewer.** 94 sentences now claim what their support carries, in the declarations and the account.
2. **Rooms told:** the same story rooms, with the same 23 elements.
3. **Tested arrows:** all kept; A01 weakens from strong to fair.
4. **The prose test:** every name still does work. Stigmergy now reads one third-order theme.
5. **The readers:** they do not run again.

Pass 6 changed two elements' statements (P02, P03), the fourth-order tier (Stigmergy's recut) and four arrows' counts. So by section 7 another pass is due, which reads the account and the model as they now stand.

**Slips, C5c-02 and C5c-02-p2.**
- **A count I typed.** I first counted 33 declarations in the spec. The script found 34, all amended, and D06 later made 35.
- **A whitespace error.** T4-011's sentence was given with a trailing space it does not have. The dry run caught it.
- **A word count logged wrong.** The diary line on the account's second part gives 2,425 words; the file has 2,437.
- **The pause.** The PI's pause came mid-pass. Nothing was written to a ledger before the pause log.

## C5c-03: the third check pass (pass 7)

**What the pass read.** It read the model as pass 6 left it, together with every file that carries it, for anything pass 6 changed in one place and not in another: the elements, the arrows' mechanisms, the propositions, the figure, the mapping, the prose test and the account.

**What it found.** Pass 6 corrected over-reaching wording in the declarations and the account, but the model's own statements still carried the same claims.
- **Eight element statements:**
  - P04: a template that "fixes" the output, and members who "hold strays";
  - P07: sparing "without a written agreement";
  - P08: rooms that "settle" deals;
  - P09: "griefing for fun";
  - P13's range: "a lasting group";
  - P14: "multiply their hands beyond the rate limit";
  - C01: "almost never asked", which both readers rejected;
  - K01: the play that "fills the room".
- **Four arrow mechanisms:**
  - A01: "start or extend", though extending moved to P02;
  - A11: a template that "fixes" the design;
  - A12 and A16: a reason that always comes with a refusal, against F-014's 23 of 38.
- **Three proposition fields:**
  - N01's count without joining lines: 132 of 189, now 78 of 126, with 50 rooms of replies, not 70;
  - N03: "refuse it with a reason";
  - N07: "align", and its F-006 boundary.
- **The figure's K01 line,** which said F-009 found that the play "did not delay the work".

**What it did, by the rule logged first.** Each item takes the wording already accepted in the declaration or finding it repeats, and nothing new is claimed.
- Twelve moves, one per element or arrow (C5-move-developing-131 to 142), each with a `model/history.jsonl` line keeping the old line.
- The three proposition fields were edited in `c5_propositions.json`, and `propositions.jsonl` was regenerated. Pass 6's copies are kept as `c5_propositions-p6.json` and `propositions-p6.jsonl`. Only N01, N03 and N07 changed, with the mechanisms carried from the four arrows.
- The figure was written again.
- **Kept as historical records:**
  - K01's `cut_cost` (C5a-02);
  - the mapping line's `was_why`;
  - the prose test's C5a-01 entry;
  - `author_claims.jsonl` as served to the readers, whose c2 says refusing "comes with" a reason.

**What the criterion says about pass 7: prefer.**
1. **Unmarked over-reaching sentences: fewer.** Fifteen statements in the model now claim what their support carries.
2. **Rooms told:** unchanged, with the same 23 elements.
3. **Tested arrows:** every one kept; no count changed.
4. **The prose test:** unchanged.
5. **The readers:** they do not run again.

**What is due next.** Pass 7 changed eight element statements, so by section 7 a further pass is due. It reads pass 7's changes as they stand.

**Slip, C5c-03.** The head first named three proposition ids, which the link check does not resolve. It was reworded before the close.

## C5c-04: the fourth check pass (pass 8)

**What the pass read.** It read pass 7's twelve changes as they stand. All twelve say what their declarations and findings now say. It then swept every standing element, arrow mechanism and proposition against the advice accepted at pass 6. That sweep found five claims pass 7 missed:
- P13: "At the close the room decides what to keep". T4-028's accepted advice: the count is gated on rooms writing after hour 73, some acts came before it [minecraft/c0188, h46.25], and members propose what to carry on;
- P12: "records what happened to its work". T4-027's: the records also cover the canvas around the room's work [pokemon/c0506];
- K02 and A10: "the room judges". T4-012's: single members voice the judgment, which is not shown to be the room's shared belief;
- N05's boundary, which read the 78 rooms with no posts in the prior week as subs opened for the canvas. T4-002's: a quiet week does not show when a room began;
- the account's "lasting groups". T4-028's and D07's: an announced group is shown, a lasting one is not.

**What it did.** Each claim takes the wording already accepted, and nothing new is claimed.
- Four moves (C5-move-developing-143 to 146), each with a `model/history.jsonl` line keeping the old line.
- N05's boundary was edited, and `propositions.jsonl` was regenerated. Pass 7's copies are kept as `c5_propositions-p7.json` and `propositions-p7.jsonl`. Only N05's boundary and N08's carried mechanism changed.
- One phrase in the account was changed, and its title now records pass 8.

**What was kept, and why.** P05's "keep the placed work against erosion" stays. The list after the colon names acts (watch, repair, defend, cover the night), not an outcome.

**What the criterion says about pass 8: prefer.**
1. **Over-reaching sentences: five fewer.**
2. **Rooms told:** unchanged, with 23 elements.
3. **Tested arrows:** every one kept; no count changed.
4. **The prose test:** unchanged.
5. **The readers:** they do not run again.

**What is due next.** Pass 8 changed three element statements, so by section 7 a further pass is due. The sweep covered every standing element, arrow mechanism and proposition, so that pass reads these four changes and the N05 boundary.

**Slips, C5c-04.**
- **Parallel edits.** Two Edits to the head ran as parallel calls. Both landed, and a later turn counted the words and ran the link check.
- **A proposition id in the head, again.** The head named one proposition id, as at C5c-03. It was reworded before the close.

## C5c-05: the fifth check pass (pass 9)

**The advice, from J through the PI (12:01 Amsterdam).**
- Passes 6 to 8 changed wording only. The field analyst's standard was a test of description, not the bar for theory. My rule asks that a broad claim carry a count, a finding or a setting fact, not that every claim be restated at the lowest level a quote can show.
- The unit of this study is the room. Where members spoke or acted for the room, in its threads, its calls or its adopted plans, a claim about the room is my theoretical work.
- Pass 9 reads pass 8's five changes and stops there.

**Pass 8's five changes, read on the room as the unit.** These are the members' words under each theme, from the field packages' seeded draws.
- **Restored, K02 and A10: "the room judges".** Members voice the judgment for the room, in its threads and in the first person plural: "We have to shrink. We're being eaten alive by that green monster thing. We can't grow and maintain." [floridagators/c0045]; "we're not doing this anymore don't do it" [raocow/c0066]; "Close the borders before the capital is destroyed" [greenlattice/c0344]. One member speaks apart from the room ("I can't help no more." [fivenightsatfreddys/c0485]). One quote is not enough to demote the element. The declaration keeps its difference from Bandura's measured shared belief.
- **Restored, P13: "the room decides what of its temporary effort to keep".** Members propose and request for the room, in its threads and to its moderators: "Request to the mods: could we have this preserved in our CSS somewhere?" [fireemblem/c0412]; "LONG LIVE THE LATTICE!! In the form of the official Steam group" [greenlattice/c1156]. Pass 8's correction of the time stays ("near the close and after it"), since some of these acts came before hour 73.
- **Kept, P12: "and to the canvas around it".** It widens what the room records; the actor is still the room.
- **Kept, N05's boundary.** It concerns what a count of quiet weeks can show, not the unit.
- **Kept, the account's "groups announced to carry on".** Whether a group lasted is an outcome after the record ends, not a question of the unit.
- **The writes.** Three moves (C5-move-developing-147 to 149), each with a `model/history.jsonl` line keeping the old line. `propositions.jsonl` was regenerated, with pass 8's copy kept as `propositions-p8.jsonl`; only N08's carried mechanism changed.

**What the criterion says about pass 9: prefer.** Item 4: Collective efficacy names a judgment held at the level of the room, and with K02 restored the name does its work in the prose test sentence ("because the room judged its strength too low, it could stop fighting and move"). Items 1 to 3 are unchanged: no claim gains a cause, every room is told as before, and every arrow and count is kept.

**What is due next.** Pass 9 changed two element statements (K02, P13) and one arrow mechanism. So by section 7 a further pass is due, which reads only these three restorations. No new sweep is made.

**For C5d: how confident I am, and what the strict reading cost.** Noted as I go, as asked.
- **Sure.** The spine and the contest are orders of first concepts in coded talk that beat a null of 500 shuffles within each room:
  - the start before calls, 64 of 89;
  - calls before build reports, 81 of 126 (fair since the recut);
  - build reports before upkeep, 148 of 190, and before celebration, 139 of 182;
  - calls before the host's line, 132 of 155;
  - the attack call before sparing, refusal or apology, 82 of 104.

  These are orders in what members wrote, not observed causes.
- **Less sure.**
  - The thin arrows: A05, A10, A14 and A19.
  - The theorised A11 and A12.
  - Stigmergy's membership: three coders agree moderately, and T3-060 sits exactly at the line.
  - The bare answer: its reason test was run on attack calls only.
- **What the strict reading cost, as I see it:**
  1. The room as actor in K02 and P13, now restored.
  2. "The completion ritual is not reward provision" became "is not shown to be". I still believe credit worked as recognition after the work, not as an inducement to place, on the timing evidence (F-016). The record cannot test inducement, so the weaker words are the honest ones.
  3. D02's "ways a room aligned many hands" became "ways members tried to align". I believe these routes did align hands, since marks were built and kept, but the canvas is not evidence here (rule 7), so "tried" stands.
  4. Stigmergy narrowed to one member. I still think many proposals to extend a mark read its state, which is what the MP code caught. The three codings decided otherwise for two themes, and I follow the rule I wrote.
  5. "Lasting groups" became "groups announced". I believe some groups born on the canvas lasted, but the record ends, so the account does not claim it.
- **On balance.** The strict reading removed overstatement more than insight. The insight it cost was mostly the room as the actor, which this pass restores.

**Slip, C5c-05.** The head again first named a proposition id. It was reworded before the link check.

## C5c-06: the sixth check pass (pass 10)

**What the pass read.** It read only pass 9's three restorations, as they stand, with no new sweep.
- **K02:** "The room judges that it has too few hands or too little room for the work it wants…". Its range, "from one member saying there are not enough people to defenders told to give up", runs from one member's voice to the room's.
- **A10:** "A room that judges it has too few hands to hold its spot stops fighting for it and moves."
- **P13:** "Near the close and after it, the room decides what of its temporary effort to keep…". The time correction is kept, and the range ends in "a canvas-born collective announcing a group to carry on".
- **Against the rest of the model.** The account ("Members who judge that the room has too few hands stop fighting for the spot and move, in 11 of 21 rooms [A10, K02, P10]") and N08 say that members voice the judgment and the room moves. That agrees with K02 and A10, since members speak for the room. The account's "groups announced to carry on in 113 of 145 [A09, P13]" agrees with P13's range.

**What the criterion says about pass 10: no change.** No element, arrow, count, finding or cut changed, and no sentence of the account changed.

**The passes stop.** By section 7, pass 10 changed no element and no cut. The passes stop here, and I choose to move to C5d next.

## C5d: the table, the figure, the implications and the handback

**The rule that chose the data structure's rows** (section 9). It was logged before the table was built.
- **One row per third-order theme** that a fourth-order theme gathers: 195 rows, ordered by dimension, fourth-order theme and member.
- **The range, not the centre.** Within each fourth-order theme, the k-th member takes a room from the k-th quartile of rooms by `items_in_window` (k taken mod 4, quartiles over the 705 rooms). Within that quartile, the concepts cited under the theme are shuffled with `random.Random(20261015)`. The first of 5 to 40 words, with no table-breaking character and from a room not yet used in that fourth-order theme, is taken; failing that, the next quartile.
- **Each quote enters through `cite.py`,** with its community, author, hour and concept id.
- **The result.** The rows draw 45, 55, 56 and 36 quotes from the four quartiles. One theme (T3-144, recruiting quietly) has no cited concept, and its row says so. The residue below the table is T3-017 and T3-133, each with its account and a quote. The paper's figure, when it is drawn, is a sample of these rows by the same rule.

**What was written.**
- **`data_structure-C5.md`:** all 192 quotes resolve, and every third-order theme, fourth-order theme and dimension appears.
- **`figure-C5.md`, final:** 21 boxes in three columns with the hour 73 terminus. It has 20 arrows, 19 shown by an audited transition and 1 by a quote, and two drawings, with and without A11 and A12, as text and as Mermaid. No loop is drawn. The paragraph on what it leaves out names the field's tentative arrow, the tentative and candidate elements, the seven fourth-order themes no element uses, the residue, and the register the coders' topic-based tier scattered (CC-057).
- **`implications-C5.md`:** the theory question in the model's terms; two counterfactuals at a leaf; transferability, with six conditions and the frame; ten expectations for the return; and which forms keep the work alive, from the record (`c5d_kept.py`). No form sorts kept from lost by much, and the clearest difference is less silence.
- **`handback-C5.md` and `interview/C5d.md`.**

## C5c-07: the serial work, planned

**J's ruling (13:45 Amsterdam, 15 October, through the PI).** The freeze at C5d is lifted for serial work in this branch.
- This leg builds the package for the second coding of border talk and writes this plan.
- Each later leg works one problem only. It reads this plan, the head and the finding files written so far, does the work, writes its finding to its own file, and closes.
- After the last problem, one leg folds the findings into the head and the setup I had before the serial work. Then C5d is redone.

**The package for the second coding of border talk** is in `out/field-packages-C5b/` (`c5c7_border_package.py`).
- **What it holds:**
  - the 40 records of my C5a-02 read, each a room's first border-talk concept through `cite.py`, in a seeded order;
  - the T, D and O codes, copied from the rules I wrote before that read;
  - a read-me and a return format.

  None of my codes or doubts is served.
- **The rule for the return, written before it comes back.** Each record takes the code that at least two coders gave.
  - With two codings, mine and the field analyst's, a record we code alike takes that code.
  - A record we split is counted both ways, so the result is a range, as for Stigmergy's three-way splits. Cohen's kappa is reported.
  - If a third coding comes, each record takes the code the majority gave.
  - A04's bound then states T of T plus D at the low and the high end of the range.
- **Where it is scored.** The leg for problem 3 scores it if the return is in `out/sources-from-J/` by then. Otherwise the fold-in leg scores it.

**The setup before the serial work.**
- The head as it stood at C5d's close is copied to `out/serial-C5/head-before-serial.md`.
- The model and its tiers at that close are hashed in `_closes/model-C5.sha256` and snapped as `C5-cut-interview-C5d-20261015T103817Z`.

**What every serial leg does.**
- It reads this plan, the head and the finding files in `out/serial-C5/`.
- It writes the rules for any read before the read, logged with `--kind abductive`.
- In every sentence it writes, the actor is the room, or a group of rooms, wherever members spoke or acted for it (problem 1's rule, below).
- It makes each change to the model as a logged and snapped move, with its ledger line (`tier_history.jsonl`, `model/history.jsonl`, and `findings.jsonl` under rule 14). It also writes one line in `account_passes.jsonl`, with what the criterion says.
- It does not rewrite `account.md` or `propositions.jsonl`. Its finding file lists the sentences and fields its change touches, and the fold-in leg rewrites them once.
- It writes its finding file with seven parts:
  - the question;
  - the rule, written first;
  - what was read, with counts and denominators;
  - what changed, by ledger id;
  - what did not change, and why;
  - what the fold-in must carry;
  - how sure I am.
- It adds one line to the head's revisions, pointing to its finding file, and otherwise leaves the head as it stands.
- It closes with `done.sh C5`.

**The order, and why.** I keep J's order.
1. The unit comes first, because every later leg writes under its rule.
2. The reason test stands alone.
3. Thin evidence comes third. This gives the second coding of border talk time to return, and the leg sets when a count should weigh more than my reading of the material.
4. Stigmergy and "aligned" come last. That choice draws on the unit and on the stance on counts, and a recut of the tier changes what the redone C5d regenerates in any case.

### Problem 1: the unit (`out/serial-C5/finding-1-unit.md`)

- **The question.** At pass 6, I accepted 94 pieces of field advice. Which of them moved the actor from the room, or a group of rooms, to members, where members spoke or acted for the room?
- **The rule, from J's advice (12:01 and 13:45).**
  - **The room is the actor** where members spoke or acted for it: in its threads, in the first person plural, in its calls, or in plans it adopted.
  - **A group of rooms is the actor** where a coalition or an agreement acted.
  - **Members are the actor** only where the quotes show them acting apart from the room or against it, such as a refusal of the room's call or a member placing alone.
  - **The rule holds in the global model too.** The account, the propositions, the element statements and the arrows speak of rooms or groups of rooms.
- **The read.**
  - A script lists the 94 accepted pieces from the C5c-02-p2 lines of `tier_history.jsonl`, with the old sentence (`was`) beside the new one. It flags each piece where the actor changed.
  - Passes 7 and 8 carried that wording into the elements, the arrows and the propositions (`model/history.jsonl`, moves 131 to 146), so those are swept too.
  - For each flagged item, I read the quotes it rests on through `cite.py`, with the quotes drawn for the field packages.
- **What changes.** Only the actor.
  - The rest of the accepted advice stays: no universals without support, counts with their limits, motives the quotes do not state, quotes read right.
  - Each restoration is a declaration amendment or a model history line, logged as a "developing" move and snapped.
  - Each item that keeps members as the actor says why, in a line.
- **For the fold-in.** The leg lists every sentence of the account and every proposition field whose actor changes.

### Problem 2: the reason test (`out/serial-C5/finding-2-reason-test.md`)

- **The question.** In replies to attack calls, refusals gave a reason in 23 of 38, and acceptances in 2 of 14 (F-014). How much of that is what members did, and how much is what the written record kept? And do replies to calls to place show the same pattern?
- **What the draw already sets.** F-014 drew acceptances and refusals apart, each by its theme, up to 40 rooms per kind (`c3b_ca_pairs.py`). So 38 against 14 is not a ratio from the rooms. Only the share giving a reason, within each kind, is a result.
- **Survivor bias, as J frames it: omission against commission.**
  - A member can accept a call by placing pixels and never write a reply. A member who declines leaves no mark on the canvas, so the record shows the refusal only if it was written.
  - A refusal may need a reason to be said at all, while an acceptance is shown by doing. So among written replies, the acceptances that survive may be the barest ones.
  - Removed and deleted replies drop out of the record. I check what the store records of removed and deleted items, under each kind of call, and say what the record cannot show.
- **The test on calls to place, with rules written first.**
  - **The pairs:** a first part under the calls element's theme (P01) that asks members to place, and the first direct reply by another author, later in the same thread.
  - **The draw:** 80 pairs with seed 20261015, drawn from replies of any theme, since the theme a reply sits under does not track its stance.
  - **The codes:** as in `c3b_ca_codes.json`: stance (accept, refuse, mixed, other) and account (a reason given or not).
  - **The test:** Fisher's test, as before.
  - **Coding:** by me alone, and the finding says so. If the result changes a claim, a package for a second coder is built in the form of `field-packages-C5b/`.
- **What a result can change.**
  - F-014's bound, through a new finding or a superseding line.
  - A12's mechanism, the bare answer, which is theorised, if calls to place show it.
  - The bare answer's wording in the account.
  - How the account reads the asymmetry: as a fact about written replies.

### Problem 3: thin evidence (`out/serial-C5/finding-3-thin-evidence.md`)

- **The question.** Thin is not weak, and crucial things happen rarely. When should a count weigh more than my reading of the material, and when should it not? The leg applies the answer to the move after doubt (A10) and to border talk and what follows it.
- **The stance, written first and then checked against the method's sources.**
  - **A count decides** a claim about a distribution or an order across rooms, when its denominator is large enough for a null.
  - **My reading decides, with the count stated beside it,** when three things hold:
    - the event is rare by its nature (a loss, a move, a broken deal), so few rooms can carry it;
    - the step shows in members' words in the rooms that carry it;
    - no room that carries both elements shows the reverse.
  - **Then the claim stands as a mechanism shown in N rooms.** It is labelled thin (rule 8), not stated as a tendency (rule 16).
  - **The sources.** I check what Gioia, Corley and Hamilton 2013 and Grodal, Anteby and Holm 2021 say on this before I cite them. QC5-002 asks J for the passages he means.
- **The move after doubt (A10, from K02 to P10, 11 of 21 rooms).**
  - Read the first K02 concept and the first P10 concept of all 21 rooms whole, with their hours.
  - Code each room under codes written first:
    - the move follows a judgment of too few hands or too little space;
    - the move came first;
    - the move was by choice or by a coalition's plan;
    - there was no move.
  - Then count the rooms that could have carried a loss (rule 6).
- **Border talk and what follows it ("the border replies").** I read J's phrase as covering three things:
  - A05, the thin arrow from border talk to sparing, refusal or apology;
  - A14, the thin arrow from border talk to help;
  - the first-turn reading behind A04's bound (34 of 38).

  For A05 and A14, the leg reads every room that carries both elements, whole, under codes written first, as for A10. The second coding of the 40 border records is scored by the rule above when it returns.
- **What a result can change.**
  - The arrows' strength and mechanism.
  - A04's bound.
  - How the account and the propositions word a thin claim.
  - K02's and P10's ranges.

### Problem 4: Stigmergy and "aligned" (`out/serial-C5/finding-4-stigmergy-aligned.md`)

- **The question.** Is Stigmergy, with one member, the right fourth-order theme? Is "aligned" or "tried to align" the right word for what rooms did with many hands? J defers to me and asks for a choice with literature behind it.
- **Stigmergy: the options.**
  - **(a)** Keep it with one member (T3-038), as now.
  - **(b)** Withdraw it, and place T3-038 in the fourth-order theme of its dimension that takes it.
  - **(c)** Return T3-041 and T3-060 where their records propose additions grounded in the work's state (the MP code). Heylighen 2016 counts such a trace as "an opportunity for advancement" (p. 8). This would set aside the outcome of the three-coder rule for a reading, so it needs a reason stronger than my belief.
- **"Aligned".**
  - D02 and the alignment proposition now say that members tried to align.
  - The rooms' own reports of built and kept work are in the record, apart from the canvas: building and reporting the mark, and `work_remained` kept in 347 of 705 rooms.
  - If those reports carry the result, "rooms aligned" can rest on them. If they do not, "tried" stays.
- **The literature.**
  - **On file:** Heylighen 2016 and Grassé 1959 (`sources-from-J/`), and Puranam, Alexy and Reitzig 2014 (checked at C3).
  - **Asked of J (QC5-002):** Bolici, Howison and Crowston 2016, on stigmergic coordination in free and open-source teams; Okhuysen and Bechky 2009, on coordination.
  - Anything not on file is marked as not checked against the text.
- **Sparring.** If my tools allow it, one adversarial reader is asked for the strongest reasons on both sides.
  - It is given the declaration, the members' quotes, the three codings and the sources, and never my notes.
  - It decides nothing.
- **The rule for the choice, written before the read.** Choose the option that:
  - the members' records under each member theme support;
  - the source's definition admits;
  - keeps the dimension whole.

  On a tie, choose the option with fewer claims that lack support (the criterion's first item).
- **What a result can change.**
  - The fourth-order tier: `fourth.jsonl` and `tier_history.jsonl`, and `scheme_v2.jsonl` if a third-order theme moves.
  - F-018, superseded or bounded.
  - D02, P02 and P03.
  - The counts of A01, A03, A07 and A11, if the elements change.
  - The alignment proposition.

### The fold-in, and C5d again

- **The fold-in leg:**
  - starts from `out/serial-C5/head-before-serial.md` and the four finding files;
  - scores the border return, if problem 3 could not;
  - rewrites `account.md` and `propositions.jsonl` once, as one pass;
  - writes the head, and closes with `done.sh C5`.
- **C5d again:** it regenerates the data structure, the figure, the implications with their expectations, the handback and the interview from the model the findings leave.

### How each problem serves the two questions (QC5-002, written at C5c-08 before problem 1)

J's answer to QC5-002 (14:14 Amsterdam) asks me to reread the contract's section 1 and say how each problem serves the theory question and the method question. I reread it. Three of its lines bear on this work:
- "A subreddit is an observation venue, not automatically an organization."
- "Record rooms that did not organize and organizing that crossed room boundaries."
- The model has to say four things: how a scattered readership becomes something that can act; how it settles what to act on; what sends a group back to that beginning; and what they leave behind.

How each problem serves the questions:
- **The unit, problem 1.**
  - *Method question.* The return composes the global model from room-level case histories (D1 to D3), and stage D4 forms are sets of rooms. A global model that speaks of members cannot compose with them.
  - *Theory question.* Forms are forms of organizing, and the room, or a group of rooms, is what organizes.
  - *The contract's limit.* The rule restores the room only where members spoke or acted for it, so no subreddit is assumed to be an organization. Groups of rooms are named where organizing crossed room boundaries.
- **Thin evidence, problem 3.**
  - *Theory question.* The move after doubt (A10) is the model's answer to what sends a group back to its beginning. Border talk and what follows it is organizing that crossed room boundaries. These are two of the paths by which rooms differ in what they meet after building.
  - *Method question.* A thin arrow at the population level may be a strong one inside a form. Where the arrow belongs, at the population or in a branch, is a question of composition.
- **Stigmergy and "aligned", problem 4.**
  - *Theory question.* It answers how a scattered readership becomes something that can act: how the room coordinates through the work, and whether many hands were aligned or only asked to align. Stigmergy is mapped to information provision (`mapping-C3.jsonl`), one of the four universal problems of organization design.
  - *Method question.* A fourth-order theme with one member groups nothing, so construction upward fails at that tier.
- **The reason test, problem 2.**
  - *Theory question.* In organization terms, it is how a room settles what to act on: a refusal with a reason contests the room's goal, and an acceptance is often done rather than said. This is J's point on omission against commission.
  - *Method question.* It serves the method question as a check on evidence of the record's kind: talk records contest more than consent.

**The new order.** None of the four is dropped, since each serves both questions.
1. The unit stays first.
2. Thin evidence moves to second. It sets the stance on when a count outweighs my reading of the material, which the Stigmergy choice needs, since T3-060 sits exactly at its rule's line.
3. Stigmergy and "aligned" move to third.
4. The reason test moves to last. It serves one of the four things through one mechanism borrowed from outside organization theory, and it is the narrowest.

The finding files keep their numbers by problem, not by order.

**The literature, revised on J's answer.**
- **Bolici, Howison and Crowston 2016 is dropped.**
- **Stigmergy is argued from organization design and coordination:** Moffett et al. 2021 (`moffett-et-al-2021-ant-colonies-jod.md`) and Okhuysen and Bechky 2009 (`okhuysen-bechky-2009.md`). Heylighen 2016 and Grassé 1959 stay only as the construct's sources.
- **For thin evidence, I find the passages myself and cite them from the page:** Gioia, Corley and Hamilton 2013 (`gioia-corley-hamilton-2013.md`) and Grodal, Anteby and Holm 2021 (`grodal-anteby-holm-2021.md`).

**Slips, C5c-07.**
- **A cut after a read.** I chained `cut -c` after a `mem.py diary` read, and the guard refused it. I reran the search without it.
- **A drafted addition to the codes.** I drafted two lines under the border codes that restated my doubtful calls. They came from my read, not from the rules written before it, so I removed them before the package was written.

## C5c-08: problem 1, the unit (pass 11)

The finding is `serial-C5/finding-1-unit.md`. In short:
- **The rule.** It was logged before the read (diary, C5c-08, abductive). The room, or a group of rooms, is the actor where members spoke or acted for it. Members stay where they act apart from the room or the act is a person's.
- **The restorations.** Five declarations (D02, D07, T4-014, T4-018, T4-028), five elements (P01, P03, P04's range, P05, C02) and four arrow mechanisms (A01, A05, A08, A17) take the room or a group of rooms again (C5-move-developing-150 to 163).
- **For the fold-in.** 11 proposition sentences and 16 account sentences are listed.
- **Unchanged.** No count, grounding or status changed.
- **A check.** In the restored themes, members speak in the first person plural about two to three times as often as in the singular alone. Carrying on is even, and its declaration names both rooms and members on their own.

**What the criterion says about pass 11: prefer.** Items 1 to 3 are unchanged. On item 4, Territoriality and Meta-organization again name what rooms do.

**Slips, C5c-08.** I ran an Edit and a `sed` on `c5c8_unit_sweep.py` as parallel calls. Both landed, since the rerun used the new code.

## C5c-09: problem 3, thin evidence (pass 12)

The finding is `serial-C5/finding-3-thin-evidence.md`. In short:
- **The stance.** I wrote it first and then checked it against Gioia et al. 2013 (pp. 16, 18, 20) and Grodal et al. 2021 (pp. 597, 598, 599, 604).
  - A rare-thin claim stands on my reading, with its count beside it.
  - A weak-thin order stands on its count.
- **The border second coding,** scored by the rule logged at C5c-07: terms before damage in 19 of 26 to 36 of 38, with kappa 0.19. The claim holds at both ends.
- **A10, the move after doubt.** The judgment came before the move in 10 of 20 rooms, or 9 if one mixed room is read the other way. Of the 26 rooms that voiced doubt, lost their work and did not move, 11 gave the work up (F-019).
- **A05, border talk to sparing.** The first sparing names a line in 17 of 124 rooms, so the mechanism is theorised. Sparing rests mostly on the room's own norm (F-020).
- **A14, border talk to help.** The first help names a deal or the neighbour relation in 63 of 127 rooms where border talk comes first, against 23 of 67 where help comes first. The rule written first does not decide 0.496, and I judge the mechanism shown in words (F-020).
- **The writes.** Four arrows were amended (C5-move-developing-164 to 167). No count, strength or element changed.

**What the criterion says about pass 12: prefer.**
- *Item 1:* one mechanism that claimed more than its words show is now marked theorised.
- *Items 2 and 3:* unchanged.
- *Item 4:* Live and let live, Reciprocity and Collective efficacy now have read evidence for their mechanisms.

**Slips, C5c-09.**
- **A command refused whole.** A Bash command that chained a log line, an inline script and a file read was refused as a whole. I reran the parts separately, and nothing in it had run.
- **Finding ids as tier events.** The pass 12 line first named F-019 and F-020 as tier events. The check takes tier events only from the tier and model histories, so the line was rewritten without them (`c5c9_fix_pass12.py`).
- **A share rounded up.** The tally script prints 63 of 127 as 0.50; it is 0.496.

## C5c-10: problem 4, Stigmergy and "aligned" (pass 13)

The finding is `serial-C5/finding-4-stigmergy-aligned.md`. In short:
- **The rules.** They were written first, and options (d) and (e) were each named before they were weighed.
- **The sources,** cited from the page: Moffett et al. 2021 (pp. 58, 63–64, 71), Okhuysen and Bechky 2009 (pp. 469, 474, 482–483) and Grassé 1959 (p. 75, checked).
- **The adversarial reader** was given a brief and no notes, and ran read-only. Its reasons are quoted in the finding.
- **The choice: (e).**
  - Stigmergy keeps its one member, its place in D02 and its mapping to information provision. It is renamed Direct information sharing (C5-move-developing-168).
  - The records are members' posts of the work's state, which Okhuysen and Bechky name. The old name claimed the placing that would answer the posts, which the record does not hold.
  - Merging with Standardization of output would join two routes the rooms carry apart (89 rooms carry both, against 80 expected by independence; F-022) and two universal problems.
  - The cost, one member against C2's criterion, is stated in the declaration.
- **"Aligned."** D02 says the room aligned many hands, with the count: in 233 of 370 rooms that called for hands, the record reports a work up after the first call (F-021; C5-move-developing-169). The others tried.
- **The ledgers.** F-018 was superseded by a bounded line. No element, arrow or count changed.

**What the criterion says about pass 13: prefer.**
- *Item 1:* one construct name that claimed more than its records show is replaced.
- *Items 2 and 3:* unchanged.
- *Item 4:* the renamed theme passes the prose test on what its records show.

## C5c-11: problem 2, the reason test (pass 14)

The finding is `serial-C5/finding-2-reason-test.md`. In short, under J's framing (omission against commission):
- **Survival, counted before any reply was read.**
  - Of 1,949 calls to place, 920 (0.47) have a written direct reply by another member. Of 1,565 attack calls, 682 (0.44) do.
  - Of the replies written, 0.21 and 0.26 carry no coded text. About 1 in 100 has a deleted author.
  - So most answers are not in the writing, and later removal is small.
- **The read.** 80 seeded first coded replies to calls to place, coded under rules logged first, gave 63 pairs.
  - 31 accept, 3 refuse, 2 are mixed, 27 are other.
  - Refusals gave a reason in 3 of 3, and acceptances in 6 of 31 (one-sided Fisher p 0.014). 25 acceptances are bare.
- **The writes.**
  - F-023 is written.
  - F-014 is superseded. It is scoped to written, coded replies, and its 38 against 14 is named as set by the draw.
  - A12's bound and mechanism take the read count, and the answer given by placing (C5-move-developing-170).
  - No element, order count or strength changed.

**What the criterion says about pass 14: prefer.**
- *Item 1:* a universal reading of the asymmetry is scoped to what the record holds.
- *Items 2 and 3:* unchanged.
- *Item 4:* the bare answer now has a count.

**Slips, C5c-11.**
- **A same-file Edit and `sed`.** I put an Edit and a `sed` on `c5c11_place_pairs.py` in one turn, and the `sed` was refused. I made the change with Edit.
- **An unchecked field.** The pair script first stopped on items with no hour. Nothing had been written, and the draw ran after the fix.
- **An Edit and its check in one turn.** The last head Edit and its word count ran in one turn. The count, 2,999, came after the edit.

## C5c-12: the fold-in (pass 15)

**The rule, written before any write.** One pass folds in the changes the four findings list, with no new read and no claim beyond the findings and the ledgers. The room, or a group of rooms, is the actor where the findings put it. Copies are kept before each rewrite.

**What was folded in:**
- **The account (pass 15; pass 8 kept as `account-p8.md`).**
  - The room is the actor in the sentences finding 1 listed.
  - The bare answer is read on written replies, after the survival counts (F-023, F-014).
  - "Aligned" carries its count (F-021).
  - The paragraph on the mark is now Direct information sharing, told apart from stigmergy, templates (F-022), imitation and open source.
  - Border talk takes the two-coder range. A05's line is theorised, and sparing rests on the room's own norm; A14's channel shows in words (F-020).
  - A loss is followed by a move or by giving the work up (F-019).
  - A new section, "What the account answers", covers the theory question, which forms keep the work alive (from the record), and the method question.
  - The paragraph on the cuts is shortened. All 30 quoted citations match the record (`c5c12_cite_check.py`).
- **The propositions.** 23 fields are set (`c5c12_props.py`), and the file was regenerated: 9 propositions, 3 thin, 1 wholly theorised, 2 from the literature.
  - N01 to N08 take the room as actor where the findings say so.
  - N07 now rests primarily on counts.
  - N08 takes F-019.
  - N09 is narrowed to the channel for help, with A05's line theorised.
- **The prose test.** 8 passages changed (`c5c12_prose_test.py`; the file before is kept as `prose-test-C5-p14.md`):
  - Direct information sharing replaces Stigmergy;
  - Collective efficacy, Live and let live and Reciprocity get read evidence for their mechanisms, and keep their flags where a return or a shared belief is still untested;
  - Territoriality and Meta-organization now name rooms.
- **The model.** A16's mechanism says the reason comes "in written replies" (C5-move-developing-171).
- **F-019** is superseded: its quote is restored to the record's spelling ("Buildling"). Finding 3's copy is corrected likewise.
- **The head** is rewritten from `serial-C5/head-before-serial.md`, with the findings folded in.

**What the criterion says about pass 15: prefer.**
- *Item 1, unmarked causal and universal sentences: fewer.* The asymmetry of reasons is scoped to written replies, and A05's mechanism is marked theorised.
- *Item 2, rooms told:* the same, with the same 23 elements.
- *Item 3, tested arrows:* every one kept, with no count changed.
- *Item 4, the prose test:* three flagged names gain read evidence, and two names now do their work on rooms.
- *Item 5, the readers:* they do not run again.

**Slips, C5c-12.**
- **A cut after a read, again.** A `cut -c` after `mem.py` was refused by the guard. I reran the command without it.
- **A no-op command.** I ran one no-op command with a shell variable, against the rules. It changed nothing.
- **A stale head line.** The head's first line had said "Last written at C5c-08" through three closes (C5c-09 to C5c-11).
- **A proposition id in the head.** The rewritten head named a proposition id. It was reworded before the link check passed.
- **A quote corrected silently.** At C5c-09 I had corrected the spelling of a member's quote in F-019 and in finding 3. Both now carry the record's spelling.

## C5c-13: C5d's work redone after the serial work

**J's ruling (16:29 Amsterdam, through the PI).** The handler cannot reopen C5d, a closed leg. This leg redoes C5d's work from the model as pass 15 left it, under a C5c label. The earlier outputs are kept as `data_structure-C5-p14.md`, `figure-C5-p14.md`, `implications-C5-p14.md` and `handback-C5-p14.md`.

**The rule that chose the table's rows** is the one logged at C5d before that table was built, applied unchanged (`c5c13_data_structure.py`, a copy of C5d's script that changes only its title and log name):
- one row per third-order theme that a fourth-order theme gathers;
- rooms taken from the four size quarters in turn, with seed 20261015;
- the residue below the table.

The result matches C5d's: 195 rows, quartiles 45, 55, 56 and 36, and residue T3-017 and T3-133. Only T4-007's name differs. All 192 quotes resolve.

**What was redone:**
- **`figure-C5.md`** (`c5c13_figure.py`):
  - 21 boxes and 20 arrows: 19 shown by a transition, 1 by a quote;
  - A11 and A12 theorised, and A05's mechanism theorised;
  - P03's box named for posting the work's state;
  - giving the work up named among what the figure leaves out.
- **`implications-C5.md`:**
  - the theory question with the two routes (F-022), "aligned" (F-021), settling what to act on (F-023, F-014), help through deals and sparing on the room's own norm (F-020), and a loss followed by a move or by giving up (F-019);
  - the day9 counterfactual, which borrows A14's channel and not A05's theorised line;
  - thirteen expectations;
  - which forms keep the work alive.
- **`handback-C5.md`:** it states that C5d's work was redone here and why, gives the stage's final-message content as the model now stands, and reports both model hashes.
- **`interview/C5c-13.md`:** 650 words. Step C5c has no interview point in `tools/steps.tsv`, so this leg closes with plain `done.sh C5`, and the brief stays at its leg name for the interview that follows.

**The model freeze (QC5-003).** `done.sh` records the model's hash only when a C5d leg closes.
- `_closes/model-C5.sha256` holds C5d's hash: 24d18e0e…216d7.
- The model as pass 15 left it hashes to e15f9647…b3fecd.
- I asked how the freeze is to be re-recorded, and I left `_closes/` untouched.

**Slips, C5c-13.**
- **Edits and their checks in one turn.** The table script's title Edit and its grep ran in one turn, and so did the brief's Write and its word count. Both checks were read-only and saw the change.

## The close-check, C5c-13

`python3 tools/validate.py C5`, run after the table, the figure, the implications, the handback, the brief and the head:

```
stage C5:
  data_structure-C5.md: 195 rows, 192 quotes checked
  leg: check; passes 15, propositions 9, elements 30, arrows 21, history lines 134


0 errors (0 distinct shapes), 0 warnings
```

## The close-check, C5c-12

`python3 tools/validate.py C5`, run after the account, the propositions, the prose test, the model change and the head:

```
stage C5:
  data_structure-C5.md: 195 rows, 192 quotes checked
  leg: check; passes 15, propositions 9, elements 30, arrows 21, history lines 134


0 errors (0 distinct shapes), 0 warnings
```

## The close-check, C5c-11

`python3 tools/validate.py C5`, run after the writes, the finding and the head:

```
stage C5:
  data_structure-C5.md: 195 rows, 192 quotes checked
  leg: check; passes 14, propositions 9, elements 30, arrows 21, history lines 133


0 errors (0 distinct shapes), 0 warnings
```

## The close-check, C5c-10

`python3 tools/validate.py C5`, run after the writes, the finding and the head:

```
stage C5:
  data_structure-C5.md: 195 rows, 192 quotes checked
  leg: check; passes 13, propositions 9, elements 30, arrows 21, history lines 132


0 errors (0 distinct shapes), 0 warnings
```

## The close-check, C5c-09

`python3 tools/validate.py C5`, run after the reads, the writes, the finding and the head:

```
stage C5:
  data_structure-C5.md: 195 rows, 192 quotes checked
  leg: check; passes 12, propositions 9, elements 30, arrows 21, history lines 132


0 errors (0 distinct shapes), 0 warnings
```

## The close-check, C5c-08

`python3 tools/validate.py C5`, run after the restorations, the finding and the head were written:

```
stage C5:
  data_structure-C5.md: 195 rows, 192 quotes checked
  leg: check; passes 11, propositions 9, elements 30, arrows 21, history lines 128


0 errors (0 distinct shapes), 0 warnings
```

## The close-check, C5c-07

`python3 tools/validate.py C5`, run after the package, the plan and the head were written:

```
stage C5:
  data_structure-C5.md: 195 rows, 192 quotes checked
  leg: check; passes 10, propositions 9, elements 30, arrows 21, history lines 119


0 errors (0 distinct shapes), 0 warnings
```

No model file changed in this leg, so it writes no `account_passes.jsonl` line.

## The close-check, C5d

`python3 tools/validate.py C5`, run after the C5d files were written and before the head was rewritten:

```
stage C5:
  data_structure-C5.md: 195 rows, 192 quotes checked
  leg: check; passes 10, propositions 9, elements 30, arrows 21, history lines 119


0 errors (0 distinct shapes), 0 warnings
```

## The close-check, C5c-06

`python3 tools/validate.py C5`, run after the pass 10 line and before the head was rewritten:

```
stage C5:
  leg: check; passes 10, propositions 9, elements 30, arrows 21, history lines 119


0 errors (0 distinct shapes), 0 warnings
```

## The close-check, C5c-05

`python3 tools/validate.py C5`, run after the pass 9 line and before the head was rewritten:

```
stage C5:
  leg: check; passes 9, propositions 9, elements 30, arrows 21, history lines 119


0 errors (0 distinct shapes), 0 warnings
```

## The close-check, C5c-04

`python3 tools/validate.py C5`, run after the pass 8 line and before the head was rewritten:

```
stage C5:
  leg: check; passes 8, propositions 9, elements 30, arrows 21, history lines 116


0 errors (0 distinct shapes), 0 warnings
```

## The close-check, C5c-03

`python3 tools/validate.py C5`, run after the pass 7 line and before the head was rewritten:

```
stage C5:
  leg: check; passes 7, propositions 9, elements 30, arrows 21, history lines 112


0 errors (0 distinct shapes), 0 warnings
```

## The close-check, C5c-02-p2

`python3 tools/validate.py C5`, run after the pass 6 line and before the head was rewritten:

```
stage C5:
  leg: check; passes 6, propositions 9, elements 30, arrows 21, history lines 100


0 errors (0 distinct shapes), 0 warnings
```

## The close-check, C5c-01

`python3 tools/validate.py C5`, run after the pass 5 line and before the head was rewritten:

```
stage C5:
  leg: check; passes 5, propositions 9, elements 30, arrows 21, history lines 94


0 errors (0 distinct shapes), 0 warnings
```

## The close-check, C5b

`python3 tools/validate.py C5`, run after the packets were rebuilt and before the head was rewritten:

```
stage C5:
  leg: build, packets out; passes 4, propositions 9, elements 30, arrows 21, history lines 94


0 errors (0 distinct shapes), 0 warnings
```

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
