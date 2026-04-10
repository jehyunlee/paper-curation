---
title: "355_From_Human_Memory_to_AI_Memory_A_Survey_on_Memory_Mechanisms"
authors:
  - "Yaxiong Wu"
  - "Sheng Liang"
  - "Chen Zhang"
  - "Yichao Wang"
  - "Yongyue Zhang"
date: "2025"
doi: "10.48550/arXiv.2504.15965"
arxiv: ""
score: 4.0
essence: "본 논문은 대규모 언어모델(LLM) 기반 AI 시스템의 메모리 메커니즘을 인간의 기억 체계와 비교 분석하여, 객체(personal/system), 형태(parametric/non-parametric), 시간(short-term/long-term) 3개 차원의 8개 사분면 분류 체계를 제시하는 종합 리뷰 논문이다."
tags:
  - "cat/LLM-Based_Scientific_Reasoning"
  - "sub/Large_Language_Model_Agents"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wu et al._2025_From Human Memory to AI Memory A Survey on Memory Mechanisms in the Era of LLMs.pdf"
---

# From Human Memory to AI Memory: A Survey on Memory Mechanisms in the Era of LLMs

> **저자**: Yaxiong Wu, Sheng Liang, Chen Zhang, Yichao Wang, Yongyue Zhang | **날짜**: 2025 | **DOI**: [10.48550/arXiv.2504.15965](https://doi.org/10.48550/arXiv.2504.15965)

---

## Essence

본 논문은 대규모 언어모델(LLM) 기반 AI 시스템의 메모리 메커니즘을 인간의 기억 체계와 비교 분석하여, 객체(personal/system), 형태(parametric/non-parametric), 시간(short-term/long-term) 3개 차원의 8개 사분면 분류 체계를 제시하는 종합 리뷰 논문이다.

## Motivation

- **Known**: 기존 연구들은 LLM의 메모리 메커니즘을 시간 차원(단기/장기 기억)으로만 분류하여 설명하고 있으며, 메모리 강화 AI 시스템(예: ChatGPT Memory, MemoryBank)들이 상용화되고 있음
  
- **Gap**: 인간의 기억 체계와 LLM 기반 AI 시스템의 메모리 간의 체계적인 관계 분석 부재; 객체와 형태 차원을 포함한 다차원 분류 체계의 부족
  
- **Why**: LLM 기반 AI가 사용자 개인화(personal memory)와 복잡한 작업 수행(system memory)을 모두 요구하며, 인간의 기억 과학에서 영감을 받은 더 강력한 메모리 시스템 설계 필요
  
- **Approach**: 신경과학 기반 인간 기억 체계 분석 → AI 메모리와의 대응 관계 수립 → 3차원 8사분면 분류 체계 제시 → 개인 메모리와 시스템 메모리 관련 연구 종합 → 미해결 과제 및 향후 방향 제시

## Achievement

![Figure 1: Illustrating the parallels between human and AI memory.](figures/fig1.webp)
*인간의 기억과 AI 메모리 간의 대응 관계를 시각화한 그림*

1. **인간-AI 메모리 대응 프레임워크**: 인간의 기억(단기/장기, 감각/작업, 외현/내현 기억)과 AI 메모리(개인/시스템, 매개변수/비매개변수, 단기/장기)의 체계적 매핑 관계 확립

2. **다차원 분류 체계**: 객체(personal vs. system) × 형태(parametric vs. non-parametric) × 시간(short-term vs. long-term)의 3개 축으로 8개 사분면(quadrant) 메모리 분류 체계 제시, 기존의 시간 차원만의 분류를 확장

3. **개인 메모리 연구 종합**: 사용자 프로필(user profile), 상호작용 이력(interaction history), 선호도 학습(preference learning) 등 AI 시스템의 개인화 능력 향상을 위한 연구들을 체계적으로 정리

4. **시스템 메모리 연구 종합**: 계획(planning), 추론(reasoning), 도구 사용(tool use), 중간 결과 저장 등 복잡한 작업 수행을 위한 메모리 메커니즘 분석

5. **미해결 과제 및 향후 방향 제시**: 메모리 용량 제한, 검색 효율성, 메모리 망각(forgetting), 개인정보 보호, 메모리 일관성 등의 개방 문제 식별

## How

- **인간 기억 체계 분석**: Multi-Store Model(Atkinson-Shiffrin) 기반으로 단기 기억(sensory memory, working memory)과 장기 기억(explicit/declarative, implicit/non-declarative memory) 상세 설명

- **AI 메모리 특성 규정**: 
  - 객체: 개인 메모리(사용자 정보, 상호작용 기록)와 시스템 메모리(중간 결과, 추론 과정)
  - 형태: 매개변수 메모리(모델 가중치에 인코딩)와 비매개변수 메모리(외부 문서 저장소)
  - 시간: LLM의 컨텍스트 윈도우 제한을 극복하기 위한 단기/장기 구분

- **메모리 메커니즘 카테고리화**: 
  - 검색 기반 접근(retrieval-based): 관련 기억 동적 검색
  - 적응적 업데이트(adaptive updating): 상호작용을 통한 지속적 진화
  - 개인 적응(personalization): 사용자 특성 학습 및 반영

- **메모리 강화 AI 시스템 사례 분석**: MemoryBank, ChatGPT Memory, Apple Personal Context, mem0, MemoryScope 등 실제 구현 사례를 통한 실증적 검토

## Originality

- **새로운 분류 체계**: 기존의 단순 시간 차원 분류에서 객체(개인/시스템)와 형태(매개변수/비매개변수)를 추가한 다차원 8사분면 분류 체계는 메모리 연구의 포괄성을 획기적으로 확장

- **학제적 통합 관점**: 신경과학의 인간 기억 모델과 LLM 기반 AI 메모리를 체계적으로 연결하여, 인간 뇌의 메모리 메커니즘이 AI 설계에 주는 영감을 명시적으로 도출

- **문제 중심적 조직화**: 개인화 능력 향상과 복잡 작업 수행이라는 실제 AI 시스템의 두 가지 핵심 요구사항을 기축으로 메모리 연구를 조직화하여 실무적 관련성 강조

- **미래 연구 방향 제시**: 메모리 용량, 검색 효율성, 망각 메커니즘, 보안/프라이버시 등 미해결 과제를 명확히 식별하여 향후 연구 의제를 제시

## Limitation & Further Study

- **경험적 평가 부재**: 논문이 리뷰 성격이므로 각 메모리 메커니즘의 성능을 직접 비교 평가하는 실증적 벤치마크 실험이 부재

- **메모리 통합 메커니즘 미흡**: 개인 메모리와 시스템 메모리 간의 상호작용 및 통합 방식에 대한 심화 논의 필요

- **인간 기억과의 대응 심화 필요**: 인간의 망각(forgetting)과 재통합(reconsolidation) 현상 등 더 복잡한 기억 과정이 AI에 어떻게 적용될 수 있는지에 대한 탐구 부재

- **후속 연구 방향**:
  - 메모리 효율성과 검색 속도의 균형을 맞추는 최적화 알고리즘 개발
  - 개인정보 보호를 고려한 메모리 암호화 및 접근 제어 메커니즘
  - 메모리 망각과 우선순위 관리를 모방한 동적 메모리 할당 전략
  - 다중 메모리 시스템 간의 상호 강화(synergy) 메커니즘 연구

## Evaluation

- **Novelty**: 4/5 - 3차원 분류 체계와 인간-AI 대응 프레임워크는 신선하나, 개별 메모리 메커니즘은 기존 연구의 종합

- **Technical Soundness**: 4/5 - 신경과학 이론 기반이 견고하고 AI 응용이 명확하지만, 형식적 수학 모델링이 부재

- **Significance**: 4/5 - LLM 시대의 메모리 연구에 체계적 틀을 제공하여 학계에 기여할 잠재력이 높음

- **Clarity**: 4/5 - 전반적으로 명확한 구성이지만, 8개 사분면 간의 경계와 중복을 더 명확히 할 필요

- **Overall**: 4/5

**총평**: 본 논문은 LLM 시대의 메모리 메커니즘을 인간 기억과 연결하며 다차원 분류 체계를 제시하여, 메모리 강화 AI 시스템 연구에 유용한 개념적 틀과 연구 의제를 제공하는 가치 있는 리뷰 논문이다. 다만 실증적 벤치마킹과 형식적 모델링을 추가하면 더욱 강화될 수 있을 것으로 판단된다.

## Related Papers

- 🔗 후속 연구: [[papers/039_A-MEM_Agentic_Memory_for_LLM_Agents/review]] — 인간 기억 체계를 LLM 에이전트 메모리로 확장한 연구를 에이전틱 메모리로 발전
- 🧪 응용 사례: [[papers/400_Hiagent_Hierarchical_working_memory_management_for_solving_l/review]] — 인간-AI 메모리 비교 연구를 계층적 작업 메모리 관리로 구현한 응용
- 🔄 다른 접근: [[papers/412_HuggingGPT_Solving_AI_Tasks_with_ChatGPT_and_its_Friends_in/review]] — 메모리 메커니즘 서베이 vs 계층적 메모리 관리로 서로 다른 메모리 연구 접근
- 🔗 후속 연구: [[papers/681_Revisiting_Gene_Ontology_Knowledge_Discovery_with_Hierarchic/review]] — AI 메모리 메커니즘을 Gene Ontology 지식 발견으로 확장한 생물정보학 응용
- 🏛 기반 연구: [[papers/400_Hiagent_Hierarchical_working_memory_management_for_solving_l/review]] — 인간 메모리에서 AI 메모리로의 전환 연구가 작업 메모리 설계의 기초가 됨
- 🏛 기반 연구: [[papers/412_HuggingGPT_Solving_AI_Tasks_with_ChatGPT_and_its_Friends_in/review]] — 인간 메모리에서 AI 메모리로의 메커니즘 연구가 계층적 작업 메모리 관리의 인지과학적 기반을 제공한다.
- 🔄 다른 접근: [[papers/039_A-MEM_Agentic_Memory_for_LLM_Agents/review]] — A-MEM의 동적 에이전트 메모리와 From Human Memory to AI Memory는 모두 AI 메모리 시스템을 다루지만, 젯엘카스텐 방법론과 인간-AI 메모리 비교라는 서로 다른 접근법을 취합니다.
