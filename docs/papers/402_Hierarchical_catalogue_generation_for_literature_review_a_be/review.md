---
title: "402_Hierarchical_catalogue_generation_for_literature_review_a_be"
authors:
  - "Kun Zhu"
  - "Xiaocheng Feng"
  - "Xiachong Feng"
  - "Yingsheng Wu"
  - "Bing Qin"
date: "2023"
doi: "N/A"
arxiv: ""
score: 4.0
essence: "본 논문은 과학 문헌 리뷰 자동 생성 과정에서 계층적 카탈로그(목차)의 중요성을 강조하고, 참고 논문들을 입력받아 리뷰 논문의 계층적 카탈로그를 생성하는 새로운 과제(HiCatGLR)를 제안한다. 7.6k개의 리뷰 카탈로그와 389k개의 참고 논문으로 구성된 벤치마크 데이터셋을 구축하고, 구조적 특성을 반영한 평가 지표를 설계하여 다양한 최신 모델의 성능을 평가한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Hierarchical_Knowledge_Graphs"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhu et al._2023_Hierarchical catalogue generation for literature review a benchmark.pdf"
---

# Hierarchical catalogue generation for literature review: a benchmark

> **저자**: Kun Zhu, Xiaocheng Feng, Xiachong Feng, Yingsheng Wu, Bing Qin | **날짜**: 2023 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: gpt-3.5-turbo로 생성한 과학 문헌 리뷰의 예시. (A) 직접 생성 시 중복 콘텐츠와 논리적 혼란 발생, (B) 오라클 카탈로그 사용 시 체계적 생성, (C) 생성된 카탈로그 사용 시 품질 저하 문제*

본 논문은 과학 문헌 리뷰 자동 생성 과정에서 계층적 카탈로그(목차)의 중요성을 강조하고, 참고 논문들을 입력받아 리뷰 논문의 계층적 카탈로그를 생성하는 새로운 과제(HiCatGLR)를 제안한다. 7.6k개의 리뷰 카탈로그와 389k개의 참고 논문으로 구성된 벤치마크 데이터셋을 구축하고, 구조적 특성을 반영한 평가 지표를 설계하여 다양한 최신 모델의 성능을 평가한다.

## Motivation

- **Known**: 기존 문헌 리뷰 생성 연구는 인용 문장 생성(citation sentence generation)이나 관련 연구 요약(related work generation) 같은 단편적 과제에 집중했으며, 최근 대규모 언어 모델(LLM)도 직접 리뷰를 생성할 때 체계적 구조 없이 무질서하게 생성한다.

- **Gap**: 장황한 리뷰 콘텐츠에서 중복, 논리적 혼란, 부실한 조직화 문제 발생. 계층적 카탈로그 생성이라는 중간 단계가 부재하여 최종 리뷰 품질이 저하된다.

- **Why**: 계층적 지도(hierarchical guidance)가 텍스트 생성에 효과적이라는 기존 연구를 근거로, 카탈로그는 저자의 지식 구조와 논리적 이해를 반영하므로 리뷰 생성의 첫 단계로 활용하면 개선 효과를 기대할 수 있다.

- **Approach**: 리뷰 생성을 두 단계로 분리 → (1) 계층적 카탈로그 생성, (2) 각 섹션별 콘텐츠 생성. 이를 위해 새로운 과제 정의, 대규모 데이터셋 구축, 구조 인식 평가 지표 설계가 필요하다.

## Achievement

1. **새로운 과제 및 데이터셋**: HiCatGLR(Hierarchical Catalogue Generation for Literature Review) 과제 정의 및 HiCaD 데이터셋 구축
   - 7,600개의 리뷰 논문-카탈로그 쌍
   - 총 389,000개의 참고 논문 초록
   - 평균 81.1개의 참고 논문/리뷰, 평균 입력 길이 21,548 토큰

