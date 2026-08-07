"""review.md 제목 헤더 유실 → HTML 제목 경로 노출 회귀 테스트."""
import re
import sys
import tempfile
import unittest
from pathlib import Path

# pipeline 모듈들은 형제 모듈을 top-level 로 import 한다(config_loader 등).
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from inject_frontmatter import _rebuild_title_header  # noqa: E402
from validate_papers import check_title_header  # noqa: E402

FM = '''---
title: "Learning to Discover Regulatory Elements for Gene Expression Prediction"
authors:
  - "Xingyu Su"
  - "Shuiwang Ji"
date: "2025"
doi: "10.48550/arXiv.2502.13991"
primary_topic: "ai4s"
---
'''


class RebuildTitleHeaderTests(unittest.TestCase):
    def test_header_matches_canonical_template(self):
        h = _rebuild_title_header(FM)
        self.assertTrue(h.startswith(
            "# Learning to Discover Regulatory Elements for Gene Expression Prediction\n"))
        self.assertIn("> **저자**: Xingyu Su, Shuiwang Ji | **날짜**: 2025", h)
        self.assertIn("**DOI**: [10.48550/arXiv.2502.13991]"
                      "(https://doi.org/10.48550/arXiv.2502.13991)", h)
        self.assertTrue(h.rstrip().endswith("---"))

    def test_missing_doi_falls_back_to_na(self):
        h = _rebuild_title_header('---\ntitle: "T"\ndate: "2026"\ndoi: "N/A"\n---\n')
        self.assertIn("**DOI**: N/A", h)
        self.assertNotIn("https://doi.org/N/A", h)

    def test_url_used_when_doi_absent(self):
        h = _rebuild_title_header('---\ntitle: "T"\ndate: "2026"\ndoi: ""\nurl: "https://x.dev/p"\n---\n')
        self.assertIn("**URL**: [https://x.dev/p](https://x.dev/p)", h)


class ValidateTitleHeaderTests(unittest.TestCase):
    def _write(self, text):
        d = tempfile.mkdtemp()
        p = Path(d) / "review.md"
        p.write_text(text, encoding="utf-8")
        return str(p)

    def test_flags_review_without_h1(self):
        issues = check_title_header(self._write(FM + "\n## Essence\n\n본문\n"))
        self.assertEqual(len(issues), 1)
        self.assertIn("NO_TITLE_HEADER", issues[0])

    def test_clean_review_passes(self):
        body = FM + "\n# Real Title\n\n> **저자**: A | **날짜**: 2025\n\n---\n\n## Essence\n\n본문\n"
        self.assertEqual(check_title_header(self._write(body)), [])

    def test_frontmatter_title_alone_is_not_enough(self):
        """frontmatter 에 title 이 있어도 본문 H1 이 없으면 잡아야 한다."""
        self.assertTrue(check_title_header(self._write(FM + "\n## Essence\n\n본문\n")))


class HtmlTitleFallbackTests(unittest.TestCase):
    def test_review_to_html_never_uses_directory_path(self):
        """H1 이 없어도 <title>/<h1> 에 slug_dir 절대경로가 들어가면 안 된다."""
        src = (Path(__file__).resolve().parents[1] / "review_to_html.py").read_text(encoding="utf-8")
        block = re.search(r'# Extract title.*?meta_m = ', src, re.S).group(0)
        self.assertNotIn("else slug_dir", block,
                         "title 폴백이 slug_dir(절대경로)로 남아 있다")
        self.assertIn("^title:", block, "frontmatter title 폴백이 없다")


if __name__ == "__main__":
    unittest.main()
