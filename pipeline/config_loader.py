"""
config.json 로더 + Zotero User ID / Collection Key 자동 조회.

모든 스크립트가 이 모듈을 통해 설정을 읽는다.
config.json이 없으면 환경변수 폴백.

Collection은 이름(예: "AI assisted Research")으로 지정하면
Zotero API로 collection key를 자동 조회한다.
"""

import json
import os
import ssl
import urllib.request
from pathlib import Path

# Corporate proxy intercepts HTTPS with self-signed cert; skip verification
_ssl_ctx = ssl.create_default_context()
_ssl_ctx.check_hostname = False
_ssl_ctx.verify_mode = ssl.CERT_NONE

PIPELINE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = PIPELINE_DIR.parent
CONFIG_PATH = PROJECT_ROOT / "config.json"

# 배포 파일 경로 (GitHub Pages 서빙 루트)
DOCS_DIR = PROJECT_ROOT / "docs"
PAPERS_DIR = DOCS_DIR / "papers"

# 타임라인/워크플로우 이미지 출력
IMG_TIMELINES_DIR = PIPELINE_DIR / "_img_timelines"
IMG_WORKFLOWS_DIR = PIPELINE_DIR / "_img_workflows"

REPO = PROJECT_ROOT  # backward compat alias

_config_cache = None
_user_id_cache = None
_collection_key_cache = None


def load_config():
    """config.json 로드. 없으면 환경변수 폴백."""
    global _config_cache
    if _config_cache is not None:
        return _config_cache

    if CONFIG_PATH.exists():
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            _config_cache = json.load(f)
    else:
        _config_cache = {
            "zotero": {
                "api_key": os.environ.get("ZOTERO_API_KEY", ""),
                "email": os.environ.get("UNPAYWALL_EMAIL", ""),
                "collections": {},
            },
            "unpaywall_email": os.environ.get("UNPAYWALL_EMAIL", ""),
        }

    return _config_cache


def get_zotero_api_key():
    cfg = load_config()
    return cfg.get("zotero", {}).get("api_key", "") or os.environ.get("ZOTERO_API_KEY", "")


def get_google_key():
    """Google(Gemini) API 키. env(GOOGLE_API_KEY/GEMINI_API_KEY) 우선, 없으면
    config.json(gemini_api_key/google_api_key). figure 검증·TTS·임베딩 공용 해석기.

    참고: figure 검증처럼 'env 키 유무'를 Gemini on/off 스위치로 쓰던 호출부는
    이 함수가 config.json 까지 보므로 env 를 pop 해도 키가 남는다. 그런 곳은
    PAPER_CURATION_NO_GEMINI 환경 플래그로 명시 비활성화한다
    (reextract_figures.py 의 geometric-only 모드 참조)."""
    cfg = load_config()
    return (os.environ.get("GOOGLE_API_KEY")
            or os.environ.get("GEMINI_API_KEY")
            or cfg.get("gemini_api_key", "")
            or cfg.get("google_api_key", "")) or ""


def get_local_model_config():
    """로컬 LLM fallback (Ollama / LM Studio / llama.cpp / vLLM) 설정.

    OpenAI 호환 엔드포인트 한 개를 가정한다. 환경변수가 config.json 보다 우선.
    base_url 과 model 이 둘 다 있어야 유효하고, 그렇지 않으면 None 을 반환해
    호출자가 "로컬 fallback 미설정" 으로 조용히 건너뛰게 한다.

    config.json 예시::

        "local_model": {
          "base_url": "http://localhost:11434/v1",
          "model": "qwen2.5:7b-instruct",
          "api_key": "ollama",      # 로컬 서버는 대개 무시하지만 SDK 가 비어있으면 거부
          "batch_size": 8,          # (선택) 로컬 연결 배치 크기
          "timeout": 300            # (선택) per-call 초
        }
    """
    cfg = load_config().get("local_model", {}) or {}
    base_url = os.environ.get("LOCAL_MODEL_BASE_URL") or cfg.get("base_url")
    model = os.environ.get("LOCAL_MODEL_NAME") or cfg.get("model")
    if not base_url or not model:
        return None
    out = {
        "base_url": base_url,
        "model": model,
        "api_key": os.environ.get("LOCAL_MODEL_API_KEY") or cfg.get("api_key") or "local",
    }
    if cfg.get("batch_size"):
        out["batch_size"] = int(cfg["batch_size"])
    if cfg.get("timeout"):
        out["timeout"] = float(cfg["timeout"])
    if cfg.get("reasoning_effort"):
        # thinking 모델(EXAONE-4.5 등): "none" 이면 think OFF — 없으면 content 가
        # 빈 채 thinking 채널만 채우는 모델이 있다 (lib/local_llm.chat_json 참조)
        out["reasoning_effort"] = str(cfg["reasoning_effort"])
    if cfg.get("json_mode"):
        # response_format json_object — 서버 문법 제약으로 JSON 유효성 보장
        out["json_mode"] = True
    if cfg.get("num_ctx"):
        # Ollama 네이티브 경로 전용: 요청 단위 컨텍스트(기본 8192). 신형 Ollama 가
        # 모델 최대치(128K+)로 로드해 느려지는 것을 요청 단위로 줄인다.
        out["num_ctx"] = int(cfg["num_ctx"])
    if cfg.get("retries"):
        # 형식 깨짐은 확률적이라 배치당 재시도 횟수(기본 2)
        out["retries"] = int(cfg["retries"])
    return out


