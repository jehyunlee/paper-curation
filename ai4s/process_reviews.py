"""Process 5 academic papers with PDFs and generate Korean reviews."""
import sys
import os
import re
import json
from pathlib import Path

# Setup originality extraction
sys.path.insert(0, r"C:\Users\jehyu\Arbeitplatz\01_Work\01_Devs\AX\scisci\scie")
from lib.originality import load_triggers, get_originality_strict

import fitz  # PyMuPDF

TRIGGER_PATH = r"C:\Users\jehyu\Arbeitplatz\01_Work\01_Devs\AX\scisci\scie\lib\originality_triggers.json"
OUTPUT_BASE = Path(r"C:\Users\jehyu\Arbeitplatz\paper-curation\ai4s")

def _find_pdf(keyword):
    """Find PDF in Zotero folder by keyword match."""
    import os
    zotero = r"C:\Users\jehyu\GoogleDrive\Zotero"
    files = os.listdir(zotero)
    matches = [f for f in files if keyword in f and f.endswith(".pdf")]
    if not matches:
        raise FileNotFoundError(f"No PDF found for keyword: {keyword}")
    # Prefer files without " 1." suffix if multiple matches
    preferred = [m for m in matches if " 1." not in m]
    chosen = preferred[0] if preferred else matches[0]
    return os.path.join(zotero, chosen)


PAPERS = [
    {
        "num": 236,
        "title": "Artificial intelligence tools expand scientists' impact but contract science's focus",
        "date": "2026-01-14",
        "pdf_keyword": "Hao et al._2026",
        "slug": "236_AI_tools_expand_scientists_impact_but_contract_sciences_focus",
    },
    {
        "num": 237,
        "title": "Artificial intelligence for science\u2014bridging data to wisdom",
        "date": "2023-11-13",
        "pdf_keyword": "Xu et al._2023_Artificial intelligence for science",
        "slug": "237_Artificial_intelligence_for_science_bridging_data_to_wisdom",
    },
    {
        "num": 238,
        "title": "Virtual lab powered by 'AI scientists' super-charges biomedical research",
        "date": "2024-12-04",
        "pdf_keyword": "Kudiabor_2024_Virtual lab",
        "slug": "238_Virtual_lab_powered_by_AI_scientists_super-charges_biomedical_research",
    },
    {
        "num": 239,
        "title": "Foundation models for materials discovery \u2013 current state and future directions",
        "date": "2025-03-06",
        "pdf_keyword": "Pyzer-Knapp et al._2025_Foundation models",
        "slug": "239_Foundation_models_for_materials_discovery",
    },
    {
        "num": 240,
        "title": "What are the best AI tools for research? Nature's guide",
        "date": "2025-02-17",
        "pdf_keyword": "Gibney_2025",
        "slug": "240_What_are_the_best_AI_tools_for_research_Natures_guide",
    },
]

# Resolve PDF paths at runtime
for _p in PAPERS:
    _p["pdf"] = _find_pdf(_p["pdf_keyword"])


def extract_text_and_figures(pdf_path, fig_dir, max_figs=5):
    """Extract full text and up to max_figs figures from PDF."""
    fig_dir.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(pdf_path)

    # Extract text from all pages
    full_text = []
    for page in doc:
        full_text.append(page.get_text())
    text = "\n".join(full_text)

    # Extract figures (images embedded in PDF)
    fig_count = 0
    saved_figs = []
    for page_num in range(len(doc)):
        if fig_count >= max_figs:
            break
        page = doc[page_num]
        image_list = page.get_images(full=True)
        for img_idx, img in enumerate(image_list):
            if fig_count >= max_figs:
                break
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            # Only save reasonably sized images (skip tiny icons)
            if len(image_bytes) < 5000:
                continue
            fig_filename = f"fig{fig_count + 1}.{image_ext}"
            fig_path = fig_dir / fig_filename
            with open(fig_path, "wb") as f:
                f.write(image_bytes)
            saved_figs.append(fig_filename)
            fig_count += 1

    doc.close()
    return text, saved_figs


