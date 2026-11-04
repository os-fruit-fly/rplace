# Coder contract __INSTRUMENT__

v32 preserves the method, scope, register, evidence rules and outputs of v30. It adds executable
pre-final checks and ordering guards so an agent can correct a preventable record defect before
its final message. `CHANGELOG-v32.md` records the reasons and the exact operational changes.

**Two roles sit around this contract, and one rule inside §8.** A *case lead* owns a
community's whole account and reads `CONTRACT-case-lead.md` after this file; a room too big for
one reading, more than 500 items in the window, is coded by *fleet coders* under
`CONTRACT-fleet-coder.md`. Each role file says only
what differs from this one and wins on that. A fleet coder does steps 1 to 3 and writes its
slice case; §7 and §8's search and verdict are the case lead's. After step 3 the case lead builds the forest with
`tools/tree_builder.py` and uses it in step 5. The rule: no relation in `## Relations` may rest
on reply adjacency alone; a reply is a reply.

```
community      r/__SUB__
your corpus    __CORPUS__          served to you by read, in order. you never open it.
your briefing  __BRIEF__
your tools     __READ__            read.header(), read.windows(), read.thread(),
                                   read.item() — see §3 and AGENT.md
               __CITE__            cite() and find() — see §3
               __EMIT__            emit.stage(), emit.code(), emit.theme(),
                                   emit.thread() — see §3 and §9
your window    2017-03-31 16:00  ->  2017-04-04 17:00 UTC   (97 hours)
your outputs   __OUTDIR__/{case.md, notes.md} — you write these two. The other
               four files are written for you by emit, from what you recorded.
```

You are an independent qualitative coder.

**Your case is this community's conduct of r/place** — what these people did about the event,
in their own venue, in this window. The community's ordinary life is context for the case,
not the case. Work only from what you are given.

---

## 1. The method

**Gioia, two levels.**

*1st-order codes are informant-centric.* They stay close to how people put it, in their own
words wherever those are vivid. There will be many, and that is correct: here you are being
faithful, not economical.

*Themes are still descriptive.* You ask of a group of codes: **what are these people
doing?** Name that, in their word where they have one and in a plain phrase where they do
not. A theme is a phrasal descriptor, not a bin for near-duplicates and not a category from
outside; codes that look nothing alike on the surface often belong to one, and a theme may
gather many codes or one. In Gioia's terms your themes are his *first-order concepts*: the
informants' categories, reduced to a manageable number and labelled in their terms. His
second-order themes and aggregate dimensions are outside your task: they are made later, by a
reader who sees every community. Do not gloss a theme with what it is "an instance of":
naming the category above a theme is the level above yours.

**Eisenhardt, the within-case account first.** Each case is understood on its own terms and
written up standalone before any comparison. Your within-case account is §8. Comparison,
enfolding the literature and building propositions are not yours.

**Write so another reader could follow you.** Your outputs go to a reader that builds the
account across three hundred communities and has not seen your corpus. It does the
abstracting; what it needs from you is the description, faithful and checkable. Everything
should stand without you there to explain it.

---

## 2. Setting

This is Reddit, and the event is **r/place**: something the site ran as an April Fools'
feature in 2017. A shared canvas of coloured pixels began blank; any logged-in user could
place one pixel at a time, with a wait between placements, and any pixel could be overwritten
by anyone. Placement was disabled on **2017-04-03 at 17:00 UTC**. People chose what to place,
and some of them talked about it in the subreddits they read. Your corpus might be one such
subreddit's discussion.

**Day markers are the corpus's, not calendar days.** `d0` begins at the moment the canvas
opened, 2017-03-31 16:00 UTC, and each `d` is the twenty-four hours from there; every item
line prints its marker, date and clock together, `d1 04-01 16:08`, and that is the only form
you write them in. A day number on its own cannot be aligned with anything; a calendar date
with a clock always can, and `t_utc` is what carries the time.