def get_zotero_user_id():
    """Zotero API Key로 User ID를 자동 조회. 캐싱."""
    global _user_id_cache
    if _user_id_cache is not None:
        return _user_id_cache

    env_id = os.environ.get("ZOTERO_USER_ID", "")
    if env_id:
        _user_id_cache = env_id
        return env_id

    api_key = get_zotero_api_key()
    if not api_key:
        raise ValueError("Zotero API key not found. Set config.json or ZOTERO_API_KEY env var.")

    try:
        url = "https://api.zotero.org/keys/current"
        req = urllib.request.Request(url, headers={
            "Zotero-API-Key": api_key, "User-Agent": "Mozilla/5.0",
        })
        with urllib.request.urlopen(req, timeout=15, context=_ssl_ctx) as resp:
            data = json.load(resp)
        _user_id_cache = str(data.get("userID", ""))
        return _user_id_cache
    except Exception as e:
        raise ValueError(f"Failed to fetch Zotero User ID: {e}")


def _fetch_collection_keys():
    """Zotero에서 collection name → key 매핑을 조회. 캐싱."""
    global _collection_key_cache
    if _collection_key_cache is not None:
        return _collection_key_cache

    api_key = get_zotero_api_key()
    user_id = get_zotero_user_id()

    try:
        url = f"https://api.zotero.org/users/{user_id}/collections?format=json&limit=100"
        req = urllib.request.Request(url, headers={
            "Zotero-API-Key": api_key, "User-Agent": "Mozilla/5.0",
        })
        with urllib.request.urlopen(req, timeout=15, context=_ssl_ctx) as resp:
            cols = json.load(resp)
        _collection_key_cache = {c["data"]["name"]: c["data"]["key"] for c in cols}
        return _collection_key_cache
    except Exception as e:
        print(f"WARNING: Failed to fetch Zotero collections: {e}")
        _collection_key_cache = {}
        return _collection_key_cache


def _resolve_collection_value(value):
    """Collection value가 이름이면 key로 변환, 이미 key면 그대로.

    Zotero collection key는 8자 대문자 영숫자 (예: WKEZLEE8).
    "Humanoid"처럼 8자이면서 알파벳이 섞인 이름과 구분하기 위해
    먼저 이름으로 조회한다.
    """
    if not value:
        return ""
    # 이름으로 먼저 조회 (API 캐시)
    name_to_key = _fetch_collection_keys()
    if value in name_to_key:
        return name_to_key[value]
    # Zotero key 패턴: 8자 + 대문자/숫자만 (소문자 불가)
    if len(value) == 8 and value.isalnum() and not any(c.islower() for c in value):
        return value
    print(f"WARNING: Collection '{value}' not found in Zotero.")
    return value


def get_collections():
    """topic → collection key dict 반환. 이름은 자동으로 key로 변환."""
    cfg = load_config()
    raw = cfg.get("zotero", {}).get("collections", {})
    return {topic: _resolve_collection_value(val) for topic, val in raw.items()}


def get_collection_key(topic):
    return get_collections().get(topic, "")


def get_unpaywall_email():
    cfg = load_config()
    return cfg.get("unpaywall_email", "") or cfg.get("zotero", {}).get("email", "")


# ---------------------------------------------------------------------------
# 검색 키워드 (Core-1 search)
# ---------------------------------------------------------------------------
# config.json 최상위 "search_keywords".<topic> 가 우선. 없으면 아래 빌트인
# 기본값으로 폴백한다 (ai4s/scisci 는 설정 없이도 동작). 새 토픽은 config.json 에
# 블록을 추가하면 되고, 누락 시 get_search_keywords() 가 추가할 JSON 을 안내한다.

