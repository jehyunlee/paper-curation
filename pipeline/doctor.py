"""
pipeline/doctor.py — 설치 환경 일괄 진단 도구.

신규 사용자가 설치 후 "왜 안 되지"를 5초 만에 알 수 있도록, 파이프라인 실행에
필요한 환경(인터프리터·패키지·Java·config·API 키·Zotero·node·산출물)을 한 번에
점검한다. 각 항목은 ✓(정상) / △(선택·경고) / ✗(필수 실패) 로 표시하고, 실패하면
바로 아래에 한 줄 해결법을 붙인다.

이 도구는 진단이 목적이므로 _env_guard.force_py312() 를 호출하지 않는다 — 잘못된
인터프리터로 실행돼도 그 사실을 보고해야 하기 때문이다. config.json / 네트워크가
깨져 있어도 끝까지 돌 수 있도록 모든 검사를 방어적으로 감싼다.

Usage:
  PYTHONUTF8=1 python pipeline/doctor.py                    # 로컬 환경만 점검
  PYTHONUTF8=1 python pipeline/doctor.py --network          # Zotero API 연결까지
  PYTHONUTF8=1 python pipeline/doctor.py --topic humanoid   # 특정 토픽 산출물까지

종료코드: 필수 항목이 하나라도 ✗ 이면 1, 아니면 0.
"""

import argparse
import importlib
import json
import os
import shutil
import ssl
import subprocess
import sys
import urllib.request
from pathlib import Path

PIPELINE_DIR = Path(__file__).resolve().parent
REPO = PIPELINE_DIR.parent
CONFIG_PATH = REPO / "config.json"
EXAMPLE_PATH = REPO / "config.example.json"
DOCS_DIR = REPO / "docs"
PAPERS_INDEX = DOCS_DIR / "papers" / "_papers_index.json"

# 기업 프록시가 HTTPS 를 self-signed 로 가로채는 환경 대비 (config_loader 와 동일)
_SSL_CTX = ssl.create_default_context()
_SSL_CTX.check_hostname = False
_SSL_CTX.verify_mode = ssl.CERT_NONE


# ---------------------------------------------------------------------------
# 출력 헬퍼
# ---------------------------------------------------------------------------
class Reporter:
    """검사 결과를 ✓/△/✗ 로 출력하고 실패·경고 수를 집계한다."""

    def __init__(self):
        on = sys.stdout.isatty() and os.environ.get("NO_COLOR") is None
        self._g = "\033[32m" if on else ""
        self._y = "\033[33m" if on else ""
        self._r = "\033[31m" if on else ""
        self._b = "\033[1m" if on else ""
        self._dim = "\033[2m" if on else ""
        self._x = "\033[0m" if on else ""
        self.fails = 0   # ✗ (필수 실패) → 종료코드 1
        self.warns = 0   # △ (선택·경고)
        self.oks = 0     # ✓

    def section(self, title):
        print(f"\n{self._b}── {title}{self._x}")

    def ok(self, label, detail=""):
        self.oks += 1
        tail = f" {self._dim}— {detail}{self._x}" if detail else ""
        print(f"  {self._g}✓{self._x} {label}{tail}")

    def warn(self, label, detail="", fix=""):
        self.warns += 1
        tail = f" {self._dim}— {detail}{self._x}" if detail else ""
        print(f"  {self._y}△{self._x} {label}{tail}")
        if fix:
            print(f"      {self._y}→ {fix}{self._x}")

    def fail(self, label, detail="", fix=""):
        self.fails += 1
        tail = f" {self._dim}— {detail}{self._x}" if detail else ""
        print(f"  {self._r}✗{self._x} {label}{tail}")
        if fix:
            print(f"      {self._r}→ {fix}{self._x}")

    def note(self, text):
        print(f"    {self._dim}{text}{self._x}")

    def summary(self):
        print(f"\n{self._b}{'─' * 52}{self._x}")
        print(
            f"요약: {self._g}✓ {self.oks}{self._x}  "
            f"{self._y}△ {self.warns}{self._x}  "
            f"{self._r}✗ {self.fails}{self._x}"
        )
        if self.fails:
            print(
                f"{self._r}{self._b}✗ 필수 항목 {self.fails}개 실패{self._x} — "
                "위 → 해결법을 확인한 뒤 다시 실행하세요."
            )
        elif self.warns:
            print(
                f"{self._g}{self._b}✓ 필수 항목 통과{self._x} — 파이프라인 실행 준비 완료 "
                f"({self._y}△ {self.warns}개는 선택 기능{self._x})."
            )
        else:
            print(f"{self._g}{self._b}✓ 모든 항목 통과 — 완벽합니다.{self._x}")


