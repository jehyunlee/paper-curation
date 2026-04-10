---
title: "1125_Accelerating_cell_culture_media_development_using_Bayesian_o"
authors:
  - "Harini Narayanan"
  - "Joshua A. Hinckley"
  - "Rachel Barry"
  - "Brendan Dang"
  - "Lenna A. Wolffe"
date: "2025.07"
doi: "10.1038/s41467-025-61113-5"
arxiv: ""
score: 4.0
essence: "베이지안 최적화(Bayesian Optimization) 기반의 반복적 실험 설계 프레임워크를 적용하여 세포 배양 배지 개발을 가속화했으며, PBMC 배양과 K. phaffii의 재조합 단백질 생산 최적화에서 기존 방법 대비 3-30배 적은 실험으로 우수한 결과를 달성했다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "cat/Reinforcement_Learning_and_Self-Verification"
  - "sub/Bayesian_Materials_Inference"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Narayanan et al._2025_Accelerating cell culture media development using Bayesian optimization-based iterative experimental.pdf"
---

# Accelerating cell culture media development using Bayesian optimization-based iterative experimental design

> **저자**: Harini Narayanan, Joshua A. Hinckley, Rachel Barry, Brendan Dang, Lenna A. Wolffe, Adel Atari, Yuen-Yi Tseng, J. Christopher Love | **날짜**: 2025-07-01 | **DOI**: [10.1038/s41467-025-61113-5](https://doi.org/10.1038/s41467-025-61113-5)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1 | Workﬂow. Schematic representation of the Bayesian Optimization (BO)-based iterative experimental design workﬂow*

베이지안 최적화(Bayesian Optimization) 기반의 반복적 실험 설계 프레임워크를 적용하여 세포 배양 배지 개발을 가속화했으며, PBMC 배양과 K. phaffii의 재조합 단백질 생산 최적화에서 기존 방법 대비 3-30배 적은 실험으로 우수한 결과를 달성했다.

## Motivation

- **Known**: 세포 배양 배지 최적화는 생명과학 연구와 생명공학에서 필수적인 작업이지만, 10-100개 범위의 다양한 설계 인자들로 인해 매우 복잡하고 자원 집약적이다. 기존 방법들(OFAT, Design of Experiments)은 설계 공간 전체를 광범위하게 탐색해야 하며 범주형 변수 처리에 제한이 있다.
- **Gap**: 기존 DoE 및 메타휴리스틱 최적화 접근법은 데이터 수집, 모델링, 최적화를 분리하여 수행하고, 생물학적 잡음(noise)을 충분히 고려하지 못하며, 범주형 설계 인자와 제약 조건이 있는 설계 공간을 효율적으로 처리하지 못한다.
- **Why**: 베이지안 최적화 기반 접근법은 비용이 많이 드는 생물학적 실험에서 탐색-활용(exploration-exploitation) 트레이드오프를 통해 실험 횟수를 대폭 줄이고, 범주형 변수와 제약 조건을 자연스럽게 처리할 수 있어 정확하고 빠른 최적화가 가능하다.
- **Approach**: 가우시안 프로세스(Gaussian Process) 기반 확률적 서로게이트 모델과 베이지안 최적화기를 결합하여 반복적 실험 설계 프레임워크를 구축했으며, 초기 실험 세트로 GP 모델을 구성하고 각 반복에서 탐색-활용 균형을 맞추며 모델을 지속적으로 업데이트한다.

## Achievement

![Figure 2](figures/fig2.webp)

*Fig. 2 | Media blend and cytokine composition optimization PBMC cultures.*

- **PBMC 배양 배지 최적화**: 세포 생존력 유지와 표현형 분포 안정성을 위한 사이토카인 보충 배지 조성을 도출하여 72시간까지 세포 배양 가능
- **K. phaffii 재조합 단백질 생산**: 3개의 재조합 단백질 생산을 최적화하는 배지 조건을 발견하여 표준 배지 대비 향상된 성능 달성
- **실험 효율성 향상**: 기존 DoE 방법 대비 3-30배 적은 실험으로 우수한 결과 달성 (특히 범주형 변수 포함 9개 설계 인자에서 10-30배 감소)
- **전이 학습 적용**: 추가 설계 인자나 배지 보충제 추가 시 사후 수정 가능하고 학습 전이 가능함을 입증
- **복합 설계 공간 처리**: 연속 변수와 범주형 변수, 제약 조건이 혼재된 복잡한 설계 공간을 효율적으로 처리

## How

![Figure 1](figures/fig1.webp)

*Fig. 1 | Workﬂow. Schematic representation of the Bayesian Optimization (BO)-based iterative experimental design workﬂow*

- 가우시안 프로세스(GP)를 확률적 서로게이트 모델로 사용하여 생물학적 시스템의 부드러운 응답 함수 학습
- GP에 사전 신념(prior beliefs)과 공정 잡음(process noise)을 명시적으로 포함하여 생물학적 불확실성 반영
- 베이지안 최적화기와 GP의 상호작용을 통해 각 반복에서 탐색(unexplored regions)-활용(favorable regions) 트레이드오프 구현
- 초기 실험 세트로 첫 번째 GP 모델 구축 후 반복적으로 실험 계획, 수행, 모델 업데이트 (수렴 또는 실험 예산 소진 시까지)
- 범주형 설계 인자를 커스텀 커널(custom kernels)로 처리하여 OFAT 및 DoE의 확장성 문제 해결
- 제약 조건이 있는 설계 공간에서 실험 계획 가능하게 설계

## Originality

- 기존 BO 기반 세포 배양 배지 최적화 연구들이 연속 변수만 고려한 반면, 본 연구는 범주형 변수와 제약 조건을 포함한 복합 설계 공간 처리
- 데이터 수집, 모델링, 최적화를 순차적으로 분리하는 기존 방식을 벗어나 반복적 피드백 루프로 통합한 능동 학습(active learning) 접근
- GP의 고유한 장점(선행 신념 인코딩, 공정 잡음 명시적 포함, 설계 공간 내 위치 기반 불확실성)을 생물학적 최적화에 활용
- PBMC 배양과 K. phaffii 단백질 생산이라는 두 가지 상이한 응용 사례에서 프레임워크의 일반성과 확장성 입증
- 전이 학습 메커니즘으로 설계 공간 수정 후 추가 실험 효율성 입증

## Limitation & Further Study

- PBMC와 K. phaffii 두 가지 사례에 국한되어 다른 세포주 또는 배양 목표에 대한 일반화 가능성 검증 필요
- GP 모델의 성능이 초기 실험 세트의 품질과 크기에 의존하며, 초기 설계 선택에 대한 민감도 분석 부재
- 복잡한 다중 목적 최적화(multi-objective optimization) 시나리오에서의 확장성 명확히 제시되지 않음
- 베이지안 최적화와 DoE의 정량적 비교 분석이 추정치에 기반한 것으로, 동일 조건에서 직접 비교 실험 필요
- 생물학적 시스템의 재현성(reproducibility) 변동성이 최적화 결과에 미치는 영향 분석 부족
- 후속 연구에서는 더 많은 세포주, 배양 조건, 복합 목적 함수에 대한 적용과 머신러닝 모델(예: 신경망) 기반 서로게이트와의 비교 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 베이지안 최적화와 가우시안 프로세스를 활용한 반복적 실험 설계 프레임워크를 통해 세포 배양 배지 최적화의 효율성을 획기적으로 향상시켰으며, 범주형 변수와 제약 조건 처리, 전이 학습 적용 등에서 기술적 혁신성을 보여준다. 실무적 영향력이 크고 일반화 가능성이 높아 생명공학 분야에 상당한 기여를 할 수 있다.

## Related Papers

- 🔄 다른 접근: [[papers/1126_Autonomous_platform_for_solution_processing_of_electronic_po/review]] — 두 논문 모두 베이지안 최적화를 자동화 실험에 적용하되 세포 배양 배지는 생물학, 전자 고분자는 재료과학 분야에 특화되어 있다.
- 🔗 후속 연구: [[papers/788_Targeted_materials_discovery_using_Bayesian_algorithm_execut/review]] — 베이지안 알고리즘 실행을 통한 표적 재료 발견은 세포 배양 배지 개발의 베이지안 최적화 프레임워크를 재료 발견으로 확장한다.
- 🧪 응용 사례: [[papers/072_Agents_for_self-driving_laboratories_applied_to_quantum_comp/review]] — 자율주행 실험실의 AI 에이전트는 세포 배양 배지 개발의 베이지안 최적화 과정을 완전 자동화된 실험 시스템으로 구현할 수 있다.
- 🔗 후속 연구: [[papers/140_Autonomous_reinforcement_learning_agent_for_chemical_vapor_d/review]] — 화학 기상 증착의 자율 강화학습에서 베이지안 최적화로의 확장
- 🔄 다른 접근: [[papers/658_Real-time_experiment-theory_closed-loop_interaction_for_auto/review]] — 자동화된 실시간 실험-이론 폐쇄루프와 베이지안 최적화의 다른 접근법
- 🏛 기반 연구: [[papers/744_Self-Driving_Laboratories_for_Chemistry_and_Materials_Scienc/review]] — 화학과 재료과학의 자율주행 실험실이 베이지안 최적화의 이론적 기반
- 🔄 다른 접근: [[papers/1126_Autonomous_platform_for_solution_processing_of_electronic_po/review]] — 두 논문 모두 베이지안 최적화 기반 자동화를 다루되 Polybot은 재료과학, 세포 배양은 생물학 응용에 초점을 맞춘다.
