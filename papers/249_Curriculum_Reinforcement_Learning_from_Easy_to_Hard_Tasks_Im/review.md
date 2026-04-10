---
title: "249_Curriculum_Reinforcement_Learning_from_Easy_to_Hard_Tasks_Im"
authors:
  - "Shubham Parashar"
  - "Shurui Gui"
  - "Xiner Li"
  - "Hongyi Ling"
  - "Sushil Vemuri"
date: "2025"
doi: "10.48550/arXiv.2506.06632"
arxiv: ""
score: 4.0
essence: "본 논문은 대규모 언어모델(LLM)의 추론 능력을 강화학습(RL)과 커리큘럼 학습을 결합하여 개선하는 **E2H Reasoner** 방법을 제시한다. 작업을 난이도별로 분해하고 확률적 스케줄러를 통해 쉬운 작업에서 어려운 작업으로 점진적 학습을 수행함으로써, 단순 RL만으로는 해결 불가능한 추론 문제를 학습 가능하게 한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/AI-Powered_Research_Planning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Parashar et al._2025_Curriculum Reinforcement Learning from Easy to Hard Tasks Improves LLM Reasoning.pdf"
---

# Curriculum Reinforcement Learning from Easy to Hard Tasks Improves LLM Reasoning

> **저자**: Shubham Parashar, Shurui Gui, Xiner Li, Hongyi Ling, Sushil Vemuri | **날짜**: 2025 | **DOI**: [10.48550/arXiv.2506.06632](https://doi.org/10.48550/arXiv.2506.06632)

---

## Essence

![Figure 2](figures/fig2.webp)
*E2H Reasoner의 작업 분해: 학습이 진행됨에 따라 자명(Trivial) → 쉬움(Easy) → 중간(Medium) → 어려움(Hard) 작업으로 점진적 전환*

본 논문은 대규모 언어모델(LLM)의 추론 능력을 강화학습(RL)과 커리큘럼 학습을 결합하여 개선하는 **E2H Reasoner** 방법을 제시한다. 작업을 난이도별로 분해하고 확률적 스케줄러를 통해 쉬운 작업에서 어려운 작업으로 점진적 학습을 수행함으로써, 단순 RL만으로는 해결 불가능한 추론 문제를 학습 가능하게 한다.

## Motivation

- **Known**: DeepSeek-R1과 OpenAI o1 같은 모델들은 RL 기반 사후학습(post-training)을 통해 뛰어난 추론 능력을 보여준다. 그러나 기존 RL 방식만으로는 사전학습 모델이 0-shot으로 해결하지 못하는 어려운 작업 학습에 한계가 있다.

- **Gap**: 단순 RL은 어려운 작업에서 희소한 보상 신호(sparse reward)로 인해 학습이 비효율적이다. 또한 복잡한 추론 작업은 여러 기초 기술의 조합을 요구하는데, 세밀한 단계별 보상 설계는 작업 특화적이고 확장성이 떨어진다.

- **Why**: 커리큘럼 학습은 인간 학습과 유사하게 기초부터 심화 내용으로 순차 진행하여 학습 효율을 높일 수 있다. 작업 분해를 통해 분포 변화(distribution shift)를 완화하고, 난이도별 학습으로 기초 기술 습득을 단계화할 수 있다.

- **Approach**: 
  1. 학습 데이터를 난이도별 부분집합으로 분해 (자명/쉬움/중간/어려움)
  2. 학습 진행에 따라 확률적 스케줄러로 작업 비중을 동적 조정
  3. 이론적 수렴 보장 제공 (Approximate Policy Iteration 프레임워크)

## Achievement

![Figure 1](figures/fig1.webp)
*Pass@k 평가에서 E2H가 기저 모델을 상회: (a) Countdown, (b) Blocksworld, (c) LLaMA 3.2 3B의 추론 예시*

1. **실증적 성과**: 5개 추론 작업(Blocksworld, Countdown, MATH, AQuA, GSM8K)에서 최고 성능(SOTA) 달성. 특히 기저 모델이 0-shot으로 해결 불가능한 문제까지 학습하여 높은 pass@k 값 달성

2. **이론적 보장**: Approximate Policy Iteration 프레임워크 내에서 E2H Reasoner의 수렴성을 증명하고, 적절하게 분해된 작업을 통한 커리큘럼 학습이 직접 학습보다 **적은 표본으로도 수렴** 가능함을 보였다 (finite-sample complexity bound 도출)

3. **일반화 능력**: 커리큘럼 학습을 통해 모델이 분포 내 난제뿐만 아니라 분포 외(OOD) 작업으로의 일반화 능력을 강화

## How

![Figure 3](figures/fig3.webp)
*코사인 기반 스케줄링 메커니즘 (Gaussian Sampler를 통한 동적 작업 비중 조정)*

**방법론의 핵심 요소:**

- **작업 분해 (Task Decomposition)**:
  - 인간 주석 활용: 계획 길이(Blocksworld), 라벨된 난이도(MATH), 피연산자 수(Countdown)
  - 자동 난이도 추정: CoT 프롬프팅 기반 오류율 쿼타일(quartile) 분류 (AQuA, GSM8K)
  - 총 4단계 난이도 레벨 설정

- **확률적 스케줄러 (Probabilistic Scheduler)**:
  - Gaussian Sampler를 통한 부드러운 확률 분포 전환
  - 코사인 함수 기반 스케줄링으로 학습 초기 쉬운 작업 강조 후 점진적 하강
  - 각 학습 스텝에서 작업 난이도를 샘플링하여 적응적 커리큘럼 구성

- **강화학습 포리티 최적화**:
  - MDP 형식화: 상태(토큰 프리픽스), 행동(어휘), 보상(정답 여부의 희소 신호)
  - <think></think>, <answer></answer> 태그로 추론 과정과 최종 답 구분
  - 기존 RL 알고리즘(GRPO 등)과 호환 가능한 설계

- **과적합 방지**:
  - 적절한 스케줄링을 통해 쉬운 작업을 점진적으로 페이드 아웃
  - 단순히 쉬운 작업에만 집중하지 않도록 동적 조정

## Originality

- **새로운 관점**: 추론을 "중간 단계 생성"이 아니라 **"기초 원리를 습득하여 복잡한 문제에 적용하는 일반화 능력"**으로 재정의하여 추론의 본질에 접근

- **개선된 커리큘럼 설계**: 기존의 고정된 반복(fixed iterations) 기반 전환이 아니라 **확률적 스케줄러(Gaussian Sampler)**를 통한 부드럽고 동적인 작업 비중 조정으로 차별화

- **이론적 기여**: Approximate Policy Iteration 프레임워크에서 CRL의 수렴성과 표본 복잡도 상한을 엄밀하게 증명하여 경험적 관찰을 이론으로 뒷받침

- **확장 가능한 난이도 추정**: 인간 주석이 없는 경우 CoT 기반 자동 난이도 추정으로 새로운 작업에 빠른 적용 가능

## Limitation & Further Study

- **작업 분해의 한계**: 난이도 분해가 휴리스틱(경험법칙)에 기반하며, 최적의 분해 방식이나 단계 수에 대한 이론적 지침이 부재. 다양한 도메인에 대한 보편적 분해 기준 부족

- **확장성 제약**: 현재 평가는 작은 규모 모델(1.5B~3B)과 제한된 작업 수에서 수행. 대규모 모델(10B 이상)과 더 다양한 추론 작업에 대한 검증 필요

- **스케줄링 하이퍼파라미터**: 코사인 스케줄러의 기울기, 가우시안 분포의 표준편차 등 하이퍼파라미터의 민감도 분석 및 자동 설정 방안 미제시

- **후속 연구 방향**:
  - 메타러닝(meta-learning) 기반 최적 커리큘럼 자동 설계
  - 다중 추론 도메인 간 전이학습(transfer learning) 효과 분석
  - 혼합 전략(hybrid approach): 단계별 보상 신호와 커리큘럼의 결합 효과 연구
  - 인간 피드백(RLHF) 통합으로 커리큘럼 학습의 안정성 개선

## Evaluation

| 항목 | 평점 |
|------|------|
| **Novelty (독창성)** | 4/5 |
| **Technical Soundness (기술적 타당성)** | 4.5/5 |
| **Significance (중요도)** | 4/5 |
| **Clarity (명확성)** | 4/5 |
| **Overall (종합)** | 4/5 |

**총평**: 본 논문은 LLM 추론 학습을 위해 커리큘럼 학습과 강화학습을 결합한 실질적으로 효과적인 방법을 제시하며, 이론적 수렴 보장과 실증적 우수성을 동시에 제공한다. 다만 난이도 분해의 자동화, 대규모 모델 검증, 하이퍼파라미터 민감도 분석 등의 보완이 있으면 영향력이 더욱 증대될 것으로 판단된다.

## Related Papers

- 🔄 다른 접근: [[papers/265_DeepSeek-R1_incentivizes_reasoning_in_LLMs_through_reinforce/review]] — DeepSeek-R1과 E2H Reasoner 모두 강화학습을 통해 LLM의 추론 능력을 향상시키지만 서로 다른 학습 전략을 사용한다.
- 🏛 기반 연구: [[papers/484_Learning_to_generate_research_idea_with_dynamic_control/review]] — 동적 제어를 통한 연구 아이디어 생성 학습은 쉬운 작업에서 어려운 작업으로의 점진적 학습 패러다임의 이론적 기반이다.
- 🔗 후속 연구: [[papers/625_PlanGenLLMs_A_Modern_Survey_of_LLM_Planning_Capabilities/review]] — LLM 계획 능력에 대한 현대적 조사는 E2H Reasoner의 커리큘럼 기반 계획 학습 접근방식을 더 넓은 맥락에서 이해할 수 있게 한다.
- 🏛 기반 연구: [[papers/395_Guided_by_guardrails_Control_barrier_functions_as_safety_ins/review]] — 쉬운 태스크에서 어려운 태스크로의 커리큘럼 강화학습은 제어 장벽 함수를 통한 안전 학습에 점진적 훈련 방법론을 제공한다.
- 🧪 응용 사례: [[papers/863_Value_iteration_for_learning_concurrently_executable_robotic/review]] — 커리큘럼 강화학습의 쉬운 태스크에서 어려운 태스크로의 점진적 학습은 동시 실행 태스크를 우선순위에 따라 순차적으로 학습하는 실제 구현 방법을 제시한다.
- 🔄 다른 접근: [[papers/140_Autonomous_reinforcement_learning_agent_for_chemical_vapor_d/review]] — 강화학습을 통한 과학적 과제 해결에서 단일 vs 다중 과제 학습의 다른 접근법을 비교할 수 있다
