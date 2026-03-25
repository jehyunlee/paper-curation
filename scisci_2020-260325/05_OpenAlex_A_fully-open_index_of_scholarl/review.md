# OpenAlex: A fully-open index of scholarly works, authors, venues, institutions, and concepts

> **저자**: Jason Priem, Heather Piwowar, Richard Orr | **날짜**: 2022 | **Journal**: STI Conference 2022 (arXiv: 2205.01833) | **DOI**: -

---

## Essence

OpenAlex는 Microsoft Academic Graph(MAG) 중단에 대응하여 만들어진 **완전 오픈(100% open data, open API, open-source code)** 학술 지식 그래프로, 약 2억 900만 편의 학술 저작물(works), 2억 1,300만 명의 저자(authors), 12만 4,000개의 출판 매체(venues), 10만 9,000개의 기관(institutions), 6만 5,000개의 개념(concepts)을 색인하며, 매일 약 5만 건의 새로운 저작물이 추가된다.

## Motivation

- **알려진 것**: 학술 메타데이터는 연구 평가, 탐색, 발견의 핵심 인프라이며, MAG는 무료로 널리 사용되던 Scientific Knowledge Graph(SKG)였다.
- **문제**: 2021년 5월 Microsoft가 MAG 지원 중단을 발표하면서, 기존 시스템으로는 대체가 어렵다는 우려가 제기되었다.
- **왜 중요한가**: Scopus, Web of Science 등 기존 유료 데이터베이스는 접근 비용이 높고 폐쇄적이어서, 연구 평가의 투명성과 재현성을 저해한다.
- **접근법**: MAG의 데이터를 계승·확장하면서 완전 오픈 원칙을 적용한 새로운 SKG를 구축하여, 2022년 1월 1일 MAG 퇴역과 동시에 출시했다.

## Achievement

1. **대규모 오픈 데이터셋 구축**: Works 2억 900만 건, Authors 2억 1,300만 명, Venues 12만 4,000개, Institutions 10만 9,000개, Concepts 6만 5,000개를 포함하는 이종 유향 그래프(heterogeneous directed graph) 구축.
2. **다중 접근 채널 제공**: 전체 데이터 덤프(격주 갱신), REST API(일일 갱신, 등록 불필요, 속도 제한 없음), 웹 GUI의 세 가지 무료 접근 방식 제공.
3. **표준 외부 ID 연동**: Works에 DOI(약 50% 보유), Authors에 ORCID, Venues에 ISSN-L(약 90%), Institutions에 ROR ID(약 94%), Concepts에 Wikidata ID(100%)를 매핑하여 상호운용성 극대화.
4. **자동 엔티티 연결**: 저자-기관-저작물 간 3자 관계를 "authorship" 객체로 공식화하고, 규칙 기반 + 머신러닝 2단계 알고리즘으로 소속기관 문자열을 파싱·정규화·ROR 연결.
5. **완전 오픈소스**: 코드, 분류 모델, 데이터 전체가 오픈소스이며, OurResearch(비영리단체)가 POSI 원칙에 따라 지속가능하게 운영.

## How

- **데이터 소스**: Crossref, PubMed, arXiv, 기관/분야별 리포지토리, MAG(과거 저작물)
- **엔티티 구조**: 5종류 엔티티(Works, Authors, Venues, Institutions, Concepts)와 연결 관계로 구성된 이종 유향 그래프
- **저자 동명이인 해소**: ORCID + 출판 이력 + 인용 이력을 활용한 알고리즘적 저자 구분
- **기관 매칭**: 소속 문자열 파싱 후 규칙 기반 + ML 2단계 알고리즘으로 ROR ID 매핑
- **개념 분류**: MAG 코퍼스로 학습한 자동 분류기가 제목·초록 기반으로 개념 태깅 (85% 커버리지)
- **버전 매칭**: 프리프린트와 출판 버전을 fingerprinting 알고리즘으로 매칭, Version of Record(VoR) 플래그 지정

## Originality

- **MAG의 완전 오픈 후계자**: MAG 중단이라는 위기를 100% 오픈(데이터+API+코드) 원칙으로 해결한 최초의 대규모 SKG.
- **POSI 원칙 조기 채택**: 학술 오픈 인프라의 지속가능성 원칙(Principles of Open Scholarly Infrastructure)을 적극 준수하며 운영.
- **통합적 엔티티 모델**: Works, Authors, Venues, Institutions, Concepts의 5종 엔티티를 하나의 그래프로 통합하고, 각각에 Canonical External ID를 부여하여 외부 시스템과의 상호운용성을 체계화.

## Limitation & Further Study

### 저자들이 언급한 한계
- 저자 및 기관의 파싱·정규화·동명이인 해소가 아직 개선 중이며, 고위험 평가 맥락에서 사용될 경우 오류의 현실적 영향이 우려된다.
- 펀딩 소스(funding sources) 및 교신저자(corresponding author) 메타데이터가 아직 누락되어 있다.
- 데이터셋의 완전성과 정확성에 대한 체계적 검증이 부족하며, 유사 도구와의 비교 연구가 필요하다.

### 리뷰어 판단 아쉬운 점
- **정량적 품질 평가 부재**: 저자 동명이인 해소 정확도, 기관 매칭 정밀도/재현율, 개념 분류 성능 등에 대한 벤치마크 수치가 전혀 제시되지 않았다. 4페이지 컨퍼런스 페이퍼 특성상 불가피하나, 신뢰성 판단이 어렵다.
- **비영어권 커버리지**: 비영어권 저널, 기관, 저자에 대한 커버리지와 정확도가 영어권 대비 어떠한지에 대한 논의가 없다.
- **지속가능성 모델**: Arcadia 재단 펀딩에 의존하고 있으나, 장기 재정 지속가능성에 대한 구체적 로드맵이 제시되지 않았다.

### 후속 연구
- Scopus, Web of Science, Semantic Scholar 등과의 체계적 커버리지·정확도 비교 연구가 필요하다.
- 저자 동명이인 해소 알고리즘의 정밀도/재현율 벤치마킹 및 비영어권 데이터에 대한 성능 평가가 요구된다.
- OpenAlex 기반 계량서지학(bibliometrics) 연구의 재현성과 타당성을 검증하는 메타 연구가 가능하다.

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 3/5 |
| Technical Soundness | 3/5 |
| Significance | 5/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: MAG 중단이라는 학술 인프라 위기에 대한 시의적절하고 실용적인 해법으로, 완전 오픈 원칙과 대규모 데이터 커버리지의 조합이 학술 커뮤니티에 막대한 영향을 미치고 있으나, 기술적 상세와 품질 검증이 짧은 컨퍼런스 논문 형식의 한계로 부족하다.
