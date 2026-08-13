"""A live Zotero API key rode into the public repo and stayed there.

`pipeline/_archive/_batch_zotero.py` carried the key as a default argument —
`os.environ.get("ZOTERO_API_KEY", "<24-char key>")` — so the env lookup that
looked like good hygiene was in fact the delivery vehicle. It was committed,
pushed to `origin/master`, `origin/gh-pages` and `origin/pr-3`, and the key it
exposed was the same one the pipeline used in production, with read+write on
the whole personal library and every group.

Two rules come out of that, and both are tested here:

1. No git-tracked file may contain a secret-shaped literal.
2. The Zotero key is read from the environment and nowhere else — `config.json`
   is git-ignored, but it is also backed up, synced and pasted into chats, so
   it is not a place for credentials.
"""
import json
import os
import re
import subprocess
import sys
import unittest
from pathlib import Path

PIPELINE = Path(__file__).resolve().parents[1]
PROJECT_ROOT = PIPELINE.parent
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))


# Shapes that are secrets wherever they appear. Kept deliberately narrow: a
# false positive here blocks a commit, so each pattern anchors on a vendor
# prefix or on an assignment to a credential-named variable.
SECRET_PATTERNS = (
    ("Anthropic API key", re.compile(r"sk-ant-[A-Za-z0-9_-]{24,}")),
    ("OpenAI API key", re.compile(r"sk-(?:proj-)?[A-Za-z0-9]{40,}")),
    ("Google API key", re.compile(r"AIza[A-Za-z0-9_-]{35}")),
    ("Resend API key", re.compile(r"\bre_[A-Za-z0-9]{20,}")),
    ("GitHub token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}")),
    ("Cloudflare token", re.compile(r"\bCF_API_TOKEN\s*=\s*[\"'][A-Za-z0-9_-]{20,}[\"']")),
    # Zotero keys are 24 bare alphanumerics with no prefix to anchor on, so
    # anchor on the assignment instead: any credential-named binding whose
    # value is a 20+ char literal.
    ("hardcoded credential literal", re.compile(
        r"(?i)\b(?:api[_-]?key|apikey|secret|token|password|passwd)\b"
        r"\s*[=:]\s*[\"'][A-Za-z0-9_\-]{20,}[\"']")),
)

# Documented placeholders, not credentials.
PLACEHOLDER = re.compile(
    r"(?i)your[_-]|_here\b|example|placeholder|xxxx|\.\.\.|<[a-z_]+>|"
    r"dummy|fake|sample|redacted|sk-ant-api03-8Hj")

# Binary and vendored trees carry no reviewable source.
SKIP_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".pdf", ".ico", ".woff",
                 ".woff2", ".zip", ".gz", ".joblib", ".sqlite3", ".db"}


def tracked_files():
    """Files git actually publishes. Untracked scratch is not our problem."""
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=PROJECT_ROOT, capture_output=True, text=True, timeout=60,
    )
    if result.returncode != 0:
        raise unittest.SkipTest("not a git checkout")
    for name in result.stdout.split("\0"):
        if not name:
            continue
        path = PROJECT_ROOT / name
        if path.suffix.lower() in SKIP_SUFFIXES or not path.is_file():
            continue
        yield path


class TrackedSourceHasNoSecrets(unittest.TestCase):
    def test_no_tracked_file_carries_a_secret_literal(self):
        findings = []
        this_file = Path(__file__).resolve()
        for path in tracked_files():
            if path.resolve() == this_file:
                continue  # the patterns above would match themselves
            try:
                text = path.read_text(encoding="utf-8")
            except (UnicodeDecodeError, OSError):
                continue
            for lineno, line in enumerate(text.splitlines(), 1):
                if PLACEHOLDER.search(line):
                    continue
                for label, pattern in SECRET_PATTERNS:
                    if pattern.search(line):
                        rel = path.relative_to(PROJECT_ROOT)
                        findings.append(f"{rel}:{lineno} — {label}")
        self.assertEqual(findings, [], "\n".join(
            ["git-tracked 파일에 비밀값이 있습니다. 키를 폐기·재발급하고 "
             "환경변수로 옮기세요:"] + findings))

    def test_the_leaked_zotero_key_is_gone_from_the_worktree(self):
        """The specific key from the 2026-08-13 leak, by shape not by value."""
        leaked = re.compile(r"ZOTERO_API_KEY[\"']?\s*,\s*[\"'][A-Za-z0-9]{24}[\"']")
        offenders = [
            str(path.relative_to(PROJECT_ROOT))
            for path in tracked_files()
            if path.suffix == ".py"
            and leaked.search(path.read_text(encoding="utf-8", errors="ignore"))
        ]
        self.assertEqual(offenders, [], "os.environ.get('ZOTERO_API_KEY', <literal>) "
                                        "형태의 폴백은 키를 커밋하는 것과 같습니다")