# ---------------------------------------------------------------------------
# 1. Python 인터프리터 (py312 단독)
# ---------------------------------------------------------------------------
def _find_py312():
    """_env_guard.find_py312() 로 py312 경로를 찾는다 (import 실패 시 None)."""
    try:
        sys.path.insert(0, str(PIPELINE_DIR))
        from _env_guard import find_py312  # type: ignore
        return find_py312()
    except Exception:
        return shutil.which("python3.12")


def check_python(rep):
    rep.section("1. Python 인터프리터 (py312 단독)")
    ver = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    if sys.version_info[:2] == (3, 12):
        rep.ok("Python 3.12", f"{sys.executable} (Python {ver})")
        return
    alt = _find_py312()
    if alt and Path(alt).resolve() != Path(sys.executable).resolve():
        fix = f"py312 로 실행: PYTHONUTF8=1 {alt} pipeline/doctor.py"
    else:
        fix = ("conda create -n py312 -c conda-forge python=3.12 -y && conda activate py312 "
               "(또는 PAPER_CURATION_PY312 로 절대경로 지정)")
    rep.fail("Python 3.12 아님", f"현재 Python {ver} — py314 등 비-3.12 금지", fix)


# ---------------------------------------------------------------------------
# 2. 필수/선택 패키지 import
# ---------------------------------------------------------------------------
# (import 명, pip 패키지명, 용도)
REQUIRED_PKGS = [
    ("anthropic", "anthropic", "legacy Anthropic SDK (OpenRouter 없을 때 폴백)"),
    ("fitz", "pymupdf", "PyMuPDF — PDF 텍스트/figure 추출"),
    ("PIL", "Pillow", "PNG→WebP 변환"),
    ("requests", "requests", "HTTP (검색·다운로드)"),
]
OPTIONAL_PKGS = [
    ("google.genai", "google-genai", "legacy Gemini 폴백 (임베딩·TTS·figure)"),
    ("openai", "openai", "legacy OpenAI / 로컬 OpenAI-compat"),
]
# 재클러스터링(topic_modeling/classify_papers) 전용 — 없으면 리뷰·인덱스·배포는 되고
# 재분류만 불가.
CLUSTER_PKGS = [
    ("umap", "umap-learn"),
    ("hdbscan", "hdbscan"),
    ("sentence_transformers", "sentence-transformers"),
]


def _can_import(mod):
    try:
        importlib.import_module(mod)
        return True, ""
    except Exception as e:
        return False, f"{type(e).__name__}: {e}"


def check_packages(rep):
    rep.section("2. 필수 패키지")
    missing_pip = []
    for mod, pip_name, why in REQUIRED_PKGS:
        ok, err = _can_import(mod)
        if ok:
            rep.ok(mod, why)
        else:
            missing_pip.append(pip_name)
            rep.fail(mod, why, f"pip install {pip_name}")
    if missing_pip:
        rep.note(f"한 번에: pip install {' '.join(dict.fromkeys(missing_pip))}")

    rep.section("2a. 선택 패키지 (legacy 벤더 폴백)")
    for mod, pip_name, why in OPTIONAL_PKGS:
        ok, _err = _can_import(mod)
        if ok:
            rep.ok(mod, why)
        else:
            rep.warn(mod, why, f"pip install {pip_name}")

    rep.section("2b. 재클러스터링 패키지 (선택 — reclassify/topic_modeling 전용)")
    missing_cluster = [pip for mod, pip in CLUSTER_PKGS if not _can_import(mod)[0]]
    if not missing_cluster:
        rep.ok("umap-learn / hdbscan / sentence-transformers", "재클러스터링 가능")
    else:
        rep.warn(
            "클러스터링 스택 일부 없음",
            f"미설치: {', '.join(missing_cluster)} — 리뷰·인덱스·배포는 정상, 재분류만 불가",
            f"pip install {' '.join(missing_cluster)}",
        )


