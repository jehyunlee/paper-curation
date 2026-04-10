---
title: "375_Generating_full_length_wikipedia_biographies_The_impact_of_g"
authors:
  - "Angela Fan"
  - "Claire Gardent"
date: "2022"
doi: "N/A"
arxiv: ""
score: 4.0
essence: "본 논문은 웹 검색 기반 정보 검색(retrieval-augmented generation)과 사전학습 모델을 활용하여 전체 길이의 위키피디아 전기문을 자동 생성하는 시스템을 제시하며, 특히 웹상 정보가 부족한 여성 인물 전기 생성에서 성별 편향의 영향을 분석한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Academic_Writing_Diversity"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Chung et al._2022_Generating full length wikipedia biographies The impact of gender bias on the retrieval-based gener.pdf"
---

# Generating full length wikipedia biographies: The impact of gender bias on the retrieval-based generation of women biographies

> **저자**: Angela Fan, Claire Gardent | **날짜**: 2022 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)
*모델 아키텍처: 웹 검색 결과에서 관련 정보를 검색(retrieval)한 후, 섹션별로 위키피디아 전기문을 생성하고 인용문을 추가하는 end-to-end 시스템*

본 논문은 웹 검색 기반 정보 검색(retrieval-augmented generation)과 사전학습 모델을 활용하여 전체 길이의 위키피디아 전기문을 자동 생성하는 시스템을 제시하며, 특히 웹상 정보가 부족한 여성 인물 전기 생성에서 성별 편향의 영향을 분석한다.

## Motivation

- **Known**: 위키피디아는 지식 보급의 주요 매체이지만, 남성 중심의 편향된 정보를 담고 있으며, 특히 전기 부문에서 여성에 관한 기사가 매우 부족함
- **Gap**: 기존 위키피디아 생성 연구는 단편적이거나 추출 기반 방법을 사용하였으며, 장문 생성, 인용 처리, 여성 전기 생성의 어려움을 체계적으로 다루지 못함
- **Why**: 자동 전기 생성 시스템은 인간 편집자의 부담을 줄이고 성별 편향을 완화하는 기초 도구가 될 수 있음
- **Approach**: 검색-생성(retrieval-augmented generation) 아키텍처와 섹션별 생성, 캐싱 메커니즘을 활용하여 장문의 구조화된 전기문 생성 및 인용 추가

## Achievement

![Figure 2](figures/fig2.webp)
*Libbie Hyman(동물학자)의 Work 섹션 생성 사례: 검색된 정보를 바탕으로 자연스러운 문장 생성 및 인용 추가*

1. **여성 전기 데이터셋 구축**: 1,527개의 여성 인물 위키피디아 전기 평가 데이터셋 구축으로 웹 정보 부족 시나리오 분석
2. **장문 생성 모델 개발**: 섹션별 생성과 Transformer-XL 캐싱을 통해 장문 일관성 유지 및 신뢰성 있는 인용 추가 달성
3. **성별 편향 정량화**: 여성 전기(검색 어려움) vs 일반 전기(검색 용이) 간 생성 성능 차이를 ROUGE-L, entailment, 개체명 커버리지로 분석
4. **대규모 인간 평가**: 생성 전기의 사실성(factuality)과 정보 커버리지(coverage)를 인간 평가로 검증

## How

- **검색 모듈(Retrieval Module)**:
  - 쿼리: 인물명 + 직업 + 섹션 헤더의 조합으로 다양한 섹션별 정보 검색 가능
  - RoBERTa-base(LayerDrop 적용)로 웹 문서 문장 인코딩 후 dot-product로 관련도 계산
  - 상위 k개 문장(~1,000단어) 추출 및 생성 모듈 학습에 따라 동적 업데이트

- **생성 모듈(Generation Module)**:
  - BART-Large 기반 Sequence-to-Sequence 모델 사용
  - 인물명, 직업, 섹션 헤더, 검색된 증거 정보를 입력으로 활용
  - Transformer-XL 캐싱: 이전 섹션의 숨겨진 상태를 메모리로 사용하여 중복 제거 및 일관성 유지

- **인용 모듈(Citation Module)**:
  - 각 섹션 생성 후 검색된 웹 문서를 인용으로 명시
  - 인간이 작성한 위키피디아 형식 모방

## Originality

- **여성 전기 편향 분석**: 웹상 정보 가용성 차이가 생성 품질에 미치는 영향을 체계적으로 분석한 첫 시도
- **섹션별 생성 구조**: 전체 기사를 한 번에 생성하지 않고 섹션 단위로 생성하여 장문 일관성 및 구조 보존
- **End-to-end 검색-생성**: 검색 모듈이 생성 모듈의 역전파 피드백을 받아 학습되는 통합 시스템
- **자동 인용 생성**: 기존 연구에서 다루지 않은 인용 추가 기능으로 실질적인 위키피디아 품질 구현

## Limitation & Further Study

- **검색 의존성**: 모델 성능이 웹 검색 결과 품질에 크게 의존하므로, 정보가 부족한 분야(여성, 소수자, 비영어권)에서 성능 저하
- **평가 제한**: 자동 지표(ROUGE)는 장문 생성의 다양성을 충분히 반영하지 못하며, 인간 평가 규모 제한
- **인포박스 미포함**: 위키피디아의 구조화된 정보(infobox)를 생성하지 않아 완전한 자동화 미달성
- **후속 연구**:
  - 정보 부족 분야에 대한 특화된 검색 전략 개발
  - 다국어 전기 생성 확장 및 지역별 편향 분석
  - 생성 전기와 인간 편집자 협업 시스템 구축

## Evaluation

- **Novelty**: 4/5 — 여성 전기 편향 분석은 신선하나, 기본 검색-생성 아키텍처는 기존 기술 활용
- **Technical Soundness**: 4/5 — 전반적으로 견고한 설계이나, 검색 모듈의 제한적 스케일링과 평가 지표의 한계
- **Significance**: 4/5 — 위키피디아 성별 편향 완화에 기여하나, 실제 배포까지의 간격 존재
- **Clarity**: 4/5 — 전체 구조 및 방법론이 명확하게 서술되었으나, 세부 학습 과정 및 하이퍼파라미터 정보 부족
- **Overall**: 4/5

**총평**: 본 논문은 장문 위키피디아 전기 자동 생성이라는 도전적인 과제를 검색-생성 아키텍처로 해결하며, 여성 인물에 대한 웹 정보 부족이 생성 품질에 미치는 영향을 처음으로 정량화한 점에서 의의가 있다. 다만 검색 결과의 품질에 대한 과도한 의존성과 자동 평가 지표의 제한성이 실무 적용을 위해 개선되어야 할 과제이다.

## Related Papers

- 🏛 기반 연구: [[papers/284_Does_writing_with_language_models_reduce_content_diversity_a/review]] — 언어 모델과의 글쓰기가 콘텐츠 다양성에 미치는 영향 연구로 본 논문의 성별 편향 분석의 이론적 기반을 제공한다.
- 🔄 다른 접근: [[papers/886_Wordcraft_A_human-ai_collaborative_editor_for_story_writing/review]] — 스토리 작성을 위한 인간-AI 협업 편집기로 본 논문과 다른 장르에서의 생성 및 편향 문제를 다룬다.
- 🔗 후속 연구: [[papers/158_Biasfilter_An_inference-time_debiasing_framework_for_large_l/review]] — 대규모 언어 모델을 위한 추론 시간 편향 제거 프레임워크로 본 논문의 성별 편향 문제를 해결하는 방법론을 제시한다.
