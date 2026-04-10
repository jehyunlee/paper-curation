---
title: "732_Scireviewgen_a_large-scale_dataset_for_automatic_literature"
authors:
  - "Tetsu Kasanishi"
  - "Masaru Isonuma"
  - "Junichiro Mori"
  - "Ichiro Sakata"
date: "2023"
doi: "논문"
arxiv: ""
score: 4.25
essence: "본 논문은 자동 문헌 리뷰 생성을 위한 최초의 대규모 데이터셋인 **SciReviewGen**을 제시한다. 10,000개 이상의 문헌 리뷰와 690,000개의 인용 논문으로 구성되어 있으며, 쿼리 기반 다중 문서 요약(query-focused multi-document summarization) 작업으로 정의한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Scientific_Literature_Summarization"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Kasanishi et al._2023_Scireviewgen a large-scale dataset for automatic literature review generation.pdf"
---

# SciReviewGen: a large-scale dataset for automatic literature review generation

> **저자**: Tetsu Kasanishi, Masaru Isonuma, Junichiro Mori, Ichiro Sakata | **날짜**: 2023 | **DOI**: [논문 링크](https://arxiv.org/abs/2305.15186)

---

## Essence

![Figure 1](figures/fig1.webp)
*Figure 1: 문헌 리뷰 생성 작업의 개요. 입력된 논문의 초록과 리뷰/챕터 제목(쿼리)을 통해 문헌 리뷰 텍스트를 생성한다.*

본 논문은 자동 문헌 리뷰 생성을 위한 최초의 대규모 데이터셋인 **SciReviewGen**을 제시한다. 10,000개 이상의 문헌 리뷰와 690,000개의 인용 논문으로 구성되어 있으며, 쿼리 기반 다중 문서 요약(query-focused multi-document summarization) 작업으로 정의한다.

## Motivation

- **Known**: 신경망 기반 NLP 모델이 다양한 분야에서 성공을 거두었으나, 매 9년마다 발표 논문이 2배 증가하면서 문헌 리뷰의 자동화 필요성이 대두됨. GALACTICA 같은 대규모 언어 모델도 환각(hallucination) 문제로 중단됨.

- **Gap**: 자동 문헌 리뷰 생성을 위한 **대규모 데이터셋이 부재**하여 지도 학습 기반의 신경망 모델 개발이 어려움. 기존 연구는 수십 개 수준의 작은 데이터셋에만 의존.

- **Why**: 과학 논문의 폭발적 증가로 새로운 분야 진입 시 자동 문헌 리뷰 생성이 연구자들에게 큰 도움이 될 수 있음.

- **Approach**: Semantic Scholar Open Research Corpus(S2ORC)를 기반으로 컴퓨터 과학 분야의 대규모 문헌 리뷰 데이터셋을 구축하고, 트랜스포머 기반 요약 모델을 확장하여 평가.

## Achievement

![Table 1](figures/table1.webp)
*Table 1: SciReviewGen과 기타 다중 문서 요약 데이터셋의 비교. SciReviewGen(split)은 평균 1,274개의 입력 토큰과 604개의 출력 토큰을 가짐.*

1. **최초의 대규모 문헌 리뷰 데이터셋 구축**: 9,187개의 학습 샘플, 484개의 검증 샘플, 459개의 테스트 샘플로 구성된 SciReviewGen 릴리스. 챕터 단위로 분할 시 84,705개의 학습 샘플으로 확대.

2. **기존 데이터셋과 차별화**: Multi-XScience(116개 토큰)와 비교하여 약 5.2배 긴 출력(604개 토큰), Multi-News(2,103개)와 비교하여 6배 긴 입력(12,503개 토큰)을 처리하는 더 도전적인 과제 제시.

3. **자동 및 인간 평가**: 약 30%의 생성된 챕터가 인간이 작성한 리뷰와 동등하거나 우수한 수준을 달성하며, 동시에 환각 문제와 정보 부족 등의 한계 명확화.

## How

- **데이터셋 구축 프로세스**:
  - S2ORC에서 제목에 "survey", "overview", "literature review", "review"를 포함하는 13,984개 후보 논문 추출
  - SciBERT 기반 분류기로 정제: 1) 여러 논문 검토, 2) 과학 논문만 검토하는 두 가지 기준 적용
  - 최종 10,000개 이상의 문헌 리뷰와 690,000개 인용 논문 확보

- **작업 정의**:
  - 입력: 인용 논문의 초록, 문헌 리뷰 제목, 챕터 제목(쿼리)
  - 출력: 각 챕터별 문헌 리뷰 텍스트
  - 분석 범위: 논문 선정 및 챕터 분류 과정 제외, 주어진 논문들을 기반으로 한 요약에만 집중

- **모델 확장**:
  - Fusion-in-Decoder(FiD)를 쿼리 기반 다중 문서 요약용으로 확장
  - Query-weighted Fusion-in-Decoder(QFiD) 제안: 각 입력 문서의 쿼리 관련성을 명시적으로 고려

- **평가 방식**:
  - 자동 평가: ROUGE, BERTScore 등 활용
  - 인간 평가: 생성된 챕터와 인간 작성 리뷰 비교 (정보성, 정확성, 일관성 등)

## Originality

- **최초 대규모 데이터셋**: 문헌 리뷰 자동 생성을 위한 첫 번째 체계적인 대규모 데이터셋 제공으로 새로운 연구 분야 개척

- **도메인 무관적 구축 방식**: S2ORC 기반으로 구축되어 의료, 생물학 등 다른 과학 분야로 확장 가능한 방법론 제시

