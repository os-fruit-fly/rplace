# Room form F, the spot: lost, chosen or yielded, and building again: the form account

Written at D5a-41, 27 October 2026. The model is the version frozen at D3 (46384686d6173fdeb4c749667478c1363e675bc6b52bb6f4fdc211d387e68525). Form F is one of the six room forms of the cut J ruled at D4a-08 (`room-forms-D4a08c.*`); how every room reaches its form is in `room-forms-allocation.md`. It holds 56 of the 705 analysed rooms. 34 are defining rooms: rooms with 5 or more selected changes, which shaped the form. 16 are thin rooms (1 to 4 selected changes) and 6 are core rooms (no selected change), placed afterwards. Thin and core rooms weigh less: every share, signature, theme count, representative choice and split below is read on the 34 defining rooms, and the thin and core rooms are named in section 15. Form F is the smallest of the six forms, and its rooms have the shortest records: the median defining member has 64.5 coded concepts. Shares here rest on few rooms.

A room form is not a branch: it gathers rooms by the whole mix of their changes (two thirds) and their codes (one third), and the 35 branches are the level below it (section 12). The form is a pole of a continuum: 2 of its 34 defining rooms lie nearer another form's centre (section 13). This file sits beside the room-forms files, not in `forms/`, because the stage's close-check reads every account in `forms/` as a branch account (`departures.jsonl` line 18). Hours are counted from the start of the event (h+).

## 1. How these rooms organized, as a narrative

In these 56 subreddits most of the talk was about where the mark could go. Members looked for a free spot, asked neighbours for space, gave up a spot when its owner claimed it, moved after a loss, and began again at the new spot. One room, r/dallasstars, started at six spots or more.

The search began with the canvas already full. A r/sips member wrote, "we need to find a good free spot though" [sips/c0029], and another, "it's just 15x5 pixels surely we can squeeze it somewhere!" [sips/c0063]. A r/phish member said what had gone wrong the night before: "A bunch of us tried to get fluffhead on the r/place mural last night, but due to lack of coordination and a ton of other "factions" it was too difficult." [phish/c0019].

Rooms asked before they built. A r/sips member held the room back: "right we need to ask for permission from green lattice before starting, the admin just went offline in their discord, I'll apply when I get the chance." [sips/c0042]. When an early builder started, the same member wrote, "great, but I think we should wait for permission!" [sips/c0045]. Later the room gave up on that host: "turns out alot of people are applying for the green lattice. Should we find another spot?" [sips/c0048].

Rooms gave up a spot when a neighbour claimed it. In r/dallasstars a neighbour wrote, "Hey guys, we've been working our logo on that spot" [dallasstars/c0064]. A member answered, "Sorry, looked unoccupied. We'll relocate." [dallasstars/c0065], and the neighbour replied, "No worries, good luck!" [dallasstars/c0066]. Rooms also moved after a loss. A r/UPenn member wrote, "Someone took the spot, moving to (212, 892)" [UPenn/c0002]. In r/portal members asked, "Do we move our thing a little bit to the left or do we fight back when the time comes?" [portal/c0028], then "I think we lost..." [portal/c0029], and then "Ok i create a new plan. But we already wasted so much time.." [portal/c0034].

After a move the room built again. A r/dallasstars member called the room to a new spot after several had failed: "I KNOW WE'VE TRIED THIS IN A BUNCH OF SPOTS BUT (957, 605) IS LARGELY UNOCCUPIED. COME HELP!" [dallasstars/c0067]. Later a member reported, "Furthest we've gotten I think." [dallasstars/c0076]. Rooms that built beside others made terms at the border. A r/phish builder was asked, "Can you move it over a few pixels to the right to avoid the Koi?" [phish/c0028], and answered, "can we just agree to let your koi tail be on top a little bit of our logo?" [phish/c0029]. At the close a r/UPenn member wrote, "Place is over - we made the final canvas!" [UPenn/c0019].

## 2. What the form does

These elements are instantiated in 80 per cent of the defining members or more (`_analysis/d5f_model.py`, current ledger, particular lines included). The model's prose says them so.

- P01 (34 of 34; 100 per cent of the 558): "The room calls its own members, and kindred subs, to come and place for a work: to start it, build it, finish it or hold it."
- P02 (34 of 34; 100 per cent of the 558): "The room settles what its mark will show of it: a member proposes a picture, the room argues its design, makes its land's flag or emblems the mark, signs it or leaves it unsigned, claims a mark others made, adds to it or enlarges it, or adds a personal piece to a shared mark."
- P04 (34 of 34; 97 per cent of the 558): "Members circulate a template that lays out the mark pixel by pixel, or coordinates that locate it, ask for them, and ask strays to keep to them."
- R01 (34 of 34; 96 per cent of the 558): "The starter: a member who proposes the mark, maps it or begins placing it. Others joining is not part of the role: it is the answer to the room's call (P15), in the order A02 and A01 state."
- P03 (33 of 34; 97 per cent of the 558): "The room builds its mark, and members report its state to the thread: what is placed, done or missing, and where."
- K02 (32 of 34; 82 per cent of the 558): "The room judges that it has too few hands or too little room for the work it wants: doubt, a canvas judged too full, a work judged absent or outclassed."
- P12 (32 of 34; 97 per cent of the 558): "The room records what happened to its work and to the canvas around it: screenshots and timelapses, reports of its fate, mourning, imagined art, atlas entries, the end marked."
- P24 (30 of 34; 89 per cent of the 558): "Members ask what the canvas is, how to place, what a call or a name means and what a picture shows, and others explain the rule, the timer, the controls, whose mark a picture is and what happened. They ask before, during and after the close, and some questions get no answer."
- P15 (29 of 34; 91 per cent of the 558): "A member answers a call or proposal in one line that joins, assents, reports a part done or thanks, and the line asks for nothing back."
- P11 (28 of 34; 96 per cent of the 558): "When a work is up, the room marks it: announces it, celebrates it, credits makers and helpers, reports members' own parts and says what working with strangers meant."

The model has the room call its members (P01), settle its design (P02), build (P03) and circulate a template (P04), and it has the room judge that it has too few hands or too little room (K02). These rooms do all of it. K02 is instantiated in 32 of 34 defining members (94.1 per cent), against 82.4 per cent of the 558. Keeping (P05), which 93.4 per cent of the 558 instantiate, is instantiated here in 22 (64.7 per cent). The difference is in what these rooms change, and in what their short records hold.

## 3. What it does differently, element by element and arrow by arrow

**The change signature.** The form's defining members change three fourth-order columns more than the defining population does (at 1.5 times its share or more, in a third of the members or more). Territoriality, the theme of space and claims to it, is changed by 94.1 per cent of them, against 28.0 per cent of the 558 (share ratio 5.36), the highest ratio of any form's signature. Mobilization, the theme of calls, by 44.1 per cent, against 27.6 (ratio 1.67). The link from repair work to the negotiated order, lines that join keeping the mark to terms with neighbours, by 41.2 per cent, against 28.3 (ratio 1.55).

**Element by element and arrow by arrow.** The table gives every element or arrow and op that 14 defining members or more change, at 1.2 times the defining population's share or more (`_analysis/d5f_facts.py`). A selected line specifies the model (add-condition, add-step), restricts it (restrict), connects two of its parts (link) or contradicts it. The kind of a line is not relied on (J: kappa 0.08).

