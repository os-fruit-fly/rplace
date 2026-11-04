# Head, claude-v43-1

Target length: under 3,000 words. Rewritten whole at every close. Last written at the close of A1b-55, 2026-10-07.

## The method question, in one sentence

Can independently reconstructed case histories be composed into a shared dynamic account that supports explanations at successive levels of specificity, from population-wide patterns, through forms and subforms, to particular organizational histories, while keeping access to the evidence from which those explanations were developed?

The theory question is unchanged: when strangers organize on a clock they did not set, with no way to compel anyone and no goal given to them, what forms does organizing take, how do they differ in their functioning, and which of them keep the work alive?

## Where the run stands

Stage A1, the reading. Legs A1a, A1b-01 to A1b-19 and A1c are closed; A1c closed at the interview cut. All 705 rooms have a note.

J's rulings of 7 October 2026 (after the A1c handback) opened a catch-up pass, legs A1b-20 onward:
1. For every room whose case.md or brief.md was not served whole in A1, read both whole, then amend the note: replace the `coder unsure:` line with what case.md says, with thread ids, and add a dated `later:` line wherever the account or the brief changes the note. Forests and concepts are not part of the pass. Read each file whole, with no head, cut or limit below its total; before amending, check in the read log that lines served equal the total. If a block does not fit in a leg, stop at a safe stop and pause; never shorten the route. Log any departure the moment it is made.
2. Hour 0 is the canvas opening; Reddit's tests appear from about hour -16. Defect 7 is answered (a line appended to `defects.jsonl`).
3. The onset is the first coded turn at hour 0 or later. Done: only r/italy moves (to the early side); early 132, late 61, held size unchanged (appended to `contrast.md`).
4. The organizing end reported with and without calls after hour 73. Done: `out/organizing_end-to73-A1.jsonl`.
5. The rule is kept; its measured error is in `coordinating-rule-A1.md`.
6. `leads-outside-frame-A1.jsonl` is a ledger B1 may read.
7. `mem.py diary --last` now reads the newest part.

The catch-up pass is declared in `out/order-A1.txt` as comment lines `#<block><TAB><sub>` after the A1 order. 702 rooms, blocks 20 to 48, 25 rooms each (block 48 has 2). The diary's amendment lines are found with `mem.py diary --grep "amended" --limit 5000`.

Blocks 20 to 48 are done; the diary holds an amendment for all 702 declared rooms.
The shell shows at most 30 KB per call; the overflow goes under CONTROL, which is read-denied.

Note length (J, 7 October 2026): about 350 words is a guide, not a limit. Length and wording are my judgement; the pass/fail rules stand (the fixed lines, concept ids, case and brief read before the note). Do not cut earlier lines to fit new ones; cut only what I would not miss later, and log it. Keep the new lines short: coder unsure about 25 words, later about 45. The hook now reports a note over the guide as advice and lets it stand; `validate.py` counts these as warnings (18 to 24 a block, blocks 36 to 47). If unsure about writing, ask J (`mem.py ask`). When cutting the last doing clause, keep a full stop; removing it removes the line break before `week:`, and the hook refuses the note. A coder unsure line that says none, cites a concept id, or gives the brief's coverage ("N threads out of scope") is not case.md's word: replace it with case.md's limits and thread ids. Remove any gendered pronoun for a member when a line is cut.

`validate.py A1` before this close: 0 errors, 556 warnings (notes over the 350-word guide). A coder unsure line already drawn from case.md in an earlier read is kept and extended, not replaced (block 47: androidgaming, TheID). When case.md shows an earlier line is wrong, correct it through the later line or a small logged edit (blocks 46 to 48: seven, seven and two rooms, named in the close reports). Recount the head with `wc -w` after the last edit and before `done.sh`.

## Section 5, done in A1b-19

- `out/coordinating-rule-A1.md`: the coordinating-turn rule. A turn counts when its label's leading act calls, assigns, plans, reports placement before hour 73, defends, makes or breaks a deal, or corrects another's placement; not when it recounts, jokes, mourns, thanks, praises, apologizes, blames, or is a moderator's removal. After hour 73 only calls or plans for canvas work count. Stage B1 copies it into `prior.md` §5; a change needs a departure line and a diary line, and figures under both rules.
- `out/organizing_end-A1.jsonl`: 705 lines, nine fields, recomputed by the close-check from the store (scripts `a1_ends.py` and `a1_codes_dump.py`, logged departures).
- Figures: 44,116 of 115,388 concepts coordinate (0.382). Nine rooms have no coordinating turn: watchmen, Redox, yerbamate, Lugarix, azores, ReBoot, PokemonSage, UNLincoln, tetris. 146 rooms have their last coordinating turn after hour 73. work_remained: kept 347, lost 218, silent 140.
- Measured error (ruling 5): agreement 79 of 100; precision 0.92, recall 0.66. Median end h72.02 with calls after hour 73, h71.69 without (ruling 4).

