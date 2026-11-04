# Notes, stage C3 (the model against the literature)

## The literature is read after the model (section 1)

The explanation literature is read after the model and not through it. That is the design (contract section 4), not a departure, and no `departures.jsonl` line is written for it. The model it is read against is stage C2's resting state: pass 5 (`model-p5.md`, `model/story-p5.md`, `model/elements.jsonl`, `model/arrows.jsonl`, `structure-p4.md` for the tier).

**Whether the substitution worked.** The contract's section 1 frame is the claim that every group with a goal must solve four problems: task division, task allocation, reward provision and information provision. I knew it from stage A1 on and was told not to build with it. The distinction held in the names, as far as a search can show it:
- No fourth-order theme, dimension or construct block is named for one of the four. A search of `fourth/fourth.jsonl`, `dimensions.jsonl`, `structure.md` and `structure-p4.md` for "task allocation", "task division", "reward provision" and "information provision" finds nothing.
- The words "allocate" and "rewards" appear twice, each inside a `changed` sentence, the sentence that says what this material's version of a borrowed name cannot do. Mobilization's says that resource mobilization assumes organizations that hold and allocate resources, and here no one can hold a member's minutes. Completion ritual's mentions credit and rewards handed out in the ritual.
- `prior.md` expected a kind for reward to be thin ("thanks and credit are talk about the work, not reward"). The structure has no reward theme; credit to others is a third-order theme of its own.

Whether it held in the cuts, and not only in the names, I cannot judge from inside. The third-order tier was built at B1 in participants' words. My prior's list of kinds included "who does the work", which is close to allocation, and the coders' selection decided what talk reached me. Stage C3c's mapping is the test of the cuts, and section 5 forbids revising the structure to fit the frame.

## What I expected (`prior.md`, read first at C3a, before anything else)

`prior.md` was written at B1a, 2026-10-07, before any second-order theme was opened. What it expected, quoted:

- **The scheme.** "The scheme will hold hundreds of third-order themes, not tens. I expect between 250 and 450 at the end of B1, with a long rare tier." The scheme holds 197.
- **The kinds the material will refuse.** "Deliberation off the record ... the material will give only 'a decision returned from a venue'." "Reward and motive. The rooms rarely say why a member placed a pixel, beyond pride, fun, a joke or loyalty to a team or nation." "The canvas as outcome ... A kind like 'keeping the work' will rest on the room's words, never on the atlas."
- **Becoming able to act.** "Becoming able to act will rest less on persuasion than on a find. Many rooms became able to act when a member showed a mark already on the canvas, a template, or a host's permission. A call alone often drew nothing."
- **Settling what to act on.** "Settling what to act on will often be settled by the canvas before the room spoke (the linked work placed from the first hours), by a host's terms, or by one member's start. Votes and polls will be rare and late."
- **What sends a group back.** "What sends a group back to the beginning will be loss of the spot: a bigger neighbour, the Void, bots, a flag war, a moderator's move. After it, rooms either relocate, shrink, join a host, or stop."
- **What follows.** "What follows organizing will be talk about it: credit, blame, mourning, and calls to rebuild on a successor canvas."
- **The forms.** "I expect a handful of forms that differ in where the work was coordinated and on whose terms the room held its space: single-call rooms with little follow; template-and-defend rooms run through a Discord; canvas-born factions that govern territory; national rooms whose organizing is diplomacy among nations; late rooms that live on a host's permission."
- **At the top.** "I expect the population to compile more than compose: different rooms contributing different configurations (Kozlowski and Klein)."
- **The onset contrast.** "late rooms organize around finding room on a full canvas ... early rooms around claiming, enlarging and holding ... early rooms name rivals and keep fights going, late rooms name hosts; at held size the first difference stays and most of the third goes."

Where the model now stands against these, before any shelf is opened:
- **Becoming able to act** went the other way. The model's spine is the call: a start, then calls, then building (the call arrow holds in 137 of 190 rooms against a null mean of 0.467). A find of a mark already placed is a bound on two arrows, not the start.
- **Settling what to act on** came true in part. Votes are rare (decided order, finding F-006), and the work mostly settles itself: the topic's picture, or the land's flag. The host's terms settle it only for guests, which the model does not reach.
- **What sends a group back** came true: loss of the spot, then a move, with calls continuing (F-002).
- **What follows** came true in part. The close runs celebration, record, carrying on. Blame and mourning are not elements.
- **The forms** are stage D4's, but two of the five I expected are already boundaries the model does not reach: canvas-born factions that govern, and hosts' terms.
- **Reward** came back nearly empty, as expected.

## The re-read before the shelf (section 1)

