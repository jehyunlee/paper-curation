---
title: "396_Hallucination_mitigation_using_agentic_ai_natural_language-b"
authors:
  - "Diego Gosmar"
  - "Deborah A. Dahl"
date: "2025"
doi: "N/A"
arxiv: ""
score: 3.5
essence: "대규모 언어 모델(LLM)의 환각(hallucination) 문제를 완화하기 위해 OVON(Open Voice Network) 프레임워크 기반의 자연어 처리(NLP) 인터페이스를 활용한 다중 에이전트(multi-agent) 오케스트레이션 방식을 제안하고, 구조화된 JSON 메시지를 통한 에이전트 간 통신이 AI 생성 응답의 신뢰성과 설명 가능성을 향상시킬 수 있음을 실증적으로 입증한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Multi-Agent_Language_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Gosmar and Dahl_2025_Hallucination mitigation using agentic ai natural language-based frameworks.pdf"
---

# Hallucination mitigation using agentic ai natural language-based frameworks

> **저자**: Diego Gosmar, Deborah A. Dahl | **날짜**: 2025 | **DOI**: N/A

---

## Essence

대규모 언어 모델(LLM)의 환각(hallucination) 문제를 완화하기 위해 OVON(Open Voice Network) 프레임워크 기반의 자연어 처리(NLP) 인터페이스를 활용한 다중 에이전트(multi-agent) 오케스트레이션 방식을 제안하고, 구조화된 JSON 메시지를 통한 에이전트 간 통신이 AI 생성 응답의 신뢰성과 설명 가능성을 향상시킬 수 있음을 실증적으로 입증한다.

## Motivation

- **Known**: 현재 생성형 AI 모델에서 환각 현상은 필연적이며(Hallucination is Inevitable: An Innate Limitation of Large Language Models), AI 시스템의 신뢰성을 훼손하는 심각한 문제로 알려져 있음. 기존 연구에서는 다중 에이전트 환경을 통한 환각 완화 가능성이 제시되었음(예: 'Good Parenting is All You Need', 'Multi-agent Debate' 등).

- **Gap**: 기존 다중 에이전트 접근 방식들은 특정 모델 조합이나 제한된 실험 범위에 집중되어 있으며, 표준화된 에이전트 간 통신 프로토콜을 통한 체계적인 환각 완화 메커니즘과 정량적 평가 지표가 부족함.

- **Why**: LLM 기반 AI 시스템의 신뢰도 확보와 설명 가능성(Explainability) 향상을 위해서는 에이전트 간의 투명한 정보 교환과 구조화된 메타데이터 전달이 필수적.

- **Approach**: 310개의 환각 유도 프롬프트를 4단계 에이전트 파이프라인에 주입하고, OVON 표준 기반의 JSON 구조화 메시지를 통해 각 에이전트의 검증 결과를 다음 단계에 전달하며, 새로운 KPI(Key Performance Indicators) 4가지를 설계하여 환각 완화 효과를 정량적으로 측정.

## Achievement

1. **환각 점수 감소 효과**: 다중 에이전트 파이프라인을 거치면서 Total Hallucination Scores(THS)가 단계적으로 감소하며, 특히 1단계에서 2-3단계로 진행되면서 유의미한 환각 감소율 달성.

2. **설명 가능성 향상**: 투기적 내용(speculative content)이 사실 기반 주장과 명확하게 구분되고, 명시적 면책조항(explicit disclaimers)과 맥락화(contextualization)가 강화되어 AI의 설명 가능성(XAI) 수준 개선.

3. **구조화된 평가 프레임워크**: 새로운 KPI 4가지(Factual Claim Density, Factual Grounding References, Fictional Disclaimer Frequency, Explicit Contextualization Score)를 통해 환각 완화를 객관적으로 측정할 수 있는 메트릭 체계 확립.

4. **상호운용성 검증**: OVON 표준 기반의 NLP API가 다양한 LLM 모델들 간의 효율적인 상호작용을 가능하게 함을 입증.

## How

![Fig 1]() *다중 에이전트 시뮬레이션 환경 구성도*

- **4단계 에이전트 파이프라인 설계**:
  - 1단계(Front-end): 사용자 입력 프롬프트 수신 및 초기 응답 생성
  - 2-3단계(Refinement agents): 서로 다른 LLM을 활용하여 검증되지 않은 주장 감지, 면책조항 추가, 투기적 내용 명확화
  - 4단계(Evaluation agent): 제시된 KPI들을 평가하고 환각 관련 행동의 변화 정량화

- **OVON 프레임워크 기반 통신**:
  - 구조화된 JSON 메시지로 에이전트 간 메타정보(면책조항, 경고 필드 등) 전달
  - 각 에이전트가 환각 가능성 및 의심 내용의 근거를 명시적으로 기록
  - 문맥 정보 손실 없이 텍스트 정제 진행

- **환각 유도 기법**:
  - 지식 격차 활용: 모호한 질문, 고도로 전문화된 주제
  - 사실과 허구 혼합: 부분적으로 정확한 정보와 함께 오류 정보 제시
  - 모델의 한계 초과: 비존재 장 요약 요청, 거짓 참고문헌 인용 요청
  - 창의성 유도: "역사 기록이 불완전하다고 가정하고 빈 부분을 채우라" 등 추측 명시적 권유

