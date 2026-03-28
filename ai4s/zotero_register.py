"""
Zotero registration script for AI4S papers.
Steps: duplicate check → PDF download → create item → attach PDF → output JSON
"""
import json, os, time, re, urllib.request, urllib.parse, urllib.error, sys

# ── Config ──────────────────────────────────────────────────────────────────
API_KEY       = "4R2R3iQKe7I7NBHWlCWDRk8X"
USER_ID       = "1356104"
COLLECTION_KEY= "WKEZLEE8"
ZOTERO_DIR    = r"C:\Users\jehyu\GoogleDrive\Zotero"
UNPAYWALL_EMAIL = "jehyun.lee@gmail.com"
BASE_URL      = f"https://api.zotero.org/users/{USER_ID}"

HEADERS = {
    "Zotero-API-Key": API_KEY,
    "Content-Type":   "application/json",
    "User-Agent":     "ZoteroLibrarian/1.0 (jehyun.lee@gmail.com)",
}

# ── Helpers ──────────────────────────────────────────────────────────────────

def safe_title(title, maxlen=80):
    """Sanitize title for use as filename."""
    s = re.sub(r'[^\w\s\-]', '', title)
    s = re.sub(r'\s+', ' ', s).strip()
    return s[:maxlen]

def zotero_get(path, params=None):
    url = BASE_URL + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read())

def zotero_post(path, payload):
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        BASE_URL + path, data=data, headers=HEADERS, method="POST"
    )
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read())

def parse_author(name):
    """Split 'First Last' or 'Last, First' into firstName/lastName."""
    if "," in name:
        parts = [p.strip() for p in name.split(",", 1)]
        return {"creatorType": "author", "lastName": parts[0], "firstName": parts[1]}
    parts = name.strip().split()
    if len(parts) == 1:
        return {"creatorType": "author", "lastName": parts[0], "firstName": ""}
    return {"creatorType": "author", "lastName": parts[-1], "firstName": " ".join(parts[:-1])}

def download_pdf(url, dest_path, label=""):
    """Download PDF from url to dest_path. Returns True on success."""
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (compatible; ZoteroLibrarian/1.0)",
            "Accept": "application/pdf,*/*",
        })
        with urllib.request.urlopen(req, timeout=30) as r:
            content = r.read()
        # Validate: must start with %PDF
        if not content.startswith(b"%PDF"):
            print(f"    [WARN] {label}: not a valid PDF (got {content[:20]})")
            return False
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        with open(dest_path, "wb") as f:
            f.write(content)
        size_kb = len(content) // 1024
        print(f"    [OK] {label}: {size_kb} KB → {os.path.basename(dest_path)}")
        return True
    except Exception as e:
        print(f"    [FAIL] {label}: {e}")
        return False

def try_unpaywall(doi):
    """Query Unpaywall for OA PDF URL. Returns url string or None."""
    try:
        encoded = urllib.parse.quote(doi, safe="")
        url = f"https://api.unpaywall.org/v2/{encoded}?email={UNPAYWALL_EMAIL}"
        req = urllib.request.Request(url, headers={"User-Agent": "ZoteroLibrarian/1.0"})
        with urllib.request.urlopen(req, timeout=15) as r:
            uw = json.loads(r.read())
        best = uw.get("best_oa_location") or {}
        pdf_url = best.get("url_for_pdf")
        return pdf_url
    except Exception as e:
        print(f"    [Unpaywall] {e}")
        return None

# ── Main pipeline ─────────────────────────────────────────────────────────────

INPUT_PATH  = r"C:\Users\jehyu\Arbeitplatz\paper-curation\ai4s\_refs_to_add.json"
OUTPUT_PATH = r"C:\Users\jehyu\Arbeitplatz\paper-curation\ai4s\_refs_zotero_results.json"

with open(INPUT_PATH, encoding="utf-8") as f:
    data = json.load(f)
