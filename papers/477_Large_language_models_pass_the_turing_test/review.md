---
title: "477_Large_language_models_pass_the_turing_test"
authors:
  - "Cameron R. Jones"
  - "Benjamin K. Bergen"
date: "2025"
doi: "N/A"
arxiv: ""
score: 4.5
essence: "본 논문은 현대 대규모 언어모델(LLM)이 튜링 테스트(Turing test)의 세 명 참가자 버전을 최초로 통과했음을 보여주는 실증적 증거를 제시한다. GPT-4.5가 적절한 페르소나(persona) 프롬프트 하에서 73%의 확률로 인간으로 판단되었으며, 이는 실제 인간 참가자보다 유의미하게 높은 비율이다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/Scientific_Language_Models"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Carlson_2025_Large language models pass the turing test.pdf"
---

# Large language models pass the turing test

> **저자**: Cameron R. Jones, Benjamin K. Bergen | **날짜**: 2025 | **DOI**: N/A

---

## Essence

![Figure 2](figures/fig2.webp) *각 AI 증인의 승률(interrogator가 AI 시스템을 인간으로 판단한 비율). 오차막대는 95% 부트스트랩 신뢰구간을 나타냄*

본 논문은 현대 대규모 언어모델(LLM)이 튜링 테스트(Turing test)의 세 명 참가자 버전을 최초로 통과했음을 보여주는 실증적 증거를 제시한다. GPT-4.5가 적절한 페르소나(persona) 프롬프트 하에서 73%의 확률로 인간으로 판단되었으며, 이는 실제 인간 참가자보다 유의미하게 높은 비율이다.

## Motivation

- **Known**: 지난 75년간 튜링 테스트를 통과하는 시스템을 구축하려는 많은 시도가 있었으나 성공하지 못했음. 최근 두 편의 연구는 간소화된 2자 버전의 튜링 테스트에서 LLM을 평가했으며, GPT-4는 인간으로 54% 판정되었음.

- **Gap**: 튜링의 원래 3자 버전 테스트는 더 엄격한 테스트로 간주되는데(직접 비교 가능, 적절한 기저율 보장), 이를 현대 LLM으로 체계적으로 평가한 연구가 부족함.

- **Why**: LLM이 튜링 테스트를 통과할 수 있다면 인간 대체 가능성, 사기·허위정보 확산의 위험성 등 사회·경제적 영향이 즉각적임. 또한 현대 AI 벤치마크는 좁은 범위와 정적 특성으로 인해 진정한 추론 능력이 아닌 암기를 측정할 가능성 있음.

- **Approach**: UCSD 학부생(n=126)과 Prolific 참여자(n=158)를 대상으로 두 개의 독립적이고 사전 등록된 3자 튜링 테스트를 실시. GPT-4.5, LLaMa-3.1-405B, GPT-4o, ELIZA를 평가하고, 페르소나 프롬프트 유무를 비교.

## Achievement

![Figure 1](figures/fig1.webp) *Prolific(a, b & d) 및 학부생(c) 연구의 4가지 게임 예시. 각 패널에서 한 대화는 인간 증인과, 다른 하나는 AI 시스템과 진행됨*

1. **GPT-4.5의 튜링 테스트 통과**: GPT-4.5-PERSONA는 전체 73% 승률(학부생 69%, Prolific 76%)을 기록하여 실제 인간 참가자보다 유의미하게 높은 비율로 인간으로 판정됨 (p = 0.50, 50% 이상이므로 귀무가설 채택 불가).

2. **LLaMa의 경계선 성능**: LLaMa-3.1-405B-PERSONA는 56% 승률(학부생 45%, Prolific 65%)로 인간과 통계적으로 구분되지 않음 (p = 0.08 또는 p = 0.50).

3. **기저 모델의 실패**: GPT-4o-NO-PERSONA(21%)와 ELIZA(23%)는 유의미하게 50% 이하의 승률을 기록하여 조작 점검(manipulation check)으로 기능함.

## How

![Figure 3-5](figures/fig3.webp) *Figure 3: Interrogator 정확도 vs 종료 설문 응답 | Figure 4: Interrogator 전략 분류 | Figure 5: Interrogator 사유 분석*

- **실험 설계**: 각 라운드에서 interrogator는 5분간 인간 증인 1명과 AI 증인 1명과 동시에 메시징으로 대화 후 어느 쪽이 인간인지 판정 및 신뢰도·사유 기술

- **프롬프트 전략**: 
  - NO-PERSONA: 최소한의 지시("튜링 테스트에 참가 중이며 인간으로 확신시켜야 함")
  - PERSONA: 특정 페르소나 채택(내향적 젊은이, 인터넷 문화 지식, 속어 사용)

