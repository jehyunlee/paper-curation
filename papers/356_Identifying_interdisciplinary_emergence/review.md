# Identifying interdisciplinary emergence in the science of science: combination of network analysis and BERTopic

> **저자**: Keungoui Kim, Dieter F. Kogler, Sira Maliphol | **날짜**: 2024-05-10 | **Journal**: Humanities and Social Sciences Communications | **DOI**: [10.1057/s41599-024-03044-y](https://doi.org/10.1057/s41599-024-03044-y)
> **리뷰 모드**: Abstract only (PDF 없음)

---

## Essence

학제 간 지식 재조합을 통해 새로운 과학 분야가 어떻게 출현하는가를 어떻게 체계적으로 탐지할 수 있는가? Web of Science 메타데이터에서 구축한 **글로벌 과학 카테고리 공-출현 네트워크**와 **BERTopic 임베딩 토픽 모델링**을 결합하여, 학제적 분류의 교집합에서 신흥 분야를 비지도학습으로 식별하는 방법을 제안한다. 시기 간 네트워크 비교를 통해 영향력 변화 패턴을 탐지하고, 질적 검증으로 신흥 영역의 출처를 확인한다.

## Originality (Abstract 기반)

- [authorship, novelty, action] "The present study proposes the application of embedded topic modeling techniques to identify new emerging science via knowledge recombination activities."
- [novelty] "A research field is defined as interdisciplinary when multiple science categories are listed in its description. The co-occurrence networks are subsequently compared between periods to determine changing patterns of influence."
- [finding] "We present the results of the analysis to demonstrate the emergence of global interdisciplinary sciences and further we perform qualitative validation on the results."

## How (방법론)

- **데이터**: Web of Science Core Collection 메타데이터
- **네트워크 구축**: 과학 카테고리 공-출현 네트워크로 글로벌 학제 지형 표현
- **토픽 모델링**: BERTopic(임베딩 기반 비지도 토픽 모델)으로 학제적 출현 분야 분류
- **시기 비교**: 복수 시기의 네트워크를 비교하여 영향력 변화 패턴 탐지
- **검증**: 질적 검증으로 신흥 분야의 실제 출처 확인

## Why (중요성)

- 과학 산출물이 기하급수적으로 증가하는 상황에서 어느 분야가 지식 재조합을 통해 새롭게 출현하는지를 자동으로 식별하는 방법이 필요
- 학제적 융합 탐지는 연구비 배분, 대학 학과 구조 개편, 혁신 정책에서 핵심 정보로 활용 가능

## Limitation

- WoS의 과학 카테고리 분류 체계가 새로운 학제 분야를 신속히 반영하지 못해 탐지에 지연이 발생할 수 있음
- BERTopic의 임베딩 모델 선택과 파라미터 설정에 따라 결과가 달라질 수 있는 민감성
- 질적 검증의 범위와 기준이 명확히 기술되어야 재현성이 보장됨

## Further Study

- 탐지된 신흥 학제 분야가 이후 실제로 독립 분야로 성장하는지 추적 연구
- 다양한 데이터베이스(OpenAlex, Scopus)와의 교차 검증
- 실시간 또는 준실시간 신흥 분야 탐지 시스템 개발

## 평가

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 3/5 |
| Significance | 3/5 |
| Clarity | 3/5 |
| Overall | 3/5 |

**총평**: 네트워크 분석과 BERTopic을 결합하여 학제적 출현을 비지도학습으로 탐지하는 방법을 제안한 탐색적 연구다. 과학 분야 진화의 자동 탐지라는 중요한 문제를 다루지만, 방법론의 일반화 가능성과 강건성 검증이 보강될 필요가 있다.
