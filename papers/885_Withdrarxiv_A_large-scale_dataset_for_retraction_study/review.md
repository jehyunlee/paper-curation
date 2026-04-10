---
title: "885_Withdrarxiv_A_large-scale_dataset_for_retraction_study"
authors:
  - "Delip Rao"
  - "Jonathan Young"
  - "Thomas G. Dietterich"
  - "Chris Callison-Burch"
date: "2024"
doi: "미공개"
arxiv: ""
score: 4.4
essence: "본 논문은 arXiv 플랫폼에서 철회된 14,000개 이상의 논문을 수집한 첫 대규모 철회 연구 데이터셋(WithdrawArXiv)을 제시하며, 철회 이유를 10가지 범주로 분류하는 자동 분류 체계를 개발했다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Scientific_Literature_Summarization"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Rao et al._2024_Withdrarxiv A large-scale dataset for retraction study.pdf"
---

# Withdrarxiv: A large-scale dataset for retraction study

> **저자**: Delip Rao, Jonathan Young, Thomas G. Dietterich, Chris Callison-Burch | **날짜**: 2024 | **DOI**: [미공개]

---

## Essence

![Figure 1](figures/fig1.webp) *arXiv 초록 페이지에서 추출한 메타데이터 요소*

본 논문은 arXiv 플랫폼에서 철회된 14,000개 이상의 논문을 수집한 첫 대규모 철회 연구 데이터셋(WithdrawArXiv)을 제시하며, 철회 이유를 10가지 범주로 분류하는 자동 분류 체계를 개발했다.

## Motivation

- **Known**: 의학 분야에서는 정기적인 논문 철회 연구가 이루어지고 있으며, 생성형 AI 기반 과학과 검색 증강 시스템이 프리프린트 서버에 의존하고 있다.
- **Gap**: 컴퓨터과학 및 STEM 분야에서 arXiv 프리프린트에 대한 체계적인 철회 연구가 부재하며, 철회된 논문 정보의 불일치로 인해 철회 후에도 계속 인용되는 문제가 발생한다.
- **Why**: 빠르게 성장하는 과학 커뮤니티가 arXiv에 의존하고 있고, 철회된 논문이 AI 기반 시스템에 포함될 위험이 증가하고 있으며, 과학적 실현가능성(scientific feasibility) 자동화 연구의 기초 데이터가 필요하다.
- **Approach**: arXiv와 협력하여 철회된 16,460개 논문 ID를 수집하고, 임베딩과 K-means 클러스터링으로 철회 의견(comment)을 분석한 후, GPT-4 제로샷 프롬프팅으로 자동 분류를 수행했다.

## Achievement

![Figure 2](figures/fig2.webp) *수동 주석 10% 계층화 샘플(총 1,620개)에서 평가한 제로샷 분류 혼동 행렬*

1. **WithdrawArXiv 데이터셋 구축**: 2024년 9월까지 arXiv 전체 역사에 걸친 16,395개의 철회 논문과 관련 의견을 포함한 첫 대규모 dataset 개발

2. **철회 이유 분류 체계 개발**: 10가지 범주(중대한 오류, 미완성 저작, 오타, 신규성 부족, 행정/법적 문제, arXiv 정책 위반, 다른 출판물에 포함, 표절, 개인적 사유, 미명시)를 식별하고 각 범주별 예제 제시

3. **높은 정확도의 자동 분류 달성**: 가중 평균 F1-score 0.9594로 제로샷 프롬프팅 분류 성능 입증, 특히 "개인적 사유"(1.0)와 "중대한 오류"(0.9967)에서 우수한 성능

4. **WithdrawArXiv-SciFy 릴리스**: 과학적 실현가능성 연구, 주장 검증, 자동화된 정리 증명을 위해 파싱된 전체 텍스트 PDF 스크립트를 포함한 확장 데이터셋 공개

## How

![Figure 3](figures/fig3.webp) *논문 철회 사유의 분포*

