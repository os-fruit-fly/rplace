# How to write, for the analyst

Target length: under 750 words. Read once at stage A1; again before a stage that ends in prose (C5, D5, D6, E1). It governs every sentence in your own words: notes, gates, accounts, briefs, the diary, questions, handbacks, final messages; not a quote (verbatim, through `cite.py`), an id, a field name or a count.

## Orwell's six rules (Politics and the English Language, 1946)

1. Never use a metaphor, simile, or other figure of speech which you are used to seeing in print.
2. Never use a long word where a short one will do.
3. If it is possible to cut a word out, always cut it out.
4. Never use the passive where you can use the active.
5. Never use a foreign phrase, a scientific word, or a jargon word if you can think of an everyday English equivalent.
6. Break any of these rules sooner than say anything outright barbarous.

Here: a figure of speech belongs to the participants, inside the quote marks; you add none. The passive hides who did what, and who did what is the finding: "r/sweden held the border", not "the border was held". The instrument's own words (third-order theme, gate, arrow, branch, adaptation) are defined; a word from the literature only after stage C3, as a declared construct; the rest in everyday English, in the participants' terms where the material has them.

## Signs of machine writing (Wikipedia, "Signs of AI writing", read 4 October 2026)

Each is a habit of language models, and each hides what the rooms did.

- **Inflated significance.** *stands as, a testament, pivotal, crucial, key, vital, underscores, highlights, reflects broader, enduring, landscape, tapestry, vibrant, robust, intricate, fostering, showcase, garner, valuable insights.* A room did something; say what and when.
- **The trailing clause of analysis.** A sentence ending in *..., highlighting*, *..., ensuring*, *..., reflecting*, *..., contributing to*. Cut it; a claim it carried gets its own sentence with its evidence, or goes.
- **Vague attribution.** *observers, experts, some, many, several, various, widely seen as.* Name the rooms and count them with their denominator (rules 5 and 6); where you cannot, the claim is thin and says so (rule 8).
- **Editorial asides.** *it is important to note, notably, worth noting, significantly, arguably, interestingly.* Cut.
- **Negative parallelism.** *not X but Y; not only X but also Y; it is not about X, it is about Y.* Say Y.
- **The rule of three by reflex.** Three adjectives, three examples, three clauses. Give the number the material has.
- **Copulas avoided.** *serves as, functions as, represents, boasts, features, offers* for *is* and *has*.
- **Hollow closers.** *In summary, in conclusion, overall*; a paragraph that restates; *challenges and future prospects*; *despite its ..., it faces challenges*.
- **Chat remnants.** *Certainly, I hope this helps, would you like, let me know, as an AI model, as of my last update.* Never in the record; a question goes through `mem.py ask`.
- **Stacked hedges.** One hedge where the uncertainty is real, with what would settle it.

## Shape and marks

- Headings in sentence case; no level skipped; no rules between sections.
- Bold for a defined term at its first use or a label the format asks for, never for emphasis; no list of bold labels with colons where a paragraph reads as prose. A list is for what a reader scans or compares, as here.
- No em dash and no en dash: a comma, a colon, a full stop or parentheses.
- Straight quotation marks. No emoji. No table where a sentence does.
- No contractions (house style), except let's.
- Vary sentence length. Two sentences or bullets in a row that open the same way: rewrite one.

## The record's own rules, restated

A quote is verbatim and resolves through `cite.py`; your words stay outside the quote marks. A count is of communities, with its denominator, from the file that governs (rules 4, 5, 19). A diary line says what you did and why, as you work; nothing about effort or feelings. A long file states its target length first and keeps to it. A thin claim is made and labelled thin (rule 8); *looked for and not found* is a result.

## Before a close

`python3 tools/prose_check.py out/<file>.md` lists the watch words above with their lines and decides nothing; the close-check does not read prose. What to fix is your judgment, rule 6 included.
