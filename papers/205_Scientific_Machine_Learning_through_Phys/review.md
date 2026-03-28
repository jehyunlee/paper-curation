# Scientific Machine Learning through Physics-Informed Neural Networks: Where we are and What's next
> **저자**: Salvatore Cuomo et al. | **날짜**: 2022.01 | **arXiv**: [2201.05624](https://arxiv.org/abs/2201.05624)

---

## Essence

This article provides a comprehensive review of the literature on PINNs: while the primary goal of the study was to characterize these networks and their related advantages and disadvantages.

## Motivation

- **Known**: Physics-Informed Neural Networks (PINN) are neural networks (NNs) that encode model equations, like Partial Differential Equations (PDE), as a component of the neural network itself.
- **Gap**: Despite the wide range of applications for which PINNs have been used, by demonstrating their ability to be more feasible in some contexts than classical numerical techniques like Finite Element Method (FEM), advancements are still possible, most notably theoretical issues that remain unresolved.
- **Approach**: This article provides a comprehensive review of the literature on PINNs: while the primary goal of the study was to characterize these networks and their related advantages and disadvantages.

## Achievement

1. This article provides a comprehensive review of the literature on PINNs: while the primary goal of the study was to characterize these networks and their related advantages and disadvantages.

## How

Physics-Informed Neural Networks (PINN) are neural networks (NNs) that encode model equations, like Partial Differential Equations (PDE), as a component of the neural network itself. This novel methodology has arisen as a multi-task learning framework in which a NN must fit observed data while reducing a PDE residual. This article provides a comprehensive review of the literature on PINNs: while the primary goal of the study was to characterize these networks and their related advantages and disadvantages.

## Originality

- This novel methodology has arisen as a multi-task learning framework in which a NN must fit observed data while reducing a PDE residual.
- This article provides a comprehensive review of the literature on PINNs: while the primary goal of the study was to characterize these networks and their related advantages and disadvantages.
- The review also attempts to incorporate publications on a broader range of collocation-based physics informed neural networks, which stars form the vanilla PINN, as well as many other variants, such as physics-constrained neural networks (PCNN), variational hp-VPINN, and conservative PINN (CPINN).
- The study indicates that most research has focused on customizing the PINN through different activation functions, gradient optimization techniques, neural network structures, and loss function structures.
- Despite the wide range of applications for which PINNs have been used, by demonstrating their ability to be more feasible in some contexts than classical numerical techniques like Finite Element Method (FEM), advancements are still possible, most notably theoretical issues that remain unresolved.

## Limitation & Further Study

### 저자들이 언급한 한계
- 서베이 논문의 특성상 개별 방법론의 심층 분석보다는 전체적 조망에 초점
- 빠르게 발전하는 분야 특성상 최신 연구가 누락될 수 있음

### 자체판단 아쉬운 점
- 서베이 범위의 선택적 제한으로 인해 관련 분야의 교차점이 충분히 다루어지지 않을 수 있음
- 정량적 비교 분석의 부족

### 후속 연구
- 더 넓은 범위의 분야를 포함하는 통합적 서베이
- 벤치마크 기반의 체계적 성능 비교

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 3/5 |
| Technical Soundness | 3/5 |
| Significance | 4/5 |
| Clarity | 4/5 |
| Overall | 3/5 |

**총평**: 관련 분야의 포괄적 서베이로서 연구자들에게 유용한 참고 자료를 제공하나, 서베이 논문 특성상 독창적 기여는 제한적이다.