## The census and the analysed set

- Census 705 rooms (`package/FRAME.md`, copy date 2026-10-04, hash 51513b1e...). Every count agrees across the frame, `rooms.jsonl`, the folders, the concepts and the themes.
- Screen: dropped 0, so the analysed set is 705. `dropped.jsonl` is written empty.
- Concepts 115,388. Second-order themes 7,844, all to be placed later in the run.

## What the checks found

Seven defects are in `defects.jsonl`, plus an eighth line answering the seventh. None blocks the reading. The first six: r/tenma has no canvas line; r/archlinux has a coded turn at hour 100.9; `n_codes_coder` has two meanings; `items.jsonl` has an undocumented state `collapsed`; concept reach is 1.0 everywhere; r/yogscast's first coded turn is not about the canvas.

The seventh, answered by J (ruling 2): 25 rooms' linked artworks show placements before hour 0, earliest h-15.92 (AmericanFlaginPlace); they are Reddit's tests while the canvas was closed. Catch-up later lines call them tests.

## The principal investigator's answer QA1-001

The concept-reach threshold stays at 0 items. No substitute measure is to be invented. Every room is read at concept level in the later model-building stages, and unplaced concepts are read at the end too.

## Figures I carry

- Log-log slopes on `items_in_window`: concepts 0.530, second-order themes 0.231.
- `n_off_platform`: median 4, max 88 (dankmemes).
- `px_window_share`: median 0.111, max 0.547; null for tenma.
- Concentration is null in 3 rooms (nonbinary, oltp, wario).

## The onset contrast

`out/contrast.md`. Onset = first coded turn at hour 0 or later: early 132, late 61, neither 512. Early: hours 0 to before 3. Late: after hour 48. The confound is size (median items 5067 against 33); a held-size comparison (items 156 to 2770, 41 against 12) travels with it. The expectation is in `contrast.md`. In every late room read, the linked work was placed from the first hours.

## The three sentences written before reading

The three sentences: one burst of calls in the first day or two, then defence and looking back, with coordinating turns ending near hour 73; fights with canvas neighbours and deals about borders, struck in the thread or sent to Discord; the goal set early by one call and changed only under pressure.

What the reading found against them (`notes-A1.md` §6): the artwork was often on the canvas before the room spoke; coordinating turns do not all end near hour 73; rivals often became partners; deals often did not bind the crowd.

