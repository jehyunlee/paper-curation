# A Survey on Uncertainty Quantification Methods for Deep Learning

> **저자**: Wenchong He, Zhe Jiang, Tingsong Xiao, Zelin Xu, Yukun Li | **날짜**: 2023 | **Link**: [https://arxiv.org/abs/2302.13425](https://arxiv.org/abs/2302.13425)

---

## Essence

DNN의 uncertainty quantification(UQ) 방법론을 uncertainty source(data uncertainty vs model uncertainty)에 기반하여 체계적으로 분류하는 새로운 taxonomy를 제시하는 survey이다. 기존 survey가 network architecture나 Bayesian formulation 중심이었던 반면, 실제 적용 시 적절한 UQ 방법 선택을 용이하게 하는 실용적 관점을 제공한다.

## Motivation

- **알려진 것**: DNN이 CV, NLP, 과학/공학 분야에서 큰 성공을 거두었으나, 예상치 못한 고확신 오류 예측이 high-stakes 응용에서 심각한 결과 초래
- **Gap**: 기존 UQ survey들은 neural network architecture나 Bayesian formulation으로 분류하여, 각 방법이 다루는 uncertainty source를 파악하기 어려움
- **왜 중요한가**: 적절한 UQ 방법 선택은 자율주행, 의료진단, 재난대응 등 안전 필수 응용에서 필수적
- **접근법**: Uncertainty source (data vs model uncertainty) 기반 taxonomy로 UQ 방법론을 재분류하고 장단점을 체계적으로 비교

## Achievement

1. Uncertainty source 기반의 새로운 UQ 방법론 taxonomy 제시 -- 실무에서의 방법 선택을 직접 지원
2. Data uncertainty와 model uncertainty 각각에 대한 방법론의 장단점을 체계적으로 정리
3. Active learning, OOD robustness, deep RL 등 ML 문제에서의 UQ 적용 사례 종합
4. LLM, AI-driven scientific simulation, structured output DNN을 위한 UQ 연구 방향 제시

## How

- **분류 체계**: Uncertainty source를 기준으로 data uncertainty(aleatoric)와 model uncertainty(epistemic)로 대분류하고, 각각의 세부 방법론 정리
- **방법론 비교**: Bayesian methods, ensemble methods, evidential deep learning, MC Dropout 등의 장단점을 source 관점에서 분석
- **응용 사례**: Active learning, OOD detection, deep RL, scientific computing에서의 UQ 활용을 illustration
- **향후 방향**: LLM uncertainty, AI-driven simulation, structured output에 대한 UQ 연구 필요성 제안

## Originality

- **Source-based Taxonomy**: 기존의 architecture/formulation 중심 분류를 벗어나 uncertainty source 기반으로 재분류한 새로운 시각
- **실용적 방법 선택 가이드**: 연구자와 실무자가 문제의 uncertainty source에 맞는 방법을 선택할 수 있도록 하는 실용적 프레임워크
- **미래 연구 방향 제시**: LLM과 AI-driven scientific simulation에서의 UQ를 핵심 연구 방향으로 선제적 제안

**Abstract에서 추출된 독창성 문장**: To fill this gap, this paper presents a taxonomy of UQ methods for DNNs based on uncertainty sources (e.g., data versus model uncertainty).. We summarize the advantages and disadvantages of each category, and illustrate how UQ can be applied to machine learning problems (e.g., active learning, out-of-distribution robustness, and deep reinforcement learning).. We also identify future research directions, including UQ for large language models (LLMs), AI-driven scientific simulations, and deep neural networks with structured outputs.

## Limitation & Further Study

### 저자들이 언급한 한계

- 빠르게 발전하는 분야로 최신 방법론의 완전한 포괄이 어려움
- 실증적 비교 실험이 아닌 문헌 기반 정리에 한정

### 자체판단 아쉬운 점

- 각 UQ 방법의 computational cost와 scalability에 대한 정량적 비교가 부족
- Calibration quality 등 UQ 성능 평가 메트릭에 대한 체계적 논의가 미흡
- Survey 시점(2023.02) 이후 발전한 conformal prediction, LLM uncertainty 등 최신 동향 반영 부재
- Domain-specific(과학/공학) UQ 적용의 깊이 있는 논의가 상대적으로 부족

### 후속 연구

- LLM hallucination detection을 위한 UQ 방법론 개발
- AI-driven scientific simulation에서의 uncertainty propagation 프레임워크 구축
- Conformal prediction과 기존 UQ 방법의 통합적 비교 연구

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 3/5 |
| Technical Soundness | 4/5 |
| Significance | 4/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: Uncertainty source 기반의 새로운 분류 체계를 통해 DNN UQ 방법론을 실용적 관점에서 정리한 가치 있는 survey이다. 특히 AI for Science 응용에서의 UQ 필요성을 선제적으로 제시한 점이 의미 있으나, 정량적 비교와 최신 동향 반영이 보완되면 더욱 강력할 것이다.