# ---------------------------------------------------------------------------
# 3. Java 런타임 (opendataloader-pdf)
# ---------------------------------------------------------------------------
def check_java(rep):
    rep.section("3. Java 런타임 (opendataloader-pdf)")
    java = shutil.which("java")
    if not java:
        rep.warn(
            "java 없음",
            "opendataloader-pdf 대신 PyMuPDF 로 fallback → 표/구조 추출 품질 저하",
            "brew install --cask temurin  (macOS) / apt install default-jre (Linux)",
        )
        return
    ver = ""
    try:
        out = subprocess.run([java, "-version"], capture_output=True, text=True, timeout=10)
        blob = (out.stderr or out.stdout).strip()
        if blob:
            ver = blob.splitlines()[0]
    except Exception:
        pass
    rep.ok("java", ver or java)


# ---------------------------------------------------------------------------
# 4. config.json (존재 + 필수 필드)
# ---------------------------------------------------------------------------
def _load_config():
    if not CONFIG_PATH.exists():
        return None
    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        return {"__error__": str(e)}


def check_config(rep, cfg):
    rep.section("4. config.json")
    if cfg is None:
        rep.fail(
            "config.json 없음",
            f"{CONFIG_PATH}",
            "PYTHONUTF8=1 python pipeline/setup.py  (또는 config.example.json 복사 후 수정)",
        )
        return
    if isinstance(cfg, dict) and "__error__" in cfg:
        rep.fail("config.json 파싱 실패", cfg["__error__"], "JSON 문법을 확인하세요")
        return
    if not isinstance(cfg, dict):
        rep.fail(
            "config.json 형식 오류",
            f"최상위가 JSON 객체가 아님 ({type(cfg).__name__})",
            'config.json 은 {"zotero": {...}} 형태의 객체여야 합니다',
        )
        return
    rep.ok("config.json 로드", str(CONFIG_PATH))

    zot = cfg.get("zotero", {}) if isinstance(cfg.get("zotero"), dict) else {}

    # zotero.api_key — placeholder 는 미설정 취급
    api_key = str(zot.get("api_key", "")).strip()
    if api_key and api_key != "YOUR_ZOTERO_API_KEY_HERE":
        rep.ok("zotero.api_key", "설정됨")
    elif os.environ.get("ZOTERO_API_KEY", "").strip():
        rep.ok("zotero.api_key", "env ZOTERO_API_KEY 로 대체")
    else:
        rep.fail(
            "zotero.api_key 미설정",
            "Zotero 컬렉션·PDF 가져오기에 필요",
            "https://www.zotero.org/settings/keys 에서 발급 후 config.json 에 기입",
        )

    # zotero.collections — 최소 1개
    cols = zot.get("collections", {}) if isinstance(zot.get("collections"), dict) else {}
    if cols:
        rep.ok("zotero.collections", f"{len(cols)}개 토픽: {', '.join(cols.keys())}")
    else:
        rep.fail(
            "zotero.collections 비어있음",
            "최소 1개 토픽→컬렉션 매핑 필요",
            'config.json 의 zotero.collections 에 {"topic": "Collection Name"} 추가',
        )

    # zotero.pdf_dir — 필드 존재 여부 (실제 디렉토리 점검은 6번에서)
    if str(zot.get("pdf_dir", "")).strip():
        rep.ok("zotero.pdf_dir", str(zot.get("pdf_dir")))
    else:
        rep.fail(
            "zotero.pdf_dir 미설정",
            "PDF 다운로드 저장 경로",
            "config.json 의 zotero.pdf_dir 에 Zotero PDF 저장 경로 지정",
        )

    # unpaywall_email — 선택 (OA 조회 시 예의상 필요)
    if str(cfg.get("unpaywall_email", "")).strip() or str(zot.get("email", "")).strip():
        rep.ok("unpaywall_email", "설정됨")
    else:
        rep.warn(
            "unpaywall_email 미설정",
            "Unpaywall OA PDF 조회에만 사용 (없어도 리뷰는 가능)",
            "config.json 최상위 unpaywall_email 에 이메일 지정",
        )

    return cfg


