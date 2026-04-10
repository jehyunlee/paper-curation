---
title: "963_Forecasting_the_future_of_artificial_intelligence_with_machi"
authors:
  - "Mario Krenn"
  - "Lorenzo Buffoni"
  - "Bruno Coutinho"
  - "Sagi Eppel"
  - "Jacob Gates Foster"
date: "2023.10"
doi: "10.1038/s42256-023-00735-0"
arxiv: ""
score: 4.0
essence: "143,000개의 AI 논문으로부터 64,000개 개념노드의 의미 네트워크를 구축하고, 머신러닝 기반 링크 예측을 통해 미래의 AI 연구 방향을 예측하는 Science4Cast 벤치마크를 제시한다."
tags:
  - "cat/Scientific_Information_Systems"
  - "sub/AI-Driven_Research_Discovery"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Krenn et al._2023_Forecasting the future of artificial intelligence with machine learning-based link prediction in an.pdf"
---

# Forecasting the future of artificial intelligence with machine learning-based link prediction in an exponentially growing knowledge network

> **저자**: Mario Krenn, Lorenzo Buffoni, Bruno Coutinho, Sagi Eppel, Jacob Gates Foster, Andrew Gritsevskiy, Harlin Lee, Yichao Lu, João P. Moutinho, Nima Sanjabi, Rishi Sonthalia, Ngoc Mai Tran, Francisco Valente, Yangxinyu Xie, Rose Yu, Michael Kopp | **날짜**: 2023-10-16 | **DOI**: [10.1038/s42256-023-00735-0](https://doi.org/10.1038/s42256-023-00735-0)

---

## Essence

![Figure 2](figures/fig2.webp)

*Fig. 2 | From arXiv to Science4Cast. Utilizing 143,000 AI and ML papers on*

143,000개의 AI 논문으로부터 64,000개 개념노드의 의미 네트워크를 구축하고, 머신러닝 기반 링크 예측을 통해 미래의 AI 연구 방향을 예측하는 Science4Cast 벤치마크를 제시한다.

## Motivation

- **Known**: 과학 문헌에서 개념 공출현(co-occurrence)을 이용한 의미 네트워크 구축은 기존에 생화학, 양자물리 분야에서 수행되었으며, 링크 예측(link prediction)은 네트워크 과학에서 고전적 통계 방법과 머신러닝 기법으로 다루어져 왔다.
- **Gap**: AI 분야의 지수적 논문 증가로 연구자들이 전체 진전을 추적하기 어려우며, 10배 이상 큰 규모의 의미 네트워크에서 향상된 링크 예측 방법이 부족하다.
- **Why**: 미래 연구 방향을 정확히 예측할 수 있다면 개인화된 연구 제안 도구 개발이 가능하고, 이는 과학 진전을 가속화하며 학제간 협력 기회를 발굴할 수 있다.
- **Approach**: 1994-2020년 arXiv AI/ML 논문 143,000개에서 RAKE와 NLP를 이용해 64,000개 개념을 추출하고, 시간 스탬프가 있는 의미 네트워크를 구축한 후, 10가지 다양한 통계 및 머신러닝 방법으로 미래 링크 예측을 수행한다.

## Achievement

![Figure 3](figures/fig3.webp)

*Fig. 3 | Heavy-tail distribution in node degrees due to hubs. Nodes with the*

- **Science4Cast 벤치마크 구축**: 143,000개 논문으로부터 64,000개 노드와 1,789만 개 간선을 가진 동적 의미 네트워크 구축
- **예측 성능**: 10가지 다양한 방법으로 미래 AI 연구 주제 조합을 높은 정확도로 예측
- **핵심 발견**: 수작업으로 정성한 네트워크 특성(hand-crafted features)을 사용한 방법이 엔드-투-엔드 AI 접근보다 우수한 성능 달성
- **확장성**: CSO 같은 고정 온톨로지 대신 자동 추출 방식을 사용하여 모든 과학 분야에 적용 가능한 확장성 제시
- **공개**: 모든 방법을 GitHub에 공개하여 재현성과 후속 연구 용이

## How

![Figure 2](figures/fig2.webp)

*Fig. 2 | From arXiv to Science4Cast. Utilizing 143,000 AI and ML papers on*

- ArXiv의 cs.AI, cs.LG, cs.NE, stat.ML 카테고리에서 1994-2020년 논문 수집
- 논문 제목과 초록으로부터 RAKE(Rapid Automatic Keyword Extraction) 알고리즘으로 개념 추출
- NLP 기술과 커스텀 정규화 방법으로 개념 표준화
- 개념을 노드로, 같은 논문에 공출현하는 개념쌍을 간선으로 하는 의미 네트워크 구성
- 출판 날짜 기반 타임 스탬프 추가하여 시간 진화 네트워크 형성
- 네트워크 이론 기반 특성(motif, 중심성 등)과 머신러닝 특성 학습 방법 적용
- 과거 데이터로 훈련하고 미래 기간의 새로운 링크 예측 성능 평가

## Originality

- 기존 양자물리(6,000개 개념) 대비 10배 이상 큰 규모(64,000개)의 AI 의미 네트워크 구축
- 통계 방법부터 딥러닝까지 10가지 다양한 방법을 체계적으로 비교 분석
- 수작업 특성 기반 방법의 우월성을 실증적으로 입증하여 순수 ML 접근의 개선 가능성 제시
- 고정 온톨로지 대신 자동 추출 방식으로 도메인 독립적 확장성 달성
- 개인화된 과학 연구 제안 도구의 기초 구축

## Limitation & Further Study

- 개념 추출이 논문 제목과 초록에만 제한되어 전문 지식 깊이 부족 가능
- 대규모 언어모델(LLM)의 추론 능력이 아직 미흡하여 상세한 관계 추출 미실시
- 학위논문, 학술대회 자료, 출판 전 원고 등 arXiv 외 자료 미포함
- 네트워크 차수 분포가 power law, truncated power law, lognormal 등 명확하지 않음
- 예측 정확도가 높지만 실제 과학적 타당성과 영향력 검증 필요
- **후속연구**: CSO 같은 고품질 온톨로지와의 병합 방안 탐색, LLM의 추론 능력 향상을 통한 심층 관계 추출, 다른 과학 분야로의 적용 확대, 예측된 아이디어의 실제 과학적 가치 평가 메커니즘 개발

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 이 논문은 지수적으로 증가하는 AI 문헌에서 의미 있는 연구 방향을 예측하기 위해 대규모 의미 네트워크와 링크 예측 기법을 결합한 혁신적 접근을 제시한다. 수작업 특성이 자동 학습을 능가한다는 발견은 향후 더 나은 순수 ML 방법 개발의 가능성을 시사하며, 공개 벤치마크와 방법 제공으로 학계에 상당한 기여할 것으로 기대된다.

## Related Papers

- 🔄 다른 접근: [[papers/998_Predicting_Scientific_Breakthroughs_Based_on_Structural_Dyna/review]] — AI 연구 예측에서 의미 네트워크 대신 구조적 역학을 기반으로 과학적 돌파를 예측하는 다른 접근법을 제시한다.
- 🏛 기반 연구: [[papers/1076_Predicting_research_trends_with_semantic_and_neural_networks/review]] — 의미 네트워크와 신경망을 활용한 연구 트렌드 예측의 기본 방법론을 AI 분야에 특화하여 적용한다.
- 🧪 응용 사례: [[papers/1064_Data-driven_predictions_in_the_science_of_science/review]] — AI 분야의 기계학습 예측을 통해 과학의 과학에서 데이터 기반 예측의 구체적 적용 사례와 한계를 보여준다.
