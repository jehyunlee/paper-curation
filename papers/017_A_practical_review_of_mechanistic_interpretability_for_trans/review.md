---
title: "017_A_practical_review_of_mechanistic_interpretability_for_trans"
authors:
  - "Daking Rai"
  - "Yilun Zhou"
  - "Shi Feng"
  - "Abulhair Saparov"
  - "Ziyu Yao"
date: "2024"
doi: ""
arxiv: ""
score: 4.0
essence: "트랜스포머 기반 언어모델의 내부 계산을 역공학하여 이해하는 기계적 해석가능성(Mechanistic Interpretability, MI)에 대한 종합 리뷰로, 초보자를 위한 실무 가이드를 제시한다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/Cognitive_LLM_Evaluation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Rai et al._2024_A practical review of mechanistic interpretability for transformer-based language models.pdf"
---

# A practical review of mechanistic interpretability for transformer-based language models

> **저자**: Daking Rai, Yilun Zhou, Shi Feng, Abulhair Saparov, Ziyu Yao | **날짜**: 2024 | **URL**: [https://arxiv.org/abs/2407.02646](https://arxiv.org/abs/2407.02646)

---

## Essence

![Figure 3](figures/fig3.webp)

*Figure 3: Beginner’s roadmap to MI, designed to help newcomers quickly pick up the field. The MI study is*

트랜스포머 기반 언어모델의 내부 계산을 역공학하여 이해하는 기계적 해석가능성(Mechanistic Interpretability, MI)에 대한 종합 리뷰로, 초보자를 위한 실무 가이드를 제시한다.

## Motivation

- **Known**: 트랜스포머 기반 언어모델이 NLP 분야에서 뛰어난 성능을 보이고 있으나, 안전성과 신뢰성에 대한 우려가 증대되고 있다. 기존 해석가능성 연구는 모델의 행동을 설명하는 데 제한적이었다.
- **Gap**: MI 분야의 빠른 성장에도 불구하고 초보자를 위한 포괄적 가이드가 부족하며, 다양한 기법과 평가 방법, 그리고 실제 응용 사례를 체계적으로 정리한 자료가 없었다. MI의 확장성과 일반화 가능성에 대한 우려도 존재한다.
- **Why**: 언어모델의 안전성, 신뢰성, 강건성을 보장하기 위해서는 내부 계산 메커니즘을 정확히 이해해야 하며, 이는 AI 안전과 모델 개선에 직결되는 중요한 문제이다.
- **Approach**: 작업 중심 분류체계(task-centric taxonomy)를 통해 기능(Feature) 연구, 회로(Circuit) 연구, 범용성(Universality) 연구로 구분하고, 각 카테고리별 기법, 평가 방법, 주요 발견을 체계적으로 정리한다.

## Achievement


- **MI 기본 개념 정립**: 기능, 회로, 범용성이라는 MI의 세 가지 기본 연구 대상을 명확히 정의
- **초보자 로드맵 제시**: 특정 기능 연구부터 개방형 기능 연구, 회로 연구, 범용성 연구로 이어지는 단계별 워크플로우 제공
- **기법 비교 분석**: 어휘 투영법(Vocabulary Projection), 개입 기반 방법(Intervention-based Methods), 희소 자동인코더(Sparse Autoencoder, SAE), 탐사(Probing), 시각화 등 5가지 주요 기법의 장단점 상세 분석
- **평가 방법론 체계화**: 기능 연구와 회로 연구를 위한 평가 벤치마크 정리 및 제시
- **실제 응용 사례**: 모델 강화, AI 안전, 인문맥 학습(In-Context Learning), 추론, 지식 메커니즘 등 다양한 응용 분야의 구체적 사례 제시
- **학습 동역학 분석**: 모델 학습 중 위상 변화와 사후 학습(post-training) 효과에 대한 MI 관점의 분석

## How

![Figure 4](figures/fig4.webp)

*Figure 4: Logit lens implementation at (1) RS, (2) attention head, and (3) FF sublayer.*

- 트랜스포머 아키텍처의 배경 지식 제공 (뉘런, 주의 헤드, 피드포워드 층)
- 어휘 투영법: 뉘런/헤드 활성화를 어휘 공간에 투영하여 해석 (로짓 렌즈, 주의 패턴 분석)
- 개입 기반 방법: 노이징(Noising), 제거(Ablation), 패치(Patching) 등을 통한 인과관계 추론
- 희소 자동인코더: 활성화를 희소한 기저(sparse basis)로 분해하여 해석 가능한 기능 추출
- 탐사(Probing): 선형/비선형 분류기를 이용한 숨겨진 표현의 정보 검출
- 시각화: 주의 패턴, 활성화 분포 등을 시각적으로 표현
- 사례 연구: 프로빙을 이용한 목표 기능 연구와 SAE를 이용한 개방형 기능 연구 사례 제시

## Originality

- 작업 중심 분류체계는 기존의 기법 중심 관점에서 벗어나 문제 정의 단계부터 실제 구현까지의 전체 프로세스를 다룸
- 초보자 로드맵은 이론과 실제 연구의 간극을 메우기 위해 체계적인 워크플로우와 구체적 사례를 결합
- 다양한 MI 기법 간 비교 분석을 통해 각 접근법의 적용 상황과 한계를 명확히 함
- MI의 실제 응용을 단순한 나열이 아닌 구체적 성과와 영향으로 정리

## Limitation & Further Study

- **확장성 제약**: 더 큰 모델과 복잡한 작업으로의 MI 기법 확장 가능성에 대한 검증 부족
- **일반화 문제**: 특정 모델이나 작업에서 발견된 기능과 회로의 다른 모델/작업으로의 전이 가능성 미검증
- **평가 표준화 부재**: MI 기법의 평가를 위한 통일된 벤치마크와 메트릭이 아직 확립되지 않음
- **자동화 부재**: 가설 생성과 해석 프로세스의 자동화 부족으로 인한 수동 작업 의존
- **후속 연구 방향**: (1) 더 직관적이고 실용적인 응용으로의 확대, (2) 인간-AI 협업을 중심으로 한 새로운 패러다임 개발, (3) MI 기법의 계산 효율성 개선

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 이 논문은 빠르게 성장하는 MI 분야에서 초보자부터 경험자까지 모두를 위한 실용적이고 포괄적인 가이드를 제공하며, 작업 중심의 분류체계와 구체적 워크플로우를 통해 해석가능성 연구의 새로운 표준을 제시한다. 현장 적용을 위한 실제 고려사항과 미래 방향을 함께 제시한 점에서 높은 가치를 지닌다.

## Related Papers

- 🔄 다른 접근: [[papers/527_Mechanistic_interpretability_for_ai_safetya_review/review]] — AI 안전을 위한 기계적 해석가능성 리뷰와 트랜스포머 기반 모델의 기계적 해석가능성은 상호 보완적인 관점에서 AI 이해가능성을 다룹니다
- 🏛 기반 연구: [[papers/846_TrustLLM_Trustworthiness_in_Large_Language_Models/review]] — 대형 언어모델의 신뢰성 평가는 기계적 해석가능성을 통한 모델 내부 이해의 궁극적인 목표와 평가 기준을 제공합니다
- 🔗 후속 연구: [[papers/836_Towards_uncovering_how_large_language_model_works_An_explain/review]] — 대형 언어모델 작동 방식의 설명가능한 연구는 기계적 해석가능성의 실무 가이드를 더욱 심화된 연구 방향으로 확장합니다
- 🔗 후속 연구: [[papers/527_Mechanistic_interpretability_for_ai_safetya_review/review]] — 트랜스포머 모델의 기계론적 해석가능성 연구를 AI 안전성 맥락으로 확장한다
- 🔗 후속 연구: [[papers/582_On_gradient-like_explanation_under_a_black-box_setting_when/review]] — 트랜스포머의 기계적 해석가능성 실용적 검토를 블랙박스 설정의 그래디언트 유사 설명으로 확장할 수 있다.
