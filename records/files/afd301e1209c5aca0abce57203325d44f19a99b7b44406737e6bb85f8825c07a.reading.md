# The onset contrast (contract section 5), written at A1a, 2026-10-06, before any room is read

Target length: under 900 words, the member lists apart.

## The rule

The clock is `onset_first_code_hour` in `rooms.jsonl`: the hour, since the canvas opened, of the room's first coded turn. It is populated for all 705 rooms.

- **Early side**: the first coded turn falls after hour 0 and before hour 3. These rooms wrote about the canvas within its first three hours, while it was still mostly empty.
- **Late side**: the first coded turn falls after hour 48. These rooms first wrote about the canvas in its third day or later, when most of it was already drawn and held.
- Rooms with a first coded turn before hour 0 (r/italy at -1.14, r/yogscast at -18.58) stand on neither side. Their first coded turn comes before the canvas existed, so it does not date when they came to it. In r/yogscast that turn (yogscast/c0024, at -18.58) is an offer of spare streaming keys. Its first canvas turn is yogscast/c0001 at hour 5.03.
- The middle, hours 3 to 48, is left out. With the two rooms above, 513 rooms stand on neither side.

The bounds come from the canvas's own clock, not from these figures. Hour 3 ends the first stretch of the empty canvas. Hour 48 starts the third day. Placement stopped at hour 73. I chose the bounds after seeing the quartiles (q1 3.76, median 9.51, q3 24.82). That knowledge shaped the bounds, and I say so here.

## Size of each side

- Early: 131 rooms (of 705).
- Late: 61 rooms (of 705).

## The confound, before anything else

Onset on this clock is in large part a measure of how much a room wrote. A room that writes more has more chances to write early. The two sides differ a hundredfold in size. The early side's median `items_in_window` is 5067 (q1 1468, q3 10885). The late side's median is 33 (q1 18, q3 131). The canvas areas differ the same way: medians of 1564 px and 152 px. Contract section 5 says code mass measures corpus size, not conduct. So any difference between the two sides must first be shown not to be a size difference.

I carry a held-size comparison with the main one. It uses the rooms on each side whose `items_in_window` lies in the census's middle half (156 to 2770). That leaves 41 early rooms and 12 late rooms. Twelve is thin, and any claim from it is labelled thin (rule 8).

## What I expect to differ

These are expectations, written before reading, for stage C2 to test against the model's arrows.

1. Late rooms will organize around finding room on a full canvas. I expect asking neighbours for space, moving the drawing, fitting into gaps and treaties made to be let in. Early rooms will organize around claiming and enlarging a space and then holding it against others.
2. Late rooms will have shorter organizing lives, with fewer hours between the first and last coordinating turn. Their record will hold more single calls with no visible reply. Some late rooms will show no coordination at all: one notice that something of theirs appeared on the canvas (r/watchmen, r/yerbamate are of this kind on the screen).
3. Early rooms will more often name rivals and keep fights going over many hours. Late rooms will more often name a host or a neighbour who let them in.
4. The held-size comparison will keep difference 1 and lose most of difference 3. If difference 1 also vanishes at held size, then onset on this clock is size and the contrast shows nothing about timing.

## Members, early side (131)

