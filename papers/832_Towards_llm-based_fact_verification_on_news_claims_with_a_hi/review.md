---
title: "832_Towards_llm-based_fact_verification_on_news_claims_with_a_hi"
authors:
  - "Xuan Zhang"
  - "Wei Gao"
date: "2023"
doi: "N/A"
arxiv: ""
score: 4.25
essence: "대규모 언어모델(LLM)의 인컨텍스트 학습(ICL) 능력을 뉴스 클레임 검증에 활용하되, 계층적 단계별 프롬프팅(HiSS) 방법을 통해 클레임을 세부 클레임으로 분해하고 검색 엔진 기반의 증거 수집을 통해 사실 확인의 정확도와 설명 가능성을 높인 연구이다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Fact_Verification_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Singhal et al._2023_Towards llm-based fact verification on news claims with a hierarchical step-by-step prompting method.pdf"
---

# Towards LLM-based Fact Verification on News Claims with a Hierarchical Step-by-Step Prompting Method

> **저자**: Xuan Zhang, Wei Gao | **날짜**: 2023 | **DOI**: N/A

---

## Essence

대규모 언어모델(LLM)의 인컨텍스트 학습(ICL) 능력을 뉴스 클레임 검증에 활용하되, 계층적 단계별 프롬프팅(HiSS) 방법을 통해 클레임을 세부 클레임으로 분해하고 검색 엔진 기반의 증거 수집을 통해 사실 확인의 정확도와 설명 가능성을 높인 연구이다.

## Motivation

- **Known**: BERT와 같은 사전학습 언어모델(PLM)은 가짜뉴스 탐지에서 우수한 성능을 보였으며, GPT-3.5 같은 대규모 언어모델(LLM)은 다양한 다운스트림 태스크에서 인상적인 성능을 달성했다. Chain-of-Thought(CoT) 프롬프팅은 산술, 상식, 기호 추론에서 성능을 향상시켰다.

- **Gap**: LLM의 추론 능력을 가짜뉴스 관련 태스크에 활용한 연구는 매우 제한적이며, 뉴스 클레임 검증에서 vanilla CoT가 표준 프롬프팅보다 오히려 성능이 낮다는 역직관적 현상이 존재한다.

- **Why**: 그림 1에서 보듯이 vanilla CoT는 두 가지 문제점을 드러낸다: (1) 필수 사고의 누락 - 클레임의 주목할 만한 부분을 무시하여 부정확한 판단 야기, (2) 사실 환각(fact hallucination) - 필요한 정보가 없을 때 신뢰할 수 없는 "사실"을 생성하여 최종 예측을 오도한다.

- **Approach**: 복잡한 클레임을 더 작은 세부 클레임으로 분해하도록 LLM에 지시하고, 검색 엔진을 통해 외부 지식을 제공하여 사실 환각을 완화하는 HiSS 프롬프팅 방법을 제안한다.

## Achievement

![Figure 1](figures/fig1.webp)
*그림 1: Vanilla CoT 프롬프팅 기반 클레임 검증의 예시. 생성된 CoT가 "nukes"에 관한 필수 사고 누락과 증거 없는 사실 환각으로 인해 잘못된 판단에 도달한다.*

1. **LLM의 인컨텍스트 학습 능력 입증**: 단 4-shot 시연 예제만으로도 LLM이 대부분의 지도학습 방법을 능가할 수 있음을 확인하였으며, 이는 LLM이 허위정보 대응의 유망한 도구임을 시사한다.

2. **최첨단 성능 달성**: RAWFC와 LIAR 두 가지 공개 미정보 데이터셋에서 HiSS 프롬프팅이 기존의 완전 지도학습 방식을 능가하며, 매크로 평균 F1에서 평균 4.95% 향상을 달성하고 소수-샷 뉴스 클레임 검증에서 새로운 최첨단 성과를 수립했다.