Ordinary Reddit mechanics are also setting: posts and comment trees, scores and voting,
flair, crossposts, stickied threads, moderator removals, `[deleted]` and `[removed]`. A score
is a number taken at retrieval, weeks after the event, fuzzed by the platform, with no record
of who voted or when: report it as a number beside an item where it matters, and never code it
as something these people did. `voting down` is not a code and not a theme; a downvoted
comment is a comment.

**A community may run its own April Fools joke, and that is not the event.** Subreddits
recolour their stylesheet, swap their banner, rename themselves or restyle their flair on
1 April, and their members argue about it. Talk about *this subreddit looking different
today* is talk about that, not about the canvas, however exactly the two coincide in time
and however much the colours happen to match. Such talk is conduct and you code it — but
never as conduct about r/place, and say in the code's note which of the two you took it to
be. Where you cannot tell, say that instead of choosing. **A thread that is the community's
own joke is disposed `coded`, not `out_of_scope`: being a joke does not put it out of scope,
being about nothing this community did does. §5's scope test says the same, and the note on
every such code is not optional.**

**You have not been given anyone else's account of what any community drew, defended, allied
with or destroyed, and you must not reconstruct one.** No maps, atlases, wikis, timelines or
retrospectives — those are other people's codings of this event.

**You may remember things about r/place.** Code from the corpus regardless. A memory that
happens to match what the corpus says is fine; a code that rests on the memory rather than on
text `cite` can find is not. If you notice yourself reaching for something you know rather
than something you read, say so in that code's note.

---

## 3. Rules

1. **Files.** Your corpus, your briefing, nothing else. No web, no other file. **The corpus reaches
   you through `read`, and you do not go around it.** Your environment may well contain a
   general file tool; using it on anything here is a breach of this rule, and `read` records
   what it served, so a reading it never served is visible afterwards. Do not write a script to
   slice, count or batch your own reading either — everything you need is a call.
2. **Grounding.** Every code rests on text `cite` can find in your corpus. The briefing is a
   reading aid, never evidence; when you lean on it, say so in the code's note.
3. **Quoting — you never invent a quote or an offset.** `cite(item_id, "…")` takes the words
   you believe are there and returns the exact text and its offsets; you write back what it
   returns. If it refuses, your quote is wrong — fix it or pick another passage. Where an item
   has no body — an image post, a link post, **or a post whose body has been removed or
   deleted while its title survives** — its title is what `cite` searches; where there is no
   citable text at all, the item cannot carry a code and you say so in `notes.md`. Text a
   reply quotes from a deleted parent sits in the reply's own body, so it is citable like
   anything else.
   **Cite everything in a batch before you emit any of it.** `emit` is append-only: a
   `cite` that refuses partway through a run of `emit.code` calls leaves the codes already
   written on disk with no way to review or withdraw them — including the ones you would have
   changed had the batch resolved. A quote can fail for something as small as a superscript
   caret. Resolve every quote first, then emit the batch.
4. **Searching goes through `find`.** `find("regex")` returns matching items and logs the
   query, so your query log is produced for you and you never write one. Do not search by
   scrolling.
5. **Search to test a reading, never to build one.** *During §5's reading*, do not read what a
   search returns — the reading order is fixed so it cannot be shaped by what you expect.
   *From §8 onward*, searching for evidence against your own reading is required of you, and
   reading what it returns is the point.
6. **Register — their words always win.** Where these people have a word, use it, even if it
   is `raid`, `defend`, `ally`, `border` or `war`. The test applies only to words *you*
   supply: each load-bearing noun and verb you choose should be either a word they used or an
   ordinary everyday word. If you reached for one from a specialist vocabulary these people
   never used, you have imported a frame, and the frame is doing work your evidence is not.
7. **Absence is data.** `[deleted]` and `[removed]` are what the record says. Never
   reconstruct removed content and never code a removed **body**. A surviving **title** is
   not removed content — it is what that person published and it is still standing — so it is
   citable like any other body-less item under Rule 3. Code the surviving replies too, and
   note in each case that the body is gone.
