---
title: "085_Ai-newton_A_concept-driven_physical_law_discovery_system_wit"
authors:
  - "You-Le Fang"
  - "Dong-Shan Jian"
  - "Xiang Li"
  - "Yan-Qing Ma"
date: "2025"
doi: "N/A"
arxiv: ""
score: 4.3
essence: "AI-Newton은 감독 없이 원본 다중 실험 데이터로부터 뉴턴의 제2법칙, 에너지 보존, 중력의 보편 법칙 등 일반적인 물리 법칙을 자동으로 발견하는 개념 기반 과학 발견 시스템이다. 이는 기존 AI 방식의 한계인 '개별 실험의 경험적 모델 도출'을 넘어 '다양한 현상에 공통으로 적용되는 기본 물리 법칙의 발견'을 달성한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Autonomous_Hypothesis_Discovery"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Yang et al._2025_Ai-newton A concept-driven physical law discovery system without prior physical knowledge.pdf"
---

# AI-Newton: A concept-driven physical law discovery system without prior physical knowledge

> **저자**: You-Le Fang, Dong-Shan Jian, Xiang Li, Yan-Qing Ma | **날짜**: 2025 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)
*AI-Newton의 실험 기반(experiment base), 이론 기반(theory base), 자동 발견 워크플로우*

AI-Newton은 감독 없이 원본 다중 실험 데이터로부터 뉴턴의 제2법칙, 에너지 보존, 중력의 보편 법칙 등 일반적인 물리 법칙을 자동으로 발견하는 개념 기반 과학 발견 시스템이다. 이는 기존 AI 방식의 한계인 '개별 실험의 경험적 모델 도출'을 넘어 '다양한 현상에 공통으로 적용되는 기본 물리 법칙의 발견'을 달성한다.

## Motivation

- **Known**: 현재 AI 기반 물리 발견 방법들은 개별 실험에서 신경망(NN) 또는 기호 회귀(symbolic regression) 기법을 통해 특정 모델을 도출하는 데 성공했다. 다만 이들은 단일 실험 내에서의 문제별 모델 핏팅(problem-specific model fitting)에 제한된다.

- **Gap**: 인간 과학자가 수행하는 고차원적 사고—즉, 여러 실험의 특정 모델들에서 공통 패턴을 찾아 모든 실험에 적용 가능한 일반 법칙을 수립하는 능력—을 AI가 아직 달성하지 못했다.

- **Why**: 진정한 과학 발견은 보편적이고 일반화 가능한 지식의 추출에 있다. 뉴턴 역학처럼 의미 있는 물리 개념을 정의하고 다양한 현상을 설명하는 일반 법칙을 수립하는 것이 과학의 궁극 목표다.

- **Approach**: 개념 기반 발견(concept-driven discovery) 접근법을 채택하며, 명시적 기호 표현(explicit symbolic representation)으로 물리 개념과 법칙을 구성하고, 개연적 추론(plausible reasoning)과 기호 회귀를 결합한 자동화 워크플로우를 설계했다.

## Achievement

![Figure 2](figures/fig2.webp)
*테스트된 실험들의 개략도 및 발견된 주요 일반 법칙들*

