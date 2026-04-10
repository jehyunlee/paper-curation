---
title: "449_Kimi_k15_Scaling_reinforcement_learning_with_llms"
authors:
  - "Kimi Team"
  - "Angang Du"
  - "Bofei Gao"
  - "Bowei Xing"
  - "Changjiu Jiang"
date: "2025"
doi: "arXiv:2501.12599v4"
arxiv: ""
score: 4.3
essence: "본 논문은 대규모 언어모델(LLM)의 강화학습(RL) 기반 훈련을 통해 추론 성능을 대폭 향상시킨 Kimi k1.5 모델을 제시한다. 긴 맥락(long context) 확장과 개선된 정책 최적화를 기반으로 복잡한 기법(MCTS, 가치함수 등) 없이도 o1 수준의 성능을 달성했다."
tags:
  - "cat/Reinforcement_Learning_and_Self-Verification"
  - "sub/Reasoning_Enhancement_via_Reinforcement_Learning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Team et al._2025_Kimi k1.5 Scaling reinforcement learning with llms.pdf"
---

# Kimi k1.5: Scaling reinforcement learning with llms

> **저자**: Kimi Team, Angang Du, Bofei Gao, Bowei Xing, Changjiu Jiang, Cheng Chen, Cheng Li, Chenjun Xiao, Chenzhuang Du, Chonghua Liao, Chuning Tang, Congcong Wang, Dehao Zhang, Enming Yuan, Enzhe Lu, Feng Tang, Flood Sung, Guangda Wei, Guokun Lai, Haiqing Guo | **날짜**: 2025 | **DOI**: arXiv:2501.12599v4

---

## Essence

![Figure 1: Kimi k1.5 long-CoT results](figures/fig1.webp)

본 논문은 대규모 언어모델(LLM)의 강화학습(RL) 기반 훈련을 통해 추론 성능을 대폭 향상시킨 Kimi k1.5 모델을 제시한다. 긴 맥락(long context) 확장과 개선된 정책 최적화를 기반으로 복잡한 기법(MCTS, 가치함수 등) 없이도 o1 수준의 성능을 달성했다.

## Motivation

- **Known**: 
  - 차세대 토큰 예측 기반 사전훈련은 사용 가능한 고품질 데이터량으로 제한됨
  - RL은 LLM의 새로운 확장 축을 제시하지만 선행 연구는 경쟁력 있는 결과 미흡

- **Gap**: 
  - RL과 LLM의 효과적 결합 방식이 확립되지 않음
  - 복잡한 계획 알고리즘 없이도 강력한 추론 성능 달성 가능성 미탐색

- **Why**: 
  - 모델이 보상 신호로부터 자동 탐색 가능 → 정적 데이터셋 한계 극복
  - 긴 맥락 윈도우 활용으로 암시적 탐색 공간 구성 가능

- **Approach**: 
  - 128k 토큰 맥락 창 확장
  - 부분 롤아웃(partial rollout)을 통한 훈련 효율화
  - 온라인 미러 강하(online mirror descent) 기반 정책 최적화
  - 멀티모달 RL 훈련

## Achievement

![Figure 2: Kimi k1.5 short-CoT results](figures/fig2.webp)

1. **Long-CoT 성능**: AIME 77.5점(o1 74.4점과 동등), MATH-500 96.2점(o1 94.8점 상회), Codeforces 94 백분위 달성
   - MathVista 74.9점, MMMU 70점으로 멀티모달 추론 우수성 입증

2. **Short-CoT 성능**: AIME 60.8점(GPT-4o 16점 대비 +550%), MATH-500 94.6점으로 기존 단문 추론 모델 대폭 초과
   - LiveCodeBench 47.3점으로 코딩 추론 성능 향상

3. **Long2Short 방법론**: 긴 추론에서 학습한 활성화 패턴을 단문 모델에 이전하여 성능 유지

## How

![Figure 3: Large Scale Reinforcement Learning Training System for LLM](figures/fig3.webp)

- **RL 프롬프트 셋 큐레이션**:
  - 다양한 학문 분야 커버(STEM, 코딩, 일반 추론)
  - 모델 기반 난이도 평가: SFT 모델의 10회 샘플링 통과율로 난이도 산정
  - 보상 해킹 방지: 8회 무추론 샘플링으로 정답 도달 가능한 문제 제거

- **Long-CoT 지도 미세조정**:
  - 고품질 추론 경로 데이터셋 구성
  - 계획(planning), 평가(evaluation), 반성(reflection), 탐색(exploration) 요소 포함
  - 긴 맥락에서 자동회귀 추론으로 암시적 계획 수행

- **강화학습 최적화**:
  - 부분 롤아웃: 이전 궤적 재사용으로 처음부터 생성 비용 절감
  - 온라인 미러 강하 변형으로 견고한 정책 최적화
  - 길이 페널티와 데이터 레시피 최적화 통합
  - 검증 가능 문제는 규칙 기반 보상, 일반 QA는 학습된 보상 모델 활용

