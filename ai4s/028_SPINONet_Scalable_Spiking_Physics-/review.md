# SPINONet: Scalable Spiking Physics-informed Neural Operator for Computational Mechanics Applications

> **저자**: Shailesh Garg, Luis Mandl, Somdatta Goswami, Souvik Chakraborty | **날짜**: 2026-03-23 | **arXiv**: 2603.21674 | **분야**: physics.comp-ph

---

## Essence

SPINONet은 physics-informed operator learning에 에너지 효율적인 spiking neural network(SNN)를 통합한 최초의 프레임워크이다. Separable DeepONet 아키텍처에서 branch network(입력 함수 인코딩)에만 Variable Spiking Neuron(VSN)을 배치하고, trunk network(좌표 의존 경로)는 연속적으로 유지하여 PDE residual 계산에 필요한 미분 가능성을 보존하면서 sparse, event-driven 연산을 달성한다. Burgers, Heat, Eikonal 방정식에서 기존 dense baseline과 유사한 정확도를 유지하면서 GPU 메모리와 연산량을 크게 절감한다.

## Motivation

- **알려진 것**: Physics-informed operator learning(DeepONet, FNO 등)이 PDE 풀이의 surrogate model로 강력한 성능을 보이며, separable DeepONet이 scalability를 개선
- **Gap**: 기존 아키텍처는 모든 뉴런이 매 forward evaluation마다 활성화되어(continuously active), 반복적 operator evaluation에서 불필요한 연산 비용 발생 -- edge/embedded device 배포 시 에너지 제약이 병목
- **왜 중요한가**: Digital twin, parametric PDE analysis, uncertainty quantification 등에서 반복적 operator 평가가 필요하며, 전력 제약 환경에서의 실시간 추론이 점점 중요해짐
- **접근법**: 생물학적 뉴런에서 영감받은 event-driven spiking neuron을 physics-informed operator 아키텍처에 구조적으로 호환 가능하도록 설계

## Achievement

1. **아키텍처 분리 원리**: Branch network에만 VSN을 적용하여 spiking dynamics와 physics-based differentiation 간의 비호환성을 구조적으로 해결 -- 좌표 미분이 branch coefficient에 작용하지 않으므로 surrogate gradient의 근사 오차가 PDE residual을 오염시키지 않음
2. **정확도 유지**: Burgers 방정식 L2 error 0.07 (vanilla baseline 0.06, PI-DeepONet 0.05), Heat 방정식 0.09 (baseline 0.10), Eikonal 방정식 0.016 (baseline 0.007) -- comparable 수준 유지
3. **Sparse 연산**: Branch network의 평균 spiking activity가 32-53%로, 전체 뉴런의 절반 이하만 활성화
4. **Scalability**: Grid resolution 증가에 따른 GPU 메모리 및 학습 시간이 PI-DeepONet 대비 현저히 느린 속도로 증가 -- separable trunk evaluation이 multiplicative 의존성을 additive로 변환
5. **에너지 효율 분석**: 45nm CMOS 기준 ANN vs VSN layer의 에너지 parity가 ~86-90% activity에서만 도달함을 해석적으로 도출 -- 실제 53% 이하 activity에서 상당한 에너지 절감 예측
6. **Hybrid training**: 소량의 supervised data 추가로 purely physics-informed 학습에서 발생하는 degenerate solution 문제를 완화

## How

- **아키텍처**: Separable DeepONet 기반 -- d개의 독립 trunk network가 각 좌표 방향의 1D 입력을 받아 basis function 생성, branch network가 입력 함수 u에서 coefficient vector B(u) 생성, 외적(outer product)으로 결합
- **Variable Spiking Neuron (VSN)**: membrane potential m(tau) = beta_l * m(tau-1) + z(tau), Heaviside threshold로 spike 생성, spike 시 graded output y(tau) = phi(z(tau) * H(m(tau)-Th)), spike 후 membrane reset
- **핵심 설계 원리**: nabla_xi G_theta(u)(xi) = sum_m B_m(u) * nabla_xi tilde_t_m(xi) -- branch coefficient B_m(u)이 좌표 xi에 독립이므로, VSN을 branch에만 넣어도 PDE residual 미분에 영향 없음
- **Forward-mode AD**: Trunk이 1D scalar 입력을 받으므로 input dimension=1이 되어 forward-mode AD가 reverse-mode보다 유리; separable 구조에서 비용이 sum(n_j)에 비례 (non-separable은 prod(n_j))
- **Surrogate gradient**: 역전파 시 Heaviside 함수의 미분을 smooth surrogate 1/(1+K_s|m-Th|)로 근사
- **Loss**: L_phys = L_int + lambda_bc * L_bc + lambda_ic * L_ic, 선택적으로 lambda_data * L_data 추가
- **실험**: Viscous Burgers (1D+t), parametric Heat (2D+t+alpha), Eikonal (2D steady-state), Adam optimizer, 40k-100k epochs

