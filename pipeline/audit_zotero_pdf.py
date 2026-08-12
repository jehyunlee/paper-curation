"""
Zotero 서지정보 ↔ 첨부 PDF 정합성 감사.

배경: dedup_text / audit_matching 은 *로컬 docs/papers* 산출물(review.md / text.md)
을 본다. 이 스크립트는 그 **상류**인 Zotero 컬렉션 자체를 본다 — 서지 항목(메타데이터)
과 거기 붙은 PDF 파일이 실제로 같은 논문인지, 한 항목에 PDF 가 여러 개 붙지는 않았는지,
같은 논문이 여러 항목으로 중복 등록되지는 않았는지를 교차검증한다.

검사 플래그 (한 항목에 여러 개 동시 가능):
  - NO_PDF            : top-level 항목에 PDF 첨부가 0개
  - MULTI_PDF         : PDF 첨부가 2개 이상 (어느 게 맞는지 모호)
  - FILENAME_MISMATCH : 첨부 PDF 파일명의 토큰이 서지 제목 토큰과 거의 안 겹침
  - CONTENT_MISMATCH  : PDF 1페이지 본문에 제목 핵심어/DOI/arXiv-id 가 안 나타남
                        (= 엉뚱한 PDF 가 붙은 것; 파일이 디스크에 있어야 판정)
  - CONTENT_UNCHECKED : 파일을 못 찾거나 못 열어서 내용 판정 불가
  - DUPLICATE         : 같은 제목60/DOI/arXiv-id 를 공유하는 다른 항목이 존재

PDF 경로 해석은 run_update_force.find_pdf 와 같은 규약을 따른다:
  data.path 가 "attachments:<name>" → ZOTERO_DIR/<name>
  절대경로면 그대로, 아니면 basename 을 ZOTERO_DIR 아래에서 탐색.

Usage:
  PYTHONUTF8=1 python pipeline/audit_zotero_pdf.py --topic scisci
  PYTHONUTF8=1 python pipeline/audit_zotero_pdf.py --topic ai4s --no-content   # 내용검사 skip(빠름)
  PYTHONUTF8=1 python pipeline/audit_zotero_pdf.py --all                       # 설정된 전 컬렉션

출력:
  docs/{topic}/_zotero_pdf_audit.json   (토픽별 상세)
  pipeline/_logs/zotero_pdf_audit.md    (사람이 읽는 통합 표)
"""

import argparse
import json
import os
import re
import sys
import time
import urllib.request
import urllib.parse
import urllib.error
from collections import defaultdict
from datetime import datetime
from pathlib import Path, PureWindowsPath

from config_loader import (
    get_zotero_api_key,
    get_zotero_user_id,
    get_collection_key,
    get_collections,
    get_topic_dir,
    get_zotero_dir,
    PROJECT_ROOT,
    _ssl_ctx,
)

API_KEY = get_zotero_api_key()
USER_ID = get_zotero_user_id()
ZOTERO_DIR = get_zotero_dir()
LOGS_DIR = PROJECT_ROOT / "pipeline" / "_logs"

# 제목/파일명 토큰화 시 무시할 흔한 단어
_STOP = {
    "the", "a", "an", "of", "for", "and", "or", "to", "in", "on", "with", "via",
    "via", "from", "using", "use", "toward", "towards", "into", "by", "at", "as",
    "is", "are", "be", "based", "approach", "study", "paper", "arxiv", "preprint",
    "pdf", "supplementary", "supplement", "appendix", "final", "draft", "v1", "v2",
    "v3", "manuscript", "main", "full", "accepted", "camera", "ready", "copy",
}


# ── Zotero API ────────────────────────────────────────────────────────────────

def _api(endpoint, params=None, retries=4):
    base = f"https://api.zotero.org/users/{USER_ID}/{endpoint}"
    if params:
        base += "?" + urllib.parse.urlencode(params)
    headers = {"Zotero-API-Key": API_KEY, "User-Agent": "paper-curation-audit/1.0"}
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(base, headers=headers)
            with urllib.request.urlopen(req, timeout=30, context=_ssl_ctx) as resp:
                raw = resp.read()
                return json.loads(raw.decode("utf-8")) if raw else []
        except Exception as e:  # noqa: BLE001 - transient network/429
            last = e
            time.sleep(1.5 * (attempt + 1))
    raise last


