---
title: "516_Machine-Learned_Interatomic_Potentials_for_Predicting_Physic"
authors:
  - "M. Polovinkin"
  - "N. Rybin"
  - "D. Maksimov"
  - "F. Valiev"
  - "A. Khudorozhkova"
date: "2026.03"
doi: "N/A"
arxiv: ""
score: 4.2
essence: "본 논문은 기계학습 기반 원자간 포텐셜(Machine-Learned Interatomic Potentials, MLIPs)인 Moment Tensor Potentials (MTP)를 활용하여 칼슘 전해 공정에 필요한 용융 Ca-Cu 합금과 CaCl₂-KCl 전해질의 물리화학적 성질을 고정확도로 예측한다. DFT 훈련 데이터 기반의 MTP-분자동역학(MD) 시뮬레이션으로 실험값 대비 20% 이내의 편차로 밀도, 열용량, 열전도도, 이온 전도도, 점도, 확산 계수 등을 계산하여 고온 실험의 비용과 시간을 대폭 절감할 수 있음을 입증했다"
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/Bayesian_Materials_Inference"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Polovinkin et al._2026_Machine-Learned Interatomic Potentials for Predicting Physicochemical Properties of Molten Metal-Sal.pdf"
---

# Machine-Learned Interatomic Potentials for Predicting Physicochemical Properties of Molten Metal-Salt Systems for Calcium Electrolysis

> **저자**: M. Polovinkin, N. Rybin, D. Maksimov, F. Valiev, A. Khudorozhkova, M. Laptev, A. Rudenko, A. Shapeev | **날짜**: 2026-03-26 | **DOI**: N/A

---

## Essence

본 논문은 기계학습 기반 원자간 포텐셜(Machine-Learned Interatomic Potentials, MLIPs)인 Moment Tensor Potentials (MTP)를 활용하여 칼슘 전해 공정에 필요한 용융 Ca-Cu 합금과 CaCl₂-KCl 전해질의 물리화학적 성질을 고정확도로 예측한다. DFT 훈련 데이터 기반의 MTP-분자동역학(MD) 시뮬레이션으로 실험값 대비 20% 이내의 편차로 밀도, 열용량, 열전도도, 이온 전도도, 점도, 확산 계수 등을 계산하여 고온 실험의 비용과 시간을 대폭 절감할 수 있음을 입증했다.

## Motivation

- **Known**: 칼슘은 철강 제조, 배터리 생산, 고급 합금 합성에 필수적이며, 주요 생산 방법은 용융염 전해 공정이다. 이 공정은 용융 Ca-Cu 합금(음극)과 CaCl₂ 기반 전해질이라는 두 개의 고온 액체 상을 포함한다.

- **Gap**: Ca-Cu 액체 합금의 구조 연구는 순수 Ca, Cu 용융물에만 제한되어 있으며, 합금의 열용량, 확산 계수, 점도 데이터가 부족하거나 일관성이 없다. 생산에 사용되는 CaCl₂-KCl의 특정 질량비(80:20) 조성에 대한 완전한 물성 데이터도 부재하다.

- **Why**: 고온 실험을 통한 물성 측정은 자원 집약적이고 비용이 많이 들며, 조성과 온도 범위에 걸친 대규모 매개변수 스크리닝이 필요한 산업 최적화에는 부실용적이다.

- **Approach**: 밀도함수 이론(DFT) 계산으로 훈련된 MTP를 활용한 분자동역학 시뮬레이션으로 구조적, 열역학적, 수송 특성을 계산하여 데이터 공백을 채운다. 동시에 용융염의 밀도, 점도, 이온 전도도를 실험으로 측정하여 계산값을 검증한다.

## Achievement

![Figure 1](figures/fig1.webp) *그림 1: 900K, 1100K, 1300K 온도에서 Ca-Cu 액체 합금의 조성에 따른 밀도*

![Figure 3](figures/fig3.webp) *그림 3: Ca-Cu 용융물의 조성에 따른 질량 비열용량*

