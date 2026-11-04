# Checkpoint interview runtime

Target length: under 1,000 words. Python 3.11 or newer. Native Codex or Claude CLI, authenticated on the interview operator's account. Separate from research controllers.

For the original GitHub restore route and its explicit saved-state supplements, see [Original sources](ORIGINAL-SOURCES.md).

## Reader route

Download and extract the website's interview launcher, or use a repository clone. From its root folder, log in once in a separate interview home:

```bash
python3 -m website.interview login codex
# Or, for Claude checkpoints:
python3 -m website.interview login claude
```

Use the command shown on an admitted checkpoint card:

```bash
python3 -m website.interview launch CHECKPOINT_ID
```

By default, the launcher retrieves pinned original GitHub files and the declared saved-state supplement, verifies every member, and opens a private local page. With `--bundle`, it verifies the supplied bundle instead. It sends no model prompt until you submit a question. A native fork preserves the saved conversation; historical files are read-only. A missing session, mismatched runtime or failed restoration stops the interview. There is no fresh-agent fallback.

For an already downloaded bundle, append `--bundle /path/to/bundle.tar.gz`. This uses the same identity and hash checks. The explicit offline bundle route needs no GitHub access after the bundle is supplied. The default original-source route requires GitHub access while its sources are private.

A transcript-only card cannot be launched. Original research commands in old manual pages do not establish a matching historical filesystem.

## Operator route

Both routes use the same verifier and backends. Start the private service after admitting bundles:

```bash
python3 -m website.interview serve --port 8776
```

It binds to loopback only. For phone access, put an authenticated HTTPS reverse proxy in front of it and pass its exact origin with `--origin https://YOUR-PRIVATE-HOST`. Keep access limited to J. The proxy must preserve that Host. The service also requires its generated private access token. Do not publish that token, a login home or an interview transcript. Configure `website/config.json` with the HTTPS origin only after testing it. The online action stays disabled until then.

The access token lives outside Git in `~/.rplace-interviews/access-token`. New tokens are generated on service start. Only admitted checkpoint files are served. Host, origin and token checks apply to all API operations; no research command endpoint exists.

New interviews are private and are not committed or included in website releases. Login and interview homes inside any Git checkout are rejected. Keep exported conversations outside repositories too. The repository ignores default export filenames and accidental copies of the interview home.

Claude uses only the separate interview login. On macOS, its access token is read from that login's Keychain entry and passed to the isolated child without saving a credential file. An expired or missing login stops the request. Research and default account settings are never used as a fallback.

One interview may be open at a time by default. Activity is visible under a collapsed disclosure. Export offers the new interview text and bundle hash. End stops the native process and removes the owned disposable workspace, including the copied credentials. The source bundle remains in the cache. Idle sessions expire after 30 minutes without a connected page. An interrupted server may leave an owned workspace; inspect and remove it before reopening, never resume it implicitly.

## Preparing a release

Use `python3 -m website.prepare --help` to convert a closed Claude checkpoint, an Atlas case-lead store, or a sealed sibling R6 archive into a new, external staging directory. Sibling preparation requires the archive SHA-256 and `--runtime-receipt`, a JSON file with `cli_version` and `cli_sha256` verified against the closing runtime. A session's creation version may differ from its closing version. Preparation validates the saved files and boundary; it never fills gaps from the current research workspace. Links outside the archived workspace, chained links, credential filenames or missing evidence stop preparation. This is not a full review of file contents for public release.

Then:

```bash
python3 -m website.interview pack PREPARED METADATA.json BUNDLE.tar.gz
python3 -m website.interview verify BUNDLE.tar.gz --sha256 SHA256
```

Bundles use `rplace-interview-v1`, or `rplace-interview-v2` when a saved internal directory link is present. Both have a first-member manifest, historical `workspace/`, saved `native/` conversation, and `evidence/`. Version 2 records link targets and modes, creates links after verifying files, and refuses escapes or paths through links. Linux fixes symlink modes at 0777; other file modes and link targets remain exact. Older launchers refuse version 2 rather than omit links. Every file has size, mode and SHA-256. The manifest binds checkpoint ID, session, backend, model, effort, CLI version and source hash. No user login files or executable auto-installers are included.

Verify restoration and isolation before admission. Check a known historical fact and confirm reads outside the checkpoint and writes to research are denied. Save the proof's bundle hash and runtime version. Prefer the recorded runtime. A newer runtime needs a reviewed compatibility proof bound to this bundle and the new executable's SHA-256. The catalogue displays both versions. A mismatch without that proof stops the interview; the historical manifest stays unchanged.

Interview instructions disable historical research gateways and use direct, read-only access to restored files. They do not change the archived contract. This prevents an interview from trying to call the old research broker.

Publish large bundles as GitHub Release assets, not repository blobs. Keep the SHA-256 and proof in the catalogue. `python3 -m website.admit --help` validates the receipt and adds an HTTPS asset URL. Hosted admission is a separate flag, set only after testing the private service. Public bundles can contain Reddit text and usernames; review credentials and publication rights before release.

No bundles are automatically published or admitted by the website build. Unavailable checkpoints stay labelled.
