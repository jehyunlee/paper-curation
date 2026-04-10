---
title: "991_Open_Datasets_in_Learning_Analytics_Trends_Challenges_and_Be"
authors:
  - "Valdemar Švábenský"
  - "Brendan Flanagan"
  - "Erwin Daniel López Zapata"
  - "Atsushi Shimada"
date: "2026.02"
doi: "10.1145/3798096"
arxiv: ""
score: 4.0
essence: "학습분석(Learning Analytics) 연구의 세 주요 학회(LAK, EDM, AIED)에서 2020-2024년간 출판된 1,125개 논문을 분석하여 172개의 공개 데이터셋(Open Datasets)을 발굴하고, 현황을 파악하며 PRACTICE 8개 항목 체크리스트를 제시한 종합 조사 연구이다."
tags:
  - "cat/Science_of_Science_Research"
  - "sub/AI_and_Large_Language_Models"
  - "topic/scisci"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Švábenský et al._2026_Open Datasets in Learning Analytics Trends, Challenges, and Best PRACTICE.pdf"
---

# Open Datasets in Learning Analytics: Trends, Challenges, and Best PRACTICE

> **저자**: Valdemar Švábenský, Brendan Flanagan, Erwin Daniel López Zapata, Atsushi Shimada | **날짜**: 2026-02-19 | **DOI**: [10.1145/3798096](https://doi.org/10.1145/3798096)

---

## Essence

![Figure 1](figures/fig1.webp)

*Fig. 1. PRISMA flow diagram. Generated using the tool by Haddaway et al. [146].*

학습분석(Learning Analytics) 연구의 세 주요 학회(LAK, EDM, AIED)에서 2020-2024년간 출판된 1,125개 논문을 분석하여 172개의 공개 데이터셋(Open Datasets)을 발굴하고, 현황을 파악하며 PRACTICE 8개 항목 체크리스트를 제시한 종합 조사 연구이다.

## Motivation

- **Known**: Open Science의 중요성이 널리 인정되고 있으며, 데이터 공개는 연구 재현성, 협력, 신뢰성을 높이고 저자의 인용도(+25%)와 신뢰도를 증진시킨다. 그러나 LA 커뮤니티에서의 공개 데이터셋 현황과 실행 관행은 명확하지 않다.
- **Gap**: LA, EDM, AIED 분야에서 공개 데이터셋의 가용성, 특성, 분포, 그리고 데이터 공개 관행의 현황이 체계적으로 파악되지 않았으며, 연구자들이 데이터 공개 시 직면하는 구체적인 도전 요소와 해결 방안이 부재했다.
- **Why**: 공개 데이터셋은 연구 재현성과 협력을 지원하고 빠른 연구 진행을 가능하게 하며, FAIR 원칙 미준수에 따른 경제적 손실(EU 연 10.2억 유로)을 줄일 수 있다. 또한 domain-specific 접근이 필요하다는 선행 연구의 지적에 따라 LA 분야의 현황 파악이 시급하다.
- **Approach**: 3개 주요 학회에서 2020-2024년 발표된 1,125개 논문을 수작업으로 검토하여 공개 데이터셋을 발굴, 분류, 분석하고, FAIR 원칙 기반의 실행 가이드라인을 개발했다.

## Achievement

![Figure 2](figures/fig2.webp)

*Fig. 2. Distributions of dataset frequency across educational topics and levels of students.*

- **가장 포괄적인 데이터셋 컬렉션**: 172개의 고유한 공개 데이터셋을 발굴하였으며, 이 중 143개(83%)는 선행 조사에서 미포착된 신규 데이터셋이다.
- **상세한 분류 체계**: 데이터셋의 맥락(Context), 분석 방법(Analytical Methods), 사용 현황, 교육 주제, 수준, 지리적 분포, 학생 수, 데이터 포인트 규모 등을 체계적으로 분류했다.
- **PRACTICE 8개 항목 가이드라인**: 실행 가능한 체크리스트 형태의 권장사항을 제시하여 연구자들의 데이터 공개를 촉진한다.
- **원본 데이터셋 공개**: 발굴된 172개 데이터셋과 204개 관련 논문의 주석이 달린 인벤토리를 학술 커뮤니티에 제공한다.
- **현장의 갭 분석**: LA 커뮤니티가 데이터 부족한 분야(교육 맥락, 주제별, 지역별)를 식별하여 향후 연구 우선순위를 제시한다.

## How

![Figure 1](figures/fig1.webp)

*Fig. 1. PRISMA flow diagram. Generated using the tool by Haddaway et al. [146].*

- PRISMA(Preferred Reporting Items for Systematic Reviews and Meta-Analyses) 방법론을 따른 체계적 문헌 검토 수행
- LAK, EDM, AIED 3개 플래그십 학회의 2020-2024년 출판물(총 1,125개 논문) 수작업 검토
- 각 데이터셋에 대해 교육 주제, 수준, 지리적 위치, 규모, 접근성, 라이선싱, 분석 방법 등의 메타데이터 추출 및 분류
- FAIR 원칙(Findable, Accessible, Interoperable, Reusable)과 Open Data Handbook 정의 활용한 공개 데이터 정의 수립
- 발견된 갭과 도전 요소를 바탕으로 8개 항목의 PRACTICE 체크리스트 개발(Persistent identifier, Repository choice, Accessibility, Citability, Transparency, Interoperability, Community standards, Ethical compliance)

## Originality

- LA/EDM/AIED 분야의 **최초 종합 조사**: 선행 조사가 미포착한 143개 신규 데이터셋을 발굴하며, 5년간 3개 플래그십 학회 전수 조사로 현장의 정확한 현황을 제시
- **Domain-specific 실행 가이드**: 일반적 Open Science 원칙이 아닌 LA 연구자의 실제 수요와 도전에 기반한 맞춤형 PRACTICE 가이드라인 개발
- **상세한 메타데이터 체계**: 단순 데이터셋 목록화가 아닌 교육적 맥락, 분석 방법, 지리적 분포 등 다각도의 특성 분석으로 재사용성 증진
- **공개된 인벤토리 자산**: 172개 데이터셋과 204개 논문의 주석이 달린 인벤토리를 학술 커뮤니티에 공유하여 향후 연구의 출발점 제공

## Limitation & Further Study

- **시간적 범위 제한**: 2020-2024년 5년간 데이터만 분석하여 장기적 추세 변화(2019년 이전)를 포착하지 못함
- **학회 중심 분석**: 3개 주요 학회 논문만 대상으로 하여 저널 출판, gray literature, 비영어권 연구물은 미포함
- **수작업 검토의 주관성**: 1,125개 논문의 수작업 검토로 인한 검토자 간 일치도(inter-rater reliability) 문제 가능성
- **숨겨진 데이터셋**: 논문에 명시되지 않았지만 보충 자료나 저자 요청으로만 접근 가능한 데이터셋 누락 가능성
- **후속 연구 방향**: (1) 다른 학회 및 저널 확대 조사, (2) PRACTICE 가이드라인의 실제 채택률 모니터링, (3) 데이터 공개 장애 요소에 대한 심층 인터뷰 연구, (4) 자동화된 데이터셋 발굴 방법 개발

## Evaluation

- Novelty: 4/5
- Technical Soundness: 3/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: 이 논문은 Learning Analytics 분야에서 공개 데이터셋의 현황을 처음으로 종합 조사한 선구적 연구로, 143개의 신규 데이터셋 발굴과 PRACTICE 가이드라인을 통해 LA 커뮤니티의 Open Science 실행을 직접적으로 지원한다. 학회 중심 범위와 수작업 검토의 한계가 있으나, 도메인 특화 가이드라인과 공개 인벤토리 제공으로 학술 커뮤니티에 즉시 실용적 가치를 제공한다.

## Related Papers

- 🏛 기반 연구: [[papers/1071_Data_measurement_and_empirical_methods_in_the_science_of_sci/review]] — 과학의 과학 분야의 데이터와 측정 방법론에 대한 기초를 제공한다
- 🔄 다른 접근: [[papers/1115_Google_Scholar_Microsoft_Academic_Scopus_Dimensions_Web_of_S/review]] — 다양한 학술 데이터베이스 비교를 통해 공개 데이터셋의 다른 관점을 제시한다
- 🔗 후속 연구: [[papers/1023_SciSciNet_A_large-scale_open_data_lake_for_the_science_of_sc/review]] — 과학의 과학 연구를 위한 대규모 데이터 레이크로 학습분석 데이터셋을 확장한다
