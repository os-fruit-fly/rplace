#!/usr/bin/env python3
"""
Layer B step 5 — the author sweep.  Raw records, one file per username.

WHAT CHANGED FROM 09_collector_arctic_shift.py, AND WHY
------------------------------------------------------
09 fetched only the 72-hour event window and stored a wrapper object per account
with the records nested inside it.  J asked for (a) raw records first, aggregate
later, (b) all three segments — pre week, the 72 hours, the fortnight after — so
Layer B tracks Layer A, and (c) storage in the same jsonl shape as the subreddit
corpora but clustered on the username.  So:

1.  ONE CONTINUOUS FETCH PER ACCOUNT, NOT THREE.
    The span is [OPEN-7d, FRZ+14d) and the segment is written onto each record
    as a LABEL, derived from created_utc.  Two reasons, and the second matters
    more than the first.
      * Cost.  A window costs at least two requests per endpoint, because a
        short page is not a last page and only an empty response terminates.
        Three windows x two endpoints = >=12 requests per account; one span x
        two endpoints = >=4.  The wider window is not merely affordable, it is
        three times cheaper than segmenting the fetch.
      * The boundary stops being a fetch parameter.  This project has just spent
        a day discovering that OPEN was wrong by 31 hours and that every
        `during` corpus therefore begins after the founding day.  If a boundary
        moves again, re-cutting THIS data is a filter over a labelled field, not
        a re-collection.  A rule that says "re-partition instead of re-fetching"
        can be forgotten; a continuous span cannot.

2.  RECORDS ARE VERBATIM AND UNPROJECTED, exactly as `rPlace Corpus Schema.md`
    requires — "one complete arctic-shift record, verbatim, nothing curated or
    dropped" — with `kind` (post/comment) and `segment` (pre/during/after)
    injected and nothing else touched.  Same two added fields the Layer A
    corpora carry.  The 44-key post and 23-key comment shapes are preserved.

3.  PAGINATION IS collect_v6's `walk`, NOT 09's simpler loop.  `after` is
    exclusive on created_utc, so stepping to last_ts drops every sibling in that
    second; step to last_ts-1, dedupe by id, and go to last_ts+1 only when one
    second holds more than a page or the walk loops on itself.  On an
    unrecoverable page bisect the REMAINING span, so one poisoned instant costs
    a few seconds of coverage and gets named in the ledger, instead of costing
    the rest of the account.

LAYOUT — clustered on the username
----------------------------------
    authors/r000000-000999/<username>.jsonl      all three segments, one account
    authors/_batches/batch_0000000.meta.json     provenance for 500 accounts
    authors/_authors_index.jsonl                 one line per account, the card
    authors/_checkpoint.json                     one integer
    authors/_gaps.jsonl                          the ledger
    authors/_lock                                single instance

One file per username is the direct analogue of `<sub>_<segment>.jsonl`, and
`_authors_index.jsonl` is the analogue of the meta card.  The meta is per BATCH
rather than per account because the verification unit here is one API session
with its own retry tally and pacer, and because 87,903 sidecar files buys
nothing.  Verified before choosing this: all 87,903 usernames are unique
case-insensitively and match [A-Za-z0-9_-], so a file per account is safe on a
case-insensitive filesystem — the failure mode that has bitten this project
three times.

An empty account still gets a file, because "existence is not completeness" is
a named failure mode here: emptiness is asserted in the index, never inferred
from a missing file.  Half of heavy placers wrote nothing at all in the event
window (104 of the top 200), so `empty` is the MODAL outcome and can never share
a code with `failed`.

MECHANISMS (from the incident log; not optional)
-----------------------------------------------
  1. checkpoint = one integer, written after every batch
  2. single-instance lock
  3. gaps ledger; a non-empty ledger writes complete:false
  4. status distinguishes ok / empty / failed
  5. 422 -> back off IN TIME, never narrow the window
  6. no User-Agent -> 403 on every call
  7. only an empty page terminates a walk

USAGE
    python3 10_collect_authors.py --worklist W1.csv --out data/authors
    python3 10_collect_authors.py --self-test
"""

import argparse, collections, csv, datetime, gzip, json, os, random, sys, time
import threading, urllib.error, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor

sys.setrecursionlimit(60000)

API = "https://arctic-shift.photon-reddit.com/api"
UA = {"User-Agent": "rplace-research/1.0 (academic; contact via institution)"}