def list_collection_items(collection_key):
    items, start = [], 0
    while True:
        batch = _api(f"collections/{collection_key}/items/top",
                     params={"limit": 100, "start": start, "format": "json"})
        if not batch:
            break
        items.extend(batch)
        if len(batch) < 100:
            break
        start += 100
        time.sleep(0.4)
    return items


def list_children(item_key):
    try:
        return _api(f"items/{item_key}/children", params={"format": "json"})
    except Exception:
        return []


def _api_patch(item_key, fields, version):
    """PATCH 부분 업데이트 (지정 필드만). If-Unmodified-Since-Version 필수."""
    url = f"https://api.zotero.org/users/{USER_ID}/items/{item_key}"
    body = json.dumps(fields).encode("utf-8")
    headers = {
        "Zotero-API-Key": API_KEY,
        "User-Agent": "paper-curation-audit/1.0",
        "Content-Type": "application/json",
        "If-Unmodified-Since-Version": str(version),
    }
    req = urllib.request.Request(url, data=body, method="PATCH", headers=headers)
    with urllib.request.urlopen(req, timeout=30, context=_ssl_ctx) as resp:
        return resp.status


# ── Normalizers / tokenizers ──────────────────────────────────────────────────

def norm_title(title):
    return re.sub(r"[^a-z0-9]", "", (title or "").lower())[:60]


def norm_doi(doi):
    return re.sub(r"[^a-z0-9]", "", (doi or "").lower())


def extract_arxiv_id(data):
    for field in ("url", "DOI", "extra", "archiveID", "title"):
        v = data.get(field, "") or ""
        m = re.search(r"(\d{4}\.\d{4,5})", v)
        if m:
            return m.group(1)
    return ""


def tokens(text):
    """알파벳·숫자 토큰(>=4자 또는 숫자) 집합, 스톱워드 제거."""
    raw = re.findall(r"[a-z0-9]+", (text or "").lower())
    out = set()
    for t in raw:
        if t in _STOP:
            continue
        if len(t) >= 4 or t.isdigit():
            out.add(t)
    return out


# ── PDF path resolution (find_pdf 와 동일 규약) ────────────────────────────────

def resolve_pdf_path(att_data):
    """attachment data → 디스크 경로(Path) 또는 None."""
    path = att_data.get("path", "") or ""
    filename = att_data.get("filename", "") or ""
    zdir = Path(ZOTERO_DIR) if ZOTERO_DIR else None

    if path.startswith("attachments:"):
        rel = path[len("attachments:"):]
        if zdir:
            cand = zdir / rel
            if cand.exists():
                return cand
            # basename 탐색
            base = os.path.basename(rel)
            if (zdir / base).exists():
                return zdir / base
        return None
    if path:
        p = Path(path)
        if p.is_absolute() and p.exists():
            return p
        # 라이브러리를 두 대에서 쓰면 linked_file 이 다른 OS 의 절대경로로 남는다
        # ("C:\\Users\\...\\Zotero\\Foo.pdf"). POSIX 의 os.path.basename 은
        # 백슬래시를 구분자로 보지 않아 경로 전체를 파일명으로 돌려주고, 그래서
        # 1,025편이 "파일 없음" 으로 집계됐다. 두 구분자 모두에서 잘라낸다.
        base = PureWindowsPath(path.replace("\\", "/")).name
        if zdir and (zdir / base).exists():
            return zdir / base
    if filename and zdir and (zdir / filename).exists():
        return zdir / filename
    return None


def pdf_first_page_text(pdf_path, max_pages=3, max_chars=8000):
    """앞 max_pages 페이지 텍스트를 이어붙여 반환.

    제목/초록이 표지 다음 페이지로 넘어가거나(학회 초록 모음집에서는 한 초록이
    2~3페이지째 등장) 첫 페이지가 표지인 경우를 흡수하기 위해 한 페이지만 보지
    않는다. 비용은 앞 몇 페이지뿐이라 무시할 만하다.
    """
    try:
        import fitz  # PyMuPDF
    except ImportError:
        return None
    try:
        doc = fitz.open(str(pdf_path))
        n = len(doc)
        if n == 0:
            doc.close()
            return ""
        parts = []
        for i in range(min(max_pages, n)):
            parts.append(doc[i].get_text() or "")
            if sum(len(p) for p in parts) >= max_chars:
                break
        doc.close()
        return ("\n".join(parts))[:max_chars]
    except Exception:
        return None


