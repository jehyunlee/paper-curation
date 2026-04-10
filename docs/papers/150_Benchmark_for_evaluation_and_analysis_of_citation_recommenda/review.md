---
title: "150_Benchmark_for_evaluation_and_analysis_of_citation_recommenda"
authors:
  - "Puja Maharjan"
date: "2024"
doi: "N/A"
arxiv: ""
score: 4.2
essence: "인용문헌 추천 시스템(citation recommendation systems)의 평가를 위한 표준화된 벤치마크를 제안하는 논문으로, 다양한 모델, 데이터셋, 평가 지표의 불일치 문제를 해결하고자 진단 데이터셋(diagnostic datasets)과 일관된 평가 메트릭을 제시한다."
tags:
  - "cat/Academic_Peer_Review_Automation"
  - "sub/Citation_Dataset_Analysis"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Liberati et al._2024_Benchmark for evaluation and analysis of citation recommendation models.pdf"
---

# Benchmark for evaluation and analysis of citation recommendation models

> **저자**: Puja Maharjan | **날짜**: 2024 | **DOI**: N/A

---

## Essence

인용문헌 추천 시스템(citation recommendation systems)의 평가를 위한 표준화된 벤치마크를 제안하는 논문으로, 다양한 모델, 데이터셋, 평가 지표의 불일치 문제를 해결하고자 진단 데이터셋(diagnostic datasets)과 일관된 평가 메트릭을 제시한다.

## Motivation

- **Known**: 인용문헌 추천 시스템은 광범위한 연구 관심을 받고 있으며, 저자가 작성한 텍스트를 기반으로 관련 참고문헌을 자동으로 제안하는 시스템이 다수 개발되어 있다. 기존 접근법은 전체 논문 콘텐츠에 중점을 두는 글로벌(global) 방식과 인용 맥락에 집중하는 로컬(local) 방식으로 나뉜다.

- **Gap**: 각 연구에서 사용하는 데이터셋(메타데이터, 인용 맥락, 전체 텍스트 등), 모델 구조(context 길이 100-2048 토큰, 양방향/단방향 등), 평가 메트릭이 상이하여 서로 다른 인용 추천 방법을 일관성 있게 평가하고 비교하기 어렵다.

- **Why**: 인용 패턴은 학문 분야별로 상이하고, 인용의 위치, 빈도, 논문의 나이가 모델 성능에 미치는 영향을 체계적으로 분석할 필요가 있다. GLUE, SuperGLUE, GEM 같은 NLP 벤치마크의 성공 사례를 보면, 표준화된 벤치마크의 중요성이 입증된다.

- **Approach**: S2ORC 및 S2AG 데이터셋을 기반으로 필드(fields), 연도(years), 인용 개수(citation counts), 맥락 길이(context length), 인용 위치(citation location), 맥락 유형(context type), 품사(POS), 저자원(low-resource) 등 8가지 차원별 진단 데이터셋을 구성한다.

## Achievement

1. **표준화된 진단 데이터셋 개발**: S2ORC 데이터셋으로부터 의학, 물리학, 생물학, 컴퓨터과학 등 19개 분야를 포함하는 다양한 진단 데이터셋을 생성. 각 문장마다 정확히 하나의 인용만 포함하고 적절한 길이의 문장을 선별하여 일관성 있는 구조 유지.

2. **다차원 성능 분석 프레임워크**: Recall과 Mean Reciprocal Rank (MRR) 메트릭을 활용하여, BM25를 기준 모델(baseline)로 설정하고 다양한 인용 맥락 특성별로 모델 성능을 측정할 수 있는 체계 구축.

3. **공개 리소스 제공**: 소스 코드, 진단 데이터셋, 벤치마크 모델을 GitHub 및 Google Drive를 통해 공개하여 연구 커뮤니티의 접근성 향상.

## How

- **데이터 추출 및 전처리**: S2ORC 데이터셋에서 각 필드에 비례하는 데이터를 추출하고, 문장 길이 이상치(z-score > 3)를 제거하여 수학식/공식으로 인한 왜곡 방지.

- **Context Length 분류**: 토큰 단위로 문장을 분할하여 길이 분포를 분석하고, 평균과 표준편차를 기반으로 상한/하한을 정의하여 맥락 길이별 클래스 설정 (최대 70토큰).

- **Citation Location 분석**: 문장 내 인용의 위치(처음, 중간, 끝)가 모델 성능에 미치는 영향을 평가하기 위해 위치별 세분화된 데이터셋 구성 (Figure 1 참조).

