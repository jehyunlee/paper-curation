"""The bibliography release gate must finalize cross-table invariants before checking."""
import sys
import unittest
from pathlib import Path

PIPELINE = Path(__file__).resolve().parents[1]
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

import run_update_force as engine


class BibliographyReleaseStepsTests(unittest.TestCase):
    def test_finalize_runs_between_incremental_build_and_strict_check(self):
        calls = []

        def record(name, command, timeout):
            calls.append((name, command, timeout))

        engine.run_bibliography_release_steps(record)

        self.assertEqual(
            [name for name, _command, _timeout in calls],
            [
                "setup_affiliation_sources",
                "build_bibliography_db",
                "finalize_bibliography_db",
                "check_bibliography_db",
                "sync_bibliography_db (push)",
            ],
        )
        finalize = calls[2][1]
        self.assertEqual(
            finalize,
            [
                "python",
                "pipeline/build_bibliography_db.py",
                "--finalize",
                "--no-email",
            ],
        )
        self.assertEqual(calls[3][1][-1], "--strict")


if __name__ == "__main__":
    unittest.main()
