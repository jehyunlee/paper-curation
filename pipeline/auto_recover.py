"""
PDF↔review 오매칭 자동 복구 오케스트레이터 (T1-1 auto-recovery).

기존의 결정론적 복구 도구들(`audit_matching.py` → `fix_matching.py` →
`run_update_force.py`)을 하나의 `audit → judge → fix → re-review → re-audit`
루프로 묶어, 지금까지 사람이 손으로 이어붙이던 복구 글루를 자동화한다.

루프 한 라운드:
  1. audit_matching.py 를 서브프로세스로 실행 → docs/{topic}/_audit_report.json 로드
  2. 확정 오매칭 집합 결정:
       - "high" 버킷 슬러그는 전부 AUTO 확정
       - "medium" 버킷은 LLM(Anthropic tool-schema) 판정으로 true-mismatch 인
         것만 확정. `--no-llm` 이거나 ANTHROPIC_API_KEY 가 없으면 LLM 을 건너뛰고
         medium 은 보수적으로 '미확정' 처리.
  3. dry-run(기본): 어떤 슬러그를 fix+re-review 할지 계획만 출력하고 STOP — 변경 없음.
  4. --execute: 확정 슬러그에 대해 fix_matching.py --execute (자체 백업 생성) →
     run_update_force.py --slugs <those> --strict-pdf 재리뷰 → 다시 audit.
     확정 집합이 비거나 --max-rounds 도달까지 반복. 마지막에 라운드별 수렴 요약 출력.

안전장치:
  - 기본 dry-run (--execute 없으면 절대 삭제/재리뷰 안 함)
  - 어떤 에러(키 없음/네트워크/파싱 실패)에도 크래시하지 않고 현재 동작으로 graceful fallback
  - fix_matching.py 가 자체 백업을 만들고, 다른 토픽 공유 슬러그는 건너뛴다

Usage:
  # 계획만 (변경 0)
  PYTHONUTF8=1 python pipeline/auto_recover.py --topic ai4s
  # 실제 복구 (audit→fix→re-review→re-audit 반복)
  PYTHONUTF8=1 python pipeline/auto_recover.py --topic ai4s --execute
  # LLM 판정 끄고 high 만 보수적으로
  PYTHONUTF8=1 python pipeline/auto_recover.py --topic ai4s --no-llm
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

from config_loader import get_topic_dir, load_config

PIPELINE = Path(__file__).resolve().parent
PY = sys.executable

# medium 버킷 LLM 판정이 이 신뢰도 이상일 때만 확정으로 본다.
MEDIUM_CONFIRM_THRESHOLD = float(os.environ.get("AUTO_RECOVER_CONFIDENCE", "0.7"))
# medium 판정 모델 (Anthropic tool-use). 기본 Sonnet.
JUDGE_MODEL = os.environ.get("AUTO_RECOVER_JUDGE_MODEL", "claude-sonnet-5")


# ── Anthropic tool-schema verdict ────────────────────────────────────────────

VERDICT_SCHEMA = {
    "name": "emit_verdicts",
    "description": "각 논문의 PDF↔review 짝이 실제 오매칭인지 판정한다.",
    "input_schema": {
        "type": "object",
        "properties": {
            "verdicts": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "slug": {"type": "string"},
                        "is_mismatch": {"type": "boolean"},
                        "confidence": {
                            "type": "number",
                            "description": "0.0~1.0 사이 오매칭 확신도",
                        },
                        "reason_ko": {"type": "string"},
                    },
                    "required": ["slug", "is_mismatch", "confidence", "reason_ko"],
                },
            },
        },
        "required": ["verdicts"],
    },
}


def _fmt_check(checks, name):
    c = checks.get(name, {}) or {}
    passed = c.get("passed")
    state = {True: "PASS", False: "FAIL", None: "N/A"}.get(passed, "N/A")
    cov = c.get("coverage")
    cov_s = f" coverage={cov:.2f}" if isinstance(cov, (int, float)) else ""
    return f"{name.upper()}={state} ({c.get('reason', '?')}){cov_s}"


def _build_judge_prompt(medium_results):
    """medium 버킷 각 슬러그의 TITLE/DOI/ARXIV/REVIEW 시그널을 펼쳐 판정 프롬프트를 만든다."""
    lines = [
        "당신은 학술 논문 큐레이션 파이프라인의 PDF↔리뷰 매칭 감사관입니다.",
        "아래 각 항목은 '의심(medium)' 버킷으로 분류된 논문입니다. 각 검사 신호를 보고",
        "이 리뷰/PDF 짝이 실제 오매칭(잘못된 PDF로 리뷰가 생성됨)인지 판정하세요.",
        "",
        "검사 신호 의미:",
        "  - TITLE : index 제목 핵심어가 PDF 1페이지에 나타나는가 (FAIL=제목 안 보임)",
        "  - DOI   : index DOI 가 PDF 1페이지에 나타나는가 (N/A=DOI 없음, 보조 신호)",
        "  - ARXIV : arXiv ID 가 PDF 1페이지에 나타나는가 (N/A=arXiv 아님, 보조 신호)",
        "  - REVIEW: review.md 본문에 index 제목 핵심어가 나타나는가 (FAIL=본문이 다른 논문)",
        "",
        "판정 기준: TITLE 과 REVIEW 가 핵심 축. 둘 중 하나라도 명확히 FAIL 이고",
        "보조 신호(DOI/ARXIV)가 이를 반박하지 않으면 오매칭 가능성이 높다.",
        "DOI/ARXIV 가 PASS 면 clean 쪽으로 판단한다. 확신이 낮으면 confidence 를 낮게.",
        "",
    ]
    for r in medium_results:
        checks = r.get("checks", {}) or {}
        lines.append(f"### slug: {r.get('slug', '?')}")
        lines.append(f"  index_title: {r.get('title', '')}")
        if r.get("doi"):
            lines.append(f"  index_doi: {r.get('doi')}")
        for name in ("title", "doi", "arxiv", "review"):
            lines.append("  " + _fmt_check(checks, name))
        lines.append("")
    lines.append("emit_verdicts 도구로 각 slug 의 판정을 반환하세요. "
                 "reason_ko 는 한 문장 한국어.")
    return "\n".join(lines)


def _anthropic_judge(medium_results, *, model=JUDGE_MODEL):
    """기본 LLM 판정기. Anthropic tool-use 로 verdict 리스트를 반환한다.

    실패 시 예외를 raise — 호출부(build_plan)가 잡아 medium 을 '미확정'으로 fallback.
    """
    from lib.llm_client import get_chat_client
    client = get_chat_client(timeout=180.0, max_retries=4)
    prompt = _build_judge_prompt(medium_results)
    resp = client.messages.create(
        model=model,
        max_tokens=2000,
        tools=[VERDICT_SCHEMA],
        tool_choice={"type": "tool", "name": VERDICT_SCHEMA["name"]},
        messages=[{"role": "user", "content": prompt}],
    )
    for block in resp.content:
        if getattr(block, "type", None) == "tool_use" \
                and getattr(block, "name", None) == VERDICT_SCHEMA["name"]:
            return list(dict(block.input).get("verdicts", []))
    raise RuntimeError("emit_verdicts tool was not invoked")


# ── Reason helpers ───────────────────────────────────────────────────────────

def _high_reason_ko(r):
    dup = r.get("text_md_duplicate")
    if dup:
        peers = ", ".join(dup.get("peers", []))
        return f"text.md SHA 중복 (같은 PDF로 생성된 리뷰; peers={peers})"
    checks = r.get("checks", {}) or {}
    fails = [name.upper() for name in ("title", "doi", "arxiv", "review")
             if checks.get(name, {}).get("passed") is False]
    if fails:
        return f"확정 오매칭 ({', '.join(fails)} 검사 실패)"
    return "확정 오매칭 (high bucket)"


# ── Command builders (pure, testable) ────────────────────────────────────────

def _prefixes(slugs):
    """슬러그 리스트 → 정렬된 유니크 NNN 프리픽스 (fix_matching/run_update_force 규약)."""
    return sorted({s.split("_", 1)[0] for s in slugs})


def audit_command(topic):
    return [PY, "-u", str(PIPELINE / "audit_matching.py"), "--topic", topic]


def fix_command(topic, slugs):
    """fix_matching.py 를 확정 슬러그로 실제 실행(--execute). 자체 백업을 만든다."""
    return [PY, "-u", str(PIPELINE / "fix_matching.py"),
            "--topic", topic, "--slugs", ",".join(_prefixes(slugs)), "--execute"]


def rereview_command(topic, slugs):
    """run_update_force.py 로 정리된 슬러그를 재리뷰 (--strict-pdf 로 fuzzy 차단).

    --no-deploy 로 재리뷰 단계의 end-of-run 배포/ master push 를 차단한다 —
    무인 복구 루프가 사용자 모르게 Cloudflare 배포·git push 를 일으키지 않도록.
    복구 후 배포는 운영자가 명시적으로(run_full --mode deploy) 실행한다.
    """
    return [PY, "-u", str(PIPELINE / "run_update_force.py"),
            "--topic", topic, "--slugs", ",".join(_prefixes(slugs)),
            "--strict-pdf", "--no-deploy"]


# ── Planner (pure, testable) ─────────────────────────────────────────────────

def build_plan(report, *, no_llm=False, llm_judge=None, has_anthropic_key=None,
               slugs_filter=None, confidence_threshold=MEDIUM_CONFIRM_THRESHOLD):
    """audit report dict → 확정 오매칭 집합 결정 (순수 함수, 변경 없음).

    Returns a dict:
      {
        "high": [slug,...],                 # auto-confirmed
        "medium_confirmed": [slug,...],     # LLM judged true-mismatch
        "medium_rejected": [slug,...],      # LLM judged clean
        "medium_skipped": [slug,...],       # no LLM (no-llm / no key / LLM error)
        "confirmed": [{slug,bucket,reason_ko,confidence},...],
        "confirmed_slugs": [slug,...],
        "llm_used": bool,
        "llm_error": str|None,
      }
    """
    results = report.get("results", []) or []

    if slugs_filter:
        prefixes = [s.strip() for s in slugs_filter
                    if isinstance(s, str) and s.strip()] \
            if isinstance(slugs_filter, (list, tuple, set)) \
            else [s.strip() for s in str(slugs_filter).split(",") if s.strip()]
        if prefixes:
            results = [r for r in results
                       if any(str(r.get("slug", "")).startswith(p) for p in prefixes)]

    high = [r for r in results if r.get("confidence") == "high"]
    medium = [r for r in results if r.get("confidence") == "medium"]

    confirmed = []
    for r in high:
        confirmed.append({
            "slug": r["slug"], "bucket": "high",
            "reason_ko": _high_reason_ko(r), "confidence": 1.0,
        })

    if has_anthropic_key is None:
        has_anthropic_key = bool(
            os.environ.get("ANTHROPIC_API_KEY")
            or (load_config() or {}).get("anthropic_api_key", "")
        )

    medium_confirmed, medium_rejected, medium_skipped = [], [], []
    llm_used = False
    llm_error = None

    use_llm = bool(medium) and (not no_llm) and has_anthropic_key
    if use_llm:
        judge = llm_judge or _anthropic_judge
        try:
            verdicts = judge(medium) or []
            vmap = {v.get("slug"): v for v in verdicts if isinstance(v, dict)}
            llm_used = True
            for r in medium:
                v = vmap.get(r["slug"])
                if v and v.get("is_mismatch") and \
                        float(v.get("confidence", 0) or 0) >= confidence_threshold:
                    medium_confirmed.append(r["slug"])
                    confirmed.append({
                        "slug": r["slug"], "bucket": "medium",
                        "reason_ko": v.get("reason_ko", "(LLM 판정: 오매칭)"),
                        "confidence": float(v.get("confidence", 0) or 0),
                    })
                else:
                    medium_rejected.append(r["slug"])
        except Exception as e:  # graceful fallback: medium stays unconfirmed
            llm_error = f"{type(e).__name__}: {str(e)[:120]}"
            medium_skipped = [r["slug"] for r in medium]
    else:
        # --no-llm 또는 키 없음 → 보수적으로 medium 미확정
        medium_skipped = [r["slug"] for r in medium]

    return {
        "high": [r["slug"] for r in high],
        "medium_confirmed": medium_confirmed,
        "medium_rejected": medium_rejected,
        "medium_skipped": medium_skipped,
        "confirmed": confirmed,
        "confirmed_slugs": [c["slug"] for c in confirmed],
        "llm_used": llm_used,
        "llm_error": llm_error,
    }


def print_plan(plan, topic):
    """확정 집합 + fix/re-review 명령을 출력. 반환: {fix_cmd, rereview_cmd} (없으면 None)."""
    confirmed = plan["confirmed"]
    print(f"[auto-recover] high={len(plan['high'])} "
          f"medium_confirmed={len(plan['medium_confirmed'])} "
          f"medium_rejected={len(plan['medium_rejected'])} "
          f"medium_skipped={len(plan['medium_skipped'])}")
    if plan.get("llm_error"):
        print(f"[auto-recover] LLM judge error (medium left unconfirmed): {plan['llm_error']}")
    if not confirmed:
        print("[auto-recover] no confirmed mismatches in this round.")
        return None
    print(f"[auto-recover] {len(confirmed)} slug(s) would be fixed + re-reviewed:")
    for c in confirmed:
        print(f"  - {c['slug']}  [{c['bucket']}, conf={c['confidence']:.2f}]  {c['reason_ko']}")
    slugs = plan["confirmed_slugs"]
    fix_cmd = fix_command(topic, slugs)
    rer_cmd = rereview_command(topic, slugs)
    print("\n  fix      : " + " ".join(fix_cmd))
    print("  re-review: " + " ".join(rer_cmd))
    return {"fix_cmd": fix_cmd, "rereview_cmd": rer_cmd}


# ── Recovery loop ────────────────────────────────────────────────────────────

def _load_report(topic):
    p = get_topic_dir(topic) / "_audit_report.json"
    return json.loads(p.read_text(encoding="utf-8"))


def run_recover(topic, *, execute=False, max_rounds=2, no_llm=False,
                slugs_filter=None, llm_judge=None, run_cmd=subprocess.call):
    """audit → judge → (fix → re-review) → re-audit 루프.

    어떤 에러에도 크래시하지 않고 graceful 하게 반환한다.
    """
    rounds = []
    converged = False
    for rnd in range(1, max_rounds + 1):
        print(f"\n=== [auto-recover] round {rnd}/{max_rounds} — audit ({topic}) ===")
        try:
            rc = run_cmd(audit_command(topic))
        except Exception as e:
            print(f"[auto-recover] audit subprocess error ({e}); aborting gracefully")
            break
        if rc != 0:
            print(f"[auto-recover] audit exited {rc}; aborting gracefully")
            break
        try:
            report = _load_report(topic)
        except Exception as e:
            print(f"[auto-recover] could not load _audit_report.json ({e}); aborting gracefully")
            break

        plan = build_plan(report, no_llm=no_llm, slugs_filter=slugs_filter,
                          llm_judge=llm_judge)
        rounds.append({
            "round": rnd,
            "high": len(plan["high"]),
            "medium_confirmed": len(plan["medium_confirmed"]),
            "confirmed": len(plan["confirmed_slugs"]),
        })

        cmds = print_plan(plan, topic)
        confirmed = plan["confirmed_slugs"]
        if not confirmed:
            converged = True
            break

        if not execute:
            print("\n[auto-recover] DRY-RUN — no changes made. "
                  "Re-run with --execute to apply.")
            break

        # ── execute: fix (self-backup) then re-review ────────────────────────
        print(f"\n=== [auto-recover] round {rnd} — fix (delete artifacts) ===")
        try:
            rc = run_cmd(cmds["fix_cmd"])
        except Exception as e:
            print(f"[auto-recover] fix subprocess error ({e}); aborting gracefully")
            break
        if rc != 0:
            print(f"[auto-recover] fix exited {rc}; aborting gracefully")
            break

        print(f"\n=== [auto-recover] round {rnd} — re-review ===")
        try:
            rc = run_cmd(cmds["rereview_cmd"])
        except Exception as e:
            print(f"[auto-recover] re-review subprocess error ({e}); aborting gracefully")
            break
        if rc != 0:
            print(f"[auto-recover] re-review exited {rc}; aborting gracefully")
            break
        # loop continues → next round re-audits to verify convergence

    # ── convergence summary ──────────────────────────────────────────────────
    print("\n=== [auto-recover] convergence summary ===")
    print(f"  topic={topic}  mode={'EXECUTE' if execute else 'DRY-RUN'}  "
          f"rounds={len(rounds)}/{max_rounds}  converged={converged}")
    for s in rounds:
        print(f"  round {s['round']}: high={s['high']} "
              f"medium_confirmed={s['medium_confirmed']} "
              f"confirmed_total={s['confirmed']}")
    return {"rounds": rounds, "converged": converged, "execute": execute}


def main():
    ap = argparse.ArgumentParser(description="PDF↔review 오매칭 자동 복구 오케스트레이터")
    ap.add_argument("--topic", required=True)
    ap.add_argument("--execute", action="store_true",
                    help="실제 fix+재리뷰 수행. 기본은 dry-run (변경 없음).")
    ap.add_argument("--max-rounds", type=int, default=2,
                    help="audit→fix→re-review→re-audit 최대 반복 라운드 (기본 2).")
    ap.add_argument("--no-llm", action="store_true",
                    help="medium 버킷 LLM 판정을 건너뛰고 high 만 보수적으로 확정.")
    ap.add_argument("--slugs", default="",
                    help="특정 슬러그 프리픽스로 확정 집합을 제한 (테스트/범위 한정용).")
    args = ap.parse_args()

    slugs_filter = [s.strip() for s in args.slugs.split(",") if s.strip()] or None
    run_recover(topic=args.topic, execute=args.execute,
                max_rounds=args.max_rounds, no_llm=args.no_llm,
                slugs_filter=slugs_filter)


if __name__ == "__main__":
    from _env_guard import force_py312
    force_py312()
    main()