1. **최초 개발**: Ca-Cu 합금과 CaCl₂-KCl 용융염에 대한 Moment Tensor Potentials를 처음으로 개발하였으며, Ca-Cu 합금 MTP는 조성 전이성(compositionally transferable)을 확보했다.

2. **포괄적 물성 데이터**: 밀도, 방사상 분포 함수(RDF), 열용량, 열전도도, 점도, 확산 계수, 이온 전도도에 대해 온도 및 조성 의존성을 포함한 완전한 데이터셋을 제공하였으며, 모든 계산값이 실험값과 20% 이내에서 일치한다.

3. **검증된 방법론**: MTP-MD로 계산한 CaCl₂-KCl의 이온 전도도가 실험값과 우수한 일치를 보이며, 제안된 계산 프레임워크의 신뢰성을 입증했다.

4. **데이터 공백 해소**: Ca-Cu 합금의 열용량과 조성 의존성을 최초로 보고했으며, 기존 점도 및 확산 계수 데이터의 불일치를 개선했다.

## How

![Figure 4](figures/fig4.webp) *그림 4: 1000K, 1200K, 1400K 온도에서 점도의 조성 의존성*

![Figure 5](figures/fig5.webp) *그림 5: 900K, 1000K, 1200K, 1400K 온도에서 Ca-Cu 액체 합금의 확산 계수*

**MTP 훈련 절차**:
- 초기 훈련 집합: AIMD(Ab Initio Molecular Dynamics) 2ps 시뮬레이션에서 150개 원자 구조 샘플링
- 안정성 강화: 활성학습(Active Learning) 100ps NPT(정온-정압) 기반으로 외삽 등급이 높은 구조 자동 추가
- 다양성 확보: Ca 몰 분율 0.0~1.0 범위에서 6개 독립 60ps 궤적으로 360개(합금)/300개(용융염) 구조 샘플링
- 최종 최적화: 고온 범위(900~1600K)에서 활성학습을 통해 300개 훈련 집합 구성

**DFT 계산 설정**:
- 패키지: VASP (Vienna Ab initio Simulation Package)
- 함수: PBE (GGA 근사)
- 기저함수 에너지 차단: 520 eV (합금), 500 eV (용융염)
- k-점 메시: 1×1×1 Γ 중심
- 분산 보정: Ca-Cu는 DFT-D3, CaCl₂-KCl은 dDsC 방법 적용

**물성 계산 방법**:
- **밀도**: NPT 앙상블에서 500ps(합금)/1ns(용융염) 궤적의 500 프레임으로부터 계산
- **열용량**: 엔탈피(내부 에너지)의 온도 의존성 기울기로부터 직접 계산
- **점도**: Green-Kubo 이론을 통해 압력 텐서 자기상관 함수 적분 (5ps 또는 25ps 차단)
- **확산 계수**: Einstein 관계식을 이용한 평균제곱변위 분석
- **이온 전도도**: Green-Kubo 관계식으로 전하 선속(charge flux) 자기상관 함수 적분
- **열전도도**: 비평형 Muller-Plathe 방법으로 열선속 인가 및 온도 구배 측정
- **검증**: Stokes-Einstein-Sutherland (SES) 관계식과 Nernst-Einstein 공식으로 독립적 계산값 비교

## Originality

- **최초 MTP 개발**: Ca-Cu 액체 합금과 CaCl₂-KCl 용융염에 대한 MTP의 첫 개발로, 이들 복잡한 액체 시스템의 물리화학적 성질 예측에 새로운 계산 도구 제시

- **조성 전이성 달성**: Ca-Cu 합금 MTP가 넓은 조성 범위(0~100% Ca)에서 전이 가능하도록 설계되어, 임의 조성 예측 가능성 확보

- **포괄적 다중 특성 계산**: 단일 MTP 모델로 구조적, 열역학적, 수송 특성을 모두 계산할 수 있음을 입증하여 계산 효율성과 일관성 향상

- **실험 검증 강화**: 용융염의 밀도, 점도, 이온 전도도를 직접 측정하여 계산 결과의 신뢰성을 강화하고, 기존 문헌 데이터와의 비교 검증 수행

