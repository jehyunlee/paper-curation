---
title: "219_Citebart_Learning_to_generate_citations_for_local_citation_r"
authors:
  - "Ege Yiğit Çelik"
  - "Selma Tekır"
date: "2024"
doi: "N/A"
arxiv: ""
score: 4.3
essence: "본 논문은 인용 토큰(citation token)을 마스킹하는 사용자 정의 사전학습을 통해 로컬 인용 추천(Local Citation Recommendation, LCR) 작업을 수행하는 생성형 모델 CiteBART를 제안한다. 기존의 사전-검색 및 재순위(pre-fetch and re-rank) 파이프라인과 달리 엔드-투-엔드 학습 시스템으로 우수한 성능을 달성한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Citation_Context_Generation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Çelik and Tekır_2024_Citebart Learning to generate citations for local citation recommendation.pdf"
---

# Citebart: Learning to generate citations for local citation recommendation

> **저자**: Ege Yiğit Çelik, Selma Tekır | **날짜**: 2024 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)
*CiteBART의 워크플로우. 노란색과 녹색 예시는 각각 CiteBART-Base와 CiteBART-Global의 작동 방식을 나타낸다.*

본 논문은 인용 토큰(citation token)을 마스킹하는 사용자 정의 사전학습을 통해 로컬 인용 추천(Local Citation Recommendation, LCR) 작업을 수행하는 생성형 모델 CiteBART를 제안한다. 기존의 사전-검색 및 재순위(pre-fetch and re-rank) 파이프라인과 달리 엔드-투-엔드 학습 시스템으로 우수한 성능을 달성한다.

## Motivation

- **Known**: 기존 LCR 방법들은 주로 두 단계 프로세스(BERT-GCN, DualEnh, HAtten, SymTax)를 채택하며, 트랜스포머 아키텍처를 간접적으로만 활용하거나 재순위 단계에서만 활용한다. 특히 HAtten 같은 방법은 테스트 셋의 후보 논문 메타데이터(제목, 초록)를 직접 활용한다.

- **Gap**: 트랜스포머 기반 생성형 접근법이 LCR에서 전도유망함이 보고되었으나, 인용 토큰 마스킹(citation token masking)이라는 작업 특화 사전학습 전략은 아직 체계적으로 탐구되지 않았다.

- **Why**: 인용은 과학 논문의 핵심 요소이며, 정확한 인용 추천은 문헌 조사 품질과 논문 작성 효율성을 크게 향상시킬 수 있다.

- **Approach**: BART 인코더-디코더 아키텍처에서 저자-날짜 형식의 인용 토큰을 마스킹하고 재구성하도록 학습. 로컬 문맥만 사용하는 Base 방식과 저자 논문의 제목 및 초록을 추가하는 Global 방식의 두 가지 변형 제안.

## Achievement

![Figure 2](figures/fig2.webp)
*올바른 예측(a)과 부정확한 예측(b)을 포함한 정성적 분석 사례.*

1. **벤치마크 성능**: CiteBART-Global이 FullTextPeerRead를 제외한 모든 LCR 벤치마크에서 최첨단 성능 달성. 특히 Refseer와 ArXiv 같은 대규모 데이터셋에서 유의미한 개선을 보임. Refseer에서 학습된 모델이 최고 성능 모델으로 기록됨.

2. **할루시네이션 분석**: Top-3 예측의 매크로 할루시네이션율(MaHR)이 4%에 불과하며, 정답이 Top-k 리스트에 포함될 때 다른 예측의 할루시네이션 경향이 유의미하게 감소함을 실증.

3. **교차 데이터셋 일반화**: CiteBART-Global이 강한 교차 데이터셋 일반화 능력을 보유.

## How

![Figure 3](figures/fig3.webp)
*Global 데이터셋 생성을 위한 대규모 언어 모델(LLM)에 대한 프롬프트 예시.*

- **CiteBART-Base**: 로컬 문맥에서 인용 토큰을 마스킹하고 저자-날짜 형식의 인용을 예측하도록 학습. 문맥만을 입력으로 활용.

- **CiteBART-Global**: Base 방식을 확장하여 저자 논문의 제목과 초록을 로컬 문맥에 연결. REALM 프레임워크에서 영감을 받아 글로벌 정보를 통해 역전파(backpropagation)되도록 설계.

- **사전학습 전략**: 인용 토큰 마스킹은 균일 무작위 마스킹이 아닌 작업 특화 전략으로, SpanBERT나 PMI-Masking 같은 일반 토큰 마스킹과 차별화됨.

- **추론 단계**: 테스트 단계에서는 강화된 문맥(로컬 문맥 + 저자 논문 메타데이터)만을 입력하며, 후보 논문의 메타데이터를 직접 활용하지 않음 (HAtten과의 핵심 차이점).

- **엔드-투-엔드 학습**: 사전-검색-재순위 파이프라인과 달리 전체 시스템이 통합된 생성형 모델로 학습되고 추론됨.

## Originality

- **작업 특화 사전학습**: 인용 토큰 마스킹이라는 LCR에 특화된 사전학습 목적함수를 제시한 최초의 시도. 기존의 일반 MLM(Masked Language Modeling)과 구분되는 새로운 접근.

