# Modeling Changing Scientific Concepts with Complex Networks: A Case Study on the Chemical Revolution

> **저자**: Sofia Aguilar-Valdez, Stefania Degaetano-Ortlieb | **날짜**: 2026 (arXiv: 2603.17594v1) | **arXiv**: https://arxiv.org/abs/2603.17594

---

## 핵심 요약
본 논문은 LLM 기반 문맥 임베딩의 해석 가능성(interpretability) 한계를 극복하기 위해, 토픽 모델링 기반 복잡 네트워크(complex networks)로 과학적 개념의 변화 궤적을 모델링하는 프레임워크를 제안한다. Royal Society Corpus를 활용하여 화학혁명(Chemical Revolution) 시기 phlogiston 이론에서 oxygen 이론으로의 개념 전환을 사례 연구로 분석하며, onomasiological change(동일 개념에 대한 언어적 표현의 변화)가 높은 entropy 및 위상적 밀도(topological density) 증가와 연관됨을 보여준다.

## 연구 배경 및 동기
언어 변화와 개념 변화를 추적하는 기존 NLP 방법(diachronic word embeddings, LLM 기반 의미 변화 탐지)은 해석 가능성이 낮고, 시간 정보를 명시적으로 다루지 못하며, 역사 데이터에서의 편향 증폭(bias augmentation) 위험이 있다. 과학혁명 시기의 개념 전환은 언어 사용의 변화가 보다 넓은 인식론적 전환(epistemic transition)을 반영하므로, 해석 가능하고 시간 인식적인(time-aware) 모델링 프레임워크가 필요하다.

## 방법론
- **데이터**: Royal Society Corpus(RSC)에서 1750-1800년 사이 출판물 중 oxygen 관련 용어를 포함하는 2,337개 문서 필터링. 전처리(소문자화, 불용어 제거, 명사/형용사 필터링, 레마타이제이션) 수행.
- **토픽 모델링**: LDA(Latent Dirichlet Allocation)로 최적 토픽 수 6개 결정(perplexity, coherence 기반). LDAvis로 토픽 레이블 생성. Cumulative(누적)과 non-cumulative(비누적) 두 가지 샘플링 전략 비교.
- **네트워크 구축**: 문서를 노드, Jensen-Shannon distance 기반 문서-토픽 분포 유사도를 엣지로 하여 인접행렬 구성. Percolation threshold 최적화로 이진화.
- **클러스터링**: Hierarchical Agglomerative Clustering(HAC)과 Louvain 알고리즘으로 커뮤니티 탐지. UMAP으로 시각화.
- **평가 지표**: Jensen-Shannon distance(토픽 클러스터 간 차이), entropy(토픽 다양성), 네트워크 메트릭(노드 수, 엣지 밀도, 커뮤니티 수, modularity, percolation threshold).

## 주요 결과
- Non-cumulative 샘플링에서 1780년대의 핵심 토픽 클러스터가 'air' 중심에서 1800년대 'acid' 중심으로 전환되며, oxygen이 주변부(peripheral) 용어로 등장 -- onomasiological change 확인.
- Phlogiston과 calx가 주변부에서 사라지는 과정이 네트워크 구조에 반영됨.
- Non-cumulative 전략에서 entropy는 1774년 oxygen 발견 전 감소 후 상승하는 패턴을 보여, phlogiston 진영의 저항과 이후 Lavoisier 체계의 다양성 증가를 반영.
- 시간적 그래프에서 엣지 밀도 2배 이상 증가(30,037 -> 62,639), 커뮤니티 수 감소(5 -> 3), modularity 하락(0.39 -> 0.19), percolation threshold 상승 -- 혼합된 커뮤니티 구조로의 전환과 연결성 비용(connectivity effort) 증가를 시사.

## 독창성 및 기여
- **Conceptual structure shift detection task**라는 새로운 과제를 정의하고, 프로토타입 의미론(prototype semantics) 이론에 기반한 네트워크 프레임워크를 제시.
- LLM 기반 방법의 해석 불가능성 문제를 토픽 기반 네트워크로 우회하면서도, 개념의 core-periphery 구조와 시간적 변화를 추적할 수 있는 해석 가능한 도구 제공.
- 과학사(history of science)의 질적 분석 결과(Thagard, Chang)와 정량적 네트워크 분석 결과의 정합성을 보여줌.

## 한계 및 향후 연구
- **저자 언급 한계**: (1) 영어 텍스트만 대상으로 하여 Lavoisier의 프랑스어 저작 미포함. (2) 토픽-단어 분포에서 core/peripheral 용어를 도출하여 문서 임베딩 기하학 간과 가능. (3) 희소 주변부 용어의 표현 부족. (4) 비방향 그래프로 의미 방향성 미반영.
- **추가 지적**: 사례 연구가 화학혁명 단일 사례에 국한되어 프레임워크의 일반화 가능성이 검증되지 않았다. 토픽 수 6개의 선택이 다른 시대나 분야에도 적용 가능한지 불분명하다. 또한 RSC의 시대적 특성(18세기 과학 영어)이 현대 과학 텍스트에 대한 적용 가능성을 제한할 수 있다. 네트워크 메트릭의 변화와 실제 과학적 패러다임 전환 간의 인과적 관계를 주장하기에는 단일 사례로 증거가 부족하다.

## 평가
| 항목 | 점수 (1-5) |
|------|-----------|
| Novelty | 4 |
| Technical Soundness | 3 |
| Significance | 3 |
| Clarity | 4 |
| Overall | 3 |

**총평**: 과학적 개념 변화를 해석 가능한 네트워크로 모델링하는 독창적 접근이나, 단일 사례 연구에 머물러 프레임워크의 일반화 가능성이 입증되지 않았으며, 방법론적 선택(토픽 수, 샘플링 전략)에 대한 민감도 분석이 부족하다.