# ---------------------------------------------------------------------------
# 5. API 키 (env / config.json)
# ---------------------------------------------------------------------------
def _resolve_key(cfg, env_names, cfg_keys):
    """env → config.json 순으로 키를 찾는다. (found_bool, source) 반환. 값은 노출 안 함."""
    for name in env_names:
        if os.environ.get(name, "").strip():
            return True, f"env:{name}"
    if isinstance(cfg, dict):
        for k in cfg_keys:
            if str(cfg.get(k, "")).strip():
                return True, f"config:{k}"
    return False, ""


def check_api_keys(rep, cfg):
    rep.section("5. API 키")

    # OpenRouter — LLM / embed / vision / TTS 단일 키 (1순위)
    or_found = False
    or_src = ""
    if os.environ.get("OPENROUTER_API_KEY", "").strip():
        or_found, or_src = True, "env:OPENROUTER_API_KEY"
    elif isinstance(cfg, dict):
        or_block = cfg.get("openrouter") if isinstance(cfg.get("openrouter"), dict) else {}
        if str(or_block.get("api_key", "")).strip() and str(or_block.get("api_key")).strip() != "YOUR_OPENROUTER_API_KEY_HERE":
            or_found, or_src = True, "config:openrouter.api_key"
        elif str(cfg.get("openrouter_api_key", "")).strip():
            or_found, or_src = True, "config:openrouter_api_key"
    if or_found:
        rep.ok("OPENROUTER_API_KEY", f"설정됨 ({or_src}) — LLM·임베딩·비전·TTS")
    else:
        rep.fail(
            "OPENROUTER_API_KEY 미설정",
            "리뷰·임베딩·figure vision·TTS 에 권장되는 단일 키",
            "export OPENROUTER_API_KEY=sk-or-v1-...  (https://openrouter.ai/keys)",
        )

    # Hermes — 다이어그램/타임라인 이미지 전용
    hermes_base = os.environ.get("HERMES_GATEWAY_BASE_URL", "").strip()
    hermes_key = os.environ.get("HERMES_GATEWAY_API_KEY", "").strip()
    if isinstance(cfg, dict) and isinstance(cfg.get("hermes"), dict):
        hermes_base = hermes_base or str(cfg["hermes"].get("base_url", "")).strip()
        hermes_key = hermes_key or str(cfg["hermes"].get("api_key", "")).strip()
    if hermes_base and hermes_key and hermes_key != "YOUR_HERMES_GATEWAY_API_KEY_HERE":
        # Optional live probe
        try:
            models_url = hermes_base.rstrip("/") + "/models"
            req = urllib.request.Request(
                models_url,
                headers={"Authorization": f"Bearer {hermes_key}",
                         "User-Agent": "paper-curation-doctor"},
            )
            with urllib.request.urlopen(req, timeout=5, context=_SSL_CTX) as resp:
                _ = resp.read(200)
            rep.ok("HERMES_GATEWAY", f"{hermes_base} — 이미지 생성 (probe OK)")
        except Exception as e:
            rep.warn(
                "HERMES_GATEWAY 연결 실패",
                f"{hermes_base}: {type(e).__name__}",
                "hermes-tunnel.service / sns_for_paper .env 확인 — 다운 시 다이어그램만 skip",
            )
    else:
        rep.warn(
            "HERMES_GATEWAY 미설정 (선택)",
            "타임라인/워크플로 다이어그램 이미지 — 미설정 시 PaperBanana 폴백",
            "export HERMES_GATEWAY_BASE_URL=http://localhost:8642/v1 "
            "HERMES_GATEWAY_API_KEY=... HERMES_GATEWAY_MODEL=hermes-agent",
        )

    # Legacy vendor keys (fallback only)
    found, src = _resolve_key(cfg, ["ANTHROPIC_API_KEY"], ["anthropic_api_key"])
    if found:
        rep.ok("ANTHROPIC_API_KEY", f"설정됨 ({src}) — OpenRouter 없을 때 legacy 폴백")
    else:
        rep.warn(
            "ANTHROPIC_API_KEY 미설정 (legacy)",
            "OPENROUTER_API_KEY 가 있으면 불필요",
        )

    found, src = _resolve_key(
        cfg, ["GOOGLE_API_KEY", "GEMINI_API_KEY"], ["google_api_key", "gemini_api_key"]
    )
    if found:
        rep.ok("GOOGLE_API_KEY", f"설정됨 ({src}) — OpenRouter 없을 때 legacy 폴백")
    else:
        rep.warn(
            "GOOGLE_API_KEY 미설정 (legacy)",
            "OPENROUTER_API_KEY 가 있으면 불필요",
        )

    found, src = _resolve_key(cfg, ["OPENAI_API_KEY"], ["openai_api_key"])
    if found:
        rep.ok("OPENAI_API_KEY", f"설정됨 ({src}) — legacy fallback")
    else:
        rep.warn(
            "OPENAI_API_KEY 미설정 (선택)",
            "OpenRouter 단일 키로 대체됨",
        )

    found, src = _resolve_key(cfg, ["CLOUDFLARE_API_TOKEN", "CF_API_TOKEN"], [])
    if found:
        rep.ok("CLOUDFLARE_API_TOKEN", f"설정됨 ({src}) — Cloudflare Workers 배포")
    else:
        rep.warn(
            "CLOUDFLARE_API_TOKEN 미설정 (선택)",
            "wrangler deploy (Cloudflare) 에만 필요 — 로컬 운영은 불필요",
        )

    found, src = _resolve_key(cfg, ["CLOUDFLARE_ACCOUNT_ID"], [])
    if found:
        rep.ok("CLOUDFLARE_ACCOUNT_ID", f"설정됨 ({src}) — Cloudflare 계정 식별")
    else:
        rep.warn(
            "CLOUDFLARE_ACCOUNT_ID 미설정 (선택)",
            "Cloudflare 배포 시에만 필요",
        )


