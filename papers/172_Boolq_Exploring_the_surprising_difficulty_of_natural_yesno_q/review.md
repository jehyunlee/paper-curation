---
title: "172_Boolq_Exploring_the_surprising_difficulty_of_natural_yesno_q"
authors:
  - "Christopher Clark"
  - "Kenton Lee"
  - "Ming‐Wei Chang"
  - "Tom Kwiatkowski"
  - "Michael J. Collins"
date: "2019"
doi: "N/A"
arxiv: ""
score: 4.4
essence: "자연 발생적 예/아니오 질문에 대한 읽기 이해 데이터셋 BoolQ를 제시하며, BERT와 같은 최신 사전학습 모델도 도전적인 이 작업에서 인간 성능(90%)과 큰 격차(80.4%)를 보임을 입증한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Scientific_Question_Answering"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Clark et al._2019_Boolq Exploring the surprising difficulty of natural yesno questions.pdf"
---

# BoolQ: Exploring the Surprising Difficulty of Natural Yes/No Questions

> **저자**: Christopher Clark, Kenton Lee, Ming‐Wei Chang, Tom Kwiatkowski, Michael J. Collins, Kristina Toutanova | **날짜**: 2019 | **DOI**: N/A

---

## Essence

자연 발생적 예/아니오 질문에 대한 읽기 이해 데이터셋 BoolQ를 제시하며, BERT와 같은 최신 사전학습 모델도 도전적인 이 작업에서 인간 성능(90%)과 큰 격차(80.4%)를 보임을 입증한다.

## Motivation

- **Known**: 기존 자연언어 추론(NLI) 연구는 주로 명시된 단순한 추론만 요구하는 문제들로 구성되어 있으며, 예/아니오 질문이 일부 데이터셋에 포함되어 있지만 자연 발생적이지 않음.

- **Gap**: 자연적으로 생성된 예/아니오 질문들이 실제로 얼마나 어려운 추론 능력을 요구하는지, 그리고 전이학습(transfer learning)에서 어떤 소스 데이터가 가장 효과적인지에 대한 연구 부족.

- **Why**: 사용자의 실제 검색 쿼리에서 자연 발생한 예/아니오 질문들은 복잡한 추론을 요구하지만, 이를 체계적으로 평가할 대규모 데이터셋이 없음.

- **Approach**: Google 검색 엔진 쿼리에서 자연 발생적으로 수집한 16,000개의 예/아니오 질문을 Wikipedia 문단과 쌍으로 구성하여 BoolQ 데이터셋 구축, 다양한 전이학습 기법 실험.

## Achievement

