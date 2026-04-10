---
title: "220_Cited_text_spans_for_citation_text_generation"
authors:
  - "Xiangci Li"
  - "Yi‐Hui Lee"
  - "Jessica Ouyang"
date: "2023"
doi: "N/A"
arxiv: ""
score: 4.0
essence: "과학 논문의 인용 텍스트 자동 생성을 위해 기존의 초록(abstract)만 사용하는 방식 대신, 실제 인용되는 특정 텍스트 구간(Cited Text Span, CTS)을 활용하여 더 정확하고 충실한 인용 생성이 가능함을 보여준다. 이를 위해 원가(distant labeling)를 통해 대규모 CTS 데이터셋을 구축하고, 실용적인 키워드 기반 CTS 검색 방법을 제안한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Citation_Context_Generation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Li et al._2023_Cited text spans for citation text generation.pdf"
---

# Cited text spans for citation text generation

> **저자**: Xiangci Li, Yi‐Hui Lee, Jessica Ouyang | **날짜**: 2023 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)
*Overview of the proposed CTS-based citation generation approach. Context, Oracle, Keyword 전략을 통해 인용 논문에서 CTS를 검색하고 인용 텍스트를 생성*

과학 논문의 인용 텍스트 자동 생성을 위해 기존의 초록(abstract)만 사용하는 방식 대신, 실제 인용되는 특정 텍스트 구간(Cited Text Span, CTS)을 활용하여 더 정확하고 충실한 인용 생성이 가능함을 보여준다. 이를 위해 원가(distant labeling)를 통해 대규모 CTS 데이터셋을 구축하고, 실용적인 키워드 기반 CTS 검색 방법을 제안한다.

## Motivation

- **Known**: 기존 추상적 인용 생성(abstractive citation generation) 접근법들은 계산상의 제약으로 인해 인용 논문의 초록에만 기반하여 모델을 학습해왔다. 또한 Li et al. (2022)에 따르면 인간이 작성한 골드 인용 텍스트의 관련성 평가 점수가 초록에 대해 정의될 때 시스템 생성 인용보다 유의미하게 낮다.

