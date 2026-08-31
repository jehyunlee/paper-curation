"""Focused test for review_to_html._resolve_target_slugs.

Locks the per-paper render target resolution that drives the new
``--with-connected`` feature (re-render a paper's connection neighbours so a new/
changed edge shows its reverse on the neighbour's own page), and guards the
comma-`--slugs` regression where a raw string was iterated character-by-character
(matching almost the whole corpus instead of the two requested papers).

Pure function — no file IO, no rendering. Run:
  PYTHONUTF8=1 /opt/homebrew/Caskroom/miniconda/base/envs/py312/bin/python \
      pipeline/tests/test_review_to_html.py
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import review_to_html as R  # noqa: E402

ALL = sorted([
    "120_A", "1200_B", "590_Open", "900_C", "793_X", "1065_Y", "1124_Z",
    "9121_Shift", "9122_Claude", "0042_W",
])
# bidirectional connections view (a seed names all its neighbours both ways)
CONN = {
    "9121_Shift": [{"slug": "590_Open"}, {"slug": "9122_Claude"}, {"slug": "1065_Y"},
                   {"slug": "900_C"}, {"slug": "793_X"}, {"slug": "1124_Z"}],
    "9122_Claude": [{"slug": "9121_Shift"}, {"slug": "1065_Y"}],
}


def main():
    fails = []

    def check(name, cond):
        print(f"  [{'PASS' if cond else 'FAIL'}] {name}")
        if not cond:
            fails.append(name)

    r = R._resolve_target_slugs

    print("== 1. comma string -> exactly those papers (char-walk bug fixed) ==")
    out = r(ALL, slugs="9121,9122")
    check("comma '9121,9122' == the two", out == ["9121_Shift", "9122_Claude"])
    check("does NOT match unrelated 120_A", "120_A" not in out)
    check("does NOT explode to whole corpus", len(out) < len(ALL))

    print("== 2. single prefix matches NNN_ only (120 != 1200) ==")
    out = r(ALL, slugs="120")
    check("'120' -> only 120_A", out == ["120_A"])

    print("== 3. list input ==")
    out = r(ALL, slugs=["590", "900"])
    check("list ['590','900']", sorted(out) == ["590_Open", "900_C"])

    print("== 4. numeric range ==")
    out = r(ALL, slugs="119-121")
    check("range 119-121 -> 120_A (not 1200_B)", out == ["120_A"])

    print("== 5. with_connected expands seeds to neighbours ==")
    out = set(r(ALL, slugs="9121", with_connected=True, connections=CONN))
    exp = {"9121_Shift", "590_Open", "9122_Claude", "1065_Y", "900_C", "793_X", "1124_Z"}
    check("9121 + its 6 neighbours", out == exp)
    check("neighbour 590_Open included (reverse edge will render)", "590_Open" in out)

    print("== 6. with_connected on a pair (union of both seeds' neighbours) ==")
    out = set(r(ALL, slugs="9121,9122", with_connected=True, connections=CONN))
    check("includes both seeds", {"9121_Shift", "9122_Claude"} <= out)
    check("includes 9121's neighbour 793_X", "793_X" in out)

    print("== 7. with_connected but no connections dict -> no expansion ==")
    out = r(ALL, slugs="9121", with_connected=True, connections=None)
    check("no expansion without connections", out == ["9121_Shift"])

    print("== 8. neighbour not in corpus is dropped ==")
    out = set(r(ALL, slugs="9122", with_connected=True,
               connections={"9122_Claude": [{"slug": "9999_Ghost"}, {"slug": "1065_Y"}]}))
    check("ghost neighbour dropped, real kept",
          out == {"9122_Claude", "1065_Y"})

    print("== 9. no selector -> whole corpus ==")
    check("empty -> all", r(ALL) == ALL)

    print("== 10. _load_connections discovers topic dirs (no hardcoded names) ==")
    # 커스텀 토픽 설치에서 연결이 통째로 빠지던 회귀 가드: docs/ 를 스캔해
    # _paper_connections.json 을 가진 모든 디렉토리를 읽어야 한다.
    import json as _json
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        docs = os.path.join(tmp, "docs")
        for topic, conns in [
            ("ai4s", {"1_A": [{"slug": "2_B"}]}),
            ("my-custom-topic", {"3_C": [{"slug": "4_D"}]}),  # setup.py 임의 alias
        ]:
            os.makedirs(os.path.join(docs, topic))
            with open(os.path.join(docs, topic, "_paper_connections.json"),
                      "w", encoding="utf-8") as f:
                _json.dump(conns, f)
        os.makedirs(os.path.join(docs, "papers"))      # 연결 파일 없는 디렉토리
        os.makedirs(os.path.join(docs, "broken-topic"))
        with open(os.path.join(docs, "broken-topic", "_paper_connections.json"),
                  "w", encoding="utf-8") as f:
            f.write("{not json")                        # 손상 파일은 경고 후 스킵

        old_papers, old_cache = R.PAPERS, R._connections_cache
        try:
            R.PAPERS = os.path.join(docs, "papers")
            R._connections_cache = {}
            loaded = R._load_connections()
            check("기본 토픽 로드", "1_A" in loaded)
            check("커스텀 토픽도 로드 (하드코딩 제거)", "3_C" in loaded)
            check("손상 파일은 나머지를 막지 않음", len(loaded) == 2)
        finally:
            R.PAPERS, R._connections_cache = old_papers, old_cache

    print("== 11. _load_connections: freshest topic file wins for a shared paper ==")
    # 한 논문이 두 토픽에 속하면 두 파일에 같은 키가 있다. 예전엔 디렉토리 이름
    # 정렬순으로 update() 해서 알파벳상 뒤에 오는 파일이 이기게 돼 있었고,
    # 'ai4s-icml2026'('-') 가 'ai4s+scisci'('+') 뒤라 방금 재생성한 목록이 묵은
    # 목록으로 덮여 새 링크가 페이지에 못 올라왔다(2026-08-31, slug 10911).
    with tempfile.TemporaryDirectory() as tmp:
        docs = os.path.join(tmp, "docs")
        shared = "10911_paper_in_two_topics"
        # 알파벳상 뒤인 토픽을 먼저(=오래된 것으로) 쓴다.
        for topic, conns, mtime in [
            ("ai4s-icml2026", {shared: [{"slug": "1_Stale"}]}, 1_000_000),
            ("ai4s+scisci", {shared: [{"slug": "2_Fresh"}, {"slug": "3_Fresh"}]},
             2_000_000),
        ]:
            os.makedirs(os.path.join(docs, topic))
            path = os.path.join(docs, topic, "_paper_connections.json")
            with open(path, "w", encoding="utf-8") as f:
                _json.dump(conns, f)
            os.utime(path, (mtime, mtime))
        os.makedirs(os.path.join(docs, "papers"))

        old_papers, old_cache = R.PAPERS, R._connections_cache
        try:
            R.PAPERS = os.path.join(docs, "papers")
            R._connections_cache = {}
            loaded = R._load_connections()
            targets = [c["slug"] for c in loaded.get(shared, [])]
            check("알파벳상 뒤인 묵은 파일이 이기지 않음", "1_Stale" not in targets)
            check("최신 파일의 목록이 그대로 남음",
                  targets == ["2_Fresh", "3_Fresh"])
        finally:
            R.PAPERS, R._connections_cache = old_papers, old_cache

    print()
    if fails:
        print(f"RESULT: FAIL ({fails})")
        sys.exit(1)
    print("RESULT: ALL PASS")


if __name__ == "__main__":
    main()
