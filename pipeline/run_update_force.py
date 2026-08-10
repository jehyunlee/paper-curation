"""
Paper-Curation --local --update-force 배치 실행 스크립트.

사용법:
  PYTHONUTF8=1 python run_update_force.py --topic ai4s
  # --concurrency 기본값 16 (Anthropic Tier 4). Tier 1~3 은 4~12 로 낮춤.

기능:
  1. Zotero 컬렉션에서 전체 논문 fetch
  2. 기존 review.md, text.md, figures/ 삭제
  3. PDF 파싱 → text.md
  4. Figure 추출 + Gemini Flash 검증 (5라운드, 감쇠)
  5. review.md 작성 (Claude Haiku)
  6. index.html 변환 (review_to_html.py)
  7. 진행 상황을 checkpoint.json에 저장 (중단 후 재개 가능)

소요 시간 예상: 840편 × 병렬 4 = ~20시간
"""

import argparse
import json
import os
import queue
import re
import shutil
import subprocess
import sys
import time
import urllib.request
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

# Paths
from config_loader import (
    PAPERS_DIR as _PAPERS_DIR, PIPELINE_DIR, _ssl_ctx,
    get_zotero_api_key, get_zotero_user_id, get_collection_key, get_collections, get_zotero_dir,
    get_topic_dir, get_google_key,
)
from lib.categories import category_slug
PAPERS_DIR = str(_PAPERS_DIR)
PROJECT_ROOT = PIPELINE_DIR.parent


def _split_cats_by_image_presence(topic, cats):
    """Split categories by whether their timeline image exists.

    Returns (cats_with_image, cats_missing_image).
    Image path: docs/{topic}/category_timeline_{slug}.{png,webp}
    """
    topic_dir = get_topic_dir(topic)
    with_image = []
    missing = []
    for cat in cats:
        slug = category_slug(cat)
        has_image = any(
            os.path.exists(os.path.join(str(topic_dir), f"category_timeline_{slug}.{ext}"))
            for ext in ("png", "webp")
        )
        (with_image if has_image else missing).append(cat)
    return with_image, missing


