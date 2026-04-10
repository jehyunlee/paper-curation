---
title: "759_SLE-FNO_Single-Layer_Extensions_for_Task-Agnostic_Continual"
authors:
  - "Mahmoud Elhadidy"
  - "Roshan M. D'Souza"
  - "Amirhossein Arzani"
date: "2026.03"
doi: "N/A"
arxiv: ""
score: 4.0
essence: "과학기계학습(SciML) 모델의 배포 후 분포 변화(distribution shift)에 적응하면서 이전 학습 지식을 보존해야 하는 지속학습(continual learning) 문제를 해결하기 위해, Fourier Neural Operator(FNO)에 단일 레이어 확장(Single-Layer Extension)을 결합한 SLE-FNO를 제안한다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/Evolutionary_Chemistry_Models"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Elhadidy et al._2026_SLE-FNO Single-Layer Extensions for Task-Agnostic Continual Learning in Fourier Neural Operators.pdf"
---

# SLE-FNO: Single-Layer Extensions for Task-Agnostic Continual Learning in Fourier Neural Operators

> **저자**: Mahmoud Elhadidy, Roshan M. D'Souza, Amirhossein Arzani | **날짜**: 2026-03-20 | **DOI**: N/A

---

## Essence

과학기계학습(SciML) 모델의 배포 후 분포 변화(distribution shift)에 적응하면서 이전 학습 지식을 보존해야 하는 지속학습(continual learning) 문제를 해결하기 위해, Fourier Neural Operator(FNO)에 단일 레이어 확장(Single-Layer Extension)을 결합한 SLE-FNO를 제안한다.

## Motivation

- **Known**: 일반적으로 과학기계학습 모델은 훈련 데이터와 동일한 분포에서 추론되도록 가정되어 설계됨. 기존 지속학습 연구는 주로 분류 문제에 집중되어 있으며, 과학기계학습 분야의 함수-함수 매핑 회귀 문제에 대한 연구는 부족.

- **Gap**: 새로운 실험 조건이나 시뮬레이션 영역이 나타날 때, 기존 데이터 접근 없이 모델을 업데이트해야 하는데, 이는 재앙적 망각(catastrophic forgetting)과 외삽(extrapolation) 능력 간의 균형 문제 야기. 기존 지속학습 방법들의 과학기계학습 적용에서의 효과성 미검증.

- **Why**: 유체역학, 심혈관 흐름 등 복잡한 물리 시뮬레이션은 기하학, 경계조건, 흐름 영역 변화로 인해 비자명한 해의 변화 초래. 이러한 설정에서 효율적이고 파라미터 오버헤드가 적은 지속학습 방법 필요.

- **Approach**: FNO에 특화된 가벼운 단일 레이어 확장 아키텍처 제안 + 주요 지속학습 방법들(EWC, LwF, 재현(replay), GEM, OGD, PiggyBack, LoRA) 포괄적 비교 + 동맥류 혈류에서 일시적 농도 필드를 시간 평균 벽 전단응력(TAWSS)으로 매핑하는 실제 문제 적용.

## Achievement

![Figure 1: 동맥류 기하학 및 문제 설정](figures/fig1.webp)
*동맥류 기하학(a), 메시(b), 경계 조건(c), 농도 슬라이스와 TAWSS(d), 각 데이터셋의 공간 파라미터(e)*

![Figure 4: SLE-FNO 아키텍처](figures/fig4.webp)
*훈련 단계(a)에서는 기존 FNO가 새 데이터를 처리하고, 추론 단계(b)에서는 과제별 확장 레이어가 적응된 예측 제공*

1. **완전한 망각 방지**: SLE-FNO는 정확도 저하 없이 영점 망각(zero forgetting) 달성. 재현 기반 및 아키텍처 기반 방법들 중 최고 성능 보유.

2. **파라미터 효율성**: 새로운 과제당 1.5-4.4%의 파라미터만 추가하여, PiggyBack이나 완전 모델 재복제에 비해 현저히 낮은 오버헤드. 네트워크 크기 제어 가능.

3. **과제-무관(Task-Agnostic) 학습**: 훈련/추론 중 과제 라벨 불필요. 통합된 OOD 검출기로 자동 과제 식별 달성, 실험에서 100% 과제 식별 정확도.

4. **다단계 지속학습 분석**: 4개의 순차적, 분포 외(out-of-distribution) 설정에서 230개 전산유체역학 시뮬레이션 기반 데이터셋으로 상세한 종단적(longitudinal) 지속학습 평가.

5. **소수 샘플 미세조정 분석**: 제한된 새 데이터 하에서의 적응, 지식 보존, 예측 견고성에 대한 통찰 제공.

## How

![Figure 2: FNO 아키텍처 개요](figures/fig2.webp)
*FNO의 입력 들어올리기, 푸리에 블록 스택, 최종 투영 구조*

![Figure 3: 지속학습 방법 비교](figures/fig3.webp)
*정규화 기반(EWC) 방법의 제약 기제, 그리고 기타 주요 방법들의 개념*

**SLE-FNO 방법론**:

- **기본 구조**: 기존 FNO 모델 고정, 각 새 과제마다 경량 단일 푸리에 블록 추가
- **푸리에 연산 보존**: 확장 레이어도 스펙트럼 구조 유지하여 FNO의 연산자 학습 특성 손상 방지
- **과제별 라우팅**: 추론 시 OOD 입력에 대해 대응하는 과제별 확장 레이어 선택
- **OOD 검출 메커니즘**: 입력 데이터의 분포 이동을 감지하여 자동으로 적절한 과제 모듈 활성화