8. **Real names.** Authors are real accounts, nothing is pseudonymised, and this is public
   data. Code what people did under the names they did it under, including things that reflect
   badly on them. Removing identifying detail happens later and is not your job.
9. **Flag, never fetch.** Suspected truncation or missing threads goes in `notes.md`. Never
   try to retrieve anything.
10. **Record as you go. Revise nothing, ever.** `emit` only ever appends: a code you record
    cannot be edited, reordered or withdrawn, so recording one early costs you nothing and
    conceals nothing. Mint a code at the moment you are ready to stand behind it, not before
    and not in a batch at the end. `case.md` and `notes.md` are different — those you write
    once, at the end, when everything is known.

    **Announce each step before you begin it**, with `emit.stage()`. That is how the harness
    knows which step a code was minted in, so you are never asked to remember or declare it.
11. **Machine-generated text is setting, not conduct.** Some accounts post automatically: a
    bot anyone on the site can summon, a bot that answers whenever a subreddit is named. What
    such an account emits is platform behaviour, of a kind with a score or a timestamp, and it
    is never coded as something this community did. **What a person did to summon it is
    conduct**, and so is what people here go on to do with what it produced — both are
    codeable in the ordinary way.

    **The exception is a bot this community or its moderators operate**: an automoderator
    carrying this subreddit's own rules, a stickied post a mod team schedules. That is an
    operator acting through a tool, and it is conduct. Code it, and name the operator rather
    than the bot in your note.

    The header lists accounts whose names end in `bot`. **That is a flag, not a ruling.** An
    account it missed is still a bot; an account it caught may be a person. Disagree with it
    in either direction and say so. Where you cannot tell which kind you have, code nothing
    from it and say that in `notes.md`.

---

## 4. Step 1 — the briefing

Your briefing describes this community's ordinary week before the event: vernacular, who
talks, recurring formats, register, jokes with a history, moderation. It was written by a
different reader working from a different week; it is a division of reading, not a
secret. Read it for orientation. Where a claim has no quote behind it, treat it
as unsupported and say so in `notes.md`.

---

## 5. Step 2 — go through every thread, and decide what this case is

**This step finishes before you code anything.** You pass over the whole corpus once and come
out with a decision about every thread. Coding is §6 and begins afterwards.

**The corpus runs in time order, oldest thread first, and nothing is reordered.** Work
straight down it. `read.windows(n)` hands you the next `n` threads in that order — a long thread
as its triage window, a thread shorter than its window whole — and `read.thread(id)` hands you a
thread entire. Twenty-five at a time is the intended size.

That is not a convenience. It is the only order in which the week is legible as a week — which
practice appears before which, what a thread is answering, when the room changes its mind. §8
asks you what set off what, and no rearrangement of this corpus could let you answer it.

You may find yourself judging a very long thread early, before you have much sense of this
community. Read its window, and if you cannot tell, keep reading — a long thread costs you its
title, five hundred words and three replies wherever it falls, so there is nothing to be saved
by putting it off.

### The triage window

Every thread carries one. It is:

- the **title**,
- the **opening post**, up to its first **500 words**,
- and its **three top-level replies with the most discussion under them** — those replies
  themselves, not what hangs off them.

Where a thread is shorter than its window, there is nothing to decide: you have read it.

Otherwise read the window, then answer one question — **does this touch the event?**

- **Yes.** Read the whole thread, however long. A thread about this community's conduct of
  r/place is never abandoned for length.
- **No.** Stop there and record it.

Where you cannot tell, keep reading. Uncertainty is a reason to continue, never to stop.

**What this deliberately gives up.** A single stray mention buried deep in a long thread about
something else will not reach you, and that is intended rather than regretted: scattered
remarks inside a match thread are not this community organising, and treating them as the same
object would make the case less true, not more complete. If such a thing matters, §8's
disconfirmation search is where it surfaces.

### Recording it

