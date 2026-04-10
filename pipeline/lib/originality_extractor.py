"""
Originality extraction from paper text.
Ported from scisci/scie/lib/originality.py.

Strategy:
1. Primary: rule-based trigger matching (free, instant)
2. Fallback: LLM (Claude Haiku) when rule-based finds nothing
3. Self-learning: LLM-discovered triggers added to triggers JSON
"""
import json
import re
from pathlib import Path

TRIGGERS_PATH = Path(__file__).parent / "originality_triggers.json"


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


def _extract_rule_based(text, triggers):
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

    return ". ".join(sentences[start_idx:])


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
            model="claude-haiku-4-5-20251001",
            max_tokens=1024,
            temperature=0,
            messages=[{"role": "user", "content": LLM_PROMPT.format(text=text)}],
        )
        result = _parse_json_response(resp.content[0].text)
        sentences = result.get("originality_sentences", [])
        triggers = result.get("trigger_phrases", [])
        return ". ".join(sentences) if sentences else "", triggers
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
