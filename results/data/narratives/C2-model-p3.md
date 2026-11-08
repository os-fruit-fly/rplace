# The model, stage C2, pass 3 (C2a-03)

The model is typed: elements in `model/elements.jsonl`, arrows in `model/arrows.jsonl`, every change in `model/history.jsonl`, loops in `model/loops.jsonl` (empty at pass 3). Pass 1's version is `model.md` and pass 2's is `model-p2.md`, both kept unchanged.

Pass 3 added from the pass 2 story residues:
- one element: the host's line around canvas talk (P20), which brings Boundary work into the model;
- two candidates that earned no arrow: membership carried in (K04) and hosting (P19);
- one arrow (A20);
- a bound on one pass 1 arrow (A10), from two pass 2 story rooms;
- no recut of any tier. The declared split of coalitions from hosting was not taken, because hosting earned no arrow.

Pass 2 had added three elements (P16 to P18), the candidate K03, seven arrows (A13 to A19), bounds on A04, A06 and A07, and the dimension Contention (D08).

The counts come from `out/_analysis/c2_arrow_evidence.py`; pass 3's output is `c2_arrow_evidence-p3a.txt`, and the earlier passes' are kept. The reading of the hosts' rulings is `c2_vetting_concepts-p3.txt`, coded in `c2_vetting_grounds-p3.json` and tallied in `c2_vetting_tally-p3.txt`. The rooms with an empty pre-event brief are in `c2_empty_brief-p3.json`. The apparatus tables are printed by `c2_model_tables.py` (`c2_model_tables-p3.md`), the dimension masses by `c2_dim_mass.py` (`c2_dim_mass-p3.txt`), and the unused themes by `c2_unused_t3.py` (`c2_unused_t3-p3.md`).

The model relates presences and their order in time, never amounts. No coder wrote down a covariation between degrees, so no arrow is drawn between degrees.

## What the model says, in prose

The contract asks the model for four things: how a scattered readership becomes able to act and how it settles what to act on; what sends a group back to that beginning; what brought organizing about when it came, and what followed; and what is left behind. Pass 3's model is a spine, a fork between rooms, a contest, and a close, with the host sub's answer to the calls beside the spine.