| element or arrow | op | defining members with a line | share | share among the 558 | ratio |
|---|---|---|---|---|---|
| A10 | restrict | 16 | 0.471 | 0.337 | 1.40 |

The rule's floor of 14 members is 41 per cent of this form's 34 defining members, so one row passes. Below the floor, and flagged as such, three more rows reach 1.5 times the population's share with 8 to 13 members: A04 restrict (13 members, 38 per cent against 23), P03 link (12, 35 per cent against 23) and A06 restrict (9, 26 per cent against 17).

No defining member holds a contradict line, so these rooms replace nothing in the model. I read the lines behind the signature whole: the 140 Territoriality-change lines of 32 defining members (`_analysis/d5a41_dump_t4014.txt`), and the restrict lines in section 7.

- **A10, from judging too few hands to the move: restricted (16 members, 47 per cent against 34).** Section 8 reads these lines. The room moved after a loss, a taken spot or a neighbour's claim more than for too few hands.
- **A04, from keeping to border talk: restricted (13 members, below the floor).** Every one of its 13 lines here says the arrow fails: the room talked with its neighbours before it had a mark to keep. r/sips: "Neighbour permission was discussed as a prerequisite to building, so border talk cannot locally be confined to an outcome of maintaining an existing mark." r/wildhockey: "Border and permission talk can arise during insecure construction rather than require upkeep of an established mark."
- **P03, building: connected (link 12 members, below the floor).** The links run from a move back to building. r/stargate: "Repeated losses and relocation are followed by renewed construction and a completed smaller gate." r/UPenn: "The move returns directly to construction through use and correction of the new anchor." The call returns as well. r/gratefuldead: "A replacement thread carrying the new spot and design renewed the call for helpers."
- **P19, a room's work under a host's rule: conditioned and restricted (5 and 6 members).** Rooms asked a host for space, and the record holds the request more than the answer. r/UPenn: "Instantiate only the request stage, leaving a grant, protection promise and actual host-governed residence unresolved." r/warthunder: "A prospective host's own exposure to attack can cause refusal of a guest's request for space."
- **P27, choosing the spot before any loss: linked and restricted (4 and 5 members).** The choice of a spot recurs after earlier losses. r/penguins: "Prospective site selection also occurs after earlier losses, so the temporal bound must concern the particular site decision rather than the room's entire history."
- **A06, from upkeep to scripts: restricted (9 members, below the floor).** Scripts came with the building, not only after upkeep strained. r/sbu: "Treat upkeep-driven automation as one route rather than the explanation for a script offered from the outset to create the mark."

**What the model would not predict.** The model has a room that judges its hands too few move its work (A10), and the account grounds no loop from the move back to building. In these rooms the move came after a loss, a spot taken or a neighbour's claim, and the room built again at the new spot, in some rooms more than once. The model has border talk follow keeping (A04). In these rooms talk with neighbours came first: the room asked for space before it built. And the model has a host rule on a guest's request (P19); in the P19 lines here the record holds the request and leaves the ruling unresolved.

The rooms that show the form best, by the rule in section 11, are r/dallasstars and r/sips; the one that shows it least well is r/ducks.

**What the claim rests on.** The form is a cut of the allocation (changes two thirds, codes one third, Ward's method, six forms by J's ruling). Its stability on matched subsamples is about 0.21, and 2 of its 34 defining rooms lie nearer another form's centre. The table's counts are the ledger's, on few rooms. That members asked for space, yielded and moved for reasons other than too few hands, and built again is a claim on their words, through `cite.py`, in sections 1, 4 and 11. One kind of evidence does not stand in for the other.

**The name, read against the members.** The name is "the spot: lost, chosen or yielded, and building again". The strongest argument that it names the cut rather than what the rooms did: it lists four acts, and the form's lean is one theme, territoriality, held by 32 of 34. A reader who suspected the name would look for members that hold the theme without moving or building again. The members' lines and words show all four acts: the spot lost (r/UPenn, r/portal), chosen (r/sips), yielded (r/dallasstars), and building again (in 8 members territoriality lines run from a move back to building; P03 is linked in 12 of 34). Building again is the least held of the four by these counts. The name holds as a description of the form's lean. I make no renaming proposal.

## 4. The concepts it employs

First-order concepts for each change the form leans to, through `cite.py`:

- **A free spot sought.** "we need to find a good free spot though" [sips/c0029].
- **Permission asked before building.** "great, but I think we should wait for permission!" [sips/c0045].
- **A spot yielded to its owner.** "Sorry, looked unoccupied. We'll relocate." [dallasstars/c0065].
- **The move after a spot was taken.** "Someone took the spot, moving to (212, 892)" [UPenn/c0002].
- **Fight or move, weighed.** "Do we move our thing a little bit to the left or do we fight back when the time comes?" [portal/c0028].
- **Too few hands named.** "The real problem is there isn't a big enough Hawkeye presence on Reddit, sadly." [uiowa/c0004].
- **The call again, at a new spot.** "I KNOW WE'VE TRIED THIS IN A BUNCH OF SPOTS BUT (957, 605) IS LARGELY UNOCCUPIED. COME HELP!" [dallasstars/c0067].
- **Terms at the border.** "can we just agree to let your koi tail be on top a little bit of our logo?" [phish/c0029].
- **A host's own reason to protect the space.** "I'm working with the Brazillians and i approve of your placement - helps us defend against vandalism in the surroundings." [phish/c0034].

## 5. Composition here

Three judgments are kept apart.

**The original global model (historical).** `verdicts-D.jsonl`, by the last analyst ruling or else the readers' agreement. All 56 members: composes 33, composes with residue 20, does not compose 0, cannot tell 3. The 34 defining members: composes 18, composes with residue 16, does not compose 0, cannot tell 0. The three that cannot tell are placed rooms: r/FlipnoteStudio3D, a thin room (1 selected change, 2 coded concepts), and r/nonbinary and r/PokemonSage, core rooms (1 and 2 coded concepts). Their records hold 1 or 2 coded concepts each. These verdicts describe the unadapted model at the first return.

**The adapted local accounts.** By `adaptation-returns.jsonl` and the current model hash (46384686), as `vlib.local_return_states` reads them, all 56 members are unresolved; none is validated and none has insufficient evidence. The limit D3 named is the same for each: the labelers marked every local account unresolved, and prior.md section 3's measure of local validation was not computed (J after the D3c interview). The unresolved members are:

r/achievement_hunter, r/berkeley, r/clubpenguin, r/cmu, r/corridor, r/COSI, r/dallasstars, r/day9, r/dbz, r/diablo, r/ducks, r/eesti, r/ethoslab, r/FlipnoteStudio3D, r/foxstevenson, r/gameboy, r/gratefuldead, r/GreenEmpire, r/haskell, r/hoodr, r/httyd, r/KState, r/latin, r/lexington, r/miraculousladybug, r/nbaspurs, r/nonbinary, r/Northwestern, r/nyu, r/pebble, r/penguins, r/phish, r/planetside, r/PokemonSage, r/portal, r/predators, r/Produce101, r/qotsa, r/Redox, r/sbu, r/sips, r/snsd, r/stargate, r/streetfighter, r/tenma, r/TheID, r/transgender, r/TreePlace, r/twentyonepilots, r/twitch, r/ufl, r/uiowa, r/UNLincoln, r/UPenn, r/warthunder, r/wildhockey

