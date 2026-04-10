---
title: "175_Building_machines_that_learn_and_think_with_people"
authors:
  - "Katherine M. Collins"
  - "Ilia Sucholutsky"
  - "Umang Bhatt"
  - "Kartik Chandra"
  - "Lionel Wong"
date: "2024.10"
doi: "10.1038/s41562-024-01991-9"
arxiv: ""
score: 4.2
essence: "인공지능이 단순한 생각의 도구를 넘어 인간과 함께 사고하는 파트너(사고 파트너, thought partner)로 발전해야 한다는 관점에서, 협력적 인지(collaborative cognition)의 원리를 기반으로 설계된 AI 시스템의 필요성과 구현 방안을 제시한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Embodied_AI_Research"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Collins et al._2024_Building machines that learn and think with people.pdf"
---

# Building machines that learn and think with people

> **저자**: Katherine M. Collins, Ilia Sucholutsky, Umang Bhatt, Kartik Chandra, Lionel Wong, Mina Lee, Cedegao E. Zhang, Tan Zhi-Xuan, Mark Ho, Vikash Mansinghka, Adrian Weller, Joshua B. Tenenbaum, Thomas L. Griffiths | **날짜**: 2024-10 | **DOI**: [10.1038/s41562-024-01991-9](https://doi.org/10.1038/s41562-024-01991-9)

---

## Essence

인공지능이 단순한 생각의 도구를 넘어 인간과 함께 사고하는 파트너(사고 파트너, thought partner)로 발전해야 한다는 관점에서, 협력적 인지(collaborative cognition)의 원리를 기반으로 설계된 AI 시스템의 필요성과 구현 방안을 제시한다.

## Motivation

- **Known**: 현재 AI 시스템, 특히 대규모 언어 모델(LLM)은 자연언어 인터페이스를 통해 인간과 상호작용하며 일부 인지 작업에서 인간 수준의 성능을 보임

- **Gap**: 기존 스케일링 기반 접근법(웹 규모 데이터와 인간 피드백을 통한 학습)은 인간의 행동을 모방하지만, 명시적 추론, 타자 이해, 세계 모델링 등 진정한 사고 파트너십에 필요한 인지 능력을 강건하게 시뮬레이션하지 못함

- **Why**: 기술 발전에도 불구하고 프로그래밍 어시스턴트의 신뢰성 부족, 실구현 로봇의 계획 능력 한계, 의료 진단의 안전성 문제 등은 단순한 행동 모방 이상의 인간 중심 설계가 필요함을 보여줌

- **Approach**: 계산인지과학(computational cognitive science)의 베이지안 접근법을 활용하여, 인간과 세계에 대한 명시적 구조화된 모델을 구축하고 추론하는 AI 시스템 설계 방안 제시

## Achievement

![Fig. 1 | Examples of ecosystems for thinking](https://example.com/fig1.png) *인간이 함께 생각해온 다양한 생각의 생태계와 기계가 이를 어떻게 확장할 수 있는지 보여주는 사례*

1. **협력적 사고의 모드 체계화**: 협력적 계획(collaborative planning), 협력적 학습(collaborative learning), 협력적 숙의(collaborative deliberation), 협력적 의미 파악(collaborative sense-making), 협력적 창작(collaborative creation)의 5가지 주요 모드를 정의하고, 각 모드별 핵심 과제(예: 신뢰할 수 있는 목표 추론, 개인화된 학습 속도, 검증 가능한 추론)를 명확히 제시

2. **다영역 실제 사례 분석**: 프로그래밍 어시스턴트, 구체화된 보조 로봇(embodied assistive robots), 창작 지원(storytelling), 의료 진단 등 4개 도메인에서 현재 기술의 한계와 사고 파트너십의 요구사항을 구체적으로 분석

3. **설계 원칙(desiderata) 제안**: 효과적인 인간-호환 사고 파트너십을 위한 3가지 필수 요건 제시:
   - 인간을 이해할 수 있는 능력(understand us)
   - 인간이 이해 가능한 설명성(we can understand)
   - 공통의 기반이 되는 세계 이해(understanding of world)

## How

![Fig. 2 | Case study depictions](https://example.com/fig2.png) *WatChat이 사용자의 오류가 있는 정신 모델을 추론하는 사례*

- **베이지안 프레임워크 채택**: 확률 생성 모델(probabilistic generative models)을 통해 인간과 세계에 대한 명시적 모델을 구축하고, 관찰된 행동과 진술로부터 숨겨진 신념, 의도, 목표를 추론

- **구조화된 표현 결합**: 기초 모델(foundation models)과 확률 프로그래밍(probabilistic programming), 목표 지향 탐색(goal-directed search), 에이전트 추론(agent reasoning)을 통합하여 단순한 분포 학습(distributional learning)을 넘어선 체계적 추론 능력 구현

- **자원 합리성 원칙 적용**: 제한된 작업 메모리 등 인간의 인지적 제약을 이해하고, 이를 모델에 반영하여 인간-호환적 설계 달성

- **불확실성 명시화**: 시스템이 자신의 불확실성을 표현하고, 인간의 신념과 목표에 대한 불확실성을 추론하며, 이를 협력 과정에 반영

- **반복적 학습과 적응**: 상호작용을 통해 인간의 정신 모델을 지속적으로 업데이트하고, 개인의 지식과 선호도에 맞춰 맞춤형 지원 제공

## Originality

- 기존 스케일링 중심의 AI 개발 패러다임에서 **인간 중심 설계 패러다임으로의 근본적 전환** 제시

- 인지심리학과 계산인지과학의 수십 년 축적된 이론을 AI 시스템 설계에 체계적으로 적용하는 **학제 간 통합 접근**

- 추상적 개념인 "사고 파트너"를 5가지 협력 모드, 구체적 도메인 분석, 명확한 설계 원칙으로 **운영 가능한 설계 틀로 전환**

- 기초 모델 기반 스케일링이 아닌 **베이지안 구조적 모델링을 통한 새로운 스케일링 경로** 제안

- 협력적 인지를 단순한 기술 기능이 아닌 **인간의 근본적 사고 방식**으로 이해하는 철학적 재정의

## Limitation & Further Study

- **이론의 실제 구현 격차**: 제시된 베이지안 모델링 접근법의 구체적인 구현 사례와 성과에 대한 실증적 증거가 논문 범위 내에서 제한적임. 특히 복잡한 현실 도메인에서의 확장성에 대한 검증 부족

- **계산 복잡성 미해결**: 인간과 세계의 명시적 모델을 구축하고 유지하는 계산 비용이 대규모 데이터 학습보다 효율적인지에 대한 분석 부족

- **인간의 다양성 고려 미흡**: 서로 다른 배경, 전문성, 인지 스타일을 가진 사용자 집단에 대한 분화된 접근이 체계화되지 않음

- **후속 연구 방향**:
  - 각 협력 모드별 구체적인 알고리즘 및 아키텍처 개발
  - 도메인별로 설계된 사고 파트너의 사용자 연구를 통한 효과성 검증
  - 인간-AI 협력 시스템의 장기 영향 평가
  - 윤리적 가치 정렬과 신뢰 메커니즘의 구현 방안
  - 하이브리드 인간-AI 팀의 성능 최적화 연구

## Evaluation

- **Novelty**: 4.5/5
  - AI의 역할을 도구에서 파트너로 재정의하는 개념적 혁신은 탁월함
  - 다만 베이지안 구조화 접근 자체는 계산인지과학에서 기존 아이디어의 재적용

- **Technical Soundness**: 3.5/5
  - 이론적 프레임워크는 견고하고 인지과학 문헌에 충실함
  - 실제 기술 구현에 대한 상세한 검토와 성능 평가 부족

- **Significance**: 4.5/5
  - AI 시스템 설계의 패러다임 전환을 촉구하는 중대한 기여
  - 프로그래밍, 로봇, 의료 등 실제 응용 도메인들과의 연결이 강함
  - 다만 즉각적인 기술적 임팩트는 아직 제한적

- **Clarity**: 4/5
  - 복잡한 개념을 표와 구체적 사례로 잘 설명함
  - 일부 기술 용어와 계산인지과학의 개념이 일반 독자에게는 진입 장벽이 될 수 있음

- **Overall**: 4.2/5

**총평**: 이 논문은 스케일링 중심의 현대 AI 개발 패러다임에 대한 중요한 성찰을 제시하며, 인간과 기계가 진정한 협력자로서 함께 사고할 수 있는 시스템의 설계 원칙을 제안한다는 점에서 학술적·실무적 가치가 높다. 다만 제시된 베이지안 구조적 접근의 구체적 구현과 실제 도메인에서의 성능 검증이 후속 연구를 통해 보충되어야 할 것으로 보인다.

## Related Papers

- 🧪 응용 사례: [[papers/358_From_Labor_to_Collaboration_A_Methodological_Experiment_Usin/review]] — Building machines의 협력적 인지 원리가 인문사회과학 연구의 인간-AI 역할 분담 프레임워크에서 구체적으로 구현된 적용 사례이다.
- 🔗 후속 연구: [[papers/361_From_LLM_Reasoning_to_Autonomous_AI_Agents_A_Comprehensive_R/review]] — LLM 추론에서 자율 AI 에이전트로의 발전 조사가 인간과 함께 사고하는 AI 시스템으로의 진화 과정을 포괄적으로 확장한 연구이다.
- 🏛 기반 연구: [[papers/838_Training_socially_aligned_language_models_in_simulated_human/review]] — 사회적으로 정렬된 언어 모델 훈련 방법이 인간과 협력적으로 사고하는 AI 파트너 개발의 핵심 기술적 토대이다.
- 🔗 후속 연구: [[papers/102_Architecture_Design_for_Human-Driven_Systems/review]] — 인간과 함께 학습하고 사고하는 기계 구축 원리를 IoT 환경에서의 소시오-테크니컬 시스템으로 확장할 수 있다.
- 🔗 후속 연구: [[papers/050_Adasociety_An_adaptive_environment_with_social_structures_fo/review]] — AdaSociety의 적응형 사회 구조가 Building machines의 협력적 인지 프레임워크를 다중 에이전트 환경에서 구현한 확장 사례이다.
- 🏛 기반 연구: [[papers/358_From_Labor_to_Collaboration_A_Methodological_Experiment_Usin/review]] — 협력적 인지 원리와 인간-AI 파트너십 개념이 인문사회과학 연구의 해석적 특성을 고려한 역할 분담 설계의 이론적 기반이다.
- 🏛 기반 연구: [[papers/233_Cognitio_emergens_Agency_dimensions_and_dynamics_in_human-ai/review]] — 인간과 함께 학습하고 사고하는 기계 구축의 근본적 철학과 방법론을 제공한다.
