# Physics-Informed Neural Networks and Extensions

> **저자**: Maziar Raissi, Paris Perdikaris, Nazanin Ahmadi, George Em Karniadakis | **날짜**: 2024 | **Link**: [https://arxiv.org/abs/2408.16806](https://arxiv.org/abs/2408.16806)

---

## Essence

Scientific machine learning의 핵심 방법론인 Physics-Informed Neural Networks(PINNs)를 review하고, 최근의 practical extensions를 소개하며, governing differential equation의 data-driven discovery에 대한 구체적 예시를 제공한다.

## Motivation

- **알려진 것**: PINNs가 scientific machine learning의 main pillar로 자리잡으며 PDE 기반 forward/inverse 문제에 폭넓게 적용됨
- **Gap**: PINNs의 실용적 확장과 governing equation discovery에 대한 통합적 review 필요
- **왜 중요한가**: PINNs의 체계적 이해와 extensions의 정리는 과학/공학 분야의 ML 적용을 가속화하는 데 필수적
- **접근법**: PINNs의 핵심 원리를 review하고, practical extensions와 data-driven equation discovery 예시를 통합적으로 제시

## Achievement

1. PINNs의 이론적 기초와 핵심 원리를 체계적으로 정리
2. 최근 practical extensions(adaptive sampling, domain decomposition, multi-fidelity 등)을 종합
3. Governing differential equation의 data-driven discovery에 대한 구체적 적용 예시 제공
4. Scientific machine learning에서의 PINNs 활용 전반에 대한 통합적 관점 제시

## How

- **PINNs 원리**: 물리 법칙(PDE residual)을 loss function에 직접 포함하여 neural network 학습을 물리적으로 constrain
- **Extensions**: Adaptive collocation point sampling, domain decomposition(XPINNs, cPINNs), multi-fidelity training 등 실용적 확장 기법 소개
- **Equation Discovery**: Sparse regression + neural network을 결합한 governing equation의 data-driven identification 시연
- **원저자 관점**: PINNs 원저자(Raissi, Karniadakis)가 직접 작성하여 방법론의 motivation과 design philosophy를 정확히 전달

## Originality

- **원저자 Review**: PINNs 원저자 팀이 직접 작성한 review로, 방법론의 핵심 철학과 설계 의도를 가장 정확히 전달하는 고유한 가치
- **Extensions 통합**: 산발적으로 발표된 다양한 PINN extensions를 unified framework 하에 정리
- **Equation Discovery 연결**: Forward/inverse problem solving과 equation discovery를 PINNs 프레임워크 내에서 통합적으로 다룸

**Abstract에서 추출된 독창성 문장**: In this paper, we review the new method Physics-Informed Neural Networks (PINNs) that has become the main pillar in scientific machine learning, we present recent practical extensions, and provide a specific example in data-driven discovery of governing differential equations.

## Limitation & Further Study

### 저자들이 언급한 한계

- PINNs의 알려진 한계(spectral bias, training difficulty, high-dimensional 문제)에 대한 심층 논의가 제한적
- 최신 경쟁 방법론(neural operators, foundation models)과의 비교 부재

### 자체판단 아쉬운 점

- 원저자 review 특성상 PINNs의 한계에 대해 상대적으로 관대한 서술 -- critical assessment 부족
- Abstract가 매우 짧아 논문의 구체적 기여와 범위를 사전 파악하기 어려움
- Computational cost, convergence 분석, failure case 등 실용적 관점의 논의가 부족할 수 있음
- Neural operator 등 대안적 접근법과의 정량적 비교가 없어 현재 시점에서의 PINNs 위상 파악 어려움

### 후속 연구

- PINNs와 neural operator의 hybrid approach 개발
- High-dimensional, multi-scale PDE에서의 PINNs scalability 개선
- Foundation model 기반 physics-informed pre-training 전략 탐구

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 2/5 |
| Technical Soundness | 4/5 |
| Significance | 4/5 |
| Clarity | 4/5 |
| Overall | 3/5 |

**총평**: PINNs 원저자가 직접 작성한 review로서 방법론의 철학과 extensions를 정확히 전달하는 고유한 가치를 지닌다. Scientific machine learning의 핵심 방법론에 대한 authoritative한 정리이나, critical assessment와 경쟁 방법론 비교가 보완되면 더욱 균형 잡힌 survey가 될 것이다.
