---
title: "157_Beyond_outlining_Heterogeneous_recursive_planning_for_adapti"
authors:
  - "Ruibin Xiong"
  - "Yimeng Chen 외"
date: "2025"
doi: "10.48550/arXiv.2503.08275"
arxiv: ""
score: 4.0
essence: "기존의 사전 계획(pre-writing planning) 기반 접근법의 경직성을 극복하기 위해, 본 논문은 검색(Retrieval), 추론(Reasoning), 작성(Composition) 세 가지 인지 과제를 동적으로 통합하는 이질적 재귀적 계획(Heterogeneous Recursive Planning) 프레임워크를 제시한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Multi-Agent_Language_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Miraglia_2025_Beyond outlining Heterogeneous recursive planning for adaptive long-form writing with language mode.pdf"
---

# Beyond outlining: Heterogeneous recursive planning for adaptive long-form writing with language models

> **저자**: Ruibin Xiong, Yimeng Chen 외 | **날짜**: 2025 | **DOI**: [10.48550/arXiv.2503.08275](https://doi.org/10.48550/arXiv.2503.08275)

---

## Essence

![Figure 1](figures/fig1.webp) *WriteHERE 프레임워크: 재귀적 과제 분해와 상태 기반 계층적 스케줄링을 통한 적응형 장문 작성*

기존의 사전 계획(pre-writing planning) 기반 접근법의 경직성을 극복하기 위해, 본 논문은 검색(Retrieval), 추론(Reasoning), 작성(Composition) 세 가지 인지 과제를 동적으로 통합하는 이질적 재귀적 계획(Heterogeneous Recursive Planning) 프레임워크를 제시한다.

## Motivation

- **Known**: 최근 장문 작성 연구들은 개요 생성 후 순차적으로 콘텐츠를 작성하는 사전 계획 단계(pre-writing planning)를 도입하여 일정한 성과를 거두었음 (STORM, Agent's Room, Plan-Write 등)

- **Gap**: 고정된 개요와 정해진 작업 순서는 작성 중 발생하는 동적 요구사항(예: 미스터리 소설에서 중간에 새로운 플롯 발견)에 대응하기 어려우며, 기존 방법들은 특정 시나리오에 최적화되어 일반화 능력이 부족함

- **Why**: 실제 인간의 작문 과정은 고정된 순서를 따르지 않으며, 작성 중 검색, 추론, 작성이 필수적으로 상호작용하면서 적응적으로 진행됨

- **Approach**: 계층적 과제 네트워크 계획(HTN: Hierarchical Task Network Planning)에서 영감을 얻어, 장문 작성을 이질적 과제들의 동적 조합으로 공식화하고, 상태 기반 계층적 스케줄링을 통해 과제 실행과 계획을 상호교차(interleave)시키는 방식 제시

## Achievement

![Figure 2](figures/fig2.webp) *세 가지 과제 유형의 정보 흐름: 검색(메모리만 수정), 추론(메모리 간 변환), 작성(작업공간 수정)*

1. **통합 프레임워크**: 개요 작성과 콘텐츠 생성을 분리된 단계가 아닌 단일 목표 지향적 계획 프레임워크로 통합하여, 다양한 장문 작성 작업(소설, 기술 보고서)에 일반화 가능한 접근법 달성

2. **실증적 성능 향상**: 픽션 작성(TELL ME A STORY) 및 기술 문서 생성(Wildseed) 벤치마크에서 기존 최신 기법들을 모든 자동 평가 지표에서 능가

3. **적응성 증대**: 작성 과제의 복잡도에 따라 계획 깊이를 동적으로 조정하고, 과제 실행 중 필요한 순간에 새로운 검색, 추론을 즉시 수행 가능

## How

- **이질적 재귀적 분해(Heterogeneous Recursive Decomposition)**: 복잡한 작성 목표를 세 가지 인지 과제 유형(검색, 추론, 작성) 범주에서 원시 부과제(primitive subtasks)로 재귀적으로 분해하되, 각 분해 단계에서 과제 유형을 명시적으로 지정

- **상태 기반 계층적 과제 스케줄링 알고리즘**: 과제와 의존성을 방향성 비순환 그래프(DAG: Directed Acyclic Graph)로 표현하고, 과제의 상태(Active, Silent, Suspend 등)를 관리하여 계층적이고 의존성 기반의 실행 논리 보장

- **계획-실행 상호교차**: 원시 과제에 도달하면 즉시 실행하고, 모든 의존 과제의 상태를 업데이트한 후 다음 과제 노드로 진행하는 방식으로 유연한 적응 가능

- **작성 에이전트 시스템 공식화**: 에이전트 핵심(A), 내부 메모리(M), 데이터베이스(D), 작업공간(W)으로 구성하는 형식적 정의를 통해 시스템의 정보 흐름 명확화

## Originality

- **과제 유형 명시화**: 기존 재귀적 분해 연구들(예: ADaPT)은 주로 추론 과제에 초점을 맞췄으나, 본 연구는 검색, 추론, 작성의 이질적 과제들의 서로 다른 정보 흐름 패턴을 명시적으로 모델링

- **계획 문제로의 재정의**: 장문 작성을 목표 달성 문제가 아닌 HTN 기반의 원시 과제 실행 문제로 새롭게 공식화하여, 기존의 사전 계획-순차 실행 패러다임과 본질적으로 다른 패러다임 제시

- **일반화 가능한 설계**: 특정 시나리오(소설 or 보고서)에 맞춘 경직된 워크플로우 대신, 두 가지 이상의 서로 다른 장문 작성 작업에 적용 가능한 범용 프레임워크 구현

- **형식적 정의**: 작성 에이전트 시스템, 세 가지 과제 유형, 계획 문제를 수학적으로 명확히 정의하여 재현성과 확장성 강화

## Limitation & Further Study

- **계산 비용**: 재귀적 분해와 DAG 기반 스케줄링으로 인한 추가 LLM 호출 비용이 명시적으로 분석되지 않으며, 특히 깊은 분해 계층에서의 효율성 개선 방안이 필요

- **과제 유형 자동 판별**: 현재는 과제 유형을 명시적으로 지정하는 방식이며, 향후 LLM이 상황에 맞게 최적의 과제 유형을 자동으로 결정하는 메커니즘 개발 필요

- **메모리 관리**: 장문 작성 시 메모리(M)에 축적되는 정보량이 증가하면서 LLM의 컨텍스트 윈도우 제약에 직면할 가능성이 있으며, 효율적인 메모리 압축 또는 검색 메커니즘 연구 필요

- **벤치마크 확대**: 현재 두 가지 작업(소설, 보고서)에만 평가되었으며, 학술 논문, 장편 저널리즘, 교과서 등 더 다양한 장문 작성 도메인에서의 성능 검증 필요

- **사람 평가**: 자동 평가 지표 중심이며, 정성적 평가(일관성, 적응성, 창의성 등)의 인간 평가가 보강되어야 함

## Evaluation

- **Novelty (독창성)**: 4/5 — 이질적 과제 유형의 명시화와 HTN 기반 재공식화는 참신하나, 재귀적 분해 자체는 이전 연구에 기초함

- **Technical Soundness (기술적 건전성)**: 4/5 — 형식적 정의와 알고리즘 설계가 명확하나, 실제 구현 세부사항(상태 전이, 메모리 관리)에 대한 상세 설명 부족

- **Significance (중요도)**: 4/5 — 장문 작성의 실질적 한계를 정확히 지적하고 일반화 가능한 해결책을 제시하나, 아직 제한된 도메인에서만 검증됨

- **Clarity (명확성)**: 4/5 — 공식적 정의와 Figure가 잘 구성되어 있으나, Figure 1의 상태 전이(Finish, Suspend, Active 등)에 대한 상세 설명 필요

- **Overall (종합)**: 4/5

**총평**: WriteHERE는 기존의 경직된 사전 계획 방식에서 벗어나 검색, 추론, 작성을 동적으로 통합하는 이질적 재귀적 계획 프레임워크를 제시함으로써, 장문 작성의 적응성 문제에 대한 진정한 해결책을 제공한다. 형식적 공식화와 실증적 성능 향상이 강점이나, 계산 비용 분석과 더 광범위한 도메인 검증이 향후 필요하다.

## Related Papers

- 🏛 기반 연구: [[papers/833_Towards_reasoning_era_A_survey_of_long_chain-of-thought_for/review]] — 이질적 재귀적 계획의 장문 생성은 긴 추론 사슬 서베이에서 분석된 추론 시대의 방법론적 기반 위에 검색-추론-작성 통합 프레임워크를 구축합니다.
- 🧪 응용 사례: [[papers/876_What_are_the_essential_factors_in_crafting_effective_long_co/review]] — 동적 인지 과제 통합 프레임워크는 효과적인 긴 맥락 제작 연구에서 제시된 요소들을 실제 학술 글쓰기 자동화에 적용하여 맥락 인식 생성을 실현합니다.