- **Gap**: 초록은 항상 인용 생성에 가장 적절한 입력이 아니며, 골드 인용 텍스트가 논문 본문 내용을 참조하는 경우가 많으나 이 정보에 접근할 수 없다. 기존 CTS 데이터셋은 매우 작고(364-239개), 주석자간 일치도가 낮으며(Cohen's κ = 0.16∼0.52), 자동 CTS 검색 시스템의 성능도 부실(F1 < 0.2)하다.

- **Why**: CTS 기반 인용 생성은 충실성(grounding)을 통해 환각(hallucination)을 방지할 수 있으나, 수동 주석은 노동 집약적이고 비실용적이다.

- **Approach**: (1) 원가 레이블링(distant labeling)으로 대규모 CTS 데이터셋 구축, (2) 기존 CTS 검색 방식의 문제점 식별, (3) 인간-루프 기반 키워드 검색 방식 제안

## Achievement

![Figure 2](figures/fig2.webp)
*원가 레이블링 CTS는 상위 40개 문장에서 CL-SciSumm의 80%, AbuRa'ed의 95% 인간 주석 CTS를 커버*

![Figure 4](figures/fig4.webp)
*원가 레이블링 CTS(실선)는 인간 주석 CTS(점선)보다 높은 ROUGE-L 리콜 성능 달성*

1. **원가 레이블링의 효과성**: ROUGE 기반 원가 레이블링이 인간 주석과 비슷한 수준의 충실성(QuestEval, ANLI 평가)을 보이면서도 더 높은 토큰 오버랩을 달성했다. 이는 하나의 인용에 대해 여러 개의 타당한 CTS가 존재할 수 있음을 시사한다.

2. **다운스트림 작업 성능**: 원가 레이블링 CTS로 학습한 모델이 인간 주석 CTS 기반 모델과 비슷하거나 더 우수한 인용 생성 성능(BLEU, METEOR, ROUGE-L)을 달성했으며, CL-SciSumm 데이터셋에서는 오히려 우월했다.

3. **실용적 가능성**: 초록 기반 접근법 대비 CTS 기반 인용 생성으로 명백히 개선된 충실성과 정확도를 입증함으로써, 전체 논문 텍스트 기반 인용 생성의 타당성 확보했다.

## How

![Figure 1](figures/fig1.webp)

- **원가 레이블링 전략**: 골드 인용 텍스트를 쿼리로 사용하여 인용 논문에서 상위-k개 문장을 ROUGE-1/2 리콜 기반으로 순위 지어 CTS 후보 추출. GPU 불필요한 ROUGE 기반 방식 선택으로 계산 효율성 확보

- **평가 메트릭**: 
  - 토큰 오버랩 (ROUGE-recall)
  - 충실성 (QuestEval, ANLI non-contradiction score)
  
- **인용 생성 모델**: 두 가지 아키텍처 실험
  - RAG-FiD (Retrieval-Augmented Generation with Fusion-in-Decoder)
  - LED (Longformer Encoder-Decoder)를 Oracle 검색과 함께 사용

- **키워드 기반 CTS 검색**: 골드 인용 텍스트 대신 인용 맥락(citation context)의 키워드를 추출하여 검색 쿼리로 사용. 인간 개입을 통해 실용성 확보

- **데이터셋 구성**: CL-SciSumm 364개, AbuRa'ed 194개 (45개 제외) 인용 사례 활용하여 원가 레이블링 검증

## Originality

- **새로운 문제 정의**: 기존 CTS 검색 시스템이 인용 생성 태스크에 부적절한 이유를 명확히 지적 (골드 인용 텍스트를 쿼리로 사용하는 문제)

- **원가 레이블링의 정당화**: 인간 주석의 낮은 일치도를 "여러 타당한 CTS 존재 가능성" 관점에서 재해석하여 원가 레이블링의 품질 동등성 입증

- **실용적 접근**: 인간-루프 기반 키워드 검색 방식으로 실제 인용 생성 시스템 적용 가능성 제시 (기존 오라클 기반 방식의 한계 극복)

- **대규모 데이터셋 구축**: 기존 수동 주석 데이터셋의 크기 제약을 원가 레이블링으로 해결

## Limitation & Further Study

- **CTS 다양성 부족**: 원가 레이블링은 높은 토큰 오버랩을 우선시하기 때문에 의미적으로 유사하지만 다른 표현의 CTS를 놓칠 수 있다 (BERTScore가 ROUGE를 약간 하회한 이유)

- **키워드 추출의 수동성**: 제안된 키워드 기반 CTS 검색이 "인간-루프" 방식으로, 완전 자동화되지 않았다. 자동 키워드 추출 방법의 개발 필요

- **평가 메트릭의 한계**: BLEU, METEOR, ROUGE-L 등 자동 평가 메트릭만 사용되었으며, 인간 평가를 통한 충실성과 충분성(informativeness) 검증 부재

- **모델 스케일의 제약**: LED/RAG-FiD 등 상대적으로 작은 모델 기반 실험. 최신 LLM(GPT-3.5 등)과의 비교 평가 미수행

- **후속 연구 방향**:
  - 의미적 CTS 다양성을 포착할 수 있는 밀도 검색(dense retrieval) 방식 개선
  - 자동 키워드 추출 알고리즘 개발
  - 대규모 LLM을 활용한 인용 생성 및 검증
  - 학제 간 일반화 (학제별 인용 패턴의 차이 고려)


## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 인용 생성 시스템에서 초록의 한계를 지적하고 CTS 기반 접근의 타당성을 체계적으로 입증한 가치 있는 연구이다. 원가 레이블링으로 수작업 주석의 부담을 경감한 점이 실무적 기여도 크다. 다만 완전 자동화된 CTS 검색 실현 및 대규모 생성 모델과의 통합 검증이 보완되면 영향력이 더욱 증대될 것으로 기대된다.

## Related Papers

- 🔗 후속 연구: [[papers/238_Controllable_citation_sentence_generation_with_language_mode/review]] — 제어 가능한 인용 문장 생성 연구로 본 논문의 인용 텍스트 구간 활용을 언어 모델 제어로 발전시킨다.
- 🏛 기반 연구: [[papers/1091_Scirgc_Multi-granularity_citation_recommendation_and_citatio/review]] — 다중 단위 인용 추천 및 문장 생성에서 본 논문의 CTS 방법론을 인용 의도와 결합한 기반을 제공한다.
- 🔄 다른 접근: [[papers/420_Ilciter_Evidence-grounded_interpretable_local_citation_recom/review]] — 해석 가능한 로컬 인용 추천으로 본 논문의 인용 생성과 다른 접근법인 인용 추천 시스템을 제시한다.
- 🏛 기반 연구: [[papers/219_Citebart_Learning_to_generate_citations_for_local_citation_r/review]] — 인용 텍스트 생성 연구가 로컬 인용 추천을 위한 인용 토큰 마스킹 학습의 기초 아이디어를 제공합니다.
- 🏛 기반 연구: [[papers/238_Controllable_citation_sentence_generation_with_language_mode/review]] — 인용 텍스트 생성을 위한 인용된 텍스트 구간 활용 연구로 본 논문의 제어 가능한 생성을 위한 입력 정보 기반을 제공한다.
- 🔗 후속 연구: [[papers/420_Ilciter_Evidence-grounded_interpretable_local_citation_recom/review]] — 인용 텍스트 스팬 추출을 해석가능한 증거 스팬 제시로 발전시켜 더 투명한 인용 추천을 가능하게 합니다.
