---
title: "838_Training_socially_aligned_language_models_in_simulated_human"
authors:
  - "Ruibo Liu"
  - "Ruixin Yang"
  - "Chenyan Jia"
  - "Ge Zhang"
  - "Denny Zhou"
date: "2023"
doi: "arXiv:2305.16960"
arxiv: ""
score: 4.2
essence: "본 논문은 시뮬레이션된 사회적 상호작용을 통해 언어모델을 사회적으로 정렬(socially aligned)시키는 새로운 학습 패러다임을 제시한다. 기존 감독 학습이나 보상 모델링의 한계를 극복하기 위해 다중 에이전트 시뮬레이션 환경(SANDBOX)에서 생성된 상호작용 데이터를 활용하여 보다 견고하고 확장 가능한 정렬 방법을 제안한다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/Cognitive_LLM_Evaluation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Arrieta et al._2023_Training socially aligned language models in simulated human society.pdf"
---

# Training socially aligned language models in simulated human society

> **저자**: Ruibo Liu, Ruixin Yang, Chenyan Jia, Ge Zhang, Denny Zhou, Andrew M. Dai, Diyi Yang, Soroush Vosoughi | **날짜**: 2023 | **DOI**: [arXiv:2305.16960](https://arxiv.org/abs/2305.16960)

---

## Essence

![Figure 1](figures/fig1.webp)
*기존의 RLHF와 달리 Stable Alignment은 시뮬레이션된 사회적 상호작용을 통해 직접 언어모델을 정렬한다*

본 논문은 시뮬레이션된 사회적 상호작용을 통해 언어모델을 사회적으로 정렬(socially aligned)시키는 새로운 학습 패러다임을 제시한다. 기존 감독 학습이나 보상 모델링의 한계를 극복하기 위해 다중 에이전트 시뮬레이션 환경(SANDBOX)에서 생성된 상호작용 데이터를 활용하여 보다 견고하고 확장 가능한 정렬 방법을 제안한다.

## Motivation

- **Known**: 현대의 언어모델(LMs)은 다음 토큰 예측을 통해 우수한 성능을 보이지만, 해롭고 편향된 콘텐츠 생성, 허위정보 확산 등의 문제를 여전히 보인다. 기존 정렬 방법으로는 감독 미세조정(SFT)은 적대적 공격에 취약하고, 보상 모델링(RLHF)은 보상 해킹(reward gaming) 문제를 야기한다.

- **Gap**: 인간은 사회적 상호작용을 통해 사회 규범을 학습하지만, 현재 언어모델은 고립된 환경에서 학습되어 반복적 피드백이나 사회적 학습 경험이 부족하다. 또한 기존 방법들은 확장성이 낮고 인간 라벨링 비용이 높다.

- **Why**: 사회적 상호작용 시뮬레이션을 통해 자동화된 피드백과 반복적 개선을 가능하게 하면, 더 견고하고 효율적인 정렬 학습이 가능할 것이다.

- **Approach**: (1) 다중 언어모델 에이전트로 구성된 시뮬레이션 사회(SANDBOX) 구축, (2) Back-Scatter 메커니즘을 통한 동료 피드백 수집, (3) 3단계 Stable Alignment 학습 프레임워크(모방, 자기비판, 재정렬) 제안

## Achievement

![Figure 3](figures/fig3.webp)
*다양한 언어모델에서의 정렬 분석: 모델 규모가 반드시 정렬 성능을 크게 향상시키지는 않음*

![Figure 2](figures/fig2.webp)
*Back-Scatter를 통한 상호작용 데이터 생성 및 3가지 정렬 데이터 타입(모방, 자기비판, 재정렬) 구성*

1. **벤치마크 성능 우월성**: 6개의 정렬 벤치마크에서 기존 방법을 능가하며, 적대적 공격(jailbreaking)에 대한 견고성이 현저히 향상됨

2. **확장성 및 효율성 개선**: 추가 보상 모델이 필요 없어 자원 제약 환경에 쉽게 배포 가능하며, 기존 SFT 대비 인간 라벨링 비용 감소

3. **모델 규모의 한계 극복**: 175B GPT-3 모델로의 20배 확대에도 불구하고 정렬 성능 향상이 미미하여, 소규모 모델도 충분한 정렬 성능 달성 가능함을 시사

4. **생성 데이터의 질**: 169k개의 상호작용 데이터에서 수집된 비교 쌍(comparative pairs), 집단 평가(collective ratings), 상세 피드백, 반복 수정 응답을 포함한 고품질 데이터 구성

## How

![Figure 2](figures/fig2.webp)
*SANDBOX의 Back-Scatter 메커니즘: 중앙 에이전트가 초기 응답을 생성한 후, 주변 에이전트들의 평가와 피드백을 받아 반복적으로 개선*

**SANDBOX 시뮬레이션:**
- 100개의 언어모델 기반 사회 에이전트 구성
- 사회적 규범 형성을 위해 논쟁적 주제나 위험 관련 질문에 대한 토론 유도
- 임재(latent rule)를 인센티브로 설정하여 에이전트들의 자체 개선 촉진
- 임베딩 기반 의미 검색을 통해 과거 응답 일관성 유지

**Back-Scatter 메커니즘:**
- 중앙 에이전트: 질문에 대한 초기 응답 생성
- 피드백 수집: 근처 에이전트들이 평가(7점 리커트 척도)와 상세 설명 제공
- 반복적 개선: 중앙 에이전트가 피드백을 반영하여 응답 개선
- 옵저버 에이전트: 메모리 없이 정렬성과 참여도 평가

**Stable Alignment 3단계 학습:**
1. **모방(Imitation) 단계**: 정렬된 응답 데모 학습을 통한 기본 정렬 능력 습득
2. **자기비판(Self-Critic) 단계**: 상세한 피드백 학습을 통해 부정적 응답 판별 능력 개발
3. **재정렬(Realignment) 단계**: 반복 수정된 응답 학습을 통한 최종 개선

**파레토 최적성 기준**: 정렬(alignment)과 참여도(engagement) 평가의 곱이 더 이상 증가하지 않을 때 시뮬레이션 종료

## Originality

- **시뮬레이션 기반 정렬 학습**: 기존의 정적 데이터셋 기반 학습에서 벗어나 동적 시뮬레이션 환경에서 상호작용 데이터를 수집하는 혁신적 접근

- **Back-Scatter 메커니즘**: 인간의 사회적 학습 과정을 모방한 새로운 피드백 수집 방식으로, 단순 스칼라 보상을 넘어 집단적 평가와 상세 설명 결합

- **보상 모델 제거**: RLHF의 보상 해킹 문제를 근본적으로 해결하기 위해 추가 프록시 모델 없이 직접 상호작용 데이터로부터 학습

- **자동화된 감독(Automated Supervision)**: 큰 언어모델의 감독을 통한 작은 모델의 정렬 학습으로, 인간 라벨링 비용의 대폭 절감

- **다각형 평가 체계**: 단일 평가가 아닌 정렬성, 참여도, 피드백 품질을 종합적으로 고려하는 평가 메커니즘

## Limitation & Further Study

- **시뮬레이션-현실 간극(Sim2Real Gap)**: 시뮬레이션된 사회적 상호작용이 실제 인간의 가치 판단을 완전히 대표하지 못할 수 있으며, 문화적 다양성 반영 부족 가능성

- **계산 비용**: 시뮬레이션 실행 단계 자체의 계산 비용이 상세히 분석되지 않았으며, 대규모 배포 시 효율성에 대한 의문 제기

- **정렬 규칙의 명시성 부족**: SANDBOX Rule이 "잠재적 인센티브"로만 언급되어 구체적 규칙 설정이 결과에 미치는 영향에 대한 분석 부재

- **언어 및 문화적 일반화**: 주로 영어 기반 질문으로 구성되어 있으며, 다국어 환경이나 문화적으로 다양한 가치관에 대한 정렬 효과 미검증

- **후속 연구 방향**:
  - 실제 인간 사회와의 상호작용 검증을 통한 시뮬레이션 현실성 강화
  - 다국어 및 문화적으로 다양한 정렬 값 체계 통합
  - 적대적 시나리오 확대 및 더 정교한 jailbreak 기법에 대한 견고성 검증
  - 시뮬레이션 파라미터(에이전트 수, 상호작용 라운드 수)의 최적화 연구


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.2/5

**총평**: 본 논문은 기존의 감독 학습과 보상 모델링의 한계를 극복하기 위해 시뮬레이션된 사회적 상호작용을 활용하는 혁신적이고 실용적인 접근을 제시하며, 벤치마크와 적대적 공격에 대한 견고성에서 우수한 성능을 보여준다. 다만 시뮬레이션-현실 간극, 명시적 규칙 정의, 다문화적 일반화 측면에서 개선의 여지가 있다.

## Related Papers

- 🏛 기반 연구: [[papers/356_From_individual_to_society_A_survey_on_social_simulation_dri/review]] — 대형 언어모델이 주도하는 사회 시뮬레이션 조사는 시뮬레이션된 인간 사회에서의 언어모델 정렬 학습의 이론적 기반을 제공합니다
- 🔄 다른 접근: [[papers/331_Exploring_collaboration_mechanisms_for_llm_agents_A_social_p/review]] — LLM 에이전트의 협업 메커니즘 탐구와 시뮬레이션된 사회적 상호작용은 모두 AI의 사회적 학습을 위한 서로 다른 접근법입니다
- 🧪 응용 사례: [[papers/606_Patientsim_A_persona-driven_simulator_for_realistic_doctor-p/review]] — 의사-환자 시뮬레이션은 사회적으로 정렬된 언어모델 학습이 의료 분야에 적용된 구체적인 사례입니다
- 🧪 응용 사례: [[papers/247_Cultural_evolution_in_populations_of_large_language_models/review]] — 시뮬레이션된 인간 환경에서 사회적으로 정렬된 언어 모델 훈련이 LLM 문화진화의 실제 적용 사례이다.
- 🔗 후속 연구: [[papers/356_From_individual_to_society_A_survey_on_social_simulation_dri/review]] — 시뮬레이션된 인간 환경에서의 언어모델 훈련이 사회 시뮬레이션 체계를 실제 모델 개발로 확장한 사례이다.
- 🔗 후속 연구: [[papers/179_Can_ai_replace_human_subjects_a_large-scale_replication_of_p/review]] — 심리학 실험 재현을 사회적으로 정렬된 언어모델 훈련으로 발전시킨 연구
- 🏛 기반 연구: [[papers/175_Building_machines_that_learn_and_think_with_people/review]] — 사회적으로 정렬된 언어 모델 훈련 방법이 인간과 협력적으로 사고하는 AI 파트너 개발의 핵심 기술적 토대이다.
- 🔗 후속 연구: [[papers/331_Exploring_collaboration_mechanisms_for_llm_agents_A_social_p/review]] — 시뮬레이션된 인간 사회에서 사회적으로 정렬된 언어 모델 훈련은 에이전트 협력 메커니즘을 실제 사회적 맥락으로 확장한다.
- 🏛 기반 연구: [[papers/477_Large_language_models_pass_the_turing_test/review]] — 사회적으로 정렬된 언어 모델 학습이 튜링 테스트 통과의 기반 기술이 됨
- 🏛 기반 연구: [[papers/185_Can_large_language_models_understand_you_better_an_mbti_pers/review]] — 시뮬레이션된 인간 사회에서 사회적으로 정렬된 언어 모델 훈련 연구로 본 논문의 성격 탐지 데이터셋 구축의 이론적 기반을 제공한다.
