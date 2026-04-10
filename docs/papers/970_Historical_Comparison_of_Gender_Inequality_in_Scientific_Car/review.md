---
title: "970_Historical_Comparison_of_Gender_Inequality_in_Scientific_Car"
authors:
  - "Junming Huang"
  - "Alexander J. Gates"
  - "Roberta Sinatra"
  - "Albert-László Barabási"
date: "2020"
doi: "10.1073/pnas.1914221117"
arxiv: ""
score: 4.0
essence: "1955-2010년 간 150만 명 이상의 과학자 데이터를 분석하여 STEM 분야 전 학문과 83개국에 걸친 성별 불평등의 장기 추이를 규명했다. 역설적으로 여성 과학자 비율 증가가 생산성(productivity)과 영향력(impact)의 성별 격차 증가를 동반했으나, 동일한 논문 수에 대해 남녀의 연간 발표율(annual rate)과 커리어 영향력이 동등함을 발견했다."
tags:
  - "cat/Science_of_Science_Research"
  - "sub/Career_Trajectories_and_Inequality"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Huang et al._2020_Historical Comparison of Gender Inequality in Scientific Careers Across Countries and Disciplines.pdf"
---

# Historical Comparison of Gender Inequality in Scientific Careers Across Countries and Disciplines

> **저자**: Junming Huang, Alexander J. Gates, Roberta Sinatra, Albert-László Barabási | **날짜**: 2020 | **DOI**: [10.1073/pnas.1914221117](https://doi.org/10.1073/pnas.1914221117)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1.*

1955-2010년 간 150만 명 이상의 과학자 데이터를 분석하여 STEM 분야 전 학문과 83개국에 걸친 성별 불평등의 장기 추이를 규명했다. 역설적으로 여성 과학자 비율 증가가 생산성(productivity)과 영향력(impact)의 성별 격차 증가를 동반했으나, 동일한 논문 수에 대해 남녀의 연간 발표율(annual rate)과 커리어 영향력이 동등함을 발견했다.

## Motivation

- **Known**: 학계의 성별 차이는 널리 문서화되었으나 대부분 특정 국가, 학문, 기관의 활동 과학자 부분집합에 한정된 사례연구에 불과했다. 여성 과학자들이 남성에 비해 적게 발표하고 인용도 적다는 '생산성 퍼즐(productivity puzzle)'이 보고되어 왔다.
- **Gap**: 완전한 커리어 출판 이력 재구성의 방법론적 난제로 인해 전 학문 분야와 국가를 아우르는 종단적(longitudinal), 학문적, 지리적 전경이 부재했다. 작은 표본크기에서 무거운 꼬리 분포(heavy-tailed distribution)의 효과가 증폭되는 한계가 있었다.
- **Why**: 성별 불평등의 근본 원인을 이해하기 위해서는 전체 커리어 궤적을 추적할 수 있는 대규모 데이터 기반 분석이 필수적이며, 이는 학계 제도 개선과 정책 수립에 중요한 시사점을 제공할 수 있다.
- **Approach**: Web of Science 데이터베이스에서 1900-2016년 786만 명 과학자의 출판 기록을 수집하고, 머신러닝 기반 성별 식별 방법으로 356만 명 이상의 저자 성별을 판정했다. 1955-2010년 사이 커리어가 종료된 152만 명 과학자의 완전한 출판 이력을 재구성하여 비교분석했다.

## Achievement

![Figure 2](figures/fig2.webp)

*Fig. 2.*

- **성별 참여 증가와 격차 역설**: 지난 60년간 여성 과학자 비율이 12%(1955)에서 35%(2005)로 증가했으나, 동시에 생산성과 영향력의 성별 격차도 함께 증가했다.
- **성별 불변성 발견**: 남녀 과학자가 연간 동일한 속도로 논문을 발표하며, 동일한 규모의 논문집에 대해 동등한 커리어 영향력을 가지고 있다 (gender invariants).
- **커리어 길이와 탈락률의 설명력**: 생산성과 영향력의 커리어 누적 차이의 대부분은 여성의 단축된 커리어 길이(career length)와 높은 탈락률(dropout rate)로 설명되며, 이는 지속 가능성(sustainability) 문제를 지시한다.
- **광범위한 학문-국가 간 일관성**: 13개 주요 학문과 83개국 모두에서 성별 생산성 격차가 관찰되며, 특히 수학/물리/컴퓨터과학(15%)과 심리학(33%) 간 여성 비율 차이가 뚜렷하다.
- **상위 저자층에서 심화된 격차**: 상위 20% 생산성 저자에서 남성이 여성보다 37% 더 많이 발표하나, 중간층과 하위층에서는 격차가 없거나 역전된다.

## How

![Figure 1](figures/fig1.webp)

*Fig. 1.*

- Web of Science (WoS) 데이터베이스에서 1900-2016년 출판 기록 조회
- 머신러닝 기반 상태-최신 성별 식별 방법 적용 (state-of-the-art gender identification method)
- 1955-2010년 커리어 종료 과학자 152만 3천여 명 선별 (여성 41만 2천, 남성 111만)
- 연간 생산성(yearly productivity), 총 생산성(total productivity), 10년 후 인용 수(citations after 10 years c₁₀) 추출
- 커리어 길이(career length) 계산: 첫 논문과 마지막 논문 사이 기간
- 상대 성별 격차(relative gender difference) = (남성 평균 - 여성 평균) / 여성 평균
- Microsoft Academic Graph (MAG)와 DBLP 데이터셋에서 독립적 재현(replication) 수행
- t-test 등 통계적 유의성 검증 (P < 10⁻⁴)

## Originality

- 전례 없는 규모의 완전한 커리어 출판 이력 재구성: 단편적 사례연구를 벗어나 83개국, 13개 학문, 152만 명의 종단 데이터 통합 분석
- 성별 불변성(gender invariants) 개념의 발견: 동일 논문 수 조건에서 남녀의 연간 발표율과 커리어 영향력이 동등하다는 역직관적 통찰
- 생산성 퍼즐의 재해석: 절대 생산성 차이가 아닌 커리어 지속성 문제로서의 재프레이밍은 정책 방향을 근본적으로 전환
- 다중 데이터셋 독립 재현(WoS, MAG, DBLP): 데이터베이스 편향과 저자 동명이인(disambiguation) 오류에 대한 견고성 입증
- 계층별, 학문별, 국가별, 기관순위별 다차원 분층 분석으로 일반화 가능성 강화

## Limitation & Further Study

- **데이터 커버리지 편향**: 중국, 일본, 한국, 브라질, 말레이시아, 싱가포르 저자가 체계적으로 누락되어 비서구권 과소 표현
- **출판 활동 한정**: 교육, 행정, 산업 연구, 정부 연구 활동은 포착 불가능하며 출판 커리어만 분석
- **성별 이진 분류**: 비이분법적 성별 정체성, 문화적 성명 차이(예: 동아시아 가족명)로 인한 성별 식별 오류 가능성
- **생존 편향**: 1955-2010년 커리어 종료자만 대상으로 진행 중인 활동 과학자 제외
- **인과관계 미분석**: 상관관계 기반이며, 탈락이 의도적 선택인지 제도적 배제인지 미분석
- **후속연구 제언**: (1) 커리어 단축과 탈락의 원인 심층 질적 분석, (2) 육아 휴직, 겸임금지(dual-career) 정책 효과 측정, (3) 피어 리뷰와 협력 네트워크의 성별 편향 분석, (4) 비서구권 데이터 통합

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: STEM 분야 성별 불평등에 대한 가장 포괄적인 종단 분석으로, 생산성 퍼즐의 새로운 해석(커리어 지속성 문제)을 제시하여 학계 정책과 제도 개혁의 방향을 재설정하는 혁신적 연구이다. 다만 비서구권 데이터 누락과 인과 메커니즘 분석의 미흡이 후속 심층 연구의 기초가 될 것이다.

## Related Papers

- 🔗 후속 연구: [[papers/965_Gender-diverse_teams_produce_more_novel_and_higher-impact_sc/review]] — 성별 다양한 팀이 더 참신하고 높은 영향력의 과학을 생산한다는 연구와 연결되어 개별 여성 과학자의 경력 불평등이 팀 차원의 성과에 미치는 영향을 이해한다.
- 🧪 응용 사례: [[papers/1027_Systemic_Gendered_Citation_Imbalance_in_Computer_Science_Evi/review]] — 컴퓨터 과학의 체계적 성별 인용 불균형 분석과 연결되어 STEM 분야 전반의 성별 불평등이 인용 패턴에 미치는 구체적 영향을 보여준다.
- 🔗 후속 연구: [[papers/940_Bibliometrics_Global_Gender_Disparities_in_Science/review]] — 과학 분야 성별 불평등에 대한 글로벌 분석을 시간적 변화와 국가별 비교를 통해 더욱 상세히 확장한 종단 연구를 제공한다.
- 🔗 후속 연구: [[papers/1048_Unequal_effects_of_the_COVID-19_pandemic_on_scientists/review]] — 팬데믹이 기존 성별 불평등을 심화시키는 현상을 과학계 성별 불평등의 역사적 맥락에서 이해
- 🧪 응용 사례: [[papers/1052_Updated_science-wide_author_databases_of_standardized_citati/review]] — 표준화된 인용 지표 데이터베이스를 활용하여 과학 경력에서의 성별 불평등을 역사적으로 비교 분석할 수 있다.
- 🏛 기반 연구: [[papers/976_Intersectional_inequalities_in_science/review]] — 성별 불평등에 대한 역사적 분석을 제공하여 교차적 불평등 연구의 기초가 된다
- 🔗 후속 연구: [[papers/1026_Systematic_Inequality_and_Hierarchy_in_Faculty_Hiring_Networ/review]] — 학계 채용 불평등의 역사적 변화와 성별 격차를 함께 분석하면 구조적 불평등의 전체적 양상을 파악할 수 있다.
