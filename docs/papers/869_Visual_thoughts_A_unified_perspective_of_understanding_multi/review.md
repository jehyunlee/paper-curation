---
title: "869_Visual_thoughts_A_unified_perspective_of_understanding_multi"
authors:
  - "Zihui Cheng"
  - "Qiguang Chen"
  - "Xiao Xu 외"
date: "2025"
doi: "arXiv:2505.15510"
arxiv: ""
score: 4.2
essence: "대규모 비전-언어 모델(LVLM)의 멀티모달 체인-오브-쏘트(MCoT) 추론에서 **시각적 사고(Visual Thoughts)**라는 통합된 메커니즘을 발견하였으며, 이는 텍스트 기반과 이미지 교차 방식의 MCoT 모두를 설명하는 새로운 관점을 제시한다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Visual_Scientific_Reasoning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Mitchell et al._2025_Visual thoughts A unified perspective of understanding multimodal chain-of-thought.pdf"
---

# Visual thoughts: A unified perspective of understanding multimodal chain-of-thought

> **저자**: Zihui Cheng, Qiguang Chen, Xiao Xu 외 | **날짜**: 2025 | **DOI**: [arXiv:2505.15510](https://arxiv.org/abs/2505.15510)

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: (a) 순수 텍스트 근거를 사용하는 T-MCoT와 (b) 이미지-텍스트 교차 근거를 생성하는 I-MCoT의 비교*

대규모 비전-언어 모델(LVLM)의 멀티모달 체인-오브-쏘트(MCoT) 추론에서 **시각적 사고(Visual Thoughts)**라는 통합된 메커니즘을 발견하였으며, 이는 텍스트 기반과 이미지 교차 방식의 MCoT 모두를 설명하는 새로운 관점을 제시한다.

## Motivation

- **Known**: 최근 LVLM은 MCoT 추론으로 성능 향상을 이루었으며, 텍스트 기반 MCoT(T-MCoT)와 이미지-텍스트 교차 MCoT(I-MCoT) 두 가지 패러다임이 존재한다. 일부 연구는 I-MCoT가 인간의 인지 처리를 더 잘 반영한다고 주장하고, 다른 연구는 수학적 맥락에서 텍스트 기반이 우수하다고 제시한다.

- **Gap**: 서로 다른 MCoT 패러다임이 왜 효과적인지, 어떤 메커니즘으로 개선되는지 통일된 설명이 부족하며, 최적의 MCoT 패러다임을 식별하기 위한 일반화된 프레임워크가 없다.

- **Why**: MCoT의 실제 작동 메커니즘을 이해해야 더 나은 멀티모달 추론 방법을 개발할 수 있고, 상황에 맞는 최적의 전략을 선택할 수 있다.

- **Approach**: 시각적 사고를 중간 표현으로 정의하고, 텍스트 표현(자연언어, 구조화된 언어)과 시각 표현(편집 이미지, 생성 이미지)의 4가지 전략으로 분류하여 실험적으로 검증한다.

## Achievement

![Figure 2](figures/fig2.webp)
*그림 2: 컴퓨터 시스템 관점에서의 멀티모달 추론 비교: (a) 시각적 사고를 내부 캐시로 활용 vs (b) 원본 이미지에 직접 접근*

1. **시각적 사고의 효과성 입증**: 시각적 사고를 제거하고 원본 이미지만으로 추론하면 성능이 크게 저하되며, 이는 심지어 질문만으로 추론하는 것보다 나쁜 수준임을 확인했다. 이는 시각적 사고가 명시적으로 관련 시각 정보를 전달함으로써 추론 효율성을 크게 높임을 의미한다.

2. **4가지 시각적 사고 표현 전략 분석**: 
   - **N-LANG** (자연언어): 이미지 캡셔닝으로 풍부한 시각 설명 제공
   - **S-LANG** (구조화된 언어): 장면 그래프(scene graph)로 구조적 정보 제공
   - **E-IMG** (편집 이미지): 그라운딩, 깊이 추정, 분할 등으로 원본 이미지 처리
   - **G-IMG** (생성 이미지): 확산 모델으로 새로운 이미지 생성

   각 전략은 명확성과 효율성에서 차이를 보이며, 특정 시나리오에서 상이한 성능을 발휘한다.

3. **내부 메커니즘 규명**: 시각적 사고는 단순한 정보 전달을 넘어 **입력 이미지와 깊은 변환기(transformer) 계층 사이의 중개자** 역할을 하며, LVLM의 더 고급 인지 처리를 가능하게 한다.

## How

![Figure 3](figures/fig3.webp)
*그림 3: 텍스트 표현 (a)과 시각 표현 (b)의 시각적 사고. 텍스트 표현은 N-LANG과 S-LANG, 시각 표현은 E-IMG와 G-IMG를 포함*

- **정형화된 정의**: 시각적 사고(R_EVT)를 수식 (1)로 정형화하여, 과제 질문(Q_T), 명시적 지시사항(I_EVT), 이전 추론 단계(R_<i), 시각 입력(V_I)의 함수로 표현

- **분류 체계**: 생성 방식에 따라 **텍스트 기반 MCoT** (자연언어, 구조화된 언어)와 **이미지 기반 MCoT** (편집 이미지, 생성 이미지)로 이원화

- **캐시 비유**: 원본 이미지를 "외부 저장소"로, 시각적 사고를 "내부 캐시"로 개념화하여 반복적 이미지 재처리 부담을 감소시키는 방식 설명

- **정보 흐름 분석**: 어텐션 메커니즘(attention mechanism)과 LVLM 내부 정보 흐름을 추적하여 시각적 사고가 깊은 계층으로의 시각 정보 전달을 촉진하는 방식 검증

## Originality

- **통합 관점 제시**: T-MCoT와 I-MCoT의 이질적으로 보이는 두 패러다임을 **시각적 사고**라는 단일한 개념으로 통일한 첫 번째 시도로, 기존의 패러다임 간 논쟁에 이론적 해결책을 제공

- **체계적 분류 체계**: 시각적 사고의 4가지 표현 방식을 체계적으로 정의하고 비교하는 프레임워크 구축으로, 향후 새로운 MCoT 방법론 개발의 이론적 토대 마련

- **메커니즘 수준의 깊이**: 단순 성능 비교를 넘어 LVLM 내부의 정보 흐름, 어텐션 패턴, 계층 간 정보 전달 방식을 분석함으로써 "왜" 작동하는지에 대한 심층적 이해 제공

- **외부 기억 비유**: 컴퓨터 시스템의 캐시 개념을 활용한 창의적 비유로, 추상적인 AI 메커니즘을 직관적으로 설명

## Limitation & Further Study

- **제한 사항**:
  - 4가지 시각적 사고 표현이 모든 가능한 형태를 완전히 커버하는지 검증 필요 (새로운 하이브리드 형태의 가능성)
  - 실험이 특정 LVLM 아키텍처(예: LLaVA, GPT-4V 등)에 제한될 수 있으며, 다양한 아키텍처에서의 일반화 정도 미확인
  - 계산 비용(computational overhead) 분석이 명시적으로 부재하여, 각 표현 방식의 실제 효율성 비교가 불완전

- **후속 연구 방향**:
  - 시각적 사고의 최적 조합(앙상블) 전략 개발로, 서로 다른 표현 방식을 효과적으로 혼합하는 방법 탐색
  - 동적 시각적 사고 선택 메커니즘 구축으로, 과제의 특성에 따라 자동으로 최적의 표현 형태를 선택하는 적응형 시스템 개발
  - 다국어 및 다중 문화 맥락에서 시각적 사고의 효과성 검증
  - 시각적 사고가 모델의 환각(hallucination) 감소에 미치는 영향 분석


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.2/5

**총평**: 본 논문은 멀티모달 추론 분야의 오랜 논쟁(T-MCoT vs I-MCoT)에 "시각적 사고"라는 새로운 이론적 렌즈를 제공함으로써 개념적 통합을 이루었으며, 4가지 표현 전략의 체계적 분류는 향후 MCoT 방법론 개발의 로드맵을 제시한다. 다만 내부 메커니즘 분석의 기술적 깊이와 실제 성능 이득에 대한 정량적 검증이 보강된다면 더욱 영향력 있는 기여가 될 것으로 예상된다.

## Related Papers

- 🏛 기반 연구: [[papers/785_T-sciq_Teaching_multimodal_chain-of-thought_reasoning_via_mi/review]] — 멀티모달 체인-오브-쏘트 추론의 기본 메커니즘이 과학 문제 해결 교육의 이론적 토대를 제공합니다.
- 🔗 후속 연구: [[papers/840_Transforming_Science_with_Large_Language_Models_A_Survey_on/review]] — 시각적 사고 메커니즘을 과학 연구의 멀티모달 AI 시스템으로 확장하여 더 효과적인 과학적 추론을 가능하게 합니다.
- 🧪 응용 사례: [[papers/037_A_Survey_on_Uncertainty_Quantification_Methods_for_Deep_Lear/review]] — 시각적 추론에서의 불확실성을 정량화하여 멀티모달 AI 시스템의 신뢰성을 향상시키는 방법을 제시합니다.
- 🔗 후속 연구: [[papers/785_T-sciq_Teaching_multimodal_chain-of-thought_reasoning_via_mi/review]] — 멀티모달 과학 문제 해결을 시각적 사고라는 통합된 추론 메커니즘으로 확장하여 더 깊은 이해를 제공합니다.
