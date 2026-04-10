---
title: "891_Zero-shot_sim-to-real_transfer_for_reinforcement_learning-ba"
authors:
  - "Hsin-Jung Yang"
  - "Mahsa Khosravi"
  - "Benjamin Walt"
  - "Girish Krishnan"
  - "Soumik Sarkar"
date: "2025"
doi: "10.48550/arXiv.2504.16916"
arxiv: ""
score: 4.2
essence: "소프트 연속 팔(Soft Continuum Arms, SCAs)의 비선형 동역학을 다루기 위해 운동학과 기계적 특성을 분리한 강화학습(RL) 기반 시각 서보잉 프레임워크를 제시하며, 시뮬레이션에서만 학습한 정책을 실제 하드웨어에 직접 배포하여 67% 성공률의 제로샷 심-투-리얼 전이(zero-shot sim-to-real transfer)를 달성했다."
tags:
  - "cat/Reinforcement_Learning_and_Self-Verification"
  - "sub/Robot_Control_and_Policy_Robustness"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Yang et al._2025_Zero-shot sim-to-real transfer for reinforcement learning-based visual servoing of soft continuum ar.pdf"
---

# Zero-shot sim-to-real transfer for reinforcement learning-based visual servoing of soft continuum arms

> **저자**: Hsin-Jung Yang, Mahsa Khosravi, Benjamin Walt, Girish Krishnan, Soumik Sarkar | **날짜**: 2025 | **DOI**: [10.48550/arXiv.2504.16916](https://doi.org/10.48550/arXiv.2504.16916)

---

## Essence

![Figure 1](https://arxiv.org/html/2504.16916v1/x1.png)
*그림 1: 시뮬레이션(위)과 실제 하드웨어(아래)에서 시각 서보잉을 수행하는 제안된 프레임워크의 개요*

소프트 연속 팔(Soft Continuum Arms, SCAs)의 비선형 동역학을 다루기 위해 운동학과 기계적 특성을 분리한 강화학습(RL) 기반 시각 서보잉 프레임워크를 제시하며, 시뮬레이션에서만 학습한 정책을 실제 하드웨어에 직접 배포하여 67% 성공률의 제로샷 심-투-리얼 전이(zero-shot sim-to-real transfer)를 달성했다.

## Motivation

- **Known**: SCAs의 무한 자유도와 비선형 동역학 때문에 모델링과 제어가 어렵다. 기존 RL 기반 접근법들은 2D 작업이나 고가의 센싱 인프라(Vicon 모션 캡처)에 제한되어 있으며, 특히 제로샷 심-투-리얼 전이를 시연한 연구가 없다.

- **Gap**: 기존 연구들은 ① 3D 작업 공간에서의 확장성 부족, ② 광범위한 센싱 의존성, ③ 시뮬레이션 검증만 수행(실제 배포 없음), ④ 제로샷 전이 달성 실패 등의 문제를 보이고 있다. 또한 고충실도 시뮬레이션(Cosserat rod model)은 계산 비용이 높아 RL 학습에 부적합하다.

- **Why**: SCAs는 지속적 변형과 높은 유순성(compliance)을 보이기 때문에 강체 로봇의 심-투-리얼 기법을 직접 적용할 수 없다. 동시에 최소한의 센싱으로도 실용적인 제어가 필요하다.

- **Approach**: 운동학(kinematics)을 구성 공간(configuration space)에서 처리하는 RL 컨트롤러와 기계적 불확실성을 보정하는 국소 컨트롤러(local controller)로 이원화하여, 하드웨어 변동에 강건한 정책을 학습한다.

## Achievement

![Figure 2](https://arxiv.org/html/2504.16916v1/x2.png)
*그림 2: (a) 학습과 배포 프레임워크, (b) 운동학과 기계적 특성의 분리, (c) 국소 컨트롤러의 반복적 정제 루프*

1. **시뮬레이션 성능**: SAC(Soft Actor-Critic) 알고리즘으로 학습한 RL 운동학 컨트롤러가 99.8% 성공률 달성

2. **제로샷 심-투-리얼 전이**: 시뮬레이션에서만 학습한 정책을 BR2 조작기 실제 하드웨어에 직접 배포하여 67% 성공률로 작동 → 기존 연구를 초과하는 성과

3. **최소 센싱 구현**: 멀티 카메라 추적 시스템 대신 기저부 카메라 + 원위부(distal) 카메라 + 간단한 추적기만 사용하여 시스템 복잡도 감소

4. **3D 시각 서보잉**: 3D 공간에서 표적 위치 추적 및 물체 중심화(centering) 작업 성공

## How

![Figure 3](https://arxiv.org/html/2504.16916v1/x3.png)
*그림 3: 작업 공간 설정과 샘플링된 표적 위치*

- **이원 계층 제어 구조**
  - **RL 운동학 컨트롤러**: 구성 공간(곡률 κ, 비틀림 τ)에서 고수준 운동 목표 생성 → 하드웨어 특성과 무관하게 전이 가능
  - **국소 컨트롤러**: RL이 출력한 목표 구성을 반복적 보정 루프로 실제 구동 신호로 변환

- **구성 공간 모델링**
  - 상수 곡률·비틀림 모델(Constant Curvature and Torsion, CCT) 사용: 폐형해(closed-form solution) 제공으로 빠른 시뮬레이션 가능
  - Kirchhoff 막대 이론 기반의 정적 평형 방정식 적용

- **시각 피드백 처리**
  - 개방어휘 물체 검출 모델(open-vocabulary object detection)로 영상에서 과제 관련 특성 추출
  - 기저부/원위부 카메라 이중 시점 활용

- **강화학습 알고리즘**
  - **SAC(Soft Actor-Critic) 선택 이유**: 표본 효율성(sample efficiency) + 엔트로피 정규화로 탐색 성능 향상 및 부분최적(suboptimal) 정책 수렴 방지

- **시뮬레이션 환경**: 저충실도 모델로 학습 가속화 → 실제 하드웨어의 비선형성은 국소 컨트롤러가 흡수

## Originality

- **운동학-동역학 분리의 명시적 설계**: 기존 연구는 전체 동역학을 모델링하려 했으나, 본 연구는 구성 공간에서만 RL을 적용하여 하드웨어 의존성을 제거 → 매우 참신한 접근

- **제로샷 심-투-리얼 전이 달성**: 표 1에서 볼 수 있듯이 기존 모든 SCA 제어 연구가 이를 달성하지 못했으나, 본 연구가 최초로 시연

- **최소 센싱 원칙**: 고가의 모션 캡처 시스템 없이 카메라 기반 피드백만 사용하면서도 3D 작업 공간 달성

- **BR2의 복합 변형 모델링**: 동시 굽힘과 비틀림을 비대칭 FREE(Fiber Reinforced Elastomeric Enclosure) 구성으로 처리하는 것이 기존 연구보다 정교함

## Limitation & Further Study

- **67% 성공률의 한계**: 시뮬레이션 99.8%와 실제 67% 간 큰 격차 존재 → 나머지 1/3 실패 원인 분석 필요 (예: 센서 노이즈, 마모, 재료 특성 변화)

- **단일 섹션 BR2만 검증**: 다중 섹션(multi-section) SCA에의 확장 가능성은 미검증

- **국소 컨트롤러 의존성**: Cosserat 모델 기반 초기 Configuration-to-Actuation 맵이 필요 → 완전한 데이터 주도 방식이 아님

- **시각 인식 신뢰도**: 개방어휘 물체 검출의 오류 전파 영향 미분석

- **제어 대역폭**: 반복적 보정 루프의 수렴 속도와 실시간 성능 제약 미언급

- **후속 연구 방향**:
  - 도메인 랜더마이제이션(domain randomization) 등 다른 심-투-리얼 기법과의 비교
  - 적대적 학습(adversarial training)으로 시뮬레이터 격차 감소
  - 멀티 섹션 SCA로의 확장
  - 접촉 동역학(contact dynamics)이 있는 작업으로 응용

## Evaluation

- **Novelty**: 4.5/5
  - 운동학-동역학 분리 개념 신선하고, 제로샷 전이 최초 달성으로 높은 점수
  - 다만 각 구성 요소(SAC, CCT 모델, 국소 제어)는 기존 기법 조합

- **Technical Soundness**: 4/5
  - 이론적 기초(Kirchhoff 막대, CCT 모델) 견고함
  - 실험 설계 및 결과 해석이 명확함
  - 하지만 67% 성공률의 저하에 대한 심층 분석 부족, 통계적 유의성 검증 미흡

- **Significance**: 4.5/5
  - SCA 제어 분야에 실질적 진전 가져옴 (제로샷 전이 첫 성공)
  - 최소 센싱 원칙이 로봇공학 전반에 영향력 있음
  - 다만 67% 성공률은 산업 배포 수준으로 아직 부족

- **Clarity**: 4/5
  - 핵심 아이디어(이원 계층, 운동학 분리)가 명확히 설명됨
  - Figure 2가 프레임워크를 직관적으로 제시
  - 다만 국소 컨트롤러의 구체적 알고리즘 서술 간략함, 실패 케이스 분석 부재

- **Overall**: 4.2/5

**총평**: 본 논문은 소프트 연속 팔 제어에 획기적인 접근법을 제시하며 제로샷 심-투-리얼 전이라는 미달성 과제를 최초로 성공시킨 점에서 학술적 가치가 높으나, 실제 성공률 67%는 현장 적용에 향상 여지를 남기고 있다. 이원 계층 아키텍처와 최소 센싱 원칙은 앞으로의 소프트 로보틱스 연구에 유용한 설계 가이드라인을 제공할 것으로 예상된다.

## Related Papers

- 🔄 다른 접근: [[papers/395_Guided_by_guardrails_Control_barrier_functions_as_safety_ins/review]] — 두 논문 모두 로봇 제어의 안전성을 다루되 소프트 연속 팔은 시뮬레이션 전이, 제어 장벽 함수는 안전 제약에 중점을 둔다.
- 🔗 후속 연구: [[papers/422_Improving_generalization_of_robot_locomotion_policies_via_sh/review]] — 일반화 성능 향상을 위한 샤프니스 인식 최소화 기법은 소프트 연속 팔의 심-투-리얼 전이 성능을 더욱 개선할 수 있다.
- 🏛 기반 연구: [[papers/354_From_GPU_Engineering_to_Scientific_Discovery_Parallelism_Tec/review]] — GPU 엔지니어링에서 과학적 발견까지의 병렬화 기법 연구는 소프트 연속 팔의 강화학습 훈련 효율성 향상에 계산 최적화 방법론을 제공한다.
- 🔄 다른 접근: [[papers/395_Guided_by_guardrails_Control_barrier_functions_as_safety_ins/review]] — 두 논문 모두 로봇 제어 안전성을 다루되 제어 장벽 함수는 안전 제약, 소프트 연속 팔은 시뮬레이션 전이에 중점을 둔다.
- 🏛 기반 연구: [[papers/422_Improving_generalization_of_robot_locomotion_policies_via_sh/review]] — 샤프니스 인식 최소화를 통한 일반화 성능 향상은 소프트 연속 팔의 심-투-리얼 전이 성공률을 더욱 개선할 수 있는 이론적 근거를 제공한다.
