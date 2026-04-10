---
title: "618_Physical_formula_enhanced_multi-task_learning_for_pharmacoki"
authors:
  - "Yuqiang Li"
  - "Ruifeng Li"
  - "Dongzhan Zhou"
  - "Ancheng Shen"
  - "Ao Zhang"
date: "2024"
doi: "미제공"
arxiv: ""
score: 4.0
essence: "본 논문은 물리 공식(physical formula) 제약을 다중 작업 학습(multi-task learning)에 통합하여 약동학(pharmacokinetics)의 4가지 핵심 파라미터(AUC, CL, Vdss, T1/2)를 동시에 예측하는 PEMAL 프레임워크를 제시한다. 제한된 데이터와 높은 노이즈 환경에서 물리 제약을 활용한 명시적 작업 간 연결을 통해 예측 정확도와 견고성을 현저히 향상시킨다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/Biomedical_Causal_Modeling"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Li et al._2024_Physical formula enhanced multi-task learning for pharmacokinetics prediction.pdf"
---

# Physical formula enhanced multi-task learning for pharmacokinetics prediction

> **저자**: Yuqiang Li, Ruifeng Li, Dongzhan Zhou, Ancheng Shen, Ao Zhang, Mao Su, Mingqian Li, Hongyang Chen, Gang Chen, Yin Zhang, Shufei Zhang, Wanli Ouyang | **날짜**: 2024 | **DOI**: [미제공]

---

## Essence

![Figure 1](figures/fig1.webp)
*약동학 예측을 위한 물리 공식 강화 다중 작업 학습의 개요. (a) AI 기반 신약 개발의 과제, (b) 물리 공식 제약을 신경망에 통합하여 작업 간 지식 전이와 목표 정렬 강화*

본 논문은 물리 공식(physical formula) 제약을 다중 작업 학습(multi-task learning)에 통합하여 약동학(pharmacokinetics)의 4가지 핵심 파라미터(AUC, CL, Vdss, T1/2)를 동시에 예측하는 PEMAL 프레임워크를 제시한다. 제한된 데이터와 높은 노이즈 환경에서 물리 제약을 활용한 명시적 작업 간 연결을 통해 예측 정확도와 견고성을 현저히 향상시킨다.

## Motivation

- **Known**: 
  - AI 기반 신약 개발(AIDD)은 약동학 예측을 통해 용량, 안전성, 유효성 결정에 필수적 역할 수행
  - 기존 기계학습은 수작업으로 설계된 분자 서술자(descriptor) 또는 지문(fingerprint)에 의존하며 표현력 제한
  - 딥러닝은 분자 구조에서 자동으로 특징 추출 가능하지만 단일 작업(single-task) 모델은 데이터 부족 문제 해결 미흡

- **Gap**: 
  - 약동학 파라미터들(AUC, CL, Vdss, T1/2) 간의 물리적 관계(AUC×CL=K₁, CL×T₁/₂=Vdss×K₂)를 활용하지 않음
  - 기존 다중 작업 학습은 암묵적 특징 공유에만 의존하여 명시적 제약 부재
  - 습식 실험의 고비용 및 노이즈로 인한 심각한 데이터 부족 문제 미해결

- **Why**: 
  - 물리 공식을 신경망에 통합하면 작업 간 명시적 제약을 통한 지식 전이 효율성 증대
  - 상호 제약은 단일 작업의 불확실성 감소 및 노이즈 강건성 향상 가능

- **Approach**: 
  - 3단계 프레임워크: (Stage I) 자율 지도학습(self-supervised learning)으로 일반 분자 표현 학습, (Stage II) 라벨링된 약동학 데이터(CL, Vdss, T1/2)로 작업별 사전학습, (Stage III) 물리 공식 제약을 통한 다중 작업 학습

## Achievement

![Figure 2](figures/fig2.webp)
*PEMAL과 GIN의 약동학 예측 시각화. (a-d) 각 파라미터별 예측값과 관측값의 상관관계*

