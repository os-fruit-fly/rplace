# The retelling: the model with its forms inside it

Part 1 goes dimension by dimension, one leg each (D6a-01 to D6a-08); part 2, the telling, follows, written at D6b with the figure (`figure-D6.md`). The two parts, with the sensitivity section added at D6a-09 and the size-held test added at D6a-10, run to about 15,000 words. The forms are the six room forms of D4a-08c, by their final names (`room-forms-names.md`); the 35 branches are the level below and appear where they explain a form (the PI's message for D6, on J's word). The model is the version frozen at D3 (46384686d6173fdeb4c749667478c1363e675bc6b52bb6f4fdc211d387e68525), with two held proposals (QD4-001) stated in full in each form account.

The six forms:
- **A, Border terms and the announced plan** (166 rooms, 135 defining).
- **B, Behind the thread: chat, scripts, raids** (141, 113; a residual grouping, not a form, with three facets held by different rooms: the chat, the scripts and the raids).
- **C, The design reopened** (125, 96).
- **D, Keeping, with help or carrying on** (119, 96), with its splits D.1, Keeping with the call; D.2, Keeping inside the sub's play; and below D.2, D.2.1, The play, carried on, and D.2.2, The play, kept.
- **E, The sub's play, run as work** (98, 84).
- **F, Moving for the spot** (56, 34).

The form lines, one per element and room form, are in `fractal-forms-D6.jsonl`; the branch lines, at least one per branch where it explains a form, are in `fractal-D6.jsonl` (QD6-001; `departures.jsonl` line 20). How each form line is decided (rule logged at D6a-01 before it ran, `_analysis/d6_fractal.py`): on a form's defining rooms, an op on an element or arrow leans where it is held by max(5, a tenth of the defining rooms) or more, at 1.2 times the 558 defining rooms' share or more. A form **replaces** the element where contradict lines lean, **restricts** it where restrict lines lean and outnumber the other leaning ops, **specifies** it where add-step, add-condition or link lines lean, and leaves it **untouched** otherwise. No form replaces any element. The coding vocabulary made that relation nearly unreachable: the readers returned 11 contradict lines among 42,243 at the first return and 4 among 53,493 at the re-check, and none stands among the forms' selected lines. Restrict lines often say what a contradict line would have said. Of each form's restrict lines on arrows, 43 to 63 per cent say that the arrow fails in the room (Part 2 gives the counts by form). Each relation is a claim about the form's changes, a pattern across rooms counted by the ledger; what the rooms did is a claim on their words. No canvas field is used. How far each changed cell depends on the rule's two thresholds is in the sensitivity section after Part 2, and how far it depends on record size is in the size-held test after that; each cell's marks are in `form-cells-sensitivity-D6.tsv` and `form-cells-size-D6.tsv`.

**Local validation is not established.** prior.md section 3's measure was not computed, and every member's adapted local account is unresolved. That measure would show each second-order theme with a coordinating turn reached by an element or a validated adaptation; it moves to E1. So wherever this telling names a room that shows a pattern best or least well, the room shows it in its ruled lines in the ledger, not in a validated account of the room.

## Part 1. Dimension by dimension

### D01, Critical mass

**In the global model.** Critical mass is whether a scattered readership gathers enough hands, who know how to place, to make a work viable on the clock, and how a room reads its own numbers. Three fourth-order themes sit under it. Mobilization is the call and its answer: the room calls its members and kindred subs to place (P01), a member answers in one line that asks for nothing back (P15), the call follows a member's start (A02), and a bare join answers the call (A12). Sensemaking is members asking what the canvas is and others explaining it (P24). Collective efficacy is the room judging that it has too few hands or too little room (K02), and members stepping away under strain or repairing a quarrel (P32, a candidate). The model has the call at the start of the work, after a member proposes or begins the mark.

**Mobilization.** Three forms specify the call (P01), and each makes it return later in the work.
- In C, The design reopened, the call returns within the work. A finished figure, a granted space or a member's report of a part done becomes the premise for the next call. The rooms that show it best are r/starbound, r/bisexual and r/suomi; r/Honduras shows it least well. Not every C link is a return: in r/trees an explanation of the canvas leads a member to say they will place, and in r/anaheimducks the organiser explains why the timer favours working together. That is local variation inside the specification.
- In D, Keeping, with help or carrying on, the call returns from carrying on and from loss: a later canvas, damage to the mark or a lost spot leads the room back to calling for hands. r/bindingofisaac, r/rotmg and r/edmontonoilers show it best; r/rojava least well. Two branches explain part of it: F11 (carrying on as renewed work, begun before the close) and F12 (the spine restarted on another canvas) lean to D at 2.62 and 2.69 times its share, and three of their rooms in D link the call (r/bindingofisaac, r/furry_irl, r/sadboys), two of them to a later canvas or a remake.
- In F, Moving for the spot, the call returns after a lost, taken or bulldozed spot: a failed attempt or a smaller restart reopens the call at a new spot. r/twentyonepilots, r/snsd and r/penguins show it best; r/dbz least well. F09 (the move returns to building) leans to F at 2.33 times its share, but of its rooms in F only r/penguins links the call, and not to a move, so the branch does not explain this return; F09's line is read at the building element (D02).
- A, B and E leave P01 untouched.

The start before the call (A02) is restricted in D and E, where the start and the first call share one post in the restricting rooms; the lines say that the two coincide, and in two E rooms (r/nintendo, r/titanfall) a call came before any start. The bare answer (A12) is restricted in F, where answers to a call often ask where or how to help, or give a reason (r/sips, r/latin, r/UPenn; r/ducks least well). The one-line answer itself (P15) is untouched in all six forms.

**Sensemaking.** All six forms leave P24 untouched. Members asked what the canvas is and were answered in every form, at about the population's rate: P24 is instantiated in 84 to 95 per cent of each form's defining rooms.

**Collective efficacy.** All six forms leave K02 untouched as a change, although form F instantiates it in 32 of 34 defining rooms, against 82 per cent of the 558; F's rooms judged their room too small or their hands too few, and the change they made was to the move that followed (A10, read under D04). Form B restricts P32: where a member left, the reason given was the room's scripts or an ideology (r/placecanada, r/EraseThePlace), not strain, and attempts to repair a quarrel are seen without their outcome (r/reddevils, r/FederationPlace; r/EraseThePlace least well).

**What the forms add to the dimension.** The model has the call once, at the start. Three forms show it again, after a finish (C), after carrying on or a loss (D) and after a lost spot (F). The account grounds no loop; these link lines are the material for one, and they go to `proposals-D6.jsonl` as an unvalidated proposal (PR-D6-01), not into the model. Two smaller proposals answer branch notes from D5 with the forms' lines: an answer that joins and asks for a task as a second form of acceptance (PR-D6-02, from F's A12 lines and branch F35), and a start that is itself the first call, as a clause in A02's bound (PR-D6-03, from D's and E's A02 lines and branch F32). Elsewhere the forms leave critical mass as the model states it.

### D02, Coordination without command

Written at D6a-02. Form lines in `fractal-forms-D6.jsonl` (78 lines: 13 units by six forms; 21 lean, 57 untouched); branch lines in `fractal-D6.jsonl`.

**In the global model.** Coordination without command is how hands that no one can command come to place the same picture: what settles what the room will make, and what aligns the placing. Six fourth-order themes sit under it. Collective representation is the design (P02). Direct information sharing is members reporting the mark's state as they build (P03). Standardization of output is the template (P04). Workarounds are the scripts, bots and spare accounts (P14), with the site's faults (K06) and members' own time and devices (K05). Backstage decision-making is the chat (P23) and keeping plans from rivals (P33). Decided order is the starter (R01) and the claim that most rooms worked without deciding how they were organized (C01, a decided element in 46 of 705 rooms). Three arrows end here: the call brings builders (A01), a template settles the design (A11, its withdrawal a held proposal), and scripts follow upkeep under strain (A06).

**Collective representation.** Two forms specify the design.
- In C, The design reopened, the design is settled for a time and reopened: a provisional choice made overnight, rough lettering to hold a gap, a finished mark followed by the next addition. r/bardmains, r/gatech and r/aggies show it best; r/uvic least well. F07 and F34 explain it.
- In E, The sub's play, run as work, the design depends on the host and the means: a host's approval for space, the colours and size available, the upkeep of a picture already standing (r/warframe, r/starlightstage, r/yugioh; r/baylor least well). F34 explains it here too.
- A, B, D and F leave P02 untouched.

F34's rooms in C and E size the design to the hands before any loss, a consequence of K02 that the model does not state; it goes to `proposals-D6.jsonl` as PR-D6-05.

**Direct information sharing.** Only F, Moving for the spot, specifies P03: building returns after a move, as a new spot or a replacement plan is followed by a new start (r/wildhockey, r/portal, r/UPenn; r/warthunder least well). F09 (the move returns to building) explains it: 8 of the 12 holders are its rooms. The arrow from the move to building is PR-D6-04. The call-to-building arrow (A01) is restricted in D and E. In D the call and the building overlap, and an active builder also recruits (r/gorillaz, r/gamindustri, r/rotmg; r/cgpgrey least well). In E the two appear apart in the record (r/uwaterloo, r/paragon, r/teslamotors; r/baylor least well).

