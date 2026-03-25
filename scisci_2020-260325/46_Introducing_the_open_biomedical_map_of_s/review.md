# Introducing the open biomedical map of science

> **저자**: Michael Ginda, Bruce W. Herr II, Katy Börner | **날짜**: 2023-10-04 | **Journal**: Frontiers in Research Metrics and Analytics | **DOI**: 10.3389/frma.2023.1274793

---

## Essence
상업적 데이터에 의존하지 않는 공정(FAIR)한 생의학 과학 지도를 만들 수 있는가? PubMed 인용 데이터베이스와 MeSH 통제어휘를 사용하여, 저널과 MeSH 디스크립터 간 이모드 네트워크를 구축하고 ZMLT 알고리즘으로 지도화한 결과, **오픈 생의학 과학 지도(OBMS)** 프로토타입이 완성되었다. PubMed에 인덱싱된 18,234개 저널 중 34.6%가 UCSD 과학 지도와 겹쳤으며, MEDLINE에 최소 20편 이상 인덱싱된 8,209개 저널이 지도에 포함되었다.

## Motivation
기존 과학 지도들(UCSD map, VOSviewer 등)은 Web of Science, Scopus 등 상업적 데이터에 기반하여 타 팀에서 재현하거나 자유롭게 수정할 수 없다. FAIR 원칙(Findability, Accessibility, Interoperability, Reusability)을 충족하는 과학 지도가 존재하지 않았다. PubMed은 무료 공개 데이터베이스로서 MeSH 통제어휘라는 개방형 분류 체계를 사용하므로, FAIR 과학 지도 구축의 유력한 기반이 될 수 있었다.

## Achievement
1. PubMed/MEDLINE 데이터로 **최초의 FAIR 원칙 준수 생의학 과학 지도** 프로토타입 구축
2. PubMed 저널과 UCSD 과학 지도 간 **34.6% 겹침** 확인 — 주로 의학·보건·사회과학
3. MEDLINE 인덱싱 기준 **최소 20편 임계값** 설정 → 8,209개 저널 포함
4. 저널-MeSH 이모드 네트워크 → ZMLT 알고리즘 기반 **인터랙티브 지도** 생성 (map4sci 소프트웨어)
5. PubMed의 학문 분야 커버리지 분석: 의학·보건 중심, 인문학·생명공학·지구과학 취약

## How
- **데이터**: PubMed 데이터베이스 (2022년 8월 쿼리), 18,234개 저널, 11,990,394편 논문 (2009-2019)
- **네트워크**: 비방향 가중 이모드 네트워크 — 저널(source) ↔ MeSH 디스크립터(target), 가중치 = 논문 수
- **필터링**: 저널당 상위 50개 MeSH 디스크립터만 유지
- **레이아웃**: ZMLT(Zoomable Multi-Level Tree) 알고리즘
- **비교**: UCSD 과학 지도(2011)의 저널 분류와 대조

## Originality
- PubMed + MeSH 기반 **최초의 오픈(FAIR) 과학 지도** 시도
- map4sci 소프트웨어를 통한 **인터랙티브 탐색** 기능
- 오픈 데이터만으로 상업적 데이터 기반 지도와 비교 가능한 품질 달성 가능성 탐색

## Limitation & Further Study
### 저자들이 언급한 한계
- 프로토타입 단계로 최종 버전이 아님
- PubMed의 생의학 편중 — 자연과학·공학·인문학 커버리지 제한
- MeSH 디스크립터가 MEDLINE 인덱싱 저널에만 적용

### 리뷰어 판단 아쉬운 점
- "Brief Research Report" 형식으로 방법론과 결과의 깊이가 매우 제한적
- 생성된 지도의 **타당성 검증**이 부족 — UCSD 지도와의 커버리지 비교만으로는 지도의 정확성을 판단하기 어려움
- 기존 오픈 소스(OpenAlex 등)와의 비교 없음
- 상위 50 MeSH 필터링의 근거가 불충분

### 후속 연구
- 최종 OBMS 완성 (2013-2022 기간)
- OpenAlex 등 다른 오픈 데이터와의 통합
- 사용자 평가 및 유즈케이스 시연
- 시간적 동태를 포함한 동적 지도

## Evaluation
| 항목 | 점수 |
|------|------|
| Novelty | 3/5 |
| Technical Soundness | 2/5 |
| Significance | 3/5 |
| Clarity | 4/5 |
| Overall | 3/5 |

**총평**: FAIR 원칙에 부합하는 오픈 과학 지도의 필요성과 가능성을 제시한 의미 있는 초기 시도이나, 프로토타입 수준으로 타당성 검증과 완성도 면에서 개선이 필요하다.
