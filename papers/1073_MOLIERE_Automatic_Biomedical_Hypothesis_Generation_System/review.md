---
title: "1073_MOLIERE_Automatic_Biomedical_Hypothesis_Generation_System"
authors:
  - "Justin Sybrandt"
  - "Michael Shtutman"
  - "Ilya Safro"
date: "2017.08"
doi: "10.1145/3097983.3098057"
arxiv: ""
score: 4.0
essence: "MEDLINE의 24.5백만 개 문서로부터 구축한 대규모 생의학 지식 네트워크를 이용하여 자동으로 숨겨진 개념 간의 연결을 발견하고 가설을 생성하는 시스템이다."
tags:
  - "cat/Scientific_Impact_and_Innovation"
  - "sub/Artificial_intelligence_and_science"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Sybrandt et al._2017_MOLIERE Automatic Biomedical Hypothesis Generation System.pdf"
---

# MOLIERE: Automatic Biomedical Hypothesis Generation System

> **저자**: Justin Sybrandt, Michael Shtutman, Ilya Safro | **날짜**: 2017-08-13 | **DOI**: [10.1145/3097983.3098057](https://doi.org/10.1145/3097983.3098057)

---

## Essence

![Figure 2](figures/fig2.webp)

*Figure 2: MOLIERE network construction pipeline.*

MEDLINE의 24.5백만 개 문서로부터 구축한 대규모 생의학 지식 네트워크를 이용하여 자동으로 숨겨진 개념 간의 연결을 발견하고 가설을 생성하는 시스템이다.

## Motivation

- **Known**: Swanson의 Arrowsmith 시스템 이후 미발견 공개 지식(undiscovered public knowledge)을 마이닝하려는 시도들이 있었으나, 대부분 제한된 도메인과 문서 집합에서만 작동했다.
- **Gap**: 기존 시스템들은 전체 MEDLINE 데이터셋을 활용하지 못했고, 제한된 어휘(restricted vocabulary)와 도메인 특화 데이터만 처리했으며, 사용자가 이해하기 쉬운 형태의 결과를 생성하지 못했다.
- **Why**: 생의학 연구자들은 급속도로 증가하는 문헌을 모두 검토할 수 없으므로, 자동화된 가설 생성 시스템은 연구 생산성을 크게 향상시키고 새로운 발견의 가능성을 높일 수 있다.
- **Approach**: MEDLINE, UMLS 메타시소러스, 의학 논문 등 이질적 데이터소스로부터 다중모달 다중관계 네트워크를 구축하고, FastText와 FLANN을 이용한 최단 경로 탐색과 LDA 기반 주제 모델링으로 가설을 생성한다.

## Achievement

![Figure 2](figures/fig2.webp)

*Figure 2: MOLIERE network construction pipeline.*

- **전체 MEDLINE 활용**: 첫 번째로 24.5백만 개 전체 MEDLINE 데이터셋을 활용한 가설 생성 시스템 구현
- **제약 없는 어휘 처리**: 도메인 특화 제한 어휘 없이 ToPMine을 통한 자동 다중단어 구문 인식으로 유연성 극대화
- **역사적 검증**: 2009년 이전 데이터로 DDX3의 암 치료 가능성, Venlafaxine과 HTR1A의 연결 등 실제 발견 재현
- **오픈소스 공개**: 네트워크, 구현 코드, 온라인 쿼리 서비스 공개로 과학 커뮤니티 기여

## How

![Figure 3](figures/fig3.webp)

*Figure 3: MOLIERE query pipeline.*

- SPECIALIST NLP 도구로 MEDLINE 초록 정규화 및 전처리
- ToPMine을 이용한 의미 있는 n-gram 다중단어 구문 추출
- FastText로 각 토큰을 벡터 공간에 매핑하고 FLANN으로 유사도 기반 논문 네트워크 생성
- UMLS 메타시소러스와 의미 네트워크 통합으로 생의학 객체(유전자, 단백질, 질병 등) 연결
- 두 키워드 간 최단 경로 탐색 및 경로 주변의 추상 클라우드 확장
- PLDA+(확장 가능한 LDA 구현)로 클라우드 문서의 주제 모델링으로 해석 가능한 연결 기반 생성

## Originality

- 전체 MEDLINE 데이터셋 기반 최초의 대규모 가설 생성 시스템 구축
- 다중 데이터소스(논문, 키워드, 유전자, 단백질, 질병)의 이질적 정보 통합 네트워크 구조
- 제한 없는 어휘 기반 LDA와 자동 구문 인식의 결합으로 기존 방식 대비 일반화 성능 향상
- 최단 경로 발견과 주제 모델링의 조합으로 인간이 이해 가능한 텍스트 형태의 가설 제시

## Limitation & Further Study

- 최단 경로 방식의 한계: 실제로는 여러 경로가 존재할 수 있으나 단일 경로만 선택
- LDA 기반 주제 모델링의 해석 모호성: 자동 생성된 주제의 의미론적 타당성 검증 필요
- 평가 방식의 제한: 역사적 발견 재현으로 검증했으나, 진정한 새로운 가설의 발견 여부 확인 어려움
- 네트워크 구축 성능 확장성: 단어 임베딩과 근접 이웃 그래프 생성의 계산 복잡도 증가 가능성
- 후속 연구 방향: 다양한 경로 탐색 알고리즘, 주제 모델의 신뢰성 평가, 실제 임상 실험 검증, 사용자 피드백 기반 개선

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: MOLIERE는 전체 MEDLINE 데이터셋을 활용한 첫 대규모 가설 생성 시스템으로서, 기존 연구의 도메인 제약을 극복하고 오픈소스 및 온라인 서비스 제공으로 학계에 실질적인 기여를 한다. 다만 평가 방식의 보완과 실제 발견의 임상적 검증이 향후 과제이다.

## Related Papers

- 🔄 다른 접근: [[papers/1109_A_comprehensive_large-scale_biomedical_knowledge_graph_for_A/review]] — 생의학 분야에서 지식 그래프를 활용한 자동 가설 생성의 서로 다른 구현 방식과 적용 범위를 보여준다.
- 🏛 기반 연구: [[papers/929_A_network_approach_to_topic_models/review]] — 토픽 모델에 대한 네트워크 접근법이 대규모 생의학 지식 네트워크 구축의 방법론적 기반을 제공한다.
- 🔄 다른 접근: [[papers/1072_Embracing_Foundation_Models_for_Advancing_Scientific_Discove/review]] — 생의학 가설 생성 시스템을 통해 과학 발견에서 AI 활용의 다른 접근법과 벤치마크 비교 가능성을 제공한다.
- 🧪 응용 사례: [[papers/1001_Public_Profile_Matters_A_Scalable_Integrated_Approach_to_Rec/review]] — 생물의학 분야에서 자동화된 가설 생성을 통해 인용 추천 시스템의 응용 가능성을 보여준다.
- 🔄 다른 접근: [[papers/1016_Sci2Pol_Evaluating_and_Fine-tuning_LLMs_on_Scientific-to-Pol/review]] — 생의학 분야에서 과학 지식을 다른 형태(가설 vs 정책문서)로 변환하는 자동화 시스템의 다른 접근법을 보여준다.
- 🧪 응용 사례: [[papers/1112_CS-KG_20_A_Large-scale_Knowledge_Graph_of_Computer_Science/review]] — 컴퓨터과학 지식그래프를 생의학 분야 자동 가설 생성 시스템으로 응용한다.
- 🔗 후속 연구: [[papers/1109_A_comprehensive_large-scale_biomedical_knowledge_graph_for_A/review]] — 생의학 지식그래프를 활용한 가설 생성 시스템으로 약물 재위치 지정의 자동화된 접근법을 확장한다.
