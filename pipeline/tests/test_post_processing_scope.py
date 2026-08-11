"""Post-processing must follow the run's scope, not always the whole corpus.

A `--slugs` run states exactly which papers changed, yet the orchestrator
decided its post-processing scope from `--resume` alone. Six regenerated
reviews (89 seconds of work) therefore triggered the full corpus chain:
`topic_modeling` retrained over 4,196 papers (18.5 min), every category's
narrative and timeline image was rewritten (44 min), and `review_to_html
--all` re-converted every page (4 min). AGENTS.md's own audit/recovery
command, `--mode rebuild --slugs 088,1093`, paid that on every invocation.

These tests pin the scope decision so the targeted path cannot silently
become a full rebuild again.
"""
import argparse
import sys
import unittest
from pathlib import Path

PIPELINE = Path(__file__).resolve().parents[1]
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

import run_update_force as runner


def make_args(**overrides):
    """Argument namespace with the orchestrator's defaults."""
    values = {"resume": False, "slugs": "", "skip_existing": False,
              "timeline": False, "category": False, "mode": None}
    values.update(overrides)
    return argparse.Namespace(**values)


class ScopeDecisionTests(unittest.TestCase):
    def test_slugs_alone_scopes_post_processing(self):
        self.assertTrue(
            runner.scoped_post_processing(make_args(slugs="10498,9682")))

    def test_resume_still_scopes_post_processing(self):
        self.assertTrue(runner.scoped_post_processing(make_args(resume=True)))

    def test_rebuild_of_the_whole_topic_stays_full(self):
        # `--mode rebuild` with no slugs regenerates every review, so every
        # corpus-wide artifact genuinely has to be rebuilt.
        self.assertFalse(runner.scoped_post_processing(make_args()))

    def test_mode_rebuild_with_slugs_is_scoped(self):
        args = make_args(mode="rebuild", slugs="088,1093")
        runner._apply_mode_mapping(args)
        self.assertFalse(args.resume)          # rebuild clears --resume
        self.assertTrue(runner.scoped_post_processing(args))

    def test_mode_curate_is_scoped(self):
        args = make_args(mode="curate")
        runner._apply_mode_mapping(args)
        self.assertTrue(runner.scoped_post_processing(args))


class ReviewHtmlTargetTests(unittest.TestCase):
    CHANGED = {"10498_Steering", "9682_FraPPE"}

    def test_slugs_run_renders_only_its_papers(self):
        targets = runner.review_html_targets(
            make_args(slugs="10498,9682"), self.CHANGED)
        self.assertEqual(targets, sorted(self.CHANGED))

    def test_targets_are_accepted_by_the_renderer(self):
        # The renderer matches a target with `d == s`, so full slugs resolve.
        import review_to_html
        targets = runner.review_html_targets(
            make_args(slugs="10498,9682"), self.CHANGED)
        resolved = review_to_html._resolve_target_slugs(
            sorted(self.CHANGED | {"0001_Other"}), slugs=",".join(targets))
        self.assertEqual(resolved, sorted(self.CHANGED))

    def test_weekly_resume_run_still_renders_everything(self):
        # The weekly run is how a changed page template reaches every paper.
        self.assertIsNone(
            runner.review_html_targets(make_args(resume=True), self.CHANGED))

    def test_full_run_renders_everything(self):
        self.assertIsNone(
            runner.review_html_targets(make_args(), self.CHANGED))

    def test_slugs_run_that_completed_nothing_falls_back(self):
        self.assertIsNone(
            runner.review_html_targets(make_args(slugs="10498"), set()))


if __name__ == "__main__":
    unittest.main()
