# Paper-Curation Operations Manual

Detailed recipes, concurrency tuning, and recovery flows for the paper-curation pipeline.
## Affiliation registry proposal review
### Pinned operator-curated baseline import

The audited 4,747-record source may be accepted only through this explicit, SHA-pinned mode; it records `operator:jehyunlee` approval and hash-bound replay evidence. It is not a general trust switch:

```bash
python pipeline/audit_affiliation_registry.py import \
  --source <audited-fixed-4747-source.json> \
  --registry pipeline/affiliation_registry.json \
  --corrections pipeline/affiliation_registry_corrections.jsonl \
  --baseline pipeline/affiliation_registry_baseline.json \
  --operator-curated
```

The command rejects any source whose bytes do not match the pinned SHA-256 or whose record count is not exactly 4,747. New or unseen institutions, normal source imports, network resolution, and Scopus enrichment remain proposal-only until authoritative evidence or separate operator review; Scopus is never hierarchy authority.
### Official-only relationship transition

Before any automatic identity application, append the one-shot transition to the pinned import. Supply the canonical registry SHA-256 and event head from the validated current snapshot; begin with `--dry-run`, then publish the receipt. The receipt records the exact `2245 = official_retained + demoted_or_superseded` equation and complete pre-transition relationship-ID hash.

```bash
python pipeline/audit_affiliation_registry.py transition-relationship-policy \
  --registry pipeline/affiliation_registry.json \
  --corrections pipeline/affiliation_registry_corrections.jsonl \
  --baseline pipeline/affiliation_registry_baseline.json \
  --receipt .cache/affiliation-relationship-policy-2026-08-08.json \
  --timestamp 2026-08-08T00:00:00Z --effective-date 2026-08-08 \
  --expected-registry-sha256 <current-canonical-registry-sha256> \
  --expected-event-head <current-event-head> --dry-run
```

Re-run without `--dry-run` only after reviewing that receipt output. The transition preserves historical accepted evidence but retains an accepted relationship only when it already cites reviewed `authority=official` evidence; every other legacy edge becomes a proposal requiring reviewed official membership evidence. Do not hand-edit generated artifacts. Compatibility `group_id` may temporarily disappear while official relationship evidence is reviewed. Wikipedia, Scopus, ROR, and identity/correction facts never automatically establish a relationship.

The bibliography builder is deliberately offline. Run the resolver as a scheduled post-run job on either Mac; it appends every policy and provider result to proposal JSONL, while only provider-owned attempts enter `affiliation_enrichment_attempts`:

```bash
python pipeline/audit_affiliation_registry.py resolve-pending \
  --db .cache/bibliography.sqlite3 --registry pipeline/affiliation_registry.json \
  --proposals .cache/affiliation-proposals.jsonl --allow-network \
  --retrieved-at 2026-08-08T00:00:00Z
```

`--name` and `--country` support an explicit case. Verified-TLS ROR is queried first; only exact country-consistent identities are proposals, and ROR official URLs are recorded for organization/member-page review. Wikipedia exact-title lookup is a discovery fallback only; Scopus is optional metadata only. Each provider gets at most two attempts (one retry); five provider failures open the circuit breaker. Provider failures, limits, and missing credentials remain pending and return exit code 6 for a retryable incomplete batch. Faculty, School, College, and Department fragments are never guessed. Generic-fragment, request-budget, and circuit-breaker policy records remain in proposal JSONL but are never written as provider attempts.

Review proposal JSONL into a separate approved JSONL. Identity approval requires `confidence: 1.0` and exact country-consistent ROR evidence. Relationship approval requires an approved official organization/member-page URL and exact quote; seed labels and Scopus cannot establish membership. Apply under the sidecar lock, then Git-sync the tracked artifacts:

```bash
python pipeline/audit_affiliation_registry.py apply-approved \
  --registry pipeline/affiliation_registry.json \
  --corrections pipeline/affiliation_registry_corrections.jsonl \
  --baseline pipeline/affiliation_registry_baseline.json \
  --approvals reviewed-affiliation-approvals.jsonl \
  --timestamp 2026-08-08T00:00:00Z --effective-date 2026-08-08 \
  --expected-registry-sha256 <current-canonical-registry-sha256> \
  --expected-event-head <current-event-head> \
  --receipt .cache/affiliation-apply-approved-2026-08-08.json
```

