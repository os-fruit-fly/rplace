# Room forms, D4a-08c: six forms, with the core placed

Leg D4a-08, still open, 26 October 2026. J, through the handler (22:00 Berlin): "I think this is good but I would rather have fewer clusters. Also I don't get why the core is still alone. Can we try to have some 4 or 6? If not then it is fine but it is a lot for a short technical appendix. Also 31, 21, 49 is quite small." This file answers on the D4a-08b weighting: the changes weigh two thirds, the codes one third. It sits beside `room-forms-D4a05.*` to `room-forms-D4a08b.*`, which are unchanged. Files: `room-forms-D4a08c.jsonl` (the six forms, with members), `room-forms-D4a08c.tsv` (every room at six, four and eight forms), and this file. The computation is `_analysis/d4a08c_room_forms.py`; its rule was logged before it ran.

**My answer:** six forms. Section 4 gives the reasons and what is lost.

## 1. The core, placed by its codes

The 21 rooms were kept apart only because the first brief said so. None of them holds a selected change: their change profile is 0, the global model. Each is now placed in the form whose centre its code part lies nearest. I used the code part alone, because a zero change part would favour whichever form's change centre lies nearest 0. The table also gives the placement with the full distance, which differs for some rooms.

| core room | coded concepts | at eight forms | at six | at four | at six, full distance with a zero change part |
|---|---|---|---|---|---|
| r/startrek | 137 | D | E | D | E |
| r/n64 | 22 | D | E | D | E |
| r/pgang | 8 | F | B | A | B |
| r/quq | 8 | C | B | A | B |
| r/GreenEmpire | 7 | G | F | C | F |
| r/bannedfromanime_irl | 6 | H | D | C | D |
| r/mcgillrobotics | 6 | F | D | C | D |
| r/signal | 6 | F | A | B | A |
| r/Lugarix | 5 | F | A | B | B |
| r/sakartvelo | 5 | H | B | A | B |
| r/NovaScotia | 4 | A | C | A | C |
| r/Redox | 4 | G | F | C | D |
| r/greenland | 3 | A | C | A | C |
| r/churchofhelix | 2 | B | D | C | D |
| r/PokemonSage | 2 | E | F | B | B |
| r/TheID | 2 | G | F | C | D |
| r/UMiami | 2 | H | B | A | B |
| r/UNLincoln | 2 | G | F | C | D |
| r/nonbinary | 1 | G | F | C | D |
| r/wario | 1 | H | B | A | B |
| r/yerbamate | 1 | F | A | B | D |

- **r/startrek** goes to the sub's April Fools play at every count. So does r/n64.
- **The other 19 rooms spread across the forms.** They hold 1 to 8 coded concepts each, so their placement rests on a handful of codes and is weak.
- At six forms the core adds 2 to 6 rooms to each form, 6 of them to the spot.

## 2. How the forms merge

The cuts nest, so each smaller count joins forms of the larger.

| k | gap (lifetime of the cut) | size ratio, largest to smallest |
|---|---|---|
| 4 | 0.3922 | 2.67 |
| 5 | 0.0213 | 4.70 |
| 6 | 0.1780 | 2.96 |
| 7 | 0.2715 | 2.49 |
| 8 | 0.0577 | 3.51 |

- **Eight to seven:** raiding (H) joins the work behind the thread, the chat and the scripts (C).
- **Seven to six:** the plan made and announced (F) joins the terms between neighbours (E).
- **Six to five:** the work behind the thread, with raiding, joins the design.
- **Five to four:** the spot joins keeping.

The gap, the length of time a cut lasts as the joining goes on, is longest at four (0.392). It is next longest at seven (0.272), and six comes third (0.178). The eight forms, for reference, with the core placed:

| form | the pattern | rooms (thin, core) |
|---|---|---|
| A | the design and its marking | 123 (25, 2) |
| B | keeping, with traded help and carrying on | 113 (16, 1) |
| C | the work behind the thread: the chat and the scripts | 103 (14, 1) |
| D | the sub's April Fools play | 98 (12, 2) |
| E | the terms between neighbours | 97 (22, 1) |
| F | the plan made and announced | 82 (16, 5) |
| G | the spot: lost, chosen or yielded, and building again | 54 (15, 5) |
| H | raiding as the work | 35 (6, 4) |

## 3. Six forms and four forms

**At six:**

