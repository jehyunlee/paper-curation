---
title: "1022_SciSciGPT_advancing_humanAI_collaboration_in_the_science_of"
authors:
  - "Erzhuo Shao"
  - "Yifang Wang"
  - "Yifan Qian"
  - "Zhenyu Pan"
  - "Han Liu"
date: "2025.12"
doi: "10.1038/s43588-025-00906-6"
arxiv: ""
score: 4.0
essence: "SciSciGPT는 대규모 언어 모델(LLM)을 기반으로 한 오픈소스 AI 협력자로, 과학의 과학 분야에서 복잡한 연구 워크플로우를 자동화하고 재현성을 향상시킨다. 다중 에이전트 시스템을 통해 문헌 검색, 데이터 처리, 분석, 시각화를 통합적으로 수행하는 인간-AI 협력 프레임워크를 제시한다."
tags:
  - "cat/Scientific_Impact_and_Innovation"
  - "sub/Artificial_intelligence_and_science"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Shao et al._2025_SciSciGPT advancing human–AI collaboration in the science of science.pdf"
---

# SciSciGPT: advancing human–AI collaboration in the science of science

> **저자**: Erzhuo Shao, Yifang Wang, Yifan Qian, Zhenyu Pan, Han Liu, Dashun Wang | **날짜**: 2025-12-09 | **DOI**: [10.1038/s43588-025-00906-6](https://doi.org/10.1038/s43588-025-00906-6)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1 | SciSciGPT system architecture. A diagram illustrating the modular*

SciSciGPT는 대규모 언어 모델(LLM)을 기반으로 한 오픈소스 AI 협력자로, 과학의 과학 분야에서 복잡한 연구 워크플로우를 자동화하고 재현성을 향상시킨다. 다중 에이전트 시스템을 통해 문헌 검색, 데이터 처리, 분석, 시각화를 통합적으로 수행하는 인간-AI 협력 프레임워크를 제시한다.

## Motivation

- **Known**: LLM은 복잡한 추론, 도구 사용, 코딩 등 고수준의 인지 작업에 점점 더 능숙해지고 있으며, 이를 자율 에이전트(autonomous agents)의 중앙 제어기로 활용하는 연구가 진행 중이다. 과학의 과학(Science of Science) 분야는 대규모 데이터와 계산 방법의 발전으로 성장했으나, 데이터 복잡성과 높은 진입장벽이 과제로 남아 있다.
- **Gap**: 복잡해지는 연구 데이터셋과 계산 방법 사이의 괴리로 인해 연구자들이 비용이 큰 기술적 장벽에 직면하고 있으며, LLM 기반 도구가 이를 해결하는 구체적인 방식과 실제 연구 효율성 향상 사이의 관계가 충분히 입증되지 않았다.
- **Why**: AI 기반 연구 협력자는 기술 진입장벽을 낮추고 연구 효율성을 높이며 재현성을 증진할 수 있으며, 과학 정책 수립과 차세대 과학자 교육에 중대한 영향을 미칠 수 있다. 이러한 시스템의 설계와 성능 평가는 향후 과학 연구 방식의 혁신을 선도할 수 있다.
- **Approach**: 과학의 과학 분야를 테스트베드로 삼아, 다섯 가지 전문 모듈(ResearchManager, LiteratureSpecialist, DatabaseSpecialist, AnalyticsSpecialist, EvaluationSpecialist)로 구성된 다중 에이전트 시스템을 개발하고, LLM 에이전트 역량 성숙도 모델(Capability Maturity Model)을 제안하였다.

## Achievement


- **다중 에이전트 시스템 구축**: 5개의 전문화된 에이전트가 계층적으로 협력하여 연구 워크플로우를 동적으로 분해하고 실행하는 통합 프레임워크 개발
- **포괄적 기능 통합**: 문헌 검색, 데이터 추출 변환, 통계 분석, 시각화, 품질 평가 등 과학 연구의 전반적 단계를 자동화하는 end-to-end 워크플로우 구현
- **LLM 에이전트 성숙도 모델 제시**: 기능 역량, 워크플로우 오케스트레이션, 메모리 아키텍처, 인간-AI 협력 패러다임의 4단계 진화 로드맵 제안
- **재현성과 투명성 확보**: 웹 인터페이스 및 완전 오픈소스 구현으로 접근성과 확장성 보장하고, 실제 사례 연구를 통해 효능성 입증
- **도메인 적응 가능성 입증**: Ivy League 대학 협력 시각화 및 기존 논문 재현 사례를 통해 다양한 분석 접근법 지원 능력 시연

## How

![Figure 1](figures/fig1.webp)

*Fig. 1 | SciSciGPT system architecture. A diagram illustrating the modular*

- ResearchManager 에이전트가 사용자 질문을 분석하여 실행 계획(execution plan)을 수립하고 적절한 전문가 에이전트에 태스크 할당
- 각 전문가 에이전트(LiteratureSpecialist, DatabaseSpecialist, AnalyticsSpecialist)는 서브플랜을 수립하고 도구를 호출하여 반복적 추론(iterative reasoning) 수행
- EvaluationSpecialist가 분석, 시각화, 방법론의 품질, 관련성, 엄밀성을 다층적으로 평가(ToolEval, VisualEval, TaskEval)하여 지속적 개선 유도
- SciSciCorpus와 SciSciNet 등 도메인 특화 데이터 소스 및 샌드박스 환경(Python, R, Julia 지원)과의 연동을 통해 신뢰할 수 있는 실행 환경 제공
- 사용자와의 대화형 인터페이스를 통해 연구 질문의 점진적 정제와 다양한 분석 경로 탐색 지원

## Originality

- LLM을 과학 메타연구(Science of Science) 도메인에 맞춤화하여 적용한 첫 체계적 시도로, 단순한 챗봇을 넘어 실제 연구 워크플로우를 통합하는 에이전트 설계
- LLM 에이전트의 성숙도를 체계화한 4단계 모델(Functional Capabilities → Workflow Orchestration → Memory Architecture → Human-AI Paradigm)은 향후 AI 연구 협력자 개발의 참조 기준 제시
- EvaluationSpecialist를 통한 자체 평가 메커니즘으로 AI 생성 결과의 품질을 재귀적으로 검증하는 설계는 신뢰성과 투명성을 동시에 추구하는 혁신적 접근
- 도메인 특화 데이터(SciSciCorpus, SciSciNet) 및 도구(Python, R, Julia)와의 유기적 통합으로 RAG(Retrieval-Augmented Generation) 기반의 진화된 LLM 에이전트 구현
- 오픈소스 공개와 웹 인터페이스 제공으로 투명성, 재현성, 확장성을 동시에 확보한 책임감 있는 AI 도구 개발 모델 수립

## Limitation & Further Study

- **현재 제약**: 프로토타입 수준이므로 성능과 가치는 향후 LLM 발전과 함께 증가할 것으로 예상되며, 현재 평가는 제한된 사례 연구에 기반
- **인간-AI 역할 균형 문제**: 자동화 수준의 적절성, 투명성 확보, 윤리적 사용에 대한 심화된 논의가 필요하며, 인간 과학자의 창의성과 판단력 보존 메커니즘 정의 부족
- **도메인 일반화 가능성의 불확실성**: 현재는 과학의 과학에 최적화되어 있으며, 다른 과학 분야로의 이전(transfer)에는 도메인 특화 지식, 데이터, 도구의 추가 통합이 필요
- **메모리 아키텍처의 미완성**: 현재는 대화형 문맥 학습 수준이며, 장기 메모리(episodic, semantic memory)를 통한 누적 학습 능력이 성숙도 모델의 3단계에 머물러 있음
- **후속 연구 방향**: 대규모 실제 연구 프로젝트에서의 종단 효과성 평가, 다양한 배경의 사용자 그룹(신규 연구자 vs. 전문가)에 대한 비교 연구, 투명성과 설명 가능성(explainability) 강화, AI 기여도 정량화와 저자권 문제 해결 메커니즘 개발

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: SciSciGPT는 LLM 기반 AI 협력자의 설계와 평가를 위한 구체적이고 포괄적인 사례를 제시하며, 제안된 성숙도 모델은 향후 다양한 과학 분야에서 AI 연구 도구 개발의 이정표가 될 수 있다. 투명성과 오픈소스 공개를 통해 책임감 있는 AI 개발의 모범을 보이면서도, 인간-AI 협력의 윤리성과 실제 과학 생산성 향상에 대한 더 깊이 있는 논증이 후속 연구에서 요구된다.

## Related Papers

- 🔗 후속 연구: [[papers/1019_Science_of_science/review]] — 과학의 과학 분야의 기본 개념과 방법론을 AI 협력 시스템으로 확장하여 자동화된 연구 워크플로우를 구현한다.
- 🏛 기반 연구: [[papers/1071_Data_measurement_and_empirical_methods_in_the_science_of_sci/review]] — 과학의 과학 분야의 데이터, 측정, 실증 방법에 대한 체계적 이해가 AI 협력 시스템 개발의 기반을 제공한다.
- 🧪 응용 사례: [[papers/1033_The_Empowerment_of_Science_of_Science_by_Large_Language_Mode/review]] — 과학의 과학 분야에서 인간-AI 협력을 위한 구체적인 적용 사례를 제시한다
- 🔗 후속 연구: [[papers/1118_Paper_Circle_An_Open-source_Multi-agent_Research_Discovery_a/review]] — 과학의 과학 분야에서 인간-AI 협력을 다중 에이전트 시스템으로 확장하여 연구 발견과 분석을 자동화한다.
- 🧪 응용 사례: [[papers/931_AI-Driven_Automation_Can_Become_the_Foundation_of_Next-Era_S/review]] — 과학의 과학 분야에서 인간-AI 협업을 다루는 SciSciGPT와 연결되어 AI4SoS 프레임워크의 구체적인 구현 방안을 보여준다.
