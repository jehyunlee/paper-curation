---
title: "609_Peerarg_Argumentative_peer_review_with_llms"
authors:
  - "Purin Sukpanichnant"
  - "Anna Rapberger"
  - "Francesca Toni"
date: "2024"
doi: "10.48550/arXiv.2409.16813"
arxiv: ""
score: 3.5
essence: "본 논문은 대규모 언어 모델(LLM)과 계산 논증(computational argumentation) 방법을 결합하여 피어 리뷰 과정을 투명하고 해석 가능하게 만드는 PeerArg 시스템을 제안한다. 양극 논증 틀(Bipolar Argumentation Framework, BAF)을 활용하여 여러 리뷰의 의견을 구조화되고 논리적으로 통합함으로써 논문 채택 여부를 예측한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/LLM_Review_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Sukpanichnant et al._2024_Peerarg Argumentative peer review with llms.pdf"
---

# Peerarg: Argumentative peer review with llms

> **저자**: Purin Sukpanichnant, Anna Rapberger, Francesca Toni | **날짜**: 2024 | **DOI**: [10.48550/arXiv.2409.16813](https://doi.org/10.48550/arXiv.2409.16813)

---

## Essence

![Figure 1](figures/fig1.webp)
*PeerArg 파이프라인 개요: 각 리뷰에서 양극 논증 틀(BAF)을 추출한 후 통합하여 최종 논문 채택 여부를 결정*

본 논문은 대규모 언어 모델(LLM)과 계산 논증(computational argumentation) 방법을 결합하여 피어 리뷰 과정을 투명하고 해석 가능하게 만드는 PeerArg 시스템을 제안한다. 양극 논증 틀(Bipolar Argumentation Framework, BAF)을 활용하여 여러 리뷰의 의견을 구조화되고 논리적으로 통합함으로써 논문 채택 여부를 예측한다.

## Motivation

- **Known**: 피어 리뷰는 학술 출판의 핵심 프로세스이지만 주관성과 확증편향(confirmation bias), 첫인상 편향(first-impression bias) 등 여러 편견에 취약하다. 최근 NLP 기술을 적용한 리뷰 이해 및 생성 연구들(메타 리뷰 생성, 찬반 요약 등)이 증가하고 있다.

- **Gap**: 기존 딥러닝 기반 접근법들은 뛰어난 성능을 보이지만 블랙박스 특성으로 인해 결정 과정의 근거를 이해하고 신뢰하기 어렵다. 또한 기존 논증 연구들은 논문의 구조 분석에만 집중하고 논증 간 관계(support/attack)를 모델링하지 않는다.

- **Why**: 투명성과 해석 가능성(interpretability)을 갖춘 리뷰 집계 시스템이 필요하다. 논증 관계를 명시적으로 모델링하면 리뷰어의 의견 충돌과 지지를 구조화할 수 있다.

- **Approach**: 양극 논증 틀(BAF)을 사용하여 각 리뷰를 논증 구조로 변환하고, 여러 리뷰의 구조들을 통합한 후 정량적 논증 의미론(DF-QuAD, MLP-기반 의미론)을 적용하여 논문 채택 여부를 결정한다. 비교 기준으로 LLM의 few-shot 학습 기반 엔드투엔드 모델도 제안한다.

## Achievement

![Figure 2](figures/fig2.webp)
*엔드투엔드 LLM 입력 템플릿: 프라이머(primer)의 4개 예제와 프롬프트(prompt)의 대상 리뷰들로 구성*

1. **해석 가능한 리뷰 집계 프레임워크**: PeerArg는 리뷰들의 의견을 명시적인 논증 구조로 표현하여 각 논증의 강도와 상호 관계를 정량적으로 평가할 수 있다. 이는 메타 리뷰어나 컨퍼런스 의장이 채택 결정의 근거를 명확히 이해하도록 돕는다.

2. **우수한 예측 성능**: 세 개의 리뷰 데이터셋(두 개의 컨퍼런스 리뷰 데이터셋과 한 개의 저널 리뷰 데이터셋)에서 PeerArg의 특정 하이퍼파라미터 조합이 few-shot LLM을 능가하는 성능을 달성했다.

3. **LLM과 기호적 AI의 시너지**: LLM을 사용하여 자동으로 리뷰에서 논증과 관계를 추출한 후 계산 논증 방법으로 집계함으로써 두 접근 방식의 장점을 결합한다.

## How

![Figure 3 & 4](figures/fig3.webp)
*리뷰 QBAF 추출 과정: LLM이 리뷰 텍스트에서 주요 주장을 추출하고 이들 간의 support/attack 관계를 식별하여 양극 논증 틀을 구성*

### PeerArg 파이프라인의 주요 단계:

- **리뷰 → QBAF 변환**: 각 리뷰에 대해 LLM 프롬프트를 사용하여 주요 논증(arguments)과 그 관계(support/attack edges)를 추출한다. 각 논증에는 신뢰도 기반의 기초 점수(base score β)를 할당한다.

- **QBAF 통합**: 여러 리뷰의 QBAF들을 하나의 통합된 QBAF로 병합한다. 동일한 내용의 논증은 병합되고 상충하는 주장은 공격 관계(attack)로 모델링된다.

- **의미론 적용**: DF-QuAD 의미론 또는 MLP-기반 의미론을 적용하여 각 논증의 최종 강도를 계산한다. 이는 공격자와 지지자의 강도를 합산하여 기초 점수에 영향을 미친다.

- **채택 결정**: 통합 QBAF에서 "채택(accept)"과 관련된 주요 논증들의 최종 강도를 기준으로 임계값(threshold)을 사용하여 채택 여부를 결정한다.

### 엔드투엔드 LLM:

- **Few-shot 프롬프팅**: Mistral-7B 모델에 4개의 예제(2개 채택, 2개 거절)로 구성된 프라이머와 대상 리뷰들을 입력으로 제공한다.

- **직접 예측**: 구조적 분석 없이 리뷰 텍스트에서 바로 채택/거절을 예측한다.

## Originality

- **양극 논증 틀의 적용**: 기존 피어 리뷰 논증 연구와 달리 support/attack 관계를 명시적으로 모델링하여 리뷰 의견의 상호작용을 구조화하는 것이 새로운 접근이다.

- **LLM 기반 자동 추출과 기호적 AI의 결합**: 신경망 기반 LLM으로 논증 요소를 추출하고 이를 고전적 논증 프레임워크에 통합하는 하이브리드 접근법이 독창적이다.

- **정량적 의미론의 적용**: 피어 리뷰 도메인에서 DF-QuAD와 MLP-기반 의미론을 사용하여 리뷰 의견을 정량적으로 집계하는 것은 처음이다.

- **투명성 중심**: 블랙박스 모델 대신 명시적인 논증 구조를 통해 의사결정 과정을 추적할 수 있는 점이 기존 NLP 접근법과 구별된다.

## Limitation & Further Study

- **논증 추출의 정확성 의존**: 전체 시스템의 성능이 LLM의 논증 추출 품질에 크게 의존하기 때문에 추출 오류가 누적될 수 있다. 각 단계별 오류 분석과 개선이 필요하다.

- **QBAF 통합의 휴리스틱**: 서로 다른 리뷰의 논증들을 "동일하다"고 판단하는 기준이 정확하지 않을 수 있으며, 이로 인한 영향을 분석해야 한다.

- **하이퍼파라미터의 데이터셋 의존성**: 최적의 하이퍼파라미터 조합이 데이터셋별로 다르게 나타나므로 일반화 가능성과 실제 적용 방안을 명확히 해야 한다.

- **평가 지표의 제한**: 예측 정확도만 평가하고 해석 가능성 개선이나 리뷰어의 신뢰도 향상에 대한 정성적 평가가 부족하다.

- **후속 연구 방향**:
  - 논증 추출 단계의 정확도 향상 (수동 검증, 미세 조정된 모델 사용)
  - 의미론 선택 기준 및 적응형 선택 메커니즘 개발
  - 메타 리뷰 생성으로의 확장
  - 피어 리뷰어들의 실제 선호도 조사를 통한 평가

## Evaluation

- **Novelty**: 4/5
  - 양극 논증 틀을 피어 리뷰에 적용하고 LLM과 결합하는 아이디어는 신선하고 도메인에 적합하다. 다만, 개별 기술 요소들은 기존 연구를 기반으로 한다.

- **Technical Soundness**: 3.5/5
  - 논증 추출 및 QBAF 통합 과정의 기술적 엄밀성이 부분적이다. 특히 리뷰 간 논증 통합 기준과 중복 제거 메커니즘의 상세 설명이 부족하다. 정량적 의미론의 적용은 수학적으로 확실하다.

- **Significance**: 3.5/5
  - 투명성 있는 리뷰 집계라는 중요한 문제를 다루지만, 제시된 데이터셋이 제한적이고 실제 컨퍼런스 적용 가능성에 대한 논의가 부족하다. 해석 가능성 개선의 실제 효과를 정성적으로 입증할 필요가 있다.

- **Clarity**: 3.5/5
  - 논문 구조는 논리적이고 수학적 정의가 명확하지만, QBAF 추출 및 통합 프로세스의 세부 사항(특히 LLM 프롬프트 설계)이 충분히 설명되지 않아 재현 가능성이 낮다. 몇몇 개념(특히 불완전한 QBAF → 완전한 QBAF 변환)의 설명이 부족하다.

- **Overall**: 3.5/5

**총평**: 본 논문은 피어 리뷰의 투명성과 해석 가능성 문제에 대한 혁신적인 접근을 제시하며 양극 논증 틀의 새로운 응용을 보여준다. 다만 논증 추출 과정의 신뢰성, QBAF 통합의 엄밀성, 실제 적용 가능성에 대한 더 깊은 분석과 검증이 필요하며, 특히 해석 가능성 개선의 실질적 이점을 정성적으로 입증해야 한다.

## Related Papers

- 🔄 다른 접근: [[papers/080_AI_is_transforming_peer_review__and_many_scientists_are_worr/review]] — AI 동료평가에 대한 우려를 논증 틀을 통해 투명하고 해석가능하게 해결한다
- 🔗 후속 연구: [[papers/776_Streamlining_the_review_process_Ai-generated_annotations_in/review]] — AI 주석 달기를 포함한 더 체계적이고 논리적인 동료평가 시스템으로 확장한다
- 🏛 기반 연구: [[papers/1087_Gpt4_is_slightly_helpful_for_peer-review_assistance_A_pilot/review]] — GPT-4의 동료평가 보조 능력을 바탕으로 더 구조화된 논증 기반 접근법을 제시한다