Low-confidence or conflicting cases remain pending; never hand-edit registry artifacts. After projecting an approved registry into the bibliography DB, bind release drift thresholds to that reviewed snapshot. The strict checker then blocks publication when active unresolved observations grow beyond the bounded allowance, any unresolved case is older than 30 days, identity/country mismatches increase materially, or one umbrella group exceeds the concentration threshold.
### Affiliation identity freeze and publication protocol

Routine bibliography builds and review generation are offline: they only project already
accepted exact identifiers, aliases, and direct redirects. An observation with a missing
or unmappable country remains pending, except that an exact accepted external identifier
or one globally unique accepted survivor may be reported as a lookup-only result; neither
path creates, enriches, aliases, or merges an identity.

Country values use the tracked ISO 3166-1:2020 derivative from Debian `iso-codes`
4.18.0-1 (`data/iso_3166-1.json`, LGPL-2.1-or-later). The map version and canonical
hash are generation-bound. `CN`/China and `TW`/Taiwan remain distinct site codes;
a branch retains its physical site country, a legal entity its domicile, and parent
geography is obtained only through an accepted relationship. Multinational umbrellas
have `country_scope=multinational` and no country code. Only accepted `part_of` edges
may populate the legacy compatibility `group_id`; `jointly_operated_by` retains every JV
operator in the canonical graph but never supplies a compatibility parent. `member_of`
and `network_member_of` are likewise non-parental. Only the literal reviewed alias
manifest is accepted; there is no locale, package, fuzzy, transliteration, or successor
fallback. A map change needs data-owner and independent reviewer approval, a
`country_map_changed` event, correction events, reprojection, redisposition, and a
strict check before application.

The identity oracle is ROR Schema 2.1 at commit
`20ec1cf1edc3e0051de0ea2eae2bfdf536b9ba63`; the public-suffix oracle is the official
PSL snapshot `2026-07-25_14-20-03_UTC` commit
`e1b8015c3b2f0f4f8c18659c2480fc1a22c07b20` (MPL-2.0). Cache their raw bytes,
hashes, licenses, envelope/parser/extractor versions, and fixed fetch budgets in the
evidence-oracle manifest. Fetching has no proxy or runtime fallback: validate every DNS
answer as public, connect only to a vetted address, retain the original hostname for
SNI/certificate verification/Host through each redirect, and persist bounded extracted
quotes/digests rather than pages. Wikipedia is discovery-only; Scopus is optional
enrichment and never authority.
Before any network investigation, `pin-oracles` and `check-oracles` operate only on the
command-installed immutable cache; they never download substitutes. Freeze the exact
5,162 IDs with `freeze-pending-cohort --db … --registry … --cohort … --timestamp …`.
Investigate that artifact with `resolve-pending --db … --cohort … --evidence-dir …`;
each attempt carries its covered pending IDs and its immutable segment is fsynced before
the SQLite join. Evaluate with `evaluate-pending --registry … --db … --cohort …`.
The resulting artifact has one disjoint terminal disposition per frozen ID,
`UNCLASSIFIED=0`, and recomputed decision digest. `apply-investigated --dry-run` checks
that digest and current heads; `--canary` permits at most 50 eligible decisions and every
other batch permits at most 100. A zero-eligible cohort performs no identity mutation, but
is still a durable finalization: the decision segment and hash-chain ledger are fsynced,
all 5,162 dispositions join SQLite in one transaction, registry/cohort heads advance, and
the receipt plus generation descriptor are published descriptor-last.
`recover-investigated --db … --journal …` obtains the writer flock and finishes only
`PREPARED`, `LEDGER_DURABLE`, `DB_COMMITTED`, or `DESCRIPTOR_COMMITTED` journals;
unreferenced evidence and its index entry are quarantined rather than hand-deleted.

Run the audited sequence exactly: freeze the cohort and relationship heads; complete the
official-only relationship transition; investigate into immutable evidence segments;
dry-run at exact heads; apply a 50-decision canary, then no more than 100 decisions per
generation; project; strict-check; emit the cohort/disposition, source-ID/alias/redirect,
country, evidence, relationship, ledger, and generation reports; commit and push target
Git blobs; then publish the matching generation through CAS. A second host fetches Git
before CAS pull and proves DB/logical hashes, registry/event contracts, oracle/country
hashes, cohort, ledger, relationship equation, and strict result equality.

