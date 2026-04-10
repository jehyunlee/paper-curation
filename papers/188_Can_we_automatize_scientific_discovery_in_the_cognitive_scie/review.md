---
title: "188_Can_we_automatize_scientific_discovery_in_the_cognitive_scie"
authors:
  - "Akshay K. Jagadish"
  - "Milena Rmus"
  - "Kristin Witte"
  - "Marvin Mathony"
  - "Marcel Binz"
date: "2026.03"
doi: ""
arxiv: ""
score: 4.0
essence: "인지과학에서 대규모언어모델(LLM)과 기초모델(Foundation Models)을 활용하여 과학적 발견의 전체 사이클을 자동화하는 프레임워크를 제안한다. 실험 설계, 행동 데이터 생성, 모델 합성, 반복 최적화의 모든 단계를 in silico로 구현하는 고속의 자동화된 인지과학 엔진이다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/AI_Research_Ideation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Jagadish et al._2026_Can we automatize scientific discovery in the cognitive sciences.pdf"
---

# Can we automatize scientific discovery in the cognitive sciences?

> **저자**: Akshay K. Jagadish, Milena Rmus, Kristin Witte, Marvin Mathony, Marcel Binz, Eric Schulz | **날짜**: 2026-03-22 | **URL**: [https://arxiv.org/abs/2603.20988](https://arxiv.org/abs/2603.20988)

---

## Essence

![Figure 1](figures/fig1.webp)

*Figure 1. An automated cycle of scientific discovery in the cognitive sciences. An experimentalist proposes experiments,*

인지과학에서 대규모언어모델(LLM)과 기초모델(Foundation Models)을 활용하여 과학적 발견의 전체 사이클을 자동화하는 프레임워크를 제안한다. 실험 설계, 행동 데이터 생성, 모델 합성, 반복 최적화의 모든 단계를 in silico로 구현하는 고속의 자동화된 인지과학 엔진이다.

## Motivation

- **Known**: 인지과학은 전통적으로 연구자들이 실험 패러다임을 개발하고 데이터를 수집하며 미리 정의된 모델 클래스를 테스트하는 수동적 발견 사이클을 따른다. 이 과정은 인간의 개입이 느리고 연구자의 직관에 제한된 가설 공간만 탐색하는 한계가 있다.
- **Gap**: 자동화된 LLM과 기초모델의 기술이 각 발견 사이클 단계를 구현할 수 있게 되었으나, 실험 공간을 효과적으로 정의하는 형식언어(formal language), 높은 충실도의 행동 데이터 생성, 대규모 모델 합성, 그리고 과학적 '흥미로움(interestingness)' 개념의 자동화 평가가 여전히 미해결 문제이다.
- **Why**: 인간 개입의 병목 제거로 이론 개발 속도를 획기적으로 가속화하고, 제한된 인간의 직관을 벗어나 더 광범위한 가설 공간을 탐색하며, 확장성 있는 대규모 자동화 발견 엔진을 구축할 수 있기 때문이다.
- **Approach**: LLM을 지능형 실험 샘플러로 사용하여 실험을 자동 제안하고, 인지 기초모델(Centaur)로 개인 특성을 조건화한 고충실도 행동 데이터를 생성하며, LLM 기반 프로그램 합성(GeCCo, FunSearch)으로 대규모 모델 탐색을 수행하고, LLM 비평가(critic)로 '흥미로움' 메트릭을 평가하여 다음 반복을 최적화한다.

## Achievement

![Figure 1](figures/fig1.webp)

*Figure 1. An automated cycle of scientific discovery in the cognitive sciences. An experimentalist proposes experiments,*

- **완전 자동화된 발견 사이클**: 실험 제안, 데이터 생성, 모델 합성, 루프 폐쇄의 4단계를 모두 자동화한 통합 프레임워크 제시
- **LLM 기반 실험 샘플러**: 형식 문법(MDP 기반)을 넘어 LLM이 직접 개념적으로 의미 있는 새로운 실험을 생성하고 반복 개선 가능
- **개인화된 행동 데이터 생성**: 인구통계, 정신의학적 특성 등 메타데이터를 조건화하여 실제 인간 행동과 구분 불가능한 고충실도 합성 데이터 생성
- **고속 모델 합성**: GeCCo와 FunSearch로 인간이 놓칠 수 있는 알고리즘적 가설의 광대한 공간을 목적함수 최적화를 통해 탐색
- **과학적 흥미로움 최적화**: 통계적 정보 이득뿐 아니라 이론적 의미(interestingness)를 LLM 비평가가 평가하여 과학적으로 조명하는 실험 우선순위 결정

## How

![Figure 1](figures/fig1.webp)

*Figure 1. An automated cycle of scientific discovery in the cognitive sciences. An experimentalist proposes experiments,*

- **실험 제안 단계**: MDP 기반 형식 문법으로 시작하되, LLM을 메타-실험 설계자로 활용하여 새로운 인지 패러다임을 직접 샘플링하고 피드백으로 반복 정제
- **데이터 생성 단계**: Centaur 인지 기초모델에 과제 설명과 피험자 메타데이터(연령, 성별, 진단, 설문지 점수 등)를 프롬프트로 입력하여 다중 회차 의사결정 행동 시뮬레이션
- **모델 합성 단계**: GeCCo 파이프라인으로 인지 모델을 Python 함수로 프로그램 합성하고, 예측 성능 피드백으로 반복 개선하거나, FunSearch/진화 알고리즘으로 복잡한 아키텍처 돌연변이 교배
- **루프 폐쇄 단계**: 최적 실험 설계(정보 이득 최대화)와 능동 학습에 기초하되, LLM 비평가 모델이 결과의 '흥미로움'(개념적 수득량)을 평가하여 다음 실험, 피험자 프로필, 모델 탐색 목표 결정", '**피드백 루프**: 각 반복마다 모든 중간 가설과 성능 신호를 기록하여 시스템이 객관적으로 자기 성능을 개선하는 폐쇄 루프 구성

## Originality

- **패러다임 변화**: 인간 중심의 느린 발견 사이클을 고속 자동화 in silico 엔진으로 근본적으로 재설계
- **LLM의 다층적 활용**: 실험 설계자, 데이터 생성 조건화, 모델 합성자, 과학적 비평가로 LLM의 다양한 역할을 계층적으로 조합
- **과학적 흥미로움의 형식화**: 단순 통계적 정보 이득을 넘어 '흥미로움'을 LLM 비평가로 평가하는 새로운 목적함수 도입으로 이론적 의미성 강화", '**개인화된 인지 기초모델**: 피험자 특성(개인차, 정신질환 위험, 생활사)을 조건화하여 이질적 모집단의 행동을 시뮬레이션하는 고급화
- **대규모 모델 탐색**: 손수 만든(handcrafted) 소수 모델 비교에서 진화/LLM 합성을 통한 대규모 알고리즘 가설 공간 탐색으로 전환

## Limitation & Further Study

- **형식 언어의 표현력 한계**: 현재 MDP 기반 문법은 인지 실험의 다양성을 완전히 포괄하지 못하며, LLM을 샘플러로 사용할 때도 경험적 타당성 검증 필요
- **기초모델의 일반화 문제**: Centaur 등 기초모델이 훈련 분포 밖 완전히 새로운 과제로 정말 외삽(extrapolate)할 수 있는지 미해결
- **합성 데이터와 실제 인간행동 간 불일치**: 생성 데이터가 겉으로 인간과 유사하더라도 통계적/인과적 특성이 다를 수 있으며, 실제 피험자 검증 전까지 신뢰도 미지
- **'흥미로움' 메트릭의 주관성**: LLM 비평가도 학습된 데이터 분포에 의존하므로, 진정 혁신적이거나 전통적 과학 가치관을 벗어난 발견을 놓칠 가능성", '**계산 비용과 확장성**: 대규모 모델 합성(FunSearch 등)의 계산 비용이 높으며, 실시간 피드백 루프 실현의 실제 인프라 요구사항 미분명
- **후속 인간 검증의 필요성**: 자동화 발견이 후보 실험과 메커니즘을 제시하지만, 최종적으로는 실제 인간 피험자 연구로 검증해야 하므로 완전 자동화라기보다 반자동화 시스템
- **윤리적 및 편향 이슈**: LLM이 학습한 암묵적 가정과 편향이 실험 설계와 모델 평가에 전승될 위험성, 특히 개인 특성 조건화(정신질환 등)에서의 편향 재생산 위험

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 LLM과 기초모델을 활용한 인지과학의 완전 자동화된 발견 엔진을 제시하는 야심찬 비전으로, 과학적 발견 프로세스를 근본적으로 재설계하고 대규모 이론 개발을 가능하게 한다. 다만 형식 언어 표현력, 합성 데이터 타당성, '흥미로움' 평가의 객관성, 실제 인간 검증이라는 실질적 문제들이 여전히 해결 대기 중이며, 이들을 극복해야 진정한 자동화 발견이 현실화될 수 있을 것으로 보인다.

## Related Papers

- 🔗 후속 연구: [[papers/795_The_AI_Scientist_Towards_Fully_Automated_Open-Ended_Scientif/review]] — 완전 자동화된 과학 발견에서 인지과학 특화 자동화로의 확장
- 🧪 응용 사례: [[papers/673_Researchtown_Simulator_of_human_research_community/review]] — 인간 연구 커뮤니티 시뮬레이터를 인지과학 자동화에 적용한 사례
- 🏛 기반 연구: [[papers/356_From_individual_to_society_A_survey_on_social_simulation_dri/review]] — 사회 시뮬레이션 조사가 인지과학 자동화의 이론적 기반을 제공
- 🔄 다른 접근: [[papers/179_Can_ai_replace_human_subjects_a_large-scale_replication_of_p/review]] — 인간 피험자 대체 AI와 인지과학 자동화의 다른 접근법
- 🏛 기반 연구: [[papers/425_Improving_research_idea_generation_through_data_An_empirical/review]] — 인지과학 분야의 자동화된 과학적 발견 방법론이 연구 아이디어 생성 자동화의 이론적 기반을 제공한다.
