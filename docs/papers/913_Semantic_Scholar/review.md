---
title: "913_Semantic_Scholar"
authors:
  - "Kyle Lo"
  - "Lucy Lu Wang"
  - "Mark E Neumann"
  - "Rodney Kinney"
  - "Daniel S. Weld"
date: ""
doi: "N/A"
arxiv: ""
score: 4.0
essence: "S2ORC는 81.1M개의 영문 학술논문을 수집하고 8.1M개 오픈액세스 논문의 구조화된 전문(full text)을 제공하는 대규모 공개 코퍼스로, 인용(citation), 도표(figure), 표(table) 등이 자동으로 주석 처리되어 있다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Scientific_Question_Answering"
  - "topic/ai4s"
---

# Semantic Scholar

> **저자**: Kyle Lo, Lucy Lu Wang, Mark E Neumann, Rodney Kinney, Daniel S. Weld | **날짜**:  | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: Inline citations and references to ﬁgures and*

S2ORC는 81.1M개의 영문 학술논문을 수집하고 8.1M개 오픈액세스 논문의 구조화된 전문(full text)을 제공하는 대규모 공개 코퍼스로, 인용(citation), 도표(figure), 표(table) 등이 자동으로 주석 처리되어 있다.

## Motivation

- **Known**: 기존에는 arXiv, PubMed Central, CiteSeerX 등 여러 학술 디지털 아카이브와 인용 그래프(citation graph) 자원들이 있었으나, 대부분 도메인 특화적이거나 구조화된 전문 텍스트가 부족했다.
- **Gap**: 기존 코퍼스들은 논문 수가 제한적이거나 특정 분야에만 집중되어 있으며, 기계가독 가능한 구조화 전문 텍스트와 풍부한 메타데이터를 함께 제공하는 대규모 통합 자원이 부재했다.
- **Why**: 학술 논문은 NLP 연구를 위한 중요한 텍스트 도메인이며, 인용 관계, 참고문헌, 도표 등의 풍부한 구조를 활용한 텍스트 마이닝, 요약, 정보 추출 등 다양한 NLP 작업을 가능하게 하기 때문이다.
- **Approach**: Semantic Scholar 문헌 코퍼스를 기반으로 다수의 출판사와 디지털 아카이브에서 데이터를 수집하고, ScienceParse와 GROBID를 활용하여 PDF를 처리하며, arXiv의 LaTeX 소스를 직접 파싱하여 구조화된 전문을 추출하고, 메타데이터 선택 및 참고문헌 링크 해석을 수행했다.

## Achievement

![Figure 1](figures/fig1.webp)

*Figure 1: Inline citations and references to ﬁgures and*

- **대규모 통합 자원**: 81.1M개 논문(메타데이터, 초록)과 8.1M개 오픈액세스 논문의 구조화된 전문을 포함하는 가장 큰 공개 학술 텍스트 컬렉션 구축
- **풍부한 주석 정보**: 인라인 인용, 도표/표 참조가 자동 감지되고 링크되며, 1.5M개 LaTeX 파싱 논문은 수식과 표 내용까지 추출
- **학제간 광범위성**: 물리학, 수학, 컴퓨터과학, 의학 등 수십 개 학문 분야를 포괄하여 기존 도메인 특화 코퍼스보다 우수한 다양성 확보
- **고품질 구조 보존**: 단락 구분, 섹션 헤더, 참고문헌 해석 등 의미 있는 문서 구조를 유지하여 기계 가독성 향상

## How


- Semantic Scholar 문헌 그래프의 약 200M개 초기 논문 클러스터에서 출발
- ScienceParse v3.0.0으로 제목/저자 추출, GROBID v0.5.5로 PDF 처리하여 메타데이터, 본문, 캡션, 인라인 인용, 참고문헌 추출
- 비학술 문서(논문집, 보고서, 슬라이드 등) 필터링으로 처리 품질 향상
- GROBID 후처리: 정규표현식으로 거짓양성(수식 참조 오인) 제거, 인용 범위 확장(예: [3]-[5] → [3], [4], [5])
- arXiv LaTeX 소스를 XML로 변환하여 1.5M개 논문의 구조 정보(수식, 표 내용 등) 추출
- 메타데이터 품질 기준에 따른 필터링 및 각 논문 클러스터별 최적 메타데이터 선택
- 코퍼스 내 논문 클러스터 간 참고문헌 링크 해석으로 인용 그래프 형성

## Originality

- **최초의 대규모 통합 구조화 학술 코퍼스**: 여러 출판사와 아카이브 데이터를 통합하고 구조화된 전문을 대규모로 제공한 첫 공개 자원
- **이중 처리 파이프라인**: PDF와 LaTeX 소스를 동시에 처리하여 상호 보완적 장점 활용 (PDF 메타데이터 vs LaTeX 구조 정확도)
- **정교한 후처리 자동화**: 정규표현식 기반 GROBID 오류 수정(거짓양성 제거, 인용 범위 확장) 등 자동화된 품질 개선 방법론
- **풍부한 구조 주석**: 단순 인용 외에도 도표/표 참조, 수식, 섹션 구조를 링크된 형태로 주석 처리하여 다양한 NLP 작업 지원

## Limitation & Further Study

- **메타데이터 품질 불일치**: LaTeX 소스의 메타데이터 품질이 PDF보다 낮아 클러스터링에 미사용 (논문 통합 효율성 감소 가능)
- **처리 도구 제약**: ScienceParse와 GROBID의 능력 한계로 인한 오류 발생 (거짓양성/음성 완전 제거 불가)
- **오픈액세스 편향**: 8.1M개 구조화 전문은 오픈액세스 논문 중심이라 출판 모델별 편향 존재 가능
- **후속 연구 방향**: (1) 더 정교한 PDF 파싱 기술 개발로 메타데이터 추출 오류 감소, (2) 기계학습 기반 인용 오류 수정 자동화, (3) 비영문 논문 확대, (4) 도메인별 특화 전문(domain-specific full text) 추출 고도화

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: S2ORC는 학술 NLP 연구를 위한 기초 자원으로서 기존 대비 3배 이상의 구조화 전문을 제공하고, 풍부한 주석 정보와 학제간 광범위성으로 획기적인 공개 코퍼스이다. 실제 적용 가능성이 매우 높으며, 후속 학술 텍스트 마이닝 연구의 토대가 될 것으로 예상된다.

## Related Papers

- 🔄 다른 접근: [[papers/580_Oag-bench_A_human-curated_benchmark_for_academic_graph_minin/review]] — 학술 그래프 마이닝을 위한 다른 접근법과 벤치마크를 제공한다
- 🔗 후속 연구: [[papers/087_Ai2_scholar_qa_Organized_literature_synthesis_with_attributi/review]] — 조직화된 문헌 합성을 위해 S2ORC 데이터를 활용한 확장 연구이다
- 🧪 응용 사례: [[papers/812_TLDR_Extreme_Summarization_of_Scientific_Documents/review]] — 대규모 과학 문서 요약을 위한 구체적 적용 사례를 제시한다
- 🏛 기반 연구: [[papers/386_Google_Scholar_to_overshadow_them_all_Comparing_the_sizes_of/review]] — Semantic Scholar를 포함한 학술 검색 시스템의 기반 연구로 규모 비교 분석의 기준점을 제공한다.
