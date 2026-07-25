"""
Focused test for pipeline/lib/verify.py (T2-4 connection/insight verification).

This test imports ONLY pipeline/lib/verify.py — never the heavy clustering stack —
and proves:
  1. verify imports without pulling in umap / hdbscan / sentence-transformers / torch.
  2. verify_connections flags an absurd (unrelated) "extension" link as not-kept
     while keeping a plausible (genuinely related) link.
  3. apply_connection_verification(mode="strict") actually drops the spurious edge.
  4. verify_insights marks an insight citing irrelevant papers supported=False and a
     well-cited insight supported=True; apply_insight_verification drops the bad one.

It runs against a deterministic STUB client by default (a lexical-overlap judge that
exercises the real prompt construction + JSON parsing + drop/flag plumbing). If
ANTHROPIC_API_KEY is present, it ALSO does one small real Haiku call on the absurd
connection and prints the verdict (informational — not a hard assertion, to avoid
model-flakiness in CI).

Run:
  PYTHONUTF8=1 /opt/homebrew/Caskroom/miniconda/base/envs/py312/bin/python \
      pipeline/tests/test_verify.py
"""

import os
import re
import sys

# Import ONLY the target module — add pipeline/lib to sys.path so `import verify`
# resolves the single file directly (this does NOT execute lib/__init__.py and
# pulls in nothing beyond the stdlib).
# NOTE: `pipeline/lib` 를 sys.path 에 넣으면 그 안의 `dateutil.py` 가 표준
# `python-dateutil` 을 가려, 같은 프로세스에서 pandas 를 쓰는 테스트가 전부
# 깨진다. 패키지 경로로 import 한다.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lib import verify  # noqa: E402


# ─────────────────────────────────────────────────────────────────────────────
# Deterministic stub LLM client (no network). Parses verify.py's own prompts and
# judges relevance by lexical word-overlap, returning Anthropic-shaped responses.
# ─────────────────────────────────────────────────────────────────────────────

_STOP = set("the a an of for and or to in on with from this that paper papers "
            "study studies approach method methods using based via between two "
            "their its are is be as we our it relation reason claim cited "
            "evidence support supported topic research area new propose proposed "
            "novel work model models".split())


def _words(text):
    return {w for w in re.findall(r"[a-z]{4,}", (text or "").lower())
            if w not in _STOP}


def _overlap(a, b):
    wa, wb = _words(a), _words(b)
    if not wa or not wb:
        return 0.0
    return len(wa & wb) / len(wa | wb)


class _Block:
    def __init__(self, text):
        self.text = text
        self.type = "text"


class _Resp:
    def __init__(self, text):
        self.content = [_Block(text)]


class StubMessages:
    def __init__(self, threshold=0.06):
        self.threshold = threshold
        self.calls = 0

    def create(self, model=None, max_tokens=None, messages=None):
        self.calls += 1
        prompt = messages[0]["content"]
        if "related papers' link" in prompt:
            return _Resp(self._judge_connection(prompt))
        if "cross-category research insight" in prompt:
            return _Resp(self._judge_insight(prompt))
        return _Resp('{"kept": true, "verdict": "supported", "reason": "n/a"}')

    def _judge_connection(self, prompt):
        m = re.search(r"Paper A \[\d+\]: (.+?)\n\nPaper B \[\d+\]: (.+?)\n\n",
                      prompt, re.DOTALL)
        ess_a, ess_b = (m.group(1), m.group(2)) if m else ("", "")
        ok = _overlap(ess_a, ess_b) >= self.threshold
        verdict = "supported" if ok else "spurious"
        return ('{"kept": %s, "verdict": "%s", "reason": "overlap=%s"}'
                % ("true" if ok else "false", verdict, str(ok).lower()))

    def _judge_insight(self, prompt):
        cm = re.search(r"Claim: (.+?)\n\n", prompt, re.DOTALL)
        ev = re.search(r"Papers cited as evidence for this claim:\n(.+?)\n\n",
                       prompt, re.DOTALL)
        claim = cm.group(1) if cm else ""
        cited = ev.group(1) if ev else ""
        ok = bool(claim) and bool(cited.strip()) and \
            "not found in corpus" not in cited and \
            _overlap(claim, cited) >= self.threshold
        return ('{"supported": %s, "reason": "overlap-check"}'
                % ("true" if ok else "false"))


class StubClient:
    def __init__(self, threshold=0.06):
        self.messages = StubMessages(threshold)


