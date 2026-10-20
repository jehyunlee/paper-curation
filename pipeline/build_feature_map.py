#!/usr/bin/env python3
"""Build Korean and English interactive Paper Curation feature maps.

Sources (single source each, so the map cannot drift from the code):
  * ``pipeline/features.json``     — on-demand registry features
  * ``pipeline/pipeline_map.json`` — full-curation stages and steps, checked
                                     against run_update_force by
                                     tests/test_pipeline_map.py
Entry points, the shared runner and in-browser features are described here.
Each output is self-contained (no CDN, no network).

Usage:
  PYTHONUTF8=1 python pipeline/build_feature_map.py
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "pipeline" / "features.json"
PIPELINE_MAP = ROOT / "pipeline" / "pipeline_map.json"
OUTPUT = ROOT / "docs" / "feature-map.html"
OUTPUT_EN = ROOT / "docs" / "feature-map.en.html"

PATHS = {
    "reading": ("read", "Read · 읽기·내보내기", "API 키 없이 생성된 결과를 읽고 내보냅니다."),
    "ai": ("ai", "AI · 논문 AI", "선택한 제공자 하나로 논문 한 편 또는 여러 편을 다룹니다."),
    "collection": ("collection", "Collection · 컬렉션 관리", "컬렉션 전체의 색인·지표·동기화. 명시적으로 요청할 때만 실행합니다."),
    "optional": ("optional", "Optional · 선택 기능", "비용이나 외부 전송이 따르는 기능. 각각 따로 계획하고 확인합니다."),
}

PATHS_EN = {
    "reading": ("read", "Read · browse and export", "Browse and export generated results without an API key."),
    "ai": ("ai", "AI · paper AI", "Process one or more papers with one selected provider."),
    "collection": ("collection", "Collection · collection management", "Index, measure, and synchronize a collection. Runs only when explicitly requested."),
    "optional": ("optional", "Optional features", "Features involving cost or external transmission. Plan and confirm each separately."),
}

DETAILS_EN = {
    "review": "Extract text and figures from a PDF, then have the selected provider write a six-section Korean review (Essence, Motivation, Achievement, How, Originality, Evaluation).",
    "summary": "Create a summary with verbatim quotations using only the selected PDF text. Claims without a located quotation are rejected.",
    "chat": "Question and answer grounded in the PDF text, with source quotations in every answer.",
    "comparison": "Compare papers on the same criteria and attach source quotations to every claim.",
    "extract": "Extract text and figures from a local PDF: OpenDataLoader for text (PyMuPDF with a warning when unavailable) and PyMuPDF geometric crops for figures.",
    "keyword-search": "Build and query a BM25 keyword index. No API key is required.",
    "semantic-search": "Build and query a hybrid index that combines Gemini embeddings and BM25 with RRF.",
    "metrics": "Accumulate citation history and references from Crossref, OpenAlex, and Scopus (30-day incremental by default).",
    "bibliography-update": "Apply papers, authors, and institution affiliations to the SQLite bibliography database. Offline is the default.",
    "institution-export": "Export a publishable institution table.",
    "audio": "Create a podcast-style MP3 from an existing review (Gemini script plus TTS). It does not send email.",
    "timeline-text": "Write a research-trend narrative for each category.",
    "timeline-image": "Create category and main timeline images with PaperBanana.",
    "zotero-sync": "Synchronize with Zotero's remote state. The default is report-only (dry-run); applying it can remove local entries.",
    "publish": "Deploy through Cloudflare Workers and gh-pages redirect stubs.",
    "email": "Send an existing MP3 through Resend.",
}

OUTPUTS_EN = {
    "review": "review.md · index.html · bibliography.json",
    "summary": "Summary with quotations", "chat": "Answer with quotations", "comparison": "Comparison table with quotations",
    "extract": "text.md · figures/", "keyword-search": "_search_index.json (BM25)",
    "semantic-search": "_search_index.json + embeddings", "metrics": "citations.md · references.md",
    "bibliography-update": ".cache/bibliography.sqlite3", "institution-export": "Publishable institution table (xlsx)",
    "audio": "MP3", "timeline-text": "Timeline narrative", "timeline-image": "Timeline images (PNG)",
    "zotero-sync": "Synchronization report", "publish": "Deployed site", "email": "Send result",
}

DETAILS = {
    "review": "PDF에서 텍스트·그림을 추출하고 선택한 제공자가 6개 섹션 한국어 리뷰(Essence·Motivation·Achievement·How·Originality·Evaluation)를 씁니다.",
    "summary": "선택한 PDF 본문만 근거로 원문 인용이 붙은 요약을 만듭니다. 인용을 찾지 못한 주장은 거부합니다.",
    "chat": "PDF 본문에 근거한 질의응답. 답마다 원문 인용을 붙입니다.",
    "comparison": "여러 논문을 같은 기준으로 비교하고 각 주장에 원문 인용을 붙입니다.",
    "extract": "로컬 PDF에서 본문과 그림을 추출합니다. 본문은 OpenDataLoader(없으면 경고 후 PyMuPDF), 그림은 PyMuPDF 기하 크롭.",
    "keyword-search": "BM25 키워드 색인을 만들고 조회합니다. API 키가 필요 없습니다.",
    "semantic-search": "Gemini 임베딩과 BM25를 RRF로 결합한 hybrid 색인·조회.",
    "metrics": "Crossref·OpenAlex·Scopus에서 피인용 이력과 레퍼런스를 누적합니다(기본 30일 증분).",
    "bibliography-update": "서지 DB(SQLite)에 논문·저자·기관 귀속을 반영합니다. 기본은 offline.",
    "institution-export": "공개 가능한 기관표를 내보냅니다.",
    "audio": "기존 리뷰로 팟캐스트형 MP3를 만듭니다(Gemini 스크립트 + TTS). 이메일은 보내지 않습니다.",
    "timeline-text": "카테고리별 연구 흐름 내러티브를 씁니다.",
    "timeline-image": "PaperBanana로 카테고리·메인 타임라인 그림을 만듭니다.",
    "zotero-sync": "Zotero 원격 상태와 동기화합니다. 기본은 보고만(dry-run), 적용하면 로컬 항목이 삭제될 수 있습니다.",
    "publish": "Cloudflare Workers와 gh-pages 스텁으로 배포합니다.",
    "email": "이미 만든 MP3를 Resend로 보냅니다.",
}

OUTPUTS = {
    "review": "review.md · index.html · bibliography.json",
    "summary": "인용이 붙은 요약", "chat": "인용이 붙은 답변", "comparison": "인용이 붙은 비교표",
    "extract": "text.md · figures/", "keyword-search": "_search_index.json (BM25)",
    "semantic-search": "_search_index.json + 임베딩", "metrics": "citations.md · references.md",
    "bibliography-update": ".cache/bibliography.sqlite3", "institution-export": "공개 기관표 (xlsx)",
    "audio": "MP3", "timeline-text": "타임라인 내러티브", "timeline-image": "타임라인 그림 (PNG)",
    "zotero-sync": "동기화 보고서", "publish": "배포된 사이트", "email": "발송 결과",
}

TRANSMISSION_KO = {
    "selected cloud provider": "선택한 클라우드 제공자",
    "selected provider; Ollama stays on loopback": "선택한 제공자 (Ollama는 이 컴퓨터 안에서만)",
    "none": "없음",
    "Google embedding API": "Google 임베딩 API",
    "none; the paper is classified with the stored HDBSCAN bundle and neighbours are found locally in SPECTER2 embedding space, no model is called":
        "없음 (저장된 HDBSCAN 번들로 분류하고 SPECTER2 임베딩 공간에서 로컬로 이웃을 찾으며, 모델을 호출하지 않음)",
    "Crossref/OpenAlex/Scopus source APIs": "Crossref · OpenAlex · Scopus API",
    "none offline; configured bibliography sources when online; never Zotero Web paging":
        "offline이면 없음, online이면 설정된 서지 소스 (Zotero 웹 페이징은 하지 않음)",
    "none; source redistribution terms remain applicable": "없음 (원 출처의 재배포 조건은 적용됨)",
    "Google script and TTS API; no email": "Google 스크립트·TTS API (이메일 없음)",
    "Anthropic narrative API; no image backend": "Anthropic 내러티브 API (그림 백엔드 없음)",
    "configured PaperBanana backends; inspect preflight": "설정된 PaperBanana 백엔드 (사전 점검 확인)",
    "Zotero API; may remove local deleted entries when applied": "Zotero API (적용 시 로컬 삭제 가능)",
    "Cloudflare/GitHub; publishes artifacts and repository updates": "Cloudflare · GitHub (결과물과 저장소를 공개)",
    "Resend and the specified recipient; domain/recipient rights checked only by send response":
        "Resend와 지정한 수신자 (권한은 발송 응답으로만 확인)",
}

CONFIRM_REQUIRED = {"zotero-sync", "publish", "email"}
COST_TAG = {"local": "로컬", "paid": "유료", "provider-dependent": "제공자별", "unpriced": "단가 미산정"}

EN_PIPELINE = {
    "collect": ("Collect", "Collect papers and reconcile them with Zotero."),
    "search": ("Search and register", "Search arXiv, Semantic Scholar, and OpenAlex in parallel, then register results in Zotero. Only with --source web."),
    "sync": ("Synchronize", "Retrieve changes from the Zotero collection."),
    "dedup": ("Deduplicate", "Find duplicate Zotero entries for the same paper. Report-only (dry-run) by default."),
    "pdf-audit": ("Audit PDF links", "Check that bibliographic metadata matches PDF content and list suspect entries."),
    "review": ("Review", "Extract text and create a structured review for every paper."),
    "extract": ("Extract text and figures", "Extract body text with OpenDataLoader and figures with PyMuPDF. Warn and use PyMuPDF for text if OpenDataLoader is unavailable."),
    "sanity": ("Validate bibliography–PDF match", "Do not review when the Zotero title or DOI differs from the PDF content."),
    "structured-review": ("Structured review", "Claude Sonnet writes a six-section Korean review."),
    "metrics": ("Citations and references", "Accumulate citation history and references. The pipeline continues if an external API fails."),
    "analyze": ("Analyze", "Build relationships between categories and papers."),
    "index": ("Paper index", "Collect paper metadata from reviews into a complete index."),
    "classify": ("Topic modeling and classification", "Create and assign categories with SPECTER2, UMAP, and HDBSCAN. Zero LLM calls; at most three categories per paper."),
    "related": ("Related papers", "Select up to five neighbours per paper per topic using SPECTER2 cosine and title/author BM25 fused through RRF. Cross-topic unions and reverse links can exceed five displayed neighbours. Zero LLM calls."),
    "summaries": ("Category summaries", "Create a summary and subthemes for each category."),
    "timelines": ("Timelines", "Create category research-trend narratives and PaperBanana timeline images."),
    "publish": ("Publish", "Create readable artifacts, search indexes, and the bibliography database."),
    "frontmatter": ("Inject metadata", "Add metadata and related-paper lists to review.md."),
    "validate": ("Validate", "Check sections, links, figures, and timelines with --strict."),
    "html": ("Paper pages", "Create an index.html page for each paper."),
    "topic-index": ("Topic index", "Create topic pages with category cards, Deep Research, and Audio Overview."),
    "search-index": ("Search index", "Create a BM25 plus Gemini-embedding hybrid index and a cross-topic index."),
    "bibliography": ("Bibliography database", "Update the bibliography database (prepare institution sources, apply, finalize, synchronize related papers, validate strictly) and send it to the Mac mini."),
    "cleanup": ("Clean up", "Remove obsolete timeline images and temporary files."),
    "deploy": ("Deploy", "Deploy through Cloudflare Workers and gh-pages redirect stubs. Runs with --mode deploy or credentials."),
    "insights": ("O-2 Insights and network", "--insights: create cross-category insights and an interactive UMAP 2D/3D network."),
    "workflow-diagram": ("Workflow diagram", "Create a cat-style usage-path and pipeline diagram (--style plain is available)."),
}

EN_VALUE = {
    "Zotero 항목": "Zotero entries", "Zotero 동기화 상태": "Zotero synchronization status",
    "Zotero PDF": "Zotero PDF", "유료 API": "Paid API", "외부 서비스 호출": "External service call",
}

UI_EN = {
    "title": "Paper Curation feature map", "subtitle": "Select a node to expand it and view its description on the right",
    "search": "Search features (for example: review, BM25, deploy)", "open": "Expand all", "close": "Collapse all",
    "shortcuts": "Shortcuts", "tree": "Feature tree", "consumes": "Reads", "produces": "Creates",
    "run": "Run example", "copy": "Copy", "copied": "Copied", "same": "Same capability",
    "adjacent": "Previous and next steps", "children": "child items", "technical": "Technical details",
    "help": "Select a node to expand it and view its description. › only expands or collapses.<br>Keyboard: ↑↓ move · → expand · ← collapse/parent · Enter open<br>Tags: <b>Paid</b> and <b>Confirmation required</b> need attention; ↔ marks the same capability elsewhere.",
    "no_results": "No results", "result_suffix": "results · Enter",
}


def node(label, desc, *, kind="stage", tone=None, children=None, **extra):
    out = {"label": label, "desc": desc, "kind": kind}
    if tone:
        out["tone"] = tone
    if children:
        out["children"] = children
    out.update({k: v for k, v in extra.items() if v})
    return out


def feature_tags(f, english=False):
    cred = f.get("credential", {})
    cost = cred.get("cost_class", "")
    costs = ({"local": "Local", "paid": "Paid", "provider-dependent": "Provider-dependent", "unpriced": "Price not set"}
             if english else COST_TAG)
    tags = [{"t": costs.get(cost, cost), "level": "warn" if cost == "paid" else "plain"}]
    if cost == "provider-dependent":
        tags[0]["t"] = "Provider-dependent · Ollama available" if english else "제공자별 · Ollama 가능"
    if cred.get("transmission", "none").split(";")[0].strip() not in ("none", "none offline"):
        tags.append({"t": "External transmission" if english else "외부 전송", "level": "plain"})
    if f["id"] in CONFIRM_REQUIRED:
        tags.append({"t": "Confirmation required" if english else "확인 필수", "level": "warn"})
    return tags


def feature_facts(f, english=False):
    cred = f.get("credential", {})
    providers = f.get("supported_providers") or []
    key = ("No key required" if not providers or cred.get("cost_class") == "local" else "Key required") if english else ("키 불필요" if not providers or cred.get("cost_class") == "local" else "키 필요")
    transmission = cred.get("transmission", "")
    if english:
        transmission = transmission.replace("none", "None").replace("selected", "Selected").replace("configured", "Configured")
    return [
        ["Key" if english else "키", key],
        ["Cost" if english else "비용", ({"local": "Local · no cost", "paid": "Paid API", "provider-dependent": "Depends on provider",
                 "unpriced": "External service (price not set)"} if english else {"local": "로컬 · 비용 없음", "paid": "유료 API", "provider-dependent": "제공자에 따라 다름",
                 "unpriced": "외부 서비스 (단가 미산정)"}).get(cred.get("cost_class"), "")],
        ["External transmission" if english else "외부 전송", transmission if english else TRANSMISSION_KO.get(transmission, transmission)],
    ]


def registry_branch(features, links, english=False):
    paths = PATHS_EN if english else PATHS
    groups = {key: [] for key in paths}
    for f in features:
        providers = ", ".join(f.get("supported_providers") or []) or ("None" if english else "없음")
        groups.setdefault(f.get("start_path", "optional"), []).append(node(
            f.get("label_en", f["id"]) if english else f.get("label_ko", f["id"]),
            (DETAILS_EN if english else DETAILS).get(f["id"], f.get("label_en", "")), kind="feature",
            key=f"feature:{f['id']}", tags=feature_tags(f, english), facts=feature_facts(f, english),
            produces=(OUTPUTS_EN if english else OUTPUTS).get(f["id"], ""), same=links.get(f"feature:{f['id']}", []),
            tech=[["Feature ID" if english else "기능 ID", f["id"]], ["Module" if english else "모듈", f.get("module", "")], ["Provider" if english else "제공자", providers],
                  ["Runtime" if english else "런타임", ", ".join(f.get("runtime") or [])]],
            run=(f'# req.json = {{"schema_version":1,"feature":"{f["id"]}","params":{{…}}}}\n'
                 f"python pipeline/run_feature.py --request req.json            # {'plan' if english else '계획'}\n"
                 f"python pipeline/run_feature.py --request req.json --execute  # {'execute' if english else '실행'}")))
    return [node(label, desc, kind=kind, tone=kind, children=groups[key])
            for key, (kind, label, desc) in paths.items() if groups.get(key)]


STEP_COST = {"local": ("로컬", "plain"), "paid": ("유료", "warn"), "external": ("외부 서비스", "plain")}


def pipeline_branch(pmap, links, english=False):
    stages = []
    for si, stage in enumerate(pmap["stages"], 1):
        steps = []
        for ti, step in enumerate(stage["steps"], 1):
            t, lvl = STEP_COST[step["cost"]]
            if english:
                t = {"로컬": "Local", "유료": "Paid", "외부 서비스": "External service"}[t]
            tags = [{"t": t, "level": lvl}]
            if step.get("optional"):
                tags.append({"t": "Optional" if english else "선택", "level": "plain"})
            facts = [["Cost" if english else "비용", ({"local": "Local · no cost", "paid": "Paid API", "external": "External service call"} if english else {"local": "로컬 · 비용 없음", "paid": "유료 API", "external": "외부 서비스 호출"})[step["cost"]]]]
            if step.get("model"):
                facts.append(["Model" if english else "모델", step["model"]])
            label, desc = EN_PIPELINE.get(step["id"], (step["label"], step["desc"])) if english else (step["label"], step["desc"])
            steps.append(node(
                f"{si}-{ti} {label}", desc, key=f"step:{step['id']}", tags=tags, facts=facts,
                consumes=" · ".join(EN_VALUE.get(v, v) if english else v for v in step.get("inputs", [])), produces=" · ".join(EN_VALUE.get(v, v) if english else v for v in step.get("outputs", [])),
                same=links.get(f"step:{step['id']}", []), dashed=bool(step.get("optional")),
                tech=[["Script" if english else "스크립트", f"pipeline/{step['script']}.py"],
                      ["Run step" if english else "실행 단계", ", ".join(step.get("run_steps", []))]]))
        label, desc = EN_PIPELINE.get(stage["id"], (stage["label"], stage["desc"])) if english else (stage["label"], stage["desc"])
        stages.append(node(f"{'①②③④⑤⑥'[si - 1]} {label}", desc, kind="stage", children=steps))
    options = [node(*(EN_PIPELINE.get(o["id"], (o["label"], o["desc"])) if english else (o["label"], o["desc"])), key=f"step:{o['id']}", dashed=True,
                    tags=[{"t": {"로컬": "Local", "유료": "Paid", "외부 서비스": "External service"}.get(STEP_COST[o["cost"]][0], STEP_COST[o["cost"]][0]) if english else STEP_COST[o["cost"]][0], "level": STEP_COST[o["cost"]][1]}, {"t": "Optional" if english else "선택", "level": "plain"}],
                    tech=[["Script" if english else "스크립트", f"pipeline/{o['script']}.py"]])
               for o in pmap.get("options", [])]
    stages.append(node("Optional steps" if english else "선택 옵션", "Steps that run only when enabled by a flag or mode." if english else "플래그나 모드로 켤 때만 실행하는 단계.", kind="stage", children=options, dashed=True))
    return stages


def same_function_links(pmap, features, english=False):
    """step ↔ feature pairs taken from pipeline_map.json 'features'."""
    label = {f["id"]: (f.get("label_en", f["id"]) if english else f.get("label_ko", f["id"])) for f in features}
    links = {}
    for stage in pmap["stages"]:
        for step in stage["steps"]:
            for fid in step.get("features", []):
                links.setdefault(f"step:{step['id']}", []).append(
                    {"key": f"feature:{fid}", "label": f"{'Feature' if english else '기능'} › {label[fid]}"})
                links.setdefault(f"feature:{fid}", []).append(
                    {"key": f"step:{step['id']}", "label": f"{'Full curation' if english else '전체 큐레이션'} › {(EN_PIPELINE[stage['id']][0] if english else stage['label'])} › {(EN_PIPELINE[step['id']][0] if english else step['label'])}"})
    return links


def build_tree(features, pmap=None, english=False):
    pmap = pmap or json.loads(PIPELINE_MAP.read_text(encoding="utf-8"))
    links = same_function_links(pmap, features, english)
    if english:
        return node("Paper Curation", "A system that turns Zotero papers into structured reviews, classification, connections, search, and timelines. It answers three questions: how to use it, what it can do, and how full curation runs.", kind="root", children=[
            node("How to use it", "Three entry points and the shared runner used by every capability.", kind="group", tone="howto", children=[
                node("Paper Curio (Zotero right-click)", "A Zotero 9/10 plugin. Right-click a paper to create a review, run feature modules, AI Chat, or Citedby.", facts=[["Install", "paper-curio-zotero9.xpi or zotero10.xpi for the matching Zotero version"]]),
                node("Command line: run_feature.py", "Plan → confirm → execute one capability.", run="python pipeline/run_feature.py --list"),
                node("Full curation: run_full.py", "An advanced path that processes a whole collection in order.", run="python pipeline/run_full.py --topic <topic> --mode curate --dry-run"),
                node("Plan → confirm → execute", "Every capability passes through the same safeguards.", children=[
                    node("Plan", "Before execution, show requirements, transmission destination, and cost. It writes nothing."),
                    node("Confirm", "Approve the plan. Synchronization, publishing, and email require explicit confirmation."),
                    node("Execute", "Use corpus reservation and registration locks, cost caps, preserve partial results on failure, and never automatically send work to another provider."),
                    node("Credentials", "Look up environment variables, then the OS keyring (credential:<provider>). Never store keys in plaintext settings files."),
                ]),
            ]),
            node("What it can do", "On-demand capabilities, in-browser capabilities, and separate tools.", kind="group", tone="what", children=registry_branch(features, links, True) + [
                node("In-browser capabilities", "Capabilities available directly on topic pages.", kind="group", tone="browser", children=[
                    node("Deep Research", "Natural-language question → hybrid search → answer with the reader's own key (Anthropic, OpenAI, or Google) and [N] citations.", tags=[{"t": "Reader key", "level": "plain"}]),
                    node("Audio Overview", "Create and download an MP3 with Gemini TTS. Deployed copies can also deliver it by email.", tags=[{"t": "Reader key", "level": "plain"}]),
                    node("Obsidian integration", "Knowledge compounding: notes inform subsequent questions."),
                ]),
                node("Analysis and management tools", "Tools used outside the pipeline.", kind="group", tone="tools", children=[
                    node("Citedby", "Collect a paper's citation genealogy from OpenAlex, Scopus, S2, and arXiv into an HTML report. With --topic, citing papers are filtered by topic relevance before the 5W1H summaries.",
                         run="python pipeline/run_citedby.py --doi <doi> --topic <topic>",
                         facts=[["Topic filter", "OpenAI Decision API (gpt-6-luna): relevance probability per paper, kept at 0.5 or above (needs OPENAI_API_KEY and openai>=3.35)"],
                                ["Without the key", "LLM JSON judging (Anthropic → Google → OpenAI Chat); also used for a batch whose Decision call fails"]]),
                    node("Author and institution affiliation", "Resolve authors and institutions in order: OpenAlex → Scopus → PDF byline → ROR/ORCID."),
                    node("Recovery tools", "Use auto_recover, fix_matching, and validate to find and repair wrongly connected PDFs and broken reviews."),
                    node("Institution reports", "Use the bibliography database to create reports on research trends, parallel laboratories, and representative researchers."),
                ]),
            ]),
            node("How full curation runs", "run_full.py --mode curate executes the following steps in order. Dashed steps are optional.", kind="group", tone="pipeline", children=pipeline_branch(pmap, links, True)),
        ])
    return node("Paper Curation",
                "Zotero 논문을 구조화 리뷰·분류·연결·검색·타임라인으로 바꾸는 시스템입니다. "
                "세 가지 질문으로 나눴습니다: 어떻게 쓰나, 무엇을 할 수 있나, 전체 큐레이션은 어떻게 도나.",
                kind="root", children=[
        node("어떻게 쓰나", "입구 세 가지와, 모든 기능이 거치는 공통 실행기.", kind="group", tone="howto", children=[
            node("Paper Curio (Zotero 우클릭)", "Zotero 9/10 플러그인. 논문을 우클릭해 리뷰 생성, 기능 모듈, AI Chat, Citedby를 실행합니다.",
                 facts=[["설치", "Zotero 버전에 맞는 paper-curio-zotero9.xpi 또는 zotero10.xpi"]]),
            node("명령줄 run_feature.py", "기능 하나를 계획 → 확인 → 실행합니다.",
                 run="python pipeline/run_feature.py --list"),
            node("전체 큐레이션 run_full.py", "컬렉션 전체를 순서대로 처리하는 고급 경로입니다.",
                 run="python pipeline/run_full.py --topic <topic> --mode curate --dry-run"),
            node("계획 → 확인 → 실행", "모든 기능이 같은 안전장치를 거칩니다.", children=[
                node("계획 (plan)", "실행 전에 요구조건, 데이터가 전송되는 곳, 비용을 보여줍니다. 아무것도 쓰지 않습니다."),
                node("확인", "계획을 보고 승인합니다. 동기화·배포·이메일은 명시적 확인이 필수입니다."),
                node("실행 (execute)", "코퍼스 예약·등록 잠금, 비용 상한, 실패 시 부분 결과 보존, 다른 제공자로 자동 전송하지 않음."),
                node("자격증명", "환경변수 → OS 키 저장소(credential:<provider>) 순서로 찾습니다. 평문 설정 파일에는 키를 두지 않습니다."),
            ]),
        ]),
        node("무엇을 할 수 있나", "필요할 때 하나씩 실행하는 기능과, 결과 페이지 안의 기능, 별도 도구.", kind="group", tone="what",
             children=registry_branch(features, links) + [
            node("브라우저 안 기능", "토픽 페이지에서 바로 쓰는 기능.", kind="group", tone="browser", children=[
                node("Deep Research", "자연어 질문 → hybrid 검색 → 독자 자신의 키(Anthropic · OpenAI · Google)로 답변하고 [N] 인용을 붙입니다.",
                     tags=[{"t": "독자 키", "level": "plain"}]),
                node("Audio Overview", "Gemini TTS로 MP3를 만들어 내려받습니다. 배포본에서는 이메일 전달도 가능합니다.",
                     tags=[{"t": "독자 키", "level": "plain"}]),
                node("Obsidian 연동", "메모가 다음 질의에 반영되는 지식 축적."),
            ]),
            node("분석·관리 도구", "파이프라인 밖에서 쓰는 도구.", kind="group", tone="tools", children=[
                node("Citedby", "한 논문의 인용 계보를 OpenAlex · Scopus · S2 · arXiv에서 모아 HTML 보고서로 만듭니다. --topic을 주면 5W1H 요약 전에 주제 관련성으로 인용논문을 거릅니다.",
                     run="python pipeline/run_citedby.py --doi <doi> --topic <topic>",
                     facts=[["주제 필터", "OpenAI Decision API(gpt-6-luna)가 논문별 관련성 확률을 매겨 0.5 이상만 남김 (OPENAI_API_KEY, openai>=3.35 필요)"],
                            ["키가 없을 때", "LLM JSON 판정(Anthropic → Google → OpenAI Chat). Decision 호출이 실패한 배치도 이 경로"]]),
                node("저자·기관 귀속", "OpenAlex → Scopus → PDF 바이라인 → ROR/ORCID 순서로 저자와 기관을 확정합니다."),
                node("복구 도구", "auto_recover · fix_matching · validate로 잘못 연결된 PDF와 깨진 리뷰를 찾아 고칩니다."),
                node("기관 보고서", "서지 DB로 연구 흐름·병렬 연구실·대표 연구자 보고서를 만듭니다."),
            ]),
        ]),
        node("전체 큐레이션은 어떻게 도나", "run_full.py --mode curate가 아래 단계를 순서대로 실행합니다. 점선은 선택 단계입니다.",
             kind="group", tone="pipeline", children=pipeline_branch(pmap, links)),
    ])


TEMPLATE = r"""<!doctype html>
<html lang="__LANG__"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>__TITLE__</title>
<style>
:root{
  --ink:#1f2937;--muted:#5b6472;--faint:#6b7280;--rule:#e5e7eb;--paper:#f7f7f4;
  --root:#1f2937;--howto:#4c6a92;--what:#2f7d78;--pipeline:#2e6f95;--browser:#a65d57;--tools:#6e7d3a;
  --read:#4e8b62;--ai:#4a63a8;--collection:#9a6226;--optional:#8a5a9e;--warn:#b4533f;
}
*{box-sizing:border-box}
body{margin:0;font:15px/1.55 "Pretendard",-apple-system,BlinkMacSystemFont,"Apple SD Gothic Neo","Noto Sans KR",sans-serif;color:var(--ink);background:#fff}
header{display:flex;align-items:center;gap:12px;flex-wrap:wrap;padding:14px 24px;border-bottom:1px solid var(--rule)}
.brand{display:flex;flex-direction:column;margin-right:6px}
.brand h1{margin:0;font-size:19px;letter-spacing:-.01em}
.brand small{color:var(--muted);font-size:12.5px}
.search{position:relative;display:flex;align-items:center;gap:8px}
.search input{width:250px;padding:8px 12px 8px 32px;border:1px solid var(--rule);border-radius:10px;font:inherit;background:#fafafa;outline:none;transition:.15s}
.search input:focus{background:#fff;border-color:#c7d2fe;box-shadow:0 0 0 3px #eef2ff}
.search::before{content:"⌕";position:absolute;left:11px;top:50%;transform:translateY(-52%);color:var(--faint);font-size:16px}
#count{font-size:12.5px;color:var(--muted);min-width:64px}
.btn{padding:7px 12px;border:1px solid var(--rule);border-radius:10px;background:#fff;color:#374151;font:inherit;font-size:13.5px;cursor:pointer;transition:.15s}
.btn:hover{background:#f3f4f6}
.legend{display:flex;gap:6px;flex-wrap:wrap;margin-left:auto;align-items:center}
.legend small{color:var(--muted);font-size:12px;margin-right:2px}
.chip{font:inherit;font-size:12px;padding:3px 9px;border-radius:999px;cursor:pointer;color:color-mix(in srgb,var(--c) 85%,#111827);background:color-mix(in srgb,var(--c) 10%,#fff);border:1px solid color-mix(in srgb,var(--c) 24%,#fff)}
.chip:hover{background:color-mix(in srgb,var(--c) 18%,#fff)}
main{display:grid;grid-template-columns:minmax(0,1fr) minmax(320px,400px);height:calc(100vh - 69px)}
#tree{overflow:auto;padding:24px 28px 120px;background-color:var(--paper);background-image:radial-gradient(#e4e4df 1px,transparent 1px);background-size:18px 18px}
.tree ul{position:relative;display:flex;flex-direction:column;gap:9px;margin:0;padding:0 0 0 36px;list-style:none}
.tree>ul{padding-left:0}
.tree li{position:relative;display:flex;align-items:flex-start;margin:0}
.tree li::before{content:"";position:absolute;left:-18px;top:18px;width:18px;border-top:1.5px solid var(--lc,#d1d5db)}
.tree li::after{content:"";position:absolute;left:-18px;top:-5px;bottom:-5px;border-left:1.5px solid var(--lc,#d1d5db)}
.tree li:first-child::after{top:18px}.tree li:last-child::after{bottom:auto;height:23px}.tree li:only-child::after{display:none}
.tree>ul>li::before,.tree>ul>li::after{display:none}
.tree li>ul{padding-top:0}
.tree li>ul::before{content:"";position:absolute;left:0;top:18px;width:18px;border-top:1.5px solid var(--lc,#d1d5db)}
.node{display:inline-flex;align-items:center;gap:7px;padding:6px 11px 6px 6px;border-radius:9px;background:#fff;color:var(--ink);
  border:1px solid color-mix(in srgb,var(--c) 28%,#e5e7eb);border-left:4px solid var(--c);
  cursor:pointer;user-select:none;white-space:nowrap;transition:background .15s,box-shadow .15s;box-shadow:0 1px 2px rgba(17,24,39,.05);outline:none}
.node:hover{background:color-mix(in srgb,var(--c) 7%,#fff);box-shadow:0 3px 10px rgba(17,24,39,.08)}
.node:focus-visible{box-shadow:0 0 0 3px color-mix(in srgb,var(--c) 35%,#fff)}
.node.dashed{border-style:dashed;border-left-style:solid}
.node.branch{background:color-mix(in srgb,var(--c) 9%,#fff);font-weight:600;color:color-mix(in srgb,var(--c) 72%,#111827)}
.node.root{background:var(--root);color:#fff;border-color:var(--root);font-weight:600;padding:8px 15px 8px 8px;border-radius:11px}
.node.sel{background:var(--c);color:#fff;border-color:var(--c);box-shadow:0 4px 14px color-mix(in srgb,var(--c) 35%,transparent)}
.node.hit{box-shadow:0 0 0 3px #fde68a}
.node.hit.cur{box-shadow:0 0 0 3px #f59e0b}
.tog{display:inline-flex;align-items:center;justify-content:center;width:20px;height:20px;border-radius:6px;color:var(--c);font-size:14px;transition:transform .15s,background .15s}
.tog:hover{background:color-mix(in srgb,var(--c) 14%,#fff)}
li:not(.closed)>.node>.tog.has{transform:rotate(90deg)}
.node.root .tog,.node.sel .tog{color:#fff}
.dot{width:20px;display:inline-flex;justify-content:center}.dot::before{content:"";width:6px;height:6px;border-radius:50%;background:var(--c);opacity:.75}
.node.sel .dot::before{background:#fff}
.badge{font-size:11px;font-weight:500;min-width:20px;text-align:center;padding:1px 6px;border-radius:999px;color:var(--c);background:color-mix(in srgb,var(--c) 13%,#fff)}
.node.root .badge,.node.sel .badge{color:#fff;background:rgba(255,255,255,.22)}
.tag{font-size:11px;font-weight:500;padding:1px 7px;border-radius:6px;color:#4b5563;background:#fff;border:1px solid #d9dee5}
.tag.warn{color:var(--warn);border-color:color-mix(in srgb,var(--warn) 35%,#fff);background:color-mix(in srgb,var(--warn) 7%,#fff)}
.node.sel .tag{color:#fff;border-color:rgba(255,255,255,.45);background:transparent}
.same{font-size:12px;color:var(--c);opacity:.8}.node.sel .same{color:#fff}
li.closed>ul{display:none}
aside{position:relative;overflow:auto;padding:24px 24px 40px;border-left:1px solid var(--rule);background:#fff;overflow-wrap:anywhere}
aside::before{content:"";position:absolute;inset:0 0 auto 0;height:4px;background:var(--c,#1f2937)}
.crumb{font-size:12.5px;color:var(--muted);margin-bottom:8px;display:flex;flex-wrap:wrap;gap:4px}
.crumb a{color:var(--muted);cursor:pointer;text-decoration:none}.crumb a:hover{color:var(--ink);text-decoration:underline}
aside h2{margin:0 0 10px;font-size:19px;letter-spacing:-.01em}
.facts{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 14px}
.fact{font-size:12.5px;padding:5px 9px;border-radius:8px;background:color-mix(in srgb,var(--c) 8%,#fff);border:1px solid color-mix(in srgb,var(--c) 18%,#fff)}
.fact b{color:var(--muted);font-weight:500;margin-right:5px}
aside p{margin:0 0 16px;color:#374151}
.sec{margin:0 0 14px}.sec h3{font-size:12.5px;color:var(--muted);font-weight:600;margin:0 0 6px}
.sec .val{font-size:13.5px}
code{font:12.5px/1.5 Menlo,monospace;background:#f3f4f6;border-radius:6px;padding:2px 6px}
.run{display:flex;align-items:flex-start;gap:8px}.run code{flex:1;min-width:0;padding:8px 10px;white-space:pre;overflow-x:auto;display:block}
.copy{font-size:12px;padding:5px 9px;border-radius:8px;border:1px solid var(--rule);background:#fff;cursor:pointer}
.pills{display:flex;flex-wrap:wrap;gap:6px}
.pills a{font-size:13px;padding:4px 10px;border-radius:999px;cursor:pointer;color:color-mix(in srgb,var(--c) 80%,#111827);background:color-mix(in srgb,var(--c) 9%,#fff);border:1px solid color-mix(in srgb,var(--c) 20%,#fff);transition:.15s}
.pills a:hover{background:color-mix(in srgb,var(--c) 18%,#fff)}
details{margin-top:6px;border-top:1px solid var(--rule);padding-top:10px}
summary{cursor:pointer;color:var(--muted);font-size:12.5px;font-weight:600}
dl{display:grid;grid-template-columns:max-content 1fr;gap:6px 12px;margin:10px 0 0;font-size:12.5px}
dt{color:var(--muted);white-space:nowrap}dd{margin:0}
.help{font-size:12px;color:var(--muted);margin-top:18px;line-height:1.6}
@media(max-width:900px){main{grid-template-columns:1fr;height:auto}aside{border-left:0;border-top:1px solid var(--rule)}.legend{margin-left:0}}
</style></head><body>
<header>
<div class="brand"><h1>__TITLE__</h1><small>__SUBTITLE__</small></div>
<label class="search"><input id="q" placeholder="__SEARCH__" aria-label="__SEARCH__"><span id="count"></span></label>
<button class="btn" id="open">__OPEN__</button><button class="btn" id="close">__CLOSE__</button>
<div class="legend"><small>__SHORTCUTS__</small>
<button class="chip" style="--c:var(--howto)" data-go="__HOWTO__">__HOWTO__</button>
<button class="chip" style="--c:var(--read)" data-go="__READ__">Read</button>
<button class="chip" style="--c:var(--ai)" data-go="__AI__">AI</button>
<button class="chip" style="--c:var(--collection)" data-go="__COLLECTION__">Collection</button>
<button class="chip" style="--c:var(--optional)" data-go="__OPTIONAL__">Optional</button>
<button class="chip" style="--c:var(--pipeline)" data-go="__PIPELINE__">__PIPELINE__</button>
<a class="btn" href="__OTHER_PAGE__">__OTHER_LANGUAGE__</a>
</div>
</header>
<main><section id="tree" class="tree" role="tree" aria-label="__TREE_LABEL__"></section><aside id="panel" aria-live="polite"></aside></main>
<script>
const TREE = __TREE__;
const KIND=__KIND__;
let id=0;const byId={},byKey={};
function index(n,p,d){n.id=++id;n.parent=p;n.depth=d;byId[n.id]=n;if(n.key)byKey[n.key]=n;(n.children||[]).forEach(c=>index(c,n,d+1));}
index(TREE,null,0);
function tone(n){let x=n;while(x&&!x.tone)x=x.parent;return x?`var(--${x.tone})`:"var(--root)";}
function esc(s){return String(s).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));}
function render(n){
  const li=document.createElement("li");li.dataset.id=n.id;li.setAttribute("role","treeitem");
  if(n.depth>=1&&n.children)li.classList.add("closed");
  const c=tone(n);li.style.setProperty("--c",c);
  const d=document.createElement("span");d.className="node";d.tabIndex=-1;
  if(n.depth===0)d.classList.add("root");else if(n.children)d.classList.add("branch");
  if(n.dashed)d.classList.add("dashed");
  const t=document.createElement("span");
  if(n.children){t.className="tog has";t.textContent="›";t.title="__TOGGLE__";t.onclick=e=>{e.stopPropagation();toggle(li);};}
  else t.className="dot";
  d.append(t,document.createTextNode(n.label));
  if(n.children){const b=document.createElement("span");b.className="badge";b.textContent=n.children.length;d.append(b);}
  (n.tags||[]).forEach(g=>{const s=document.createElement("span");s.className="tag"+(g.level==="warn"?" warn":"");s.textContent=g.t;d.append(s);});
  if(n.same&&n.same.length){const s=document.createElement("span");s.className="same";s.textContent="↔";s.title="__SAME_TITLE__";d.append(s);}
  d.onclick=()=>select(n,{open:true});
  li.append(d);
  if(n.children){const ul=document.createElement("ul");ul.setAttribute("role","group");
    ul.style.setProperty("--lc",n.depth===0?"#d1d5db":`color-mix(in srgb, ${c} 40%, #e5e7eb)`);
    n.children.forEach(k=>ul.append(render(k)));li.append(ul);}
  n.el=d;n.li=li;return li;
}
function toggle(li,closed){const c=closed===undefined?!li.classList.contains("closed"):closed;li.classList.toggle("closed",c);
  li.setAttribute("aria-expanded",String(!c));}
function reveal(n){let x=n.parent;while(x){toggle(x.li,false);x=x.parent;}}
function visible(){return Object.values(byId).filter(n=>{let x=n.parent;while(x){if(x.li.classList.contains("closed"))return false;x=x.parent;}return true;}).sort((a,b)=>a.id-b.id);}
let current=TREE;
function crumbs(n){const p=[];let x=n.parent;while(x){p.unshift(x);x=x.parent;}
  return p.map(x=>`<a data-id="${x.id}">${esc(x.label)}</a>`).join(" › ");}
function sec(title,html){return html?`<div class="sec"><h3>${title}</h3>${html}</div>`:"";}
function pills(list){return `<div class="pills">${list.map(x=>`<a data-id="${x.id}" style="--c:${tone(x)}">${esc(x.label)}</a>`).join("")}</div>`;}
function select(n,{open=false,scroll=true}={}){
  current=n;document.querySelectorAll(".node.sel").forEach(e=>e.classList.remove("sel"));if(n.depth>0)n.el.classList.add("sel");
  reveal(n);if(open&&n.children)toggle(n.li,false);
  document.querySelectorAll(".node[tabindex='0']").forEach(e=>e.tabIndex=-1);n.el.tabIndex=0;
  const panel=document.getElementById("panel");panel.style.setProperty("--c",tone(n));
  let h=`<div class="crumb">${crumbs(n)||"&nbsp;"}</div><h2>${esc(n.label)}</h2>`;
  if(n.facts&&n.facts.length)h+=`<div class="facts">${n.facts.filter(f=>f[1]).map(f=>`<span class="fact"><b>${esc(f[0])}</b>${esc(f[1])}</span>`).join("")}</div>`;
  h+=`<p>${esc(n.desc)}</p>`;
  h+=sec("__CONSUMES__",n.consumes?`<div class="val">${esc(n.consumes)}</div>`:"");
  h+=sec("__PRODUCES__",n.produces?`<div class="val">${esc(n.produces)}</div>`:"");
  if(n.run)h+=sec("__RUN__",`<div class="run"><code>${esc(n.run)}</code><button class="copy" data-copy="${esc(n.run)}">__COPY__</button></div>`);
  if(n.same&&n.same.length)h+=sec("__SAME__",pills(n.same.map(s=>byKey[s.key]).filter(Boolean).map(x=>({...x,label:n.same.find(s=>s.key===x.key).label}))));
  const sib=n.parent&&n.parent.children&&n.key&&n.key.startsWith("step:")?n.parent.children:null;
  if(sib){const i=sib.indexOf(n);const nb=[];if(i>0)nb.push({...sib[i-1],label:"← "+sib[i-1].label});if(i<sib.length-1)nb.push({...sib[i+1],label:sib[i+1].label+" →"});
    if(nb.length)h+=sec("__ADJACENT__",pills(nb));}
  if(n.children)h+=sec(`__CHILDREN_PREFIX__ ${n.children.length} __CHILDREN_SUFFIX__`,pills(n.children));
  if(n.tech&&n.tech.some(t=>t[1]))h+=`<details><summary>__TECHNICAL__</summary><dl>${n.tech.filter(t=>t[1]).map(t=>`<dt>${esc(t[0])}</dt><dd>${esc(t[1])}</dd>`).join("")}</dl></details>`;
  if(n.depth===0)h+=`<div class="help">__HELP__</div>`;
  panel.innerHTML=h;
  panel.querySelectorAll("a[data-id]").forEach(a=>a.onclick=()=>{const k=byId[a.dataset.id];select(k,{open:true});});
  panel.querySelectorAll("[data-copy]").forEach(b=>b.onclick=()=>{navigator.clipboard&&navigator.clipboard.writeText(b.dataset.copy);b.textContent="__COPIED__";setTimeout(()=>b.textContent="__COPY__",1200);});
  if(scroll)n.el.scrollIntoView({block:"nearest",inline:"nearest",behavior:"smooth"});
  history.replaceState(null,"","#"+encodeURIComponent(n.label));
}
const root=document.createElement("ul");root.append(render(TREE));document.getElementById("tree").append(root);
document.getElementById("open").onclick=()=>Object.values(byId).forEach(n=>n.children&&toggle(n.li,false));
document.getElementById("close").onclick=()=>Object.values(byId).forEach(n=>n.children&&n.depth>=1&&toggle(n.li,true));
document.querySelectorAll("[data-go]").forEach(b=>b.onclick=()=>{const n=Object.values(byId).find(x=>x.label===b.dataset.go);if(n)select(n,{open:true});});
let hits=[],hi=-1;const qEl=document.getElementById("q"),countEl=document.getElementById("count");
function runSearch(){const q=qEl.value.trim().toLowerCase();hits=[];hi=-1;
  Object.values(byId).forEach(n=>{const s=(n.label+" "+n.desc+" "+JSON.stringify(n.facts||[])+JSON.stringify(n.tech||[])+(n.produces||"")).toLowerCase();
    const hit=!!q&&s.includes(q);n.el.classList.toggle("hit",hit);n.el.classList.remove("cur");if(hit){hits.push(n);reveal(n);}});
  countEl.textContent=q?(hits.length?`${hits.length} __RESULT_SUFFIX__`:"__NO_RESULTS__"):"";
  if(hits.length)step(1);}
function step(dir){if(!hits.length)return;if(hi>=0)hits[hi].el.classList.remove("cur");hi=(hi+dir+hits.length)%hits.length;
  const n=hits[hi];n.el.classList.add("cur");n.el.scrollIntoView({block:"center",inline:"nearest",behavior:"smooth"});
  countEl.textContent=`${hi+1}/${hits.length} · Enter`;}
qEl.oninput=runSearch;
qEl.onkeydown=e=>{if(e.key==="Enter"){e.preventDefault();if(e.shiftKey)step(-1);else if(hits.length&&hi>=0&&e.altKey)select(hits[hi]);else step(1);}
  if(e.key==="Escape"){qEl.value="";runSearch();}};
document.getElementById("tree").addEventListener("keydown",e=>{const n=current;if(!n)return;const vis=visible();const i=vis.indexOf(n);
  if(e.key==="ArrowDown"&&i<vis.length-1){e.preventDefault();select(vis[i+1]);vis[i+1].el.focus();}
  else if(e.key==="ArrowUp"&&i>0){e.preventDefault();select(vis[i-1]);vis[i-1].el.focus();}
  else if(e.key==="ArrowRight"&&n.children){e.preventDefault();if(n.li.classList.contains("closed"))toggle(n.li,false);else{select(n.children[0]);n.children[0].el.focus();}}
  else if(e.key==="ArrowLeft"){e.preventDefault();if(n.children&&!n.li.classList.contains("closed")&&n.depth>0)toggle(n.li,true);else if(n.parent){select(n.parent);n.parent.el.focus();}}
  else if(e.key==="Enter"||e.key===" "){e.preventDefault();if(n.children)toggle(n.li);}});
const hash=decodeURIComponent(location.hash.slice(1));select(Object.values(byId).find(n=>n.label===hash)||TREE,{open:true,scroll:false});
</script></body></html>
"""


def render_html(tree, english=False):
    ui = UI_EN if english else {
        "title": "Paper Curation 기능 지도", "subtitle": "노드를 누르면 펼쳐지고, 설명은 오른쪽에 나옵니다",
        "search": "기능 검색 (예: 리뷰, BM25, 배포)", "open": "모두 펼치기", "close": "모두 접기",
        "shortcuts": "바로 가기", "tree": "기능 트리", "consumes": "읽는 것", "produces": "만드는 것",
        "run": "실행 예시", "copy": "복사", "copied": "복사됨", "same": "같은 기능",
        "adjacent": "앞뒤 단계", "children": "하위 항목", "technical": "기술 정보",
        "help": "노드를 누르면 펼쳐지고 설명이 나옵니다. › 는 접기·펼치기만 합니다.<br>키보드: ↑↓ 이동 · → 펼치기 · ← 접기/상위로 · Enter 열기<br>태그: <b>유료</b>·<b>확인 필수</b>는 주의, ↔ 는 같은 기능이 다른 곳에도 있다는 표시",
        "no_results": "결과 없음", "result_suffix": "개 · Enter",
    }
    shortcuts = {
        "HOWTO": "How to use it" if english else "어떻게 쓰나",
        "READ": PATHS_EN["reading"][1] if english else PATHS["reading"][1],
        "AI": PATHS_EN["ai"][1] if english else PATHS["ai"][1],
        "COLLECTION": PATHS_EN["collection"][1] if english else PATHS["collection"][1],
        "OPTIONAL": PATHS_EN["optional"][1] if english else PATHS["optional"][1],
        "PIPELINE": "How full curation runs" if english else "전체 큐레이션은 어떻게 도나",
    }
    replacements = {
        "LANG": "en" if english else "ko", "TITLE": ui["title"], "SUBTITLE": ui["subtitle"],
        "SEARCH": ui["search"], "OPEN": ui["open"], "CLOSE": ui["close"], "SHORTCUTS": ui["shortcuts"],
        "TREE_LABEL": ui["tree"], "OTHER_PAGE": "feature-map.html" if english else "feature-map.en.html",
        "OTHER_LANGUAGE": "Korean" if english else "English",
        "CONSUMES": ui["consumes"], "PRODUCES": ui["produces"], "RUN": ui["run"], "COPY": ui["copy"],
        "COPIED": ui["copied"], "SAME": ui["same"], "ADJACENT": ui["adjacent"], "TECHNICAL": ui["technical"],
        "HELP": ui["help"], "NO_RESULTS": ui["no_results"], "RESULT_SUFFIX": ui["result_suffix"],
        "CHILDREN_PREFIX": ui["children"] if not english else "", "CHILDREN_SUFFIX": "개" if not english else ui["children"],
        **shortcuts,
    }
    html = TEMPLATE.replace("__TREE__", json.dumps(tree, ensure_ascii=False).replace("</", "<\\/"))
    kinds = ({"root": "All", "group": "Area", "read": "Read path", "ai": "AI path",
              "collection": "Collection path", "optional": "Optional feature", "feature": "Feature", "stage": "Step"}
             if english else {"root": "전체", "group": "영역", "read": "Read 경로", "ai": "AI 경로",
                               "collection": "Collection 경로", "optional": "선택 기능", "feature": "기능", "stage": "단계"})
    replacements["KIND"] = json.dumps(kinds, ensure_ascii=False)
    replacements["TOGGLE"] = "Expand/collapse" if english else "펼치기/접기"
    replacements["SAME_TITLE"] = "The same capability appears elsewhere" if english else "같은 기능이 다른 곳에도 있습니다"
    for key, value in replacements.items():
        html = html.replace(f"__{key}__", value)
    return html


def main() -> int:
    features = json.loads(REGISTRY.read_text(encoding="utf-8"))["features"]
    OUTPUT.write_text(render_html(build_tree(features)), encoding="utf-8")
    OUTPUT_EN.write_text(render_html(build_tree(features, english=True), english=True), encoding="utf-8")
    print(f"wrote {OUTPUT.relative_to(ROOT)} and {OUTPUT_EN.relative_to(ROOT)} ({len(features)} registry features)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
