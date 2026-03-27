import os, shutil, json, re

repo_dir = r"C:\Users\jehyu\Arbeitplatz\paper-curation"
ai4s_dir = os.path.join(repo_dir, "ai4s")
papers_dir = os.path.join(repo_dir, "papers")
os.makedirs(papers_dir, exist_ok=True)

# Move review directories
moved = 0
already_exists = 0
for d in sorted(os.listdir(ai4s_dir)):
    src = os.path.join(ai4s_dir, d)
    if os.path.isdir(src) and re.match(r'^\d{3}_', d):
        dst = os.path.join(papers_dir, d)
        if not os.path.exists(dst):
            shutil.move(src, dst)
            moved += 1
        else:
            print(f"Already exists: {d}")
            already_exists += 1

print(f"Moved: {moved}, Already existed: {already_exists}")

# Read classification
class_path = os.path.join(ai4s_dir, "_new_classification.json")
classification = {}
if os.path.exists(class_path):
    with open(class_path, "r", encoding="utf-8") as f:
        cls_data = json.load(f)
    for a in cls_data.get("assignments", []):
        classification[a["slug"]] = a
print(f"Classification entries: {len(classification)}")

def extract_metadata(content, slug):
    lines = content.split('\n')

    # Title: first non-empty line, strip leading #
    title = ""
    for line in lines:
        line = line.strip()
        if line:
            title = re.sub(r'^#+\s*', '', line)
            break

    # Authors, date, doi from the metadata blockquote line
    # Pattern: > **저자**: ... | **날짜**: ... | **Journal**: ... | **DOI**: ...
    # or > **저자**: ... | **날짜**: ... | **URL**: ...
    authors = []
    date = ""
    doi = ""

    meta_match = re.search(r'^>\s*\*\*저자\*\*:\s*(.+)', content, re.MULTILINE)
    if meta_match:
        meta_line = meta_match.group(0)

        # Authors
        auth_match = re.search(r'\*\*저자\*\*:\s*([^|]+)', meta_line)
        if auth_match:
            authors_str = auth_match.group(1).strip()
            authors = [a.strip() for a in authors_str.split(',') if a.strip()]

        # Date
        date_match = re.search(r'\*\*날짜\*\*:\s*([^|]+)', meta_line)
        if date_match:
            date = date_match.group(1).strip()

        # DOI
        doi_match = re.search(r'\*\*DOI\*\*:\s*([^|]+)', meta_line)
        if doi_match:
            doi = doi_match.group(1).strip()
        else:
            # Try URL
            url_match = re.search(r'\*\*URL\*\*:\s*([^|]+)', meta_line)
            if url_match:
                doi = url_match.group(1).strip()

    # Score: look for Overall row in markdown table
    score = 0
    score_match = re.search(r'\|\s*Overall\s*\|\s*([\d.]+)', content)
    if score_match:
        try:
            score = float(score_match.group(1))
        except ValueError:
            score = 0

    # Essence section: text between ## Essence and next ##
    essence = ""
    essence_match = re.search(r'##\s*Essence\s*\n+([\s\S]+?)(?=\n##|\Z)', content)
    if essence_match:
        essence = essence_match.group(1).strip()

    return title, authors, date, doi, score, essence

# Build _papers_index.json
index = []
papers_dirs = sorted(os.listdir(papers_dir))
for d in papers_dirs:
    if not re.match(r'^\d{3}_', d):
        continue
    rpath = os.path.join(papers_dir, d, "review.md")
    if not os.path.isfile(rpath):
        print(f"No review.md: {d}")
        continue

    with open(rpath, "r", encoding="utf-8") as f:
        content = f.read()

    title, authors, date, doi, score, essence = extract_metadata(content, d)

    # Check figures
    figures_dir = os.path.join(papers_dir, d, "figures")
    has_figures_dir = os.path.isdir(figures_dir)
    has_figures = False
    if has_figures_dir:
        has_figures = any(f.endswith(".png") for f in os.listdir(figures_dir))

    cls = classification.get(d, {})

    entry = {
        "slug": d,
        "title": title,
        "authors": authors,
        "date": date,
        "doi": doi,
        "topics": ["ai4s"],
        "primary_topic": "ai4s",
        "primary_category": cls.get("primary_category", "Other"),
        "all_categories": cls.get("all_categories", ["Other"]),
        "score": score,
        "essence": essence,
        "has_pdf": has_figures_dir,
        "has_figures": has_figures,
        "review_date": "2026-03-27",
    }
    index.append(entry)

out_path = os.path.join(papers_dir, "_papers_index.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(index, f, ensure_ascii=False, indent=2)

print(f"Index built: {len(index)} papers -> {out_path}")

# Verify
papers_count = sum(1 for d in os.listdir(papers_dir) if re.match(r'^\d{3}_', d) and os.path.isdir(os.path.join(papers_dir, d)))
ai4s_remaining = sum(1 for d in os.listdir(ai4s_dir) if re.match(r'^\d{3}_', d) and os.path.isdir(os.path.join(ai4s_dir, d)))
print(f"Verification: papers/ has {papers_count} dirs, ai4s/ has {ai4s_remaining} numbered dirs remaining")