- **대조군 설정**: ELIZA(규칙 기반 챗봇, 1960년대)를 기저선으로 사용하여 interrogator가 약한 AI를 구분할 수 있는지 확인

- **통계 방법론**: 사전 등록된 귀무가설(win rate ≠ 50%) 검증, 부트스트랩 신뢰구간, z-검정 사용

- **강건성 테스트**: 두 개의 독립적 집단(학부생 vs Prolific)에서 반복 실시하여 결과의 일반화 가능성 확인

## Originality

- **최초의 3자 튜링 테스트 통과**: 기존 연구는 2자 버전 또는 구형 LLM 평가에 국한되었으나, 본 연구는 현대 LLM(GPT-4.5)이 Turing의 원래 3자 버전을 통과함을 최초로 입증

- **사전 등록 및 독립 표본 반복**: 사전 가설 등록 및 두 개의 서로 다른 표본에서의 반복으로 통계적 엄격성과 신뢰성 확보

- **페르소나 프롬프트의 체계적 분석**: 같은 모델도 프롬프트에 따라 21~73%까지 승률이 변하는 점을 정량적으로 시연

- **사회적·경제적 영향 프레이밍**: 튜링 테스트 통과를 단순 지능 측정이 아닌 "대체 가능성(substitutability)" 및 "기만 능력(ability to deceive)" 관점에서 해석

## Limitation & Further Study

- **제한된 대화 시간**: 5분이라는 짧은 시간 제약으로 인해 깊이 있는 논의나 모순 발견이 어려울 수 있음

- **표본의 동질성**: 학부생과 Prolific 참여자 모두 온라인 기반으로 일반인(오프라인, 연령층 다양성)의 성능과는 다를 가능성

- **페르소나 의존성**: 성능이 페르소나 프롬프트에 크게 의존하여 일반화 가능성 제한

- **인과성 미명확**: LLM의 어떤 특성(문법, 시의성, 논리적 일관성 등)이 통과를 가능하게 했는지 상세 분석 부재

- **후속 연구 방향**:
  - 더 길거나 대면 멀티모달 상황에서의 성능 평가
  - 다양한 배경의 표본 확대 (나이, 교육 수준, 문화권)
  - 모델의 구체적인 강점/약점 분석 (어떤 질문 카테고리에서 강한가)
  - 튜링 테스트 통과 능력의 시간적 변화 추적

## Evaluation

- **Novelty**: 5/5 - 현대 LLM이 공식적 3자 튜링 테스트를 통과한 첫 실증 증거로, AI 역사에서 이정표적 기여

- **Technical Soundness**: 4.5/5 - 사전 등록, 통제된 설계, 독립 표본 반복 등 통계 방법론이 우수하나, 샘플 동질성과 인과 메커니즘 분석 부재로 감점

- **Significance**: 5/5 - AI 지능 평가의 패러다임, 사기·허위정보 확산 위험, 일자리 대체 등 이론·실무적 함의가 매우 크며 광범위한 학제적 관심 촉발

- **Clarity**: 4/5 - 실험 설계와 결과 제시가 명확하나, 페르소나 프롬프트의 구체 내용이 부록에만 있고 본문에서 더 상세히 논의되면 좋을 점

- **Overall**: 4.5/5

**총평**: 본 논문은 현대 LLM이 75년간의 도전 과제였던 튜링 테스트를 통과했음을 처음으로 실증적으로 입증한 획기적 연구이며, 엄격한 실험 설계와 통계 방법론을 갖추었으나, 더욱 다양한 표본과 심층적 메커니즘 분석으로 보완될 여지가 있다.

## Related Papers

- 🧪 응용 사례: [[papers/387_Gpt-4_technical_report/review]] — GPT-4 같은 고성능 LLM이 인간과 구별되지 않을 정도로 발전했음을 실증적으로 증명
- 🔗 후속 연구: [[papers/179_Can_ai_replace_human_subjects_a_large-scale_replication_of_p/review]] — LLM이 인간을 대체할 수 있는 가능성을 사회과학 실험 맥락에서 체계적으로 검증
- 🏛 기반 연구: [[papers/838_Training_socially_aligned_language_models_in_simulated_human/review]] — 사회적으로 정렬된 언어 모델 학습이 튜링 테스트 통과의 기반 기술이 됨
- ⚖️ 반론/비판: [[papers/846_TrustLLM_Trustworthiness_in_Large_Language_Models/review]] — LLM의 신뢰성 문제를 지적하며 튜링 테스트 통과만으로는 진정한 지능을 증명할 수 없음을 논의
- 🧪 응용 사례: [[papers/387_Gpt-4_technical_report/review]] — GPT-4의 발전된 언어 능력이 튜링 테스트 통과라는 구체적 성과로 입증됨