def _topic_default_artifacts_missing(topic):
    """Return missing default topic outputs for a complete collection page.

    Paper Curio collection processing is an "ensure the collection is browsable"
    entrypoint, not just "review new PDFs". A failed first run can leave the
    checkpoint full while narrative/timeline artifacts are absent; resume mode
    must detect that and rebuild the missing default outputs.
    """
    topic_dir = get_topic_dir(topic)
    topic_dir_str = str(topic_dir)
    missing = []
    required = [
        "_category_summaries.json",
        "_category_narratives.json",
        "_timeline_narrative.json",
        "research_timeline.png",
    ]
    for name in required:
        path = os.path.join(topic_dir_str, name)
        if not os.path.exists(path) or os.path.getsize(path) == 0:
            missing.append(name)

    expected_categories = []
    cls_path = os.path.join(topic_dir_str, "_new_classification.json")
    if os.path.exists(cls_path):
        try:
            with open(cls_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            for c in data.get("categories", []):
                name = c.get("name") if isinstance(c, dict) else str(c)
                if name and name != "Other":
                    expected_categories.append(name)
        except Exception:
            expected_categories = []

    if expected_categories:
        for cat in expected_categories:
            slug = category_slug(cat)
            has_image = any(
                os.path.exists(os.path.join(topic_dir_str, f"category_timeline_{slug}.{ext}"))
                and os.path.getsize(os.path.join(topic_dir_str, f"category_timeline_{slug}.{ext}")) > 0
                for ext in ("png", "webp")
            )
            if not has_image:
                missing.append(f"category_timeline_{slug}.png")
    elif not os.path.isdir(topic_dir_str) or not any(
        name.startswith("category_timeline_") and name.endswith((".png", ".webp"))
        for name in os.listdir(topic_dir_str)
    ):
        missing.append("category_timeline_*.png")

    return missing

# topic_modeling.py / classify_papers.py 는 UMAP + hdbscan + sentence-transformers
# 의존. 표준은 ``py312`` 단일 env 이며, 이 경우 현재 인터프리터가 곧 클러스터링
# 인터프리터다. 과거의 "py314 메인 + py312 보조" 이중 구성도 계속 지원한다: py314
# 에서는 UMAP.transform 가 sklearn.pairwise_distances 에 callable metric 을 넘기는
# 순간 numba 가 JIT 컴파일을 시도하는데, numba 의 bytecode interpreter 가 Python
# 3.14 의 ``CALL_KW`` opcode 를 아직 처리하지 못해
# (``op_CALL_KW: pop from empty list``, 0.65.1 / 0.66.0rc1 / main 모두 동일) 분류가
# 죽으므로, 클러스터링·분류만 형제 ``py312`` 인터프리터로 라우팅한다.
#
# 해석 순서:
#   0. 현재 인터프리터 프로브 — 클러스터링 *실경로* (UMAP cosine fit→transform +
#      hdbscan approximate_predict) 를 소형 데이터로 실행하는 서브프로세스가
#      성공하면 단일 env 로 보고 ``sys.executable`` 을 그대로 쓴다. import-only
#      프로브는 JIT 시점 크래시를 못 잡아 거짓 양성을 내므로 쓰지 않는다.
#      판정은 _state/env_probe.json 에 영구 캐시 (첫 1회만 JIT 비용 ~수십 초).
#   프로브 실패(의존성 미설치 또는 JIT 크래시) 시 기존 fallback 체인을 그대로 탄다:
#   1. ``PAPER_CURATION_PY312`` 환경변수 — 운영자가 명시한 절대 경로
#   2. 현재 인터프리터의 conda prefix 에서 형제 env (../py312/bin/python)
#   3. ``which python3.12`` PATH 검색
#   4. fallback → ``sys.executable`` (운영자 환경이 이미 py312 이면 동작)
_PROBE_RESULT = None  # None=미실행, True=현재 인터프리터로 클러스터링 가능, False=불가

# 프로브는 import 가 아니라 *실제 크래시 경로* 를 실행한다. numba CALL_KW 류의
# 실패는 import 시점이 아니라 UMAP.transform()/approximate_predict() 의 JIT
# 컴파일 시점에 터지므로, import-only 프로브는 py314 에서 거짓 양성을 낸다
# (import 성공 → 단일 env 판정 → 분류 단계 mid-run 크래시). 아래 스니펫은
# topic_modeling/classify 가 쓰는 경로(UMAP cosine fit→transform,
# hdbscan approximate_predict)를 소형 데이터로 그대로 통과시킨다.
# 첫 실행은 numba JIT 때문에 수십 초 걸리므로 판정을 _state/env_probe.json 에
# (인터프리터 경로, 파이썬 버전) 키로 영구 캐시한다. env 의 numba 를 갈아끼운
# 뒤 재판정이 필요하면 그 파일을 지우면 된다.
_PROBE_SNIPPET = (
    # sentence_transformers/adapters 까지 요구하는 이유: topic_modeling 은 SPECTER2
    # 임베딩이 필수이고, adapters 가 없으면 proximity 어댑터 대신 mean-pooling
    # fallback 으로 *조용히 품질이 떨어진* 번들을 만든다. 어댑터까지 갖춘 env 만
    # "단일 env" 로 인정해 EMBED_TAG(proximity vs fallback)가 env 에 따라 갈라지는
    # 것을 막는다. 모두 없는 환경이라도 fallback 체인의 마지막이 sys.executable
    # 이므로 동작 자체는 유지된다(이때는 specter2_embed 가 경고와 함께 fallback).
    "import sentence_transformers, adapters\n"
    "import numpy as np, numba, umap, hdbscan\n"
    "rs = np.random.RandomState(0)\n"
    "X = rs.rand(60, 32).astype('float32')\n"
    "um = umap.UMAP(n_components=5, n_neighbors=8, metric='cosine',"
    " random_state=42).fit(X)\n"
    "um.transform(rs.rand(3, 32).astype('float32'))\n"
    "cl = hdbscan.HDBSCAN(min_cluster_size=3, prediction_data=True)"
    ".fit(um.embedding_.astype('float64'))\n"
    "import hdbscan.prediction as hp\n"
    "hp.approximate_predict(cl, um.transform(rs.rand(2, 32).astype('float32'))"
    ".astype('float64'))\n"
    "print('PROBE_OK numba', numba.__version__)\n"
)
import pathlib as _pathlib
_PROBE_STATE = _pathlib.Path(__file__).resolve().parent / "_state" / "env_probe.json"


def _probe_current_interpreter():
    """현재 인터프리터로 클러스터링 실경로가 도는지 1회 판정 (영구 캐시).

    의존성 미설치(즉시 ImportError)·JIT 크래시·타임아웃 모두 False.
    판정은 프로세스 전역 + ``_state/env_probe.json`` 에 캐시된다.
    """
    global _PROBE_RESULT
    if _PROBE_RESULT is not None:
        return _PROBE_RESULT

    key = f"{sys.executable}|py{sys.version_info[0]}.{sys.version_info[1]}"
    try:
        state = json.loads(_PROBE_STATE.read_text(encoding="utf-8"))
    except Exception:
        state = {}
    cached = state.get(key)
    if isinstance(cached, dict) and "ok" in cached:
        _PROBE_RESULT = bool(cached["ok"])
        return _PROBE_RESULT

    try:
        r = subprocess.run(
            [sys.executable, "-c", _PROBE_SNIPPET],
            capture_output=True, text=True, timeout=180,
        )
        ok = (r.returncode == 0 and "PROBE_OK" in (r.stdout or ""))
        detail = (r.stdout if ok else (r.stderr or ""))[-200:].strip()
    except Exception as e:
        ok, detail = False, f"{type(e).__name__}: {str(e)[:120]}"

    _PROBE_RESULT = ok
    try:
        state[key] = {"ok": ok, "detail": detail,
                      "ts": datetime.now().isoformat(timespec="seconds")}
        _PROBE_STATE.parent.mkdir(parents=True, exist_ok=True)
        _PROBE_STATE.write_text(
            json.dumps(state, ensure_ascii=False, indent=1), encoding="utf-8")
    except Exception:
        pass  # 캐시 실패는 치명적이지 않음 (다음 실행에서 재프로브)
    return _PROBE_RESULT


def _resolve_topic_modeling_python():
    # 표준: py312 단독 환경. py314 등 다른 인터프리터로는 **절대 라우팅하지 않는다**.
    # (운영자 지시 2026-06-18: py312 단독 사용, py314 진입 경로 전면 차단.)
    # 0. 현재 인터프리터가 이미 py312 + 클러스터링 의존성을 직접 import 할 수 있으면
    #    그대로 사용 (단일 env 표준 경로).
    from pathlib import Path as _Path
    import shutil as _shutil
    if sys.version_info[:2] == (3, 12) and _probe_current_interpreter():
        return sys.executable
    # 그 외(예: py314 에서 호출) → py312 인터프리터로 라우팅. py314 로는 절대 가지 않는다.
    #   1) PAPER_CURATION_PY312 명시 경로
    explicit = os.environ.get("PAPER_CURATION_PY312", "").strip()
    if explicit and os.path.exists(explicit):
        return explicit
    #   2) 형제 conda env <base>/envs/py312/bin/python
    here = _Path(sys.executable).resolve()
    for anc in here.parents:
        if anc.name == "envs":
            cand = anc / "py312" / "bin" / "python"
            if cand.exists():
                return str(cand)
            break
    #   3) PATH 의 python3.12
    found = _shutil.which("python3.12")
    if found:
        return found
    #   4) 현재 인터프리터가 py312 면 그대로 (의존성 미설치 상태일 수 있음)
    if sys.version_info[:2] == (3, 12):
        return sys.executable
    # py312 를 못 찾으면 py314 로 진행하지 않고 명확히 실패한다.
    raise RuntimeError(
        "py312 인터프리터를 찾을 수 없습니다. paper-curation 은 py312 단독 환경을 사용합니다 "
        "(py314 사용 금지). conda env py312 를 만들거나 PAPER_CURATION_PY312 로 절대 경로를 지정하세요."
    )


TOPIC_MODELING_PYTHON = _resolve_topic_modeling_python()
if TOPIC_MODELING_PYTHON != sys.executable:
    print(f"[env] UMAP/HDBSCAN 단계 인터프리터: {TOPIC_MODELING_PYTHON} "
          f"(현재 env 가 py312 가 아니거나 프로브 실패 → py312 라우팅; 사유는 _state/env_probe.json)")

ZOTERO_DIR = get_zotero_dir()

API_KEY = get_zotero_api_key()
USER_ID = get_zotero_user_id()
COLLECTIONS = get_collections()

# Checkpoint
PROGRESS_FILE = PROJECT_ROOT / ".cache" / "review_progress.json"
_progress_lock = threading.Lock()
_progress_state = {"topic": "", "total": 0, "done": 0, "failed": 0,
                   "slug": "", "phase": "", "status": "idle",
                   "updated_at": ""}


def _update_progress(*, topic=None, total=None, done=None, failed=None,
                     slug=None, phase=None, status=None):
    with _progress_lock:
        for key, value in (("topic", topic), ("total", total), ("done", done),
                           ("failed", failed), ("slug", slug), ("phase", phase),
                           ("status", status)):
            if value is not None:
                _progress_state[key] = value
        _progress_state["updated_at"] = datetime.now().isoformat(timespec="seconds")
        try:
            from lib.atomic_io import atomic_write_json
            PROGRESS_FILE.parent.mkdir(parents=True, exist_ok=True)
            atomic_write_json(str(PROGRESS_FILE), dict(_progress_state))
        except Exception:
            pass


def _paper_progress(slug, phase):
    with _progress_lock:
        total = int(_progress_state.get("total") or 0)
        done = int(_progress_state.get("done") or 0)
    percent = (done / total * 100) if total else 0
    _update_progress(slug=slug, phase=phase)
    return f"[review {done}/{total} {percent:.1f}% | {phase}] {slug}"

CHECKPOINT_FILE = str(PIPELINE_DIR / "_update_force_checkpoint.json")


def log(msg):
    ts = datetime.now().strftime("%H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)


def sync_bibliography_db(direction):
    """A bibliography synchronization failure blocks the update publication path."""
    result = subprocess.run(
        [sys.executable, str(PIPELINE_DIR / "sync_bibliography_db.py"), direction],
        cwd=str(PROJECT_ROOT), capture_output=True, text=True, timeout=180,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"bibliography sync failed ({direction}): "
            f"{result.stderr.strip() or result.stdout.strip()}")
    if result.stdout.strip():
        log(f"[bibliography-sync] {result.stdout.strip()}")


def run_bibliography_release_steps(run_step):
    """Build, validate, then publish; a failed gate prevents the push call."""
    # Institution normalisation needs the ROR index and the curated group table.
    # Both live under gitignored `.cache/`, so without this step a wiped cache
    # degrades silently to raw PDF affiliation strings.
    run_step(
        "setup_affiliation_sources",
        ["python", "pipeline/setup_affiliation_sources.py"],
        1800,
    )
    # No --offline/--skip-zotero here. Both switches disable the Zotero read
    # (build_bibliography_db.py:1797) and --offline also disables Scopus
    # (:1851), which would leave newly ingested papers without a
    # `zotero_item_key` and outside the Zotero-first bibliography policy —
    # exactly the papers that need it. The Zotero library scan is a fixed ~200s
    # per cycle no matter how many papers changed.
    run_step(
        "build_bibliography_db",
        ["python", "pipeline/build_bibliography_db.py", "--changed-only",
         "--no-email"],
        7200,
    )
    run_step(
        "check_bibliography_db",
        ["python", "pipeline/check_bibliography_db.py", "--strict"],
        600,
    )
    run_step(
        "sync_bibliography_db (push)",
        ["python", "pipeline/sync_bibliography_db.py", "--push"],
        180,
    )


def load_checkpoint():
    # A truncated/corrupt checkpoint (process killed mid-flush) must NOT crash
    # the run before any work begins — degrade to the empty default instead.
    # The --skip-existing/PDF-mtime scan re-marks slugs with a valid review.md
    # as completed, so most prior work is recovered for free.
    if os.path.exists(CHECKPOINT_FILE):
        try:
            with open(CHECKPOINT_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError, ValueError) as e:
            log(f"  WARN checkpoint corrupt ({type(e).__name__}); "
                f"starting fresh — completed papers re-detected from review.md")
    return {"completed": [], "failed": [], "phase": "init"}


_cp_lock = threading.Lock()
_slug_to_zotero_key = {}
_slug_to_pdf_path = {}  # populated by find_pdf hits; persisted to _papers_index.json for PDF-change detection on subsequent runs


def save_checkpoint(cp):
    # Atomic write (tmp + os.replace) so a kill mid-flush leaves the reader the
    # old complete file rather than a half-written one. _cp_lock still
    # serializes concurrent writers AND the json serialization (callers may
    # append to cp['completed'] from other threads).
    from lib.atomic_io import atomic_write_json
    with _cp_lock:
        atomic_write_json(CHECKPOINT_FILE, cp)


# ── Phase 1: Fetch Zotero ──

def fetch_zotero_items(collection_key):
    items = []
    start = 0
    while True:
        url = (f"https://api.zotero.org/users/{USER_ID}/collections/"
               f"{collection_key}/items/top?limit=100&start={start}&format=json&sort=title")
        # Korea-to-Zotero links drop connections mid-stream; retry with exp backoff.
        last_err = None
        batch = None
        for attempt in range(5):
            try:
                req = urllib.request.Request(url, headers={"Zotero-API-Key": API_KEY})
                with urllib.request.urlopen(req, timeout=30, context=_ssl_ctx) as resp:
                    batch = json.load(resp)
                break
            except Exception as e:
                last_err = e
                wait = min(60, 2 * (2 ** attempt))
                print(f"[fetch_zotero_items] attempt {attempt+1}/5 (start={start}) failed: "
                      f"{type(e).__name__}: {str(e)[:120]}; sleeping {wait}s", flush=True)
                import time as _t; _t.sleep(wait)
        if batch is None:
            raise RuntimeError(f"fetch_zotero_items exhausted retries at start={start}: {last_err}")
        if not batch:
            break
        for item in batch:
            d = item["data"]
            if d.get("itemType") in ("attachment", "note",
                                      "forumPost", "videoRecording"):
                continue
            items.append(d)
        start += 100
        if len(batch) < 100:
            break
    return items


# ── PDF match audit log (Phase 1a: diagnose 139-paper mismatch bug) ──
# Every find_pdf() call appends one JSON line to this file so we can
# retroactively audit which matches used the weak fuzzy fallback.
_AUDIT_LOG_PATH = None  # lazily initialised in _audit_append()


def _audit_append(record):
    """Append one JSONL record to the find_pdf audit log."""
    global _AUDIT_LOG_PATH
    try:
        if _AUDIT_LOG_PATH is None:
            logs_dir = os.path.join(os.path.dirname(__file__), "_logs")
            os.makedirs(logs_dir, exist_ok=True)
            ts = datetime.now().strftime("%Y%m%d_%H%M%S")
            _AUDIT_LOG_PATH = os.path.join(logs_dir, f"find_pdf_audit_{ts}.jsonl")
        with open(_AUDIT_LOG_PATH, "a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
    except Exception:
        pass  # audit log never breaks the pipeline


def _extract_arxiv_id_from_item(item):
    """Try to read an arXiv ID from a Zotero item's url/DOI/archiveID."""
    for field in ("url", "DOI", "archiveID", "extra"):
        val = item.get(field, "") or ""
        m = re.search(r"(\d{4}\.\d{4,5})", val)
        if m:
            return m.group(1)
    return None


# Global flag toggled by CLI. When True, fuzzy fallback is disabled entirely.
_STRICT_PDF = False


def find_pdf(item):
    """Find local PDF path for a Zotero item.

    Returns (path, method). `method` is one of:
      - zotero_children_abs     : Zotero child API returned an absolute path that exists
      - zotero_children_basename: Zotero child API path's basename found under ZOTERO_DIR
      - doi_filename            : DOI string appears in a PDF filename under ZOTERO_DIR
      - arxiv_filename          : arXiv ID appears in a PDF filename under ZOTERO_DIR
      - fuzzy                   : weak title-keyword match (LAST RESORT, logged)
      - no_match                : no candidate — caller skips the paper
    """
    key = item.get("key", "")
    title = item.get("title", "")

    # Priority 1: Zotero children API (authoritative attachment path)
    try:
        url = f"https://api.zotero.org/users/{USER_ID}/items/{key}/children?format=json"
        req = urllib.request.Request(url, headers={"Zotero-API-Key": API_KEY})
        with urllib.request.urlopen(req, timeout=10, context=_ssl_ctx) as resp:
            children = json.load(resp)
        for c in children:
            cd = c.get("data", {})
            if cd.get("itemType") != "attachment":
                continue
            if cd.get("contentType") not in ("application/pdf", ""):
                continue
            path = cd.get("path", "")
            if not path.lower().endswith(".pdf"):
                continue
            # Zotero "Linked Attachment Base Directory" stores paths as
            # `attachments:<filename>` (relative to ZOTERO_DIR). Strip the
            # prefix so os.path.exists/basename work against the real file.
            if path.startswith("attachments:"):
                rel = path[len("attachments:"):]
                resolved = os.path.join(ZOTERO_DIR, rel)
                if os.path.exists(resolved):
                    _audit_append({"key": key, "title": title[:80],
                                   "method": "zotero_children_attachments_uri",
                                   "path": resolved})
                    return resolved, "zotero_children_abs"
            if os.path.exists(path):
                _audit_append({"key": key, "title": title[:80],
                               "method": "zotero_children_abs", "path": path})
                return path, "zotero_children_abs"
            # Cross-platform basename extraction: Zotero may have stored a
            # Windows-style absolute path (``C:\Users\...\Foo.pdf``) when the
            # item was added on Windows, then the user re-attached the
            # collection on macOS via "Linked Attachment Base Directory".
            # ``os.path.basename`` on POSIX doesn't treat backslash as a
            # separator, so we'd otherwise treat the whole path as the
            # filename and never resolve it. Normalise to forward slashes
            # first so the basename works on either separator.
            fname = path.replace("\\", "/").rsplit("/", 1)[-1]
            alt = os.path.join(ZOTERO_DIR, fname)
            if os.path.exists(alt):
                _audit_append({"key": key, "title": title[:80],
                               "method": "zotero_children_basename", "path": alt})
                return alt, "zotero_children_basename"
    except Exception as e:
        _audit_append({"key": key, "title": title[:80],
                       "method": "children_api_error", "error": str(e)[:200]})

    # Priority 2: DOI in filename (reliable when present)
    # Bare substring containment collides on prefix-DOIs ('10.1234/abc' is a
    # substring of '10.1234/abc.suppl'). Require the matched region to be
    # bounded — followed by end-of-name or a non-alphanumeric separator in the
    # ORIGINAL filename — and treat 2+ matches as ambiguous (no_match) since
    # os.listdir order is arbitrary.
    doi = (item.get("DOI") or item.get("doi") or "").strip()
    if doi:
        doi_norm = re.sub(r"[^a-z0-9]", "", doi.lower())
        if len(doi_norm) >= 10:  # avoid accidental short-DOI collisions
            doi_matches = []
            for fname in os.listdir(ZOTERO_DIR):
                if not fname.lower().endswith(".pdf"):
                    continue
                # Strip the .pdf extension BEFORE normalising, otherwise the
                # trailing 'pdf' makes the bounded check below see 'p' as the
                # next char and reject every match.
                stem = fname[:-4].lower()
                fname_norm = re.sub(r"[^a-z0-9]", "", stem)
                idx = fname_norm.find(doi_norm)
                if idx < 0:
                    continue
                # Bounded: the char right after the DOI in the normalised stem
                # must NOT be alphanumeric (else it's a longer DOI). Since
                # non-alphanumerics were stripped, a trailing char here means
                # the real filename had extra DOI digits/letters → reject.
                nxt = idx + len(doi_norm)
                if nxt < len(fname_norm) and fname_norm[nxt].isalnum():
                    continue
                doi_matches.append(fname)
            if len(doi_matches) == 1:
                matched = os.path.join(ZOTERO_DIR, doi_matches[0])
                _audit_append({"key": key, "title": title[:80],
                               "method": "doi_filename", "path": matched,
                               "doi": doi})
                return matched, "doi_filename"
            elif len(doi_matches) > 1:
                _audit_append({"key": key, "title": title[:80],
                               "method": "doi_ambiguous", "doi": doi,
                               "candidates": doi_matches[:5]})

    # Priority 3: arXiv ID in filename
    # Bare `arxiv_id in fname` makes '2401.0001' match '2401.00012' (wrong,
    # newer paper). Require a delimited match: no digit/dot immediately before
    # and no digit immediately after the id (an arXiv id may have a vN suffix,
    # so allow a following 'v'/non-digit). Ambiguous (2+) → no_match.
    arxiv_id = _extract_arxiv_id_from_item(item)
    if arxiv_id:
        arxiv_re = re.compile(rf"(?<![0-9.]){re.escape(arxiv_id)}(?![0-9])")
        arxiv_matches = [fname for fname in os.listdir(ZOTERO_DIR)
                         if fname.lower().endswith(".pdf") and arxiv_re.search(fname)]
        if len(arxiv_matches) == 1:
            matched = os.path.join(ZOTERO_DIR, arxiv_matches[0])
            _audit_append({"key": key, "title": title[:80],
                           "method": "arxiv_filename", "path": matched,
                           "arxiv_id": arxiv_id})
            return matched, "arxiv_filename"
        elif len(arxiv_matches) > 1:
            _audit_append({"key": key, "title": title[:80],
                           "method": "arxiv_ambiguous", "arxiv_id": arxiv_id,
                           "candidates": arxiv_matches[:5]})

    # Priority 4 (optional): fuzzy title match — STRICTER than before.
    # The original 3-of-5 keyword rule caused the 139-paper mismatch bug.
    # We now require: (a) at least 5 significant keywords from the title,
    # (b) at least 5 of them appear in the filename (score >= 5), and
    # (c) coverage >= 80% of candidate keywords. Disabled entirely under
    # --strict-pdf.
    if _STRICT_PDF or not title:
        _audit_append({"key": key, "title": title[:80], "method": "no_match",
                       "reason": "strict_pdf" if _STRICT_PDF else "no_title"})
        return None, "no_match"

    title_words = re.sub(r"[^a-z0-9\s]", "", title.lower()).split()
    key_words = [w for w in title_words if len(w) > 3][:8]
    if len(key_words) < 5:
        _audit_append({"key": key, "title": title[:80], "method": "no_match",
                       "reason": "too_few_keywords", "keywords": key_words})
        return None, "no_match"

    best_match = None
    best_score = 0
    for fname in os.listdir(ZOTERO_DIR):
        if not fname.lower().endswith(".pdf"):
            continue
        fname_lower = fname.lower()
        score = sum(1 for w in key_words if w in fname_lower)
        if score > best_score:
            best_score = score
            best_match = fname

    coverage = best_score / max(1, len(key_words))
    if best_match and best_score >= 5 and coverage >= 0.8:
        matched = os.path.join(ZOTERO_DIR, best_match)
        _audit_append({"key": key, "title": title[:80], "method": "fuzzy",
                       "path": matched, "score": best_score,
                       "coverage": round(coverage, 2), "keywords": key_words,
                       "WARNING": "weak match — verify with audit_matching.py"})
        log(f"  WARN fuzzy PDF match for '{title[:60]}' "
            f"(score {best_score}/{len(key_words)}, cov {coverage:.0%})")
        return matched, "fuzzy"

    _audit_append({"key": key, "title": title[:80], "method": "no_match",
                   "reason": "fuzzy_below_threshold", "best_score": best_score,
                   "best_candidate": best_match, "keywords": key_words})
    return None, "no_match"


# ── Zotero ↔ text.md sanity check (zero-cost PDF integrity gate) ──

def _zotero_text_sanity(item, text_md_path, min_title_coverage=0.6):
    """Verify Zotero metadata (title/DOI/first author) appears in the extracted
    text. Catches the "Zotero attachment is wrong PDF" failure mode that even
    `--strict-pdf` cannot detect: find_pdf returned Zotero's linked file, but
    that file is the wrong paper.

    All signals are local regex/substring — no LLM call.

    Returns (passed: bool, reason: str).
    """
    if not os.path.exists(text_md_path):
        return True, "no_text_skip"  # text extraction failed; downstream already fails
    try:
        with open(text_md_path, "r", encoding="utf-8", errors="replace") as f:
            text = f.read(6000).lower()
    except Exception:
        return True, "read_error_skip"

    # 1. Title keyword coverage
    # Include Hangul syllables so Korean titles like
    # "BiCoord: 장기간 시공간 협응 양팔 조작 벤치마크" yield several keywords
    # rather than just one English fragment. ASCII tokens still need >3
    # chars to skip stopwords; Hangul tokens use a ≥2-char threshold
    # since Korean morphemes are short.
    title_lower = (item.get("title") or "").lower()
    title_words = re.sub(r"[^a-z0-9가-힣\s]", " ", title_lower).split()
    kw = [w for w in title_words
          if (w.isascii() and len(w) > 3) or (not w.isascii() and len(w) >= 2)
          ][:6]
    title_hits = sum(1 for w in kw if w in text) if kw else 0
    # Scale threshold to kw length: 60% coverage with a floor of 1. The
    # original ``max(3, ...)`` rejected legitimate matches when titles
    # produced fewer than 5 keywords (typical for Korean papers and
    # short titles).
    threshold = max(1, int(len(kw) * min_title_coverage))
    title_ok = (not kw) or title_hits >= threshold

    # ASCII-only fallback: covers the "Korean title + English PDF" case
    # where the user registered a translated title in Zotero but the
    # actual PDF body is the English original. The Hangul keywords will
    # never appear in the English text, so we additionally pass if the
    # ASCII subset of the keywords has full coverage (≥60% with floor 1).
    if not title_ok and kw:
        ascii_kw = [w for w in kw if w.isascii()]
        if ascii_kw:
            ascii_hits = sum(1 for w in ascii_kw if w in text)
            ascii_thr = max(1, int(len(ascii_kw) * min_title_coverage))
            if ascii_hits >= ascii_thr:
                title_ok = True

    # 2. DOI exact (ignore non-alphanumeric)
    doi = re.sub(r"[^a-z0-9]", "", (item.get("DOI") or "").lower())
    text_norm = re.sub(r"[^a-z0-9]", "", text)
    doi_ok = True if len(doi) < 10 else (doi in text_norm)

    # 3. First author lastName
    creators = item.get("creators", []) or []
    last = ""
    for c in creators:
        last = (c.get("lastName") or "").lower()
        if last:
            break
    author_ok = True if len(last) < 3 else (last in text)

    # title + doi 둘 다 통과면 author 무관 (corporate author, 이미지 헤더 등
    # 저자명 추출 실패가 흔해서 단독 blocker로 쓰지 않음).
    if title_ok and doi_ok:
        return True, f"ok (title {title_hits}/{len(kw)} doi=T author={author_ok})"
    if title_ok and author_ok:
        return True, f"ok (title {title_hits}/{len(kw)} author=T doi={doi_ok})"
    return False, (f"title_hits={title_hits}/{len(kw)} "
                   f"doi_ok={doi_ok} author_ok={author_ok}")


# ── Phase 2: Extract text.md (OpenDataLoader → PyMuPDF fallback) ──

def extract_text(pdf_path, slug_dir):
    text_path = os.path.join(slug_dir, "text.md")

    # Strategy 1: OpenDataLoader (better table/formula/structure extraction)
    # NOTE: pip package is `opendataloader-pdf` but Python import name is
    # `opendataloader_pdf` (underscore). Earlier code used `opendataloader.pdf`
    # which silently ImportError'd and fell through to PyMuPDF every time.
    # Requires Java Runtime (e.g. `brew install --cask temurin`).
    try:
        import tempfile, re
        from opendataloader_pdf import convert as odl_convert
        with tempfile.TemporaryDirectory() as tmpdir:
            odl_convert(input_path=[pdf_path], output_dir=tmpdir,
                        format="markdown", quiet=True)
            md_files = [f for f in os.listdir(tmpdir) if f.endswith(".md")]
            if md_files:
                with open(os.path.join(tmpdir, md_files[0]), "r", encoding="utf-8") as f:
                    text = f.read()
                if text and len(text) > 100:
                    # OpenDataLoader exports its own image dump and embeds
                    # `![image N](relative/path.png)` lines pointing to a
                    # sibling dir that paper-curation never tracks (we use
                    # PyMuPDF for figures/). Collapse those refs into
                    # `[Figure N]` so the body flow survives but the broken
                    # paths don't pollute Claude review prompts.
                    text = re.sub(r'!\[image\s*(\d+)\]\([^)]*\)',
                                  r'[Figure \1]', text)
                    text = re.sub(r'\n{3,}', '\n\n', text)
                    with open(text_path, "w", encoding="utf-8") as f:
                        f.write(text)
                    return True
    except ImportError:
        pass  # OpenDataLoader not installed → fallback
    except Exception as e:
        log(f"  OpenDataLoader failed: {e}, falling back to PyMuPDF")

    # Strategy 2: PyMuPDF fallback
    try:
        import fitz
        doc = fitz.open(pdf_path)
        text = "\n".join(doc[p].get_text() for p in range(len(doc)))
        doc.close()
        if text and len(text) > 100:
            with open(text_path, "w", encoding="utf-8") as f:
                f.write(text)
            return True
    except Exception as e:
        log(f"  text.md failed: {e}")
    return False


# ── Phase 3: Extract figures + Gemini validation ──

# Figure crop is LOCALIZED FROM THE PDF'S OWN GEOMETRY before any LLM call.
# The previous design seeded every crop as the full page and relied on Gemini
# point-offsets to shrink it; a Gemini failure or an "ok" on round 0 left the
# ENTIRE PAGE as the figure. We now build the crop box from the union of the
# graphic rects (raster image blocks + get_image_rects + area-filtered
# get_drawings) that are adjacent to the caption, render THAT box first, and
# only then optionally let Gemini nudge it within bounds. Gemini can never
# enlarge the box back to a full page, and a Gemini error keeps the geometric
# box instead of falsely accepting "ok".


def _union_rects(rects):
    """Union a list of (x0,y0,x1,y1) tuples into one bounding box, or None."""
    if not rects:
        return None
    x0 = min(r[0] for r in rects)
    y0 = min(r[1] for r in rects)
    x1 = max(r[2] for r in rects)
    y1 = max(r[3] for r in rects)
    return [x0, y0, x1, y1]


def _collect_graphic_rects(page, pw, ph):
    """Gather candidate graphic rects on a page from three sources:
      1. raster image blocks (text_dict type==1)
      2. page.get_image_rects() for every embedded image xref
      3. page.get_drawings() vector paths (area-filtered, capped per page)
    Returns list of (x0,y0,x1,y1). Tiny rects (axis-tick fragments, hairlines)
    are dropped so a vector-heavy page doesn't explode the union.
    """
    MIN_W, MIN_H = 40, 40  # ignore sub-glyph fragments
    rects = []

    # Source 1: raster image blocks
    try:
        td = page.get_text("dict")
        for b in td["blocks"]:
            if b.get("type") == 1:
                bb = b["bbox"]
                if (bb[2] - bb[0]) > MIN_W and (bb[3] - bb[1]) > MIN_H:
                    rects.append((bb[0], bb[1], bb[2], bb[3]))
    except Exception:
        pass

    # Source 2: get_image_rects() — embedded raster placement (handles repeats)
    try:
        for img in page.get_images(full=True):
            xref = img[0]
            try:
                for r in page.get_image_rects(xref):
                    if (r.x1 - r.x0) > MIN_W and (r.y1 - r.y0) > MIN_H:
                        rects.append((r.x0, r.y0, r.x1, r.y1))
            except Exception:
                continue
    except Exception:
        pass

    # Source 3: get_drawings() — vector plots/schematics have no raster block.
    # This can return thousands of tiny paths; filter by area and cap work.
    try:
        drawings = page.get_drawings()
        page_area = max(1.0, pw * ph)
        count = 0
        for d in drawings:
            count += 1
            if count > 4000:  # hard cap so vector-dense pages stay fast
                break
            r = d.get("rect")
            if r is None:
                continue
            w = r.x1 - r.x0
            h = r.y1 - r.y0
            if w <= MIN_W or h <= MIN_H:
                continue
            # Drop near-page-spanning full-bleed background rects (a single
            # path covering >95% of the page is a page border, not a figure).
            if (w * h) / page_area > 0.95:
                continue
            rects.append((r.x0, r.y0, r.x1, r.y1))
    except Exception:
        pass

    return rects


def extract_figures(pdf_path, slug_dir):
    fig_dir = os.path.join(slug_dir, "figures")
    os.makedirs(fig_dir, exist_ok=True)

    try:
        import fitz
    except ImportError:
        log("  PyMuPDF not available")
        return []

    doc = fitz.open(pdf_path)
    MARGIN = 30
    MAX_ROUNDS = 2  # geometric box is the prior; Gemini only refines

    # Phase 4 B2: cheap pre-validator runs first. When the heuristic is
    # confident the figure is invalid (tiny/blank/near-uniform), we skip
    # the Gemini round trip entirely. Empirically saves ~30% of calls.
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from api.extract import pre_validate_figure

    # 키 해석: env(GOOGLE_API_KEY/GEMINI_API_KEY) → config.json. 단 reextract_figures
    # 가 geometric-only 강제 시 세팅하는 PAPER_CURATION_NO_GEMINI 가 있으면 키 유무와
    # 무관하게 Gemini 검증을 끈다 (env pop 만으론 config.json 키가 남아 스위치가 안 먹음).
    have_gemini = (not os.environ.get("PAPER_CURATION_NO_GEMINI")
                   and bool(get_google_key().strip()))
    # Log a degraded-Gemini warning at most once per run instead of silently
    # accepting full pages when the validator throws.
    _gemini_warned = {"done": False}

    def validate(img_path, caption):
        """Return a verdict dict. status ∈ {ok, clipped, oversized, both, error}.

        'error' (validator unavailable) is DISTINCT from 'ok' (figure looks
        good): the caller keeps the geometric box on 'error' rather than
        treating it as accepted.
        """
        pre = pre_validate_figure(img_path)
        if pre is not None:
            return pre
        if not have_gemini:
            # No key → skip the round-trip entirely, rely on geometry.
            return {"status": "error", "adjust_pt": {}}
        try:
            from google import genai
            from google.genai import types
            client = genai.Client(api_key=get_google_key())
            with open(img_path, "rb") as f:
                img_bytes = f.read()
            prompt = (f"Evaluate cropping of this academic figure.\nCaption: {caption}\n"
                      f"Check: (1) content CLIPPED at edges? (2) EXCESS body text?\n"
                      f"JSON only: {{\"status\":\"ok\"|\"clipped\"|\"oversized\"|\"both\","
                      f"\"issues\":\"brief\",\"adjust_pt\":{{\"top\":0,\"bottom\":0,\"left\":0,\"right\":0}}}}\n"
                      f"adjust_pt: positive=expand, negative=shrink. PDF points.")
            resp = client.models.generate_content(
                model="gemini-3.1-pro-preview",
                contents=[types.Part.from_bytes(data=img_bytes, mime_type="image/png"), prompt])
            text = resp.text.strip()
            if "```" in text:
                text = text.split("```")[1]
                if text.startswith("json"):
                    text = text[4:]
            return json.loads(text)
        except Exception as e:
            if not _gemini_warned["done"]:
                log(f"  WARN Gemini figure validator unavailable "
                    f"({type(e).__name__}); using geometric crops only")
                _gemini_warned["done"] = True
            return {"status": "error", "adjust_pt": {}}

    # Collect caption candidates across all pages first, so we can dedup a
    # fig_num globally by ADJACENT-GRAPHIC AREA (prefer the real caption over a
    # body-text mention on another page) and cap EMITTED figures by area.
    candidates = []  # each: dict(fig_num, page, caption, box, hull, graphic_area)
    orphan_caps = []  # 캡션은 있는데 소유 그래픽이 없는 경우 — 페이지 영역 폴백 후보

    for pn in range(min(30, len(doc))):
        page = doc[pn]
        pw, ph = page.rect.width, page.rect.height
        # Page rotation: get_text bboxes and get_pixmap clip both operate in
        # the rotated coordinate space PyMuPDF reports via page.rect, so no
        # manual rotation maths is needed — page.rect already reflects it.
        text_dict = page.get_text("dict")
        txt_blocks = [b for b in text_dict["blocks"] if b["type"] == 0]

        graphic_rects = _collect_graphic_rects(page, pw, ph)

        # Scanned-PDF guard: a single image covering >90% of the page IS the
        # figure — keep the whole page in that legitimate case.
        full_page_image = None
        for r in graphic_rects:
            if ((r[2] - r[0]) * (r[3] - r[1])) / max(1.0, pw * ph) > 0.90:
                full_page_image = r
                break

        # Pass 1: collect EVERY caption line on the page first, so each
        # graphic rect can be assigned to the caption it actually belongs to.
        # A caption is the first line of a text block that STARTS with
        # "Figure/Fig/FIG N". Scan all lines of the block (Nature/Science merge
        # a trailing fragment above the caption into one block, so it may be
        # line #1+). Case-insensitive for physics/PRL "FIG. 1.".
        caps = []  # each: dict(fig_num, caption, x0, top, x1, bottom)
        for tb in txt_blocks:
            for ln in tb["lines"]:
                lt = "".join(s["text"] for s in ln["spans"]).strip()
                m = re.match(r"(?:Figure|Fig\.?)\s*([0-9]+)", lt, re.I)
                if m:
                    lb = ln["bbox"]
                    caps.append({
                        "fig_num": int(m.group(1)), "caption": lt[:120],
                        "x0": lb[0], "top": lb[1], "x1": lb[2],
                        "bottom": max(lb[3], tb["bbox"][3]),
                        # 캡션다움: 번호 뒤 구두점("Figure 1." / "Fig. 1:" 등).
                        # 본문 언급("Fig. 1 shows …")과 구분하는 신호 — dedup에서
                        # 진짜 캡션이 본문 언급에게 밀리지 않게 한다.
                        "caplike": bool(re.match(
                            r"(?:Figure|Fig\.?)\s*[0-9]+\s*[.:|)\]—–-]", lt, re.I)),
                    })
                    break
        if not caps:
            continue

        # Figures sit ABOVE their caption (dominant convention), so a tall
        # figure's TOP panels can be far above the caption — allow a generous
        # gap there. The figure-BELOW-caption case is rare; keep its gap tight
        # so the block of body text under a caption isn't vacuumed into the crop.
        gap_above = ph * 0.6
        gap_below = ph * 0.12

        # Pass 2: assign each graphic rect to its OWNING caption. The figure
        # width is derived from the rects themselves, NEVER from the caption's
        # column — a single-column caption legitimately owns a full-width
        # figure's far panels (common in Nature/Science). Ranking, best first:
        #   (1) caption BELOW the rect (figure-above-caption, the dominant
        #       convention) beats a caption above it;
        #   (2) a caption that horizontally OVERLAPS the rect beats one that
        #       does not — this keeps SIDE-BY-SIDE figures separate;
        #   (3) nearest vertical gap.
        assigned = {id(c): [] for c in caps}
        if full_page_image is not None:
            assigned[id(caps[0])].append(full_page_image)
        else:
            for r in graphic_rects:
                rx0, ry0, rx1, ry1 = r
                best_key = None
                best_cap = None
                for c in caps:
                    if c["top"] >= ry1 - 2 and (c["top"] - ry1) <= gap_above:
                        direction, vgap = 0, c["top"] - ry1   # figure above caption
                    elif c["bottom"] <= ry0 + 2 and (ry0 - c["bottom"]) <= gap_below:
                        direction, vgap = 1, ry0 - c["bottom"]  # figure below caption
                    else:
                        continue
                    overlap = not (rx1 <= c["x0"] or rx0 >= c["x1"])
                    key = (direction, 0 if overlap else 1, vgap)
                    if best_key is None or key < best_key:
                        best_key, best_cap = key, c
                if best_cap is not None:
                    assigned[id(best_cap)].append(r)

        for c in caps:
            adj_rects = assigned[id(c)]
            if not adj_rects:
                # No graphic content owned by this caption → body-text mention
                # or un-extractable figure. 과거엔 DROP했지만, 등록 시 '모든
                # 그림' 보장을 위해 페이지 영역 폴백 후보로 보관한다 (최종
                # 렌더는 함수 끝의 완성 단계).
                above = [cc["bottom"] for cc in caps if cc["bottom"] < c["top"] - 4]
                below = [cc["top"] for cc in caps if cc["top"] > c["bottom"] + 4]
                orphan_caps.append({
                    "fig_num": c["fig_num"], "page": pn, "caption": c["caption"],
                    "top": c["top"], "bottom": c["bottom"],
                    "caplike": c["caplike"],
                    "floor": (max(above) + 4) if above else 0.0,
                    "ceil": (min(below) - 4) if below else ph,
                    "pw": pw, "ph": ph,
                })
                continue
            hull = _union_rects(adj_rects)
            graphic_area = sum((r[2] - r[0]) * (r[3] - r[1]) for r in adj_rects)
            # Crop box = union of owned rects + MARGIN. No caption-column clip.
            bx0 = max(0, hull[0] - MARGIN)
            by0 = max(0, hull[1] - MARGIN)
            bx1 = min(pw, hull[2] + MARGIN)
            by1 = min(ph, hull[3] + MARGIN)
            # Extend the crop toward the caption so TEXT-rendered figure content
            # (panel labels, chemical-formula lists, axis labels) between the
            # last graphic rect and the caption is not clipped. The caption is
            # the figure's hard boundary, so this can never reach body text.
            n_above = sum(1 for r in adj_rects if r[3] <= c["top"] + 2)
            if n_above * 2 >= len(adj_rects):     # figure above its caption
                by1 = min(ph, max(by1, c["top"] - 2))
            else:                                 # figure below its caption (rare)
                by0 = max(0, min(by0, c["bottom"] + 2))
            candidates.append({
                "fig_num": c["fig_num"], "page": pn, "caption": c["caption"],
                "caplike": c["caplike"],
                "box": [bx0, by0, bx1, by1],
                "hull": hull, "graphic_area": graphic_area,
                "pw": pw, "ph": ph,
            })

    # Page-scoped dedup: when the same fig_num appears on multiple pages,
    # prefer the candidate with the LARGEST adjacent graphic area (the real
    # caption, not a bare mention). Then cap EMITTED figures to top-5 by area.
    best_by_num = {}
    for c in candidates:
        prev = best_by_num.get(c["fig_num"])
        if prev is None or (
            (c.get("caplike", False), c["graphic_area"])
            > (prev.get("caplike", False), prev["graphic_area"])
        ):
            best_by_num[c["fig_num"]] = c
    # Cap emitted figures to the LOWEST 5 figure numbers. Main-body figures
    # (1-5) come before appendix figures, and in some papers (e.g. NLP papers
    # with many "Prompt for ..." boxes in the appendix) the appendix figures
    # have far larger area and would crowd out the real figures under an
    # area-based cap. Figure number is the more reliable importance signal.
    all_nums = sorted(best_by_num.values(), key=lambda c: c["fig_num"])
    # review 임베드 후보는 기존과 동일하게 top-5. 6번 이후는 아래 완성 단계에서
    # geometric-only로 저장만 한다 (등록 시 '모든 그림' 보관 — 채팅 인라인 그림용).
    chosen = all_nums[:5]
    extras = all_nums[5:20]

    figures = []
    for c in chosen:
        fig_num = c["fig_num"]
        pn = c["page"]
        caption = c["caption"]
        page = doc[pn]
        pw, ph = c["pw"], c["ph"]
        hull = c["hull"]
        x0, y0, x1, y1 = c["box"]
        out = os.path.join(fig_dir, f"fig{fig_num}.png")

        # Clamp bounds = the geometric box itself (owned-rect hull + MARGIN,
        # already extended toward the caption to capture text-rendered figure
        # content). Gemini may nudge WITHIN this box but never expand past it —
        # the geometric crop is the prior; the LLM only refines inside it, so it
        # can neither escape to a full page nor re-clip the caption extension.
        hx0, hy0, hx1, hy1 = c["box"]

        rendered_ok = False
        for rnd in range(MAX_ROUNDS + 1):
            # Inverted-box guard: revert to the geometric box.
            if x1 <= x0 or y1 <= y0:
                x0, y0, x1, y1 = c["box"]

            rendered = False
            for scale in [3, 2, 1]:
                try:
                    pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale),
                                          clip=fitz.Rect(x0, y0, x1, y1))
                    pix.save(out)
                    rendered = True
                    break
                except Exception:
                    continue
            if not rendered:
                break  # skip this figure entirely
            rendered_ok = True

            if rnd == MAX_ROUNDS:
                break

            result = validate(out, caption)
            status = result.get("status")
            if status == "ok":
                break
            if status == "error":
                # Validator unavailable → keep the geometric box, do not
                # expand, break. Never treat as 'ok'.
                break

            # 'clipped' / 'oversized' / 'both': nudge within the hull ± MARGIN.
            damping = [0.8, 0.6][min(rnd, 1)]
            adj = result.get("adjust_pt", {})
            ny0 = y0 - adj.get("top", 0) * damping
            ny1 = y1 + adj.get("bottom", 0) * damping
            nx0 = x0 - adj.get("left", 0) * damping
            nx1 = x1 + adj.get("right", 0) * damping
            # Clamp to the rect hull (± MARGIN) — the box can never escape the
            # detected graphic region back to a full page.
            x0 = min(max(nx0, hx0), hx1)
            y0 = min(max(ny0, hy0), hy1)
            x1 = min(max(nx1, hx0), hx1)
            y1 = min(max(ny1, hy0), hy1)

        if not rendered_ok:
            continue

        # Plausibility floor: if the final box is implausibly small vs the
        # union of detected rects, expand to the hull + MARGIN (a tight figure
        # box — NEVER the whole page). No full-page re-render fallback.
        hull_area = (hull[2] - hull[0]) * (hull[3] - hull[1])
        box_area = (x1 - x0) * (y1 - y0)
        if hull_area > 0 and box_area < hull_area * 0.5:
            x0, y0, x1, y1 = hx0, hy0, hx1, hy1
            for scale in [3, 2, 1]:
                try:
                    pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale),
                                          clip=fitz.Rect(x0, y0, x1, y1))
                    pix.save(out)
                    break
                except Exception:
                    continue

        figures.append({"name": str(fig_num), "page": pn, "caption": caption})

    # ── 등록 시 '모든 그림' 보장 (채팅 인라인 그림 완전성) ──────────────
    # (a) 6번 이후 그림: geometric-only 저장 (Gemini 라운드 없음 — 비용 억제).
    #     review 반환(figures)에는 넣지 않아 기존 임베드 동작 불변.
    for c in extras:
        out = os.path.join(fig_dir, f"fig{c['fig_num']}.png")
        page = doc[c["page"]]
        x0, y0, x1, y1 = c["box"]
        for scale in [3, 2, 1]:
            try:
                pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale),
                                      clip=fitz.Rect(x0, y0, x1, y1))
                pix.save(out)
                break
            except Exception:
                continue

    # (b) 캡션은 있는데 산출물이 없는/깨진 그림: 캡션 기준 페이지 영역 크롭
    #     폴백. figure-above-caption 관례(위 영역) 우선, 얕으면 아래 영역.
    #     본문 일부가 섞일 수 있는 최후 폴백이지만 '그림이 아예 안 나오는'
    #     상태를 없앤다 (예: 과거 9159 fig1 = 0-byte).
    def _fig_ok(p):
        return os.path.exists(p) and os.path.getsize(p) > 1024

    have = set()
    for c in all_nums:
        if _fig_ok(os.path.join(fig_dir, f"fig{c['fig_num']}.png")):
            have.add(c["fig_num"])
    # 렌더 실패/0-byte로 끝난 검출 후보도 폴백 대상으로 승격
    for c in all_nums:
        if c["fig_num"] in have:
            continue
        orphan_caps.append({
            "fig_num": c["fig_num"], "page": c["page"], "caption": c["caption"],
            "caplike": c.get("caplike", False),
            "top": min(c["ph"], c["box"][3] + 2),
            "bottom": min(c["ph"], c["box"][3] + 14),
            "floor": 0.0, "ceil": c["ph"], "pw": c["pw"], "ph": c["ph"],
        })
    done_orphans = set()
    for o in sorted(orphan_caps, key=lambda o: (o["fig_num"], not o.get("caplike", False), o["page"], o["top"])):
        num = o["fig_num"]
        if num in have or num in done_orphans or num > 20:
            continue
        page = doc[o["page"]]
        opw, oph = o["pw"], o["ph"]
        y0a = max(0.0, o["top"] - 0.55 * oph, o["floor"])
        y1a = max(0.0, o["top"] - 2)
        y0b = min(oph, o["bottom"] + 2)
        y1b = min(oph, o["bottom"] + 0.55 * oph, o["ceil"])
        if y1a - y0a >= 60:
            ry0, ry1 = y0a, y1a
        elif y1b - y0b >= 60:
            ry0, ry1 = y0b, y1b
        else:
            continue
        out = os.path.join(fig_dir, f"fig{num}.png")
        try:
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2),
                                  clip=fitz.Rect(12, ry0, opw - 12, ry1))
            pix.save(out)
        except Exception:
            continue
        if _fig_ok(out):
            done_orphans.add(num)
            log(f"  fig{num}: geometric 검출 실패 → 캡션 기준 페이지 영역 폴백")
        else:
            try:
                os.remove(out)
            except OSError:
                pass

    doc.close()
    return figures