- **다양한 차원별 필터링**: 연도별(2000-2023), 필드별, 인용 빈도별(저빈도/고빈도), 품사별(Figure 2 참조) 데이터셋을 생성하여 특정 특성이 성능에 미치는 영향 측정.

- **저자원 시나리오 포함**: 데이터 부족 상황에서의 모델 성능 평가를 위한 별도의 저자원 데이터셋 구성.

## Originality

- 인용 추천 분야에서 **최초로 포괄적인 진단 벤치마크** 제안. 기존 연구들은 각각 자체 데이터셋과 평가 지표를 사용했지만, 이 연구는 표준화된 평가 프레임워크 제시.

- **8가지 다차원 진단 데이터셋**: 단순한 성능 평가를 넘어 맥락 길이, 인용 위치, 품사, 시간적 요인 등 세밀한 분석을 가능하게 하는 모델 진단 도구 개발.

- **학제간 포괄성**: 19개 학문 분야를 포함하여 분야별 인용 패턴의 이질성을 반영한 벤치마크 구성.

- **재현성과 개방성**: 공개된 리소스를 통해 연구 커뮤니티가 동일한 데이터셋으로 실험할 수 있도록 보장.

## Limitation & Further Study

- **로컬 인용 추천 중심**: 논문에서는 주로 로컬 방식(맥락 기반)을 다루고 있으며, 글로벌 방식(메타데이터 기반) 평가는 부분적. 향후 두 방식을 통합한 하이브리드 모델 평가 필요.

- **모델 다양성 부족**: 현재까지 BM25를 기준 모델로만 제시했으며, LSTM, BERT, GCN 등 다양한 신경망 기반 모델들의 성능 비교 결과는 본문에서 미제시. 향후 주요 기존 모델들(Specter, Galactica 등)을 벤치마크에 포함할 필요.

- **시간적 편향(temporal bias) 분석 부족**: 논문의 나이(0-3년, 8+년 등)가 인용 선택에 미치는 영향에 대한 심층 분석 필요.

- **저자 편향 및 공정성**: 저명 저자, 기관의 편향이 인용 추천 성능에 미치는 영향에 대한 분석 부재. 공정성(fairness) 메트릭 추가 개발 필요.

- **도메인 적응(domain adaptation)**: 특정 분야에서 학습한 모델이 다른 분야에서 얼마나 잘 전이되는지에 대한 평가 프레임워크 개발 필요.


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.2/5

**총평**: 인용 추천 시스템 평가의 표준화라는 절실한 문제를 해결하고, 다층적 진단 데이터셋을 제시한 점에서 학술 가치가 높다. 다만, 다양한 신경망 모델에 대한 벤치마크 결과 제시와 공정성·저자원 시나리오에 대한 더 심층적 분석이 보강되면 더욱 영향력 있는 연구가 될 것으로 예상된다.

## Related Papers

- 🔄 다른 접근: [[papers/406_Hlm-cite_Hybrid_language_model_workflow_for_text-based_scien/review]] — 하이브리드 언어모델을 활용한 인용 추천 방법으로 기존 평가 기준과 비교 분석이 가능하다.
- 🔗 후속 연구: [[papers/273_Directed_criteria_citation_recommendation_and_ranking_throug/review]] — 기준 지향적 인용 추천과 순위 매기기 기법으로 표준화된 평가 메트릭의 실제 적용을 보여준다.
- 🏛 기반 연구: [[papers/434_Interesting_Scientific_Idea_Generation_using_Knowledge_Graph/review]] — 지식 그래프를 활용한 과학적 아이디어 생성으로 인용 추천 시스템의 이론적 배경을 제공한다.
- 🔄 다른 접근: [[papers/406_Hlm-cite_Hybrid_language_model_workflow_for_text-based_scien/review]] — 인용 추천 시스템의 표준화된 평가 방법론을 제시하여 HLM-Cite의 성능 평가에 활용할 수 있다.
- 🧪 응용 사례: [[papers/803_The_open_review-based_orb_dataset_Towards_automatic_assessme/review]] — 인용 추천 평가 벤치마크가 ORB 데이터셋의 NLP 기반 논문 평가에 적용된다.
- 🔄 다른 접근: [[papers/420_Ilciter_Evidence-grounded_interpretable_local_citation_recom/review]] — 인용 추천 평가에서 해석가능성 중심 접근법과 전통적인 벤치마킹 방식의 서로 다른 관점을 제시합니다.
