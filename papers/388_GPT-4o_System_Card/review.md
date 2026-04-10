---
title: "388_GPT-4o_System_Card"
authors:
  - "OpenAI Aaron Hurst"
  - "Adam Lerer"
  - "Adam P. Goucher"
  - "Adam Perelman"
  - "Aditya Ramesh"
date: "2024"
doi: "해당"
arxiv: ""
score: 4.0
essence: "GPT-4o는 텍스트, 오디오, 이미지, 비디오를 입력으로 받아 텍스트, 오디오, 이미지를 출력할 수 있는 엔드-투-엔드 멀티모달 모델이며, 특히 음성-음성(speech-to-speech) 대화 능력에서 인간 수준의 응답 속도(232-320ms)를 달성했다. 본 System Card는 GPT-4o의 안전성 평가, 위험 식별, 완화 조치를 종합적으로 문서화한 투명성 보고서이다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/Cognitive_LLM_Evaluation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Hurst et al._2024_GPT-4o System Card.pdf"
---

# GPT-4o System Card

> **저자**: OpenAI Aaron Hurst, Adam Lerer, Adam P. Goucher, Adam Perelman, Aditya Ramesh | **날짜**: 2024 | **DOI**: [해당 없음]

---

## Essence

GPT-4o는 텍스트, 오디오, 이미지, 비디오를 입력으로 받아 텍스트, 오디오, 이미지를 출력할 수 있는 엔드-투-엔드 멀티모달 모델이며, 특히 음성-음성(speech-to-speech) 대화 능력에서 인간 수준의 응답 속도(232-320ms)를 달성했다. 본 System Card는 GPT-4o의 안전성 평가, 위험 식별, 완화 조치를 종합적으로 문서화한 투명성 보고서이다.

## Motivation

- **Known**: 대규모 언어모델의 텍스트 기반 안전성 평가 방법론과 GPT-4, GPT-4V의 System Card 경험
- **Gap**: 음성 입출력 능력을 갖춘 멀티모달 모델의 고유한 위험 요소(음성 복제, 화자 식별, 음성 생성 오용 등)에 대한 체계적인 평가 부재
- **Why**: 오디오 모달리티는 사기(impersonation), 허위정보 확산, 개인정보 유출, 감정 조작 등 새로운 형태의 해악을 가능하게 할 수 있음
- **Approach**: (1) 45개 언어, 29개 국가의 100명 이상 외부 적색팀(red teamer)을 활용한 4단계 탐색적 평가, (2) 기존 텍스트 기반 평가를 TTS(Text-to-Speech)를 통해 음성 기반 평가로 변환, (3) 식별된 위험별 구체적 완화 조치 구현 및 검증

## Achievement

![Figure 1: Quantum physics experiment red teamer example](figures/fig1.webp)
*양자물리학 실험 관련 적색팀 테스트 사례*

![Figure 2: Multi-panel figure interpretation red teamer example](figures/fig2.webp)
*다중 패널 이미지 해석 적색팀 테스트 사례*

1. **포괄적 외부 적색팀 운영**: 4단계(3월~6월)에 걸쳐 초기 개발 단계부터 최종 iOS 앱 실제 사용 환경까지 100명 이상의 다국어 전문가(인지과학, 사이버보안, 편향성, 아동안전, 법률 등 28개 도메인)와 협력하여 2,600+ 위험 카테고리 식별

2. **음성 모달리티 특화 위험 식별 및 완화**: (1) 무단 음성 생성 - 사전 선택된 음성만 사용 + 출력 분류기, (2) 화자 식별 - 거부 교육, (3) 저작권 콘텐츠 - 음성 특화 필터, (4) 근거 없는 추론 - 민감한 특성 속성 시 완화된 응답 제공

3. **평가 방법론 혁신**: 기존 텍스트 기반 평가 데이터셋을 Voice Engine을 통해 오디오로 변환하여 재사용, 지역 방언에 따른 견고성 평가 포함

4. **안전 완화의 다층 방어**: 학습 데이터 필터링(CSAM, 혐오 콘텐츠, CBRN 제거), 후학습 정렬(post-training alignment), 출력 분류기, 정책 수준 감시(monitoring) 및 집행을 통한 포괄적 접근

## How

- **데이터 구성**: (1) 공개 웹 데이터, (2) 코드/수학 데이터(논리적 추론 능력), (3) 멀티모달 데이터(이미지, 오디오, 비디오의 해석 및 생성), (4) Shutterstock 등 파트너십을 통한 전유 데이터

- **위험 완화 전략**:
  - **사전학습 단계**: Moderation API, 안전 분류기를 통한 데이터 필터링(CSAM, 혐오, 폭력, CBRN)
  - **후학습 단계**: 인간 선호도에 따른 정렬, 적색팀 테스트, 행동 감독
  - **배포 단계**: 출력 분류기, 정책 수준 감시, 사용자 향 중재 도구

- **평가 방법론**: 
  - TTS를 통해 텍스트 입력을 오디오로 변환 → GPT-4o 입력 → 텍스트 출력 점수화
  - 음성 복제 평가 등 필요시 오디오 직접 평가
  - 자동 채점(autograders) 및/또는 정책 위반 여부 등을 기준으로 수동 라벨링