**The shared form explanation: supported as a lean, unresolved as an explanation.** One change binds nearly every defining member: 94.1 per cent change territoriality, against 28.0 per cent of the 558. The changes say what the model does not: the room asks before it builds, moves for reasons other than too few hands, and builds again. But the form is small, its records are short, the rows behind the account fall below the table's floor, and every member's own adapted account is unresolved. A verdict of composes with residue on the original model is not a current local or shared failure.

## 6. How the model runs here

Counts are of defining members with a current-ledger line, particular lines included (`_analysis/d5f_model.py`); they count any line of an op.

**The elements that do the work.** The elements of section 2. Of the elements instantiated in half the defining members or more, two are instantiated here ten points or more above the population: P10, the move after a loss, in 18 of 34 (52.9 per cent), against 40.7; and K02, judging that the room has too few hands or too little room, in 32 (94.1 per cent), against 82.4. P27, choosing the spot before any loss, is instantiated in 27 (79.4 per cent), against 71.5.

**The elements that sit idle.** P34 is absent in 34 of 34 defining members, K07 and P30 in 33, A21, P28 and P33 in 32, A19, C02 and P29 in 30, and P21 in 29. They are idle in the population too, and their idleness does not mark the form.

**The elements that fit less here.** Nineteen elements are instantiated here ten points or more below the population. The largest gaps: P18, the contest with a rival carried in talk, in 10 of 34 (29.4 per cent), against 60.8; P17, coalitions, in 7 (20.6 per cent), against 51.6; P05, keeping, in 22 (64.7 per cent), against 93.4; P23, the chat, in 14 (41.2 per cent), against 69.0. These rooms' records are short, and they hold the search for a spot more than keeping a mark, contests or chats.

**What these rooms do that the model has no place for.** 11 of 34 defining members carry 26 propose lines, against 210 of the 558 defining rooms (32 per cent against 38). The propose lines are not part of the form's lean. The return from the move to building (section 3) has no arrow in the model.

**Where the room models and my reading disagree.** They agree. r/dallasstars's model says, on its last move, that "The later move still requires a broader local condition than too few helpers: the organizer named bodily fatigue alongside competing bot art", and that "The adapted ordering allows this entry negotiation before a stable mark, rather than treating all neighbour talk as a consequence of upkeep". r/sips's model says, "The local account therefore needs neighbour permission as a possible prerequisite to building, not only an effect of maintaining an existing mark". My reading of the members' lines is the same.

**The held proposals (QD4-001; never served to any room, not re-checked).** The model above is the frozen version. J ruled that both held proposals are stated in full wherever the model is reported. They are, as the tree file states them:

- **P05, move 198 (contrasting), history lines 173 to 176, reverted by line 181 (move 203).** The statement would gain: "This holds where the keepers can learn of a planned change only by being told, and no informed member holds it." The status would be bounded. The bound would read: "It does not hold where the keepers read a planned change from its shape and stop repairing it with no telling: completeanarchy, polska, satania, halo, bangtan, thesilphroad (R-completeanarchy-c187508d7ae3-022, R-polska-dadda7358f9a-049, R-satania-84df196116f3-022, R-halo-b988854ba168-036, R-bangtan-7efe23da0d0c-070, R-thesilphroad-a3f86618e239-018), a candidate branch, 'the shape read' (F-024). It does not hold where informed members hold the change against keepers who do not know: armok, maryland, oneshot (R-armok-8852b2ab85f8-022, R-maryland-d1b6e2d1d5f3-017, R-oneshot-e840e127e9b2-013), a limit below the trigger, at three nodes. Amended at D4a-01, after the D3 freeze (46384686...); not re-checked: no room was served these words." Rooms: completeanarchy, polska, satania, halo, bangtan, thesilphroad, armok, maryland, oneshot. Lines: R-completeanarchy-c187508d7ae3-022, R-polska-dadda7358f9a-049, R-satania-84df196116f3-022, R-halo-b988854ba168-036, R-bangtan-7efe23da0d0c-070, R-thesilphroad-a3f86618e239-018, R-armok-8852b2ab85f8-022, R-maryland-d1b6e2d1d5f3-017, R-oneshot-e840e127e9b2-013.
- **A11, move 199 (dropping working hypotheses), history lines 177 to 180, reverted by line 182 (move 203).** The arrow from P02 to P04 would be withdrawn (status withdrawn, in_model false). Its reason, as written: "Rule 16 and rule 14: preserve what remains supported, and replace or withdraw what does not. No defensible formulation of A11 as an arrow survives the return. (1) The order between rooms never beat its null (111 of 185 rooms, 0.600; null p95 0.670; base_rate_beaten false), and C2 withdrew it, keeping a transition inside threads. (2) Inside threads, the return's census (D3a-38, re-run as _analysis/d4a01_a11_classes.json) shows the transition in 111 rooms and template first in 98 of the 228 rooms whose lines show both ends; across threads 19 more. The reverse order is nearly as common, so the arrow carries no direction. (3) The failure clause is present and stands alone in 117 rooms: talk only in 31 (berkeley, bih, bitcoin, edboxes, eve, FinalFantasy, guatemala, habs, HomestarRunner, indieheads, ireland, latvia, leagueoflegends, mexico, morrowind, msu, parrots, placeDE, placesnek, polska, portugal, quebec, samuraijack, slovenia, spain, suomi, titanfall, torontoraptors, unitedkingdom, wine, zootopia) and layout only in 86. (4) The mechanism's word 'settled' is contradicted by 261 accepted restrict lines whose 'how' says a template does not settle the design for good (rival templates, polls, later redesigns, placers who deviate). A reworded arrow (a layout answers design talk in its thread) would be a new claim, never served to any room, with its reverse nearly as common: a co-occurrence, not an arrow. What remains supported, that design talk and layouts meet in threads, is held by P02's and P04's statements and ranges ('a design argued over days and redone'; 'an official template the room asks everyone to follow against other versions'), which stand. The arrow's record keeps its evidence and reasoning." Rooms (the talk-only rooms of the failure clause): berkeley, bih, bitcoin, edboxes, eve, FinalFantasy, guatemala, habs, HomestarRunner, indieheads, ireland, latvia, leagueoflegends, mexico, morrowind, msu, parrots, placeDE, placesnek, polska, portugal, quebec, samuraijack, slovenia, spain, suomi, titanfall, torontoraptors, unitedkingdom, wine, zootopia. Lines (the first-return lines of the census classes talk only, layout only and template first, 216): 2007scape-012, 4chan-011, AMD-012, AmericanFlaginPlace-009, AvoArmy-011, AyyMD-041, CKCrusaders-041, CSUFoCo-015, DestinyTheGame-014, DevonUK-010, FinalFantasy-014, GuardiansOfDatBoi-009, HomestarRunner-015, MonkeyIsland-011, NewMexico-015, ScottPilgrim-015, Temple-041, TsundereSharks-048, adventuretime-041, aggies-050, albania-046, alberta-016, anaheimducks-015, animalcrossing-053, anime-012, argentina-051, armenia-030, bardmains-055, berkeley-038, berserk-012, bih-036, bisexual-012, bitcoin-012, blackmirror-046, borderlands-020, bostonbruins-052, brasil-011, canada-012, catalonia-009, catholicism-011, cfb-048, chibears-010, chicubs-010, cirkeltrek-013, clashroyale-045, completeanarchy-011, criticalrole-043, crusaderkings-039, cubers-014, cuboulder-008, czech-014, dankmemes-045, darksouls-042, detroitlions-049, edboxes-046, edmontonoilers-041, empiredidnothingwrong-013, england-045, ethereum-056, europe-050, eve-049, fivenightsatfreddys-012, flashtv-055, floridagators-035, flyers-035, formula1-048, forsen-010, ftlgame-044, fxKorea-010, gameattack-015, gamindustri-053, gatech-041, ghibli-010, globaloffensive-012, greenbaypackers-011, guatemala-010, habs-011, heyyea-010, hongkong-047, hsv-012, hyperlightdrifter-046, indieheads-056, indonesia-035, ireland-045, italy-035, katawashoujo-041, lakers-009, latvia-029, leagueoflegends-042, lifeisstrange-013, linux-015, littlewitchacademia-012, loliconsunite-010, lost-044, lovelive-041, lsu-049, luxembourg-012, madokamagica-041, magictcg-010, mechanicalkeyboards-042, metalgearsolid-013, mexico-041, miamidolphins-041, minecraft-017, mit-041, mizzou-018, mls-053, monalisaclan-013, morrowind-011, msu-011, muse-048, mylittlepony-011, nVade-013, naruto-010, nbaspurs-056, necrodancer-011, neopets-047, newzealand-046, nightinthewoods-012, nin-012, ockytop-042, opticgaming-012, overwatch-017, parahumans-013, parrots-013, pathofexile-012, pcmasterrace-013, pebble-007, penguins-055, philippines-052, pitt-041, placeDE-041, placecanada-013, placesnek-031, planetside-056, polska-054, portal-012, portugal-082, predators-010, purdue-051, puzzleanddragons-013, quebec-013, radiohead-010, rainbowgrid-006, rangers-045, re_zero-042, redpandas-018, rickandmorty-042, rit-011, rocketbeans-008, rocketleague-011, romania-015, roosterteeth-013, rpi-049, russia-052, rust-010, rutgers-012, samuraijack-047, scp-014, seahawks-014, serbia-051, singapore-016, slovenia-041, smite-010, southpark-012, spacexmasterrace-052, spain-035, ss13-016, ssbpm-012, stardewvalley-058, starryknights-041, stevenuniverse-012, straya-047, suomi-041, survivor-035, sweden-045, tampabaylightning-045, terraria-048, teslamotors-012, tf2-041, thebluecorner-016, theexpanse-012, theitalyplace-054, thepointing-043, thesimpsons-011, tinytardis-009, titanfall-013, torontoraptors-016, totallynotrobots-013, transformers-046, trees-013, turkey-055, twentyonepilots-012, ubc-046, ucf-050, uiuc-011, ultrahardcore-005, undertale-011, unitedkingdom-035, unturned-013, uofm-008, uofmn-035, uruguay-012, utahjazz-009, utaustin-013, uva-042, uwaterloo-011, vegan-043, virginiatech-043, weezer-053, wine-011, witcher-017, worldoftanks-015, xenoblade_chronicles-012, zelda-061, zootopia-012.

