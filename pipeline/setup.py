"""
paper-curation 로컬 설치 스크립트.

기본 설치에는 API 키가 필요하지 않으며 외부 서비스에 연결하거나 파이프라인을
실행하지 않는다. 선택 기능의 로컬 실행 준비 상태, 자격증명 또는 연결 상태는
사용자가 명시적으로 ``--check-feature`` 를 지정했을 때만 진단한다.

Usage:
  python pipeline/setup.py
  python pipeline/setup.py --no-install
  python pipeline/setup.py --check-feature review
  python pipeline/setup.py --check-feature keyword-search
  python pipeline/setup.py --check-feature zotero-sync
  python pipeline/setup.py --check-feature review --check-feature semantic-search
"""

import argparse
import json
import os
import sys
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CONFIG_PATH = REPO / "config.json"
TEMPLATE_PATH = REPO / "SKILL.md.template"
SKILL_OUTPUT = REPO / "SKILL.md"
SKILL_INSTALL_DIR = Path.home() / ".claude" / "skills" / "paper-curation"
LOCAL_PAPERS_DIR = REPO / "docs" / "papers"
BUILD_SEARCH_INDEX_PATH = REPO / "pipeline" / "build_search_index.py"
QUERY_SEARCH_INDEX_PATH = REPO / "pipeline" / "query_search_index.py"
FEATURES_PATH = REPO / "pipeline" / "features.json"


def _feature_registry():
    """Load the shared capability registry without importing a provider."""
    with open(FEATURES_PATH, encoding="utf-8") as feature_file:
        data = json.load(feature_file)
    return {feature["id"]: feature for feature in data["features"]}


FEATURE_CHOICES = tuple(_feature_registry())



def _cfg_unset(cfg, path):
    """중첩된 config 값을 제거하고 실제 변경 여부를 반환한다."""
    node = cfg
    for key in path[:-1]:
        if not isinstance(node, dict):
            return False
        node = node.get(key)
    if isinstance(node, dict) and path[-1] in node:
        del node[path[-1]]
        return True
    return False


def _save_config(cfg):
    """config.json을 저장하되 과거 Zotero 평문 키는 항상 제거한다."""
    _cfg_unset(cfg, ("zotero", "api_key"))
    with open(CONFIG_PATH, "w", encoding="utf-8") as config_file:
        json.dump(cfg, config_file, indent=2, ensure_ascii=False)
        config_file.write("\n")


def step_config():
    """기존 로컬 config를 로드하거나 키 없는 최소 config를 만든다."""
    if CONFIG_PATH.exists():
        print(f"[1/4] config.json 로드: {CONFIG_PATH}")
        with open(CONFIG_PATH, "r", encoding="utf-8") as config_file:
            cfg = json.load(config_file)
        if not isinstance(cfg, dict):
            raise ValueError("config.json 최상위 값은 JSON 객체여야 합니다")
        if _cfg_unset(cfg, ("zotero", "api_key")):
            _save_config(cfg)
            print("  · 기존 zotero.api_key 제거 — ZOTERO_API_KEY 환경변수만 사용합니다")
        return cfg

    print("[1/4] 키 없는 최소 config.json 생성")
    cfg = {"zotero": {"collections": {}}}
    _save_config(cfg)
    print("  · 원격 Zotero, 이메일, 배포, 그림 설정은 필요한 기능에서만 추가합니다")
    return cfg


def step_local_output():
    """Curio와 로컬 도구가 발견할 수 있는 빈 논문 저장소를 준비한다."""
    print(f"\n[2/4] 로컬 출력 디렉터리 확인: {LOCAL_PAPERS_DIR}")
    try:
        LOCAL_PAPERS_DIR.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        print(f"  ✗ 로컬 출력 디렉터리 생성 실패: {exc}")
        return False
    print("  ✓ 준비됨")
    return True


def _credential_source(provider):
    """Use the same environment/OS-store boundary as execution."""
    from lib.credentials import credential_status
    return credential_status(provider)


