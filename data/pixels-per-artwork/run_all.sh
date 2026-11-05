#!/usr/bin/env bash
# Build everything from ./inputs into $1 (default ./data, where the study's aggregator handler,
# aggregator/handler/paths.py, looked for it; that handler is in the research repository, not here).
# About two minutes on an unconstrained machine.
set -euo pipefail
cd "$(dirname "$0")"
OUT="${1:-./data}"
mkdir -p "$OUT"
python3 code/build_artwork_flow.py assign   --out "$OUT"
# bodies is resumable; loop until it reports 1473/1473
for _ in 1 2 3 4 5 6 7 8 9 10; do
  LINE=$(python3 code/build_artwork_flow.py bodies --out "$OUT" --budget 11000000)
  echo "$LINE"
  case "$LINE" in *"artworks 1473/1473"*) break;; esac
done
python3 code/build_artwork_flow.py assemble --out "$OUT"
python3 code/build_artwork_flow.py index    --out "$OUT"
python3 code/build_artwork_flow.py panel    --out "$OUT"
echo
echo "done -> $OUT"
du -sh "$OUT" 2>/dev/null || true
