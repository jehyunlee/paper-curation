---
title: "718_Scientific_discovery_in_the_age_of_artificial_intelligence"
authors:
  - "Hanchen Wang"
  - "Tianfan Fu"
  - "Yuanqi Du"
  - "Wenhao Gao"
  - "Kexin Huang"
date: "2023"
doi: "10.1038/s41586-023-06221-2"
arxiv: ""
score: 4.5
essence: "본 리뷰 논문은 자기지도학습(self-supervised learning), 기하 심층학습(geometric deep learning), 생성형 AI 등 최근 10년간의 주요 AI 기술을 통해 과학적 발견이 어떻게 변모하고 있는지 종합적으로 조망한다. AI는 대규모 데이터셋 통합, 가설 탐색, 실험 설계 자동화 등을 통해 전통적 과학방법론만으로는 불가능한 새로운 과학적 통찰을 제공할 수 있다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Scientific_Agent_Frameworks"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wang et al._2023_Scientific discovery in the age of artificial intelligence.pdf"
---

# Scientific discovery in the age of artificial intelligence

> **저자**: Hanchen Wang, Tianfan Fu, Yuanqi Du, Wenhao Gao, Kexin Huang, Ziming Liu, Payal Chandak, Shengchao Liu, Peter Van Katwyk, Andreea Deac, Anima Anandkumar, Karianne Bergen, Carla P. Gomes, Shirley Ho, Pushmeet Kohli, Joan Lasenby, Jure Leskovec, Tie-Yan Liu, Arjun Manrai, Debora Marks | **날짜**: 2023 | **DOI**: [10.1038/s41586-023-06221-2](https://doi.org/10.1038/s41586-023-06221-2)

---

## Essence

![Figure 1](figures/fig1.webp) *과학적 발견의 다단계 프로세스에서 AI의 역할: 가설 형성, 실험 설계, 데이터 수집 및 분석 단계 전반에 걸친 AI 통합*

본 리뷰 논문은 자기지도학습(self-supervised learning), 기하 심층학습(geometric deep learning), 생성형 AI 등 최근 10년간의 주요 AI 기술을 통해 과학적 발견이 어떻게 변모하고 있는지 종합적으로 조망한다. AI는 대규모 데이터셋 통합, 가설 탐색, 실험 설계 자동화 등을 통해 전통적 과학방법론만으로는 불가능한 새로운 과학적 통찰을 제공할 수 있다.

## Motivation

- **Known**: 2010년대 초 심층학습(deep learning)의 부상 이후 과학 데이터 분석의 범위와 야망이 크게 확대되었으며, 마이크로스코프와 같은 물리적 도구부터 부트스트래핑 같은 통계 기법까지 과학 도구가 지속적으로 진화해왔다.

- **Gap**: AI와 과학의 융합은 새로운 가능성을 제시하지만, 막대한 가설 공간 탐색의 어려움(예: 약물 유사 분자 10^60개), 신뢰할 수 있는 주석 데이터셋 확보의 어려움, 데이터 품질 및 관리 문제 등 구조적 한계가 존재한다.

- **Why**: 입자 충돌 실험에서 초당 100TB 이상의 데이터가 생성되는 등 현대 과학은 기존 컴퓨팅 방식으로 처리 불가능한 규모의 데이터를 다루고 있으며, AI는 이러한 도전에 대응하고 과학적 워크플로우를 근본적으로 혁신할 수 있는 도구이다.

- **Approach**: 자기지도학습, 기하 심층학습, 생성형 AI, 강화학습 등 다양한 AI 기법의 원리를 설명하고, 데이터 수집/큐레이션, 표현 학습, 가설 생성, 실험 통합 등 과학 프로세스의 각 단계에서의 구체적 응용사례를 제시한다.

## Achievement

![Figure 1](figures/fig1.webp) *AI4Science의 다층적 응용 영역: 입자 충돌에서의 희귀사건 선별부터 단백질 구조 예측, 화학 합성 경로 계획, 기상 예측까지 다양한 과학 분야에서의 AI 활용*

1. **AI의 다단계 과학 프로세스 통합**: 가설 형성에서 실험 설계, 데이터 수집·분석·해석에 이르기까지 과학적 발견의 전 단계에서 AI가 인간의 역량을 증강(augment)하고 가속화(accelerate)할 수 있음을 입증

2. **주요 기술 혁신의 체계적 분석**: 
   - 자기지도학습: 라벨이 없는 대규모 데이터로부터 전이 가능한 표현 학습
   - 기하 심층학습: 물리 법칙, 분자 기하학 등 과학적 구조를 모델에 인코딩
   - 생성형 AI: 소분자 약물, 단백질 등 새로운 설계 자동 생성

3. **구체적 성공사례**: 50년 묵은 단백질 폴딩 문제 해결, 백만 개 입자 분자 시뮬레이션, 비지도 언어 모델을 통한 주기율표와 미래 물질 발견 예측 등

## How

![Figure 2](figures/fig2.webp) *과학 데이터의 의미 있는 표현 학습: (a) 기하 심층학습이 분자 구조와 같은 과학적 구조 정보를 어떻게 활용하는지*

- **데이터 선별(Data Selection)**: 비지도 이상 탐지(unsupervised anomaly detection)를 통해 입자 물리학의 배경 신호에서 희귀 현상을 실시간 감지·선별 (99.99% 데이터 폐기 필요)

- **데이터 주석(Data Annotation)**: 의사 라벨링(pseudo-labelling)과 라벨 전파(label propagation)로 작은 크기의 주석 데이터셋으로부터 대규모 미주석 데이터셋 자동 주석

- **귀납적 편향(Inductive Bias) 활용**: 물리 법칙, 분자 구조 원리, 단백질 결합 원리 등 과학적 지식을 수학적 제약으로 모델에 통합하여 필요 학습 데이터 감소 및 일반화 성능 향상

- **표현 학습**: 다층 신경망으로부터 복합 과학 문제를 동시에 해결할 수 있는 본질적이고 압축된 특징(compact features) 학습

- **강화학습**: 다양한 시나리오 탐색을 통해 실험 설계의 정보 이득(information gain)을 최대화하는 최적 전략 발견

## Originality

- **포괄적 통합 관점**: Nature 리뷰로서 AI4Science의 현황을 개별 기술 수준을 넘어 과학 프로세스 전체 맥락에서 종합적으로 분석한 첫 체계적 접근

- **다학제적 적용 사례**: 물리학(입자 충돌), 생물학(단백질 구조), 화학(합성 경로), 기후과학(날씨 예측), 천문학(이상치 탐지) 등 광범위한 분야의 구체적 사례 제시

- **이론과 실무의 연결**: 자기지도학습, 기하 심층학습 등 이론적 토대와 함께 현실의 데이터 품질 문제, 주석 부족, 가설 공간 탐색의 실질적 한계를 균형있게 논의

- **AI의 한계와 과제의 명확화**: 단순 도구론적 낙관주의를 지양하고, 신뢰성 있는 주석 데이터셋 확보, 데이터 관리, 모델 불확실성 정량화 등 해결해야 할 근본적 도전과제 제시

## Limitation & Further Study

- **해결되지 않은 문제들**:
  - 막대한 가설 공간(예: 약물 유사 분자 10^60개) 체계적 탐색의 계산적 불가능성
  - 신뢰할 수 있는 주석 데이터셋 확보의 시간·비용 부담
  - 데이터 품질 및 큐레이션 기준의 부재로 인한 모델 편향(bias) 위험
  - AI 예측의 불확실성 정량화 및 신뢰도 평가 방법론 미흡

- **필요한 향후 연구 방향**:
  - 과학적 지식을 모델에 더 효과적으로 인코딩할 수 있는 귀납적 편향 설계
  - 저자원 환경에서도 작동하는 자기지도학습 및 전이학습 기법 고도화
  - 모델 해석 가능성(interpretability) 강화로 과학적 발견의 신뢰성 확보
  - AI의 오용(misuse) 방지 및 윤리적 가이드라인 개발
  - 학제 간 소통을 촉진하는 AI4Science 인프라 및 표준화

## Evaluation

- **Novelty (독창성)**: 4.5/5 - AI4Science를 포괄적으로 다룬 첫 Nature 리뷰로서 개별 기술의 창신성보다는 통합적 관점의 새로움이 높음

- **Technical Soundness (기술적 타당성)**: 4/5 - 구체적 기술 설명이 정확하나, 일부 과제(예: 가설 공간 탐색 방법론)에 대한 수학적 깊이는 제한적

- **Significance (중요도)**: 5/5 - 향후 과학 연구 패러다임의 근본적 변화를 예고하는 매우 중요한 주제이며, 다학제적 연구자들에게 방향 제시

- **Clarity (명확성)**: 4.5/5 - 복잡한 AI 기법을 일반 과학자 수준에서 이해 가능하도록 설명했으나, Box 1 (기술 개요)에 대한 의존도가 높음

- **Overall (종합)**: 4.5/5

**총평**: 본 논문은 AI와 과학의 융합이라는 시대적 화두를 Nature라는 최고 권위의 플랫폼에서 다학제적 전문가 30여 명이 체계적으로 조망한 획기적 리뷰이다. 기술적 혁신과 함께 현실적 한계와 미해결 과제를 균형있게 제시함으로써 AI4Science 생태계의 건전한 발전을 위한 나침반 역할을 한다.

## Related Papers

- 🏛 기반 연구: [[papers/403_Highly_accurate_protein_structure_prediction_with_AlphaFold/review]] — AlphaFold와 같은 획기적 성과들이 AI를 통한 과학적 발견 변모에 대한 종합적 조망의 대표적 사례로 제시된다
- 🏛 기반 연구: [[papers/105_Artificial_Intelligence_for_Direct_Prediction_of_Molecular_D/review]] — AI4Science의 핵심 기술인 자기지도학습과 기하 심층학습이 과학적 발견 방법론 변화의 구체적인 기술적 토대를 제공한다
- ⚖️ 반론/비판: [[papers/252_Data_integrity_in_materials_science_in_the_era_of_AI_balanci/review]] — AI를 통한 과학적 발견의 긍정적 전망에 대해 데이터 무결성 위협이라는 중요한 위험 요소와 한계를 제시한다
- 🔗 후속 연구: [[papers/795_The_AI_Scientist_Towards_Fully_Automated_Open-Ended_Scientif/review]] — AI를 통한 과학적 발견의 일반적 조망이 완전 자동화된 AI 과학자 시스템의 구체적 구현으로 발전했다
- 🔗 후속 연구: [[papers/506_LLM4SR_A_Survey_on_Large_Language_Models_for_Scientific_Rese/review]] — 과학 연구의 LLM 활용이 AI 시대의 과학적 발견으로 확장됩니다.
- 🏛 기반 연구: [[papers/403_Highly_accurate_protein_structure_prediction_with_AlphaFold/review]] — 단백질 폴딩 문제 해결이 AI를 통한 과학적 발견의 대표적 성공사례로서 AI4Science 발전의 이정표가 되었다
- 🏛 기반 연구: [[papers/105_Artificial_Intelligence_for_Direct_Prediction_of_Molecular_D/review]] — 양자역학부터 연속체까지 물리 시스템의 AI 적용에 대한 종합적 기술 리뷰가 AI를 통한 과학적 발견의 이론적 기반을 제공한다
- ⚖️ 반론/비판: [[papers/252_Data_integrity_in_materials_science_in_the_era_of_AI_balanci/review]] — AI 생성 데이터의 무결성 위협에 대한 경고가 AI를 통한 과학적 발견의 낙관적 전망에 대한 중요한 반성적 관점을 제공한다
- 🏛 기반 연구: [[papers/088_AI4Research_A_Survey_of_Artificial_Intelligence_for_Scientif/review]] — AI 시대 과학 발견의 전반적 맥락을 제공하여 AI4Research의 이론적 토대를 구성한다
- 🏛 기반 연구: [[papers/075_AI_for_Science_2025/review]] — 인공지능 시대 과학적 발견의 이론적 토대를 제공한다.
- 🏛 기반 연구: [[papers/056_Advancing_the_scientific_method_with_large_language_models_F/review]] — 인공지능 시대 과학적 발견에 대한 일반론이 LLM 기반 과학 방법론 변화의 이론적 토대를 제공한다.
- 🏛 기반 연구: [[papers/764_Sparks_Multi-Agent_Artificial_Intelligence_Model_Discovers_P/review]] — AI 시대 과학 발견의 이론적 전망과 실제 구현 사례 간의 연결고리를 제공한다.
- 🔗 후속 연구: [[papers/828_Towards_end-to-end_automation_of_AI_research/review]] — AI 시대 과학 발견의 이론적 가능성을 실제 작동하는 자동화 시스템으로 구현하여 실증적 증거를 제공한다.
- 🔄 다른 접근: [[papers/895_AI_will_transform_science__now_researchers_must_tame_it/review]] — 과학 발견에서 AI 역할을 다른 관점에서 조명하여 보완적 시각을 제공한다
