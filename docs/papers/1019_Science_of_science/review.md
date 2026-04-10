---
title: "1019_Science_of_science"
authors:
  - "Santo Fortunato"
  - "Carl T. Bergstrom"
  - "Katy Börner"
  - "James A. Evans"
  - "Dirk Helbing"
date: "2018.03"
doi: "10.1126/science.aao0185"
arxiv: ""
score: 4.0
essence: "본 논문은 과학 자체를 정량적으로 분석하는 Science of Science (SciSci)라는 새로운 학문 분야를 제시하며, 대규모 데이터를 활용하여 과학 발전의 메커니즘과 과학자의 경력 궤적을 이해하고자 한다."
tags:
  - "cat/Science_of_Science_Research"
  - "sub/Research_Evaluation_and_Impact"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Fortunato et al._2018_Science of science.pdf"
---

# Science of science

> **저자**: Santo Fortunato, Carl T. Bergstrom, Katy Börner, James A. Evans, Dirk Helbing, Staša Milojević, Alexander M. Petersen, Filippo Radicchi, Roberta Sinatra, Brian Uzzi, Alessandro Vespignani, Ludo Waltman, Dashun Wang, Albert-László Barabási | **날짜**: 2018-03-02 | **DOI**: [10.1126/science.aao0185](https://doi.org/10.1126/science.aao0185)

---

## Essence


본 논문은 과학 자체를 정량적으로 분석하는 Science of Science (SciSci)라는 새로운 학문 분야를 제시하며, 대규모 데이터를 활용하여 과학 발전의 메커니즘과 과학자의 경력 궤적을 이해하고자 한다.

## Motivation

- **Known**: 과학 문헌의 지수적 성장과 인용 네트워크의 존재는 알려져 있으나, 과학 아이디어의 실제 확장 속도와 성공적인 과학의 요인들이 정량적으로 분석되지 않았다.
- **Gap**: 과학의 구조와 진화를 설명하는 보편적이고 도메인 특화된 법칙의 부재, 그리고 서로 다른 분야와 국가 간 문화적 차이를 고려한 과학 정책의 개발 부족.
- **Why**: 과학 발전의 근본 메커니즘을 이해함으로써 과학자의 경력 발전, 연구기관의 성과 평가, 효과적인 펀딩 방식 등을 개선하여 과학이 사회적 문제 해결에 더 효과적으로 기여할 수 있기 때문이다.
- **Approach**: Web of Science, Scopus 등 다양한 대규모 학술 데이터 소스를 활용하여 과학자, 기관, 아이디어 간의 네트워크를 구축하고, 네트워크 과학, 머신러닝, 통계분석 등 다학제적 방법론을 적용하여 과학의 구조와 동역학을 분석한다.

## Achievement


- **협력 네트워크 분석**: 새로운 과학 분야의 출현 양식과 분야 내 사회적 통합 과정을 규명
- **인용 역학 모델링**: 미시적 모델을 통해 개별 논문의 미래 영향력을 예측 가능
- **과학자 선택의 역설 발견**: 위험회피적 주제 선택은 혁신을 제약하지만, 위험한 선택을 감수하는 과학자가 획기적 발견을 이룰 확률이 높음을 정량화
- **팀 규모와 영향의 관계**: 소규모 팀이 새로운 아이디어로 분야를 혼란시키고, 대규모 팀이 단기 고영향을 달성함을 입증
- **아이디어 조합의 패턴**: 최고 영향의 과학은 전통적 조합을 기반하면서도 비관습적 조합을 특징으로 함을 발견

## How


- 대규모 인용 데이터베이스(WoS, Scopus, PubMed, Google Scholar 등)에서 논문, 저자, 인용 정보 수집
- 협력 네트워크와 인용 네트워크 구축 및 커뮤니티 탐지
- 제목과 초록에서 추출한 구문을 통한 대규모 텍스트 분석으로 개념 영역 측정
- 생성 모델(generative model)과 에이전트 기반 시뮬레이션으로 과학의 동역학 재현
- 계량경제학 방법, 네트워크 과학, 머신러닝 알고리즘, 수학적 분석을 통합 적용

## Originality

- 과학 자체를 연구 대상으로 하는 학문 분야의 체계적 정립으로 자기반영적(reflexive) 과학 탄생
- scientometrics, 과학사회학, 혁신 연구 등 다학제 이론과 방법의 통합으로 새로운 분석 프레임 제시
- 출판 증가 ≠ 아이디어 증가라는 역설적 발견으로 과학의 '질적 확장' 개념 도입", '개별 논문의 영향력 예측을 통해 과학을 물리학적으로 모델링 가능함을 보임
- 위험 회피 성향의 정량적 실증과 그 제약 효과 규명으로 과학 정책의 증거 기반 제공

## Limitation & Further Study

- **문화적 다양성 미반영**: 학문 분야와 국가 간 문화, 관행, 선호도 차이가 크며 일반화 어려움
- **도메인 특화의 필요성**: 보편적 법칙 추구와 도메인 특화 필요 사이의 긴장 해결 미흡
- **데이터 편향**: 영문 논문, 인용된 논문에 대한 편향으로 글로벌 과학 현상의 완전한 대표성 부족
- **인과관계 미규명**: 대부분 상관관계 분석으로 원인과 결과의 명확한 인과 메커니즘 미확립
- **후속 연구 방향**: (1) 분야별 맥락을 반영한 세분화된 SciSci 모델 개발, (2) 정성적 인터뷰와의 혼합방법론 활용, (3) 실시간 데이터 통합으로 정책 피드백 루프 구축, (4) 저소득 국가와 소수 언어 연구 포함으로 데이터 대표성 확대

## Evaluation

- Novelty: 5/5
- Technical Soundness: 4/5
- Significance: 5/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 본 논문은 거대 학술 데이터와 다학제적 방법론을 통합하여 과학의 구조와 동역학을 정량적으로 분석하는 새로운 학문 분야를 확립한 획기적 리뷰 논문이다. 과학 정책과 과학자 경력 개발에 즉시 적용 가능한 실증적 발견들을 제시하며, 향후 과학의 가속화와 사회 문제 해결에 기여할 잠재력이 크다.

## Related Papers

- 🏛 기반 연구: [[papers/1023_SciSciNet_A_large-scale_open_data_lake_for_the_science_of_sc/review]] — 과학의 과학 연구를 위한 대규모 오픈 데이터 인프라를 제공하여 실증적 분석의 기반을 마련한다.
- 🔗 후속 연구: [[papers/1071_Data_measurement_and_empirical_methods_in_the_science_of_sci/review]] — 과학의 과학 분야의 데이터, 측정, 실증 방법론에 대한 심화된 방법론적 가이드라인을 제공한다.
- 🔗 후속 연구: [[papers/1022_SciSciGPT_advancing_humanAI_collaboration_in_the_science_of/review]] — 과학의 과학 분야의 기본 개념과 방법론을 AI 협력 시스템으로 확장하여 자동화된 연구 워크플로우를 구현한다.
- 🏛 기반 연구: [[papers/1124_The_Science_of_Science/review]] — 과학의 과학 분야에 대한 포괄적인 개관을 제공하여 빅데이터 기반 과학 연구 분석의 이론적 토대를 마련한다.
