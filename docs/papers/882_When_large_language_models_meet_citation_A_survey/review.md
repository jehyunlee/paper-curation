---
title: "882_When_large_language_models_meet_citation_A_survey"
authors:
  - "Yang Zhang"
  - "Yufei Wang"
  - "Kai Wang"
  - "Quan Z. Sheng"
  - "Lina Yao"
date: "2023"
doi: "10.48550/arXiv.2309.09727"
arxiv: ""
score: 4.0
essence: "대규모 언어 모델(LLM)과 학술 인용 분석 간의 상호 보완 관계를 체계적으로 정리한 최초의 종합 조사 연구이다. LLM이 인용 분석 작업의 성능을 향상시키고, 역으로 인용 데이터가 LLM의 텍스트 표현을 개선하는 양방향 이익 구조를 제시한다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Scientific_Data_Interpretation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhang et al._2023_When large language models meet citation A survey.pdf"
---

# When large language models meet citation: A survey

> **저자**: Yang Zhang, Yufei Wang, Kai Wang, Quan Z. Sheng, Lina Yao, A. Mahmood, Wei Emma Zhang, Rongying Zhao | **날짜**: 2023 | **DOI**: [10.48550/arXiv.2309.09727](https://doi.org/10.48550/arXiv.2309.09727)

---

## Essence

![Figure 1](figures/fig1.webp)
*LLM과 인용 간의 상호 이익적 관계*

대규모 언어 모델(LLM)과 학술 인용 분석 간의 상호 보완 관계를 체계적으로 정리한 최초의 종합 조사 연구이다. LLM이 인용 분석 작업의 성능을 향상시키고, 역으로 인용 데이터가 LLM의 텍스트 표현을 개선하는 양방향 이익 구조를 제시한다.

## Motivation

- **Known**: 학술 논문의 인용(Citation)은 원본 지식을 인정하고 신용하는 필수 요소이며, 인용 주변의 텍스트 맥락은 인용 동기와 목적을 반영한다. 또한 LLM은 최근 자연언어처리 분야에서 탁월한 성능을 보이고 있다.

- **Gap**: 기존 인용 관련 조사 논문들은 인용 분석 작업의 설계와 일반적인 기계학습/NLP 기술 적용만 다루었으며, LLM이 인용 분석을 어떻게 지원하는지, 그리고 인용 데이터가 LLM을 어떻게 개선하는지에 대한 양방향 관계 분석이 부재했다.

- **Why**: 과학 문헌의 폭증과 인용 정보의 복잡성 증가에 따라 자동화된 인용 분석이 필수화되고 있으며, 동시에 인용 네트워크가 담고 있는 문서 간 고품질 관계 정보는 LLM 사전학습(Pre-training)에 활용될 가치가 있다.

- **Approach**: LLM이 인용 분석을 돕는 경로(인용 분류, 인용 기반 요약, 인용 추천)와 인용이 LLM을 개선하는 경로(인용 예측, 네트워크 구조 활용, 문서 간 관계)를 체계적으로 분류 정리한다.

## Achievement

![Figure 2](figures/fig2.webp)
*LLM과 인용 연구의 분류 체계*

1. **LLM의 인용 분석 기여 메커니즘 규명**: 고품질 텍스트 임베딩, 강력한 텍스트 생성 능력, 인용 구조 정보 통합 능력 등 세 가지 핵심 메커니즘을 통해 LLM이 인용 분류, 인용 기반 요약, 인용 추천 작업의 성능을 향상시킴을 입증

2. **인용 분류의 다층적 접근법 제시**: BERT, SciBERT, T5 등 판별형(Discriminative) LLM의 고품질 표현뿐 아니라, T5, GPT-2 등 생성형(Generative) LLM을 통한 합성 데이터 생성 및 데이터 불균형 해결 방법 제시

3. **문서 간 관계 활용의 중요성 강조**: 단일 문서 학습을 넘어 다중 홉(Multi-hop) 지식을 학습할 수 있는 인용 네트워크 활용의 가치를 구체화

## How

![Figure 3](figures/fig3.webp)
*LLM이 인용 작업을 개선하는 경로*

**인용 분류(Citation Classification)**
- 인코더 기반 LLM(BERT, SciBERT)을 통한 고품질 표현 추출
- CNN, GBDT 등 다른 ML 모듈과의 하이브리드 결합
- 생성형 LLM(T5, GPT-2)을 활용한 직접 레이블 생성 및 합성 데이터 생성

**인용 기반 요약(Citation-based Summarization)**
- 문서 수준의 특징 추출을 위해 BERT, GPT-2, XLNET 등 활용
- 인용 문장과 참고 논문 문장 간의 의미적 유사성 매칭
- BART-large, PEGASUS-large 등 생성형 모델을 통한 추상 요약

**인용 추천(Citation Recommendation)**
- 인용 맥락의 고품질 표현을 통한 후보 논문 검색 개선
- 인용 네트워크 그래프의 구조 정보 통합
- 다중 뷰 클러스터링 및 의미 유사성 기반 추천

## Originality

- LLM과 인용 분석의 상호 이익 관계를 **최초로 체계적으로 분류**하고 정리한 종합 조사
- 판별형 LLM뿐 아니라 생성형 LLM의 활용(합성 데이터 생성, 직접 생성 기반 분류)을 구체적으로 검토
- 단순 텍스트 표현 개선을 넘어 **인용 네트워크 구조 정보**의 LLM 학습 통합 가능성 제시
- 세 가지 주요 인용 분석 작업(분류, 요약, 추천)을 통합적으로 검토하면서도 각각의 독특한 특성을 구분

## Limitation & Further Study

- **한계**: 논문의 많은 부분이 기술된 초기 단계의 조사이며, 실제 성능 비교 정량 데이터가 제한적임. 인용 데이터를 LLM 사전학습에 통합하는 구체적인 방법론의 실증적 결과가 아직 부족함

- **후속 연구**: 
  - 인용 네트워크를 명시적으로 LLM 사전학습 목표에 통합하는 방법론 개발
  - 다중 언어 및 도메인 특화 인용 분석을 위한 LLM 활용 확대
  - 인용 예측(Citation Prediction)과 LLM 학습의 통합 메커니즘 심화
  - 인용 편향(Citation Bias) 및 인용 검증(Citation Verification) 관련 LLM의 역할 규명

## Evaluation

- **Novelty**: 4/5 — LLM과 인용의 상호 이익 관계를 체계적으로 제시한 최초 조사이나, 개별 기술은 기존 연구의 결합
- **Technical Soundness**: 4/5 — 체계적인 분류와 분석이 견고하나, 실증적 비교 실험이 부재
- **Significance**: 4/5 — 학술 정보 검색, 과학 메트릭, LLM 개선에 중대한 의의가 있으나 실제 응용 검증 필요
- **Clarity**: 5/5 — 명확한 분류 체계(Figure 2)와 체계적인 구성으로 복잡한 주제를 잘 정리
- **Overall**: 4/5

**총평**: 본 논문은 LLM과 인용 분석 간의 상호 이익 관계를 최초로 체계적으로 정리한 중요한 조사 연구이며, 향후 학술 정보 처리 및 LLM 개선 분야에 명확한 연구 방향을 제시한다. 다만 실증적 성과와 정량적 비교가 강화되면 더욱 강력한 기여가 될 수 있을 것으로 예상된다.

## Related Papers

- 🏛 기반 연구: [[papers/020_A_Review_of_Relational_Machine_Learning_for_Knowledge_Graphs/review]] — 지식 그래프와 관계형 머신러닝 기반이 LLM-인용 분석 결합의 이론적 토대를 제공한다.
- 🧪 응용 사례: [[papers/219_Citebart_Learning_to_generate_citations_for_local_citation_r/review]] — 인용 텍스트 생성의 구체적 방법론이 LLM과 인용 분석의 실제 응용 사례를 보여준다.
- 🧪 응용 사례: [[papers/892_A_year_in_review_open_access_at_OUP/review]] — 대규모 언어 모델과 인용 연구가 오픈 액세스 출판물의 인용 패턴 분석에 적용된다.
