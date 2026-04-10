---
title: "018_A_retrieval-augmented_knowledge_mining_method_with_deep_thin"
authors:
  - "Yichun Feng"
  - "Jiawei Wang"
  - "Ruikun He"
  - "Lu Zhou"
  - "Yixue Li"
date: "2025"
doi: "10.1093/gigascience/giaf109"
arxiv: ""
score: 4.0
essence: "생의학 연구를 위해 Deep Thinking LLM과 Retrieval-Augmented Generation(RAG)을 통합한 지식 채굴 방법론을 제안하며, BioStrataKG 지식 그래프와 BioCDQA 데이터셋을 구축하고 IP-RAR 프레임워크로 문서 간 추론 능력을 향상시킨다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Retrieval-augmented_Generation_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Feng et al._2025_A retrieval-augmented knowledge mining method with deep thinking LLMs for biomedical research and cl.pdf"
---

# A retrieval-augmented knowledge mining method with deep thinking LLMs for biomedical research and clinical support

> **저자**: Yichun Feng, Jiawei Wang, Ruikun He, Lu Zhou, Yixue Li | **날짜**: 2025 | **DOI**: [10.1093/gigascience/giaf109](https://doi.org/10.1093/gigascience/giaf109)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: Overview of the proposed framework for biomedical knowledge mining. (A) Biomedical knowledge sources, such*

생의학 연구를 위해 Deep Thinking LLM과 Retrieval-Augmented Generation(RAG)을 통합한 지식 채굴 방법론을 제안하며, BioStrataKG 지식 그래프와 BioCDQA 데이터셋을 구축하고 IP-RAR 프레임워크로 문서 간 추론 능력을 향상시킨다.

## Motivation

- **Known**: Knowledge Graph와 LLM은 생의학 지식 통합과 추론의 핵심 도구이며, RAG(Retrieval-Augmented Generation) 기법이 외부 지식 통합에 효과적이다는 것이 알려져 있다.
- **Gap**: 기존 방법들은 생의학 용어의 복잡성, 데이터 이질성, 빠른 지식 진화로 인한 지식 그래프 구성의 한계와 LLM의 제한된 검색 및 추론 능력으로 인해 문서 간 연관성과 추론 경로를 발견하기 어렵다.
- **Why**: 생의학 연구에서 방대한 정보를 효율적으로 활용하면 임상 의학, 약리학, 분자 생물학 등 복잡한 문제 해결을 가속화할 수 있으며, 의료진의 정밀 의료 계획 수립과 연구자의 연구 전략 수립을 지원한다.
- **Approach**: LLM을 활용하여 대규모 생의학 논문으로부터 엔티티 수준과 문서 수준의 이중 계층 지식 그래프(BioStrataKG)를 구축하고, 문서 간 질의응답 데이터셋(BioCDQA)을 생성하여, Integrated Reasoning-based Retrieval과 Progressive Reasoning-based Generation을 통합한 IP-RAR 프레임워크로 검색 정확도와 추론 능력을 강화한다.

## Achievement

![Figure 1](figures/fig1.webp)

*Figure 1: Overview of the proposed framework for biomedical knowledge mining. (A) Biomedical knowledge sources, such*

- **BioStrataKG 지식 그래프 구축**: 엔티티 수준(유전자, 단백질, 질병, 약물 관계)과 문서 수준(방법, 데이터셋, 인용 관계)의 이중 계층 구조로 복잡한 생의학 관계를 포착
- **BioCDQA 데이터셋 개발**: 문서 간 추론과 지식 통합을 평가하기 위한 새로운 생의학 교차 문서 질의응답 데이터셋 구축
- **IP-RAR 프레임워크 제안**: Integrated Reasoning-based Retrieval로 검색 recall 극대화, Progressive Reasoning-based Generation으로 정확성 정제, 자기 성찰(Self-reflection) 메커니즘으로 deep thinking 구현
- **성능 향상**: 문서 검색 F1 점수 20% 개선, 답변 생성 정확도 25% 향상
- **다양한 임상 응용**: 약물 상호작용 분석, 약물 재목적화(Drug Repurposing), 정밀 의료, 연구 병목 분석 등 실제 임상 의사결정 지원

## How

![Figure 3](figures/fig3.webp)

*Figure 3: Framework of IP-RAR. (A) Integrated Reasoning-based Retrieval: Performs pre-retrieval reasoning, extracting*

- LLM을 이용한 엔티티 추출 및 관계 인식으로 엔티티 수준 지식 그래프 자동 구성
- 논문의 방법론, 데이터셋, 인용 관계를 분석하여 문서 수준 지식 그래프 생성
- 두 계층의 그래프를 병합하여 통합 지식 그래프(BioStrataKG) 형성
- Integrated Reasoning-based Retrieval: 쿼리와 관련된 모든 관련 정보를 다층적 추론으로 최대한 검색
- Progressive Reasoning-based Generation: 검색된 정보를 점진적으로 정제하면서 답변 생성
- Self-reflection 메커니즘: 생성된 답변의 품질을 자동 평가하고 반복적으로 최적화
- Deep Thinking LLM 활용: GPT-o1, DeepSeek-R1 같은 고급 추론 모델로 최종 답변 개선

## Originality

- 엔티티-문서 이중 계층 지식 그래프 구조의 새로운 설계로 생의학 도메인의 복잡한 관계를 다각도로 포착
- 문서 간 추론(cross-document reasoning)을 구체적으로 평가하는 BioCDQA 데이터셋의 개발
- Integrated Reasoning + Progressive Reasoning의 조합으로 검색과 생성 단계를 유기적으로 통합
- Self-reflection 메커니즘을 RAG에 도입하여 반복적 정제 과정 자동화
- Deep Thinking LLM의 고급 추론 능력을 생의학 지식 채굴에 처음 적용

## Limitation & Further Study

- BioStrataKG 구축 시 LLM의 엔티티 인식 오류와 관계 추출 오류가 누적될 수 있는 위험
- BioCDQA 데이터셋의 규모와 다양성이 제한적일 수 있으며, 특정 생의학 부분 분야의 편향 가능성
- IP-RAR의 계산 복잡도가 높아 대규모 실시간 응용에서의 확장성 제한
- Deep Thinking LLM의 높은 비용으로 인한 실제 임상 적용의 경제적 장벽
- **후속 연구**: (1) 여러 LLM 앙상블로 엔티티 추출 오류 감소, (2) 더 큰 규모의 다양한 의료 데이터셋 구축, (3) 경량 모델 최적화로 실시간 성능 개선, (4) 임상 검증을 통한 실제 의료 환경에서의 효과성 입증

## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 생의학 지식 채굴을 위한 포괄적이고 체계적인 프레임워크를 제시한 우수한 연구이며, LLM의 깊은 추론 능력과 RAG 기법의 효과적인 통합으로 문서 간 추론 능력을 획기적으로 향상시켰다. 실제 임상 의사결정과 연구 전략 수립을 지원할 수 있는 높은 실용성을 갖추고 있다.

## Related Papers

- 🧪 응용 사례: [[papers/602_Paperqa_Retrieval-augmented_generative_agent_for_scientific/review]] — 과학 연구를 위한 검색 증강 생성 에이전트의 실제 구현 사례를 보여준다.
