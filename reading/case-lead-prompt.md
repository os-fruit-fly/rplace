# Reading copy: case-lead-prompt

Links below are resolved against commit `7c788ae58ce0d4ae171d65e7550cf55b83a22624`. Source wording is unchanged; Markdown formatting may differ. [Exact source bytes](../sources/case-lead-prompt.md), SHA-256 `72b66473307467a8cf1dadfcada45bcf164a4139f53db4c374cc249839d3858a`. [Source and link manifest](manifest.json). Repository links open the public research repository at this commit.

---

# Case-lead prompting

Version: `lead-calibration-v2`\
Date: 2026-09-08\
Applies to: new case-lead runs under instrument v31; the compatible checklist also applies to v30 repairs\
Model for this wave: `gpt-5.6-sol`, reasoning effort `medium`

## Purpose and authority

This document records the additional prompting authorised after review of the Dorset demonstration. The research contract is unchanged. The additional message asks the lead to apply the existing consolidation, register, within-case account and counter-reading requirements more fully. It introduces no target number of themes, searches or codes, and no requirement that another model reproduce a previous reader's interpretation.

The scheduler appends the exact block below to the normal opening message printed by `_tools/room.py message lead`. The normal role contract and branch-specific workflow still apply. In branch B, the same lead retains this instruction through its saved conversation; collection and finish messages preserve the prescribed order. Fleet coders receive the normal coder message and their existing contracts.

The text outside the marked block is documentation for the scheduler, not extra material for the case lead to read. No Dorset output, comparison reading or reviewer interpretation is supplied to a new room's lead.

## Exact additional message sent to the lead

<!-- BEGIN LEAD PROMPT -->

Additional case-lead calibration: lead-calibration-v2.

Apply the supplied contracts unchanged. Pay particular attention to these existing requirements when you reach their prescribed stages:

1.  Consolidation (§7). Compare what codes in different exchanges are doing in common. Shared vocabulary or reply adjacency alone does not establish a shared practice. For each theme, explain the practice that holds its codes together and what varies within it. Keep labels concrete, gerund-led and in participants' words or ordinary language. Keep a single-code theme when that code belongs with nothing else; there is no target number or size of themes. In branch B, do this incrementally in the prescribed slice order, opening and extending themes as the contract says. Record the required grouping review and any regrouping through the instrument.

2.  Within-case findings (§8). State the patterns, differences and developments the supplied evidence supports, with their passages. Make the account useful to a reader who has not seen the threads. Distinguish a descriptive contrast, a participant's own explanation and a supported causal relation. Different speakers can express contrasting positions without establishing that the community changed its mind. Keep the contract's strict evidence requirement for a relation; state an observed sequence as a sequence when no causal link is supported. Make each qualification specific to the claim it limits. Preserve all required headings.

3.  Counter-reading (§8). Before searching, state a plausible competing account and what would be present if your reading were wrong. Test the most consequential alternative supported by this case's vocabulary. Read the returned items through the prescribed tools, name the strongest contrary item, and explain what changes or survives. There is no query-count quota. Report null results with their scope; a small or partial record limits what absence can establish. Follow the existing rules for late codes and append-only records.

4.  Checkable citations. In the case account, put each cited item or thread ID individually in backticks, including both endpoints of an episode. Give the supporting words as the contract requires. Use the instrument's measurements for times and intervals. Textual citations must be readable by the yard's checker.

5.  Complete-record check. Before the final message, check the complete run rather than only the last named defect. Every thread disposed as `coded` must retain at least one live code. Every read `out_of_scope` thread with ten or more in-window items must carry the exact exclusion citation returned by the instrument. In branch B, `notes.md` must include the literal line `branch B; threshold N; items_in_window N; chars_by_people N`, with the values copied from `_gate.json`. Under v31, run `python3 close_run.py . --role lead --preflight`, repair every failure, and rerun it until it passes. Under a v30 repair, where `--preflight` does not exist, perform this checklist explicitly and leave final validation to the scheduler.

Read the instructions completely before acting. Request long files in bounded sections and recover any clipped section. When find returns matches, inspect and read the matching items rather than treating its hit count as the result. Keep required working files and record difficulties in notes as the contract specifies.

These instructions add no case evidence or interpretive categories. Resolve any apparent conflict in favour of the supplied research contract and report it.

<!-- END LEAD PROMPT -->

## Delivery and evidence

For each run the scheduler saves the complete assembled opening message, this document's version and SHA-256, and the exact message SHA-256 in the lead store's `state/` directory before launching the lead. Those files become part of its next completed-turn filesystem checkpoint. The complete native transcript records what the lead actually received. A copy of the prompting receipt accompanies the room's validation documents. Contract and instrument hashes remain independently checked.

The native runner also supplies its existing lifecycle instruction: work only in this run directory, launch no agents, finish foreground commands before replying, leave no background process or persistent REPL state, keep working state in files, and do not inspect other rooms, native runtime files or checkpoint metadata. The exact lifecycle text and effective model settings are recorded in `STORE.json` and the native session. It is separate from the calibration above.

The scheduler checks the run mechanically after the agent ends. A case account in which the checker detects zero citations is flagged for attention; zero unknown IDs alone does not demonstrate that any citations were checked. Mechanical success does not certify the qualitative reading. The scheduler never edits an agent's account, codes, theme notes or journal to improve the result.

## Storage and continuation

The canonical reading and validation documents are published under `rooms/<community>/run/` and `rooms/<community>/validation/`. The source brief and record are preserved. The byte-identical run copy retains its original instrument paths and hash baselines; it is a review copy, not a relocated native conversation.

Only the case lead receives native conversation checkpoints. The complete store at `_lead_sessions/<run-name>/` remains at its original absolute path for continuation and forks. Every completed lead reply is checkpointed after the runtime exits. Fleet coders retain their outputs and transcripts, without a resumable native session. In branch B, the last collection stops before consolidation and is saved as `after-fleet`; the separate finish message then starts consolidation.

## Order and comparison

Continue with never-coded rooms whose briefs pass the current gate, smallest first. Previously coded rooms remain comparison material. Do not change the 500-item gate to force a branch. Keep the initial Dorset demonstration intact. Record new prompting as an explicit condition of new runs; a calibrated run is distinguishable from the earlier uncalibrated demonstration.

GPT-5.6 is run here with the explicit model ID `gpt-5.6-sol` at `medium` effort. OpenAI's model page identifies this as the target of the `gpt-5.6` alias: <https://developers.openai.com/api/docs/models/gpt-5.6-sol> (checked 2026-09-07). The methodological calibration above comes from the supplied v31 contracts and the user's approved review discussion, rather than a model-specific research method.
