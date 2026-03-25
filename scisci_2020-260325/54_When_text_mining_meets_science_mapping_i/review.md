# When text mining meets science mapping in the bibliometric analysis: A review and future opportunities

> **저자**: Haojing Chen, YP Tsang, CH Wu | **날짜**: 02/2023 | **Journal**: International Journal of Engineering Business Management | **DOI**: 10.1177/18479790231222349

---

## Essence

WoS Core Collection에서 highly cited paper 중 JCR Q1/ABDC A 이상/AJG 3* 이상 저널의 37편 bibliometric review 논문을 분석하여, science mapping의 4단계 프로세스(방법 선택 → occurrence matrix 구축 → similarity 측정 → post-hoc 분석)를 체계화하고, co-citation이 59.4%로 가장 많이 사용되는 방법임을 확인했다. 이를 바탕으로 text mining 5대 기법(information extraction, document clustering, topic modeling, text summarization, sentiment analysis)과 science mapping의 통합 가능성을 매핑하여, topic modeling/text summarization/sentiment analysis가 아직 충분히 탐구되지 않은 영역임을 제시한다.

## Motivation

- **기존 지식**: Bibliometric analysis와 science mapping(co-citation, bibliographic coupling, co-word, co-authorship)은 연구 분야의 지적 구조를 파악하는 표준 방법론으로 확립되었으며, VOSviewer, CiteSpace 등 도구가 보급됨.
- **한계/격차**: (1) Science mapping 프로세스의 내부 메커니즘(occurrence matrix → co-occurrence matrix → similarity 측정)에 대한 명확한 설명이 부족, (2) 클러스터 해석이 주관적이고 수동적, (3) text mining 기법이 science mapping 결과 해석에 체계적으로 통합되지 않음.
- **접근**: 고품질 bibliometric review 37편을 체계적으로 분석하여 현재 science mapping 실태를 파악하고, 5가지 text mining 기법을 science mapping의 각 방법론과 교차 매핑하여 미탐구 영역(연구 기회)을 식별.

## Achievement

1. **Science mapping 4단계 프레임워크 정립**: 방법 선택 → occurrence matrix(O) → co-occurrence matrix(C) → similarity 측정(association strength, cosine, inclusion, Jaccard) + 일반화된 유사도 공식 제시
2. **고품질 논문 기반 현황 조사**: 37편 분석 결과, co-citation(59.4%) > co-word(29.7%) > bibliographic coupling(16.2%) > co-authorship(13.5%) 순으로 사용 빈도 파악
3. **Post-hoc 분석 기법 5가지 정리**: data clustering, PageRank, evolution analysis, strategic graph(thematic map), network centrality(betweenness, closeness)
4. **Text mining-science mapping 통합 매핑 테이블(Table 4)**: 4개 science mapping 방법 x 5개 text mining 기법의 탐구 현황을 체계적으로 정리하여, topic modeling, text summarization, sentiment analysis가 미탐구 영역임을 식별
5. **LLM 활용 전망**: GPT/Claude 등 대규모 언어 모델의 abstractive summarization과 co-word analysis 결과의 narrative 생성 가능성을 제안

## How

- **데이터**: WoS Core Collection, "Review" AND ("bibliometric analysis" OR "bibliometrics" OR "co-citation" OR ...) 키워드 검색 → 7,404편 → Highly Cited Papers 131편 → JCR Q1 + ABDC A/A* + AJG 3*/4*/4* 기준 → 37편 선정, 19개 저널
- **방법**: 체계적 문헌조사(systematic review) 기반의 narrative synthesis. Bibliometric data 유형별 사용 빈도, science mapping 방법별 사용 빈도, post-hoc 분석 기법 분류, text mining 기법의 개념적 매핑

## Originality

- Science mapping의 수학적 메커니즘(occurrence matrix → co-occurrence matrix → similarity measures)을 통합적으로 공식화하고, 일반화된 유사도 측정 공식(equation 7)을 제시한 점
- Text mining 5대 기법과 science mapping 4대 방법의 **교차 매핑 테이블**을 통해 미탐구 연구 기회를 체계적으로 식별한 점
- LLM(GPT, Claude)을 science mapping 결과 해석에 활용하는 방향을 선제적으로 제안

## Limitation & Further Study

### 저자들이 언급한 한계
- 명시적으로 기술된 한계가 없음 (논문의 구조적 약점)

### 리뷰어 판단 아쉬운 점
- **한계 논의 부재**: 자체 연구의 한계(선정 기준의 편향성, WoS 단일 데이터베이스 의존 등)를 전혀 논의하지 않음
- **Text mining 통합의 피상성**: Text mining과 science mapping의 통합을 "가능하다"고 제안만 하고, 구체적 구현 사례나 실험적 검증이 전무
- **선정 기준의 과도한 제한**: Highly Cited Papers + 3중 저널 랭킹 기준으로 37편만 선정하여 표본이 지나치게 적고, 비즈니스/경영 분야에 편중(19개 저널 대부분이 경영/공학 저널)
- **최신 embedding 기반 방법론 누락**: BERTopic, Doc2Vec, SciBERT 등 embedding 기반 최신 접근이 text mining 개요에서 거의 다루어지지 않음
- **Sentiment analysis의 bibliometric 적용 현실성 의문**: 학술 논문의 객관적 서술 특성상 sentiment analysis의 적용 가능성이 제한적이나, 이에 대한 비판적 논의가 없음

### 후속 연구
- Text mining 기법(특히 BERTopic, LLM 기반 summarization)을 실제 bibliometric 데이터셋에 적용한 실증 연구
- Science mapping 클러스터와 topic modeling 결과의 체계적 비교 실험
- 다양한 학문 분야별 science mapping 실태 비교 연구

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 2/5 |
| Technical Soundness | 3/5 |
| Significance | 3/5 |
| Clarity | 4/5 |
| Overall | 3/5 |

**총평**: Science mapping의 수학적 프로세스를 통합적으로 정리하고 text mining과의 교차 매핑을 통해 연구 기회를 제시한 유용한 개관이나, 실증적 검증 없이 개념적 제안에 그치며 선정 기준의 과도한 제한으로 표본 대표성에 한계가 있다.