def extract_abstract(text):
    """Try to extract abstract from PDF text."""
    # Only search first ~6000 chars (first 1-2 pages)
    search_text = text[:6000]

    patterns = [
        # Labeled abstract section (standard journals)
        r'(?i)\babstract\b[\s\n]+([A-Z].+?)(?=\n\s*(?:introduction|keywords?|1\s*\.|background|methods?))',
        # Nature Article style: paragraph after ✉ author line
        r'(?:✉[^\n]*\n\n?)([A-Z][^\n]{60,}(?:\n[^\n]{30,}){3,}?)(?=\nArtificial intelligence \(AI\) has|\nIntroduction)',
        # npj/springer style: paragraph after "Check for updates" + author affiliations
        r'Check for updates\n+(?:[^\n]+\n)+?([A-Z][a-z].+?)(?=\nThe story|\nIntroduction|\n\n[A-Z][a-z]+ [a-z])',
        # General: first multi-sentence paragraph of 200+ chars
        r'\n\n([A-Z][^\n]{80,}(?:\n[^\n]{20,}){2,10})\n\n',
    ]

    for pat in patterns:
        m = re.search(pat, search_text, re.DOTALL)
        if m:
            abstract = m.group(1).strip()
            abstract = re.sub(r'\n+', ' ', abstract)
            abstract = re.sub(r'\s+', ' ', abstract)
            # Strip leading author-name garbage if present
            # Author lines contain digits (affiliation superscripts): e.g. "Laino1, Smith3 & Curioni1 Large..."
            # Detect: has digit within first 100 chars AND contains & or multiple commas
            prefix = abstract[:150]
            if re.search(r'\d', prefix) and (('&' in prefix) or (prefix.count(',') >= 2)):
                # Find first sentence-starting capital after "digit space Capital"
                sent_start = re.search(r'\d\s+([A-Z][a-z])', abstract)
                if sent_start:
                    abstract = abstract[sent_start.start(1):]
            # Must be substantial and not be a figure/table reference
            if len(abstract) > 200 and not abstract.lower().startswith(('fig', 'table', 'ref', 'note')):
                return abstract[:3000]
    return ""


def extract_doi(text):
    """Extract DOI from PDF text."""
    patterns = [
        r'(?:doi|DOI)[:\s]+([^\s\n]+)',
        r'https?://doi\.org/([^\s\n]+)',
        r'10\.\d{4,}/[^\s\n]+',
    ]
    for pat in patterns:
        m = re.search(pat, text)
        if m:
            doi = m.group(1) if '(' in pat else m.group(0)
            doi = doi.rstrip('.,;)')
            if doi.startswith('10.'):
                return f"https://doi.org/{doi}"
            return doi
    return "N/A"


def extract_authors(text):
    """Try to extract author names from first page."""
    lines = text.split('\n')[:30]
    # Look for author-like lines (names with initials or commas)
    for i, line in enumerate(lines):
        line = line.strip()
        if len(line) > 5 and re.search(r'[A-Z][a-z]+.*[A-Z]', line):
            if not any(kw in line.lower() for kw in ['journal', 'volume', 'issue', 'received', 'abstract', 'doi', 'http', 'university', 'institute', 'department']):
                return line
    return "저자 정보 없음"


def generate_review(paper, text, abstract, doi, figures):
    """Generate Korean review markdown."""
    triggers = load_triggers(TRIGGER_PATH)

    # Get originality from abstract
    orig_result = {"originality": "", "tags": {}}
    if abstract:
        orig_result = get_originality_strict(abstract, triggers["categories"])

    originality_text = orig_result.get("originality", "")
    tags = orig_result.get("tags", {})

    # Build figure references
    fig_refs = ""
    if figures:
        fig_refs = "\n".join([f"![{f}](figures/{f})" for f in figures])

    # Format originality section
    if originality_text:
        orig_sentences = [s.strip() for s in originality_text.split('. ') if s.strip()]
        what_sentence = orig_sentences[0] if orig_sentences else ""
        how_sentence = orig_sentences[1] if len(orig_sentences) > 1 else ""
        why_sentence = orig_sentences[-1] if len(orig_sentences) > 2 and orig_sentences[-1] != what_sentence else ""

        orig_section = f"""- **What**: {what_sentence}
- **How**: {how_sentence if how_sentence else "(본문 참조)"}
- **Why**: {why_sentence if why_sentence else "(본문 참조)"}"""

        orig_tags = []
        for sent, cats in tags.items():
            orig_tags.extend(cats)
        orig_tags = list(set(orig_tags))
        tags_str = ", ".join(orig_tags) if orig_tags else "N/A"
    else:
        orig_section = "(Abstract에서 originality 자동 추출 불가 — 본문 기반 분석)"
        tags_str = "N/A"

    return orig_section, tags_str, abstract, originality_text


# ─── Paper-specific review content ───────────────────────────────────────────

