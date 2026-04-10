---
title: "705_SciAgents_Automating_Scientific_Discovery_Through_Bioinspire"
authors:
  - "Alireza Ghafarollahi"
  - "Markus J. Buehler"
date: "2024"
doi: "10.1002/adma.202413523"
arxiv: ""
score: 4.0
essence: "본 연구는 대규모 온톨로지 지식 그래프(ontological knowledge graphs), 대형 언어 모델(LLMs), 그리고 다중 에이전트 시스템을 결합하여 과학 발견 프로세스를 자동화하는 SciAgents 프레임워크를 제시한다. 생물 영감 재료(biologically inspired materials) 분야에 적용하여 인간의 연구 방법을 초월하는 규모, 정밀도, 탐색 능력으로 숨겨진 학제간 관계를 발견했다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/AI_Scientific_Discovery"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Ghafarollahi and Buehler_SciAgents Automating Scientific Discovery Through Bioinspired Multi-Agent Intelligent Graph Reasoni.pdf"
---

# SciAgents: Automating Scientific Discovery Through Bioinspired Multi-Agent Intelligent Graph Reasoning

> **저자**: Alireza Ghafarollahi, Markus J. Buehler | **날짜**: 2024 | **DOI**: [10.1002/adma.202413523](https://doi.org/10.1002/adma.202413523)

---

## Essence

본 연구는 대규모 온톨로지 지식 그래프(ontological knowledge graphs), 대형 언어 모델(LLMs), 그리고 다중 에이전트 시스템을 결합하여 과학 발견 프로세스를 자동화하는 SciAgents 프레임워크를 제시한다. 생물 영감 재료(biologically inspired materials) 분야에 적용하여 인간의 연구 방법을 초월하는 규모, 정밀도, 탐색 능력으로 숨겨진 학제간 관계를 발견했다.

## Motivation

- **Known**: 전통적인 인간 중심의 과학 연구는 배경 지식 검토, 가설 수립, 테스트, 검증 과정을 거치지만 연구자의 상상력과 기존 지식에 제한된다. LLMs는 다양한 작업에서 뛰어난 성능을 보이지만, 학습 범위 외 질문에 대해 부정확한 응답을 생성하고 투명성과 설명가능성 문제를 안고 있다.

- **Gap**: 단일 LLM 기반 에이전트는 복잡한 과학 발견의 다단계 추론, 상충하는 정보의 통합, 깊이 있는 사고를 요구하는 작업에 부족하다. 구조화된 지식 기반과 협업적 다중 에이전트 시스템이 필요하다.

- **Why**: 과학적 발견은 광대한 데이터에서 패턴과 연결을 식별해야 하며, 특히 생물 영감 재료 같은 학제간 영역에서는 인간이 놓치기 쉬운 숨겨진 관계를 체계적으로 탐색해야 한다.

- **Approach**: (1) 약 1000편의 과학 논문으로부터 구축한 대규모 온톨로지 지식 그래프를 활용하여 개념 간 관계를 구조화, (2) 맥락 기반 학습(in-context learning)으로 LLMs의 응답 정확도 향상, (3) 특화된 역할을 가진 다중 에이전트 시스템으로 협업적 가설 생성 및 검증

## Achievement

1. **자동화된 가설 생성 및 검증**: 온톨로지 에이전트(Ontologist), 과학자 에이전트(Scientist 1, 2), 비평가 에이전트(Critic)의 역할 분담으로 혁신적이고 체계적인 연구 가설을 생성. 새로운 바이오복합재료(biocomposite)를 발견하여 향상된 기계적 특성과 에너지 효율적 생산을 통한 지속가능성을 달성.

2. **학제간 숨겨진 연관성 발견**: 전통적으로 무관하다고 여겨지던 개념들 간의 연결고리를 식별. 예를 들어, 실크(silk)와 에너지 집약성(energy-intensive) 같은 개념들 간의 새로운 관계를 그래프 탐색을 통해 발견.

3. **두 가지 효과적인 운영 전략**: (a) 사전 프로그래밍된 에이전트 상호작용으로 일관성과 신뢰성 보장, (b) 완전 자동화된 유연한 프레임워크로 동적 적응성 제공 (인간-루프 상호작용 지원).

4. **인간 연구 방법 초과**: 규모, 정밀도, 탐색 능력에서 인간 연구 방법을 능가하는 시스템 구현.

## How

- **지식 그래프 샘플링**: 글로벌 지식 그래프에서 관련 부분 그래프(sub-graphs)를 추출하는 혁신적 샘플링 전략으로 핵심 개념과 상호관계 파악
- **맥락 기반 프롬프팅**: 각 에이전트에 최적화된 복잡한 프롬프팅 전략(complex prompting strategies)으로 추출된 그래프 정보를 프롬프트에 임베딩
- **역할 기반 에이전트 설계**: 
  - **Ontologist**: 주요 개념과 관계 정의
  - **Scientist 1**: 상세한 연구 제안서 작성
  - **Scientist 2**: 제안서 확장 및 정제
  - **Critic**: 철저한 검토 및 개선 제안
  - **Planner** (자동화 방식): 상세 계획 수립
  - **Assistant**: 생성된 가설의 참신성(novelty) 검증
- **반복적 상호작용**: 사전 프로그래밍 방식은 정해진 순서로, 자동화 방식은 문맥에 적응하여 에이전트 간 동적 상호작용
- **인-컨텍스트 학습**: 모델의 내재적 적응 능력을 활용하여 비용 높은 파인튜닝 없이 성능 향상

## Originality

- **novel sampling strategy**: 대규모 온톨로지 지식 그래프에서 관련 부분 그래프를 효율적으로 추출하는 새로운 전략
- **bioinspired multi-agent architecture**: 생물 시스템의 군집 지능(swarm of intelligence)에서 영감을 받은 다중 에이전트 설계
- **two complementary operational approaches**: 일관성과 유연성 사이의 트레이드오프를 다루는 두 가지 상호보완적 운영 방식
- **knowledge graph-augmented LLM reasoning**: 온톨로지 지식 그래프와 LLM 기반 그래프 추론의 통합으로 과학 발견 자동화
- **human-in-the-loop integration**: 두 번째 접근에서 인간의 전문성 개입을 허용하는 구조적 설계
- **학제간 발견 능력**: 실크 같은 생물 재료의 에너지 효율적 특성 개선에 대한 새로운 인사이트 도출

## Limitation & Further Study

- **제한사항**:
  - 온톨로지 지식 그래프의 구성이 약 1000편 논문에 기반하므로 도메인 완전성이 제한될 수 있음
  - LLMs의 hallucination 문제는 완전히 해결되지 않으며, 생성된 가설의 과학적 타당성 검증을 위한 실험적 검증이 필수
  - 두 접근 방식 간의 상대적 효과성과 우수성 비교 실증 데이터 부족
  - 계산 비용과 환경 영향에 대한 상세한 논의 부재

- **후속 연구 방향**:
  - 실제 실험실 검증을 통한 생성 가설의 과학적 타당성 평가
  - 더 넓은 범위의 과학 도메인(화학, 물리학, 생의학 등)에 대한 확장 및 일반화 연구
  - 온톨로지 지식 그래프의 동적 업데이트 메커니즘 개발로 최신 과학 지식 반영
  - 인간 연구자와의 협업 방식 최적화 및 사용성 개선
  - 다중 에이전트 시스템의 설명가능성 및 투명성 강화
  - 생성된 가설의 참신성과 실현 가능성 자동 평가 메커니즘 고도화


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 3.5/5
- Overall: 4/5

**총평**: 본 논문은 온톨로지 지식 그래프, LLMs, 다중 에이전트 시스템을 통합하여 과학 발견을 자동화하는 혁신적 접근을 제시하며, 생물 영감 재료 분야에서 의미 있는 성과를 도출했으나, 생성된 가설의 실험적 검증과 더 광범위한 도메인 적용에 대한 추가 연구가 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/777_Structuring_scientific_innovation_A_framework_for_modeling_a/review]] — 과학적 발견 자동화라는 공통 목표를 가지지만 다중 에이전트 시스템과 구조적 혁신 모델링이라는 다른 접근법을 사용한다.
- 🔗 후속 연구: [[papers/794_The_AI_Scientist-v2_Workshop-Level_Automated_Scientific_Disc/review]] — AI 과학자의 워크샵 수준 자동화된 과학적 발견을 생물 영감 재료 분야로 확장 적용한 사례이다.
- 🏛 기반 연구: [[papers/134_Automating_the_practice_of_science_Opportunities_challenges/review]] — 과학 실무 자동화의 기회와 도전에 대한 종합적 검토가 SciAgents 프레임워크 개발의 이론적 배경을 제공한다.
- 🔄 다른 접근: [[papers/777_Structuring_scientific_innovation_A_framework_for_modeling_a/review]] — 과학적 혁신을 모델링한다는 공통 목표이지만 구조적 재결합 프레임워크와 다중 에이전트 시스템이라는 다른 방법론을 사용한다.