2. **구조 인식 평가 지표**: 기존 BLEU/ROUGE 지표의 한계를 극복한 두 가지 새로운 메트릭
   - **CEDS (Catalogue Edit Distance Similarity)**: 기준 카탈로그와의 구조적/의미적 유사도 측정
   - **CQE (Catalogue Quality Estimate)**: 카탈로그 표준화 정도를 템플릿 단어 빈도로 평가

3. **포괄적 벤치마크**: BART, T5 등 최신 요약 모델과 ChatGPT 포함 다양한 모델 평가
   - End-to-end 생성과 단계별 생성 두 가지 접근법 비교
   - Fine-tuned와 zero-shot 설정 모두 검토

## How

![Figure 2](figures/fig2.webp)
*그림 2: 데이터셋의 통계적 특성 및 카탈로그 구조 분포*

- **데이터 수집**: arXiv와 Semantics Scholar에서 제목에 "survey" 또는 "review" 포함 논문 수집 → 11,435개 선별, HTML 형식 확보 가능한 8,397개 최종 선정

- **카탈로그 추출**: PDF에서의 구조 정보 손실 문제를 해결하기 위해 ar5iv(LaTeX→HTML 변환 서비스)에서 HTML 파일 획득 → 정규식을 이용해 제목 계층 레벨을 `<L1>, <L2>, <L3>` 태그로 변환

- **입력 처리**: 참고 논문 목록에서 제목과 초록이 모두 존재하는 유효한 논문만 선별, 각 초록을 최대 256 단어로 제한

- **출력 정의**: 3단계 계층 구조로 제한 (L1: 주 섹션, L2: 부분 섹션, L3: 세부 항목)

- **평가 메트릭 설계**:
  - CEDS: Tree edit distance 기반으로 삽입/삭제/대체/이동 비용 계산
  - CQE: 기준 카탈로그에서 추출한 템플릿 단어(the, a, of 등)의 재현율로 표준화 정도 측정

![Figure 3](figures/fig3.webp)
*그림 3: 단계별 생성(step-by-step) 접근법의 아키텍처*

- **모델 구조**: 
  - End-to-end: 제목 + 모든 참고 논문 초록 → 전체 카탈로그 직접 생성
  - Step-by-step: 먼저 상위 레벨 섹션 생성 → 각 섹션에 대한 하위 레벨 항목 순차 생성

## Originality

- **처음으로 문헌 리뷰 생성을 중간 표현(intermediate representation)인 계층적 카탈로그 생성과 콘텐츠 생성의 두 단계로 명시적으로 분해한 과제 제안**

- **구조화된 텍스트(트리 구조)의 특성을 반영한 평가 지표 설계**: 기존 시퀀스 평가 지표의 한계를 극복하고 계층적 편집 거리(hierarchical edit distance)와 템플릿 기반 품질 평가를 결합

- **대규모 고품질 벤치마크 데이터셋 구축**: HTML 파싱을 통해 구조 정보 손실 문제를 해결하고, 수작업 검증을 통해 데이터 신뢰성 확보

- **다양한 생성 전략 비교**: End-to-end와 단계별 생성의 성능 차이를 체계적으로 분석하여 각 접근법의 장단점 도출

## Limitation & Further Study

- **입력 길이 제약**: 평균 21,548 토큰의 매우 긴 입력을 처리해야 하는데, 현재 모델의 컨텍스트 윈도우 한계로 인해 모든 참고 논문 정보를 온전히 활용하기 어려움. 향후 긴 문맥 처리 기술 개선 필요.

- **3단계 계층 제한**: 실제 리뷰 논문은 더 깊은 계층 구조를 가질 수 있으나, 계산 복잡성과 데이터 희소성으로 인해 3단계로 제한. 더 깊은 계층 구조 처리 방법 모색 필요.

- **LLM의 낮은 성능**: ChatGPT 등 최신 LLM도 이 과제에서 만족스러운 성능을 보이지 못하며, fine-tuned 모델들도 개선 여지가 큼. 도메인 특화 사전학습이나 검색 증강 생성(RAG) 기법 적용 필요.