def _diagnostic(feature, ok, status, credential, source, authorization, message):
    """기능 진단의 작고 직렬화 가능한 반환 형식."""
    return {
        "feature": feature,
        "ok": ok,
        "status": status,
        "credential": credential,
        "credential_source": source,
        "authorization": authorization,
        "message": message,
    }


def _credential_check(feature, provider, credential, detail):
    state = _credential_source(provider)
    if not state["configured"]:
        return _diagnostic(
            feature,
            False,
            "runtime_unavailable" if state["status"] == "unavailable" else "missing_credential",
            credential,
            None,
            "not_checked",
            f"{credential}가 필요합니다. 선택하지 않은 다른 기능에는 영향을 주지 않습니다.",
        )
    return _diagnostic(
        feature,
        True,
        "configured_unverified",
        credential,
        state["source"],
        "not_checked",
        detail,
    )


def check_review(cfg):
    """Anthropic 기반 리뷰의 자격증명 설정만 진단한다.

    유료 생성 요청은 보내지 않으므로 키의 유효성, 모델 접근 권한, 잔액은 확인하지
    않는다. 환경변수와 공통 OS keyring만 인정한다.
    """
    return _credential_check(
        "review",
        "anthropic",
        "ANTHROPIC_API_KEY",
        "Anthropic 자격증명이 설정되어 있습니다. API 권한·모델 접근·과금 상태는 확인하지 않았습니다.",
    )


def check_keyword_search(cfg=None):
    """로컬 BM25 인덱스 구축·조회 경로의 실행 준비 상태만 진단한다."""
    del cfg
    missing = []
    python_version = tuple(sys.version_info[:2])
    if python_version != (3, 12):
        missing.append(
            f"Python 3.12 정확히 필요 (현재 {python_version[0]}.{python_version[1]})"
        )
    if not BUILD_SEARCH_INDEX_PATH.is_file():
        missing.append("pipeline/build_search_index.py")
    if not QUERY_SEARCH_INDEX_PATH.is_file():
        missing.append("pipeline/query_search_index.py")

    if missing:
        return _diagnostic(
            "keyword-search",
            False,
            "runtime_unavailable",
            None,
            None,
            "not_required",
            "로컬 BM25 키워드 검색을 실행할 수 없습니다: "
            + ", ".join(missing)
            + ". API 자격증명은 필요하지 않으며 의미 검색이나 생성형 답변 진단이 아닙니다.",
        )

    return _diagnostic(
        "keyword-search",
        True,
        "ready",
        None,
        None,
        "not_required",
        "로컬 BM25 키워드 검색 준비 완료. 의미 검색이나 생성형 답변은 포함하지 않습니다. "
        "빌드: python3.12 pipeline/build_search_index.py --topic TOPIC --mode bm25; "
        "조회: python3.12 pipeline/query_search_index.py --topic TOPIC --query QUERY --mode bm25",
    )


def check_semantic_search(cfg):
    """Google 문서 임베딩 경로의 자격증명 설정만 진단한다."""
    return _credential_check(
        "semantic-search",
        "google",
        "GOOGLE_API_KEY",
        "Google 자격증명이 설정되어 있습니다. 임베딩 모델 권한·할당량·과금 상태는 확인하지 않았습니다.",
    )


def check_audio(cfg):
    """Google TTS 경로의 자격증명 설정만 진단한다."""
    return _credential_check(
        "audio",
        "google",
        "GOOGLE_API_KEY",
        "Google 자격증명이 설정되어 있습니다. TTS 모델 권한·할당량·과금 상태는 확인하지 않았습니다.",
    )


def check_email(cfg):
    """Resend 이메일 경로의 자격증명 설정만 진단한다."""
    return _credential_check(
        "email",
        "resend",
        "RESEND_API_KEY",
        "Resend 자격증명이 설정되어 있습니다. API 권한·발신 도메인·수신자 제한은 확인하지 않았습니다.",
    )


