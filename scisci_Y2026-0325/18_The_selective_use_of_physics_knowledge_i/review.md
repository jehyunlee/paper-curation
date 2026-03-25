# The Selective Use of Physics Knowledge in Policy: How Interdisciplinary Physics Bridges Subfields and Shapes Policy Influence

> **저자**: Jeongmin Lee, Jisung Yoon | **날짜**: 2026년 2월 | **arXiv**: 2602.10427v1

---

## 핵심 요약
본 논문은 물리학 지식이 정책 문서에 어떻게 선택적으로 동원되는지를 실증적으로 분석한다. Overton 정책 데이터베이스와 American Physical Society(APS) 출판물을 연결한 데이터셋을 구축하여, 정책 문서가 물리학 연구 생산량과는 상이한 구조로 물리학 지식을 인용함을 보인다. 핵심 발견은 학제간(interdisciplinary) 물리학이 정책 담론 진입의 "gateway" 역할을 하지만, 정책 내 downstream influence는 지구물리학(Geophysics) 분야가 약 24% 더 높다는 것이며, 이는 visibility와 influence의 분리를 실증적으로 입증한다.

## 연구 배경 및 동기
- 과학 지식이 정책 결정에 점점 중요해지고 있으나, 어떤 형태의 과학 지식이 정책에 선택적으로 동원되는지에 대한 체계적 실증 연구가 부족
- "Two communities theory"에 따르면 과학자와 정책입안자 사이에 구조적 격차가 존재: 과학은 공급 중심(supply-driven), 정책은 수요 중심(demand-driven)
- 물리학은 의학이나 경제학과 달리 기술을 통해 간접적으로 정책에 영향을 미치므로, science-policy 간극의 "hard test case"로 적합
- 학제간 연구가 정책 진입의 게이트웨이 역할을 한다는 가설을 검증하되, 진입(visibility)과 영향력(influence)을 구분해야 한다는 문제의식

## 방법론
- **데이터 구축**: Overton 데이터베이스의 757개 정책 문서와 APS의 1,156개 물리학 논문을 DOI로 연결. 미국 정부 기관, 입법부, 싱크탱크 및 국제기구(IGO) 문서로 제한
- **분야 분류**: PACS(Physics and Astronomy Classification Scheme) 코드의 1자리 수준(10개 카테고리)으로 분류. Category 0(General Physics)과 Category 8(Interdisciplinary Physics)을 학제간 물리학으로 정의
- **Fractional weighting**: 정책 문서의 인용 수와 논문의 PACS 코드 수에 따른 이중 정규화로 특정 분야의 과대 추정 방지
- **Topic modeling**: LDA를 적용하여 정책 문서를 6개 주제(Global Security, Complex Systems, Energy & Climate, Industrial Finance, Global Economy, Health & Nuclear)로 분류
- **네트워크 분석**: PACS 코드의 가중 co-citation 네트워크 구축 후 disparity filter로 backbone 추출, Louvain 알고리즘으로 커뮤니티 탐지
- **회귀 분석**: (1) Visibility 모델 — 학술 논문의 정책 인용 수를 종속변수로, (2) Influence 모델 — 정책 문서의 정책 간 인용 수를 종속변수로 하는 OLS 회귀

## 주요 결과
- **구조적 괴리**: 학술 생산의 주류인 Condensed Matter(Category 7, 29.3%)는 정책 인용에서 비중이 축소되고, 학술 생산 비중이 낮은 Interdisciplinary Physics(Category 8, 학술 5.5% vs. 정책 19.8%)가 정책에서 과대 대표됨
- **기관별 이질성**: 싱크탱크는 학제간 물리학에 77.3%(Cat 0 + Cat 8)의 인용을 집중; 정부 기관은 Condensed Matter(34.4%)에 집중; IGO는 Nuclear Physics(13.3%)에 집중
- **네트워크 brokerage**: 학제간 물리학이 co-citation 네트워크에서 가장 높은 degree centrality(0.14)와 closeness centrality(0.38)를 보이며 전문 분야 간 구조적 교량 역할
- **Visibility vs. Influence 분리**: Category 8은 정책 인용(visibility)에서 유의미한 양의 효과(beta=0.04, p=0.002)를 보이지만, downstream influence에서는 유의하지 않음(beta=-0.03, p=0.50). 반면 Category 9(Geophysics)는 visibility(beta=0.07)와 influence(beta=0.21, ~24% 증가) 모두에서 유의
- **IPCC 효과**: Geophysics의 높은 influence는 IPCC 평가 보고서 등 기후 거버넌스의 합의 문서가 표준화 메커니즘으로 작용하여 반복 인용되는 구조에 기인

## 독창성 및 기여
- Science-policy interface에서 **visibility와 influence를 명시적으로 분리**하여 분석한 점이 핵심 기여. 정책 담론 진입과 실질적 정책 영향력이 다른 메커니즘으로 작동함을 실증
- 물리학이라는 정책과 구조적으로 거리가 먼 학문을 대상으로 하여, 학제간 연구의 "gateway" 역할을 더 명확하게 드러냄
- 기관 유형과 정책 주제에 따른 물리학 하위 분야 수요의 이질성을 세밀하게 매핑
- Fractional weighting 방법론으로 인용 편향을 체계적으로 통제

## 한계 및 향후 연구
- **저자 언급 한계**: Overton 데이터베이스의 명시적 인용에 의존하여, agenda setting이나 비공식적 지식 확산 등은 포착하지 못함; PACS 코드가 2016년까지만 사용되어 시간적 해상도에 제약; 물리학에 한정되어 일반화에 한계
- **추가 지적**: APS 논문 1,156편과 정책 문서 757편이라는 표본 크기가 상대적으로 작아, 세부 분야 수준의 분석에서 통계적 검정력이 제한적일 수 있음
- OLS 회귀에서 인과 추론이 아닌 상관 분석에 머물러 있으며, 내생성(endogeneity) 문제에 대한 대응이 부족
- 정책 문서의 "영향력"을 정책 간 인용으로 측정하는 것은 실제 정책 변화나 집행에 미치는 영향과는 다를 수 있음
- 시간에 따른 동적 변화(예: 기후 정책의 부상에 따른 Geophysics 인용 증가 추세)에 대한 분석이 부족

## 평가
| 항목 | 점수 (1-5) |
|------|-----------|
| Novelty | 4 |
| Technical Soundness | 4 |
| Significance | 4 |
| Clarity | 4 |
| Overall | 4 |

**총평**: Science-policy interface에서 visibility와 influence의 분리라는 중요한 개념적 기여를 제공하며, 학제간 연구의 정책적 역할에 대한 실증적 근거를 체계적으로 제시한 우수한 연구이다. 표본 규모 확대와 인과 추론 방법론의 보강이 이루어진다면 더욱 강력한 결론을 도출할 수 있을 것이다.
