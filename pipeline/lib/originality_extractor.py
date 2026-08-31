"""
Originality extraction from paper text.
Ported from scisci/scie/lib/originality.py.

Strategy:
1. Primary: rule-based trigger matching (free, instant)
2. Fallback: LLM (Claude Haiku) when rule-based finds nothing
3. Self-learning: LLM-discovered triggers added to triggers JSON
"""
import hashlib
import json
import os
import re
import unicodedata
from pathlib import Path

TRIGGERS_PATH = Path(__file__).parent / "originality_triggers.json"

# ── Provenance ──
# `originality.md` 는 캐시인데 **자기가 어느 text.md 에서 나왔는지 기록하지
# 않았다**. 그래서 파일이 존재하고 비어 있지만 않으면 원문을 다시 보지 않고
# 그대로 신뢰했고, 한번 잘못 들어간 파일은 영구히 남았다 — 실측 29편(0.7%)이
# 자기 text.md 에서 재현 불가능한 내용을 들고 있었다. 예: 슬러그 256
# (RFdiffusion, Nature 2023)의 originality 가 "Here, we introduce VibeGen…"
# (슬러그 065)이었고, 256 의 text.md 에 "VibeGen" 은 0회 등장한다. 이 29편은
# 임베딩·분류·연관논문이 전부 남의 내용으로 계산돼 왔다.
#
# 저장소에 이미 같은 문제를 푼 선례가 있다 — `bibliography.json` 사이드카는
# `text_md_sha256` 를 같이 적고 해시가 어긋나면 거부한다. 같은 규칙을 쓴다.
ORIGINALITY_META = "originality.meta.json"
ORIGINALITY_SCHEMA = 1

_DEHYPHEN_RE = re.compile(r"-\s+")
_ALNUM_RE = re.compile(r"[^a-z0-9]+")
# 앞머리 이만큼이 원문에 있으면 그 원문에서 나온 것으로 본다. 짧으면 흔한
# 상투구("in this paper we propose")가 아무 논문에나 걸리고, 길면 OCR 잡음
# 한 글자에 정상 파일이 탈락한다.
_DERIVE_SHINGLE = 100


def text_digest(text: str) -> str:
    """text.md 내용의 sha256 — 사이드카가 가리키는 원문의 신원."""
    return hashlib.sha256((text or "").encode("utf-8", "replace")).hexdigest()


def _match_key(text: str) -> str:
    """대조용 정규화: NFKD → leak strip → 하이픈 줄바꿈 복원 → 영숫자만.

    추출기는 원문 문장을 *그대로* 잘라 쓰지만, 그 전에 `split_sentences` 가
    **NFKD 정규화**를 걸어 합자(ﬁ→fi)와 악센트를 분해하고 `_strip_metadata_leaks`
    가 공백·구두점을 손본다. PDF 는 단어를 하이픈으로 끊어 놓는다. 이 셋을 모두
    지우지 않으면 멀쩡한 파일이 대조에서 탈락한다 — 실측으로 거친 대조 729편,
    하이픈만 복원 118편, NFKD 까지 맞춰야 진짜 값 29편이 나온다.
    """
    text = unicodedata.normalize("NFKD", text or "")
    text = _strip_metadata_leaks(text)
    return _ALNUM_RE.sub("", _DEHYPHEN_RE.sub("", text).lower())


def derives_from(originality: str, paper_text: str) -> bool:
    """이 originality 가 이 text.md 에서 나올 수 있는가.

    추출기가 원문 문장을 그대로 이어 붙이므로 포함 관계로 판정된다. 너무 짧아
    판정할 근거가 없으면 통과시킨다(제목+essence fallback 이 그런 경우다).
    """
    key = _match_key(originality)
    if len(key) < _DERIVE_SHINGLE:
        return True
    return key[:_DERIVE_SHINGLE] in _match_key(paper_text)


