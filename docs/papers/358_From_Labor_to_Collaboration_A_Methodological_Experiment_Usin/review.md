---
title: "358_From_Labor_to_Collaboration_A_Methodological_Experiment_Usin"
authors:
  - "Yi-Chih Huang"
date: "2026.02"
doi: "미제공"
arxiv: ""
score: 4.2
essence: "본 논문은 인문사회과학 연구에 특화된 AI 에이전트 기반의 협업 연구 워크플로우(Agentic Workflow)를 제안하고, 대만의 Claude.ai 사용 데이터(N=7,729)를 통해 그 실행 가능성을 검증하는 방법론적 실험이다. 인문사회과학 연구의 특수성(해석성, 이론 구축 지향성, 맥락 민감성)을 고려한 인간-AI 역할 분담 프레임워크를 제시한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Multi-agent_Task_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Huang_2026_From Labor to Collaboration A Methodological Experiment Using AI Agents to Augment Research Perspec.pdf"
---

# From Labor to Collaboration: A Methodological Experiment Using AI Agents to Augment Research Perspectives in Taiwan's Humanities and Social Sciences

> **저자**: Yi-Chih Huang | **날짜**: 2026-02-19 | **DOI**: [미제공](https://doi.org/)

---

## Essence

본 논문은 인문사회과학 연구에 특화된 AI 에이전트 기반의 협업 연구 워크플로우(Agentic Workflow)를 제안하고, 대만의 Claude.ai 사용 데이터(N=7,729)를 통해 그 실행 가능성을 검증하는 방법론적 실험이다. 인문사회과학 연구의 특수성(해석성, 이론 구축 지향성, 맥락 민감성)을 고려한 인간-AI 역할 분담 프레임워크를 제시한다.

## Motivation

- **Known**: 생성형 AI는 소프트웨어 공학과 자연과학 중심으로 연구되었으며, AI 에이전트는 순차적 다단계 작업 수행 능력을 갖춘 새로운 협업 모델로 주목받고 있다.

- **Gap**: 인문사회과학 연구의 특수한 요구(문헌 검토의 중요성, 이론적 깊이, 데이터 해석의 다원성, 연구 윤리 민감성)를 반영한 AI 에이전트 워크플로우 설계가 부재하다. 기존 AI 워크플로우는 소프트웨어 개발 시나리오(AutoGen, CrewAI 등)에 편향되어 있다.

- **Why**: 일반화된 AI 도구 활용 논의를 넘어 인문사회과학 연구 프로세스 전체에 AI를 체계적으로 통합하는 방법론적 틀이 필요하다. Hall(2026a)의 정치학 논문 복제 실험 사례는 AI의 수행 능력과 한계를 동시에 보여주며, 인간의 판단이 필수불가결한 영역을 구분하는 것의 중요성을 시사한다.

- **Approach**: 설계 과학(Design Science) 정신 아래 일곱 단계의 모듈식 워크플로우를 반복 개발하고, 대만 AEI 데이터 분석을 통해 실제 운영 과정을 메타분석하며, 세 가지 인간-AI 협업 모드를 도출한다.

## Achievement

1. **방법론적 기여**: 과제 모듈화(task modularization), 인간-AI 역할 분담(human-AI division of labor), 검증 가능성(verifiability)의 세 가지 설계 원칙을 기반으로 한 일곱 단계 AI 에이전트 협업 워크플로우 제안
   - 연구 기획 → 문헌 검토 → 자료 분석 → 해석 및 이론화 → 결과 작성 → 비판적 검토 → 참고문헌 관리

2. **운영 모드 분류**: 인간-AI 협업의 세 가지 패턴 도출
   - 직접 실행 모드(direct execution): AI가 명확하게 정의된 작업을 자율적으로 수행
   - 반복 개선 모드(iterative refinement): 인간의 피드백을 통한 점진적 개선
   - 인간 주도 모드(human-led): 인간이 주도적으로 의사결정하고 AI가 보조 역할

3. **반사적 기여**: 각 단계별 인간의 개입 지점, 프롬프트 설계 진화 과정, AI 산출물 수정 과정의 상세 문서화를 통해 "인간 판단의 대체 불가능성"이 명확히 드러나는 영역 규명
   - 연구 질문 설정, 이론적 해석, 맥락적 추론, 윤리적 성찰

## How

**방법론적 설계:**

- **혼합 방법 사용**: 방법론 수준에서는 설계 과학과 반복적 개선, 경험적 수준에서는 기술 통계 활용
  
- **데이터 소스**: Anthropic Economic Index(AEI) 공개 데이터셋 활용, 2025년 11월 13-20일 대만 지역(geo_id: TW) Claude.ai 사용 기록 7,729건

- **분석 차원**: 과제 유형, 협업 모드, AI 자율성, 과제 성공률, 사용 맥락 등 다층적 분석

- **이중 구조 운영**:
  - 1차 수준: 워크플로우 설계, 운영, 성찰 중심 (주요 기여)
  - 2차 수준: AEI 데이터 분석을 통한 방법론 검증 (부록 A 제시)

## Originality

- **인문사회과학 특화 설계**: 자연과학/공학 중심의 기존 AI 워크플로우 논의를 인문사회과학의 해석성, 이론 지향성, 맥락 민감성으로 재구성

- **모듈식 워크플로우의 체계화**: 연구 프로세스 전체를 일곱 단계의 명확히 구분된 모듈로 설계하여 반복 가능성(replicability) 확보

- **인간-AI 경계의 명시화**: 단순 효율성 논의를 넘어 "인간이 반드시 해야 할 것"과 "AI가 할 수 있는 것"의 경계를 구체적 사례로 규명

- **반사적 투명성**: 프롬프트 개선 과정, 인간의 개입 시점, 오류 수정 내역 등을 상세히 문서화하여 AI 사용의 윤리성과 투명성 논의에 자료 제공

## Limitation & Further Study

**한계:**

- **단일 플랫폼 데이터**: Claude.ai만 분석하여 다른 LLM 플랫폼의 상이한 특성을 반영하지 못함

- **횡단면 설계**: 2025년 11월 단 일주일 데이터로, 시간 경과에 따른 사용 패턴 변화를 추적하지 못함

- **AI 신뢰성 위험**: LLM의 "할루시네이션(hallucination)" 현상이나 편향된 출력의 위험성이 존재하며, 이에 대한 검증 체계가 충분하지 않음

- **이차 자료 연구에 한정**: 일차 자료 수집, 질적 심층 면접 등 다른 연구 방식에 대한 워크플로우는 미개발

**후속 연구 방향:**

- 다중 LLM 플랫폼 비교를 통한 일반화된 프레임워크 개발
- 시계열 데이터를 통한 AI 사용 패턴의 동적 변화 추적
- 질적 자료 분석, 현지조사, 실험 설계 등 다양한 인문사회과학 연구 방식으로 워크플로우 확장
- AI 신뢰성 검증 프로토콜 개발 및 리스크 관리 체계 구축


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.2/5

**총평**: 본 논문은 생성형 AI의 인문사회과학 연구 적용이라는 시의적절한 주제에서 기존 문헌의 공백을 명확히 인식하고, 설계 과학 기반의 반복적 개발과 대규모 실증 데이터를 통합한 방법론적 실험을 제시함으로써 학술적·실천적 기여를 이룬다. 다만 현재 제시된 본문에서는 일곱 단계 워크플로우의 구체적 내용과 세 가지 협업 모드의 상세한 분류 기준이 명확하게 드러나지 않아, 부록의 실제 분석 사례와 함께 검토되어야 할 것으로 보인다.

## Related Papers

- 🧪 응용 사례: [[papers/120_AutoGen_Enabling_Next-Gen_LLM_Applications_via_Multi-Agent_C/review]] — AutoGen의 다중 에이전트 대화 프레임워크가 인문사회과학 연구의 특수성을 고려한 협업 워크플로우에 구체적으로 적용된 사례이다.
- 🏛 기반 연구: [[papers/175_Building_machines_that_learn_and_think_with_people/review]] — 협력적 인지 원리와 인간-AI 파트너십 개념이 인문사회과학 연구의 해석적 특성을 고려한 역할 분담 설계의 이론적 기반이다.
- 🔗 후속 연구: [[papers/077_AI_for_social_science_and_social_science_of_AI_A_Survey/review]] — 사회과학을 위한 AI와 AI의 사회과학 연구가 인문사회과학에 특화된 AI 에이전트 협업 방법론으로 구체적으로 확장된 연구이다.
- 🧪 응용 사례: [[papers/120_AutoGen_Enabling_Next-Gen_LLM_Applications_via_Multi-Agent_C/review]] — 인문사회과학 연구를 위한 Agentic Workflow가 AutoGen의 다중 에이전트 협업 메커니즘을 특정 학문 영역에 적용한 실용 사례이다.
- 🧪 응용 사례: [[papers/175_Building_machines_that_learn_and_think_with_people/review]] — Building machines의 협력적 인지 원리가 인문사회과학 연구의 인간-AI 역할 분담 프레임워크에서 구체적으로 구현된 적용 사례이다.
