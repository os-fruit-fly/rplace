#!/usr/bin/env bash
# Download one r/place checkpoint archive from the review release, check its SHA-256,
# unpack it and run its resume.sh. Usage: bash get-checkpoint.sh <archive name>
# The archive name is shown on the checkpoint's Chat Locally panel, e.g. aggregator-A1b-55.
set -euo pipefail
name="${1:?Give the archive name shown on the checkpoint page, e.g. aggregator-A1b-55}"
base="${RPLACE_RELEASE_BASE:-https://github.com/os-fruit-fly/rplace/releases/download/checkpoints-review-20261104}"
dir="${RPLACE_CHECKPOINTS:-$HOME/rplace-checkpoints}"
if ! command -v python3 >/dev/null 2>&1 || ! python3 -c 'import sys; raise SystemExit(sys.version_info < (3, 11))'; then
  echo "Python 3.11 or newer is needed. Install it, then run the same command again." >&2; exit 1
fi
mkdir -p "$dir"; cd "$dir"
if [ -x "$name/resume.sh" ]; then echo "Already unpacked in $dir/$name."; exec "./$name/resume.sh"; fi
curl -fsSL "$base/MANIFEST.json" -o MANIFEST.json
python3 - "$name" <<'PY' > "$name.parts"
import json, sys
archives = {a['name']: a for a in json.load(open('MANIFEST.json'))['archives']}
a = archives.get(sys.argv[1])
if a is None:
    sys.exit('Unknown archive: ' + sys.argv[1] + '. Copy the name from the checkpoint page.')
print(a['sha256'], a['bytes'])
for part in a['parts']:
    print(part)
PY
read -r sha size < "$name.parts"
python3 -c 'import shutil,sys; free=shutil.disk_usage(".").free; need=3*int(sys.argv[1]); sys.exit(f"Need about {need/1e9:.0f} GB free here; {free/1e9:.0f} GB is free." if free<need else 0)' "$size"
: > "$name.tar"
tail -n +2 "$name.parts" | while read -r part; do
  echo "Downloading $part ..."
  curl -fL --retry 3 "$base/$part" -o "$part.download"
  cat "$part.download" >> "$name.tar"; rm -f "$part.download"
done
python3 - "$name.tar" "$sha" <<'PY'
import hashlib, sys
h = hashlib.sha256()
with open(sys.argv[1], 'rb') as f:
    for block in iter(lambda: f.read(1 << 20), b''):
        h.update(block)
if h.hexdigest() != sys.argv[2]:
    sys.exit('The download does not match its SHA-256. Run the same command again.')
print('SHA-256 matches.')
PY
tar -xf "$name.tar" && rm -f "$name.tar" "$name.parts"
exec "./$name/resume.sh"
