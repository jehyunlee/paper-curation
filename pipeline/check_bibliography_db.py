#!/usr/bin/env python3
"""Validate bibliography DB and affiliation-2 registry projection."""
from __future__ import annotations
import argparse, hashlib, json, math, os, sqlite3
from datetime import date, datetime, timezone
from pathlib import Path
import build_bibliography_db as bib
ROOT = Path(__file__).resolve().parents[1]
PAPERS = ROOT / "docs" / "papers"
INDEX = PAPERS / "_papers_index.json"


def issue(conn, sql, message, issues):
    n = conn.execute(sql).fetchone()[0]
    if n:
        issues.append(f'{message}: {n}')


def projection_issues(conn, registry, issues):
    expected_orgs = {
        (
            row["organization_id"], row["canonical_name_en"], row["normalized_name"],
            row["organization_type"], "", row.get("country", ""), "unknown",
            row["status"], "", registry["registry_version"],
        )
        for row in registry["organizations"]
    }
    actual_orgs = {
        tuple(row) for row in conn.execute(
            "SELECT organization_id,canonical_name_en,normalized_name,organization_type,"
            "country_code,country_name_en,country_scope,status,created_event_id,"
            "registry_version FROM affiliation_organizations")
    }
    if actual_orgs != expected_orgs:
        issues.append("registry organization projection mismatch")
    expected_identifiers = {
        (
            "source" if item["authority"].startswith("source_") else item["authority"],
            item["value"], org["organization_id"], "active", "", "", "",
        )
        for org in registry["organizations"]
        for item in org.get("identifiers", [])
    }
    actual_identifiers = {
        tuple(row) for row in conn.execute(
            "SELECT authority,identifier_value,organization_id,status,valid_from,"
            "valid_to,evidence_id FROM affiliation_identifiers")
    }
    if actual_identifiers != expected_identifiers:
        issues.append("registry identifier projection mismatch")
    expected_aliases = {
        (row["alias_id"], row["name"], row["normalized_alias"], "", "source", "")
        for org in registry["organizations"] for row in org["aliases"]
    }
    actual_aliases = {
        tuple(row) for row in conn.execute(
            "SELECT alias_id,alias_text,normalized_alias,language_code,alias_type,"
            "created_event_id FROM affiliation_aliases")
    }
    if actual_aliases != expected_aliases:
        issues.append("registry alias projection mismatch")
    expected_candidates = {
        (row["alias_id"], row["organization_id"],
         row.get("country_discriminator", ""), "", 1.0, "accepted", "")
        for row in registry["alias_candidates"]
    }
    actual_candidates = {
        tuple(row) for row in conn.execute(
            "SELECT alias_id,organization_id,country_discriminator,evidence_id,"
            "confidence,review_status,event_id FROM affiliation_alias_candidates")
    }
    if actual_candidates != expected_candidates:
        issues.append("registry alias candidate projection mismatch")
    expected_edges = set()
    for row in registry["relationships"]:
        if row.get("status") not in {"accepted", "historical"}:
            continue
        interval = row.get("validity_interval") or {}
        expected_edges.add((
            row["relationship_id"],
            row["subject_organization_id"],
            row["object_organization_id"],
            row["relationship_type"],
            row.get("valid_from", interval.get("start", "")),
            row.get("valid_to", interval.get("end", "")),
            row["status"],
            float(row.get("confidence", 1.0)),
            row.get("created_event_id", ""),
            "registry",
        ))
    actual_edge_rows = {
        tuple(row) for row in conn.execute(
            "SELECT relationship_id,subject_organization_id,"
            "object_organization_id,relationship_type,valid_from,valid_to,"
            "status,confidence,created_event_id,managed_by "
            "FROM affiliation_relationships WHERE managed_by='registry'"
        )
    }
    if actual_edge_rows != expected_edges:
        issues.append("registry relationship projection mismatch")
    actual_edges = {row[0] for row in actual_edge_rows}
    evidence = {row["relationship_id"]: set(row.get("evidence_ids", []))
                for row in registry["relationships"] if row.get("status") in {"accepted", "historical"}}
    for relationship_id in actual_edges:
        actual = {row[0] for row in conn.execute(
            "SELECT evidence_id FROM affiliation_relationship_evidence WHERE relationship_id=?",
            (relationship_id,))}
        if actual != evidence.get(relationship_id, set()):
            issues.append("registry relationship evidence projection mismatch")
            break
    group_columns = {
        row[1] for row in conn.execute("PRAGMA table_info(institution_groups)")
    }
    institution_columns = {
        row[1] for row in conn.execute("PRAGMA table_info(institutions)")
    }
    if "organization_id" not in group_columns or "country_name_en" not in institution_columns:
        issues.append("collision-safe compatibility schema migration required")
    else:
        effective_date = max(
            (str(event.get("timestamp") or "")[:10]
             for event in registry.get("events", [])),
            default="",
        )
        precedence = {
            "part_of": 1, "jointly_operated_by": 2, "member_of": 3,
        }
        organizations = {
            row["organization_id"]: row for row in registry["organizations"]
        }
        choices = {}
        for edge in registry.get("relationships", []):
            kind = edge.get("relationship_type")
            interval = edge.get("validity_interval") or {}
            start = edge.get("valid_from", interval.get("start", ""))
            end = edge.get("valid_to", interval.get("end", ""))
            subject = organizations.get(edge.get("subject_organization_id"))
            parent = organizations.get(edge.get("object_organization_id"))
            if (edge.get("status") != "accepted" or kind not in precedence
                    or not subject or not parent
                    or subject.get("status") == "proposed"
                    or parent.get("status") == "proposed"
                    or (start and effective_date < start)
                    or (end and effective_date >= end)):
                continue
            choices.setdefault(edge["subject_organization_id"], []).append(
                (precedence[kind], edge["object_organization_id"]))
        expected_groups = {}
        for subject, candidates in choices.items():
            rank = min(item[0] for item in candidates)
            targets = {target for value, target in candidates if value == rank}
            if len(targets) == 1:
                expected_groups[subject] = next(iter(targets))
        expected_group_rows = {
            (organizations[parent]["canonical_name_en"],
             bib.affiliation_registry.normalize_name(
                 organizations[parent]["canonical_name_en"]),
             parent)
            for parent in expected_groups.values()
        }
        group_rows = list(conn.execute(
            "SELECT group_name,normalized_name,organization_id FROM institution_groups"
        ))
        if any(organization_id not in organizations
               for _name, _normalized, organization_id in group_rows):
            issues.append("orphan compatibility group organization")
        if set(group_rows) != expected_group_rows or len(group_rows) != len(expected_group_rows):
            issues.append("compatibility group table projection mismatch")
        assigned_groups = list(conn.execute(
            "SELECT i.organization_id,g.organization_id FROM institutions i "
            "LEFT JOIN institution_groups g ON g.group_id=i.group_id "
            "WHERE i.group_id IS NOT NULL"
        ))
        if any(subject is None or parent is None
               for subject, parent in assigned_groups):
            issues.append("unbound compatibility group assignment")
        actual_groups = {
            (subject, parent) for subject, parent in assigned_groups
            if subject is not None and parent is not None
        }
        if actual_groups != set(expected_groups.items()):
            issues.append("compatibility group projection mismatch")

