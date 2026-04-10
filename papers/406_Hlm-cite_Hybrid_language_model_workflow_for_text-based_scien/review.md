---
title: "406_Hlm-cite_Hybrid_language_model_workflow_for_text-based_scien"
authors:
  - "Jingyang Fan"
  - "Qianyue Hao"
  - "Yong Li"
  - "Fengli Xu"
  - "Jian Yuan"
date: "2024"
doi: "N/A"
arxiv: ""
score: 4.5
essence: "본 논문은 과학 논문의 인용 예측 문제를 단순한 이진 분류에서 벗어나 **핵심 인용(core citations)**을 표면적 인용 및 비인용과 구별하는 다단계 분류 문제로 재정의하고, 임베딩 모델과 생성형 LLM을 결합한 하이브리드 워크플로우(HLM-Cite)를 제안한다."
tags:
  - "cat/Academic_Peer_Review_Automation"
  - "sub/Citation_Dataset_Analysis"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Fan et al._2024_Hlm-cite Hybrid language model workflow for text-based scientific citation prediction.pdf"
---

# HLM-Cite: Hybrid Language Model Workflow for Text-based Scientific Citation Prediction

> **저자**: Jingyang Fan, Qianyue Hao, Yong Li, Fengli Xu, Jian Yuan | **날짜**: 2024 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)
*Figure 1: (a) 핵심 인용(Core Citation) 정의. (b)(c) 핵심 인용과 표면적 인용의 통계적 차이: 키워드 겹침(b)과 주요 텍스트 내 언급 빈도(c)*

본 논문은 과학 논문의 인용 예측 문제를 단순한 이진 분류에서 벗어나 **핵심 인용(core citations)**을 표면적 인용 및 비인용과 구별하는 다단계 분류 문제로 재정의하고, 임베딩 모델과 생성형 LLM을 결합한 하이브리드 워크플로우(HLM-Cite)를 제안한다.

## Motivation

- **Known**: 기존 인용 예측 연구는 인용 관계를 단순히 이진 분류(인용/비인용)로 처리하며, 인용 네트워크의 간선 정보만을 활용해 논문 간의 논리적 관계를 충분히 파악하지 못함.

- **Gap**: 한 논문이 여러 논문을 인용할 때, 그 역할이 **기초 지식(foundational knowledge)**부터 **표면적 언급(superficial context)**까지 크게 다르다는 중요한 점이 미처 다루어지지 않음. 또한 LLM의 맥락 길이 제한(context length)으로 인해 수백만 개의 후보 논문을 동시에 처리할 수 없음.

- **Why**: 
  - 12M개 논문 분석 결과, 핵심 인용이 표면적 인용보다 쿼리 논문과 더 높은 키워드 중복도(Figure 1b)와 주요 텍스트 내 언급 빈도(Figure 1c)를 보임
  - 미래의 인용 논문들이 현재 논문의 핵심 인용을 함께 인용하는 경향이 있음

- **Approach**: 
  1. 인용 네트워크의 지역적 구조(future citations)를 이용해 핵심 인용을 정의
  2. 임베딩 모델(retrieval)과 생성형 LLM(reasoning)을 순차적으로 결합해 대규모 후보 집합 처리

## Achievement

![Figure 2](figures/fig2.webp)
*Figure 2: 제안된 HLM-Cite 워크플로우의 구조. (a) 전체 개요: 검색 모듈과 LLM 에이전트 순위 결정 모듈의 두 단계. (b) 검색 모듈의 커리큘럼 파인튜닝: 분류(Stage 1)에서 순위 결정(Stage 2) 태스크로 전이. (c) LLM 에이전트 순위 결정: Guider, Analyzer, Decider의 세 역할 분담*

1. **핵심 인용 개념 도입**: 
   - 수학적 정의: $\tilde{S}_q = \{s_q \in S_q | \exists p \in F_q, q \in S_p, s_q \in S_p\}$ (미래 인용 논문과의 공통 인용 기반)
   - 기존의 단순 이진 분류를 세 가지 카테고리(핵심/표면적/비인용) 구분 문제로 확장
   - 19개 과학 분야 13개 지표에서 통계적 유의성 확인

2. **확장된 방법론 개발**:
   - 100K 규모의 후보 집합 처리 가능 (기존 방법 대비 수천 배 향상)
   - SOTA 대비 **17.6% 성능 개선** (정확도 메트릭)
   - 크로스필드(cross-field) 데이터셋에서 일반화 성능 입증

## How

![Figure 3](figures/fig3.webp)
*Figure 3: LLM 에이전트 순위 결정 모듈의 사례 연구. Guider의 원샷 학습 예시(2→3→1의 정렬)를 통해 Analyzer와 Decider가 논리적 관계를 추론하고 순위를 결정*

### 2단계 하이브리드 워크플로우

**Stage 1: 검색 모듈 (Embedding-based Retrieval)**
- 사전학습된 텍스트 임베딩 모델을 커리큘럼 파인튜닝으로 적응
  - Stage 1 (분류): CrossEntropy Loss로 핵심/표면적 인용 이진 분류 학습
  - Stage 2 (순위 결정): NeuralNDCG Loss로 순위 학습으로 전이 (ranking-aware)
  - 제목+초록만 사용하여 768차원 임베딩 생성
- 대규모 후보 집합(Cq)에서 고확률 핵심 인용 추출 (반환 집합 Rq)

