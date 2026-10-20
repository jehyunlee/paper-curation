"""merge_duplicate_slugs: canonical choice, sidecar remap, and the slug grammar
shared with refresh_paper_connections."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import merge_duplicate_slugs as M  # noqa: E402
import refresh_paper_connections as RP  # noqa: E402


def _row(slug, **kw):
    base = {"slug": slug, "title": "", "doi": "", "topics": ["ai4s"], "score": 4.0,
            "zotero_item_key": ""}
    base.update(kw)
    return base


class ChooseKeepTests(unittest.TestCase):
    item = {"key": "KEY1", "DOI": "10.1000/abc", "title": "Forecasting the future of AI", "extra": ""}

    def test_curio_marker_outranks_everything(self):
        rows = [_row("100_a", zotero_item_key="KEY1", doi="10.1000/abc", score=5.0),
                _row("200_b", topics=["ai4s", "scisci"])]
        item = dict(self.item, extra="arXiv:1\npapercurio: 200_b;2026-01-01")
        self.assertEqual(M.choose_keep(rows, item), "200_b")

    def test_index_key_then_doi_then_title(self):
        self.assertEqual(M.choose_keep([_row("100_a"), _row("200_b", zotero_item_key="KEY1")],
                                       self.item), "200_b")
        self.assertEqual(M.choose_keep([_row("100_a", doi="https://doi.org/10.1000/ABC"),
                                        _row("200_b", title="Forecasting the future of AI")],
                                       self.item), "100_a")
        self.assertEqual(M.choose_keep([_row("100_a"),
                                        _row("200_b", title="Forecasting the Future of AI!")],
                                       self.item), "200_b")

    def test_ties_prefer_more_topics_then_score_then_lower_prefix(self):
        self.assertEqual(M.choose_keep([_row("300_a"), _row("200_b", topics=["ai4s", "scisci"])],
                                       {"key": "", "DOI": "", "title": ""}), "200_b")
        self.assertEqual(M.choose_keep([_row("300_a", score=5.0), _row("200_b")],
                                       {"key": "", "DOI": "", "title": ""}), "300_a")
        self.assertEqual(M.choose_keep([_row("300_a"), _row("200_b")],
                                       {"key": "", "DOI": "", "title": ""}), "200_b")


class RemapTests(unittest.TestCase):
    def test_exact_slug_strings_are_remapped_and_lists_deduped(self):
        data = {"sub_themes": [{"slugs": ["100_drop", "200_keep", "300_other"],
                                "name": "100_drop is not a slug here? it is: exact match only"}],
                "100_drop": {"x": 1}}
        out = M._remap_values(data, {"100_drop": "200_keep"})
        self.assertEqual(out["sub_themes"][0]["slugs"], ["200_keep", "300_other"])
        self.assertIn("200_keep", out)
        self.assertNotIn("100_drop", out)
        # Prose containing the slug is untouched (no substring replacement).
        self.assertTrue(out["sub_themes"][0]["name"].startswith("100_drop is not"))


class SlugGrammarTests(unittest.TestCase):
    def test_unicode_and_nfd_slugs_pass(self):
        for slug in ("10067_Multi-marginal_temporal_Schro\u0308dinger_Bridge",
                     "10138_Optimal_Guarantees_for_Auditing_Re\u0301nyi",
                     "1286_\u03c0_05_a_Vision-Language-Action_Model",
                     "3023_AQVolt26_High-Temperature_r\u00b2SCAN_Halide",
                     "100_plain-ascii_slug"):
            self.assertIsNotNone(RP._SLUG.fullmatch(slug), slug)

    def test_path_characters_and_bad_shapes_are_rejected(self):
        for slug in ("100_../x", "100_a/b", "100_a\\b", "100_a b", "100_a.b", "100_", "abc_x",
                     "100__x", "10_x", "100_-x"):
            self.assertIsNone(RP._SLUG.fullmatch(slug), slug)


if __name__ == "__main__":
    unittest.main()
