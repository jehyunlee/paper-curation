# SciSciNet: A large-scale open data lake for the science of science research

> **저자**: Zihang Lin, Yian Yin, Lu Liu, Dashun Wang | **날짜**: 2023-06-01 | **Journal**: Scientific Data | **DOI**: [10.1038/s41597-023-02198-9](https://doi.org/10.1038/s41597-023-02198-9)
> **리뷰 모드**: Abstract only (PDF 없음)

---

## Essence

Science of Science 연구에서 데이터 접근성과 중복 처리 문제를 어떻게 해결하는가? **1억 3천 4백만 건** 이상의 과학 논문과 펀딩, 공공 활용 분야의 외부 링크 수백만 건을 포함하는 **SciSciNet**을 구축·공개했다. 단순 데이터 제공을 넘어, 전처리 단계와 분석 선택을 상세히 문서화하고, 문헌에서 자주 사용되는 측정 지표들을 미리 계산하여 제공함으로써 연구자들의 진입 장벽을 낮추고 결과의 강건성과 재현성을 높이는 것을 목표로 한다.

## Originality (Abstract 기반)

- [authorship, novelty, action] "Here we present SciSciNet, a large-scale open data lake for the science of science research, covering over 134M scientific publications and millions of external linkages to funding and public uses."
- [novelty] "We offer detailed documentation of pre-processing steps and analytical choices in constructing the data lake."
- [novelty] "We further supplement the data lake by computing frequently used measures in the literature."

## How (방법론)

- **규모**: 1억 3,400만+ 논문, 펀딩 데이터, 공공 활용(특허, 정책 문서 등) 링크 수백만 건
- **구축 과정**: 복수 출처 데이터 통합, 중복 제거, 식별자 매핑(DOI, PubMed ID 등)
- **사전 계산 지표**: CD index, disruption, novelty, team size 등 과학학 연구에서 자주 쓰이는 지표들 미리 계산 제공
- **접근 방식**: Scientific Data 표준에 따른 데이터 설명서 및 코드 공개

## Why (중요성)

- Science of Science 연구자들이 각자 같은 데이터를 독립적으로 처리하는 비효율과 전처리 방법 차이로 인한 결과 불일치 문제를 해소
- 데이터 접근 장벽을 낮춰 더 다양한 연구자가 대규모 과학학 연구에 참여할 수 있도록 함

## Limitation

- 1억 3천만 건의 데이터에서 메타데이터 품질(저자 disambiguation, 소속 기관 등)의 불균등성이 있을 수 있음
- 사전 계산 지표는 특정 분석 선택을 반영하므로, 연구자가 다른 설정을 원할 경우 재계산 필요
- 데이터 업데이트 주기와 장기 유지 관리 계획이 중요한 과제

## Further Study

- SciSciNet 기반의 분야 간 비교 연구 및 시계열 분석 촉진
- 사용자 기여형 지표 계산 확장으로 집단적 데이터 보강
- 오픈 사이언스 인프라로서 다른 데이터 레이크(OpenAlex, Semantic Scholar)와의 연동

## 평가

| 항목 | 점수 |
|------|------|
| Novelty | 3/5 |
| Technical Soundness | 4/5 |
| Significance | 5/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: Science of Science 분야의 인프라 논문으로, 1억 3천만 건의 논문 데이터와 미리 계산된 핵심 지표들을 오픈 데이터로 제공함으로써 분야 전체의 연구 효율성과 재현성을 획기적으로 높이는 공공재적 기여를 한다.
