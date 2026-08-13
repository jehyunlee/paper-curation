"""Batch register papers 111-507 from awesome-humanoid CSV to Zotero Humanoid collection.

일회성 마이그레이션 스크립트(보관용). 자격증명·계정 식별자·로컬 경로는 전부
환경변수에서만 읽는다 — 이 파일에 Zotero API key 가 하드코딩돼 있다가 public
master 로 유출된 적이 있다(2026-08-13). 상수로 되돌리지 말 것.

실행 예::

    export ZOTERO_API_KEY=...            # 필수
    export ZOTERO_USER_ID=...            # 필수
    export ZOTERO_COLLECTION_KEY=...     # 필수 (대상 컬렉션)
    export ZOTERO_DIR=/path/to/pdfs      # 필수 (PDF 저장 위치)
    export BATCH_CSV_PATH=/path/to/awesome-humanoid-robot-learning.csv
"""
import csv, json, os, re, sys, time, urllib.request, xml.etree.ElementTree as ET
from pathlib import Path
from pyzotero import zotero


def _require_env(name):
    """비밀값·계정 식별자는 환경변수에만 존재한다. 없으면 즉시 중단."""
    value = os.environ.get(name, "").strip()
    if not value:
        sys.exit(
            f"{name} 환경변수가 필요합니다. 이 스크립트는 자격증명을 "
            f"소스코드나 config.json 에서 읽지 않습니다."
        )
    return value


API_KEY = _require_env("ZOTERO_API_KEY")
USER_ID = _require_env("ZOTERO_USER_ID")
COLLECTION_KEY = _require_env("ZOTERO_COLLECTION_KEY")
PDF_DIR = Path(_require_env("ZOTERO_DIR"))
CSV_PATH = Path(_require_env("BATCH_CSV_PATH"))

zot = zotero.Zotero(USER_ID, "user", API_KEY)
NS = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}

def parse_author(name):
    parts = name.strip().split()
    if len(parts) == 1:
        return "", parts[0]
    return " ".join(parts[:-1]), parts[-1]

def make_filename(authors, year, title):
    last_names = [parse_author(a)[1] for a in authors[:3]]
    if len(authors) == 1:
        prefix = last_names[0]
    elif len(authors) == 2:
        prefix = f"{last_names[0]} and {last_names[1]}"
    else:
        prefix = f"{last_names[0]} et al"
    clean = re.sub(r'[:\\/?"*<>|]', '', title)[:50].strip()
    return f"{prefix}_{year}_{clean}.pdf"

def extract_arxiv_id(url):
    m = re.search(r'arxiv\.org/(?:abs|pdf|html)/(\d+\.\d+)', url)
    if m:
        return m.group(1)
    m = re.search(r'arxiv\.org/abs/(\d+\.\d+)', url)
    return m.group(1) if m else None

def fetch_arxiv_metadata(arxiv_ids):
    """Batch fetch metadata for up to 50 arXiv IDs."""
    id_list = ",".join(arxiv_ids)
    url = f"http://export.arxiv.org/api/query?id_list={id_list}&max_results={len(arxiv_ids)}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        tree = ET.parse(resp)
    root = tree.getroot()
    results = {}
    for entry in root.findall("atom:entry", NS):
        eid = entry.find("atom:id", NS).text
        aid = re.search(r'(\d+\.\d+)', eid)
        if not aid:
            continue
        aid = aid.group(1)
        title = entry.find("atom:title", NS).text.strip().replace("\n", " ")
        abstract = (entry.find("atom:summary", NS).text or "").strip().replace("\n", " ")
        published = entry.find("atom:published", NS).text[:10]
        authors = [a.find("atom:name", NS).text for a in entry.findall("atom:author", NS)]
        cat = entry.find("arxiv:primary_category", NS)
        cat = cat.attrib.get("term", "") if cat is not None else ""
        results[aid] = {
            "title": title, "abstract": abstract, "date": published,
            "year": published[:4], "authors": authors, "category": cat,
        }
    return results

def download_pdf(arxiv_id, authors, year, title):
    filename = make_filename(authors, year, title)
    pdf_path = PDF_DIR / filename
    if pdf_path.exists():
        return pdf_path, filename
    try:
        url = f"https://arxiv.org/pdf/{arxiv_id}"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=60) as resp:
            pdf_path.write_bytes(resp.read())
        return pdf_path, filename
    except Exception as e:
        print(f"    PDF download failed: {e}")
        return None, filename