**Stage 2: LLM 에이전트 순위 결정 모듈 (Generative LLM-based Reasoning)**
- 3-역할 에이전트 아키텍처:
  - **Guider**: 원샷(one-shot) 학습 예시 제공, 쿼리 논문이 왜 특정 논문을 인용하는지 설명
  - **Analyzer**: 각 검색된 후보 논문에 대해 쿼리 논문과의 논리적 관계 분석
  - **Decider**: 최종 순위 결정
- 암시적 논리 관계를 명시적 추론으로 전환

### 주요 설계 특징

- **텍스트 기반 예측**: 훈련/테스트 시 인용 네트워크는 그라운드 트루스 구축에만 사용, 네트워크 특성은 제외 → 미발표 원고에 적용 가능
- **커리큘럼 학습**: 분류에서 순위 결정으로의 자연스러운 전이
- **확장성**: 두 단계의 분리로 검색 단계는 신속하게, 순위 단계는 정교하게 처리

## Originality

- **개념적 기여**: 
  - "핵심 인용(core citation)" 개념의 수학적 정의 (미래 인용 논문과의 공통 인용 패턴 활용)
  - 인용 예측을 단순 이진 분류에서 3-class 문제로 재정의
  
- **방법론적 기여**:
  - 하이브리드 모델 결합 (임베딩 + 생성형 LLM)으로 context length 제약 우회
  - 검색-순위 결정의 cascade 구조로 대규모 확장성 확보
  - LLM 에이전트의 구조화된 워크플로우 (3가지 역할 분리)
  
- **평가 기여**:
  - 19개 과학 분야, 100K 규모 후보 집합으로의 확장 가능성 입증
  - 기존 방법 대비 명확한 성능 향상 (17.6%)

## Limitation & Further Study

- **제한점**:
  1. **그라운드 트루스 의존성**: 핵심 인용 정의가 미래 인용 논문의 존재에 의존하여, 최신 혹은 신흥 분야의 논문에는 적용 어려움
  2. **LLM 비용**: 생성형 LLM 기반 순위 결정 단계의 계산 비용 및 추론 속도가 실시간 적용에서 병목이 될 수 있음
  3. **원샷 학습의 제한**: 단일 예시만 제공하므로, 분야별·주제별 특성을 충분히 반영하지 못할 가능성
  4. **텍스트 기반만 사용**: 인용 네트워크의 풍부한 구조적 정보(메타데이터, 저자, 기관)를 활용하지 않음

- **후속 연구 방향**:
  1. 다중 샷(multi-shot) 또는 동적 프롬프팅으로 분야별 특화 성능 향상
  2. 캐싱/배치 처리로 LLM 추론 효율성 개선
  3. 신흥 분야 논문에 대한 별도의 평가 메커니즘 개발
  4. 임베딩 모델과 LLM의 end-to-end 학습 탐색

## Evaluation

- **Novelty (4.5/5)**: 핵심 인용 개념과 수학적 정의는 신선하며, 하이브리드 모델 결합도 새로우나, 임베딩+LLM 결합 자체는 비교적 표준적 접근
  
- **Technical Soundness (4/5)**: 커리큘럼 파인튜닝, NeuralNDCG Loss 적용, LLM 에이전트 구조가 기술적으로 타당하나, 핵심 인용 정의의 순환성(future citations 필요)과 원샷 학습의 효과성 검증이 다소 약함
  
- **Significance (4.5/5)**: 100K 규모 확장성, 17.6% 성능 향상, 19개 분야 적용은 실무적 의미가 크나, 인용 예측의 절대적 난제(의미론적 관계 파악)를 완전히 해결하진 못함
  
- **Clarity (4/5)**: 전체 구조와 동기가 명확하고 Figure 2, 3이 잘 설명되나, 커리큘럼 파인튜닝의 구체적 하이퍼파라미터와 LLM 프롬프트 엔지니어링 세부사항이 부족
  
- **Overall (4.5/5)**

---

**총평**: 본 논문은 인용 예측 문제를 개념적으로 재정의하고 하이브리드 모델을 통해 실질적인 확장성을 달성한 견실한 연구이다. 특히 100K 후보 집합 처리와 17.6% 성능 개선은 실무적 가치가 높으나, 핵심 인용 정의의 순환성과 LLM 기반 추론의 효율성 개선이 향후 중요한 과제로 남아있다.

## Related Papers

- 🔄 다른 접근: [[papers/150_Benchmark_for_evaluation_and_analysis_of_citation_recommenda/review]] — 인용 추천 시스템의 표준화된 평가 방법론을 제시하여 HLM-Cite의 성능 평가에 활용할 수 있다.
- 🔗 후속 연구: [[papers/273_Directed_criteria_citation_recommendation_and_ranking_throug/review]] — 기준 지향적 인용 추천 기법을 다루어 핵심 인용과 표면적 인용을 구별하는 HLM-Cite와 보완적이다.
- 🏛 기반 연구: [[papers/219_Citebart_Learning_to_generate_citations_for_local_citation_r/review]] — 지역적 인용 맥락에서의 인용문 생성 기법으로 HLM-Cite의 텍스트 기반 인용 예측 방법론의 기초를 제공한다.
- 🔄 다른 접근: [[papers/150_Benchmark_for_evaluation_and_analysis_of_citation_recommenda/review]] — 하이브리드 언어모델을 활용한 인용 추천 방법으로 기존 평가 기준과 비교 분석이 가능하다.