No room of form F is among the rooms of the P05 proposal. 1 is among the talk-only rooms of the A11 proposal's failure clause: r/berkeley.

Neither held proposal bears on this form's lean, which is the spot.

## 7. The restrict lines: the arrow fails here, or the record cannot show it

**The rule, logged at D5a-36 before reading, unchanged.** I read every restrict line on an arrow held by a defining member, 114 lines, and sorted each `how` sentence (`_analysis/d5f_restricts.py`; my sort in `d5a41_sort_1.json` and `d5a41_sort_2.json`, joined in `d5a41_restrict_sorted.json`). *The arrow fails here*: the line says the consequent came without the antecedent, from another source or in another order, or that the antecedent did not lead to it. *The record cannot show it*: the line says the order, the link or the step is not visible, not dated or not established in the record. *Both*, where it says both. *Neither*, where it states a condition or a scope, or says that the two acts coincide or overlap. This is one reader's sort, mine; no second coder read it (J: no readers for the rest of the run).

| arrow | from, to | lines | the arrow fails here | the record cannot show it | both | neither |
|---|---|---|---|---|---|---|
| A01 | P01, P03 | 3 | 1 | 2 | 0 | 0 |
| A02 | R01, P01 | 3 | 0 | 0 | 0 | 3 |
| A03 | P03, P05 | 3 | 1 | 2 | 0 | 0 |
| A04 | P05, P08 | 13 | 13 | 0 | 0 | 0 |
| A05 | P08, P07 | 7 | 5 | 2 | 0 | 0 |
| A06 | P05, P14 | 9 | 6 | 1 | 1 | 1 |
| A07 | P03, P11 | 7 | 4 | 3 | 0 | 0 |
| A08 | P11, P12 | 6 | 5 | 1 | 0 | 0 |
| A09 | P12, P13 | 2 | 1 | 0 | 1 | 0 |
| A10 | K02, P10 | 16 | 10 | 3 | 1 | 2 |
| A11 | P02, P04 | 12 | 10 | 1 | 0 | 1 |
| A12 | P01, P15 | 10 | 5 | 5 | 0 | 0 |
| A13 | P05, P16 | 10 | 6 | 2 | 2 | 0 |
| A14 | P08, P16 | 2 | 0 | 2 | 0 | 0 |
| A15 | P01, P09 | 2 | 1 | 1 | 0 | 0 |
| A16 | P09, P07 | 2 | 2 | 0 | 0 | 0 |
| A17 | P09, P08 | 1 | 0 | 0 | 1 | 0 |
| A18 | P09, P18 | 1 | 1 | 0 | 0 | 0 |
| A19 | P05, P17 | 2 | 1 | 1 | 0 | 0 |
| A20 | P01, P20 | 2 | 0 | 1 | 0 | 1 |
| A21 | P08, P21 | 1 | 0 | 1 | 0 | 0 |
| all | | 114 | 72 | 28 | 6 | 8 |

**The arrow fails here, more often than in any other form.** Across the 114 lines the arrow fails here in 72 (63 per cent), against 47 per cent in form A, 46 in B, 57 in C, 54 in D and 43 in E. The record cannot show it in 28 (25 per cent). These rooms' short records still date their acts: the request for space, the loss, the move and the new start appear in order, and the order is often not the model's.

**The form's own arrows: A10 and A04.** A10 is read in section 8. A04 runs from keeping to border talk, and here it fails in all 13 of its lines: border talk came before there was a mark to keep (section 3).

**The arrows every form restricts.** A11 (the design, then the template) fails here in 10 of 12 lines; A13 (keeping under strain, then help) in 6 of 10; A06 (upkeep, then scripts) in 6 of 9; A05 (a settled border, then restraint) in 5 of 7; A08 (marking, then the record) in 5 of 6.

**Where the record cannot show it.** A12, the one-line pledge as every reader's answer, divides evenly: it fails in 5 of 10 lines (acceptances that ask for instructions) and the record cannot show it in 5. Help traded across a border (A14) cannot be shown in 2 of 2.

**So the two readings divide by kind, as in forms A to E.** Where the line concerns the order of two acts the rooms report (talk and keeping, a loss and a move, a design and its template), it mostly says the arrow fails as stated. Where it concerns cause or delivery (a pledge that obliges every reader, help delivered), it mostly says the record cannot show it. Across all 114 lines: the arrow fails here in 72, the record cannot show it in 28, both in 6, neither in 8.

## 8. The one relationship that runs differently here

