#!/usr/bin/env bash
# get_pixels.sh: the pixel record and the username table, into data/pixels/. Public, no key.
#   bash pixels/get_pixels.sh            (from data/)
# 1. Reddit's 2017 record with SHA-1 name hashes, from archive.org: 16,559,897 rows, no header,
#    ts_ms,username_sha1_b64,x,y,color. Only this release's hashes are base64(sha1(username)).
#    Skipped if already here (pixels-per-artwork/code/fetch_sources.py fetches the same file).
#    The same rows, xz-compressed and sorted as text, were at static.aperiodic.net, whose
#    certificate had expired on 2026-09-26; do not use newer_tile_placements there.
# 2. opl's table of usernames and their hashes, 1,102,111 rows, no header: "username","hash".
set -euo pipefail
cd "$(dirname "$0")"
[ -s place_tiles_sha1.csv ] || curl -fL -o place_tiles_sha1.csv \
  "https://archive.org/download/official-rplace-dataset-2017-2022/2017%2Fplace_tiles_sha1.csv"
n="$(wc -l < place_tiles_sha1.csv | tr -d ' ')"
[ "$n" = 16559897 ] || { echo "expected 16,559,897 rows, got $n" >&2; exit 1; }
curl -fL -o reddit-place-opl-username-hashes.tar.xz https://archive.org/download/place2017-opl/reddit-place-opl-username-hashes.tar.xz
tar -xJf reddit-place-opl-username-hashes.tar.xz
n="$(wc -l < reddit-place-username-hashes/reddit-place-username-hashes.csv | tr -d ' ')"
[ "$n" = 1102111 ] || { echo "expected 1,102,111 username hashes, got $n" >&2; exit 1; }
echo "pixels ready: $(pwd)"
