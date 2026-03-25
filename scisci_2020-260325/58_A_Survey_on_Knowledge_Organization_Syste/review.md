# A Survey on Knowledge Organization Systems of Research Fields: Resources and Challenges

> **저자**: Angelo Salatino, Tanay Aggarwal, Andrea Mannocci, Francesco Osborne, Enrico Motta | **날짜**: 2025-06-20 | **Journal**: Quantitative Science Studies | **DOI**: 10.1162/qss_a_00363

---

## Essence

학술 분야의 Knowledge Organization Systems(KOSs) -- 용어 목록, 분류 체계(taxonomy), 시소러스(thesaurus), 온톨로지(ontology) -- 에 대한 최초의 체계적 서베이로, 45개 KOS를 scope, structure, curation, external links, usage의 5가지 차원과 15개 세부 특성으로 분석했다. 19개 주요 학문 분야 중 7개("History", "Political Science", "Environmental Science", "Material Science", "Geography", "Sociology", "Business")에는 전용 KOS가 존재하지 않으며, 포괄적이면서 세분화되고 지속 관리되며 개방적인 multi-field KOS는 현재 없다는 것이 핵심 발견이다.

## Motivation

학술 출판물의 기하급수적 증가, Open Science의 부상, 학제 간 연구의 확대, LLM 기반 AI 시스템의 등장으로 인해 연구 분야를 체계적으로 조직하는 KOS의 중요성이 더욱 커지고 있다. KOS는 디지털 도서관의 문서 검색, 연구 영향력 분석, 연구 동향 예측 등 다양한 AI 기반 시스템의 핵심 인프라로 기능한다. 그러나 기존 KOS들은 scope, 규모, 품질, 활용도 면에서 매우 이질적이며, 이들에 대한 체계적 비교 분석이 부재했다. 특히 COVID-19 팬데믹 시기의 논문 홍수 경험은 견고한 연구 개념 표현 체계의 필요성을 절실하게 보여주었다.

## Achievement

1. **45개 KOS의 체계적 식별 및 분류**: 7단계 검색 전략(Google Scholar, 출판사 웹사이트, Google 검색, 전문가 자문, Wikipedia, KOS 간 상호참조, 분야별 교수 접촉)을 통해 단일 분야 23개, 다분야 22개 KOS를 식별
2. **구조적 다양성 규명**: 개념 수 48개(OECD FORD)에서 1,300만 개(BioPortal), 깊이 1단계(WoS Categories)에서 39단계(OBO)까지 극단적 편차 확인; taxonomy 23개, ontology 18개, thesaurus 3개, term list 1개의 분포
3. **분야별 커버리지 격차 발견**: 7개 주요 학문 분야에 전용 KOS 부재; Medicine(4개), Computer Science(3개) 등 일부 분야는 과잉 커버리지
4. **큐레이션 패턴 분석**: 32개 KOS가 수작업 생성, 6개 반자동, 2개 자동 생성; 18개가 연 1회 이상 업데이트; 26개가 오픈 라이선스; 35개가 영어 전용
5. **통합 KOS의 부재 확인**: 5개 multi-field KOS만이 19개 분야 전체를 커버하나, 포괄성-세분화-지속 관리-개방성 4가지를 모두 충족하는 시스템은 없음
6. **8가지 핵심 도전과제 식별**: 포괄적 KOS 구축, KOS 통합, 다국어 확장, 전문가 불일치 해소, 품질 평가, 모호한 라벨 처리, 자동 생성/업데이트, 대규모 자동 분류

## How

