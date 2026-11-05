#!/usr/bin/env python3
"""Stage 0 — fetch the two public sources and build ./inputs from scratch.

Run this on a machine with no data at all and it produces everything
build_artwork_flow.py needs:

    python3 pixels-per-artwork/code/fetch_sources.py     # from data/; ~900 MB download, ~5 min
    bash pixels-per-artwork/run_all.sh                   # writes pixels-per-artwork/data/

REPOSITORY LAYOUT.  The record is kept in data/pixels/ and the atlas is the
copy in data/atlas/atlas_2017.json, the one the v38 run used. Each is
downloaded only if absent, and neither is deleted afterwards: users/
build_worklist.py reads the same record. `bash pixels/get_pixels.sh` fetches
the record too.

ROW ORDER.  Timestamps are whole seconds, so almost every row ties with
another, and the two releases order ties differently. The study parsed the
aperiodic file, whose lines are sorted as text: by time, then hashed name, then
the rest of the line. This script sorts the archive.org copy the same way
before saving, so pixel_record.npz holds the study's order exactly (checked
2026-09-26: every array equal). Without the sort, repaints, reverts and
restorations move by a few hundred and the panel differs.

Needs numpy and Pillow; uses pandas if present and falls back to the csv module
if not. Around 1.5 GB of free disk while it works.

WHAT IT FETCHES

1. The placement record — `2017/place_tiles_sha1.csv` from the Internet Archive
   item `official-rplace-dataset-2017-2022` (894 MB, headerless,
   `ts_ms,username_sha1_b64,x,y,color_index`). This is the release that carries
   SHA-1 username hashes, which is the one the whole C4/C5 line of work is built
   on. The sibling `2017/place_tiles.csv` in the same item is a DIFFERENT
   release — it has a header, ISO timestamps, MD5-style hashes and rows with
   empty coordinates. Do not substitute it.

   A second mirror exists at
   `https://static.aperiodic.net/place/original_tile_placements.csv.xz`
   (same content, xz-compressed, ~180 MB). On 2026-09-26 that host's TLS
   certificate was expired, so it is offered behind `--source aperiodic` rather
   than used by default. `newer_tile_placements.csv.xz` on the same host is a
   later release with 16,567,567 rows and will fail this script's assertions.

2. The atlas — `web/atlas.json` from `github.com/placeAtlas/atlas-2017`
   (675 KB, 1,473 entries, one time period each).

WHAT IT CHECKS, and refuses to proceed without

    16,559,897  rows in the record
     1,166,924  distinct placers
    16,556,641  rows with 0 <= x,y < 1000  (3,256 dropped)
         1,473  atlas entries, 1,236 with a subreddit link
       956,741  canvas pixels inside >= 1 polygon
     1,319,701  pixel-artwork memberships
    final canvas fingerprint 6017455b06eea6bac1e505d79a0e3e06

The fingerprint is sha256 of the 1,000,000-byte final-colour array, built with a
DETERMINISTIC tie-break (lexsort on pixel, then time, then colour). The
tie-break matters: 241 pixels receive two different colours in the same final
millisecond, so without one, two orderings of the identical record disagree on
up to 241 pixels. With it, this fetch was verified on 2026-09-26 to reproduce
the project's own preserved parse exactly.

PLACER IDS.  `placer_uid` is only an index into `placer_hashes.txt.gz`. The
study numbered placers by a 64-bit key of each hash (the first 16 characters
folded with two constants, as in C4's parse), ascending; with no file present
this script numbers them the same way and writes the file, so ids equal the
study's (checked 2026-09-26: all 1,166,924). An existing file is reused as is.
"""
import argparse, csv, gzip, hashlib, io, json, os, sys, time, urllib.request
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                        # data/pixels-per-artwork
DATA = os.path.dirname(ROOT)                        # data/
INP = os.path.join(ROOT, "inputs")
PIXELS = os.path.join(DATA, "pixels")               # the record lives here
ATLAS_FILE = os.path.join(DATA, "atlas", "atlas_2017.json")

