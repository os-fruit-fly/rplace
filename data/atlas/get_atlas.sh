#!/usr/bin/env bash
# get_atlas.sh: the 2017 atlas, into data/atlas/atlas_2017.json. Public, no key.
#   bash atlas/get_atlas.sh              (from data/)
# The atlas is a POINTER: which subreddits an artwork names, and its outline. Its name and description
# fields are one annotator's words and never enter the coding.
# Pinned to the placeAtlas/atlas-2017 commit whose web/atlas.json is the copy the v38 run used;
# the script checks the download against that copy's SHA-256 (SHA below) and stops if the bytes differ.
set -euo pipefail
cd "$(dirname "$0")"
C=fb730258dd35766860804674f719dec6335625a4
SHA=40a93f67dc55287812b66c0b3cdf2fb93980e2232fb0b3631e744a3550903b26
[ -s atlas_2017.json ] || curl -fL -o atlas_2017.json "https://raw.githubusercontent.com/placeAtlas/atlas-2017/$C/web/atlas.json"
python3 -c "import hashlib,sys; h=hashlib.sha256(open('atlas_2017.json','rb').read()).hexdigest(); sys.exit(0 if h=='$SHA' else 'atlas_2017.json is not the run\'s atlas: sha256 '+h[:16])"
echo "atlas ready: $(pwd)/atlas_2017.json, 1,473 entries, the run's copy"
