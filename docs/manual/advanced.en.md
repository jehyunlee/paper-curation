# Advanced operations manual: Paper Curation and Paper Curio

This document gives safe operating procedures and recovery criteria for users running both products. Start with the [beginner guide](beginner.en.md) or the [manual index](index.en.md) when new to them.

- **Paper Curation:** the Python pipeline in the local `paper-curation` repository and its `docs/` corpus.
- **Paper Curio:** a Zotero 9 plugin. Light mode provides PDF chat; Enhanced mode calls Curation's shared runner.
- The actual runtime contract in `pipeline/features.json`, `pipeline/run_feature.py`, and each module source takes precedence over this guide.
- See the [operations manual](../operations.md) for full operations, the [setup guide](../setup-guide.md) for installation, and [architecture](../architecture.md) for structure.

![Paper Curation architecture: Zotero/Paper Curio and the CLI connect through the shared feature registry and local corpus to selected external providers and optional deployment targets.](images/architecture.png)

Text equivalent: a user supplies request JSON through the Curio menu or `run_feature.py`. Both paths validate feature, permission, and runtime with `features.json`, then run only the selected module under the corpus lock. Reviews and text tasks may send content only to the selected AI provider; search, bibliography, audio, timeline, synchronization, deployment, and email are independently requested. Results and caches remain in local `docs/`, `docs/papers/`, and `.cache/`.

## 1. Operating principles and boundaries

### 1.1 What one request runs

The shared feature runner plans and executes **one feature only**. A successful review does not implicitly start classification, connections, a global index, timelines, audio, email, or deployment.

| Path | Purpose | Does not automatically do |
|---|---|---|
| Curio Light | Attachment-PDF AI Chat and Comparative Chat | Install Curation, create review files, change a collection |
| Curio Enhanced minimal review | One PDF's `text.md`, `figures/`, `review.md`, `index.html`, `bibliography.json` | Originality, connections, classification, global database/index |
| `run_feature.py` | Plan or execute a selected feature | Chain other features or change providers |
| `run_full.py` | The older full orchestrator | Replace the shared-feature plan/execute contract |

`run_full.py` is for legacy full workflows. With `--source web` it automatically selects search, registration, and synchronization; with `--source zotero` it automatically selects synchronization. Those are not shared-feature rules: do not expect “full processing after review” from an individual feature request.

### 1.2 Plan, then execute

`run_feature.py --request REQUEST.json` is a read-only plan: it makes no API call or file change. Review `transmission`, `cost`, `outputs`, `authorization`, and `steps`, then append `--execute` to the same request only when correct.

```bash
python pipeline/run_feature.py --request /absolute/path/request.json
python pipeline/run_feature.py --request /absolute/path/request.json --execute
```

`REQUEST.json` is a file at a user-created absolute path. Put no secret in it; `credential_ref` is only a reference such as `credential:anthropic`. Fields outside the request schema are rejected.

### 1.3 Do not mistake status for success

| Status | Meaning and response |
|---|---|
| `ready` | Planning succeeded; nothing has run. |
| `completed` | The selected feature completed; inspect returned `outputs`. |
| `exists` | Existing output was reused; check overwrite policy. |
| `needs-key` | The selected provider credential is absent; configure an environment variable or OS keyring. |
| `needs-runtime` | A required runtime such as Python 3.12, a library, or `ffmpeg` is absent. |
| `insufficient-data` | Prerequisite material such as a PDF, index, classification, or input text is absent. |
| `budget-unavailable` | A cap cannot be calculated from verified pricing. Do not guess pricing. |
| `blocked` | A confirmation field or safety condition is missing; amend and plan again. |
| `busy` | Another Curio/CLI operation owns a corpus reservation or lock; do not duplicate it. Retry after it finishes. |
| `failed` | The request, runtime, or selected provider failed. Preserve the error and partial information, then fix the cause. |

When a review error includes `partial`, some stage outputs may exist. Do not deploy or manually register them as complete. Inspect the output directory and error, then recover with the same input. A normal review validates required outputs in staging before atomically publishing them.

## 2. Runtime, paths, and secrets

### 2.1 Curation runtime

Shared features require **exactly Python 3.12**.

```bash
python --version
python pipeline/run_feature.py --list
```

Confirm that the first command prints `Python 3.12.x`. When another `python` is default, invoke the required interpreter by absolute path. Follow the [setup guide](../setup-guide.md) for project and dependency installation.

### 2.2 How Curio locates Curation