def correction_projection_issues(path, registry, issues):
    try:
        raw = path.read_bytes()
        if raw and not raw.endswith(b"\n"):
            raise ValueError("missing final LF")
        rows = []
        for line in raw.splitlines(keepends=True):
            if not line.endswith(b"\n"):
                raise ValueError("missing final LF")
            row = json.loads(line.decode("utf-8"))
            if bib.affiliation_registry.canonical_json_bytes(row) != line:
                raise ValueError("non-canonical JSONL record")
            rows.append(row)
    except (OSError, UnicodeDecodeError, ValueError, json.JSONDecodeError) as exc:
        issues.append(f"correction ledger invalid: {exc}")
        return
    if rows != bib.affiliation_registry.correction_projection(registry):
        issues.append("registry correction ledger projection mismatch")

def operational_threshold_issues(approved, current):
    """Return deterministic release-threshold violations for one snapshot pair."""
    violations = []
    current_observations = int(current["current_observation_count"])
    active_pending = int(current["active_pending_total"])
    growth_allowance = max(5, math.ceil(0.005 * current_observations))
    if active_pending > int(approved.get("active_pending_total", 0)) + growth_allowance:
        violations.append(
            "active affiliation backlog exceeds baseline allowance: "
            f"{active_pending}>{approved.get('active_pending_total', 0)}+{growth_allowance}"
        )
    new_observations = max(
        0, current_observations - int(
            approved.get("current_observation_count", current_observations)))
    new_active_pending = max(
        0, active_pending - int(
            approved.get("active_pending_total", active_pending)))
    new_pending_allowance = max(5, math.ceil(0.01 * new_observations))
    if new_active_pending > new_pending_allowance:
        violations.append(
            "new active affiliation backlog exceeds per-run allowance: "
            f"{new_active_pending}>{new_pending_allowance} "
            f"for {new_observations} new observations"
        )
    oldest_age = int(current["oldest_active_age_days"])
    if oldest_age > 30:
        violations.append(
            f"oldest active affiliation case exceeds 30 days: {oldest_age}")
    mismatch_count = int(current["identity_country_mismatches"])
    if mismatch_count > int(approved.get("identity_country_mismatches", 0)) + 3:
        violations.append(
            "identity/country mismatch backlog exceeds baseline allowance: "
            f"{mismatch_count}>{approved.get('identity_country_mismatches', 0)}+3"
        )
    approved_shares = approved.get("group_shares") or {}
    for group_name, share in current.get("group_shares", {}).items():
        baseline_share = float(approved_shares.get(group_name, 0.0))
        if share > 0.35 or share > baseline_share + 0.05:
            violations.append(
                f"group share drift exceeds release threshold: {group_name}={share:.4f} "
                f"(baseline={baseline_share:.4f})"
            )
    return violations


