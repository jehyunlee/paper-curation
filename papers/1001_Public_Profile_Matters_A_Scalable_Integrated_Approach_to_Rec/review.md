---
title: "1001_Public_Profile_Matters_A_Scalable_Integrated_Approach_to_Rec"
authors:
  - "Karan Goyal"
  - "Dikshant Kukreja"
  - "Vikram Goyal"
  - "Mukesh Mohania"
date: "2026.03"
doi: "10.48550/arXiv.2603.17361"
arxiv: ""
score: 4.0
essence: "논문은 인용 추천 시스템에서 인간의 인용 행동 패턴(public profile)을 효율적으로 캡처하는 경량 모듈 Profiler와 적응형 벡터 게이팅을 통해 신뢰도 사전정보와 의미론적 정보를 통합하는 DAVINCI 모델을 제안하며, 현실적인 귀납적(inductive) 평가 설정을 도입하여 새로운 최첨단 성능을 달성한다."
tags:
  - "cat/Scientific_Information_Systems"
  - "sub/Citation_and_Bibliometric_Analysis"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Goyal et al._2026_Public Profile Matters A Scalable Integrated Approach to Recommend Citations in the Wild.pdf"
---

# Public Profile Matters: A Scalable Integrated Approach to Recommend Citations in the Wild