# ── Phase 4: Write review.md (Claude Haiku → JSON → Template) ──

REVIEW_TEMPLATE = """# {title}

> **저자**: {authors} | **날짜**: {date} | {ref_label}: {ref_link}

---

## Essence

{fig_essence}
{essence}

## Motivation

- **Known**: {known}
- **Gap**: {gap}
- **Why**: {why}
- **Approach**: {approach}

## Achievement

{fig_achievement}
{achievement}

## How

{fig_how}
{how}

## Originality

{originality}

## Limitation & Further Study

{limitation}

## Evaluation

- Novelty: {novelty}/5
- Technical Soundness: {tech}/5
- Significance: {significance}/5
- Clarity: {clarity}/5
- Overall: {overall}/5

**총평**: {verdict}
"""


REVIEW_TOOL_SCHEMA = {
    "name": "emit_review",
    "description": (
        "Emit the structured Korean review for the given paper. All "
        "narrative fields must be in Korean except for jargon "
        "(technical terms, model names, datasets, algorithms, formulas, "
        "framework/product names) which must stay in the original form."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "essence":         {"type": "string", "minLength": 20,
                                "description": "핵심 요약 1-2문장."},
            "fig_essence":     {"type": "integer", "minimum": 0, "maximum": 20,
                                "description": "Essence에 가장 관련된 Figure 번호. 없으면 0."},
            "known":           {"type": "string", "minLength": 10,
                                "description": "알려진 것 1-2문장."},
            "gap":             {"type": "string", "minLength": 10,
                                "description": "연구 갭 1-2문장."},
            "why":             {"type": "string", "minLength": 10,
                                "description": "왜 중요한지 1-2문장."},
            "approach":        {"type": "string", "minLength": 10,
                                "description": "접근법 1-2문장."},
            "achievement":     {"type": "string", "minLength": 20,
                                "description": "성과 (마크다운 번호 목록, 각 항목 **굵은 제목**: 설명)."},
            "fig_achievement": {"type": "integer", "minimum": 0, "maximum": 20},
            "how":             {"type": "string", "minLength": 10,
                                "description": "방법론 (마크다운 bullet 목록)."},
            "fig_how":         {"type": "integer", "minimum": 0, "maximum": 20},
            "originality":     {"type": "string", "minLength": 10,
                                "description": "독창성 (마크다운 bullet 목록)."},
            "limitation":      {"type": "string", "minLength": 10,
                                "description": "한계 + 후속연구 (마크다운 bullet 목록)."},
            "novelty":         {"type": "integer", "minimum": 1, "maximum": 5},
            "technical":       {"type": "integer", "minimum": 1, "maximum": 5,
                                "description": "Technical soundness."},
            "significance":    {"type": "integer", "minimum": 1, "maximum": 5},
            "clarity":         {"type": "integer", "minimum": 1, "maximum": 5},
            "overall":         {"type": "integer", "minimum": 1, "maximum": 5},
            "verdict":         {"type": "string", "minLength": 10,
                                "description": "총평 1-2문장."},
        },
        "required": ["essence", "fig_essence", "known", "gap", "why", "approach",
                     "achievement", "fig_achievement", "how", "fig_how",
                     "originality", "limitation",
                     "novelty", "technical", "significance", "clarity", "overall",
                     "verdict"],
    },
}

