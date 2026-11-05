#!/usr/bin/env python3
"""The event window, in one place, with its derivation beside it.

WHY THIS FILE EXISTS
--------------------
This project has now shipped two window errors, and both had the same cause: a
number that lived in more than one file, so nobody could re-derive it.

  1. `OPEN = 1491004800` (2017-04-01 00:00 UTC) was read off the editorial phrase
     "the April Fools event, April 1-3 2017" and then copied into the segment
     definitions, the collector, the frame table and the instrument's setting
     facts.  The canvas actually opened 2017-03-31 at about 16:55 UTC.
  2. Layer B's memo, which diagnosed (1) from the pixel record, then titled itself
     "wrong by 31 hours" and repeated 31/32 in four sections.  Its own corrected
     constant is 8 hours from the one it replaces.  1491004800 - 1490976000 =
     28800 = 8h.

Every script imports from here.  Nothing defines a window for itself.  Anything
that writes a corpus stamps `WINDOW_REVISION` into its meta card, and anything
that reads one asserts the stamp matches.  That is the mechanism; the rule alone
already failed twice.

DERIVATION (Layer B, 2026-07-29, from `original_tile_placements.csv`)
--------------------------------------------------------------------
A histogram of 16,559,897 timestamped placements, not a recollection and not a
wiki:

    2017-03-31 00:00-15:59      391 placements, 18 distinct accounts   <- testing
    2017-03-31 16:55             41   <- first minute of public traffic
    2017-03-31 17:00         46,642
    2017-03-31 20:00        202,717
    2017-04-01 00:00        122,077   <- where the old OPEN started
    2017-04-03 16:58:54                  last placement in the file

From 16:55 the count rises in every single minute without exception; before it,
minutes are mostly empty.  Two regimes, not a ramp.

Prose figure: "approximately 72 hours" (72.1h measured from the 16:55 ramp).
Code figure: OPEN below, which is 73.0h.  State both in the methods appendix.

WHY 16:00 AND NOT 16:55
-----------------------
16:00 is a clean hour, it sits after all 391 testing placements, and it makes the
rule statable in one line: everything from 16:00 on 31 March is the public event.
16:55 would buy 55 minutes containing 41 placements and cost a constant nobody
can hold in their head.
"""

# ---------------------------------------------------------------- the constants

OPEN = 1490976000
"""2017-03-31 16:00:00 UTC — operational start of the public canvas.

Derived from the placement histogram above, NOT from the "April 1-3" framing.
Supersedes 1491004800, which was 8 hours late and excluded the launch surge:
991,892 placements by 300,274 distinct accounts (25.7% of all placers), 96,470 of
whom placed only in those 8 hours.
"""

FRZ = 1491238800
"""2017-04-03 17:00:00 UTC — all further placement disabled.

Unchanged and confirmed: the last placement in the pixel record is
2017-04-03 16:58:54 UTC.
"""

PRE_OPEN = OPEN - 7 * 86400
"""2017-03-24 16:00:00 UTC — seven clean days before OPEN.

J's ruling, 2026-07-29: restore a symmetric 7-day baseline rather than accept the
6d16h that falls out of the correction.  The first collection ran
[2017-03-25 00:00, 2017-03-31 16:00) by accident of the old constant, so the
8 hours [PRE_OPEN, 1490400000) are a back-fill.
"""

AFTER_CLOSE = FRZ + 14 * 86400
"""2017-04-17 17:00:00 UTC — fourteen days after the freeze. Unaffected by the
correction; the AFTER segment never touched OPEN."""

SEGMENTS = {
    "pre":    (PRE_OPEN, OPEN),
    "during": (OPEN, FRZ),
    "after":  (FRZ, AFTER_CLOSE),
}

WINDOW_REVISION = "w2-2026-07-29"
"""Stamp written into every corpus meta card by the builder and asserted by every
reader.  `w1` is the superseded split (OPEN=1491004800, pre from 2017-03-25
00:00); `w2` is this file.  A corpus with no stamp is `w1` by construction —
nothing under w1 knew to write one."""

# --------------------------------------------------- what changed from w1 to w2

W1_OPEN = 1491004800
"""The superseded constant. Kept so that the two repair operations can be
expressed against it rather than as bare literals."""

W1_PRE_OPEN = 1490400000
"""2017-03-25 00:00 UTC — where the first pre collection actually began."""

MOVE_WINDOW = (OPEN, W1_OPEN)
"""[2017-03-31 16:00, 2017-04-01 00:00) — 8 hours that w1 filed as `pre` and w2
files as `during`.  Repaired by re-partitioning on created_utc; nothing to
collect, every record is already on disk.  Measured across the sample of 101:
12,573 posts + 66,542 comments = 79,115 items, +19.4% on the DURING corpus."""