## Originality

- **Physics-informed learning과 SNN의 최초 통합**: Spiking neuron의 event-driven sparse computation을 operator learning에 도입한 최초 시도로, "어디에 spiking을 넣을 수 있는가"라는 구조적 질문에 명확한 답(branch only)을 제시
- **Forward-mode AD + separable architecture의 시너지 분석**: 두 기법이 독립적으로는 알려져 있으나, SPINONet에서 결합했을 때의 복합 효율성 이점을 해석적으로 정량화한 점이 새로움
- **에너지 효율의 해석적 프레임워크**: MAC/ACC/메모리 연산 수준에서 ANN vs VSN의 에너지 비용을 비교하는 hardware-agnostic 분석 모델 제시

## Limitation & Further Study

### 저자들이 언급한 한계

- 에너지 효율 분석이 해석적(analytical) 수준에 머물며, 실제 neuromorphic hardware나 GPU에서의 에너지 측정이 수행되지 않음
- Deep learning 공통 한계(optimization sensitivity, initialization 민감도)가 여전히 존재
- Surrogate gradient가 true gradient의 근사이므로, branch network 학습에 근사 오차 내재

### 자체판단 아쉬운 점

- 실험 대상 PDE가 비교적 단순한 3개(Burgers, Heat, Eikonal)에 한정되며, 복잡한 다중 물리(multi-physics), 비선형 구조역학, 3D 문제에서의 성능이 미검증
- Eikonal 방정식에서 SPINONet의 L2 error(0.016)가 PI-DeepONet(0.005)이나 vanilla baseline(0.007) 대비 2-3배 높아, "comparable accuracy"라는 주장이 모든 경우에 성립하지는 않음
- Spiking activity가 32-53%로 보고되어 이론적 에너지 절감은 분명하나, 실제 GPU 학습에서의 wallclock time 차이는 미미(Burgers: 0.012 vs 0.013 s/epoch) -- 현재 GPU 생태계가 sparse spike 연산에 최적화되어 있지 않기 때문
- 비교 대상이 PI-DeepONet과 vanilla separable DeepONet에 한정되며, FNO, Wavelet Neural Operator 등 다른 operator learning 방법과의 비교가 없음
- Hybrid training에서 supervised data 양의 sensitivity analysis가 부족

### 후속 연구

- Neuromorphic hardware(Intel Loihi, IBM TrueNorth 등)에서의 실제 에너지 측정 및 배포 실험
- 3D multi-physics 시스템(유체-구조 상호작용, 열-기계 커플링 등)으로의 확장
- Sparsity-aware training objective 도입 -- spiking activity를 명시적으로 최소화하는 regularization
- Trunk network에도 spiking을 도입할 수 있는 방법론 탐색 (미분 가능성 보존 조건 하)
- 대규모 parametric space에서의 real-time inference 시연

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 4/5 |
| Significance | 3/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: Physics-informed operator learning에 spiking neural network를 통합하는 참신한 아이디어를 제시하며, branch/trunk 분리를 통해 spiking dynamics와 PDE 미분의 호환성 문제를 우아하게 해결한 연구이다. 해석적 에너지 효율 분석은 설득력 있으나, 현재 GPU 생태계에서의 실질적 이점은 제한적이며 neuromorphic hardware에서의 검증이 필수적이다. Computational mechanics의 edge deployment라는 미래 방향에 대한 선구적 탐색으로서 가치가 있다.