- **Step 1 - 철회 논문 ID 수집**: arXiv.org와 협력하여 공식 채널을 통해 2024년 9월까지의 모든 철회 논문 ID(16,460개) 확보
- **Step 2 - 메타데이터 추출**: HTML 파싱을 통해 철회 의견, 주제 영역, 버전 URL 등 메타데이터 추출
- **Step 3 - 개인정보 보호**: scrubadubdub 패키지를 사용하여 이름, 이메일 등 개인식별정보(PII)를 [RETRACTED_NAME] 등으로 대체
- **Step 4 - 의견 클러스터링**: 텍스트 임베딩 모델로 의견 벡터화 후 K=100으로 K-means 클러스터링 수행, 수동으로 100개 클러스터를 검토하여 10개 범주로 정제
- **Step 5 - 제로샷 분류**: GPT-4 모델에 10가지 범주 정의와 예제를 제공하여 제로샷 프롬프팅 기반 분류, 어려운 사례 테스트로 프롬프트 검증

## Originality

- **첫 arXiv 대규모 철회 연구**: 의학 분야 중심의 기존 철회 연구를 STEM 전반, 특히 컴퓨터과학 분야로 확장
- **종합적 분류 체계**: 10가지 세분화된 철회 이유 분류로 철회의 특성을 다차원적으로 분석
- **윤리적 데이터 공개**: 책임 있는 데이터 릴리스를 위해 PII 제거 및 윤리 고려사항 명시적 논의 (Section 8)
- **실용적 응용**: 과학적 실현가능성 자동화, 주장 검증, 검색 증강 시스템의 신뢰성 향상 등 실질적 응용 연결
- **높은 성능의 자동화 방법론**: 수동 라벨링 최소화(1,620개만) 후 제로샷 LLM 기반 분류로 일관성 있는 확장 가능성 입증

## Limitation & Further Study

- **단일 플랫폼 제한**: arXiv만 대상으로 하여 다른 프리프린트 서버(bioRxiv, medRxiv 등)나 정식 저널의 철회 패턴과의 비교 분석 부재
- **영문 편향**: arXiv의 영문 중심 특성으로 인해 비영어권 학문 공동체의 철회 패턴 미포함
- **분류 오류 분석**: "신규성 부족"과 "다른 출판물에 포함" 범주 간 혼동(F1-score 0.75, 0.91)으로 인한 미분화 가능성
- **시간적 분석 부족**: 철회 원인의 시간적 추이나 학문 분야별 동향 분석의 깊이 제한
- **후속 연구**: (1) 다국어 프리프린트 서버 포함 확장, (2) 철회 결정 시간 분석, (3) 자동 결함 탐지 모델 개발, (4) 철회 예측 모델 구축


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4.5/5
- Significance: 4/5
- Clarity: 4.5/5
- Overall: 4.4/5

**총평**: 이 논문은 STEM 분야에서 처음으로 대규모 논문 철회 데이터셋을 제시하고 실용적 자동화 방법론을 제공하여 과학 무결성 연구에 중요한 기여를 하고 있으나, 단일 플랫폼 한정과 분류 세분화 미흡이라는 제한사항이 있다.

## Related Papers

- 🔄 다른 접근: [[papers/812_TLDR_Extreme_Summarization_of_Scientific_Documents/review]] — 과학 논문의 생산적 요약 생성과 문제가 있는 논문의 철회 분석이라는 서로 다른 과학 문헌 처리 관점을 제시합니다.
- 🔗 후속 연구: [[papers/093_All_that_glitters_is_not_novel_Plagiarism_in_ai_generated_re/review]] — arXiv 철회 논문 연구에서 AI 생성 연구의 표절 문제로 확장하여 현대적 학술 윤리 문제를 다룹니다.
- 🏛 기반 연구: [[papers/591_Openreview_should_be_protected_and_leveraged_as_a_community/review]] — 철회 논문 데이터셋 연구가 OpenReview와 같은 학술 커뮤니티 플랫폼 보호의 중요성을 뒷받침하는 실증적 근거를 제공합니다.
- 🧪 응용 사례: [[papers/698_Scaling_Reproducibility_An_AI-Assisted_Workflow_for_Large-Sc/review]] — 철회된 논문에 대한 대규모 데이터셋 연구는 AI 지원 재현성 워크플로우가 해결해야 할 연구 신뢰성 문제의 실제 사례를 보여준다.
- 🔄 다른 접근: [[papers/812_TLDR_Extreme_Summarization_of_Scientific_Documents/review]] — 과학 논문의 요약 생성과 철회 논문의 분류라는 서로 다른 과학 문헌 처리 접근법을 제시합니다.