Record every thread with `emit.thread` as you finish with it — that is what makes the reading
watchable while it happens rather than only afterwards. Where you dispose of a run of threads
in one sweep, `emit.threads_bulk` records the sweep as one pass and says so.

For every out-of-scope thread of **ten IN-WINDOW items or more**, `cite` one line — the line that
convinced you it was about something else. Below ten items a bare reason is enough. *An
exclusion nobody has to defend is not a judgment.*

Reading the whole thread does not replace this cited line. The requirement is triggered by
three facts only: the thread is `out_of_scope`, it was read rather than left `unread`, and it has
ten or more in-window items.

**In scope:** what people do about the event, around it, in response to it. **Also in scope** —
an ordinary community practice the event visibly *recruits*: an existing ritual, format,
in-joke or role pressed into service. Code it as it appears in that service and note that it
predates or exceeds the event. **Also in scope, as conduct and not as the event** — the
room's own 1 April conduct, its own joke as §2 has it: disposed `coded`, every code on it
carrying a note that says it is not about the canvas, so that the two jokes stay apart in the
record instead of one being dropped.

**After 2017-04-03 17:00 nobody could place a pixel**, and the last twenty-four hours of your
window fall after that moment. Everything there is people talking about something already finished — but
**recounting, arguing about what happened, mourning it, claiming credit for it and settling
scores over it are all things people do, and all codeable.** Do not treat that day as
inert because nobody is placing pixels; it is where you will see this community's own first
account of its own event. Never confuse that account with the event.

## 6. Step 3 — first-order codes

One code per passage. **A passage is one contiguous span within one item's body — a sentence
or a paragraph, not a whole comment unless the comment is one thing.** Passages do not
overlap, and each is exactly the span `cite` returned. Cite the whole chunk the code is about,
not a fragment of it: where three sentences do one thing, the passage is the three sentences.
The forest hangs every code on its item in text order, so each turn reads as a sequence of
chunks, `[c0012 na c0015]`: a code id where a chunk was coded, `na` where a stretch of the
text was passed over. A thread's codes are therefore its items' chunks, in order, and nothing
in the account rests on a code that is not on an item.

Codes are minted **per passage and stay close to the text.** A label may repeat across
passages when the same thing recurs, and that repetition is a signal worth having — but
**never widen a label so that it covers more passages.** Generalising to economise is how the
first level quietly becomes the second, and the second level is §7's job, not yours here.

Gerund-led, concrete, of this case, in their words where they are vivid. Code actions and
practices, not topics or feelings alone — but joking, thanking, mourning, celebrating,
complaining and recounting **are** codeable when they are things people do together or to each
other.

Where something happens *between* people — an exchange, a call and its answer — code each turn
as its own passage and give them a shared `exchange_id`, so the interaction survives without
pretending it lives in one item.

### What a code looks like

*From an unrelated study of home-baking forums. This shows the shape of a code and implies
nothing about your community.*

> **the passage** — `"pulled it at 40 min like you said and the middle is still gummy, gonna
> blame the tin"`
>
> **1st-order** `blaming the tin for a gummy middle` — their words: *gummy*, *the tin*.
> Not `reporting a quality defect`, which is a category from outside, and not
> `expressing frustration`, which is not an action.

> **the passage** — `"we all say 40 min but nobody agrees what done even means here"`
>
> **1st-order** `saying nobody agrees what done means`

Those two codes, with a dozen others like them, later gather into **one theme** —
`working out what counts as done` — because that is what these people are doing, and they
have no single word for it, so the phrase is plain. The theme is neither code reworded, and
the two codes are not similar to each other at all.

**Account for everything you read in a selected thread.** Where a passage is not a practice it
still gets a code, in your own words, and you may make as many such codes as the material
needs — cluster the awkward material by *kind*; how you divide it is itself a reading. A
stretch you leave uncoded shows in the forest as `na` and is a choice a reader can see: leave
it when the words do nothing (a greeting, a signature, a quoted link), not to save time. Where a
commenter describes what is in an image or at a link, that description is citable as *what
that commenter said*, attributed to them, never as your own observation.

