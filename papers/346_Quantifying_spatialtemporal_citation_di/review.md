# Quantifying spatial–temporal citation diffusion of individual papers in knowledge space

> **저자**: Shuang Zhang, Feifan Liu, Haoxiang Xia | **날짜**: 12/2025 | **Journal**: Journal of the Association for Information Science and Technology | **DOI**: [10.1002/asi.70021](https://doi.org/10.1002/asi.70021)
> **리뷰 모드**: Abstract only (PDF 없음)

---

## Essence

논문 인용이 지식 공간에서 시간과 함께 어떻게 확산되는가? 7개 대규모 학문 분야에서 수백만 건의 논문을 대상으로 document representation 알고리즘을 사용해 인용 확산 궤적을 분석한 결과, 세 가지 핵심 패턴이 발견되었다: (1) 인용 확산은 **가우시안 분포**를 따르는 범위와 **지수 분포**를 따르는 거리를 보이며 의미적으로 국소화되는 경향이 있다. (2) 초기 인용 확산의 폭은 장기적 인용 축적과 **양의 상관관계**를 보여, 초기 광범위한 확산이 장기 임팩트를 증폭시킨다. (3) 참신하고 파괴적인 논문은 더 적고 지연된 인용을 받지만, 더 먼 지식 거리의 인용을 유인하며 장기적으로 더 광범위한 영향을 미친다.

## Originality (Abstract 기반)

- [authorship, novelty, action] "We apply document representation algorithms capturing semantic associations to construct citation diffusion trajectories in the embedded disciplinary knowledge landscape."
- [finding] "A positive correlation between initial citation diffusion breadth and citation growth, which significantly amplifies long-term impact among papers with comparable early citation counts."
- [novelty] "We identify distinct spatial–temporal citation diffusion patterns for novel and disruptive papers."

## How (방법론)

- **데이터**: 7개 대형 학문 분야의 수백만 편 논문
- **지식 공간 구성**: document representation 알고리즘(예: doc2vec 또는 유사 기법)으로 논문을 고차원 임베딩 공간에 배치
- **인용 확산 궤적**: 각 논문에 대해 시간 순서별로 인용 논문들의 지식 공간 위치를 추적
- **통계 분석**: 인용 범위(scope), 인용 거리(distance)의 분포 적합, 초기 확산과 장기 임팩트 상관 분석

## Why (중요성)

- 기존 인용 역학 연구는 시간적 패턴(인용 축적)에만 집중했으나, 지식 공간에서의 공간적 확산을 함께 분석한 연구는 드물었음
- 초기 인용 확산 폭이 장기 임팩트의 선행 지표가 될 수 있다면, 조기 과학적 영향 예측에 새로운 차원을 제공함

## Limitation

- Document representation 알고리즘의 선택에 따라 지식 공간 구조가 크게 달라질 수 있어 방법론적 의존성이 높음
- 7개 분야 선택 기준과 분야별 대표성 불명확
- 초기 인용 확산 폭과 장기 임팩트 간의 인과관계 해석에 주의 필요 (공통 원인 가능성)

## Further Study

- 인용 확산 패턴의 분야별 차이와 학제 간 연구의 특성 분석
- 초기 인용 확산 폭을 활용한 논문 장기 임팩트 예측 모델 개발
- 지식 공간에서의 인용 확산과 실제 연구자 협력 네트워크의 관계 분석

## 평가

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 4/5 |
| Significance | 4/5 |
| Clarity | 3/5 |
| Overall | 4/5 |

**총평**: 인용 역학에 공간적 차원을 추가하여 지식 공간에서의 인용 확산 궤적을 체계적으로 분석한 독창적 연구다. 참신하고 파괴적인 논문이 더 먼 지식 거리에서 인용을 받는다는 발견은 과학적 혁신의 확산 메커니즘에 대한 새로운 통찰을 제공한다.