A10 runs from K02 (judging that the room has too few hands or too little room) to P10 (the move after a loss). Its connection: "in a room carrying both, the first doubt about the room's numbers or room comes before the first move after a loss". Its mechanism: "A room that judges it has too few hands to hold its spot stops fighting for it and moves."

The arrow's side. In r/uiowa a member reported a lost spot and named too few hands in one turn: "Yeah, the 72, 826 spot got overtaken by Michigan." [uiowa/c0004], and "The real problem is there isn't a big enough Hawkeye presence on Reddit, sadly." [uiowa/c0004]. The same member then chose a new spot: "Above Minnesota might work." [uiowa/c0007]; "Ok, I'm going for it. Help me out, guys!!" [uiowa/c0007]. The coders' line on r/uiowa says that the record holds the judgement and the proposal, not the completed move: "The weakness diagnosis accompanies a proposed replacement spot but does not demonstrate that the diagnosis produced a completed move."

The other side. In r/UPenn the move followed a taken spot, and no one spoke of hands: "Someone took the spot, moving to (212, 892)" [UPenn/c0002]. In r/dallasstars the room moved when a neighbour claimed the spot (section 1), and later because its builder was tired and bots crowded the place: "Yeah, the old location isn't gonna work out and I don't think I can do another handmade one again" [dallasstars/c0097]. "I moved our image northwest underneath the Hawks on the other side of the rainbow." [dallasstars/c0097]. In r/portal the room weighed fighting against moving, lost, and made a new plan (section 1). r/portal's line: "Loss prompts relocation here without an explicit diagnosis of too few hands, leaving that narrower manpower mechanism unsupported."

In 16 of 34 defining members a current-ledger line restricts A10, against 33.7 per cent of the 558. In 10 of the 16 the arrow fails: the move came from a loss, a taken spot, a neighbour's claim or a lack of space, or the shortage led the room to stay, shrink or give up. r/nbaspurs: "Shortage can supply a reason to oppose moving, so the arrow must allow contested relocation rather than treating too few hands as a uniform reason to leave." In 3 the record cannot show that a judgement produced a completed move. What runs differently here is the cause of the move. The model has the room's own judgement of its hands move it. In these rooms the spot moved them: a neighbour's claim, a loss or a lack of room.

This is description, not a test. A10's expectation in form F is 0.159 (2 within-case datings over 705 rooms, times 56), so A10 is not-testable-here (section 10). One of its two datings, r/day9, is a thin room of this form; the account names it as the room that best supports the account, and there it lost its border at hour 48 and moved within two hours.

## 9. Fourth-order themes over- and under-represented

The rule was logged at D5a-01 before it ran (`_analysis/d5_themes.py`), and it is applied here to the defining members' codes (`_analysis/d5f_facts.py`). A member's coded concepts are counted by the fourth-order themes of their second-order theme's placements, and the form's pooled share on a theme is set against the pooled share over all 705 rooms. Over-represented: a ratio of 1.5 or more, with the theme present in 5 members or more. Under-represented: a ratio of 0.67 or less, with a population share of 1 per cent or more. These are shares of what the coders coded in these rooms, never a property of the rooms (contract section 5).

**Over-represented (5).**

- **Territoriality:** 20.7 per cent of the defining members' coded concepts against 3.8 per cent (ratio 5.49), in 32 members.
- **Collective efficacy:** 1.3 per cent of the defining members' coded concepts against 0.4 per cent (ratio 3.65), in 9 members.
- **Sensemaking:** 4.1 per cent of the defining members' coded concepts against 1.9 per cent (ratio 2.13), in 17 members.
- **Mobilization:** 8.2 per cent of the defining members' coded concepts against 4.1 per cent (ratio 2.00), in 23 members.
- **Standardization of output:** 3.7 per cent of the defining members' coded concepts against 2.1 per cent (ratio 1.75), in 11 members.

In the rooms' words, from members holding the largest share on each theme (`_analysis/d5f_theme_quotes.py`): Territoriality, "Doesn't it make more sense to have SNSD near all the other kpop related things? We can help them make a new one somewhere else." [snsd/c0052]. Collective efficacy, "Out of all the spots to choose, we pick a spot right underneath Penn State...no wonder people get us confused...." [UPenn/c0013]. Sensemaking, "10 people is a pixel a minute tho, so it adds up fast if you spread it out." [gratefuldead/c0029]. Mobilization, "We should think about a design and help The Void clear some space for it." [diablo/c0029]. Standardization of output, "I didn't realize how big 80x80 would have been." [penguins/c0057].

**Under-represented (10):** Neo-tribes (ratio 0.04), Attribution (ratio 0.07), Visibility returns (ratio 0.33), Rivalry (ratio 0.37), Repertoire of contention (ratio 0.39), Repair work (ratio 0.45), Live and let live (ratio 0.47), Negotiated order (ratio 0.49), Frame bridging (ratio 0.57), Transition (ratio 0.59).

Territoriality is the form's change signature, so its excess in the codes restates the cut: a fifth of the defining members' coded concepts (20.7 per cent) fall under it. The coders coded less repair work, negotiated order and contention here than in the population. In these rooms' short records, the search for space takes the place of keeping and fighting.

## 10. Arrows present, absent or not-testable-here

Section 1's arithmetic, declared at D5a-01: an arrow's expectation in a form is its within-case datings (its `subs`, counted over the 705 analysed rooms) over 705, times the form's n, here 56. Below one the arrow is not-testable-here, and no absence, boundary condition or failed proposition may be written from it. In form F the expectations run from 0.000 to 0.318, the lowest of the six forms:

- A01 (P01 to P03): 2 datings, expected 0.159; not-testable-here
- A02 (R01 to P01): 2 datings, expected 0.159; not-testable-here
- A03 (P03 to P05): 2 datings, expected 0.159; not-testable-here
- A04 (P05 to P08): 2 datings, expected 0.159; not-testable-here
- A05 (P08 to P07): 3 datings, expected 0.238; not-testable-here
- A06 (P05 to P14): 3 datings, expected 0.238; not-testable-here
- A07 (P03 to P11): 2 datings, expected 0.159; not-testable-here
- A08 (P11 to P12): 2 datings, expected 0.159; not-testable-here
- A09 (P12 to P13): 2 datings, expected 0.159; not-testable-here
- A10 (K02 to P10): 2 datings, expected 0.159; not-testable-here
- A11 (P02 to P04): 2 datings, expected 0.159; not-testable-here
- A12 (P01 to P15): 3 datings, expected 0.238; not-testable-here
- A13 (P05 to P16): 4 datings, expected 0.318; not-testable-here
- A14 (P08 to P16): 4 datings, expected 0.318; not-testable-here
- A15 (P01 to P09): 4 datings, expected 0.318; not-testable-here
- A16 (P09 to P07): 4 datings, expected 0.318; not-testable-here
- A17 (P09 to P08): 4 datings, expected 0.318; not-testable-here
- A18 (P09 to P18): 4 datings, expected 0.318; not-testable-here
- A19 (P05 to P17): 4 datings, expected 0.318; not-testable-here
- A20 (P01 to P20): 3 datings, expected 0.238; not-testable-here
- A21 (P08 to P21): 0 datings, expected 0.000; not-testable-here

**Present: none. Absent: none. Not-testable-here: all 21.** Members' current-ledger lines on an arrow (sections 7 and 8) are description only. Members among an arrow's within-case datings: r/corridor (A19); r/day9 (A10); r/latin (A01); r/sips (A02). That is arithmetic about the model's own evidence, and it tests nothing in the form.

