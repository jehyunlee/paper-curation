# Introducing the open biomedical map of science

> **저자**: Michael Ginda, Bruce W. Herr, Katy Börner | **날짜**: 2023-10-04 | **Journal**: Frontiers in Research Metrics and Analytics | **DOI**: [10.3389/frma.2023.1274793](https://doi.org/10.3389/frma.2023.1274793)
> **리뷰 모드**: Abstract only (PDF 없음)

---

## Essence

PubMed 데이터를 사용하여 생의학 분야에 특화된 오픈 과학 지도(Open Biomedical Map of Science, OBMS)를 만들 수 있는가? 저널과 MeSH(Medical Subject Headings) 디스크립터 간의 bimodal 네트워크 관계를 기반으로 OBMS 프로토타입을 구축했다. PubMed 저널과 2011년 UCSD 과학 지도의 저널을 비교하여 2009-2019년 기간의 분야별 커버리지 기준선을 확립했으며, 지도 포함을 위한 최소 인용 임계값도 분석했다. OBMS의 강점과 한계를 논의하고, 일반 무료 사용을 위한 다음 단계를 제시한다.

## Originality (Abstract 기반)

- [authorship, novelty, action] "This article introduces work in progress to develop a new, open biomedical map of science (OBMS) using the PubMed citation database."
- [novelty] "The new science map represents bimodal network relationships between journals and medical subject heading (MeSH) descriptors."
- [conclusion] "A prototype OBMS is presented, and we discuss the strengths and weaknesses of the OBMS, as well as the next steps for using and productizing this new open map."

## How (방법론)

- **데이터**: PubMed/MEDLINE 인용 데이터베이스 (2009-2019)
- **네트워크 구조**: 저널 ↔ MeSH 디스크립터 bimodal 네트워크 (저널의 MeSH 인덱싱 빈도 기반)
- **비교 기준**: 2011년 UCSD 과학 지도와의 저널 커버리지 비교
- **임계값 분석**: 지도 포함을 위한 최소 인용 수 요건 분석

## Why (중요성)

- 기존 과학 지도(UCSD 지도 등)는 특정 상업 데이터베이스에 의존하거나 생의학 분야의 세밀한 의미 구조(MeSH)를 충분히 활용하지 못함
- 오픈 데이터(PubMed)를 사용한 무료 생의학 과학 지도는 재현 가능하고 접근 가능한 연구 인프라 제공

## Limitation

- PubMed/MEDLINE은 생의학에 특화되어 있어 다학제적 연구나 타 분야와의 연결이 제한됨
- MeSH 디스크립터 기반 구조가 최신 연구 주제의 출현을 신속히 반영하지 못할 수 있음
- 프로토타입 단계로 실용화까지의 경로가 명확하지 않음

## Further Study

- OBMS를 완성하여 생의학 연구 커뮤니티에 공개 배포
- 시계열 OBMS 구축으로 생의학 지식 진화 추적
- PubMed 외 OpenAlex 등 타 오픈 데이터베이스와의 통합

## 평가

| 항목 | 점수 |
|------|------|
| Novelty | 3/5 |
| Technical Soundness | 3/5 |
| Significance | 3/5 |
| Clarity | 4/5 |
| Overall | 3/5 |

**총평**: PubMed와 MeSH를 활용한 오픈 생의학 과학 지도 개발의 초기 작업을 소개하는 논문으로, 오픈 사이언스 인프라 구축의 중요한 첫 걸음이나 아직 프로토타입 단계의 기여에 그친다.
