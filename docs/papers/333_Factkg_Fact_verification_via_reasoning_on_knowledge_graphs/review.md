---
title: "333_Factkg_Fact_verification_via_reasoning_on_knowledge_graphs"
authors:
  - "Jiho Kim"
  - "Sungjin Park"
  - "Yeonsu Kwon"
  - "Yohan Jo"
  - "James H. Thorne"
date: "2023"
doi: "arXiv:2305.06590"
arxiv: ""
score: 4.3
essence: "본 논문은 지식 그래프(Knowledge Graph, KG)를 기반으로 사실 검증(fact verification)을 수행하기 위한 첫 번째 대규모 데이터셋 FACTKG를 제시한다. 이 데이터셋은 5가지 추론 유형(One-hop, Conjunction, Existence, Multi-hop, Negation)을 포함하는 108k개의 자연언어 주장으로 구성되어 있다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Fact_Verification_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Kim et al._2023_Factkg Fact verification via reasoning on knowledge graphs.pdf"
---

# Factkg: Fact verification via reasoning on knowledge graphs

> **저자**: Jiho Kim, Sungjin Park, Yeonsu Kwon, Yohan Jo, James H. Thorne, Edward Choi | **날짜**: 2023 | **DOI**: [arXiv:2305.06590](https://arxiv.org/abs/2305.06590)

---

## Essence

![Figure 1](figures/fig1.webp)
*Figure 1: FACTKG의 예제 데이터. 주장을 SUPPORTED 또는 REFUTED로 검증하기 위해 DBpedia에서 추출한 트리플(triple)을 증거로 사용*

본 논문은 지식 그래프(Knowledge Graph, KG)를 기반으로 사실 검증(fact verification)을 수행하기 위한 첫 번째 대규모 데이터셋 FACTKG를 제시한다. 이 데이터셋은 5가지 추론 유형(One-hop, Conjunction, Existence, Multi-hop, Negation)을 포함하는 108k개의 자연언어 주장으로 구성되어 있다.

## Motivation

- **Known**: 사실 검증 연구는 주로 텍스트(FEVER) 및 테이블(TabFact) 기반 증거를 활용해왔다. 기존의 KG 기반 작업(FB15K, WN18)은 단일 트리플만 다루어 복잡한 추론을 요구하지 않는다.

- **Gap**: 지식 그래프는 높은 신뢰성과 명확한 논리 구조를 제공함에도 불구하고, 사실 검증 태스크에서 충분히 활용되지 못했다. 또한 자연언어 주장과 KG를 매핑하는 방법에 대한 이해가 부족하다.

- **Why**: (1) KG는 노드-엣지 구조를 통해 개념 간 연결을 명확하게 표현하여 더 신뢰성 높은 추론을 가능하게 한다. (2) Alexa, Google Assistant 같은 대화 시스템이 내부 KG를 유지하므로, KG 기반 사실 검증의 실용적 가치가 높다.

- **Approach**: WebNLG 데이터셋의 텍스트-그래프 쌍을 기반으로 5가지 추론 유형에 따라 주장을 생성하고, Entity/Relation 치환, NLI 검증 등의 방법으로 다양한 스타일의 주장을 구성한다.

## Achievement

![Figure 2](figures/fig2.webp)
*Figure 2: FACTKG에서 사용된 두 가지 치환 방법. Entity 치환에서는 원래 주장의 모든 엔터티로부터 4-hop 외부에 위치한 새 엔터티를 선택하며, 양방향 NLI 결과가 모두 contradiction이면 완료한다. Relation 치환에서는 원래 relation과 동일한 엔터티 타입을 갖는 relation을 무작위로 추출하여 치환한다.*

1. **데이터셋 구성**: 5가지 추론 유형(One-hop, Conjunction, Existence, Multi-hop, Negation)을 체계적으로 분류한 108k개 주장 생성. DBpedia 전체(0.1B 트리플)를 증거로 사용하여 기존 KG 데이터셋(FB15K: 592K)보다 훨씬 대규모이다.

2. **다양한 언어 스타일**: Colloquial(구어) 및 Written(문어) 스타일을 모두 포함하여 대화 시스템 등 실제 응용에 더 적합하게 구성.

3. **기준 모델 성능**: 그래프 증거를 활용한 모델이 텍스트만 사용하는 기준 모델보다 우수한 성능을 달성함을 실증적으로 입증.

## How

![Figure 3](figures/fig3.webp)
*Figure 3: Conjunction과 Multi-hop 주장에서 사용되는 그래프 패턴*

- **One-hop 생성**: WebNLG의 단일 트리플 문장을 SUPPORTED 주장으로 사용. REFUTED는 Entity 치환(4-hop 이상 떨어진 동일 타입 엔터티) 또는 Relation 치환(호환 가능한 relation으로 변경)으로 생성.

- **Conjunction 생성**: 2개 이상 트리플로 구성된 문장을 SUPPORTED로 사용. 모든 트리플이 존재해야 검증 성공. REFUTED는 Entity 치환으로 생성.

- **Existence 생성**: {head, relation} 또는 {tail, relation} 쌍으로 "∼ had a(an) ∼" 같은 템플릿을 적용. 22개 relation만 현실적 주장이 되도록 필터링.

- **Multi-hop 생성**: Conjunction 주장에서 중간 엔터티를 엔터티 타입명으로 대체. GPT-2-large perplexity로 가장 자연스러운 타입명 선택.

- **Negation 생성**: (1) One-hop: WikiFactCheck-English 기반 Negative Claim Generation 모델 사용. (2) Conjunction: GPT-J를 활용하여 다양한 위치에 부정 삽입. (3) Existence/Multi-hop: 규칙 기반 부정 추가.

- **품질 관리**: NLI 모델(RoBERTa-base on MNLI)로 양방향 contradiction 검증하여 REFUTED 주장 정확성 확보.

## Originality

- 자연언어 주장을 요구하는 첫 번째 대규모 KG 기반 사실 검증 데이터셋 (기존 KG 데이터셋은 단일 트리플만 다룸).

- 5가지 구조화된 추론 유형(One-hop, Conjunction, Existence, Multi-hop, Negation)의 체계적 분류 및 구현.

- NLI 모델 기반 품질 검증, GPT-2 perplexity 활용, 양방향 검증 등 정교한 데이터 생성 파이프라인.

- Colloquial 및 Written 스타일을 모두 포함하여 대화 시스템 등 실제 응용 맥락을 반영.

- 기존 FEVER, TabFact 등과 달리 그래프 구조의 추론 과정이 명확하게 추적 가능하여 해석 가능성(interpretability) 향상.

## Limitation & Further Study

- **데이터 생성의 자동화**: Entity 및 Relation 치환이 자동으로 이루어지지만, 부정 생성(특히 Conjunction/Existence/Multi-hop)에서 규칙 기반 방법이 사용되어 다양성이 제한될 수 있다.

- **언어 다양성**: WebNLG 기반 구성으로 인해 영어 중심이며, 다국어 확장이 미흡하다.

- **실제 KG 완성도**: DBpedia의 불완전성(missing facts)으로 인해 실제 사실 검증 성능에 영향을 미칠 수 있다.

- **추론 복잡도 제한**: Multi-hop이 최대 2개 relation 정도로 제한되어 있어, 더 깊은 추론 경로에 대한 연구 기회가 남아있다.

- **후속 연구**: (1) 신경망 기반 부정 생성 방법 도입. (2) 다국어 및 다중 KG(Wikidata, Freebase) 지원. (3) 부분적 사실(partially true) 주장 추가. (4) 추론 설명(reasoning explanation) 생성 모델 개발.


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.3/5

**총평**: FACTKG는 KG 기반 사실 검증의 체계적이고 대규모 데이터셋을 제시하여 학문적·실용적 가치가 높으나, 자동화된 데이터 생성 파이프라인의 한계와 언어 다양성 부족으로 인해 개선의 여지가 있다. 그래프 구조를 통한 명확한 추론 과정 제시는 해석 가능성이 중요한 사실 검증 분야에 큰 기여를 한다.

## Related Papers

- 🏛 기반 연구: [[papers/267_Defame_Dynamic_evidencebased_fact-checking_with_multimodal_e/review]] — 지식 그래프 기반 사실 검증의 구조적 추론 방법이 멀티모달 증거 기반 팩트체킹 시스템의 추론 모듈 설계 기반을 제공합니다.
- 🔄 다른 접근: [[papers/541_Missing_counter-evidence_renders_nlp_fact-checking_unrealist/review]] — 지식 그래프의 구조화된 추론과 반박 증거 부족 문제 지적이라는 서로 다른 팩트체킹 접근법과 비판을 제시합니다.
- 🔗 후속 연구: [[papers/172_Boolq_Exploring_the_surprising_difficulty_of_natural_yesno_q/review]] — 자연어 예/아니오 질문에서 지식 그래프 기반 구조화된 추론으로 확장한 더 체계적인 사실 검증 접근법입니다.
- 🔄 다른 접근: [[papers/317_Enhancing_natural_language_inference_performance_with_knowle/review]] — 지식 그래프 추론 기반 팩트 검증이 NLI 성능 향상과 같은 목표의 다른 접근법을 제시한다.
- 🔗 후속 연구: [[papers/448_Kgvalidator_A_framework_for_automatic_validation_of_knowledg/review]] — 지식 그래프 기반 추론을 통한 사실 검증으로 지식 그래프 완성 검증을 확장한다.
- 🔄 다른 접근: [[papers/541_Missing_counter-evidence_renders_nlp_fact-checking_unrealist/review]] — 반박 증거 부족의 한계를 지적하는 반면, 지식 그래프 기반 추론을 통한 체계적 사실확인 접근법을 제시합니다.
- 🔄 다른 접근: [[papers/172_Boolq_Exploring_the_surprising_difficulty_of_natural_yesno_q/review]] — 자연 발생 질문에 대한 읽기 이해와 지식 그래프 기반 구조화된 추론이라는 서로 다른 질의응답 접근법입니다.
- 🔗 후속 연구: [[papers/267_Defame_Dynamic_evidencebased_fact-checking_with_multimodal_e/review]] — 텍스트 기반 지식 그래프 추론에서 텍스트와 이미지를 모두 포함하는 멀티모달 팩트체킹으로 확장한 연구입니다.
- 🏛 기반 연구: [[papers/332_Fact-checking_complex_claims_with_program-guided_reasoning/review]] — 지식 그래프를 활용한 팩트체킹의 기초적 접근이 프로그램 가이드 추론 시스템의 이론적 배경을 제공함
- 🏛 기반 연구: [[papers/235_Comparing_knowledge_sources_for_open-domain_scientific_claim/review]] — 지식 그래프를 통한 사실 검증으로 본 논문의 과학적 주장 검증에서 구조화된 지식의 활용 기반을 제공한다.
- 🔄 다른 접근: [[papers/567_Multivers_Improving_scientific_claim_verification_with_weak/review]] — 과학 청구 검증에서 약한 감독과 지식 그래프 추론의 서로 다른 사실 검증 접근법을 비교할 수 있습니다.