| form | the pattern | joins the eight | rooms (thin, core) | change signature (times the population; members holding it) | codes most above the average room | median coded concepts | raiding-heavy rooms | takeover rooms | a differing account? |
|---|---|---|---|---|---|---|---|---|---|
| A | the terms between neighbours, with the plan announced | E (the terms between neighbours), F (the plan made and announced) | 166 (28, 3) | Negotiated order (1.8; 87%); Completion ritual (1.6; 51%); Standardization of output (2.1; 37%) | Negotiated order (0.176 against 0.093); Repair work (0.125 against 0.095); Standardization of output (0.048 against 0.028) | 91.5 | 5 | 0 | In part. Negotiated order in 87 per cent of the defining members: the changes limit A04 and A05 (talk with neighbours can come before keeping; sparing holds where an agreement is known and accepted). The plan made and announced is folded in and loses its own account. |
| B | the work behind the thread: the chat, the scripts and raiding | C (the work behind the thread: the chat and the scripts), H (raiding as the work) | 141 (23, 5) | Workarounds (2.1; 43%); Backstage decision-making (2.3; 42%); Repertoire of contention (2.4; 35%) | Repertoire of contention (0.064 against 0.031); Workarounds (0.053 against 0.022); Live and let live (0.040 against 0.024) | 109 | 12 | 0 | No single account: its three signatures are each held by under half its members (workarounds 43, backstage decision-making 42, attack calls 35 per cent). Scripts (A06 limited) and raiding could each carry one; together they do not. It holds 12 of the 21 raiding-heavy rooms. |
| C | the design and its marking | A (the design and its marking) | 125 (27, 2) | Collective representation (2.6; 98%) | Collective representation (0.198 against 0.117); Repair work (0.108 against 0.095); Negotiated order (0.101 against 0.093) | 97 | 0 | 0 | In part. Collective representation in 98 per cent: the design is argued and sized, and a template does not settle it (A11, the held proposal). |
| D | keeping, with traded help and carrying on | B (keeping, with traded help and carrying on) | 119 (20, 3) | Repair work (1.8; 74%); Transition (2.2; 41%); Reciprocity (2.5; 38%) | Repair work (0.143 against 0.095); Reciprocity (0.060 against 0.035); Transition (0.025 against 0.012) | 113 | 1 | 7 | In part. Repair work in 74 per cent: keeping gains conditions the model lacks (coverage, handoffs, sleep). |
| E | the sub's April Fools play | D (the sub's April Fools play) | 98 (12, 2) | Keying (3.8; 71%); Collective memory (1.7; 40%); Direct information sharing (2.8; 37%) | Keying (0.485 against 0.120); Direct information sharing (0.050 against 0.033); Visibility returns (0.013 against 0.013) | 215 | 3 | 26 | Yes, for the frame, which sits beside the canvas work: the sub's play gains steps the model holds only as a key. 26 of the 33 takeover rooms are here. |
| F | the spot: lost, chosen or yielded, and building again | G (the spot: lost, chosen or yielded, and building again) | 56 (16, 6) | Territoriality (5.4; 94%); Mobilization (1.7; 44%); Repair work > Negotiated order (1.6; 41%) | Territoriality (0.209 against 0.051); Mobilization (0.083 against 0.059); Direct information sharing (0.053 against 0.033) | 45.5 | 0 | 0 | Yes. Territoriality in 94 per cent: the move follows a loss or a neighbour's advance more than a judgement of too few hands (A10 limited), and the room builds again at the new spot, a return the model lacks. |

**At four:**

| form | the pattern | joins the eight | rooms (thin, core) | change signature (times the population; members holding it) | codes most above the average room | median coded concepts | raiding-heavy rooms | takeover rooms | a differing account? |
|---|---|---|---|---|---|---|---|---|---|
| A | making the mark: the design, with the work behind the thread and raiding | A (the design and its marking), C (the work behind the thread: the chat and the scripts), H (raiding as the work) | 262 (46, 7) | Collective representation (1.6; 73%) | Collective representation (0.151 against 0.117); Workarounds (0.037 against 0.022); Repertoire of contention (0.044 against 0.031) | 101 | 12 | 0 | In part, for the design only (collective representation in 73 per cent). The chat, the scripts and raiding are folded in and lose their accounts. |
| B | the terms between neighbours, with the plan announced | E (the terms between neighbours), F (the plan made and announced) | 170 (31, 4) | Negotiated order (1.8; 87%); Completion ritual (1.6; 51%); Standardization of output (2.1; 37%) | Negotiated order (0.176 against 0.093); Repair work (0.125 against 0.095); Standardization of output (0.048 against 0.028) | 91 | 5 | 0 | In part, as at six forms. |
| C | holding ground: keeping, or moving and building again | B (keeping, with traded help and carrying on), G (the spot: lost, chosen or yielded, and building again) | 175 (37, 8) | Territoriality (2.0; 44%); Reciprocity (2.0; 34%); Transition (1.9; 34%) | Territoriality (0.083 against 0.051); Repair work (0.118 against 0.095); Reciprocity (0.053 against 0.035) | 84 | 1 | 7 | In part, and only as a pair. Its signatures are weak (territoriality 44, traded help 34, carrying on 34 per cent). Keeping and moving are the model's two answers to losing ground, and the return from the move to building is the part the model lacks. But the spot no longer has an account of its own. |
| D | the sub's April Fools play | D (the sub's April Fools play) | 98 (12, 2) | Keying (3.8; 71%); Collective memory (1.7; 40%); Direct information sharing (2.8; 37%) | Keying (0.485 against 0.120); Direct information sharing (0.050 against 0.033); Visibility returns (0.013 against 0.013) | 215 | 3 | 26 | Yes, for the frame, as at six forms. |

**Where the small forms go.** Raiding (35 rooms with the core placed) is gone by six: it sits inside the work behind the thread, which holds 12 of the 21 raiding-heavy rooms. The spot (56 at six) stays a form at six and joins keeping at four. The core no longer stands alone at any count.

## 4. Which I would stand behind for a short technical appendix

