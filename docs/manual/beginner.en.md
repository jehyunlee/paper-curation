# Beginner guide: Paper Curation and Paper Curio

This guide is for a first experience that **safely reads one paper, inspects the plan, and opens an HTML review**. Process one paper first. Collection-wide processing, deployment, and timelines are covered in the [advanced guide](advanced.en.md).

![First-use flow for Paper Curation and Paper Curio: install, connect, select a paper, inspect the plan, and open the review HTML.](images/quickstart.png)

This is a conceptual diagram, not a screen capture. In text, the sequence is:

> Install Paper Curation → install Paper Curio → configure paths and credentials → select the parent paper item with a local PDF → inspect the plan → run the review → open the HTML

## The two tools and three kinds of work

| Tool | What it does | First use |
|---|---|---|
| **Paper Curation** | Python engine, web documents, and CLI. Creates reviews and HTML from PDFs and can optionally run search, bibliography, audio, and other work. | Inspect a plan at the command line after installation, or use it as Curio's shared engine. |
| **Paper Curio** | Zotero 9 plugin. Opens chat, review, and shared-feature modules from Zotero paper items. | Chat with a PDF in Zotero or request a review. |

- **Reading and exporting** do not need a key: opening existing review HTML, viewing public sites, extracting a local PDF, and keyword search are examples.
- **AI work** (review, summary, question answering, comparison) uses only the selected provider; a failure does not automatically send content to another company's model.
- **Collection work** (indexing, bibliography, timelines, deployment, and email) is separate. A one-paper review does not start the full pipeline.

## 1. Install Paper Curation

macOS and Linux require **exactly Python 3.12**. Other versions, including 3.14, are rejected for local review. Windows does not support local review or corpus locking, but can read existing results and use AI Chat.

Git and conda must be installed. Install Miniconda first when the `conda` command is unavailable. Dependency-download time varies by environment.

```bash
git clone https://github.com/jehyunlee/paper-curation.git
cd paper-curation
conda create -n py312 -c conda-forge python=3.12 pip -y
conda activate py312
pip install -r requirements.txt
PYTHONUTF8=1 python pipeline/setup.py
python pipeline/run_feature.py --list
```

The basic installation is complete when the final command prints the feature-list JSON. `setup.py` neither asks for credentials nor performs network calls or runs the full pipeline. For installation problems and other operating systems, use the [setup guide](../setup-guide.md).

## 2. Install and connect Paper Curio