Read again this leg, whole, before the explanation shelf was opened: `METHOD.md`'s first section; Suddaby (2006); Gioia, Corley and Hamilton (2013); Grodal, Anteby and Holm (2021); Eisenhardt (1989); Langley (1999); Van de Ven and Poole (1990). Langley's page 12 is Figure 2 turned into noise by the text extraction. I read it to line 1440 and checked lines 1441 to 1767 by pattern for words, and found none.

What these works ask of this stage, each `verified` (opened on the shelf this session):
- **Eisenhardt (1989, p. 544):** "Examining literature which conflicts with the emergent theory is important for two reasons. First, if researchers ignore conflicting findings, then confidence in the findings is reduced ... Second and perhaps more importantly, conflicting literature represents an opportunity." Her enfolding step, conflicting work first and then similar work, is this stage's first two legs.
- **Gioia, Corley and Hamilton (2013, p. 21):** "Upon consulting the literature, the research process might be viewed as transitioning from 'inductive' to a form of 'abductive' research, in that data and existing theory are now considered in tandem." This is why a read of the rooms prompted by a paper is logged as abductive.
- **Suddaby (2006, p. 635):** "The real danger of prior knowledge in grounded theory is not that it will contaminate a researcher's perspective, but rather that it will force the researcher into testing hypotheses, either overtly or unconsciously, rather than directly observing."
- **Langley (1999, p. 698):** the alternate templates strategy, where "the analyst proposes several alternative interpretations of the same events based on different but internally coherent sets of a priori theoretical premises." A contradicting work read against the rooms is one such template.
- **Van de Ven and Poole (1990, p. 318):** "It is generally better to develop and juxtapose alternative theories, and then determine which theory better explains the data."
- **Grodal, Anteby and Holm (2021):** a change made at this stage is still a move, named and logged.

## The log point (section 1)

Counted with `wc -l` after the method shelf was re-read and before any work of the explanation shelf was served:
- `_cite_reads-C3.jsonl`: does not exist, 0 lines.
- `_mem_reads-C3.jsonl`: 63 lines. The `mem.py log` call that recorded this count wrote one more line, so the file held 64 lines when the first explanation-shelf work was opened; the first served shelf line is line 65 or later.

From here on, a read of the rooms prompted by a paper is an abductive read, logged before it is made with `mem.py log --kind abductive`. The read logs record what was served, not why, so they cannot tell a check from an abductive read I failed to log.

At the close of C3a the read logs hold 135 lines (`_mem_reads-C3.jsonl`) and 12 lines (`_cite_reads-C3.jsonl`).

## Leg 1 (C3a): the contradicting shelf

### The works read

The six works of the explanation shelf's read tier were served whole, in pages under the output limit (`c3a_shelf_pages.py` planned the pages). Each is `verified`. What each did to which claim is in `literature-C3.md`, Leg 1, and in the diary line logged after each work.
- **O'Mahony and Ferraro (2007)** contradicts the claim that rooms organized mostly without decided order (C01, F-006). The disagreement is about the setting. An abductive read bounded F-006.
- **Bechky (2006)** contradicts the model on what coordinates a temporary group: a role structure carried in by careers, against a start, calls and a visible work. The disagreement is about the setting, which she names as her own open question (p. 17). It bounds her claim, not the model.
- **Felin and Zenger (2016; 2017)** explain organizing by an actor's contrarian theory. The model uses a start and a given picture. They are about different things. The question of whether each room inherited or chose what it made goes to C3c, under the goal.
- **Olson (1965), recalled,** on collective action without selective incentives. Open: the record cannot see members who never placed.
- **Puranam, Alexy and Reitzig (2014)** is the standing claim, put to the structure at C3c. Read here it resembles the model more than it contradicts it.
- **March (1991)**, read last, contradicts nothing. It bears on the residue of six pass 5 rooms, for C3b.

### The abductive read, and what it changed

One read, logged before it ran, prompted by O'Mahony and Ferraro (2007): does decided order gather in rooms that rule on other rooms' works, held to room size? It does, in the smaller rooms:
- 7 of the 39 rooms placed on a colour-faction theme or on vetting guests' requests carry decided order, against 39 of the 666 others.
- Held to size, 7 against a null mean of 2.7 (95th percentile 5, p 0.014).
- In the two smaller size quartiles: 5 of 14 against 13 of 339. In the two larger: 2 of 25 against 26 of 327.
- 0 of the 56 rooms whose members asked a host for space.

