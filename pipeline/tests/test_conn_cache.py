"""Focused test for pipeline/lib/conn_cache.py (incremental connection regen).

Proves the dirty-set logic that lets the expensive full-corpus connection runs
(extract_insights top_k=25, topic_modeling top_k=5) only fire an LLM call for
papers whose connections can actually have changed, WITHOUT losing edges.

It imports ONLY the dependency-light targets — ``conn_cache`` (stdlib-only) and
the REAL ``lib/connections`` (also stdlib-only) — never the heavy clustering
stack. The LLM is always stubbed (a fake ``generate_connections_from_candidates``
that records which slugs it was handed); no network, no real keys. The global
connections store is redirected to a scratch tmp dir, so live
``docs/<topic>/_paper_connections.json`` / ``_global_connections.json`` are never
touched.

Covers:
  * topk_sets extraction; cache round-trip save/load.
  * dirty rules: new / unchanged / membership-changed / 0-connection(gap) /
    force / top_k mismatch / embed_model mismatch / corrupt-input fallback.
  * HUB SCENARIO end-to-end with the real merge: a new paper N pushes into an
    old paper O's top-k → O is dirty → fake generate {N,O} → merge_to_global →
    make_bidirectional_deduped → N gets the INBOUND link from O (hub not lost),
    while a far-away unchanged paper P is NOT regenerated yet keeps its edges.
  * 0-dirty: generate handed {} (skipped) AND the consumer view still rebuilt.
  * cost proof: stubbed generator received exactly the d dirty slugs.

Run:
  PYTHONUTF8=1 /opt/homebrew/Caskroom/miniconda/base/envs/py312/bin/python \
      pipeline/tests/test_conn_cache.py
"""

import os
import sys
import tempfile

# Import ONLY the dependency-light targets — add pipeline/lib to sys.path so
# `import conn_cache` / `import connections` resolve the single files directly
# (lib/__init__.py is empty; nothing heavy is pulled in).
# NOTE: `pipeline/lib` 를 sys.path 에 넣으면 그 안의 `dateutil.py` 가 표준
# `python-dateutil` 을 가려, 같은 프로세스에서 pandas 를 쓰는 테스트가 전부
# 깨진다. `unittest discover` 는 실행 전에 모든 모듈을 import 하므로 이 한 줄이
# 스위트를 오염시킨다. 패키지 경로로 import 한다.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lib import conn_cache  # noqa: E402
from lib import connections  # noqa: E402  (the REAL merge/bidirectional logic)

# sync_topic_connections now self-heals connection slugs against the real
# _papers_index.json (remap renumbered, prune deleted). This test uses synthetic
# slugs that aren't indexed, so force the resolver to identity (empty index = no
# remap, no prune) to exercise the orthogonal bidirectional/cache logic.
connections.load_index_slugs = lambda: set()


# ─────────────────────────────────────────────────────────────────────────────
# Stub LLM generator: records the slugs it was asked to generate for, and returns
# the connections handed to it via a small per-test "script". NO network.
# ─────────────────────────────────────────────────────────────────────────────

class StubGenerator:
    def __init__(self, script):
        # script: {slug: [{slug, relation, reason}, ...]}
        self.script = script
        self.seen_slugs = None

    def __call__(self, candidates, *args, **kwargs):
        self.seen_slugs = set(candidates.keys())
        return {s: list(self.script.get(s, [])) for s in candidates}


def _logs():
    out = []
    return out, (lambda m: out.append(str(m)))