**Standardization of output.** Three forms specify the template.
- In A, Border terms and the announced plan, members keep the template in step with the placements: they correct references against what is placed and replace stale plans (r/FloydVsVoid, r/stardewvalley, r/kamenrider; r/Villanova least well). F15 explains it: 20 of the 32 holders are its rooms. F15's note asked whether the plan follows the work; in form A it does.
- In C the template is kept current: builders retire outdated posts, announce changed locations and message overwriters (r/torontoraptors, r/eve, r/tf2; r/kuwait least well). F33 explains it.
- In F the template moves with the spot: a new site gets an anchor coordinate (r/dallasstars, r/latin, r/portal; r/warthunder least well).

F15 and F33, which their notes call one change at two nodes, fall in different forms, A and C. C restricts A11. In 40 of its 58 lines the template did not settle the design: colours, sizes and spacing stayed open, or a redesign was repaired away as damage (r/starbound, r/bardmains, r/pitt; r/guatemala least well; F07 and F33). These are the grounds of the held A11 proposal, which stays held.

**Workarounds.** Three forms specify machine hands and two restrict them.
- B, Behind the thread: chat, scripts, raids, runs scripts as shared tools whose targets and versions are kept in step (r/mexico, r/PlaceNL, r/AmericanFlaginPlace; r/aeon least well). F08 (machine hands kept on one target) explains it: 24 of the 33 holders.
- E lets machine hands help only on conditions: matching targets, agreed overlaps, updates reaching every runner (r/mls, r/dota2, r/teslamotors).
- F keeps scripts and overlays in step across accounts, and members switch automation off to place by hand (r/wildhockey, r/predators, r/sbu; F08).
- A and D restrict P14. There scripts are offered, debated and refused, and the record shows the offer more than any placing (A: r/FloydVsVoid, r/mindcrack, r/prequelmemes; D: r/rutgers, r/danganronpa, r/Temple, with F24).
- A06 is restricted in D and F. Scripts did not wait for strain: they were offered for a new build or a move, or came with the first request to coordinate construction (D 12 of 21 lines fail as stated; F: r/sips, r/wildhockey, r/uiowa).
- K05 and K06 are untouched in all six forms.

**Backstage decision-making.** B specifies the chat. It works on conditions: invitations that work and a current plan members can find (r/mexico, r/quebec, r/reddevils; r/lithuania least well). F16 and F29 explain it, the chat family the D5 notes read as one change with three ops. A specifies the chat's upkeep: expired invitations are replaced and decisions are brought back for members outside it (r/berserk, r/theexpanse, r/de; r/japan least well). Inside A, F30 (the chat seen only through its invitations and returned reports, not its choices) restricts P23: its rooms are 10 of A's 16 restrict holders, and they show the chat only from outside, through invitations, venues offered and reports that come back (r/xcom, r/forsen, r/prequelmemes; line added at D6a-07). E restricts P23: its threads hold invitations and claims brought back, not how the chat decided. No form changes P33.

**Decided order.** A and C restrict C01. In their lines, rooms divided the work, appointed representatives, assigned defenders or pixels, and endorsed a template, though implementation is not shown and the population count is not tested. A's best rooms are r/FloydVsVoid, r/furry and r/berserk; C's are r/PUBATTLEGROUNDS, r/bisexual and r/gatech. R01 is untouched.

**What the forms add to the dimension.** Each form specifies the part of coordination its name says:
- A, the template kept in step with the placements and a division of the work;
- B, shared scripts and a chat that works only on conditions;
- C, the design reopened and the template kept current;
- E, design and scripts on the host's and the tools' conditions;
- F, building again after a move, with a template that moves with the spot.

D specifies nothing here; it restricts the order of call and building and the arrow from strain to scripts. Two unvalidated proposals come from this dimension: PR-D6-04 (after the move, the room builds again) and PR-D6-05 (the design sized to the hands before any loss).

### D03, Maintenance

Written at D6a-03. Form lines in `fractal-forms-D6.jsonl` (18 lines: 3 units by six forms; 4 lean, 14 untouched); branch lines in `fractal-D6.jsonl`.

**In the global model.** Maintenance is what keeps a finished work alive on a surface anyone can change, and how a room decides what a change to its work was. Two fourth-order themes sit under it. Repair work is keeping (P05): members watch the work and repair changed pixels, rally under attack, cover the night, harden the shape and put upkeep before growth. Its second and third sentences are the telling clause. Repair restores the form the keepers know, so a change the room planned is repaired away until its keepers are told of it. Attribution is working out who changed the work and why (P06). One arrow ends here: once a mark stands, keeping it becomes the work (A03, building then keeping). Four D5 findings bound the telling clause: F-024 (the change read from its shape, informed members holding it), F-025 (informed members reject it), F-026 (at the border) and F-027 (in keeping). The held P05 proposal states the first of these as a bound, and it stays held (QD4-001).

**Repair work.** Four forms change keeping, each in its own way.
- In A, Border terms and the announced plan, keeping takes conditions and links. Protecting a neighbour can mean undoing the room's own overextension (r/FloydVsVoid). Keepers can refuse a change they know of as a takeover (r/de). Repair follows the keeper's own idea of the right form, even when that form holds a spelling error (r/prequelmemes). An announced finish is followed by repair and renewed defence (r/stardewvalley, r/ripcity). F32 (the marking returns to keeping) explains the links: 9 of its rooms hold them. r/halo shows the form's keeping least well.
- In C, The design reopened, the lines restrict the telling clause. Informed members refused changes, or the record cannot tell ignorance from dissent, and none of the 47 lines shows a change lost only for want of telling (r/bardmains, r/pitt, r/PUBATTLEGROUNDS; r/pusheen least well). F07 (the telling clause not shown at the design) explains it: 34 of its rooms are among the 46 that restrict.
- In D, Keeping, with help or carrying on, keeping is shared and checked. Watches are volunteered and handed on, keepers check the current canvas and the intended form before they repair, and the room ranks what to keep (r/portugal, r/mylittlepony, r/rotmg; r/glasgow least well). F27 explains part of it: two of its four rooms here check whether a change is intended before undoing it (r/OnePiece, r/radiohead).
- In F, Moving for the spot, keeping begins before the mark is finished. A border reserves the space, defenders are planned before a stable work exists, and a repair tool's reference image is diagnosed and changed (r/wildhockey, r/portal, r/planetside; r/clubpenguin least well). F08 explains the machine part.
- B, Behind the thread: chat, scripts, raids, and E, The sub's play, run as work, leave P05 untouched. E instantiates it in 71 of 84 defining rooms, against 93.4 per cent of the 558; its records hold less keeping.

A03, building then keeping, is untouched in all six forms.

**Attribution.** P06 is untouched in all six forms. Form D comes nearest: 9 of its defining rooms add steps to working out who changed the work, at 2.01 times the 558's share, one room under its floor of 10.

