---
title: "021_A_Review_on_Scientific_Knowledge_Extraction_using_Large_Lang"
authors:
  - "Gabriel Lino Garcia"
  - "João Renato Ribeiro Manesco"
  - "P. H. Paiola"
  - "Lucas Miranda"
  - "Maria Paola de Salvo"
date: "2024"
doi: "10.48550/arXiv.2412.03531"
arxiv: ""
score: 3.0
essence: "본 논문은 의료 과학 분야에서 대규모 언어모델(LLM)을 활용한 과학적 지식 추출 및 증거 합성(evidence synthesis)의 현황을 체계적으로 검토한다. LLM의 의료 문헌 자동화 처리 잠재력과 함께 hallucination, 맥락 이해, 일반화 능력 등의 주요 과제를 분석한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/AI_in_Scientific_Research"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Garcia et al._2024_A Review on Scientific Knowledge Extraction using Large Language Models in Biomedical Sciences.pdf"
---

# A Review on Scientific Knowledge Extraction using Large Language Models in Biomedical Sciences

> **저자**: Gabriel Lino Garcia, João Renato Ribeiro Manesco, P. H. Paiola, Lucas Miranda, Maria Paola de Salvo | **날짜**: 2024 | **DOI**: [10.48550/arXiv.2412.03531](https://doi.org/10.48550/arXiv.2412.03531)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: Illustration of the screening process, conducted in*

본 논문은 의료 과학 분야에서 대규모 언어모델(LLM)을 활용한 과학적 지식 추출 및 증거 합성(evidence synthesis)의 현황을 체계적으로 검토한다. LLM의 의료 문헌 자동화 처리 잠재력과 함께 hallucination, 맥락 이해, 일반화 능력 등의 주요 과제를 분석한다.

## Motivation

- **Known**: 체계적 문헌고찰(systematic review)은 의료 분야에서 증거 합성의 표준 방법으로 인정되어 왔으나, 기하급수적으로 증가하는 과학 출판물로 인해 접근성과 처리 속도의 문제가 지속되고 있다. 최근 LLM 기술 발전이 이러한 자동화 과제 해결의 가능성을 보여주고 있다.
- **Gap**: 현재 LLM 기반 의료 증거 합성 연구에서 표준화된 벤치마크(unified benchmark)의 부재, 다양한 의료 작업 간 성능 비교의 어려움, 그리고 실무 적용 가능성 검증의 미흡이 주요 연구 공백으로 남아있다.
- **Why**: 의료 분야에서 방대한 과학 문헌 속의 중요한 발견이 묻혀 있어 환자 치료 결과 개선과 의료 과학 발전을 저해하고 있으며, LLM 기반 자동화는 의료 전문가와 비전문가 모두에게 접근 가능한 증거 기반 의사결정 지원 체계를 제공할 수 있다.
- **Approach**: PRISMA 지침을 준수하여 5년간 발표된 ACM, IEEE, Scopus 등 다중 학술 데이터베이스를 검색하고, ChatGPT-4를 활용한 자동 요약과 수동 검증을 결합한 이중 스크리닝 방식으로 14개 핵심 연구를 선정하여 분석했다.

## Achievement

![Figure 1](figures/fig1.webp)

*Figure 1: Illustration of the screening process, conducted in*

- **의료 증거 합성을 위한 LLM 성능 평가**: 현재 사용되는 주요 LLM 모델들의 임상 의사결정 지원 및 지식 추출 작업에서의 성능 비교 분석 제시
- **핵심 제약 요인 식별**: hallucination(환각), 맥락 이해 부족, 확장성 문제 등 LLM의 의료 응용에서 해결해야 할 구체적인 기술 한계 규명
- **표준화 벤치마크 필요성 제기**: 의료 LLM 평가의 신뢰성과 재현성을 위한 통일된 평가 지표 개발의 필수성 강조
- **미래 연구 방향 제시**: Retrieval-Augmented Generation(RAG) 등 최첨단 기법의 통합을 통한 LLM 성능 향상 경로 제안

## How

![Figure 1](figures/fig1.webp)

*Figure 1: Illustration of the screening process, conducted in*

- PRISMA(Preferred Reporting Items for Systematic Reviews and Meta-Analyses) 프로토콜 준수를 통한 체계적 검토 수행
- ACM Digital Library, IEEE Xplore, Scopus, SOLO(arXiv), ScienceDirect 등 6개 주요 학술 데이터베이스 통합 검색
- ChatGPT-4 LLM을 활용한 대규모 문헌 자동 요약 및 분류로 검토 효율성 증대
- 자동화 결과에 대한 수동 검증 과정으로 분석 품질 보증
- 각 포함된 연구에 대해 LLM 모델 유형, 의료 작업 적용 영역, 성능 결과, 직면 과제 등 구조화된 데이터 추출
- 생물의학 분야별 LLM 성능 효율성 비교 및 다른 지식 추출 기법과의 상대 평가

## Originality

- 의료 증거 합성 분야에 특화된 LLM 응용에 대한 포괄적 체계적 고찰로, 기존 개별 응용 연구와 구별되는 메타-분석적 관점 제공
- LLM을 평가 도구로 활용하는 동시에 피평가 대상으로 삼는 이중적 접근 방식(ChatGPT-4를 활용한 자동 요약)으로 LLM의 역할 다양화
- 일반적 지식 추출을 넘어 '증거 합성' 특화 관점으로 의료 의사결정 프로세스와의 연계성 강화", 'RAG(Retrieval-Augmented Generation) 등 특정 기술 통합의 구체적 제안으로 LLM 성능 개선의 실행 가능한 방향 제시

## Limitation & Further Study

- **제한된 포함 연구**: 최종 651개 중 14개 연구만 포함되어 검토 범위의 선택성 가능성
- **시간 제한**: 과거 5년 데이터에 제한되어 최신 모델(예: GPT-4 Turbo, Claude 등)의 성능 미포함 가능
- **영어 편향**: 영어 발표 논문만 포함으로 비영어권 중요 연구 누락 위험
- **정량적 비교 부족**: 다양한 평가 지표 사용으로 모델 간 직접 성능 비교의 어려움
- **후속 연구 방향**: (1) 의료 도메인별 세부 벤치마크 개발 (예: 진단, 치료, 약물 상호작용), (2) LLM과 기존 NLP 기법의 하이브리드 모델 개발, (3) 임상 환경 실제 도입 성과 연구, (4) 다국어 LLM의 의료 응용 성능 비교

## Evaluation

- Novelty: 3/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 3/5

**총평**: 본 논문은 의료 분야 LLM 응용의 현황을 체계적으로 정리한 의미 있는 종설이나, 최종 포함 연구 수의 제한성과 기술적 심화 분석 부족이 제약이다. 향후 표준화된 평가 체계 구축과 실제 임상 적용 연구로의 발전이 필요하다.

## Related Papers

- 🏛 기반 연구: [[papers/530_Medbiolm_Optimizing_medical_and_biological_qa_with_fine-tune/review]] — 의료 과학 분야 LLM 활용의 체계적 검토가 특화된 의료 QA 모델 개발의 배경을 제공한다
- 🧪 응용 사례: [[papers/897_Can_AI_review_the_scientific_literature__and_figure_out_what/review]] — 의료 분야에서 LLM 기반 문헌 검토의 구체적 적용 가능성과 한계를 다룬다
- 🔗 후속 연구: [[papers/087_Ai2_scholar_qa_Organized_literature_synthesis_with_attributi/review]] — 의료 과학 지식 추출을 조직화된 문헌 합성으로 확장한 연구이다
- 🧪 응용 사례: [[papers/530_Medbiolm_Optimizing_medical_and_biological_qa_with_fine-tune/review]] — 의료 과학 분야 LLM 지식 추출의 체계적 검토를 구체적 QA 시스템으로 구현한다