def operational_baseline_issues(conn, baseline, registry, report, issues):
    """Enforce complete provenance and bounded release drift from the approved snapshot."""
    approved = baseline.get("database_baseline")
    if not isinstance(approved, dict) or not approved:
        issues.append("database operational baseline missing")
        return
    required_metrics = {
        "current_observation_count", "active_pending_total", "active_pending_case_count",
        "lifetime_pending_total", "oldest_active_age_days", "identity_country_mismatches",
        "observation_version_count", "superseded_observation_count",
    }
    required_provenance = {
        "captured_at", "registry_sha256", "event_head", "base_generation",
        "migration_receipt_id", "relationship_cardinality_histogram", "group_shares",
    }
    missing = (required_metrics | required_provenance) - approved.keys()
    if missing:
        issues.append("database operational baseline provenance missing: " + ",".join(sorted(missing)))
        return
    try:
        datetime.strptime(approved["captured_at"], "%Y-%m-%dT%H:%M:%SZ")
    except (TypeError, ValueError):
        issues.append("database operational baseline capture timestamp invalid")
    if (approved["registry_sha256"] != baseline.get("registry_sha256")
            or approved["registry_sha256"] != hashlib.sha256(
                bib.affiliation_registry.canonical_json_bytes(registry)).hexdigest()):
        issues.append("database operational baseline registry provenance mismatch")
    if approved["event_head"] != registry.get("event_head"):
        issues.append("database operational baseline event provenance mismatch")
    if (not isinstance(approved["base_generation"], int) or approved["base_generation"] < 0
            or not isinstance(approved["migration_receipt_id"], str)
            or not approved["migration_receipt_id"]):
        issues.append("database operational baseline migration provenance invalid")
    else:
        metadata = conn.execute(
            "SELECT registry_sha256,event_head,base_generation,migration_receipt_id "
            "FROM affiliation_registry_metadata WHERE singleton=1"
        ).fetchone()
        if not metadata:
            issues.append("database operational baseline metadata provenance missing")
        elif (approved["registry_sha256"], approved["event_head"],
              approved["base_generation"], approved["migration_receipt_id"]) != tuple(metadata):
            issues.append("database operational baseline metadata provenance mismatch")
    if (not isinstance(approved["relationship_cardinality_histogram"], dict)
            or not isinstance(approved["group_shares"], dict)
            or any(not isinstance(approved[key], int) or approved[key] < 0
                   for key in required_metrics)):
        issues.append("database operational baseline metric provenance invalid")
        return
    current_observations = conn.execute(
        "SELECT COUNT(*) FROM observed_affiliations WHERE is_current=1"
    ).fetchone()[0]
    active_pending = conn.execute(
        "SELECT COALESCE(SUM(active_observation_count),0) "
        "FROM affiliation_pending_cases WHERE status IN ('open','proposed')"
    ).fetchone()[0]
    active_cases = conn.execute(
        "SELECT COUNT(*) FROM affiliation_pending_cases "
        "WHERE status IN ('open','proposed')"
    ).fetchone()[0]
    lifetime_pending = conn.execute(
        "SELECT COALESCE(SUM(lifetime_observation_count),0) "
        "FROM affiliation_pending_cases"
    ).fetchone()[0]
    oldest_age = conn.execute(
        "SELECT COALESCE(MAX(0,CAST(julianday('now')-julianday(MIN(first_seen_at)) "
        "AS INTEGER)),0) FROM affiliation_pending_cases "
        "WHERE status IN ('open','proposed')"
    ).fetchone()[0]
    mismatch_count = conn.execute(
        "SELECT COUNT(*) FROM affiliation_pending_cases "
        "WHERE status IN ('open','proposed') AND reason_code LIKE '%country%'"
    ).fetchone()[0]
    version_count, superseded_count = conn.execute(
        "SELECT COUNT(*),COALESCE(SUM(is_current=0),0) FROM observed_affiliations"
    ).fetchone()
    cardinalities = {
        str(degree): count for degree, count in conn.execute(
            "SELECT degree,COUNT(*) FROM (SELECT o.organization_id,"
            "COUNT(r.relationship_id) degree FROM affiliation_organizations o "
            "LEFT JOIN affiliation_relationships r ON "
            "r.subject_organization_id=o.organization_id GROUP BY o.organization_id) "
            "GROUP BY degree ORDER BY degree")
    }
    compatibility_tables = {
        row[0] for row in conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table'")
    }
    group_shares = {}
    if {"paper_institutions", "institutions", "institution_groups"} <= compatibility_tables:
        denominator = conn.execute(
            "SELECT COUNT(DISTINCT paper_id) FROM paper_institutions"
        ).fetchone()[0]
        if denominator:
            group_shares = {
                name: count / denominator for name, count in conn.execute(
                    "SELECT g.group_name,COUNT(DISTINCT pi.paper_id) "
                    "FROM institution_groups g JOIN institutions i USING(group_id) "
                    "JOIN paper_institutions pi USING(institution_id) "
                    "GROUP BY g.group_id ORDER BY g.group_name")
            }
    current = {
        "current_observation_count": current_observations,
        "active_pending_total": active_pending,
        "active_pending_case_count": active_cases,
        "lifetime_pending_total": lifetime_pending,
        "oldest_active_age_days": oldest_age,
        "identity_country_mismatches": mismatch_count,
        "observation_version_count": version_count,
        "superseded_observation_count": superseded_count,
        "relationship_cardinality_histogram": cardinalities,
        "group_shares": group_shares,
    }
    report["affiliation_operational_baseline"] = approved
    report["affiliation_operational_current"] = current

    issues.extend(operational_threshold_issues(approved, current))