Use the stable local lock pathname only with POSIX advisory `flock`: shared for readers,
exclusive for writers and recovery. The pathname is not ownership and is never deleted;
kernel close, process death, and reboot release it. The Mac mini authority issues,
renews, and checks a 90-second monotonic lease under its own short `flock`, with a
durable increasing fence token and boot ID. Acquire remote lease before local exclusive;
a current unexpired token alone may advance the manifest. Do not use PID files, remote
`mkdir`, wall-clock early takeover, or manual lock/lease/manifest cleanup. On a failed
writer, acquire exclusive, recover only a proven journal state (or quarantine
unreferenced staging), revalidate heads, and retry. After owner death wait for lease
expiry; after authority reboot obtain a higher fence. A stale token, unknown hash,
descriptor mismatch, evidence gap, automatic relationship, duplicate active identity
key, or cohort/transition accounting mismatch blocks publication rather than bypassing
the gate.

```bash
python pipeline/audit_affiliation_registry.py apply-investigated \
  --registry pipeline/affiliation_registry.json \
  --decisions .cache/affiliation-decisions.json \
  --db .cache/bibliography.sqlite3 \
  --evidence-dir .cache/affiliation-evidence \
  --ledger .cache/affiliation-ledger.jsonl \
  --corrections pipeline/affiliation_registry_corrections.jsonl \
  --baseline pipeline/affiliation_registry_baseline.json \
  --receipt .cache/affiliation-apply-receipt.json \
  --journal .cache/affiliation-apply.journal \
  --generation-descriptor .cache/affiliation-generation.json \
  --timestamp 2026-08-09T01:59:00Z --effective-date 2026-08-09

python pipeline/audit_affiliation_registry.py snapshot-db-baseline \
  --db .cache/bibliography.sqlite3 \
  --registry pipeline/affiliation_registry.json \
  --baseline pipeline/affiliation_registry_baseline.json \
  --captured-at 2026-08-09T01:59:00Z

python pipeline/check_bibliography_db.py --strict --release-date 2026-08-09 \
  --db .cache/bibliography.sqlite3 \
  --registry pipeline/affiliation_registry.json \
  --baseline pipeline/affiliation_registry_baseline.json \
  --cohort .cache/affiliation-frozen-cohort.json \
  --decisions .cache/affiliation-decisions.json \
  --ledger .cache/affiliation-ledger.jsonl \
  --generation-descriptor .cache/affiliation-generation.json

python pipeline/audit_affiliation_registry.py report \
  --registry pipeline/affiliation_registry.json \
  --db .cache/bibliography.sqlite3 \
  --cohort .cache/affiliation-frozen-cohort.json \
  --decisions .cache/affiliation-decisions.json \
  --ledger .cache/affiliation-ledger.jsonl \
  --generation-descriptor .cache/affiliation-generation.json \
  > .cache/affiliation-final-report.json
```
The trigger-side dispatcher lives in `SKILL.md`; this file is the operator's reference.

## Pipeline overview

Single orchestrator: `pipeline/run_full.py` (3 axes — `--mode`,
`--source`, `--images`). Individual scripts under `pipeline/*.py` are
also importable as functions from `pipeline.api`:

```python
from pipeline.api import (
    search, register, sync, dedup_zotero,
    curate, classify, topic_model, category_summary, insights,
    timeline, network, search_index, topic_index, review_to_html,
    deploy, validate, audit_matching, fix_matching, cleanup,
)
```

## Modes (run_full.py)

| Mode | Default `--source` | Default `--images` | Purpose |
|------|--------------------|---------------------|---------|
| `curate` | `zotero` | `skip` | Pick up new papers; reuse existing reviews |
| `rebuild` | `zotero` | `all` | Regenerate everything (destructive — review.md/figures wiped) |
| `reclassify` | (none) | `changed` | Re-run topic_modeling + classify only |
| `retime` | (none) | `all` | Regenerate timeline narrative + images |
| `deploy` | (none) | `skip` | wrangler deploy + gh-pages sync + master push |
| `audit` | — | — | Standalone: PDF↔review mismatch audit |
| `fix-matching` | — | — | Standalone: delete artifacts for audit-flagged slugs |
| `dedup` | — | — | Standalone: Zotero collection dedup |
| `validate` | — | — | Standalone: post-build validation gate |