# ─────────────────────────────────────────────────────────────────────────────
# Synthetic corpus
# ─────────────────────────────────────────────────────────────────────────────

ESSENCE = {
    "001_GNN_Molecular": {
        "title": "Graph neural networks for molecular property prediction",
        "essence": ("A graph neural network that predicts molecular properties by "
                    "message passing over atom-bond graphs of small molecules for "
                    "drug discovery."),
    },
    "002_MPNN_Molecules": {
        "title": "Message passing neural networks for molecules",
        "essence": ("Message passing neural network architecture learning molecular "
                    "representations from atom graphs, improving molecular property "
                    "prediction over fingerprint baselines."),
    },
    "003_Medieval_Poetry": {
        "title": "Structure of medieval French sonnet poetry",
        "essence": ("A literary analysis of rhyme, meter, and stanza structure in "
                    "medieval French sonnet poetry across the 14th century."),
    },
}

# One plausible edge (001 extends 002: both GNN/molecular) + one absurd edge
# (001 "extension" of 003: GNN molecules vs medieval poetry — unrelated).
CONNECTIONS = {
    "001_GNN_Molecular": [
        {"slug": "002_MPNN_Molecules", "relation": "extension",
         "reason": "분자 그래프 메시지 패싱을 확장한다"},
        {"slug": "003_Medieval_Poetry", "relation": "extension",
         "reason": "중세 시 구조를 확장한다 (의심스러운 연결)"},
    ],
}

# One well-supported insight (cites the two GNN/molecular papers) + one unsupported
# insight (claims a molecular-ML convergence but cites only the poetry paper).
INSIGHTS = {
    "cross_category": [
        {"type": "convergence", "title": "GNN-분자 수렴",
         "description": ("Graph neural networks and message passing are converging "
                         "for molecular property prediction in drug discovery."),
         "categories": ["ML", "Chemistry"],
         "evidence": ["001", "002"], "signal_strength": "strong",
         "policy_implication": "분자 ML 투자 확대"},
        {"type": "convergence", "title": "분자ML-문학 융합",
         "description": ("Molecular machine learning for drug discovery is merging "
                         "with graph neural network message passing methods."),
         "categories": ["ML", "Chemistry"],
         "evidence": ["003"], "signal_strength": "strong",
         "policy_implication": "근거 없음"},
    ],
    "per_category": {}, "meta": {},
}