**Six.** At six, every form I was sure of at eight still stands on its own: the terms between neighbours, the design and its marking, keeping, and the spot. The April Fools play is its own form, the frame beside the canvas work. The pieces I was not sure of are joined into one form and named for what it is, a mixture: the chat, the scripts and raiding, the work behind the thread. Its three signatures are each held by under half its members, so I would not write one account for it. The largest form is 2.96 times the smallest, within J's bound of 3. The smallest form, the spot, has 56 rooms, and the narrow form F09, moving and building again, lives there.

**What is lost going down from eight to six:**
- Raiding as a form of its own. It remains a pattern inside the work behind the thread.
- The plan made and announced, which I was not sure of. It folds into the terms between neighbours.

**Why not four.** Four is the clearest split by the gap. It has no small forms, and it reads as four broad orientations: making the mark, the terms with neighbours, holding ground, and the April Fools play. But two of the four lose what made them forms. The design absorbs the chat, the scripts and raiding, and its signature falls from 98 to 73 per cent. Keeping and the spot join into "holding ground", whose signatures are each held by under half its members. The spot is the form with the clearest account that differs from the model (the move followed by building again), and at four it no longer has an account of its own. I would use four only as a one-line summary of the six, not as the forms.

**What I am still not sure of at six.** The work behind the thread is a mixture, and I would split it at the level below. The forms remain poles of a continuum. The real stability of the cut is low (about 0.21 at every count), and many rooms lie between forms.

## 5. The room table

One row per room, at six, four and eight forms (also in `room-forms-D4a08c.tsv`). Core rooms are marked.

