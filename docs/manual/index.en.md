# Paper Curation · Paper Curio Manual

This English manual helps everyone from readers of a single paper to operators of a personal paper library choose only the work they need.

| Manual | For | Outcome |
|---|---|---|
| **[Beginner guide](beginner.en.md)** | Users installing for the first time or reviewing one Zotero paper | Connect the two programs → inspect the plan → create a review → open HTML |
| **[Advanced guide](advanced.en.md)** | Users operating CLI automation, multiple papers, search, bibliography databases, and deployment | Feature request JSON, credential and cost controls, search, full processing, and recovery |

## How the two programs relate

- **Paper Curation** is the Python runner that processes PDFs and creates reviews, search indexes, and web outputs. It also works from the command line.
- **Paper Curio** is a Zotero plugin. It provides the UI for selecting papers and requesting work; integrated features call Paper Curation.
- **Reading an existing review** and **creating a new AI result** are different. Opening existing HTML needs no generation API key.
- **GJC/Claude subscription authentication is not a Paper Curation API credential.** Cloud API work performed by the pipeline can be billed separately even when a subscription provides coding tools.

![Select a paper and PDF in Zotero, inspect the plan in Paper Curio, then approve it for Paper Curation to create a review. Indexing, timelines, and deployment are separate work.](images/quickstart.png)

Read the diagram as: **paper and PDF → Paper Curio → inspect plan → approve → Paper Curation → open review**. The dotted boxes are not automatic follow-up steps.

## Find your task

| Task | Read |
|---|---|
| Start from Zotero without much terminal experience | [Beginner guide](beginner.en.md) |
| Store API keys, cap costs, and distinguish subscriptions from APIs | [Advanced guide](advanced.en.md) |
| Run search, connection building, or the bibliography database separately | [Advanced guide](advanced.en.md) |
| Detailed installation requirements | [Setup guide](../setup-guide.md) |
| Full-pipeline operations and recovery | [Operations manual](../operations.md) |
| Data flow and web-deployment architecture | [Architecture](../architecture.md) |
| Institutional-attribution method | [Institutional attribution](../attribution.md) |

## Scope and diagrams

- Current as of the local implementation on **2026-09-13**. Check [`pipeline/features.json`](../../pipeline/features.json) for features and the [Paper Curio releases](https://github.com/jehyunlee/paper-curio/releases/latest) for the plugin build. Menus can differ by installed version.
- The diagrams are conceptual, not UI screenshots. They use English labels to avoid misreading small text. The advanced architecture diagram explains the shared feature execution path; the advanced guide separately describes the older AI Chat and full `run_full.py` paths.
- `quickstart.png` and `architecture.png` were generated with PaperBanana through `lib.paperbanana.generate_diagram()`. The generation configuration used text model `gemini-3.1-pro-preview`, image model `gemini-3.1-flash-image-preview`, 16:9 output, and at most two critic passes.
- Regeneration source: [`generate_figures.py`](generate_figures.py). Run it from the repository root with Python 3.12. It makes paid image-generation requests and preserves existing files by default.

```bash
python docs/manual/generate_figures.py --figure quickstart
# Add --force only when intentionally regenerating an existing image.
```

[한국어 매뉴얼](index.md) · [Paper Curation repository](https://github.com/jehyunlee/paper-curation) · [Paper Curio repository](https://github.com/jehyunlee/paper-curio)
