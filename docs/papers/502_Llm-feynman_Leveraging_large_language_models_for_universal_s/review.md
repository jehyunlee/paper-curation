---
title: "502_Llm-feynman_Leveraging_large_language_models_for_universal_s"
authors:
  - "Zhilong Song"
  - "Qionghua Zhou"
  - "Chunjin Ren"
  - "Chongyi Ling"
  - "Minggang Ju"
date: "2025"
doi: "N/A"
arxiv: ""
score: 4.0
essence: "대규모 언어 모델(LLM)과 체계적 최적화를 결합하여 데이터와 도메인 지식으로부터 간결하고 해석 가능한 과학 공식을 자동으로 발견하는 통합 프레임워크를 제시한다. Feynman 강의의 90% 이상 물리 공식 재발견 및 재료과학 응용 분야에서 뛰어난 성능을 입증한다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Scientific_Language_Models"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Liu et al._2025_Llm-feynman Leveraging large language models for universal scientific formula and theory discovery.pdf"
---

# LLM-Feynman: Leveraging Large Language Models for Universal Scientific Formula and Theory Discovery

> **저자**: Zhilong Song, Qionghua Zhou, Chunjin Ren, Chongyi Ling, Minggang Ju, Jinlan Wang | **날짜**: 2025 | **DOI**: N/A

---

## Essence

대규모 언어 모델(LLM)과 체계적 최적화를 결합하여 데이터와 도메인 지식으로부터 간결하고 해석 가능한 과학 공식을 자동으로 발견하는 통합 프레임워크를 제시한다. Feynman 강의의 90% 이상 물리 공식 재발견 및 재료과학 응용 분야에서 뛰어난 성능을 입증한다.

## Motivation

- **Known**: 종래의 기계학습(ML) 기반 데이터 분석은 예측 정확도에는 우수하나 모델의 해석 가능성(interpretability)과 일반화(generalization) 측면에서 제한적. 기호 회귀(symbolic regression, SR) 등 해석 가능한 ML 방법도 과도하게 복잡한 공식을 생성하는 경향.

- **Gap**: LLM은 광범위한 과학 문헌 기반 도메인 지식을 보유하고 있으나, 자기회귀(autoregressive) 특성으로 인해 물리적으로 일관성 없는 공식을 생성할 수 있음. 기존 LLM 기반 공식 발견 방법은 도메인 지식 통합 및 다목적 최적화 부족.

- **Why**: 과학적 발견은 단순 데이터 피팅을 넘어 도메인 지식과 데이터를 통합하여 해석 가능하고 일반화 가능한 공식과 이론을 도출해야 함.

- **Approach**: LLM의 과학적 추론 능력과 체계적 최적화 기법을 결합한 3단계 통합 프레임워크 구축: (I) 자동 데이터 전처리 및 특징 공학, (II) 자가 평가 및 다목적 최적화를 통한 기호 회귀, (III) MCTS 기반 공식 해석.

## Achievement

1. **기초 물리 공식 재발견**: Feynman 강의에서 추출한 기본 물리 공식의 90% 이상 자동 재발견 달성, LLM 기반 방법의 과학 공식 발견 능력 입증.

2. **재료과학 응용 성공**: 
   - 2D 재료 및 페로브스카이트 합성 가능성 분류 태스크
   - 2D 재료 GW 밴드갭 및 리튬 고체 전해질 이온 전도도 회귀 예측
   - 기존 SR 방법(SISSO, PySR)과 비교하여 정확도 우월성 유지하면서 해석 가능성 향상.

3. **자가 평가 및 도메인 지식의 효과 검증**: 삭제 연구(ablation study)를 통해 도메인 지식(특징 의미, 차원) 통합과 자가 평가 점수(S) 도입이 모델 성능 향상에 핵심 기여함을 입증.

## How

- **모듈 I 데이터 전처리 및 특징 공학**:
  - 상호정보(mutual information) 기반 특징 선택으로 중복 제거
  - LLM 가이드 특징 매칭: Matminer 라이브러리에서 물리적 의미를 가진 기술자(descriptor) 자동 제안
  - 반복적 특징 정제: 공식 생성 정체 시 특징 집합 확장
  - LLM을 통한 자동 물리 의미 및 차원 정의

- **모듈 II 자기 평가 기반 기호 회귀**:
  - 구조화된 프롬프트를 통해 도메인 지식(물리 의미, 차원) 통합
  - LLM이 N개 초기 공식을 Python 함수 형태로 생성
  - 다목적 손실함수: $L = \alpha N(E) + \beta N(C) + \gamma S$
    - E: 예측 오차(MAE, R², 정확도 등)
    - C: 공식 복잡도
    - S: LLM 기반 자가 평가 해석 점수(0~1)
  - 반복 최적화(기본값 500회): 상위 30개 공식 선택 → 각 반복마다 10개 신규 공식 생성 → 재평가
  - Pareto 경계(frontier) 분석으로 정확도와 단순성 간 최적 균형점 도출