**The telling clause, read across the forms, as the D5 notes asked.** The forms that touch the clause show four ways it holds only in part:
- informed keepers refuse a change: C, and r/de in A (F-025);
- the news must cross to a neighbour: the border, read under D04 (F-026);
- a script keeps the old form until its operator changes the target: F, and branch F08 (F-027's machine route);
- keepers check before they repair: D.

The last is a route by which keepers learn of a planned change other than being told. It is the step the room models of r/OnePiece, r/cowchop and r/armok proposed (F27's note), and it goes to `proposals-D6.jsonl` as PR-D6-06, unvalidated. No form's lines show a planned change lost only because its keepers were not told. P05's statement is unchanged, and the held proposal stays held.

**What the forms add to the dimension.** Every form keeps its work as P05 states it. What differs is when keeping starts and how keepers learn the intended form:
- A ties keeping to the neighbours and to the finished mark;
- C meets the telling clause with refusal;
- D shares and checks the keeping;
- F keeps the spot before there is a mark to keep.

### D04, Order without law

Written at D6a-04. Form lines in `fractal-forms-D6.jsonl` (120 lines: 20 units by six forms; 22 lean, 98 untouched); branch lines in `fractal-D6.jsonl`.

**In the global model.** Order without law is how rooms that cannot compel one another keep order between their works on one canvas. Five fourth-order themes sit under it. Live and let live is sparing: rooms spare their neighbours' work, rein in their own attackers and apologise for damage (P07), and members argue whether covering others' work is fair (P31, a candidate). Negotiated order is border terms: rooms propose, settle and contest borders, truces and deals (P08), through envoys (R02). Members say that one member's agreement does not bind every placer (P21), and some members belong to both rooms (K07, a candidate). Reciprocity is help between rooms (P16). Meta-organization is coalitions (P17). Territoriality is the spot: the room chooses where to build before any loss (P27, a candidate), moves after a loss (P10), and lives on a host's mark under the host's rule (P19). Nine arrows end here. Keeping the mark brings the room to its neighbours (A04), and an attack call is met with a truce (A17). A settled border is a line members keep (A05), and an attack call is refused inside the room (A16). Short of hands, a room turns to other rooms (A13), and a settled border opens a channel for help (A14). Under attack, works defend each other (A19). Too few hands, so the room moves (A10). A21 runs from an agreement to the dispute over who may commit the room. F-020 bounds the dimension: sparing rests mostly on the room's own norm, and help rests on a deal about as often as not.

**Live and let live.** Four forms specify sparing, each with its own condition.
- In A, Border terms and the announced plan, sparing rests on overlapping membership, valued neighbouring art or fear of retaliation, and on placers whom the negotiators admit they cannot control (r/foxes, r/twice, r/hellointernet; r/germany least well).
- In B, Behind the thread: chat, scripts, raids, sparing passes through the room's tools. An instruction to spare agreed space must reach script users as a target update, and admitted script damage brings apology and repair (r/PlaceNL, r/theitalyplace, r/monero; r/asexual least well).
- In C, The design reopened, the room states its reason for restraint: an apology after a complaint, or help and space received from the neighbour (r/bisexual, r/farmcarrots, r/metroid; r/kindafunny least well).
- In D, Keeping, with help or carrying on, restraint protects the room's own logo, repays earlier help, and does not reach every placer (r/gamindustri, r/denverbroncos, r/portugal; r/magictcg least well).

A05, the settled border kept, changes in three forms. A restricts it in 39 of 135 defining rooms. Restraint often comes before any settlement is shown, and a treaty guides the members who learn and accept it while others keep placing against it (r/stardewvalley, r/furry, r/berserk; r/RelientK least well). F26 (the telling clause not shown at the border) explains the second half: its rooms keep a border only where placers learn and accept its terms (r/placetardis, r/furry, r/thailand). B and D add the condition that the terms reach the placer (B: r/quebec, r/reddevils, r/AmericanFlaginPlace; r/neu least well. D: r/bindingofisaac, r/denverbroncos, r/mylittlepony; r/pepe least well). In B, F08 (machine hands kept on one target) explains part of it: an accommodation needs compatible script targets (r/india, r/AmericanFlaginPlace). In D some placers do not learn of the truce (r/bindingofisaac, r/radiohead). Read together, these lines state F-026 for the border. Told placers stop. Placers the terms do not reach keep placing, and a script keeps placing until its target is changed. The reading goes to `proposals-D6.jsonl` as PR-D6-07, a bound on A05, unvalidated.

E, The sub's play, run as work, restricts A16. Its restraint answers reported harm, overlap or a planned enlargement, not a written attack call refused inside the room (r/uwaterloo, r/starlightstage, r/hunterxhunter; r/wow least well). No form changes P31. E comes nearest, with 8 restrict holders, one room under its floor of 9.

**Negotiated order.** Three forms specify border terms.
- In A, border terms take work and meet limits (r/FloydVsVoid, r/catalunya, r/twice; r/kurdistan least well). F10 (a deal carried out as work) explains it: 14 of its rooms hold the deciding lines. Members discuss a border inside the room before contact (r/drawhelix), check a request's consensus and credibility (r/switzerland), and carry the terms to placers and templates, a step members say is still incomplete (r/poland, r/transformers). Identity colours limit what members concede (r/twice), and uncontrolled placers can defeat a promise (r/littlewitchacademia).
- In B, border talk has steps before and after it: a treaty request before any damage, local consensus before a proposal, and a negotiated move relayed to builders (r/linux, r/czech, r/FederationPlace; r/duckgame least well).
- In C, agreements are kept apart from compliance: members report attacks after announced terms, and a truce needs a counterpart able to keep it (r/torontoraptors, r/gatech, r/suomi; r/earthbound least well).

F, Moving for the spot, restricts A04. In 13 of its 34 defining rooms border talk comes before keeping. Rooms ask neighbours for permission or access while they seek a spot (r/dallasstars, r/sips, r/wildhockey; r/Northwestern least well), or a neighbour objects when the room's building or script crosses its work (r/KState, r/httyd). No branch explains the cell. F09's rooms hold 4 of the 13 lines, but F09's change is building again after a move. The two routes go to `proposals-D6.jsonl` as PR-D6-09: arrows from choosing the spot (P27) and from building (P03) into border terms, beside A04, unvalidated. R02, P21, K07, A17 and A21 are untouched in all six forms.

**Reciprocity.** Two forms specify help, and one branch specifies it where its form does not.
- In C help is part of the room's own building. Helpers alternate placements between the two works, and paired scripts give spare capacity to the neighbour (r/starbound, r/pitt, r/timbers; r/bretagne least well).
- In D help waits on the helper's own work (r/gamindustri, r/rutgers, r/mylittlepony; r/OneTrueEmilia least well). F22 (help conditional on the helper's own work and spare hands) explains it: 11 of its rooms hold the deciding lines. Donors give when their work is secure and pixels are spare (r/mylittlepony, r/OnePiece), and they weigh what the help does to a third room's mark (r/gamindustri).
- In A the form leaves P16 untouched, but F28 (help at the border conditional) specifies it: its rooms are 10 of the form's 22 add-condition holders. The helper's home work must be safe (r/ripcity, r/utaustin), the neighbour must stop attacking (r/catalunya), and promised help stays apart from help delivered (r/lsu, r/necrodancer).

C and D restrict A13, short of hands, a room turns to other rooms (C 30 of 96 defining rooms, D 33 of 96). In C donors help from completed or well-kept work, and help comes with construction and overlap repair (r/bardmains, r/cubers, r/PUBATTLEGROUNDS; r/uvic least well). F07's rooms hold 12 of the 30 lines, but F07's change is the telling clause, not help, so it does not explain the cell. In D help comes from surplus more than shortage. Donors give after their own work is finished or safe, repay earlier protection, and put off help while their home defence is short (r/gamindustri, r/bindingofisaac, r/denverbroncos; r/cgpgrey least well). F22 explains part of it: aid repays earlier protection once the room's own image is finished (r/OnePiece), and donors weigh their own work's safety (r/mylittlepony). Read with F22 and F28, the lines say that a shortage brings the request, and the donor's spare hands decide whether help comes. This answers the D5 note on D's A13. It goes to `proposals-D6.jsonl` as PR-D6-08, unvalidated. In 12 other lines a request is recorded and arriving help is not shown; the record cannot tell whether it came.

A restricts A14, a settled border opens a channel for help. In A help is part of the bargain more than its result: pixels and shared upkeep are offered as the terms, or help is under way when the bargaining starts (r/catalunya, r/jerma985, r/empiredidnothingwrong; r/norway least well).

**Meta-organization.** P17 and A19 are untouched in all six forms.

**Territoriality.** Three forms change the spot and the move.
- D restricts P19, hosting. Guests ask for space or depend on a host, but a grant, an approval procedure or a durable host rule is not shown (r/gorillaz, r/gamindustri, r/denverbroncos; r/sadboys least well). F restricts it the same way, at the request stage (r/sips, r/latin, r/UPenn; r/streetfighter least well). In A the form leaves P19 untouched, but F31 (hosting as one-off permission) restricts it: its rooms are 8 of the form's 12 restrict holders. An overlap is permitted for one arrangement (r/foxes), a replacement permission is called provisional (r/malaysia), and an incorporation is offered and accepted on conditions (r/mindcrack). In all three forms hosting shows as a request and a single permission, not a standing host rule.
- F restricts P27. The choice of spot also comes after a loss: the room picks a new site or a backup while another of its works has been lost (r/penguins, r/twitch, r/ethoslab; r/dbz least well). The before-loss bound holds for the site decision, not for the room's whole history.
- E and F restrict A10, too few hands, so the room moves. In E a judgment of too few hands ends one member's part or one expansion, while the others keep repairing, recruit or finish (r/fivenightsatfreddys, r/mls, r/worldoftanks; r/battlecats least well). In F the move answers the spot more than the hands. A taken spot or a lack of permitted space moves the room, and where members name too few hands, the move is only proposed or hesitant (r/wildhockey, r/latin, r/twentyonepilots; r/warthunder least well). This answers the D5 note on F's A10. P10's statement already names the loss of the spot as the move's cause, so the reading needs no proposal. It bounds A10 as F-019 does, where the loss itself prompted the move in 10 of 21 rooms.
- P10 is untouched in all six forms. F comes nearest, with 3 restrict holders against a floor of 5.

**What the forms add to the dimension.** Every form keeps order between rooms as the model states it, by sparing, terms and help. What differs is how far the order reaches:
- A holds sparing and terms to the placers the terms reach, and makes help part of the bargain;
- B carries terms to placers and scripts;
- C states its reasons for restraint and helps from its own building;
- D gives help from surplus and keeps hosting at the request;
- E restrains without a refused attack call, and a judgment of too few hands ends a member's part, not the room's place;
- F talks with neighbours before it has a mark, and moves for the spot.

Three unvalidated proposals come from this dimension: PR-D6-07, PR-D6-08 and PR-D6-09.

### D05, Collective identity

Written at D6a-05. Form lines in `fractal-forms-D6.jsonl` (36 lines: 6 elements by six forms; 0 lean, 36 untouched); no branch lines.

**In the global model.** Collective identity is what a room brings to the canvas as a body, and what it makes of itself there. Four fourth-order themes sit under it. Frame bridging, the carrying of a frame from outside the canvas into it, holds the quarrel the community carries in (K03) and the new jokes members make out of the canvas work (P26, a candidate). Flagging the nation holds the room acting as the body it was before the canvas (K04): it argues the nation's history and belonging, carries in the sub's lore, jokes or ideology, or professes a colour as a faith. The same theme holds C02: in some rooms a tie from before the canvas names the rival in the turn that calls for the attack, a claim untested for order. Neo-tribes, groups that form around a shared sign, holds the room that forms for the canvas around a mark (P28, a candidate) and K04's faith in a colour. Symbolic boundaries holds what members say offends: they refuse slurs and hate symbols and argue over jokes (P29, a candidate). No arrow ends here. C02 also sits under Contention and P28 under Host framing; their lines are written here once.

**No form changes collective identity.** All 36 cells are untouched. Changes to these elements are rare in the population. Across the 558 defining rooms the most common is a restrict line on C02, in 35 rooms; then P28 (18), P26 (13), and K04 and P29 (12 each). No form reaches its floor, which runs from 5 to 14 defining rooms. The nearest cells are C02 in B (9 restrict holders against a floor of 12) and P26 in D (6 against 10, at 2.68 times the share). Among the branches that lean to a form, the most any holds on one op is 4 rooms (F07 on C02 in C).

Of the restrict lines I read (the nearest cells and form B's), nearly all say what the record cannot show, not that the element fails:
- on C02, a national, historical or lore frame names a target, but the record does not show that a tie from before the canvas selected it (r/austria and r/dwarffortress in B; r/switzerland and r/xcom in A; r/costa_rica in D);
- on K03, invoked national history does not show an earlier quarrel between the two subs (r/england and r/quebec in B);
- on P28, a venue or a chat is opened, but the record does not show the room's founding or its first recruits (r/osugame, r/prequelmemes and r/TheFarLeftSide in A; r/czech in B);
- on P26, a joke is made, but the record does not show that the room took it up or kept it (r/frc and r/gameattack in D; r/habs and r/paladins in E).

A few lines say the element fails as stated: a rival named by some members divides the room instead of aligning it (r/chicago in C), and one member's ideological target is not the room's when another member turns that effort to helping allies (r/mylittlepony in D).

**Where the forms differ: how often they hold it.** The forms keep these elements as the model states them, but their rooms hold them at different rates (each form line gives its count):
- B, Behind the thread: chat, scripts, raids, holds every element of the dimension above the 558's rate. The largest gaps are C02, in 28 of 113 defining rooms (25 per cent, against 16), and P28, in 20 (18 per cent, against 11). The carried quarrel is held in 31 (27 against 21), the room as a prior body in 91 (81 against 70), and the argument over offence in 30 (27 against 20).
- F, Moving for the spot, holds them least: K04 in 18 of 34 (53 per cent), C02 in 2, P28 in 1 and P29 in 4. Its records are the shortest of the six forms (median 64.5 coded concepts), so the low rates may follow from short records.
- E, The sub's play, run as work, has the longest records (median 222 concepts) and still holds C02 in 9 of 84 (11 per cent) and P28 in 3 (4 per cent). Record size does not explain B's high rates: B's median record (131 concepts) is shorter than D's (142) and E's.
- New jokes made from the canvas (P26) are held at about the same rate in every form, from 73 to 81 per cent, against 78.

These are rates of instantiation, not changes, and the rule does not test them. They say where identity sits. In B, the form named for chats and raids, the room brings its prior quarrel and body to the canvas, and some rooms form around a mark: r/purplecorner sustains a split over which colour is legitimate, and r/thebluecorner, a day-old group, claims its own lore. r/thebluecorner is also the room that most threatens the account, a colour faction whose faith names its rivals and rules on guests. C02 is read again under Contention.

**The D5 notes that touch this dimension.**
- F14 (D5a-14), kept damage beside P26 and P05: in three rooms the final damage became part of the emblem once the canvas was locked. P26 is untouched in every form, and F14 has 7 members, so the case stays a particular of three histories, as the note said. F14's line comes with its key, P13, under Imprinting.
- F23 (D5a-23), a group outliving its task: rooms formed for the canvas asked whether to last, set goals or closed and reopened on a new canvas. P28 is untouched in every form. F23's line comes with its key, P13, under Imprinting.

**What the forms add to the dimension.** Nothing to its statements. No form specifies, restricts or replaces an element of collective identity, and no branch changes one inside a form. The forms differ in how often their rooms bring identity in: B holds it most and F least. No proposal comes from this dimension.

### D06, Host framing

Written at D6a-06. Form lines in `fractal-forms-D6.jsonl` (24 lines: K01, P20, P34 and A20 by six forms; 5 lean, 19 untouched; P28's lines were written under D05); branch lines in `fractal-D6.jsonl`.

**In the global model.** Host framing is what the host sub does around the room's canvas work. Two fourth-order themes sit under it. Keying, the framing of an activity as something other than what it seems, holds K01: the host sub is keyed as play for April Fools, members post fakes and takeovers under the one-day licence, and a claim in it, a call to the canvas included, may be a joke. Boundary work, the drawing of a line around an activity, holds P20 and P34. The host sub draws a line around canvas talk (P20): moderators gather it into a megathread, remove canvas posts by rule or pause the sub's usual events, and members open a canvas sub or object to the flood. Members who object to the canvas posts can turn against the room's own mark (P34, a candidate held by two rooms). The room that forms for the canvas around a mark (P28) sits here too; it is told under D05. One arrow ends here: calls flood the host sub, and the host draws a line (A20, strong, 132 of 155 rooms). Its bound says the line is partly constitutive, and that 23 of the 155 rooms draw it before the room calls.

**Keying.** Three forms specify the frame, all by added steps.
- In E, The sub's play, run as work, the play is run as work (r/warframe, r/fivenightsatfreddys, r/mls; r/polandball least well). Moderators start it and set its rules, real removals and bots enforce them, members test claims and repair what the styling breaks, and they argue its end by the clock and the time zone. 58 of the 84 defining rooms hold these lines, 56 of them as added steps (66.7 per cent, against 18.5 per cent of the 558). F01 (the play administered) explains the cell: 54 of the 58 holders are its rooms. Each of its subforms explains one part of it:
  - F02 (the takeover run as a temporary regime): fictional rules enforced by real removals (r/battlecats, r/zelda), mock bans and resignations performed (r/acecombat, r/ontario), and the licence ended by restoring ordinary rules (r/MMA);
  - F03 (the joke tested): claims checked by sources and the date (r/yugioh), an author's authenticity tested after the takeover ended (r/hunterxhunter), and a joke told from an earnest mistake (r/drumcorps);
  - F04 (the licence policed): compulsory joke participation contested (r/monstercat), and the licence's end disputed (r/dankmemes);
  - F05 (the styling ended): styles switched off or the font uninstalled (r/pcmasterrace, r/schoolidolfestival), and the joke period ended by a moderator (r/popheads);
  - F06 (the joke kept): permanent flair, a real version of an invented reward, or the banner kept (r/mls, r/runescape, r/rust).
- In D, Keeping, with help or carrying on, the play is administered beside the keeping (r/bindingofisaac, r/denverbroncos, r/nyjets; r/yuyuyu least well). Members dispute when the joke ends, test fakes by date and source and police tasteless claims, and moderators restore the ordinary styling. 21 of the 24 holders are rooms of D.2, Keeping inside the sub's play, the split of form D whose rooms keep their canvas work inside the sub's play. F04 explains part of it: members demand restoration and dispute the prank's duration (r/chelseafc), and set tasteless death claims apart from jokes everyone can enjoy (r/bostonceltics).
- In F, Moving for the spot, members argue the play's limits more than they run it (r/dallasstars, r/wildhockey, r/stargate; r/streetfighter least well). F04 explains part of it: members contest a painful prank, and moderators apologise and remove an official-looking endorsement (r/stargate, r/nbaspurs).
- A, Border terms and the announced plan, B, Behind the thread: chat, scripts, raids, and C, The design reopened, leave K01 untouched.

F01's rooms are 23 of D's 24 holders and all 9 of F's, but F01 leans to D and F at 1.32 and 1.22 times its share, under the rule's 1.5, so it is not named there. The form notes asked whether F01 and form E restate each other. They do in part: 59 of F01's 103 rooms are in E, all five subforms lean to E, and F01 explains E's only leaning cell in this dimension. The other 44 of F01's rooms lie in D (23), F (10), C (6) and B (5). F01 is therefore a facet that runs mostly inside E and reaches D's split D.2, not a second name for E.

F21 (the canvas call not a joke) leans to E. Its rooms there restrict the frame, but few of them in F21's own terms. In r/scp the play does not show that the canvas calls were false, and in r/borussiadortmund a recognised prank does not make the canvas construction a fiction. The other lines bound details of the play, such as styling kept or the calendar. In r/osu the play reached the canvas work: a redirect blocked reinforcement and sent members to a chat. The record shows the play running beside the canvas work in most rooms and reaching it in a few (r/osu and r/polandball here; r/battlecats and r/bindingofisaac in the D5 notes).

The form notes also said that the model holds the play only as a key. The cells bear it out: in E, D and F the play is organized work with the steps the model gives the canvas work, and the model has no element for those steps. The reading goes to `proposals-D6.jsonl` as PR-D6-10, a process element beside K01, unvalidated. It would bring into the model the sub's own business that the scope ruling of D3a-55 put outside it, so it is a change of scope as well as a new element.

**Boundary work.** D specifies P20: the host makes room for canvas talk inside the sub as well as drawing a line around it (r/denverbroncos, r/mylittlepony, r/nyjets; r/sabres least well). Moderators offer a sticky (r/texans), mark canvas posts with flair (r/kirby), refuse a requested ban while keeping the organising thread (r/chicubs) and reverse a removal after checking in their chat (r/mylittlepony). Members contest removals or move to another venue because of them (r/canada). No branch explains the cell.

D also restricts A20 (r/rutgers, r/bindingofisaac, r/denverbroncos; r/polyamory least well). In its 10 lines the host's line is not shown to answer a flood of calls. Moderators route talk for visibility and timing, apply existing rules on duplicates and images, or decline a sticky for want of slots (r/radiohead, r/kpop, r/bostonceltics). The record does not show the calls flooding the sub first. This lies inside A20's bound, which already says the line is partly constitutive and sometimes comes first; no proposal. P34 is untouched in all six forms, and the held proposal beside it (members spoiling their own room's mark for fun, r/paladins and r/portugal) stays held.

**What the forms add to the dimension.** The forms differ on the frame, not on the host's line:
- E runs the April Fools play as work, and the frame family F01 to F06 explains it;
- D administers the play in its split D.2 and is the one form that changes the host's line, which in D makes room for canvas talk and is not shown to answer a flood;
- F argues the play's limits;
- A, B and C hold the frame and the host's line as the model states them.

One unvalidated proposal comes from this dimension: PR-D6-10.

### D07, Imprinting

Written at D6a-07. Form lines in `fractal-forms-D6.jsonl` (54 lines: 6 elements and 3 arrows by six forms; 11 lean, 43 untouched; K05's lines were written under D02); branch lines in `fractal-D6.jsonl`.

**In the global model.** Imprinting is what the room does to make its temporary work last beyond the canvas. Four fourth-order themes sit under it. Completion ritual holds the marking: when a work is up, the room announces it, celebrates it, credits makers and helpers, and says what working with strangers meant (P11). Collective memory holds the record: screenshots, timelapses, reports of the work's fate, mourning, atlas entries and the end marked (P12). The same theme holds the contest over which version of the canvas and the event is kept, after placement ends (P22). Transition holds carrying on: near the close and after it, the room decides what of its effort to keep, such as a later canvas, a new purpose for its sub, the mark in its banner or the work remade elsewhere (P13). Visibility returns holds what the work brings back: new members who found the sub through the mark (P25, a candidate) and the notice of the people the mark shows or addresses (P30, a candidate). Three arrows run through the dimension in order. A finished mark is marked together (A07, 139 of 182 rooms), what is celebrated is kept on record (A08, 225 of 289), and the record is what passes on (A09, 113 of 145). Their bounds already admit the late side: a mark found already made, a work the close cut short, a record that comes first, and a next canvas planned while still building.

**Completion ritual.** Two forms specify the marking.
- In A, Border terms and the announced plan, the marking is provisional and contested (r/ripcity, r/utahjazz, r/opticgaming; r/halo least well). Success is judged and credit disputed while the work goes on, an announced finish reopens the work, and members celebrate a damaged remnant or partial progress. Three branches explain it:
  - F17 (the marking provisional and contested), 16 of the 21 holders: credit is checked and corrected during building (r/anime, r/vocaloid), and a finish is announced and the work reopened (r/taiwan);
  - F19 (credit contested during the work): members challenge who may claim credit (r/opticgaming) and ask for the names of forgotten helpers for a memorial (r/SwissNeutralityZone);
  - F18 (success judged while upkeep continues): celebration keeps the duty to maintain (r/ripcity), and success is weighed project by project (r/ftlgame).
- In D, Keeping, with help or carrying on, the marking is weighed (r/denverbroncos, r/yogscast, r/edmontonoilers; r/rojava least well). Members correct the room's name in the celebration, challenge and prove credit, and credit an effort that did not survive. F18 explains part of it: a mark recognizable and lasting enough counts as victory despite defects (r/kirby), and recognizable survival outranks perfect lettering while maintenance goes on (r/bostonceltics).

E, The sub's play, run as work, and F, Moving for the spot, restrict A07. In E the marking does not wait for a finished mark. Rooms celebrate a surviving emblem with planned additions unfinished, an incomplete attempt or a milestone, and pride and disappointment share the thread (r/pcmasterrace, r/uwaterloo, r/hunterxhunter; r/homelab least well). In F the marking answers a partial or traced work (r/twentyonepilots, r/nbaspurs, r/penguins; r/warthunder least well). F09 (the move returns to building) explains part of it: two of its three rooms here mark an unfinished work after moving (r/penguins, r/warthunder).

**Collective memory.** A specifies P12: the record holds more than the result (r/furry, r/theexpanse, r/jerma985; r/DCFU least well). Members mourn a destroyed neighbour with a memorial artwork, keep an imagined version of the hoped-for design, and help a viewer find a small surviving mark in the final image. F specifies P12 by links (r/corridor, r/planetside, r/qotsa; r/streetfighter least well). A locating question draws a fate report, and unfinished construction at the close leads straight to a tally and mourning, with no celebration between. B leaves P12 untouched, but F20 (the close as news) specifies it there: its rooms are 3 of B's 10 add-step holders. A closure reply corrects a rebuild call (r/chibears), and a member learns of the end after offering to restart (r/stlouis).

E restricts A08 (r/warframe, r/fivenightsatfreddys, r/mls; r/homelab least well). In its 24 lines the record does not wait for the celebration. Timelapses, live updates and reports of loss run before any celebration (r/minecraft, r/python, r/uoft). Where both appear, the lines show a sequence, not that the celebration caused the record. P22 is untouched in all six forms; A comes nearest, with 10 restrict holders against a floor of 14.

**Transition.** D specifies P13: carrying on is new work begun before the close (r/gamindustri, r/bindingofisaac, r/portugal; r/cgpgrey least well). Five branches of the carrying-on family explain it:
- F11 (carrying on as renewed work, begun before the close), 18 of the 30 holders: a successor canvas restarts recruiting, building and defence, and alternative canvases are discussed while placement is live (r/italy);
- F12 (the spine restarted on another canvas): construction, repair and destruction return on a live successor venue (r/furry_irl), and members weigh traffic and mobile access when they choose it (r/greyblob);
- F23 (the close scoped to the original canvas): hour 73 ends placement there while successor canvases allow more (r/rotmg, r/catholicism);
- F13 (the work remade in other media): a territorial claim lives on as copypasta (r/portugal), and members teach how to reproduce the image by hand (r/romania);
- F14 (the mark adopted as the room's emblem while it is still placed, damage included): an unwanted final blemish is valued as the emblem (r/cgpgrey).

The D5 notes asked whether F11 and F23 are one set of events read with two ops. In this cell they share 4 of F23's 9 holders (r/bindingofisaac, r/cgpgrey, r/greyblob, r/naruto). This is the overlap expected of two groupings that meet at one node; it is not one branch. F14's kept damage, noted at D5 beside P26 and P05, shows here in r/cgpgrey, and in form A in r/utahjazz, where members joke about an imperfect finish and take shared pride in the damaged work.

E restricts P13 (r/warframe, r/pcmasterrace, r/stevenuniverse; r/totallynotrobots least well). Carrying on is invited or proposed more than taken up: a successor canvas or a reused chat is offered, and adoption is not shown. F25 (carrying on in talk) explains it: 7 of the 10 holders are its rooms (r/paladins, r/starcitizen).

D and E restrict A09. In D carrying on does not wait for the record (r/rutgers, r/bindingofisaac, r/mylittlepony; r/magictcg least well). Successor invitations, reuse and remaking come before or beside the final image. F11 explains part of it: design reuse precedes the close (r/lovelive), and preservation starts from an interim image (r/texans). In E carrying on follows the record in order, but no line shows the record causing it, and uptake is not shown (r/warframe, r/starlightstage, r/stevenuniverse; r/homelab least well). Many of these lines deny that a saved record caused the room to carry on. A09 is an order and does not claim that, which bears out the D5 note that the account's words for A09 should state an order, not a cause.

**Visibility returns.** P25 and P30 are untouched in all six forms. P25 comes nearest in B, with 8 link holders at 2.32 times the share, against a floor of 12.

**Read across the forms.** The forms that change this dimension show one pattern. The marking, the record and carrying on often begin while the work is being built, and the rooms mark and record an attempt cut short or lost. The order of the three arrows still holds in most rooms, as their counts say. In 46 rooms of A, D, E and F the lines say the act came during the work, before a finish or after a loss (my reading). The reading goes to `proposals-D6.jsonl` as PR-D6-11, bounds on P11 and P13 and wider bounds on A07, A08 and A09, unvalidated. It answers the D5 notes that A07's bound does not cover marking during the work, before its finish, after its loss or on a spot held on leave (F27, F30 and F31).

**What the forms add to the dimension.**
- A marks while the work goes on and disputes the credit, and its record holds mourning and imagined versions;
- D weighs the marking and carries on as new work begun before the close;
- E marks unfinished work, records before it celebrates and invites successors that the record does not show taken up;
- F marks partial work and records failure;
- B carries the end as news only in F20's rooms, and C leaves the dimension as the model states it.

One unvalidated proposal comes from this dimension: PR-D6-11.

### D08, Contention

Written at D6a-08. Form lines in `fractal-forms-D6.jsonl` (24 lines: P09, P18, A15 and A18 by six forms; 2 lean, 22 untouched; C02's lines were written under D05 and P33's under D02); no branch lines.

**In the global model.** Contention is how rooms fight over the canvas and over each other. Two fourth-order themes sit under it. Repertoire of contention, the set of moves a group has for attacking others, holds P09: rooms attack others' work by the moves the canvas affords, such as erasing, encroaching, converting a sign, raiding on a streamer's call, planting a script or altering a work as a joke. Rivalry holds P18: rooms carry a contest with a rival room in talk, trading taunts, flooding the rival's threads, claiming victory, saluting the rival after the fight and blaming attackers after the close. Both themes hold C02, the claim that a tie from before the canvas names the rival in the turn that calls for the attack, untested for order. Repertoire of contention also holds P33: rooms keep their plans from rivals who read their threads and reach into the rivals' venues (a candidate). Two arrows end here: a call's hands can turn on a rival (A15, strong, 93 of 129 rooms), and an attack is carried on in taunts (A18, fair, 56 of 68). A15's bound says that where a room's first canvas act is an attack, the attack call is the first call. Two more arrows start here and end in Order without law: an attack call is refused inside the room (A16) and met with a truce (A17). They are told under D04.

**Repertoire of contention.** No form changes P09. Two forms restrict A15.
- In B, Behind the thread: chat, scripts, raids, the record does not show a call's builders turning on a rival (r/PlaceNL, r/virginiatech, r/india; r/shitredditsays least well). Of its 18 lines, 7 fall inside A15's bound by my reading. The attack call is the first call or shares the opening turn with recruitment (r/ohio, r/virginiatech, r/HomestarRunner), or an attack call recruits directly (r/shitredditsays). In the other 11 the lines show the order of the calls but not that the same recruited hands attacked (r/india, r/latvia, r/Russiaclan). The D5 notes on form B counted the same 11.
- In E, The sub's play, run as work, the attack talk sits inside the recruiting (r/fivenightsatfreddys, r/dota2, r/stevenuniverse; r/pokemon least well). Recruitment and attack proposals share a thread or a call, and the lines do not show that recruited builders became the attacking hands. In r/habs the switch ran the other way, from a rival's interference to helping the room's own mark.

No branch explains either cell. F08 holds 4 of B's lines and F01 10 of E's, but their changes concern machine hands and the April Fools play, not the turn from building to attack. The restrictions mostly say what the record cannot show. A15 is an order (93 of 129 rooms hold it), and its gloss, "a call's hands can turn on a rival", reads as if the same hands were followed from the build to the attack. They are not followed in the record. This is a wording item for A15, like A09's under D07, and it is held with the arrows' wording items; no proposal.

**Rivalry.** No form changes P18 or A18. A18 comes nearest in B and E, with 8 and 6 restrict holders at 1.7 times the share, against floors of 12 and 9.

**Where the forms differ: how often they hold it.** As with Collective identity, the forms keep these elements as the model states them but hold them at different rates (the form lines give each count). B holds contention most. P09 is held in 103 of its 113 defining rooms (91 per cent, against 79 of the 558), P18 in 88 (78 against 61), C02 in 28 (25 against 16) and P33 in 18 (16 against 9). F holds rivalry least: P18 in 10 of 34 (29 per cent), on the shortest records of the six forms. E holds P18 in 41 of 84 (49 per cent) on the longest. These are rates of instantiation, which the rule does not test. They put the fight, the taunts and the tie from before the canvas mostly in the form named for chats and raids.

**What the forms add to the dimension.** Nothing to its statements. Two forms restrict the arrow from the call to the attack, mostly on what the record cannot show, and B holds the dimension's elements more often than any other form. No proposal comes from this dimension.

## Part 2. The telling

Written at D6b and corrected at D6a-09 on J's rulings (27 October, 09:27 Berlin). Part 1 read the model one dimension at a time. This part reads it across the dimensions, form by form, then says which forms kept the work alive, what the unadapted group is, what the rooms the model could not compose have in common, and what the forms show that the model lacks. The sensitivity of the form lines to the rule's thresholds follows this part. The figure is `figure-D6.md`. The proposals of this stage are listed at the end, apart from the telling, and none of them is part of the model. Local validation is not established (the frame says why): each room named as showing a pattern shows it in its ruled lines.

### The model with its forms inside it

The model is the version frozen at D3. It has 30 standing elements, 15 candidates and 21 arrows, and its spine runs from a member's start (R01) to the room's calls (P01), to building (P03), to keeping (P05), and on to the marking, the record and carrying on (P11, P12, P13). The six room forms were cut from what the rooms did to that model, not from the canvas. Read against the model unit by unit, each form changes the part of the model its name says and leaves most of the rest as the model states it. Of the 396 form lines (66 elements and arrows by six forms), 37 specify, 35 restrict, 324 leave the unit untouched, and none replaces it.

That last count says less than it seems. A form replaces a unit only where contradict lines lean, and the coding vocabulary made such lines nearly unreachable. The readers returned 11 contradict lines among 42,243 at the first return and 4 among 53,493 at the re-check, and none stands in any form's selected lines. Restrict lines carried much of what a contradict line would have said. Of each form's restrict lines on arrows, as sorted at D5 (one reader's sort), 43 to 63 per cent say that the arrow fails in the room:
- A, 201 of 432 (47 per cent);
- B, 135 of 292 (46 per cent);
- C, 172 of 301 (57 per cent);
- D, 171 of 316 (54 per cent);
- E, 130 of 304 (43 per cent);
- F, 72 of 114 (63 per cent).

A further 6 to 34 lines per form say both that the arrow fails and that the record cannot show it. So no form replaces an element, but "restricts" in this telling covers two things. One is a condition under which the unit holds. The other is a failure of the arrow in the room. The forms do not show that the level below never contradicts the level above. They show that the vocabulary offered almost no way to say so, and that the rooms' lines often said it as a restriction.

Thirty-one units are held by every form as the model states them. Among them are the step from building to keeping (A03), the starter (R01), attack calls (P09), the move (P10), the bare answer (P15), coalitions (P17) and the contest in talk (P18).

**How the forms differ in their functioning.** Each form changes a different part of the model.
- **A, Border terms and the announced plan** (11 units changed) works through terms and a plan kept current. It specifies the template (P04; F15), keeping (P05; F32), sparing (P07) and border terms (P08; F10), the marking and the record (P11, P12; F17, F18, F19), and the chat's upkeep (P23). It restricts the settled border kept (A05; F26), help after a settlement (A14), decided order (C01) and machine hands (P14). In A, terms and plans hold for the placers they reach. None of A's 11 changed cells survives the stricter thresholds (see the sensitivity section).
- **B, Behind the thread: chat, scripts, raids** (7 units) is a residual grouping, not a form, with three facets.
  - The facets are the scripts (Workarounds, held by 49 of its 113 defining rooms), the chat (Backstage decision-making, 48) and the raids (Repertoire of contention, 40).
  - Different rooms hold them, at about chance overlap. 19 rooms hold only the scripts, 22 only the chat and 15 only the raids. 30 hold two facets and 7 hold all three, against 7.4 if the facets were independent. 20 hold none (`_analysis/d6a09_b_facets.json`; `room-form-B-account.md`, section 14).
  - It is residual: 43 of its 113 defining rooms lie nearer another form's centre, the largest share of any form.
  - B specifies the scripts (P14; F08), the chat (P23; F16, F29), and sparing, terms and the border kept (P07, P08, A05; F08). It restricts the turn from the call to the attack (A15) and stepping away under strain (P32). It holds the elements of collective identity and contention more often than any other form, without changing them (D05, D08).
- **C, The design reopened** (10 units) works through the design. It specifies the call, which returns after each finish (P01), the design (P02; F07, F34), the template kept current (P04; F33), sparing and terms (P07, P08) and help woven into building (P16). It restricts keeping's telling clause, because informed members refuse a change (P05; F07), and it restricts the template settling the design (A11; F07, F33), help from shortage (A13) and decided order (C01).
- **D, Keeping, with help or carrying on** (17 units) changes the most units. It specifies keeping, shared and checked (P05; F27), carrying on as new work begun before the close (P13; F11, F12, F13, F14, F23), help from a helper whose own work is safe (P16; F22), the call that returns from carrying on and loss (P01; F11, F12), the marking weighed (P11; F18), the sub's play administered in its split D.2 (K01; F04), sparing (P07), the border kept where the terms reach (A05) and the host who makes room for canvas talk (P20). It restricts six arrows (A01, A02, A06, A09, A13, A20), the scripts (P14; F24) and hosting (P19).
- **E, The sub's play, run as work** (13 units) specifies the April Fools frame (K01; F01 to F06, F21), the design (P02; F34) and the scripts (P14). Its other ten changes are restrictions, eight of them on arrows (A01, A02, A07, A08, A09, A10, A15, A16), with carrying on (P13; F25) and the chat (P23). Its records hold the play and the reports of the canvas work, and less of the work between them. Its lines often say the record cannot show an arrow's order, and it has the lowest share of restrict lines on arrows that say the arrow fails (43 per cent).
- **F, Moving for the spot** (14 units) works through the spot. It specifies the call after a lost spot (P01), building again after a move (P03; F09), the template that moves with the spot (P04), keeping before the mark exists (P05; F08), the record of failure (P12), the scripts (P14; F08) and the play's limits (K01; F04). It restricts border talk after keeping (A04), scripts under strain (A06), the marking of a finished mark (A07; F09), the move for too few hands (A10), the bare answer (A12), hosting (P19) and choosing the spot before any loss (P27). Its restrict lines on arrows say most often that the arrow fails (63 per cent).

Two patterns run across the forms. First, the four working forms specify where they work: A specifies 7 of its 11 changed units, C 6 of 10, D 9 of 17 and F 7 of 14, while E restricts 10 of its 13. Second, the changes to arrows are nearly all restrictions. Of the 20 arrows in the figure, 16 are restricted in some form and one is specified (A05, by B and D). The order counts of the arrows still hold in most rooms across the population. Where a form restricts an arrow, its lines say one of four things: the arrow fails in the room, the order holds there only under a condition, the second act came first or at the same time, or the record cannot show the order. The sensitivity section gives how many of these cells survive a stricter rule: 20 of the 72.

**One condition across the dimensions.** Read together, the forms show one condition at four places in the model. A placer acts on a form or a term only where it reaches them. Keepers repair a change away until they are told of it or check it (P05, read under D03). A settled border holds for the placers who learn and accept its terms, and for the scripts whose targets are changed (A05, under D04). A script places the old target until its operator changes it (F08). A helper must know the allied picture to help it (F22). The model states the first of these, in P05's telling clause. The check and the terms are proposals of this stage (PR-D6-06, PR-D6-07), unvalidated, and the script's target and the allied picture are notes of branches F08 and F22.

### Which forms kept the work alive

These readings come from the record, by the fields stage A1 wrote for every room (prior.md section 5):
- when the room's coordinating ended (`organizing_end_hour`);
- how much of its talk after hour 73 coordinated rather than recounted (the aftermath share), with the rooms that coordinated after the close counted;
- the room's own last word on its work (`work_remained`: kept, lost or silent), with silence counted as an unknown outcome.

Beside the field is the D5b re-reading for the members in a branch (stood or gone at the close, by a rule logged before the reading). The canvas is not read here (rule 7): its pixels show what stood, not whose work it was, and the forms were not cut from it. The figures are for each form's defining rooms (`_analysis/d6b_survival_forms.json`).

| form | defining rooms | median end (hour) | ended at 73 or later | coordinated after 73 | mean aftermath share | field: kept, lost, silent | kept share | re-read: stood, gone (of rooms in a branch) |
|---|---|---|---|---|---|---|---|---|
| A | 135 | 72.18 | 30 | 29 | 0.018 | 67, 43, 25 | 50 per cent | 33, 9 (of 99) |
| B | 113 | 72.58 | 36 | 35 | 0.028 | 60, 38, 15 | 53 per cent | 28, 4 (of 80) |
| C | 96 | 72.09 | 17 | 16 | 0.016 | 58, 29, 9 | 60 per cent | 25, 3 (of 75) |
| D | 96 | 72.26 | 29 | 29 | 0.017 | 55, 35, 6 | 57 per cent | 28, 13 (of 73) |
| E | 84 | 72.16 | 20 | 20 | 0.016 | 39, 38, 7 | 46 per cent | 18, 11 (of 77) |
| F | 34 | 71.23 | 2 | 2 | 0.008 | 15, 12, 7 | 44 per cent | 7, 1 (of 24) |

Over all 705 rooms the median end is hour 72.02, 146 rooms coordinated after the close, and the field reads kept 347, lost 218 and silent 140 (49 per cent kept).

**To the freeze.** C and D keep most by their own word: 60 and 57 per cent of their defining rooms say the work was kept, against 49 per cent of all rooms. D's split D.2, Keeping inside the sub's play, says kept in 27 of 42 (64 per cent). D's records also say most often what became of the work: 6 of its 96 defining rooms are silent, the fewest of any form, and its re-reading finds the most work gone (13). E keeps least among the large forms: 39 kept against 38 lost. F's defining rooms say kept in 15 of 34, and its other members are silent in 16 of 22.

**After the freeze.** B's defining rooms coordinate after the close more than any other form's (35 of 113), and their mean aftermath share is the highest (0.028). The lead belongs to B's chat and script rooms, not to B as a whole. Of the 35 rooms that coordinated after hour 73, 26 hold the chat or the scripts: that is 26 of the 78 chat or script rooms, 33 per cent. Of the 15 rooms that hold only the raids, 3 did (20 per cent), and of the 20 that hold none of the three facets, 6 did. Across all 705 rooms, 146 did (21 per cent). A and D follow B, with 29 rooms each. F stops before the close: its median end is hour 71.23, and 2 of its 34 defining rooms coordinate after it.

**What in the model separates them.** The forms that keep most and speak most about their outcome change the keeping part of the model. D specifies keeping (P05), help from a helper whose work is safe (P16), carrying on begun before the close (P13) and the call that returns from carrying on (P01). C reopens the design and keeps the template current (P02, P04), and its keepers refuse changes they know of (P05). The rooms that coordinate most after the close are the chat and script rooms of B, which change the chat and the scripts (P23, P14), the means that outlast the canvas. The forms that keep least change other parts. E changes the sub's play, which ends with the day, and its records hold the canvas work thinly. F changes the spot and the move: its rooms lost or were refused a spot, built again, and stopped before the close. The call and the fight do not separate the forms: every form holds attack calls and the contest in talk as the model states them.

These are readings, not tests. The differences in kept share are modest (44 to 60 per cent). The field was right in 25 of 34 rooms when prior.md measured it, and the D5b re-reading agrees with it in 248 of the 476 rooms in a branch. The forms' records differ in length (the median defining room holds 64.5 coded concepts in F and 222 in E), so silence and the end hour partly measure the record. A test that holds record size fixed is owed (below).

### The unadapted group, and the rooms the model could not compose

**The unadapted group is empty.** No room returned `none`: all 705 rooms adapted the model. 229 adapted rooms sit in no branch (A 60, B 54, C 37, D 39, E 11, F 28). They are in the forms, and the forms' lines include them.

**The rooms the model could not compose.** Two counts apply. By the verdicts the forms carry (my last ruling at D3, else the readers' agreed verdict at the first return), one room does not compose and ten cannot be told. The one is r/picturegame (form E, 13 coded concepts). At the first return its record was, in the readers' words, "a subreddit game of SoundGame rounds, picture hints, guesses, correct-marking, Discord invitations, and emoji proposals, not a canvas mark". At the re-check no room failed to compose: both readers found r/picturegame composes with residue, and both could not tell 19 rooms. Those 19 are r/austriahungary, r/azerbaijan, r/azores, r/bannedfromanime_irl, r/bigbang, r/Braveryjerk, r/FlipnoteStudio3D, r/greenland, r/Lugarix, r/nonbinary, r/PokemonSage, r/polyamory, r/ReBoot, r/Redox, r/THE_R, r/TheID, r/wario, r/watchmen and r/yerbamate. What they have in common is a short record, not another way of organizing. Each holds 1 to 8 coded concepts, against a median of 101 over the 705 rooms. Only r/polyamory is a defining member of its form; 15 are silent on what became of their work, and 16 are in no branch. They sit in five forms (A 3, B 3, C 4, D 4, F 5) and in none of E. At D3a-56 I ruled two of them, r/polyamory and r/THE_R, to compose with residue. r/picturegame's first-return record differs in kind: it is the sub's own play, the work that form E runs beside the canvas and that the model holds only as a key (PR-D6-10).

### What the forms show the model lacks: the returns

The model grounds no loop: no room's record runs a whole cycle, and no counted arrow runs back. The forms carry the material for three returns.
- **The call returns** (C, D and F; PR-D6-01). After a finished part, a later canvas, damage, a loss or a move, the room calls for hands again.
- **The move returns to building** (F; F09; PR-D6-04). After a relocation the room recruits, designs and builds again at the new spot.
- **The marking returns to keeping** (A; F32). An announced finish is followed by repair and renewed defence.

The first two are the returns this telling found missing at its first legs. The third is F32's. None is entered in the model. Each would need a return to the rooms and a new validation cycle.

### The held proposals (QD4-001), stated in full

Both were made at D4a-01 and reverted in the same leg (move 203). Neither was served to any room, and neither is re-checked. The model told here holds P05 and A11 as frozen at D3.
- **P05, move 198, history lines 173 to 176, reverted by line 181.** The statement would gain: "This holds where the keepers can learn of a planned change only by being told, and no informed member holds it." The status would be bounded. The bound would read: "It does not hold where the keepers read a planned change from its shape and stop repairing it with no telling: completeanarchy, polska, satania, halo, bangtan, thesilphroad (R-completeanarchy-c187508d7ae3-022, R-polska-dadda7358f9a-049, R-satania-84df196116f3-022, R-halo-b988854ba168-036, R-bangtan-7efe23da0d0c-070, R-thesilphroad-a3f86618e239-018), a candidate branch, 'the shape read' (F-024). It does not hold where informed members hold the change against keepers who do not know: armok, maryland, oneshot (R-armok-8852b2ab85f8-022, R-maryland-d1b6e2d1d5f3-017, R-oneshot-e840e127e9b2-013), a limit below the trigger, at three nodes."
- **A11, move 199, history lines 177 to 180, reverted by line 182.** The arrow from P02 to P04 (a template settles a design argued in a thread) would be withdrawn under rules 14 and 16. Its order between rooms never beat its null (111 of 185 rooms, 0.600, against a null 95th percentile of 0.670). Inside threads, the template came first in 98 rooms against the transition in 111, so the arrow carries no direction. The failure clause stands alone in 117 rooms, 31 of them talk only. And 261 accepted restrict lines say that a template does not settle the design for good. What remains supported, that design talk and layouts meet in threads, is held by P02's and P04's statements. The full text, with its rooms and lines, is in `tree-D4.md` ("The held proposals").

Form C bears on both. Its keepers refuse changes they know of (F-025), a case the held P05 bound does not name, and it restricts A11 in 40 of its 58 lines (Part 1, D02 and D03). Both stay held.

### The proposals of this stage, apart from the telling

Eleven proposals came from the form lines. Each is in `proposals-D6.jsonl` with its evidence and rooms, against the frozen model, with status unvalidated. None enters the model in this run, and E1 reports them.
- PR-D6-01, the call returns (23 rooms).
- PR-D6-02, the answer that asks for a task (4).
- PR-D6-03, a proposal that is itself the call (8).
- PR-D6-04, after the move, the room builds again (9).
- PR-D6-05, the room sizes its design to its hands before any loss (9).
- PR-D6-06, the check before repair (6).
- PR-D6-07, the terms bind the placers they reach (24).
- PR-D6-08, help comes from the hands a helper can spare (21).
- PR-D6-09, border talk before keeping (12).
- PR-D6-10, the play run as work (89). It stays unvalidated and is flagged for E1 against the scope ruling of D3a-55, which put the sub's own business outside the model.
- PR-D6-11, imprinting runs with the work (46).

### What is owed

These items are recorded at D6a-09 on J's rulings.
- **The size-held test.** Done at D6a-10, in the section after the sensitivity section. With each form's rooms matched to rooms of the other forms on record size and, separately, on canvas-work concepts, 62 of the 72 changed cells keep their lean and 10 are size-dependent (A 4, E 3, and one each in B, C and F; none in D).
- **prior.md section 3's element-reach half** moves to E1. Until it is computed, local validation is not established.
- **Defects 100 and 101 stay open**, with no rewrite. The account's survival paragraph rests on the `work_remained` field, and four timings are contradicted by the canvas.
- **The branch-naming rule** is recorded as a dated amendment (`departures.jsonl` line 21), applying backwards. Of the 50 branch lines, 38 stand on the rule as stated and 12 on its widened readings.

### The answer to the theory question

When strangers organize on a clock they did not set, with no way to compel anyone, organizing takes six forms in this record.
- **Four are working forms**, each named by the part of the work its rooms changed: the terms with neighbours (A), the design (C), keeping with help and carrying on (D) and the spot (F).
- **One is a residual grouping (B)** of the rooms whose work ran behind the thread, in three facets held by different rooms: the chat, the scripts and the raids.
- **One is a form whose record is mostly the host sub's April Fools play (E)**, run as work beside the canvas.

The forms differ in their functioning by which part of the shared model they change. None replaces an element, but the coding vocabulary left almost no way to replace one. Where a form restricts an arrow, its rooms' lines often say the arrow fails there. Of the 72 changed cells, 20 survive a stricter rule, and 62 keep their lean when record size is held fixed; form A is the most fragile on both counts.

By the rooms' own word, the forms that kept the work alive to the freeze were the ones that changed keeping (D, with C). After it, the rooms that coordinated most were the chat and script rooms of B, then rooms of A and D. The forms built on the spot (F) and on the play (E) kept least. What separates them in the model is keeping and its returns, not the call or the fight: every form holds the call and the fight as the model states them. These readings rest on the rooms' ruled lines, not on validated local accounts.

## The sensitivity of the form lines to the rule's thresholds

Written at D6a-09 on J's ruling 1b (27 October, 09:27 Berlin) by `_analysis/d6a09_sensitivity.py`, which re-runs the rule of D6a-01 on the same facts files. The rule names a cell changed where an op is held by at least the floor (the larger of 5 and a share of the form's defining rooms) at the ratio threshold or more times the 558 defining rooms' share. Run at the rule's own thresholds (ratio 1.2, floor 10 per cent), the script gives back all 396 written relations. The table counts the changed cells at each setting, all forms first, then by form.

| ratio threshold | changed cells, floor 10 per cent | changed cells, floor 15 per cent |
|---|---|---|
| 1.0 | 99 (A 19, B 12, C 15, D 22, E 16, F 15) | 67 (A 11, B 8, C 9, D 16, E 10, F 13) |
| 1.1 | 82 (A 14, B 7, C 12, D 20, E 14, F 15) | 53 (A 8, B 4, C 6, D 14, E 8, F 13) |
| 1.2 (the rule) | 72 (A 11, B 7, C 10, D 17, E 13, F 14) | 45 (A 5, B 4, C 5, D 12, E 7, F 12) |
| 1.3 | 57 (A 6, B 7, C 6, D 15, E 11, F 12) | 36 (A 3, B 4, C 2, D 11, E 6, F 10) |
| 1.4 | 42 (A 4, B 4, C 3, D 9, E 10, F 12) | 29 (A 2, B 2, C 1, D 8, E 6, F 10) |
| 1.5 | 27 (A 1, B 3, C 2, D 6, E 6, F 9) | 20 (A 0, B 2, C 1, D 6, E 4, F 7) |

Raising either threshold only removes cells: at every setting stricter than the rule, each cell still changed keeps its written relation. Lowering the ratio adds cells the rule leaves untouched (27 more at 1.0 with the 10 per cent floor).

**The cells kept at the stricter rule.** J's ruling names two marks. A changed cell is marked "robust" if it keeps its written relation at ratio 1.5 and floor 15 per cent, and "marginal" otherwise. Of the 72 changed cells, 20 are kept and 52 are marginal. Each cell's mark, holders, ratio and relation at the stricter settings are in `form-cells-sensitivity-D6.tsv`.

- **A, Border terms and the announced plan:** 0 of 11 kept.
- **B, Behind the thread: chat, scripts, raids:** 2 of 7 kept: P14 (specifies), P23 (specifies).
- **C, The design reopened:** 1 of 10 kept: P02 (specifies).
- **D, Keeping, with help or carrying on:** 6 of 17 kept: P01 (specifies), P14 (restricts), P05 (specifies), P20 (specifies), P13 (specifies), A09 (restricts).
- **E, The sub's play, run as work:** 4 of 13 kept: A01 (restricts), K01 (specifies), A07 (restricts), A15 (restricts).
- **F, Moving for the spot:** 7 of 14 kept: P01 (specifies), P03 (specifies), P04 (specifies), A06 (restricts), P19 (restricts), A04 (restricts), A07 (restricts).

Most single cells do not survive the stricter rule, though D, E and F keep their central changes: D its keeping and carrying on (P05, P13), E the play run as work (K01), F building again after a move and border talk before keeping (P03, A04). B keeps its scripts and its chat (P14, P23), and C keeps the design (P02). A keeps none of its changes at ratio 1.5 and floor 15 per cent, and 1 of 11 at ratio 1.5 with the 10 per cent floor, so A's telling (terms, plans and their reach) rests on cells that do not survive a stricter rule. A cell marked marginal is a lean of the form at the rule's thresholds, not a finding that survives a change of rule.

## The size-held test

Written at D6a-10 on J's word (27 October, 09:27 Berlin) by `_analysis/d6a10_size_test.py`; each cell's result is in `form-cells-size-D6.tsv`. The test asks whether a form's lean on a unit survives when the form's rooms are compared with rooms of the same record size, rather than with all 558 defining rooms. The rule was logged in the diary before the script ran:
- each of a form's defining rooms is matched, with replacement, to the 5 defining rooms of the other five forms nearest to it in size (by the logarithm of the count), ties broken by room name;
- two measures are run separately: record size (coded concepts) and canvas-work concepts (concepts whose theme sits under Critical mass, Coordination without command, Maintenance or Order without law);
- an op survives where the form's share of rooms holding it is 1.2 times the matched rooms' share or more (the rule's own ratio), and a cell survives where one of its deciding ops survives both matchings; a cell that fails either is size-dependent.

**The result.** 62 of the 72 changed cells survive both matchings; 10 are size-dependent. None of the 20 cells the sensitivity section keeps at ratio 1.5 and floor 15 per cent is size-dependent.

- **A, Border terms and the announced plan** (median record 99 coded concepts, 79 of them canvas work): 7 of 11 cells survive. Size-dependent: C01 (restricts; size-held ratio on canvas-work concepts 1.18); P23 (specifies; size-held ratio on canvas-work concepts 0.93); P07 (specifies; size-held ratio on record size 1.07 and canvas-work concepts 0.98); P12 (specifies; size-held ratio on record size 1.18). Matching on record size raises the ratio above the unmatched comparison with the other forms in 7 of the 11 cells.
- **F, Moving for the spot** (median record 64.5 coded concepts, 50 of them canvas work): 13 of 14 cells survive. Size-dependent: A12 (restricts; size-held ratio on record size 1.16). Matching on record size raises the ratio above the unmatched comparison with the other forms in 10 of the 14 cells.
- **B, Behind the thread: chat, scripts, raids** (median record 131 coded concepts, 91 of them canvas work): 6 of 7 cells survive. Size-dependent: A05 (specifies; size-held ratio on canvas-work concepts 1.14). Matching on record size raises the ratio above the unmatched comparison with the other forms in 3 of the 7 cells.
- **C, The design reopened** (median record 119.5 coded concepts, 90.5 of them canvas work): 9 of 10 cells survive. Size-dependent: P04 (specifies; size-held ratio on canvas-work concepts 1.18). Matching on record size raises the ratio above the unmatched comparison with the other forms in 7 of the 10 cells.
- **D, Keeping, with help or carrying on** (median record 142 coded concepts, 92 of them canvas work): 17 of 17 cells survive. Matching on record size raises the ratio above the unmatched comparison with the other forms in 11 of the 17 cells.
- **E, The sub's play, run as work** (median record 222 coded concepts, 75.5 of them canvas work): 10 of 13 cells survive. Size-dependent: A02 (restricts; size-held ratio on canvas-work concepts 1.12); A10 (restricts; size-held ratio on record size 1.16); A09 (restricts; size-held ratio on record size 0.96). Matching on record size raises the ratio above the unmatched comparison with the other forms in 3 of the 13 cells.

**How firm the marks are.** With 3 or 10 matches instead of 5, 12 cells change outcome at one setting or the other: A02 in D, A02 in E, C01 in A, P04 in C, A01 in D, P23 in E, P05 in C, P08 in B, A05 in B, A13 in C, A10 in E, P12 in A. At 5 matches their deciding ratios (the lower of the two matchings) lie between 1.12 and 1.27, close to the 1.2 line. The mark follows the logged rule (5 matches).

**What it means.** The forms' leans are not, in the main, an effect of record size. A and F were the forms whose scores might rest on size: F's rooms have the shortest records and A's the next shortest. F keeps 13 of its 14 changes, and in 10 of them matching on record size raises the ratio: F's rooms change these units more often than other rooms whose records are as short. A keeps 7 of its 11, and none at the stricter thresholds, so A's telling is the most fragile of the six. E, whose records hold the play and less canvas work, keeps 7 of its 8 restrictions on arrows when matched on canvas-work concepts, so those restrictions are not only an effect of a thin record of canvas work. The size-dependent cells are named above and marked in `form-cells-sensitivity-D6.tsv` (column `size_mark`).