1. **데이터 효율성 극대화**: 공개 데이터 170개 포인트만으로도 전통 기계학습(Random Forest, Gaussian Process, XGBoost) 및 단일 작업 딥러닝(GIN) 초과 성능 달성. 물리 제약이 암묵적 특징 공유보다 더 효과적인 지식 전이 실현

2. **노이즈 강건성 우수성**: 데이터에 의도적 노이즈 추가 시 GIN은 성능 급격히 저하하나, PEMAL은 작업 간 물리적 제약으로 인해 상대적으로 안정적 예측 유지. 노이즈 환경에서의 우월성은 습식 실험의 고유한 불확실성 특성 반영

3. **다양한 데이터 희소성 조건 대응**: 훈련 데이터 규모를 단계적으로 감소시킬 때 PEMAL의 성능 저하율이 GIN보다 현저히 낮음. 극도로 제한된 샘플에서도 일반화 성능 유지

## How

![Figure 3](figures/fig3.webp)
*다양한 데이터 볼륨에 따른 성능 비교. PEMAL과 GIN의 각 약동학 파라미터별 성능 변화*

**Stage I - 자율 지도학습 (Dual-level Reconstruction)**:
- 원자(atom) 분기: 무작위 마스킹된 원자에 대해 재구성 작업 수행. MAE 손실로 감독
- 모티프(motif) 분기: 기능 그룹 수준의 정보 포착. 모티프 특징 마스킹 및 재구성
- 교차 수준 대조학습(cross-level contrastive learning): 동일 분자 내 원자-모티프 거리 최소화, 서로 다른 분자 간 거리 최대화로 상호작용 강화

**Stage II - 약동학 데이터 사전학습**:
- Stage I에서 학습된 그래프 인코더 로드
- CL, Vdss, T1/2에 대해 각각 완전 연결층(fully connected layer) 추가
- 로그 변환된 예측값과 관측값 간 MAE 손실로 감독
- AUC는 데이터 부족으로 이 단계에서 제외 (Stage III에서 물리 공식으로 유도)

**Stage III - 물리 공식 강화 다중 작업 학습**:
- 3개 병렬 분기: CL, Vdss, T1/2 각각 예측 (Stage II 가중치 상속)
- 물리 공식 제약 적용:
  - 식(1): AUC × CL = K₁ (K₁ 상수) → AUC 유추
  - 식(2): CL × T₁/₂ = Vdss × K₂ (K₂ 상수) → 명시적 작업 간 제약
- 감독 신호: 4개 파라미터의 MAE 손실(L_AUC, L_CL, L_Vdss, L_T₁/₂) + 식(2)의 물리 공식 제약

## Originality

- **물리 제약의 신경망 통합**: 기존 다중 작업 학습의 암묵적 특징 공유를 넘어, 약동학적 물리 관계식을 명시적 제약으로 통합한 혁신적 접근. 약동학의 내재된 메커니즘을 수학적으로 인코딩

- **이중 수준 사전학습 전략**: 원자와 모티프 수준의 동시 재구성으로 분자의 기본 구성과 기능 그룹 모두 포착. 기존 생성 기반 방법의 원자 수준만의 한계 극복

- **희소 데이터 환경 최적화**: 자율 지도학습(unlabeled)과 라벨링된 노이즈 데이터의 2단계 사전학습 통합으로 제한된 고품질 라벨 효율적 활용

- **다중 작업 간 명시적 정렬**: 물리 공식을 통한 작업 간 상호 제약이 단일 작업의 불확실성 감소 및 노이즈 강건성 향상을 동시에 달성하는 우아한 설계

## Limitation & Further Study

- **물리 공식 제약의 보편성 한정**: AUC, CL, Vdss, T1/2 간의 관계식은 특정 약동학 모델에 기반. 다른 약물 성질이나 생물 시스템에 대한 일반화 가능성 미흡. 향후 다양한 물리/화학 제약 통합 필요

- **데이터셋의 제한성**: 공개 170개 데이터 포인트만 사용. 제약적 환경에서의 성능이지만, 보다 광범위한 임상 데이터셋 검증 부재