`--source web` adds search + register + sync as a preflight to `curate`.

## Common Commands

```bash
# Weekly run — web search + Zotero register + new-paper review
PYTHONUTF8=1 python pipeline/run_full.py --topic ai4s --mode curate --source web --days 7

# Local-only update (Zotero already has new papers)
PYTHONUTF8=1 python pipeline/run_full.py --topic ai4s --mode curate --source zotero

# Force-rebuild specific slugs (recovery)
PYTHONUTF8=1 python pipeline/run_full.py --topic ai4s --mode rebuild --slugs 088,1093 --strict-pdf

# Reclassify only (no LLM, HDBSCAN approximate_predict)
PYTHONUTF8=1 python pipeline/run_full.py --topic ai4s --mode reclassify

# Timeline narrative + images
PYTHONUTF8=1 python pipeline/run_full.py --topic ai4s --mode retime --images all

# Deploy
PYTHONUTF8=1 python pipeline/run_full.py --topic humanoid --mode deploy

# Dry-run (no execution)
PYTHONUTF8=1 python pipeline/run_full.py --topic ai4s --mode curate --source web --dry-run

# Citedby — PDF-first index + default timeline/narrative + localhost open
PYTHONUTF8=1 python pipeline/run_citedby.py \
  --doi 10.xxxx/xxxxx --slug 042_Some_Paper \
  --pdf-first --build-index --serve --open
```

## Safety flags

- `--strict-pdf` — block fuzzy PDF matching; ID (Zotero/DOI/arXiv) only
- `--slugs A,B,C` — restrict to specific slug prefixes
- `--dry-run` — print plan, no execution
- `--skip-dedup` / `--dedup-execute` — control Zotero dedup preflight
- `--yes` — bypass `--mode rebuild` confirmation gate

## Concurrency (Anthropic Tier 4 default)

`run_full.py --concurrency` and `run_update_force.py --concurrency`
control per-paper review parallelism. Default 16 (Tier 4). Lower
tiers should drop:

| Tier | Recommended |
|------|-------------|
| Free / 1 | 2–4 |
| 2 | 6–8 |
| 3 | 10–12 |
| **4** | **16–20** |

Phase 2 added per-category parallelism for the post-review phase:
- `CAT_SUMMARY_PARALLEL` (default 8) — Haiku per-category summaries
- `TIMELINE_NARRATIVE_PARALLEL` (default 8) — Opus per-category narratives
- `TIMELINE_IMAGE_PARALLEL` (default 4) — PaperBanana per-category images
- `EXTRACT_INSIGHTS_PARALLEL` (default 4) — Sonnet per-category paper_connections

Wall-clock for finalize phase: ~25 min → ~6 min at Tier 4.

## Python environment

**Standard: single conda env `py312` (Python 3.12).** `requirements.txt`
includes the clustering stack (umap-learn / hdbscan / sentence-transformers),
so topic modeling/classification runs in-process — no subprocess routing.

```bash
conda create -n py312 -c conda-forge python=3.12 pip -y
conda activate py312
pip install -r requirements.txt
brew install --cask temurin   # Java for opendataloader-pdf
```

## Korean network workarounds

- **HuggingFace LFS blocked**: download SPECTER2 via AWS S3 mirror to
  `.cache/base/`, then `topic_modeling.py` auto-detects:

  ```bash
  mkdir -p .cache && cd .cache
  curl -L -o specter2_0.tar.gz \
       "https://ai2-s2-research-public.s3.amazonaws.com/specter2_0/specter2_0.tar.gz"
  tar -xzf specter2_0.tar.gz
  ```

- **arXiv chronic 429**: `search_papers.py --skip-arxiv` (OpenAlex + S2 only)
- **OpenDataLoader fallback**: PyMuPDF takes over silently; install
  Temurin Java to get pdffigures2 structure
