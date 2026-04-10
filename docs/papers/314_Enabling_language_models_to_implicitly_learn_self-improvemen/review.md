---
title: "314_Enabling_language_models_to_implicitly_learn_self-improvemen"
authors:
  - "Ziqi Wang"
  - "Le Hou"
  - "Tianjian Lu"
  - "Yuexin Wu"
  - "Yunxuan Li"
date: "2023"
doi: ""
arxiv: ""
score: 4.2
essence: "본 논문은 대규모 언어모델(LLM)이 인간 선호도 데이터로부터 암묵적으로 자기 개선 목표를 학습할 수 있도록 하는 **PIT(ImPlicit Self-ImprovemenT)** 프레임워크를 제안한다. 기존 프롬프팅 기반 자기 개선 방법들과 달리, 명시적인 평가 기준(rubric) 설계 없이 보상 모델 학습에 사용되는 선호도 데이터만으로 응답 품질을 개선할 수 있다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Self-Refining_Text_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wang et al._2023_Enabling language models to implicitly learn self-improvement.pdf"
---

# Enabling language models to implicitly learn self-improvement

> **저자**: Ziqi Wang, Le Hou, Tianjian Lu, Yuexin Wu, Yunxuan Li, Hongkun Yu, Heng Ji | **날짜**: 2023 | **출판처**: ICLR 2024

---

## Essence

본 논문은 대규모 언어모델(LLM)이 인간 선호도 데이터로부터 암묵적으로 자기 개선 목표를 학습할 수 있도록 하는 **PIT(ImPlicit Self-ImprovemenT)** 프레임워크를 제안한다. 기존 프롬프팅 기반 자기 개선 방법들과 달리, 명시적인 평가 기준(rubric) 설계 없이 보상 모델 학습에 사용되는 선호도 데이터만으로 응답 품질을 개선할 수 있다.

## Motivation

- **Known**: 프롬프팅 기반 자기 개선 방법(Self-Refine 등)들이 효과적이고 효율적이며, 명시적 루브릭이 필요함. RLHF 기반 정렬 방법이 널리 사용 중임.

- **Gap**: 복잡한 실제 목표(더 도움이 되고 해롭지 않기 등)에 대해 포괄적인 평가 기준을 수동으로 작성하기 어렵고 비용이 높음. 도메인 전문 지식이 필요한 경우 확장 불가능함.

- **Why**: 응답 개선을 위한 명확한 지표를 수량화하기 어렵고, "더 도움이 되도록"이라는 모호한 지시는 응답 길이만 증가시켜 오히려 성능을 저하시킬 수 있음.

- **Approach**: 명시적 루브릭 설계에서 벗어나 데이터로부터 암묵적으로 자기 개선을 학습. 보상 모델 훈련용 선호도 데이터에 이미 개선 목표가 내재되어 있다는 직관을 활용. RLHF 훈련 목표를 재구성: 주어진 입력에 대한 응답 품질 최대화 → 참조 응답 조건에서 응답 품질 차이 최대화.

## Achievement

1. **프롬프팅 기반 방법 대비 우수한 성능**: 실제 데이터셋 2개와 합성 데이터셋 1개에 대한 평가에서 Self-Refine 등 프롬프팅 방법을 크게 능가함.

2. **추가 데이터 및 인적 노력 불필요**: 보상 모델 훈련에 사용되는 기존 선호도 데이터를 재활용하므로 새로운 인간 주석 필요 없음.

3. **도메인 일반성**: 루브릭 설계가 필요 없어 도메인 전문 지식이 필요한 분야에도 적용 가능.

## How

**방법론의 핵심 요소:**

- **입력 형식 변경**: 정책 모델은 입력 x에서 응답 생성, PIT는 입력 x와 참조 응답 y_ref에서 개선된 응답 생성

