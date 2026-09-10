import unittest
import sys
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from text_task import run


class TextTaskTests(unittest.TestCase):
    def setUp(self):
        self.request = {"schema_version": 1, "feature": "summary", "provider": "ollama",
                        "sources": [{"id": "one", "title": "One", "text": "Supported fact."}]}

    def test_plan_is_network_free_and_has_stable_input_hash(self):
        with patch("text_task.generate_structured") as call:
            first = run(self.request)
            second = run(self.request)
        call.assert_not_called()
        self.assertEqual(first["input_sha256"], second["input_sha256"])
        self.assertEqual(first["data_destinations"], ["ollama"])

    def test_budget_without_rates_blocks_before_model_call(self):
        request = self.request | {"provider": "anthropic", "max_cost_usd": 1}
        with patch("text_task.generate_structured") as call, patch("lib.credentials.credential_status", return_value={"configured": False, "reference": "credential:anthropic"}):
            result = run(request, execute=True)
        self.assertEqual(result["status"], "budget-unavailable")
        call.assert_not_called()

    def test_local_zero_api_budget_needs_no_cloud_rates(self):
        result = run(self.request | {"max_cost_usd": 0})
        self.assertEqual(result["status"], "ready")
        self.assertEqual(result["cost_estimate_usd"], 0)

    def test_execution_rejects_unsupported_citation(self):
        payload = {"data": {"status": "completed", "claims": [{"text": "claim", "source_id": "other", "quote": "no"}]}}
        with patch("text_task.generate_structured", return_value=payload):
            result = run(self.request, execute=True)
        self.assertEqual(result["status"], "failed")

    def test_plan_hash_matches_execution_provenance_input(self):
        payload = {"data": {"status": "completed", "claims": [{"text": "fact", "source_id": "one", "quote": "Supported fact."}]},
                   "provenance": {"input_sha256": "placeholder"}}
        planned = run(self.request)
        with patch("text_task.generate_structured", return_value=payload) as call:
            run(self.request, execute=True)
        self.assertEqual(call.call_args.args[3], "Feature: summary\nQuestion: \nSources:\n[one] One\nSupported fact.")
        system = call.call_args.args[2]
        self.assertEqual(planned["input_sha256"], __import__("hashlib").sha256((system + "\n" + call.call_args.args[3]).encode()).hexdigest())

    def test_insufficient_data_is_explicit_and_has_no_claims(self):
        payload = {"data": {"status": "insufficient-data", "claims": []}}
        with patch("text_task.generate_structured", return_value=payload):
            result = run(self.request, execute=True)
        self.assertEqual(result["status"], "insufficient-data")
        self.assertEqual(result["data"]["claims"], [])

    def test_insufficient_data_with_claims_is_rejected(self):
        payload = {"data": {"status": "insufficient-data", "claims": [{
            "text": "fact", "source_id": "one", "quote": "Supported fact.",
        }]}}
        with patch("text_task.generate_structured", return_value=payload):
            result = run(self.request, execute=True)
        self.assertEqual(result["status"], "failed")
        self.assertEqual(
            result["error"]["message"],
            "insufficient-data response must not contain claims",
        )

    def test_rejects_secret_and_boolean_limits(self):
        self.assertEqual(run(self.request | {"api_key": "secret"})["status"], "failed")
        self.assertEqual(run(self.request | {"max_output_tokens": True})["status"], "failed")


if __name__ == "__main__": unittest.main()
