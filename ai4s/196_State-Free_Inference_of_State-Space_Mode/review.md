# State-Free Inference of State-Space Models: The Transfer Function Approach

> **저자**: Rom N. Parnichkun, Stefano Massaroli, Alessandro Moro, Jimmy T. H. Smith, Ramin Hasani, Mathias Lechner, Qi An, Christopher Ré, Hajime Asama, Stefano Ermon, Taiji Suzuki, Atsushi Yamashita, Michael Poli | **날짜**: 2024 | **Link**: [https://arxiv.org/abs/2405.06147](https://arxiv.org/abs/2405.06147)

---

## Essence

State-space model(SSM)의 dual representation인 transfer function 관점에서 접근하여, state size 증가에 따른 메모리/계산 비용이 없는 state-free inference 알고리즘을 제안한다. Frequency domain parametrization을 통해 단일 FFT로 convolutional kernel spectrum을 직접 계산하며, Long Range Arena에서 S4 대비 평균 35% 학습 속도 향상과 SOTA 성능을 달성했다.

## Motivation

- **알려진 것**: State-space model(S4 등)은 long-range dependency 처리에 효과적이나, 시간 도메인 parametrization으로 인해 state size에 비례하는 계산/메모리 비용 발생
- **Gap**: 기존 SSM의 sequence parallel inference는 state size 증가 시 significant overhead를 수반하여 확장성에 제약
- **왜 중요한가**: State-free inference가 가능하면 SSM의 실용적 적용 범위가 크게 확장되며, attention-free 모델의 효율성 경쟁력 강화
- **접근법**: Transfer function(주파수 도메인) parametrization을 통해 state를 완전히 제거하고, FFT 기반의 효율적 추론 알고리즘 설계

## Achievement

1. State size에 무관한 메모리/계산 비용의 state-free sequence parallel inference 알고리즘 달성
2. Long Range Arena 벤치마크에서 S4 layers 대비 평균 35% 학습 속도 향상
3. Attention-free 접근법 중 state-of-the-art downstream 성능 달성
4. Hyena baseline 대비 language modeling perplexity 개선 -- transfer function parametrization 단순 적용만으로 달성

## How

- **핵심 아이디어**: SSM을 time-domain state representation이 아닌 frequency-domain transfer function으로 parametrize하여 state 개념 자체를 제거
- **FFT 기반 추론**: Transfer function parametrization의 수학적 성질을 활용하여 단일 FFT로 convolutional kernel의 spectrum을 직접 계산
- **실험 설정**: Long Range Arena 벤치마크(다양한 시퀀스 길이/state size)에서 S4 및 기타 attention-free 모델과 비교
- **Language Modeling**: Hyena 아키텍처에 transfer function parametrization을 plug-in으로 적용하여 perplexity 개선 검증

## Originality

- **Transfer Function Parametrization**: SSM을 frequency domain dual representation으로 재해석하여 state 자체를 제거하는 근본적으로 새로운 접근
- **State-Free Inference**: State size에 완전히 독립적인 추론 알고리즘으로, 기존 SSM의 scalability 병목을 원천적으로 해결
- **Plug-in 범용성**: 기존 convolutional 모델(Hyena 등)에 직접 적용 가능한 parametrization으로서의 범용적 가치

**Abstract에서 추출된 독창성 문장**: We approach designing a state-space model for deep learning applications through its dual representation, the transfer function, and uncover a highly efficient sequence parallel inference algorithm that is state-free: unlike other proposed algorithms, state-free inference does not incur any significant memory or computational cost with an increase in state size.. We achieve this using properties of the proposed frequency domain transfer function parametrization, which enables direct computation of its corresponding convolutional kernel's spectrum via a single Fast Fourier Transform.. Our experimental results across multiple sequence lengths and state sizes illustrates, on average, a 35% training speed improvement over S4 layers -- parametrized in time-domain -- on the Long Range Arena benchmark, while delivering state-of-the-art downstream performances over other attention-free approaches.. Moreover, we report improved perplexity in language modeling over a long convolutional Hyena baseline, by simply introducing our transfer function parametrization.. Our code is available at https://github.com/ruke1ire/RTF.

## Limitation & Further Study

### 저자들이 언급한 한계

- 매우 긴 시퀀스(>16K)에서의 성능 및 효율성 검증이 제한적
- Autoregressive generation 시나리오에서의 state-free 접근법 적용에 대한 논의 부족

### 자체판단 아쉬운 점

- Frequency domain parametrization의 수치적 안정성(numerical precision)에 대한 분석이 부족하며, 특히 매우 긴 시퀀스에서 FFT precision 문제 가능성
- 실제 대규모 language model 학습에서의 scalability 검증이 없어, 실용적 적용 가능성 판단이 어려움
- Attention 기반 모델과의 직접 비교가 제한적이며, hybrid architecture에서의 활용 가능성 미탐구

### 후속 연구

- 대규모 language model(GPT 규모)에서의 transfer function parametrization 적용 및 검증
- Autoregressive inference에서의 효율적 state-free generation 알고리즘 개발
- Mamba 등 최신 SSM 변형과의 통합 및 성능 비교

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 4/5 |
| Significance | 3/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: SSM을 transfer function 관점에서 재해석하여 state-free inference를 가능하게 한 이론적으로 elegant한 연구이다. Long-range dependency 처리의 효율성을 근본적으로 개선했으나, 대규모 실용 시나리오에서의 검증이 후속 과제로 남는다.