3. **향상된 설명 가능성**: 기존 방법 대비 더 세분화되고 따라가기 쉬운 설명을 자동 평가와 인간 평가를 통해 입증했다.

## How

![Figure 2](figures/fig2.webp)
*그림 2: 제안된 HiSS 모델의 개요. 원본 인간 입력은 빨간색 배경으로 표시된다.*

### Hierarchical Step-by-Step (HiSS) 프롬프팅의 두 가지 주요 프로세스:

1. **클레임 분해(Claim Decomposition)**
   - LLM에 복잡한 클레임을 검증하기 더 쉬운 세부 클레임들로 분할하도록 지시
   - 명시적 및 암시적 검증 대상점(check-worthy points)을 철저히 생성하도록 유도
   - 예: "Donald Trump has said he loves war, 'including with nukes'"를 2개의 세부 클레임으로 분해

2. **세부 클레임 검증(Subclaim Verification)**
   - 각 세부 클레임에 대해 LLM이 단계적으로 일련의 질문을 생성하고 답변
   - 각 질문마다 외부 지식(검색 엔진)의 필요성을 명시적으로 판단하도록 지시
   - 신뢰도 평가 메커니즘을 통해 답변의 신뢰성 검증
   - 최종적으로 각 세부 클레임의 사실성을 판단하고 전체 클레임의 최종 라벨 결정

### 핵심 설계 원칙:

- **명시적 신뢰도 표현**: "yes" 또는 "no"로 답변에 대한 신뢰도를 명시하도록 요청
- **외부 지식의 적시 활용**: 필요할 때만 검색 엔진을 활용하여 환각 완화
- **세분화된 추론**: 전체 클레임의 복잡성을 여러 단계의 질문-답변으로 분해
- **K-shot 시연**: 구조화된 시연 예제를 통한 in-context learning 활용

## Originality

- **새로운 문제 식별**: 뉴스 클레임 검증에서 vanilla CoT가 표준 프롬프팅보다 성능이 낮다는 역직관적 현상을 체계적으로 분석하고 두 가지 구체적 문제점(필수 사고 누락, 사실 환각)을 규명했다.

- **계층적 분해 전략**: 복잡한 클레임을 세부 클레임으로 계층적으로 분해하는 접근은 기존 CoT의 일반적 추론 추적과 차별화된 세분화된 검증 방식을 제공한다.

- **검색 기반 증거 통합**: 단순 검색 활용이 아닌, 각 질문 단계에서 외부 지식의 필요성을 명시적으로 판단하고 활용하는 메커니즘은 LLM 환각 완화의 새로운 접근이다.

- **미정보 도메인 특화**: 기존 CoT 연구가 QA(HotpotQA), 증거 기반 사실 검증(FEVER) 등에서 활용된 반면, 본 연구는 실시간 동적 뉴스 클레임이라는 고유한 도메인 특성에 맞춘 맞춤형 프롬프팅을 설계했다.

## Limitation & Further Study

- **검색 의존성**: 외부 지식 제공을 위해 검색 엔진에 의존하므로, 검색 결과의 품질과 최신성이 최종 성능을 직접 제약할 수 있다. 특히 모호하거나 검증 어려운 클레임의 경우 관련 증거를 찾기 어려울 수 있다.

- **비용 및 지연**: 계층적 분해와 다단계 질문-답변 프로세스는 단일 프롬프팅 대비 추론 비용 증가와 처리 시간 증가를 초래한다.

- **다언어 및 도메인 확장성**: 현재 영어 뉴스 클레임 데이터셋(RAWFC, LIAR)에서만 평가되었으므로, 다른 언어와 도메인(과학 클레임, 소셜 미디어 클레임 등)으로의 일반화 가능성은 미지수이다.

- **후속 연구 방향**:
  - 더 효율적인 클레임 분해 전략 개발
  - LLM 기반 시스템의 신뢰성과 일관성 평가
  - 다양한 LLM 모델(GPT-4, Claude 등)에 대한 비교 분석
  - 사용자 피드백을 반영한 점진적 학습 메커니즘 구축

