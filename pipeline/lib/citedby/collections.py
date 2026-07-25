"""인용논문을 어느 Zotero 컬렉션에 넣으면 좋을지 추천한다.

배경 — citedby 로 등록한 인용논문은 **컬렉션이 지정되지 않는다**(인용논문은
검색 결과이지 사용자가 고른 논문이 아니라, 원논문의 컬렉션에 섞으면 그
컬렉션의 의미가 오염된다). 그래서 Unfiled 에 쌓인다(실측 121편). 분류는
사용자 판단이지만, **후보를 제안해 주면 판단이 훨씬 빨라진다.**

설계 원칙:
  * **기존 컬렉션만 제안한다.** 새 컬렉션을 만들라고 하지 않는다 — 분류 체계는
    사용자 것이고, LLM 이 늘릴 대상이 아니다.
  * 근거를 함께 낸다. "왜 여기인지" 없이 이름만 주면 검증이 안 된다.
  * 확신이 없으면 **비워 둔다**. 억지 배정이 Unfiled 보다 나쁘다.
  * 판단 재료는 PDF 전문이 있으면 전문, 없으면 초록·제목.
"""
from __future__ import annotations

import logging
import sqlite3

logger = logging.getLogger(__name__)

BATCH_SIZE = 12

# 후보에서 빼는 컬렉션 — 비어 있거나 시험용이면 제안해도 쓸모가 없다.
_MIN_ITEMS = 3
_SKIP_NAMES = frozenset({"test", "temp", "tmp", "untitled"})

_COLLECTION_QUERY = """
SELECT c.collectionID, c.collectionName, c.parentCollectionID,
       (SELECT COUNT(*) FROM collectionItems ci
        WHERE ci.collectionID = c.collectionID) AS n
FROM collections c
"""

_PROMPT = """아래는 내 Zotero 컬렉션 목록과, 새로 수집한 논문들이다.
각 논문을 **기존 컬렉션 중 하나**에 배정하라.

## 내 컬렉션
{collections}

## 논문
{papers}

규칙:
- **위 목록에 있는 컬렉션 이름만** 쓴다. 새로 만들지 않는다.
- 주제가 어느 컬렉션에도 뚜렷이 맞지 않으면 collection 을 빈 문자열로 둔다.
  억지로 배정하지 마라 — 미분류가 잘못된 분류보다 낫다.
- reason 은 한국어 한 문장. 논문의 어떤 내용이 그 컬렉션과 맞는지 말한다.
- confidence 는 high / medium / low.

JSON 만 출력:
{{"results": [{{"paper": 1, "collection": "이름", "reason": "...", "confidence": "high"}}]}}
"""


def load_collections(db_path=None, *, min_items: int = _MIN_ITEMS) -> list[dict]:
    """내 Zotero 컬렉션 목록. 부모 경로를 붙여 중복 이름을 구분한다.

    실측상 "Industrial Trend" 처럼 **이름이 겹치는 컬렉션**이 존재하므로,
    부모가 있으면 `부모 / 자식` 으로 표기해 LLM 과 사용자 모두 구분할 수 있게 한다.
    """
    from .local_library import DEFAULT_DB
    import os
    import shutil
    import tempfile
    from pathlib import Path

    db = Path(db_path or os.environ.get("ZOTERO_SQLITE") or DEFAULT_DB)
    if not db.exists():
        return []

    tmp = None
    try:
        fd, tmp = tempfile.mkstemp(suffix=".sqlite", prefix="zotero_col_")
        os.close(fd)
        shutil.copy2(db, tmp)
        conn = sqlite3.connect(f"file:{tmp}?mode=ro", uri=True)
        rows = list(conn.execute(_COLLECTION_QUERY))
        conn.close()
    except Exception as e:  # noqa: BLE001 — 추천은 부가 기능
        logger.warning("컬렉션 목록 로드 실패: %s", str(e)[:120])
        return []
    finally:
        if tmp:
            Path(tmp).unlink(missing_ok=True)

    by_id = {cid: (name, parent, n) for cid, name, parent, n in rows}

    out = []
    for cid, (name, parent, n) in by_id.items():
        if n < min_items or name.strip().lower() in _SKIP_NAMES:
            continue
        label = name
        if parent and parent in by_id:
            label = f"{by_id[parent][0]} / {name}"
        out.append({"id": cid, "name": name, "label": label, "count": n})

    out.sort(key=lambda c: -c["count"])
    logger.info("Zotero 컬렉션 후보: %d개", len(out))
    return out