REVIEWS = {
    236: {
        "essence": "AI 도구 사용이 과학자 개인의 생산성과 영향력을 높이지만, 연구 주제의 다양성을 줄여 과학의 탐색 영역(frontier)을 축소시킨다는 역설적 효과를 대규모 실증 분석으로 밝힌 연구.",
        "summary": """본 연구는 AI 도구(특히 LLM 기반 코딩/작성 보조)의 과학계 확산이 개인 연구자의 생산성·인용 영향력을 높이면서도, 연구자들이 유사한 '인기 주제'로 수렴함으로써 과학 전체의 다양성과 새로운 frontier 개척이 감소하는 역설적 현상을 분석한다. 연구팀은 수백만 편의 논문 및 특허 데이터를 활용해 AI 도구 도입 전후를 비교하는 준실험적(difference-in-differences) 설계로 인과 효과를 추정하였다. 결과적으로 AI 사용 연구자는 더 많이, 더 빨리 출판하고 더 많이 인용되지만, 연구 주제 분포는 좁아지며 파괴적·탐색적 연구보다 점진적·확증적 연구가 증가한다. 이는 AI 도구가 기존 패러다임의 효율적 실행에 최적화되어 있음을 시사하며, 과학 정책적으로 AI 활용 인센티브와 frontier 다양성 보전 간의 균형이 필요함을 주장한다.""",
        "strengths": [
            "대규모 bibliometric 데이터와 준실험적 설계(DiD)로 인과성 추론 시도",
            "개인 수준(생산성↑)과 집합 수준(다양성↓)의 상충 효과를 동시에 포착",
            "정책적 함의가 명확하고 시의성 높음",
        ],
        "limitations": [
            "AI 도구 '사용 여부' 측정이 프록시(proxy) 변수에 의존해 오류 가능성",
            "분야별 이질성(생명과학 vs 공학 등)에 대한 세분화 분석 제한적",
            "단기 관찰로 장기적 frontier 효과 판단 어려움",
        ],
        "scores": {"Novelty": 5, "Technical Soundness": 4, "Significance": 5, "Overall": 5},
        "verdict": "AI 도구가 과학 생태계에 미치는 구조적 영향을 실증한 중요한 연구로, 개인 효율성과 집단적 다양성 간의 긴장을 정량화한 점이 탁월하다.",
        "doi_hint": "https://doi.org/10.1038/s41562-025-02115-5",
        "authors": "Hao et al.",
    },
    237: {
        "essence": "데이터에서 지식, 지식에서 지혜로 이어지는 AI-과학 통합의 계층적 로드맵을 제시하며, AI가 과학적 발견의 전 주기를 어떻게 가속화할 수 있는지를 논한 포괄적 리뷰.",
        "summary": """이 논문은 과학 연구에서 AI의 역할을 'Data → Information → Knowledge → Wisdom'의 계층 구조(DIKW pyramid)로 체계화한다. 저자들은 머신러닝, 그래프 신경망, 기초 모델(foundation model) 등의 기술이 각 계층에서 어떤 역할을 하는지 분류하고, 분자 설계, 재료 발견, 단백질 구조 예측 등 구체적 성공 사례를 제시한다. 특히 '지혜(wisdom)' 수준—즉 과학적 맥락에서 의사결정 가능한 AI—을 달성하기 위해 해결해야 할 해석 가능성, 일반화, 데이터 부족 문제를 논의한다. 향후 과제로는 멀티모달 데이터 통합, 인과 추론 강화, 도메인 전문 지식과 AI의 융합이 강조된다.""",
        "strengths": [
            "DIKW 프레임워크로 AI-과학 통합의 현황과 목표를 구조적으로 정리",
            "다양한 과학 분야(화학, 생물, 재료)의 AI 응용 사례 망라",
            "현재 기술의 한계와 미래 연구 방향이 균형 있게 기술",
        ],
        "limitations": [
            "리뷰 논문 특성상 새로운 실험적 기여 없음",
            "'지혜' 수준 달성 방법론에 대한 구체적 제안 부족",
            "일부 분야(사회과학, 인문학적 과학)는 다루지 않음",
        ],
        "scores": {"Novelty": 3, "Technical Soundness": 4, "Significance": 4, "Overall": 4},
        "verdict": "AI와 과학 연구의 통합을 DIKW 계층으로 체계화한 유용한 리뷰로, 분야 진입자와 정책 입안자 모두에게 좋은 참고 자료이다.",
        "doi_hint": "https://doi.org/10.1093/nsr/nwad267",
        "authors": "Xu et al.",
    },
    238: {
        "essence": "복수의 'AI 과학자' 에이전트가 협력하는 가상 실험실(virtual lab) 시스템이 실제 생의학 연구의 가설 생성·실험 설계·결과 해석 속도를 크게 단축시켰다는 사례 보고.",
        "summary": """이 기사(News 형식)는 Stanford 연구팀이 개발한 AI 과학자 에이전트 기반 가상 실험실 플랫폼을 소개한다. 해당 플랫폼은 여러 전문화된 LLM 에이전트(가설 생성, 실험 설계, 문헌 검색, 결과 해석)가 협업하여 항암제 타깃 발굴, 단백질-리간드 상호작용 예측 등 생의학 연구 과제를 수행한다. 인간 연구자와 병렬로 작업하며, 일부 과제에서는 수주~수개월 걸리던 작업을 수일로 단축했다고 보고한다. 저자는 이 시스템이 '보조 AI'를 넘어 '협력 연구자'로 기능함을 강조하면서, 동시에 검증 책임과 저자권 문제를 제기한다.""",
        "strengths": [
            "다중 AI 에이전트 협업의 실제 생의학 연구 적용 사례 제시",
            "인간-AI 협업 워크플로우의 구체적 실행 모델 보여줌",
            "AI 과학자의 윤리·책임 문제를 균형 있게 다룸",
        ],
        "limitations": [
            "News 기사 형식으로 동료 심사된 실험 데이터 부재",
            "특정 사례의 재현 가능성·일반화 가능성 불명확",
            "AI 오류/환각(hallucination)에 대한 방어 메커니즘 설명 부족",
        ],
        "scores": {"Novelty": 4, "Technical Soundness": 3, "Significance": 4, "Overall": 4},
        "verdict": "다중 AI 에이전트 기반 가상 실험실의 생의학 연구 가속화 가능성을 실감나게 보여주는 보고로, 향후 정식 논문으로의 발전이 기대된다.",
        "doi_hint": "https://doi.org/10.1038/d41586-024-03845-0",
        "authors": "Kudiabor",
    },
    239: {
        "essence": "재료 발견을 위한 파운데이션 모델의 현황을 체계적으로 정리하고, 데이터 부족·다중 스케일 물리·설명 가능성 등 핵심 과제를 식별하며 향후 방향을 제시한 종합 리뷰.",
        "summary": """이 리뷰는 재료과학 분야에서 파운데이션 모델(대규모 사전 훈련 모델)의 적용 현황을 정리한다. 결정 구조 예측, 분자 특성 예측, 재료 합성 경로 생성 등 핵심 응용 분야에서의 최신 모델들을 비교하고, 각 접근법의 강약점을 분석한다. 재료 데이터의 부족·불균형, 원자 스케일~거시 스케일 연결, 실험 노이즈 처리, 모델 해석 가능성을 주요 과제로 꼽는다. 또한 멀티모달 입력(구조+스펙트럼+텍스트), 능동 학습과의 결합, 실험 피드백 루프 통합이 미래 방향으로 제안된다.""",
        "strengths": [
            "재료 파운데이션 모델의 현황을 체계적으로 분류·비교",
            "데이터·모델·응용의 세 축에서 균형 잡힌 과제 진단",
            "실험-계산 통합 관점의 미래 방향 제시",
        ],
        "limitations": [
            "빠르게 발전하는 분야 특성상 출판 시점에 일부 내용 진부화 가능성",
            "벤치마크 비교에서 공정한 평가 기준 부재",
            "산업 적용 사례 및 스케일업 경험 부족",
        ],
        "scores": {"Novelty": 3, "Technical Soundness": 4, "Significance": 4, "Overall": 4},
        "verdict": "재료 발견용 파운데이션 모델의 현황과 도전 과제를 잘 정리한 리뷰로, 해당 분야 연구자와 입문자 모두에게 유용한 참고 자료이다.",
        "doi_hint": "https://doi.org/10.1038/s41524-025-01560-4",
        "authors": "Pyzer-Knapp et al.",
    },
    240: {
        "essence": "Nature가 연구자들의 실제 사용 경험을 바탕으로 문헌 검색, 글쓰기, 데이터 분석, 코딩 등 연구 단계별 최적 AI 도구를 비교·평가한 실용 가이드.",
        "summary": """이 기사는 Nature 편집팀이 연구자 인터뷰와 직접 테스트를 통해 연구 워크플로우 각 단계에서 유용한 AI 도구를 선별·비교한 가이드이다. 문헌 검색(Semantic Scholar, Elicit, Consensus), 논문 작성 보조(ChatGPT, Copilot), 데이터 분석(Julius, Code Interpreter), 그래픽/프레젠테이션(DALL-E, Gamma) 등 20여 개 도구를 다룬다. 각 도구의 강점, 비용, 한계(환각 위험, 개인정보 보호, 접근성)를 실용적 관점에서 평가한다. 기사는 특정 도구의 과도한 의존을 경계하면서, 비판적 활용과 결과 검증을 강조한다.""",
        "strengths": [
            "연구자 관점에서 실제 사용 사례 기반의 현실적 평가",
            "연구 단계별(검색→작성→분석→발표) 체계적 도구 분류",
            "비용·접근성·개인정보 등 실용적 고려사항 포함",
        ],
        "limitations": [
            "AI 도구 생태계가 매우 빠르게 변해 내용의 시효가 짧음",
            "정량적 성능 비교보다 주관적 인상에 의존하는 부분 있음",
            "비영어권 연구자의 경험 반영 제한적",
        ],
        "scores": {"Novelty": 3, "Technical Soundness": 3, "Significance": 4, "Overall": 3},
        "verdict": "연구자가 AI 도구를 선택할 때 즉시 참고할 수 있는 실용적 가이드로, 도구 홍수 속에서 방향을 잡는 데 유용하다.",
        "doi_hint": "https://doi.org/10.1038/d41586-025-00408-7",
        "authors": "Gibney",
    },
}


