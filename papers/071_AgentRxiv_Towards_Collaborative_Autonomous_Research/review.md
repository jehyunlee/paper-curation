---
title: "071_AgentRxiv_Towards_Collaborative_Autonomous_Research"
authors:
  - "Samuel Schmidgall"
  - "Michael Moor"
date: "2025.03"
doi: "10.48550/arXiv.2503.18102"
arxiv: ""
score: 4.2
essence: "본 논문은 LLM 에이전트들이 공유 프리프린트 서버를 통해 연구 결과를 주고받으며 협업하는 AgentRxiv 프레임워크를 제시한다. 단독으로 동작하는 기존 자율 연구 시스템의 한계를 극복하여, 에이전트들이 서로의 발견을 기반으로 누적적으로 개선할 수 있게 한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Multi-Agent_Scientific_Frameworks"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Schmidgall and Moor_2025_AgentRxiv Towards Collaborative Autonomous Research.pdf"
---

# AgentRxiv: Towards Collaborative Autonomous Research

> **저자**: Samuel Schmidgall, Michael Moor | **날짜**: 2025-03-23 | **DOI**: [10.48550/arXiv.2503.18102](https://doi.org/10.48550/arXiv.2503.18102)

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: AgentRxiv를 통한 협업 자율 연구. 분산된 자율 에이전트 실험실들이 공유 연구 목표를 향해 협업하며, 인간 연구자의 초기 지도 하에 에이전트들이 자율적으로 연구를 수행하고 중앙 프리프린트 서버에 논문을 업로드한다.*

본 논문은 LLM 에이전트들이 공유 프리프린트 서버를 통해 연구 결과를 주고받으며 협업하는 AgentRxiv 프레임워크를 제시한다. 단독으로 동작하는 기존 자율 연구 시스템의 한계를 극복하여, 에이전트들이 서로의 발견을 기반으로 누적적으로 개선할 수 있게 한다.

## Motivation

- **Known**: 최근 LLM 에이전트들이 자율적으로 연구를 수행할 수 있음이 입증되었다 (AI Scientist, Virtual Lab, Agent Laboratory). 과학적 발견은 역사적으로 여러 과학자의 점진적 협업의 결과이다.

- **Gap**: 기존 자율 연구 시스템들은 고립된 환경에서 단독으로 작동하며, 선행 연구 결과를 지속적으로 개선하는 능력이 부족하다. 인간 과학자들 간의 협업 메커니즘이 에이전트에게 구현되지 않았다.

- **Why**: 에이전트 간 협업을 통해 누적적 지식 구축이 가능하다면, 과학적 발견의 속도와 품질을 동시에 향상시킬 수 있다.

- **Approach**: 중앙 집중식 프리프린트 서버 인프라를 제공하여 여러 에이전트 실험실이 연구 논문을 업로드/검색하고, 서로의 발견을 기반으로 새로운 기법을 개발하도록 한다.

## Achievement

![Figure 3](figures/fig3.webp)
*그림 3: 자율 연구 협업을 위한 AgentRxiv 프레임워크. 두 개의 에이전트 실험실이 공유 프리프린트 서버를 통해 연구 결과를 교환한다.*

1. **단계별 성능 향상**: MATH-500 벤치마크에서 기준값 70.2%에서 최종 78.2%로 상향 (11.4% 상대 개선). Simultaneous Divergence Averaging (SDA) 등 새로운 추론 기법 발견.

2. **크로스 도메인 일반화**: MATH-500에서 발견된 추론 전략이 GPQA, MMLU-Pro, MedQA 등 다양한 벤치마크에 일반화되며, 5개 언어모델(DeepSeek-v3 ~ Gemini-2.0 pro)에서 평균 3.3% 개선.

3. **병렬 협업 효과**: 3개의 병렬 실험실 운영 시 MATH-500에서 +6.0% 추가 개선. 다중 에이전트 협업이 단일 에이전트보다 13.7% 상대 개선 달성.

## How

![Figure 2](figures/fig2.webp)
*그림 2: 에이전트 실험실 워크플로우. 3단계: 문헌 검토, 실험 수행, 보고서 작성*

![Figure 4](figures/fig4.webp)
*그림 4: MATH-500에서 새로운 추론 기법 설계. 단일 자율 에이전트의 진행 과정*

- **아키텍처**: 기존 Agent Laboratory 시스템에 기반하여 중앙 프리프린트 서버 모듈 추가. 각 에이전트가 생성한 논문을 자동으로 서버에 업로드하고, 다른 에이전트들이 검색·활용 가능하게 함.

- **반복 프로세스**: 
  - 인간이 초기 연구 방향과 상세 지시사항 제공
  - 에이전트가 자율적으로 연구 수행 및 논문 작성
  - 완성된 논문을 AgentRxiv에 업로드
  - 다른 에이전트들이 이전 연구 논문을 검색하여 새로운 기법 개발

- **병렬 모드**: 여러 에이전트 실험실이 동시에 실행되어 발견 속도 향상. 속도 vs. 계산 효율성 간 트레이드오프 존재.

- **평가 메커니즘**: MATH-500 벤치마크를 주요 평가 지표로 설정. 생성된 추론 기법의 일반화 능력을 다양한 도메인과 언어모델에서 검증.

## Originality

- **첫 협업 자율 연구 플랫폼**: 에이전트 간 지속적 협업과 누적적 개선을 지원하는 구조화된 프레임워크의 첫 제시. 기존 단독 자율 연구 시스템과의 명확한 차별화.

- **체계적 지식 공유**: 프리프린트 서버 인프라를 통해 인간 과학자 커뮤니티의 협업 모델을 에이전트 시스템으로 확장. 오픈소스 공개로 재현성 확보.

- **다중 에이전트 시너지 검증**: 병렬 실험실 구성을 통해 협업 이점을 정량적으로 입증. 단순한 개별 개선을 넘어 집단 협업 효과 실증.

- **일반화 능력 입증**: 특정 도메인(수학)에서 발견한 기법이 다양한 도메인과 모델에 이전된다는 증거 제시.

## Limitation & Further Study

- **계산 비용**: 병렬 모드에서 속도 향상(+6%)이 상당한 계산 오버헤드를 동반. 더 효율적인 병렬화 전략 필요.

- **에이전트 해석 문제**: 에이전트가 발견한 기법(예: SDA)에 대한 명확한 설명 메커니즘 부재. 왜 특정 기법이 효과적인지에 대한 심층 분석 필요.

- **스케일링 한계**: 현재 3개 에이전트까지만 실험. 수십, 수백 개 에이전트로 확장 시 협업 구조와 효율성 변화 미검증.

- **다양한 도메인 검증 부족**: 주로 수학적 추론 중심. 실험 설계, 문헌 발굴, 가설 생성 등 다양한 과학 활동에서의 협업 효과 검증 필요.

- **피드백 루프**: 현재 인간의 초기 지도만 존재. 에이전트 생성 논문에 대한 자동 평가 및 피드백 메커니즘 강화 필요.


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.2/5

**총평**: AgentRxiv는 자율 연구 시스템의 협업 패러다임을 처음 구현한 의미 있는 기여이며, 실증적 성과(11.4% ~ 13.7% 개선)와 일반화 능력을 보여준다. 다만 계산 효율성, 메커니즘 해석성, 다양한 과학 도메인에서의 검증이 향후 과제이다.

## Related Papers

- 🔄 다른 접근: [[papers/825_Towards_an_AI_co-scientist/review]] — AgentRxiv의 협업적 연구 공유 메커니즘과 AI co-scientist의 생성-토론-진화 방식은 서로 다른 접근으로 에이전트 간 지식 축적을 달성한다.
- 🔗 후속 연구: [[papers/826_Towards_Autonomous_Mathematics_Research/review]] — 수학 연구의 자율적 정리 발견을 위한 Aletheia가 AgentRxiv의 협업적 연구 프레임워크를 전문 수학 도메인으로 확장한 사례이다.
- 🏛 기반 연구: [[papers/668_ResearchAgent_Iterative_Research_Idea_Generation_over_Scient/review]] — ResearchAgent의 반복적 아이디어 생성 메커니즘이 AgentRxiv의 누적적 지식 개선 시스템의 기반이 되는 기술적 토대이다.
- 🔄 다른 접근: [[papers/825_Towards_an_AI_co-scientist/review]] — AI co-scientist의 생성-토론-진화 방식과 AgentRxiv의 프리프린트 서버 기반 협업은 서로 다른 메커니즘으로 에이전트 간 지식 발전을 달성한다.
- 🔗 후속 연구: [[papers/826_Towards_Autonomous_Mathematics_Research/review]] — AgentRxiv의 협업적 연구 프레임워크가 Aletheia의 수학 연구 자동화를 위한 다중 에이전트 지식 공유 시스템으로 확장된 형태이다.
