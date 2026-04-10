---
title: "829_Towards_Foundation_Models_for_Scientific_Machine_Learning_Ch"
authors:
  - "Shashank Subramanian"
  - "P. Harrington"
  - "K. Keutzer"
  - "W. Bhimji"
  - "D. Morozov"
date: "2023"
doi: "10.48550/arXiv.2306.00258"
arxiv: ""
score: 4.25
essence: "본 논문은 자연언어처리(NLP)와 컴퓨터비전(CV) 분야에서 성공적으로 활용된 파운데이션 모델 패러다임(사전학습-미세조정)을 과학 머신러닝(Scientific Machine Learning, SciML) 분야에 적용 가능한지 체계적으로 검증한다. 편미분방정식(PDE) 학습 작업에서 신경 연산자(Neural Operator)를 다양한 물리 시스템으로 사전학습한 후 미세조정하면, 처음부터 학습한 모델보다 수 자릿수 적은 데이터로 목표 정확도에 도달할 수 있음을 보인다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/Structured_Research_Frameworks"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Subramanian et al._2023_Towards Foundation Models for Scientific Machine Learning Characterizing Scaling and Transfer Behav.pdf"
---

# Towards Foundation Models for Scientific Machine Learning: Characterizing Scaling and Transfer Behavior

> **저자**: Shashank Subramanian, P. Harrington, K. Keutzer, W. Bhimji, D. Morozov, M. W. Mahoney, Amir Gholami | **날짜**: 2023 | **DOI**: [10.48550/arXiv.2306.00258](https://doi.org/10.48550/arXiv.2306.00258)

---

## Essence

![Figure 1](figures/fig1.webp) *다양한 PDE 시스템에 대한 사전학습과 미세조정 프레임워크*

본 논문은 자연언어처리(NLP)와 컴퓨터비전(CV) 분야에서 성공적으로 활용된 파운데이션 모델 패러다임(사전학습-미세조정)을 과학 머신러닝(Scientific Machine Learning, SciML) 분야에 적용 가능한지 체계적으로 검증한다. 편미분방정식(PDE) 학습 작업에서 신경 연산자(Neural Operator)를 다양한 물리 시스템으로 사전학습한 후 미세조정하면, 처음부터 학습한 모델보다 수 자릿수 적은 데이터로 목표 정확도에 도달할 수 있음을 보인다.

## Motivation

- **Known**: NLP(BERT, GPT)와 CV 분야에서 파운데이션 모델의 사전학습-미세조정 패러다임이 매우 성공적임. 기존 SciML에서는 각 PDE 문제마다 신경 연산자를 처음부터 재학습해야 함.

- **Gap**: SciML 분야에서는 (1) 모델 크기 확장 효과, (2) 다운스트림 데이터 스케일링, (3) 물리 파라미터의 분포 외(OOD) 동작, (4) 다중 물리 시스템에 대한 전이 학습 특성이 체계적으로 연구되지 않음.

- **Why**: SciML은 과학 계산에서 중요한 역할을 하지만, 전통적인 일회용 모델 학습 방식은 확장성과 효율성 측면에서 한계가 있음. 파운데이션 모델 패러다임이 SciML에도 적용 가능하면 데이터 효율성을 극적으로 개선할 수 있음.

- **Approach**: Fourier Neural Operator(FNO)를 기본 아키텍처로 사용하여 Poisson, Advection-Diffusion, Helmholtz 등 다양한 PDE 시스템에서 (1) 데이터셋 다양성 확보, (2) 모든 PDE 입력 변수(계수, 소스 함수) 샘플링, (3) 다운스트림 데이터 크기, 모델 파라미터, 물리 파라미터 변화에 따른 전이 학습 효과를 측정.

## Achievement

![Figure 3](figures/fig3.webp) *다운스트림 데이터 스케일링: 전이학습 vs 처음부터 학습*

![Figure 4](figures/fig4.webp) *모델 크기 확장 (64K에서 256M 파라미터): 미세조정이 처음부터 학습보다 우수한 성능 향상*

1. **다운스트림 데이터 효율성**: 전이학습을 통해 목표 정확도에 도달하는 데 처음부터 학습 대비 **자릿수 단위의 데이터 감소**. 영점-샷(zero-shot) 또는 소수-샷(few-shot, O(10) 데이터) 미세조정에서도 유의미한 성능 향상 관찰. 다운스트림 데이터가 사전학습 데이터 규모에 도달할 때까지 일관된 이점 유지.

2. **모델 크기 스케일링 효과**: 매개변수를 64K에서 256M으로 확대(4,000배)할 때, 작은 모델에서의 오류 포화 현상 해소 후 단조 감소. **미세조정된 모델이 처음부터 학습한 모델보다 매개변수 스케일링에 따른 성능 향상 폭이 더 큼**.

3. **분포 내 전이학습**: 사전학습 분포 범위 내의 다운스트림 작업에서는 미세조정 데이터 규모와 무관하게 일관되게 처음부터 학습을 능가. 중간 정도 OOD 작업에서도 수 자릿수 우수한 정확도 달성.

4. **분포 외(OOD) 일반화**: 물리 파라미터를 체계적으로 분포 외로 이동하면 성능 향상폭이 예상대로 감소하지만, 저데이터 체제에서도 유의미한 이점 유지. OOD 정도를 정량화하여 분석.

5. **다중 연산자 전이**: 서로 다른 해의 특성을 보이는 Poisson, Helmholtz 등 여러 PDE 시스템으로 동시에 사전학습한 단일 모델도 다양한 다운스트림 작업에서 성능 이점 유지. **동일한 모델이 서로 다른 PDE 시스템 간 전이 가능함을 입증**.

## How

![Figure 5](figures/fig5.webp) *물리 파라미터 변화에 따른 전이학습: 분포 내(a)에서 심화 OOD(d)로의 성능 곡선*

- **사전학습 데이터셋 구성**: 다양한 PDE에서 모든 입력 변수(PDE 계수, 소스 함수, 경계/초기 조건)를 동시에 샘플링. 기존 연구에서 일부 변수를 고정한 것과 대조. 정규화 전략 적용으로 성능 저하 방지.

- **신경 연산자 아키텍처**: Fourier Neural Operator(FNO) 기반으로 함수 공간 간 매핑 학습. 다양한 PDE 계수와 경계 조건의 조합 처리 가능.

- **영점-샷 및 소수-샷 평가**: 사전학습 모델을 다운스트림 데이터에 직접 적용(영점-샷) 또는 O(10)개 데이터로 미세조정(소수-샷).

- **스케일링 분석**: 모델 크기(64K~256M), 다운스트림 데이터량, PDE 파라미터 범위를 독립적으로 변화시키며 성능 측정.

- **OOD 정량화**: Tab. 1에서 확산 계수(diffusion coefficient), 이류 속도(advection velocity), 파수(wavenumber) 등을 단계적으로 변화시켜 OOD 정도를 정량화하고 성능 변화 추적.

## Originality

- **최초 종합 분석**: SciML에서 파운데이션 모델의 모든 핵심 차원(모델 크기, 데이터 규모, 물리 매개변수 범위, 다중 연산자)을 체계적으로 평가한 첫 연구. 기존 SciML 전이학습 연구들은 이러한 차원 중 일부만 개별적으로 다룸.

- **다양성 기반 사전학습**: PDE의 모든 입력 변수를 샘플링하여 사전학습 데이터셋 구성. 기존 FNO 및 관련 연구에서 일부 변수를 고정한 것을 개선.

- **정량화된 OOD 분석**: 물리 파라미터를 단계적으로 변화시켜 OOD 정도를 명확히 정의하고 측정. SciML에서 OOD 일반화 특성을 물리적 의미와 함께 분석한 점이 참신.

- **다중 PDE 시스템 결합**: 여러 미분 연산자(Poisson, Helmholtz, Advection-Diffusion)를 하나의 모델로 통합하여 사전학습하고 전이 가능함을 입증. 기존 연구는 단일 PDE 시스템에 집중.

## Limitation & Further Study

- **아키텍처 한정성**: 단일 아키텍처(FNO)에 대한 분석. DeepONet, Transformer 기반 연산자 등 다른 신경 연산자 아키텍처에 대한 일반화 가능성 미제시.

- **PDE 시스템 범위**: Poisson, Advection-Diffusion, Helmholtz 등 상대적으로 간단한 선형/준선형 PDE에 집중. Navier-Stokes 같은 비선형 유체역학 문제에 대한 확장 필요.

- **기하학 및 이산화 다양성**: 정규 그리드 기반의 균일한 해상도만 다룸. 불규칙 기하, 적응 메시, 다중 해상도에 대한 일반화는 미흡.

- **계산 비용 분석**: 사전학습 비용-효과 분석 및 실제 과학 응용에서의 총 계산 시간 비교 부재. 미세조정 시간, 추론 시간도 상세히 제시하지 않음.

- **물리 기반 손실 함수 미포함**: PINN 스타일의 물리 제약을 손실 함수에 포함하지 않음. 물리 정보와 데이터 기반 학습의 결합 가능성 탐색 필요.

- **후속 연구 방향**:
  - 더 복잡한 비선형 PDE, 시간 의존 문제로의 확장
  - 기하학적 다양성과 메시 생성 독립성 달성
  - 하이브리드 접근법(물리 기반 손실 + 데이터 기반 전이학습)
  - 더 큰 규모 모델(256M 이상)에서의 성능 분석
  - 실제 과학 응용(유체역학, 구조해석 등)에 대한 사례 연구


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.25/5

**총평**: 본 논문은 SciML 분야에서 파운데이션 모델 패러다임의 가능성을 처음으로 체계적으로 검증한 중요한 연구로, 모델 크기, 데이터 스케일, 물리 파라미터 범위, 다중 연산자 등 여러 차원의 종합 분석을 통해 전이학습의 강력한 이점을 명확히 보인다. 다만 단일 아키텍처와 상대적으로 단순한 PDE 시스템에 국한되었으며, 실제 과학 응용으로의 확장과 물리 기반 제약의 통합이 향후 과제이다. SciML 커뮤니티에 중요한 벤치마크와 로드맵을 제시하는 점에서 의의가 크다.

## Related Papers

- 🧪 응용 사례: [[papers/772_State-Free_Inference_of_State-Space_Models_The_Transfer_Func/review]] — 과학 머신러닝 파운데이션 모델 패러다임을 상태공간모델의 물리 시스템 학습에 적용할 수 있다
- 🧪 응용 사례: [[papers/140_Autonomous_reinforcement_learning_agent_for_chemical_vapor_d/review]] — 편미분방정식 학습의 사전학습-미세조정 패러다임을 화학 공정 최적화에 적용할 수 있다
- 🔗 후속 연구: [[papers/343_Foundation_models_for_materials_discovery__current_state_and/review]] — 재료 발견을 위한 파운데이션 모델의 현재 상태를 과학 머신러닝 전반으로 확장한다
- 🏛 기반 연구: [[papers/721_Scientific_Machine_Learning_through_Physics-Informed_Neural/review]] — 물리정보신경망이 과학 머신러닝 파운데이션 모델의 물리적 제약 조건 구현에 기반을 제공한다
- 🏛 기반 연구: [[papers/105_Artificial_Intelligence_for_Direct_Prediction_of_Molecular_D/review]] — 과학 기계학습의 핵심 원리를 제시하여 과학 분야 파운데이션 모델 개발의 중요한 이론적 토대를 마련한다
- 🏛 기반 연구: [[papers/342_Foundation_Models_for_Environmental_Science_A_Survey_of_Emer/review]] — 과학 기계학습을 위한 파운데이션 모델의 일반적 도전과제와 기회를 환경과학에 적용할 수 있다
- 🔗 후속 연구: [[papers/479_Large_physics_models_towards_a_collaborative_approach_with_l/review]] — 과학적 머신러닝을 위한 파운데이션 모델 개념이 물리학 특화 대규모 모델로 확장된다.
- 🏛 기반 연구: [[papers/694_Scalable_Cross-Facility_Federated_Learning_for_Scientific_Fo/review]] — 과학 머신러닝을 위한 파운데이션 모델의 분산 학습 구현 사례이다.
- 🏛 기반 연구: [[papers/140_Autonomous_reinforcement_learning_agent_for_chemical_vapor_d/review]] — 과학 머신러닝의 파운데이션 모델 패러다임이 화학 공정 최적화에 적용될 수 있는 이론적 기반을 제공한다
- 🏛 기반 연구: [[papers/772_State-Free_Inference_of_State-Space_Models_The_Transfer_Func/review]] — 과학 머신러닝의 파운데이션 모델 패러다임이 상태공간모델의 전달함수 접근법에 기반을 제공한다
- 🧪 응용 사례: [[papers/354_From_GPU_Engineering_to_Scientific_Discovery_Parallelism_Tec/review]] — GPU 병렬화 기법을 과학 기계학습을 위한 기초 모델에 적용하여 대규모 모델의 효율적인 학습과 배포를 실현할 수 있다.
