# Fleet coder's contract, instrument __INSTRUMENT__

You read one time-ordered slice of one community's week and code it. **Read `CONTRACT.md` first
and whole.** The method, the register, the citation rule and steps 1, 2 and 3 hold for you
unchanged; this file says what is different about reading a slice, and it wins over `CONTRACT.md`
on those differences only.

Rule 1 for you reads: your corpus, your briefing, `timeline.md`, `lexicon.md`, nothing else.

---

## 1. What you do and do not do

You do step 1, step 2 and step 3 on your slice, and then write `case.md` and `notes.md` as §4
says. **You do not do step 4**: no theme, and nothing about the community as a whole; your
one-sentence reading in §5 is of your slice and no more. You do not run the counter-reading
search, you give no verdict, and you do not call `emit.close()`; the case lead does those over
every slice.

You are not given any other coder's codes, case or notes, and you must not ask for them. Two
files reach you from earlier slices, and both are facts, not readings.

## 2. What you get

- **`brief.md`**, the community before the canvas opened.
- **`timeline.md`**: stickies, moderator posts and edits, with times and item ids, as earlier
  slices left it.
- **`lexicon.md`**: the room's own words, one per line, each with the item id of its first use.
  A name for a piece of the drawing, a nickname for a neighbour, a verb the room made up. No
  gloss.
- **Your slice**: whole threads, in time order. `AGENT.md`'s STATE block says which slice it
  is and where it sits in the week. The corpus's counts include the context openings below;
  the STATE block's slice line is the count of your own threads.
- **Openings of earlier slices' threads** that were still receiving replies during your slice,
  marked `[CONTEXT — an earlier slice's opening]`. Read them, so the room's running threads are
  known to you. Never code them, never cite them, and do not record them with `emit.thread`:
  they are not threads of your slice, and `emit` refuses all three.

If you find a reading in either facts file, say so in `notes.md` and do not extend it that way.

## 3. Your slice has two edges

Unless yours is the first slice, you start mid-week: what you read began before you, and you
cannot see it begin. Do not write as if the practices you find started when your slice did.
Unless yours is the last slice, you stop mid-week: an argument still running at your last thread
is not resolved, it is unresolved to you.

Every episode in your `## Chronology`, and every exchange you name in `case.md`, ends with one
tag: `[closed]` when it begins and ends inside your slice; `[inherited]` when it began in an
earlier slice's opening you were given; `[unresolved]` when it is still running at your last
thread, with what would settle it. Where you cannot tell, write `[unresolved]` and say why. The
case lead reassembles the week from these tags.

## 4. Coding, and what you leave alone

`CONTRACT.md`'s step 3 applies unchanged. A bare "placed", "done", a set of coordinates, a
one-word agreement: these are passages of a kind, and §6 lets you cluster the awkward material by
kind, so one code for the kind is enough. Do not mark an item as uncoded and do not draw a tree:
the forest is built afterwards from the reply structure and your codes, and it keeps an uncoded
turn whenever a coded turn hangs below it.

Give a call and its answer one `exchange_id` whenever both are in your slice.

A `coded` thread disposition is a commitment: before you finish, that thread must have at
least one live, non-retracted code. If no passage supports a live code, revisit the thread and
record the disposition the evidence supports. An `out_of_scope` thread with ten or more
in-window items carries the exact exclusion citation returned by `cite.py`, as the main
contract requires. Reading the whole thread does not replace that citation; the trigger is
size, read state, and exclusion.

## 5. Outputs

`emit` keeps your codes, dispositions and pointers in `out/_journal.jsonl` from your calls;
the case lead's `consolidate` writes the files from it. Announce `step6_account` before
`case.md` and `step7_write` before `notes.md`. You write:

    out/case.md      your slice, in CONTRACT.md's sections, each episode and exchange tagged;
                     `## Counter-reading` states your one-sentence reading of the slice and
                     what would unseat it, and says the search is the case lead's
    out/notes.md     CONTRACT.md's notes without the two-themes question, and three more
                     things: where your slice sits (its
                     first and last thread, and the hours of the 97 it covers, from STATE);
                     what you could not tell because you did not see the earlier week; whether
                     your slice ended in the middle of something, and what
    timeline.md      extended with what your slice adds: facts only, one line each, with item ids
    lexicon.md       extended with every new term your slice introduces, with the item id of
                     its first use

Before your final message, run:

    python3 close_run.py . --role fleet --preflight

Fix every reported failure and run it again until it passes. This checks the whole assigned
slice. A retry instruction naming one defect adds that defect to the checklist; it never narrows
the assignment to that defect or to a subset of the slice.

**Final message.** The community, the batch, your two edges as §3 has them, and anything that
blocked you. Nothing else.