![Figure 1](https://imgur.com/placeholder.jpg) 
*BoolQ 데이터셋의 예시: 자연 발생적 예/아니오 질문, Wikipedia 문단, 정답 및 설명*

1. **도전적 데이터셋 구축**: 자연 발생적 질문들이 단순 사실 질문을 넘어 복잡한 비-사실적 정보(non-factoid)를 요구함을 입증. 엔터테인먼트, 자연과학, 스포츠 등 다양한 주제 포함.

2. **전이학습 효과성 규명**: MultiNLI에서의 전이학습이 SQuAD 같은 추출형 QA(extractive QA)나 의역(paraphrase) 데이터 전이보다 훨씬 효과적임을 실증.

3. **BERT의 한계 노출**: 사전학습된 BERT도 단독으로는 62% 정도의 성능만 달성하며, MultiNLI 전이학습과 결합했을 때 80.4%에 도달하여 BERT만으로는 충분하지 않음을 명시.

## How

- **데이터 수집 파이프라인**: Natural Questions(NQ) 파이프라인을 기반으로 Google 검색 쿼리에서 자동으로 예/아니오 질문 필터링(첫 단어가 "did", "is", "are" 등 지시어 집합에 포함되는 경우 선택).

- **3단계 주석(annotation) 프로세스**: (1) 질문이 명확하고 사실적인지 판단, (2) 질문에 답변하기 충분한 Wikipedia 문단 탐색 및 선택, (3) 예/아니오 답변 표시.

- **데이터셋 구성**: 13k개의 새로운 질문 + NQ 훈련셋의 3k개 질문 = 총 16k개. 훈련셋(9.4k), 개발셋(3.2k), 시험셋(3.2k)으로 분할. 예 답변 비율 62.31%.

- **전이학습 기법**: (1) BERT 단독, (2) MultiNLI 데이터로 사전학습 후 BoolQ에서 재학습, (3) SQuAD 데이터 활용, (4) 다양한 NLI 데이터셋 조합.

- **기준선(baseline) 비교**: 다수결 기준선(majority baseline) 62.31% vs. 인간 성능 90% vs. 최고 모델 80.43%.

## Originality

- **자연 발생적 데이터 수집의 중요성**: 기존의 인위적으로 조작된 데이터셋과 달리 실제 사용자 검색 쿼리에서 자연스럽게 발생한 질문들을 수집하여 실제 응용 가능성 제시.

- **예/아니오 질문의 숨겨진 복잡성 규명**: 단순해 보이는 예/아니오 질문이 실제로는 복잡한 추론, 암묵적 정보 추출, 반증적 추론(contradictory inference)을 요구함을 체계적으로 증명.

- **NLI-QA 전이학습의 보완성**: 최신 사전학습 모델(BERT)과 지도학습 기반 전이학습(MultiNLI)이 상호 보완적임을 최초로 명시적으로 실증.

- **명확한 인간-모델 성능 격차**: 90% 인간 성능 대비 80.4% 모델 성능으로 약 10% 격차를 정량화하여 향후 연구 방향을 제시.

## Limitation & Further Study

- **제한사항**:
  - 단일 쌍(question-passage) 구조로 멀티-홉(multi-hop) 추론이 제한적
  - 예/아니오 답변 비율이 불균형(62% 예 답변)
  - Wikipedia에만 국한되어 다른 도메인의 자연 질문 다양성 부족
  - 모델들이 문장 제목(article title)을 활용하지 않아 활용 가능성 미검증

- **후속 연구**:
  - 더욱 정교한 추론 능력을 요구하는 멀티-스텝 질문 확장
  - 도메인 외(out-of-domain) 질문에 대한 전이학습 효율성 연구
  - 설명 가능성(explainability)과 신뢰도(reliability) 분석
  - 더 큰 규모의 사전학습 모델(GPT 계열)과의 비교 실험


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4.5/5
- Significance: 4/5
- Clarity: 4.5/5
- Overall: 4.4/5

**총평**: BoolQ는 자연 발생적 예/아니오 질문의 내재된 복잡성을 체계적으로 규명하고, BERT 이후 시대에도 NLI 전이학습의 지속적 가치를 증명하는 중요한 벤치마크 데이터셋이다. 다만 멀티-홉 추론과 도메인 다양성 측면에서는 확장 가능성을 남겨두고 있다.

## Related Papers

- 🏛 기반 연구: [[papers/747_Selfcheck_Using_llms_to_zero-shot_check_their_own_step-by-st/review]] — 자연어 예/아니오 질문의 도전성을 보인 연구가 LLM의 자체 추론 검증 능력 연구의 기초적 동기를 제공합니다.
- 🔄 다른 접근: [[papers/333_Factkg_Fact_verification_via_reasoning_on_knowledge_graphs/review]] — 자연 발생 질문에 대한 읽기 이해와 지식 그래프 기반 구조화된 추론이라는 서로 다른 질의응답 접근법입니다.
- 🔗 후속 연구: [[papers/645_Pubmedqa_A_dataset_for_biomedical_research_question_answerin/review]] — 일반적인 예/아니오 질문에서 생물의학 도메인의 전문적 질의응답으로 확장한 도메인 특화 연구입니다.
- 🔗 후속 연구: [[papers/747_Selfcheck_Using_llms_to_zero-shot_check_their_own_step-by-st/review]] — 자연 예/아니오 질문의 어려움을 보인 연구에서 LLM이 자체 추론을 검증할 수 있는지로 확장한 더 고차원적 연구입니다.
- 🔗 후속 연구: [[papers/333_Factkg_Fact_verification_via_reasoning_on_knowledge_graphs/review]] — 자연어 예/아니오 질문에서 지식 그래프 기반 구조화된 추론으로 확장한 더 체계적인 사실 검증 접근법입니다.
