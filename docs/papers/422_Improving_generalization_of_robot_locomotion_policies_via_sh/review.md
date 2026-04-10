---
title: "422_Improving_generalization_of_robot_locomotion_policies_via_sh"
authors:
  - "S. Bochem"
  - "E. Gonzalez-Sanchez"
  - "Y. Bicker"
  - "G. Fadini (ETH Zürich)"
date: "2024"
doi: "arXiv:2411.19732"
arxiv: ""
score: 4.0
essence: "미분 가능 시뮬레이터 기반의 1차 정책 최적화(first-order policy gradient) 방법은 샘플 효율성은 우수하나 일반화 성능이 떨어진다는 문제를 해결하기 위해, Sharpness-Aware Minimization (SAM) 기법을 로봇 강화학습에 처음 도입한 연구이다. SHAC-ASAM 알고리즘을 통해 손실 함수의 평평한 극소점(flat minima)을 찾음으로써 접촉 기반 로봇 제어 환경에서 견고성과 효율성을 동시에 달성한다."
tags:
  - "cat/Reinforcement_Learning_and_Self-Verification"
  - "sub/Robot_Control_and_Policy_Robustness"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Song et al._2024_Improving generalization of robot locomotion policies via sharpness-aware reinforcement learning.pdf"
---

# Improving generalization of robot locomotion policies via sharpness-aware reinforcement learning

