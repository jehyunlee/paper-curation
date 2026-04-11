"""
Paper-Curation --local --update-force 배치 실행 스크립트.

사용법:
  PYTHONUTF8=1 python run_update_force.py --topic ai4s --concurrency 4

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
import re
import shutil
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
    get_topic_dir,
)
PAPERS_DIR = str(_PAPERS_DIR)

ZOTERO_DIR = get_zotero_dir()

API_KEY = get_zotero_api_key()
USER_ID = get_zotero_user_id()
COLLECTIONS = get_collections()

# Checkpoint
CHECKPOINT_FILE = str(PIPELINE_DIR / "_update_force_checkpoint.json")


def log(msg):
    ts = datetime.now().strftime("%H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)


def load_checkpoint():
    if os.path.exists(CHECKPOINT_FILE):
        with open(CHECKPOINT_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"completed": [], "failed": [], "phase": "init"}


_cp_lock = threading.Lock()


def save_checkpoint(cp):
    with _cp_lock:
        with open(CHECKPOINT_FILE, "w", encoding="utf-8") as f:
            json.dump(cp, f, ensure_ascii=False, indent=2)


# ── Phase 1: Fetch Zotero ──

def fetch_zotero_items(collection_key):
    items = []
    start = 0
    while True:
        url = (f"https://api.zotero.org/users/{USER_ID}/collections/"
               f"{collection_key}/items/top?limit=100&start={start}&format=json&sort=title")
        req = urllib.request.Request(url, headers={"Zotero-API-Key": API_KEY})
        with urllib.request.urlopen(req, context=_ssl_ctx) as resp:
            batch = json.load(resp)
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


def find_pdf(item):
    """Find local PDF path for a Zotero item."""
    # Try children API for linked file path
    key = item["key"]
    try:
        url = f"https://api.zotero.org/users/{USER_ID}/items/{key}/children?format=json"
        req = urllib.request.Request(url, headers={"Zotero-API-Key": API_KEY})
        with urllib.request.urlopen(req, timeout=10, context=_ssl_ctx) as resp:
            children = json.load(resp)
        for c in children:
            path = c["data"].get("path", "")
            if path.endswith(".pdf"):
                if os.path.exists(path):
                    return path
                # Try under ZOTERO_DIR
                fname = os.path.basename(path)
                alt = os.path.join(ZOTERO_DIR, fname)
                if os.path.exists(alt):
                    return alt
    except Exception:
        pass

    # Fallback: fuzzy match in ZOTERO_DIR
    # Zotero filenames: "Author et al._YEAR_Title.pdf"
    title = item.get("title", "")
    if not title:
        return None
    # Normalize title for matching: take first 5 significant words
    title_words = re.sub(r"[^a-z0-9\s]", "", title.lower()).split()
    key_words = [w for w in title_words if len(w) > 3][:5]

    best_match = None
    best_score = 0
    for fname in os.listdir(ZOTERO_DIR):
        if not fname.endswith(".pdf"):
            continue
        fname_lower = fname.lower()
        score = sum(1 for w in key_words if w in fname_lower)
        if score > best_score and score >= min(3, len(key_words)):
            best_score = score
            best_match = fname

    if best_match:
        return os.path.join(ZOTERO_DIR, best_match)
    return None


# ── Phase 2: Extract text.md (OpenDataLoader → PyMuPDF fallback) ──

def extract_text(pdf_path, slug_dir):
    text_path = os.path.join(slug_dir, "text.md")

    # Strategy 1: OpenDataLoader (better table/formula/structure extraction)
    try:
        import tempfile
        from opendataloader.pdf import convert as odl_convert
        with tempfile.TemporaryDirectory() as tmpdir:
            odl_convert(input_path=[pdf_path], output_dir=tmpdir,
                        format="markdown")
            md_files = [f for f in os.listdir(tmpdir) if f.endswith(".md")]
            if md_files:
                with open(os.path.join(tmpdir, md_files[0]), "r", encoding="utf-8") as f:
                    text = f.read()
                if text and len(text) > 100:
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

def extract_figures(pdf_path, slug_dir):
    fig_dir = os.path.join(slug_dir, "figures")
    os.makedirs(fig_dir, exist_ok=True)

    try:
        import fitz
    except ImportError:
        log("  PyMuPDF not available")
        return []

    doc = fitz.open(pdf_path)
    figures = []
    MARGIN = 30
    MAX_ROUNDS = 5

    # Gemini validation function
    def validate(img_path, caption):
        try:
            from google import genai
            from google.genai import types
            client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY", ""))
            with open(img_path, "rb") as f:
                img_bytes = f.read()
            prompt = (f"Evaluate cropping of this academic figure.\nCaption: {caption}\n"
                      f"Check: (1) content CLIPPED at edges? (2) EXCESS body text?\n"
                      f"JSON only: {{\"status\":\"ok\"|\"clipped\"|\"oversized\"|\"both\","
                      f"\"issues\":\"brief\",\"adjust_pt\":{{\"top\":0,\"bottom\":0,\"left\":0,\"right\":0}}}}\n"
                      f"adjust_pt: positive=expand, negative=shrink. PDF points.")
            resp = client.models.generate_content(
                model="gemini-3-flash-preview",
                contents=[types.Part.from_bytes(data=img_bytes, mime_type="image/png"), prompt])
            text = resp.text.strip()
            if "```" in text:
                text = text.split("```")[1]
                if text.startswith("json"):
                    text = text[4:]
            return json.loads(text)
        except Exception:
            return {"status": "ok", "adjust_pt": {}}

    for pn in range(min(30, len(doc))):
        page = doc[pn]
        pw, ph = page.rect.width, page.rect.height
        text_dict = page.get_text("dict")
        txt_blocks = [b for b in text_dict["blocks"] if b["type"] == 0]
        img_blocks = [b for b in text_dict["blocks"] if b["type"] == 1
                      and (b["bbox"][2] - b["bbox"][0]) > 50
                      and (b["bbox"][3] - b["bbox"][1]) > 50]

        for tb in txt_blocks:
            first_line = tb["lines"][0] if tb["lines"] else None
            if not first_line:
                continue
            lt = "".join(s["text"] for s in first_line["spans"])
            m = re.match(r"(Figure|Fig\.?)\s*(\d+)", lt)
            if not m:
                continue
            fig_num = int(m.group(2))
            if fig_num in [int(f["name"]) for f in figures]:
                continue
            if fig_num > 5:
                continue

            cap_top = tb["bbox"][1]
            cap_bottom = tb["bbox"][3]
            caption = lt.strip()[:120]

            # Full page start
            x0, y0 = 0, 0
            x1, y1 = pw, ph

            out = os.path.join(fig_dir, f"fig{fig_num}.png")

            for rnd in range(MAX_ROUNDS + 1):
                # Try rendering with decreasing resolution on error
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

                if rnd == MAX_ROUNDS:
                    break

                result = validate(out, caption)
                if result.get("status") == "ok":
                    break

                # Round 0: educated guess
                if rnd == 0 and result.get("status") in ("oversized", "both"):
                    cap_cx = (tb["bbox"][0] + tb["bbox"][2]) / 2
                    cap_w = tb["bbox"][2] - tb["bbox"][0]
                    if cap_w < pw * 0.6:
                        if cap_cx < pw * 0.45:
                            x1 = pw * 0.52
                        elif cap_cx > pw * 0.55:
                            x0 = pw * 0.48
                    y1 = min(ph, cap_bottom + 15)
                    y0 = max(0, 40)
                    continue

                damping = [1.0, 0.8, 0.6, 0.45, 0.35][min(rnd, 4)]
                adj = result.get("adjust_pt", {})
                y0 = max(0, y0 - adj.get("top", 0) * damping)
                y1 = min(ph, y1 + adj.get("bottom", 0) * damping)
                x0 = max(0, x0 - adj.get("left", 0) * damping)
                x1 = min(pw, x1 + adj.get("right", 0) * damping)

            # Fallback
            final_ratio = (x1 - x0) * (y1 - y0) / (pw * ph)
            if final_ratio < 0.15:
                for scale in [3, 2, 1]:
                    try:
                        pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale))
                        pix.save(out)
                        break
                    except Exception:
                        continue

            figures.append({"name": str(fig_num), "page": pn, "caption": caption})

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
        client = Anthropic()

        prompt = f"""논문을 분석하고 JSON으로 리뷰 필드를 반환하세요.