- **감독 학습(SFT) 재구성**: 
  - 정책 모델: L^SFT_P = -∑log M_P(y_w|x)
  - PIT: L^SFT_PIT = -∑log M_PIT(y_w|x, y_l) (더 나쁜 응답과 더 좋은 응답 모두 활용)

- **보상 모델 재설계**: 절대 보상이 아닌 응답 간 품질 차이(reward gap) 학습
  - 순서 제약: r^w,l_gap ≥ r^w,w_gap ≈ r^l,l_gap ≥ r^l,w_gap
  - 다중 쌍 관계를 고려한 손실 함수(식 2): 5개의 부등식 조건 모두 만족하도록 훈련

- **강화 학습(RL)**: 개선된 응답의 품질 차이를 최대화하는 정책 최적화
  - 기존: E[r(x, y)] 최대화 → PIT: E[r_gap(x, y_ref, y_PIT)] 최대화

- **반복 적용**: 개선된 응답을 새로운 참조 응답으로 사용하여 반복적 개선 가능

## Originality

- **새로운 관점**: RLHF 훈련 목표를 응답 절대 품질에서 상대적 품질 차이로 재구성하는 혁신적 아이디어

- **간단하고 우아한 설계**: 기존 선호도 데이터만 활용하여 추가 주석 필요 없음

- **이론적 정당성**: 보상 모델의 학습 목표가 순서 관계를 통해 명확하게 정의됨

- **확장성**: 임의의 RLHF 기반 정렬 방법과 결합 가능

## Limitation & Further Study

**제한사항:**

- 추가 선호도 데이터 없이 보상 모델용 선호도 데이터만으로 훈련하므로 다양한 개선 각도를 완전히 학습하기 어려울 수 있음

- PIT의 반복 적용이 수렴하는지, 반복 횟수의 최적값은 얼마인지 명확하지 않음

- 보상 모델의 품질에 크게 의존 (보상 모델이 부정확하면 성능 저하)

**후속 연구:**

- 다양한 RLHF 대안(DPO, PRO 등)과의 통합 시도

- 온라인 강화 학습을 통한 동적 개선 목표 학습

- 도메인별 특화된 개선 목표 학습 방법론 개발

## Evaluation

- **Novelty (독창성)**: 4.5/5 - RLHF 목표 재구성이라는 참신한 아이디어이나, 개념 자체는 상대적으로 직관적

- **Technical Soundness (기술적 건전성)**: 4/5 - 수학적 공식화가 명확하나, 보상 모델 손실 함수의 완전한 정당성에 대한 이론적 증명 부족

- **Significance (중요도)**: 4.5/5 - 실무에서 인적 노력 감소라는 실질적 가치가 있으나, 개념적 기여도는 중간 수준

- **Clarity (명확성)**: 4/5 - 전반적으로 명확하나 보상 모델 손실 함수 유도 과정이 다소 단순하게 설명됨

- **Overall**: 4.2/5

**총평**: PIT는 선호도 데이터로부터 암묵적으로 개선 목표를 학습한다는 우아한 아이디어와 추가 인적 노력 없이 기존 데이터를 재활용한다는 실용성으로 가치 있는 기여를 하지만, 이론적 정당성 강화와 보상 모델 의존성 완화 방안이 향후 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/746_Self-Refine_Iterative_Refinement_with_Self-Feedback/review]] — 둘 다 LLM의 자기개선을 다루지만 하나는 암묵적 학습, 다른 하나는 명시적 자기반성을 사용함
- 🏛 기반 연구: [[papers/470_Large_language_models_can_self-improve/review]] — LLM의 일반적인 자기개선 능력에 대한 기초 연구가 암묵적 자기개선 프레임워크 개발의 이론적 토대를 제공함
- 🔗 후속 연구: [[papers/314_Enabling_language_models_to_implicitly_learn_self-improvemen/review]] — 기본적인 자기개선을 인간 선호도 데이터를 활용한 더 정교한 암묵적 학습 방법으로 확장함