> **저자**: S. Bochem, E. Gonzalez-Sanchez, Y. Bicker, G. Fadini (ETH Zürich) | **날짜**: 2024 | **DOI**: [arXiv:2411.19732](https://arxiv.org/abs/2411.19732)

---

## Essence

미분 가능 시뮬레이터 기반의 1차 정책 최적화(first-order policy gradient) 방법은 샘플 효율성은 우수하나 일반화 성능이 떨어진다는 문제를 해결하기 위해, Sharpness-Aware Minimization (SAM) 기법을 로봇 강화학습에 처음 도입한 연구이다. SHAC-ASAM 알고리즘을 통해 손실 함수의 평평한 극소점(flat minima)을 찾음으로써 접촉 기반 로봇 제어 환경에서 견고성과 효율성을 동시에 달성한다.

## Motivation

- **Known**: 
  - Brax, DiffPD 등의 미분 가능 시뮬레이터와 SHAC/AHAC 같은 1차 정책 그래디언트 방법이 뛰어난 샘플 효율성 제공
  - 심층 학습에서 평평한 극소점이 더 좋은 일반화 성능과 분포 외(out-of-distribution) 강건성과 연관되어 있음을 이론적, 실증적으로 증명
  
- **Gap**: 
  - 1차 정책 최적화 방법들이 노이즈와 환경 변동성에 대한 강건성이 부족함
  - 기존 강화학습에서 SAM/ASAM 같은 샤프니스 인식 최적화 기법이 거의 미적용됨
  - 시뮬레이션-실제 환경 갭(sim-to-real gap) 극복을 위해 효율성과 강건성의 균형이 필요

- **Why**: 
  - 미분 가능 시뮬레이터의 근사화로 인한 바이어스와 고분산이 날카로운 손실 함수 지형(sharp loss landscape) 야기
  - 접촉 기반 환경의 비미분 가능 동역학으로 인해 정책이 과도하게 손실 함수의 좁은 계곡에 갇힘

- **Approach**: 
  - ASAM(Adaptive Sharpness-Aware Minimization) 옵티마이저를 SHAC에 통합
  - 미니맥스 최적화 문제를 풀어 평평한 극소점 탐색
  - 스케일 불변성(scale-invariance)을 갖춘 적응형 섭동(adaptive perturbation) 적용

## Achievement

![Figure 2: Average episode reward as function of the noise strength for SHAC, SHAC-ASAM, and PPO](figures/fig2.webp)
*액션 노이즈 강도에 따른 평균 에피소드 보상 비교*

1. **강건성 향상**: SHAC-ASAM이 표준 SHAC 대비 액션 노이즈(action noise)에 대해 유의미하게 높은 허용 범위 달성. 특히 Ant와 Humanoid 환경에서 노이즈가 증가해도 성능 저하가 적음

2. **일반화 성능**: 0차 방법(PPO)과 유사한 수준의 일반화 성능을 달성하면서도 1차 방법의 샘플 효율성 유지

![Figure 3: Average episode reward as a function of the contact Coulomb friction for SHAC, SHAC-ASAM, and PPO](figures/fig3.webp)
*접촉 마찰 계수 변화에 따른 성능 비교*

3. **환경 변동성 대응**: 쿨롱 마찰(Coulomb friction) 등 환경 파라미터 변화에 대한 적응 능력 향상

## How

![Figure 1: Average episode reward heatmaps for SHAC (left) and PPO (right) policies under varying noise conditions](figures/fig1.webp)
*다양한 노이즈 조건에서의 정책 성능 히트맵*

- **SHAC 기반**: 짧은 수평선(short horizon) 윈도우 기반의 미분 가능 시뮬레이션으로 샘플 효율성 확보

- **ASAM 통합**:
  - 매 에피소드마다 미니맥스 최적화 문제 해결
  - 1단계: 스케일 불변 섭동 $\epsilon_t = \rho \frac{T^2_{\theta_t}\nabla L(\theta_t)}{\|T_{\theta_t}\nabla L(\theta_t)\|_2}$ 계산
  - 2단계: 섭동된 파라미터에서 그래디언트 재계산 후 정책 업데이트
  - 정규화 연산자(normalization operator) $T_{\theta_t} = \text{diag}(|\theta_t|)$로 파라미터 스케일에 따른 적응

- **계산 효율**:
  - 최적화 단계당 2회의 전방향-역방향 패스(forward-backward pass) 필요로 계산 비용 증가
  - Adam 옵티마이저를 기반으로 하는 래퍼(wrapper) 구현으로 기존 파이토치 파이프라인에 용이한 통합

- **섭동 강도 제어**:
  - 하이퍼파라미터 $\rho$로 $\ell_2$ 노름 볼(norm ball) 반경 제어
  - 환경 특성에 맞게 조정 가능한 트레이드오프(Figure 4)

## Originality

- **첫 적용**: 강화학습 분야에서 SAM/ASAM 같은 샤프니스 인식 최적화 기법을 1차 정책 그래디언트 방법에 처음 도입

- **미분 가능 시뮬레이터 특화**: 미분 가능 시뮬레이터의 그래디언트 편향 문제를 샤프니스 관점에서 접근한 새로운 해석

- **스케일 불변성**: ASAM의 적응형 정규화 연산자를 활용한 파라미터 스케일 불변 정책 학습

- **일반화 가능성**: SHAC뿐 아니라 AHAC, PODS 등 다른 미분 가능 시뮬레이터 기반 알고리즘에도 원칙적으로 적용 가능함을 제시

## Limitation & Further Study

- **계산 비용**: 최적화 단계당 2배의 그래디언트 계산 필요로 학습 시간 약 2배 증가. ESAM(Efficient ESAM, 40% 오버헤드)과 같은 경량화 기법 적용 가능성 언급 부족

- **실제 로봇 검증 부재**: 모든 실험이 시뮬레이션 환경(MuJoCo 기반)에서만 수행되어 실제 sim-to-real 전이 성과 검증 필요

- **하이퍼파라미터 민감도**: $\rho$ 값 선택이 성능에 미치는 영향이 크나, 자동 선택 메커니즘 부재

- **이론적 분석 부족**: 미분 가능 시뮬레이터의 바이어스가 왜 날카로운 극소점을 유발하는지에 대한 수학적 증명 부재

- **후속 연구 방향**:
  - 경량 샤프니스 기법(SAF, ESAM)을 이용한 계산 효율성 개선
  - 실제 로봇 플랫폼에서의 sim-to-real 전이 검증
  - 다양한 접촉 모델(contact model)과 환경에서의 일반화 성능 평가
  - 적응형 $\rho$ 선택 알고리즘 개발

## Evaluation

- **Novelty (독창성)**: 4/5
  - 강화학습에 SAM/ASAM 적용은 새로우나, 두 기법의 조합 자체는 기술적으로 직관적

- **Technical Soundness (기술적 타당성)**: 4/5
  - ASAM 통합 방법론은 건전하고 구현이 명확하나, 미분 가능 시뮬레이터의 그래디언트 오류와 샤프니스 관계에 대한 이론적 분석 부족

- **Significance (중요성)**: 4/5
  - sim-to-real 갭 극복이라는 로봇 공학의 실질적 문제 해결에 기여하나, 시뮬레이션 실험만으로는 영향력 제한적

- **Clarity (명확성)**: 4/5
  - 논문 구조와 방법론 설명이 명확하나, 계산 비용-성능 트레이드오프에 대한 정량적 분석 미흡

- **Overall**: 4/5

**총평**: SHAC과 ASAM의 결합을 통해 미분 가능 시뮬레이터 기반 정책 학습에서 샘플 효율성과 강건성 사이의 균형을 효과적으로 달성한 실용적 접근이나, 실제 로봇 검증과 이론적 분석 강화가 필요하다.

## Related Papers

- 🏛 기반 연구: [[papers/891_Zero-shot_sim-to-real_transfer_for_reinforcement_learning-ba/review]] — 샤프니스 인식 최소화를 통한 일반화 성능 향상은 소프트 연속 팔의 심-투-리얼 전이 성공률을 더욱 개선할 수 있는 이론적 근거를 제공한다.
- 🔗 후속 연구: [[papers/688_Robustness_evaluation_of_offline_reinforcement_learning_for/review]] — 오프라인 강화학습의 견고성 평가 연구는 샤프니스 인식 최소화 기법이 실제 로봇 제어에서 어떤 견고성 개선을 가져오는지 실증적으로 분석할 수 있다.
- 🧪 응용 사례: [[papers/863_Value_iteration_for_learning_concurrently_executable_robotic/review]] — 동시 실행 가능한 로봇 제어 태스크 학습에서 샤프니스 인식 최소화는 각 태스크의 일반화 성능을 향상시켜 더 안정적인 멀티태스킹을 가능하게 한다.
- 🏛 기반 연구: [[papers/759_SLE-FNO_Single-Layer_Extensions_for_Task-Agnostic_Continual/review]] — 로봇 운동 정책의 일반화 개선이 SLE-FNO의 분포 변화 적응과 지속학습의 기반 원리를 제공한다.
- 🔗 후속 연구: [[papers/449_Kimi_k15_Scaling_reinforcement_learning_with_llms/review]] — 로봇 정책의 일반화 성능 향상을 위한 SAM 기법은 Kimi k1.5의 정책 최적화 방법론에 샤프니스 인식 최소화를 도입할 수 있다.
- 🔗 후속 연구: [[papers/891_Zero-shot_sim-to-real_transfer_for_reinforcement_learning-ba/review]] — 일반화 성능 향상을 위한 샤프니스 인식 최소화 기법은 소프트 연속 팔의 심-투-리얼 전이 성능을 더욱 개선할 수 있다.
- 🔗 후속 연구: [[papers/662_Reinforcement_Learning_for_Dynamic_Microfluidic_Control/review]] — 샤프니스 인식 최소화를 통한 일반화 개선은 오프라인 강화학습의 견고성 문제를 모델 최적화 관점에서 해결하는 추가적인 방법론을 제시한다.
- 🏛 기반 연구: [[papers/863_Value_iteration_for_learning_concurrently_executable_robotic/review]] — 샤프니스 인식 최소화를 통한 일반화 성능 향상은 동시 실행 로봇 태스크 학습에서 각 태스크의 안정적인 수렴과 성능 개선에 이론적 토대를 제공한다.
- 🧪 응용 사례: [[papers/003_A_comprehensive_survey_of_cross-domain_policy_transfer_for_e/review]] — 로봇 보행 정책의 일반화 개선을 통해 크로스 도메인 정책 전이의 실제 적용 사례를 제시한다.