WRITE_REVIEW_SCHEMA_VERSION = "v1"
# 기존 review.md 는 재생성하지 않으므로 모델 변경은 신규 리뷰부터 적용된다
# (캐시 키에 model 포함 — 변경 시 기존 캐시는 자연 무효).
WRITE_REVIEW_MODEL = os.environ.get("WRITE_REVIEW_MODEL", "claude-sonnet-5")


_REVIEW_STR_TAGS = ("essence", "known", "gap", "why", "approach", "achievement",
                    "how", "originality", "limitation", "verdict")
_REVIEW_INT_TAGS = ("fig_essence", "fig_achievement", "fig_how",
                    "novelty", "technical", "significance", "clarity", "overall")


def _salvage_review_data(data):
    """Recover a structured review when the model invoked `emit_review` but
    dumped the XML-tagged review into one field instead of filling the schema.

    Three observed claude-sonnet-5 failure modes:
      A) everything crammed into `essence` (with a trailing `</invoke>`);
      B) `essence` is clean but the rest is stuffed into `known`/`how`/
         `originality` using antml `<parameter name="x">…</parameter>` syntax;
      C) clean fields plus a `<parameter name="x">…</parameter>` blob (for
         known/gap/why/approach) appended inside `essence`.
    All render as empty sections + default 3/3/3/3/3 scores. Normalize the
    tool-parameter syntax and re-parse every field. No-op for clean responses.
    """
    d = dict(data or {})
    other = [t for t in _REVIEW_STR_TAGS if t != "essence"]

    def _norm(s):
        s = re.sub(r'<parameter name="([^"]+)">(.*?)</parameter>', r'<\1>\2</\1>',
                   s or "", flags=re.S)
        s = re.sub(r'<parameter name="([^"]+)">', r'<\1>', s)
        s = re.sub(r'</parameter[^>]*>', '', s)
        return s.replace("</invoke>", "")

    normed = {k: _norm(v) for k, v in d.items() if isinstance(v, str)}
    combined = "\n".join(normed.values())
    tagged = "</essence>" in combined or any(
        ("<%s>" % t) in combined or ("</%s>" % t) in combined for t in other)
    if not tagged:
        return data  # well-formed

    strip_tags = re.compile(
        r"</?(?:%s|fig_\w+|novelty|technical|significance|clarity|overall)>"
        % "|".join(_REVIEW_STR_TAGS))
    fixed = dict(d)

    er = normed.get("essence", "")
    if "<essence>" in er:
        m = re.search(r"<essence>(.*?)</essence>", er, re.S)
        essence = m.group(1) if m else er
    elif "</essence>" in er:
        essence = er.split("</essence>", 1)[0]
    else:
        essence = re.split(r"<(?:%s|fig_\w+)>" % "|".join(other), er, 1)[0]
    essence = strip_tags.sub("", essence).strip()
    if essence:
        fixed["essence"] = essence

    for t in other:
        m = re.search(r"<%s>(.*?)</%s>" % (t, t), combined, re.S)
        if m and m.group(1).strip():
            val = m.group(1)
        else:
            # carrier field: keep only the leading text before the first
            # leaked tag (handles `known` holding a `<parameter …>` blob, a
            # bare `</known>`, or a spilled `<gap>…` sequence).
            cur = normed.get(t, "")
            val = re.split(
                r"<(?:/?)(?:parameter|%s|fig_\w+|novelty|technical|"
                r"significance|clarity|overall)\b" % "|".join(_REVIEW_STR_TAGS),
                cur, 1, flags=re.S)[0]
        val = strip_tags.sub("", val).strip()
        if val:
            fixed[t] = val
    for t in _REVIEW_INT_TAGS:
        m = re.search(r"<%s>\s*(\d+)" % t, combined)
        if m:
            fixed[t] = int(m.group(1))
    return fixed


def write_review(item, slug_dir, figures):
    text_path = os.path.join(slug_dir, "text.md")
    if not os.path.exists(text_path):
        return False

    with open(text_path, "r", encoding="utf-8") as f:
        paper_text = f.read()[:15000]

    title = item.get("title", "")
    authors = ", ".join(
        f"{c.get('firstName', '')} {c.get('lastName', '')}".strip()
        for c in item.get("creators", [])
    )
    date = item.get("date", "")
    doi = item.get("DOI", "")
    abstract = item.get("abstractNote", "")

    fig_refs = ""
    for fig in figures:
        fig_refs += f"\n- Fig {fig['name']}: {fig['caption'][:80]}"

    try:
        from anthropic import Anthropic
        client = Anthropic(timeout=180.0, max_retries=4)

        # Tool-use forces a structured JSON response that matches
        # REVIEW_TOOL_SCHEMA. The SDK auto-retries on schema validation
        # failures so we no longer need post-hoc list-literal / figure
        # path / evaluation fixers.
        prompt = (
            "논문을 분석하고 `emit_review` 도구를 호출해 리뷰 필드를 채워라.\n\n"
            "모든 narrative 필드는 한국어 서술. 단 Jargon — 기술 용어·모델명·데이터셋·"
            "알고리즘·수식·프레임워크·제품명 등 — 은 원문 그대로 유지하고 번역하지 "
            "말 것. 예: \"diffusion model을 사용한다\" (O), "
            "\"확산 모델(diffusion model)을 사용한다\" (X).\n\n"
            f"제목: {title}\n"
            f"Abstract: {abstract}\n"
            f"본문 (발췌): {paper_text[:12000]}\n"
            f"Figure 목록:{fig_refs}\n"
        )

        # cached_call: same (slug + prompt + model + schema_version) → cache
        # hit, no Anthropic call. Re-runs of --mode rebuild on unchanged
        # papers cost zero LLM calls.
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        from api._llm import cached_call, paper_cache_dir
        slug = os.path.basename(slug_dir.rstrip("/\\"))
        cache_dir = paper_cache_dir(slug)

        def _make_call():
            response = client.messages.create(
                model=WRITE_REVIEW_MODEL,
                max_tokens=4000,
                tools=[REVIEW_TOOL_SCHEMA],
                tool_choice={"type": "tool", "name": "emit_review"},
                messages=[{"role": "user", "content": prompt}],
            )
            for block in response.content:
                # SDK returns ToolUseBlock; check by attribute presence.
                if getattr(block, "type", None) == "tool_use" \
                        and getattr(block, "name", None) == "emit_review":
                    return dict(block.input)
            raise RuntimeError("emit_review tool was not invoked")

        data = cached_call(
            cache_dir, prompt, WRITE_REVIEW_MODEL, _make_call,
            schema_version=WRITE_REVIEW_SCHEMA_VERSION,
        )
        data = _salvage_review_data(data)

        # Build figure insertions
        def fig_block(fig_num_str):
            try:
                n = int(fig_num_str)
            except (ValueError, TypeError):
                return ""
            if n == 0:
                return ""
            fig = next((f for f in figures if int(f["name"]) == n), None)
            if not fig:
                return ""
            cap = fig.get("caption", f"Figure {n}")
            return f"![Figure {n}](figures/fig{n}.png)\n\n*{cap}*\n"

        # DOI vs URL
        url = item.get("url", "")
        if doi:
            ref_label = "**DOI**"
            ref_link = f"[{doi}](https://doi.org/{doi})"
        elif url:
            ref_label = "**URL**"
            ref_link = f"[{url}]({url})"
        else:
            ref_label = "**DOI**"
            ref_link = "N/A"

        review_text = REVIEW_TEMPLATE.format(
            title=title, authors=authors, date=date,
            ref_label=ref_label, ref_link=ref_link,
            essence=data.get("essence", ""),
            fig_essence=fig_block(data.get("fig_essence", 0)),
            known=data.get("known", ""),
            gap=data.get("gap", ""),
            why=data.get("why", ""),
            approach=data.get("approach", ""),
            achievement=data.get("achievement", ""),
            fig_achievement=fig_block(data.get("fig_achievement", 0)),
            how=data.get("how", ""),
            fig_how=fig_block(data.get("fig_how", 0)),
            originality=data.get("originality", ""),
            limitation=data.get("limitation", ""),
            novelty=data.get("novelty", 3),
            # Tool-use schema field is `technical`; legacy SDK responses
            # used `tech` so we accept both during the migration window.
            tech=data.get("technical", data.get("tech", 3)),
            significance=data.get("significance", 3),
            clarity=data.get("clarity", 3),
            overall=data.get("overall", 3),
            verdict=data.get("verdict", ""),
        )

        review_path = os.path.join(slug_dir, "review.md")
        with open(review_path, "w", encoding="utf-8") as f:
            f.write(review_text.strip() + "\n")
        return True

    except Exception as e:
        log(f"  review.md failed: {e}")
        return False