In Zotero → Settings → Paper Curio → **Output location**, configure the Curation root and, when needed, Python path. Curio looks for the root in this order:

1. Root path in Paper Curio preferences
2. `PAPER_CURATION_DIR` or `PAPER_CURATION_ROOT`
3. Automatic discovery of known `paper-curation` candidates
4. Existing material in the fallback output path

A valid root contains `<root>/docs/papers/`. Fallback is read-only and cannot create a review. A minimal review does not create a managed environment when the configured Python is absent; managed venv/relocatable-Python preparation is supported only by Curio's collection-wide processing path.

### 2.3 API-key precedence and separation

Credentials use **environment variables first, then the OS keyring**. Curation never uses plaintext config, request JSON, or logs as a credential store. Keyring references use `credential:<provider>`.

| Purpose | Environment-variable example | Keyring reference |
|---|---|---|
| Anthropic | `ANTHROPIC_API_KEY` | `credential:anthropic` |
| OpenAI | `OPENAI_API_KEY` | `credential:openai` |
| Google/Gemini | `GOOGLE_API_KEY` or `GEMINI_API_KEY` | `credential:google` |
| Zotero remote sync | `ZOTERO_API_KEY` | `credential:zotero` |
| Resend mail | `RESEND_API_KEY` | `credential:resend` |

A macOS GUI Zotero process might not inherit login-shell environment variables. Saving the selected provider key through Curio's API-key screen to the OS keyring is more reliable. Environment variables suit temporary CI/automation injection.

**GJC OAuth and pipeline API keys are separate.** Do not use a GJC login/OAuth token in place of an Anthropic, OpenAI, Google, Zotero, or Resend key, and never copy GJC OAuth values into a pipeline request or Curio setting. Pipeline API billing remains separate from a GJC subscription.

Store a terminal-entered key without displaying it:

```bash
python -c 'import getpass,sys; sys.stdout.write(getpass.getpass())' | \
  python pipeline/credentials.py --operation write --provider anthropic
python pipeline/credentials.py --operation status --provider anthropic
```

`--operation read` is for plugin-internal IPC and must not be run in a terminal.

Shared review, summary, question-answering, and comparison do not fall back to another provider when the selected provider fails. This no-fallback guarantee applies to the shared feature provider; it does not forbid the independent cross-category-insights fallback described by that feature's own runtime.

## 3. Safe request-JSON recipes

The templates below contain no secrets. Replace `__...__` with real absolute paths, bibliographic data, and source text; keep keys in the environment or OS keyring.

### 3.1 One-PDF review

`review` puts a local-review request in the shared wrapper's `params.request`. PDF and output paths must be absolute, and `output_dir` must be the paper-slug directory.

```json
{
  "schema_version": 1,
  "feature": "review",
  "provider": "anthropic",
  "credential_ref": "credential:anthropic",
  "budget": {"max_cost_usd": 1.00, "max_output_tokens": 2000},
  "params": {"request": {
    "schema_version": 1, "feature": "review",
    "pdf_path": "__ABSOLUTE_PDF_PATH__",
    "output_dir": "__ABSOLUTE_CURATION_ROOT__/docs/papers/__SLUG__",
    "overwrite": false,
    "item": {
      "key": "__ZOTERO_KEY__", "title": "__TITLE__",
      "creators": [{"firstName": "__GIVEN__", "lastName": "__FAMILY__", "creatorType": "author"}],
      "date": "__DATE_OR_EMPTY_STRING__", "DOI": "__DOI_OR_EMPTY_STRING__",
      "abstractNote": "__ABSTRACT_OR_EMPTY_STRING__", "url": "__URL_OR_EMPTY_STRING__",
      "publicationTitle": "__VENUE_OR_EMPTY_STRING__"
    }
  }}
}
```

This intentionally omits prices, so it is blocked until you verify the selected provider/model's official prices and add numeric `input_per_million_usd` and `output_per_million_usd` to `budget`. Do not bypass blocking with zero or invented prices. Defer execution when pricing is unknown. Review output tokens must be 1–4000.

```bash
python pipeline/run_feature.py --request /absolute/path/review.request.json
python pipeline/run_feature.py --request /absolute/path/review.request.json --execute
```

The default `overwrite: false` preserves existing reviews. Change it to `true` only after confirming the rebuild and backing up needed results. A Curio minimal review uses the same scope and output contract.

| Review provider | Default model | Selection |
|---|---|---|
| `anthropic` | `claude-sonnet-5` | Default |
| `openai` | `gpt-5` | Explicit |
| `google` | `gemini-3.1-pro-preview` | Explicit |

