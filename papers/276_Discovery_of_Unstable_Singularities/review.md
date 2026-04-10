---
title: "276_Discovery_of_Unstable_Singularities"
authors:
  - "Yongji Wang"
  - "Mehdi Bennani"
  - "James Martens"
  - "Sébastien Racanière"
  - "Sam Blackwell"
date: "2025.09"
doi: "10.48550/arXiv.2509.14185"
arxiv: ""
score: 4.7
essence: "기계학습과 고정밀 수치해석을 결합하여 **3D 오일러 방정식, 비압축성 다공질 매질 방정식, Boussinesq 방정식에서 처음으로 불안정 특이점(unstable singularities)의 체계적인 발견**을 보여주는 연구이다. 불안정 특이점은 무한 정밀도의 초기조건이 필요하며, 미량의 교란으로도 폭발 궤적에서 벗어나는 특수한 현상으로, 이전에는 안정 특이점만 수치적으로 발견되었다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/Evolutionary_Chemistry_Models"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wang et al._2025_Discovery of Unstable Singularities.pdf"
---

# Discovery of Unstable Singularities

> **저자**: Yongji Wang, Mehdi Bennani, James Martens, Sébastien Racanière, Sam Blackwell, Alex Matthews, Stanislav Nikolov, Gonzalo Cao-Labora, Daniel S. Park, Martin Arjovsky, Daniel Worrall, Chongli Qin, Ferran Alet, Borislav Kozlovskii, Nenad Tomašev, Alex Davies, Pushmeet Kohli, Tristan Buckmaster, Bogdan Georgiev, Javier Gómez-Serrano, Ray Jiang, Ching-Yao Lai | **날짜**: 2025-09-17 | **DOI**: [10.48550/arXiv.2509.14185](https://doi.org/10.48550/arXiv.2509.14185)

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: 고정밀 자기유사해(Self-similar solution) 발견을 위한 연구 방법론. (a) 해의 발견: PINN과 Gauss-Newton 최적화기를 이용한 다단계 학습으로 자기유사 스케일링 계수 λ를 찾음. (b) 해의 분석: 선형화된 PDE의 안정성 분석을 통해 불안정 모드 특성화.*

기계학습과 고정밀 수치해석을 결합하여 **3D 오일러 방정식, 비압축성 다공질 매질 방정식, Boussinesq 방정식에서 처음으로 불안정 특이점(unstable singularities)의 체계적인 발견**을 보여주는 연구이다. 불안정 특이점은 무한 정밀도의 초기조건이 필요하며, 미량의 교란으로도 폭발 궤적에서 벗어나는 특수한 현상으로, 이전에는 안정 특이점만 수치적으로 발견되었다.

## Motivation

- **Known**: 유체 운동의 편미분방정식(3D Euler, Navier-Stokes)에서 특이점(singularity) 형성 여부는 오랫동안 미해결 문제. Luo-Hou의 축대칭 3D Euler 폭발(blow-up) 시나리오는 PINN으로 발견되고 컴퓨터 보조 증명(CAP)으로 검증됨.

- **Gap**: 기존 수치해석 기법(B-spline, 유한요소법, 스펙트럼 방법)은 안정 특이점 해에는 우수하나 **불안정 특이점은 포착 불가능**. 불안정 매니폴드 위의 지수적 불안정성으로 인해 극도의 정밀도가 필요하며, 양자화된(quantized) 해의 경우 연속해석법(continuation method)을 적용할 수 없음.

- **Why**: 경계 없는 3D Euler와 Navier-Stokes에서의 특이점은 **불안정하다고 가설**되며, 이를 발견하고 검증하는 것이 밀레니엄 상 문제 해결의 중간 단계임. 고도로 불안정한 해는 이상화된 방정식에서 점성 항이 있는 현실적인 방정식으로 전이될 때 존속할 가능성이 높음.

- **Approach**: PINN의 신경망 아키텍처와 훈련 스킴을 정교하게 설계하고 고정밀 Gauss-Newton 최적화기를 결합하여 불안정 특이점을 발견 및 검증.

## Achievement

![Figure 2](figures/fig2.webp)
*그림 2: IPM 및 Boussinesq 방정식의 자기유사 특이점. (a,b) 3번째 불안정 해의 와도(vorticity) Ω 공간 프로필. (c,d) y₁축 단면도 (안정부터 3번째 불안정까지). (e) 역 스케일 계수 vs 불안정성 차수: 두 시스템 모두에서 선형 추세 발견. (f) 발견된 스케일 계수들(초록색, 노란색)과 기존 해(파란색).*

1. **불안정 특이점의 체계적 발견**: CCF, 2D IPM, 2D Boussinesq 방정식에서 **새로운 불안정 자기유사해 계열 다수 발견**. IPM에서는 3개, Boussinesq에서는 최소 4개의 불안정 모드 식별. 각각 대응하는 스케일링 계수 λ 값을 고정밀 계산.

2. **이중정밀도 기계 정밀도 달성**: CCF의 안정 해 및 1번째 불안정 해에 대해 **거의 이중정밀도(double-float) 기계 정밀도**에 도달. GPU 하드웨어의 반올림 오차로만 제한되는 수준으로, 컴퓨터 보조 증명(CAP)의 엄격한 요구사항 충족 가능.

3. **불안정성 차수와 폭발 속도의 경험적 관계식 발견**: 역 스케일 계수(1/λ)와 불안정성 차수 간의 **단순한 선형 관계** 도출. 이는 더 높은 차수의 불안정성이 더 빠른 폭발을 야기함을 정량화.

4. **정밀도 획기적 개선**: 모든 발견된 해에 대해 이전 연구를 훨씬 상회하는 정확도 달성 (최대 잔차 10⁻²⁵ 이하).

## How

![Figure 1](figures/fig1.webp)

- **자기유사 좌표 변환(Self-similar coordinates)**: 시간 진화 시뮬레이션 문제를 정상(stationary) 자기유사 프로필 찾기로 변환. 스케일링 계수 λ로 매개변수화된 공간-시간 재스케일링으로 빠르게 발산하는 물리량 추적 어려움 제거.

- **PINN 아키텍처 설계**:
  - 수학적 귀납편향(inductive bias) 내장: 입력 좌표 변환 및 출력 필드 형성
  - 다층 퍼셉트론(MLP)으로 자기유사 공간 프로필 표현
  - PDE 잔차(residual), 경계조건 손실 동시 최소화

- **고정밀 Gauss-Newton 최적화기**: Newton 방법 기반 고차 수렴 특성으로 기계 정밀도 근처까지 수렴 가능. 표준 gradient descent 대비 우수한 수렴성.

- **다단계 정제 훈련(Multi-stage refinement training)**:
  1. 초기 PINN 훈련으로 대략적 해 및 λ 후보 찾기
  2. 후보 해의 정보로 신경망 아키텍처 개선
  3. Gauss-Newton 최적화로 반복적 정제
  4. 손실이 10⁻²⁵ 수준까지 감소 (그림 4)

- **안정성 분석**: 고정밀 해 주변에서 PDE를 선형화하여 스펙트럼 분석. 불안정 모드 개수 및 성질 특성화로 해의 차수(order) 결정.

- **검증 방법**:
  - 최대 잔차(maximum absolute residual) 계산
  - λ의 유효 자리수 검증: λ에 최소 교란값을 적용했을 때 해의 품질 변화 기준
  - 선형화 스펙트럼의 예상 성질 확인

## Originality

- **불안정 특이점의 최초 체계적 발견**: 이전 수치 기법으로 불가능했던 지수적 불안정성 극복. 양자화된 불안정 해의 발견은 학계 최초.

- **PINN과 고정밀 최적화의 새로운 조합**: 신경망의 유연성과 Gauss-Newton 최적화의 고정밀 수렴을 결합하여 이중정밀도 기계 정밀도 달성. 기존 PINN은 주로 10⁻⁶~10⁻¹² 수준의 정확도에 그침.

- **수학적 귀납편향을 통한 아키텍처 설계**: 문제의 수학적 구조(자기유사 좌표, 대칭성 등)를 명시적으로 신경망에 인코딩하여 학습 효율 및 정확도 극대화.

- **경험적 불안정성 공식**: 폭발 속도와 불안정 차수의 선형 관계식 발견은 특이점 형성의 물리적 이해를 심화.

- **CAP를 위한 필요 정밀도 달성**: 컴퓨터 보조 증명의 엄격한 요구사항(interval arithmetic 기반)을 만족하는 수치해 제공으로 향후 수학적 증명의 토대 마련.

## Limitation & Further Study

- **경계의 존재에 의존**: 현재 발견은 경계가 있는 IPM(경계 포함)과 Boussinesq, 축대칭 3D Euler에 국한. **경계 없는 3D Euler와 Navier-Stokes의 불안정 특이점 발견은 미해결**. 경계의 안정화 효과를 제거하고 경계-없는 경우로 확장하는 것이 다음 도전.

- **4번째 불안정해의 미검증**: Boussinesq의 4번째 불안정 해는 아직 엄밀히 검증되지 않음. 더 높은 차수의 불안정성 해 발견의 계산 비용 증가.

- **GPU 반올림 오차의 한계**: 이중정밀도를 초과하는 정밀도는 구조적으로 불가능. 더 높은 정밀도 요구 시 임의정밀도(arbitrary precision) 계산 필요.

- **스케일링 일반화 부재**: 발견된 경험적 불안정성 공식(선형 관계)의 이론적 근거 미제시. 왜 이러한 관계가 성립하는지의 수학적 설명 필요.

- **계산 비용**: 고정밀도 달성에 필요한 훈련 시간 및 자원 명시 부족. 실무 적용 가능성 및 확장성 평가 필요.

- **후속 연구**:
  - 컴퓨터 보조 증명(CAP)을 이용한 엄격한 수학적 검증
  - 더 높은 차수의 불안정 모드 탐색 및 특성화
  - 경계-없는 경우로의 확장 (이론적 및 기술적 돌파)
  - 다른 수학 물리 시스템(예: 화염 전파, 가우시안 곡률 흐름)으로의 방법론 전이

## Evaluation

- **Novelty**: 4.8/5 — 불안정 특이점의 최초 체계적 발견, PINN-Gauss-Newton 조합의 혁신적 정밀도 달성, 경험적 불안정성 공식 제시.

- **Technical Soundness**: 4.7/5 — 다단계 훈련, 자기유사 좌표, 선형화 안정성 분석 모두 수학적으로 엄밀하고 타당함. 4번째 불안정해 미검증이 소수 제한점.

- **Significance**: 4.9/5 — 밀레니엄 상 문제(Navier-Stokes)의 근본 해결을 향한 핵심 중간 단계. CAP 적용 가능 정밀도는 향후 수학적 증명의 토대. 유체역학의 수십 년 미해결 문제에 대한 첫 답변.

- **Clarity**: 4.6/5 — 문제 정의, 방법론, 결과 모두 명확하고 체계적. 그림 1-2로 핵심 내용 시각화 잘 됨. 다만 일부 수학 기호(예: λ의 정량적 의미)는 본문에서 더 명확히 설명 필요.

- **Overall**: 4.7/5

**총평**: 불안정 특이점이라는 오랫동안 포착 불가능했던 수학적 현상을 고정밀 머신러닝과 수치해석의 결합으로 처음 발견하고 측정한 획기적 연구. 경계 조건 확장과 CAP 연계를 통해 밀레니엄 상 문제 해결의 구체적

## Related Papers

- 🏛 기반 연구: [[papers/103_Architectures_variants_and_performance_of_neural_operators_A/review]] — 신경 연산자 아키텍처는 불안정 특이점 발견에 필요한 고정밀 수치해석의 기반이 됨
- 🔗 후속 연구: [[papers/619_Physics_Informed_Deep_Learning_Part_I_Data-driven_Solutions/review]] — 물리 정보 기반 딥러닝 방법론이 오일러 방정식 특이점 연구에 적용될 수 있음
- 🏛 기반 연구: [[papers/275_Discovering_symbolic_differential_equations_with_symmetry_in/review]] — 수학적 대칭성과 불안정 특이점 발견은 물리 불변량 보존 원리를 공유합니다
- 🔄 다른 접근: [[papers/217_Chiral_spin_symmetry_and_hot_QCD/review]] — 불안정 특이점 발견과 QCD 상 통일 설명의 다른 물리학적 접근법