def rollback_validation_issues(db, marker):
    issues = []
    try:
        payload = json.loads(marker.read_text(encoding="utf-8"))
        receipt = json.loads(Path(payload["rollback_receipt"]).read_text(encoding="utf-8"))
        expected_schema = receipt["schema_version"]
        conn = sqlite3.connect(db)
        try:
            if conn.execute("PRAGMA quick_check").fetchone()[0] != "ok":
                issues.append("rollback database quick_check failed")
            actual_schema = (bib.AFFILIATION_SCHEMA_VERSION
                             if bib.is_latest_affiliation_schema(conn) else "legacy")
            if actual_schema != expected_schema:
                issues.append("rollback original-schema mismatch")
        finally:
            conn.close()
    except (OSError, KeyError, json.JSONDecodeError) as exc:
        issues.append(f"rollback receipt validation failed: {exc}")
    return issues


def evidence_issues(registry, release_date, issues, warnings):
    """Enforce official relationship evidence freshness at the release date."""
    try:
        released = date.fromisoformat(release_date)
    except (TypeError, ValueError):
        issues.append("relationship evidence release date invalid")
        return
    evidence_by_id = {
        item.get("evidence_id"): item
        for item in registry.get("evidence", []) if item.get("evidence_id")
    }
    for relationship in registry.get("relationships", []):
        if relationship.get("status") not in {"accepted", "historical"}:
            continue
        for evidence_id in relationship.get("evidence_ids", []):
            evidence = evidence_by_id.get(evidence_id)
            if not isinstance(evidence, dict):
                issues.append("relationship evidence missing from registry")
                continue
            revalidated_at = evidence.get("revalidated_at")
            try:
                validated = datetime.strptime(
                    revalidated_at, "%Y-%m-%dT%H:%M:%SZ").date()
            except (TypeError, ValueError):
                issues.append("relationship evidence revalidation timestamp invalid")
                continue
            age_days = (released - validated).days
            if age_days < 0:
                issues.append("relationship evidence revalidation is after release date")
            elif age_days > 90:
                issues.append("relationship evidence revalidation exceeds 90 days")
            elif age_days >= 60:
                warnings.append("relationship evidence revalidation due within 30 days")