_DEFAULT_SEARCH_KEYWORDS = {
    "ai4s": {
        "primary": [
            "AI for science",
            "machine learning science",
            "scientific discovery AI",
            "neural network physics",
            "deep learning chemistry",
            "AI drug discovery",
            "scientific foundation model",
            "AI materials",
        ],
        "secondary": [
            "molecular dynamics",
            "protein structure",
            "weather prediction",
            "quantum chemistry",
            "scientific NLP",
            "research automation",
        ],
    },
    "scisci": {
        "primary": [
            "science of science",
            "bibliometrics",
            "scientometrics",
            "research evaluation",
            "citation analysis",
            "scientific collaboration",
        ],
        "secondary": [
            "h-index",
            "research impact",
            "academic careers",
            "peer review",
            "research funding",
            "open access",
            "reproducibility",
            "research trend",
            "international collaboration",
            "science mapping",
        ],
    },
}


def get_search_keywords(topic):
    """topic → {"primary": [...], "secondary": [...]} 검색 키워드 dict 반환.

    우선순위:
      1) config.json 최상위 "search_keywords".<topic>
      2) 빌트인 기본값 (_DEFAULT_SEARCH_KEYWORDS — ai4s/scisci)

    둘 다 없으면 config.json 에 그대로 붙여넣을 수 있는 JSON 블록을 담은
    ValueError 를 던진다.
    """
    cfg = load_config()
    configured = cfg.get("search_keywords", {}) or {}
    if topic in configured:
        return configured[topic]
    if topic in _DEFAULT_SEARCH_KEYWORDS:
        return _DEFAULT_SEARCH_KEYWORDS[topic]

    example_block = json.dumps(
        {
            "search_keywords": {
                topic: {
                    "primary": [
                        f"{topic} 핵심 키워드 1",
                        f"{topic} 핵심 키워드 2",
                        f"{topic} 핵심 키워드 3",
                    ],
                    "secondary": [
                        f"{topic} 보조 키워드 1",
                        f"{topic} 보조 키워드 2",
                    ],
                }
            }
        },
        ensure_ascii=False,
        indent=2,
    )
    raise ValueError(
        f"'{topic}' 토픽의 검색 키워드(search_keywords)가 정의되지 않았습니다.\n"
        f"config.json 최상위에 아래 \"search_keywords\" 블록을 추가하세요.\n"
        f"  - primary: 관련성 가중치가 높은 핵심 키워드 (제목/초록 매칭 0.5점)\n"
        f"  - secondary: 보조 키워드 (매칭 0.2점)\n\n"
        f"{example_block}"
    )


def get_paperbanana_dir():
    cfg = load_config()
    return cfg.get("paperbanana_dir", "") or os.environ.get("PAPERBANANA_DIR", "")


def get_openrouter_config():
    """OpenRouter (LLM / embed / vision / TTS) 설정.

    env 가 config.json 보다 우선. api_key 없으면 None (호출부가 legacy
    Anthropic/Google/OpenAI 로 폴백).

    config.json 예시::

        "openrouter": {
          "api_key": "sk-or-v1-...",
          "base_url": "https://openrouter.ai/api/v1",
          "models": {
            "haiku": "anthropic/claude-haiku-4.5",
            "sonnet": "anthropic/claude-sonnet-5",
            "opus": "anthropic/claude-opus-5",
            "embed": "qwen/qwen3-embedding-8b",
            "vision": "google/gemini-2.5-flash",
            "tts": "openai/gpt-4o-mini-tts"
          },
          "embed_dimensions": 768
        }
    """
    cfg = load_config().get("openrouter", {}) or {}
    api_key = (os.environ.get("OPENROUTER_API_KEY")
               or cfg.get("api_key") or "").strip()
    if not api_key:
        return None
    models = dict(cfg.get("models") or {})
    # Per-role env overrides (OPENROUTER_MODEL_HAIKU etc.)
    for role, env_name in (
        ("haiku", "OPENROUTER_MODEL_HAIKU"),
        ("sonnet", "OPENROUTER_MODEL_SONNET"),
        ("opus", "OPENROUTER_MODEL_OPUS"),
        ("embed", "OPENROUTER_MODEL_EMBED"),
        ("vision", "OPENROUTER_MODEL_VISION"),
        ("tts", "OPENROUTER_MODEL_TTS"),
    ):
        v = os.environ.get(env_name, "").strip()
        if v:
            models[role] = v
    # Sensible defaults when a role is unset
    models.setdefault("haiku", "anthropic/claude-haiku-4.5")
    models.setdefault("sonnet", "anthropic/claude-sonnet-5")
    models.setdefault("opus", "anthropic/claude-opus-5")
    models.setdefault("embed", "qwen/qwen3-embedding-8b")
    models.setdefault("vision", "google/gemini-2.5-flash")
    models.setdefault("tts", "openai/gpt-4o-mini-tts")
    dim_raw = (os.environ.get("OPENROUTER_EMBED_DIMENSIONS")
               or cfg.get("embed_dimensions") or 768)
    try:
        embed_dimensions = int(dim_raw)
    except (TypeError, ValueError):
        embed_dimensions = 768
    return {
        "api_key": api_key,
        "base_url": (os.environ.get("OPENROUTER_BASE_URL")
                     or cfg.get("base_url")
                     or "https://openrouter.ai/api/v1").rstrip("/"),
        "models": models,
        "embed_dimensions": embed_dimensions,
        "http_referer": (os.environ.get("OPENROUTER_HTTP_REFERER")
                         or cfg.get("http_referer") or ""),
        "app_title": (os.environ.get("OPENROUTER_APP_TITLE")
                      or cfg.get("app_title") or "paper-curation"),
    }


