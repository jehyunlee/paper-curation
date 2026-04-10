---
title: "027_A_survey_of_llm-based_agents_in_medicine_How_far_are_we_from"
authors:
  - "Wenxuan Wang"
  - "Zizhan Ma"
  - "Zheng Wang"
  - "Chenghan Wu"
  - "Jiaming Ji"
date: "2025"
doi: ""
arxiv: ""
score: 4.0
essence: "의료 분야에서 LLM 기반 에이전트(LLM-based agents)의 아키텍처, 응용, 도전과제를 종합적으로 조사한 서베이로, 60개 논문(2022-2024)을 분석하여 의료 AI의 현황과 미래 방향을 제시합니다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Clinical_Multi-Agent_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wang et al._2025_A survey of llm-based agents in medicine How far are we from baymax arXiv preprint arXiv2502.1121.pdf"
---

# A survey of llm-based agents in medicine: How far are we from baymax? arXiv preprint arXiv:2502.11211, 2025.

> **저자**: Wenxuan Wang, Zizhan Ma, Zheng Wang, Chenghan Wu, Jiaming Ji, Wenting Chen, Xiang Li, Yixuan Yuan | **날짜**: 2025 | **URL**: [https://arxiv.org/abs/2502.11211](https://arxiv.org/abs/2502.11211)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: Conceptual framework of LLM-based medical agents. This figure depicts the architecture of the proposed*

의료 분야에서 LLM 기반 에이전트(LLM-based agents)의 아키텍처, 응용, 도전과제를 종합적으로 조사한 서베이로, 60개 논문(2022-2024)을 분석하여 의료 AI의 현황과 미래 방향을 제시합니다.

## Motivation

- **Known**: LLM은 텍스트 이해, 생성, 추론에 뛰어나며, 진단 지원, 환자 소통, 의료 교육 등 다양한 임상 작업에 적용되고 있습니다. 그러나 구현 문제, 안전 우려, 윤리적 고려사항 등의 도전이 남아있습니다.
- **Gap**: 의료 분야에서 LLM 기반 에이전트의 체계적인 종합 분석이 부족하며, 아키텍처 설계, 임상 통합 방법, 신뢰성 평가 기준이 명확히 정립되지 않았습니다.
- **Why**: LLM 기반 에이전트는 의료 서비스 전달을 향상시킬 수 있지만, 환자 안전과 윤시적 책임을 고려한 신뢰할 수 있는 임상 실무 통합이 필수적입니다.
- **Approach**: 60개의 peer-reviewed 논문을 체계적으로 검토하여 LLM 에이전트의 아키텍처 컴포넌트(프로필, 임상 계획, 의료 추론, 외부 용량 강화), 임상 응용 시나리오, 평가 프레임워크를 분석하고 분류합니다.

## Achievement

![Figure 1](figures/fig1.webp)

*Figure 1: Conceptual framework of LLM-based medical agents. This figure depicts the architecture of the proposed*

- **아키텍처 프레임워크 제시**: 시스템 프로필(기능 모듈화, 역할 전문화, 부서 조직), 임상 계획(작업 분해, 다중 에이전트 협업, 적응형 계획, 반복적 진화), 의료 추론(다단계 진단 추론, 반성적 의사결정, 협업 그룹 추론)을 포함한 통합 아키텍처
- **응용 범위 종합 분류**: 임상 의사결정 지원, 의료 기록, 훈련 시뮬레이션, 의료서비스 최적화 등 주요 임상 응용 시나리오 식별
- **평가 프레임워크 제시**: 의료 에이전트 성능 평가를 위한 구조화된 지표 및 메트릭스 정의
- **주요 도전과제 분석**: 환각(hallucination) 관리, 다중모달 통합, 구현 장벽, 윤리적 고려사항 등의 현안 문제 체계적 분석

## How

![Figure 1](figures/fig1.webp)

*Figure 1: Conceptual framework of LLM-based medical agents. This figure depicts the architecture of the proposed*

- 주요 데이터베이스에서 healthcare AI 관련 키워드로 검색하여 2022-2024 논문 300개 초기 수집
- 스크리닝 후 80개로 축소, 최종 60개가 포함 기준 충족하도록 필터링
- 각 논문의 에이전트 아키텍처, 임상 응용, 평가 방법을 구조화된 분류 체계로 분석
- LLM 에이전트의 네 가지 패러다임(단일 에이전트, 순차 작업 체인, 협업 전문가, 반복적 진화) 식별 및 분석
- 각 컴포넌트별 구체적 구현 방식(예: MEGDA, MDAgets, 수술실 시뮬레이션)의 사례 연구 수행

## Originality

- 의료 분야에서 LLM 기반 에이전트에 대한 최초의 종합적 서베이로, 아키텍처-응용-평가를 통합한 체계적 분석 제시
- 네 가지 에이전트 패러다임의 명확한 분류 및 의료 시나리오별 매핑
- 임상 계획과 의료 추론 모듈의 구체적 방법론(Chain-of-Thought, Tree-of-Thought, ReAct 등) 의료 맥락에서의 체계적 분석
- 의료 특화된 고려사항(다중모달 통합, 임상 협업, 투명성, 추적가능성)을 별도로 강조

## Limitation & Further Study

- 2024년까지의 논문만 포함하여 최신 발전(예: GPT-4o, Gemini 2.0 등 2025년 모델)이 미반영될 수 있음
- 포함된 60개 논문이 전체 의료 AI 분야의 제한된 표본일 가능성 (초기 300개 논문 중 20%만 선택)
- 실제 임상 실무 배포 사례와 장기 효과 평가 데이터 부족으로 이론-실제 갭 존재
- 다중모달 통합(영상, 텍스트, 수치 데이터 동시 처리)의 기술적 실현 방식에 대한 상세 분석 부족
- **후속 연구 방향**: (1) 실제 임상 환경에서의 검증 연구, (2) 환각 관리 및 안전성 보장 메커니즘 심화 연구, (3) 물리 시스템 통합 가능성 탐색, (4) 의료진-AI 협업 최적화 연구

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 의료 분야에서 LLM 기반 에이전트의 현황을 종합적으로 분석한 중요한 서베이로, 체계적인 아키텍처 프레임워크와 임상 응용 분류를 제시하며, 안전성과 윤리를 고려한 향후 연구 방향을 명확히 합니다. 실제 임상 배포 사례와 장기 효과 평가 데이터를 보강하면 더욱 실용적인 가이드가 될 수 있습니다.

## Related Papers

- 🔄 다른 접근: [[papers/529_MedAgents_Large_Language_Models_as_Collaborators_for_Zero-sh/review]] — 의료 LLM 에이전트 서베이와 MedAgents는 모두 의료 AI 에이전트를 다루지만, 포괄적 현황 분석과 제로샷 의료 진단이라는 서로 다른 관점을 제시합니다.
- 🏛 기반 연구: [[papers/168_Biomni_A_General-Purpose_Biomedical_AI_Agent/review]] — 의료 LLM 에이전트 연구는 BiomeMedLM과 같은 의료 특화 언어모델이 제공하는 도메인 지식 기반 위에 구축된 다중 에이전트 시스템을 분석합니다.
