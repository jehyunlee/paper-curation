"""The Zotero directory differs per machine, so resolving it must too.

One library is used from this laptop, from the macmini and from a Windows box,
and a `linked_file` attachment stores the absolute path of whichever machine
created it. Pinning a single path meant 1,025 papers resolved to "file
missing" — the audit counted them before the resolver learned to look
elsewhere.
"""
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

PIPELINE = Path(__file__).resolve().parents[1]
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

import config_loader


class ZoteroDirResolutionTests(unittest.TestCase):
    def setUp(self):
        self._saved = config_loader._config_cache
        os.environ.pop("ZOTERO_DIR", None)

    def tearDown(self):
        config_loader._config_cache = self._saved
        os.environ.pop("ZOTERO_DIR", None)

    def _config(self, zotero: dict):
        config_loader._config_cache = {"zotero": zotero}

    def test_env_overrides_everything(self):
        self._config({"pdf_dir": "/from/config",
                      "pdf_dir_by_host": {"anyhost": "/from/host"}})
        os.environ["ZOTERO_DIR"] = "/from/env"
        with patch.object(config_loader, "_hostname", return_value="anyhost"):
            self.assertEqual(config_loader.get_zotero_dir(), "/from/env")

    def test_host_map_wins_over_the_single_default(self):
        self._config({
            "pdf_dir": "/single/default",
            "pdf_dir_by_host": {"macmini-cf": "/on/macmini",
                                "jehyun-macbook": "/on/laptop"},
        })
        with patch.object(config_loader, "_hostname",
                          return_value="macmini-cf"):
            self.assertEqual(config_loader.get_zotero_dir(), "/on/macmini")
        with patch.object(config_loader, "_hostname",
                          return_value="jehyun-macbook"):
            self.assertEqual(config_loader.get_zotero_dir(), "/on/laptop")

    def test_host_map_ignores_domain_suffix_and_case(self):
        # macOS reports "Jehyun-MacBook.local"; the map should still hit.
        self._config({"pdf_dir": "/single",
                      "pdf_dir_by_host": {"Jehyun-MacBook.local": "/on/laptop"}})
        with patch.object(config_loader, "_hostname",
                          return_value="jehyun-macbook"):
            self.assertEqual(config_loader.get_zotero_dir(), "/on/laptop")

    def test_an_unlisted_host_falls_through(self):
        self._config({"pdf_dir": "/single",
                      "pdf_dir_by_host": {"macmini-cf": "/on/macmini"}})
        with patch.object(config_loader, "_hostname", return_value="stranger"):
            self.assertEqual(config_loader.get_zotero_dir(), "/single")

    def test_candidates_pick_the_one_that_exists(self):
        with tempfile.TemporaryDirectory() as real:
            self._config({
                "pdf_dir": "/single",
                "pdf_dir_candidates": ["/nowhere/at/all", real],
            })
            self.assertEqual(config_loader.get_zotero_dir(), real)

    def test_candidates_that_all_miss_fall_back(self):
        self._config({"pdf_dir": "/single",
                      "pdf_dir_candidates": ["/nowhere", "/also/nowhere"]})
        self.assertEqual(config_loader.get_zotero_dir(), "/single")

    def test_plain_config_still_works(self):
        # A single-machine setup must behave exactly as before.
        self._config({"pdf_dir": "/single"})
        self.assertEqual(config_loader.get_zotero_dir(), "/single")

    def test_missing_config_returns_empty(self):
        self._config({})
        self.assertEqual(config_loader.get_zotero_dir(), "")


class WindowsPathAttachmentTests(unittest.TestCase):
    """A linked_file written on Windows must resolve on macOS."""

    def test_windows_absolute_path_resolves_by_basename(self):
        from audit_zotero_pdf import resolve_pdf_path
        with tempfile.TemporaryDirectory() as zdir:
            name = "Singh et al._2026_Citation of classical research.pdf"
            (Path(zdir) / name).write_bytes(b"%PDF-1.4\n")
            with patch("audit_zotero_pdf.ZOTERO_DIR", zdir):
                found = resolve_pdf_path(
                    {"path": "C:\\Users\\jehyu\\GoogleDrive\\Zotero\\" + name})
            self.assertIsNotNone(found)
            self.assertEqual(Path(found).name, name)

    def test_posix_absolute_path_still_resolves(self):
        from audit_zotero_pdf import resolve_pdf_path
        with tempfile.TemporaryDirectory() as zdir:
            name = "Paper.pdf"
            target = Path(zdir) / name
            target.write_bytes(b"%PDF-1.4\n")
            with patch("audit_zotero_pdf.ZOTERO_DIR", zdir):
                self.assertEqual(
                    Path(resolve_pdf_path({"path": str(target)})), target)


if __name__ == "__main__":
    unittest.main()
