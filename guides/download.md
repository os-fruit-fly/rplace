# 1. Open the collection handler

The data scripts and their READMEs: [data/](https://github.com/os-fruit-fly/rplace/tree/main/data) in this site's repository.

Open a new Codex or Claude chat that can work with files and a shell. Name it **Collection handler**. Use an empty working folder for this study. A chat without file or shell access cannot run the collection scripts.

[Download the collection handler brief](../agents/collection.md), attach it to the chat, then paste this prompt:

```text
You are the Collection handler for my r/place study. Read the attached Collection handler brief first. Obtain the instrument from the research repository into a separate working folder, record its version, and follow that brief and the repository's data recipes.

Help me choose between the archived study inputs and a fresh collection. Obtain and check the required raw24, pixel, atlas and other inputs. Ask only for missing access or research decisions. Keep your head and action log on disk. Leave a checked handoff for the existing coding handler. Do not start coding or aggregation.
```

The handler can download the instrument and data, so the folders need no assembly first. Credentials go in the provider's sign-in flow, never in the prompt.

## Get the instrument

Open the research repository, then choose **Code → Download ZIP**, or clone it if you use Git. The repository is public.

To use the original starting point, download the verified starting package and extract it in an empty folder. It holds the first instrument and the prepared run at commit `f6588ae37d807884af5fdcc9f7e27a03b4ff253a`, with no aggregator conversation. The archive SHA-256 is `1755f467ec0e2a3753a616b5eb19ccfa5b5e1af187a61ceef4ec449274a89b4c`. Give this folder to the existing aggregator handler to start from the prepared inputs. A new collection still begins with the collection handler.

The repository holds the instruments, scripts and recorded outputs. Large data stores and resumable checkpoint bundles are separate downloads. The interview launcher opens saved checkpoints and installs nothing of the research workflow.

Research runs need a computer with a shell, Python 3.11, the dependencies the package lists, and the model access your chosen platform requires. Each handler's instructions name the requirements of its own part. The starting package passed all eight offline checks in a fresh Python 3.11 environment on the author's Mac, with its documented numpy, scipy and pandas dependencies; the test used a simulated model. Provider access, recollection and installation on another operating system remain untested.

## Prepare the records

This step starts from the public pixel record, the atlas, the Reddit archives and the study's census decisions. Follow the collection recipes, keep the selected time window, then build each community's record. The census rests on judgments recorded in its files, and downloading the source data does not repeat them. Keep the prepared records, source versions, time window and census decisions. Move on when the recipes' checks pass and the inputs and versions are recorded.

The handler keeps the archived study inputs apart from a new collection. Some archived stores still have no published download link. A recollection can lose records removed since the study, so it may differ from the archived bytes. The handler records each such gap and substitutes no input without saying so.

## Open the next chat

The collection handler leaves `HANDOFF-collection.md` with input paths, versions, checks and unresolved gaps. Open the [coding handler](communities.html) and give it that file. Keep this collection chat for data questions.

## Documents for this handler

- [Collection handler brief](../agents/collection.html): the brief attached above, as a page.
- [Data recipes](../sources/data-README.html): how each input is obtained and checked.
- [Agent reading key](../agents/download.html): what the handler must read, in order.