- **일반화된 프레임워크**: 개발된 방법론이 다른 용융염과 액체 합금으로 확장 가능한 일반적 틀을 제시하여 야금학적 응용 최적화의 기초 마련

## Limitation & Further Study

- **계산 정확도**: 실험값 대비 20% 이내 편차는 산업 응용에 충분하지만, 특정 고정밀도가 요구되는 공정에서는 추가 개선 필요

- **이온 전하 할당**: 이온 전도도 계산에서 고정 부분 전하(Ca²⁺=+2, K⁺=+1, Cl⁻=-1)를 사용했으나, 동적 전하 변화의 영향은 미고려

- **온도 범위 제한**: 현재 MTP는 900~1600K 범위에서 훈련되었으므로, 이 범위 외 극한 조건에서의 외삽성 검증 필요

- **압력 의존성**: 본 연구는 대기압(0 bar) 조건만 다루었으므로, 고압 환경에서의 물성 변화 예측을 위한 추가 훈련 필요

- **후속 연구 방향**:
  - 다른 용융염 시스템(예: LiCl-KCl, MgCl₂-기반 전해질)에 대한 MTP 확장 개발
  - 양자 핵 효과(Quantum Nuclear Effect)가 중요한 저온 영역에 대한 MTP 적용
  - 실제 전해 셀 설계를 위한 다물리학 모델링(Multiphysics Modeling) 통합
  - 머신러닝 모델의 불확실성 정량화 및 신뢰도 구간 제시


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4.5/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4.2/5

**총평**: 본 논문은 기계학습 포텐셜을 활용하여 칼슘 전해 공정의 핵심 물질들에 대한 완전한 물성 데이터베이스를 구축한 견고한 산업 응용 연구로, 실험 검증과 체계적인 MTP 훈련 절차를 통해 높은 신뢰성을 확보했으며, 향후 다양한 용융염 및 액체 합금 시스템 연구의 모범 사례가 될 수 있다.

## Related Papers

- 🏛 기반 연구: [[papers/574_Neural-POD_A_Plug-and-Play_Neural_Operator_Framework_for_Inf/review]] — Neural-POD의 무한차원 함수공간 학습 방법이 MTP-분자동역학의 물리화학적 성질 예측 정확도 향상에 활용됨
- 🔗 후속 연구: [[papers/721_Scientific_Machine_Learning_through_Physics-Informed_Neural/review]] — 물리정보 신경망의 과학적 기계학습 방법론이 MTP의 DFT 기반 원자간 포텐셜 학습을 개선할 수 있음
- 🏛 기반 연구: [[papers/427_Incorporating_Continuous_Dependence_Qualifies_Physics-Inform/review]] — 연속 의존성 정성화 방법이 MTP의 물리화학적 성질 예측에서 불확실성 정량화에 필수적임
- 🧪 응용 사례: [[papers/694_Scalable_Cross-Facility_Federated_Learning_for_Scientific_Fo/review]] — 분산 학습을 원자간 포텐셜 같은 물리 모델 훈련에 적용한다.
- 🔄 다른 접근: [[papers/372_General-Purpose_Machine-Learned_Potential_for_CrCoNi_Alloys/review]] — 원자간 포텐셜 예측을 NEP vs 다른 머신러닝 기법으로 접근한다.
- 🧪 응용 사례: [[papers/574_Neural-POD_A_Plug-and-Play_Neural_Operator_Framework_for_Inf/review]] — Neural-POD의 무한차원 함수 학습 능력이 칼슘 전해 공정의 물리화학적 성질 예측 문제에 직접 적용됨
- 🏛 기반 연구: [[papers/095_AMDAT_An_Open-Source_Molecular_Dynamics_Analysis_Toolkit_for/review]] — 기계학습 원자간 포텐셜이 MD 시뮬레이션의 물리적 예측 기반을 제공
- 🧪 응용 사례: [[papers/007_A_fine-tuned_large_language_model_based_molecular_dynamics_a/review]] — 분자동역학 자동화를 위한 MDAgent는 Machine-Learned Interatomic Potentials 연구에서 개발된 물리적 특성 예측 기법을 실제 재료 설계에 적용합니다.