# _refs_to_add.json is a plain list of papers (no wrapper dict)
if isinstance(data, list):
    papers = data
else:
    papers = data.get("papers", data)
print(f"Loaded {len(papers)} papers\n")

# Load existing results to resume from where we left off
if os.path.exists(OUTPUT_PATH):
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        results = json.load(f)
    # Build set of titles already handled (registered + already_exists + manual_download)
    done_titles = set()
    for r in results["registered"]:
        done_titles.add(r["title"].lower().strip())
    for r in results["already_exists"]:
        done_titles.add(r["title"].lower().strip())
    for r in results["manual_download"]:
        done_titles.add(r["title"].lower().strip())
    # Clear failed list - we'll retry those
    results["failed"] = []
    print(f"Resuming: {len(done_titles)} already done, retrying failed papers\n")
else:
    results = {"registered": [], "already_exists": [], "failed": [], "manual_download": []}
    done_titles = set()

consecutive_failures = 0

for idx, paper in enumerate(papers):
    title   = paper["title"]
    arxiv_id= paper.get("arxiv_id", "") or ""
    doi     = paper.get("doi", "") or ""
    pdf_url = paper.get("pdf_url", "") or ""
    authors = paper.get("authors", [])
    abstract= paper.get("abstract", "") or ""
    date    = str(paper.get("date", "") or paper.get("year", "") or "")
    category= paper.get("category", "AI4S")

    print(f"\n[{idx+1}/{len(papers)}] {title[:70]}")

    # Skip papers already successfully processed in a previous run
    if title.lower().strip() in done_titles:
        print(f"  [SKIP] Already processed in previous run")
        continue

    # ── Step 1: Duplicate check ──────────────────────────────────────────────
    query = title[:40]
    try:
        existing = zotero_get("/items", {"q": query, "limit": 5})
        time.sleep(1)
    except Exception as e:
        print(f"  [ERROR] Zotero search failed: {e}")
        results["failed"].append({"title": title, "error": f"Zotero search: {e}"})
        continue

    # Check for title match (case-insensitive, first 40 chars)
    dup_key = None
    for item in existing:
        existing_title = item.get("data", {}).get("title", "")
        if existing_title.lower()[:40] == title.lower()[:40]:
            dup_key = item["key"]
            break
    if dup_key:
        print(f"  [SKIP] Already exists: {dup_key}")
        results["already_exists"].append({"title": title, "existing_key": dup_key})
        continue

    # ── Step 2: Download PDF ─────────────────────────────────────────────────
    stitle = safe_title(title)
    pdf_dest = os.path.join(ZOTERO_DIR, f"{stitle}.pdf")
    pdf_downloaded = False
    pdf_source = None

    # Priority 1: arXiv
    if arxiv_id and not pdf_downloaded:
        # Normalize arxiv_id: strip trailing version if needed but keep for URL
        ax_id = arxiv_id.split("v")[0] if "v" in arxiv_id else arxiv_id
        ax_url = f"https://arxiv.org/pdf/{ax_id}.pdf"
        print(f"  Trying arXiv: {ax_url}")
        pdf_downloaded = download_pdf(ax_url, pdf_dest, "arXiv")
        if pdf_downloaded:
            pdf_source = "arXiv"
        time.sleep(3)

    # Priority 2: S2 / direct pdf_url
    if pdf_url and not pdf_downloaded:
        print(f"  Trying S2/direct URL: {pdf_url[:60]}")
        pdf_downloaded = download_pdf(pdf_url, pdf_dest, "S2/direct")
        if pdf_downloaded:
            pdf_source = "S2/direct"

    # Priority 3: Unpaywall
    if doi and not pdf_downloaded:
        print(f"  Trying Unpaywall for DOI: {doi}")
        uw_url = try_unpaywall(doi)
        time.sleep(0.5)
        if uw_url:
            print(f"    Unpaywall URL: {uw_url[:60]}")
            pdf_downloaded = download_pdf(uw_url, pdf_dest, "Unpaywall")
            if pdf_downloaded:
                pdf_source = "Unpaywall"

    if not pdf_downloaded:
        print(f"  [NO PDF] All sources failed - added to manual list")
        results["manual_download"].append({
            "title": title, "doi": doi,
            "arxiv_id": arxiv_id, "pdf_url": pdf_url
        })
        pdf_dest = None

    # ── Step 3: Create Zotero item ───────────────────────────────────────────
    item_type = "preprint" if arxiv_id else "journalArticle"
    creators  = [parse_author(a) for a in authors]

    item = {
        "itemType":     item_type,
        "title":        title,
        "abstractNote": abstract,
        "date":         date,
        "creators":     creators,
        "tags":         [{"tag": category}, {"tag": "AI4S"}],
        "collections":  [COLLECTION_KEY],
    }
    if arxiv_id:
        ax_base = arxiv_id.split("v")[0] if "v" in arxiv_id else arxiv_id
        item["url"]       = f"https://arxiv.org/abs/{ax_base}"
        item["archiveID"] = f"arXiv:{ax_base}"
        item["repository"]= "arXiv"
    if doi:
        item["DOI"] = doi
    venue = paper.get("venue", "") or ""
    if venue:
        if item_type == "journalArticle":
            item["publicationTitle"] = venue
        else:
            # preprint uses 'repository' for venue; don't overwrite arXiv
            if not item.get("repository"):
                item["repository"] = venue

    try:
        resp = zotero_post("/items", [item])
        time.sleep(1)
    except Exception as e:
        print(f"  [ERROR] Zotero POST failed: {e}")
        results["failed"].append({"title": title, "error": f"Zotero POST: {e}"})
        consecutive_failures += 1
        if consecutive_failures >= 5:
            print("\n[ABORT] 5 consecutive failures - stopping")
            break
        continue

    # Extract parent key
    successful = resp.get("successful", {})
    if "0" not in successful:
        err_msg = json.dumps(resp.get("failed", {}))
        print(f"  [ERROR] Item not created: {err_msg}")
        results["failed"].append({"title": title, "error": err_msg})
        continue

    parent_key = successful["0"]["key"]
    print(f"  [CREATED] Zotero key: {parent_key}")

    # ── Step 4: Attach PDF as linked_file ────────────────────────────────────
    attached = False
    if pdf_dest and os.path.exists(pdf_dest):
        filename = os.path.basename(pdf_dest)
        attach_payload = [{
            "itemType":    "attachment",
            "parentItem":  parent_key,
            "linkMode":    "linked_file",
            "title":       filename,
            "contentType": "application/pdf",
            "path":        pdf_dest,
            "tags":        [],
        }]
        try:
            attach_resp = zotero_post("/items", attach_payload)
            time.sleep(1)
            att_ok = attach_resp.get("successful", {})
            if "0" in att_ok:
                att_key = att_ok["0"]["key"]
                print(f"  [ATTACHED] attachment key: {att_key}")
                attached = True
            else:
                print(f"  [WARN] Attachment failed: {attach_resp.get('failed', {})}")
        except Exception as e:
            print(f"  [WARN] Attachment error: {e}")

    # ── Record result ────────────────────────────────────────────────────────
    consecutive_failures = 0
    results["registered"].append({
        "title":    title,
        "key":      parent_key,
        "pdf":      attached,
        "pdf_path": pdf_dest,
        "pdf_source": pdf_source,
        "arxiv_id": arxiv_id,
        "doi":      doi,
    })

# ── Save output ───────────────────────────────────────────────────────────────
def save_results():
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

save_results()

print(f"\n{'='*60}")
print(f"DONE")
print(f"  Registered:      {len(results['registered'])}")
print(f"  Already exists:  {len(results['already_exists'])}")
print(f"  Failed:          {len(results['failed'])}")
print(f"  Manual download: {len(results['manual_download'])}")
print(f"\nResults saved to: {OUTPUT_PATH}")
