---
title: "289_Drsr_Llm_based_scientific_equation_discovery_with_dual_reaso"
authors:
  - "R. Wang"
  - "Boxiao Wang"
  - "Kai Li"
  - "Yifan Zhang"
  - "Jian Cheng"
date: "2025"
doi: "arXiv:2506.04282"
arxiv: ""
score: 4.3
essence: "본 논문은 대규모 언어모델(LLM)을 활용한 기호 회귀(Symbolic Regression)에서 **데이터 구조 분석**과 **생성 이력 반영**의 이중 추론을 통해 과학 방정식 발견의 정확성과 효율성을 획기적으로 향상시킨다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/AI_in_Scientific_Research"
  - "topic/ai4s"
---

# DrSR: LLM 기반 과학 방정식 발견 (데이터와 경험의 이중 추론)

> **저자**: R. Wang, Boxiao Wang, Kai Li, Yifan Zhang, Jian Cheng | **날짜**: 2025 | **DOI**: [arXiv:2506.04282](https://arxiv.org/abs/2506.04282)

---

## Essence

![Figure 1](figures/fig1.webp) *DrSR 프레임워크 개요: (a) 데이터 인식 통찰 (b) 귀납적 아이디어 추출 (c) 방정식 생성 및 선택*

본 논문은 대규모 언어모델(LLM)을 활용한 기호 회귀(Symbolic Regression)에서 **데이터 구조 분석**과 **생성 이력 반영**의 이중 추론을 통해 과학 방정식 발견의 정확성과 효율성을 획기적으로 향상시킨다.

## Motivation

- **Known**: 최근 LLM-SR이 LLM 내재 과학 선행지식(prior)을 활용하여 기호 회귀에서 전통 방법을 능가하는 성능을 보임

- **Gap**: 
  - 기존 LLM-SR은 LLM 내재 선행지식에 과도히 의존하면서 **실제 데이터의 구조적 특성을 직접 분석하지 않음** (변수 간 관계, 단조성, 비선형성 등 무시)
  - **생성 이력에 대한 체계적 반영 메커니즘 부재**: 문법 오류, 수치 불안정성 등 무효 표현식 반복 생성으로 효율성 저하

- **Why**: 과학자의 인지 과정은 관찰로부터 패턴 유도 → 시행착오를 통한 반영 → 효율적 가설 탐색으로 이루어지는데, 기존 방법들이 이를 반영하지 못함

- **Approach**: 
  - **데이터 인식 통찰(Data-aware Insight)**: LLM이 샘플 데이터와 잔차(residual)를 분석하여 구조화된 변수 관계 도출
  - **귀납적 아이디어 추출(Inductive Idea Extraction)**: 방정식 평가 결과(성공/실패)로부터 재사용 가능한 전략을 동적 아이디어 라이브러리로 축적

## Achievement

![Figure 2](figures/fig2.webp) *다양한 과학 분야에서의 일반화 성능 (ID/OOD 설정)*

![Figure 4](figures/fig4.webp) *문법적으로 유효한 해 비율 비교 - DrSR의 우월한 안정성*

1. **높은 발견 정확성**: 물리학, 화학, 생물학, 재료과학 6개 벤치마크에서 **유효 방정식 생성률 및 정확도 면에서 SOTA 달성**
   - 전통 유전 프로그래밍(GP) 및 강화학습(RL) 기반 방법 대비 우월
   - LLM-SR 기준선 대비 일관된 개선

2. **강화된 안정성과 효율성**:
   - 무효 표현식 생성 빈도 대폭 감소 (문법 오류, 수치 오버플로우 방지)
   - **수렴 속도 향상**: 더 적은 반복으로 고성능 방정식 발견
   - 도메인 내(ID) 및 도메인 외(OOD) 모두에서 일반화 성능 우수

3. **강건한 일반화**: 학습 데이터와 다른 분포를 가진 테스트 데이터에서도 일관된 성능 유지

## How

![Figure 1](figures/fig1.webp)

### 3.1 데이터 인식 통찰 (Data-aware Insight)

- **초기 통찰 생성**: 원본 데이터 D에서 균등 샘플링으로 100개 샘플 추출 → πdata LLM이 변수 관계 분석하여 초기 통찰 D₀ 도출
  - 단조성(monotonicity), 비선형성(nonlinearity), 변수 상관관계 등 포착

- **잔차 기반 반복 개선**: 
  1. 현재 최적 방정식 f*가 이전 최고 성능 개선 시 → 잔차 reₜ,ᵢ = yᵢ - f*(xᵢ) 계산
  2. 잔차를 포함한 증강 데이터셋 Dₜ = {(xᵢ, yᵢ, resₜ,ᵢ)} 구성 → 다시 100개 샘플 추출
  3. πdata가 개선된 통찰 D_new 생성: 국소 단조성 변화, 비선형 상호작용(곱, 나눗셈), 구체적 변수 상관관계 포착
  
- **효과**: 반복할수록 거시 패턴 → 미시·고차 구조로 통찰 진화 → πmain의 방정식 생성을 점진적으로 정제

### 3.2 귀납적 아이디어 추출 (Inductive Idea Extraction)

- **평가 기반 분류**: 생성된 각 방정식 f를 평가 결과에 따라 3가지로 분류
  1. **Positive**: 현재 최고 점수 s*를 초과 → 성공적 모델링 패턴 추출
  2. **Negative**: s* 이하 → 성능 부족의 원인 분석
  3. **Invalid**: 문법/수치 오류, 변수 불일치 → 오류 회피 기법 도출

- **아이디어 라이브러리 관리** (L):
  - **Positive Ideas**: 성공한 방정식의 구조적 특징, 효과적 변수 조합, 함수 형태 저장
  - **Negative Ideas**: 성능 부진의 원인, 피해야 할 패턴 기록
  - **Invalid Ideas**: 흔한 오류 유형 및 대응 방안 축적
  
- **동적 업데이트**: 각 반복마다 새로운 아이디어로 라이브러리 확장 → 프롬프트 구성 시 최근 아이디어의 λ 비율 샘플링하여 주입

### 3.3 방정식 생성 및 선택 (Equation Generation & Selection)

- **통합 프롬프트 구성**: 문제 설명 + 데이터 통찰 D + 선택된 아이디어 집합 → πmain에 입력
- **다중 샘플링**: 각 반복마다 b개의 방정식 스켈레톤 생성
- **파라미터 최적화**: BFGS 알고리즘으로 각 스켈레톤의 가중치 최적화
- **성능 평가 및 캐싱**: 음수 MSE 기반 점수 계산 → 최고 성능 결과 유지

## Originality

- **이중 추론 메커니즘의 통합**: 기존 LLM-SR의 일방향 생성-평가 루프에 **데이터 구조 분석**과 **행동 수준 반영**의 폐루프 추가
  - 데이터 기반(data-driven)과 경험 기반(experience-driven) 추론을 동시에 수행하는 설계는 기존 문헌에서 찾기 어려움

- **잔차 기반 진화적 통찰**: 단순 초기 데이터 분석을 넘어 **오류 신호(잔차)를 활용한 반복적 정제** → 미발견 변수 상호작용 포착에 새로운 접근

- **다중 역할 LLM 앙상블**: 같은 LLM 백본으로 πdata(분석), πidea(반영), πmain(생성) 3가지 특화 역할 수행 → 계산 효율성과 일관성 동시 달성

- **구조화된 아이디어 라이브러리**: 프롬프트 엔지니어링 수준에서 벗어나 **범주화된 휴리스틱 체계** 구축 → 검색 안정성과 전이성 향상

## Limitation & Further Study

- **계산 비용**: 반복마다 3개 LLM 호출(데이터 분석, 아이디어 추출, 방정식 생성) → 추론 지연 증가 (LLM-SR 대비 구체적 오버헤드 미기재)

- **샘플 크기 제약**: 데이터 분석 및 잔차 계산 시 고정 100개 샘플 사용 → 대규모 데이터셋에서의 대표성 문제 및 최적 크기 미결정

- **LLM 백본 의존성**: Mixtral-8x7B와 LLaMA3.1-8B에서만 평가 → 더 작은 모델, 최신 대형 모델(GPT-4 등)에서의 성능 미검증

- **아이디어 라이브러리 포화**: 반복 누적에 따른 라이브러리 규모 증가 → 관련성 낮은 오래된 아이디어 필터링 메커니즘 부재

- **후속 연구 방향**:
  - 계산 비용-성능 트레이드오프 최적화 (배치 처리, 캐싱 기법)
  - 적응적 샘플 크기 및 아이디어 라이브러리 프루닝 전략
  - 여러 과학 도메인 간 아이디어 전이학습 연구
  - 방정식 복잡도-정확도 파레토 최적화 추가


## Evaluation

- Novelty: 4.2/5
- Technical Soundness: 4.5/5
- Significance: 4.3/5
- Clarity: 4.4/5
- Overall: 4.3/5

**총평**: DrSR은 LLM 기반 기호 회귀의 두 가지 핵심 약점(데이터 무시, 경험 부재)을 동시에 해결하는 실용적이고 우아한 솔루션으로, 다중 과학 도메인에서 입증된 성과를 보인다. 다만 계산 비용-성능 트레이드오프 정량화와 이론적 수렴성 분석이 추가되면 학술적 영향력이 더욱 증대될 것으로 예상된다.

## Related Papers

- 🔗 후속 연구: [[papers/504_Llm-srbench_A_new_benchmark_for_scientific_equation_discover/review]] — 과학 방정식 발견을 위한 LLM 기반 기호 회귀에서 더 포괄적인 과학 방정식 발견 벤치마크로 확장한 평가 프레임워크입니다.
- 🔄 다른 접근: [[papers/503_LLM-ODE_Data-driven_Discovery_of_Dynamical_Systems_with_Larg/review]] — 데이터와 경험의 이중 추론 접근법과 대규모 언어모델을 활용한 동역학 시스템 발견이라는 서로 다른 방정식 발견 방법론입니다.
- 🏛 기반 연구: [[papers/426_Improving_Scientific_Hypothesis_Generation_with_Knowledge_Gr/review]] — 지식 그래프를 활용한 과학 가설 생성 연구가 방정식 발견에서 경험적 지식을 활용하는 접근법의 이론적 기반을 제공합니다.
- 🔄 다른 접근: [[papers/504_Llm-srbench_A_new_benchmark_for_scientific_equation_discover/review]] — 동일한 과학 방정식 발견 문제를 데이터와 경험 기반 이중 추론으로 접근
- 🔗 후속 연구: [[papers/275_Discovering_symbolic_differential_equations_with_symmetry_in/review]] — 데이터와 경험의 이중 추론을 통한 방정식 발견은 대칭 불변량 제약을 더욱 발전시킨 방법론입니다
- 🔗 후속 연구: [[papers/1083_A_framework_for_discovering_scientific_equations_with_large/review]] — 과학 방정식 발견에서 데이터와 경험의 이중 추론으로 확장된 프레임워크
- 🔄 다른 접근: [[papers/547_Mllm-based_discovery_of_intrinsic_coordinates_and_governing/review]] — 과학 방정식 발견이라는 공통 목표를 가지지만 멀티모달 접근법과 데이터-경험 이중 추론이라는 다른 방법을 사용한다.
- 🔄 다른 접근: [[papers/502_Llm-feynman_Leveraging_large_language_models_for_universal_s/review]] — 둘 다 과학 공식 발견을 목표로 하지만 하나는 LLM 기반이고 다른 하나는 데이터와 경험의 이중 추론을 사용한다.
