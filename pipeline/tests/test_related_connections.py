"""Focused regression coverage for related-paper connections.

Connected papers are found in embedding space only. These tests replace
embedding retrieval, so they never load SPECTER2 weights, and they guard that
no connection writer can reach an LLM again.
"""
from __future__ import annotations

import contextlib
import ast
import importlib
import io
import json
import os
import re
import subprocess
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest.mock import patch

PIPELINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PIPELINE not in sys.path:
    sys.path.insert(0, PIPELINE)

from lib.related import build_connections  # noqa: E402


PAPERS = [
    {"slug": "001_Source", "authors": ["Ada Lovelace"], "date": "2024",
     "classifications": {"demo": {"primary_category": "Methods"}}},
    {"slug": "002_Earlier", "authors": ["Ada Lovelace"], "date": "2022",
     "classifications": {"demo": {"primary_category": "Methods"}}},
    {"slug": "003_Alternative", "authors": ["Grace Hopper"], "date": "2025",
     "classifications": {"demo": {"primary_category": "Applications"}}},
]


class DeterministicBuilderTests(unittest.TestCase):
    def test_relation_limit_and_empty_results_are_deterministic(self):
        candidates = {
            "001_Source": [("002_Earlier", 0.91), ("003_Alternative", 0.88)],
            "003_Alternative": [],
        }
        result = build_connections(candidates, PAPERS, limit=1)

        self.assertEqual(result["003_Alternative"], [])
        self.assertEqual(len(result["001_Source"]), 1)
        link = result["001_Source"][0]
        self.assertEqual(link["slug"], "002_Earlier")
        self.assertEqual(link["relation"], "alternative")
        self.assertEqual(link["reason"],
                         "SPECTER2 임베딩 공간에서 가까운 논문입니다 (코사인 유사도 0.91).")
        self.assertEqual(link["basis"], "embedding")
        self.assertEqual(link["model"], "")
        self.assertEqual(link["evidence"], {"cosine": 0.91})


class NoLlmInConnectionPathTests(unittest.TestCase):
    """Connected papers are found in embedding space. No writer may call an LLM."""

    WRITERS = ("lib/related.py", "lib/connections.py", "refresh_paper_connections.py",
               "sync_paper_connections.py")
    PROVIDERS = {"anthropic", "openai", "google", "lib.relation_judge",
                 "lib.credentials", "lib.verify"}

    @staticmethod
    def _imports(path):
        with open(os.path.join(PIPELINE, path), encoding="utf-8") as f:
            tree = ast.parse(f.read())
        names = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                names.update(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                names.add(node.module)
                names.update(f"{node.module}.{alias.name}" for alias in node.names)
        return names

    def test_connection_writers_import_no_provider_or_judge(self):
        for path in self.WRITERS:
            with self.subTest(path=path):
                hits = {n for n in self._imports(path)
                        if n in self.PROVIDERS or n.split(".")[0] in self.PROVIDERS}
                self.assertEqual(hits, set())

    def test_relation_judge_module_is_gone(self):
        self.assertFalse(os.path.exists(os.path.join(PIPELINE, "lib", "relation_judge.py")))
        for path in ("topic_modeling.py", "extract_insights.py", "run_feature.py",
                     *self.WRITERS):
            with self.subTest(path=path):
                self.assertFalse({n for n in self._imports(path) if "relation_judge" in n})

    def test_legacy_judged_entries_never_load(self):
        import json
        import tempfile
        from lib import connections
        stored = {"A": [{"slug": "B", "basis": "model", "model": "claude-haiku-4-5"},
                        {"slug": "C", "basis": "metadata"},
                        {"slug": "D", "relation": "foundation", "reason": "legacy"},
                        {"slug": "E", "basis": "embedding", "reason": "near"}]}
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "_global_connections.json")
            with open(path, "w", encoding="utf-8") as f:
                json.dump(stored, f)
            with patch.object(connections, "GLOBAL_CONN_PATH", path):
                loaded = connections.load_global_connections()
        self.assertEqual([c["slug"] for c in loaded["A"]], ["E"])


