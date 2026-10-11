"""Content-grounded LLM judging for retrieved paper-connection candidates."""
from __future__ import annotations

import hashlib
import json
import os
import re
from pathlib import Path

from config_loader import PAPERS_DIR

PROMPT_VERSION = "relation-judge-v7"
METADATA_REASON = "관계 미분석 — 임베딩 유사도로 추천된 후보입니다."
RELATIONS = {"foundation", "extension", "alternative", "application", "counterpoint"}
OUTPUT_TOKENS_PER_PAIR = 260
PRICES = {
    "claude-haiku-4-5": (1.0, 5.0),
    "claude-sonnet-5": (3.0, 15.0),
}


def _section(text: str, name: str) -> str:
    match = re.search(rf"^## {re.escape(name)}\s*$([\s\S]*?)(?=^## |\Z)", text, re.M)
    return match.group(1) if match else ""


def _clean(text: str) -> str:
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("![") or stripped.startswith("*Figure "):
            continue
        lines.append(re.sub(r"!\[[^]]*\]\([^)]*\)", "", stripped))
    return " ".join(lines)


def _bullet(section: str, label: str) -> str:
    match = re.search(rf"^\s*[-*]\s+\*\*{label}\*\*:\s*(.+)$", section, re.M)
    return _clean(match.group(1)) if match else ""


def paper_profile(slug: str, paper: dict) -> str:
    """Return a compact, model-safe profile from the paper review and index data."""
    review = Path(PAPERS_DIR) / slug / "review.md"
    text = ""
    try:
        text = review.read_text(encoding="utf-8")
    except OSError:
        pass
    title = str(paper.get("title") or "")
    year = str(paper.get("year") or paper.get("date") or "")
    essence = str(paper.get("essence") or "")
    gap = approach = achievement = ""
    if text:
        heading = re.search(r"^#\s+(.+)$", text, re.M)
        title = heading.group(1).strip() if heading else title
        date = re.search(r"\*\*날짜\*\*:\s*([^|\n]+)", text)
        year = date.group(1).strip() if date else year
        essence = _clean(_section(text, "Essence")) or essence
        motivation = _section(text, "Motivation")
        gap, approach = _bullet(motivation, "Gap"), _bullet(motivation, "Approach")
        achievement_text = _clean(_section(text, "Achievement"))
        first = re.search(r"(?:^|\s)1\.\s*(.+?)(?=\s+2\.\s|$)", achievement_text)
        achievement = first.group(1).strip() if first else ""
    fields = [("제목", title), ("연도", year), ("핵심", essence), ("연구 공백", gap),
              ("접근", approach), ("주요 성과", achievement)]
    profile = "\n".join(f"{key}: {value}" for key, value in fields if value)
    return profile[:900]


def pair_cache_dir() -> Path:
    """Corpus-level cache. A pair judgment depends only on the two papers'
    content, so topics that share papers (ai4s, ai4s+scisci) share it."""
    return Path(PAPERS_DIR) / ".llm_cache"