- **모듈 III MCTS 기반 공식 해석**:
  - Monte Carlo Tree Search와 LLM 결합
  - 각 트리 노드는 LLM 생성 해석 가설, UCB(Upper Confidence Bound)로 점수 부여
  - LLM이 명확성, 과학적 관련성, 일관성 평가 후 노드 점수 갱신
  - 새로운 아이디어 탐색과 고품질 해석 우선화의 균형 조절
  - 예시: 페로브스카이트 OER 활성도 공식 μ/t의 설명 개선 (자가평가 -72 → 65)

## Originality

- **다층 통합 접근**: LLM의 도메인 지식, 자가 평가 점수, 다목적 최적화, MCTS를 통합하여 종래 SR 방법의 한계(과도한 복잡도, 낮은 해석성) 극복.

- **자가 평가 메커니즘 혁신**: 정량화 어려운 "해석 가능성"을 LLM의 과학적 추론으로 0~1 점수화하여 최적화에 직접 반영 - 기존 SR에서는 불가능한 접근.

- **과학 공식 발견의 이중 검증**: 데이터 정확도(E)와 LLM 기반 물리적 일관성(S) 동시 최적화로 단순 수치 맞춤을 넘어 이론적 타당성 확보.

- **재료과학 특화 자동화 파이프라인**: Matminer 기반 재료 특성 특징 공학, 자동 물리 차원 정의 등 도메인별 맞춤 자동화.

## Limitation & Further Study

- **LLM 의존성**: 모델 성능이 선택된 LLM(Falcon-Mamba, ChemLLM, LLaMA3 등)에 따라 변동 가능. 부정확한 LLM 자가 평가가 공식 선택에 편향 초래 위험.

- **복잡도 정의의 모호성**: 수식 복잡도 정의 및 정규화 방식에 대한 상세 설명 부족. 다양한 도메인에서 최적 α, β, γ 가중치 결정 방법 미상.

- **제한된 검증 범위**: 주로 재료과학, 촉매, 물리 분야 검증. 생물학, 화학, 생명과학 등 다른 과학 분야 적용 가능성 미시험.

- **계산 비용**: 500회 반복 + MCTS 기반 해석으로 인한 총 계산 시간, 자원 소비 정량화 부재. 대규모 데이터셋에서의 확장성 미검토.

- **후속 연구 방향**:
  - 다양한 LLM 모델 간 성능 비교 및 앙상블 기법 도입
  - 다학제 적용 확대 (생물학, 약물 발견, 기후 과학 등)
  - 자가 평가 점수의 신뢰도 검증 방법론 개발
  - 계산 효율성 개선 (병렬화, 조기 종료 기준 등)

## Evaluation

- **Novelty**: 4.5/5
  - LLM 기반 자가 평가 해석성 점수화와 다목적 최적화는 독창적
  - MCTS 기반 공식 해석 또한 새로운 시도
  - 다만 개별 기법(LLM 사용, SR, MCTS)은 기존 기술의 조합

- **Technical Soundness**: 4/5
  - 3단계 모듈 설계 및 수학적 프레임워크는 논리적
  - 자가 평가 기반 최적화가 직관적이나, LLM 평가의 객관성 검증 부족
  - 복잡도 정규화 및 하이퍼파라미터 선정 근거 미흡

- **Significance**: 4.5/5
  - 과학 공식 자동 발견이라는 중요 문제 해결 시도
  - 90% 이상 Feynman 공식 재발견은 매우 인상적
  - 재료과학 응용 4개 분야 성공은 실용성 입증
  - 다만 대규모 과학 분야 범위 확대 필요

- **Clarity**: 3.5/5
  - 프레임워크 개요 명확하나, 구체적 구현(특히 자가평가 점수 계산, MCTS 상세) 설명 부족
  - Figure 1은 개괄적이나, 각 모듈의 수식 및 알고리즘 가시화 미흡
  - 프롬프트 템플릿 위치(Figure S)가 보충자료에 산재

- **Overall**: 4/5

**총평**: LLM의 도메인 지식과 자가 평가 메커니즘을 창의적으로 결합하여 해석 가능한 과학 공식 자동 발견에 중요한 진전을 이룬 의미 있는 연구. Feynman 공식 검증과 재료과학 응용이 강점이나, 기술 상세도 개선과 학제 간 확장을 통해 더욱 견고해질 여지 있음.

## Related Papers

- 🔄 다른 접근: [[papers/275_Discovering_symbolic_differential_equations_with_symmetry_in/review]] — 둘 다 AI를 이용한 과학 공식 발견을 다루지만, 하나는 LLM 기반이고 다른 하나는 대칭성을 활용한 기호적 미분방정식 발견에 초점을 맞춘다.
- 🔗 후속 연구: [[papers/503_LLM-ODE_Data-driven_Discovery_of_Dynamical_Systems_with_Larg/review]] — LLM을 이용한 동역학 시스템 발견의 체계적인 벤치마크를 제공하여 LLM-Feynman의 성능을 평가할 수 있다.
- 🔄 다른 접근: [[papers/289_Drsr_Llm_based_scientific_equation_discovery_with_dual_reaso/review]] — 둘 다 과학 공식 발견을 목표로 하지만 하나는 LLM 기반이고 다른 하나는 데이터와 경험의 이중 추론을 사용한다.