class ZoteroKeyComesFromTheEnvironmentOnly(unittest.TestCase):
    def setUp(self):
        import config_loader
        self.config_loader = config_loader
        config_loader._config_cache = None
        self._saved = os.environ.get("ZOTERO_API_KEY")

    def tearDown(self):
        if self._saved is None:
            os.environ.pop("ZOTERO_API_KEY", None)
        else:
            os.environ["ZOTERO_API_KEY"] = self._saved
        self.config_loader._config_cache = None

    def test_the_env_var_is_returned(self):
        os.environ["ZOTERO_API_KEY"] = "env-side-value"
        self.assertEqual(self.config_loader.get_zotero_api_key(), "env-side-value")

    def test_config_json_is_not_consulted(self):
        os.environ.pop("ZOTERO_API_KEY", None)
        self.config_loader._config_cache = {"zotero": {"api_key": "config-side-value"}}
        self.assertEqual(self.config_loader.get_zotero_api_key(), "")

    def test_env_wins_even_when_config_disagrees(self):
        os.environ["ZOTERO_API_KEY"] = "env-side-value"
        self.config_loader._config_cache = {"zotero": {"api_key": "config-side-value"}}
        self.assertEqual(self.config_loader.get_zotero_api_key(), "env-side-value")

    def test_missing_key_fails_where_zotero_is_actually_called(self):
        """Empty is fine at import time; the failure belongs at the call site."""
        os.environ.pop("ZOTERO_API_KEY", None)
        os.environ.pop("ZOTERO_USER_ID", None)
        self.config_loader._config_cache = {"zotero": {}}
        self.config_loader._user_id_cache = None
        with self.assertRaises(ValueError) as caught:
            self.config_loader.get_zotero_user_id()
        self.assertIn("ZOTERO_API_KEY", str(caught.exception))


class SetupNeverPersistsTheZoteroKey(unittest.TestCase):
    def test_the_spec_is_env_only_and_has_no_config_path(self):
        import setup
        spec = next(s for s in setup.REQUIRED_KEYS if s["env"] == "ZOTERO_API_KEY")
        self.assertTrue(spec.get("env_only"))
        self.assertNotIn("path", spec)

    def test_a_legacy_config_key_is_removed_on_setup(self):
        import setup
        # Short on purpose: scripts/scan-secrets.py refuses any 20+ char
        # literal bound to `api_key`, and it collapses whitespace first, so a
        # long human-readable placeholder trips the scanner too.
        cfg = {"zotero": {"api_key": "stale-value",
                          "email": "a@b.c"}}
        spec = next(s for s in setup.REQUIRED_KEYS if s["env"] == "ZOTERO_API_KEY")
        self.assertTrue(setup._cfg_unset(cfg, spec["legacy_path"]))
        self.assertNotIn("api_key", cfg["zotero"])
        self.assertEqual(cfg["zotero"]["email"], "a@b.c")

    def test_env_only_specs_ignore_config_values(self):
        import setup
        spec = next(s for s in setup.REQUIRED_KEYS if s["env"] == "ZOTERO_API_KEY")
        saved = os.environ.pop("ZOTERO_API_KEY", None)
        try:
            value, source = setup._key_value(
                {"zotero": {"api_key": "config-side-value"}}, spec)
        finally:
            if saved is not None:
                os.environ["ZOTERO_API_KEY"] = saved
        self.assertEqual((value, source), ("", None))

    def test_the_example_config_does_not_ship_an_api_key_field(self):
        example = json.loads((PROJECT_ROOT / "config.example.json")
                             .read_text(encoding="utf-8"))
        self.assertNotIn("api_key", example.get("zotero", {}))


if __name__ == "__main__":
    unittest.main()
