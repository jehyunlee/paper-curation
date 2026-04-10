---
title: "420_Ilciter_Evidence-grounded_interpretable_local_citation_recom"
authors:
  - "Sayar Ghosh Roy"
  - "Jiawei Han"
date: "2024"
doi: "미제공"
arxiv: ""
score: 4.0
essence: "본 논문은 학술 논문 인용 추천 작업에 **해석가능성(interpretability)**을 도입하기 위해, 쿼리(claim 또는 entity mention)에 대해 인용할 논문을 추천할 때 기존 문헌에서 추출한 유사한 증거 스팬(evidence span)을 근거로 제시하는 새로운 접근방식 ILCiteR을 제안한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Citation_Context_Generation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Roy and Han_2024_Ilciter Evidence-grounded interpretable local citation recommendation.pdf"
---

# ILCiteR: Evidence-grounded interpretable local citation recommendation

> **저자**: Sayar Ghosh Roy, Jiawei Han | **날짜**: 2024 | **DOI**: [미제공](https://arxiv.org/abs/2403.08737)

---

## Essence

![Figure 2](figures/fig2.webp) *ILCiteR 시스템의 개요: 증거 데이터베이스 사전 로딩, 조건부 신경 순위 앙상블을 통한 증거 스팬 재순위화, 논문 순위화의 3단계 프로세스*

본 논문은 학술 논문 인용 추천 작업에 **해석가능성(interpretability)**을 도입하기 위해, 쿼리(claim 또는 entity mention)에 대해 인용할 논문을 추천할 때 기존 문헌에서 추출한 유사한 증거 스팬(evidence span)을 근거로 제시하는 새로운 접근방식 ILCiteR을 제안한다.

## Motivation

- **Known**: 기존 로컬 인용 추천(local citation recommendation) 시스템들은 쿼리 공간에서 논문 공간으로의 직접적인 매핑을 학습하여, 특정 논문을 인용해야 하는 이유를 명확히 설명할 수 없고 해석성이 제한적이다.

- **Gap**: 왜 특정 논문을 인용해야 하는지에 대한 명시적인 추론 메커니즘이 부재하며, 기존 방법들은 대규모 라벨링 데이터에 대한 비용이 높고 논문 풀(pool)이 업데이트될 때마다 모델을 재학습해야 한다.

- **Why**: 과학 논문 작성에서 인용의 근거를 명확히 제시하면 추천의 신뢰성을 높이고 저자가 더 나은 결정을 내릴 수 있다.

- **Approach**: 쿼리와 유사하면서 동시에 특정 논문을 인용하고 있는 기존 문헌의 증거 스팬을 찾아 이를 근거로 인용을 추천하는 증거 기반 프레임워크를 도입한다.

## Achievement

![Figure 1](figures/fig1.webp) *로컬 인용 추천 작업의 개요: 쿼리와 후보 논문 풀로부터 인용 가능한 논문을 추천*

1. **증거 기반 로컬 인용 추천 작업 정의**: 기존의 직접적 매핑 방식에서 벗어나 증거 스팬을 매개변수로 하는 새로운 문제 정의를 도입하여 모든 추천이 구체적인 근거를 갖도록 함.

2. **대규모 증거 데이터베이스 구축**: Computer Science 분야의 3가지 주요 주제(NER, SUMM, MT)에 대해 200,000개 이상의 고유한 증거 스팬과 인용 논문 쌍을 포함하는 데이터셋 개발 (NER: 23,803개, SUMM: 79,345개, MT: 108,692개 스팬).

3. **학습 없는 추천 시스템**: 원거리 감시(distant supervision) 학습 방식과 사전학습된 Transformer 언어모델을 활용하여 명시적인 모델 학습 없이 동작하므로 논문 풀 업데이트 시 재학습이 불필요.

4. **조건부 신경 순위 앙상블**: 어휘 유사성과 의미적 유사성을 결합한 순위 재정렬 방식이 순수 렉시컬/시맨틱 검색 및 단순 앙상블보다 우수한 성능 달성.

## How

![Figure 3](figures/fig3.webp) *조건부 신경 순위 앙상블: 여러 유사도 점수를 결합하여 증거 스팬 재순위화*

**증거 데이터베이스 구축 (Section 5)**:
- S2ORC 데이터셋에서 정규화된 전문 텍스트를 가진 20,000개 이상의 Computer Science 논문 수집
- 각 논문에서 최소 하나의 인용([REF] 태그)을 포함하는 문장 추출
- 각 문장에서 관련 텍스트 스팬을 증거로 추출하고, 동일 증거에 대한 인용 횟수를 support로 기록

**2단계 재순위화 프로세스 (Section 6)**:
1. **증거 스팬 재순위화**: 
   - 어휘 유사도(BM25)로 m개의 후보 증거 스팬 사전 로딩
   - 조건부 신경 순위 앙상블을 이용해 시맨틱 유사도(SBERT 임베딩)와 어휘 유사도 결합
   
2. **논문 순위화**:
   - 선택된 증거 스팬들과 연관된 모든 논문 후보 추출
   - 각 논문에 대해: (1) 최적 관련 증거 스팬의 순위, (2) 누적 support 수, (3) 출판 연도(최신성)를 종합 고려하여 최종 순위 결정

## Originality

- **새로운 문제 정의**: 기존의 쿼리→논문 직접 매핑에서 쿼리→증거스팬→논문의 3단계 구조로 전환하여 해석가능성을 핵심으로 도입한 첫 시도.

- **원거리 감시 기반 설계**: 별도의 라벨링 과정 없이 기존 인용 구조로부터 자동 추출한 증거-논문 쌍을 활용한 혁신적 접근.

- **학습 불필요 아키텍처**: 사전학습 모델만으로 동작하여 새로운 논문 추가 시 재학습이 불필요한 실용적 설계.

- **조건부 신경 순위 앙상블**: 기존 순위 앙상블 방식을 개선하여 쿼리 특성을 반영한 동적 가중치 학습 적용.

## Limitation & Further Study

- **증거 추출의 단순성**: 문장 단위 추출에 기반하여 더 복잡한 문맥적 정보가 손실될 수 있으며, 추출된 증거 스팬의 품질이 PDF 파싱 오류에 영향을 받음.

- **주제 범위 제한**: 현재 NER, SUMM, MT 3가지 NLP 주제에만 한정되어 있으며, 다른 Computer Science 분야나 다학제 논문 추천으로의 확장성 미흡.

- **평가 데이터셋 부재**: 논문에서 평가 방법론에 대한 자세한 설명이 제시된 본문에서 누락되어 있으며, 인간 평가(human evaluation)의 규모와 방식이 불명확.

- **후속 연구 방향**:
  - 멀티홉(multi-hop) 증거 스팬 구성으로 더 복잡한 인용 관계 모델링
  - 대규모 언어모델(LLM) 활용한 증거 요약 및 설명 생성
  - 학제간 인용 추천으로 확장 및 도메인 특화 모델 개발
  - 인용 맥락의 감정/의도 분류를 통한 더 세분화된 추천

## Evaluation

- **Novelty**: 4.5/5
  - 증거 기반 해석가능한 추천이라는 새로운 문제 정의와 접근방식은 혁신적이나, 증거 추출 자체는 기존 기술의 조합

- **Technical Soundness**: 4/5
  - 전체 방법론은 논리적이고 견고하지만, 평가 방법론 상세 설명 부재로 재현성 우려
  - 조건부 신경 순위 앙상블의 이론적 기반이 다소 제한적

- **Significance**: 4/5
  - 인용 추천 시스템에 해석가능성 도입은 중요한 기여이나, 실제 적용 시나리오와 사용자 연구 부족
  - 200K+ 규모의 증거 데이터셋은 커뮤니티 자산으로 가치있음

- **Clarity**: 3.5/5
  - 전체 구조는 명확하나 Section 6 평가 부분이 본문에서 누락
  - 조건부 신경 순위 앙상블의 상세한 수식과 구현 디테일 부족

- **Overall**: 4/5

**총평**: 학술 논문 인용 추천에 **해석가능성**이라는 중요한 차원을 도입한 의미 있는 연구로, 원거리 감시 기반의 실용적 설계와 대규모 증거 데이터셋 구축이 장점이다. 다만 평가 방법론의 상세 제시와 실제 사용자 연구를 통한 해석가능성 검증이 이루어진다면 더욱 강력한 논문이 될 수 있다.

## Related Papers

- 🏛 기반 연구: [[papers/219_Citebart_Learning_to_generate_citations_for_local_citation_r/review]] — 지역 인용 생성의 기본 방법론이 증거 기반 해석가능한 인용 추천의 이론적 기반을 제공합니다.
- 🔗 후속 연구: [[papers/220_Cited_text_spans_for_citation_text_generation/review]] — 인용 텍스트 스팬 추출을 해석가능한 증거 스팬 제시로 발전시켜 더 투명한 인용 추천을 가능하게 합니다.
- 🔄 다른 접근: [[papers/150_Benchmark_for_evaluation_and_analysis_of_citation_recommenda/review]] — 인용 추천 평가에서 해석가능성 중심 접근법과 전통적인 벤치마킹 방식의 서로 다른 관점을 제시합니다.
- 🔗 후속 연구: [[papers/219_Citebart_Learning_to_generate_citations_for_local_citation_r/review]] — 생성형 인용 모델에서 증거 기반 해석 가능한 로컬 인용 추천으로 발전한 더 정교한 인용 추천 시스템입니다.
- 🔗 후속 연구: [[papers/1091_Scirgc_Multi-granularity_citation_recommendation_and_citatio/review]] — 해석 가능한 로컬 인용 추천 시스템으로 본 논문의 인용 추천 기능을 설명 가능성 측면에서 확장한다.
- 🔄 다른 접근: [[papers/220_Cited_text_spans_for_citation_text_generation/review]] — 해석 가능한 로컬 인용 추천으로 본 논문의 인용 생성과 다른 접근법인 인용 추천 시스템을 제시한다.
- 🔄 다른 접근: [[papers/273_Directed_criteria_citation_recommendation_and_ranking_throug/review]] — 신용평가 문서의 인용 추천을 일반적인 해석가능한 지역 인용 추천과 다른 접근법으로 처리한다