When changing provider, change the top-level `credential_ref` to that provider too. Direct `local_review.py` uses a flat request with `provider`, `credential_ref`, and `budget` inside the local request, not the `params.request` wrapper. Do not mix the two CLI shapes.

### 3.2 Evidence-grounded summaries and chat

`summary` summarizes when its question is omitted; `chat` requires `question`. Both support Anthropic, OpenAI, Google, or loopback Ollama. `comparison` needs at least two sources and does not support Ollama. Source text is in the request file, so never commit sensitive text to a shared repository.

```json
{
  "schema_version": 1,
  "feature": "chat",
  "provider": "ollama",
  "params": {
    "sources": [{"id": "paper-a", "title": "__TITLE__", "text": "__LOCAL_EXCERPT__"}],
    "question": "Explain the claims and limitations in this text with supporting quotations.",
    "max_input_chars": 30000,
    "max_output_tokens": 1000
  }
}
```

Loopback Ollama needs no cloud API key. For a cloud provider, add top-level `credential_ref` and, when required, `budget`. `max_input_chars` ranges from 1 to 1,000,000 and `max_output_tokens` from 1 to 32,000. A text task does not report success when the model cannot provide source-grounded citations.

Save it as `chat.request.json`, then plan and execute. For a summary, change `feature` to `summary` and adjust the question to a summary request. Ollama and local model `qwen3.8:27b-mlx` must be ready.

```bash
python pipeline/run_feature.py --request chat.request.json
python pipeline/run_feature.py --request chat.request.json --execute
```

### 3.3 Common feature-request shape

```bash
python pipeline/run_feature.py --list
```

The common top-level fields are `schema_version`, `feature`, `params`, plus optional `provider`, `credential_ref`, and `budget`. `topic` and `slug` must each be one path component within the Curation root; arbitrary paths and parent-directory strings are rejected.

## 4. Search and bibliography: keep features separate

### 4.1 BM25 keyword index and semantic search

`keyword-search` is local BM25: build and query need no cost review or credential. `semantic-search` builds a hybrid index and uses the Google embedding API, so it needs a Google key and cost review.

```json
{"schema_version":1,"feature":"keyword-search","params":{"topic":"__TOPIC__","operation":"build","include_text":"auto"}}
```

```json
{"schema_version":1,"feature":"keyword-search","params":{"topic":"__TOPIC__","operation":"query","query":"__KEYWORDS__","top_k":10,"include_text":"auto"}}
```

Save each JSON in its own file, plan it, then build or query. Query needs a built index. A semantic query cannot run on a BM25-only index; explicitly rebuild hybrid. Public topics cannot index full text with `include_text: "yes"`.

### 4.2 Bibliography database and attribution

`bibliography-update` updates `.cache/bibliography.sqlite3` from papers in the chosen topic. The default `offline: true` uses only local sidecars and PDF evidence, avoiding network transmission and cost.

```json
{"schema_version":1,"feature":"bibliography-update","params":{"topic":"__TOPIC__","offline":true}}
```

Online mode can use configured bibliography sources, but pricing may not permit a verified budget cap. This feature does not page Zotero Web. A Curio minimal review's `bibliography.json` is sidecar-only; “bibliography database update pending” means a separate update has not run, not that review failed.

`metrics` independently updates citation/reference outputs. Remote Zotero sync is another `zotero-sync` feature. Keep its default dry run; applying remote deletion requires both `dry_run:false` and `confirm:true`.

## 5. Connections, full collections, and recovery

### 5.1 Current connections implementation

Connections are built deterministically from `pipeline/lib/related.py` and `pipeline/topic_modeling.py`. Candidate ranking fuses SPECTER2 cosine similarity with title/author BM25 using reciprocal-rank fusion (RRF, `k=60`). The metadata builder then uses that ranking and recorded metadata only to choose up to the link limit, assign `foundation`, `extension`, or `alternative`, and write Korean rationale text. This path uses no provider SDK, LLM judge, local fallback, or network fallback. A Curio minimal review does not create connections.

The full workflow uses this same deterministic metadata builder for its connections stage. Cross-category insights are a separate feature and may use its explicitly configured fallback; that is not a provider fallback for shared review/text features and does not alter connection construction.

Relation labels are metadata heuristics, not verified citations, causality, or proof of a scientific extension. Shared surname keys and publication years can be incomplete or ambiguous. Inspect the stored `evidence` and the papers themselves.