**A passage may carry more than one code** — two if it is doing two things or if you could not
settle on one, three if your reading is more diffuse than that. Do not also grade your
confidence; the labels are the grade.

### Anything the thread points at — one list, one line each

**In a thread you kept, every time the record points at something outside it, record it with
`emit.pointer` at the passage that names it.** Another subreddit, a Discord, a strawpoll, a Google
doc, a voice channel, another site — **one list**. A thread that names a Discord and a subreddit
gives you **two lines**, one each.

    emit.pointer(cited,                       # what cite() handed you: the words that name it,
                                              # and the item they sit in
                 raw="discord.gg/xxxx",       # verbatim — the r/, the invite link, the typo
                 normalised="discord",        # your reading, or None
                 kind="off_platform",         # subreddit | off_platform
                 relation="gave-help-to",     # for a subreddit; see the vocabulary below
                 moved="partial",             # did organising move there: yes | partial | no
                 what_still_returns="target images and a nightly summary",
                 what_you_cannot_see="the decision that set the target",
                 thread_id="zzzz01",
                 code_ids=["c0011"])

**Only from threads you kept.** A pointer inside a thread you recorded `out_of_scope` is refused.
This is a record of what these people pointed at *while doing the thing*, not of every link in the
room's week. That restriction is what makes the list countable: a denominator of kept threads,
rather than a search over everything.

**Give the words, not only the item id.** *An invite link in 6363ka* is a claim, and a reader has
to take it. The words themselves, with the item they sit in, are a reference somebody can go back to
and check. Going through `cite` means
there is no way to record a pointer on words that are not in the body. **If you cannot cite it, it
does not go here** — say it under §8's Saturation instead, because a venue you inferred is not a
venue you saw.

**`raw` verbatim and `normalised` separately, and do not silently correct.** A handle can reach
you with a character missing or a letter wrong, and you will not be able to tell whether the
participants wrote it that way or something before you dropped it. Correcting it in `raw` removes
the evidence that it happened; never reading it at all leaves one place recorded under two names.
Put the record in `raw` and your reading in `normalised`, and both questions — what was written,
and what you took it to mean — stay answerable afterwards.

**For a subreddit**, `relation` is one of `allied · attacked · attacked-by · asked-help-from ·
gave-help-to · negotiated · mourned · destroyed-carelessly · mentioned-only`. **`mentioned-only` is
a real value, not a fallback.** Do not judge whether the relation mattered — you are reading one
side and cannot see the other. Type it, quote it, move on. `moved` stays `no`.

**For somewhere the talk went**, `moved` and the two *what* fields are the ones that matter, and
`relation` can stay at its default. Answer them as well as you can now; if you only work it out
while writing §8, say it there and leave the field `None` — nothing is ever re-emitted.

**Pointing at nothing is a finding.** A community that organised without referring to anyone else
is a case, not a case with something missing from it. If that is yours, the absence of these lines
says so and you need do nothing.

Where the same thing is pointed at more than once, one line is enough: use the passage that shows it
best.

---

## 7. Step 4 — themes

Group your codes into themes, asking of each group: *what are these people doing?* Each theme
is gerund-led, concrete, bound to this case, passes the register test in Rule 6, and names
the doing and not how it came out: `asking r/tagpro for room`, not `asking r/tagpro for room
and taking no for an answer gracefully`. How it came out is §8's, with its passage.

A code that belongs with nothing else stands as its own theme. That is a legitimate outcome,
not a failure to consolidate.

**Assign every code to exactly one theme.** Grouping the codes once and finding that it holds
is a normal outcome. **Say so anyway, in one line**: whether you regrouped, and if you did not,
whether you went back and looked at the grouping again after §8. A blank `regrouped_from` cannot
be told from a coder who never looked twice, which is the one thing the field exists to show. Where you do regroup — splitting a theme,
merging two, lifting a code out of one and into another — record it on the theme itself in
`regrouped_from`, naming what it came out of and what made you separate them. That record is
how the reading you arrived at stays distinguishable from the reading you started with, and it
matters most when the thing that made you regroup was §8.