class ExtractInsightsWiringTests(unittest.TestCase):
    def setUp(self):
        self.topic_modeling = types.ModuleType("topic_modeling")
        self.topic_modeling.extract_originalities = lambda papers: papers
        self.topic_modeling.compute_embeddings = lambda originalities, cache_path: (
            "fake-embeddings", [paper["slug"] for paper in originalities]
        )
        self.topic_modeling.compute_related_candidates = lambda embeddings, slugs, top_k, papers: {
            "001_Source": [("002_Earlier", 0.91)],
            "002_Earlier": [("001_Source", 0.91)],
            "003_Alternative": [],
        }
        self.modules = patch.dict(sys.modules, {"topic_modeling": self.topic_modeling})
        self.modules.start()
        sys.modules.pop("extract_insights", None)
        self.ei = importlib.import_module("extract_insights")

    def tearDown(self):
        sys.modules.pop("extract_insights", None)
        self.modules.stop()

    def test_connection_caller_uses_builder_without_provider_client(self):
        # Three papers make this category eligible. No provider SDK is importable:
        # finding connections must not need one.
        with patch.dict(sys.modules, {"anthropic": None, "openai": None,
                                      "lib.relation_judge": None}):
            connections = self.ei.extract_paper_connections(
                "demo", {"Methods": PAPERS}, PAPERS
            )
        self.assertEqual(connections["001_Source"][0]["relation"], "alternative")
        self.assertEqual(connections["001_Source"][0]["basis"], "embedding")
        self.assertEqual(connections["003_Alternative"], [])

    def test_narrow_and_other_categories_do_not_become_targets(self):
        connections = self.ei.extract_paper_connections(
            "demo",
            {"Other": PAPERS, "Too small": PAPERS[:2]},
            PAPERS,
        )
        self.assertEqual(connections, {})

    def test_scoped_sources_use_the_full_cross_category_pool(self):
        cross_category = {
            "slug": "004_Cross_Category", "authors": ["Linus Torvalds"],
            "date": "2023",
            "classifications": {"demo": {"primary_category": "Applications"}},
        }
        pool = PAPERS + [cross_category]
        seen = {}

        def candidates(embeddings, slugs, top_k, papers):
            seen["pool"] = papers
            return {
                "001_Source": [("004_Cross_Category", 0.92)],
                "002_Earlier": [], "003_Alternative": [],
                "004_Cross_Category": [("001_Source", 0.92)],
            }

        self.topic_modeling.compute_related_candidates = candidates
        connections = self.ei.extract_paper_connections(
            "demo", {"Methods": PAPERS}, pool
        )
        self.assertEqual(seen["pool"], pool)
        self.assertEqual(connections["001_Source"][0]["slug"], "004_Cross_Category")
        self.assertNotIn("004_Cross_Category", connections)

    def test_persistence_receives_empty_results_once(self):
        with patch("lib.connections.sync_topic_connections") as sync:
            self.ei.extract_paper_connections(
                "demo", {"Methods": PAPERS}, PAPERS,
                topic_dir="/tmp/demo", topic_slugs=[paper["slug"] for paper in PAPERS],
            )
        sync.assert_called_once()
        persisted = sync.call_args.args[0]
        self.assertEqual(persisted["003_Alternative"], [])

    def test_persistence_failure_reaches_the_caller(self):
        with patch("lib.connections.sync_topic_connections",
                   side_effect=OSError("disk unavailable")):
            with self.assertRaisesRegex(OSError, "disk unavailable"):
                self.ei.extract_paper_connections(
                    "demo", {"Methods": PAPERS}, PAPERS,
                    topic_dir="/tmp/demo", topic_slugs=[paper["slug"] for paper in PAPERS],
                )

    def test_connections_only_does_not_construct_a_provider(self):
        with patch.object(self.ei, "load_topic_data", return_value=(PAPERS, {"Methods": PAPERS}, [])), \
             patch.object(self.ei, "get_topic_dir", return_value="/tmp/demo"), \
             patch.object(self.ei, "extract_paper_connections", return_value={}) as extract, \
             patch.object(self.ei, "Anthropic", side_effect=AssertionError("provider constructed")):
            self.ei._run_insights("demo", connections_only=True)
        extract.assert_called_once()

    def test_cli_no_longer_accepts_seed_cache_flag(self):
        with patch.object(self.ei, "_run_insights") as run, \
             patch.object(sys, "argv", ["extract_insights.py", "--connections-only"]):
            self.ei.main()
        run.assert_called_once_with(topic="ai4s", insights_only=False,
                                    connections_only=True, categories=None)

        with patch.object(sys, "argv", ["extract_insights.py", "--seed-cache-only"]), \
             contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as error:
                self.ei.main()
        self.assertEqual(error.exception.code, 2)