def is_duplicate(title):
    try:
        existing = zot.items(q=title[:50], limit=5)
        return any(title.lower() == e["data"].get("title", "").lower() for e in existing)
    except Exception:
        return False

# --- Load CSV ---
papers = []
with open(CSV_PATH, "r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
        no = int(row["no."])
        if 111 <= no <= 507:
            papers.append({"no": no, "title": row["title"], "url": row["URL"]})

print(f"Total papers to process: {len(papers)}")

# --- Separate arXiv vs non-arXiv ---
arxiv_papers = []
other_papers = []
for p in papers:
    aid = extract_arxiv_id(p["url"])
    if aid:
        p["arxiv_id"] = aid
        arxiv_papers.append(p)
    else:
        other_papers.append(p)

print(f"arXiv: {len(arxiv_papers)}, other: {len(other_papers)}")

# --- Phase 1: Batch fetch arXiv metadata ---
print("\n=== Fetching arXiv metadata ===")
BATCH = 40
all_meta = {}
arxiv_ids = [p["arxiv_id"] for p in arxiv_papers]
for i in range(0, len(arxiv_ids), BATCH):
    batch = arxiv_ids[i:i+BATCH]
    print(f"  Batch {i//BATCH+1}: {len(batch)} papers...")
    meta = fetch_arxiv_metadata(batch)
    all_meta.update(meta)
    time.sleep(1)
print(f"  Metadata fetched: {len(all_meta)}")

# --- Phase 2: Register arXiv papers ---
print("\n=== Registering arXiv papers ===")
ok_count = 0
skip_count = 0
fail_count = 0

for p in arxiv_papers:
    aid = p["arxiv_id"]
    no = p["no"]
    meta = all_meta.get(aid)
    if not meta:
        print(f"[{no}] SKIP: no metadata for {aid}")
        skip_count += 1
        continue

    title = meta["title"]
    if is_duplicate(title):
        print(f"[{no}] DUP: {title[:60]}")
        skip_count += 1
        continue

    # Download PDF
    pdf_path, filename = download_pdf(aid, meta["authors"], meta["year"], title)

    # Create Zotero item
    creators = []
    for a in meta["authors"]:
        first, last = parse_author(a)
        creators.append({"creatorType": "author", "firstName": first, "lastName": last})

    item = {
        "itemType": "preprint",
        "title": title,
        "abstractNote": meta["abstract"][:5000],
        "date": meta["date"],
        "url": f"https://arxiv.org/abs/{aid}",
        "repository": "arXiv",
        "archiveID": aid,
        "creators": creators,
        "tags": [{"tag": meta["category"]}] if meta["category"] else [],
        "collections": [COLLECTION_KEY],
    }
    try:
        result = zot.create_items([item])
        if "0" not in result["successful"]:
            print(f"[{no}] FAIL: {result.get('failed', result)}")
            fail_count += 1
            continue
        parent_key = result["successful"]["0"]["key"]

        # Link PDF
        if pdf_path and pdf_path.exists():
            attach = [{
                "itemType": "attachment",
                "parentItem": parent_key,
                "linkMode": "linked_file",
                "title": filename,
                "contentType": "application/pdf",
                "path": str(pdf_path),
                "tags": [],
            }]
            zot.create_items(attach)

        print(f"[{no}] OK: {parent_key} - {title[:55]}")
        ok_count += 1
    except Exception as e:
        print(f"[{no}] ERROR: {e}")
        fail_count += 1
    time.sleep(0.3)

# --- Phase 3: Register non-arXiv papers as webpage ---
print(f"\n=== Registering {len(other_papers)} non-arXiv papers ===")
for p in other_papers:
    no = p["no"]
    title = p["title"]

    if is_duplicate(title):
        print(f"[{no}] DUP: {title[:60]}")
        skip_count += 1
        continue

    item = {
        "itemType": "webpage",
        "title": title,
        "url": p["url"],
        "websiteTitle": "Project Page",
        "date": "",
        "collections": [COLLECTION_KEY],
        "tags": [{"tag": "non-arxiv"}],
    }
    try:
        result = zot.create_items([item])
        if "0" in result["successful"]:
            key = result["successful"]["0"]["key"]
            print(f"[{no}] OK (web): {key} - {title[:55]}")
            ok_count += 1
        else:
            print(f"[{no}] FAIL: {result.get('failed', result)}")
            fail_count += 1
    except Exception as e:
        print(f"[{no}] ERROR: {e}")
        fail_count += 1
    time.sleep(0.3)

print(f"\n=== Done ===")
print(f"OK: {ok_count}, Skipped/Dup: {skip_count}, Failed: {fail_count}")
