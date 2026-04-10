---
title: "683_RM-R1_Reward_Modeling_as_Reasoning"
authors:
  - "Xiusi Chen"
  - "Gaotang Li"
  - "Ziqi Wang"
  - "Bowen Jin"
  - "Cheng Qian"
date: "2025"
doi: "10.48550/arXiv.2505.02387"
arxiv: ""
score: 4.4
essence: "보상 모델(Reward Model, RM)에 추론 능력을 통합함으로써 해석 가능성과 성능을 모두 향상시킨 새로운 클래스의 생성형 보상 모델인 RM-R1을 제시한다. Chain-of-Rubrics(CoR) 메커니즘을 통해 작업 특성에 맞춘 맞춤형 추론 전략을 적용하여 70B, 340B 모델과 GPT-4o를 최대 4.9% 능가한다."
tags:
  - "cat/Reinforcement_Learning_and_Self-Verification"
  - "sub/Reasoning_Enhancement_via_Reinforcement_Learning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Chen et al._2025_RM-R1 Reward Modeling as Reasoning.pdf"
---

# RM-R1: Reward Modeling as Reasoning

> **저자**: Xiusi Chen, Gaotang Li, Ziqi Wang, Bowen Jin, Cheng Qian | **날짜**: 2025 | **DOI**: [10.48550/arXiv.2505.02387](https://doi.org/10.48550/arXiv.2505.02387)

---

## Essence

보상 모델(Reward Model, RM)에 추론 능력을 통합함으로써 해석 가능성과 성능을 모두 향상시킨 새로운 클래스의 생성형 보상 모델인 RM-R1을 제시한다. Chain-of-Rubrics(CoR) 메커니즘을 통해 작업 특성에 맞춘 맞춤형 추론 전략을 적용하여 70B, 340B 모델과 GPT-4o를 최대 4.9% 능가한다.

## Motivation

- **Known**: 기존 보상 모델은 스칼라 기반(ScalarRM)과 생성형(GenRM) 두 가지로 분류됨. 스칼라 기반은 효율적이지만 불투명하고, 생성형은 투명하지만 표면적 추론만 수행하여 성능이 제한됨
  
- **Gap**: 현실의 복잡한 선호도 판단은 공감, 다중 기준 간 트레이드오프 네비게이션, 결과 시뮬레이션 등 다층적 인지 활동을 요구하나, 기존 GenRM은 이를 충분히 수행하지 못함

- **Why**: Figure 1의 예시처럼 오프더셸프 명령 튜닝 모델은 감독 데이터의 패턴에 과적합되어 정서적 해로움과 뉘앙스 부족을 감지하지 못함

- **Approach**: 보상 모델링을 추론 작업으로 공식화하고, (1) 추론 증류(reasoning distillation)와 (2) 검증 가능한 보상을 통한 강화학습(RLVR)의 두 단계 파이프라인으로 RM-R1을 훈련

## Achievement

![Figure 2](figures/fig2.webp)
*RM-R1의 훈련 파이프라인: 증류 단계에서 고품질 합성 데이터로 추론 능력을 부트스트랩하고, RL 단계에서 추가로 강화*

1. **벤치마크 성능**: RewardBench, RM-Bench, RMB 세 가지 벤치마크에서 평균적으로 최고 성능 달성. 70B/340B 오픈웨이트 모델, GPT-4o, Claude 모델을 최대 4.9% 능가

2. **해석 가능성**: RM-R1은 일관되고 고도로 해석 가능한 추론 궤적(reasoning traces)을 생성하여 "왜 이 응답이 더 나은가"를 명확히 설명

3. **스케일링 효율**: 7B에서 32B까지의 모델 패밀리에서 일관된 성능 향상을 보여 스케일 효율성 입증

## How

- **Chain-of-Rubrics (CoR) 메커니즘**: 입력 샘플을 대화(chat) 또는 추론(reasoning) 작업으로 분류
  - *대화 작업*: 평가 루브릭 생성 → 루브릭 정당화 → 특정 질문에 맞춘 평가 수행
  - *추론 작업*: 모델이 먼저 문제를 직접 해결한 후 후보 응답 평가 및 선택

- **2단계 훈련 파이프라인**:
  1. **추론 증류(Eq. 6)**: o3 또는 Claude-3.5-Sonnet 같은 오라클 모델에서 고품질 추론 체인 생성. NLL 손실로 구조화된 추론 트레이스와 응답 선택을 함께 최적화
  2. **강화학습(Eq. 7)**: 검증 가능한 보상 함수 $R(x, j)$로 모델을 정책처럼 취급하여, 올바른 판단을 생성하도록 KL 발산 제약 하에서 누적 보상 최대화

- **작업 인식 적응(Task-aware Adaptation)**: 대화와 추론 작업에 맞춘 차별화된 롤아웃 전략으로 보상 신호 정렬성 향상

- **기존 추론 모델 활용**: 이미 추론 중심 증류를 거친 모델(예: o1)에서 추론 증류 없이 RLVR만으로 바로 미세조정 가능

## Originality

- **개념적 창신성**: 보상 모델링 자체를 추론 작업으로 재정의하는 관점의 전환. 기존 GenRM은 투명성만 추구했으나, REASRM은 투명성과 정확성을 동시에 달성

- **Chain-of-Rubrics 방식**: 고정된 프롬프트 기반이 아닌, 작업 특성을 자동 인식하여 동적으로 추론 전략을 조정하는 메커니즘의 참신함

- **훈련 방법론**: 추론 증류와 RLVR의 조합으로 순수 RLVR만으로는 달성 못하는 추론 능력과 일반화 능력의 균형. 논문에서 순수 RL만으로는 추론 능력이 제한됨을 실증적으로 입증

- **체계적 경험적 분석**: 여러 훈련 레시피의 영향을 비교 분석하고, 스케일링 효과, 비추론 기반선과의 비교 등 다각적 분석 제공

## Limitation & Further Study

- **데이터 생성 비용**: 고품질 추론 체인 생성을 위해 o3나 Claude-3.5-Sonnet 같은 강력한 오라클 모델 필요로, 스케일링 시 계산 비용 및 경제성 우려

- **작업 분류의 한계**: 대화와 추론 이진 분류가 실제 작업의 연속적 복잡도 스펙트럼을 충분히 포착하지 못할 가능성

- **강화학습 최적화**: 보상 함수 $R(x, j)$ 설계의 상세 사항이 제한적으로 기술됨. 검증 가능한 보상의 구체적 정의와 확장성에 대한 추가 연구 필요

- **후속 연구 방향**:
  - 더 세분화된 작업 분류 체계 개발
  - 다중 오라클 모델 활용 및 합성 데이터 품질 개선
  - 다른 도메인(코드, 과학 등)으로의 확장 및 일반화 가능성 검증


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4.5/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.4/5

**총평**: 보상 모델링을 추론 작업으로 재정의하는 핵심 아이디어와 Chain-of-Rubrics의 작업 인식 메커니즘이 혁신적이며, 실증적 성과(최대 4.9% 성능 향상)와 체계적 분석을 통해 실질적 기여를 입증한 우수한 연구이다. 다만 오라클 모델 의존성과 작업 분류의 이진 구조는 실무 확장성 측면에서 개선 여지가 있다.

## Related Papers

- 🔄 다른 접근: [[papers/845_Trust_But_Verify_A_Self-Verification_Approach_to_Reinforceme/review]] — 두 논문 모두 보상 모델의 검증 능력을 다루되 RM-R1은 추론 통합, RISE는 자기검증 학습에 초점을 맞춘다.
- 🏛 기반 연구: [[papers/598_PAG_Multi-Turn_Reinforced_LLM_Self-Correction_with_Policy_as/review]] — PAG의 다중 턴 자기 수정 프레임워크는 RM-R1의 Chain-of-Rubrics 메커니즘 설계에 이론적 기반을 제공한다.
- 🔗 후속 연구: [[papers/322_Evaluation_of_openai_o1_Opportunities_and_challenges_of_agi/review]] — OpenAI o1의 추론 능력 평가는 RM-R1의 생성형 보상 모델이 실제로 달성할 수 있는 성능 상한을 보여준다.
- 🔗 후속 연구: [[papers/845_Trust_But_Verify_A_Self-Verification_Approach_to_Reinforceme/review]] — RM-R1의 추론 능력을 통합한 보상 모델링은 RISE의 검증 가능한 보상 시스템에 더 정교한 평가 메커니즘을 제공한다.
