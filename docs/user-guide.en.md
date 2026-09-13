# Paper Curation User Guide

Start with the [Beginner Manual](manual/beginner.en.md) or use the
[Power-user Manual](manual/advanced.en.md) for automation and collection operations.

A step-by-step guide to **where each setting lives and how each task runs**.
Installation options are in the [Setup Guide](setup-guide.md), full-workflow
operations in the [Operations Manual](operations.md), and internals in
[Architecture](architecture.md).

🇰🇷 [한국어 버전](user-guide.md)

![Three usage paths](../usage_workflow.en.png)

## 0. Concepts to know first

| Concept | Meaning |
|---------|---------|
| **Three paths** | **Read** (browse and export, no key) · **AI** (review, summary, chat, comparison with one selected provider) · **Collection** (indexes, metrics, bibliography, audio, timelines, sync, publish, email — only when explicitly requested) |
| **Plan → confirm → execute** | Every task first produces a **plan** showing requirements, transmission destination and estimated cost. Only after you **confirm** does it **execute**. Planning writes no files and makes no API calls. |
| **Shared registry** | The Zotero plugin (Paper Curio) and the command line (`run_feature.py`) read the same capability list, `pipeline/features.json`. The generated table in the [Setup Guide](setup-guide.md#공유-기능-레지스트리) is the reference for IDs and requirements. |
| **Credentials** | API keys are resolved from **environment variables first, then the OS keyring** (macOS Keychain etc.). Settings files, request JSON and logs never hold plaintext keys. |
| **No silent fallback** | If the selected provider fails, nothing is re-sent to another company's model. Failures are reported as status codes. |
| **One capability = one task** | Requesting a review produces only a review. Classification, search indexes, timelines, email and publication each require their own request. |

## 1. Install and connect (once)

### 1-1. Install paper-curation — terminal

```bash
git clone https://github.com/jehyunlee/paper-curation.git && cd paper-curation
conda create -n py312 -c conda-forge python=3.12 pip -y && conda activate py312
pip install -r requirements.txt
PYTHONUTF8=1 python pipeline/setup.py
```

- Result: a minimal `config.json` and `docs/papers/`. No key prompts, no network calls, no pipeline run.
- Check: `python pipeline/run_feature.py --list` prints the capability registry as JSON.
- **Python must be exactly 3.12.** Local reviews and corpus locks currently require macOS/Linux (POSIX file locking); Windows is not yet supported for those.

### 1-2. Install the Zotero plugin — Zotero

1. Download `paper-curio.xpi` from the [latest Paper Curio release](https://github.com/jehyunlee/paper-curio/releases/latest).
2. Zotero → **Tools → Plugins → ⚙️ → Install Plugin From File…** → choose the file.
3. Later updates are picked up automatically by Zotero.

### 1-3. Connect the two — Zotero → Settings → Paper Curio → **Output Location**

| Field | Value |
|-------|-------|
| **paper-curation root** | Absolute path of the checkout from 1-1 (the folder containing `docs/papers/`). Leave empty to auto-detect `~/Documents/.../paper-curation` and similar. |
| **Python path** | Empty uses the default conda `py312`. Enter the interpreter path if you created it elsewhere. |
| **Fallback output dir** | Read-only browsing of an existing corpus on a machine without paper-curation. New reviews are not possible there. |
| **Overwrite existing reviews** | OFF by default; papers that already have a review are skipped. |

The status line at the top of the pane switches to "connected" once the link works.

### 1-4. Store API keys — Zotero → Settings → Paper Curio → **API keys**

1. Choose one **Review provider**: Anthropic · Sonnet 5 (default) / OpenAI · GPT-5 / Google · Gemini 3.1 Pro.
2. Paste the key into that provider's field and press **Save to OS keyring**.
   - The value goes into the OS keyring; Zotero settings keep only a `credential:<provider>` reference.
   - Saving an **empty value** with the same button deletes the stored key.
   - If the button reports that paper-curation and the Python keyring runtime must be connected first, finish 1-3.
3. Other chat providers (OpenAI/Gemini) and literature-database keys (Scopus etc.) live in the collapsed **Other chat providers and optional features** section and are saved the same way.

From the terminal (the key is never echoed):

```bash
python -c 'import getpass,sys; sys.stdout.write(getpass.getpass())' | \
  python pipeline/credentials.py --operation write --provider anthropic
python pipeline/credentials.py --operation status --provider anthropic     # never prints the value
PYTHONUTF8=1 python pipeline/setup.py --check-feature review                # readiness diagnosis
```

> Plaintext key preferences from v0.9.x are no longer read. Re-save each key with the procedure above after upgrading.
> Automation may inject environment variables (`ANTHROPIC_API_KEY` etc.); they take precedence over the OS keyring.

### 1-5. Cost ceiling (optional) — **Review cost ceiling** in the same **API keys** section

Enter a maximum USD amount together with the current provider's **input/output rates (USD per million tokens)**. Missing rates or a conservative estimate above the ceiling **block** execution (`budget-unavailable` / `budget-exceeded`). Leave it empty for no ceiling.

## 2. Path A — Read and export (no key)

| Goal | Where | How |
|------|-------|-----|
| Browse the public site | Browser | [Humanoid](https://paper-curation.jehyunlee.dev/humanoid/) · [Physical AI](https://paper-curation.jehyunlee.dev/physical-ai/) — cards, search, timelines, per-paper reviews |
| Open my review | Zotero context menu → **Open paper-curation Review HTML** | Opens the existing `docs/papers/{slug}/index.html` in the browser (no generation) |
| Browse the whole local site | Terminal | `PYTHONUTF8=1 python pipeline/serve_local.py` → `http://localhost:8000/` |
| Export the public institution table (`institution-export`) | Modules → **Read / export** → *Public institution table export* | Set `outdir` → Inspect plan → Execute. The export refuses private data, formulas and local paths |
| Extract a local PDF only (`extract`) | Modules → **Read / export** → *Local PDF extraction* | The selected item's PDF path is prefilled. Writes `text.md` and `figures/` into an empty `output_dir`. No API call |

## 3. Path B — Paper AI

### 3-1. Generate a review (from Zotero) — `review`

1. Select the **paper item** in the library (the parent item, not the PDF attachment row). A local PDF must be attached.
2. Right-click → **paper-curation Review generation**.
3. A **plan dialog** appears. Check:
   - provider and model (matching the Review provider in Settings)
   - **Output** — the reserved final directory `docs/papers/{number}_{title}/`
   - estimated cost and ceiling — only the title, abstract, figure captions and a text excerpt are sent to the selected provider
4. **OK** runs: PDF text/figure extraction → review → `review.md` + `index.html` + `bibliography.json`. Cancelling releases the reservation without any API call.
5. The completion toast "Review completed … **bibliography DB integration pending**" is normal: the review is done; global bibliography integration is the separate task in 4-2.
6. Open the result: right-click → **Open paper-curation Review HTML**.

Multiple selected items are processed in order, each with its own plan confirmation.

### 3-2. Generate a review (command line) — `review`

Save the [request example from the Setup Guide](setup-guide.md#단일-pdf-로컬-리뷰) as `review-request.json`, then:

```bash
python pipeline/local_review.py --request review-request.json            # plan only (no files, no API call)
python pipeline/local_review.py --request review-request.json --execute  # execute after review
```

`--request` takes a **JSON file path**. Exit code 0 means `ready`/`completed`/`exists`; 2 means a blocked status.

### 3-3. Summary, chat and comparison (module panel) — `summary` · `chat` · `comparison`

1. With the evidence papers selected (one or more; comparison needs two or more), use the last Paper Curio right-click entry → **(adv.) run Paper Curation modules** → **Paper AI** tab.
   (Right-click **paper-curation Comparison** opens the *Grounded comparison* card of the same panel directly.)
2. Press **Use selected PDF texts** to fill `sources` with the selected papers' text.
3. Choose a provider. Summary and chat also accept local **Ollama `qwen3.8:27b-mlx`** (free, on-device). Comparison and review support cloud providers only.
4. Fill `question` (required for chat) and, optionally, the cost ceiling and rates.
5. **Inspect plan** → read provider, destination and cost in the plan JSON → **Execute selected task** → OK in the confirmation dialog.
6. The result is a **list of claims with verbatim quotations**. Answers whose quotations cannot be found in the sources are rejected; weak evidence ends as `insufficient-data`.
7. Save with **Export result JSON** or **Export portable HTML report**. The HTML report contains no local paths or keys.

Editing any input invalidates the previous plan; press **Inspect plan** again.

### 3-4. AI Chat (talk to the PDF)

Right-click → **paper-curation AI Chat — single / multiple**. This existing feature works without the paper-curation link; choose the model at the top of the window and switch EN/KO answers. It uses the OS-keyring credentials from 1-4 or injected environment variables.

## 4. Path C — Collection and optional features

Run them from the **Collection** / **Optional features** tabs of **(adv.) run Paper Curation modules**, or from the command line with `run_feature.py`: write a request JSON file, pass it with `--request`, inspect the plan, then add `--execute`.

```bash
python pipeline/run_feature.py --list                                   # capabilities and requirements
python pipeline/run_feature.py --request feature-request.json           # plan
python pipeline/run_feature.py --request feature-request.json --execute # execute
```

Request format: `{"schema_version":1,"feature":"<capability id>","params":{...},"provider"?:..., "budget"?:...}`

### 4-1. Search indexes and queries

| ID | Needs | Notes |
|----|-------|-------|
| `keyword-search` | no key | `params.operation` `build` creates the BM25 index, `query` (default) searches it. Works without Google |
| `semantic-search` | Google key | Embedding-based index and query. Semantic queries against a BM25 index are refused explicitly instead of silently downgraded |

```json
{"schema_version":1,"feature":"keyword-search","params":{"topic":"my_topic","operation":"build"}}
```

### 4-2. Metrics, bibliography DB, institution table

| ID | Needs | Notes |
|----|-------|-------|
| `metrics` | no key (public APIs) | Accumulates citations/references into `citations.md` and `references.md` |
| `bibliography-update` | no key (offline by default) | Resolves "bibliography DB integration pending" after reviews. Ingests changed items into the local DB; never touches remote Zotero or email |
| `institution-export` | no key | Public institution normalization table (CSV and XLSX) |

### 4-3. Audio and timelines

| ID | Needs | Notes |
|----|-------|-------|
| `audio` | Google key, `ffmpeg` | MP3 from an existing review (or a validated saved script). Sends no email |
| `timeline-text` | Anthropic key | Category narratives (text) only |
| `timeline-image` | PaperBanana configuration and backend keys | Images from saved narratives only. An unready backend is blocked at planning time with `needs-runtime` |

### 4-4. Sync, publish, email (confirmation required)

| ID | Needs | Notes |
|----|-------|-------|
| `zotero-sync` | Zotero API key, collection mapping in `config.json` | `dry_run: true` by default. Applying deletions needs `dry_run:false` plus `confirm:true` |
| `publish` | Cloudflare token and account ID, Node.js, Git | `confirm:true` required. Uploads and repository changes happen; verify publication rights first |
| `email` | Resend key | Sends an **existing MP3** to the given recipient. Never generates audio |

### 4-5. Full collection processing (advanced)

- Right-click a Zotero collection → **Process this collection (review · classify · timelines)** — a new collection is asked for an alias, registered in `config.json`, then processed (deployment excluded).
- Terminal: always look at the plan first with `--dry-run`.

```bash
PYTHONUTF8=1 python pipeline/run_full.py --topic my_topic --mode curate --source zotero --dry-run
```

While a full run holds the corpus, reviews and module tasks on the same corpus wait with `busy`. Modes and recovery are in the [Operations Manual](operations.md).

## 5. Reading status and error messages

| Status | Meaning | Action |
|--------|---------|--------|
| `ready` | Plan complete, executable | Review it, then execute |
| `exists` | A completed review of the same paper already exists | Enable **Overwrite existing reviews** to replace it |
| `needs-key` | No credential for the selected provider | Store it in the OS keyring (1-4) |
| `needs-runtime` | Python 3.12, PyMuPDF, provider SDK, PaperBanana etc. not ready | Check 1-1 and 1-3; run `setup.py --check-feature <id>` |
| `insufficient-data` | PDF missing/unreadable/mismatched, or weak evidence | Check the attachment and the selected item |
| `budget-exceeded` / `budget-unavailable` | Ceiling exceeded / rates unknown | Adjust 1-5. No model was called |
| `blocked` | The task needs `confirm:true` | Add the confirmation if intended |
| `busy` | Another corpus task (full run, another review) is active | Retry after it finishes |
| `completed` | Success | — |
| **partial** ("index/marker update failed") | Review files are complete; only index registration or the Zotero marker failed | Open the shown HTML directly. Re-running the same item reuses the finished folder and retries registration only (no paid call) |

Plugin error messages include a `[code]` such as `[corpus-busy]`. The wording is a fixed safe message; raw third-party errors are not shown because they can contain credentials.

## 6. FAQ

- **What leaves my machine?** Review: title, abstract, figure captions and a text excerpt (up to 12,000 characters) to **the selected provider only**. Summary/chat/comparison: the selected PDF text. Reading, keyword search, extraction and offline bibliography updates transmit nothing.
- **Is another provider tried automatically?** No. Failures are reported as status; retries are explicit.
- **Where could a key remain in plaintext?** Nowhere. Settings hold only `credential:<provider>` references; values live in the OS keyring. `credentials.py --operation read` is a private plugin pipe — do not run it in a terminal.
- **Reviews fail on Windows.** Local reviews and corpus locks need POSIX file locking. Reading and AI Chat work.
- **Cost?** Roughly $0.05–0.15 per review depending on model and length. Set the ceiling in 1-5 for a hard bound. Summary and chat can run free on Ollama.
- **Is the full pipeline (`run_full`) gone?** No. It remains the advanced task in 4-5; what changed is that a single review no longer drags the whole pipeline along.
