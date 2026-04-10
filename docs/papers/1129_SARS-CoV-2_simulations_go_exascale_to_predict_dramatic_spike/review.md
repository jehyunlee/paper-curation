---
title: "1129_SARS-CoV-2_simulations_go_exascale_to_predict_dramatic_spike"
authors:
  - "Maxwell I. Zimmerman"
  - "Justin R. Porter"
  - "Michael D. Ward"
  - "Sukrit Singh"
  - "Neha Vithani"
date: "2021.07"
doi: "10.1038/s41557-021-00707-0"
arxiv: ""
score: 5.0
essence: "Folding@home 분산 컴퓨팅 플랫폼으로 exascale 수준의 계산 자원을 확보하여 SARS-CoV-2 바이러스 단백질의 전체 구조 앙상블(structural ensemble)을 밀리초 단위로 시뮬레이션하고, 스파이크 단백질의 극단적 개방 현상과 약물 타겟이 될 수 있는 '숨겨진 포켓(cryptic pockets)'을 예측했다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Protein-Drug_Design_Models"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zimmerman et al._2021_SARS-CoV-2 simulations go exascale to predict dramatic spike opening and cryptic pockets across the.pdf"
---

# SARS-CoV-2 simulations go exascale to predict dramatic spike opening and cryptic pockets across the proteome