def get_hermes_config():
    """Hermes gateway (다이어그램/타임라인 이미지 전용) 설정.

    sns_for_paper 터널과 동일 키를 재사용한다. base_url+api_key 없으면 None
    → PaperBanana 폴백.

    config.json 예시::

        "hermes": {
          "base_url": "http://localhost:8642/v1",
          "api_key": "...",
          "model": "hermes-agent"
        }
    """
    cfg = load_config().get("hermes", {}) or {}
    base_url = (os.environ.get("HERMES_GATEWAY_BASE_URL")
                or cfg.get("base_url") or "").strip().rstrip("/")
    api_key = (os.environ.get("HERMES_GATEWAY_API_KEY")
               or cfg.get("api_key") or "").strip()
    if not base_url or not api_key:
        return None
    return {
        "base_url": base_url,
        "api_key": api_key,
        "model": (os.environ.get("HERMES_GATEWAY_MODEL")
                  or cfg.get("model") or "hermes-agent"),
        "timeout": float(os.environ.get("HERMES_GATEWAY_TIMEOUT")
                         or cfg.get("timeout") or 300),
    }


def get_zotero_dir():
    """Zotero PDF 저장 디렉토리."""
    cfg = load_config()
    return (cfg.get("zotero", {}).get("pdf_dir", "")
            or os.environ.get("ZOTERO_DIR", ""))


def get_github_repo():
    """GitHub repo (owner/repo 형식)."""
    cfg = load_config()
    return (cfg.get("github", {}).get("repo", "")
            or os.environ.get("GITHUB_REPO", ""))


def get_github_branch():
    """GitHub branch (기본 master)."""
    cfg = load_config()
    return (cfg.get("github", {}).get("branch", "")
            or os.environ.get("GITHUB_BRANCH", "master"))


def get_pages_base_url():
    """GitHub Pages base URL."""
    cfg = load_config()
    return (cfg.get("github", {}).get("pages_base_url", "")
            or os.environ.get("PAGES_BASE_URL", ""))


def get_topic_dir(topic: str) -> Path:
    """docs/{topic} 경로 반환."""
    return DOCS_DIR / topic


def get_papers_index_path() -> Path:
    """papers/_papers_index.json 경로 반환."""
    return PAPERS_DIR / "_papers_index.json"

# ---------------------------------------------------------------------------
# Gemini usage instrumentation (dashboard 종량제 그래프)
# ---------------------------------------------------------------------------
# Every pipeline entry point imports config_loader, and so does the PaperBanana
# wrapper (lib/paperbanana.py) before it runs PaperBanana's agents in-process.
# Installing the google-genai monkey-patch here guarantees that *all* Gemini
# calls report token usage to PC_USAGE_ENDPOINT — the pipeline's own
# generate_content/TTS *and* PaperBanana's image + agent calls, which build
# their own genai.Client and never call usage_log directly. Failure-swallowing;
# never fatal to config loading.
try:
    import usage_log as _usage_log

    _usage_log.instrument_genai()
except Exception:
    pass