**Propositions.** N01, N02, N03, N04, N05, N06, N07, N08, N09; the highest expectation among the arrows they rest on is 0.318. Every proposition is not testable here; none holds and none fails against a real expectation. No `findings.jsonl` line is bounded from this form.

## 11. How representative members do the work

**The rule, logged at D5a-36 before it ran, unchanged** (`_analysis/d5f_facts.py`). Fit is a defining member's distance to the form's centre in the allocation's 892 columns. The best two are the nearest members whose selected changes and coded concepts are at or above the form's defining medians (11 changes, 64.5 concepts). The least well is the farthest defining member. The member read at length is, among the ten nearest, the one with the most selected changes not read at length earlier in stage D5. As at form E, the rule picks one room twice: r/sips is the second best fit and has the most changes among the ten nearest. So three rooms are told, and r/sips is told once, at length.

**Best fit: r/dallasstars** (distance 0.757; 11 selected changes; 109 coded concepts; first-return verdict composes, re-check grade composes with residue; in F01 and F24). Its members follow an ice hockey team, and they tried at least six spots. Their first start was in a rival's space: "Started it at (579, 802) D: Edit: The Blues do not like that we took that spot" [dallasstars/c0025]. A member proposed a host's area, "we should build this one in green lattice. maybe in the 940, 245 area" [dallasstars/c0026], and another doubted that a host's agreement would bind its placers: "Even if everyone in that sub agrees, I doubt everyone who's defending green lattice is in that sub." [dallasstars/c0034]. Asked to recolour a rival's logo, a member refused: "there's no need to attack other people's art. better to focus on adding our logo somewhere." [dallasstars/c0059]. The room yielded a spot to its owner (section 1), dropped it, "we're dropping it." [dallasstars/c0046], and looked again: "Okay so, there's looks to be room on the Finland flag, Chicago Bears have moved on the far right side." [dallasstars/c0047]. It left that spot too: "Excellent! Finland was far too hostile." [dallasstars/c0057]. At a new spot it made terms with a neighbour writing beside it. The neighbour asked, "Hey could you please not do this? or at least let us write over it?" [dallasstars/c0079], and a member proposed a fix, "If you could move your writing 3 or 4 pixels down I don't think we'd mind the bottom star being cut off? Would that work?" [dallasstars/c0081], then agreed: "Sure, we'll try that out." [dallasstars/c0082]. The logo was made and kept by hand: "We made and maintain our logo by hand." [dallasstars/c0095]. In the end the builder moved again, tired and crowded by bots (section 8).

**Second best fit, and read at length: r/sips** (distance 0.758; 21 selected changes; 109 coded concepts; first-return verdict composes with residue, re-check grade composes with residue; in F20, F21 and F24). The rule chose it: among the ten nearest it has the most selected changes, and it was not read at length earlier. Its members are viewers of a video game streamer. They looked for a spot (section 1), and one member found a host's space: "There's a space at the top of the green lattice, below the purple writing. They're usually pretty tolerant of art" [sips/c0031]. The room waited for that host's permission (section 1). Meanwhile a member started beside another work: "I have started just to the right of the Rolling Stones lips, tucked in a small space that wont be missed, just added the blue so far" [sips/c0038]. In another thread members squeezed a small sign in (section 1) and finished it: "we did it guys. well done." [sips/c0066]. A neighbour then asked the room not to build over its work: "Can you guys not do the spaceman over /r/kingdomhearts keyblade? we've been working on it for a while and are almost done aside from the portion youre trying to build over." [sips/c0068], and offered a strip: "Would you consider trading to the tiny 8 wide strip? We were trying to get a couple of other spots before we were pushed out, this is the original design." [sips/c0069]. The sign was lost, "Its gone rip" [sips/c0070], and one who erased it said why: "I destroyed it last night lol. Thought it was vandalism" [sips/c0078]. Near the close the room was still choosing a spot, around another room's sign: "Actually, that would go over /r/tf2's sign, so I suggest 300, 359" [sips/c0055]. A member saw almost no free space and proposed a host: "i've been looking all over and there's almost no blank spaces that aren't being built upon, we could maybe try to co-operate with another subreddit to built upon theirs which would also offer some protection from vandalism hopefully." [sips/c0058]. A script was offered for the last spot, "I was going to write a quick script after I finish work that we could use" [sips/c0049], and helpers came from the streamer's audience: "I've been enlisted from the stream donation!" [sips/c0050]. What is unrepresentative about it: its sign was erased by a keeper who took it for vandalism, which is P05's telling clause seen from the eraser's side, and its record runs to the close with the spot still unsettled.

**Least well: r/ducks** (distance 1.314; 5 selected changes; 14 coded concepts; first-return verdict composes with residue; in no branch; its point lies only 0.011 nearer form F's centre than form B's). Its record is a few calls and answers. A member called for a letter, "Lets make a sick O to support our boys" [ducks/c0001], and another reported a start: "Got a green line started" [ducks/c0002]. A member proposed a spot: "We could cut it out of a pre-green area" [ducks/c0005]. Late, others proposed taking another room's letter, "I say we hijack the OSU 'O' (bottom left corner, below Michigan) CHARGE!" [ducks/c0006], or adding to a neighbour's logo: "I have already begun adding green below the Trail Blazers logo (802,551). Lets turn it into a full fledged Ducks logo! Go Ducks!" [ducks/c0012]. A member answered an invitation from another room, "Not very many people on our sub. But we'll see what we can do!" [ducks/c0010], and the last asked, "It's officially over already isn't it?" [ducks/c0013]. Its lines are about where to put a letter, and they are few. It is in form F because Ward's method put it there.

## 12. The branches its rooms come from

J asked that stage D6 build on the forms with the 35 branches as the level below. The branches do not nest in the forms: a branch was cut on one shared key, a form gathers rooms by the whole mix of their changes and codes. The table gives, for every branch, how many of its rooms are in form F, and the branch's share in F against F's share of the 705 rooms (56 of 705, 0.079). A ratio of 1 is what a branch would show if its rooms fell in the forms at random.

