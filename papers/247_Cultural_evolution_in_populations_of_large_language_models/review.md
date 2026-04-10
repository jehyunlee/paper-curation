---
title: "247_Cultural_evolution_in_populations_of_large_language_models"
authors:
  - "J'érémyPerez"
  - "Corentin Léger"
  - "Marcela Ovando-Tellez"
  - "Chris Foulon"
  - "Joan Dussauld"
date: "2024"
doi: "2403.08882"
arxiv: ""
score: 4.0
essence: "이 논문은 대규모 언어모델(LLM) 인구에서 문화진화를 시뮬레이션하는 프레임워크를 제안하며, 네트워크 구조, 성격, 정보 변환 방식 등 문화진화의 주요 변수들을 조작하면서 기계가 생성하는 문화의 역학을 탐구한다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/Evolutionary_Chemistry_Models"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Perez et al._2024_Cultural evolution in populations of large language models.pdf"
---

# Cultural evolution in populations of large language models

> **저자**: J'érémyPerez, Corentin Léger, Marcela Ovando-Tellez, Chris Foulon, Joan Dussauld, Pierre-Yves Oudeyer, Clément Moulin-Frier | **날짜**: 2024 | **DOI**: [2403.08882](https://arxiv.org/abs/2403.08882)

---

## Essence

![Figure 1](figures/fig1.webp)
*LLM 에이전트들이 네트워크 구조로 조직되어 이웃 에이전트들과 이야기를 교환하며, 각 에이전트는 특정 성격과 프롬프트를 통해 이전 세대의 이야기들을 변환하여 새로운 이야기를 생성한다.*

이 논문은 대규모 언어모델(LLM) 인구에서 문화진화를 시뮬레이션하는 프레임워크를 제안하며, 네트워크 구조, 성격, 정보 변환 방식 등 문화진화의 주요 변수들을 조작하면서 기계가 생성하는 문화의 역학을 탐구한다.

## Motivation

- **Known**: 문화진화 연구는 실험적, 역사적, 계산적 방법으로 문화변화에 대한 인과적 설명을 제공해왔으며, 캘리포니아 학파(유전자-문화 공진화)와 파리 학파(문화흡인이론)는 인구 구조, 전승 편향 등의 효과를 성공적으로 모델화해왔다.

- **Gap**: 진화된 인지메커니즘에 의해 유도되는 사회정보의 변환 효과와 같은 흡인 요소들은 에이전트 기반 모델과 형식 모델로 포착하기 어려워, CAT 기반 연구들이 주로 실험과 역사 데이터 분석에만 의존해왔다.

- **Why**: (1) LLM이 인간 행동을 모방하는 능력으로 인간의 문화 역학을 현실적으로 근사할 수 있고, (2) AI가 점차 문화 창출에 참여함에 따라 '기계 문화(machine culture)'의 역학을 이해하는 것이 중요하다.

- **Approach**: 성격(personality), 초기화 프롬프트, 변환 프롬프트를 조작 가능한 오픈소스 소프트웨어를 개발하여 LLM 인구에서의 언어문화 진화를 시뮬레이션한다.

## Achievement

![Figure 2](figures/fig2.webp)
*50개 에이전트의 직선 전승 체인에서 생성된 텍스트의 진화 시각화: (a) 모든 이야기 간의 의미론적 유사성 행렬, (b) 생성된 이야기들 간의 유사성을 네트워크 그래프로 표현, (c) 각 세대에서 사용된 단어의 변화.*

1. **LLM 기반 문화진화 프레임워크 개발**: 네트워크 구조, 에이전트 성격, 정보 변환 방식을 조작할 수 있는 통합 시뮬레이션 플랫폼 구축

2. **다층적 분석 도구 제공**: 생성 세대 내 유사성, 연속 세대 간 유사성, 초기 세대와의 유사성 측정 및 단어 체인 분석, 유사성 네트워크 시각화 제공

3. **문화진화와 생성AI 연결**: 두 분야 간의 접점을 개척하여 인간 문화진화의 가설 생성과 기계문화의 역학 이해라는 이중 목표 달성

## How

![Figure 3](figures/fig3.webp)
*네트워크 구조의 효과: 10개 에이전트, 10세대 동안 다양한 네트워크 구조(선형, 격자, 완전 연결 등)에서의 문화 역학 비교.*

- **모델 구조**: 각 세대의 LLM 에이전트들이 (1) 초기화 프롬프트로 시작 이야기 생성 → (2) 변환 프롬프트와 이웃 에이전트의 이야기를 입력받아 새 이야기 생성 → (N) 세대를 거쳐 반복

