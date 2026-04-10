---
title: "039_A-MEM_Agentic_Memory_for_LLM_Agents"
authors:
  - "Wujiang Xu"
  - "Zujie Liang"
  - "Kai Mei"
  - "Hang Gao"
  - "Juntao Tan"
date: "2025"
doi: "10.48550/arXiv.2502.12110"
arxiv: ""
score: 4.0
essence: "본 논문은 LLM 에이전트를 위한 동적 에이전트 메모리 시스템 A-MEM을 제안하며, 젯엘카스텐(Zettelkasten) 방법론의 원리를 기반으로 새로운 메모리가 추가될 때 자동으로 문맥적 연결을 생성하고 기존 메모리를 진화시키는 메커니즘을 구현했다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Multi-Agent_Language_Systems"
  - "topic/ai4s"
---

# A-MEM: Agentic Memory for LLM Agents

> **저자**: Wujiang Xu, Zujie Liang, Kai Mei, Hang Gao, Juntao Tan | **날짜**: 2025 | **DOI**: [10.48550/arXiv.2502.12110](https://doi.org/10.48550/arXiv.2502.12110)

---

## Essence

![Figure 1](figures/fig1.webp)
*전통적 메모리 시스템은 미리 정의된 메모리 접근 패턴을 요구하는 반면, A-MEM은 동적 메모리 연산을 가능하게 함*

본 논문은 LLM 에이전트를 위한 동적 에이전트 메모리 시스템 A-MEM을 제안하며, 젯엘카스텐(Zettelkasten) 방법론의 원리를 기반으로 새로운 메모리가 추가될 때 자동으로 문맥적 연결을 생성하고 기존 메모리를 진화시키는 메커니즘을 구현했다.

## Motivation

- **Known**: 기존 LLM 에이전트 메모리 시스템(MemGPT, SCM 등)은 기본적인 저장 및 검색 기능을 제공하며, Mem0와 같은 최신 시스템도 그래프 데이터베이스를 활용하여 구조화된 조직을 시도하고 있음
- **Gap**: 현존 시스템들은 미리 정의된 스키마(schema)와 고정된 워크플로우에 의존하여 새로운 지식 패턴의 발견과 동적 조직화에 실패하며, 장기 상호작용과 다양한 환경 적응에 취약함
- **Why**: LLM 에이전트가 복잡한 개방형 작업을 수행할수록 유연한 지식 조직화와 지속적인 적응이 필수적이므로, 사전 정의 없이 동적으로 작동하는 범용 메모리 시스템이 필요함
- **Approach**: 젯엘카스텐 방법의 원자적 노트(atomic note) 원리와 유연한 연결 메커니즘을 LLM 기반의 에이전트 메모리 아키텍처로 구현하여 자율적 노트 생성, 동적 링크 형성, 메모리 진화를 가능하게 함

## Achievement

![Figure 2](figures/fig2.webp)
*A-MEM 아키텍처: 노트 구성, 링크 생성, 메모리 진화의 3단계 과정을 통해 상호연결된 메모리 네트워크 형성*

1. **동적 메모리 구조화**: 미리 정의된 메모리 연산 없이 에이전트가 자율적으로 메모리를 조직화하고 진화시킬 수 있는 아젠틱 메모리 시스템 구현
2. **메모리 업데이트 메커니즘**: 새로운 메모리 추가 시 링크 생성(link generation)과 메모리 진화(memory evolution) 두 가지 핵심 연산이 자동으로 작동하여 기존 메모리의 문맥 표현을 동적으로 적응시킴
3. **실증적 성능 개선**: 6개 파운데이션 모델(foundation model)을 대상으로 장기 대화 데이터셋에서 6가지 평가 지표로 기존 SOTA 대비 현저한 성능 향상 달성

## How

![Figure 2](figures/fig2.webp)

### 노트 구성 (Note Construction)
- 각 메모리 노트 $m_i = \{c_i, t_i, K_i, G_i, X_i, e_i, L_i\}$로 표현
  - $c_i$: 원본 상호작용 콘텐츠
  - $t_i$: 타임스탬프
  - $K_i$: LLM 생성 키워드(주요 개념)
  - $G_i$: LLM 생성 태그(분류)
  - $X_i$: LLM 생성 문맥 설명(풍부한 의미론적 이해)
  - $e_i$: 텍스트 인코더를 통한 밀집 벡터 표현
  - $L_i$: 연결된 메모리 집합

- LLM 프롬프트 템플릿 $P_{s1}$을 통해 의미론적 성분 자동 추출
- 모든 텍스트 성분 연결(concatenation) 후 인코딩: $e_i = f_{enc}[\text{concat}(c_i, K_i, G_i, X_i)]$

### 링크 생성 (Link Generation)
- 코사인 유사도를 통한 상위-k 유사 메모리 검색
  - 유사도: $s_{n,j} = \frac{e_n \cdot e_j}{|e_n||e_j|}$
  - 후보 집합: $M_n^{\text{near}} = \{m_j | \text{rank}(s_{n,j}) \leq k\}$

- LLM이 후보 메모리들의 잠재적 공통 속성 분석하여 의미 있는 연결 자동 형성
- 임베딩 기반 검색으로 확장성 확보하면서도 LLM의 뉘앙스 있는 관계 파악 가능

### 메모리 진화 (Memory Evolution)
- 새로운 메모리 추가 시 기존 메모리의 문맥 표현 및 속성이 자동으로 업데이트
- 고차 패턴(higher-order pattern)의 자동 발현으로 메모리 네트워크가 지속적으로 이해를 정교화

## Originality

- **젯엘카스텐 원리의 현대적 응용**: 전통적 지식관리 방법론을 LLM 기반 에이전트 메모리에 처음 적용하여 원자적 노트와 유연한 연결 메커니즘 구현
- **에이전트 수준의 메모리 동작성(agency)**: 기존 에이전트 RAG(Retrieval-Augmented Generation)가 검색 단계의 자율성만 제공하는 것과 달리, A-MEM은 메모리 저장과 진화 단계에서의 근본적 자율성 실현
- **메모리 진화 개념의 도입**: 새로운 경험이 기존 메모리의 구조와 의미론적 표현을 자동으로 업데이트하는 동적 적응 메커니즘은 기존 정적 메모리 시스템과의 명확한 차별점
- **LLM과 임베딩의 하이브리드 접근**: 임베딩 기반 효율성과 LLM 기반 의미론적 정교함을 결합하여 확장성과 정확성 동시 달성

## Limitation & Further Study

- **계산 비용**: 새 메모리 추가마다 LLM 호출이 3회(노트 구성, 링크 생성, 진화 분석) 필요하여 실시간 시스템에서 지연 발생 가능성
- **메모리 크기 제약**: 논문에서 평가한 데이터셋 규모와 매우 큰 메모리 저장소에서의 확장성 검증 부족
- **링크 관계성의 평가**: 자동 생성된 링크의 의미론적 적절성을 정량적으로 평가하는 지표 부재
- **메모리 진화의 제어**: 메모리 진화가 무한정 반복될 수 있는지, 수렴 조건이 명확하지 않음
- **후속 연구 방향**:
  - 다중 모달(multi-modal) 메모리 지원으로 시각 정보 포함
  - 메모리 압축 및 통합 메커니즘으로 장기 메모리의 효율성 개선
  - 강화학습을 통한 링크 생성 및 진화 정책의 최적화
  - 사용자 정의 가능한 메모리 조직화 규칙 도입

## Evaluation

- **Novelty**: 4.5/5
  - 젯엘카스텐 기반 에이전트 메모리는 창의적이나, 개별 기술(LLM 프롬프팅, 임베딩 유사도)의 조합 성격이 강함

- **Technical Soundness**: 4/5
  - 핵심 알고리즘(노트 구성, 링크 생성)은 명확하나 메모리 진화의 구체적 메커니즘과 수렴성 증명 부족

- **Significance**: 4/5
  - LLM 에이전트의 장기 상호작용 문제에 실질적 기여하며 6개 모델에서 일관된 개선 보여주나, 평가 데이터셋의 다양성(주로 대화) 제한적

- **Clarity**: 4/5
  - 전반적으로 구조가 명확하고 그림 설명이 도움이 되나, 메모리 진화 과정의 상세 알고리즘과 프롬프트 템플릿 공개 부족

- **Overall**: 4/5

**총평**: A-MEM은 LLM 에이전트의 메모리 문제에 대한 창의적이고 실용적인 해결책을 제시하며, 젯엘카스텐 원리의 현대적 적용과 메모리 진화라는 개념이 의미 있으나, 계산 효율성, 메모리 진화의 이론적 기반, 그리고 평가의 폭을 넓힐 필요가 있다.

## Related Papers

- 🔄 다른 접근: [[papers/355_From_Human_Memory_to_AI_Memory_A_Survey_on_Memory_Mechanisms/review]] — A-MEM의 동적 에이전트 메모리와 From Human Memory to AI Memory는 모두 AI 메모리 시스템을 다루지만, 젯엘카스텐 방법론과 인간-AI 메모리 비교라는 서로 다른 접근법을 취합니다.
- 🔗 후속 연구: [[papers/400_Hiagent_Hierarchical_working_memory_management_for_solving_l/review]] — A-MEM의 문맥적 메모리 연결 시스템은 HiAgent의 계층적 작업 메모리 관리를 확장하여 더 동적이고 진화하는 메모리 구조를 제공합니다.
- 🔗 후속 연구: [[papers/400_Hiagent_Hierarchical_working_memory_management_for_solving_l/review]] — 에이전트 메모리 관리가 계층적 작업 메모리로 구체화되고 발전됨
- 🔗 후속 연구: [[papers/355_From_Human_Memory_to_AI_Memory_A_Survey_on_Memory_Mechanisms/review]] — 인간 기억 체계를 LLM 에이전트 메모리로 확장한 연구를 에이전틱 메모리로 발전