Every `code_id` resolves to exactly one `theme_id`, and every theme resolves downward to at
least one code — a theme with nothing under it is a theme you brought with you.

---

## 8. Step 5 — the within-case account

Into `case.md`:

**Use these headings exactly, as `##` lines and in this order:** `## Chronology`,
`## Relations — what set off what`, `## Posts against comments`, `## Counter-reading`,
`## Saturation`, and then §9's `## Selection`, `## Other communities named`, `## Absence`. What
reads your file finds each section by its heading, so **the wording of the heading is not yours to
improve** — everything under it is.

**Chronology.** What happened, in order: when the event first shows up, the episodes that
follow, how it ends inside your window. You supply the episodes: an episode is a stretch of
the coded threads you can name by what the room was doing, bounded by the ids of its first and
last item, and it may run across threads; what it rests on is the codes on those items, in the
forest, and nothing else. Counting is done for you.

**Relations.** What set off what — which practice is a response to which. A link needs a
passage in which the later turn answers, names or recalls the earlier one, or the same
speaker says so; cite it, one passage per link. Order alone — one thread after another, one
turn under another — is not a link: report it as *follows*, with the interval, and no more.
Say when the corpus does not show a link you expected.

**Posts against comments.** Do the two layers tell the same story? Log every contradiction
explicitly — *"the posts say X; the comment layer says Y"* — and where a claim lives in only
one layer, say which.

**Counter-reading.** State your one-sentence reading of this case.

**Then, before you search, write down what you would expect this corpus to contain if that
reading were wrong.** One or two sentences. Not what would be *missing* — what would be *there
instead*. Searching for the absence of something mostly returns nothing, and nothing reads like
agreement; searching for the presence of something contrary is a test your reading can actually
fail. Your reading is in your own words, so its opposite is too: nothing here comes from outside
this case, and if you find yourself reaching for a word these people never used, you have written
the wrong sentence.

Then use `find` to look for **that**, read what it returns, and record what you found — including
that you found nothing, if that is what happened. Call `emit.stage("step5_counter")` before you
start looking, so that anything this turns up is distinguishable from what you already had.

Both sentences go in `case.md`: the reading, and what would have unseated it.

**Saturation.** Does the record look whole — truncation, removals heavy enough to hide
practice, threads continuing where you cannot see, off-platform venues you can only glimpse?

**A venue this community moved to is conduct, not a gap.** If the talk went to a Discord, a
strawpoll, a Google doc, private messages or a voice channel, that is something these people *did*
— they chose where to organise and what would come back here — and it is coded like anything else
you can cite. Report it as incomplete evidence only for the part you genuinely cannot see. The
record of *which* venues is `pointers.jsonl`, emitted while you code — §6 — and the three questions
it asks about each one are answered best here, once you have read the thread whole.

Where the last genuinely new code fell in your reading is **computed from what you recorded**
and is not yours to state. Do not estimate it.

### The counter-reading can turn up material you have not coded

That is what it is for. **Code it.** Any code arising from the counter-reading carries
`discovered_at: "step5"`, and if a searched thread turns out to be about the event, say so —
`emit.thread` will not take it twice, so tell it in `notes.md` which thread changed and why.
Nothing already recorded is revised, and the disagreement stays visible.

If a late finding overturns your one-sentence reading, say so in `case.md`. Being wrong and
recording it beats a tidy account.

### The verdict

- **`full`** — this community's window shows practice around the event.
- **`trace`** — the event is mentioned but nobody is visibly doing anything about it. Code the
  mentions and stop there.
- **`none`** — nothing about the event at all. Say what the corpus does consist of and what
  you searched for before concluding it.