# ---------------------------------------------------------------------------
# 6. Zotero (pdf_dir 존재 + --network 시 API 연결)
# ---------------------------------------------------------------------------
def check_zotero(rep, cfg, do_network):
    rep.section("6. Zotero")
    zot = cfg.get("zotero", {}) if isinstance(cfg, dict) and isinstance(cfg.get("zotero"), dict) else {}
    pdf_dir = str(zot.get("pdf_dir", "")).strip() or os.environ.get("ZOTERO_DIR", "").strip()

    if not pdf_dir:
        rep.fail("Zotero PDF 경로 미설정", "", "config.json 의 zotero.pdf_dir 지정")
    elif Path(pdf_dir).is_dir():
        try:
            n_pdf = sum(1 for _ in Path(pdf_dir).glob("*.pdf"))
            rep.ok("Zotero PDF 디렉토리", f"{pdf_dir} (PDF {n_pdf}개)")
        except Exception:
            rep.ok("Zotero PDF 디렉토리", pdf_dir)
    else:
        rep.warn(
            "Zotero PDF 디렉토리 없음",
            pdf_dir,
            f"mkdir -p '{pdf_dir}'  (Zotero 'Linked Attachment Base Directory' 와 일치시킬 것)",
        )

    if not do_network:
        rep.note("Zotero API 연결 테스트는 생략됨 (--network 로 활성화)")
        return

    api_key = (str(zot.get("api_key", "")).strip() or os.environ.get("ZOTERO_API_KEY", "").strip())
    if not api_key or api_key == "YOUR_ZOTERO_API_KEY_HERE":
        rep.fail("Zotero API 연결 불가", "API key 미설정", "config.json 의 zotero.api_key 지정")
        return

    # User ID 조회
    try:
        req = urllib.request.Request(
            "https://api.zotero.org/keys/current",
            headers={"Zotero-API-Key": api_key, "User-Agent": "Mozilla/5.0"},
        )
        with urllib.request.urlopen(req, timeout=15, context=_SSL_CTX) as resp:
            data = json.load(resp)
        user_id = str(data.get("userID", ""))
        rep.ok("Zotero User ID", user_id)
    except Exception as e:
        rep.fail("Zotero User ID 조회 실패", str(e), "API key/네트워크 확인")
        return

    # 컬렉션 검증
    cols = zot.get("collections", {}) if isinstance(zot.get("collections"), dict) else {}
    if not cols:
        rep.warn("컬렉션 미설정", "config.json 의 zotero.collections 비어있음")
        return
    try:
        req = urllib.request.Request(
            f"https://api.zotero.org/users/{user_id}/collections?format=json&limit=100",
            headers={"Zotero-API-Key": api_key, "User-Agent": "Mozilla/5.0"},
        )
        with urllib.request.urlopen(req, timeout=15, context=_SSL_CTX) as resp:
            fetched = json.load(resp)
        name_to_key = {c["data"]["name"]: c["data"]["key"] for c in fetched}
    except Exception as e:
        rep.fail("Zotero 컬렉션 목록 조회 실패", str(e), "네트워크 확인")
        return

    available = sorted(name_to_key.keys())
    for alias, name in cols.items():
        # name 이 이미 8자 대문자 key 형태면 그대로 인정
        is_key = len(str(name)) == 8 and str(name).isalnum() and not any(c.islower() for c in str(name))
        if name in name_to_key:
            rep.ok(f"컬렉션 '{alias}'", f"'{name}' → {name_to_key[name]}")
        elif is_key and name in name_to_key.values():
            rep.ok(f"컬렉션 '{alias}'", f"key {name}")
        else:
            rep.fail(
                f"컬렉션 '{alias}' 없음",
                f"'{name}' 을 Zotero 에서 찾을 수 없음",
                f"사용 가능: {', '.join(available) if available else '(없음)'}",
            )