1. Download `paper-curio.xpi` from the [latest Paper Curio release](https://github.com/jehyunlee/paper-curio/releases/latest).
2. In Zotero 9, open **Tools → Plugins → ⚙️ → Install Plugin From File…** and select the XPI.
3. Open Zotero → **Settings → Paper Curio → Output location** and set:

| Field | Value |
|---|---|
| **paper-curation root path** | The absolute path to the folder just cloned. It must contain `docs/papers/`. |
| **Python path** | Leave blank to use the default conda `py312`; otherwise enter the Python 3.12 interpreter path for the chosen environment. |
| **Fallback output path** | A location for opening existing reviews on a computer without paper-curation. It cannot create a new review. |

When the settings window reports “Connected,” Enhanced mode is ready. Without an integration, Light mode can still use AI Chat and Comparative Chat, but needs an API key.

## 3. Configure credentials and costs safely

Existing HTML needs no key, but creating new cloud reviews or chat results does. In Zotero → **Settings → Paper Curio → API keys**, choose one **review provider**, enter its key, and select **Save to OS keyring**.

- Settings retain only a `credential:<provider>` reference; the value stays in the OS keyring. Saving an empty value deletes the key.
- Never put keys in `config.json`, request JSON, command-line arguments, or notes. In automation, environment variables take precedence over the OS keyring.
- Claude/GJC OAuth subscription login is not an API credential for this pipeline. Use the chosen provider's API key or a correctly injected environment variable.
- A **review cost cap** is optional. When setting one, also enter the current provider's input and output USD prices per million tokens. Execution is blocked when prices are unknown; do not guess them.

Pipeline API charges are separate from a GJC subscription.

## 4. Create your first Zotero review

1. In Zotero, select one **parent paper item, not its PDF attachment row**. It must have an accessible local PDF attachment.
2. Right-click and choose **Create paper-curation Review**.
3. In the plan window, read the provider and model, the output path under `docs/papers/{number}_{title}/`, and the estimated cost and cap.
4. Select OK only when it is correct, to run this review only. Canceling releases the reservation without an API call. Because a reservation exists, do not assume planning can never create a file.
5. When complete, right-click and choose **Open paper-curation Review HTML**.

On success, the output folder contains `review.md`, `index.html`, and `bibliography.json`; HTML opens in the browser. “Review complete … bibliography database update pending” does not mean the review failed: updating the global bibliography database is separate.

Completed reviews are skipped by default. To rebuild one, enable **Overwrite existing review**. Reviews created directly by Paper Curio may be regenerated regardless of that setting.

## 5. Process one paper from the command line without Zotero

Save the following as `request.json`. Replace paths and bibliographic fields with real values, then inspect the plan first. Do not put the credential itself in the file.

```json
{
  "schema_version": 1,
  "feature": "review",
  "pdf_path": "/absolute/path/to/paper.pdf",
  "output_dir": "/absolute/path/to/output/paper-slug",
  "item": {
    "key": "LOCAL_ITEM_KEY", "title": "Paper title",
    "creators": [{"firstName": "Ada", "lastName": "Lovelace", "creatorType": "author"}],
    "date": "2026", "DOI": "10.0000/example", "abstractNote": "Abstract text",
    "url": "https://example.org/paper", "publicationTitle": "Journal name"
  },
  "overwrite": false,
  "provider": "anthropic",
  "credential_ref": "credential:anthropic"
}
```

```bash
python pipeline/local_review.py --request request.json
python pipeline/local_review.py --request request.json --execute
```

Run the second command only after the first reports `ready`. `completed` means complete; `exists` means an identical completed review already exists. `needs-key`, `needs-runtime`, and `insufficient-data` can be corrected before execution. See the [single-PDF local-review example in the setup guide](../setup-guide.md) for provider, budget, and output contracts.

## What to do next

- **Local chat and summaries:** In **(adv.) run Paper Curation modules → Paper AI**, prepare selected PDF text, then run summaries or questions using installed and running Ollama `qwen3.8:27b-mlx`. It has no cloud API charge but uses local compute. This is distinct from the existing **AI Chat — single** menu; reviews and comparisons use cloud-provider features.
- **Evidence-grounded summary, question answering, and comparison:** Open a card in **(adv.) run Paper Curation modules**, inspect **Review execution plan**, then choose **Run selected task**. Changing input requires a new plan.
- For search indexes, bibliography updates, collection-wide processing, deployment, and email, inspect plans, confirmations, and permissions in the [advanced guide](advanced.en.md).

## Short troubleshooting

| Status or symptom | Check |
|---|---|
| `needs-key` | Confirm that the chosen provider's key was saved to the OS keyring under **API keys**. |
| `needs-runtime` | Check the Output location root, Python 3.12, and installed dependencies. |
| `insufficient-data` | Confirm that the parent paper item is selected and has an accessible local PDF. |
| `busy` or a reservation message | Wait for the other corpus operation or reservation to finish, then retry. |
| HTML opens but the list is not updated | The status may be `partial`. The review file is retained; open its HTML and rerun the same item to retry registration. |
| Local review fails on Windows | Run it in a macOS/Linux Python 3.12 environment. Windows supports reading and AI Chat. |

Start with the [manual index](index.en.md). Read [한국어 초보자 안내](beginner.md), the [setup guide](../setup-guide.md), or the [advanced guide](advanced.en.md) for further detail.