제목: {title}
Abstract: {abstract}
본문 (발췌): {paper_text[:12000]}
Figure 목록:{fig_refs}

JSON 필드 (모두 한국어 서술. 단 Jargon — 기술 용어·모델명·데이터셋·알고리즘·수식·프레임워크·제품명 등 — 은 원문 그대로 유지하고 번역하지 말 것. 예: "diffusion model을 사용한다" (O), "확산 모델(diffusion model)을 사용한다" (X)):
{{
  "essence": "1-2문장 핵심 요약",
  "fig_essence": "Essence에 가장 관련된 Figure 번호 (예: 1). 없으면 0",
  "known": "알려진 것 1-2문장",
  "gap": "연구 갭 1-2문장",
  "why": "왜 중요한지 1-2문장",
  "approach": "접근법 1-2문장",
  "achievement": "성과 (마크다운 번호 목록, 각 항목 **굵은 제목**: 설명)",
  "fig_achievement": "Achievement에 관련된 Figure 번호. 없으면 0",
  "how": "방법론 (마크다운 bullet 목록)",
  "fig_how": "How에 관련된 Figure 번호. 없으면 0",
  "originality": "독창성 (마크다운 bullet 목록)",
  "limitation": "한계 + 후속연구 (마크다운 bullet 목록)",
  "novelty": 4, "tech": 3, "significance": 4, "clarity": 4, "overall": 4,
  "verdict": "총평 1-2문장"
}}

