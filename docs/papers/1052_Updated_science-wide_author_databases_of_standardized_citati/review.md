---
title: "1052_Updated_science-wide_author_databases_of_standardized_citati"
authors:
  - "John P. A. Ioannidis"
  - "Kevin W. Boyack"
  - "Jeroen Baas"
date: "2020"
doi: "10.1371/journal.pbio.3000918"
arxiv: ""
score: 4.0
essence: "Scopus 데이터를 기반으로 전 과학 분야의 상위 인용 과학자들에 대한 표준화된 인용 지표 데이터베이스를 2019년까지 업데이트하여 공개한 논문이다."
tags:
  - "cat/Scientific_Impact_and_Innovation"
  - "sub/Citation_metrics_and_impact_measurement"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Ioannidis et al._2020_Updated science-wide author databases of standardized citation indicators.pdf"
---

# Updated science-wide author databases of standardized citation indicators

> **저자**: John P. A. Ioannidis, Kevin W. Boyack, Jeroen Baas | **날짜**: 2020 | **DOI**: [10.1371/journal.pbio.3000918](https://doi.org/10.1371/journal.pbio.3000918)

---

## Essence


Scopus 데이터를 기반으로 전 과학 분야의 상위 인용 과학자들에 대한 표준화된 인용 지표 데이터베이스를 2019년까지 업데이트하여 공개한 논문이다.

## Motivation

- **Known**: 과학자들의 인용 영향력을 측정하기 위해 h-index, h-m index 등 다양한 인용 지표가 사용되고 있으며, 2019년 첫 데이터베이스 버전이 과학계에 큰 관심을 받았다.
- **Gap**: 기존 데이터베이스는 최신 데이터가 부족했고, 학제간 저널 분류가 정확하지 않았으며, 세부 분야별 비교 가능성이 제한적이었다.
- **Why**: 과학자의 인용 영향력 평가는 학문적 성과 평가, 펀딩 배분, 인사 결정 등에 중요하며, 분야별 정확한 비교는 공정한 평가를 위해 필수적이다.
- **Approach**: Scopus 데이터베이스의 2020년 5월 기준 데이터를 활용하여 합성 인용 지수(composite citation index) 기반 상위 과학자 데이터베이스를 구성하고, 딥러닝을 통해 학제간 저널 분류를 개선했다.

## Achievement


- **업데이트된 포괄적 데이터베이스**: 경력 전체 인용 영향력(career-long)과 2019년 단일 연도 영향력(single year) 데이터 제공
- **저인용 분야 포용성 확대**: 상위 100,000명 기준 외에도 자신의 세부 분야에서 상위 2%에 속하는 과학자 포함
- **학제간 저널 분류 개선**: 문자 기반 합성곱 신경망(character-based CNN)을 이용해 학제간 저널을 특정 분야로 분류
- **분야별 맥락 정보 강화**: 각 과학자의 세부 분야 내 순위와 해당 분야 전체 과학자 수 제공
- **자인용 분석 강화**: 자인용 포함/미포함 상황에서의 인용 지표와 자인용 비율의 백분위수 임계값 제공
- **공개 접근성**: 모든 데이터와 코드를 Mendeley Data에서 무료로 공개

## How


- Scopus 데이터베이스에서 2020년 5월 6일 기준 인용 데이터 수집
- 6개 인용 지표(NC, H, Hm, NCS, NCSF, NCSFL)를 로그 정규화하여 합성 지수 계산
- Science-Metrix 분류 시스템을 기반으로 하면서 CNN을 통해 학제간 저널의 분야 할당
- career-long과 single year 2019 각각에 대해 백분위수(25th, 50th, 75th, 90th, 95th, 99th) 임계값 계산
- 분야별, 세부분야별 인용 밀도 고려하여 상위 2% 기준 적용
- 자인용 비율 및 인용/인용 논문 비율 분석으로 인용 조작 가능성 검토

## Originality

- 전 과학 분야를 대상으로 한 최대 규모의 표준화된 인용 지표 데이터베이스 구축
- 학제간 저널 분류에 딥러닝 기법 적용으로 분류 정확도 향상
- 분야별 상대적 비교를 가능하게 하는 맥락 정보(분야 내 순위, 총 과학자 수) 포함
- 자인용 조작 탐지를 위한 통계적 지표 제공

## Limitation & Further Study

- Scopus 데이터 기반으로 다른 데이터베이스(WoS 등)와의 포괄성 차이 존재 가능
- 저명도가 낮은 과학자들의 데이터 포함이 부족할 수 있음 (상위 100,000명 또는 분야 상위 2% 기준)
- 자인용 비율이 높거나 인용/논문 비율이 극단적인 경우의 판단이 전적으로 연구자의 해석에 의존
- 학제간 저널 분류의 CNN 모델이 완벽하지 않을 수 있으며, 모델 성능이 제시되지 않음
- 저인용 분야의 인용 밀도 차이로 인한 분야 간 비교 시 여전히 주의 필요
- **후속 연구**: 다른 데이터베이스(WoS, Google Scholar)와의 비교 분석, 시간에 따른 인용 추세 변화 분석, 인용 조작 탐지 알고리즘 고도화

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 전 과학 분야 과학자의 인용 영향력을 포괄적이고 투명하게 평가할 수 있는 중요한 자원을 제공하며, 딥러닝을 통한 분류 개선과 분야별 맥락 정보 강화로 학문적 평가의 공정성을 높였다.

## Related Papers

- 🔗 후속 연구: [[papers/933_An_index_to_quantify_an_individuals_scientific_research_outp/review]] — 개별 연구자의 과학적 성과를 정량화하는 h-지수 연구를 전체 과학 분야로 확장한 표준화된 데이터베이스를 제공한다.
- 🧪 응용 사례: [[papers/970_Historical_Comparison_of_Gender_Inequality_in_Scientific_Car/review]] — 표준화된 인용 지표 데이터베이스를 활용하여 과학 경력에서의 성별 불평등을 역사적으로 비교 분석할 수 있다.
- 🔗 후속 연구: [[papers/1056_Where_Do_Your_Citations_Come_From_Citation-Constellation_A_F/review]] — 표준화된 저자 데이터베이스를 인용 네트워크의 사회구조적 분석으로 확장한다.
- 🔗 후속 연구: [[papers/993_OpenAlex_A_fully-open_index_of_scholarly_works_authors_venue/review]] — OpenAlex의 저자 정보를 표준화된 인용 데이터베이스와 연결하여 더 정확한 학술 성과 분석이 가능하다.
