---
title: "812_TLDR_Extreme_Summarization_of_Scientific_Documents"
authors:
  - "Isabel Cachola"
  - "Kyle Lo"
  - "Arman Cohan"
  - "Daniel S. Weld"
date: "2020"
doi: "10.48550/ARXIV.2004.15011"
arxiv: ""
score: 4.5
essence: "본 논문은 과학 논문을 위한 극단적 요약(extreme summarization) 작업인 TLDR 생성을 소개하고, 이를 위한 5.4K 규모의 멀티-타겟 데이터셋 SciTLDR과 제목을 보조 신호로 활용하는 CATTS 학습 전략을 제시한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Scientific_Literature_Summarization"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Cachola et al._2020_TLDR Extreme Summarization of Scientific Documents.pdf"
---

# TLDR: Extreme Summarization of Scientific Documents

> **저자**: Isabel Cachola, Kyle Lo, Arman Cohan, Daniel S. Weld | **날짜**: 2020 | **DOI**: [10.48550/ARXIV.2004.15011](https://doi.org/10.48550/ARXIV.2004.15011)

---

## Essence

![Figure 1](figures/fig1.webp)
*과학 논문의 TLDR 예시. TLDR은 일반적으로 논문의 초록, 서론, 결론 섹션에서 발견되는 두드러진 정보로 구성됨*

본 논문은 과학 논문을 위한 극단적 요약(extreme summarization) 작업인 TLDR 생성을 소개하고, 이를 위한 5.4K 규모의 멀티-타겟 데이터셋 SciTLDR과 제목을 보조 신호로 활용하는 CATTS 학습 전략을 제시한다.

## Motivation

- **Known**: 기존의 과학 논문 요약 연구는 초록(abstract) 생성이나 초록의 보완 요약에 초점을 맞춤. 논문 출판 속도가 가파르게 증가하면서 학자들이 관련 논문을 따라잡기 어려워지고 있음.

- **Gap**: 한 문장의 극단적 요약인 TLDR 생성 작업은 아직 다루어지지 않음. 과학 논문의 TLDR 생성은 높은 압축률(compression ratio), 전문가 배경 지식, 복잡한 도메인 특화 언어 이해가 필요함.

- **Why**: TLDR은 독자가 논문의 핵심 내용을 빠르게 파악하고 읽을 가치가 있는지 판단하도록 도울 수 있음. 다중 목표 요약(multi-target summary)은 자동 평가 메트릭의 신뢰성을 향상시킴.

- **Approach**: 저자 작성 TLDR과 전문가 파생 TLDR의 두 가지 유형을 포함하는 멀티-타겟 데이터셋 구성. 제목을 보조 학습 신호로 활용하는 CATTS 학습 전략 제안.

## Achievement

![Figure 2](figures/fig2.webp)
*동료 평가 의견을 TLDR로 다시 쓴 예시. 피어 리뷰 의견의 첫 부분을 활용하여 주석 자들이 TLDR을 작성*

1. **SciTLDR 데이터셋**: 3,229개의 컴퓨터 과학 논문에 대한 5,411개의 TLDR로 구성. 학습셋(1,992개), 개발셋(619개), 테스트셋(618개) 구성. 기존 요약 데이터셋과 달리 다중 목표 요약 포함.

2. **CATTS 학습 전략**: 제목을 보조 신호로 활용하여 제어 코드(control code)를 통해 제목과 TLDR을 동시에 생성하도록 훈련. BART 모델에 적용 시 자동 메트릭과 인간 평가 모두에서 개선 달성.

3. **데이터셋 특성 분석**: 압축률 238.1배 (기존 scientific 데이터셋 14.9-36.5배), 새로운 단어 비율 15.2% (기존 7.4-10.5%)로 높은 수준의 추상화(abstractiveness) 요구.

## How

- **데이터 수집**: OpenReview 플랫폼에서 저자 작성 TLDR 자동 수집. 동료 평가(peer review) 의견의 초반 128단어를 전문가가 TLDR로 재작성하는 혁신적 주석 방식 도입.

- **주석 프로토콜**: 컴퓨터 과학 전공 대학생 28명을 모집하여 1시간의 집중 교육 후 작업. TLDR 길이를 15-25단어로 제한하고 원본 표현 보존 지향. 모든 요약을 수동 검증하여 품질 관리.

- **CATTS 방법론**: 멀티태스크 학습의 스캐폴딩(scaffolding) 아이디어와 조건부 언어 생성의 제어 코드 결합. 제목 생성을 보조 작업으로 활용하여 제한된 데이터에서 모델의 추상화 능력 강화.

- **정보 내용 분석**: 두 명의 연구자가 TLDR에서 발견되는 정보를 6가지 범주(주제 영역, 동기, 방법론, 결과, 기여, 제한사항)로 분류하는 너겟(nugget) 기반 분석 수행.

## Originality

- **새로운 작업 정의**: TLDR 생성이라는 극단적 요약 작업을 과학 논문 도메인에서 처음으로 제시.

- **혁신적 주석 방식**: 피어 리뷰 의견을 활용하여 전체 논문을 읽지 않고도 고품질 요약을 생성하는 효율적인 주석 프로토콜 제안.

- **멀티-타겟 데이터셋**: 대부분의 요약 데이터셋이 단일 목표 요약만 포함하는 반면, 동일 논문에 대해 여러 개의 정답 TLDR 제공.

- **CATTS 학습 전략**: 제목을 자연 발생적 보조 신호로 활용하는 간단하면서도 효과적인 학습 전략 제안.

## Limitation & Further Study

- **데이터셋 규모**: 자동 수집 데이터셋(XSUM, ArXiv)에 비해 3.2K 논문의 상대적으로 작은 규모. 다른 과학 도메인(생의학, 화학 등)으로의 확장 가능성.

- **모델 복잡도**: 제시된 방법이 BART 같은 대규모 사전 학습 모델에 의존. 자원 제약이 있는 환경에서의 적용 가능성 검토 필요.

- **평가 메트릭**: ROUGE 같은 자동 메트릭의 한계 인식. 인간 평가의 광범위한 확대와 사실적 정확성(factual correctness) 평가 강화 필요.

- **도메인 적응**: 컴퓨터 과학 분야에 한정된 데이터셋. 다른 과학 분야에서의 TLDR 특성과 학습 전략의 일반화 가능성 탐색.

## Evaluation

- **Novelty**: 4.5/5
  - TLDR 생성이라는 새로운 작업 정의와 혁신적 주석 프로토콜은 독창적이나, 멀티태스크 학습 자체는 기존 기법

- **Technical Soundness**: 4/5
  - 명확한 방법론과 체계적인 데이터셋 구성. 다만 CATTS의 기술적 복잡도는 제한적

- **Significance**: 4.5/5
  - 급증하는 논문 출판에 대응하는 실용적 해결책 제시. 멀티-타겟 데이터셋의 평가 신뢰성 향상 기여도 높음

- **Clarity**: 4.5/5
  - 전체적으로 명확한 구성과 설명. 다양한 예시 제공으로 이해 용이

- **Overall**: 4.5/5

**총평**: 본 논문은 과학 논문의 극단적 요약이라는 현실적 필요성을 반영하여 새로운 작업과 고품질 멀티-타겟 데이터셋을 제시했으며, 혁신적 주석 프로토콜과 효과적인 학습 전략으로 자연어 처리 커뮤니티에 실질적 기여를 하였다.

## Related Papers

- 🔗 후속 연구: [[papers/593_Openscholar_Synthesizing_scientific_literature_with_retrieva/review]] — 과학 논문의 극단적 요약에서 전체 과학 문헌의 종합적 검색과 합성으로 확장한 더 포괄적인 연구입니다.
- 🔄 다른 접근: [[papers/885_Withdrarxiv_A_large-scale_dataset_for_retraction_study/review]] — 과학 논문의 요약 생성과 철회 논문의 분류라는 서로 다른 과학 문헌 처리 접근법을 제시합니다.
- 🔗 후속 연구: [[papers/732_Scireviewgen_a_large-scale_dataset_for_automatic_literature/review]] — 단일 논문 요약에서 다중 논문을 활용한 자동 문헌 리뷰 생성으로 확장한 발전된 형태의 연구입니다.
- 🏛 기반 연구: [[papers/907_Is_AI_ready_to_mass-produce_lay_summaries_of_research_articl/review]] — 과학 문서의 극단적 요약 기법이 일반 독자용 간략 요약 생성의 기술적 기반을 제공한다.
- 🏛 기반 연구: [[papers/593_Openscholar_Synthesizing_scientific_literature_with_retrieva/review]] — 과학 논문 극단적 요약 연구가 대규모 문헌 검색 합성 시스템의 요약 생성 모듈 개발에 기초 기술을 제공합니다.
- 🔄 다른 접근: [[papers/885_Withdrarxiv_A_large-scale_dataset_for_retraction_study/review]] — 과학 논문의 생산적 요약 생성과 문제가 있는 논문의 철회 분석이라는 서로 다른 과학 문헌 처리 관점을 제시합니다.
- 🔗 후속 연구: [[papers/561_Ms2_Multi-document_summarization_of_medical_studies/review]] — 의료 연구의 다중문서 요약을 과학 문서의 극단적 요약으로 확장하여 더 간결한 정보 압축 방법을 탐구함
- 🔄 다른 접근: [[papers/108_Ask_retrieve_summarize_A_modular_pipeline_for_scientific_lit/review]] — 과학 문서의 극단적 요약 방법으로 본 논문의 다중문서 요약과 다른 접근법을 제시한다.
- 🧪 응용 사례: [[papers/401_Hierarchical_attention_graph_for_scientific_document_summari/review]] — 과학 문서의 극한 요약에 계층적 관계 모델링을 적용하여 더 정확한 요약을 생성할 수 있습니다.
- 🧪 응용 사례: [[papers/913_Semantic_Scholar/review]] — 대규모 과학 문서 요약을 위한 구체적 적용 사례를 제시한다
