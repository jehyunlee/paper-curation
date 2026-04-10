---
title: "064_Agentic_AI_for_Scientific_Discovery_A_Survey_of_Progress_Cha"
authors:
  - "Mourad Gridach"
  - "Jay Nanavati"
  - "Khaldoun Zine El Abidine"
  - "Lenon Mendes"
  - "Christina Mack"
date: "2025.03"
doi: "N/A"
arxiv: ""
score: 3.8
essence: "LLM(Large Language Model) 기반의 에이전틱 AI 시스템이 과학 연구의 자동화를 혁신하고 있으며, 본 논문은 화학, 생물학, 재료과학 등 다양한 분야에서의 진행 상황, 평가 지표, 구현 프레임워크, 그리고 극복해야 할 과제들을 종합적으로 검토한다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/AI_Chemistry_Planning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Gridach et al._2025_Agentic AI for Scientific Discovery A Survey of Progress, Challenges, and Future Directions.pdf"
---

# Agentic AI for Scientific Discovery: A Survey of Progress, Challenges, and Future Directions

> **저자**: Mourad Gridach, Jay Nanavati, Khaldoun Zine El Abidine, Lenon Mendes, Christina Mack | **날짜**: 2025-03-12 | **DOI**: N/A

---

## Essence

LLM(Large Language Model) 기반의 에이전틱 AI 시스템이 과학 연구의 자동화를 혁신하고 있으며, 본 논문은 화학, 생물학, 재료과학 등 다양한 분야에서의 진행 상황, 평가 지표, 구현 프레임워크, 그리고 극복해야 할 과제들을 종합적으로 검토한다.

## Motivation

- **Known**: LLM의 급속한 발전으로 추론(reasoning), 계획(planning), 자율적 의사결정이 가능한 AI 에이전트들이 등장했으며, 이들이 과학 연구의 문헌 검토, 가설 생성, 실험 수행, 결과 분석을 변혁할 수 있는 잠재력을 보유하고 있음
  
- **Gap**: 기존의 LitSearch, ResearchArena, Agent Laboratory 등의 일반적 연구 자동화 프레임워크들이 높은 성공률을 보이지만, 특히 문헌 검토 단계에서 현저히 떨어지는 성능을 보임. 또한 도메인 특화성, 시스템 신뢰성, 재현성, 윤리적 거버넌스에 대한 체계적 이해가 부족함
  
- **Why**: 과학 발견의 자동화는 연구 가속화, 비용 감축, 접근성 확대의 잠재력을 가지고 있지만, 복잡한 워크플로우의 자동화와 인간-AI 협업 메커니즘에 대한 체계적 분석이 필요함
  
- **Approach**: 에이전틱 AI 시스템을 자율 시스템(fully autonomous)과 인간-AI 협업 시스템(human-AI collaborative)으로 분류하고, 데이터셋, 구현 도구, 평가 지표, 그리고 개방형 과제들을 종합적으로 검토

## Achievement

1. **에이전틱 AI의 기초 개념 정립**: 철학에서 비롯된 "에이전시(agency)"의 개념을 AI 맥락에서 재정의하고, 자율성(autonomy), 학습(learning), 메모리(memory), 지각(perception), 계획(planning), 의사결정(decision-making), 행동(action)의 통합 프레임워크 제시

2. **아키텍처 비교 분석**: 단일 에이전트(single agent) vs. 다중 에이전트(multi-agent) 시스템의 장단점을 명확히 구분
   - 단일 에이전트: 잘 정의된 문제와 반복적 작업에 효과적
   - 다중 에이전트: 협업과 도메인 간 교차 필요 시 우수

3. **분야별 성공 사례 카테고리화**:
   - **완전 자율 시스템**: CoScientist(화학 실험 설계·실행), ChemCrow(유기합성·약물발견), ProtAgents(단백질 설계), LLaMP(재료 과학)
   - **인간-AI 협업 시스템**: Virtual Lab(학제 간 연구), BioPlanner(실험 프로토콜 설계), CALMS(실시간 실험 보조), Agent Laboratory(문헌검토-실험-보고서 작성 통합)

4. **문헌 검토 자동화 현황 분석**: SciLitLLM, LitSearch 등의 도구들이 정보 검색과 합성을 개선하였으나, 구조화된 문헌 검토의 엄격성 달성이 여전히 과제임을 지적

## How

- **에이전틱 AI 워크플로우**: 센서 입력 → 자율적 지각 → 계획 수립 → 도구 활용 → 실행 → 피드백 루프를 통한 반복적 개선
  
- **단일 에이전트 구현**: LLM 백본에 기반하여 다중 작업/도메인 처리, 추론과 도구 실행을 독립적으로 수행

- **다중 에이전트 협업**: Minsky의 Society of Mind 이론에 영감을 받아, 도메인별 전문가 에이전트들의 상호작용과 정보 공유를 통한 분산 문제 해결

- **문헌 검토 자동화 기법**: 연속 사전 학습(CPT, Continual Pre-training) + 지도 학습 미세조정(SFT, Supervised Fine-tuning)을 결합한 하이브리드 전략으로 도메인 특화 지식 주입

## Originality

- **포괄적 분류 체계**: 에이전틱 AI를 단순히 기술적으로 구분하지 않고, **자율성 수준**과 **인간 협업의 정도**에 따라 이분법적으로 체계화한 점이 실용적

- **도메인별 사례 연계**: 일반적 AI 진전이 아닌 화학, 생물학, 재료과학 등 **구체적 과학 분야**와의 연결로 적용성 강조