## Evaluation

- **Novelty**: 4.5/5
  - 뉴스 클레임 검증에서 LLM의 문제점을 명확히 규명하고 계층적 분해라는 창의적 해결책을 제시했으나, 기본적 개념(분해, CoT)은 선행 연구에서 보았다.

- **Technical Soundness**: 4/5
  - 방법론의 설계가 논리적이고 두 가지 문제점에 대한 해결책이 일관성 있으나, 검색 기반 증거 획득의 성공률이나 검색 쿼리 생성 방식에 대한 기술적 상세 기술이 부족하다.

- **Significance**: 4.5/5
  - 실제 가짜뉴스 대응이라는 중요한 응용 분야에서 LLM의 활용 가능성을 입증했고, 소수 샷 학습으로 지도학습 기반 방법을 능가한 결과는 실무적 가치가 높다.

- **Clarity**: 4/5
  - 논문 구조와 핵심 아이디어가 명확하게 설명되었으나, 실제 프롬프팅 템플릿의 전체 형태와 검색 엔진 호출 메커니즘에 대한 상세 설명이 부족하다.

- **Overall**: 4.25/5
  - 뉴스 클레임 검증이라는 실제 중요 문제에 LLM의 특성을 고려한 창의적 해결책을 제시하고, 표준 벤치마크에서 최첨단 성과를 달성했다. 다만 기술적 독창성과 일반화 가능성 측면에서 약간의 제약이 있다.

**총평**: 본 논문은 LLM 기반의 뉴스 클레임 검증에서 실무 지향적 성과를 보였으며, 계층적 분해와 검색 기반 증거 통합을 통해 LLM의 추론 능력을 실효적으로 향상시킨 의의 있는 연구이다. 다만 다양한 도메인과 언어로의 확장성 검증과 비용 효율성 개선이 향후 과제로 남아있다.

## Related Papers

- 🔄 다른 접근: [[papers/859_Unsupervised_pretraining_for_fact_verification_by_language_m/review]] — HiSS가 계층적 단계별 프롬프팅을 통해 뉴스 클레임을 세분화하는 반면, SFAVEL은 언어모델 증류를 통한 무감독 학습으로 서로 다른 팩트 검증 접근법을 제시함
- 🔗 후속 연구: [[papers/332_Fact-checking_complex_claims_with_program-guided_reasoning/review]] — 프로그램 가이드 추론을 통한 복잡한 클레임 팩트 체킹이 HiSS의 계층적 분해 방법을 더 정교한 논리적 추론 체계로 발전시킨 연구임
- 🧪 응용 사례: [[papers/827_Towards_effective_extraction_and_evaluation_of_factual_claim/review]] — 효과적인 사실 클레임 추출과 평가 방법론이 HiSS의 계층적 클레임 분해와 증거 수집 과정을 실제 뉴스 검증 시스템에 적용할 수 있는 구체적 기술을 제공함
- 🏛 기반 연구: [[papers/541_Missing_counter-evidence_renders_nlp_fact-checking_unrealist/review]] — 기존 팩트체킹의 한계를 지적한 연구가 계층적 증거 기반 뉴스 클레임 검증 시스템 개발의 동기를 제공합니다.
- 🔄 다른 접근: [[papers/267_Defame_Dynamic_evidencebased_fact-checking_with_multimodal_e/review]] — 동적 증거 수집 기반 접근법과 계층적 증거 구조화 접근법이라는 서로 다른 팩트체킹 시스템 설계 철학을 제시합니다.
- 🔄 다른 접근: [[papers/859_Unsupervised_pretraining_for_fact_verification_by_language_m/review]] — SFAVEL은 언어모델 증류를 통한 무감독 접근을, HiSS는 계층적 단계별 프롬프팅을 사용하여 서로 다른 방식으로 팩트 검증 문제를 해결함