def main(argv=None) -> int:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--db', type=Path, default=bib.DEFAULT_DB); ap.add_argument('--registry', type=Path, default=bib.REGISTRY_PATH)
    ap.add_argument('--baseline', type=Path, default=Path(__file__).with_name('affiliation_registry_baseline.json'))
    ap.add_argument('--release-date',
                    default=datetime.now(timezone.utc).date().isoformat())
    ap.add_argument('--strict', action='store_true'); ap.add_argument('--strict-warnings', action='store_true')
    args=ap.parse_args(argv); issues=[]; warnings=[]; report={'ok':False,'issues':issues,'warnings':warnings}
    marker = args.db.with_suffix(args.db.suffix + ".remigration-required.json")
    if marker.exists():
        issues.extend(rollback_validation_issues(args.db, marker))
        report["remigration_required"] = True
        report["ok"] = False
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 3
    baseline = None
    try:
        baseline = json.loads(args.baseline.read_text(encoding="utf-8"))
    except Exception as exc:
        issues.append(f"registry baseline read failed: {exc}")
    if not args.db.exists(): issues.append(f'missing database: {args.db}')
    else:
        conn=sqlite3.connect(args.db); conn.execute('PRAGMA foreign_keys=ON')
        tables={r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")}
        paper_columns = {row[1] for row in conn.execute("PRAGMA table_info(papers)")}
        if {"title", "review_dir"} <= paper_columns:
            count = conn.execute("SELECT COUNT(*) FROM papers").fetchone()[0]
            empty_titles = conn.execute(
                "SELECT COUNT(*) FROM papers WHERE title='' OR title IS NULL").fetchone()[0]
            bad_dirs = conn.execute(
                "SELECT COUNT(*) FROM papers WHERE review_dir='' OR review_dir IS NULL").fetchone()[0]
            institution_names = [row[0] for row in conn.execute(
                "SELECT institution_name FROM institutions").fetchall()]
            suspicious = [name for name in institution_names
                          if bib.is_suspicious_institution_name(name)]
            local_language = [name for name in institution_names
                              if bib.is_local_language_institution(name)]
            report.update({"db_papers": count, "empty_titles": empty_titles,
                           "empty_review_dirs": bad_dirs,
                           "institution_aliases": conn.execute(
                               "SELECT COUNT(*) FROM institution_aliases").fetchone()[0],
                           "country_links": conn.execute(
                               "SELECT COUNT(*) FROM paper_institutions WHERE country_name<>''").fetchone()[0],
                           "suspicious_institution_names": len(suspicious),
                           "local_language_institution_names": len(local_language)})
            if empty_titles:
                issues.append(f"empty titles: {empty_titles}")
            if bad_dirs:
                issues.append(f"empty review directories: {bad_dirs}")
            if suspicious:
                issues.append("suspicious institution names: " + ", ".join(suspicious[:10]))
            if local_language:
                issues.append("local-language institution names: " + ", ".join(local_language[:10]))
        if 'affiliation_registry_metadata' not in tables: issues.append('affiliation-2 migration required')
        else:
            try: registry=bib.affiliation_registry.load_registry(args.registry)
            except Exception as exc: issues.append(f'invalid registry: {exc}'); registry=None
            meta=conn.execute('SELECT schema_version,registry_sha256,event_head,policy_version,source_sha256,base_generation,migration_receipt_id FROM affiliation_registry_metadata WHERE singleton=1').fetchone()
            expected=hashlib.sha256(args.registry.read_bytes()).hexdigest() if args.registry.exists() else ''
            if not meta or meta[0]!=bib.AFFILIATION_SCHEMA_VERSION: issues.append('stale affiliation schema metadata')
            elif meta[1]!=expected or (registry and (meta[2],meta[3],meta[4]) != (registry['event_head'],registry['policy_version'],registry['source_sha256'])): issues.append('registry metadata digest/replay mismatch')
            if meta:
                migration_receipt_id = meta[6]
                if not migration_receipt_id:
                    issues.append("missing migration receipt binding")
                elif migration_receipt_id != "fresh-schema":
                    audit = conn.execute(
                        "SELECT base_generation,schema_to "
                        "FROM affiliation_migration_audit WHERE receipt_id=?",
                        (migration_receipt_id,)).fetchone()
                    if not audit:
                        issues.append("migration receipt binding missing from audit")
                    elif audit != (meta[5], bib.AFFILIATION_SCHEMA_VERSION):
                        issues.append("migration receipt metadata mismatch")
            if registry and baseline:
                registry_sha = hashlib.sha256(args.registry.read_bytes()).hexdigest()
                if baseline.get("schema_version") != bib.AFFILIATION_SCHEMA_VERSION:
                    issues.append("registry baseline schema mismatch")
                if baseline.get("registry_sha256") != registry_sha:
                    issues.append("registry baseline digest mismatch")
                if baseline.get("source_sha256") != registry.get("source_sha256"):
                    issues.append("registry baseline source mismatch")
                if baseline.get("policy_version") != registry.get("policy_version"):
                    issues.append("registry baseline policy mismatch")
                proposed = sum(
                    row.get("status") == "proposed"
                    for row in registry.get("relationship_proposals", []))
                accepted = sum(
                    row.get("status") in {"accepted", "historical"}
                    for row in registry.get("relationships", []))
                if baseline.get("proposed_relationship_edge_count") != proposed:
                    issues.append("registry baseline proposed-edge count mismatch")
                if baseline.get("accepted_official_relationship_edge_count") != accepted:
                    issues.append("registry baseline accepted-edge count mismatch")
                correction_projection_issues(
                    args.registry.with_name("affiliation_registry_corrections.jsonl"),
                    registry, issues)
                operational_baseline_issues(conn, baseline, registry, report, issues)
            if conn.execute('PRAGMA quick_check').fetchone()[0] != 'ok': issues.append('sqlite quick_check failed')
            if conn.execute('PRAGMA foreign_key_check').fetchone() is not None: issues.append('foreign key violation')
            issue(
                conn,
                "SELECT COUNT(*) FROM observed_affiliation_slots s WHERE "
                "(SELECT COUNT(*) FROM observed_affiliations o "
                " WHERE o.observation_slot_id=s.observation_slot_id AND o.is_current=1)>1 "
                "OR ((SELECT COUNT(*) FROM observed_affiliations o "
                "     WHERE o.observation_slot_id=s.observation_slot_id AND o.is_current=1)=1 "
                "    AND (SELECT observation_version FROM observed_affiliations o "
                "         WHERE o.observation_slot_id=s.observation_slot_id AND o.is_current=1)"
                "        <>(SELECT MAX(observation_version) FROM observed_affiliations o "
                "           WHERE o.observation_slot_id=s.observation_slot_id)) "
                "OR ((SELECT COUNT(*) FROM observed_affiliations o "
                "     WHERE o.observation_slot_id=s.observation_slot_id AND o.is_current=1)=0 "
                "    AND COALESCE((SELECT resolution_status FROM observed_affiliations o "
                "                  WHERE o.observation_slot_id=s.observation_slot_id "
                "                  ORDER BY observation_version DESC LIMIT 1),'')<>'superseded')",
                'slot current-version invariant',
                issues,
            )
            issue(conn,"SELECT COUNT(*) FROM affiliation_pending_cases WHERE active_observation_count<0 OR lifetime_observation_count<active_observation_count OR (status IN ('open','proposed') AND (active_observation_count=0 OR resolved_event_id<>'')) OR (status IN ('resolved','rejected') AND (active_observation_count<>0 OR resolved_event_id=''))",'pending status/count/terminal-reference invariant',issues)
            issue(conn,"SELECT COUNT(*) FROM affiliation_pending_cases p WHERE active_observation_count != (SELECT COUNT(*) FROM affiliation_pending_observations l JOIN observed_affiliations o USING(observation_id) WHERE l.pending_id=p.pending_id AND o.is_current=1 AND o.resolution_status IN ('ambiguous','unseen'))",'pending active recount mismatch',issues)
            issue(conn,"SELECT COUNT(*) FROM affiliation_pending_cases p WHERE lifetime_observation_count != (SELECT COUNT(*) FROM affiliation_pending_observations l WHERE l.pending_id=p.pending_id)",'pending lifetime recount mismatch',issues)
            issue(conn, "SELECT COUNT(*) FROM affiliation_pending_cases p LEFT JOIN affiliation_resolution_decisions d "
                        "ON d.decision_id=p.resolved_event_id WHERE "
                        "(p.status='resolved' AND (d.decision_id IS NULL OR d.outcome<>'resolved' OR d.reason_code='' "
                        "OR d.registry_sha256<>(SELECT registry_sha256 FROM affiliation_registry_metadata WHERE singleton=1) "
                        "OR d.policy_version<>(SELECT policy_version FROM affiliation_registry_metadata WHERE singleton=1))) "
                        "OR (p.status='rejected' AND (d.decision_id IS NULL OR d.outcome NOT IN ('rejected','superseded') OR d.reason_code='' "
                        "OR d.registry_sha256<>(SELECT registry_sha256 FROM affiliation_registry_metadata WHERE singleton=1) "
                        "OR d.policy_version<>(SELECT policy_version FROM affiliation_registry_metadata WHERE singleton=1)))",
                  'terminal decision ownership/outcome/reason/registry-policy invariant',issues)
            issue(conn,"SELECT COUNT(*) FROM affiliation_relationships r WHERE r.status='accepted' AND NOT EXISTS (SELECT 1 FROM affiliation_relationship_evidence e WHERE e.relationship_id=r.relationship_id)",'accepted relationship lacks evidence',issues)
            issue(conn,"SELECT COUNT(*) FROM affiliation_relationships WHERE subject_organization_id=object_organization_id",'self relationship',issues)
            required = {"affiliation_enrichment_attempts", "affiliation_resolution_decisions",
                        "affiliation_pending_observations", "affiliation_alias_candidates"}
            missing = required - tables
            if missing:
                issues.append("missing affiliation-2 tables: " + ",".join(sorted(missing)))
            issue(conn, "SELECT COUNT(*) FROM affiliation_pending_cases p WHERE "
                        "p.attempt_count<>(SELECT COUNT(*) FROM affiliation_enrichment_attempts a "
                        "WHERE a.pending_id=p.pending_id) OR "
                        "p.last_attempt_at<>COALESCE((SELECT MAX(a.finished_at) "
                        "FROM affiliation_enrichment_attempts a WHERE a.pending_id=p.pending_id),'')",
                  "pending attempt counter/timestamp invariant", issues)
            issue(conn, "SELECT COUNT(*) FROM affiliation_enrichment_attempts WHERE "
                        "provider NOT IN ('official','ror','wikidata','wikipedia','scopus') OR "
                        "outcome NOT IN ('success','no_match','unavailable','subscription_required',"
                        "'timeout','rate_limited','error','budget_exhausted')",
                  "attempt provider/outcome vocabulary invariant", issues)
            issue(conn, "SELECT COUNT(*) FROM observed_affiliations o LEFT JOIN affiliation_resolution_decisions d "
                        "ON d.decision_id=o.current_decision_id WHERE o.current_decision_id IS NULL OR d.observation_id<>o.observation_id",
                  "current decision ownership invariant", issues)
            issue(conn, "SELECT COUNT(*) FROM affiliation_resolution_decisions WHERE "
                        "(outcome='resolved' AND selected_organization_id IS NULL) OR "
                        "(outcome<>'resolved' AND selected_organization_id IS NOT NULL)",
                  "decision outcome/organization invariant", issues)
            issue(conn, "SELECT COUNT(*) FROM affiliation_relationships "
                        "WHERE managed_by<>'registry' OR status NOT IN ('accepted','historical')",
                  "non-registry relationship projection", issues)
            issue(conn, "WITH RECURSIVE walk(start,node,path) AS ("
                        "SELECT subject_organization_id,object_organization_id,subject_organization_id||','||object_organization_id "
                        "FROM affiliation_relationships UNION ALL "
                        "SELECT walk.start,r.object_organization_id,walk.path||','||r.object_organization_id "
                        "FROM walk JOIN affiliation_relationships r ON r.subject_organization_id=walk.node "
                        "WHERE instr(walk.path,r.object_organization_id)=0) "
                        "SELECT COUNT(*) FROM walk JOIN affiliation_relationships r "
                        "ON r.subject_organization_id=walk.node WHERE r.object_organization_id=walk.start",
                  "relationship cycle", issues)
            issue(conn, "SELECT COUNT(*) FROM affiliation_relationships WHERE "
                        "relationship_type NOT IN ('part_of','jointly_operated_by',"
                        "'member_of','network_member_of')",
                  "forbidden relationship type", issues)
            issue(conn, "SELECT COUNT(*) FROM affiliation_relationships WHERE "
                        "(valid_from<>'' AND valid_from NOT GLOB "
                        "'[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]') OR "
                        "(valid_to<>'' AND valid_to NOT GLOB "
                        "'[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]') OR "
                        "(valid_from<>'' AND valid_to<>'' AND valid_from>=valid_to)",
                  "invalid relationship interval", issues)
            issue(conn, "SELECT COUNT(*) FROM affiliation_relationships a "
                        "JOIN affiliation_relationships b ON "
                        "a.relationship_id<b.relationship_id AND "
                        "a.subject_organization_id=b.subject_organization_id AND "
                        "a.object_organization_id=b.object_organization_id AND "
                        "a.relationship_type=b.relationship_type AND "
                        "(a.valid_to='' OR b.valid_from='' OR b.valid_from<a.valid_to) AND "
                        "(b.valid_to='' OR a.valid_from='' OR a.valid_from<b.valid_to)",
                  "overlapping relationship interval", issues)
            issue(conn, "SELECT COUNT(*) FROM observed_affiliations o WHERE "
                        "(o.supersedes_observation_id IS NOT NULL AND NOT EXISTS "
                        "(SELECT 1 FROM observed_affiliations p WHERE "
                        "p.observation_id=o.supersedes_observation_id AND "
                        "p.superseded_by_observation_id=o.observation_id)) OR "
                        "(o.superseded_by_observation_id IS NOT NULL AND NOT EXISTS "
                        "(SELECT 1 FROM observed_affiliations n WHERE "
                        "n.observation_id=o.superseded_by_observation_id AND "
                        "n.supersedes_observation_id=o.observation_id))",
                  "observation supersession symmetry", issues)
            issue(conn, "SELECT COUNT(*) FROM observed_affiliations o WHERE "
                        "o.is_current=1 AND o.resolution_status='ambiguous' AND "
                        "(SELECT COUNT(*) FROM affiliation_decision_candidates c "
                        "WHERE c.decision_id=o.current_decision_id)<2",
                  "ambiguous decision candidate loss", issues)
            if registry:
                projection_issues(conn, registry, issues)
            # The registry API itself verifies event-chain ordering and accepted-edge policy.
            if registry:
                try: bib.affiliation_registry.validate_registry(registry)
                except Exception as exc: issues.append(f'registry replay/evidence invalid: {exc}')
                evidence_issues(registry, args.release_date, issues, warnings)
        conn.close()
    try:
        source_count = len(json.loads(INDEX.read_text(encoding="utf-8")))
        report["source_index_papers"] = source_count
        if "db_papers" in report and report["db_papers"] != source_count:
            issues.append(
                f"paper count mismatch: DB={report['db_papers']} index={source_count}")
    except Exception as exc:
        issues.append(f"index read failed: {exc}")
    report['ok']=not issues and (not args.strict_warnings or not warnings)
    print(json.dumps(report,ensure_ascii=False,indent=2))
    return 0 if report['ok'] or (not args.strict and not args.strict_warnings) else 2
if __name__=='__main__': raise SystemExit(main())