ATLAS_COMMIT = "fb730258dd35766860804674f719dec6335625a4"   # web/atlas.json here = the run's atlas
ATLAS_SHA256 = "40a93f67dc55287812b66c0b3cdf2fb93980e2232fb0b3631e744a3550903b26"
ARCHIVE_CSV = ("https://archive.org/download/official-rplace-dataset-2017-2022/"
               "2017%2Fplace_tiles_sha1.csv")
APERIODIC_XZ = "https://static.aperiodic.net/place/original_tile_placements.csv.xz"
ATLAS_URL = "https://raw.githubusercontent.com/placeAtlas/atlas-2017/%s/web/atlas.json" % ATLAS_COMMIT

N_ROWS, N_PLACERS, N_INRANGE = 16_559_897, 1_166_924, 16_556_641
N_ART, N_ART_SUB, N_COVERED, N_MEMB = 1473, 1236, 956_741, 1_319_701
FINAL_FP = "6017455b06eea6bac1e505d79a0e3e06"


def fetch(url, dest):
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        print("  cached: %s (%d B)" % (os.path.basename(dest), os.path.getsize(dest)))
        return dest
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    print("  GET %s" % url, flush=True)
    t0 = time.time()
    tmp = dest + ".part"
    with urllib.request.urlopen(url, timeout=120) as r, open(tmp, "wb") as f:
        n = 0
        while True:
            b = r.read(1 << 22)
            if not b:
                break
            f.write(b); n += len(b)
            if n % (1 << 26) < (1 << 22):
                print("    %d MB" % (n >> 20), flush=True)
    os.replace(tmp, dest)
    print("  -> %s  %d B  %.0fs" % (os.path.basename(dest), os.path.getsize(dest),
                                    time.time() - t0))
    return dest


def rows(path):
    """Yield (ts, hash_bytes, x, y, colour) chunks as arrays, bounded memory."""
    opener = (lambda p: __import__("lzma").open(p, "rt")) if path.endswith(".xz") else \
             (lambda p: open(p, "r", newline=""))
    try:
        import pandas as pd
        for ch in pd.read_csv(path, header=None, names=["ts", "h", "x", "y", "c"],
                              dtype={"ts": np.int64, "h": "string",
                                     "x": np.int32, "y": np.int32, "c": np.int16},
                              chunksize=2_000_000,
                              compression="xz" if path.endswith(".xz") else None):
            yield (ch.ts.values, ch.h.values.astype("S28"),
                   ch.x.values, ch.y.values, ch.c.values.astype(np.uint8))
        return
    except ImportError:
        pass
    with opener(path) as f:                     # pandas-free fallback
        rd = csv.reader(f)
        T, H, X, Y, C = [], [], [], [], []
        for r in rd:
            T.append(int(r[0])); H.append(r[1].encode())
            X.append(int(r[2])); Y.append(int(r[3])); C.append(int(r[4]))
            if len(T) == 2_000_000:
                yield (np.array(T, np.int64), np.array(H, "S28"), np.array(X, np.int32),
                       np.array(Y, np.int32), np.array(C, np.uint8))
                T, H, X, Y, C = [], [], [], [], []
        if T:
            yield (np.array(T, np.int64), np.array(H, "S28"), np.array(X, np.int32),
                   np.array(Y, np.int32), np.array(C, np.uint8))