What it changed:
- `findings.jsonl` line 21 supersedes F-006 with status bounded, the condition in its `bound`, and `literature`, `abductive` and `prompted_by` fields.
- `model/history.jsonl` line 83 is a C01 line (event bounded, move relating or contrasting, abductive, prompted_by).
- C01's statement and range are unchanged. Its range already ends at "canvas-born factions holding elections".
- Snap C3-move-relating-48.

Why the new state serves the claim better: a reader of C01 alone would take decided order as rare everywhere. The bound says where it is not rare, and why the contradicting work found it necessary: governing a body over time, not making one picture in hours.

One turn surfaced by the read is carried as a doubt, not acted on: "a fellow comrade during the button" [PurplePixels/c0165] names a tie from an event before the canvas. The model states colour factions as bodies the canvas gathered.

### Switch records

None. No claim moved between the rooms' words and a pattern across rooms, and no name moved from the participants' to the literature's.

### What C3a did not change

No arrow, element statement, fourth-order theme, dimension or concept changed. No stage C3 successor file is written yet. `manifest-C3.txt` says so for each stage C2 file. Stage A1's three sentences (section 7) are read at C3c, when this stage's conclusions are in.

### Slips, C3a

- **The size script first listed the explanation shelf's works.** It would have served each work's first line before the log point. I caught it before running, and it served only the method shelf.
- **Four reads ran over the output limit** and were saved where they cannot be read: one page of Suddaby (2006) during the method re-read, two pages of Felin and Zenger (2017), whose lines are very wide, and one call that took two pages of O'Mahony and Ferraro (2007) at once. Each was read again in smaller pages. The served lines are in the read log twice.
- **One Eisenhardt (1989) page was piped through `grep` and `head -c 25000`.** That is a shelf read, not a room read, and its output was 10,746 bytes, so nothing was cut.
- **One command used awk with a `$` field** to filter Langley's figure page. The guard did not refuse it this time; the head's rule stands.
- **The manifest write and the check ran in one turn,** against the rule that keeps a write and its check apart. The check found a manifest line naming a file not yet written; the line was reworded and the check run again alone.
- **A head edit and its word count ran in one turn** while cutting the head under 3,000 words. The count ran again in a turn of its own after each later edit.
- **`mem.py log` writes a line to `_mem_reads-C3.jsonl`.** The log point above records both counts.

### The close-check, C3a

`python3 tools/validate.py C3`, run after the notes body and before the head was rewritten:

```
stage C3:
  mapping-C3.jsonl not yet written (leg 3's output)
  arrows 20 (0 with a mechanism from the literature), fourth-order themes 28, mapping lines 0, successors: none


0 errors (0 distinct shapes), 0 warnings
```

`done.sh C3` runs the same check at the close. Its report is in the leg's closing diary line.

## Leg 2 (C3b): the resembling shelf, with the concept

### Order kept

Opened with `AGENT.md`, the head, the stage file, the last five diary lines and `validate.py --open C3` (0 errors, 0 warnings). The shelf's read tier was served whole at C3a; this leg cites it from those reads, and each citation is `verified` with its page. The distant works are not on the shelf, and each is `recalled`. Stage C3 reads `assignments_final.jsonl` nowhere, so the C2 evidence script, which reads it directly, was not used. Pairs and samples were drawn through `mem.py codes --fourth ... --json`.

### What the leg did

- **Two abductive reads,** each logged before it ran, with its rules written first.
  - *Conversation analysis:* refusals of a call carry a reason in 23 of 38 read pairs, acceptances in 2 of 14 (p 0.003), and refusals are not longer (F-014).
  - *Threshold models:* none of 11 judgments of the room's own numbers rests on who answered (F-015, weak).
- **One distant field supplied a mechanism:** conversation analysis, for the one-line answer to a call (A12) and the refusal of an attack call (A16). Both are rewritten with the stage C2 sentences kept beside them (C3-move-relating-50). A12 stays theorised.
- **Four distant matches not rewritten,** each read declined with its reason in `literature-C3.md`: the dear enemy effect for the settled border, superordinate goals for coalitions, focal points for the template, the war of attrition for the move.
- **The concept is a relabelling.** The one-line enrolment is conversation analysis's preferred acceptance. It is renamed as borrowed, its head-count claim is dropped, and what it adds is a setting. `concept-C3.md` is written whole, and `concept.md` stands. A switch record is in `literature-C3.md`.
- **Two declarations amended** (`mistaken_for` only): Stigmergy against Puranam and colleagues' transparent task architecture, and Decided order against O'Mahony and Ferraro's shared basis of authority (C3-move-relating-49).
- **Successor files written whole:** `model-C3.md` (from `model-p5.md`), `structure-C3.md` (from `structure-p4.md`) and `concept-C3.md`. `manifest-C3.txt` names them.

