---
title: "311_Empowering_Biomedical_Discovery_with_AI_Agents"
authors:
  - "Shanghua Gao"
  - "Ada Fang"
  - "Yepeng Huang"
  - "Valentina Giunchiglia"
  - "Ayush Noori"
date: "2024"
doi: "10.48550/arXiv.2404.02831"
arxiv: ""
score: 4.0
essence: "본 논문은 생의학 발견을 가속화하기 위해 대규모 언어 모델(LLM), 기계 학습(ML) 도구, 실험 플랫폼을 통합한 AI 에이전트 시스템의 구성과 활용을 제시한다. 이는 인간 과학자를 배제하지 않고 AI의 데이터 분석 능력과 인간의 창의성을 결합한 협업 발견 체계이다."
tags:
  - "cat/LLM-Based_Scientific_Reasoning"
  - "sub/Large_Language_Model_Agents"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Gao et al._2024_Empowering Biomedical Discovery with AI Agents.pdf"
---

# Empowering Biomedical Discovery with AI Agents

> **저자**: Shanghua Gao, Ada Fang, Yepeng Huang, Valentina Giunchiglia, Ayush Noori | **날짜**: 2024 | **DOI**: [10.48550/arXiv.2404.02831](https://doi.org/10.48550/arXiv.2404.02831)

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: AI 에이전트를 통한 생의학 연구 역량 강화. AI 에이전트는 회의적 학습과 추론이 가능한 "AI 과학자"의 길을 열어줌*

본 논문은 생의학 발견을 가속화하기 위해 대규모 언어 모델(LLM), 기계 학습(ML) 도구, 실험 플랫폼을 통합한 AI 에이전트 시스템의 구성과 활용을 제시한다. 이는 인간 과학자를 배제하지 않고 AI의 데이터 분석 능력과 인간의 창의성을 결합한 협업 발견 체계이다.

## Motivation

- **Known**: 지난 수십 년간 데이터 주도 모델(데이터베이스, 검색 엔진, 기계학습)이 생의학 연구를 혁신해왔으며, 단백질 구조 예측(AlphaFold) 같은 전문화된 모델들이 성공을 거두었음

- **Gap**: 기존 머신러닝 모델은 각 작업별로 특화된 모델이 필요하고, 검색 엔진은 쿼리 개선 및 반복적 추론 능력이 부족하며, 현재의 기초 모델(Foundation Models)만으로는 학습 데이터에 없는 새로운 가설을 생성할 수 없음

- **Why**: 생물학적 문제는 복잡하므로 문제 분해 능력, 전문화된 부분 작업 수행, 지속적 학습과 불확실성 평가 능력이 필요함

- **Approach**: LLM, ML 도구, 실험 플랫폼을 통합하고 인간 감독 하에 지속적 학습과 자기 평가가 가능한 다중 에이전트 시스템(Multi-Agent System) 구축

## Achievement

![Figure 2](figures/fig2.webp)
*그림 2: 생의학 연구의 데이터 주도 모델 진화. 데이터베이스, 검색 엔진에서 기계학습, 대화형 학습, AI 에이전트로 발전*

1. **AI 에이전트의 다층 구성**: LLM 기반 에이전트, 다중 에이전트 시스템, 멀티모달 학습 에이전트 등 다양한 아키텍처 제시로 생의학 문제의 특수성에 맞춘 구현 방안 제공

2. **기존 접근법과의 차별화**: 데이터베이스의 정확성, 검색 엔진의 질의 기반 검색, ML 모델의 패턴 인식, 상호작용학습의 피드백 메커니즘을 모두 통합한 종합적 시스템

3. **응용 분야 확대**: 가상 세포 시뮬레이션(Virtual Cell Simulation), 표현형 프로그래밍 제어(Programmable Control of Phenotypes), 세포 회로 설계(Cellular Circuit Design), 신약 개발에 걸친 광범위한 임상 응용 가능성 제시

## How

![Figure 3](figures/fig3.webp)
*그림 3: 생의학의 다양한 AI 에이전트 구성 - LLM 기반 AI 에이전트부터 다중 에이전트 시스템까지*

![Figure 4](figures/fig4.webp)
*그림 4: 생의학 AI 에이전트의 네 가지 핵심 모듈: 인지(Perception), 상호작용(Interaction), 추론(Reasoning), 메모리(Memory) 모듈*

- **LLM 기반 에이전트**: 단일 LLM을 다양한 역할로 프로그래밍하여 대화형 인터페이스 제공, 지시 튜닝(Instruction Tuning)과 인간 피드백 강화학습(RLHF)으로 도메인 특화 지식 및 인간 정렬 달성

- **다중 에이전트 시스템**: 이질적 에이전트(ML 도구, 도메인 특화 도구, 인간 전문가) 결합으로 텍스트 기반이 아닌 생의학 연구에 더 높은 적용성 제공

- **핵심 모듈 설계**:
  - **인지 모듈(Perception)**: 시각 ML 도구 등을 통해 환경으로부터 정보 수신
  - **상호작용 모듈(Interaction)**: 검색 엔진, ML 도구, 실험 장비와 연결되어 외부 도구 호출
  - **추론 모듈(Reasoning)**: 과학적 근거를 바탕으로 가설 생성 및 평가
  - **메모리 모듈(Memory)**: 단기 메모리(이전 대화 기록)와 장기 메모리(구조화된 지식 베이스)로 지속적 학습 지원

- **검색 증강 생성(RAG)**: 과학 문헌 기반 답변으로 할루시네이션(Hallucination) 위험 감소

- **상호작용 학습 통합**: 능동학습(Active Learning)과 강화학습(Reinforcement Learning)으로 작은 데이터셋에서도 효율적 학습

## Originality

- 생의학 발견의 맥락에서 "AI 과학자"의 실현을 구체적으로 정의하고 다층적 시스템 아키텍처로 제시한 최초의 종합적 관점 제공

- 기존 LLM 중심 에이전트를 넘어 다중 에이전트 시스템과 도메인 특화 도구의 이질적 통합 모델 제안

- 데이터베이스 → 검색 엔진 → 머신러닝 → 상호작용학습 → AI 에이전트로 이어지는 진화 스펙트럼의 역사적 맥락화

- AI 에이전트의 네 가지 핵심 모듈(인지, 상호작용, 추론, 메모리)의 생의학 특화 설계 원칙 제시

- 가상 세포 시뮬레이션, CRISPR 기반 유전자 편집 자동화, 세포 회로 설계 등 구체적 생의학 사례를 통한 실용성 입증

## Limitation & Further Study

- **데이터 부족 문제**: 생의학 실험 데이터셋이 제한적이고 특정 영역(구조 생물학, 단일 세포 과학)에 집중되어 있어 일반화 성능 저하 가능성

- **윤리적 우려**: AI 에이전트가 실험 플랫폼을 통해 환경을 변경할 수 있다는 점에서 안전장치(Safeguard) 부재 시 해악 가능성, 과도한 AI 의존도에 따른 과학자의 자율성 문제

- **현재 기초 모델의 한계**: LLM의 다음 토큰 예측(Next-Token Prediction) 방식이 과학적 창의성과 새로운 가설 생성에 직접 적용되기 어려움

- **데이터 효율성**: 생의학 에이전트는 최소 추가 학습으로 새 작업에 강한 일반화(Few-Shot/Zero-Shot) 성능 달성 필요

- **후속 연구 방향**: (1) 다양한 생의학 도메인에 대한 대규모 실험 데이터셋 구축, (2) 불확실성 정량화와 신뢰도 평가 메커니즘 개발, (3) 인간-AI 협업의 최적 인터페이스 설계, (4) 생의학 에이전트의 책임있는 배포를 위한 규제 프레임워크 수립

## Evaluation

- **Novelty**: 4/5
  - 생의학 맥락에서 AI 에이전트의 종합적 비전과 다중 에이전트 아키텍처는 신선하나, 개별 기술(LLM, RAG, 상호작용학습)은 기존 기술의 조합

- **Technical Soundness**: 4/5
  - 제안된 모듈 설계와 아키텍처는 논리적으로 타당하나, 구체적 구현 사례와 정량적 평가 결과 부재로 이론적 가능성 수준

- **Significance**: 5/5
  - 생의학 연구의 자동화, 고속화, 대규모화에 미치는 잠재적 영향이 매우 크며, 신약 개발부터 기초 생물학까지 광범위한 응용 가능성

- **Clarity**: 4/5
  - 구조화된 서술과 명확한 그림으로 일반적 이해는 용이하나, 구체적 구현 세부사항과 실험 결과 부족으로 완전한 기술적 깊이 제공 미흡

- **Overall**: 4/5

**총평**: 본 논문은 생의학 발견을 위한 AI 에이전트 시스템의 비전과 설계 원칙을 제시하는 중요한 관점 문서로, 단백질 구조 예측 후 AI가 생의학 연구에 미칠 다음 단계의 변혁을 조망한다. 다만 개념 제시에 중점을 두어 실제 구현 프로토타입이나 실증 결과가 부재한 점이 주요 한계이다.

## Related Papers

- 🔗 후속 연구: [[papers/847_Two_heads_are_better_than_one_A_multi-agent_system_has_the_p/review]] — 생의학 AI 에이전트를 다중 에이전트 과학 연구 시스템으로 일반화한 확장 연구
- 🔄 다른 접근: [[papers/529_MedAgents_Large_Language_Models_as_Collaborators_for_Zero-sh/review]] — 생의학 발견 vs 의료 진단에서 서로 다른 생의학 AI 에이전트 응용 영역
- 🔗 후속 연구: [[papers/774_STELLA_Towards_a_Biomedical_World_Model_with_Self-Evolving_M/review]] — 생의학 AI 에이전트를 자기진화형 세계 모델로 발전시킨 차세대 시스템
- 🧪 응용 사례: [[papers/616_PharmAgents_Building_a_Virtual_Pharma_with_Large_Language_Mo/review]] — 생의학 발견을 가상 제약회사 시스템으로 구현한 구체적인 응용 사례
- 🏛 기반 연구: [[papers/847_Two_heads_are_better_than_one_A_multi-agent_system_has_the_p/review]] — 생의학 AI 에이전트 시스템이 다중 에이전트 과학 연구의 도메인별 기반
