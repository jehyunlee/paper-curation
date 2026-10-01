"""Collection-wide Zotero audit fetches children in paginated batches."""
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

PIPELINE = Path(__file__).resolve().parents[1]
if str(PIPELINE) not in sys.path:
    sys.path.insert(0, str(PIPELINE))

import audit_zotero_pdf as audit


def item(key, data):
    return {"key": key, "data": data}


class AuditTopicBatchingTests(unittest.TestCase):
    def test_collection_scan_groups_children_without_per_parent_requests(self):
        first_page = [
            item("PARENT1", {"itemType": "journalArticle", "title": "First"}),
            item("PARENT2", {"itemType": "journalArticle", "title": "Second"}),
            item("CHILD1", {"itemType": "attachment", "parentItem": "PARENT1"}),
            item("CHILD2", {"itemType": "note", "parentItem": "PARENT1"}),
        ]
        first_page.extend(
            item(f"TOP{number}", {"itemType": "journalArticle", "title": str(number)})
            for number in range(96)
        )
        second_page = [
            item("CHILD3", {"itemType": "attachment", "parentItem": "PARENT2"}),
            item("LAST", {"itemType": "journalArticle", "title": "Last"}),
        ]
        calls = []
        audited = []

        def fake_api(endpoint, params=None, retries=4):
            calls.append((endpoint, params))
            return first_page if params["start"] == 0 else second_page

        def fake_audit_item(value, *, check_content=True):
            audited.append(value)
            return {"key": value["key"], "flags": []}

        with tempfile.TemporaryDirectory() as directory, \
             patch.object(audit, "_api", side_effect=fake_api), \
             patch.object(audit, "get_collection_key", return_value="COLLECTION"), \
             patch.object(audit, "get_topic_dir", return_value=Path(directory)), \
             patch.object(audit, "audit_item", side_effect=fake_audit_item), \
             patch.object(audit, "list_children", side_effect=AssertionError("must not be called")), \
             patch.object(audit.time, "sleep"):
            report = audit.audit_topic("ai4s", check_content=False)

        self.assertEqual([params["start"] for _, params in calls], [0, 100])
        self.assertEqual({endpoint for endpoint, _ in calls}, {"collections/COLLECTION/items"})
        self.assertEqual(report["total_items"], 99)
        self.assertEqual({value["key"] for value in audited},
                         {"PARENT1", "PARENT2", "LAST", *[f"TOP{i}" for i in range(96)]})
        children = {value["key"]: value["_children"] for value in audited}
        self.assertEqual([child["key"] for child in children["PARENT1"]], ["CHILD1", "CHILD2"])
        self.assertEqual([child["key"] for child in children["PARENT2"]], ["CHILD3"])
        self.assertEqual(children["LAST"], [])

    def test_short_acronym_title_exact_match_is_not_mismatch(self):
        value = item("SHORT", {
            "itemType": "journalArticle",
            "title": "From AGI to ASI",
            "DOI": "",
        })
        value["_children"] = [item("PDF", {
            "itemType": "attachment",
            "contentType": "application/pdf",
            "filename": "unhelpful.pdf",
        })]
        text = ("From AGI to ASI Tim Genewein and colleagues. "
                + "Artificial general intelligence research " * 20)
        with patch.object(audit, "resolve_pdf_path", return_value=Path("paper.pdf")), \
             patch.object(audit, "pdf_first_page_text", return_value=text):
            result = audit.audit_item(value)

        self.assertNotIn("CONTENT_MISMATCH", result["flags"])
        self.assertTrue(result["detail"]["content_exact_title_hit"])


if __name__ == "__main__":
    unittest.main()