| branch | parent | name | rooms | in form F (defining, thin, core) | share of the branch in the form | against the form's share of 705 |
|---|---|---|---|---|---|---|
| F09 |  | the move returns to building: relocation followed by renewed construction | 54 | 10 (8, 2, 0) | 0.185 | 2.33 |
| F05 | F01 | the styling ended: ordinary use restored | 12 | 2 (1, 1, 0) | 0.167 | 2.10 |
| F04 | F01 | the licence policed: objections to the play, its limits and its end | 13 | 2 (2, 0, 0) | 0.154 | 1.94 |
| F08 |  | machine hands kept on one target: installing, teaching and updating every runner | 50 | 6 (6, 0, 0) | 0.120 | 1.51 |
| F03 | F01 | the joke tested: members check a claim's truth | 18 | 2 (2, 0, 0) | 0.111 | 1.40 |
| F24 |  | machine hands debated, not shown placing | 27 | 3 (3, 0, 0) | 0.111 | 1.40 |
| F25 |  | carrying on in talk: proposals and single attempts, not shown taken up | 27 | 3 (3, 0, 0) | 0.111 | 1.40 |
| F35 |  | the call made workable: answers ask for a task, and callers supply it | 18 | 2 (1, 1, 0) | 0.111 | 1.40 |
| F20 |  | the close as news: late arrivals told that placement has ended | 10 | 1 (1, 0, 0) | 0.100 | 1.26 |
| F01 |  | the play administered: steps that test, police, end and convert the April Fools frame | 103 | 10 (9, 1, 0) | 0.097 | 1.22 |
| F21 |  | the canvas call not a joke: the April Fools frame kept apart from the canvas work | 32 | 3 (3, 0, 0) | 0.094 | 1.18 |
| F12 | F11 | the spine restarted on another canvas | 22 | 2 (2, 0, 0) | 0.091 | 1.14 |
| F11 |  | carrying on as renewed work, begun before the close | 43 | 3 (2, 1, 0) | 0.070 | 0.88 |
| F32 |  | the marking returns to keeping: celebration followed by renewed defence | 21 | 1 (1, 0, 0) | 0.048 | 0.60 |
| F31 |  | hosting as one-off permission: requests and leave, no standing host rule | 22 | 1 (1, 0, 0) | 0.045 | 0.57 |
| F34 |  | the design sized to the hands: scale and detail conditioned on crew, upkeep, space and colours | 22 | 1 (1, 0, 0) | 0.045 | 0.57 |
| F33 |  | the plan kept current while the design settles | 23 | 1 (1, 0, 0) | 0.043 | 0.55 |
| F30 |  | the chat seen only through its invitations and returned reports, not its choices | 24 | 1 (1, 0, 0) | 0.042 | 0.52 |
| F29 |  | the chat's reach conditional: access, and the return of decisions to the thread | 25 | 1 (1, 0, 0) | 0.040 | 0.50 |
| F22 |  | help conditional on the helper's own work and spare hands | 30 | 1 (1, 0, 0) | 0.033 | 0.42 |
| F23 |  | the close scoped to the original canvas: continuation renewed, uncertain and contested | 30 | 1 (1, 0, 0) | 0.033 | 0.42 |
| F10 |  | a deal carried out as work: prepared in the room, then implemented and relayed | 38 | 1 (1, 0, 0) | 0.026 | 0.33 |
| F07 |  | the telling clause not shown at the design: informed members reject the planned change | 59 | 1 (1, 0, 0) | 0.017 | 0.21 |
| F02 | F01 | the takeover run as a temporary regime | 33 | 0 (0, 0, 0) | 0.000 | 0.00 |
| F06 | F01 | the joke kept: a request that its change last | 8 | 0 (0, 0, 0) | 0.000 | 0.00 |
| F13 | F11 | the work remade in other media, often before the close | 9 | 0 (0, 0, 0) | 0.000 | 0.00 |
| F14 | F11 | the mark adopted as the room's emblem while it is still placed, damage included | 7 | 0 (0, 0, 0) | 0.000 | 0.00 |
| F15 |  | the plan kept current: correcting, updating and re-circulating the template | 42 | 0 (0, 0, 0) | 0.000 | 0.00 |
| F16 |  | the chat kept open: invitations renewed, entrants screened, outcomes relayed to the thread | 35 | 0 (0, 0, 0) | 0.000 | 0.00 |
| F17 |  | the marking provisional and contested: success judged and credit disputed while the work goes on | 36 | 0 (0, 0, 0) | 0.000 | 0.00 |
| F18 | F17 | success judged while upkeep continues | 15 | 0 (0, 0, 0) | 0.000 | 0.00 |
| F19 | F17 | credit contested during the work | 14 | 0 (0, 0, 0) | 0.000 | 0.00 |
| F26 |  | the telling clause not shown at the border: informed members contest the terms | 23 | 0 (0, 0, 0) | 0.000 | 0.00 |
| F27 |  | the telling clause not shown in keeping: interference seen, its cause and loss not | 27 | 0 (0, 0, 0) | 0.000 | 0.00 |
| F28 |  | help at the border conditional: on the home work, the terms and harm to a third room | 22 | 0 (0, 0, 0) | 0.000 | 0.00 |

**What the table shows.** Four branches lean to form F at 1.5 times its share or more:
- F09, the move returns to building: relocation followed by renewed construction: 10 of 54.
- F05, the styling ended: ordinary use restored: 2 of 12.
- F04, the licence policed: objections to the play, its limits and its end: 2 of 13.
- F08, machine hands kept on one target: installing, teaching and updating every runner: 6 of 50.