# ── 항목 단위 감사 ─────────────────────────────────────────────────────────────

def audit_item(item, *, check_content=True):
    d = item.get("data", {})
    title = d.get("title", "") or ""
    doi = d.get("DOI", "") or ""
    arxiv = extract_arxiv_id(d)
    children = item.get("_children", [])
    pdfs = [c for c in children
            if c.get("data", {}).get("itemType") == "attachment"
            and c.get("data", {}).get("contentType") == "application/pdf"]

    flags = []
    detail = {}

    if not pdfs:
        flags.append("NO_PDF")
    if len(pdfs) >= 2:
        flags.append("MULTI_PDF")
        detail["pdf_filenames"] = [
            (c.get("data", {}).get("filename")
             or os.path.basename(c.get("data", {}).get("path", "") or "")
             or "?")
            for c in pdfs
        ]

    title_tok = tokens(title)
    # 대표 PDF(첫 번째)로 파일명/내용 검사
    fn_mismatch = None
    content_state = None
    if pdfs:
        primary = pdfs[0].get("data", {})
        fname = primary.get("filename") or os.path.basename(primary.get("path", "") or "")
        detail["primary_pdf"] = fname
        # 파일명 토큰 vs 제목 토큰
        fname_stem = re.sub(r"\.pdf$", "", fname or "", flags=re.I)
        fn_tok = tokens(fname_stem)
        if title_tok and fn_tok:
            overlap = len(title_tok & fn_tok) / max(1, len(title_tok))
            detail["filename_overlap"] = round(overlap, 2)
            # arXiv id 파일명(예 2506.13784.pdf)은 토큰이 안 겹쳐도 정상 → arxiv 매치면 면제
            arxiv_in_fname = arxiv and arxiv in fname
            if overlap < 0.25 and not arxiv_in_fname:
                flags.append("FILENAME_MISMATCH")
                fn_mismatch = True
        # 내용 검사
        if check_content:
            ppath = resolve_pdf_path(primary)
            if ppath is None:
                flags.append("CONTENT_UNCHECKED")
                content_state = "no_file"
            else:
                text = pdf_first_page_text(ppath)
                if text is None:
                    flags.append("CONTENT_UNCHECKED")
                    content_state = "unreadable"
                    detail["content_uncheck_reason"] = "unreadable"
                else:
                    # 비교 가능한 영문 본문이 충분한지 먼저 가늠한다. 스캔/벡터
                    # 표지(추출 0자)나 비라틴(러시아어 등, 영문 제목은 번역본)
                    # 은 영문 제목 토큰과 본질적으로 대조 불가 → mismatch 가
                    # 아니라 '판정 불가'로 분류해야 false positive 를 막는다.
                    latin_words = re.findall(r"[a-z]{3,}", text.lower())
                    latin_letters = len(re.findall(r"[a-zA-Z]", text))
                    # Cyrillic/CJK/Hangul/Greek/Arabic 등 비라틴 표기 문자 수.
                    # 본문이 비라틴 표기 우세면 영문 제목(번역)과 대조 불가.
                    other_script = len(re.findall(
                        r"[Ͱ-ϿЀ-ӿ֐-׿؀-ۿ"
                        r"぀-ヿ㐀-鿿가-힣]", text))
                    if len(latin_words) < 30 or other_script > latin_letters:
                        flags.append("CONTENT_UNCHECKED")
                        content_state = ("no_text" if len(text.strip()) < 40
                                         else "non_latin")
                        detail["content_uncheck_reason"] = content_state
                        detail["content_latin_words"] = len(latin_words)
                        detail["content_other_script"] = other_script
                    else:
                        body_tok = tokens(text)
                        norm_text = re.sub(r"[^a-z0-9]", "", text.lower())
                        doi_hit = bool(doi) and norm_doi(doi) in norm_text
                        arxiv_hit = bool(arxiv) and arxiv.replace(".", "") in norm_text
                        title_hit = 0.0
                        if title_tok:
                            title_hit = len(title_tok & body_tok) / len(title_tok)
                        detail["content_title_overlap"] = round(title_hit, 2)
                        detail["content_doi_hit"] = doi_hit
                        detail["content_arxiv_hit"] = arxiv_hit
                        # 명시 신호(DOI/arXiv) 없고 제목 키워드도 거의 없으면 mismatch
                        if not doi_hit and not arxiv_hit and title_hit < 0.30:
                            flags.append("CONTENT_MISMATCH")
                            content_state = "mismatch"
                        else:
                            content_state = "ok"

    return {
        "key": item["key"],
        "title": title[:140],
        "doi": doi,
        "arxiv": arxiv,
        "n_pdf": len(pdfs),
        "flags": flags,
        "detail": detail,
    }