def _hash(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _cache_path(cache_dir: str | Path, slug_a: str, profile_a: str, slug_b: str,
                profile_b: str, model: str) -> Path:
    pair = sorted(((slug_a, _hash(profile_a)), (slug_b, _hash(profile_b))))
    material = "\0".join([PROMPT_VERSION, model] + [item for pair_item in pair for item in pair_item])
    return Path(cache_dir) / "relation_pairs" / f"{_hash(material)}.json"


# relation = what the CANDIDATE is to the paper being described. The reverse
# view is derived in code (see REVERSE), never asked of the model, so the two
# directions cannot contradict each other.
REVERSE = {"foundation": "extension", "extension": "foundation",
           "application": "foundation", "alternative": "alternative",
           "counterpoint": "counterpoint"}


# The model answers with direction-explicit keys; abstract labels such as
# "foundation" were read backwards ("this paper is the candidate's foundation").
MODEL_LINKS = {
    "this_builds_on_candidate": "foundation",
    "candidate_builds_on_this": "extension",
    "candidate_applies_this": "application",
    "alternative": "alternative",
    "counterpoint": "counterpoint",
    "unrelated": "unrelated",
}


def _year_of(profile: str) -> int | None:
    match = re.search(r"^연도:\s*((?:19|20)\d{2})", profile, re.M)
    return int(match.group(1)) if match else None


def _guard_direction(relation: str, source_year, target_year) -> str:
    """A later paper cannot be an earlier paper's foundation, and an earlier
    paper cannot extend or apply a later one. Contradicted directions become
    the direction-free ``alternative`` rather than an invented lineage."""
    if source_year and target_year and source_year != target_year:
        if relation == "foundation" and target_year > source_year:
            return "alternative"
        if relation in ("extension", "application") and target_year < source_year:
            return "alternative"
    return relation


def _title(profile: str) -> str:
    match = re.search(r"^제목:\s*(.+)$", profile, re.M)
    return match.group(1).strip() if match else ""


def short_name(profile: str) -> str:
    """Reader-facing short name: the part before ':' when the title has one
    ('Safe-SDL: Establishing …' → 'Safe-SDL'), else the first five words."""
    title = _title(profile)
    head = re.split(r"\s*[:：]\s*", title, maxsplit=1)[0].strip()
    if head and head != title and len(head) <= 40:
        return head
    words = title.split()
    return " ".join(words[:5]) + ("…" if len(words) > 5 else "")


_KEY = r"(?<![A-Za-z0-9])C(\d+)(?![0-9A-Za-z])"


def _sanitize(text: str, source_name: str, target_name: str, key_names: dict) -> str:
    """Rewrite leaked internal references to the names a reader sees.

    Only references to a *paper* are touched: "기준/출처 논문" → the source's
    short name, "대상/후보 논문 [Cn]" → that candidate's, a stray "이 논문" →
    the source's, and bare keys "C3" → candidate names. Bare "대상"/"후보"
    are ordinary Korean ("교수자를 대상으로", "후보 물질") and are left alone.
    """
    # Names come from titles and may contain backslashes (LaTeX); pass them
    # through a function so re.sub never parses them as a template.
    text = re.sub(r"(?:기준|출처)\s*논문", lambda _m: source_name, text)

    def candidate(match):
        key = match.group(1)
        return key_names.get(int(key), target_name) if key else target_name
    text = re.sub(r"(?:대상|후보)\s*논문(?:\s*C(\d+))?", candidate, text)
    text = re.sub(r"이\s*논문", lambda _m: source_name, text)
    text = re.sub(_KEY, lambda m: key_names.get(int(m.group(1)), m.group(0)), text)
    return re.sub(r"\s{2,}", " ", text).strip()


def _prompt(source_slug: str, source: str, candidates: list[tuple[str, str]]) -> str:
    # Candidates are keyed C1..Cn: the model must echo the key back, and it
    # shortens long slugs ('535_MetaOpenFOAM'), which silently lost judgments.
    rendered = "\n\n".join(f"[후보 C{i}] 약칭: {short_name(profile)}\n{profile}"
                           for i, (_slug, profile) in enumerate(candidates, 1))
    return f"""논문 리뷰 사이트의 "같이 보면 좋은 논문" 설명을 씁니다. 아래 [기준 논문]과 각 [후보]의 내용 프로필만 근거로 판단하십시오. 프로필에 없는 사실은 추정하지 마십시오.

모든 후보(C1부터 마지막까지)에 대해 빠짐없이 하나씩, target에 후보 키를 그대로 쓰고:
1. relation — 아래 키 중 하나를 그대로 쓰십시오. 방향에 주의하십시오.
   - this_builds_on_candidate: 기준 논문이 후보의 문제정의·방법·데이터를 직접 가져다 쓴다 (후보가 먼저 나온 선행 연구)
   - candidate_builds_on_this: 후보가 기준 논문의 방법·문제를 직접 이어받아 확장한다 (후보가 나중 연구)
   - candidate_applies_this: 후보가 기준 논문의 방법을 특정 분야·과제에 적용한다
   - alternative: 같은 문제를 다른 방법으로 푼다 (같은 분야일 뿐 직접 의존이 없으면 여기)
   - counterpoint: 한쪽이 다른 쪽의 가정·결론을 반박하거나 한계를 드러낸다
   - unrelated: 주제어만 겹치고 실질적인 문제·방법·발견의 연결이 없다 (확신이 없으면 unrelated)
   "결과를 시각화해야 한다", "같이 쓰일 수 있다" 같은 가능성만으로 builds_on/applies를 고르지 마십시오.
2. reason — 이 문장은 두 논문의 페이지 양쪽에 그대로 표시됩니다. 두 논문을 모두 약칭으로 부르며, 공유하는 구체적 문제·방법·발견과 무엇이 다른지를 한국어 1~2문장(150자 안팎)으로 쓰십시오.

금지: "이 논문", "기준 논문", "후보", "출처", "대상" 같은 지칭, C1·C2 같은 후보 키, 유사도 점수, 카테고리, 한 논문만 요약하는 문장.
좋은 예: "Safe-SDL과 MADS-CPS 모두 LLM이 만든 실험 명령의 물리적 위험을 다루지만, Safe-SDL은 제어장벽함수로 실행 중 차단하고 MADS-CPS는 실행 기록을 사후 검증 가능한 계약으로 남긴다."

[기준 논문] 약칭: {short_name(source)}
{source}

{rendered}"""


def _tool_schema() -> dict:
    item = {"type": "object", "properties": {
        "target": {"type": "string", "description": "candidate key such as C1"},
        "relation": {"type": "string", "enum": list(MODEL_LINKS)},
        "reason": {"type": "string"}},
        "required": ["target", "relation", "reason"]}
    return {"name": "judge_relations",
            "description": "Return one content-grounded judgment per candidate.",
            "input_schema": {"type": "object",
                             "properties": {"judgments": {"type": "array", "items": item}},
                             "required": ["judgments"]}}


def _parse_response(response) -> list[dict]:
    kinds = []
    for block in getattr(response, "content", []) or []:
        kinds.append(getattr(block, "type", "?"))
        if getattr(block, "type", None) == "tool_use" and getattr(block, "name", None) == "judge_relations":
            data = getattr(block, "input", None)
            judgments = data.get("judgments") if isinstance(data, dict) else None
            if isinstance(judgments, str):
                # Haiku occasionally serialises the array as a JSON string.
                try:
                    judgments = json.loads(judgments)
                except ValueError:
                    judgments = None
            if isinstance(judgments, list):
                return judgments
    reason = getattr(response, "stop_reason", None)
    raise ValueError(f"judge_relations tool was not returned "
                     f"(stop_reason={reason}, blocks={kinds})")


def _cost(tokens_in: int, tokens_out: int, model: str) -> float:
    price_in, price_out = PRICES.get(model, PRICES["claude-haiku-4-5"])
    return tokens_in * price_in / 1_000_000 + tokens_out * price_out / 1_000_000


def _estimate_input_tokens(prompt: str) -> int:
    """Upper-bound input tokens. Korean prose tokenizes near one token per
    character, so a chars/4 estimate undercounts spend about five-fold."""
    return max(1, len(prompt))


def _judge_source(client, model, source_slug, source_profile, pairs):
    """One call for ``pairs`` = [(target, target_profile, cache_path)].
    Returns (judgments_by_target, input_tokens, output_tokens)."""
    prompt = _prompt(source_slug, source_profile, [(t, prof) for t, prof, _ in pairs])
    response = client.messages.create(
        model=model, max_tokens=400 + OUTPUT_TOKENS_PER_PAIR * len(pairs),
        messages=[{"role": "user", "content": prompt}], tools=[_tool_schema()],
        tool_choice={"type": "tool", "name": "judge_relations"})
    usage = getattr(response, "usage", None)
    tokens = (int(getattr(usage, "input_tokens", 0) or 0),
              int(getattr(usage, "output_tokens", 0) or 0))
    returned = {}
    for item in _parse_response(response):
        if isinstance(item, dict):
            key = re.sub(r"[^0-9]", "", str(item.get("target") or ""))
            if key:
                returned[int(key)] = item
    judged = {}
    key_names = {position: short_name(profile)
                 for position, (_target, profile, _path) in enumerate(pairs, 1)}
    for position, (target, _profile, path) in enumerate(pairs, 1):
        item = returned.get(position)
        if not item or item.get("relation") not in MODEL_LINKS:
            continue
        relation = _guard_direction(MODEL_LINKS[item["relation"]],
                                    _year_of(source_profile), _year_of(_profile))
        reason = _sanitize(str(item.get("reason") or ""), short_name(source_profile),
                           short_name(_profile), key_names)
        # One neutral sentence names both papers, so both pages show it as is.
        data = {"source": source_slug, "target": target, "relation": relation,
                "reverse_relation": REVERSE.get(relation, "unrelated"),
                "reason_source": reason, "reason_target": reason,
                "model": model, "prompt_version": PROMPT_VERSION}
        if not data["reason_source"] or not data["reason_target"]:
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        judged[target] = data
    return judged, tokens


def judge_connections(connections, papers, *, topic, cache_dir, client, log=print) -> dict:
    """Judge metadata candidates, preserving them unchanged whenever judging fails.

    Three phases so a run pays once per undirected pair and never exceeds its
    cap: (1) plan — read the pair cache and assign every uncached pair to the
    first source that lists it; (2) execute — one call per source, run
    concurrently, each reserving its worst-case cost against the cap and
    reconciling to the reported usage; (3) assemble — every entry, from either
    direction, reads the shared pair judgment.
    """
    import threading
    from concurrent.futures import ThreadPoolExecutor

    if os.environ.get("RELATION_JUDGE", "on").lower() == "off":
        return connections
    model = os.environ.get("RELATION_JUDGE_MODEL", "claude-haiku-4-5")
    try:
        cap = float(os.environ.get("RELATION_JUDGE_MAX_USD", "5.0"))
    except ValueError:
        cap = 5.0
    try:
        workers = max(1, int(os.environ.get("RELATION_JUDGE_WORKERS", "6")))
    except ValueError:
        workers = 6
    by_slug = {p.get("slug"): p for p in papers if isinstance(p, dict) and p.get("slug")}
    profiles = {}

    def profile(slug):
        if slug not in profiles:
            profiles[slug] = paper_profile(slug, by_slug[slug]) if slug in by_slug else ""
        return profiles[slug]

    stats = {"pairs": 0, "hits": 0, "calls": 0, "judged": 0, "dropped": 0,
             "fallback": 0, "failed_calls": 0, "budget_skipped": 0}
    pair_data = {}          # frozenset({a, b}) -> judgment dict
    assigned = {}           # source -> [(target, target_profile, cache_path)]
    claimed = set()

    # ── 1. plan ─────────────────────────────────────────────────────────────
    for source_slug, entries in connections.items():
        source_profile = profile(source_slug)
        for entry in entries:
            target = entry.get("slug")
            if entry.get("basis") != "metadata" or not target:
                continue
            key = frozenset((source_slug, target))
            if key in pair_data or key in claimed:
                continue
            target_profile = profile(target)
            if not source_profile or not target_profile:
                continue
            path = _cache_path(cache_dir, source_slug, source_profile, target,
                               target_profile, model)
            try:
                pair_data[key] = json.loads(path.read_text(encoding="utf-8"))
                stats["hits"] += 1
            except (OSError, ValueError, TypeError):
                claimed.add(key)
                assigned.setdefault(source_slug, []).append((target, target_profile, path))
    stats["pairs"] = stats["hits"] + len(claimed)

    # ── 2. execute ──────────────────────────────────────────────────────────
    lock = threading.Lock()
    spend = {"reserved": 0.0, "actual": 0.0}
    first_error = []

    def run(source_slug):
        pairs = assigned[source_slug]
        prompt = _prompt(source_slug, profiles[source_slug],
                         [(t, prof) for t, prof, _ in pairs])
        worst = _cost(_estimate_input_tokens(prompt),
                     400 + OUTPUT_TOKENS_PER_PAIR * len(pairs), model)
        with lock:
            if spend["actual"] + spend["reserved"] + worst > cap:
                stats["budget_skipped"] += len(pairs)
                return
            spend["reserved"] += worst
        for attempt in (1, 2):
            if attempt == 2:
                with lock:
                    if spend["actual"] + spend["reserved"] + worst > cap:
                        stats["budget_skipped"] += len(pairs)
                        return
                    spend["reserved"] += worst
            try:
                judged, (tin, tout) = _judge_source(
                    client, model, source_slug, profiles[source_slug], pairs)
            except Exception as exc:  # network, rate limit, parse failure
                with lock:
                    spend["reserved"] -= worst
                    stats["failed_calls"] += 1
                    if not first_error:
                        first_error.append(f"{type(exc).__name__}: {str(exc)[:200]}")
                continue
            with lock:
                spend["reserved"] -= worst
                spend["actual"] += _cost(tin, tout, model)
                stats["calls"] += 1
                for target, data in judged.items():
                    pair_data[frozenset((source_slug, target))] = data
            return

    if assigned:
        with ThreadPoolExecutor(max_workers=workers) as pool:
            list(pool.map(run, sorted(assigned)))
    if first_error:
        log(f"  관계 판정 호출 실패 {stats['failed_calls']}건 (첫 오류: {first_error[0]})")

    # ── 3. assemble ─────────────────────────────────────────────────────────
    result = {}
    for source_slug, entries in connections.items():
        updated = []
        for entry in entries:
            target = entry.get("slug")
            data = (pair_data.get(frozenset((source_slug, target)))
                    if entry.get("basis") == "metadata" and target else None)
            if not data:
                if entry.get("basis") == "metadata":
                    stats["fallback"] += 1
                updated.append(dict(entry))
                continue
            forward = data.get("source") == source_slug
            relation = data["relation"] if forward else data["reverse_relation"]
            reverse = data["reverse_relation"] if forward else data["relation"]
            reason = data["reason_source"] if forward else data["reason_target"]
            reverse_reason = data["reason_target"] if forward else data["reason_source"]
            if relation == "unrelated" or reverse == "unrelated":
                stats["dropped"] += 1
                continue
            updated.append(dict(entry, relation=relation, reason=reason,
                                reverse_relation=reverse, reverse_reason=reverse_reason,
                                basis="model", model=model))
            stats["judged"] += 1
        result[source_slug] = updated
    log("  관계 판정: papers={papers}, pairs={pairs}, cache hits={hits}, calls={calls}, "
        "judged={judged}, unrelated-dropped={dropped}, fallback={fallback}, "
        "failed-calls={failed_calls}, budget-skipped={budget_skipped}, "
        "actual=${actual:.4f} (cap ${cap:.2f})".format(
            papers=len(connections), actual=spend["actual"], cap=cap, **stats))
    return result


def judge_if_enabled(connections, papers, *, topic, log=print) -> dict:
    """Judge freshly built candidates — the single entry every writer uses.

    Both ``topic_modeling`` Step 6 and the ``extract_insights`` connections
    pass rewrite a topic's connections. If only one of them judged, the other
    would overwrite judged pairs with metadata candidates. Judged pairs come
    from the shared cache, so calling this again costs only for new pairs.
    Without a credential the candidates stay as the honest fallback.
    """
    if os.environ.get("RELATION_JUDGE", "on").lower() == "off":
        return connections
    from lib.credentials import CredentialsError, resolve_credential
    try:
        api_key = resolve_credential("anthropic")
    except CredentialsError as exc:
        log(f"  관계 판정 건너뜀: Anthropic 자격증명 없음 ({exc}) — 미분석 후보로 유지")
        return connections
    from anthropic import Anthropic
    client = Anthropic(api_key=api_key,
                       timeout=float(os.environ.get("EXTRACT_INSIGHTS_HTTP_TIMEOUT", "120")),
                       max_retries=int(os.environ.get("EXTRACT_INSIGHTS_HTTP_RETRIES", "1")))
    return judge_connections(connections, papers, topic=topic,
                             cache_dir=pair_cache_dir(), client=client, log=log)
