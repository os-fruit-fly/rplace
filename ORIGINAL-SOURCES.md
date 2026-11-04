# Where restored files come from

Target length: under 450 words.

The default launch command uses the original GitHub record wherever a checkpoint has an original-source recipe. The checkpoint card links to the exact commit and its file-by-file recipe. A moving branch is never the source.

## Two sources, one saved state

1. **Original GitHub files.** Git fetches the recorded commit from `the research repository`. For aggregator checkpoints, this includes the main conversation and the matching research files. Community coding files come from the unchanged `materials.tar.zst` and `run.tar.zst` archives at their original repository paths, or from the regular files beside them.
2. **Declared supplements.** Files absent from that commit, or saved before their published version changed, come from an existing verified checkpoint archive. These include runtime state, unpublished conversation history and community R6 outputs. Community native conversations come from their saved-session archives, not Git-tracked transcripts. The recipe names each exception and its reason.

The supplement cannot replace a failed Git fetch or a mismatched original file. Restoration stops instead. Every restored file must match the accepted checkpoint's SHA-256, size and permissions. Directory modes, internal links and native session identity are checked too. The existing native interview proof applies to that exact saved state. Restoration makes no model call.

Existing supplement archives can contain files that Git also supplies. The launcher reads only the declared exceptions from them. This keeps the existing archives intact, but still downloads the whole supplement. It does not claim that all saved bytes were originally committed to Git.

## Setup and evidence

Use Git and Python 3.11 or newer. While the repository is private, install GitHub CLI and sign in with `gh auth login`, using an account with repository access. The launcher uses that login without copying credentials into the interview. Community archives also need:

```bash
python3 -m pip install zstandard
```

The exported interview records the source commit, supplement hash and restore route. The private session folder holds the same receipt and Git transfer log. New replies remain private.

The verified bundle download remains an explicit alternative. Add `--bundle /path/to/bundle.tar.gz` to choose it. The export records that choice. There is no automatic switch to the bundle after an original-source failure.

End the interview to remove its disposable restoration. Cached downloads remain in the private interview home's `cache` folder. Source archives and GitHub records are never deleted by restoration.
