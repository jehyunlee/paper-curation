"""Test the connection slug self-heal: build_slug_resolver + make_bidirectional_deduped(resolve=).

Papers keep their title but get re-assigned NNN over time, orphaning connection
endpoints stored by full slug ('1762_WoCoCo_…' once the paper is '1759_WoCoCo_…').
The resolver remaps such orphans to the current slug by title-part and prunes the
unresolvable (deleted / ambiguous). Pure stdlib; no LLM, no IO.

Run: PYTHONUTF8=1 /opt/homebrew/Caskroom/miniconda/base/envs/py312/bin/python \
       pipeline/tests/test_conn_remap.py
"""
import os
import sys

# NOTE: `pipeline/lib` 를 sys.path 에 직접 넣으면 안 된다. 그 디렉토리의
# `dateutil.py` 가 표준 `python-dateutil` 패키지를 가려서, 같은 프로세스에서
# pandas 를 import 하는 다른 테스트가 통째로 깨진다
# (`No module named 'dateutil.tz'; 'dateutil' is not a package`).
# `unittest discover` 는 실행 전에 모든 테스트 모듈을 import 하므로, 이 한 줄이
# 스위트 전체를 오염시켰다. 패키지 경로로 import 한다.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lib import connections as C  # noqa: E402

# 100_/200_ deliberately share title-part "Foo_Bar" -> ambiguous.
IDX = {"1759_WoCoCo_Learning_X", "9119_Unique_Paper", "100_Foo_Bar", "200_Foo_Bar"}


def main():
    fails = []

    def check(name, cond):
        print(f"  [{'PASS' if cond else 'FAIL'}] {name}")
        if not cond:
            fails.append(name)

    print("== 1. resolver: current / renumbered / deleted / ambiguous ==")
    r = C.build_slug_resolver(IDX)
    check("current slug -> itself", r("1759_WoCoCo_Learning_X") == "1759_WoCoCo_Learning_X")
    check("renumbered 1762 -> current 1759", r("1762_WoCoCo_Learning_X") == "1759_WoCoCo_Learning_X")
    check("deleted -> None", r("500_Totally_Gone") is None)
    check("ambiguous title-part -> None", r("300_Foo_Bar") is None)
    check("stats.remapped records 1762->1759",
          r.stats["remapped"].get("1762_WoCoCo_Learning_X") == "1759_WoCoCo_Learning_X")
    check("stats.pruned has the deleted + ambiguous",
          {"500_Totally_Gone", "300_Foo_Bar"} <= r.stats["pruned"])

    print("== 2. empty index -> identity, never prunes (safety guard) ==")
    r0 = C.build_slug_resolver(set())
    check("identity on empty index", r0("anything_123") == "anything_123")
    check("empty index prunes nothing", r0.stats["pruned"] == set())

    print("== 3. make_bidirectional_deduped(resolve=): remap + prune end-to-end ==")
    gconns = {
        # renumbered source; target is current -> edge kept, source remapped to 1759
        "1762_WoCoCo_Learning_X": [
            {"slug": "9119_Unique_Paper", "relation": "alternative", "reason": "r1"}],
        # deleted source -> its whole edge list dropped
        "500_Totally_Gone": [
            {"slug": "1759_WoCoCo_Learning_X", "relation": "foundation", "reason": "r2"}],
        # current source with a deleted target -> that edge dropped
        "9119_Unique_Paper": [
            {"slug": "777_Vanished", "relation": "extension", "reason": "r3"}],
    }
    bidi = C.make_bidirectional_deduped(gconns, resolve=C.build_slug_resolver(IDX))
    tgt = lambda s: {e["slug"] for e in bidi.get(s, [])}
    check("renumbered src 1762 folded into current 1759",
          "1762_WoCoCo_Learning_X" not in bidi and "1759_WoCoCo_Learning_X" in bidi)
    check("1759 -> 9119 forward kept", "9119_Unique_Paper" in tgt("1759_WoCoCo_Learning_X"))
    check("9119 -> 1759 reverse synthesized", "1759_WoCoCo_Learning_X" in tgt("9119_Unique_Paper"))
    check("deleted source 500 dropped", "500_Totally_Gone" not in bidi)
    check("deleted target 777 dropped (no 9119->777)", "777_Vanished" not in tgt("9119_Unique_Paper"))
    check("no orphan key 777 created", "777_Vanished" not in bidi)

    print("== 4. resolve=None -> backward compatible (no remap, no prune) ==")
    bidi2 = C.make_bidirectional_deduped(gconns)
    check("without resolver, 1762 stays as-is", "1762_WoCoCo_Learning_X" in bidi2)
    check("without resolver, deleted slugs survive", "500_Totally_Gone" in bidi2)

    print()
    if fails:
        print(f"RESULT: FAIL ({fails})")
        sys.exit(1)
    print("RESULT: ALL PASS")


if __name__ == "__main__":
    main()