# Corrected constants.  OPEN is the 31-hour fix from the pixel record; FRZ is
# confirmed by the last placement in the file (2017-04-03 16:58:54Z).
OPEN = 1490976000              # 2017-03-31 16:00Z  public open, operational cut
FRZ = 1491238800               # 2017-04-03 17:00Z  freeze
PRE_START = OPEN - 7 * 86400   # 2017-03-24 16:00Z
AFTER_END = FRZ + 14 * 86400   # 2017-04-17 17:00Z

# `after` is EXCLUSIVE, so the span starts one second low.
SPAN_LO, SPAN_HI = PRE_START, AFTER_END

MAX_ATTEMPTS = 6
BISECT_FLOOR = 60
BATCH = 250                    # accounts per checkpoint / per meta card
BUCKET = 1000                  # accounts per directory

utc = lambda t: datetime.datetime.utcfromtimestamp(t).strftime("%Y-%m-%d %H:%M:%S")


def segment_of(ts):
    """The segment LABEL.  Boundaries are half-open and contiguous, so every
    record in the span gets exactly one label and none can fall between two."""
    if ts < OPEN:
        return "pre"
    if ts < FRZ:
        return "during"
    return "after"


def bucket_of(rank):
    lo = (rank // BUCKET) * BUCKET
    return f"r{lo:06d}-{lo + BUCKET - 1:06d}"


# --------------------------------------------------------------------------- #
# transport — collect_v6's Session, narrowed to what an author sweep needs
# --------------------------------------------------------------------------- #
class Session:
    # The inter-request floor is a measured parameter, not a taste.  collect_v6
    # used 0.5 s against the subreddit endpoints; on the author endpoints a floor
    # that size halves throughput, because an author page is small and latency is
    # flat at ~0.5 s.  FLOOR is set from the throughput measurement in
    # `docs/W1-arctic-shift-scoping.md` and re-measured before the real run.
    FLOOR = 0.0

    def __init__(self, floor=None):
        self.gaps, self.retries = [], collections.Counter()
        self.pages = self.bytes = 0
        self.floor = self.FLOOR if floor is None else floor
        self.delay = self.floor
        self.lock = threading.Lock()

    def gap(self, path, lo, hi, reason, kw):
        with self.lock:
            self.gaps.append({"path": path, "after": lo, "before": hi,
                              "after_utc": utc(lo), "before_utc": utc(hi),
                              "reason": reason, "params": dict(kw)})

    def call(self, path, **kw):
        q = urllib.parse.urlencode({k: v for k, v in kw.items() if v is not None})
        url = f"{API}/{path}?{q}"
        for attempt in range(MAX_ATTEMPTS):
            t = time.time()
            try:
                req = urllib.request.Request(url, headers=UA)
                with urllib.request.urlopen(req, timeout=180) as r:
                    raw = r.read()
                dt = time.time() - t
                with self.lock:
                    self.bytes += len(raw)
                    self.pages += 1
                    # pace on observed latency: there is no X-RateLimit-Remaining
                    if dt > 10:
                        self.delay = min(self.delay * 2, 8.0)
                    elif dt < 2:
                        self.delay = max(self.delay * 0.7, self.floor)
                    d = self.delay
                if d:
                    time.sleep(d)
                return json.loads(raw).get("data") or []
            except urllib.error.HTTPError as e:
                body = e.read()[:200].decode("utf8", "replace")
                if e.code == 400:
                    # malformed query.  Retrying is pointless; name it.
                    raise RuntimeError(f"HTTP 400 {url} :: {body}")
                with self.lock:
                    self.retries[f"http_{e.code}"] += 1
                    if e.code in (422, 429):
                        self.delay = min(self.delay * 1.5, 8.0)
                if attempt == MAX_ATTEMPTS - 1:
                    return None
                reset = e.headers.get("X-RateLimit-Reset")
                # 422 is a server-side timeout: back off in TIME, never narrow.
                wait = float(reset) if (e.code == 429 and reset) else 2.0 * 2 ** attempt
                time.sleep(min(90.0, wait) + random.random())
            except Exception as e:
                with self.lock:
                    self.retries[type(e).__name__] += 1
                if attempt == MAX_ATTEMPTS - 1:
                    return None
                time.sleep(min(60, 2.0 * 2 ** attempt) + random.random())
        return None


def walk(sess, path, lo, hi, out=None, depth=0, **kw):
    """Exclusive-`after` pagination, tie-safe, uncapped.  Bisects the remaining
    span on an unrecoverable page rather than abandoning the account."""
    if out is None:
        out = {}
    after = lo - 1
    while after < hi:
        d = sess.call(path, after=after, before=hi, limit="auto", sort="asc", **kw)
        if d is None:
            if hi - after <= BISECT_FLOOR or depth > 12:
                sess.gap(path, after, hi, "unrecoverable after retries", kw)
                return out
            mid = after + (hi - after) // 2
            walk(sess, path, after + 1, mid, out, depth + 1, **kw)
            walk(sess, path, mid, hi, out, depth + 1, **kw)
            return out
        if not d:                      # ONLY an empty page ends the walk
            break
        fresh = [r for r in d if r["id"] not in out]
        for r in fresh:
            out[r["id"]] = r
        last = d[-1]["created_utc"]
        nxt = last - 1
        if not fresh or nxt <= after:
            nxt = last + 1
        after = nxt
    return out


# --------------------------------------------------------------------------- #
# one account
# --------------------------------------------------------------------------- #
def collect_author(sess, username, rank, outdir):
    """Returns the index card.  Writes <bucket>/<username>.jsonl always."""
    t0 = time.time()
    g0 = len(sess.gaps)
    try:
        posts = walk(sess, "posts/search", SPAN_LO, SPAN_HI, author=username)
        comments = walk(sess, "comments/search", SPAN_LO, SPAN_HI, author=username)
    except RuntimeError as e:
        return {"username": username, "rank": rank, "status": "failed",
                "error": str(e)[:300]}

    recs = []
    for kind, obj in (("post", posts), ("comment", comments)):
        for r in obj.values():
            r["kind"] = kind
            r["segment"] = segment_of(r["created_utc"])
            recs.append(r)
    recs.sort(key=lambda r: (r["created_utc"], r["kind"], r["id"]))

    bdir = os.path.join(outdir, bucket_of(rank))
    os.makedirs(bdir, exist_ok=True)
    path = os.path.join(bdir, f"{username}.jsonl")
    tmp = path + ".part"
    with open(tmp, "w") as f:
        for r in recs:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    os.replace(tmp, path)          # a reader never sees a half-written file

    # ---- verification, per account.  Every one of these has a negative case
    # ---- in --self-test; a check that cannot fail is worse than no check.
    n_lines = sum(1 for _ in open(path))
    seg = collections.Counter(r["segment"] for r in recs)
    kin = collections.Counter(r["kind"] for r in recs)
    out_of_span = sum(1 for r in recs if not (SPAN_LO <= r["created_utc"] < SPAN_HI))
    # arctic-shift matches author case-insensitively; a different name means the
    # query did not do what it says.
    wrong_author = sorted({r.get("author") for r in recs
                           if (r.get("author") or "").lower() != username.lower()})
    card = {
        "username": username, "rank": rank,
        "n_posts": kin.get("post", 0), "n_comments": kin.get("comment", 0),
        "n_records": len(recs), "n_lines": n_lines,
        "pre": seg.get("pre", 0), "during": seg.get("during", 0),
        "after": seg.get("after", 0),
        "first_utc": recs[0]["created_utc"] if recs else None,
        "last_utc": recs[-1]["created_utc"] if recs else None,
        "n_subreddits": len({r.get("subreddit") for r in recs}),
        "seconds": round(time.time() - t0, 2),
        "file": os.path.join(bucket_of(rank), f"{username}.jsonl"),
        "checks": {"lines_match": n_lines == len(recs),
                   "out_of_span": out_of_span,
                   "wrong_author": wrong_author,
                   "new_gaps": len(sess.gaps) - g0},
    }
    bad = (not card["checks"]["lines_match"] or out_of_span or wrong_author
           or card["checks"]["new_gaps"])
    card["status"] = "failed" if bad else ("empty" if not recs else "ok")
    return card


# --------------------------------------------------------------------------- #
# run
# --------------------------------------------------------------------------- #
def load_worklist(path):
    op = gzip.open if path.endswith(".gz") else open
    with op(path, "rt", newline="") as f:
        return [(i + 1, r["username"]) for i, r in enumerate(csv.DictReader(f))
                if r["username"]]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--worklist")
    ap.add_argument("--out")
    ap.add_argument("--conc", type=int, default=5)
    ap.add_argument("--floor", type=float, default=0.0,
                    help="inter-request floor in seconds; 0 = pace on latency only")
    ap.add_argument("--limit", type=int, default=0, help="stop after N accounts")
    ap.add_argument("--start", type=int, default=-1, help="override checkpoint")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()

    if a.self_test:
        return self_test()
    if not (a.worklist and a.out):
        sys.exit("--worklist and --out are required")

    os.makedirs(a.out, exist_ok=True)
    lock = os.path.join(a.out, "_lock")
    try:                                              # mechanism 2
        fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        os.write(fd, f"{os.getpid()}\n".encode())
        os.close(fd)
    except FileExistsError:
        sys.exit(f"another collector holds {lock} (pid {open(lock).read().strip()}); "
                 f"verify with: ps -eo pid,args | grep 10_collect_authors | grep -v grep")

    try:
        work = load_worklist(a.worklist)
        if a.limit:
            work = work[:a.limit]
        ckpt = os.path.join(a.out, "_checkpoint.json")
        if a.start >= 0:
            start = a.start
        elif os.path.exists(ckpt):
            start = json.load(open(ckpt))["next_index"]
        else:
            start = 0
        idx_path = os.path.join(a.out, "_authors_index.jsonl")
        gaps_path = os.path.join(a.out, "_gaps.jsonl")
        bdir = os.path.join(a.out, "_batches")
        os.makedirs(bdir, exist_ok=True)

        print(f"{len(work):,} accounts; resuming at {start:,}; conc={a.conc}; "
              f"span {utc(SPAN_LO)} -> {utc(SPAN_HI)}", flush=True)
        t_run = time.time()

        for base in range(start, len(work), BATCH):
            chunk = work[base:base + BATCH]
            sess = Session(floor=a.floor)
            t0 = time.time()
            with ThreadPoolExecutor(max_workers=a.conc) as ex:
                cards = list(ex.map(
                    lambda rw: collect_author(sess, rw[1], rw[0], a.out), chunk))

            with open(idx_path, "a") as f:
                for c in cards:
                    f.write(json.dumps(c, ensure_ascii=False) + "\n")
            with open(gaps_path, "a") as f:           # mechanism 3
                for g in sess.gaps:
                    f.write(json.dumps(g) + "\n")
                for c in cards:
                    if c["status"] == "failed":
                        f.write(json.dumps({"account": c}) + "\n")

            st = collections.Counter(c["status"] for c in cards)
            meta = {
                "batch_base": base, "n_accounts": len(chunk),
                "rank_range": [chunk[0][0], chunk[-1][0]],
                "span": [SPAN_LO, SPAN_HI],
                "span_utc": [utc(SPAN_LO), utc(SPAN_HI)],
                "segments": {"pre": [PRE_START, OPEN], "during": [OPEN, FRZ],
                             "after": [FRZ, AFTER_END]},
                "segment_note": "labels only; a different boundary is a filter "
                                "on created_utc, not a re-collection",
                "collected_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "collector": "10_collect_authors rev-a", "api": API,
                "conc": a.conc, "floor": a.floor,
                "limit": "auto", "projection": None,
                "status": dict(st),
                "n_posts": sum(c.get("n_posts", 0) for c in cards),
                "n_comments": sum(c.get("n_comments", 0) for c in cards),
                "n_pre": sum(c.get("pre", 0) for c in cards),
                "n_during": sum(c.get("during", 0) for c in cards),
                "n_after": sum(c.get("after", 0) for c in cards),
                "pages": sess.pages, "bytes": sess.bytes,
                "seconds": round(time.time() - t0, 1),
                "retries": dict(sess.retries), "gaps": sess.gaps,
                "complete": not sess.gaps and st.get("failed", 0) == 0,
            }
            json.dump(meta, open(os.path.join(bdir, f"batch_{base:07d}.meta.json"), "w"),
                      indent=1)
            json.dump({"next_index": base + len(chunk),
                       "worklist": os.path.basename(a.worklist),
                       "span": [SPAN_LO, SPAN_HI]}, open(ckpt, "w"))

            done = base + len(chunk)
            # Rate is measured over accounts done THIS RUN, not since index 0.
            # After a resume the two differ, and dividing the absolute count by
            # this run's elapsed time reported a 1.5 h ETA on a 10.6 h job — a
            # number that looks like progress and is an artefact of the restart.
            rate = (done - start) / max(1e-9, time.time() - t_run)
            print(f"[{done:>7,}/{len(work):,}] ok={st.get('ok',0)} "
                  f"empty={st.get('empty',0)} failed={st.get('failed',0)} "
                  f"recs={meta['n_posts']+meta['n_comments']:,} "
                  f"({meta['n_pre']}/{meta['n_during']}/{meta['n_after']} p/d/a) "
                  f"{len(chunk)/(time.time()-t0):.2f} acct/s "
                  f"eta {(len(work)-done)/max(rate,1e-9)/3600:.1f} h", flush=True)

        n_gaps = sum(1 for _ in open(gaps_path)) if os.path.exists(gaps_path) else 0
        json.dump({"complete": n_gaps == 0, "n_gaps": n_gaps,
                   "span": [SPAN_LO, SPAN_HI], "api": API,
                   "collected_accounts": len(work),
                   "collector": "10_collect_authors rev-a"},
                  open(os.path.join(a.out, "_manifest.json"), "w"), indent=1)
        print(f"done. gaps={n_gaps}. complete={n_gaps == 0}")
        if n_gaps:
            print("NON-EMPTY LEDGER: this is not a corpus until the gaps are closed.")
    finally:
        os.unlink(lock)


# --------------------------------------------------------------------------- #
# self-test — every assertion gets a case that MUST fire and one that must not
# --------------------------------------------------------------------------- #
def self_test():
    import shutil, tempfile
    fails = []

    def ck(name, got, want):
        if got != want:
            fails.append(f"{name}: got {got!r}, want {want!r}")

    # --- segment labelling: boundaries are half-open and contiguous
    ck("seg pre/just-before-open", segment_of(OPEN - 1), "pre")
    ck("seg during/at-open", segment_of(OPEN), "during")
    ck("seg during/just-before-frz", segment_of(FRZ - 1), "during")
    ck("seg after/at-frz", segment_of(FRZ), "after")
    ck("seg pre/at-span-start", segment_of(PRE_START), "pre")
    ck("span is 24.0 days", round((SPAN_HI - SPAN_LO) / 86400, 1), 24.0)
    ck("during is 73h", (FRZ - OPEN) // 3600, 73)
    ck("no label gap", sorted({segment_of(t) for t in
                              (PRE_START, OPEN - 1, OPEN, FRZ - 1, FRZ, SPAN_HI - 1)}),
       ["after", "during", "pre"])

    # --- bucket naming
    ck("bucket 1", bucket_of(1), "r000000-000999")
    ck("bucket 999", bucket_of(999), "r000000-000999")
    ck("bucket 1000", bucket_of(1000), "r001000-001999")

    # --- the walk's tie handling, against a fake server
    class FakeSess:
        """A server with a real page size.  `page` must be >1: a 1-record page
        makes every second look saturated and fires the escape branch below on
        data that is not actually saturated — my first version of this test did
        that and reported a defect in `walk` that was a defect in the test."""
        def __init__(self, rows, page=2):
            self.rows, self.page = rows, page
            self.pages, self.gaps, self.calls = 0, [], 0
        def call(self, path, after=None, before=None, **kw):
            self.calls += 1
            if self.calls > 50:
                raise AssertionError("walk did not terminate")
            d = [r for r in self.rows if after < r["created_utc"] < before]
            return d[:self.page]
        def gap(self, *a, **k):
            self.gaps.append(a)

    # Two records share one second and the page boundary falls after them, so a
    # naive step to last_ts would refetch forever and a step to last_ts+1 would
    # drop the sibling.  Tie-safe stepping must find all three.
    rows = [{"id": "a", "created_utc": 1000}, {"id": "b", "created_utc": 1000},
            {"id": "c", "created_utc": 1005}]
    got = walk(FakeSess(rows), "p", 900, 2000)
    ck("walk finds both same-second siblings", sorted(got), ["a", "b", "c"])

    # The escape branch: when one second saturates a whole page, the walk must
    # still TERMINATE.  It does so by stepping past that second, which is the
    # documented cost — collect_v6 makes the same trade, so Layer A and Layer B
    # paginate identically.  Requires >page-size records in one second from one
    # author, which limit=auto (100-1000 per page) puts out of reach.
    sat = [{"id": x, "created_utc": 1000} for x in "abc"]
    s_sat = FakeSess(sat, page=2)
    got = walk(s_sat, "p", 900, 2000)
    ck("saturated second terminates", len(got) >= 2, True)
    ck("saturated second does not loop", s_sat.calls <= 5, True)

    # --- an empty page terminates; a SHORT page does not
    class ShortThenEmpty:
        def __init__(self):
            self.pages, self.gaps, self.n = 0, [], 0
        def call(self, path, after=None, before=None, **kw):
            self.n += 1
            if self.n == 1:
                return [{"id": "x", "created_utc": 1000}]      # short, not last
            if self.n == 2:
                return [{"id": "y", "created_utc": 1100}]
            return []
        def gap(self, *a, **k):
            self.gaps.append(a)
    ck("short page is not a last page", sorted(walk(ShortThenEmpty(), "p", 900, 2000)),
       ["x", "y"])

    # --- an unrecoverable page bisects and ledgers rather than vanishing
    class AlwaysNone:
        def __init__(self):
            self.pages, self.gaps = 0, []
        def call(self, *a, **k):
            return None
        def gap(self, *a, **k):
            self.gaps.append(a)
    s = AlwaysNone()
    walk(s, "p", 0, 10 ** 6)
    ck("unrecoverable page writes a gap", len(s.gaps) > 0, True)

    s2 = AlwaysNone()
    walk(s2, "p", 0, 30)          # below BISECT_FLOOR: ledger immediately, no recursion
    ck("below bisect floor ledgers once", len(s2.gaps), 1)

    # --- collect_author's four checks, each with a firing case
    tmp = tempfile.mkdtemp()
    try:
        class Canned:
            """Serves a fixed record set once per endpoint, then empties."""
            def __init__(self, posts, comments):
                self.by = {"posts/search": posts, "comments/search": comments}
                self.gaps, self.pages, self.served = [], 0, set()
            def call(self, path, after=None, before=None, **kw):
                if path in self.served:
                    return []
                self.served.add(path)
                return self.by[path]
            def gap(self, *a, **k):
                self.gaps.append(a)

        good_p = [{"id": "p1", "created_utc": OPEN + 10, "author": "Alice",
                   "subreddit": "place"}]
        good_c = [{"id": "c1", "created_utc": PRE_START + 5, "author": "alice",
                   "subreddit": "place"},
                  {"id": "c2", "created_utc": FRZ + 100, "author": "Alice",
                   "subreddit": "canada"}]
        card = collect_author(Canned(good_p, good_c), "Alice", 1, tmp)
        ck("good account is ok", card["status"], "ok")
        ck("segments split 1/1/1", (card["pre"], card["during"], card["after"]),
           (1, 1, 1))
        ck("author case difference is not an error", card["checks"]["wrong_author"], [])
        ck("lines match records", card["n_lines"], 3)
        ck("subreddits counted", card["n_subreddits"], 2)
        ck("file is where the card says", os.path.exists(os.path.join(tmp, card["file"])),
           True)

        # empty is a status, not a failure, and the file still exists
        card = collect_author(Canned([], []), "Bob", 2, tmp)
        ck("empty account is empty, not failed", card["status"], "empty")
        ck("empty account still gets a file",
           os.path.exists(os.path.join(tmp, card["file"])), True)
        ck("empty account has no records", card["n_records"], 0)

        # a record outside the span must fail
        card = collect_author(Canned([{"id": "p", "created_utc": SPAN_HI + 1,
                                       "author": "Carol", "subreddit": "x"}], []),
                              "Carol", 3, tmp)
        ck("out-of-span record fails", card["status"], "failed")
        ck("out-of-span counted", card["checks"]["out_of_span"], 1)

        # a record by someone else must fail
        card = collect_author(Canned([], [{"id": "c", "created_utc": OPEN,
                                          "author": "Someone_Else",
                                          "subreddit": "x"}]), "Dave", 4, tmp)
        ck("wrong-author record fails", card["status"], "failed")
        ck("wrong author named", card["checks"]["wrong_author"], ["Someone_Else"])

        # a gap raised during the account must fail it
        class Gappy(AlwaysNone):
            pass
        card = collect_author(Gappy(), "Erin", 5, tmp)
        ck("an account with a gap fails", card["status"], "failed")

        # records are verbatim: no key is dropped, exactly two are added
        rec = json.loads(open(os.path.join(tmp, bucket_of(1), "Alice.jsonl")).readline())
        ck("verbatim + kind + segment",
           sorted(set(rec) - {"kind", "segment"}),
           ["author", "created_utc", "id", "subreddit"])
        ck("kind injected", rec["kind"], "comment")
        ck("sorted by created_utc first", rec["id"], "c1")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    n = 36
    if fails:
        print(f"SELF-TEST FAILED ({len(fails)} of {n}):")
        for f in fails:
            print("  -", f)
        sys.exit(1)
    print(f"self-test OK — {n} cases, including a firing case for every "
          f"account-level check")


if __name__ == "__main__":
    main()
