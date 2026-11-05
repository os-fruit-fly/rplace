#!/usr/bin/env python3
"""build_worklist.py: every placer account, as a list for the collector.

    python3 users/build_worklist.py [--tiles pixels/place_tiles_sha1.csv]
                                    [--hashes pixels/reddit-place-username-hashes/reddit-place-username-hashes.csv]
                                    [--out users/worklist.csv.gz]            (from data/)

Counts each account's placements in the tile dump (column 2, base64(sha1(username))), resolves the hash
to a username through opl's table, and writes one row per resolved account, most placements first, ties
by username: order, username, user_hash, placements_total. Hashes the table cannot resolve are counted
and reported, not written.

The study built its list in steps (W1: 87,903 accounts with 50 or more placements; then a recovery pass;
then the tail, to 1,101,801), and its collector's resume state is an index into that list. This script
writes the whole list at once; it holds the same accounts, and its order within a tie can differ.
"""
import argparse, collections, csv, gzip, lzma, os, sys

HERE = os.path.dirname(os.path.abspath(__file__)); DATA = os.path.dirname(HERE)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--tiles", default=os.path.join(DATA, "pixels", "place_tiles_sha1.csv"))
    ap.add_argument("--hashes", default=os.path.join(DATA, "pixels", "reddit-place-username-hashes",
                                                     "reddit-place-username-hashes.csv"))
    ap.add_argument("--out", default=os.path.join(HERE, "worklist.csv.gz"))
    a = ap.parse_args(argv)
    op = lzma.open if a.tiles.endswith(".xz") else open
    n = collections.Counter(); rows = 0
    with op(a.tiles, "rt", encoding="ascii", newline="") as f:
        for r in csv.reader(f):
            if len(r) < 5 or r[0] == "ts":
                continue
            n[r[1]] += 1; rows += 1
    name = {}
    with open(a.hashes, encoding="utf-8", newline="") as f:
        for r in csv.reader(f):
            if len(r) == 2:
                name[r[1]] = r[0]
    ok = [(c, name[h], h) for h, c in n.items() if h in name and name[h]]
    ok.sort(key=lambda t: (-t[0], t[1]))
    with gzip.open(a.out, "wt", encoding="utf-8", newline="") as f:
        w = csv.writer(f); w.writerow(["order", "username", "user_hash", "placements_total"])
        for i, (c, u, h) in enumerate(ok, 1):
            w.writerow([i, u, h, c])
    print("placements %d; accounts %d; resolved %d; unresolved %d (%d placements) -> %s" % (
        rows, len(n), len(ok), len(n) - len(ok), sum(c for h, c in n.items() if h not in name or not name[h]), a.out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
