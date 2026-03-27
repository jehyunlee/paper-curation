# Can we automatize scientific discovery in the cognitive sciences?

> **저자**: Akshay K. Jagadish, Milena Rmus, Kristin Witte, Marvin Mathony, Marcel Binz, Eric Schulz | **날짜**: 2026-03-22 | **arXiv**: 2603.20988 | **분야**: cs.AI

---

## Essence

인지과학의 발견 사이클(실험 설계 -> 데이터 수집 -> 모델 비교 -> 결론 도출)을 LLM 기반으로 완전 자동화하는 "in silico science of the mind" 비전을 제시하는 짧은 Perspective 논문이다. LLM이 실험 패러다임을 제안하고(Experimentalist), cognitive foundation model(Centaur)이 합성 행동 데이터를 생성하며, LLM 기반 program synthesis가 인지 모델을 대규모 탐색하고(Modeller), LLM-critic이 "interestingness"를 평가하여 루프를 닫는 4단계 자동 발견 엔진을 구상한다.

## Motivation

- **알려진 것**: 인지과학은 계산 모델로 지능을 이해하려는 학문으로, 실험 설계 -> 데이터 수집 -> 모델 테스트 -> 결론의 발견 사이클을 따름
- **Gap**: 이 사이클의 모든 단계가 인간의 수동 개입에 의존하여 (i) 인간 개입의 느린 속도에 제약받고, (ii) 연구자의 배경과 직관에 의해 탐색 공간이 제한되며, (iii) 소수의 handcrafted 모델만 비교하는 구조적 한계 존재
- **왜 중요한가**: 인지 과정의 가능한 계산 메커니즘 공간이 인간이 수동으로 탐색할 수 있는 범위를 훨씬 초과하며, 혁신적 발견은 종종 기존 탐색 공간 밖에서 발생
- **접근법**: LLM을 실험 설계자, 데이터 생성기(cognitive foundation model), 모델 합성기, 평가 비평가로 각각 활용하여 발견 사이클 전체를 자동화

## Achievement

1. **4단계 자동 발견 사이클 설계**: Experimentalist(LLM 기반 실험 제안) -> Cognitive Foundation Model(Centaur 기반 합성 행동 데이터 생성) -> Modeller(LLM program synthesis로 인지 모델 대규모 탐색) -> Critic(LLM이 "interestingness" 평가)
2. **Generative grammar 접근과 LLM sampler의 결합 제안**: MDP 기반 형식 문법으로 실험 공간을 정의하되, LLM을 "intelligent experiment sampler"로 사용하여 문법의 표현력 한계를 극복
3. **Cognitive foundation model (Centaur) 활용**: 인간 인지의 foundation model로부터 high-fidelity 합성 행동 데이터를 생성하여 실제 인간 실험의 비용/시간을 대폭 절감
4. **GeCCo 파이프라인 소개**: LLM이 인지 모델을 Python 함수로 합성하고, 예측 성능 피드백을 기반으로 반복 정제하는 Guided generation of Computational Cognitive Models 접근
5. **실패 모드의 솔직한 진단**: 5가지 핵심 위험(문법의 표현력 한계, 합성 데이터의 비충실성, 모델 발견의 비매끄러운 최적화, interestingness 정의의 순환성, 실제 인간 검증 필요성)을 명시적으로 논의

## How

- **실험 설계 (Experimentalist)**: MDP 기반 generative grammar으로 의사결정 과제 공간을 정의 (상태, 전이 동역학, 보상 구조) + LLM이 특정 행동을 유도할 실험을 직접 제안하고 피드백 기반으로 실험 요인을 추가/제거
- **데이터 생성**: Centaur 모델(인간 인지의 foundation model)에 과제 설명과 참가자별 메타데이터(나이, 성별, 교육 등)를 입력하여 합성 행동 데이터 생성 -- 개인차와 모집단 수준 효과 모두 시뮬레이션 가능
- **모델 합성 (Modeller)**: GeCCo(LLM 기반 인지 모델 합성) -- LLM이 인지 모델을 Python 함수로 생성하고, 예측 성능 피드백으로 반복 정제; 대안으로 evolutionary algorithm(FunSearch 등)이나 hybrid 시스템도 가능
- **루프 닫기 (Critic)**: LLM-critic이 결과의 "interestingness"(참신성, 문헌 적합성, 품질, 불확실성 등)를 평가하여 다음 실험 사이클에 피드백; Bayesian optimization 유사하나 "interest" 함수가 LLM에 의해 정의