class TopicModelingCliTests(unittest.TestCase):
    def test_main_passes_only_supported_defaults_to_programmatic_entrypoint(self):
        source_path = os.path.join(PIPELINE, "topic_modeling.py")
        tree = ast.parse(open(source_path, encoding="utf-8").read(), source_path)
        main = next(node for node in tree.body
                    if isinstance(node, ast.FunctionDef) and node.name == "main")
        calls = []
        namespace = {
            "argparse": __import__("argparse"),
            "_run_topic_model": lambda **kwargs: calls.append(kwargs),
        }
        exec(compile(ast.Module(body=[main], type_ignores=[]), source_path, "exec"),
             namespace)
        with patch.object(sys, "argv", ["topic_modeling.py"]):
            namespace["main"]()
        self.assertEqual(calls, [{
            "topic": "ai4s",
            "skip_connections": False,
            "skip_classification": False,
            "min_cats": 8,
            "max_cats": 12,
        }])


class DeeperSimilarityTests(unittest.TestCase):
    """Run the emitted pure JS helpers, without a DOM, retrieval, or provider."""

    @classmethod
    def setUpClass(cls):
        cls.source = Path(PIPELINE, "build_topic_index.py").read_text(encoding="utf-8")
        tree = ast.parse(cls.source)
        cls.js = max(
            node.value.value for node in ast.walk(tree)
            if isinstance(node, ast.Assign) and isinstance(node.value, ast.Constant)
            and isinstance(node.value.value, str)
            and any(isinstance(target, ast.Name) and target.id == "JS"
                    for target in node.targets)
        )
        cls.labels = re.search(r"    const RELATION_KO = \{.*?\n    \};",
                               cls.js, re.S).group()

    def _function(self, name):
        match = re.search(r"    (?:async )?function " + re.escape(name)
                          + r"\([^\n]*\) \{.*?\n    \}", self.js, re.S)
        self.assertIsNotNone(match, name)
        return match.group()

    def _js(self, names, expression, data):
        script = ("const data = JSON.parse(require('node:fs').readFileSync(0, 'utf8'));\n"
                  + self.labels + "\n"
                  + "\n".join(self._function(name) for name in names)
                  + "\nconsole.log(JSON.stringify(" + expression + "));\n")
        result = subprocess.run(["node", "-e", script], input=json.dumps(data, ensure_ascii=False),
                                text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout)

    def test_neighbor_ranking_uses_shared_seeds_not_relation_semantics(self):
        def edge(slug, relation, cosine=.9, basis="embedding"):
            return {"slug": slug, "relation": relation, "basis": basis,
                    "reason": "unverified rebuttal", "evidence": {"cosine": cosine}}

        data = {
            "index": {"papers": {slug: {} for slug in
                                  ("A", "B", "shared", "first", "second", "third", "legacy")}},
            "conn": {
                "A": [edge("shared", "foundation"), edge("shared", "alternative"),
                      edge("first", "foundation"), edge("second", "alternative"),
                      edge("third", "counterpoint"), edge("legacy", "counterpoint", basis="model"),
                      edge("legacy", "alternative", basis="metadata"),
                      edge("legacy", "alternative", basis=None), edge("missing", "alternative"),
                      edge("B", "alternative"), None],
                "B": [edge("shared", "alternative", .94)],
            },
        }
        ranked = self._js(["rankConnectedPapers"],
                          "rankConnectedPapers(data.index, new Set(['A', 'B']), data.conn)", data)
        self.assertEqual([item["slug"] for item in ranked], ["shared", "first", "second", "third"])
        self.assertEqual([item["count"] for item in ranked], [2, 1, 1, 1])
        self.assertEqual(ranked[0]["evidence"], {"cosine": .94})
        self.assertTrue(all(item["relation"] == "alternative" for item in ranked))
        self.assertTrue(all("reason" not in item for item in ranked))

    def test_neighbor_expansion_stays_bounded_and_handles_empty_graphs(self):
        slugs = [f"neighbor-{i}" for i in range(85)]
        ranked = self._js(["rankConnectedPapers"], "({"
                          "ranked: rankConnectedPapers(data.index, new Set(['seed']), data.conn),"
                          "empty: rankConnectedPapers(data.index, new Set(['seed']), {})})", {
                              "index": {"papers": {slug: {} for slug in slugs}},
                              "conn": {"seed": [{"slug": slug, "basis": "embedding"}
                                                for slug in slugs]},
                          })
        self.assertEqual([item["slug"] for item in ranked["ranked"]], slugs[:80])
        self.assertEqual(ranked["empty"], [])

    def test_prompts_expose_numeric_similarity_not_unverified_relation_reasons(self):
        selected = [{"slug": "neighbor", "paper": {"title": "Neighbor", "year": "2025"},
                     "chunks": [{"section": "Essence", "text": "The study measures accuracy."}],
                     "isSeed": False, "basis": "embedding", "relation": "counterpoint",
                     "reason": "unverified rebuttal", "evidence": {"cosine": .812345}}]
        result = self._js(["connectionEvidenceTag", "buildPrompt", "buildEvidenceText"], "({"
                          "ko: buildPrompt('question', data, 'ko', null, true),"
                          "en: buildPrompt('question', data, 'en', null, true),"
                          "plain: buildPrompt('question', data, 'ko', null, false),"
                          "evidence: buildEvidenceText(data, null, {neighbor: 'Original detail.'}),"
                          "excluded: buildEvidenceText(data, new Set(), null),"
                          "seed: connectionEvidenceTag({...data[0], isSeed: true}),"
                          "legacy: connectionEvidenceTag({...data[0], basis: 'model'}),"
                          "nonnumeric: connectionEvidenceTag({...data[0], evidence: {cosine: '0.9'}})"
                          "})", selected)
        for text in (result["ko"]["user"], result["en"]["user"], result["evidence"]):
            self.assertIn("유사 연구", text)
            self.assertIn("cosine 0.8123", text)
            self.assertIn("논문 간 관계 미검증", text)
            self.assertNotIn("[연결관계:", text)
            self.assertNotIn("unverified rebuttal", text)
        self.assertIn("발췌에 명시된 근거가 있을 때만", result["ko"]["user"])
        self.assertIn("only when explicitly supported by the excerpts", result["en"]["user"])
        self.assertIn("Original detail.", result["evidence"])
        self.assertNotIn("Neighbor", result["excluded"])
        self.assertEqual(result["seed"], "")
        self.assertEqual(result["legacy"], "")
        self.assertNotIn("cosine", result["nonnumeric"])
        self.assertEqual(result["ko"]["system"], result["plain"]["system"])

    def test_fallback_outline_compares_papers_without_inventing_lineage(self):
        result = self._js(["defaultSections"], "({"
                          "ko: defaultSections(data, 'ko'), en: defaultSections(data, 'en'),"
                          "seedOnly: defaultSections([data[0]], 'en'),"
                          "label: RELATION_KO.alternative})",
                          [{"isSeed": True}, {"isSeed": False, "relation": "alternative"}])
        self.assertEqual(result["label"], "유사 연구")
        self.assertIn("유사 연구 비교", [section["title"] for section in result["ko"]])
        self.assertIn("Comparison with Similar Research", [section["title"] for section in result["en"]])
        self.assertEqual(len(result["seedOnly"]), 3)
        outline = json.dumps(result, ensure_ascii=False)
        for invented in ("반론", "대안", "Counterpoints", "Alternatives", "Foundations"):
            self.assertNotIn(invented, outline)

    def test_planner_writer_and_assembler_do_not_promote_similarity_to_evidence(self):
        planner = self._function("planReportSections")
        writer = self._function("writeSection")
        assembler = self._function("assembleReport")
        self.assertIn("Do not infer research lineage from titles or similarity", planner)
        self.assertIn("유사도만으로 연구 계보를 추론하지 마세요", planner)
        self.assertIn("not evidence of foundation", writer)
        self.assertIn("발췌에 명시된 경우에만", writer)
        self.assertIn("never invent research lineage", assembler)
        self.assertIn("임베딩 유사도만으로", assembler)
        self.assertIn("RELATION_KO.alternative", self._function("deepRenderExpansion"))
        self.assertIn("핵심 논문의 임베딩 유사 연구를 추가 검색", self.source)
        for obsolete in ("relBoost", "dissent", "[연결관계:", "revealing the research lineage",
                         "make the research lineage", "연결된 후속·반론·기반"):
            self.assertNotIn(obsolete, self.js)

    def test_schema_diagram_describes_embedding_and_numeric_evidence(self):
        tree = ast.parse(Path(PIPELINE, "generate_schema_diagram.py").read_text(encoding="utf-8"))
        notes = next(ast.literal_eval(node.value) for node in tree.body
                     if isinstance(node, ast.Assign)
                     and any(isinstance(target, ast.Name) and target.id == "NOTES"
                             for target in node.targets))
        note = notes["paper_connections"]
        self.assertIn("Embedding-space similarity", note)
        self.assertIn("numeric cosine", note)
        self.assertIn("No LLM", note)
        self.assertNotIn("LLM claims", note)
        self.assertNotIn("every row names the model", note)


