---
title: "070_Agentreview_Exploring_peer_review_dynamics_with_llm_agents"
authors:
  - "Yiqiao Jin"
  - "Qinlin Zhao"
  - "Yiyang Wang"
  - "Hao Chen"
  - "Kaijie Zhu"
date: "2024"
doi: "미제공"
arxiv: ""
score: 4.3
essence: "본 논문은 대규모언어모델(LLM) 기반 에이전트를 활용하여 학술지 피어 리뷰 과정을 시뮬레이션하고, 검토자 편향(reviewer bias), 사회적 영향(social influence), 권위 편향(authority bias) 등 다양한 사회학적 요인이 리뷰 결정에 미치는 영향을 정량화하는 첫 번째 프레임워크를 제시한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Multi-Agent_Scientific_Frameworks"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Jin et al._2024_Agentreview Exploring peer review dynamics with llm agents.pdf"
---

# Agentreview: Exploring peer review dynamics with llm agents

> **저자**: Yiqiao Jin, Qinlin Zhao, Yiyang Wang, Hao Chen, Kaijie Zhu, Yijia Xiao, Jindong Wang | **날짜**: 2024 | **DOI**: [미제공](https://doi.org/)

---

## Essence

![Figure 1](figures/fig1.webp) *AgentReview 프레임워크는 피어 리뷰 프로세스를 현실적으로 시뮬레이션하며, 다중 변수의 영향을 분리하여 분석한다.*

본 논문은 대규모언어모델(LLM) 기반 에이전트를 활용하여 학술지 피어 리뷰 과정을 시뮬레이션하고, 검토자 편향(reviewer bias), 사회적 영향(social influence), 권위 편향(authority bias) 등 다양한 사회학적 요인이 리뷰 결정에 미치는 영향을 정량화하는 첫 번째 프레임워크를 제시한다.

## Motivation

- **Known**: 피어 리뷰는 학술 출판의 핵심이지만, 검토자 편향, 불균형한 리뷰 품질, 불명확한 동기 등 여러 문제가 존재한다. 기존 분석은 실제 피어 리뷰 데이터에 의존하고 있다.

- **Gap**: (1) 피어 리뷰의 다변량(multivariate) 특성으로 인해 특정 요인의 영향 격리가 어렵다, (2) 검토자 편향과 의도 같은 잠재변수(latent variables)를 측정하기 어렵다, (3) 피어 리뷰 데이터의 민감성으로 인한 개인정보 보호 문제가 존재한다.

- **Why**: 피어 리뷰 메커니즘 개선을 위해서는 각 요인의 인과적 영향을 체계적으로 분리하고 정량화할 필요가 있으며, 이는 실제 데이터 기반 분석으로는 불가능하다.

- **Approach**: LLM 에이전트 기반 시뮬레이션 프레임워크를 구축하여 검토자(reviewer), 저자(author), 분야 의장(area chair, AC) 등의 특성을 조절하면서 대규모 피어 리뷰를 시뮬레이션하고, 53,800개 이상의 생성된 리뷰 문서를 분석한다.

## Achievement

![Figure 2](figures/fig2.webp) *5단계 피어 리뷰 파이프라인: (I) 검토자 평가, (II) 저자-검토자 토론, (III) 검토자-의장 토론, (IV) 메타리뷰 작성, (V) 최종 결정*

1. **사회적 영향(Social Influence)**: 리베탈(rebuttal) 이후 검토자들이 동료의 의견에 맞추는 현상을 확인하였으며, 이로 인해 평점의 표준편차가 27.2% 감소한다.

2. **검토자 편향의 결정적 영향**: 단 1명의 편향된 검토자만으로도 최종 결정의 37.1%가 변경되며, 무책임한(irresponsible) 검토자 1명은 전체 검토자의 commitment를 18.7% 감소시킨다(altruism fatigue).

3. **권위 편향과 후광효과(Halo Effects)**: 저자 신원이 알려진 논문에 대해서는 더 높은 평가가 주어지며, 전체 논문의 10%에서만 저자 신원이 공개되어도 최종 결정이 27.7% 변경된다.

4. **편향 증폭(Groupthink & Echo Chamber)**: 편향된 검토자들이 서로 부정적 의견을 강화하여 평점이 0.17 감소하고, 이것이 중립적 검토자에게까지 영향을 미쳐 0.25의 추가 평점 감소를 초래한다.

5. **정박 편향(Anchoring Bias)**: 리베탈의 영향이 다른 요인들보다 덜 중요하며, 이는 검토자들이 초기 인상에 크게 의존하기 때문이다.

## How

![Figure 3](figures/fig3.webp) *책임감 없는 검토자와 악의적 검토자의 수에 따른 초기 및 최종 평점의 분포 변화*

- **검토자 특성화**: 3개 차원으로 검토자 유형을 정의
  - Commitment: 책임감 있음(responsible) vs 없음(irresponsible)
  - Intention: 선의(benign) vs 악의(malicious)
  - Knowledgeability: 전문가 vs 비전문가

- **저자 신원 관리**: 이중맹검(double-blind) 정책 준수 vs 신원 공개 시나리오

- **분야 의장 유형**: 3가지 의사결정 스타일
  - Authoritarian: 자신의 판단 우선
  - Conformist: 검토자 의견 과도 의존
  - Inclusive: 모든 정보 종합 고려

- **5단계 파이프라인**:
  - Phase I: 3명 검토자의 독립적 평가
  - Phase II: 저자 리베탈 작성
  - Phase III: AC 주도 검토자 토론 및 평점 재검토
  - Phase IV: AC의 메타리뷰 작성
  - Phase V: 고정 수용률(32%) 기준 최종 결정

- **데이터 선택**: ICLR 2020-2023 논문 4년치, 공개 논문만 사용하여 개인정보 보호

## Originality

- 피어 리뷰 프로세스의 **전체 파이프라인을 LLM 에이전트로 시뮬레이션**한 첫 번째 연구로, 기존의 통계 분석이나 제한된 데이터 활용에서 벗어남

- **다중 변수의 인과적 영향을 정량화**할 수 있는 실험 설계로, 사회학 이론(사회적 영향, 집단사고, 권위편향 등)과의 명시적 연결

- **53,800개 이상의 생성된 피어 리뷰 문서로 구성된 대규모 합성 데이터셋** 제공으로 미래 연구의 기초 제공

- 검토자 commitment, intention, knowledgeability의 **3차원 특성화**로 피어 리뷰 과정의 복잡성을 체계적으로 모델링

## Limitation & Further Study

- **LLM 기반 시뮬레이션의 한계**: 생성된 리뷰와 실제 인간 검토자의 리뷰 간의 미묘한 차이가 존재할 수 있으며, LLM의 내재적 편향이 시뮬레이션 결과에 반영될 가능성

- **제한된 회의 선택**: ICLR만을 대상으로 하였으므로, 다른 학문 분야나 저널의 피어 리뷰 특성에 일반화 가능성 불명확

- **평가 메트릭의 단순화**: 최종 결정을 이진(binary) 수용/거절로만 평가하였으므로, 더 세분화된 평점(oral, spotlight, poster) 차이 미반영

- **상호작용 효과의 미흡한 분석**: 여러 요인의 결합 효과(interaction effects)에 대한 심화 분석 부재

- **후속 연구**: (1) 다양한 회의/저널 데이터로 확장, (2) 실제 리뷰어와의 검증 연구, (3) 파이프라인의 다양한 변형(예: single-blind, open review) 탐색, (4) 피어 리뷰 개선 메커니즘의 제안 및 평가

## Evaluation

- **Novelty**: 4.5/5 - LLM 에이전트 기반 피어 리뷰 시뮬레이션은 새로운 접근이나, 개별 기술 요소는 기존 연구 기반

- **Technical Soundness**: 4/5 - 5단계 파이프라인 설계와 실험 구성이 합리적이나, LLM 기반 시뮬레이션의 타당성 검증(human evaluation 등)이 제한적

- **Significance**: 4.5/5 - 피어 리뷰 시스템 개선에 구체적인 정량적 근거를 제공하며, 사회학 이론과의 연결로 학문적 기여도 높음

- **Clarity**: 4.5/5 - 전체 구조와 결과 제시가 명확하나, 일부 기술 세부사항(프롬프트 설계, 평가 기준)은 부록에만 기술

- **Overall**: 4.3/5

**총평**: 본 논문은 LLM 에이전트를 활용한 피어 리뷰 시뮬레이션이라는 혁신적 접근으로 기존 분석의 한계를 극복하고, 검토자 편향, 사회적 영향, 권위 편향 등의 정량적 영향을 처음 규명하여 피어 리뷰 시스템 개선에 실질적 기초를 제공한다. 다만 합성 데이터 기반 분석의 타당성 검증과 다양한 학문 영역으로의 일반화가 향후 과제이다.

## Related Papers

- 🔄 다른 접근: [[papers/608_Peer_Review_as_A_Multi-Turn_and_Long-Context_Dialogue_with_R/review]] — 피어 리뷰 과정에서 사회학적 편향 분석과 다중 턴 대화 분석이라는 서로 다른 접근법으로 리뷰 역학을 탐구한다.
- 🔗 후속 연구: [[papers/262_Deepreview_Improving_llm-based_paper_review_with_human-like/review]] — 기본적인 LLM 리뷰 생성을 사회적 요인과 편향을 고려한 복잡한 시뮬레이션으로 발전시킨다.
- 🏛 기반 연구: [[papers/628_Position_The_ai_conference_peer_review_crisis_demands_author/review]] — AI 기반 피어 리뷰의 위기 상황에서 편향과 사회적 영향을 정량화할 수 있는 분석 도구를 제공한다.
- 🏛 기반 연구: [[papers/608_Peer_Review_as_A_Multi-Turn_and_Long-Context_Dialogue_with_R/review]] — LLM 에이전트를 이용한 피어 리뷰 동역학 탐구로 다중턴 대화 기반 리뷰 프로세스의 이론적 기반을 제공한다.
