# BibFusion: A Python Package to Integrate, Deduplicate, and Harmonize Exported Bibliographic Records from Scopus and Web of Science for Bibliometric Analysis

> **저자**: Angelo Britto, Sebastian Robledo, Martha Zuluaga | **날짜**: 2026-02-15 | **DOI**: 10.47909/ijsmc.342

---

## 핵심 요약
본 논문은 Scopus와 Web of Science(WoS)의 서지 데이터를 통합, 중복 제거, 정규화하여 분석 가능한 단일 코퍼스를 생성하는 Python 패키지 BibFusion을 소개한다. DOI 기반 1차 매칭과 보수적 fallback 전략, OpenAlex를 통한 식별자 보강, 그리고 canonical PersonID 기반 저자 동음이의어 해소를 핵심 기능으로 하며, 7개의 관계형 엔티티 테이블과 감사 추적(audit artifact)을 산출한다.

## 연구 배경 및 동기
Bibliometric 분석의 신뢰성은 서지 메타데이터의 일관성에 의존하지만, Scopus와 WoS는 coverage, export 구조, 필드 완전성에서 상이하여 중복, 저자명 변이, 불완전한 소속 정보, 비표준화된 인용 문자열 등의 문제를 야기한다. 기존 도구들(bibliometrix, VOSviewer, CiteSpace 등)은 데이터 시각화와 분석에 강점이 있으나, 크로스 데이터베이스 통합 전처리에서는 별도의 수작업이 필요했다. 특히 (i) 명시적 entity-relationship(ER) 모델로 통합 결과를 구조화하고, (ii) 병합/동음이의어 해소 결정을 감사 가능하게 문서화하는 도구가 부재했다.

## 방법론
- **입력**: Scopus CSV + WoS TXT (full record with cited references)
- **정규화**: ASCII/대문자 표준화, SR/SR_ref 키 정리, 소속 파싱 및 국가 추출
- **OpenAlex 보강** (선택적): DOI 기반 resolution으로 OpenAlex work ID, ORCID, OpenAlexAuthorID 복구
- **중복 제거**: DOI-first matching cascade + 보수적 fallback (title-year-first author)
- **저자 동음이의어 해소**: canonical PersonID 계층 (ORCID > OpenAlexAuthorID > normalized name)
- **인용 정리**: malformed reference 필터링, SR/SR_ref 키 재매핑
- **저널 통합**: ISSN/EISSN 규칙 기반 저널/Scimago 정보 병합
- **출력**: 7개 관계형 CSV (Articles, Authors, ArticleAuthor, Citation, Affiliation, Journal, Scimagodb) + 감사 파일
- **시연**: "entrepreneurial marketing" 검색으로 436개 원본 -> 253개 고유 main works, 8,569개 통합 레코드

## 주요 결과
- 253개 main records 중 72.3%(183건)가 양 DB에 존재, 23.3% Scopus 전용, 4.3% WoS 전용
- Main records의 DOI 커버리지: 87% (양 DB 결합 시 98.9%)
- 17,219명의 동음이의어 해소된 저자, 24,392개의 방향성 인용 엣지, 34,488개의 소속 인스턴스 생성
- DOI-first 전략으로 중복 인플레이션과 메타데이터 단편화를 효과적으로 감소

## 독창성 및 기여
- Scopus-WoS 통합을 명시적 ER 모델로 구조화하여 7개의 관계형 엔티티로 출력하는 최초의 Python 패키지
- 감사 추적(aliases, potential conflicts, merge logs)을 통한 투명성 확보 - 기존 도구 대비 차별점
- OpenAlex 기반 식별자 보강과 canonical PersonID 계층을 결합한 저자 동음이의어 해소
- Cited reference 수준의 정리와 재매핑으로 citation network 분석의 신뢰성 향상

## 한계 및 향후 연구
- **저자 언급 한계**: OpenAlex 보강은 DOI 유효성에 의존; 외부 API rate limit에 의한 대규모 처리 제약; ORCID/OpenAlexAuthorID 커버리지가 불완전한 경우 저자 동음이의어 해소 한계
- **추가 지적**:
  - "entrepreneurial marketing"이라는 단일 검색어로만 시연하여 다양한 분야에서의 일반화 검증 부족
  - Scopus와 WoS 두 DB에만 한정 - Dimensions, Semantic Scholar 등 다른 DB와의 통합 미지원
  - Title-year-first author fallback 매칭의 false positive/negative 비율에 대한 정량적 평가 부재
  - 논문이 지나치게 서술적(descriptive)이며, 기존 도구(bibliometrix의 mergeDbSources 등)와의 정량적 성능 비교 없음
  - 코드의 실제 사용 편의성(API 설계, 에러 처리 등)에 대한 논의 부족

## 평가
| 항목 | 점수 (1-5) |
|------|-----------|
| Novelty | 3 |
| Technical Soundness | 3 |
| Significance | 3 |
| Clarity | 3 |
| Overall | 3 |

**총평**: Scopus-WoS 통합의 실질적 필요성을 다루는 유용한 소프트웨어 기여이나, 단일 사례 시연에 그치고 기존 도구와의 정량적 비교가 없어 실질적 우위를 입증하지 못하며, 논문의 서술이 반복적이고 기술적 깊이가 부족하다.