# ── 사용 불가 출력 판정 ──
# LLM 으로 originality 를 쓰게 하면 **거부 문장이 그대로 파일에 들어가는** 실패가
# 생긴다. 실측(8편 A/B): text.md 가 목차·슬라이드 덤프인 슬러그 9132 에서
# claude-haiku-4-5 가 "I cannot provide the requested summary because the provided
# text is only a table of contents..." 를 돌려줬다(qwen3.8·sonnet 은 정상 요약).
# 그 문장이 저장되면 SPECTER2 가 *거부문*을 임베딩하고, 거부당한 논문들끼리
# 서로 가까워져 가짜 클러스터가 생긴다 — 어설픈 요약보다 훨씬 나쁘다.
# 해시 사이드카는 이걸 못 잡는다(출처는 진짜 맞으므로). 그래서 별도 게이트다.
_REFUSAL_RE = re.compile(
    r"\b(i (cannot|can't|can not|am unable|do not have|don't have)"
    r"|unable to (provide|summari[sz]e|determine)"
    r"|cannot (provide|determine|summari[sz]e)"
    r"|would need (access|the actual)"
    r"|(is|are) only a (table of contents|list of|set of)"
    r"|no (abstract|content|actual paper)"
    r"|as an ai\b)", re.I)

# 이 아래로는 기여를 한 문장도 못 담는다. A/B 표본의 정상 출력은 428~893자였다.
MIN_ORIGINALITY_CHARS = 120


def looks_unusable(text: str, prompt_echo: str = "") -> str:
    """쓸 수 없는 LLM 출력이면 사유 문자열, 쓸 수 있으면 "".

    호출부는 사유가 있으면 **파일을 쓰지 않고** 다음 백엔드로 넘어가야 한다.
    전부 실패하면 기존 규칙 기반 결과를 그대로 둔다 — 나쁜 것을 쓰느니
    낡은 것을 두는 편이 낫다.
    """
    body = (text or "").strip()
    if len(body) < MIN_ORIGINALITY_CHARS:
        return f"too-short({len(body)})"
    if _REFUSAL_RE.search(body):
        return "refusal"
    if prompt_echo and prompt_echo[:60].lower() in body.lower():
        return "prompt-echo"
    return ""


def read_provenance(slug_dir) -> dict:
    """`originality.meta.json` 을 읽는다. 없거나 스키마가 낯설면 {}."""
    path = os.path.join(str(slug_dir), ORIGINALITY_META)
    try:
        with open(path, "r", encoding="utf-8") as f:
            meta = json.load(f)
    except Exception:
        return {}
    if not isinstance(meta, dict) or meta.get("schema") != ORIGINALITY_SCHEMA:
        return {}
    return meta


def write_provenance(slug_dir, text_sha256, extractor):
    """originality.md 옆에 그 출처를 남긴다."""
    path = os.path.join(str(slug_dir), ORIGINALITY_META)
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"schema": ORIGINALITY_SCHEMA,
                   "text_md_sha256": text_sha256,
                   "extractor": extractor}, f, ensure_ascii=False, indent=1)


# ── Metadata leak strip ──
# originality.md 에 PDF 추출 잔재 (DOI, arXiv id, URL, HTML 태그) 가 섞여
# 들어가면 다운스트림 c-TF-IDF 키워드 추출 시 *클러스터 구별 단어* 로
# 부각되어 카테고리 이름 품질을 망친다. 모든 추출 경로의 마지막에서 적용.
_LEAK_PATTERNS = [
    # URL — 다음에 등장하는 DOI/arXiv 패턴이 URL 안에 포함되어 있어도 먼저 제거
    re.compile(r"https?://\S+", re.I),
    # arXiv ID (arXiv:2407.09811v1 / 2407.09811v1 / abs/2407.09811)
    re.compile(r"\b(?:arXiv:|abs/)?\d{4}\.\d{4,5}(?:v\d+)?\b", re.I),
    # DOI (10.NNNN/...)
    re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.I),
    # HTML 태그 (<br>, <p>, <span>, ...)
    re.compile(r"<[a-zA-Z][^>]*>"),
]