> **저자**: Maxwell I. Zimmerman, Justin R. Porter, Michael D. Ward, Sukrit Singh, Neha Vithani, Artur Meller, Upasana L. Mallimadugula, Catherine E. Kuhn, Jonathan H. Borowsky, Rafal P. Wiewiora, Matthew F. D. Hurley, Aoife M. Harbison, Carl A. Fogarty, Joseph E. Coffland, Elisa Fadda, Vincent A. Voelz, John D. Chodera, Gregory R. Bowman | **날짜**: 07/2021 | **DOI**: [10.1038/s41557-021-00707-0](https://doi.org/10.1038/s41557-021-00707-0)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1 | Summary of Folding@home’s computational power. a, The growth of Folding@home in response to COVID-19. The cumul*

Folding@home 분산 컴퓨팅 플랫폼으로 exascale 수준의 계산 자원을 확보하여 SARS-CoV-2 바이러스 단백질의 전체 구조 앙상블(structural ensemble)을 밀리초 단위로 시뮬레이션하고, 스파이크 단백질의 극단적 개방 현상과 약물 타겟이 될 수 있는 '숨겨진 포켓(cryptic pockets)'을 예측했다.

## Motivation

- **Known**: SARS-CoV-2 스파이크 단백질은 감염 시작에 필수적인 구조 변화를 겪으며, 폐쇄된 구조로 면역 회피 전략을 사용한다. 기존 구조 생물학 연구들은 정적인 단백질 스냅샷을 제공했지만 생물학적으로 중요한 동적 과정을 충분히 포착하지 못했다.
- **Gap**: 분자동역학 시뮬레이션(molecular dynamics simulation)은 단백질의 전체 구조 앙상블을 포착할 수 있지만 생물학적으로 관련된 느린 시간 스케일(millisecond timescale)의 과정을 관찰하려면 엄청난 계산 자원이 필요하며, SARS-CoV-2의 모든 관련 단백질을 시뮬레이션하는 것은 기술적으로 불가능했다.
- **Why**: 스파이크 단백질의 동적 구조 변화와 숨겨진 약물 결합 위치를 파악하면 COVID-19 치료제 및 백신 개발을 크게 가속화할 수 있으며, 바이러스의 감염 메커니즘과 면역 회피 전략을 이해하는 데 필수적이다.
- **Approach**: 100만 명 이상의 시민 과학자가 자신의 컴퓨터 자원을 기부하는 Folding@home 분산 컴퓨팅 플랫폼을 활용하여 총 0.1초의 시뮬레이션 데이터를 생성하고, FAST(goal-oriented adaptive sampling) 알고리즘을 적용하여 마르코프 상태 모델(Markov state model)을 구축했다.

## Achievement

![Figure 2](figures/fig2.webp)

*Fig. 2 | Structural characterization of spike opening and conformational masking for three spike homologues. a, An examp*

- **Exascale 컴퓨팅 달성**: 피크 성능 1.01 exaflops(28만 개 GPU와 480만 개 CPU 코어 활용)으로 당시 세계 최고 성능 슈퍼컴퓨터 Summit의 5배 이상 성능 달성
- **스파이크 단백질의 극단적 개방 현상 발견**: 기존 실험에서 보지 못한 수준의 스파이크 개방을 예측, 수용체-결합 영역(RBD)의 접근성과 숨겨진 항원 에피토프(cryptic epitopes) 존재 규명
- **50개 이상의 암호화된 포켓(cryptic pockets) 발견**: 정적 구조 스냅샷에서는 보이지 않지만 동적 시뮬레이션에서 드러나는 항바이러스제 설계의 새로운 약물 표적 제시
- **정량적 단백질 구조 지도 작성**: 2dozen(약 25개) 이상의 SARS-CoV-2 관련 단백질과 복합체에 대한 밀리초 단위의 시뮬레이션 데이터로부터 구조 앙상블 맵 구축
- **오픈 사이언스 원칙 준수**: 모든 데이터와 모델을 공개 저장소(covid.molssi.org, osf.io)에 제공하여 전 세계 연구자의 신약 개발 가속화

## How

![Figure 1](figures/fig1.webp)

*Fig. 1 | Summary of Folding@home’s computational power. a, The growth of Folding@home in response to COVID-19. The cumul*

- Folding@home 플랫폼: 분산 컴퓨팅을 통한 대규모 병렬 처리로 개별 연구기관이 불가능한 계산 규모 달성
- FAST(Feedback-Adaptive Sampling and Training) 알고리즘: 목표 지향적(goal-oriented) 적응형 샘플링으로 관심 구조(스파이크 개방)를 효율적으로 탐색하면서 구조 공간의 광범위한 탐색 균형 유지
- 마르코프 상태 모델(MSM) 구축: 반복 시뮬레이션 배치에서 생성된 데이터로부터 구조 상태 공간의 정량적 지도 작성
- 다양한 초기 구조 활용: FAST로 획득한 분산된 구조들을 Folding@home의 광범위한 시뮬레이션의 시작점으로 사용하여 통계적으로 견고한 최종 모델 생성
- 실험 검증: 크라이오-EM(cryo-EM) 구조, 생화학적 데이터 등 다양한 실험 관찰로 시뮬레이션 결과 지지

## Originality

- **분산 컴퓨팅의 혁신적 규모 확대**: 일반 시민의 컴퓨터 자원을 활용하여 전통 슈퍼컴퓨터를 능가하는 exascale 성능 달성 (당시 기술적으로 혁신적)
- **동적 구조 예측 방법론의 고도화**: FAST 알고리즘을 대규모 분산 컴퓨팅과 결합하여 이전에 관찰 불가능했던 느린 동역학 과정 포착
- **암호화된 포켓의 체계적 발견**: 동적 시뮬레이션을 통해 정적 구조에서 숨겨진 약물 결합 위치 50개 이상 예측하는 새로운 약물 개발 전략 제시
- **실시간 팬데믹 대응**: COVID-19 팬데믹 중 신속하게 연구 방향을 전환하여 공중 보건에 직접 기여하는 과학 수행
- **완전한 오픈 데이터 공유**: 모든 원본 데이터와 모델을 공개하여 전 세계 연구자가 즉시 접근 가능한 표준 설정

## Limitation & Further Study

- **시간 스케일 한계**: 밀리초 단위의 시뮬레이션도 일부 생물학적 과정(예: 바이러스 입자 조립)이 일어나는 초 단위 이상의 현상을 직접 포착하지 못함
- **모델 검증의 제한성**: 일부 예측된 구조와 동역학 과정에 대한 직접적인 실험 검증(예: 특정 cryptic pocket의 약물 결합)이 논문 게시 시점에는 부족함
- **다른 변이형에 대한 제한된 분석**: 논문 작성 당시 알파, 델타 등 주요 변이형에 대한 광범위한 비교 분석은 제한적
- **후속 연구 방향**: (1) 예측된 cryptic pocket에 대한 고처리량 약물 스크리닝 및 구조-활성 관계(SAR) 연구, (2) 실시간 변이형 모니터링과 신속한 동역학 업데이트 파이프라인 구축, (3) 스파이크의 극단적 개방 상태의 생리적 의미와 빈도에 대한 추가 실험 검증

## Evaluation

- Novelty: 5/5
- Technical Soundness: 5/5
- Significance: 5/5
- Clarity: 4/5
- Overall: 5/5

**총평**: 분산 컴퓨팅으로 exascale 성능을 달성하고 0.1초 분량의 대규모 분자동역학 시뮬레이션 데이터를 생성하여 SARS-CoV-2 단백질의 동적 구조를 전례 없이 상세히 규명한 획기적 연구이다. 스파이크 개방 메커니즘 발견과 50개 이상의 약물 표적 제시는 COVID-19 치료제 개발에 직접적인 기여를 하며, 오픈 사이언스 원칙에 따른 데이터 공유는 과학 공동체 전체의 신약 개발 가속화를 촉진했다.

## Related Papers

- 🏛 기반 연구: [[papers/403_Highly_accurate_protein_structure_prediction_with_AlphaFold/review]] — 단백질 구조 예측 기술이 바이러스 스파이크 단백질의 동역학 시뮬레이션에 필수적인 구조적 기반을 제공한다
- 🔗 후속 연구: [[papers/046_Accurate_structure_prediction_of_biomolecular_interactions_w/review]] — AlphaFold 3의 생체분자 복합체 예측 기술과 스파이크 단백질의 동역학 시뮬레이션이 상호 보완적인 구조-기능 분석을 가능하게 한다
- 🧪 응용 사례: [[papers/138_Autonomous_chemical_research_with_large_language_models/review]] — 대규모 분자 시뮬레이션 결과를 AI 기반 자율 화학 연구 시스템에 적용하여 약물 개발을 가속화할 수 있다
- 🔗 후속 연구: [[papers/795_The_AI_Scientist_Towards_Fully_Automated_Open-Ended_Scientif/review]] — 분산 컴퓨팅을 활용한 단백질 동역학 연구가 완전 자동화된 과학 발견 시스템의 핵심 구성요소가 될 수 있다
- 🔄 다른 접근: [[papers/171_Boltz-1_Democratizing_Biomolecular_Interaction_Modeling/review]] — 둘 다 단백질 구조 예측에 초점을 두지만 Boltz-1은 오픈소스 접근법을 제시한다.
- 🔗 후속 연구: [[papers/686_Robust_deep_learning_based_protein_sequence_design_using_Pro/review]] — ProteinMPNN의 서열 설계 기법을 스파이크 단백질 동역학 연구에 적용할 수 있다.
- 🧪 응용 사례: [[papers/403_Highly_accurate_protein_structure_prediction_with_AlphaFold/review]] — 정확한 단백질 구조 예측이 바이러스 스파이크 단백질의 동역학 시뮬레이션과 약물 타겟 발견에 필수적인 출발점을 제공한다
- 🧪 응용 사례: [[papers/046_Accurate_structure_prediction_of_biomolecular_interactions_w/review]] — 생체분자 복합체 구조 예측 기술이 바이러스-숙주 상호작용 연구와 약물-단백질 결합 분석에 직접 활용될 수 있다
- 🔄 다른 접근: [[papers/171_Boltz-1_Democratizing_Biomolecular_Interaction_Modeling/review]] — 같은 생체분자 구조 예측 문제를 상용 vs 오픈소스 접근법으로 해결한다.
- 🧪 응용 사례: [[papers/686_Robust_deep_learning_based_protein_sequence_design_using_Pro/review]] — 단백질 서열 설계 기법을 바이러스 단백질 구조 연구에 적용할 수 있다.
- 🧪 응용 사례: [[papers/095_AMDAT_An_Open-Source_Molecular_Dynamics_Analysis_Toolkit_for/review]] — 분자동역학 분석을 SARS-CoV-2 시뮬레이션의 엑사스케일 예측에 적용
- 🔗 후속 연구: [[papers/758_Simulations_in_the_era_of_exascale_computing/review]] — SARS-CoV-2 시뮬레이션의 엑사스케일 확장이 계산 재료과학 분야 엑사스케일 활용의 구체적 사례이다.
