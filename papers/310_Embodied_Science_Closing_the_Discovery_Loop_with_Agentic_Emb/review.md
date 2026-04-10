---
title: "310_Embodied_Science_Closing_the_Discovery_Loop_with_Agentic_Emb"
authors:
  - "Xiang Zhuang"
  - "Chenyi Zhou"
  - "Kehua Feng"
  - "Zhihui Zhu"
  - "Yunfan Gao"
date: "2026.03"
doi: "미제공"
arxiv: ""
score: 4.0
essence: "본 논문은 과학 발견을 고립된 예측 작업이 아닌 물리 세계와의 지속적 상호작용을 통한 폐쇄 루프 프로세스로 재정의하는 **Embodied Science** 패러다임을 제시한다. 이를 구현하기 위해 지각(Perception)–언어(Language)–행동(Action)–발견(Discovery)을 통합하는 PLAD 프레임워크 기반의 에이전틱 구현화 AI 시스템을 제안한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Embodied_AI_Research"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhuang et al._2026_Embodied Science Closing the Discovery Loop with Agentic Embodied AI.pdf"
---

# Embodied Science: Closing the Discovery Loop with Agentic Embodied AI

> **저자**: Xiang Zhuang, Chenyi Zhou, Kehua Feng, Zhihui Zhu, Yunfan Gao, Yijie Zhong, Yichi Zhang, Junjie Huang, Keyan Ding, Lei Bai, Haofen Wang, Qiang Zhang, Huajun Chen | **날짜**: 2026-03-20 | **DOI**: [미제공](https://doi.org/)

---

## Essence

![Figure 1](figures/fig1.webp)
*Figure 1: 예측 중심 AI4S에서 embodied science으로의 전환. 좌측은 기존의 인간-오케스트레이션 워크플로우, 우측은 폐쇄 루프의 PLAD 프레임워크를 보여줌*

본 논문은 과학 발견을 고립된 예측 작업이 아닌 물리 세계와의 지속적 상호작용을 통한 폐쇄 루프 프로세스로 재정의하는 **Embodied Science** 패러다임을 제시한다. 이를 구현하기 위해 지각(Perception)–언어(Language)–행동(Action)–발견(Discovery)을 통합하는 PLAD 프레임워크 기반의 에이전틱 구현화 AI 시스템을 제안한다.

## Motivation

- **Known**: AI는 단백질 구조 예측, 분자 성질 예측, 합성 설계 등에서 뛰어난 능력을 보여주고 있음. LLM 기반 에이전트는 고수준의 과학적 의도를 실험 계획으로 번역하고, 로봇 실험실은 잘 정의된 공간 내에서 신뢰성 있는 실행을 가능하게 함.

- **Gap**: 현재 AI4S 접근법은 두 가지로 분화: (1) 인지 중심(reasoning-centric)은 강력하지만 기기 수준의 피드백과 물리적 제약에 약하게 접지(grounded)되고, (2) 실행 중심(execution-centric)은 견고하지만 사전 정의된 목표와 절차적 경계 내에서만 최적화됨. 모듈의 단순 통합으로는 구조적 문제 해결 불가.

- **Why**: 과학 발견은 본질적으로 물리적이며 장기적 프로세스. 가설 형성→실험 설계→물리적 실행→분석→모델 수정의 반복 사이클이 필수. 예측 모델이 우수해도 시스템이 다음 단계를 결정하지 못하거나, 기기 신호를 감지하지 못하거나, 결정을 실행 가능한 실험 작업으로 변환하지 못하면 발견 과정이 정체됨.

- **Approach**: 과학 발견의 폐쇄 루프 프로세스로의 재정의: 지각(기기 신호), 인지(과학적 추론), 행동(실험실 개입), 발견(결과 내재화)의 통합을 통해 장기 자율 발견 시스템 구현.

## Achievement

![Figure 2](figures/fig2.webp)
*Figure 2: 장기 자율 과학 발견을 위한 PLAD 루프. 지각은 원시 기기 신호를 변환하고, 추론과 계획을 통해 다음 실험을 결정하며, 행동으로 물리적 개입을 실행하고, 발견을 통해 결과를 내재화함*

1. **Embodied Science 패러다임 정의**: 과학 발견을 인간이 오케스트레이션하는 느슨한 연결의 단계적 프로세스에서 AI가 직접 참여하는 폐쇄 루프 프로세스로 전환하는 이론적 프레임워크 제시.

2. **PLAD 프레임워크 개발**: Perception(기기 신호 해석), Language(과학적 추론 및 계획), Action(실험실 개입), Discovery(통찰력 내재화)의 네 가지 핵심 기능을 통합하는 통일된 시스템 아키텍처 제안.

3. **Agentic Embodied AI 정의**: (1) 장기 목표 관리 능력, (2) 실험 루프 내 구체적 인터페이스(원시 기기 스트림, 작동 상태, 작동 기제), (3) 장기 지속성(메모리, 추적성, 모니터링, 복구 동작)을 필수 속성으로 하는 에이전틱 시스템의 구체적 정의.

## How

![Figure 3](figures/fig3.webp)
*Figure 3: 과학 발견에서 PLAD 인스턴스화. (a) 효소 설계: 구조적 및 기능적 지각이 언어 기반 추론을 유도하고, 변이 실험을 설계하며, 생화학적 검증을 통해 효소 속성을 발견함*

- **지각(Perception)**: 기기에서 생성된 생 데이터(스펙트럼, 크로마토그램, 현미경 영상, 센서 로그, 보정 추적)를 다모달, 불완전한 신호로 해석. 목표 지향적 감지(적응형 확대, 재측정, 재보정, 이상 감지 시 양식 전환) 수행.

- **언어 기반 추론(Language-grounded Reasoning)**: 불확실성 하에서의 실험 추론, 비용과 우발상황을 고려한 계획 수립, 증거 축적에 따른 가설 수정. 다음 실험 선택뿐 아니라 측정 대상, 개입 시점, 가설 수정 방식 결정.

- **행동(Action)**: 시약 조작, 기기 구성, 프로토콜 실행, 안전 제약 유지, 오류 복구의 정확하고 검증 가능한 행동. 권장사항을 발견으로 성숙시키기 위한 필수 요소.

- **발견(Discovery)**: 각 사이클의 결과를 내재화하여 이후 탐색을 구동하는 과학적 통찰력으로 변환. 기기 드리프트, 확률적 결과, 축적된 불확실성을 넘어 자율 운영 지속.

## Originality

- **새로운 개념 프레임워크**: "Embodied Science"와 "Agentic Embodied AI"라는 명확한 정의와 함께 장기 자율 과학 발견의 운영 기준을 제시. 기존 AI4S 문헌의 인식론적 격차를 명확히 함.

- **구조적 문제 인식**: 인지 중심과 실행 중심 시스템의 분화가 단순한 통합으로 해결 불가능한 구조적 문제임을 논증. 폐쇄 루프의 세 가지 필수 요소(지각, 인지, 행동)의 외부화 불가능성 강조.

- **다학제적 통합**: 물리적 로봇공학, LLM 기반 추론, 계측학, 실험 심리학을 아우르는 통합 관점. 기존 AI4S 연구와 구별되는 본질적 차이 제시.

- **장기성과 재현성**: 단일 에피소드 이상의 여러 완전한 발견 사이클 수행을 요구하는 높은 자율성 기준 제시. 추적성(provenance), 안전, 재현성 유지 조건 명시.

## Limitation & Further Study

- **구현 세부사항 부족**: 논문의 대부분은 제시된 텍스트(15,000자) 범위 내에서 개념적 프레임워크 소개에 그침. PLAD의 구체적 알고리즘, 아키텍처, 실제 사례 연구의 상세한 구현이 후속 섹션(전문 제공 안 됨)에서 다루어져야 함.

- **기술적 도전 과제 명시 필요**: Figure 4에서 언급된 "장기 PLAD 루프 유지를 위한 도전과 설계 해결"의 구체적 내용이 제시되지 않음. 기기 드리프트, 확률성, 안전 제약 등의 실제 해결 방안 필요.

- **검증 및 평가 부재**: 현재까지의 텍스트에서 실제 실험실 환경이나 복잡한 과학 문제에 대한 구체적 사례 검증 부재. 효소 설계, 신약 발견 등 실제 응용 분야에서의 성과 검증 필요.

- **인간-AI 협업의 역할 모호**: "최소한의 인간 개입"이란 명시되나, 장기적으로 어느 단계에서 인간 전문가의 개입이 필수적이고 어느 정도가 자율적으로 가능한지에 대한 구체적 경계 정의 부족.

- **확장성과 비용 고려**: 로봇 실험실, 멀티모달 기기 인터페이스, 실시간 모니터링 인프라의 광범위한 도입에 따른 비용, 표준화, 상호운용성 문제에 대한 논의 미흡.


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 3.5/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 AI 기반 과학 발견의 패러다임 전환을 제시하는 중요한 관점의 논문으로, "Embodied Science"라는 명확한 개념 프레임워크와 PLAD 통합 아키텍처를 통해 기존 분산된 AI4S 접근법의 구조적 한계를 날카롭게 지적한다. 특히 폐쇄 루프 자율 발견의 운영 기준을 정의한 점은 향후 과학 AI 연구의 벤치마크로 기여할 것으로 판단된다. 다만, 제시된 부분의 범위 내에서는 구체적인 알고리즘, 실제 구현 사례, 기술적 도전과제의 해결 방안이 충분히 상세하게 다루어지지 않아, 완전한 기술적 타당성 검증을 위해서는 후속 섹션과 실험 결과에 대한 검토가 필수적이다.

## Related Papers

- 🏛 기반 연구: [[papers/655_ReAct_Synergizing_Reasoning_and_Acting_in_Language_Models/review]] — ReAct의 추론과 행동 통합 패러다임은 Embodied Science의 PLAD 프레임워크에서 언어-행동 통합의 기초가 된다.
- 🧪 응용 사례: [[papers/141_Autonomous_robotic_system_with_optical_coherence_tomography/review]] — 광학 코히런스 단층촬영을 사용한 자율 로봇 시스템은 Embodied Science 패러다임의 구체적인 실현 사례다.
- 🔗 후속 연구: [[papers/745_Self-driving_laboratories_to_autonomously_navigate_the_prote/review]] — 단백질 공간 탐색을 위한 자율 연구소는 Embodied Science의 물리적 세계 상호작용 개념을 생물학적 발견으로 확장한다.
- 🏛 기반 연구: [[papers/141_Autonomous_robotic_system_with_optical_coherence_tomography/review]] — 체현된 과학 발견의 구체적 구현 사례로서 물리적 실험과 AI의 결합 가능성을 실증한다.