| room | six forms | four forms | eight forms | primary branch |
|---|---|---|---|---|
| 2007scape | A | B | E |  |
| 49ers | C | A | A | F10 |
| 4chan | E | D | D | F01 |
| aceattorney | C | A | A |  |
| acecombat | E | D | D | F02 |
| AceOfAngels8 | E | D | D |  |
| AcePlace | A | B | F | F17 |
| achievement_hunter | F | C | G |  |
| adventuretime | A | B | E | F09 |
| aeon | B | A | C | F19 |
| aeskwadraat | C | A | A | F12 |
| afip | B | A | C | F19 |
| aggies | C | A | A |  |
| ainbowroad | A | B | E |  |
| albania | B | A | A |  |
| alberta | B | A | H |  |
| AMD | C | A | A | F01 |
| AmericanFlaginPlace | B | A | C | F08 |
| anaheimducks | C | A | A | F14 |
| anarchism | B | A | H |  |
| anarcho_capitalism | D | C | B |  |
| anarchocapitalism | D | C | B |  |
| androidgaming | D | C | B |  |
| animalcrossing | A | B | F | F09 |
| anime | A | B | F | F19 |
| anime_irl | E | D | D | F01 |
| aoe2 | C | A | A | F34 |
| apocalypserising | E | D | D |  |
| AprilKnights | B | A | C | F16 |
| araragi | C | A | A |  |
| archlinux | B | A | C | F07 |
| argentina | B | A | C |  |
| armenia | B | A | C |  |
| armok | B | A | C | F27 |
| aromantic | B | A | C |  |
| asexual | B | A | H |  |
| asexuality | A | B | E | F17 |
| asktransgender | D | C | B |  |
| auburn | A | B | E |  |
| australia | C | A | A | F07 |
| austria | B | A | H |  |
| austriahungary | C | A | A |  |
| AvoArmy | C | A | A | F07 |
| AyyMD | B | A | C | F07 |
| azerbaijan | D | C | F | F19 |
| azores | B | A | F |  |
| babymetal | D | C | B | F22 |
| bahrain | E | D | D | F01 |
| bakchodi | B | A | H | F08 |
| bangladesh | B | A | C |  |
| bangtan | D | C | B | F17 |
| bannedfromanime_irl (core) | D | C | H |  |
| bardmains | C | A | A | F07 |
| batman | A | B | E |  |
| battlecats | E | D | D | F02 |
| baylor | E | D | D | F33 |
| bdsm | C | A | A |  |
| bees | B | A | H |  |
| belgium | B | A | H | F24 |
| berkeley | F | A | G | F09 |
| berserk | A | B | F | F09 |
| bigbang | C | A | A |  |
| bih | D | C | B |  |
| bindingofisaac | D | C | B | F01 |
| bisexual | C | A | A | F07 |
| bitcoin | C | A | A |  |
| blackmirror | C | A | A |  |
| bobross | D | C | B |  |
| borderlands | D | C | B | F27 |
| borussiadortmund | E | D | D | F21 |
| bostonbruins | A | B | F | F32 |
| bostonceltics | D | C | B | F04 |
| brasil | B | A | C |  |
| Bravenewbies | B | A | C |  |
| Braveryjerk | B | A | H |  |
| bretagne | C | A | A |  |
| btc | E | D | D | F28 |
| buffalo | D | C | B | F12 |
| buffalobills | A | B | E | F10 |
| buffalowizards | D | C | B | F09 |
| bulgaria | C | A | A |  |
| calgaryflames | D | C | B | F09 |
| calvinandhobbes | C | A | A | F07 |
| canada | D | C | B | F01 |
| canucks | B | A | H | F01 |
| cardinals | B | A | C |  |
| carletonu | A | B | F |  |
| catalonia | B | A | C | F08 |
| catalunya | A | B | E | F07 |
| catholicism | D | C | B | F23 |
| cavestory | A | B | E | F10 |
| CelticFc | A | B | E | F28 |
| cfb | E | D | D | F02 |
| cgpgrey | D | C | B | F14 |
| chelseafc | D | C | B | F04 |
| chess | E | D | D | F33 |
| chibears | B | A | C | F09 |
| chicago | C | A | A | F07 |
| chicubs | D | C | B |  |
| chile | B | A | C | F21 |
| ChronoTrigger | A | B | E | F12 |
| churchofhelix (core) | D | C | B |  |
| cirkeltrek | A | B | F |  |
| CKCrusaders | C | A | A |  |
| Clannad | C | A | A |  |
| clashroyale | E | D | D | F35 |
| clg | A | B | F | F32 |
| cloud9 | B | A | C | F12 |
| clubpenguin | F | C | G | F12 |
| cmu | F | C | G |  |
| coldplay | C | A | A | F07 |
| colombia | C | A | A | F22 |
| colorado | C | A | F | F15 |
| columbia | D | C | B | F15 |
| completeanarchy | D | C | B |  |
| compsoc | A | C | F |  |
| Cornwall | A | B | E |  |
| corridor | F | C | G | F25 |
| COSI | F | B | G |  |
| costa_rica | D | C | B |  |
| counting | B | C | C |  |
| cowchop | A | B | F | F24 |
| criticalrole | C | A | A | F01 |
| croatia | A | B | E | F07 |
| crusaderkings | C | A | A | F08 |
| CryptoFR | D | C | F |  |
| crystalclear | C | A | A | F34 |
| CSUFoCo | C | A | A | F33 |
| cubers | C | A | A | F12 |
| cuboulder | B | C | C |  |
| czech | B | A | C | F07 |
| daftpunk | C | A | A |  |
| dallasstars | F | C | G | F01 |
| danganronpa | D | C | B | F02 |
| dankmemes | E | D | D | F01 |
| darksouls | B | A | C | F16 |
| DatBoi | B | A | H |  |
| davidbowie | C | A | F | F15 |
| day9 | F | B | G | F09 |
| dbz | F | C | G | F01 |
| DCFU | A | B | F | F22 |
| de | A | B | F | F16 |
| denmark | D | C | B | F11 |
| denverbroncos | D | C | B | F03 |
| destiny | B | A | H | F22 |
| DestinyTheGame | E | D | D | F02 |
| detroitlions | E | D | D | F34 |
| detroitredwings | A | B | E |  |
| DevonUK | A | B | E |  |
| diablo | F | C | G |  |
| DiamondClub | D | C | F |  |
| dmt | D | C | B |  |
| dofus | C | A | A |  |
| Dominican | B | A | C |  |
| donaldglover | D | C | B | F11 |
| Dorset | A | B | E |  |
| dota2 | E | D | D | F05 |
| dragonquest | C | A | A | F33 |
| drawhelix | A | B | E | F10 |
| drugs | C | A | A |  |
| drumcorps | E | D | D | F01 |
| duckgame | B | A | C |  |
| ducks | F | C | G |  |
| Dustforce | A | B | E | F09 |
| dwarffortress | B | A | C | F16 |
| eagles | D | C | B |  |
| earthbound | C | A | A | F10 |
| edboxes | A | B | F | F07 |
| eder | C | A | A | F20 |
| edmontonoilers | D | C | B |  |
| eesti | F | C | G | F08 |
| egypt | C | A | A | F22 |
| ElderScrolls | D | C | B | F01 |
| elitedangerous | E | D | D | F04 |
| ElSalvador | D | C | B |  |
| empiredidnothingwrong | A | B | F | F27 |
| england | B | A | H |  |
| enterthegungeon | D | C | B | F23 |
| epublica | A | B | E | F24 |
| EraseThePlace | B | A | C | F29 |
| esperanto | C | A | A | F12 |
| ethereum | E | D | D | F01 |
| ethoslab | F | C | G | F01 |
| europe | D | C | B |  |
| eve | C | A | A | F07 |
| evedreddit | A | B | E |  |
| evex | B | A | C | F08 |
| factorio | C | A | A | F07 |
| faeria | A | B | F | F18 |
| falcons | B | A | H | F01 |
| farmcarrots | C | A | A | F07 |
| FaroeIslands | B | A | C | F09 |
| FederationPlace | B | A | C | F08 |
| feedthebeast | E | D | D | F14 |
| Fez | D | C | B | F21 |
| FinalFantasy | D | C | B |  |
| finland | A | B | E |  |
| fireemblem | A | B | E |  |
| fivenightsatfreddys | E | D | D | F01 |
| FlaggyFlag | C | A | A | F07 |
| flashtv | E | D | D | F02 |
| FlipnoteStudio3D | F | C | G |  |
| floridagators | B | A | C |  |
| FloydVsVoid | A | B | F | F15 |
| flyers | D | C | B | F18 |
| formula1 | E | D | D | F02 |
| forsen | A | B | F | F12 |
| foxes | A | B | F | F31 |
| foxstevenson | F | C | G |  |
| france | B | A | C |  |
| frankocean | D | C | B | F27 |
| frc | D | C | B | F24 |
| freedomplanet | B | A | C | F19 |
| ftlgame | A | B | F | F18 |
| fullcommunism | B | A | C | F17 |
| funhaus | A | B | E | F30 |
| furry | A | B | F | F26 |
| furry_irl | D | C | B | F05 |
| futanari | A | B | F |  |
| futurama | D | C | B | F23 |
| fxKorea | C | A | A | F18 |
| GabrielDropout | C | A | A |  |
| gameattack | D | C | B | F21 |
| gameboy | F | C | G |  |
| gameofthrones | D | C | B | F02 |
| gamindustri | D | C | B | F12 |
| gatech | C | A | A | F08 |
| genderfluid | D | C | B |  |
| geometrydash | E | D | D | F01 |
| germany | A | B | E |  |
| ghibli | A | B | F | F15 |
| giantbomb | A | B | E |  |
| giivasunner | D | C | B | F09 |
| glasgow | D | C | B |  |
| globaloffensive | E | D | D | F13 |
| Goodboye | A | B | E |  |
| gorillaz | D | C | B | F25 |
| GranColombia | B | A | C | F16 |
| gratefuldead | F | C | G |  |
| gravityfalls | A | B | E | F12 |
| greece | D | C | B | F27 |
| greenbaypackers | E | D | D |  |
| GreenCorner | B | A | C |  |
| GreenEmpire (core) | F | C | G |  |
| greenland (core) | C | A | A |  |
| greenlattice | A | B | E | F12 |
| greyblob | D | C | B | F12 |
| GrowTheTree | C | B | A |  |
| GuardiansOfDatBoi | B | A | H | F15 |
| guatemala | C | A | A |  |
| GuildWars2 | E | D | D | F01 |
| h3h3productions | C | A | A | F21 |
| habs | E | D | D | F32 |
| halo | A | B | E |  |
| harrypotter | C | A | A | F01 |
| haskell | F | A | G |  |
| hatsune | A | B | E | F20 |
| hawks | D | C | B | F22 |
| hearthstone | E | D | D | F10 |
| hellointernet | A | B | E | F27 |
| hentai | C | A | A | F07 |
| heroesofthestorm | D | C | B | F01 |
| heyyea | A | B | F | F11 |
| homelab | E | D | D |  |
| HomestarRunner | B | A | H |  |
| homestuck | D | C | B | F35 |
| Homura | B | A | C |  |
| Honduras | C | A | A |  |
| hongkong | C | A | A | F07 |
| hoodr | F | B | G |  |
| hsv | A | B | F |  |
| httyd | F | C | G | F32 |
| hungary | A | B | E | F23 |
| hunterxhunter | E | D | D | F03 |
| hyperlightdrifter | B | A | C | F07 |
| iastate | D | C | B |  |
| ibo | D | C | B |  |
| ice_poseidon | D | C | B | F21 |
| iceland | A | B | E |  |
| ik_ihe | B | A | C | F16 |
| india | B | A | H | F08 |
| indieheads | B | A | C | F01 |
| indonesia | A | B | E | F25 |
| ireland | A | B | E |  |
| israel | A | B | E | F07 |
| italy | D | C | B | F12 |
| Jamaica | A | B | F | F15 |
| japan | A | B | F | F15 |
| jerma985 | A | B | F | F09 |
| k_on | A | B | F |  |
| kamenrider | A | B | F | F15 |
| kanye | B | A | C | F06 |
| katawashoujo | C | A | A | F07 |
| kcroyals | A | B | E | F18 |
| kerbalspaceprogram | E | D | D | F01 |
| kilian | A | B | E | F16 |
| kindafunny | C | A | A | F34 |
| kingdomhearts | E | D | D | F09 |
| kirby | D | C | B | F18 |
| konosuba | C | A | A | F33 |
| korea | C | A | A | F07 |
| kpop | D | C | B | F01 |
| KState | F | C | G | F08 |
| kurdistan | A | B | E | F10 |
| kuwait | C | A | A | F33 |
| lakers | A | B | F | F16 |
| landry | A | B | E |  |
| latin | F | C | G |  |
| latvia | B | A | C |  |
| leafs | C | A | A |  |
| leagueoflegends | E | D | D |  |
| lebanon | B | A | C | F35 |
| lego | E | D | D | F13 |
| lexington | F | C | G |  |
| lifeisstrange | A | B | E | F26 |
| linux | B | A | C | F10 |
| liquicity | B | A | C | F15 |
| lithuania | B | A | C | F16 |
| littlebusters | B | A | F |  |
| littlewitchacademia | A | B | F | F10 |
| livecounting | B | A | C | F08 |
| liverpoolfc | E | D | D | F29 |
| lofihiphop | B | A | C | F15 |
| loliconsunite | A | B | E | F23 |
| loltyler1 | B | A | H | F08 |
| lost | D | C | B |  |
| lovelive | D | C | B | F13 |
| lsu | A | B | E | F09 |
| luciomains | A | B | F | F19 |
| Lugarix (core) | A | B | F |  |
| luxembourg | B | A | H | F32 |
| Madeon | E | D | D |  |
| madokamagica | B | A | C |  |
| magictcg | D | C | B | F01 |
| malaysia | A | B | E | F09 |
| malta | C | A | A |  |
| mamamoo | A | B | F | F35 |
| ManningPlace | A | B | E | F26 |
| Mario | D | C | B | F12 |
| mariokart | E | D | D | F03 |
| marvel | E | D | D | F34 |
| maryland | C | A | A | F22 |
| masseffect | B | A | C | F09 |
| math | D | C | B |  |
| mcgill | E | D | D | F16 |
| mcgillrobotics (core) | D | C | F |  |
| mechanicalkeyboards | E | D | D | F26 |
| megaman | B | A | C | F07 |
| metalcore | D | C | B | F27 |
| metalgearsolid | C | A | A | F01 |
| metroid | C | A | A | F26 |
| mexico | B | A | C | F08 |
| miamidolphins | C | A | A | F26 |
| MiamiHurricanes | A | B | E |  |
| mindcrack | A | B | E | F24 |
| minecraft | E | D | D | F01 |
| minnesotavikings | B | A | C | F08 |
| miraculousladybug | F | C | G | F05 |
| mit | C | A | A | F10 |
| mizzou | D | C | B |  |
| mls | E | D | D | F06 |
| MMA | E | D | D | F01 |
| monalisaclan | A | B | F | F15 |
| monero | B | A | C | F16 |
| MonkeyIsland | A | B | F | F15 |
| monstercat | E | D | D | F01 |
| monsterhunter | A | B | E |  |
| montenegro | C | A | A | F16 |
| Moondye7 | A | B | F | F19 |
| mordhau | A | C | E |  |
| morrowind | A | B | E | F07 |
| msu | B | A | C | F09 |
| muse | C | A | A | F07 |
| mylittlepony | D | C | B | F16 |
| mysterydungeon | A | B | F |  |
| n64 (core) | E | D | D |  |
| naruto | D | C | B | F02 |
| nascar | E | D | D | F10 |
| natsume | D | A | B |  |
| nbaspurs | F | C | G | F01 |
| necrodancer | A | B | F | F09 |
| neopets | A | B | E | F29 |
| nerf | B | A | C | F15 |
| neu | B | A | C | F08 |
| neutralmilkhotel | A | B | E |  |
| NewMexico | C | A | A | F10 |
| newzealand | C | A | A | F07 |
| NieR | D | C | B | F05 |
| nightinthewoods | D | C | B | F01 |
| nin | C | A | A | F18 |
| nintendo | E | D | D | F01 |
| nlsscirclejerk | D | C | B | F34 |
| nonbinary (core) | F | C | G |  |
| norge | B | A | C |  |
| Northwestern | F | C | G |  |
| norway | A | B | E |  |
| notredame | C | A | A | F07 |
| NovaScotia (core) | C | A | A |  |
| npr | A | B | F |  |
| nuclearthrone | D | C | B | F33 |
| nVade | A | B | E |  |
| nyjets | D | C | B | F02 |
| nyu | F | C | G |  |
| ockytop | B | A | C | F15 |
| ohio | B | A | C | F10 |
| Okami | A | B | F | F19 |
| OKState | B | A | C | F08 |
| oltp | D | C | B |  |
| oman | D | C | B |  |
| OnePiece | D | C | B | F22 |
| oneplus | E | D | D | F01 |
| onepunchman | A | B | E | F10 |
| oneshot | A | B | E |  |
| OneTrueEmilia | D | C | B | F21 |
| ontario | E | D | D | F01 |
| opticgaming | A | B | F | F19 |
| orderofthebluecorner | A | B | E |  |
| OrderOfTheKoi | B | A | C | F16 |
| osu | E | D | D | F07 |
| osugame | A | B | E | F29 |
| overwatch | C | A | A |  |
| pakistan | B | A | H | F08 |
| paladins | E | D | D | F01 |
| palestine | C | A | A | F34 |
| pansexual | A | B | E |  |
| parabola | A | B | F |  |
| paragon | E | D | D | F01 |
| parahumans | B | A | C | F25 |
| paranatural | A | B | E |  |
| parrots | D | C | B | F13 |
| partyparrot | D | C | B |  |
| pathofexile | B | A | C |  |
| patriots | D | C | B | F21 |
| paydaytheheist | E | D | D | F32 |
| pcmasterrace | E | D | D | F25 |
| pebble | F | C | G | F09 |
| penguins | F | C | G | F09 |
| pepe | D | C | B | F08 |
| Peru | A | B | F | F30 |
| peterdraws | A | B | E |  |
| pgang (core) | B | A | F |  |
| philippines | A | B | F | F15 |
| phish | F | C | G | F01 |
| physical_removal | D | C | B | F23 |
| picturegame | E | D | D | F25 |
| Pigifs | B | C | H |  |
| PinkUnion | A | B | E |  |
| PinkVomitMonster | B | A | C |  |
| pitt | C | A | A | F14 |
| placecanada | B | A | C |  |
| placeDE | C | A | A | F23 |
| placehearts | A | B | E |  |
| placehfarts | B | A | H |  |
| PlaceNL | B | A | H | F08 |
| placeportalpattern | A | B | E | F23 |
| placesnek | B | A | C |  |
| placestart | B | A | C | F15 |
| placetardis | A | B | F | F10 |
| planetside | F | C | G | F03 |
| pokemon | E | D | D | F27 |
| PokemonSage (core) | F | B | E |  |
| poland | A | B | E | F10 |
| polandball | E | D | D | F02 |
| polska | B | A | C | F12 |
| polyamory | D | C | B | F35 |
| popheads | E | D | D | F01 |
| portal | F | C | G | F33 |
| porterrobinson | D | C | B | F07 |
| portugal | D | C | B | F13 |
| PORTUGALCARALHO | C | A | A | F34 |
| predators | F | C | G | F08 |
| prequelmemes | A | B | F | F13 |
| Produce101 | F | C | G |  |
| ProfessorLayton | C | A | A |  |
| PUBATTLEGROUNDS | C | A | A | F03 |
| purdue | D | C | B | F08 |
| purplecorner | B | A | C | F23 |
| PurplePixels | B | A | C | F16 |
| pusheen | C | A | A | F07 |
| puzzleanddragons | C | A | A | F07 |
| python | E | D | D | F08 |
| qotsa | F | C | G |  |
| quebec | B | A | C | F28 |
| quq (core) | B | A | C |  |
| radiohead | D | C | B | F27 |
| Rainbow6 | E | D | D | F01 |
| rainbowgrid | A | B | E |  |
| rangers | C | A | A | F29 |
| raocow | A | B | F | F35 |
| ravens | A | B | F | F15 |
| re_zero | C | A | A | F20 |
| ReBoot | A | B | C |  |
| reddevils | B | A | C | F03 |
| redhotchilipeppers | A | B | E | F16 |
| Redox (core) | F | C | G |  |
| redpandas | C | A | A | F22 |
| redvsblue | A | B | E |  |
| RelientK | A | B | E | F22 |
| rhythmheaven | A | B | E | F21 |
| rickandmorty | C | A | A | F32 |
| ripcity | A | B | F | F18 |
| riskofrain | A | B | F | F10 |
| rit | E | D | D |  |
| rocketbeans | A | B | F | F19 |
| rocketleague | E | D | D |  |
| rojava | D | C | B |  |
| romania | D | C | B | F01 |
| roosterteeth | A | B | F |  |
| rotmg | D | C | B | F23 |
| rpi | C | A | A | F08 |
| runescape | E | D | D | F01 |
| rush | E | D | D | F02 |
| russia | B | A | C | F22 |
| Russiaclan | B | A | C |  |
| rust | E | D | D | F08 |
| rutgers | D | C | B | F09 |
| rwby | E | D | D | F01 |
| sabres | D | C | B | F12 |
| sadboys | D | C | B | F12 |
| sakartvelo (core) | B | A | H |  |
| sakuragakuin | C | A | A |  |
| samuraijack | E | D | D | F01 |
| satania | C | A | A | F07 |
| sbu | F | C | G | F08 |
| schoolidolfestival | E | D | D | F01 |
| scotland | C | A | A | F24 |
| ScottPilgrim | C | A | A |  |
| scp | E | D | D | F21 |
| seahawks | E | D | D | F01 |
| seolhyun | A | B | E | F09 |
| serbia | B | A | H | F08 |
| seventeen | A | C | F |  |
| sheffield | C | A | A | F07 |
| shield | C | A | A | F07 |
| shishamo | D | C | B | F22 |
| shitredditsays | B | A | H | F24 |
| shrooms | D | C | B |  |
| signal (core) | A | B | F |  |
| simonfraser | B | A | C | F22 |
| singapore | B | A | C |  |
| sips | F | C | G | F20 |
| sixers | C | A | A | F27 |
| skyrim | C | A | A | F10 |
| Slovakia | B | A | C |  |
| slovenia | B | A | C | F08 |
| smashbros | E | D | D | F02 |
| smite | E | D | D | F22 |
| snsd | F | C | G |  |
| sonicthehedgehog | A | B | E |  |
| sooners | A | B | E | F08 |
| southafrica | C | A | A | F21 |
| southpark | D | C | B | F21 |
| soylent | A | B | E | F26 |
| spacex | E | D | D | F06 |
| spacexmasterrace | C | A | A | F07 |
| spain | B | A | H | F16 |
| spelunky | E | D | D | F01 |
| splatoon | C | A | A | F17 |
| spongebob | B | A | C | F15 |
| SquareSpiral | D | C | B | F09 |
| ss13 | C | A | A | F15 |
| ssbpm | C | A | A | F16 |
| starbound | C | A | A | F35 |
| starcitizen | E | D | D | F08 |
| starcraft | C | A | A | F01 |
| stardewvalley | A | B | F | F09 |
| stardustcrusaders | E | D | D | F01 |
| stargate | F | C | G | F01 |
| starlightstage | E | D | D | F10 |
| starryknights | A | B | F | F15 |
| startrek (core) | E | D | D |  |
| starvstheforcesofevil | A | B | E | F23 |
| stevenuniverse | E | D | D | F01 |
| stlouis | B | A | C | F20 |
| stlouisblues | B | A | C |  |
| strangerthings | C | A | A | F34 |
| straya | B | A | C |  |
| streetfighter | F | C | G | F03 |
| Summit1G | A | B | E |  |
| suomi | C | A | A |  |
| superman | C | A | A | F33 |
| survivor | E | D | D | F02 |
| sweden | B | A | H |  |
| SwissNeutralityZone | A | B | F | F19 |
| switzerland | A | B | E | F10 |
| swordartonline | E | D | D | F18 |
| SydneyFC | C | A | A |  |
| tagpro | B | A | C | F29 |
| taiwan | A | B | F | F18 |
| tampabaylightning | C | A | A | F07 |
| teamcube | C | A | A |  |
| TeamDignitas | B | A | H |  |
| TeamYellowPlace | A | B | E |  |
| telegram | A | B | E |  |
| Temple | D | C | B | F08 |
| tenma | F | C | G | F35 |
| terraria | D | C | B | F01 |
| teslamotors | E | D | D | F08 |
| tetris | C | A | A |  |
| texans | D | C | B | F02 |
| texas | C | A | A | F08 |
| texastech | A | B | E |  |
| tf2 | C | A | A | F33 |
| thailand | A | B | E | F26 |
| the_pack | D | C | B |  |
| THE_R | D | C | B | F27 |
| TheAdventuresofTintin | C | A | A |  |
| TheB1G | A | B | E |  |
| theblackvoid | B | A | C | F12 |
| thebluecorner | B | A | C | F23 |
| theexpanse | A | B | F | F16 |
| TheFarLeftSide | A | B | F | F23 |
| Thegreatblackhole | B | A | C |  |
| TheGreatGreenBox | B | A | C |  |
| TheHulk | A | B | F | F07 |
| TheID (core) | F | C | G |  |
| theitalyplace | B | A | C |  |
| thenetherlands | E | D | D | F02 |
| thepointing | C | A | A | F09 |
| thesilphroad | E | D | D |  |
| thesimpsons | D | C | B | F01 |
| thetreesnetwork | D | C | B |  |
| timbers | C | A | A | F07 |
| tinytardis | A | B | F | F15 |
| titanfall | E | D | D | F01 |
| tokyo | D | C | B | F20 |
| toolband | A | B | F | F09 |
| torontoraptors | C | A | A | F07 |
| totallynotrobots | E | D | D | F01 |
| touhou | B | A | C | F13 |
| traaaaaaannnnnnnnnns | D | C | B |  |
| TransFlagPlace | B | A | C | F16 |
| transformers | A | B | F | F10 |
| transgender | F | C | F |  |
| TreePlace | F | C | G |  |
| trees | C | A | A |  |
| truestl | C | A | A |  |
| TsundereSharks | A | B | E | F07 |
| turkey | B | A | C | F09 |
| twentyonepilots | F | C | G | F25 |
| twice | A | B | E | F09 |
| twitch | F | C | G | F07 |
| twitchplayspokemon | E | D | D | F01 |
| ubc | C | B | E | F22 |
| ubreddit | A | B | E | F09 |
| ucf | A | B | F | F15 |
| udub | B | A | H | F15 |
| ufl | F | C | G |  |
| uiowa | F | C | G |  |
| uiuc | A | B | E | F09 |
| ukplace | B | A | C | F08 |
| ukraine | B | A | C | F08 |
| ultrahardcore | E | D | D | F01 |
| UMiami (core) | B | A | H |  |
| undertale | B | A | C | F32 |
| unitedkingdom | B | A | H | F07 |
| UNLincoln (core) | F | C | G |  |
| unturned | C | A | A | F21 |
| uofm | B | A | C | F08 |
| uofmn | B | A | C | F10 |
| uoft | E | D | D | F24 |
| UPenn | F | C | G | F09 |
| uruguay | D | C | B |  |
| utahjazz | A | B | F | F14 |
| utaustin | A | B | E | F28 |
| uva | A | B | E |  |
| uvic | C | A | A | F07 |
| uwaterloo | E | D | D | F02 |
| vegan | C | A | A |  |
| VelvetUnderground | A | B | E |  |
| vermont | A | B | E |  |
| vietnam | C | A | A |  |
| Villanova | A | B | E |  |
| vim | D | C | F | F32 |
| vinesauce | A | B | E | F09 |
| virginiatech | B | A | H | F08 |
| vocaloid | A | B | F | F17 |
| wales | B | A | C |  |
| wallstreetbets | B | A | H | F08 |
| warframe | E | D | D | F01 |
| wario (core) | B | A | H |  |
| warriors | D | C | B | F13 |
| warthunder | F | C | G | F09 |
| watchmen | C | A | A |  |
| weezer | C | A | A | F18 |
| wholesomememes | D | C | B | F01 |
| wildhockey | F | C | G | F01 |
| wine | E | D | D | F19 |
| winnipegjets | A | B | F |  |
| WisconsinBadgers | B | B | F | F15 |
| witcher | A | B | E | F27 |
| worldoftanks | E | D | D | F02 |
| worldpowers | B | A | C |  |
| wow | E | D | D | F01 |
| WPI | B | A | C | F08 |
| wsu | B | C | C |  |
| xcom | A | B | E | F30 |
| xenoblade_chronicles | A | B | E |  |
| yerbamate (core) | A | B | F |  |
| yogscast | D | C | B | F19 |
| yugioh | E | D | D | F03 |
| yumenikki | D | C | B |  |
| yuyuyu | D | C | B |  |
| zelda | E | D | D | F01 |
| zootopia | B | A | C | F08 |