def main():
    failures = []

    def check(name, cond):
        status = "PASS" if cond else "FAIL"
        print(f"  [{status}] {name}")
        if not cond:
            failures.append(name)

    print("== 0. dependency-light import ==")
    heavy = [m for m in ("umap", "hdbscan", "sentence_transformers", "torch",
                          "numba", "llvmlite")
             if m in sys.modules]
    check("conn_cache imported", "conn_cache" in sys.modules)
    check("connections imported", "connections" in sys.modules)
    check(f"no heavy deps loaded (found: {heavy or 'none'})", not heavy)

    # ── candidates: {slug: [(target, score), ...]} as compute_related_candidates returns
    CAND = {
        "001_A": [("002_B", 0.9), ("003_C", 0.8)],
        "002_B": [("001_A", 0.9), ("003_C", 0.7)],
        "003_C": [("002_B", 0.7), ("001_A", 0.8)],
    }

    print("== 1. topk_sets: membership only, sorted, scores dropped ==")
    sets = conn_cache.topk_sets(CAND)
    check("001_A set == sorted targets", sets["001_A"] == ["002_B", "003_C"])
    check("003_C set sorted (not score order)", sets["003_C"] == ["001_A", "002_B"])
    check("plain-string lists tolerated",
          conn_cache.topk_sets({"x": ["b", "a"]}) == {"x": ["a", "b"]})

    print("== 2. cache round-trip save/load ==")
    with tempfile.TemporaryDirectory() as td:
        path = conn_cache.save_topk_cache(td, CAND, 25, "specter2-tag")
        check("cache file written", os.path.exists(path))
        check("cache path encodes k", path.endswith("_conn_topk_cache_k25.json"))
        loaded = conn_cache.load_topk_cache(td, 25)
        check("loaded top_k", loaded.get("top_k") == 25)
        check("loaded embed_model", loaded.get("embed_model") == "specter2-tag")
        check("loaded sets match", loaded.get("sets") == conn_cache.topk_sets(CAND))
        # separate cache per top_k — k5 must not see k25's cache
        check("k5 cache absent (separate per top_k)",
              conn_cache.load_topk_cache(td, 5) == {})
        check("missing dir/file -> {}",
              conn_cache.load_topk_cache(os.path.join(td, "nope"), 25) == {})

    print("== 3. dirty rules ==")
    prev = {"top_k": 25, "embed_model": "tag",
            "sets": conn_cache.topk_sets(CAND)}
    existing_all = {"001_A": [{"slug": "002_B"}], "002_B": [{"slug": "001_A"}],
                    "003_C": [{"slug": "002_B"}]}

    # 3a unchanged + all have connections -> nothing dirty
    d, r = conn_cache.compute_dirty(CAND, prev, existing_all, 25, "tag")
    check(f"unchanged -> empty dirty ({r})", d == set())

    # 3b new paper -> dirty
    cand_new = dict(CAND)
    cand_new["004_D"] = [("001_A", 0.6), ("002_B", 0.6)]
    d, r = conn_cache.compute_dirty(cand_new, prev, existing_all, 25, "tag")
    check("new paper 004_D dirty", "004_D" in d)
    check("only the new paper dirty", d == {"004_D"})

    # 3c membership changed -> dirty (hub trap unit)
    cand_chg = dict(CAND)
    cand_chg["001_A"] = [("002_B", 0.9), ("009_X", 0.85)]  # 003_C -> 009_X
    d, r = conn_cache.compute_dirty(cand_chg, prev, existing_all, 25, "tag")
    check("membership-changed 001_A dirty", "001_A" in d)
    check("unchanged 002_B NOT dirty", "002_B" not in d)

    # 3d 0-connection paper -> dirty (gap safety) even if set unchanged
    existing_gap = {"001_A": [{"slug": "002_B"}], "002_B": [{"slug": "001_A"}]}
    d, r = conn_cache.compute_dirty(CAND, prev, existing_gap, 25, "tag")
    check("0-connection 003_C dirty (gap)", "003_C" in d)
    check("connected 001_A NOT dirty", "001_A" not in d)

    # 3e force -> all
    d, r = conn_cache.compute_dirty(CAND, prev, existing_all, 25, "tag", force=True)
    check(f"force -> all keys ({r})", d == set(CAND) and r == "force")

    # 3f empty/missing prev cache -> all
    d, r = conn_cache.compute_dirty(CAND, {}, existing_all, 25, "tag")
    check(f"no prev cache -> all keys ({r})", d == set(CAND))

    # 3g top_k mismatch -> all
    prev_k5 = {"top_k": 5, "embed_model": "tag", "sets": conn_cache.topk_sets(CAND)}
    d, r = conn_cache.compute_dirty(CAND, prev_k5, existing_all, 25, "tag")
    check(f"top_k mismatch -> all keys ({r})", d == set(CAND) and "top_k" in r)

    # 3h embed_model mismatch -> all
    prev_oldmodel = {"top_k": 25, "embed_model": "OLD",
                     "sets": conn_cache.topk_sets(CAND)}
    d, r = conn_cache.compute_dirty(CAND, prev_oldmodel, existing_all, 25, "tag")
    check(f"embed_model mismatch -> all keys ({r})",
          d == set(CAND) and "embed_model" in r)

    # 3i corrupt prev (sets is a non-iterable) -> exception -> all (fallback)
    bad_prev = {"top_k": 25, "embed_model": "tag", "sets": 12345}
    _, logfn = _logs()
    d, r = conn_cache.compute_dirty(CAND, bad_prev, existing_all, 25, "tag", log=logfn)
    check(f"corrupt input -> all keys (fallback) ({r})",
          d == set(CAND) and r.startswith("error-fallback"))

    print("== 4. restrict_candidates: only dirty keys ==")
    restricted = conn_cache.restrict_candidates(cand_new, {"004_D"})
    check("restrict keeps only dirty + present", set(restricted) == {"004_D"})
    check("restrict ignores missing dirty key",
          conn_cache.restrict_candidates(CAND, {"zzz"}) == {})

    # ── HUB SCENARIO ───────────────────────────────────────────────────────────
    print("== 5. HUB scenario end-to-end (real merge, no edge lost) ==")
    topic = "testtopic"
    with tempfile.TemporaryDirectory() as td:
        # Redirect the global store to scratch (NEVER touch live docs/).
        connections.GLOBAL_CONN_PATH = os.path.join(td, "_global_connections.json")

        O, N, P = "100_Old_O", "300_New_N", "200_Far_P"
        MID, MID2, PN = "050_Mid", "060_Mid2", "210_PNeighbor"
        topic_slugs = [O, N, P, MID, MID2, PN]

        # Prior cache (k=5): O's top-k does NOT include N; P present & stable.
        prev_sets = {
            O:   sorted([MID, MID2]),
            P:   sorted([PN]),
            MID: sorted([MID2]),
            MID2: sorted([MID]),
            PN:  sorted([P]),
        }
        prev_cache = {"top_k": 5, "embed_model": "tag", "sets": prev_sets}

        # Current candidates: N exists now; O's top-k now includes N (MID pushed
        # out → membership changed); P unchanged.
        cur_cand = {
            O:   [(MID2, 0.8), (N, 0.79)],        # MID -> N  (CHANGED)
            N:   [(O, 0.79), (MID2, 0.7)],        # NEW
            P:   [(PN, 0.9)],                      # unchanged
            MID: [(MID2, 0.6)],
            MID2: [(MID, 0.6)],
            PN:  [(P, 0.9)],
        }
        # Existing per-paper connections (prior _paper_connections view): O & P
        # connected; N has none (so even without the membership rule N is a gap).
        existing_conns = {
            O:   [{"slug": MID, "relation": "foundation", "reason": "old"}],
            P:   [{"slug": PN, "relation": "foundation", "reason": "old P"}],
            MID: [{"slug": MID2, "relation": "alternative", "reason": "m"}],
            MID2: [{"slug": MID, "relation": "alternative", "reason": "m"}],
            PN:  [{"slug": P, "relation": "extension", "reason": "p"}],
        }

        dirty, reason = conn_cache.compute_dirty(
            cur_cand, prev_cache, existing_conns, 5, "tag")
        check("O dirty (top-k gained N — hub)", O in dirty)
        check("N dirty (new)", N in dirty)
        check("P NOT dirty (unchanged & connected)", P not in dirty)
        check("far MID/MID2/PN NOT dirty", not ({MID, MID2, PN} & dirty))

        # Seed the global store with prior edges for EVERYONE (same source_topic),
        # so we can prove non-dirty P keeps its edge through the merge.
        connections.save_global_connections({
            O: [{"slug": MID, "relation": "foundation", "reason": "old",
                 "source_topic": topic}],
            P: [{"slug": PN, "relation": "foundation", "reason": "old P",
                 "source_topic": topic}],
        })

        # Fake generate ONLY for the dirty set. O→N (so N gets an inbound link).
        gen = StubGenerator({
            O: [{"slug": N, "relation": "foundation", "reason": "O founds N"}],
            N: [{"slug": MID2, "relation": "alternative", "reason": "N alt"}],
        })
        gen_candidates = conn_cache.restrict_candidates(cur_cand, dirty)
        new_conns = gen(gen_candidates)

        check("generator handed EXACTLY the dirty slugs",
              gen.seen_slugs == dirty)

        # Real persistence: merge_to_global → bidi → filter for topic.
        _, logfn = _logs()
        topic_conns = connections.sync_topic_connections(
            new_conns, topic, topic_slugs, td, log=logfn)

        # N must have the inbound hub link from O (would be lost by "new-only").
        n_targets = {c["slug"] for c in topic_conns.get(N, [])}
        check("N has INBOUND link from O (hub preserved)", O in n_targets)
        # O still links to N too (forward).
        o_targets = {c["slug"] for c in topic_conns.get(O, [])}
        check("O links to N (forward)", N in o_targets)
        # Non-dirty P keeps its prior edge (untouched by merge).
        p_targets = {c["slug"] for c in topic_conns.get(P, [])}
        check("non-dirty P keeps prior edge to PN", PN in p_targets)
        # O's stale old edge to MID was replaced (O regenerated), not duplicated.
        check("O's stale MID edge dropped after regen", MID not in o_targets)

    # ── 0-DIRTY: consumer view still produced, generator handed {} ────────────
    print("== 6. 0-dirty: generate skipped/handed {}, consumer view rebuilt ==")
    with tempfile.TemporaryDirectory() as td:
        connections.GLOBAL_CONN_PATH = os.path.join(td, "_global_connections.json")
        topic = "testtopic2"
        A, B = "001_A", "002_B"
        topic_slugs = [A, B]
        # Prior global has an A↔B edge already.
        connections.save_global_connections({
            A: [{"slug": B, "relation": "foundation", "reason": "x",
                 "source_topic": topic}],
        })
        cand = {A: [(B, 0.9)], B: [(A, 0.9)]}
        prev_cache = {"top_k": 25, "embed_model": "tag",
                      "sets": conn_cache.topk_sets(cand)}
        existing_conns = {A: [{"slug": B}], B: [{"slug": A}]}
        dirty, reason = conn_cache.compute_dirty(
            cand, prev_cache, existing_conns, 25, "tag")
        check(f"0 dirty when nothing changed ({reason})", dirty == set())

        gen = StubGenerator({})
        gen_candidates = conn_cache.restrict_candidates(cand, dirty)
        # Integration contract: empty dirty -> all_connections = {} (skip LLM),
        # but STILL sync so the consumer view is rebuilt.
        if gen_candidates:
            all_conns = gen(gen_candidates)
        else:
            all_conns = {}  # LLM skipped entirely
        check("generator NOT called for non-empty dirty (it was empty)",
              gen.seen_slugs is None)

        _, logfn = _logs()
        topic_conns = connections.sync_topic_connections(
            all_conns, topic, topic_slugs, td, log=logfn)
        # merge_to_global({}) is a no-op; bidi over unchanged global still yields
        # the A↔B view.
        check("consumer view still produced (A present)", A in topic_conns)
        a_targets = {c["slug"] for c in topic_conns.get(A, [])}
        b_targets = {c["slug"] for c in topic_conns.get(B, [])}
        check("A↔B edge preserved (forward)", B in a_targets)
        check("A↔B edge preserved (inbound/bidi)", A in b_targets)

    # ── COST PROOF ───────────────────────────────────────────────────────────
    print("== 7. cost proof: generator receives exactly d of K slugs ==")
    K_cand = {f"{i:03d}_P": [("000_seed", 0.5)] for i in range(1, 21)}  # K=20
    K = len(K_cand)
    prev_cache = {"top_k": 25, "embed_model": "tag",
                  "sets": conn_cache.topk_sets(K_cand)}
    existing_conns = {s: [{"slug": "000_seed"}] for s in K_cand}
    # Make exactly 3 dirty: one new, one membership-changed, one gap.
    K_cur = dict(K_cand)
    K_cur["099_NEW"] = [("000_seed", 0.4)]                  # new
    K_cur["001_P"] = [("000_seed", 0.5), ("888_X", 0.4)]   # membership changed
    existing_conns.pop("002_P")                              # gap
    dirty, reason = conn_cache.compute_dirty(
        K_cur, prev_cache, existing_conns, 25, "tag")
    d = len(dirty)
    check(f"exactly 3 dirty of {len(K_cur)} (d={d})", dirty == {"099_NEW", "001_P", "002_P"})
    gen = StubGenerator({})
    gen(conn_cache.restrict_candidates(K_cur, dirty))
    check("stub received exactly d slugs", len(gen.seen_slugs) == d)
    check("stub received the dirty slugs (not all K)",
          gen.seen_slugs == dirty and len(gen.seen_slugs) < K)

    # ── next_cache_sets: regenerated advance vs truncated-dirty retry ─────────
    print("== 8. next_cache_sets: advance regenerated, retry truncated dirty ==")
    prev8 = {"top_k": 5, "embed_model": "tag",
             "sets": {"100_O": ["050_M", "060_M2"], "200_P": ["210_PN"]}}
    cur8 = {
        "100_O": [("060_M2", 0.8), ("300_N", 0.79)],  # gained 300_N (membership changed)
        "200_P": [("210_PN", 0.9)],                    # unchanged
        "300_N": [("100_O", 0.79)],                    # new (no prev)
    }
    dirty8 = {"100_O", "300_N"}

    # (a) both dirty slugs regenerated -> advance both to current
    sets_a = conn_cache.next_cache_sets(cur8, prev8, dirty8, {"100_O", "300_N"})
    check("regenerated O advanced to current (incl 300_N)",
          sets_a["100_O"] == sorted(["060_M2", "300_N"]))
    check("regenerated new N saved at current", sets_a["300_N"] == ["100_O"])
    check("non-dirty P advanced (==prev)", sets_a["200_P"] == ["210_PN"])

    # (b) generation truncated -> neither dirty slug returned
    sets_b = conn_cache.next_cache_sets(cur8, prev8, dirty8, set())
    check("truncated OLD O keeps PREV set (no 300_N)",
          sets_b.get("100_O") == sorted(["050_M", "060_M2"]))
    check("truncated NEW N omitted from cache", "300_N" not in sets_b)
    check("non-dirty P still advanced when others truncated",
          sets_b["200_P"] == ["210_PN"])
    # Re-diffing against the (b) cache must re-flag BOTH truncated papers, even
    # if a stray edge would mask the gap rule (so they self-heal next run).
    d_re, _ = conn_cache.compute_dirty(
        cur8, {"top_k": 5, "embed_model": "tag", "sets": sets_b},
        {"100_O": [{"slug": "x"}], "200_P": [{"slug": "y"}],
         "300_N": [{"slug": "z"}]},  # all "connected" so GAP rule would NOT catch
        5, "tag")
    check("truncated OLD O re-flagged dirty (membership vs kept-prev)", "100_O" in d_re)
    check("truncated NEW N re-flagged dirty (omitted -> NEW)", "300_N" in d_re)
    check("non-dirty P NOT re-flagged", "200_P" not in d_re)

    # ── scope isolation: ei vs tm caches never collide ────────────────────────
    print("== 9. cache scope isolation (ei vs tm never collide at same k) ==")
    with tempfile.TemporaryDirectory() as td:
        p_ei = conn_cache.save_topk_cache(td, CAND, 5, "tag", scope="ei")
        p_tm = conn_cache.save_topk_cache(td, {"z_Z": [("y_Y", 0.5)]}, 5, "tag",
                                          scope="tm")
        check("ei and tm cache files differ at same k", p_ei != p_tm)
        check("ei filename namespaced", p_ei.endswith("_conn_topk_cache_ei_k5.json"))
        check("tm load isolated from ei",
              conn_cache.load_topk_cache(td, 5, scope="tm").get("sets")
              == {"z_Z": ["y_Y"]})
        check("ei load isolated from tm",
              conn_cache.load_topk_cache(td, 5, scope="ei").get("sets")
              == conn_cache.topk_sets(CAND))
        check("unscoped load does not see scoped caches",
              conn_cache.load_topk_cache(td, 5) == {})

    print()
    if failures:
        print(f"RESULT: FAIL ({len(failures)} failed: {failures})")
        sys.exit(1)
    print("RESULT: ALL PASS")


if __name__ == "__main__":
    main()