# ---------------------------------------------------------------------------
# 7. node / npx (wrangler 배포용, 선택)
# ---------------------------------------------------------------------------
def check_node(rep):
    rep.section("7. node / npx (Cloudflare 배포용, 선택)")
    node = shutil.which("node")
    npx = shutil.which("npx")
    if node and npx:
        ver = ""
        try:
            out = subprocess.run([node, "--version"], capture_output=True, text=True, timeout=10)
            ver = out.stdout.strip()
        except Exception:
            pass
        rep.ok("node / npx", f"node {ver} — wrangler deploy 가능")
    else:
        rep.warn(
            "node/npx 없음",
            "wrangler deploy (Cloudflare 배포) 에만 필요 — 로컬 운영은 불필요",
            "https://nodejs.org 또는 fnm/nvm 으로 Node.js 설치",
        )


# ---------------------------------------------------------------------------
# 8. papers index
# ---------------------------------------------------------------------------
def _load_papers_index():
    try:
        with open(PAPERS_INDEX, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


def check_papers_index(rep, papers):
    rep.section("8. 마스터 논문 인덱스")
    if not PAPERS_INDEX.exists():
        rep.warn(
            "_papers_index.json 없음",
            str(PAPERS_INDEX),
            "첫 파이프라인 실행(run_full.py) 후 자동 생성됩니다",
        )
        return
    if papers is None:
        rep.fail("_papers_index.json 파싱 실패", str(PAPERS_INDEX), "JSON 손상 여부 확인")
        return
    n = len(papers) if isinstance(papers, list) else 0
    rep.ok("_papers_index.json", f"{n}개 논문")


# ---------------------------------------------------------------------------
# 9. --topic 산출물
# ---------------------------------------------------------------------------
# (파일명, 필수여부, 설명)
TOPIC_ARTIFACTS = [
    ("index.html", True, "토픽 카드 인덱스"),
    ("_new_classification.json", True, "카테고리 분류"),
    ("_search_index.json", False, "Deep Research RAG 인덱스"),
    ("network.html", False, "D3 네트워크 시각화"),
]


def check_topic(rep, topic, cfg, papers):
    rep.section(f"9. 토픽 산출물: {topic}")
    tdir = DOCS_DIR / topic

    # config 에 등록된 토픽인지 (정보성)
    cols = {}
    if isinstance(cfg, dict) and isinstance(cfg.get("zotero"), dict):
        cols = cfg["zotero"].get("collections", {}) or {}
    if topic in cols:
        rep.ok(f"'{topic}' config 등록됨", f"컬렉션 매핑 존재")
    else:
        rep.warn(
            f"'{topic}' config 미등록",
            f"zotero.collections 에 없음 (등록된 토픽: {', '.join(cols.keys()) or '없음'})",
        )

    if not tdir.is_dir():
        rep.fail(
            f"docs/{topic}/ 없음",
            str(tdir),
            f"PYTHONUTF8=1 python pipeline/run_full.py --topic {topic} --mode curate --source zotero",
        )
        return

    for fname, required, desc in TOPIC_ARTIFACTS:
        fpath = tdir / fname
        if fpath.exists():
            rep.ok(f"{topic}/{fname}", desc)
        elif required:
            rep.fail(
                f"{topic}/{fname} 없음",
                desc,
                f"PYTHONUTF8=1 python pipeline/build_topic_index.py {topic}",
            )
        else:
            rep.warn(f"{topic}/{fname} 없음", f"{desc} (선택)")

    # 인덱스에서 이 토픽 논문 수 교차 확인 (정보성)
    if isinstance(papers, list):
        n_topic = sum(1 for p in papers if isinstance(p, dict) and topic in (p.get("topics") or []))
        rep.note(f"_papers_index.json 에서 topics 에 '{topic}' 포함: {n_topic}개")


# ---------------------------------------------------------------------------
# 10. Git 가드레일 (pre-push 훅 · 백업)
# ---------------------------------------------------------------------------
def _git_hooks_dir():
    """core.hooksPath / worktree 를 고려한 실제 훅 디렉토리."""
    try:
        out = subprocess.run(
            ["git", "-C", str(REPO), "rev-parse", "--git-path", "hooks"],
            capture_output=True, text=True, timeout=5)
        if out.returncode == 0 and out.stdout.strip():
            p = Path(out.stdout.strip())
            return p if p.is_absolute() else (REPO / p)
    except Exception:
        pass
    return REPO / ".git" / "hooks"


def check_guardrails(rep):
    rep.section("10. 가드레일 (Git · 에이전트 · 백업)")

    src = REPO / "scripts" / "pre-push"
    installed = _git_hooks_dir() / "pre-push"
    fix = "bash scripts/install-hooks.sh"

    if not src.exists():
        rep.warn("scripts/pre-push 없음", "훅 소스가 저장소에 없음")
    elif not installed.exists():
        rep.fail("pre-push 훅 미설치",
                 "시크릿 유출 스캔이 실행된 적 없음 (.git/hooks 에 pre-push 없음)", fix)
    elif installed.read_bytes() != src.read_bytes():
        rep.warn("pre-push 훅 구버전",
                 "scripts/pre-push 와 설치본이 다름 — 재설치 필요", fix)
    elif not os.access(installed, os.X_OK):
        rep.warn("pre-push 훅 비실행", "chmod +x 필요", fix)
    else:
        rep.ok("pre-push 훅 활성", "시크릿 스캔 차단 + validate 권고")

    scanner = REPO / "scripts" / "scan-secrets.py"
    if scanner.exists():
        rep.ok("raw-object 시크릿 스캐너", "commit · tag · binary blob 검사")
    else:
        rep.fail("시크릿 스캐너 없음", "scripts/scan-secrets.py 누락")

    # Agent layer: source-controlled guard must match its installed global copy,
    # settings must wire PreToolUse + deny and must not bypass dangerous prompts.
    guard_src = REPO / "scripts" / "claude_guard.py"
    guard_dst = Path.home() / ".claude" / "hooks" / "guard.py"
    settings_path = Path.home() / ".claude" / "settings.json"
    agent_fix = "python3 scripts/install-agent-guard.py"
    if not guard_src.exists():
        rep.fail("에이전트 가드 소스 없음", "scripts/claude_guard.py 누락")
    elif not guard_dst.exists():
        rep.fail("에이전트 PreToolUse 가드 미설치", str(guard_dst), agent_fix)
    elif guard_dst.read_bytes() != guard_src.read_bytes():
        rep.fail("에이전트 가드 구버전/변조",
                 "설치본이 저장소 소스와 다름", agent_fix)
    else:
        rep.ok("에이전트 PreToolUse 가드 활성", "설치본 == 버전관리 소스")

    try:
        settings = json.loads(settings_path.read_text(encoding="utf-8"))
    except Exception as exc:
        rep.fail("Claude settings 읽기 실패", str(exc), agent_fix)
    else:
        deny = settings.get("permissions", {}).get("deny", [])
        pre = settings.get("hooks", {}).get("PreToolUse", [])
        wired = any("guard.py" in json.dumps(x) for x in pre)
        if settings.get("skipDangerousModePermissionPrompt") is True:
            rep.fail("dangerous-mode 프롬프트 스킵 활성",
                     "skipDangerousModePermissionPrompt=true", agent_fix)
        elif not deny or not wired:
            rep.fail("Claude deny/PreToolUse 미배선",
                     f"deny={len(deny)} · PreToolUse guard={wired}", agent_fix)
        else:
            rep.ok("Claude 권한 정책 활성",
                   f"deny {len(deny)}건 · dangerous-mode 스킵 없음")

    broken_agents = []
    agents_dir = Path.home() / ".claude" / "agents"
    if agents_dir.exists():
        broken_agents = [p for p in agents_dir.iterdir()
                         if p.is_symlink() and not p.exists()]
    if broken_agents:
        rep.warn("에이전트 심링크 단절",
                 f"{len(broken_agents)}개가 존재하지 않는 경로를 가리킴",
                 "끊어진 링크를 삭제하거나 현재 agent 소스로 다시 연결")
    else:
        rep.ok("에이전트 심링크 정상")

    # 백업 대상 (macOS Time Machine) — git 밖 로컬 산출물 보호
    if sys.platform == "darwin":
        try:
            tm = subprocess.run(["tmutil", "destinationinfo"],
                                capture_output=True, text=True, timeout=5)
            if tm.returncode != 0 or "No destinations" in (tm.stdout + tm.stderr):
                rep.warn(
                    "Time Machine 대상 없음",
                    "git 밖 로컬 산출물(docs/papers · _agent · _local_keys 등) 미백업",
                    "시스템 설정 → Time Machine 에서 백업 디스크 지정")
            else:
                rep.ok("Time Machine 대상 구성됨")
        except FileNotFoundError:
            pass
        except Exception:
            pass


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="paper-curation 설치 환경 일괄 진단 (✓/△/✗)"
    )
    parser.add_argument("--network", action="store_true",
                        help="Zotero API 연결까지 테스트 (네트워크 필요)")
    parser.add_argument("--topic", default="",
                        help="해당 토픽의 산출물 존재 여부까지 점검 (예: humanoid)")
    args = parser.parse_args()

    print("=" * 52)
    print("  Paper Curation — Doctor (환경 진단)")
    print("=" * 52)

    rep = Reporter()
    cfg = _load_config()
    papers = _load_papers_index()

    check_python(rep)
    check_packages(rep)
    check_java(rep)
    check_config(rep, cfg)
    check_api_keys(rep, cfg)
    check_zotero(rep, cfg, args.network)
    check_node(rep)
    check_papers_index(rep, papers)
    if args.topic:
        check_topic(rep, args.topic, cfg, papers)
    check_guardrails(rep)

    rep.summary()
    sys.exit(1 if rep.fails else 0)


if __name__ == "__main__":
    main()
