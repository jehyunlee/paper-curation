---
title: "488_Leveraging_LLMs_in_Scholarly_Knowledge_Graph_Question_Answer"
authors:
  - "Tilahun Abedissa Taffa"
  - "Ricardo Usbeck"
date: "2023.11"
doi: "미공개"
arxiv: ""
score: 3.8
essence: "본 논문은 대규모 언어모델(LLM)을 활용하여 학술 지식 그래프에 대한 자연어 질문을 SPARQL 쿼리로 변환하는 few-shot 기반 접근법을 제시하며, SciQA 벤치마크에서 F1 스코어 0.99를 달성했다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Scholarly_Document_QA"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Taffa and Usbeck_2023_Leveraging LLMs in Scholarly Knowledge Graph Question Answering.pdf"
---

# Leveraging LLMs in Scholarly Knowledge Graph Question Answering

> **저자**: Tilahun Abedissa Taffa, Ricardo Usbeck | **날짜**: 2023-11-16 | **DOI**: [미공개](https://doi.org/)

---

## Essence

![Figure 2](figures/fig2.webp) *학술 KGQA 모델의 전체 파이프라인*

본 논문은 대규모 언어모델(LLM)을 활용하여 학술 지식 그래프에 대한 자연어 질문을 SPARQL 쿼리로 변환하는 few-shot 기반 접근법을 제시하며, SciQA 벤치마크에서 F1 스코어 0.99를 달성했다.

## Motivation

- **Known**: 기존 KGQA 시스템은 retriever-reasoner 또는 semantic parsing 기반 접근법을 사용하지만, 두 방식 모두 대량의 학습 데이터가 필요함. 특히 학술 KGQA 데이터셋의 부족으로 인해 일반 KGQA보다 더 어려운 상황
  
- **Gap**: LLM이 생백과사전(Wikidata)에 대해서는 zero-shot으로도 우수한 SPARQL 생성이 가능하지만, ORKG(Open Research Knowledge Graph)의 스키마를 모르기 때문에 올바른 쿼리를 생성하지 못함
  
- **Why**: 학술 지식 그래프는 도메인 특화적이며 스키마가 다르므로, few-shot prompting을 통해 LLM이 학습 질문-SPARQL 쌍으로부터 패턴을 학습하도록 유도할 필요가 있음
  
- **Approach**: BERT 기반 문장 인코더로 유사 질문을 검색하고, top-n개의 유사 질문-SPARQL 쌍을 프롬프트의 예제로 활용하여 LLM(Vicuna-13B)이 대상 질문에 대한 SPARQL을 생성하도록 함

## Achievement

![Figure 1](figures/fig1.webp) *ChatGPT 3.5의 zero-shot SPARQL 생성: Wikidata(좌)에서는 성공, ORKG(우)에서는 실패*

1. **우수한 성능**: SciQA 벤치마크에서 F1 스코어 0.99(top-3 few-shot) 달성, Scholarly-QALD-23 챌린지에서 2위 랭크

2. **Few-shot 최적화**: 1-shot(F1=0.96) → 3-shot(F1=0.99) → 5-shot(F1=0.989)의 결과를 통해 과도한 예제의 부정적 영향을 실증적으로 입증

## How

- **질문 분석(Question Analysis)**: BERT 기반 문장 인코더를 사용하여 학습 데이터셋의 모든 질문을 오프라인으로 임베딩하고, 테스트 질문과의 코사인 유사도를 기반으로 top-5 유사 질문 선택

- **쿼리 생성(Query Generation)**: 프롬프트 템플릿에 유사 질문-SPARQL 쌍(n=1,3,5)을 예제로 포함하고, "Generate SPARQL queries to query the ORKG" 지시문과 함께 Vicuna-13B 인스턴스에 입력

- **답변 추출(Answer Extraction)**: 생성된 SPARQL 쿼리의 특수문자/줄바꿈 정리 후 ORKG SPARQL 엔드포인트에 실행하여 최종 답변 반환

## Originality

- BERT 기반 문장 유사도와 few-shot LLM prompting을 결합한 학술 KGQA 접근법 제시

- 기존의 T5 기반 fine-tuning(DBLP-QuAD) 또는 triple-to-text 변환(JarvisQA)과 달리, 소수의 예제만으로 추가 사전학습 없이 학술 지식 그래프에 적응하는 방식 제안

- Few-shot 수(1, 3, 5)에 따른 성능 변화를 체계적으로 분석하고, 과도한 예제로 인한 성능 저하 메커니즘 규명

## Limitation & Further Study

- **데이터셋 편향성**: 테스트 질문이 학습에 사용된 템플릿으로부터 생성되지 않아 모델이 상대적으로 쉬운 과제에 최적화되었을 가능성. 실제 사람이 작성한 질문에 대한 범용성은 미검증

- **null 답변 문제**: 개발셋에서 모델이 생성한 null 답변(3-shot: 23개, 5-shot: 25개)이 실제 null 답변(14개)을 초과하며, 구문 오류로 인한 null 답변 비율 증가 추세 확인 필요

- **도메인 제한성**: Computer Science 연구 논문에만 특화되어 있으며, 다른 학술 도메인(생명과학, 사회과학 등)에의 전이 학습 효과 미검증

- **후속 연구 방향**: (1) 다양한 LLM 아키텍처(GPT-4, LLaMA-2 등) 비교, (2) 프롬프트 엔지니어링 최적화, (3) 구문 오류 감지 및 자동 수정 메커니즘 개발, (4) 크로스 도메인 평가

## Evaluation

- **Novelty**: 3.5/5 — Few-shot LLM prompting은 잘 알려진 기법이나, 학술 KGQA 컨텍스트에서의 체계적 적용은 신규성 있음

- **Technical Soundness**: 4/5 — 방법론이 명확하고 실험 설계는 합리적이나, 데이터셋 편향성과 null 답변 문제에 대한 심층 분석 부족

- **Significance**: 3.5/5 — SciQA 챌린지 2위 성적은 실질적 영향을 보이나, 제한된 도메인과 템플릿 기반 데이터셋으로 인해 일반화 가능성 의문

- **Clarity**: 4.5/5 — 논문 구조와 방법 설명이 명확하며 Figure 제시가 효과적이나, 실패 사례 분석이 부족

- **Overall**: 3.8/5

**총평**: 본 논문은 LLM의 few-shot 능력을 학술 KGQA에 효과적으로 적용하여 우수한 성능을 달성했으나, 템플릿 기반 데이터셋의 특수성과 제한된 도메인으로 인해 실제 학술 검색 시스템으로의 배포 가능성에는 추가 검증이 필요하다.

## Related Papers

- 🧪 응용 사례: [[papers/530_Medbiolm_Optimizing_medical_and_biological_qa_with_fine-tune/review]] — LLM을 특정 도메인(의료/생물학)에 특화된 QA 시스템으로 발전시킨 사례이다
- 🔗 후속 연구: [[papers/602_Paperqa_Retrieval-augmented_generative_agent_for_scientific/review]] — 과학적 질의응답을 검색 증강 생성 에이전트로 확장한 연구이다
- 🏛 기반 연구: [[papers/715_Scidqa_A_deep_reading_comprehension_dataset_over_scientific/review]] — 과학 문서에 대한 깊이 있는 읽기 이해의 기초를 제공한다
- 🔄 다른 접근: [[papers/063_Agent-enhanced_large_language_models_for_researching_politic/review]] — 정치기관 연구용 LLM 에이전트와 Leveraging LLMs in Scholarly Knowledge Graph QA는 모두 학술 연구 지원을 다루지만, 특정 도메인 특화와 지식그래프 기반 질의응답이라는 서로 다른 접근법을 취합니다.
- 🔄 다른 접근: [[papers/338_Figuring_out_figures_Using_textual_references_to_caption_sci/review]] — 둘 다 과학 논문의 텍스트 정보를 활용한 QA를 다루지만 하나는 도형 캡션 생성에, 다른 하나는 학술 지식 그래프 질의응답에 초점을 맞춘다.
- 🔗 후속 연구: [[papers/530_Medbiolm_Optimizing_medical_and_biological_qa_with_fine-tune/review]] — 일반적인 학술 지식 그래프 QA를 의료/생물학 분야로 특화하여 발전시킨다