class RefreshPublishedViewTests(unittest.TestCase):
    """Legacy invalidation uses actual JSON views in an isolated temp corpus."""

    def setUp(self):
        self.stack = contextlib.ExitStack()
        self.addCleanup(self.stack.close)
        root = Path(self.stack.enter_context(tempfile.TemporaryDirectory()))
        self.docs, self.papers = root / "docs", root / "docs" / "papers"
        self.papers.mkdir(parents=True)
        self.slug, self.old, self.incoming = "001_Source", "002_Legacy_Model", "003_Legacy_Metadata"
        self.unrelated, self.new, self.keep = "004_Unrelated_Legacy", "005_New", "006_Keep"
        self.index = [{"slug": slug, "topics": [topic]} for slug, topic in (
            (self.slug, "z_demo"), (self.old, "a_old"), (self.incoming, "m_old"),
            (self.unrelated, "z_demo"), (self.new, "z_demo"), (self.keep, "z_demo"))]
        self.index[3]["topics"].append("untouched")
        self._write(self.papers / "_papers_index.json", self.index)
        self.global_path = self.papers / "_global_connections.json"
        self.connections = importlib.import_module("lib.connections")
        clean_global = {self.keep: [{"slug": self.new, "basis": "embedding", "relation": "alternative",
                                    "reason": "embedding neighbour", "evidence": {"cosine": .7},
                                    "model": "", "source_topic": "z_demo"}]}
        self.clean_view = self.connections.make_bidirectional_deduped(clean_global)
        self._write(self.global_path, {
            self.slug: [{"slug": self.old, "basis": "model", "source_topic": "z_demo"}],
            self.incoming: [{"slug": self.slug, "basis": "metadata", "source_topic": "m_old"}],
            self.unrelated: [{"slug": self.incoming, "basis": "model", "source_topic": "z_demo"}],
            **clean_global,
        })
        self._write(self.docs / "z_demo" / "_paper_connections.json", {
            self.slug: [{"slug": self.old, "basis": "model"}],
            self.unrelated: [{"slug": self.incoming, "basis": "model"}],
            **self.clean_view,
        })
        self._write(self.docs / "a_old" / "_paper_connections.json",
                    {self.old: [{"slug": self.slug, "basis": "model"}]})
        self._write(self.docs / "m_old" / "_paper_connections.json",
                    {self.incoming: [{"slug": self.slug, "basis": "metadata"}]})
        self.untouched_view = {self.unrelated: [{"slug": self.incoming, "basis": "model"}]}
        self._write(self.docs / "untouched" / "_paper_connections.json", self.untouched_view)
        self.mod = importlib.import_module("refresh_paper_connections")
        self.stack.enter_context(patch.multiple(self.mod, PAPERS_DIR=self.papers, DOCS_DIR=self.docs))
        self.stack.enter_context(patch.multiple(self.connections, PAPERS_DIR=str(self.papers),
                                               GLOBAL_CONN_PATH=str(self.global_path)))
        self.stack.enter_context(patch.object(self.mod, "plan_connections", return_value={}))
        self.stack.enter_context(patch.object(self.mod, "_context",
                                              return_value=(self.index[0], self.index, ["z_demo"])))
        self.embedding = self.stack.enter_context(patch.object(
            self.mod, "_embedding_for_target", return_value=(self.index, "unused vectors")))
        topic_modeling = types.ModuleType("topic_modeling")
        topic_modeling.RELATED_RRF_K = 60
        topic_modeling.compute_related_candidates = lambda *_a, **_k: {self.slug: self.candidates}
        renderer = types.ModuleType("review_to_html")
        renderer._run_review_to_html = self._render
        self.stack.enter_context(patch.dict(sys.modules, {"topic_modeling": topic_modeling,
                                                        "review_to_html": renderer,
                                                        "anthropic": None, "openai": None}))
        self.stack.enter_context(patch("lib.corpus_store.corpus_operation_lock", self._lease))
        snapshot = self.mod._published_topic_connections

        def snapshot_under_lease():
            self.assertTrue(self.locked)
            return snapshot()

        self.stack.enter_context(patch.object(self.mod, "_published_topic_connections", snapshot_under_lease))
        self.locked, self.candidates, self.rendered = False, [], []

    @staticmethod
    def _write(path, value):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value, ensure_ascii=False), encoding="utf-8")

    @contextlib.contextmanager
    def _lease(self, root, *, exclusive):
        self.assertEqual(root, self.papers)
        self.assertTrue(exclusive)
        self.assertFalse(self.locked)
        self.locked = True
        try:
            yield
        finally:
            self.locked = False

    def _render(self, *, slugs, with_connected):
        self.assertTrue(self.locked)
        self.assertFalse(with_connected)
        self.rendered = slugs
        return {"converted": len(slugs), "skipped": 0}

    def _view(self, topic):
        return json.loads((self.docs / topic / "_paper_connections.json").read_text(encoding="utf-8"))

    def _publish_clean_cross(self):
        stored = self.connections.load_global_connections()
        stored[self.slug] = [{**entry, "source_topic": "z_demo"} for entry in
                             build_connections({self.slug: [(self.new, .8123)]}, self.index)[self.slug]]
        stored[self.old] = []
        self._write(self.global_path, stored)
        view = self.connections.make_bidirectional_deduped(stored)
        for topic in ("z_demo", "a_old", "m_old", "untouched", "_cross"):
            slugs = [paper["slug"] for paper in self.index
                     if topic == "_cross" or topic in paper["topics"]]
            self._write(self.docs / topic / "_paper_connections.json",
                        self.connections.filter_for_topic(view, slugs))
        self.candidates = [(self.new, .8123)]
        return view

    def test_empty_refresh_clears_legacy_outgoing_incoming_and_other_rewritten_sources(self):
        self.assertEqual(self.connections.load_global_connections()[self.slug], [])
        result = self.mod.refresh_connections(self.slug)
        self.assertEqual(result["status"], "completed")
        self.assertEqual(result["related_count"], 0)
        self.assertEqual(result["topics"], ["a_old", "m_old", "z_demo"])
        self.assertEqual(set(self.rendered), {self.slug, self.old, self.incoming, self.unrelated})
        self.assertEqual(self._view("a_old"), {self.old: []})
        self.assertEqual(self._view("m_old"), {self.incoming: []})
        self.assertEqual(self._view("z_demo")[self.slug], [])
        self.assertEqual(self._view("z_demo")[self.unrelated], [])
        self.assertEqual(self._view("z_demo")[self.keep], self.clean_view[self.keep])
        self.assertEqual(self._view("z_demo")[self.new], self.clean_view[self.new])
        self.assertEqual(self._view("untouched"), self.untouched_view)
        for slug in (self.old, self.incoming, self.unrelated):
            self.assertIn(str(self.papers / slug / "index.html"), result["outputs"])
        self.assertFalse(self.locked)

    def test_new_neighbor_does_not_hide_removed_legacy_neighbor_invalidation(self):
        self.candidates = [(self.new, .8123)]
        result = self.mod.refresh_connections(self.slug)
        self.assertEqual(result["related_count"], 1)
        self.assertEqual(set(self.rendered), {self.slug, self.old, self.incoming, self.unrelated, self.new})
        (edge,) = self._view("z_demo")[self.slug]
        self.assertEqual((edge["slug"], edge["basis"], edge["evidence"]),
                         (self.new, "embedding", {"cosine": .8123}))
        self.assertEqual(self._view("a_old")[self.old], [])

    def test_cross_projection_preserves_all_indexed_sources_and_unrelated_clean_edges(self):
        previous = self._publish_clean_cross()
        self.candidates = [(self.old, .91)]
        result = self.mod.refresh_connections(self.slug)
        expected = self.connections.make_bidirectional_deduped(self.connections.load_global_connections())
        self.assertIn("_cross", result["topics"])
        self.assertEqual(self._view("_cross"), expected)
        self.assertEqual(set(self._view("_cross")), {paper["slug"] for paper in self.index})
        self.assertEqual(self._view("_cross")[self.keep], previous[self.keep])
        self.assertEqual(self._view("_cross")[self.slug][0]["slug"], self.old)
        self.assertEqual(set(self.rendered), {self.slug, self.old, self.new})

    def test_fresh_cross_does_not_rerender_unrelated_clean_pages(self):
        previous = self._publish_clean_cross()
        stored = self.global_path.read_bytes()
        result = self.mod.refresh_connections(self.slug)
        self.assertEqual(result["topics"], ["_cross", "z_demo"])
        self.assertEqual(self._view("_cross"), previous)
        self.assertEqual(json.loads(self.global_path.read_bytes()), json.loads(stored))
        self.assertEqual(set(self.rendered), {self.slug, self.new})
        for slug in (self.old, self.incoming, self.unrelated, self.keep):
            self.assertNotIn(str(self.papers / slug / "index.html"), result["outputs"])

    def test_deleted_view_only_legacy_source_gets_an_explicit_empty_global_key(self):
        stored = json.loads(self.global_path.read_text(encoding="utf-8"))
        del stored[self.unrelated]
        self._write(self.global_path, stored)
        self._write(self.docs / "_cross" / "_paper_connections.json",
                    self._view("z_demo") | self._view("a_old") | self._view("m_old"))
        self.mod.refresh_connections(self.slug)
        self.assertEqual(self.connections.load_global_connections()[self.unrelated], [])
        self.assertEqual(self._view("z_demo")[self.unrelated], [])
        self.assertEqual(self._view("_cross")[self.unrelated], [])
        self.assertEqual(self._view("_cross")[self.keep], self.clean_view[self.keep])
        self.assertEqual(set(self.rendered), {self.slug, self.old, self.incoming, self.unrelated})

    def test_malformed_published_snapshot_fails_before_embedding_or_publication(self):
        before = self.global_path.read_bytes()
        self._write(self.docs / "z_demo" / "_paper_connections.json", {self.slug: [42]})
        with patch.object(self.connections, "merge_to_global") as publish:
            with self.assertRaisesRegex(ValueError, "invalid published connections"):
                self.mod.refresh_connections(self.slug)
        publish.assert_not_called()
        self.embedding.assert_not_called()
        self.assertEqual(self.global_path.read_bytes(), before)
        self.assertFalse(self.locked)


if __name__ == "__main__":
    unittest.main()
