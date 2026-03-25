# OpenAlex in focus: Metadata quality of publication type and language fields in an open peer review corpus

> **저자**: Güleda Dogan, Ayca Nur Sezen | **날짜**: 2026-03-20 | **DOI**: 10.47989/ir31iconf64207

---

## 핵심 요약
본 연구는 OpenAlex 데이터베이스의 메타데이터 품질을 출판물 유형(publication type)과 언어(language) 필드를 중심으로 평가한다. Open peer review 관련 6,640건의 레코드를 수동 검증한 결과, 43%(2,878건)에서 출판물 유형 불일치가, 3.3%(222건)에서 언어 불일치가 발견되었으며, 'Article'이 가장 빈번하게 오분류된 유형이었다.

## 연구 배경 및 동기
OpenAlex는 Microsoft Academic Graph의 후속으로 2022년에 출범한 무료 학술 데이터베이스로, 광범위한 커버리지와 개방성으로 bibliometric 연구에 널리 활용되고 있다. 그러나 기관 소속 누락, OA 상태 불일치, 철회 논문 오분류 등 메타데이터 한계가 보고되어 왔다. 문서 유형과 언어는 체계적 리뷰와 bibliometric 분석의 필터링/적격 기준에 직접 영향을 미치므로, 이 필드들의 정확성 검증이 필수적이다.

## 방법론
- **데이터**: OpenAlex에서 "open peer review" 전문 검색으로 9,275건 수집, 필터링 및 중복 제거 후 6,640건
- **수동 검증**: 각 레코드의 출판물 유형과 언어를 출판사 웹사이트 정보와 대조하여 수동 확인
- **분류 체계**: OpenAlex 원래 분류보다 세분화된 체계 개발(article, blog post, book, book chapter, book review, editorial, peer review, proceeding paper, opinion/commentary, report, review, thesis/dissertation, other)
- **Crossref 비교**: OpenAlex 할당 유형, 수동 검증 유형, Crossref 유형 간 일치도 비교

## 주요 결과
- 6,640건 중 2,878건(43%)에서 출판물 유형 불일치 발견
- 오분류의 60%(1,719건)가 OpenAlex에서 'Article'로 할당된 레코드 — 이 중 43%가 'Other', 18%가 'Opinion/Commentary', 14%가 'Editorial'로 재분류
- 'Preprint'으로 분류된 795건 중 51%가 실제로는 'Article', 18.5%가 'Review'
- 'Review'로 분류된 298건 중 66%가 실제로는 'Peer Review' 보고서
- 222건(3.3%)의 언어 불일치 — 대부분 비영어 문헌에 영어 라벨이 잘못 할당
- Crossref는 광범위 카테고리에서 OpenAlex와 유사하지만, 수동 검증과는 상당한 차이

## 독창성 및 기여
OpenAlex의 출판물 유형 및 언어 메타데이터의 정확성을 대규모(6,640건) 수동 검증으로 실증적으로 평가한 연구이다. 43%라는 높은 유형 오분류율은 OpenAlex 기반 연구에서 체계적 전처리와 검증의 필수성을 강력히 시사하며, 세분화된 분류 체계를 제안한 점도 실용적 기여이다.

## 한계 및 향후 연구
- Open peer review라는 특정 주제의 코퍼스에 한정되어 일반화에 제한
- 수동 검증 자체의 주관성과 오류 가능성
- 출판사 웹사이트 정보를 ground truth로 사용하였으나, 이 역시 불완전할 수 있음
- 다른 메타데이터 필드(저자, 기관, OA 상태 등)는 미분석
- 향후 다양한 학문 분야와 주제에 걸친 메타데이터 품질 평가 확장 필요

## 평가
| 항목 | 점수 |
|------|------|
| Novelty | 3/5 |
| Technical Soundness | 4/5 |
| Significance | 3/5 |
| Clarity | 4/5 |
| Overall | 3/5 |

**총평**: OpenAlex 메타데이터의 실질적 품질 문제를 정량적으로 드러낸 실용적 연구로, 해당 데이터베이스를 활용하는 모든 연구자에게 중요한 경고와 지침을 제공한다.