> **저자**: Karan Goyal, Dikshant Kukreja, Vikram Goyal, Mukesh Mohania | **날짜**: 2026-03-18 | **DOI**: [10.48550/arXiv.2603.17361](https://doi.org/10.48550/arXiv.2603.17361)

---

## Essence

![Figure 2](figures/fig2.webp)

*Figure 2: The architecture of our two-stage citation recommendation system. (1) The non-learnable Profiler*

논문은 인용 추천 시스템에서 인간의 인용 행동 패턴(public profile)을 효율적으로 캡처하는 경량 모듈 Profiler와 적응형 벡터 게이팅을 통해 신뢰도 사전정보와 의미론적 정보를 통합하는 DAVINCI 모델을 제안하며, 현실적인 귀납적(inductive) 평가 설정을 도입하여 새로운 최첨단 성능을 달성한다.

## Motivation

- **Known**: 기존 인용 추천 시스템은 텍스트 정보를 활용하며, 최근 연구들은 인간의 인용 패턴을 반영하여 성능을 개선하고 있다. 다만 높은 계산 비용과 체계적 편향(systematic bias)이 문제로 지적되어 왔다.
- **Gap**: 현재 평가 프로토콜은 전이적(transductive) 설정으로 평가하여 실제 상황(새로운 논문에 대한 인용 추천)을 반영하지 못하고 있으며, 기존 방법들은 계산 효율성과 편향 제거 사이의 균형을 맞추지 못하고 있다.
- **Why**: 과학 출판물의 급속한 증가로 자동화된 인용 추천 시스템의 필요성이 증대되었으며, 현실 조건에 맞는 평가 방식이 시스템의 실제 적용 가능성을 판단하는 데 중요하기 때문이다.
- **Approach**: 논문은 비학습 기반의 경량 Profiler 모듈로 인용 패턴을 포착하고, 시간적 제약을 적용한 귀납적 평가 설정을 제안하며, 적응형 벡터 게이팅(adaptive vector-gating mechanism)을 통해 신뢰도 사전정보와 의미론적 정보를 통합하는 DAVINCI 모델을 구축한다.

## Achievement

![Figure 3](figures/fig3.webp)

*Figure 3: The indispensable role of the public profile.*

- **Profiler 모듈**: 비학습 기반의 경량 모듈로 인간의 인용 행동 패턴을 효율적으로 캡처하며, 기존의 sequential prefetcher+enricher 조합을 초과하는 성능을 달성하면서도 확인 편향(confirmation bias)을 제거
- **Public Profile의 중요성**: 연구 생태계가 논문을 인식하는 방식('public profile')이 인용 추천을 위한 매우 중요한 신호임을 실증적으로 입증", '**DAVINCI 리랭킹 모델**: 적응형 벡터 게이팅 메커니즘을 통해 신뢰도 사전정보와 의미론적 정보를 통합하며, 특수 메타데이터(분류법) 없이도 다양한 데이터셋에 일반화 가능
- **귀납적 평가 설정**: 시간적 제약을 적용하여 실제 상황을 반영하는 현실적인 평가 프레임워크를 제안하고 벤치마킹
- **최첨단 성능**: 여러 벤치마크 데이터셋(ACL-200, FTPR, RefSeer, arXiv, ArSyTa)에서 전문화된 LCR 시스템과 대규모 오픈소스 리랭커를 능가하는 새로운 최첨단 결과 달성

## How

![Figure 2](figures/fig2.webp)

*Figure 2: The architecture of our two-stage citation recommendation system. (1) The non-learnable Profiler*

- Profiler: 논문의 '공개 프로필'(인용 빈도, 영향도 등)에 기반한 신뢰도 점수 산출을 통해 후보 문서 검색", 'DAVINCI: 적응형 벡터 게이팅을 이용하여 Profiler의 신뢰도 사전정보(confidence priors)와 심층 의미론적 분석 결과를 판별적으로 융합
- 귀납적 평가: 평가 쿼리 문서와 후보 코퍼스의 완전한 분리(Deval ∩ C = ∅) 및 시간적 일관성(temporal consistency) 제약 적용
- 2단계 아키텍처: 효율적인 검색 단계(Profiler)와 정교한 리랭킹 단계(DAVINCI)로 구성하여 속도와 정확도 최적화

## Originality

- 비학습 기반 Profiler 개념: 기존의 복잡한 enricher(symbiotic neighbourhood 관계 포착)를 대체하면서도 더 효율적인 접근법 제시
- 공개 프로필(public profile)의 신호 활용: 인간의 인용 행동을 포착하는 새로운 관점으로, 개별 논문의 영향도와 명성을 기반으로 한 추천
- 귀납적 평가 설정의 도입: 전이적 설정의 근본적 한계를 지적하고 시간적 일관성을 강제하는 엄격한 평가 프로토콜 정의
- 적응형 벡터 게이팅: 신뢰도 사전정보와 의미론적 정보의 통합에 있어 새로운 메커니즘 제안

## Limitation & Further Study

- **메타데이터 의존성**: Profiler는 논문의 인용 통계 정보 접근 가능성에 의존하며, 신규 또는 저명도가 낮은 논문에 대해서는 신뢰도 점수 산출이 제한될 수 있음
- **cold-start 문제**: 공개 프로필이 부족한 새로운 출판물에 대한 추천 성능 평가 필요
- **평가 데이터셋 편향**: ArXiv, RefSeer 등 특정 분야의 논문들로 구성된 데이터셋 사용으로 인한 도메인 특화성 문제
- **후속 연구**: (1) 다양한 학문 분야에 대한 일반화 성능 평가, (2) 실시간 동적 환경에서의 Profiler 업데이트 전략 개발, (3) 저명도 정보가 부족한 신규 논문에 대한 하이브리드 접근법 연구

## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 논문은 인용 추천 시스템의 효율성, 편향 제거, 현실성을 동시에 개선하는 포괄적인 해결책을 제시하며, 특히 귀납적 평가 설정의 도입은 향후 연구의 평가 기준을 재정의하는 중요한 기여이다. Profiler의 경량성과 DAVINCI의 일반화 가능성은 실무 적용 가능성이 높다.

## Related Papers

- 🔄 다른 접근: [[papers/1066_Accelerating_science_with_human-aware_artificial_intelligenc/review]] — 인용 추천에서 인간의 행동 패턴 대신 과학자의 전문성 분포를 AI에 통합하는 다른 접근법을 제시한다.
- 🧪 응용 사례: [[papers/1073_MOLIERE_Automatic_Biomedical_Hypothesis_Generation_System/review]] — 생물의학 분야에서 자동화된 가설 생성을 통해 인용 추천 시스템의 응용 가능성을 보여준다.
- 🔄 다른 접근: [[papers/994_Organisational_accounts_engaged_in_scholarly_communication_o/review]] — 연구자 프로필 관리에 대한 통합적 접근법으로 소셜미디어 활동과 다른 관점을 제시한다