F09 is one of the two narrow forms of the branch accounts: rooms that rebuild after moving. Its lean here (2.33 times F's share) is what the form's name says. But 44 of F09's 54 rooms are in other forms, so the branch and the form are not the same set. The two April Fools branches lean on 2 rooms each. Twelve branches have no room in form F, among them F02 (the takeover), F17 and its subforms (the marking provisional), the telling clause not shown in keeping or at the border (F27, F26), and help at the border conditional (F28). 28 of form F's 56 rooms are in no branch, half the form: 18 of them are thin or core rooms, and 10 are defining.

**Rooms in no branch.** 28 rooms (10 defining): r/achievement_hunter (thin), r/cmu, r/COSI (thin), r/diablo, r/ducks, r/FlipnoteStudio3D (thin), r/foxstevenson (thin), r/gameboy (thin), r/gratefuldead, r/GreenEmpire (core), r/haskell (thin), r/hoodr (thin), r/latin, r/lexington (thin), r/nonbinary (core), r/Northwestern, r/nyu, r/PokemonSage (core), r/Produce101 (thin), r/qotsa, r/Redox (core), r/snsd, r/TheID (core), r/transgender (thin), r/TreePlace (thin), r/ufl (thin), r/uiowa, r/UNLincoln (core).

## 13. The nearest form and what separates them

**The nearest form is D**, keeping, with traded help and carrying on. The distances between form F's centre and the others are D 0.541, B 0.547, C 0.563, A 0.567, E 0.816. Four forms lie within 0.57 of F's centre; only E lies far. In the tree F joins D at four forms, and the two join A, B and C at two. F and D are separated by what the rooms changed: F's members change territoriality, the spot, D's keeping, help and carrying on.

**The rooms between forms.** B 1, E 1: these are the forms whose centres lie nearer than F's to its defining members, 2 rooms in all, the fewest share of the six forms. The room that could have gone either way, the defining member with the smallest margin to another centre, is r/phish (11 selected changes, 97 coded concepts, in F01, F08, F10 and F23). Its point lies nearer form B's centre, the work behind the thread, by 0.038. Its record has both. Members asked how to coordinate, "Any ideas on how we can all coordinate? I guess we should just pick a spot and start writing it?" [phish/c0002], and used a script and an overlay to place: "Using the Tamper monkey plugin and the r/place script, I set an overlay at an area that doesn't seem to busy, and doesn't overwrite too much other stuff." [phish/c0021]. The scripts are form B's; the spot chosen where it overwrites little, and the terms at the border (section 1), are form F's.

## 14. The split below the form

**The split rule, logged at D5a-36 before it ran, unchanged** (`_analysis/d5f_split.py`, on `room-forms-tree-rooms.tsv`). A split reads as a split when both parts hold 10 defining rooms or more and each part has a fourth-order change column (a node or a link) at 1.5 times the parent's defining share or more, held by a third of the part or more and by fewer in the other part. The walk descends only while splits read.

| group | splits at k | part | defining rooms | all rooms | change columns the part leans to | reads as a split |
|---|---|---|---|---|---|---|
| F | 20 | F.1 | 25 | 41 | none | no |
| F | 20 | F.2 | 9 | 15 | Keying (2.99 times the parent's share; 0.889 of the part, 0.160 of the other); Collective efficacy > Territoriality (1.84 times the parent's share; 0.889 of the part, 0.360 of the other); Territoriality > Direct information sharing (1.98 times the parent's share; 0.444 of the part, 0.160 of the other) | no |

**Form F's first split, at twenty forms, does not read as a split.** F.2 holds 9 defining rooms, under the rule's 10. It leans to keying, the April Fools frame (88.9 per cent of its defining rooms against 16.0 of F.1), and 7 of its 15 rooms are in F01; its nearest rooms are r/nbaspurs, r/ethoslab and r/stargate. F.1 (25 defining rooms, 41 in all) has no column of its own. The share of defining rooms holding each signature column in each part: F.1: Territoriality 0.920, Mobilization 0.440, Repair work > Negotiated order 0.480; F.2: Territoriality 1.000, Mobilization 0.444, Repair work > Negotiated order 0.222. The walk stops at the form, and I write no subform candidate.

**Whether calls and terms stand apart.** The mixture rule of D5a-37, logged at this leg's opening, applies to the signatures held by under half the members: Mobilization (calls) and the link Repair work > Negotiated order (keeping joined to terms). Territoriality, at 94.1 per cent, is the form's base and not part of the mixture (`_analysis/d5f_mixture.py`, `d5a41_mixture.json`).

- **They are held by the same rooms, more than chance.** Mobilization is held by 15 defining members, the link by 14. They meet in 8, against 6.2 if the two were independent. Territoriality meets Mobilization in 15 (against 14.1) and the link in 14 (against 13.2): every holder of either holds territoriality. All three meet in 8, against 5.8. 2 members hold none of the three, and 11 hold territoriality alone.
- **The tree does not part them.** At the first split Mobilization falls 11 of 15 in F.1 and the link 12 of 14.
- **The rule's outcome.** They stand apart if their holders overlap no more than independence gives and the first split sorts them into different parts; they are mixed if the holders overlap more than independence or neither condition holds. The overlap is above independence. So the rule gives its first definite outcome of the six forms: **mixed.** In these rooms the call and the terms at the border go together, and both sit on the spot. The counts are small (8 against 6.2), and I read them as a lean.

So form F is one pattern, the spot, with calls and terms held together on it by about a quarter of its defining members. The tree finds no part, and I write no subform candidate.

## 15. The thin and core rooms placed here

**Thin rooms (16),** placed by the whole mix of their changes and codes at the nearest form centre: r/achievement_hunter (3 changes, 36 concepts), r/berkeley (4 changes, 98 concepts), r/COSI (1 change, 7 concepts), r/day9 (3 changes, 38 concepts), r/FlipnoteStudio3D (1 change, 2 concepts), r/foxstevenson (3 changes, 29 concepts), r/gameboy (3 changes, 14 concepts), r/haskell (3 changes, 88 concepts), r/hoodr (3 changes, 50 concepts), r/lexington (2 changes, 15 concepts), r/miraculousladybug (4 changes, 28 concepts), r/Produce101 (2 changes, 6 concepts), r/tenma (1 change, 2 concepts), r/transgender (3 changes, 12 concepts), r/TreePlace (4 changes, 35 concepts), r/ufl (4 changes, 33 concepts).

Their selected lines weigh less and enter no share above. The most frequent are P01 add-step 3 (r/lexington, r/miraculousladybug, r/tenma); C01 restrict 2 (r/TreePlace, r/ufl); A10 restrict 2 (r/day9, r/TreePlace); P27 link 2 (r/achievement_hunter, r/foxstevenson); P03 link 2 (r/berkeley, r/day9); P17 add-step 2 (r/foxstevenson); P07 link 1 (r/COSI); P24 link 1 (r/FlipnoteStudio3D). Among them are the spot and the move (P27 link, A10 restrict, P03 link), as in the defining members. r/day9 is among them (section 8).

**Core rooms (6),** with no selected change, placed by their codes alone at the nearest centre in the code columns: r/GreenEmpire (7 concepts; verdict composes), r/nonbinary (1 concept; verdict cannot-tell), r/PokemonSage (2 concepts; verdict cannot-tell), r/Redox (4 concepts; verdict composes-with-residue), r/TheID (2 concepts; verdict composes), r/UNLincoln (2 concepts; verdict composes). Their placement rests on 1 to 7 coded concepts and is weak. Form F holds more placed rooms, 22 of 56, than any other form's share.

## 16. The form test

**The constructs.** P27 (choosing the spot), P10 (the move after a loss), P19 (a room's work under a host's rule) and P08 (border terms), at the fourth-order theme T4-014 (Territoriality), with K02, the arrows A10 and A04, and the return from the move to building (P03 link).

**The relations.** The room looks for a spot before it builds, and it asks the neighbour or host for space, so border talk comes before keeping. When a spot is claimed, taken or lost, the room yields or moves, and the cause it names is the spot more than its own hands. At the new spot it calls again and builds again, and the cycle may repeat. Where it builds beside others it makes terms at the border, and the rooms that call are more often the rooms that make terms than chance gives (8 against 6.2).

**Is it falsifiable?** Yes. A room that moved only when it judged its hands too few, or that built first and talked with its neighbours only to keep what it had, would fall outside the relations. A10's within-case dating, r/day9, fits the relations: the account says it offered a neighbour terms before any damage, the agreement broke at hour 48, and the room judged the spot lost and moved. I have not looked for such rooms outside the form.

**The four organizing problems.** The form binds information provision: a room must learn where it can build, from the canvas and from its neighbours, before it can call anyone. It touches task division between rooms: the canvas is divided by request, claim and terms. Reward and the allocation of members to tasks are left free. A remainder is supported: the search for space, and the return from the move to building.

**What varies among members.** How many spots a room tried, and whether it asked a host or found free space. The tree finds no split that reads, and its one small part leans to the April Fools frame. The variation is accommodated by the form.

**Result: a form in a narrow sense, on few rooms.** One theme binds nearly every defining member (32 of 34), and the members' words show its relations: asking before building, yielding and moving for the spot's reasons, and building again. A smaller share of its defining rooms lies nearer another centre than in any other form (2 of 34). Two limits stay. The form is small and its records are short, so the rows behind the account fall below the table's floor. And the claim rests on my reading of the lines and the members' words, with every local account unresolved.

## 17. What would make you doubt this is a form at all

Three things.

First, the size and the short records. 34 defining rooms with a median of 64.5 coded concepts. Form F may be the rooms whose records were short and mostly about where to build, not rooms that organized differently. Its 19 elements instantiated ten points or more below the population say the same: much of what other rooms recorded is not in these records.

Second, my sort of the restrict lines. One reader sorted 114 lines, fewer than in any other form. The share where the arrow fails, 63 per cent, rests on that sort.

Third, the survival figures, from the record, never from the canvas. The median organizing end is hour 70.86 for the 53 members with one, and the mean aftermath share is 0.0056, the lowest of the six forms. The coded `work_remained` field says kept in 20 members, lost in 13 and silent in 23. These figures are not compared here, and nothing in this account rests on them.

What would undo the form: rooms outside it with as much talk about the spot whose moves followed their own judgement of too few hands; or a cut on longer records in which these rooms fall into the forms of keeping and design.