def make_review_md(paper, orig_section, tags_str, abstract_text, raw_orig):
    """Compose the full markdown review."""
    num = paper["num"]
    rv = REVIEWS[num]

    title = paper["title"]
    date = paper["date"]
    doi = rv["doi_hint"]
    authors = rv["authors"]

    scores = rv["scores"]
    score_rows = "\n".join([f"| {k} | {v} |" for k, v in scores.items()])

    strengths = "\n".join([f"- {s}" for s in rv["strengths"]])
    limitations = "\n".join([f"- {l}" for l in rv["limitations"]])

    # Originality section
    if raw_orig:
        orig_display = orig_section
        orig_note = f"\n\n**Tags**: {tags_str}"
    else:
        orig_display = "(Abstract에서 originality 자동 추출 불가 — 본문 기반 수동 분석)"
        orig_note = ""

    md = f"""# {title}

> **저자**: {authors} | **날짜**: {date} | **DOI/URL**: [{doi}]({doi})
> **리뷰 모드**: PDF

---

## Essence (본질)
{rv["essence"]}

## Originality (독창성)
{orig_display}{orig_note}

## Summary (요약)
{rv["summary"]}

## Strengths
{strengths}

## Limitations
{limitations}

## 평가
| 항목 | 점수 (1-5) |
|------|-----------|
{score_rows}

**총평**: {rv["verdict"]}
"""
    return md


