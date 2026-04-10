---
title: "458_Language_agents_mirror_human_causal_reasoning_biases"
authors:
  - "Anthony GX-Chen"
  - "Dongyan Lin"
  - "Mandana Samiei"
  - "Doina Precup"
  - "Blake A. Richards"
date: "2025"
doi: "arXiv:2505.09614"
arxiv: ""
score: 4.25
essence: "언어 모델(LM) 에이전트는 인과관계 추론에서 선언적(disjunctive, OR) 규칙에는 능하지만 결합적(conjunctive, AND) 규칙에서 체계적으로 편향되어 있으며, 이러한 편향이 인간 성인의 인지 편향과 유사함을 보여주는 연구이다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Scientific_Agent_Frameworks"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/GX-Chen et al._2025_Language agents mirror human causal reasoning biases.pdf"
---

# Language agents mirror human causal reasoning biases

> **저자**: Anthony GX-Chen, Dongyan Lin, Mandana Samiei, Doina Precup, Blake A. Richards, Rob Fergus, Kenneth Marino | **날짜**: 2025 | **DOI**: [arXiv:2505.09614](https://arxiv.org/abs/2505.09614)

---

## Essence

![Figure 1: The Blicket Test](figures/fig1.webp) 
*언어 모델이 객체를 기계에 올려놓는 상호작용을 통해 인과관계를 파악해야 하는 블리켓 테스트*

언어 모델(LM) 에이전트는 인과관계 추론에서 선언적(disjunctive, OR) 규칙에는 능하지만 결합적(conjunctive, AND) 규칙에서 체계적으로 편향되어 있으며, 이러한 편향이 인간 성인의 인지 편향과 유사함을 보여주는 연구이다.

## Motivation

- **Known**: 언어 모델은 자연언어 처리와 로봇 제어 등에서 뛰어난 성능을 보이고 있으며, LM 에이전트는 항생제 설계, 학술지 논문 작성 등 실무적 적용이 확대되고 있음
- **Gap**: LM 에이전트가 인과관계(causal relationships)를 효율적으로 탐색하고 추론할 수 있는지, 그리고 체계적 편향을 갖고 있는지 불명확함. 특히 인간 훈련 데이터로부터 학습한 LM이 인간의 인지 편향을 상속받았는지 알려지지 않음
- **Why**: 자율 의사결정 에이전트는 과학적으로 견고한 인과추론 능력이 필수적이나, 심리학 연구에서 인간도 특정 상황에서 체계적으로 비합리적임이 알려져 있음
- **Approach**: 발달심리학의 블리켓 테스트(Blicket Test) 패러다임을 텍스트 기반 게임으로 적응시켜, 다양한 LM들의 인과추론 능력과 편향을 측정하고 인간 데이터와 비교

## Achievement

![Figure 2: Quiz accuracy of various models](figures/fig1.webp)
*다양한 언어 모델들의 선언적/결합적 규칙에서의 정확도: 모든 모델이 결합적 규칙에서 체계적으로 낮은 성능 보임*

1. **선언적 편향 발견**: 모든 LM 모델군(GPT-4o, DeepSeek, Gemma 등)이 결합적 규칙보다 선언적 규칙에서 신뢰성 높게 더 나은 성능을 보임. 이는 옳은 탐색 데이터가 주어져도 나타나는 현상으로, 순수한 탐색 비효율의 문제가 아님

2. **인간과 유사한 편향 패턴**: LM의 추론 프로필이 인간 성인의 패턴과 유사하지만 유아/어린이의 패턴(편향 없는 "요람 속의 과학자")과는 다름을 정량적으로 입증

3. **복합 인과요인**: 정보 이득(information gain)과 정확도 간 강한 상관관계(ρ=0.76)를 발견했으나, 동일한 정보 수집 후에도 모델이 결합적 가설을 제거하지 못함

4. **확장성 있는 개선방법**: 테스트 타임 샘플링을 통해 명시적으로 인과 가설을 샘플링하고 제거하도록 프롬프팅하면 선언적 편향이 유의미하게 감소

## How

![Figure 3: Correlation analysis](figures/fig1.webp)
*모델 성능에 영향을 미치는 요소들: 정보 이득이 가장 강한 양의 상관(ρ=0.76), 탐색 단계 수는 음의 상관(ρ=-0.35)*

- **텍스트 기반 블리켓 테스트**: 에이전트는 순차적으로 객체를 기계에 올렸다 내렸다 하면서 상태 변화를 관찰하고, 탐색 단계 이후 모든 관찰 이력을 제공받아 각 객체의 블리켓 여부를 판단
- **정보이득 측정**: Shannon 엔트로피 기반 기댓값 정보이득(expected information gain)을 계산하여 최적 탐색 행동 정의. 오라클 에이전트는 한 단계 정보 최대화로 상한선 제시
- **다양한 모델 평가**: GPT-4o, DeepSeek-Reasoner/Chat, Gemma 3, QWQ 등 여러 모델군 및 시스템 메시지, CoT/ReAct/Reflexion 같은 프롬프팅 기법으로 로버스트 검증
- **가설 제거 방법(Hypothesis Elimination)**: 명시적으로 가능한 인과 가설들의 평면적 사전분포(flat prior)를 구성하고, 각 가설을 의도적으로 제거하도록 유도하는 테스트-타임 절차

## Originality

- 발달심리학 패러다임(블리켓 테스트)을 LM 에이전트 평가에 처음 적용하여, 인공지능의 인과추론 편향을 체계적으로 측정
- 인간 성인과 LM 간의 정량적 비교를 통해 "모델이 훈련 데이터의 인간 편향을 상속한다"는 가설을 실증적으로 검증
- 선언적 편향이 탐색 전략 부족이 아닌 근본적 추론 편향임을 보여줌으로써, 단순한 프롬프팅 개선을 넘어 인과추론의 본질적 문제를 지적
- 정보이득 최적화와 실제 모델 성능 간의 간극을 측정하고, 이를 해결하는 가설 제거 기반의 구성적 방법 제시

## Limitation & Further Study

- **태스크 단순성**: 블리켓 테스트는 제한된 인과구조(2가지 규칙만)만 다루며, 현실의 복잡한 인과 관계(시간적 지연, 숨겨진 변수, 다중 상호작용 등)는 포함하지 않음
- **프롬프트 의존성**: 다양한 시스템 메시지와 프롬프팅 기법을 시도했으나, 개별 최적화된 프롬프트에 대한 "금은 총알(silver bullet)" 존재 여부는 미해결
- **확장성 검증**: 제안된 가설 제거 방법이 더 복잡한 인과 구조와 더 많은 객체(>8)에서 어느 정도로 스케일되는지 실험이 제한적
- **인간 비교의 깊이**: 성인과 유아 간 성능 비교는 데이터 수준이지만, 선언적 편향의 심리학적 근원(예: 언어 구조, 선험적 개념 등)에 대한 이론적 분석 부재
- **인과 발견 일반화**: 블리켓 테스트 외 다른 인과 추론 패러다임(예: 중재 실험, 관측 데이터 분석)에서 유사한 편향이 나타나는지 미검증

## Evaluation

| 평가 항목 | 점수 |
|---------|------|
| **Novelty** (독창성) | 4.5/5 |
| **Technical Soundness** (기술 건전성) | 4/5 |
| **Significance** (중요성) | 4.5/5 |
| **Clarity** (명확성) | 4/5 |
| **Overall** (종합) | 4.25/5 |

**총평**: 본 논문은 언어 모델의 인과추론 편향을 심리학 패러다임과 연계하여 처음으로 체계적으로 규명하였으며, 인간 행동과의 정량적 비교를 통해 모델이 훈련 데이터의 인지 편향을 상속함을 실증했다. 제안된 가설 제거 방법은 이론적 근거가 명확하고 성능 개선이 유의미하나, 더 복잡한 인과 구조와 다양한 추론 시나리오로의 확장 가능성 검증이 필요하다. 자율 에이전트의 과학적 추론 능력 강화라는 중요한 문제를 다루는 높은 수준의 연구이다.

## Related Papers

- 🧪 응용 사례: [[papers/360_From_lived_experience_to_insight_Unpacking_the_psychological/review]] — 인과관계 추론에서 언어 에이전트의 인간 유사 편향을 AI 시스템의 심리적 위험 분석에 적용할 수 있다
- 🔗 후속 연구: [[papers/191_Causal_learning_for_socially_responsible_ai/review]] — 사회적 책임 AI를 위한 인과 학습을 언어 에이전트의 인지 편향 연구로 확장할 수 있다
- 🏛 기반 연구: [[papers/173_Bridging_social_psychology_and_llm_reasoning_Conflict-aware/review]] — 사회 심리학과 LLM 추론의 연결이 언어 에이전트 편향 연구의 이론적 기반을 제공한다
- 🏛 기반 연구: [[papers/360_From_lived_experience_to_insight_Unpacking_the_psychological/review]] — 언어 에이전트의 인간과 유사한 인지 편향 연구가 AI의 심리적 위험 분석에 이론적 기반을 제공한다
