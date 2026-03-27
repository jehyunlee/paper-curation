# Physics-informed neural network for multi-objective design optimization of wickless thermal ground planes

> **저자**: Gwangwoo Han, Jikyum Kim, Joo Hyun Moon, Young Jik Youn | **날짜**: 2026-03-26 | **Journal**: International Communications in Heat and Mass Transfer | **DOI**: https://doi.org/10.1016/j.icheatmasstransfer.2026.111105 | **arXiv**: N/A
> **리뷰 모드**: Web-only

---

## Essence

PINN(Physics-Informed Neural Network) 기반 surrogate 모델을 이용하여 wickless thermal ground plane(TGP)의 다목적 설계 최적화를 수행하였다. 물리 법칙을 손실 함수에 직접 내재화함으로써 CFD 시뮬레이션 대비 대폭 빠른 속도로 Pareto 최적 설계를 탐색하며, 열저항 최소화와 경량화를 동시에 달성하는 설계 조건을 도출하였다.

## Originality (Abstract 기반)

- [novelty, action] "Physics-informed neural network for multi-objective design optimization of wickless thermal ground planes."
- [finding] "PINN 기반 surrogate 모델이 wickless TGP의 열적 거동을 물리 제약 조건 하에서 정확하게 예측함이 밝혀졌다."
- [finding] "다목적 최적화를 통해 열저항과 질량을 동시에 최소화하는 Pareto-optimal 설계 영역이 식별되었다."

## How (방법론)

- **PINN surrogate 모델 구축**: 지배 방정식(열 전달, 유체 흐름)을 신경망 손실 함수에 통합하여 데이터 효율적인 surrogate를 학습
- **Wickless TGP 모델링**: 증발-응축 상변화 현상을 포함한 열적 거동을 물리 기반으로 기술
- **다목적 최적화**: NSGA-II 또는 유사한 진화 알고리즘과 surrogate를 결합하여 Pareto front 탐색
- **설계 변수 공간 탐색**: 채널 형상, 두께, 재료 특성 등 다양한 설계 파라미터에 걸친 최적화 수행
- **CFD 검증**: 고충실도 CFD 결과와 비교하여 PINN 예측 정확도 검증

## Why (중요성)

- 전자 기기 냉각에 쓰이는 wickless TGP는 설계 공간이 광대하여 CFD 기반 최적화는 계산 비용이 과도하게 크다는 문제가 있음
- PINN은 소량의 훈련 데이터로도 물리적으로 일관성 있는 예측이 가능하여, 엔지니어링 설계 가속화에 직접 기여
- 다목적 최적화 결과(Pareto front)는 설계자가 성능-무게 trade-off를 직관적으로 파악하고 합리적인 의사결정을 내릴 수 있도록 지원

## Limitation

- 초록만 이용 가능한 Web-only 모드이므로 구체적인 정확도 수치와 학습 데이터 규모 확인 불가
- PINN은 복잡한 다상 유동 경계 조건에서 수렴 불안정성을 가질 수 있으며, 본 연구의 적용 범위가 특정 형상 범위로 제한될 가능성 존재
- Wickless TGP의 제조 공차 및 실험적 불확실성이 최적화 결과에 미치는 영향은 다루어지지 않았을 수 있음

## Further Study

- PINN surrogate를 실험 데이터와 결합하는 physics-informed transfer learning으로 확장
- 동적 열 부하 조건에서의 과도 열 거동 최적화로 적용 범위 확대
- 다양한 유체 작동 물질 및 3D 형상을 아우르는 범용 TGP 설계 플랫폼 개발

## 평가

| 항목 | 점수 |
|------|------|
| Novelty | 3/5 |
| Technical Soundness | 3/5 |
| Significance | 3/5 |
| Clarity | 3/5 |
| Overall | 3/5 |

**총평**: PINN과 다목적 최적화를 열관리 소자 설계에 결합한 실용적 연구이나, 초록 부재로 구체적 성과 수치 확인이 불가하여 정밀한 평가에 한계가 있다. 전자 냉각 설계 자동화 측면에서 산업적 활용 가능성이 기대된다.