### What the leg showed that I did not expect

- **The theme a reply sits under does not track its stance.** Replies coded under contention refuse attack calls ("Why? That'll just cause them to want to attack us" sits under "calling for attacks and answering the calls"), and replies coded under restraint include reports and remarks. A test that took the theme as the stance would have found a weak difference (0.38 against 0.55, by theme) where reading found a strong one (0.14 against 0.61).
- **The rooms judge their numbers by their readership.** "The game itself doesn't have enough population to pull this off." The rules for the threshold read did not foresee that ground.

### What I am sure of, and what I am not

- **Sure:** the account asymmetry on attack calls, as read; the failure of the head-count claim in the sample read; the decisions not to rewrite four arrows, each for a stated reason.
- **Not sure:** every code is mine alone, with no second reader. The CA asymmetry is untested on calls to place. The threshold read is one sample of one theme and an absence claim. Every distant work is recalled, not verified. The focal-point fit rests on a part of Schelling I cannot check.

### Slips, C3b

- **A claim about a ledger logged before it was checked.** The diary note on the threshold result gave the grounds as 4, 2, 1 and 4, counted from memory. The codes file gives 3, 2, 1 and 5. A correction line followed. The findings were written by script from the file and carry the right counts. My status message to the user carried the same wrong counts.
- **A field name assumed.** The threshold sample script first read a `label` field that the store's records do not have (they carry `first_order`). It ran once with empty labels; the script was fixed and run again. The sample is the same, drawn by seed.
- **One command used `cut -c`** after a script that read nothing from the rooms. The guard refused it, and it ran again without the cut.
- **The conversation-analysis pair script's output was first sent to `wc -c`.** The pairs were served and not seen. I read them from the sample file it wrote, not by serving them again.

### The close-check, C3b

`python3 tools/validate.py C3`, run after the notes body and before the head was rewritten:

```
stage C3:
  mapping-C3.jsonl not yet written (leg 3's output)
  arrows 20 (2 with a mechanism from the literature), fourth-order themes 28, mapping lines 0, successors: model-C3.md, structure-C3.md, concept-C3.md


0 errors (0 distinct shapes), 0 warnings
```

`done.sh C3` runs the same check at the close. Its report is in the leg's closing diary line.

## Leg 3 (C3c): the four universal problems, the goal, and stage A1's three sentences

### Order kept

Opened with `AGENT.md`, the head, the stage file, the last five diary lines and `validate.py --open C3` (0 errors, 0 warnings). The context was compacted once during the leg. After it I read the head and the stage file again, ran `diary --last 5`, and logged "compacted; head reconciled", but only after one write (the slips below). The page citations of Puranam, Alexy and Reitzig (2014) were checked against the shelf copy (`mem.py shelf ... --grep`, `--page`) before each was used. `notes-A1.md` was opened only for section 7, after the four-problems section and the goal were written.

### What the leg did

- **The mapping.** `mapping-C3.jsonl` has 28 lines, one per fourth-order theme. Nine map to one of the four universal problems and 19 do not: information 4 themes, reward 2, allocation 2, division 1. Two themes answer by construction: Mobilization (allocation) and Completion ritual (reward). Each mapped line says what this material's version cannot do. Each unmapped line names its test. Checked by `c3c_mapping_check.py`.
- **The counts.** Rooms per problem, rule 5's gates, and the goal's modes, each printed by a script (`c3c_rooms_per_theme.py`, `c3c_rule5_members.py`, `c3c_goal_counts.py`, `c3c_hours.py`). Thirteen quotes served through `cite.py`, chosen from a seeded sample (`c3c_quote_sample.py`).
- **Two findings.** F-016 (the mapping) and F-017 (the goal), written by `c3c_findings.py`; `findings.jsonl` now holds 25 lines and 17 findings.
- **The seven parts** in `literature-C3.md`, with `prior.md` quoted for part 1, each absence claim marked weak, and a side taken on reward and on allocation.
- **Nothing in the structure or the model changed.** No recut, no declaration amended, no arrow rewritten. The section 5 rule forbids revising either to fit the claim, and nothing else this leg called for it. No successor file was rewritten and the manifest stands.

### Stage A1's three sentences (section 7)

Read from `notes-A1.md`, for the first time since stage A1:

> Most rooms will show one burst of calls, coordinates and reports in the first day or two, then a long tail of defence and of looking back, and the coordinating turns will stop near hour 73 with little after. The fights the rooms name will be with their canvas neighbours more than with distant rivals, and the deals will be about borders and space, struck in the open thread or sent off to Discord. The goal will be settled in the first hours by one person's call, a flag, a logo or a character, and changed afterwards only under pressure from a neighbour or a loss of ground, rarely by argument inside the room.