- **카탈로그와 콘텐츠 연계**: 생성된 카탈로그가 실제 리뷰 콘텐츠 생성 품질에 미치는 영향을 정량적으로 측정하는 후속 실험 필요.

- **평가 지표의 상관성**: CEDS와 CQE가 실제 사람의 평가와 얼마나 일치하는지 확인하는 인간 평가 비교 연구 필요.

## Evaluation

- **Novelty**: 4.5/5
  - 문헌 리뷰 생성을 카탈로그 생성과 분리한 것은 창의적이며, 계층적 구조에 특화된 평가 지표는 차별성이 있음. 다만 계층적 텍스트 생성 자체는 기존 연구에서 다루어진 영역.

- **Technical Soundness**: 4/5
  - 데이터셋 구축 방법론이 합리적이고, 평가 지표 설계가 논리적. 다만 컨텍스트 길이 제약으로 인한 입력 처리 전략이 명확하지 않음. 단계별 생성 접근법의 이론적 근거가 충분하지 않음.

- **Significance**: 4/5
  - 논문 리뷰 자동 생성이라는 중요한 실제 문제를 다루며, 새로운 과제와 벤치마크를 제시한 것이 후속 연구에 기여할 수 있음. 그러나 현 단계에서는 카탈로그 생성만 다루므로 최종 리뷰 품질 개선 효과를 직접 입증하지 못함.

- **Clarity**: 4/5
  - 동기 부여와 문제 정의가 명확하고, 도형(Figure 1)을 통한 시각적 설명이 효과적. 데이터셋 구축 절차와 평가 지표 설명이 이해하기 좋음. 일부 기술적 세부사항(CEDS 계산)의 수식 표현이 더 정교할 수 있음.

- **Overall**: 4/5

**총평**: 본 논문은 문헌 리뷰 생성의 첫 단계로 계층적 카탈로그 생성을 명시적으로 제안하고 대규모 벤치마크 데이터셋과 새로운 평가 지표를 제시한 가치 있는 연구다. 구조화된 텍스트 생성에 대한 새로운 관점과 도메인 맞춤형 평가 방식이 돋보이나, 현재 모델들의 낮은 성능과 카탈로그-콘텐츠 통합의 부재가 실제 영향력을 제한한다.

## Related Papers

- 🔗 후속 연구: [[papers/732_Scireviewgen_a_large-scale_dataset_for_automatic_literature/review]] — 문헌 리뷰 자동 생성에서 단순한 데이터셋을 계층적 카탈로그 구조로 확장한 고도화된 접근법입니다.
- 🏛 기반 연구: [[papers/563_Multi-document_scientific_summarization_from_a_knowledge_gra/review]] — 다중 문서 요약의 지식 그래프 활용이 계층적 카탈로그 생성의 구조적 기반을 제공합니다.
- 🔄 다른 접근: [[papers/450_Knowledge_navigator_Llm-guided_browsing_framework_for_explor/review]] — 문헌 탐색에서 계층적 카탈로그 구조와 LLM 가이드 클러스터링의 서로 다른 조직화 방식을 비교할 수 있습니다.
- 🔗 후속 연구: [[papers/374_Generating_a_structured_summary_of_numerous_academic_papers/review]] — 문헌 리뷰를 위한 계층적 카탈로그 생성 방법으로 BigSurvey 데이터셋의 구조화된 요약과 보완적이다.
- 🔄 다른 접근: [[papers/215_Chime_Llm-assisted_hierarchical_organization_of_scientific_s/review]] — 문헌 검토를 위한 계층적 카탈로그 생성의 다른 접근법으로 본 논문과 유사한 목표를 다른 방식으로 달성한다.
- 🏛 기반 연구: [[papers/450_Knowledge_navigator_Llm-guided_browsing_framework_for_explor/review]] — 계층적 카탈로그 생성의 구조적 접근법이 LLM 가이드 탐색 프레임워크의 조직화 기반을 제공합니다.
