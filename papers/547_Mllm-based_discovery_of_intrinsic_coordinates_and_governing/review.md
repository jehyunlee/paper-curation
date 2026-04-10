---
title: "547_Mllm-based_discovery_of_intrinsic_coordinates_and_governing"
authors:
  - "Ruikun Li"
  - "Yan Lu*"
  - "Shixiang Tang"
  - "Biqing Qi"
  - "Wanli Ouyang"
date: "2025"
doi: "미기재"
arxiv: ""
score: 4.0
essence: "본 논문은 멀티모달 대규모 언어 모델(MLLM)을 활용하여 고차원 동영상 데이터로부터 저차원 물리 좌표계와 지배 방정식을 자동으로 발견하는 Video Equation Reasoning (VER) 프레임워크를 제안한다. 향상된 시각적 프롬프트와 가설-평가-반복 추론 체인을 통해 종래 방법 대비 외삽 정확도를 약 26.96% 향상시킨다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/Multimodal_Scientific_Reasoning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Li et al._2025_Mllm-based discovery of intrinsic coordinates and governing equations from high-dimensional data.pdf"
---

# MLLM-based discovery of intrinsic coordinates and governing equations from high-dimensional data

> **저자**: Ruikun Li, Yan Lu*, Shixiang Tang, Biqing Qi, Wanli Ouyang | **날짜**: 2025 | **소속**: Shanghai Artificial Intelligence Laboratory | **DOI**: 미기재

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: 제안된 비디오 방정식 추론 프레임워크의 전체 파이프라인. 고차원 관측 데이터로부터 물리 좌표계 발견과 지배 방정식 추론을 수행한다.*

본 논문은 멀티모달 대규모 언어 모델(MLLM)을 활용하여 고차원 동영상 데이터로부터 저차원 물리 좌표계와 지배 방정식을 자동으로 발견하는 Video Equation Reasoning (VER) 프레임워크를 제안한다. 향상된 시각적 프롬프트와 가설-평가-반복 추론 체인을 통해 종래 방법 대비 외삽 정확도를 약 26.96% 향상시킨다.

## Motivation

- **Known**: 
  - 과학 데이터로부터 지배 방정식 발견(symbolic regression)은 시스템 이해에 필수적
  - 깊은 학습 기반의 신경망과 물리 엔진 통합으로 고차원 데이터로부터 물리량 추론 가능
  - LLM은 사전학습 지식을 활용한 효율적인 문제 해결에 탁월함

- **Gap**: 
  - 기존 방법들은 물리 좌표 발견과 방정식 추론을 분리하거나, 사전에 방정식 형태와 상태 차원을 알아야 함
  - 고차원 데이터의 지수적으로 확장하는 방정식 공간에서 효율적인 탐색이 어려움
  - 고차원 데이터에서 저차원 물리 좌표를 자동으로 발견하면서 동시에 방정식을 구하는 문제의 해결책 부재

- **Why**: 
  - MLLM의 시각 인식 능력(visual perception)과 사전학습 과학 지식(domain knowledge)이 고차원 방정식 공간 탐색에 효과적으로 활용될 수 있음
  - 시각적 프롬프트 강화를 통해 MLLM의 공간 이해도 향상 가능

- **Approach**: 
  - 물리 좌표 발견: 픽셀 좌표계(rigid body motion)와 잠재 좌표계(oscillatory dynamics) 두 가지 유형에 대한 시각적 위치 지정 도구 설계
  - 방정식 추론: MLLM의 과학 지식을 활용한 가설 생성-최적화-평가 전략 구현

## Achievement

![Figure 2](figures/fig2.webp)
*그림 2: 픽셀 좌표 시스템의 추론 결과. 파란색은 그라운드 트루스, 녹색과 회색 점선은 제안 방법의 궤적*

![Figure 3](figures/fig3.webp)
*그림 3: 잠재 좌표 시스템의 추론 결과*