def fix_python_list_literals(slug_dir):
    """Post-process: convert Python list literals ['a','b'] to markdown bullets."""
    review_path = os.path.join(slug_dir, "review.md")
    if not os.path.exists(review_path):
        return
    with open(review_path, "r", encoding="utf-8") as f:
        content = f.read()
    if "['" not in content and '["' not in content:
        return
    lines = content.split("\n")
    new_lines = []
    for line in lines:
        s = line.strip()
        if (s.startswith("[") and s.endswith("]") and
                ("'" in s or '"' in s) and len(s) > 20):
            # Parse by splitting on quote-comma-quote patterns
            inner = s[1:-1]  # remove [ ]
            # Split on ', ' or ", " patterns between items
            items = re.split(r"'\s*,\s*'|'\s*,\s*\"|\"'\s*,\s*'|\"'\s*,\s*\"", inner)
            if len(items) > 1:
                for item in items:
                    clean = item.strip().strip("'\"")
                    if clean:
                        new_lines.append(f"- {clean}")
                continue
        new_lines.append(line)
    new_content = "\n".join(new_lines)
    if new_content != content:
        with open(review_path, "w", encoding="utf-8") as f:
            f.write(new_content)


def validate_review_format(slug_dir):
    """Post-process: review.md 포맷 검증 + 자동 수정."""
    review_path = os.path.join(slug_dir, "review.md")
    if not os.path.exists(review_path):
        return
    with open(review_path, "r", encoding="utf-8") as f:
        content = f.read()
    issues = []

    # 1. 필수 섹션 존재 확인
    required = ["## Essence", "## Motivation", "## Achievement", "## How",
                 "## Originality", "## Limitation", "## Evaluation"]
    for sec in required:
        if sec not in content:
            issues.append(f"Missing section: {sec}")

    # 2. Python 리스트 리터럴 잔류
    if re.search(r"^\['.{20,}", content, re.MULTILINE):
        issues.append("Python list literal remaining")

    # 3. Evaluation 테이블 형식 잔류
    if "## Evaluation" in content:
        eval_part = content.split("## Evaluation")[-1][:500]
        if "| " in eval_part and "---" in eval_part:
            issues.append("Evaluation in table format")

    # 4. 빈 DOI 링크
    if "[](https://doi.org/)" in content:
        issues.append("Empty DOI link")

    # 5. 제목이 파일명
    title_m = re.search(r'^#\s+(.+)', content, re.MULTILINE)
    if title_m and ".pdf" in title_m.group(1):
        issues.append(f"Title contains filename: {title_m.group(1)[:40]}")

    if issues:
        slug = os.path.basename(slug_dir)
        log(f"  FORMAT ISSUES in {slug}: {issues}")

    return issues


def fix_figure_paths(slug_dir):
    """Post-process: replace placeholder URLs and broken figure paths with actual figure files."""
    review_path = os.path.join(slug_dir, "review.md")
    if not os.path.exists(review_path):
        return
    with open(review_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Build map of available figures
    fig_dir = os.path.join(slug_dir, "figures")
    fig_map = {}
    if os.path.isdir(fig_dir):
        for fname in os.listdir(fig_dir):
            m = re.match(r"fig(\d+)\.(png|webp)", fname)
            if m:
                fig_map[int(m.group(1))] = f"figures/{fname}"

    if not fig_map:
        return

    changed = False

    # Replace any external image URL `![alt](http(s)://...)` with the matching
    # local figure. Picks figure number from alt text ("Figure 3", "Fig.2",
    # "그림 1"); falls back to sequential assignment from available figures.
    seq_state = {"next": min(fig_map.keys())}
    sorted_keys = sorted(fig_map.keys())
    ext_replaced = 0

    def replace_external_image(match):
        nonlocal ext_replaced
        alt = match.group(1)
        target = None
        num_m = re.search(r"(?:Figure|Fig\.?|그림)\s*(\d+)", alt, re.IGNORECASE)
        if num_m:
            n = int(num_m.group(1))
            if n in fig_map:
                target = fig_map[n]
        if target is None:
            for k in sorted_keys:
                if k >= seq_state["next"]:
                    target = fig_map[k]
                    seq_state["next"] = k + 1
                    break
        if target is None:
            return match.group(0)
        ext_replaced += 1
        return f"![{alt}]({target})"

    new_content = re.sub(
        r"!\[([^\]]*)\]\(https?://[^)]+\)",
        replace_external_image,
        content,
    )
    if new_content != content:
        content = new_content
        changed = True

    # Legacy placeholder pattern fallback (cases without `![alt](...)` syntax,
    # e.g. inline `<img src=...>` shipped by an older prompt template).
    def replace_placeholder(match):
        url = match.group(0)
        fig_m = re.search(r"Fig[+_ ](\d+)", url)
        if fig_m:
            num = int(fig_m.group(1))
            if num in fig_map:
                return fig_map[num]
        if 1 in fig_map:
            return fig_map[1]
        return url

    if "placeholder" in content:
        new_content = re.sub(r"https://via\.placeholder\.com/[^\)]+", replace_placeholder, content)
        if new_content != content:
            content = new_content
            changed = True

    # Fix broken relative paths (e.g., figures/fig1.png when only .webp exists)
    def fix_ext(match):
        path = match.group(1)
        fig_m = re.match(r"figures/fig(\d+)\.(png|webp)", path)
        if fig_m:
            num = int(fig_m.group(1))
            if num in fig_map and fig_map[num] != path:
                return f"({fig_map[num]})"
        return match.group(0)

    new_content = re.sub(r"\((figures/fig\d+\.(?:png|webp))\)", fix_ext, content)
    if new_content != content:
        content = new_content
        changed = True

    if changed:
        with open(review_path, "w", encoding="utf-8") as f:
            f.write(content)
        slug = os.path.basename(slug_dir)
        log(f"  {slug}: fixed figure paths")


def fix_evaluation_format(slug_dir):
    """Post-process: convert any remaining Evaluation tables to list format."""
    review_path = os.path.join(slug_dir, "review.md")
    if not os.path.exists(review_path):
        return
    with open(review_path, "r", encoding="utf-8") as f:
        content = f.read()
    # If Evaluation has table rows, convert
    if "## Evaluation" in content and "| " in content.split("## Evaluation")[-1][:500]:
        eval_section = content.split("## Evaluation")[-1]
        scores = {}
        for label in ["Novelty", "Technical Soundness", "Significance", "Clarity", "Overall"]:
            m = re.search(rf'{label}\D*(\d+(?:\.\d+)?)\s*/\s*5', eval_section)
            if m:
                scores[label] = m.group(1)
        verdict_m = re.search(r'\*\*총평\*\*[:\s]*(.+?)(?:\n|$)', eval_section)
        verdict = verdict_m.group(1).strip() if verdict_m else ""

        new_eval = "\n## Evaluation\n\n"
        for label in ["Novelty", "Technical Soundness", "Significance", "Clarity", "Overall"]:
            new_eval += f"- {label}: {scores.get(label, '3')}/5\n"
        if verdict:
            new_eval += f"\n**총평**: {verdict}\n"

        before_eval = content.split("## Evaluation")[0]
        content = before_eval + new_eval
        with open(review_path, "w", encoding="utf-8") as f:
            f.write(content)


# ── Phase 5: Convert to HTML ──

def convert_to_html(slug):
    try:
        # Import review_to_html from repo
        sys.path.insert(0, str(PIPELINE_DIR))
        from review_to_html import convert_review, detect_topic
        md_path = os.path.join(PAPERS_DIR, slug, "review.md")
        html_path = os.path.join(PAPERS_DIR, slug, "index.html")
        index_path = os.path.join(PAPERS_DIR, "_papers_index.json")
        if not os.path.exists(md_path):
            return False
        topic = detect_topic(slug, index_path)
        # convert_review's figure-existence guard resolves figures/figN.png
        # against this arg, so it MUST be the full slug directory — passing
        # the bare slug name made the check look under CWD and silently drop
        # every figure from the rendered HTML (review_to_html.py:697 and
        # validate_papers.py:497 both pass the full dir).
        slug_dir = os.path.join(PAPERS_DIR, slug)
        html = convert_review(md_path, topic, slug_dir)
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html)
        return True
    except Exception as e:
        log(f"  html failed: {e}")
        return False


# ── Process single paper ──

def make_slug(item, existing_slugs):
    """Match item to existing slug or generate a new one.

    Matching policy (Phase 4 collision fix):
      • Normalise title and slug-text by stripping non-alphanumerics and
        lowercasing.
      • Require the FULL 40-character prefix to match — the original
        25-character cutoff conflated different papers that shared their
        first few words (e.g. "A hierarchical framework for measuring
        scientific impact" vs "A Hierarchical Framework for Humanoid
        Locomotion with Supernumerary Limbs", both → `ahierarchical
        frameworkfor` at 25 chars).
      • Both sides must have ≥ 40 normalised chars to be eligible; short
        titles fall through to new-slug allocation rather than risking a
        false match.
    """
    title = item.get("title", "Unknown")
    norm_title = re.sub(r"[^a-z0-9]", "", title.lower())

    # Match against existing slugs. The compared prefix length is
    # ``min(40, min(len(a), len(b)))``: 40 chars when both sides are long
    # enough (rejects the "Hierarchical Framework for measuring/Humanoid"
    # false positive at chars 25-40), but the full overlap when either
    # title is shorter (matches "Robot Learning from Human Videos: A
    # Survey" — 35 normalised chars — against its own existing slug).
    # Require a 10-char floor so single-word titles can't claim each
    # other.
    if len(norm_title) >= 10:
        for s in existing_slugs:
            parts = s.split("_", 1)
            if len(parts) < 2:
                continue
            slug_text = re.sub(r"[^a-z0-9]", "", parts[1].lower())
            if len(slug_text) < 10:
                continue
            match_len = min(40, len(norm_title), len(slug_text))
            if match_len >= 10 and norm_title[:match_len] == slug_text[:match_len]:
                return s

    # No match → new slug
    safe = "".join(c if c.isalnum() or c in " -_" else "" for c in title)[:60].strip()
    safe = safe.replace(" ", "_")
    max_num = 0
    for d in existing_slugs:
        m = re.match(r"(\d+)_", d)
        if m:
            max_num = max(max_num, int(m.group(1)))
    return f"{max_num + 1:03d}_{safe}"


def paper_has_other_topics(slug):
    """Check if paper belongs to topics other than the current one."""
    index_path = os.path.join(PAPERS_DIR, "_papers_index.json")
    if not os.path.exists(index_path):
        return False
    try:
        with open(index_path, "r", encoding="utf-8") as f:
            papers = json.load(f)
        for p in papers:
            if p.get("slug") == slug:
                topics = p.get("topics", [])
                return len(topics) > 1
    except Exception:
        pass
    return False


MAX_RETRIES = 3


def _index_entries_for_ingest():
    """`_papers_index.json` entries the ingest thread needs to build rows.

    Read once up front: the ingest thread must not re-read a 10 MB index on
    every flush, and the index may be rewritten while the pool is running.
    """
    path = os.path.join(PAPERS_DIR, "_papers_index.json")
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return []


class BibliographyIngestor:
    """Loads reviewed papers into the bibliography DB during the run.

    Reviews run at `--concurrency 16`; SQLite takes one writer at a time and the
    DB ships with `journal_mode=delete` and `busy_timeout=0`, so sixteen workers
    writing directly would either serialise behind the lock or fail outright
    with "database is locked". Instead every worker hands its slug to a queue
    and a single background thread does all the writing — reviews stay fully
    parallel, and rows land in the DB while the run is still going instead of
    only at the end.

    Batches are flushed by size or by idle time, whichever comes first. The
    table-wide consolidation passes (~1.6 s each run) are deferred and executed
    once by `close()`.
    """

    def __init__(self, db_path, index_entries, batch=8, idle=20.0):
        self._db_path = db_path
        self._by_slug = {e["slug"]: e for e in index_entries}
        self._batch = max(1, batch)
        self._idle = idle
        self._queue = queue.Queue()
        self._thread = None
        self._stats = {"ingested": 0, "flushes": 0, "errors": 0, "skipped": 0}
        self._lock = threading.Lock()

    def start(self):
        if self._thread is not None:
            return self
        self._thread = threading.Thread(
            target=self._run, name="bibliography-ingest", daemon=True)
        self._thread.start()
        log("  [bibliography] 실시간 적재 스레드 시작 "
            f"(batch={self._batch}, idle={self._idle:.0f}s)")
        return self

    def submit(self, slug):
        """Non-blocking hand-off from a review worker."""
        if self._thread is not None:
            self._queue.put(slug)

    def close(self, timeout=1800):
        """Drain, then run the deferred table-wide passes."""
        if self._thread is None:
            return self._stats
        self._queue.put(None)
        self._thread.join(timeout)
        try:
            import build_bibliography_db as bib
            final = bib.finalize(_pathlib.Path(self._db_path))
            self._stats["finalize"] = final
        except Exception as exc:
            self._stats["errors"] += 1
            log(f"  [bibliography] finalize 실패: {type(exc).__name__}: {exc}")
        log(f"  [bibliography] 적재 완료: {self._stats}")
        return self._stats

    def _run(self):
        pending, deadline = [], None
        while True:
            timeout = None if deadline is None else max(
                0.1, deadline - time.monotonic())
            try:
                slug = self._queue.get(timeout=timeout)
            except queue.Empty:
                self._flush(pending)
                pending, deadline = [], None
                continue
            if slug is None:
                self._flush(pending)
                return
            pending.append(slug)
            deadline = deadline or (time.monotonic() + self._idle)
            if len(pending) >= self._batch:
                self._flush(pending)
                pending, deadline = [], None

    def _flush(self, slugs):
        slugs = [s for s in slugs if s]
        if not slugs:
            return
        import build_bibliography_db as bib
        # Only papers whose sidecar is readable are ingested here. Without one
        # the builder would page the entire Zotero library (~200 s) on every
        # batch, so those are left to the post-run `--changed-only` build that
        # pages it once. `skip_zotero=True` is therefore safe: the sidecar is
        # the Zotero record.
        entries = [self._by_slug[s] for s in slugs
                   if s in self._by_slug
                   and bib.load_sidecar(bib.PAPERS_DIR / s) is not None]
        deferred = len(slugs) - len(entries)
        if deferred:
            with self._lock:
                self._stats["skipped"] += deferred
        if not entries:
            return
        try:
            bib.build(entries, _pathlib.Path(self._db_path),
                      skip_zotero=True, offline=False,
                      defer_consolidation=True)
            with self._lock:
                self._stats["ingested"] += len(entries)
                self._stats["flushes"] += 1
            log(f"  [bibliography] {len(entries)}편 적재 "
                f"(누적 {self._stats['ingested']})")
        except Exception as exc:
            with self._lock:
                self._stats["errors"] += 1
            # Never fail a review run over ingestion: the sidecars survive and
            # the post-run `--changed-only` build picks the papers up.
            log(f"  [bibliography] 적재 실패 ({len(entries)}편, "
                f"사이드카는 보존): {type(exc).__name__}: {exc}")


SIDECAR_NAME = "bibliography.json"
SIDECAR_SCHEMA = "bibliography-sidecar-1"


def write_bibliography_sidecar(item, slug_dir, pdf_path):
    """Persist bibliographic facts at review time, next to the review.

    Review generation is the only moment where the Zotero record, the freshly
    extracted `text.md` and the matched PDF are all in hand at once. Writing them
    out here means the later DB build does not have to page the whole Zotero
    library back over the network (a fixed ~200 s that also failed with a 502 and
    silently dropped 939 `zotero_item_key` values) nor re-open every PDF.

    A file, not a direct DB write: reviews run at `--concurrency 16`, and a
    per-paper insert would serialise all of them behind one SQLite writer lock.

    `text_md_sha256` pins the affiliations to the text they came from, so a
    stale sidecar is ignored rather than trusted.
    """
    import hashlib

    text_path = os.path.join(slug_dir, "text.md")
    payload = {
        "schema": SIDECAR_SCHEMA,
        "captured_at": datetime.now().isoformat(timespec="seconds"),
        "zotero": {k: item.get(k) for k in (
            "key", "title", "DOI", "publicationTitle", "date", "volume",
            "issue", "pages", "publisher", "ISSN", "itemType", "url",
            "archiveID", "extra", "journalAbbreviation") if item.get(k)},
        "authors": [
            (" ".join(p for p in (c.get("firstName"), c.get("lastName")) if p)
             or c.get("name", ""))
            for c in (item.get("creators") or [])
            if c.get("creatorType") in (None, "author")],
    }
    try:
        with open(text_path, "rb") as fh:
            payload["text_md_sha256"] = hashlib.sha256(fh.read()).hexdigest()
    except OSError:
        payload["text_md_sha256"] = ""

    try:
        payload["affiliations"] = _extract_affiliations_for_sidecar(
            slug_dir, pdf_path, payload["authors"], payload["zotero"])
    except Exception as exc:                      # never block a review
        payload["affiliations"] = []
        payload["affiliation_error"] = f"{type(exc).__name__}: {exc}"

    tmp = os.path.join(slug_dir, SIDECAR_NAME + ".tmp")
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=1)
    os.replace(tmp, os.path.join(slug_dir, SIDECAR_NAME))
    return payload