- **성격 메커니즘**: 모든 프롬프트 앞에 성격 서술("당신은 매우 창의적이다")을 추가하여 에이전트의 개별 특성 반영

- **유사성 측정**: TF-IDF 벡터화와 코사인 유사성으로 텍스트 간의 의미론적 유사도 계산

- **시각화 기법**: (1) 단어 체인 분석으로 핵심 단어의 안정성/변화 추적, (2) 네트워크 그래프로 세대 간 진화 궤적 표현

## Originality

- **최초 시도**: 문화진화 이론과 생성AI를 직접 결합한 최초의 통합 시뮬레이션 프레임워크

- **이론적 교량**: 캘리포니아/파리 학파의 개념적 틀을 LLM 에이전트에 적용하여 심리적 메커니즘의 영향을 직접 모델화할 수 있는 경로 제시

- **이중 의의**: 인간 문화진화의 계산적 모델링뿐만 아니라 기계문화의 역학 자체를 연구 대상으로 정립

- **도구 개발**: 학술 접근성을 높인 직관적 인터페이스의 오픈소스 소프트웨어 제공

## Limitation & Further Study

- **예비 결과 성격**: 논문의 실험 결과들이 주로 개념 증명(proof-of-concept) 수준으로, 변수들의 효과를 체계적으로 검증하지 못함

- **모델의 단순화**: LLM의 행동 메커니즘이 인간의 인지 메커니즘과 완전히 동일하지 않아, 인간 문화진화 모델의 타당성 제약

- **프롬프트 의존성**: 초기화/변환 프롬프트 설계가 결과에 미치는 영향에 대한 체계적 분석 부재

- **향후 연구**: (1) 더 큰 규모의 인구/세대 수로 체계적 실험, (2) 실제 인간 실험과의 비교 검증, (3) 다양한 문화 영역(음악, 시각예술 등)으로의 확장, (4) LLM의 편향과 문화 역학의 관계 심화 분석

## Evaluation

- **Novelty**: 4.5/5 — 문화진화와 생성AI의 혁신적 결합이지만, 실험 수준이 예비적임

- **Technical Soundness**: 3.5/5 — 방법론은 타당하나, 대규모 검증 부재 및 LLM-인간 행동 동등성에 대한 검토 필요

- **Significance**: 4/5 — 두 학제 간 새로운 연구 방향을 제시하고 기계문화 연구의 중요성을 강조

- **Clarity**: 4/5 — 전반적으로 명확하나, 기술 세부사항과 이론적 배경 간 균형 개선 여지

- **Overall**: 4/5

**총평**: 이 논문은 문화진화 이론과 생성AI라는 두 분야를 창의적으로 연결하여 기계문화 시대의 새로운 연구 방향을 제시하는 의미 있는 작업이나, 실험적 검증과 대규모 시뮬레이션을 통한 심화가 필요하다.

## Related Papers

- 🔗 후속 연구: [[papers/356_From_individual_to_society_A_survey_on_social_simulation_dri/review]] — LLM 기반 사회 시뮬레이션을 문화진화 관점에서 더 구체적으로 다루며 네트워크 구조와 정보 변환의 역학을 탐구한다.
- 🏛 기반 연구: [[papers/319_Ethnography_and_machine_learning_Synergies_and_new_direction/review]] — 민족지학과 머신러닝의 결합이 LLM 인구에서의 문화진화 연구에 방법론적 기초를 제공한다.
- 🧪 응용 사례: [[papers/838_Training_socially_aligned_language_models_in_simulated_human/review]] — 시뮬레이션된 인간 환경에서 사회적으로 정렬된 언어 모델 훈련이 LLM 문화진화의 실제 적용 사례이다.
- 🧪 응용 사례: [[papers/319_Ethnography_and_machine_learning_Synergies_and_new_direction/review]] — 민족지학적 현장 연구 방법론이 LLM 인구의 문화진화 시뮬레이션에서 사회 역학 분석에 직접 적용될 수 있다.
- 🏛 기반 연구: [[papers/356_From_individual_to_society_A_survey_on_social_simulation_dri/review]] — LLM 인구의 문화진화가 개별 에이전트부터 사회 전체까지의 다층적 시뮬레이션 체계의 이론적 기반을 제공한다.
- 🏛 기반 연구: [[papers/460_Language_models_surface_the_unwritten_code_of_science_and_so/review]] — 대규모 언어모델 집단에서의 문화적 진화 연구가 과학과 사회의 불문율을 드러내는 LLM 활용의 이론적 배경을 제공함
- 🏛 기반 연구: [[papers/301_Economic_anthropology_in_the_era_of_generative_artificial_in/review]] — 대규모 언어모델에서 문화적 진화의 기초적 이해를 제공한다