- **Anthropic stale connections (half-open sockets)**: the Related-Papers
  connection step defends itself automatically — multi-round retry (only
  stuck batches), zero-connection-papers-first ordering, and unfinished
  papers keep their previous connections (self-heals next cycle). If a
  local model is available, `--local-fallback` completes the remainder
  on the spot (measured: EXAONE-4.0-32B, ~32 s per 8-paper batch):

  ```bash
  # config.json — add a local_model block (Ollama example)
  #   "local_model": {
  #     "base_url": "http://localhost:11434/v1",
  #     "model": "exaone-4.0:latest",
  #     "num_ctx": 8192, "retries": 2, "batch_size": 8
  #   }
  PYTHONUTF8=1 python pipeline/run_full.py --topic ai4s --mode curate --source zotero --local-fallback
  ```

  Ollama is auto-detected (native API: per-request `num_ctx`, `think:false`);
  LM Studio/llama.cpp/vLLM use the OpenAI-compatible path. A dead endpoint
  is skipped silently — the pipeline never blocks on it.

## Schema v1 frontmatter (Phase 3)

Every `docs/papers/{slug}/review.md` carries YAML frontmatter
populated by `inject_frontmatter.py`. Readers prefer frontmatter over
body-regex parsing when `schema_version: v1` is present.

```yaml
---
title: "<full paper title>"
authors: ["First Last", ...]
date: "2021-07-15"
doi: "..."
primary_topic: ai4s
primary_category: "..."
all_categories: [...]
sub_categories: {"Category": "Sub-category", ...}
sub_category: "..."
scores:
  novelty: 5
  technical: 5
  significance: 5
  clarity: 4
  overall: 5
score: 5
essence: "..."
tags: [paper, ai4s, "ai4s/category-slug/sub-slug", ...]
schema_version: v1
---
```

Migration script: `pipeline/_archive/migrate_to_toolschema.py` (one-time, now archived). Originals are
preserved at `docs/papers/.legacy/{slug}_v0.md`. Re-running the
migration is idempotent (existing backups are kept).

## LLM tool-use + cache

Phase 3 migrated `write_review` and `extract_insights.cross_category`
to Anthropic tool-use schemas. Responses are forced into the schema
shape; the SDK retries on mismatch. Post-hoc fixers
(`fix_python_list_literals`, `fix_figure_paths`, `fix_evaluation_format`,
`validate_review_format`) are no longer invoked.

Each tool-use call is wrapped in `api._llm.cached_call` keyed on
`sha256(prompt || model || schema_version)`. Cache layout:

```
docs/papers/{slug}/.llm_cache/{hash}.json     # per-paper (write_review)
docs/{topic}/.llm_cache/{hash}.json           # per-topic (insights)
```

A re-run of `--mode rebuild` on an unchanged paper costs zero LLM
calls. Pass `force=True` to `cached_call` to bypass.

## Figure pre-validator (Phase 4)

`api.extract.pre_validate_figure(png_path)` runs before each Gemini
figure validation call. Heuristics: file size, dimensions, grayscale
variance. Skips ~30% of Gemini calls on obviously-invalid crops while
deferring borderline cases to the LLM.

## Retrieval quality regression

The tracked `pipeline/eval/retrieval_queries.jsonl` corpus contains five fixed
queries for each of the eight current collections. Query vectors are generated
once with Gemini `RETRIEVAL_QUERY` and committed, so routine evaluation is
offline and deterministic.

```bash
# Run all collections and reject recall@5 regressions beyond 0.025
python pipeline/evaluate_retrieval.py \
  --queries pipeline/eval/retrieval_queries.jsonl \
  --vectors pipeline/eval/retrieval_query_vectors.json \
  --all --baseline pipeline/eval/retrieval_baseline.json \
  --min-recall-at-5 0 --strict \
  --output pipeline/eval/results/latest.json \
  --failures pipeline/eval/results/failures.json

# Install the same test on macOS (Sunday 03:17)
scripts/install-retrieval-eval-launchd.sh
```
The installer mirrors only evaluator runtime, tracked corpus, baseline, and the
eight index sidecars to
`~/Library/Application Support/paper-curation/retrieval-eval/`. macOS
LaunchAgents cannot read a repository under `Documents` without TCC approval,
so the scheduled job evaluates this atomic snapshot and writes reports under
`~/Library/Logs/paper-curation/`. Successful orchestrated index rebuilds refresh
the snapshot automatically when the LaunchAgent is installed.