1. **물리 좌표 자동 발견**: 세 가지 향상된 시각적 프롬프트 도구(Spatial Measurement, Regional Amplifier, Plot Replayer)를 설계하여 MLLM의 공간 인식 능력 강화. 픽셀 좌표와 잠재 좌표 두 유형 모두에 대응 가능.

2. **방정식 추론 성능 향상**: 가설-평가-반복(hypothesis-assessment-iteration) 추론 체인을 통해 MLLM의 사전학습 지식을 방정식 탐색에 활용. 기존 symbolic regression 방법 대비 외삽 정확도 26.96% 향상 달성.

3. **실제 데이터 검증**: 시뮬레이션 데이터뿐만 아니라 Kármán vortex street 등 실험 데이터에서도 효과성 입증.

## How

- **물리 좌표 발견 (픽셀 좌표계)**:
  - **Spatial Measurement**: 원본 이미지에 격자선과 눈금이 있는 좌표계 오버레이. MLLM이 예측이 아닌 눈금 읽기로 좌표 결정 가능하게 함.
  - **Regional Amplifier**: MLLM이 먼저 사분면(quadrant)을 탐지한 후 해당 영역을 확대. 목표 객체와 좌표계의 공간 관계를 세밀하게 관찰. 이차 검증으로 오식별 방지.
  - **Plot Replayer**: MLLM의 초기 위치 탐지 결과를 표식(red dots)으로 표시하고 목표 객체와의 시각적 차이 비교. 오류 교정 및 피드백 반복.
  - **필터링**: Savitzky-Golay 필터를 바탕으로 한 피드백 교정 모듈. MLLM이 궤적의 진화 추세와 주기성을 고려하여 윈도우 길이 h와 다항식 차수 p 결정.

- **물리 좌표 발견 (잠재 좌표계)**:
  - 다양한 저차원 표현 학습 기법(manifold learning, Koopman operator, delayed embedding 등) 통합
  - 고차원 데이터의 복잡한 시공간 진화 패턴을 포착하는 내재 변수(intrinsic variables) 인코딩

- **방정식 추론**:
  - 후보 기호 표현식 라이브러리 구축 (다항식, 삼각함수, 지수함수, 로그함수 등)
  - MLLM의 사전학습 과학 지식으로 유망한 방정식 후보 생성 및 평가
  - 계수 최적화 및 NMSE(Normalized Mean Squared Error) 기반 성능 평가
  - 추론 체인을 통한 반복적 개선

## Originality

- **MLLM을 고차원 물리 발견에 처음 적용**: 종래의 신경망 기반 접근이나 유전 프로그래밍 기반 symbolic regression이 아닌, MLLM의 시각-언어 통합 능력을 직접 활용한 혁신적 접근.

- **향상된 시각적 프롬프트 설계**: 단순한 텍스트 프롬프트를 넘어, 시각적 위치 지정 도구(Spatial Measurement, Regional Amplifier, Plot Replayer)라는 구체적이고 실용적인 기법 제안. 기존 MLLM의 공간 인식 한계를 체계적으로 극복.

- **좌표 발견과 방정식 추론의 통합**: 두 개의 결합된 부분문제(coupled subproblems)를 하나의 통합 프레임워크로 해결. 종래 방법처럼 순차적 또는 분리된 처리가 아닌 상호작용적 개선.

- **Zero-shot 방식**: 사전 학습된 MLLM을 특정 작업에 미세조정하지 않고 프롬프트 엔지니어링만으로 달성. 새로운 시스템에 대한 일반화 능력 향상.

## Limitation & Further Study

- **계산 비용 미분석**: MLLM의 반복적 호출로 인한 계산량과 실행 시간에 대한 구체적 분석 부재. API 기반 MLLM 사용 시 실제 적용의 경제성 검토 필요.

- **시스템 유형 제한**: 현재는 rigid body motion(픽셀 좌표)과 oscillatory dynamics(잠재 좌표) 두 유형에만 적용. 더 복잡한 비선형 동역학(chaos, bifurcation 등)에 대한 확장 필요.

- **MLLM 모델 의존성**: 특정 MLLM(논문에서 명시되지 않음)의 성능에 크게 의존. 다양한 MLLM 모델 간 성능 비교 분석 미흡.