- **실패 사례 분석**: Agent Laboratory의 문헌 검토 단계 성능 저하 사례를 명시적으로 언급하여, 기술의 **현재 한계**를 정직하게 드러냄

- **신뢰성-창의성 트레이드오프 제시**: 완전 자율 시스템이 효율적이나 창의성과 도메인 직관이 필요한 작업에서 인간 감독의 필요성을 명확히 함

## Limitation & Further Study

- **데이터 품질 의존성**: SciLitLLM 등 도메인 특화 시스템들이 고품질 학습 데이터에 의존하는데, 신흥 분야에서는 이러한 데이터 가용성이 제한적

- **문헌 검토 자동화의 근본적 어려움**: 자연언어 이해의 깊이, 도메인 특화 지식, 모호성과 뉘앙스 처리가 여전히 미해결 문제

- **에이전트 간 통신 복잡성**: 다중 에이전트 시스템의 상호운용성, 정보 공유 메커니즘이 단일 에이전트에 비해 관리가 어려움

- **재현성 및 신뢰성 보증**: 자율 실험 수행 시스템의 결과 신뢰도, 재현 가능성에 대한 엄격한 평가 체계 부족

- **윤리적 거버넌스**: 자율 의사결정 시스템의 편향성, 책임성(accountability) 문제에 대한 정책적·기술적 대응 미흡

- **후속 연구 방향**:
  1. 인간-AI 협업에서 **인간 개입의 최적 지점** 연구
  2. 시스템 **캘리브레이션(calibration)** 개선으로 신뢰도 향상
  3. 도메인별 맞춤형 평가 메트릭 개발
  4. 다분야 통합 워크플로우 설계 연구

## Evaluation

- **Novelty**: 3.5/5
  - 개념적 신성은 제한적이나, 과학 응용 분야에서의 **체계적 분류와 비교 분석**은 유용함

- **Technical Soundness**: 3.5/5
  - 기술 내용은 건실하나, 아직 본문이 15,000자 미만으로 추출되어 완전한 기술적 깊이 평가가 어려움. 제시된 사례들은 검증되어 있으나 새로운 방법론 개발은 부재

- **Significance**: 4/5
  - 과학 연구의 **자동화와 가속화**라는 실질적 영향력이 높으며, 산업 및 학계 모두에 직접적 적용 가능성이 있음. 다만, 문헌 검토 자동화 한계 등 미해결 과제가 명확

- **Clarity**: 4.5/5
  - 구조화된 분류, 명확한 용어 정의, 구체적 사례 제시로 가독성이 우수함. ICLR 2025 발표 논문으로 학술 표현 수준이 높음

- **Overall**: 3.8/5

**총평**: 본 논문은 LLM 기반 에이전틱 AI의 과학 응용을 **체계적으로 정리한 중요한 서베이**로, 자율-협업 이분법을 통해 실용적 관점을 제공하나, 현실적 한계(문헌 검토 자동화, 신뢰성 보증)를 직시하고 있다. 다만 새로운 기술 혁신보다는 **기존 기술의 종합·분류** 성격이 강하므로, 추후 구체적 개선 방법론(예: 하이브리드 검색-생성 문헌 분석, 불확실성 정량화)이 필요한 상태이다.

## Related Papers

- 🧪 응용 사례: [[papers/508_LLMs_as_Research_Tools_A_Large_Scale_Survey_of_Researchers_U/review]] — 연구자들의 LLM 사용 현황 조사가 과학 발견을 위한 에이전틱 AI 시스템의 실제 도입과 활용을 보여주는 구체적인 사례이다.
- 🏛 기반 연구: [[papers/693_scAgent_Universal_Single-Cell_Annotation_via_a_LLM_Agent/review]] — 과학 발견을 위한 에이전틱 AI의 종합적 체계가 단일세포 주석과 같은 구체적인 생물학 응용의 이론적 프레임워크를 제공한다.
- 🔗 후속 연구: [[papers/090_AIRS-Bench_a_Suite_of_Tasks_for_Frontier_AI_Research_Science/review]] — 프론티어 AI 연구 과학 에이전트 평가가 과학 발견을 위한 에이전틱 AI의 실제 성능 측정으로 확장된다.
- 🏛 기반 연구: [[papers/508_LLMs_as_Research_Tools_A_Large_Scale_Survey_of_Researchers_U/review]] — 과학 연구를 위한 에이전틱 AI의 종합적 조사가 연구자들의 LLM 사용 현황 조사의 이론적 맥락을 제공한다.
- 🧪 응용 사례: [[papers/693_scAgent_Universal_Single-Cell_Annotation_via_a_LLM_Agent/review]] — 과학 발견을 위한 에이전틱 AI 시스템의 구체적인 생물학 분야 적용 사례로서 단일세포 주석에 특화된다.
- 🧪 응용 사례: [[papers/493_Litllm_A_toolkit_for_scientific_literature_review/review]] — 과학 문헌 리뷰 자동화 도구가 과학 발견을 위한 에이전틱 AI 시스템의 구체적인 문헌 분석 응용 사례이다.
- 🏛 기반 연구: [[papers/090_AIRS-Bench_a_Suite_of_Tasks_for_Frontier_AI_Research_Science/review]] — 과학 발견을 위한 에이전틱 AI 체계가 프론티어 AI 연구 과학 에이전트의 벤치마크 설계 기반을 제공한다.
