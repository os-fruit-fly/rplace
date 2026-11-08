---
kind: "handler-brief"
title: "Interview a saved checkpoint"
---

# Interview a saved checkpoint

Target length: under 600 words. Operational reading key, not permission to continue research.

## Choose and inspect

Select an exact ID in the [checkpoint catalogue](../interviews.html). Use **Read saved outputs** first to inspect selected narrative files without starting an agent. Each reading page names its checkpoint, original location, hashes and any known closure limitation. It does not contain the entire saved world.

Read the [interview guide](../guides/interviews.md), [runtime guide](../runtime.md), the selected entry in [catalog.json](../catalog.json), and its source recipe. Community coding close, local model, D2 and D3 are distinct milestones. Use recorded parent links; do not invent lineage.

## Start here

The checkpoint's Run on your computer button expands instructions on the same page. Its first Bash command downloads and verifies the launcher, prepares a private environment, checks access, requests missing sign-ins and opens the selected interview. Separate download, login and launch steps follow it. Use a Mac or Linux computer with Python 3.11 or newer and the supported native executable. The command does not install system tools or replace runtimes. Keep its private interview home outside every Git checkout.

For manual setup, download and extract the site's [launcher](../downloads/rplace-interviews.zip), check its [version and hash](../downloads/launcher.json), and follow its README.

## Pick an access route

| Route | Required access |
|---|---|
| Default command on the card | Git and GitHub CLI; the repository and supplements are public. Matching provider login and supported native runtime. Community archives also require `zstandard`. |
| Explicit `--bundle /path/to/bundle.tar.gz` | An already obtained, exact verified bundle, matching provider login and supported native runtime. This route does not fetch the original Git repository. |
| Hosted interview | A configured service and an admitted checkpoint. **Online: not enabled** means no hosted route exists for that card. |

The website cannot grant repository or provider access. Ask the study owner for access or an approved bundle if needed. A GitHub 404 while signed out does not establish that the saved files are missing. Localhost links work on the same computer, not a phone.

## Open and check

Use **Run on your computer** on the selected card. Paste its first command into Terminal, or follow the separate steps below it. The launcher verifies the source recipe or supplied bundle, saved file hashes, conversation identity and supported runtime. It refuses mismatches. Restoration alone sends no aggregator question.

The default route restores original GitHub files plus the explicitly declared saved-state supplement. [Original-source details](../ORIGINAL-SOURCES.md) explain the distinction. Do not silently fall back to another checkpoint, current workspace or fresh agent.

## Ask, export and stop

Ask about evidence, interpretation, alternatives or uncertainty. Answers are new interview responses. Check references against the saved files; verification does not establish scientific truth.

Export before **End and delete interview** if a copy is wanted. Keep exports outside Git. Ending removes disposable interview files, not the original checkpoint. Do not modify research, resume later stages or publish an interview under this task.

Stop and report the exact missing access, file, version or failed check. Do not treat a working help command, archive hash or website label as proof of a successful native interview.
