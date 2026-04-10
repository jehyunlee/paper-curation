---
title: "003_A_comprehensive_survey_of_cross-domain_policy_transfer_for_e"
authors:
  - "Haoyi Niu"
  - "Jianming Hu"
  - "Guyue Zhou"
  - "Xianyuan Zhan"
date: "2024"
doi: ""
arxiv: ""
score: 4.0
essence: "구현 로봇(embodied agents)을 위한 크로스 도메인 정책 전이(cross-domain policy transfer) 방법들을 체계적으로 검토한 종합 서베이. 시뮬레이션, 실험실 등 저비용 소스 도메인의 데이터를 실제 환경(타겟 도메인)에 효과적으로 전이하는 기술들을 분류 및 분석."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Scientific_Agent_Frameworks"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Niu et al._2024_A comprehensive survey of cross-domain policy transfer for embodied agents.pdf"
---

# A comprehensive survey of cross-domain policy transfer for embodied agents

> **저자**: Haoyi Niu, Jianming Hu, Guyue Zhou, Xianyuan Zhan | **날짜**: 2024 | **URL**: [https://arxiv.org/abs/2402.04580](https://arxiv.org/abs/2402.04580)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1: The main architecture of the survey: domain gap taxonomy, overarching insights on methodologies, and future tr*

구현 로봇(embodied agents)을 위한 크로스 도메인 정책 전이(cross-domain policy transfer) 방법들을 체계적으로 검토한 종합 서베이. 시뮬레이션, 실험실 등 저비용 소스 도메인의 데이터를 실제 환경(타겟 도메인)에 효과적으로 전이하는 기술들을 분류 및 분석.

## Motivation

- **Known**: 로봇 학습과 구현 AI 분야에서 대규모 고품질 학습 데이터의 필수성이 인정되고 있으며, 시뮬레이션과 현실 간의 도메인 갭(domain gap)이 정책 전이의 주요 장애물임이 알려져 있다.
- **Gap**: 기존 크로스 도메인 정책 전이 연구들이 다양한 도메인 갭 유형, 학습 패러다임, 데이터 제약 조건에 따라 분산되어 있어 전체적인 이해가 어렵고, 체계적 분류와 방법론적 통합이 부재한 상태이다.
- **Why**: 현실 환경에서의 비용이 많이 드는 데이터 수집과 안전 문제를 해결하고, 소스 도메인의 기존 데이터를 효과적으로 활용하기 위해 도메인 갭을 극복하는 정책 전이 기술이 필수적이다.
- **Approach**: 도메인 갭을 외형(appearance), 시점(viewpoint), 동역학(dynamics), 형태(morphology)의 4가지로 분류하고, 각 갭에 대한 기존 정책 전이 방법들을 체계적으로 정리 및 분석하여 방법론적 통찰력을 제시.

## Achievement

![Figure 1](figures/fig1.webp)

*Figure 1: The main architecture of the survey: domain gap taxonomy, overarching insights on methodologies, and future tr*

- **도메인 갭의 정규화된 분류**: 환경 불일치와 구현체 불일치를 구분하여 appearance, viewpoint, dynamics, morphology gap을 명확히 정의 및 분류
- **포괄적 방법론 정리**: 시각 도메인 적응(visual domain adaptation), 도메인 랜덤화(domain randomization), 동역학 전이 등 기존 정책 전이 기법들을 체계적으로 분석
- **개념적 통합 프레임워크**: Domain-Dependent MDP(D-MDP)와 정규화된 표기법을 통해 서로 다른 크로스 도메인 정책 전이 문제들을 통일된 관점에서 이해 가능하게 제시
- **향후 연구 방향 제시**: 현존 패러다임의 한계를 분석하고 오픈 챌린지 및 미래 연구 방향을 제안

## How

![Figure 1](figures/fig1.webp)

*Figure 1: The main architecture of the survey: domain gap taxonomy, overarching insights on methodologies, and future tr*

- Domain과 Domain-Dependent MDP(D-MDP)를 엄밀히 정의하여 크로스 도메인 정책 전이 문제를 형식화
- 도메인 갭을 환경 불일치(appearance, viewpoint gap)와 구현체 불일치(dynamics, morphology gap)로 계층적으로 분류
- 크로스 외형 정책 전이: CycleGAN 기반 이미지 변환, 의미론적 분할(semantic segmentation), 도메인 랜덤화, 시각 데이터 증강(visual data augmentation) 등의 기법 검토
- 각 도메인 갭 범주에 대해 표현 학습, 적응 알고리즘, 도메인 일반화(domain generalization) 등의 방법론적 접근법 분석
- 실제 로봇 배포 사례와 벤치마크를 통한 기존 방법들의 효과성 비교 검토

## Originality

- 크로스 도메인 정책 전이를 위한 **첫 번째 종합적 서베이** 제시로 분산된 연구들을 통합적으로 정리
- 도메인 갭을 체계적으로 분류하고 각 갭 유형 간의 **구별 및 연결성** 명확화
- D-MDP 정의를 통해 다양한 크로스 도메인 정책 전이 문제를 **통일된 수학적 프레임워크**로 표현
- 방법론적 통찰력을 제공하여 기존 기법들의 **내재적 연관성과 차이점** 규명
- 오픈 소스 저장소(GitHub)를 통한 **지속적 업데이트 계획**으로 동적 지식 관리

## Limitation & Further Study

- **방법론의 세부 성능 비교 부족**: 각 접근법의 구체적인 성능 메트릭과 직접 비교가 제한적이며, 통합된 벤치마크 평가가 부재
- **실제 구현 난제의 논의 부족**: 방법론 이론적 분석에 집중되어 있으며, 실제 로봇 시스템에서의 구현 복잡성이나 계산 비용에 대한 논의가 제한적
- **다중 도메인 갭 상호작용 분석 미흡**: 여러 도메인 갭이 동시에 존재할 때의 상호작용과 누적 효과에 대한 심화 분석이 필요
- **후속 연구 방향**: 멀티모달 정보 통합, 메타 학습 기반 접근법, 온라인 적응(online adaptation) 기법의 발전이 필요하며, 비전 기반 접근에서 다른 센서 모달리티로의 확장 연구가 요구됨

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 이 서베이는 크로스 도메인 정책 전이 분야의 첫 체계적 검토로서, 분산된 연구들을 통합하고 도메인 갭을 명확히 분류하여 해당 분야에 중요한 기초 자료를 제공한다. 로봇 학습과 구현 AI의 실세계 배포를 위한 필수적인 기술 영역을 포괄적으로 정리하여 향후 연구 방향을 제시하는 가치 있는 기여이다.

## Related Papers

- 🧪 응용 사례: [[papers/422_Improving_generalization_of_robot_locomotion_policies_via_sh/review]] — 로봇 보행 정책의 일반화 개선을 통해 크로스 도메인 정책 전이의 실제 적용 사례를 제시한다.
- 🔗 후속 연구: [[papers/662_Reinforcement_Learning_for_Dynamic_Microfluidic_Control/review]] — 오프라인 강화학습의 로봇 제어 견고성을 크로스 도메인 정책 전이로 확장한다.