- **장기 외삽 성능**: 26.96% 향상은 의미 있지만, 절대 외삽 정확도 수치가 논문의 발췌 부분에 명시되지 않음. 매우 장기 예측(long-term extrapolation)에 대한 한계 가능성.

- **후속 연구 방향**:
  - 더 일반적인 동역학 시스템(stochastic systems, coupled systems, high-order equations)으로의 확장
  - 노이즈가 많은 실제 데이터에 대한 강건성(robustness) 강화
  - 여러 MLLM 모델의 앙상블 활용
  - 물리적으로 일관성 있는 제약조건(physics-informed constraints) 통합

## Evaluation

- **Novelty**: 4.5/5
  - MLLM을 symbolic regression에 직접 적용한 참신한 접근. 시각적 프롬프트 도구의 구체성 우수. 다만 개별 구성 요소(manifold learning, coefficient optimization)는 기존 기법의 조합.

- **Technical Soundness**: 4/5
  - 방법론의 논리적 흐름과 알고리즘 설계가 합리적. 그러나 발췌 부분에서 latent coordinate 검출 알고리즘이 완전히 설명되지 않음. MLLM의 오류 전파 가능성에 대한 이론적 분석 부족.

- **Significance**: 4.5/5
  - 고차원 과학 데이터로부터 자동으로 물리 법칙 발견은 과학 및 공학 전반에 중대한 영향. 26.96% 성능 향상은 실질적 가치. 다만 두 가지 시스템 유형만 검증하여 일반성에 제한.

- **Clarity**: 3.5/5
  - 전체 파이프라인의 개요는 명확하나, 발췌된 텍스트에서 latent coordinate detection 방식이 충분히 설명되지 않음. 수식 표기(φ, ψ, g)는 명확하지만, 실제 구현 디테일 부족. 그림과 알고리즘이 부록에 집중되어 본문 가독성 저하.

- **Overall**: 4/5

## 총평

본 논문은 멀티모달 대규모 언어 모델의 시각 인식 능력과 사전학습 지식을 물리 방정식 발견이라는 도전적인 문제에 창의적으로 적용한 우수한 연구이다. 향상된 시각적 프롬프트(특히 Spatial Measurement, Regional Amplifier)는 MLLM의 공간 인식 한계를 극복하는 실용적 해법을 제시한다. 다만 계산 비용 분석, 노이즈 강건성, 더 복잡한 동역학 시스템으로의 확장이 필요하며, 절대 성능 수치와 알고리즘 세부사항의 명확한 기술이 추가되면 더욱 강화될 수 있다.

## Related Papers

- 🔗 후속 연구: [[papers/627_Position_Multimodal_large_language_models_can_significantly/review]] — 멀티모달 과학적 추론의 일반적 가능성을 동영상 데이터에서 물리 법칙 발견이라는 구체적 문제에 적용한다.
- 🔄 다른 접근: [[papers/289_Drsr_Llm_based_scientific_equation_discovery_with_dual_reaso/review]] — 과학 방정식 발견이라는 공통 목표를 가지지만 멀티모달 접근법과 데이터-경험 이중 추론이라는 다른 방법을 사용한다.
- 🏛 기반 연구: [[papers/503_LLM-ODE_Data-driven_Discovery_of_Dynamical_Systems_with_Larg/review]] — 동적 시스템 발견을 위한 LLM 활용 방법론이 동영상에서 지배 방정식 발견의 이론적 기반을 제공한다.
- 🔗 후속 연구: [[papers/241_Criteria-first_semantics-later_reproducible_structure_discov/review]] — 기준 우선 구조 발견을 멀티모달 LLM 기반 내재 좌표 발견으로 확장한다.
- 🏛 기반 연구: [[papers/627_Position_Multimodal_large_language_models_can_significantly/review]] — 멀티모달 대형 언어 모델의 과학적 추론 향상 가능성을 동영상에서 물리 법칙 발견이라는 구체적 사례로 입증한다.
