# A Dynamic Network Measure of Technological Change

> **저자**: Russell J. Funk, Jason Owen-Smith | **날짜**: 2017 | **Journal**: Management Science | **DOI**: 10.1287/mnsc.2015.2366 | **arXiv**: -
> **리뷰 모드**: Web-only

---

## Essence

기술 특허가 기존 기술 궤적을 강화(consolidate)하는가, 아니면 새로운 방향을 열어젖히는(disrupt)가? 이 논문은 **CD(Consolidation-Disruption) 지수**라는 새로운 동적 네트워크 지표를 개발하여, 특허가 이후 발명가들에게 기존 피인용 기술을 계속 인용하게 하는지(consolidation) 아니면 우회하게 하는지(disruption)를 측정했다. 이 지표는 이후 Park et al.(2023)의 과학·특허 혁신성 분석에서 핵심 도구로 채택되었다.

## Originality (Abstract 기반)

- **rule_base_novelty**: 특허 인용 네트워크의 동적 변화를 포착하는 CD 지수 최초 개발
- **rule_base_action**: 인용 네트워크에서 focal 특허의 역할(통합자 vs. 파괴자)을 정량화
- **rule_base_result**: CD 지수가 기술 혁신의 방향(점진적 발전 vs. 급진적 혁신)을 포착하는 유효한 지표임을 검증

## How (방법론)

- **데이터**: USPTO 특허 데이터베이스
- **CD 지수**: $$CD_t = \frac{n_{forward} - n_{backward}}{n_{forward} + n_{backward} + n_{neither}}$$
  - $n_{forward}$: focal 특허를 인용하면서 focal 특허의 피인용 특허는 인용하지 않는 이후 특허 수
  - $n_{backward}$: focal 특허와 그 피인용 특허 모두를 인용하는 이후 특허 수
- **검증**: CD 지수와 기존 혁신성 지표(원자력, 반도체 등 기술 역사) 비교

## Why (중요성)

기술 변화의 성격(점진적 vs. 혁명적)을 인용 구조에서 자동으로 측정할 수 있는 도구를 제공한다. 이는 기술 예측, R&D 투자 전략, 혁신 정책 평가에 활용될 수 있으며, 이후 과학 분야로 확장되어 Park et al.(2023)의 "과학 혁신성 감소" 발견의 방법론적 기초가 되었다.

## Limitation

### 저자들이 언급한 한계
- CD 지수가 인용 행동에 의존하므로, 인용 관행이 다른 분야 간 비교에 주의 필요
- 단기적 CD 값이 장기적 기술 중요성을 반영하지 못할 수 있음

### 자체판단 아쉬운 점
- 지수 계산에 사용되는 시간 창(time window)의 선택이 결과에 민감하게 영향
- 특허 데이터만 사용하여 논문 기반 과학 혁신과의 통합 분석 부재

## Further Study

- 과학 논문으로 확장 → Park et al.(2023)에서 실현됨
- CD 지수와 기업 시장 성과, 기술 확산 속도 간 관계 분석

## 평가

| 항목 | 점수 |
|------|------|
| Novelty | 5/5 |
| Technical Soundness | 4/5 |
| Significance | 5/5 |
| Clarity | 4/5 |
| Overall | 5/5 |

**총평**: 기술 혁신의 성격을 인용 네트워크 구조에서 포착하는 CD 지수를 개발한 방법론적 기여로, 이후 과학 혁신성 연구의 핵심 도구가 된 영향력 높은 논문이다.
