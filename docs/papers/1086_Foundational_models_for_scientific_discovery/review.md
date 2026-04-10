---
title: "1086_Foundational_models_for_scientific_discovery"
authors:
  - "Vanessa López"
  - "Lam Thanh Hoang"
  - "Marcos Martinez-Galindo"
  - "Raúl Fernández-Díaz"
  - "Marco Luca Sbodio"
date: ""
doi: "N/A"
arxiv: ""
score: 4.0
essence: "본 논문은 과학적 가설 생성(hypothesis generation)을 위한 대규모 언어 모델(LLM) 활용에 대한 종합적 설문 논문으로, 기존 방법론부터 LLM 기반 접근법까지의 분류 체계(taxonomy)를 제시한다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Biological_Foundation_Models"
  - "topic/ai4s"
---

# Foundational models for scientific discovery

> **저자**: Vanessa López, Lam Thanh Hoang, Marcos Martinez-Galindo, Raúl Fernández-Díaz, Marco Luca Sbodio, Rodrigo Ordóñez-Hurtado, Mykhaylo Zayats, Natasha Mulligan, Joao H. Bettencourt‐Silva | **날짜**:  | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: Taxonomy of Methods for Scientiﬁc Hypothesis Generation (SHG).*

본 논문은 과학적 가설 생성(hypothesis generation)을 위한 대규모 언어 모델(LLM) 활용에 대한 종합적 설문 논문으로, 기존 방법론부터 LLM 기반 접근법까지의 분류 체계(taxonomy)를 제시한다.

## Motivation

- **Known**: 과학적 가설 생성은 과학 발견의 핵심 단계이며, 전통적으로 인간의 직관과 도메인 전문성에 의존해왔다. 문헌 기반 발견(LBD)과 같은 계산적 접근법들이 기존에 존재했다.
- **Gap**: 과학 문헌의 폭발적 증가로 인한 정보 과부하와 학문 간 단편화로 인해 인간 연구자들이 가설 생성에 어려움을 겪고 있으며, LLM 기반 방법의 체계적 분류와 평가 전략이 부족하다.
- **Why**: LLM은 대규모 과학 텍스트를 처리하여 새로운 가설을 생성할 잠재력을 가지고 있으며, 이를 체계적으로 이해하는 것이 과학적 발견의 자동화 및 가속화에 필수적이다.
- **Approach**: 체계적 문헌 검색(arXiv API 활용, 2005-2025년)을 통해 관련 논문을 수집하고, 인간 중심 방법부터 LLM 기반 방법까지 발전 단계별로 분류하여 종합적 분석을 수행한다.

## Achievement

![Figure 1](figures/fig1.webp)

*Figure 1: Taxonomy of Methods for Scientiﬁc Hypothesis Generation (SHG).*

- **가설 생성 방법론의 분류 체계**: 인간 중심, LBD(Literature-Based Discovery), 텍스트 마이닝, 지도학습, 그래프 기반, LLM 기반 방법을 포함한 체계적 분류 제시
- **LLM 기반 접근법의 세부 분석**: Prompting, Fine-Tuning, RAG(Retrieval-Augmented Generation), Knowledge Graph 기반 방법 등 다양한 기법 검토
- **가설 품질 개선 기법**: 새로움 부스팅(novelty boosting)과 구조화된 추론(structured reasoning) 등 가설의 질적 향상 방법 분석
- **평가 전략 개요**: 가설의 새로움, 관련성, 실현가능성, 중요도, 명확성 평가 방법 제시

## How

![Figure 1](figures/fig1.webp)

*Figure 1: Taxonomy of Methods for Scientiﬁc Hypothesis Generation (SHG).*

- arXiv API를 이용한 체계적 문헌 검색(cs.CL 범주, 검색어 기반 및 수동 큐레이션)
- 제목과 초록 기반 1차 필터링 후 수동 스크리닝을 통한 관련성 검증
- 방법론적 패러다임(LBD, NLP, LLM, 하이브리드), 과학 도메인(생의학, 천체물리학, 화학), 가설 표현 방식별 분류
- 시간에 따른 기술 진화와 방법론 전환 양상 추적 및 분석
- 기존 방법(ARROWSMITH, MOLIERE, KnIT, DiseaseConnect 등)의 상세 검토

## Originality

- LLM 시대 가설 생성에 대한 최초의 포괄적 설문 논문으로, 계산적 접근의 전체 역사적 발전 과정을 통합적으로 다룸
- 기존 방법(LBD, 텍스트 마이닝)과 최신 LLM 기반 방법을 단계적 분류 체계로 통합
- 다양한 과학 도메인과 실제 사례(e.g., fish oil-Raynaud's syndrome)를 통한 구체적 검증", '혁신적 가설 생성과 기존 지식 재구성의 구분, 훈련 데이터 편향 문제 등 심층적 도전 과제 분석

## Limitation & Further Study

- **시간적 한계**: 2025년 4월 현재 진행 중인 작업으로 LLM 기술의 급속한 발전 속도를 완전히 반영하지 못할 가능성
- **평가 기준의 모호성**: 가설의 '새로움'과 '타당성'을 정량적으로 평가하는 표준화된 메트릭 부재", '**도메인 편향**: 생의학 분야 사례가 과도하게 많아 다른 과학 분야(물리학, 지구과학 등)의 대표성 부족
- **실제 검증 부족**: 대부분이 사전 학습 자료이므로 실제 과학적 발견으로 검증된 사례의 제한적 포함
- **후속 연구**: (1) 다중모달(multimodal) 입력 통합, (2) 인간-AI 협력 프레임워크 개발, (3) 도메인 특화 평가 메트릭 수립, (4) 장기 검증 연구 설계 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 과학적 가설 생성의 진화 과정을 포괄적으로 정리하고 LLM 시대의 새로운 기회와 도전을 체계적으로 분석한 중요한 설문 논문이다. 다만 실제 사례 검증과 정량화된 평가 메트릭 개발이 향후 보완되어야 할 주요 과제로 남아있다.

## Related Papers

- 🏛 기반 연구: [[papers/343_Foundation_models_for_materials_discovery__current_state_and/review]] — 재료 발견을 위한 파운데이션 모델의 현재 상태와 미래 전망의 이론적 토대를 제공한다.
- 🔗 후속 연구: [[papers/342_Foundation_Models_for_Environmental_Science_A_Survey_of_Emer/review]] — 환경과학 분야 파운데이션 모델로 과학적 발견 모델을 확장한다.