`run_update_force.py` rebuilds `_cross`, then hard-gates the rebuilt source
collection and `_cross` before deploy. The bootstrap labels are BM25 top-1
known-item targets, not exhaustive relevance judgments; therefore the active
gate detects regression from the tracked baseline rather than claiming a
0.95 absolute floor. Review observed failures before adding them to the query
set. Regenerate vectors explicitly after changing query bytes:

```bash
python pipeline/generate_retrieval_vectors.py \
  --queries pipeline/eval/retrieval_queries.jsonl \
  --output pipeline/eval/retrieval_query_vectors.json --force
```

Record measurement-driven model, chunking, or collection changes in
`pipeline/eval/retrieval_decisions.json`; do not revise labels merely to make a
gate pass.

## Citedby operations

`run_citedby.py` is a standalone tool rather than a `run_full.py` mode. For a reviewed
seed paper, pass its slug so all timestamped artifacts stay under that paper:

```bash
PYTHONUTF8=1 python pipeline/run_citedby.py \
  --doi 10.xxxx/xxxxx \
  --slug 042_Some_Paper \
  --pdf-first --build-index --serve --open
```

Default behavior and controls:

- Timeline narrative and PaperBanana image are **on by default**. Use
  `--no-timeline` only for a deliberately text-only or fast run.
- Timeline candidate generation and critique have a **1800-second wall-clock cap**.
  A timeout does not discard the report: the narrative and remaining sections are
  still written, with the image failure shown explicitly.
- `--pdf-first` applies the evidence order corpus review > Zotero PDF > abstract >
  title. Use `--build-index` with it to write `_citedby_index.json` plus the
  int8 embedding sidecar from those enriched sources.
- `--serve` reuses a healthy paper-curation server or starts one; `--open` launches
  the generated `http://localhost:8000/...` URL. Do not open the report as
  `file://` when using Deep(er) Research.
- The report and Deep(er) Research result have separate PDF, Markdown, Obsidian,
  and Audio controls. Screen links open local corpus reviews, print links switch
  to DOI/arXiv/source URLs, and Obsidian links target review Markdown or generated
  evidence notes.
- The local server must return 200 from `/api/health`. `/api/embed` needs
  `GOOGLE_API_KEY`; `/api/citedby-answer` uses the configured answer providers.
  A `304` for `_citedby_index_emb.bin` is a normal browser-cache hit.

Re-running the same command creates a new timestamped report and reuses available
corpus chunks, embeddings, and cached analysis. Source failures are soft: available
providers continue, and the final report records the surviving evidence.

## Deploy (Option O-1)

로컬 사용이 기본(Core)입니다. 외부 공유가 필요하면 **3-계층 split-host** 구조로 자동 배포됩니다:

| 계층 | 역할 | 내용 |
|------|------|------|
| **Cloudflare Workers (Static Assets + Function)** | 사용자 콘텐츠 서빙 + `/api/audio-email` 라우트 | `docs/` 전체 업로드 (`docs/.assetsignore`로 로컬 전용 토픽 제외) + `worker/index.js` (Audio Overview 이메일 발송 핸들러) |
| **GitHub `gh-pages` 브랜치** | 진입 URL → Cloudflare 리다이렉트 | 토픽별 리다이렉트 스텁 (1KB 미만), `jehyunlee.github.io/paper-curation/{topic}/` → 운영자가 설정한 Cloudflare URL |
| **GitHub `master` 브랜치** | 코드·설정·README | 대용량 `docs/papers/`, `docs/{topic}/` 콘텐츠는 `.gitignore`로 제외 |

```bash
# 배포 (환경변수 필요: CF_API_TOKEN + CLOUDFLARE_ACCOUNT_ID)
PYTHONUTF8=1 python pipeline/run_full.py --topic my_topic --mode deploy
```

자동 처리:
- PNG → WebP 변환 (용량 ~60% 절감)
- 배포용 HTML에서 API 키·로컬 이메일 제거 후 로컬 working tree 자동 복원
- `npx wrangler deploy` → Cloudflare 업로드 (해시 기반 증분 업로드) + Worker 함수 동시 배포
- gh-pages 리다이렉트 스텁 idempotent 동기화 (새 토픽 자동 감지, 변경 없으면 푸시 스킵)
- Cloudflare 200 OK 검증 (최대 5분 폴링)
- master에는 **코드·설정 변경만** commit + push (대용량 콘텐츠는 `.gitignore`)