def check_zotero_sync(cfg=None):
    """공통 자격증명으로 실제 Zotero 원격 인증·연결을 진단한다.

    ``cfg``는 다른 진단 함수와 같은 호출 모양을 위한 선택 인자다. 의도적으로
    config.json의 ``zotero.api_key``를 읽지 않는다.
    """
    del cfg
    from lib.credentials import CredentialsError, resolve_credential
    try:
        api_key = resolve_credential("zotero")
    except CredentialsError:
        return _diagnostic(
            "zotero-sync",
            False,
            "missing_credential",
            "ZOTERO_API_KEY",
            None,
            "not_checked",
            "ZOTERO_API_KEY 환경변수 또는 OS keyring 참조가 필요합니다. config.json의 키는 사용하지 않습니다.",
        )
    source = "env:ZOTERO_API_KEY" if os.environ.get("ZOTERO_API_KEY", "").strip() else "keyring"

    request = urllib.request.Request(
        "https://api.zotero.org/keys/current",
        headers={
            "Zotero-API-Key": api_key,
            "User-Agent": "paper-curation-setup/1",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            payload = json.load(response)
    except Exception as exc:
        return _diagnostic(
            "zotero-sync",
            False,
            "connection_failed",
            "ZOTERO_API_KEY",
            source,
            "failed",
            f"Zotero 원격 인증 또는 연결에 실패했습니다 ({type(exc).__name__}).",
        )

    if not isinstance(payload, dict) or not str(payload.get("userID", "")).strip():
        return _diagnostic(
            "zotero-sync",
            False,
            "invalid_response",
            "ZOTERO_API_KEY",
            source,
            "failed",
            "Zotero가 사용자 ID 없는 응답을 반환했습니다. 키 권한과 서비스 상태를 확인하세요.",
        )

    return _diagnostic(
        "zotero-sync",
        True,
        "connected",
        "ZOTERO_API_KEY",
        source,
        "verified",
        "Zotero가 키를 받아 사용자 정보를 반환했습니다. 컬렉션별 읽기·쓰기 권한은 확인하지 않았습니다.",
    )


def check_feature(feature, cfg):
    """이름으로 한 기능만 진단한다. 파이프라인이나 유료 요청은 실행하지 않는다."""
    if feature == "review":
        return check_review(cfg)
    if feature == "zotero-sync":
        return check_zotero_sync(cfg)
    if feature == "keyword-search":
        return check_keyword_search(cfg)
    if feature == "semantic-search":
        return check_semantic_search(cfg)
    if feature == "audio":
        return check_audio(cfg)
    if feature == "email":
        return check_email(cfg)
    registry = _feature_registry().get(feature)
    if registry:
        providers = registry["supported_providers"]
        if feature == "timeline-image":
            from generate_timelines import diagnose_timeline_capabilities
            state = diagnose_timeline_capabilities(images_only=True)
            return _diagnostic(
                feature, state["available"], state["status"], None, None,
                "not_checked", state.get("reason", "Configured backend credentials found; API access is not verified."),
            )
        if not providers:
            return _diagnostic(
                feature, True, "requires-request", None, None, "not_required",
                f"{registry['label_en']} has no mandatory credential. Inspect a run_feature request for input/runtime readiness.",
            )
        from run_feature import ENV_NAMES
        provider = providers[0]
        return _credential_check(
            feature, provider, ENV_NAMES.get(provider, f"credential:{provider}"),
            f"{registry['label_en']} default provider is configured. API access is unverified; select alternatives in the feature request.",
        )
    return _diagnostic(
        feature,
        False,
        "unsupported",
        None,
        None,
        "not_checked",
        f"지원하지 않는 기능 진단입니다: {feature}",
    )


def _print_diagnostic(result):
    marker = "✓" if result["ok"] else "✗"
    print(f"\n[기능 진단] {result['feature']}")
    print(f"  {marker} {result['status']}")
    if result["credential_source"]:
        print(f"  · 자격증명 출처: {result['credential_source']}")
    print(f"  · 인증 확인: {result['authorization']}")
    print(f"  · {result['message']}")


def step_skill_md(cfg):
    """설치용 SKILL.md를 템플릿에서 생성한다."""
    print("\n[3/4] SKILL.md 생성")
    if not TEMPLATE_PATH.exists():
        print("  ✗ SKILL.md.template이 없습니다")
        return False

    zotero = cfg.get("zotero", {}) if isinstance(cfg.get("zotero", {}), dict) else {}
    github = cfg.get("github", {}) if isinstance(cfg.get("github", {}), dict) else {}
    replacements = {
        "{github_repo}": str(github.get("repo", "")),
        "{pages_base_url}": str(github.get("pages_base_url", "")),
        "{zotero_dir}": str(zotero.get("pdf_dir", "")),
        "{project_dir}": str(REPO),
        "{email}": str(zotero.get("email", "") or cfg.get("unpaywall_email", "")),
    }

    try:
        content = TEMPLATE_PATH.read_text(encoding="utf-8")
        for placeholder, value in replacements.items():
            content = content.replace(placeholder, value)
        SKILL_OUTPUT.write_text(content, encoding="utf-8")
    except OSError as exc:
        print(f"  ✗ SKILL.md 생성 실패: {exc}")
        return False

    print(f"  ✓ {SKILL_OUTPUT}")
    return True


def step_install():
    """생성된 SKILL.md를 Claude Code skills 디렉터리에 설치한다."""
    print("\n[4/4] SKILL.md 설치")
    if not SKILL_OUTPUT.exists():
        print("  ✗ SKILL.md가 없습니다")
        return False
    try:
        SKILL_INSTALL_DIR.mkdir(parents=True, exist_ok=True)
        content = SKILL_OUTPUT.read_text(encoding="utf-8")
        # The machine-specific checkout belongs only to the privately installed
        # skill, never to the tracked template/dispatcher.
        content += "\n\nInstalled checkout (local-only): " + json.dumps(str(REPO), ensure_ascii=False) + "\n"
        (SKILL_INSTALL_DIR / "SKILL.md").write_text(content, encoding="utf-8")
    except OSError as exc:
        print(f"  ✗ SKILL.md 설치 실패: {exc}")
        return False
    print(f"  ✓ {SKILL_INSTALL_DIR / 'SKILL.md'}")
    return True


def build_parser():
    parser = argparse.ArgumentParser(description="paper-curation keyless setup")
    parser.add_argument(
        "--no-install",
        action="store_true",
        help="SKILL.md 스킬 설치를 건너뜁니다",
    )
    parser.add_argument(
        "--check-feature",
        choices=FEATURE_CHOICES,
        action="append",
        default=[],
        help="선택한 기능의 실행 준비/자격증명/연결만 진단합니다 (반복 지정 가능)",
    )
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)

    print("=" * 50)
    print("  Paper Curation — Keyless Setup")
    print("=" * 50)

    try:
        cfg = step_config()
    except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
        print(f"  ✗ config.json 준비 실패: {exc}")
        return 1

    if not step_local_output():
        return 1
    if not step_skill_md(cfg):
        print("\n설치 실패: SKILL.md를 생성하지 못했습니다.")
        return 1

    if args.no_install:
        print("\n[4/4] 스킬 설치 건너뜀 (--no-install)")
        print(f"  수동 설치: cp {SKILL_OUTPUT} ~/.claude/skills/paper-curation/SKILL.md")
    elif not step_install():
        print("\n설치 실패: SKILL.md를 설치하지 못했습니다.")
        return 1

    diagnostics = []
    for feature in args.check_feature:
        diagnostic = check_feature(feature, cfg)
        diagnostics.append(diagnostic)
        _print_diagnostic(diagnostic)

    print("\n" + "=" * 50)
    print("  설치 완료 — API 키는 설치 필수 조건이 아닙니다")
    print("=" * 50)
    print(f"  Config:       {CONFIG_PATH}")
    print(f"  Local papers: {LOCAL_PAPERS_DIR}")
    print("  유료 API 요청과 전체 파이프라인은 실행하지 않았습니다.")
    print(f"  선택 진단: --check-feature {{{','.join(FEATURE_CHOICES)}}}")

    if any(not diagnostic["ok"] for diagnostic in diagnostics):
        print("\n설치는 완료됐지만 하나 이상의 선택 기능 진단이 실패했습니다.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