bitcoin, halo, overwatch, pcmasterrace, schoolidolfestival, dota2, leagueoflegends, thesilphroad, smite, totallynotrobots, worldoftanks, streetfighter, clashroyale, counting, india, mls, wow, hearthstone, ElderScrolls, globaloffensive, oneplus, australia, tagpro, thenetherlands, 2007scape, dankmemes, splatoon, pokemon, texans, kingdomhearts, teslamotors, philippines, undertale, babymetal, smashbros, eve, spacexmasterrace, mylittlepony, twitchplayspokemon, homestuck, cloud9, tf2, formula1, puzzleanddragons, rit, thailand, zootopia, titanfall, de, ice_poseidon, baylor, cirkeltrek, giivasunner, eagles, TheGreatGreenBox, AprilKnights, brasil, uofm, startrek, asktransgender, eder, fivenightsatfreddys, Rainbow6, mechanicalkeyboards, drugs, argentina, europe, ockytop, harrypotter, fullcommunism, frankocean, anarchism, rotmg, bindingofisaac, catholicism, feedthebeast, wholesomememes, monsterhunter, patriots, GreenEmpire, kanye, ireland, luciomains, radiohead, prequelmemes, nintendo, sweden, donaldglover, haskell, danganronpa, redhotchilipeppers, traaaaaaannnnnnnnnns, newzealand, unitedkingdom, paladins, france, habs, romania, leafs, h3h3productions, rwby, warthunder, rickandmorty, EraseThePlace, starlightstage, megaman, stlouisblues, transgender, chicubs, touhou, wallstreetbets, foxes, DestinyTheGame, ainbowroad, nascar, evex, runescape, lakers, nlsscirclejerk, rocketleague, PurplePixels, asexuality, kirby, denmark, floridagators, chile, portugal, suomi, trees, crusaderkings, dwarffortress

## Members, late side (61)

littlewitchacademia, vermont, fxKorea, guatemala, vietnam, latin, COSI, sooners, wsu, k_on, CelticFc, UMiami, watchmen, corridor, MiamiHurricanes, UPenn, mysterydungeon, nVade, parabola, ukplace, OrderOfTheKoi, DevonUK, natsume, seventeen, udub, mcgillrobotics, sheffield, bees, DiamondClub, Villanova, CSUFoCo, quq, Clannad, ibo, VelvetUnderground, heyyea, ManningPlace, Redox, Dorset, OKState, ElSalvador, DCFU, TheID, crystalclear, mamamoo, bigbang, signal, rainbowgrid, Cornwall, TheAdventuresofTintin, sakartvelo, azores, aeskwadraat, carletonu, Produce101, aeon, tetris, cgpgrey, UNLincoln, pgang, azerbaijan

## Held size (items_in_window 156 to 2770)

Early, 41: totallynotrobots, ElderScrolls, oneplus, tagpro, splatoon, texans, undertale, spacexmasterrace, twitchplayspokemon, homestuck, cloud9, rit, thailand, zootopia, cirkeltrek, giivasunner, eagles, TheGreatGreenBox, AprilKnights, uofm, ockytop, frankocean, luciomains, donaldglover, haskell, danganronpa, redhotchilipeppers, traaaaaaannnnnnnnnns, EraseThePlace, starlightstage, megaman, transgender, touhou, foxes, nlsscirclejerk, PurplePixels, asexuality, kirby, floridagators, chile, dwarffortress.

Late, 12: littlewitchacademia, vermont, vietnam, latin, k_on, mysterydungeon, nVade, ukplace, udub, ibo, ManningPlace, cgpgrey.

The lists come from `mem.py facts --field onset_first_code_hour --where ...` calls made in leg A1a and logged in `_mem_reads-A1.jsonl`.

## Recomputed on J's ruling 3, leg A1b-20, 2026-10-07

J ruled on 7 October 2026 that the onset is the room's first coded turn at hour 0 or later. Turns before hour 0 are reported apart. The sides keep their bounds: early from hour 0 to before hour 3, late after hour 48. The text above stays as written at A1a.

I recomputed the onset from every concept's hour in the store. The concepts were read through `mem.py codes` by `out/_analysis/a1_codes_dump.py`. Two rooms have a coded turn before hour 0, one turn each:
- r/italy: one turn at h-1.14. Its onset is now h0.15, so it moves from neither side to the early side.
- r/yogscast: one turn at h-18.58, the offer of streaming keys (yogscast/c0024). Its onset is now h5.03. It stays on neither side.

No other room moves. The quartiles of the onset are unchanged: q1 3.76, median 9.51, q3 24.82.

Sizes on the new rule:
- Early: 132 rooms (131 above, with italy). The median `items_in_window` is 5149.
- Late: 61 rooms, unchanged. The median `items_in_window` is 33.
- Neither: 512 rooms.
- Held size (`items_in_window` 156 to 2770): 41 early and 12 late, unchanged, because r/italy lies outside the band.
