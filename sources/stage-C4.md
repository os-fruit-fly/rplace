# Stage C4. The field.

**Model:** as `arm.json` sets for this stage (your platform file lists the model and effort). **Legs:** one. **Fleet:** none.

**Steps:** `C4a` the field, the handback and the interview. Each leg is named by its step (STANDING §2).

**Safe stops:** after each list of §2 and after each change the field forces. At a safe stop, check for `.pause` (`ls .pause`); if it is there, log where to pick up and the next item (`mem.py log "<hypothesis>; next: <item>" --kind pause`), and close with `done.sh C4 --pause` (STANDING §2).

**Startup packet:** `_head.md`, this file, the last five diary entries, `validate.py --open C4`; `field/`, placed by the handler when this leg opens.

**Reads allowed:** everything stage C3 allowed, and `field/`: the field model, its phases and its evidence. Quotes from your rooms through `cite.py`; the field's quotes as `field/` gives them. **Forbidden:** reading r/place's own threads (you hold the field's model and its evidence, never its corpus); rewriting the story (that is C5); withdrawing a finding because the field says otherwise; entering from the field anything your rooms could not confirm or refute; the canvas as an undeclared ground (rule 7).

**Outputs:** `field-C4.md`; tentative entries in `model/elements.jsonl` or `model/arrows.jsonl`, each with `"origin": "from-field"`, `"status": "tentative"`, `field_support` and a `model/history.jsonl` line; wherever this stage changes something, `model-C4.md`, `structure-C4.md` and `concept-C4.md`, each a whole file superseding the stage C3 file (or the stage C2 file where C3 wrote none), and `manifest-C4.txt`, one line per file of `manifest-C3.txt` saying whether it has a stage C4 successor, which stage C5 reads first; `notes-C4.md`.

## 1. Why this stage exists

r/place, the subreddit the event was named after, is not one of your rooms. It was the square where the
rooms met: where factions recruited, allied, argued over borders, and told each other what was
happening. It is the field, and the census keeps it out of the population for that reason: a room
of 207,342 items that narrates every other room is not a case beside them. It was coded apart,
under its own contract, and a separate analyst, sealed from you as you were from it, built a model
of the event from it. You receive that model now, and not before, so that it could not become the
template your rooms were read through.

## 2. The return to the field

**What arrives.** The handler places `field/` in your folder when this leg opens: the field
analyst's model (`field/model.md`, its tiers and arrows), its account of the event's phases, and its
evidence, each claim with quotes and thread ids. Not r/place's corpus. If `field/` has not arrived,
write in `field-C4.md` that the field was not held and why the handler gave, and close the leg;
nothing below applies.

**Read your own model first.** Restate in `field-C4.md`, before opening `field/`, the three claims
of your model that a view of the whole event could most easily overturn. Then read the field model
whole.

**The confrontation, in three lists, in `field-C4.md`:**

1. **Where the two agree.** A mechanism both models hold, said in each model's own words, with one
   room and one field thread. Agreement from two sources read by sealed analysts is the strongest
   evidence the study has; say which of your findings it touches.
2. **What only the field sees.** Mechanisms that live between rooms (coordination, alliances,
   disputes, the event's phases) and that no single room could show you. Each may enter your
   model as an element in `model/elements.jsonl` or an arrow in `model/arrows.jsonl`, with
   `"origin": "from-field"`, `"status": "tentative"`, `field_support` (the field's threads or items
   that show it) and a `model/history.jsonl` line, as a hypothesis. Stage D sends a tentative entry
   to every room, marked tentative and with no word of where it came from (J, 2026-09-29), and each
   room says from its own record whether it shows its side of the entry, contradicts it, or says
   nothing; silence counts. Enter only what a room could answer from its own record; what no room
   could goes in the list and stays out of the model. A fourth-order theme never enters from the
   field: no room can answer a grouping. An entry sits under a fourth-order theme stage C3 already
   mapped to the four problems (`mapping-C3.jsonl`); if the entry changes which problem that theme
   reaches, say so in `field-C4.md`, and the mapping line is amended as stage C3's §6 says.
3. **Where they disagree.** Where the rooms contradict the field's account, or the field
   contradicts yours. Nothing in your model is withdrawn because the field says otherwise; it is
   bounded, or the disagreement is printed beside it, as with the literature at stage C3. Say which
   source you trust on the point and why: the field sees the whole, the rooms see the inside.

A change the field forces follows stage C3's §6: amend, record in `tier_history.jsonl` with the move, log and
snap it (`python3 tools/snap.py C4 move-<move>-<n>`). Every finding line a change touches is
re-examined in the same act (rule 14), and a finding the field changed says so (rule 13).

## Moments to log

The field's arrival, or its absence and the reason; the three claims restated before reading; each agreement, each `from-field` entry and each disagreement; each change by move.

## Final message

How many mechanisms the two models share, how many entered `from-field`, and the sharpest disagreement, with the source you trust on it and why. Then: findings bounded or changed by the field; files with a stage C4 successor.

## Close

`done.sh C4` at the end of the leg, every change logged and snapped as it was made; paste the close-check report into `notes-C4.md`; `handback-C4.md`; the head; the closing diary line.

**Interview point.** `C4a` writes `out/interview/C4a.md` (under 800 words: what you did, what you found, what surprised you, what you doubt, and the three questions you would most like to be asked) and closes with `done.sh C4 --cut interview`: the model read against the field: what the two sources share, what only the field shows, where the rooms and the field disagree. The principal investigator may talk with you here, in a fork of this leg, run in a copy of your folder as it stood at the close (not read-only; nothing done there reaches the run); the run goes on from the cut either way. `done.sh` files the brief under the leg, the stage, the step and the minute, and refuses the cut without the brief and the handback.

## Level and distributed process evidence

An inter-room mechanism may be evidenced jointly across several case records. Name its level, the participating rooms, exact dated items and how their contributions connect. A property of their interaction need not appear unchanged in each room. Within-room claims still require within-room evidence. Record any grounded field feedback loop in `model/loops.jsonl` using C2's typed provenance rules; otherwise retain it as tentative or unresolved.