## Originality

- **맥락 길이의 명시적 확장 축**: 128k 토큰 범위에서 RL 성능이 지속 향상됨을 입증 → 기존의 MCTS나 가치함수 중심 접근과 차별화

- **부분 롤아웃 기법**: 이전 궤적 재사용으로 RL 훈련 효율성 대폭 개선 → 대규모 훈련 가능성 제시

- **단순한 프레임워크의 강력성**: 복잡한 별도 계획 알고리즘 없이 자동회귀 생성만으로 암시적 탐색 달성

- **멀티모달 RL 훈련**: 텍스트와 비전 데이터 공동 훈련으로 크로스모달 추론 능력 확보

- **Long2Short 지식 이전**: 장문 추론의 내부 표현을 단문 모델에 적용하는 체계적 방법론

## Limitation & Further Study

- **검증 모델의 한계**: 보상 해킹 방지를 위한 현재 방법(N=8 무추론 샘플링)이 경험적 휴리스틱 → 더 정교한 검증 모델 개발 필요

- **훈련 데이터 공개 미흡**: RL 프롬프트 셋 상세 구성 및 규모에 대한 구체적 정보 부족 → 재현성 제한

- **추론 비용 분석 부재**: 긴 맥락 활용으로 인한 추론 시간/계산량 증가의 정량적 평가 미제시

- **문제 도메인 한정성**: STEM, 코딩 중심의 검증 가능 문제에 최적화 → 개방형 생성 과제로의 확장 방안 미명시

- **후속 연구 방향**:
  - 더욱 정교한 보상 모델 및 검증 시스템 개발
  - 다양한 도메인(대화, 창작, 분석)으로의 RL 확대 적용
  - 추론 효율성 최적화 (길이-성능 트레이드오프 개선)
  - 가치함수 없는 계획의 이론적 근거 강화

## Evaluation

- **Novelty**: 4.5/5
  - 맥락 확장을 RL의 주축으로 명시적 제시한 점 신선로움
  - 부분 롤아웃, Long2Short 방법론 창의성 높음
  - 다만 온라인 미러 강하는 기존 기법의 응용

- **Technical Soundness**: 4/5
  - RL 프롬프트 셋 큐레이션, 지도 미세조정 등 각 단계가 체계적 설계됨
  - 보상 모델, 정책 최적화 방법론이 합리적
  - 훈련 세부사항 공개 미흡으로 재현성 검증 제약

- **Significance**: 5/5
  - o1 수준의 추론 성능 달성 → 기존 SOTA 모델 초과
  - Short-CoT 성능 (최대 550% 개선)으로 실용성 높은 결과 제시
  - 멀티모달 추론 성능 우수성으로 적용 범위 확대

- **Clarity**: 3.5/5
  - 핵심 아이디어(맥락 확장, 부분 롤아웃) 명확
  - 방법론 상세 설명 충분하나 인프라, 계산량 등 구체적 수치 부족
  - RL 훈련 알고리즘의 수식 표현 단순 (목적함수 구체화 필요)

- **Overall**: 4.3/5

**총평**: 본 논문은 긴 맥락과 간단한 정책 최적화만으로 o1 수준의 추론 성능을 달성한 점에서 실질적 기여도가 크다. 특히 Long2Short 기법으로 단문 모델도 대폭 향상시킨 결과는 실무적 가치가 높으나, 훈련 데이터 공개 미흡과 이론적 근거 보강이 이루어진다면 더욱 설득력 있는 연구가 될 것으로 판단된다.

## Related Papers

- 🔄 다른 접근: [[papers/265_DeepSeek-R1_incentivizes_reasoning_in_LLMs_through_reinforce/review]] — 두 논문 모두 강화학습으로 LLM 추론을 향상시키되 Kimi k1.5는 긴 맥락 확장, DeepSeek-R1은 순수 RL에 중점을 둔다.
- 🔗 후속 연구: [[papers/422_Improving_generalization_of_robot_locomotion_policies_via_sh/review]] — 로봇 정책의 일반화 성능 향상을 위한 SAM 기법은 Kimi k1.5의 정책 최적화 방법론에 샤프니스 인식 최소화를 도입할 수 있다.
- 🏛 기반 연구: [[papers/033_A_survey_on_large_language_model_based_autonomous_agents/review]] — 대규모 언어모델 기반 자율 에이전트 서베이는 Kimi k1.5의 강화학습 기반 에이전트 설계에 이론적 배경과 방법론적 근거를 제공한다.
- 🔄 다른 접근: [[papers/265_DeepSeek-R1_incentivizes_reasoning_in_LLMs_through_reinforce/review]] — 두 논문 모두 강화학습으로 LLM의 추론 능력을 향상시키되 DeepSeek-R1은 순수 RL, Kimi k1.5는 긴 맥락과 정책 최적화를 강조한다.