def _strip_metadata_leaks(text: str) -> str:
    """Remove URL/arXiv/DOI/HTML leaks from extracted originality text.

    Idempotent. Returns the cleaned text with collapsed whitespace.
    """
    if not text:
        return text
    for pat in _LEAK_PATTERNS:
        text = pat.sub(" ", text)
    text = re.sub(r"\s+([,.;:?!])", r"\1", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def load_triggers(path=None):
    """Load trigger categories and flat list."""
    path = path or TRIGGERS_PATH
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    categories = {k: v for k, v in data.items() if k.startswith("rule_base_")}
    all_triggers = []
    for words in categories.values():
        all_triggers.extend(words)
    return {"categories": categories, "all": list(set(all_triggers)), "_path": str(path)}


def split_sentences(text):
    # Normalize: ligatures, non-breaking space, newlines, copyright symbol
    import unicodedata
    text = unicodedata.normalize("NFKD", text)
    text = text.replace("\u00a9", " ").replace("\xa0", " ").replace("\n", " ")
    text = re.sub(r'\s+', ' ', text).strip()
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return [s.strip() for s in sentences if len(s.strip()) > 10]


# Strong novelty signals
_STRONG_NOVELTY = frozenset({
    "for the first time", "unprecedented", "pioneering",
    "state-of-the-art", "cutting-edge", "innovative",
})

_STRICT_AUTHORSHIP = frozenset({
    "we ", " our ", "this study", "this paper", "this work",
    "this article", "this research", "this report", "this investigation",
    "in this study", "in this work", "in this paper",
    "here ", "herein",
    "the paper ", "the study ", "the work ", "the article ",
    "the present study", "the present work", "the present paper",
    "the current study", "the current work", "the current paper",
})

_REFERENTIAL_STARTS = ("it ", "its ", "this ", "these ", "such ", "the ")

# Stop triggers (too broad to learn)
_STOP_TRIGGERS = frozenset({
    "the", "a", "an", "is", "are", "was", "were", "be", "been", "being",
    "have", "has", "had", "do", "does", "did", "will", "would", "could",
    "should", "may", "might", "can", "shall", "must", "need", "also",
    "not", "no", "but", "and", "or", "if", "then", "than", "that", "this",
    "these", "those", "it", "its", "they", "their", "them",
    "with", "from", "into", "for", "of", "on", "in", "at",
    "to", "by", "as", "about", "between", "through", "during",
    "more", "most", "very", "much", "many", "some", "any", "all",
    "based on", "due to", "in order to", "according to",
    "important", "significant", "recent", "various", "different",
    "however", "therefore", "thus", "hence", "moreover",
    "data", "method", "model", "system", "paper", "study", "research",
})


# 트리거 문장부터 어디까지 담을지. 이 함수는 originality 문장을 *고르는* 게
# 아니라 첫 트리거 문장부터 **문서 끝까지** 잘라 왔다. 초록 창(1000자)으로
# 부를 때는 창이 곧 경계라 티가 안 났지만, 트리거를 못 찾아 전문으로 재호출하면
# 경계가 사라져 논문 한 편이 통째로 들어왔다 — 실측 262편이 20KB 초과, 최대
# 711KB. SPECTER2 는 512 토큰에서 자르므로 그 텍스트의 평균 1.2% 만 임베딩되고
# 나머지는 디스크만 먹었다.
#
# 문장 수와 문자 수를 **둘 다** 건다. 문장 수만으로는 못 막는다 — PDF 추출이
# 마침표를 잃으면 `split_sentences` 의 `(?<=[.!?])\s+` 가 아무 데서도 쪼개지
# 못해 논문 한 편이 '문장 1개' 가 되고, 12문장 상한이 통째로 통과시킨다.
# 초록 한 문단이 대개 4~8 문장이라 12, SPECTER2 가 읽는 512 토큰이 대략
# 2,000~2,500자라 여유를 둬 4,000자.
_MAX_SENTENCES = 12
_MAX_CHARS = 4000


def _extract_rule_based(text, triggers, max_sentences=_MAX_SENTENCES,
                        max_chars=_MAX_CHARS):
    """Rule-based originality extraction with strict co-occurrence."""
    if not text or not text.strip():
        return ""

    content_categories = {k: v for k, v in triggers["categories"].items()
                          if "authorship" not in k}

    sentences = split_sentences(text)
    first_orig_idx = None

    for i, sentence in enumerate(sentences):
        s_lower = sentence.lower()
        has_strong = any(t in s_lower for t in _STRONG_NOVELTY)
        has_authorship = any(t in s_lower for t in _STRICT_AUTHORSHIP)
        has_content = False
        if has_authorship:
            for words in content_categories.values():
                for w in words:
                    if w in s_lower:
                        has_content = True
                        break
                if has_content:
                    break
        if has_strong or (has_authorship and has_content):
            first_orig_idx = i
            break

    if first_orig_idx is None:
        return ""

    start_idx = first_orig_idx
    if first_orig_idx > 0:
        s_lower = sentences[first_orig_idx].lower().lstrip()
        if any(s_lower.startswith(ref) for ref in _REFERENTIAL_STARTS):
            start_idx = first_orig_idx - 1

    selected = sentences[start_idx:start_idx + max_sentences]
    out = _strip_metadata_leaks(". ".join(selected))
    if len(out) > max_chars:
        # 문장 경계로 자를 수 있으면 거기서, 아니면(=쪼개지지 않은 덩어리)
        # 문자 상한에서 끊는다. 조각난 문장이 남아도 통째보다 낫다.
        cut = out.rfind(". ", 0, max_chars)
        out = out[:cut + 1] if cut > max_chars // 2 else out[:max_chars]
    return out


# ── LLM Fallback ──

LLM_PROMPT = """Given the following scientific paper text, identify sentences
that describe the paper's originality, novelty, or unique contribution.

Return a JSON object with:
{{
  "originality_sentences": ["exact sentence 1 from text", "exact sentence 2", ...],
  "trigger_phrases": ["phrase that signals originality 1", "phrase 2", ...]
}}

Rules:
- "originality_sentences" must be EXACT copies of sentences from the text (no paraphrasing).
- "trigger_phrases" must be 1-3 word phrases FROM those sentences that signal authorship or novelty
  (e.g., "we report", "novel approach", "for the first time").
- Each trigger_phrase should be lowercase.
- If no originality is found, return empty lists.

Text:
{text}
"""


def _parse_json_response(text):
    """Parse JSON from LLM response."""
    text = text.strip()
    if text.startswith("```"):
        first_nl = text.index("\n") if "\n" in text else len(text)
        text = text[first_nl + 1:]
        if "```" in text:
            text = text[:text.rindex("```")]
        text = text.strip()
    return json.loads(text)


def _llm_fallback(text):
    """Claude Haiku로 originality 추출."""
    try:
        from anthropic import Anthropic
        client = Anthropic()
        resp = client.messages.create(
            model="claude-haiku-4-5",
            max_tokens=1024,
            temperature=0,
            messages=[{"role": "user", "content": LLM_PROMPT.format(text=text)}],
        )
        result = _parse_json_response(resp.content[0].text)
        sentences = result.get("originality_sentences", [])
        triggers = result.get("trigger_phrases", [])
        out = ". ".join(sentences) if sentences else ""
        return _strip_metadata_leaks(out), triggers
    except Exception:
        return "", []


def _update_triggers(triggers_data, new_triggers):
    """LLM이 발견한 trigger를 JSON에 추가 (self-learning)."""
    if not new_triggers:
        return 0

    added = 0
    existing = set(w.strip().lower() for w in triggers_data["all"])

    for trigger in new_triggers:
        trigger = trigger.strip().lower()
        if len(trigger) < 4:
            continue
        if trigger in existing:
            continue
        if trigger.strip() in _STOP_TRIGGERS:
            continue
        words = trigger.split()
        has_verb = any(w.endswith(("ed", "ing", "ize", "ise", "ate", "ify")) for w in words)
        if len(words) < 2 and not has_verb:
            continue

        if "rule_base_learned" not in triggers_data["categories"]:
            triggers_data["categories"]["rule_base_learned"] = []
        triggers_data["categories"]["rule_base_learned"].append(trigger)
        triggers_data["all"].append(trigger)
        existing.add(trigger)
        added += 1

    if added > 0 and "_path" in triggers_data:
        save_data = dict(triggers_data["categories"])
        save_data["_version"] = "2026.1-live"
        save_data["_description"] = "Auto-updated by LLM fallback learning"
        with open(triggers_data["_path"], "w", encoding="utf-8") as f:
            json.dump(save_data, f, indent=4, ensure_ascii=False)

    return added


def extract_originality(text, triggers=None):
    """Extract originality: rule-based first, LLM fallback if empty, self-learning.

    Args:
        text: Paper text (first ~1000 chars recommended)
        triggers: Pre-loaded triggers dict, or None to auto-load

    Returns:
        Originality string (joined sentences), or empty string
    """
    if not text or not text.strip():
        return ""

    if triggers is None:
        triggers = load_triggers()

    # 1. Rule-based
    result = _extract_rule_based(text, triggers)
    if result:
        return result

    # 2. LLM fallback
    result, new_triggers = _llm_fallback(text)

    # 3. Self-learning
    if new_triggers:
        learned = _update_triggers(triggers, new_triggers)
        if learned > 0:
            pass  # logging handled by caller if needed

    return result