### 5.2 Curio collection-wide processing

Right-click a Zotero collection and choose **Process this entire collection**. For a new collection, enter an alias and register it in `config.json`; the path then runs Zotero sync → review → classify → narrative/timeline → topic index. Cloudflare deployment is not included. It changes the full corpus, so keep it separate from a one-paper review.

Citedby is a separate Enhanced menu. From a selected paper DOI, it queries OpenAlex, Scopus, Semantic Scholar, and arXiv; it produces a self-contained HTML report after originality extraction and optional LLM filtering/5W1H. PDF output and batch Zotero registration are supported. Batch registration checks DOI/arXiv/title duplicates. Run full curation separately after registration when needed.

### 5.3 Legacy full workflow: explicit dry run

The full orchestrator does not use request JSON and differs from the shared feature runner. Print a plan first.

```bash
PYTHONUTF8=1 python pipeline/run_full.py --topic __TOPIC__ --mode curate --source zotero --dry-run
```

Only remove `--dry-run` after checking the plan, corpus backup, and lock state. `--source web` includes web search, registration, and sync. Prefer the narrowest recovery over full regeneration.

```bash
PYTHONUTF8=1 python pipeline/run_full.py --topic __TOPIC__ --mode rebuild --slugs __SLUGS__ --strict-pdf --dry-run
```

`__SLUGS__` is a comma-separated list of existing slugs. `rebuild` can require destructive confirmation; do not routinely add `--yes`. `recover` is dry-run without `--yes`. On failure, preserve the failed stage, partial results, input PDF, and reservation state; do not delete output directories or lock files manually. Reproduce with the narrowest dry run.

## 6. Optional features are independent

### 6.1 Audio, timelines, and email

- `audio` needs an existing review or verified `audio_script.txt`, Google, and `ffmpeg`; it produces MP3 and script.
- `timeline-text` needs a classified topic and Anthropic narrative runtime.
- `timeline-image` needs a saved narrative and configured PaperBanana backend. PaperBanana is not installed by default; check `paperbanana_dir`/`scisci_lib` and backend-model configuration in `config.json`.
- `email` sends only an existing MP3 of at most 20 MiB with Resend. Sender-domain and recipient authorization are known only from the actual sending response.

A timeline image is separate from timeline text. Do not run an image task when backend status is `needs-configuration`, `unverified-backend`, or `needs-credential`. Email neither generates audio nor deploys content.

### 6.2 Local hosting and public deployment

Opening generated `index.html` locally is not public deployment. Curio's **Open Review HTML** only opens existing output; it neither creates nor deploys it. `publish` needs Cloudflare/GitHub credentials, Node.js, Git, topic HTML, and `confirm:true`; it can create artifacts and repository updates.

```bash
python pipeline/serve_local.py --port 8000
```

Open generated output at `http://localhost:8000/`. Distinguish a paid API proxy from ordinary local HTML viewing, and do not casually expose the local server through a public tunnel.

Before publishing, separately check rights for PDF copyright, source quotation, personal data, institutional-data redistribution, and sender-domain authorization. Never publish request JSON, `.cache`, or config containing tokens, API keys, OAuth values, or internal source text. Review environment and authorization in the plan/feature UI before explicitly running deployment; this manual intentionally provides no copy-and-run publish command.

## 7. Curio UI and data layout

### 7.1 UI behavior

From a selected item, right-click → **(adv.) run Paper Curation modules**, then fill a card's inputs. For summary, question answering, and comparison, prepare evidence with **Use selected PDF text**, then use **Review execution plan** → **Run selected task** → confirmation. Editing input invalidates the plan, so inspect it again. Use **Export result JSON** or **Export shareable HTML report** to retain results.

Light mode needs only Zotero and a selected LLM key for PDF AI Chat and Comparative Chat; it locally caches PDF text for fast reopening. Enhanced mode preferentially reads existing `docs/papers/<slug>/text.md` and `figures/`, and adds in-answer figures, Obsidian export, shared review/summary/question-answering/comparison, Citedby, and collection-wide processing.

Curio's **Overwrite existing review** is off by default, so existing reviews are skipped. Reviews created directly by Curio can be regenerated; separately preserve any edits to their output files. Its progress window and `busy` state honor shared corpus reservation, registration, cancellation, and locking.

### 7.2 What remains where

