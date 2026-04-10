---
title: "1109_A_comprehensive_large-scale_biomedical_knowledge_graph_for_A"
authors:
  - "Yuan Zhang"
  - "Xin Sui"
  - "Feng Pan"
  - "Kaixian Yu"
  - "Keqiao Li"
date: "2025.04"
doi: "10.1038/s42256-025-01014-w"
arxiv: ""
score: 4.0
essence: "PubMed의 모든 초록을 이용한 대규모 생의학 지식그래프(iKraph)를 구축하고, 확률론적 의미 추론(PSR)을 통해 간접 인과관계를 식별하여 약물 재위치 지정(drug repurposing)에 적용했다."
tags:
  - "cat/Scientific_Information_Systems"
  - "sub/Knowledge_Graphs_and_Semantic_Mapping"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhang et al._2025_A comprehensive large-scale biomedical knowledge graph for AI-powered data-driven biomedical researc.pdf"
---

# A comprehensive large-scale biomedical knowledge graph for AI-powered data-driven biomedical research

> **저자**: Yuan Zhang, Xin Sui, Feng Pan, Kaixian Yu, Keqiao Li, Shubo Tian, Arslan Erdengasileng, Qing Han, Wanjing Wang, Jianan Wang, Jian Wang, Donghu Sun, Henry Chung, Jun Zhou, Eric Zhou, Ben Lee, Peili Zhang, Xing Qiu, Tingting Zhao, Jinfeng Zhang | **날짜**: 2025-04 | **DOI**: [10.1038/s42256-025-01014-w](https://doi.org/10.1038/s42256-025-01014-w)

---

## Essence

![Figure 2](figures/fig2.webp)

*Fig. 2 | Drug repurposing for COVID-19. a, The number of repurposed drugs,*

PubMed의 모든 초록을 이용한 대규모 생의학 지식그래프(iKraph)를 구축하고, 확률론적 의미 추론(PSR)을 통해 간접 인과관계를 식별하여 약물 재위치 지정(drug repurposing)에 적용했다.

## Motivation

- **Known**: 지식그래프는 이기종 데이터를 통합하여 자동화된 지식 발견을 가능하게 하지만, 비정형 과학 문헌을 지식그래프로 변환하는 것은 여전히 인간 수준의 정확도 달성이 어렵다.
- **Gap**: 기존 약물 재위치 지정 연구는 특정 질병 또는 약물의 모든 치료 연관성을 포괄적으로 평가하기 어려워 엄격한 성능 평가가 불가능했다.
- **Why**: 급증하는 과학 문헌과 데이터를 효율적으로 통합하고 자동화된 가설 생성을 통해 신약 개발 비용을 절감하고 새로운 치료 기회를 발굴할 수 있기 때문이다.
- **Approach**: LitCoin NLP 챌린지 우승 파이프라인을 사용하여 34백만 건의 PubMed 초록에서 고정확도로 엔티티와 관계를 추출하고, 40개 공개 데이터베이스와 고처리량 유전체학 데이터를 통합하여 포괄적인 지식그래프를 구축했다.

## Achievement

![Figure 2](figures/fig2.webp)

*Fig. 2 | Drug repurposing for COVID-19. a, The number of repurposed drugs,*

- **대규모 생의학 지식그래프 구축**: 3,468만 건 PubMed 초록에서 1,068만 개 고유 엔티티와 3,075만 개 고유 관계를 추출하여 인간 주석 수준의 정확도 달성
- **COVID-19 약물 재위치 지정 검증**: 처음 4개월(2020년 3월~6월)에 약 1,200개 후보 약물 식별, 처음 2개월에 발견한 약 1/3이 임상시험 또는 PubMed 출판으로 입증됨
- **확률론적 의미 추론(PSR) 개발**: 해석 가능한 방법으로 직접 연결되지 않은 엔티티 간 간접 인과관계를 식별
- **포괄적 성능 평가 실현**: 전체 PubMed 문헌 기반으로 리콜(recall)과 관찰된 양성률(OPR) 측정 가능하게 함
- **클라우드 기반 플랫폼 개발**: 학술 사용자를 위한 웹 인터페이스(https://biokde.insilicom.com) 제공

## How

![Figure 5](figures/fig5.webp)

*Fig. 5 | The overview of our drug repurposing strategy and validation*

- 명명 엔티티 인식(NER)과 관계 추출을 위해 BERT 기반 미세 조정 모델 사용
- LitCoin NLP 챌린지 데이터셋의 500개 PubMed 초록으로 훈련된 파이프라인 활용
- 엔티티 정규화(entity normalization) 과정 통합
- 관계의 방향성을 예측하도록 모델 훈련하여 인과 지식그래프 구축
- 40개 공개 데이터베이스(STRING, DrugBank 등)와 고처리량 유전체학 데이터 통합
- COVID-19, 낭포성 섬유증 등에 대해 회고적 실시간 약물 재위치 지정 실험 수행
- 50개 무작위 선택 PubMed 초록(1,583개 엔티티 쌍) 샘플로 정확도 검증

## Originality

- LitCoin NLP 챌린지 우승 파이프라인을 전체 PubMed 초록(34백만 건)에 최초로 적용하여 대규모 생의학 지식그래프 구축
- 관계 방향성 주석을 추가하여 인과 지식그래프 생성 - 기존 LitCoin 데이터셋에 없던 혁신적 확장
- 확률론적 의미 추론(PSR)이라는 새로운 해석 가능한 간접 인과관계 추론 방법 제시
- 전체 PubMed 문헌 기반 리콜과 관찰된 양성률(OPR) 측정으로 엄격한 성능 평가 방법론 제시
- 약물 재위치 지정의 실시간 회고적 검증으로 초기 발견의 1/3이 나중에 임상시험으로 입증됨을 보여줌

## Limitation & Further Study

- **LLM의 특화 작업 성능 한계**: GPT-4와 같은 대규모 언어모델이 장꼬리 엔티티(long-tail entities) 처리, 방향성 함의(directional entailments), 패러프레이즈된 정보 검색에서 미세 조정 모델에 뒤짐
- **데이터 소스의 시간적 한계**: 2023년 5월 이전 PubMed 초록만 포함하여 최신 연구 내용 누락 가능성
- **고처리량 데이터 통합의 완전성 미확인**: 유전체학 데이터 통합이 모든 관련 생물학적 관계를 포함하는지 체계적 검증 필요
- **약물 재위치 지정 성공률의 조정**: 1/3 임상 입증 비율이 최종 임상 성공으로 이어지는 정도 추적 필요
- **후속 연구**: (1) 동적 업데이트 파이프라인 개발로 신규 PubMed 초록 자동 통합, (2) LLM과 미세 조정 모델 하이브리드 접근법 개발, (3) 다른 질병과 약물에 대한 대규모 임상 검증 수행

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 이 연구는 LitCoin 우승 파이프라인을 전체 PubMed 데이터에 적용하여 인간 수준의 정확도로 대규모 생의학 지식그래프를 최초로 구축하고, 확률론적 의미 추론으로 약물 재위치 지정에 성공한 중대한 기여다. 특히 전체 문헌 기반 엄격한 성능 평가가 가능해졌다는 점과 COVID-19 약물 발굴의 1/3이 임상 입증된 점이 실무적 가치를 입증한다.

## Related Papers

- 🔄 다른 접근: [[papers/1111_A_Strategic_Guide_to_White_Space_Analysis_for_Pharmaceutical/review]] — 생의학 분야 대신 제약 R&D에서 특허와 임상 데이터를 결합한 다른 형태의 지식그래프 접근법을 제시한다.
- 🔗 후속 연구: [[papers/1073_MOLIERE_Automatic_Biomedical_Hypothesis_Generation_System/review]] — 생의학 지식그래프를 활용한 가설 생성 시스템으로 약물 재위치 지정의 자동화된 접근법을 확장한다.
- 🔄 다른 접근: [[papers/1073_MOLIERE_Automatic_Biomedical_Hypothesis_Generation_System/review]] — 생의학 분야에서 지식 그래프를 활용한 자동 가설 생성의 서로 다른 구현 방식과 적용 범위를 보여준다.
- 🔗 후속 연구: [[papers/978_Introducing_the_open_biomedical_map_of_science/review]] — PubMed 기반의 생의학 과학 지도를 AI 기반 drug discovery를 위한 포괄적 지식그래프로 확장 발전시킨다.
- 🔄 다른 접근: [[papers/1112_CS-KG_20_A_Large-scale_Knowledge_Graph_of_Computer_Science/review]] — 컴퓨터과학 특화 지식그래프 대신 생의학 분야의 포괄적 지식그래프를 제안한다.