JSON만 출력. 코드 블록 없이."""

        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=3000,
            messages=[{"role": "user", "content": prompt}]
        )

        text = response.content[0].text.strip()
        if text.startswith("```"):
            text = text.split("```")[1]
            if text.startswith("json"):
                text = text[4:]
        data = json.loads(text)

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
            tech=data.get("tech", 3),
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

    # Fix placeholder URLs
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
        html = convert_review(md_path, topic, slug)
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html)
        return True
    except Exception as e:
        log(f"  html failed: {e}")
        return False


# ── Process single paper ──

def make_slug(item, existing_slugs):
    """Match item to existing slug or generate new one."""
    title = item.get("title", "Unknown")
    # Normalize for matching
    norm_title = re.sub(r"[^a-z0-9]", "", title.lower())[:40]

    # Match against existing slugs (skip number prefix)
    for s in existing_slugs:
        # Extract text part after NNN_
        parts = s.split("_", 1)
        if len(parts) < 2:
            continue
        slug_text = re.sub(r"[^a-z0-9]", "", parts[1].lower())[:40]
        if norm_title[:25] == slug_text[:25] and len(norm_title[:25]) > 10:
            return s

    # No match → new slug
    safe = "".join(c if c.isalnum() or c in " -_" else "" for c in title)[:60].strip()
    safe = safe.replace(" ", "_")
    # Find max slug number across all existing
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


def _do_process(item, slug, slug_dir, pdf_path):
    """Single attempt: text.md → figures → review.md → index.html.
    Returns (status, reason) — status is 'ok' or 'fail'."""

    # Extract text
    log(f"  {slug}: extracting text...")
    extract_text(pdf_path, slug_dir)
    text_path = os.path.join(slug_dir, "text.md")
    if not os.path.exists(text_path) or os.path.getsize(text_path) < 100:
        return "fail", "text_extraction_failed"

    # Extract figures
    log(f"  {slug}: extracting figures...")
    figures = extract_figures(pdf_path, slug_dir)
    log(f"  {slug}: {len(figures)} figures extracted")

    # Write review
    log(f"  {slug}: writing review...")
    write_review(item, slug_dir, figures)
    review_path = os.path.join(slug_dir, "review.md")
    if not os.path.exists(review_path) or os.path.getsize(review_path) < 200:
        return "fail", "review_write_failed"

    # Post-process
    fix_python_list_literals(slug_dir)
    fix_evaluation_format(slug_dir)
    fix_figure_paths(slug_dir)
    validate_review_format(slug_dir)

    # Convert to HTML
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
    pdf_path = find_pdf(item)
    if not pdf_path:
        log(f"  {slug}: no PDF found")
        with _cp_lock:
            cp["failed"].append({"slug": slug, "reason": "no_pdf"})
        save_checkpoint(cp)
        return "no_pdf"

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

def main():
    parser = argparse.ArgumentParser(description="Paper-curation --update-force batch")
    parser.add_argument("--topic", default="ai4s", help="Topic: ai4s or scisci")
    parser.add_argument("--concurrency", type=int, default=4, help="Parallel workers")
    parser.add_argument("--resume", action="store_true", help="Resume from checkpoint")
    parser.add_argument("--skip-existing", action="store_true",
                        help="Skip papers that already have review.md (for --update mode)")
    parser.add_argument("--limit", type=int, default=0, help="Limit papers (0=all)")
    parser.add_argument("--timeline", action="store_true",
                        help="Regenerate timeline images (with --resume: changed cats only, alone: all cats)")
    parser.add_argument("--category", action="store_true",
                        help="Re-run topic_modeling to reclassify all papers. Auto-enables --timeline for changed categories.")
    args = parser.parse_args()

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

    # Skip papers with existing review.md (--skip-existing or --resume)
    if args.skip_existing or args.resume:
        skipped = 0
        for item, slug in item_slug_pairs:
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
    log(f"Concurrency: {args.concurrency}")
    log(f"Estimated time: ~{len(remaining) * 5 / args.concurrency / 60:.1f} hours")

    # Process with thread pool
    start_time = time.time()
    done = 0

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
                elapsed = time.time() - start_time
                rate = elapsed / done if done else 0
                eta = rate * (len(remaining) - done) / 3600
                log(f"[{done}/{len(remaining)}] {slug}: {result} (ETA: {eta:.1f}h)")
            except Exception as e:
                log(f"[{done}/{len(remaining)}] {slug}: ERROR {e}")
                with _cp_lock:
                    cp["failed"].append({"slug": slug, "reason": str(e)})
                save_checkpoint(cp)

    elapsed_total = (time.time() - start_time) / 3600
    log(f"\nPass 1 done! {done} papers in {elapsed_total:.1f}h")
    log(f"Completed: {len(cp['completed'])}, Failed: {len(cp['failed'])}")

    # Note: per-paper auto-retry (MAX_RETRIES=3) is built into process_paper.
    # No separate retry pass needed.

    log(f"\nFinal: {len(cp['completed'])} completed, {len(cp['failed'])} failed")

    # ── Post-processing: rebuild index, classify, insights, topic page ──
    if len(cp['completed']) > 0 or args.timeline or args.category:
        log("\n" + "=" * 60)
        log("POST-PROCESSING: index → classify → summaries → insights → HTML → topic index")
        log("=" * 60)

        import subprocess
        topic = args.topic
        is_update = args.resume  # --resume implies update mode
        do_reclassify = args.category  # --category forces topic_modeling
        do_timeline_images = args.timeline or args.category  # --category auto-enables timeline

        # Identify newly processed slugs (for update mode)
        newly_completed = set(cp.get("completed", [])) - previously_completed

        def run_step(step_name, cmd, step_timeout=600):
            log(f"  [{step_name}] ...")
            try:
                result = subprocess.run(
                    cmd, cwd=str(PIPELINE_DIR.parent),
                    capture_output=True, text=True, timeout=step_timeout,
                    env={**os.environ, "PYTHONUTF8": "1"},
                )
                if result.returncode != 0:
                    log(f"  [{step_name}] FAILED (exit {result.returncode})")
                    if result.stderr:
                        log(f"    {result.stderr[:200]}")
                else:
                    out_lines = [l for l in result.stdout.strip().split("\n") if l.strip()]
                    if out_lines:
                        log(f"  [{step_name}] OK: {out_lines[-1][:100]}")
                    else:
                        log(f"  [{step_name}] OK")
            except subprocess.TimeoutExpired:
                log(f"  [{step_name}] TIMEOUT ({step_timeout}s)")
            except Exception as e:
                log(f"  [{step_name}] ERROR: {str(e)[:100]}")

        # Step 1: Always rebuild index
        run_step("build_papers_index",
                 ["python", "pipeline/build_papers_index.py", "--topic", topic])

        # Step 2: topic_modeling
        # --category: always run (reclassify all)
        # --resume without --category: skip (keep existing categories)
        # full mode: always run
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
                     ["python", "pipeline/topic_modeling.py", "--topic", topic], 1200)
        elif is_update:
            run_step("topic_modeling (coords+connections)",
                     ["python", "pipeline/topic_modeling.py", "--topic", topic, "--skip-classification"], 1200)
        else:
            run_step("topic_modeling",
                     ["python", "pipeline/topic_modeling.py", "--topic", topic], 1200)

        # Step 3: classify (always — new papers only in update mode without --category)
        run_step("classify_papers",
                 ["python", "pipeline/classify_papers.py", "--topic", topic], 600)

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

        # Step 5-6: summaries, insights, timelines — scoped by changed categories
        if do_reclassify and changed_cats:
            # --category: full reclassification → rebuild ALL summaries/insights (old cats must be purged)
            # Only timelines are scoped to changed categories
            run_step("build_category_summaries",
                     ["python", "pipeline/build_category_summaries.py", "--topic", topic], 1200)
            run_step("extract_insights",
                     ["python", "pipeline/extract_insights.py", "--topic", topic], 1800)
            cats_arg = ["--categories"] + changed_cats
            run_step("generate_timelines",
                     ["python", "pipeline/generate_timelines.py", "--topic", topic] + cats_arg, 3600)
        elif do_reclassify:
            # --category but no diff detected: full regeneration
            run_step("build_category_summaries",
                     ["python", "pipeline/build_category_summaries.py", "--topic", topic], 1200)
            run_step("extract_insights",
                     ["python", "pipeline/extract_insights.py", "--topic", topic], 1800)
            run_step("generate_timelines",
                     ["python", "pipeline/generate_timelines.py", "--topic", topic], 3600)
        elif is_update:
            if changed_cats:
                cats_arg = ["--categories"] + changed_cats
                run_step("build_category_summaries",
                         ["python", "pipeline/build_category_summaries.py", "--topic", topic] + cats_arg, 1200)
                run_step("extract_insights",
                         ["python", "pipeline/extract_insights.py", "--topic", topic] + cats_arg, 1800)
                tl_cmd = ["python", "pipeline/generate_timelines.py", "--topic", topic] + cats_arg
                if not do_timeline_images:
                    tl_cmd.append("--narrative-only")
                run_step("generate_timelines", tl_cmd, 3600)
            else:
                log("  [summaries/insights/timelines] SKIP (no new papers classified)")
        elif do_timeline_images:
            # --timeline alone (no --resume): full regeneration of all narratives + images
            run_step("build_category_summaries",
                     ["python", "pipeline/build_category_summaries.py", "--topic", topic], 1200)
            run_step("extract_insights",
                     ["python", "pipeline/extract_insights.py", "--topic", topic], 1800)
            run_step("generate_timelines",
                     ["python", "pipeline/generate_timelines.py", "--topic", topic], 3600)
        else:
            # Full mode (no --resume, no --timeline)
            run_step("build_category_summaries",
                     ["python", "pipeline/build_category_summaries.py", "--topic", topic], 1200)
            run_step("extract_insights",
                     ["python", "pipeline/extract_insights.py", "--topic", topic], 1800)
            run_step("generate_timelines",
                     ["python", "pipeline/generate_timelines.py", "--topic", topic], 3600)

        # Step 7-10: Always run (fast steps)
        run_step("inject_frontmatter",
                 ["python", "pipeline/inject_frontmatter.py", "--topic", topic], 600)
        run_step("generate_moc",
                 ["python", "pipeline/generate_moc.py", "--topic", topic], 600)
        run_step("generate_network",
                 ["python", "pipeline/generate_network.py", "--topic", topic], 600)

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
                         ["python", "pipeline/topic_modeling.py", "--topic", topic, "--skip-connections"], 1200)
                run_step("generate_network (rebuild)",
                         ["python", "pipeline/generate_network.py", "--topic", topic], 600)
            else:
                log(f"  [verify_umap] OK: all {len(topic_slugs)} papers have coordinates")
        except Exception as e:
            log(f"  [verify_umap] WARNING: verification failed ({str(e)[:100]})")

        run_step("review_to_html",
                 ["python", "pipeline/review_to_html.py", "--all"], 600)
        run_step("build_topic_index",
                 ["python", "pipeline/build_topic_index.py", topic], 600)

        # Deep Research search index (section-aware chunks + OpenAI embeddings).
        # Reads OPENAI_API_KEY from env or config.json; fails fast if missing.
        run_step("build_search_index",
                 ["python", "pipeline/build_search_index.py", "--topic", topic], 900)

        # Deploy if GitHub config exists
        from config_loader import get_github_repo
        if get_github_repo():
            log("\n  [prepare_deploy] GitHub config found, deploying...")
            try:
                result = subprocess.run(
                    ["python", "pipeline/prepare_deploy.py", "--topic", topic, "--push"],
                    cwd=str(PIPELINE_DIR.parent),
                    capture_output=True, text=True, timeout=600,
                    env={**os.environ, "PYTHONUTF8": "1"},
                )
                if result.returncode == 0:
                    log(f"  [prepare_deploy] OK: deployed to gh-pages")
                else:
                    log(f"  [prepare_deploy] FAILED (exit {result.returncode})")
                    if result.stderr:
                        log(f"    {result.stderr[:200]}")
            except Exception as e:
                log(f"  [prepare_deploy] ERROR: {str(e)[:100]}")
        else:
            log("\n  [prepare_deploy] SKIP: no github config in config.json")

        log("\nPost-processing complete!")


if __name__ == "__main__":
    main()