- **상수 K₁, K₂의 추정 방식 명확화 필요**: 물리 공식의 상수 값 결정 과정이 상세히 기술되지 않음. 일반화 및 재현성 강화 위해 명시적 설정 방법 필요

- **해석성(interpretability) 강화**: 모델이 특정 예측을 도출하는 물리적 메커니즘에 대한 해석 제한. 화학자/약학자의 신뢰성 구축 위해 주요 분자 특성의 기여도 분석 추가 필요

- **다른 약동학 파라미터 확장**: 현재 4개 파라미터만 다룸. 경구 생물이용률(F), 혈청 단백질 결합률 등 추가 파라미터로의 확장 연구

## Evaluation

- **Novelty (독창성)**: 4/5
  - 물리 공식 제약을 다중 작업 학습에 통합한 새로운 패러다임 제시
  - 이중 수준 분자 표현 학습과 2단계 사전학습 전략은 상당히 참신
  - 다만 개별 기술 요소(자율 지도학습, 다중 작업 학습)는 기존 기법의 조합

- **Technical Soundness (기술적 타당성)**: 4/5
  - 약동학의 물리 관계식 활용은 원리적으로 타당하고 수학적 형식화 명확
  - Stage I-III 프레임워크의 순차적 설계는 논리적으로 정당화됨
  - 상수 K₁, K₂의 결정 및 손실함수 가중치 설정에 대한 상세 기술 부족

- **Significance (의의)**: 4.5/5
  - 데이터 부족 및 노이즈가 만연한 신약 개발 분야에 실질적 기여 큼
  - 물리 제약을 신경망에 통합하는 원칙은 다른 과학 분야(물리, 화학, 생물) 응용 가능
  - 170개 공개 데이터로 우월한 성능은 실용성 입증

- **Clarity (명확성)**: 3.5/5
  - 전체 프레임워크 구조는 명확하나, 구체적 구현 세부사항(손실함수 결합, 하이퍼파라미터) 부족
  - Figure 1, 3은 개념과 결과 효과적 전달이나, Stage II 사전학습 필요성에 대한 절제 기술 미흡
  - 물리 공식 제약의 정확한 통합 방식 (예: soft constraint vs. hard constraint) 명시 필요

- **Overall (종합)**: 4/5

**총평**: 본 논문은 물리 제약을 신경망에 명시적으로 통합하여 희소하고 노이즈가 많은 약동학 데이터에서 우수한 성능을 달성한 기술적 기여도 높은 연구이다. 특히 이중 수준 분자 표현과 2단계 사전학습 전략은 혁신적이며, 약동학의 물리 관계식 활용은 도메인 지식의 효과적 인코딩을 보여준다. 다만 상수 결정, 손실함수 설계, 일반화 가능성 관련 설명이 보완되면 더욱 견고한 연구가 될 것으로 판단된다.

## Related Papers

- 🏛 기반 연구: [[papers/576_Nonlinear_stochastic_and_quantum_motion_from_Coulomb_forces/review]] — 물리 법칙 기반의 비선형 상호작용 이해가 약동학 파라미터 간의 물리적 제약 관계 모델링에 도움이 된다.
- 🔄 다른 접근: [[papers/621_Physics-informed_neural_network_for_multi-objective_design_o/review]] — 물리 정보를 신경망에 통합한다는 공통 접근법이지만 약동학 예측과 열관리 설계라는 다른 응용 분야를 다룬다.
- 🔗 후속 연구: [[papers/427_Incorporating_Continuous_Dependence_Qualifies_Physics-Inform/review]] — 연속 의존성을 고려한 PINN의 개선 방법을 약동학 예측의 물리 제약 통합에 적용할 수 있다.
- 🏛 기반 연구: [[papers/621_Physics-informed_neural_network_for_multi-objective_design_o/review]] — 물리 제약을 신경망에 통합하는 방법론이 열관리 장치 설계 최적화의 기술적 기반이 된다.
