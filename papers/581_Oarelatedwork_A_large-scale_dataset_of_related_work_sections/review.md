---
title: "581_Oarelatedwork_A_large-scale_dataset_of_related_work_sections"
authors:
  - "Martin Docekal"
  - "Martin Fajcik"
  - "Pavel Smrz"
date: "2024"
doi: "arXiv:2405.01930"
arxiv: ""
score: 4.2
essence: "본 논문은 오픈 액세스 논문의 전체 텍스트를 포함하는 대규모 관련 업무 생성 데이터셋 OARelatedWork를 제시하며, 초록(abstract)만 사용하는 기존 방식에서 벗어나 전체 콘텐츠를 활용한 다중 문서 요약 연구를 추진한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Scientific_Literature_Summarization"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Son et al._2024_Oarelatedwork A large-scale dataset of related work sections with full-texts from open access sourc.pdf"
---

# OARelatedWork: A large-scale dataset of related work sections with full-texts from open access sources

> **저자**: Martin Docekal, Martin Fajcik, Pavel Smrz | **날짜**: 2024 | **DOI**: [arXiv:2405.01930](https://arxiv.org/abs/2405.01930)

---

## Essence

![Figure 1](figures/fig1.webp) *전체 관련 업무(Related Work) 섹션을 인용된 논문들과 대상 논문의 전체 텍스트로부터 생성하는 태스크*

본 논문은 오픈 액세스 논문의 전체 텍스트를 포함하는 대규모 관련 업무 생성 데이터셋 OARelatedWork를 제시하며, 초록(abstract)만 사용하는 기존 방식에서 벗어나 전체 콘텐츠를 활용한 다중 문서 요약 연구를 추진한다.

## Motivation

- **Known**: 기존 관련 업무 생성 연구는 인용 논문의 초록만 사용하고, 관련 업무 섹션의 일부분만 생성하는 방식에 국한되어 있음
- **Gap**: 전체 관련 업무 섹션을 생성할 수 있는 대규모 데이터셋 부재, 장문 요약(long-form summarization) 평가 메트릭의 한계
- **Why**: 과학 논문의 전체 텍스트 접근이 어려우며(저작권 장벽), 초록 기반 학습의 한계를 극복하기 위함
- **Approach**: 오픈 액세스 소스(CORE, Semantic Scholar)로부터 1억 2,490만 개 문서를 수집하고, 자동 문헌 연결 및 계층 구조 파싱을 통해 정제된 데이터셋 구축

## Achievement

![Figure 2](figures/fig2.webp) *문헌의 계층 구조 파싱 예시: 내부 번호 매기기와 앵커 생성 단계*

1. **대규모 데이터셋 구축**: 94,450개의 관련 업무 섹션과 5,824,689개의 고유 참조 논문을 포함한 첫 번째 전체 관련 업무 생성 데이터셋 완성

2. **성능 향상 실증**: 추상적 요약(abstractive)의 추출적 상한(extractive upper bound)이 초록만 사용할 때 대비 전체 콘텐츠 사용 시 ROUGE-2 기준 217% 증가 (PRIMERA 모델 0.08 → 0.15)

3. **평가 메트릭 개선**: BERTScore의 길이 제한 문제를 해결하는 메타-메트릭(meta-metric) 제안 및 인간 판단과의 상관성 검증

## How

![Figure 3](figures/fig3.webp) *연구 도메인에 따른 데이터셋 분포의 차이*

- **데이터 소스 통합**: CORE(540만 문서)와 Semantic Scholar(1억 2,920만 문서) 데이터 병합 및 중복 제거
  
- **자동 문헌 연결**: Microsoft Academic Graph와 Semantic Scholar 인용 그래프를 활용한 다단계 문헌 매칭
  - 후보 검색(title 문자열 매칭), 근사 매칭(LSH 기반 임베딩), 필터링(제목/저자/연도 기반)
  - 제목 유사도 임계값 0.75(Jaccard/Containment 조화평균)

- **계층 구조 파싱**: 제목의 번호 매김을 이용한 섹션/소섹션 자동 추출
  - 결측 번호 보충, 가장 긴 sparse 수열(앵커) 식별, 나머지 제목 계층에 적합
  - scispaCy를 활용한 문장 분할(biomedical 도메인 특화)

- **데이터 정제**: 인용 범위 확장(merged citations [3-6] → 개별 인용으로 분리), JSON 형식의 트리 표현 구조 적용

- **평가 메트릭**: 장문 요약을 작은 블록으로 분할하여 BERTScore 적용, 인간 판단과의 상관성 검증

## Originality

- 오픈 액세스 소스만을 활용한 첫 번째 **전체 관련 업무 생성 데이터셋** 공개 (이전 연구는 초록 기반)

- **자동 문헌 연결 파이프라인**: 다중 소스(MAG, Semantic Scholar) 통합으로 링크 정확도 향상 (수동 평가 94%)

- **계층 구조 파싱 알고리즘**: 불완전한 제목 번호를 자동 복원하는 지능형 방법론 제시

- **메타-메트릭 제안**: 길이 제한이 있는 임베딩 기반 메트릭을 활용한 장문 요약 평가 방법론

- **구조화된 데이터 포맷**: JSON 기반 트리 표현으로 향후 응용 확장성 극대화

## Limitation & Further Study

- **문헌 연결 한계**: 자체 검색기의 기여도가 미미(0.6% 증가)하여 수동 정제 필요 가능성 존재

- **파싱 오류율**: 섹션 파싱 실패율 20%(100개 샘플 기준), 초록 없는 논문의 처리 방안 미흡

- **도메인 편향**: 생의학(biomedical) 분야에 최적화된 scispaCy 사용으로 다른 분야에 대한 성능 검증 필요

- **후속 연구**: (1) 메타-메트릭의 대규모 검증, (2) 추상적 요약 모델의 장문 생성 성능 개선, (3) 구조 인식 모델링(structure-aware modeling)

## Evaluation

- **Novelty**: 4.5/5 - 첫 전체 관련 업무 데이터셋이나, 기본적인 데이터 처리 기법 활용

- **Technical Soundness**: 4/5 - 자동 파이프라인 설계가 타당하나, 오류 분석과 정제 방법이 제한적

- **Significance**: 4.5/5 - 초록 기반 연구의 한계를 명확히 보여주고 실질적 개선(217% ROUGE-2)을 입증

- **Clarity**: 4/5 - 전반적으로 명확하나, 문헌 연결 알고리즘의 세부 기준이 복잡함

- **Overall**: 4.2/5

**총평**: 오픈 액세스 자료만으로 구축한 첫 대규모 관련 업무 데이터셋으로서 학술 요약 분야에 실질적 기여를 하며, 전체 콘텐츠 활용의 이점을 강력히 입증한 점이 주요 강점이다. 다만 자동 파이프라인의 정확성 검증과 다양한 도메인에 대한 확장성 평가가 보완되어야 한다.

## Related Papers

- 🏛 기반 연구: [[papers/561_Ms2_Multi-document_summarization_of_medical_studies/review]] — 의료 분야 다중문서 요약의 기초적 접근이 관련 업무 생성을 위한 전체 텍스트 활용 방법의 토대를 제공함
- 🔄 다른 접근: [[papers/778_Summarizing_multiple_documents_with_conversational_structure/review]] — 둘 다 학술 논문의 다중문서 요약을 다루지만 하나는 관련 업무, 다른 하나는 메타리뷰 생성에 중점을 둠
- 🔗 후속 연구: [[papers/732_Scireviewgen_a_large-scale_dataset_for_automatic_literature/review]] — 관련 업무 섹션 생성을 자동화된 문헌 리뷰 생성의 더 포괄적인 프로세스로 확장함
- 🔗 후속 연구: [[papers/190_Causal_intervention_for_abstractive_related_work_generation/review]] — 오픈액세스 관련 업무 섹션 대규모 데이터셋을 활용하여 인과 개입 기법의 효과를 검증할 수 있다.
- 🏛 기반 연구: [[papers/732_Scireviewgen_a_large-scale_dataset_for_automatic_literature/review]] — 관련 연구 섹션의 대규모 데이터셋이 SciReviewGen의 자동 문헌 리뷰 생성 시스템을 훈련하고 평가할 수 있는 핵심적인 데이터 자원을 제공함
- 🔗 후속 연구: [[papers/561_Ms2_Multi-document_summarization_of_medical_studies/review]] — 의료 연구의 다중문서 요약을 전체 논문 텍스트를 활용하는 관련 업무 생성으로 확장하여 더 포괄적인 문헌 요약을 제공함
- 🔄 다른 접근: [[papers/778_Summarizing_multiple_documents_with_conversational_structure/review]] — 둘 다 학술 논문의 다중문서 요약을 다루지만 하나는 메타리뷰, 다른 하나는 관련 업무 생성에 중점을 둠
- 🔗 후속 연구: [[papers/573_Neural_related_work_summarization_with_a_joint_context-drive/review]] — 관련 연구 섹션 데이터셋을 신경망 기반 관련 연구 요약 시스템으로 확장한 실제 적용 연구입니다.