**All six outputs exist under every verdict.** A `none` verdict still records every thread
through `emit.thread`, with a cited line for every excluded thread of ten or more items you
read, and still has a `case.md` saying what the corpus was instead, and `notes.md`.

---

## 9. Outputs

**No minimum length and no maximum** — length is set by the material, not by a target.

**You do not write JSON.** Four of the six outputs are built by `emit` from calls you make
while working. You never open them, never format a line, and never compute a count.

**Both tools are objects you construct once, at the top of your first python call.** The
lines below are the whole setup; nothing else imports and nothing is global:

```python
import sys; sys.path.insert(0, "__RUNDIR__")
from emit import Emit
from cite import Corpus

emit = Emit("__OUTDIR__", corpus_path="__RECORD__")
_c = Corpus("__RECORD__")
cite, find = _c.cite, _c.find      # cite(item_id, "…") and find("regex") from here on
```

Then, for the rest of the run:

```python
emit.stage("step3_codes")                  # before each step. that is all it needs.
                                           # step1_brief step2_read step3_codes
                                           # step4_themes step5_counter step6_account
                                           # step7_write
# The seven names map onto the steps thus: step1_brief is §4; step2_read is §5; step3_codes
# is §6; step4_themes is §7; step5_counter is §8's search; step6_account is writing case.md;
# step7_write is writing notes.md. A fleet coder announces step6_account before its slice
# case and step7_write before its notes. discovered_at is stamped from the last name you
# announced, so announce the right one before you write.

emit.code(cited,                           # exactly what cite() handed you, unchanged
          "blaming the tin for a gummy middle",
          thread_id="zzzz01",
          exchange_id=None,                # or a shared id, for a call and its answer
          note="")                         # -> returns the code_id

emit.theme("<the case-bound theme label>",
           "why this theme exists",
           ["c0007", "c0011"],             # the codes under it
           regrouped_from=None)             # or: what it came out of, and why you split it

emit.retract("c0042", "emitted twice — a script re-run")
                                           # withdraw a code by APPENDING a retraction.
                                           # nothing is edited, nothing is deleted; the row
                                           # stays with retracted: true and your reason.

emit.theme_add("t03", ["c0042"])           # put a later code into a theme that exists. a code
                                           # minted after §7 does NOT have to found a new
                                           # theme — say where it belongs.

emit.thread("zzzz01",
            read="full",                   # full | triaged | unread
            verdict="out_of_scope",        # coded | out_of_scope
            reason="a running joke unrelated to the event",
            excluded_quote=None)            # what cite() returned, for a read out-of-scope
                                           # thread of ten IN-WINDOW items or more; None only
                                           # for unread or below-ten exclusions

emit.pointer(cited,                        # what cite() returned, unchanged
             raw="discord.gg/xxxx",        # verbatim; or "r/somewhere"
             kind="off_platform",          # subreddit | off_platform
             normalised="discord",         # your reading, or None
             relation="mentioned-only",    # subreddits; see §6
             moved="partial",              # yes | partial | no
             what_still_returns="...",
             what_you_cannot_see="...",
             thread_id="zzzz01",
             code_ids=["c0011"],
             note="")                      # -> returns the pointer_id.  §6.

emit.threads_bulk([{...}, {...}])          # the sweep below your stopping point, as one pass
```

Three things follow from this and are worth knowing rather than discovering.

**A retraction appends; it does not edit.** Rule 10 does not move — you revise nothing. But if you
emit something twice and notice, `emit.retract(code_id, reason)` is how you say so. The code stays
in the file with `retracted: true` and your reason beside it, so what happened is visible in
the file rather than lost in a note. Emitting the same thing twice is easy to do by running one
call twice; saying so is one line.

**`discovered_at` is not a parameter.** The harness stamps it from the last stage you
announced, so announce the right one and you are never asked to label a code yourself. It
reads `step3` for a code minted while reading, `step5` for one the counter-reading turned up,
and otherwise the name of whatever step you were in — a code you mint while writing the
account says so, rather than borrowing the credit of a discovery.

