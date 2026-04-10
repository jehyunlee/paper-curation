---
title: "577_Nova_An_iterative_planning_and_search_approach_to_enhance_no"
authors:
  - "Xiang Hu"
  - "Hongyu Fu"
  - "Jinge Wang"
  - "Yifeng Wang"
  - "Zhikun Li"
date: "2024"
doi: "N/A"
arxiv: ""
score: 4.2
essence: "LLM의 연구 아이디어 생성 능력을 향상시키기 위해 반복적인 계획 수립과 지식 검색을 결합한 Nova 프레임워크를 제안한다. 이 방법은 기존 접근법 대비 새로운 아이디어 생성을 3.4배, 상위 평가 아이디어를 2.5배 이상 증가시킨다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/Multi-Hop_Reasoning_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Hu et al._2024_Nova An iterative planning and search approach to enhance novelty and diversity of llm generated id.pdf"
---

# Nova: An iterative planning and search approach to enhance novelty and diversity of llm generated ideas

> **저자**: Xiang Hu, Hongyu Fu, Jinge Wang, Yifeng Wang, Zhikun Li, Renjun Xu, Yu Lu, Yaochu Jin, Lu Pan, Zhenzhong Lan | **날짜**: 2024 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)
*좌측: 다른 최신 기법들과의 성능 비교. 우측: 반복 단계별 생성된 고유한 새로운 아이디어의 수 증가 추이*

LLM의 연구 아이디어 생성 능력을 향상시키기 위해 반복적인 계획 수립과 지식 검색을 결합한 Nova 프레임워크를 제안한다. 이 방법은 기존 접근법 대비 새로운 아이디어 생성을 3.4배, 상위 평가 아이디어를 2.5배 이상 증가시킨다.

## Motivation

- **Known**: 최근 LLM들이 수학 문제 해결, 증명, 코드 생성 등에서 우수한 성능을 보이고 있으며, 과학 연구 아이디어 생성에도 활용되고 있다. Si et al. (2024)는 LLM이 생성한 아이디어가 인간 전문가보다 더 새롭다고 보였다.

- **Gap**: 기존 LLM 기반 아이디어 생성 방법들은 제한된 지식 수집 범위와 방향성 부족으로 인해 반복적이고 동일한 아이디어를 생성하는 다양성 부족 문제를 보인다. 기존의 개체(entity) 및 키워드 기반 검색은 목표지향적이지 않아 혁신을 촉진하지 못한다.

- **Why**: 어떤 지식을 검색할 것인가를 결정하는 것이 중요하다. 단순한 검색 전략으로는 혁신에 필요한 최적의 외부 지식을 획득할 수 없다.

- **Approach**: 초기 시드 아이디어 생성 후, 반복적으로 계획을 수립하여 검색 범위를 확장하고, 새로운 지식을 기반으로 아이디어를 개선하고 상세화하는 3단계 파이프라인을 제안한다.

## Achievement

![Figure 2](figures/fig2.webp)
*Nova 파이프라인: 초기 시드 아이디어 생성 → 반복적 개선 → 아이디어 완성의 3단계 구성*

1. **높은 정량적 성과**: 170개 상위 학회 논문(ACL, ICLR, CVPR)을 대상으로 Swiss Tournament Score 5를 받은 아이디어가 기존 최신 방법 대비 2.5배 이상 증가했으며, 고유한 새로운 아이디어는 3.4배 증가.

2. **우수한 질적 평가**: 자동 평가(Swiss Tournament)와 인간 평가 모두에서 아이디어의 새로움(novelty)과 다양성(diversity)이 크게 향상됨을 입증.

3. **반복 효과 검증**: 반복 단계가 진행될수록 새로운 아이디어의 비중이 점진적으로 증가함을 시각화하여 입증.

## How

![Figure 3](figures/fig3.webp)
*계획 기반 반복 시드 아이디어 생성 프로세스 예시*

### 초기 시드 아이디어 생성 (Initial Seed Idea Generation)
- 입력 논문의 참고문헌과 최신 출판물을 활용한 다중 소스 기반 지식 추적
- 10가지 기본 과학 발견 방법론(Kuhn의 패러다임 기반)을 이용한 다양한 관점의 아이디어 생성
  - 예: 기존 접근법의 이상(anomaly) 분석, 문제점 파악 등
- 자기수정 메커니즘(self-check, self-critique, reflection) 적용으로 환각 억제 및 논리성 보장
- 각 입력 논문당 15개의 시드 아이디어 생성

### 반복적 계획과 검색 (Iterative Planning and Search)
- **계획 수립**: LLM이 현재 아이디어 풀을 분석하여 추가 지식 획득을 위한 핵심 분야 식별
- **맥락 학습(In-context Learning)**: LLM의 내부 지식을 활용하여 새로운 아이디어에 유용한 지식 결정
- **새 시드 아이디어 생성**: 검색된 논문 + 기존 아이디어 + 입력 논문을 기반으로 각 아이디어당 10개 생성 후 자기 성찰을 통해 3개로 축약
- **반복 효과**: 각 반복에서 기존 시드 아이디어를 새로운 아이디어로 교체하여 검색 범위를 점진적으로 확장
- T 단계 반복 수행

### 최종 아이디어 완성 (Output Idea Generation)
- T번 반복 후의 최종 시드 아이디어 풀을 상세한 방법론으로 확장
- 각 아이디어에 더 자세한 기술적 세부사항 추가

## Originality