- **적색팀 구성 및 활동**:
  - Phase 1: 10명, 초기 모델(텍스트/오디오 입출력), 단일턴
  - Phase 2: 30명, 초기 안전 완화 포함(텍스트/오디오/이미지 입력), 다중턴
  - Phase 3: 65명, 최종 후보 모델(완전 멀티모달), 개선된 안전 완화 테스트
  - Phase 4: 65명, iOS 앱 실제 경험(오디오/비디오 입력, 오디오 생성), 실시간 다중턴

## Originality

- **멀티모달 음성 모델의 체계적 안전성 평가 체계화**: 기존 텍스트/이미지 중심의 평가를 음성 생성 모델의 고유 위험(impersonation, 화자 식별, 감정 조작 등)을 포함하도록 확장

- **TTS 기반 평가 방법론의 실용화**: 기존 평가 데이터셋을 음성으로 변환하여 대규모 재사용 가능하게 만들어 평가 효율성 증대

- **광범위한 국제적 다학제 적색팀 운영**: 45개 언어, 29개 국가, 28개 전문 도메인을 아우르는 포괄적 외부 협력 모델로 문화·언어·지역 특수 위험 발굴

- **위험별 맞춤형 완화 조치의 구체화**: 각 위험(무단 음성 생성, 화자 식별, 저작권 침해, 근거 없는 추론)에 대해 학습 단계별 구체적 기술적 조치를 투명하게 문서화

## Limitation & Further Study

- **평가 방법론의 한계**: 
  - TTS 기반 평가는 음성의 운율(intonation), 감정 톤(valence), 배경 잡음, 교차 음성(cross-talk) 등 실제 사용자 입력의 다양성을 완전히 포착하지 못함
  - 수학 방정식, 코드 등 특정 텍스트는 오디오 변환에 부적합
  - 생성된 오디오의 아티팩트(배경음, 음성 외 음향 효과)는 텍스트 기반 채점으로는 감지 불가능

- **평가 범위의 제약**:
  - 대부분의 Preparedness 평가, 적색팀 평가, 사회적 영향 평가가 텍스트/이미지 능력에 집중(음성은 부분적)
  - API 수준의 외부 적색팀 진행 중 → 완전한 결과 미제공

- **후속 연구 필요 영역**:
  - 실제 사용 환경에서의 음성 입력 다양성(방언, 톤, 환경 잡음)에 대한 견고성 추적 모니터링
  - 음성 생성 모델의 감정 조작 위험에 대한 더 정교한 평가 메트릭 개발
  - 장시간 대화에서의 음성 특성 유지(voice consistency) 및 오용 가능성 연구
  - 비영어권 언어의 음성 이해/생성 위험 심화 평가


## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 5/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 System Card는 멀티모달 음성 생성 모델의 고유한 위험을 체계적으로 식별하고 다층 방어 전략으로 완화하는 실질적 사례를 제시함으로써, 거대언어모델의 투명성과 책임성 보고 기준을 정립하는 데 중요한 기여를 했다. 다만 TTS 기반 평가의 방법론적 한계와 실제 사용 환경의 음성 다양성 사이의 간극 해결이 향후 과제로 남아있다.

## Related Papers

- 🔄 다른 접근: [[papers/736_SciTrust_Evaluating_the_Trustworthiness_of_Large_Language_Mo/review]] — GPT-4o의 안전성 평가와 SciTrust의 과학 분야 LLM 신뢰성 평가가 동일한 평가 목표를 가지지만 다른 도메인과 방법론을 사용한다.
- 🏛 기반 연구: [[papers/846_TrustLLM_Trustworthiness_in_Large_Language_Models/review]] — 대규모 언어모델의 전반적인 신뢰성 평가 체계가 GPT-4o의 멀티모달 안전성 평가의 이론적 기반을 제공한다.
- 🔗 후속 연구: [[papers/727_Scimage_How_good_are_multimodal_large_language_models_at_sci/review]] — 멀티모달 과학 이미지 생성 능력 평가가 GPT-4o의 멀티모달 기능에 대한 구체적인 확장 평가이다.
- 🏛 기반 연구: [[papers/727_Scimage_How_good_are_multimodal_large_language_models_at_sci/review]] — GPT-4o의 멀티모달 기능이 과학적 이미지 생성 능력 평가의 기술적 토대를 제공한다.
- 🔄 다른 접근: [[papers/736_SciTrust_Evaluating_the_Trustworthiness_of_Large_Language_Mo/review]] — 과학 분야 LLM 신뢰성 평가와 GPT-4o 안전성 평가가 동일한 신뢰성 목표를 가지지만 평가 도메인과 방법이 다르다.
- 🏛 기반 연구: [[papers/181_Can_gpt-4v_ision_serve_medical_applications_case_studies_on/review]] — GPT-4o 시스템 카드가 GPT-4V 의료 응용의 기술적 기반 제공
- 🏛 기반 연구: [[papers/585_Openai_o1_system_card/review]] — GPT-4o 시스템 카드는 OpenAI o1의 강화학습 기반 chain-of-thought 추론 개발에 이르는 기술적 진화의 배경을 제공한다.
- ⚖️ 반론/비판: [[papers/760_Small_Language_Models_are_the_Future_of_Agentic_AI/review]] — GPT-4o의 대규모 모델 능력과 달리 소규모 언어모델이 에이전트 AI의 미래라는 관점은 모델 크기에 대한 상반된 시각을 제시한다.