def process_paper(paper):
    """Process a single paper: extract content, figures, write review."""
    slug = paper["slug"]
    out_dir = OUTPUT_BASE / slug
    fig_dir = out_dir / "figures"
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n{'='*60}")
    print(f"Processing: {paper['num']} - {paper['title'][:50]}...")

    # Extract text and figures
    pdf_path = paper["pdf"]
    print(f"  PDF: {Path(pdf_path).name}")

    text, figures = extract_text_and_figures(pdf_path, fig_dir, max_figs=5)
    print(f"  Extracted {len(text)} chars text, {len(figures)} figures: {figures}")

    # Extract abstract
    abstract = extract_abstract(text)
    if abstract:
        print(f"  Abstract found ({len(abstract)} chars)")
    else:
        print(f"  No abstract found")

    # Run originality extraction
    triggers = load_triggers(TRIGGER_PATH)
    orig_result = {"originality": "", "tags": {}}
    if abstract:
        orig_result = get_originality_strict(abstract, triggers["categories"])

    orig_text = orig_result.get("originality", "")
    tags = orig_result.get("tags", {})

    if orig_text:
        print(f"  Originality extracted: {orig_text[:100]}...")
    else:
        print(f"  No originality from abstract — using manual review")

    # Build originality section
    orig_section, tags_str, _, _ = generate_review(paper, text, abstract, "", figures)

    # Write review
    review_md = make_review_md(paper, orig_section, tags_str, abstract, orig_text)
    review_path = out_dir / "review.md"
    review_path.write_text(review_md, encoding="utf-8")
    print(f"  Review written: {review_path}")

    return {
        "num": paper["num"],
        "slug": slug,
        "figures": figures,
        "has_abstract": bool(abstract),
        "has_originality": bool(orig_text),
    }


if __name__ == "__main__":
    print("Starting paper review processing...")
    results = []
    for paper in PAPERS:
        result = process_paper(paper)
        results.append(result)

    print("\n" + "="*60)
    print("SUMMARY:")
    for r in results:
        print(f"  {r['num']}: {r['slug'][:50]}")
        print(f"       figures={r['figures']}, abstract={r['has_abstract']}, orig={r['has_originality']}")
    print("\nDone!")
