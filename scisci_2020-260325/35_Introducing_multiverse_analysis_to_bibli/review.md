# Introducing multiverse analysis to bibliometrics: The case of team size effects on disruptive research

> **저자**: Christian Leibel, Lutz Bornmann | **날짜**: 2026-03-23 | **Journal**: Quantitative Science Studies | **DOI**: 10.1162/qss.a.475

---

## Essence
소규모 팀이 대규모 팀보다 더 파괴적인(disruptive) 연구를 생산한다는 Wu et al.(2019)의 발견은 모델 선택에 따라 얼마나 달라지는가? Multiverse 분석으로 모든 합리적인 모델 조합을 검증한 결과, 팀 크기가 disruption score에 미치는 **부정적 효과 자체는 강건**했다(모든 모델에서 음의 계수). 그러나 **효과 크기는 모델 사양에 따라 상당히 변동**하며, 특히 인용 인플레이션(citation inflation) 통제 여부와 disruption index 조작화 방식이 결과에 가장 큰 영향을 미쳤다.

## Motivation
Wu et al.(2019, Nature)은 소규모 팀이 파괴적 연구를 생산한다고 보고하여 과학정책에 큰 영향을 미쳤다. 그러나 Petersen et al.(2025)은 인용 인플레이션을 통제하면 팀 크기가 오히려 파괴적 영향을 증가시킨다고 반박했다. 두 연구의 상반된 결론은 서로 다른 모델링 가정에서 비롯된 것으로, 어느 것이 "진실"에 가까운지 판단할 수 없는 상태였다. 이는 계량서지학에서 모델 불확실성을 체계적으로 다룰 방법론의 필요성을 보여주었다.

## Achievement
1. **Multiverse 분석**을 계량서지학에 최초로 도입하여 모델 불확실성을 체계적으로 측정
2. 팀 크기의 disruption에 대한 **부정적 효과는 강건** — 모든 모델 사양에서 음의 계수
3. **효과 크기는 모델 사양에 크게 의존**: 모델 표준편차(√V_M)가 상당
4. **가장 영향력 있는 모델링 결정**: (a) 인용 인플레이션 통제, (b) disruption index 조작화, (c) 통제변수 선택
5. 기존 robustness check의 한계를 넘어 **모든 합리적 모델의 결과를 투명하게 보고**하는 방법론 제시

## How
- **데이터**: SciSciNet 기반, Wu et al.(2019)과 Petersen et al.(2025)의 데이터 및 모델 사양 재현
- **방법**: Wu et al.과 Petersen et al.의 모델링 가정을 체계적으로 분해 → 모든 합리적인 모델 조합(multiverse) 구축 → 각 모델의 추정치, 분산, 영향력 통계 계산
- **핵심 차원**: 데이터 소스(WoS vs SciSciNet), 인용 윈도우, disruption index 변형, 이상치 처리, 통제변수 조합, 추정 방법

## Originality
- 심리학·사회과학에서 발전한 multiverse 분석을 **계량서지학에 최초로 적용**
- Wu et al. vs Petersen et al. 논쟁을 제3의 관점에서 체계적으로 해소
- 모델 영향력 통계(model influence statistics)를 통해 어떤 모델링 결정이 결과를 좌우하는지 투명하게 제시

## Limitation & Further Study
### 저자들이 언급한 한계
- Multiverse 정의 자체가 연구자의 판단에 의존
- 인과 추론이 아닌 관찰 연구의 한계

### 리뷰어 판단 아쉬운 점
- Disruption index 자체의 타당성 문제는 multiverse로도 해결되지 않음
- 실질적 정책 함의가 "효과가 있긴 하지만 크기가 불확실하다"는 다소 유보적 결론에 그침
- 계산 비용이 높아 대규모 multiverse 구축의 실용성이 제한될 수 있음

### 후속 연구
- 다른 계량서지학 논쟁(예: OA 인용 이점, 다양성과 혁신)에 multiverse 분석 적용
- Multiverse 분석의 표준화된 가이드라인 및 소프트웨어 도구 개발
- 인과 추론 프레임워크와의 통합

## Evaluation
| 항목 | 점수 |
|------|------|
| Novelty | 5/5 |
| Technical Soundness | 5/5 |
| Significance | 5/5 |
| Clarity | 4/5 |
| Overall | 5/5 |

**총평**: Multiverse 분석이라는 강력한 방법론을 계량서지학에 도입하여 모델 불확실성의 투명한 보고를 가능하게 한 방법론적 기여가 탁월한 연구다.
