---
title: "668_ResearchAgent_Iterative_Research_Idea_Generation_over_Scient"
authors:
  - "Jinheon Baek"
  - "Sujay Kumar Jauhar"
  - "Silviu Cucerzan"
  - "Sung Ju Hwang"
date: "2025.02"
doi: "10.48550/arXiv.2404.07738"
arxiv: ""
score: 4.3
essence: "대규모 언어 모델(LLM)의 백과사전적 지식과 추론 능력을 활용하여 과학 문헌으로부터 자동으로 새로운 연구 아이디어를 생성하고 인간 선호도 기반의 피어 리뷰 에이전트를 통해 반복적으로 개선하는 시스템을 제안한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Autonomous_Hypothesis_Discovery"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Baek et al._2025_ResearchAgent Iterative Research Idea Generation over Scientific Literature with Large Language Mod.pdf"
---

# ResearchAgent: Iterative Research Idea Generation over Scientific Literature with Large Language Models

> **저자**: Jinheon Baek, Sujay Kumar Jauhar, Silviu Cucerzan, Sung Ju Hwang | **날짜**: 2025-02-09 | **DOI**: [10.48550/arXiv.2404.07738](https://doi.org/10.48550/arXiv.2404.07738)

---

## Essence

![Figure 1](figures/fig1.webp)
*Figure 1: (A) 과학 지식 자원 구성 - 논문, 학술 그래프, 엔티티 중심 지식 저장소 (B) 문제 식별→방법 개발→실험 설계의 체계적 연구 아이디어 생성 과정과 인간 판단 기반 검토 에이전트의 반복적 개선*

대규모 언어 모델(LLM)의 백과사전적 지식과 추론 능력을 활용하여 과학 문헌으로부터 자동으로 새로운 연구 아이디어를 생성하고 인간 선호도 기반의 피어 리뷰 에이전트를 통해 반복적으로 개선하는 시스템을 제안한다.

## Motivation

- **Known**: 최근 LLM은 수학, 물리, 의학 등 다양한 전문 분야에서 뛰어난 성능을 보이고 있으며, 기존 연구는 주로 실험 검증 단계를 가속화하는 데 집중해 왔다.

- **Gap**: 과학 연구의 첫 번째 단계인 **새로운 연구 문제의 개념화와 아이디어 생성**에 LLM을 활용한 연구가 부족하다. 기존 가설 생성 방법들은 두 개념 간의 단순한 관계 탐지에 그쳐 실제 연구의 다면적 복잡성을 포착하지 못한다.

- **Why**: 연령 7백만 건 이상의 학술 논문 발표, 신약 개발의 수년에 걸친 시간 소모 등 현재 과학 연구 프로세스는 매우 느리고 노동집약적이며 광대한 지식 통합을 요구한다.

- **Approach**: 인간 연구자의 작업 방식을 모델링하여 (1) 학술 그래프 기반 관련 문헌 이해, (2) 엔티티 중심 지식 저장소를 통한 개념 간 관계 파악, (3) 인간 판단으로부터 유도된 평가 기준을 갖춘 검토 에이전트를 통한 반복적 개선을 구현한다.

## Achievement

![Figure 2](figures/fig2.webp)
*Figure 2: 인간 평가(상단)와 모델 기반 평가(하단)에서 ResearchAgent의 주요 결과 - 베이스라인 대비 명확성, 관련성, 유의성, 특히 참신성에서 우수*

1. **우수한 생성 품질**: 인간 평가와 모델 기반 평가 모두에서 LLM 베이스라인을 크게 상회하며, 특히 생성된 아이디어의 참신성(novelty)에서 뛰어난 성과를 달성

2. **다학제적 검증**: 여러 학문 분야의 과학 논문에 대해 실험 검증을 수행하여 ResearchAgent의 일반화 가능성과 실용성을 입증

3. **컴포넌트 유효성**: 엔티티 중심 지식 저장소와 반복적 개선 단계가 순수 선행 연구만 기반한 인스턴스 대비 의미 있게 더 나은 아이디어 생성에 기여함을 정량화

## How

![Figure 4](figures/fig4.webp)
*Figure 4: 반복 개선 단계 수에 따른 성과 변화 - 초기 단계에서 가장 큰 개선이 이루어지며 3-4 단계 이후 수렴*

**ResearchAgent 시스템 구성**:

- **지식 소스 통합**: 
  - 핵심 논문으로부터 시작하여 학술 그래프(references, citations) 기반으로 관련 논문 탐색
  - 수많은 논문에서 채굴한 개념의 공출현(co-occurrence)을 통해 엔티티 중심 지식 저장소 구축
  - 엔티티 추출 및 검색 단계로 도메인 내 및 도메인 간 개념 관계 포착

- **체계적 아이디어 생성**:
  - 문제 식별(Problem Identification): 연구 공백 및 미해결 질문 분석
  - 방법 개발(Method Development): 제안된 문제 해결을 위한 방법론 제시
  - 실험 설계(Experiment Design): 방법의 성공 여부 측정을 위한 실험 계획

- **피어 리뷰 기반 반복 개선**:
  - 다수의 LLM 기반 ReviewingAgents 인스턴스 운영
  - 인간 연구자의 실제 판단으로부터 프롬프팅을 통해 평가 기준 유도(human preference-aligned)
  - 구성적 비판(constructive critique) 제공으로 생성된 아이디어 반복 정제

**형식적 표현**: o = [p, m, d]로 아이디어 구성 (문제, 방법, 실험설계)

## Originality

- **개방형 아이디어 생성**: 기존 가설 생성 연구의 제한된 스코프(두 개념 간 단순 관계)를 벗어나 다면적, 복잡한 연구 문제의 완전한 구성 가능

- **인간 중심 평가 기준 도입**: 실제 연구자의 판단으로부터 LLM 검토 에이전트의 평가 기준을 귀납적으로 유도하여 과학적 선호도 정렬 달성

- **통합적 지식 활용**: 개별 논문, 학술 그래프 관계, 엔티티 중심 지식을 연동하여 도메인 간 아이디어 교차수분(cross-pollination) 촉진

- **첫 번째 체계적 검증**: 과학 아이디어 생성 단계에서 LLM의 효과를 개방형 설정에서 인간 평가와 모델 기반 평가를 모두 포함하여 최초 평가

## Limitation & Further Study

- **지식 취득 병목**: 엔티티 추출 및 학술 그래프 구성에 상당한 전처리가 필요하며, 논문이 제한된 분야에서의 적용 가능성 미탐색

- **평가 객관성 문제**: 인간 판단 기반 평가 기준 유도 시 평가자 편향, 평가 일관성, 그리고 평가자 샘플 크기의 영향 검토 필요

- **실제 검증 부재**: 생성된 연구 아이디어의 실제 실험적 실행 가능성, 윤리적 타당성, 실제 과학자의 채택 의도에 대한 검증 부재

- **후속 연구 방향**:
  - 자동 논문 작성 및 코드 생성까지 확장하여 전체 연구 사이클 지원 
  - 다양한 학문 분야의 전문성을 반영한 도메인별 맞춤형 에이전트 개발
  - 생성된 아이디어와 실제 발표된 연구 간의 중복성 및 실제 임팩트 측정

## Evaluation

- **Novelty**: 4.5/5 — 과학 문헌 기반 개방형 아이디어 생성의 첫 체계적 시도이나, 세부 메커니즘의 신규성은 개별적으로는 제한적

- **Technical Soundness**: 4/5 — 방법론의 전반적 타당성은 우수하나, 엔티티 추출 정확도, 학술 그래프 품질의 영향에 대한 민감도 분석 부족

- **Significance**: 4.5/5 — 과학 연구 효율화에 미칠 잠재적 임팩트가 크고, AI 기반 과학 지원의 새로운 방향 제시이나 실제 도입까지의 거리 존재

- **Clarity**: 4/5 — 전반적 구조와 논리 전개가 명확하나, 시스템 아키텍처 세부 및 프롬프팅 전략에 대한 상세한 기술 설명 부족

- **Overall**: 4.3/5

**총평**: 과학 연구의 아이디어 생성 단계에 LLM을 체계적으로 적용한 선도적 연구로, 인간 중심의 평가 기준 도입과 다층적 지식 통합이 강점이나, 실제 연구 적용 가능성 검증과 세부 메커니즘의 강화가 향후 과제이다.

## Related Papers

- 🔗 후속 연구: [[papers/577_Nova_An_iterative_planning_and_search_approach_to_enhance_no/review]] — ResearchAgent의 반복적 연구 아이디어 생성은 Nova 프레임워크의 계획 수립과 검색 결합 방식을 더욱 발전시킨 형태입니다
- 🔄 다른 접근: [[papers/418_Hypothesis_Generation_for_Materials_Discovery_and_Design_Usi/review]] — 과학 지식 그래프 기반 가설 생성과 LLM 기반 재료 가설 생성의 다른 접근법을 비교할 수 있다
- 🔗 후속 연구: [[papers/194_Chain_of_ideas_Revolutionizing_research_via_novel_idea_devel/review]] — 과학 지식 그래프 기반 가설 생성을 문헌 체인 구조로 확장한 연구다
- 🧪 응용 사례: [[papers/757_Simulating_tabular_datasets_through_llms_to_rapidly_explore/review]] — 표 형식 데이터셋 시뮬레이션 기법을 과학 지식 그래프 기반 연구 아이디어 생성에 적용하여 더 체계적인 가설 검증 과정을 구축할 수 있다.
- 🏛 기반 연구: [[papers/071_AgentRxiv_Towards_Collaborative_Autonomous_Research/review]] — ResearchAgent의 반복적 아이디어 생성 메커니즘이 AgentRxiv의 누적적 지식 개선 시스템의 기반이 되는 기술적 토대이다.
- 🔗 후속 연구: [[papers/059_Agent_Laboratory_Using_LLM_Agents_as_Research_Assistants/review]] — Agent Laboratory의 연구 자동화 프레임워크는 ResearchAgent의 반복적 연구 아이디어 생성을 확장하여 실험 수행과 보고서 작성까지 포괄하는 완전한 연구 파이프라인을 구축합니다.
- 🏛 기반 연구: [[papers/434_Interesting_Scientific_Idea_Generation_using_Knowledge_Graph/review]] — 과학 지식 그래프를 활용한 연구 아이디어 생성의 기초적 접근이 개인화된 아이디어 생성 시스템의 이론적 토대를 제공함
