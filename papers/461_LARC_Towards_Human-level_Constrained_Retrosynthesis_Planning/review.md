---
title: "461_LARC_Towards_Human-level_Constrained_Retrosynthesis_Planning"
authors:
  - "Frazier N. Baker"
  - "Daniel Adu-Ampratwum"
  - "Reza Averly"
  - "Botao Yu"
  - "Huan Sun"
date: "2025"
doi: "10.48550/arXiv.2508.11860"
arxiv: ""
score: 4.2
essence: "본 논문은 대규모 언어 모델(LLM) 기반의 에이전트 프레임워크 LARC를 제안하여, 화학에서 발암물질 회피, 자연발화물질 제거 등 실질적인 제약조건 하에서 망원(retrosynthesis) 계획을 수행한다. LARC는 72.9%의 성공률을 달성하여 기존 LLM 기반 방법을 크게 상회하고 인간 전문가 수준에 접근한다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/Retrosynthesis_Strategy_Planning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Baker et al._2025_LARC Towards Human-level Constrained Retrosynthesis Planning through an Agentic Framework.pdf"
---

# LARC: Towards Human-level Constrained Retrosynthesis Planning through an Agentic Framework

> **저자**: Frazier N. Baker, Daniel Adu-Ampratwum, Reza Averly, Botao Yu, Huan Sun | **날짜**: 2025 | **DOI**: [10.48550/arXiv.2508.11860](https://doi.org/10.48550/arXiv.2508.11860)

---

## Essence

![Figure 1: LARC 개요](figures/fig1.webp) *그림 1: LARC 프레임워크 개요. (a) 사용자 프롬프트로 목표 분자와 제약조건 지정, (b) EVALUATOR가 각 반응을 제약조건에 대해 평가, (c) 툴박스로 평가 근거화, (d) SYNTHESIZER가 피드백을 반영하여 경로 탐색, (e) 제약조건을 만족하는 합성 경로 출력*

본 논문은 대규모 언어 모델(LLM) 기반의 에이전트 프레임워크 LARC를 제안하여, 화학에서 발암물질 회피, 자연발화물질 제거 등 실질적인 제약조건 하에서 망원(retrosynthesis) 계획을 수행한다. LARC는 72.9%의 성공률을 달성하여 기존 LLM 기반 방법을 크게 상회하고 인간 전문가 수준에 접근한다.

## Motivation

- **Known**: 기존 AI 기반 망원 계획 방법들은 주로 제약조건 없는 경로 생성에 집중했으며, 극소수의 방법만 사용자 지정 분자 포함 같은 단순한 제약만 지원한다.

- **Gap**: 발암물질, 자연발화물질, 위험 물질 군(class) 회피 같은 실질적이고 복잡한 다중 제약조건을 광범위하게 지원하는 방법이 부재하다. 기존 재순위 기반 접근(Bran et al., 2025)은 계산 비효율적이고 LLM의 고유 지식에만 의존한다.

- **Why**: 화학에서 제약조건 평가는 (1) 다양한 해저드로부터의 회피 필요, (2) 화학 참고자료 활용의 필요성, (3) 단계별 합리적 의사결정이 필수적이어서 LLM 에이전트의 도구 활용이 적합하다.

- **Approach**: Agent-as-a-Judge 패러다임을 도입하여, EVALUATOR(평가 담당)와 SYNTHESIZER(탐색 담당)의 이중 구조로 반응 단위 피드백을 제약조건 인식형 가치 함수에 통합한다.

## Achievement

![Figure 3: LARC와 전문가 합성 경로 비교](figures/fig3.webp) *그림 3: LARCMistral과 EXPERT의 합성 경로 비교. 특정 중간체에서 LARC가 더 효율적인 경로를 발견함*

1. **성과1 - 높은 성공률**: 48개의 주의깊게 선별된 제약조건 망원 과제(3가지 제약유형)에서 72.9% 성공률 달성. 일반 LLM 기준선 대비 압도적 우월성 입증.

2. **성과2 - 전문가 수준 접근**: 인간 화학 전문가의 성공률에 근접하면서도 실행 시간을 크게 단축. 사례 연구에서 인간 전문가의 논리를 모방하거나 일부 과제에서 더 우수한 경로 발견.

3. **성과3 - 도구 기반 피드백의 효과성**: 제거 실험을 통해 도구 활용의 핵심 역할 입증. 발암물질 예측기, 자연발화물질 예측기 등 화학 특화 도구의 통합이 성능 향상을 견인.

## How

- **EVALUATOR 구조**:
  - *평가 계획(Evaluation Planning)*: 사용자 제약조건에 맞춤형 평가 지침 수립, 도구 선택 및 점수 전략 결정
  - *반응 평가(Reaction Evaluation)*: 고유 지식과 외부 도구를 적응적으로 전환하며 반응을 1-5 점수로 평가 (1: 완전 위반, 5: 완전 만족)

- **SYNTHESIZER의 제약 통합**:
  - 기존 무제약 망원 계획 알고리즘(여기선 MEEA*)을 적응하여 사용
  - 원래 가치 함수 V(m, R)를 제약 인식형 함수로 확장: **V'(m, R) = V(m, R) + λ∑ S(r)**
  - 이를 통해 MCTS 시뮬레이션과 A* 탐색 양쪽에서 제약조건 반영
  - 미평가 반응은 낙관적 점수(5점) 사용으로 탐색 격려

- **확장성 설계**:
  - 새로운 도구나 제약유형 추가 시 EVALUATOR만 수정하면 됨
  - 다른 무제약 계획 알고리즘으로 SYNTHESIZER 교체 가능 (원래 V 재학습 불필요)

## Originality

- **제약 통합의 혁신성**: 기존 재순위 방식(post-hoc filtering)과 달리, 제약 평가를 계획 과정 내부에 직접 통합하는 최초의 접근. 경로 전체의 제약 만족도를 누적하여 고려.

- **Agent-as-a-Judge 패러다임**: 화학 도구를 활용한 근거 기반 평가(grounded evaluation)로 LLM의 할루시네이션 위험 완화. 인간 화학자의 참고자료 활용 행동 모방.

- **다양한 실질적 제약 지원**: 포함(inclusion) 제약의 단순성을 벗어나, 발암성, 자연발화성, 사용자 지정 물질 회피 같은 다중 해저드 제약을 동시 지원.

- **하이퍼파라미터 선택의 합리성**: λ를 통한 원래 가치함수와 제약 점수의 가중 결합으로 유연한 제약 강도 조절.

## Limitation & Further Study

- **평가 데이터셋 규모**: 48개 과제는 프루프 오브 컨셉으로는 의미 있으나, 광범위한 화학 공간에서의 일반화 능력을 완전히 검증하기엔 제한적. 더 대규모의 다양한 제약조건 데이터셋 필요.

- **도구 정확성 의존성**: EVALUATOR의 성능이 발암물질, 자연발화물질 예측 도구의 정확성에 크게 의존. 도구 오류는 직접 평가 오류로 전파됨. 도구 신뢰도 평가 메커니즘 부재.

- **제약 유형 확장의 한계**: 현재 3가지 제약유형만 시연. 용해도, 수율 예측, 원자 경제성, 환경 영향 등 더 복잡한 물리화학적 제약으로 확장 시 새로운 도구 개발 필요.

- **비용-효율 분석 부재**: LLM API 호출 횟수, 전산 비용이 명시적으로 분석되지 않음. 산업 적용 가능성 평가를 위한 경제성 분석 필요.

- **해석가능성 제한**: EVALUATOR의 의사결정 과정(어떤 도구를 언제 사용했는지)이 충분히 기록·분석되지 않아, 오류 발생 시 원인 규명 어려움.

- **향후 방향**: (1) 도구 정확성 향상 및 신뢰도 추정, (2) 더 다양한 실제 화학 제약조건 통합, (3) 인간-AI 협업 인터페이스 설계, (4) 합성 경로의 실험적 검증.


## Evaluation

- Novelty: 4.2/5
- Technical Soundness: 4.0/5
- Significance: 4.1/5
- Clarity: 4.3/5
- Overall: 4.2/5

**총평**: 본 논문은 LLM 기반 에이전트를 화학의 실질적 제약조건 망원 계획에 처음 적용한 의미 있는 연구로, Agent-as-a-Judge를 계획 루프 내부에 통합하는 설계가 창의적이며 72.9% 성공률로 높은 실효성을 입증한다. 다만 평가 데이터셋 규모가 제한적이고 도구 정확성 의존성, 제약유형 확장성, 비용 분석 부재 등이 보완되어야 산업 적용 가능성이 확보될 것으로 예상된다.

## Related Papers

- 🔄 다른 접근: [[papers/788_Targeted_materials_discovery_using_Bayesian_algorithm_execut/review]] — 베이지안 알고리즘 실행을 통한 재료 발견과 LLM 기반 역합성 계획은 서로 다른 AI 접근법으로 화학 문제를 해결합니다
- 🔗 후속 연구: [[papers/210_ChemCrow_Augmenting_large-language_models_with_chemistry_too/review]] — ChemCrow의 화학 도구 증강 언어모델은 LARC의 제약조건 기반 역합성 계획을 더욱 발전시킨 형태입니다
- 🧪 응용 사례: [[papers/744_Self-Driving_Laboratories_for_Chemistry_and_Materials_Scienc/review]] — 자율 실험실 기술은 LARC의 역합성 계획을 실제 화학 실험으로 구현하는 응용 분야입니다
- 🧪 응용 사례: [[papers/744_Self-Driving_Laboratories_for_Chemistry_and_Materials_Scienc/review]] — LARC의 제약조건 기반 역합성 계획은 자율 실험실에서 실제 화학 합성을 자동화하는 핵심 응용 기술입니다
- 🔄 다른 접근: [[papers/788_Targeted_materials_discovery_using_Bayesian_algorithm_execut/review]] — 베이지안 알고리즘 실행과 LLM 기반 역합성 계획은 모두 복잡한 재료/화학 설계 목표 달성을 위한 서로 다른 AI 기반 접근법입니다
- 🧪 응용 사례: [[papers/316_Enhancing_chemical_reaction_and_retrosynthesis_prediction_wi/review]] — 인간 수준의 제약 조건을 고려한 역합성 계획이 ChemDual의 역합성 예측 기능의 실제 적용 영역이다.
- 🏛 기반 연구: [[papers/459_Language_Models_for_Controllable_DNA_Sequence_Design/review]] — 제약 조건 하에서의 역합성 계획 연구가 조건부 DNA 서열 생성의 방법론적 기반을 제공한다.
