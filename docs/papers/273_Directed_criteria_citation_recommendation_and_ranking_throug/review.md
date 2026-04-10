---
title: "273_Directed_criteria_citation_recommendation_and_ranking_throug"
authors:
  - "William Watson"
  - "Lawrence Yong"
date: "2024"
doi: "10.48550/arXiv.2403.18855"
arxiv: ""
score: 3.5
essence: "신용평가기관의 평가 기준 문서들 사이의 인용 관계를 그래프 링크 예측(link prediction) 문제로 모델링하여, 트랜스포머 기반 그래프 신경망으로 누락된 인용을 자동 추천하고 순위를 매기는 방법론을 제시한다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Citation_Context_Generation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Watson and Yong_2024_Directed criteria citation recommendation and ranking through link prediction.pdf"
---

# Directed criteria citation recommendation and ranking through link prediction

> **저자**: William Watson, Lawrence Yong | **날짜**: 2024 | **DOI**: [10.48550/arXiv.2403.18855](https://doi.org/10.48550/arXiv.2403.18855)

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: 학습된 잔차(Learned Residual)를 갖춘 증강 트랜스포머 아키텍처*

신용평가기관의 평가 기준 문서들 사이의 인용 관계를 그래프 링크 예측(link prediction) 문제로 모델링하여, 트랜스포머 기반 그래프 신경망으로 누락된 인용을 자동 추천하고 순위를 매기는 방법론을 제시한다.

## Motivation

- **Known**: 트랜스포머 기반 그래프 신경망(Graph Attention Network)이 여러 그래프 관련 작업에서 우수한 성능을 보임
- **Gap**: 신용평가기관의 평가 기준 문서 간 인용 관계의 일관성 유지를 위해 누락되거나 암묵적인 인용을 자동으로 발굴할 수 있는 체계적인 방법이 부재함
- **Why**: 신용평가 과정의 정확성을 위해 기준 문서들 간 인용 그래프를 최신 상태로 유지하는 것이 매우 중요함
- **Approach**: 인용 네트워크의 문서 노드를 트랜스포머 기반 그래프 임베딩으로 인코딩한 후, 링크 예측을 통해 새 문서의 관련 인용을 추천하고 순위 지정

## Achievement

![Figure 2](figures/fig2.webp)
*그림 2: 주제 영역별로 색칠된 임베딩(t-SNE 투영)*

1. **성능 향상**: TF-IDF 기준 대비 MAP 10.5% → 25.4%, MAR 34.6% → 65.3% (k=20 기준) 달성
2. **그래프 구조의 효과성**: 그래프 정보를 활용한 모델이 콘텐츠 기반 방법을 크게 상회하는 성능 입증
3. **임베딩 품질**: 주제 영역별 자기조직화(self-organization)를 통해 도메인 내 및 도메인 간 인용 패턴 자동 포착

## How

![Figure 3](figures/fig3.webp)
*그림 3: 주제 영역별로 정렬된 실제 교차참조 행렬*

![Figure 4](figures/fig4.webp)
*그림 4: 50% 임계값으로 설정된 예측 교차참조 행렬*

**모델 아키텍처:**
- 초기 임베딩: 300차원 정규화 TF-IDF 벡터를 64차원 밀집 벡터로 압축
- 그래프 층(Graph Layer): 2개 층 적층으로 2-홉 부분그래프 정보 캡처
- 다중헤드 어텐션: 8개 헤드 사용, ELU 활성화함수 적용
- 학습된 잔차(Learned Residual): 첫 번째 잔차 연결에 어텐션 메커니즘 적용하여 이웃 노드의 영향력 제어
- 이중선형 점수 함수(Bilinear Scoring): 비대칭 방향성 인용 행렬 생성을 위해 $f(e_i, e_j) = e_i^T W_b e_j$ 사용

**학습 설정:**
- 훈련 세트: 1,472개 노드(65.5%), 검증 세트: 260개 노드(11.6%)
- 음수 샘플링으로 희소 행렬의 불균형 문제 해결
- Adam 옵티마이저(α=0.001), 1,920 업데이트

## Originality

- 신용평가 기준 문서라는 특정 도메인에 링크 예측을 처음 적용한 실무 사례 제시
- 학습된 잔차 메커니즘을 그래프 어텐션에 결합하여 노드 자체의 정보와 그래프 구조 간 영향력 균형 제어
- 방향성 인용을 위해 이중선형 점수 함수 도입으로 대칭성 문제 해결
- 링크 예측이 인용 추천뿐 아니라 도메인 간 교차 오염(cross-pollination) 분석에도 활용 가능함을 시연

## Limitation & Further Study

- **데이터 규모 제한**: 2,247개 문서(13,959개 인용)로 상대적으로 작은 규모의 데이터셋 사용
- **평가 지표 한계**: MAP/MAR만으로는 추천의 맥락적 관련성 평가 부족; 도메인 전문가의 정성적 평가 필요
- **임계값 민감도**: 50% 임계값에서 3.5%의 매우 낮은 추천 비율로, 실무 적용 시 임계값 선택이 중요
- **후속 연구**: 비즈니스 관계(business relationships) 및 공급망 네트워크(supply chain networks)와 같은 다른 도메인으로 확대 적용

## Evaluation

- **Novelty**: 3.5/5 - 실무 도메인 응용은 신선하나 기술적 방법론은 기존 그래프 트랜스포머의 점진적 개선
- **Technical Soundness**: 3.5/5 - 구조는 타당하나 비교 대상이 TF-IDF만으로 제한적; 다른 SOTA 그래프 방법과의 비교 부재
- **Significance**: 3/5 - 특정 금융 도메인 문제 해결에 유용하나 학술적 파급력은 제한적
- **Clarity**: 4/5 - 전반적으로 명확하나 일부 설정(dropout 비율 등)의 정당성 설명 부족
- **Overall**: 3.5/5

**총평**: 신용평가 기관의 실무 문제를 그래프 신경망으로 효과적으로 해결한 응용 사례이나, 학술적 혁신성은 제한적이며 평가의 엄밀성과 비교 대상의 다양성을 강화할 필요가 있다.

## Related Papers

- 🔄 다른 접근: [[papers/420_Ilciter_Evidence-grounded_interpretable_local_citation_recom/review]] — 신용평가 문서의 인용 추천을 일반적인 해석가능한 지역 인용 추천과 다른 접근법으로 처리한다
- 🔗 후속 연구: [[papers/219_Citebart_Learning_to_generate_citations_for_local_citation_r/review]] — 지역 인용 생성을 그래프 링크 예측이라는 더 구조적 접근법으로 확장한다
- 🔗 후속 연구: [[papers/406_Hlm-cite_Hybrid_language_model_workflow_for_text-based_scien/review]] — 기준 지향적 인용 추천 기법을 다루어 핵심 인용과 표면적 인용을 구별하는 HLM-Cite와 보완적이다.
- 🔗 후속 연구: [[papers/150_Benchmark_for_evaluation_and_analysis_of_citation_recommenda/review]] — 기준 지향적 인용 추천과 순위 매기기 기법으로 표준화된 평가 메트릭의 실제 적용을 보여준다.
- 🏛 기반 연구: [[papers/1091_Scirgc_Multi-granularity_citation_recommendation_and_citatio/review]] — 방향성 기준 인용 추천 및 순위화를 통해 본 논문의 인용 네트워크 활용 방법론의 이론적 기반을 제공한다.
