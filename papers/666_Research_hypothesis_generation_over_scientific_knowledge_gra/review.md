---
title: "666_Research_hypothesis_generation_over_scientific_knowledge_gra"
authors:
  - "Agustín Borrego"
  - "D. Dessí"
  - "Daniel Ayala"
  - "Inma Hernández"
  - "Francesco Osborne"
date: "2025"
doi: "10.1016/j.knosys.2025.113280"
arxiv: ""
score: 4.0
essence: "과학적 지식 그래프(Scientific Knowledge Graphs)를 활용하여 새로운 연구 가설을 자동으로 생성하는 방법론을 제시한다. 특히 대규모 언어모델(LLM)과 구조화된 지식 표현을 결합하여 학제 간 연구 연결과 숨겨진 지식을 발굴하는 접근법을 제안한다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Knowledge_Graph_Reasoning"
  - "topic/ai4s"
---

# Research hypothesis generation over scientific knowledge graphs

> **저자**: Agustín Borrego, D. Dessí, Daniel Ayala, Inma Hernández, Francesco Osborne | **날짜**: 2025 | **DOI**: [10.1016/j.knosys.2025.113280](https://doi.org/10.1016/j.knosys.2025.113280)

---

## Essence

과학적 지식 그래프(Scientific Knowledge Graphs)를 활용하여 새로운 연구 가설을 자동으로 생성하는 방법론을 제시한다. 특히 대규모 언어모델(LLM)과 구조화된 지식 표현을 결합하여 학제 간 연구 연결과 숨겨진 지식을 발굴하는 접근법을 제안한다.

## Motivation

- **Known**: 과학적 발견 과정에서 가설 생성은 필수적이지만 전통적으로 연구자의 직관과 경험에 의존해왔으며, 급증하는 학술 문헌으로 인한 정보 과부하 문제 존재

- **Gap**: 기존의 문헌 기반 발견(Literature-Based Discovery, LBD) 방법들은 학문 간 단편화(disciplinary fragmentation)를 극복하지 못하고 있으며, LLM을 단순히 직접 프롬프팅으로만 활용하는 방식은 생성 가설의 신뢰성과 타당성 검증 부족

- **Why**: 과학적 지식이 구조화된 형태로 표현되어 있는 지식 그래프를 활용하면 더 체계적이고 검증 가능한 가설 생성이 가능할 수 있음

- **Approach**: 지식 그래프 기반의 구조화된 추론(structured reasoning)과 LLM을 통합하여, 개념 간의 명시적 관계성을 활용한 가설 생성 프레임워크 제안

## Achievement

1. **체계적 분류체계 구축**: 인간 중심(Human-Centric), 문헌 기반 발견(LBD), 텍스트 마이닝, 감독학습(Supervised Learning), 그래프 기반(Graph-Based), LLM 기반 방법론으로 구분하여 과학 가설 생성 방법론의 진화 과정을 명확히 제시

2. **LLM 활용 방법론의 다층적 접근**: 직접 프롬프팅(Direct Prompting), 적대적 프롬프팅(Adversarial Prompting), 파인튜닝(Fine-tuning), 검색 증강 생성(RAG: Retrieval-Augmented Generation) 등 다양한 기법을 체계적으로 분류하고 각각의 장단점 분석

3. **지식 그래프와 LLM의 하이브리드 접근**: 지식 그래프의 구조적 명확성과 LLM의 생성 능력을 결합하여 가설의 신뢰성과 창의성을 동시에 확보하는 방법론 제시

4. **평가 전략의 다층화**: 신규성(Novelty), 관련성(Relevance), 실행 가능성(Feasibility), 유의성(Significance), 명확성(Clarity) 등 다각도의 평가 기준 제안

## How

- **지식 그래프 구축**: 과학 문헌에서 개념, 관계, 속성을 추출하여 구조화된 지식 그래프 구성 (예: 질병-유전자-단백질 관계)

- **개념 간 경로 발견**: 그래프 알고리즘을 통해 직접 연결되지 않은 개념들 사이의 중간 경로(intermediate concepts)를 식별하여 "미발견 공개 지식(Undiscovered Public Knowledge)" 발굴

- **LLM 기반 가설 생성**: 
  - 컨텍스트 제공: 식별된 개념 경로와 관련 메타데이터를 LLM에 입력
  - 구조적 생성: 프롬프트를 통해 LLM이 발견한 관계를 기반으로 형식화된 가설 생성
  - 신규성 부스팅: 기존 출판물에 없는 새로운 연결에만 집중하도록 제약

- **다단계 검증**: 생성된 가설에 대해 관련 논문 탐색, 개념적 타당성 검토, 도메인 전문가 평가 수행

- **학제 간 확장**: 여러 과학 도메인의 지식 그래프를 통합하여 기존에 고립된 분야 간 연결점 발견

## Originality

- **지식 그래프의 명시적 활용**: 기존의 암묵적 가정에 기반한 LLM 프롬프팅을 넘어, 명시적 지식 구조를 활용하여 생성 가설의 추적 가능성(traceability)과 해석 가능성(interpretability) 확보

- **하이브리드 방법론**: LBD의 체계성과 LLM의 생성 능력을 결합하는 새로운 패러다임 제시로, 단순 패러프레이징을 벗어난 진정한 혁신적 가설 생성 가능

- **도메인 적응형 평가 프레임워크**: 과학 영역별 특성을 반영한 다층 평가 기준 제안으로, 가설의 질 보증 체계화

- **편향 완화 메커니즘**: 지식 그래프의 구조적 제약이 학습 데이터 편향을 일부 보정하고, 대안적 경로 탐색을 가능하게 함

## Limitation & Further Study

**한계**:
- 지식 그래프의 완성도에 높은 의존성: 누락되거나 부정확한 관계 표현이 생성 가설의 질에 직접 영향
- 평가의 어려움: 생성 가설이 실제로 새로운지, 실험적으로 검증 가능한지 확인하는 자동화 방법 부족
- 도메인 이식성(Transferability) 제한: 생물의학 중심으로 개발되어 다른 과학 분야(물리학, 천문학 등)로의 확장 시 추가 작업 필요
- 설명 가능성 부족: LLM의 생성 과정이 여전히 블랙박스로 남아있어 가설 생성 논리 추적 어려움

**후속 연구**:
- 멀티모달 통합(Multimodal Integration): 이미지, 표, 실험 데이터 등을 포함한 다양한 과학 데이터 소스 통합
- 인간-AI 협력 모델: 연구자와 시스템 간 반복적 상호작용을 통해 가설을 점진적으로 정제하는 상호작용 설계
- 동적 그래프 업데이트: 신규 발표 논문을 실시간으로 반영하여 지식 그래프를 지속적으로 갱신하는 메커니즘
- 크로스도메인 추론: 서로 다른 과학 도메인의 지식 그래프를 통합하여 더욱 혁신적인 학제 간 가설 생성
- 가설 검증 자동화: 생성된 가설의 선행 연구 존재 여부, 실험 설계 가능성 등을 자동으로 평가하는 검증 시스템

## Evaluation

- **Novelty**: 4/5 – 지식 그래프와 LLM 결합 자체는 새로우나, LBD와의 선형적 진화로 볼 여지도 있음

- **Technical Soundness**: 4/5 – 제안된 방법론이 기술적으로 타당하나, 실제 구현 및 실험 결과 상세성 필요

- **Significance**: 4/5 – 과학 발견 자동화의 중요한 진전이나, 실제 과학 공동체의 채택 및 영향력은 아직 실증 필요

- **Clarity**: 3/5 – 체계적인 분류와 설명이 있으나, 지식 그래프 구축, 경로 발견, LLM 프롬프팅 간의 구체적 상호작용 설명 부족

- **Overall**: 4/5

**총평**: 본 논문은 지식 그래프와 대규모 언어모델을 통합하여 과학적 가설 생성의 신뢰성과 창의성을 동시에 추구하는 유의미한 접근법을 제시하지만, 평가 자동화, 다양한 도메인 적용 사례, 인간-AI 협력 모델의 구체적 설계가 강화되면 더욱 완성도 있는 기여가 될 것으로 판단된다.

## Related Papers

- 🔄 다른 접근: [[papers/434_Interesting_Scientific_Idea_Generation_using_Knowledge_Graph/review]] — 과학적 가설 생성에서 지식 그래프와 지식 그래프 기반 접근법을 비교할 수 있습니다.
- 🏛 기반 연구: [[papers/393_Graphusion_a_rag_framework_for_knowledge_graph_construction/review]] — 과학 분야 지식그래프 구축을 위한 RAG 프레임워크가 가설 생성의 기반 지식 구조를 제공합니다.
- 🔗 후속 연구: [[papers/419_Hypothesis_Generation_with_Large_Language_Models/review]] — 대형 언어 모델을 활용한 가설 생성이 과학 지식 그래프 기반 방법론으로 확장될 수 있습니다.
- 🔗 후속 연구: [[papers/473_Large_Language_Models_for_Automated_Open-domain_Scientific_H/review]] — 과학 지식 그래프 기반 연구 가설 생성으로 웹 코퍼스에서 발견한 가설을 체계적으로 검증할 수 있다.
- 🔗 후속 연구: [[papers/426_Improving_Scientific_Hypothesis_Generation_with_Knowledge_Gr/review]] — 지식 그래프 기반 가설 생성의 실제 연구 적용 사례
- 🧪 응용 사례: [[papers/393_Graphusion_a_rag_framework_for_knowledge_graph_construction/review]] — 과학 지식 그래프를 활용한 연구 가설 생성이 Graphusion 프레임워크의 실제 응용 사례입니다.
- 🧪 응용 사례: [[papers/031_A_Survey_on_Hypothesis_Generation_for_Scientific_Discovery_i/review]] — 과학 지식 그래프를 활용한 연구 가설 생성의 구체적인 구현 방법을 보여준다.
- 🏛 기반 연구: [[papers/569_Nanostructured_Material_Design_via_a_Retrieval-Augmented_Gen/review]] — 과학 지식 그래프 기반 가설 생성 방법이 ACCELMAT의 소재 발견 가설 자동 생성 프레임워크의 이론적 토대가 됨
- 🔗 후속 연구: [[papers/763_Sparks_of_science_Hypothesis_generation_using_structured_pap/review]] — 과학 지식 그래프 기반의 연구 가설 생성을 구조화된 논문 데이터로 확장한 발전된 형태이다.
- 🔗 후속 연구: [[papers/123_Automated_Hypothesis_Validation_with_Agentic_Sequential_Fals/review]] — 지식 그래프 기반 가설 생성을 자동화된 통계적 검증으로 확장하여 완전한 가설 발견 파이프라인을 구축한다.
- 🔗 후속 연구: [[papers/149_Bayes-Entropy_Collaborative_Driven_Agents_for_Research_Hypot/review]] — HypoAgents는 지식그래프 기반 연구 가설 생성을 베이지안 추론과 정보엔트로피를 결합하여 확장함으로써 더 체계적이고 불확실성을 고려한 가설 생성을 실현합니다.
- 🏛 기반 연구: [[papers/492_Literature_meets_data_A_synergistic_approach_to_hypothesis_g/review]] — 과학 지식 그래프를 활용한 연구 가설 생성이 문헌과 데이터 통합 방법론의 구조화된 지식 표현과 추론 과정의 이론적 기반을 제공함