# ── 중복 그룹 (title60 / DOI / arxiv) ──────────────────────────────────────────

def find_duplicate_groups(items):
    parent = {}

    def find(x):
        while parent.get(x, x) != x:
            parent[x] = parent.get(parent[x], parent[x])
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    for it in items:
        parent.setdefault(it["key"], it["key"])

    for key_type in ("title", "doi", "arxiv"):
        bucket = defaultdict(list)
        for it in items:
            d = it.get("data", {})
            if key_type == "title":
                k = norm_title(d.get("title", ""))
            elif key_type == "doi":
                k = norm_doi(d.get("DOI", ""))
            else:
                k = extract_arxiv_id(d)
            if k and len(k) >= 8:
                bucket[k].append(it["key"])
        for keys in bucket.values():
            for other in keys[1:]:
                union(keys[0], other)

    groups = defaultdict(list)
    for it in items:
        groups[find(it["key"])].append(it["key"])
    return {root: keys for root, keys in groups.items() if len(keys) > 1}


# ── 토픽 1개 감사 ──────────────────────────────────────────────────────────────

def audit_topic(topic, *, check_content=True, sleep=0.3):
    ck = get_collection_key(topic)
    if not ck:
        print(f"  ! collection for '{topic}' not configured — skip", file=sys.stderr)
        return None
    print(f"[{datetime.now():%H:%M:%S}] {topic}: fetching items ({ck})...")
    items = list_collection_items(ck)
    print(f"  {len(items)} top-level items; fetching children...")
    t0 = time.time()
    for i, it in enumerate(items, 1):
        it["_children"] = list_children(it["key"])
        if i % 50 == 0 or i == len(items):
            print(f"  [{i}/{len(items)}] {time.time()-t0:.0f}s")
        time.sleep(sleep)

    dup_groups = find_duplicate_groups(items)
    key_to_dupgroup = {}
    for gi, (root, keys) in enumerate(dup_groups.items(), 1):
        for k in keys:
            key_to_dupgroup[k] = gi

    print(f"  auditing {len(items)} items (content={'on' if check_content else 'off'})...")
    rows = []
    for it in items:
        r = audit_item(it, check_content=check_content)
        if it["key"] in key_to_dupgroup:
            r["flags"].append("DUPLICATE")
            r["dup_group"] = key_to_dupgroup[it["key"]]
        rows.append(r)

    # 요약
    flagged = [r for r in rows if any(f != "CONTENT_UNCHECKED" for f in r["flags"])]
    by_flag = defaultdict(int)
    for r in rows:
        for f in r["flags"]:
            by_flag[f] += 1

    report = {
        "topic": topic,
        "collection_key": ck,
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "total_items": len(items),
        "content_checked": check_content,
        "flag_counts": dict(by_flag),
        "duplicate_groups": [
            {"group": gi, "keys": keys}
            for gi, (root, keys) in enumerate(dup_groups.items(), 1)
        ],
        "rows": rows,
    }
    out = get_topic_dir(topic) / "_zotero_pdf_audit.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    try:
        from lib.atomic_io import atomic_write_json
        atomic_write_json(out, report)
    except Exception:
        with open(out, "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=1)
    print(f"  -> {out}  | flagged {len(flagged)}/{len(items)}  flags={dict(by_flag)}")
    return report


# ── 통합 마크다운 표 ───────────────────────────────────────────────────────────

_FLAG_ORDER = ["CONTENT_MISMATCH", "FILENAME_MISMATCH", "MULTI_PDF",
               "DUPLICATE", "NO_PDF", "CONTENT_UNCHECKED"]


def write_markdown(reports):
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    md = LOGS_DIR / "zotero_pdf_audit.md"
    lines = ["# Zotero 서지정보 ↔ PDF 정합성 감사",
             f"\n생성: {datetime.now():%Y-%m-%d %H:%M}\n"]

    # 요약 표
    lines.append("## 요약\n")
    lines.append("| topic | items | CONTENT_MISMATCH | FILENAME_MISMATCH | MULTI_PDF | DUPLICATE | NO_PDF | UNCHECKED |")
    lines.append("|---|--:|--:|--:|--:|--:|--:|--:|")
    for rep in reports:
        if not rep:
            continue
        fc = rep["flag_counts"]
        lines.append(
            f"| {rep['topic']} | {rep['total_items']} | "
            f"{fc.get('CONTENT_MISMATCH',0)} | {fc.get('FILENAME_MISMATCH',0)} | "
            f"{fc.get('MULTI_PDF',0)} | {fc.get('DUPLICATE',0)} | "
            f"{fc.get('NO_PDF',0)} | {fc.get('CONTENT_UNCHECKED',0)} |")

    # 토픽별 상세 (실질 이슈만 — CONTENT_UNCHECKED 단독은 제외)
    for rep in reports:
        if not rep:
            continue
        # NO_PDF 는 인용용 reference 항목이 대부분이라 상세 표에서 제외(요약엔 카운트 유지).
        # 사용자 관심사: 잘못 붙은 PDF(MISMATCH) / 중복(DUPLICATE) / 다중 PDF(MULTI_PDF).
        actionable = [r for r in rep["rows"]
                      if any(f in ("CONTENT_MISMATCH", "FILENAME_MISMATCH",
                                   "MULTI_PDF", "DUPLICATE")
                             for f in r["flags"])]
        if not actionable:
            continue
        lines.append(f"\n## {rep['topic']} — {len(actionable)}건\n")
        lines.append("| key | title | n_pdf | flags | 근거 |")
        lines.append("|---|---|--:|---|---|")
        # 심각도 정렬
        def sev(r):
            return min([_FLAG_ORDER.index(f) for f in r["flags"]
                        if f in _FLAG_ORDER] or [99])
        for r in sorted(actionable, key=sev):
            d = r["detail"]
            ev = []
            if "content_title_overlap" in d:
                ev.append(f"내용제목겹침 {d['content_title_overlap']}")
            if d.get("content_doi_hit"):
                ev.append("DOI매치")
            if d.get("content_arxiv_hit"):
                ev.append("arXiv매치")
            if "filename_overlap" in d:
                ev.append(f"파일명겹침 {d['filename_overlap']}")
            if "primary_pdf" in d:
                ev.append(f"`{d['primary_pdf'][:50]}`")
            if "pdf_filenames" in d:
                ev.append("PDFs: " + ", ".join(f"`{x[:30]}`" for x in d["pdf_filenames"]))
            dup = f" g{r['dup_group']}" if r.get("dup_group") else ""
            flags = ",".join(f + (dup if f == "DUPLICATE" else "") for f in r["flags"])
            title = (r["title"] or "").replace("|", "\\|")[:70]
            lines.append(f"| {r['key']} | {title} | {r['n_pdf']} | {flags} | {'; '.join(ev)} |")

    md.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"\n[md] {md}")
    return md


