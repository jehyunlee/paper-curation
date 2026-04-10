---
title: "953_Do_Large_Language_Models_Reduce_Research_Novelty_Evidence_fr"
authors:
  - "Ali Safari"
date: "2026.03"
doi: ""
arxiv: ""
score: 4.0
essence: "ChatGPT 출시 이후 비영어권 국가 소속 연구자들의 논문이 영어권 연구자들 대비 의미론적 새로움(semantic novelty)이 유의미하게 감소했으며, 이는 LLM이 생산성 향상과 동시에 지적 다양성을 감소시킬 수 있음을 보여준다."
tags:
  - "cat/Scientific_Impact_and_Innovation"
  - "sub/Artificial_intelligence_and_science"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Safari_2026_Do Large Language Models Reduce Research Novelty Evidence from Information Systems Journals.pdf"
---

# Do Large Language Models Reduce Research Novelty? Evidence from Information Systems Journals

> **저자**: Ali Safari | **날짜**: 2026-03-23 | **URL**: [https://arxiv.org/abs/2603.22510v1](https://arxiv.org/abs/2603.22510v1)

---

## Essence

![Figure 2](figures/fig2.webp)

*Figure 2. Event study coefficients for Post x Non-EDA interaction, relative to 2022. Pre-treatment coefficients*

ChatGPT 출시 이후 비영어권 국가 소속 연구자들의 논문이 영어권 연구자들 대비 의미론적 새로움(semantic novelty)이 유의미하게 감소했으며, 이는 LLM이 생산성 향상과 동시에 지적 다양성을 감소시킬 수 있음을 보여준다.

## Motivation

- **Known**: ChatGPT는 전문가들의 생산성을 8-40% 증가시켰으나, 이러한 산출량 증가가 진정한 지적 진전을 의미하는지는 검증되지 않았다. 과학 시스템은 구조적으로 새로운 아이디어를 처벌하고 관습적 연구를 선호한다.
- **Gap**: 기존 연구는 LLM의 생산성 효과만 측정했으나, 산출된 연구의 의미론적 새로움(novelty)이 실제로 변했는지는 실증적으로 규명되지 않았다.
- **Why**: 과학 진보는 출판량이 아닌 새로운 아이디어 결합에 달려 있으므로, LLM이 생산성은 높이되 새로움은 감소시킨다면 지적 정체를 야기할 수 있다.
- **Approach**: 2020-2025년 정보시스템 저널 44개에 게재된 13,847개 논문의 SPECTER2 임베딩을 이용하여 의미론적 새로움을 측정하고, ChatGPT 출시(2022년 11월)를 처치 시점으로 하는 이중차분(difference-in-differences) 설계를 적용했다.

## Achievement

![Figure 3](figures/fig3.webp)

*Figure 3. Mean z-scored novelty by affiliation group and period. Non-EDA authors show higher baseline novelty*

- **이질적 처치 효과 발견**: 비영어권 국가(Non-EDA) 소속 저자들이 영어권 국가(EDA) 저자들 대비 상대적 새로움에서 0.18 표준편차 감소 (beta = -0.176, p < 0.001), 즉 새로움 분포상 7백분위 포인트 하락
- **견고성 검증**: 대체 근처이웃값, 대체 처치시점, COVID 년도 제외, 사전 처치 플라시보 검정 등 모든 강건성 검정에서 결과 유지
- **구성 수준 이론(Construal Level Theory) 적용**: LLM이 심리적 거리 감소(즉시성, 확실성, 노력 감소)를 통해 추상적·탐색적 사고에서 구체적·관습 추종적 실행으로 전환
- **생산성-새로움 트레이드오프 증거**: 생산성 향상과 새로움 감소의 동시 발생 가능성 제시

## How

![Figure 1](figures/fig1.webp)

*Figure 1. Research model. The main path captures the association between LLM availability and semantic novelty,*

- SPECTER2 임베딩 사용: 각 논문을 고차원 벡터로 표현하여 의미론적 유사성 측정
- 코사인 거리(cosine distance) 계산: 각 논문과 가장 가까운 선행 논문들 간 거리를 새로움으로 정의
- 이중차분 설계: Post × Non-EDA 상호작용항으로 처치 효과 추정
- 사건 연구(event study) 사양: 사전 추세 검정으로 평행 추세 가정 검증
- 하위 표본 분석: 출판 연도, 저자 경력, 저널 영향력 등으로 층화 분석

## Originality

- 의미론적 새로움을 LLM 생산성 문헌의 종속변수로 최초 도입
- ChatGPT 출시라는 자연실험을 활용한 인과 추론의 가시성 높음
- 구성 수준 이론을 AI-생산성 논쟁에 명시적으로 연결한 이론적 기여
- 비영어권 저자라는 특정 집단의 이질적 효과 규명으로 LLM 효과의 불평등성 입증

## Limitation & Further Study

- LLM 실제 채택률과 사용 강도를 직접 관찰하지 못함 (제도 변수를 간접 지표로 사용)
- SPECTER2 임베딩이 '새로움'의 유일한 측정법일 수 없으며, 의미론적 거리가 질적 새로움을 완전히 포착하지 못할 가능성", '정보시스템 분야 중심이므로 다른 학문 분야 일반화 가능성 제한
- 구성 수준 이론 메커니즘이 추론(inference)에만 기반하고 직접 검증되지 않음
- **후속 연구**: (1) 문헌 기반 LLM 채택 실제 데이터 수집, (2) 인지 실험을 통한 구성 수준 변화 직접 측정, (3) 다분야·다국가 비교 연구, (4) 새로움의 질적 평가와의 수렴타당도 검증

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 이 논문은 LLM이 생산성을 높이는 동시에 연구의 지적 다양성을 감소시킬 수 있다는 중요한 실증적 증거를 제시하며, 특히 비영어권 저자에게 집중된 효과를 통해 기술 도입의 불평등한 영향을 조명한다. 강력한 연구 설계와 견고한 검정으로 신뢰도가 높으나, 메커니즘의 직접 검증과 분야 간 일반화 가능성 확대가 필요하다.

## Related Papers

- 🔗 후속 연구: [[papers/1021_Scientific_production_in_the_era_of_large_language_models/review]] — 대규모 언어모델 시대의 과학적 생산성 변화를 의미론적 새로움 감소라는 구체적 지표로 확장하여 측정한다.
- 🏛 기반 연구: [[papers/1119_Publish_and_Perish_How_AI-Accelerated_Writing_Without_Propor/review]] — AI 가속화된 글쓰기가 적절한 사고 없이 이루어질 때의 문제점이 연구 새로움 감소의 근본 원인을 설명한다.
- 🏛 기반 연구: [[papers/1077_Quantifying_large_language_model_usage_in_scientific_papers/review]] — LLM이 연구 참신성에 미치는 영향에 대한 실증적 근거를 제공하여 LLM 사용률 측정의 중요성을 뒷받침한다.
- ⚖️ 반론/비판: [[papers/1041_The_Rise_of_Large_Language_Models_and_the_Direction_and_Impa/review]] — LLM이 연구의 참신성을 감소시키는지에 대한 상반된 관점을 제시하여 연방 자금 지원에 미치는 영향을 비판적으로 검토한다.
- ⚖️ 반론/비판: [[papers/1021_Scientific_production_in_the_era_of_large_language_models/review]] — LLM이 연구 생산성을 높이지만 동시에 연구 참신성을 감소시킬 수 있는 상반된 효과를 보여준다.
- ⚖️ 반론/비판: [[papers/1119_Publish_and_Perish_How_AI-Accelerated_Writing_Without_Propor/review]] — LLM이 연구 참신성을 감소시킨다는 발견과 AI 글쓰기 도구의 급속한 확산이 과학적 지식 생산에 미치는 상반된 효과를 보여준다.
- 🔗 후속 연구: [[papers/1113_Definition_and_Value_Reconstruction_of_Human_Creativity_in_t/review]] — 대형 언어모델이 연구 참신성에 미치는 영향을 다루어 AI 시대 창의성 평가의 실증적 근거를 제공한다.