- **검색 전략**: 7단계 체계적 검색 -- Google Scholar 쿼리, 출판사/데이터베이스 웹사이트 분석(Scopus, WoS, OpenAlex, PubMed 등), Google 검색(19개 분야별 조합), 전문가 자문, Wikipedia 링크 추적, KOS 간 상호참조, 누락 분야 교수 접촉
- **분석 프레임워크**: Scope(분야 커버리지), Structure(유형, 개념 수, 깊이, 계층 종류, 관련 용어), Curation(생성 방식, 포맷, 라이선스, 업데이트 빈도, 언어, 관리자), External Links(외부 KOS 연결), Usage(디지털 도서관 활용)의 5차원 15개 특성
- **데이터 추출**: RDF 등 표준 포맷의 KOS는 Python 스크립트로 자동 추출(GitHub 공개), HTML/PDF만 제공하는 KOS는 수작업 추출
- **포함/배제 기준**: 학술 연구 토픽 기술, 19개 주요 분야 중 1개 이상 커버, 주요 서지 DB 또는 학술 커뮤니티 활용 필수; 영어 미지원 및 특정 도서관 전용은 배제

## Originality

학술 분야 KOS에 대한 최초의 체계적이고 포괄적인 서베이라는 점 자체가 핵심 기여이다. 기존에는 개별 KOS에 대한 설명이나 특정 분야 내 비교는 있었으나, 45개 KOS를 통일된 프레임워크(5차원 15개 특성)로 분석한 시도는 없었다. 특히 분야별 커버리지 격차를 체계적으로 드러내고, 포괄적-세분화-지속관리-개방형 KOS의 부재라는 핵심 문제를 명확히 정의한 점, 그리고 EuroVoc 기반의 통합 경로를 제안한 점이 실질적 기여이다. Open Science 원칙에 따라 분석 코드와 데이터를 모두 공개한 것도 재현 가능성 측면에서 의미가 있다.

## Limitation & Further Study

### 저자들이 언급한 한계

- 검색 엔진이나 쿼리 용어의 한계로 일부 관련 KOS가 누락되었을 가능성
- 영어 미지원 KOS 배제로 비영어권 KOS의 대표성 부족
- 개별 도서관 전용 KOS 배제로 전체 KOS 생태계의 일부만 반영
- KOS의 "품질"에 대한 보편적 정의 부재로 품질 평가 미수행
- KOS의 동적 특성으로 인해 분석 시점(2024년 4월) 이후 변화 미반영

### 리뷰어 판단 아쉬운 점

- **정량적 비교의 한계**: KOS 간 개념 중복도나 커버리지 겹침에 대한 정량적 분석이 부족 -- 예를 들어, MeSH와 UMLS의 실제 개념 겹침률 등
- **사용자 관점 부재**: KOS의 실제 사용 경험이나 사용자 만족도에 대한 조사가 없어, 기술적 특성과 실질적 유용성 간 연결이 약함
- **LLM과의 관계 피상적**: LLM이 KOS를 대체하거나 보완할 수 있는 가능성에 대한 논의가 미래 방향에서 간략히 언급될 뿐 심층 분석이 없음
- **자동 생성 KOS의 품질**: Computer Science Ontology 등 자동 생성 KOS와 수작업 KOS 간 품질 비교가 부재
- **시간적 진화 분석 부족**: KOS의 역사적 진화와 개념 변화 추이에 대한 종단적 분석이 없음

### 후속 연구

- EuroVoc 기반 통합 KOS 프로토타입 구축 및 평가
- LLM 활용 KOS 자동 생성 및 업데이트 파이프라인 개발
- KOS 간 자동 매핑의 정확도 향상을 위한 deep learning 기반 방법론 연구
- 7개 미커버 분야(History, Political Science 등)에 대한 전용 KOS 개발
- KOS 품질 평가를 위한 표준화된 벤치마크 및 메트릭 개발

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 4/5 |
| Significance | 4/5 |
| Clarity | 5/5 |
| Overall | 4/5 |

**총평**: 학술 분야 KOS 생태계에 대한 최초의 체계적 서베이로서 45개 시스템을 통일된 프레임워크로 분석하고 핵심 격차와 도전과제를 명확히 정의한 기여가 크지만, 정량적 비교와 LLM 시대의 KOS 역할에 대한 심층 논의가 보완되면 더 큰 영향력을 가질 수 있다.