def _extract_affiliations_for_sidecar(slug_dir, pdf_path, authors, zotero):
    """Institutions for one paper, using the bibliography builder's own code.

    Imported rather than reimplemented: the extraction window, the ROR
    normalisation, the country rule and the parent-group rules must stay
    identical to what `build_bibliography_db.py` would produce, or the sidecar
    becomes a second, diverging source of truth.
    """
    from pathlib import Path

    import build_bibliography_db as bib

    text_path = Path(slug_dir) / "text.md"
    if not text_path.exists():
        return []
    _header, raw_affs, _conf = bib.extract_header(text_path)
    pdf = Path(pdf_path) if pdf_path and os.path.exists(pdf_path) else None
    window = bib._pdf_text_for_affiliations(pdf, text_path)
    records = bib.reconcile_affiliations(
        [], window, raw_affs, offline=True,
        paper_title=str(zotero.get("title") or ""), authors=authors)
    out = []
    for record in records:
        name = bib.canonical_institution(record["name"])
        country = record.get("country") or bib.country_from_raw(
            record.get("raw_name", ""))
        ror = bib.ror_normalize(record.get("raw_name", ""), name, country,
                                offline=True)
        out.append({
            "raw_name": record.get("raw_name", ""),
            "name": ror.get("institution") or name,
            "country_name": country,
            "ror_id": ror.get("ror_id", ""),
            "parent_name": ror.get("parent", ""),
            "parent_ror_id": ror.get("parent_ror_id", ""),
            "name_source": ror.get("evidence", ""),
            "source": record.get("source", "pdf"),
        })
    return out


def _do_process(item, slug, slug_dir, pdf_path):
    """Single attempt: text.md → figures → review.md → index.html.
    Returns (status, reason) — status is 'ok' or 'fail'."""

    # Extract text
    log(_paper_progress(slug, "text.md 추출"))
    extract_text(pdf_path, slug_dir)
    text_path = os.path.join(slug_dir, "text.md")
    if not os.path.exists(text_path) or os.path.getsize(text_path) < 100:
        return "fail", "text_extraction_failed"

    # Zotero ↔ text sanity check (zero-cost PDF integrity gate)
    ok, reason = _zotero_text_sanity(item, text_path)
    if not ok:
        log(f"  {slug}: SANITY FAIL ({reason}) — aborting review")
        return "fail", f"sanity_mismatch:{reason}"

    # Extract figures
    log(_paper_progress(slug, "figure 추출"))
    figures = extract_figures(pdf_path, slug_dir)
    log(f"  {slug}: {len(figures)} figures extracted")

    # Write review
    log(_paper_progress(slug, "review.md 생성"))
    write_review(item, slug_dir, figures)
    review_path = os.path.join(slug_dir, "review.md")
    if not os.path.exists(review_path) or os.path.getsize(review_path) < 200:
        return "fail", "review_write_failed"

    # Bibliography sidecar: Zotero record + authors + ROR-normalised
    # institutions, captured while the item, text.md and the PDF are all in
    # hand. `build_bibliography_db.py` consumes it instead of re-paging the
    # whole Zotero library and re-opening every PDF.
    log(_paper_progress(slug, "서지 추출"))
    sidecar = write_bibliography_sidecar(item, slug_dir, pdf_path)
    log(f"  {slug}: 저자 {len(sidecar['authors'])}명 · "
        f"기관 {len(sidecar['affiliations'])}곳")

    # Phase 3: tool-use schema enforces structured output, so the
    # post-hoc fixers (fix_python_list_literals / fix_evaluation_format /
    # fix_figure_paths / validate_review_format) are obsolete. Definitions
    # are kept below for backward-compat tooling but no longer invoked.

    # Convert to HTML
    log(_paper_progress(slug, "HTML 변환"))
    convert_to_html(slug)
    html_path = os.path.join(slug_dir, "index.html")
    if not os.path.exists(html_path) or os.path.getsize(html_path) < 200:
        return "fail", "html_conversion_failed"

    return "ok", ""


def process_paper(item, slug, cp):
    """Process a single paper with up to MAX_RETRIES auto-retries on failure."""
    if slug in cp["completed"]:
        return "skipped"

    slug_dir = os.path.join(PAPERS_DIR, slug)
    os.makedirs(slug_dir, exist_ok=True)

    # Clean existing files — but SKIP if paper belongs to other topics too
    if paper_has_other_topics(slug):
        log(f"  {slug}: belongs to multiple topics, skipping file deletion")
    else:
        for fname in ["review.md", "index.html", "text.md"]:
            fpath = os.path.join(slug_dir, fname)
            if os.path.exists(fpath):
                os.remove(fpath)
        fig_dir = os.path.join(slug_dir, "figures")
        if os.path.isdir(fig_dir):
            shutil.rmtree(fig_dir)

    # Find PDF
    log(_paper_progress(slug, "PDF 매칭"))
    pdf_path, match_method = find_pdf(item)
    if not pdf_path:
        log(f"  {slug}: no PDF found (method={match_method})")
        with _cp_lock:
            cp["failed"].append({"slug": slug, "reason": f"no_pdf:{match_method}"})
        save_checkpoint(cp)
        return "no_pdf"
    # Record Zotero item key → slug mapping for index persistence (Phase 1
    # PDF integrity field). Keyed across threads via _cp_lock for safety.
    with _cp_lock:
        _slug_to_zotero_key[slug] = item.get("key", "")
        _slug_to_pdf_path[slug] = pdf_path
    if match_method == "fuzzy":
        log(f"  {slug}: PDF matched via FUZZY — review required")

    # Try up to MAX_RETRIES times
    last_reason = ""
    for attempt in range(1, MAX_RETRIES + 1):
        status, reason = _do_process(item, slug, slug_dir, pdf_path)
        if status == "ok":
            with _cp_lock:
                cp["completed"].append(slug)
            save_checkpoint(cp)
            if attempt > 1:
                log(f"  {slug}: succeeded on attempt {attempt}")
            return "ok"
        last_reason = reason
        log(f"  {slug}: attempt {attempt}/{MAX_RETRIES} failed ({reason})")
        if attempt < MAX_RETRIES:
            time.sleep(2)

    # All retries exhausted
    log(f"  {slug}: FAILED after {MAX_RETRIES} attempts ({last_reason})")
    with _cp_lock:
        cp["failed"].append({"slug": slug, "reason": last_reason})
    save_checkpoint(cp)
    return last_reason


# ── Main ──

# ── Phase 2: 3-axis mode mapping ─────────────────────────────────────────────
# MECE modes replace the 8-recipe legacy grid. Each --mode implies a specific
# combination of --resume/--skip-existing/--timeline/--category. When --mode
# is not used, the legacy flags behave exactly as before (backward compatible).
_MODE_LEGACY_MAP = {
    "curate":     {"resume": True,  "skip_existing": True,  "timeline": False, "category": False},
    "rebuild":    {"resume": False, "skip_existing": False, "timeline": False, "category": False},
    "reclassify": {"resume": True,  "skip_existing": True,  "timeline": False, "category": True},
    "retime":     {"resume": True,  "skip_existing": True,  "timeline": True,  "category": False},
}


def _apply_mode_mapping(args):
    """Translate --mode into legacy flag values.

    When args.mode is None (default), this is a no-op and existing callers keep
    working unchanged. When --mode is set, any conflicting legacy flag that was
    *explicitly* provided earns a DeprecationWarning, and the mode wins.
    """
    if args.mode is None:
        return  # legacy-only invocation, nothing to do

    target = _MODE_LEGACY_MAP[args.mode]
    # Detect explicit legacy flags that diverge from the mode's target
    overridden = []
    for field, expected in target.items():
        current = getattr(args, field)
        if current and not expected:
            overridden.append(f"--{field.replace('_', '-')}")
    if overridden:
        print(f"[deprecated] --mode {args.mode} overrides legacy flags: "
              f"{', '.join(overridden)} (these will be ignored)",
              file=sys.stderr)

    # Apply the mapping
    for field, value in target.items():
        setattr(args, field, value)
    print(f"[mode] {args.mode} → resume={args.resume}, skip_existing={args.skip_existing}, "
          f"timeline={args.timeline}, category={args.category}")


def _run_curate(topic, *, mode=None, concurrency=16, resume=False,
                 skip_existing=False, limit=0, timeline=False, category=False,
                 strict_pdf=False, slugs="", dry_run=False, skip_dedup=False,
                 dedup_execute=False):
    """Programmatic entrypoint. Patches ``sys.argv`` so the existing
    ``main()`` argparse parses the kwargs as if from the CLI. Behaviour-
    preserving; restores ``sys.argv`` on exit.
    """
    argv_backup = sys.argv[:]
    new_argv = ["run_update_force.py", "--topic", str(topic),
                "--concurrency", str(concurrency)]
    if mode:
        new_argv.extend(["--mode", str(mode)])
    if resume:
        new_argv.append("--resume")
    if skip_existing:
        new_argv.append("--skip-existing")
    if limit and limit > 0:
        new_argv.extend(["--limit", str(limit)])
    if timeline:
        new_argv.append("--timeline")
    if category:
        new_argv.append("--category")
    if strict_pdf:
        new_argv.append("--strict-pdf")
    if slugs:
        new_argv.extend(["--slugs", str(slugs)])
    if dry_run:
        new_argv.append("--dry-run")
    if skip_dedup:
        new_argv.append("--skip-dedup")
    if dedup_execute:
        new_argv.append("--dedup-execute")
    sys.argv = new_argv
    try:
        return main()
    finally:
        sys.argv = argv_backup