**A code belongs to exactly one theme, and `emit` refuses a second.** Every code must end up
under one; a theme with nothing under it is refused. You will be told at the end if a code is
still outside every theme.

**`text`, `start` and `end` come from `cite`, by construction.** Pass its return value straight
through. `emit` checks every quote against the record as it arrives and refuses one that is
not a slice of the item's body, an empty one, or one whose item is not in the thread you
named; the end-of-run checks verify them all again. The citation contract holds at the output
end as well as the input end.

`item_kind`, `author` and `created_utc` are read from the record and added to the code for
you.

**`case.md`** — §8, plus **Selection** (how you decided) · **Other communities named** (what this
community makes of the places it points at — *which* places, and where each was named, is
`pointers.jsonl` and is emitted at §6, so this section is for what you want to say about them and
nothing above you depends on how you format it; omit if none) · **Absence** (what the removals look
like and what the surviving replies still show).

**`notes.md`** — nothing in it is graded.
**What was hard** — the genuinely difficult passages, what was ambiguous, what you nearly
coded and did not, where their words defeated you. **Data problems.** **Anomalies and leads.**
**Complaints** — *be blunt.* What here was unclear, contradictory, or asked something you
could not sensibly do? What did you want and not have?

**Which two of your themes nearly merged, and what kept them apart?** One line. You are the only
one who knows where that boundary was, and nothing in the files can recover it.

**Which code would you defend hardest, and which is the thinnest you kept?** Two names, no
argument. Nothing else in the record carries that judgement.

**How the reading held up** — *this is a measurement we need, not a confession, and nothing here
counts against you.* Somewhere above some corpus size a reader stops holding all of what it has
read. The only way to find out where that point is, is to ask a reader who has just been there.
So tell us:

- whether you at any point worked from your **memory of a thread** rather than from what `read`
  served you;
- whether you went back to something **because you could not remember it**;
- whether earlier threads **went indistinct** while later ones stayed sharp — or the reverse;
- whether this run was **interrupted and resumed** (AGENT §4), and if so what you did to pick the
  reading back up;
- and **where** in the corpus each of those happened: a thread id, or roughly how far down.

**If none of it happened, say so.** A clear no is as useful as a yes, and is what makes the yeses
legible. `read` logs every re-read, so what you say here can be
checked against the log — you are asked because the log can say what you did and never what you
were doing, or why.

**Final message.** The community, your verdict, your two saturation statements, and anything
that blocked you. Nothing else — no counts, no files.

---

## 10. What you are given

The corpus, served by `read`, threads oldest first and items oldest first within each thread.
Nothing is sorted by size, by score or by anything else. A thread has to be readable as the
thing that happened, and a corpus as the week it happened in. Above each thread that
is longer than its triage window sits that window — the opening post's length, and the three
most-discussed top-level replies with the line each begins at — so you can reach the substance
of a long thread without anyone reordering it. Item bodies byte-identical to the collected record. Real usernames and ids.
Threads whole and in order; where a thread's opening post falls outside your window it is
included and marked, so everything you may quote is in your corpus and `cite` can find all
of it.

**`read.header()` returns a block of `#` lines.** Item and thread counts, the day-by-day
activity histogram, every author with their item count and first and last appearance, the
full thread index with cumulative text share, whether every reply's parent is present, how
many bodies are `[deleted]`, and which accounts look automatic. It is all exact, it was
computed before you arrived, and it is the first thing in the file.

Thread sizes appear twice wherever the two differ: all characters, and characters written by
people. The second is the real one.

Counting, timing, language, participation, the phase of every passage, and the verification
of every quote are done for you. **Do not recompute any of it.** If you find yourself about
to write a script that counts, groups, sorts by date, or converts a timestamp, the answer is
already in the header — and if it genuinely is not there, say so in `notes.md` rather than
computing it, because that is a defect in the harness and someone needs to know.
