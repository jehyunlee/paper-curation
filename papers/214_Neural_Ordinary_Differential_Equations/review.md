# Neural Ordinary Differential Equations
> **저자**: Ricky T. Q. Chen et al. | **날짜**: 2018.06 | **arXiv**: [1806.07366](https://arxiv.org/abs/1806.07366)

---

## Essence

We introduce a new family of deep neural network models. We demonstrate these properties in continuous-depth residual networks and continuous-time latent variable models.

## Motivation

- **Known**: The output of the network is computed using a black-box differential equation solver.
- **Gap**: Instead of specifying a discrete sequence of hidden layers, we parameterize the derivative of the hidden state using a neural network.
- **Approach**: We introduce a new family of deep neural network models.

## Achievement

1. We introduce a new family of deep neural network models.
2. We demonstrate these properties in continuous-depth residual networks and continuous-time latent variable models.
3. For training, we show how to scalably backpropagate through any ODE solver, without access to its internal operations.

## How

We introduce a new family of deep neural network models. Instead of specifying a discrete sequence of hidden layers, we parameterize the derivative of the hidden state using a neural network. The output of the network is computed using a black-box differential equation solver.

## Originality

- We introduce a new family of deep neural network models.
- Instead of specifying a discrete sequence of hidden layers, we parameterize the derivative of the hidden state using a neural network.
- The output of the network is computed using a black-box differential equation solver.
- These continuous-depth models have constant memory cost, adapt their evaluation strategy to each input, and can explicitly trade numerical precision for speed.
- We demonstrate these properties in continuous-depth residual networks and continuous-time latent variable models.
- We also construct continuous normalizing flows, a generative model that can train by maximum likelihood, without partitioning or ordering the data dimensions.
- For training, we show how to scalably backpropagate through any ODE solver, without access to its internal operations.
- This allows end-to-end training of ODEs within larger models.

## Limitation & Further Study

### 저자들이 언급한 한계
- (논문 본문 참조)

### 자체판단 아쉬운 점
- 실험적 검증의 범위와 일반화 가능성에 대한 추가 논의 필요

### 후속 연구
- 다양한 도메인으로의 확장 적용
- 대규모 벤치마크에서의 체계적 비교 평가

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 4/5 |
| Significance | 4/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: 해당 분야에 의미 있는 기여를 하는 논문으로, 기술적 건전성과 실험적 검증이 돋보인다.