def build_record(path):
    t0 = time.time()
    existing = os.path.join(INP, "placer_hashes.txt.gz")
    lookup = None
    if os.path.exists(existing):
        with gzip.open(existing, "rt") as f:
            hs = [l.rstrip("\n").encode() for l in f]
        lookup = {h: i for i, h in enumerate(hs)}
        print("  reusing existing placer_hashes.txt.gz (%d ids stay stable)" % len(hs))
    TS, X, Y, C, U = [], [], [], [], []
    seen = {} if lookup is None else lookup
    nxt = len(seen)
    for ts, h, x, y, c in rows(path):
        uid = np.empty(h.size, np.int32)
        for i, hh in enumerate(h.tolist()):
            v = seen.get(hh)
            if v is None:
                if lookup is not None:
                    raise SystemExit("hash %r absent from placer_hashes.txt.gz -- "
                                     "delete it to rebuild ids from scratch" % hh)
                v = seen[hh] = nxt; nxt += 1
            uid[i] = v
        TS.append(ts); X.append(x.astype(np.int16)); Y.append(y.astype(np.int16))
        C.append(c); U.append(uid)
        print("    parsed %d rows  %.0fs" % (sum(a.size for a in TS), time.time() - t0),
              flush=True)
    ts = np.concatenate(TS); x = np.concatenate(X); y = np.concatenate(Y)
    c = np.concatenate(C); u = np.concatenate(U)
    del TS, X, Y, C, U
    # the study's order: the lines sorted as text (time, hashed name, "x,y,colour")
    hs = sorted(seen, key=seen.get)             # uid -> hash, in uid order
    hrank = np.empty(len(hs), np.int64); hrank[np.argsort(np.array(hs), kind="stable")] = np.arange(len(hs))
    tail = np.char.add(np.char.add(np.char.add(np.char.add(
        x.astype("U5"), ","), y.astype("U5")), ","), c.astype("U3"))
    trank = np.unique(tail, return_inverse=True)[1].ravel()
    o = np.lexsort((trank, hrank[u], ts)); del tail, trank
    ts, x, y, c, u = ts[o], x[o], y[o], c[o], u[o]
    assert ts.size == N_ROWS, "expected %d rows, got %d" % (N_ROWS, ts.size)
    assert len(seen) == N_PLACERS, "expected %d placers, got %d" % (N_PLACERS, len(seen))
    if lookup is None:                          # the study's order: by a 64-bit key of the hash
        hs = sorted(seen, key=seen.get)         # hash bytes, in first-seen id order
        b = np.frombuffer(b"".join(hs), np.uint8).reshape(len(hs), 28)
        a1 = np.ascontiguousarray(b[:, 0:8]).view(np.uint64).ravel()
        a2 = np.ascontiguousarray(b[:, 8:16]).view(np.uint64).ravel()
        key = (a1 * np.uint64(0x9E3779B97F4A7C15)) ^ (a2 * np.uint64(0xC2B2AE3D27D4EB4F))
        order = np.argsort(key, kind="stable")  # new id -> first-seen id
        remap = np.empty(len(hs), np.int32); remap[order] = np.arange(len(hs), dtype=np.int32)
        u = remap[u]
        with gzip.open(existing, "wt", compresslevel=6) as f:
            f.write("\n".join(hs[i].decode() for i in order))   # no final newline, as the study's
        print("  wrote placer_hashes.txt.gz in the study's id order")
    ok = (x < 1000) & (y < 1000)
    assert int(ok.sum()) == N_INRANGE, "expected %d in range, got %d" % (N_INRANGE, ok.sum())
    pid = (y[ok].astype(np.int64) * 1000 + x[ok])
    o = np.lexsort((c[ok], ts[ok], pid))        # pixel, time, colour -- deterministic
    p = pid[o]; cc = c[ok][o]
    uq, first = np.unique(p[::-1], return_index=True)
    st = np.zeros(1000000, np.uint8); st[uq] = cc[::-1][first]
    fp = hashlib.sha256(st.tobytes()).hexdigest()[:32]
    assert fp == FINAL_FP, "final-canvas fingerprint %s != expected %s" % (fp, FINAL_FP)
    print("  fingerprint %s  OK" % fp)
    np.savez_compressed(os.path.join(INP, "pixel_record.npz"),
                        x=x, y=y, ts_ms=ts, color=c, placer_uid=u)
    print("  pixel_record.npz written  %.0fs" % (time.time() - t0))