BACKFILL_WINDOW = (PRE_OPEN, W1_PRE_OPEN)
"""[2017-03-24 16:00, 2017-03-25 00:00) — 8 hours never collected, needed to make
the baseline a clean 7 days under the new OPEN.  Requires a collection run."""


def hours(span):
    lo, hi = span
    return (hi - lo) / 3600.0


def which_segment(created_utc):
    """The segment a record belongs to under w2, or None if outside all three."""
    for name, (lo, hi) in SEGMENTS.items():
        if lo <= created_utc < hi:
            return name
    return None


def assert_window(meta, segment, where="corpus"):
    """Refuse to proceed on a corpus whose meta card disagrees with these constants.

    The memo asked for this on the builder.  It belongs on every reader: the w1
    corpora are still on disk and will stay there, so 'the file exists' is not
    evidence that it is the file you meant.
    """
    lo, hi = SEGMENTS[segment]
    rev = meta.get("window_revision")
    if rev != WINDOW_REVISION:
        raise AssertionError(
            "%s: window_revision is %r, expected %r. This corpus was built under a "
            "superseded window (w1 had OPEN=%d, pre from %d) and its pre/during "
            "boundary is 8 hours wrong. Re-partition before using it."
            % (where, rev, WINDOW_REVISION, W1_OPEN, W1_PRE_OPEN))
    got = (meta.get("after"), meta.get("before"))
    if got != (lo, hi):
        raise AssertionError(
            "%s: meta window %r does not match SEGMENTS[%r] = %r"
            % (where, got, segment, (lo, hi)))
    return True


def stamp(meta, segment):
    """Write the window fields a corpus must carry. Call this in the builder."""
    lo, hi = SEGMENTS[segment]
    meta["segment"] = segment
    meta["after"] = lo
    meta["before"] = hi
    meta["window_revision"] = WINDOW_REVISION
    return meta


if __name__ == "__main__":
    import datetime as _dt

    def _s(t):
        return _dt.datetime.fromtimestamp(t, _dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    print("window revision %s\n" % WINDOW_REVISION)
    for name in ("pre", "during", "after"):
        lo, hi = SEGMENTS[name]
        print("  %-7s %s -> %s  (%.1f h / %.2f d)"
              % (name, _s(lo), _s(hi), hours((lo, hi)), hours((lo, hi)) / 24))
    print()
    print("  move     %s -> %s  (%.1f h)  pre -> during, re-partition"
          % (_s(MOVE_WINDOW[0]), _s(MOVE_WINDOW[1]), hours(MOVE_WINDOW)))
    print("  backfill %s -> %s  (%.1f h)  never collected, needs a run"
          % (_s(BACKFILL_WINDOW[0]), _s(BACKFILL_WINDOW[1]), hours(BACKFILL_WINDOW)))
    print()

    # self-checks: the arithmetic that both errors got wrong
    assert hours(MOVE_WINDOW) == 8.0, "the move window is 8 hours, not 31 or 32"
    assert hours(BACKFILL_WINDOW) == 8.0
    assert hours(SEGMENTS["pre"]) == 168.0, "pre must be a clean 7 days under w2"
    assert hours(SEGMENTS["during"]) == 73.0
    assert hours(SEGMENTS["after"]) == 336.0
    assert which_segment(OPEN) == "during"
    assert which_segment(OPEN - 1) == "pre"
    assert which_segment(FRZ) == "after"
    assert which_segment(FRZ - 1) == "during"
    assert which_segment(PRE_OPEN - 1) is None
    assert which_segment(AFTER_CLOSE) is None
    # every record w1 filed as during is still during under w2
    assert which_segment(W1_OPEN) == "during"
    # and the launch hours have moved
    assert which_segment(OPEN + 3600) == "during", "17:00 on 31 Mar is the event"
    # the stamp gate actually fires
    try:
        assert_window({"after": OPEN, "before": FRZ}, "during")
    except AssertionError as e:
        assert "window_revision" in str(e)
    else:
        raise SystemExit("FAIL: assert_window passed an unstamped meta")
    try:
        assert_window(stamp({}, "pre"), "during")
    except AssertionError as e:
        assert "does not match" in str(e)
    else:
        raise SystemExit("FAIL: assert_window passed a pre meta as during")
    assert_window(stamp({}, "during"), "during")
    print("self-checks pass — including that the move window is 8 hours")