**What I would have reached anyway.**
- *The goal is settled early by one person's start or by the room's own sign.* The third sentence says so. F-017 counts it: a proposal in 166 rooms with a median first hour of 12.7, an inherited sign in 152.
- *The goal changes under a loss of ground.* Also the third sentence. Relocating after losing the spot is in 116 rooms.
- *The remainder lies between rooms.* The second sentence put neighbours, borders and deals at the centre. A frame about one organization was always going to leave them over.
- *Bechky, and O'Mahony and Ferraro, differ from the model in setting.* I would have argued the setting from what I knew of the canvas.

**What the material forced.**
- *F-006's condition.* `prior.md` expected canvas-born rooms that govern. The count decided the condition: decided order gathers in those rooms (7 of 39, p 0.014 at held size), the gap lies in the smaller rooms, and it vanishes in the larger ones.
- *Refusals carry reasons and acceptances come bare (F-014).* Nothing I wrote before the shelf touched it.
- *The rooms judge their numbers by their readership, not by the replies (F-015).* This went against my own concept, and the concept lost its head-count claim.
- *The goal is argued.* The design is argued in 281 rooms, against the third sentence's "rarely by argument inside the room". The argument is over the pixels, not over which goal. A1 was right about who chooses and wrong about how much the room argues.
- *The goal is contested in the host sub,* in 152 rooms, over whether the canvas belongs there at all. No sentence foresaw the host as the place of contest.
- *Reward.* My C1 declaration called credit pay. The frame's definition and the 9 rooms that offered a reward before the work sent me back to `prior.md`: thanks and credit are talk about the work.
- *The goal has no home in the structure.* It is scattered across five themes. That came from doing the mapping, not from any expectation.

The first sentence, about the shape of the clock, was not tested at this stage.

### What the leg showed that I did not expect

- **The frame would cut through my widest reward theme.** Completion ritual joins credit, which maps something to members, with celebration, which maps nothing to anyone. The rooms do both in the same turns. The frame would take the credit and leave the celebration with no problem to belong to.
- **Division and allocation come apart.** A template divides the picture into pixels anyone can take (237 rooms). Division among members or teams appears in 5 rooms. The rooms divided the work, not the people.

### What I am sure of, and what I am not

- **Sure:** the mapping's counts, read by script; the reward definition's own condition, "if its constituent agents need to be motivated to contribute" (p. 165); that the structure, as it stands, carries 19 themes the claim has no place for.
- **Not sure:** the mapping is mine alone, with no second reader. Three mappings are more mine than the material's (Decided order, Visibility returns, Attribution). The goal's modes are my placement of third-order themes by their names, and the theme a record sits under does not track its stance. The sides I took on reward and on allocation are absence claims about small rooms writing in public, and weak. The claim that the four are not sufficient to tell the forms apart waits for stage D4.

### Slips, C3c

- **A write before the reconciliation.** After the compaction, I wrote `mapping-C3.jsonl` before reading the head and the stage file again and logging "compacted; head reconciled". The guard then held the log until the head read registered. The file came from the plan drafted before the compaction, and it was checked afterwards against the shelf and the tier.
- **An unchecked claim attributed to the paper.** Decided order's mapping line first called allocation by decision "the frame's classic, authority-based solution". I had not checked that the paper says so. The clause was replaced with a plain reading of the theme.
- **A tool's output format assumed.** The mapping check first parsed `mem.py rooms --with` as JSON. Its output is plain text, paged at 80 lines. The script was fixed before any count was used.
- **A regex took names from the wrong lines.** The goal-count script first read third-order names from anywhere in `structure-C3.md`, and printed wrong names. The counts were unaffected. It now reads names from the member lists only.
- **One `cite.py` call failed.** `--theme` needs `--room`. Nothing was served.
- **A placement changed between runs.** The first goal count put the proposal by one member under negotiation. I moved it apart before writing, because a proposal others join is a start. Both runs are in the read log; the findings carry the second.
- **The interview brief first ran to 820 words** by `wc -w`, over the 800 limit. It was cut to 768.

### The close-check, C3c

`python3 tools/validate.py C3`, run after the notes body, the handback and the interview brief, and before the head was rewritten:

```
stage C3:
  arrows 20 (2 with a mechanism from the literature), fourth-order themes 28, mapping lines 28, successors: model-C3.md, structure-C3.md, concept-C3.md


0 errors (0 distinct shapes), 0 warnings
```

`done.sh C3 --cut interview` runs the same check at the close. Its report is in the leg's closing diary line.
