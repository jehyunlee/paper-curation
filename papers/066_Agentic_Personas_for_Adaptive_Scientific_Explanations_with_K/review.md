---
title: "066_Agentic_Personas_for_Adaptive_Scientific_Explanations_with_K"
authors:
  - "Susana Nunes"
  - "Tiago Guerreiro"
  - "Catia Pesquita"
date: "2026.03"
doi: "미제공"
arxiv: ""
score: 4.2
essence: "본 논문은 지식그래프(Knowledge Graph) 기반 설명 생성에 **에이전틱 페르소나(agentic personas)**를 도입하여, 정적 사용자 모델의 한계를 극복하고 전문가의 다양한 인식론적 입장(epistemic stances)을 반영한 적응형 설명을 제공하는 강화학습 기반 접근법을 제시한다."
tags:
  - "cat/Reinforcement_Learning_and_Self-Verification"
  - "sub/Autonomous_Agent_Learning_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Nunes et al._2026_Agentic Personas for Adaptive Scientific Explanations with Knowledge Graphs.pdf"
---

# Agentic Personas for Adaptive Scientific Explanations with Knowledge Graphs

> **저자**: Susana Nunes, Tiago Guerreiro, Catia Pesquita | **날짜**: 2026-03-23 | **DOI**: [미제공](https://doi.org/)

---

## Essence

![Figure 1](figures/fig1.webp) *페노피브레이트의 관상동맥질환 치료 관계에 대한 비적응형(REx)과 적응형(페르소나 조건부) 설명 예시*

본 논문은 지식그래프(Knowledge Graph) 기반 설명 생성에 **에이전틱 페르소나(agentic personas)**를 도입하여, 정적 사용자 모델의 한계를 극복하고 전문가의 다양한 인식론적 입장(epistemic stances)을 반영한 적응형 설명을 제공하는 강화학습 기반 접근법을 제시한다.

## Motivation

- **Known**: 현존하는 설명가능 AI(XAI) 시스템과 지식그래프 기반 설명은 정적 사용자 모델을 가정하여 전문가의 목표, 추론 전략, 결정 맥락을 무시함. 기존 지식그래프 설명은 경로 기반 추론으로 신뢰성 있는 설명을 제공하나 일괄적(one-size-fits-all) 방식임.

- **Gap**: 생물의학 등 복잡한 영역의 전문가들은 인식론적으로 다양한 입장을 가짐(기계적 vs. 인과적 추론, 과학적 타당성 우선도, 불확실성 가중치 등). 개별 수준의 사용자 데이터 수집은 비용이 높고 비현실적이어서 적응형 설명 생성의 주요 장애물이 됨.

- **Why**: 약물 발견과 같은 고위험 영역에서 전문가의 인식론적 입장에 맞춘 설명이 신뢰도 상승, 의사결정 품질 개선, 더 깊은 이해 증진을 도모할 수 있음.

- **Approach**: 제한된 전문가 피드백으로부터 파생된 **구조화된 추론 전략 표현(agentic personas)**을 대언어모델(LLM)로 구현하고, 이를 강화학습의 보상 함수에 통합하여 적응형 설명을 조건부로 생성하는 2단계 프레임워크 제시.

## Achievement

![Figure 2](figures/fig2.webp) *적응형 설명성 접근법의 개요: Phase I은 전문가 피드백으로부터 에이전틱 페르소나 생성, Phase II는 페르소나 조건부 보상을 통한 강화학습*

1. **페르소나 기반 설명이 비적응형 기준선을 일관되게 능가**: 22명 사용자 연구에서 적응형 페르소나 조건부 설명이 과학적 타당성, 관련성, 완성도 측면에서 일관되게 선호됨.

2. **피드백 요구사항 대폭 감소**: 페르소나 기반 학습이 직접적 인간 피드백 요구량을 **2자리 수(약 100배) 감소**시키면서도 최첨단 예측 성능 유지.

3. **페르소나 일관성 검증**: 생성된 페르소나들이 대응하는 전문가의 평가와 높은 일치도를 보이며, 페르소나가 실제 전문가 추론을 신뢰성 있게 모델링함을 입증.

## How

![Figure 4](figures/fig4.webp) *전문가 응답 임베딩의 t-SNE 투영 및 응집 클러스터링(k=2)*

![Figure 5](figures/fig5.webp) *페르소나 내러티브 프로필의 예시*

### Phase I: 에이전틱 페르소나 구축

- **전문가 연구 설계**: 생명과학(n=4), CS/AI 바이오메디컬(n=5), 계산생물학(n=2) 배경의 11명 전문가를 대상으로 약물 재창출(DR), 약물-표적 상호작용(DTI) 과제에 대한 지식그래프 설명 평가
  
- **평가 차원**: 관련성(causal mechanism informative), 완성도(세부/간결 균형), 타당성(생의학 원리 일관성)의 3가지 차원에서 Likert 5점 척도 평가 + 정성적 피드백 수집

- **임베딩 & 클러스터링**:
  - 125개 정성 피드백 문장을 "I prefer..." 형식의 1인칭 표현으로 정규화
  - Sentence-BERT(all-mpnet-base-v2)로 768차원 벡터로 인코딩
  - K-Means, Agglomerative, HDBSCAN 3가지 알고리즘으로 클러스터링
  - Silhouette, Davies-Bouldin, Calinski-Harabasz, Inertia로 최적 k값 결정

- **LLM 기반 페르소나 합성**: 클러스터된 전문가 피드백에 대한 LLM 기반 내러티브 합성으로 응집성 있는 인식론적 입장 캡슐화

- **페르소나 윤리성 설계**: 
  - 인구통계학 대신 설명 선호도 기반 특성화
  - 클러스터 수준 증거로 추적가능성 유지
  - 신원 기술자 최소화
  - 배포 전 집계 전문가 평가로 신뢰성 검증

### Phase II: 페르소나 조건부 강화학습

- **적응형 설명의 정의**: 기존 충실도(fidelity) α와 관련성(relevance) β에 **인식론적 입장 점수 γ(p, θ)** 추가
  - 목표: $\arg\max_p f[\alpha(p), β(p), γ(p, θ)]$

- **보상 함수 개선**: 페르소나 선호도를 RL 보상으로 통합하여 경로 선택을 인식론적 입장에 정렬

- **학습 효율성**: 개별 사용자 추적 없이 일반화 가능한 페르소나로 학습하여 피드백 요구량 최소화

## Originality

- **개념적 기여**: 정적 사용자 모델을 넘어 "인식론적 입장(epistemic stance)"이라는 새로운 개념으로 전문가 다양성을 이론화하고 설명성에 적용한 첫 시도.

- **방법론적 혁신**: RLHF 원리를 지식그래프 설명에 적응시키되, LLM 기반 페르소나를 조건부 보상 모델로 활용하는 새로운 파이프라인.

- **페르소나 윤리성**: 기존 페르소나 방법론의 본질주의적(essentialist) 위험성을 인식하고, 증거 추적성과 투명성을 내재한 설계 원칙 제시.

- **고위험 도메인 적용**: 약물 발견의 다층 추론(분자 메커니즘 ↔ 임상 결과)과 고위험 의사결정 맥락에서의 검증으로 실제 영향력 시연.

## Limitation & Further Study

- **표본 규모 제한**: 전문가 11명, 피드백 15개(최소)로부터 도출된 페르소나는 도메인 내 더 광범위한 인식론적 다양성을 완전히 대표하지 못할 가능성.

- **클러스터링 안정성**: k=2 선택의 일관성과 더 큰 전문가 집단에서의 재현성 미검증. 과소 또는 과잉 클러스터링의 영향 미분석.

- **LLM 의존성**: 페르소나 합성 품질이 기반 LLM(및 프롬프트)에 크게 의존하며, 상이한 LLM 간 안정성 미평가.

- **일반화 가능성**: 생물의학 영역 특화 평가로, 타 고위험 도메인(금융, 법률)에의 적용성 미검증.

- **페르소나 정적성**: 전문가의 추론 전략이 시간/맥락에 따라 진화할 가능성에 대한 동적 적응 메커니즘 부재.

**후속 연구**:
- 대규모 전문가 데이터를 통한 페르소나 입도(granularity) 최적화
- 다중 도메인 일반화 평가
- 실시간 사용자 선호도 피드백으로 페르소나 동적 갱신 메커니즘
- 페르소나 간 경계 모호성 또는 중첩 케이스 처리

## Evaluation

- **Novelty**: 4.5/5 — 인식론적 입장 개념과 LLM 기반 페르소나의 RL 적분이 참신하나, 개별 기술 요소(clustering, RLHF)는 기존 기법의 조합.

- **Technical Soundness**: 4/5 — 전체 파이프라인이 논리적이고 강화학습 공식화가 명확하나, 클러스터링 선택(k=2)의 엄격한 통계적 정당성 및 LLM 프롬프트 민감도 분석 부족.

- **Significance**: 4.5/5 — 고위험 과학 영역에서의 적응형 설명성이 높은 실무적 가치를 가지며, 피드백 요구 100배 감소는 확장성 측면에서 의미 있음. 다만 11명 규모 검증이 광범위 임팩트 주장을 제약.

- **Clarity**: 4/5 — 전반 문제 정의와 방법론이 명확하고 체계적이나, 페르소나 내러티브 프로필의 구체적 구성 요소와 보상 함수의 다목적 집계 함수 f의 세부사항이 본문에 명시적으로 기술되지 않음(보충자료 참조).

- **Overall**: 4.2/5

**총평**: 본 논문은 적응형 설명성을 인식론적 입장 개념으로 재정의하고, 제한된 전문가 피드백을 LLM 기반 페르소나로 확장하는 창의적이고 실용적인 접근법을 제시한다. 약물 발견 도메인에서의 엄격한 검증과 윤리적 페르소나 설계 원칙은 강점이나, 표본 규모의 제한과 다중 도메인 일반화 부재는 주요 약점이다. 고위험 전문가 AI 시스템의 설명성 향상에 의미 있는 기여를 하지만, 대규모 재현성 검증으로 강화될 필요가 있다.

## Related Papers

- 🔄 다른 접근: [[papers/484_Learning_to_generate_research_idea_with_dynamic_control/review]] — 두 논문 모두 연구 아이디어 생성을 다루되 Agentic Personas는 지식그래프 기반 설명, Learning to generate는 참신성-실현성 균형에 초점을 맞춘다.
- 🏛 기반 연구: [[papers/020_A_Review_of_Relational_Machine_Learning_for_Knowledge_Graphs/review]] — 지식 그래프 관계형 머신러닝 리뷰는 Agentic Personas의 지식그래프 기반 설명 생성 시스템 설계에 핵심적인 이론적 배경을 제공한다.
- 🧪 응용 사례: [[papers/187_Can_LLMs_Generate_Novel_Research_Ideas_A_Large-Scale_Human_S/review]] — 대규모 인간 평가를 통한 LLM의 새로운 연구 아이디어 생성 연구는 Agentic Personas의 적응형 설명 효과를 실증적으로 검증하는 방법론을 제시한다.
- 🔄 다른 접근: [[papers/484_Learning_to_generate_research_idea_with_dynamic_control/review]] — 두 논문 모두 연구 아이디어 생성을 다루되 동적 제어는 참신성-실현성 균형, Agentic Personas는 적응형 설명에 중점을 둔다.
