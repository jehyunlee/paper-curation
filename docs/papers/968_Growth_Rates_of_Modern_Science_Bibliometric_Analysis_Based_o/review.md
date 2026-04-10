---
title: "968_Growth_Rates_of_Modern_Science_Bibliometric_Analysis_Based_o"
authors:
  - "Lutz Bornmann"
  - "Rüdiger Mutz"
date: "2015"
doi: "10.1002/asi.23329"
arxiv: ""
score: 4.0
essence: "1650년부터 2012년까지 과학의 성장률을 분석한 연구로, 인용 참고문헌(cited references)과 출판물 수를 기반으로 segmented regression analysis(구간 회귀 분석)를 적용하여 과학의 성장 단계를 규명했다."
tags:
  - "cat/Bibliometric_Network_Analysis"
  - "sub/Temporal_and_Longitudinal_Analysis"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Bornmann and Mutz_2015_Growth Rates of Modern Science Bibliometric Analysis Based on the Number of Publications and Cited.pdf"
---

# Growth Rates of Modern Science: Bibliometric Analysis Based on the Number of Publications and Cited References

> **저자**: Lutz Bornmann, Rüdiger Mutz | **날짜**: 2015 | **DOI**: [10.1002/asi.23329](https://doi.org/10.1002/asi.23329)

---

## Essence

![Figure 2](figures/fig2.webp)

*Figure 2 shows the segmented growth of the annual number of cited references*

1650년부터 2012년까지 과학의 성장률을 분석한 연구로, 인용 참고문헌(cited references)과 출판물 수를 기반으로 segmented regression analysis(구간 회귀 분석)를 적용하여 과학의 성장 단계를 규명했다.

## Motivation

- **Known**: Price(1965)의 선구적 연구에서 과학이 지수함수적으로 성장하며 10-15년마다 규모가 2배 증가한다는 것이 알려져 있다. 정보과학 분야에서 문헌 역학(literature dynamics) 연구가 지속되어 왔다.
- **Gap**: 기존 연구들은 특정 시기만 분석했으나, 본 연구는 최신 데이터(~2012년)를 포함한 장기간 분석이 부족했다. 또한 단순 지수함수 모델만 사용하여 성장률이 변하는 시점을 놓쳤다.
- **Why**: 과학의 성장 패턴을 정확히 파악하면 과학정책 수립, 자원 배분, 학문 분야의 미래 발전 예측에 중요한 정보를 제공할 수 있다.
- **Approach**: WoS(Web of Science) 기반 1980-2012년 출판물과 1650-2012년 인용 참고문헌 데이터를 수집한 후, segmented regression analysis를 적용하여 성장률이 변하는 breakpoint(구간 경계)를 자동으로 탐지했다.

## Achievement

![Figure 2](figures/fig2.webp)

*Figure 2 shows the segmented growth of the annual number of cited references*

- **세 가지 성장 단계 규명**: 인용 참고문헌 분석에서 18세기 중반까지 1% 미만, 양차 대전 사이까지 2-3%, 2012년까지 8-9%의 세 가지 성장 단계를 확인
- **지수함수적 성장의 구간별 차이 입증**: 각 단계에서 성장률이 이전 단계 대비 약 3배 증가하는 패턴 발견
- **학문 분야별 비교 분석**: 자연과학(natural sciences)과 의학·보건과학(medical and health sciences)의 성장률 차이를 통계적으로 검증
- **최신 데이터 기반 재검증**: Price의 1960년대 이론을 현대 데이터로 재검증하여 장기간 성장 추세 확인

## How


- WoS 데이터베이스에서 1980-2012년 전체 출판물(38,508,986건) 추출
- 인용 참고문헌 데이터 수집(총 755,607,107건, 1650-2012년 커버)
- 지수함수 모델 y(t)=b0*exp(b1*(t-1980)) 적용 (비선형 회귀)
- Segmented regression analysis로 다중 breakpoint(a1, a2, ...) 동시 추정
- 최소제곱법(Least Squares, Gauss-Newton)으로 회귀 계수(b1, b2, b3) 추정
- 설명력(R²) 및 시각적 검사로 최적 구간(segment) 수 결정 (3개 breakpoint → 4개 segment, R²=99%)
- 학문 분야 간 차이 검증을 위해 상호작용항(interaction terms) 추가

## Originality

- 기존의 단순 지수함수 모델에서 벗어나 시간에 따라 변하는 성장률을 **구간별로 분리 추정**하는 segmented regression 도입
- 인용 참고문헌을 이용하여 데이터베이스 자료가 없는 **1650년대부터의 과학 성장을 추론**할 수 있는 방법론 제시
- 최신 데이터(2012년까지)와 advanced statistical technique 조합으로 **Price의 이론을 재검증하면서 성장 단계의 구체적 시점 규명**
- 학문 분야(자연과학 vs 의학·보건)별 성장률 **비교 분석 틀 제시**

## Limitation & Further Study

- 인용 참고문헌 기반 분석으로 **아직 인용되지 않은 문헌을 누락**할 수 있음
- 초기 과학 발전이 현재의 인용 관행에 의존하므로 **현대 인용 문화의 편향(citation bias) 영향 가능성**
- WoS 데이터베이스만 사용하여 **타 분야(사회과학, 인문학) 대표성 부족**
- Segmented regression의 가정(정규분포, 등분산성, 자기상관 없음)이 **시계열 데이터에서 위반될 수 있으나 모델 적합도로 판단**
- 후속 연구: 다른 인용 데이터베이스(Scopus, Google Scholar) 활용 비교, 더 세분화된 학문 분류로 분석, 비인용 지표(altmetrics) 통합, 학문 분야별 출판 문화 차이 심층 분석 필요

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: Price의 고전적 지수함수 성장 모델을 segmented regression으로 정교하게 재검증하여, 과학의 성장이 세 단계의 뚜렷한 성장률 변화를 보임을 입증했다. 방법론의 혁신성과 역사적 데이터 복원의 독창성이 높으나, 인용 편향 및 데이터베이스 한계에 대한 더 깊은 논의가 필요하다.

## Related Papers

- ⚖️ 반론/비판: [[papers/995_Papers_and_patents_are_becoming_less_disruptive_over_time/review]] — 과학의 지속적 성장 패턴과 최근 과학의 파괴적 혁신 감소 현상이 상반된 관점을 제시한다.
- 🔗 후속 연구: [[papers/1030_The_Burden_of_Knowledge_and_the_Death_of_the_Renaissance_Man/review]] — 과학 성장률 변화가 지식 축적 부담과 르네상스맨 소멸이라는 구조적 문제로 이어지는 연결고리를 보여준다.
- 🧪 응용 사례: [[papers/1045_The_strain_on_scientific_publishing/review]] — 과학 출판의 양적 성장이 학술 출판 시스템에 가하는 압박을 실증적으로 분석한다.
- 🔄 다른 접근: [[papers/1037_The_Misleading_Narrative_of_the_Canonical_Faculty_Productivi/review]] — 서지계량학적 성장률 분석과 개별 연구자의 생산성 궤적 분석을 결합하여 미시-거시 수준의 과학 성장을 통합적으로 이해할 수 있다.