환경변수 발급: Cloudflare Dashboard → My Profile → API Tokens → "Edit Cloudflare Workers" 템플릿.
```cmd
setx CF_API_TOKEN "..."
setx CLOUDFLARE_ACCOUNT_ID "..."
```

**Custom domain (권장)** — `wrangler.toml` 의 `[[routes]]` 블록에 `pattern = "your-subdomain.your-domain.tld"` + `custom_domain = true` + `zone_name = "your-domain.tld"` 를 박으면 `wrangler deploy` 가 Cloudflare DNS · SSL · 라우팅까지 자동 설정합니다. 동시에 `prepare_deploy.py` 의 `CF_BASE_URL` 도 같은 값으로 갱신해야 gh-pages 스텁이 새 도메인을 가리킵니다. workers.dev 기본 도메인으로도 동작은 하지만 메일 도메인 일관성을 위해 custom domain 권장.

**Cloudflare Worker secrets (이메일 + 질의 임베딩)** — `worker/index.js` 가 두 라우트를 노출합니다: `/api/audio-email` ([Resend](https://resend.com) API 로 MP3 첨부 메일 발송) + `/api/embed` (`gemini-embedding-001` 질의 임베딩 프록시 — 독자가 키 없이 검색하도록). `wrangler secret put` 으로 등록:

```bash
npx wrangler secret put GOOGLE_API_KEY    # /api/embed 질의 임베딩 프록시용 (gemini-embedding-001, 필수)
npx wrangler secret put RESEND_API_KEY    # Resend 대시보드의 re_xxx 키 (이메일 발송 필수)
npx wrangler secret put AUDIO_FROM        # 예: "Paper Curation <noreply@your-domain.tld>" (도메인 verify 필요)
npx wrangler secret put AUDIO_REPLY_TO    # 답장이 갈 운영자 메일, 예: "you@gmail.com" (선택)
```

- `GOOGLE_API_KEY` 가 없으면 `/api/embed` 가 실패해 Deep Research 검색이 동작하지 않습니다 (배포 시 필수). 로컬에서는 `pipeline/serve_local.py` 가 같은 역할을 합니다.
- `RESEND_API_KEY` 가 비어 있으면 `/api/audio-email` 이 503 을 반환하고, 클라이언트는 다운로드만으로 fallback 합니다.
- `AUDIO_FROM` 의 도메인은 Resend 에서 SPF/DKIM/DMARC TXT 3개를 등록해 verify 해두어야 임의 수신자에게 발송할 수 있습니다 (verify 전엔 Resend 계정 메일 1명만 가능).
- 로컬 빌드 시 운영자 본인 메일을 미리 박아두려면 `config.json` 에 `"local_emails": ["a@b.com", ...]` 또는 환경변수 `PAPER_CURATION_LOCAL_EMAILS="a@b.com,c@d.com"`. 배포 시 자동 strip 됩니다.

---


## Bibliography DB operations

The bibliography DB is the persistent memory layer for author, institution, country, DOI/URL, journal, date, Zotero key, and local review-directory queries. It is collection-independent and must be checked after corpus changes.
The Mac mini's `.cache/bibliography.sqlite3` is canonical. The MacBook keeps a local copy; `pipeline/sync_bibliography_db.py --pull` runs before review generation and `--push` runs afterward. Google Drive is backup/transport only, not a live SQLite volume.
Review generation also writes `.cache/review_progress.json`. The live phase label cycles through `PDF 매칭 → text.md 추출 → figure 추출 → review.md 생성 → HTML 변환`, while the log includes the completed/total percentage.
Bootstrap establishes generation zero only when the remote object and manifest are unchanged; run it once before the first CAS-protected push:
```bash
python pipeline/sync_bibliography_db.py --bootstrap
```
Every publish supplies the immutable pull/bootstrap receipt as `--base-receipt` (and
migration receipt when applicable). A strict affiliation generation also supplies the
complete all-or-nothing artifact set; each role is stored as an immutable hash-addressed
object and the descriptor is installed after the cohort, decisions, and ledger:
```bash
python pipeline/sync_bibliography_db.py --push \
  --base-receipt .cache/bibliography.base.json \
  --migration-receipt .cache/bibliography-migration.json \
  --cohort .cache/affiliation-frozen-cohort.json \
  --decisions .cache/affiliation-decisions.json \
  --ledger .cache/affiliation-ledger.jsonl \
  --generation-descriptor .cache/affiliation-generation.json

# The second host fetches/fast-forwards Git first, then stages and verifies every
# declared object before taking the local writer flock and installing descriptor-last.
python pipeline/sync_bibliography_db.py --pull \
  --cohort .cache/affiliation-frozen-cohort.json \
  --decisions .cache/affiliation-decisions.json \
  --ledger .cache/affiliation-ledger.jsonl \
  --generation-descriptor .cache/affiliation-generation.json
```
A missing, partial, or hash-mismatched declared artifact fails closed. All subsequent
migration/publish operations use the immutable pull/base receipt, not a reconstructed
receipt.

```bash
# Institution-centered literature search
PYTHONUTF8=1 python pipeline/query_bibliography.py --institution "Cambridge" --sort date

# Country / author / journal filters
PYTHONUTF8=1 python pipeline/query_bibliography.py --country "United Kingdom" --json
PYTHONUTF8=1 python pipeline/query_bibliography.py --author "Yuan" --sort date --desc

# Completeness gate
PYTHONUTF8=1 python pipeline/check_bibliography_db.py --strict
```

Registry updates must be projected before publication. The strict checker rejects stale registry/baseline/correction projections, any remigration-required marker, relationship-row drift, and every observation slot without exactly one current version; terminal superseded slots retain one current `superseded` observation.

```bash
# Controlled local migration; creates a verified backup and receipt.
# The base receipt comes from the last successful sync pull/bootstrap.
python pipeline/repair_bibliography_institutions.py \
  --db .cache/bibliography.sqlite3 \
  --base-receipt .cache/bibliography.base.json --execute
python pipeline/check_bibliography_db.py --strict

# Local rollback restores the verified pre-migration backup and deliberately
# leaves a remigration-required marker, which blocks push until migration reruns.
python pipeline/repair_bibliography_institutions.py \
  --db .cache/bibliography.sqlite3 --rollback

# Published rollback never rewinds the manifest. It republishes a retained
# immutable object as a newer CAS generation, binds the migration receipt,
# and forces a controlled remigration before the next push.
python pipeline/sync_bibliography_db.py \
  --rollback-generation <older-generation> \
  --migration-receipt .cache/bibliography.sqlite3.affiliation-migrate.json
```

The DB is stale when its paper count differs from `docs/papers/_papers_index.json`. After Zotero ingestion, forced rebuilds, or review corpus changes, run the builder with `--all` on the Mac mini worker before treating institution statistics as current. Institution spelling changes must be added to `institution_aliases`, not patched in individual queries.
## Recovery flows

```bash
# Audit PDF↔review mismatches
PYTHONUTF8=1 python pipeline/run_full.py --topic ai4s --mode audit

# Delete artifacts for high-confidence mismatches
PYTHONUTF8=1 python pipeline/run_full.py --topic ai4s --mode fix-matching --yes

# Re-review cleaned slugs
PYTHONUTF8=1 python pipeline/run_full.py --topic ai4s --mode rebuild --slugs <list> --strict-pdf

# Validate
PYTHONUTF8=1 python pipeline/run_full.py --topic ai4s --mode validate --yes  # --yes → --strict
```

## Topic configuration

Each topic ↔ Zotero collection is in `config.json`:

```json
{
  "zotero": {
    "collections": {
      "ai4s": "WKEZLEE8",
      "scisci": "3KVIDDKH",
      "humanoid": "...",
      "physical-ai": "..."
    }
  }
}
```

`docs/.assetsignore` controls which topics ship to Cloudflare.

## See also

- `CLAUDE.md` — codebase-wide Claude Code guidance
- `SKILL.md` — the user-facing skill dispatcher (this trigger entry)
- `pipeline/api/__init__.py` — programmatic API (25 functions)
- `pipeline/api/_llm.py` — caching helpers for LLM calls
- `pipeline/api/extract.py` — figure pre-validation heuristics