def clear_arxiv_ids(keys, *, execute=False):
    """주어진 Zotero 항목들에서 (잘못 박힌) arXiv 식별자를 외과적으로 제거.

    arXiv-ID collision(서로 다른 논문이 같은 arXiv id 공유) 교정용. 한쪽 항목의
    id 만 비워 find_pdf 가 DOI/제목 매칭으로 안전하게 떨어지게 한다. 비우는 위치:
      - url        : arxiv.org/abs/<id> 형태면 ""
      - archiveID  : "arXiv:<id>" 면 ""
      - extra      : "arXiv:<id>" 라인 제거
      - title      : 제목 끝에 인용문 찌꺼기("... arXiv preprint arXiv:<id>, year.")
                     가 붙어 있으면 그 부분만 절단
    DOI/저자/날짜 등 정당한 메타데이터는 건드리지 않는다. dry-run 기본, --execute 로 적용.
    """
    for k in keys:
        it = _api(f"items/{k}", params={"format": "json"})
        d = it.get("data", {})
        ver = it.get("version")
        aid = extract_arxiv_id(d)
        if not aid:
            print(f"  {k}: arXiv id 없음 — skip")
            continue
        esc = re.escape(aid)
        fields = {}
        url = d.get("url", "") or ""
        if aid in url and "arxiv.org" in url.lower():
            fields["url"] = ""
        arch = d.get("archiveID", "") or ""
        if aid in arch:
            fields["archiveID"] = ""
        extra = d.get("extra", "") or ""
        if aid in extra:
            kept = [ln for ln in extra.splitlines()
                    if not re.search(r"arxiv:\s*" + esc, ln, re.I)]
            fields["extra"] = "\n".join(kept)
        title = d.get("title", "") or ""
        if aid in title:
            new_t = re.sub(r"\s*(arxiv\s+preprint\s+)?arxiv:\s*" + esc + r".*$",
                           "", title, flags=re.I).rstrip()
            if new_t and new_t != title:
                fields["title"] = new_t
        if not fields:
            print(f"  {k}: arXiv {aid} 발견했으나 안전 절단 위치 불명 — 수동 확인 필요")
            continue
        print(f"  {k}: clear arXiv {aid} -> change {list(fields.keys())}")
        for f, v in fields.items():
            old = d.get(f, "")
            print(f"      {f}: {old!r} -> {v!r}")
        if execute:
            try:
                st = _api_patch(k, fields, ver)
                print(f"      PATCH ok (HTTP {st})")
            except Exception as e:  # noqa: BLE001
                print(f"      PATCH FAIL: {e}")
        time.sleep(0.3)