**지속학습 범주별 방법**:

- **정규화 기반** (EWC, LwF): 파라미터 중요도 가중치 또는 이전 모델 출력 제약
- **재현 기반**: 과거 샘플 버퍼 유지 및 새 데이터와 혼합
- **최적화 기반** (OGD, GEM): 그래디언트 방향 제어 또는 손실 제약
- **아키텍처 기반** (PiggyBack, LoRA, SLE-FNO): 파라미터 마스킹, 저랭크 적응, 또는 동적 확장

## Originality

- **과학기계학습 지속학습의 새로운 문제 정의**: 함수-함수 회귀 매핑에서 분포 변화 적응 문제를 SciML 맥락에서 처음으로 체계적으로 다룸. 기존 연구는 FNO 기반 operator learning에서 지속학습을 거의 다루지 않음.

- **푸리에 구조 보존 설계**: 확장 레이어가 푸리에 블록 형태로 설계되어, 단순 MLP 추가가 아닌 연산자 학습 특성 유지. 이는 FNO 아키텍처에 특화된 novel adaptation.

- **과제-무관 OOD 검출 통합**: 과제 라벨 없이 자동으로 분포 변화를 탐지하고 대응 모듈 선택. 기존 방법들은 주로 과제 라벨 또는 경계 조건에 의존.

- **포괄적 비교 벤치마크**: 5가지 지속학습 범주에서 2개씩 방법(총 7개 기준선) 비교. 이전 SciML 지속학습 연구들(한두 개 방법 비교)에 비해 훨씬 상세.

- **실제 의료 응용 문제**: 단순 인공 데이터가 아닌 동맥류 혈류 시뮬레이션 문제 활용. 기하학 및 흐름 조건 변화가 물리적 의미를 가짐.

## Limitation & Further Study

- **단일 과학 문제 평가**: 동맥류 TAWSS 예측 문제에만 적용. 다양한 SciML 과제(열전달, 구조역학, 난류 등)에서의 일반화 가능성 미검증.

- **OOD 검출 메커니즘 상세 설명 부족**: 논문 초안에서 OOD 검출의 기술적 구현(예: 임계값 설정, 거리 메트릭)에 대한 명확한 기술 필요.

- **큰 분포 변화 시나리오 부족**: 현재 평가는 4개 순차 과제로 제한. 더 극단적인 분포 변화나 더 많은 과제 수열에서의 성능 미검토.

- **계산 효율성 분석 미흡**: 파라미터 수는 비교되나, 훈련/추론 시간, 메모리 사용량 등 실제 계산 효율성 평가 부재.

- **물리 보존 특성 미검증**: 확장 레이어 추가가 FNO의 기본 물리적 특성(예: 해의 부드러움, 편미분방정식 구조)을 어느 정도 보존하는지 미분석.

**향후 연구**:

- 다양한 SciML 영역(난류, 열전달, 구조역학)에서 SLE-FNO 적용 및 일반화 연구
- 비선형 또는 다모달(multimodal) OOD 시나리오에서의 OOD 검출 강건성 향상
- 수백 개 이상의 순차 과제 환경에서 확장성 검토
- 물리-정보 기반 손실 함수와 SLE-FNO 결합으로 물리 보존성 강화
- 동적 과제 경계(task boundaries)가 불명확한 비정형 분포 변화 대응


## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 과학기계학습에서 실제 배포 후 분포 변화 적응이라는 과소 연구 문제를 다루며, FNO에 특화된 경량 지속학습 방법(SLE-FNO)을 제시한다. 포괄적 벤치마크, 영점 망각 달성, 낮은 파라미터 오버헤드, 자동 OOD 검출 등이 주요 강점이다. 다만 단일 심혈관 응용 문제만 평가되었고, OOD 검출 메커니즘과 물리 보존 특성에 대한 기술적·이론적 깊이가 부족하다. SciML 커뮤니티에 실질적 기여를 하는 견실한 연구이나, 광범위한 일반화 입증과 기술적 완성도 향상이 필요하다.

## Related Papers

- 🧪 응용 사례: [[papers/503_LLM-ODE_Data-driven_Discovery_of_Dynamical_Systems_with_Larg/review]] — 과학 머신러닝 모델의 지속학습이 LLM 기반 동역학 시스템 발견에서 새로운 데이터 적응에 적용된다.
- 🏛 기반 연구: [[papers/422_Improving_generalization_of_robot_locomotion_policies_via_sh/review]] — 로봇 운동 정책의 일반화 개선이 SLE-FNO의 분포 변화 적응과 지속학습의 기반 원리를 제공한다.
- 🔗 후속 연구: [[papers/574_Neural-POD_A_Plug-and-Play_Neural_Operator_Framework_for_Inf/review]] — 플러그앤플레이 신경 연산자 프레임워크가 FNO의 단일 레이어 확장을 더 범용적인 인컨텍스트 추론으로 확장한다.
- 🏛 기반 연구: [[papers/503_LLM-ODE_Data-driven_Discovery_of_Dynamical_Systems_with_Larg/review]] — 과학 머신러닝에서의 지속학습 문제가 LLM 기반 동역학 시스템 발견의 지식 보존과 적응에 기반을 제공한다.