- **후보 논문 메타데이터 미사용**: 기존 파이프라인 기반 방법(HAtten, SymTax)과 달리 테스트 단계에서 후보 논문의 제목/초록을 활용하지 않음으로써, 실제 추천 상황에서 더 현실적인 설정 제시.

- **생성형 엔드-투-엔드 시스템**: LCR을 처음으로 완전한 생성형 아키텍처로 모델링. 기존 인코더 기반 또는 파이프라인 기반 방법과 차별화.

- **Global 학습 스킴**: 저자 논문의 전역 정보(제목, 초록)를 학습 신호로 활용하는 REALM 기반 아이디어의 적용.

- **포괄적 분석**: 할루시네이션의 상세한 분류체계(taxonomy) 및 매크로 할루시네이션율 메트릭 제시. 교차 데이터셋 일반화 능력 실증적 검증.

## Limitation & Further Study

- **소규모 데이터셋 성능**: FullTextPeerRead(PeerRead) 데이터셋에서는 HAtten 등 기존 방법을 능가하지 못함. 생성형 사전학습의 이점을 보이기에 데이터셋이 너무 작다는 한계 지적.

- **할루시네이션**: 완전히 제거되지 않은 할루시네이션 문제(4%의 MaHR도 여전히 존재). 특히 정답이 Top-k에 없을 때 다른 논문을 추천하는 경우의 신뢰성.

- **계산 효율성**: 사전-검색-재순위 파이프라인과의 추론 시간/메모리 비교 분석 부재. 엔드-투-엔드 생성 시스템의 확장성 논의 부족.

- **후속 연구 방향**: 
  - 더욱 정교한 할루시네이션 완화 전략 개발
  - 소규모 데이터셋에서의 성능 향상 방안
  - 더 큰 규모의 인용 코퍼스 활용 시 성능 변화 연구
  - 다국어 과학 문헌에 대한 확장
  - 실시간 인용 추천 시스템으로의 배포 시 추론 최적화

## Evaluation

- **Novelty**: 4.5/5
  - 작업 특화 마스킹과 엔드-투-엔드 생성형 접근은 LCR에서 참신함. 다만 개별 요소(BART, 마스킹, REALM 아이디어)는 기존 기법의 조합.

- **Technical Soundness**: 4/5
  - 방법론이 명확하고 실험 설계가 체계적임. 코드와 데이터셋 공개로 재현성 우수. 다만 소규모 데이터셋의 성능 저하에 대한 이론적 분석 부족.

- **Significance**: 4.5/5
  - 대규모 벤치마크(Refseer, ArXiv)에서의 우수한 성능과 교차 데이터셋 일반화는 실제 응용 가치 높음. 과학 논문 저작 보조 도구로서의 실질적 기여.

- **Clarity**: 4.5/5
  - 논문 구성이 명확하고 Figure와 Table로 개념 설명이 잘 됨. 다만 Base와 Global 방식 간의 이론적 차이와 학습 메커니즘을 더 깊게 설명할 여지 있음.

- **Overall**: 4.3/5

**총평**: CiteBART는 LCR 문제에 대한 창의적인 생성형 접근으로서, 특히 대규모 데이터셋에서 우수한 성능을 보이며 실제 응용 가치가 높다. 다만 소규모 데이터셋 성능 한계와 할루시네이션 문제는 추가 개선이 필요하다.

## Related Papers

- 🔗 후속 연구: [[papers/420_Ilciter_Evidence-grounded_interpretable_local_citation_recom/review]] — 생성형 인용 모델에서 증거 기반 해석 가능한 로컬 인용 추천으로 발전한 더 정교한 인용 추천 시스템입니다.
- 🏛 기반 연구: [[papers/220_Cited_text_spans_for_citation_text_generation/review]] — 인용 텍스트 생성 연구가 로컬 인용 추천을 위한 인용 토큰 마스킹 학습의 기초 아이디어를 제공합니다.
- 🧪 응용 사례: [[papers/109_Assisting_in_writing_wikipedia-like_articles_from_scratch_wi/review]] — 처음부터 위키피디아 스타일 글 작성 지원에서 로컬 인용 추천이라는 구체적 기능을 제공하는 응용 기술입니다.
- 🏛 기반 연구: [[papers/406_Hlm-cite_Hybrid_language_model_workflow_for_text-based_scien/review]] — 지역적 인용 맥락에서의 인용문 생성 기법으로 HLM-Cite의 텍스트 기반 인용 예측 방법론의 기초를 제공한다.
- 🧪 응용 사례: [[papers/882_When_large_language_models_meet_citation_A_survey/review]] — 인용 텍스트 생성의 구체적 방법론이 LLM과 인용 분석의 실제 응용 사례를 보여준다.
- 🔄 다른 접근: [[papers/1091_Scirgc_Multi-granularity_citation_recommendation_and_citatio/review]] — 로컬 인용 생성을 위한 BART 기반 접근법으로 본 논문의 인용 추천과 다른 방식의 인용 생성을 제시한다.
- 🏛 기반 연구: [[papers/420_Ilciter_Evidence-grounded_interpretable_local_citation_recom/review]] — 지역 인용 생성의 기본 방법론이 증거 기반 해석가능한 인용 추천의 이론적 기반을 제공합니다.
- 🔗 후속 연구: [[papers/273_Directed_criteria_citation_recommendation_and_ranking_throug/review]] — 지역 인용 생성을 그래프 링크 예측이라는 더 구조적 접근법으로 확장한다
