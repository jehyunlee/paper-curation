---
title: "275_Discovering_symbolic_differential_equations_with_symmetry_in"
authors:
  - "Jianke Yang"
  - "M. A. Bhat"
  - "B. L. Hu"
  - "Yadi Cao"
  - "Nima Dehmamy"
date: "2025"
doi: "10.48550/arXiv.2505.12083"
arxiv: ""
score: 4.2
essence: "데이터로부터 미분방정식을 발견할 때 물리법칙을 위반하는 복잡한 해를 얻는 문제를 해결하기 위해, 대칭 불변량(differential invariants)을 기본 단위로 사용하여 방정식 발견 알고리즘을 제약하는 일반적 프레임워크를 제안한다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/Evolutionary_Chemistry_Models"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Yang et al._2025_Discovering symbolic differential equations with symmetry invariants.pdf"
---

# Discovering symbolic differential equations with symmetry invariants

> **저자**: Jianke Yang, M. A. Bhat, B. L. Hu, Yadi Cao, Nima Dehmamy, Robin Walters, Rose Yu | **날짜**: 2025 | **DOI**: [10.48550/arXiv.2505.12083](https://doi.org/10.48550/arXiv.2505.12083)

---

## Essence

![Figure 1](figures/fig1.webp) *프레임워크는 대칭 불변량(symmetry invariants)을 사용하여 방정식 발견에서 대칭성을 강제한다. 원형 영역에서의 예측 함수는 불변량 사용 시 대칭 출력을 보장함을 시각화한다.*

데이터로부터 미분방정식을 발견할 때 물리법칙을 위반하는 복잡한 해를 얻는 문제를 해결하기 위해, 대칭 불변량(differential invariants)을 기본 단위로 사용하여 방정식 발견 알고리즘을 제약하는 일반적 프레임워크를 제안한다.

## Motivation

- **Known**: 기존 기호 회귀(symbolic regression, SR) 방법들은 광대한 탐색 공간으로 인해 실패하거나 과적합된 복잡한 방정식을 생성할 수 있으며, 일부 물리 제약을 도입하려는 시도들이 있어왔다(Udrescu & Tegmark 2020, Otto et al. 2023, Yang et al. 2024).

- **Gap**: 기존 대칭성 기반 방법들은 처리 가능한 방정식의 유형, 호환되는 기본 알고리즘, 적용 범위가 제한적이다. 예를 들어 Yang et al. (2024)는 희소 회귀(sparse regression)에만 적용 가능하고 유전 프로그래밍(genetic programming)에는 미적용.

- **Why**: 대칭성은 회전, 평행이동, 스케일링 등 변환 하에서 물리계의 불변성을 지배하는 근본적 원리로, 발견 알고리즘에 통합될 경우 탐색 공간 축소 및 해석 가능성 향상을 가져온다.

- **Approach**: 대칭 변환의 미분 불변량(differential invariants) 이론을 활용하여 원래 변수 대신 불변량을 기본 단위로 사용함으로써, 모든 기호 회귀 방법에 일반적으로 적용 가능한 대칭성 강제 메커니즘을 구축.

## Achievement

![Figure 3](figures/fig3.webp) *유전 프로그래밍 기반 방법들의 성공 확률: 제안 방법(대칭성 포함)이 다양한 물리계에서 기본 방법들을 현저히 능가한다.*

1. **일반적 프레임워크**: Lie 점 대칭(Lie point symmetry) 이론의 미분 불변량에 기반한 범용 프레임워크 개발. 방정식의 유형, 대칭 그룹, 기본 SR 알고리즘에 제약이 적음.

2. **기존 방법과의 통합**: 희소 회귀와 유전 프로그래밍 등 기존 SR 방법들과 원활하게 통합되며, 정확도와 효율성을 개선. 발견된 방정식은 지정된 대칭성을 자동으로 만족함을 보장.

3. **강건성 검증**: Darcy 유동, 반응-확산(reaction-diffusion) 시스템 등 다양한 물리계에서 검증. 노이즈가 있는 데이터와 불완전한 대칭성 조건에서도 견고한 성능 유지.

## How

![Figure 5](figures/fig5.webp) *Lie 점 변환과 그 연장(prolongation)의 군 작용 시각화: 대칭 변환 하에서 미분량들의 변환 관계를 보여준다.*

- **대칭 불변량 계산**: 주어진 대칭 그룹 G에 대해 Lie 점 대칭 이론을 활용하여 미분 불변량 I₁, I₂, ... 체계적으로 도출
  
- **탐색 공간 재정의**: 기존 기본 단위(변수, 미분항)를 미분 불변량으로 대체하여 후보 함수 라이브러리 구성

- **알고리즘 통합**: 
  - **희소 회귀**: 불변량으로 구성된 후보 함수 행렬 Θ(I)을 사용하여 선형 조합 계수 추정
  - **유전 프로그래밍**: 불변량을 기본 터미널 노드로 사용하여 진화 연산 수행

- **발견 보장**: 불변량으로만 구성된 방정식은 수학적으로 지정된 대칭성을 자동 만족

- **노이즈 대응**: 근사적 불변량(approximate invariants) 개념도입으로 불완전 대칭성 처리 가능

## Originality

- **차별성 1**: Lie 군 이론의 미분 불변량을 기호 회귀에 직접 적용하는 최초의 시도. 이전 연구(Yang et al. 2024)는 선형 결합 형태로 제한됨.

- **차별성 2**: 희소 회귀, 유전 프로그래밍, 신경망 기반 방법 등 **다양한 기본 SR 알고리즘**과 호환 가능한 일반적 프레임워크 제시.

- **차별성 3**: 불완전 대칭성과 노이즈가 있는 실제 데이터에 대한 견고성 이론 및 실증적 분석 제공.

- **차별성 4**: LLM 기반 방법과 달리 **해석 가능하고 투명한 물리 제약** 조건을 명시적으로 주입하여 신뢰성 향상.

## Limitation & Further Study

- **한계 1**: 미분 불변량 계산이 모든 대칭 그룹에 대해 자동화되어 있지 않은 경우 수동 개입 필요. Lie 군 이론 지식을 요구함.

- **한계 2**: 여러 대칭 그룹이 동시에 작용하는 경우(예: 회전 + 평행이동) 불변량 구성의 복잡도 증가.

- **한계 3**: 측정된 데이터가 실제 대칭성과 완전히 일치하지 않을 때 발견 성능 저하 가능. 근사 불변량 개념으로 완화되나 수량적 한계치 미정.

- **한계 4**: 고차(high-order) 미분을 포함하는 PDE의 경우 불변량 개수가 급증하여 계산 복잡도 증가.

- **후속 연구**: 
  - 대칭 그룹 자동 발견(symmetry group discovery) 알고리즘 개발
  - 다중 종속 변수 시스템으로의 확장
  - 보존량(conserved quantities)과 같은 추가 물리 제약 통합

## Evaluation

- **Novelty**: 4.5/5
  - Lie 이론의 미분 불변량을 일반적 SR 프레임워크에 적용한 점에서 창의적
  - 기존 대칭성 기반 방법들보다 범용성 높음
  - 다만 Lie 군 이론 자체는 고전적 수학 분야

- **Technical Soundness**: 4/5
  - 미분 불변량 이론의 수학적 기초 견고함
  - 실험 검증이 충분하고 노이즈 강건성도 입증
  - 다만 근사 불변량 오류 분석이 다소 부족

- **Significance**: 4.5/5
  - 물리 기반 머신러닝에서 실질적 영향력 높음
  - 해석 가능성과 물리 정확성 동시 달성
  - 실용적 응용 범위 넓음(유체역학, 반응확산, 파동 방정식 등)

- **Clarity**: 3.5/5
  - 핵심 아이디어는 명확하나 Lie 군 및 미분 불변량 배경 필요
  - 수학 표기법이 다소 복잡
  - 알고리즘 의사코드(pseudocode) 추가 필요

- **Overall**: 4.2/5

**총평**: 본 논문은 대칭 불변량이라는 우아한 수학적 개념을 기호 회귀에 적용하여 물리적으로 타당한 방정식 발견을 효율적으로 달성하는 창의적인 방법을 제시하며, 다양한 기본 알고리즘과의 호환성과 실제 노이즈 조건에서의 강건성이 돋보인다. 다만 Lie 군 이론의 사전 지식 요구와 고차 미분 시스템에서의 확장성이 향후 개선 과제이다.

## Related Papers

- 🏛 기반 연구: [[papers/276_Discovery_of_Unstable_Singularities/review]] — 수학적 대칭성과 불안정 특이점 발견은 물리 불변량 보존 원리를 공유합니다
- 🔄 다른 접근: [[papers/503_LLM-ODE_Data-driven_Discovery_of_Dynamical_Systems_with_Larg/review]] — LLM 기반 동적 시스템 발견과 대칭 불변량 기반 방정식 발견은 서로 다른 접근법으로 같은 문제를 해결합니다
- 🔗 후속 연구: [[papers/289_Drsr_Llm_based_scientific_equation_discovery_with_dual_reaso/review]] — 데이터와 경험의 이중 추론을 통한 방정식 발견은 대칭 불변량 제약을 더욱 발전시킨 방법론입니다
- 🔗 후속 연구: [[papers/503_LLM-ODE_Data-driven_Discovery_of_Dynamical_Systems_with_Larg/review]] — 대칭성을 가진 기호 미분방정식 발견이 LLM-ODE의 동역학 시스템 발견을 더 구체적으로 확장한 사례이다.
- 🏛 기반 연구: [[papers/1083_A_framework_for_discovering_scientific_equations_with_large/review]] — 대칭성을 가진 상미분방정식 발견의 수학적 기반을 제공
- 🏛 기반 연구: [[papers/085_Ai-newton_A_concept-driven_physical_law_discovery_system_wit/review]] — 기호적 미분방정식 발견의 기본적 접근법을 다중 실험 데이터에서 일반 물리 법칙을 발견하는 고도화된 시스템으로 발전시킨다.
- 🧪 응용 사례: [[papers/012_A_Multi-agent_Framework_for_Physical_Laws_Discovery/review]] — 다중 에이전트 물리 법칙 발견 프레임워크는 Discovering symbolic differential equations with symmetry 연구가 제시한 대칭성 기반 방정식 발견 기법을 실제 재료과학 문제에 적용합니다.
- 🔄 다른 접근: [[papers/502_Llm-feynman_Leveraging_large_language_models_for_universal_s/review]] — 둘 다 AI를 이용한 과학 공식 발견을 다루지만, 하나는 LLM 기반이고 다른 하나는 대칭성을 활용한 기호적 미분방정식 발견에 초점을 맞춘다.
- 🏛 기반 연구: [[papers/1104_A_Physics-Informed_Chemical_Rule_for_Topological_Materials_D/review]] — 대칭성을 활용한 미분방정식 발견이 위상 물질의 대칭성 기반 규칙 개발의 기초
