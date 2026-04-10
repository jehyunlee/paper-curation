---
title: "319_Ethnography_and_machine_learning_Synergies_and_new_direction"
authors:
  - "Corey M. Abramson"
  - "Zhuofan Li"
date: "2025"
doi: "10.1093/oxfordhb/9780197653609.013.36"
arxiv: ""
score: 4.0
essence: "민족지학적 현장 연구와 기계학습(ML)은 각각 현대 사회과학의 핵심 도구이지만 실제로는 분리되어 있었으며, 본 논문은 이 두 방법론을 결합하여 대규모 비교 연구에서 상승효과를 창출할 수 있음을 주장한다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/Multi-Hop_Reasoning_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Abramson and Li_2024_Ethnography and machine learning Synergies and new directions.pdf"
---

# Ethnography and Machine Learning: Synergies and New Directions

> **저자**: Corey M. Abramson, Zhuofan Li | **날짜**: 2025 | **DOI**: [10.1093/oxfordhb/9780197653609.013.36](https://doi.org/10.1093/oxfordhb/9780197653609.013.36)

---

## Essence

민족지학적 현장 연구와 기계학습(ML)은 각각 현대 사회과학의 핵심 도구이지만 실제로는 분리되어 있었으며, 본 논문은 이 두 방법론을 결합하여 대규모 비교 연구에서 상승효과를 창출할 수 있음을 주장한다.

## Motivation

- **Known**: 민족지학(ethnography)은 사람들이 자신의 삶의 맥락을 이해하고 탐색하며 형성하는 방식을 조명하는 사회과학 방법론이며, 기계학습은 빅데이터와 통계 학습 모델을 활용한 계산 기법이다.

- **Gap**: 두 방법론의 상보성에도 불구하고 실제 연구 실무에서는 주로 분리되어 사용되어 왔으며, 특히 반구조화된 텍스트 데이터 분석 시 해석적 깊이를 유지하면서 규모를 확대하는 방법이 부족했다.

- **Why**: (a) 계산사회과학(computational social science) 도구의 확장, (b) 계산 기능을 통합한 팀 기반 민족지 연구의 증가, (c) 질적 데이터 저장소의 성장으로 인해 두 방법론 결합의 필요성이 증대되었다.

- **Approach**: 민족지학과 ML의 개념적 기초를 검토하고, 결합 방식의 가치와 과제를 논의하며, 대규모 프로젝트의 실제 워크플로우 사례를 제시하고, 두 방법론의 생산적 공진화(coevolution)를 위한 로드맵을 제공한다.

## Achievement

![Figure 14.1: Ethnography와 ML의 중첩 영역을 나타내는 벤 다이어그램](figures/fig14_1.webp)
*민족지학과 기계학습 간의 반복성, 규모성, 맥락성의 중첩 관계*

1. **세 가지 핵심 시너지 규명**: 반복성(iteration), 규모성(scale), 맥락성(context)의 영역에서 두 방법론의 중첩을 명확히 했다. ML은 반복과 확장에 강점이 있고, 민족지학은 맥락 이해에 깊이가 있으므로 보완적 관계를 형성한다.

2. **계산 민족지학(computational ethnography)의 체계화**: 디지털 민족지학과 구분되는 새로운 연구 경향을 정의하고, 민족지학 방법으로 생성된 데이터에 ML 도구를 적용하는 접근법을 제시했다.

3. **다양한 적용 가능성의 제시**: 현장 관찰, 심층 인터뷰, 필드노트 작성, 텍스트 코딩, 패턴 탐색, 발견 사항 표현 등 민족지학 연구의 핵심 실무 과제 전 단계에서 ML 활용 가능성을 제안했다.

## How

| 연구 단계 | ML의 활용 방식 |
|---------|-------------|
| **연구 설계** | 선행 문헌 분석, 사이트 선정 최적화 |
| **관찰 및 기록** | 필드노트 디지털화 및 자동 정리 |
| **인터뷰 및 전사** | 음성-텍스트 변환(speech-to-text) 자동화 |
| **패턴 탐색** | 주제 모델링(topic modeling), 자동 범주 발견 |
| **텍스트 코딩** | 반자동 코딩(semi-automatic coding), 코드 추천 |
| **메모 작성** | 자동화된 분석 메모 생성 지원 |
| **발견 사항 표현** | 패턴 시각화, 대규모 비교 가능 |

**방법론적 특징**:
- 자연어처리(NLP)와 대규모 언어모델(LLM)을 민족지 데이터에 적용
- 정성적 해석과 정량적 패턴 인식의 통합
- 팀 기반 연구에서 코딩 표준화 및 효율화
- '스케일 업(scale up)' 필드 메서드와 '스케일 다운(scale down)' 빅데이터의 수렴

## Originality

- **전통적 이분법 극복**: 정성/정량, 사례/표본, 깊이/규모의 이분법적 대립을 해결하는 실용적 통합 방안을 제시했다.

- **다중 전통 포용**: 근거이론(grounded theory), 확장된 사례 방법(extended case method), 후기 실증주의적 현실주의(post-positivist realism) 등 다양한 민족지 전통에 걸쳐 ML 통합의 가능성을 논의했다.

- **생태적 타당성과 알고리즘 편향 해결**: ML의 맥락성 한계를 민족지 방법으로 보완하여 '생태적 타당성(ecological validity)'을 증진하고 '알고리즘 편향(algorithmic bias)' 우려를 완화하는 방안을 제안했다.

- **메서드 다원주의**: 기존의 방법론적 편향성을 초월하여 질적 사회학, 민족지학, 하이브리드 텍스트 분석에 기여하는 방법론 다원주의적 입장을 취했다.

## Limitation & Further Study

- **명시적 보수성**: 논문은 프리프린트 버전으로 구체적인 실제 사례 워크플로우와 정량적 성과 측정이 약화되어 있으며, 다양한 프로젝트의 실행 경험이 충분히 상세히 제시되지 않았다.

- **기술적 깊이의 부재**: ML 기법의 구체적 적용 방식(알고리즘 선택, 하이퍼파라미터 설정, 성능 평가 메트릭 등)에 대한 기술적 논의가 제한적이다.

- **맥락성 문제의 미해결**: 민족지 연구의 풍부한 맥락을 ML 모델에 어떻게 인코딩하고 유지할 것인가에 대한 구체적 기술적 해결책은 여전히 미흡하다.

- **향후 연구 방향**:
  - 구체적 프로젝트별 성공 사례와 실패 사례의 비교 분석
  - ML 도구가 연구 해석의 자율성이나 신뢰성을 침해하는 방식에 대한 비판적 검토
  - 대규모 팀 연구에서 해석적 일관성 유지 메커니즘 개발
  - 문화적 맥락이 상이한 지역 간 비교 연구에서의 ML 적용 방안


## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 민족지학과 기계학습의 상보성을 체계적으로 분석하고 실용적 통합 방안을 제시하여 방법론 다원주의를 선도하는 중요한 기여를 하고 있으나, 구체적 기술 구현과 대규모 프로젝트 사례의 상세한 제시를 통해 설득력을 더욱 강화할 필요가 있다.

## Related Papers

- 🧪 응용 사례: [[papers/247_Cultural_evolution_in_populations_of_large_language_models/review]] — 민족지학적 현장 연구 방법론이 LLM 인구의 문화진화 시뮬레이션에서 사회 역학 분석에 직접 적용될 수 있다.
- 🏛 기반 연구: [[papers/356_From_individual_to_society_A_survey_on_social_simulation_dri/review]] — 사회과학 방법론의 통합이 LLM 기반 사회 시뮬레이션의 개인-사회 다층 분석에 이론적 토대를 제공한다.
- 🔗 후속 연구: [[papers/173_Bridging_social_psychology_and_llm_reasoning_Conflict-aware/review]] — 사회심리학과 LLM 추론의 결합이 민족지학과 머신러닝 융합의 구체적인 확장 사례이다.
- 🏛 기반 연구: [[papers/247_Cultural_evolution_in_populations_of_large_language_models/review]] — 민족지학과 머신러닝의 결합이 LLM 인구에서의 문화진화 연구에 방법론적 기초를 제공한다.
- 🧪 응용 사례: [[papers/356_From_individual_to_society_A_survey_on_social_simulation_dri/review]] — 민족지학과 머신러닝의 결합된 방법론이 사회 시뮬레이션에서 현실적인 인간 행동 모델링에 적용된다.
- 🔗 후속 연구: [[papers/301_Economic_anthropology_in_the_era_of_generative_artificial_in/review]] — 기계학습과 민족지학의 시너지를 경제 인류학적 관점에서 생성형 AI에 적용한다
