# OpenAlex in Focus: Metadata Quality of Publication Type and Language Fields in an Open Peer Review Corpus

> **저자**: Guleda Dogan, Ayca Nur Sezen | **날짜**: 2026 | **DOI**: https://doi.org/10.47989/ir31iConf64207

---

## 핵심 요약
본 논문은 OpenAlex의 메타데이터 품질을, publication type과 language 필드를 중심으로 실증적으로 검증한다. Open peer review 관련 6,640개 레코드를 수동 검증한 결과, 43%에서 publication type 불일치, 3.3%에서 language 불일치가 발견되었으며, OpenAlex가 이질적인 문서 유형을 'Article'로 과도하게 분류하는 구조적 경향을 밝혔다.

## 연구 배경 및 동기
OpenAlex는 2022년 Microsoft Academic Graph(MAG)의 후속으로 출시된 무료 개방형 서지 데이터베이스로, bibliometric 연구와 scholarly communication 연구에 널리 사용된다. 그러나 기존 연구들이 OpenAlex의 institutional affiliation 누락, open access 상태 불일치, retracted publication 분류 오류 등의 메타데이터 한계를 보고해 왔다. Publication type과 language는 bibliometric 분석과 systematic review에서 필터링 및 eligibility 판단의 핵심 요소이므로, 이 필드의 정확성 검증이 필요했다.

## 방법론
- **데이터 수집**: 2024년 11월 26일 OpenAlex에서 'open peer review' full-text 검색 (9,275건)
- **필터링**: document type 기반 1차 필터링 후 7,090건, DOI 기반 중복 제거 후 6,640건
- **수동 검증**: 6,640건 전수에 대해 publication type과 language를 출판사 웹페이지와 대조하여 수동 확인
- **비교 분석**: Crossref의 document type 정보와 OpenAlex, 수동 분류 간 일치도 비교
- **분류 체계**: OpenAlex 원본 분류를 확장한 정교한 분류 체계 개발 (Article, Blog post, Book, Book chapter, Book review, Editorial, Peer review, Proceeding paper, Opinion/commentary, Report, Review, Thesis/Dissertation, Other)

## 주요 결과
- **Publication type 불일치**: 6,640건 중 2,878건(43%)에서 OpenAlex 분류와 수동 검증 결과가 불일치
- **'Article' 과분류**: 불일치 건 중 1,719건(60%)이 OpenAlex에서 'Article'로 분류되었으나, 실제로는 Other(43%), Opinion/Commentary(18%), Editorial(14%) 등으로 재분류
- **Preprint 오분류**: 795건의 preprint 오분류 중 51%가 실제로는 Article, 18.5%가 Review
- **Crossref와의 비교**: Crossref는 Article/Preprint 등 대범주에서 OpenAlex와 높은 일치율을 보이나, Peer Review(100% 수동 검증과 일치, OpenAlex와 0%)와 Proceeding Paper(68.4% 수동 검증과 일치, OpenAlex와 0%)에서 현저한 차이
- **Language 불일치**: 222건(3.3%)에서 language mismatch 발견, 그 중 51%가 영어로 잘못 표기된 비영어 논문

## 독창성 및 기여
- 6,640건 전수를 수동 검증하여 OpenAlex의 publication type 메타데이터 품질을 실증적으로 정량화한 점이 핵심 기여
- OpenAlex, Crossref, 수동 분류의 3자 비교를 통해 데이터베이스별 분류 체계의 차이와 한계를 구체적으로 규명
- 확장된 document type 분류 체계를 제안하여 OpenAlex의 'Article' 과분류 문제를 구조적으로 진단

## 한계 및 향후 연구
- **저자 언급 한계**: publication type과 language 두 필드에만 한정; open peer review라는 특정 주제 코퍼스로 일반화 제한; 수동 분류도 출판사 메타데이터에 의존하여 자체 오류 가능성; 2024년 11월 데이터로 이후 OpenAlex 업데이트 미반영
- **추가 지적**:
  - 비영어 문헌의 검증에 Google 번역과 ChatGPT를 사용하여 정확성에 의문
  - Open peer review라는 특수 주제로 인해 'Peer Review' 문서 유형의 오분류가 과대 대표되었을 가능성
  - 2024년 10월 OpenAlex rewrite 이후 개선 사항이 반영되지 않아 현재 시점의 타당성 확인 필요

## 평가
| 항목 | 점수 (1-5) |
|------|-----------|
| Novelty | 3 |
| Technical Soundness | 4 |
| Significance | 4 |
| Clarity | 4 |
| Overall | 4 |

**총평**: OpenAlex 메타데이터의 publication type 오류를 대규모 수동 검증으로 실증한 가치 있는 연구로, bibliometric 연구자들에게 데이터 전처리의 중요성을 환기시키며, 특히 43%라는 높은 불일치율은 OpenAlex 사용자들에게 실질적 경고를 제공한다.