PAPER_META = {n.split("_")[0]: v for n, v in ESSENCE.items()}


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

    print("== 1. dependency-light import ==")
    heavy = [m for m in ("umap", "hdbscan", "sentence_transformers", "torch",
                          "numba", "llvmlite")
             if m in sys.modules]
    check("verify imported", "verify" in sys.modules)
    check(f"no heavy deps loaded (found: {heavy or 'none'})", not heavy)

    print("== 2. verify_connections: absurd flagged, plausible kept (stub) ==")
    stub = StubClient()
    results = verify.verify_connections(CONNECTIONS, ESSENCE, stub, sample_n=0)
    by_tgt = {verify._slug_num(r["target"]): r for r in results}
    check("checked both edges", len(results) == 2)
    check("plausible 001->002 kept", by_tgt["002"]["kept"] is True)
    check("absurd 001->003 NOT kept", by_tgt["003"]["kept"] is False)
    check("absurd verdict == spurious", by_tgt["003"]["verdict"] == "spurious")

    print("== 3. apply_connection_verification strict drops the spurious edge ==")
    conns = {k: [dict(c) for c in v] for k, v in CONNECTIONS.items()}
    logs, logfn = _logs()
    os.environ.pop("VERIFY_CONNECTIONS_SAMPLE", None)
    verify.apply_connection_verification(
        conns, ESSENCE, stub, mode="strict", sample_n=0, log=logfn)
    remaining = {verify._slug_num(c["slug"]) for c in conns["001_GNN_Molecular"]}
    check("strict kept plausible 002", "002" in remaining)
    check("strict dropped absurd 003", "003" not in remaining)

    print("== 3b. sample (flag-only) mode keeps everything ==")
    conns2 = {k: [dict(c) for c in v] for k, v in CONNECTIONS.items()}
    _, logfn2 = _logs()
    verify.apply_connection_verification(
        conns2, ESSENCE, stub, mode="sample", sample_n=0, log=logfn2)
    check("sample mode keeps both edges",
          len(conns2["001_GNN_Molecular"]) == 2)

    print("== 3c. off mode is a no-op ==")
    conns3 = {k: [dict(c) for c in v] for k, v in CONNECTIONS.items()}
    verify.apply_connection_verification(
        conns3, ESSENCE, stub, mode="off", log=lambda m: None)
    check("off mode keeps both edges", len(conns3["001_GNN_Molecular"]) == 2)

    print("== 4. verify_insights: irrelevant citation -> supported False (stub) ==")
    ins = {"cross_category": [dict(i) for i in INSIGHTS["cross_category"]],
           "per_category": {}, "meta": {}}
    verify.verify_insights(ins, PAPER_META, stub)
    items = ins["cross_category"]
    check("well-cited insight supported", items[0]["supported"] is True)
    check("irrelevant-cited insight NOT supported", items[1]["supported"] is False)

    print("== 5. apply_insight_verification drops unsupported (default ON) ==")
    ins2 = {"cross_category": [dict(i) for i in INSIGHTS["cross_category"]],
            "per_category": {}, "meta": {}}
    os.environ.pop("VERIFY_INSIGHTS", None)
    _, logfn3 = _logs()
    verify.apply_insight_verification(ins2, PAPER_META, stub, log=logfn3)
    titles = [i["title"] for i in ins2["cross_category"]]
    check("kept supported insight", "GNN-분자 수렴" in titles)
    check("dropped unsupported insight", "분자ML-문학 융합" not in titles)
    check("dropped insight stashed", len(ins2.get("_verify_dropped", [])) == 1)

    print("== 6. graceful fallback: VERIFY_INSIGHTS=0 disables ==")
    ins3 = {"cross_category": [dict(i) for i in INSIGHTS["cross_category"]],
            "per_category": {}, "meta": {}}
    os.environ["VERIFY_INSIGHTS"] = "0"
    verify.apply_insight_verification(ins3, PAPER_META, stub, log=lambda m: None)
    os.environ.pop("VERIFY_INSIGHTS", None)
    check("disabled keeps both insights", len(ins3["cross_category"]) == 2)

    print("== 7. graceful fallback: client=None never raises / drops ==")
    ins4 = {"cross_category": [dict(i) for i in INSIGHTS["cross_category"]],
            "per_category": {}, "meta": {}}
    verify.apply_insight_verification(ins4, PAPER_META, None, log=lambda m: None)
    check("no-client keeps both insights", len(ins4["cross_category"]) == 2)
    conns4 = {k: [dict(c) for c in v] for k, v in CONNECTIONS.items()}
    verify.apply_connection_verification(
        conns4, ESSENCE, None, mode="strict", log=lambda m: None)
    check("no-client keeps both edges", len(conns4["001_GNN_Molecular"]) == 2)

    print("== 7b. graceful fallback: bad client (raises) keeps originals ==")
    class _BoomMessages:
        def create(self, **kw):
            raise RuntimeError("simulated API failure")

    class _BoomClient:
        messages = _BoomMessages()

    res_boom = verify.verify_connections(CONNECTIONS, ESSENCE, _BoomClient(), sample_n=0)
    check("api error -> all edges kept", all(r["kept"] for r in res_boom))
    check("api error -> verdict==error", all(r["verdict"] == "error" for r in res_boom))

    # Optional real Haiku call (informational only).
    if os.environ.get("ANTHROPIC_API_KEY"):
        print("== 8. real Haiku call on absurd connection (informational) ==")
        try:
            from anthropic import Anthropic
            real = Anthropic(timeout=180.0, max_retries=4)
            rres = verify.verify_connections(
                {"001_GNN_Molecular": [CONNECTIONS["001_GNN_Molecular"][1]]},
                ESSENCE, real, sample_n=0)
            r = rres[0]
            print(f"     real verdict for 001->003 (absurd 'extension'): "
                  f"kept={r['kept']} verdict={r['verdict']} reason={r['verify_reason']!r}")
            print(f"     (soft check) real model flagged absurd as not-kept: "
                  f"{r['kept'] is False}")
        except Exception as e:
            print(f"     real call skipped ({type(e).__name__}: {str(e)[:80]})")
    else:
        print("== 8. real Haiku call skipped (no ANTHROPIC_API_KEY) ==")

    print()
    if failures:
        print(f"RESULT: FAIL ({len(failures)} failed: {failures})")
        sys.exit(1)
    print("RESULT: ALL PASS")


if __name__ == "__main__":
    main()