## Originality

- **인지과학 발견 사이클의 완전 자동화 비전**: AI Scientist 등 일반적 연구 자동화와 달리, 인지과학의 고유한 발견 구조(실험 패러다임 -> 행동 데이터 -> 계산 모델 -> 이론)에 특화된 자동화 설계
- **Cognitive foundation model을 in-loop data generator로 활용**: Centaur 모델을 합성 데이터 생성기로 사용하여 인간 실험 없이 가설 탐색을 가속화하는 아이디어 -- "accelerator for hypothesis generation, not ground truth"라는 실용적 위치 설정
- **"Interestingness"의 LLM 기반 정의**: 과학적 발견의 가치를 LLM-critic으로 평가한다는 제안은 도발적이며, 이것이 순환적(circular)일 수 있다는 위험을 저자 스스로 인정

## Limitation & Further Study

### 저자들이 언급한 한계

- 실험 문법(grammar)의 표현력이 탐색 가능한 실험 공간을 근본적으로 제약 -- "No search procedure can discover what the representation forbids"
- 합성 데이터가 실제 인간 행동의 충실한 대체물이 아닐 수 있음 -- shortcut, average subject으로의 drift, distribution shift 위험
- 모델 발견이 rugged optimization landscape에서 이루어지며, behavioral equivalence(행동적으로 구분 불가능한 상이한 메커니즘)의 문제
- "Interestingness"의 정의가 순환적일 수 있음 -- LLM의 편향이 발견 방향을 제한할 가능성
- 최종적으로 실제 인간 참가자를 대상으로 한 검증이 필수적

### 자체판단 아쉬운 점

- 5페이지의 짧은 Perspective로, 각 구성 요소의 기술적 깊이가 매우 제한적 -- Centaur 모델의 한계, GeCCo의 수렴 특성, 실험 문법의 구체적 설계 등이 모두 참조로만 처리됨
- 어떤 구성 요소도 통합적으로 구현/실증되지 않았으며, 개별 구성 요소(Centaur, GeCCo)의 기존 결과만 인용
- 인지과학 이외의 행동과학(경제학, 사회심리학 등)으로의 일반화 가능성 논의가 부족
- "Interestingness"를 LLM이 평가한다는 제안의 구체적 구현 방안(프롬프트 설계, 평가 기준의 operationalization)이 제시되지 않음
- In silico 발견이 실제 인간 실험과의 validation loop를 어떻게 구성할지에 대한 구체적 방법론이 미비

### 후속 연구

- MDP 이외의 인지 과제 도메인(기억, 범주화, 추론, 사회적 인지)으로 실험 문법 확장
- Centaur 모델의 adversarial evaluation -- 기존 인지심리학 벤치마크 효과에 대한 체계적 검증
- 자동 발견 사이클의 end-to-end 파일럿 구현 및 실제 인간 실험과의 validation
- "Interestingness" metric의 형식화 -- 정보 이론적 접근(예: Bayesian surprise) vs LLM judge의 비교 연구
- 발견 루프에서 생성된 가설의 재현성(reproducibility) 검증 프레임워크 개발

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 2/5 |
| Significance | 4/5 |
| Clarity | 4/5 |
| Overall | 3/5 |

**총평**: 인지과학의 발견 사이클을 LLM과 cognitive foundation model로 완전 자동화하겠다는 대담한 비전을 제시한 짧은 Perspective 논문이다. 특히 Centaur를 in-loop data generator로 사용하고, LLM program synthesis로 인지 모델을 대규모 탐색한다는 아이디어는 인지과학과 AI의 교차점에서 참신하다. 그러나 5페이지 분량의 제약으로 각 구성 요소의 기술적 깊이가 부족하고, 통합 구현이 없으며, 실패 모드(특히 LLM에 의한 interestingness 평가의 순환성)가 핵심 위험으로 남아 있다. "In silico science of the mind"라는 방향성 자체는 AI4Science 커뮤니티에서 주목할 가치가 있다.
