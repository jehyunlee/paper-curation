# Mapping Knowledge: Topic Analysis of Science Locates Researchers in Disciplinary Landscape

> **저자**: Radim Hladik, Yann Renisio | **날짜**: 2024-02-22 | **Journal**: OSF Preprints | **DOI**: [10.31235/osf.io/94jd5](https://doi.org/10.31235/osf.io/94jd5)
> **리뷰 모드**: Abstract only (PDF 없음)

---

## Essence

개별 연구자를 학문 분야의 지형 안에서 연속적으로 위치시킬 수 있는 인식론적 좌표계를 어떻게 구성하는가? 국가 수준의 과학 산출물 데이터에서 제목·초록·키워드의 텍스트를 기반으로 의미 네트워크 토픽 모델을 구축하고, compositional data 변환을 적용하여 네 가지 핵심 결과를 도출했다: (1) 계층적 클러스터링이 전통적 학문 분류와 일치하는 저층부 정렬을 확인했다. (2) PCA가 세 축 — **문화-자연, 생명-비생명, 재료-방법** — 으로 지식 공간의 주요 구조를 드러냈다. (3) 개별 연구자를 토픽 포트폴리오로 이 세 연속 차원에 투영하는 것이 가능했다. (4) 연구자의 주제 방향성과 출판 관행, 성별, 소속 기관, 펀딩 출처 간의 연관성 검증으로 방법의 강건성을 확인했다.

## Originality (Abstract 기반)

- [authorship, novelty, action] "The study presents a new approach for constructing an epistemological coordinate system that locates individual researchers within the disciplinary landscape of science."
- [novelty] "Compositional data transformation applied to the topic model enables a geometric analysis of topics across disciplines."
- [finding] "Principal component analysis reveals three axes — Culture-Nature, Life-Non-life, and Materials-Methods — that primarily structure this scientific knowledge space."

## How (방법론)

- **데이터**: 국가 수준의 종합 과학 산출물 데이터셋 (제목·초록·키워드 텍스트)
- **토픽 모델**: 텍스트 내용에서 의미 네트워크 기반 토픽 모델 구축
- **Compositional data 변환**: 토픽 비율의 기하학적 분석을 위한 logratio 변환 (Aitchison geometry)
- **분석**: 계층적 클러스터링, PCA로 지식 공간 구조 추출
- **연구자 투영**: 개별 연구자를 토픽 포트폴리오로 3차원 좌표에 위치시킴
- **검증**: 성별, 기관, 펀딩 등 보조 변수와의 연관성 분석

## Why (중요성)

- 기존 학문 분류(WoS 분야, Scopus 분야)는 이분법적·범주적이어서 연구자의 실제 지적 위치를 연속 공간에서 표현하지 못함
- "문화-자연", "생명-비생명", "재료-방법"이라는 세 축은 서양 지식 전통의 근본적 인식론적 구분을 반영하며, 이를 데이터에서 귀납적으로 발견한 점이 중요

## Limitation

- 단일 국가 데이터에 기반하여 국제적 대표성 검증이 필요
- 토픽 모델의 파라미터 선택과 텍스트 전처리가 결과에 미치는 영향의 민감도 분석이 제한적
- 영어 중심 텍스트 분석이 비영어 연구 전통을 과소 대표할 가능성

## Further Study

- 복수 국가 데이터로 확장하여 세 축의 보편성 검증
- 연구자 주제 방향성의 경력 궤적 추적 (tenure, 펀딩 변화와의 상관)
- 과학 평가·정책에서 범주적 분류를 대체하는 연속 좌표계 활용

## 평가

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 4/5 |
| Significance | 4/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: 연구자를 학문 지형에서 연속 좌표로 위치시키는 인식론적 좌표계를 구축한 창의적이고 방법론적으로 탄탄한 연구다. "문화-자연, 생명-비생명, 재료-방법"이라는 세 축이 귀납적으로 도출된 점은 과학 지식 구조에 대한 깊은 통찰을 제공한다.