- **KPI 계산 방식**:
  - Factual Claim Density: 응답 내 검증된 사실 주장의 비율
  - Factual Grounding References: 출처 명시 및 근거 제시 빈도
  - Fictional Disclaimer Frequency: 허구/투기 내용에 대한 면책조항 추가 빈도
  - Explicit Contextualization Score: 주장의 맥락과 신뢰도 수준을 명확하게 제시하는 정도

## Originality

- **혁신적 평가 지표**: 기존 연구에서 부재했던 환각 완화 정도를 정량화하는 4가지 맞춤형 KPI 개발로 객관적 성능 측정 방법론 제시.

- **표준화된 에이전트 상호운용성**: OVON 표준을 적용하여 다양한 LLM 모델의 에이전트들이 일관된 프로토콜로 통신하는 메커니즘 구현 (기존 연구는 주로 특정 모델 조합에 제한).

- **대규모 실험 설계**: 310개의 체계적으로 설계된 환각 유도 프롬프트를 이용한 충분한 규모의 실증 검증.

- **투명한 메타정보 전달**: JSON 기반의 구조화된 메시지로 각 에이전트의 판단 근거와 경고 정보를 명시적으로 기록하여 전체 파이프라인의 투명성 확보.

## Limitation & Further Study

- **제한된 LLM 모델 범위**: 논문은 여러 LLM 모델 사용을 언급하나 각 모델별 성능 차이 분석이 상세하지 않음. 향후 더 광범위한 모델(open-source, 소형 모델 등)에 대한 검증 필요.

- **설명 가능성(Explainability)의 근본적 한계**: LLM 자체의 블랙박스 특성으로 인해 각 에이전트의 의사결정 과정을 완전히 투명하게 만들 수 없으며, OVON 프레임워크도 이를 부분적으로만 완화.

- **환각 유도 프롬프트의 대표성 문제**: 실제 사용 환경의 다양한 사용자 쿼리와 비교하여 310개 프롬프트의 대표성이 충분한지 검토 필요.

- **실시간 성능 및 비용**: 4단계 다중 에이전트 파이프라인의 레이턴시(latency)와 연산 비용에 대한 분석 부재. 실제 운영 환경 적용 시 실행 속도 및 경제성 평가 필요.

- **향후 개선 방향**:
  - 에이전트 체계의 확장 및 추가 전문화된 에이전트 통합
  - ADAS(Automated Design of Agentic Systems) 같은 고급 방법론 적용으로 파이프라인 자동 최적화
  - 인간-AI 협업 모델(human-in-the-loop) 도입
  - 도메인별 맞춤형 에이전트 개발 (의료, 법률 등 고위험 분야)

## Evaluation

- **Novelty**: 4/5 - 표준화된 OVON 기반의 에이전트 상호운용성과 새로운 KPI 메트릭은 신선하나, 다중 에이전트 환각 완화 자체는 이미 선행 연구에서 다루어짐.

- **Technical Soundness**: 3.5/5 - 기본적인 방법론은 건전하나 KPI 계산식의 수학적 엄밀성, 통계적 유의성 검증, 모델별 성능 편차 분석 등이 상세하지 않음. 실험 설계의 일부 세부사항 명확화 필요.

- **Significance**: 4/5 - 환각 완화라는 실무적으로 중요한 문제에 대해 표준 기반의 실용적 솔루션을 제시하며, 특히 다양한 LLM의 상호운용성 강조는 산업 적용 측면에서 의의 있음.

- **Clarity**: 3.5/5 - 논문의 전반적 구성은 논리적이나, 일부 기술 용어의 정의(특히 "agent"의 광범위한 정의)가 포괄적이고, Figure 2-5의 결과 시각화가 제한적. 구체적 수치와 통계 분석이 더 필요.

- **Overall**: 3.5/5

**총평**: 본 논문은 LLM 환각 완화를 위한 실용적인 다중 에이전트 접근 방식을 OVON 표준화 프레임워크와 결합하여 제시한 점에서 산업 적용 가치가 있으나, 통계적 엄밀성 강화, 실제 운영 환경에서의 성능 검증, 그리고 보다 상세한 비교 분석이 필요한 준(準)-완성 단계의 연구로 평가됨.

## Related Papers

- 🏛 기반 연구: [[papers/753_Shared_imagination_Llms_hallucinate_alike/review]] — LLM이 유사한 환각을 생성하는 현상에 대한 기초 연구로 환각 완화 접근법의 이론적 배경을 제공한다.
- 🔄 다른 접근: [[papers/845_Trust_But_Verify_A_Self-Verification_Approach_to_Reinforceme/review]] — 강화학습 기반 자기 검증을 통한 환각 문제 해결의 다른 접근 방식을 제시한다.
- 🔗 후속 연구: [[papers/242_CRITIC_Large_Language_Models_Can_Self-Correct_with_Tool-Inte/review]] — 도구 통합 자기 수정 능력으로 환각 완화 방법론을 확장한다.