def _paper_brief(p: dict, limit: int = 900) -> str:
    """판단 재료 — 전문이 있으면 앞부분, 없으면 초록·독창성."""
    body = (p.get("abstract") or "").strip() or (p.get("originality") or "").strip()
    return f"{p.get('title', '')}\n{body[:limit]}".strip()


def recommend_collections(papers: list[dict], *,
                          collections: list[dict] | None = None,
                          keys=None, cache_dir=None,
                          progress=None) -> list[dict]:
    """논문마다 컬렉션 후보를 붙인다.

    각 논문에 다음을 추가한다 (확신이 없으면 아예 넣지 않는다):
        _suggest_collection  str  기존 컬렉션 이름
        _suggest_reason      str  한 문장 근거
        _suggest_confidence  str  high | medium | low

    실패해도 원본을 그대로 돌려준다 — 추천이 없다고 리포트가 막히면 안 된다.
    """
    from .topic_filter import llm_json

    papers = [dict(p) for p in (papers or [])]
    if not papers:
        return papers

    cols = collections if collections is not None else load_collections()
    if not cols:
        logger.info("컬렉션 추천 생략: 후보 없음")
        return papers

    valid = {c["label"]: c for c in cols}
    valid.update({c["name"]: c for c in cols})
    col_block = "\n".join(f"- {c['label']} ({c['count']}편)" for c in cols)

    total = len(papers)
    for start in range(0, total, BATCH_SIZE):
        batch = papers[start:start + BATCH_SIZE]
        end = min(start + BATCH_SIZE, total)
        if progress:
            progress("collections", f"컬렉션 추천 {start + 1}-{end}/{total}")

        block = "\n\n".join(f"[논문 {i}]\n{_paper_brief(p)}"
                            for i, p in enumerate(batch, 1))
        result = llm_json(
            _PROMPT.format(collections=col_block, papers=block),
            max_tokens=200 * len(batch), keys=keys, cache_dir=cache_dir)
        if not result or "results" not in result:
            continue

        for item in (result["results"] or []):
            idx = (item.get("paper") or 0) - 1
            if not (0 <= idx < len(batch)):
                continue
            name = str(item.get("collection") or "").strip()
            if not name:
                continue
            # **환각 방어** — 목록에 없는 이름은 버린다. 새 컬렉션을 만들라는
            # 제안은 이 기능의 범위가 아니다.
            hit = valid.get(name)
            if not hit:
                logger.debug("목록에 없는 컬렉션 제안 무시: %r", name[:40])
                continue
            batch[idx]["_suggest_collection"] = hit["label"]
            batch[idx]["_suggest_reason"] = str(item.get("reason") or "").strip()
            batch[idx]["_suggest_confidence"] = str(
                item.get("confidence") or "").strip().lower()

    n = sum(1 for p in papers if p.get("_suggest_collection"))
    logger.info("컬렉션 추천: %d/%d편", n, total)
    return papers


def summarize(papers: list[dict]) -> list[dict]:
    """추천 결과를 컬렉션별로 집계 — 리포트 요약표용."""
    agg: dict[str, dict] = {}
    for p in papers:
        name = p.get("_suggest_collection")
        if not name:
            continue
        rec = agg.setdefault(name, {"name": name, "count": 0, "titles": []})
        rec["count"] += 1
        if len(rec["titles"]) < 5:
            rec["titles"].append(p.get("title", ""))
    out = sorted(agg.values(), key=lambda r: -r["count"])
    unfiled = sum(1 for p in papers if not p.get("_suggest_collection"))
    if unfiled:
        out.append({"name": "", "count": unfiled, "titles": []})
    return out