**How a scattered readership becomes able to act.** A member proposes a mark or begins it (R01). Calls gather around the start [A02], and calls bring the hands that build [A01]. The cheapest answer to a call is a one-line enrolment, "On it.", which commits a member and asks for nothing back [A12]. Where a member placed first, the call follows the first build (A01's bound). The calls fill the host sub, and the sub draws a line around canvas talk: a megathread, removals under its rules, a canvas sub, members objecting to the flood [A20] (finding F-010). One room in nine has no posts in the week before the canvas (78 of 705); among them are side subs opened for the canvas work and bodies the canvas itself gathered.

**How it settles what to act on.** The room settles what its mark will show (P02). Inside a reply thread, a template settles a design under argument [A11]. Across rooms the first template is as likely to come before design talk as after it, and it can arrive with the first call (A11's bound). The half-built mark tells the next placer what is missing (P03). Decided order, such as a leader, a vote or an oath, is rare (C01; finding F-006).

**What brought organizing about when it came, and what followed.** Organizing came when someone started and others answered [A02] [A01]. The April Fools frame (K01) does not, across rooms, delay that start (finding F-009). Then the road forks.

- **Keeping the work.** Once a mark stands, keeping it becomes the work [A03]. Upkeep under attack outruns one pixel per interval, and members turn to scripts and spare accounts [A06].
- **Keeping the work brings in other rooms.** Upkeep brings a room up against the neighbours whose pixels erode it, and the room talks with them [A04]. A settled border gives members a line they keep [A05]. Short of hands, a room also turns to other rooms for help and receives it [A13]. Talk over a border can open a channel through which the two rooms trade help [A14]. A room under attack joins with other rooms whose works face the same threat [A19] (finding F-008).
- **The contest.** A call to the canvas can also turn its hands against a rival's work [A15]. A room's own call to attack is mostly answered inside the room: members refuse it, rein the attackers in or apologise [A16], or invoke a truce or propose a deal [A17] (finding F-007). Where the attack goes on, it is carried on in talk: taunts, chants, claims of victory, a salute after the fight [A18].

**What sends a group back to the beginning.** A loss. A room that judges it has too few hands stops fighting for its spot and moves [A10]. A room inside a coalition can also move by the coalition's plan, and a late room may write its reason after the move (A10's bound, pass 3). After the move, calls fall from the crisis before it: a call comes in the six hours after the first move in 0.392 of moving rooms, against 0.500 in the six hours before. The room keeps calling more than rooms that did not move, which stand at 0.290 at the same hours (finding F-002, bounded). It goes back to choosing a spot, and often to a fresh call.

**What is left behind.** A finished mark is celebrated together [A07]; where hour 73 cut the work unfinished, the room marks the attempt (A07's bound). What is celebrated is recorded [A08]. What is recorded is carried on into banners, later canvases and lasting groups [A09] (finding F-004). Placement stops at hour 73. After it, a room can only celebrate, record, carry on, and keep up its rivalries in talk.

**Conditions.** The April Fools frame (K01) and doubt about numbers (K02) are conditions. Membership carried in from outside the canvas is in the structure as Collective identity and not in the model. Two candidates stand for it:
- a quarrel carried in (K03): its one test had 9 rooms and failed;
- membership carried in as a whole (K04: the nation's flag and history, a colour, the sub's quarrel, lore, jokes or ideology): it does not come before the attack more than chance (145 rooms, F-011).

**Hosting.** One room's work living on another's mark under the host's rule is a candidate (P19). It follows neither exchange, coalition nor upkeep, and the hosts that give a ground for a ruling most often give space or design (F-012). The six hosts whose rulings are cited all have an empty pre-event brief.

## The elements

The next table lists the 27 elements with their kind, statement, tier, dimension and range. K03, K04 and P19 are candidates, not in the model. The other 24 stand.

| id | kind | statement | tier | dimension | range |
|---|---|---|---|---|---|
| P01 | process | Members call the room's own members, and kindred subs, to come and place for a work: to start it, build it, finish it or hold it. | T4-005 | D01 | from one unanswered post asking who will help to a run of calls, cheering and a set time for placing together |
| P02 | process | The room settles what its mark will show of it: a member proposes a picture, the room argues its design, signs it or leaves it unsigned, or claims a mark others made. | T4-006 | D02 | from a single member's unanswered proposal to a design argued over days and redone |
| P03 | process | Members build the mark and report its state, and the state of the canvas itself tells the next placer what is missing: progress, extension, personal pieces on a shared mark. | T4-007 | D02 | from one report that the logo is half done to a mark grown into several pieces over two days |
| P04 | process | Members circulate a template or coordinates that fix the output pixel by pixel, ask for them, and hold strays to them. | T4-008 | D02 | from one anchor coordinate to an official template enforced against versions |
| P05 | process | Members keep the placed work against erosion: they watch it, repair changed pixels, rally to defend it under attack, cover the night, harden its shape and put upkeep before growth. | T4-013 | D03 | from one member fixing stray pixels to shifts, scripts and calls to defend over many hours |
| P06 | process | Members work out who changed their work and why: they trace placers and rooms, find friendly fire or their own mistake, blame officers, or disown placers acting in their name. | T4-019 | D03 | from one question who keeps adding a line to a dossier on a rival's bots |
| P07 | process | Rooms spare their neighbours' work without a written agreement, rein in their own attackers, apologise for damage and appeal to attackers to stop. | T4-015 | D04 | from one member refusing to cover a neighbour to a room restoring a work it had damaged |
| P08 | process | Rooms settle borders, truces and deals with neighbours by talk, through envoys, hold each other to them and dispute them. | T4-016 | D04 | from a one-line border agreed in a thread to treaties across languages kept and broken over a day |
| P09 | process | Rooms attack others' work by the recurring moves the canvas affords: erasing, encroaching, converting a sign, raiding on a streamer's call, planting a script, griefing for fun. | T4-020 | D08 | from one member's call to deface a rival to a coordinated raid |
| P10 | process | After the work is erased or overrun, the room weighs fighting for the spot against moving, and moves: a new spot, a smaller version, a fresh start. | T3-022, T3-124 | D04 | from a lone member asking where to rebuild to a room relocating together within two hours |
| P11 | process | When a work is up, the room marks it: announces it, celebrates it, credits makers and helpers, reports members' own parts and says what working with strangers meant. | T4-026 | D07 | from one 'We did it!' post to threads of credit and reflection at the close |
| P12 | process | The room records what happened to its work: screenshots and timelapses, reports of its fate, mourning, imagined art, atlas entries, the end marked. | T4-027 | D07 | from one screenshot request to a full account of the week |
| P13 | process | At the close the room decides what of its temporary effort to keep: a later canvas, a new purpose for its canvas sub, the mark in its banner, ties with other rooms, the work remade elsewhere. | T4-028 | D07 | from a wish to do better next year to a canvas-born collective carried into a lasting group |
| P14 | process | Members multiply their hands beyond the rate limit with scripts, bots and extra accounts, and the room governs these machine hands. | T4-009 | D02 | from one member running spare accounts to a shared bot holding several rooms' works |
| P15 | process | A member answers a call or proposal in one line that joins, assents, reports a part done or thanks, and the line asks for nothing back. | FP-01 | none (form pass) | from 'On it.' to 'Did my part.' |
| P16 | process | Rooms help one another's works and trade help: they give pixels to a neighbour's mark, ask other rooms for help, barter help for space or repair, thank their allies, greet them, and turn requests away. | T4-017 | D04 | from one member placing a pixel on a neighbour's flag to rooms trading night-time repairs for room on their mark |
| P17 | process | Rooms join other rooms in coalitions and host them: they meet in shared chats, form alliances, gather kindred rooms, make joint marks, ask a host for space or vet others' requests to build on their own mark. | T4-018 | D04 | from two rooms agreeing to defend each other to a flag hosting dozens of other rooms' works by vote |
| P18 | process | Rooms carry a contest with a rival room in talk: they trade taunts, flood the rival's threads, claim victory, salute the rival after the fight and blame attackers after the close. | T4-021 | D08 | from one taunt in a thread to days of chants, victory claims and an after-the-fight salute |
| K01 | condition | The host sub is keyed as play for April Fools: fakes, takeovers and the one-day licence fill the room, and every claim in it, a call to the canvas included, may be a joke. | T4-001 | D06 | from one fake post in an ordinary sub to a sub given over to parody for a day and a half |
| K02 | condition | The room judges that it has too few hands or too little room for the work it wants: doubt, a canvas judged too full, a work judged absent or outclassed. | T4-012 | D01 | from one member saying there are not enough people to defenders told to give up |
| K03 (candidate) | condition | The community carries a quarrel from before the canvas into it: a rival sub, a sports or national rivalry, an old dispute. | T3-086 | D05 | from one member naming the sub's old rival to a room whose first canvas act is against that rival |
| C01 | claim | Rooms aligned their placers mostly without deciding how they were organized: a decided element of order (a leader, a vote, an oath, a sanction, a division of the work) appears in few rooms, and the question who is in charge is almost never asked. | T4-011, FP-08 | D02 | from rooms that say they wing it to canvas-born factions holding elections |
| R01 | role | The starter: a member who proposes the mark, maps it or begins placing it, and whom others then join. | T3-033, T3-092 | D02 | from a member who only asks to a member who maps and places alone first |
| R02 | role | The envoy: a member who acts for a room toward another room, carrying a proposal between threads or chats. | T3-194 | D04 | from a member calling themself a diplomat once to a standing representative in a shared council |
| P20 | process | The host sub draws a line around canvas talk: moderators gather it into a megathread, remove canvas posts by rule, change posting rules, pause the sub's usual events or disown the work; members open a canvas sub, object to the flood or argue the canvas's worth. | T4-002 | D06 | from one member asking for a megathread to moderators moving all canvas talk to a new sub and removing the rest |
| K04 (candidate) | condition | The room acts as a body it was before the canvas, or as a faith in a colour: it builds and argues the homeland's flag and history, carries in the sub's quarrel, lore, jokes or ideology, or professes and spreads a colour. | T4-022, T4-023, T4-004 | D05 | from a fandom's running joke in canvas talk to a nation's flag fought over as its history |
| P19 (candidate) | process | One room's work lives on another room's mark or territory under the host's rule: guests ask for space or protection, hosts rule on requests, and both sides dispute who may approve. | T3-035, T3-094, T3-099, T3-162 | D04 | from a small room asking to slip into a neighbour's lot to a flag hosting dozens of works by application and vote |

Every element has a range. 21 of the 24 standing elements are named for what they do. Three (K01, K02, C01) are named for a state or a pattern. Fewer than a third are named for what they are about, so the model is not a lattice. K04, a candidate, is named for what it is about.

**Why 24.** Pass 1's 20 elements stand. Pass 2 added three because the pass 1 story could not tell what 9, 6 and 4 of its twenty rooms did:
- exchange between rooms (9 rooms);
- the contest carried on in talk, beside attack as a room's own work (6 rooms);
- coalitions, seen in the rooms that entered the canvas through other rooms.

Pass 3 adds one: the host's line around canvas talk, which the pass 2 story could not tell in 4 of its 32 rooms (unitedkingdom, texas, sweden, starcitizen). Without it the model cannot say what the calls did to the host sub.

Each enters only with a grounded arrow. The quarrel carried in, membership carried in and hosting had no grounded arrow and stay candidates. P19's four third-order themes stay inside P17 while P19 is a candidate.

## The arrows

The next table lists the 20 arrows in the model. For each it gives the kind, the strength, the rooms where the connection statement holds out of those carrying both elements, the permutation null (500 shuffles of labels within each room, seed 20261014), the holds on the early and late sides of the onset contrast, and whether the base rate is beaten.

| id | from -> to | kind | strength | rooms: holds of both (share) | null mean (p95) | early / late holds | base rate beaten |
|---|---|---|---|---|---|---|---|
| A01 | P01 -> P03 | order | strong | 137 of 190 (0.721) | 0.467 (0.521) | 35 of 47 / 3 of 5 | true |
| A02 | R01 -> P01 | order | fair | 64 of 89 (0.719) | 0.473 (0.539) | 21 of 34 / 2 of 2 | true |
| A03 | P03 -> P05 | order | strong | 182 of 291 (0.625) | 0.392 (0.436) | 43 of 69 / 6 of 8 | true |
| A04 | P05 -> P08 | order | fair | 235 of 401 (0.586) | 0.501 (0.539) | 56 of 93 / 6 of 15 | true |
| A05 | P08 -> P07 | order | thin | 106 of 158 (0.671) | 0.600 (0.658) | 25 of 40 / 4 of 4 | true |
| A06 | P05 -> P14 | order | strong | 160 of 203 (0.788) | 0.603 (0.655) | 41 of 50 / 1 of 3 | true |
| A07 | P03 -> P11 | order | strong | 182 of 282 (0.645) | 0.433 (0.475) | 38 of 65 / 5 of 9 | true |
| A08 | P11 -> P12 | order | strong | 225 of 289 (0.779) | 0.565 (0.609) | 61 of 77 / 8 of 15 | true |
| A09 | P12 -> P13 | order | fair | 113 of 145 (0.779) | 0.563 (0.628) | 38 of 47 / 1 of 3 | true |
| A10 | K02 -> P10 | order | thin | 11 of 21 (0.524) | 0.298 (0.429) | 2 of 4 / 1 of 1 | true |
| A11 | P02 -> P04 | transition | thin | 85 of 153 (0.556) | 0.557 (0.621) | 21 of 37 / 3 of 5 | false |
| A12 | P01 -> P15 | transition | thin | never counted (form pass) | - | - | null |
| A13 | P05 -> P16 | order | fair | 171 of 240 (0.713) | 0.596 (0.642) | 44 of 51 / 6 of 8 | true |
| A14 | P08 -> P16 | order | thin | 138 of 214 (0.645) | 0.591 (0.636) | 32 of 45 / 7 of 10 | true |
| A15 | P01 -> P09 | order | strong | 93 of 129 (0.721) | 0.487 (0.550) | 32 of 42 / 2 of 2 | true |
| A16 | P09 -> P07 | order | strong | 82 of 104 (0.788) | 0.529 (0.606) | 19 of 28 / 1 of 2 | true |
| A17 | P09 -> P08 | order | fair | 95 of 172 (0.552) | 0.423 (0.477) | 21 of 43 / 0 of 4 | true |
| A18 | P09 -> P18 | order | fair | 56 of 68 (0.824) | 0.591 (0.676) | 10 of 13 / 0 of 0 | true |
| A19 | P05 -> P17 | order | thin | 106 of 157 (0.675) | 0.569 (0.631) | 21 of 32 / 2 of 7 | true |
| A20 | P01 -> P20 | order | strong | 132 of 155 (0.852) | 0.538 (0.594) | 48 of 57 / 2 of 2 | true |

**The connection statement, written before every count:** "in a room carrying both, the first concept of FROM comes before the first concept of TO". It is a statement of order. The null holds each room's coded turns and their hours fixed, and shuffles which element each turn belongs to. A relation that holds nearly everywhere is not deleted by its base rate. A03, A16 and A20 are in part constitutive: a work must stand before it can be kept, an attack must be called before it can be reined in, and a canvas post must exist before it can be removed or objected to.

Pass 2 ran twelve order tests; seven beat the null. A14 and A19 beat the 95th percentile by 0.009 and 0.044, so they are thin. With twelve tests, one such margin could be chance.

Pass 3 ran seven order tests; three beat the null. One entered the model (A20, 0.852 against a 95th percentile of 0.594). Membership then hosting beat the null by 0.036 on 28 rooms but did not enter: its declared mechanism shows in 5 of the 21 rooms where it holds. Upkeep then coalition, on coalitions without hosting, held at 0.719 against 0.686; it was a retest of A19 that would count only if the split were taken, and A19 is unchanged.

Every arrow is grounded `codes-read`: the concepts were read across rooms, and each arrow rests on quotes and at least one transition in one thread.

Each arrow, with its mechanism, the observation that would show it failed, its bound, the sampled rooms that failed, and its instances:

- **A01, the call brings the hands that build (P01 to P03).** Mechanism: a call brings members to the canvas who then start or extend the mark and say how far it has come. Fails if: build reports come only before any call, or calls are followed by no build report. Present: in 53 of 190 rooms. Bound: where a member has begun the mark before any call, the call follows the first build. Sampled and failing: xenoblade_chronicles. Transitions: 164 in 70 rooms. Instances: "Help us draw Metroid over at /r/place!" [metroid/c0001], answered one minute later by the location [metroid/c0002]; latin c0010 to c0011.
- **A02, a start gives the call something to gather around (R01 to P01).** Mechanism: a member who proposes or begins a mark gives the room something to answer, and calls gather around it. Fails if: calls come only before any proposal or start. Present: in 25 of 89 rooms. Bound: where the room calls before anyone proposes, the proposal answers the call (worldoftanks, day9). Sampled and failing: worldoftanks. Transitions: 59 in 27 rooms. Instance: "Let's draw sips from 'Spacemen' in r/place" [sips/c0026], answered four minutes later by "I'm in." [sips/c0027].
- **A03, a built mark becomes a mark to keep (P03 to P05).** Mechanism: once a mark stands on a surface anyone can change, keeping it becomes the work. Fails if: upkeep comes only before any build report. Present: in 109 of 291 rooms. Bound: where the mark was found already placed, or a rival attacked first, upkeep comes first. All four sampled rooms hold. Transitions: 214 in 85 rooms. Instance: "It's done!" [monsterhunter/c0082], answered one minute later by "time for upkeep now" [monsterhunter/c0083].
- **A04, keeping the mark brings the room to its neighbours (P05 to P08).** Mechanism: keeping a mark against erosion brings the room up against the neighbours whose pixels erode it, and it talks with them. Fails if: border talk comes only before any upkeep. Present: in 166 of 401 rooms. Bound (pass 1): on the late side rooms talk with neighbours first (6 of 15 hold). Bound (pass 2): border talk also comes first where the work was found already placed (unitedkingdom), where a room entered the canvas through another room's offer (yuyuyu), and where neighbours were present from the room's first post (sweden, worldoftanks). Transitions: 293 in 129 rooms. Instance: "We're currently under attack. Seems like its coming from the mona lisa guys, I need help fellow swiss people!" [switzerland/c0044], answered: "We have a peace treaty with the mona lisa guys and the rainbow." [switzerland/c0045].
- **A05, a settled border is a line members keep (P08 to P07).** Mechanism: a settled border gives members a line to keep, and they spare the neighbour's work by it. Fails if: sparing comes only before any talk. Present: in 52 of 158 rooms. Bound: sparing is often tacit and first. Sampled and failing: edmontonoilers, totallynotrobots. Thin. Instance: "We have an agreement with them, we won't mess with each other." [ubc/c0084].
- **A06, scripts arrive under strain (P05 to P14).** Mechanism: upkeep under attack outruns one pixel per interval, and members turn to scripts and spare accounts. Fails if: machine hands come only before any upkeep. Present: in 43 of 203 rooms. Bound: where a room scripted the building from the start; spare accounts can also serve an attack before any upkeep (canucks, pass 2). Sampled and failing: canucks. Transitions: 117 in 53 rooms. Instance: "DEFEND THE FOX WITH EVERYTHING YOU HAVE." [foxes/c0061], answered in one minute by a console script.
- **A07, a finished mark is celebrated together (P03 to P11).** Mechanism: a mark reported done gives the room a finished thing to point at, and the room celebrates it. Fails if: celebration comes only before any build report. Present: in 100 of 282 rooms. Bound: where the first mark was found made by others, the room celebrates the find; where hour 73 cut the work unfinished, the room marks the attempt ("We almost did it!" [ultrahardcore/c0212]; a watermark mourned in totallynotrobots, pass 2). Transitions: 96 in 47 rooms. Instance: suomi c0097 to c0098, "Me teimme sen!".
- **A08, what is celebrated is recorded (P11 to P12).** Mechanism: celebrating the work turns members toward keeping a record of it. Fails if: records come only before any celebration. Present: in 64 of 289 rooms. Bound: on the late side the record often comes first (8 of 15 hold). Transitions: 259 in 108 rooms. Instance: "Place 2017, we did it guys. Good work." [lakers/c0226], answered in one minute by an account of the border [lakers/c0227].
- **A09, the record is what passes on (P12 to P13).** Mechanism: a record of the work gives the room something to carry. Fails if: carrying on comes only before any record. Present: in 32 of 145 rooms. Bound: where a room adopted its mark as an emblem while still building (texans). Sampled and failing: texans. Instance: "Petition to add that image to the subreddit theme." [uiuc/c0155], 46 minutes after the final image [uiuc/c0154].
- **A10, too few hands, so the room moves (K02 to P10).** Mechanism: a room that judges it has too few hands to hold its spot stops fighting for it and moves. Fails if: a move comes with no doubt before it. Present: in 10 of 21 rooms. Bound: where a room moves early by choice; at pass 3, from the pass 2 story rooms, where a late room writes its judgment of too few hands after the move (guatemala, h79.1), and where a room inside a coalition moves by the coalition's plan with no doubt of its own (MiamiHurricanes). Sampled and failing: anarcho_capitalism. Thin. Instance: "Guess we're a little too small to make this work" [paranatural/c0020], answered by "We're in a new spot now." [paranatural/c0021].
- **A11, a template settles a design argued in a thread (P02 to P04).** Mechanism: design talk in a thread is settled by someone posting a template. Its order between rooms is at chance, so it is kept as a transition. Sampled and failing: texas, empiredidnothingwrong. Instance: "Maybe make it 20x20? Or just a purple W?" [udub/c0008], answered: "Will update template image and upload here." [udub/c0009].
- **A12, the cheapest answer to a call (P01 to P15).** Mechanism: a call is answered with one line that commits and asks nothing back. Never counted. Instance: "Help us build the lebanese flag!" [lebanon/c0026], answered "On it" [lebanon/c0027].
- **A13, short of hands, a room turns to other rooms (P05 to P16).** Mechanism: a room keeping its work under strain runs short of hands and turns to other rooms for help, and other rooms send it. Fails if: help is traded only before any upkeep. Present: in 69 of 240 rooms. Bound: where a room helps before it has a work of its own, or comes to the canvas as another room's helper. All four sampled rooms hold. Transitions: 106 in 44 rooms. Instances: "I can only do so much! We need back up stat!" [naruto/c0144], answered three minutes later: "Member of /r/OnePiece here! I'm helping all I can to save our neighbor!" [naruto/c0145]; "Maybe we should ask the Danganropa subreddit for support." [aceattorney/c0050].
- **A14, a settled border opens a channel for help (P08 to P16).** Mechanism: talk over a border opens a channel through which the two rooms trade help. Fails if: help is traded only before any border talk. Present: in 76 of 214 rooms. Bound: thin, 0.009 above the null's 95th percentile. All four sampled rooms hold. Transitions: 108 in 44 rooms. Instance: "Hi, I'll be the ambassador for WIT on /r/place, we arent trying to write over you guys." [littlewitchacademia/c0049], answered: "Thank you very much! I'll stick around as often as I can to help maintain your logo :P" [littlewitchacademia/c0051].
- **A15, a call's hands can turn on a rival (P01 to P09).** Mechanism: a call brings members to the canvas, and some turn its hands against a rival's work instead of, or before, building the room's own. Fails if: attack calls come only before any call to place. Present: in 36 of 129 rooms. Bound: where a room's first canvas act is an attack (edmontonoilers, canucks, anarcho_capitalism), the attack call is the first call. All four sampled rooms hold. Transitions: 34 in 19 rooms. Instance: "me and my roommate are trying to make one in that spot rn if you wanted to join in" [Temple/c0005], answered four minutes later: "Conversely we could aim for right over the Penn State logo" [Temple/c0007].
- **A16, an attack call is refused inside the room (P09 to P07).** Mechanism: a call to attack another room's work is answered inside the room: members refuse it, rein in their attackers or apologise to the target. Fails if: restraint comes only before any attack call, or attack calls draw no refusal. Present: in 22 of 104 rooms. Bound: partly constitutive; where sparing is tacit and first (touhou, calgaryflames), restraint comes before any attack call. Sampled and failing: touhou, calgaryflames. Transitions: 127 in 52 rooms. Instances: "Wipe out the Dolphins. They're building." [nyjets/c0086], answered in one minute: "Nah, keep /r/place neutral." [nyjets/c0087]; "How about we just work on our own and not be assholes" [leafs/c0240].
- **A17, an attack call is met with a truce (P09 to P08).** Mechanism: a call to attack is met by the room's relations with its neighbours: members invoke a truce or propose a deal. Fails if: border talk comes only before any attack call. Present: in 77 of 172 rooms. Bound: early side only; on the late side border talk comes first (0 of 4). Sampled and failing: strangerthings. Transitions: 73 in 35 rooms. Instance: "Let is be us for once who invades! Texas shall fall" [czech/c0151], answered four minutes later: "We [already agreed to a truce here]" [czech/c0153].
- **A18, an attack is carried on in talk (P09 to P18).** Mechanism: an attack makes the rival a named party, and the contest is carried on in taunts, chants, claims of victory and a salute. Fails if: rivalry talk comes only before any attack. Present: in 12 of 68 rooms. Bound: early side only; no late room carries both. All four sampled rooms hold. Transitions: 50 in 14 rooms. Instances: "Help us hijack the WPI r/place!" [rpi/c0024], answered: "Come at us bro" [rpi/c0026]; "TSM fans may far outnumber us, but the simple fanaticism of us CLG fans ensured a loss on your part this day." [clg/c0041].
- **A19, under attack, works defend each other (P05 to P17).** Mechanism: a room keeping its work against attack joins other rooms whose works face the same threat. Fails if: coalitions come only before any upkeep. Present: in 51 of 157 rooms. Bound: on the late side 2 of 7 hold, since late rooms enter the canvas through other rooms (bretagne, MiamiHurricanes, yuyuyu); thin. Sampled and failing: bretagne. Transitions: 52 in 28 rooms. Instance: "Some people are attacking the naruto logo on r/place! Please defend! They are from r/forsen" [naruto/c0167], answered in one minute: "/r/Funhaus and /r/Naruto should stick together." [naruto/c0168].
- **A20, the calls fill the host sub, and the sub draws a line (P01 to P20).** Mechanism: calls to the canvas flood the host sub, and its moderators or members answer by drawing a line around canvas talk: one thread, removals, a canvas sub. Fails if: the line comes before any call, or the line's words name no canvas flood. Present: in 23 of 155 rooms, of three kinds: the sub's automatic rules remove the first call as it is posted (9 rooms, three in the same hour); a canvas sub or megathread is set up before the host carries any call (7); members dismiss the canvas or object to other rooms' canvas posts before the room calls (7). Bound: partly constitutive, and those three paths. All four sampled rooms hold; in one (transformers) the first line is a member's judgment of the canvas after the close and names no flood. Transitions: 29 in 22 rooms. Instances: "Help build a Mario in /r/place!" [nintendo/c0120], answered 17 minutes later: "Maybe want to go to the /r/place Megathread where we're trying to build a Mario... slowly..." [nintendo/c0121]; "Can we just stop posting about r/place please? It's becoming just spam at this point" [rocketleague/c0722]; "N'y a t il pas de super poteau pour cette requête?" [france/c0444].

## Theorised arrows, and the model with and without them

No arrow rests on my reading alone. Two arrows do not rest on an order count that beats a shuffle, and they are listed apart as theorised:
- A11: its order across rooms is at chance, and it stands on transitions inside threads only.
- A12: never counted, on exemplars only.

Four more are counted and beat the null, but thinly: A05, A10, A14 and A19.

**Without the two theorised arrows**, the model can no longer say how a room settles a design under argument, or why calls are cheap to answer.

**Without all six weak arrows**, the model keeps the spine (A02, A01, A03, A04, A06), the host's line (A20), exchange under strain (A13), the contest (A15, A16, A17, A18) and the close (A07, A08, A09). It loses why rooms with neighbours mostly do not fight (A05), what sends a room back (A10), help traded along a border (A14), and coalitions (A19). The second of the four things then has no counted answer.

## The model on the dimensions

The next table gives, per dimension, the mass of coded turns answering coded turns across the dimension's boundary (`c2_dim_mass-p3.txt`; the masses do not depend on the elements and are unchanged from pass 2). Rooms are beside each count. The last three columns drop every transition touching a double. Of 56,071 transitions with both ends placed, 31,636 touch no double.

| dimension | in (rooms) | out (rooms) | internal (rooms) | in, no doubles | out, no doubles | internal, no doubles |
|---|---|---|---|---|---|---|
| D01 Critical mass | 3579 (415) | 5188 (387) | 3100 (420) | 696 (210) | 1076 (179) | 1647 (284) |
| D02 Coordination without command | 7612 (557) | 8252 (541) | 8686 (574) | 1510 (299) | 1685 (296) | 4362 (406) |
| D03 Maintenance | 5616 (486) | 4959 (459) | 3717 (463) | 1222 (242) | 1243 (212) | 1929 (283) |
| D04 Order without law | 8790 (576) | 5616 (509) | 8584 (581) | 1776 (325) | 892 (251) | 4135 (409) |
| D05 Collective identity | 3055 (295) | 3430 (240) | 2904 (287) | 565 (162) | 643 (125) | 1496 (209) |
| D06 Host framing | 1947 (234) | 1318 (172) | 9930 (397) | 622 (135) | 226 (69) | 6839 (335) |
| D07 Imprinting | 3641 (490) | 5609 (479) | 5763 (547) | 672 (254) | 1396 (272) | 3175 (416) |
| D08 Contention | 2341 (235) | 2209 (216) | 1480 (213) | 407 (95) | 309 (78) | 583 (109) |

The next table states the arrows at the dimension level. Each row names the arrows beneath it, a mechanism written at that level, the observation that would show it failed, the strongest instance beneath, and the transition mass from the first dimension to the second.

| dimensions | arrows beneath | mechanism at the dimension level | fails if | strongest instance | mass |
|---|---|---|---|---|---|
| Critical mass to Coordination without command | A01 | hands gathered by a call are spent on the mark the room is aligning on | aligned work comes only before any gathering | metroid c0001 to c0002, 1 minute | 1,727 |
| Coordination without command to Critical mass | A02 | a coordinating role, the starter, gives the call something to gather around | calls come only before any start | sips c0026 to c0027, 4 minutes | 1,346 |
| Coordination without command to Maintenance | A03 | aligned work, once standing, becomes something to keep | upkeep comes only before any aligned work | monsterhunter c0082 to c0083, 1 minute | 1,684 |
| Maintenance to Order without law | A04, A13, A19 | keeping a work brings a room into relations with other rooms: talk, help and coalitions | talk, help and coalitions come only before any upkeep | naruto c0144 to c0145, 3 minutes | 1,558 |
| Maintenance to Coordination without command | A06 | upkeep under strain changes how the room multiplies its hands | machine hands come only before any upkeep | ubc c0089 to c0090, 2 minutes | 1,432 |
| Coordination without command to Imprinting | A07 | aligned work, once finished, is celebrated | celebration comes only before any finished work | suomi c0097 to c0098, 17 minutes | 924 |
| Critical mass to Contention | A15 | hands gathered by a call can be turned against a rival's work | attacks come only before any call | Temple c0005 to c0007, 4 minutes | 182 |
| Contention to Order without law | A16, A17 | a contest is answered by the order between rooms: refusal, restraint, a truce | restraint and truces come only before any attack | nyjets c0086 to c0087, 1 minute | 719 |
| Critical mass to Host framing | A20 | gathering hands floods the host sub's channels, and the host sub draws a line around them | the line comes only before any gathering | nintendo c0120 to c0121, 17 minutes | 262 |

One cross-dimension arrow is reported as mass, not as a dimension-level arrow. A10 runs from Critical mass to Order without law, but it rests on 21 rooms, against a mass of 1,257 transitions of other traffic. A12 runs from Critical mass to a form-pass element outside the dimensions. A05 and A14 lie inside Order without law, A08 and A09 inside Imprinting, A11 inside Coordination without command, and A18 inside Contention.

What the arrows and masses show:
- **Contention is not residue.** One arrow runs in (from Critical mass) and two run out (to Order without law). Its masses are close to balanced (407 in, 309 out, without doubles). The contest is fed by mobilized hands and answered by the order between rooms.
- **Order without law draws in about twice what it sends** (1,776 against 892 without doubles). Six arrows run into it from other dimensions (A04, A13 and A19 from Maintenance, A10 from Critical mass, A16 and A17 from Contention) and none out, so it is residue: the model ends there.
- **Imprinting is residue too:** A07 runs in and nothing runs out. Its masses say otherwise: 1,121 transitions go into Maintenance and 1,298 into Order without law, since "we did it" posts are answered by repair and border talk (see the ungrounded relationships).
- **Host framing is almost all internal** (6,839 against 226 out, without doubles). One arrow runs in (A20, from Critical mass) and none out, so it is residue: the host's line answers the calls, and no arrow says what the line does to the room's work. Finding F-009 says the play frame does not delay the canvas work across rooms.
- **Collective identity carries no arrow.** Its two candidates failed: the quarrel carried in on 9 rooms, and membership carried in as a whole on 145 (F-011).

## Dynamics

- **Loops.** None is grounded. A within-room loop needs one room's dated chain to run the whole cycle. Pass 3 adds no closing arrow; A20 runs out of the spine and nothing runs back from it. Pass 2 added none either: the contest runs from calls to attack to restraint or truce, and nothing grounded runs from restraint or truce back to a call. The move-and-rebuild candidate (loss, move, build, keep) still lacks an arrow from the move to building that beats its base rate. `model/loops.jsonl` is empty.
- **What returns a room to a state it had left:** a loss. The room goes back to choosing a spot and cutting its design to what can survive. Its calls fall from the crisis before the move, but it keeps calling more than rooms that did not move (F-002, bounded).
- **What is irreversible across hour 73:** placement stops. Calls to place, building, upkeep, machine hands, attacks, help traded in pixels and deals over pixels end with it. After hour 73 a room can celebrate, record and carry on (A07, A08, A09), call for a later canvas, and keep a rivalry going in talk (victory claims, salutes, blame after the close). Its organizing for this canvas is over.

## Ungrounded relationships

These relations have a count and no mechanism I have stated and tested. They are correlations, `in_model` false by definition, listed so that stage C5 can mark anything that rests on them. Counts are from `mem.py pairs` and `c2_dim_mass-p2b.txt`.
- **Completion ritual answered by repair work:** 1,167 transitions in 274 rooms (fourth-order ledger).
- **Completion ritual answered by border talk:** 805 transitions in 221 rooms.
- **Coordination without command into Order without law:** 2,823 transitions, the largest cross-dimension mass, and 1,848 back.
- **Imprinting into Order without law:** 1,298 transitions.
- **Collective identity into Order without law:** 848 transitions.
- **Order without law into Contention:** 598 transitions. Deals broken may turn into attacks; no arrow from talk to attack was tested.
- **Membership carried in, then hosting** (K04 to P19, pass 3): 21 of 28 rooms (0.750 against a 95th percentile of 0.714). It has a count and a declared mechanism (guests come to the body's mark), but the mechanism shows in 5 of the 21 rooms. 16 show the reverse role: a room asks a host for space after laying its own mark (`c2_first_concepts-K04-P19-p3.txt`). Not in the model.
- **Hosting, then coalition:** 12 of 17 rooms carrying both put hosting first. The reverse of a declared test, not declared and not tested.

## Looked for and not found

Each of these was tested and not grounded. They are results (rule 8).

Pass 1:
- **Attribution as the hinge between restraint and contention.** P06 to P07 holds in 0.452 of rooms against a null mean of 0.456. P06 to P09 holds in 0.194 against 0.408, reversed.
- **A room under attack, then repair or a move.** P09 to P05 holds in 0.444 against a 95th percentile of 0.449. P09 to P10 holds in 0.561 against 0.610.
- **Doubt, then calls.** K02 to P01 holds in 0.175 against 0.352, reversed.
- **Machine hands, then upkeep.** P14 to P05 holds in 0.202 against 0.375, reversed.
- **Emblem before template, as an order between rooms:** at chance.

Pass 2:
- **Exchange, then sparing.** P16 to P07 holds in 0.427 against 0.494.
- **Border talk, then coalition.** P08 to P17 holds in 0.632 against a 95th percentile of 0.654.
- **Exchange, then coalition.** P16 to P17 holds in 0.384 against 0.450.
- **A quarrel carried in, then attack.** K03 to P09 holds in 2 of 9 rooms.
- **Attack, then the room's own building.** P09 to P03 holds in 0.385 against 0.469, reversed: rooms build first.
- **The play frame delaying the canvas work.** 59 frame-filled rooms start at a median h21.80, against h20.25 for 275 others (p 0.43; F-009). A first run that undercounted the frame found the opposite on 8 rooms. It was corrected before the result was used.
- **A move stopping the room's calls.** A move lowers calling from the crisis before it, but not below other rooms (F-002, bounded; `c2_relocation_window-p2.txt`).

Pass 3:
- **Membership carried in, then attack.** K04 to P09 holds in 0.593 of 145 rooms against a 95th percentile of 0.634 (F-011).
- **Exchange, then hosting.** P16 to P19 holds in 0.379 of 29 rooms against 0.552.
- **Coalition, then hosting.** Coalitions without hosting, then P19, holds in 0.294 of 17 rooms, below the null mean of 0.451.
- **Upkeep, then hosting.** P05 to P19 holds in 0.635 of 52 rooms against 0.654.
- **A host admitting guests by fit with the body it carried in.** Of 23 cited rulings that give a ground, 6 give fit with the nation, colour or theme, 12 give space or design, and 5 give ties (`c2_vetting_tally-p3.txt`; F-012).

## The tiers the arrows run between, and what the model does not use

Most arrows join two elements tied to fourth-order themes. A02 runs from a pair of third-order themes (R01) to a fourth-order theme. A10 runs from a fourth-order theme to a pair of third-order themes (P10). A12 runs to a form-pass finding (P15). Four standing elements carry no arrow: P06, K01, C01 and R02.

The next list gives the 53 of 197 third-order themes the model does not use (`c2_unused_t3-p3.md`), grouped by fourth-order theme. Boundary work is now used (P20). K04's members are listed as unused, since K04 is a candidate. P19's members are not listed: they stay in P17, which is in the model.
- **T4-003 Sensemaking** (3): T3-016 explaining what the canvas is; T3-018 decoding the finished picture's details; T3-052 remarking on neighbouring pictures.
- **T4-004 Frame bridging** (4; in the candidate K04): T3-086 carrying in the sub's quarrel (the candidate K03); T3-179 arguing ideology from the canvas; T3-135 telling clashes as fandom lore; T3-031 playing the room's in-jokes.
- **T4-010 Backstage decision-making** (7): T3-014 moving planning into a chat; T3-107 keeping planning in the thread; T3-109 arguing which chat to use; T3-114 disputing the chat's authority; T3-116 hiding the plan from rivals; T3-132 spying in a rival's chat; T3-152 announcing what the chat decided.
- **T4-014 Territoriality** (5; its other two members are P10): T3-020 choosing a canvas spot; T3-039 yielding space when asked; T3-123 refusing to give up space; T3-012 granting a neighbour room; T3-045 arguing who was there first.
- **T4-022 Flagging the nation** (12; in the candidate K04): T3-065 building the homeland's flag; T3-078 helping kin nations' flags; T3-079 joining flags with a heart; T3-085 weighing the room against nations; T3-113 drawing national emblems; T3-145 feeling national through the canvas; T3-165 debating friendship with historic enemies; T3-180 disputing national belonging; T3-081 casting fights as national history; T3-130 reading national politics in pixels; T3-142 making ethnic jokes about rivals; T3-166 arguing the nation's historical record.
- **T4-023 Neo-tribes** (6; in the candidate K04): T3-137 joining an outside group's build; T3-096 hailing the colour corners; T3-163 defecting from a rival faction; T3-171 spreading a faction's colour; T3-174 professing loyalty to a colour; T3-190 splitting a faction over doctrine.
- **T4-024 Symbolic boundaries** (5): T3-080 arguing over political symbols; T3-146 covering swastikas and hate symbols; T3-177 calling to draw swastikas; T3-182 shutting down bigotry in chat; T3-143 judging whether a joke offends.
- **T4-025 Visibility returns** (9): T3-051 pushing posts up the rankings; T3-053 spelling slogans with post titles; T3-110 placing a tile as payment; T3-044 recruiting canvas visitors; T3-129 making passers-by notice a demand; T3-189 fearing newcomers the mark draws; T3-196 drawing lapsed fans back; T3-127 seeking the creators' notice; T3-147 sharing the work's press coverage.
- **Unpicked by any fourth-order theme** (2): T3-017 carrying on ordinary sub talk; T3-133 recovering a hacked sub.

**What was dropped, and which of the five it failed.** The five are the concept and the contract's four things. Each item below was considered as an element and left out, because at pass 3 the model says nothing different about any of the five without it.
- **Sensemaking** would bear on becoming able to act. No arrow was formed.
- **Frame bridging, Flagging the nation and Neo-tribes** would bear on becoming able to act and on what followed, as membership carried in. Tested at pass 3 as one condition (K04): it does not come before the attack more than chance, and its count before hosting rests on the reverse of its declared mechanism. The quarrel carried in alone failed at pass 2.
- **Symbolic boundaries** would bear on settling what to act on (which symbols may be drawn). Left out of K04 by declaration; no arrow was formed.
- **Hosting** (four members of Meta-organization) would bear on what followed between rooms. Tested at pass 3 as P19: it follows neither exchange, coalition nor upkeep.
- **Backstage decision-making** would bear on settling what to act on. Chat decisions reach the record only as announcements.
- **Visibility returns** would bear on what is left behind. No arrow was formed.

## Where the model should break, in its own terms

- **Rooms whose canvas work is one thread** (ultrahardcore): the spine collapses into one exchange, and the model can still tell it (below).
- **Rooms where a starter places alone and no one answers:** R01 with no P01.
- **Bag rooms** (greenlattice t03), where many acts between rooms each carry a few concepts: P07, P08, P09, P16 and P17 cannot be told apart there.
- **Late rooms that enter the canvas through other rooms** (bounds on A04, A17, A19): there the order between rooms comes before the room's own work.
- **Rooms that host other rooms' works on their own mark** (sweden, catalunya, smashbros, placeDE, greenlattice, orderofthebluecorner, purplecorner, among the pass 3 story rooms): P17 holds them only as a coalition; hosting (P19) is a candidate with no grounded arrow, and the vote or form that decided each guest is decided order the model counts as rare.
- **Rooms the canvas founded** (78 of 705 have an empty pre-event brief). The six hosts whose rulings are coded as vetting are all among them, but hosts with readers before the canvas (sweden, catalunya, smashbros) rule on guests too. The pass 3 story's opening carries these rooms: the founded rooms read at pass 3 (rainbowgrid, pgang, placecanada, CKCrusaders, purplecorner, greenlattice, orderofthebluecorner) run the story's steps from their founding. What three of them do after it, as hosts ruling on guests and as colour faiths naming a rival, the model does not reach.
- **Rooms whose answers the coders dropped:** the enrolment and many replies are not in the record.

## The three strongest arrows, read as artefacts

The three are chosen by the gap between share and null mean: A20 (0.314), A16 (0.259) and A01 (0.254). A15 (0.234), third at pass 2, is now fourth. For each, the argument is that the order comes from which turns the coders chose to code and how they labelled them.

- **A20.** A removal, a pointer to the megathread or an objection to the flood is coded as such only when there is a canvas post to remove, point or object to, so the line would follow the first call by definition. What separates it from a pure artefact: P20 also holds acts that need no call in the host sub (opening a canvas sub, arguing the canvas's worth), and 23 rooms draw the line first. In 22 rooms a line by another member or a moderator replies to a specific call in the same thread within minutes (29 transitions).

- **A16.** A refusal is coded as reining in an attacker only when there is an attack call to refuse, so restraint would follow attack by definition. What separates it from a pure artefact: P07 also holds tacit sparing and apologies, which need no prior call, and 22 rooms spare first. In 52 rooms a refusal by another member replies to a specific attack call in the same thread, within minutes (127 transitions).
- **A01.** A call is usually a submission title, the first turn of its thread, and build reports are comments under it. What separates: the null keeps each room's coded turns and hours fixed, so the choice of turns is held constant. 53 rooms report building before any call, and 70 rooms have a build report replying to a call (164 transitions).
## Two tests

**Every element has a range.** See the elements table.

**The odd room: ultrahardcore,** read again whole at pass 3 against the pass 3 model. The April Fools frame (K01) filled the room from h7.7 to h40: 193 of its 212 coded items fall before h40, and only a question about the canvas at h40 touches it. The moderators' play with their own powers belongs to the frame; the host sub drew no line around canvas talk, so A20 does not fire. Across rooms the frame does not delay the canvas work (F-009), so ultrahardcore's late start is the room's own, inside the frame. At h57.6 a starter asked for a design (R01). Within half an hour the thread had a proposal (P02), a template, a spot and an order: "Make it completely red first." [ultrahardcore/c0209] (A11). Building followed (P03). There was no second call, no neighbour, no help from another room and no contest, so A03, A04, A13 and A15 never fired. At the close the room marked an attempt cut short ("We almost did it!" [ultrahardcore/c0212]; A07's bound) and recounted it (P12). The model tells it as a late, compressed spine that the clock cut before upkeep. What it cannot say is why this room, inside a frame that does not delay most rooms, came so late.