- **계획 수립의 도입**: 기존 연구에서는 외부 환경과의 상호작용이 미흡했으나, 본 연구는 **처음으로 과학 연구 작업에 계획 수립 방법론을 통합**
- **목표 지향적 지식 검색**: 전통적인 개체/키워드 기반 검색을 넘어 **LLM의 추론 능력을 활용한 목표 지향적 검색 방식** 제안
- **다중 과학 발견 방법론 통합**: Kuhn의 패러다임을 바탕으로 한 10가지 과학 발견 방법론을 체계적으로 적용
- **반복적 개선 메커니즘**: 각 반복에서 기존 아이디어를 새로운 아이디어로 교체하여 **점진적이고 깊이 있는 탐색(depth-first exploration)** 가능
- **다층적 품질 보증**: 초기 생성, 중간 개선, 최종 완성 단계에서 자기수정 기법 적용으로 품질 보장

## Limitation & Further Study

### 한계
- **평가 방법의 제한**: Swiss Tournament Score와 인간 평가는 여전히 주관적 판단에 의존하며, 더 객관적인 평가 지표 필요
- **계산 비용**: 반복적 계획과 검색으로 인한 높은 계산 비용 및 LLM 호출 횟수 증가는 실제 활용 시 비용 문제 야기
- **검색 범위 최적화 미흡**: T(반복 횟수)의 최적값 결정 방법이 명확하지 않으며, 과도한 반복의 수렴성 분석 부재
- **도메인 일반화**: LLM 관련 논문(170개)으로만 평가되어 다른 과학 분야(생물학, 화학, 물리학 등)에서의 성능 미검증
- **시드 아이디어의 초기 다양성**: 초기 15개 시드 아이디어의 품질이 최종 결과에 미치는 영향도 미분석

### 후속 연구 방향
- 더 다양한 과학 분야와 대규모 논문 집합에 대한 평가 수행
- 반복 횟수 결정을 위한 자동 종료 조건 개발
- 계산 효율성 개선을 위한 경량화된 계획 수립 방식 연구
- LLM 기반 평가와 인간 평가 간의 일관성 개선 방법 탐구
- 다양한 LLM 모델(GPT, Claude, Llama 등)에서의 성능 비교 분석

## Evaluation

- **Novelty**: 4.5/5 
  - 반복적 계획과 검색을 통한 새로운 관점 도입이 충분히 참신함. 다만 과학 발견 방법론 자체가 기존 이론에 기반한 것으로, 완전한 혁신성은 제한적

- **Technical Soundness**: 4/5
  - 파이프라인의 각 단계가 논리적이고 자기수정 메커니즘을 통한 품질 보증이 우수함. 그러나 반복 횟수 최적화, 수렴성 분석 등 기술적 깊이가 다소 부족함

- **Significance**: 4.5/5
  - LLM 기반 연구 아이디어 생성의 실질적인 성과 달성(2.5~3.4배 향상)으로 높은 실용성 제시. 다만 평가 대상이 LLM 논문에 제한되어 일반화 가능성은 불완전

- **Clarity**: 4/5
  - 파이프라인과 전체 프로세스가 명확하게 설명되었고, Figure 3의 구체적 예시가 이해를 돕음. 다만 일부 기술적 세부사항(정확한 prompt 구성, 하이퍼파라미터 선택 근거 등)이 부족

- **Overall**: 4.2/5

**총평**: Nova는 반복적 계획과 목표 지향적 지식 검색을 결합하여 LLM 기반 아이디어 생성의 새로움과 다양성을 크게 향상시키는 실질적으로 효과적인 방법론이다. 다만 평가 범위의 제한, 계산 비용, 그리고 타 분야에서의 일반화 가능성 검증이 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/509_Llms_can_realize_combinatorial_creativity_generating_creativ/review]] — 조합적 창의성 이론과 반복적 계획 수립은 모두 연구 아이디어 생성을 위한 서로 다른 체계적 접근법입니다
- 🔗 후속 연구: [[papers/668_ResearchAgent_Iterative_Research_Idea_Generation_over_Scient/review]] — ResearchAgent의 반복적 연구 아이디어 생성은 Nova 프레임워크의 계획 수립과 검색 결합 방식을 더욱 발전시킨 형태입니다
- 🧪 응용 사례: [[papers/494_Liveideabench_Evaluating_llms_scientific_creativity_and_idea/review]] — LiveIdeaBench의 과학적 창의성 평가는 Nova가 생성한 새로운 아이디어의 품질을 측정하는 실제 응용 플랫폼입니다
- 🔄 다른 접근: [[papers/509_Llms_can_realize_combinatorial_creativity_generating_creativ/review]] — Nova의 반복적 계획 수립과 조합적 창의성 이론은 모두 연구 아이디어 생성을 위한 서로 다른 체계적 접근법입니다
- 🧪 응용 사례: [[papers/366_Futuregen_Llm-rag_approach_to_generate_the_future_work_of_sc/review]] — Nova의 반복적 계획과 지식 검색으로 생성된 연구 아이디어는 FutureGen의 미래 연구 방향 자동 생성에 직접 활용될 수 있습니다
- 🔗 후속 연구: [[papers/854_Understanding_the_planning_of_LLM_agents_A_survey/review]] — 반복적 계획과 검색을 통한 추론 향상이 LLM 에이전트 계획 수립의 구체적인 확장 방법이다.
- 🔄 다른 접근: [[papers/469_Large_Language_Models_as_Evolutionary_Optimizers/review]] — 조합 최적화에서 LLM 기반 진화 알고리즘과 반복적 계획 및 탐색 접근법을 비교할 수 있습니다.
