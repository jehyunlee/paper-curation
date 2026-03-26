import fitz
import sys
import os

pdf_path = sys.argv[1]
out_path = sys.argv[2]

doc = fitz.open(pdf_path)
all_text = []
for i, page in enumerate(doc):
    text = page.get_text()
    all_text.append(f"=== PAGE {i+1} ===\n{text}")
doc.close()

with open(out_path, "w", encoding="utf-8") as f:
    f.write("\n".join(all_text))
