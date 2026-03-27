# Visualizing the context of citations referencing papers published by Eugene Garfield: a new type of keyword co-occurrence analysis

> **저자**: Lutz Bornmann, Robin Haunschild, Sven E. Hug | **날짜**: 2018-02-01 | **Journal**: Scientometrics | **DOI**: [10.1007/s11192-017-2591-8](https://doi.org/10.1007/s11192-017-2591-8)
> **리뷰 모드**: Abstract 기반 (PDF 없음)

---

## Essence

인용 맥락(citation context) — 특정 인용 주변의 텍스트 — 을 키워드 공출현 분석에 활용하면 기존 방법과 어떻게 다른 통찰을 제공하는가? 이 논문은 Eugene Garfield(EG)의 약 1,500편 논문을 대상으로 세 가지 키워드 공출현 네트워크를 비교한다: (1) EG 논문의 제목·초록 키워드, (2) EG 논문을 인용한 논문들의 제목·초록 키워드, (3) EG 논문을 인용한 논문들의 **인용 맥락** 키워드. 핵심 발견은 인용 맥락 키워드가 EG 논문 자체와 의미론적으로 더 밀접하게 연결되며, 이는 인용이 피인용 논문의 인지적 영향력을 반영한다는 가정과 일치한다.

## Originality (Abstract 기반)

- [authorship, novelty] "we use the impressive oeuvre of EG to introduce a new type of bibliometric networks: keyword co-occurrences networks based on the context of citations."
- [authorship, action] "We retrieved the citation context from Microsoft Academic."
- [result, finding] "The comparison of the three networks suggests that papers of EG and citation contexts of papers citing EG are semantically more closely related to each other than to titles and abstracts of papers citing EG."

## How (방법론)

- **데이터**: Eugene Garfield의 약 1,500편 논문; 이 논문들을 인용한 후속 논문들; Microsoft Academic에서 수집한 인용 맥락 텍스트
- **네트워크 1**: EG 논문 제목·초록 키워드 공출현 네트워크
- **네트워크 2**: EG 논문을 인용한 논문들의 제목·초록 키워드 공출현 네트워크
- **네트워크 3**: EG 논문을 인용한 논문들의 인용 맥락(인용 주변 텍스트) 키워드 공출현 네트워크
- **비교 분석**: 세 네트워크의 클러스터 구조, 의미론적 근접성 비교
- **EG 선택 이유**: 정보과학 분야 선구자로서 광범위한 인용 이력과 다양한 주제를 포괄하는 이상적인 케이스 스터디 대상

## Why (중요성)

- 기존 인용 분석은 인용 사실(누가 누구를 인용했는가)에만 주목했으나, **왜, 어떤 맥락에서** 인용했는지를 포착하는 인용 맥락 분석이 중요한 새 연구 방향
- 인용 맥락이 피인용 논문과 의미론적으로 더 가깝다는 발견은 인용이 단순한 참조가 아닌 실질적 인지적 영향을 반영한다는 citation theory를 지지하는 경험적 증거
- Microsoft Academic의 인용 맥락 데이터를 bibliometric 분석에 활용한 방법론 시연은 다른 연구자들이 유사한 분석을 수행할 수 있는 경로 제시
- Eugene Garfield 자신이 정보과학과 인용 분석의 창시자라는 점에서, 그의 연구를 인용 맥락 분석으로 검토하는 것이 메타적 의미를 가짐

## Limitation

### 저자들이 언급한 한계
- Microsoft Academic에서 추출한 인용 맥락 데이터의 완전성과 정확성에 의존 — 모든 인용의 맥락이 정확히 추출되었는지 보장 어려움

### 자체판단 아쉬운 점
- EG라는 단일 사례 연구에 한정 — 다른 분야나 다른 학자에서도 동일한 패턴이 성립하는지 검증 필요
- 인용 맥락의 정의(주변 몇 문장/단어를 포함하는지)가 결과에 미치는 영향 분석 부재
- Microsoft Academic 서비스 종료로 인해 방법론의 재현 가능성이 현재 제한됨

### 후속 연구
- 다양한 분야와 학자들을 대상으로 인용 맥락 키워드 분석의 일반성 검증
- Semantic Scholar, OpenAlex 등 현재 가용한 인용 맥락 데이터 소스로의 방법론 이전
- 인용 맥락의 긍정·부정·중립 극성(sentiment) 분석과 결합한 인용 품질 연구

## 평가

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 3/5 |
| Significance | 3/5 |
| Clarity | 4/5 |
| Overall | 3/5 |

**총평**: 인용 맥락 기반 키워드 공출현 네트워크라는 새로운 bibliometric 방법론을 Eugene Garfield의 방대한 저작을 통해 시연한 방법론적으로 창의적인 논문이다. 단일 사례 연구의 한계와 Microsoft Academic 종료에 따른 재현 제약이 있으나, 인용 맥락 분석을 계량서지학에 도입한 선구적 기여로 평가된다.