- **복합 입력 정보 활용**: 논문 초록뿐만 아니라 인용 문장, 인용 네트워크, 메타데이터 등 다양한 추가 정보 포함

- **쿼리 기반 접근**: 일반적인 입력 문서 연결이 아닌 쿼리 가중 방식으로 더 정교한 요약 모델 제안

## Limitation & Further Study

- **현재 한계**:
  - 환각(hallucination) 문제로 인한 사실 정확성 부족
  - 30%만이 인간 수준의 품질 달성
  - 추상적이고 세부 정보 부족한 생성 결과
  - 챕터 단위 독립 생성으로 인한 전체 문헌 리뷰의 일관성 결여
  - 논문 초록만 사용으로 인한 정보 손실 (전체 텍스트는 미사용)

- **후속 연구 방향**:
  - 사실 검증 메커니즘 추가로 환각 문제 완화
  - 챕터 간 의존성을 고려한 전체 문헌 리뷰 생성
  - 전체 논문 텍스트 통합 활용 방식 개발
  - 인용 네트워크와 인용 문장을 더 활용한 모델 개선
  - 의료, 생물학 등 다른 학문 분야로의 확장 및 도메인 특화 모델 개발
  - 문헌 리뷰에서 제외된 논문 선정 및 챕터 분류 작업의 자동화

## Evaluation

- **Novelty**: 4.5/5
  - 최초의 대규모 문헌 리뷰 데이터셋으로 높은 가치, 다만 기존 MDS 방법론의 응용에 그침

- **Technical Soundness**: 4/5
  - 데이터셋 구축 방법론 타당하고, QFiD 제안이 합리적이나, 인간 평가가 제한적

- **Significance**: 4.5/5
  - 자동 문헌 리뷰 생성 분야의 중요한 기초 자료 제공으로 높은 임팩트 예상, 현실 적용에는 추가 개선 필요

- **Clarity**: 4/5
  - 전반적으로 명확하고 체계적이나, 데이터셋 정제 기준이 다소 주관적

- **Overall**: 4.25/5

**총평**: 본 논문은 자동 문헌 리뷰 생성을 위한 첫 번째 대규모 벤치마크 데이터셋을 제시함으로써 학술 NLP 분야에 중요한 기여를 한다. 다만 생성된 리뷰의 품질 개선과 현실적 적용을 위해서는 환각 문제 해결 및 더 정교한 모델 개발이 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/109_Assisting_in_writing_wikipedia-like_articles_from_scratch_wi/review]] — SciReviewGen이 쿼리 기반 다중 문서 요약으로 문헌 리뷰를 자동 생성하는 반면, STORM은 다관점 질문을 통한 아웃라인 중심 접근법을 사용하여 상호 보완적 전략을 제시함
- 🔗 후속 연구: [[papers/534_Meta-review_generation_with_checklist-guided_iterative_intro/review]] — 체크리스트 가이드 반복적 내성을 통한 메타 리뷰 생성이 SciReviewGen의 기본적인 문헌 리뷰 생성을 더 정교한 검토와 평가 과정을 포함하는 메타 수준으로 발전시킨 연구임
- 🏛 기반 연구: [[papers/581_Oarelatedwork_A_large-scale_dataset_of_related_work_sections/review]] — 관련 연구 섹션의 대규모 데이터셋이 SciReviewGen의 자동 문헌 리뷰 생성 시스템을 훈련하고 평가할 수 있는 핵심적인 데이터 자원을 제공함
- 🏛 기반 연구: [[papers/780_Surveyforge_On_the_outline_heuristics_memory-driven_generati/review]] — 대규모 문헌 리뷰 데이터셋 구축 방법론을 자동 설문지 생성에 적용한 기반
- 🔗 후속 연구: [[papers/812_TLDR_Extreme_Summarization_of_Scientific_Documents/review]] — 단일 논문 요약에서 다중 논문을 활용한 자동 문헌 리뷰 생성으로 확장한 발전된 형태의 연구입니다.
- 🔄 다른 접근: [[papers/109_Assisting_in_writing_wikipedia-like_articles_from_scratch_wi/review]] — STORM이 다관점 질문을 통한 아웃라인 생성에 초점을 맞춘 반면, SciReviewGen은 쿼리 기반 다중 문서 요약으로 접근하여 서로 다른 장문 작성 전략을 제시함
- 🔗 후속 연구: [[papers/581_Oarelatedwork_A_large-scale_dataset_of_related_work_sections/review]] — 관련 업무 섹션 생성을 자동화된 문헌 리뷰 생성의 더 포괄적인 프로세스로 확장함
- 🏛 기반 연구: [[papers/108_Ask_retrieve_summarize_A_modular_pipeline_for_scientific_lit/review]] — 자동 문헌 검토를 위한 대규모 데이터셋으로 본 논문의 요약 시스템 학습 기반을 제공한다.
- 🔗 후속 연구: [[papers/402_Hierarchical_catalogue_generation_for_literature_review_a_be/review]] — 문헌 리뷰 자동 생성에서 단순한 데이터셋을 계층적 카탈로그 구조로 확장한 고도화된 접근법입니다.
- 🔗 후속 연구: [[papers/742_Select_read_and_write_A_multi-agent_framework_of_full-text-b/review]] — 자동 문헌 리뷰 생성을 다중 에이전트와 그래프 기반 제약을 활용한 더 정교한 관련 연구 섹션 생성으로 발전시킨다.
- 🧪 응용 사례: [[papers/897_Can_AI_review_the_scientific_literature__and_figure_out_what/review]] — 자동 문헌 검토 생성의 실제 적용 사례와 데이터셋을 제공한다
