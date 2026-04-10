---
title: "788_Targeted_materials_discovery_using_Bayesian_algorithm_execut"
authors:
  - "S. Chitturi"
  - "Akash Ramdas"
  - "Yue Wu"
  - "Brian A. Rohr"
  - "Stefano Ermon"
date: "2023"
doi: "10.1038/s41524-024-01326-2"
arxiv: ""
score: 4.2
essence: "본 연구는 사용자가 정의한 필터링 알고리즘을 자동으로 데이터 수집 전략으로 변환하여, 복잡한 재료 설계 목표를 달성하기 위한 Bayesian Algorithm Execution (BAX) 기반 프레임워크를 제시한다. 이를 통해 최적화나 전체 함수 추정이 아닌 특정 설계 공간의 부분집합 탐색을 효율적으로 수행할 수 있다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/Retrosynthesis_Strategy_Planning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Chitturi et al._2023_Targeted materials discovery using Bayesian algorithm execution.pdf"
---

# Targeted materials discovery using Bayesian algorithm execution

> **저자**: S. Chitturi, Akash Ramdas, Yue Wu, Brian A. Rohr, Stefano Ermon | **날짜**: 2023 | **DOI**: [10.1038/s41524-024-01326-2](https://doi.org/10.1038/s41524-024-01326-2)

---

## Essence

본 연구는 사용자가 정의한 필터링 알고리즘을 자동으로 데이터 수집 전략으로 변환하여, 복잡한 재료 설계 목표를 달성하기 위한 Bayesian Algorithm Execution (BAX) 기반 프레임워크를 제시한다. 이를 통해 최적화나 전체 함수 추정이 아닌 특정 설계 공간의 부분집합 탐색을 효율적으로 수행할 수 있다.

## Motivation

- **Known**: 기존 Bayesian Optimization (BO)은 단일 목적 최적화와 다중 목적 최적화(Pareto 최적성)에 집중되어 있으며, 함수 전체 추정(mapping)을 위한 Uncertainty Sampling 등이 존재한다.

- **Gap**: 재료 발견에서는 종종 특정 범위의 물성을 만족하는 설계점들의 집합(target subset)을 찾아야 하는데, 기존 획득 함수(acquisition function)는 이러한 복합적인 실험 목표를 직접 반영하지 못한다. 새로운 획득 함수를 개발하려면 상당한 수학적 통찰과 시간이 필요하다.

- **Why**: TiO₂ 나노입자 합성의 특정 크기 범위 탐색, 고온 초전도체의 안정성 윈도우 매핑, 장기 신뢰성 실패 모드 회피를 위한 다양한 재료 후보 확보 등 많은 실제 재료 과학 문제가 부분집합 추정에 해당한다.

- **Approach**: 사용자가 정의한 알고리즘(정확한 함수를 알면 올바른 부분집합을 반환하는)을 자동으로 매개변수 없는 순차적 데이터 수집 전략(SwitchBAX, InfoBAX, MeanBAX)으로 변환하는 프레임워크를 개발한다.

## Achievement

1. **세 가지 BAX 기반 전략 개발**: 
   - **InfoBAX**: 정보이론 기반 접근으로 작은 데이터 체제에서 우수한 성능 제공
   - **MeanBAX**: 다중 물성에 대한 후진 평균(posterior mean)을 활용한 탐색 전략의 다중 물성 일반화
   - **SwitchBAX**: 데이터 크기에 따라 InfoBAX와 MeanBAX 간 동적 전환하는 매개변수 없는 하이브리드 전략

2. **실제 재료 데이터 검증**: 
   - TiO₂ 나노입자 합성 데이터셋에서 특정 크기 범위 탐색
   - 자기 재료 고정밀 특성화 데이터셋에서 다중 물성 조건 만족 영역 탐색
   - 기존 최첨단 방법 대비 현저히 높은 효율성 입증

3. **사용성 중심 설계**: 과학자가 복잡한 수학 없이 간단한 알고리즘 절차로 실험 목표를 표현할 수 있는 오픈소스 인터페이스 제공

## How

- **알고리즘 기반 목표 표현**: 사용자가 제공한 필터링 알고리즘 A가 정확한 함수 f*를 입력받으면 목표 부분집합 T*을 반환하도록 설계
  
- **Bayesian Algorithm Execution 적응**: 
  - 기존 InfoBAX와 Multipoint-BAX를 이산 설계 공간(discrete design space)과 다중 물성 측정에 맞게 수정
  - 각 순차 단계에서: (1) 현재까지 수집한 데이터로 확률 모델 훈련, (2) 사용자 알고리즘을 이 모델의 표본/평균 함수에 적용, (3) 획득 함수를 통해 다음 측정점 결정

- **적응형 전략 선택**: 
  - 작은 데이터 체제(초기 단계): 정보 이득이 큰 InfoBAX 사용
  - 중간~대규모 데이터: 후진 평균의 신뢰도가 증가한 MeanBAX 선호
  - SwitchBAX는 성능 메트릭에 기반해 자동으로 전환

- **이산 설계 공간 최적화**: 연속 공간이 아닌 구체적인 합성/측정 조건의 유한 집합에서 효율적으로 작동

## Originality

- **프레임워크 혁신성**: 사용자 정의 알고리즘을 자동으로 획득 함수로 변환하는 패러다임은 기존의 고정된 목표(최적화, Pareto 전면, 함수 추정)에 벗어난 혁신적 접근

- **다중 물성 일반화**: MeanBAX의 다중 물성 확장은 실제 재료 문제의 복잡성을 직접 반영하며, 기존 단일 물성 중심 최적화 방법의 한계 극복

- **매개변수 없는 설계**: SwitchBAX의 자동 전환 메커니즘은 사용자가 알고리즘 매개변수를 조정할 필요를 제거하여 접근성 극대화

- **재료과학 특화**: 이산 설계 공간과 다중 물성이라는 재료 발견의 현실적 특성을 처음으로 BAX 프레임워크에 명시적으로 통합

## Limitation & Further Study

- **계산 비용**: 각 순차 단계에서 사용자 알고리즘을 다수의 후진 표본(InfoBAX) 또는 평균 함수(MeanBAX)에 반복 적용해야 하므로, 알고리즘 복잡도가 높으면 계산 병목이 될 수 있음

- **데이터셋 규모 제한**: TiO₂와 자기 재료 데이터셋만으로 검증되었으며, 더 큰 설계 공간(d > 20)이나 더 많은 물성(m > 10)에서의 확장성 미실증

- **노이즈 모델 가정**: 측정 노이즈가 독립적 정규분포를 따른다고 가정하지만, 실제 재료 실험에서 체계적 오류(systematic error)나 상관된 노이즈가 존재할 경우 영향 미검토

- **확률 모델 의존성**: Gaussian Process 등의 확률 모델의 품질이 전략 성능에 직접적 영향을 미치는데, 높은 차원에서의 모델 오류에 대한 견고성 분석 부재

- **후속 연구 방향**:
  - 연속 설계 공간으로의 확장
  - 정보 수집과 측정 비용(실험 시간, 재료비)의 균형을 고려한 비용-효과 획득 함수 개발
  - 강화학습(reinforcement learning)과의 결합을 통한 더 복잡한 실험 목표 처리
  - 실시간 자동화 실험 시스템과의 통합 사례 연구

## Evaluation

- **Novelty**: 4.5/5
  - 사용자 알고리즘 자동 변환 개념은 신선하고 독창적이나, BAX 자체는 기존 연구이며 주로 재료과학 적응이 중심

- **Technical Soundness**: 4/5
  - 수학적 기초는 견고하고 이산 공간·다중 물성 확장이 적절하나, 고차원 또는 대규모 설계 공간에서의 확장성 증명 부족

- **Significance**: 4.5/5
  - 재료 과학 커뮤니티의 실제 문제(부분집합 추정)를 정면으로 해결하며, 접근성 높은 오픈소스 구현으로 산업 도입 가능성 높음

- **Clarity**: 4/5
  - 논문 구조와 동기는 명확하고 Figure 1의 설명이 직관적이나, 기술적 세부사항(InfoBAX와 MeanBAX의 수학적 차이)은 더 상세한 설명 필요

- **Overall**: 4.2/5

**총평**: 본 연구는 사용자 중심의 알고리즘 기반 목표 표현을 Bayesian sequential design과 결합한 창의적 프레임워크로, 재료 발견의 실제 수요(다중 물성, 복잡한 제약)에 직접 대응한다. 두 개의 실제 재료 데이터셋에서 우수한 성과를 입증했으나, 더 큰 규모의 설계 공간 검증과 실시간 자동화 실험 통합을 통한 추가 검증이 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/461_LARC_Towards_Human-level_Constrained_Retrosynthesis_Planning/review]] — 베이지안 알고리즘 실행과 LLM 기반 역합성 계획은 모두 복잡한 재료/화학 설계 목표 달성을 위한 서로 다른 AI 기반 접근법입니다
- 🏛 기반 연구: [[papers/418_Hypothesis_Generation_for_Materials_Discovery_and_Design_Usi/review]] — 대형 언어모델을 이용한 재료 발견 가설 생성은 베이지안 알고리즘 실행의 재료 설계 목표 설정에 이론적 기반을 제공합니다
- 🧪 응용 사례: [[papers/343_Foundation_models_for_materials_discovery__current_state_and/review]] — 재료 발견을 위한 파운데이션 모델은 베이지안 알고리즘 실행이 타겟으로 하는 재료 설계 분야의 실제 응용 사례입니다
- 🔄 다른 접근: [[papers/461_LARC_Towards_Human-level_Constrained_Retrosynthesis_Planning/review]] — 베이지안 알고리즘 실행을 통한 재료 발견과 LLM 기반 역합성 계획은 서로 다른 AI 접근법으로 화학 문제를 해결합니다
- 🏛 기반 연구: [[papers/258_Deep_active_learning_based_experimental_design_to_uncover_sy/review]] — 베이지안 알고리즘 실행을 통한 타겟 재료 발견이 생물학적 상호작용 탐색의 방법론적 기반을 제공합니다.
- 🧪 응용 사례: [[papers/799_The_frontier_of_simulation-based_inference/review]] — 베이지안 추론을 재료 발견의 타겟 최적화에 적용한다.
- 🔗 후속 연구: [[papers/867_Verifier-Constrained_Flow_Expansion_for_Discovery_Beyond_the/review]] — 베이지안 알고리즘 실행을 통한 표적 소재 발견이 Flow 확장의 검증기 제약 최적화 프레임워크에 직접 적용됨
- 🔗 후속 연구: [[papers/024_A_sober_look_at_llms_for_material_discovery_Are_they_actuall/review]] — 베이지안 알고리즘을 통한 표적 소재 발견이 LLM의 분자 공간 베이지안 최적화 유용성을 실제로 검증함
- 🏛 기반 연구: [[papers/1100_Representative_Informative_and_De-Amplifying_Requirements_fo/review]] — 베이지안 실험설계 방법론을 모델 신뢰성 향상에 적용한 이론적 기반
- 🔄 다른 접근: [[papers/1104_A_Physics-Informed_Chemical_Rule_for_Topological_Materials_D/review]] — 베이지안 알고리즘 vs 물리 기반 화학 규칙으로 재료 발견의 서로 다른 접근법
- 🔗 후속 연구: [[papers/1125_Accelerating_cell_culture_media_development_using_Bayesian_o/review]] — 베이지안 알고리즘 실행을 통한 표적 재료 발견은 세포 배양 배지 개발의 베이지안 최적화 프레임워크를 재료 발견으로 확장한다.
