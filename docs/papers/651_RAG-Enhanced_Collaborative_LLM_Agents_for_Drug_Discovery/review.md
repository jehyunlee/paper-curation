---
title: "651_RAG-Enhanced_Collaborative_LLM_Agents_for_Drug_Discovery"
authors:
  - "Namkyeong Lee"
  - "E. Brouwer"
  - "Ehsan Hajiramezanali"
  - "Chanyoung Park"
  - "Gabriele Scalia"
date: "2025"
doi: "10.48550/arXiv.2502.17506"
arxiv: ""
score: 4.0
essence: "본 논문은 검색 증강 생성(RAG, Retrieval-Augmented Generation)과 다중 에이전트 협력을 활용하여 신약 발견 작업을 수행하는 CLADD 프레임워크를 제시한다. 도메인 특화 미세조정 없이 일반용도 LLM을 활용하면서도 이질적인 생화학 데이터의 동적 통합과 개방형 질문에 대한 추론을 가능하게 한다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/AI_Drug_Discovery"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Lee et al._2025_RAG-Enhanced Collaborative LLM Agents for Drug Discovery.pdf"
---

# RAG-Enhanced Collaborative LLM Agents for Drug Discovery

> **저자**: Namkyeong Lee, E. Brouwer, Ehsan Hajiramezanali, Chanyoung Park, Gabriele Scalia | **날짜**: 2025 | **DOI**: [10.48550/arXiv.2502.17506](https://doi.org/10.48550/arXiv.2502.17506)

---

## Essence

![Figure 1](figures/fig1.webp) *CLADD 프레임워크의 전체 구조: 계획 팀(Planning Team), 지식그래프 팀(Knowledge Graph Team), 분자 이해 팀(Molecule Understanding Team)의 협력*

본 논문은 검색 증강 생성(RAG, Retrieval-Augmented Generation)과 다중 에이전트 협력을 활용하여 신약 발견 작업을 수행하는 CLADD 프레임워크를 제시한다. 도메인 특화 미세조정 없이 일반용도 LLM을 활용하면서도 이질적인 생화학 데이터의 동적 통합과 개방형 질문에 대한 추론을 가능하게 한다.

## Motivation

- **Known**: 최근 대형언어모델(LLM)이 신약 발견 가속화에 큰 잠재력을 보이고 있으며, 특히 과학 문헌과 분자 데이터를 이해할 수 있는 능력이 뛰어남

- **Gap**: 기존 접근법들은 도메인 특화 미세조정에 의존하는데, 이는 (1) 새로운 LLM 아키텍처의 빠른 등장으로 유지보수가 어렵고, (2) 지속적인 미세조정으로 재앙적 망각(catastrophic forgetting)을 야기하며, (3) 신약 발견의 복잡하고 개방형 특성에 적응하기 어려움

- **Why**: 실제 신약 발견 질문은 복잡하고 맥락에 따라 다르며, 새로운 실험 결과와 문헌이 지속적으로 생성되므로 정적 모델로는 일반화 불가능

- **Approach**: RAG 기반 다중 에이전트 프레임워크를 통해 동적 지식 통합, 이질적 생화학 데이터 처리, 미세조정 불필요

## Achievement

![Figure 3](figures/fig3.webp) *약물-표적 예측 작업에서 에이전트 간 협력 예시: 활성화된 단백질(OPRD1, ADRB2, OPRM1)을 식별*

1. **다양한 신약 발견 작업 지원**: 약물-표적 예측(drug-target prediction), 분자 주석(molecular captioning), 생물학적 활성도 예측 등 다양한 제로샷(zero-shot) 및 개방형 작업 수행 가능

2. **일반용도 LLM의 효과적 활용**: 도메인 특화 미세조정 없이 외부 생화학 데이터베이스와 지식그래프를 동적으로 통합하여 성능 향상

3. **성능 우월성**: 일반용도 LLM, 도메인 특화 LLM, 전통 딥러닝 방식 모두를 능가하는 성능 달성

## How

![Figure 1](figures/fig1.webp) *CLADD의 세 가지 팀 구조와 정보 흐름*

**Planning Team (계획 팀)**
- **MolAnn Planner**: 질의 분자의 주석이 충분한지 판단하여 추가 정보 필요성 결정
- **KG Planner**: 지식그래프에 관련 정보가 존재하는지 평가

**Knowledge Graph (KG) Team (지식그래프 팀)**
- **Anchoring 방식**: 질의 분자가 지식그래프에 없을 때, 유사한 약물을 앵커로 활용하여 관련 정보 검색
- **DrugRel Agent**: 약물 간 관계 정보 추출 (유사성 검색 및 GNN 활용)
- **BioRel Agent**: 생물학적 관계 정보 추출 (2-hop 경로 등)

**Molecular Understanding (MU) Team (분자 이해 팀)**
- **분자 구조 분석**: 화학 구조 기반 분석
- **외부 도구 활용**: 분자 주석 모델을 통한 추가 설명
- **정보 통합**: KG 팀의 요약 정보와 함께 종합 분석

**Prediction Agent (예측 에이전트)**
- 모든 팀의 정보를 통합하여 최종 답변 생성

## Originality

- **다중 에이전트 협력의 모듈화**: 각 에이전트가 특정 데이터 소스와 역할에 특화되어 정보 처리 개선
- **Anchoring 메커니즘**: 질의 분자가 지식그래프에 없을 때 유사 분자를 통한 효과적인 정보 검색 (신규성)
- **RAG 적용의 도메인 특화**: 생화학 데이터의 이질성(heterogeneity), 모호성(ambiguity), 다중 소스 통합 문제를 체계적으로 해결
- **미세조정 불필요**: 일반용도 LLM만으로 도메인 특화 성능 달성, 지식 업데이트의 유연성 제공

## Limitation & Further Study

- **지식그래프 품질 의존성**: 외부 지식베이스의 완성도가 시스템 성능에 큰 영향을 미치는데, 현실의 생화학 데이터는 불완전하고 편향되어 있을 수 있음
- **검색 정확도 제한**: 광대한 생화학 공간에서 정확한 검색이 어렵고, 일반용도 LLM의 제한된 도메인 전문성으로 관련성 있는 정보 식별이 어려울 수 있음
- **앵커링 방식의 한계**: 유사 분자가 존재하지 않거나 매우 드문 경우 효율성 저하
- **해석성과 신뢰도**: 다중 에이전트 협력의 복잡성으로 인한 의사결정 과정 추적의 어려움
- **후속 연구 방향**: (1) 지식그래프 질 개선과 자동 업데이트 메커니즘, (2) 도메인 특화 임베딩 모델 통합, (3) 불확실성 정량화 및 신뢰도 평가 메커니즘

## Evaluation

- **Novelty**: 4/5
  - 신약 발견을 위한 다중 에이전트 RAG 프레임워크는 참신하나, 개별 기술 요소들은 기존 방법의 조합

- **Technical Soundness**: 4/5
  - 전체적으로 기술적으로 건전하나, 지식그래프 품질 및 검색 정확도에 대한 깊이 있는 분석 부족

- **Significance**: 4/5
  - 신약 발견 분야에 실질적 영향을 미칠 수 있으나, 실제 임상 단계의 신약 발견 파이프라인과의 통합 예시 부족

- **Clarity**: 4/5
  - 전반적으로 잘 구성되고 명확하나, 복잡한 다중 에이전트 상호작용의 일부 세부사항이 형식화 부족

- **Overall**: 4/5

**총평**: CLADD는 신약 발견에 RAG와 다중 에이전트 협력을 효과적으로 적용한 실용적 프레임워크로, 도메인 특화 미세조정의 필요성을 제거하면서도 우수한 성능을 달성했다. 다만 외부 지식 품질과 검색 정확도에 대한 더 심화된 분석과 실제 산업 적용 가능성 검증이 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/814_Tooling_or_Not_Tooling_The_Impact_of_Tools_on_Language_Agent/review]] — 신약 발견에서 LLM 활용이라는 공통점이 있지만 RAG 기반 협력적 접근법과 도구 증강의 한계라는 다른 관점을 제시한다.
- 🔗 후속 연구: [[papers/290_DrugAgent_Automating_AI-aided_Drug_Discovery_Programming_thr/review]] — AI 기반 약물 발견 프로그래밍 자동화 연구를 RAG 증강 협력 프레임워크로 확장할 수 있다.
- 🏛 기반 연구: [[papers/675_Retrieval-Augmented_Generation_for_Knowledge-Intensive_NLP_T/review]] — 검색 증강 생성의 일반적 방법론이 신약 발견을 위한 협력적 LLM 에이전트 시스템의 기술적 기반이다.
- 🔗 후속 연구: [[papers/415_Hunt_Globally_Wide_Search_AI_Agents_for_Drug_Asset_Scouting/review]] — RAG 강화 협력 LLM 에이전트가 글로벌 약물 자산 스카우팅의 다국어 처리 능력을 향상시킬 수 있습니다.
- ⚖️ 반론/비판: [[papers/814_Tooling_or_Not_Tooling_The_Impact_of_Tools_on_Language_Agent/review]] — 화학 작업에서 도구 증강이 항상 성능을 향상시키지 않는다는 발견이 RAG 기반 협력적 접근법의 필요성을 뒷받침한다.
- 🏛 기반 연구: [[papers/837_Training_a_Scientific_Reasoning_Model_for_Chemistry/review]] — 약물 발견을 위한 RAG 강화 협업 LLM 에이전트 기술이 ether0의 약물 발견 지원 능력에 기반을 제공한다.
