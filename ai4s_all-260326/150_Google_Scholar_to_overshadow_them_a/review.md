# Google Scholar to Overshadow Them All? Comparing the Sizes of 12 Academic Search Engines and Bibliographic Databases

* **저자**: Michael Gusenbauer
* **기관**: Institute of Innovation Management, Johannes Kepler University Linz, Austria
* **발행**: Scientometrics, Vol. 118, pp. 177-214, 2019
* **DOI**: [10.1007/s11192-018-2958-5](https://doi.org/10.1007/s11192-018-2958-5)
* **PDF**: [Springer Link](http://link.springer.com/10.1007/s11192-018-2958-5)

---

## Essence (본질)

12개 주요 **학술 검색 엔진 및 서지 데이터베이스(ASEBDs)**의 규모를 비교 추정하는 계량서지학 연구이다. **반복적 쿼리 최적화(iterative query optimization)** 방법을 통해 각 데이터베이스에서 **쿼리 히트 카운트(QHC)**의 최댓값을 식별하여 규모를 추정한다. 주요 발견으로, **Google Scholar가 약 3억 8,900만 건**의 레코드를 보유하여 가장 포괄적인 학술 검색 엔진임을 확인했으며, 이는 기존 추정치(1억 7,600만 건, Orduna-Malea et al., 2015)보다 **50% 이상 크다**는 것을 보여준다. ProQuest(2억 8,000만)와 WorldWideScience(3억 2,300만, 단 불안정)가 뒤를 이으며, BASE(1억 1,800만), Web of Science(1억 600만), EbscoHost(1억 300만) 등의 규모도 최초로 비교 제시했다.

---

## Motivation (연구 동기)

- ASEBD의 규모 정보는 종종 오래되었거나 완전히 부재하여, 연구자가 특정 데이터베이스의 범위를 평가하기 어려움
- 기존 계량서지학 연구는 개별 데이터베이스를 단독으로 또는 소수만 비교하여, 주요 ASEBD 간의 최신 비교 정보가 부재
- Google Scholar의 규모가 과소추정되어 왔으며, Google 자체가 규모 정보를 공개하지 않아 독립적 추정이 필요
- ProQuest, EbscoHost 등 대형 구독 기반 서비스의 규모 추정이 처음으로 시도됨

---

## Achievement (주요 성과)

1. **12개 ASEBD 규모 비교**: Google Scholar, BASE, CiteSeerX, EbscoHost, Microsoft Academic, ProQuest, Q-Sensei Scholar, Scopus, Semantic Scholar, Web of Science, WorldWideScience, AMiner의 규모를 단일 방법론으로 비교
2. **Google Scholar 규모 재추정**: 3억 8,900만 건으로, 2014년 추정치(1억 7,600만) 대비 121% 증가 확인. 시간 차이(40%)와 방법론 차이가 복합 작용
3. **ProQuest/EbscoHost 최초 추정**: ProQuest 19개 DB 선택 시 약 2억 8,000만 건, EbscoHost 25개 DB 선택 시 약 1억 300만 건
4. **7개 ASEBD에서 QHC의 타당성 검증**: 공식 규모 정보 또는 기존 연구와의 비교를 통해 BASE(정확 일치), CiteSeerX, EbscoHost, ProQuest, Q-Sensei Scholar, Scopus, Web of Science에서 QHC의 타당성 확인
5. **재현 가능한 방법론**: 공개된 쿼리를 사용하여 누구나 규모 정보를 업데이트할 수 있는 체계 제공

---

## How (방법론)

- **반복적 쿼리 최적화**: 5가지 쿼리 변형 카테고리(단일 문자, 숫자, 단어, ANSI 기호, 교차 조합 및 넓은 날짜 범위)를 반복적으로 테스트하여 각 ASEBD에서 최대 QHC를 식별
- **"직접 쿼리"와 "무의미 쿼리"**: Orduna-Malea et al.(2015)의 방법론을 계승·확장. "the", "a", "*", "1" 등 보편적 문자/기호를 사용하여 가능한 한 많은 레코드를 매칭
- **Google Scholar 특수 처리**: `1 -site:ssstfsffsdfasdfsf.com` 형태의 쿼리로 존재하지 않는 사이트를 제외하는 방식 적용 (Orduna-Malea et al. 방법론 기반)
- **타당성 검증**: (1) ASEBD 운영자의 공식 규모 정보와 비교, (2) 기존 학술 연구의 추정치와 비교. 단일 데이터베이스의 QHC가 공식 수치와 일치하면 다중 데이터베이스 QHC도 타당하다고 추론
- **데이터 수집 기간**: 2018년 1월~8월, Google Chrome 시크릿 모드에서 수행

---

## Originality (독창성)

- **최초의 대규모 비교 연구**: 12개 ASEBD를 단일 방법론으로 동시에 비교한 최초의 시도로, 기존의 개별적·쌍별 비교 연구의 한계를 극복
- **반복적 쿼리 최적화의 도입**: 기존의 단일 쿼리 접근법을 체계적인 반복적 탐색으로 확장하여, 더 높은 QHC를 식별할 수 있음을 입증
- **ProQuest/EbscoHost 규모의 최초 추정**: 구독 모델 기반 대형 애그리게이터의 규모를 처음으로 학술적으로 추정
- 다만, 핵심 방법론(QHC)은 기존 연구(Orduna-Malea et al., 2015; Vaughan & Thelwall, 2004)의 직접적 확장에 해당

---

## Limitation & Further Study (한계 및 향후 연구)

- **QHC의 본질적 한계**: QHC는 검색 시스템의 "최소 추정 규모"이며, 쿼리로 접근 불가능한 레코드는 체계적으로 배제됨. 중복 레코드 문제도 해결하지 못함
- **Google Scholar QHC의 불안정성**: 동일 쿼리에 대해 시간에 따라 QHC가 변동하여 "questionable"로 분류. 대형 검색 엔진의 분산 아키텍처에 기인할 가능성
- **4개 ASEBD 추정 실패**: AMiner, Microsoft Academic(QHC 미보고), Semantic Scholar(QHC가 공식 규모의 1/7), WorldWideScience(극도로 불안정)에서 QHC 방법 부적합
- **영어 편향**: 쿼리가 주로 영어 단어 기반이어 비영어 문서가 과소 대표될 가능성 (러시아어/중국어 추가 테스트에서 차이 없었으나 포괄적 검증은 아님)
- **시간적 스냅샷**: 2018년 1~8월 데이터로, ASEBD 규모는 지속적으로 변동. 종단적 추적 필요
- **품질 미평가**: 규모(quantity)만 측정하고, 문서의 품질, 고유성, 관련성 등은 평가하지 않음
- **향후 방향**: 종단적 규모 추적, 중복 레코드 비율 추정, 분야별 커버리지 비교, API 기반 자동화된 규모 모니터링 시스템 구축

---

## Evaluation (평가)

| 항목 | 점수 (1-10) | 비고 |
|------|:-----------:|------|
| **참신성 (Novelty)** | 6 | 기존 QHC 방법론의 확장이며, 반복적 최적화와 12개 ASEBD 동시 비교라는 규모가 차별점 |
| **기술적 깊이 (Technical Depth)** | 5 | 방법론이 본질적으로 쿼리 변형의 경험적 탐색에 의존하며, 통계적 엄밀성(신뢰구간, 반복 측정)이 부족 |
| **실용성 (Practicality)** | 8 | 도서관 사서, 정보 전문가, 체계적 문헌 리뷰 수행자에게 ASEBD 선택의 실질적 근거 제공. 재현 가능한 쿼리 공개 |
| **완성도 (Completeness)** | 7 | 12개 ASEBD 포괄, 상세한 타당성 검증, 쿼리별 결과 공개. 그러나 4개 ASEBD 추정 실패와 품질 차원 미평가가 한계 |
| **영향력 (Impact)** | 7 | Scientometrics 분야에서 널리 인용되는 참고 자료. Google Scholar 규모에 대한 기준점 재설정에 기여 |
| **종합 (Overall)** | **6.5** | 학술 정보 검색 생태계의 규모를 실증적으로 비교한 유용한 연구. 방법론의 한계(불안정한 QHC, 영어 편향)에도 불구하고, 12개 ASEBD를 체계적으로 비교한 실용적 가치가 높음 |