Seen three or more times and logged, blocks 10 to 48 (each block's rooms are in `running-A1.md`):
- The brief shows words or habits the canvas work reused (eight to sixteen rooms a block, blocks 35 to 47); a shared project ran the week before (five in block 35).
- Members saying the canvas did not belong in the sub, or dismissing it (block 39 tampabaylightning, chicago, colombia, bostonceltics; block 40 math; block 41 buffalo, eesti, 49ers; block 42 startrek, corridor; block 46 HomestarRunner, detroitlions, unturned).
- Scripts, bots or extra accounts inside the room's own work (block 40 placesnek, bangtan, metalgearsolid; block 41 foxes, KState, python, eesti; block 43 dragonquest, teamcube; block 45 sbu, afip, livecounting, catalonia; block 46 sips, unturned, Goodboye, cowchop; block 47 catalunya, rpi, FederationPlace; block 48 predators).
- Members outside the Discord missed the plan or refused the venue (block 36 dwarffortress, vocaloid; block 38 SwissNeutralityZone, nyu); a venue or command could not bind every placer (block 37 polska, sixers; block 40 ChronoTrigger, metalgearsolid).
- The result disputed or doubted after the close (block 38 diablo, ElSalvador, Lugarix; block 39 kcroyals, rit, redpandas, truestl).
- Green Lattice and Rainbow Road as host, permit office and border authority (blocks 19, 26 to 28; block 34 latin, planetside, esperanto).
- A representative, Discord or deal that cannot bind the crowd; restraint or deals not accepted by every member (blocks 19 to 31, 33, 34).
- A room relocates or trims its work when a neighbour asks (blocks 19, 28).
- Restraint named as the room's rule (blocks 10 to 24), qualified by the room's own conquest talk (blocks 25 to 28); attack talk beside restraint (blocks 32 to 48); restraint only after a neighbour objected (block 44 mindcrack, paranatural).
- A neighbour protects the room's work, or a room that wrecked one helps it after (blocks 19, 24 to 30, 33).
- Decisions made in Discord, IRC, Telegram or a second sub, seen only as returned (blocks 19, 24, 28, 30 to 48).
- One or two members carrying the work; credit as one member's claim; a remake or last mark by one member (blocks 19, 27 to 29, 31 to 33).
- Members joining work already under way, or a room credited with work another group started (blocks 31, 32; block 34 araragi); outsiders defending or credited with the work (block 47 ElderScrolls, parabola, parrots).
- A canvas mark, call or label grown from something already running that week (blocks 20, 22 to 34).
- Misread edits, and the room's own defenders, scripts or bots undoing its work (blocks 22 to 31, 33).
- Bots or scripts deciding what stays, or named as makers (blocks 21, 24, 25, 29, 32).
- Members' own accounts of the same act disagreeing; blame never settled (blocks 23, 24, 29, 32, 33, 37).
- The work called pointless, spam or tiring, too small or thinly staffed; the result recounted as partial (blocks 24 to 28, 30, 31, 33, 34).
- Moderators gathering, routing or turning the canvas work (blocks 25 to 28, 30, 31, 34).
- The room's own April Fools switch or fake rules running beside the canvas (blocks 33, 34).
- The event recruiting into the sub, or to the product (blocks 25 to 33, 42 to 45, 47).
- The work carried elsewhere after the close (blocks 25 to 30, 32 to 34, 36, 37, 39 to 47).

## Contrary rooms

Blocks 01 to 18 by name only: morrowind, megaman, heyyea, egypt, duckgame, AprilKnights, flashtv, PinkVomitMonster, FloydVsVoid, anime, watchmen, TheAdventuresofTintin, tagpro, qotsa, cfb, drugs, UNLincoln, yerbamate, Redox, azores, archlinux; homelab, hentai, kpop, ubc, norge, cirkeltrek, loltyler1, bobross, nonbinary, zelda; ukplace, SwissNeutralityZone, GuardiansOfDatBoi, minecraft, GuildWars2, bardmains, placeDE; theitalyplace, spacexmasterrace, tampabaylightning, aoe2, 4chan, ice_poseidon, korea, drawhelix; greenlattice, norway, utaustin, france, masseffect, ducks, mariokart, natsume; thebluecorner, germany, vim, furry_irl, placehfarts, Pigifs, TreePlace, evedreddit; falcons, formula1, slovenia, sweden, wine, btc, nin, uoft; ReBoot, nVade, epublica, lego, foxes, math, popheads, ockytop; sadboys, spacex, Fez, warthunder, nascar, israel, magictcg, tenma, ManningPlace; cgpgrey, EraseThePlace, dankmemes, anarcho_capitalism, twice, TeamYellowPlace, mcgill, PokemonSage; totallynotrobots, finland, udub, GreenEmpire, danganronpa, india; ontario, orderofthebluecorner, CelticFc, enterthegungeon, eve, anarchocapitalism, teamcube; counting; polandball, ubreddit, canucks, rust, fivenightsatfreddys, kanye, azerbaijan; theblackvoid, rainbowgrid, raocow, Slovakia, taiwan, oltp, asexual; PlaceNL, pcmasterrace, PinkUnion, streetfighter, aeskwadraat, Mario, wallstreetbets; placestart, starryknights, tf2, brasil, wholesomememes, Thegreatblackhole, GreenCorner, ibo, wario; destiny, Summit1G, Okami, 2007scape, lithuania, stardewvalley, planetside.

Block 19: ainbowroad, dota2, Braveryjerk, dofus, Russiaclan, rotmg.

Catch-up notes whose not-this line the account qualified: utaustin, miamidolphins, placehearts, chicubs, lego, lebanon, israel, vegan, touhou, magictcg, straya, farmcarrots, TransFlagPlace, titanfall, rust, funhaus, AmericanFlaginPlace, trees, starvstheforcesofevil, brasil, prequelmemes, phish (blocks 23 to 29); bardmains, osu (block 30); vim, TreePlace, bih, japan (block 31); PORTUGALCARALHO, npr (block 32); GreenEmpire, armenia, satania, nyjets (block 33); hoodr, muse, esperanto, araragi, twentyonepilots, GreenCorner, Thegreatblackhole, yogscast (block 34); forsen, AcePlace, lithuania, terraria, PinkVomitMonster (block 35); DatBoi, WPI, ubc (block 36); texastech, linux, dallasstars, oman, sixers (block 37); aceattorney, sakuragakuin, quq, lsu, vermont (block 38); norway (block 39); FlipnoteStudio3D, placesnek, TheB1G, bulgaria (block 40); nVade, cardinals (block 41); COSI, bretagne (block 42); hungary, ucf, donaldglover, aggies (block 43); lifeisstrange, mindcrack, CKCrusaders (block 44); pitt, taiwan, msu, portal, catalonia (block 45); PinkUnion, gratefuldead, cavestory, destiny (block 46); daftpunk, WisconsinBadgers, seventeen (block 47); Russiaclan (block 48). The later lines say how.

The one room that fits nothing else, chosen at A1c: r/Summit1G.

## Open distinctions

None is filed in `_questions/`. Distinctions forming, to carry into B1:
- Who started the work: joining or finding work begun elsewhere, against starting it; a linked region placed from the first hours, against the room's late first call; a work credited to another sub or its Discord; a work the room mourned as lost that the canvas keeps.
- Where organizing happened: in the thread, against in Discord, IRC, Telegram, a second sub, a private sub (ockytop), a forum, or a stream; venues interleaved rather than replaced (esperanto); plans brought back for members outside the venue.
- Deals: binding, against not kept; truce against alliance; living on an ally's land by permission; hosting others' works in exchange for upkeep (TeamYellowPlace); leaders' deals against members' fights; a room kept by the stronger side's terms (Slovakia).
- A sub made for the canvas that governs others, polices purity, migrates, or claims a colour; or forms late around a pattern others repeated (rainbowgrid).
- Scripts: self-defence, refused, repairing a rival, joint, fighting the room's own plan, a neighbour's bot erasing an unregistered addition (yumenikki); hand defence against scripts (GabrielDropout).
- The moderator as organiser, obstacle, funnel, enforcer or permit office; a moderator who is also the main defender (oneplus).
- The end of organizing: before hour 73, at the close, or in calls to rebuild after it; the work kept elsewhere after the close.

## The last rooms read

Catch-up findings are in `running-A1.md` under "catch-up block NN". The last restore batch: splatoon to zelda.

## Ledgers at this close

- `lexicon-A1.md`: 1,289 lines. `running-A1.md`: 773 lines (this leg 6 entries). `leads-A1.jsonl`: 2,478 lines. `departures.jsonl`: 9 lines. `defects.jsonl`: 8 lines.
- Rule, kept:
  - Fetch every id with `cite.py`. Check every lead's room with grep against the frame before appending. Append through a grep filter on the item id. Never type an id from memory; check an id carried through a compaction against the notes or the diary before using it.
  - Never log "noted" or "passed" in the same call that writes the note; wait for the hook's answer.
  - Count a ledger's lines after appending, before logging the count; count the diary's trim lines before writing the closing line.
  - There is no `--kind close`; log the closing line as a note.
- The permission check refuses "=w=", for and while loops, shell functions, heredocs, awk and a variable set from `$(...)`. The command guard reads a bare "rm" inside quoted text as a delete. Use the Write and Edit tools for file content; an Edit whose old text spans non-adjacent lines fails, so edit lines one at a time.
- The diary rolls into a new part as it grows; during A1b-55 it moved into part A1-58. After a compaction the guard requires the exact line "compacted; head reconciled" through `mem.py log --kind note`.

## The next comparison

The restore pass (J, 7 October 2026), legs A1b-49 to A1b-53: one batch each from `out/_handling/pretrim-A1/BATCHES.tsv`. For each room, choose among the prototype in `restored/`, the cuts in `review/`, or leaving the note. Put back only my own pre-cut words, with no new reading, and log `<sub> restore: ...` for every room. Helpers: `python3 out/_analysis/restore_show.py <subs>` (read-only diff and review); `python3 out/_analysis/restore_put.py <sub> <leg> <field>...` (copies that leg's pre-cut "+" line for each field; refuses when the current line holds words the pre-cut one lacks; read those words, then add `--force` only for wording). All five batches are done: 447 rooms, 197 prototypes taken whole (A1b-49 to A1b-53: 91, 89, 88, 92, 87 rooms). Each leg's choices are in its close report in `notes-A1.md`. Leave out pre-cut lines that a cut leg corrected (ended lines, hedges, quotes of four words or more, gendered pronouns, stray thread marks such as "(t03 aside)"), but check ended lines against `organizing_end-A1.jsonl` (greece's pre-cut line was the right one); a catch-up not-this line that a later line qualifies stands. A1b-55 (J, 7 October): national, political and conflict content is study material. The 9 rooms I had left out for it, plus israel and tagpro, now hold my pre-cut words. Handler's rule: a choice to leave out or soften content for any reason other than the study's goes to J first (`mem.py ask`), and the content stays meanwhile. QA1-003 is open: bakchodi and dankmemes still hold back A1b-10 pre-cut lines after a safety stop in A1b-49. A pre-cut line that dates a turn differently from the cut line stays out. QA1-002 is answered: organizing is counted before the freeze at h73, so an ended line before h73 stands against a later ledger hour (canada, southafrica). The restore pass is complete; no further batch is declared.

After the restore, the next comparison is the `later:` lines across rooms, by the patterns above, when a leg message asks for it.

## Nothing changed in the scheme or the model

No scheme exists at A1, and none may be written in this stage.