1. **일반 법칙의 자동 발견**: 46개의 고전 역학 실험에서 뉴턴의 제2법칙(Newton's second law), 에너지 보존 법칙(energy conservation), 만유중력의 법칙(universal gravitation) 등 약 50개의 일반 법칙을 자동으로 재발견했다.

2. **개념의 자동 추출**: 시공간 좌표만을 초기 입력으로 하여 감독 없이 약 90개의 물리 개념(질량, 속도, 운동에너지, 중력 퍼텐셜 등)을 자동 도출했다.

3. **노이즈 있는 현실적 데이터 처리**: 가우시안 오차를 포함한 미분방정식 기반 시뮬레이션 데이터에서도 안정적으로 법칙을 발견하여 실험적 타당성을 입증했다.

4. **복잡 시스템 처리 능력**: 단순한 자유 운동부터 연쇄 2-볼-2-스프링 시스템의 결합 진동, 4-볼-4-스프링 시스템의 회전 동역학 등 고자유도(high-degree-of-freedom) 문제까지 다룰 수 있음을 입증했다.

## How

![](figures/fig1.webp)

**지식 기반(Knowledge Base) 구성:**
- **실험 기반**: 물리 객체(공, 스프링, 경사면), 기하 정보, 실험 매개변수, 시공간 좌표만을 입력으로 하고, 노이즈가 포함된 시뮬레이션 데이터를 출력
- **이론 기반**: 기호, 개념, 법칙을 상호연결된 라이브러리로 저장 (동역학 개념, 본질적 개념, 보편 상수로 분류)
- **물리 DSL(Domain-Specific Language)**: 개념과 법칙을 명시적 기호 형태로 표현하며, 측정 절차를 기록하여 개념 일관성 보장

**자동 발견 워크플로우:**
- **시험 선택**: UCB(Upper Confidence Bound) 기반 값 함수와 동적 신경망을 결합한 추천 엔진으로 실험과 개념 선택 (탐색-활용 트레이드오프 자동 조절)
- **에라 제어 전략**: 초기 단계에서는 단순한 실험에 집중하고, 새로운 지식 획득이 중단되면 시간 제한을 지수적으로 증가시켜 단계적 학습 구현
- **법칙 탐색**: 기호 회귀(SR)로 특정 법칙 발견, PCA 기반 미분 다항식 회귀(differential polynomial regression) 활용
- **개연적 추론**: 기존 일반 법칙이 특정 실험에서 실패하면, 간단한 항을 추가하여 수정된 법칙 도출 (예: 탄성 충돌의 운동 에너지 보존 → 스프링 시스템에 탄성 퍼텐셜 에너지 항 추가)
- **지식 단순화**: Rosenfeld Gröbner 알고리즘(differential algebra)으로 중복 지식 제거 및 최소 표현 달성
- **종속성 분석**: 제어변수 분석(controlled-variable analysis)으로 물리 객체와 실험 매개변수에 대한 관계 의존성 파악

## Originality

- **명시적 기호 표현**: 기존 연구가 신경망의 잠재 특징(latent features)을 물리 개념으로 해석하던 것과 달리, AI-Newton은 물리 개념과 법칙을 구조화된 DSL로 명시적으로 표현하여 해석 가능성(interpretability)과 전이 가능성(transferability) 획기적 향상

- **계층적 지식 표현**: 동역학 개념 → 본질적 개념 → 보편 상수 → 특정 법칙 → 일반 법칙으로 이어지는 다층 구조로, 복잡한 다중 객체 시스템의 동역학 방정식을 일반 법칙으로부터 자동 도출 가능

- **개연적 추론 기반 발견**: 과학적 가설 수립 과정을 모방하여, 기존 법칙의 부분적 실패로부터 새로운 일반 법칙을 체계적으로 생성

- **다중 실험 통합 학습**: 개별 실험의 특정 모델들에서 공통 일반 법칙을 추출하는 메타-수준의 발견 능력—기존 AI 방법이 달성하지 못한 수준

## Limitation & Further Study

- **제한된 검증 범위**: 현재 증명 개념(proof-of-concept)은 고전 역학 범위 내에서만 평가되었으며, 양자역학, 상대성 이론, 열역학 등 다른 물리학 분야에 대한 확장 가능성은 미지수이다.

- **계산 자원 의존성**: 1200회 최대 시도에 48시간 평균 실행 시간이 소요되어, 더 큰 실험 집합이나 더 복잡한 법칙 발견에는 상당한 컴퓨팅 자원이 필요하다.

- **DSL 설계의 수동성**: 물리 DSL의 기본 구조(측정 절차 정의, 객체 타입 분류 등)는 여전히 사람이 설계해야 하므로, 진정한 '사전 물리 지식 무': 제한적이다.

- **후속 연구 방향**:
  - 자동 DSL 생성 또는 학습 메커니즘 개발
  - 다양한 물리학 분야 적용 및 일반화 가능성 검증
  - 발견 속도 최적화 및 병렬화 구조 개선
  - 실험적 노이즈의 상한선 설정 및 로버스트성 강화
  - 인간 과학자와의 상호작용 모드 설계 (예: 가설 기반 실험 제안)

## Evaluation

- **Novelty**: 4.5/5
  - 개념 기반 발견과 명시적 기호 표현이라는 신선한 접근
  - 다중 실험 통합 학습으로 일반 법칙 추출은 매우 참신함
  - 다만 기호 회귀, 개연적 추론, 제어변수 분석 각각은 기존 기법들의 조합

- **Technical Soundness**: 4/5
  - 워크플로우 설계가 체계적이고 논리적
  - Rosenfeld Gröbner 알고리즘 등 정교한 수학적 도구 활용
  - 에라 제어 전략으로 단계적 학습 구현이 우수함
  - 다만 플러시블 러시닝(plausible reasoning)의 구체적 수학적 정의가 다소 약함

- **Significance**: 4.5/5
  - AI 기반 과학 발견의 패러다임 전환 제시 (개별 모델 도출 → 일반 법칙 추출)
  - 뉴턴 역학의 기본 법칙 재발견은 원칙 검증으로서 높은 의미
  - 향후 물리학 외 타 과학 분야(화학, 생물학) 확장 잠재력 큼
  - 그러나 현재는 고전 역학에만 국한되어 즉각적 실무 적용성은 제한적

- **Clarity**: 4/5
  - 논문 구조가 명확하고 주요 아이디어가 잘 전달됨
  - Figure 2로 발견된 법칙들이 시각화되어 좋음
  - DSL 문법 설명(식 1-4)이 구체적이고 이해하기 쉬움
  - 다만 워크플로우의 상세 알고리즘은 Supplemental Materials 참조 필요

- **Overall**: 4.3/5

**총평**: AI-Newton은 기존 AI 기반 물리 발견 방법의 근본적 한계를 명확히 인식하고, 명시적 기호 표현과 개념 기반 발견이라는 창의적 해결책을 제시한 의미 있는 연구다. 뉴턴 역학 범위 내에서의 성공적 재발현은 원칙 검증으로서 가치 있으나, 향후 더 광범위한 물리 영역 적용, 발견 속도 최적화, 진정한 감독 없는 학습 달성을 위한 후속 개선이 필요하다.

## Related Papers

- 🏛 기반 연구: [[papers/275_Discovering_symbolic_differential_equations_with_symmetry_in/review]] — 기호적 미분방정식 발견의 기본적 접근법을 다중 실험 데이터에서 일반 물리 법칙을 발견하는 고도화된 시스템으로 발전시킨다.
- 🔗 후속 연구: [[papers/012_A_Multi-agent_Framework_for_Physical_Laws_Discovery/review]] — 물리 법칙 발견을 위한 다중 에이전트 프레임워크의 개념적 기반을 실제 작동하는 시스템으로 구현한다.
- 🔄 다른 접근: [[papers/764_Sparks_Multi-Agent_Artificial_Intelligence_Model_Discovers_P/review]] — 물리 법칙과 생명과학이라는 서로 다른 과학 영역에서 개념 기반 자동 발견 접근법을 비교한다.
- 🔗 후속 연구: [[papers/764_Sparks_Multi-Agent_Artificial_Intelligence_Model_Discovers_P/review]] — 단백질 분야의 구체적 발견을 물리 법칙 발견으로 확장하여 자동화된 과학 발견의 일반화 가능성을 보여준다.