| Location | Contents | Operational note |
|---|---|---|
| `docs/papers/<slug>/` | Single-paper text, figures, review, HTML, bibliography sidecar | Canonical minimal-review output |
| `docs/<topic>/` | Topic HTML, search index, narrative/timeline outputs | Full or selected-collection output |
| `docs/papers/_papers_index.json` | Corpus paper index | Do not edit concurrently by hand |
| `.cache/bibliography.sqlite3` | Bibliography database | Rebuildable local data, not a secret store |
| OS keyring | Provider secret | Keep only `credential:*` references in settings |

Caches aid reuse, not freshness. A feature can return `exists` or read prior output. When input PDF, metadata, provider, or output policy differs, inspect the plan and explicitly regenerate only the needed scope. Do not use Curio and CLI simultaneously on the same corpus.

## 8. Cost, diagnosis, and avoiding repeated calls

### 8.1 Meaning of a cost cap

A cap is not a provider invoice. Review and text tasks calculate a pre-execution upper bound from input/output token limits and current per-million-token prices supplied by the user. Missing prices, unclear provider pricing, or a breached cap must block execution. Check the provider billing page for actual cost.

BM25 search and offline bibliography updates are local. Semantic embeddings, cloud review/summary/chat/comparison, Google audio, and Anthropic timelines can incur charges. Metrics, online bibliography, PaperBanana, Zotero, Cloudflare, and Resend can lack pricing that permits a verified estimate. Do not bypass `budget-unavailable` with invented prices.

### 8.2 Order for avoiding repeated cost

1. Inspect `--list` and the request plan for feature, transmission, runtime, and outputs.
2. Check existing `text.md`, review, index, sidecar, and cache.
3. Start with one paper, small `top_k`, and low output tokens.
4. Resolve `exists`, `busy`, `partial`, and `needs-*` before repeating a paid request.
5. Use full review rebuilds only when the inputs actually require them. Connections are recomputed locally; they have no LLM-cache reset flag or judge retry mode.
6. Retain provider/model/transmission/estimate from errors and local logs, but never secrets.

### 8.3 Quick diagnostic table

| Symptom | Check in order |
|---|---|
| Curio cannot create a review | Output-location root, `docs/papers/`, Python 3.12, selected-provider key, PDF attachment |
| Curio can chat but Enhanced menu fails | Light mode can be normal; check Curation root, requirements, and Python bridge |
| Shell works but Zotero reports `needs-key` | GUI may not inherit environment variables; check the OS keyring for the same provider |
| Semantic query fails | Google key, completed hybrid build, and whether the index is BM25-only |
| Timeline image fails | Saved narrative and PaperBanana preflight/backend credential |
| Bibliography update pending | Inspect review output, then separately plan/execute `bibliography-update` |
| `busy` | Wait for another Curio/CLI job; do not retry the same request in parallel |
| Full run fails | Start by reproducing input matching with `--dry-run`, narrow `--slugs`, and `--strict-pdf` |

## 9. Verifiable sources and current implementation

This guide is grounded in:

- `pipeline/features.json`: shared feature IDs, parameters, runtimes, providers, transmission, and cost classes
- `pipeline/run_feature.py`: planning/execution, budget checks, locks, build/query, deployment and synchronization conditions
- `pipeline/local_review.py`: minimal-review request, outputs, atomic publication, and `partial` status
- `pipeline/lib/credentials.py`: environment-variable then native OS-keyring lookup, with no file fallback
- `pipeline/lib/related.py`, `pipeline/topic_modeling.py`: SPECTER2 cosine + title/author BM25 RRF candidates and deterministic connections metadata builder
- `pipeline/extract_insights.py`, `pipeline/run_full.py`: full orchestration and separate cross-category-insights behavior
- [User guide](../user-guide.en.md), [operations manual](../operations.md), and [setup guide](../setup-guide.md)
- Paper Curio `README.md`: Light/Enhanced modes, UI, Citedby, collection-wide processing, and root discovery

Reviews default to Anthropic `claude-sonnet-5`; request validation permits explicit OpenAI or Google selection. `features.json` registers only those three providers for review, and shared-feature providers do not automatically fall back.

For connections, Step 6 of `topic_modeling.py` fuses SPECTER2 cosine and title/author BM25 rankings with RRF (`k=60`). The deterministic builder in `lib/related.py` uses persisted metadata to create relation labels and Korean rationale. It does not call an LLM judge and has no local or network fallback. Cross-category insights remain a distinct runtime with its own explicitly configured fallback policy.

[한국어 고급 안내](advanced.md) · [Manual index](index.en.md)