def load_existing_reports():
    """디스크의 토픽별 _zotero_pdf_audit.json 을 전부 읽어 통합 md 재료로."""
    out = []
    for t in get_collections().keys():
        p = get_topic_dir(t) / "_zotero_pdf_audit.json"
        if p.exists():
            try:
                out.append(json.load(open(p, encoding="utf-8")))
            except Exception:
                pass
    return out


def main():
    ap = argparse.ArgumentParser(description="Zotero 서지정보↔PDF 정합성 감사")
    ap.add_argument("--topic", help="단일 토픽")
    ap.add_argument("--topics", help="콤마구분 다중 토픽 (예: scisci,ai4s)")
    ap.add_argument("--all", action="store_true", help="설정된 전 컬렉션")
    ap.add_argument("--combine-only", action="store_true",
                    help="새 감사 없이 디스크의 토픽별 JSON 만으로 통합 md 재생성")
    ap.add_argument("--clear-arxiv",
                    help="콤마구분 항목키에서 (잘못된) arXiv id 제거 (collision 교정)")
    ap.add_argument("--execute", action="store_true",
                    help="--clear-arxiv 실제 적용 (기본 dry-run)")
    ap.add_argument("--no-content", action="store_true",
                    help="PDF 내용 검사 skip (파일명/중복만, 빠름)")
    ap.add_argument("--sleep", type=float, default=0.3)
    args = ap.parse_args()

    if args.clear_arxiv:
        keys = [k.strip() for k in args.clear_arxiv.split(",") if k.strip()]
        print(f"{'EXECUTE' if args.execute else 'DRY-RUN'} clear arXiv id on {len(keys)} item(s):")
        clear_arxiv_ids(keys, execute=args.execute)
        if not args.execute:
            print("\n(dry-run) --execute 로 실제 적용.")
        return

    if args.combine_only:
        write_markdown(load_existing_reports())
        return

    if args.all:
        topics = list(get_collections().keys())
    elif args.topics:
        topics = [t.strip() for t in args.topics.split(",") if t.strip()]
    elif args.topic:
        topics = [args.topic]
    else:
        ap.error("--topic / --topics / --all / --combine-only 중 하나 필요")

    for t in topics:
        audit_topic(t, check_content=not args.no_content, sleep=args.sleep)

    # 통합 md 는 방금 돈 토픽뿐 아니라 디스크의 모든 토픽 JSON 을 모아 만든다.
    write_markdown(load_existing_reports())


if __name__ == "__main__":
    main()
