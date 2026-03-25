# OpenAlex in focus: Metadata quality of publication type and language fields in an open peer review corpus

> **저자**: Güleda Dogan, Ayça Nur Sezen | **날짜**: 2026-03-20 | **Journal**: Information Research | **DOI**: 10.47989/ir31iconf64207

---

## Essence
OpenAlex의 출판 유형 및 언어 메타데이터는 얼마나 정확한가? 6,640건의 오픈 피어리뷰 관련 논문을 수동 검증한 결과, **43%(2,878건)에서 출판 유형 불일치**, **3.3%(222건)에서 언어 불일치**가 발견되었다. 가장 큰 문제는 'Article' 라벨의 과용으로, 실제로는 Editorial, Opinion/Commentary, 기타 유형인 자료들이 모두 'Article'로 분류되어 있었다. Crossref 유형과 비교 시 Peer Review와 Proceeding Paper 범주에서 OpenAlex와의 괴리가 특히 컸다.

## Motivation
OpenAlex는 MAG의 후속으로 무료 대규모 학술 데이터베이스로서 계량서지학 연구에 널리 사용되고 있다. 그러나 메타데이터의 정확성에 대한 우려가 지속적으로 제기되어 왔으며, 특히 문서 유형과 언어 필드는 체계적 리뷰와 계량서지학 분석에서 포함/제외 기준으로 직접 사용되므로, 이들의 정확성이 하류 분석의 타당성에 직결된다.

## Achievement
1. 출판 유형 불일치 **43%**: 오분류 중 60%가 'Article'로 잘못 배정 — 이 중 43%는 기타(Other), 18%는 Opinion/Commentary, 14%는 Editorial
2. 'Preprint' 라벨 오류: 795건 중 51%가 실제로는 Article, 18.5%가 Review
3. 'Review' 라벨 오류: 298건 중 66%가 실제로는 Peer Review 보고서
4. 언어 불일치 **3.3%**: 51%가 영어로 잘못 표시된 비영어 자료 (스페인어 21건, 포르투갈어 17건, 독일어 14건)
5. Crossref는 Peer Review(100% 수동 검증과 일치)와 Proceeding Paper(68.4%)에서 OpenAlex보다 정확

## How
- **데이터**: OpenAlex에서 'open peer review' 검색 → 9,275건 → 필터링/중복 제거 후 6,640건
- **검증**: 출판사 웹사이트 대조를 통한 수동 검증 (출판 유형 및 언어)
- **비교**: OpenAlex, Crossref, 수동 검증 3자 비교
- **분류 체계**: 13개 범주의 정제된 출판 유형 분류 체계 개발

## Originality
- OpenAlex의 출판 유형 메타데이터를 **대규모(6,640건) 수동 검증**으로 체계적으로 평가
- OpenAlex, Crossref, 수동 검증 간 **3자 비교** 수행
- 메타데이터 품질 문제의 구체적 패턴과 규모를 정량적으로 제시

## Limitation & Further Study
### 저자들이 언급한 한계
- 두 가지 메타데이터 필드(출판 유형, 언어)만 분석
- 오픈 피어리뷰 코퍼스에 한정되어 일반화 제한
- 수동 분류가 출판사 제공 정보에 의존

### 리뷰어 판단 아쉬운 점
- 오픈 피어리뷰라는 특수 분야의 코퍼스로, 일반적인 OpenAlex 메타데이터 품질을 대표하기 어려움
- 'Peer Review' 유형이 다수 포함된 코퍼스 특성이 오분류 비율을 높였을 가능성
- 개선 방안이나 자동 품질 관리 방법론 제안이 없음

### 후속 연구
- 다양한 분야의 코퍼스로 확대 검증
- 자동화된 메타데이터 품질 관리 도구 개발
- OpenAlex의 분류 알고리즘 개선 제안

## Evaluation
| 항목 | 점수 |
|------|------|
| Novelty | 3/5 |
| Technical Soundness | 4/5 |
| Significance | 3/5 |
| Clarity | 4/5 |
| Overall | 3/5 |

**총평**: OpenAlex 메타데이터의 구체적 품질 문제를 체계적으로 문서화한 유용한 연구로, 계량서지학 연구자들에게 데이터 전처리의 중요성을 환기시킨다.