def main():
    parser = argparse.ArgumentParser(description="Paper-curation --update-force batch")
    parser.add_argument("--topic", default="ai4s", help="Topic: ai4s or scisci")
    parser.add_argument("--concurrency", type=int, default=16, help="Parallel workers (Tier 4 default; lower for Tier 1~3 — see README)")
    parser.add_argument("--resume", action="store_true", help="Resume from checkpoint")
    parser.add_argument("--skip-existing", action="store_true",
                        help="Skip papers that already have review.md (for --update mode)")
    parser.add_argument("--limit", type=int, default=0, help="Limit papers (0=all)")
    parser.add_argument("--timeline", action="store_true",
                        help="Regenerate timeline images (with --resume: changed cats only, alone: all cats)")
    parser.add_argument("--ensure-timeline", action="store_true",
                        help="기본 narrative/timeline 산출물이 없으면 생성하고, 업데이트 중 바뀐 카테고리만 보강한다.")
    parser.add_argument("--category", action="store_true",
                        help="Re-run topic_modeling to reclassify all papers. Auto-enables --timeline for changed categories.")
    parser.add_argument("--strict-pdf", action="store_true",
                        help="Disable fuzzy PDF matching — skip papers without Zotero/DOI/arXiv link.")
    parser.add_argument("--slugs", default="",
                        help="Comma-separated slug prefixes (e.g. '088,1093'). Only these papers are (re)processed. "
                             "Implies force-rebuild of the listed slugs regardless of checkpoint.")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print which papers would be processed and exit without writing.")
    parser.add_argument("--skip-dedup", action="store_true",
                        help="Skip the Zotero duplicate preflight (saves ~1-5 min; not recommended).")
    parser.add_argument("--skip-metrics", action="store_true",
                        help="피인용수·레퍼런스 수집(citations.md/references.md) 스킵. "
                             "외부 API 를 타므로 오프라인이거나 급할 때.")
    parser.add_argument("--dedup-execute", action="store_true",
                        help="Let the Zotero dedup preflight actually delete duplicates. "
                             "Default is dry-run (report only).")
    parser.add_argument("--insights", action="store_true",
                        help="extract_insights 에서 cross-category insights(Option)까지 재생성. "
                             "기본은 paper connections(Core, '같이 보면 좋은 논문')만 생성 (--only connections).")
    parser.add_argument("--local-fallback", action="store_true",
                        help="topic_modeling 연결 단계에서 max retry round 를 다 돌고도 막힌 "
                             "papers 를 로컬 OpenAI 호환 모델(Ollama/LM Studio 등)로 마저 연결. "
                             "config.json 의 local_model 또는 LOCAL_MODEL_BASE_URL/NAME 필요.")
    parser.add_argument("--no-deploy", action="store_true",
                        help="end-of-run prepare_deploy(wrangler deploy + gh-pages + master push)를 건너뛴다. "
                             "무인 자동복구(auto_recover --execute)처럼 배포를 원치 않는 경우용. "
                             "환경변수 PAPER_CURATION_NO_DEPLOY 로도 켤 수 있다.")
    parser.add_argument("--conn-full", action="store_true",
                        help="연결 캐시(_conn_topk_cache_k*.json)를 무시하고 이번 실행에서 전체 연결을 "
                             "재생성한다 (월간/대량 추가 후 주기적 full rebuild 용). 자식 프로세스"
                             "(extract_insights / topic_modeling)가 환경변수 CONN_FULL_REBUILD=1 로 "
                             "상속한다. 환경변수 CONN_FULL_REBUILD=1 로도 직접 켤 수 있다.")
    # ── Phase 2: 3-axis mode (new, MECE). When --mode is set, it overrides the
    # legacy flag combinations and emits DeprecationWarnings for any legacy
    # flags that were also specified. Omitting --mode keeps 100% legacy
    # behavior, so existing callers (incl. in-flight batches) are unaffected.
    parser.add_argument("--mode", choices=["curate", "rebuild", "reclassify", "retime"],
                        default=None,
                        help="New MECE mode selector. curate=new papers only (keeps existing reviews); "
                             "rebuild=regenerate all reviews; reclassify=re-run topic modeling on existing reviews; "
                             "retime=regenerate timeline narratives+images only. "
                             "When set, overrides --resume/--skip-existing/--timeline/--category combinations.")
    args = parser.parse_args()

    # Apply --mode → legacy flags mapping. Pure translation; no behavior change
    # when --mode is absent (args.mode is None → all legacy flags honored as-is).
    _apply_mode_mapping(args)

    # --conn-full → force full connection regen for child subprocesses
    # (extract_insights / topic_modeling). They read CONN_FULL_REBUILD from env,
    # which is inherited across subprocess.run, so setting it here is enough.
    if getattr(args, "conn_full", False):
        os.environ["CONN_FULL_REBUILD"] = "1"
        print("[conn] --conn-full → CONN_FULL_REBUILD=1 "
              "(전체 연결 재생성; 자식 프로세스 env 상속)")

    # Propagate strict-pdf flag to find_pdf()
    global _STRICT_PDF
    _STRICT_PDF = args.strict_pdf
    if _STRICT_PDF:
        print("[strict-pdf] fuzzy PDF matching disabled — papers without authoritative PDF links will be skipped")

    # ── Rebuild safety: snapshot _papers_index.json so an accidental wipe
    # is reversible. Only triggered when --mode rebuild AND not --slugs (mass).
    if args.mode == "rebuild" and not args.slugs and not args.dry_run:
        idx_path = os.path.join(PAPERS_DIR, "_papers_index.json")
        if os.path.exists(idx_path):
            backup_path = os.path.join(PAPERS_DIR, "_papers_index.backup.json")
            try:
                shutil.copy2(idx_path, backup_path)
                print(f"[rebuild-safety] snapshot saved: {backup_path}")
            except Exception as _e:
                print(f"[rebuild-safety] snapshot FAILED: {_e}")

    # ── Preflight: Zotero dedup ────────────────────────────────────────────
    # Runs in ALL modes (full/local/update). Users may accidentally double-
    # register the same paper in Zotero via the UI or imports; running this
    # every time keeps the collection clean before we spend compute on reviews.
    # Default is dry-run → a report is written to {topic}/_dedup_zotero_report.json;
    # pass --dedup-execute once trust is built and you want auto-deletion.
    # `--slugs` and `--dry-run` modes skip the preflight because they are
    # targeted operations that should not touch the collection as a whole.
    if not args.skip_dedup and not args.slugs and not args.dry_run:
        dedup_script = os.path.join(os.path.dirname(__file__), "dedup_zotero.py")
        if os.path.exists(dedup_script):
            print(f"\n[preflight] Zotero dedup ({'EXECUTE' if args.dedup_execute else 'dry-run'}) for topic={args.topic}")
            dedup_cmd = [sys.executable, dedup_script, "--topic", args.topic]
            if args.dedup_execute:
                dedup_cmd.append("--execute")
            rc = subprocess.call(dedup_cmd)
            if rc != 0:
                print(f"[preflight] dedup exited {rc} — continuing anyway")

    collection_key = COLLECTIONS.get(args.topic, "")
    if not collection_key:
        print(f"Unknown topic: {args.topic}")
        return

    # Load checkpoint
    if args.resume:
        cp = load_checkpoint()
        # Clear failed list so they get retried
        prev_failed = len(cp.get("failed", []))
        cp["failed"] = []
        previously_completed = set(cp.get("completed", []))
        log(f"Resuming: {len(cp['completed'])} completed, {prev_failed} previously failed (will retry)")
    else:
        cp = {"completed": [], "failed": [], "phase": "init"}
        previously_completed = set()

    sync_bibliography_db("--pull")
    # Fetch items
    log(f"Fetching Zotero collection '{args.topic}' ({collection_key})...")
    items = fetch_zotero_items(collection_key)
    log(f"Total papers: {len(items)}")

    # Get existing slugs
    existing_slugs = sorted(d for d in os.listdir(PAPERS_DIR)
                            if os.path.isdir(os.path.join(PAPERS_DIR, d)) and d[0].isdigit())

    # Map items to slugs
    item_slug_pairs = []
    for item in items:
        slug = make_slug(item, existing_slugs)
        item_slug_pairs.append((item, slug))
        if slug not in existing_slugs:
            existing_slugs.append(slug)

    # --slugs filter: restrict processing to listed slug prefixes, and force-rebuild them
    if args.slugs:
        wanted_prefixes = [s.strip() for s in args.slugs.split(",") if s.strip()]
        before = len(item_slug_pairs)
        item_slug_pairs = [
            (it, slug) for (it, slug) in item_slug_pairs
            if any(slug.startswith(p) or slug == p for p in wanted_prefixes)
        ]
        log(f"--slugs: kept {len(item_slug_pairs)}/{before} papers matching {wanted_prefixes}")
        # Force rebuild: drop from checkpoint.completed so they are re-processed
        kept = {slug for _, slug in item_slug_pairs}
        cp["completed"] = [s for s in cp.get("completed", []) if s not in kept]
        save_checkpoint(cp)

    # Rebuild safety: preview PDF matching for first 5 papers so the
    # operator can spot fuzzy/wrong matches before the destructive run.
    if args.mode == "rebuild" and not args.slugs and not args.dry_run:
        print(f"\n[rebuild-preview] sampling 5 PDFs to verify matching before "
              f"processing {len(item_slug_pairs)} papers:")
        for it, slug in item_slug_pairs[:5]:
            try:
                _p, _m = find_pdf(it)
            except Exception as _e:
                _p, _m = None, f"err:{_e}"
            print(f"  {slug[:55]:55s} | method={_m} | path={_p or '(none)'}")
        print(f"[rebuild-preview] proceed if these look correct. "
              f"Ctrl-C now to abort.\n")

    if args.dry_run:
        print(f"[dry-run] would process {len(item_slug_pairs)} papers:")
        for _, slug in item_slug_pairs[:50]:
            print(f"  {slug}")
        if len(item_slug_pairs) > 50:
            print(f"  ... +{len(item_slug_pairs) - 50} more")
        return

    # Skip papers with existing review.md (--skip-existing or --resume).
    # When --slugs is used the listed papers must be force-rebuilt, so they
    # are intentionally excluded from this "already done" shortcut.
    forced_slugs = set()
    if args.slugs:
        forced_slugs = {slug for _, slug in item_slug_pairs}

    # PDF-change auto-detect: if _papers_index.json has cached pdf_path for a
    # slug AND that PDF's mtime is newer than the slug's review.md, force a
    # rebuild. Cheap (stat-only) — no Zotero API calls. Cache populated by
    # prior find_pdf hits and persisted in the index.
    if args.skip_existing or args.resume:
        try:
            _idx_path = os.path.join(PAPERS_DIR, "_papers_index.json")
            if os.path.exists(_idx_path):
                with open(_idx_path, "r", encoding="utf-8") as _f:
                    _cached = {p["slug"]: p.get("pdf_path", "") for p in json.load(_f)}
                _pdf_detected = []
                for _, slug in item_slug_pairs:
                    if slug in forced_slugs:
                        continue
                    _pdf = _cached.get(slug, "")
                    _review = os.path.join(PAPERS_DIR, slug, "review.md")
                    if _pdf and os.path.exists(_pdf) and os.path.exists(_review):
                        if os.path.getmtime(_pdf) > os.path.getmtime(_review):
                            _pdf_detected.append(slug)
                if _pdf_detected:
                    forced_slugs.update(_pdf_detected)
                    log(f"[pdf-change] {len(_pdf_detected)} papers: PDF mtime > review.md mtime — forcing rebuild")
                    for _s in _pdf_detected[:10]:
                        log(f"  - {_s}")
                    if len(_pdf_detected) > 10:
                        log(f"  ... +{len(_pdf_detected)-10} more")
        except Exception as _e:
            log(f"[pdf-change] check skipped: {_e}")

    if args.skip_existing or args.resume:
        skipped = 0
        for item, slug in item_slug_pairs:
            if slug in forced_slugs:
                continue
            review_path = os.path.join(PAPERS_DIR, slug, "review.md")
            if os.path.exists(review_path) and os.path.getsize(review_path) >= 200:
                if slug not in cp["completed"]:
                    cp["completed"].append(slug)
                    skipped += 1
        save_checkpoint(cp)
        log(f"--skip-existing: {skipped} papers with existing review.md marked as completed")

    # Filter already completed
    remaining = [(item, slug) for item, slug in item_slug_pairs
                 if slug not in cp["completed"]]

    if args.limit > 0:
        remaining = remaining[:args.limit]

    log(f"To process: {len(remaining)} (completed: {len(cp['completed'])}, failed: {len(cp['failed'])})")
    _update_progress(topic=args.topic, total=len(remaining), done=0,
                     failed=len(cp["failed"]), status="running")
    log(f"Concurrency: {args.concurrency}")
    log(f"Estimated time: ~{len(remaining) * 5 / args.concurrency / 60:.1f} hours")

    # Process with thread pool
    start_time = time.time()
    done = 0

    # One writer, many reviewers: workers hand finished slugs to this thread
    # rather than contending for the SQLite write lock themselves.
    ingestor = BibliographyIngestor(
        os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                     ".cache", "bibliography.sqlite3"),
        _index_entries_for_ingest()).start()

    with ThreadPoolExecutor(max_workers=args.concurrency) as executor:
        futures = {}
        for item, slug in remaining:
            future = executor.submit(process_paper, item, slug, cp)
            futures[future] = slug

        for future in as_completed(futures):
            slug = futures[future]
            try:
                result = future.result()
                done += 1
                if str(result) in ("ok", "completed", "success"):
                    ingestor.submit(slug)
                _update_progress(done=done, failed=len(cp["failed"]))
                elapsed = time.time() - start_time
                rate = elapsed / done if done else 0
                eta = rate * (len(remaining) - done) / 3600
                log(f"[{done}/{len(remaining)}] {slug}: {result} (ETA: {eta:.1f}h)")
            except Exception as e:
                _update_progress(done=done, failed=len(cp["failed"]))
                log(f"[{done}/{len(remaining)}] {slug}: ERROR {e}")
                with _cp_lock:
                    cp["failed"].append({"slug": slug, "reason": str(e)})
                save_checkpoint(cp)

    # Drain the queue and run the deferred table-wide passes before any
    # post-processing step reads the DB.
    ingestor.close()

    elapsed_total = (time.time() - start_time) / 3600
    log(f"\nPass 1 done! {done} papers in {elapsed_total:.1f}h")
    log(f"Completed: {len(cp['completed'])}, Failed: {len(cp['failed'])}")

    # Note: per-paper auto-retry (MAX_RETRIES=3) is built into process_paper.
    # No separate retry pass needed.

    log(f"\nFinal: {len(cp['completed'])} completed, {len(cp['failed'])} failed")
    _update_progress(done=done, failed=len(cp["failed"]),
                     status="completed" if not cp["failed"] else "completed_with_failures",
                     phase="post-processing")

    # ── Persist Zotero item key + PDF path → slug mapping into _papers_index.json ──
    # build_papers_index will preserve `zotero_item_key` and `pdf_path` via prev.get(...).
    if _slug_to_zotero_key or _slug_to_pdf_path:
        try:
            from lib.atomic_io import atomic_write_json
            idx_path = os.path.join(PAPERS_DIR, "_papers_index.json")
            if os.path.exists(idx_path):
                with open(idx_path, "r", encoding="utf-8") as f:
                    _idx = json.load(f)
                _patched_key = 0
                _patched_pdf = 0
                for _e in _idx:
                    _s = _e.get("slug")
                    _k = _slug_to_zotero_key.get(_s)
                    if _k and _e.get("zotero_item_key") != _k:
                        _e["zotero_item_key"] = _k
                        _patched_key += 1
                    _p = _slug_to_pdf_path.get(_s)
                    if _p and _e.get("pdf_path") != _p:
                        _e["pdf_path"] = _p
                        _patched_pdf += 1
                if _patched_key or _patched_pdf:
                    atomic_write_json(idx_path, _idx)
                    log(f"  [persist] zotero_item_key={_patched_key}, pdf_path={_patched_pdf} mappings into _papers_index.json")
        except Exception as _e:
            log(f"  [persist] failed: {_e}")

    # ── Post-processing: rebuild index, classify, insights, topic page ──
    topic = args.topic
    newly_completed = {slug for _item, slug in remaining if slug in cp.get("completed", [])}
    do_timeline_images = args.timeline or args.category  # --category auto-enables timeline
    do_ensure_timeline = getattr(args, "ensure_timeline", False)
    missing_default_artifacts = (
        _topic_default_artifacts_missing(topic)
        if (do_ensure_timeline or do_timeline_images)
        else []
    )
    needs_postprocess = (
        bool(newly_completed)
        or (len(cp["completed"]) > 0 and not args.resume)
        or bool(args.timeline)
        or bool(args.category)
        or bool(missing_default_artifacts)
    )
    if not needs_postprocess:
        log("\nPost-processing skipped: no new papers, no explicit reclassify/retime, "
            "and default timeline artifacts already exist.")
    if needs_postprocess:
        log("\n" + "=" * 60)
        log("POST-PROCESSING: index → classify → summaries → insights → HTML → topic index")
        log("=" * 60)

        is_update = args.resume  # --resume implies update mode
        do_reclassify = args.category  # --category forces topic_modeling

        # extract_insights 는 paper connections(Core — '같이 보면 좋은 논문' 박스)만
        # 기본 생성한다. cross-category insights 는 Option 이라 --insights 가 명시될
        # 때만 둘 다(--only all) 돌린다. 미생성 시 _insights.json 은 stale/absent 로
        # 남고 build_topic_index 가 부재를 허용한다.
        insights_only_arg = ["--only", "all" if args.insights else "connections"]


        # Steps in this set MUST succeed — any non-zero exit, timeout, or
        # unexpected exception aborts the whole orchestration. Soft-failing
        # them would leave the topic with stale classifications (so new
        # papers vanish from the index) or stale per-category text (so
        # downstream renders mis-attribute work to wrong categories).
        # Anything not in this set may degrade gracefully (LLM narrative,
        # image generation, search index).
        CRITICAL_STEPS = {
            "build_papers_index",
            "topic_modeling",
            "topic_modeling (coords+connections)",
            "topic_modeling (umap fix)",
            "classify_papers",
            "build_search_index",
            "build_cross_index",
            "evaluate_retrieval",
            "evaluate_retrieval (_cross)",
            "refresh_retrieval_eval_snapshot",
            "build_bibliography_db",
            "check_bibliography_db",
            # "sync_bibliography_db (push)" is deliberately NOT critical while
            # the CAS manifest still demands the retired registry's artifacts
            # (see that module's docstring). The local DB and its strict gate
            # are what a cycle depends on; failing to mirror the DB to the
            # other host must not abort classification, indexing and deploy.
        }

        def run_step(step_name, cmd, step_timeout=600):
            log(f"  [{step_name}] ...")
            is_critical = step_name in CRITICAL_STEPS
            try:
                result = subprocess.run(
                    cmd, cwd=str(PIPELINE_DIR.parent),
                    capture_output=True, text=True, timeout=step_timeout,
                    env={**os.environ, "PYTHONUTF8": "1"},
                )
                if result.returncode != 0:
                    severity = "ABORT" if is_critical else "FAILED"
                    log(f"  [{step_name}] {severity} (exit {result.returncode})")
                    # Dump full stderr + stdout to disk so the real traceback
                    # (often >200 chars) survives for diagnosis.
                    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
                    safe_step = re.sub(r'[^A-Za-z0-9_-]+', '_', step_name)[:50]
                    dump_path = PIPELINE_DIR / "_logs" / f"step_failure_{safe_step}_{ts}.log"
                    try:
                        dump_path.parent.mkdir(parents=True, exist_ok=True)
                        with open(dump_path, "w", encoding="utf-8") as f:
                            f.write(f"=== command ===\n")
                            f.write(" ".join(str(c) for c in cmd) + "\n")
                            f.write(f"\n=== exit code: {result.returncode} ===\n")
                            f.write(f"\n=== STDERR ({len(result.stderr or '')} chars) ===\n")
                            f.write(result.stderr or "(empty)\n")
                            f.write(f"\n=== STDOUT ({len(result.stdout or '')} chars) ===\n")
                            f.write(result.stdout or "(empty)\n")
                        log(f"    [diag] full output dumped: {dump_path}")
                    except Exception as _dump_e:
                        log(f"    [diag] dump failed: {_dump_e}")
                    # Console: last 30 lines of stderr (not first 200 chars) —
                    # tracebacks are most useful at the tail.
                    if result.stderr:
                        last = result.stderr.rstrip().splitlines()[-30:]
                        for ln in last:
                            log(f"    {ln}")
                    if is_critical:
                        raise RuntimeError(
                            f"critical step '{step_name}' failed "
                            f"(exit {result.returncode}); aborting orchestration. "
                            f"See {dump_path} for full output."
                        )
                else:
                    out_lines = [l for l in result.stdout.strip().split("\n") if l.strip()]
                    if out_lines:
                        log(f"  [{step_name}] OK: {out_lines[-1][:100]}")
                    else:
                        log(f"  [{step_name}] OK")
            except subprocess.TimeoutExpired:
                log(f"  [{step_name}] TIMEOUT ({step_timeout}s)")
                if is_critical:
                    raise RuntimeError(
                        f"critical step '{step_name}' timed out "
                        f"after {step_timeout}s; aborting orchestration."
                    )
            except RuntimeError:
                raise  # critical-step abort: re-raise as-is
            except Exception as e:
                log(f"  [{step_name}] ERROR: {str(e)[:100]}")
                if is_critical:
                    raise RuntimeError(
                        f"critical step '{step_name}' raised {type(e).__name__}; "
                        "aborting orchestration."
                    ) from e

        # Step 1: Always rebuild index
        run_step("build_papers_index",
                 ["python", "pipeline/build_papers_index.py", "--topic", topic])

        # Step 1.5: 피인용수·레퍼런스 (citations.md / references.md)
        #
        # build_papers_index 직후에 둔다 — `_papers_index.json` 이 방금 갱신돼
        # 대상 목록이 정확하고, run_metrics 가 되쓰는 피인용수 캐시를 이후
        # 단계(classify / build_topic_index / build_search_index)가 그대로
        # 읽을 수 있다.
        #
        # 기본이 30일 증분이라 매 사이클 돌려도 비용이 거의 없다. 새로 리뷰된
        # 논문은 citations.md 가 없으므로 항상 대상에 들어간다.
        #
        # **soft step 이다** — 외부 API(Crossref/OpenAlex/Scopus) 장애나 망
        # 문제로 지표를 못 받는 것이 리뷰 파이프라인 전체를 중단시켜서는 안 된다.
        # CRITICAL_STEPS 에 넣지 않은 이유다.
        if not getattr(args, "skip_metrics", False):
            run_step("run_metrics",
                     ["python", "pipeline/run_metrics.py", "--quiet"],
                     step_timeout=5400)

        # Step 2: topic_modeling
        # --category: always run (reclassify all)
        # --resume without --category: skip (keep existing categories)
        # full mode: always run
        # opt-in: connection 단계가 끝까지 막히면 로컬 모델로 마저 연결 (--local-fallback)
        tm_local = ["--local-fallback"] if getattr(args, "local_fallback", False) else []
        old_cats_by_slug = {}
        if do_reclassify:
            # Snapshot current classifications before reclassification
            try:
                idx_path = os.path.join(PAPERS_DIR, "_papers_index.json")
                with open(idx_path, "r", encoding="utf-8") as f:
                    idx = json.load(f)
                for p in idx:
                    cls = p.get("classifications", {}).get(topic, {})
                    old_cats_by_slug[p["slug"]] = set(cls.get("all_categories", []))
            except Exception:
                pass
            run_step("topic_modeling",
                     [TOPIC_MODELING_PYTHON, "pipeline/topic_modeling.py", "--topic", topic] + tm_local, 3600)
        elif is_update:
            # Update mode normally runs --skip-classification (refresh coords +
            # connections only, reuse the existing HDBSCAN bundle). But
            # classify_papers.py hard-exits if `_hdbscan_model.joblib` is
            # absent. On a topic that never had a full (non-skip) run the bundle
            # doesn't exist yet, so a missing bundle must trigger a one-time
            # FULL topic_modeling (no --skip-classification) to build it,
            # rather than aborting the whole pipeline at a critical step.
            bundle_path = os.path.join(str(get_topic_dir(topic)), "_hdbscan_model.joblib")
            if not os.path.exists(bundle_path):
                log("  [topic_modeling] HDBSCAN bundle missing — running full "
                    "topic_modeling to build it (first run for this topic)")
                run_step("topic_modeling",
                         [TOPIC_MODELING_PYTHON, "pipeline/topic_modeling.py", "--topic", topic] + tm_local, 3600)
            else:
                run_step("topic_modeling (coords+connections)",
                         [TOPIC_MODELING_PYTHON, "pipeline/topic_modeling.py", "--topic", topic, "--skip-classification"] + tm_local, 3600)
        else:
            run_step("topic_modeling",
                     [TOPIC_MODELING_PYTHON, "pipeline/topic_modeling.py", "--topic", topic] + tm_local, 3600)

        # Step 3: classify (always — new papers only in update mode without --category)
        run_step("classify_papers",
                 [TOPIC_MODELING_PYTHON, "pipeline/classify_papers.py", "--topic", topic], 600)

        # Step 4: Determine changed categories
        changed_cats = []
        if do_reclassify:
            # Compare before/after classifications to find changed categories
            try:
                idx_path = os.path.join(PAPERS_DIR, "_papers_index.json")
                with open(idx_path, "r", encoding="utf-8") as f:
                    idx = json.load(f)
                cat_set = set()
                for p in idx:
                    if topic not in p.get("topics", []):
                        continue
                    slug = p["slug"]
                    cls = p.get("classifications", {}).get(topic, {})
                    new_cats = set(cls.get("all_categories", []))
                    old_cats = old_cats_by_slug.get(slug, set())
                    # Categories that gained or lost this paper
                    diff = new_cats.symmetric_difference(old_cats)
                    cat_set.update(diff)
                    cat_set.update(new_cats)  # also include current cats of moved papers
                changed_cats = sorted(cat_set) if cat_set else []
                if changed_cats:
                    log(f"  [changed_categories] {len(changed_cats)} categories changed after reclassification")
                    for c in changed_cats:
                        log(f"    - {c}")
                else:
                    log("  [changed_categories] No category changes detected — full regeneration")
            except Exception as e:
                log(f"  [changed_categories] ERROR comparing: {e} — full regeneration")
                changed_cats = []
        elif is_update and newly_completed:
            try:
                idx_path = os.path.join(PAPERS_DIR, "_papers_index.json")
                with open(idx_path, "r", encoding="utf-8") as f:
                    idx = json.load(f)
                cat_set = set()
                for p in idx:
                    if p.get("slug") in newly_completed:
                        cls = p.get("classifications", {}).get(topic, {})
                        for c in cls.get("all_categories", []):
                            cat_set.add(c)
                        pc = cls.get("primary_category", "")
                        if pc:
                            cat_set.add(pc)
                changed_cats = sorted(cat_set)
                log(f"  [changed_categories] {len(changed_cats)} categories affected by {len(newly_completed)} new papers")
                for c in changed_cats:
                    log(f"    - {c}")
            except Exception as e:
                log(f"  [changed_categories] ERROR reading index: {e}")
                changed_cats = []

        if missing_default_artifacts:
            log("  [default_outputs] missing narrative/timeline artifacts — will ensure:")
            for name in missing_default_artifacts[:12]:
                log(f"    - {name}")
            if len(missing_default_artifacts) > 12:
                log(f"    ... +{len(missing_default_artifacts) - 12} more")

        def run_default_topic_outputs(reason):
            log(f"  [default_outputs] full narrative/timeline generation ({reason})")
            run_step("build_category_summaries",
                     ["python", "pipeline/build_category_summaries.py", "--topic", topic], 1200)
            run_step("extract_insights",
                     ["python", "pipeline/extract_insights.py", "--topic", topic] + insights_only_arg, 14400)
            run_step("generate_timelines",
                     ["python", "pipeline/generate_timelines.py", "--topic", topic], 21600)
        # Step 5-6: summaries, insights, timelines — scoped by changed categories
        if do_reclassify and changed_cats and missing_default_artifacts:
            # If default outputs are absent, scoped timeline regeneration would
            # still leave the main narrative/timeline incomplete. Build all.
            run_default_topic_outputs("missing default outputs")
        elif do_reclassify and changed_cats:
            # --category: full reclassification → rebuild ALL summaries/insights (old cats must be purged)
            # Only timelines are scoped to changed categories
            run_step("build_category_summaries",
                     ["python", "pipeline/build_category_summaries.py", "--topic", topic], 1200)
            run_step("extract_insights",
                     ["python", "pipeline/extract_insights.py", "--topic", topic] + insights_only_arg, 14400)
            cats_arg = ["--categories"] + changed_cats
            run_step("generate_timelines",
                     ["python", "pipeline/generate_timelines.py", "--topic", topic] + cats_arg, 21600)
        elif do_reclassify:
            # --category but no diff detected: full regeneration
            run_step("build_category_summaries",
                     ["python", "pipeline/build_category_summaries.py", "--topic", topic], 1200)
            run_step("extract_insights",
                     ["python", "pipeline/extract_insights.py", "--topic", topic] + insights_only_arg, 14400)
            run_step("generate_timelines",
                     ["python", "pipeline/generate_timelines.py", "--topic", topic], 21600)
        elif is_update:
            if missing_default_artifacts and (do_ensure_timeline or do_timeline_images):
                run_default_topic_outputs("missing default outputs")
            elif changed_cats:
                cats_arg = ["--categories"] + changed_cats
                run_step("build_category_summaries",
                         ["python", "pipeline/build_category_summaries.py", "--topic", topic] + cats_arg, 1200)
                run_step("extract_insights",
                         ["python", "pipeline/extract_insights.py", "--topic", topic] + cats_arg + insights_only_arg, 14400)

                # Split by image presence:
                #   - cats_with_image: narrative-only (unless --timeline explicitly requested)
                #   - cats_missing_image: always full generation (new/renamed categories MUST get images)
                cats_with_image, cats_missing_image = _split_cats_by_image_presence(topic, changed_cats)
                if cats_missing_image:
                    log(f"  [generate_timelines] {len(cats_missing_image)} categories missing timeline image — will generate:")
                    for c in cats_missing_image:
                        log(f"    - {c}")
                if do_timeline_images:
                    # --timeline: full generation for all changed cats
                    run_step("generate_timelines",
                             ["python", "pipeline/generate_timelines.py", "--topic", topic] + cats_arg, 21600)
                else:
                    # Auto: narrative-only for cats with existing images
                    if cats_with_image:
                        run_step("generate_timelines (narrative)",
                                 ["python", "pipeline/generate_timelines.py", "--topic", topic,
                                  "--categories"] + cats_with_image + ["--narrative-only"], 21600)
                    # Auto: full generation for new/renamed cats without images
                    if cats_missing_image:
                        run_step("generate_timelines (images)",
                                 ["python", "pipeline/generate_timelines.py", "--topic", topic,
                                  "--categories"] + cats_missing_image, 21600)
            elif do_timeline_images:
                run_default_topic_outputs("--timeline requested")
            else:
                log("  [summaries/insights/timelines] SKIP (no new papers classified)")
        elif do_timeline_images:
            # --timeline alone (no --resume): full regeneration of all narratives + images
            run_step("build_category_summaries",
                     ["python", "pipeline/build_category_summaries.py", "--topic", topic], 1200)
            run_step("extract_insights",
                     ["python", "pipeline/extract_insights.py", "--topic", topic] + insights_only_arg, 14400)
            run_step("generate_timelines",
                     ["python", "pipeline/generate_timelines.py", "--topic", topic], 21600)
        else:
            # Full mode (no --resume, no --timeline)
            run_step("build_category_summaries",
                     ["python", "pipeline/build_category_summaries.py", "--topic", topic], 1200)
            run_step("extract_insights",
                     ["python", "pipeline/extract_insights.py", "--topic", topic] + insights_only_arg, 14400)
            run_step("generate_timelines",
                     ["python", "pipeline/generate_timelines.py", "--topic", topic], 21600)

        # Step 7-10: Always run (fast steps)
        run_step("inject_frontmatter",
                 ["python", "pipeline/inject_frontmatter.py", "--topic", topic], 600)
        # Keep the collection-independent bibliography DB synchronized with every
        # review/frontmatter refresh. The ordered helper makes strict validation
        # a hard publication gate and `--changed-only` keeps it incremental.
        run_bibliography_release_steps(run_step)
        run_step("generate_moc",
                 ["python", "pipeline/generate_moc.py", "--topic", topic], 600)
        # 네트워크 시각화는 Research Insights 와 묶인 Option(O-2) — --insights 일 때만.
        # (LLM 호출은 없지만 기능 분류상 인사이트 분석 부가물로 함께 게이트)
        if args.insights:
            run_step("generate_network",
                     ["python", "pipeline/generate_network.py", "--topic", topic], 600)
        else:
            log("  [generate_network] SKIP (Option O-2 — --insights 일 때만 재생성)")

        # Verify UMAP coordinate coverage before deploy
        try:
            topic_dir = str(get_topic_dir(topic))
            umap_path = os.path.join(topic_dir, "_umap_coords.json")
            idx_path = os.path.join(PAPERS_DIR, "_papers_index.json")
            with open(idx_path, "r", encoding="utf-8") as f:
                all_idx = json.load(f)
            topic_slugs = {p["slug"] for p in all_idx if topic in p.get("topics", [])}
            umap_slugs = set()
            if os.path.exists(umap_path):
                with open(umap_path, "r", encoding="utf-8") as f:
                    umap_slugs = set(json.load(f).keys())
            missing = topic_slugs - umap_slugs
            if missing:
                log(f"\n  [verify_umap] {len(missing)} papers missing UMAP coordinates — re-running topic_modeling...")
                run_step("topic_modeling (umap fix)",
                         [TOPIC_MODELING_PYTHON, "pipeline/topic_modeling.py", "--topic", topic, "--skip-connections"], 3600)
                if args.insights:   # 네트워크는 Option(O-2) — --insights 일 때만
                    run_step("generate_network (rebuild)",
                             ["python", "pipeline/generate_network.py", "--topic", topic], 600)
            else:
                log(f"  [verify_umap] OK: all {len(topic_slugs)} papers have coordinates")
        except RuntimeError:
            raise
        except Exception as e:
            log(f"  [verify_umap] WARNING: verification failed ({str(e)[:100]})")

        run_step("review_to_html",
                 ["python", "pipeline/review_to_html.py", "--all"], 600)
        run_step("build_topic_index",
                 ["python", "pipeline/build_topic_index.py", topic], 600)

        # Atom 피드(feed.xml) — build_topic_index 가 심은 autodiscovery <link> 의 대상.
        run_step("build_rss",
                 ["python", "pipeline/build_rss.py", topic], 300)

        # Deep Research search index (section-aware chunks + Gemini embeddings).
        # Reads GOOGLE_API_KEY/GEMINI_API_KEY from env or config.json.
        # Cleanup stale category narratives/timelines before building the
        # search index so Deep Research never surfaces renamed categories.
        # Always runs --execute because post-processing has just rewritten
        # the classifier output; any orphan entries are safe to remove.
        run_step("cleanup",
                 ["python", "pipeline/cleanup.py", "--execute"], 300)

        run_step("build_search_index",
                 ["python", "pipeline/build_search_index.py", "--topic", topic], 900)

        # `_cross` is a cheap merge of existing topic sidecars (no embedding
        # calls). Keep the agent/CLI default collection synchronized after every
        # source-topic rebuild; the generic page itself need not be regenerated.
        run_step("build_cross_index",
                 ["python", "pipeline/build_cross_index.py", "--no-page"], 300)

        # Fixed query vectors make this a deterministic, network-free deploy
        # gate. A source collection and the merged agent collection must both
        # retain the tracked recall floor and baseline before publication.
        eval_dir = PIPELINE_DIR / "eval"
        eval_results = eval_dir / "results"
        eval_common = [
            "python", "pipeline/evaluate_retrieval.py",
            "--queries", str(eval_dir / "retrieval_queries.jsonl"),
            "--vectors", str(eval_dir / "retrieval_query_vectors.json"),
            "--baseline", str(eval_dir / "retrieval_baseline.json"),
            "--strict",
            "--min-recall-at-5", "0",
            "--max-regression", "0.025",
        ]
        run_step("evaluate_retrieval",
                 eval_common + ["--topic", topic,
                                "--output", str(eval_results / f"{topic}.json"),
                                "--failures", str(eval_results / f"{topic}_failures.json")],
                 300)
        run_step("evaluate_retrieval (_cross)",
                 eval_common + ["--topic", "_cross",
                                "--output", str(eval_results / "_cross.json"),
                                "--failures", str(eval_results / "_cross_failures.json")],
                 300)
        run_step(
            "refresh_retrieval_eval_snapshot",
            ["python", "pipeline/refresh_retrieval_eval_snapshot.py", "--if-installed"],
            900,
        )

        # Deploy via wrangler (Cloudflare Workers with Static Assets) +
        # idempotent gh-pages stub sync. Requires:
        #   CLOUDFLARE_API_TOKEN (or CF_API_TOKEN), CLOUDFLARE_ACCOUNT_ID.
        has_cf_token = bool(
            os.environ.get("CLOUDFLARE_API_TOKEN") or os.environ.get("CF_API_TOKEN")
        )
        has_account_id = bool(os.environ.get("CLOUDFLARE_ACCOUNT_ID"))
        no_deploy = (getattr(args, "no_deploy", False)
                     or bool(os.environ.get("PAPER_CURATION_NO_DEPLOY")))
        if no_deploy:
            log("\n  [prepare_deploy] SKIP: deploy suppressed "
                "(--no-deploy / PAPER_CURATION_NO_DEPLOY)")
        elif has_cf_token and has_account_id:
            log("\n  [prepare_deploy] Cloudflare env vars found, deploying...")
            try:
                result = subprocess.run(
                    ["python", "pipeline/prepare_deploy.py", "--topic", topic, "--push"],
                    cwd=str(PIPELINE_DIR.parent),
                    capture_output=True, text=True, timeout=1800,
                    env={**os.environ, "PYTHONUTF8": "1"},
                )
                if result.returncode == 0:
                    log(f"  [prepare_deploy] OK: wrangler deploy + gh-pages sync done")
                else:
                    log(f"  [prepare_deploy] FAILED (exit {result.returncode})")
                    if result.stderr:
                        log(f"    {result.stderr[:500]}")
                    raise RuntimeError(
                        f"prepare_deploy failed with exit {result.returncode}"
                    )
            except Exception as e:
                log(f"  [prepare_deploy] ERROR: {str(e)[:100]}")
                raise
        else:
            missing = []
            if not has_cf_token:
                missing.append("CLOUDFLARE_API_TOKEN (or CF_API_TOKEN)")
            if not has_account_id:
                missing.append("CLOUDFLARE_ACCOUNT_ID")
            log(f"\n  [prepare_deploy] SKIP: missing env vars — {', '.join(missing)}")

        log("\nPost-processing complete!")


if __name__ == "__main__":
    from _env_guard import force_py312
    force_py312()
    main()
