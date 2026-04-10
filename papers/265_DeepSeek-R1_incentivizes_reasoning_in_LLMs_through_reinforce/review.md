---
title: "265_DeepSeek-R1_incentivizes_reasoning_in_LLMs_through_reinforce"
authors:
  - "DeepSeek-AI"
  - "Daya Guo"
  - "Dejian Yang"
  - "Haowei Zhang"
  - "Jun-Mei Song"
date: "2025"
doi: "10.1038/s41586-025-09422-z"
arxiv: ""
score: 4.75
essence: "본 논문은 인간이 주석을 단 추론 궤적(reasoning trajectory) 없이 순수 강화학습(RL)을 통해 대형언어모델(LLM)의 추론 능력을 유도할 수 있음을 보여준다. RL 훈련 과정에서 모델은 자발적으로 자기 검증, 재검토, 동적 전략 적응 등의 고급 추론 패턴을 개발한다."
tags:
  - "cat/Reinforcement_Learning_and_Self-Verification"
  - "sub/Reasoning_Enhancement_via_Reinforcement_Learning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/DeepSeek-AI et al._2025_DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning.pdf"
---

# DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning

> **저자**: DeepSeek-AI, Daya Guo, Dejian Yang, Haowei Zhang, Jun-Mei Song | **날짜**: 2025 | **DOI**: [10.1038/s41586-025-09422-z](https://doi.org/10.1038/s41586-025-09422-z)

---

## Essence

![Figure 1](figures/fig1.webp)
*Figure 1: (a) RL 훈련 과정에서 DeepSeek-R1-Zero의 AIME 정확도. (b) RL 프로세스 중 응답의 평균 길이 증가.*

본 논문은 인간이 주석을 단 추론 궤적(reasoning trajectory) 없이 순수 강화학습(RL)을 통해 대형언어모델(LLM)의 추론 능력을 유도할 수 있음을 보여준다. RL 훈련 과정에서 모델은 자발적으로 자기 검증, 재검토, 동적 전략 적응 등의 고급 추론 패턴을 개발한다.

## Motivation

- **Known**: 최근 LLM과 연쇄-생각-프롬프팅(Chain-of-Thought, CoT)은 기초 추론 작업에서 상당한 성공을 거두었으나, 이는 광범위한 인간 주석 데이터에 크게 의존함
- **Gap**: 기존 감독 학습(supervised learning) 방식은 인간 시연에 의존하므로 확장성이 제한되고, 모델의 성능이 인간의 사고 과정 수준으로 상한선이 정해짐
- **Why**: 인간이 고안한 추론 패턴에 제약을 받으면 모델의 탐색 범위가 제한되어 인간보다 우수한 추론 경로를 발견할 수 없음
- **Approach**: DeepSeek-V3-Base에 기반하여 Group Relative Policy Optimization (GRPO)을 사용한 순수 RL 훈련을 수행하되, SFT 단계를 건너뛰고 최종 예측의 정확성만을 보상 신호로 사용

## Achievement

![Figure 1a](figures/fig1.webp)
*AIME 2024 벤치마크에서 Pass@1 15.6%에서 77.9%로, Self-consistency 적용 시 86.7%까지 달성*

1. **수학 문제 해결**: AIME 2024에서 Pass@1 기준 77.9%, Self-consistency 적용 시 86.7% 정확도 달성 (인간 평균 수준 초과)

2. **코딩 경쟁 및 STEM 분야 우수성**: 코딩 경쟁(coding competitions) 및 대학원 수준의 생물, 물리, 화학 문제에서 탁월한 성능 입증

3. **자발적 추론 능력 발전**: 외부 제약 없이 자동으로 사고 시간 증가(Figure 1b, 수백에서 수천 토큰), 검증과 재검토 등의 고급 추론 전략 독립적 개발

4. **모델 증류(Distillation)**: 소형 모델로 증류된 버전들도 원래의 명령어 조정(instruction-tuned) 모델을 능가하는 추론 능력 보유

## How

![Figure 5](figures/fig5.webp)
*RL 프레임워크 개요*

- **Group Relative Policy Optimization (GRPO)**: PPO(Proximal Policy Optimization)의 단순화 버전으로, 각 질문에 대해 16개 출력을 샘플링한 후 정책 목적함수 최대화 (식 1-3 참고)

- **보상 설계**: 규칙 기반 보상 시스템 활용
  - 정확도 보상: 수학 문제는 지정된 형식의 최종 답변 검증, 코드는 컴파일러 기반 테스트 케이스 검증
  - 형식 보상: `<think>...</think>` 태그 내에 추론 과정 명시 강제

- **템플릿 최소화**: 추론 과정과 최종 답변을 순차적으로 생성하도록 하는 구조만 규정하고, 내용에 대한 편향은 제거

- **훈련 설정**: 
  - 총 10,400 스텝(1.6 에포크), 각 스텝당 32개 질문
  - 배치 크기 512, 샘플 온도 1.0
  - 8.2k 스텝에서 최대 토큰 길이 32,768에서 65,536으로 증가
  - 400 스텝마다 참조 모델을 최신 정책 모델로 교체

- **신경망 보상 모형 회피**: 대규모 RL에서 보상 해킹(reward hacking) 위험과 재훈련 비용 때문에 의도적으로 규칙 기반 보상만 사용

## Originality

- **SFT 단계 제거**: 기존의 감독 학습 → RL 파이프라인에서 SFT를 건너뛴 최초의 대규모 실험으로, 인간 편향 제거와 모델 자발적 탐색을 가능케 함

- **순수 RL 기반 추론 능력 유도**: 인간 주석 추론 궤적 없이도 고급 추론 패턴(자기 검증, 재검토, "wait" 사용 증가 등)의 자동 발현 입증

- **"아하 순간(Aha Moment)" 발견**: 훈련 중 "wait"의 사용 급증이라는 뚜렷한 행동 변화로 RL의 자기 진화 프로세스를 정성적으로 보여줌

- **GRPO의 대규모 적용**: 가치 모형을 제거하여 PPO보다 효율적인 알고리즘을 대규모 추론 작업에 성공적으로 적용

## Limitation & Further Study

- **DeepSeek-R1-Zero의 제한성**: 
  - 가독성 부족 및 언어 혼합(동일 응답에서 영어와 중국어 혼용)
  - 규칙 기반 RL이 추론 작업에만 집중되어 작문, 개방형 질문 답변 등 광범위한 작업에서 성능 부족

- **보상 설계의 확장성**: 현재 규칙 기반 보상은 수학, 코딩 등 검증 가능한 작업에만 적용 가능하며, 개방형 또는 주관적 평가가 필요한 작업으로의 확장 방안이 명확하지 않음

- **후속 연구 방향**:
  - 다단계 학습 파이프라인(거부 샘플링 + RL + SFT)을 통한 DeepSeek-R1 개발으로 일반화 능력 개선 필요
  - 신경망 기반 보상 모형의 안정성 개선으로 대규모 RL에서의 신뢰성 향상
  - 소형 모델에 대한 증류 방법론의 체계화


## Evaluation

- Novelty: 5/5
- Technical Soundness: 5/5
- Significance: 5/5
- Clarity: 4/5
- Overall: 4.75/5

**총평**: 본 논문은 LLM의 추론 능력 발전에 있어 인간 주석의 필요성을 근본적으로 재검토하며, 순수 RL만으로 고급 추론 패턴의 자발적 발현을 입증한 혁신적 연구이다. AIME에서 인간 수준을 초과하는 성능 달성과 함께 모델의 자기 진화 과정을 명확히 보여주는 점이 높이 평가되나, 개방형 작업으로의 확장과 신경망 보상 모형의 안정화가 향후 과제로 남아있다.

## Related Papers

- 🔄 다른 접근: [[papers/449_Kimi_k15_Scaling_reinforcement_learning_with_llms/review]] — 두 논문 모두 강화학습으로 LLM의 추론 능력을 향상시키되 DeepSeek-R1은 순수 RL, Kimi k1.5는 긴 맥락과 정책 최적화를 강조한다.
- 🔗 후속 연구: [[papers/243_Critique-GRPO_Advancing_LLM_Reasoning_with_Natural_Language/review]] — 자연언어 비판을 통합한 Critique-GRPO는 DeepSeek-R1의 순수 RL 접근법에 추가적인 언어적 피드백 메커니즘을 제공한다.
- 🧪 응용 사례: [[papers/795_The_AI_Scientist_Towards_Fully_Automated_Open-Ended_Scientif/review]] — DeepSeek-R1의 자기 검증 능력은 AI Scientist의 완전 자동화된 과학 발견에서 핵심적인 추론 검증 모듈로 활용될 수 있다.
- 🔗 후속 연구: [[papers/750_SEVerA_Verified_Synthesis_of_Self-Evolving_Agents/review]] — 강화학습 기반 추론이 형식적 검증과 결합되어 더 안전한 자기 진화 에이전트 구현 가능
- 🔄 다른 접근: [[papers/449_Kimi_k15_Scaling_reinforcement_learning_with_llms/review]] — 두 논문 모두 강화학습으로 LLM 추론을 향상시키되 Kimi k1.5는 긴 맥락 확장, DeepSeek-R1은 순수 RL에 중점을 둔다.
- 🏛 기반 연구: [[papers/243_Critique-GRPO_Advancing_LLM_Reasoning_with_Natural_Language/review]] — DeepSeek-R1의 순수 강화학습 기반 추론 능력은 Critique-GRPO의 자연언어 비판과 수치 보상 통합에 기본적인 RL 토대를 제공한다.
- 🔗 후속 연구: [[papers/833_Towards_reasoning_era_A_survey_of_long_chain-of-thought_for/review]] — 강화학습을 통한 추론 장려가 Long CoT 특성 향상에 어떻게 기여하는지 확장 연구를 제공한다
- 🔗 후속 연구: [[papers/674_ReTool_Reinforcement_Learning_for_Strategic_Tool_Use_in_LLMs/review]] — DeepSeek-R1의 강화학습을 통한 추론 인센티브화가 ReTool의 전략적 도구 사용 학습을 더 광범위한 추론 능력으로 확장한 발전 형태이다.
- 🔄 다른 접근: [[papers/249_Curriculum_Reinforcement_Learning_from_Easy_to_Hard_Tasks_Im/review]] — DeepSeek-R1과 E2H Reasoner 모두 강화학습을 통해 LLM의 추론 능력을 향상시키지만 서로 다른 학습 전략을 사용한다.
- 🔄 다른 접근: [[papers/585_Openai_o1_system_card/review]] — DeepSeek-R1과 OpenAI o1 모두 강화학습을 통한 추론 능력 향상을 추구하지만 서로 다른 훈련 방법론과 안전성 접근을 사용한다.
- 🧪 응용 사례: [[papers/751_SFT_Memorizes_RL_Generalizes_A_Comparative_Study_of_Foundati/review]] — DeepSeek-R1의 강화학습 기반 추론이 일반화 능력 향상에 미치는 영향 분석에 적용
- 🔗 후속 연구: [[papers/1100_Representative_Informative_and_De-Amplifying_Requirements_fo/review]] — 강화학습 기반 추론 모델의 신뢰성을 베이지안 최적실험설계로 향상시킨 확장