def build_atlas(path):
    from PIL import Image, ImageDraw
    got = hashlib.sha256(open(path, "rb").read()).hexdigest()
    assert got == ATLAS_SHA256, "atlas sha256 %s != the run's %s" % (got[:16], ATLAS_SHA256[:16])
    d = json.load(open(path))
    assert len(d) == N_ART, "expected %d atlas entries, got %d" % (N_ART, len(d))
    nsub = sum(1 for e in d if e.get("links", {}).get("subreddit"))
    assert nsub == N_ART_SUB, "expected %d entries with a subreddit, got %d" % (N_ART_SUB, nsub)
    memb = [[] for _ in range(1000000)]
    area = np.zeros(N_ART, np.int32); out = []
    for i, e in enumerate(d):
        pts = [(float(a), float(b)) for a, b in list(e["path"].values())[0]]
        im = Image.new("1", (1000, 1000), 0)
        if len(pts) >= 3:
            ImageDraw.Draw(im).polygon(pts, fill=1)
        idx = np.flatnonzero(np.asarray(im, bool).ravel())   # row-major => y*1000+x
        area[i] = idx.size
        for j in idx:
            memb[j].append(i)
        subs = e.get("links", {}).get("subreddit", []) or []
        out.append(dict(artwork_id=i, name=e["name"], subreddits="|".join(subs),
                        n_subreddits=len(subs), area_px=int(idx.size),
                        n_vertices=len(pts),
                        center=" ".join(str(int(v)) for v in list(e["center"].values())[0])))
    deg = np.array([len(m) for m in memb], np.int8)
    assert int((deg > 0).sum()) == N_COVERED, "covered pixels %d != %d" % ((deg > 0).sum(), N_COVERED)
    assert int(deg.sum()) == N_MEMB, "memberships %d != %d" % (deg.sum(), N_MEMB)
    flat = np.concatenate([np.array(m, np.int16) for m in memb if m])
    ptr = np.zeros(1000001, np.int64); ptr[1:] = np.cumsum(deg)
    prim = np.full(1000000, -1, np.int16); best = np.full(1000000, np.iinfo(np.int64).max, np.int64)
    has = np.flatnonzero(deg > 0)
    for slot in range(int(deg.max())):
        sel = has[deg[has] > slot]; a = flat[ptr[sel] + slot]
        b = area[a].astype(np.int64) < best[sel]
        prim[sel[b]] = a[b]; best[sel[b]] = area[a][b]
    np.savez_compressed(os.path.join(INP, "atlas_membership.npz"),
                        memb_indices=flat, memb_indptr=ptr, artwork_area=area,
                        pixel_deg=deg, pixel_primary=prim)
    with open(os.path.join(INP, "artworks.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
    print("  atlas: %d artworks, %d covered pixels, %d memberships  OK"
          % (N_ART, N_COVERED, N_MEMB))


def manifest():
    man = {}
    for f in ("pixel_record.npz", "placer_hashes.txt.gz", "atlas_membership.npz", "artworks.csv"):
        p = os.path.join(INP, f)
        h = hashlib.sha256()
        with open(p, "rb") as fh:
            for b in iter(lambda: fh.read(1 << 22), b""):
                h.update(b)
        man[f] = {"bytes": os.path.getsize(p), "sha256": h.hexdigest()}
        print("  %-24s %12d B" % (f, man[f]["bytes"]))
    man["_sources"] = {"record": ARCHIVE_CSV, "atlas": ATLAS_FILE + " (else " + ATLAS_URL + ")",
                       "fetched": time.strftime("%Y-%m-%d")}
    json.dump(man, open(os.path.join(INP, "MANIFEST.json"), "w"), indent=1)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", choices=["archive", "aperiodic"], default="archive")
    a = ap.parse_args()
    os.makedirs(INP, exist_ok=True)
    print("1/4 record")
    if a.source == "archive":
        rec = fetch(ARCHIVE_CSV, os.path.join(PIXELS, "place_tiles_sha1.csv"))
    else:
        print("  NOTE: this host's TLS certificate was expired on 2026-09-26.")
        rec = fetch(APERIODIC_XZ, os.path.join(PIXELS, "original_tile_placements.csv.xz"))
    print("2/4 atlas")
    atl = fetch(ATLAS_URL, ATLAS_FILE)
    print("3/4 parse record")
    build_record(rec)
    print("    atlas")
    build_atlas(atl)
    print("4/4 manifest")
    manifest()
    print("\ninputs/ ready -- now run:  bash pixels-per-artwork/run_all.sh")
