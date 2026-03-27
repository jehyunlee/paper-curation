# Design and Update of a Classification System: The UCSD Map of Science

> **저자**: Katy Börner, Richard Klavans, Michael Patek, Angela M. Zoss, Joseph R. Biberstine, Robert P. Light, Vincent Larivière, Kevin W. Boyack | **날짜**: 2012 | **Journal**: PLoS ONE | **DOI**: [10.1371/journal.pone.0039464](https://doi.org/10.1371/journal.pone.0039464) | **arXiv**: N/A
> **리뷰 모드**: Web-only

---

## Essence

UCSD 과학 지도(Map of Science)는 약 2,500만 편 논문의 인용 관계를 기반으로 과학 전체를 13개 주요 분야, 554개 세부 분야 클러스터로 시각화한 글로벌 과학 분류 시스템이다. Börner et al.(2012)은 이 지도의 설계 원칙과 2009–2011년 업데이트 과정을 기술하며, 연구 포트폴리오 분석, 정책 평가, 과학 나침반(science compass)으로의 활용 방법을 제시한다.

## Originality (Abstract 기반)

- [authorship, action] "We present the design and update of the UCSD Map of Science, a global classification system covering 25 million papers across 554 subdiscipline clusters."

## How (방법론)

- **데이터**: Web of Science + Scopus 2009–2011 합산 약 2,500만 편 논문
- **군집화**: 서지 결합(bibliographic coupling) 기반 유사도 행렬 → Louvain 커뮤니티 탐지 → 554개 클러스터 → 13개 대분야 수동 합병
- **시각화**: Gephi 기반 force-directed 레이아웃, 색상 코딩
- **검증**: 전문가 패널 리뷰 및 NIH, NSF 연구비 데이터 적용 테스트

## Why (중요성)

- 과학 전체의 구조와 분야 간 연결성을 한눈에 파악하는 표준 참조 지도 제공
- 기관·국가·연구자의 연구 포트폴리오를 과학 지도 위에 투영하여 전략적 분석 지원
- 과학 정책, 연구비 배분, 학제간 협업 기회 탐색에 실용적 도구

## Limitation

- Web of Science·Scopus 색인 편향이 지도에 그대로 반영
- 인문학·사회과학은 인용 관행 차이로 클러스터 품질이 낮음
- 2년 단위 업데이트 주기로 빠르게 변하는 신흥 분야 포착에 지연

## Further Study

- 실시간 업데이트 가능한 동적 과학 지도 개발
- arXiv, PubMed 등 미색인 데이터 포함 확대
- LLM 기반 의미론적 과학 지도와의 비교·통합

## 평가

| 항목 | 점수 |
|------|------|
| Novelty | 3/5 |
| Technical Soundness | 4/5 |
| Significance | 4/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: 2,500만 편 논문을 554개 클러스터로 분류한 UCSD 과학 지도의 설계 방법론과 업데이트 과정을 기술한 실용적 도구 논문으로, 과학 지도 제작 분야의 방법론 표준을 제공한다.
