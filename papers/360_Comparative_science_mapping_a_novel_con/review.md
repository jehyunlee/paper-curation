# Comparative science mapping: a novel conceptual structure analysis with metadata

> **저자**: Massimo Aria, Corrado Cuccurullo, Luca D'Aniello, Michelangelo Misuraca, Maria Spano | **날짜**: 11/2024 | **Journal**: Scientometrics | **DOI**: [10.1007/s11192-024-05161-6](https://doi.org/10.1007/s11192-024-05161-6)
> **리뷰 모드**: Abstract only (PDF 없음)

---

## Essence

단일 연구 도메인의 개념 구조를 분석하는 기존 science mapping을 넘어, **서로 다른 관찰 단위들(저자, 기관, 지역)을 동시에 비교**할 수 있는가? 이 논문은 서지 데이터셋을 저자 특성, 소속 기관, 지리적 위치 등 다양한 메타데이터 차원에 따라 분절하고, 이들을 단일 시각화에서 공동으로 표현하는 "비교 과학 지도(Comparative Science Mapping)" 기법을 제안한다. 이탈리아 학술의료센터(AMC)의 종양학 연구에 적용하여 기관별 연구 전문화 패턴과 상호작용을 분석했으며, 연구 전략 수립과 정책 의사결정을 지원한다.

## Originality (Abstract 기반)

- [authorship, novelty, action] "This paper introduces an innovative technique to explore the conceptual structure of different observation units in a joint representation."
- [novelty] "The proposed strategy segments bibliographic datasets based on several metadata dimensions, such as the authors (and their characteristics), the corresponding institutions, or their geographical localisation."
- [finding] "The analysis focuses on how different AMCs specialise and interact, providing a comparative framework that aids AMCs themselves in directing their research strategies."

## How (방법론)

- **데이터**: 이탈리아 Academic Medical Centers(AMC) 종양학 연구 서지 데이터
- **분절**: 메타데이터 차원(저자, 기관, 지역)별 데이터셋 분절
- **시각화**: 복수 개념 프레임워크를 공동 시각화하는 전략적 다이어그램(strategic diagram) 확장
- **구현**: bibliometrix R 패키지 기반

## Why (중요성)

- 기존 co-word analysis와 strategic diagram은 단일 도메인의 전체 개념 구조만 보여주어, 서로 다른 행위자들(기관·지역·저자 그룹)이 어떻게 차별화된 연구를 수행하는지 비교 분석이 불가능했음
- 의료기관의 연구 전략 수립, 기금 배분, 정책 결정에서 기관별 비교 시각화의 필요성이 높음

## Limitation

- 이탈리아 AMC라는 특수한 사례에 한정되어 방법론의 일반화 가능성 검증이 필요
- 분절 단위가 많아질수록 시각화의 복잡도가 증가하고 해석이 어려워질 수 있음
- 연구가 초록 기반으로 검토되어 방법론 세부 사항 확인 불가

## Further Study

- 다양한 국가, 분야, 기관 유형으로 확장 적용
- 비교 과학 지도의 시계열 버전(종단 분석) 개발
- bibliometrix 패키지에 완전 통합하여 사용자 접근성 향상

## 평가

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 3/5 |
| Significance | 3/5 |
| Clarity | 3/5 |
| Overall | 3/5 |

**총평**: 복수 관찰 단위를 동시에 비교하는 혁신적 과학 지도 기법을 제안한 연구로, bibliometrix 생태계 내에서 실용적 도구화 가능성이 높다. 이탈리아 AMC라는 제한적 사례가 아쉬우나 방법론적 독창성이 인정된다.
